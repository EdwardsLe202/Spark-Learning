# Ngày 28 — Đo một thay đổi hiệu năng đơn giản

[Trang ngày](README.md) · [Sang thực hành sau khi đọc](thuc_hanh.md)

**Mục tiêu nhỏ:** Đo phép tính có action, thử cache khi dùng lại và không hứa tăng tốc trên bảng nhỏ.

## 1. Nhanh phải đi kèm đúng

**Baseline (mốc so sánh ban đầu)** gồm code, dữ liệu, cấu hình và thời gian đo. Trước khi so, xác nhận kết quả đúng. Tám dòng quá nhỏ để khẳng định tối ưu nào tốt cho production; mục tiêu hôm nay là biết đo công việc thực sự được chạy.

`perf_counter()` đo thời gian. Phải đặt action bên trong khoảng đo; chỉ đo dòng filter có thể chủ yếu đo lúc xây kế hoạch. **Warm-up (lượt khởi động trước khi đo)** giúp tách khởi tạo ban đầu khỏi các lần đo sau. Ghi từng lần, không chỉ giữ lần đẹp nhất.

## 2. Cache dùng khi tái sử dụng

**Cache (giữ kết quả để tái dùng)** có thể hữu ích khi cùng DataFrame được tính nhiều lần. Cache không miễn phí và thường cần action đầu tiên để vật hóa. Nếu chỉ dùng một lần, chi phí lưu có thể không bù lại.

Sau khi dùng xong gọi unpersist. Khi so có/không cache, ghi cả chi phí vật hóa và điều kiện chạy. Không để cache từ lần trước làm một nhánh được lợi mà vẫn gọi là so công bằng.

## 3. Chấp nhận kết quả không nhanh hơn

Nếu cache chậm hơn trên tám dòng, đó là một kết quả hợp lệ. Bài học là mô tả nguyên nhân có thể và giới hạn đo local. Kỹ thuật broadcast join, skew và UDF được đọc sâu sau khi bạn tự hiểu một phép đo đơn giản.

## Ví dụ có thể chạy nguyên file

Đoạn dưới là phần chính bên trong phiên Spark. [vi_du.py](vi_du.py) có đủ import, mở phiên, dữ liệu và stop để chạy nguyên file. Bảng orders đọc từ [orders.csv](../data/beginner/orders.csv) tám dòng, được giải thích ở ngày 06.

```python
from time import perf_counter
completed = orders.filter(F.col("status") == "completed")
start = perf_counter()
value = completed.agg(F.sum("amount")).first()[0]
print("Tổng:", value, "giây:", perf_counter() - start)
cached = completed.cache()
cached.count()
start = perf_counter()
print("Tổng từ cache:", cached.agg(F.sum("amount")).first()[0], "giây:", perf_counter() - start)
cached.unpersist()
```

## Đọc từng phần của ví dụ

- first là action lấy bảng tổng một dòng, nên khoảng đo có thực thi.
- Count trước lần đo cache làm vật hóa, chi phí này vẫn cần ghi riêng khi so toàn luồng.
- Hai tổng phải cùng 1100000, runtime không có số chuẩn chung.

## Kết quả để đối chiếu

Hai nhánh tổng 1100000. Có thời gian đo thật; không bắt buộc cache nhanh hơn.

## Từ mới cần nhận ra hôm nay

- **Baseline (mốc so sánh ban đầu)**.
- **Cache (giữ kết quả để tái dùng)**.
- **Warm-up (lượt khởi động trước khi đo)**.

Chỉ cần gắn từ với ví dụ trong bài. Chưa cần học thuộc cả [bảng thuật ngữ](../docs/THUAT_NGU.md).

## Ba câu kiểm tra hiểu bài

1. Đo filter chưa có action có đủ không?
2. Cache có chắc nhanh hơn không?
3. Vì sao phải unpersist?

<details>
<summary>Mở sau khi đã tự trả lời</summary>

1. Không đủ để đo toàn phép tính.
2. Không.
3. Giải phóng kết quả đã giữ khi không dùng nữa.

</details>

**Dừng ở đây nếu vẫn chưa rõ đầu vào và kết quả; chưa cần mở ngày sau.** Khi đã hiểu, sang [thực hành](thuc_hanh.md).
