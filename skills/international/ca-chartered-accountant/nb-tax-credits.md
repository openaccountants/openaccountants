---
name: nb-tax-credits
description: Use this skill for New Brunswick provincial tax credits — NB Low-Income Tax Reduction, NB Harmonized Sales Tax Credit, Seniors' Home Renovation Tax Credit, Tuition Amount, NB Small Business Investor Tax Credit (refundable 50% for individuals), NB Film Tax Credit. Triggers "New Brunswick tax credits", "Form NB428", "NB Small Business Investor Tax Credit", "NB seniors home renovation".
jurisdiction: CA
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# NB Tax Credits

## New Brunswick — Provincial Tax Credits — Skill v1.0

This skill catalogues the principal New Brunswick (NB) provincial tax credits available to individuals and corporations for the 2025 tax year. It complements `nb-individual-return.md` (the Form NB428 computation skill) by isolating the credit mechanics, eligibility tests, application procedures, and refundability rules. NB administers most personal credits through the CRA via the federal–provincial Tax Collection Agreement; the NB Small Business Investor Tax Credit (NB SBITC) and the NB Film Tax Credit are administered directly by the Province (Department of Finance and Treasury Board and Opportunities NB).

## 1. Quick reference — personal + corporate credit summary

### Personal credits (claimed on Form NB428 or via CRA)

**Personal credits table**  _(Schedule on NB428 / Schedule NB(S12) / Schedule NB(S11) / NB-SBITC-1 certificate from NB Finance)_

| Credit | Type | 2025 amount / rate | Mechanism |
| --- | --- | --- | --- |
| NB Low-Income Tax Reduction (LITR) | Non-refundable | Reduces NB tax to zero up to threshold; phase-out 3% | Schedule on NB428 |
| NB Harmonized Sales Tax Credit (NBHSTC) | Refundable | $300 / adult + $100 / child; quarterly | Auto via T1 (CRA) |
| NB Seniors' Home Renovation Tax Credit | Refundable | 10% × eligible expenses, max $10,000 base → $1,000 credit | Schedule NB(S12) |
| NB Tuition Amount | Non-refundable | 9.40% × eligible tuition fees (post-secondary) | Schedule NB(S11) |
| NB Small Business Investor Tax Credit (individuals) | **Refundable** | **50%** of eligible investment; max $250,000 invested → $125,000 credit / year | NB-SBITC-1 certificate from NB Finance |

### Corporate / business credits

**Corporate credits table**  _(NB-SBITC-1 certificate / Application via NB Film / Schedule 360 (federal T2))_

| Credit | Type | 2025 amount / rate | Mechanism |
| --- | --- | --- | --- |
| NB SBITC (corporations & trusts) | Non-refundable, 7-year carry-forward | 15% × eligible investment; max $500,000 invested → $75,000 credit / year | NB-SBITC-1 certificate |
| NB Film Tax Credit | Refundable | 25% (resident labour) – 30% (with bonus) of eligible NB labour | Application via NB Film |
| NB Research and Development Tax Credit | Refundable | 15% of eligible SR&ED expenditures | Schedule 360 (federal T2) |

## 2. Required inputs + refusal catalogue

### Required inputs (always collect before quoting numbers)

- **Tax year** — Confirm 2025 (calendar) or fiscal year for corporates.  _(Section 2)_
- **Province of residence on 31 Dec 2025** — Must be NB for personal credits (R1 refusal if not).  _(Section 2)_
- **Family net income** — Line 23600 + spouse, for LITR and NBHSTC.  _(Section 2)_
- **Age and disability status** — Of taxpayer/spouse for the Seniors' Home Renovation Tax Credit.  _(Section 2)_
- **NB SBITC certificate (NB-SBITC-1)** — Required before claim; obtained from NB Finance after the eligible business issues qualifying shares.  _(Section 2)_
- **Eligible expense documentation** — Invoices, paid receipts, contractor licence info for the Seniors' Home Renovation credit.  _(Section 2)_
- **Eligible NB-resident labour breakdown** — For the NB Film Tax Credit.  _(Section 2)_

### Refusal catalogue

- **R-NB-C-1** — Non-resident of NB on 31 Dec 2025 — defer to province of residence; do not file NB428.  _(R-NB-C-1)_
- **R-NB-C-2** — Part-year NB resident — out of scope; refer to credentialed reviewer (proration of LITR and refundable credits is non-trivial).  _(R-NB-C-2)_
- **R-NB-C-3** — NB SBITC claim where the investor is connected to the issuing corporation (>10% control, or director/officer with prescribed exceptions) — refer to NB Finance; eligibility requires written confirmation.  _(R-NB-C-3)_
- **R-NB-C-4** — NB Film Tax Credit for a production that has NOT received a Part A certificate from NB Film before principal photography — out of scope.  _(R-NB-C-4)_
- **R-NB-C-5** — Retroactive claims older than statutory amendment window (T1: 10 calendar years; SBITC: per certificate terms) — refer to credentialed reviewer.  _(R-NB-C-5)_
- **R-NB-C-6** — Any claim involving non-arm's length transactions or share redemptions inside the SBITC 4-year hold period — out of scope; clawback rules apply.  _(R-NB-C-6)_

