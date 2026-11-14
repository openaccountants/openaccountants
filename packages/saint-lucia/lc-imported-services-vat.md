---
name: lc-imported-services-vat
description: >
  Saint Lucia VAT on services bought from abroad for 2026. Covers recipient liability
  under section 9(2)(c), who pays under section 28(3) (overseas businesses supplying a
  person or local branch, registered recipients using the service outside taxable
  supplies, and non-registered recipients below the threshold or not making taxable
  supplies), the local branch rule, the import declaration and payment within 21 calendar
  days after the tax period, the time of import (section 26) and the 12.5% rate. Trigger
  phrases include Saint Lucia imported services VAT, reverse charge Saint Lucia, foreign
  consultant VAT Saint Lucia.
version: 1.0
jurisdiction: LC
tax_year: 2026
last_updated: 2026-11-14
category: international
type: situation-rules
domain: vat-gst
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
---

# Saint Lucia VAT on imported services

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

VAT on imports of services into Saint Lucia in 2026 under the Value Added Tax Act (Revised Laws 2023). Covers who is liable, the declaration and payment, timing and the rate. Amounts are EC$. Registration, rates on local supplies and returns are in [lc-vat](lc-vat.md). Withholding tax, treaty relief, related-party valuation and input deduction are outside this skill.

## Ask the client first

1. Where is the supplier established and does it carry on business from outside Saint Lucia?
2. Is the recipient registered for VAT? Does it make taxable supplies, exempt supplies or both?
3. What will the service be used for?
4. Is the recipient a local branch or affiliate of a foreign business?
5. Contract, invoice and service period (for the time of import), and the value excluding VAT.

## The method, step by step

### Rates, bands and thresholds

| Item | 2026 figure and conditions | Official source |
|---|---|---|
| Liability | Tax on an import of services is paid by the recipient (s.9(2)(c)) | [VAT Act s.9](https://attorneygeneralchambers.com/laws-of-saint-lucia/value-added-tax-act/section-9) |
| Rate | 12.5% of the value of taxable services imported (s.10(1)) | [VAT Act s.10](https://attorneygeneralchambers.com/laws-of-saint-lucia/value-added-tax-act/section-10) |
| Declaration and payment | Import declaration (approved form) and payment within 21 calendar days after the tax period of the import, except where s.4(12) applies (s.28(1), (2)) | [VAT Act s.28](https://attorneygeneralchambers.com/laws-of-saint-lucia/value-added-tax-act/section-28) |
| Who pays, s.28(3) | (a) an overseas business supplying a person or local branch in Saint Lucia; (b) a registered recipient if the import is not for use in making taxable supplies; (c) a non-registered recipient, whether below the s.12 threshold or not making taxable supplies | same |
| Local branch, s.28(4) | Treated as a person separate from its nonresident home office | same |
| Time of import | Section 18 applied as if the import were a supply of services (s.26) | [VAT Act s.26](https://attorneygeneralchambers.com/laws-of-saint-lucia/value-added-tax-act/section-26) |

### Steps

1. **Is it an import of services** by a supplier established outside Saint Lucia? Check exemptions and s.4(12) first.
2. **Recipient status:** registered and using the service to make taxable supplies, not liable under s.28(3)(b); registered and using it otherwise, liable; non-registered, liable whatever its turnover.
3. **Time of import:** apply the s.18 time-of-supply rules (invoice, payment, performance) as for a service; the bank payment date is not automatically the tax point.
4. **Tax:** value excluding VAT x 12.5%.
5. **Declare and pay** within 21 calendar days after the tax period of the import.

## Boundary and exception table

| Situation | Treatment | Source |
|---|---|---|
| "We are below the VAT threshold" | Not an answer: non-registered recipients below the threshold are liable | [VAT Act s.28(3)(c)](https://attorneygeneralchambers.com/laws-of-saint-lucia/value-added-tax-act/section-28) |
| "We are VAT registered" | Not an answer either: liable if the service is not used for taxable supplies | [VAT Act s.28(3)(b)](https://attorneygeneralchambers.com/laws-of-saint-lucia/value-added-tax-act/section-28) |
| Mixed taxable and exempt use | Not resolved in s.28(3)(b); establish actual use and refer | same |
| Local subsidiary billed by its parent abroad | Branch or affiliate is a separate person; import VAT applies | [VAT Act s.28(4)](https://attorneygeneralchambers.com/laws-of-saint-lucia/value-added-tax-act/section-28) |
| Input credit for import VAT | Do not assume a matching credit; check entitlement | not covered |

## Worked cases

### Case 1: non-registered business buys foreign consulting

A non-registered business with turnover of EC$200,000 buys consulting worth EC$10,000 from an overseas firm. It is liable under s.28(3)(c): VAT 1,250, declared and paid within 21 days after the tax period.

```oa-check
name: Saint Lucia import VAT on 10,000 of services
inputs:
  value: 10000
steps:
  - vat: value * 0.125
  - total_cost: value + vat
expected:
  vat: 1250
  total_cost: 11250
```

### Case 2 (decision): registered recipient, taxable or exempt use?

A registered company buys EC$24,000 of foreign software services. If it uses them to make its taxable supplies, s.28(3)(b) does not make it liable: import VAT 0. If it uses them for an exempt activity, it pays 3,000. Record the use with evidence before deciding.

```oa-check
name: Saint Lucia registered recipient, taxable against exempt use
inputs:
  value: 24000
steps:
  - vat_taxable_use: value * 0
  - vat_exempt_use: value * 0.125
  - difference: vat_exempt_use - vat_taxable_use
expected:
  vat_taxable_use: 0
  vat_exempt_use: 3000
  difference: 3000
```

## When to refuse or refer

- Mixed-use services, related-party valuation, VAT-inclusive contracts.
- Withholding tax and treaty questions: a separate matter.
- Section 4(12), zero-rating and exemptions: read the Act.

## Filing and payment

1. Complete the import declaration in the form approved by the Comptroller (s.28(2)).
2. Pay within 21 calendar days after the tax period in which the services were imported (s.28(1)(b)).
3. Keep the contract, supplier identity and location, service description, use analysis, valuation, tax point, declaration and receipt together.

## Completion checklist

- Import of services confirmed; exemptions checked.
- Recipient status and use recorded.
- Time of import fixed under s.18.
- 12.5% declared and paid within 21 days.

## Sources

| Source | URL | Read on |
|---|---|---|
| VAT Act s.9, Revised Laws 2023: read for s.9(2)(c), import of services tax paid by the recipient | https://attorneygeneralchambers.com/laws-of-saint-lucia/value-added-tax-act/section-9 | 2026-11-14 |
| VAT Act s.10: read for the 12.5% rate on imported services | https://attorneygeneralchambers.com/laws-of-saint-lucia/value-added-tax-act/section-10 | 2026-11-14 |
| VAT Act s.26: read for the time of import of services | https://attorneygeneralchambers.com/laws-of-saint-lucia/value-added-tax-act/section-26 | 2026-11-14 |
| VAT Act s.28: read for the declaration, 21-day payment, s.28(3) liability cases and s.28(4) branches | https://attorneygeneralchambers.com/laws-of-saint-lucia/value-added-tax-act/section-28 | 2026-11-14 |

Not yet confirmed: the treatment of mixed-use imports; the text of s.4(12) and s.18 (not opened); the IRD imported-services brochure (returned 404 on 22 October 2026, not retried); post-2023 amendments.
