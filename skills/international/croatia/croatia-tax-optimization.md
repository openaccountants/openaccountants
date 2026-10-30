---
name: croatia-tax-optimization
description: "Use this skill whenever asked about lowering tax legally in Croatia for tax year 2026: tax planning, saving tax, allowances or deductions a client might be missing, or strategies for a self-employed person or small business. Covers the choice between a lump-sum paušalni obrt (seven 2026 bands up to EUR 60,000, 12% tax, EUR 797.20 contribution base), a trade on books and a d.o.o. (10% or 18% profit tax, then 12% on dividends), employing family, dependants on the allowance, the youth, returnee and assisted-area reliefs, voluntary pension premiums, depreciation timing, and the anti-avoidance lines in the General Tax Act. Trigger on: reduce tax Croatia, paušalni obrt, paušalist, lump-sum tax, obrt vs d.o.o., save tax Croatia, tax planning Croatia, porezno planiranje, returnee tax relief, young person tax relief. Out of scope: croatia-income-tax, hr-corporate-income-tax, croatia-social-contributions, croatia-vat-return, hr-cross-border."
version: 0.2
jurisdiction: HR
tax_year: 2026
last_updated: 2026-10-30
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: tax-optimization
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Croatia Tax Optimization

## Croatia Tax Optimization Skill v0.2

**Tax year 2026. Every figure below is taken from the consolidated texts in the Tax Administration's register of regulations, read on 2026-10-30 (see Sources). Figures must agree with [croatia-income-tax](croatia-income-tax.md), [hr-corporate-income-tax](hr-corporate-income-tax.md) and [croatia-social-contributions](croatia-social-contributions.md); if they ever differ, those skills win. No licensed Croatian tax adviser has signed this skill off. Every suggestion must be reviewed by a credentialed professional; aggressive positions are never advised.**

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Croatia (Republika Hrvatska) |
| Tax year | 2026 (calendar year) |
| Currency | EUR |
| Key optimisation levers | Regime choice (paušalni obrt / obrt on books / d.o.o.); personal allowance and dependants; youth, returnee and assisted-area reliefs; voluntary pension premiums; depreciation timing |
| PIT rates (2026) | Lower rate on the annual base up to EUR 60,000, higher rate above (Income Tax Act, ZPD, art. 19). Each local unit sets its rates inside ranges: lower 15% to 20%/21%/22%/23% and higher 25% to 30%/31%/32%/33% depending on the type of unit, Zagreb having the widest range; default 20% / 30% where no decision was made (art. 19.a(2), (5)). The rate follows the taxpayer's domicile or habitual abode (art. 1(2)). |
| Profit tax (d.o.o.) | 10% if revenue in the period is up to EUR 1,000,000; 18% above (Profit Tax Act art. 28). |
| Dividends to individuals | 12% withheld (ZPD art. 70(19)). |
| VAT registration threshold (2026) | EUR 60,000 of domestic turnover in the year (VAT Act art. 90(1)). |
| Anti-avoidance | Substance over form (General Tax Act, OPZ, art. 11(1)); sham transactions (art. 12); use of tax advantages against the purpose of the law, including disguised employment and frequent changes of business form (art. 12.a). |

> **The single biggest Croatian lever is REGIME CHOICE.** For a trade with receipts up to EUR 60,000 a year and low real costs, the paušalni (lump-sum) obrt usually pays far less than an obrt on books or a d.o.o. Confirm eligibility before anything else: free professions cannot use it.

## Section 2 -- Regime Election (the core decision)

**Regime Election**

