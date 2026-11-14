---
name: mt-freelance-intake
description: "Document intake and routing for a Malta self-employed or personal-tax client, basis year 2026. Collects the facts and documents, keeps the TA24, VAT, social security and provisional tax papers apart, and routes each question to the Malta skill that owns it (income tax, provisional tax, social security, payroll, VAT, rent, non-dom, crypto, capital gains). It does not compute tax, map return boxes, file, pay or certify compliance."
version: "1.0"
jurisdiction: MT
tax_year: 2026
last_updated: 2026-11-14
category: orchestrator
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: router
---

# Malta personal-tax intake and routing, basis year 2026

## Scope

This router collects facts and documents for one basis year and sends each question to the Malta skill that owns it. Basis year 2026 is year of assessment 2027. It carries no rates, no amounts and no return box numbers: each destination skill holds its own figures and sources.

It replaced `mt-return-assembly` on 14 November 2026: the two files had the same body, so one was retired. The former automated filing workflow behind both stays withdrawn, because it used the rental TA24 as the annual business return, return-box mappings with no official source, the wrong provisional-tax benchmark year and quarterly Class 2 scheduling.

Do not assume a resident is domiciled, entitled to a family rate table, or exempt from a contribution.

Built from the law: not yet approved by an accountant.

## Ask the client first

- Which basis year, and which returns or notices have already been issued (tax statement, PT notice, SSC bills)?
- Individual or entity; residence, domicile, ordinary residence and any special residence status (permanent residence, programmes)?
- Income types: employment, own business, rent, investment income, foreign income, capital gains, crypto?
- Marital status, children, custody and maintenance, for the rate table.
- Business start or cessation date, employment and contribution history, date of birth, VAT registration and cross-border supplies.

Read the documents supplied first. Ask only for missing facts that change the computation or the route. An uploaded bank debit is not proof of its tax allocation.

## The method, step by step

1. Record each source document, its period and what is missing, without inventing tax facts.
2. Keep income records, expenses, capital assets, employment statements (FS3), tax notices, VAT returns and SSC bills as separate schedules. Keep private data out of the public repository.
3. Provisional tax: obtain the PT notice and the benchmark-year self-assessment (for 2026, normally basis 2024, year of assessment 2025), not the latest profit figure. Route to [mt-estimated-tax](mt-estimated-tax.md).
4. Class 2 contributions: reconcile by contribution weeks and the actual bills and allocations, not by four quarterly totals. Route to [malta-ssc](malta-ssc.md).
5. Rent: a TA24 is the 15% final tax on rent, not the self-employed annual return. Route to [mt-rental-income](mt-rental-income.md).
6. Route every other question using the table below. Do not create return box numbers, and do not require VAT turnover to equal income without an explained timing or scope bridge.
7. List open questions and source conflicts for the practitioner. A route is not permission to file or pay.

### Topic routing

| Question | Destination | Boundary |
|---|---|---|
| Business or employment income, deductions, rate tables | [malta-income-tax](malta-income-tax.md) | Where the Act and MTCA's published table differ, that skill says which governs |
| Provisional tax | [mt-estimated-tax](mt-estimated-tax.md) | The benchmark-year return and notice, not the latest profit |
| Social security, Class 1 and Class 2 | [malta-ssc](malta-ssc.md) | No personal SSC deduction or return box that the law does not give |
| Employer payroll, FSS forms | [malta-payroll](malta-payroll.md) | The actual FS forms and that year's tables |
| VAT | [malta-vat-return](malta-vat-return.md) | Registration article, place of supply and periods need their own analysis |
| Rent | [mt-rental-income](mt-rental-income.md) | TA24 is the rental final tax |
| Selling Malta property | [mt-property-transfer-tax-the-sale-immovable](mt-property-transfer-tax-the-sale-immovable.md) | Notary collects; final tax |
| Shares and other capital gains | [mt-capital-gains](mt-capital-gains.md) | 7% provisional tax within fifteen days |
| Residence, remittances, foreign income | [mt-non-dom](mt-non-dom.md) | Check the status and spouse exclusions before the remittance basis |
| Crypto | [mt-crypto-tax](mt-crypto-tax.md) | Held receipt classes are not filled by a default |
| Company, formation or accounts | [mt-corporate-tax](mt-corporate-tax.md), [malta-formation](malta-formation.md), [malta-financial-statements](malta-financial-statements.md) | Entity work is outside personal intake |

### Routing examples

- A client supplies a TA24 and business invoices. Record the TA24 under rent, and ask for the personal return or tax statement for the business year. Do not put business fees into a TA24.
- A 2026 PT request arrives with a basis-2025 profit schedule. Record it, and ask for the PT notice and the basis-2024 self-assessment before routing to provisional tax.

## When to refuse or refer

- Hold any request for a filing package until the real form, the computation from the owning skill, the source evidence and an independent review exist.
- Refer entities, disputed residence, complex cross-border cases, historic arrears and unresolved conflicts between authorities to a practitioner.
- Do not give filing or payment instructions, return-box values or payment amounts from this router; the owning skill gives them.

## Sources

| Source | URL | Read on |
|---|---|---|
| Read for the TA24 service (myTax for residents, separate form for non-residents and companies): TA24 is the rental final tax | https://mtca.gov.mt/personal-tax/individual/tax-on-rental-income-(ta24) | 2026-11-14 |
| Read for S.L. 372.18 rules 2 and 6 (benchmark year of assessment and benchmark) | https://legislation.mt/getpdf/62220f5fe3d8c541c4ac85d4 | 2026-11-14 |
| Read for S.L. 372.16 rule 2(c) (return dates, used only to fix the year of assessment) | https://legislation.mt/getpdf/6022595cbc8272018c0f2ad2 | 2026-11-14 |

Not yet confirmed: none for routing. This router supplies no return-box mapping, computation, payment allocation or approval.
