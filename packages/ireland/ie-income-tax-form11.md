---
name: ie-income-tax-form11
description: Use this skill whenever asked about Irish income tax for self-employed individuals filing Form 11. Trigger on phrases like "Form 11", "self-assessment Ireland", "Case I profits", "Case II profits", "USC", "PRSI Class S", "preliminary tax Ireland", "earned income credit", "trading profits", "self-employed tax Ireland", "ROS filing", or any question about computing or filing income tax for a self-employed person in Ireland. This skill covers income tax rates (20%/40%), USC bands, PRSI Class S, personal tax credits, allowable deductions, capital allowances, preliminary tax, and Form 11 structure. ALWAYS read this skill before touching any Irish income tax work.
version: 2.0
jurisdiction: IE
tax_year: 2026
last_updated: 2026-09-27
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

## Scope

This Guide is for a self-employed individual in the Republic of Ireland (sole trader, profession, or partner reporting a share of partnership profit), or an adviser preparing their Income Tax Return and self-assessment on Form 11. It covers who must file, adjusted Case I / Case II profit, capital allowances, income tax bands and credits, Universal Social Charge (USC), PRSI Class S, preliminary tax (the 90% / 100% / 105% tests, see [Revenue: preliminary tax](https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/preliminary-tax.aspx)), the Pay and File deadline and the Revenue Online Service (ROS) extension, the late filing surcharge and interest.

