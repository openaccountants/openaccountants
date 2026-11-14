---
name: turkey-references
jurisdiction: TR
tax_year: 2026
last_updated: 2026-11-14
version: 2.0
description: >
  Find the official primary sources used by the Turkey 2026 tax pack and the open-source
  projects the old file listed. Use when looking for the consolidated Income Tax Law No. 193,
  Corporate Tax Law No. 5520, VAT Law No. 3065, Tax Procedure Law No. 213, the yearly income
  tax tariff and fee communiqués, the Revenue Administration (GİB) filing calendar, or the
  Official Gazette. Start from the Guide that owns the tax job, then open its cited official
  text. This is a source-navigation router without tax rates, calculations or filing authority.
  Open-source Turkish tax calculators and e-invoice libraries are tooling references, not tax
  authority evidence.
tier: 2
domain: tax
type: router
---

# Turkey: official source index 2026

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## The method, step by step

**Quick answer:** load the Guide that owns the job, then read the official text it cites. This router holds no rates of its own.

1. Pick the owning Guide from the [pack map](README.md): income tax [turkey-pit](turkey-pit.md), companies [tr-corporate-income-tax](tr-corporate-income-tax.md), VAT [turkey-vat](turkey-vat.md), payroll and social security [tr-payroll-social](tr-payroll-social.md), transfer pricing [tr-transfer-pricing](tr-transfer-pricing.md), non-residents [tr-cross-border](tr-cross-border.md), formation [tr-company-formation](tr-company-formation.md), the overview [tr-tax-overview](tr-tax-overview.md).
2. **Statute text.** mevzuat.gov.tr publishes consolidated PDFs at `https://www.mevzuat.gov.tr/MevzuatMetin/<type>.<series>.<number>.pdf`. The series prefix differs by law: Income Tax Law 1.4.193, Tax Procedure Law 1.4.213, Corporate Tax Law 1.5.5520, VAT Law 1.5.3065, Commercial Code 1.5.6102, Collection Law 1.3.6183. A wrong prefix returns an empty page, not an error, so check the text before citing it.
3. **Yearly figures.** The income tax tariff and the fixed fees are re-set each year by communiqué in the Official Gazette (for 2026: Income Tax General Communiqué No. 332 and Fees Law General Communiqué No. 98, both of 31 December 2025). GİB restates the tariff on its site. Some annexes are scans without a text layer: read them by OCR and say so.
4. **Dates.** GİB's filing calendar (Beyanname Verme ve Ödeme Süreleri) can show later dates than the statute. The owning Guide says which date is the safe one.
5. **Rates set by Presidential Decision** (VAT rates, the late payment surcharge) sit in the footnotes of the consolidated law or in GİB's consolidated decision text; check the latest decision.
6. Record the URL, the part read, the read date and a short quotation in the owning Guide's Sources table. A server answering is not a read.
7. **Open-source tooling (not tax authority).** The old file listed seven projects, kept here as tooling pointers only, as GitHub showed them on 2026-11-14:

| Project | Licence (GitHub) | Last push | What it is |
|---|---|---|---|
| ozgurg/vergihesaplayici.com | AGPL-3.0 | 2026-09-22 | Turkish tax calculator site (income tax, stamp tax and others) |
| mlevent/fatura | MIT | 2026-11-01 | PHP integration with GİB's e-Arşiv portal for e-invoices and e-SMM receipts |
| saidsurucu/borsapy | Apache-2.0 | 2026-08-07 | Python library for Borsa İstanbul data, including fund tax categories |
| berkaygure/gelir-vergisi-kesintisi-hesaplama | none stated | 2022-03-26 | Income tax withholding calculator; no licence, so do not reuse code |
| umuterturk/vergi-hesapla | AGPL-3.0 | 2025-03-07 | Tax calculation website ("Midas") |
| bahattinyunus/E-VIZOR (was arch-yunus/E-VIZOR) | MIT | 2026-01-30 | AI and OCR document processing for Turkish accounting work |
| hamitaksln/hamitaksln.github.io | none stated | 2025-09-28 | 2025 income tax calculator page; no licence, so do not reuse code |

A calculator's bracket table is never a source for a figure: take the figure from the communiqué or GİB.

## When to refuse or refer

Stop the affected figure when the official text, the year's communiqué or the decision cannot be read; record it on the owning Guide's Not yet confirmed line. Refer treaty-by-treaty withholding, free zones, technology zones and investment incentive regimes to their own official texts and a qualified professional. Do not treat a calculator project, a firm's summary or a news site as authority.

## Sources

| Source and portion read | URL | Read on |
|---|---|---|
| mevzuat.gov.tr, Gelir Vergisi Kanunu No. 193 consolidated PDF: read for the URL pattern and that the 1.4 prefix returns the law text | https://www.mevzuat.gov.tr/MevzuatMetin/1.4.193.pdf | 2026-11-14 |
| mevzuat.gov.tr, Kurumlar Vergisi Kanunu No. 5520 consolidated PDF: read for the 1.5 prefix and the in-force tables | https://www.mevzuat.gov.tr/MevzuatMetin/1.5.5520.pdf | 2026-11-14 |
| GİB, Gelir Vergisi Tarifesi 2026: read for the restated 2026 tariff and its legal basis (art. 103) | https://cdn.gib.gov.tr/api/gibportal-file/file/getFileResources?objectKey=arsiv%2Fyardim-kaynaklar%2Fyararli-bilgiler%2Fgelir-vergisi-tarifeleri%2Fgelir-vergisi-tarifesi-2026.pdf | 2026-11-14 |
| GİB, Beyanname Verme ve Ödeme Süreleri: read for the structure of the filing calendar | https://cdn.gib.gov.tr/api/gibportal-file/file/getFileResources?objectKey=arsiv%2Fyardim-kaynaklar%2Fyararli-bilgiler%2FBeyannameVermeveOdemeSureleri.pdf | 2026-11-14 |
| Official Gazette 31 December 2025, No. 33124 (5th repeat), Fees Law Communiqué No. 98: read for its basis (Law No. 492, repeated art. 138) and that its annex is a scan | https://www.resmigazete.gov.tr/eskiler/2025/12/20251231M5-28.pdf | 2026-11-14 |
| GitHub repository pages of the seven projects: read for licence, last push and owner (GitHub API) | https://github.com/ozgurg/vergihesaplayici.com | 2026-11-14 |

Not yet confirmed: whether the two projects with no stated licence allow any reuse; whether the open-source calculators match the 2026 tariff (not tested, and they are not a source in any case).
