#!/usr/bin/env python3
"""Valida a cadeia pública mínima antes de liberar um QR do piloto."""

from __future__ import annotations

import argparse
import json
import sys
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


def fetch(base_url: str, path: str) -> tuple[int, str, bytes]:
    request = Request(
        f"{base_url.rstrip('/')}{path}",
        headers={"User-Agent": "phyllos-dpp-pilot-preflight/1.0"},
    )
    with urlopen(request, timeout=20) as response:
        return response.status, response.headers.get_content_type(), response.read()


def validate(base_url: str, dpp_uuid: str) -> dict:
    status_code, status_type, status_body = fetch(base_url, "/api/status")
    status_payload = json.loads(status_body)
    if status_code != 200 or status_payload.get("status") != "ok":
        raise RuntimeError("healthcheck do app não retornou status ok")

    page_code, page_type, page_body = fetch(base_url, f"/p/{dpp_uuid}")
    if page_code != 200 or page_type != "text/html":
        raise RuntimeError("página pública do DPP não retornou HTML 200")
    if b"Passaporte do Produto" not in page_body:
        raise RuntimeError("página pública não contém o marcador do passaporte")

    qr_code, qr_type, qr_body = fetch(base_url, f"/dpp/{dpp_uuid}/qr")
    if qr_code != 200 or qr_type != "image/png" or not qr_body.startswith(b"\x89PNG"):
        raise RuntimeError("endpoint de QR não retornou PNG 200")

    return {
        "status": "ok",
        "base_url": base_url.rstrip("/"),
        "dpp_uuid": dpp_uuid,
        "app_commit": status_payload.get("commit"),
        "public_page": {"status": page_code, "content_type": page_type},
        "qr": {"status": qr_code, "content_type": qr_type, "bytes": len(qr_body)},
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-url", required=True)
    parser.add_argument("--uuid", required=True, dest="dpp_uuid")
    args = parser.parse_args()

    try:
        result = validate(args.base_url, args.dpp_uuid)
    except (HTTPError, URLError, RuntimeError, json.JSONDecodeError) as exc:
        print(json.dumps({"status": "erro", "detail": str(exc)}, ensure_ascii=False))
        return 1

    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
