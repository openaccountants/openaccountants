---
jurisdiction: SO
version: 0.2
last_updated: 2026-11-01
applicable: [IT-IND, IT-CORP, VAT, SC, PR, TP, XB]
not_applicable: {}
covered_by:
  IT-IND: so-income-tax
  IT-CORP: so-corporate-income-tax
  VAT: so-vat-gst
  SC: so-payroll-social
  PR: so-payroll-social
  TP: so-transfer-pricing
  XB: so-cross-border-residence
partial:
  IT-IND: "Conditional annual classification/rates and simplified screen rebuilt; effective implementation, annual top-band conflict, modified cash, relief/gain/rental workflows and current filing path unresolved."
  IT-CORP: "Ordinary-company reconciliation rebuilt; implementation, specialist deductions/sectors, transition instalments and actual forms/payment unresolved."
  VAT: "Ordinary domestic invoice method from archived signed regulation; later sector conflicts, full current amendment/exemption chain and reporting/settlement path unresolved."
  SC: "No contribution rate/base/cap or operative public/private scheme workflow established; no zero-contribution claim."
  PR: "Primary/secondary and employer transition rules sourced; mandatory notice/choice, benefits, reconciliation and live filing unresolved."
  TP: "Prior limited statutory-baseline paper preserved unchanged; current notices/circulars and documentation/CbCR/APA jobs remain open."
  XB: "Prior limited residence paper preserved unchanged; treaty/PE/source/WHT/credit/property/entry/exit computations incomplete."
---

# Somalia tax pack

