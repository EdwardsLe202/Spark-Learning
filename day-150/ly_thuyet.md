# Ngày 150 — Nghiệm thu toàn lộ trình và demo portfolio

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Nghiệm thu toàn lộ trình và demo portfolio”. Kết quả cần đạt: Có ba dự án nghiệm thu, demo và rubric có dẫn chứng; không tự đánh dấu phần mở rộng chưa chạy.

## Từ mới gắn với bài này

- **Portfolio (bộ dự án minh chứng)**.
- **Rubric (bảng tiêu chí chấm)**.
- **Trade-off (đánh đổi kỹ thuật)**.

## Tình huống và cách hiểu

**Portfolio (bộ dự án minh chứng)** phải có code/test/log/report, không chỉ ảnh giao diện. **Rubric (bảng tiêu chí chấm)** hướng dẫn tự đánh giá, không bảo đảm tuyển dụng. **Trade-off (đánh đổi kỹ thuật)** cần dẫn tới số liệu và giới hạn bạn đã kiểm tra.

Dùng trọng số gốc: Spark 20, thực thi/hiệu năng 15, ML 15, MLOps 20, API 10, RAG/workflow 15, tài liệu 5. Mốc gợi ý 80/100 chưa đủ nếu còn leakage, rerun tạo trùng hoặc sai quyền. Các lỗi nghiêm trọng phải sửa trước.

Demo 10 phút gồm kiến trúc, tính đúng, MLOps/API, RAG và giới hạn. Khi hỏi gấp mười dữ liệu/lưu lượng, nói đo gì đầu tiên thay vì tự hứa tăng tốc tuyến tính. Hoàn thành các phần core theo tiêu chí là hoàn thành phạm vi học của lộ trình; nhánh GPU/cloud/fine-tune chưa chạy phải ghi riêng.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-150/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. Các helper chuẩn bị snapshot/model chỉ chạy khi được gọi, không train hoặc tải model lúc import.

```python
rubric = {"spark_correctness": 20, "execution_performance": 15, "ml_evaluation": 15, "mlops": 20, "api_operations": 10, "rag_workflow": 15, "documentation": 5}
assert sum(rubric.values()) == 100
write_json(out / "rubric.json", rubric)
print(rubric)
print("Checklist cuối:", ROOT / "projects/NGHIEM_THU_TOAN_LO_TRINH.md")
```

## Đọc từng phần của ví dụ

Các số là trọng số rubric gốc, không là điểm tự động đã đạt. Bằng chứng từng mục do bạn điền và giải thích.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Có ba dự án nghiệm thu, demo và rubric có dẫn chứng; không tự đánh dấu phần mở rộng chưa chạy.

## Ba câu kiểm tra hiểu bài

1. Portfolio có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: bộ dự án minh chứng.
- Luồng chính: Các số là trọng số rubric gốc, không là điểm tự động đã đạt. Bằng chứng từng mục do bạn điền và giải thích.
- Đối chiếu tiêu chí: Có ba dự án nghiệm thu, demo và rubric có dẫn chứng; không tự đánh dấu phần mở rộng chưa chạy. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 30 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
