"""Ngày 20: ví dụ khởi động; đọc thuc_hanh.md rồi hoàn thiện TODO.
Chạy từ repo: python scripts/run_day.py 20
"""
from spark_lab import ROOT, DATA, output_dir

import json
from spark_lab import output_dir
reference = [0.05, 0.10, 0.20, 0.30]
current = [0.20, 0.35, 0.60, 0.80]
report = {"reference_mean_score": sum(reference)/len(reference),
          "current_mean_score": sum(current)/len(current),
          "labels_available": False,
          "conclusion": "Phân bố score đổi; chưa kết luận chất lượng model."}
(output_dir(20) / "monitoring_demo.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
print(report)

# Bài tự làm hôm nay:
# TODO Lấy snapshot score ngày 18 làm current, chọn reference có cùng contract và lưu hash hai tập.
# TODO Tạo ba bản sao: spend nhân 3, region lạ, thiếu cột events_30d. Kiểm tra schema lỗi phải chặn score, hai trường hợp còn lại tạo cảnh báo phù hợp.
# TODO Tính tỷ lệ thiếu, tỷ lệ category lạ, trung bình/quantile feature và score theo region. Ghi ngưỡng minh họa, không gọi đó là ngưỡng chuẩn.
# TODO Giả lập nhãn đến sau 30 ngày, tính precision/recall trên đúng snapshot. Phân biệt kết luận trước và sau khi có nhãn.
# TODO Viết policy retrain: điều kiện mở điều tra, điều kiện train, chất lượng candidate cần đạt và trường hợp giữ model cũ. Thử một candidate kém và lưu lý do từ chối.
