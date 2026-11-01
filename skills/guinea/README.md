---
jurisdiction: GN
applicable: [IT-IND, IT-CORP, VAT, SC, PR, TP, XB]
not_applicable: {}
covered_by:
  VAT: [gn-vat-gst, gn-vat-invoice-control]
partial:
  IT-IND: "Legacy 2025 Guide unchanged; all bands, bases, residence and filing require current enacted-law research."
  IT-CORP: "Legacy 2025 Guide unchanged; ordinary/mining rates, minimum tax, base, withholding and deadlines unresolved for 2026."
  VAT: "New 2026 invoice-field control only; legacy rate/threshold/return and cross-border claims are not confirmed current law."
  SC: "2026 ordinary full-month CNSS base/contribution method added; deadline conflict, parameter instruments, special categories, partial months and multi-employer cap allocation remain unresolved."
  PR: "Current salary-tax withholding, employer salary/apprenticeship taxes and tax remittance remain unresolved; CNSS is computed separately."
  TP: "No current transfer-pricing job; operative pricing and documentation provisions unavailable in this bounded research."
  XB: "No current cross-border job; residence, non-resident withholding, treaties and relief remain unverified."
---

# Guinea: two conditional March-text workpapers, country pack partial

Two new tier-2 workpapers read from enacted Law L/2026/010/CNT and its signed promulgation decree on 1 November 2026. Independent source review accepted candidate `8f84f15a2a89e62158c959d05d150dd9deb3090a` only as conditional March-text workpapers. This does not establish operative current-year law: users must confirm the version governing the actual period or invoice, including the October rectification effect, before live use. If unresolved, outputs remain hypothetical March-text analysis. No accountant attestation. Four historical 2025 tax Guides remain unchanged; payroll/social and formation are expanded below with independent review pending. Keep [issue 461](https://github.com/openaccountants/openaccountants/issues/461) open.

| Job | Guide | Actual scope |
|---|---|---|
| CFU property-rate workpaper | [Property tax](gn-property-tax.md) | Replaced CGI265 rate/base pairs only; liability, valuation, exemptions and filing unresolved |
| VAT invoice control | [Invoice control](gn-vat-invoice-control.md) | Replaced CGI383 VI fields and arithmetic control only; underlying VAT treatment and filing unresolved |

The source contains promulgation decree D/2026/0103/PRG/SGG signed 31 March 2026. The period before the replacements and the final promulgated status/effect of the October 2026 rectifying bill have not been established. Parliamentary adoption/news and a project document do not substitute for enacted amendments.

The Ministry's CGI library returned 403 through direct fetch and an ordinary Brave visit. The DGI 2021 PDF is identified as a project; no old tax rate is taken from it as enacted law. The new jobs use complete replacement provisions in the actual official 2026 law, not assumptions from the old Guides. No claim of a complete consolidated CGI follows.

[Legacy-topic destination map](../../evidence/ledgers/gn-old-topic-destinations.md) preserves every old topic. New-job ledgers sit beside that map; full captures, OCR and rendered pages remain privately outside Git.

Historical tax Guides awaiting research: [individual](gn-income-tax.md), [corporate](gn-corporate-income-tax.md), [VAT](gn-vat-gst.md), [overview](gn-tax-overview.md). Payroll/social and formation have new sourced methods below. All existing platform fields and complete CTA suffixes are preserved exactly. Formation and reporting remain partial for the stated gaps.

## Independent source review

The [initial review](../../evidence/ledgers/guinea-review-20261101/review.md) is preserved with its HOLD. The [focused closure](../../evidence/ledgers/guinea-closure-20261101/closure.md) accepts the repaired version within the conditional scope above. All 25 legal ledger rows and four examples carry forward unchanged; all seven domains remain partial. October promulgation, effect and the wider country gaps remain unresolved.

## Remaining-work draft, independent review pending

The expanded [payroll/social Guide](gn-payroll-social.md) now computes ordinary full-month CNSS contributions from current authority guidance and the CNSS-hosted Code/decree. The decree states a twenty-day payment window; current agency pages state fifteen days. The earlier agency date is an operational control, not a resolved legal amendment. The new [ledger](../../evidence/ledgers/guinea-remaining-20261101/gn-payroll-social.md) records the source limits. No accountant attestation or full-domain acceptance follows. The unchanged prior reviews retain their original scope.

The rewritten [formation Guide](gn-company-formation.md) adds entity choice, capital funding, route-specific APIP fees, incorporation evidence, foreign-branch controls and annual approval/registry deposit. Guinea capital/formality instruments, some fee applicability and full reporting/tax duties remain explicit gaps. Its [new ledger](../../evidence/ledgers/guinea-remaining-20261101/gn-company-formation.md) and [immutable predecessor map](../../evidence/ledgers/guinea-remaining-20261101/predecessor-destinations.json) preserve the old scope and holds. Review pending.

The expanded [property Guide](gn-property-tax.md) now adds ordinary liability, exemptions, occupied-property valuation, owner payment and qualifying rental-withholding procedures from the enacted CGI base and April 2026 DGI guidance. The March rate table and original two examples are preserved exactly. The [additive property ledger](../../evidence/ledgers/guinea-remaining-20261101/gn-property-tax.md) does not extend prior acceptance; review is pending, and the actual-period governing-version prerequisite remains. Vacant-property estimation, allocation, relief, sanctions and filing-screen gaps remain explicit.
