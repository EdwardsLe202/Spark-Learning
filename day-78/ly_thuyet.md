# Ngày 78 — Artifact sklearn riêng cho API

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Artifact sklearn riêng cho API”. Kết quả cần đạt: Score trước/sau joblib.load tương đương; inference nhánh này không cần Spark.

## Từ mới gắn với bài này

- **Online inference (dự đoán theo yêu cầu)**.
- **Input contract (hợp đồng đầu vào)**.

## Tình huống và cách hiểu

**Online inference (dự đoán theo yêu cầu)** cần runtime nhẹ và đầu vào rõ. Nhánh API trong khóa dùng sklearn Pipeline riêng, còn Spark PipelineModel tiếp tục phục vụ batch. Hai artifact không mặc định thay thế nhau.

**Input contract (hợp đồng đầu vào)** gồm năm cột, kiểu, đơn vị và chính sách thiếu/category mới. Lưu model với metadata và input example. File joblib chỉ load khi do bạn tạo hoặc có nguồn tin cậy, vì deserialization có thể thực thi mã.

Mẫu train/load trong tiến trình hiện tại. Lab dùng script tiến trình mới, không mở SparkSession. Ghi model version và source hash để ngày phục vụ API không mất gốc.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-078/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. Các helper chuẩn bị snapshot/model chỉ chạy khi được gọi, không train hoặc tải model lúc import.

```python
import joblib
model, train, val = fit_sklearn()
path = out / "model.joblib"
joblib.dump(model, path)
loaded = joblib.load(path)
a = model.predict_proba(val[FEATURES].head(3))
b = loaded.predict_proba(val[FEATURES].head(3))
assert np.allclose(a, b)
write_json(out / "metadata.json", {"model_version": "sklearn-demo-v1", "features": FEATURES, "data_hash": data_hash()})
print("Đã lưu và load pipeline sklearn.")
```

## Đọc từng phần của ví dụ

Artifact chứa cả preprocessing. Metadata nói đây là nhánh sklearn, không nhầm với model Spark ngày 72.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Score trước/sau joblib.load tương đương; inference nhánh này không cần Spark.

## Ba câu kiểm tra hiểu bài

1. Online inference có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: dự đoán theo yêu cầu.
- Luồng chính: Artifact chứa cả preprocessing. Metadata nói đây là nhánh sklearn, không nhầm với model Spark ngày 72.
- Đối chiếu tiêu chí: Score trước/sau joblib.load tương đương; inference nhánh này không cần Spark. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 14 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
