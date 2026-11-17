---
name: croatia-tax-optimization
description: "Use this skill whenever asked about lowering tax legally in Croatia for tax year 2026: tax planning, saving tax, allowances or deductions a client might be missing, or strategies for a self-employed person or small business. Covers the choice between a lump-sum paušalni obrt (seven 2026 bands up to EUR 60,000, 12% tax, EUR 797.20 contribution base), a trade on books and a d.o.o. (10% or 18% profit tax, then 12% on dividends), employing family, dependants on the allowance, the youth, returnee and assisted-area reliefs, voluntary pension premiums, depreciation timing, and the anti-avoidance lines in the General Tax Act. Trigger on: reduce tax Croatia, paušalni obrt, paušalist, lump-sum tax, obrt vs d.o.o., save tax Croatia, tax planning Croatia, porezno planiranje, returnee tax relief, young person tax relief. Out of scope: croatia-income-tax, hr-corporate-income-tax, croatia-social-contributions, croatia-vat-return, hr-cross-border."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/croatia-tax-optimization"
  jurisdiction: "HR"
  tax_year: "2026"
  last_updated: "2026-11-17"
---

# Croatia Tax Optimization v0.3

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

**Tax year 2026 (calendar year). Every figure below is taken from the consolidated texts in the Tax Administration's register of regulations, read on 2026-10-30 and re-read on 2026-11-17 (see Sources). Figures must agree with [croatia-income-tax](croatia-income-tax.md), [hr-corporate-income-tax](hr-corporate-income-tax.md) and [croatia-social-contributions](croatia-social-contributions.md); if they ever differ, those skills win. No licensed Croatian tax adviser has signed this skill off (Not yet approved). Every suggestion must be reviewed by a credentialed professional; aggressive positions are never advised.**

- **Who this is for.** Residents of Croatia (Republika Hrvatska) who are self-employed or run a small business, and their employees and families, asking how to lower tax legally. Currency EUR.
- **Key optimisation levers.** Regime choice (paušalni obrt / obrt on books / d.o.o.); personal allowance and dependants; youth, returnee and assisted-area reliefs; voluntary pension premiums; depreciation timing.
- **Out of scope.** The full computations: [croatia-income-tax](croatia-income-tax.md), [hr-corporate-income-tax](hr-corporate-income-tax.md), [croatia-social-contributions](croatia-social-contributions.md), [croatia-vat-return](croatia-vat-return.md), [hr-cross-border](hr-cross-border.md).
- **Disclaimer.** This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a licensed tax adviser in Croatia) before acting upon.

> **The single biggest Croatian lever is REGIME CHOICE.** For a trade with receipts up to EUR 60,000 a year and low real costs, the paušalni (lump-sum) obrt usually pays far less than an obrt on books or a d.o.o. Confirm eligibility before anything else: free professions cannot use it.

## Ask the client first

1. Is the activity a trade (obrt) or agriculture or forestry, or a free profession (health, law, engineering, consulting, journalism, art, sport and the others in ZPD art. 29(2))? Free professions cannot be paušalist.
2. Expected annual receipts, and real business costs, for 2026.
3. Is the client in VAT, or likely to pass EUR 60,000 of domestic turnover?
4. Is the obrt the only insurance basis, or a second activity next to employment?
5. Local unit of domicile or habitual abode (sets the income tax rates), age, dependants, and whether the client lived abroad for two years or more.
6. For a d.o.o.: revenue level (EUR 1,000,000 split) and how much profit will be paid out each year.

## The method, step by step

### Step 1. The figures that decide (2026)

