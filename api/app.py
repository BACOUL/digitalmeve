from __future__ import annotations

import shutil
import tempfile
from pathlib import Path

from fastapi import FastAPI, File, Form, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from digitalmeve.generator import generate_meve
from digitalmeve.verifier import verify_meve

app = FastAPI(title="DigitalMeve API", version="1.7.1")

# CORS ouvert en dev (à restreindre en prod)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.post("/generate")
async def generate(
    file: UploadFile = File(...),
    issuer: str = Form("Personal"),
) -> JSONResponse:
    """
    Upload d’un fichier → renvoie la preuve (dict JSON).
    """
    try:
        tmpdir = Path(tempfile.mkdtemp(prefix="digitalmeve_"))
        infile = tmpdir / (file.filename or "upload.bin")

        with infile.open("wb") as f:
            shutil.copyfileobj(file.file, f)

        proof = generate_meve(infile, issuer=issuer)
        return JSONResponse(content={"ok": True, "proof": proof})
    except Exception as e:  # noqa: BLE001
        raise HTTPException(status_code=400, detail=str(e)) from e


@app.post("/verify")
async def verify(file: UploadFile = File(...)) -> JSONResponse:
    """
    Upload d’un fichier (document ou sidecar .meve.json) → vérification.
    """
    try:
        tmpdir = Path(tempfile.mkdtemp(prefix="digitalmeve_"))
        infile = tmpdir / (file.filename or "upload.bin")

        with infile.open("wb") as f:
            shutil.copyfileobj(file.file, f)

        ok, info = verify_meve(str(infile))
        return JSONResponse(content={"ok": ok, "info": info})
    except Exception as e:  # noqa: BLE001
        raise HTTPException(status_code=400, detail=str(e)) from e


# Optionnel : exécution locale
if __name__ == "__main__":
    import uvicorn

    uvicorn.run("api.app:app", host="127.0.0.1", port=8000, reload=False)
