---
jurisdiction: MC
applicable: [IT-IND, IT-CORP, VAT, SC, PR, TP, XB]
not_applicable: {}
covered_by:
  IT-IND: mc-income-tax
  IT-CORP: mc-corporate-income-tax
  VAT: monaco-vat
  SC: mc-payroll-social
  PR: mc-payroll-social
  TP: mc-transfer-pricing
  XB: mc-cross-border
---

# Monaco tax pack

2026 source-cited drafts checked 25 October 2026. The seven applicable tax domains are covered for ordinary taxpayers and computations on the stated facts. Payroll and social contributions share one Guide. All eight Guides remain tier 2: no named Monaco professional has signed off. Source coverage, independent AI review and arithmetic validation are distinct from professional attestation and from a maintainer merging this PR.

| Domain | Guide | Ordinary coverage |
|---|---|---|
| IT-IND | [Individual tax](mc-income-tax.md) | Genuine residence, full French-exception screen, certificates, foreign filing destination and sanctions; French calculations route to the France Guide |
| IT-CORP | [Business profits tax](mc-corporate-income-tax.md) | Scope, base, deductions, executive scale, dated shareholder interest, losses/carryback, participation, disposals, cessation, advances and DSF filing |
| VAT | [VAT](monaco-vat.md) | Rates/franchise, tax points, input coefficients/capital adjustments, refunds, imports/EU trade, DSF onboarding/returns and invoicing |
| SC, PR | [Payroll/social](mc-payroll-social.md) | January to September and October to December 2026 rates, bases/caps/rounding, directors, domestic and self-employed schemes, hiring/payslips, France collection and bilateral affiliation |
| TP | [Transfer pricing](mc-transfer-pricing.md) | Normal foreign conditions, evidence, related deduction tests, disclosures/retention, CbCR population/notification/EAI filing and sanctions |
| XB | [Cross-border](mc-cross-border.md) | Residence/source/PE decisions, foreign credits and participation, cessation, employment/social routing, CRS account-holder classification and CbCR routing |

[Overview](mc-tax-overview.md) is the entry point. [Formation](mc-company-formation.md) preserves the existing Accounting packs topic with current capital/permission corrections; its exhaustive registry, beneficial-owner, accounts/audit and October-reform implementation remain partial. Formation is not one of the seven tax domains and does not add a completed domain.

Niche regimes remain outside this ordinary pack: banking/insurance and specialised tax credits; special VAT margin/travel/online schemes and development property; sector-specific flat social bases and derogatory CMRC contracts; formal advance/corresponding pricing agreements; a worldwide treaty-rate/refund atlas; financial-institution industry implementation; and multinational minimum-tax computations. The Guides identify those boundaries without asserting that a tax, treaty, reporting duty or relief is absent. These boundaries follow the repository’s distinction between an ordinary missing taxpayer/computation and a specialist regime.

The statute uses **at least 25%** foreign turnover, despite the government summary’s stricter wording. The payroll Guide gives the January to September 2026 rates and caps from the official October 2025 CSM circulars and the October 2026 rates and caps from the current ones. It covers the June minimum-wage change. Earlier CSM letters were recovered from dated archive captures after the live download IDs were replaced with October 2026 documents; the receipts identify each original URL and capture. Domestic-staff relief includes exactly **254 hours** under the native law, despite the authority summary’s “below” wording. The shareholder-interest reference is derived through the Banque de France decision and ECB effective-date history, with later dates requiring rechecking. Project 1.129 is not enacted-law evidence. Every Guide links the operative provisions.

The six inherited Guide paths, categories, attribution fields and platform footers are preserved; the two added tax slugs are retained. The prior [research](../../../docs/research/2026-10-24-monaco-research.md), [receipts](../../../docs/research/2026-10-24-monaco-sources.json) and [partial-scope review](../../../docs/research/2026-10-24-monaco-pack-review.md) remain unchanged as history. They do not review the expanded pack. The current [research and source-reading record](../../research/monaco-2026/completion-research.md), [retrieval receipts](../../research/monaco-2026/retrievals.json) and [fresh independent whole-pack review](../../research/monaco-2026/independent-review.md) record this continuation. Each computational Guide has exactly two recomputing examples, fourteen across the pack; additional boundary controls live with the research.

Country issue: [#410](https://github.com/openaccountants/openaccountants/issues/410). A maintainer merge and named professional review remain separate gates. Do not infer a merged/closed issue, live ingestion or a filed taxpayer return from these source documents.
