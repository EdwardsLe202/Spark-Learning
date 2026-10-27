"""Ngày 13: ví dụ khởi động; đọc thuc_hanh.md rồi hoàn thiện TODO.
Chạy từ repo: python scripts/run_day.py 13
"""
from spark_lab import ROOT, DATA, output_dir

# Ví dụ số học độc lập với thư viện metric.
tp, fp, fn, tn = 12, 8, 3, 77
precision = tp / (tp + fp)
recall = tp / (tp + fn)
print({"precision": precision, "recall": recall, "accuracy": (tp + tn) / 100})

# Bài tự làm hôm nay:
# TODO Chạy ví dụ, tính tay ba metric rồi đối chiếu.
# TODO Dùng dữ liệu ngày 11 và pipeline ngày 12, so baseline luôn đoán lớp đa số với regParam=0.01 và 0.1. Giữ nguyên split.
# TODO Dùng BinaryClassificationEvaluator với areaUnderPR; ghi cả confusion matrix tại threshold 0.3, 0.5, 0.7 trên validation. Lấy probability lớp 1 bằng vector_to_array nếu cần.
# TODO Chọn cấu hình/ngưỡng theo chi phí FP và FN bạn tự nêu. Ghi quyết định trước khi chạy test một lần.
# TODO Lưu bảng số lần fit, runtime, metric toàn bộ và metric theo region; ghi nhóm thiếu mẫu.
