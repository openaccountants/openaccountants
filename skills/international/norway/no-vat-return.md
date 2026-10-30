---
name: no-vat-return
description: "Use this skill for Norwegian VAT (merverdiavgift, MVA) for 2026: registration, rates, deductions and the VAT return (skattemelding for merverdiavgift). It covers the NOK 50,000 registration limit (NOK 140,000 for charities, NOK 3 million for sports tickets), pre-registration, the 25% standard rate and the 15%, 12% and 11.11% reduced rates, exempt and zero-rated supplies, input VAT and the blocked items (entertainment, serving, passenger cars, staff benefits), the NOK 10,000 bank-payment rule, two-monthly and annual periods and their deadlines, imports, remote services bought from abroad, VOEC for low-value goods, corrections, enforcement fines, additional tax and interest. Norway is in the EEA but not the EU: there are no intra-community supplies. Trigger on: MVA, mva-melding, merverdiavgift, Norwegian VAT, VAT return Norway, VOEC, reverse charge Norway, import VAT Norway. Out of scope: no-income-tax, no-corporate-income-tax, no-employer-payroll, no-social-contributions, no-transfer-pricing; VAT compensation for public bodies and property adjustment are flagged only."
version: 2.1
jurisdiction: "NO"
tax_year: 2026
last_updated: 2026-10-30
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Norway: VAT (merverdiavgift) for 2026

This skill covers Norwegian value added tax (merverdiavgift, MVA) for 2026. The law is the VAT Act (merverdiavgiftsloven, lov 2009-06-19-58) and the VAT Regulation (merverdiavgiftsforskriften, FOR-2009-12-15-1540). The Storting sets the rates each year: for 2026 in the decision on VAT (Stortingsvedtak om merverdiavgift for 2026, FOR-2025-12-18-2752). Returns, deadlines and penalties are in the Tax Administration Act (skatteforvaltningsloven) and its regulation; due dates and interest in the Tax Payment Act (skattebetalingsloven). Skatteetaten administers VAT; Norwegian Customs handles imports for businesses not registered. Amounts are in Norwegian kroner (NOK).

Norway is part of the EEA but not the EU and not the EU VAT area. There are no intra-community supplies or acquisitions and no EU VAT number checks that change Norwegian treatment. Goods from an EU country are imports like goods from anywhere else.

Read [no-income-tax](no-income-tax.md) and [no-corporate-income-tax](no-corporate-income-tax.md) for income tax, [no-employer-payroll](no-employer-payroll.md) for payroll and [no-transfer-pricing](no-transfer-pricing.md) for related-party pricing. The older file norway-mva is a copy of the previous version of this skill in the older shape; use this skill instead.

## Who this applies to

