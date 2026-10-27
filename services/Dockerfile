FROM python:3.11-slim-bookworm
WORKDIR /app
COPY requirements-serving.txt .
RUN pip install --no-cache-dir -r requirements-serving.txt
COPY course_support.py .
COPY services ./services
COPY data/raw ./data/raw
EXPOSE 8000
CMD ["python", "-m", "uvicorn", "services.churn_api:app", "--host", "0.0.0.0", "--port", "8000"]
