---
name: egypt-vat
description: Use this skill whenever asked to prepare, review, or classify transactions for an Egypt VAT return or advise on Egyptian VAT registration, filing, and e-invoicing compliance. Trigger on phrases like "prepare Egypt VAT return", "Egyptian VAT", "ضريبة القيمة المضافة مصر", "ETA e-invoice", or any Egypt VAT request. ALWAYS read this skill before touching any Egypt VAT work.
version: 2.1
jurisdiction: EG
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - vat-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Egypt VAT

For tax year 2026. Figures come from the VAT Law as amended up to Law 149 of 2026 (Official Gazette no. 30 bis (a), 28 July 2026, in force the next day). Egypt has no consolidated official text on the ETA site, so read the base law together with each amending law.

## Who this applies to

**Must register:**
- Anyone selling taxable goods or services whose total taxable and exempt sales reach EGP 500,000 in the 12 months. Apply within 30 days of reaching the limit (VAT Law art. 16; UTPL art. 25). The test counts exempt sales too.
- Every importer of taxable goods or services for trade, every exporter and every distribution agent, whatever the turnover (art. 16).
- Every producer, provider or importer of a Schedule item, whatever the turnover (arts. 1, 41).
- Non-residents selling to unregistered customers in Egypt, under the simplified supplier system (art. 17, replaced by Law 3 of 2022; Regulations art. 21 bis text added by Decision 24 of 2023).
- Legal persons who sell nothing taxable but must account for imported services, for reverse charge purposes (art. 17).

**May register:** a person under the limit (art. 18). They then carry all the duties of a registered person.

**Not caught:** a natural person who does not carry on a business of selling goods or providing services, even if sales reach the limit (art. 16).

**If you do not apply,** the tax office registers you from the data it holds and tells you within 5 working days (Unified Tax Procedures Law (UTPL) art. 25; UTPL art. 4 repealed VAT Law art. 16 paras 3 and 4). Failure to register on time is treated as evasion (art. 68(1)).

**Under the limit:** a person below the limit must still register on the ETA electronic system for an annual fee set by the Minister, at most EGP 500, which stops when sales reach the limit (UTPL art. 25).

**Small projects:** a project with annual turnover up to EGP 20 million that opts into Law 6 of 2025 files VAT quarterly (see Deadlines). A consultancy earning at least 90% of annual turnover from one or two persons is outside it (Law 6/2025, art. 4). The choice locks in for five years (art. 5).

## Rates, bands and thresholds