| Regime | Best when | Tax treatment | Trade-offs |
| --- | --- | --- | --- |
| **Paušalni obrt** (lump-sum sole trader) | Receipts up to EUR 60,000; low real costs; trades (obrt) and agriculture or forestry | Income tax of 12% on a deemed income fixed by the band the year's receipts fall in (ZPD art. 82(1), (6); Paušalni Ordinance art. 3(1), 4(1)), paid quarterly by the last day of each quarter (Ordinance art. 6(1)). Contributions on a fixed monthly base of EUR 797.20 in 2026 (Contributions Act art. 70; 2026 Bases Order art. 7). Keeps only a sales book (ZPD art. 82(4)). Not in VAT. | Real costs cannot be deducted; capped at the VAT limit; free professions (for example doctors, vets, lawyers, sportspeople) must keep books instead (Tax Administration, Obrtnici paušalisti). |
| **Obrt on books** (sole trader, real books) | Receipts above EUR 60,000, high real costs, or the client wants to be in VAT | PIT at the local lower and higher rates on actual income after business expenses and the allowance (ZPD art. 19, 30 to 33). Contributions on a fixed monthly base of EUR 1,295.45 for a trade (EUR 2,192.30 for a free profession) in 2026, not on actual profit (Contributions Act art. 66(1); 2026 Bases Order art. 6). | Full bookkeeping; DOH return by the end of February. |
| **d.o.o.** (limited company) | Profit is high and largely kept in the business, or the client needs limited liability | Profit tax 10% or 18% (Profit Tax Act art. 28), then 12% on dividends paid to individuals (ZPD art. 70(19)). A board member with no employment contract pays contributions on EUR 1,993 a month in 2026 (2026 Bases Order art. 7). | Accounts, FINA filings and possibly audit; a second layer of tax on what is paid out. |

**Paušalni bands for 2026.** The deemed income is set by the year's total receipts (Paušalni Ordinance art. 3(1)); tax is 12% of it (art. 4(1)).

| Annual receipts (EUR) | Deemed income (EUR) | Annual tax at 12% (EUR) |
| --- | --- | --- |
| up to 11,300.00 | 1,695.00 | 203.40 |
| 11,300.01 to 15,300.00 | 2,295.00 | 275.40 |
| 15,300.01 to 19,900.00 | 2,985.00 | 358.20 |
| 19,900.01 to 30,600.00 | 4,590.00 | 550.80 |
| 30,600.01 to 40,000.00 | 6,000.00 | 720.00 |
| 40,000.01 to 50,000.00 | 7,500.00 | 900.00 |
| 50,000.01 to 60,000.00 | 9,000.00 | 1,080.00 |

A paušalist working in the City of Vukovar, in a local unit in development group I or on a group I island pays 25% of this tax (Ordinance art. 5). Contributions for a paušalist insured on that basis are, a month in 2026, EUR 119.58 Pillar I, EUR 39.86 Pillar II and EUR 131.54 health: EUR 3,491.76 a year in all (Tax Administration, Obrtnici paušalisti).

**Illustration (2026, default local rates 20% / 30%).** A sole trader has receipts of EUR 40,000 and real costs of EUR 10,000.
- As a paušalist: tax EUR 720 plus contributions EUR 3,491.76, so EUR 4,211.76 in all.
- On books: contributions are EUR 472.84 a month (36.5% of EUR 1,295.45), EUR 5,674.08 a year, and are a business expense (ZPD art. 32(6)). Income is EUR 40,000 - 10,000 - 5,674.08 = EUR 24,325.92. After the EUR 7,200 annual allowance the base is EUR 17,125.92, taxed at 20%: EUR 3,425.18. Tax and contributions together are EUR 9,099.26.
- At these numbers the paušalni obrt costs EUR 4,887.50 less. Books win only when real costs are high enough to close that gap.

**Tipping points to flag for the reviewer:**
- **Approaching EUR 60,000.** A paušalist whose receipts pass the VAT limit loses the regime: income is lump-sum only to the end of the month in which the limit is passed, then it is taxed on books (ZPD art. 82(8) to (10)), and VAT registration follows (VAT Act art. 90(1)). Plan the year's invoicing with the client, but never by hiding or splitting receipts (see Section 7).
- **Real costs above the deemed margin.** The deemed income is 15% of the top of each band (85% deemed costs, Ordinance art. 3(1)). Where real costs plus contributions are higher, books may be cheaper; model both.
- **Profit consistently above EUR 60,000 and largely kept in the business.** In an obrt on books the part of the annual base above EUR 60,000 is taxed at the higher local rate (default 30%, up to 33% in Zagreb). In a d.o.o. with revenue up to EUR 1,000,000, profit kept in the company is taxed at 10%; paid out, EUR 100 of profit bears EUR 10 of profit tax and EUR 10.80 of dividend tax (12% of EUR 90), EUR 20.80 in all. **AUDIT FLASH POINT**: incorporating purely for tax, without commercial substance, can be challenged under OPZ art. 12.a.

## Section 3 -- Income Splitting & Structuring

**Income Splitting & Structuring**

