---
name: north-macedonia-income-tax
description: "Use this skill for North Macedonia personal income tax for calendar year 2026. It covers resident and nonresident individuals, employment, sole traders and professionals, rent, dividends, interest, copyright income and ordinary capital gains. Trigger on Macedonian income tax, UJP, e-PDD, DLD-DB, tax allowance, self-employed tax, rental tax, foreign income or annual personal tax return. It explains category-specific bases, business adjustments, investment relief, advance payments, annual reconciliation and treaty-credit routing. Use the separate payroll and social-contributions skills to calculate insurance by insured group and wage period. This is a tier 2 skill, checked against the law, for preparing reviewable working papers; it does not carry a licensed accountant’s sign-off."
jurisdiction: MK
tax_year: 2026
last_updated: 2026-10-30
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
version: 0.3
---

# North Macedonia personal income tax v0.3

**Tax year: 2026. Checked against the law, tier 2.** Amounts are MKD unless stated otherwise. Professional review remains outstanding.

## Who this applies to

Residents pay PIT on domestic and foreign income. Residence follows a permanent home or residence in North Macedonia; presence for at least **183 days in any 12-month period** establishes residence under [PIT art. 5][pit]. Nonresidents pay on North Macedonia-source income under art. 7, subject to a particular treaty. Registered sole traders, farmers, craftspeople and independent professionals fall within arts. 6 and 19-20. Income received in kind is included (art. 3).

This skill covers ordinary PIT. Salary insurance is computed in `north-macedonia-social-contributions`, withholding in `north-macedonia-payroll`, company profit in `mk-corporate-income-tax`, and treaty procedures in `north-macedonia-cross-border`. Gambling operators are outside this computation. Unexplained wealth is assessed by UJP decision under arts. 76-78, not self-assessed: the base is the value of the assets less the proven funds used to acquire them, taxed at 70%.

## Rates, bands and thresholds

| Item | Amount | Tax year | Official provision |
|---|---|---|---|
| Ordinary PIT | 10% | 2026 | [PIT art. 11(1)][pit] |
| Games-of-chance income, separately classified | 15% | 2026 | [PIT art. 11(2)][pit] |
| First-year business PIT advance reference / base / tax | January-published net wage 45,961; 50% base 22,980.50; 10% advance 2,298.05 before accepted payment rounding | 2026 | [PIT art. 94(2)][pit]; [State Statistical Office, 21 January 2026 release][net-wage] |
| Unsupported business-loan interest fallback | Matching-maturity EURIBOR (FX) or SKIBOR (MKD), plus 1 percentage point | 2026 | [PIT art. 27(7)][pit] |
| Own-product agricultural sales boundary | 1,000,000; activity-registration and paid-tax-refund tests are separate | 2026 | [PIT arts. 45-46][pit] |
| Salary/pension reduction | 10,932 monthly; 131,184 published annual amount | 2026 | [PIT arts. 10, 17][pit]; [2026 ministerial publication][allowance] |
| Rental deemed costs | 10%; furnished residential/business premises 15% | 2026 | [PIT art. 53][pit] |
| Industrial-property rights deemed costs | 10% for original holder; inherited/transferred holder uses full receipt | 2026 | [PIT art. 50][pit] |
| Copyright deemed costs | 50%, 40%, 30% or 20%, by statutory work type | 2026 | [PIT art. 40][pit] |
| Business entertainment add-back | 90% | 2026 | [PIT art. 27(3)][pit] |
| Own/rented vehicle use and maintenance add-back | 50% | 2026 | [PIT art. 27(4)][pit] |
| Ordinary business expansion relief | 30% of qualifying investment, capped at 50% of the period's tax base; retain assets 5 years | 2026 | [PIT art. 28(1)-(4)][pit] |
| Qualifying capital-gain deemed costs | 10% | 2026 | [PIT art. 60(2)][pit] |
| Undeclared income of unproven origin (special UJP assessment) | 70% of the difference between asset value and proven funding | 2026 | [PIT arts. 76-78][pit] |
| Late-payment interest | 0.03% each day from day after original due date | 2026 | [Tax Procedure Law arts. 3, 123][procedure] |
| Late-filing surcharge | Up to 10% of the tax assessed by law | 2026 | [Tax Procedure Law art. 55][procedure] |

