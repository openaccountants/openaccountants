---
name: ly-transfer-pricing
description: >
  Research connected-enterprise pricing for Libya, including the actual associated-enterprises rule in the in-force UK Libya convention, branch profit attribution, head-office charges and domestic market-value disposal rules. Separates supported adjustment analysis from unverified documentation thresholds, methods and filing obligations. It distinguishes the source text actually read from unresolved later amendments, records the inputs that change the result, and supplies two recomputing working papers. Use it when researching Libyan tax in 2026, preparing an adviser brief, checking an earlier answer, or identifying which return and supporting records are needed. It is a partial research reference, subject to the currentness limits in the body, and it does not represent a local accountant's sign-off or a tested electronic submission.
jurisdiction: LY
category: transfer-pricing
tax_year: 2026
tax_year_notes: "2026 research edition; domestic amendment chain not closed"
tier: 2
last_updated: 2026-11-01
version: 1.0
---

# Libya Transfer Pricing and Connected Transactions v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

**2026 research edition, incomplete currentness check.** The domestic rules below are transcribed from the Tax Authority's official 2016 compilation. Its live legislation catalogue and history still identify Income Tax Law 7/2010 and Regulation 592/2010. That establishes the source text, not a complete amendment chain through 2026. Use the calculations as statutory research working papers; obtain the applicable later instruments and current filing instructions before acting. This pack remains partial and has no accountant attestation.

## Who this applies to

Related enterprises, branches and advisers reviewing Libyan connected transactions. The UK-Libya convention provides a genuine associated-enterprises rule in art. 10. Apply it only to enterprises in the treaty relationship and only after treaty residence and scope are established. It is not proof of a comprehensive domestic transfer-pricing documentation regime.

Domestic Law 7/2010 arts. 28, 45 and 66-69 also address avoidance, market-value disposals and foreign branches. These operate on their own statutory conditions. No ownership percentage, safe harbour or documentation exemption is invented.

## Rates, bands and thresholds

| Rule and condition | Operative test | Source | Official URL |
|---|---|---|---|
| UK-Libya connected enterprises | Direct/indirect participation in management, control or capital; imposed conditions differ from independent enterprises | UK-Libya convention art. 10(1) | https://assets.publishing.service.gov.uk/media/5a819e9ded915d74e33ff2ef/uk-libya-dtc_-_in_force.pdf |
| UK-Libya corresponding adjustment | Other state makes an appropriate tax adjustment where the inclusion meets the independent-enterprise condition; authorities consult if necessary | Convention art. 10(2) | https://assets.publishing.service.gov.uk/media/5a819e9ded915d74e33ff2ef/uk-libya-dtc_-_in_force.pdf |
| UK-Libya branch profit attribution | Distinct and separate enterprise under same/similar activities and conditions, dealing independently | Convention art. 8(2)-(5) | https://assets.publishing.service.gov.uk/media/5a819e9ded915d74e33ff2ef/uk-libya-dtc_-_in_force.pdf |
| Domestic business-asset disposal below market | Substitute market value in computing gain | Law 7/2010 arts. 45, 71 | https://tax.gov.ly/assets/m2016.pdf |
| Domestic branch head-office charges | Necessity and ceiling owned by ly-corporate-income-tax, art. 66 | Law 7/2010 art. 66 | https://tax.gov.ly/assets/m2016.pdf |
| Domestic documentation, CbCR, master/local file thresholds or APA process | unverified; absence and exemption cannot be asserted | No operative instrument establishing these read | https://tax.gov.ly/Law1.aspx |

## The base

Build a transaction schedule showing counterparties, residence, connection, dates, contracts, goods/services/rights, amount, currency and allocation. Document the actual functions performed, assets used, risks and reliable independent dealings. Those records are evidence for the treaty's independent-enterprise test; this Guide does not label them a prescribed Libyan local-file format.

For art. 10, identify the profits that would have accrued without the non-independent conditions and reconcile the proposed inclusion to the accounts and the Libyan company's tax computation. Related ownership alone does not prove that the price is wrong. A supported price difference requires analysis of comparability, not a selected percentage of turnover. A corresponding adjustment in the other state is not an automatic cash refund or a deduction copied into the Libyan return.

For a branch, distinguish the treaty art. 8 separate-enterprise attribution and actual business expenses from the domestic art. 66 head-office restriction. A supported treaty deduction can raise a treaty-versus-domestic issue; do not mechanically apply the domestic cap before checking the convention. Route it for professional resolution. Non-treaty branch calculations use the statutory provisions in the corporate Guide.

A domestic sale of a business asset below market uses art. 45 market value and depreciated cost. Legal-form change and mergers have separate art. 45/art. 69 rules. General anti-avoidance in art. 28 and Reg. art. 73 needs the stated facts and evidence; it is not authority to disregard every connected-party contract.

## Deadlines and filing

