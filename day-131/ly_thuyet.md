# Ngày 131 — Spark chuẩn bị corpus và embedding theo batch

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Spark chuẩn bị corpus và embedding theo batch”. Kết quả cần đạt: Job manifest không trùng; embedding worker khôi phục có kiểm soát, không nhét API side effect vào UDF.

## Từ mới gắn với bài này

- **Batch embedding (tính vector theo lô)**.
- **Rate limit (giới hạn tần suất)**.
- **Idempotency key (khóa chống lặp)**.

## Tình huống và cách hiểu

Spark có thể làm sạch/dedup metadata hàng loạt, nhưng không nên gọi embedding API tùy tiện trong UDF. Task retry có thể gọi trùng, phát sinh chi phí và khó khôi phục.

**Batch embedding (tính vector theo lô)** dùng manifest ID/hash để chỉ xử lý phần cần, giới hạn kích thước lô và retry hữu hạn. **Rate limit (giới hạn tần suất)** phải xét ở phía ứng dụng/provider; nhiều executor chạy song song không tự tôn trọng tổng quota. **Idempotency key (khóa chống lặp)** chỉ hữu ích nếu đích thực sự hỗ trợ.

Mẫu chỉ dedup chunk nguồn trong Spark. Lab xuất job manifest và dùng worker local/model thật theo batch, lưu hoàn thành theo chunk ID/model revision. Không báo gọi API một lần mỗi dòng là pipeline production.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-131/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. `spark` là phiên đã mở và `orders` là tám đơn ở khóa nền; F/Window là API đã học. Các helper sự kiện/feature có code trong course_support.py.

```python
from rag_support import load_corpus, chunk_documents
chunks = chunk_documents(load_corpus())
rows = [(c["chunk_id"], c["content_hash"], c["text"]) for c in chunks]
df = spark.createDataFrame(rows + rows[:1], "chunk_id string, content_hash string, text string")
clean = df.dropDuplicates(["chunk_id", "content_hash"])
print("Trước/sau:", df.count(), clean.count())
clean.write.mode("overwrite").parquet(str(out / "embedding_jobs"))
```

## Đọc từng phần của ví dụ

Dedup metadata không gọi model. Lô embedding cần version và ledger ngoài bước chuẩn bị này.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Job manifest không trùng; embedding worker khôi phục có kiểm soát, không nhét API side effect vào UDF.

## Ba câu kiểm tra hiểu bài

1. Batch embedding có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: tính vector theo lô.
- Luồng chính: Dedup metadata không gọi model. Lô embedding cần version và ledger ngoài bước chuẩn bị này.
- Đối chiếu tiêu chí: Job manifest không trùng; embedding worker khôi phục có kiểm soát, không nhét API side effect vào UDF. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 25 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
