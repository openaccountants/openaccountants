---
name: egypt-vat
description: Use this skill whenever asked to prepare, review, or classify transactions for an Egypt VAT return or advise on Egyptian VAT registration, filing, and e-invoicing compliance. Trigger on phrases like "prepare Egypt VAT return", "Egyptian VAT", "ضريبة القيمة المضافة مصر", "ETA e-invoice", or any Egypt VAT request. ALWAYS read this skill before touching any Egypt VAT work.
version: 2.4
jurisdiction: EG
tax_year: 2026
last_updated: 2026-11-26
depends_on:
  - vat-workflow-base
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: vat-gst
type: situation-rules
---

# Egypt VAT

For 2026, in EGP. Start with the transaction, registration position and return period. The examples assume established classifications and credit eligibility; they do not decide those facts.

## Who this applies to

**Registration.** A seller of taxable goods or services must register when taxable **and exempt** sales reach EGP 500,000 (VAT Law art. 16). Its commencement test used the previous 12 months; for subsequent periods the text says a financial year or part of one. Do not substitute a rolling-12-month rule for that wording. Apply within 30 days of reaching the limit. Importers of taxable goods/services for trade, exporters and distribution agents register regardless of turnover. The natural-person exception is for someone who does not conduct an activity selling goods or providing services. A below-limit person may apply voluntarily, subject to the Regulations, and then has registered-person duties. [Law 67/2016 arts. 16, 18](https://eta.gov.eg/sites/default/files/2024-03/vat-law_no.67-2016.pdf)

**Decision 281/2025.** The cited ETA Head decision concerns the named taxpayers in e-receipt phase 8, second sub-phase, from 15 September 2025; its signature is dated 9 July 2025. It is not evidence for an EGP 250,000 VAT limit. The Minister may change the statutory limit by decision: any claimed different instrument must be identified before applying it. [Decision](https://eta.gov.eg/sites/default/files/2025-07/karar-281-2025-e.reciept-phase8-wave2.pdf)

Under UTPL art. 25, registration is due within 30 days from starting activity or becoming subject to VAT, as applicable. If no application is made, ETA registers on available information and notifies within 5 working days, without removing criminal liability. Below-limit persons must register on ETA's electronic system; the ministerially set annual fee is capped at EGP 500 and stops on reaching the limit. Notify registration-data changes within 30 days; heirs notify death within 60 days (art. 28). [UTPL](https://eta.gov.eg/sites/default/files/2024-03/law_no.206-2020.pdf)

Schedule-item registration, non-resident simplified registration, legal persons receiving imported services, deregistration and the practical treatment of the statutory year test in a particular registration dispute: Check this point with one of our partner accountants.

### Small projects under Law 6/2025

Quarterly VAT filing requires actual applicability of the regime and an existing VAT filing obligation. Ordinary request-based entry covers annual turnover up to EGP 20 million, including professions, registered or unregistered when the law commenced. Conditions include timely statutory returns, joining electronic systems according to mandatory phases, and issuing the required invoices/receipts. Professional consultancy earning at least 90% of annual turnover from one or two persons is excluded, subject to an activity exception made by the Minister. Improper entry, including fragmentation without economic justification, is excluded; ETA bears the burden of proof. Withdrawal is prohibited before five years starting the day after the request. Continuation after turnover growth and any special transition or claimed ministerial exception: Check this point with one of our partner accountants. [Law 6 arts. 1, 3-5, 12](https://eta.gov.eg/sites/default/files/2025-02/law_no.6.of_.2025.pdf)

### State entities: Law 159/2023

From 26 July 2023, exemptions granted to State entities by laws, regulations or decisions are removed for their economic/investment activities, subject to the exceptions below. Those activities follow their governing tax laws; State ownership alone does not establish a VAT rate. Decree 242/2024 expressly includes VAT. State entities include sovereign and local-administration units, national/service/economic authorities and special-budget bodies, plus their directly or indirectly owned or participated entities/companies, whatever the ownership percentage, legal form, activity or use of proceeds. Economic/investment activity includes producing/selling goods, providing services or exploitation rights ordinarily undertaken by private-sector or natural/legal investors. [Law 159 art. 1](https://eta.gov.eg/sites/default/files/2024-12/law_no._159_for_2023.pdf), [Decree 242 arts. 1, 3](https://media.mof.gov.eg/mof-prd/qrar_ryys_alwzrae_rqm_242_lsnt_2024_06283d9646.pdf)

Preserved exemptions concern operative international agreements for their duration; military works/tasks, defence and national security; and basic public utilities to be identified by Cabinet decision. Pre-commencement contracts retain their old legal treatment until fully performed. A renewal or increase in work beyond the contractually stipulated percentage is a new contract. Mixed exempt/taxable activities require independent accounts and payment of the taxes/fees due. [Law 159 arts. 1, 2, 4](https://eta.gov.eg/sites/default/files/2024-12/law_no._159_for_2023.pdf), [Decree 242 arts. 2, 4, 6](https://media.mof.gov.eg/mof-prd/qrar_ryys_alwzrae_rqm_242_lsnt_2024_06283d9646.pdf)

Identification of protected utilities, special-law entities including the social-insurance body, the particular exemption inventory, a disputed contract, or any claimed later narrowing/widening of Law 159: Check this point with one of our partner accountants.

## Rates, bands and thresholds

| Item | Figure | Conditions for 2026 | Official URL |
|---|---|---|---|
| General VAT | 14% | General rate; classify the supply before using it | https://eta.gov.eg/sites/default/files/2026-08/law.no_.149.of_.2026.pdf |
| Machinery, equipment and medical devices | 5% | Used to produce goods or provide services; buses and passenger cars excluded; devices used for medical purposes count as medical devices | https://eta.gov.eg/sites/default/files/2026-08/law.no_.149.of_.2026.pdf |
| Exports | 0% | Only on meeting the Regulations' export conditions. Specific goods/service evidence, foreign-payment requirements and incomplete documents: Check this point with one of our partner accountants. | https://eta.gov.eg/sites/default/files/2024-03/vat-law_no.67-2016.pdf |
| Registration limit | EGP 500,000 | Taxable plus exempt sales; statutory timing and exceptions above; amount written in words on the page | https://eta.gov.eg/sites/default/files/2024-03/vat-law_no.67-2016.pdf |
| Credit-balance refund age, from 29 July 2026 | More than 4 consecutive tax periods | Law 6/2025 projects instead: more than 3 months. This is one refund ground, not approval of a refund claim | https://eta.gov.eg/sites/default/files/2026-08/law.no_.149.of_.2026.pdf |
| Natural gas Schedule tax, from 29 July 2026 | EGP 20 per 1,000 cubic feet | New Schedule I item 17; do not substitute the general VAT rate | https://eta.gov.eg/sites/default/files/2026-08/law.no_.149.of_.2026.pdf |

The Law 149/2026 changes apply from 29 July 2026, the day after Gazette publication. Earlier-period rates/credit-refund timing: Check this point with one of our partner accountants.

### Exempt list changes from 29 July 2026

Law 149 art. 2 replaces these items. [Official text](https://eta.gov.eg/sites/default/files/2026-08/law.no_.149.of_.2026.pdf)

| Item | Scope | Official URL |
|---|---|---|
| 19 | Butane gas only | https://eta.gov.eg/sites/default/files/2026-08/law.no_.149.of_.2026.pdf |
| 20 | Natural materials, including mine and quarry products in their natural state, except crude oil and natural gas | https://eta.gov.eg/sites/default/files/2026-08/law.no_.149.of_.2026.pdf |
| 28 | Sale/rent of vacant and agricultural land, buildings and residential units, and sale/rent of non-residential buildings/units; excludes rent of premises serving as an independent seat of an activity, even commercial/customer-facing. Premises for religious, charitable, social, educational and health activities remain excepted from that exclusion, as do activities designated by ministerial decision for public-interest social necessities | https://eta.gov.eg/sites/default/files/2026-08/law.no_.149.of_.2026.pdf |
| 32 | Wheelchairs and their separate parts; artificial body parts and parts; hearing aids and parts; worn/carried/implanted devices compensating for deficiency/disability and production inputs; dialysis equipment, parts, supplies including artificial-kidney filters and production inputs; infant incubators; serums, vaccines, blood/derivatives, blood-collection bags and family-planning means | https://eta.gov.eg/sites/default/files/2026-08/law.no_.149.of_.2026.pdf |
| 35 | Postal savings, banking and financial services provided by the National Postal Authority | https://eta.gov.eg/sites/default/files/2026-08/law.no_.149.of_.2026.pdf |
| 36 | Non-bank financial services subject to FRA or Central Bank supervision | https://eta.gov.eg/sites/default/files/2026-08/law.no_.149.of_.2026.pdf |

## Classification requiring an individual check

For each row, identify the precise supply, date and statutory item before calculating:

| Topic | Action |
|---|---|
| Machinery parts/spares; industrial machinery suspension, extension, exemption and later disposal | Check this point with one of our partner accountants. |
| Schedule-only versus Schedule-plus-VAT treatment and the special machinery-parts credit/settlement; tobacco, alcohol, fuels, vehicles and mobile telecom | Check this point with one of our partner accountants. |
| Crude oil; shop goodwill; professional/consulting services versus craftsmen; advertising including public-interest adverts; news-agency services; contracting/construction and contracts straddling the change | Check this point with one of our partner accountants. |
| Gypsum, soap/detergents, edible oils/fats, crackers/confectionery, processed potatoes, fertilisers/pesticides, media/film production and air-conditioned inter-governorate transport | Check this point with one of our partner accountants. |
| Dairy/infant food, eggs, tea/sugar/coffee, mill products/bread, meat/fish/produce, water/bottled water, electricity, newsprint/books/newspapers | Check this point with one of our partner accountants. |
| Bank operations/currency exchange, insurance/reinsurance, education/training/research, health/cosmetic/slimming services, medicines, transport/fare types and Suez Canal services | Check this point with one of our partner accountants. |
| Named banks, payment gateways/wallets, ride-hailing, courier/post, hospitals, utilities, retail/office/electronics, cloud/software/fintech, advertising and recruitment suppliers; do not classify by the supplier's name or bank narrative alone | Check this point with one of our partner accountants. |

## The base

A sale is triggered by the earliest of invoice issue, delivery/service performance, or payment of all or part of the price. Personal consumption or special use is treated as a sale. The general value is the amount actually paid or payable; it includes amounts charged to the buyer and incidental charges such as commission, packing, handling, transport and insurance. [Law 67 arts. 1, 5, 10(1)-(2)](https://eta.gov.eg/sites/default/files/2024-03/vat-law_no.67-2016.pdf)

Related-party/arm's-length and ownership tests, barter, instalment interest, Schedule-inclusive bases, customs valuation, precious-metal workmanship, used goods and the claimed reduced used-goods base: Check this point with one of our partner accountants.

**Input credit.** A registered person deducts eligible VAT borne on inputs against tax on sales, subject to the statutory and regulatory conditions. Unused eligible credit carries forward. Hold the tax invoice; imported-purchase evidence includes the customs-procedures certificate and customs payment receipt. Schedule tax and input tax already included in cost are excluded from ordinary credit, subject to any specific statutory exception. Do not assume an unnamed e-receipt is a purchase-credit document: obtain the supplier's e-invoice. Simplified non-resident cases and any special credit entitlement: Check this point with one of our partner accountants. [Law 67 art. 22](https://eta.gov.eg/sites/default/files/2024-03/vat-law_no.67-2016.pdf), [Regulations arts. 26-28](https://eta.gov.eg/sites/default/files/2024-03/vat-law_no.66-2017.pdf), [ETA receipt FAQ](https://eta.gov.eg/sites/default/files/2024-02/ERECEIPT-FAQ-V24-31-1-2024.pdf)

**Mixed sales**, Regulations art. 27:
1. Inputs used solely for taxable sales: deduct the eligible tax, whether the sale occurs in that period or later.
2. Inputs used solely for exempt or Schedule-only sales: no ordinary deduction.
3. Shared inputs: deduct according to taxable sales divided by total sales.
4. Reverse previously deducted tax on exempt/Schedule-only inputs through an addition notice. For sales bearing both VAT and Schedule tax, the input deduction is from VAT, not Schedule tax, under the same controls.

Opening-stock statements, the amended indirect-input definition, capital/vehicle/entertainment credit, continuous services/consultant certificates and special timing: Check this point with one of our partner accountants.

**Invoice working check.** Obtain serial number/date, seller name/address/registration, buyer name/address/registration if any, goods/service details, value, VAT or Schedule rate/amount and total, plus any further prescribed data. Electronic mandate, document type and issuance rules must follow the taxpayer's phase; see [Egypt bookkeeping](eg-bookkeeping.md). [UTPL art. 37](https://eta.gov.eg/sites/default/files/2024-03/law_no.206-2020.pdf)

## Deadlines and filing

| Duty | Timing | Official URL |
|---|---|---|
| Ordinary monthly VAT/Schedule return | During the following month; nil returns remain required where no taxable sales/services occurred | https://eta.gov.eg/sites/default/files/2024-03/law_no.206-2020.pdf |
| Established Law 6/2025 VAT filer | Every 3 months, during the following month, with payment | https://eta.gov.eg/sites/default/files/2025-02/law_no.6.of_.2025.pdf |
| Registration | 30 days; see the triggering conditions above | https://eta.gov.eg/sites/default/files/2024-03/law_no.206-2020.pdf |
| Registration-data changes; death | 30 days from change; heirs within 60 days from death | https://eta.gov.eg/sites/default/files/2024-03/law_no.206-2020.pdf |
| Ordinary UTPL records | 5 years following the tax period for which the return is submitted | https://eta.gov.eg/sites/default/files/2024-03/law_no.206-2020.pdf |

UTPL art. 31 permits ETA's authorised official to approve month-of-transaction filing for an exporter, importer or service provider acting once or twice in the year, on the provision's terms; it is not automatic. Law 6 art. 13 substitutes prescribed simplified records for ordinary UTPL records. Its specific retention/application question: Check this point with one of our partner accountants.

Portal screens, Form 10/10 bis/111 mapping and boxes, sales/purchase Excel field codes, upload-volume cutoffs, nil/amended forms, imported-service double entries, first-return carryforward, submission reference/PDF dates, payment-claim sequencing, returned-goods/amendment-period choices and holiday adjustments: Check this point with one of our partner accountants.

Refund eligibility/procedure, tourist refunds, required accountant certificates/exceptions, refund-payment deadline/interest, assessment limitation periods and evasion extension, objections/internal committees/court appeal, dispute settlements and historical transitional claims: Check this point with one of our partner accountants.

## Penalties and interest

UTPL art. 45 bis, added by Law 7/2025, caps delay charge or additional tax at 100% of the principal tax on which it arises. [Official law](https://eta.gov.eg/sites/default/files/2025-02/law_no.7.of_.2025.pdf)

The applicable additional-tax rate, commencement and any excluded period, late/incorrect return fines, repeat-offence rules, other VAT breaches, evasion/registration offences, non-resident access restrictions, offence settlements and the case-specific cap calculation: Check this point with one of our partner accountants.

## Cross-border points

Imported goods/customs clearance and foreign-supplier collection, imported services/business-use distinctions, government and other-body direct payments, non-resident simplified suppliers/representatives/credit/refunds, exports, free zones/free cities/free markets/SEZ, transit goods/services and simplified agricultural regimes: Check this point with one of our partner accountants.

## Two worked examples that recompute

These are conditional arithmetic for one period, using the original case inputs. Establish registration, classifications, documentary eligibility and any carried credit separately before treating an amount as a return liability.

**Example 1. Mixed seller.** A Cairo firm sells EGP 3,000,000 taxable and EGP 1,000,000 exempt. Direct taxable inputs bear EGP 140,000 VAT, and shared overheads bear EGP 56,000. Assuming the taxable sales bear 14% and those input amounts qualify, output is EGP 420,000. The taxable share is 75%, so shared credit is EGP 42,000 and the current-period difference is EGP 238,000, before any other adjustments or carried credit.

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

**Example 2. Voluntary registration.** Annual sales are EGP 400,000; net purchases EGP 250,000 carry 14% VAT. Assume ordinary below-limit trading, no compulsory-registration exception, all purchases creditable if registered, and the same underlying goods/costs in each comparison. Input VAT is EGP 35,000. With an unchanged net B2B selling price, output VAT is EGP 56,000 and the current output less input is EGP 21,000; recovering the input tax improves the trader's margin by EGP 35,000 before compliance costs. A business customer can deduct only if it independently meets the credit conditions. With consumers paying a fixed EGP 400,000 total, net sales are EGP 350,877.19 and output VAT EGP 49,122.81. The trader's margin falls by EGP 14,122.81 against the unregistered case, before compliance costs. No automatic eligibility or universal commercial advantage is claimed.

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

**Earlier Example 1 retained: IT consultancy receipt.** The Cairo IT consultant's CIB credit transfer dated 15 April 2025 described TECH SOLUTIONS CO, invoice INV-2025-041, IT CONSULTING SERVICES: EGP 570,000 received and balance EGP 2,570,000. The repeated NBE format used INV-041 for the same EGP 570,000 date/receipt. If independently established as a 14%-inclusive sale, net is EGP 500,000 and tax EGP 70,000. The old Section A mapping and automatic classification of consultancy at that rate are withdrawn. Check this point with one of our partner accountants.

**Earlier Example 2 retained: SaaS export receipt.** The Egyptian software firm's NBE foreign-currency credit dated 20 April 2025 described BRITISH TECH LTD UK, SaaS subscription April 2025: EGP 1,250,000 (GBP 28,000). Preserve both currency inputs; no exchange rate has been established here. If the service independently qualifies for zero-rating, EGP 1,250,000 × 0% = EGP 0; a UK customer and foreign payment alone do not establish qualification. The old Section C mapping is withdrawn. Check this point with one of our partner accountants.

```oa-check
name: Earlier receipts, conditional arithmetic only
inputs:
  domestic_gross: 570000
  export_egp: 1250000
steps:
  - domestic_net: domestic_gross / 1.14
  - domestic_tax: domestic_gross - domestic_net
  - export_tax: export_egp * 0
expected:
  domestic_net: 500000.00
  domestic_tax: 70000.00
  export_tax: 0.00
```

## Ask the client first

Use records already available before requesting: period and transaction dates; annual taxable/exempt sales and financial year; registration/mandate documents; Law 6 request and continuing conditions; supply descriptions/classifications; importer/exporter/agent/non-resident status; foreign services and business use; changed machinery/rent/construction/gas/product categories; invoices/customs documents; old credit amounts/age; State ownership, exemptions and contract dates.

Keep a working paper of date, party, registration number, invoice reference, net, rate, tax, in/out and queries, with sales, purchases, customs, foreign-services and summary tabs. Reconcile output less eligible input and prior carried credit, without inferring either from bank totals. Seek missing records; do not turn an unknown rate, export condition, business use or invoice status into a final tax treatment.

Optional internal review prompts retain the original thresholds: one transaction above EGP 500,000; uncertain-treatment effect above EGP 70,000; one party above 40% of sales or purchases; more than four unresolved treatments; net position above EGP 1,000,000. These are working-paper prompts, not legal thresholds or permission to file an unresolved return.

## Sources

| Official source and operative scope | URL | Read on |
|---|---|---|
| Law 67/2016 arts. 1-5, 10, 16, 18, 22; exact operative wording recovered from selected page images; art. 16 repealed paragraphs excluded using UTPL issuing art. 4 | https://eta.gov.eg/sites/default/files/2024-03/vat-law_no.67-2016.pdf | 2026-11-26 |
| Law 149/2026 art. 1 rate/refund changes, art. 2 exempt list, art. 3 gas and art. 5 commencement; exact wording recovered from page images | https://eta.gov.eg/sites/default/files/2026-08/law.no_.149.of_.2026.pdf | 2026-11-26 |
| Regulations 66/2017 arts. 26-28, deduction evidence and mixed supplies; selected page images, not a claim of a consolidated re-read | https://eta.gov.eg/sites/default/files/2024-03/vat-law_no.66-2017.pdf | 2026-11-26 |
| UTPL issuing art. 4 and arts. 25, 28, 31; selected images recovered; arts. 37-38 invoice/retention reads reused from completed Egypt bookkeeping proof | https://eta.gov.eg/sites/default/files/2024-03/law_no.206-2020.pdf | 2026-11-26 |
| Law 6/2025 arts. 1, 3-5, 12-13; exact operative reads reused from completed Egypt SME/bookkeeping proof | https://eta.gov.eg/sites/default/files/2025-02/law_no.6.of_.2025.pdf | 2026-11-26 |
| Law 159/2023 arts. 1-2, 4; Decree 242/2024 arts. 1-4, 6; exact operative reads reused from completed Egypt corporate/stamp proof | https://eta.gov.eg/sites/default/files/2024-12/law_no._159_for_2023.pdf ; https://media.mof.gov.eg/mof-prd/qrar_ryys_alwzrae_rqm_242_lsnt_2024_06283d9646.pdf | 2026-11-26 |
| Decision 281/2025, operative e-receipt mandate and signature; page image | https://eta.gov.eg/sites/default/files/2025-07/karar-281-2025-e.reciept-phase8-wave2.pdf | 2026-11-26 |
| Law 7/2025 art. 1 inserting UTPL art. 45 bis; exact read reused from completed Egypt stamp proof | https://eta.gov.eg/sites/default/files/2025-02/law_no.7.of_.2025.pdf | 2026-11-26 |
| ETA e-receipt FAQ, unnamed-buyer purchase-credit question; exact read reused from completed Egypt bookkeeping proof | https://eta.gov.eg/sites/default/files/2024-02/ERECEIPT-FAQ-V24-31-1-2024.pdf | 2026-11-26 |

Not yet confirmed: no unverified rule is retained for use. The individual applications identified above use explicit partner-accountant referrals.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.
