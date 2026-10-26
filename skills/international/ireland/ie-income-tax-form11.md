---
name: ie-income-tax-form11
description: "Irish income tax self-assessment on Form 11 for tax year 2026 (and the 2025 return due now). Covers who is a chargeable person (self-employed, proprietary directors over 15%, non-PAYE income over EUR 5,000 net or EUR 30,000 gross), the 20% and 40% bands (EUR 44,000 single, EUR 53,000 married) and the main credits including the EUR 2,000 Earned Income Credit, Case I and II trading profit, add-backs, capital allowances at 12.5% over 8 years and the car CO2 limits, losses, pension relief, Case V rental income, where USC and PRSI Class S fit, pay and file on 31 October (18 November 2026 on ROS), preliminary tax, the 5% and 10% surcharges and 0.0219% daily interest. Trigger on: Form 11, self-assessment Ireland, sole trader tax Ireland, Case I, ROS pay and file, earned income credit, proprietary director return. Out of scope: ie-payroll, ie-usc, ie-prsi-class-s, ie-preliminary-tax, ie-paye-rental-nonresident, ie-cgt, ie-corporation-tax, ie-cross-border."
version: 2.1
jurisdiction: IE
tax_year: 2026
last_updated: 2026-10-24
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Ireland Form 11 (2026): self-assessment for self-employed and other chargeable persons

> **Source-cited draft.** Drafted from the Taxes Consolidation Act 1997 (TCA) as amended by Finance Act 2024 s.3 (bands and credits from 2025 on) and Finance Act 2025 ss.2, 26, 32, 100 and 102, Revenue's Notes for Guidance on Part 41A (Finance Act 2025 edition), Revenue's Guide to Completing 2025 Pay and File Self-Assessment Returns and Revenue's self-assessment pages, all read on 2026-10-24. No accountant has reviewed it.

Authority: the Revenue Commissioners. The tax year is the calendar year. Currency: euro. Section numbers are TCA 1997 unless another act is named. The Law Reform Commission's Revised Acts do not include the TCA, so the law is cited through the Finance Act section that set each figure.

Two years are live in October 2026. The **2025 Form 11** is due now (31 October 2026, or 18 November 2026 on ROS), with **2026 preliminary tax**. The **2026 Form 11** is due by 31 October 2027. The bands and credits are the same for both years; USC and PRSI differ (see the rates table).

See also: `ie-payroll` (PAYE under the RPN, Class A PRSI), `ie-usc` (USC in depth), `ie-prsi-class-s` (Class S in depth), `ie-preliminary-tax` (preliminary tax in depth), `ie-paye-rental-nonresident` (Form 12, Case V rental income in depth, non-residents), `ie-cgt` (the CGT panel), `ie-corporation-tax` (companies), `ie-formation` (registering), `ie-vat-return` (VAT), `ie-cross-border` and `ie-foreign-tax-and-withholding` (residence, treaties).

## Who this applies to

