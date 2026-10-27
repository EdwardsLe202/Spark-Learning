"""DAG Airflow 3.0.0. Đặt COURSE_PYTHON trỏ tới venv ML của repo."""
from datetime import datetime, timedelta, timezone
from pathlib import Path
import os
import subprocess

from airflow.sdk import dag, task, get_current_context

ROOT = Path(os.environ.get("COURSE_ROOT", Path(__file__).resolve().parents[3]))


@dag(schedule=None, start_date=datetime(2025, 1, 1, tzinfo=timezone.utc), catchup=False,
     max_active_runs=1, params={"snapshot_date": "2025-07-01", "version": "airflow-demo-v1"})
def churn_pipeline():
    @task(retries=1, retry_delay=timedelta(seconds=5), execution_timeout=timedelta(minutes=6))
    def execute(step):
        context = get_current_context()
        params = context["params"]
        python = os.environ.get("COURSE_PYTHON", str(ROOT / ".venv/bin/python"))
        subprocess.run([python, str(ROOT / "services/pipeline.py"), "--step", step,
                        "--snapshot-date", params["snapshot_date"], "--version", params["version"]],
                       cwd=ROOT, check=True, timeout=300)
        return {"step": step, "snapshot_date": params["snapshot_date"], "version": params["version"]}

    validate = execute.override(task_id="validate")("validate")
    features = execute.override(task_id="features")("features")
    train = execute.override(task_id="train")("train")
    evaluate = execute.override(task_id="evaluate")("evaluate")
    score = execute.override(task_id="score")("score")
    validate >> features >> train >> evaluate >> score


churn_pipeline()