- **Registration duty.** A business or public body must register in the VAT Register (Merverdiavgiftsregisteret) once its VAT-able supplies and withdrawals have exceeded NOK 50,000 in a period of twelve months. The limit is NOK 140,000 for charitable and non-profit institutions and organisations (merverdiavgiftsloven § 2-1 first paragraph). The twelve months can be any rolling period, not only a calendar year.
- **Sports tickets.** For selling the right to attend sporting events the limit is NOK 3 million, except for the two top men's football divisions and the top men's ice hockey division, which use the ordinary limit (§ 2-1 second paragraph).
- **What counts.** Only supplies within the Act count: standard, reduced and zero-rated sales and withdrawals. Supplies exempt from the Act (chapter 3) do not.
- **Pre-registration.** A business below the limit can pre-register if it has made significant purchases directly linked to later VAT-able sales, or if sales will pass the limit within three weeks of starting (§ 2-4). Significant means at least NOK 250,000 including VAT. It must look clearly likely that turnover will be well above the limit in normal operation, and pre-registration is not possible if the limit will be reached in less than four months from the application (VAT Regulation § 2-4-1).
- **Foreign businesses.** A business with no place of business or home in Norway registers through a representative. A business resident in an EEA state or the UK does not need a representative where that state exchanges information and helps collect VAT under a treaty with Norway (§ 2-1 sixth paragraph). A foreign seller of low-value goods or remote services to consumers can use the simplified VOEC scheme instead (§ 14-4).
- **Out of scope here.** Joint registration, VAT compensation for municipalities and other public bodies, the adjustment rules for capital goods and property (chapter 9), VAT on property letting by voluntary registration, petroleum and Svalbard (outside the VAT area). They are flagged, not computed.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Standard rate | 25% | 2026 | Stortingsvedtak om merverdiavgift 2026 § 2; https://lovdata.no/dokument/STV/forskrift/2025-12-18-2752 |
| Food (næringsmidler), and water from waterworks and wastewater services | 15% | 2026 | same decision § 3; merverdiavgiftsloven §§ 5-2, 5-12 |
| Passenger transport, transport of vehicles on ferries, hotel rooms and holiday letting, cinema, broadcasting, museums and exhibitions, amusement parks, sporting events | 12% | 2026 | same decision § 4; merverdiavgiftsloven §§ 5-3 to 5-7, 5-9 to 5-11 |
| Wild marine resources (§ 5-8) | 11.11% | 2026 | same decision § 5; merverdiavgiftsloven § 5-8 |
| Registration limit | Over NOK 50,000 in twelve months | 2026 | merverdiavgiftsloven § 2-1 first paragraph; https://lovdata.no/lov/2009-06-19-58/§2-1 |
| Registration limit, charities and non-profits | NOK 140,000 | 2026 | § 2-1 first paragraph |
| Registration limit, sports event tickets | NOK 3 million | 2026 | § 2-1 second paragraph |
| Pre-registration: significant purchases | At least NOK 250,000 including VAT; not if the limit will be reached within four months | 2026 | merverdiavgiftsforskriften § 2-4-1; https://lovdata.no/forskrift/2009-12-15-1540/§2-4-1 |
| Bank-payment rule for input VAT | No deduction unless paid through a bank or payment provider, or the total payment is under NOK 10,000 | 2026 | merverdiavgiftsloven § 8-8 |
| Gifts and advertising items of "insignificant value" | NOK 200 or less | 2026 | merverdiavgiftsforskriften § 1-3-6 |
| Low-value goods (VOEC) | Under NOK 3,000 per item, excluding transport and insurance | 2026 | merverdiavgiftsforskriften § 1-3-8 |
| Non-registered business buying remote services | VAT due only when purchases in a quarter exceed NOK 2,000 excluding VAT | 2026 | merverdiavgiftsloven § 11-3 first paragraph |
| Mixed use, small share rules | No deduction if VAT-able sales are normally no more than 5% of total; full deduction if exempt sales are normally no more than 5% | 2026 | merverdiavgiftsloven § 8-2 third and fourth paragraphs |
| Annual period, low turnover | Calendar year if VAT-able sales and withdrawals are no more than NOK 1 million in the year, with consent | 2026 | skatteforvaltningsforskriften § 8-3-3 |
| Late-payment interest | 12% from 1 January 2026; 12.25% from 1 July 2026 | 2026 | skattebetalingsloven § 11-1; https://www.skatteetaten.no/satser/forsinkelsesrenter/ |
| Enforcement fine for a late VAT return | Half a court fee (NOK 672.50) per day, at most 50 court fees (NOK 67,250) | 2026 | Skatteetaten, Enforcement fines; skatteforvaltningsloven § 14-1 |
| Additional tax | 20% of the tax advantage; aggravated 20% or 40% more | 2026 | skatteforvaltningsloven §§ 14-5, 14-6 |

## The taxable base

**What is taxed.** VAT is charged on supplies of goods and services, on withdrawals for private or non-business use, and on imports (merverdiavgiftsloven §§ 3-1 and 11-1). The registered business charges output VAT on its sales and pays the net amount after deducting input VAT.

