---
name: td-tax-overview
description: "Route Chad tax and company compliance work for 2026 to the country’s substantive Guides and preserve the jobs that remain unresolved. Covers individual categories, company profit and minimum tax, VAT, payroll and social contributions, foreign related-party documentation, company formation and annual reporting, and the narrow September import-eligibility job. Use for Chad tax overview, country intake, DGI obligations, country-pack completeness or a multi-tax working-paper plan. Figures and deadlines stay in their owning Guide rather than being duplicated here. Two reconciliation cases distinguish remaining payments from potential credits. The pack remains partial and neither this router nor an AI source review establishes a filing-ready return or accountant attestation."
jurisdiction: TD
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
category: orchestrator
version: 1.1
---

# Chad tax working-paper router v1.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Use this2026 router for Chad individuals, employers, companies and foreign-connected transactions. It selects the country working papers and preserves unresolved jobs; it does not calculate a return from legacy headline figures. The ordinary legal baseline is the official CGI2025 reconciled with the enacted2026 finance law. Each destination records its precise sources and gaps. The country pack remains partial; no accountant has attested to these AI drafts. [Official CGI archive](https://web.archive.org/web/20250720004455id_/https://www.finances.gouv.td/index.php/le-ministere/le-ministre/item/download/438_afa372566d4acca63cb857e846d67eef); [LF2026](https://ecofinances.gouv.td/wp-content/uploads/2026/06/Loi-n008-AN-SENAT-2025-Portant-loi-de-Finances-2026-LF-2026.pdf).

## Rates, bands and thresholds

Each figure has one home. Open the substantive Guide before deciding a rate, threshold or filing period.

