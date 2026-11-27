---
name: cg-corporate-income-tax
description: "Compute ordinary Republic of Congo company income tax under the initial 2026 Finance Act, distinguishing general and sector rates, the minimum perception, deductions, interest restrictions, losses and statutory filing obligations. This is a source-cited research draft for the Republic of Congo, country code CG, using fetched official law and authority material. The initial 2026 statutory baseline is distinguished from unresolved later amendments and operating procedures. Trigger phrases include Congo-Brazzaville tax, tax calculation, tax return, source verification and country compliance. It is general reference, with explicit partial coverage and no accountant attestation. Use the linked country Guides for related jobs and obtain the missing facts before calculating or filing."
jurisdiction: CG
category: international
tax_year: 2026
tax_year_notes: "Initial 2026 enacted-law baseline; later 2026 currentness and filing procedures remain partial"
last_updated: 2026-11-27
version: 1.3
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
---

# Republic of Congo Corporate Income Tax v1.3

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

**Scope.** This guide covers ordinary company income tax (IS) under the Republic of Congo’s initial 2026 Finance Act. Obtain specialist advice for special petroleum, group and investment regimes.

## Who this applies to

Use this guide for companies and other bodies within CGI article 2.

## Rates, bands and thresholds

| Item | Rule and conditions | Authority |
|---|---|---|
| General and sector rates | Initial 2026 law: general IS 28%; microfinance and private education organised as a company 25%; mines/quarries and property operations 28%; foreign legal persons within IS 33%. Hydrocarbon exploration, production, storage and transport use their contract rate, no lower than ordinary law. Round taxable profit down to the lower XAF 1,000. | [CGI86A](https://sgg.cg/JO/2026/congo-jo-2026-3-2.pdf); ledger C01 |
| Minimum tax | Minimum perception is 1% of total operating, financial and non-ordinary receipts, excluding receipts already subject to final withholding. The gross IS liability is the greater of the minimum and the ordinary IS calculation. | [CGI86C(1)–(3)](https://sgg.cg/JO/2026/congo-jo-2026-3-2.pdf); ledger C08 |

## The base

Prepare an accounting-to-tax reconciliation. Test each cost against C04, remove IS and penalties, apply the interest limits and eligible losses, then round the taxable profit as C01 requires. Compare ordinary IS with the minimum under C08. Credit substantiated minimum instalments against the same year’s IS. Check other available credits under CGI 86B and 86C(9). The examples assume no foreign credits, incentives or separately established levy.

| Item | Rule and conditions | Authority |
|---|---|---|
| Taxable entities | Companies including single-member SA, SAS and SARL are within IS by form; public entities and other bodies conducting taxable commercial activities are within its activity scope. Partnership options and statutory exemptions must be considered separately. | [CGI2–3](https://sgg.cg/JO/2026/congo-jo-2026-3-2.pdf); ledger C02 |
| Tax base and accounts | Determine taxable net profit from all taxable receipts less allowable costs using OHADA accounting or applicable regulated-sector rules. Tax is assessed on the preceding financial year. Close accounts on 31 December unless ceasing during the year or using the first-year option under CGI 86. A business starting in the final 6 months before the mandatory close may close its first accounts at the end of the following financial year if it notifies the tax administration before 31 December of its start year. | [CGI6,9,86](https://sgg.cg/JO/2026/congo-jo-2026-3-2.pdf); ledger C03 |
| Conditions for deductions | Record costs in the tax year to which they relate. They must serve the business directly or arise in its ordinary management, be real and supported, reduce net assets and have no statutory exclusion. Exclude costs that generate exempt receipts or arise from abnormal management. Domestic supplier invoices must show the NIU and come from the certified electronic invoicing system (SFEC). Cash payments of XAF 200,000 or more fail the deduction condition. | [CGI25](https://sgg.cg/JO/2026/congo-jo-2026-3-2.pdf); ledger C04 |
| Tax and penalties | IS itself is not deductible; taxes borne by the enterprise and assessed during the year can be deductible. Exclude settlements, fines, confiscations and penalties for breaches of law. Include subsequent relief from a deductible tax in receipts for the year the company is notified. | [CGI42](https://sgg.cg/JO/2026/congo-jo-2026-3-2.pdf); ledger C05 |
| Interest restriction | Interest must meet the ordinary conditions and market pricing. Interest paid to shareholders or to companies or financial establishments in the same group under CGI 77 additionally requires fully paid capital and is limited by BEAC tender rate plus 3 points. Total annual net interest is capped at 20% of OHADA gross operating surplus attributable to non-exempt activity, with disallowed interest carryforward up to 5 years subject to the same conditions. Article 49’s interest rules exclude operating-charge interest paid or owed by financial institutions or approved insurers. No live BEAC rate is supplied. | [CGI49](https://sgg.cg/JO/2026/congo-jo-2026-3-2.pdf); ledger C06 |
| Losses | Ordinary losses carry forward through the fifth year after the loss year. Losses from IS-exempt years cannot carry forward. Deferred depreciation is unresolved: article 53 permits properly recorded and declared deferred depreciation without a duration limit, while article 75 treats depreciation booked during loss years as ordinary losses. Check this point with one of our partner accountants. | [CGI53,75: deferred-depreciation conflict](https://sgg.cg/JO/2026/congo-jo-2026-3-2.pdf); ledger C07 |

## Deadlines and filing

Identify the competent tax office and retain the NIU, existence filing, DSF schedules, payment references and electronic acknowledgements.

| Item | Rule and conditions | Authority |
|---|---|---|
| Minimum declaration and instalments | Declare the current-year minimum by 15 March using preceding-year/last-closed-year receipts provisionally. Pay four minimum-tax instalments by 15 March, 15 June, 15 September and 15 December. The minimum credits against same-year IS, but remains with Treasury where ordinary liability is lower or nil. | [CGI86C(4)–(7)](https://sgg.cg/JO/2026/congo-jo-2026-3-2.pdf); ledger C09 |
| Annual statutory rule | CGI 86F sets a 4-month period from year-end, subject to CGI 86, and requires a return even if profits are exempt. Under CGI 86G, pay the balance on filing. The ACPCE 2026 calendar lists 15 May for annual IS and 15 May following year-end for the DSF. The applicable operational deadline needs confirmation. Check this point with one of our partner accountants. | [CGI86F–G](https://sgg.cg/JO/2026/congo-jo-2026-3-2.pdf); [ACPCE2026 calendar](https://acpce.cg/wp-content/uploads/2026/02/Calendrier-des-obligations-fiscales-et-sociales-au-titre-de-lannee-2026.pdf); ledger C10 |
| Existence and filing package | Make the declarations under CGI 86E within 3 months of definitive constitution and at latest within 15 days of beginning activity. CGI 128 separately requires a declaration of existence within 15 days of starting operations. Use the prescribed DSF model. CGI 131 requires 3 complete sets of annual financial statements and an electronic copy. Under CGI 130, real-regime taxpayers file and pay electronically. If there is no statutory auditor, have an expert accountant attest and certify the financial statements. | [CGI86E,128,130–131](https://sgg.cg/JO/2026/congo-jo-2026-3-2.pdf); ledger C11 |
| Electronic filing and payment channels | From 1 October 2026, businesses in the large and medium taxpayer units and the oil and gas subcontractors unit must file through E-TAX and pay through FOUTA, including assessments raised through a collection notice. The circular permits small and very small taxpayer units and equivalent units to continue paying through the single payment counter. | [Finance Ministry circular 1091](https://www.finances.gouv.cg/sites/default/files/documents/D2026-1091_Lettre%20circulaire_Date%20ultime%20paiement%20FOUTA.pdf) |

## Penalties and interest

Apply each trigger separately. Under CGI 86F, the tax authority assesses the tax and increases the assessment under CGI 372 if the return is absent or late. For the amount of that increase, other misstatements or enforced collection, check the applicable provision before calculating. Check this point with one of our partner accountants.

| Item | Rule and conditions | Authority |
|---|---|---|
| Minimum-tax default | Failure to pay the minimum attracts 50% of the unpaid minimum under 86C(8). This is not a universal rate for every late tax. | [CGI86C(8)](https://sgg.cg/JO/2026/congo-jo-2026-3-2.pdf); ledger C12 |
| Electronic filing/payment default | Non-compliance with the real-regime electronic declaration/payment obligation attracts 10% of the amount to declare. This does not establish an all-purpose annual-return penalty. | [CGI130](https://sgg.cg/JO/2026/congo-jo-2026-3-2.pdf); ledger C13 |
| Voluntary underpayment correction | Where a taxpayer corrects an underpayment before any claim or information request from the tax administration, CGI 374 ter prescribes 0.5% per day capped at 20% of principal and no penalty in that particular case. It is not a general late-payment interest rate. | [CGI 374 ter as amended in 2026](https://sgg.cg/JO/2026/congo-jo-2026-3-2.pdf); ledger C14 |

## Cross-border points

Use [cross-border](cg-cross-border.md) for territoriality, PE and foreign payments, [transfer pricing](cg-transfer-pricing.md) for related parties and [income tax](cg-income-tax.md) for shareholder/individual income. Do not add a service withholding to IS mechanically without classifying the recipient.

## Two worked examples that recompute

### 1. CIT above minimum

Assume an ordinary domestic company has reconciled taxable profit XAF 20,000,800 and minimum-tax receipts XAF 100,000,000. C01 rounds profit to 20,000,000; 28% is 5,600,000. C08 gives minimum 1,000,000. Ordinary IS governs, before verified credits or any separately established levy.

```oa-check
name: CIT above minimum
inputs:
  profit: 20000800
  receipts: 100000000
steps:
  - rounded_profit: floor(profit / 1000) * 1000
  - ordinary: rounded_profit * 0.28
  - minimum: receipts * 0.01
  - is_before_credits: max(ordinary, minimum)
expected:
  is_before_credits: 5600000
```

### 2. Decision: deduction boundary changes ordinary tax

Assume pre-cost taxable profit XAF 10,000,000, an otherwise qualifying domestic cost of 200,000 and minimum receipts 20,000,000. Payment in cash fails C04 at equality, leaving IS 2,800,000. A qualifying traceable non-cash payment permits the cost, giving 2,744,000. The difference 56,000 is the ordinary IS consequence; all other deduction conditions still have to hold.

```oa-check
name: Decision: deduction boundary changes ordinary tax
inputs:
  profit_before: 10000000
  cost: 200000
  receipts: 20000000
steps:
  - cash_tax: max(profit_before * 0.28, receipts * 0.01)
  - noncash_tax: max((profit_before - cost) * 0.28, receipts * 0.01)
  - difference: cash_tax - noncash_tax
expected:
  cash_tax: 2800000
  noncash_tax: 2744000
  difference: 56000
```

## Ask the client first

- Legal form, incorporation and effective management?
- Activities and any petroleum/investment/group approval?
- Year-end, taxable receipts and full tax reconciliation?
- Cash/SFEC support, related-party debt and losses?
- Actual filings, payments and notices received?

## Sources

| Source and portion actually read | Official URL | Read on |
|---|---|---|
| ACPCE 2026 fiscal and social calendar, annual IS and DSF rows. | https://acpce.cg/wp-content/uploads/2026/02/Calendrier-des-obligations-fiscales-et-sociales-au-titre-de-lannee-2026.pdf | 2026-11-27 |
| 2026 Finance Act 42-2025, special Gazette 3-2026. CGI 2–3, 6, 9, 25, 42, 49, 53, 75, 86–86C, 86E–G, 128, 130–131 and 374 ter. | https://sgg.cg/JO/2026/congo-jo-2026-3-2.pdf | 2026-11-27 |
| Finance Ministry circular 1091 of 24 August 2026, E-TAX and FOUTA payment channels. | https://www.finances.gouv.cg/sites/default/files/documents/D2026-1091_Lettre%20circulaire_Date%20ultime%20paiement%20FOUTA.pdf | 2026-11-27 |

Figure/rule quotations and source hashes: [country ledger](../../evidence/ledgers/republic-of-congo-draft-20261101/cg-corporate-income-tax.md). Every worked figure is conditional on the stated example facts.

Not yet confirmed: the treatment of deferred depreciation under CGI 53 and 75, the operative annual filing date, the treatment of any separate levy, later amendments, current form fields, other penalties, sector incentives and full depreciation tables. Check this point with one of our partner accountants.
