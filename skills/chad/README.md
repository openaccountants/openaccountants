---
jurisdiction: TD
applicable: [IT-IND, IT-CORP, VAT, SC, PR, TP, XB]
not_applicable: {}
covered_by:
  XB: td-import-exemption-eligibility
partial:
  IT-IND: "2026 labour scale, salary base, capital separation and residence expanded; full BIC/BNC, live payroll scale, annual individual filing date/forms and treaty/exit computations remain open."
  IT-CORP: "Existing 2025 Guide retained; current ordinary and special company computations not refreshed."
  VAT: "Existing 2025 Guide retained; 2026 domestic VAT and filing not refreshed."
  SC: "Existing 2025 payroll/social Guide retained; current CNPS rates, ceilings and procedures not verified."
  PR: "Existing 2025 payroll/social Guide retained; current withholding and employer obligations not refreshed."
  TP: "No transfer-pricing Guide; current domestic implementation, documentation and deadlines unverified."
  XB: "Only September 2026 non-wheat listed-goods import-eligibility draft; customs claim workflow, treaties, withholding and other cross-border jobs remain open."
---

# Chad: partial tax pack

The income Guide now has a source-ledger-backed 2026 expansion pending fresh independent review. Five other existing 2025 Guides remain unchanged. The new 2026 draft supports only the listed-goods import-exemption eligibility working paper under the signed 9 September order. It does not complete a customs claim or verify the wider pack. Independent source review accepted the narrow non-wheat job at `d91f12a172626fb9c4ee9ee69f860dd410856492`; local drafts only, no accountant attestation. All wheat is held pending reconciliation of finance-law article 65 with the September order.

## Domains

| Domain | Guide | Status/scope |
|---|---|---|
| IT-IND | [Income tax](td-income-tax.md) | 2026 salary/base/category expansion; review pending, domain partial |
| IT-CORP | [Corporate tax](td-corporate-income-tax.md) | Legacy 2025, not refreshed |
| VAT | [VAT](td-vat-gst.md) | Legacy 2025, not refreshed |
| SC and PR | [Payroll/social](td-payroll-social.md) | Legacy 2025, not refreshed |
| TP | Missing | Unverified |
| XB | [Import-exemption eligibility](td-import-exemption-eligibility.md) | Narrow non-wheat draft; independent source review accepted |

## Other retained work

[Formation](td-company-formation.md) and [overview](td-tax-overview.md) remain 2025 and unrefreshed. Complete old-topic preservation map: `evidence/ledgers/chad-old-topics.md`.

## Official source

[Signed Arrêté 135, 9 September 2026](https://ecofinances.gouv.td/wp-content/uploads/2026/09/Arrete-N135-Exoneration-des-droits-et-taxes-sur-les-produits09092026164852.pdf), both pages and all three articles read 2026-11-01. The general CGI could not be opened because of a certificate error; it was not read. The finance-law article 65 wheat provision and adjacent articles 64–66 were read on PDF page 78 and visually checked. Its interaction with the later order remains unresolved; wheat is excluded. This scoped reading is not a whole-law review or coverage claim. Full source captures stay outside Git.

Tracked by [TD pack issue #490](https://github.com/openaccountants/openaccountants/issues/490). Six domains remain partial and transfer pricing is missing. No generated inventory or bundle files edited.

## Independent review evidence

The initial source-conflict finding is preserved in `evidence/ledgers/chad-review-20261101/review.md`; additive closure is in `evidence/ledgers/chad-review-closure-1/closure.md`. Fourteen ledger rows, both examples, six unchanged legacy Guides and 82 preserved editorial topics were checked. After acceptance, only the stale review-status sentences in the Guide and ledger changed.

## Remaining-coverage continuation

Draft follow-on [#1219](https://github.com/openaccountants/openaccountants/pull/1219), pinned base `59c23acba2ad66dd2bb29ffc81ffbb9289769ef8`. Additive ledgers, exact predecessor destinations and historical identities live in `evidence/ledgers/chad-remaining-2026/`. The official CGI 2025 was recovered through a dated 2025-07-20 archive after direct TLS and browser failures; the relevant baseline provisions are reconciled with the enacted 2026 law. Prior import-eligibility acceptance does not cover these expansions.
