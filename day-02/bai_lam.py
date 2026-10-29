"""Ngày 02: lọc và tính tổng bằng Python thông thường.
Chạy từ gốc repo: uv run python scripts/run_day.py 02
"""

orders = [
    {"order_id": "O001", "customer_id": "C001", "amount": 100000},
    {"order_id": "O002", "customer_id": "C001", "amount": 200000},
    {"order_id": "O003", "customer_id": "C002", "amount": 50000},
]

# 1. Dự đoán: C002 có O003, tổng tiền 50000.
selected = [order for order in orders if order["customer_id"] == "C002"]
print("Các đơn của C002:", selected)
print("Tổng của C002:", sum(order["amount"] for order in selected))

# 2. >= giữ cả đơn đúng bằng 100000: O001 và O002.
large_order_ids = [order["order_id"] for order in orders if order["amount"] >= 100000]
print("Mã đơn có amount >= 100000:", large_order_ids)

# 3. Thêm vào danh sách trong bộ nhớ, không sửa file dữ liệu nguồn.
orders.append({"order_id": "O004", "customer_id": "C002", "amount": 70000})
total_amount = sum(order["amount"] for order in orders)
print("Tổng sau khi thêm O004:", total_amount)  # 420000

# 4. Viết phép lọc C001 bằng vòng for: vẫn giữ O001 và O002.
selected_with_loop = []
for order in orders:
    if order["customer_id"] == "C001":
        selected_with_loop.append(order)
print("Các đơn của C001, lọc bằng for:", selected_with_loop)
print("Tổng của C001:", sum(order["amount"] for order in selected_with_loop))
