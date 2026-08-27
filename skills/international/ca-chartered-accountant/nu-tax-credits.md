---
name: nu-tax-credits
description: Use this skill for Nunavut provincial tax credits — Nunavut Cost of Living Tax Credit, Nunavut Volunteer Firefighters Tax Credit, Nunavut Carbon Credit, Nunavut Risk Capital Investment Tax Credit (45% — highest in Canada). Triggers "Nunavut tax credits", "Nunavut Cost of Living", "Form NU428", "Nunavut Risk Capital", "NRCITC".
jurisdiction: CA
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# NU Tax Credits

## Nunavut — Provincial Tax Credits — Skill v1.0

This skill consolidates Nunavut's personal and corporate tax credits for tax year 2025. Nunavut is a small jurisdiction (population ~40,000) but uses tax credits aggressively to offset the territory's extreme cost of living and attract risk capital into a remote economy. The headline incentive — the Nunavut Risk Capital Investment Tax Credit (NRCITC) at **45%** — is the most generous angel investor credit in Canada.

This skill MUST be loaded alongside `ca-tax-workflow-base` (workflow scaffolding) and, where personal income is involved, the federal individual return skill. It does not replace federal credits; it layers Nunavut-specific credits on top of the federal computation via Form NU428 (personals) and the Nunavut corporate schedule (T2 SCH 481 equivalent).

## 1. Quick reference — personal + corporate credit summary

### Personal credits (Form NU428)

**Personal credits (Form NU428)**

| Credit | Type | 2025 amount | Notes |
| --- | --- | --- | --- |
| Nunavut Cost of Living Tax Credit | Non-refundable | Up to ~$1,200 territorial tax reduction | Recognises high cost of living in NU; reduces NU tax payable only, no carryforward |
| Nunavut Volunteer Firefighters Tax Credit | Non-refundable | $500 (15% × $3,000) | Mirrors federal VFA but stacks on NU return |
| Nunavut Carbon Credit | Refundable | Paid quarterly | Delivered alongside federal Canada Carbon Rebate (formerly CAI) |
| Nunavut Children's Activity Tax Credit | Non-refundable | Up to $500/child | Eligible physical-activity programs |
| Nunavut Risk Capital Investment Tax Credit | Non-refundable (corporate or individual) | **45%** of eligible investment | Max $1M investment / yr → max $450k credit; 7-yr carryforward |

### Corporate (Form T2 SCH 481 — Nunavut credits)

**Corporate (Form T2 SCH 481 — Nunavut credits)**

| Credit | Rate | Notes |
| --- | --- | --- |
| Nunavut general CIT | 12% | On taxable income > SBD limit |
| Nunavut small business CIT | 3% | On first $500k active business income |
| Nunavut Business Training Credit | Refundable | Eligible training expenditure |
| NRCITC (corporate investor) | 45% | Same cap as individual side |

### Combined federal + Nunavut CIT rates (2025)

- **Active income up to $500k SBD** — 9% (federal) + 3% (NU) = 12% combined  _(Combined federal + Nunavut CIT rates (2025))_
- **Active income above SBD** — 15% (federal) + 12% (NU) = 27% combined  _(Combined federal + Nunavut CIT rates (2025))_

## 2. Required inputs + refusal catalogue

### Required inputs

For personal credits via Form NU428:
- Federal Schedule 1 / Form T1 line 26000 (taxable income) and line 11700 (basic personal amount carryover)
- Residency on Dec 31, 2025: must be a resident of Nunavut to claim NU428 credits
- Receipts for volunteer firefighter hours (200+ hours of eligible service)
- Eligible children's activity program receipts
- NRCITC certificate (T2C-NU) from the Nunavut Business Credit Corporation confirming investment registration

For corporate Nunavut credits:
- T2 Schedule 5 (provincial/territorial allocation by permanent establishment)
- Allocation factor for Nunavut PE
- Active business income figures by jurisdiction
- NRCITC certificate from Nunavut Business Credit Corporation

### Refusal catalogue

- **R-NU-1** — Non-resident of Nunavut at year-end — NU428 credits unavailable; route to actual province of residence  _(Refusal catalogue)_
- **R-NU-2** — Partial-year residency — proration rules require advisor judgement  _(Refusal catalogue)_
- **R-NU-3** — NRCITC claim without a valid T2C-NU certificate  _(Refusal catalogue)_
- **R-NU-4** — Investment in a non-registered Nunavut business (NRCITC requires the issuer to be registered with the Nunavut Business Credit Corporation before share issuance)  _(Refusal catalogue)_
- **R-NU-5** — Inuit-owned business structures involving land claims trusts or Inuit-owned corporations under the Nunavut Land Claims Agreement — defer to advisor familiar with Article 29 economic measures  _(Refusal catalogue)_
- **R-NU-6** — Multi-jurisdictional corporate allocation where Nunavut PE allocation is contested  _(Refusal catalogue)_
- **R-NU-7** — Tax-shelter or limited-partnership structures using NRCITC — high audit risk, requires advisor signoff  _(Refusal catalogue)_

