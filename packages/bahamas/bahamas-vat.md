---
name: bahamas-vat
description: >
  Bahamas value added tax (VAT) for 2026. Covers who must register (taxable
  activity over BSD 100,000 in a past or future 12 months), the 10% standard
  rate, the 5% reduced rate on listed medical goods, the exemption from 1 April
  2026 for listed unprepared food sold by a food store, zero rating, VAT on
  conveyances of real property (Third Schedule bands, first home cap raised to
  BSD 600,000 from 1 July 2026), input VAT, refunds, VAT withholding by
  government entities, return periods and the 21-day filing rule, and the
  late filing and late payment fines. Trigger on Bahamas VAT, DIR VAT return,
  vat.revenue.gov.bs, food store VAT exemption, provisional VAT invoice,
  Bahamas VAT registration. The Bahamas has no income tax. Built from the VAT
  Act and the Department of Inland Revenue; not reviewed by an accountant.
version: 3.0
jurisdiction: BS
tax_year: 2026
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
category: international
tier: 2
domain: vat-gst
type: situation-rules
depends_on:
  - vat-workflow-base
---

# Bahamas VAT

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

Tax year: calendar 2026. Authority: Department of Inland Revenue (DIR), online at vat.revenue.gov.bs. Currency: Bahamian dollar (BSD), at par with the US dollar. The Bahamas has no income tax, so VAT is the main tax most businesses deal with. Load `vat-workflow-base` for the general bank-statement method; this skill supplies the Bahamas rules.

## Who this applies to

- **Must register:** a person whose taxable activity in the past 12 months, or expected in the next 12 months, exceeds BSD 100,000. Apply within 14 days of meeting the test (DIR FAQ). Section 21 of the VAT Act sets the BSD 100,000 threshold.
- **May register:** a business below the threshold can apply voluntarily; it then charges VAT and can recover input VAT (DIR FAQ, Q3 and Q4).
- **Business licence first:** section 22A of the VAT Act ties VAT registration to holding a business licence (see `bs-company-formation`).
- **Cancellation:** DIR uses BSD 80,000 a year as its administrative de-registration threshold; taxable sales must have fallen below the threshold in the past 12 months and be expected to stay below it in the next 12 (DIR FAQ).
- **Out of scope here:** Grand Bahama Port Area (Hawksbill Creek Agreement) licensees, investment funds, cruise lines and private islands, the condo-hotel tax and the Global Blue VAT-free shopping scheme. Refer (see the refusal list below).

## Rates, bands and thresholds