The annual salary reduction is restricted to the right actually used on salary, salary compensation and pension during advance assessment (art. 10(5)). Do not deduct the full annual publication from sole-trader profit or rent.

## The base

**Employment:** use gross salary and taxable benefits, less mandatory insurance and the month's salary reduction, with a nonnegative base (arts. 9, 14-17). Directors' fees and temporary personal services use their specific art. 16 base, not automatically the salary reduction. Use the payroll skill to distinguish them.

**Business:** start with total accounting revenue less accounting expenses (arts. 21-23). Include business costs supported by records, statutory depreciation and the trader's own compulsory pension, health and employment contributions and business public charges under arts. 24 and 26. Avoid deducting a contribution twice. Add back private/nonbusiness costs, fines, public-debt penalty interest, scholarships, disallowed vehicle interest, excessive loan interest, nonmarket related-party differences, 90% of entertainment, and 50% of own/rented vehicle operating costs; apply the other specific art. 27 limits to employee benefits and reimbursements. The personal reduction is not a business deduction. For borrowing interest under art. 27(7), use evidence of the comparable commercial-bank credit rate. If the taxpayer cannot substantiate compliance with that limit, deductible interest is capped at the matching-maturity EURIBOR rate for foreign-currency loans or SKIBOR for denar loans, plus one percentage point. Retain the applicable benchmark, currency, maturity, principal and interest-period calculation; do not use a guessed fixed borrowing rate.

Depreciate eligible assets using the [Decree arts. 2-7 and nomenclature][depreciation]: acquisition cost above **EUR 500 equivalent**, useful life beyond **one year**, straight-line, from the day becoming available for use. Deduction excludes revaluation above acquisition cost. The prescribed rate can increase by up to **50%** (art. 4), subject to consistency and the asset's remaining value. Retired unusable assets require UJP approval for full remaining-value write-off, requested by **31 January** next year (PIT art. 24).

Apply documented expansion relief after computing the adjusted base; ordinary relief is the lower of 30% of qualifying investment and 50% of that base. Eligible items are business-expansion property, plant, equipment, software and patents. Administrative furnishings and ordinary passenger cars do not qualify. Vehicles in the specific rental/taxi/driver-training/special-vehicle activities have the separate art. 28(2) rule. Disposal within the statutory retention period reverses relief with interest (art. 28).

**Business loss and annual reconciliation:** show the accounting loss and add-backs separately. [DLD-DB field 22 instructions][self-brochure] require a negative adjusted net result with a minus sign; leave the following business-tax fields blank. The [current prescribed DLD-GDP instructions p. 3][dld-gdp] transfer that same field 22 to annual business-income row 2. The annual form p. 2 aggregates income, less permitted deductions and the salary reduction actually used. Thus a current-year negative business result enters that annual reconciliation; it does not alter an employer's monthly salary withholding. Do not deduct own business insurance again: it is already expensed in field 22. Verify/correct UJP's populated return and request any resulting overpayment refund under [arts. 96-100, especially 100(4)-(5)][pit]. These are current-calendar-year mechanics under arts. 4 and 9. No general prior-year business-loss carryforward or carryback is authorised by these PIT provisions; do not import the corporate three-year loss rule or carry an unused negative annual base into another year.

**Other categories:** gross dividends and other distributions are taxable capital income; loan interest uses calculated interest (arts. 55-57). Tax on term-deposit interest is deferred until EU accession (art. 116), not a current blanket interest exemption. Rent uses gross receipts, including tenant-paid improvements for the landlord, less the applicable deemed costs; subletting deducts rent paid, rather than stacking both deductions (arts. 51-54). Copyright: 50% for specified sculpture/tapestry/ceramic/stained-glass work; 40% for the art/design/music/film categories listed in art. 40(2); 30% for scientific/professional/publicist and specified performing works; 20% for translations, lectures, popular performances and other works. Transferred copyright holders deduct only the agency/authorised-agent fees permitted by art. 41. Agricultural own-product sales have the separate **80%** deemed-cost rule in art. 44, not ordinary trader-profit treatment. Art. 45 requires registration of the activity by **15 January of the following year** where that taxpayer's total annual income exceeds **1,000,000**. Art. 46 separately permits refund of tax paid on own-product sales not exceeding **1,000,000**, provided there is no other taxable income apart from its specified free-production-input exceptions; other nontaxable income is permitted except income under art. 13. UJP uses confirmed annual returns and Ministry of Agriculture verification; refund is due by the end of the following year. Do not turn this conditional refund into a general exemption at source.