**Exempt supplies (chapter 3).** Some supplies are outside the Act: for example health services (§ 3-2), education (§ 3-5), financial services (§ 3-6), letting of real property (§ 3-11) and certain cultural, sports and charitable activity. No output VAT is charged, they do not count towards registration, and input VAT on costs for them is not deductible.

**Zero-rated supplies (chapter 6).** Some supplies are within the Act but carry no output VAT: for example newspapers (§ 6-1), books (§ 6-4), exports of goods (§ 6-21) and services wholly used abroad or remote services to a buyer resident abroad (§ 6-22). They count towards registration, are reported in the return, and input VAT on costs for them is deductible. Do not post exempt and zero-rated sales to the same code.

**Food.** Food is any food or drink meant for people; medicines, tobacco, alcoholic drinks and water from waterworks are not food (§ 5-2). Food sold as part of a serving service (restaurant, café, catering) carries 25%, not 15% (§ 5-2 first paragraph). Water from waterworks has its own 15% rate (§ 5-12).

**Hotels.** Letting of hotel rooms, camping and holiday homes is 12%, and so are conference rooms let by such a business and goods or services included in the room price without a separate charge (§ 5-5).

**Input VAT.** A registered business deducts input VAT on purchases for use in the registered business (§ 8-1). Purchases used partly for other purposes give a deduction only for the share used in the registered business (§ 8-2). Input VAT must be documented with a voucher (§ 15-10 first paragraph). These are blocked even when the cost is wholly for the business (§ 8-3):

- serving (restaurant meals, catering) and hire of function rooms in connection with serving;
- art and antiques, unless the buyer trades in the same kind of goods or runs a museum-type business;
- food for, and benefits in kind to, the owner, management, employees and pensioners;
- entertainment of business contacts (representasjon);
- gifts and goods or services handed out for advertising, unless the value is insignificant (NOK 200 or less);
- building, maintaining, renting and running property that meets housing or welfare needs, including furniture and equipment. Building and maintaining a staff canteen, with its loose furniture, stays deductible.

**Passenger cars.** No deduction for input VAT on buying, running and maintaining a passenger vehicle, unless it is stock for sale, a rental car in a professional rental business or used to carry passengers for payment (§ 8-4). A passenger vehicle includes a car registered as a passenger car, a van registered as class 1, motorcycles and mopeds not mainly for goods, camper vans and small buses with up to 17 seats (VAT Regulation § 1-3-1).

**Bank-payment rule.** Input VAT is deductible only if the payment went through a bank or licensed payment provider, unless the total payment is under NOK 10,000. Several payments for the same delivery, service or contract count as one (§ 8-8).

**Purchases before registration.** After registration, a business can deduct input VAT on goods and services bought up to three years before registration, to the extent they are directly linked to its VAT-able sales and were not sold before registration. The claim must be made within three years of registration (§ 8-6). Keep the receipts.

**Imports.** The base is the customs value under the Customs Act plus customs duty and other taxes charged on import (§ 4-11). Skatteetaten describes this as the statistical value on the customs declaration plus the duties and taxes in item 47. A registered business calculates import VAT itself in its VAT return for all goods it imports, including goods it cannot deduct. A business not registered pays import VAT to Norwegian Customs or the forwarder.

## Deadlines and filing

| Period | What | Deadline | Source |
|---|---|---|---|
| Ordinary periods | Six two-month periods: Jan-Feb, Mar-Apr, May-Jun, Jul-Aug, Sep-Oct, Nov-Dec | One month and ten days after each period: 10 April, 10 June, 31 August (fixed for May-Jun), 10 October, 10 December, 10 February | skatteforvaltningsforskriften §§ 8-3-1, 8-3-10 first paragraph |
| Annual period, low turnover | Calendar year, with consent | Two months and ten days after the year: 10 March | §§ 8-3-3, 8-3-10 second paragraph |
| Primary industries (fishing, forestry, farming and related) | Calendar year | Three months and ten days after the year: 10 April | §§ 8-3-7, 8-3-10 third paragraph |
| Special return (buyers of remote services not registered; buyers of emission allowances and gold) | Quarters | One month and ten days after the quarter; 31 August for April-June | §§ 8-3-9, 8-3-10 first paragraph |
| VOEC (simplified scheme) | Quarters | 20 days after the quarter | §§ 8-3-9, 8-3-10 fourth paragraph |
| Payment | Same as the filing deadline | | skattebetalingsloven § 10-30 |
| Correction of own return | Up to three years after the filing deadline | | skatteforvaltningsloven § 9-4 |

