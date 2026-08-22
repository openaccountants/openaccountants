# OpenAccountants MCP Server

<!-- mcp-name: io.github.openaccountants/openaccountants-mcp -->

A read-only [Model Context Protocol](https://modelcontextprotocol.io/) server that gives Claude, Cursor, and any MCP client **on-demand access** to 134 countries + 51 US state packages + 13 Canadian provinces/territories of open-source accounting skills across 10 domains (tax, bookkeeping, payroll, e-invoicing, formation, financial statements, transfer pricing, tax optimization, cross-border, and more) — no manual file uploads.

> **Two MCPs, different surfaces.** This **self-hosted server** reads the open-source markdown bundled with the package (or in your local checkout). The **hosted server** at `https://www.openaccountants.com/api/mcp` reads the production database and exposes a larger surface that includes the **accountant-reviewed** tier, the `request_accountant_review` handoff (routes to a named licensed CPA/CA/EA with your working paper attached), `get_rates`, `list_verifiers`, `compare_jurisdictions`, and `plan_cross_border`. The hosted server is the product; this self-hosted one is the open research base.

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
| `_cross-border` | 37 skills — multi-jurisdiction orchestrator, EU rules, OECD treaty defaults, 70+ treaty corridor WHT rates |
| `_verticals` | 14 industry-specific skills — banking, charity / nonprofit, construction, consultant, content creator, e-commerce, freelance developer, insurance, investment funds / REITs, medical, oil & gas, property investor, SaaS, shipping / aviation |
| `_integrations` | 10 platform export formats — Xero, QuickBooks, Stripe, Wise, PayPal, Revolut, Amazon, Shopify, FreeAgent, Sage |

## Tools

The self-hosted server exposes 6 read-only tools below. The hosted server at `https://www.openaccountants.com/api/mcp` is a superset — it adds `get_rates`, `list_jurisdictions`, `list_verifiers`, `compare_jurisdictions`, `plan_cross_border`, and the `request_accountant_review` handoff. Install the hosted MCP if you want the AI-to-human routing; install this one if you want the open research base.

| Tool | Description |
|------|-------------|
| `start` | **Front door.** Call first whenever a user asks for tax/accounting help. Takes optional `intent` (free text — e.g. `"taxes"`, `"VAT return"`, `"set up a company"`) and `jurisdiction` (e.g. `"MT"`, `"GB"`, `"US-CA"`). Returns either a clarification question or a ready-to-execute plan (`skills_to_load`, `expectations`, `next_action`, `guardrails`). |
| `list_skills` | List published skills with quality tier and reviewing accountant. Optional `jurisdiction` (ISO code, e.g. `MT`, `GB`, `US-CA`) and `category` filters. |
| `get_skill` | Given a skill `slug`, returns the full markdown plus a provenance/attribution footer. |
| `get_skill_sections` | Given a `slug`, returns the skill parsed into sections (`heading`, `content`, `level`) for step-by-step application. |
| `search_skills` | Keyword search across skill markdown (`query`, optional `jurisdiction`). Returns the matched section heading and a snippet. |
| `submit_feedback` | Build a pre-filled GitHub New Issue URL the user opens to submit feedback (skill problem, missing jurisdiction, bug, etc.). Takes `summary` plus optional `title`, `skill_slug`, `jurisdiction`, `rating`. Returns `github_url`, `title`, `body`, `labels`. No server-side auth — user submits under their own account. |

Skill access is **read-only** and **path-sandboxed** to the `packages/` directory; `submit_feedback` does not call GitHub itself, it only constructs a URL.

### The `start` flow

`start` is what makes the connector self-guiding. A typical session looks like:

```
User:    "Help me with my Malta taxes."
          ↓
Model:   start(intent="taxes", jurisdiction="MT")
          → { status: "ready",
              skills_to_load: [mt-freelance-intake, malta-income-tax, …],
              expectations: "I'll help you build a working paper for your accountant…",
              next_action: "Run the intake skill first, then classify transactions",
              guardrails: [...] }
          ↓
Model:   get_skill("mt-freelance-intake")  →  scope-check questions
Model:   get_skill("malta-income-tax")     →  rates, brackets, deductions
          ↓
Model:   walks the user through the working paper using the loaded skills
```

If the user only says "help me with my taxes" (no country), call `start(intent="taxes")` — you get back the list of jurisdictions that have a tax skill so you can ask which one applies. Same if only the country is known: `start(jurisdiction="MT")` returns the available categories for Malta.

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

> Note: the on-disk server reads the open-source markdown in `packages/`. Most skill files don't carry a `jurisdiction` field, so it's inherited from the package directory (the folder name for `us-XX`/`ca-XX`, otherwise the code its siblings declare). Quality tier is derived from a file's explicit `tier` frontmatter: only `tier: 1` **plus** a named reviewer (`reviewed_by`, or the legacy `verified_by`) reports as accountant-verified. A reviewer name on its own no longer implies tier 1, and a non-tier-1 file's reviewer is not exposed as `verified_by`.

> **Canadian users on a development (clone) install — important:** the `ca-XX/` provincial packages (`ca-on`, `ca-qc`, `ca-bc`, …) are **generated**, not checked in. After cloning, run `python3 scripts/build-packages.py` once to materialise them. Until you do, the MCP won't return Canadian provincial skills via `list_skills(jurisdiction="CA-ON")` — only the federal Canadian files visible under `packages/canada/`. (The PyPI wheel ships with the packages already built.)

## Quick start

Three ways to install, easiest first.

### Option 1 — Hosted endpoint (1 step, nothing to install)

Point any remote-capable MCP client at:

```
https://www.openaccountants.com/api/mcp
```

That's it. The hosted server is the full product surface (live database, accountant-reviewed tier, `request_accountant_review`, `get_rates`, and more — see the note at the top).

### Option 2 — Install from PyPI (no clone needed)

Requires **Python 3.10+**. The wheel bundles all skill packages — you do not need a checkout of this repo:

```bash
pip install openaccountants-mcp
```

Or run it directly with `uvx`:

```bash
uvx openaccountants-mcp
```

Then connect your AI client (next section) using the `openaccountants-mcp` command.

### Development install (clone the repo)

For contributors, or if you want the server to read your local, editable checkout:

```bash
git clone https://github.com/openaccountants/openaccountants.git
cd openaccountants
pip install ./mcp
```

Or with `uv`:

```bash
uv pip install ./mcp
```

The server reads `packages/` from the repo root (override with `OPENACCOUNTANTS_ROOT`, see environment variables below).

### Connect to your AI client

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

### Start chatting

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
docker run --rm -p 127.0.0.1:8000:8000 -e MCP_HOST=0.0.0.0 openaccountants-mcp
# Point an MCP client at http://localhost:8000/mcp
```

The server itself defaults to the loopback address `127.0.0.1`. Docker's port
forwarder reaches the container through its network interface, so the local-only
Docker example above deliberately sets `MCP_HOST=0.0.0.0` **inside the container**
while binding the published host port to `127.0.0.1`. That keeps the endpoint
available only to local clients.

Remote network binding is an explicit operator choice, not a default:

```bash
MCP_TRANSPORT=streamable-http MCP_HOST=0.0.0.0 openaccountants-mcp
```

This package does not add an authentication layer. Only use a non-loopback
`MCP_HOST` behind an authenticated, TLS-terminating reverse proxy or equivalent
network controls; do not publish the raw MCP endpoint directly to the internet.

When fronted by a reverse proxy that strips an upstream path prefix (e.g. Caddy `uri strip_prefix /oamcp`), set `MCP_STREAMABLE_HTTP_PATH=/` so the endpoint mounts at the proxied root:

```bash
docker run --rm -p 127.0.0.1:8000:8000 \
  -e MCP_HOST=0.0.0.0 \
  -e MCP_STREAMABLE_HTTP_PATH=/ \
  openaccountants-mcp
```

The default stdio transport (`pip install ./mcp && openaccountants-mcp`) is unchanged.

## Environment variables

| Variable | Default | Description |
|----------|---------|-------------|
| `OPENACCOUNTANTS_ROOT` | Auto-detected repo root (parent of `mcp/`) | Path to your OpenAccountants checkout. The server reads `$OPENACCOUNTANTS_ROOT/packages/`. |
| `MCP_TRANSPORT` | `stdio` | `stdio`, `streamable-http`, or `sse`. HTTP transports let remote MCP clients connect via a reverse proxy. |
| `MCP_HOST` | `127.0.0.1` | Bind host for HTTP transports. Set explicitly, for example to `0.0.0.0`, only when an authenticated reverse proxy or equivalent network boundary is intentionally exposing the service. |
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

All skills and outputs are for informational and computational purposes only. Not tax, legal, or financial advice. Not a replacement for professional judgment. Every skill is in one of [two tiers](../docs/QUALITY-TIERS.md) — **accountant-reviewed** (a licensed practitioner reviewed and signed off) or a **source-cited draft** (drafted from authoritative sources, awaiting review). Most skills are source-cited drafts. Always have a qualified professional review before filing or acting upon.
