# OpenAccountants MCP Server

<!-- mcp-name: io.github.openaccountants/openaccountants-mcp -->

A read-only [Model Context Protocol](https://modelcontextprotocol.io/) server that gives Claude, Cursor, and any MCP client **on-demand access** to 134 countries + 51 US state packages of open-source accounting skills across 10 domains (tax, bookkeeping, payroll, e-invoicing, formation, financial statements, transfer pricing, tax optimization, cross-border, and more) — no manual file uploads.

## Why this exists

Without MCP, using OpenAccountants means downloading a country folder and dragging `.md` files into your LLM by hand, every conversation. With MCP, your AI assistant **discovers and fetches** the right skills automatically:

```
You:    "Help me set up a company in Malta and understand my tax obligations."
          ↓
Claude: calls list_skills(jurisdiction="MT") → sees malta-formation, malta-vat-return, …
Claude: calls get_skill("malta-formation") → formation rules loaded
Claude: calls get_skill("malta-vat-return") → VAT rules loaded
          ↓
Claude: walks you through entity selection, registration, and tax setup
```

Install once, configure once — skills are available in every conversation from that point on.

US states work the same way:

```
You:    "Help me with my California taxes. Here's my bank statement."
          ↓
Claude: calls list_skills(jurisdiction="US-CA") → federal + CA state skills
Claude: calls get_skill("ca-income-tax") → state rules loaded
          ↓
Claude: now processes with federal AND California rules
```

Special packages are also available:

| Package | What's inside |
|---------|--------------|
| `_cross-border` | Multi-jurisdiction orchestrator, EU rules, OECD treaty defaults, 70+ treaty corridor WHT rates |
| `_verticals` | Industry-specific skills (developer, e-commerce, content creator, consultant, property investor, medical) |
| `_integrations` | Platform export formats (Xero, QuickBooks, Stripe, Wise, PayPal, Revolut, Amazon, Shopify, FreeAgent, Sage) |

## Tools

This server mirrors the hosted server at `https://www.openaccountants.com/api/mcp` so both expose the same surface.

| Tool | Description |
|------|-------------|
| `list_skills` | List published skills with quality tier and verifier. Optional `jurisdiction` (ISO code, e.g. `MT`, `GB`, `US-CA`) and `category` filters. |
| `get_skill` | Given a skill `slug`, returns the full markdown plus a provenance/attribution footer. |
| `get_skill_sections` | Given a `slug`, returns the skill parsed into sections (`heading`, `content`, `level`) for step-by-step application. |
| `search_skills` | Keyword search across skill markdown (`query`, optional `jurisdiction`). Returns the matched section heading and a snippet. |

All access is **read-only** and **path-sandboxed** to the `packages/` directory.

## Prompts

Guided workflows that turn the skills into a tax engine, not just a library:

| Prompt | Arguments | Purpose |
|--------|-----------|---------|
| `tax-return` | `country`, `tax_year`, `entity_type` | Intake → transaction classification → working paper. |
| `vat-check` | `country`, `period` | Classify transactions for VAT/GST and build a return working paper. |
| `find-deductions` | `country`, `entity_type` | Review expenses and surface deductions the taxpayer is missing. |
| `compare-jurisdictions` | `countries`, `income`, `entity_type` | Side-by-side tax comparison for cross-border planning. |
| `skill-feedback` | `skill_slug`, `country` | Collect structured feedback on a skill after use. |
| `skill-review` | `skillSlug`, `scenario` | Load a skill's sections and apply them to one scenario. |

> Note: the on-disk server reads the open-source markdown in `packages/`. Most skill files don't carry a `jurisdiction` field, so it's inherited from the package directory (the folder name for `us-XX`/`ca-XX`, otherwise the code its siblings declare). Quality tier is derived from whether a file names a verifier.

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

or:

> I need to run payroll for my German employee. What are the withholding rates?

or:

> Help me set up a company in Singapore. What are my options?

The AI will call the MCP tools behind the scenes to load the right country and domain skills, then produce working papers, payslips, formation guides, or whatever output matches your request — all without you uploading a single file.

## Docker (local development / self-hosting)

For contributors who'd rather iterate inside a container, the repo root ships a `Dockerfile` that builds the MCP server and runs it under FastMCP's Streamable-HTTP transport:

```bash
docker build -t openaccountants-mcp .
docker run --rm -p 8000:8000 openaccountants-mcp
# Point an MCP client at http://localhost:8000/mcp
```

When fronted by a reverse proxy that strips an upstream path prefix (e.g. Caddy `uri strip_prefix /oamcp`), set `MCP_STREAMABLE_HTTP_PATH=/` so the endpoint mounts at the proxied root:

```bash
docker run --rm -p 8000:8000 -e MCP_STREAMABLE_HTTP_PATH=/ openaccountants-mcp
```

The default stdio transport (`pip install ./mcp && openaccountants-mcp`) is unchanged.

## Environment variables

| Variable | Default | Description |
|----------|---------|-------------|
| `OPENACCOUNTANTS_ROOT` | Auto-detected repo root (parent of `mcp/`) | Path to your OpenAccountants checkout. The server reads `$OPENACCOUNTANTS_ROOT/packages/`. |
| `MCP_TRANSPORT` | `stdio` | `stdio`, `streamable-http`, or `sse`. HTTP transports let remote MCP clients connect via a reverse proxy. |
| `MCP_HOST` | `127.0.0.1` (stdio) / `0.0.0.0` (HTTP) | Bind host for HTTP transports. |
| `MCP_PORT` | `8000` | Bind port for HTTP transports. |
| `MCP_STREAMABLE_HTTP_PATH` | `/mcp` | Path the Streamable-HTTP endpoint is mounted at. Set to `/` when behind a proxy that strips the upstream prefix. |

## What changes vs manual upload

| Before (manual) | After (MCP) |
|------------------|-------------|
| Download folder, upload files by hand | One-time install, always available |
| Pick the right files yourself | Model discovers what's available |
| Repeat for every new conversation | Persistent — server always running |
| Can't easily switch countries mid-chat | Model calls `list_skills` / `search_skills` and pivots |

## Smoke test

Run from the repo root to verify everything works:

```bash
python mcp/smoke_test.py
```

All checks should pass (path safety, tool outputs, jurisdiction count, US state discovery).

## Disclaimer

All skills and outputs are for informational and computational purposes only. Not tax, legal, or financial advice. Not a replacement for professional judgment. Every skill is in one of [two tiers](../docs/QUALITY-TIERS.md) — **accountant-verified** (a licensed practitioner signed off) or **research-verified** (drafted from authoritative sources, awaiting sign-off). Most skills are research-verified. Always have a qualified professional review before filing or acting upon.
