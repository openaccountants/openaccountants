---
name: tg-corporate-income-tax
description: >
  Togo corporate income tax reference for the 2026 tax year, covering ordinary companies and taxable entities, the territorial business test, taxable profit adjustments, loss carryforwards, the minimum forfaitaire de perception and annual filing. Use it for impôt sur les sociétés, IS, corporate profit, MFP, loss relief, GUDEF financial statements and instalment calculations. The Guide applies the enacted 2026 finance law to the consolidated tax code, including the shorter construction permanent establishment test and used vehicle minimum-tax rule. It distinguishes profit tax from turnover minimum tax, links distributions and associated-party transactions to dedicated Guides, and identifies special regimes and filing details that are outside the verified computation.
jurisdiction: TG
category: international
tax_year: 2026
last_updated: 2026-11-01
version: 1.0
tier: 2
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Togo Corporate Income Tax v1.0

**General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Ordinary companies and entities within CGI arts. 91-94 are assessed under IS, subject to statutory exclusions and exemptions. SARL, SA and other taxable entities need an entity-status check; a small company is not automatically within the natural-person TPU regime. IS applies to profits of enterprises exploited in Togo and profits allocated to Togo by a tax convention. [CGI arts. 91-95; LPF art. 15](https://web.archive.org/web/20260702000000id_/https://www.otr.tg/index.php/fr/documentation/sur-les-impots/code-general-des-impots/600-code-general-des-impots-livre-des-procedures-fiscales-mis-a-jour-2025/file.html). This is the ordinary regime, with investment approvals and free-zone concessions outside the verified computation.

## Rates, bands and thresholds

| Item and conditions | 2026 rule | Official source |
|---|---|---|
| Ordinary taxable corporate profit | 27%; taxable profit rounded down to CFA 1,000 | [CGI art. 113](https://web.archive.org/web/20260702000000id_/https://www.otr.tg/index.php/fr/documentation/sur-les-impots/code-general-des-impots/600-code-general-des-impots-livre-des-procedures-fiscales-mis-a-jour-2025/file.html) |
| MFP for ordinary real-regime businesses without an exemption | 1% of turnover excluding VAT, annual minimum CFA 20,000; regulated-margin exception | [CGI art. 120, LF2026 art. 21](https://finances.gouv.tg/wp-content/uploads/2026/01/Loi-de-finances-de-lannee-exercice-2026.pdf) |
| Used vehicles imported for resale by IRPP/IS taxpayers | 2% of customs value; 2026 rule no longer limited to vehicles put into circulation in Togo | [CGI art. 120, LF2026 art. 21](https://finances.gouv.tg/wp-content/uploads/2026/01/Loi-de-finances-de-lannee-exercice-2026.pdf) |
| Carried-forward loss deduction | At most 50% of the following year's profit; unused balance carries forward without a time limit | [CGI art. 101](https://web.archive.org/web/20260702000000id_/https://www.otr.tg/index.php/fr/documentation/sur-les-impots/code-general-des-impots/600-code-general-des-impots-livre-des-procedures-fiscales-mis-a-jour-2025/file.html) |
| New business MFP exclusion | First 12 months of genuine exploitation; transformation of another entity does not qualify | [CGI art. 121](https://web.archive.org/web/20260702000000id_/https://www.otr.tg/index.php/fr/documentation/sur-les-impots/code-general-des-impots/600-code-general-des-impots-livre-des-procedures-fiscales-mis-a-jour-2025/file.html) |

## The base

1. Start from annual accounts and identify the activity taxable in Togo. Under art. 97, net profit includes operations of every kind, financial and accessory income and asset-disposal gains; do not label every capital gain exempt. Match sales to delivery and services to completion or the specific continuous-performance rule. [CGI art. 97](https://web.archive.org/web/20260702000000id_/https://www.otr.tg/index.php/fr/documentation/sur-les-impots/code-general-des-impots/600-code-general-des-impots-livre-des-procedures-fiscales-mis-a-jour-2025/file.html).
2. Reconcile book profit to tax. Deduct only actual, sufficiently evidenced charges incurred in the enterprise's direct interest or normal management, affecting net assets, in the proper year and contributing to nonexempt income. Remuneration must correspond to real work and be nonexcessive. Apply statutory depreciation, provision and specific interest restrictions rather than book deductions automatically. Enterprise taxes and duties assessed during the year are deductible unless a statute expressly excludes them (art. 99(n)); later relief on a deducted tax enters receipts when notified. Exclude IS/IRPP, the fines, settlements, confiscations, penalties and sanctions specified in art. 103(f), and private or other prohibited expenses under art. 103. [CGI arts. 98-103](https://web.archive.org/web/20260702000000id_/https://www.otr.tg/index.php/fr/documentation/sur-les-impots/code-general-des-impots/600-code-general-des-impots-livre-des-procedures-fiscales-mis-a-jour-2025/file.html).
3. Deduct eligible brought-forward losses within the cap, preserving a year-by-year rollforward. Round the resulting taxable profit down to CFA 1,000 and compute ordinary IS. [CGI arts. 101, 113](https://web.archive.org/web/20260702000000id_/https://www.otr.tg/index.php/fr/documentation/sur-les-impots/code-general-des-impots/600-code-general-des-impots-livre-des-procedures-fiscales-mis-a-jour-2025/file.html).
4. Compute MFP separately. Compare ordinary IS with the applicable turnover/customs-value minimum unless art. 121 exempts the taxpayer; MFP is the floor, not an extra tax added to ordinary IS. The new-business exemption concerns MFP and does not create a general corporate profit holiday. [CGI arts. 120-121](https://web.archive.org/web/20260702000000id_/https://www.otr.tg/index.php/fr/documentation/sur-les-impots/code-general-des-impots/600-code-general-des-impots-livre-des-procedures-fiscales-mis-a-jour-2025/file.html); [LF2026 art. 21, art. 120](https://finances.gouv.tg/wp-content/uploads/2026/01/Loi-de-finances-de-lannee-exercice-2026.pdf).
5. Deduct substantiated instalments and eligible credits from the definitive liability; an excess is handled under art. 115, subject to other direct tax debts. Do not confuse CGI art. 115 on credits with LPF art. 115 on penalties. [CGI arts. 114-117](https://web.archive.org/web/20260702000000id_/https://www.otr.tg/index.php/fr/documentation/sur-les-impots/code-general-des-impots/600-code-general-des-impots-livre-des-procedures-fiscales-mis-a-jour-2025/file.html).

## Deadlines and filing

The ordinary year ends on 31 December. New companies created before 30 June close that December; those created after 30 June can close the next December and must give the art. 96 notice at least 15 days before the legal financial-statement filing date. [CGI art. 96](https://web.archive.org/web/20260702000000id_/https://www.otr.tg/index.php/fr/documentation/sur-les-impots/code-general-des-impots/600-code-general-des-impots-livre-des-procedures-fiscales-mis-a-jour-2025/file.html).

Declare the annual result through GUDEF by 30 April after the preceding December close; insurance/reinsurance companies have 31 May. The prescribed financial statements and schedules under amended LPF art. 50 accompany the return, including the tax reconciliation, depreciation/provisions, customer list, third-party payments and remuneration/benefits. The customer list covers customers with cumulative annual sales of at least CFA 5 million excluding tax and includes their NIF, full identity, addresses, telephone number and total sales. Separately, furnish the tax administration quarterly with the list of goods/service suppliers established or domiciled in Togo, their names or business names, addresses and transaction amounts. A justified provisional return must be regularised within three months. [LF2026 art. 21, LPF arts. 49-50](https://finances.gouv.tg/wp-content/uploads/2026/01/Loi-de-finances-de-lannee-exercice-2026.pdf).

Four instalments are each one quarter of the preceding closed year's liability, rounded down to CFA 1,000, due 31 January, 31 May, 31 July and 31 October. Pay the balance with the result return and retain GUDEF acceptance and payment proof. [CGI art. 114; LPF art. 55](https://web.archive.org/web/20260702000000id_/https://www.otr.tg/index.php/fr/documentation/sur-les-impots/code-general-des-impots/600-code-general-des-impots-livre-des-procedures-fiscales-mis-a-jour-2025/file.html). The live form fields and payment-reference sequence remain unconfirmed; obtain the current prescribed model before entering a return.

## Penalties and interest

Late payment ordinarily incurs 10% for the first month and a further 1% for each month or part after the first, with a minimum of CFA 1,000. The rule also covers withholding and instalments. Do not add the separate LPF art. 116 surcharge to the art. 115 penalty. [LPF arts. 109, 115-116](https://web.archive.org/web/20260702000000id_/https://www.otr.tg/index.php/fr/documentation/sur-les-impots/code-general-des-impots/600-code-general-des-impots-livre-des-procedures-fiscales-mis-a-jour-2025/file.html). Late-result fines depend on the taxpayer segment; nil and VAT-credit returns are not exempt from sanctions. [LPF art. 113](https://web.archive.org/web/20260702000000id_/https://www.otr.tg/index.php/fr/documentation/sur-les-impots/code-general-des-impots/600-code-general-des-impots-livre-des-procedures-fiscales-mis-a-jour-2025/file.html). Late annual-result filing incurs segment-specific fines and further formal-notice consequences under art. 113; understatement/bad-faith/fraud rules are in arts. 117-118. [LPF arts. 113, 117-118](https://web.archive.org/web/20260702000000id_/https://www.otr.tg/index.php/fr/documentation/sur-les-impots/code-general-des-impots/600-code-general-des-impots-livre-des-procedures-fiscales-mis-a-jour-2025/file.html).

## Cross-border points

The 2026 replacement art. 95 includes a construction, assembly, installation or related supervision PE where the project lasts more than three months. The complete-commercial-cycle and agency/platform rules must also be tested; a shorter project does not establish absence of every other nexus. Treaty provisions require separate verification. [LF2026 art. 21, CGI art. 95](https://finances.gouv.tg/wp-content/uploads/2026/01/Loi-de-finances-de-lannee-exercice-2026.pdf).

[Transfer pricing](tg-transfer-pricing.md) covers associated-party conditions and documentary thresholds. [Cross-border and withholding](tg-cross-border.md) owns dividend, interest, royalty/service withholding and the conditional parent-subsidiary rules, rather than a blanket exemption on all group dividends.

## Two worked examples that recompute

An established ordinary company has CFA 20 million profit before losses, CFA 14 million eligible losses and CFA 180 million turnover. The loss cap permits CFA 10 million; IS is CFA 2.7 million, exceeding CFA 1.8 million MFP. Carry CFA 4 million losses forward. No credits or special approvals are assumed.

```oa-check
name: Ordinary IS after capped losses
inputs:
  profit: 20000000
  losses: 14000000
  turnover: 180000000
steps:
  - used_loss: min(losses,profit*0.5)
  - taxable: floor((profit-used_loss)/1000)*1000
  - profit_tax: taxable*0.27
  - mfp: max(turnover*0.01,20000)
  - liability: max(profit_tax,mfp)
  - loss_balance: losses-used_loss
expected:
  used_loss: 10000000
  profit_tax: 2700000
  mfp: 1800000
  liability: 2700000
  loss_balance: 4000000
```

An established company with CFA 1 million taxable profit and CFA 80 million ordinary turnover computes IS of CFA 270,000 but MFP of CFA 800,000. With no art. 121 exemption, the liability is CFA 800,000. If the same business qualifies for the first-12-month MFP exclusion, the comparison changes and ordinary IS remains the relevant charge; confirm the start date before applying the floor.

```oa-check
name: Minimum-tax decision in a low-profit year
inputs:
  profit: 1000000
  turnover: 80000000
steps:
  - profit_tax: floor(profit/1000)*1000*0.27
  - mfp: max(turnover*0.01,20000)
  - liability: max(profit_tax,mfp)
  - uplift: liability-profit_tax
expected:
  profit_tax: 270000
  mfp: 800000
  liability: 800000
  uplift: 530000
```

## Ask the client first

Obtain legal form, residence/management and activity locations, exact formation and exploitation dates, year end, turnover and regulated margins, used-vehicle imports, tax reconciliation, loss schedules, instalment receipts and approval certificates. Ask about foreign projects, group transactions, investment/free-zone approvals and distributions only where they affect the computation.

## Sources

| Source and actual read scope | URL | Read on |
|---|---|---|
| CGI (loi n°2018-024) and LPF (loi n°2018-025), OTR consolidation 2025, archived official copy. Relevant articles specified above, including neighbouring conditions; actual read scopes in the source manifest. Official live download returned 404 after site migration. Current-year archived OTR PDF read locally. | https://web.archive.org/web/20260702000000id_/https://www.otr.tg/index.php/fr/documentation/sur-les-impots/code-general-des-impots/600-code-general-des-impots-livre-des-procedures-fiscales-mis-a-jour-2025/file.html | 2026-11-01 |
| Loi n°2025-002 du 31 décembre 2025, finances 2026. Art. 2 and fiscal provisions arts. 7-21, especially the replacement CGI/LPF text in art. 21; scanned PDF read using local OCR with material provisions checked against page images. | https://finances.gouv.tg/wp-content/uploads/2026/01/Loi-de-finances-de-lannee-exercice-2026.pdf | 2026-11-01 |
| OTR Cahier fiscal 2026. Fiscal measures and reproduced amendments, pp. 7-24; administrative explanation cross-checked to the enacted finance law, which controls. | https://otr.tg/wp-content/uploads/2026/10/cahier-fiscal-2026.pdf | 2026-11-01 |

Not yet confirmed: Current GUDEF field identifiers and payment-reference steps; detailed interest limitation, all depreciation asset classes and extraordinary gains/restructuring calculations; operative investment-code and industrial free-zone relief schedules (old holiday/reduced-rate statements are not retained as blanket rules); old 3% employer salary tax and 2% capital-contribution duty claims, for which no current primary rule was established. Do not quote those figures.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
