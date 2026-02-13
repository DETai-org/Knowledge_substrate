FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY api /app/api

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--app-dir", "/app/api", "--host", "0.0.0.0", "--port", "8000"]
