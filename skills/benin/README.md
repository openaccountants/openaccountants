---
jurisdiction: BJ
applicable: [IT-IND, IT-CORP, VAT, SC, PR, TP, XB]
not_applicable: {}
covered_by:
  XB: bj-cross-border-withholding
partial:
  IT-IND: "Monthly salary ITS refreshed; Rental IRF and annual TFU jobs added as independently source-reviewed partial drafts; business/capital and exceptional-pay computations remain open."
  IT-CORP: "Ordinary IS working paper refreshed; all special expense/incentive/sector and authenticated filing cases not completed."
  VAT: "Monthly working paper refreshed; threshold ministerial order, product classification and authenticated workflows remain open."
  SC: "CNSS source failed in direct/web/ordinary browser; current bases, rates, ceilings and CNSS filing not verified."
  PR: "VPS and salary schedules refreshed; CNSS and full authenticated payroll filing remain open."
  TP: "Pricing/reporting screen added; current forms, documentation order detail and CbCR exchange/secondary application remain open."
  XB: "Domestic withholding screen added; individual treaties, special distributions/gains, platform commencement and authenticated filing remain open."
---

# Benin: partial 2026 tax pack

Six legacy Guides have local 2026 replacements and two missing jobs have local drafts. All seven tax domains remain partial. Independent AI source review and focused repair closure passed on 1 November 2026 for the bounded jobs at candidate `3a14e7b7bbb9ac80425e046325b0b946e66fb927`. No accountant has attested to this version, and no authenticated filing is certified.

| Domain | Guide | Reviewed job boundary |
|---|---|---|
| IT-IND | [Salary ITS](bj-income-tax.md) | Monthly salary working paper; other personal-income classes remain separate |
| IT-CORP | [Corporate IS](bj-corporate-income-tax.md) | Ordinary profit/minimum and instalment working paper with sector/incentive gates |
| VAT | [VAT](bj-vat-gst.md) | Monthly calculation for confirmed VAT status, deductions and platform-place screen |
| SC and PR | [Payroll VPS](bj-payroll-social.md) | Employer tax schedule; CNSS is explicitly not verified |
| TP | [Transfer pricing](bj-transfer-pricing.md) | Pricing evidence and separate annual-return/documentation/CbCR screens |
| XB | [Cross-border withholding](bj-cross-border-withholding.md) | Domestic-law classification; unresolved treaty/special cases held |

[Formation](bj-company-formation.md) covers SARL/SA packet and capital/fee reconciliation. [Overview](bj-tax-overview.md) routes the pack and owns general DGI sanctions. Every legacy topic, including unverified items, is mapped in `evidence/ledgers/benin-old-topics.md`.

The official 2026 CGI was fetched from the tax authority's current website-configured document host, along with the signed June rectifying law. The code only consolidates the original finance law, so the relevant rectifying-law overlays were read separately. Read scopes and dates are stated in each Guide. Source retrieval is not treated as a whole-document review. Full source captures remain outside Git.

Tracked by [BJ issue #446](https://github.com/openaccountants/openaccountants/issues/446). This is one local country batch; no generated bundles or inventory files are edited.

## Independent source review

The [initial review](../../evidence/ledgers/benin-review-20261101/review.md) checked 113 ledger rows, 81 legacy-topic destinations and 16 examples. The [focused closure](../../evidence/ledgers/benin-review-closure-20261101/review.md) closes its three findings and six destination corrections. Both original findings and separate repair evidence are preserved. Acceptance covers the stated partial preparation jobs only. All seven domains remain partial, CNSS remains unverified, and neither accountant attestation nor an authenticated filing is claimed.

## Property and rental additions, 1 November 2026

Two distinct partial jobs supplement the eight preserved Guides, with [independent source review](../../evidence/ledgers/benin-property-review-20261101/review.md) accepted for 42 ledger rows and four examples: [annual property TFU](bj-property-tfu.md) and [rental IRF/withholding](bj-rental-income-tax.md). TFU uses its own rights-holder, valuation, communal rate, exemption and payment rules. Rental IRF separates the landlord’s annual base from tenant/platform withholding. The June platform text is recorded, but its first operative withholding period remains held. No lease-registration duty or property-gain computation is claimed.

All seven domains remain partial. These additions have writer checks only; they do not inherit the independent review of the earlier eight Guides and do not constitute accountant attestation or a certified filing. Source/rule ledgers and the immutable preservation baseline are in `evidence/ledgers/benin-property-20261101/`.

## Individual business IBA addition, 1 November 2026

[Individual business IBA](bj-business-income-tax.md) adds a distinct partial job for an established IBA sole trader, independent professional or taxable transparent-entity member. Its individual-specific minimum, loss and cash-election rules are separate from salary ITS and company IS. Shared company filing/base methods and overview sanctions retain their existing owners. This new writer checkpoint awaits independent review and does not inherit the earlier property/rental or eight-Guide review.

The numerical TPS eligibility order, June exemption-transition timing, special incentive interactions, full cash-basis transition and authenticated IBA filing remain held. All seven domains remain partial. The preceding property/rental accepted review and all ten prior Guide bodies remain intact. The new rule ledger and immutable preservation identities are in `evidence/ledgers/benin-business-20261101/`.
