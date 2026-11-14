---
name: myanmar-ct
description: "Myanmar commercial tax (CT), the country's turnover tax in place of VAT or GST, for FY 2026-27 (1 April 2026 to 31 March 2027) under the Union Taxation Law 2026 and the Commercial Tax Law. Covers the 5% general rate on goods, imports and services, the 3% rates (hotels and tourism, gold, construction for sale), 15% on internet services, the SIM card charge, 0% on exports (8% electricity, 5% crude oil), the 50 million kyat threshold, exempt goods and services, set-off, monthly payment within 10 days, quarterly and annual returns, and fines. Also classifies bank-statement lines for a CT return. Use for Myanmar VAT, GST, sales tax or commercial tax questions."
version: 3.0
jurisdiction: MM
category: international
tax_year: 2026
tax_year_notes: "FY 2026-27, 1 April 2026 to 31 March 2027, Union Taxation Law 2026 (in force 1 April 2026)"
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: vat-gst
type: situation-rules
---

# Myanmar Commercial Tax v3.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Anyone producing and selling goods, importing, trading or providing services in Myanmar in FY 2026-27. Myanmar has no VAT or GST: it levies **commercial tax (CT)** under the Commercial Tax Law (1990, as amended), with the schedules and rates set each year by the Union Taxation Law. For FY 2026-27 that is the Union Taxation Law 2026, Chapter VI (ss 14 to 18), in force 1 April 2026. CT is administered by the Internal Revenue Department (IRD); CT on imports is collected by the Customs Department with customs duty.

**Specific goods tax** (tobacco, liquor, vehicles, fuel, gems and other listed goods, UTL 2026 Chapter V) is a separate tax and is not computed here (refusal R-MM-1).

## Rates, bands and thresholds

| Item | Amount and conditions | Tax year | Official URL |
|---|---|---|---|
| Goods produced and sold domestically, or imported | 5% of sale proceeds, or of landed value on import (including any specific goods tax) (UTL 2026 s 14(b)) | FY 2026-27 | https://www.ird.gov.mm/storage/laws/6a6b496e035ea-utl2026.pdf |
| Importing and reselling, and trading | 5% of sale proceeds (s 14(c)) | FY 2026-27 | same |
| Services and other goods not listed | 5% of receipts (s 14(e)) | FY 2026-27 | same |
| SIM cards | 20,000 kyats per SIM card sold or activated (s 14(f)(i)) | FY 2026-27 | same |
| Internet service | 15% of receipts (s 14(f)(ii)) | FY 2026-27 | same |
| Construction, repair and sale of buildings and infrastructure (long-term lease of State land, with the State or on private land) | 3% of sale proceeds (s 14(g)) | FY 2026-27 | same |
| Hotel and tourism services | 3% of receipts (s 14(h)) | FY 2026-27 | same |
| Pure gold (bars, blocks, coins) and gold jewellery | 3% of sale proceeds or landed value; CT paid on purchase or import is not set off (s 14(i)) | FY 2026-27 | same |
| Exempt goods | 46 listed goods: staple foods (rice, pulses, fresh produce, fish, meat, eggs, milk, sugar), agricultural inputs, school books and stationery, medicines and medical supplies, solar equipment, CMP raw materials and others (s 14(a)) | FY 2026-27 | same |
| Exempt services | 34 listed services: goods and public transport, air transport, education, healthcare (not fitness), life insurance, microfinance, capital market, licensed banking and money services, childcare, funeral services, EV charging and others (s 14(d)) | FY 2026-27 | same |
| Threshold | No CT unless the year's sale proceeds from domestic production, receipts from services, or trading proceeds exceed 50 million kyats (each, measured over 12 months from commencement) (s 15(b)) | FY 2026-27 | same |
| Exports of goods | 0%; CT paid on purchase or production may be set off, and refunded if larger (s 17(b)) | FY 2026-27 | same |
| Exported electricity | 8% (s 17(a)) | FY 2026-27 | same |
| Exported crude oil | 5% (s 17(a)) | FY 2026-27 | same |
| Foreign currency proceeds | CT paid in kyats at the rates above (s 16) | FY 2026-27 | same |
| Monthly payment | Within 10 days after the end of each month (Commercial Tax Law s 12(a)) | FY 2026-27 | https://www.ird.gov.mm/storage/laws/68b55a995979f-Commercial%20Tax%20Law%20English%20version.pdf |
| Quarterly return | Within one month after the end of each quarter (s 12(a)) | FY 2026-27 | same |
| Annual return | Within 3 months after the end of the year (s 13(a)) | FY 2026-27 | same |
| Annual CT return due, FY 2025-26 | 30 June 2026 | FY 2025-26 | https://www.ird.gov.mm/announcement-lists/96 |
| Late return penalty (IRD notice) | Greater of 5% of tax owing plus 1% a month (to assessment) and K 100,000 | 2026 | same |
| Commercial Tax Law fines | 10% of the tax due for each default: failure to register, to pay monthly, to send the quarterly or annual return in time, to pay assessed tax, to keep receipts (s 21) | FY 2026-27 | https://www.ird.gov.mm/storage/laws/68b55a995979f-Commercial%20Tax%20Law%20English%20version.pdf |

