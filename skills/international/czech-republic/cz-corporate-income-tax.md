---
name: cz-corporate-income-tax
description: "Use this skill for Czech corporate income tax (daň z příjmů právnických osob, DPPO) in tax year 2026. It covers who is a taxpayer and who is resident (Income Taxes Act § 17), the 21% rate and the 5%, 0% and 15% special rates (§ 21), the tax base and the main non-deductible costs (§§ 23 to 25), tax depreciation (§§ 26 to 33), losses (back 2 years, forward 5, § 34), the participation exemption (§ 19), the limit on exceeding borrowing costs (30% of tax EBITDA or CZK 80 million, § 23e), advances (§ 38a), return and payment deadlines for 2026, penalties and late payment interest. Trigger on: Czech corporate tax, DPPO, s.r.o. tax, daňové přiznání právnických osob, zálohy na daň, daňové odpisy, daňová ztráta, úroky 23e. Out of scope: transfer pricing and thin capitalisation (cz-transfer-pricing), withholding on payments abroad and exit tax (cz-cross-border), VAT (cz-vat-return), top-up tax for large groups."
jurisdiction: CZ
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-23
version: 0.1
verified_by: pending
trust_label: Built by Michael Cutajar and the OpenAccountants team
---

# Czech Republic: corporate income tax (2026) v0.1

> **Source-cited draft.** Built by Michael Cutajar and the OpenAccountants team. No accountant has reviewed this skill yet. The law comes from the consolidated texts on e-Sbírka (the official Collection of Laws), and the guidance from financnisprava.gov.cz and cnb.cz, all read on 23 October 2026. It prepares working papers; it is not authority to file or pay.

This is the corporate income tax (IT-CORP) skill for the Czech pack. It links rather than repeats:

- Transfer pricing, related persons, the related-party annex and thin capitalisation (§ 25(1)(w)): [cz-transfer-pricing](cz-transfer-pricing.md).
- Withholding on payments to non-residents, the tax security, exit tax (§ 23g) and treaties: [cz-cross-border](cz-cross-border.md).
- Payroll withholding by the company as employer: [cz-payroll](cz-payroll.md).
- Setting up a company: [cz-company-formation](cz-company-formation.md). Overview: [cz-tax-overview](cz-tax-overview.md).

Law: Act No. 586/1992 Coll., Income Taxes Act ("ITA"), version in force from 1 August 2026, and Act No. 280/2009 Coll., Tax Code ("TC"), version in force from 1 January 2026. Currency: Czech koruna (CZK). Authority: the Financial Administration (Finanční správa).

## Who this applies to