- **A chargeable person files Form 11** (s.959A, s.959I). You are a chargeable person if any of these apply for the year ([Revenue, Guide to Completing 2025 Returns, "Who is this guide for?"](https://www.revenue.ie/en/self-assessment-and-self-employment/documents/guide-pay-file.pdf)):
  - you have trading income from a business, trade, profession or vocation (Case I or Case II);
  - you are a **proprietary director**: you own, or can control directly or indirectly, more than 15% of the company's ordinary share capital;
  - you have PAYE income and non-PAYE income over EUR 5,000 net (after capital allowances, expenses and losses carried forward), or over EUR 30,000 gross (before capital allowances and losses);
  - your income is only rental, foreign or other non-PAYE income;
  - you are resident in Ireland and opened a foreign bank account in the year (s.895; not if it is reported under DAC2/CRS or FATCA, is not in a listed territory under s.835YA, and you are not otherwise chargeable).
- **The EUR 5,000 and EUR 30,000 tests.** Section 959B takes out of self-assessment a PAYE worker whose net non-PAYE income does not exceed EUR 5,000 (and gross does not exceed EUR 30,000), where it is coded against their credits or fully taxed at source. This exclusion does not apply to company directors or their jointly assessed spouses, unless the company is dormant ([Revenue, Notes for Guidance Part 41A, s.959B](https://www.revenue.ie/en/tax-professionals/documents/notes-for-guidance/tca/part41a.pdf)). Below the limits, the person uses Form 12 in myAccount ([Revenue, who should register](https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/register-it-self-assessment.aspx)).
- **Out:** companies (they file CT1, see `ie-corporation-tax`; a proprietary director still files their own Form 11); the partnership itself (the precedent partner files Form 1 (Firms), s.959M; each partner then puts their share on their own Form 11); a PAYE-only employee (Form 12, see `ie-paye-rental-nonresident`).
- **Residence** decides what is taxed: see `ie-cross-border`. A non-resident files Form 11 for Irish-source income above the limits.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Standard rate band, single or widowed, no qualifying children (s.15, Table Part 1) | first EUR 44,000 at 20%, balance at 40% | 2025 and 2026 | https://www.irishstatutebook.ie/eli/2024/act/43/section/3/enacted/en/html |
| Band, single person qualifying for the Single Person Child Carer Credit (s.15, Part 2) | first EUR 48,000 at 20%, balance at 40% | 2025 and 2026 | same |
| Band, married or civil partners (s.15, Part 3) | first EUR 53,000 at 20%, balance at 40% | 2025 and 2026 | same |
| Increase for a second income (s.15(3)(i)) | lower of EUR 35,000 or the lower earner's income; not transferable | 2025 and 2026 | same |
| Single Person Tax Credit / Married or Civil Partner Tax Credit (s.461) | EUR 2,000 / EUR 4,000 | 2025 and 2026 | same |
| Single Person Child Carer Credit (s.462B) | EUR 1,900 | 2025 and 2026 | same |
| Home Carer Tax Credit, maximum (s.466A) | EUR 1,950 | 2025 and 2026 | same |
| Employee (PAYE) Tax Credit (s.472) | EUR 2,000 | 2025 and 2026 | same |
| Earned Income Tax Credit (s.472AB) | lower of EUR 2,000 or 20% of qualifying earned income; with the Employee credit, the two together cannot exceed EUR 2,000 | 2025 and 2026 | https://www.revenue.ie/en/personal-tax-credits-reliefs-and-exemptions/income-and-employment/earned-income-credit/index.aspx |
| Age Tax Credit, single / married | EUR 245 / EUR 490 | 2025 and 2026 | https://www.revenue.ie/en/personal-tax-credits-reliefs-and-exemptions/tax-relief-charts/index.aspx |
| USC (detail in `ie-usc`) | 0.5% on first EUR 12,012; 2% on next EUR 16,688; 3% on next EUR 41,344; 8% on the balance; none if income is EUR 13,000 or less; 3% surcharge on non-PAYE income over EUR 100,000 | 2026 | https://www.irishstatutebook.ie/eli/2025/act/18/section/2/enacted/en/html |
| USC for the 2025 return due now | 0.5% on first EUR 12,012; 2% from EUR 12,012 to EUR 27,382; 3% to EUR 70,044; 8% on the balance | 2025 | https://www.revenue.ie/en/self-assessment-and-self-employment/documents/guide-pay-file.pdf |
| PRSI Class S on self-assessed income (detail in `ie-prsi-class-s`) | 4.2375% blended (4.2% to 30 September, 4.35% from 1 October), minimum EUR 650; nil if income under EUR 5,000 | 2026 | https://www.gov.ie/en/department-of-social-protection/publications/prsi-class-s-rates/ |
| PRSI Class S on 2025 income | 4.125% blended, minimum EUR 650 | 2025 | https://www.revenue.ie/en/self-assessment-and-self-employment/documents/guide-pay-file.pdf |
| Wear and tear on plant, machinery and cars bought on or after 4 December 2002 (s.284) | 12.5% a year over 8 years | 2026 | https://www.revenue.ie/en/self-assessment-and-self-employment/documents/guide-pay-file.pdf |
| Car cost limit, cars bought on or after 1 January 2025: CO2 0-120 g/km (VRT A) / 121-155 (B, C) / 156 and over (D, E, F) | EUR 24,000 / 50% of EUR 24,000, or 50% of the retail price new if lower / nil | 2026 | same |
| Accelerated allowances for energy-efficient equipment (s.285A) | scheme extended to 31 December 2030 | 2026 | https://www.irishstatutebook.ie/eli/2025/act/18/section/26/enacted/en/html |
| Losses of a trade carried on in a non-active capacity, set against other income | up to EUR 31,750 a year | 2025 | https://www.revenue.ie/en/self-assessment-and-self-employment/documents/guide-pay-file.pdf |
| Pension relief (RAC, PRSA), % of net relevant earnings by age | under 30: 15%; 30-39: 20%; 40-49: 25%; 50-54: 30%; 55-59: 35%; 60+: 40% | 2026 | https://www.revenue.ie/en/jobs-and-pensions/pension/relief/tax-relief-limits.aspx |
| Pension relief earnings limit | EUR 115,000 a year | 2026 | same |
| High Income Earner Restriction: applies if income is EUR 125,000 or more, specified reliefs are over EUR 80,000 and over 20% of adjusted income | Form RR1 | 2026 | https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/hier.aspx |
| Pay and file date (s.959A specified return date; s.959AO) | 31 October after the tax year; preliminary tax for the current year on the same date | 2026 | https://www.revenue.ie/en/tax-professionals/documents/notes-for-guidance/tca/part41a.pdf |
| ROS extension for the 2025 return and 2026 preliminary tax, if both filed and paid on ROS | 18 November 2026 | 2026 | https://www.revenue.ie/en/tax-professionals/ebrief/2026/no-0342026.aspx |
| Preliminary tax safe harbours (s.959AO) | lowest of 90% of current year, 100% of previous year, 105% of pre-preceding year (direct debit only, not if that year was nil) | 2026 | https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/preliminary-tax.aspx |
| Late filing surcharge (s.1084) | 5% of tax due, max EUR 12,695, within 2 months; 10%, max EUR 63,485, after 2 months | 2026 | https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/pay-file-system.aspx |
| Interest on late income tax (s.1080) | 0.0219% a day or part of a day | 2026 | https://www.revenue.ie/en/tax-professionals/tdm/collection/debt-management/guidelines-for-charging-interest-on-late-payment.pdf |
| Revenue estimate for a missing return (s.959AX, from 1 January 2026) | greater of the average tax due on the last 2 returns or EUR 1,000 | 2026 | https://www.irishstatutebook.ie/eli/2025/act/18/section/32/enacted/en/html |

Budget 2027 (6 October 2026) announced changes for 2027. They are not law until the Finance Act 2026 is passed and are not in this skill.

## The taxable base

**Step 1: trading profit (Case I trade, Case II profession).** Start from the accounts. Turnover excludes VAT if the trader is VAT registered (see `ie-vat-return`). Separate non-trading receipts: salary, rent, interest, dividends, refunds and transfers between the client's own accounts. Accounts are kept, not sent: complete the "Extract from Accounts" panels and keep the records for six years ([Guide, "Attachments to Returns"](https://www.revenue.ie/en/self-assessment-and-self-employment/documents/guide-pay-file.pdf)).

**Step 2: deductions and add-backs.** A cost is deductible if it is revenue (not capital) and incurred wholly and exclusively for the trade. Add back on Form 11: the private part of motor, light, heat and phone; donations and non-staff entertainment; depreciation; a loss on sale of fixed assets (deduct a profit on sale) ([Guide, Panel B](https://www.revenue.ie/en/self-assessment-and-self-employment/documents/guide-pay-file.pdf)). Never deductible: income tax, USC, PRSI and preliminary tax; drawings; loan principal.

**Step 3: capital allowances instead of depreciation.** Plant, machinery and business cars: 12.5% a year over 8 years on net cost (after grants and reclaimable VAT). A car's cost is capped by its CO2 band (rates table) and the allowance is cut to the business-use share. A sale gives a balancing allowance or charge. Taxis and cars for short-term hire use 40% reducing balance ([Guide, capital allowances](https://www.revenue.ie/en/self-assessment-and-self-employment/documents/guide-pay-file.pdf)).

**Step 4: losses.** A trading loss can be set against other income of the same year (s.381), or carried forward against later profits of the same trade only (s.382). A trade carried on in a non-active capacity can set only EUR 31,750 a year against other income; the excess carries forward ([Guide, Lines 117-118](https://www.revenue.ie/en/self-assessment-and-self-employment/documents/guide-pay-file.pdf)).

**Step 5: other income.** Add Case V rental profit, PAYE income (Panels D and E), foreign income (Panel F), and other Irish income such as interest and dividends (Panel G). **Rental income in outline:** compute each letting separately: gross rent less the outgoings s.97(2) allows. 100% of interest on borrowing for a residential letting is deductible where the tenancy is registered with the Residential Tenancies Board. Rental losses carry forward against rental income ([Guide, Panel C](https://www.revenue.ie/en/self-assessment-and-self-employment/documents/guide-pay-file.pdf)). Use `ie-paye-rental-nonresident` for Case V in depth.

**Step 6: total income and deductions.** Deduct pension contributions (Panel I) within the age percentage of net relevant earnings and the EUR 115,000 earnings limit. Rental income is not relevant earnings.

**Step 7: income tax.** Apply the band for the person's status at 20% and the rest at 40%. Then subtract credits; credits reduce tax, not income ([FA 2024 s.3](https://www.irishstatutebook.ie/eli/2024/act/43/section/3/enacted/en/html)). The Earned Income Credit is for self-employed earned income and a proprietary director's pay, not rent or interest. It cannot pass to a spouse. With the Employee credit, the two together cannot exceed EUR 2,000 ([Revenue, EIC](https://www.revenue.ie/en/personal-tax-credits-reliefs-and-exemptions/income-and-employment/earned-income-credit/index.aspx)).

**Step 8: USC and PRSI.** Both are self-assessed on Form 11 and paid with income tax.
- USC: on total income after capital allowances (active traders) but **before** pension contributions; the surcharge tests non-PAYE income only. Use `ie-usc`.
- PRSI Class S: on gross income after capital allowances, before pension contributions; minimum EUR 650 ([Revenue, PRSI](https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/prsi-need-pay.aspx)). Pension contributions get income tax relief only, not PRSI or USC relief ([Revenue, pension relief](https://www.revenue.ie/en/jobs-and-pensions/pension/relief/index.aspx)). Use `ie-prsi-class-s`. Department of Social Protection pensions and benefits are exempt from PRSI ([Guide, PRSI for the self-employed](https://www.revenue.ie/en/self-assessment-and-self-employment/documents/guide-pay-file.pdf)).

**Step 9: self-assessment.** Total income tax, USC and PRSI, less tax deducted at source and preliminary tax paid, gives the balance due or overpaid (Panel P).

**Where items go on the 2025 Form 11** ([Guide, contents](https://www.revenue.ie/en/self-assessment-and-self-employment/documents/guide-pay-file.pdf)): A personal details; B self-employed income; C Irish rental income; D and E PAYE, BIK, pensions; F foreign income; G Irish other income; H exempt income; I charges and deductions; J personal tax credits; K restriction of reliefs (HIER); L capital gains; M, N, O chargeable assets, capital acquisitions, property incentives; P self-assessment. A shorter Form 11S exists for simpler cases.

## Deadlines and filing

- **Register** through eRegistration on ROS or Form TR1 parts A and B ([Revenue, who should register](https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/register-it-self-assessment.aspx)).
- **Pay and file, 31 October each year** (s.959I, s.959AO). By 31 October 2026: file the 2025 return, make the 2025 self-assessment, pay the 2025 balance, and pay 2026 preliminary tax ([Guide, "Pay and File"](https://www.revenue.ie/en/self-assessment-and-self-employment/documents/guide-pay-file.pdf)).
- **ROS extension:** 18 November 2026, but only if the 2025 return is filed **and** the 2025 balance and 2026 preliminary tax are paid through ROS. If only one is done on ROS, the date stays 31 October 2026 ([eBrief 034/26](https://www.revenue.ie/en/tax-professionals/ebrief/2026/no-0342026.aspx)).
- **The 2026 return** is due by 31 October 2027, with 2027 preliminary tax. Revenue has not yet announced the 2027 ROS date.
- **Preliminary tax:** pay at least the lowest of the three safe harbours (rates table). If too little is paid, or it is paid late, all the year's tax is treated as due on 31 October of the tax year and interest runs from then (s.959AO). In the first year in self-assessment the previous year's liability is nil, so preliminary tax is usually nil ([Revenue, preliminary tax](https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/preliminary-tax.aspx)). Detail in `ie-preliminary-tax`.
- **Direct debit:** Finance Act 2025 s.100 deleted s.959AP(2) to (4), removing the fixed payment dates and the minimum number of instalments. The Collector-General now sets the conditions; if all scheduled payments are made, preliminary tax is treated as paid on 31 October. Revenue's Tax and Duty Manual 41-00-28 still prints the old 3 and 8 instalment rule; the statute governs ([FA 2025 s.100](https://www.irishstatutebook.ie/eli/2025/act/18/section/100/enacted/en/html); [Notes for Guidance, s.959AP](https://www.revenue.ie/en/tax-professionals/documents/notes-for-guidance/tca/part41a.pdf)).
- **Paper returns:** file by 31 August 2026 and Revenue calculates the tax; Revenue extended this to 30 September 2026. A paper return after that must include the self-assessment; leaving that panel blank can cost a EUR 250 penalty ([Guide](https://www.revenue.ie/en/self-assessment-and-self-employment/documents/guide-pay-file.pdf)).
- **How to pay:** on ROS by debit instruction or Visa or Mastercard card; on myAccount; or by direct debit for preliminary tax ([Revenue, preliminary tax](https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/preliminary-tax.aspx)).
- **Amend** a ROS return on ROS; for a paper return, contact Revenue ([Revenue, pay and file](https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/pay-file-system.aspx)).
- **Late claims:** from Finance Act 2025, a return filed late can still claim allowances, deductions and reliefs, unless another provision sets its own deadline (s.959I(6), [FA 2025 s.102](https://www.irishstatutebook.ie/eli/2025/act/18/section/102/enacted/en/html)).
- **Repayment claims** have a four-year limit (s.865): 2022 claims must reach Revenue by 31 December 2026 ([Guide](https://www.revenue.ie/en/self-assessment-and-self-employment/documents/guide-pay-file.pdf)).

## Penalties and interest

- **Late filing surcharge (s.1084):** a percentage of the **total** tax for the year, not just the unpaid balance. For the 2025 return: 5% (max EUR 12,695) if filed after 31 October 2026 and by 31 December 2026; 10% (max EUR 63,485) after 31 December 2026 ([Guide, "Surcharge for Late Returns"](https://www.revenue.ie/en/self-assessment-and-self-employment/documents/guide-pay-file.pdf)). Missing the ROS conditions means the 31 October date applies.
- **LPT surcharge:** if the Local Property Tax return or payment (or an agreed arrangement) is outstanding when Form 11 is filed, the self-assessment is increased by 10%, even if Form 11 is on time. Once LPT is brought up to date, this surcharge is capped at the LPT owed (same source).
- **Interest (s.1080):** 0.0219% a day, or part of a day, on late income tax ([TDM, interest guidelines](https://www.revenue.ie/en/tax-professionals/tdm/collection/debt-management/guidelines-for-charging-interest-on-late-payment.pdf)). A preliminary tax shortfall moves the due date of the whole liability back to 31 October of the tax year.
- **Revenue estimate (s.959AX, from 2026):** if a return is not filed, Revenue may serve an estimate of the greater of the average tax due on the last two returns or EUR 1,000, recoverable as if self-assessed. It falls away if, within 30 days, the person files and pays (with interest and surcharge) or shows they are not chargeable ([FA 2025 s.32](https://www.irishstatutebook.ie/eli/2025/act/18/section/32/enacted/en/html)).
- **Audit:** self-assessed returns are open to Revenue audit; refer audit and disclosure cases to a practitioner.

## Cross-border points

- **Residence and domicile** decide the scope: residents are taxed on worldwide income; non-domiciled residents use the remittance basis on foreign income (see `ie-cross-border`, `ie-non-dom`).
- **Foreign income** goes in Panel F. Relief for foreign tax is by treaty credit or Schedule 24: see `ie-foreign-tax-and-withholding`.
- **A foreign bank account** opened in the year can make a resident a chargeable person (see "Who this applies to").
- **Non-residents** with Irish rent or trading income file Form 11; personal credits and the 75% test under s.1032 are in `ie-paye-rental-nonresident`. A non-resident whose self-assessed income is only unearned income (such as rent or deposit interest) pays no PRSI ([Guide, PRSI for the self-employed](https://www.revenue.ie/en/self-assessment-and-self-employment/documents/guide-pay-file.pdf)).
- **Social insurance across borders** (A1 certificates, postings): see `ie-prsi-cross-border`.

## Worked examples

### Example 1: single sole trader, profit EUR 60,000 (2026 estimate)

Siobhan, single, aged 38, a designer, has adjusted trading profit of EUR 60,000 for 2026 after capital allowances. No other income, no pension contributions.

Income tax: EUR 44,000 at 20% = 8,800; EUR 16,000 at 40% = 6,400; gross 15,200. Less the Single Person credit 2,000 and the Earned Income Credit 2,000 (20% of 60,000 is more than 2,000): EUR 11,200. USC: 60.06 + 333.76 + 3% of (60,000 less 28,700) = 939.00, total EUR 1,332.82; no surcharge. PRSI Class S: 60,000 x 4.2375% = EUR 2,542.50, above the EUR 650 minimum. Total 2026 liability: EUR 15,075.32. This also sets her 2027 preliminary tax under the 100% test.

```oa-check
name: Single sole trader, profit EUR 60,000 (2026)
inputs:
  profit: 60000
steps:
  - it_gross: min(profit, 44000) * 0.20 + max(profit - 44000, 0) * 0.40
  - eic: min(2000, profit * 0.20)
  - income_tax: it_gross - 2000 - eic
  - usc: 12012 * 0.005 + 16688 * 0.02 + (min(profit, 70044) - 28700) * 0.03 + max(profit - 70044, 0) * 0.08
  - prsi: max(profit * 0.042375, 650)
  - total: income_tax + usc + prsi
expected:
  income_tax: 11200.00
  usc: 1332.82
  prsi: 2542.50
  total: 15075.32
```

### Example 2: trader with a car, rental income, a pension and the USC surcharge (2026)

Ciaran, single, aged 42, an active sole trader, has trading profit of EUR 95,000 before capital allowances. In 2026 he buys a new car for EUR 40,000 with CO2 of 130 g/km (VRT category B), used 80% for business, and a laptop for EUR 2,400. He has Case V rental profit of EUR 12,000 and pays EUR 8,000 into a PRSA.

Capital allowances: the car is category B, so the cost that qualifies is the lower of 50% of 24,000 and 50% of its retail price new (40,000), which is 12,000. 12.5% of that is 1,500; at 80% business use, 1,200. Laptop: 2,400 x 12.5% = 300. Total 1,500. Trading profit 93,500. Total income with rent: 105,500.

Pension: his limit is 25% of net relevant earnings of 93,500 (under the 115,000 cap) = 23,375, so all 8,000 is relieved. Taxable income 97,500. Income tax: 8,800 + 40% of 53,500 (21,400) = 30,200, less credits 4,000 = EUR 26,200.

USC is on 105,500 (after capital allowances, before the pension): 60.06 + 333.76 + 1,240.32 + 8% of 35,456 (2,836.48) = 4,470.62. All his income is non-PAYE and it is over EUR 100,000, so the 3% surcharge applies to 5,500: 165.00. USC EUR 4,635.62. PRSI Class S: 105,500 x 4.2375% = EUR 4,470.56 (rent counts; the pension does not reduce it). Total EUR 35,306.18.

```oa-check
name: Trader with car, rental income, PRSA and USC surcharge (2026)
inputs:
  trading_before_ca: 95000
  car_cost: 40000
  business_use: 80
  laptop: 2400
  rent_profit: 12000
  pension_paid: 8000
steps:
  - car_qualifying: min(24000 * 0.5, car_cost * 0.5)
  - car_ca: car_qualifying * 0.125 * business_use / 100
  - ca: car_ca + laptop * 0.125
  - trading: trading_before_ca - ca
  - total_income: trading + rent_profit
  - pension_relief: min(pension_paid, min(trading, 115000) * 0.25)
  - taxable: total_income - pension_relief
  - income_tax: 44000 * 0.20 + (taxable - 44000) * 0.40 - 2000 - min(2000, trading * 0.20)
  - usc_standard: 12012 * 0.005 + 16688 * 0.02 + 41344 * 0.03 + (total_income - 70044) * 0.08
  - usc_surcharge: max(total_income - 100000, 0) * 0.03
  - usc: usc_standard + usc_surcharge
  - prsi: round(max(total_income * 0.042375, 650), 2)
  - total: income_tax + usc + prsi
expected:
  ca: 1500.00
  total_income: 105500.00
  taxable: 97500.00
  income_tax: 26200.00
  usc: 4635.62
  prsi: 4470.56
  total: 35306.18
```

## Ask the client first

1. Which year, and why are you in self-assessment: trading, proprietary director (over 15%), rent, foreign income, or side income over EUR 5,000 net / EUR 30,000 gross? (Form 11 or Form 12.)
2. Single, married or civil partner (one or two incomes), or a single parent; your age and any full medical card? (Band, credits, USC reduced rates, pension limit.)
3. Accounts or records for the year, assets bought or sold, and for any car: cost, date, CO2 g/km and business-use share? (Capital allowances and add-backs.)
4. Other income: PAYE pay, rent, interest, dividends, foreign income, social welfare? (Credits, USC surcharge, PRSI.)
5. Preliminary tax paid and how (direct debit?), and the final liabilities for the two previous years? (Balance due and the 90/100/105% tests.)
6. Losses or capital allowances carried forward, pension contributions paid, and is your LPT up to date? (Base, relief, the 10% LPT surcharge.)

Refer to a practitioner: partnerships' own accounts (Form 1 (Firms)), the High Income Earner Restriction, property-based incentive reliefs and Section 23 relief, farming reliefs, residence changes and split years, foreign tax credits, share schemes, Revenue audits or unfiled years, and any year other than 2025 or 2026.

## Sources

| Source | URL | Read on |
|---|---|---|
| Finance Act 2024 (No. 43 of 2024) s.3: s.15 bands, s.461, 462B, 466A, 472, 472AB credits, from 2025 on | https://www.irishstatutebook.ie/eli/2024/act/43/section/3/enacted/en/html | 2026-10-24 |
| Finance Act 2025 (No. 18 of 2025), arrangement of sections (no change to s.15 or the personal credits) | https://www.irishstatutebook.ie/eli/2025/act/18/enacted/en/html | 2026-10-24 |
| Finance Act 2025 s.2: s.531AN USC 2026 bands | https://www.irishstatutebook.ie/eli/2025/act/18/section/2/enacted/en/html | 2026-10-24 |
| Finance Act 2025 s.26: s.285A accelerated allowances to 31 December 2030 | https://www.irishstatutebook.ie/eli/2025/act/18/section/26/enacted/en/html | 2026-10-24 |
| Finance Act 2025 s.32: new s.959AX Revenue estimate | https://www.irishstatutebook.ie/eli/2025/act/18/section/32/enacted/en/html | 2026-10-24 |
| Finance Act 2025 s.100: s.959AP direct debit | https://www.irishstatutebook.ie/eli/2025/act/18/section/100/enacted/en/html | 2026-10-24 |
| Finance Act 2025 s.102: s.959I(6) late claims | https://www.irishstatutebook.ie/eli/2025/act/18/section/102/enacted/en/html | 2026-10-24 |
| Finance Act 2025 s.107: Part 1 in operation 1 January 2026 | https://www.irishstatutebook.ie/eli/2025/act/18/section/107/enacted/en/html | 2026-10-24 |
| Revenue, Notes for Guidance TCA 1997 Part 41A, Finance Act 2025 edition (s.959B, 959I, 959AN to 959AP) | https://www.revenue.ie/en/tax-professionals/documents/notes-for-guidance/tca/part41a.pdf | 2026-10-24 |
| Revenue, Guide to Completing 2025 Pay and File Self-Assessment Returns | https://www.revenue.ie/en/self-assessment-and-self-employment/documents/guide-pay-file.pdf | 2026-10-24 |
| Revenue, Tax rates, bands and reliefs | https://www.revenue.ie/en/personal-tax-credits-reliefs-and-exemptions/tax-relief-charts/index.aspx | 2026-10-24 |
| Revenue, Earned Income Credit | https://www.revenue.ie/en/personal-tax-credits-reliefs-and-exemptions/income-and-employment/earned-income-credit/index.aspx | 2026-10-24 |
| Revenue, Who should register for Income Tax self-assessment | https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/register-it-self-assessment.aspx | 2026-10-24 |
| Revenue, What is preliminary tax | https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/preliminary-tax.aspx | 2026-10-24 |
| Revenue, Pay and file system | https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/pay-file-system.aspx | 2026-10-24 |
| Revenue, eBrief 034/26, ROS extension to 18 November 2026 | https://www.revenue.ie/en/tax-professionals/ebrief/2026/no-0342026.aspx | 2026-10-24 |
| Revenue, Do you need to pay PRSI | https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/prsi-need-pay.aspx | 2026-10-24 |
| Revenue, High Income Earner Restriction | https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/hier.aspx | 2026-10-24 |
| Revenue, Tax relief limits on pension contributions | https://www.revenue.ie/en/jobs-and-pensions/pension/relief/tax-relief-limits.aspx | 2026-10-24 |
| Revenue, Tax relief for pension contributions (income tax relief only; no USC or PRSI relief) | https://www.revenue.ie/en/jobs-and-pensions/pension/relief/index.aspx | 2026-10-24 |
| Revenue, Tax and Duty Manual, Guidelines for charging interest on late payment (updated May 2025) | https://www.revenue.ie/en/tax-professionals/tdm/collection/debt-management/guidelines-for-charging-interest-on-late-payment.pdf | 2026-10-24 |
| Department of Social Protection, PRSI Class S rates | https://www.gov.ie/en/department-of-social-protection/publications/prsi-class-s-rates/ | 2026-10-24 |

Not yet confirmed: (1) the consolidated TCA text: the Law Reform Commission's Revised Acts do not include the TCA, so sections are cited through the amending Finance Act and Revenue's Notes for Guidance; amendments before Finance Act 2024 were not read in their enacting acts; (2) the 2027 ROS extension date for the 2026 Form 11; (3) the conditions the Collector-General now sets for preliminary tax direct debits after FA 2025 s.100 (the old version's rules of 8 or more payments, or at least 3 for a mid-year start, were in the deleted subsections); (4) the rule letting a new trader file the first two years' returns by the second year's return date (old version, Tax and Duty Manual 41-00-28, not re-read); (5) the DIRT rate on deposit interest (the old version said 33%; the USC exemption for DIRT-paid interest is in `ie-usc`); (6) the statutory section behind the EUR 250 penalty for an incomplete self-assessment panel; (7) whether the PRSI exemption above age 66 in Revenue's 2025 guide still applies after the age limit moved to 70 from 1 January 2024 (see `ie-prsi-class-s`); (8) whether the s.1084 surcharge base includes USC and PRSI; (9) the home office apportionment and the "treat unclear items as capital" practice points from the old version; (10) Budget 2027 changes, not yet law.

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
