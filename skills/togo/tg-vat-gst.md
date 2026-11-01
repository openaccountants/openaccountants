---
name: tg-vat-gst
description: >
  Togo value added tax reference for the 2026 tax year, covering ordinary domestic supplies, imports, exports, registration, input deductions and monthly returns. Use it for TVA, VAT threshold, taxable turnover, foreign services, digital platforms, factures normalisées and certified electronic invoicing. It applies the consolidated tax code with the enacted 2026 finance law, distinguishes the compulsory registration threshold from professional activity exceptions and voluntary registration, and explains why an export exemption has a different input deduction result from an ordinary exempt sale. The Guide includes the new deduction exclusions and electronic invoicing transition, with explicit gaps for implementing orders, live return fields, mixed activity calculations and special sector procedures.
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

# Togo VAT v1.0

**General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Independent persons making taxable supplies fall within TVA under arts. 172-179. Employees acting under subordination are not independent suppliers. Professional and specified freight/maritime activities are compulsorily taxable without relying on the ordinary turnover threshold. Public bodies require the competition and listed-activity tests in art. 179. [CGI arts. 172-179](https://web.archive.org/web/20260702000000id_/https://www.otr.tg/index.php/fr/documentation/sur-les-impots/code-general-des-impots/600-code-general-des-impots-livre-des-procedures-fiscales-mis-a-jour-2025/file.html). This Guide covers the ordinary system; product-specific exemptions require a classification and the actual legal list.

## Rates, bands and thresholds

| Item and conditions | 2026 rule | Official source |
|---|---|---|
| Ordinary taxable supplies | Single 18% rate, except legally exempt supplies | [CGI art. 195](https://web.archive.org/web/20260702000000id_/https://www.otr.tg/index.php/fr/documentation/sur-les-impots/code-general-des-impots/600-code-general-des-impots-livre-des-procedures-fiscales-mis-a-jour-2025/file.html) |
| Ordinary compulsory registration | Turnover greater than CFA 100 million; specified professions taxable irrespective of turnover | [CGI art. 177](https://web.archive.org/web/20260702000000id_/https://www.otr.tg/index.php/fr/documentation/sur-les-impots/code-general-des-impots/600-code-general-des-impots-livre-des-procedures-fiscales-mis-a-jour-2025/file.html) |
| Threshold met during the year | Taxability begins on the first day of the month the condition is met; falling below the limit does not end obligations for three consecutive exercises | [CGI art. 177](https://web.archive.org/web/20260702000000id_/https://www.otr.tg/index.php/fr/documentation/sur-les-impots/code-general-des-impots/600-code-general-des-impots-livre-des-procedures-fiscales-mis-a-jour-2025/file.html) |
| Voluntary registration below the ordinary threshold | Application before 30 November, CI approval; five years from the following 1 January with renewal unless timely denounced | [CGI art. 176](https://web.archive.org/web/20260702000000id_/https://www.otr.tg/index.php/fr/documentation/sur-les-impots/code-general-des-impots/600-code-general-des-impots-livre-des-procedures-fiscales-mis-a-jour-2025/file.html) |

## The base

1. Determine where the transaction is taxable, then whether a precise exemption applies. For goods, Togo location/delivery or import release governs; for services, execution is the starting point but use elsewhere moves taxation to the place of use. [CGI arts. 182-185](https://web.archive.org/web/20260702000000id_/https://www.otr.tg/index.php/fr/documentation/sur-les-impots/code-general-des-impots/600-code-general-des-impots-livre-des-procedures-fiscales-mis-a-jour-2025/file.html).
2. The ordinary supply base is total consideration plus ancillary costs and non-VAT taxes, excluding genuine discounts and documented agency disbursements. Imports use customs value plus non-VAT import duties/taxes. Apply the art. 194 rounding rule to the taxable base. [CGI arts. 186-194](https://web.archive.org/web/20260702000000id_/https://www.otr.tg/index.php/fr/documentation/sur-les-impots/code-general-des-impots/600-code-general-des-impots-livre-des-procedures-fiscales-mis-a-jour-2025/file.html).
3. Output tax on goods is due with delivery and on imports with customs release. Services and construction are ordinarily due on cash receipts, including advances, unless an approved debit basis applies. An invoice charging VAT itself creates liability under art. 191(5). [CGI arts. 189-193](https://web.archive.org/web/20260702000000id_/https://www.otr.tg/index.php/fr/documentation/sur-les-impots/code-general-des-impots/600-code-general-des-impots-livre-des-procedures-fiscales-mis-a-jour-2025/file.html).
4. Deduct properly evidenced input VAT attributable to taxable or qualifying export operations, subject to the exclusions. Export-related inputs qualify only when the exported operation would be taxable locally (art. 196). The right arises when the deductible tax becomes exigible for the supplier; exercise it in the invoice-accounting month, but for services and construction in the payment month and for self-supplies in the month the goods are allocated. Missed deductions can be claimed on later returns filed no later than 30 April of the following year (arts. 199-200). The 2026 art. 197 excludes accommodation, hospitality, restaurant, spectacle and travel expenditure, except transport expenses under a permanent transport contract and expenses meeting collective personnel needs at the workplace. Passenger vehicles have listed exceptions, and vehicle fuel is excluded. Do not deduct a restaurant invoice solely because the business paid it. Mixed activities require the art. 198-202 allocation and adjustment rules before a credit is used. [CGI arts. 196-202](https://web.archive.org/web/20260702000000id_/https://www.otr.tg/index.php/fr/documentation/sur-les-impots/code-general-des-impots/600-code-general-des-impots-livre-des-procedures-fiscales-mis-a-jour-2025/file.html); [LF2026 art. 21, replacement art. 197](https://finances.gouv.tg/wp-content/uploads/2026/01/Loi-de-finances-de-lannee-exercice-2026.pdf).
5. Financial/insurance, medical and agricultural exemptions depend on their art. 180 conditions and the annex, not the supplier's general industry. Exported goods and assimilated services are exempt under art. 181 with the specified input deduction entitlement. The temporary 2026 art. 18 exemption covers feed/compound feed/supplements for local livestock/fishery products and local livestock/fishery products transformed by operators duly registered with the competent authorities; a joint implementing order governs application and control. [CGI arts. 180-181](https://web.archive.org/web/20260702000000id_/https://www.otr.tg/index.php/fr/documentation/sur-les-impots/code-general-des-impots/600-code-general-des-impots-livre-des-procedures-fiscales-mis-a-jour-2025/file.html); [LF2026 art. 18](https://finances.gouv.tg/wp-content/uploads/2026/01/Loi-de-finances-de-lannee-exercice-2026.pdf).

## Deadlines and filing

Declare taxable and nontaxable operations, gross output VAT, input deductions and the net amount or credit on the OTR prescribed monthly return by the 15th of the following month. A nil month still requires a return. Pay the amount with the return and preserve submission and payment evidence. [LPF arts. 60-61, 65](https://web.archive.org/web/20260702000000id_/https://www.otr.tg/index.php/fr/documentation/sur-les-impots/code-general-des-impots/600-code-general-des-impots-livre-des-procedures-fiscales-mis-a-jour-2025/file.html).

Prepare a sales ledger, import documents, valid purchase invoices, exemption/export evidence and credit rollforward; reconcile each to the return. Use the official OTR e-services directory to reach the current service. The exact portal fields, credit-refund process and payment references are not confirmed by the texts read.

The 2026 replacement LPF art. 62 creates certified electronic invoices and implementing regulations. It expressly retains normalised paper invoices pending effective implementation. Art. 64 lists serial number, vignette, NIF, date, supplier identity/address/RCCM, transaction, net price, rate/tax, exemption where relevant and total; below-threshold issuers use “NE FACTURE PAS LA TVA”. This does not prove every business has already migrated to an electronic platform. [LF2026 art. 21, LPF arts. 62, 64](https://finances.gouv.tg/wp-content/uploads/2026/01/Loi-de-finances-de-lannee-exercice-2026.pdf).

## Penalties and interest

Late payment ordinarily incurs 10% for the first month and a further 1% for each month or part after the first, with a minimum of CFA 1,000. The rule also covers withholding and instalments. Do not add the separate LPF art. 116 surcharge to the art. 115 penalty. [LPF arts. 109, 115-116](https://web.archive.org/web/20260702000000id_/https://www.otr.tg/index.php/fr/documentation/sur-les-impots/code-general-des-impots/600-code-general-des-impots-livre-des-procedures-fiscales-mis-a-jour-2025/file.html). Late-result fines depend on the taxpayer segment; nil and VAT-credit returns are not exempt from sanctions. [LPF art. 113](https://web.archive.org/web/20260702000000id_/https://www.otr.tg/index.php/fr/documentation/sur-les-impots/code-general-des-impots/600-code-general-des-impots-livre-des-procedures-fiscales-mis-a-jour-2025/file.html). Understatement ordinarily carries a 40% VAT increase, rising to 60% for bad faith and 80% for fraud. Nil or credit-return default has a CFA 50,000 fine unless a specific rule applies. Invalid normalised invoices can cause deduction reversal as well as invoice sanctions. [LPF arts. 113(5), 117-118](https://web.archive.org/web/20260702000000id_/https://www.otr.tg/index.php/fr/documentation/sur-les-impots/code-general-des-impots/600-code-general-des-impots-livre-des-procedures-fiscales-mis-a-jour-2025/file.html); [LF2026 art. 21, LPF art. 64](https://finances.gouv.tg/wp-content/uploads/2026/01/Loi-de-finances-de-lannee-exercice-2026.pdf).

## Cross-border points

A foreign supplier must have an accredited local representative; failing that, recipients or beneficiaries must liquidate and pay tax under art. 185. Electronic services/platform transactions have the separate intermediary collection rule in art. 183 bis, for which the 2026 law calls for a ministerial implementation order. Do not assume every offshore invoice falls under a fully specified reverse-charge screen. [CGI arts. 183-185](https://web.archive.org/web/20260702000000id_/https://www.otr.tg/index.php/fr/documentation/sur-les-impots/code-general-des-impots/600-code-general-des-impots-livre-des-procedures-fiscales-mis-a-jour-2025/file.html); [LF2026 art. 21, CGI art. 183 bis](https://finances.gouv.tg/wp-content/uploads/2026/01/Loi-de-finances-de-lannee-exercice-2026.pdf). Keep VAT analysis separate from [income withholding](tg-cross-border.md).

## Two worked examples that recompute

An ordinary registered trader has CFA 1 million taxable net sales and CFA 54,000 valid, wholly deductible purchase VAT. Output VAT is CFA 180,000 and the monthly payable is CFA 126,000. No exempt turnover, carried credit or withholding/prepayment is assumed.

```oa-check
name: Ordinary month with eligible inputs
inputs:
  net_sales: 1000000
  eligible_input_tax: 54000
steps:
  - output_tax: net_sales*0.18
  - vat_payable: output_tax-eligible_input_tax
expected:
  output_tax: 180000
  vat_payable: 126000
```

Add a CFA 100,000 ordinary business restaurant expense that falls within the 2026 exclusion and neither statutory exception. Its CFA 18,000 VAT cannot join the eligible input pool. The correct payment remains CFA 126,000; deducting it would understate tax by CFA 18,000. The exclusion is tested before the arithmetic.

```oa-check
name: Deductibility changes the invoice decision
inputs:
  net_cost: 100000
  eligible_input: 54000
  net_sales: 1000000
steps:
  - restaurant_vat: net_cost*0.18
  - incorrect_credit: eligible_input+restaurant_vat
  - correct_payable: net_sales*0.18-eligible_input
  - incorrect_payable: net_sales*0.18-incorrect_credit
  - understatement: correct_payable-incorrect_payable
expected:
  restaurant_vat: 18000
  correct_payable: 126000
  incorrect_payable: 108000
  understatement: 18000
```

## Ask the client first

Obtain activity and annual/monthly turnover, compulsory-profession status, option approval, turnover threshold history, supply and customer locations, execution/use of services, import/export evidence, invoice dates and cash receipts. Obtain complete input invoices, asset/vehicle details, mixed taxable/exempt turnover, prior credits and the current normalised/electronic invoicing status.

## Sources

| Source and actual read scope | URL | Read on |
|---|---|---|
| CGI (loi n°2018-024) and LPF (loi n°2018-025), OTR consolidation 2025, archived official copy. Relevant articles specified above, including neighbouring conditions; actual read scopes in the source manifest. Official live download returned 404 after site migration. Current-year archived OTR PDF read locally. | https://web.archive.org/web/20260702000000id_/https://www.otr.tg/index.php/fr/documentation/sur-les-impots/code-general-des-impots/600-code-general-des-impots-livre-des-procedures-fiscales-mis-a-jour-2025/file.html | 2026-11-01 |
| Loi n°2025-002 du 31 décembre 2025, finances 2026. Art. 2 and fiscal provisions arts. 7-21, especially the replacement CGI/LPF text in art. 21; scanned PDF read using local OCR with material provisions checked against page images. | https://finances.gouv.tg/wp-content/uploads/2026/01/Loi-de-finances-de-lannee-exercice-2026.pdf | 2026-11-01 |
| OTR Cahier fiscal 2026. Fiscal measures and reproduced amendments, pp. 7-24; administrative explanation cross-checked to the enacted finance law, which controls. | https://otr.tg/wp-content/uploads/2026/10/cahier-fiscal-2026.pdf | 2026-11-01 |

Not yet confirmed: The old 10% hospitality/tour-operator rate is contradicted by the single-rate art. 195 and is not applied; exact 2026 implementation orders and rollout for certified e-invoicing and digital-service intermediary collection; mixed-use prorata and capital-goods adjustment execution; current VAT return fields, precompte operation, credit refunds and product-by-product exemption list. The domain remains partial for these ordinary practical computations and procedures.

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
