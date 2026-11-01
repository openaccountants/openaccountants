---
name: morocco-vat
description: >
  Use this skill whenever asked to prepare, review or classify transactions for a Morocco VAT
  (TVA, taxe sur la valeur ajoutee) return for tax year 2026. Covers who is liable, the two rates
  of 20% and 10% with the end of the 2024 to 2026 transition, exemptions with deduction (Art. 92)
  against exemptions without deduction (Art. 91), the cash basis and the option for the debit
  basis, the deduction right, prorata, excluded input tax, non-resident supplies, monthly and
  quarterly returns, and late filing and late payment penalties. Trigger on phrases like
  "TVA Maroc", "Morocco VAT", "declaration TVA", "SIMPL-TVA", "taux de TVA 2026", "prorata de
  deduction". Applies to businesses and professionals in Morocco. Replies in the user's language.
version: 2.1
jurisdiction: MA
category: international
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Morocco VAT v2.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

Tax year 2026. Law: Code General des Impots (CGI), 2026 edition, Art. 87 to 125, as amended by Finance Law 50-25. Authority: Direction Generale des Impots (DGI). Currency: MAD.

## Who this applies to

- Manufacturers, wholesalers, importers selling in the same state, works contractors and the other operations listed in Art. 89-I.
- Retail traders (commercants) whose taxable turnover in the previous year is MAD 2,000,000 or more (Art. 89-I-2 b). They leave VAT only after three consecutive years below that amount.
- Individual manufacturers and service providers with annual turnover above MAD 500,000. At or below that amount they are exempt without deduction (Art. 91-II-3). Once liable, they leave only after three consecutive years at or below it.
- Non-residents making taxable supplies to a client established in Morocco (Art. 115): see Cross-border points.

Out of scope: corporate tax, salary tax, CNSS and AMO. Casablanca Finance City status has its own regime: refer it.

## Rates, bands and thresholds

All rows: tax year 2026, from 1 January 2026.

| Item | Figure | Conditions | Source |
|---|---|---|---|
| Normal rate | 20% | Everything not listed at 10% or exempt | [CGI Art. 99-A](https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1) |
| Reduced rate, with deduction | 10% | Lodging, restaurants and cafes; tourist-property letting; art works; museum, cinema and theatre tickets; edible oils except palm; cooking salt; milled rice; pasta other than Art. 91-I-A-1 pasta; solar panels and solar water heaters; livestock feed; petroleum gas and petroleum oils; banking, credit and exchange commissions; securities transactions; listed agricultural and fishing equipment; wood and charcoal | [CGI Art. 99-B-1](https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1) |
| Reduced rate, 2026 end point | 10% | Public-network water, sanitation, water-meter rental; renewable electricity sold by its producers; economy car; refined sugar; urban transport and road transport of people and goods | [CGI Art. 99-B-1 and Art. 247-XXXXI](https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1) |
| Insurance agents and brokers | 10%, no deduction | Commissions on contracts brought to an insurer | [CGI Art. 99-B-2](https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1) |
| Electricity and electricity-meter rental | 20% | From 1 January 2026; 18% and 15% applied in 2025 | [CGI Art. 247-XXXXI-B and C](https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1) |
| Transport other than urban and road | 20% | From 1 January 2026; 18% in 2025 | [CGI Art. 247-XXXXI-F](https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1) |
| Road and urban transport in 2025 | 12% | For 2025 periods only | [CGI Art. 247-XXXXI-G](https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1) |
| Refined sugar in 2025 | 9% | For 2025 periods only | [CGI Art. 247-XXXXI-E](https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1) |
| Monthly return | Turnover of MAD 1,000,000 or more | Taxable turnover of the previous year; also every non-resident with taxable operations and no Moroccan establishment | [CGI Art. 108-I](https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1) |
| Quarterly return | Below MAD 1,000,000 | Also seasonal or occasional activity, and new taxpayers for the current calendar year. Can ask for monthly before 31 January | [CGI Art. 108-II](https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1) |
| Cash payment cap on input VAT | MAD 5,000 a day and MAD 50,000 a month, per supplier | Above this, VAT is not deductible unless paid by crossed cheque, bill, card, bank transfer or another listed means | [CGI Art. 106-II](https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1) |

The 7% and 14% rates are gone. Pharmaceutical products and blood derivatives are not at 10%: they are exempt with deduction (see below). Professions such as lawyers and accountants have no 10% entry in Art. 99, so they fall at 20%.

## The base