| Item (tax year 2026) | Figure and conditions | Law | Source |
|---|---|---|---|
| PIT rates (2026) | Lower rate on the annual base up to EUR 60,000, higher rate above | Income Tax Act (ZPD) art. 19 | https://porezna-uprava.gov.hr/Propisi/Propis/zakon-o-porezu-na-dohodak-redakcijski-procisceni-tekst/3 |
| Local rate ranges | Each local unit sets its rates inside ranges: lower 15% to 20%/21%/22%/23% and higher 25% to 30%/31%/32%/33% depending on the type of unit, Zagreb having the widest range; default 20% / 30% where no decision was made. The rate follows the taxpayer's domicile or habitual abode (art. 1(2)) | ZPD art. 19.a(2), (5) | same |
| Basic personal allowance | EUR 600 a month, EUR 7,200 a year (computed: 12 x EUR 600) | ZPD art. 14(1) | same |
| Dependants | Coefficients 0.5 / 0.5 / 0.7 / 1.0 x EUR 600 for a dependent close family member and the first, second and third child: EUR 300 / 300 / 420 / 600 a month; a dependant with own income above EUR 3,600 a year (computed: six times the EUR 600 monthly allowance) does not count | ZPD art. 14(3), 17(1) | same |
| Dividends to individuals | 12% withheld | ZPD art. 70(19) | same |
| Private use of company assets or services | 36% withheld on the benefit | ZPD art. 70(2) | same |
| Voluntary pension premiums | Tax-free and deductible up to EUR 67 a month, EUR 804 a year | ZPD art. 9 point 18, 32(11) | same |
| Profit tax (d.o.o.) | 10% if revenue in the period is up to EUR 1,000,000; 18% above | Profit Tax Act art. 28 | https://porezna-uprava.gov.hr/Propisi/Propis/zakon-o-porezu-na-dobit-redakcijski-procisceni-tekst/1641 |
| Long-term asset threshold | Items costing more than EUR 665 each and lasting more than a year | Profit Tax Act art. 12(3) | same |
| Car depreciation cap | EUR 54,000 of cost per passenger car | Profit Tax Act art. 12(13) | same |
| VAT registration threshold (2026) | EUR 60,000 of domestic turnover in the year | VAT Act art. 90(1) | https://porezna-uprava.gov.hr/Propisi/Propis/zakon-o-porezu-na-dodanu-vrijednost/1651 |
| Paušalist contribution base | EUR 797.20 a month | Contributions Act art. 70; 2026 Bases Order art. 7 | https://porezna-uprava.gov.hr/Propisi/Propis/naredba-o-iznosima-osnovica-za-obracun-doprinosa-za-obvezna-osiguranja-za-2026-godinu/5778 |
| Obrt on books contribution base | EUR 1,295.45 a month for a trade; EUR 2,192.30 for a free profession | Contributions Act art. 65, 66(1); 2026 Bases Order art. 6 | same |
| Second-activity annual cap | EUR 15,545.40 | Contributions Act art. 185(1); 2026 Bases Order art. 12 | same |
| Board member without employment contract | Contributions on EUR 1,993 a month | 2026 Bases Order art. 7 | same |
| Paušalist contributions a month | EUR 119.58 Pillar I, EUR 39.86 Pillar II, EUR 131.54 health: EUR 3,491.76 a year in all (computed: 12 x the three monthly amounts) | Tax Administration, Obrtnici paušalisti | https://porezna-uprava.gov.hr/hr/obrtnici-pausalisti/4564 |
| Anti-avoidance | Substance over form (art. 11(1)); sham transactions (art. 12); use of tax advantages against the purpose of the law, including disguised employment and frequent changes of business form (art. 12.a) | General Tax Act (OPZ) art. 11, 12, 12.a | https://porezna-uprava.gov.hr/Propisi/Propis/opci-porezni-zakon-redakcijski-procisceni-tekst/3155 |

### Step 2. Regime election (the core decision)

