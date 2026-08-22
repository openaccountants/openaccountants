# OpenAccountants — Skill Quality Tiers

How we measure whether a skill is ready for production use.

We use **two tiers**. No drafts, no stubs — every published skill is one of these:

---

## The two tiers

| Tier | Label | What it means | Legacy identifier |
|------|-------|--------------|-------------------|
| **1** | **Accountant-reviewed** | A licensed practitioner has reviewed the skill, run it against real (or representative) data, and signed off. Errors found during use have been corrected. The skill is current with the latest tax-year rates and filing forms. | `accountant-verified` |
| **2** | **Source-cited draft** | Every rate, threshold, form number, and deadline has been drafted from authoritative sources — tax-authority publications and the relevant statutes. Format matches the accountant-reviewed standard. Awaiting a full review by an accountant. | `research-verified` |

That's it. If a skill is published, it is one of those two.

> **Display label vs. stored identifier.** The machine identifiers do not change: frontmatter still uses `tier: 1|2` and `verified_by:`, and legacy badges/enums still say `accountant-verified` / `research-verified`. What changed is the **display language**: Tier 1 is written as **"accountant-reviewed"** and Tier 2 as **"source-cited draft"** everywhere a human reads it. This doc is the mapping between the two.

---

## What each tier guarantees

### Accountant-reviewed (Tier 1)