| Item | Figure | Conditions | Tax year | Official URL |
|---|---|---|---|---|
| General rate | 14% | All taxable goods and services; 1% point of the tax goes to social justice programmes (art. 3, replaced by Law 149/2026 art. 1) | 2026 | https://eta.gov.eg/sites/default/files/2026-08/law.no_.149.of_.2026.pdf |
| Machinery, equipment and medical devices | 5% | Used to produce a good or provide a service. Buses and passenger cars stay outside. Devices used for medical purposes count as medical devices (art. 3) | 2026 | same |
| Machinery parts and spare parts | 14% | Regulations art. 4 | 2026 | https://eta.gov.eg/sites/default/files/2024-03/vat-law_no.66-2017.pdf |
| Exports of goods and services | 0% | Conditions in Regulations art. 5; see The base (VAT Law art. 3) | 2026 | same |
| Free zone exports and project inputs | 0% | Free zones, free cities, free markets and special economic zones; passenger cars excluded (art. 6, replaced by Law 3/2022) | 2026 | https://eta.gov.eg/sites/default/files/2024-03/vat-law_no.3-2022.pdf |
| Advertising services | 14% | Listed public-interest adverts stay exempt (exempt item 57); Law 3/2022 art. 5 | 2026 | same |
| Registration limit | EGP 500,000 | Taxable plus exempt sales, 12 months (art. 16); the minister may change it by decision | 2026 | https://eta.gov.eg/sites/default/files/2024-03/vat-law_no.67-2016.pdf |
| Tourist refund floor | EGP 1,500 per invoice | Foreign visitors staying up to 3 months; goods leave with them or otherwise (art. 30 bis) | 2026 | https://eta.gov.eg/sites/default/files/2024-03/vat-law_no.3-2022.pdf |
| Credit balance refund | More than 4 consecutive periods | Art. 30(1)(3), replaced by Law 149/2026. Was 6 periods before 29 July 2026 | 2026 | https://eta.gov.eg/sites/default/files/2026-08/law.no_.149.of_.2026.pdf |
| Same, Law 6/2025 projects | More than 3 months | Art. 30(1)(3) | 2026 | same |
| Machinery tax suspension | 1 year, extendable to 3 years in total | Factories and production units, industrial production; includes medical devices (art. 28 bis, replaced by Law 149/2026) | 2026 | same |
| Natural gas Schedule tax | EGP 20 per 1,000 cubic feet | New Schedule I item 17 (Law 149/2026 art. 3) | 2026 | same |
| Crude oil Schedule tax | 10% of value | Schedule I item 16 (Law 157/2025 art. 5) | 2026 | https://eta.gov.eg/sites/default/files/2025-07/vat-law_no.157.of_.2025.pdf |
| Goodwill on shop sale or rent | 10% of 10% of the rent or sale value | Schedule I item 15 (Law 157/2025 art. 2); return type "Schedule and VAT", Excel code 46 | 2026 | same |
| Professional and consulting services | 10% of the amount actually paid | Schedule I item 12: Schedule tax only. Craftsmen are outside it | 2026 | https://eta.gov.eg/sites/default/files/2024-03/vat-law_no.67-2016.pdf |
| Contracting and construction | 14% | Schedule I item 9 repealed by Law 157/2025 art. 6. Decision 418/2025 art. 1 has the contractor collect VAT at the rate set by law on the invoice, and covers contracts straddling the change | 2026 | https://eta.gov.eg/sites/default/files/2025-07/vat-law_no.157.of_.2025.pdf |
| Gypsum; soap and household detergents | 14% | Schedule I items 8 and 10 (5% Schedule tax) repealed by Law 149/2026 art. 4 from 29 July 2026. The repeal names no rate: 14% follows from arts. 2 and 3, because neither item is on the exempt list. Gypsum in its natural state falls under exempt item 20 | 2026 | https://eta.gov.eg/sites/default/files/2026-08/law.no_.149.of_.2026.pdf |
| Air-conditioned inter-governorate transport (bus, rail) | 5% of value | Schedule I item 11 | 2026 | https://eta.gov.eg/sites/default/files/2024-03/vat-law_no.67-2016.pdf |
| Other Schedule I items as enacted | Edible oils and fats 0.5%; crackers and flour confectionery, processed potato products, fertilisers and pesticides, media and film production 5% | Schedule I items 3 to 7 and 13; later amendments to items 3 and 4 changed the description | 2026 | same |

**Schedule I** items bear Schedule tax only: no VAT and no input credit, except that tax paid on machinery parts, equipment and spare parts used for Schedule-only output can be settled against Schedule tax (art. 27). **Schedule II** items bear Schedule tax plus VAT, and input credit goes against the VAT only (Regulations art. 27). Check tobacco, alcohol, fuel, vehicles and similar items against the Schedule and its amendments for the rate.

### Exempt list, 2026 changes

Replaced by Law 149/2026 art. 2:
- Item 19: butane gas only. Natural gas moved to the Schedule.
- Item 20: natural materials and mine and quarry products in their natural state, except crude oil and natural gas.
- Item 28: sale and rent of vacant land, farmland, buildings and residential units, and sale and rent of non-residential buildings, except rent of premises used as an independent seat of a business, even with a commercial character and customer contact. Premises for religious, charitable, social, educational and health activities stay exempt, as do others the minister names.
- Item 32: wheelchairs, prosthetics, hearing aids and other worn or implanted devices, now with their production inputs; dialysis equipment with inputs; incubators, serums, vaccines, blood, blood bags, family planning means.
- Item 35: postal savings banking and financial services of the National Postal Authority.
- Item 36: non-bank financial services supervised by the FRA or the Central Bank.

Removed by Law 157/2025: items 18 (crude oil) and 48 (news agency services).