- **Every period, even with no sales.** A registered business must file a return for every period, even with no VAT-able sales (skatteforvaltningsloven § 8-3 second paragraph). Skatteetaten imposes enforcement fines for missing returns even with no turnover.
- **Annual period.** Apply so the application reaches Skatteetaten by 1 February to apply from that year. The business must have been registered with ordinary periods for at least 12 months and have kept its filing and payment duties (§§ 8-3-3, 8-3-4). A business that sees turnover will pass NOK 1 million must tell Skatteetaten at once (§ 8-3-6). Skatteetaten can refuse or withdraw the annual period, for at least two years, for late filing or payment or turnover over the limit; turnover at least 25% over the limit, which the business should have foreseen, is a serious breach (§ 8-3-5). A business that goes back to ordinary periods stays there for at least two years (§ 8-3-4).
- **Shorter periods.** If input VAT regularly exceeds output VAT by at least 25%, Skatteetaten can allow monthly returns; at least 50%, periods down to one week, normally for at least two years (§ 8-3-8). Repeated serious breaches can lead to monthly returns for up to 12 months (§ 8-3-2).
- **Invoicing at registration.** A business cannot charge VAT on invoices until registered. If an invoice for a sale after the limit was sent before registration, issue a credit note without VAT and a new invoice with VAT. Late registration makes interest run on the VAT that should have been paid (Skatteetaten, register for VAT).
- **Who can submit.** In Altinn, the access packages "Value added tax" and "Accountant with signing rights" can complete and submit. "Auditor in charge", "Assistant auditor" and "Accountant without signing rights" can complete but not submit. Some older roles work only until 31 December 2026 (Skatteetaten, VAT return).
- **Import dates.** Post an import by the invoice date in the accounts but report the import VAT in the return for the period of the shipping date registered by Norwegian Customs. Keep the customs declarations; temporary imports with a zero rate go in item 85 of the return (Skatteetaten, imports).
- **Records.** Sales documents may not be issued before delivery (§ 15-10 third paragraph). Keep accounting records five years (bokføringsloven § 13).

## Penalties and interest

- **Enforcement fine.** Half a court fee per day for a late VAT return, at most 50 court fees. With the 2026 court fee of NOK 1,345 that is NOK 672.50 a day and at most NOK 67,250 (Skatteetaten, enforcement fines; skatteforvaltningsforskriften § 14-1-1; skatteforvaltningsloven § 14-1).
- **Additional tax.** 20% of the VAT advantage that was or could have been gained from wrong or missing information (skatteforvaltningsloven § 14-5). Aggravated additional tax for intent or gross negligence adds 20% or 40% (§ 14-6).
- **No additional tax** where a seller failed to charge VAT on ordinary booked sales and shows the buyer had full deduction or VAT compensation; on obvious calculation or typing errors; on a voluntary correction not prompted by a control; or where it would be under NOK 1,000 (§ 14-4).
- **Late-payment interest.** From the due date to payment: 12% from 1 January 2026, 12.25% from 1 July 2026 (skattebetalingsloven § 11-1). Interest also runs on VAT increased by a change decision or the business's own correction, from the original due date (§ 11-2).
- **Reopening.** Skatteetaten can change an assessment for five years after the end of the period, ten years with aggravated additional tax (skatteforvaltningsloven § 12-6).

## Cross-border points

