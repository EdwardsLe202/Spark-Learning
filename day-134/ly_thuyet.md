# Ngày 134 — Hybrid search bằng RRF

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Hybrid search bằng RRF”. Kết quả cần đạt: Fixture b xếp đầu; hybrid thật cần dùng hai retrieval thật, không chỉ list viết tay.

## Từ mới gắn với bài này

- **Hybrid search (kết hợp nhiều cách tìm)**.
- **RRF — Reciprocal Rank Fusion (hợp nhất theo nghịch đảo thứ hạng)**.

## Tình huống và cách hiểu

**Hybrid search (kết hợp nhiều cách tìm)** lấy ứng viên từ dense và sparse. Không cộng trực tiếp hai score khác thang. **RRF — Reciprocal Rank Fusion (hợp nhất theo nghịch đảo thứ hạng)** dùng thứ tự của mỗi danh sách.

Mỗi chunk được tính một lần mỗi danh sách, rồi cộng 1/(constant+rank). Khử trùng bằng chunk_id và có tie-breaker ổn định. Không trộn hai index có quyền/version khác nhau mà bỏ kiểm tra.

Ví dụ dùng các ranking fixture để hiểu công thức, không giả làm benchmark model. Lab thay bằng dense/sparse thật của ngày 132–133, chỉ chọn constant/top-k trên dev.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-134/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. Các helper chuẩn bị snapshot/model chỉ chạy khi được gọi, không train hoặc tải model lúc import.

```python
from rag_support import rrf
first = [{"chunk_id": "a", "score": 0.9}, {"chunk_id": "b", "score": 0.8}]
second = [{"chunk_id": "b", "score": 20}, {"chunk_id": "c", "score": 15}]
print(rrf([first, second], k=3))
```

## Đọc từng phần của ví dụ

Score 0.9 và 20 không bị cộng trực tiếp. Chunk b đứng cao do xuất hiện ở cả hai ranking.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Fixture b xếp đầu; hybrid thật cần dùng hai retrieval thật, không chỉ list viết tay.

## Ba câu kiểm tra hiểu bài

1. Hybrid search có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: kết hợp nhiều cách tìm.
- Luồng chính: Score 0.9 và 20 không bị cộng trực tiếp. Chunk b đứng cao do xuất hiện ở cả hai ranking.
- Đối chiếu tiêu chí: Fixture b xếp đầu; hybrid thật cần dùng hai retrieval thật, không chỉ list viết tay. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 26 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
