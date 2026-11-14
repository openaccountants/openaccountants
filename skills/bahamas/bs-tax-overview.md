---
name: bs-tax-overview
description: >
  Overview of the Bahamas tax system for 2026. No personal income tax, no
  corporate income tax, no capital gains, inheritance or gift tax. What exists
  is VAT (10% standard, 5% medical goods, unprepared food from food stores
  exempt from 1 April 2026), the business licence tax on turnover, National
  Insurance (NIB) contributions, real property tax, VAT on property
  conveyances, stamp duty on some instruments, customs duties and the
  Domestic Minimum Top-Up Tax for large multinational groups. Gives the
  headline 2026 figures and which skill to load. Trigger on Bahamas tax
  system, taxes in the Bahamas, is the Bahamas tax free, moving to the Bahamas
  tax. Built from Bahamian legislation and DIR pages; not reviewed by an
  accountant.
version: 1.0
jurisdiction: BS
tax_year: 2026
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
category: international
tier: 2
domain: income-tax
type: situation-rules
---

# Bahamas tax overview

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Anyone asking how The Bahamas taxes people and businesses in 2026. Tax year: calendar year. Currency: Bahamian dollar (BSD), at par with the US dollar. Authorities: the Department of Inland Revenue (DIR, Ministry of Finance) for VAT, business licence, real property tax, DMTT and stamp duty; the National Insurance Board (NIB) for social contributions; Bahamas Customs for import duties.

There is no income tax of any kind: none on individuals, none on company profits, and none on capital gains. There is no inheritance, estate or gift tax. No Bahamian Act imposes one (Bahamas legislation index). Revenue comes from VAT, customs and excise, the business licence tax, real property tax and stamp duty.

## Rates, bands and thresholds

| Tax | 2026 headline | Load | Source |
|---|---|---|---|
| Personal and corporate income tax, capital gains, inheritance | None | `bs-income-tax`, `bs-corporate-income-tax` | Bahamas legislation, Acts by year and index: https://laws.bahamas.gov.bs/cms/legislation/acts_only/acts-by-year.html |
| VAT standard rate | 10% | `bahamas-vat` | VAT (Amendment) Act 2025, s. 3: https://inlandrevenue.finance.gov.bs/wp-content/uploads/2025/07/VALUE-ADDED-TAX-AMENDMENT-ACT-2025.pdf |
| VAT reduced rate | 5% on Fourth Schedule medical goods; unprepared food sold by a food store exempt from 1 April 2026 | `bahamas-vat` | VAT (Amendment) Act 2026: https://laws.bahamas.gov.bs/cms/images/LEGISLATION/AMENDING/2026/2026-0004A/2026-0004A.pdf |
| VAT registration | Taxable activity over BSD 100,000 | `bahamas-vat` | DIR VAT FAQs: https://inlandrevenue.finance.gov.bs/value-added-tax/faqs/ |
| Business licence tax | Exempt to BSD 100,000 turnover (not IBCs or financial services entities); 0.5%, 0.75%, 1.25%; 1.5% above BSD 175 million from 1 July 2026 | `bs-corporate-income-tax` | Business Licence (Amendment) Act 2026, s. 8: https://laws.bahamas.gov.bs/cms/images/LEGISLATION/AMENDING/2026/2026-0022A/2026-0022A.pdf |
| NIB contributions | Employee 4.65%, employer 6.65%, self-employed 10.30% | `bs-payroll-social` | National Insurance (Contributions) (Amendment) Regulations 2024: https://laws.bahamas.gov.bs/cms/images/LEGISLATION/AMENDING/2024/2024-0037S/2024-0037S.pdf |
| Real property tax, owner-occupied | First BSD 300,000 exempt; 0.625% on the next BSD 200,000; 1% above; cap BSD 150,000 | `bs-income-tax` | DIR RPT FAQs: https://inlandrevenue.finance.gov.bs/real-property-tax/faqs-rpt/ |
| Real property tax, foreign owner-occupied | 0.625% on the part to BSD 1 million; 1% above; cap BSD 200,000 | `bs-income-tax` | Real Property Tax (Amendment) Act 2026, s. 3: https://laws.bahamas.gov.bs/cms/images/LEGISLATION/AMENDING/2026/2026-0021A/2026-0021A.pdf |
| VAT on property conveyances | 2.5% to 10% by buyer and value band; foreign buyer 10% | `bahamas-vat` | VAT Act reprint, Third Schedule: https://inlandrevenue.finance.gov.bs/wp-content/uploads/2024/11/Value-Added-Tax-Act.pdf |
| DMTT | Large multinational groups (EUR 750 million revenue test) only | `bs-corporate-income-tax` | DIR, What is DMTT FAQ: https://inlandrevenue.finance.gov.bs/wp-content/uploads/2026/06/What-is-DMTT-FAQ-1.pdf |
| Stamp duty | Stamp Act 2024; sale of a business taxed on property other than land, valued from the gross asset value in the accounts, from 1 July 2026 | This skill | Stamp (Amendment) Act 2026, s. 3: https://laws.bahamas.gov.bs/cms/images/LEGISLATION/AMENDING/2026/2026-0018A/2026-0018A.pdf |