## 3. NB Low-Income Tax Reduction (LITR)

### Mechanics

- **Type** — Non-refundable. Reduces NB tax (line 42800) to zero but cannot create a refund.  _(Section 3)_
- **Base reduction (single)** — $818  _(Section 3, Computation (2025))_
- **Base reduction (family)** — $1,326  _(Section 3, Computation (2025))_
- **Reduction for dependant spouse / common-law partner** — $674  _(Section 3, Computation (2025))_
- **Reduction per eligible dependant child under 19** — $674  _(Section 3, Computation (2025))_
- **Phase-out rate** — 3% percent (of family net income exceeding $20,851 (single) / $35,851 (family))  _(Section 3, Computation (2025))_
- **Claim point** — Schedule built into Form NB428, Part C.  _(Section 3)_

### Eligibility

- **Eligibility conditions** — Resident of NB on 31 Dec 2025. Filed a T1 General. Only one spouse claims the family reduction.  _(Section 3)_

### Interaction

- **Interaction rule** — Applied after non-refundable tax credits but before the LITR cannot reduce NB tax below zero — any excess is forfeit. If both spouses qualify individually, the higher-income spouse generally claims to maximise the reduction; model both ways.  _(Section 3)_

## 4. NB Harmonized Sales Tax Credit (NBHSTC)

### Mechanics

- **Type** — Refundable. Paid quarterly alongside the federal GST/HST Credit. Fully integrated administration via CRA — no separate application.  _(Section 4)_
- **2025 benefit year amount per adult** — $300 CAD (per adult (taxpayer + spouse/common-law partner); benefit year July 2025 – June 2026, based on 2024 return)  _(Section 4)_
- **2025 benefit year amount per child** — $100 CAD (per child under 19)  _(Section 4)_
- **Phase-out rate** — 2% percent (of adjusted family net income above $35,000)  _(Section 4)_

### Eligibility

- **Eligibility conditions** — Resident of NB at the beginning of the payment month. Age 19+ OR has a spouse OR is a parent. Has filed a 2024 return (even with zero income) — credit is auto-calculated.  _(Section 4)_

### Practical notes

Newcomers to NB file Form RC151 once. Marital status changes must be reported via RC65 to avoid clawback. Direct deposit via CRA "My Account".

## 5. NB Seniors' Home Renovation Tax Credit

### Mechanics

- **Type** — Refundable.  _(Section 5)_
- **Rate** — 10% percent (of eligible expenses)  _(Section 5)_
- **Cap** — Eligible expenses up to $10,000 per year, so maximum credit = $1,000 / year  _(Section 5)_
- **Claim** — Schedule NB(S12) attached to T1; reported on Form NB428 line 47900.  _(Section 5)_

### Eligibility

- **Eligibility conditions** — Taxpayer is 65+ at end of year OR lives with a senior family member who is 65+, OR the senior is the spouse/common-law partner. Renovation is to the principal residence in NB. Purpose: improve accessibility, mobility, or reduce risk of harm for the senior (e.g., grab bars, walk-in tubs, ramps, stair lifts, non-slip flooring, lever handles, widened doorways). Expenses must be paid in the calendar year (or by 31 Jan of the following year for arrangements entered before year-end, per CRA practice).  _(Section 5)_

### Ineligible expenses

- **Ineligible expenses** — Routine repairs and maintenance (roof, painting, landscaping not accessibility-related). Appliances and electronics not attached to the dwelling. Services performed by a non-arm's length person who is not GST/HST registered.  _(Section 5)_

### Documentation

Itemised invoices showing GST/HST and contractor's BN. Proof of payment. Photos optional but useful on audit.

## 6. NB Small Business Investor Tax Credit (NB SBITC)

The NB SBITC is one of the most generous angel-investor credits in Canada because the individual rate is refundable at 50%. Most other provinces cap their analogues at 30% non-refundable.

### Statutory basis

- **Statutory basis** — Small Business Investor Tax Credit Act (SNB 2003, c S-9.05) and regulations. Administered by NB Department of Finance and Treasury Board, Revenue Administration Division.  _(Small Business Investor Tax Credit Act (SNB 2003, c S-9.05))_

