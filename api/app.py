from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import JSONResponse
from digitalmeve.generator import generate_meve
from digitalmeve.verifier import verify_identity

app = FastAPI(title="DigitalMeve API", version="1.7.1-dev")


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.post("/generate")
async def generate(
    file: UploadFile = File(...),
    issuer: str = Form("Personal"),
    also_json: bool = Form(False),
):
    """
    Generate a MEVE proof for the uploaded file.
    """
    contents = await file.read()
    proof = generate_meve(contents, issuer=issuer)

    response = {"proof": proof}
    if also_json:
        response["sidecar"] = f"{file.filename}.meve.json"
    return JSONResponse(response)


@app.post("/verify")
async def verify(proof: dict):
    """
    Verify a MEVE proof.
    """
    result = verify_identity(proof)
    return JSONResponse(result)
