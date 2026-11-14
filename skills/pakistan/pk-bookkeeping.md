---
name: pk-bookkeeping
description: Use for pakistan bookkeeping and records. Read the stated period, eligibility conditions, evidence requirements, owner skills and unresolved boundaries before calculating or preparing a return.
  Use this skill whenever asked about record-keeping and bookkeeping for self-employed people and
  small businesses in Pakistan. Trigger on phrases like "Pakistan bookkeeping", "records for FBR",
  "invoice requirements Pakistan", "freelancer records Pakistan", "what records to keep FBR". Covers
  the records a business individual must keep, foreign-remittance evidence for IT exporters, invoicing,
  and retention. ALWAYS read before any Pakistan bookkeeping work.
version: 1.1
jurisdiction: PK
tax_year: 2026
last_updated: 2026-11-14
category: international
depends_on:
  - income-tax-workflow-base
tier: 2
domain: bookkeeping
type: filing-howto
---

# Pakistan bookkeeping and records v 1.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

For Pakistan business individuals, freelancers and small businesses in 2026, prepare an evidence-backed receipts/expenses ledger and reconciliation for professional review. Income tax records are governed by [ITO s.174](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf); sales-tax records have separate requirements. This is bookkeeping support, not authority to submit a return.

## Ask the client first

Obtain legal form, tax period, NTN and any federal/provincial registrations; all PKR and foreign-currency bank accounts; invoices, Upwork/Fiverr or other platform statements, refunds and fees; supplier bills, utilities/rent, equipment and subscriptions; prior returns, wealth statement and actual withholding certificates; and any pending assessment, appeal or other proceeding. For IT exports obtain each bank credit advice/e-PRC and PSEB evidence before using `pk-it-export-tax`.

## The method, step by step

1. Import actual statements and confirm their date/sign/currency conventions. Match opening balance, movements and closing balance; do not infer a bank schema or gross receipts from a platform's net credit.
2. Match income invoices to gross platform settlements, separately identifying platform fees, refunds and transfers. Record domestic and export income in separate columns. Keep the foreign-currency receipt and the evidenced PKR amount without inventing a conversion rate.
3. Match expenses to bills and payment evidence. Keep enduring equipment in an asset register for the applicable depreciation analysis, separate from ordinary expenses. Maintain vendor bills, utilities/rent receipts, subscription support and all bank statements.
4. Reconcile bank withholding to the correct taxpayer, stream and tax period. Retain prior returns and wealth reconciliations; never plug an unexplained difference or assume a tax payment is a deductible business cost.
5. Retain income-tax accounts/documents for 6 years after the end of their tax year (in words on the page), and until final decision where proceedings remain pending. The statutory limit does not apply to the s.111(2)(ii) records identified by the proviso. [ITO s.174(1)-(4)](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf).

## Boundary and exception table

| Situation | Treatment and evidence boundary | Source |
|---|---|---|
| Unsupported deduction | Commissioner may disallow or reduce it if transaction evidence cannot be provided without reasonable cause | [s.174(2)](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf) |
| Business not sales-tax registered | Keep ordinary business invoices and NTN evidence; do not label an invoice as charging sales tax without the relevant registration and liability analysis | [ITO s.174](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf) |
| Registered for federal goods or provincial services tax | Keep tax invoices and separate input/output records; load `pk-sales-tax-federal` or `pk-sales-tax-services` for that regime | [FBR sales-tax legislation register](https://fbr.gov.pk/Categ/Sales-Tax-Act-1990/301) |
| IT export evidence missing | Keep the receipt visible; do not discard credit advices/e-PRCs or certify the concession | [s.154A](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf) |

## Worked cases

These are bookkeeping reconciliations, with illustrative inputs and derived results. They determine missing evidence, not legal tax rates.

```oa-check
name: Gross platform receipts matched to bank
inputs:
  invoices: 1200000
  fees: 60000
  bank_credit: 1140000
steps:
  - expected_bank: invoices - fees
  - unexplained: bank_credit - expected_bank
expected:
  expected_bank: 1140000
  unexplained: 0
```

```oa-check
name: Separate domestic and export ledger with unsupported bank difference
inputs:
  opening_bank: 100000
  export_credits: 800000
  domestic_credits: 200000
  documented_payments: 350000
  closing_bank: 780000
steps:
  - supported_closing: opening_bank + export_credits + domestic_credits - documented_payments
  - difference: closing_bank - supported_closing
expected:
  supported_closing: 750000
  difference: 30000
```

The second case leaves 30,000 unresolved. Obtain the missing source, transfer or correction; never create a balancing expense.

## When to refuse or refer

Refuse fabricated invoices, undocumented tax credits, missing-bank-period certification and a plugged wealth reconciliation. Keep domestic/export streams separate. Refer sales-tax invoice validity, asset depreciation, non-residence, disputed expenses and retention exceptions to the applicable specialist skill/practitioner. A freelancer's tidy expense sheet does not prove tax eligibility by itself.

## Filing and payment

Deliver the ledger, asset register, bank reconciliation, withholding schedule and unresolved-items list to the return preparer; `pk-return-assembly` handles the reviewed IRIS workflow. This bookkeeping skill does not create a payment or filing confirmation.

## Completion checklist

Full-period records and currencies reconciled; gross/net and fees separated; domestic/export receipts identified; evidence for each expense/asset/withholding retained; unresolved differences visible; pending-proceeding retention checked; sales-tax records routed separately.

## Sources

| Source and actual portions read | Official URL | Read on |
|---|---|---|
| Read for ITO s.174 accounts, evidence, 6-year retention and both exceptions; s.154A exporter evidence/compliance context | https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf | 2026-11-14 |

Not yet confirmed: current tax-rule invoice fields for every business category, provincial record-retention periods, actual platform/bank export schemas and fees, and client-specific currency conversions. The older blanket NTN-invoice statement is not a substitute for the applicable tax-invoice law.