### Rates and caps (2025)

**Rates and caps table**  _(Section 6, Rates and caps (2025))_

| Investor type | Rate | Max eligible investment / year | Max credit / year | Refundability |
| --- | --- | --- | --- | --- |
| Individual | **50%** | $250,000 | **$125,000** | **Refundable** |
| Corporation or trust | 15% | $500,000 | $75,000 | Non-refundable; 7-year carry-forward, 3-year carry-back |

### Eligible investment — what qualifies

- **What qualifies** — Newly issued equity (common voting shares; certain preferred shares) of a registered Eligible Business Corporation (EBC), Community Economic Development Corporation (CEDC), or Co-operative.  _(Section 6)_
- **Issuing corporation requirements** — Be registered with NB Finance and hold a current SBITC registration certificate. Have a permanent establishment in NB. Have no more than 75 employees at registration. Have at least 75% of wages/salaries paid to NB residents (or 50% if engaged in export). Use the funds for active business operations (not money lending, real estate development for resale, financial services, retail not adding value, professional practices reserved to regulated members, or activities offending public policy).  _(Section 6)_
- **Minimum hold period** — Investor must hold the shares for 4 years. Early redemption, sale to a non-arm's length party, or wind-up triggers clawback of the credit.  _(Section 6)_

### Application workflow

0. **Step 1** — Eligible business applies for and receives the SBITC registration certificate from NB Finance.
0. **Step 2** — Investor subscribes for qualifying shares; funds are paid to the corporation.
0. **Step 3** — Corporation issues Form NB-SBITC-1 (Tax Credit Certificate) to the investor after share issuance, normally within 90 days.
0. **Step 4** — Investor claims the credit on the personal T1 (line 47900 / Form NB428 Part C) or corporate T2 (Schedule 305 NB), attaching NB-SBITC-1.
0. **Step 5** — Unused individual credit is refunded; unused corporate credit carries forward 7 years / back 3 years.

### Connected-investor exclusion