- **Goods from abroad, including the EU.** Imports, with a customs declaration. A registered business self-assesses import VAT in its return and deducts it under the ordinary rules. Check that the customs declaration matches the supplier and forwarder documents; ask the forwarder or Customs to correct it if not.
- **Remote services bought from abroad (reverse charge).** VAT is due on remote services bought from outside Norway when the buyer is resident in Norway and the service would be VAT-able if sold here (§ 3-30). A business or public body buyer calculates and pays the VAT (§ 11-3). A registered buyer reports it in the ordinary return and deducts it under the ordinary rules. A buyer not registered pays only when purchases in a quarter exceed NOK 2,000 excluding VAT, on the special quarterly return. A service a foreign branch buys for use by the Norwegian part of the same entity is also covered (§ 3-30 second paragraph), unless the service is wholly for use that would give a deduction, or foreign VAT was charged and is shown not to be deductible or refundable (§ 3-30 third paragraph).
- **Services that must be done in Norway** (work on property or goods in Norway, for example) are not remote; the foreign supplier must register through the ordinary rules.
- **Sales to consumers by foreign sellers (VOEC).** A foreign seller of low-value goods (under NOK 3,000 per item) or remote services to consumers in Norway must register (§ 2-1 third paragraph) and can use the simplified VOEC scheme without reaching the NOK 50,000 limit (§ 14-4). Food, goods needing a special import permit and goods with excise duties are not low-value goods under this rule (§ 3-1 second paragraph). VOEC returns are quarterly, due 20 days after the quarter.
- **Exports.** Goods exported are zero-rated (§ 6-21). Services wholly used abroad, and remote services to a buyer resident abroad, are zero-rated (§ 6-22). Keep proof of export and of the buyer's residence.
- **Input VAT on remote services used abroad.** A registered business may deduct input VAT on remote services it uses outside Norway (§ 8-9).

## Worked examples

### Example 1: two-month return for a shop with a café counter

A registered shop sells standard-rated goods of NOK 200,000 and food to take away of NOK 40,000 in January and February 2026, all amounts excluding VAT. Output VAT is NOK 50,000 at 25% and NOK 6,000 at 15%, together NOK 56,000. Deductible input VAT on stock and costs is NOK 18,000. A restaurant lunch with a supplier carried NOK 500 of VAT, which is serving and entertainment and cannot be deducted. Net VAT payable is NOK 38,000, due with the return on 10 April 2026.

```oa-check
name: NO two-month VAT return, Jan-Feb 2026
inputs:
  standard_sales: 200000
  food_sales: 40000
  input_vat_deductible: 18000
  input_vat_blocked: 500
steps:
  - output_standard: pct(standard_sales, 25)
  - output_food: pct(food_sales, 15)
  - output_total: output_standard + output_food
  - net_payable: output_total - input_vat_deductible
expected:
  output_standard: 50000.00
  output_food: 6000.00
  output_total: 56000.00
  net_payable: 38000.00
```

### Example 2: crossing the limit and claiming back pre-registration VAT

A sole proprietor's VAT-able sales over the last twelve months are NOK 48,000. A new sale of NOK 5,000 takes the total to NOK 53,000, over the NOK 50,000 limit, so the business must register. Eight months earlier it bought equipment for NOK 40,000 plus NOK 10,000 VAT, paid by bank, for use in the business. In its first return it reports sales of NOK 30,000 at 25%, output VAT NOK 7,500, and deducts the NOK 10,000 on the equipment under § 8-6. The return shows NOK 2,500 to be paid back to the business.

```oa-check
name: NO registration crossing and pre-registration input VAT (2026)
inputs:
  rolling_sales: 48000
  new_sale: 5000
  limit: 50000
  first_period_sales: 30000
  equipment_vat: 10000
steps:
  - rolling_total: rolling_sales + new_sale
  - over_limit: rolling_total - limit
  - output_vat: pct(first_period_sales, 25)
  - net: output_vat - equipment_vat
expected:
  rolling_total: 53000.00
  over_limit: 3000.00
  output_vat: 7500.00
  net: -2500.00
```

