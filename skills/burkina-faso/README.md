---
jurisdiction: BF
version: 0.2
last_updated: 2026-11-01
applicable: [IT-IND, IT-CORP, VAT, SC, PR, TP, XB]
not_applicable: {}
covered_by:
  IT-IND: bf-income-tax
  IT-CORP: bf-corporate-tax
  VAT: bf-vat
  SC: bf-social-contributions
  PR: bf-payroll
  TP: bf-transfer-pricing
  XB: bf-nonresident-services-withholding
partial:
  IT-IND: "Legacy 2025 Guide retained unchanged; current law and procedure not rebuilt."
  IT-CORP: "Legacy 2025 Guide retained unchanged; current law and procedure not rebuilt."
  VAT: "Legacy 2025 Guide retained unchanged; current law and procedure not rebuilt."
  SC: "Legacy 2025 Guide retained unchanged; CNSS and separate AMU not rebuilt."
  PR: "Legacy 2025 Guide retained unchanged; current law and procedure not rebuilt."
  TP: "2026 pricing and documentation draft only; annual form workflow, CbCR implementation and APAs incomplete; independent AI source review accepted for the stated draft scope."
  XB: "2026 non-resident services withholding draft only; treaty relief, PE, investment income, residence and exit jobs incomplete; independent AI source review accepted for the stated draft scope."
---

# Burkina Faso tax pack

**Partial local draft, 1 November 2026.** Eight legacy 2025 Guides remain unchanged. Two new 2026 tier-2 Guides have source ledgers and executable examples and have passed independent AI source review for their stated limited scope. Neither has accountant attestation. Adding two jobs does not complete [issue #444](https://github.com/openaccountants/openaccountants/issues/444).

| Domain | Guide | Actual status |
|---|---|---|
| IT-IND | [Business income](bf-income-tax.md) | Legacy 2025; needs full source rebuild |
| IT-CORP | [Corporate tax](bf-corporate-tax.md) | Legacy 2025; needs full source rebuild |
| VAT | [VAT](bf-vat.md) | Legacy 2025; needs full source rebuild |
| SC | [Social contributions](bf-social-contributions.md) | Legacy 2025; needs full source rebuild |
| PR | [Payroll](bf-payroll.md) | Legacy 2025; needs full source rebuild |
| TP | [Transfer pricing](bf-transfer-pricing.md) | 2026 draft: controlled pricing, distinct declaration/documentation size tests, July 2026 documentation contents, audit request and fines |
| XB | [Non-resident services withholding](bf-nonresident-services-withholding.md) | 2026 draft: payer/service scope, base, general and road-freight rates, declaration fields, remittance and default branches |

The unchanged [overview](bf-tax-overview.md), [formation](bf-company-formation.md) and [optimisation](bf-tax-optimization.md) remain legacy 2025 content, not current country advice. Their old rules, figures, procedures, exceptions and edge cases are explicitly preserved in the [complete old-topic destination table](../../evidence/ledgers/burkina-faso-old-topics.md). They are not vouched for by these additions.

## Evidence and limits

The two draft ledgers are [TP](../../evidence/ledgers/bf-transfer-pricing.md) and [non-resident services](../../evidence/ledgers/bf-nonresident-services-withholding.md). Every new rule maps to an act/article, an opened official URL, a short original-language quotation and an actual read date. Raw PDFs, text extraction and source images are kept outside the public repository.

The writer read the relevant articles in the official 2026 CGI and all five pages of the separately published 2026 documentation order. The latter repeals the 2022 order still reproduced in the consolidated CGI. Current law at the date read is the draft basis; there is no accountant sign-off.

Current form box identifiers and authenticated portal steps were not accessed. Do not treat the source-backed declaration fields as a verified portal walkthrough. The two Guides' `Not yet confirmed:` lines record exact unresolved items. CbCR, APAs, treaty-specific relief, investment income, permanent establishments, individual residence/foreign income, exit taxation and wider specialist regimes remain unfinished. No domain is declared inapplicable. Country coverage must continue to show all seven domains as partial.

## Review checkpoint

The [initial independent review](../../evidence/ledgers/burkina-faso-review-20261101/review.md) identified one incomplete TP documentation checklist. After repair, the [dated acceptance closure](../../evidence/ledgers/burkina-faso-review-20261101/closure-199e3df/closure.md) accepted the two limited drafts at commit `199e3dfae83beaeb0a908206b11d8317cef37c96`. Together the receipts cover 51 ledger rows, four recomputed examples and preservation checks for the eight legacy Guides. The closure records exact accepted Guide and ledger hashes; the only later Guide edit corrects the closing review-status sentence.

The coverage gaps above remain open and all seven domains remain partial. This is the local drafting checkpoint for this batch. It authorises no issue closure, merge, professional attestation or country-completion claim.
