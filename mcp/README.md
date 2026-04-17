# OpenAccountants MCP Server

<!-- mcp-name: io.github.openaccountants/openaccountants-mcp -->

A read-only [Model Context Protocol](https://modelcontextprotocol.io/) server that gives Claude, Cursor, and any MCP client **on-demand access** to 134 countries of open-source tax skills — no manual file uploads.

## Why this exists

Without MCP, using OpenAccountants means downloading a country folder and dragging `.md` files into your LLM by hand, every conversation. With MCP, your AI assistant **discovers and fetches** the right skills automatically:

```
You:    "Help me with my Malta taxes. Here's my bank statement."
          ↓
Claude: calls list_jurisdictions → sees "malta"
Claude: calls list_files("malta") → foundation.md, malta-vat.md, …
Claude: calls get_file("malta", "foundation.md") → full skill in context
Claude: calls get_file("malta", "malta-vat.md") → VAT rules loaded
          ↓
Claude: now processes your bank statement with the right tax rules
```

Install once, configure once — skills are available in every conversation from that point on.

## Tools

| Tool | Description |
|------|-------------|
| `list_jurisdictions` | Returns every country slug that has at least one `.md` skill file under `packages/`. |
| `list_files` | Given a jurisdiction slug (e.g. `malta`), returns the `.md` / `.json` filenames in that package. |
| `get_file` | Given a jurisdiction + filename, returns the full UTF-8 text of that skill file (capped at 2 MB). |

All access is **read-only** and **path-sandboxed** to the `packages/` directory.

## Quick start

### 1. Clone and install

Requires **Python 3.10+**.

```bash
git clone https://github.com/openaccountants/openaccountants.git
cd openaccountants
pip install ./mcp
```

Or with `uv` (recommended):

```bash
uv pip install ./mcp
```

### 2. Connect to your AI client

Pick **one** of the following.

#### Claude Desktop

Add to `~/Library/Application Support/Claude/claude_desktop_config.json` (macOS):

```json
{
  "mcpServers": {
    "openaccountants": {
      "command": "openaccountants-mcp"
    }
  }
}
```

If installed in a virtualenv or with `uv`:

```json
{
  "mcpServers": {
    "openaccountants": {
      "command": "uv",
      "args": ["run", "--directory", "/path/to/openaccountants/mcp", "openaccountants-mcp"]
    }
  }
}
```

#### Cursor

Add to `.cursor/mcp.json` in the project (or via Cursor Settings > MCP):

```json
{
  "mcpServers": {
    "openaccountants": {
      "command": "openaccountants-mcp"
    }
  }
}
```

#### Any other MCP client

Run `openaccountants-mcp` (or `python -m openaccountants_mcp`) as a **stdio** transport server.

### 3. Start chatting

> Help me with my 2025 taxes. Here's my bank statement.

The AI will call the MCP tools behind the scenes to load the right country skills, then classify transactions and produce a working paper — all without you uploading a single file.

## Environment variables

| Variable | Default | Description |
|----------|---------|-------------|
| `OPENACCOUNTANTS_ROOT` | Auto-detected repo root (parent of `mcp/`) | Path to your OpenAccountants checkout. The server reads `$OPENACCOUNTANTS_ROOT/packages/`. |

## What changes vs manual upload

| Before (manual) | After (MCP) |
|------------------|-------------|
| Download folder, upload files by hand | One-time install, always available |
| Pick the right files yourself | Model discovers what's available |
| Repeat for every new conversation | Persistent — server always running |
| Can't easily switch countries mid-chat | Model calls `list_jurisdictions` and pivots |

## Smoke test

Run from the repo root to verify everything works:

```bash
python mcp/smoke_test.py
```

All 14 checks should pass (path safety, tool outputs, jurisdiction count).

## Disclaimer

All skills and outputs are for informational and computational purposes only. Not tax advice. Not a replacement for professional judgment. Content quality is [tiered (Q1-Q5)](../docs/QUALITY-TIERS.md) — most skills are **not** practitioner battle-tested. Always have a qualified professional review before filing.