1. Reconcile the connected-transaction schedule and adjustment to Form 9 and its supporting accounts using the corporate return workflow in [Corporate income tax](ly-corporate-income-tax.md). Retain contracts, independent-price evidence, allocation workings, approvals and correspondence.
2. Preserve the relevant residence certificate and treaty text for the period before using arts. 8 or 10. HMRC's live Libya treaty page identifies the 2008 convention as in force: https://www.gov.uk/government/publications/libya-tax-treaties .
3. If the adjustment taxes the same profit twice, request competent-authority consideration under convention arts. 10(2) and 26. Article 26 permits presentation to the resident state's competent authority, with its stated nationality exception. This read convention does not prescribe a three-year MAP filing period; do not import one from a model treaty. Domestic objection deadlines continue to require attention.
4. Current prescribed transfer-pricing forms, documentation filing deadlines and an APA route have not been established. No separate return is created or certified by this Guide.

## Penalties and interest

No distinct transfer-pricing penalty was verified. Ordinary income-tax underpayment, records, withholding and deliberate-evasion provisions remain relevant to the actual conduct, as linked in the corporate Guide. A defensible price disagreement is not automatically deliberate evasion. Preserve the assessment notification and consider domestic objection and treaty procedure independently.

## Cross-border points

UK-Libya treaty art. 10 is corridor-specific. Do not extend it to every treaty partner from the authority's treaty index. Interest and royalties have their own special-relationship provisions in arts. 12(4) and 13(4): residence-only treatment applies only to the independent amount, with excess left to domestic law subject to the rest of the treaty. See [Cross-border](ly-cross-border-tax.md) for residence, source and relief routing.

## Two worked examples that recompute

**Supported connected-sale adjustment.** Assume treaty eligibility and independent-price evidence are established, and the tax authority properly includes LYD 20,000 extra profit from a connected sale. Book profit is LYD 80,000 and adjusted profit LYD 100,000. Using the ordinary corporate rate from the corporate Guide as an input, additional Libyan tax is LYD 4,000. An appropriate other-state adjustment must be considered separately.

```oa-check
name: Treaty adjustment after independent-price evidence
inputs:
  book_profit: 80000
  supported_adjustment: 20000
  ordinary_corporate_rate: 0.2
steps:
  - adjusted_profit: book_profit + supported_adjustment
  - tax_before: book_profit * ordinary_corporate_rate
  - tax_after: adjusted_profit * ordinary_corporate_rate
  - additional_tax: tax_after - tax_before
expected:
  adjusted_profit: 100000
  additional_tax: 4000
```

**Market-value disposal decision.** A business asset cost LYD 100,000 with LYD 40,000 accepted tax depreciation. Sale price is LYD 70,000 but supported market value is LYD 90,000. The depreciated basis is LYD 60,000. Using the contract alone reports LYD 10,000 gain; art. 45 requires LYD 30,000. The difference is LYD 20,000 before the applicable taxpayer-specific tax computation.

```oa-check
name: Below-market business disposal comparison
inputs:
  original_cost: 100000
  tax_depreciation: 40000
  contract_price: 70000
  market_value: 90000
steps:
  - basis: original_cost - tax_depreciation
  - contract_gain: contract_price - basis
  - statutory_gain: max(contract_price, market_value) - basis
  - adjustment: statutory_gain - contract_gain
expected:
  basis: 60000
  contract_gain: 10000
  statutory_gain: 30000
  adjustment: 20000
```

## Ask the client first

- Which entities, residence evidence, ownership/control links and treaty corridor are involved?
- What contracts, actual functions, independent comparables and price adjustments are supported?
- Is this a branch charge, goods/service transaction, financing, royalty, asset sale or restructuring?
- Which taxpayer, accounting year and existing assessment or objection deadline applies?
- Has the other state taxed the same profit, and what correspondence proves that?

## Sources

| Source and actual read scope | URL | Read on |
|---|---|---|
| Tax Authority, 2016 tax legislation compilation: Law 7/2010 arts. 28, 45, 66-71; Reg. art. 73; PDF pp. 18, 23, 28-29 and 58; original Arabic, local OCR checked against selected page images | https://tax.gov.ly/assets/m2016.pdf | 2026-11-01 |
| Tax Authority live law and regulation catalogues; law titles and the income-law history paragraph, not a consolidated 2026 certificate | https://tax.gov.ly/Law1.aspx ; https://tax.gov.ly/Law2.aspx ; https://tax.gov.ly/TaxHistory.aspx | 2026-11-01 |
| UK-Libya convention, English original: arts. 1-5, 8, 10, 12-13, 26; actual treaty PDF pp. 4-12, 15, 17, 20-21, 36; live in-force status page also read | https://assets.publishing.service.gov.uk/media/5a819e9ded915d74e33ff2ef/uk-libya-dtc_-_in_force.pdf ; https://www.gov.uk/government/publications/libya-tax-treaties | 2026-11-01 |
Not yet confirmed: complete domestic amendment chain and administrative practice through 2026; complete domestic and 2026 amendment chain; domestic arm's-length documentation legislation, thresholds, master/local file, CbCR, prescribed methods, APA process, penalty regime and filing forms. No absence or exemption is claimed.