## The base

- **VAT** is charged on almost all goods and services supplied or imported for use in The Bahamas.
- **Business licence tax** is charged on turnover (all business revenue, without deductions), not profit.
- **NIB** is charged on insurable wages or income up to a ceiling.
- **Real property tax** is charged on the assessed value of property by class.
- **Stamp duty** applies to instruments under the Stamp Act 2024; from 1 July 2026 a Grand Bahama Port licensee counts as a "business" for it, and the sale of a business is charged on property other than land.

## Deadlines and filing

| Obligation | Deadline |
|---|---|
| Business licence renewal | 31 January |
| Business licence turnover return and tax | 31 March, or estimated tax in four instalments |
| Real property tax | 31 March (10% discount if paid in full by then) |
| VAT return and payment | 21 days after each monthly or quarterly period |
| DMTT filing | Not before 30 September 2026; payment for the transition year 18 months after its end |

## Penalties and interest

- VAT: late return the greater of BSD 100 or 2% of tax payable; late payment 10% (VAT Act s. 47A).
- Business licence: BSD 100 late filing; 10% late payment; 5% a year interest after 30 days.
- Real property tax: 5% surcharge on 1 January if unpaid at 31 December, plus 5% interest.

## Cross-border points

- Moving to The Bahamas does not create any Bahamian income tax. The country you leave may still tax you; the absence of Bahamian tax gives no foreign tax credit.
- Foreign buyers of real property pay 10% VAT on the conveyance; foreign-owned rentals pay commercial RPT rates.
- Non-Bahamians need Bahamas Investment Authority approval to carry on business.
- No withholding tax on dividends, interest or royalties paid abroad.

## Two worked examples that recompute

### Bahamian homeowner, assessed value BSD 450,000

```oa-check
name: BS RPT owner-occupied 450000, paid by 31 March
inputs:
  value: 450000
steps:
  - band_0625: (min(value, 500000) - 300000) * 0.00625
  - band_1: max(value - 500000, 0) * 0.01
  - rpt: band_0625 + band_1
  - discount: rpt * 0.10
  - net_if_paid_by_31_march: rpt - discount
expected:
  rpt: 937.50
  discount: 93.75
  net_if_paid_by_31_march: 843.75
```

The first BSD 300,000 is exempt; BSD 150,000 at 0.625% is BSD 937.50; paying in full by 31 March saves 10%.

### Decision: foreign owner who lives in the home, BSD 1.5 million

Under the 2026 Act a foreign owner-occupier pays 0.625% on the first BSD 1 million and 1% on the rest. A Bahamian owner-occupier of the same home pays nothing on the first BSD 300,000, 0.625% on the next BSD 200,000 and 1% on BSD 1 million.