Year labels: figures are for tax year 2026 (the calendar year 1 January to 31 December 2026) unless marked 2025. A dated section near the end covers the **2025 Form 11 being filed now**, due by 31 October 2026, or 18 November 2026 if paid and filed on ROS ([Revenue: filing your tax return](https://www.revenue.ie/en/self-assessment-and-self-employment/filing-your-tax-return/index.aspx)).

Related Guides:
- Forming the business, registering for tax (TR1, eRegistration) and choosing sole trader or company: **ie-formation**.
- Companies (CT1, Corporation Tax rates, company preliminary tax, close company surcharges): **ie-corporation-tax**.
- VAT registration thresholds, rates and VAT returns: **ireland-vat-return**.

Out of scope items are listed under When to refuse or refer.

## Ask the client first

- **Which year?** The return being filed now is for 2025; preliminary tax being paid now is for 2026. Get both years' figures.
- **Why are you a chargeable person?** You must register for self-assessment if taxable non-PAYE income exceeds €5,000 or gross non-PAYE income exceeds €30,000 ([Revenue: who should register](https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/register-it-self-assessment.aspx)). Self-employed people and proprietary directors (control of more than 15% of the ordinary share capital) file Form 11. Below those amounts a PAYE worker declares non-PAYE income on Form 12 through myAccount instead.
- **Personal status for the year:** single, married or in a civil partnership (jointly assessed, one or two incomes), widowed, or a single person with a qualifying child (Single Person Child Carer Credit). Age and date of birth (age tax credit, USC reduced rates, pension limits, PRSI age limits). Full medical card holder?
- **The business:** trade, start date, year end, VAT status, accounts or bank statements and invoices, asset register, car details (cost, date bought, CO2 emissions in g/km, business use %), home working arrangements.
- **Other income:** employment (PAYE), rent, deposit interest, dividends, foreign income, share options.
- **Payments already made:** preliminary tax paid for 2025 and the date; any direct debit for 2026 preliminary tax; tax, USC or PRSI deducted at source; RCT or PSWT credits.
- **Prior years:** the 2024 and 2025 final liabilities (needed for the 100% and 105% preliminary tax tests, [Revenue: preliminary tax](https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/preliminary-tax.aspx)), losses and unused capital allowances carried forward.
- **Compliance flags:** Local Property Tax up to date? Any late returns? Any Revenue contact, audit notification or unfiled years?
- **Pension contributions:** amounts paid to a Retirement Annuity Contract or PRSA and the date paid.
- **Large reliefs or high income?** If income is €125,000 or more and reliefs are large, the High Income Earner Restriction may apply ([Revenue: HIER](https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/hier.aspx); see When to refuse or refer).

If the client cannot answer the business-use questions, claim no business use for mixed items until they give a reasonable basis, and say so on the working paper.

## The method, step by step

1. **Confirm the year and the return.** A chargeable person files Form 11 through ROS; most individuals must file online ([Revenue: a guide to self-assessment](https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/index.aspx)).
2. **Build the trading account from the records.** Turnover is what the business earned in its accounting period, excluding VAT charged if the trader is VAT registered (VAT goes to the VAT return, see ireland-vat-return). Match platform payouts to invoices: turnover is the gross sale and the platform fee is a cost. Separate out non-trading receipts: salary (PAYE income), rent (rental income), deposit interest and dividends (other income), tax refunds and transfers between the client's own accounts (not income).
3. **Deduct allowable revenue costs.** A cost is deductible only if it is incurred wholly and exclusively for the trade and is revenue, not capital. Typical allowable costs: premises rent, business insurance, accountancy and legal fees, software, advertising, bank and card fees, training for the current trade, professional subscriptions, business travel, interest on business borrowings, and specific bad debts written off. Keep receipts and records for six years ([Revenue: Guide to completing 2025 returns](https://www.revenue.ie/en/self-assessment-and-self-employment/documents/guide-pay-file.pdf)).
4. **Add back what the trade cannot deduct.** Revenue's Form 11 adjustments list: the private element of motor expenses; political and charitable donations and non-staff entertainment; the private element of light, heat and phone; a loss on sale of fixed assets (and deduct a profit on sale) ([Revenue: Guide to completing 2025 returns](https://www.revenue.ie/en/self-assessment-and-self-employment/documents/guide-pay-file.pdf)). Also never deductible: income tax, USC and PRSI (including preliminary tax paid, which is a payment on account), fines, drawings, the capital part of loan repayments, depreciation, and general bad debt provisions.
   Practical points: VAT paid over to Revenue on a VAT return is not a business expense (**check** against the VAT treatment in ireland-vat-return); Department of Social Protection payments are generally taxable unless specifically exempt, and are subject to income tax but not USC or PRSI ([Revenue: taxation of DSP payments](https://www.revenue.ie/en/jobs-and-pensions/taxation-of-social-welfare-payments/index.aspx)); a home office is claimed as the floor-area share of a room used for the business, applied to heat, light and similar costs (**check**); where it is unclear whether a cost is capital or revenue, treat it as capital and claim capital allowances until the position is confirmed (**check**).
5. **Claim capital allowances instead of depreciation.** Plant and machinery (computers, furniture, equipment) and business cars get wear and tear at 12.5% a year over 8 years on the net cost after grants and reclaimable VAT; the asset must be in use at the end of the accounting year; a sale gives a balancing allowance or charge. Cars are limited by CO2 emissions (table below) and by the business-use share ([Revenue: Guide to completing 2025 returns](https://www.revenue.ie/en/self-assessment-and-self-employment/documents/guide-pay-file.pdf)). Accelerated allowances for energy-efficient equipment exist only in limited cases: **check** eligibility before claiming.
6. **Apply losses.** A current-year trading loss (which capital allowances can increase) may be set against other income of the same year (section 381). Unused losses carry forward against later profits of the same trade only (section 382). A trade carried on in a non-active capacity can set losses against other income only up to €31,750 ([Revenue: Guide to completing 2025 returns](https://www.revenue.ie/en/self-assessment-and-self-employment/documents/guide-pay-file.pdf)).
7. **Total income.** Adjusted trading profit, plus other income, less pension relief (Retirement Annuity Contract or PRSA premiums within the age-related limit and earnings cap) and other deductions.
8. **Income tax.** Apply the standard rate band at 20% and the balance at 40% for the person's status, then subtract tax credits. Credits reduce tax; they are not deductions from income ([Revenue: tax rates, bands and reliefs](https://www.revenue.ie/en/personal-tax-credits-reliefs-and-exemptions/tax-relief-charts/index.aspx)).
9. **USC.** Charged on total income after capital allowances but before pension contributions. If total income is €13,000 or less there is no USC; above that, all income is chargeable ([Revenue: USC overview](https://www.revenue.ie/en/jobs-and-pensions/usc/index.aspx)). Apply the bands, then the 3% surcharge if non-PAYE income exceeds €100,000.
10. **PRSI Class S.** On gross income after capital allowances, if income is €5,000 or more a year and the person is within the PRSI ages ([Revenue: do you need to pay PRSI?](https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/prsi-need-pay.aspx)). The minimum contribution applies once liable.
11. **Self-assess and settle.** Total liability less tax, USC and PRSI deducted at source and less preliminary tax paid gives the balance due or overpaid.
12. **Pay preliminary tax for the current year** by the same date (see Preliminary tax below).

### Where each item goes on the 2025 Form 11

The panels of the 2025 return are ([Revenue: Guide to completing 2025 returns](https://www.revenue.ie/en/self-assessment-and-self-employment/documents/guide-pay-file.pdf)):

| Panel | Content |
| --- | --- |
| A | Personal Details (status, proprietary director, medical card) |
| B | Self-Employed Income (trading account extract, adjustments, capital allowances, losses) |
| C | Irish Rental Income |
| D and E | PAYE / BIK / Pensions |
| F | Foreign Income |
| G | Irish Other Income (for example deposit interest, dividends) |
| H | Exempt Income |
| I | Charges and Deductions (Retirement Annuity Contract and PRSA premiums) |
| J | Personal Tax Credits |
| K | Restriction of Reliefs (High Income Earner Restriction) |
| L | Capital Gains |
| M, N, O | Chargeable Assets, Capital Acquisitions, Property Based Incentives |
| P | Self-Assessment |

Do not attach accounts or schedules: complete the extract from accounts panels and keep the working papers.

## Figures for 2026 (and 2025 where different)

### Income tax bands ([Revenue: tax rates, bands and reliefs](https://www.revenue.ie/en/personal-tax-credits-reliefs-and-exemptions/tax-relief-charts/index.aspx))

| Personal circumstances | 2026 | 2025 |
| --- | --- | --- |
| Single, widowed or surviving civil partner, without qualifying children | €44,000 @ 20%, balance @ 40% | same |
| Single, qualifying for Single Person Child Carer Credit | €48,000 @ 20%, balance @ 40% | same |
| Married or civil partners, one income | €53,000 @ 20%, balance @ 40% | same |
| Married or civil partners, both with income | €53,000 @ 20%, increased by up to €35,000, balance @ 40% | same |

The two-income increase is the lower of €35,000 or the income of the lower earner, and it cannot be transferred between spouses or civil partners ([Revenue: tax rates, bands and reliefs](https://www.revenue.ie/en/personal-tax-credits-reliefs-and-exemptions/tax-relief-charts/index.aspx)).

### Main tax credits ([Revenue: tax rates, bands and reliefs](https://www.revenue.ie/en/personal-tax-credits-reliefs-and-exemptions/tax-relief-charts/index.aspx))

| Credit | 2026 | 2025 |
| --- | --- | --- |
| Single Person | €2,000 | €2,000 |
| Married Person or Civil Partner | €4,000 | €4,000 |
| Single Person Child Carer Credit | €1,900 | €1,900 |
| Employee (PAYE) Tax Credit | €2,000 | €2,000 |
| Earned Income Tax Credit (maximum) | €2,000 | €2,000 |
| Home Carer's Tax Credit (maximum) | €1,950 | €1,950 |
| Age Tax Credit, single / married | €245 / €490 | €245 / €490 |

The Earned Income Credit is for self-employed earned income and pay of proprietary directors. It is the lower of €2,000 or 20% of qualifying earned income; it does not apply to rental or deposit interest income; where a person has both PAYE income and earned income, the Employee and Earned Income credits together cannot exceed the Employee Tax Credit maximum; and it cannot be transferred to a spouse ([Revenue: Earned Income Credit](https://www.revenue.ie/en/personal-tax-credits-reliefs-and-exemptions/income-and-employment/earned-income-credit/index.aspx)).

### USC ([Revenue: USC rates](https://www.revenue.ie/en/jobs-and-pensions/usc/standard-rates-thresholds.aspx))

| Band | 2026 | 2025 |
| --- | --- | --- |
| First €12,012 | 0.5% | 0.5% |
| Next band at 2% | next €16,688 (up to €28,700) | next €15,370 (up to €27,382) |
| Next band at 3% | next €41,344 (up to €70,044) | next €42,662 (up to €70,044) |
| Balance | 8% | 8% |

- **Exemption:** total income of €13,000 or less pays no USC; above that, all income is chargeable ([Revenue: USC overview](https://www.revenue.ie/en/jobs-and-pensions/usc/index.aspx)).
- **Reduced rates:** aged 70 or over, or holding a full medical card, with income of €60,000 or less: 0.5% on the first €12,012 and 2% on the balance, in 2026 and 2025 ([Revenue: reduced rates of USC](https://www.revenue.ie/en/jobs-and-pensions/usc/reduced-rates.aspx)).
- **Surcharge:** 3% extra if non-PAYE income is more than €100,000 a year ([Revenue: other rates of USC](https://www.revenue.ie/en/jobs-and-pensions/usc/other-rates.aspx)), so the top rate on that income is 11%. Revenue's examples apply the 3% to all income above €100,000, including PAYE income, once non-PAYE income is over €100,000 ([Revenue: Guide to completing 2025 returns](https://www.revenue.ie/en/self-assessment-and-self-employment/documents/guide-pay-file.pdf)).

### PRSI Class S

- **Who:** self-employed people aged 16 or over with income of €5,000 or more a year. The upper age limit moved from 66 to 70 from 1 January 2024, except for people already receiving the State Pension (Contributory) or aged 66 by 1 January 2024 ([Revenue: do you need to pay PRSI?](https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/prsi-need-pay.aspx)). Revenue's 2025 return guide still lists "over 66" as exempt: **check** the age position with the Department of Social Protection for anyone aged 66 to 69.
- **2025 rate:** 4.2% from 1 October 2025, and a blended 4.125% on 2025 annual income, with a minimum of €650 ([Revenue: Guide to completing 2025 returns](https://www.revenue.ie/en/self-assessment-and-self-employment/documents/guide-pay-file.pdf)).
- **2026 rate:** 4.2% until 30 September 2026 and 4.35% from 1 October 2026, minimum €650 a year. For self-assessed 2026 annual income the Department of Social Protection gives a blended rate of 4.2375% (the same method as the 2025 blended 4.125%) ([DSP: PRSI contribution rates SW 14, January 2026](https://assets.gov.ie/static/documents/cb168977/PRSI_C20260116_Contribution_Rates_and_User_Guide_-_SW_14_-_English_Version_-_January_2026_.pdf-web.pdf)). Confirm Revenue's own 2026 figure when it publishes the 2026 return guide.
- **Not payable** where total income before capital allowances and pension contributions is less than €5,000, or where a non-resident's self-assessed income is only unearned income such as deposit interest or rent ([Revenue: Guide to completing 2025 returns](https://www.revenue.ie/en/self-assessment-and-self-employment/documents/guide-pay-file.pdf)).

### Capital allowances ([Revenue: Guide to completing 2025 returns](https://www.revenue.ie/en/self-assessment-and-self-employment/documents/guide-pay-file.pdf))

| Asset | Allowance |
| --- | --- |
| Plant and machinery bought on or after 4 December 2002 | 12.5% a year over 8 years |
| Private cars bought on or after 4 December 2002 | 12.5% a year over 8 years, on the limited cost below, times the business-use share |
| Industrial buildings | 4% a year |

Cars bought on or after 1 January 2025, by CO2 emissions:

| CO2 (g/km) | Cost that qualifies |
| --- | --- |
| 0 to 120 (category A) | up to €24,000 |
| 121 to 155 (categories B and C) | 50% of €24,000, or 50% of the retail price when new if lower |
| 156 and above (categories D, E and F) | nil |

### Pension relief ([Revenue: Guide to completing 2025 returns](https://www.revenue.ie/en/self-assessment-and-self-employment/documents/guide-pay-file.pdf))

Relief for Retirement Annuity Contract and PRSA premiums is limited to a percentage of net relevant earnings by age: under 30, 15%; 30 to 39, 20%; 40 to 49, 25%; 50 to 54, 30%; 55 to 59, 35%; 60 and over, 40%. Earnings taken into account are capped at €115,000 for 2025 across all pension products. Unrelieved premiums carry forward. Confirm the 2026 cap before using it (**check**).

### Preliminary tax ([Revenue: what is preliminary tax?](https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/preliminary-tax.aspx))

Preliminary tax is the estimate of income tax, USC and PRSI for the current year, due by 31 October of that year (for 2026: 31 October 2026, or 18 November 2026 if paid with the 2025 return on ROS). To avoid interest it must be at least the lowest of:

- 90% of the tax due for the current year;
- 100% of the tax due for the immediately previous year; or
- 105% of the tax due for the pre-preceding year. This option applies only if preliminary tax is paid by direct debit, and not where the pre-preceding year's tax was nil.

Direct debit: payments are collected on the ninth day of the month (or the next working day) and can be set up on ROS ([Revenue: preliminary Income Tax direct debit](https://www.revenue.ie/en/starting-a-business/paying-your-tax/monthly-direct-debit/preliminary-income-tax.aspx)); you can join during the year as long as you make at least 3 equal monthly payments in that year ([Revenue: Tax and Duty Manual Part 41-00-28](https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-41/41-00-28.pdf)). In the second and subsequent years there must be 8 or more monthly direct debit payments ([Revenue: Tax and Duty Manual Part 41-00-28](https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-41/41-00-28.pdf)). If the arrangement lapses or falls short, the 105% test is lost for that year and interest can arise on any shortfall.

First year in self-assessment: because the previous year's self-assessed liability is normally nil, the 100% test usually means no preliminary tax is needed in the first year; the client may still pay 90% of the current year to reduce the bill the following year. The first year's balance is still due on 31 October of the following year, together with preliminary tax for the second year.

If preliminary tax is late or too low, the full liability is treated as due on the preliminary tax date (31 October of the tax year) and interest runs from then ([Revenue: Tax and Duty Manual Part 41-00-28](https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-41/41-00-28.pdf)).

### Surcharge and interest

| Item | Rule |
| --- | --- |
| Return filed late, within 2 months of the filing date (for the 2025 return: after 31 October 2026 and on or before 31 December 2026) | Surcharge of 5% of the tax due, capped at €12,695 ([Revenue](https://www.revenue.ie/en/self-assessment-and-self-employment/documents/guide-pay-file.pdf)) |
| Return filed more than 2 months late (after 31 December 2026 for the 2025 return) | Surcharge of 10% of the tax due, capped at €63,485 ([Revenue](https://www.revenue.ie/en/self-assessment-and-self-employment/documents/guide-pay-file.pdf)) |
| Local Property Tax return or payment outstanding when Form 11 is filed | A 10% surcharge may apply to the final liability even if Form 11 is on time ([Revenue](https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/pay-file-system.aspx)) |
| Late payment of income tax | Interest of 0.0219% a day, for each day or part of a day ([Revenue](https://www.revenue.ie/en/tax-professionals/tdm/collection/debt-management/guidelines-for-charging-interest-on-late-payment.pdf)) |

Sources: [Revenue: pay and file system](https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/pay-file-system.aspx); [Revenue: Guide to completing 2025 returns](https://www.revenue.ie/en/self-assessment-and-self-employment/documents/guide-pay-file.pdf); [Revenue: guidelines for charging interest on late payment](https://www.revenue.ie/en/tax-professionals/tdm/collection/debt-management/guidelines-for-charging-interest-on-late-payment.pdf).

The surcharge is a percentage of the total tax payable for the year of the late return, not just the balance still unpaid. The ROS extension is conditional: if the client files on ROS but pays another way (or pays on ROS but files on paper), the deadline stays 31 October ([Revenue eBrief No. 034/26](https://www.revenue.ie/en/tax-professionals/ebrief/2026/no-0342026.aspx)).

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| PAYE worker with small side income | Chargeable person only if taxable non-PAYE income exceeds €5,000 or gross non-PAYE income exceeds €30,000; otherwise Form 12 ([Revenue](https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/register-it-self-assessment.aspx)) |
| Director owning or controlling more than 15% | Proprietary director: chargeable person, files Form 11 even if all pay is under PAYE; gets the Earned Income Credit, not the Employee credit, on that pay ([Revenue](https://www.revenue.ie/en/self-assessment-and-self-employment/documents/guide-pay-file.pdf)) |
| Total income exactly €13,000 | No USC (exempt if €13,000 or less) ([Revenue](https://www.revenue.ie/en/jobs-and-pensions/usc/index.aspx)) |
| Aged 70+ or full medical card, income €60,000 or less | USC reduced rates; above €60,000, standard rates ([Revenue](https://www.revenue.ie/en/jobs-and-pensions/usc/reduced-rates.aspx)) |
| Non-PAYE income exactly €100,000 | No USC surcharge (it applies only if more than €100,000) ([Revenue](https://www.revenue.ie/en/jobs-and-pensions/usc/other-rates.aspx)) |
| Self-employed income under €5,000 | No Class S PRSI ([Revenue](https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/prsi-need-pay.aspx)) |
| Earned income below €10,000 (2026) | Earned Income Credit is 20% of that income, not €2,000 ([Revenue](https://www.revenue.ie/en/personal-tax-credits-reliefs-and-exemptions/income-and-employment/earned-income-credit/index.aspx)) |
| Spouse with lower income of €20,000 | Band increase is €20,000, not €35,000; the unused part cannot pass to the other spouse ([Revenue](https://www.revenue.ie/en/personal-tax-credits-reliefs-and-exemptions/tax-relief-charts/index.aspx)) |
| Car with CO2 above 155 g/km bought in 2025 or 2026 | No capital allowances ([Revenue](https://www.revenue.ie/en/self-assessment-and-self-employment/documents/guide-pay-file.pdf)) |
| Client entertainment | Add back; the Form 11 add-back is for non-staff entertainment |
| Paper return filed early | If filed by 31 August 2026, Revenue calculates the tax. Revenue has extended this to 30 September by concession each year since 2015 and announces it yearly, so do not rely on it until announced; later paper filers must self-assess ([Revenue](https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-41/41-00-28.pdf)) |
| New trader | May file the first and second year returns by the second year's return date; payment dates do not move ([Revenue](https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-41/41-00-28.pdf)) |
| Pre-preceding year's tax was nil | The 105% direct debit test cannot be used ([Revenue](https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/preliminary-tax.aspx)) |
| Deposit interest | Not trading income; taxed with DIRT (33% maximum liability) and exempt from USC ([Revenue](https://www.revenue.ie/en/personal-tax-credits-reliefs-and-exemptions/tax-relief-charts/index.aspx); [Revenue](https://www.revenue.ie/en/self-assessment-and-self-employment/documents/guide-pay-file.pdf)) |

## Worked cases

All cases are illustrations with assumed facts; recompute with the client's own figures.

### Case 1: Siobhán, single sole trader, 2026 estimate ([Revenue: tax rates, bands and reliefs](https://www.revenue.ie/en/personal-tax-credits-reliefs-and-exemptions/tax-relief-charts/index.aspx))

Siobhán, single with no children, aged 38, is a graphic designer. For 2026 she expects turnover of €90,000, allowable costs of €27,250 after add-backs, and capital allowances of €2,750 (Case 4), so adjusted profit of €60,000. No other income.

- Income tax: €44,000 at 20% = €8,800; €16,000 at 40% = €6,400; gross €15,200; less Single Person credit €2,000 and Earned Income Credit €2,000 = **€11,200**.
- USC 2026 ([Revenue: USC rates](https://www.revenue.ie/en/jobs-and-pensions/usc/standard-rates-thresholds.aspx)): €12,012 at 0.5% = €60.06; €16,688 at 2% = €333.76; €31,300 at 3% (€60,000 less €28,700) = €939; total **€1,332.82**. No surcharge (non-PAYE income not over €100,000).
- PRSI Class S at the 2026 blended rate: €60,000 x 4.2375% = **€2,542.50** ([DSP: SW 14](https://assets.gov.ie/static/documents/cb168977/PRSI_C20260116_Contribution_Rates_and_User_Guide_-_SW_14_-_English_Version_-_January_2026_.pdf-web.pdf); confirm Revenue's figure).
- Estimated 2026 liability: **€15,075.32**.

### Case 2: married couple, two incomes, 2026 ([Revenue: tax rates, bands and reliefs](https://www.revenue.ie/en/personal-tax-credits-reliefs-and-exemptions/tax-relief-charts/index.aspx))

Aidan (sole trader, adjusted profit €72,000) and Niamh (employee, salary €20,000) are jointly assessed.

- Standard rate band: €53,000 plus the lower of €35,000 or Niamh's €20,000, so €73,000; the increase can be used only against Niamh's income, which it fully covers.
- Tax: €73,000 at 20% = €14,600; the balance of €19,000 (all Aidan's) at 40% = €7,600; gross €22,200.
- Credits: Married Person €4,000, Employee credit €2,000 (Niamh), Earned Income Credit €2,000 (Aidan) = €8,000. Income tax **€14,200**, less PAYE deducted from Niamh's salary.
- USC is computed for each spouse separately. Aidan 2026: €60.06 + €333.76 + €1,240.32 (€41,344 at 3%) + €156.48 (€1,956 at 8%) = **€1,790.62** ([Revenue: USC rates](https://www.revenue.ie/en/jobs-and-pensions/usc/standard-rates-thresholds.aspx)).
- Aidan's Class S at the 2026 blended 4.2375%: €72,000 x 4.2375% = €3,051 ([DSP: SW 14](https://assets.gov.ie/static/documents/cb168977/PRSI_C20260116_Contribution_Rates_and_User_Guide_-_SW_14_-_English_Version_-_January_2026_.pdf-web.pdf)).

### Case 3: USC surcharge, 2026 ([Revenue: other rates of USC](https://www.revenue.ie/en/jobs-and-pensions/usc/other-rates.aspx))

A consultant has trading profit of €130,000 and no PAYE income. USC: €60.06 + €333.76 + €1,240.32 + €4,796.48 (€59,956 at 8%) = €6,430.62, plus the 3% surcharge on €30,000 above €100,000 = €900; total **€7,330.62**.

### Case 4: a business car bought in 2026 ([Revenue: Guide to completing 2025 returns](https://www.revenue.ie/en/self-assessment-and-self-employment/documents/guide-pay-file.pdf))

Siobhán buys a car for €40,000 in March 2026 and uses it 75% for business (mileage log kept). The finance repayments are not the cost; the purchase price is.

- CO2 110 g/km (category A): qualifying cost €24,000; allowance €24,000 x 12.5% = €3,000 a year; business share 75% = **€2,250**. With €500 on a laptop and desk (€4,000 x 12.5%), her 2026 capital allowances are €2,750.
- If the car emitted 150 g/km (category C): qualifying cost is 50% of €24,000 = €12,000 (lower than 50% of a €40,000 retail price, €20,000); allowance €1,500; business share **€1,125**.
- If it emitted 170 g/km (category D): **nil**.
- Running costs (fuel, insurance, repairs) are deductible at the business share only; add back the private 25%.

### Case 5: the 2025 return and 2026 preliminary tax, due 18 November 2026 on ROS ([Revenue: what is preliminary tax?](https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/preliminary-tax.aspx))

Siobhán's 2025 adjusted profit was €52,000, and she paid €10,000 preliminary tax for 2025.

- 2025 income tax: €44,000 at 20% = €8,800; €8,000 at 40% = €3,200; gross €12,000 less credits €4,000 = **€8,000** ([Revenue: tax rates, bands and reliefs](https://www.revenue.ie/en/personal-tax-credits-reliefs-and-exemptions/tax-relief-charts/index.aspx)).
- 2025 USC: €60.06 + €307.40 (€15,370 at 2%) + €738.54 (€24,618 at 3%) = **€1,106.00** ([Revenue: USC rates](https://www.revenue.ie/en/jobs-and-pensions/usc/standard-rates-thresholds.aspx)).
- 2025 PRSI: €52,000 x 4.125% = **€2,145** ([Revenue: Guide to completing 2025 returns](https://www.revenue.ie/en/self-assessment-and-self-employment/documents/guide-pay-file.pdf)).
- 2025 total €11,251; less €10,000 paid = balance **€1,251**.
- 2026 preliminary tax: 100% of 2025 = €11,251; 90% of the 2026 estimate (Case 1) = €13,567.79; she has no direct debit, so the 105% test is not available. Pay the lower, **€11,251**.
- Paying and filing on ROS by 18 November 2026: €1,251 + €11,251 = **€12,502**. If she had joined the direct debit scheme early in 2026 and her 2024 liability had been €8,000, 105% of that, €8,400, would have been enough.

### Case 6: filing late ([Revenue: pay and file system](https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/pay-file-system.aspx))

Same facts, but Siobhán files the 2025 return on 10 December 2026 (the ROS extension to 18 November 2026 needs both filing and paying on ROS by that date, so it does not help her). The return is late but within 2 months of 31 October, so the surcharge is 5% of €11,251 = **€562.55** (under the €12,695 cap). Filed on 15 January 2027 it would be 10% = **€1,125.10**. If the €1,251 balance was also paid 30 days after 31 October, interest is €1,251 x 0.0219% x 30 = about **€8.22** ([Revenue: interest on late payment](https://www.revenue.ie/en/tax-professionals/tdm/collection/debt-management/guidelines-for-charging-interest-on-late-payment.pdf)).

## When to refuse or refer

- **A company** (LTD, DAC, PLC): the company files a CT1, not Form 11. Use ie-corporation-tax. A proprietary director still files their own Form 11 for their salary and other income.
- **Partnership accounts:** the partnership computes profits on Form 1 (Firms); each partner then reports their share on Form 11. This Guide covers only the partner's own return.
- **Non-resident, newly arrived or departing individuals, split-year or dual residence, foreign income with foreign tax credits:** refer.
- **Capital Gains Tax** computations for the CGT panel, share options and employee share schemes: refer or use a CGT Guide. CGT has different payment dates.
- **High Income Earner Restriction:** may apply where income is €125,000 or more (less with ring-fenced income), specified reliefs exceed €80,000 and exceed 20% of adjusted income; it needs Form RR1 through ROS ([Revenue: HIER](https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/hier.aspx)). Refer.
- **Property-based incentive reliefs, farming reliefs, Section 23 relief** (with its 5% USC property relief surcharge where gross income is €100,000 or more ([Revenue: other rates of USC](https://www.revenue.ie/en/jobs-and-pensions/usc/other-rates.aspx))): refer.
- **Revenue audit, aspect query, unfiled earlier years or a disclosure:** refer to a practitioner before filing anything.

## Filing and payment

- **Pay and File:** by 31 October each year you pay preliminary tax for that year, file the previous year's return with a self-assessment and pay the balance for the previous year; paying and filing on ROS extends 31 October to 18 November ([Revenue: pay and file system](https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/pay-file-system.aspx)). Check each year's ROS date in Revenue's announcement.
- **How to file:** ROS Form 11 (or, if everything fits, Form 11S). Tick at least one reason for filing in the Personal Details panel. Complete the IT Self-Assessment panel and the Statement of Net Liabilities ([Revenue: filing your tax return](https://www.revenue.ie/en/self-assessment-and-self-employment/filing-your-tax-return/index.aspx)).
- **How to pay:** on ROS by ROS Debit Instruction or debit or credit card (Visa and Mastercard only); on myAccount by Single Debit Instruction or card; or by monthly direct debit for preliminary tax ([Revenue: what is preliminary tax?](https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/preliminary-tax.aspx)).
- **Amending:** correct a ROS return through ROS; for a paper return, write to Revenue ([Revenue: pay and file system](https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/pay-file-system.aspx)).
- **Records:** keep supporting documents for six years; do not send them with the return unless asked.

### Dated: the 2025 Form 11 being filed now

- The Pay and File deadline for the 2025 Form 11 is Saturday 31 October 2026. Filing and paying through ROS (the 2025 balance and 2026 preliminary tax) extends it to Wednesday 18 November 2026; if only one of the two is done through ROS, the deadline stays 31 October 2026 ([Revenue eBrief No. 034/26](https://www.revenue.ie/en/tax-professionals/ebrief/2026/no-0342026.aspx)).
- 2025 figures: bands and credits the same as 2026; USC first €12,012 at 0.5%, next €15,370 at 2%, next €42,662 at 3%, balance at 8% ([Revenue: USC rates](https://www.revenue.ie/en/jobs-and-pensions/usc/standard-rates-thresholds.aspx)); Class S blended 4.125% with a €650 minimum; pension earnings cap €115,000 ([Revenue: Guide to completing 2025 returns](https://www.revenue.ie/en/self-assessment-and-self-employment/documents/guide-pay-file.pdf)).
- Late 2025 returns: 5% surcharge (cap €12,695) if filed after 31 October 2026 and on or before 31 December 2026; 10% (cap €63,485) after 31 December 2026 ([Revenue: Guide to completing 2025 returns](https://www.revenue.ie/en/self-assessment-and-self-employment/documents/guide-pay-file.pdf)).
- The early paper-filer date (Revenue calculates the tax) was 31 August 2026; Revenue's yearly concession extended it to 30 September 2026, so it has passed ([Revenue: Tax and Duty Manual Part 41-00-28](https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-41/41-00-28.pdf)).

## Completion checklist

- [ ] Year confirmed: 2025 return and 2026 preliminary tax; the client's reason for being a chargeable person recorded.
- [ ] Status, age, medical card and joint or single assessment confirmed; band and credits match the status.
- [ ] Turnover excludes VAT (if registered) and non-trading receipts; platform payouts matched to invoices.
- [ ] Add-backs made: private motor, light, heat and phone; donations; non-staff entertainment; depreciation; tax payments; drawings; loan principal.
- [ ] Capital allowances on net cost at 12.5% over 8 years; car cost limited by CO2 category and business share; disposals give a balancing allowance or charge ([Revenue](https://www.revenue.ie/en/self-assessment-and-self-employment/documents/guide-pay-file.pdf)).
- [ ] Losses: current year (s.381) or carried forward (s.382) applied to the right income.
- [ ] Pension relief within the age percentage and earnings cap.
- [ ] Income tax, USC (with surcharge if non-PAYE income over €100,000) and Class S PRSI computed for the right year's rates: 2025 blended 4.125%, 2026 blended 4.2375% (4.2% to 30 September, 4.35% from 1 October 2026), minimum €650 ([DSP: SW 14](https://assets.gov.ie/static/documents/cb168977/PRSI_C20260116_Contribution_Rates_and_User_Guide_-_SW_14_-_English_Version_-_January_2026_.pdf-web.pdf)).
- [ ] Credits for tax, USC and PRSI deducted at source and preliminary tax paid.
- [ ] 2026 preliminary tax at least the lowest of 90% / 100% / 105% (direct debit only), with the working kept ([Revenue](https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/preliminary-tax.aspx)).
- [ ] Filed and paid on ROS by 18 November 2026, or both by 31 October 2026 otherwise; LPT up to date.
- [ ] Records kept for six years; refer-out items listed for the client.

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
