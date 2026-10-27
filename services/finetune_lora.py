"""Nhánh tùy chọn: thí nghiệm LoRA nhỏ, không hứa cải thiện chất lượng.

Model nền phải được tải trước. Dữ liệu mặc định tự tạo chỉ kiểm tra cơ chế.
"""
from pathlib import Path
import argparse
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import FULL, write_json


def main():
    import torch
    from peft import LoraConfig, TaskType, get_peft_model
    from rag_support import generator_components, model_manifest
    parser = argparse.ArgumentParser()
    parser.add_argument("--steps", type=int, default=2)
    parser.add_argument("--data", type=Path, help="JSONL instruction/input/output của train, không lấy từ test")
    args = parser.parse_args()
    if not 1 <= args.steps <= 20:
        parser.error("Smoke lab giới hạn 1..20 step; thiết kế train lớn hơn riêng")
    rows = [{"instruction": "Trả JSON order_id và amount_vnd.", "input": "Đơn A01 có giá 120000 đồng.",
             "output": '{"order_id":"A01","amount_vnd":120000}'}]
    if args.data:
        rows = [json.loads(line) for line in args.data.read_text().splitlines() if line.strip()]
    if not rows or any(set(r) != {"instruction", "input", "output"} for r in rows):
        raise ValueError("Mỗi dòng cần instruction/input/output; dùng dữ liệu train có quyền sử dụng")
    torch.manual_seed(42)
    tokenizer, base = generator_components()
    config = LoraConfig(task_type=TaskType.CAUSAL_LM, r=4, lora_alpha=8, lora_dropout=0.0, target_modules=["q_proj", "v_proj"])
    model = get_peft_model(base, config)
    model.config.use_cache = False
    model.train()
    optimizer = torch.optim.AdamW((p for p in model.parameters() if p.requires_grad), lr=3e-4)
    losses = []
    for step in range(args.steps):
        row = rows[step % len(rows)]
        prefix = tokenizer.apply_chat_template([{"role": "system", "content": row["instruction"]},
                                                {"role": "user", "content": row["input"]}], tokenize=False, add_generation_prompt=True)
        encoded = tokenizer(prefix + row["output"] + tokenizer.eos_token, return_tensors="pt", truncation=True, max_length=128)
        prefix_length = len(tokenizer(prefix, add_special_tokens=False)["input_ids"])
        labels = encoded["input_ids"].clone()
        labels[:, :prefix_length] = -100
        if not (labels != -100).any():
            raise ValueError("Input quá dài, target bị cắt hết; giảm prompt hoặc điều chỉnh budget")
        optimizer.zero_grad()
        loss = model(**encoded, labels=labels).loss
        if not torch.isfinite(loss):
            raise ValueError("Loss không hữu hạn")
        loss.backward()
        optimizer.step()
        losses.append(float(loss.detach()))
        print("step", step + 1, "loss", losses[-1], flush=True)
    out = FULL / "lora-smoke/adapter"
    model.save_pretrained(out, safe_serialization=True)
    tokenizer.save_pretrained(out)
    write_json(out / "course_metadata.json", {"base": model_manifest("generator"), "steps": args.steps, "losses": losses,
               "source": str(args.data) if args.data else "self-authored-smoke-fixture", "quality_claim": "not_evaluated"})
    print("Adapter:", out, "Cần load ở tiến trình mới và đánh giá held-out trước mọi kết luận.")


if __name__ == "__main__":
    main()