## Ask the client first

- Are you registered for VAT? From what date, and with two-monthly, annual or another period? Who has the Altinn access package to submit?
- What were your VAT-able sales in the last twelve months (excluding VAT and exempt sales)? Are you a charity or non-profit?
- What do you sell, and does any of it fall under the 15%, 12% or 11.11% rates, an exemption or a zero rate (exports, books, newspapers)? Do you sell food as part of serving?
- Do you import goods or buy services from abroad? Do you have the customs declarations?
- Do your costs include meals, entertainment, gifts, staff benefits, art, housing, or passenger cars? Was anything paid in cash at NOK 10,000 or more?
- Is any purchase used partly outside the VAT-able business?

## Sources

| Source | URL | Read on |
|---|---|---|
| Stortingsvedtak om merverdiavgift for 2026, FOR-2025-12-18-2752 (§§ 1 to 5) | https://lovdata.no/dokument/STV/forskrift/2025-12-18-2752 | 2026-10-30 |
| Merverdiavgiftsloven, lov 2009-06-19-58 (§§ 1-3, 2-1, 2-4, 3-1, 3-30, 4-11, 5-2, 5-5, 5-12, 6-21, 6-22, 8-1 to 8-4, 8-6, 8-8, 8-9, 11-1, 11-3, 14-4, 15-10) | https://lovdata.no/lov/2009-06-19-58 | 2026-10-30 |
| Merverdiavgiftsforskriften, FOR-2009-12-15-1540 (§§ 1-3-1, 1-3-6, 1-3-8, 2-4-1) | https://lovdata.no/forskrift/2009-12-15-1540 | 2026-10-30 |
| Skatteforvaltningsloven, lov 2016-05-27-14 (§§ 8-3, 9-4, 12-6, 14-1, 14-4 to 14-6) | https://lovdata.no/lov/2016-05-27-14 | 2026-10-30 |
| Skatteforvaltningsforskriften, FOR-2016-11-23-1360 (§§ 8-3-1 to 8-3-10, 14-1-1) | https://lovdata.no/forskrift/2016-11-23-1360 | 2026-10-30 |
| Skattebetalingsloven, lov 2005-06-17-67 (§§ 10-30, 11-1, 11-2) | https://lovdata.no/lov/2005-06-17-67 | 2026-10-30 |
| Bokføringsloven, lov 2004-11-19-73 (§ 13) | https://lovdata.no/lov/2004-11-19-73/§13 | 2026-10-30 |
| Skatteetaten, Register, change or delete (VAT) | https://www.skatteetaten.no/en/business-and-organisation/vat-and-duties/vat/register-change-delete/ | 2026-10-30 |
| Skatteetaten, VAT return: view, change and submit | https://www.skatteetaten.no/en/business-and-organisation/vat-and-duties/vat/vat-return/ | 2026-10-30 |
| Skatteetaten, Calculating and reporting VAT on goods imports | https://www.skatteetaten.no/en/business-and-organisation/vat-and-duties/vat/foreign/import/calculating-and-reporting-vat-on-goods-imports/ | 2026-10-30 |
| Skatteetaten, Enforcement fines | https://www.skatteetaten.no/en/business-and-organisation/start-and-run/deadlines-certificates-and-accounting/enforcement-fines/ | 2026-10-30 |
| Skatteetaten, Forsinkelsesrenter | https://www.skatteetaten.no/satser/forsinkelsesrenter/ | 2026-10-30 |

Not yet confirmed: the return codes 81 to 84 for imports by rate and deduction (only item 85 was found on the import page today); the exchange rate rule for services bought from abroad (Norwegian Customs' rate at delivery); the contact-form routes for correcting periods before 2022 and 2023; whether a weekend or holiday deadline moves to the next working day for the VAT return; the full lists of exempt and zero-rated supplies (only the sections named are summarised); joint registration, VAT compensation and property adjustment.

> Contributed by Michael Cutajar.

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
