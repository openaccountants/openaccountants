---
name: vu-tax-overview
description: "Vanuatu tax overview, tax year 2026: no ordinary personal or corporate income tax; VAT 15%, rent tax 12.5%, VNPF 6% plus 6% from January 2026, business licence and VFSC fees, main due dates, and Common Reporting Standard returns by financial institutions (31 May, nil returns, 5-year records)."
version: 1.4
jurisdiction: VU
tax_year: 2026
last_updated: 2026-11-26
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: situation-rules
---

# Vanuatu tax overview

> **General reference only.** Source-cited draft, not reviewed by an accountant. Do not use it to file or take a position without professional review.

## Who this applies to

Anyone who needs the map of Vanuatu's taxes for 2026. Vanuatu has no ordinary personal or corporate income tax ("Vanuatu does not have an income tax system", Vanuatu Competent Authority). Revenue comes from VAT, rent tax, business licences, import duties and excise. The authority is the Department of Customs and Inland Revenue (DCIR); companies register with the Vanuatu Financial Services Commission (VFSC). Currency: vatu (VT, VUV). Detail sits in the sibling skills, which own their figures: [income tax and rent tax](vu-income-tax.md), [company taxation](vu-corporate-income-tax.md), [VAT](vu-vat-gst.md), [payroll](vu-payroll-social.md), [company formation](vu-company-formation.md).

## Rates, bands and thresholds

| Tax | Headline | Tax year | Official URL |
|---|---|---|---|
| Personal and corporate income tax | None | 2026 | https://vanuatucustoms.gov.vu/images/Forms/VCA/VU_AEOI_Guide_v4.pdf |
| VAT | 15% standard rate (s 11) | 2026 | https://vanuatucustoms.gov.vu/images/Laws_Regulations/VAT/247_Value_Added_Tax_Consolidated_2020.pdf |
| VAT registration | Taxable supplies over VT4 million in 12 months | 2026 | https://vanuatucustoms.gov.vu/taxes-and-licensing/taxes/value-added-tax-vat/introduction.html |
| Rent tax | 12.5% of the excess over VT 200,000 per period for a natural person; 12.5% of all chargeable rent otherwise (Sch 1) | 2026 | https://vanuatucustoms.gov.vu/images/TAA/196_Rent_Taxation_Act_Consolidated_2020.pdf |
| VNPF | 6% employer plus 6% employee from the January 2026 contribution (4% plus 4% before) | 2026 | https://www.vnpf.com.vu/uploads/9/5/0/5/95052148/vanuatu_national_provident_fund_consolidated_2026.pdf |
| Company registration and annual return | VT 35,000 each | 2026 | https://www.vfsc.vu/companies-fees-and-penalties/ |

## The base

VAT falls on supplies by registered persons and on imports; rent tax on rent from Vanuatu land per six-month period; VNPF on covered remuneration; the business licence on carrying on business, by activity and turnover. Property, estate and stamp duties apply by transaction and were not reconciled for this guide.

## Deadlines and filing

| Obligation | When | Official URL |
|---|---|---|
| VAT return and payment | 27th of the month after the period; 5 January for a period ending 30 November; next working day if a holiday | https://vanuatucustoms.gov.vu/taxes-and-licensing/taxes/value-added-tax-vat/introduction.html |
| Rent tax | Within 28 days after the periods ending 31 May and 30 November. Check the DCIR calendar for the actual dates. | https://vanuatucustoms.gov.vu/index.php/important-dates |
| VNPF | End of the month after the contribution month | https://www.vnpf.com.vu/uploads/9/5/0/5/95052148/vanuatu_national_provident_fund_consolidated_2026.pdf |
| Business licence renewal | For 2026, Monday 2 February at 5 pm. The second instalment, where applicable, was due 31 July. | https://vanuatucustoms.gov.vu/images/News/2026/Business%20License%20Approved%20Notice%202026.pdf |
| Common Reporting Standard return | 31 May of the year after the calendar year reported | https://vanuatucustoms.gov.vu/images/Forms/VCA/VU_AEOI_Guide_v4.pdf |