- **Taxable amount:** the price of goods, works or services plus related receipts, costs, duties and taxes, excluding VAT itself (Art. 96).
- **When VAT falls due:** on cash received, in whole or part (Art. 95). A taxpayer can opt for the debit basis (invoice or booking of the receivable) by declaring it before 1 January or within 30 days of starting. Part payments and deliveries before the debit stay taxable.
- **Exempt without deduction (Art. 91):** no output VAT, no input recovery. Includes bread, couscous, semolina, flour; milk, butter from milk; raw sugar; Moroccan packaged dates; fresh or frozen fish; fresh or frozen meat; olive oil from artisanal units; sardine tins; powdered milk; household soap; newspapers, books; school supplies; public baths and traditional ovens; insurance operations subject to the insurance contracts tax; individuals at or below MAD 500,000 (Art. 91-II-3); cooperatives under Art. 93-II conditions.
- **Exempt with deduction (Art. 92):** no output VAT, input recoverable. Includes exports of goods and of services used outside Morocco (with transport documents, or an invoice to the foreign client and proof of payment in foreign currency); goods under customs suspense; fertilisers and listed farm inputs for exclusive farm use; pharmaceutical products, blood and derivatives (Art. 92-I-19); investment goods for 36 months from the start of activity (Art. 92-I-6).
- **The 36-month window:** goods must go in a fixed asset account; cars bought by car-rental agencies are excluded. It runs from the first commercial act, or from the building permit where the business builds its project. A further 24 months can apply to businesses building their project, on the conditions in Art. 92-I-6. Existing businesses with a State agreement of MAD 50 million or more start from signature or permit.
- **Right to deduct (Art. 101):** arises in the month of the customs receipt or the partial or full payment of the invoice. It must be used within one year from that month or quarter. An excess carries to the next period.
- **Prorata (Art. 104):** a business with taxable and Art. 91 or out-of-scope turnover applies numerator / denominator. Numerator: taxable turnover including Art. 92 and 94 operations. Denominator: numerator plus Art. 91 and out-of-scope turnover.
- **Fixed assets (Art. 102):** must be in a fixed asset account. Movable goods are kept for 60 months, buildings for 10 years, or a regularisation follows.
- **No deduction (Art. 106-I):** goods and services not used for the business; unrelated premises; passenger vehicles other than public or staff collective transport; non-fuel petroleum products outside the listed diesel and kerosene cases; gifts (liberalites); mission, reception and entertainment costs; Art. 99-B-2 operations; purchases without an invoice that meets Art. 146.

### Transaction patterns

These are classification hints from the supplier name; confirm against the invoice.

| Pattern on the bank statement | Treatment |
|---|---|
| ATTIJARIWAFA, AWB, BMCE, BANK OF AFRICA, BANQUE POPULAIRE, BP, CIH, BMCI, CREDIT DU MAROC | Interest and fees: check the bank's invoice. Banking operations carry 10% (Art. 99-B-1); loan principal is outside VAT |
| DGI, CNSS, AMO | Exclude: tax and social payments, not purchases |
| DOUANE | Check for import VAT on the customs receipt |
| ONE, ONEE | Electricity 20%, public-network water 10% in 2026 |
| IAM, MAROC TELECOM, ORANGE MA, INWI | Domestic 20% |
| GOOGLE, MICROSOFT, AWS | Non-resident without a Moroccan representative: client accounts for VAT at the applicable rate (Art. 115) |

Minimum input is a bank statement, from any Moroccan bank, plus invoices for what is claimed.

## Deadlines and filing

| Filer | Period | Deadline by electronic filing | Source |
|---|---|---|---|
| Monthly | Previous month | Before the end of each month | [CGI Art. 110](https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1) |
| Quarterly | Previous quarter | Before the end of the first month of each quarter | [CGI Art. 111](https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1) |

Art. 110 and 111 set the 20th of the month for paper filing. All businesses must file electronically from 1 January 2017, on terms set by regulation (Art. 155), so the end-of-month date is the working date. Pay with the return.

Steps, in order:

1. Confirm the regime (monthly or quarterly) from last year's taxable turnover, Art. 108.
2. Total taxable turnover by activity and by rate, non-taxable and exempt turnover (Art. 112-I items 2 to 6).
3. List deductible VAT, split between non-fixed purchases (services; imports, purchases, contract work) and fixed assets (Art. 112-I-8).
4. Prepare the detailed deduction statement: invoice reference, supplier and the other Art. 112-II details.
5. Bring forward the previous period's credit (item 7), and compute VAT due or the credit to carry (item 9).
6. File electronically on the DGI portal, SIMPL, and pay the amount due by the deadline.

## Penalties and interest