**Insurance and other income:** art. 3(1) lists eleven categories. Insurance income (arts. 68-70) is the premium for life, voluntary health or non-life insurance paid for the individual by a legal person or a self-employed payer; it is taxed at 10%. Other income (art. 71) is any income outside the first ten categories and not exempt under art. 12; it expressly includes useful solid-waste sales, income from e-commerce over the internet and internet marketing services. Use the ordinary 10% rate and the art. 87-88 calculation route where no domestic payer withholds.

**Capital gains:** sale/exchange proceeds less documented acquisition cost; inherited/gifted assets generally use the predecessor's cost (arts. 58-61). For securities and investment-fund units, **Gazette 274/2022 transitional arts. 21-22** apply this regime to assets acquired by the taxpayer, or the predecessor on inheritance/gift, **from 1 January 2023**, with chronological **FIFO** from the oldest to newest transaction. Separate pre-2023 acquisitions and retain predecessor lot dates; do not tax every portfolio sale under the post-2023 regime. Transitional art. 24 separately preserves the prior property-gift rules for the gifts it specifies. Art. 60(2)'s 10% deemed costs apply to securities, investment-fund units, equity interests, other movable property, and a property occupied for at least one year before sale; do not apply this to every asset. Property sellers can request documented investment costs instead where art. 60(3) applies. Domestic exchange-security losses offset that category's domestic gains in the same year; domestic fund-unit losses offset that fund-unit category's gains in the same year (art. 62). Do not net unrelated categories. Check art. 63 property exemptions, including sale after five years or residence for one year followed by sale after three years, and the specific inheritance/gift/divorce rules. Arts. 63-a to 63-c contain distinct securities and fund exemptions; no general two-year holding exemption is asserted here.

**Lump-sum assessment:** apply to UJP, not a self-selected flat turnover amount. Art. 29 excludes specified trading/catering/commission activities, more than one employee besides the taxpayer, outside investors and prior net income above two annual average gross salaries. Apply by year-end before the covered year, or within 15 days of registration/before starting. Use UJP's assessed net income, with the ordinary rate.

## Deadlines and filing

Register the activity with its competent register and obtain an EDB through Central Registry/UJP; keep registration data current ([PIT art. 20][pit]; [UJP registration instructions][self-brochure]). Register separately for VAT where the VAT skill requires it. Cessation requires closing the activity registration and filing for the actual operating period under art. 97(2); do not abandon outstanding returns or balances.

- Domestic payers withhold on covered payments and submit the electronic calculation before payment; salary uses monthly MPIN by the **10th of the following month** (arts. 80, 84-85). Withholding is paid on each payment (art. 92).
- Self-assessed e-PDD income generally has a calculation due by the **10th**, payment by the **15th of the following month** (arts. 87-88, 93). Rental contracts and sale events have their own art. 88 triggers. Foreign salary/pension with foreign tax paid uses the **31 March next-year** evidence/calculation deadline in art. 88(2).
- Business advances: one twelfth of prior annual tax monthly; January and February use the year before the preceding year. First-year advances use **50% of the average net wage published in January** as the monthly base. The [21 January 2026 statistical release][net-wage] reports **45,961** for November 2025, so the 2026 monthly first-year PIT advance base is **22,980.50** and analytical tax at 10% is **2,298.05**, before accepted payment rounding. This net-wage parameter is distinct from the gross-wage insurance reference. Pay by the **15th of the next month** (arts. 90, 94); request revision for materially changed conditions (art. 91).
- Business books, form B and **DLD-DB**: submit by **15 March 2027** for 2026; pay the balance within **15 days after the statutory filing deadline** (arts. 97, 100(1)).
- For securities/fund gains covered by domestic intermediary reporting, the Central Securities Depository and fund managers report by **15 January** of the next year (art. 85-a); UJP assesses by **15 February** (art. 91-a), and assessed tax is paid within **15 days of service** (art. 93(4)). Preserve FIFO lot data and do not replace this assessment route with a general 10th/15th monthly filing. Foreign-source receipts outside this reporting route must still be tested under arts. 87-88's foreign-income obligations.
- UJP supplies **DLD-GDP** by **30 April 2027**; confirm/correct by **31 May 2027**, otherwise deemed confirmed. Pay annual PIT by **30 June 2027**; an assessment difference is due within **15 days of service**. Request overpayment refund in the annual return, otherwise carried as an advance; statutory refund period **60 days** (arts. 96-100).

