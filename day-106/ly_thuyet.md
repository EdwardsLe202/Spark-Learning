# Ngày 106 — HTTP JSON request và response

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “HTTP JSON request và response”. Kết quả cần đạt: Có contract rõ, chưa coi in JSON là đã có dịch vụ hoạt động.

## Từ mới gắn với bài này

- **HTTP (giao thức yêu cầu và phản hồi)**.
- **Status code (mã trạng thái)**.
- **API contract (hợp đồng giao tiếp)**.

## Tình huống và cách hiểu

**HTTP (giao thức yêu cầu và phản hồi)** cho client gửi request và nhận response. **Status code (mã trạng thái)** nói kết quả xử lý: 2xx thành công, 4xx lỗi đầu vào/quyền, 5xx lỗi hoặc chưa sẵn sàng phía server.

**API contract (hợp đồng giao tiếp)** của predict gồm năm feature và đầu ra score/prediction/version/request_id. JSON hợp lệ về cú pháp chưa chắc đúng kiểu hoặc nghiệp vụ; số đơn âm vẫn cần bị chặn.

Hôm nay chỉ đọc cấu trúc một yêu cầu. Mã khách là metadata nếu endpoint cần truy vết, không tự nhét vào vector model. Không gửi nhãn tương lai trong request inference.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-106/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. Các helper chuẩn bị snapshot/model chỉ chạy khi được gọi, không train hoặc tải model lúc import.

```python
payload = {"events_30d": 2, "spend_30d": 300000, "recency_days": 12, "region": "HN", "plan": "basic"}
serialized = json.dumps(payload)
assert json.loads(serialized) == payload
print({"method": "POST", "path": "/predict", "body": payload, "expected_fields": ["score", "prediction", "model_version", "request_id"]})
```

## Đọc từng phần của ví dụ

JSON serialization giữ cấu trúc dữ liệu; không train hay gọi model ở ví dụ contract này.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Có contract rõ, chưa coi in JSON là đã có dịch vụ hoạt động.

## Ba câu kiểm tra hiểu bài

1. HTTP có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: giao thức yêu cầu và phản hồi.
- Luồng chính: JSON serialization giữ cấu trúc dữ liệu; không train hay gọi model ở ví dụ contract này.
- Đối chiếu tiêu chí: Có contract rõ, chưa coi in JSON là đã có dịch vụ hoạt động. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 21 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
