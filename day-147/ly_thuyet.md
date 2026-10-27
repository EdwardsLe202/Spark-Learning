# Ngày 147 — Dataset instruction và chống contamination

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Dataset instruction và chống contamination”. Kết quả cần đạt: Có dataset và split manifest sạch, không chỉ hai dòng ví dụ trong mẫu.

## Từ mới gắn với bài này

- **Instruction dataset (tập ví dụ hướng dẫn)**.
- **Contamination (nhiễm dữ liệu test vào train)**.
- **Data rights (quyền sử dụng dữ liệu)**.

## Tình huống và cách hiểu

**Instruction dataset (tập ví dụ hướng dẫn)** cần input/output đúng và **data rights (quyền sử dụng dữ liệu)** rõ. **Contamination (nhiễm dữ liệu test vào train)** có thể qua bản paraphrase gần trùng, không chỉ cùng dòng text.

Tách theo nhóm/tài liệu phù hợp trước khi tạo nhiều biến thể. Không lấy câu test RAG rồi cho model tạo đáp án để thêm vào train. Giữ test độc lập với chọn checkpoint và lọc ví dụ.

Mẫu phát hiện trùng text bằng hash. Nó chỉ bắt exact duplicate, chưa bắt gần giống; lab đọc/so semantic và gán group_id. Chất lượng nhãn quan trọng hơn tăng số ví dụ một cách tự động.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-147/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. Các helper chuẩn bị snapshot/model chỉ chạy khi được gọi, không train hoặc tải model lúc import.

```python
import hashlib
rows = [{"group_id": "g1", "instruction": "Trả JSON", "input": "Đơn A01", "output": '{"order_id":"A01"}'}, {"group_id": "g1", "instruction": "Trả JSON", "input": "Đơn A01", "output": '{"order_id":"A01"}'}]
keys = [hashlib.sha256(json.dumps(r, sort_keys=True).encode()).hexdigest() for r in rows]
print({"rows": len(rows), "unique_exact": len(set(keys))})
write_json(out / "dataset_example.json", rows[:1])
```

## Đọc từng phần của ví dụ

Hash của bản giống hệt khớp nhau. Nó không chứng minh hai câu khác chữ không cùng nội dung.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Có dataset và split manifest sạch, không chỉ hai dòng ví dụ trong mẫu.

## Ba câu kiểm tra hiểu bài

1. Instruction dataset có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: tập ví dụ hướng dẫn.
- Luồng chính: Hash của bản giống hệt khớp nhau. Nó không chứng minh hai câu khác chữ không cùng nội dung.
- Đối chiếu tiêu chí: Có dataset và split manifest sạch, không chỉ hai dòng ví dụ trong mẫu. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 29 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
