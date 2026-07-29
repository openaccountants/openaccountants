# Changelog

All notable changes to OpenAccountants will be documented in this file.

## [2.4.0] — 2026-07-29

### How figures know which tax year they belong to

- **Every rule now carries its period.** `search_rules` renders `TY2026` for
  calendar-year jurisdictions and `2025/26` for fiscal ones, on every figure.
- **Mixed-year responses say so.** When one answer carries figures from more
  than one tax year, the header names the years and forbids combining them.
  This closes the failure where a 2025 threshold and a 2026 catch-up could be
  summed into a total true for no year.
- **Current year ranks first.** Year coverage now outranks text relevance, so
  the figure for the year you asked about surfaces above older vintages, which
  still serve, clearly labeled. Serving window is the current tax year plus the
  prior one (people file last year all year long); older vintages serve only
  when their year is named.
- **Fiscal-year jurisdictions got their real windows.** ~5,000 figures across
  GB, IN, HK, NZ, AU, PK, BD and ZA were stamped 1 Jan–31 Dec. They now carry
  the actual tax year: UK 6 Apr–5 Apr, India/HK/NZ 1 Apr–31 Mar, AU/PK/BD
  1 Jul–30 Jun, ZA 1 Mar–end Feb. Ireland, Singapore (calendar for
  individuals) and Japan (calendar for individuals, April for corporates) were
  deliberately left alone.
- New: [`docs/TAX-YEARS.md`](docs/TAX-YEARS.md).

### Search and serving correctness

- **`401k` now matches `401(k)`.** Users type the compact form; the law — and
  therefore our figures — uses parentheses. The tokenizer split on punctuation,
  so the two spellings never met and the current-year figure was invisible to
  the most-asked US retirement query. It looked exactly like stale data and was
  not. Citation variants now expand both ways (401k ↔ 401(k), 403b, 402g,
  401a17).
- **`/skills/<slug>.md` serves the Guide, not the web app.** It previously
  returned HTTP 200 with the HTML shell, so an AI told to fetch the markdown —
  as our own Guides instruct — parsed markup and never knew it had failed.
- **A Guide can no longer claim a review it did not have.** Some stored bodies
  carried "accountant-reviewed" prose and a reviewer's name from an earlier
  era while the verification state said source-cited draft. The state now wins
  at serve time: the claim is neutralised, a correction leads the body, and the
  divergence is reported in `provenance.body_review_claim_corrected`.

### Research guardrails

- Analysis-shaped questions now carry a research protocol: authority hierarchy,
  citation discipline, a confidence ladder, a memo contract, and escalation to
  a named accountant. `verify_citations` machine-checks the model's own
  citations against the pages it cited.
- New: [`docs/RESEARCH-GUARDRAILS.md`](docs/RESEARCH-GUARDRAILS.md), including
  the limits — we cannot make a model obey, and we say so.

### Naming

- **"Partner" is retired** across the repo. The public role is **accountant**
  (or *Open Accountant*). `PARTNERS.md` is now
  [`ACCOUNTANTS.md`](ACCOUNTANTS.md).
- **The roster no longer claims credentials we have not checked.** It now
  states exactly what was self-declared and what was confirmed against a public
  register, and says plainly that a blank means *not independently checked*,
  never *not qualified*.

## [2.3.0] — 2026-07-16

### Mixed-licence restructure (Guides move to a source-available licence)

- **Split code from content.** Software (`mcp/`, `scripts/`, `tools/`, `plugins/`) is now **AGPL-3.0-only**; the Guides (`skills/`, `packages/`, `workflows/`, `index.json`, `llms*.txt`) move to the new source-available **OA Guide License** (`LICENSES/LicenseRef-OA-Guide-License-1.0.txt`). Commercial embedding / RAG / model-training / bulk redistribution of the Guides now requires a commercial licence. See [`LICENSING.md`](LICENSING.md).
- **Removed `LICENSE-ADDITIONAL.md`** (the Section 7 output-attribution additional term), which was causing GitHub to report "unknown licenses" and reached beyond what GPL §7 reliably permits.
- **Standardised on `AGPL-3.0-only`** (was a mix of `AGPL-3.0` / `AGPL-3.0-or-later`) across `glama.json`, `mcp/pyproject.toml`, `CITATION.cff`, and the plugin manifest.
- **Renamed** `COMMERCIAL_LICENSE.md` → `COMMERCIAL-LICENSING.md` and rewrote it for the two-track model.
- **Added `REUSE.toml`** for machine-readable per-path licence mapping.
- **Added a CLA status check** (`.github/workflows/cla.yml`).

