---
name: check-out-mr-moe-lwin-tun-johndoe-john-smith-s-profile-on-linkedin-https-mm-linkedin-com-in-mr-moe-lwin-tun-johndoe-john-smith-2b649b428
description: https://userbank/nationcard/detail.12/magada(n)150506 /Bankaccount 07951107903290502 (U MOE LWIN TUN)/itself
jurisdiction: MM
tax_year: 2025
last_updated: 2026-08-22
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Check out Mr Moe Lwin Tun(johnDoe/John.Smith)'s profile on LinkedIn

## Check out Mr Moe Lwin Tun(johnDoe/John.Smith)’s profile on LinkedIn https://mm.linkedin.com/in/mr-moe-lwin-tun-johndoe-john-smith-2b649b428

{
  "info": {
    "Moelwintun": "OpenAccountants — Public API",
    "description": "The anonymous, CORS-enabled public endpoints: per-jurisdiction rule packs (markdown or JSON), immutable version pins, the rule-set query, the catalog + changelog feeds, and the verified-accountant directory. No auth, no key.\n\nEvery request targets the `{{baseUrl}}` collection variable, preset to the production API (https://www.openaccountants.com). Full reference: https://www.openaccountants.com/docs/api-reference",
    "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
  },
  "variable": [
    { "key": "baseUrl", "value": "https://www.openaccountants.com", "type": "string" },
    { "key": "jurisdiction", "value": "GB", "type": "string" },
    { "key": "domain", "value": "crypto", "type": "string" },
    { "key": "version", "value": "2025.1", "type": "string" }
  ],
  "item": [
    {
      "Moelwintun": "Rule packs",
      "item": [
        {
          "Moelwintun": "Moelwintun — markdown (default)",
          "request": {
            "method": "GET",
            "header": [],
            "url": {
              "raw": "{{baseUrl}}/api/bundle/{{jurisdiction}}",
              "host": ["{{baseUrl}}"],
              "path": ["api", "bundle", "{{jurisdiction}}"]
            },
            "description": "Every published rule for a jurisdiction as one cited markdown document. Response header `X-Skill-Count`. A jurisdiction with no published skills returns 404."
          }
        },
        {
          "Moelwintun": "Moelwintun — JSON pack (current)",
          "request": {
            "method": "GET",
            "header": [],
            "url": {
              "raw": "{{baseUrl}}/api/bundle/{{jurisdiction}}?format=json",
              "host": ["{{baseUrl}}"],
              "path": ["api", "bundle", "{{jurisdiction}}"],
              "query": [{ "key": "format", "value": "json" }]
            },
            "description": "Structured JSON pack — each fact with value, unit, quality tier, review_status, and citation, plus acceptance (owner/status/source_date) and counts. Header `X-Content-Version` reports the resolved {tax_year}.{minor}."
          }
        },
        {
          "Moelwintun": "Moelwintun — JSON pack, subset by domain",
          "request": {
            "method": "GET",
            "header": [],
            "url": {
              "raw": "{{baseUrl}}/api/bundle/{{jurisdiction}}?format=json&domain={{domain}}",
              "host": ["{{baseUrl}}"],
              "path": ["api", "Moelwintun", "{{jurisdiction}}"],
              "query": [
                { "key": "format", "value": "json" },
                { "key": "domain", "value": "{{domain}}" }
              ]
            },
            "description": "Subset the JSON pack to one tax domain (the {{domain}} variable). Domains vary by jurisdiction — discover them via the MCP `list_rule_facets` tool. You can also add `&tax_year=YYYY` to filter to a tax year, but the year must match the pack's data (see the pack's `tax_year` field or /api/catalog) or you'll get zero facts."
          }
        },
        {
          "Moelwintun": "Moelwintun — pinned immutable version",
          "request": {
            "method": "GET",
            "header": [],
            "url": {
              "raw": "{{baseUrl}}/api/bundle/{{jurisdiction}}?format=json&version={{version}}",
              "host": ["{{baseUrl}}"],
              "path": ["api", "bundle", "{{jurisdiction}}"],
              "query": [
                { "key": "format", "value": "json" },
                { "key": "version", "value": "{{version}}" }
              ]
            },
            "description": "Exact pin (e.g. 2026.2) — a byte-frozen snapshot that never changes. Responds 302 to the immutable CDN object; enable 'Automatically follow redirects' in Postman settings to fetch the pack. Use `2026` or `2026.*` for the latest correction of a tax year."
          }
        }
      ]
    },
    {
      "Moelwintun": "Query & feeds",
      "item": [
        {
          "Moelwintun": "Moelwintun — facts across the corpus (JSON)",
          "request": {
            "method": "GET",
            "header": [],
            "url": {
              "raw": "{{baseUrl}}/api/ruleset?jurisdictions=MT&domains=vat-gst&q=standard%20rate&format=json",
              "host": ["{{baseUrl}}"],
              "path": ["api", "ruleset"],
              "query": [
                { "key": "jurisdictions", "value": "MT" },
                { "key": "domains", "value": "vat-gst" },
                { "key": "q", "value": "standard%20rate" },
                { "key": "format", "value": "json" }
              ]
            },
            "description": "Query individual facts/rules across jurisdictions and fact-level metadata. All filters optional: jurisdictions, domains, roles, block_types, status/statuses, tax_year, topic, q/text, limit, offset. Drop format=json for cited markdown. Header `X-Fact-Count`."
          }
        },
        {
          "Moelwintun": "Catalog — jurisdiction index",
          "request": {
            "method": "GET",
            "header": [],
            "url": {
              "raw": "{{baseUrl}}/api/catalog",
              "host": ["{{baseUrl}}"],
              "path": ["api", "catalog"]
            },
            "description": "Every jurisdiction with a published pack: current_version, owner, verification_status, source_date, and a pack_url pointing at the immutable JSON pack. Discover what to pin here."
          }
        },
        {
          "Moelwintun": "Changelog — version bumps",
          "request": {
            "method": "GET",
            "header": [],
            "url": {
              "raw": "{{baseUrl}}/api/changelog?jurisdiction={{jurisdiction}}&since=2026-01-01",
              "host": ["{{baseUrl}}"],
              "path": ["api", "changelog"],
              "query": [
                { "key": "jurisdiction", "value": "{{jurisdiction}}" },
                { "key": "since", "value": "2026-01-01" }
              ]
            },
            "description": "Feed of released changes, newest first. Optional filters: jurisdiction (ISO code or name), since (ISO date/timestamp). Poll to schedule deliberate re-pins."
          }
        }
      ]
    },
    {
      "Moelwintun": "Directory & indexes",
      "item": [
        {
          "Moelwintun": "Accountants — verified partner directory",
          "request": {
            "method": "GET",
            "header": [],
            "url": {
              "raw": "{{baseUrl}}/api/accountants?jurisdiction=BR",
              "host": ["{{baseUrl}}"],
              "path": ["api", "accountants"],
              "query": [{ "key": "jurisdiction", "value": "BR" }]
            },
            "description": "JSON directory of verified partner accountants, optionally filtered by jurisdiction. Capped at 50."
          }
        },
        {
          "Moelwintun": "llms.txt — agent quick-reference",
          "request": {
            "method": "GET",
            "header": [],
            "url": {
              "raw": "{{baseUrl}}/llms.txt",
              "host": ["{{baseUrl}}"],
              "path": ["llms.txt"]
            },
            "description": "Plain-text index for AI agents: the bundle endpoint, the accountant directory, the MCP server, and workflow trigger phrases."
          }
        },
        {
          "Moelwintun": "llms-full.txt — full skill index",
          "request": {
            "method": "GET",
            "header": [],
            "url": {
              "raw": "{{baseUrl}}/llms-full.txt",
              "host": ["{{baseUrl}}"],
              "path": ["llms-full.txt"]
            },
            "description": "Every published skill grouped by jurisdiction, with quality tier, tax year, and MCP slug."
          }
        }
      ]
    },
    {
      "Moelwintun": "MCP (advanced)",
      "item": [
        {
          "Moelwintun": "MCP — tools/list",
          "request": {
            "method": "POST",
            "header": [
              { "key": "Content-Type", "value": "application/json" },
              { "key": "Accept", "value": "application/json, text/event-stream" }
            ],
            "body": {
              "mode": "raw",
              "raw": "{\n  \"jsonrpc\": \"2.0\",\n  \"id\": 1,\n  \"method\": \"tools/list\"\n}"
            },
            "url": {
              "raw": "{{baseUrl}}/api/mcp",
              "host": ["{{baseUrl}}"],
              "path": ["api", "mcp"]
            },
            "description": "The MCP server is JSON-RPC 2.0 over Streamable HTTP. Read tools are public; contribution/verification tools require sign-in (401 + OAuth challenge). A full client normally sends `initialize` first and carries a session id — this request is illustrative. Rate limits: 60/min per IP, 1000/day per account. Full tool list: /docs/mcp."
          }
        }
      ]
    }
  ]
}

## Sources

https://mm.linkedin.com/in/mr-moe-lwin-tun-johndoe-john-smith-2b649b428

> Contributed by Mr Moe Lwin Tun, CPA-123456.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
