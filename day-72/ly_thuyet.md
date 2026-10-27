# Ngày 72 — Lưu và load toàn Spark PipelineModel

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Lưu và load toàn Spark PipelineModel”. Kết quả cần đạt: Có artifact đầy đủ, 120 dòng khi transform toàn snapshot, score tái lập trong tolerance.

## Từ mới gắn với bài này

- **Persistence (lưu trạng thái để dùng lại)**.
- **Artifact (tệp hoặc thư mục đầu ra)**.

## Tình huống và cách hiểu

**Persistence (lưu trạng thái để dùng lại)** giữ các stage đã học, không chỉ hệ số classifier. **Artifact (tệp hoặc thư mục đầu ra)** của Spark thường là một cây thư mục, cần runtime Spark/Java tương thích để load.

Lưu cả schema đầu vào, feature order, data hash và cấu hình. Chỉ có đường dẫn model chưa đủ nếu nội dung đường dẫn bị ghi đè. Dùng version hoặc đích bất biến khi phát hành thật.

Mẫu so score trên fixture trước/sau load trong cùng tiến trình; lab yêu cầu tiến trình mới để không phụ thuộc notebook hay biến còn trong RAM. So bằng sai số số học, không chỉ nhìn một nhãn.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-072/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. `spark` là phiên đã mở và `orders` là tám đơn ở khóa nền; F/Window là API đã học. Các helper sự kiện/feature có code trong course_support.py.

```python
from pyspark.ml import PipelineModel
from pyspark.ml.functions import vector_to_array
train = spark_snapshot(spark)
model = spark_ml_pipeline().fit(train)
path = out / "pipeline"
model.write().overwrite().save(str(path))
loaded = PipelineModel.load(str(path))
print("Đọc lại:", loaded.transform(train.limit(2)).select(vector_to_array("probability")[1].alias("score")).collect())
```

## Đọc từng phần của ví dụ

PipelineModel.load đọc đủ preprocessing. vector_to_array lấy score lớp 1 từ vector Spark.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Có artifact đầy đủ, 120 dòng khi transform toàn snapshot, score tái lập trong tolerance.

## Ba câu kiểm tra hiểu bài

1. Persistence có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: lưu trạng thái để dùng lại.
- Luồng chính: PipelineModel.load đọc đủ preprocessing. vector_to_array lấy score lớp 1 từ vector Spark.
- Đối chiếu tiêu chí: Có artifact đầy đủ, 120 dòng khi transform toàn snapshot, score tái lập trong tolerance. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 12 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
