from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import JSONResponse
from pathlib import Path
import tempfile
import uvicorn

from digitalmeve.generator import generate_meve
from digitalmeve.verifier import verify_meve

app = FastAPI(title="DigitalMeve API", version="1.0.0")


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.post("/generate")
async def generate(
    file: UploadFile = File(...),
    issuer: str = Form("Personal"),
    also_json: bool = Form(False),
):
    with tempfile.TemporaryDirectory() as tmpdir:
        path = Path(tmpdir) / file.filename
        content = await file.read()
        path.write_bytes(content)

        proof = generate_meve(str(path), issuer=issuer)

        if also_json:
            return JSONResponse({"proof": proof})
        return {"ok": True, "subject": proof["subject"]}


@app.post("/verify")
async def verify(proof: dict):
    ok, info = verify_meve(proof)
    return {"ok": ok, "info": info}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