| Regime | Best when | Tax treatment | Trade-offs |
| --- | --- | --- | --- |
| **Paušalni obrt** (lump-sum sole trader) | Receipts up to EUR 60,000; low real costs; trades (obrt, including other business activities the law does not list separately) and agriculture or forestry (ZPD art. 82(1), 29(1) point 1, 29(3); Paušalni Ordinance art. 2(1)) | Income tax of 12% on a deemed income fixed by the band the year's receipts fall in (ZPD art. 82(1), (6); Paušalni Ordinance art. 3(1), 4(1)), paid quarterly by the last day of each quarter (Ordinance art. 6(1)). Contributions on a fixed monthly base of EUR 797.20 in 2026 (Contributions Act art. 70; 2026 Bases Order art. 7). Keeps only a sales book (ZPD art. 82(4)). Not in VAT. | Real costs cannot be deducted; capped at the VAT limit; free professions cannot use it and must keep books (ZPD art. 82(1) covers only trades and agriculture or forestry). Free professions include health professionals, vets, lawyers, notaries, auditors, engineers, architects, tax advisers, interpreters, translators, lecturers, journalists, artists and sportspeople (art. 29(2); Tax Administration, Obrtnici paušalisti). |
| **Obrt on books** (sole trader, real books) | Receipts above EUR 60,000, high real costs, or the client wants to be in VAT | PIT at the local lower and higher rates on actual income after business expenses and the allowance (ZPD art. 19, 30 to 33). Contributions on a fixed monthly base of EUR 1,295.45 for a trade (EUR 2,192.30 for a free profession) in 2026, not on actual profit (Contributions Act art. 65, 66(1); 2026 Bases Order art. 6). Exception: where the obrt is a second activity next to employment or another insurance basis, contributions are on the year's actual income at pension 10% (or 7.5% Pillar I plus 2.5% Pillar II) and health 7.5%, with the annual base capped at EUR 15,545.40 for 2026 (Contributions Act art. 7 point 6, 13(3), 14(2), 17(2), 185(1), 186(5); 2026 Bases Order art. 12); see [croatia-social-contributions](croatia-social-contributions.md). | Full bookkeeping; DOH return by the end of February. |
| **d.o.o.** (limited company) | Profit is high and largely kept in the business, or the client needs limited liability | Profit tax 10% or 18% (Profit Tax Act art. 28), then 12% on dividends paid to individuals (ZPD art. 70(19)). A board member with no employment contract pays contributions on EUR 1,993 a month in 2026 (2026 Bases Order art. 7). | Accounts, FINA filings and possibly audit; a second layer of tax on what is paid out. |

**Paušalni bands for 2026.** The deemed income is set by the year's total receipts (Paušalni Ordinance art. 3(1)); tax is 12% of it (art. 4(1)). The Ordinance sets the bands and deemed income; the Tax Administration page Obrtnici paušalisti prints the same bands with the 12% tax, and the rows below link it.

| Annual receipts (EUR) | Deemed income (EUR) | Annual tax at 12% (EUR) | Source |
| --- | --- | --- | --- |
| up to 11,300.00 | 1,695.00 | 203.40 | https://porezna-uprava.gov.hr/hr/obrtnici-pausalisti/4564 |
| 11,300.01 to 15,300.00 | 2,295.00 | 275.40 | same |
| 15,300.01 to 19,900.00 | 2,985.00 | 358.20 | same |
| 19,900.01 to 30,600.00 | 4,590.00 | 550.80 | same |
| 30,600.01 to 40,000.00 | 6,000.00 | 720.00 | same |
| 40,000.01 to 50,000.00 | 7,500.00 | 900.00 | same |
| 50,000.01 to 60,000.00 | 9,000.00 | 1,080.00 | same |

A paušalist working in the City of Vukovar, in a local unit in development group I or on a group I island pays 25% of this tax (Ordinance art. 5). Contributions for a paušalist insured on that basis are, a month in 2026, EUR 119.58 Pillar I, EUR 39.86 Pillar II and EUR 131.54 health: EUR 3,491.76 a year in all (Tax Administration, Obrtnici paušalisti).

**Tipping points to flag for the reviewer:**
- **Approaching EUR 60,000.** A paušalist whose receipts pass the VAT limit loses the regime: income is lump-sum only to the end of the month in which the limit is passed (unless that month is December), then it is taxed on books (ZPD art. 82(8) to (10)), and VAT registration follows (VAT Act art. 90(1)). Plan the year's invoicing with the client, but never by hiding or splitting receipts (see Step 7).
- **Real costs above the deemed margin.** The deemed income is 15% of the top of each band (85% deemed costs, Ordinance art. 3(1)). Where real costs plus contributions are higher, books may be cheaper; model both.
- **Profit consistently above EUR 60,000 and largely kept in the business.** In an obrt on books the part of the annual base above EUR 60,000 is taxed at the higher local rate (default 30%, up to 33% in Zagreb). In a d.o.o. with revenue up to EUR 1,000,000, profit kept in the company is taxed at 10%; paid out, EUR 100 of profit bears EUR 10 of profit tax and EUR 10.80 of dividend tax (12% of EUR 90), EUR 20.80 in all. **AUDIT FLASH POINT**: incorporating purely for tax, without commercial substance, can be challenged under OPZ art. 12.a.

