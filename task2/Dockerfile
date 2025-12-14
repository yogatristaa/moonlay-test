FROM python:3.12-slim AS builder

WORKDIR /build

RUN pip install --no-cache-dir \
    --prefix=/install \
    fastapi uvicorn psycopg2-binary


FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1 \
    PATH="/install/bin:$PATH" \
    PYTHONPATH="/install/lib/python3.12/site-packages"

WORKDIR /app

COPY --from=builder /install /install

COPY api.py .

EXPOSE 8000

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