Other main exempt items (list to Law 67/2016 as amended by Law 3/2022): dairy and infant food; eggs other than pasteurised; tea, sugar, coffee; mill products; bread; meat, fish and fresh produce; water purification and distribution and sewerage, not bottled water; electricity; newsprint; books and newspapers; bank operations reserved by law to banks; currency exchange; insurance and reinsurance; education, training and research; health services other than non-medical cosmetic and slimming work; land passenger transport other than tourist transport, inter-governorate air-conditioned transport and private car rental; non-tourist water and air passenger transport; medicines; Suez Canal Authority services to transiting ships (item 58).

## The base

**What is taxed.** Goods and services, local or imported, at every stage (art. 2). A sale happens at the earliest of invoice, delivery or performance, or payment (art. 1). Self-supply for personal use or special use counts as a sale (art. 5).

**Value.** The amount paid or due, including all charges collected from the buyer and incidental costs (art. 10). Sales between related persons cannot be below an arm's length price (related means spouses, ascendants and descendants, and 50% ownership links, art. 1). Schedule II items: value plus Schedule tax. Gold, silver, platinum and gemstones: workmanship value only (art. 10(9)). Imports: customs value plus customs tax and other charges (art. 10(7)).

**Input credit.** Deduct VAT borne on inputs tied to taxable sales, including machinery (arts. 1, 22). The credit stops at the tax due, and the rest carries forward (art. 22). No credit for: Schedule tax, input tax included in cost, exempt goods and services, and simplified supplier cases (art. 22, Law 3/2022). Indirect inputs include construction, finance, indirect production, selling and general costs (Regulations art. 1, Decision 417/2025).

**Mixed sales** (Regulations art. 27):
1. Inputs for taxable sales only: full credit.
2. Inputs for exempt or Schedule-only sales: no credit.
3. Shared inputs: credit by taxable sales over total sales.

Reverse any earlier credit by an addition notice.

**Opening stock.** Credit VAT on stock held at registration if you keep regular books, hold the purchase invoices or customs papers, file the stock statement form with the application, have not costed the tax (or corrected that within one year of purchase), and the stock relates to taxable sales (Regulations art. 22 as replaced by Decision 417/2025).

**Exports.** Goods: follow customs procedure and keep the export papers, including the customs export certificate, for 5 years. Services: prove the deal with a foreign recipient by contract or other suitable means, hold the tax invoice with service details, and hold proof of payment by bank transfer from abroad to a bank supervised by the Central Bank (Regulations art. 5).

**Continuous services.** The invoice triggers the tax for telecoms, cleaning and security, goods transport, and contracting supported by the consultant's approved certificate (art. 33; Regulations art. 26 as replaced by Decision 417/2025).

**Tax invoice.** Serial number, date, seller name, address and registration number, buyer name, address and tax registration or national number, description, value, rate, tax, total (Regulations art. 13; VAT Law art. 12 was repealed by UTPL art. 4).

## Deadlines and filing

| Duty | When | Source |
|---|---|---|
| Monthly return, Form 10 | Within the month after the tax period ends, even with no sales | UTPL art. 31(a) |
| Quarterly return, Law 6/2025 project | Every 3 months, within the month after the period, with payment | Law 6/2025 art. 12 |
| Gold and silver, Form 10 bis | Same monthly deadline | ETA FAQ |
| Reverse charge, Form 111 | 30 days from receiving the service | Art. 32; ETA FAQ |
| Register | 30 days from reaching the limit | Art. 16; UTPL art. 25 |
| Notify changes | 30 days from the change; heirs 60 days from death | UTPL art. 28 (VAT Law art. 20 repealed) |
| Records | Keep 5 years after the tax period | UTPL art. 38 (VAT Law art. 13 repealed) |

A deadline on an official holiday moves to the next working day (Regulations art. 16). The VAT law's old two-month period and 15 June April rule were overtaken by UTPL art. 31 and by art. 14 as replaced in 2022. The 2017 Regulations still show the old rule; the law wins.

An exporter, importer or service provider acting once or twice a year can ask ETA to file only for that month (UTPL art. 31).

### How to file the monthly return

