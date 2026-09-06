# OpenAccountants

**Open-source Tax Guides your AI can cite — reviewed by named, licensed accountants.**

Every AI can do tax math. None of them can stand behind an answer. Here, real accountants put their **name, credential and review date** on the Guides your AI reads — publicly, on the record, in this repo.

[![License: AGPL-3.0](https://img.shields.io/badge/license-AGPL--3.0-047857)](LICENSE)
[![PyPI](https://img.shields.io/pypi/v/openaccountants-mcp?label=openaccountants-mcp&color=047857)](https://pypi.org/project/openaccountants-mcp/)
[![smithery badge](https://smithery.ai/badge/info-ood9/openaccountants)](https://smithery.ai/servers/info-ood9/openaccountants)
[![GitHub stars](https://img.shields.io/github/stars/openaccountants/openaccountants?style=social)](https://github.com/openaccountants/openaccountants/stargazers)

<!-- oa-stats:start -->
**1,843 Guides** across **232 jurisdictions** · **176 accountant-reviewed** · **43 named accountants** · **9,688 questions answered** through connected AIs

<sub>Live from openaccountants.com — updated 2026-09-06 by the nightly sync.</sub>
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

Without OpenAccountants, models answer from training data. With it, the answer cites the current Guide — and names the accountant who reviewed it.

```
You:    "I'm a freelancer in South Africa. What do I owe?"
          ↓  loads za-income-tax, za-provisional-tax
AI:     ITR12 working paper · IRP6 provisional schedule
        Medical credits · Retirement annuity deduction
        ─────────────────────────────────────────
        Reviewed by Werner Britz CA(SA)
```

<details>
<summary><strong>Prefer self-hosting or manual files?</strong></summary>

- **pip MCP server:** `pip install openaccountants-mcp` (mirrors this repo's `packages/`)
- **Manual:** download your jurisdiction's folder from [`packages/`](packages/) and upload the files to your AI. Start with your country's main package; `index.json` is the machine-readable inventory.

</details>

---

## Two states, greppable honesty

Every Guide is in exactly one state — and the repo greps honestly:

| State | Meaning |
|---|---|
| **Accountant-reviewed** | A named, licensed accountant reviewed the complete Guide. Their name is in the frontmatter (`reviewed_by:`) and on [the public roster](VERIFIERS.md) |
| **Source-cited draft** | Written from primary legislation, every figure cited to its source — not yet professionally reviewed |

⚠️ **General reference, not advice.** Guides may be incomplete, outdated, or wrong for your facts. Have a qualified professional review outputs before filing, payment, or action.

---

## Are you an accountant?

Your name on the tax knowledge AI actually uses — with attribution built in:

1. **Build a Guide** for the work you know cold: [openaccountants.com/skills/new](https://www.openaccountants.com/skills/new). It publishes credited to you, and lands in this repo under your name.
2. **Review a Guide** in your jurisdiction — your name, credential and review date go on it, here and on every AI answer that cites it.
3. **Set your GitHub username** in [your profile](https://www.openaccountants.com/profile) and your platform edits are committed to this repo as *you* — your contribution graph reflects your work.

The current roster: **[VERIFIERS.md](VERIFIERS.md)** (generated nightly from the platform).

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

- **[payday-super-checker](https://github.com/ryanduguid/payday-super-checker)** (MIT) — Verifies superannuation contributions against Australian Payday Super deadlines (in force since 1 July 2026) and estimates SG charge exposure on late payments, with all workings and statutory assumptions disclosed.
- **[div7a-loan-review](https://github.com/ryanduguid/div7a-loan-review)** (MIT) — Reviews Division 7A loan terms and minimum yearly repayments against the ATO benchmark interest rate, with fabricated inputs and explicit refusal boundaries.
- **[xero-trial-balance-export](https://github.com/ryanduguid/xero-trial-balance-export)** (MIT) — Exports a Xero trial balance to CSV only when month-movement and YTD column pairs both balance exactly.
- **[ato-benchmark-compare](https://github.com/ryanduguid/ato-benchmark-compare)** (MIT) — Evaluates business P&L statements locally against the Australian Taxation Office (ATO) small business performance benchmarks, surfacing variance flags and ratio analyses.

*(External tools provide computational review assistance and do not constitute tax or legal advice.)*

---

## License

- **Code** (mcp/, scripts/, tools/): [AGPL-3.0](LICENSE)
- **Guide content**: OpenAccountants Guide License v1.0 — see [LICENSING.md](LICENSING.md); commercial options in [COMMERCIAL-LICENSING.md](COMMERCIAL-LICENSING.md)

**Contact:** info@openaccountants.com · [Security policy](SECURITY.md) · [Cite this repo](CITATION.cff)
