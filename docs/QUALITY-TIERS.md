# OpenAccountants — Skill Quality Tiers

How we measure whether a skill is actually ready for production use.

---

## The five quality tiers

| Tier | Label | What it means | Badge |
|------|-------|--------------|-------|
| **Q1** | **Battle-tested** | Skill has been run against real client bank statements, real transactions, and real filings. Gone through multiple iterations. Output was reviewed and signed off by a licensed practitioner. Errors found during real use have been corrected. This skill has survived contact with reality. | `battle-tested` |
| **Q2** | **Research-verified, Q1 format** | Skill follows the Q1 execution format (Step 0 → Step N). Every rate, threshold, form number, and deadline has been cross-checked against authoritative sources via deep research. Structure matches the battle-tested skills exactly. But it has not yet been tested against real transaction data. | `verified` |
| **Q3** | **AI-drafted** | Skill was drafted by Claude from training data. May be in Step format (119 skills) or Section format (56 skills). Has citations, edge cases, test suites — but facts have not been independently verified and format may not match Q1. | `draft` |
| **Q4** | **Stub with metadata** | Skill file exists with correct frontmatter, scope statement, and dependency chain, but computation rules and rates are placeholder or empty. | `stub` |
| **Q5** | **Planned** | Skill is listed in the taxonomy but no file exists yet. | — |

---

## What separates each tier

### Q3 → Q2: Restructure + deep research (no human needed)

This is entirely automatable with Claude Code. Two things must happen:

#### A. Restructure to Q1 format

The skill must follow the exact execution order proven in battle-tested skills:

```
## Skill Metadata                          ← who, what, where
## Confidence Tier Definitions             ← T1/T2/T3 rules
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

**Key format rules from Q1 skills:**
- Step 0 (onboarding) is ALWAYS first — never buried at the end
- Box/line assignments are **deterministic lookup tables**, not narrative text
- Classification matrix uses **tables**, not paragraphs
- No "Overview" or "What is VAT?" sections — this is an execution skill, not a textbook
- Every rule tagged with confidence tier [T1], [T2], or [T3]
- PROHIBITIONS section before edge cases

**56 skills currently in Section format need this restructure.**
**119 skills already in Step format — may need minor alignment.**

#### B. Deep research verification

Every fact in the skill must be cross-checked against authoritative sources. The agent runs deep research and verifies:

| What to verify | Authoritative source |
|---------------|---------------------|
| VAT/GST/sales tax rates | Tax authority website, EU TEDB, PWC Tax Summaries |
| Form numbers and names | Tax authority filing portal |
| Filing deadlines | Tax authority calendar / guidance |
| Registration thresholds | Tax authority registration page |
| Penalty rates | Tax code / tax authority penalty guidance |
| Reverse charge rules | Tax code articles, EU VAT Directive art. 196 |
| Blocked input categories | Tax code (deductibility restrictions) |
| Invoice requirements | Tax code / e-invoicing regulations |

**Sources by region (see Part 3 below for full list).**

After restructure + deep research verification, the skill is Q2.

---

### Q2 → Q1: Real transaction data + multiple iterations

This requires humans and real data. Cannot be automated.

1. Real bank statements are classified using the skill's rules
2. Output is compared against a manually-prepared return
3. Discrepancies are investigated and the skill is corrected
4. The skill goes through **multiple iterations** — each real-world use exposes new edge cases
5. A licensed practitioner reviews the output and would sign the return
6. At least one complete filing cycle has been completed

**This is how Malta, Germany, and US federal skills reached Q1.** It wasn't one pass — it was iterations against real data until the skill stopped producing errors.

---

## Part 2 — Current inventory

### Q1 — Battle-tested (7 skills)

| Skill | Jurisdiction | Iterations | Data |
|-------|-------------|------------|------|
| `malta-vat-return` | Malta | Multiple | Real VAT3 filings |
| `malta-income-tax` | Malta | Multiple | Real TA24 data |
| `malta-ssc` | Malta | Multiple | Real Class 2 SSC data |
| `germany-vat-return` | Germany | Multiple | Real bank statements |
| `us-sole-prop-bookkeeping` | US Federal | Multiple | Real freelancer data |
| `us-schedule-c-and-se-computation` | US Federal | Multiple | Real Schedule C data |
| `us-ca-freelance-intake` | US-CA | Multiple | Real intake sessions |

### Q2 — Research-verified, Q1 format (9 skills)

| Skill | Jurisdiction | Notes |
|-------|-------------|-------|
| `france-vat-return` | France | Deep researched, Q1 format |
| `italy-vat-return` | Italy | Deep researched, Q1 format |
| `ny-it-201-resident-return` | US-NY | Deep researched, Q1 format |
| `ny-llc-filing-fee-it-204-ll` | US-NY | Deep researched, Q1 format |
| `us-federal-return-assembly` | US Federal | Orchestrator, reviewed |
| `us-ca-return-assembly` | US-CA | Orchestrator, reviewed |
| `eu-vat-directive` | EU | Directive layer, reviewed |
| `vat-workflow-base` | Global | Infrastructure, reviewed |
| `us-tax-workflow-base` | Global | Infrastructure, reviewed |

### Q3 — AI-drafted (175 skills)

| Format | Count | Action needed |
|--------|-------|--------------|
| Step format (correct structure) | 119 | Deep research verification only |
| Section format (wrong structure) | 56 | Restructure + deep research |

### Q4 — Stubs (~60 skills)

Income tax, social contributions, estimated tax stubs across all jurisdictions.

### Q5 — Planned

Skills in taxonomy with no file yet.

---

## Part 3 — Deep research sources by region

These are the authoritative sources agents should use to verify Q3 skills.

### Global / multi-jurisdiction

| Source | URL pattern | What it covers |
|--------|------------|----------------|
| **PWC Worldwide Tax Summaries** | taxsummaries.pwc.com | Income tax, VAT/GST rates, filing for 150+ countries |
| **Deloitte Tax Guides** | dits.deloitte.com | VAT/GST rates, thresholds, compliance requirements |
| **EY Worldwide Tax Guide** | ey.com/en_gl/tax-guides | Country-by-country tax overviews |
| **KPMG Tax Rates Online** | kpmg.com/tax-rates | Corporate/individual/indirect tax rates |
| **OECD Tax Database** | oecd.org/tax/tax-policy | Standardised cross-country tax data |
| **Trading Economics** | tradingeconomics.com/country-list/sales-tax-rate | Quick rate verification |

### European Union

| Source | URL | What it covers |
|--------|-----|----------------|
| **EU TEDB** (Taxes in Europe Database) | ec.europa.eu/taxation_customs/tedb | Official EU VAT rates for all 27 member states |
| **EC VAT Information Exchange System** | ec.europa.eu/taxation_customs/vies | VAT number validation |
| **VAT Expert Group publications** | ec.europa.eu | Directive interpretations |

### Country-specific tax authority websites

| Country | Tax authority | URL |
|---------|--------------|-----|
| **UK** | HMRC | gov.uk/government/organisations/hm-revenue-customs |
| **Canada** | CRA | canada.ca/en/revenue-agency |
| **Australia** | ATO | ato.gov.au |
| **New Zealand** | IRD | ird.govt.nz |
| **Ireland** | Revenue | revenue.ie |
| **Germany** | BZSt/Finanzamt | bzst.de, elster.de |
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

| State | Authority | URL |
|-------|----------|-----|
| **California** | CDTFA | cdtfa.ca.gov |
| **New York** | DTF | tax.ny.gov |
| **Texas** | Comptroller | comptroller.texas.gov |
| **Florida** | DOR | floridarevenue.com |
| **Illinois** | IDOR | tax.illinois.gov |
| **Washington** | DOR | dor.wa.gov |

*All 45 sales-tax states have online portals. Agent should search "[State] department of revenue sales tax" for the correct URL.*

---

## Part 4 — The Q3 → Q2 automation pipeline

For each Q3 skill, an agent runs this exact process:

```
1. READ the current skill file
2. CHECK format:
   - If Section format → RESTRUCTURE to Step format (Q1 order)
   - If Step format → CHECK alignment with Q1 section order
