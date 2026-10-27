"""Ngày 02: ví dụ hoàn chỉnh để đọc và chạy.
Chạy từ gốc repo: python scripts/run_day.py 02 --example
"""
orders = [
    {"order_id": "O001", "customer_id": "C001", "amount": 100000},
    {"order_id": "O002", "customer_id": "C001", "amount": 200000},
    {"order_id": "O003", "customer_id": "C002", "amount": 50000},
]
selected = [order for order in orders if order["customer_id"] == "C001"]
print("Các đơn của C001:", selected)
print("Tổng của C001:", sum(order["amount"] for order in selected))
