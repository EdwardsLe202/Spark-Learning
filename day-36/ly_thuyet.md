# Ngày 36 — Repartition coalesce và file đầu ra

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Repartition coalesce và file đầu ra”. Kết quả cần đạt: Mỗi đích 8 dòng và tổng 1400000; có ghi số file quan sát.

## Từ mới gắn với bài này

- **Coalesce (gộp giảm partition)**.
- **Small files (nhiều tệp nhỏ)**.

## Tình huống và cách hiểu

Bạn đã biết repartition chia lại dữ liệu. **Coalesce (gộp giảm partition)** thường giảm số phần mà không shuffle đầy đủ như repartition; nó có thể giữ lại mất cân bằng. Không tăng số phần bằng coalesce để thay repartition.

**Small files (nhiều tệp nhỏ)** gây chi phí liệt kê, mở và lập lịch. Ghi mọi dữ liệu về một file cũng có thể dồn công việc vào một task. Chọn số phần cần xét kích thước thực và cách đọc, không áp một con số cho mọi bảng.

Phân biệt số partition trong thực thi với partitionBy theo giá trị thư mục. Ví dụ chỉ ghi vào đích riêng và đếm part-file. Chưa tuyên bố số file luôn bằng đúng số partition trong mọi định dạng và cấu hình.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-036/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. `spark` là phiên đã mở và `orders` là tám đơn ở khóa nền; F/Window là API đã học. Các helper sự kiện/feature có code trong course_support.py.

```python
df = orders.repartition(4)
for name, part in [("four", df), ("two", df.coalesce(2))]:
    target = out / name
    part.write.mode("overwrite").parquet(str(target))
    print(name, "dòng:", spark.read.parquet(str(target)).count(), "part-file:", len(list(target.glob("part-*"))))
```

## Đọc từng phần của ví dụ

Đích four và two tách nhau. Đọc lại count bảo vệ dữ liệu khi đổi cách chia.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Mỗi đích 8 dòng và tổng 1400000; có ghi số file quan sát.

## Ba câu kiểm tra hiểu bài

1. Coalesce có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: gộp giảm partition.
- Luồng chính: Đích four và two tách nhau. Đọc lại count bảo vệ dữ liệu khi đổi cách chia.
- Đối chiếu tiêu chí: Mỗi đích 8 dòng và tổng 1400000; có ghi số file quan sát. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 08 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