### Step 3. Income splitting and structuring

| Strategy | Detail | Source |
| --- | --- | --- |
| Employ a spouse or family member | Genuine, documented, market-rate work. Salary and the contributions on it are a business expense of an obrt on books (ZPD art. 32(8)) and are taxed in the family member's hands, where his or her own EUR 600 monthly allowance applies (art. 14(1)). | https://porezna-uprava.gov.hr/Propisi/Propis/zakon-o-porezu-na-dohodak-redakcijski-procisceni-tekst/3 |
| Dependants on the allowance | Each dependant raises the monthly allowance: close family member and first child EUR 300, second child EUR 420, third child EUR 600 (art. 14(3)). A dependant whose own income is above EUR 3,600 a year (computed: six times the EUR 600 monthly allowance) does not count (art. 17(1); see [croatia-income-tax](croatia-income-tax.md)). Make sure the employer applies them, or claim them with the Tax Administration by the end of February for the previous year (art. 53(1)). | same |
| Place of residence | The rates are those of the local unit of domicile or habitual abode (art. 1(2)), and they differ inside the legal ranges (art. 19.a). A genuine move to a lower-rate unit lowers the tax; a paper address does not. | same |
| d.o.o. salary vs dividend mix | A director's salary is deductible for profit tax but bears contributions and PIT at the local rates; dividends bear 12% after profit tax. Model both for the client's numbers. | same |

### Step 4. Deductions most people miss (obrt on books)

*(A paušalni obrt cannot deduct real expenses. This step is for an obrt on books; a d.o.o. follows the Profit Tax Act, see [hr-corporate-income-tax](hr-corporate-income-tax.md).)*

An obrt on books deducts all outflows made to earn, secure and keep business receipts that are directly linked to the activity (ZPD art. 32(1)); costs not directly linked are not deductible (art. 33(3)).

| Deduction | Note |
| --- | --- |
| Home office share | Business-use share of rent, utilities and internet, documented, under the direct-link test of art. 32(1). |
| Chamber and professional body fees | Directly linked to the activity (art. 32(1)). |
| Training and CPD | Courses and conferences for the current activity (art. 32(1)). |
| Software and SaaS | Recurring business subscriptions (art. 32(1)). |
| Bank and payment-processor fees | Business account, card and payment-platform fees (art. 32(1)). |
| Business insurance | Including professional indemnity (art. 32(1)); car insurance is deductible in full (art. 33(2)). |
| Mandatory contributions | Contributions paid are a business expense (art. 32(6)). Check that Pillar I and Pillar II are both applied correctly. |
| Voluntary pension premiums | Premiums to a Croatian voluntary pension fund for employees and for the owner himself are a business expense up to the tax-free amount: EUR 67 a month, EUR 804 a year (art. 32(11), art. 9 point 18). |

Watch the limits: 50% of representation (hospitality, gifts, holidays, sport) and 50% of passenger car and other personal transport costs, where no benefit in kind is taxed, are not deductible (art. 33(1) points 1 and 5).

### Step 5. Reliefs and credits

| Relief | Detail |
| --- | --- |
| **Basic personal allowance** | EUR 600 a month, EUR 7,200 a year (ZPD art. 14(1)). |
| **Dependants** | Coefficients 0.5 / 0.5 / 0.7 / 1.0 x EUR 600 for a dependent close family member and the first, second and third child: EUR 300 / 300 / 420 / 600 a month (art. 14(3)). |
| **Youth relief** | On salary only: up to age 25, the tax on the part of the base taxed at the lower rate is cut by 100%; ages 26 to 30, by 50% (art. 46(2)). It covers the whole year in which the age is reached (art. 46(8)). It does not apply to obrt income. |
| **Returnee relief** | Croatian citizens resident in Croatia who lived abroad without a break for at least two years, and were not posted abroad by a Croatian employer, have the tax on their salary cut by 100% for five years (art. 46(3)), counted from 1 January of the year the conditions are met (art. 46(5)). It replaces the youth and assisted-area reliefs (art. 46(9)). **AUDIT FLASH POINT**: confirm the two years abroad from the residence records and that the income is salary. |
| **Assisted areas and Vukovar** | A taxpayer with domicile and residence in a group I assisted local unit or in Vukovar has the tax on pension or on other employment income cut by 50% (art. 46(1)). A paušalist working there pays 25% of the lump-sum tax (Paušalni Ordinance art. 5). A company working there with more than five permanent employees, more than half living in those areas, pays no profit tax in Vukovar and half the rate in group I units, within de minimis aid limits (Profit Tax Act art. 28.a). |