## The base

1. **Is the item taxable?** Check the exempt goods list (s 14(a)) and exempt services list (s 14(d)). If listed, no CT.
2. **Is the person over the threshold?** Below 50 million kyats a year of taxable proceeds or receipts, no CT, but a person who wants to set off CT, or whose proceeds are chargeable on registration, must register (s 15(b), Explanation 2). Once over the threshold, CT applies to the whole amount, not only the excess (IRD companies page).
3. **Which rate?** 5% by default; 3%, 15%, the SIM charge or the export rates where listed.
4. **Base.** Sale proceeds for domestic sales; landed value for imports (collected by Customs); receipts for services. CT is charged on top of the price.
5. **Set-off.** CT paid on purchase or production may be set off under the Commercial Tax Regulations; for exports, any excess is refundable (s 17(b)). Gold is the exception: no set-off (s 14(i)).
6. **Landlords.** Rent from land, buildings and rooms over 50 million kyats a year: 5% CT collected from the tenant and paid with challan Form (KaThaKha)-7 (IRD individual page).

### Bank-statement classification

| Pattern | Treatment | Note |
|---|---|---|
| KBZ, KANBAWZA; CB BANK; AYA BANK; YOMA BANK | Exclude bank charges and interest | Money services of licensed banks are exempt services |
| INTEREST, LOAN, REPAYMENT | Exclude | Out of scope |
| IRD, INTERNAL REVENUE; CUSTOMS; SSB | Exclude | Tax, duty and social security payments |
| YESC, ELECTRICITY SUPPLY | Purchase; check set-off eligibility | Electricity |
| MPT, OOREDOO, TELENOR, ATOM (mobile and internet) | Purchase; internet bills carry 15% CT | Telecoms |
| WAVE MONEY, KBZ PAY, OK$ | Exclude fees | Financial service |
| GOOGLE, MICROSOFT, META, AWS, ZOOM, SLACK | Flag: services from non-residents (see Cross-border points) | Not self-assessed by default |
| SALARY, WAGES; OWN TRANSFER; INTERNAL | Exclude | Outside CT |
| CASH WITHDRAWAL | Ask | Default exclude |

### Conservative defaults

| Unknown | Default |
|---|---|
| Rate on a domestic sale | 5% |
| Whether a purchase can be set off | No set-off until the regulation condition is shown |
| Counterparty location | Domestic Myanmar |
| Whether a product is a specific good | Ask; refuse if it is (R-MM-1) |

## Deadlines and filing

1. **Register** with the Township Revenue Officer (Form PaTaKha (KaThaKha)-1; the office issues (KaThaKha)-2) and give notice of commencement (Form (KaThaKha)-3). Companies register with the tax office that assesses them, after DICA approval, through e-Registration for a TIN.
2. **Pay monthly** within 10 days after each month.
3. **Quarterly return** within one month after each quarter: Form (KaThaKha)-5 for goods, (KaThaKha)-6 for services.
4. **Annual return** within 3 months after year end (30 June): Forms (KaThaKha)-11 and -12, or (KaThaKha)-11Ka for self-assessment taxpayers. For FY 2026-27, due 30 June 2027. Large and Medium Taxpayer Office taxpayers file electronically.
5. **Imports:** CT is collected by Customs with the customs duty.

## Penalties and interest

- Late annual return: greater of 5% of tax owing plus 1% a month and K 100,000 (IRD notice of 28 April 2026, which covers the annual CT return).
- Commercial Tax Law s 21: 10% of the tax due for each listed default (failure to register, late monthly payment, late quarterly or annual return, unpaid assessed tax, missing receipts).
- Where the two sources overlap, see Not yet confirmed.

## Cross-border points

- **Exports** of goods: 0% (electricity 8%, crude oil 5%), with set-off and refund of CT paid on inputs.
- **Imports** of goods: 5% on landed value (including specific goods tax), collected by Customs; goods under temporary admission or drawback are exempt but CT is repaid if they stay in Myanmar.
- **Services from non-residents:** the Union Taxation Law 2026 sets no separate rule for them in Chapter VI. The old file told users to self-assess 5% on SaaS and cloud services; no official source opened today says so, so it is removed and listed under Not yet confirmed.
- **Foreign currency proceeds** are taxed in kyats.

