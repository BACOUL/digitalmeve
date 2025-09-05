from __future__ import annotations

import json
import os
import tempfile
from pathlib import Path
from typing import Any, Dict, Optional

from fastapi import Depends, FastAPI, File, Form, Header, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

# Librairie cœur
from digitalmeve.generator import generate_meve
from digitalmeve.verifier import verify_meve

# (Présents dans le paquet — utilisables plus tard si tu veux renvoyer des fichiers embarqués)
try:
    from digitalmeve.embedding_pdf import embed_proof_pdf, extract_proof_pdf  # noqa: F401
except Exception:  # pragma: no cover
    embed_proof_pdf = None  # type: ignore[misc,assignment]
    extract_proof_pdf = None  # type: ignore[misc,assignment]

try:
    from digitalmeve.embedding_png import embed_proof_png, extract_proof_png  # noqa: F401
except Exception:  # pragma: no cover
    embed_proof_png = None  # type: ignore[misc,assignment]
    extract_proof_png = None  # type: ignore[misc,assignment]


app = FastAPI(title="DigitalMeve API", version="1.0.0")

# CORS (ouvert en dev ; à restreindre en prod)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # en prod: ["https://ton-domaine.tld", ...]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# --- Sécurité simple par clé API (facultatif) --------------------------------
def require_api_key(x_api_key: Optional[str] = Header(default=None)) -> None:
    """
    Si la variable d'env API_KEY est définie, on exige le header X-API-Key identique.
    Sinon, on n'exige rien (mode dev).
    """
    expected = os.getenv("API_KEY")
    if expected and x_api_key != expected:
        raise HTTPException(status_code=401, detail="Invalid or missing API key")


# --- Routes -------------------------------------------------------------------
@app.get("/health")
def health() -> Dict[str, str]:
    return {"status": "ok"}


@app.post("/generate", dependencies=[Depends(require_api_key)])
async def api_generate(
    file: UploadFile = File(..., description="Fichier source (PDF, PNG, etc.)"),
    issuer: Optional[str] = Form(default=None, description="Émetteur (ex: 'Alice' ou 'Personal')"),
    also_json: bool = Form(default=True, description="Toujours renvoyer la preuve JSON"),
) -> JSONResponse:
    """
    Reçoit un fichier, calcule sa preuve .meve (en mémoire) et renvoie la preuve JSON.
    (Option: plus tard, on pourra renvoyer un fichier embarqué *.meve.pdf/png)
    """
    # 1) Sauvegarder le fichier uploadé dans un fichier temporaire
    suffix = Path(file.filename or "").suffix or ""
    with tempfile.NamedTemporaryFile(suffix=suffix, delete=False) as tmp:
        tmp_path = Path(tmp.name)
        content = await file.read()
        tmp.write(content)

    try:
        # 2) Générer la preuve avec la lib (dictionnaire Python)
        proof = generate_meve(str(tmp_path), issuer=issuer)

        # 3) Réponse JSON standard
        payload: Dict[str, Any] = {
            "ok": True,
            "filename": file.filename,
            "size": len(content),
            "proof": proof,
        }
        return JSONResponse(content=payload, status_code=200)
    finally:
        # Nettoyage du fichier temporaire
        try:
            tmp_path.unlink(missing_ok=True)
        except Exception:
            pass


@app.post("/verify", dependencies=[Depends(require_api_key)])
async def api_verify(
    file: Optional[UploadFile] = File(
        default=None,
        description="Preuve .meve.json à vérifier (sidecar) OU JSON brut",
    ),
    expected_issuer: Optional[str] = Form(
        default=None, description="Émetteur attendu (ex: 'Personal', 'Alice', ...)"
    ),
) -> JSONResponse:
    """
    Vérifie une preuve .meve.
    - Cas 1: chargée depuis un UploadFile (sidecar .meve.json)
    - Cas 2: JSON brut envoyé comme fichier (content-type application/json)
    """
    if not file:
        raise HTTPException(status_code=400, detail="Aucun fichier fourni (attendu: .meve.json)")

    try:
        raw = await file.read()
        # On essaie de charger en JSON ; si ce n’est pas du JSON valide → erreur 400
        proof: Dict[str, Any] = json.loads(raw.decode("utf-8"))
    except Exception as exc:  # JSONDecodeError ou autre
        raise HTTPException(status_code=400, detail=f"Preuve invalide: {exc!s}")

    # Vérification via la lib
    ok, info = verify_meve(proof, expected_issuer=expected_issuer)

    return JSONResponse(
        content={
            "ok": ok,
            "info": info if ok else None,
            "error": None if ok else info,  # la lib renvoie des détails utiles en cas d’échec
        },
        status_code=200,
    )


# --- Démarrage local ----------------------------------------------------------
if __name__ == "__main__":  # pragma: no cover
    import uvicorn

    uvicorn.run("api.app:app", host="127.0.0.1", port=8000, reload=True)
