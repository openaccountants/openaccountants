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

**Audit status, 4 November 2026:** this pack has undergone source-backed corrections and remains partial, with unresolved rules and specialist scopes stated explicitly. Reading a source, passing an arithmetic test or carrying a 2026 label does not establish that a Guide is safe to use for a filing. The [audit record](../../evidence/malta-deep-audit-20261104/README.md) identifies defects, source discrepancies, checked scopes and unverified claims.

## Named maintenance scope

Michael Cutajar's ongoing scope is limited to these three core skills. On 5 November 2026 he confirmed that all three are his own professional work and should carry **Approved by Michael Cutajar**. That approval is recorded in each file's frontmatter. Existing source-check dates and outstanding findings remain as recorded.

| Guide | Maintainer | Current state |
|---|---|---|
| [Malta individual income tax](malta-income-tax.md) | Michael Cutajar | Filing and workflow findings corrected; parent-rate authority discrepancy held |
| [Malta VAT returns](malta-vat-return.md) | Michael Cutajar | Transaction routing and dates corrected; specialist and portal questions held |
| [Malta bookkeeping](malta-bookkeeping.md) | Michael Cutajar | Unsupported classifications and tax-deduction conclusions are held |

Other Malta topics are open to contributions and review by other Maltese accountants. No person is assigned to an unclaimed topic by this audit. Existing review records naming another accountant are preserved; this audit does not extend or validate their scope. Contribution history remains in Git.

## Domains and holds

| Domain | Existing research | Status |
|---|---|---|
| IT-IND | malta-income-tax, mt-capital-gains, mt-non-dom, mt-rental-income | Partial; audited filing, recognition and property/rental defects corrected; authority and specialist holds remain |
| IT-CORP | mt-corporate-tax, mt-holding-company-participation-exemption | Partial; election conditions corrected; unresolved floor/refund and specialist applications held |
| VAT | malta-vat-return and reverse-charge Guides | Partial; audited VAT defects corrected; VAT3 retained only as synchronised compatibility content pending controlled alias migration |
| SC | malta-ssc | Partial; current annual tables added; student eligibility discrepancy and special cases held |
| PR | malta-payroll | Partial; current contribution inputs and bonuses added; parent-rate discrepancy held |
| TP | malta-transfer-pricing | Partial; example eligibility corrected; CbCR detail and prescribed-form questions held |
| XB | mt-non-dom, moving-to-malta-tax-residence and programme Guides | Partial; corridor eligibility corrected; immigration, treaty and specialist conditions remain bounded |

**The two old workflows, `mt-freelance-intake` and `mt-return-assembly`, are quarantined to neutral document intake and routing. Do not use them to prepare a filing package.** Their former incorrect TA24 forms/boxes, provisional-tax benchmarks and quarterly contribution instructions are preserved only in the audit archive. This repository change does not assert the live platform has withdrawn or ingested them.

The audited rental-method and property-transfer errors are corrected in this batch; this does not settle every property valuation, duty or immigration situation. The audit includes a consolidation/withdrawal plan: preserve research and old-topic destinations, use one canonical Guide per job, and leave unsupported specialist work explicitly unclaimed. No source Guide has been deleted or silently unpublished by this change.

## Official sources

- Income Tax Act, Cap. 123: https://legislation.mt/eli/cap/123/eng
- Income Tax Management Act, Cap. 372: https://legislation.mt/eli/cap/372/eng
- Value Added Tax Act, Cap. 406: https://legislation.mt/eli/cap/406/eng
- Social Security Act, Cap. 318: https://legislation.mt/eli/cap/318/eng
- MTCA: https://mtca.gov.mt