1. Log in to the ETA portal linked from eta.gov.eg ("بوابة الممول").
2. Open the obligations box and pick Form 10 for the period. For an earlier period, add it through the forms box: Add form, VAT forms, tax period.
3. Upload invoices one of three ways: one at a time; the system Excel sheet, up to 60,000 invoices; or Excel through attachments, above 60,000. ETA publishes the sales and purchases sheets on its VAT forms page.
4. Report sales lines. Sales sheet fields include document type (DOC_TYP_S), tax type (TAX_TYP), Schedule type (TYP_SCH), invoice number (INVNUM), customer registration number (CUST_REG_NO), net (NET_AMM), tax (TAX_VAL), total (TOTAL).
5. For an imported service needed for your business, enter the invoice value twice: once in sales and once in purchases.
6. First return on the new system: enter the earlier credit balance once. It then carries forward automatically.
7. No activity: choose Form 10, return type "zero".
8. Press Submit. The system issues a reference number at the top of the page. The PDF shows the sending date; a blank date means it is only a saved draft.
9. Pay after filing. The system issues a claim, and you pay by claim number, not registration number. You cannot pay first.

**Returned goods:** enter an addition or discount notice in the current return, or amend the earlier one. The notice date must match the return period.

**Amended return:** Add form, VAT forms, tax period, Form 10, return type original or amended. Conditions: the original was on time, no Form 4 examination notice has been issued for the period, and the period is not in anti-evasion work.

**Refund:** claim with supporting papers, including a certificate signed by a listed accountant unless the payment shows on the ETA electronic system. ETA pays within 45 days (art. 30). Grounds: exports, tax collected in error, the credit balance above, buses and passenger cars where carrying passengers is the licensed activity, and tax borne by a simplified non-resident. A late refund bears interest at the Central Bank credit and discount rate on 1 January, plus 2 points (UTPL refund chapter).

**After filing:** ETA may assess or amend within 5 years of the filing deadline; 6 years for evasion (UTPL art. 44). You have 30 days from notice to object to an assessment, or the assessment becomes final (UTPL art. 55). An internal committee decides within 60 days of receiving the file, extendable once, then the appeal committee. Court appeal is 60 days (UTPL art. 55). VAT Law art. 48 and the dispute chapter except art. 62 were repealed by UTPL art. 4.

## Penalties and interest

| Event | Consequence | Source |
|---|---|---|
| Unpaid tax | Additional tax 1.5% a month or part month from the end of the payment period | VAT Law art. 1 |
| ETA amends after year 3 | No additional tax from the end of year 3 to the notice | Art. 15 |
| Return or payment late up to 60 days; wrong data raising the tax | Fine EGP 3,000 to 50,000 plus tax, tripled on repeat | UTPL art. 69 |
| Return over 60 days late | Fine EGP 5,000 to 200,000, doubled on repeat within 3 years | UTPL art. 70 |
| Other non-evasion breaches under the VAT law | 1% of the tax due, minimum EGP 1,000, maximum EGP 10,000, doubled within 3 years | Art. 50 as added by Law 3/2022 art. 2 (old art. 66 repealed by UTPL art. 4) |
| Evasion, such as no invoices, wrongful credit, late registration | 3 to 5 years in prison and/or fine EGP 5,000 to 50,000 | Arts. 67, 68 |
| Non-resident registrant in default | Minister may seek a block on access to the Egyptian market | Art. 67 bis, Law 3/2022 |
| Settlement of an offence | Pay 100% of the tax amounts due before prosecution, 150% before judgment, 175% after a final judgment | UTPL art. 75 (VAT Law art. 73 repealed) |

Law 152/2026 renews the Law 79/2016 dispute settlement scheme; Decision 450/2026 sets the application.

## Cross-border points

- **Imported goods:** VAT at customs clearance, no final release before payment (art. 31). Not collected where a non-resident registrant already collected it (art. 5).
- **Imported services for your taxable business:** you are importer and supplier together (art. 32); put it in Form 10.
- **Services not needed for your business, or received by a government or other body:** pay within 30 days on Form 111 unless the supplier uses the simplified system (art. 32).
- **Non-residents selling to unregistered customers:** register on the ETA portal on the simplified form, personally or through a representative. Input credit does not apply, but a refund claim can be filed electronically (Regulations as amended by Decision 24/2023). ETA can treat a non-applicant as registered by notice.
- **Free zones:** taxed when goods or services enter for local consumption inside the zone or the local market (art. 7).
- **Transit goods and services on them:** no tax, if carried under customs control (art. 5, Law 149/2026).

