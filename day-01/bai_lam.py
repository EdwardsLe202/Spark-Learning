"""Ngày 01: đọc bảng, tính tiền và giải thích vai trò của Spark.
Chạy từ gốc repo: uv run python scripts/run_day.py 01
"""

# Một dòng là một đơn hàng; C001 có hai đơn khác nhau.
print("Bảng ban đầu: 3 đơn, 3 cột, 2 khách khác nhau.")
print("Tổng ba đơn:", 100000 + 200000 + 50000)
print("Tổng của C001:", 100000 + 200000)

# 1. Đọc dòng O002.
print("O002: khách C001 mua một đơn trị giá 200000 đồng.")

# 2. C002 chỉ có đơn O003 trong bảng ban đầu.
print("Tổng của C002:", 50000)

# 3. Thêm O004 của C002, không tạo thêm khách mới.
print("Sau khi thêm O004: 4 đơn, vẫn 2 khách.")
print("Tổng tiền mới:", 100000 + 200000 + 50000 + 70000)

# 4. Phân biệt nơi lưu dữ liệu và công cụ xử lý.
print("File đơn hàng lưu mã đơn, mã khách và số tiền.")
print("Spark đọc và xử lý dữ liệu, chẳng hạn lọc đơn theo khách rồi tính tổng.")