Convert foreign-currency income using the National Bank middle rate on the income date (art. 93(2)). Preserve advance payments by category for reconciliation; an annual return does not replace monthly obligations. Dates are statutory; apply the Tax Procedure Law's nonworking-day rule where relevant.

## Penalties and interest

[PIT art. 107][pit]: late business calculations/balances, absent/inaccurate books or failure to retain books attract **EUR 100-250 equivalent** for sole traders/self-employed; failure by an ordinary individual to submit the art. 88 calculation attracts **EUR 50-250**. Art. 108 payer failures to calculate/pay or comply with art. 85: legal persons micro **EUR 300-1,000**, small **600-2,000**, medium **1,800-6,000**, large **3,000-10,000**, with separate responsible-person fines. These are offence-specific ranges, not a daily surcharge. A late return can also carry a separate late-filing surcharge of up to **10%** of the tax ([Tax Procedure Law art. 55][procedure]). UJP can assess tax for **5 years** from the end of the year in which the taxable event occurred, **10 years** for tax evasion, with an absolute 10-year cut-off (art. 110); collection of assessed tax lapses **10 years** after the year it fell due (art. 122-a). Interest is debt × 0.0003 × overdue days under [Tax Procedure Law art. 123][procedure]; art. 123-a's temporary reduced rate ended in 2021.

## Cross-border points

Classify residence before source and treaty. Foreign tax credit under [PIT art. 8(4)][pit] is limited to domestic tax on that income; obtain evidence of foreign tax paid. A foreign bank account does not exclude income. Nonresident treaty relief requires the prescribed foreign-authority/UJP-certified forms or approval under arts. 81-83 and 89-a. Use the cross-border skill for residence evidence, treaty application dates and payment procedures; a move abroad does not itself establish a zero liability.

## Two worked examples that recompute

**Simple: unfurnished property rental.** A resident receives gross rent of 240,000 for 2026. Art. 53's 10% deemed costs give a base of 216,000; art. 11 tax is 21,600. No salary reduction is used.

```oa-check
name: MK 2026 unfurnished rent
inputs:
  rent: 240000
steps:
  - costs: rent * 0.10
  - base: rent - costs
  - tax: base * 0.10
expected:
  costs: 24000
  base: 216000
  tax: 21600
```

**Edge: business add-backs and capped investment relief.** Accounting profit 800,000 already includes 100,000 entertainment and 60,000 vehicle maintenance; own mandatory insurance has already been expensed. Add back 90,000 and 30,000. A documented qualifying expansion investment of 2,000,000 produces 600,000 potential relief, capped at half the 920,000 base: 460,000. Tax is 46,000, with 40,000 advances leaving 6,000. No personal reduction, duplicate contribution deduction or loss relief is used (arts. 21, 26-28, 100).

```oa-check
name: MK 2026 business investment cap
inputs:
  profit: 800000
  entertainment: 100000
  car_costs: 60000
  investment: 2000000
  advances: 40000
steps:
  - adjusted: profit + entertainment * 0.90 + car_costs * 0.50
  - relief: min(investment * 0.30, adjusted * 0.50)
  - base: adjusted - relief
  - tax: base * 0.10
  - balance: tax - advances
expected:
  adjusted: 920000
  relief: 460000
  base: 460000
  tax: 46000
  balance: 6000
```

## Ask the client first

- Where are the permanent home and days of presence, and is another state claiming residence?
- Which income categories, payers, foreign taxes and withholding certificates exist, including securities/fund lot dates and predecessor acquisition history?
- Are business books complete, including own insurance, private costs, asset history and losses?
- Which investment qualifies, when was it used, and will it be retained?
- Which salary reduction and advances were actually used, and were rental/sale events reported?

