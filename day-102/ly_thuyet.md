# Ngày 102 — Release manifest promote và rollback

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Release manifest promote và rollback”. Kết quả cần đạt: Con trỏ cuối về release-v1; có log version và xác nhận API sau restart.

## Từ mới gắn với bài này

- **Release manifest (bản ghi thành phần phát hành)**.
- **Rollback (quay về phiên bản trước)**.
- **Atomic replace (thay con trỏ nguyên tử trên filesystem)**.

## Tình huống và cách hiểu

**Release manifest (bản ghi thành phần phát hành)** nối code, model, schema, config và data. **Rollback (quay về phiên bản trước)** cần artifact cũ và contract còn tương thích. Đổi alias model đơn lẻ chưa đủ nếu preprocessing/schema cũng đổi.

Lab dùng JSON pointer tới đường dẫn model tương đối trong repo. **Atomic replace (thay con trỏ nguyên tử trên filesystem)** giảm trạng thái đọc file nửa chừng trong tình huống local, nhưng chưa thay thế mọi cơ chế deploy phân tán.

API load model trong lifespan nên thay pointer chưa đổi model của process đang sống; cần restart/rollout theo kế hoạch. Luôn kiểm tra /ready và version response sau rollback.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-102/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. Các helper chuẩn bị snapshot/model chỉ chạy khi được gọi, không train hoặc tải model lúc import.

```python
from services.release import promote, rollback
from services.pipeline import run_step
for version in ["release-v1", "release-v2"]:
    run_step("train", version=version)
    run_step("evaluate", version=version)
    print("Promote:", promote(version))
print("Rollback:", rollback())
```

## Đọc từng phần của ví dụ

Promote chỉ nhận candidate đã evaluate accepted. Previous pointer được giữ trước khi đổi current.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Con trỏ cuối về release-v1; có log version và xác nhận API sau restart.

## Ba câu kiểm tra hiểu bài

1. Release manifest có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: bản ghi thành phần phát hành.
- Luồng chính: Promote chỉ nhận candidate đã evaluate accepted. Previous pointer được giữ trước khi đổi current.
- Đối chiếu tiêu chí: Con trỏ cuối về release-v1; có log version và xác nhận API sau restart. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 19 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
