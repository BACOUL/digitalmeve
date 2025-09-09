from fastapi import FastAPI, UploadFile, Form
from fastapi.responses import StreamingResponse, JSONResponse
from typing import Optional
from io import BytesIO
from datetime import datetime, timezone
import hashlib, json, mimetypes

from pypdf import PdfReader, PdfWriter
from PIL import Image, PngImagePlugin

app = FastAPI()

# ---------- Helpers ----------

def sha256_hex(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()

def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

def stringify_canonical(obj) -> str:
    # JSON canonique simple (clés triées)
    def _canon(o):
        if o is None or isinstance(o, (int, float, bool, str)):
            return json.dumps(o, separators=(",", ":"), ensure_ascii=False)
        if isinstance(o, list):
            return "[" + ",".join(_canon(x) for x in o) + "]"
        if isinstance(o, dict):
            keys = sorted(o.keys())
            return "{" + ",".join(json.dumps(k, ensure_ascii=False)+":"+_canon(o[k]) for k in keys) + "}"
        raise TypeError("Unsupported type")
    return _canon(obj)

def clean_none(d):
    if isinstance(d, dict):
        return {k: clean_none(v) for k, v in d.items() if v is not None}
    if isinstance(d, list):
        return [clean_none(x) for x in d]
    return d

def build_proof(name: Optional[str], mime: Optional[str], size: int, sha256: str, issuer_identity: Optional[str]):
    proof = {
        "version": "meve/1",
        "created_at": now_iso(),
        "doc": {
            "name": name or None,
            "mime": mime or None,
            "size": size,
            "sha256": sha256,
            # "preview_b64": "...",  # optionnel
        },
        "issuer": {
            "name": "DigitalMeve",
            "identity": issuer_identity or None,
            "type": "personal",        # le vérif recalcule le badge
            "website": "https://digitalmeve.com",
            "verified_domain": False
        },
        "meta": {}
    }
    return clean_none(proof)

def infer_ext_and_mime(filename: Optional[str], sniff_mime: Optional[str]) -> tuple[str, str]:
    if sniff_mime:
        mime = sniff_mime
    else:
        mime = mimetypes.guess_type(filename or "")[0] or "application/octet-stream"
    ext = (filename or "").split(".")[-1].lower() if filename and "." in filename else {
        "application/pdf": "pdf",
        "image/png": "png"
    }.get(mime, "bin")
    return ext, mime

# ---------- Embedding ----------

def embed_in_pdf(src: bytes, proof_json: str) -> bytes:
    reader = PdfReader(BytesIO(src))
    writer = PdfWriter()
    for page in reader.pages:
        writer.add_page(page)
    # métadonnée personnalisée /MeveProof
    meta = reader.metadata or {}
    meta = {**{k: v for k, v in meta.items() if isinstance(k, str)}, "/MeveProof": proof_json}
    writer.add_metadata(meta)
    out = BytesIO()
    writer.write(out)
    return out.getvalue()

def embed_in_png(src: bytes, proof_json: str) -> bytes:
    with Image.open(BytesIO(src)) as im:
        meta = PngImagePlugin.PngInfo()
        meta.add_itxt("meve_proof", proof_json, lang="", tkey="meve_proof")
        out = BytesIO()
        im.save(out, format="PNG", pnginfo=meta)
        return out.getvalue()

# ---------- Endpoints ----------

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/generate")
async def generate(
    file: UploadFile,
    issuer: Optional[str] = Form(None),
    also_json: Optional[str] = Form(None),  # "1" si l'appelant veut explicitement un sidecar
):
    src_bytes = await file.read()
    size = len(src_bytes)
    ext, mime0 = infer_ext_and_mime(file.filename, file.content_type)
    sha = sha256_hex(src_bytes)

    proof_obj = build_proof(file.filename, mime0, size, sha, issuer)
    proof_json = stringify_canonical(proof_obj)

    # 1) Si output "binaire intégré" possible -> renvoyer name.meve.ext
    try:
        if ext == "pdf" or mime0 == "application/pdf":
            out_bytes = embed_in_pdf(src_bytes, proof_json)
            out_mime = "application/pdf"
            out_name = f"{file.filename.rsplit('.',1)[0]}.meve.pdf"
            return StreamingResponse(
                BytesIO(out_bytes),
                media_type=out_mime,
                headers={"Content-Disposition": f'attachment; filename="{out_name}"'}
            )
        if ext == "png" or mime0 == "image/png":
            out_bytes = embed_in_png(src_bytes, proof_json)
            out_mime = "image/png"
            out_name = f"{file.filename.rsplit('.',1)[0]}.meve.png"
            return StreamingResponse(
                BytesIO(out_bytes),
                media_type=out_mime,
                headers={"Content-Disposition": f'attachment; filename="{out_name}"'}
            )
    except Exception as e:
        # si l'intégration échoue, on passe au sidecar
        pass

    # 2) Fallback / ou output sidecar explicite : renvoie le JSON de preuve
    return JSONResponse(content={"ok": True, "proof": json.loads(proof_json)})
