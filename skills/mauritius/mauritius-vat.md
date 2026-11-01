---
name: mauritius-vat
description: >
  Mauritius VAT for 2026. Use to prepare, review or classify transactions for a Mauritius VAT return, Form VAT 3. Covers the 15 percent rate, the Rs 3 million registration threshold, monthly and quarterly periods, zero-rated and exempt supplies, the Rs 10 million monthly limit, reverse charge, blocked input tax, partial exemption, repayment, foreign digital suppliers, visitor refunds, freeport supplies, e-invoicing and Finance Act 2026 changes. Always read before handling Mauritius VAT work, MRA VAT returns or VAT registration questions.
jurisdiction: MU
category: international
tax_year: 2026
tax_year_notes: "Income year 1 July 2026 to 30 June 2027 (year of assessment 2027/28)"
version: 2.1
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Mauritius VAT v2.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

Tax year covered: Income year 1 July 2026 to 30 June 2027 (year of assessment 2027/28).

## Who this applies to

Anyone making taxable supplies in Mauritius in the course of business, importers, and foreign suppliers of digital services to Mauritius customers. Authority: Mauritius Revenue Authority (MRA). Currency: Mauritian rupee (MUR, Rs). Law: Value Added Tax Act. A person with only exempt supplies cannot register ([VAT FAQs](https://www.mra.mu/download/VATFAQs.pdf)). A person with only zero-rated supplies, or zero-rated and exempt supplies, is not bound to register (s.15(3)).

A client with a Global Business Licence gets specific treatment: escalate rather than classify from this skill. Minimum viable input for a return is a bank statement, from any Mauritian bank such as MCB, SBM, Absa, AfrAsia or Bank One, but VAT invoices are needed before input tax is claimed.

## Rates, bands and thresholds

| Item | Figure | Conditions | Tax year | Source |
|---|---|---|---|---|
| Standard rate | 15% | Fourth Schedule | 2026 | https://www.mra.mu/download/VATAct.pdf |
| Zero rate | 0% | Fifth Schedule, listed below | 2026 | same |
| Compulsory registration | Turnover of taxable supplies above Rs 3 million a year | Sixth Schedule, cut from Rs 6 million by Finance Act 2025 | 2026 | same |
| Tenth Schedule Part I professions | Register below the threshold | Accountants, advisers, architects, attorneys and others; not an employee alone (s.15(2)) | 2026 | same |
| Tenth Schedule Part II businesses | Register at any turnover | Banking, some management services, merchant card services | 2026 | same |
| Foreign digital suppliers | Above Rs 3 million, and not where all customers are VAT registered | From 1 October 2026; before that, any turnover (Finance Act 2026 s.25(g), s.28(2)) | 2026 | https://www.mra.mu/download/FinanceAct2026.pdf |
| Monthly return | Turnover above Rs 10 million | Second Schedule; at or below, quarterly or irrevocable monthly election (s.22(1A)) | 2026 | https://www.mra.mu/download/VATAct.pdf |
| Repayment on capital goods | Excess includes more than Rs 100,000 of input tax on capital goods | Also main zero-rated traders | 2026 | https://www.mra.mu/download/VATFAQs.pdf |
| Visitor refund floor | No refund under Rs 300 in aggregate | Before administrative charges; not spirits, wine, tobacco (VAT Regulations reg. on visitors) | 2026 | https://www.mra.mu/download/VATReg.pdf |
| E-invoicing | Fiscal invoices above Rs 100 million from 15 May 2024 (LTD), 1 August 2025 (MSTD) | Above Rs 80 million by 30 June 2026; above Rs 40 million by 1 September 2026 | 2026 | https://www.mra.mu/index.php/e-invoicing |
| Insurance premium tax | 5% on general insurance premiums | Policies from 1 January 2027 (s.53T); general insurers only | 2027 | https://www.mra.mu/download/VATAct.pdf |

Zero-rated, per the Fifth Schedule: exports under Customs control; rice, wheat flour, bread, edible oils, milk, sugar, unprocessed produce, poultry, meat, fish, tea, honey, spices, salt, fertiliser, animal feed, printed and electronic books; transport of people and goods by sea or air to or from Mauritius; duty-free shop sales; supplies to a freeport licensee for freeport activity; services to a non-resident outside Mauritius not consumed in Mauritius; CEB electricity and CWA water; photovoltaic systems; medical, hospital and dental services; public transport by public service vehicle and light rail; cooking gas up to 12 kg for domestic use; postal services (from 1 October 2026).

Exempt, per the First Schedule: educational services and approved training; most banking and other listed financial services; sale of immovable property for residential purposes, and for other purposes unless sold by a VAT-registered developer to a VAT-registered person; burial and cremation; journals and periodicals; the other listed items. Management company services to global business clients became exempt from 1 October 2026 (item 97).

## The base

**Time of supply.** From 1 October 2026 a third trigger joins invoice and payment: 3 months after delivery or performance (s.5, Finance Act 2026 s.25(b)).

**Reverse charge.** A VAT-registered person receiving services from a non-registered foreign supplier, performed or utilised in Mauritius, self-assesses and may claim the tax as input tax under s.21 (s.14). Bookkeeping result is net zero where input tax is fully allowed. SaaS bought by a registered business follows this rule.

**Blocked input tax (s.21(2)).** Supplies used for exempt supplies; cars and vehicles up to 9 seats, motorcycles and mopeds for own use, with spare parts, repairs and hire; parking for them; accommodation, catering, receptions, entertainment; fuel of heading 27.10 with stated exceptions; digital services. Quad bikes and golf cars are outside the car block. No credit without the required documents (s.21(5)).

**Partial exemption (s.21(3)).** Credit in proportion of taxable supplies to turnover, on the previous year's actual figures or estimates for a new business, adjusted at year end in the next return. The Director-General may approve another basis.

**Late claims.** Input tax not taken in its period can be taken within 24 months; Finance Act 2026 s.25(j) cut this from 36 months.

**Bad debts.** Output or input tax adjusts for a debit note, a credit note, or a debt proved bad and written off (s.21(4)).

**Visitors.** Visitor means a foreign passport holder with a valid ticket abroad. Refund goes through customs at departure, less administrative charges, or the goods are delivered free of VAT at the port or airport. Never confuse this with a registered person's repayment claim.

**Supplier patterns.** Classify from the invoice, then the rule above.

| Pattern | Treatment | Why |
|---|---|---|
| MCB, SBM, Absa, AfrAsia, Bank One | Exclude bank charges unless the invoice shows VAT | Banking services exempt |
| MRA, Customs | Exclude tax payments; check customs entries for import VAT | Not a supply |
| CSG, NSF | Exclude | Social contribution |
| CEB, CWA | Zero-rated | Fifth Schedule item 7 |
| Mauritius Telecom, Emtel, MTML | 15% on the invoice | Standard-rated telecoms |
| Google, Microsoft, AWS, unregistered | Reverse charge 15% | s.14, unless the invoice shows Mauritius VAT |

## Deadlines and filing

Filing a VAT 3:
1. Log in at [MRA e-Services](https://www.mra.mu/index.php/e-services) under Value Added Tax, or File and Pay.
2. Pick the month or quarter. Quarters end 31 March, 30 June, 30 September, 31 December.
3. Box 1.1 zero-rated exports; 1.2 other zero-rated; 1.3 taxable supplies to exempt bodies; 1.4 other taxable supplies. Box 2 deferred VAT on importation. Box 3 exempt supplies. Box 4 penalty on overclaimed excess. Box 5 total.
4. Box 6.1 to 6.6 input allowed: capital goods imported, zero-rated imports, other imports, capital goods purchased locally, zero-rated purchases, other local purchases. Box 7 input with no credit. Box 8.1 and 8.2 exempt input. Box 9 total. Box 10 input tax deductible.
5. Box 11 VAT due or excess, 5B minus 10B. Box 12 excess brought forward. Box 13 adjustments, with a statement. Box 14 result.
6. Box 15.1 to 15.3 repayment claim, capital goods and other. Box 16 excess carried forward. Boxes 17 and 18 penalties and interest. Box 19 total due.
7. Monthly filers also submit a list of taxable supplies, other than retail, with invoice number and value (s.22(1C)).
8. Pay electronically at submission, then keep the confirmation.

Due dates: 20 days after the period; one month where both return and payment are electronic ([VAT FAQs](https://www.mra.mu/download/VATFAQs.pdf), [calendar](https://www.mra.mu/important-dates)). A nil return is still due (s.22(3)). A date on a weekend or public holiday moves to the next working day. Foreign digital suppliers file within 20 days and also list supplies to Mauritius persons (s.22(4), (1E)); from 1 October 2026 they no longer appoint a tax representative (s.14A). Registration: the simplified online form on mra.mu, or via CBRIS at business registration; a certificate follows.

Hotels and tourist residences receiving over 50% in listed foreign currency file and pay 50% of the tax in that currency from 1 October 2026 (s.12(1A)).

## Penalties and interest

| Item | Figure | Conditions | Source |
|---|---|---|---|
| Late return | Rs 2,000 per month or part, cap Rs 20,000 | s.26; cap Rs 5,000 for a small enterprise | https://www.mra.mu/download/VATAct.pdf |
| Late payment | 10% of the tax | s.27(1); 2% for a small enterprise | same |
| Interest | 1% per month or part | s.27A | same |
| Failure to register | Rs 5,000 per month or part, cap Rs 50,000 | s.15B | same |
| Failure to join e-filing | Rs 5,000 per month or part, cap Rs 100,000 | s.26A, after notice | same |
| No fiscal invoice | Rs 5,000 per day, cap Rs 1 million in 12 months | s.20B from 1 October 2026 | same |
| Not using e-invoicing | Fine up to Rs 500,000 and up to 24 months | s.20E on conviction | same |
| Deferred import VAT not declared | Rs 10,000, declare next period | s.9A(3) | same |

The VAT FAQs treat a small enterprise as turnover up to Rs 10 million.

## Cross-border points

Exports need Customs evidence. Services to a non-resident are zero-rated only if the person is outside Mauritius when performed and the services are not consumed in Mauritius. A company exporting IT services meets item 6 on those facts. Freeport supplies need the buyer's licence and freeport use.

## Two worked examples that recompute

**Example 1.** Quarterly trader: standard sales Rs 1,000,000, local purchases Rs 500,000 net with valid VAT invoices. Output Rs 150,000, input Rs 75,000, payable Rs 75,000.

```oa-check
name: Quarterly return, standard sales and purchases
inputs:
  sales: 1000000
  purchases: 500000
steps:
  - output: sales * 0.15
  - input: purchases * 0.15
  - payable: output - input
expected:
  payable: 75000.00
```

**Example 2. Decision: is it worth registering voluntarily?** Consultant with Rs 2,000,000 of sales to registered businesses and Rs 400,000 of local costs. Registered: input credit Rs 60,000 and clients can reclaim. Unregistered: the Rs 60,000 is a cost. If clients are consumers, registering takes Rs 300,000 from them or from margin, so net cost Rs 240,000. Note a Tenth Schedule profession has no choice.

```oa-check
name: Voluntary registration, consumer clients
inputs:
  sales: 2000000
  costs: 400000
steps:
  - input_credit: costs * 0.15
  - output: sales * 0.15
  - net_cost_if_consumers: output - input_credit
expected:
  input_credit: 60000.00
  net_cost_if_consumers: 240000.00
```

## Ask the client first

1. Turnover of taxable supplies, last 12 months and expected?
2. Business type: is it on the Tenth Schedule?
3. Exports, zero-rated or exempt supplies, any mix?
4. Global Business Licence or freeport licence?
5. Services bought from abroad?
6. Turnover against the Rs 10 million and e-invoicing limits?

## Sources

| Source | URL | Read on |
|---|---|---|
| VAT Act consolidated to Finance Act 2026, sections read: ss.2, 5, 9A, 10 to 15B, 20A to 20E, 21, 22, 26 to 27A, 53T; First, Second, Fourth, Fifth, Sixth, Tenth and Fourteenth Schedules, in part | https://www.mra.mu/download/VATAct.pdf | 2026-11-01 |
| Finance Act 2026, read in sections 25 and 28 | https://www.mra.mu/download/FinanceAct2026.pdf | 2026-11-01 |
| VAT Regulations 1998, read in the visitor and return sections | https://www.mra.mu/download/VATReg.pdf | 2026-11-01 |
| Form VAT 3, read in full | https://www.mra.mu/download/VAT3FormNew.pdf | 2026-11-01 |
| VAT FAQs, September 2025, read in full | https://www.mra.mu/download/VATFAQs.pdf | 2026-11-01 |
| MRA e-invoicing page, read in full | https://www.mra.mu/index.php/e-invoicing | 2026-11-01 |
| MRA tax calendar, read in full | https://www.mra.mu/important-dates | 2026-11-01 |
| MRA e-Services menu, read in full | https://www.mra.mu/index.php/e-services | 2026-11-01 |

Not yet confirmed: the older Rs 2,300 minimum per invoice for tourist refunds, which is not in the Regulations we read; whether residential letting is exempt, as the old version said, which we did not find on our read of the First Schedule; the old 6 month wait for bad debts; the telecoms treatment rests on no exemption being found; the rule on freeport certificates. VAT Regulations text still mentions a 12 million rupee figure in a form template; the Second Schedule says Rs 10 million and governs. Old version said monthly filers meant large taxpayers on the 20th, and residential first sale was standard-rated; both replaced by the law above.

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