## 3. Nunavut Cost of Living Tax Credit

- **Nunavut Cost of Living Tax Credit** — A non-refundable credit unique to Nunavut. It recognises that Nunavut residents face the highest consumer prices in Canada — food, fuel, housing, and freight costs are 2-3x the southern Canadian average.  _(3. Nunavut Cost of Living Tax Credit)_
- **Mechanics (2025)** — Computed as a fixed dollar amount times a credit rate (4% — Nunavut's lowest territorial bracket rate), then deducted from Nunavut tax payable on Form NU428. Available to all Nunavut residents on Dec 31, 2025. Cannot reduce NU tax below zero; no carryforward. Does NOT interact with the federal Northern Residents Deduction (T2222) — they are separate. The Northern Residents Deduction reduces federal taxable income; the Cost of Living Tax Credit reduces NU territorial tax. Both apply.  _(3. Nunavut Cost of Living Tax Credit)_

Conservative default: assume the maximum where the taxpayer has been resident in NU for the full year and has earned income above the basic personal amount. Reviewer confirms residency days from utility bills, GN payroll, or housing records.

## 4. Nunavut Volunteer Firefighters Tax Credit

- **Nunavut Volunteer Firefighters Tax Credit** — Non-refundable territorial credit mirroring the federal Volunteer Firefighters Amount (VFA) but stackable on the NU return.  _(4. Nunavut Volunteer Firefighters Tax Credit)_
- **Mechanics** — $500 credit (computed as 4% × $12,500 territorial claim amount, rounded — effectively a flat $500 reduction). Requires at least 200 hours of eligible volunteer firefighter or search-and-rescue service in the year. Cannot be combined with the Search and Rescue Volunteers Amount for the same hours. Must obtain a written certification from the fire chief or SAR coordinator.  _(4. Nunavut Volunteer Firefighters Tax Credit)_
- **Form line** — NU428 line 58315 (Nunavut version of federal line 31220).  _(4. Nunavut Volunteer Firefighters Tax Credit)_

## 5. Nunavut Carbon Credit

- **Nunavut Carbon Credit** — Refundable credit delivered quarterly alongside the federal Canada Carbon Rebate (CCR, formerly Climate Action Incentive Payment).  _(5. Nunavut Carbon Credit)_
- **Mechanics (2025)** — Paid automatically based on the prior-year T1 filing — no separate claim form. Amount varies by family composition; supplements the federal CCR. Rural supplement does NOT apply because all of Nunavut is treated as a single zone under the federal carbon pricing backstop. Delivery: CRA direct deposit; quarterly schedule aligned with federal CCR (April, July, October, January).  _(5. Nunavut Carbon Credit)_
- **Eligibility** — Nunavut resident on the first day of the payment month, 19 or older (or has spouse/dependent child).  _(5. Nunavut Carbon Credit)_

Caveat: following the federal Government's March 2025 decision to set the consumer fuel carbon price to zero, the Carbon Credit amounts for 2025 reflect a partial-year regime. Reviewer confirms post-April 2025 payment schedule.

## 6. Nunavut Risk Capital Investment Tax Credit (NRCITC)

- **NRCITC** — The headline credit. The NRCITC offers a 45% non-refundable credit on qualifying equity investments in registered Nunavut businesses. This is the highest provincial/territorial angel investor credit in Canada (BC's EBC is 30%; Manitoba's Small Business Venture Capital is 45% but capped much lower; Nova Scotia's Innovation Equity Tax Credit is 35-45%).  _(6. Nunavut Risk Capital Investment Tax Credit (NRCITC))_
- **NRCITC rate** — 45% percent (of the eligible investment amount)  _(6. Nunavut Risk Capital Investment Tax Credit (NRCITC))_
- **Maximum investment per investor per year** — $1,000,000  _(6. Nunavut Risk Capital Investment Tax Credit (NRCITC))_
- **Maximum credit per investor per year** — $450,000  _(6. Nunavut Risk Capital Investment Tax Credit (NRCITC))_
- **Lifetime cap per investor** — $2,000,000 invested (= $900,000 lifetime credit)  _(6. Nunavut Risk Capital Investment Tax Credit (NRCITC))_
- **Carryforward** — 7 years for unused credit (non-refundable, so investors need NU tax payable to use it)  _(6. Nunavut Risk Capital Investment Tax Credit (NRCITC))_
- **Holding period** — investor must hold shares for at least 4 years; early disposition triggers full recapture  _(6. Nunavut Risk Capital Investment Tax Credit (NRCITC))_
- **Eligible issuer** — corporation must be registered with the Nunavut Business Credit Corporation (NBCC) BEFORE share issuance; must have at least 50% of assets and employees in Nunavut; cannot be in a restricted sector (real estate, financial services, mining of non-eligible minerals)  _(6. Nunavut Risk Capital Investment Tax Credit (NRCITC))_
- **Eligible investor** — individuals (residents or non-residents of Nunavut) and corporations; arm's length to the issuer  _(6. Nunavut Risk Capital Investment Tax Credit (NRCITC))_
- **Form / certificate** — investor receives a T2C-NU certificate from NBCC. The certificate number is entered on Form NU428 (individual) or on the corporate Nunavut credit schedule.  _(6. Nunavut Risk Capital Investment Tax Credit (NRCITC))_

Nunavut's economy depends heavily on attracting outside capital to compensate for geographic isolation, infrastructure gaps, and a small domestic capital pool. The 45% rate is a deliberate policy lever from the Government of Nunavut and Nunavut Business Credit Corporation to drive equity formation in Iqaluit, Rankin Inlet, and Cambridge Bay.

- **Stacking with federal** — the NRCITC is in addition to any federal SR&ED or CEE/CDE deductions the issuer flows through. No federal credit equivalent exists, so there's no federal grind.  _(6. Nunavut Risk Capital Investment Tax Credit (NRCITC))_

Conservative default: require the T2C-NU certificate before claiming. Without the certificate, the credit is refused and routed to NBCC for issuance.

## 7. Nunavut Corporate Tax

**Nunavut corporate tax rates**  _(7. Nunavut Corporate Tax)_

| Bracket | Rate | Applies to |
| --- | --- | --- |
| Small business | **3%** | First $500,000 of active business income (the SBD limit, matching federal) |
| General | **12%** | Active business income above $500k, plus M&P and investment income (no separate M&P rate) |

- **Combined (federal + Nunavut) SBD active income** — 9% federal + 3% NU = 12% combined  _(7. Nunavut Corporate Tax)_
- **Combined (federal + Nunavut) General active income** — 15% federal + 12% NU = 27% combined  _(7. Nunavut Corporate Tax)_
- **Allocation** — corporations with permanent establishments inside and outside Nunavut allocate taxable income using the standard two-factor (wages + gross revenue) formula on T2 Schedule 5. The NU portion is taxed at NU rates.  _(7. Nunavut Corporate Tax)_
- **Refundable Nunavut Business Training Credit** — corporations carrying on business in Nunavut may claim a refundable credit on eligible training expenditures for Nunavut-resident employees. The credit covers a percentage of wages paid during approved training programs (apprenticeships, GN-recognised trades training). Reviewer to confirm rate and cap from the most recent Nunavut Budget.  _(7. Nunavut Corporate Tax)_

## 8. Nunavut Children's Activity Tax Credit

- **Nunavut Children's Activity Tax Credit** — Non-refundable credit available to Nunavut-resident parents.  _(8. Nunavut Children's Activity Tax Credit)_
- **Mechanics** — Up to $500 per child in eligible expenses (registration fees for prescribed physical-activity programs, sports clubs, supervised fitness activities). Additional $500 supplement for children eligible for the federal Disability Tax Credit. Claimed on Form NU428 by either parent (or split between them, max $500 per child total). Requires receipt from the program organiser identifying the child, dates, amount, and the activity.  _(8. Nunavut Children's Activity Tax Credit)_

Conservative default: include only receipts with explicit program-organiser certification. Equipment purchases, travel, and uniform costs are NOT eligible.

## 9. Form NU428 — claiming the credits

Form NU428 is the Nunavut provincial tax form filed with the federal T1. Key lines (2025):

**NU428 key lines (2025)**

| NU428 line | Item |
| --- | --- |
| Part A | Nunavut tax on taxable income (4% / 7% / 9% / 11.5% brackets) |
| 58040 | Basic personal amount (NU) |
| 58120 | Spouse or common-law partner amount |
| 58315 | Volunteer firefighters' / SAR amount |
| 58326 | Nunavut Children's Activity Tax Credit |
| 58440 | Nunavut Cost of Living Tax Credit |
| 58980 | Nunavut Risk Capital Investment Tax Credit (T2C-NU certificate number required) |
| 42800 | Net Nunavut tax payable (flows to T1 line 42800) |

Reviewer verifies:
1. T1 line 42800 matches NU428 bottom line
2. NRCITC certificate number entered correctly
3. Carryforward balances tracked year-over-year in a separate workpaper

## 10. Worked example — Iqaluit Inuit-owned construction company

"Aqsarniit Construction Ltd.", CCPC incorporated in Nunavut, sole permanent establishment in Iqaluit. 100% Inuit-owned (eligible under NLCA Article 24 procurement policies but tax-neutral). Tax year ending Dec 31, 2025. Active business income: $300,000 (all attributable to Nunavut PE). No investment income, no associated corporations sharing the SBD. No NRCITC claim this year.

**Computation**

| Item | Amount |
| --- | --- |
| Taxable income | $300,000 |
| SBD limit | $500,000 — all $300k eligible for SBD |
| Federal small business rate | 9% |
| Federal CIT (9% × $300,000) | $27,000 |
| Nunavut small business rate | 3% |
| Nunavut CIT (3% × $300,000) | $9,000 |
| **Total federal + NU CIT** | **$36,000** |
| **Effective combined rate** | **12.0%** |

The 12% combined rate is one of the lowest in Canada for SBD-eligible income (BC = 11%, ON = 12.2%, NS = 11.5%, AB = 11%). Inuit ownership does not generate a separate income tax credit; however, federal procurement preferences under NLCA Article 24 may significantly increase top-line revenue. That is a revenue effect, not a tax effect, and is outside this skill's scope. If the company invests in eligible Nunavut equipment, accelerated CCA classes (federal) may apply but there is no Nunavut M&P preferential rate.

## 11. Conservative defaults

When inputs are ambiguous or evidence is missing, this skill applies the following conservative defaults:

1. **Residency:** if residency status on Dec 31, 2025 is not clearly documented, REFUSE the NU428 claim and route to advisor (R-NU-1/R-NU-2).
2. **NRCITC:** never claim without a T2C-NU certificate number; never claim if the holding period (4 years) has not been confirmed.
3. **Children's Activity:** exclude any receipt that does not explicitly identify the activity as a prescribed physical-activity program.
4. **Volunteer Firefighters:** require fire chief / SAR coordinator certification of 200+ eligible hours.
5. **Cost of Living Tax Credit:** assume eligibility for full-year residents with positive NU tax payable; refuse for taxpayers with no positive NU tax (the credit is non-refundable and would be wasted — flag for advisor in case of carryforward planning, but Nunavut has NO carryforward of this credit).
6. **Corporate allocation:** for multi-jurisdictional corporations, require Schedule 5 PE allocation before applying NU rates. Refuse if the allocation is contested or unsupported (R-NU-6).
7. **Carbon Credit:** reviewer confirms quarterly payment schedule rather than computing a single annual figure — the post-April 2025 federal carbon price change creates a partial-year payment pattern.
8. **Inuit business structures:** any NLCA-related entity (Inuit Birthright Corporation, Inuit-Owned Land trust, designated Inuit organisation) is refused and routed to an advisor familiar with Article 29 (R-NU-5).

## 12. Sources

Primary authority:
- **Nunavut Income Tax Act**, R.S.N.W.T. (Nu.) 1988, c. I-1, as continued and amended for Nunavut
- **Nunavut Risk Capital Investment Tax Credit Act**, SNu 2012, c. 11 (and regulations administered by the Nunavut Business Credit Corporation)
- **Nunavut Department of Finance** — annual Budget documents and Tax Information Bulletins
  - https://www.gov.nu.ca/finance/information/personal-income-tax
  - https://www.gov.nu.ca/finance/information/corporate-income-tax
- **Nunavut Business Credit Corporation (NBCC)** — NRCITC issuer registration, T2C-NU certificate issuance, and program guidelines
  - https://www.nbcc.nu.ca/
- **Canada Revenue Agency** — Form NU428 (2025), T2 Schedule 481 (Nunavut), and the Nunavut Provincial Tax Pamphlet (5014-PC)
- **Canada-Nunavut Tax Collection Agreement** — CRA administers and collects Nunavut personal and corporate income tax on behalf of the Government of Nunavut

Secondary / interpretive:
- CRA Income Tax Folio S5-F1-C1 (residency determination — applied analogously for Nunavut residency at year-end)
- Government of Nunavut, Department of Economic Development and Transportation — guidance on Inuit-owned business definitions (not a tax authority; advisory only)

Reviewer verification (verified_by: pending) — this skill awaits sign-off from a Canadian tax professional with Nunavut-specific experience, ideally an accountant in Iqaluit or with active NRCITC files.

## End of skill v1.0.

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
