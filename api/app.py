name: api-smoke

on:
  push:
    paths:
      - "api/**"
      - ".github/workflows/api.yml"
  pull_request:
    paths:
      - "api/**"
      - ".github/workflows/api.yml"

jobs:
  smoke:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install uvicorn fastapi .

      # ✅ Lancer l’API en arrière-plan
      - name: Run API in background
        run: |
          nohup uvicorn api.app:app --host 127.0.0.1 --port 8000 &
          sleep 5

      # ✅ Vérifier le endpoint /health
      - name: Health check
        run: curl -f http://127.0.0.1:8000/health

      # ✅ Arrêter les process (optionnel mais propre)
      - name: Shut down API
        run: pkill -f "uvicorn" || true
