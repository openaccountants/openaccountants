---
name: bermuda-tax
description: >
  Start here for any Bermuda tax question in 2026. Bermuda has no personal income tax, no
  VAT, GST or sales tax, no capital gains tax and no withholding tax on dividends, interest
  or royalties. This skill says so plainly and covers what Bermuda does charge outside
  payroll and corporate income tax, namely customs import duty under the 2026 tariff,
  duty-free allowances, stamp duty on land transfers, leases and other documents, and
  land tax on annual rental value, and routes payroll tax, social insurance, corporate
  income tax and company formation to their own skills. Trigger phrases include Bermuda
  tax, Bermuda income tax, Bermuda VAT, Bermuda customs duty, Bermuda stamp duty, land tax.
version: "3.0"
jurisdiction: BM
tax_year: 2026
last_updated: 2026-11-14
category: international
type: situation-rules
domain: tax
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
---

# Bermuda tax v3.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Anyone asking what tax applies in Bermuda: residents, non-residents with Bermuda property, importers, buyers and tenants of land, and companies. Bermuda is a British Overseas Territory. The currency is the Bermuda dollar (BMD), at par with the US dollar. Taxes are administered by the Office of the Tax Commissioner (payroll tax, land tax, stamp duty), the Customs Department (import duty), the Department of Social Insurance and, for corporate income tax, the Corporate Income Tax Agency (CITA).

