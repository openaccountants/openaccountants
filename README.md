# OpenAccountants

> Every skill here is written from the official law and the tax authority's own pages, with each figure linked to its source, and checked before it is published. Accountants write and approve these skills, but approvals, and the accountant's name, appear only through the OpenAccountants plugin (MCP). More than 100 skills are approved by a named, licensed accountant, and this repository runs behind what the plugin serves. For the current, accountant-approved version, add the plugin to your AI: https://www.openaccountants.com/connect?utm_source=github&utm_medium=readme

**Tax skills for AI, written from the law and approved by named accountants.** Your AI answers tax questions from memory. Add these skills and it answers from the law: every rate, threshold and deadline links to the official page it came from, and the plugin says which accountant, if any, has approved each skill.

[![OpenSSF Scorecard](https://api.securityscorecards.dev/projects/github.com/openaccountants/openaccountants/badge)](https://securityscorecards.dev/viewer/?uri=github.com/openaccountants/openaccountants)
[![OpenSSF Best Practices](https://www.bestpractices.dev/projects/16906/badge)](https://www.bestpractices.dev/projects/16906)
[![Skill checks](https://github.com/openaccountants/openaccountants/actions/workflows/validate.yml/badge.svg?branch=main)](https://github.com/openaccountants/openaccountants/actions/workflows/validate.yml)
[![Approved by accountants](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2Fopenaccountants%2Fopenaccountants%2Fstatus-data%2Fstatus.json&query=%24.approvers&label=named%20accountants&color=047857)](#accountants)
[![MCP Registry](https://img.shields.io/badge/MCP_Registry-listed-047857)](https://registry.modelcontextprotocol.io/v0/servers?search=io.github.openaccountants/openaccountants)
[![License: AGPL-3.0](https://img.shields.io/badge/code-AGPL--3.0-047857)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/openaccountants/openaccountants?style=social)](https://github.com/openaccountants/openaccountants/stargazers)

<a href="https://glama.ai/mcp/servers/openaccountants/openaccountants"><img width="380" height="200" src="https://glama.ai/mcp/servers/openaccountants/openaccountants/badges/card.svg" alt="OpenAccountants MCP server on Glama" /></a>

<!-- oa-stats:start -->
**34 named accountants** approving skills in **28 countries and states** · skills for **283 countries, states and territories** · every figure linked to its official source
<!-- oa-stats:end -->

---

## Accountants

A skill is **Approved by [name]** only when a licensed accountant read that exact text and approved it ([how approval works](CONTRIBUTING.md#2-approve-a-skill-accountants)). If the text changes, the approval is cleared until they approve again. Who approved which skill is shown on [openaccountants.com](https://www.openaccountants.com?utm_source=github&utm_medium=readme) and in the plugin's answers, not in this repository.

**Are you an accountant?** Approve the skills for your country and your name appears next to every AI answer that uses them, in ChatGPT, Claude and Cursor. It takes one click from the [accountant portal](https://www.openaccountants.com/for-accountants?utm_source=github&utm_medium=readme), from your own GitHub account. Found something wrong? Correct it in the same place. Each accountant works under their own licence; OpenAccountants does not sell accountancy services.

---

## Every figure has a source

A tax answer is only as good as the number in it. So every figure in a skill sits in a row that links the official page it came from, and the page can be opened and checked by anyone. A real row, from the Malta VAT skill:

| Activity | Registration threshold | Exit threshold | Source |
|---|---|---|---|
| Economic activities consisting principally in the supply of goods | €35,000 | €28,000 | https://legislation.mt/getpdf/67691cdeb52f1d38d8a4103f |

What keeps those figures honest:

- **Official sources only.** Laws, gazettes and tax authority pages; never blogs or firm summaries.
- **[The figure check](docs/AUTOMATED-REVIEW.md).** On every pull request, each figure in a rates table is looked for on the page its row links to. A figure that is not there blocks the merge until it is fixed or explained.
- **The evidence archive.** Snapshots of the source pages and the working ledgers behind the skills live in [openaccountants/evidence](https://github.com/openaccountants/evidence), so a figure can still be traced after a government site changes.
- **Worked examples that add up.** Every skill's examples are recomputed on every pull request ([`scripts/check-examples.py`](scripts/check-examples.py)).

How skills are built, checked and corrected: [docs/ACCURACY-METHODOLOGY.md](docs/ACCURACY-METHODOLOGY.md).

---

## Add to your AI

Add this address to [Claude](https://claude.ai), [ChatGPT](https://chatgpt.com), [Cursor](https://cursor.com), [Windsurf](https://windsurf.com) or any AI that takes a connector:

```
https://www.openaccountants.com/api/mcp
```

Guided setup: **[openaccountants.com/connect](https://www.openaccountants.com/connect?utm_source=github&utm_medium=readme)**. Then ask a question your AI would otherwise guess at:

> *"I'm a freelancer in Malta billing €40,000 this year. Do I have to register for VAT?"*

<details>
<summary><strong>Prefer self-hosting or manual files?</strong></summary>

- **[Python MCP server](mcp/):** [install the tested GitHub revision](mcp/README.md). The current PyPI release is older and has no bundled skills.
- **Manual:** download your jurisdiction's folder from [`packages/`](packages/) and upload the files to your AI. `index.json` is the machine-readable inventory.

Also listed on the [MCP Registry](https://registry.modelcontextprotocol.io/v0/servers?search=io.github.openaccountants/openaccountants) and [Glama](https://glama.ai/mcp/servers/openaccountants/openaccountants).

</details>

---

## Find your country

**[Browse all countries](skills/COUNTRIES.md)**, by region, with the state of each pack. United States: [federal](skills/us/federal/) and [states](skills/us/states/).

In the plugin, each skill carries one of two labels ([definitions](docs/QUALITY-TIERS.md)):

| Label | Meaning |
|---|---|
| **Approved by [name]** | A named, licensed accountant approved this exact text. The name is shown in the plugin and on the website. |
| **Not yet approved** | Built from the law and checked before merge, but no accountant has approved it yet. |

⚠️ **General reference, not advice.** Skills may be incomplete, outdated, or wrong for your facts. Have a qualified professional review outputs before filing, payment, or action.

---

## Contribute

Three ways in, all in **[CONTRIBUTING.md](CONTRIBUTING.md)**:

- **I am an accountant.** Approve or correct the skills for your country, under your own name.
- **I can write.** Take a country and write its missing skills from the law.
- **I found a mistake.** Open an issue with the official source that shows it.

Need an accountant for your own bookkeeping, VAT, payroll or return? [Get in touch](https://www.openaccountants.com/contact?utm_source=github&utm_medium=readme) and we will put you in touch with one in your country.

---

## For developers

| What | Where |
|---|---|
| Skill source (per jurisdiction) | [`skills/`](skills/) |
| Per-country bundles (generated) | [`packages/`](packages/) |
| Machine-readable inventory | [`index.json`](index.json) · [`llms.txt`](llms.txt) |
| What is left, per country (rebuilt daily) | [`status.json`](https://github.com/openaccountants/openaccountants/blob/status-data/status.json) |
| Python MCP server | [`mcp/`](mcp/) · [PyPI](https://pypi.org/project/openaccountants-mcp/) |
| Repo layout and sync | [`docs/REPO-LAYOUT.md`](docs/REPO-LAYOUT.md) · [`docs/WEBSITE-SYNC.md`](docs/WEBSITE-SYNC.md) |

API and platform integrations: [openaccountants.com/for-developers](https://www.openaccountants.com/for-developers?utm_source=github&utm_medium=readme)

---

## Related open-source projects

Independent, open-source review aids and calculation tools that complement the OpenAccountants skill library:

- **[aus-accounting-mcp](https://github.com/ryanduguid/australian-accounting/tree/main/apps/aus-accounting-mcp)** (AGPL-3.0-or-later): Local stdio MCP server for Australian accounting reviews (ATO small business benchmarks, Payday Super timing, Division 7A, GST coding and BAS reconciliation), bounded tax and super worksheets (paired with `australian-tax-calculators`) and cited retrieval from a local Markdown folder. [Releases](https://github.com/ryanduguid/australian-accounting/releases) · [PyPI](https://pypi.org/project/aus-accounting-mcp/) · [MCP Registry](https://registry.modelcontextprotocol.io/v0.1/servers?search=io.github.ryanduguid%2Faus-accounting&version=latest) · [Glama](https://glama.ai/mcp/servers/ryanduguid/australian-accounting).
- **[australian-tax-calculators](https://github.com/ryanduguid/australian-accounting/tree/main/packages/australian-tax-calculators)** (AGPL-3.0-or-later): Deterministic local Rust CLI covering bounded Australian tax and super worksheets (income tax, PAYG withholding, super caps, Division 7A, CGT, FBT, GST, fuel tax credits, state land tax, stamp duty and payroll tax) with explicit statutory scope and refusal boundaries. [Releases](https://github.com/ryanduguid/australian-accounting/releases).
- **[payday-super-checker](https://github.com/ryanduguid/australian-accounting/tree/main/packages/payday-super-checker)** (Apache-2.0): Verifies superannuation contributions against Australian Payday Super deadlines (in force since 1 July 2026) and estimates SG charge exposure on late payments, with all workings and statutory assumptions disclosed.
- **[div7a-loan-review](https://github.com/ryanduguid/australian-accounting/tree/main/packages/div7a-loan-review)** (Apache-2.0): Reviews Division 7A loan terms and minimum yearly repayments against the ATO benchmark interest rate, with fabricated inputs and explicit refusal boundaries.
- **[xero-trial-balance-export](https://github.com/ryanduguid/accounting-review-pipeline/tree/main/packages/xero-trial-balance-export)** (Apache-2.0): Exports a Xero trial balance to CSV only when month-movement and YTD column pairs both balance exactly.
- **[ato-benchmark-compare](https://github.com/ryanduguid/australian-accounting/tree/main/packages/ato-benchmark-compare)** (Apache-2.0): Evaluates business P&L statements locally against the Australian Taxation Office (ATO) small business performance benchmarks, surfacing variance flags and ratio analyses.
- **[OsaBooks](https://github.com/hidicker/osabooks)** (AGPL-3.0): Free bookkeeping for businesses, rental properties and households in Australia, New Zealand, South Korea and the United States, with Xero and QuickBooks imports. Use it as a standard bookkeeping platform, or with several AI features: coding suggestions, year-end checks against the OpenAccountants guides, and an MCP connector so Claude, ChatGPT or another AI app can read your books. Runs on your own computer or online on your own Supabase. [Home page and demo](https://nbparagliding.nz/osabooks/home/).
  
*(External tools provide computational review assistance and do not constitute tax or legal advice.)*

---

## License

- **Code** (mcp/, scripts/, tools/, calculators/): [AGPL-3.0-only](LICENSE)
- **Skill content**: OpenAccountants Guide License, see [LICENSING.md](LICENSING.md); commercial options in [COMMERCIAL-LICENSING.md](COMMERCIAL-LICENSING.md)

**Contact:** info@openaccountants.com · [Security policy](SECURITY.md) · [Cite this repo](CITATION.cff)
