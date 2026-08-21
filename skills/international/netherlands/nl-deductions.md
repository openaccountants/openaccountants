---
name: nl-deductions
description: Use this skill whenever asked about Dutch tax deductions and special schemes (aftrekposten en regelingen) beyond self-employed deductions. Trigger on phrases like "aftrekposten", "belastingaftrek", "deductions Netherlands", "hypotheekrenteaftrek", "mortgage interest deduction", "eigenwoningforfait", "specifieke zorgkosten", "giftenaftrek", "studiekosten", "alimentatie aftrek", "persoonsgebonden aftrek", "partnerregeling", "heffingskorting", "ouderenkorting", "jonggehandicaptenkorting", "levensloopvrijstelling", "box 3 vrijstelling", "groene belegging", "ANBI", "kom ik in aanmerking", "tax deduction check NL", or any question about Dutch individual or business tax deductions, credits, or special regimes. This skill covers persoonsgebonden aftrek, hypotheekrenteaftrek, zorgkosten, giften, heffingskortingen, and business investment schemes. ALWAYS read this skill before advising on Dutch deduction eligibility.
version: 1.0
jurisdiction: NL
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# NL Deductions

## Netherlands Tax Deductions & Schemes — Aftrekposten en Regelingen v1.0

> **Based on work by [John in 't Hout (@johnhout)](https://github.com/johnhout/knowledge-work-belastingzaken)**, licensed under MIT. Adapted for the OpenAccountants format.

## Section 1 — Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Netherlands (Koninkrijk der Nederlanden) |
| Scope | Personal deductions (persoonsgebonden aftrek), property deductions, tax credits (heffingskortingen), special schemes |
| Currency | EUR only |
| Tax year | Calendar year (1 January — 31 December) |
| Primary legislation | Wet inkomstenbelasting 2001 (Wet IB 2001), Chapters 6 (persoonsgebonden aftrek) and 8 (heffingskortingen) |
| Tax authority | Belastingdienst |
| Filing portal | Mijn Belastingdienst via DigiD |
| Contributor | Open Accountants Community |
| Validated by | Pending — requires sign-off by a qualified Dutch belastingadviseur |
| Skill version | 1.0 |

### Deduction Categories Overview [T1]

**Deduction Categories Overview**

| Category | Type | Where Claimed |
| --- | --- | --- |
| Hypotheekrenteaftrek (mortgage interest) | Aftrekbare kosten eigen woning | Box 1 — Section eigen woning |
| Persoonsgebonden aftrek | Individual deduction | Deducted from total Box 1/2/3 income |
| Ondernemersaftrek | Business deduction | Box 1 — profit from enterprise |
| Heffingskortingen (tax credits) | Reduce tax payable | Reduces computed tax (not income) |
| Investment schemes (Box 3) | Reduced rate or exemption | Box 3 |

## Section 2 — Eigen Woning (Owner-Occupied Property)

### Hypotheekrenteaftrek — Mortgage Interest Deduction [T1]

**Hypotheekrenteaftrek — Mortgage Interest Deduction**

| Parameter | Rule 2025 |
| --- | --- |
| Deductible | Interest paid on acquisition debt (eigenwoningschuld) for primary residence |
| Maximum mortgage term | 30 years from first mortgage start date |
| Repayment requirement | Annuity or linear repayment required (for mortgages from 2013+) |
| Rate limitation | Deduction limited to max 36.97% effective rate (2025) — "Hillen" phase-in |
| Maximum acquisition debt | No cap on amount, but only for primary residence (eigen woning) |
| Legislation | Articles 3.110–3.123 Wet IB 2001 |

### Eigenwoningforfait (Imputed Rental Value) [T1]

**Eigenwoningforfait (Imputed Rental Value)**

| WOZ Value (EUR) | Percentage | Addition to Income |
| --- | --- | --- |
| 0 — 12,500 | 0.00% | EUR 0 |
| 12,500 — 25,000 | 0.10% | Variable |
| 25,000 — 50,000 | 0.20% | Variable |
| 50,000 — 75,000 | 0.30% | Variable |
| 75,000 — 1,310,000 | 0.35% | Variable |
| Above 1,310,000 | EUR 4,585 + 2.35% of excess | High-value surcharge |

**Net effect:** Eigenwoningforfait is added to income; mortgage interest is subtracted. If interest > forfait, net deduction exists.

### Aftrek geen of geringe eigenwoningschuld (Hillen-aftrek) [T1]

If eigenwoningforfait exceeds mortgage interest (e.g., mortgage fully repaid), the excess used to be fully eliminated. This is being phased out:

**Hillen reduction percentage by year**

| Year | Hillen reduction percentage |
| --- | --- |
| 2024 | 83.33% of excess eliminated |
| 2025 | 80.00% of excess eliminated |
| 2026 | 76.67% |
| ... | Declining ~3.33% per year |
| 2048 | 0% (Hillen fully eliminated) |

## Section 3 — Persoonsgebonden Aftrek (Personal Deductions)

These deductions are subtracted from taxable income across all boxes (in order: Box 1, Box 3, Box 2).

### 3.1 Alimentatie (Maintenance Payments) [T1]

**Alimentatie (Maintenance Payments)**

| Rule | Detail |
| --- | --- |
| Deductible | Periodic spousal maintenance (partneralimentatie) |
| NOT deductible | Child maintenance (kinderalimentatie) — not since 2015 |
| Rate limitation | Deductible at max 36.97% (2025) |
| Evidence required | Court order or notarial agreement + proof of payment |
| Legislation | Article 6.3 Wet IB 2001 |

### 3.2 Specifieke Zorgkosten (Medical Expenses) [T1]

**Specifieke Zorgkosten (Medical Expenses)**

| Rule | Detail |
| --- | --- |
| Scope | Expenses not reimbursed by insurance: dental, physiotherapy, prescribed medication, disability aids, transport to medical care, dietary requirements (dietist-prescribed) |
| Threshold | Only excess above income-dependent drempel is deductible |
| Drempel calculation | Based on drempelinkomen (threshold income); ranges from 1.65% to 13.3% |
| Multiplication factor | Some costs multiplied by factor (e.g., specific chronic illness costs ×1.13 or ×1.40) |
| Legislation | Articles 6.16–6.20 Wet IB 2001 |

**Drempel (threshold) 2025:**

**Drempel (threshold) 2025**

| Drempelinkomen (EUR) | Threshold |
| --- | --- |
| Up to EUR 9,344 | 1.65% |
| EUR 9,344 — EUR 46,724 | EUR 154 + 5.75% of income above EUR 9,344 |
| Above EUR 46,724 | EUR 2,303 + 1.65% of income above EUR 46,724 |

### 3.3 Giftenaftrek (Charitable Donations) [T1]

**Giftenaftrek (Charitable Donations)**

| Type | Rule |
| --- | --- |
| Gewone giften (regular donations) | Deductible above 1% of drempelinkomen (min EUR 60); max 10% of drempelinkomen |
| Periodieke giften (periodic donations) | Fully deductible; no floor or ceiling |
| Requirement for periodieke giften | Written agreement (notarieel or onderhandse akte) for ≥5 years |
| Qualifying recipients | ANBI-registered institutions; SBBI for periodic |
| Rate limitation | Deductible at max 36.97% (2025) |
| Legislation | Articles 6.32–6.39 Wet IB 2001 |

### 3.4 Studiekosten (Study Expenses) [T1]

**Studiekosten (Study Expenses)**

| Rule | Detail |
| --- | --- |
| Status 2025 | ABOLISHED since 2022. Replaced by STAP-budget (government scheme, not tax deduction) |
| Exception | If study costs were committed before 2022 under old rules, transitional rules may apply — flag for advisor |

### 3.5 Weekenduitgaven Gehandicapten (Disabled Dependents) [T1]

**Weekenduitgaven Gehandicapten (Disabled Dependents)**

| Rule | Detail |
| --- | --- |
| Deductible | Extra costs of caring for a severely disabled person (21+) who regularly visits |
| Amount | Fixed amounts per day/overnight; depends on age and frequency |
| Legislation | Article 6.25 Wet IB 2001 |

## Section 4 — Heffingskortingen (Tax Credits)

Tax credits reduce the computed tax (not the taxable income). They are applied after tax computation.

### Main Credits 2025 [T1]

**Main Credits 2025**

| Credit | Maximum Amount (EUR) | Phase-out | Notes |
| --- | --- | --- | --- |
| Algemene heffingskorting | 3,068 | Phases out from EUR 24,813 to EUR 76,817 income | Universal; reduces to EUR 0 at top |
| Arbeidskorting (employment credit) | 5,174 | Phases out above EUR 43,071 | For those with employment/business income |
| Inkomensafhankelijke combinatiekorting (IACK) | 2,950 | Requires youngest child < 12 and > EUR 6,073 income | Working parent credit |
| Ouderenkorting (elderly credit) | 2,010 | Phases out above EUR 44,770 | For those at/above AOW age |
| Alleenstaande-ouderenkorting | 524 | No phase-out | Single elderly receiving AOW supplement |
| Jonggehandicaptenkorting | 898 | No phase-out | For those with Wajong benefit |
| Levensloopverlofkorting | EUR 238 × participation years | Max based on years deposited | Transitional; levensloop scheme ended |
| Korting groene beleggingen | 0.7% of Box 3 green investment value | Max EUR 65,072 per person | For green investment funds |

### Algemene Heffingskorting Phase-Out Formula [T1]

- **Algemene Heffingskorting Phase-Out Formula** — If income ≤ EUR 24,813: full EUR 3,068 If income between EUR 24,813 and EUR 76,817: Reduction = 5.902% × (income − EUR 24,813) Credit = EUR 3,068 − reduction If income ≥ EUR 76,817: EUR 0

### Arbeidskorting Phase-Out Formula [T1]

- **Arbeidskorting Phase-Out Formula** — If income ≤ EUR 11,491: 8.425% × income If EUR 11,491 – EUR 24,821: EUR 968 + 29.861% × (income − EUR 11,491) If EUR 24,821 – EUR 43,071: EUR 4,947 + 1.248% × (income − EUR 24,821) If EUR 43,071 – EUR 124,935: EUR 5,174 − 6.317% × (income − EUR 43,071) If income > EUR 124,935: EUR 0

## Section 5 — Business Investment Deductions

### KIA — Kleinschaligheidsinvesteringsaftrek [T1]

**KIA — Kleinschaligheidsinvesteringsaftrek**

| Total Investment (EUR) | Deduction |
| --- | --- |
| 0 — 2,900 | No deduction |
| 2,901 — 70,602 | 28% of investment amount |
| 70,603 — 130,744 | EUR 19,769 (fixed) |
| 130,745 — 392,230 | EUR 19,769 minus 7.56% of amount exceeding EUR 130,744 |
| > 392,230 | No deduction |

- **KIA Conditions** — Per qualifying asset: minimum EUR 450 investment. Excludes: land, residential property, passenger cars, securities, goodwill.  _(Article 3.41 Wet IB 2001)_

### EIA — Energie-investeringsaftrek (Energy Investment) [T1]

**EIA — Energie-investeringsaftrek (Energy Investment)**

| Parameter | Value 2025 |
| --- | --- |
| Rate | 45.5% of qualifying investment |
| Minimum per asset | EUR 2,500 |
| Maximum total per year | EUR 136,000,000 (per entity; effectively unlimited for SME) |
| Qualification | Must be on Energielijst (published annually by RVO) |
| Application | Within 3 months of commitment (opdrachtbevestiging) to RVO |
| Legislation | Article 3.42 Wet IB 2001 |

### MIA/Vamil — Milieu-investeringsaftrek / Willekeurige Afschrijving [T1]

**MIA/Vamil — Milieu-investeringsaftrek / Willekeurige Afschrijving**

| Scheme | Benefit |
| --- | --- |
| MIA | 27%, 36%, or 45% additional deduction on qualifying environmental investments |
| Vamil | Accelerated depreciation (75% in year 1) on qualifying investments |
| Qualification | Must be on Milieulijst (published annually by RVO) |
| Application | Within 3 months of purchase commitment to RVO |
| Legislation | Articles 3.42a–3.42b Wet IB 2001 |

### WBSO — R&D Tax Credit [T1]

**WBSO — R&D Tax Credit**

| Parameter | Value 2025 |
| --- | --- |
| First bracket rate | 32% on first EUR 350,000 R&D costs |
| Second bracket rate | 16% on excess above EUR 350,000 |
| Starters bonus | 40% first bracket rate (first 5 years) |
| Benefit type | Reduction in payroll tax liability (loonheffingen) |
| Application | RVO — before start of R&D period |
| Legislation | Wet vermindering afdracht loonbelasting en premie voor de volksverzekeringen (WVA) |

## Section 6 — Box 3 Relevant Deductions & Exemptions

### Box 3 Tax-Free Allowance 2025 [T1]

**Box 3 Tax-Free Allowance 2025**

| Parameter | Value |
| --- | --- |
| Heffingsvrij vermogen (per person) | EUR 57,000 |
| Fiscal partners (combined) | EUR 114,000 |

### Green Investment Exemption [T1]

**Green Investment Exemption**

| Parameter | Value |
| --- | --- |
| Exempt amount (Box 3) | Up to EUR 65,072 per person in qualifying green funds |
| Tax credit | 0.7% of exempt green investment value (separate from Box 3 exemption) |
| Qualification | Investment must be in certified groene instelling |

## Section 7 — Evidence Requirements and Conservative Defaults

### Evidence Checklist Per Deduction [T1]

**Evidence Checklist Per Deduction**

| Deduction | Required Evidence |
| --- | --- |
| Hypotheekrenteaftrek | Mortgage deed, annual interest statement (jaaropgave), WOZ description |
| Specifieke zorgkosten | Medical invoices, insurance rejection letters, prescriptions, dietist declaration |
| Giften (regular) | Bank statements showing payments to ANBI, donation receipts |
| Giften (periodic) | Signed donation agreement (≥5 year), bank statements |
| Alimentatie | Court order or notarial deed, bank transfer proof |
| KIA | Purchase invoices (≥ EUR 450 per asset), asset register |
| EIA/MIA | RVO confirmation (meldingsnummer), invoice, Energie/Milieulijst reference |

### Conservative Defaults [T1]

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Mortgage type unclear (pre/post 2013) | Apply strictest rules (annuity repayment required) — flag |
| Medical expense reimbursement status unknown | Assume reimbursed (not deductible) — flag for client to confirm |
| ANBI status of charity unconfirmed | Do NOT deduct — verify on belastingdienst.nl ANBI register |
| Gift agreement duration unclear | Treat as regular gift (with floor and ceiling) — flag |
| Investment qualifying for EIA/MIA not confirmed | Do NOT apply — verify on RVO Energielijst/Milieulijst |
| Partner allocation unclear | Do NOT split deductions — flag for client |
| Eigenwoningforfait WOZ value unknown | Cannot compute — request WOZ-beschikking |

### Red Flags [T1]

**Red Flags**

| Flag | Issue |
| --- | --- |
| Mortgage interest > 30% of gross income | High debt burden — verify loan documentation |
| Medical deductions > EUR 5,000 | Verify all items have supporting documentation |
| Charitable gifts > 10% of income | Exceeds ceiling for regular gifts — check if periodic |
| KIA claimed on passenger car | Not eligible — exclude |
| EIA/MIA without RVO confirmation number | Cannot claim — not valid without meldingsnummer |
| Multiple homes claimed as eigen woning | Only ONE primary residence qualifies |
| Deductions claimed for non-resident with no NL income | Kwalificerende buitenlandse belastingplichtige status needed |

## Section 8 — Computation Order

### Complete Deduction Application Order [T1]

- **Complete Deduction Application Order** — 1. Compute gross income per box: - Box 1: employment + business + property (eigen woning) - Box 2: substantial interest (aanmerkelijk belang) - Box 3: savings and investments (forfaitair) 2. Apply Box 1 business deductions (if applicable): - Zelfstandigenaftrek → Startersaftrek → MKB-winstvrijstelling - KIA, EIA, MIA (investment deductions) 3. Apply eigen woning saldo: - Eigenwoningforfait (add) − mortgage interest (subtract) = saldo - If negative: Box 1 deduction - If positive: Hillen-aftrek may eliminate part 4. Determine persoonsgebonden aftrek: - Sum of: alimentatie + zorgkosten (above drempel) + giften (above floor, within ceiling) - Deduct from Box 1 first; if Box 1 insufficient → Box 3 → Box 2 5. Compute tax per box at applicable rates 6. Apply heffingskortingen (tax credits): - Algemene heffingskorting (phase-out based on Box 1 income) - Arbeidskorting (if employment/business income exists) - Other applicable credits (IACK, ouderenkorting, etc.) 7. Final tax payable = Sum box taxes − total credits - Minimum EUR 0 (credits cannot create negative tax)

## Section 9 — Official Source Verification Requirements

Before any deduction amount, threshold, or eligibility criterion is used:

1. Verify practical deduction rules on `belastingdienst.nl/aftrek`
2. Verify statutory text on `wetten.overheid.nl` (Wet IB 2001, relevant articles)
3. For investment schemes: verify qualifying lists on `rvo.nl`
4. For ANBI status: verify on `belastingdienst.nl/anbi`
5. Record exact URL and retrieval date (YYYY-MM-DD)
6. If source unavailable or conflicting: mark as **UNVERIFIED** and require professional confirmation

## Section 10 — Escalation Points

Escalate to a qualified belastingadviseur when:

- Eigen woning qualification disputed (e.g., two residences, partial rental)
- Complex mortgage structures (multiple loans, box migration)
- Non-resident taxpayer claiming deductions (kwalificerende buitenlandse belastingplichtige)
- High-value medical expense claims requiring medical evidence review
- Partner allocation optimisation (fiscal partnership choices)
- Investment deduction eligibility disputes with Belastingdienst
- Anti-abuse provisions triggered (e.g., recycling box migration)
- Transitional rules from abolished deductions (study costs, FOR)

## Netherlands Tax Deductions & Schemes — Aftrekposten en Regelingen v1.0

**⚠️ DISCLAIMER: This skill provides workflow support only and does not constitute tax advice. All deduction positions must be reviewed and signed off by a qualified Dutch belastingadviseur before filing. Thresholds and amounts change annually — verify all figures against belastingdienst.nl for the applicable tax year.**

---

*OpenAccountants — open-source accounting skills for AI*
*openaccountants.com*

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is
different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your
jurisdiction — **no liability on either side until you and the accountant sign
a formal engagement letter** — book a free 30-minute call:

**→ [Book a call](https://calendly.com/openaccountants-info/30min)**

We'll route you to the named verifier covering your country or state. You can
also see the full list of verified accountants at
[openaccountants.com/network](https://openaccountants.com/network).

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
