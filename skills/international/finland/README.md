---
jurisdiction: FI
version: 1.3
last_updated: 2026-10-26
applicable: [IT-IND, IT-CORP, VAT, SC, PR, TP, XB]
not_applicable: {}
covered_by:
  IT-IND: fi-income-tax
  IT-CORP: fi-corporate-income-tax
  XB: fi-individual-cross-border-residence
  PR: fi-employer-payroll
  VAT: finland-vat-return
  SC: fi-yel-social
  TP: fi-transfer-pricing
partial: {}
---

# Finland tax pack

Tax year **2026**, currency EUR, tax authority [Vero](https://www.vero.fi/en/). Michael / ChatGPT owns this pack under [OWNERS.md](../../../OWNERS.md). Work remains on [issue #392](https://github.com/openaccountants/openaccountants/issues/392) and the existing Finland [PR #777](https://github.com/openaccountants/openaccountants/pull/777). Historical consolidated PR #514 is not the current publication destination.

## Domains

The twelve ordinary tax Guides passed independent source review on 26 October 2026 after the recorded corrections. No unresolved ordinary content error was identified within the scope below. This is the bounded ordinary-tax milestone; none has professional attestation. Passing arithmetic or having a Guide does not establish comprehensive country coverage.

| Domain | Ordinary computation / procedure |
|---|---|
| IT-IND | [Income tax](fi-income-tax.md): wages, pensions, investment, rent/gains, sole-trade allocation, deductions/credits, mainland and Åland components; [prepayments](fi-prepayments.md) |
| IT-CORP | [Corporate income tax](fi-corporate-income-tax.md): book-to-tax base, depreciation, dividends/gains, interest, groups, losses and broadcasting tax |
| VAT | [VAT return](finland-vat-return.md): taxable base, rates, exemptions, input deduction, EU/import routes, Åland, construction reverse charge and property adjustments |
| SC / PR | [YEL](fi-yel-social.md) and [payroll](fi-employer-payroll.md): entrepreneur/employee eligibility, insurance bases, health contributions, benefits, withholding and reporting |
| TP | [Transfer pricing](fi-transfer-pricing.md): ordinary method execution, documentation and requests; [CbCR](fi-country-by-country-reporting.md): role, country rows, notification and filing |
| XB | [Individual residence/income/relief](fi-individual-cross-border-residence.md); [corporate residence/PE/withholding/credit/exit](fi-corporate-cross-border-tax.md) |
| Property | [Transfer tax](fi-property-transfer-tax.md) and [annual real-estate tax](fi-annual-real-estate-tax.md); rent/gains in income-tax Guides |

Formation and accounting are a separate milestone. The existing [company-formation Guide](fi-company-formation.md) is preserved unchanged by the 26 October tax rebuild; this batch makes no accounting-pack completion claim.

## Scope boundaries

Ordinary taxpayers and calculations above are the current tax milestone. Country-specific treaty rates/MLI outcomes, actual municipal valuation inputs, benchmark studies and taxpayer elections require case evidence. Those inputs are not invented national constants. Specialist agriculture/forestry/MYEL benefits, estate/gift taxes, fund/hybrid/CFC/minimum-tax/reorganisation cases, special VAT margin/travel/group/marketplace schemes, power plants and unusual professional/service regimes are not completed by this ordinary pack. They require separately scoped Guides; the worldwide goal is broader than this bounded ordinary-tax milestone.

Confirmed future parameters are separated from current law. The October 2026 income-tax amendments with whole-2026 effect are identified in the individual Guide. 2027 interest rates and the exact December 2026 additional-prepayment opening day are not asserted. Annual property tax uses **2025 values**; future 2027 wording in consolidated statutes is not silently applied to 2026.

## Evidence and next action

The earlier [23 October independent review](../../../docs/research/2026-10-23-finland-pack-review.md), [source reachability record](../../../docs/research/2026-10-23-finland-source-reachability.json) and [direct statutory retrieval](../../../docs/research/2026-10-23-finland-direct-statute-retrieval.json) are preserved as historical evidence. They do **not** approve the rebuilt 26 October blobs. HTTP availability is not legal verification.

The 26 October pack contains twelve ordinary tax Guides, a router and the unchanged formation Guide. Each ordinary tax Guide has the nine-section standard and exactly two executable controls. A fresh reviewer independently re-read the sources, closed the findings after corrections, checked the file hashes and recomputed all 26 examples, including the unchanged formation examples, with 113 matching results. The reviewed source commit is `255ab46c83b1b65d6f6a982f04121372a3be9e6a`; this README-only closure changes no reviewed tax Guide. The local review record comprises `independent-review.md` and `reviewed-hashes.json`, prepared for the existing PR's review comment. Those records have not yet been published to the PR.

The review records a direct EUR-Lex consolidated Directive/Annex access limit; domestic implementation and official Vero guidance support the ordinary conditions stated. It does not claim a direct reading of that Annex by the reviewer. Specialist coverage and taxpayer-specific evidence remain outside the completed ordinary milestone.

Local source review is complete. Publication still requires the finished country batch on PR #777, its review comment with figures checked, source-backed fixes, evidence limits and exact hashes, and the required checks and reviews on the pushed head. This local record is not the public PR review comment and does not authorise a merge. Issue #392 stays open pending assessment against its full milestone; formation/accounting and wider specialist coverage are not established here. No new PR is required for this country.