| Strategy | Detail |
| --- | --- |
| Employ a spouse or family member | Genuine, documented, market-rate work. Salary and the contributions on it are a business expense of an obrt on books (ZPD art. 32(8)) and are taxed in the family member's hands, where his or her own EUR 600 monthly allowance applies (art. 14(1)). |
| Dependants on the allowance | Each dependant raises the monthly allowance: close family member and first child EUR 300, second child EUR 420, third child EUR 600 (art. 14(3)). A dependant whose own income is above EUR 3,600 a year does not count (art. 17(1); see [croatia-income-tax](croatia-income-tax.md)). Make sure the employer applies them, or claim them with the Tax Administration by the end of February for the previous year (art. 53(1)). |
| Place of residence | The rates are those of the local unit of domicile or habitual abode (art. 1(2)), and they differ inside the legal ranges (art. 19.a). A genuine move to a lower-rate unit lowers the tax; a paper address does not. |
| d.o.o. salary vs dividend mix | A director's salary is deductible for profit tax but bears contributions and PIT at the local rates; dividends bear 12% after profit tax. Model both for the client's numbers. |

## Section 4 -- Deductions Most People Miss (obrt on books)

*(A paušalni obrt cannot deduct real expenses. This section is for an obrt on books; a d.o.o. follows the Profit Tax Act, see [hr-corporate-income-tax](hr-corporate-income-tax.md).)*

An obrt on books deducts all outflows made to earn, secure and keep business receipts that are directly linked to the activity (ZPD art. 32(1)); costs not directly linked are not deductible (art. 33(3)).

**Deductions Most People Miss**

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

## Section 5 -- Reliefs & Credits

**Reliefs & Credits**

| Relief | Detail |
| --- | --- |
| **Basic personal allowance** | EUR 600 a month, EUR 7,200 a year (ZPD art. 14(1)). |
| **Dependants** | Coefficients 0.5 / 0.5 / 0.7 / 1.0 x EUR 600 for a dependent close family member and the first, second and third child: EUR 300 / 300 / 420 / 600 a month (art. 14(3)). |
| **Youth relief** | On salary only: up to age 25, the tax on the part of the base taxed at the lower rate is cut by 100%; ages 26 to 30, by 50% (art. 46(2)). It covers the whole year in which the age is reached (art. 46(8)). It does not apply to obrt income. |
| **Returnee relief** | Croatian citizens resident in Croatia who lived abroad without a break for at least two years, and were not posted abroad by a Croatian employer, have the tax on their salary cut by 100% for five years (art. 46(3)), counted from 1 January of the year the conditions are met (art. 46(5)). It replaces the youth and assisted-area reliefs (art. 46(9)). **AUDIT FLASH POINT**: confirm the two years abroad from the residence records and that the income is salary. |
| **Assisted areas and Vukovar** | A taxpayer with domicile and residence in a group I assisted local unit or in Vukovar has the tax on pension or on other employment income cut by 50% (art. 46(1)). A paušalist working there pays 25% of the lump-sum tax (Paušalni Ordinance art. 5). A company working there with more than five permanent employees, more than half living in those areas, pays no profit tax in Vukovar and half the rate in group I units, within de minimis aid limits (Profit Tax Act art. 28.a). |

## Section 6 -- Capital Allowances Optimization

- **Timing.** Depreciation starts on the first day of the month after the asset is put into use (Profit Tax Act art. 12(8)). An asset put into use in December gives no depreciation for that year; one in use by November gives one month. Plan purchases accordingly (obrt on books and d.o.o.).
- **Rates.** Straight line, asset by asset, at no more than: buildings and ships over 1,000 GRT 5%; basic herd and passenger cars 20%; intangibles, equipment, vehicles other than cars and machinery 25%; computers, hardware, software, mobile phones and network equipment 50%; other assets 10% (art. 12(1), (2), (5)). The rates may be doubled (art. 12(6)). An obrt on books uses the same rates (ZPD art. 32(9)).
- **Low-value items.** Only items costing more than EUR 665 each and lasting more than a year are long-term assets (Profit Tax Act art. 12(3)). Cheaper items are not depreciated; they are expensed as bought (ZPD art. 32(3) for an obrt).
- **Cars.** Depreciation on a passenger car counts only up to EUR 54,000 of cost per car, unless the car is used only in a registered rental or transport business (Profit Tax Act art. 12(13)).

## Section 7 -- Red Lines (do not cross)