> **Note:** Guides that incorporate third-party AGPL/GPL material remain under those copyleft terms; the Guide License applies to the rest (see [`LICENSING.md`](LICENSING.md) § "Third-party copyleft material").

## [2.2.0] — 2026-07-04

### Metadata everywhere, docs that agree with each other

- **Complete frontmatter metadata on all 1,007 Guides**, with strict CI enforcement so a Guide can no longer merge with missing or malformed frontmatter ([PR #54](https://github.com/openaccountants/openaccountants/pull/54)).
- **Docs coherence pass**: one canonical frontmatter spec that all contributor docs point at, plus community health files ([PR #53](https://github.com/openaccountants/openaccountants/pull/53)).
- **UK Guides gained structured rate tables**, and the README got an animated demo ([PR #51](https://github.com/openaccountants/openaccountants/pull/51)).
- **`tax_year` normalized** to one consistent format across every Guide ([PR #52](https://github.com/openaccountants/openaccountants/pull/52)).

## [2.1.0] — 2026-07-04

### First professional OBBBA review: 33 corrections by Christopher Aryee, CPA

A licensed US CPA reviewed the four core US federal form Guides (1040, 1120, 1065, 1041) against the One Big Beautiful Bill Act and returned 33 sourced corrections: rates, thresholds, and statutory citations. All applied in [PR #45](https://github.com/openaccountants/openaccountants/pull/45), with the full red-line public. Highlights: §174A domestic R&D immediate expensing, §163(j) EBITDA add-back restored, new permanent GILTI/FDII rates, §6698 penalty $255, §199A stays 20%, SALT $40k cap, §1202 phased exclusion. Each Guide now carries `reviewed_by: Christopher Aryee, CPA` and a changelog.

### Repo overhaul (trust + machine-readability)

- **`index.json`** at repo root: machine-readable inventory of every Guide (slug, jurisdiction, tier, reviewed_by, last_updated), generated by `scripts/build-index.py`.
- **CI validation** (`.github/workflows/validate.yml`): frontmatter checks, index freshness, and a guard against deleting the hand-authored `packages/us-federal/` on every PR.
- **Fixed a data-destruction bug** in `scripts/build-packages.py`: a full rebuild used to wipe `packages/us-federal/` (which has no generator) — it is now protected.
- **`llms.txt` corrected** (its repo map was wrong) and **`llms-full.txt` added** for AI crawlers; `CLAUDE.md` gained a "for AI agents landing here" fast path.
- **One source-of-truth story** across CONTRIBUTING/CLAUDE/llms/docs: `skills/` is the editable source, `packages/` is generated from it, `packages/us-federal/` is hand-authored. See `docs/REPO-LAYOUT.md`.
- README rebuilt: honest quality states (source-cited draft / accountant-reviewed), Partners table with public proof links, 2-step install, reconciled counts.
- Internal strategy drafts removed from `docs/`; vestigial folders pruned.

## [0.2.0] — 2026-05-22 (mcp package version)

> Tracks the `openaccountants-mcp` PyPI package version. The repo as a whole is on v1.x; this entry summarises the changes that ship with the v0.2.0 MCP release.

### New universal cross-border skills (13)
- `pillar-two-globe-minimum-tax` — OECD GloBE 15% minimum tax (IIR, UTPR, QDMTT, SBIE, safe harbours)
- `dac6-mdr-reportable-arrangements` — EU DAC6 + UK MDR + OECD model
- `fatca-crs-automatic-exchange` — FATCA + CRS + DAC2 + CARF/DAC8
- `cbam-carbon-border-adjustment` — EU Carbon Border Adjustment Mechanism
- `digital-services-tax-matrix` — 25+ in-force DSTs incl. Canada DST 2024
- `ifrs-local-gaap-reconciliation` — IFRS ↔ US GAAP / HGB / FRS 102 / OIC / PCG / Ind AS / ASBE / J-GAAP / CPC / ASPE
- `saf-t-realtime-ereporting-matrix` — SAF-T + global e-invoicing + EU ViDA
- `ip-patent-box-matrix` — 18+ IP regimes with OECD MNA mechanics
- `free-zones-sez-matrix` — 50+ zones across UAE, Saudi, China, India, LatAm, EU, Africa
- `rd-tax-credits-matrix` — 25+ R&D regimes incl. UK merged RDEC, US §174
- `wealth-tax-matrix`, `inheritance-estate-gift-matrix`, `stamp-duty-matrix`, `property-transfer-tax-matrix`, `tax-controversy-map-apa`

### New foundation workflow bases (5)
Corporate income tax, statutory audit, customs/duties, excise, wealth/estate.

### New sector verticals (8)
Banking, insurance, shipping/aviation tonnage tax, funds/REITs, oil & gas, charity/nonprofit, SaaS/digital, construction.

### New pattern library files (4)
Global cloud infrastructure, productivity tools, ad platforms, marketplaces + banking fees.

### Canada split
Canada is now split into 13 per-province/territory packages (`packages/ca-ab/` through `packages/ca-yt/`) mirroring the US-state model. Three new territory skills added (Yukon, NWT, Nunavut). `packages/canada/` is now a thin index page.

### Quality tier simplification
Collapsed from four tiers (Q1-Q4) to two: **accountant-verified** and **research-verified**. `docs/QUALITY-TIERS.md` rewritten. Manifest at `skills/manifest.json` regenerated by new `scripts/build-skills-manifest.py` (auto-derives quality from skill frontmatter).

### Usability
- New `START-HERE.md` with 17 persona-driven scenarios routing users to the right files
- Domain index READMEs added in `skills/cross-border/`, `skills/verticals/`, `skills/foundation/`, `skills/patterns/`
- Top-level README updated with prominent "Start here" section

### Infrastructure docs
- `docs/TEMPORAL-VERSIONING-SPEC.md` — schema for time-bounded tax rates (Level 3 of intelligence roadmap)
- `docs/CORRECTION-FEEDBACK-LOOP-SPEC.md` — practitioner correction capture & moat-building (Level 6)

### License
LICENSE split — canonical AGPL-3.0 stays in `LICENSE`, custom Section 7 attribution + commercial licensing terms moved to `LICENSE-ADDITIONAL.md`. Restores GitHub auto-detection. `glama.json` now declares the SPDX identifier explicitly.

### Totals
- 748 skill files (up from 713)
- 199 packages (51 US states + 13 Canada + 132 international + 3 special)

---

## [1.0.0] — 2026-04-14

### The initial release

**371 tax skills across 134 countries.** Upload to any LLM with your bank statement.

#### Skills
- 185 consumption tax skills (VAT/GST/sales tax) — verified against tax authority websites
- 45 income tax skills — brackets, deductions, transaction pattern libraries
- 50 social contribution skills — SSC/NIC/pension/health with payment pattern libraries
- 14 estimated tax skills — advance payments, provisional tax, quarterly instalments
- 5 cross-border skills — reverse charge, withholding tax matrix, PE risk, OSS, exports
- 5 transaction pattern files — 120+ global vendor patterns for instant classification
- 3 intelligence skills — deadline engine, threshold alerts, optimisation advisor

#### End-to-end jurisdictions
Complete guided experience (intake → classification → computation → assembly → review):
Malta, United Kingdom, Germany, Australia, Canada, India, Spain, United States (California)

#### Architecture
- Per-jurisdiction packages in `packages/` — self-contained, upload to any LLM
- Universal foundation + intake (same for every country)
- Country-specific content skills with local supplier/transaction pattern libraries
- Malta v2.0 structure: tiers as sections (Classified/Assumed/Needs Input), not inline tags
- Build script generates packages from source skills

#### Quality
- **Accountant-verified**: Malta VAT/IT/SSC, Germany VAT, US federal bookkeeping/SE
- **Research-verified**: everything else — drafted from authoritative sources (tax-authority publications and primary legislation), awaiting credentialed sign-off
- Deep research caught 200+ errors across 100+ countries during research verification
