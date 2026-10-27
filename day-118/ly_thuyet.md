# Ngày 118 — Batching worker cache và backpressure

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Batching worker cache và backpressure”. Kết quả cần đạt: Có đo trước/sau một thay đổi, cache không trả kết quả sai version và không vượt RAM.

## Từ mới gắn với bài này

- **Batching (gom nhiều mẫu)**.
- **Worker (tiến trình phục vụ)**.
- **Backpressure (hạn chế nhận việc khi quá tải)**.

## Tình huống và cách hiểu

**Batching (gom nhiều mẫu)** có thể tăng hiệu suất nhưng thêm thời gian chờ. **Worker (tiến trình phục vụ)** thường load một bản model, nên tăng worker cũng tăng bộ nhớ. **Backpressure (hạn chế nhận việc khi quá tải)** ngăn hàng đợi tăng vô hạn.

Cache prediction cần khóa input chuẩn hóa cùng model version. Nếu không, sau rollout có thể trả score của model cũ. Cache dữ liệu nhạy cảm còn cần quyền và thời gian giữ phù hợp.

Mẫu cho hai khóa cache khác version, không thực hiện benchmark. Lab đổi một yếu tố như số worker hoặc endpoint batch, rồi đo lại cùng dữ liệu và kiểm tra kết quả, RAM và lỗi.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-118/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. Các helper chuẩn bị snapshot/model chỉ chạy khi được gọi, không train hoặc tải model lúc import.

```python
import hashlib
def cache_key(model_version, body):
    payload = json.dumps({"model_version": model_version, "input": body}, sort_keys=True, allow_nan=False)
    return hashlib.sha256(payload.encode()).hexdigest()
body = {"events_30d": 2, "spend_30d": 300000, "region": "HN", "plan": "basic"}
assert cache_key("v1", body) != cache_key("v2", body)
print("Cache key đổi khi model đổi.")
```

## Đọc từng phần của ví dụ

Sort_keys chuẩn hóa thứ tự key JSON. Version là một phần input cache, không lấy alias động mơ hồ.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Có đo trước/sau một thay đổi, cache không trả kết quả sai version và không vượt RAM.

## Ba câu kiểm tra hiểu bài

1. Batching có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: gom nhiều mẫu.
- Luồng chính: Sort_keys chuẩn hóa thứ tự key JSON. Version là một phần input cache, không lấy alias động mơ hồ.
- Đối chiếu tiêu chí: Có đo trước/sau một thay đổi, cache không trả kết quả sai version và không vượt RAM. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 23 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