**Partial source-based working papers, 1 November 2026.** Five existing Guides are expanded on the follow-on branch after merged [PR1180](https://github.com/openaccountants/openaccountants/pull/1180). Fresh independent review checked all 80 unique rule/figure rows, all 61 predecessor body lines and ten executable cases. Acceptance is limited to the expressly conditional source baseline. Neither legal currentness gates nor country acceptance criteria disappear when mechanical checks pass. No accountant has attested. [Issue486](https://github.com/openaccountants/openaccountants/issues/486) stays open.

| Job | Guide | What the expansion does | Specific unresolved work |
|---|---|---|---|
| Individual income | [Annual reconciliation](so-income-tax.md) | Income classes, ordinary/minor/non-resident rules, simplified sole-trader screen, conditional annual cases | Implementation notices, printed annual top-band conflict, modified cash, rental/gain/pension/charity methods, foreign credit and actual filing |
| Company income | [Ordinary-company method](so-corporate-income-tax.md) | Accrual reconciliation, deductions, 95% ceiling, losses, ordinary rate and instalment formula | Implementation, detailed depreciation/interest/repair/assets/financial instruments, transition instalments, special sectors and actual filing |
| Payroll | [Employer reconciliation](so-payroll-social.md) | Taxable pay, reimbursement decision, primary/secondary rules, employer transition choice, report/certificate duties | Mandatory notice and employer choice, noncash/bonus/part-month/year-end methods, form/payment/acknowledgement |
| Sales tax | [Domestic invoice method](so-vat-gst.md) | Seller/completion tax point, invoice sequence, exclusive/inclusive price decision | Current amendment/exemption/sector/territorial chain, digital split payment, threshold, return fields/deadlines, import/services, credits/refunds |
| Formation/reporting | [Company registration packet](so-company-formation.md) | Registrar reservation, domestic and certified foreign-branch documents, annual-report contents and licensing distinction | Conflicting fees/deadlines, original law/court/notarial reconciliation, ownership/investment approvals, BO, accounts/audit and licence renewal |
| Pricing | [Prior pricing paper](so-transfer-pricing.md) | Previously accepted limited statutory working paper, byte-identical | Applicable notices/circulars, method/documentation/retention/return duties, CbCR/APA and corresponding relief |
| Residence | [Prior residence paper](so-cross-border-residence.md) | Previously accepted limited domestic residence screen, byte-identical | Operative currentness; wider source/PE/treaty/WHT/credit and asset entry/exit computations |
| Social/pensions | [Payroll's explicit hold](so-payroll-social.md#the-base) | Distinguishes public/private/fund questions and rejects an inferred zero rate | Separate operative contribution law/regulations, membership, base/caps, benefits and collection procedure |

## Specific source conflicts and limits

- The Act's annual top-band constant conflicts with its lower-band arithmetic and monthly authority guidance. The income Guide identifies the exact conflict and avoids silently correcting it. [Act37 Schedule1, PDF126](https://sag.gov.so/media/documents/bulletins-contents/legislation/2025/Sharciyeedka_Canshuurta_Dakhliga.pdf).
- Regulation9-1 restricts presumptive taxation to qualifying resident individuals; the corporate summary on the authority website is broader. Primary/secondary employment and the employer-specific old/new withholding choice must be tested, not collapsed into a single monthly table. Postponement/allocation circulars and employer notices remain unlocated. [Regulations9-1,90-1 to90-3,105-8,106-1,107-1](https://mof.gov.so/sites/default/files/Publications/Income%20Tax%20Regulation_%200141%2C%202025.pdf).
- The official annual report describes delayed implementation and FY2026 plans. It is evidence of uncertainty, not a substitute for the dated legal instrument. [Directorate Annual Report2025](https://revenuedirectorate.gov.so/sites/default/files/Annual%20Revenue%20Performance_2025_FINAL11.pdf).
- The general sales-tax regulation was read from a dated official-site archive after ordinary direct/browser failure. Later sector rates and current penalties/appeals remain unreconciled. The invoice examples are conditional ordinary domestic cases.
- Registry fees and annual-report wording conflict across official publications. The formation Guide exposes both and stops before choosing a payment amount or final deadline.

## Full scope still open

No domain is declared inapplicable merely because a source or form could not be obtained. Beyond the bounded methods above, the country still needs detailed property/asset-gain and rental compliance, customs/import/export/excise work, sector/extractive/bank/insurance rules, exemptions/incentives, bookkeeping and financial reporting/audit, beneficial ownership, tax administration/registration/retention/sanctions/objections, territorial collection and the complete filing/payment/receipt jobs. Current social/pension instruments were located and partly read; their presence is not rate/base/cap coverage. The [source findings](../../evidence/ledgers/somalia-remaining-20261101/somalia-other-source-findings.md) distinguish actual clauses, scan defects, access failures and remaining instruments.

[Tax overview](so-tax-overview.md) remains byte-identical legacy2025 research, held as history and not recertified. Its old headline rates, residence/gain summaries and procedure claims must not override the new bounded Guides or their stop conditions.

## Evidence and review boundaries

All five rewritten slugs preserve every platform-owned frontmatter value and complete stamped CTA suffix. The three other Guides and all earlier review/source evidence remain unchanged. Every predecessor introduction, heading, paragraph, bullet and table item is mapped to a sourced destination or an explicit hold, with immutable base commit, blob and hash.

- [Current complete figure/rule ledger](../../evidence/ledgers/somalia-remaining-20261101/rule-rows.json), with one rendered ledger per changed Guide.
- [Complete predecessor destinations](../../evidence/ledgers/somalia-remaining-20261101/old-topic-destinations.md).
- [Income source reading](../../evidence/ledgers/somalia-remaining-20261101/somalia-remaining-source-findings.md) and [other source reading](../../evidence/ledgers/somalia-remaining-20261101/somalia-other-source-findings.md).
- [Initial three-Guide fresh review](../../evidence/ledgers/somalia-remaining-20261101/independent-review/frozen-three-review.md); [complete five-Guide review](../../evidence/ledgers/somalia-remaining-20261101/independent-review/full-five-review.md), and [targeted closure](../../evidence/ledgers/somalia-remaining-20261101/independent-review/closure.md). All four findings are closed at source candidate `2dd804ca1cde948dd5adcce2e2c3156fb3d58e0f`; acceptance remains limited to the conditional source baseline.

The original pricing/residence acceptance remains bound to the earlier historical statutory baseline and repaired candidate recorded in its [initial review](../../evidence/ledgers/somalia-review-20261101/review.md) and [closure](../../evidence/ledgers/somalia-review-closure-20261101/closure.md). That acceptance is not extended to any new expansion or claimed as operative2026 approval. Full PDFs, scans, OCR and browser captures remain in the private sibling source cache; official URLs, dates, hashes and actual reading scope are committed for review.