| Job and population | Rule location | Official baseline |
|---|---|---|
| Individual labour, rental and other capital categories | [Income tax](td-income-tax.md), annual scale and supported salary base | [LF3–5,8,14–15](https://ecofinances.gouv.td/wp-content/uploads/2026/06/Loi-n008-AN-SENAT-2025-Portant-loi-de-Finances-2026-LF-2026.pdf) |
| Ordinary company profit, territorial base, losses and minimum | [Corporate tax](td-corporate-income-tax.md) | [CGI129–152](https://web.archive.org/web/20250720004455id_/https://www.finances.gouv.td/index.php/le-ministere/le-ministre/item/download/438_afa372566d4acca63cb857e846d67eef) |
| VAT principal, additional centimes, input support and period | [VAT](td-vat-gst.md) | [LF29–35,73](https://ecofinances.gouv.td/wp-content/uploads/2026/06/Loi-n008-AN-SENAT-2025-Portant-loi-de-Finances-2026-LF-2026.pdf) |
| Employer/employee social contributions and employer taxes | [Payroll/social](td-payroll-social.md) | [CNPS employer Guide](https://web.archive.org/web/20240717045908id_/https://cnps-tchad.com/wp-content/uploads/2021/06/GUIDE-DE-LEMPLOYEUR.pdf), [CGI171–190](https://web.archive.org/web/20250720004455id_/https://www.finances.gouv.td/index.php/le-ministere/le-ministre/item/download/438_afa372566d4acca63cb857e846d67eef) |
| Foreign related-party flows and documentation | [Transfer pricing](td-transfer-pricing.md) | [CGI41,1000](https://web.archive.org/web/20250720004455id_/https://www.finances.gouv.td/index.php/le-ministere/le-ministre/item/download/438_afa372566d4acca63cb857e846d67eef) |
| Formation, capital, audit and ordinary annual reporting | [Formation/reporting](td-company-formation.md) | [OHADA company law](https://biblio.ohada.org/doc_num.php?explnum_id=2032), [accounting law](https://biblio.ohada.org/doc_num.php?explnum_id=2061) |
| September listed-goods import eligibility | [Import eligibility](td-import-exemption-eligibility.md), limited accepted scope and wheat hold | [Signed September order](https://ecofinances.gouv.td/wp-content/uploads/2026/09/Arrete-N135-Exoneration-des-droits-et-taxes-sur-les-produits09092026164852.pdf) |

## The base

1. Identify legal person, fiscal domicile/source, activities, ownership, year/period and actual operations. Keep separate entities' accounts and source documents separate.
2. Route salary and personal categories to income, company profits to corporate, supplies to VAT, workers to payroll, foreign controlled transactions to TP and entity/reporting events to formation. One transaction can need multiple working papers; documentation for one tax does not resolve another.
3. Record inputs, proposed treatment, source/article, evidence, calculation, credits/payments and unresolved items for each job. Use the destination's explicit condition and source date; do not use this router to bypass its holds.
4. Reconcile approved liabilities and payments by taxpayer, tax and period. Separate numerical reconciliation from legal permission to credit/offset: an arithmetical total alone is not a payment instruction.
5. Keep a completion table. Income business-profit/disposal and live payroll/annual-return details, corporate depreciation/advance references, VAT regime/commodity/platform issues, CNPS current/special cases, national formation procedure, wider cross-border/property/customs and specialist accounting jobs remain open as described in the README. Presence of a Guide is not completion of a domain.

## Deadlines and filing

Confirm the actual civil/accounting period, legal taxpayer, assigned office, prescribed form and current channel in each substantive Guide. Annual corporate accounts, corporate returns, monthly VAT/payroll, CNPS periods and transaction withholding are separate calendars. The old overview's undifferentiated annual corporate deadline has moved to the corporate Guide with return/payment distinction. No new general individual-return deadline is invented. Live form/box/payment-reference gaps prevent a filing-ready status.

## Penalties and interest

Use the offence-specific source in the owning Guide. Determine the failed obligation, due date, notice, tax base, delay and statutory cap before calculating. A combined total of all possible penalties is not a valid assessment. National registry penalties and several cumulative interpretations remain held.

## Cross-border points

Residence/source, corporate PE, related-party deductions, collection tax and customs are separate questions. The relevant domestic provisions and any actual convention must be read for the payment and parties. The country pack has no comprehensive treaty-rate table, foreign-service withholding resolution, foreign-credit/exit method, property-gain computation or complete customs claim. The September import Guide retains its narrower independently accepted scope; its wheat hold remains.

## Two worked examples that recompute

### Reconcile two separately approved liabilities

Two already-approved working papers for the same taxpayer/period show hypothetical liabilities450,000 and150,000. The first has payments400,000; the second150,000. Track remaining amounts50,000 and0, then total50,000. These are reconciliation inputs, not statutory rates or a combined return.

```oa-check
name: Reconcile supported liabilities without inventing rates
inputs:
  liability_a: 450000
  liability_b: 150000
  paid_a: 400000
  paid_b: 150000
steps:
  unpaid_a: max(0, liability_a - paid_a)
  unpaid_b: max(0, liability_b - paid_b)
  remaining: unpaid_a + unpaid_b
expected:
  unpaid_a: 50000
  unpaid_b: 0
  remaining: 50000
```

### Decide whether a simple net total is sufficient

Working paperA has liability450,000 and payments500,000; B has liability150,000 and payments100,000. Track A's50,000potential credit separately and B's50,000unpaid. Their aggregate signed balance is zero, but B's payment requirement is still unresolved until legal credit/offset authority is established. This is a preparation control, not a claim that every cross-tax offset is prohibited.

```oa-check
name: Separate potential credit from unresolved payment
inputs:
  liability_a: 450000
  paid_a: 500000
  liability_b: 150000
  paid_b: 100000
steps:
  potential_credit_a: max(0, paid_a - liability_a)
  unpaid_b: max(0, liability_b - paid_b)
  aggregate_signed: liability_a + liability_b - paid_a - paid_b
expected:
  potential_credit_a: 50000
  unpaid_b: 50000
  aggregate_signed: 0
```

## Ask the client first

- Which taxpayers, fiscal homes, activities, ownership and periods are involved?
- What operations, workers, foreign counterparties and entity/reporting events need a working paper?
- What accounts, contracts, invoices, payroll and official status/registration evidence exist?
- What returns, payments, credits, notices and near-term deadlines already exist?
- Which unresolved job changes whether a return/payment can be completed?

## Sources

| Primary source | Read on | Scope |
|---|---|---|
| [Official CGI2025 ministry archive, capture2025-07-20](https://web.archive.org/web/20250720004455id_/https://www.finances.gouv.td/index.php/le-ministere/le-ministre/item/download/438_afa372566d4acca63cb857e846d67eef) |2026-11-01| Income, company, VAT, employer-tax and reporting excerpts described in each destination ledger; not entire code |
| [Enacted LF2026](https://ecofinances.gouv.td/wp-content/uploads/2026/06/Loi-n008-AN-SENAT-2025-Portant-loi-de-Finances-2026-LF-2026.pdf) |2026-11-01| Relevant old/new amendments as recorded in destination ledgers; router adds no new rate or filing-date claim |
| [OHADA company law](https://biblio.ohada.org/doc_num.php?explnum_id=2032) and [accounting law](https://biblio.ohada.org/doc_num.php?explnum_id=2061) |2026-11-01| Formation/reporting researcher read the exact capital, audit, accounts and timetable clauses listed in that Guide |
| [CNPS employer Guide, dated archive](https://web.archive.org/web/20240717045908id_/https://cnps-tchad.com/wp-content/uploads/2021/06/GUIDE-DE-LEMPLOYEUR.pdf) |2026-11-01| Actual contribution guidance and source-currentness qualification recorded in payroll ledger |

Not yet confirmed: all substantive holds listed in the README and destination Guides, including comprehensive later-law/implementation updates, live filing screens, wider cross-border, property/compliance and specialist accounting scope. The router does not close those gaps. Cases are hypothetical reconciliation controls, not sourced tax amounts. For independent AI source review and its limits, see the [country README](README.md). No accountant attestation.

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
