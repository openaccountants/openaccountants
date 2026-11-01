---
name: na-vat-gst
description: >
  Namibia value-added tax, 2026: 15%, the N$1,000,000 registration threshold, zero rates, two-month periods, filing on ITAS with boxes, and penalties. Figures come from Namibian law and official pages opened on 2026-11-01. Items that could not be opened are named as not yet confirmed. Not reviewed by a licensed accountant.
version: 0.2
jurisdiction: NA
category: international
tax_year: 2026
tax_year_notes: "Individuals: year of assessment 1 March 2026 to 28 February 2027. Companies: financial year."
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Namibia VAT v0.2

> **General reference only.** This skill is general tax reference material for AI-assisted workflows. Do not rely on it to file, pay or take a position without review by a qualified professional in Namibia.

VAT Act 10 of 2000, annotated to Amendment Act 5 of 2024.

## Who this applies to

A person carrying on a taxable activity whose taxable supplies exceeded N$1,000,000 in 12 months, or will (s.15(1)). NamRA's page still says N$500,000; the Act as amended by Act 5 of 2024 says N$1,000,000 and the statute wins. Voluntary: an intending trader expecting over N$200,000 in 12 months (s.15(4)). Connected persons' supplies may be counted (s.15(2)(b)). A rise caused only by ceasing or shrinking an activity, or replacing capital goods, does not trigger registration (s.15(3)).

## Rates, bands and thresholds

| Item | Amount | Tax year | Official URL |
|---|---|---|---|
| Standard rate, supplies and imports | 15% | 2026 | https://www.lac.org.na/laws/annoSTAT/Value-Added%20Tax%20Act%2010%20of%202000.pdf (s.6(1)) |
| Compulsory registration | Over N$1,000,000 in 12 months | 2026 | https://www.lac.org.na/laws/annoSTAT/Value-Added%20Tax%20Act%2010%20of%202000.pdf (s.15(1)) |
| Voluntary registration | Over N$200,000 expected | 2026 | https://www.lac.org.na/laws/annoSTAT/Value-Added%20Tax%20Act%2010%20of%202000.pdf (s.15(4)) |
| Zero-rated | 0%: exports, international transport, services to non-residents outside Namibia, petrol and diesel, mahango and maize meal, residential electricity, water, refuse, sewerage and telecoms, residential building, livestock other than game | 2026 | https://www.lac.org.na/laws/annoSTAT/Value-Added%20Tax%20Act%2010%20of%202000.pdf (Schedule III para 2) |
| Interest on tax debt from 1 May 2026 | 10.00% | 2026 | https://www.lac.org.na/laws/2026/8864.pdf |
| Interest on tax debt from 1 November 2026 | 10.25% | 2026 | https://www.lac.org.na/laws/2026/9030.pdf |

## The base

