---
jurisdiction: ML
version: 0.1
last_updated: 2026-11-01
applicable: [IT-IND, IT-CORP, VAT, SC, PR, TP, XB]
not_applicable: {}
covered_by:
  IT-IND: ml-income-tax
  IT-CORP: ml-corporate-income-tax
  VAT: ml-vat-gst
  SC: ml-payroll-social
  PR: ml-payroll-social
partial:
  IT-IND: "Legacy 2025 Guide retained unchanged; current law, scope and procedure need rebuilding."
  IT-CORP: "Legacy 2025 Guide retained unchanged; CSS is a separate levy and its 2026 treatment is unverified."
  VAT: "Legacy 2025 Guide retained unchanged; current law, scope and procedure need rebuilding."
  SC: "Legacy 2025 joint payroll/social Guide retained unchanged; contributions need primary-source rebuilding."
  PR: "Legacy 2025 joint payroll/social Guide retained unchanged; withholding and employer procedure need rebuilding."
  TP: "Missing; older online code and later amendments were not reconciled into a 2026 Guide."
  XB: "Missing; no residence, treaty, non-resident, PE or exit Guide drafted."
---

# Mali tax pack

**Partial local source-baseline draft, 1 November 2026. No new current-year coverage is claimed.** Six legacy 2025 Guides remain unchanged. A new tier-2 CSS draft reconstructs the enacted 2025 rules and two executable examples while the enacted 2026 fiscal annex remains unavailable. Its `tax_year: 2025` and explanatory notes are deliberate. Independent review of the source baseline is pending; no accountant has attested to it. This does not complete [issue #471](https://github.com/openaccountants/openaccountants/issues/471).

| Domain | Guide | Actual status |
|---|---|---|
| IT-IND | [Income tax](ml-income-tax.md) | Legacy 2025; needs primary-source rebuilding |
| IT-CORP | [Corporate income tax](ml-corporate-income-tax.md) | Legacy 2025; needs primary-source rebuilding |
| VAT | [VAT](ml-vat-gst.md) | Legacy 2025; needs primary-source rebuilding |
| SC and PR | [Payroll/social](ml-payroll-social.md) | Legacy 2025; needs primary-source rebuilding |
| TP | None | Missing; not filled with unreconciled old code |
| XB | None | Missing |

## Additional source-baseline job

The [CSS solidarity-contribution draft](ml-solidarity-contribution.md) reconstructs the enacted 2025 IBIC/IS scope, tax-exclusive turnover base, 0.5% rate, VAT-linked tax points, deduction of CSS paid, monthly reporting and article 8 penalty branches. These are verified 2025 enactment facts, not verified 2026 requirements. The draft must not determine a client's 2026 liability or filing until its source gate is closed. It is a separate levy and fills neither TP nor XB.

The [ledger](../../evidence/ledgers/ml-solidarity-contribution.md) records every new rule and figure with act/article, an opened official URL, a short French quotation and actual read date. The [complete old-topic destination map](../../evidence/ledgers/mali-old-topics.md) preserves all six legacy Guides, including [overview](ml-tax-overview.md) and [formation](ml-company-formation.md), without recertifying their claims. Full PDFs and text extractions remain outside public Git.

## Sources and exact gaps

The writer read the complete Ordonnance 2025-007 in SGG gazette pages 89–91 and the unconditional ratification, Loi 2025-022. CSS's own operative chapter and final article state no fixed term, sunset or delayed commencement. The exact first liable partial period in 2025 is not asserted. A different levy or fund's duration is not borrowed.

The writer also read enacted 2026 finance-law articles 1 and 46. Article 46 refers to fiscal Annex U, which is not printed in the retrieved gazette. A focused search of the official DGI, ministry and SGG sources did not obtain the enacted annex. The ministry's accessible 2026 publication is labelled **Projet de loi de Finances 2026**, dated 2 October 2025, and links `PLF 2026_CNT_v_26-09-2025.pdf`. That proposed bill and the proposed rectifying bill supply no enacted tax figures here. Generic 2026 collection permission and the absence of a sunset in the 2025 ordinance do not establish an unchanged 2026 rate.

The missing enacted Annex U and any relevant later amendment block current-year approval and publication. CSS form identifiers and boxes, authenticated filing/payment/confirmation steps, detailed VAT tax points, exemption/conventions, cross-border treatment, unpaid deduction timing, late-payment interest and wider sanction interaction also remain unconfirmed. All seven core domains remain applicable and partial; none is declared inapplicable. TP and XB remain missing.

## Next action

An independent reviewer must check the historical CSS baseline and its explicit 2026 source gate, recompute both examples and spot-check the old-topic map. Current-year approval requires the enacted amendment chain first. This local draft authorises no push, PR, public comment, issue closure, merge, attestation or country-completion claim.
