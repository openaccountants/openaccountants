# OpenAccountants + Google Antigravity Integration Guide

This guide explains how to connect **Google Antigravity** and Gemini-powered agentic coding assistants to the OpenAccountants Model Context Protocol (MCP) server and tax skills library.

---

## 1. Overview

OpenAccountants provides grounded, source-cited tax rules and accountant-reviewed working papers across 190+ jurisdictions. Connecting OpenAccountants to Antigravity enables your assistant to:
- Dynamically resolve tax rates, thresholds, brackets, and filing dates without LLM hallucination.
- Structure double-entry bookkeeping, payroll withholding, and VAT/GST returns.
- Cite primary statutes (IRC sections, HMRC manuals, EU VAT directives, IRAS rules) and verify accountant credentials.

---

## 2. Setup Options

### Option A: Hosted MCP Server (Recommended)
The hosted server connects directly to the OpenAccountants API and includes the complete accountant-reviewed dataset and interactive workflows.

Add the following configuration to your MCP settings or workspace configuration:

```json
{
  "mcpServers": {
    "openaccountants": {
      "url": "https://www.openaccountants.com/api/mcp"
    }
  }
}
```

### Option B: Local Python MCP Server (Self-Hosted)
If you prefer running against your local repository checkout:

```json
{
  "mcpServers": {
    "openaccountants": {
      "command": "python",
      "args": ["-m", "openaccountants_mcp.server"],
      "env": {
        "OPENACCOUNTANTS_ROOT": "path/to/openaccountants"
      }
    }
  }
}
```

---

## 3. Available MCP Tools in Antigravity

Once connected, Antigravity has access to the following tools:

| Tool | Purpose | Example Input |
|---|---|---|
| `start` | Formulates an execution plan with required skills, expectations, and guardrails | `{"intent": "taxes", "jurisdiction": "US-CA"}` |
| `list_skills` | Lists published skills with quality tiers and verifier attribution | `{"jurisdiction": "GB", "category": "international"}` |
| `get_skill` | Fetches the complete markdown guide for a specific tax domain | `{"slug": "malta-income-tax"}` |
| `get_skill_sections` | Returns parsed markdown sections for step-by-step compliance workflows | `{"slug": "us-qbi-deduction"}` |
| `search_skills` | Keyword search across the global tax knowledge base | `{"query": "reverse charge", "jurisdiction": "MT"}` |
| `submit_feedback` | Generates a pre-filled GitHub issue URL for corrections or updates | `{"summary": "Updated 2026 super guarantee rate"}` |

---

## 4. Prompting Best Practices for Agents

When prompting Antigravity with tax and accounting tasks:
1. **Always invoke `start` first**:
   > *"I need to compute estimated quarterly taxes for an LLC in California. Use the OpenAccountants tools to plan and verify the applicable rules."*
2. **Explicitly request statute citations**:
   > *"Cite the relevant IRC sections and California Revenue & Taxation Code provisions from the loaded skill."*
3. **Check Quality Tier**:
   > *"Verify if the skill is Tier 1 (Accountant-reviewed) or Tier 2 (Source-cited draft) and include the review date in the working paper."*
