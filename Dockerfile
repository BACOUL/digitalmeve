# ---- Build stage (optional, keeps final image slim) ----
FROM python:3.12-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

# System deps (pikepdf: poppler utils & qpdf runtime)
RUN apt-get update && apt-get install -y --no-install-recommends \
    qpdf \
    libjpeg62-turbo \
    zlib1g \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy only deps first (better caching)
COPY requirements-api.txt /app/requirements-api.txt
RUN python -m pip install -U pip && pip install -r requirements-api.txt

# Copy project
COPY . /app

# Install lib in editable mode so API peut importer digitalmeve
RUN pip install -e .

EXPOSE 8000

# Démarre l’API
CMD ["uvicorn", "api.app:app", "--host", "0.0.0.0", "--port", "8000"]
