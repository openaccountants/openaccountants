---
jurisdiction: MT
applicable: [IT-IND, IT-CORP, VAT, SC, PR, TP, XB]
not_applicable: {}
covered_by:
  IT-IND: malta-income-tax
  IT-CORP: mt-corporate-tax
  VAT: malta-vat-return
  SC: malta-ssc
  PR: malta-payroll
  TP: malta-transfer-pricing
  XB: mt-non-dom
partial: [IT-IND, IT-CORP, VAT, SC, PR, TP, XB]
---

# Malta: tax pack

**Audit status, 4 November 2026:** this pack is partial and contains confirmed errors. Reading a source, passing an arithmetic test or carrying a 2026 label does not establish that a Guide is safe to use for a filing. The [audit record](../../evidence/malta-deep-audit-20261104/README.md) identifies defects, source discrepancies, checked scopes and unverified claims.

## Named maintenance scope

Michael Cutajar's requested ongoing scope is limited to these three core Guides. This is an ownership assignment, not a new professional approval or a statement that their outstanding findings are fixed.

| Guide | Maintainer | Current state |
|---|---|---|
| [Malta individual income tax](malta-income-tax.md) | Michael Cutajar | Corrections and an authority-table discrepancy remain open |
| [Malta VAT returns](malta-vat-return.md) | Michael Cutajar | Transaction-routing and deadline corrections remain open |
| [Malta bookkeeping](malta-bookkeeping.md) | Michael Cutajar | Conditional classification and tax-deduction claims remain open |

Other Malta topics are open to contributions and review by other Maltese accountants. No person is assigned to an unclaimed topic by this audit. Existing review records naming another accountant are preserved; this audit does not extend or validate their scope. Contribution history remains in Git.

## Domains and holds

| Domain | Existing research | Status |
|---|---|---|
| IT-IND | malta-income-tax, mt-capital-gains, mt-non-dom, mt-rental-income | Partial; filing-extension, classification and property/rental findings open |
| IT-CORP | mt-corporate-tax, mt-holding-company-participation-exemption | Partial; election conditions and specialist questions open |
| VAT | malta-vat-return and reverse-charge Guides | Partial; consolidate duplicated VAT3 material after correcting the audit findings |
| SC | malta-ssc | Partial; current annual tables and eligibility discrepancies need resolution |
| PR | malta-payroll | Partial; current contribution inputs and parent-rate discrepancy remain |
| TP | malta-transfer-pricing | Partial; example eligibility and CbCR detail incomplete |
| XB | mt-non-dom, moving-to-malta-tax-residence and programme Guides | Partial; corridor remittance eligibility error and specialist conditions open |

**Do not use the two old workflows, `mt-freelance-intake` and `mt-return-assembly`, to prepare a filing package.** They route self-employed income to TA24, use incorrect provisional-tax benchmark years and quarterly contribution scheduling. This is a repository audit hold; it does not assert the live platform has withdrawn them.

The short rental method and property-transfer table also require correction before reliance. The audit includes a consolidation/withdrawal plan: preserve research and old-topic destinations, use one canonical Guide per job, and leave unsupported specialist work explicitly unclaimed. No source Guide has been deleted or silently unpublished by this change.

## Official sources

- Income Tax Act, Cap. 123: https://legislation.mt/eli/cap/123/eng
- Income Tax Management Act, Cap. 372: https://legislation.mt/eli/cap/372/eng
- Value Added Tax Act, Cap. 406: https://legislation.mt/eli/cap/406/eng
- Social Security Act, Cap. 318: https://legislation.mt/eli/cap/318/eng
- MTCA: https://mtca.gov.mt
