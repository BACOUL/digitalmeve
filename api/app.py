from fastapi import FastAPI, UploadFile, Form
from fastapi.responses import JSONResponse, FileResponse
from pathlib import Path
import tempfile
import shutil
import digitalmeve.generator as generator
import digitalmeve.verifier as verifier

app = FastAPI(title="DigitalMeve API", version="1.7.1-dev")


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.post("/generate")
async def generate(
    file: UploadFile,
    issuer: str = Form("Personal"),
    also_json: bool = Form(False),
):
    tmpdir = Path(tempfile.mkdtemp())
    in_path = tmpdir / file.filename
    with open(in_path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    proof = generator.generate_meve(in_path, issuer=issuer, outdir=tmpdir)

    if also_json:
        return JSONResponse(proof)

    out_path = proof["subject"]["filename"] + ".meve.json"
    return FileResponse(out_path, filename=Path(out_path).name)


@app.post("/verify")
async def verify(file: UploadFile):
    tmpdir = Path(tempfile.mkdtemp())
    in_path = tmpdir / file.filename
    with open(in_path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    ok, info = verifier.verify_meve(in_path)
    return JSONResponse({"ok": ok, "info": info})
