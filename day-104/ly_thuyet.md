# Ngày 104 — Data drift concept drift và nhãn đến trễ

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Data drift concept drift và nhãn đến trễ”. Kết quả cần đạt: Phân biệt thay đổi dữ liệu, lỗi pipeline và suy giảm có nhãn; không auto-retrain theo một số trung bình.

## Từ mới gắn với bài này

- **Data drift (thay đổi phân bố đầu vào)**.
- **Concept drift (thay đổi quan hệ đầu vào và mục tiêu)**.
- **Delayed labels (nhãn đến trễ)**.

## Tình huống và cách hiểu

**Data drift (thay đổi phân bố đầu vào)** không tự chứng minh model kém hơn. **Concept drift (thay đổi quan hệ đầu vào và mục tiêu)** cần bằng chứng phù hợp, thường dựa trên hiệu năng khi có nhãn. **Delayed labels (nhãn đến trễ)** làm kết luận hiện tại có giới hạn.

Churn 30 ngày phải chờ đủ tương lai. Trước đó có thể theo dõi schema, distribution, score và freshness; chưa thể báo precision thực tháng mới nếu chưa có nhãn. Khi nhãn tới, ghép đúng customer/snapshot/model version đã tạo prediction.

Bài so reference/current ở một feature và score, rồi tính metric có nhãn riêng. Không chọn retrain chỉ vì trung bình spend đổi; kiểm tra nguồn, nhóm và tác động trước.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-104/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. Các helper chuẩn bị snapshot/model chỉ chạy khi được gọi, không train hoặc tải model lúc import.

```python
model, train, val = fit_sklearn()
current = val.copy()
current["spend_30d"] *= 3
print({"reference_mean_spend": float(val.spend_30d.mean()), "current_mean_spend": float(current.spend_30d.mean())})
print("Có thay đổi phân bố; chưa đủ để kết luận performance nếu chưa có nhãn current.")
```

## Đọc từng phần của ví dụ

Current là bản sao có thay đổi chủ ý. Mẫu không tạo nhãn giả để khẳng định concept drift.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Phân biệt thay đổi dữ liệu, lỗi pipeline và suy giảm có nhãn; không auto-retrain theo một số trung bình.

## Ba câu kiểm tra hiểu bài

1. Data drift có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: thay đổi phân bố đầu vào.
- Luồng chính: Current là bản sao có thay đổi chủ ý. Mẫu không tạo nhãn giả để khẳng định concept drift.
- Đối chiếu tiêu chí: Phân biệt thay đổi dữ liệu, lỗi pipeline và suy giảm có nhãn; không auto-retrain theo một số trung bình. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 20 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