## Two worked examples that recompute

**Example 1. Mixed seller.** A Cairo firm sells EGP 3,000,000 taxable and EGP 1,000,000 exempt. Direct taxable inputs bear EGP 140,000 VAT, and shared overheads bear EGP 56,000. Output is EGP 420,000. Shared credit is 75%, EGP 42,000. Payable is EGP 238,000.

```oa-check
name: Mixed seller, one month
inputs:
  taxable: 3000000
  exempt: 1000000
  direct_input: 140000
  shared_input: 56000
steps:
  - output: taxable * 0.14
  - share: taxable / (taxable + exempt)
  - shared_credit: shared_input * share
  - payable: output - direct_input - shared_credit
expected:
  output: 420000.00
  shared_credit: 42000.00
  payable: 238000.00
```

**Example 2. Should a small B2B trader register voluntarily?** Sales are EGP 400,000 a year, below the limit, and purchases EGP 250,000 net carry 14% VAT. Unregistered, the VAT of EGP 35,000 is a cost. Registered, the trader charges business customers EGP 56,000, who can claim it, and credits the EGP 35,000. Registering saves EGP 35,000 if customers accept the same net price. If the customers are consumers who pay a fixed price of EGP 400,000, the VAT comes out of that price: net sales are EGP 350,877.19 and output VAT EGP 49,122.81, so the trader ends EGP 14,122.81 worse off. Decide on who the customers are.

```oa-check
name: Voluntary registration, both ways
inputs:
  sales: 400000
  purchases: 250000
steps:
  - input_vat: purchases * 0.14
  - b2b_gain: input_vat
  - consumer_net: sales / 1.14
  - consumer_output: sales - consumer_net
  - consumer_change: input_vat - consumer_output
expected:
  input_vat: 35000.00
  b2b_gain: 35000.00
  consumer_output: 49122.81
  consumer_change: -14122.81
```

## Ask the client first

1. Annual sales, taxable and exempt, and whether a Law 6/2025 election is in place.
2. What is sold, with Schedule and exempt item checked. Any mix?
3. Importer, exporter, distribution agent, or non-resident?
4. Any services bought from abroad, and needed for the business or not?
5. Any item touched by the 2025 or 2026 changes: contracting, commercial rent, gypsum, detergents, gas, machinery?
6. Existing credit balance and how many periods old.

### Working defaults when facts are missing

| Gap | Default |
|---|---|
| Rate unknown | 14% |
| 5% unclear | 14% until the use is shown |
| Export papers incomplete | Domestic 14% |
| Business use unknown | No credit |
| No tax invoice | No credit |

Review prompts for the reviewer's file: single transaction above EGP 500,000; tax effect of one default above EGP 70,000; one party above 40% of sales or purchases; more than four defaults in a return; net position above EGP 1,000,000.

### Reading bank lines and supplier types

| Line or supplier type | Treatment |
|---|---|
| Bank fees | Exempt where reserved to banks, no input VAT |
| Insurance premiums | Exempt |
| Electricity | Exempt |
| Water distribution | Exempt; bottled water taxed |
| Hospitals, clinics, medicines | Exempt, other than non-medical cosmetic and slimming work |
| Rail, metro, taxi, air passenger fares | Exempt, other than the carve-outs above |
| Accountant, lawyer, consultant | Schedule 10%, no credit for the buyer |
| Advertising agency | 14% |
| Foreign cloud or software with SWIFT debit | Imported service; Form 10 twice if business use |
| Customs payment | VAT claimable with customs certificate and receipt |
| Foreign currency credit | Check export papers before 0% |

Keep a working paper with date, party, registration number, invoice reference, net, rate, VAT, in or out, flags; tabs for sales, purchases, customs, foreign services, summary and queries. Without invoices, net is total divided by 1.14 for estimating only; no input credit without a tax invoice. Refer partial credit disputes, refunds, free zone cases and real estate questions to a licensed Egyptian adviser.