| Case | Charge | Source |
|---|---|---|
| Late return, within 30 days | 5% | [CGI Art. 184](https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1) |
| Late return, after 30 days | 15% | same |
| Assessment for no return, or incomplete or insufficient return | 20% | same |
| Late payment, general | 10% penalty, plus 5% for the first month, plus 0.50% for each further month or part month | [CGI Art. 208-I](https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1) |
| Late payment within 30 days | Penalty cut to 5% | same |
| VAT unpaid or paid late (Art. 110, 111) | Penalty raised to 20%, plus the monthly charges | same |

## Cross-border points

- **Imports:** VAT is paid to customs. The customs receipt starts the deduction right (Art. 101-3).
- **Exports:** Art. 92-I-1 with its evidence, and a register of exports where no accounts are kept.
- **Non-resident supplier to a Moroccan client (Art. 115):** must appoint a Moroccan representative. Without one, a VAT-liable client declares the net amount on its own return, computes the VAT and deducts it in the same return, so the net cost is nil where the deduction is allowed. A client outside VAT withholds the tax from each payment.

## Two worked examples that recompute

**Example 1. Road haulier in 2026.** Invoice MAD 300,000 for road freight. Rate 10% from 1 January 2026. VAT MAD 30,000. The same invoice for 2025 was at 12%: MAD 36,000.

```oa-check
name: Road freight 2026 against 2025
inputs:
  net: 300000
steps:
  - vat_2026: net * 0.10
  - vat_2025: net * 0.12
expected:
  vat_2026: 30000
  vat_2025: 36000
```

**Example 2. Decision: debit basis or cash basis, with prorata.** A consultant has taxable turnover 800,000 and Art. 91 turnover 200,000, and paid input VAT of 50,000. Prorata = 800,000 / 1,000,000 = 80%, so MAD 40,000 is deductible. Output VAT at 20% is MAD 160,000 on the debit basis. On the cash basis with MAD 600,000 collected it is MAD 120,000 in the period, so the cash basis defers MAD 40,000 until the rest is received. The cash due is the figure that decides: MAD 80,000 against MAD 120,000.

```oa-check
name: Cash or debit basis with prorata
inputs:
  taxable: 800000
  exempt: 200000
  input_vat: 50000
  collected: 600000
steps:
  - deductible: input_vat * taxable / (taxable + exempt)
  - due_cash: collected * 0.20 - deductible
  - due_debit: taxable * 0.20 - deductible
expected:
  deductible: 40000
  due_cash: 80000
  due_debit: 120000
```

Quick cases: MAD 100,000 sale at 20% gives 20,000. Hotel MAD 1,500 a night at 10% gives 150. Export of MAD 5M: no output VAT, input recoverable. US services MAD 200,000: 40,000 output and 40,000 input where fully deductible. Passenger car MAD 300,000 plus 60,000 VAT: input nil. Bank interest charged by a bank: 10% (Art. 99-B-1), not exempt.

## Ask the client first

1. Business type: manufacturer, trader, service provider, profession; individual or company?
2. Last year's taxable turnover, for liability and for monthly or quarterly?
3. Cash basis, or was the debit option declared?
4. Any Art. 91 or out-of-scope turnover (prorata)?
5. New business inside the 36-month window?
6. Any supplier without a Moroccan establishment, or any export?

Never confuse Art. 92 (with deduction) with Art. 91 (without). Never apply 7% or 14% to a 2026 period. Never accept a purchase invoice that fails Art. 146. Refer Casablanca Finance City entities.

## Sources

| Source | URL | Read on |
|---|---|---|
| DGI, Code General des Impots 2026 (French), Art. 89, 91, 92, 95, 96, 99, 101, 102, 104, 106, 108, 110 to 112, 115, 144, 155, 184, 208, 247-XXXXI; extracts read, opened in a browser | https://www.tax.gov.ma/wps/wcm/connect/08712531-1e81-4e28-a38b-2bd9edf8e09e/CGI+2026+FR.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-08712531-1e81-4e28-a38b-2bd9edf8e09e-pM5DEs1 | 2026-11-01 |
| DGI, Note circulaire 737, Finance Law 50-25; title and contents page read | https://www.tax.gov.ma/wps/wcm/connect/e48c5c9d-ae80-4b30-a1b3-80af7ec09be1/NC+737+LF+2026.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-e48c5c9d-ae80-4b30-a1b3-80af7ec09be1-pOvNbSq | 2026-11-01 |

Not yet confirmed: the current SIMPL-TVA screen names, the return form number and box numbers (the old skill's lines 1 to 23 had no source; the official portal guide could not be opened, so they are removed from the steps); the old skill's blocked gifts limit of MAD 100 per item (not found in Art. 106 as read); the old MAD 200,000 services registration figure (not in Art. 91-II-3 or 89 as read); Art. 146 invoice content; any 2026 VAT change in Note 737 beyond those in the CGI text; the full Art. 91, 92 and 99 lists, which are abridged here.

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
