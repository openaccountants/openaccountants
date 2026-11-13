"""Check an explicitly approved hosted manifest before manual Registry publishing."""
import hashlib
import json
import os
from pathlib import Path
import re
import sys
import unicodedata
from urllib.request import Request, urlopen

MCP_URL = "https://www.openaccountants.com/api/mcp"
NAME = "io.github.openaccountants/openaccountants"
BANNED = re.compile(r"\bverified\s+by\s+licensed\s+accountants\b|\bcertified\b|\baccountant[\s\u2010-\u2015-]+verified\b", re.I)


def validate_manifest(raw: str, approved_sha256: str, source: dict) -> dict:
    if not re.fullmatch(r"[0-9a-f]{64}", approved_sha256):
        raise ValueError("An approved SHA256 is required")
    if hashlib.sha256(raw.encode("utf-8")).hexdigest() != approved_sha256:
        raise ValueError("Manifest differs from the exact approved file")
    value = json.loads(raw)
    if not isinstance(value, dict) or value.get("name") != NAME:
        raise ValueError("Wrong hosted Registry name")
    if not isinstance(value.get("version"), str) or not value["version"] or value["version"] != source.get("version"):
        raise ValueError("Version differs from public mcp/server.json")
    if value.get("remotes") != [{"type": "streamable-http", "url": MCP_URL}] or value.get("packages"):
        raise ValueError("Only the approved hosted endpoint may be published")
    if value.get("repository") != {"url": "https://github.com/openaccountants/openaccountants", "source": "github"}:
        raise ValueError("Wrong source repository")
    description = value.get("description")
    if not isinstance(description, str) or not description.strip() or len(description) > 100 or BANNED.search(unicodedata.normalize("NFKC", description)):
        raise ValueError("Missing, overlong or misleading description")
    return value


def main(output: Path) -> None:
    raw = os.environ["MCP_MANIFEST_JSON"]
    manifest = validate_manifest(raw, os.environ["MCP_APPROVED_SHA256"], json.loads(Path("mcp/server.json").read_text()))
    request = Request(MCP_URL, method="POST", headers={"Content-Type": "application/json", "Accept": "application/json, text/event-stream"}, data=json.dumps({
        "jsonrpc": "2.0", "id": "registry-publish-preflight", "method": "initialize", "params": {
            "protocolVersion": "2025-03-26", "capabilities": {},
            "clientInfo": {"name": "openaccountants-registry-publish-preflight", "version": "1.0.0"},
        },
    }).encode())
    with urlopen(request, timeout=30) as response:
        live = json.load(response)
    if live.get("id") != "registry-publish-preflight" or live.get("error") or live.get("result", {}).get("serverInfo", {}).get("version") != manifest["version"]:
        raise ValueError("Live server does not confirm the approved version")
    output.write_bytes(raw.encode("utf-8"))
    print(f"Approved hosted manifest: {manifest['name']} {manifest['version']}; SHA256 matches; live version matches")


if __name__ == "__main__":
    main(Path(sys.argv[1]))