3. DEEP RESEARCH — for each factual claim:
   a. Hit the tax authority website (primary source)
   b. Cross-check against PWC Tax Summaries (secondary source)
   c. If discrepancy → flag and use tax authority as truth
4. UPDATE the skill:
   - Correct any wrong rates, form numbers, thresholds, deadlines
   - Add missing [T1]/[T2]/[T3] tags
   - Ensure PROHIBITIONS section exists
   - Ensure Test Suite has at least 5 tests
   - Ensure Edge Case Registry has at least 5 cases
   - Add/update Validated By field: "Deep research verification, [date]"
5. ADD disclaimer if missing
6. MARK as Q2 in skill metadata
```

**Estimated time per skill:** 10–20 minutes per agent run
**Estimated total for 175 Q3 skills:** ~30–50 agent-hours

---

## Part 5 — What the user sees

```
┌─────────────────────────────────────────────┐
│  Malta VAT Return (VAT3) v1.0               │
│  ████████████ BATTLE-TESTED (Q1)            │
│                                             │
│  Verified by: Michael Cutajar, CPA          │
│  Tested against: Real client data           │
│  Iterations: Multiple filing cycles         │
│  Last updated: March 2026                   │
└─────────────────────────────────────────────┘

┌─────────────────────────────────────────────┐
│  France VAT Return (CA3) v0.1               │
│  ▓▓▓▓▓▓▓▓░░░░ VERIFIED (Q2)                │
│                                             │
│  Format: Q1 structure                       │
│  Verified via: Deep research, April 2026    │
│  Sources: impots.gouv.fr, PWC, EU TEDB      │
│  Tested against real data: Not yet          │
└─────────────────────────────────────────────┘

┌─────────────────────────────────────────────┐
│  Honduras ISV Return v1.0                   │
│  ░░░░░░░░░░░░ DRAFT (Q3)                    │
│                                             │
│  Format: Step (correct)                     │
│  Verified: Not yet                          │
│  ⚠ Facts not independently verified.       │
│  Help verify: openaccountants.com/verify    │
└─────────────────────────────────────────────┘
```
