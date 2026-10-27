# Ngày 41 — JSON struct array map và explode

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “JSON struct array map và explode”. Kết quả cần đạt: Ví dụ có hai dòng item a/b của C001; phân biệt mất dòng với dữ liệu nguồn bị xóa.

## Từ mới gắn với bài này

- **Struct (cấu trúc có trường)**.
- **Array (mảng phần tử)**.
- **Explode (tách phần tử mảng thành dòng)**.

## Tình huống và cách hiểu

JSON có thể chứa object, danh sách và cặp khóa/giá trị. **Struct (cấu trúc có trường)** cho bạn truy cập một trường con; **array (mảng phần tử)** lưu nhiều phần tử cùng kiểu; map lưu khóa và giá trị. Schema tường minh giúp parser giữ kiểu mong muốn.

**Explode (tách phần tử mảng thành dòng)** thay một đơn có hai sản phẩm thành hai dòng sản phẩm. Vì vậy tổng amount của đơn nếu được lặp trên mỗi dòng có thể bị cộng hai lần. Luôn ghi cấp độ của bảng sau explode.

Explode với mảng rỗng/NULL có thể không tạo dòng; explode_outer giữ dòng đại diện thiếu. Chọn theo mục tiêu báo cáo. Hôm nay chỉ đếm phần tử, chưa join sản phẩm vào báo cáo doanh thu mà không kiểm tra.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-041/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. `spark` là phiên đã mở và `orders` là tám đơn ở khóa nền; F/Window là API đã học. Các helper sự kiện/feature có code trong course_support.py.

```python
df = spark.createDataFrame([('{"customer":{"id":"C001"},"items":["a","b"]}',), ('{"customer":{"id":"C002"},"items":[]}',)], "payload string")
parsed = df.select(F.from_json("payload", "customer struct<id:string>, items array<string>").alias("data"))
parsed.select("data.customer.id", F.explode("data.items").alias("item")).show()
```

## Đọc từng phần của ví dụ

from_json parse chuỗi theo schema. C001 sinh hai dòng; C002 mảng rỗng không có dòng từ explode.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Ví dụ có hai dòng item a/b của C001; phân biệt mất dòng với dữ liệu nguồn bị xóa.

## Ba câu kiểm tra hiểu bài

1. Struct có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: cấu trúc có trường.
- Luồng chính: from_json parse chuỗi theo schema. C001 sinh hai dòng; C002 mảng rỗng không có dòng từ explode.
- Đối chiếu tiêu chí: Ví dụ có hai dòng item a/b của C001; phân biệt mất dòng với dữ liệu nguồn bị xóa. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 05 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
