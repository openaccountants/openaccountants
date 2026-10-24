---
name: sm-tax-overview
description: >
  Route 2026 San Marino tax questions to the relevant source Guide and country gap register. Use for corporate and personal IGR, monofase import tax, payroll/social contributions, related-party dealings, international agreements, nonresident income, selected foreign credit and formation intake. Establish the actual person, entity, transaction, period and current Guide status before choosing a method. The country batch preserves six older entry paths and adds TP/XB. This router replaces the prior approximate rate/deadline summary; it supplies no independent liability formula or treaty/filing entitlement. The linked methods identify dated source baselines and current amendments, with specialist and operational gaps retained. All domains remain partial. The dated pack record identifies independent source-review scope and limits; named local accountant review remains open.
jurisdiction: SM
tax_year: 2026
last_updated: 2026-10-24
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
category: international
version: 0.4
sources:
  - url: "https://www.consigliograndeegenerale.sm/on-line/documento17086436.html"
    title: "Official coordinated IGR archive; dated source router"
    as_of: "2026-10-24"
  - url: "https://www.consigliograndeegenerale.sm/on-line/home/archivio-leggi-decreti-e-regolamenti/documento17155359.html"
    title: "Law 141/2025; reform source router"
    as_of: "2026-10-24"
  - url: "https://www.bollettinoufficiale.sm/on-line/RicercaBU?operation=getDocBU&id=9c3a0dfeb72a7aeab52d1c5c0440879b4cf2ad33"
    title: "DD 156/2026; current-amendment router"
    as_of: "2026-10-24"
---

# San Marino tax overview and routing v0.4

## Establish person, transaction and year

Use the [country register](README.md) for each Guide's scope and remaining gaps. All eight source Guides are source-cited drafts, using selected primary-source methods and express amendment/implementation limits; formation retains its November 2024 coordinated baseline and later-amendment gap. Original bodies remain in Git history. All source Guides remain tier 2; publication and CI evidence are tracked on the country issue and consolidated PR.

| Question | Start with |
|---|---|
| Resident individual income, wage/pension or business base and SMaC credits | [Individual IGR](sm-income-tax.md) |
| Corporate base, losses, ordinary rate, conditional new-activity relief and advances | [Corporate IGR](sm-corporate-income-tax.md) |
| Import tax, goods classification and Italian invoice interface | [Monofase/indirect tax](sm-vat-gst.md) |
| Employee withholding and social/pension/FONDISS coverage | [Payroll/social](sm-payroll-social.md) |
| Related-party normal value, adjustments and international advance agreements | [Transfer pricing](sm-transfer-pricing.md) |
| Residence/source/PE, nonresident receipts and selected corporate foreign credit | [Cross-border](sm-cross-border.md) |
| Entity capital, governance, registration and annual compliance | [Formation](sm-company-formation.md), with its dated company-law and later-amendment limits |

## Sources

The [official IGR coordinated archive](https://www.consigliograndeegenerale.sm/on-line/documento17086436.html) has separate dated 2025 editions. Read its relevant provisions with [Law 141/2025](https://www.consigliograndeegenerale.sm/on-line/home/archivio-leggi-decreti-e-regolamenti/documento17155359.html) and authentic [DD 156/2026](https://www.bollettinoufficiale.sm/on-line/RicercaBU?operation=getDocBU&id=9c3a0dfeb72a7aeab52d1c5c0440879b4cf2ad33). Current methods identify provisions read and their limits; no full amendment chain, municipality/special-case outcome or live portal acceptance is inferred from a source URL.

The working branch `codex/san-marino-country-completion` is tracked on [issue #426](https://github.com/openaccountants/openaccountants/issues/426) and uses consolidated draft [PR #514](https://github.com/openaccountants/openaccountants/pull/514). The [dated source-review record](../../../docs/research/2026-10-24-san-marino-pack-review.md) identifies the exact country revision, findings and scope. The country is published as one combined content batch after review corrections, with published-head CI tracked separately. Preserve all seven partial flags and the separate named local accountant gate.

This router supplies no standalone rates or calculation blocks. Use the exact tax-year/source/status of the selected method and the actual case evidence before computing or filing.

## Source-review status

See the [independent source-review record](../../../docs/research/2026-10-24-san-marino-pack-review.md) for its exact revision, scope and findings. Named San Marino accountant review remains open. This record is separate from comprehensive coverage, named professional approval and live filing.

<!-- openaccountants-cta-block -->

---

## Talk to an accountant

Find the current Guide and professional-review status at [OpenAccountants](https://www.openaccountants.com).
