---
jurisdiction: MD
version: "2.22"
last_updated: 2026-10-31
applicable: [IT-IND, IT-CORP, VAT, SC, PR, TP, XB]
not_applicable: {}
covered_by:
  IT-IND: moldova-income-tax
  IT-CORP: md-corporate-income-tax
  VAT: moldova-vat
  SC: moldova-social-contributions
  PR: moldova-payroll
  TP: md-transfer-pricing
  XB: md-cross-border
partial:
  IT-IND: "Business deductions, return contradictions, dependent relief and special-regime procedures remain incomplete."
  IT-CORP: "Foreign-credit and donation variants, assets, deferred distributions and sector/entity procedures remain incomplete."
  VAT: "Refunds, non-exact pro-rata rounding, currency conversion, e-services and specialist procedures remain incomplete."
  SC: "CNAM correction entitlement, farm/special categories, status and agreement procedures remain incomplete."
  PR: "Ambiguous return fields, foreign-currency loans, benefits, leave and special categories remain incomplete."
  TP: "IUPT ambiguities, retention, APA payment/refund, corresponding adjustments and specialist routes remain incomplete."
  XB: "Treaty applications, additional PE forms, refunds, departure and credit procedures remain incomplete."
---

# Moldova tax pack

This is a 2026 source-cited draft pack. Ten predecessor Guides received a [bounded independent source review](../../evidence/ledgers/md-country-evidence/independent-review/FINAL-REVIEW.md) covering 3,913 ledger claims, 50 arithmetic blocks, 58 standalone cases and 80 sampled predecessor topics. [The decision](../../evidence/ledgers/md-country-evidence/independent-review/FINAL-DECISION.json) confirms that all seven tax domains remain partial. No accountant has attested to the pack. Completion remains tracked in [issue #411](https://github.com/openaccountants/openaccountants/issues/411); the consolidated batch is [PR #1057](https://github.com/openaccountants/openaccountants/pull/1057). Ownership is recorded in [docs/OWNERS.md](../../docs/OWNERS.md).

## Domains

| Domain | Guide | Quality |
|---|---|---|
| IT-IND, individual income tax | [moldova-income-tax](moldova-income-tax.md) | sourced from the law; partial |
| IT-CORP, corporate income tax | [md-corporate-income-tax](md-corporate-income-tax.md) | sourced from the law; partial |
| VAT | [VAT12](moldova-vat.md), [refund application](md-vat-refund.md) | sourced from the law; partial |
| SC, social and medical contributions | [moldova-social-contributions](moldova-social-contributions.md) | sourced from the law; partial |
| PR, payroll withholding | [moldova-payroll](moldova-payroll.md) | sourced from the law; partial |
| TP, transfer pricing | [md-transfer-pricing](md-transfer-pricing.md) | sourced from the law; partial |
| XB, cross-border | [md-cross-border](md-cross-border.md) | sourced from the law; partial |

Supporting Guides cover [company formation](md-company-formation.md), [tax-system and reporting orientation](md-tax-overview.md), and [tax planning and the IT-park interface](moldova-tax-optimization.md). They do not replace a missing operative tax method. Each Guide states its remaining source and procedure questions under Sources. The [reviewed gap classification](../../evidence/ledgers/md-country-evidence/independent-review/final-gap-classification.json) is the detailed completion checklist. Property, local and other taxes require a specific applicability and job-level coverage audit before the country can be declared complete.

The new VAT refund application Guide has a separate [184-row source ledger](../../evidence/ledgers/md-vat-refund.md) and requires an independent delta review. Its existence does not clear the remaining VAT gaps.

## Official sources and evidence

- [Fiscal Code No. 1163/1997, operative consolidation of 30 October 2026](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro): selected operative provisions read 30–31 October 2026; individual source scope and dates are recorded in the Guide ledgers.
- [SFS transfer-pricing page](https://www.sfs.md/ro/pagina/preturi-de-transfer): used with the enacted Code, Ministry orders and approved forms cited in the TP Guide, read 30–31 October 2026.
- [Source records and predecessor reconciliations](../../evidence/ledgers/md-country-evidence/): original material, official attachments, exact quotations, calculation controls and independent findings are preserved. Earlier writer status notes are historical, including the [previous README](../../evidence/ledgers/md-country-evidence/layout-20261031/README-before-map-repair.md).
