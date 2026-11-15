---
name: je-crypto-tax
description: >
  Jersey cryptocurrency tax classification checked in October 2026, covering
  mining, exchanges, business receipts, sterling valuation and GST treatment.
  Use for Jersey Bitcoin tax, crypto disposals, mining income, crypto payments
  or reporting-provider obligations. Applies the published trading distinction
  before treating a disposal as taxable or non-taxable and separates tax
  liability from the Crypto-Asset Reporting Framework. Includes a bounded
  GST valuation example for an established standard-rated sale. Staking,
  decentralised finance, tokens, international reporting and regulatory
  status need further evidence. This source-cited draft awaits professional
  review and does not classify every cryptocurrency transaction from its label.
jurisdiction: JE
category: crypto
tax_year: 2026
tier: 2
type: situation-rules
last_updated: 2026-11-14
version: 1.1
depends_on:
  - workflow-base
  - crypto-tax-workflow-base
---

# Jersey cryptocurrency tax

Tax year: the 2026 year of assessment. Currency is GBP. Authority: Revenue Jersey (the Comptroller for CARF reporting).

## Who this applies to

Individuals and businesses in Jersey that mine, exchange, receive or pay with cryptocurrency, and Crypto-Asset Service Providers within Section I of the Crypto-Asset Reporting Framework (CARF). A user's income tax treatment is separate from a provider's reporting obligations.

## Rates, bands and thresholds

