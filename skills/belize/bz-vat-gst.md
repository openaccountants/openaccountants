---
name: bz-vat-gst
description: >
  Belize General Sales Tax (GST) for tax year 2026. GST is charged at 12.5% on taxable supplies
  and imports, 0% on the zero-rated schedules (exported goods and services and listed other
  supplies), with exempt supplies such as financial services. Covers who must register (supplies
  of BZD 75,000 or more in twelve months), the monthly tax period, the BTS210 return lines and
  due date fifteen days after the month, input tax, penalties and interest, and electronic
  invoicing under the 2024 amendment. Trigger phrases include Belize GST, Belize sales tax,
  Belize VAT, BTS210, GST registration Belize and Belize GST return.
version: "1.0"
jurisdiction: BZ
tax_year: 2026
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: tax
type: situation-rules
category: international
---

# Belize General Sales Tax (GST) v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

**Quick answer.** Belize charges General Sales Tax at **12.5%** on taxable supplies and taxable importations, **0%** on zero-rated supplies, and no tax on exempt supplies (General Sales Tax Act, Cap. 63, s.8 and s.9). A person must register once supplies reach **BZD 75,000 in twelve months** (s.23). The tax period is a **calendar month**, and the BTS210 return is due **within fifteen days after the month** (s.2 and the return section). Tax year: calendar year 2026. Currency: BZD. Authority: Belize Tax Service (BTS).

## Who this applies to

- **Registered persons** making taxable supplies in Belize, and importers of taxable goods (GST on imports is paid to the Comptroller of Customs and claimed on BTS210 line 240).
- **Must register:** a person meets the registration limit if, on the last day of any month, supplies in the previous twelve months were BZD 75,000 or more and are expected to be BZD 75,000 or more in the next twelve months, or if supplies in the next twelve months are expected to be BZD 75,000 or more (s.23(1)). Sales of capital assets and supplies that would not be taxable are left out of the test (s.23(2)).
- **Not in this skill:** business tax on receipts ([bz-corporate-income-tax](bz-corporate-income-tax.md)) and customs duties.

## Rates, bands and thresholds

