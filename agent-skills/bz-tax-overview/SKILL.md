---
name: bz-tax-overview
description: "Overview of the Belize tax system for tax year 2026 and a router to the Belize skills. Belize taxes employed persons on chargeable income at 25%, taxes businesses and the self-employed on gross receipts through business tax at activity rates, charges General Sales Tax at 12.5%, and collects social security through the Social Security Board. Covers which tax applies to whom, the headline figures with their sources, filing calendar, penalties, cross-border withholding and where to go next. Trigger phrases include Belize taxes overview, how is Belize taxed, Belize tax system, Belize Tax Service, BTS and IRIS Belize."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/bz-tax-overview"
  jurisdiction: "BZ"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Belize tax overview v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

**Quick answer.** Belize has four taxes most people meet: **income tax** on employed persons only (25% of chargeable income, [bz-income-tax](bz-income-tax.md)); **business tax** on the gross receipts of companies, partnerships and the self-employed at activity rates such as 1.75%, 3% and 6% ([bz-corporate-income-tax](bz-corporate-income-tax.md)); **General Sales Tax** at 12.5% ([bz-vat-gst](bz-vat-gst.md)); and **social security** contributions to the SSB ([bz-payroll-social](bz-payroll-social.md)). Company formation is in [bz-company-formation](bz-company-formation.md). The Belize Tax Service (BTS) administers income tax, business tax and GST through the IRIS Belize portal. Tax year: calendar year. Currency: Belize dollar (BZD).

## Who this applies to

| Person | Taxes | Skill |
|---|---|---|
| Employee | Income tax under PAYE; employee SSB share | [bz-income-tax](bz-income-tax.md), [bz-payroll-social](bz-payroll-social.md) |
| Self-employed or sole proprietor | Business tax on receipts (no income tax since basis year 2020); GST if registered | [bz-corporate-income-tax](bz-corporate-income-tax.md), [bz-vat-gst](bz-vat-gst.md) |
| Company or partnership | Business tax on receipts; withholding on dividends, contracts and non-resident payments; GST; employer SSB and PAYE | [bz-corporate-income-tax](bz-corporate-income-tax.md), [bz-vat-gst](bz-vat-gst.md), [bz-payroll-social](bz-payroll-social.md) |
| Someone forming a company | Registration at BCCAR, then a TIN at BTS | [bz-company-formation](bz-company-formation.md) |

Since basis year 2020 no income tax is charged on any person other than an employed person (Income and Business Tax Act, Cap. 55, s.6(2) as replaced by Act No. 40 of 2024).

## Rates, bands and thresholds

Headline figures only; each owning skill carries the conditions and full tables.