| Item | 2026 figure | Conditions | Source |
|---|---|---|---|
| Standard rate | 10% | Any taxable supply or import not zero rated, reduced or exempt (s. 6(1)(c)) | VAT (Amendment) Act 2025, s. 3 replacing s. 6(1): https://inlandrevenue.finance.gov.bs/wp-content/uploads/2025/07/VALUE-ADDED-TAX-AMENDMENT-ACT-2025.pdf |
| Zero rate | 0% | Supplies and imports in the First Schedule, for example exported goods (s. 6(1)(a)) | same |
| Reduced rate | 5% | Goods listed in the Fourth Schedule; from 1 April 2026 the "sold unprepared in a food store" condition is deleted and the list is the medical goods list (vaccines, insulin, other medicaments by tariff code) | VAT (Amendment) Act 2026, ss. 2 and 4, in force 1 April 2026: https://laws.bahamas.gov.bs/cms/images/LEGISLATION/AMENDING/2026/2026-0004A/2026-0004A.pdf |
| Medical goods at 5% | From 1 September 2025 | Fourth Schedule Part II inserted (now Part I) | VAT (Amendment) (No. 2) Act 2025, ss. 1(3) and 22: https://inlandrevenue.finance.gov.bs/wp-content/uploads/2025/07/VALUE-ADDED-TAX-AMENDMENT-NO.2-ACT-2025-.pdf |
| Sweets, chewing gum, sodas | 10% | Moved from 5% back to 10% from 1 July 2025 (tariff 1704.1000, 1704.9010, 1704.9090, 2202.10) | same |
| Unprepared food sold by a food store | Exempt | From 1 April 2026; the goods listed in new Second Schedule Part III (fresh meat and similar by tariff heading), wholesale or retail, sold unprepared by a food store, and their import by a food store | VAT (Amendment) Act 2026, s. 3: https://laws.bahamas.gov.bs/cms/images/LEGISLATION/AMENDING/2026/2026-0004A/2026-0004A.pdf |
| "Food store" | At least 10% of prior year business licence turnover from unprepared food for human consumption (new business: 10% of estimated turnover), or a licensed pharmacy, or as the Comptroller prescribes | Definition in s. 2 | VAT (Amendment) (No. 2) Act 2025, s. 2: https://inlandrevenue.finance.gov.bs/wp-content/uploads/2025/07/VALUE-ADDED-TAX-AMENDMENT-NO.2-ACT-2025-.pdf |
| Mandatory registration threshold | BSD 100,000 | Taxable activity in past or next 12 months | VAT FAQs, Q1: https://inlandrevenue.finance.gov.bs/value-added-tax/faqs/ |
| Time to apply | 14 days | From meeting the test | same |
| De-registration threshold | BSD 80,000 a year | DIR administrative figure | same |
| Return period, turnover over BSD 5 million | Monthly | | VAT FAQs, Q22: https://inlandrevenue.finance.gov.bs/value-added-tax/faqs/ |
| Return period, turnover under BSD 5 million | Quarterly | May ask the Comptroller in writing to file monthly | same |
| Filing and payment deadline | 21 days after the end of each tax period | Online; an extension to file does not extend payment | same |
| Minimum refund claim | Over BSD 500 | Monthly filers carry an excess credit forward one more period first; quarterly filers and those with zero rated supplies over 50% of total supplies in the period may claim in the period | VAT FAQs, input VAT answer: https://inlandrevenue.finance.gov.bs/value-added-tax/faqs/ |
| Record keeping | 5 years | In English | VAT FAQs, Q19: https://inlandrevenue.finance.gov.bs/value-added-tax/faqs/ |
| Late or missing return | Greater of BSD 100 or 2% of the tax payable | Automatic, strict liability (s. 47A(3)(a)) | VAT Act reprint 1 July 2024, s. 47A: https://inlandrevenue.finance.gov.bs/wp-content/uploads/2024/11/Value-Added-Tax-Act.pdf |
| Late or non-payment | 10% of the tax owed | s. 47A(3)(b) | same |
| VAT withholding by appointed agents | 100% of the VAT on standard rated payments above BSD 9,999.99 | Agents named by DIR (Public Treasury, Ministry of Works and Utilities, Ministry of Education, Ministry of the Public Service) | DIR, VAT withholding: https://inlandrevenue.finance.gov.bs/vat-withholding/ |
| Government contracts | Paying government entity is the withholding agent for the full VAT | New s. 23A(11) and (12), from 1 July 2026 | VAT (Amendment) (No. 2) Act 2026, s. 2: https://laws.bahamas.gov.bs/cms/images/LEGISLATION/AMENDING/2026/2026-0019A/2026-0019A.pdf |
| Non-profit organisation refunds | May claim input VAT it incurred (not a donor) for taxable supplies, core activities or its premises | New s. 56(7A) and (7B), from 1 July 2026 | same |
| Real property to a Bahamian company or other Bahamian entity | 2.5% where the value does not exceed BSD 100,000; 10% where it exceeds BSD 100,000 | Third Schedule item (1) | VAT Act reprint 1 July 2024, Third Schedule: https://inlandrevenue.finance.gov.bs/wp-content/uploads/2024/11/Value-Added-Tax-Act.pdf |
| Real property to a Bahamian individual (or Bahamian property-holding company not conducting business) | 2.5% to BSD 100,000; 4% over 100,000 to 300,000; 6% over 300,000 to 500,000; 8% over 500,000 to 700,000; 9% over 700,000 to 1,000,000; 10% over 1,000,000 | Third Schedule item (2), subject to item (3) | same |
| First home bought by a Bahamian citizen | 4% where the value exceeds BSD 300,000 but not BSD 600,000 | Item (3); the upper figure rose from BSD 500,000 on 1 July 2026 | VAT (Amendment) (No. 2) Act 2026, s. 5: https://laws.bahamas.gov.bs/cms/images/LEGISLATION/AMENDING/2026/2026-0019A/2026-0019A.pdf; VAT Act reprint, Third Schedule (the BSD 300,000 lower figure): https://inlandrevenue.finance.gov.bs/wp-content/uploads/2024/11/Value-Added-Tax-Act.pdf |
| Real property to a foreign person | 10% | Third Schedule item (3A) | VAT Act reprint 1 July 2024, Third Schedule: https://inlandrevenue.finance.gov.bs/wp-content/uploads/2024/11/Value-Added-Tax-Act.pdf |
| Long-term lease or its transfer | 2.5% to BSD 100,000; 10% above | Third Schedule item (4) | same |