**Financial account reporting.** Under the Applied Common Reporting Standard, in force from 1 January 2020 in the Tax Administration Regulation Order No. 154 of 2019, a Reporting Financial Institution applies the prescribed due diligence and files an electronic return for each calendar year, including a nil return if it finds no reportable accounts. The return is due by 31 May of the following year unless the Competent Authority allows more time (AEOI guide, section 1.7). For calendar 2025, the Competent Authority's public notice opened the MDES portal "until May 31st, 2026" (https://vanuatucustoms.gov.vu/images/VCA/Public%20Notice%20-%20CRS%20Reporting%20%202026%20English.pdf); its 2026 reporting plan gives 31 July 2026, so which date governed that cycle is open. Ryan Duguid reads Order No. 156 of 2020 as requiring records to be kept for 5 years after the end of the calendar year in which the return for the last relevant period falls due (to 31 December 2031 for a calendar 2025 record); the Order could not be reopened.

## Penalties and interest

The VNPF surcharge is 5% of unpaid contributions per month or part of a month, subject to the statutory minimum rule and remission. The business licence surcharge is 10% per chargeable month on overdue principal. VFSC late-document fees are VT 10,000 or VT 25,000, depending on the delay. The Tax Administration Act sets the VAT and rent tax penalties. See the sibling skills.

## Cross-border points

No tax on foreign or domestic income, so no foreign tax credit, no CFC rules and no treaty network for income tax. Imports bear VAT and duties at the border. Vanuatu exchanges financial account information under the Common Reporting Standard.

## Two worked examples that recompute

**1. Retail company: one month's VAT.** Sales VT 2,000,000 exclusive of VAT, input VAT VT 120,000: VAT payable VT 180,000 by the 27th (derived).

```oa-check
name: Vanuatu overview VAT month
inputs:
  sales: 2000000
  input_vat: 120000
steps:
  - payable: sales * 0.15 - input_vat
expected:
  payable: 180000
```

**2. Individual landlord, VT 500,000 chargeable rent in the period to 31 May 2026.** Rent tax is (500,000 minus 200,000) times 12.5% = VT 37,500. The statutory period gives a nominal date of 28 June, a Sunday in 2026. The DCIR calendar gives Monday 29 June for the June deadline.

```oa-check
name: Vanuatu overview rent tax individual
inputs:
  rent: 500000
  threshold: 200000
steps:
  - tax: max(rent - threshold, 0) * 0.125
expected:
  tax: 37500
```

## Ask the client first

- Individual, local company, international company or financial institution?
- Business activity, turnover and imports?
- Any rental income from Vanuatu land?
- Any employees?

## Sources

| Source | URL | Read on |
|---|---|---|
| Vanuatu Competent Authority, AEOI guide v4, sections 1.6 and 1.7 (Read for no income tax system, the 31 May deadline and nil returns) | https://vanuatucustoms.gov.vu/images/Forms/VCA/VU_AEOI_Guide_v4.pdf | 2026-11-14 |
| VCA public notice, CRS reporting 2026 (Read for the portal open until 31 May 2026) | https://vanuatucustoms.gov.vu/images/VCA/Public%20Notice%20-%20CRS%20Reporting%20%202026%20English.pdf | 2026-11-14 |
| Value Added Tax Act [Cap 247] 2020 and DCIR VAT introduction (Read for 15%, VT4 million, due dates) | https://vanuatucustoms.gov.vu/taxes-and-licensing/taxes/value-added-tax-vat/introduction.html | 2026-11-14 |
| Rent Taxation Act [Cap 196] 2020, Sch 1; VFSC fees; DCIR business licencing (Read for the rent tax, company and licence rows) | https://vanuatucustoms.gov.vu/images/TAA/196_Rent_Taxation_Act_Consolidated_2020.pdf | 2026-11-14 |
| DCIR Notice 001/2026 (2026 business licence deadline) | https://vanuatucustoms.gov.vu/images/News/2026/Business%20License%20Approved%20Notice%202026.pdf | 2026-11-22 |
| DCIR Important Dates (second instalment and rent tax dates) | https://vanuatucustoms.gov.vu/index.php/important-dates | 2026-11-22 |
| VNPF Act 2026 consolidation (Read by Ryan Duguid; vnpf.com.vu refused scripts on 2026-11-14) | https://www.vnpf.com.vu/uploads/9/5/0/5/95052148/vanuatu_national_provident_fund_consolidated_2026.pdf | 2026-11-11 |

Not yet confirmed: which CRS deadline (31 May or 31 July 2026) governed calendar 2025; the effect of the 2024 Tax Administration Regulation amendment on the record-keeping rule (Order No. 156 of 2020 read by Ryan Duguid at https://doft.gov.vu/images/2020/Tax_Policy/Tax_Administration_Regualtion_Amendment_Order_No_156_of_2020.pdf); property, estate and stamp duties; withholding on payments to non-residents; the gazetted VNPF Act No. 25 of 2025.
