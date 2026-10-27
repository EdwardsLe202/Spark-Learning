# Ngày 125 — Đánh giá prompt bằng tập cố định

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Đánh giá prompt bằng tập cố định”. Kết quả cần đạt: Có bảng đo thật cho hai prompt; fixture minh họa field accuracy=0.75.

## Từ mới gắn với bài này

- **Field accuracy (tỷ lệ trường trích đúng)**.
- **Schema pass rate (tỷ lệ đầu ra đạt schema)**.

## Tình huống và cách hiểu

**Field accuracy (tỷ lệ trường trích đúng)** cần so với nhãn thủ công. **Schema pass rate (tỷ lệ đầu ra đạt schema)** chỉ đo định dạng; không gộp hai chỉ số thành một lời khen model tốt.

Mỗi prompt chạy cùng 10 mẫu, cùng model/revision và budget. Giữ raw output hoặc bản đã che dữ liệu cùng lý do lỗi. Nếu dùng retry, ghi cả số lần gọi để không làm một cấu hình trông rẻ hơn giả.

Mẫu chỉ minh họa cách tính trên nhãn dự đoán cố định. Lab chạy hai prompt bằng adapter thật. Các trường thiếu cần được chấm null đúng theo nguồn, không thưởng vì model đoán may một mã đơn không có bằng chứng.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-125/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. Các helper chuẩn bị snapshot/model chỉ chạy khi được gọi, không train hoặc tải model lúc import.

```python
truth = [{"order_id": "A01", "amount_vnd": 120000}, {"order_id": "B02", "amount_vnd": None}]
predictions = [{"order_id": "A01", "amount_vnd": 120000}, {"order_id": "B02", "amount_vnd": 0}]
correct = sum(pred.get(key) == true[key] for true, pred in zip(truth, predictions) for key in true)
print({"field_accuracy": correct / 4, "source": "fixture_not_llm_benchmark"})
```

## Đọc từng phần của ví dụ

Mẫu thứ hai sai vì 0 không bằng thiếu. Score 0.75 chỉ cho fixture này, không phải model thực.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Có bảng đo thật cho hai prompt; fixture minh họa field accuracy=0.75.

## Ba câu kiểm tra hiểu bài

1. Field accuracy có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: tỷ lệ trường trích đúng.
- Luồng chính: Mẫu thứ hai sai vì 0 không bằng thiếu. Score 0.75 chỉ cho fixture này, không phải model thực.
- Đối chiếu tiêu chí: Có bảng đo thật cho hai prompt; fixture minh họa field accuracy=0.75. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 24 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