## The base

### What is taxed

VAT applies to almost all goods and services imported, bought and sold for use in The Bahamas (DIR, About VAT). Tax the value of the supply at the rate in the table. Supplies of real property that are not zero rated are taxed at the Third Schedule rates on the conveyance, lease or transfer; the parties must obtain a Provisional VAT Invoice from DIR before the conveyance (Guidance Note 20, July 2025). A person who pays out funds for a prospective purchase without checking that a Provisional VAT Invoice was obtained can be liable for a penalty equal to the unpaid VAT assessed (Conveyancing and Law of Property Act s. 40(6), as quoted in that note).

### Input VAT

A registrant may claim input VAT on everything that can be allocated to making taxable supplies (DIR FAQ). VAT on purchases that go into exempt supplies is not claimable. Since 1 April 2026 a food store's sales of the listed unprepared food are exempt, not zero rated or 5%, so the VAT on buying that food is no longer claimable and its imports are exempt instead.

### Exempt and zero rated

- **Exempt from 1 April 2026:** listed unprepared food sold by a food store (Second Schedule Part I item 19, Part II item 10, Part III list).
- **Exempt, Second Schedule:** other items as listed in the Act (financial services, residential rent and others; read the Schedule for the item before relying on it). The transshipment items 16 and 16A as replaced by the 2026 No. 2 Act start on a date the Minister appoints.
- **Zero rated, First Schedule:** exported goods where the registrant enters them for export under the Customs Management Act and they leave The Bahamas; goods not situated in The Bahamas at the time of supply; first-home and inter vivos transfers that DIR approves for zero rating.

### Bank-statement pattern library (kept from the previous version)

Use these as a pre-classifier on bank lines; confirm against invoices.

| Pattern | Treatment | Notes |
|---|---|---|
| CIBC FIRSTCARIBBEAN, RBC BAHAMAS, SCOTIABANK, COMMONWEALTH BANK, FIDELITY BANK (charges) | Exclude | Bank charges treated as exempt financial services |
| INTEREST, LOAN, REPAYMENT | Exclude | Out of scope |
| DIR, DEPT INLAND REVENUE | Exclude | Tax payment, not a purchase |
| CUSTOMS, BAHAMAS CUSTOMS | Exclude the duty; import VAT on the entry is input VAT if for taxable supplies | Check the customs entry |
| BUSINESS LICENCE, BL FEE | Exclude | Government tax |
| NIB, NATIONAL INSURANCE | Exclude | Social contribution |
| BPL (electricity), WSC (water), BTC, ALIV (telecoms) | Domestic purchase at 10% | Keep the VAT invoice |
| BAHAMAS FIRST, COLINA, J.S. JOHNSON, SUMMIT INSURANCE | Exclude | Insurance |
| GOOGLE, MICROSOFT, META, AWS, ZOOM, SLACK, CANVA | Imported service: check whether the supplier is registered and charges VAT | Old "self-assess 10%" rule not confirmed, see Not yet confirmed |
| HOTEL, RESORT, ATLANTIS (sales) | Domestic output at 10% | Hotel and vacation rentals must register (DIR vacation rental page) |
| BOOKING.COM, EXPEDIA, AIRBNB | Platform fee: verify the entity | |
| SALARY, WAGES, DIVIDEND, OWN TRANSFER | Exclude | Outside VAT |
| CASH WITHDRAWAL | Ask; default exclude | |

### Conservative defaults

| Unknown | Default |
|---|---|
| Rate on a sale | 10% |
| VAT status of a purchase | Not deductible until a valid VAT invoice is seen |
| Counterparty location | Domestic |
| Food sold by a retailer | 10% unless the seller is a food store, the item is in Part III and it is sold unprepared |
| Medical item | 10% unless its tariff code is in the Fourth Schedule list |

## Deadlines and filing

