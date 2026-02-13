FROM python:3.11-slim

WORKDIR /app

RUN pip install --no-cache-dir \
    fastapi==0.111.0 \
    uvicorn[standard]==0.30.1 \
    psycopg[binary]==3.2.1 \
    python-dotenv==1.0.1

COPY api /app/api

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--app-dir", "/app/api", "--host", "0.0.0.0", "--port", "8000"]