### Step 6. Capital allowances

- **Timing.** Depreciation starts on the first day of the month after the asset is put into use (Profit Tax Act art. 12(8)). An asset put into use in December gives no depreciation for that year; one in use by November gives one month. Plan purchases accordingly (obrt on books and d.o.o.).
- **Rates.** Straight line, asset by asset, at no more than: buildings and ships over 1,000 GRT 5%; basic herd and passenger cars 20%; intangibles, equipment, vehicles other than cars and machinery 25%; computers, hardware, software, mobile phones and network equipment 50%; other assets 10% (art. 12(1), (2), (5)). The rates may be doubled (art. 12(6)). An obrt on books uses the same rates (ZPD art. 32(9)).
- **Low-value items.** Only items costing more than EUR 665 each and lasting more than a year are long-term assets (Profit Tax Act art. 12(3)). Cheaper items are not depreciated; they are expensed as bought (ZPD art. 32(3) for an obrt).
- **Cars.** Depreciation on a passenger car counts only up to EUR 54,000 of cost per car, unless the car is used only in a registered rental or transport business (Profit Tax Act art. 12(13)).

### Step 7. Red lines (do not cross)

- **Substance over form.** Tax facts are set by their economic substance (OPZ art. 11(1)). A sham transaction is taxed as the transaction it hides (art. 12).
- **Use of tax advantages against the purpose of the law** (OPZ art. 12.a(1)). Three named cases:
  1. A payer has work with the features of employment done through another arrangement or a lower-taxed business form. The worker is then taxed as an employee and the payer is liable as guarantor (art. 12.a(1) point 1, (2)). **AUDIT FLASH POINT**: a paušalni obrt with one client and employer-like control.
  2. A business keeps changing its form, or uses a new form for each contract, to get lower rates or avoid obligations (point 2).
  3. Related companies used only to get a lower rate (point 3). For points 2 and 3 the person who actually runs all the companies is liable, and the companies are guarantors (art. 12.a(4)).
- **Incorporation or splitting purely for tax.** Setting up a d.o.o., or splitting one business across several obrti, purely to stay under EUR 60,000 or reach lower rates, without a genuine commercial purpose, falls under the cases above. **AUDIT FLASH POINT**.
- **Taking company assets privately.** When an owner withdraws assets or uses company services privately, the company withholds income tax at 36% on that benefit (ZPD art. 70(2)). Never treat private spending through a d.o.o. as a saving.
- **Returnee, youth and assisted-area reliefs.** Never claim them without checking the statutory conditions and the type of income.

## Boundary and exception table

| Situation | Effect | Law |
|---|---|---|
| Free profession (art. 29(2) list) | Cannot be paušalist; must keep books | ZPD art. 82(1), 29(2) |
| Paušalist passes EUR 60,000 in a month other than December | Lump-sum to the end of that month, then books; VAT registration | ZPD art. 82(8) to (10); VAT Act art. 90(1) |
| Paušalist in Vukovar, group I unit or group I island | Pays 25% of the lump-sum tax | Paušalni Ordinance art. 5 |
| Obrt as a second activity | Contributions on actual income, annual cap EUR 15,545.40 | Contributions Act art. 185(1), 186(5); 2026 Bases Order art. 12 |
| Asset put into use in December | No depreciation that year | Profit Tax Act art. 12(8) |
| Passenger car used only in a registered rental or transport business | EUR 54,000 depreciation cap does not apply | Profit Tax Act art. 12(13) |
| Returnee relief applies | Replaces the youth and assisted-area reliefs | ZPD art. 46(9) |
| Youth relief | Salary only, not obrt income | ZPD art. 46(2) |

## Worked cases

