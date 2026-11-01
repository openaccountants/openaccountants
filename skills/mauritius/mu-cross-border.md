---
name: mu-cross-border
description: >
  Mauritius cross-border tax for the 2026/27 income year. Covers residence and sourcing, the tax residence certificate, foreign income of individuals, premium and golden visa holders, foreign tax credit, treaties, withholding on payments to non-residents including new digital items from Finance Act 2026, global business entities and foreign digital suppliers. Use for non-residents with Mauritius income, Mauritians with foreign income, treaty relief, or withholding on a payment abroad.
jurisdiction: MU
category: cross-border
tax_year: 2026
tax_year_notes: "Income year 1 July 2026 to 30 June 2027 (year of assessment 2027/28)"
version: 0.1
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Mauritius Cross-Border Tax v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

Tax year covered: Income year 1 July 2026 to 30 June 2027 (year of assessment 2027/28).

## Who this applies to

Non-residents with Mauritius income, residents with foreign income, and payers sending money abroad. Residence tests are in [Income tax](mu-income-tax.md) and [Corporate income tax](mu-corporate-income-tax.md).

## Rates, bands and thresholds

| Item | Figure | Conditions | Tax year | Source |
|---|---|---|---|---|
| Interest to non-resident | 15% | Payer other than a bank; treaty rate if lower | 2026/27 | https://www.mra.mu/download/ITAConsolidated.pdf |
| Royalties to non-resident | 15% | Treaty rate if lower (s.111C(4)) | 2026/27 | same |
| Rent to non-resident | 10% | Same | 2026/27 | same |
| Services in Mauritius by non-resident | 10% | s.111B(h) | 2026/27 | same |
| Management fees to non-resident | 10% | s.111B(i) | 2026/27 | same |
| Non-resident entertainer or sportsperson | 10% | Treaty rate if lower | 2026/27 | same |
| ICT provider, non-resident | 1% above Rs 300,000 | ICT services supplied in Mauritius are now Mauritius-source (s.74(1)(j)); payer not an individual | 2026/27 | https://www.mra.mu/download/FinanceAct2026.pdf |
| Digital marketing, non-resident | 5% | Social media and similar, payer not an individual | 2026/27 | same |
| Treaties | 45 agreements | Check the country on the list | 2026/27 | https://www.mra.mu/index.php/taxes-duties/international-taxation/double-taxation-agreements |
| Partial exemption | 80% | No foreign tax credit on the same income | 2026/27 | https://www.mra.mu/download/ITAConsolidated.pdf |
| Foreign digital VAT registration | Above Rs 3 million | See [VAT](mauritius-vat.md) | 2026 | https://www.mra.mu/download/VATAct.pdf |

## The base

Income from Mauritius includes employment duties performed wholly or mainly there, fees as a director of a resident company wherever the work happens, and business carried on wholly or partly there (s.74). Income derived while resident also counts (s.5(1)). An individual's foreign income is derived when received or dealt with in Mauritius (s.5(3)). Premium or golden visa holders: remote-work income counts when remitted; foreign card spending is not a remittance; a Mauritius deposit is taxed unless they declare tax was paid abroad (s.73B). Foreign tax paid is a credit against Mauritius tax on that income, and for dividends includes underlying tax (s.77). No credit on income under partial exemption, or income under s.44C. Non-residents get no reliefs.

**Global business.** "Global business entity" now reaches foundations, trusts and unit trust trustees by non-resident or licence tests, from the year of assessment starting 1 July 2027 (Finance Act 2026 s.7(a)(ii), s.28(10)).

## Deadlines and filing

1. Tax Residence Certificate: apply through e-TRC on [MRA e-Services](https://www.mra.mu/index.php/e-services). Issued within 7 days if the s.112 or s.116 return is filed and the fee paid (s.73(3)).
2. Before paying abroad: find the Sixth Schedule item, check the treaty, take the lower rate.
3. Withhold and file the monthly TDS return with payment by the end of the following month on the e-filing route ([calendar](https://www.mra.mu/important-dates)).
4. Annual TDS return and related statements for the year to 30 June fall in August in the calendar.

## Penalties and interest

Income tax penalties apply: see [Corporate income tax](mu-corporate-income-tax.md).

## Cross-border points

Transfer pricing: [Transfer pricing](mu-transfer-pricing.md). Foreign tax credit detail is in the 2011 regulations made under s.77(3).

## Two worked examples that recompute

**Example 1.** Rs 1,000,000 royalty to a non-resident, no treaty: withhold 15%, Rs 150,000; net Rs 850,000.

```oa-check
name: Royalty to non-resident
inputs:
  royalty: 1000000
steps:
  - wht: royalty * 0.15
  - net: royalty - wht
expected:
  net: 850000.00
```

**Example 2. Decision: partial exemption or foreign tax credit on foreign interest.** Rs 1,000,000 interest with Rs 100,000 foreign tax. Exemption: Rs 200,000 taxed at 15%, Rs 30,000, no credit. Credit: Rs 150,000 less Rs 100,000, Rs 50,000. The exemption costs Rs 20,000 less, where the company qualifies.

```oa-check
name: Exemption against credit
inputs:
  income: 1000000
  foreign: 100000
steps:
  - exempt_route: income * 0.20 * 0.15
  - credit_route: income * 0.15 - foreign
  - saving: credit_route - exempt_route
expected:
  saving: 20000.00
```

## Ask the client first

1. Payer and payee residence?
2. Income type, and where the work happens?
3. Which treaty, and a residence certificate?
4. Foreign tax actually paid?
5. Visa type, if an individual?
6. Global Business Licence?

## Sources

| Source | URL | Read on |
|---|---|---|
| Income Tax Act consolidated: ss.5, 73, 73B, 74, 77, 111B, 111C, Sixth Schedule read | https://www.mra.mu/download/ITAConsolidated.pdf | 2026-11-01 |
| Finance Act 2026: s.7, s.28 read | https://www.mra.mu/download/FinanceAct2026.pdf | 2026-11-01 |
| MRA treaty list page read | https://www.mra.mu/index.php/taxes-duties/international-taxation/double-taxation-agreements | 2026-11-01 |
| MRA tax calendar, August and monthly entries read | https://www.mra.mu/important-dates | 2026-11-01 |
| MRA e-Services menu read | https://www.mra.mu/index.php/e-services | 2026-11-01 |
| VAT Act: s.15, Sixth Schedule read | https://www.mra.mu/download/VATAct.pdf | 2026-11-01 |

Not yet confirmed: treaty rates by country, which we did not open; capital gains on non-residents; substance tests for licences; whether the 80% exemption applies to every foreign interest stream; how the foreign tax credit cap works under the 2011 regulations.