What Bermuda does not charge, for individuals and for companies outside an in-scope multinational group: income tax, capital gains tax, VAT, GST or general sales tax, and withholding tax on dividends, interest or royalties. There is no income tax return for individuals and no VAT registration, return or reverse charge. The tax on employment income is the employee portion of payroll tax, and indirect tax is collected mainly as customs duty at import ([Payroll tax](https://www.gov.bm/payroll-tax); [Customs Tariff 2026](https://www.gov.bm/files/media-library/20260413/753f0169-2026_bermuda_customs_tariff_2026.03.27v1r0_0.pdf)).

What changed: since fiscal years beginning on or after 1 January 2025, Bermuda constituent entities of multinational groups with EUR 750 million revenue pay 15% corporate income tax ([gov.bm, corporate income tax](https://www.gov.bm/articles/cit)). The old statement that a tax assurance guarantees no income tax until 2035 is wrong for those groups: the CIT applies notwithstanding any assurance under the Exempted Undertakings Tax Protection Act 1966 (CIT Act 2023 s.4(4)).

Which skill to load:

| Question | Skill |
|---|---|
| Payroll tax, employer and employee portions, social insurance | [bm-payroll-social](bm-payroll-social.md) |
| 15% corporate income tax for large groups, transfer pricing | [bm-corporate-income-tax](bm-corporate-income-tax.md) |
| Forming a company, beneficial ownership, economic substance declaration | [bm-company-formation](bm-company-formation.md) |
| Customs duty, stamp duty, land tax, no income tax, no VAT | this skill |

## Rates, bands and thresholds

| Item | 2026 figure and conditions | Official source |
|---|---|---|
| Personal income tax, capital gains tax, VAT or sales tax | None; employment income bears the payroll tax employee portion instead | [Payroll tax](https://www.gov.bm/payroll-tax) |
| Customs duty, most common ad valorem rate | 25% of value, for example portable computers (8471.300) and colour televisions (8528.720); rate is per tariff line | [Customs Tariff 2026](https://www.gov.bm/files/media-library/20260413/753f0169-2026_bermuda_customs_tariff_2026.03.27v1r0_0.pdf) |
| Customs duty, cotton T-shirts (6109.100) and footwear (6403.990) | 6.5% | same |
| Customs duty, prescription-only medicaments (3004.901) | 0%; other medicaments (3004.909) 25% | same |
| Customs duty, milk powder (0402.100) | 0% | same |
| Customs duty, small cars up to 1,000 cc valued BMD 10,000 or less (8703.217) | 75%; other vehicle lines carry their own value-banded rates | same |
| Passenger allowance, visitor | Up to BMD 50 on other accompanied personal goods that will remain in Bermuda, plus 200 cigarettes, 50 cigars, 0.5 kg tobacco, 1 litre wine and 1 litre spirits | [Duty free allowances](https://www.gov.bm/articles/duty-free-allowances) |
| Passenger allowance, resident | Up to BMD 300 on other accompanied personal goods acquired outside Bermuda, plus the same tobacco and alcohol limits | same |
| Stamp duty, conveyance or transfer on sale of Bermuda land, first BMD 100,000 | 2.1% | [Stamp duty](https://www.gov.bm/articles/stamp-duty-tax-legal-transactions) |
| Stamp duty, next BMD 400,000 (to 500,000) | 3.15% | same |
| Stamp duty, next BMD 500,000 (to 1,000,000) | 4.20% | same |
| Stamp duty, next BMD 500,000 (to BMD 1.5 million) | 6.3% | same |
| Stamp duty, over BMD 1.5 million | 7.35% | same |
| Stamp duty, property that is not Bermuda property | 1% | same |
| Stamp duty, lease up to three years | 1.05% of aggregate rent for the term | same |
| Stamp duty, lease over three years | 1.05% of aggregate rent for the first three years plus 0.5% of aggregate rent for the remaining period | same |
| Stamp duty, duplicate copies | BMD 27 each | same |
| Stamp duty, mortgage refinanced to another institution | No duty on the first BMD 1,000,000; excess at 0.5% | same |
| Adjudication fee (Tax Commissioner's opinion on duty), from 1 April 2023 | BMD 212 per item | same |
| Land tax, private dwelling, flat charge | BMD 150, with the band rates on ARV over BMD 22,000 | [Land tax](https://www.gov.bm/land-tax) |
| Land tax, private dwelling ARV bands | 0.80% (0 to 11,000), 1.80% (11,001 to 22,000), 3.50% (22,001 to 33,000), 6.50% (33,001 to 44,000), 17.00% (44,001 to 90,000), 35.00% (90,001 to the next band), 55.00% (120,001 and over) | same |
| Land tax, commercial property from 1 July 2019 | 9.5%; Economic Empowerment Zone 7%; tourist properties 8.9% | same |
| Land tax, late payment interest | 7% a year | same |
| Land tax relief, owner-occupier aged 65 or over | Up to BMD 1,791 a year (including the BMD 150 flat charge), for homes with ARV up to BMD 45,500; tax due on ARV above 45,500 | same |

## The base

- **Customs duty** is charged on the value of goods imported for home use at the rate on the tariff line (Customs Tariff Act 1970 and its Schedules, updated to 1 April 2026). Classify the goods to the tariff line before applying a rate; the 25% common rate is not a default for every good. Some lines carry specific rates instead of a percentage, for example wine (2204.210) at BMD 6.00 a litre.
- **Stamp duty** is charged on instruments: conveyances, leases, mortgages, trust deeds, the affidavit of value of a deceased estate, powers of attorney, insurance policies, share transfers, memoranda of association and others on the Office's list. Unstamped documents are not received in evidence. Land transfer duty is a sliding scale on the value of the transaction.
- **Land tax** is charged on the annual rental value (ARV) set by the Department of Land Valuation. It is payable by the sole proprietor, a life tenant, a leaseholder for three years or more, or a periodic tenant of Government property.
- **No estate or gift tax as such:** Bermuda has no inheritance tax; an estate meets stamp duty through the affidavit of value of the deceased estate, which is on the Office's list of dutiable documents (rate not confirmed here).
- **No income base:** profits, salaries, dividends, interest and gains of individuals and of companies outside an in-scope CIT group are not taxed on income.

## Deadlines and filing

| Tax | When and how | Source |
|---|---|---|
| Payroll tax | Quarterly, 15 January, 15 April, 15 July and 15 October; see [bm-payroll-social](bm-payroll-social.md) | [Payroll tax](https://www.gov.bm/payroll-tax) |
| Land tax | Twice a year, in March and September, on the date in the Tax Commissioner's demand note; pay online, in person, by mail (cheque) or through a bank | [Land tax](https://www.gov.bm/land-tax) |
| Stamp duty | Before the document is relied on; documents must be dated and signed before stamping; pay the Accountant General by cheque or cash | [Stamp duty](https://www.gov.bm/articles/stamp-duty-tax-legal-transactions) |
| Customs duty | At import, on the customs declaration; refunds of duty paid in error by letter to the Collector of Customs | [Customs Department](https://www.gov.bm/department/customs) |
| Corporate income tax | Two instalments and an annual return; see [bm-corporate-income-tax](bm-corporate-income-tax.md) | [CITA deadlines](https://www.cita.bm/assets/images/files/Filing%20%26%20Payment%20Deadlines%2005.06.2026.pdf) |

## Penalties and interest

- Land tax paid late carries interest at 7% a year ([Land tax](https://www.gov.bm/land-tax)).
- An unstamped document cannot be used in evidence in any proceedings ([Stamp duty](https://www.gov.bm/articles/stamp-duty-tax-legal-transactions)).
- Customs decisions about duty and civil penalties can be reviewed by the Customs Department and then appealed to the Tax Appeal Tribunal ([Customs Department](https://www.gov.bm/department/customs)).
- Payroll tax and CIT penalties are in their own skills.

## Cross-border points

- Bermuda levies no withholding tax on dividends, interest or royalties paid abroad (no Bermuda statute read for this skill charges one). CITA administers the Common Reporting Standard, Country-by-Country Reporting, FATCA and economic substance from 2026 ([gov.bm, corporate income tax](https://www.gov.bm/articles/cit)).
- A Bermuda resident who is a citizen or resident of another country (for example a US citizen) may owe that country's income tax; that is the other country's skill.
- Foreign contractors and subcontractors working in Bermuda pay payroll tax ([Payroll tax](https://www.gov.bm/payroll-tax)).
- Stamp duty on property that is not Bermuda property is 1%.

## Two worked examples that recompute

### Example 1: stamp duty on a BMD 2,000,000 house purchase

2,100 on the first 100,000; 12,600 on the next 400,000; 21,000 on the next 500,000; 31,500 on the next 500,000; 36,750 on the last 500,000. Total 103,950. (The old version of this skill used 2%, 4%, 6% and 8% and gave 128,000; those rates are not the current ones.)

```oa-check
name: Bermuda land transfer stamp duty, BMD 2,000,000, 2026
inputs:
  price: 2000000
steps:
  - b1: min(price, 100000) * 0.021
  - b2: max(0, min(price, 500000) - 100000) * 0.0315
  - b3: max(0, min(price, 1000000) - 500000) * 0.042
  - b4: max(0, min(price, 1500000) - 1000000) * 0.063
  - b5: max(0, price - 1500000) * 0.0735
  - duty: b1 + b2 + b3 + b4 + b5
expected:
  duty: 103950
```

### Example 2 (decision): sign a three-year or a five-year lease at BMD 60,000 a year

A three-year lease: 1.05% of 180,000 = 1,890. A five-year lease: 1.05% of the first three years' rent (1,890) plus 0.5% of the remaining 120,000 (600) = 2,490. The longer lease costs 600 more stamp duty up front but secures two more years; two successive three-year leases would cost 1,890 each, 3,780 over six years. Choose on the business need; the duty favours the single longer lease.

```oa-check
name: Bermuda lease stamp duty, three years against five years
inputs:
  annual_rent: 60000
steps:
  - three_year: annual_rent * 3 * 0.0105
  - five_year: annual_rent * 3 * 0.0105 + annual_rent * 2 * 0.005
  - extra_for_five: five_year - three_year
  - two_three_year_leases: three_year * 2
expected:
  three_year: 1890
  five_year: 2490
  extra_for_five: 600
  two_three_year_leases: 3780
```

## Ask the client first

1. Are you an individual or a company, and is the company part of a group with EUR 750 million consolidated revenue?
2. Do you employ anyone or work for yourself in Bermuda (payroll tax and social insurance)?
3. Are you importing goods? What are they, and what is their value?
4. Are you buying, selling or leasing property, and is it Bermuda property? What is the price or rent and the lease term?
5. Do you own or occupy a home, and are you 65 or over (land tax relief)?
6. Are you a citizen or resident of another country that taxes worldwide income?

## Sources

| Source | URL | Read on |
|---|---|---|
| Office of the Tax Commissioner, payroll tax: read for the statement that payroll tax is the tax on remuneration and applies to foreign contractors | https://www.gov.bm/payroll-tax | 2026-11-14 |
| Customs Department, Bermuda Customs Tariff 2026 (PDF, schedules to 1 April 2026): read for the tariff lines 0402.100, 2204.210, 3004.901, 3004.909, 6109.100, 6403.990, 8471.300, 8528.720 and 8703.217 and the frequency of the 25% rate | https://www.gov.bm/files/media-library/20260413/753f0169-2026_bermuda_customs_tariff_2026.03.27v1r0_0.pdf | 2026-11-14 |
| Customs Department, duty free allowances: read for the visitor and resident allowances and the tobacco and alcohol limits | https://www.gov.bm/articles/duty-free-allowances | 2026-11-14 |
| Customs Department, department page: read for refunds, reviews and appeals | https://www.gov.bm/department/customs | 2026-11-14 |
| Office of the Tax Commissioner, stamp duty on legal transactions (last updated 6 July 2026): read for the land transfer scale, non-Bermuda property, leases, duplicates, mortgage refinancing and the adjudication fee | https://www.gov.bm/articles/stamp-duty-tax-legal-transactions | 2026-11-14 |
| Office of the Tax Commissioner, land tax (last updated 6 July 2026): read for the ARV bands, the flat charge, commercial and tourist rates, due dates, interest and senior relief | https://www.gov.bm/land-tax | 2026-11-14 |
| Government of Bermuda, corporate income tax: read for the 1 January 2025 start and CITA's role for CRS and CbCR | https://www.gov.bm/articles/cit | 2026-11-14 |
| CITA, filing and payment deadlines (PDF): read for the CIT due dates referred to | https://www.cita.bm/assets/images/files/Filing%20%26%20Payment%20Deadlines%2005.06.2026.pdf | 2026-11-14 |

Not yet confirmed: Bermuda's treaty position (the old file said there are no general double tax treaties, only a US insurance arrangement; no official page opened); the absence of withholding tax rests on no charging statute being found, not on an official page saying so; how the land tax BMD 150 flat charge combines with the band rates for ARV over BMD 22,000 (the page's table is ambiguous; no land tax computation is given here); the old file's customs rates for "food 0% to 10%", "electronics 25%" as a category and "motor vehicles 33.5%" (food and vehicles have many lines; only the lines listed above were checked, and 33.5% was not found for cars); stamp duty rates for the affidavit of value and other instruments other than conveyances, leases and mortgages; whether any customs duty relief applies to a given business (the Customs guidance on relief for businesses and charities was not opened).
