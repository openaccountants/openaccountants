---
name: lr-tax-overview
description: "Routes Liberia tax questions across the 2026 country pack and supplies the shared tax-administration working paper: currency, period, registration, records, filing cutoffs, late filing, late payment and statutory interest. Use for Liberia tax overview, LRA registration, TIN, tax-year change, record retention, penalties or an electronic return confirmation. The Guide links income, corporate, payroll, GST, transfer pricing, cross-border and formation computations to their owning Guides instead of maintaining duplicate rate tables. It distinguishes the current source review date from accountant attestation and flags unresolved VAT commencement, assessment wording, source-chain completeness and live filing details. Every domain remains partial; Guide presence does not establish comprehensive country coverage."
jurisdiction: LR
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
category: international
version: 0.1
---

# Liberia Tax Administration and Pack Overview v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

Tax year: 2026. Read on: 2026-11-01. Source-cited country draft; currentness gaps are listed below.

## Who this applies to

Taxpayers, withholding agents and advisers assembling a Liberia 2026 working paper. This country pack is a source-cited draft and has not been independently reviewed or attested by a local accountant. The Code separately lists income tax, GST, excise, customs, real-property tax and government fees. This pack does not compute every listed tax. [s 4](https://www.lra.gov.lr/wp-content/uploads/2021/08/REVENUE-CODE-LIBERIA-REVENUE-CODE-AMENDEMENT-2020-min.pdf) [O02]

## Rates, bands and thresholds

| Rule | Condition and result | Official source |
|---|---|---|
| O03 | Statutory dollar amounts are LRD unless expressly denominated otherwise. Books can be in LRD or USD, but USD books must show LRD taxable-income and tax equivalents. USD payment translates LRD due at the CBL market rate on payment day; other foreign-exchange translations follow s 6(c). | [s 6(a),(c)](https://www.lra.gov.lr/wp-content/uploads/2021/08/REVENUE-CODE-LIBERIA-REVENUE-CODE-AMENDEMENT-2020-min.pdf) [O03] |
| O04 | The default tax year is the calendar year. A legal person other than a trust or estate needs written permission for a different twelve-month year on compelling need. Changes produce a transitional year; cessation closes the tax books at the end of the second month after cessation and produces a short year. | [s 222(a)–(d)](https://www.lra.gov.lr/wp-content/uploads/2021/08/REVENUE-CODE-LIBERIA-REVENUE-CODE-AMENDEMENT-2020-min.pdf) [O04] |
| O05 | A resident with a tax obligation must obtain one TIN, must not obtain multiple TINs, and must give it to the withholding agent. Obtaining the TIN itself is free. | [s 53(a)](https://www.lra.gov.lr/wp-content/uploads/2021/08/REVENUE-CODE-LIBERIA-REVENUE-CODE-AMENDEMENT-2020-min.pdf) [O05] |
| O06 | Keep adequate English-language books and supporting invoices, bank and customs records in Liberia; produce them on request. Retain them for seven years after the relevant period ends. | [s 55(a)–(b)](https://www.lra.gov.lr/wp-content/uploads/2021/08/REVENUE-CODE-LIBERIA-REVENUE-CODE-AMENDEMENT-2020-min.pdf) [O06] |
| O07 | The filing/payment cutoff is 11:59 pm using electronic channels and 5 pm otherwise. Keep the submission confirmation email and attached electronic form showing submission date, and successful electronic-payment notification. A filing extension under s 50(c) does not extend payment. | [amended s50(b),(g),(h)](https://www.lra.gov.lr/wp-content/uploads/2025/02/TAX-AMENDMENT-ACT-OF-DECEMBER-2024-AMENDING-THE-LIBERIA-CONSOLIDATED-REVENUE-CODE-AS-AMENDED.pdf) [O07] |

## The base

Route the job: [resident individual](lr-income-tax.md), [corporate/business tax](lr-corporate-income-tax.md), [payroll and NASSCORP](lr-payroll-social.md), [GST/VAT transition](lr-vat-gst.md), [transfer pricing](lr-transfer-pricing.md), [cross-border withholding/PE](lr-cross-border.md), [formation](lr-company-formation.md).

The ordinary income and GST amendments are read alongside the 2020 consolidation, not treated as a complete 2026 consolidation. No independent revenue-code source-chain audit is claimed. The rate-owning Guides provide computations and specific scope conditions.

## Deadlines and filing

The filing/payment cutoff is 11:59 pm using electronic channels and 5 pm otherwise. Keep the submission confirmation email and attached electronic form showing submission date, and successful electronic-payment notification. A filing extension under s 50(c) does not extend payment. [amended s50(b),(g),(h)](https://www.lra.gov.lr/wp-content/uploads/2025/02/TAX-AMENDMENT-ACT-OF-DECEMBER-2024-AMENDING-THE-LIBERIA-CONSOLIDATED-REVENUE-CODE-AS-AMENDED.pdf) [O07]

A calendar year is not compulsory where the proper written fiscal-year approval exists. Cessation and a change of year require separate short/transitional periods. [s 222(a)–(d)](https://www.lra.gov.lr/wp-content/uploads/2021/08/REVENUE-CODE-LIBERIA-REVENUE-CODE-AMENDEMENT-2020-min.pdf) [O04]

Use the official [LRA Forms and Schedules](https://www.lra.gov.lr/forms-and-schedules/) catalogue and [LITAS](https://elitas.lra.gov.lr/) link published by LRA. Select the tax kind, year and TIN; reconcile the return with the working paper and withholding credits; submit the applicable return and schedules, pay against the resulting reference and preserve submission/payment confirmation. The public catalogue was read; live portal screens, box numbers, payment references and a successful filing have not been verified. Stop before submission if the live workflow differs. [amended s50(b),(g),(h)](https://www.lra.gov.lr/wp-content/uploads/2025/02/TAX-AMENDMENT-ACT-OF-DECEMBER-2024-AMENDING-THE-LIBERIA-CONSOLIDATED-REVENUE-CODE-AS-AMENDED.pdf) [O07]

## Penalties and interest

Late filing starts at 5% for a delay not exceeding one month; subsequent months or part-months add 5% to tax plus preceding filing penalties, capped 50%. Use unpaid net liability after timely payments/withholding. Separate failure-to-file liability arises after six months for income returns or one month for other returns; do not confuse this with the ordinary monthly penalty. [s 51(a)–(b)](https://www.lra.gov.lr/wp-content/uploads/2021/08/REVENUE-CODE-LIBERIA-REVENUE-CODE-AMENDEMENT-2020-min.pdf) [O08]

Late payment of tax shown starts 5% and compounds monthly/part-monthly on tax plus that penalty, cap 25%; failure to pay correct liability also has 0.5% monthly/part-monthly, cap 50%. Partial payments reduce the subsequent balance. Where s 51(a) and s 52(a) overlap, reduce the filing penalty by the payment penalty for that same month; s 52(b) has no such reduction. [s 52(a)–(c)](https://www.lra.gov.lr/wp-content/uploads/2021/08/REVENUE-CODE-LIBERIA-REVENUE-CODE-AMENDEMENT-2020-min.pdf) [O09]

Unpaid tax also bears monthly-compounded interest using the CBL market rate under s 11. No fixed 2026 interest percentage is supplied here. [ss 11,14(a)](https://www.lra.gov.lr/wp-content/uploads/2021/08/REVENUE-CODE-LIBERIA-REVENUE-CODE-AMENDEMENT-2020-min.pdf) [O10]

Inadequate recordkeeping attracts a fine of 150% of resulting tax underpayment, in addition to applicable filing/payment penalties. This is not 150% of transaction value. Conviction conditions for repeated/substantial failure are in the same paragraph. [amended s55(e)](https://www.lra.gov.lr/wp-content/uploads/2025/02/TAX-AMENDMENT-ACT-OF-DECEMBER-2024-AMENDING-THE-LIBERIA-CONSOLIDATED-REVENUE-CODE-AS-AMENDED.pdf) [O11]

The 2026 amendment adds offences for facilitating tax evasion, including advisers/accountants, and changes evasion/knowing noncompliance penalties. These require legal review; routine late filing is not itself a conviction. [amended ss 76,90–92](https://www.lra.gov.lr/wp-content/uploads/2026/04/LRC-Amendment-December-2025.pdf) [O12]

The 2026 amended s74(d) appears to omit the ordinary assessment lookback duration while retaining distinct exception periods. This draft does not silently reinsert the older seven-year wording. Take an actual assessment/protest to a qualified Liberian practitioner before applying a limitation defence. [amendeds74(d), physicalpage7](https://www.lra.gov.lr/wp-content/uploads/2026/04/LRC-Amendment-December-2025.pdf) [O14]

## Cross-border points

Treaties in force and anti-abuse conditions are addressed by [Cross-border](lr-cross-border.md). Keep LRD statutory figures distinct from expressly USD amounts; do not apply a made-up exchange rate. [s 6(a),(c)](https://www.lra.gov.lr/wp-content/uploads/2021/08/REVENUE-CODE-LIBERIA-REVENUE-CODE-AMENDEMENT-2020-min.pdf) [O03]

## Two worked examples that recompute

### Late filing compounds until its own cap

Assume unpaid net tax 100,000 and three chargeable filing months, no simultaneous s 52(a) penalty and no additional failure-to-file liability. Filing penalty after one month 5,000, after two 10,250, after three 15,762.50, below the 50% cap. The 5% is not simply multiplied by three. [s 51(a)–(b)](https://www.lra.gov.lr/wp-content/uploads/2021/08/REVENUE-CODE-LIBERIA-REVENUE-CODE-AMENDEMENT-2020-min.pdf) [O08]

```oa-check
name: Late filing compounds until its own cap
inputs:
  tax: 100000
steps:
  - month1: tax * 0.05
  - month2: month1 + (tax + month1) * 0.05
  - month3: month2 + (tax + month2) * 0.05
  - capped: min(month3, tax * 0.50)
expected:
  month1: 5000
  month2: 10250
  month3: 15762.5
  capped: 15762.5
```

### Coordinate filing and payment penalties

Assume 100,000 unpaid tax, first late month, both s51(a) and 52(a), with correct-liability s52(b) also applicable. Initial filing 5,000 is reduced by shown-tax payment penalty 5,000 to zero. Add the separate 0.5% correct-liability penalty 500: total 5,500 before statutory interest, not 10,500. No criminal default assumed. [s 52(a)–(c)](https://www.lra.gov.lr/wp-content/uploads/2021/08/REVENUE-CODE-LIBERIA-REVENUE-CODE-AMENDEMENT-2020-min.pdf) [O09]

```oa-check
name: Coordinate filing and payment penalties
inputs:
  tax: 100000
steps:
  - initial_filing: tax * 0.05
  - shown_payment: tax * 0.05
  - net_filing: max(0, initial_filing - shown_payment)
  - correct_payment: tax * 0.005
  - total: net_filing + shown_payment + correct_payment
expected:
  initial_filing: 5000
  shown_payment: 5000
  net_filing: 0
  correct_payment: 500
  total: 5500
```

## Ask the client first

- Taxpayer entity, TIN, residence, year and tax kind.
- Actual submission/payment dates, confirmations, extensions and balances.
- English-language books, source records and exchange-rate evidence.
- Notices, prior returns, withheld credits, minimum-tax vintages and legal disputes.

## Sources

| Source and actual scope read | Official URL | Read on |
|---|---|---|
| December 2024 general amendment, approved 17 December/printed 20 December 2024, substantive pages 1–9 | https://www.lra.gov.lr/wp-content/uploads/2025/02/TAX-AMENDMENT-ACT-OF-DECEMBER-2024-AMENDING-THE-LIBERIA-CONSOLIDATED-REVENUE-CODE-AS-AMENDED.pdf | 2026-11-01; read in part, specific scope in first column |
| Revenue Code 2020, selected general, income, nonresident, filing and GST provisions | https://www.lra.gov.lr/wp-content/uploads/2021/08/REVENUE-CODE-LIBERIA-REVENUE-CODE-AMENDEMENT-2020-min.pdf | 2026-11-01; read in part, specific scope in first column |
| LRA Forms and Schedules, named return/schedule links read; not a completed portal filing | https://www.lra.gov.lr/forms-and-schedules/ | 2026-11-01; read in part, specific scope in first column |
| December 2025 amendment, approved 24 March/printed 1 April 2026, cover/preliminary/amended 63,74,76,79,90–92,803,805,806,1000,1021; excise schedule not used | https://www.lra.gov.lr/wp-content/uploads/2026/04/LRC-Amendment-December-2025.pdf | 2026-11-01; read in part, specific scope in first column |

Not yet confirmed: Defective ordinary assessment-period wording in the 2026 amendment; current CBL interest rate and administrative flat penalties; complete tax-amendment/inflation chain; operative VAT commencement; property/customs/excise computations, live return boxes and professional attestation.

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