- **Substance over form.** Tax facts are set by their economic substance (OPZ art. 11(1)). A sham transaction is taxed as the transaction it hides (art. 12).
- **Use of tax advantages against the purpose of the law** (OPZ art. 12.a(1)). Three named cases:
  1. A payer has work with the features of employment done through another arrangement or a lower-taxed business form. The worker is then taxed as an employee and the payer is liable as guarantor (art. 12.a(1) point 1, (2)). **AUDIT FLASH POINT**: a paušalni obrt with one client and employer-like control.
  2. A business keeps changing its form, or uses a new form for each contract, to get lower rates or avoid obligations (point 2).
  3. Related companies used only to get a lower rate (point 3). For points 2 and 3 the person who actually runs all the companies is liable, and the companies are guarantors (art. 12.a(4)).
- **Incorporation or splitting purely for tax.** Setting up a d.o.o., or splitting one business across several obrti, purely to stay under EUR 60,000 or reach lower rates, without a genuine commercial purpose, falls under the cases above. **AUDIT FLASH POINT**.
- **Taking company assets privately.** When an owner withdraws assets or uses company services privately, the company withholds income tax at 36% on that benefit (ZPD art. 70(2)). Never treat private spending through a d.o.o. as a saving.
- **Returnee, youth and assisted-area reliefs.** Never claim them without checking the statutory conditions and the type of income.

## PROHIBITIONS

- **Hiding income / splitting business without substance** -- NEVER advise staying paušalni by hiding income or splitting one business across related obrti without substance.
- **Incorporation without substance warning** -- NEVER present incorporation as a tax play without the commercial-substance warning.
- **Youth/returnee relief without eligibility check** -- NEVER apply the youth, returnee or assisted-area relief without confirming eligibility for the specific income type.
- **Contradicting other skill figures** -- NEVER contradict the rates and thresholds in [croatia-income-tax](croatia-income-tax.md), [hr-corporate-income-tax](hr-corporate-income-tax.md) or [croatia-social-contributions](croatia-social-contributions.md).
- **Presenting unconfirmed items as confirmed** -- NEVER present an item on the "Not yet confirmed" line below as confirmed.
- **Definitive advice without routing to adviser** -- NEVER present optimisation suggestions as definitive advice; always route to a licensed Croatian tax adviser.

## Sources

| Source | URL | Read on |
|---|---|---|
| Zakon o porezu na dohodak, consolidated text NN 115/16 to 152/24, in force from 1 January 2025 (Tax Administration register, node 3) (art. 1, 9, 14, 17, 19, 19.a, 32, 33, 46, 70, 82) | https://porezna-uprava.gov.hr/Propisi | 2026-10-30 |
| Pravilnik o paušalnom oporezivanju samostalnih djelatnosti, consolidated text NN 1/20 to 16/25 (register, node 5) (art. 2 to 6) | https://porezna-uprava.gov.hr/Propisi | 2026-10-30 |
| Zakon o porezu na dobit, consolidated text NN 177/04 to 151/25 (register, node 1641) (art. 12, 28, 28.a) | https://porezna-uprava.gov.hr/Propisi | 2026-10-30 |
| Zakon o porezu na dodanu vrijednost, NN 73/13 to 48/26 (register, node 1651) (art. 90) | https://porezna-uprava.gov.hr/Propisi | 2026-10-30 |
| Zakon o doprinosima, consolidated text (register, node 3119) (art. 13, 14, 17, 66, 70) | https://porezna-uprava.gov.hr/Propisi | 2026-10-30 |
| Naredba o iznosima osnovica za obračun doprinosa za obvezna osiguranja za 2026. godinu, NN 150/25 (register, node 5778) (art. 6, 7) | https://porezna-uprava.gov.hr/Propisi | 2026-10-30 |
| Opći porezni zakon, consolidated text NN 115/16 to 151/25, in force from 1 January 2026 (register, node 3155) (art. 11, 12, 12.a) | https://porezna-uprava.gov.hr/Propisi | 2026-10-30 |
| Tax Administration, Obrtnici paušalisti (2026 bands and contributions; free professions excluded) | https://porezna-uprava.gov.hr/hr/obrtnici-pausalisti/4564 | 2026-10-30 |

Not yet confirmed: no statutory method for apportioning home-office costs was found (only the direct-link test of ZPD art. 32(1)); the list of trades that may not use the paušalni regime beyond the free professions named by the Tax Administration; the 2026 rate chosen by each local unit (see croatia-income-tax).

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a licensed tax adviser in Croatia) before acting upon.

The most up-to-date version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

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
