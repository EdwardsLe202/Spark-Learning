# Ngày 130 — Qdrant local upsert filter delete

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Qdrant local upsert filter delete”. Kết quả cần đạt: API store hoạt động; nghiệm thu semantic retrieval chỉ sau khi dùng embedding thật.

## Từ mới gắn với bài này

- **Vector store (kho tìm vector)**.
- **Payload (metadata kèm vector)**.
- **Upsert (thêm hoặc cập nhật theo ID)**.

## Tình huống và cách hiểu

**Vector store (kho tìm vector)** lưu vector và **payload (metadata kèm vector)**. **Upsert (thêm hoặc cập nhật theo ID)** cần ID ổn định để chạy lại không tạo bản sao.

Qdrant local chạy trong process không cần server cho corpus nhỏ. Đường dẫn store chỉ mở bởi một owner khi có lock; đóng client sau khi dùng. Local mode không chứng minh khả năng chịu tải của server nhiều người dùng.

Mẫu dùng vector hai chiều cố định để học API store, không gọi đó là embedding ngữ nghĩa. Lab thay bằng vector thật ngày 129 và lọc access ở truy vấn trước khi lấy context; thử xóa doc và kiểm tra không còn kết quả.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-130/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. Các helper chuẩn bị snapshot/model chỉ chạy khi được gọi, không train hoặc tải model lúc import.

```python
from qdrant_client import QdrantClient, models
client = QdrantClient(":memory:")
client.create_collection("docs", vectors_config=models.VectorParams(size=2, distance=models.Distance.COSINE))
point = models.PointStruct(id=1, vector=[1.0, 0.0], payload={"doc_id": "doc-spark", "access": "public"})
client.upsert("docs", points=[point])
client.upsert("docs", points=[point])
print("Số point:", client.count("docs").count)
print(client.query_points("docs", query=[1.0, 0.0], query_filter=models.Filter(must=[models.FieldCondition(key="access", match=models.MatchValue(value="public"))]), limit=3).points)
client.delete("docs", points_selector=models.PointIdsList(points=[1]))
assert client.count("docs").count == 0
client.close()
```

## Đọc từng phần của ví dụ

Thai API upsert/query/delete thật với vector fixture. Count=1 sau upsert hai lần, rồi 0 sau delete.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

API store hoạt động; nghiệm thu semantic retrieval chỉ sau khi dùng embedding thật.

## Ba câu kiểm tra hiểu bài

1. Vector store có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: kho tìm vector.
- Luồng chính: Thai API upsert/query/delete thật với vector fixture. Count=1 sau upsert hai lần, rồi 0 sau delete.
- Đối chiếu tiêu chí: API store hoạt động; nghiệm thu semantic retrieval chỉ sau khi dùng embedding thật. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 25 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
