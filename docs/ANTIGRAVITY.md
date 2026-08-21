# OpenAccountants for Google Antigravity (AGY)

This guide explains how to connect and use the **OpenAccountants MCP Server** in **Google Antigravity IDE** and with Antigravity agents.

---

## 1. Quick Setup in Antigravity IDE

### Option A: Hosted Connector (Recommended)

In your Antigravity MCP settings or workspace configuration, add the OpenAccountants hosted MCP endpoint:

```json
{
  "mcpServers": {
    "openaccountants": {
      "url": "https://www.openaccountants.com/api/mcp",
      "transport": "streamable-http",
      "description": "Open-source Tax & Accounting Guides reviewed by licensed CPAs/CAs/EAs across 230+ jurisdictions."
    }
  }
}
```

### Option B: Local Python Package (`openaccountants-mcp`)

If you prefer running the MCP server locally against bundled packages:

```bash
pip install openaccountants-mcp
```

Configure the local stdio transport in Antigravity:

```json
{
  "mcpServers": {
    "openaccountants": {
      "command": "python",
      "args": ["-m", "openaccountants_mcp.server"],
      "env": {
        "MCP_TRANSPORT": "stdio"
      }
    }
  }
}
```

---

## 2. Available MCP Tools in Antigravity

| Tool | Purpose |
|---|---|
| `start(intent, jurisdiction)` | **Session Entry Point:** Maps user intent (e.g. `"income tax"`, `"VAT return"`, `"company formation"`) to relevant guide skills, guardrails, and execution plans. |
| `list_skills(jurisdiction, category)` | Discover all available skills, quality tiers (Tier 1 / Tier 2), and named verifiers. |
| `get_skill(slug)` | Fetches a skill's complete markdown, calculation rules, statutory citations, and provenance footer. |
| `get_skill_sections(slug)` | Parses a guide into structured sections (rules, thresholds, examples, working paper templates). |
| `search_skills(query, jurisdiction)` | Full-text search across all accounting rules and pattern libraries. |
| `submit_feedback(summary, ...)` | Generates a pre-filled GitHub issue URL for reporting inaccuracies or proposing rate updates. |

---

## 3. Recommended Antigravity Agent Workflows

### 3-Outcome Transaction Classification System

When processing ledgers, bank exports, or financial statements, instruct Antigravity agents to classify transactions into three explicit categories:

1. **`Classified`** — The rule applies clearly from the verified guide.
2. **`Assumed`** — A conservative default treatment was applied (flagged for accountant review).
3. **`Needs Input`** — Information is missing; prompts the user for clarification.

### Conservative Computation Rule

Antigravity agents must compute tax calculations **strictly using the rates, thresholds, and formulas provided in the loaded skills** — never from parametric memory. When uncertain, default to higher tax or stricter compliance.

---

## 4. Multi-Agent Orchestration Example

For complex workflows (e.g. cross-border restructuring, US multi-state nexus, or corporate tax return assembly), delegate specialized reviews to Antigravity subagents:

```
                  ┌─────────────────────────────────┐
                  │ Antigravity Lead Agent (Router) │
                  └───────────────┬─────────────────┘
                                  │
         ┌────────────────────────┼────────────────────────┐
         ▼                        ▼                        ▼
┌──────────────────┐    ┌──────────────────┐    ┌──────────────────┐
│ Subagent: Intake │    │ Subagent: Rules  │    │ Subagent: Review │
│ Scope validation │    │ Rate calculation │    │ Working paper    │
└──────────────────┘    └──────────────────┘    └──────────────────┘
```

---

## 5. Working Paper Standard Output

Every tax preparation and accounting session in Antigravity culminates in a standardized working paper:

- **Classified Transactions:** Grouped by tax line items and statutory schedules.
- **Computed Working Balances:** All calculations and statutory brackets disclosed.
- **Assumptions & Audit Trail:** Full provenance citing the guide slug and reviewing CPA/CA.
- **Reviewer Sign-off Notice:**
  > *"This working paper was prepared using skills verified by [Verifier Name] at openaccountants.com. Have your qualified accountant review before filing."*