**Case 1. Decision: paušalni obrt or obrt on books (2026, default local rates 20% / 30%).** A sole trader in a trade (not a free profession), only insured on this basis, has receipts of EUR 40,000 and real costs of EUR 10,000.
- As a paušalist: tax EUR 720 plus contributions EUR 3,491.76, so EUR 4,211.76 in all.
- On books: contributions are EUR 472.84 a month (36.5% of EUR 1,295.45), EUR 5,674.08 a year, and are a business expense (ZPD art. 32(6)). Income is EUR 40,000 - 10,000 - 5,674.08 = EUR 24,325.92. After the EUR 7,200 annual allowance the base is EUR 17,125.92, taxed at 20%: EUR 3,425.18. Tax and contributions together are EUR 9,099.26.
- At these numbers the paušalni obrt costs EUR 4,887.50 less. Books win only when real costs are high enough to close that gap.

```oa-check
name: Croatia 2026, receipts EUR 40,000, costs EUR 10,000, paušal vs books at default 20%
inputs:
  receipts: 40000
  costs: 10000
  pausal_tax: 720
  pausal_contrib_year: 3491.76
  base_month: 1295.45
  allowance_year: 7200
steps:
  - pausal_total: pausal_tax + pausal_contrib_year
  - contrib_month: round(base_month * 0.365, 2)
  - contrib_year: contrib_month * 12
  - income: receipts - costs - contrib_year
  - base: income - allowance_year
  - books_tax: round(min(base, 60000) * 0.20 + max(base - 60000, 0) * 0.30, 2)
  - books_total: books_tax + contrib_year
  - saving_pausal: books_total - pausal_total
expected:
  pausal_total: 4211.76
  contrib_month: 472.84
  contrib_year: 5674.08
  income: 24325.92
  base: 17125.92
  books_tax: 3425.18
  books_total: 9099.26
  saving_pausal: 4887.50
```

**Case 2. Decision: profit kept in a d.o.o. or taken out (revenue under EUR 1,000,000).** A d.o.o. makes EUR 100,000 of taxable profit. Profit tax at 10% is EUR 10,000 (Profit Tax Act art. 28). If the whole after-tax profit of EUR 90,000 is paid as a dividend, 12% is withheld: EUR 10,800 (ZPD art. 70(19)), EUR 20,800 in all. If the profit is kept, only EUR 10,000 is paid now. For comparison, the same EUR 100,000 as obrt income at default rates, after the EUR 7,200 allowance, is taxed EUR 12,000 + EUR 9,840 = EUR 21,840 (art. 19, 19.a(5)). These are tax figures only: contributions differ by regime (obrt on books on its fixed base; a board member without employment contract on EUR 1,993 a month) and must be added before deciding. Keeping profit in the company is where the d.o.o. clearly wins; paying it all out narrows the gap.

```oa-check
name: Croatia 2026, profit EUR 100,000, d.o.o. retained vs paid out vs obrt tax at default rates
inputs:
  profit: 100000
  allowance_year: 7200
steps:
  - cit: profit * 0.10
  - dividend_tax: (profit - cit) * 0.12
  - doo_paid_out: cit + dividend_tax
  - obrt_base: profit - allowance_year
  - obrt_tax: min(obrt_base, 60000) * 0.20 + max(obrt_base - 60000, 0) * 0.30
expected:
  cit: 10000.00
  dividend_tax: 10800.00
  doo_paid_out: 20800.00
  obrt_base: 92800.00
  obrt_tax: 21840.00
```

## When to refuse or refer

- **Hiding income / splitting business without substance**: NEVER advise staying paušalni by hiding income or splitting one business across related obrti without substance.
- **Incorporation without substance warning**: NEVER present incorporation as a tax play without the commercial-substance warning.
- **Youth/returnee relief without eligibility check**: NEVER apply the youth, returnee or assisted-area relief without confirming eligibility for the specific income type.
- **Contradicting other skill figures**: NEVER contradict the rates and thresholds in [croatia-income-tax](croatia-income-tax.md), [hr-corporate-income-tax](hr-corporate-income-tax.md) or [croatia-social-contributions](croatia-social-contributions.md).
- **Presenting unconfirmed items as confirmed**: NEVER present an item on the "Not yet confirmed" line below as confirmed.
- **Definitive advice without routing to adviser**: NEVER present optimisation suggestions as definitive advice; always route to a licensed Croatian tax adviser.

## Filing and payment