1. Register online at vat.revenue.gov.bs within 14 days of crossing BSD 100,000 (DIR "Applying for VAT registration"; the Bahamas VAT Guide to Registration has the steps). DIR emails a reason within 21 days if an application is refused.
2. Display the VAT certificate, show VAT-inclusive prices at retail, issue valid VAT invoices and receipts (DIR FAQ).
3. File each return online within 21 days of the period end, monthly if turnover is over BSD 5 million, otherwise quarterly. Pay by the same date.
4. Claim refunds over BSD 500 as described in the table; a claim may be audited.

## Penalties and interest

- Late or missing return: the greater of BSD 100 or 2% of the tax payable (s. 47A).
- Late or non-payment: 10% of the tax owed (s. 47A).
- Criminal fines (DIR fines table): failure to apply for registration, up to BSD 100,000 or 12 months; charging VAT while unregistered, up to BSD 50,000 or two years; an unregistered person issuing a VAT invoice, up to BSD 250,000 or 12 months; not showing VAT-inclusive prices or not stating VAT separately on an invoice, up to BSD 100,000 or 12 months; not displaying the certificate, up to BSD 50,000 or 12 months.

## Cross-border points

- Exports of goods are zero rated when the export conditions are met.
- Imports: VAT is charged on import (taxable importation, s. 6(1)); a food store's import of Part III food is exempt from 1 April 2026.
- Grand Bahama Port Area licensees, cruise lines and private islands have their own DIR guidance: refer.
- No income tax applies to the profit on any of these supplies; see `bs-corporate-income-tax`.

### When to refuse or refer

- R-BS-1, Freeport: client operates in the Grand Bahama Port Area under the Hawksbill Creek Agreement. "Freeport operations have special VAT provisions. Please escalate."
- R-BS-2, investment funds: "Investment fund VAT treatment needs specialist analysis. Please escalate."
- VAT refund claims involving an audit, and any real property transaction where the value band method (whole value or slice) decides the figure: refer to a Bahamian practitioner.

## Two worked examples that recompute

### Food store quarter after 1 April 2026

A food store files quarterly (turnover under BSD 5 million). In the July to September 2026 quarter it sells BSD 40,000 of standard rated goods (net), BSD 10,000 of Fourth Schedule medicines at 5% (net) and BSD 30,000 of Part III unprepared food (exempt). VAT on purchases that relate to its taxable sales is BSD 2,600; VAT of BSD 900 relates to buying the exempt food and is not claimable.

```oa-check
name: BS food store Q3 2026 return
inputs:
  standard_sales: 40000
  reduced_sales: 10000
  exempt_food_sales: 30000
  input_taxable: 2600
  input_exempt: 900
steps:
  - output_standard: standard_sales * 0.10
  - output_reduced: reduced_sales * 0.05
  - output_exempt: exempt_food_sales * 0
  - output_total: output_standard + output_reduced + output_exempt
  - input_claimable: input_taxable
  - net_vat: output_total - input_claimable
expected:
  output_standard: 4000
  output_reduced: 500
  output_total: 4500
  net_vat: 1900
```

Output VAT BSD 4,500, input VAT BSD 2,600, so BSD 1,900 is due by 21 October 2026. The BSD 900 on exempt food purchases is a cost.

### Decision: register voluntarily below BSD 100,000?

A consultant expects BSD 80,000 of fees a year and pays BSD 3,000 of VAT on purchases.

- **Customers are consumers and the price stays at BSD 80,000 including VAT if registered.** Registered: output VAT is 80,000 × 10/110 = BSD 7,272.73; less input 3,000 = BSD 4,272.73 paid to DIR. Not registered: the BSD 3,000 input VAT is a cost. Registration costs BSD 1,272.73 more, so stay unregistered.
- **Customers are VAT-registered businesses and VAT is added on top.** Registered: the consultant charges BSD 8,000, the customers reclaim it, and the consultant recovers BSD 3,000. Registering saves BSD 3,000.

```oa-check
name: BS voluntary registration decision, fees 80000
inputs:
  fees: 80000
  input_vat: 3000
steps:
  - output_inclusive: round(fees * 10 / 110, 2)
  - payable_registered: output_inclusive - input_vat
  - extra_cost_if_registered: payable_registered - input_vat
  - saving_b2b: input_vat
expected:
  output_inclusive: 7272.73
  payable_registered: 4272.73
  extra_cost_if_registered: 1272.73
  saving_b2b: 3000
```

## Ask the client first