## Two worked examples that recompute

**Example 1. Manufacturer, domestic sales 60,000,000 kyats in the year plus 20,000,000 exported, CT paid on inputs 1,000,000.** Domestic proceeds exceed 50 million, so CT is 5% of the whole 60,000,000 = 3,000,000. Exports 0%. Assuming the inputs qualify for set-off, net CT 2,000,000.

```oa-check
name: Myanmar CT, manufacturer over the threshold with exports
inputs:
  domestic: 60000000
  exports: 20000000
  input_ct: 1000000
steps:
  - output_domestic: domestic * 0.05
  - output_exports: exports * 0
  - net_ct: output_domestic + output_exports - input_ct
expected:
  output_domestic: 3000000.00
  net_ct: 2000000.00
```

**Example 2 (decision). A guesthouse expects 48,000,000 kyats of receipts; a new tour package would add 5,000,000. Register?** At 48,000,000 it is under the 50 million threshold: CT nil. At 53,000,000 it is over, and hotel and tourism receipts carry 3% on the whole amount: 1,590,000. The extra 5,000,000 of receipts brings 1,590,000 of CT, so the package adds only 3,410,000 net unless prices rise to pass the CT on. The figure that decides is the 50 million line.

```oa-check
name: Myanmar CT threshold cliff, hotel receipts
inputs:
  base: 48000000
  extra: 5000000
steps:
  - ct_base: 0
  - total: base + extra
  - ct_total: total * 0.03
  - net_gain: extra - ct_total
expected:
  ct_total: 1590000.00
  net_gain: 3410000.00
```

## Ask the client first

1. What goods or services, and are any on the exempt lists or specific goods?
2. Expected sale proceeds or receipts in the year (over 50 million kyats?) and when the business started.
3. Domestic sales, imports, trading or exports?
4. Hotel, tourism, gold, construction for sale, internet or SIM card business (special rates)?
5. CT paid on purchases and whether it qualifies for set-off.
6. Which tax office assesses the business, and is it on self-assessment?

## When to refuse or escalate

| Code | Trigger | Message |
|---|---|---|
| R-MM-1 | Specific goods (tobacco, liquor, vehicles, fuel, gems, natural gas and other UTL 2026 Chapter V goods) | "Specific goods tax is a separate tax with price-tier rates. This skill does not compute it; please escalate." |
| R-MM-2 | Special Economic Zone (Thilawa or other) | "SEZ businesses have their own incentives. Please escalate." |
| R-MM-3 | Branch of a foreign company | "Branch operations have specific CT and income tax obligations. Please escalate." |

## Sources

| Source | What was read | URL | Read on |
|---|---|---|---|
| Union Taxation Law 2026, English (IRD), Chapter VI | Read for ss 14 to 18: exempt goods and services, 5%, 3%, 15% and SIM rates, the 50 million threshold, foreign currency, export rates and set-off | https://www.ird.gov.mm/storage/laws/6a6b496e035ea-utl2026.pdf | 2026-11-14 |
| Commercial Tax Law, English (IRD) | Read for s 11 registration, s 12 monthly payment and quarterly return, s 13 annual return, s 21 fines | https://www.ird.gov.mm/storage/laws/68b55a995979f-Commercial%20Tax%20Law%20English%20version.pdf | 2026-11-14 |
| IRD notice to file returns (28 April 2026) | Read for the annual CT return due 30 June 2026, filing methods and the late filing penalty | https://www.ird.gov.mm/announcement-lists/96 | 2026-11-14 |
| IRD, taxes: companies (Burmese) | Read for the registration and return form numbers and that CT applies to the whole amount once over 50 million | https://www.ird.gov.mm/tax-knowledge/taxes/companies | 2026-11-14 |
| IRD, taxes: individual (Burmese) | Read for landlords' 5% CT over 50 million kyats and Form (KaThaKha)-7 | https://www.ird.gov.mm/tax-knowledge/taxes/individual | 2026-11-14 |

Not yet confirmed: whether a Myanmar business must self-assess CT on services bought from non-residents (the old file said 5%; no official text read supports it); the conditions for set-off of input CT under the Commercial Tax Regulations (not opened); how the Commercial Tax Law s 21 fines of 10% interact with the Tax Administration Law penalty quoted in the IRD notice of 28 April 2026 (both are official; the Tax Administration Law text was not opened); specific goods tax rates.
