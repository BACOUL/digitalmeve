# --- remplace ENTIEREMENT les définitions de cmd_verify et cmd_inspect ---


@cli.command("verify")
@click.argument("proof_path", type=str)  # chaîne brute (plus de Path ici)
@click.option(
    "--issuer", "expected_issuer", default=None, help="Expected issuer to match."
)
def cmd_verify(proof_path: str, expected_issuer: Optional[str]) -> None:
    """Vérifie une preuve (embedded PDF/PNG ou JSON/sidecar)."""
    if not proof_path or not str(proof_path).strip():
        click.echo(json.dumps({"error": "empty-path"}, ensure_ascii=False))
        return

    p = Path(proof_path).resolve()

    obj: Optional[Dict[str, Any]] = _maybe_extract_embedded(p)
    if obj is None:
        obj = _read_json_file(p)
    if obj is None:
        sidecar = _find_sidecar_for(p)
        if sidecar:
            obj = _read_json_file(sidecar)

    if obj is None:
        click.echo(json.dumps({"error": "no-proof"}, ensure_ascii=False))
        return

    ok, info = verify_meve(obj, expected_issuer=expected_issuer)
    if not ok:
        click.echo(
            json.dumps({"error": info.get("error", "invalid")}, ensure_ascii=False)
        )
        return

    click.echo("OK: proof is valid.")
    subj = info.get("subject") or {}
    click.echo(f"subject.filename={subj.get('filename')}")
    click.echo(f"issuer={info.get('issuer')}")


@cli.command("inspect")
@click.argument("proof_path", type=str)  # chaîne brute (plus de Path ici)
def cmd_inspect(proof_path: str) -> None:
    """
    Affiche (JSON pretty) la preuve (embedded/JSON/sidecar).
    Toujours renvoyer un JSON même en cas d’erreur (pour éviter JSONDecodeError).
    """
    try:
        if not proof_path or not str(proof_path).strip():
            click.echo(json.dumps({"error": "empty-path"}, ensure_ascii=False))
            return

        p = Path(proof_path).resolve()

        obj: Optional[Dict[str, Any]] = _maybe_extract_embedded(p)
        if obj is None:
            obj = _read_json_file(p)
        if obj is None:
            sidecar = _find_sidecar_for(p)
            if sidecar:
                obj = _read_json_file(sidecar)

        if obj is None:
            click.echo(json.dumps({"error": "no-proof"}, ensure_ascii=False))
            return

        click.echo(json.dumps(obj, indent=2, ensure_ascii=False))
    except Exception as exc:
        click.echo(
            json.dumps(
                {"error": "inspect-failed", "detail": str(exc)}, ensure_ascii=False
            )
        )