| 2026 item | Rate, figure or date | Conditions | Source |
|---|---|---|---|
| GST on a standard-rated sale paid for in cryptocurrency | 5% of the sterling value at the transaction date | GST-registered supplier; the exchange of cryptocurrency itself does not attract GST | [GST for businesses](https://www.gov.je/Industry/BusinessAdviceHub/BusinessTaxesSocialSecurity/Pages/GoodsServicesTaxBusinesses.aspx) |
| CARF Regulations in force | 1 January 2026 | Providers within CARF Section I | [CARF Regulations 2025, reg 18](https://www.jerseylaw.je/laws/current/ro_96_2025) |
| CARF information return due date | 30 June following the reporting year (2026 return due by 30 June 2027) | Each calendar year; reportable users or controlling persons | [CARF Regulations 2025, reg 5](https://www.jerseylaw.je/laws/current/ro_96_2025) |
| Partner-jurisdiction exception notification | 30 June following the relevant year | Provider or branch fulfils Section I requirements in a listed partner jurisdiction | [CARF Regulations 2025, reg 3](https://www.jerseylaw.je/laws/current/ro_96_2025) |
| CARF record retention | 5 years from the day after the calendar year ends | Due diligence steps and collected information | [CARF Regulations 2025, reg 4](https://www.jerseylaw.je/laws/current/ro_96_2025) |

## The base

Revenue Jersey's [cryptocurrency treatment guidance](https://www.gov.je/TaxesMoney/IncomeTax/Technical/Guidelines/Pages/CryptocurrenciesTreatment.aspx) distinguishes trading from occasional activity. Small or irregular mining is generally not trading by itself; commercial mining combined with trading can require a different result. Exchange activity gives rise to income tax where the features of trading are met. An occasional non-trading exchange gain generally has no taxable profit and no deductible associated loss or expenses. Establish the facts before applying these descriptions.

Business receipts and payments in cryptocurrency must be reflected in the accounts under ordinary tax rules. Convert transactions to the accounts currency and express taxable profit or loss in sterling for Jersey assessment. Retain transaction timestamps, asset quantities, valuation sources, fees and the evidence used to establish trading status.

### GST

The [cryptocurrency guidance](https://www.gov.je/TaxesMoney/IncomeTax/Technical/Guidelines/Pages/CryptocurrenciesTreatment.aspx) requires a sterling value for goods or services bought with cryptocurrency at the transaction date. Exchanging cryptocurrency for sterling, other currency or another cryptocurrency does not itself attract GST under that guidance. This does not exempt the underlying goods or services purchased with it.

## Deadlines and filing

The [Jersey CARF Regulations 2025, reg 18](https://www.jerseylaw.je/laws/current/ro_96_2025) took effect on 1 January 2026. Providers within Section I of the Crypto-Asset Reporting Framework (CARF) must establish and maintain due diligence arrangements under reg 2. Apply the incorporated CARF rules to the provider, assets, users and controlling persons before determining what to report.

Regulation 5 requires an information return to the Comptroller for each calendar year in the required form and manner. It covers users with a relationship during the year who are reportable or have reportable controlling persons. Include the information required by CARF Section II and any other information the Comptroller reasonably requires. The due date is 30 June following the reporting year, so the 2026 return is due by 30 June 2027. [CARF Regulations, regs 1 to 2, 5 and Schedule](https://www.jerseylaw.je/laws/current/ro_96_2025)

Regulation 3 provides a separate due diligence exception if the provider or its branch fulfils the requirements in a listed partner jurisdiction under CARF Section I. Notify the Comptroller by 30 June following the relevant year, naming the jurisdiction and the applicable Section I criterion. Check partner status, reporting treatment and the required notification form separately. Regulation 4 requires records of the due diligence steps and collected information for 5 years from the day after the calendar year ends. [CARF Regulations, regs 3 to 4](https://www.jerseylaw.je/laws/current/ro_96_2025)

The [Revenue Jersey CARF and CRS page](https://www.gov.je/TaxesMoney/InternationalTaxAgreements/IGAs/pages/cryptoassetreporting.aspx) gives the dated reportable-jurisdiction list. Check the applicable list and current filing directions.

Individual and company income tax returns follow `je-income-tax`, `je-corporate-income-tax` and `je-income-tax-compliance`; GST returns follow `je-gst`.

## Penalties and interest

CARF penalties are a research gap (see Not yet confirmed). Income-tax penalties are in [je-income-tax-compliance](je-income-tax-compliance.md).

## Cross-border points

CARF reporting concerns users and controlling persons resident in reportable jurisdictions on the dated list. A user's Jersey residence decides their own income tax (see `je-income-tax` and `je-cross-border-withholding`).

## Two worked examples that recompute

**Example 1: sale priced at GBP 100 excluding GST.** A GST-registered business makes an established standard-rated sale for a cryptocurrency amount worth GBP 100 excluding GST at the transaction date. The sale carries GBP 5 GST and GBP 105 total consideration. Valuation and supply classification are assumed established. The [GST business guidance](https://www.gov.je/Industry/BusinessAdviceHub/BusinessTaxesSocialSecurity/Pages/GoodsServicesTaxBusinesses.aspx) supplies the 5% rate; retain evidence of the actual conversion used.

```oa-check
name: Jersey GST on a crypto-paid sale, GBP 100 excluding GST
inputs:
  value_ex_gst: 100
  rate: 0.05
steps:
  - gst: value_ex_gst * rate
  - total: value_ex_gst + gst
expected:
  gst: 5
  total: 105
```

**Example 2: sterling equivalent agreed as GBP 105 including GST.** If the agreed sterling equivalent is instead GBP 105 including GST, the GST component is GBP 105 x 5 / 105 = GBP 5.

```oa-check
name: Jersey GST on a crypto-paid sale, GBP 105 including GST
inputs:
  value_inc_gst: 105
steps:
  - gst: value_inc_gst * 5 / 105
  - net: value_inc_gst - gst
expected:
  gst: 5
  net: 100
```

## Ask the client first

1. Is the activity trading (frequency, organisation, commercial mining), or occasional?
2. Are cryptocurrency receipts or payments part of a business, and what is the accounts currency?
3. What valuation source and timestamp were used to convert each transaction to sterling?
4. Is the business GST-registered, and is the supply standard-rated?
5. For a provider: is it within CARF Section I, and does a partner-jurisdiction exception apply?

Self-checks: establish trading status, value business transactions in the correct currency, and distinguish exchanging a token from selling goods for a token. Keep tax classification and international reporting separate.

## Sources

Primary tax guidance was read on 11 October 2026. The CARF Regulations were checked on 11 November 2026. See `references.md` for periods and capture hashes. This is a source-cited draft awaiting professional review.

| Source | URL | Read on |
|---|---|---|
| Revenue Jersey, Cryptocurrency tax treatment: read for trading, mining, exchange, sterling valuation and GST treatment | https://www.gov.je/TaxesMoney/IncomeTax/Technical/Guidelines/Pages/CryptocurrenciesTreatment.aspx | 2026-10-11 |
| Government of Jersey, GST for businesses: read for the 5% standard rate | https://www.gov.je/Industry/BusinessAdviceHub/BusinessTaxesSocialSecurity/Pages/GoodsServicesTaxBusinesses.aspx | 2026-10-11 |
| Taxation (Implementation) (Crypto-Asset Reporting Framework) (Jersey) Regulations 2025, regs 1 to 5, 18 and Schedule: read for due diligence, return, exception, records and commencement | https://www.jerseylaw.je/laws/current/ro_96_2025 | 2026-11-11 |
| Revenue Jersey, CARF and expansion of the CRS: read for the reportable-jurisdiction list | https://www.gov.je/TaxesMoney/InternationalTaxAgreements/IGAs/pages/cryptoassetreporting.aspx | 2026-10-11 |

Not yet confirmed: trading classification, staking, decentralised finance, token classification, mining GST exceptions, current CARF and CRS filing mechanics, penalties and licensing remain research gaps.