- **Taxpayers.** Legal persons (s.r.o., a.s., cooperatives, foundations and others), units of the state, unit trusts and sub-funds, pension company funds, trust funds, and foreign entities treated as taxpayers under their own law (ITA § 17(1)).
- **Residents.** A taxpayer with its seat or its place of management in the Czech Republic is resident and is taxed on worldwide income (ITA § 17(3)).
- **Non-residents.** A taxpayer with no Czech seat, or one a treaty treats as non-resident, is taxed only on Czech-source income (ITA § 17(4)). A non-resident with a permanent establishment files a return for the establishment's profit. Withholding on other Czech-source income is in [cz-cross-border](cz-cross-border.md).
- **Tax period.** The calendar year, a financial year (hospodářský rok), the period from the effective date of a merger or division, or an accounting period longer than 12 months (ITA § 21a).
- **Partnerships.** A corporate partner in a v.o.s. includes its share of the partnership's base. A k.s. is taxed on the part not attributable to general partners, and a corporate general partner includes its share (ITA § 20(4) to (6)).
- **Out of scope.** Windfall profits tax: it applies to tax periods that fall at least partly in the calendar years 2023 to 2025 (ITA § 20ba(1), (3)). A calendar year 2026 period is outside it. A financial year that began in 2025 and ends in 2026 is inside it, and this skill does not cover it. Top-up tax for groups with consolidated revenue of EUR 750 million or more in at least 2 of the 4 prior periods (Act No. 416/2023 Coll., § 8(1)(b)) is not covered here.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Standard corporate income tax rate | 21% | 2026 | [ITA § 21(1)](https://e-sbirka.gov.cz/sb/1992/586/2026-08-01) |
| Basic investment fund | 5% | 2026 | ITA § 21(2) |
| Pension company funds and pension institutions | 0% | 2026 | ITA § 21(3) |
| Separate base: profit shares from abroad that are not exempt | 15% | 2026 | ITA § 20b, § 21(4) |
| Rounding | Base (after deductions) rounded down to whole CZK thousands; tax rounded up to whole CZK | 2026 | ITA § 20(11), § 21(1); [TC § 146(1)](https://e-sbirka.gov.cz/sb/2009/280/2026-01-01) |
| Tangible asset threshold for tax depreciation (movable items) | input price over CZK 80,000 and useful life over 1 year | 2026 | ITA § 26(2)(a) |
| Depreciation groups and minimum periods | Group 1: 3 years; 2: 5; 3: 10; 4: 20; 5: 30; 6: 50 | 2026 | ITA § 30(1) |
| Passenger car (category M1): depreciation counted for tax | only the share of each charge equal to CZK 2,000,000 divided by the input price | 2026 | ITA § 30e(1), (2) |
| Zero-emission vehicle bought 2024 to 2028, first user | 100% over 24 months: 60% in the first 12 months, 40% in the next 12 | 2026 | ITA § 30a(1) |
| Tax loss carry-forward | 5 periods after the loss period | 2026 | ITA § 34(1) |
| Tax loss carry-back | 2 periods before the loss period, CZK 30,000,000 in total | 2026 | ITA § 34(1) |
| Loss forfeited on a substantial change in ownership | more than 25% of capital or votes changes hands, unless at least 80% of revenue still comes from the same activity | 2026 | ITA § 38na(1), (3) |
| Participation exemption: holding | at least 10% of the subsidiary's capital, held for at least 12 months without a break | 2026 | ITA § 19(1)(ze), § 19(3)(b), (c), § 19(4) |
| Participation exemption: non-EU subsidiary | treaty state, comparable legal form, taxed at a rate of at least 12% | 2026 | ITA § 19(9) |
| Limit on exceeding borrowing costs | the higher of 30% of tax EBITDA or CZK 80,000,000 | 2026 | ITA § 23e(1) |
| Thin capitalisation (related-party debt) | interest on debt above 4 times equity (6 times for banks and insurers) not deductible; see cz-transfer-pricing | 2026 | ITA § 25(1)(w) |
| Gifts deductible from the base | each gift at least CZK 2,000; in total at most 10% of the base after losses | 2026 | ITA § 20(8) |
| Advances: none due | last known tax up to CZK 30,000 | 2026 | ITA § 38a(2)(a) |
| Advances: two a year | last known tax over CZK 30,000 up to CZK 150,000: 40% each, by the 15th day of the 6th and 12th month of the period | 2026 | ITA § 38a(3) |
| Advances: four a year | last known tax over CZK 150,000: 1/4 each, by the 15th day of the 3rd, 6th, 9th and 12th month | 2026 | ITA § 38a(4) |
| Advance rounding | up to whole CZK hundreds | 2026 | TC § 146(2) |
| Withholding on dividends, interest, royalties and service fees paid to non-residents | 15%; 35% to residents of states outside the EU and EEA with no treaty, tax information exchange agreement or multilateral information exchange convention in force with the Czech Republic | 2026 | ITA § 36(1)(a) to (c), § 36(2) |
| Penalty on extra tax assessed by the tax office (penále) | 20% of the extra tax; 1% of a reduced tax loss | 2026 | TC § 251(1) |
| Late return penalty | 0.05% of the tax a day after 5 working days late, capped at 5% of the tax and CZK 300,000 (0.01% a day of a tax loss) | 2026 | TC § 250(1), (5) |
| Late payment interest: CNB repo rate on the first day of the calendar half-year in which each day of interest falls, plus 8 points | 11.50% a year for days from 1 January to 30 June 2026; 11.75% for days from 1 July to 31 December 2026 | 2026 | TC § 251a(5), § 252(4); [Government Regulation 351/2013 § 2(1)](https://e-sbirka.gov.cz/sb/2013/351); [CNB repo history](https://www.cnb.cz/cs/faq/vyvoj_repo_historie.txt) |

Repo rate: 3.50% from 9 May 2025 and 3.75% from 19 June 2026 (CNB repo history). The rate on 1 January 2026 was 3.50%, so 3.50 + 8 = 11.50%; on 1 July 2026 it was 3.75%, so 3.75 + 8 = 11.75%.

The rate that applies is the rate in force on the first day of the tax period (ITA § 21(7)).

## The taxable base

**Starting point.** The base is the accounting result (profit or loss under Czech accounting rules), adjusted under ITA §§ 23 to 33 (ITA § 20(1), § 23). A taxpayer that keeps no accounts uses income less expenses. The Financial Administration describes the same link to the accounts ([Finanční správa, DPPO obecné informace](https://financnisprava.gov.cz/cs/dane/dane/dan-z-prijmu/pravnicke-osoby/obecne-informace)).

**Order of the computation.**

1. Accounting result.
2. Add back non-deductible costs and items that increase the base; deduct income that is exempt or not taxable (ITA §§ 23 to 25).
3. Replace accounting depreciation of tangible assets with tax depreciation (ITA § 25(1)(zg), § 24(2)(a), §§ 26 to 33).
4. Apply the borrowing cost limit (ITA § 23e).
5. Deduct a tax loss and the R&D and vocational training deductions (ITA § 34).
6. Deduct qualifying gifts (ITA § 20(8)).
7. Round down to whole CZK thousands and apply 21% (ITA § 20(11), § 21(1)).
8. Deduct tax credits, for example an investment incentive (ITA § 35a, § 35b).

**Common non-deductible costs (ITA § 25(1)).**

- Acquiring tangible and intangible assets, except through depreciation (a).
- Profit distributions (e).
- Penalties, late payment interest and fines, and surcharges on social and health insurance (f). Contractual penalties, late payment interest and other sanctions under contracts are deductible once paid (§ 24(2)(zi)).
- Representation costs: hospitality, refreshments and gifts. A promotional item with the company's name or trademark, worth no more than CZK 500 excluding VAT and not subject to excise duty, is not a gift (t).
- Income tax itself, and deferred tax (s).
- Reserve funds and valuation allowances, except those § 24 allows (l, v).
- Interest on related-party debt above 4 times equity (w), and interest that depends wholly or mainly on the borrower's profit (zl). Both are in [cz-transfer-pricing](cz-transfer-pricing.md).
- Accounting depreciation of long-term assets where tax depreciation applies instead (zg).
- Costs of a parent company connected with holding a share in a subsidiary (zk), and costs relating to exempt or non-taxable income (i).
- Losses and shortfalls above compensation received (n), and the written-down value of an asset given away (o).

**Tax depreciation.** Movable items costing over CZK 80,000 with a useful life of more than a year, and buildings and structures, are depreciated for tax (ITA § 26(2)). Each asset goes into one of six groups in Annex 1 (ITA § 30(1)). The company chooses straight-line (§ 31) or accelerated (§ 32) for each new asset and cannot change it later (§ 30(2)).

- Straight-line maximum rates, first year and later years: group 1, 20% and 40%; group 2, 11% and 22.25%; group 3, 5.5% and 10.5%; group 4, 2.15% and 5.15%; group 5, 1.4% and 3.4%; group 6, 1.02% and 2.02% (§ 31(1)(a)). A company may use lower rates (§ 31(7)).
- Accelerated coefficients, first year and later years: group 1, 3 and 4; group 2, 5 and 6; group 3, 10 and 11; group 4, 20 and 21; group 5, 30 and 31; group 6, 50 and 51 (§ 32(1)).
- Charges are rounded up to whole CZK (§ 31(9), § 32(5)).
- A company need not claim tax depreciation and may interrupt it, but must later continue as if it had not been interrupted (§ 26(8)).
- Intangible assets are written off through accounting depreciation, which is deductible under § 24(2)(v).

**Losses.** A tax loss can be deducted in the 5 periods after the loss period. It can also be carried back to the 2 periods before it, up to CZK 30,000,000 in total. A company may waive the right to deduct the loss in the periods after the loss period, by notice to the tax office within the filing deadline for the loss year. The waiver covers all later periods and cannot be withdrawn (ITA § 34(1)). The 30,000,000 cap applies only to the carry-back. A loss cannot be used after a substantial change in the persons who hold the capital or control, which always includes an acquisition of more than 25% of the capital or votes in total, or a member gaining decisive influence. The bar does not apply if the company shows that at least 80% of its revenue comes from the same activity it carried on in the loss year (ITA § 38na(1), (3)). The time limit to assess tax runs with the last year in which the loss could be used (ITA § 38r(2)).

**Participation exemption.** Dividends from a subsidiary paid to a Czech parent, and gains on selling a share in a subsidiary, are exempt where the parent holds at least 10% of the capital for at least 12 months without a break and is the beneficial owner (ITA § 19(1)(ze), (zi), § 19(3)(b), (c), § 19(9)). Dividends from a Czech subsidiary fall under § 19(1)(ze) and dividends from an EU subsidiary under § 19(1)(zi). The exemption can be claimed before 12 months have passed, but the holding must then reach 12 months (§ 19(4)). The subsidiary must be a Czech company or an EU company in a listed form (§ 19(3)). A subsidiary in a non-EU state qualifies if the state has a tax treaty with the Czech Republic in force, the subsidiary has a form comparable to an s.r.o., a.s. or cooperative, and it is taxed at a rate of at least 12% in the year the dividend is booked and the year before (§ 19(9)). Norway, Iceland and Liechtenstein are treated like EU states (§ 19(10)). Foreign dividends that are not exempt go into a separate base taxed at 15% (§ 20b, § 21(4)).

**Limit on exceeding borrowing costs (ITA § 23e).**

- Exceeding borrowing costs are deductible borrowing costs (interest and similar costs) less taxable interest income (§ 23e(2) to (4)).
- Where they exceed the limit, the excess is added to the base. The limit is the higher of 30% of tax EBITDA or CZK 80,000,000 (§ 23e(1)).
- Tax EBITDA is the adjusted result before the § 23e adjustment, plus bases taxed by withholding and the 15% separate base, plus tax depreciation, plus the goodwill amortisation allowed for tax, plus the exceeding borrowing costs (§ 23e(6)).
- An amount added back can be deducted in later periods, up to the unused headroom in each period. It does not pass to a legal successor (§ 23e(7)).
- Only deductible costs count (§ 23e(2)), so interest already disallowed under thin capitalisation (§ 25(1)(w)) is not counted again.

**Gifts.** Gifts to municipalities, regions, Czech legal persons and others for listed public purposes reduce the base. Each gift must be at least CZK 2,000, and in total the deduction is capped at 10% of the base after losses (ITA § 20(8)).

**Other rules.** Exit tax on moving assets abroad (§ 23g) and controlled foreign companies (§ 38fa) are in [cz-cross-border](cz-cross-border.md). Arm's length prices between related persons (§ 23(7)) are in [cz-transfer-pricing](cz-transfer-pricing.md).

## Deadlines and filing

**Return (ITA § 38m, TC § 136).** Every corporate taxpayer files a return, with narrow exceptions for public benefit taxpayers (ITA § 38mb). The return is due within 3 months after the end of the tax period. The deadline extends to 4 months where the return is filed electronically after the 3-month date. It extends to 6 months where the accounts must be audited, or where a tax adviser files after the 3-month date (TC § 136(1), (2)). A deadline that falls on a Saturday, Sunday or public holiday moves to the next working day (TC § 33(4)).

For a calendar year 2026 company, counting the same way as the [cz-income-tax](cz-income-tax.md) skill:

- paper or electronic: **1 April 2027** (Thursday);
- electronic, after 1 April: **3 May 2027**, because 1 May 2027 is a Saturday and a public holiday;
- audited company, or tax adviser files: **1 July 2027**.

For a company whose accounts must be audited, only the 6-month deadline applies; the Financial Administration says the 3-month deadline never applies to it ([Finanční správa, DPFO obecné informace](https://financnisprava.gov.cz/cs/dane/dane/dan-z-prijmu/fyzicke-osoby/obecne-informace)). For the 2025 period the Financial Administration gave 1 April, 4 May and 1 July 2026 on the same page. A company with a financial year counts the same months from the end of its period.

**Electronic filing.** A company with a data box set up by law, or one that must have its accounts audited, must file the return electronically (TC § 72(6)).

**Payment.** The tax is due on the last day for filing the return (TC § 135(3)).

**Advances (ITA § 38a).** Advances depend on the last known tax liability. The advance period runs from the day after the filing deadline for the previous period to the filing deadline for the current one (§ 38a(1)).

- Last known tax up to CZK 30,000: no advances (§ 38a(2)(a)).
- Over CZK 30,000 up to CZK 150,000: two advances of 40%, due by the 15th day of the 6th and 12th months of the tax period (§ 38a(3)).
- Over CZK 150,000: four advances of 25%, due by the 15th day of the 3rd, 6th, 9th and 12th months (§ 38a(4)).
- A previous period shorter or longer than 12 months is scaled to 12 months (§ 38a(6)). Tax in the 15% separate base is left out of the last known tax (§ 38a(1)).
- Advances are rounded up to whole CZK hundreds (TC § 146(2)). The tax office may set advances differently on request ([Finanční správa, DPPO obecné informace](https://financnisprava.gov.cz/cs/dane/dane/dan-z-prijmu/pravnicke-osoby/obecne-informace)).

**Supplementary return.** If the company finds its tax should be higher than the last known tax, it files a supplementary return (dodatečné daňové přiznání) and pays the difference by the end of the month after the month it found this (TC § 141(1)). Self-disclosed extra tax carries no 20% penalty (TC § 251(4)).

**Related-party annex.** Companies over the size tests file the related-party transactions annex with the return; see [cz-transfer-pricing](cz-transfer-pricing.md).

## Penalties and interest

- **Late return (TC § 250).** If the return is more than 5 working days late, the penalty is 0.05% of the assessed tax for each further day, capped at 5% of the tax. For a tax loss it is 0.01% a day, capped at 5% of the loss (§ 250(1)). The penalty is never more than CZK 300,000 (§ 250(5)). A penalty under CZK 1,000 is not charged (§ 250(3)). It is halved if the return is filed within 30 days of the deadline and no other late filing was found that year (§ 250(7)). If no return is filed at all, the cap applies and the penalty is at least CZK 500 (§ 250(4)).
- **Penalty on extra tax (penále, TC § 251).** When the tax office assesses extra tax, the penalty is 20% of the extra tax, or 1% of a reduced tax loss (§ 251(1)). There is none on tax the company disclosed itself in a valid supplementary return (§ 251(4)).
- **Late payment interest (TC § 252).** It runs from the fourth day after the original due date until payment (§ 252(2)). Interest arises for each day separately (§ 251a(1)). The rate for each day is the CNB repo rate on the first day of the calendar half-year in which that day falls, plus 8 points (TC § 251a(5), § 252(4); Government Regulation 351/2013 § 2(1)). Days from 1 January to 30 June 2026 bear 11.50% a year; days from 1 July to 31 December 2026, 11.75%. A daily amount uses a 365-day year (TC § 146(4)). Interest of CZK 1,000 or less in total for one tax and period is not charged (§ 251a(2)).
- **Not deductible.** Penalties and late payment interest owed on tax are not deductible for corporate tax (ITA § 25(1)(f)).
- **Missed reporting duties.** Fines for missed reporting duties and the transfer pricing points are in [cz-transfer-pricing](cz-transfer-pricing.md).

## Cross-border points

- **Withholding on payments abroad.** A Czech company paying dividends, interest, royalties or service fees to a non-resident withholds 15%. The rate is 35% where the recipient is resident outside the EU and EEA in a state that has neither a tax treaty nor a tax information exchange agreement with the Czech Republic in force, and is not party to a multilateral convention on tax information exchange in force between it and the Czech Republic (ITA § 36(1)(a) to (c), § 36(2)). The tax is paid to the tax office by the end of the month after the month of withholding (ITA § 38d(3)). For dividends, it is withheld on payment and no later than the end of the third month after the month the accounts were approved and the profit distribution was decided (§ 38d(2)). EU directive exemptions, treaty caps and the 10% tax security are in [cz-cross-border](cz-cross-border.md).
- **Dividends paid to a Czech company.** Dividends from a Czech s.r.o. or a.s. to a Czech company that does not meet the participation exemption bear 15% withholding (ITA § 36(2)(a), (b)).
- **Foreign dividends received.** These are exempt if § 19 is met; otherwise they fall in the 15% separate base (§ 20b).
- **Foreign tax relief.** A resident company relieves double tax under the treaty (ITA § 38f(1)). See [cz-cross-border](cz-cross-border.md).
- **Interest and prices between related persons, and thin capitalisation.** See [cz-transfer-pricing](cz-transfer-pricing.md).

## Worked examples

### Example 1: s.r.o., calendar year 2026, with a loss brought forward

Novák Trade s.r.o. has an accounting profit for 2026 of CZK 5,013,450. Its accounts include CZK 120,000 of client hospitality, a CZK 30,000 fine from a regulator and CZK 400,000 of accounting depreciation. Its tax depreciation for 2026 is CZK 350,000. It has an unused tax loss of CZK 600,000 from 2023, still within the 5-year window, and no change of ownership.

1. Add back hospitality (ITA § 25(1)(t)) and the fine (§ 25(1)(f)): CZK 150,000.
2. Swap depreciation: add back CZK 400,000 of accounting depreciation (§ 25(1)(zg)) and deduct CZK 350,000 of tax depreciation (§ 24(2)(a)).
3. Base before losses: 5,013,450 + 150,000 + 400,000 - 350,000 = CZK 5,213,450.
4. Deduct the 2023 loss (§ 34(1)): CZK 4,613,450.
5. Round down to whole thousands (§ 20(11)): CZK 4,613,000.
6. Tax at 21% (§ 21(1)): CZK 968,730.
7. The tax is over CZK 150,000, so four quarterly advances are due in the next advance period. Each is 968,730 / 4 = 242,182.50, rounded up to whole hundreds: CZK 242,200 (§ 38a(4); TC § 146(2)).
8. The return and payment are due by 1 April 2027, or 3 May 2027 if filed electronically after 1 April, or 1 July 2027 if a tax adviser files.

```oa-check
name: Czech s.r.o. 2026, loss brought forward, 21% rate and advances
inputs:
  accounting_profit: 5013450
  hospitality: 120000
  fine: 30000
  accounting_depreciation: 400000
  tax_depreciation: 350000
  loss_brought_forward: 600000
steps:
  - base_before_loss: accounting_profit + hospitality + fine + accounting_depreciation - tax_depreciation
  - base_after_loss: base_before_loss - loss_brought_forward
  - base_rounded: floor(base_after_loss / 1000) * 1000
  - tax: base_rounded * 21 / 100
  - advance: ceil(tax / 4 / 100) * 100
expected:
  base_before_loss: 5213450
  base_after_loss: 4613450
  base_rounded: 4613000
  tax: 968730
  advance: 242200
```

### Example 2: financing company caught by the borrowing cost limit

Brno Logistics a.s. (calendar year 2026) has an adjusted result, before any § 23e adjustment, of CZK 120,000,000. Its tax depreciation is CZK 35,000,000. Its deductible interest costs are CZK 97,000,000 and its taxable interest income is CZK 2,000,000. No related-party debt is above the thin capitalisation limit, and it has no withholding-taxed or separate-base income.

1. Exceeding borrowing costs: 97,000,000 - 2,000,000 = CZK 95,000,000 (ITA § 23e(2)).
2. Tax EBITDA: 120,000,000 + 35,000,000 + 95,000,000 = CZK 250,000,000 (§ 23e(6)(a), (d), (f)).
3. 30% of tax EBITDA is CZK 75,000,000. That is below CZK 80,000,000, so the limit is CZK 80,000,000, the higher figure (§ 23e(1)).
4. Excess added back: 95,000,000 - 80,000,000 = CZK 15,000,000.
5. Base: 120,000,000 + 15,000,000 = CZK 135,000,000, already in whole thousands.
6. Tax at 21%: CZK 28,350,000.
7. The CZK 15,000,000 can be deducted in later periods, up to the headroom in each period between the limit and that period's exceeding borrowing costs (§ 23e(7)). Without the CZK 80,000,000 floor, the limit would be CZK 75,000,000 and the add-back CZK 20,000,000.

```oa-check
name: Czech a.s. 2026, exceeding borrowing costs above the CZK 80m floor
inputs:
  adjusted_result: 120000000
  tax_depreciation: 35000000
  interest_costs: 97000000
  interest_income: 2000000
  floor_amount: 80000000
steps:
  - ebc: interest_costs - interest_income
  - tax_ebitda: adjusted_result + tax_depreciation + ebc
  - thirty_pct: tax_ebitda * 30 / 100
  - limit: max(thirty_pct, floor_amount)
  - add_back: max(ebc - limit, 0)
  - base: floor((adjusted_result + add_back) / 1000) * 1000
  - tax: base * 21 / 100
expected:
  ebc: 95000000
  tax_ebitda: 250000000
  thirty_pct: 75000000
  limit: 80000000
  add_back: 15000000
  base: 135000000
  tax: 28350000
```

## Ask the client first

1. The tax period: calendar year or financial year, and any merger, division or change of period. This sets the deadlines and the advance periods.
2. Whether the accounts must be audited, and whether a tax adviser files the return. This decides the 1 April, 3 May or 1 July deadline.
3. The last known tax liability. This sets whether advances are due and how often.
4. Tax losses from earlier years, by year, and any change in ownership or control since. This decides how much loss can be used.
5. Borrowings: interest costs and income, related-party lenders and equity. This decides the § 23e limit and thin capitalisation.
6. Shareholdings in other companies (percentage, holding period, country) and any dividends or share sales. This decides the participation exemption.

## Sources

| Source | URL | Read on |
|---|---|---|
| Act No. 586/1992 Coll., Income Taxes Act, version in force from 1 August 2026: §§ 17, 19, 20, 20b, 20ba, 21, 21a, 23, 23e, 24, 25, 26, 30, 30a, 30e, 31, 32, 34, 36, 38a, 38d, 38f, 38m, 38mb, 38na, 38r | https://e-sbirka.gov.cz/sb/1992/586/2026-08-01 | 2026-10-23 |
| Act No. 280/2009 Coll., Tax Code, version in force from 1 January 2026: §§ 33, 72, 135, 136, 141, 146, 250, 251, 251a, 252 | https://e-sbirka.gov.cz/sb/2009/280/2026-01-01 | 2026-10-23 |
| Government Regulation No. 351/2013 Coll., § 2(1) (late payment interest: repo plus 8 points) | https://e-sbirka.gov.cz/sb/2013/351 | 2026-10-23 |
| Act No. 416/2023 Coll., top-up taxes, § 8(1)(b) (EUR 750 million group test) | https://e-sbirka.gov.cz/sb/2023/416 | 2026-10-23 |
| Finanční správa, Daň z příjmů fyzických osob, obecné informace (2025 filing dates; the 3-month deadline does not apply to audited taxpayers) | https://financnisprava.gov.cz/cs/dane/dane/dan-z-prijmu/fyzicke-osoby/obecne-informace | 2026-10-23 |
| Finanční správa, Daň z příjmů právnických osob, obecné informace (rate, advances, link to accounts) | https://financnisprava.gov.cz/cs/dane/dane/dan-z-prijmu/pravnicke-osoby/obecne-informace | 2026-10-23 |
| Czech National Bank, two-week repo rate history | https://www.cnb.cz/cs/faq/vyvoj_repo_historie.txt | 2026-10-23 |

Not yet confirmed: the Financial Administration had not published the filing dates for 2026 corporate returns, so 1 April, 3 May and 1 July 2027 are counted from TC §§ 33(4) and 136 in the same way as cz-income-tax; the full conditions of the investment incentive credit (§ 35a, § 35b) and the R&D deduction (§ 34(4) and § 34a onwards) were not read here.
