---
name: be-employee-income-tax
description: "Belgian personal income tax (personenbelasting / impot des personnes physiques) for employees and pensioners who are Belgian residents, for income 2026 (assessment year 2027). Covers the art. 130 scale (25%, 40%, 45%, 50%), the tax-free amount of EUR 11,550 and its supplements for children and dependants, the 30% lump sum for employee expenses capped at EUR 6,070 versus actual costs, the fiscal work bonus, the pension and replacement income reduction, the main federal reductions (pension savings, long-term savings, gifts, childcare), the municipal surcharge, joint assessment and the marital quotient, the credit for payroll withholding (bedrijfsvoorheffing), the refund or balance, Tax-on-web filing, the simplified proposal, tax increases and late interest. Trigger on: Belgian tax return employee, aangifte personenbelasting, Tax-on-web, belastingvrije som, forfaitaire beroepskosten, huwelijksquotient, bedrijfsvoorheffing refund, voorstel vereenvoudigde aangifte, gemeentebelasting. Out of scope: be-income-tax (self-employed), belgium-payroll, be-capital-gains, be-cross-border, be-social-contributions, belgium-crypto-tax."
jurisdiction: BE
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-23
version: 0.1
verified_by: pending
---

# Belgium: income tax for employees and pensioners (income 2026, assessment year 2027)

> **General reference only.** This skill is general tax reference material for AI-assisted work. It has not been reviewed for any person's facts. Do not rely on it to file, pay or take a tax position without review by a qualified professional in Belgium.

This skill computes the annual personal income tax of a Belgian resident whose income is pay from employment or a pension. It links to the other Belgian skills instead of repeating them:

- Self-employed profits and their costs: `be-income-tax`
- Monthly payroll withholding and employer and employee social security: `belgium-payroll`
- Capital gains on financial assets (the 10% tax from 2026): `be-capital-gains`
- Residence, the inbound regime, non-residents and exit tax: `be-cross-border`
- Self-employed social contributions: `be-social-contributions`

## Who this applies to

- **Belgian residents** (home or seat of wealth in Belgium; see `be-cross-border` for the test) taxed on worldwide income in the personenbelasting.
- **Employees** (pay under art. 30, 1° WIB 92), including those with a company car or other benefits in kind, which the employer reports on the pay slip form 281.10.
- **Pensioners and people on replacement income** (unemployment, sickness and invalidity benefits), who get the reduction of art. 147 instead of a cost lump sum.
- **Married couples and legal cohabitants**, who file one joint return (art. 126, §1). Each partner's taxable income is still computed separately.

Out: company directors (3% lump sum, see `be-income-tax` and `be-corporate-tax`), the self-employed, and non-residents (belasting niet-inwoners, see `be-cross-border`).

