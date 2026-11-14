---
name: la-income-tax
description: "Louisiana 2026 resident wage and sole-proprietor income tax: federal AGI modifications, flat 3%, final indexed deductions, retirement exemption, IT-540 and estimates. Load us-tax-workflow-base first."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/la-income-tax"
  jurisdiction: "US-LA"
  tax_year: "2026"
  last_updated: "2026-11-13"
---

# Louisiana individual income tax, 2026

> **Built from the law. Not yet approved.** Written by Codex; this version has not been reviewed by an accountant. General reference only. Under Circular 230 section 10.37, apply the cited authorities to the actual facts and obtain qualified professional review before filing or acting.

**Answer first:** Louisiana taxes resident wages and business income at 3% of state taxable income. The final 2026 standard deduction is $12,838 for single/MFS and $25,676 for MFJ/HOH/qualifying surviving spouse. These final return deductions differ from the payroll withholding amounts. [R.S.47:32](https://www.legis.la.gov/legis/Law.aspx?d=101946); [RIB26-019](https://dam.ldr.la.gov/lawspolicies/RIB%2026-019.pdf).

## Scope

Full-year Louisiana residents with wages, sole-proprietor or disregarded single-member LLC income, rents, gains, interest or retirement income. Use IT-540; nonresident and part-year choice/IT-540B, complex K-1 adjustments and incentive-credit work require separate review. Corporate and payroll owners are `la-corporate-tax` and `la-payroll`. Federal inputs belong to `us-schedule-c-and-se-computation`, `us-self-employed-health-insurance`, `us-self-employed-retirement`, `us-schedule-c-and-se-computation` and `us-qbi-deduction`; load those rather than restating federal amounts.

## Ask the client first

1. Full-year domicile, move dates, other-state workdays and returns; is a resident return appropriate?
2. Federal filing status, completed federal AGI and income by wages, Schedule C, rents, K-1, gains, interest and retirement; ages and plan names?
3. Other-state municipal bonds and acquisition dates, U.S. obligations, Social Security and state-exempt retirement amounts already included in AGI?
4. Federal itemization and medical deduction, state depreciation elections/schedules, active-duty orders and days outside Louisiana, other state adjustments and credit evidence?
5. Withholding, estimated payments, prior-year tax, other-state income taxes and any extension or IRS adjustment?

## The method, step by step

1. **Select the period and taxpayer.** Use the same filing status as federal. Start from federal AGI rather than federal taxable income. The completed federal Schedule C and above-the-line insurance/retirement deductions are already reflected there; do not deduct them twice. QBI is below AGI and does not itself reduce this starting point. [R.S.47:293(1),(9)](https://www.legis.la.gov/legis/Law.aspx?d=101760); [R.S.47:294](https://legis.la.gov/Legis/Law.aspx?d=101761).
2. **Reconcile additions and subtractions.** Add other-state bond interest when required: the statutory rule distinguishes obligations acquired on/after January 1, 1980. Subtract only exempt income included in federal AGI. Federal income tax paid is **not deductible**: the former provisions were repealed in 2022. Check specific Louisiana conformity and separate depreciation adjustments before accepting federal amounts unchanged. [R.S.47:293(9)](https://www.legis.la.gov/legis/Law.aspx?d=101760). Ordinary wages, Schedule C profit, rents, gains, interest and dividends remain in the base unless an identified exclusion applies; there is no separate lower capital-gain rate.
3. **Apply the exemptions with evidence.** Social Security and qualifying federal/railroad retirement are exempt under [R.S.47:44.2](https://legis.la.gov/legis/Law.aspx?d=102134). The opened 2025-2026 filing cycle booklet identifies U.S. obligation interest and separately exempt state-system pensions; retain the issuer/plan evidence and confirm the final 2026 adjustment code rather than subtracting all pensions. For otherwise taxable annual pension/annuity income of each recipient age 65+, the 2026 exemption is capped at $12,324. Do not exempt the same income twice. [R.S.47:44.1](https://www.legis.la.gov/legis/Law.aspx?d=102133); [RIB26-019](https://dam.ldr.la.gov/lawspolicies/RIB%2026-019.pdf); [2025 instructions, Schedule E](https://dam.ldr.la.gov/taxforms/IT540i%20WEB%282025%29D11.pdf).
4. **Subtract the final deduction and allowable excess medical expenses.** Use the current amounts below. Prior additional age/blind/dependent exemptions were repealed. General federal itemized deductions do not replace the state deduction; R.S.47:293 allows the qualifying excess of federally deductible itemized medical expenses over the applicable federal standard deduction, subject to federal limits. The old skill's general itemize-versus-standard comparison was too broad. [R.S.47:293(3),(9)(a)(xi)](https://www.legis.la.gov/legis/Law.aspx?d=101760); [RIB25-012](https://dam.ldr.la.gov/lawspolicies/RIB-25-012-Louisiana-Individual-Income-Tax-Reform-1.pdf).
5. **Compute and reconcile.** Taxable income = max(0, AGI + additions - exempt income - state standard deduction - qualifying excess medical deduction). Gross tax = taxable income x 0.03. Apply separately substantiated credits in their statutory order, then withholding and estimates. Other-state credit eligibility/limits are in [R.S.47:33](https://legis.la.gov/legis/Law.aspx?d=102000); collect the other return and tax proof before computing. Never treat payroll withholding as the final liability.

### Rates, bands and thresholds

| 2026 item | Amount or rule | Authority |
| --- | --- | --- |
| Individual rate | 3% | [R.S.47:32](https://www.legis.la.gov/legis/Law.aspx?d=101946) |
| Standard deduction single/MFS | $12,838 | [RIB26-019](https://dam.ldr.la.gov/lawspolicies/RIB%2026-019.pdf) |
| Standard deduction MFJ/HOH/qualifying surviving spouse | $25,676 | [RIB26-019](https://dam.ldr.la.gov/lawspolicies/RIB%2026-019.pdf) |
| Age-65 annual retirement exemption | Up to $12,324 per eligible recipient, limited to qualifying income | [RIB26-019](https://dam.ldr.la.gov/lawspolicies/RIB%2026-019.pdf); [R.S.47:44.1](https://www.legis.la.gov/legis/Law.aspx?d=102133) |
| Individual estimates trigger | Expected tax after credits/withholding exceeds $1,000; joint declaration exceeds $2,000 | [IT-540ESi2026 p.1](https://dam.ldr.la.gov/taxforms/IT540ESi-2026.pdf) |

### Boundary table

| Fact | Treatment or stopping point |
| --- | --- |
| Military wages | The resident active-duty exclusion concerns at least 120 consecutive full-time days and compensation earned outside Louisiana, capped at $50,000; do not exempt all military wages. [R.S.47:293(9)(e)](https://www.legis.la.gov/legis/Law.aspx?d=101760). |
| State bonus depreciation | RIB25-012 describes Louisiana full-expensing elections and later federal-depreciation addbacks. Reconcile state asset basis and no duplicate deduction; fixed-date definitions and final 2026 federal conformity require specialist review. [RIB25-012 pp.2-3](https://dam.ldr.la.gov/lawspolicies/RIB-25-012-Louisiana-Individual-Income-Tax-Reform-1.pdf). |
| Federal home office, insurance and retirement contributions | Bring the completed federal result through AGI and test Louisiana modifications; federal computation remains with the named owner skills. |
| K-1, PTE election, purchased or industry credits | Reconcile entity-level exclusions/owner schedules; do not simply deduct the state tax as federal income tax. Refer the election, historic rehabilitation, motion-picture and enterprise-zone credit computations. |
| Nonresident or part-year | Stop this resident computation; the opened 2025-2026 booklet uses IT-540B for nonresidents and allows part-year resident/nonresident-return comparison. Final 2026 form choice/lines must be confirmed. [2025 instructions p.2](https://dam.ldr.la.gov/taxforms/IT540i%20WEB%282025%29D11.pdf). |
| Prior tax year | The 2025-2026 filing cycle has $12,500/$25,000 standard deductions and $12,000 retirement exemption; do not use those amounts on a 2026 estimate or final return. [RIB26-019 comparison table](https://dam.ldr.la.gov/lawspolicies/RIB%2026-019.pdf). |

## Worked cases

### Wage earner: final deduction and withholding are different inputs

A single full-year resident has $60,000 federal AGI consisting only of wages, no adjustments or credits, and $1,500 Louisiana withholding. 2026 taxable income is $47,162; gross tax is $1,414.86 before whole-dollar return rounding, leaving $85.14 overpayment in this illustration. The deduction is the final indexed $12,838, not the payroll-table deduction.

```oa-check
name: LA resident wage tax 2026
inputs:
  agi: 60000
  withholding: 1500
steps:
  - taxable: max(0, agi - 12838)
  - gross_tax: taxable * 0.03
  - overpayment: withholding - gross_tax
expected:
  taxable: 47162
  gross_tax: 1414.86
  overpayment: 85.14
```

### Retirement exemption belongs to the eligible recipient

A single resident age 67 has $50,000 federal AGI, including $10,000 federally taxable Social Security and $20,000 otherwise taxable qualifying pension income. No separately exempt pension, other adjustment or credit applies. Exclude $10,000 and $12,324, then subtract $12,838; taxable income is $14,838 and tax $445.14 before return rounding. A younger recipient cannot use the age-65 exemption merely because a spouse qualifies.

```oa-check
name: LA age 65 retirement limit 2026
inputs:
  agi: 50000
  social_security: 10000
  pension: 20000
steps:
  - exempt_pension: min(pension, 12324)
  - taxable: max(0, agi - social_security - exempt_pension - 12838)
  - tax: taxable * 0.03
expected:
  exempt_pension: 12324
  taxable: 14838
  tax: 445.14
```

## When to refuse or refer

Refer disputed domicile, IT-540B sourcing, K-1/PTE adjustments, entity credits, state/federal asset-basis differences or recent federal-law conformity that has not been researched. Do not invent a federal-tax-paid deduction, final return line number or inflation amount. The published 2026 indexed values above resolve the former inflation gap; other Sources gaps remain filing gates.

## Filing and payment

The recurring due-date rule is the fifteenth day of the fifth month, moved to the next business day when necessary. May 15, 2027 is Saturday; the ordinary weekend adjustment gives May 17, 2027 for a calendar 2026 return, subject to any subsequently announced relief. The opened **2025-2026 filing cycle** instructions allow an automatic six-month filing extension without extending payment. Use LaTAP, retain acknowledgment and apply final 2026 instructions before filing. [IT-540 instructions pp.1-4](https://dam.ldr.la.gov/taxforms/IT540i%20WEB%282025%29D11.pdf).

For 2026 estimates use IT-540ES or LaTAP; regular installments are April 15, June 15, September 15, 2026 and January 15, 2027. Recompute on changed facts. Special farm/fishing and final-return payment alternatives have separate conditions in IT-540ESi; do not use them to erase earlier underpayments. Its preliminary deduction worksheet does not supersede September's final RIB26-019 amounts. [2026 estimate instructions](https://dam.ldr.la.gov/taxforms/IT540ESi-2026.pdf).

### 2025-2026 filing cycle form map retained for migration

The opened 2025 IT-540 booklet maps line 7 to AGI or Schedule E adjusted AGI, line 8 to the state deduction, 9A-9D to the excess medical calculation, 10 to taxable income and 11 to 3% tax. Line 12 is nonrefundable priority-1 credit; withholding/estimates and refundable priorities reconcile through later lines. The old blanket descriptions of lines 9, 12-19, 20-25 and line 30 were unreliable. **Final 2026 line numbers are not confirmed.** [IT-540 instructions pp.2-4](https://dam.ldr.la.gov/taxforms/IT540i%20WEB%282025%29D11.pdf).

## Completion checklist

Confirm resident status and federal owners, reconcile AGI and each adjustment, apply final 2026 amounts by recipient/status, attach credit and state-basis support, reconcile payments, and obtain review of every unresolved filing issue. Save the official source and computation with the return.

## Sources

| Source and reading scope | URL | Read on |
| --- | --- | --- |
| R.S.47:32; read for complete individual rate, repeal and corporate cross-reference. | https://www.legis.la.gov/legis/Law.aspx?d=101946 | 2026-11-13 |
| R.S.47:293; read for definitions and complete resident net-income modifications, repeal neighbours, military and nonresident boundaries. | https://www.legis.la.gov/legis/Law.aspx?d=101760 | 2026-11-13 |
| R.S.47:294; read for all status groups and annual indexing. | https://legis.la.gov/Legis/Law.aspx?d=101761 | 2026-11-13 |
| RIB26-019; read for entire final 2026 index table, comparison year and footnote. | https://dam.ldr.la.gov/lawspolicies/RIB%2026-019.pdf | 2026-11-13 |
| R.S.47:44.1; read for retirement age/base/indexing and separate disability neighbour. | https://www.legis.la.gov/legis/Law.aspx?d=102133 | 2026-11-13 |
| R.S.47:44.2; read for entire exemption provision. | https://legis.la.gov/legis/Law.aspx?d=102134 | 2026-11-13 |
| R.S.47:33; read for other-state-credit conditions and limits. | https://legis.la.gov/legis/Law.aspx?d=102000 | 2026-11-13 |
| RIB25-012; read for all nine pages, reform, repeal, state bonus election and withholding distinction. | https://dam.ldr.la.gov/lawspolicies/RIB-25-012-Louisiana-Individual-Income-Tax-Reform-1.pdf | 2026-11-13 |
| 2025 IT-540 instructions; read for resident filing, p.2-4 return map, Schedule E exemptions and other-state-credit instructions; 2025-2026 filing cycle. | https://dam.ldr.la.gov/taxforms/IT540i%20WEB%282025%29D11.pdf | 2026-11-13 |
| IT-540ESi2026; read for complete instructions, thresholds, special cases and worksheet. | https://dam.ldr.la.gov/taxforms/IT540ESi-2026.pdf | 2026-11-13 |

Not yet confirmed: final 2026 IT-540/IT-540B line numbers and adjustment codes, final 2026 conformity to later federal changes, credit-specific eligibility and depreciation election computations. The 2025-2026 filing cycle procedures are retained as dated evidence, not extrapolated forms. Legacy 2024 graduated rates, prior $4,500/$9,000 deductions and the former additional $1,000 exemptions are historical topics only and not supplied as current rules. Exact 2026 extended filing date and disaster relief were not confirmed.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `la-income-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/la-income-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