- **Connected-investor exclusion** — A claim is denied if the investor (alone or with non-arm's length persons) controls more than 10% of any class of issued shares of the EBC, or is a "specified shareholder" within meaning of the Income Tax Act (Canada). Founders investing in their own company are not eligible — the credit is designed for arm's length angel investors.  _(Section 6)_

### Stacking with federal credits

Stacks freely with federal Lifetime Capital Gains Exemption on later disposition (subject to QSBC rules and the OBBBA-era adjustments — out of scope here; refer to a federal skill). Stacks with flow-through share treatment only if the issuer is also a Principal Business Corporation in mining/oil & gas (rare for SBITC issuers).

## 7. NB Film Tax Credit

### Mechanics

- **Type** — Refundable corporate credit.  _(Section 7)_
- **Base rate (2025)** — 25% percent (of eligible NB-resident labour (base rate))  _(Section 7)_
- **Rural bonus rate (2025)** — +5% percent (for productions outside the Greater Moncton, Fredericton, and Saint John regions (rural NB filming), bringing the rate to 30%)  _(Section 7)_
- **Cap** — 50% of total production costs  _(Section 7)_

### Eligibility

- **Eligibility conditions** — Corporation with a permanent establishment in NB. Production has received a Part A certificate from NB Film (Department of Tourism, Heritage and Culture) before principal photography. Production is a film, television, or interactive digital media project (excluding news, sports, advertising, pornography, and certain reality programming). Eligible labour = salaries and wages paid to NB residents who worked on the production in NB.  _(Section 7)_

### Workflow

0. **Step 1** — Pre-production: Part A application to NB Film.
0. **Step 2** — Post-production: Part B certificate of completion from NB Film with audited labour schedule.
0. **Step 3** — Claim on T2 Schedule 305 (NB), attaching Part B certificate.

### Interaction

- **Interaction with federal credits** — Stacks with the federal Canadian Film or Video Production Tax Credit (CPTC) or Film or Video Production Services Tax Credit (PSTC) — but only one of the two federal credits, never both, and the NB credit is computed on a labour base reduced by federal assistance per the grind-down rule.  _(Section 7)_

## 8. Form NB428 and credit-specific schedules

**Form / line reference table**  _(Section 8)_

| Credit | Form / line |
| --- | --- |
| Non-refundable personal credits (basic, age, spouse, CCB-equivalent, etc.) | Form NB428 Part A |
| NB Tuition Amount | Schedule NB(S11) → NB428 line 58560 |
| NB Tax on split income | Form T1206 + NB428 line 42800 |
| NB Low-Income Tax Reduction | NB428 Part C, lines 47600–47700 |
| NB Seniors' Home Renovation Credit | Schedule NB(S12) → NB428 line 47900 |
| NB SBITC (individual) | NB-SBITC-1 attached; NB428 line 47900 schedule |
| NBHSTC | No form — auto-calculated by CRA from T1 |
| NB Film Tax Credit | T2 Schedule 305 (NB) with Part B certificate |
| NB R&D Tax Credit | T2 Schedule 360 |

## 9. Worked example — Moncton angel investor

Ava is a Moncton resident, NB resident on 31 Dec 2025, with employment income of $185,000 (federal + NB tax already provided for via payroll). On 15 March 2025 she subscribes for $200,000 of newly issued common shares in TideTech Inc., an NB-registered EBC with 18 employees building agritech sensors in Dieppe. TideTech holds a current SBITC registration certificate. Ava is unrelated to all TideTech founders and owns 4.2% of post-money common shares (below the 10% connected-investor threshold). TideTech issues Ava Form NB-SBITC-1 in June 2025 certifying $200,000 of eligible investment.

### Credit computation.

Eligible investment: $200,000 (under the $250,000 individual cap). Rate: 50%. NB SBITC: $200,000 × 50% = $100,000. Refundability: Refundable for individuals. Even though Ava's NB tax liability is roughly $14,800 for 2025, the full $100,000 is paid: $14,800 reduces NB tax to zero, and the remaining $85,200 is refunded when she files her 2025 T1.

### Reporting.

Attach NB-SBITC-1 to her 2025 T1. Enter on NB428 Part C, line 47900 schedule for refundable provincial credits. Hold period: Ava must hold the TideTech shares until at least 15 March 2029. If she disposes before then to a non-arm's length party or TideTech redeems, the full $100,000 is clawed back via reassessment.

### Other NB credits this year.

LITR: phased out at her income level — zero. NBHSTC: phased out at her income level — zero. Seniors' Home Renovation: not eligible (Ava is 41).

### Net NB filing impact.

Refundable credit of $85,200 after offsetting NB tax.

## 10. Conservative defaults

- **Default 1** — Always require the NB-SBITC-1 certificate before quoting an SBITC credit. Do not estimate from share-subscription documents alone — the certificate is the operative document, and NB Finance routinely denies issuance where end-use covenants are missing.  _(Section 10)_
- **Default 2** — Treat the 4-year hold period as binding for engagement-letter purposes. Flag in the cover letter that disposition before March 2029 (in the example) triggers full clawback.  _(Section 10)_
- **Default 3** — For the Seniors' Home Renovation Credit, default to the most restrictive interpretation of "principal-purpose accessibility" when an expense could be characterised as routine renovation. CRA and NB Finance both deny mixed-purpose claims absent contemporaneous documentation linking the expense to the senior's mobility or safety needs.  _(Section 10)_
- **Default 4** — For LITR, model both spousal claim positions and use the one producing the lower combined NB tax.  _(Section 10)_
- **Default 5** — For NBHSTC, never assume eligibility without confirming province of residence on the first day of the payment month — moves out of NB during the benefit year unwind the credit.  _(Section 10)_
- **Default 6** — For NB Film Tax Credit, require both Part A and Part B certificates on file before posting the receivable. Verbal commitments from NB Film are insufficient.  _(Section 10)_
- **Default 7** — Do not stack the NB SBITC against any other equity-based provincial investor credit on the same shares (no double-dipping across provinces for inter-provincial investors).  _(Section 10)_
- **Default 8** — Refer out any cross-border investor scenario (US individual investing in NB EBC) — Canada–US treaty interaction with refundable credits is fact-specific.  _(Section 10)_

## 11. Sources

- New Brunswick Income Tax Act, SNB 2000, c N-6.001 — provincial tax computation and credits framework.
- Small Business Investor Tax Credit Act, SNB 2003, c S-9.05, and New Brunswick Regulation 2003-39 — SBITC statutory and regulatory basis.
- New Brunswick Department of Finance and Treasury Board — Small Business Investor Tax Credit Program Guide (2025 edition).
- New Brunswick Department of Finance and Treasury Board — Seniors' Home Renovation Tax Credit Guide.
- Canada Revenue Agency — Form NB428 — New Brunswick Tax and Credits (2025) and Schedule NB(S11), Schedule NB(S12).
- Canada Revenue Agency — New Brunswick Harmonized Sales Tax Credit program page.
- Opportunities NB — NB Film Tax Credit program guide (2025).
- Income Tax Act (Canada), RSC 1985, c 1 (5th Supp), s. 120.4 (tax on split income) and Part XVII — coordination with federal computation.
- Federal–Provincial Tax Collection Agreement (NB schedule) — administration of personal NB credits via CRA.

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