Income year 2026 is assessment year 2027. All figures below are the indexed amounts for income 2026 as printed in Fisconetplus. Several were changed by the law of 15 July 2026 (Belgian Official Gazette 29 July 2026), which applies from assessment year 2027.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Tax scale | 25% to EUR 16,720; 40% from EUR 16,720 to EUR 29,510; 45% from EUR 29,510 to EUR 51,070; 50% above EUR 51,070. Applied to each spouse separately in a joint assessment | Income 2026 | [Art. 130 WIB 92](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/796a4fc5-340e-4c89-a72a-88caa804ca96) |
| Tax-free amount, basic | EUR 11,550 per taxpayer; plus EUR 2,030 if the taxpayer is disabled | Income 2026 (law of 15 July 2026) | [Art. 131 WIB 92](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/f3c5d665-cac4-4cbd-b714-bd287f791751) |
| Supplements for dependent children (total, not per child) | 1 child EUR 2,130; 2 children EUR 5,130; 3 children EUR 11,440; 4 children EUR 18,510; each child above four EUR 7,070 more. Extra EUR 740 per child under 3 on 1 January 2027 (not combined with the childcare reduction). A disabled child counts as two | Income 2026 | [Art. 132 WIB 92](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/caa866c3-8820-4ba4-b5bc-f64ae0cd2869) |
| Other dependants | EUR 5,950 for a dependant aged 66 or over in need of care; EUR 1,980 for any other dependant | Income 2026 | [Art. 132 WIB 92](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/caa866c3-8820-4ba4-b5bc-f64ae0cd2869) |
| Single parent supplement | EUR 1,980; plus up to EUR 1,290 more when taxable income is under EUR 24,990 (full below EUR 19,720, tapering between) | Income 2026 | [Art. 133 WIB 92](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/0f863e7a-b131-494b-8617-7b62efed5e75) |
| Tax on the tax-free amount (deducted from the scale tax) | 25% up to EUR 11,750; 30% from EUR 11,750 to EUR 16,720; 40% to EUR 27,860; 45% to EUR 51,070; 50% above | Income 2026 | [Art. 134, §2 WIB 92](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/20a503a9-4213-4e60-a91c-0ebb907e176a) |
| Refundable child credit | Unused tax on the child supplements becomes a refundable credit, up to EUR 550 per dependent child (not indexed) | Income 2026 | [Art. 134, §3 WIB 92](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/20a503a9-4213-4e60-a91c-0ebb907e176a) |
| Lump-sum professional expenses, employees | 30% of gross taxable pay after employee social security, capped at EUR 6,070 | Income 2026 | [Art. 51 WIB 92](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/e2fb1778-ac33-4e91-8e57-e53c0cac384c) |
| Employee social security (deducted before tax) | 13.07% of gross pay (pensions 7.50, health care 3.55, benefits 1.15, unemployment 0.87) | 2026 | [RSZ administrative instructions 2026/3](https://www.socialsecurity.be/employer/instructions/dmfa/nl/latest/instructions/socialsecuritycontributions/contributions.html) |
| Marital quotient | 30% of the earning spouse's net professional income is moved to a spouse with none, capped at EUR 11,780 (EUR 12,790 if both are 66 or over on 1 January 2027). If the other spouse earns less than 30% of the total, a top-up to 30% within the same cap | Income 2026 (law of 15 July 2026) | [Art. 87](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/9f17497c-c0f6-415e-b715-81f9aeca6765) and [art. 88 WIB 92](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/0a136e8c-9144-4e7e-b596-0aede2c66c3e) |
| Fiscal work bonus (low pay) | Credit of 33.14% of part A and 63% of part B of the social security work bonus actually granted; at most EUR 2,000 a year | Income 2026 | [Art. 289ter/1 WIB 92](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/5403364d-120e-4c43-8945-ac770f1228f6) |
| Pension and replacement income reduction | Pensions only: EUR 2,182.06 basic plus EUR 467.87 additional; sickness and invalidity benefits only: EUR 2,959.25; unemployment only: EUR 545.51; pro rata when mixed with other income | Income 2026 | [Art. 147 WIB 92](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/29f2d0bb-6658-4cf8-b870-283c99274b07) |
| Income limit on that reduction | Unemployment reduction lost from EUR 29,190 taxable income (tapers from EUR 21,810); other replacement income reductions cut to one third from EUR 58,980 (tapers from EUR 29,490) | Income 2026 | [Art. 151](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/9609a0ab-0649-4095-8977-ec48c21a0bdf) and [art. 152 WIB 92](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/5f0ded05-81ef-42c3-9fd4-03cc0b912b24) |
| Pension savings | 30% reduction on up to EUR 1,050; or, by an irrevocable choice told to the provider, 25% on up to EUR 1,350 | Income 2026 | [Art. 145/8](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/d811dab7-9607-417e-ba02-1c25e129bb8a) and [art. 145/2 WIB 92](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/bbab9898-8738-4184-9278-187768359a3b) |
| Long-term savings (individual life insurance, capital repayments on a loan for a home other than your own, taken out by 31 December 2023) | 30% reduction; payments capped at 15% of the first EUR 2,040 of professional income plus 6% of the rest, at most EUR 2,450 | Income 2026 | [Art. 145/1, 145/2](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/c06c831e-30de-44e2-af79-c380a0798b1c) and [art. 145/6 WIB 92](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/f3ed8f21-ac56-4810-aeb6-f648afbb7f35) |
| Employer shares bought as an employee | 30% reduction on up to EUR 820; not in the same year as pension savings | Income 2026 | [Art. 145/7 WIB 92](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/5c2814b9-851f-4581-86c7-72de251575ab) |
| Gifts to approved institutions | 30% reduction; at least EUR 40 per institution per year with an attestation; capped at 10% of total net income and EUR 408,130 | Income 2026 | [Art. 145/33 WIB 92](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/bd3c241f-c535-42fd-b3d1-8501e3a5907a) |
| Childcare | 45% reduction on costs up to EUR 17.30 per day per child under 14 (under 21 if severely disabled), paid to approved providers | Income 2026 | [Art. 145/35 WIB 92](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/496c7428-bd55-4d78-bfc5-c3526c941973) |
| Service vouchers and PWA cheques | Regional reduction: the federal text sets a 30% rate on a base of EUR 920, but the indexed amounts are in each region's version (Flanders, Wallonia, Brussels) | Income 2026 | [Art. 145/21 WIB 92](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/02c01cea-4780-47b4-967b-ede4c1be0fb1) |
| Energy-saving expenses in a home | Federal reduction repealed from assessment year 2026 (law of 18 December 2025) | From income 2025 | [Art. 145/24 WIB 92](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/db43c0d6-c890-4985-8777-23c352281951) |
| Municipal surcharge | Rate set by each municipality, one decimal; charged on the total tax. Withholding and prepayments collect it as if it were 6.7% | Income 2026 | [Art. 466](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/81bf3101-a837-4d89-8b97-713e080f00ac), [art. 468](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/4d803548-89eb-4ef5-b1a5-12f5751e1313) and [art. 469 WIB 92](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/2f544d3e-e76c-499d-855e-e9c58fe0e6a7) |
| Late payment interest | 4% a year for calendar years 2026 and 2027 | 2026, 2027 | [Law of 5 May 1865, art. 2, §2/1](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/da7e0caf-3428-43aa-ab80-30410a15beca); [art. 414 WIB 92](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/db296af5-75b3-49bc-95e2-a35bb742fed5) |
| Tax increase | 10% to 200% of the tax on undeclared or late income; none for a first offence in good faith, presumed | Income 2026 | [Art. 444 WIB 92](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/5095859f-8ffb-42f9-b535-3197a7c3dbe0) |

## The taxable base

Work through the return in this order.

1. **Gross taxable pay.** Pay, bonuses, holiday pay and benefits in kind as shown on form 281.10. The employer's payroll is in `belgium-payroll`.
2. **Less employee social security.** 13.07% of gross pay, minus any social security work bonus (art. 52, 7° and art. 51 WIB 92 treat these contributions as deducted before the lump sum).
3. **Less professional expenses.** Either the lump sum of 30% of step 2, capped at EUR 6,070, or the actual costs if you can prove them (art. 51, first paragraph: the lump sum applies "bij gebrek aan bewijzen", for lack of proof). One method for all your pay. Actual costs make sense when commuting, a home office or training costs beat EUR 6,070; keep the evidence. Pensions and replacement income get no lump sum.
4. **Net professional income.** For a couple, apply the marital quotient here (art. 87 and 88) when one partner earns nothing or less than 30% of the couple's total. It is skipped if it would raise the couple's tax.
5. **Add other income.** Rental income from Belgian property (cadastral income), taxable investment income you chose to declare, and miscellaneous income. Capital gains on financial assets have their own rules in `be-capital-gains`.
6. **Taxable income.** Apply the scale of art. 130 to each partner's own taxable income.
7. **Less tax on the tax-free amount** (art. 134). Work out the tax-free amount (EUR 11,550 plus supplements) and tax it on the art. 134 scale. Deduct that tax from step 6. In a joint return, the child supplements go to the partner with the higher income; unused tax-free amount of one partner can move to the other.
8. **Less reductions.** The pension and replacement income reduction (art. 147, with the income limits in art. 151 and 152), then the federal reductions for savings, gifts and childcare, and any regional reductions. For a home loan, regional rules apply, and each region sets its own; name the region and use its rules.
9. **Regional split.** The basic tax is shared between the federal state and the region (Flanders, Wallonia or Brussels-Capital), which levies its own surcharge. The regional rate for income 2026 is under "Not yet confirmed" below. The worked examples below assume the regional surcharge exactly offsets the federal autonomy cut.
10. **Municipal surcharge.** Multiply the total tax by the municipality's rate (art. 466 and 468). It does not apply to tax on non-professional dividends and interest or on capital gains taxed under art. 90, 9° (art. 466, second paragraph).
11. **Credits.** Deduct the payroll withholding (bedrijfsvoorheffing) actually withheld (art. 296), the fiscal work bonus (art. 289ter/1) and the refundable child credit (art. 134, §3).
12. **Refund or balance.** A surplus of credits and withholding is set off against the municipal surcharge and refunded if at least EUR 2.50 (art. 304, §2). A balance due under EUR 2.50 is not collected (art. 304, §1).

**Pensioners.** Statutory pensions and pensions from the second pillar are taxed on the scale. The reduction of art. 147 brings the tax on a small pension down; in full it applies only when the net income consists only of pensions. Lump sums from group insurance and similar can be taxed separately at fixed rates (art. 171); check the payer's form 281.11.

## Deadlines and filing

| What | When | Source |
|---|---|---|
| Paper return | By 30 June 2027 for income 2026, and at least one month after the form is sent | [Art. 308, §1 WIB 92](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/182821e5-122a-4948-867e-297c16371fe1) |
| Electronic return in Tax-on-web (MyMinfin) | By 15 July 2027 for income 2026, and at least one month after the electronic return is made available | [Art. 308, §1 WIB 92](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/182821e5-122a-4948-867e-297c16371fe1) |
| Electronic return with foreign professional income, or with self-employed or director income | By 16 October 2027, and at least five months after the electronic return is available | [Art. 308/1 WIB 92](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/51c63576-3d3c-49cd-bf84-e5c6e20022ad) |
| No form received | Ask the tax office for one by 15 June 2027, unless you used Tax-on-web last year or receive a simplified proposal | [Art. 308, §3 WIB 92](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/182821e5-122a-4948-867e-297c16371fe1) |
| Simplified proposal (voorstel van vereenvoudigde aangifte) | Sent to taxpayers exempted from filing. It shows the base and the tax. If it is wrong or incomplete, tell the administration within one month of it being sent; otherwise it counts as your return, and an uncorrected error counts as a wrong return | [Art. 306 WIB 92](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/4e0c82f4-176b-4e40-a97e-7be85954d7f0) |
| Paying a balance | Within two months of the assessment notice being sent | [Art. 413 WIB 92](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/09b8ca93-c681-40df-9a8f-c5a947e063ae) |

The exact Tax-on-web opening and closing dates for income 2026 are not yet published; see "Not yet confirmed". The legal end dates above apply unless the form gives a later date.

## Penalties and interest

- **Tax increase (art. 444 WIB 92).** Not filing, filing late, or filing an incomplete or wrong return adds 10% to 200% of the tax on the undeclared or late part of income, on a scale set by royal decree. No increase is charged for a first offence in good faith. Since the programme law of 18 July 2025 (for assessments made from 29 July 2025), good faith is presumed for a first offence unless the administration proves otherwise. The increase applies only if the undeclared or late income reaches EUR 2,500, and tax plus increase cannot exceed that income. ([Art. 444 WIB 92](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/5095859f-8ffb-42f9-b535-3197a7c3dbe0))
- **Administrative fine (art. 445 WIB 92).** EUR 50 to EUR 1,250 per breach, on a scale set by royal decree. ([Art. 445 WIB 92](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/f9f2e45e-5e3b-4642-a5e3-31ad4ca7f25f))
- **Late payment interest (art. 414 WIB 92).** 4% a year for 2026 and 2027, charged per calendar month on the unpaid tax rounded down to a multiple of EUR 10, from the first day of the month after the due date. Not charged when under EUR 5 a month.
- **Wrong simplified proposal.** If you do not correct an inaccurate or incomplete proposal within one month, it is treated as an incomplete or wrong return (art. 306, §4), so art. 444 can apply.

## Cross-border points

- **Foreign pay exempt by a treaty.** It is exempt with progression, and the municipal surcharge is still charged on the tax as if the pay were Belgian, where the treaty allows (art. 466bis). Such a return gets the later filing date of art. 308/1. See `be-cross-border`.
- **Joint return with a partner who has treaty-exempt pay above EUR 11,550.** The couple is taxed separately (art. 126, §2, 4°).
- **Arriving or leaving during 2026.** Resident status, the inbound regime for recruited staff (35% cost allowance) and the non-resident return are in `be-cross-border`.
- **Frontier workers and social security.** Which country's social security applies changes the 13.07% deduction; see `belgium-payroll` and `be-cross-border`.

## Worked examples

### Example 1: single employee, gross pay EUR 50,000

Facts: a single resident employee, no children, gross pay EUR 50,000 in 2026, no other income, no reductions, uses the lump sum. The municipality's rate is assumed to be 7%. The employer withheld EUR 10,900 in payroll withholding (an input from form 281.10). The regional surcharge is assumed to offset the federal autonomy cut exactly.

1. Employee social security: 13.07% x 50,000 = EUR 6,535.
2. Taxable pay: 50,000 - 6,535 = EUR 43,465.
3. Lump sum: 30% x 43,465 = EUR 13,039.50, capped at EUR 6,070.
4. Taxable income: 43,465 - 6,070 = EUR 37,395.
5. Scale tax: 25% x 16,720 = 4,180; 40% x (29,510 - 16,720) = 5,116; 45% x (37,395 - 29,510) = 3,548.25. Total EUR 12,844.25.
6. Tax on the tax-free amount: 25% x 11,550 = EUR 2,887.50 (all within the first EUR 11,750 band of art. 134).
7. Tax after the tax-free amount: 12,844.25 - 2,887.50 = EUR 9,956.75.
8. Municipal surcharge at 7%: EUR 696.97.
9. Total: EUR 10,653.72. Withholding EUR 10,900, so the refund is EUR 246.28.

```oa-check
name: Single employee, gross pay EUR 50,000, income 2026
inputs:
  gross: 50000
  employee_ss_rate: 0.1307
  lump_rate: 0.30
  lump_cap: 6070
  tax_free: 11550
  municipal_rate: 0.07
  withholding: 10900
steps:
  - employee_ss: gross * employee_ss_rate
  - taxable_pay: gross - employee_ss
  - lump_sum: min(taxable_pay * lump_rate, lump_cap)
  - taxable_income: taxable_pay - lump_sum
  - band_25: min(taxable_income, 16720) * 0.25
  - band_40: (min(taxable_income, 29510) - 16720) * 0.40
  - band_45: (min(taxable_income, 51070) - 29510) * 0.45
  - band_50: max(taxable_income - 51070, 0) * 0.50
  - scale_tax: band_25 + band_40 + band_45 + band_50
  - tax_on_tax_free: min(tax_free, 11750) * 0.25
  - tax_after_tax_free: scale_tax - tax_on_tax_free
  - municipal: round(tax_after_tax_free * municipal_rate, 2)
  - total_tax: tax_after_tax_free + municipal
  - refund: withholding - total_tax
expected:
  employee_ss: 6535
  taxable_pay: 43465
  lump_sum: 6070
  taxable_income: 37395
  scale_tax: 12844.25
  tax_on_tax_free: 2887.50
  tax_after_tax_free: 9956.75
  municipal: 696.97
  total_tax: 10653.72
  refund: 246.28
```

### Example 2: married couple, one earner, marital quotient

Facts: a married resident couple, both under 66, no children. One partner earns gross pay of EUR 80,000 in 2026; the other has no income. Lump sum, no reductions. Municipal rate assumed 7%. Withholding EUR 17,000 (an input). Same regional assumption as Example 1.

1. Employee social security: 13.07% x 80,000 = EUR 10,456. Taxable pay EUR 69,544.
2. Lump sum capped at EUR 6,070. Net professional income EUR 63,474.
3. Marital quotient: 30% x 63,474 = EUR 19,042.20, capped at EUR 11,780. The earner keeps EUR 51,694; the spouse is taxed on EUR 11,780.
4. Earner's scale tax: 4,180 + 5,116 + 45% x (51,070 - 29,510) = 9,702 + 50% x (51,694 - 51,070) = 312. Total EUR 19,310. Less 2,887.50 on the tax-free amount: EUR 16,422.50.
5. Spouse's scale tax: 25% x 11,780 = EUR 2,945. Less 2,887.50: EUR 57.50. The spouse's income is above EUR 11,550, so no tax-free amount moves to the earner.
6. Couple's tax: EUR 16,480.
7. Check that the quotient lowers the tax (art. 87 skips it otherwise). Without it the earner is taxed on 63,474: scale tax EUR 25,200. The spouse's unused EUR 11,550 tax-free amount moves to the earner (art. 134, §4, 4°), so the earner's tax-free amount is EUR 23,100. Tax on it: 25% x 11,750 + 30% x 4,970 + 40% x 6,380 = EUR 6,980.50. Tax EUR 18,219.50. The quotient saves EUR 1,739.50.
8. Municipal surcharge at 7%: EUR 1,153.60. Total EUR 17,633.60. Withholding EUR 17,000, so EUR 633.60 is still due, within two months of the assessment notice.

```oa-check
name: Married couple, one earner on gross EUR 80,000, marital quotient, income 2026
inputs:
  gross: 80000
  employee_ss_rate: 0.1307
  lump_cap: 6070
  quotient_rate: 0.30
  quotient_cap: 11780
  tax_free: 11550
  municipal_rate: 0.07
  withholding: 17000
steps:
  - taxable_pay: gross - gross * employee_ss_rate
  - net_prof: taxable_pay - min(taxable_pay * 0.30, lump_cap)
  - quotient: min(net_prof * quotient_rate, quotient_cap)
  - earner_income: net_prof - quotient
  - earner_scale: min(earner_income, 16720) * 0.25 + (min(earner_income, 29510) - 16720) * 0.40 + (min(earner_income, 51070) - 29510) * 0.45 + max(earner_income - 51070, 0) * 0.50
  - tax_on_tax_free: tax_free * 0.25
  - earner_tax: earner_scale - tax_on_tax_free
  - spouse_tax: max(min(quotient, 16720) * 0.25 - tax_on_tax_free, 0)
  - couple_tax: earner_tax + spouse_tax
  - no_quotient_scale: 4180 + 5116 + (51070 - 29510) * 0.45 + (net_prof - 51070) * 0.50
  - pooled_tax_free: tax_free * 2
  - no_quotient_tax_free_tax: 11750 * 0.25 + (16720 - 11750) * 0.30 + (pooled_tax_free - 16720) * 0.40
  - no_quotient_tax: no_quotient_scale - no_quotient_tax_free_tax
  - saving: no_quotient_tax - couple_tax
  - municipal: round(couple_tax * municipal_rate, 2)
  - total_tax: couple_tax + municipal
  - balance_due: total_tax - withholding
expected:
  net_prof: 63474
  quotient: 11780
  earner_income: 51694
  earner_scale: 19310
  earner_tax: 16422.50
  spouse_tax: 57.50
  couple_tax: 16480
  no_quotient_scale: 25200
  no_quotient_tax_free_tax: 6980.50
  no_quotient_tax: 18219.50
  saving: 1739.50
  municipal: 1153.60
  total_tax: 17633.60
  balance_due: 633.60
```

## Ask the client first

1. Your forms 281.10 (pay) and 281.11 (pensions) for 2026: gross pay, social security, benefits in kind, payroll withholding.
2. Your municipality of residence, for the surcharge rate, and your region, for regional reductions and the home loan.
3. Your family on 1 January 2027: married or legal cohabitant, children and their ages, other dependants, co-parenting arrangements (art. 132bis).
4. Your real work costs (commuting, home office, training), if they could exceed EUR 6,070.
5. Payments that give reductions: pension savings (and whether you chose the EUR 1,350 option), life insurance, gifts with attestations, childcare attestations, service vouchers.
6. Any foreign income or a partner with treaty-exempt pay.

## Sources

| Source | URL | Read on |
|---|---|---|
| Fisconetplus, art. 51 WIB 92 (income 2026), lump-sum expenses | https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/e2fb1778-ac33-4e91-8e57-e53c0cac384c | 2026-10-23 |
| Fisconetplus, art. 87 WIB 92 (income 2026), marital quotient | https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/9f17497c-c0f6-415e-b715-81f9aeca6765 | 2026-10-23 |
| Fisconetplus, art. 88 WIB 92 (income 2026) | https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/0a136e8c-9144-4e7e-b596-0aede2c66c3e | 2026-10-23 |
| Fisconetplus, art. 126 WIB 92 (income 2026), joint assessment | https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/3e4f68bf-5e84-4124-b5dd-482d1e94b4fb | 2026-10-23 |
| Fisconetplus, art. 130 WIB 92 (income 2026), tax scale | https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/796a4fc5-340e-4c89-a72a-88caa804ca96 | 2026-10-23 |
| Fisconetplus, art. 131 WIB 92 (income 2026), tax-free amount | https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/f3c5d665-cac4-4cbd-b714-bd287f791751 | 2026-10-23 |
| Fisconetplus, art. 132 WIB 92 (income 2026), supplements | https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/caa866c3-8820-4ba4-b5bc-f64ae0cd2869 | 2026-10-23 |
| Fisconetplus, art. 132bis WIB 92, co-parenting split | https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/d6d287ee-1ad3-4f93-9b43-31fd48c705bc | 2026-10-23 |
| Fisconetplus, art. 133 WIB 92 (income 2026) | https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/0f863e7a-b131-494b-8617-7b62efed5e75 | 2026-10-23 |
| Fisconetplus, art. 134 WIB 92 (income 2026) | https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/20a503a9-4213-4e60-a91c-0ebb907e176a | 2026-10-23 |
| Fisconetplus, art. 145/1, 145/2, 145/6, 145/7, 145/8 WIB 92 (income 2026) | https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/c06c831e-30de-44e2-af79-c380a0798b1c | 2026-10-23 |
| Fisconetplus, art. 145/21, 145/24, 145/33, 145/35 WIB 92 (income 2026) | https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/496c7428-bd55-4d78-bfc5-c3526c941973 | 2026-10-23 |
| Fisconetplus, art. 147, 151, 152 WIB 92 (income 2026) | https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/29f2d0bb-6658-4cf8-b870-283c99274b07 | 2026-10-23 |
| Fisconetplus, art. 289ter/1 WIB 92 (income 2026), fiscal work bonus | https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/5403364d-120e-4c43-8945-ac770f1228f6 | 2026-10-23 |
| Fisconetplus, art. 296 WIB 92, credit for withholding | https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/5e78417c-8576-421e-8e4c-b35eed613404 | 2026-10-23 |
| Fisconetplus, art. 304 WIB 92, refund and EUR 2.50 limit | https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/7b9fd251-9dee-420b-abc5-6d34344400f9 | 2026-10-23 |
| Fisconetplus, art. 306 WIB 92, simplified proposal | https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/4e0c82f4-176b-4e40-a97e-7be85954d7f0 | 2026-10-23 |
| Fisconetplus, art. 308 and 308/1 WIB 92, filing dates | https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/182821e5-122a-4948-867e-297c16371fe1 | 2026-10-23 |
| Fisconetplus, art. 413 and 414 WIB 92, payment and interest | https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/db296af5-75b3-49bc-95e2-a35bb742fed5 | 2026-10-23 |
| Fisconetplus, law of 5 May 1865, art. 2, §2/1, yearly rates | https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/da7e0caf-3428-43aa-ab80-30410a15beca | 2026-10-23 |
| Fisconetplus, art. 444 and 445 WIB 92 (income 2026) | https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/5095859f-8ffb-42f9-b535-3197a7c3dbe0 | 2026-10-23 |
| Fisconetplus, art. 465 to 470 WIB 92 (income 2026), municipal surcharge | https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/81bf3101-a837-4d89-8b97-713e080f00ac | 2026-10-23 |
| RSZ, administrative instructions 2026/3, contribution rates | https://www.socialsecurity.be/employer/instructions/dmfa/nl/latest/instructions/socialsecuritycontributions/contributions.html | 2026-10-23 |

Not yet confirmed: the Tax-on-web opening date and any administrative extension for income 2026 (FPS Finance pages at financien.belgium.be were behind a human-verification check and could not be read; the legal end dates of art. 308 are given instead); the regional surcharge rates and the autonomy factor for income 2026 that split the basic tax between the federal state and the regions (the examples assume they offset exactly); the indexed regional amounts for service vouchers and the regional home loan rules; the detail of the new minimum tax credit for dependent children in chapter 2 of the law of 15 July 2026; which date fixes the municipality whose rate applies; the parts A and B of the social security work bonus (law of 20 December 1999) for 2026.
