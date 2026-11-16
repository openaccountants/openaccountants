---
name: thailand-pit
description: "Thailand individual income tax for 2026: ordinary progressive computation, salary expense and supported allowances, family and retirement conditions, filing thresholds by income category, historical/current salary cases and foreign-remittance tracing."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/thailand-pit"
  jurisdiction: "TH"
  tax_year: "2026"
  last_updated: "2026-11-16"
---

# Thailand personal income tax v1.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

**2026 answer layer:** work out ordinary Thai individual income tax from identified assessable income, supported expenses/allowances and credits. Do not use a bank transfer alone as the tax base. Load `workflow-base`; return a working paper and questions for review, not a filed return. Tax year 2026 is BE 2569: the calendar conversion is CE + 543 (derived). The annual 2026 PND.90/91 forms were not listed on the opened 2026 index; the opened annual forms are explicitly the 2025-2026 filing cycle.

**Contributor: Open Accountants Community.** Historical software source credit is retained: `ratanon97/ThaiTaxCalculator` (`TH-2567.json`) and `anurat/laravel-thai-tax` (previously described as MIT). These are discovery/provenance credits, not primary tax sources; see [references](references.md).

Determine Thai-source employment/business/property income and domestic residence before bringing foreign income into the computation. Revenue Code §41 uses at least 180 aggregate days. Section 40 distinguishes employment, hire of services, rights, investment, rent, liberal professions, contracts with essential materials and other business. A generic freelance keyword does not prove the liberal-profession category. [Revenue Code §§39-41](https://www.rd.go.th/5937.html).

## Rates, bands and thresholds

| Item | Amount and conditions | Period | Official source |
|---|---|---|---|
| First net-income slice | Exempt up to THB 150,000 under the ordinary progressive method; not a filing threshold | 2026 | [Decree 470 and Act 44, as identified in the official reform table](https://www.rd.go.th/59668.html) |
| Next marginal slice | 5% on net income over THB 150,000 to THB 300,000; lower boundary is derived from the separately cited first-slice exemption | 2026 | [Income Tax Schedule (1), read with the first-slice exemption above](https://www.rd.go.th/5938.html) |
| Next marginal slice | 10% over THB 300,000 to THB 500,000 | 2026 | [Income Tax Schedule (1)](https://www.rd.go.th/5938.html) |
| Next marginal slice | 15% over THB 500,000 to THB 750,000 | 2026 | [Income Tax Schedule (1)](https://www.rd.go.th/5938.html) |
| Next marginal slice | 20% over THB 750,000 to THB 1,000,000 | 2026 | [Income Tax Schedule (1)](https://www.rd.go.th/5938.html) |
| Next marginal slice | 25% over THB 1,000,000 to THB 2,000,000 | 2026 | [Income Tax Schedule (1)](https://www.rd.go.th/5938.html) |
| Next marginal slice | 30% over THB 2,000,000 to THB 5,000,000 | 2026 | [Income Tax Schedule (1)](https://www.rd.go.th/5938.html) |
| Top marginal slice | 35% over THB 5,000,000 | 2026 | [Income Tax Schedule (1)](https://www.rd.go.th/5938.html) |
| Employment/hire-of-service expense | 50% of qualifying §40(1) and (2) income combined, maximum THB 100,000; do not grant a separate cap to each category | 2026 | [Revenue Code §42 bis](https://www.rd.go.th/5937.html) |
| Personal allowance | THB 60,000 for the ordinary individual; spouse treatment depends on filing and income status | 2026 | [Revenue Code §47(1)(a)-(b)](https://www.rd.go.th/5937.html) |
| Salary-only filing threshold | Single: income exceeds THB 120,000; married: combined relevant income exceeds THB 220,000 | 2026 | [Revenue Code §56](https://www.rd.go.th/5937.html) |
| Other-income filing threshold | Single: income exceeds THB 60,000; married: combined relevant income exceeds THB 120,000; do not apply salary-only thresholds universally | 2026 | [Revenue Code §56](https://www.rd.go.th/5937.html) |

## The base

### Income and expenses in order

Identify assessable receipts under §40 and separately substantiate exemptions. Employment includes salary, bonus and taxable benefits; commissions can fall under §40(2), rents under §40(5), qualifying liberal professions under §40(6), and e-commerce/business receipts under §40(8). Classify a freelancer by the actual work, capital, materials and professional category, not their job label. The employment expense percentage is not a universal business deduction. Establish the legally available actual or standard expenses for other categories before computing them; those category-specific schedules are outside this ordinary salary example, not replaced with zero evidence.

Separate exempt retirement contributions from post-expense allowances without claiming either twice. Apply allowable expenses, then personal and supported allowances, then donations in their proper order. Ordinary net taxable income cannot be made negative by an allowance. Apply the marginal bands; compare the alternate gross-income method where §48(2) applies, then supported tax credits and withholding. The alternate method is not an extra percentage charged on top of progressive tax and does not apply to employment-only income. [Revenue Code §§42 bis-48 and 60](https://www.rd.go.th/5937.html). For assessable non-§40(1) income totalling at least THB 120,000, compute 0.5% of the relevant gross assessable income and compare with the ordinary net-income liability. The [RD method-2 guidance](https://www.rd.go.th/26218.html) states that where method-2 tax does not exceed THB 5,000, pay under method 1; otherwise pay the larger result. For example, hypothetical non-employment assessable income of THB 800,000 gives method-2 tax THB 4,000, so it does not create a minimum liability above method 1. At THB 1,200,000 it gives THB 6,000: if the properly computed ordinary liability is THB 4,000, THB 6,000 prevails. Establish category-specific expenses, special final-tax elections and excluded income before using this comparison; the examples do not assume a universal business expense rate.

```oa-check
name: Thailand alternate method threshold and comparison
inputs:
  low_gross: 800000
  higher_gross: 1200000
  ordinary_higher: 4000
steps:
  - low_method2: low_gross * 0.005
  - higher_method2: higher_gross * 0.005
  - higher_payable: max(higher_method2, ordinary_higher)
expected:
  low_method2: 4000
  higher_method2: 6000
  higher_payable: 6000
```

### Family allowances and proof

| Item | Amount and conditions | Period | Official source |
|---|---|---|---|
| Spouse | THB 60,000 where the spouse has no income or the applicable joint computation permits it; no duplicate allowance on separate returns | 2026 | [§47(1)(b), (2) and (3)](https://www.rd.go.th/5937.html) |
| Child | THB 30,000 per qualifying child; second/later lawful child born in/after 2018 has an additional THB 30,000, giving THB 60,000 derived | 2026 | [§47(1)(c); Act 46](https://www.rd.go.th/5937.html) |
| Parent care | THB 30,000 per qualifying parent aged at least 60; qualifying support, lawful-child relationship, income condition and one claimant per parent are required | 2026 | [Notification 136 clauses 1-3; §47(1)(j)](https://www.rd.go.th/23368.html) |
| Disabled/incompetent-person support | THB 60,000 per statutorily qualifying supported person (in words on the page); status, relationship/caregiver evidence and Director-General conditions are required | 2026 | [§47(1)(k)](https://www.rd.go.th/5937.html) |

For child relief, check lawful/adopted status and birth order, including deceased lawful children for the additional-child ordering rule. An adopted child does not receive the additional lawful-child relief; adopted-child numbers interact with the lawful-child count and the combined statutory limit. The child must be a minor, a qualifying student not older than 25, or an eligible court-declared incapable/quasi-incapable dependent, and cannot have non-exempt assessable income of THB 30,000 or more. Non-residents have the statutory Thai-resident spouse/child limitation. These conditions come from [§47(1)(c) and (3)](https://www.rd.go.th/5937.html).

Parent relief is not automatically the former 'maximum 4 parents'. Examine each taxpayer's and spouse's parents, filing status and support certification; siblings cannot duplicate the claim. Notification 136 states the income boundary and requires the parent's identification and support evidence; do not apply the old strict 'income below THB 30,000' shorthand without the actual qualification. Disabled-person support likewise requires proof of qualifying status and support; no automatic deduction follows from a narrative description alone. Particular subsidiary disability/caregiver conditions still not read are listed below and block an automatic claim.

### Retirement, insurance and other allowances

| Item | Amount and conditions | Period | Official source |
|---|---|---|---|
| Provident fund (PVD) | Supported actual contributions within the 15% wage condition, combining the allowance slice and exempt excess; the excess exemption is capped at THB 490,000 above the THB 10,000 allowance slice (amounts in words on the page) | 2026 | [§47(1)(g) and MR126 clause 2(35)](https://www.rd.go.th/2502.html) |
| Government Pension Fund | Actual qualifying contributions under its law, within THB 500,000 and the shared retirement cap; the old generic 15% salary limit is not established by this provision | 2026 | [MR126 clause 2(43), (55) and (61) (amount in words on the page)](https://www.rd.go.th/2502.html) |
| Retirement Mutual Fund (RMF) | 30% of assessable income, maximum THB 500,000; also the shared retirement cap; hold at least 5 years from first purchase and redeem at age at least 55, subject to prescribed conditions and recapture | 2026 | [MR126 clause 2(55) (figures in words on the page)](https://www.rd.go.th/2502.html) |
| Pension life insurance | Additional qualifying relief up to 15% of assessable income and THB 200,000, also within the THB 500,000 shared retirement limit; policy and Director-General conditions apply | 2026 | [MR126 clause 2(61) (figures in words on the page)](https://www.rd.go.th/2502.html) |
| Own life insurance | Base allowance plus additional exemption totals at most THB 100,000 derived; domestic insurer, qualifying policy of at least 10 years and prescribed conditions | 2026 | [§47(1)(d) and MR126 clause 2(61) (amounts in words on the page)](https://www.rd.go.th/2502.html) |
| Non-earning spouse life insurance | At most THB 10,000, qualifying policy and marriage throughout the year; do not grant the own-policy additional exemption to the spouse by analogy | 2026 | [§47(1)(d)](https://www.rd.go.th/5937.html) |
| Own health insurance | Actual qualifying premium up to THB 25,000; together with the relevant life-insurance relief at most THB 100,000 | 2026 | [MR126 clause 2(97) (amounts in words on the page)](https://www.rd.go.th/2502.html) |
| Parent health insurance | Actual eligible premium up to THB 15,000, subject to parent/support/income and prescribed conditions; not an automatic per-parent allowance | 2026 | [MR126 clause 2(76) (amount in words on the page)](https://www.rd.go.th/2502.html) |
| Social security | Actual legally paid employee contribution under the social-security law, not the old universal THB 9,000 annual cap; current contribution computation is in payroll | 2026 | [§47(1)(i)](https://www.rd.go.th/5937.html) |
| Home-loan interest | Actual qualifying mortgage interest up to THB 100,000 derived from the base THB 10,000 allowance and additional THB 90,000 exemption; eligible lender, residence/mortgage and evidence rules apply | 2026 | [§47(1)(h) and MR126 clause 2(53) (amounts in words on the page)](https://www.rd.go.th/2502.html) |
| Ordinary donations | Actual qualifying donation, at most 10% of the balance after expenses and preceding allowances; any special enhanced deduction must be tested first | 2026 | [§47(7)](https://www.rd.go.th/5937.html) |
| Political-party donations | Actual qualifying support, up to THB 10,000 (in words on the page); prescribed party/fundraising conditions apply | 2026 | [§47(1)(l)](https://www.rd.go.th/5937.html) |

Keep a single retirement-cap worksheet: PVD, Government Pension Fund, private-teacher fund, RMF, qualifying pension insurance and National Savings Fund must be cross-checked under the applicable shared-cap provisions. The National Savings Fund topic is retained: MR126 clause 2(90) grants relief for actual statutory contributions and links the shared cap, but its separate current member-contribution ceiling is not established by that tax provision. Do not turn the tax ceiling into permission to contribute that amount. The former THB 30,000 National Savings Fund headline remains unconfirmed here.

SSF is not a standing 2026 purchase deduction. [MR126 clause 2(102)](https://www.rd.go.th/2502.html) confines the ordinary historical purchase window to the stated 2020-2024 period, at 30% of assessable income/THB 200,000 within the shared cap, with a 10-year holding condition and exceptions for disability or death (figures in words on the page). Retain old holdings for compliance/recapture review; do not claim a new 2026 purchase under the expired window.

Enhanced education/sport/social donations are a separate eligibility question, not every gift multiplied automatically. The opened [2025-2026-cycle PND.91 calculation page](https://www.rd.go.th/fileadmin/download/english_form/2025/PIT91_2568_eng_310368_02.pdf) places qualifying enhanced donations before ordinary donations, each with its own base. Check the effective decree, eligible recipient, payment/e-Donation evidence and period before allowing enhancement; do not cap both against the same unreduced balance. The temporary Easy E-Receipt topic also remains: the opened [2025 allowance attachment](https://www.rd.go.th/fileadmin/download/english_form/2025/Allowance2568_eng_310368_02.pdf) names a dated 2025 purchase window. It does not establish a 2026 THB 50,000 shopping deduction.

### Bank-statement classification and defaults

| Original pattern | Evidence-led classification and return route |
|---|---|
| เงินเดือน / Salary / Payroll; โบนัส / Bonus | Employment §40(1); reconcile employer withholding certificate and benefits; salary-only PND.91 if otherwise eligible |
| ค่าเช่า / Rent received | Rental §40(5), normally PND.90; obtain lease and expense evidence, consider half-year filing |
| เงินปันผล / Dividend | Investment §40(4); final-withholding election/gross-up depends on the actual distribution and residence, not the keyword |
| ดอกเบี้ย / Interest income | Investment §40(4); identify exempt/final-tax treatment and certificates before inclusion or election |
| ค่านายหน้า / Commission | Investigate §40(2) service income and the actual contract; broader PND.90 route |
| ขายของออนไลน์ / E-commerce | Business §40(8); reconcile gross sales, platform fees, refunds and expenses; PND.90/possible PND.94 |
| ฟรีแลนซ์ / Freelance | Determine §40(2), (6), (7) or (8) from actual facts; never automatically label every freelancer a liberal professional |

These are practical triage patterns, not merchant-specific legal rulings or verified bank export specifications. With unclear deduction eligibility or missing donation proof, leave the claim pending and ask for the evidence. With ambiguous income, identify the facts before final classification; a provisional reserve is not a filing position. With foreign receipts, trace the funds under the next section; do not apply the former same-year-only default.

## Deadlines and filing

Filing can be required even if progressive tax is zero; use the separate salary-only and other-income thresholds above. PND.91 is for employment-only §40(1); PND.90 handles the broader income mix. Section 56's statutory deadline is the last day of March after the tax year, with payment under §57 quater. Section 56 bis requires applicable §40(5)-(8) January-June income to be reported during September on PND.94, excluding its stated key-money/construction-contribution/property-transfer category; half-year allowances follow its half-allowance rule and the payment is credited to the annual tax.

Collect employer 50 bis certificates, deduction/insurance/PVD statements, donation evidence, other-income records, bank tracing and prior payments. Follow the [official e-Filing route](https://www.rd.go.th/rdeservice/63813.html): select taxpayer, year, PND.90/91/94 and original/amended status; classify income; enter exempt income, allowable expenses and supported allowances; calculate progressive/alternate liability; enter eligible foreign tax credit, withholding and advances; review, submit, pay any balance using the generated reference and retain the acknowledgement/receipt. The opened [2025-2026 filing-cycle PND.91](https://www.rd.go.th/fileadmin/download/english_form/2025/PIT91_2568_eng_310368_02.pdf) labels these as computation A1-A22, with exempt-income subsection B and the allowance attachment. Do not reuse those box numbers as a claim to have read final 2026 annual forms. An overpayment requires the refund election and supporting evidence; the form describes the available refund route.

The former automatic 8 April electronic deadline is not assumed for a 2026 return due in the following year. Check the actual calendar and qualifying electronic-extension notice. No signed-in filing was tested for this rewrite.

## Penalties and interest

Do not infer a nil penalty from nil tax. Late filing, late payment and understatement are separate tests; the current general assessment, fine and remission provisions were not fully read here. Prepare the dates, assessed tax, payments and notice for a qualified reviewer rather than inventing a universal charge.

## Cross-border points

Thai-source income remains in scope even if paid outside Thailand. For foreign-source income, [the RD foreign-income guide, printed pages 3-4](https://www.rd.go.th/fileadmin/user_upload/porphor/GuideTaxFromAbroad_TH.pdf) tests residence in the year the income arose and taxation in the year it is brought into Thailand. [Order P.162/2566](https://www.rd.go.th/fileadmin/user_upload/kormor/newlaw/dn162A.pdf) excludes income arising before 1 January 2024 from the new P.161 interpretation. Reconstruct mixed accounts, principal, old savings, income, dates and applicable exemptions; do not tax the entire inward transfer by default or exempt a later remittance solely because it was earned in a different year. Treaty residence, pensions, foreign tax credits and any later legislative exemption require their own current instrument and limitation calculation.

## Two worked examples that recompute

### Original salary case retained as a historical actual-payment fixture

The original 2024 case has annual salary THB 1,200,000, single/no children, PVD 10% (THB 120,000), actual social-security payments THB 9,000 and life premium THB 50,000. Assume all policy and fund conditions were met. Expense deduction THB 100,000 and personal allowance THB 60,000 give taxable income THB 861,000. Slice tax is THB 7,500 + 20,000 + 37,500 + 22,200 = THB 87,200. Withholding THB 95,000 gives THB 7,800 refund. This preserves the original inputs/result; THB 9,000 is an actual historical input, not the current annual maximum.

```oa-check
name: Thailand original salary case historical actual contributions
inputs:
  salary: 1200000
  pvd: 120000
  social_actual: 9000
  life: 50000
  withheld: 95000
steps:
  - expense: min(salary * 0.50, 100000)
  - net: salary - expense - 60000 - pvd - social_actual - life
  - tax: 7500 + 20000 + 37500 + (net - 750000) * 0.20
  - refund: withheld - tax
expected:
  expense: 100000
  net: 861000
  tax: 87200
  refund: 7800
```

### Current salary and PVD decision

Use the same salary, family and life-premium facts for 2026, but assume actual employee social payments THB 10,500, derived from 12 full ordinary months at the current payroll ceiling, with no temporary rate reduction. With PVD THB 120,000, taxable income is THB 859,500, tax THB 86,900 and refund from the same withholding THB 8,100. Without the optional PVD contribution, taxable income is THB 979,500 and tax THB 110,900. Eligible participation reduces tax by THB 24,000 but locks away THB 120,000; the immediate net cash cost is THB 96,000, excluding returns, employer contributions and later tax. Do not recommend the contribution without liquidity and fund-condition review.

```oa-check
name: Thailand 2026 PVD decision both ways
inputs:
  salary: 1200000
  social_actual: 10500
  life: 50000
  pvd_option: 120000
  withheld: 95000
steps:
  - expense: min(salary * 0.50, 100000)
  - net_without: salary - expense - 60000 - social_actual - life
  - net_with: net_without - pvd_option
  - tax_without: 7500 + 20000 + 37500 + (net_without - 750000) * 0.20
  - tax_with: 7500 + 20000 + 37500 + (net_with - 750000) * 0.20
  - tax_saved: tax_without - tax_with
  - net_cash_cost: pvd_option - tax_saved
  - refund_with: withheld - tax_with
expected:
  net_without: 979500
  net_with: 859500
  tax_without: 110900
  tax_with: 86900
  tax_saved: 24000
  net_cash_cost: 96000
  refund_with: 8100
```

## Ask the client first

- Year, residence days, family/filing status and place the work or investment income arose?
- Income categories and gross benefits, withholding certificates and prior payments?
- Children, parents and supported persons: status, income, relationship and non-duplicate proof?
- Actual retirement contributions and policy terms, other retirement-cap use and holding dates?
- Donation recipient, date, payment evidence and any proposed special deduction?
- Foreign income earned/remitted by year, source documents and foreign tax paid?

## Sources

| Source and actual reading scope | URL | Read on |
|---|---|---|
| Current Thai Revenue Code (Read for §§39-42 bis, 47-48, 50 bis, 56-57 quater and 60; family eligibility, exempt contributions, income categories, alternate method and filing) | https://www.rd.go.th/5937.html | 2026-11-16 |
| Income Tax Schedule (Read for all ordinary individual bands and the current schedule amendment) | https://www.rd.go.th/5938.html | 2026-11-16 |
| RD tax-method guidance for e-commerce individuals (Read for method 2, the THB 120,000 non-employment trigger, 0.005 computation, larger-result comparison and THB 5,000 exception; older temporary SME material on that page is not used) | https://www.rd.go.th/26218.html | 2026-11-16 |
| RD statutory reform table (Read for post-2017 expenses, allowances, filing thresholds and first-slice exemption attribution; older English overview not used for current deduction amounts) | https://www.rd.go.th/59668.html | 2026-11-16 |
| Consolidated Ministerial Regulation 126 (Read for clause 2(35), (36), (43), (53), (55), (61), (76), (90), (97), (102)-(103) and neighboring cross-cap/recapture conditions; not the whole regulation) | https://www.rd.go.th/2502.html | 2026-11-16 |
| Director-General income-tax Notification 136 (Read for all operative clauses 1-4, including support, parent income, lawful-child status, claimant restriction and evidence) | https://www.rd.go.th/23368.html | 2026-11-16 |
| RD foreign-income credit guide, November 2025 (Read for printed pages 3-4 for residence in the income year, remittance timing and treaty-credit boundaries) | https://www.rd.go.th/fileadmin/user_upload/porphor/GuideTaxFromAbroad_TH.pdf | 2026-11-16 |
| Order P.162/2566 (Read for the full operative single-page amendment excluding income arising before 1 January 2024) | https://www.rd.go.th/fileadmin/user_upload/kormor/newlaw/dn162A.pdf | 2026-11-16 |
| PND.91 annual return, 2025-2026 filing cycle (Read for both pages, computation A/B, allowances, donation order, withholding, foreign tax credit and refund choice) | https://www.rd.go.th/fileadmin/download/english_form/2025/PIT91_2568_eng_310368_02.pdf | 2026-11-16 |
| 2025 allowance attachment (Read for the complete single-page list and the dated Easy E-Receipt purchase window; not authority for 2026 stimulus relief) | https://www.rd.go.th/fileadmin/download/english_form/2025/Allowance2568_eng_310368_02.pdf | 2026-11-16 |
| 2026 form index (Read for all listed entries, half-year forms and annual-form availability boundary) | https://www.rd.go.th/english/68443.html | 2026-11-16 |
| RD filing-service index (Read for PND.90/91/94 routes, not a signed-in submission) | https://www.rd.go.th/rdeservice/63813.html | 2026-11-16 |

Not yet confirmed: final 2026 annual PND.90/91 forms and electronic deadline extensions; full non-employment standard-expense schedules before finalising mixed/business-income liability; subsidiary disability/support and parent-health-insurance conditions needed for an automatic claim; RMF purchase-continuity and all current Director-General recapture details; the National Savings Fund separate statutory member limit (legacy THB 30,000); the old Government Pension Fund 15% headline; blanket enhanced donation relief for education/sport/social gifts; any 2026 Easy E-Receipt THB 50,000 relief; complete late-filing/payment/remission rules, investment-income elections and taxpayer-specific treaty/foreign-credit relief. New SSF purchases are not allowed here under the expired historical window.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-16. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `thailand-pit` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/thailand-pit. If neither is available, confirm every figure against the official source pages cited above before relying on it.
