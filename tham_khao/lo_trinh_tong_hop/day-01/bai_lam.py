"""Bài mẫu ngày 01: đọc dữ liệu và thiết kế luồng dự đoán churn.

Chạy từ gốc repo: python3 scripts/run_day.py 01
Chỉ dùng thư viện chuẩn; sơ đồ là thiết kế, chưa chạy Spark hay train model.
"""
import csv

from spark_lab import DATA, output_dir


# Đây là các giả định của bài mẫu, không phải cấu hình phần cứng đã đo.
TOOL_CHOICES = """1. CSV 20 MB: chọn pandas để khám phá và tổng hợp đơn giản.
   Giả định máy có RAM 8 GB, còn trống 4 GB; cần kết quả trong vài giây.
   Đo bộ nhớ và thời gian thực tế vì dữ liệu khi đọc có thể lớn hơn file CSV.
2. Giao dịch nhiều năm: chọn Spark SQL cho tổng hợp theo khách hàng.
   Giả định dữ liệu 2 TB trên Parquet, máy cá nhân có RAM 16 GB;
   có cluster 4 worker, mỗi worker 16 GB RAM, chạy batch mỗi đêm.
   Mục tiêu hoàn tất trong 2 giờ; cần benchmark để xác nhận tài nguyên đủ.
   Nếu dữ liệu đã ở kho SQL và truy vấn đạt mục tiêu, ưu tiên SQL sẵn có.
3. Sự kiện ứng dụng tới liên tục: Kafka nhận sự kiện, Spark Structured
   Streaming xử lý micro-batch và ghi Parquet/bảng kết quả.
   Giả định 10.000 sự kiện/giây, khoảng 1 KB/sự kiện, giữ Kafka 24 giờ;
   cluster khởi điểm 4 worker x 16 GB RAM, chấp nhận độ trễ 30–60 giây.
   Cần đo backlog, state và độ trễ; xử lý thời gian sự kiện và dữ liệu đến muộn.
   Các con số là giả định để chọn công cụ, chưa phải kết quả benchmark.
"""

PIPELINE = """flowchart TD
    raw["Nguồn: events.csv + customers.csv / CSV, Parquet"]
    validate["Validate và làm sạch / Spark SQL"]
    features["Features lịch sử tại cutoff / Spark SQL → Parquet"]
    labels["Nhãn churn: không có purchase trong 30 ngày tiếp theo / Spark SQL"]
    train["Train theo thời gian / Spark ML hoặc scikit-learn nếu vừa RAM"]
    evaluate["Evaluate trên validation và test / thư viện ML"]
    model["Model được chọn + phiên bản / MLflow và artifact store"]
    batch["Dự đoán batch / Spark ML hoặc Python đọc features"]
    online["Dự đoán online / FastAPI + model và features sẵn có"]
    monitor["Monitor dữ liệu, độ trễ và chất lượng khi có nhãn / Python + dashboard"]
    raw --> validate --> features
    validate --> labels
    features --> train
    labels --> train
    train --> evaluate --> model
    model --> batch
    model --> online
    features --> batch
    features --> online
    batch --> monitor
    online --> monitor
"""

WHY_SMALL_DATA = """Repo dùng dữ liệu nhỏ để người học chạy được trên máy cá nhân.
Thời gian chạy ngắn giúp thử, quan sát lỗi và sửa nhanh hơn.
Với fixture nhỏ, ta có thể tính tay kết quả để đối chiếu phép lọc, join và tổng hợp.
Các nguyên lý như schema, partition, lazy evaluation và shuffle vẫn có thể minh họa bằng dữ liệu nhỏ.
Tuy nhiên, Spark local nhiều luồng chưa chứng minh chương trình chạy trên nhiều máy.
Dữ liệu nhỏ cũng chưa thể hiện đầy đủ chi phí truyền mạng, lệch phân vùng hay thiếu bộ nhớ ở quy mô lớn.
Sau khi hiểu đúng logic, ta cần đo trên dữ liệu và môi trường lớn hơn trước khi kết luận về hiệu năng.
"""


def describe_csv(path):
    """Đếm theo luồng và giữ một dòng mẫu, không nạp cả CSV vào list."""
    with path.open(encoding="utf-8", newline="") as source:
        reader = csv.DictReader(source)
        first_row = next(reader, None)
        row_count = 0 if first_row is None else 1 + sum(1 for _ in reader)
    return (
        f"File: {path}\n"
        f"Số dòng dữ liệu (không tính header): {row_count}\n"
        f"Kích thước trên đĩa: {path.stat().st_size:,} byte\n"
        f"Dòng mẫu (giá trị CSV đang là chuỗi): {first_row}\n"
    )


def main():
    events_path = DATA / "raw" / "events.csv"
    customers_path = DATA / "raw" / "customers.csv"
    tiny_path = DATA / "raw" / "events_tiny.csv"

    report = "\n".join([
        "NGÀY 01 — BÀI MẪU",
        "\n1. ĐỌC DỮ LIỆU THẬT TỪ CSV",
        "Mỗi dòng events là một sự kiện mua hàng của một khách hàng.",
        describe_csv(events_path),
        "Mỗi dòng customers là một khách hàng, kể cả người không giao dịch.",
        describe_csv(customers_path),
        "\n2. CHỌN CÔNG CỤ THEO GIẢ ĐỊNH",
        TOOL_CHOICES,
        "\n3. SƠ ĐỒ THIẾT KẾ (CHƯA TRIỂN KHAI)",
        PIPELINE,
        "Feature chỉ dùng lịch sử sẵn có trước cutoff; nhãn dùng 30 ngày sau cutoff.",
        "Online dùng feature đã tính sẵn hoặc tính từ dữ liệu có sẵn tại lúc dự đoán.",
        "\n4. VÌ SAO DÙNG DỮ LIỆU NHỎ? (7 CÂU)",
        WHY_SMALL_DATA,
        "\n5. BIẾN THỂ: ĐỌC FIXTURE TINY (KỲ VỌNG 4 DÒNG)",
        describe_csv(tiny_path),
        "\n6. BÀI MỞ RỘNG",
        f"1.000.000 dòng × 200 byte = {1_000_000 * 200:,} byte = 200 MB (hệ thập phân).",
        "RAM còn chứa chuỗi/object, index, bảng hash và dữ liệu trung gian của join/sort.",
        "Không thể suy ra RAM cần dùng chỉ từ kích thước file; cần đo khi xử lý.",
        "\nĐã chạy: đọc/đếm CSV và ghi báo cáo bằng Python chuẩn.",
        "Chưa chạy: pandas, Spark, Kafka, train/evaluate, MLflow, API và monitor.",
    ])

    # Chỉ ghi đầu ra vào artifacts, giữ nguyên dữ liệu nguồn trong data/raw.
    destination = output_dir(1)
    (destination / "bao_cao.txt").write_text(report + "\n", encoding="utf-8")
    (destination / "pipeline.mmd").write_text(PIPELINE, encoding="utf-8")
    print(report)
    print("\nĐã lưu báo cáo và sơ đồ tại:", destination)


if __name__ == "__main__":
    main()
