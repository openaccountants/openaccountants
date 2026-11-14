---
name: il-income-tax-returns
description: Use this skill when preparing, reviewing, or advising on Israeli annual income tax returns. Trigger on phrases like "doch shnati", "Form 1301", "Form 1214", "דוח שנתי", "mas hachnasa", "income tax Israel", "nekudot zikui", "נקודות זיכוי", "tax brackets Israel", "mas yesafim", "מס יסף", "surtax Israel", "mikdamot", "מקדמות", "Mas Shevach", "מס שבח", "capital gains Israel", "Form 6111", "Form 856", "Form 126", or any Israel income tax return query. ALWAYS read this skill before advising on Israeli income tax returns.
version: 1.2
jurisdiction: IL
tax_year: 2026
last_updated: 2026-11-14
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
---

# Israel: annual income tax returns and computation

> **Based on work by [Skills IL](https://github.com/skills-il/tax-and-finance)**, licensed under MIT. Adapted for the OpenAccountants format.

> **General reference only.** Produce a tax working paper and filing brief for review by an Israeli CPA. Establish the applicable year before using any rate or deadline.

## Scope

Individuals, sole proprietors and company return preparation for Israel in 2026. The personal-exertion bands and surtax below apply to 2026. The latest complete annual-return guidance read is the **2025-2026 filing cycle**: do not label its return forms, thresholds or extensions as tax-year 2026 instructions.

| Quick reference | Rate or threshold and condition | Official source |
|---|---|---|
| Personal-exertion income | Progressive s.121(b) bands below; also generally available from age 60, subject to the statutory books condition | ITO s.121, https://www.btl.gov.il/Laws1/00_0103_000000.pdf |
| Credit-point value | NIS 242/month; NIS 2,904/year (derived: 12 months) | ITO s.33A; 2026 booklet p.12, https://www.gov.il/BlobFolder/generalpage/income-tax-monthly-deductions-booklet/he/generalInformation_income-tax-monthly-deductions-booklet_monthly-deductions-booklet-2026.pdf |
| General surtax | 3% on total taxable income above NIS 721,560/year | ITO s.121B(a), https://www.btl.gov.il/Laws1/00_0103_000000.pdf |
| Capital-source surtax | Separate 2% on capital-source taxable income above NIS 721,560/year | ITO s.121B(a1), https://www.btl.gov.il/Laws1/00_0103_000000.pdf |
| Residential sale surtax entry | Sale value must exceed NIS 5,385,285 and sale must not be exempt; this is a sale-value test, not a gain threshold | ITO s.121B(e), https://www.btl.gov.il/Laws1/00_0103_000000.pdf |

## Ask the client first

Ask for residence, tax year, age, all household income and supporting certificates; every employer's Form 106 and withholding certificates; business books and allowable-expense evidence; VAT status; foreign income/assets/entity holdings; property acquisition/sale history; securities and crypto transaction records; pension deposits, insured income and fund certificates; personal-status/child/custody evidence; advance payments, losses and prior returns. Identify joint/separate spouse treatment and any representative authorization. Do not assume standard points, a default rental track or a universal capital-gain rate when facts are missing.

## The method, step by step

### Route the return and annexes

Use Form 1301 for an individual return; Form 135 for a voluntary refund only where the taxpayer qualifies and is not obliged to file the full return, as explained in [il-employee-tax-refund](il-employee-tax-refund.md). Companies use Form 1214; profit extraction is in [il-corporate-tax](il-corporate-tax.md). Employer salary reporting (Form 126) and supplier withholding reconciliation (Form 856) are payer obligations, not substitutes for the recipient's return. See [il-tax-withholding](il-tax-withholding.md).

Self-employment, salary, foreign interests/income, gains and rent are filing-screen inputs. Apply ITO ss.131-134 and the return-exemption regulations to the actual facts: multiple employers alone or a single threshold alone does not settle every filing case. New immigrants and returners need [il-new-immigrant](il-new-immigrant.md), including the reporting transition from 2026.

### Compute the taxable base

Reconcile income by source to books and third-party certificates; deduct only substantiated allowable amounts, applying restrictions, exemptions and the applicable loss rules. Allocate special-rate income separately. Salary withholding is a prepayment, not final tax. Keep a bridge from accounting profit to taxable income, then from tax before credits to liability after eligible credits and payments. Corporate taxable income is not automatically accounting profit. Use ITO ss.2, 17, 28, 31-32, 91-92 and 121 as applicable ([Ordinance](https://www.btl.gov.il/Laws1/00_0103_000000.pdf)).

### Personal-exertion bands: one home for the pack

The March 2026 amendment widens the bands retrospectively from 1 January 2026. Do not use the narrower 2025 bands for 2026. The monthly figures below are derived by dividing annual endpoints by 12; lower boundaries describe the next whole shekel, while actual calculations apply marginal slices without rounding a fractional shekel out of tax.

| Annual taxable slice (NIS) | Monthly equivalent (NIS, derived) | Rate | Official source |
|---|---|---|---|
| First 84,120 | First 7,010 | 10% | ITO s.121(b)(1)(a), https://www.btl.gov.il/Laws1/00_0103_000000.pdf |
| Above 84,120 to 120,720 | Above 7,010 to 10,060 | 14% | ITO s.121(b)(1)(b), https://www.btl.gov.il/Laws1/00_0103_000000.pdf |
| Above 120,720 to 228,000 | Above 10,060 to 19,000 | 20% | ITO s.121(b)(1)(c), https://www.btl.gov.il/Laws1/00_0103_000000.pdf |
| Above 228,000 to 301,200 | Above 19,000 to 25,100 | 31% | ITO s.121(b)(1)(d), https://www.btl.gov.il/Laws1/00_0103_000000.pdf |
| Above 301,200 to 560,280 | Above 25,100 to 46,690 | 35% | ITO s.121(a)(2), https://www.btl.gov.il/Laws1/00_0103_000000.pdf |
| Above 560,280 | Above 46,690 | 47% before surtax | ITO s.121(a)(3), https://www.btl.gov.il/Laws1/00_0103_000000.pdf |

Income outside personal exertion generally starts at 31% up to NIS 301,200, then 35% up to NIS 560,280, then 47%; s.121(b) also extends the lower bands to a person who reached age 60 in the tax year. The lower bands do not apply to income requiring books where acceptable books were not maintained, under s.121(b)(2). Special-rate income and exemptions require their own provisions. The 2025-2027 indexation freeze does not cancel the express 2026 band amendment (2026 booklet pp.3-4).

### Apply both surtax bases

General surtax = max(total taxable income - NIS 721,560, 0) x 3%. Additional capital surtax = max(capital-source taxable income - NIS 721,560, 0) x 2%. Capital-source income excludes business/employment income under s.2(1)/(2) and other personal-exertion income under s.121B(e). Capital-source is a statutory residual category, not just gains on disposals. Exclude the defined inflationary components. A residential-apartment gain enters only when both the sale-value and non-exempt conditions above hold. Do not apply a flat 5% to every dividend or gain merely because total income exceeds the threshold ([ITO s.121B](https://www.btl.gov.il/Laws1/00_0103_000000.pdf)).

### Credits and pension relief

Nekudot Zikui reduce tax subject to actual eligibility and use limits. The old category table is not a reliable entitlement calculator: resident sex/status, child birth year/age, custody, single parenthood, immigration, returning-resident benefit status, degree/vocational completion date, disability and combat reserve service need the applicable provision and evidence. Use [il-employee-tax-refund](il-employee-tax-refund.md) for the personal-status checklist; do not infer 5.75 points merely from the old freelancer's children's ages.

Keep s.45A credit and s.47 deduction separate from the mandatory pension contribution. The old blanket calculation of 5.5% and 11% of all NIS 300,000 income ignored qualifying-income ceilings and is withheld. The 2026 booklet p.12 lists s.45A(e)(2) NIS 19,400/month, s.45A(d)/(e)(1) NIS 189/month, s.47(a) NIS 9,700/month and s.47(a)(5) NIS 24,250/month. These are different statutory ceilings, not interchangeable deposit limits. Calculate relief only after confirming member status, insured/non-insured income, contribution type and how deductions/credits interact ([2026 booklet](https://www.gov.il/BlobFolder/generalpage/income-tax-monthly-deductions-booklet/he/generalInformation_income-tax-monthly-deductions-booklet_monthly-deductions-booklet-2026.pdf)). The earlier NIS 23,232 monthly credit ceiling remains withdrawn.

### Residential rent: compare lawful tracks

The exemption regime, the s.122 gross-rent election and ordinary net-income treatment are different choices. Under s.122, an individual with non-business income from residential letting in Israel may elect 10% on gross rent, generally without expenses, depreciation, deductions, offsets, credits or exemptions against that income, subject to the specific rent-paid exception in s.122(f). The s.122(f) exception permits qualifying rent paid in the same year for the taxpayer's Israeli home, or qualifying retirement/geriatric-home payments for the taxpayer/cohabiting spouse, against rent from the sole apartment. Deduct the lowest of actual qualifying payments, rental income and NIS 90,000/year (the statute says 90 thousand), with no duplicate deduction by anyone and no qualifying payment to the specified relative. The sole-apartment and household aggregation definitions include the cohabiting spouse and cohabiting children under 18; check them before use. Payment of the elected tax is within 30 days after tax-year end unless paid through advances, not automatically 31 January. The disposal calculation must also account for the statutory depreciation adjustment ([ITO s.122](https://www.btl.gov.il/Laws1/00_0103_000000.pdf)).

The 2026 deduction booklet p.13 confirms an exemption ceiling of NIS 5,654/month. The Residential Rental Income Exemption Law ss.1-3 requires qualifying residential property/tenant and a tenant-signed residential-use document. Aggregate rental income of the taxpayer, cohabiting spouse and children under 18; test each month across all residential-dwelling rents, including rents taxed on the 10% track and rents from a tenant who does not meet the exemption conditions. Where aggregate monthly rent exceeds the ceiling, reduce the ceiling by the excess, floored at zero; do not treat the ceiling as an annual all-or-nothing exemption. Property entered or required in business-income books is excluded from the definition. A corporate tenant must be approved by the Commissioner in a Gazette notice, operate without profit mainly for Ministry-approved housing, immigrant absorption, health or welfare, and rent to sublet for that purpose to an individual who is not its employee. [Exemption Law](https://www.btl.gov.il/Laws1/02_0103_100002.pdf). Ordinary-rate treatment may start above the lowest personal-exertion bracket, depending on age and income character. Do not default to a track without comparing tax and conditions.

### Gains, securities and real estate

For an individual, s.91(b) taxes real gains at the ordinary scale capped at 25%, or 30% for a company security where the seller is a material shareholder at sale or during the preceding 12 months. Unindexed debt instruments have separate 15%/20% rules; historical acquisition periods, inflationary components and special regimes differ. Hence “25% on every asset regardless of holding period” is wrong. Material shareholder is at least 10% of a control right under s.88, including indirect/joint-holding rules ([ITO ss.88, 91](https://www.btl.gov.il/Laws1/00_0103_000000.pdf)).

Under s.92, only a loss that would have been taxable as a gain qualifies. Offset real gains first; foreign-asset losses first offset foreign gains. Securities losses may also offset interest/dividends from the same security in that year. For other securities, the interest/dividend tax rate must not exceed the applicable s.125B(1)/s.125C(b) individual limit or s.126(a) company limit, under s.92(a)(4). Carryforward generally offsets capital gains only and requires filing the loss-year return; retain foreign-source ordering. Do not equate “same category” with the full statutory rule ([ITO s.92](https://www.btl.gov.il/Laws1/00_0103_000000.pdf)).

Forms 1322/1325 concern securities; do not automatically use them for all capital assets or crypto. The general s.91(d) asset-disposal report and tax advance are due within 30 days. Listed-security sales with full withholding have an exception; where no withholding and an annual-return duty apply, the statutory half-year reports/payments fall on 31 July and 31 January for the preceding half-years ([ITO s.91(d)](https://www.btl.gov.il/Laws1/00_0103_000000.pdf)). Crypto requires [il-crypto-tax](il-crypto-tax.md).

Mas Shevach has its own legislation. The old 30/40-day distinction, single-apartment NIS 5,008,000 ceiling and 18-month conditions, claimed 7 January 2014 linear cutoff, 25% gain method and expenses/CPI adjustments remain unresolved below. Do not file or compute a property return from this income-tax outline.

### Advance payments, company return and Form 6111

Use the assessment notice to identify the advance rate, taxable turnover and payment frequency. Reconcile advances against final liability and consider a supported rate-reduction request when income changes. Do not offer the old universal two-month calendar: ss.175 and following have distinct statutory/installment arrangements. VAT-exclusive revenue must be reconciled to the applicable advance base ([ITO s.175](https://www.btl.gov.il/Laws1/00_0103_000000.pdf)).

The 2025-2026 filing-cycle guide describes Form 6111 as standardized P&L, balance-sheet and tax-adjustment data. For 2025, turnover not exceeding NIS 300,000 including VAT is exempt, and qualifying agricultural books have a separate exception. Electronic/accounting-system conditions affect submission; retain the acknowledged copy. Reconcile to financial statements **and tax adjustments**, rather than forcing every tax field to equal accounting profit ([rights guide, return annex section](https://www.gov.il/BlobFolder/generalpage/income-tax-guide-knowyourright/he/Guides_IncomeTax_da-2025.pdf)). Do not assume the 2026 trigger without the year's instructions.

Company rate, closely held undistributed-profit rules, management fees, shareholder loans and dividend/salary comparisons are owned by [il-corporate-tax](il-corporate-tax.md); do not duplicate their figures here.

## Worked cases

### Freelancer: reconcile income, approved points and advance payments

Retain the old developer's NIS 450,000 revenue less NIS 80,000 allowable expenses = NIS 370,000 taxable personal-exertion income. **Assume an independently established 5.75 eligible points**; the old facts “male resident, children aged 4 and 8” do not prove that count. Gross 2026 tax is NIS 81,764; points reduce it by NIS 16,698, leaving NIS 65,066 before other reliefs and advances. On assumed advances of NIS 60,000, balance due is NIS 5,066. Pension/social-insurance deductions and other income are assumed already settled in the taxable input.

```oa-check
name: Freelancer annual working-paper reconciliation
inputs:
  revenue: 450000
  expenses: 80000
  eligible_points: 5.75
  advances: 60000
steps:
  - income: revenue-expenses
  - gross: 84120*0.10+36600*0.14+107280*0.20+73200*0.31+(income-301200)*0.35
  - credits: eligible_points*2904
  - liability: gross-credits
  - due: liability-advances
expected:
  income: 370000
  gross: 81764
  credits: 16698
  liability: 65066
  due: 5066
```

### Residential sale: decide whether it enters surtax

Retain the 2018 investment-apartment purchase at NIS 1,600,000 and sale for NIS 2,800,000. The unadjusted gain is NIS 1,200,000; this is **not** final Mas Shevach, since CPI, allowable costs and statutory property treatment are unresolved. Even assuming the sale is not exempt, its sale value is below NIS 5,385,285, so that apartment gain does not enter s.121B surtax. Assume separate employment income of NIS 800,000, no other capital income: general surtax on employment is NIS 2,353.20; the capital-source surtax from this apartment is zero. An above-ceiling, non-exempt sale would need both surtax bases recomputed.

```oa-check
name: Below-ceiling apartment sale and employment surtax
inputs:
  sale: 2800000
  purchase: 1600000
  employment: 800000
steps:
  - unadjusted_gain: sale-purchase
  - employment_surtax: max(employment-721560,0)*0.03
  - included_apartment_gain: 0
  - capital_surtax: max(included_apartment_gain-721560,0)*0.02
expected:
  unadjusted_gain: 1200000
  employment_surtax: 2353.20
  capital_surtax: 0
```

## When to refuse or refer

Refer unverified filing exemptions, personal-status points, pension ceilings, rental-track elections, historical gains, property disposals, mixed foreign income and closely held company rules. Do not promise a refund until aggregate annual tax and all prepayments are reconciled. Missing documents remain an open item rather than a conservative invented rate.

## Filing and payment

Choose the correct form and year in the Tax Authority personal/Shaam service, verify identity and representative authority, enter/upload reconciled data and all required annexes, clear validation messages, review liability, submit and retain the acknowledgment. Complete any signature/supporting-document delivery required by the selected submission route; payment is a separate step. No portal simulation authorizes actual submission here.

No tax-year 2026 annual-return deadline is confirmed. The 2025 guide states statutory baseline dates and possible extensions; the old claimed 29 May/30 June 2026 deadlines require the live year's service/extension notice, which could not be reopened. Form 126/856 dates and represented-client quotas require their own current notices. Keep their dates out of the client filing calendar until sourced.

## Completion checklist

Confirm year/place/source; reconcile every income certificate and the books; substantiate expenses, exemptions and losses; check age, status and credit eligibility; apply the correct bands and both surtax bases; compare rental options where applicable; reconcile advances and withholding; obtain professional review; retain filing/payment acknowledgments and unresolved items.

## Sources

| Source | URL | Read on |
|---|---|---|
| Consolidated Income Tax Ordinance; Read for ss.91(b), 91(d) including listed-security exceptions, 92 loss ordering/carryforward, 121 bands, 121B definitions and surtax, 122 rental election and 175 advances | https://www.btl.gov.il/Laws1/00_0103_000000.pdf | 2026-11-14 |
| Residential Rental Income Exemption Law; Read for ss.1-4 property/tenant definitions, household/monthly aggregation, taper and signed-use condition | https://www.btl.gov.il/Laws1/02_0103_100002.pdf | 2026-11-14 |
| ITA 2026 deduction booklet; Read for pp.3-4 freeze/band amendment, pp.10-13 rates, surtax, credit point, individually labelled pension ceilings and rental exemption ceiling | https://www.gov.il/BlobFolder/generalpage/income-tax-monthly-deductions-booklet/he/generalInformation_income-tax-monthly-deductions-booklet_monthly-deductions-booklet-2026.pdf | 2026-11-14 |
| ITA 2025 rights guide, 2025-2026 filing cycle; Read for return annex Form 6111 turnover and agricultural/electronic exceptions, filing baseline/extensions, residential-rent exemption/taper section | https://www.gov.il/BlobFolder/generalpage/income-tax-guide-knowyourright/he/Guides_IncomeTax_da-2025.pdf | 2026-11-14 |

Not yet confirmed: tax-year 2026 return forms/deadlines and Form 6111 trigger; the old 2025-cycle 29 May/30 June 2026 extensions; Form 1214/126/856 dates and representative extensions. The old pension example (NIS 300,000 income, NIS 33,000/11% deduction and NIS 16,500/5.5% base for a 35% credit) is not usable without full member/insured-income and cap computation; NIS 23,232 monthly credit ceiling is withdrawn. The old married-woman example (children aged 3 and 7, claimed 6.25 points giving NIS 18,150) is preserved as an unsupported entitlement scenario, not a verified credit claim. The old personal-status category table, child/immigrant point counts and reserve-service eligibility are routed to the refund skill, not assumed here. Mas Shevach calculation/30-vs-40-day filing/single-apartment relief (old NIS 5,008,000 and 18-month claims), old 7 January 2014 linear cutoff and non-income-tax property conditions remain unconfirmed. The annual-return service page could not be reopened (HTTP 403); no failed fetch is recorded as a read. The old two-month advance calendar is not treated as universal. Companies and withholding retain their own sibling boundaries.
