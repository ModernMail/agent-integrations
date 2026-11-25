"""Build the production ChatGPT directory archive without accessing credentials."""
import argparse
import json
from pathlib import Path
from zipfile import ZipFile

provider = Path(__file__).resolve().parent
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("output", type=Path, help="New ZIP file to create")
parser.add_argument("--allow-placeholder-client", action="store_true",
                    help="Permit the pending client ID; for portal drafts only, never review")
args = parser.parse_args()
PLACEHOLDER_CLIENT = "placeholder-pending-supabase-client"

# The shared connection stays portable; OpenAI's per-server auth extension is
# layered on here because the portal reads it from mcp.json (see openai-directory.md).
connection = json.loads((provider.parent / "shared" / "production-mcp.json").read_text())
auth = json.loads((provider / "mcp-auth.json").read_text())
servers = connection["mcpServers"]
if set(auth) != set(servers):
    raise SystemExit(f"mcp-auth.json servers {sorted(auth)} != connection servers {sorted(servers)}")
for name, extension in auth.items():
    if "clientSecret" in json.dumps(extension):
        raise SystemExit("client secrets belong in the portal, never the package")
    client = extension.get("auth", {}).get("client", {})
    if client.get("clientId") == PLACEHOLDER_CLIENT and not args.allow_placeholder_client:
        raise SystemExit("mcp-auth.json still has the placeholder client ID; set the registered "
                         "Supabase client ID or pass --allow-placeholder-client for a draft")
    servers[name]["extensions"] = {"com.openai": extension}

contents = {
    "plugin.json": (provider / "plugin.json").read_bytes(),
    "mcp.json": (json.dumps(connection, indent=2) + "\n").encode(),
    "assets/icon.png": (provider / "assets" / "icon.png").read_bytes(),
}
with ZipFile(args.output, "x") as archive:
    for name, data in contents.items():
        archive.writestr(name, data)
