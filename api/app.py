from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import JSONResponse
from pathlib import Path
import shutil
import tempfile

from digitalmeve.generator import generate_meve
from digitalmeve.verifier import verify_meve

app = FastAPI(title="DigitalMeve API", version="1.7.1-dev")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/generate")
async def generate(
    file: UploadFile = File(...),
    issuer: str = Form("Unknown"),
    also_json: bool = Form(False),
):
    tmpdir = Path(tempfile.mkdtemp())
    infile = tmpdir / file.filename

    with open(infile, "wb") as f:
        shutil.copyfileobj(file.file, f)

    proof = generate_meve(infile, issuer=issuer)

    result = {"ok": True, "proof": proof}

    if also_json:
        json_path = infile.with_suffix(infile.suffix + ".meve.json")
        result["json_sidecar"] = str(json_path)

    return JSONResponse(content=result)


@app.post("/verify")
async def verify(file: UploadFile = File(...)):
    tmpdir = Path(tempfile.mkdtemp())
    infile = tmpdir / file.filename

    with open(infile, "wb") as f:
        shutil.copyfileobj(file.file, f)

    result = verify_meve(infile)
    return JSONResponse(content=result)