- A real licensed practitioner (CPA, EA, CA, Steuerberater, expert-comptable, commercialista, asesor fiscal, or equivalent for the jurisdiction) has put their name and license number on it.
- The skill has been used against real client data and refined through filing cycles.
- The contributor is publicly credited on the skill and at [openaccountants.com](https://www.openaccountants.com).
- The skill is reviewed at least annually for rate / threshold / form changes.

### Source-cited draft (Tier 2)

- The skill follows the accountant-reviewed format (Step 0 onboarding → Step N output).
- Every figure carries a primary-source citation (statute, regulation, tax authority notice).
- Deep research against the tax authority's published guidance has been completed.
- It is **not** a substitute for accountant review of an actual filing. The reviewer brief always says so.
- It is the right tier to use *as a starting point* — your accountant reviews and signs off before you file.

---

## The standard skill format

Every published skill, in either tier, must use this section order:

```
## Skill Metadata                          ← who, what, where
## Confidence Tier Definitions             ← T1 / T2 / T3 rules within the skill
## Step 0: Client Onboarding Questions     ← FIRST — gate before any work
## Step 1: Transaction Classification      ← sale/purchase, location, rate
## Step 2: Box/Line Assignment             ← deterministic lookup tables
## Step 3: Reverse Charge Mechanics        ← cross-border rules
## Step 4: Deductibility Check             ← blocked categories
## Step 5: Derived Calculations            ← computed boxes/totals
## Step 6: Key Thresholds                  ← registration, filing, penalties
## Step 7: Filing Deadlines                ← dates, frequencies
## Step 8: [Country-specific section]      ← e.g., Article 11, Kleinunternehmer
## PROHIBITIONS                            ← hard stops
## Edge Case Registry                      ← numbered EC1, EC2, etc.
## Test Suite                              ← numbered tests with expected output
## Reviewer Escalation Protocol            ← T2/T3 output templates
## Contribution Notes                      ← how to adapt for other jurisdictions
## Disclaimer                              ← standard liability + openaccountants.com
```

Key rules:

- Step 0 (onboarding) is ALWAYS first — never buried at the end.
- Box / line assignments are **deterministic lookup tables**, not narrative text.
- Classification matrices use **tables**, not paragraphs.
- No "Overview" or "What is VAT?" sections — this is an execution skill, not a textbook.
- Every rule tagged with confidence tier `[T1]`, `[T2]`, or `[T3]` (these are *within-skill* rule confidence, not the overall quality tier).
- PROHIBITIONS section comes before edge cases.

---

## Current inventory

### Accountant-reviewed (Tier 1)

| Skill | Jurisdiction | Reviewed by |
|-------|-------------|-------------|
| `malta-vat-return` | Malta | Michael Cutajar, CPA |
| `malta-income-tax` | Malta | Michael Cutajar, CPA |
| `malta-ssc` | Malta | Michael Cutajar, CPA |
| `malta-tax-optimization` | Malta | Michael Cutajar, CPA |
| `mt-estimated-tax` | Malta | Michael Cutajar, CPA |
| `germany-vat-return` | Germany | Pending publication of practitioner registry |
| `south-africa-vat` | South Africa | Michael Cutajar, CPA |
| `za-vat-return` | South Africa | Michael Cutajar, CPA |
| `za-income-tax` | South Africa | Michael Cutajar, CPA |
| `za-provisional-tax` | South Africa | Michael Cutajar, CPA |
| `us-sole-prop-bookkeeping` | US Federal | Pending publication of practitioner registry |
| `us-schedule-c-and-se-computation` | US Federal | Pending publication of practitioner registry |
| `us-ca-freelance-intake` | US-CA | Pending publication of practitioner registry |

This list is derived from each skill's explicit `tier: 1` plus its reviewer name (`reviewed_by`, or the legacy `verified_by` — a stored identifier that keeps its spelling). To add a new accountant-reviewed skill, set **both** `tier: 1` and the reviewer's name and credential, then regenerate the canonical inventory with `python3 scripts/build-index.py` — the tier and verifier land in `index.json`. Setting a reviewer name without flipping `tier` to `1` is a validation error: `tier: 2` must not claim accountant verification. Every accountant-reviewed skill carries the reviewer's name and license number on the skill page at openaccountants.com.

### Source-cited drafts (Tier 2)

Everything else in this repo. ~700+ skills covering 134 countries and 51 US states. Each one's frontmatter shows the research date and the authoritative sources cross-checked.

---

## What the user sees on a skill

```
┌─────────────────────────────────────────────┐
│  Malta VAT Return v1.0                      │
│  ████████████ ACCOUNTANT-REVIEWED           │
│                                             │
│  Reviewed by: [Practitioner name + license] │
│  Tested against: Real client data           │
│  Last updated: [Date]                       │
└─────────────────────────────────────────────┘

┌─────────────────────────────────────────────┐
│  France VAT Return (CA3) v0.1               │
│  ▓▓▓▓▓▓▓▓░░░░ SOURCE-CITED DRAFT            │
│                                             │
│  Sources: impots.gouv.fr, PWC, EU TEDB      │
│  Research date: April 2026                  │
│  Awaiting accountant review                 │
│  Help review: openaccountants.com/verify    │
└─────────────────────────────────────────────┘
```

---

## How a skill moves from source-cited draft to accountant-reviewed

1. A credentialed practitioner in the jurisdiction picks up the skill.
2. They review the rates, thresholds, forms, and deadlines against current law.
3. They run the skill against representative or real client data.
4. They submit corrections (web form at openaccountants.com or GitHub PR).
5. A skill maintainer merges the corrections; the skill is tagged with the practitioner's name and license number.
6. The skill is bumped to **accountant-reviewed** in the next release.

The practitioner is credited publicly. Their profile lists all the skills they've signed off.

---

## Authoritative research sources

These are the sources a source-cited draft must be drafted and cross-checked against. The same sources are recommended to practitioners reviewing their jurisdiction.

### Global / multi-jurisdiction

| Source | URL pattern | What it covers |
|--------|------------|----------------|
| **Deloitte Tax Guides** | dits.deloitte.com | VAT/GST rates, thresholds, compliance |
| **EY Worldwide Tax Guide** | ey.com/en_gl/tax-guides | Country-by-country tax overviews |
| **KPMG Tax Rates Online** | kpmg.com/tax-rates | Corporate / individual / indirect tax rates |
| **OECD Tax Database** | oecd.org/tax/tax-policy | Standardised cross-country tax data |

### European Union

| Source | URL | What it covers |
|--------|-----|----------------|
| **EU TEDB** (Taxes in Europe Database) | ec.europa.eu/taxation_customs/tedb | Official EU VAT rates for all 27 Member States |
| **EC VAT Information Exchange System** | ec.europa.eu/taxation_customs/vies | VAT number validation |
| **VAT Expert Group publications** | ec.europa.eu | Directive interpretations |

### Country-specific tax authorities

| Country | Authority | URL |
|---------|-----------|-----|
| **UK** | HMRC | gov.uk/government/organisations/hm-revenue-customs |
| **Canada** | CRA | canada.ca/en/revenue-agency |
| **Australia** | ATO | ato.gov.au |
| **New Zealand** | IRD | ird.govt.nz |
| **Ireland** | Revenue | revenue.ie |
| **Germany** | BZSt / Finanzamt | bzst.de, elster.de |
| **France** | DGFiP | impots.gouv.fr |
| **Italy** | Agenzia delle Entrate | agenziaentrate.gov.it |
| **Spain** | AEAT | agenciatributaria.es |
| **Netherlands** | Belastingdienst | belastingdienst.nl |
| **Portugal** | AT | portaldasfinancas.gov.pt |
| **Belgium** | SPF Finances | finances.belgium.be |
| **Poland** | KAS | podatki.gov.pl |
| **India** | GSTN / CBDT | gst.gov.in, incometax.gov.in |
| **Japan** | NTA | nta.go.jp |
| **Singapore** | IRAS | iras.gov.sg |
| **South Korea** | NTS | nts.go.kr |
| **Brazil** | RFB | gov.br/receitafederal |
| **Mexico** | SAT | sat.gob.mx |
| **UAE** | FTA | tax.gov.ae |
| **South Africa** | SARS | sars.gov.za |
| **Kenya** | KRA | kra.go.ke |
| **Nigeria** | FIRS | firs.gov.ng |

### US state tax authorities

Each state has an online portal. Search "[State] department of revenue" for the canonical URL. Major examples:

| State | Authority | URL |
|-------|-----------|-----|
| **California** | CDTFA | cdtfa.ca.gov |
| **New York** | DTF | tax.ny.gov |
| **Texas** | Comptroller | comptroller.texas.gov |
| **Florida** | DOR | floridarevenue.com |
| **Illinois** | IDOR | tax.illinois.gov |
| **Washington** | DOR | dor.wa.gov |

---

## Disclaimer

Quality tiers describe the review status of a skill, not a guarantee that any specific output is correct. LLMs hallucinate, tax law changes, and individual circumstances vary. Every output must be reviewed by a qualified professional before filing.
