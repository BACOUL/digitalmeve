# api/app.py
from __future__ import annotations

import json
from typing import Any, Dict, Optional

from fastapi import FastAPI, File, Form, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

# ⚠️ dépend de ton package existant
from digitalmeve.generator import generate_meve
from digitalmeve.verifier import verify_meve

app = FastAPI(
    title="DigitalMeve API", version="1.0.0", docs_url="/docs", redoc_url="/redoc"
)

# CORS (dev: ouvert ; prod: restreindre aux domaines nécessaires)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # TODO: restreindre en prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class HealthResponse(BaseModel):
    status: str = "ok"


class GenerateResponse(BaseModel):
    ok: bool = True
    proof: Dict[str, Any] = Field(default_factory=dict)


class VerifyRequest(BaseModel):
    proof: Optional[Dict[str, Any]] = None
    expected_issuer: Optional[str] = None


class VerifyResponse(BaseModel):
    ok: bool
    info: Dict[str, Any] = Field(default_factory=dict)


@app.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    return HealthResponse()


@app.post("/generate", response_model=GenerateResponse)
async def generate_endpoint(
    file: UploadFile = File(..., description="Fichier à certifier"),
    issuer: str = Form("Personal"),
    metadata: Optional[str] = Form(
        None,
        description='JSON optionnel: ex. {"author":"Alice","project":"X"}',
    ),
) -> GenerateResponse:
    """
    Reçoit un fichier (multipart), calcule la preuve .meve (en mémoire) et renvoie le JSON.
    - issuer: texte libre (ex: "Alice", "alice@company.com")
    - metadata: JSON facultatif (clé/valeur)
    """
    try:
        import tempfile
        from pathlib import Path

        suffix = Path(file.filename or "input.bin").suffix
        with tempfile.NamedTemporaryFile(delete=True, suffix=suffix) as tmp:
            content = await file.read()
            tmp.write(content)
            tmp.flush()

            meta_obj: Dict[str, Any] = {}
            if metadata:
                try:
                    meta_obj = json.loads(metadata)
                    if not isinstance(meta_obj, dict):
                        raise ValueError("metadata must be a JSON object")
                except Exception as e:  # noqa: BLE001
                    raise HTTPException(
                        status_code=400, detail=f"Invalid metadata JSON: {e}"
                    ) from e

            proof = generate_meve(tmp.name, issuer=issuer, metadata=meta_obj)

        return GenerateResponse(ok=True, proof=proof)
    except HTTPException:
        raise
    except Exception as e:  # noqa: BLE001
        raise HTTPException(status_code=500, detail=f"generate failed: {e}") from e


@app.post("/verify", response_model=VerifyResponse)
async def verify_endpoint(
    body: Optional[VerifyRequest] = None,
    proof_file: Optional[UploadFile] = File(
        default=None, description="Optionnel: upload d’un .meve.json"
    ),
) -> VerifyResponse:
    """
    Vérifie une preuve.
    - Cas A: body.proof (dict) est fourni → vérif in-memory
    - Cas B: proof_file (.meve.json) uploadé → vérif à partir du contenu JSON
    """
    try:
        meve_obj: Dict[str, Any]
        expected_issuer: Optional[str] = None

        if body and body.proof:
            if not isinstance(body.proof, dict):
                raise HTTPException(
                    status_code=400, detail="proof must be a JSON object"
                )
            meve_obj = body.proof
            expected_issuer = body.expected_issuer
        elif proof_file is not None:
            raw = await proof_file.read()
            try:
                meve_obj = json.loads(raw.decode("utf-8"))
            except Exception as e:  # noqa: BLE001
                raise HTTPException(
                    status_code=400, detail=f"Invalid JSON in uploaded file: {e}"
                ) from e
        else:
            raise HTTPException(
                status_code=400,
                detail="Missing proof (JSON body or uploaded file)",
            )

        ok, info = verify_meve(meve_obj, expected_issuer=expected_issuer)
        return VerifyResponse(ok=ok, info=info)
    except HTTPException:
        raise
    except Exception as e:  # noqa: BLE001
        raise HTTPException(status_code=500, detail=f"verify failed: {e}") from e
