---
jurisdiction: FI
version: 1.2
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
partial:
  IT-IND: "Ordinary computation rebuilt; fresh whole-pack source review pending."
  IT-CORP: "Ordinary computation rebuilt; fresh whole-pack source review pending."
  VAT: "Ordinary computation and return routes rebuilt; fresh whole-pack source review pending."
  SC: "YEL and employee contributions covered together; fresh whole-pack source review pending."
  PR: "Ordinary withholding, benefits and insurance rebuilt; fresh whole-pack source review pending."
  TP: "Ordinary pricing/documentation method rebuilt; fresh whole-pack source review pending."
  XB: "Individual and corporate ordinary routes rebuilt; fresh whole-pack source review pending."
---

# Finland tax pack

Tax year **2026**, currency EUR, tax authority [Vero](https://www.vero.fi/en/). Michael / ChatGPT owns this pack under [OWNERS.md](../../../OWNERS.md). Work remains on [issue #392](https://github.com/openaccountants/openaccountants/issues/392) and the existing Finland [PR #777](https://github.com/openaccountants/openaccountants/pull/777). Historical consolidated PR #514 is not the current publication destination.

## Domains

All revised tax Guides are **sourced from the law**, pending fresh independent whole-pack review. None has professional attestation. Passing arithmetic or having a Guide does not establish complete coverage.

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

The 26 October pack contains twelve ordinary tax Guides, a router and the unchanged formation Guide. Each ordinary tax Guide has the nine-section standard and exactly two executable controls. Fresh independent review must re-read the primary sources, test scope and calculations, identify the exact file hashes and close findings. Until then the domain entries above remain partial and issue #392 stays open. Local commits save drafts; publication and merging remain separate gates. No new PR is required for this country.