- Paušalist: tax paid quarterly by the last day of each quarter (Paušalni Ordinance art. 6(1)); annual report PO-SD within 15 days after the year ends, so by 15 January 2027 for 2026, with any balance paid the same day (ZPD art. 82(6)).
- Obrt on books: DOH return by the end of February (ZPD art. 50(2)); contributions by the 15th of the month for the month before (Contributions Act art. 67, 71). Dependants not applied by the employer are claimed by the end of February for the previous year (ZPD art. 53(1)).
- d.o.o.: PD return and payment within four months of the year end (Profit Tax Act art. 35); see [hr-corporate-income-tax](hr-corporate-income-tax.md).

## Completion checklist

- Eligibility for paušal checked against the free-profession list.
- Both regimes modelled with contributions, not tax alone.
- The client's local unit rates used, not the defaults, where a decision exists.
- Reliefs checked for income type and conditions.
- Every suggestion screened against OPZ art. 11, 12 and 12.a.

## Sources

| Source | URL | Read on |
|---|---|---|
| Zakon o porezu na dohodak, consolidated text NN 115/16 to 152/24, in force from 1 January 2025 (Tax Administration register, node 3) (art. 1, 9, 14, 17, 19, 19.a, 29, 32, 33, 46, 50, 53, 70, 82) | https://porezna-uprava.gov.hr/Propisi/Propis/zakon-o-porezu-na-dohodak-redakcijski-procisceni-tekst/3 | 2026-10-30; art. 9, 14, 17, 46, 70, 82 re-read 2026-11-17 |
| Pravilnik o paušalnom oporezivanju samostalnih djelatnosti, consolidated text NN 1/20 to 16/25 (register, node 5) (art. 2 to 6) | https://porezna-uprava.gov.hr/Propisi/Propis/pravilnik-o-pausalnom-oporezivanju-samostalnih-djelatnosti-redakcijski-procisceni-tekst/5 | 2026-10-30; art. 3 to 6 re-read 2026-11-17 |
| Zakon o porezu na dobit, consolidated text NN 177/04 to 151/25 (register, node 1641) (art. 12, 28, 28.a, 35) | https://porezna-uprava.gov.hr/Propisi/Propis/zakon-o-porezu-na-dobit-redakcijski-procisceni-tekst/1641 | 2026-10-30; art. 12, 28.a re-read 2026-11-17 |
| Zakon o porezu na dodanu vrijednost, NN 73/13 to 48/26 (register, node 1651) (art. 90) | https://porezna-uprava.gov.hr/Propisi/Propis/zakon-o-porezu-na-dodanu-vrijednost/1651 | 2026-10-30; re-read 2026-11-17 |
| Zakon o doprinosima, consolidated text (register, node 3119) (art. 7, 13, 14, 17, 65, 66, 67, 70, 71, 185, 186) | https://porezna-uprava.gov.hr/Propisi/Propis/zakon-o-doprinosima-redakcijski-procisceni-tekst/3119 | 2026-10-30; art. 67, 71 re-read 2026-11-17 |
| Naredba o iznosima osnovica za obračun doprinosa za obvezna osiguranja za 2026. godinu, NN 150/25 (register, node 5778) (art. 6, 7, 12) | https://porezna-uprava.gov.hr/Propisi/Propis/naredba-o-iznosima-osnovica-za-obracun-doprinosa-za-obvezna-osiguranja-za-2026-godinu/5778 | 2026-10-30; re-read 2026-11-17 |
| Opći porezni zakon, consolidated text NN 115/16 to 151/25, in force from 1 January 2026 (register, node 3155) (art. 11, 12, 12.a) | https://porezna-uprava.gov.hr/Propisi/Propis/opci-porezni-zakon-redakcijski-procisceni-tekst/3155 | 2026-10-30; art. 12.a re-read 2026-11-17 |
| Tax Administration, Obrtnici paušalisti (2026 bands and contributions; free professions excluded) | https://porezna-uprava.gov.hr/hr/obrtnici-pausalisti/4564 | 2026-10-30; contribution figures re-read 2026-11-17 |

Not yet confirmed: no statutory method for apportioning home-office costs was found (only the direct-link test of ZPD art. 32(1)); the 2026 rate chosen by each local unit (see croatia-income-tax).

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-17. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `croatia-tax-optimization` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/croatia-tax-optimization. If neither is available, confirm every figure against the official source pages cited above before relying on it.
