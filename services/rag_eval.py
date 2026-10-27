"""Eval theo query cố định; generation grades cần người học chấm tay."""
from pathlib import Path
from time import perf_counter
import argparse
import json
import sys
import uuid

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import FULL, write_json
from rag_support import eval_queries, load_corpus, chunk_documents, retrieve, doc_ids, retrieval_metrics, rag_answer


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--strategy", choices=["keyword", "sparse", "dense", "hybrid", "reranked"], default="sparse")
    parser.add_argument("--split", choices=["all", "dev", "test"], default="all")
    parser.add_argument("--generation", action="store_true")
    parser.add_argument("--min-score", type=float, help="Chọn trên dev, đúng thang điểm retrieval")
    args = parser.parse_args()
    if args.generation and args.strategy != "dense" and args.min_score is None:
        parser.error("Generation ngoài dense cần --min-score đã chọn trên dev; score các strategy không cùng thang")
    cases = eval_queries(None if args.split == "all" else args.split)
    chunks = chunk_documents(load_corpus())
    out = FULL / "rag-evals" / uuid.uuid4().hex[:10]
    out.mkdir(parents=True)
    rows = []
    for case in cases:
        start = perf_counter()
        row = {"query_id": case["query_id"], "category": case["category"], "split": case["split"],
               "strategy": args.strategy, "expected_behavior": case["expected_behavior"]}
        try:
            ranked = retrieve(case["query"], chunks, role=case["user_role"], k=10, strategy=args.strategy)
            row.update(retrieval_metrics(doc_ids(ranked), case["relevant_doc_ids"], k=3))
            row["retrieved_ids"] = [c["chunk_id"] for c in ranked]
            row["permission_violation"] = any(c["access"] != "public" for c in ranked) if case["user_role"] == "public" else False
            if args.generation:
                row["generation"] = rag_answer(case["query"], role=case["user_role"], k=3,
                    min_score=0.25 if args.min_score is None else args.min_score, strategy=args.strategy)
                row["manual_grade"] = {"correctness": None, "groundedness": None, "citation_support": None, "behavior_correct": None}
            row["status"] = "processed"
        except Exception as error:
            # Giữ ca lỗi trong kết quả và mẫu số, không chỉ giữ câu chạy đẹp.
            row.update({"status": "error", "error": type(error).__name__, "message": str(error)})
            row.update({"recall": 0.0 if case["relevant_doc_ids"] else None, "mrr": 0.0 if case["relevant_doc_ids"] else None, "ndcg": 0.0 if case["relevant_doc_ids"] else None})
        row["total_seconds"] = perf_counter() - start
        rows.append(row)
        print(case["query_id"], row["status"], flush=True)
    (out / "results.jsonl").write_text("\n".join(json.dumps(r, ensure_ascii=False) for r in rows) + "\n", encoding="utf-8")
    labeled = [r for r in rows if r.get("recall") is not None]
    summary = {"cases": len(rows), "errors": sum(r["status"] == "error" for r in rows),
               "labeled_retrieval_cases": len(labeled),
               "mean_recall_at_3": sum(r["recall"] for r in labeled) / len(labeled) if labeled else None,
               "generation_requested": args.generation, "generation_quality": "requires_manual_grading",
               "permission_violations": sum(bool(r.get("permission_violation")) for r in rows)}
    write_json(out / "summary.json", summary)
    print(summary)
    print("Bằng chứng:", out)
    if any(r["status"] == "error" for r in rows):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