Value of the supply. Exempt (Schedule IV): financial services listed, education, residential rental, public transport, fringe benefits, medical and paramedical services by listed persons, and others in para 2. No input tax on passenger vehicles, entertainment, club subscriptions or private use, unless s.19(2) applies ([NamRA](https://www.namra.org.na/tax-types/page/value-added-tax-vat-30120/)). Imported services: the recipient pays where the service is not used for taxable supplies (s.6(2)(c)); a registered person importing to make taxable supplies has an exempt import. Imports of goods: at entry, or on a VAT import account by the 20th of the next month, with a nil declaration if none. Keep records in English at the place of business. Tax invoices carry the words "tax invoice", both parties' details and VAT number, description, VAT and totals.

## Deadlines and filing

Two-month periods: Category A ends in January, March, May, July, September, November; Category B in even months (s.23(2)(b)). Farmers only: 2, 4, 6 or 12 months, chosen on registration; mixed activities 2 months. Return and payment: 25th of the month after the period, even if nil (s.24(1)).

Register: apply with proof of banking details, fitness certificate, founding statement and expected 12-month turnover ([NamRA](https://www.namra.org.na/tax-types/page/value-added-tax-vat-30120/)).

File on ITAS ([NamRA steps](https://www.namra.org.na/documents/cms/uploaded/how-to-file-vat-returns-on-itas-a9438c4f18.pdf)), form VAT 2:
1. Log in at https://itas.namra.org.na.
2. Returns tab, then My Returns.
3. Search Your Return, select the period, File Your Return.
4. Upload VAT summaries, bank statements, and invoices for capital goods claimed (5MB limit).
5. Enter VAT Declared and VAT Claimed. On [VAT 2](https://www.namra.org.na/documents/cms/uploaded/return-for-value-added-tax-f8b15298a9.pdf): boxes 8 trading sales, 9 capital goods sold, 10 output adjustments, 11 totals, 12 output tax to block 5; boxes 13 local purchases, 14 local capital goods, 15 imported purchases, 16 imported capital goods, 17 input adjustments, 18 totals, 19 input tax to block 6; block 7 amount due or repayable.
6. VAT Payable tab shows payable or refundable.
7. Tick the declaration, enter the verification code, Submit. Keep the confirmation.

Payment ([NamRA](https://www.namra.org.na/documents/cms/uploaded/information-brochure--tax-payments-325a997127.pdf)): EFT, direct deposit, cash or point of sale. The reference is payment type, registration office, taxpayer number, tax type and tax period. Tax type 11 is income tax; its period is the year plus a 2-digit value, "00" for final income tax.

## Penalties and interest

Late return: N$100 a day (s.67). Late payment: 10% per month or part, capped at the unpaid tax (s.68), plus interest at the rates above (s.53). Failure to register: double the output tax from when liable (s.66). Poor records: N$3,000 a day (s.69). Objection: within 90 days ([NamRA](https://www.namra.org.na/tax-types/page/value-added-tax-vat-30120/)). The 20% interest on NamRA's page predates s.53(1B); the gazetted rate governs.

## Cross-border points

Exports zero-rated if documented (Sch III para 2(a)). EPZ supplies: Sch III para 2(g) and s.6(4). Goods from Botswana, Lesotho, South Africa and Eswatini: import declaration on import.

## Two worked examples that recompute

Example 1. Output N$150,000, input N$60,000. Pay N$90,000.

```oa-check
name: VAT period
inputs:
  o: 150000
  i: 60000
steps:
  - pay: o - i
expected:
  pay: 90000.00
```

Example 2. A decision: pay late or borrow? N$90,000 paid in month 2 after the due date costs 10% twice, N$18,000, before interest. Borrowing is cheaper at any normal rate.

```oa-check
name: Late VAT
inputs:
  t: 90000
  m: 2
steps:
  - pen: min(t, t * 0.10 * m)
expected:
  pen: 18000.00
```

## Ask the client first

1. Taxable turnover over the last and next 12 months?
2. Farming only, or other activities?
3. Category A or B?
4. Exports or imported services?
5. Connected businesses?

## Sources

| Source | URL | Read on |
|---|---|---|
| VAT Act 10 of 2000, annotated (read: ss.6, 15, 23, 24, 53, 66-69, Schedules III, IV by para 2 headings) | https://www.lac.org.na/laws/annoSTAT/Value-Added%20Tax%20Act%2010%20of%202000.pdf | 2026-11-01 |
| Government Gazette 8864 GN 107 (read: notice) | https://www.lac.org.na/laws/2026/8864.pdf | 2026-11-01 |
| Government Gazette 9030 GN 299, 300 (read: notices) | https://www.lac.org.na/laws/2026/9030.pdf | 2026-11-01 |
| NamRA VAT page (read: whole page; threshold stale) | https://www.namra.org.na/tax-types/page/value-added-tax-vat-30120/ | 2026-11-01 |
| NamRA how to file VAT (read: whole) | https://www.namra.org.na/documents/cms/uploaded/how-to-file-vat-returns-on-itas-a9438c4f18.pdf | 2026-11-01 |
| NamRA form VAT 2 (read: whole) | https://www.namra.org.na/documents/cms/uploaded/return-for-value-added-tax-f8b15298a9.pdf | 2026-11-01 |

Not yet confirmed: Bread and sugar zero rating (old skill; not seen in paragraphs read, remaining Schedule III items after (aa) not fully read); refund interest rate in GN 300; fitness certificate detail; Budget 2026/27 proposals.

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
