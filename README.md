# OpenAccountants

**Open tax skills for AI.** Your AI answers tax questions from memory. Add these skills and it answers from the law: every rate, threshold and deadline cited to its official source, for 190+ jurisdictions.

[![License: AGPL-3.0](https://img.shields.io/badge/license-AGPL--3.0-047857)](LICENSE)
[![PyPI](https://img.shields.io/pypi/v/openaccountants-mcp?label=openaccountants-mcp&color=047857)](https://pypi.org/project/openaccountants-mcp/)
[![GitHub stars](https://img.shields.io/github/stars/openaccountants/openaccountants?style=social)](https://github.com/openaccountants/openaccountants/stargazers)

<!-- oa-stats:start -->
**2,132 AI skills** across **249 jurisdictions** · **33 accountant-reviewed** · **39 named accountants** · **6,115 questions answered** through connected AIs

<sub>Live from openaccountants.com — updated 2026-10-30 by the nightly sync.</sub>
<!-- oa-stats:end -->

---

## Find your country

**[Browse all countries](skills/COUNTRIES.md)**, by region, with the state of each pack. United States: [federal](skills/us/federal/) and [states](skills/us/states/).

---

## Add to your AI

Add this address to Claude, ChatGPT, Cursor, Windsurf or any AI that takes a connector:

```
https://www.openaccountants.com/api/mcp
```

Guided setup: **[openaccountants.com/connect](https://www.openaccountants.com/connect)**

Then ask a question your AI would otherwise guess at:

> *"What's the combined sales tax rate in Manatee County, Florida for 2026?"*

<details>
<summary><strong>Prefer self-hosting or manual files?</strong></summary>

- **Python MCP server:** [install the tested GitHub revision](mcp/README.md). The current PyPI release is older and has no bundled skills.
- **Manual:** download your jurisdiction's folder from [`packages/`](packages/) and upload the files to your AI. Start with your country's main package; `index.json` is the machine-readable inventory.

Also listed on [Smithery](https://smithery.ai/server/info-ood9/openaccountants) and the [MCP Registry](https://registry.modelcontextprotocol.io/v0/servers?search=io.github.openaccountants/openaccountants).

</details>

---

## Contribute

Three ways in, all in **[CONTRIBUTING.md](CONTRIBUTING.md)**:

- **I can write.** Take a country and write its missing skills from the law.
- **I am an accountant.** Review a skill and put your name on it.
- **I found a mistake.** Open an issue with the source that shows it.

---

## How to read a skill

Every skill shows **Built from the law**. An approved accountant publishing their own professional work is also its approver; they record their own approval in the original PR. No second accountant or separate approval PR is required. Skill content is source-available under the terms in [LICENSING.md](LICENSING.md).

Each skill has one approval status:

| State | Meaning |
|---|---|
| **Approved by [name]** | The accountant's approval is recorded with `tier: 1`, `reviewed_by` and `reviewed_on`. The website resolves that name to a current approved accountant account. |
| **Not yet approved** | No named accountant approval is recorded. Independent source checking before merge is separate from professional approval. |

The definitions: [docs/QUALITY-TIERS.md](docs/QUALITY-TIERS.md). How skills are built, checked and corrected: [docs/ACCURACY-METHODOLOGY.md](docs/ACCURACY-METHODOLOGY.md). Which number to quote and where it is measured: [docs/COVERAGE.md](docs/COVERAGE.md).

⚠️ **General reference, not advice.** Skills may be incomplete, outdated, or wrong for your facts. Have a qualified professional review outputs before filing, payment, or action.

---

## Need the work done?

OpenAccountants also does the bookkeeping, VAT, payroll and tax work for businesses, in the countries they work in. [Talk to us](https://www.openaccountants.com/tax-help?source=github_readme#book). The skills and the AI connection stay free.

---

## How it stays accurate

A tax library is only as good as its worst stale number, so machines re-check this one
every night:

- **The maths check** re-reads every skill and flags sums that do not add up, tax bands
  with gaps, totals that do not total, and years that disagree.
- **The source watch** visits the official pages the figures came from and raises a hand
  when a page changes.
- **The refresh engine** re-derives the stalest skills from official sources on a fixed
  monthly budget, refusing to publish any figure without a link.
- **The nightly exam** tests whether AIs actually said what the skills say that day, or
  improvised. Improvisation gets caught, counted and fixed at the source.

GitHub is the source of truth for skill documents. Merged PRs are delivered to the
platform and checked against the published content. Generated packages and indexes
are refreshed by the scheduled sync. A merge alone does not prove that a skill is live.

The whole story, in plain words: [openaccountants.com/how-it-works](https://www.openaccountants.com/how-it-works)

---

## For developers

| What | Where |
|---|---|
| Skill source (per jurisdiction) | [`skills/`](skills/) |
| Per-country bundles (generated) | [`packages/`](packages/) |
| Machine-readable inventory | [`index.json`](index.json) |
| LLM entry point | [`llms.txt`](llms.txt) |
| Python MCP server | [`mcp/`](mcp/) · [PyPI](https://pypi.org/project/openaccountants-mcp/) |
| Repo architecture + sync | [`docs/REPO-LAYOUT.md`](docs/REPO-LAYOUT.md) · [`docs/WEBSITE-SYNC.md`](docs/WEBSITE-SYNC.md) |

API and platform integrations: [openaccountants.com/for-developers](https://www.openaccountants.com/for-developers)

---

## Related open-source projects

Independent, open-source review aids and calculation tools that complement the OpenAccountants skill library:

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