## Sources

| Source | URL | Read on |
|---|---|---|
| Law 67/2016, whole law, schedules and exempt list, read by OCR, key pages by image; read for the figures cited | https://eta.gov.eg/sites/default/files/2024-03/vat-law_no.67-2016.pdf | 2026-11-01 |
| Law 149/2026, all pages by image or OCR; read for the figures cited | https://eta.gov.eg/sites/default/files/2026-08/law.no_.149.of_.2026.pdf | 2026-11-01 |
| Correction notice for Laws 149 to 151 of 2026; read for the figures cited | https://eta.gov.eg/sites/default/files/2026-08/law.no_.149.150.151.of_.2026.retractation.pdf | 2026-11-01 |
| Law 157/2025, arts. 2, 4, 5, 6; read for the figures cited | https://eta.gov.eg/sites/default/files/2025-07/vat-law_no.157.of_.2025.pdf | 2026-11-01 |
| Law 3/2022, whole law; archived copy, ETA refused the direct connection; read for the figures cited | https://web.archive.org/web/2025/https://eta.gov.eg/sites/default/files/2024-03/vat-law_no.3-2022.pdf | 2026-11-01 |
| Regulations, Decree 66/2017, arts. searched, not the whole; archived copy; read for the figures cited | https://web.archive.org/web/2025/https://eta.gov.eg/sites/default/files/2024-03/vat-law_no.66-2017.pdf | 2026-11-01 |
| Decision 24/2023, non-resident parts; archived copy; read for the figures cited | https://web.archive.org/web/2025/https://eta.gov.eg/sites/default/files/2024-03/vat-law_no.24-2023.pdf | 2026-11-01 |
| Decision 417/2025; read for the figures cited | https://eta.gov.eg/sites/default/files/2025-12/mof.decision.no_.417.of_.2025.pdf | 2026-11-01 |
| UTPL Law 206/2020, issuing art. 4 (VAT repeals), arts. 25, 28, 31, 38, 44, 55, 69, 70, 75, refund chapter; read for the figures cited | https://eta.gov.eg/sites/default/files/2024-03/law_no.206-2020.pdf | 2026-11-01 |
| Law 6/2025, arts. 4, 5, 12; read for the figures cited | https://eta.gov.eg/sites/default/files/2025-02/law_no.6.of_.2025.pdf | 2026-11-01 |
| ETA FAQ, returns (VAT), 2nd edition; archived copy; read for the figures cited | https://web.archive.org/web/2026/https://eta.gov.eg/sites/default/files/2024-12/faqs-value-added-tax.v2.pdf | 2026-11-01 |
| ETA VAT laws list and VAT forms page, sales sheet archived copy; read for the figures cited | https://eta.gov.eg/ar/content/qwanyn-aldrybt-ly-alqymt-almdaft | 2026-11-01 |

Not yet confirmed: the EGP 250,000 VAT limit attributed to Resolution 281 of 2025: VAT Law art. 16 reads EGP 500,000, ETA's VAT law list shows no such decision, and the minister's power to change the limit means a decision outside that list would displace the figure; e-invoice and e-receipt scope and phases (old text said mandatory for all registered businesses; the decisions were not read); VAT Regulations article numbers for the simplified system, opening stock form number and continuous services (OCR digits); whether any later law changed the 1.5% additional tax; the Schedule rate reading of 14% has no ETA instruction behind it for gypsum and detergents; government bodies' direct payment share under art. 31 as replaced in 2022 (the figure did not read clearly); mobile telecom Schedule II rate and current Schedule rates for tobacco, alcohol, fuel, vehicles; used goods 90% base in art. 10(10) (digit not image-checked); deregistration conditions; VAT on real estate sale details and construction contract straddling terms in Decision 418/2025; simplified agricultural regimes; form box numbers of Form 10 itself, which ETA does not publish outside the logged-in portal (the old Section A to K letters had no official source and are removed); portal screens not seen, steps come from the ETA FAQ; ride-hailing, courier and post, payment gateway and mobile wallet treatment by named supplier.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

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