```oa-check
name: BS RPT foreign vs Bahamian owner-occupied, 1.5m
inputs:
  value: 1500000
steps:
  - foreign: min(value, 1000000) * 0.00625 + max(value - 1000000, 0) * 0.01
  - bahamian: (min(value, 500000) - 300000) * 0.00625 + max(value - 500000, 0) * 0.01
  - difference: foreign - bahamian
expected:
  foreign: 11250
  bahamian: 11250
  difference: 0
```

At BSD 1.5 million both owners pay BSD 11,250. From BSD 1 million upwards the two schedules give the same tax until the caps (BSD 150,000 Bahamian, BSD 200,000 foreign); below BSD 1 million the foreign owner pays more because there is no BSD 300,000 exemption (at BSD 500,000: BSD 3,125 against BSD 1,250). Which tax year first applies the 2026 class is not yet confirmed.

## Ask the client first

1. Individual or business; Bahamian, permanent resident or foreign?
2. Employed, self-employed, or running a company; turnover?
3. VAT registered?
4. Property owned or being bought: class, value, buyer status?
5. Part of a multinational group?

## Sources

| Source | URL | Read on |
|---|---|---|
| Bahamas legislation, Acts by year 2026: read for the 2026 tax Acts and to confirm no income, capital gains or inheritance tax Act | https://laws.bahamas.gov.bs/cms/legislation/acts_only/acts-by-year.html | 2026-11-14 |
| VAT (Amendment) Act 2025: read for the 0%, 5% and 10% rates | https://inlandrevenue.finance.gov.bs/wp-content/uploads/2025/07/VALUE-ADDED-TAX-AMENDMENT-ACT-2025.pdf | 2026-11-14 |
| VAT (Amendment) Act 2026: read for the food exemption from 1 April 2026 | https://laws.bahamas.gov.bs/cms/images/LEGISLATION/AMENDING/2026/2026-0004A/2026-0004A.pdf | 2026-11-14 |
| VAT Act reprint 1 July 2024: read for s. 47A and the Third Schedule | https://inlandrevenue.finance.gov.bs/wp-content/uploads/2024/11/Value-Added-Tax-Act.pdf | 2026-11-14 |
| DIR VAT FAQs: read for registration and return deadlines | https://inlandrevenue.finance.gov.bs/value-added-tax/faqs/ | 2026-11-14 |
| Business Licence (Amendment) Act 2026: read for the 1.5% band | https://laws.bahamas.gov.bs/cms/images/LEGISLATION/AMENDING/2026/2026-0022A/2026-0022A.pdf | 2026-11-14 |
| National Insurance (Contributions) (Amendment) Regulations 2024: read for the NIB rates | https://laws.bahamas.gov.bs/cms/images/LEGISLATION/AMENDING/2024/2024-0037S/2024-0037S.pdf | 2026-11-14 |
| DIR RPT FAQs: read for RPT classes, rates, deadline, discount and surcharge | https://inlandrevenue.finance.gov.bs/real-property-tax/faqs-rpt/ | 2026-11-14 |
| Real Property Tax (Amendment) Act 2026: read for the BSD 150,000 cap and the foreign owner-occupied class | https://laws.bahamas.gov.bs/cms/images/LEGISLATION/AMENDING/2026/2026-0021A/2026-0021A.pdf | 2026-11-14 |
| Stamp (Amendment) Act 2026: read for the business definition and sale of a business from 1 July 2026 | https://laws.bahamas.gov.bs/cms/images/LEGISLATION/AMENDING/2026/2026-0018A/2026-0018A.pdf | 2026-11-14 |
| DIR, What is DMTT FAQ: read for DMTT scope and dates | https://inlandrevenue.finance.gov.bs/wp-content/uploads/2026/06/What-is-DMTT-FAQ-1.pdf | 2026-11-14 |

Not yet confirmed: stamp duty rates under the Stamp Act 2024 First Schedule (the text did not extract cleanly); customs duty rates; the 15% DMTT minimum rate figure; the NIB wage ceiling; the first RPT bill year for the 2026 Act changes.
