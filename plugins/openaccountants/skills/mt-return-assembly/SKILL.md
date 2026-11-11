---
name: mt-return-assembly
description: "Neutral document intake and routing for Malta personal-tax research. Does not compute tax, assemble a filing-ready package, map official return boxes, file, pay or certify compliance."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/mt-return-assembly"
  jurisdiction: "MT"
  tax_year: "2026"
  last_updated: "2026-11-08"
---

# Malta personal-tax routing v0.3

**Source-cited draft. Restricted to neutral document collection and routing.** The former automated filing workflow is quarantined because it used the rental TA24 as the annual business return, unsupported box mappings, the wrong provisional-tax benchmark and quarterly Class 2 scheduling. This router does not produce filing instructions, return-box values, payment amounts or a filing-ready package.

## Scope

Collect facts and documents for a specific basis year and route questions to the relevant Malta Guide. Basis year 2026 is assessment year 2027. Do not assume the taxpayer is domiciled in Malta, entitled to a family table or exempt from a contribution merely because they are resident.

## Ask the client first

- Which basis year, and which returns or notices have already been issued?
- Individual or entity; residence, domicile, ordinary residence and any special legal residence status?
- Employment, own business, rent, investment income, foreign income or capital gains?
- Relevant marital status, children, custody/maintenance and citizenship/status facts?
- Actual business start/cessation date, employment/contribution history, date of birth, VAT registration and cross-border supplies?

Read provided documents first. Ask only for missing facts that affect the computation or route. An uploaded bank debit is not proof of its tax allocation.

## The method, step by step

1. Record source documents, periods and missing items without inventing tax facts.
2. Keep income records, expenses, capital assets, employment statements, tax notices, VAT returns and SSC bills as separate schedules. Keep private data outside the public repository.
3. Obtain the actual PT notice and benchmark-year self-assessment. Ordinarily 2026 PT refers to basis 2024 / assessment 2025, not basis 2025. An override or missing-return history needs the detailed PT Guide.
4. Class 2 is reconciled by contribution weeks and three four-monthly periods, not four quarterly totals. Obtain the actual bills and allocations.
5. Route using the table below. Do not manufacture return box numbers or require VAT turnover to equal income without an explained timing/scope bridge.
6. List unresolved questions and source discrepancies. A source-cited draft is not a professional approval or permission to file/pay. A qualified practitioner must determine the actual return and review any eventual computation outside this neutral router.

## Topic routing

| Question | Destination | Boundary |
|---|---|---|
| Personal business/employment income, deductions, family table | [Malta income tax](../malta/malta-income-tax.md) | Parent with one qualifying child above €60,000: compute with the Act's €10,270 and say that MTCA's table shows €10,275 ([Act III of 2026, art. 19](https://legislation.mt/getpdf/69d8ed326fe5fd3994d17430)) |
| Provisional tax | [Estimated tax](../malta/mt-estimated-tax.md) | Actual benchmark-year return and notice, not the latest profit figure |
| Personal contributions | [Social security](../malta/malta-ssc.md) | No unsupported personal SSC deduction or fictitious return box |
| Payroll records | [Payroll](../malta/malta-payroll.md) | Actual FS forms and applicable annual tables |
| VAT | [VAT return](../malta/malta-vat-return.md) | VAT regime, place of supply and periods need their own analysis |
| Rent at final tax | [Rental income](../malta/mt-rental-income.md) | TA24 is rental final tax, not the annual self-employed return |
| Residence, remittances and foreign income | [Non-dom](../malta/mt-non-dom.md) | Apply legal-status and spouse exclusions before remittance treatment |
| Crypto | [Crypto](../malta/mt-crypto-tax.md) | Held DeFi and recognition questions cannot be filled by a default |

## Worked cases

**Document-routing example 1.** A taxpayer supplies a TA24 rental submission and business invoices. Record the rental submission separately and request the actual personal income tax return or notice for the business year. Do not enter business fees into a fictional TA24 Box 1.

**Document-routing example 2.** A 2026 PT request arrives with a basis-2025 profit schedule. Record that document but request the PT notice and basis-2024 self-assessment before routing to the PT computation. Do not use basis-2025 profit as the 2026 benchmark.

## Deadlines and filing boundary

This router gives no filing or payment instructions. Calendar context only: MTCA's 3 June 2026 notice extended both manual/electronic individual assessment-2026 returns and the related tax to **31 July 2026**. The general statutory assessment-2027 individual date is **30 June 2027**, subject to any later notice. Confirm the actual year and notice before a practitioner prepares instructions.

## When to refuse or refer

Hold any requested filing package until the genuine form, computation, source evidence and independent review exist. Refer entity, disputed residence, complex cross-border, historic arrears and unresolved authority discrepancies to the appropriate practitioner. Never treat self-check failure as a reason to publish a complete filing-ready output anyway.

## Archive and old-topic destinations

The complete superseded body is retained at [personal archive](../../evidence/malta-deep-audit-20261104/personal-archive/mt-return-assembly.md). The [changed-claim ledger and full old-topic destination table](../../evidence/malta-deep-audit-20261104/ledgers/personal-mt-return-assembly.md) preserves every former section and identifies its safe route or quarantine. Archive content is historical research, not operative instructions.

## Sources

| Source | URL | Read on |
|---|---|---|
| MTCA TA24 rental service | https://mtca.gov.mt/personal-tax/individual/tax-on-rental-income-%28ta24%29 | 2026-11-04 |
| PT Rules, S.L. 372.18, rules 2–7 | https://legislation.mt/getpdf/62220f5fe3d8c541c4ac85d4 | 2026-11-04 |
| Social Security Act, article 11 | https://legislation.mt/getpdf/69d6033d6fe5fd3994d1710c | 2026-11-04 |
| MTCA assessment-2026 filing/payment extension | https://mtca.gov.mt/news-results-page/2026/06/03/tax-returns-submission-deadline | 2026-11-04 |
| Statutory Dates Rules, S.L. 372.16, rules 2 and 5 | https://legislation.mt/getpdf/6022595cbc8272018c0f2ad2 | 2026-11-04 |
| Act III of 2026, art. 19: ITA art. 56(1)(b)(iv)(d), subtraction €10,270 | https://legislation.mt/getpdf/69d8ed326fe5fd3994d17430 | 2026-11-08 |

Not yet confirmed: no official personal-return box mapping, complete tax computation, payment allocation or professional approval is supplied by this neutral router. Do not treat it as a filing package.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-08. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `mt-return-assembly` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/mt-return-assembly. If neither is available, confirm every figure against the official source pages cited above before relying on it.