| Item | Figure (2026) | Conditions | Source |
|---|---|---|---|
| Standard rate | 12.5% | Every taxable supply or importation not zero-rated; the Minister may vary the rate by Order (s.9(2)) | [GST Act, Cap. 63, s.9(1)(b)](https://media.bts.gov.bz/uploads/General_Sales_Tax_Act_2011_f573a52314.pdf) |
| Zero rate | 0% | Supplies and imports under the First Schedule (exported goods), Second Schedule (exported services) and Third Schedule (other zero-rated supplies and imports) | [GST Act, s.9(1)(a) and Schedules 1 to 3](https://media.bts.gov.bz/uploads/General_Sales_Tax_Act_2011_f573a52314.pdf) |
| Exempt supplies | No GST, no input credit | Fourth Schedule, for example financial services and other intermediation, and supplies by educational institutions; Fifth Schedule lists exempt imports | [GST Act, Schedules 4 and 5](https://media.bts.gov.bz/uploads/General_Sales_Tax_Act_2011_f573a52314.pdf) |
| Registration limit | BZD 75,000 of supplies in twelve months | Tested on the last day of each month, looking back and forward (s.23(1)) | [GST Act, s.23](https://media.bts.gov.bz/uploads/General_Sales_Tax_Act_2011_f573a52314.pdf) |
| Tax period | One calendar month | Definition of "tax period" | [GST Act, s.2](https://media.bts.gov.bz/uploads/General_Sales_Tax_Act_2011_f573a52314.pdf) |
| Return due | Within fifteen days after the end of the tax period; within fourteen days after ceasing to be registered | Or later if the Commissioner allows in writing | [GST Act, return section](https://media.bts.gov.bz/uploads/General_Sales_Tax_Act_2011_f573a52314.pdf) |
| Late payment penalty on the return | 10% of the tax due for the period | BTS210 line 330, if paying after the due date | [BTS210 GST return](https://media.bts.gov.bz/uploads/BTS_210_GST_RETURN_MANUAL_d6b6eaa77c.pdf) |
| Late payment interest on the return | 1.5% of the tax due per month | BTS210 line 340 | same |

## The base

The BTS210 return sets the computation ([BTS210 GST return](https://media.bts.gov.bz/uploads/BTS_210_GST_RETURN_MANUAL_d6b6eaa77c.pdf)):

1. **Supplies:** line 100 standard-rated supplies (GST exclusive); line 110 zero-rated supplies including exports; line 120 exempt supplies; line 130 total.
2. **Output tax:** line 140 = line 100 x 12.5%; line 150 adjustments (debit notes issued, credit notes received); line 160 total output tax.
3. **Purchases and input tax:** lines 200 to 230 record the value of imports and domestic standard, zero-rated and exempt purchases; line 240 GST paid to Customs on imports; line 250 GST paid or payable on domestic taxable supplies; line 260 adjustments; line 270 total input tax.
4. **Payable or credit:** if output exceeds input, line 300 tax payable, less line 310 credit from a previous period, gives line 320 tax due; add line 330 penalty and line 340 interest if late; line 350 total due. GST withheld from insurance indemnity payments (line 370) and on Government contracts (line 380) count as paid. If input exceeds output, line 400 excess credit plus line 410 previous excess gives line 420.
5. **Also report:** ending inventory, GST on major capital acquisitions and the range of tax invoice numbers used in the month.
6. **Invoices:** from the 2024 amendment, an "invoice" includes one issued, transmitted and received in a structured data format for automatic electronic processing ([GST (Amendment) Act No. 34 of 2024, s.2](https://media.bts.gov.bz/uploads/Act_No_34_of_2024_General_Sales_Tax_Amendment_Act_2024_5aa922a419.pdf)). BTS has published an orientation manual for issuers of electronic tax documents ([BTS home page notice](https://bts.gov.bz/)).

## Deadlines and filing

- Register on [IRIS Belize](https://irisbelize.bts.gov.bz) and obtain a TIN; the TIN is used for GST, business tax and customs ([BTS registration guide](https://bts.gov.bz/guide/registration)).
- File BTS210 and pay within fifteen days after each month (for example, the March 2026 return by 15 April 2026), online on IRIS Belize. Purchase and sales ledgers (forms 210a and 210b) support the return ([BTS tax resources](https://bts.gov.bz/tax_resources)).
- A person ceasing to be registered files within fourteen days after cancellation.

## Penalties and interest

- Paying after the due date: penalty of 10% of the tax due (line 330) and interest of 1.5% per month (line 340), as computed on BTS210.
- It is a serious offence to submit a false GST return (BTS210 declaration).

## Cross-border points

- Exported goods (First Schedule) and exported services (Second Schedule) are zero-rated; keep the export evidence the schedule requires.
- Imports of taxable goods bear GST at Customs (line 240), creditable as input tax when used for taxable supplies.
- Imported services: the reverse charge or place-of-supply treatment was not confirmed on an official page read today (see the Not yet confirmed line).

## Two worked examples that recompute

**Example 1: monthly return (simple).** A registered retailer sells BZD 100,000 of standard-rated goods and BZD 20,000 of exports in May 2026, and pays BZD 6,000 of GST on purchases. Output tax 100,000 x 12.5% = 12,500; exports at 0%; tax payable 12,500 less 6,000 = BZD 6,500, due by 15 June 2026.

```oa-check
name: Belize GST, May 2026 return
inputs:
  standard_supplies: 100000
  zero_rated_exports: 20000
  input_tax: 6000
  rate: 0.125
steps:
  - output_tax: standard_supplies * rate
  - export_tax: zero_rated_exports * 0
  - tax_payable: output_tax + export_tax - input_tax
expected:
  output_tax: 12500.00
  export_tax: 0.00
  tax_payable: 6500.00
```

**Example 2: must the business register, and the cost of paying late (decision and edge case).** A business has BZD 72,000 of supplies in the twelve months to 30 June 2026 and expects BZD 80,000 in the next twelve months. Under s.23(1)(b) the forward test alone is met (80,000 is BZD 75,000 or more), so it must register even though the past twelve months are BZD 3,000 below the limit. Once registered, if a month's tax due of BZD 6,500 is paid one month late, BTS210 adds 10% (BZD 650) and 1.5% interest (BZD 97.50), BZD 7,247.50 in total.

```oa-check
name: Belize GST registration test and late payment on BTS210
inputs:
  past_12m_supplies: 72000
  next_12m_expected: 80000
  limit: 75000
  tax_due: 6500
  months_late: 1
steps:
  - past_margin: past_12m_supplies - limit
  - forward_margin: next_12m_expected - limit
  - penalty: tax_due * 0.10
  - interest: tax_due * 0.015 * months_late
  - total_due: tax_due + penalty + interest
expected:
  past_margin: -3000.00
  forward_margin: 5000.00
  penalty: 650.00
  interest: 97.50
  total_due: 7247.50
```

## Ask the client first

1. Supplies in the last twelve months and expected in the next twelve (the BZD 75,000 test).
2. What is sold: standard-rated, zero-rated (exports, scheduled items) or exempt (financial services, education)?
3. Imports of goods, and services bought from abroad.
4. Is the business already registered with a TIN, and are returns up to date?
5. GST withheld by insurers or Government on payments to the business.

## Sources

| Source | URL | Read on |
|---|---|---|
| General Sales Tax Act, Cap. 63, Revised Edition 2011, read for s.2 (tax period), s.8 and s.9 (imposition, 12.5% and 0%), s.23 (registration limits), the return section (fifteen days) and the headings of Schedules 1 to 5 | https://media.bts.gov.bz/uploads/General_Sales_Tax_Act_2011_f573a52314.pdf | 2026-11-14 |
| General Sales Tax (Amendment) Act No. 34 of 2024, read for the arrangement of sections and the new definitions of invoice (structured electronic data) and profession | https://media.bts.gov.bz/uploads/Act_No_34_of_2024_General_Sales_Tax_Amendment_Act_2024_5aa922a419.pdf | 2026-11-14 |
| BTS210 General Sales Tax Return, read for every line from 100 to 420, the 10% penalty and 1.5% monthly interest lines | https://media.bts.gov.bz/uploads/BTS_210_GST_RETURN_MANUAL_d6b6eaa77c.pdf | 2026-11-14 |
| BTS registration guide, read for TIN registration on IRIS Belize | https://bts.gov.bz/guide/registration | 2026-11-14 |
| BTS tax resources page, read for the GST Acts, forms 210, 210a and 210b | https://bts.gov.bz/tax_resources | 2026-11-14 |
| BTS home page, read for the notice of the orientation manual for issuers of electronic tax documents | https://bts.gov.bz/ | 2026-11-14 |

Not yet confirmed: the full current zero-rated and exempt item lists (the 2011 schedules were amended by later Orders, including 2018 and agriculture and utilities amendments listed by BTS, which were not read); the old file's BZD 6,250 a month proxy for new businesses (not in s.23 as read); the treatment of imported services; the start date and scope of mandatory electronic invoicing; the consolidated Revised Edition 2020 text.
