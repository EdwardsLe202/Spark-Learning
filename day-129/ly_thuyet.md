# Ngày 129 — Embedding thật normalization và model revision

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Embedding thật normalization và model revision”. Kết quả cần đạt: Có vector thật và manifest; chưa tải model thì bài dense chưa hoàn thành.

## Từ mới gắn với bài này

- **Embedding (biểu diễn ngữ nghĩa bằng vector)**.
- **Normalization (chuẩn hóa vector)**.
- **Cosine similarity (độ gần theo góc vector)**.

## Tình huống và cách hiểu

**Embedding (biểu diễn ngữ nghĩa bằng vector)** cần model đã học thật. Vector random hoặc TF-IDF không được coi là dense semantic baseline. **Normalization (chuẩn hóa vector)** giúp dùng tích vô hướng như **cosine similarity (độ gần theo góc vector)** khi norm bằng 1.

Không trộn embedding từ hai model chỉ vì cùng số chiều. Lưu model ID, resolved revision, chiều, normalization và metric cùng index. Đổi model thường cần embed/reindex lại.

Script tải riêng embedding, giữ cache trong artifacts và manifest commit thực. Bài này dùng hai câu tiếng Việt; similarity cao/thấp là quan sát từ model, chưa là bằng chứng ứng dụng tốt. Lab cần truy vấn có nhãn.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-129/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. Các helper chuẩn bị snapshot/model chỉ chạy khi được gọi, không train hoặc tải model lúc import.

```python
from rag_support import embedding_model, model_manifest
import numpy as np
model = embedding_model()
vectors = model.encode(["Spark xử lý bảng dữ liệu", "Đơn hàng có số tiền"], normalize_embeddings=True)
print("Shape:", vectors.shape, "Norm:", np.linalg.norm(vectors, axis=1).tolist())
print(model_manifest("embedding"))
```

## Đọc từng phần của ví dụ

Đây là model thật từ cache, không tự tải khi chạy. Norm gần 1 do normalize_embeddings=True.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Có vector thật và manifest; chưa tải model thì bài dense chưa hoàn thành.

## Ba câu kiểm tra hiểu bài

1. Embedding có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: biểu diễn ngữ nghĩa bằng vector.
- Luồng chính: Đây là model thật từ cache, không tự tải khi chạy. Norm gần 1 do normalize_embeddings=True.
- Đối chiếu tiêu chí: Có vector thật và manifest; chưa tải model thì bài dense chưa hoàn thành. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 25 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
