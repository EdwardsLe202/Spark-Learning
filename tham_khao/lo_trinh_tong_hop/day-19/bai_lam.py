"""Ngày 19: ví dụ khởi động; đọc thuc_hanh.md rồi hoàn thiện TODO.
Chạy từ repo: python scripts/run_day.py 19
"""
from spark_lab import ROOT, DATA, output_dir

import json
from spark_lab import ROOT, output_dir
manifest = {"code_commit": "DIEN_COMMIT_CUA_BAN", "model_version": "DIEN_VERSION",
            "feature_schema_version": "v1", "environment": "local"}
path = output_dir(19) / "release.json"
path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
print(path)
# TODO: thay giá trị minh họa bằng phiên bản thực tế trước khi gọi đây là release.

# Bài tự làm hôm nay:
# TODO Đọc workflow mẫu `.github/workflows/ci.yml`. Chạy kiểm tra tương đương ở local trước khi đẩy code.
# TODO Sau khi đã có test ngày 16, thêm job CI dùng Python 3.11, Java 17, cài requirements.txt và chạy pytest project. Chạy fixture nhỏ, không cần dataset riêng tư.
# TODO Điền release manifest bằng thông tin thật, lưu hai bản candidate và previous. Mô tả quality gate model và schema.
# TODO Thử phát hành local model candidate, rồi quay về model previous; xác nhận cùng fixture tạo dự đoán tương ứng version cũ.
# TODO Viết sơ đồ quyền cho nguồn chỉ đọc và thư mục prediction chỉ ghi. Nếu chọn cloud, lập kế hoạch và ngân sách riêng trước, không cần deploy trả phí để xong ngày này.
