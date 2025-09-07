from __future__ import annotations

import json
import tempfile
from pathlib import Path
from typing import Optional

from fastapi import FastAPI, File, Form, HTTPException, UploadFile
from fastapi.responses import JSONResponse

from digitalmeve.generator import generate_meve
from digitalmeve.verifier import verify_meve

# Aligne la version API sur la lib publiée
app = FastAPI(title="DigitalMeve API", version="1.7.1")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/generate")
async def generate(
    file: UploadFile = File(...),
    issuer: Optional[str] = Form(None),
) -> JSONResponse:
    """
    Reçoit un fichier, génère une preuve MEVE, renvoie la preuve (JSON) dans la réponse.
    - Pas d’écriture de sidecar sur disque côté API (MVP stateless).
    """
    try:
        # Sauve l’upload en temporaire (nom conservé pour les métadonnées)
        suffix = Path(file.filename or "").suffix
        tmp_path = Path(tempfile.mkstemp(suffix=suffix)[1])
        tmp_path.write_bytes(await file.read())

        proof = generate_meve(tmp_path, issuer=issuer or "Personal")
        return JSONResponse({"ok": True, "proof": proof})
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/verify")
async def verify(
    # Option 1 : on envoie une preuve JSON brute (Content-Type: application/json)
    proof: Optional[dict] = None,
    # Option 2 : on envoie un fichier .meve.json via multipart/form-data
    file: Optional[UploadFile] = File(None),
    expected_issuer: Optional[str] = Form(None),
) -> JSONResponse:
    """
    Vérifie une preuve :
      - soit via `proof` (JSON) directement,
      - soit via un fichier `*.meve.json` uploadé.
    Renvoie { ok: bool, info: dict }.
    """
    try:
        proof_obj: Optional[dict] = None

        if proof is not None:
            # JSON direct dans le body
            if not isinstance(proof, dict):
                raise ValueError("Invalid JSON for 'proof'")
            proof_obj = proof

        elif file is not None:
            # Fichier uploadé — seulement *.meve.json (MVP)
            filename = file.filename or ""
            if not filename.endswith(".meve.json"):
                raise ValueError("Upload a .meve.json file or provide 'proof' JSON.")
            raw = await file.read()
            try:
                proof_obj = json.loads(raw.decode("utf-8"))
            except Exception:
                raise ValueError("Cannot decode JSON from uploaded .meve.json")

        else:
            raise ValueError("Provide either a 'proof' JSON body or a .meve.json file.")

        ok, info = verify_meve(proof_obj, expected_issuer=expected_issuer)
        return JSONResponse({"ok": ok, "info": info})
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e)})
