FROM python:3.12-slim

WORKDIR /app
COPY . .

RUN pip install --no-cache-dir -e . \
    && pip install fastapi uvicorn[standard] python-multipart

EXPOSE 8000

CMD ["uvicorn", "api.app:app", "--host", "0.0.0.0", "--port", "8000"]
