---
name: ghana-vat
description: >
  Use this skill to prepare or review a Ghana VAT return for tax year 2026 under the Value Added Tax Act, 2025 (Act 1151), in force from 1 January 2026. It covers the 15% VAT plus 2.5% NHIL and 2.5% GETFund on one base (20% in total, all recoverable), the GHS 750,000 goods threshold, registration of all service providers, zero-rated and exempt supplies, imported services, digital services, 7% VAT withholding, upfront payment, E-VAT invoicing, the monthly return boxes, the ETAX portal, deadlines and penalties. The flat rate scheme is abolished. Trigger on "Ghana VAT", "NHIL", "GETFund", "VAT return Ghana", "withholding VAT", "VAT registration Ghana", or any Ghana VAT classification request. Payroll and income tax sit in other Ghana skills.
version: 2.1
jurisdiction: GH
category: international
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Ghana VAT v2.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

Tax year: 2026. Law: Value Added Tax Act, 2025 (Act 1151), from 1 January 2026, with GRA Guidelines GRA/AG/25/002. Tax periods are months. The return is DT 0135 on ETAX.

## Who this applies to

- **Goods:** register when taxable supplies exceed the thresholds below.
- **Services:** every provider registers within 30 days of starting, unless the Commissioner-General directs otherwise. There is no threshold ([Act 1151 s.6](https://gra.gov.gh/wp-content/uploads/2026/01/VALUE-ADDED-TAX-ACT-2025-ACT-1151.pdf), [Guidelines 7.1](https://gra.gov.gh/wp-content/uploads/2026/01/VAT-Guidelines-for-VAT-ACT-1151.pdf)).
- **Promoters of public entertainment:** at least 48 hours before the event. **Auctioneers:** within 30 days of becoming one, whatever their turnover.
- **Non-residents** selling telecommunications or electronic commerce, including digital services, for use in Ghana register under s.15 if they make a taxable supply.
- Flat rate taxpayers above GHS 750,000 and real estate developers were moved to the standard rate. Registered goods suppliers below the threshold stay registered, charge VAT and file until the Commissioner-General verifies and deregisters them ([Guidelines 15](https://gra.gov.gh/wp-content/uploads/2026/01/VAT-Guidelines-for-VAT-ACT-1151.pdf)).

## Rates, bands and thresholds

| Item | Figure | Conditions | Tax year | Official URL |
|---|---|---|---|---|
| VAT | 15% | On the value of the taxable supply or import (s.3) | 2026 | https://gra.gov.gh/wp-content/uploads/2026/01/VALUE-ADDED-TAX-ACT-2025-ACT-1151.pdf |
| NHIL | 2.5% | Same base as VAT | 2026 | https://gra.gov.gh/wp-content/uploads/2026/01/VAT-Guidelines-for-VAT-ACT-1151.pdf |
| GETFund Levy | 2.5% | Same base as VAT | 2026 | same |
| Total | 20% | COVID-19 levy repealed | 2026 | https://gra.gov.gh/domestic-tax/tax-types/vat/ |
| Zero rate | 0% | Second Schedule; levies also 0% | 2026 | https://gra.gov.gh/wp-content/uploads/2026/01/VALUE-ADDED-TAX-ACT-2025-ACT-1151.pdf |
| Goods threshold, 12 months or less | GHS 750,000 | Made, or expected in the following 12 months (s.6(1)(b)) | 2026 | same |
| Three-month test | GHS 187,500 | And expected to exceed 750,000 over that quarter plus the next nine months (s.6(2)) | 2026 | same |
| Six-month guidance figure | GHS 375,000 | GRA guidance | 2026 | https://gra.gov.gh/wp-content/uploads/2026/01/VAT-Guidelines-for-VAT-ACT-1151.pdf |
| One-month guidance figure | GHS 62,500 | GRA guidance | 2026 | same |
| VAT withholding | 7% of taxable output value | Appointed agents; not 7% of the VAT (s.56(1)) | 2026 | https://gra.gov.gh/wp-content/uploads/2026/01/VALUE-ADDED-TAX-ACT-2025-ACT-1151.pdf |
| Upfront payment | 20% of customs value | Unregistered importer required to register, import VAT base above GHS 750,000 | 2026 | https://gra.gov.gh/wp-content/uploads/2026/01/VAT-Guidelines-for-VAT-ACT-1151.pdf |
| Communications Service Tax in the base | 5% | CST is added before VAT and levies | 2026 | same |
| Tax fraction on inclusive prices | 1/6 total; VAT 1/8; NHIL 1/48; GETFund 1/48 | Tax-inclusive amount | 2026 | same |
| Mixed supplier, de minimis | Under 5% taxable: no deduction. Over 95%: full deduction | s.52(3), ratio of taxable to total supplies | 2026 | https://gra.gov.gh/wp-content/uploads/2026/01/VALUE-ADDED-TAX-ACT-2025-ACT-1151.pdf |
| Input tax time limit | 6 months after the deduction accrued | s.49(4); once only | 2026 | same |

## The base

**Value.** Charge all three on the value before tax. GHS 1,000 gives GHS 1,200 ([GRA](https://gra.gov.gh/domestic-tax/tax-types/vat/)). Excise goes into the value first, as does CST ([Guidelines 15.3](https://gra.gov.gh/wp-content/uploads/2026/01/VAT-Guidelines-for-VAT-ACT-1151.pdf)).

**Zero-rated (Second Schedule, para 2 and 3):** exports with customs evidence; goods under rental or charter used only abroad; stores on foreign-going ships and aircraft; goods to a free zone developer or enterprise with satisfactory documents; going-concern transfers with the required notices; locally manufactured textiles by an approved manufacturer to 31 December 2028; locally manufactured sanitary towels; services on land or property abroad; IP services for use abroad; freight and insurance for exports; stevedoring, port and shipping charges for transit and transshipment. Services to a free zone are standard rated ([Guidelines 14](https://gra.gov.gh/wp-content/uploads/2026/01/VAT-Guidelines-for-VAT-ACT-1151.pdf)).

**Exempt (First Schedule):** raw local food including maize, rice, tubers, fish, vegetables, fruit, nuts, coffee, cocoa beans, shea butter and edible meat; local cattle, sheep, goats, swine and poultry; agricultural inputs; fishing gear; water other than bottled or packaged; electricity to a dwelling; approved textbooks, newspapers, maps and music (not imported ones, nor periodicals, magazines or stationery); education; laboratory and library equipment; medical services and supplies; pharmaceuticals; domestic passenger transport by road, rail and water, not haulage or hire; machinery designed for agriculture, mining, manufacturing, railways, upstream petroleum and dredging; crude oil, petrol, diesel, LPG, kerosene, residual fuel oil, natural petroleum gas; dwellings and agricultural land, not supplies by an estate developer; civil engineering public works; financial services other than non-life insurance; goods for persons with disability; postage stamps; salt; mosquito nets; paper for exercise books and textbooks. A taxable-looking item must be checked against the Schedule text.

**Relief:** third Schedule persons, and holders of reconnaissance or prospecting licences, who pay and claim a refund ([Guidelines 15.8](https://gra.gov.gh/wp-content/uploads/2026/01/VAT-Guidelines-for-VAT-ACT-1151.pdf)).

**Input tax.** VAT, NHIL and GETFund are all deductible with a tax invoice or customs entry. Blocked under s.50: motor vehicles and spare parts unless the business deals in or hires them; entertainment, restaurant, meals and hotels unless that is the taxable activity; club, sporting, social or recreational subscriptions; the personal share of mixed use. Nothing on purchases for exempt supplies (s.49(3)). Unattributable input is apportioned by A x B / C (Fifth Schedule). The Commissioner-General may approve or direct another method if this one gives an unreasonable result (s.52(4)). A bank or other financial institution deducts only input directly attributable to taxable supplies (s.52(5)).

**Bad debts (s.47).** Deductible when written off, with reasonable recovery efforts, recovery proved futile, and all entries made in the books. Recovery later brings the tax back.

**Imported services (s.61, Guidelines 10).** Tax applies only so far as the service is not used to make taxable supplies. A business making only taxable supplies has nothing to self-assess. For a mixed business, the taxable value is exempt supplies / total supplies x service value. Those liable register on the portal, file DT 0134 and pay within 21 days after the period.

**Digital services (Guidelines 11).** If the non-resident is unregistered, the VAT Automatic Collection System treats the invoice as tax-inclusive and withholds at settlement. Where the service is used for taxable supplies the importer may claim that tax with records. If the supplier is registered, it invoices and the importer may claim. Non-residents under s.15 get no input deduction for digital services.

**Supplier pattern library.** Bank charges from GCB, Ecobank, Stanbic, Standard Chartered, Fidelity: exempt financial services. GRA payments and SSNIT: outside VAT. Customs: check import VAT on the entry. ECG and VRA electricity: taxable for a business, exempt only to a dwelling. Ghana Water: exempt unless bottled or packaged. MTN, Vodafone, AirtelTigo: taxable with CST in the base. Google, Microsoft, AWS: digital service rule above.

**Retail schemes.** Need written approval, for retail sales of goods only. Output tax is taxable takings x 1/6 ([GRA](https://gra.gov.gh/domestic-tax/tax-types/retail-scheme/)).

**Invoices.** Issue through the certified invoicing system. Tell GRA within 24 hours of an outage, at evat.support3@gra.gov.gh ([Guidelines 8](https://gra.gov.gh/wp-content/uploads/2026/01/VAT-Guidelines-for-VAT-ACT-1151.pdf)). To get E-VAT, write to your Taxpayer Service Centre ([GRA](https://gra.gov.gh/e-services/e-vat/)).

## Deadlines and filing

| Obligation | Date | Official URL |
|---|---|---|
| Monthly return and payment | Last working day of the next month, nil or not (ss 59(5), 60(1)) | https://gra.gov.gh/wp-content/uploads/2026/01/VALUE-ADDED-TAX-ACT-2025-ACT-1151.pdf |
| Withholding agent return and payment | 15th of the next month | same |
| Non-resident under s.15 | Last day of the next month; weekends and holidays count | same |
| Imported services | 21 days after the period | same |
| Upfront payment recovery | Apply within 6 months; decision within 30 days | https://gra.gov.gh/wp-content/uploads/2026/01/VAT-Guidelines-for-VAT-ACT-1151.pdf |
| Refund of export excess | Credit outstanding three months or more; exports over 25% of supplies and proceeds repatriated (s.53(1)(b), (2)). Other excess credit carries forward (s.53(12)); locally made textiles, sanitary towels and s.38 relief have their own refund route (s.53(1)(c), (d)) | https://gra.gov.gh/wp-content/uploads/2026/01/VALUE-ADDED-TAX-ACT-2025-ACT-1151.pdf |

**Filing the return.** Portal: www.etax.gra.gov.gh ([ITAS](https://gra.gov.gh/itas-faqs/)). Boxes are from [form DT 0135](https://gra.gov.gh/wp-content/uploads/2021/06/DT-0135-VAT-NHIL-COVID-19-Standard-Rate-Return-Form-20082018-Ver1.5.pdf), still the form GRA lists.

1. Log in and open the VAT return for the period (mm/yyyy). If nothing happened, tick Box 0 and go to the declaration.
2. **Box 1** taxable value; **Box 2** rate; **Box 3** output tax. Lines i to iii carry the supply, NHIL and GETFund. Ignore the COVID-19 line.
3. **Box 4** zero rated; **Box 5** relief; **Box 6** sum of 1, 4, 5; **Box 7** exempt; **Box 8** sum of 6 and 7.
4. Inputs: **Boxes 12 to 14** local standard; **Boxes 15 to 17** imports (claim import VAT in Box 17); **Boxes 18 to 20** withholding VAT credits. Boxes 9 to 11 are the old flat rate line; enter zero.
5. **Box 21** total inputs; **Box 22** total VAT; **Box 23** deductible input VAT.
6. **Box 24** net payable (3 less 23), or **Box 25** net credit (23 less 3). **Box 26** credit brought forward.
7. Attach documents, sign the declaration, submit, keep the acknowledgement.
8. Start payment in ETAX and pay through Ghana.gov by the same date. Keep withholding certificates.

## Penalties and interest

| Failure | Consequence | Official URL |
|---|---|---|
| Not registering | Not less than three times the tax from when registration was due (s.16) | https://gra.gov.gh/wp-content/uploads/2026/01/VALUE-ADDED-TAX-ACT-2025-ACT-1151.pdf |
| Late return | GHS 500 plus GHS 10 a day (Act 915 s.73) | https://gra.gov.gh/wp-content/uploads/2023/01/Revenue-Administration-Act-2016-.pdf |
| Late payment | 125% of the Bank of Ghana policy rate, compounded monthly | same |
| Agent fails to withhold or remit | The tax plus 30% (s.57(2)) | https://gra.gov.gh/wp-content/uploads/2026/01/VALUE-ADDED-TAX-ACT-2025-ACT-1151.pdf |
| Claiming a refund not due | Twice the original claim plus interest (s.53) | same |
| No tax invoice or receipt | Offence: fine up to 100 penalty units, or up to six months in prison, or both (s.66(1)). False invoice, or failing to use or connect the certified system: in addition, up to 50,000 currency points or three times the tax, whichever is higher (s.66(2)) | same |

## Cross-border points

- Exports need customs entry and evidence; refunds need repatriated proceeds.
- Import VAT falls due with customs duty, on customs value plus duties ([GRA](https://gra.gov.gh/domestic-tax/tax-types/vat-on-imports-and-exports/)).
- Non-residents: s.15 registration; failure can mean restriction of access to the country.
- Upfront payment applies through ICUMS as tax code 101; waiver applications go through ICUMS.

## Two worked examples that recompute

**Example 1: withholding.** A ministry, an appointed agent, buys for GHS 20,000. VAT is 3,000 and levies 1,000. Total GHS 24,000. It withholds 7% of 20,000, GHS 1,400, and pays GHS 22,600. The supplier accounts for all 4,000 and claims 1,400 in Box 20.

```oa-check
name: Withholding VAT on 20,000
inputs:
  value: 20000
steps:
  - vat: value * 0.15
  - levies: value * 0.05
  - invoice: value + vat + levies
  - withheld: value * 0.07
  - paid: invoice - withheld
expected:
  invoice: 24000.00
  withheld: 1400.00
  paid: 22600.00
```

**Example 2: is the imported service taxed, and how much?** Alpha makes taxable supplies of GHS 4,300,000 and exempt GHS 5,700,000 in a month, and imports a GHS 2,000,000 service used for both. Value subject to tax is 5,700,000 / 10,000,000 x 2,000,000, GHS 1,140,000. Tax at 20% is GHS 228,000 (GRA Illustration 3). Had Alpha made only taxable supplies, the tax would be nil.

```oa-check
name: Imported service for a mixed supplier
inputs:
  exempt: 5700000
  taxable: 4300000
  service: 2000000
steps:
  - base: service * exempt / (exempt + taxable)
  - tax: base * 0.20
expected:
  base: 1140000.00
  tax: 228000.00
```

## Ask the client first

1. Goods, services or both, and turnover over the last 3, 6 and 12 months.
2. Any exempt or zero-rated sales, and the export share.
3. Registered, and with E-VAT or an approved own system.
4. Sales to government or other withholding agents.
5. Imports of goods, and foreign services and how they are used.
6. Bank statements, invoices and customs entries for the period; a statement alone is not evidence for input tax.

Do not apply the flat rate scheme. It is abolished.

## Sources

| Source | URL | Read on |
|---|---|---|
| Value Added Tax Act, 2025 (Act 1151), OCR of scan; ss 3, 6, 15, 16, 36, 47, 49 to 53, 56, 57, 59 to 61, 66, Schedules 1, 2, 5 read | https://gra.gov.gh/wp-content/uploads/2026/01/VALUE-ADDED-TAX-ACT-2025-ACT-1151.pdf | 2026-11-01 |
| GRA VAT Administrative Guidelines GRA/AG/25/002, OCR, whole document | https://gra.gov.gh/wp-content/uploads/2026/01/VAT-Guidelines-for-VAT-ACT-1151.pdf | 2026-11-01 |
| GRA, VAT page (2026 reforms), page read in full | https://gra.gov.gh/domestic-tax/tax-types/vat/ | 2026-11-01 |
| GRA, VAT Withholding page (penalty table; page still cites Act 870), page read in full | https://gra.gov.gh/domestic-tax/tax-types/vat-withholding/ | 2026-11-01 |
| GRA, Monthly Standard VAT Return form DT 0135 (2018 version, the one GRA still lists), whole form | https://gra.gov.gh/wp-content/uploads/2021/06/DT-0135-VAT-NHIL-COVID-19-Standard-Rate-Return-Form-20082018-Ver1.5.pdf | 2026-11-01 |
| Revenue Administration Act, 2016 (Act 915); ss 27 to 30, 46, 47, 70 to 73 read | https://gra.gov.gh/wp-content/uploads/2023/01/Revenue-Administration-Act-2016-.pdf | 2026-11-01 |
| GRA, ITAS FAQs, page read in full | https://gra.gov.gh/itas-faqs/ | 2026-11-01 |
| GRA, Retail Scheme page, page read in full | https://gra.gov.gh/domestic-tax/tax-types/retail-scheme/ | 2026-11-01 |
| GRA, VAT on Imports and Exports page, page read in full | https://gra.gov.gh/domestic-tax/tax-types/vat-on-imports-and-exports/ | 2026-11-01 |
| GRA, Upfront Payment page (older figures; the Guidelines supersede it), page read in full | https://gra.gov.gh/domestic-tax/tax-types/upfront-payment/ | 2026-11-01 |
| GRA, E-VAT page, page read in full | https://gra.gov.gh/e-services/e-vat/ | 2026-11-01 |

Not yet confirmed: (1) Whether the ETAX screen has the same box numbers as DT 0135, which dates from 2018; GRA lists no 2026 form. (2) Act 1151 does not itself set NHIL and GETFund; those Acts as amended were not opened, so the levies rest on GRA guidance. (3) The s.66 amounts come from OCR of the scan; the penalty unit is GHS 12 on the GRA penalties page. (4) Six-month and one-month thresholds are in the Guidelines; the Act section read shows the 12-month and three-month tests only. (5) The GRA upfront page still says 15% and GHS 200,000; the Guidelines dated 31 Dec 2025 say 20% and GHS 750,000, and s.17 should be read for a live case. (6) Old skill box map 1 to 21 did not match the form and was replaced. (7) The old skill's 12-month wait before a bad debt claim is not in s.47 and was dropped. (8) Guidelines sect 15.7 reads 15 January in OCR where the Act took effect 1 January; treat as a scan error, not checked against a clean copy.

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
