---
name: mg-transfer-pricing
description: "Madagascar 2026 related-party arm length review, disclosure, full-documentation threshold and adjustment working papers; partial implementation scope."
jurisdiction: MG
category: transfer-pricing
tax_year: 2026
tier: 2
last_updated: 2026-11-01
version: 1.1
---

# Madagascar transfer pricing: annual disclosure and documentation scope v1.1

> **General reference only.** This Guide is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person’s facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in Madagascar.

## Who this applies to

Apply arm’s-length pricing to financial/commercial goods, intangible and service transactions with associated enterprises abroad, profit attributable to a non-resident’s Madagascar PE and domestic transactions (CDI 01.01.13 IV 1°–3°). Dependency includes majority capital, actual decision-making power or common control (9°). The correction/documentation provisions extend to transactions with a foreign privileged-tax enterprise even without association (7°); the privileged-tax test is no income/profit tax or an amount at most half the ordinary Madagascar tax under equivalent facts (8°). A treaty can use its own associated-enterprise definition. [CDI](https://www.impots.mg/explorer?path=/legislation/Codes%20et%20Manuels/CDI-LFI%202026.pdf).

## Rates, bands and thresholds

| Obligation / conditions | 2026 test | Official source |
|---|---|---|
| Full TP documentary obligation, in addition to the declaration | Intragroup transactions at least MGA 450,000,000 **and** one size test below | [CPF IV-08](https://www.impots.mg/explorer?path=/legislation/Codes%20et%20Manuels/CPF-LFI%202026.pdf) |
| Own-enterprise size alternative | Annual VAT-exclusive turnover at least MGA 40,000,000,000 or equivalent total assets | same |
| Group-linked alternative | Holds or is held by a subsidiary meeting group turnover/assets at least MGA 240,000,000,000; obtain exact ownership chain before applying | same |
| Annual TP disclosure | LFI: before 30 June. July LFR changes this to by 30 June; previous calendar year, regardless of close | [LFR amendment to CPF IV-10](https://www.mef.gov.mg/assets/vendor/ckeditor/plugins/kcfinder/upload/files/2026/lfr/LFR2026%20Ampliation%20SIGNEE%20DATEE.pdf); [CPF IV-09–10](https://www.impots.mg/explorer?path=/legislation/Codes%20et%20Manuels/CPF-LFI%202026.pdf) |
| Full documentation | 90 days from disclosure deadline | [CPF IV-08; V-24](https://www.impots.mg/explorer?path=/legislation/Codes%20et%20Manuels/CPF-LFI%202026.pdf) |

For the annual disclosure that fell due in June 2026, the LFI wording applied before the July amending law. The amended “by 30 June” rule governs later deadlines, including the 2026-transaction declaration in 2027. The full-documentation size thresholds do not turn off arm’s-length pricing or the annual disclosure obligation for enterprises described by CDI 01.01.13 IV 5°.

## The base

Build the related-party transaction register from contracts, invoices, accounts and ownership/control facts. Document functions, assets and risks, select the supported arm’s-length price from comparables, and preserve information available at the transaction date. A taxpayer whose controlled terms depart from arm’s length includes the relevant difference in taxable profit when declaring income; it bears the proof burden for its own correction (CDI 01.01.13 IV 1°,4°). The administration can adjust after comparability analysis and bears its statutory proof burden in that assessment (6°). No safe margin, documentation-price tolerance or automatic downward deduction is established here. Pass an established adjustment to the IR reconciliation in [corporate income tax](mg-corporate-income-tax.md). [CDI](https://www.impots.mg/explorer?path=/legislation/Codes%20et%20Manuels/CDI-LFI%202026.pdf).

## Deadlines and filing

Prepare the capital organization chart and transaction-category details, counterparties and relationships for the dedicated electronic platform under CPF IV-09–10. Download current models from that platform, complete, submit **and validate** the disclosure by the operative statutory date, preserving acknowledgement and the submitted files. Enterprises meeting IV-08 also lodge the remaining documentary annexes on the same platform within the additional period under V-24. CDI 01.01.13 IV 5° requires Malagasy or French documentation. An audit request for complements has a one-month response period, extendable on a reasoned request to at most two months total; an insufficient response can lead to a notice requiring completion within fifteen days (CPF V-25,28). [CPF](https://www.impots.mg/explorer?path=/legislation/Codes%20et%20Manuels/CPF-LFI%202026.pdf); [CDI](https://www.impots.mg/explorer?path=/legislation/Codes%20et%20Manuels/CDI-LFI%202026.pdf). Actual annex numbers, portal URL and accepted file format remain unverified.

## Penalties and interest

CDI 20.01.52 provides MGA 10,000,000 for breaches of the TP obligation, including missing elements preventing arm’s-length evaluation and late documentary submission. For refusal to produce complementary annexes under CPF V-24 after an unsuccessful reminder, CDI 20.01.56.8 2° adds a fine of 5% of the transaction concerned, alongside the 20.01.52 sanction and without prejudice to ex-officio adjustment under CPF V-34 onwards. The same consequences apply to an insufficient response or no response to the V-28 completion notice. The sanctions cumulate when the taxpayer both failed to lodge TP documents within the legal deadline and failed to respond, refused production or responded insufficiently to the complementary-document request. These triggers must be established from the actual requests, notices and responses. [CDI 20.01.56.8 2°](https://www.impots.mg/explorer?path=/legislation/Codes%20et%20Manuels/CDI-LFI%202026.pdf). This does not replace other applicable understatement/payment sanctions. Refer contested comparability or sanctions for Malagasy professional review. [CDI](https://www.impots.mg/explorer?path=/legislation/Codes%20et%20Manuels/CDI-LFI%202026.pdf).

## Cross-border points

Test foreign and domestic parties, a PE’s allocation and privileged-tax counterparties separately. Treaties can change the associated-enterprise definition and provide a remedy for double taxation; do not promise a corresponding adjustment or treaty outcome without the operative text. No separate country-by-country reporting obligation or threshold has been established in this scope.

## Two worked examples that recompute

Hypothetical prices are independently supported inputs, not asserted safe harbours. The first is an underpriced controlled sale; the second is an excessive related-party service charge. Both increase the preliminary tax base under CDI 01.01.13 IV 4°. They do not calculate final IR/minimum tax.

```oa-check
name: Underpriced controlled sale
inputs:
  units: 10000
  charged_price: 12000
  supported_price: 15000
  preliminary_profit: 100000000
steps:
  - adjustment: units * (supported_price - charged_price)
  - adjusted_profit: preliminary_profit + adjustment
expected:
  adjustment: 30000000
  adjusted_profit: 130000000
```

```oa-check
name: Excessive service charge
inputs:
  booked_charge: 90000000
  supported_charge: 65000000
  preliminary_profit: 20000000
steps:
  - adjustment: booked_charge - supported_charge
  - adjusted_profit: preliminary_profit + adjustment
expected:
  adjustment: 25000000
  adjusted_profit: 45000000
```

## Ask the client first

Get full ownership/control chain, country/tax status of each counterparty, individual and group turnover/assets, annual controlled transaction totals, domestic/foreign/PE classification, contracts, pricing documentation, comparable evidence, prior disclosures and audits, and the live platform models.

## Sources

 | Source and provisions actually read | Read on |
|---|---|
| [DGI 2026 CDI](https://www.impots.mg/explorer?path=/legislation/Codes%20et%20Manuels/CDI-LFI%202026.pdf), 01.01.13 IV in full; 20.01.52; 20.01.56.8 2° | 2026-11-01 |
| [DGI 2026 CPF](https://www.impots.mg/explorer?path=/legislation/Codes%20et%20Manuels/CPF-LFI%202026.pdf), IV-08–10; V-19–28 | 2026-11-01 |

| [Signed Loi 2026-004, LFR 2026](https://www.mef.gov.mg/assets/vendor/ckeditor/plugins/kcfinder/upload/files/2026/lfr/LFR2026%20Ampliation%20SIGNEE%20DATEE.pdf), tax amendments and article 22 entry provision read | 2026-11-01 |

**Not yet confirmed:** Exact radio/posted publication date activating the July LFR under article 22; do not resolve a transaction at that transition without the publication evidence. current implementing decision and annex identifiers, dedicated platform URL/fields, accepted pricing-method detail, the exact group-ownership threshold interpretation in IV-08, country-by-country reporting and treaty-specific corresponding adjustments. Do not use this Guide as a full documentary filing template.