1. Taxable turnover for the past 12 months and expected for the next 12 (BSD 100,000 test; BSD 5 million monthly filing test).
2. Does the business hold a business licence, and is it in the Grand Bahama Port Area?
3. What does it sell: is it a food store (10% test), does it sell Part III food unprepared, Fourth Schedule medicines, exports?
4. Is it a hotel, vacation rental, government contractor or non-profit (2026 withholding and refund rules)?
5. Any real property bought, sold or leased in the period: buyer status (Bahamian individual, Bahamian company, foreign person, first-time buyer), value, and has a Provisional VAT Invoice been obtained?
6. Credit brought forward from the last return, and the DIR TIN.

## Sources

| Source | URL | Read on |
|---|---|---|
| Value Added Tax Act reprint as at 1 July 2024: read for s. 21 registration threshold, s. 47A late filing and payment fines, First Schedule zero rating and Third Schedule real property rates | https://inlandrevenue.finance.gov.bs/wp-content/uploads/2024/11/Value-Added-Tax-Act.pdf | 2026-11-14 |
| VAT (Amendment) Act 2025: read for the replacement s. 6(1) (0%, 5%, 10%) and its 1 April 2025 start | https://inlandrevenue.finance.gov.bs/wp-content/uploads/2025/07/VALUE-ADDED-TAX-AMENDMENT-ACT-2025.pdf | 2026-11-14 |
| VAT (Amendment) (No. 2) Act 2025: read for the food store definition, sweets and sodas back to 10%, the medical goods list from 1 September 2025 | https://inlandrevenue.finance.gov.bs/wp-content/uploads/2025/07/VALUE-ADDED-TAX-AMENDMENT-NO.2-ACT-2025-.pdf | 2026-11-14 |
| VAT (Amendment) Act 2026 (No. 4 of 2026, assent 23 March 2026): read for the food exemption and the Fourth Schedule change from 1 April 2026 | https://laws.bahamas.gov.bs/cms/images/LEGISLATION/AMENDING/2026/2026-0004A/2026-0004A.pdf | 2026-11-14 |
| VAT (Amendment) (No. 2) Act 2026 (No. 19 of 2026): read for government withholding, non-profit refunds, transshipment items and the first home cap of BSD 600,000 from 1 July 2026 | https://laws.bahamas.gov.bs/cms/images/LEGISLATION/AMENDING/2026/2026-0019A/2026-0019A.pdf | 2026-11-14 |
| Bahamas legislation, Acts by year 2026: read to confirm both 2026 VAT Bills were enacted | https://laws.bahamas.gov.bs/cms/legislation/acts_only/acts-by-year.html | 2026-11-14 |
| DIR VAT FAQs: read for the threshold, 14 days, BSD 80,000 de-registration, return periods, 21-day deadline, refunds over BSD 500, five-year records | https://inlandrevenue.finance.gov.bs/value-added-tax/faqs/ | 2026-11-14 |
| DIR VAT withholding page: read for the 100% withholding above BSD 9,999.99 and the named agents | https://inlandrevenue.finance.gov.bs/vat-withholding/ | 2026-11-14 |
| DIR fines and penalties table (2015): read for the criminal fines for registration and invoicing offences | https://inlandrevenue.finance.gov.bs/wp-content/uploads/2015/10/FINES-AND-PENALTIES-TABLE.pdf | 2026-11-14 |
| DIR Guidance Note 20, Provisional VAT Invoice: read for the requirement before conveyance and the penalty for disbursing without checking | https://inlandrevenue.finance.gov.bs/wp-content/uploads/2025/08/Requirement-for-Provisional-VAT-Invoice-Guidance-Note.pdf | 2026-11-14 |
| DIR First home FAQs: read for zero rating of a Bahamian's first home and inter vivos transfers | https://inlandrevenue.finance.gov.bs/faqs-first-home/ | 2026-11-14 |

Not yet confirmed: whether each Third Schedule rate applies to the whole value or only to the slice in its band (the reprint lists rates by value band without saying); the value up to which a first home is fully zero rated (DIR says full exemption is zero rating but the page gives no figure, and the old BSD 500,000 FAQ cap predates the 2026 change); reverse charge or self-assessment on services bought from abroad (the old "self-assess 10%" rule was not found in the Act text read); the interest rate on unpaid VAT (the old "1.5% a month" was not found); the voluntary registration figure of BSD 50,000 in the old file; the old "bimonthly" and "annual" return periods; the complete Second Schedule exempt list.