## Sources

| Official source | URL | Read on |
|---|---|---|
| Current UJP-listed DLD-GDP annual form, Gazette 101/2020; p. 2 reconciliation, p. 3 business row 2/field 22 instructions | https://www.ujp.gov.mk/files/attachment/0000/1264/Prijava_DLD-GDP_101-2020_15.04.2020.pdf | 2026-10-24 |
| State Statistical Office, average net wage November 2025, published 21 January 2026 | https://www.stat.mk/en/stat/population-and-living-conditions/labour-market/average-monthly-net-wage-paid-per-employee/average-monthly-net-wage-paid-per-employee-november-2025/ | 2026-10-30 |
| Personal Income Tax Law, consolidated through Gazette 274/2022 | https://www.ujp.gov.mk/files/attachment/0000/1466/ZAKON_ZA_DANOKOT_NA_LICEN_DOHOD_-_Azuriran_so_Sl.vesnik____274___od_20.12.2022.pdf | 2026-10-24; 2026-10-30 (web.archive.org copy, UJP site offline) |
| Tax Procedure Law, through Gazette 3/2025 | https://www.ujp.gov.mk/files/attachment/0000/0900/_________________________.pdf | 2026-10-24; 2026-10-30 (web.archive.org copy, UJP site offline) |
| UJP, 2026 reduction, publication 23-6493/1 of 17 December 2025, under PIT art. 10(4) | https://www.ujp.gov.mk/e/plakjanje/licno_osloboduvanje | 2026-10-24; 2026-10-30 (web.archive.org copy, UJP site offline) |
| Depreciation Decree, Gazette 277/2019 | https://www.ujp.gov.mk/files/attachment/0000/0157/Uredba_za_amortizacija__277-_219.pdf | 2026-10-24 |
| UJP, self-employment brochure issued 9 March 2026 (2025 return instructions) | https://ujp.gov.mk/files/attachment/0000/0730/08-2102-1-Odanocuvanje_na_prihodi_ostvareni_od_vrsenje_na_samostojna_dejnost_09.03.2026.pdf | 2026-10-24 |
| Annual self-employment tax balance Rulebook, Gazette 6/2020 | https://www.ujp.gov.mk/files/attachment/0000/1220/____________________________________________________271-19.pdf | 2026-10-24 |
| Individual treaty-relief Rulebook, Gazette 271/2019 | https://www.ujp.gov.mk/files/attachment/0000/1219/_____________________________________________________________________________271-19.pdf | 2026-10-24 |

[net-wage]: https://www.stat.mk/en/stat/population-and-living-conditions/labour-market/average-monthly-net-wage-paid-per-employee/average-monthly-net-wage-paid-per-employee-november-2025/
[pit]: https://www.ujp.gov.mk/files/attachment/0000/1466/ZAKON_ZA_DANOKOT_NA_LICEN_DOHOD_-_Azuriran_so_Sl.vesnik____274___od_20.12.2022.pdf
[procedure]: https://www.ujp.gov.mk/files/attachment/0000/0900/_________________________.pdf
[allowance]: https://www.ujp.gov.mk/e/plakjanje/licno_osloboduvanje
[depreciation]: https://www.ujp.gov.mk/files/attachment/0000/0157/Uredba_za_amortizacija__277-_219.pdf
[self-brochure]: https://ujp.gov.mk/files/attachment/0000/0730/08-2102-1-Odanocuvanje_na_prihodi_ostvareni_od_vrsenje_na_samostojna_dejnost_09.03.2026.pdf
[dld-gdp]: https://www.ujp.gov.mk/files/attachment/0000/1264/Prijava_DLD-GDP_101-2020_15.04.2020.pdf
[dld-db]: https://www.ujp.gov.mk/files/attachment/0000/1220/____________________________________________________271-19.pdf
[treaty-pit]: https://www.ujp.gov.mk/files/attachment/0000/1219/_____________________________________________________________________________271-19.pdf

Not yet confirmed: A standalone departure/deemed-disposal tax procedure. Do not infer a nil charge from absence of a transaction-specific analysis.

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