| Item | Figure (2026) | Owning skill | Source |
|---|---|---|---|
| Income tax, employed persons | 25% of chargeable income; not chargeable under BZD 29,000 total income; BZD 20,000 basic deduction above it | bz-income-tax | [Act No. 40 of 2024, s.3 and s.4](https://media.bts.gov.bz/uploads/Act_No_40_of_2024_Income_and_Business_Tax_Amendment_Act_2024_b6bf496b66.pdf) |
| Business tax, general trade | 1.75% of gross receipts | bz-corporate-income-tax | [BTS Business Tax Guide, Ninth Schedule](https://media.bts.gov.bz/uploads/Business_Tax_Guide_20250929_fc95296232.pdf) |
| Business tax, rents from real property | 3% of gross receipts | bz-corporate-income-tax | same |
| Business tax, professions and vocations | 6% of gross receipts | bz-corporate-income-tax | same |
| Withholding on dividends | 15% | bz-corporate-income-tax | same |
| General Sales Tax | 12.5% standard; 0% zero-rated | bz-vat-gst | [GST Act, Cap. 63, s.9](https://media.bts.gov.bz/uploads/General_Sales_Tax_Act_2011_f573a52314.pdf) |
| GST registration limit | Supplies of seventy-five thousand dollars or more in twelve months | bz-vat-gst | [GST Act, s.23](https://media.bts.gov.bz/uploads/General_Sales_Tax_Act_2011_f573a52314.pdf) |
| Social security | 10% of weekly insurable earnings in total, wage ceiling BZD 520 a week | bz-payroll-social | [SSB Contribution and Benefit Schedule](https://socialsecurity.org.bz/wp-content/uploads/2022/03/Cont_Ben_Schedule.jpg) |

## The base

- **Income tax:** chargeable income of employed persons accruing in or derived from Belize, after deductions ([bz-income-tax](bz-income-tax.md)).
- **Business tax:** total receipts, in cash or in kind, without deduction of expenses, excluding GST and other amounts collected for others ([bz-corporate-income-tax](bz-corporate-income-tax.md)). There is no separate capital gains tax on individuals in the texts read; companies pay 5% business tax on annual net gains from specified foreign assets (BTS notice, 19 August 2026).
- **GST:** the value of taxable supplies and imports ([bz-vat-gst](bz-vat-gst.md)).
- **SSB:** weekly insurable earnings by wage band ([bz-payroll-social](bz-payroll-social.md)).

## Deadlines and filing

| Obligation | Due | Source |
|---|---|---|
| Business tax return and payment | 15th day of the following month, on IRIS Belize | [BTS Business Tax Guide](https://media.bts.gov.bz/uploads/Business_Tax_Guide_20250929_fc95296232.pdf) |
| GST return BTS210 and payment | Within fifteen days after the month | [GST Act](https://media.bts.gov.bz/uploads/General_Sales_Tax_Act_2011_f573a52314.pdf) |
| SSB contributions | No later than fourteen days after the month | [SSB contributions page](https://www.socialsecurity.org.bz/contributions/) |
| Annual income tax return | Last day of the third month after the basis year (31 March 2027 for 2026) | [Cap. 55 s.31](https://media.bts.gov.bz/uploads/Income_and_Business_Tax_Act_2011_13d48a3c6e.pdf) |

Registration for all BTS taxes uses one TIN obtained on IRIS Belize ([BTS registration guide](https://bts.gov.bz/guide/registration)).

## Penalties and interest

- Business tax: 10% of the tax per month late (minimum BZD 10, up to 24 months) and 1.5% a month interest.
- GST: 10% penalty and 1.5% a month interest on the BTS210 return.
- Income tax: 3% a month late return penalty (up to 20 months) and 1.5% a month interest.
Details and sources are in the owning skills.

## Cross-border points

- Payments to non-residents bear final withholding: dividends 15%, interest 15%, management fees, technical services and equipment rental 25%, insurance premiums 25%; CARICOM treaty residents get reduced rates ([bz-corporate-income-tax](bz-corporate-income-tax.md)).
- Double taxation relief extends to every treaty country since 1 January 2025 (Cap. 55 s.47 as replaced).
- Exports are zero-rated for GST.
- Transfer pricing: no general transfer pricing regime was found in Cap. 55 as read; the only arm's length rule is for petroleum operations.

## Two worked examples that recompute

**Example 1: employee or self-employed? (decision).** Ana is offered BZD 40,000 for a year's consulting by one client. If she works for that client for 60 days or more, BTS treats her as an employee: income tax (40,000 less 20,000) x 25% = BZD 5,000 under PAYE. If she instead works as an independent consultant for several clients with the same BZD 40,000 of receipts, she pays business tax at 6%: BZD 2,400, with no income tax. The deciding facts are the 60-day rule and the activity rate, not a choice of label.

```oa-check
name: Belize employee versus self-employed consultant, BZD 40,000
inputs:
  amount: 40000
  basic_deduction: 20000
  income_tax_rate: 0.25
  profession_rate: 0.06
steps:
  - as_employee_tax: (amount - basic_deduction) * income_tax_rate
  - as_self_employed_tax: amount * profession_rate
  - difference: as_employee_tax - as_self_employed_tax
expected:
  as_employee_tax: 5000.00
  as_self_employed_tax: 2400.00
  difference: 2600.00
```

**Example 2: small professional with a year-end refund (edge case).** A part-time bookkeeper (a profession, 6%) receives BZD 24,000 in 2026 and pays BZD 1,440 of business tax month by month. Because gross revenue for the year is BZD 25,000 or less, she can apply after year end for a refund of the BZD 1,440. If her client invoices also carried GST because she registered voluntarily, a BZD 1,000 fee would be billed at BZD 1,125.

```oa-check
name: Belize professional under BZD 25,000, refund and GST on a fee
inputs:
  receipts: 24000
  profession_rate: 0.06
  refund_limit: 25000
  fee: 1000
  gst_rate: 0.125
steps:
  - business_tax_paid: receipts * profession_rate
  - headroom_under_limit: refund_limit - receipts
  - refundable: business_tax_paid
  - fee_with_gst: fee * (1 + gst_rate)
expected:
  business_tax_paid: 1440.00
  headroom_under_limit: 1000.00
  refundable: 1440.00
  fee_with_gst: 1125.00
```

## Ask the client first

1. Employee, self-employed, company or a mix?
2. Activities and gross receipts (activity rate, refund limits, GST limit of BZD 75,000).
3. Any employees (SSB and PAYE)?
4. Any foreign income, foreign gains or payments to non-residents?
5. Registered with BTS (TIN) and SSB, and up to date with monthly returns?

## Sources

| Source | URL | Read on |
|---|---|---|
| Income and Business Tax (Amendment) Act No. 40 of 2024, read for s.6 (charge only on employed persons, 25%) and s.16 (BZD 29,000 and BZD 20,000) and s.47 | https://media.bts.gov.bz/uploads/Act_No_40_of_2024_Income_and_Business_Tax_Amendment_Act_2024_b6bf496b66.pdf | 2026-11-14 |
| BTS Business Tax Guide (September 2025), read for business tax rates, the 15th-day deadline, penalties, refunds, the 60-day employee rule and withholding | https://media.bts.gov.bz/uploads/Business_Tax_Guide_20250929_fc95296232.pdf | 2026-11-14 |
| General Sales Tax Act, Cap. 63, Revised Edition 2011, read for s.9 (12.5% and 0%), s.23 (seventy-five thousand dollars) and the fifteen-day return | https://media.bts.gov.bz/uploads/General_Sales_Tax_Act_2011_f573a52314.pdf | 2026-11-14 |
| SSB Contribution and Benefit Schedule effective 4 April 2022, read for the 10% total and the BZD 520 wage ceiling | https://socialsecurity.org.bz/wp-content/uploads/2022/03/Cont_Ben_Schedule.jpg | 2026-11-14 |
| SSB contributions page, read for the fourteen-day payment deadline | https://www.socialsecurity.org.bz/contributions/ | 2026-11-14 |
| Income and Business Tax Act, Cap. 55, Revised Edition 2011, read for s.31 (annual return date) | https://media.bts.gov.bz/uploads/Income_and_Business_Tax_Act_2011_13d48a3c6e.pdf | 2026-11-14 |
| BTS registration guide, read for one TIN for all BTS taxes on IRIS Belize | https://bts.gov.bz/guide/registration | 2026-11-14 |

Not yet confirmed: the currency peg (the old file's BZD 2 to USD 1, not read on a Central Bank page today); the statutory residence test; any 2026 budget changes; the consolidated Revised Edition 2020 texts.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `bz-tax-overview` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/bz-tax-overview. If neither is available, confirm every figure against the official source pages cited above before relying on it.
