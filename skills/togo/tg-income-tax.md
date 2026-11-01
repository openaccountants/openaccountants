---
name: tg-income-tax
description: >
  Togo personal income tax reference for the 2026 tax year, covering resident and nonresident individuals, employees, majority managers, pensioners, landlords and independent businesses. Use it for IRPP, salaire imposable, progressive annual bands, family deductions, pension taxation, rental income, sole trader profit and Taxe Professionnelle Unique routing. It explains how to classify income before applying a rate, how to round the annual employment calculation, and when withholding replaces an annual return. The Guide distinguishes general business profit taxation from eligible small enterprise turnover taxation. It links payroll contributions and international withholding to their dedicated Guides and records unresolved procedural details before any filing work.
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

# Togo Personal Income Tax v1.0

**General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

For individuals with fiscal domicile in Togo, IRPP covers Togolese and foreign income, subject to applicable tax conventions. Domicile follows a home or principal stay, a professional activity that is not merely accessory, or the centre of economic interests; do not invent a day-count safe harbour. Nonresidents have source-income and habitation rules. [CGI arts. 2-3](https://web.archive.org/web/20260702000000id_/https://www.otr.tg/index.php/fr/documentation/sur-les-impots/code-general-des-impots/600-code-general-des-impots-livre-des-procedures-fiscales-mis-a-jour-2025/file.html). This Guide covers ordinary categories and TPU routing, not a universal tax on all receipts at the employment scale. Read the 2025 consolidated CGI together with the 2026 finance law; its art. 2 separately defines effective dates for income taxes and other measures. [LF2026 art. 2](https://finances.gouv.tg/wp-content/uploads/2026/01/Loi-de-finances-de-lannee-exercice-2026.pdf).

## Rates, bands and thresholds

| Item and conditions | 2026 rule | Official source |
|---|---|---|
| Employment, qualifying manager, pension and rental annual net income | CFA 0-900,000 exempt; 900,001-3,000,000: 3%; 3,000,001-6,000,000: 10%; 6,000,001-9,000,000: 15%; 9,000,001-12,000,000: 20%; 12,000,001-15,000,000: 25%; 15,000,001-20,000,000: 30%; above 20,000,000: 35% | [CGI arts. 74-77](https://web.archive.org/web/20260702000000id_/https://www.otr.tg/index.php/fr/documentation/sur-les-impots/code-general-des-impots/600-code-general-des-impots-livre-des-procedures-fiscales-mis-a-jour-2025/file.html) |
| Independent business profit under ordinary real regime | 30%, rather than the employment scale | [CGI arts. 29, 78](https://web.archive.org/web/20260702000000id_/https://www.otr.tg/index.php/fr/documentation/sur-les-impots/code-general-des-impots/600-code-general-des-impots-livre-des-procedures-fiscales-mis-a-jour-2025/file.html) |
| Employment family reduction | CFA 10,000 per qualifying dependent per month; maximum six dependants | [CGI arts. 72-73](https://web.archive.org/web/20260702000000id_/https://www.otr.tg/index.php/fr/documentation/sur-les-impots/code-general-des-impots/600-code-general-des-impots-livre-des-procedures-fiscales-mis-a-jour-2025/file.html) |
| TPU eligibility, natural persons only | Annual turnover at most CFA 60 million, with exclusions; forfait at most CFA 30 million, declarative above CFA 30 million through CFA 60 million | [CGI arts. 129-131; LPF art. 15](https://web.archive.org/web/20260702000000id_/https://www.otr.tg/index.php/fr/documentation/sur-les-impots/code-general-des-impots/600-code-general-des-impots-livre-des-procedures-fiscales-mis-a-jour-2025/file.html) |
| TPU declarative | Production/trade 2%, services 8% of turnover; regulated gross-margin exception; annual minimum CFA 20,000 | [CGI art. 134](https://web.archive.org/web/20260702000000id_/https://www.otr.tg/index.php/fr/documentation/sur-les-impots/code-general-des-impots/600-code-general-des-impots-livre-des-procedures-fiscales-mis-a-jour-2025/file.html) |

## The base

1. Establish fiscal domicile and classify each receipt. Employment, business, rent and investment income do not share one computational base. A spouse with own income is assessed separately, and the same child cannot produce a reduction for two taxpayers. [CGI arts. 5-6, 12-13](https://web.archive.org/web/20260702000000id_/https://www.otr.tg/index.php/fr/documentation/sur-les-impots/code-general-des-impots/600-code-general-des-impots-livre-des-procedures-fiscales-mis-a-jour-2025/file.html).
2. For employment, start with cash pay and taxable benefits. Include noncash benefits under art. 20, including the statutory vehicle valuation. Deduct qualifying mandatory pension withholding up to 6% of gross pay, compulsory employee social and health contributions, and employee payments toward benefits. The flat professional deduction is 28% on the first CFA 10 million remaining after art. 26(1)-(3). Apply other art. 26 deductions only against their documents and statutory conditions. Deduct the employment-only family reduction afterwards. A spouse without resources and qualifying children, invalid dependants or supported relatives must meet art. 72; children are under 21, or up to 25 while studying or apprenticed, with disability rules. [CGI arts. 17, 20, 23-26, 72-73](https://web.archive.org/web/20260702000000id_/https://www.otr.tg/index.php/fr/documentation/sur-les-impots/code-general-des-impots/600-code-general-des-impots-livre-des-procedures-fiscales-mis-a-jour-2025/file.html).
3. Qualifying majority managers and partners instead have the art. 28 flat expense deduction of 20% on the first CFA 10 million, followed by the art. 74 scale under art. 75. Do not add the employee flat deduction or a further abatement. [CGI arts. 28, 75, 111](https://web.archive.org/web/20260702000000id_/https://www.otr.tg/index.php/fr/documentation/sur-les-impots/code-general-des-impots/600-code-general-des-impots-livre-des-procedures-fiscales-mis-a-jour-2025/file.html).
4. Pensions/rentes of at most CFA 2.4 million annually are exempt. Under art. 27, after compulsory social charges where applicable, the income included is 25% in the annual CFA 2.4-3.6 million range and 50% above CFA 3.6 million. An employment retirement-departure indemnity has its separate 50% inclusion rule. [CGI arts. 21, 23(3), 27, 76](https://web.archive.org/web/20260702000000id_/https://www.otr.tg/index.php/fr/documentation/sur-les-impots/code-general-des-impots/600-code-general-des-impots-livre-des-procedures-fiscales-mis-a-jour-2025/file.html).
5. Private rental income uses receipts and tenant-paid owner expenses, less qualifying owner-paid tenant expenses, the 50% flat expense deduction and owner-borne property taxes. Actual expenses require the statutory election before 30 November, binding for three years from the following January. Deemed rent of the owner's own home and the specified exclusively agricultural properties are excluded. Apply the annual scale to net rent. [CGI arts. 14-16, 77](https://web.archive.org/web/20260702000000id_/https://www.otr.tg/index.php/fr/documentation/sur-les-impots/code-general-des-impots/600-code-general-des-impots-livre-des-procedures-fiscales-mis-a-jour-2025/file.html).
6. Ordinary independent business profits use the net-profit rules and 30% rate. Check TPU first: it excludes liberal/noncommercial professions, industrial bakeries, importers and exporters, as well as companies. Eligible regularly CFE-registered natural persons have the initial 24-month TPU exemption. Do not substitute the declarative percentages for a forfait taxpayer's activity-specific tariff. [CGI arts. 29-37, 78, 128-135](https://web.archive.org/web/20260702000000id_/https://www.otr.tg/index.php/fr/documentation/sur-les-impots/code-general-des-impots/600-code-general-des-impots-livre-des-procedures-fiscales-mis-a-jour-2025/file.html).
7. For the annual scale, discard taxable-income fractions below CFA 1,000, apply each band marginally, then round the tax down to CFA 10. Investment income follows its own withholding rules in [Cross-border and withholding](tg-cross-border.md). [CGI arts. 74, 79-80](https://web.archive.org/web/20260702000000id_/https://www.otr.tg/index.php/fr/documentation/sur-les-impots/code-general-des-impots/600-code-general-des-impots-livre-des-procedures-fiscales-mis-a-jour-2025/file.html).

## Deadlines and filing

The general annual return is due by 31 March for the preceding year's income. LPF art. 21 exempts taxpayers receiving only salaries, pensions/rentes and/or investment income where tax has been withheld. Business taxpayers declare their result through GUDEF by 31 March under the amended art. 22, including losses. Ordinary business instalments fall on 31 January, 31 May, 31 July and 31 October, with the balance paid with the return. [LPF arts. 20-22, 25, 43](https://web.archive.org/web/20260702000000id_/https://www.otr.tg/index.php/fr/documentation/sur-les-impots/code-general-des-impots/600-code-general-des-impots-livre-des-procedures-fiscales-mis-a-jour-2025/file.html); [LF2026 art. 21, replacement LPF art. 22](https://finances.gouv.tg/wp-content/uploads/2026/01/Loi-de-finances-de-lannee-exercice-2026.pdf).

Prepare category schedules, deductions and withholding certificates; reconcile them to the OTR prescribed return and GUDEF financial statements where required. Use OTR's official e-services directory and retain the submission receipt and payment evidence. Current screen names, form version and field numbers were not obtained; this is a computation reference, and the procedural gap remains open. Payroll remittance and DAS are in [Payroll and social](tg-payroll-social.md).

## Penalties and interest

Late payment ordinarily incurs 10% for the first month and a further 1% for each month or part after the first, with a minimum of CFA 1,000. The rule also covers withholding and instalments. Do not add the separate LPF art. 116 surcharge to the art. 115 penalty. [LPF arts. 109, 115-116](https://web.archive.org/web/20260702000000id_/https://www.otr.tg/index.php/fr/documentation/sur-les-impots/code-general-des-impots/600-code-general-des-impots-livre-des-procedures-fiscales-mis-a-jour-2025/file.html). Late-result fines depend on the taxpayer segment; nil and VAT-credit returns are not exempt from sanctions. [LPF art. 113](https://web.archive.org/web/20260702000000id_/https://www.otr.tg/index.php/fr/documentation/sur-les-impots/code-general-des-impots/600-code-general-des-impots-livre-des-procedures-fiscales-mis-a-jour-2025/file.html). Ordinary understatement is 20%, bad faith 40% and fraud 80%; identify the actual offence and any special rule before computing. [LPF arts. 117-118](https://web.archive.org/web/20260702000000id_/https://www.otr.tg/index.php/fr/documentation/sur-les-impots/code-general-des-impots/600-code-general-des-impots-livre-des-procedures-fiscales-mis-a-jour-2025/file.html).

## Cross-border points

Use [Cross-border and withholding](tg-cross-border.md) for source rules, the nonresident habitation minimum, arrivals/departures and withholding. A foreign-source salary is not excluded merely because it is paid offshore. Any treaty adjustment needs the actual operative convention and the person's residence facts; this pack supplies no treaty-rate table. [CGI arts. 2, 64-69](https://web.archive.org/web/20260702000000id_/https://www.otr.tg/index.php/fr/documentation/sur-les-impots/code-general-des-impots/600-code-general-des-impots-livre-des-procedures-fiscales-mis-a-jour-2025/file.html).

## Two worked examples that recompute

An employee already has annual net taxable income of CFA 4,000,000 after all permitted deductions. The exempt band is removed, the next CFA 2,100,000 is taxed at 3%, and the last CFA 1,000,000 at 10%. Annual tax is CFA 163,000 under art. 74. This is not a gross-to-net salary calculation.

```oa-check
name: Annual salary taxable base before scale
inputs:
  net_base: 4000000
steps:
  - tax_raw: (3000000-900000)*0.03+(net_base-3000000)*0.10
  - tax: floor(tax_raw/10)*10
expected:
  tax: 163000
```

Two eligible natural-person businesses, outside their initial exemption and without a regulated-margin exception, each have CFA 40 million turnover. A production/trade activity pays CFA 800,000 TPU; an eligible service activity pays CFA 3,200,000. The CFA 2,400,000 difference makes activity classification essential. A liberal professional is excluded and cannot elect this service percentage merely because it is lower than ordinary tax.

```oa-check
name: TPU classification changes the answer
inputs:
  turnover: 40000000
steps:
  - production_tax: max(turnover*0.02,20000)
  - services_tax: max(turnover*0.08,20000)
  - difference: services_tax-production_tax
expected:
  production_tax: 800000
  services_tax: 3200000
  difference: 2400000
```

## Ask the client first

Obtain the year, fiscal domicile facts, arrival/departure dates, income category, gross and net pay, benefits, contribution statements, dependent documents and who claims each child. For a business, obtain turnover, activity, import/export status, registration/start date, tax regime and any election. Obtain property-tax receipts and expense elections for rent, and withholding certificates for investment or foreign receipts.

## Sources

| Source and actual read scope | URL | Read on |
|---|---|---|
| CGI (loi n°2018-024) and LPF (loi n°2018-025), OTR consolidation 2025, archived official copy. Relevant articles specified above, including neighbouring conditions; actual read scopes in the source manifest. Official live download returned 404 after site migration. Current-year archived OTR PDF read locally. | https://web.archive.org/web/20260702000000id_/https://www.otr.tg/index.php/fr/documentation/sur-les-impots/code-general-des-impots/600-code-general-des-impots-livre-des-procedures-fiscales-mis-a-jour-2025/file.html | 2026-11-01 |
| Loi n°2025-002 du 31 décembre 2025, finances 2026. Art. 2 and fiscal provisions arts. 7-21, especially the replacement CGI/LPF text in art. 21; scanned PDF read using local OCR with material provisions checked against page images. | https://finances.gouv.tg/wp-content/uploads/2026/01/Loi-de-finances-de-lannee-exercice-2026.pdf | 2026-11-01 |

Not yet confirmed: Current IRPP/GUDEF screen names, return field numbers and payment-reference workflow; full TPU forfait activity tariffs; old claim of a family quotient in parts (replaced by the sourced fixed employment deduction); treaty-specific relief and foreign-tax-credit mechanics; the exact current interface for pension declarations. These gaps prevent treating the ordinary individual-income domain as complete.

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
