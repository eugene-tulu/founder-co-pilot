#!/usr/bin/env python3
"""cfo.ai MCP client with device-code OAuth (AuthKit).

Usage:
  python scripts/cfoai_mcp.py login     # register client + device code, then you approve in browser
  python scripts/cfoai_mcp.py call TOOL [json-args]
  python scripts/cfoai_mcp.py tools     # list MCP tools

Token is stored at ~/.config/stagezero/cfoai.json (never in the repo).
"""
from __future__ import annotations

import json
import os
import sys
import time
import urllib.request
import urllib.parse
from pathlib import Path

AUTH = "https://complete-cottage-73.authkit.app"
MCP = "https://api.cfo.ai/mcp"
TOKEN_FILE = Path.home() / ".config" / "stagezero" / "cfoai.json"
SCOPE = "openid profile email offline_access"


def http(url: str, data: dict | None = None, headers: dict | None = None, method: str | None = None) -> tuple[int, dict | str]:
    body = json.dumps(data).encode() if data is not None else None
    req = urllib.request.Request(url, data=body, method=method or ("POST" if body else "GET"))
    req.add_header("user-agent", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0 Safari/537.36")
    req.add_header("accept", "application/json")
    for k, v in (headers or {}).items():
        req.add_header(k, v)
    if body:
        req.add_header("content-type", "application/json")
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            raw = resp.read().decode()
            return resp.status, (json.loads(raw) if raw.strip().startswith(("{", "[")) else raw)
    except urllib.error.HTTPError as e:
        raw = e.read().decode()
        try:
            return e.code, json.loads(raw)
        except Exception:
            return e.code, raw


def save_tokens(tok: dict) -> None:
    TOKEN_FILE.parent.mkdir(parents=True, exist_ok=True)
    existing = {}
    if TOKEN_FILE.exists():
        existing = json.loads(TOKEN_FILE.read_text())
    existing.update(tok)
    existing["saved_at"] = int(time.time())
    TOKEN_FILE.write_text(json.dumps(existing, indent=2))
    TOKEN_FILE.chmod(0o600)


def load_tokens() -> dict:
    if not TOKEN_FILE.exists():
        raise SystemExit("not logged in — run: python scripts/cfoai_mcp.py login")
    return json.loads(TOKEN_FILE.read_text())


def login() -> int:
    status, reg = http(f"{AUTH}/oauth2/register", {
        "client_name": "stagezero (neatHack)",
        "grant_types": ["authorization_code", "refresh_token"],
        "token_endpoint_auth_method": "none",
        "redirect_uris": ["http://localhost:8976/callback"],
        "scope": SCOPE,
        "response_types": ["code"],
    })
    if status not in (200, 201):
        raise SystemExit(f"client registration failed ({status}): {reg}")
    client_id = reg["client_id"]
    existing = load_tokens() if TOKEN_FILE.exists() else {}
    if existing.get("client_id"):
        client_id = existing["client_id"]  # reuse registered client

    import base64
    import hashlib
    import secrets
    from http.server import BaseHTTPRequestHandler, HTTPServer

    verifier = base64.urlsafe_b64encode(secrets.token_bytes(48)).decode().rstrip("=")
    challenge = base64.urlsafe_b64encode(hashlib.sha256(verifier.encode()).digest()).decode().rstrip("=")
    state = secrets.token_urlsafe(16)
    q = urllib.parse.urlencode({
        "response_type": "code",
        "client_id": client_id,
        "redirect_uri": "http://localhost:8976/callback",
        "scope": SCOPE,
        "state": state,
        "code_challenge": challenge,
        "code_challenge_method": "S256",
        "resource": MCP,
    })
    url = f"{AUTH}/oauth2/authorize?{q}"
    print(f"\nAPPROVE: {url}\n")
    print("(login in the browser; the redirect lands on localhost:8976 and is captured automatically)\n")
    sys.stdout.flush()

    got: dict[str, str] = {}

    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):  # noqa: N802
            parsed = urllib.parse.urlparse(self.path)
            params = urllib.parse.parse_qs(parsed.query)
            got.update({k: v[0] for k, v in params.items()})
            self.send_response(200)
            self.send_header("content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"<h3>Approved - you can close this tab.</h3>")

        def log_message(self, *args):  # silence
            pass

    server = HTTPServer(("127.0.0.1", 8976), Handler)
    server.timeout = 300
    while "code" not in got and "error" not in got:
        server.handle_request()

    if "error" in got:
        raise SystemExit(f"authorization error: {got}")
    if got.get("state") != state:
        raise SystemExit("state mismatch")

    t_status, res = http(f"{AUTH}/oauth2/token", {
        "grant_type": "authorization_code",
        "code": got["code"],
        "redirect_uri": "http://localhost:8976/callback",
        "client_id": client_id,
        "code_verifier": verifier,
    })
    if t_status != 200:
        raise SystemExit(f"token exchange failed ({t_status}): {res}")
    save_tokens({
        "client_id": client_id,
        "access_token": res["access_token"],
        "refresh_token": res.get("refresh_token"),
        "expires_at": int(time.time()) + res.get("expires_in", 3600),
    })
    print("APPROVED — token saved")
    return 0


def parse_sse(raw: str) -> dict | str:
    """Unwrap text/event-stream frames into the JSON-RPC payload."""
    text = raw.strip()
    if not text.startswith("event:") and not text.startswith("data:"):
        return json.loads(text) if text.strip().startswith(("{", "[")) else raw
    payload: list[str] = []
    for line in text.splitlines():
        if line.startswith("data:"):
            payload.append(line[5:].strip())
    blob = "\n".join(payload)
    try:
        return json.loads(blob)
    except Exception:
        return blob


def mcp_call(tool: str, args: dict | None = None, token: str | None = None) -> dict:
    tok = load_tokens() if token is None else {"access_token": token}
    headers = {
        "authorization": f"Bearer {tok['access_token']}",
        "accept": "application/json, text/event-stream",
        "content-type": "application/json",
    }
    status, res = http(f"{MCP}", {
        "jsonrpc": "2.0", "id": 1, "method": "tools/call",
        "params": {"name": tool, "arguments": args or {}},
    }, headers=headers)
    return {"status": status, "result": parse_sse(res) if isinstance(res, str) else res}


def list_tools() -> int:
    tok = load_tokens()
    headers = {
        "authorization": f"Bearer {tok['access_token']}",
        "accept": "application/json, text/event-stream",
        "content-type": "application/json",
    }
    # initialize first (required handshake)
    http(MCP, {"jsonrpc": "2.0", "id": 0, "method": "initialize",
               "params": {"protocolVersion": "2025-03-26", "capabilities": {},
                          "clientInfo": {"name": "stagezero", "version": "0.1"}}}, headers=headers)
    status, res = http(MCP, {"jsonrpc": "2.0", "method": "notifications/initialized"}, headers=headers)
    status, res = http(MCP, {"jsonrpc": "2.0", "id": 2, "method": "tools/list", "params": {}}, headers=headers)
    parsed = parse_sse(res) if isinstance(res, str) else res
    print(json.dumps(parsed))
    return 0


def main() -> int:
    if len(sys.argv) < 2 or sys.argv[1] not in {"login", "tools", "call"}:
        print(__doc__)
        return 1
    cmd = sys.argv[1]
    if cmd == "login":
        return login()
    if cmd == "tools":
        return list_tools()
    tool = sys.argv[2]
    args = json.loads(sys.argv[3]) if len(sys.argv) > 3 else {}
    out = mcp_call(tool, args)
    print(json.dumps(out, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
