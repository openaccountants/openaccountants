# OpenAccountants — Skill Quality Tiers

How we say who stands behind a skill.

Every published skill is in exactly one of **three attribution states**:

---

## The three states

| State | Frontmatter | What it means | Legacy `tier` |
|------|-------------|--------------|---------------|
| **Built by Michael Cutajar and the OpenAccountants team** | `trust_label: Built by Michael Cutajar and the OpenAccountants team` (team rewrites also carry `authored_by: Michael Cutajar and the OpenAccountants team`) | Written by the team from primary sources: every rate, threshold, form number and deadline cites the tax authority or statute. No named accountant stands behind it. | `2` |
| **Accountant-authored** | `authored_by: <Name[, credential]>` and `trust_label: Accountant-authored` | A named accountant, approved on openaccountants.com, wrote the skill. Nobody else has checked it yet. | `2` |
| **Checked by <name>** | `reviewed_by: <Name[, credential]>`, `review_status: current`, `trust_label: Checked by <Name>` | An accountant other than the author checked the complete skill. Their name is on the skill and on [VERIFIERS.md](../VERIFIERS.md). | `1` |

That's it. If a skill is published, it is one of those three.

> **Display label vs. stored identifier.** `tier` stays as the machine field: `1` = checked by a second accountant, `2` = not independently checked. The `verified_by` key is retired; the export removes it. Legacy enums in scripts (`accountant-verified` / `research-verified`) keep their spelling as identifiers only. Everywhere a human reads it, the three labels above are the words.

---

## What each state guarantees

### Built by Michael Cutajar and the OpenAccountants team

- Every figure carries a primary-source citation (statute, regulation, tax authority notice).
- Deep research against the tax authority's published guidance has been completed.
- The machine checks in the README ("How it stays accurate") run against it every night.
- It is **not** a substitute for an accountant's check of an actual filing. The reviewer brief always says so.

### Accountant-authored

- A real accountant (CPA, EA, CA, Steuerberater, expert-comptable, commercialista, asesor fiscal, or equivalent for the jurisdiction) whose licence or registration number we have checked wrote it and is named on it.
- The author is publicly credited on the skill and at [openaccountants.com](https://www.openaccountants.com).
- No second accountant has checked it yet.

### Checked by <name>

- An accountant other than the author has checked the complete skill and put their name on it.
- The checking accountant is publicly credited on the skill, on the roster and at [openaccountants.com](https://www.openaccountants.com).
- A substantive edit sets `review_status` back to `pending_review` until the skill is checked again.

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

### Checked by a second accountant (tier 1)

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

This list is a hand-curated sample; the generated [VERIFIERS.md](../VERIFIERS.md) at the repo root is the current roster. A skill is in this state when it carries `tier: 1` plus the checking accountant's name in `reviewed_by`. To add one, set **both** `tier: 1` and `reviewed_by`, then regenerate the canonical inventory with `python3 scripts/build-index.py` so the tier and name land in `index.json`.

### Not independently checked (tier 2)

Everything else in this repo, either team-built or Accountant-authored; the `counts` block of `index.json` gives the current total. Each one's frontmatter shows the research date and the authoritative sources cross-checked.

---

## What the user sees on a skill

```
┌─────────────────────────────────────────────┐
│  Malta VAT Return v1.0                      │
│  ████████████ CHECKED BY [NAME]             │
│                                             │
│  Checked by: [Accountant name + license]    │
│  Tested against: Real client data           │
│  Last updated: [Date]                       │
└─────────────────────────────────────────────┘

┌─────────────────────────────────────────────┐
│  France VAT Return (CA3) v0.1               │
│  ▓▓▓▓▓▓▓▓░░░░ BUILT BY THE OA TEAM          │
│                                             │
│  Sources: impots.gouv.fr, PWC, EU TEDB      │
│  Research date: April 2026                  │
│  Not independently checked                  │
│  Check it: openaccountants.com/verify       │
└─────────────────────────────────────────────┘
```

---

## How a skill becomes Checked by a second accountant

1. A credentialed practitioner in the jurisdiction picks up the skill.
2. They review the rates, thresholds, forms, and deadlines against current law.
3. They run the skill against representative or real client data.
4. They submit corrections (web form at openaccountants.com or GitHub PR).
5. A skill maintainer merges the corrections; the skill is tagged with the practitioner's name and license number.
6. The skill becomes **Checked by <name>** in the next release.

The practitioner is credited publicly. Their profile lists all the skills they have checked.

---

## Authoritative research sources

These are the sources a team-built skill must be drafted and cross-checked against. The same sources are recommended to accountants checking their jurisdiction.

### Global / multi-jurisdiction

| Source | URL pattern | What it covers |
|--------|------------|----------------|
| **Deloitte Tax skills** | dits.deloitte.com | VAT/GST rates, thresholds, compliance |
| **EY Worldwide Tax skill** | ey.com/en_gl/tax-guides | Country-by-country tax overviews |
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

Attribution states describe who stands behind a skill, not a guarantee that any specific output is correct. LLMs hallucinate, tax law changes, and individual circumstances vary. Every output must be reviewed by a qualified professional before filing.
