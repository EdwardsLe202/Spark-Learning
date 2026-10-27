# Ngày 19 — Lý thuyết: CI CD và nền tảng triển khai

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md) · [Thuật ngữ](../docs/THUAT_NGU.md)

Mục tiêu: Có kiểm tra tự động và bản thiết kế release có thể rollback.

## 1. Tách kiểm tra và phát hành
**CI — Continuous Integration (tích hợp liên tục)** chạy kiểm tra khi code thay đổi. **CD — Continuous Delivery/Deployment (chuẩn bị hoặc thực hiện phát hành liên tục)** đưa artifact tới môi trường mục tiêu theo chính sách. Test xanh mới là một điều kiện; chưa tự chứng minh model tốt hơn hay dữ liệu mới đúng.

**Development (môi trường phát triển)** để sửa nhanh, **staging (môi trường kiểm chứng trước phát hành)** mô phỏng điều kiện mục tiêu, **production (môi trường phục vụ thật)** có yêu cầu vận hành. Bài học dùng triển khai local để tránh cần tài khoản trả phí. Ghi rõ phần nào chỉ thiết kế thay vì mô tả như đã chạy cloud.

## 2. Một release cần nhiều phiên bản
**Release manifest (bản ghi các thành phần của một lần phát hành)** nối commit, image tag hoặc digest, model version, feature schema, config và data/index version. **Rollback (quay về phiên bản trước)** cần giữ artifact cũ và contract tương thích; sửa alias đơn lẻ có thể không đủ nếu schema đầu vào đã đổi.

**Client mode (chế độ driver chạy phía máy gửi job)** khác **cluster mode (chế độ driver chạy trong cụm)**. Spark Standalone, YARN và Kubernetes là các lựa chọn quản lý tài nguyên, không phải ba hệ phải học sâu cùng lúc. Chọn một khi thật sự triển khai; local không mô phỏng hết network hoặc permission của cluster.

## 3. Quyền và tài nguyên
**IAM — Identity and Access Management (quản lý danh tính và quyền)** và **service account (danh tính cho ứng dụng)** giúp job chỉ đọc đúng nguồn, ghi đúng đích. **Resource limit (giới hạn tài nguyên)** và **quota (hạn mức sử dụng)** giảm rủi ro chi phí, còn secret phải nằm ngoài Git. Trong CI, dùng fixture nhỏ và không cần tài khoản dữ liệu thật.

## Ví dụ nhỏ để đọc và chạy

Ví dụ Python nằm sẵn trong `bai_lam.py`; xem điều kiện thư viện ở README của ngày.

```python
import json
from spark_lab import ROOT, output_dir
manifest = {"code_commit": "DIEN_COMMIT_CUA_BAN", "model_version": "DIEN_VERSION",
            "feature_schema_version": "v1", "environment": "local"}
path = output_dir(19) / "release.json"
path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
print(path)
# TODO: thay giá trị minh họa bằng phiên bản thực tế trước khi gọi đây là release.
```

## Năm ý đối chiếu với lộ trình gốc

- 19.1 — Local, development, staging và production; client mode và cluster mode.
- 19.2 — Spark Standalone, YARN, Kubernetes; chọn một môi trường để thực hành triển khai.
- 19.3 — Object storage, IAM, service account, network và secret management.
- 19.4 — CI cho test và build; CD cho phát hành có kiểm tra và rollback.
- 19.5 — Version image, model, dữ liệu, cấu hình; resource limit, quota và dự toán chi phí.

Các ý trên giữ phạm vi phần 19 của tài liệu gốc. Phần giải thích và lab là vòng học đầu trong 30 ngày; công nghệ nâng cao được triển khai sâu ở bài mở rộng.

## Câu hỏi tự kiểm tra

1. CI khác CD thế nào?
2. Rollback cần giữ những thành phần nào?
3. Driver ở đâu trong client mode?

## Đọc thêm từ nguồn chính thức

- [Spark deployment overview](https://spark.apache.org/docs/3.5.7/cluster-overview.html)
- [GitHub Actions Python](https://docs.github.com/en/actions/use-cases-and-examples/building-and-testing/building-and-testing-python)

Ưu tiên tài liệu đúng phiên bản đã cài. Mục [nguồn học](../docs/NGUON_HOC.md) ghi bộ phiên bản và phạm vi tham khảo.
