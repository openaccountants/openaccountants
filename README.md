# OpenAccountants

**Open-source Tax Guides your AI can cite, with sources, methods and applicable periods.**

Published by **OpenAccountants**, founded by [Michael Cutajar](https://www.openaccountants.com/network/ecd6fe97-c3ed-4337-8e12-d1e7456201a9). Each Guide explains a tax task for a particular jurisdiction. Named authors receive credit for their work; founder credit does not imply authorship or professional expertise in every jurisdiction.

[![License: AGPL-3.0](https://img.shields.io/badge/license-AGPL--3.0-047857)](LICENSE)
[![PyPI](https://img.shields.io/pypi/v/openaccountants-mcp?label=openaccountants-mcp&color=047857)](https://pypi.org/project/openaccountants-mcp/)
[![GitHub stars](https://img.shields.io/github/stars/openaccountants/openaccountants?style=social)](https://github.com/openaccountants/openaccountants/stargazers)

<!-- oa-stats:start -->
**1,890 Guides** across **231 jurisdictions** · **44 named accountants** · **17,141 questions answered** through connected AIs

<sub>Live from openaccountants.com — updated 2026-10-09 by the nightly sync.</sub>
<!-- oa-stats:end -->

---

## Try it in 60 seconds

Add the hosted connector to Claude, ChatGPT, Cursor, Windsurf or any MCP client:

```
https://www.openaccountants.com/api/mcp
```

Guided setup: **[openaccountants.com/connect](https://www.openaccountants.com/connect)**

Then ask a question your AI would otherwise guess at:

> *"What's the combined sales tax rate in Manatee County, Florida for 2026?"*

Without OpenAccountants, models answer from training data. With it, the answer can cite a Guide, its applicable period and its official sources.

```
You:    "I'm a freelancer in South Africa. What do I owe?"
          ↓  loads za-income-tax, za-provisional-tax
AI:     ITR12 working paper · IRP6 provisional schedule
        Medical credits · Retirement annuity deduction
        ─────────────────────────────────────────
        Source: OpenAccountants · applicable tax year
```

<details>
<summary><strong>Prefer self-hosting or manual files?</strong></summary>

- **pip MCP server:** `pip install openaccountants-mcp` (mirrors this repo's `packages/`)
- **Manual:** download your jurisdiction's folder from [`packages/`](packages/) and upload the files to your AI. Start with your country's main package; `index.json` is the machine-readable inventory.

</details>

---

## How to assess a Guide

Read its jurisdiction, applicable tax year, scope, assumptions, calculation method and official sources. Publisher and author credit identify who supplied material; they do not certify it as correct or current. Automated source checks describe a check, not professional sign-off.

Historical review fields may remain in older source files and Git history. Current generated indexes and MCP responses do not present them as endorsements. See [Guide attribution and evidence](docs/QUALITY-TIERS.md).

⚠️ **General reference, not advice.** Guides may be incomplete, outdated, or wrong for your facts. Have a qualified professional review outputs before filing, payment, or action.

---

## Are you an accountant?

Your name on the tax knowledge AI actually uses — with attribution built in:

1. **Build a Guide** for the work you know cold: [openaccountants.com/skills/new](https://www.openaccountants.com/skills/new). It publishes credited to you, and lands in this repo under your name.
2. **Improve a Guide** in your jurisdiction with a correction, method or official source. Authorship credit reflects the work you contribute.
3. **Set your GitHub username** in [your profile](https://www.openaccountants.com/profile) and your platform edits are committed to this repo as *you* — your contribution graph reflects your work.

Find practitioners in the **[accountant directory](https://www.openaccountants.com/network)**. A directory listing is not a Guide endorsement.

---

## How it stays accurate

A tax library is only as good as its worst stale number, so machines re-check this one
every night:

- **The maths check** re-reads every guide and flags sums that do not add up, tax bands
  with gaps, totals that do not total, and years that disagree.
- **The source watch** visits the official pages the figures came from and raises a hand
  when a page changes.
- **The refresh engine** re-derives the stalest guides from official sources on a fixed
  monthly budget, refusing to publish any figure without a link.
- **The nightly exam** tests whether AIs actually said what the guides say that day, or
  improvised. Improvisation gets caught, counted and fixed at the source.

The sync runs both ways: platform edits land here as commits under the author's own name,
and merged PRs here flow back into what every AI serves, credited to you. A guide with an
accountant's byline never changes without that accountant's one-click approval.

The whole story, in plain words: [openaccountants.com/how-it-works](https://www.openaccountants.com/how-it-works)

---

## Contributing

Edit **`skills/**` only** — everything else regenerates automatically:

- `packages/`, `index.json`, `llms-full.txt` — generated nightly; never edit in a PR
- Merged source PRs are credited to you and must be confirmed as ingested before the next platform export
- Full guide: [CONTRIBUTING.md](CONTRIBUTING.md) · Layout: [docs/REPO-LAYOUT.md](docs/REPO-LAYOUT.md)

---

## For developers

| What | Where |
|---|---|
| Guide source (per jurisdiction) | [`skills/`](skills/) |
| Per-country bundles (generated) | [`packages/`](packages/) |
| Machine-readable inventory | [`index.json`](index.json) |
| LLM entry point | [`llms.txt`](llms.txt) |
| Python MCP server | [`mcp/`](mcp/) · [PyPI](https://pypi.org/project/openaccountants-mcp/) |
| Repo architecture + sync | [`docs/REPO-LAYOUT.md`](docs/REPO-LAYOUT.md) · [`docs/WEBSITE-SYNC.md`](docs/WEBSITE-SYNC.md) |

API and platform integrations: [openaccountants.com/for-developers](https://www.openaccountants.com/for-developers)

---

## Related open-source projects

Independent, open-source review aids and calculation tools that complement the OpenAccountants guide library:

- **[payday-super-checker](https://github.com/ryanduguid/australian-accounting/tree/main/packages/payday-super-checker)** (MIT) — Verifies superannuation contributions against Australian Payday Super deadlines (in force since 1 July 2026) and estimates SG charge exposure on late payments, with all workings and statutory assumptions disclosed.
- **[div7a-loan-review](https://github.com/ryanduguid/australian-accounting/tree/main/packages/div7a-loan-review)** (MIT) — Reviews Division 7A loan terms and minimum yearly repayments against the ATO benchmark interest rate, with fabricated inputs and explicit refusal boundaries.
- **[xero-trial-balance-export](https://github.com/ryanduguid/accounting-review-pipeline/tree/main/packages/xero-trial-balance-export)** (MIT) — Exports a Xero trial balance to CSV only when month-movement and YTD column pairs both balance exactly.
- **[ato-benchmark-compare](https://github.com/ryanduguid/australian-accounting/tree/main/packages/ato-benchmark-compare)** (MIT) — Evaluates business P&L statements locally against the Australian Taxation Office (ATO) small business performance benchmarks, surfacing variance flags and ratio analyses.

*(External tools provide computational review assistance and do not constitute tax or legal advice.)*

---

## License

- **Code** (mcp/, scripts/, tools/): [AGPL-3.0](LICENSE)
- **Guide content**: OpenAccountants Guide License v1.0 — see [LICENSING.md](LICENSING.md); commercial options in [COMMERCIAL-LICENSING.md](COMMERCIAL-LICENSING.md)

**Contact:** info@openaccountants.com · [Security policy](SECURITY.md) · [Cite this repo](CITATION.cff)
