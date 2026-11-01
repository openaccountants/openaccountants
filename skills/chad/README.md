---
jurisdiction: TD
applicable: [IT-IND, IT-CORP, VAT, SC, PR, TP, XB]
not_applicable: {}
covered_by:
  SC: td-payroll-social
  PR: td-payroll-social
  TP: td-transfer-pricing
  XB: td-import-exemption-eligibility
partial:
  IT-IND: "2026 labour/salary/category methods supported; full BIC/BNC, disposal gains, live payroll scale, individual annual filing and treaty/exit computations remain open."
  IT-CORP: "Ordinary territorial profit/loss/minimum methods supported; depreciation maxima, sub-50million regime, instalment definition, special sectors and live filing workflow remain open."
  VAT: "Ordinary output/base/input methods and centimes supported; lower RSI entitlement, period conflict, commodity overlap, cement implementation, digital platforms and live workflow remain open."
  SC: "Archived official CNPS ordinary contribution method supported; later instruments, special workers, partial months/multiple employers and live portal remain unverified."
  PR: "Employer tax/training methods supported; monthly IRPP scale, special cases and current portal fields remain open."
  TP: "Domestic adjustment/documentation method supported; implementing template, APA/CbCR, treaty relief and fine interpretation remain open."
  XB: "Accepted narrow non-wheat import eligibility only; treaties, payment-specific withholding conflicts, foreign credits, exit, property and complete customs claims remain open."
---

# Chad: partial 2026 working-paper pack

Six legacy Guides have source-ledger-backed 2026 expansions and a new transfer-pricing Guide supplies the domestic adjustment/documentation method. Independent review of these expansions is pending. Current-year metadata and passing structural checks do not establish comprehensive coverage, a live filing procedure or accountant attestation.

## Coverage and remaining jobs

| Job | Guide | Supported method / unresolved boundary |
|---|---|---|
| Individual income | [Income](td-income-tax.md) | Salary base, annual marginal scale, residence and separate rent/capital categories; full business-profit/disposal and filing/credit paths open |
| Company income | [Corporate](td-corporate-income-tax.md) | Territorial profit bridge, deductions, ordinary losses, profit/minimum comparison, DSF timetable; specialist calculations/implementation open |
| Consumption | [VAT](td-vat-gst.md) | Principal plus centimes, base/tax point, input tests, preparation calendar; lower-regime/commodity conflicts and digital implementation open |
| Workers and employer taxes | [Payroll/social](td-payroll-social.md) | CNPS base/ceiling/shares, period/payment/late charge/annual reconciliation, employer taxes; special/current implementation issues open |
| Related-party dealings | [Transfer pricing](td-transfer-pricing.md) | Adjustments, turnover-or-assets documentation, group/entity evidence, request periods; APA/CbCR/template/relief open |
| Formation, ordinary accounts and annual corporate compliance | [Formation/reporting](td-company-formation.md) | Capital, dossier, audit tests, SYSCOHADA system/records/statement set, approval/RCCM timing; national forms/fees and specialist accounting open |
| Cross-border trade | [Import eligibility](td-import-exemption-eligibility.md) | Previously accepted narrow September non-wheat eligibility; all wheat and complete customs claims held |
| Intake/completeness | [Router](td-tax-overview.md) | Routes jobs without repeating stale headline rates; explicit gap register controls completion |

## Still unresolved, beyond Guide presence

- Ordinary individual business/noncommercial/agricultural bases, property-disposal gains, treaty/foreign credits, relocation and complete filing procedures.
- Company depreciation maxima, low-turnover legal-person regime, minimum-tax period/floor references and advance-base implementing order; petroleum/mining/banking/investment/exempt-entity calculations.
- VAT lower RSI entitlement/monthly-versus-quarterly text, milk/meat exemption overlap, cement rate, comprehensive tariff exemptions, nonresident digital platforms, input-centimes/credit implementation and current electronic normalised-invoice procedures.
- CNPS later minimum-wage/rate instruments, partial-year/month/multiple-employer/expatriate cases, annual recap date and current portal. The official archived employer page still linked its historical contribution Guide in February 2026; that is not a newly promulgated 2026 schedule.
- National SARL capital instrument, formation fees/timing, beneficial-owner/registry forms and national late-filing penalties; complete bookkeeping/recognition/valuation/consolidation, nonprofit, IFRS and sector accounting implementation.
- Payment-specific cross-border withholding, including conflicting CGI26 foreign-service paragraphs, CEMAC/treaty entitlement, property/local taxes, customs valuation/HS/declaration workflow and the wheat legal interaction. These are real remaining jobs, not assumed completed from a green check.

## Sources and review history

The official 2025 CGI was recovered from its [dated 20 July 2025 ministry archive](https://web.archive.org/web/20250720004455id_/https://www.finances.gouv.td/index.php/le-ministere/le-ministre/item/download/438_afa372566d4acca63cb857e846d67eef) after normal TLS and ordinary browser failure. Relevant clauses were read and reconciled with the [enacted 2026 finance law](https://ecofinances.gouv.td/wp-content/uploads/2026/06/Loi-n008-AN-SENAT-2025-Portant-loi-de-Finances-2026-LF-2026.pdf). CNPS/ANIE dated archives and correctly identified official OHADA Acts support the additional methods. Exact read scopes, source failures and hashes are in `docs/research/chad-remaining-2026/` and `evidence/ledgers/chad-remaining-2026/`. Full source captures remain outside Git.

The earlier import Guide and historical evidence remain byte-for-byte. Its initial source-conflict finding is in `evidence/ledgers/chad-review-20261101/review.md`, closure in `evidence/ledgers/chad-review-closure-1/closure.md`. That acceptance covered fourteen ledger rows, both import examples and the six then-unchanged legacy Guides' preservation, not the present expansions. All wheat remains held pending finance-law article65/September-order reconciliation. Old evidence is history, not extended acceptance.

Draft continuation [PR #1219](https://github.com/openaccountants/openaccountants/pull/1219), base `59c23acba2ad66dd2bb29ffc81ffbb9289769ef8`, follows merged #1179. The immutable predecessor map accounts for159 original editorial lines, including introductions, headings, bullets and table content; unsupported old claims have explicit holds. Platform fields and complete CTA suffixes are preserved. No generated packages/index/llms or application changes.

[Country issue #490](https://github.com/openaccountants/openaccountants/issues/490) remains open. All seven tax domains remain partial; formation/reporting depth and wider property/compliance work are also unfinished. No accountant attestation.
