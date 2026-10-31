---
name: isle-of-man-vat
description: "Use this skill for Isle of Man VAT in 2026 under the Value Added Tax Act 1996 (an Act of Tynwald) and the Customs and Excise Agreement with the UK. It covers who must register with Isle of Man Customs and Immigration (the GBP 90,000 threshold, GBP 88,000 exception and deregistration test), the 20%, 5% and 0% rates, the Manx-only reduced rates on hotel and holiday accommodation and on construction services on eligible buildings, the domestic reverse charge for construction, exempt supplies, input tax recovery and partial exemption, return periods and online filing, late return and late payment penalties, interest, error correction, and trade with the UK and the rest of the world. Trigger on: Isle of Man VAT, IOM VAT, Manx VAT, VAT 1 MAN, Isle of Man VAT return, reduced rate construction Isle of Man. Out of scope: income tax (im-income-tax, im-corporate-income-tax), payroll (im-payroll-social), customs and excise duties."
jurisdiction: IM
category: international
tax_year: 2026
last_updated: 2026-10-31
version: 1.2
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Isle of Man VAT (2026)

The Isle of Man has its own VAT law, the Value Added Tax Act 1996 (AT 1 of 1996). Under the Customs and Excise Agreement with the United Kingdom, the Island is treated as part of the UK for customs, excise and VAT purposes, and the Island's VAT law follows UK VAT law closely. VAT is run locally by the Customs and Immigration Division of the Treasury (its web pages still sit under "Customs and Excise"). Most HMRC VAT notices are relevant to Isle of Man traders, but the Island has its own rates in a few areas, its own registration and filing, and its own penalty rules. Amounts are in pounds sterling (GBP).

There is one VAT skill for the Island. It sits in this folder with the rest of the [pack](README.md). There is no duplicate VAT skill. Related skills: [im-corporate-income-tax](../im/im-corporate-income-tax.md), [im-income-tax](../im/im-income-tax.md), [im-payroll-social](../im/im-payroll-social.md).

## Who this applies to

- **Taxable persons in the Island.** A person who makes taxable supplies (standard, reduced or zero-rated) in the course of business must consider registration. A person who makes only exempt supplies cannot register (Customs and Immigration, VAT page; Registering for VAT page).
- **One VAT area with the UK.** Most goods moving between the UK and the Island are not imports or exports and face no customs formalities. UK government guidance applies to the Island as if it were part of the UK (Imports and Exports page; VAT page). In practice a sale from the Island to a UK customer, or from the UK to an Island customer, is treated like a domestic UK sale.
- **Island-established persons register with Customs and Immigration, not HMRC.** Schedule 2 to the Act sets the threshold for Island-established persons (VATA 1996 Sch 2 para 1). Most businesses established outside both the Island and the UK that must register in the IOM/UK VAT area deal with HMRC's non-established taxable persons unit. Where Island registration fits better, they may need a tax representative, who is jointly and severally liable (Registering for VAT page).
- **Registration also follows events.** A change of legal status (for example sole trader to company), taking over a VAT-registered business as a going concern, or taking a new lease of premises to carry on the same kind of business as a VAT-registered previous tenant without a significant gap in trading (Registering for VAT page).
- **VAT groups.** Two or more eligible persons (companies, individuals, partnerships) can be treated as one taxable person. Groups and partnerships register on paper (VAT 1 MAN, VAT 50 MAN, VAT 51 MAN), not online (Registering for VAT page).

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Standard rate | 20% | 2026 | VATA 1996 s.2(1), https://legislation.gov.im/cms/images/LEGISLATION/PRINCIPAL/1996/1996-0001/1996-0001_61.pdf ; https://www.gov.im/categories/tax-vat-and-your-money/customs-and-excise/vat/ |
| Reduced rate (supplies in Schedule 1) | 5% | 2026 | VATA 1996 s.29A(1), Sch 1 |
| Zero rate (supplies in Schedule 8) | 0% | 2026 | VATA 1996 s.30, Sch 8; VAT page |
| Reduced rate: sleeping accommodation in hotels, guest-houses, hostels, holiday dwellings, holiday camps, caravan and camp sites in the Island | 5% | 2026 | VATA 1996 Sch 1 Group 8; VAT Notice 709/3A MAN, https://www.gov.im/media/1385421/vat-notice-709-3a-man_compressed.pdf |
| Reduced rate: construction services on eligible buildings in the Island | 5% | notice in effect from 6 August 2026 (Group 14 inserted by SD 2022/0249) | VATA 1996 Sch 1 Group 14; VAT Notice 708 MAN, https://www.gov.im/media/1393990/reduced-rate-notice-construction-services-6-august-2026.pdf |
| Catering share of a half or full board tariff (hotels) | normally not less than 35% of the inclusive tariff, at 20% | 2026 | VAT Notice 709/3A MAN para 5 |
| Registration threshold, taxable supplies in the past 12 months (tested at each month end) | more than GBP 90,000 | 2026 | VATA 1996 Sch 2 para 1(1)(a); https://www.gov.im/categories/tax-vat-and-your-money/customs-and-excise/vat/registering-for-vat/ |
| Registration, taxable supplies expected in the next 30 days alone | more than GBP 90,000 | 2026 | VATA 1996 Sch 2 para 1(1)(b); Registering for VAT page |
| No registration if the next 12 months will not exceed | GBP 88,000 | 2026 | VATA 1996 Sch 2 para 1(3) |
| Voluntary deregistration if the next 12 months will not exceed | GBP 88,000 | 2026 | https://www.gov.im/categories/tax-vat-and-your-money/customs-and-excise/vat/de-registering-for-vat/ |
| VAT on stock and assets at deregistration, accounted for only if over | GBP 1,000 | 2026 | De-registering for VAT page |
| Error correction threshold | net errors up to the greater of GBP 10,000 or 1% of box 6, capped at GBP 50,000, can be corrected on a later return | 2026 | https://www.gov.im/categories/tax-vat-and-your-money/customs-and-excise/vat/correcting-a-vat-return-error/ |
| Late return penalty | GBP 200 for a late return when 3 other returns were late in the previous 24 months | periods starting on or after 1 January 2023 | VATA 1996 s.59ZA, Sch 15B para 5; VAT Penalties and Interest notice (March 2026), https://www.gov.im/media/1392259/vat-penalties-and-interest-notice-27-march-2026_compressed.pdf |
| Late payment penalty, first | 3% of VAT unpaid at day 15, plus 3% of VAT unpaid at day 30 | same | VATA 1996 Sch 15C para 5 |
| Late payment penalty, second | 10% a year on VAT unpaid after day 30 | same | VATA 1996 Sch 15C para 7(3) |
| Late payment interest | 7.75% a year | from 1 May 2026 | https://www.gov.im/categories/tax-vat-and-your-money/customs-and-excise/payments/ |
| Repayment interest | 2.75% a year | from 8 January 2026 | Payments page |
| Partial exemption de minimis | exempt input tax not more than GBP 625 a month on average and not more than half of total input tax | 2026 | HMRC VAT Notice 706 para 11.2 (HMRC notices apply to Island traders: VAT page) |

## The taxable base

### Step 1: is there a taxable supply, and where is it made?

VAT is charged on supplies of goods and services and on imports (VATA 1996 s.2(1)). For services, use the place of supply rules in HMRC VAT Notice 741A, which Customs and Immigration points to; services received from outside the UK and the Island are covered there (VAT page).

### Step 2: pick the rate

- **20%** for most goods and services (s.2(1)).
- **5%** for supplies in Schedule 1. The groups are: domestic fuel or power (Group 1); grant-funded heating equipment, security goods and gas connections (Group 3); children's car seats (Group 5); residential conversions (Group 6); residential renovations and alterations (Group 7); sleeping accommodation (Group 8); contraceptive products (Group 9); welfare advice (Group 10); mobility aids for the elderly (Group 11); smoking cessation products (Group 12); caravans (Group 13); and construction services on eligible buildings (Group 14) (VATA 1996 Sch 1 Part I index).
- **0%** for supplies in Schedule 8, including food, books, construction of new dwellings, protected buildings, international services, transport, children's clothing and footwear, drugs and medicines, exports, women's sanitary products (Group 20; not the reduced rate), and the installation of energy-saving materials in the Island from 1 April 2022 to 31 March 2027 (Group 23) (VATA 1996 Sch 8 Part I index; VAT page).
- **Exempt** supplies are in Schedule 9: land, insurance, postal services, betting and gaming, finance, education, health and welfare, burial and cremation, subscriptions to trade unions and professional bodies, sport, charity fund-raising events, cultural services, investment gold and cost-sharing groups (VATA 1996 s.31, Sch 9 index). The sale of land and property is normally exempt unless the owner opts to tax (Land and Property page).
- **Private schools are not exempt.** From 1 January 2025 the education exemption does not cover education or vocational training by a private school, or board and lodging closely related to it, so these are at 20%. Teaching English as a foreign language, nursery-class education and higher education courses stay exempt (VATA 1996 Sch 9 Part III items 1 to 3 and notes, inserted by SD 2025/0102 for education and board and lodging on or after 1 January 2025).

### Step 3: the two Manx reduced rates that differ from the UK

- **Hotel and holiday accommodation (Group 8).** Accommodation in hotels, guest-houses, hostels, self-catering holiday dwellings, holiday camps, caravan sites and camp sites in the Island, including pitches, is at 5%. Timeshare is not included. A single bed and breakfast tariff is wholly at 5%. Where catering is part of a half or full board price, apportion it, normally with at least 35% of the inclusive tariff as catering at 20%. Separately charged meals are catering at 20%. Invoices must show the reduced rate on the qualifying part; less detailed invoices are not allowed. Reduced-rate supplies go in box 10 of the Island return (VAT Notice 709/3A MAN paras 2 to 5, 8). Tour operators use the Island's TOMS notice, VAT Notice 709/5 MAN, whose sections 8 to 13 have force of law.
- **Construction services on eligible buildings (Group 14).** The supply by a person registered (or required to be registered) for VAT in the Island or the UK of eligible services on an eligible building in the Island, with any building materials supplied at the same time, is at 5%. Eligible services are alterations, extensions or enlargements, repairs to the building or its boundary, safety-related repairs or maintenance to land within the boundary, and installing, repairing or maintaining building materials ordinarily incorporated in the building. Eligible buildings are dwellings with self-contained living accommodation in private use only, buildings used for a relevant residential or relevant charitable purpose, and places of worship. Holiday accommodation, separate garages, garden rooms, pools and business areas of a home are out. Surveys, architects' and interior designers' fees stay at 20%. Goods supplied alone take their own rate (VATA 1996 Sch 1 Group 14 Notes 1 to 4; VAT Notice 708 MAN, in effect from 6 August 2026).

### Step 4: domestic reverse charge for construction

A VAT-registered business that buys or sells construction services reportable under the Construction Industry Scheme, at 20% or 5%, for onward supply (not to an end user) applies the reverse charge. The supplier does not charge VAT; the customer accounts for it on its own return. End users, and intermediaries connected or linked to an end user, are outside it (VATA 1996 s.55A; Domestic Reverse Charge notice, July 2024). A subcontractor supplying reduced-rate Group 14 services to a VAT-registered contractor shows 5% on the invoice and the contractor accounts for VAT at 5% (VAT Notice 708 MAN section 4).

### Step 5: input tax and partial exemption

Input tax on costs used for taxable supplies (including zero-rated ones) is recoverable. Input tax on costs used for exempt supplies is not, except under the de minimis rule: a business is treated as fully taxable in a period if exempt input tax is not more than GBP 625 a month on average and not more than half of all input tax (HMRC VAT Notice 706 paras 11.1, 11.2). Business entertainment and motor cars follow HMRC VAT Notices 700/65 and 700/64 (HMRC VAT Notice 700). Fuel used privately in a business car either attracts the road fuel scale charge or no VAT on that car's fuel is recovered (VAT page).

### Step 6: special schemes

Flat Rate Scheme (VAT 600 FRS MAN), Annual Accounting Scheme (VAT 600 AA MAN) and Cash Accounting (no application needed) are available, on the conditions in HMRC Notices 733, 732 and 731 (Registering for VAT page).

## Deadlines and filing

- **Registration.** Register online through gov.im online services, or on VAT 1 MAN (plus REG 5 MAN turnover sheet if supplies have already been made, REG 3 MAN for land and property, REG 4 MAN or REG 7 MAN for yachts and aircraft, REG 9 MAN for digital services and IP businesses). Customs and Immigration aims to process applications in 10 working days. You receive a VAT registration certificate and a Tax Identification Number. VAT cannot be shown on invoices until the number arrives (Registering for VAT page).
- **Return periods.** Most businesses file quarterly, with quarters ending in January, April, July and October; February, May, August and November; or March, June, September and December. Monthly returns are possible, and annual returns under the Annual Accounting Scheme (VAT 1 MAN guidance notes, April 2026, note 14).
- **Online filing and payment.** All registered persons file returns and pay electronically through the Customs and Immigration online portal, unless granted an exemption (insolvency, religious objection, age, disability, location or other reason why online filing is not reasonable) (Exemption from using VAT Online Services, July 2026). Agents can be appointed in the portal.
- **Payment timing.** Payment must reach the Treasury's account by the deadline; if the deadline falls on a weekend or bank holiday, it must arrive on the last working day before. Electronic payments received after 5:30pm count as received the next working day; card payments online count on the day made (Payments page).
- **Deregistration.** Tell Customs and Immigration within 30 days if you stop making taxable supplies, sell or close the business, join a VAT group or change legal status. The final return is due within one month of the cancellation date, or two months under cash accounting (De-registering for VAT page; form VAT 7 MAN).
- **Option to tax.** Notify options to tax on land or buildings in the Island or UK on the VAT 1614 MAN forms (Land and Property page).

## Penalties and interest

- **Late returns** (VAT periods starting on or after 1 January 2023). The first three late returns in a rolling 24 months get warning letters. A late return when three other returns were late in the 24 months ending on its due date costs GBP 200. Each further late return can cost another GBP 200 (VATA 1996 Sch 15B para 5(2); VAT Penalties and Interest notice paras 2.1, 2.2). This applies to nil and repayment returns too (Payments page).
- **Late payments.** No penalty if paid in full within 15 days of the due date, or if a time to pay arrangement is proposed in that time and agreed. Otherwise 3% of the VAT unpaid at day 15. If VAT is still unpaid at day 30 with no time to pay agreement, another 3% of the amount unpaid then. From day 31 a second penalty accrues daily at 10% a year on the VAT outstanding until paid (VATA 1996 Sch 15C paras 4, 5, 7; notice paras 3.1 to 3.5).
- **Interest.** Late payment interest runs from the due date to payment, whether or not a penalty applies. The rate is 7.75% a year from 1 May 2026 (6.25% from 8 January to 30 April 2026). Repayment interest is 2.75% a year from 8 January 2026 (Payments page; notice paras 4.1, 4.2).
- **Errors.** Most errors on returns from the last four years can be amended online. Net errors over the threshold (the greater of GBP 10,000 or 1% of box 6, up to GBP 50,000) must be reported on VAT 652 MAN. Undisclosed errors found later can lead to a penalty, and default interest is charged as commercial restitution (Correcting a VAT Return Error page).
- **Reviews and appeals.** Penalties can be challenged by internal review and appeal to the VAT and Duties Tribunal, including on grounds of reasonable excuse (notice para 5).
- **Late registration** can lead to a penalty (Registering for VAT page).

## Cross-border points

- **UK.** Sales between the Island and the UK are not imports or exports for VAT or customs; most goods move without customs formalities. A UK-registered supplier carrying out Group 14 work in the Island can apply the 5% rate (Imports and Exports page; Sch 1 Group 14 Note 1).
- **Imports and exports with other countries,** including the EU, are imports and exports. Goods must clear customs controls, including payment of any taxes, at the border; declarations go through the Customs Declaration Service, where businesses that have used postponed import VAT accounting already have a login. A GB EORI number is needed, and goods from the EU have needed a safety and security declaration since 31 January 2025 (Imports and Exports page).
- **Services from abroad.** Place of supply and reverse charge follow HMRC Notice 741A (VAT page).
- **Overseas businesses** that must register usually deal with HMRC; where Island registration is more appropriate a tax representative may be required (Registering for VAT page).
- **Island reduced rates are territorial.** The Group 8 and Group 14 rates apply only to accommodation and buildings in the Island (Sch 1 Groups 8 and 14). The same services in the UK are taxed under UK law.

## Worked examples

### Example 1: registration, a quarterly return and a late payment

A Douglas consultancy's taxable supplies for the 12 months to 31 May 2026 are GBP 92,000. That exceeds GBP 90,000 at the end of May, so it must register. In its first quarter it makes GBP 30,000 of standard-rated sales and incurs GBP 1,500 of input tax on business costs. Output tax is GBP 6,000 and the net VAT due is GBP 4,500. It pays 20 days after the due date with no time to pay arrangement. The first late payment penalty is 3% of the VAT unpaid at day 15, GBP 135. Interest also runs from the due date.

```oa-check
name: IM VAT registration test, quarterly return and late payment penalty (2026)
inputs:
  rolling_12m_supplies: 92000
  threshold: 90000
  sales_net: 30000
  input_tax: 1500
steps:
  - excess_over_threshold: rolling_12m_supplies - threshold
  - output_tax: sales_net * 0.20
  - net_vat: output_tax - input_tax
  - penalty_day15: net_vat * 0.03
expected:
  excess_over_threshold: 2000.00
  output_tax: 6000.00
  net_vat: 4500.00
  penalty_day15: 135.00
```

### Example 2: hotel dinner, bed and breakfast at mixed rates

A Ramsey hotel sells dinner, bed and breakfast for GBP 100 including VAT. Under Notice 709/3A MAN the catering element is at least 35% of the inclusive tariff, so GBP 35 is catering at 20% and GBP 65 is accommodation at 5%. VAT on the catering is 35 x 20/120 = GBP 5.83. VAT on the accommodation is 65 x 5/105 = GBP 3.10. Total VAT is GBP 8.93. The accommodation value excluding VAT, GBP 61.90, goes in box 10 as well as box 6. A bed and breakfast tariff of GBP 100 would be all at 5%: VAT GBP 4.76.

```oa-check
name: IM hotel DBB tariff 100 split 35% catering at 20% and accommodation at 5% (2026)
inputs:
  tariff_incl_vat: 100
  catering_share: 0.35
steps:
  - catering_gross: tariff_incl_vat * catering_share
  - accommodation_gross: tariff_incl_vat - catering_gross
  - vat_catering: round(catering_gross * 20 / 120, 2)
  - vat_accommodation: round(accommodation_gross * 5 / 105, 2)
  - total_vat: vat_catering + vat_accommodation
  - accommodation_net: accommodation_gross - vat_accommodation
  - bb_only_vat: round(tariff_incl_vat * 5 / 105, 2)
expected:
  catering_gross: 35.00
  vat_catering: 5.83
  vat_accommodation: 3.10
  total_vat: 8.93
  accommodation_net: 61.90
  bb_only_vat: 4.76
```

## Ask the client first

1. Is the business established in the Island, in the UK or elsewhere, and what are its taxable supplies for each of the last 12 months?
2. What does it sell, and do any sales fall in the Manx reduced rates (accommodation in the Island, work on eligible buildings in the Island) or the exempt groups (finance, insurance, gaming, land)?
3. Is it a contractor or subcontractor in construction, and are its customers end users?
4. Which return stagger and schemes does it use (flat rate, annual accounting, cash accounting)?
5. Have any returns or payments been late in the last 24 months, and is there a time to pay arrangement?
6. Does it import or export goods outside the UK and the Island, or buy services from abroad?

## Sources

| Source | URL | Read on |
|---|---|---|
| Value Added Tax Act 1996 (AT 1 of 1996), consolidated text [61]: ss.2, 29A, 30, 31, 55A, 59ZA; Sch 1 (Groups 8 and 14), Sch 2 para 1, Sch 8 and Sch 9 indexes, Sch 9 Part III, Sch 15B para 5, Sch 15C paras 4 to 7 | https://legislation.gov.im/cms/images/LEGISLATION/PRINCIPAL/1996/1996-0001/1996-0001_61.pdf | 2026-10-30 |
| Customs and Immigration, VAT | https://www.gov.im/categories/tax-vat-and-your-money/customs-and-excise/vat/ | 2026-10-30 |
| Customs and Immigration, Registering for VAT | https://www.gov.im/categories/tax-vat-and-your-money/customs-and-excise/vat/registering-for-vat/ | 2026-10-30 |
| Customs and Immigration, De-registering for VAT | https://www.gov.im/categories/tax-vat-and-your-money/customs-and-excise/vat/de-registering-for-vat/ | 2026-10-30 |
| Customs and Immigration, Correcting a VAT Return Error | https://www.gov.im/categories/tax-vat-and-your-money/customs-and-excise/vat/correcting-a-vat-return-error/ | 2026-10-30 |
| Customs and Immigration, Land and Property | https://www.gov.im/categories/tax-vat-and-your-money/customs-and-excise/vat/land-and-property/ | 2026-10-30 |
| Customs and Immigration, Payments (penalties and interest rates) | https://www.gov.im/categories/tax-vat-and-your-money/customs-and-excise/payments/ | 2026-10-30 |
| Customs and Immigration, Imports and Exports | https://www.gov.im/categories/tax-vat-and-your-money/customs-and-excise/imports-and-exports/ | 2026-10-30 |
| Customs and Immigration, Customs and Excise Online Service | https://www.gov.im/categories/tax-vat-and-your-money/customs-and-excise/customs-and-excise-online-service/ | 2026-10-30 |
| Notice: VAT Penalties and Interest (March 2026) | https://www.gov.im/media/1392259/vat-penalties-and-interest-notice-27-march-2026_compressed.pdf | 2026-10-30 |
| VAT Notice 708 MAN, Reduced Rate: Construction Services in the Isle of Man (effect from 6 August 2026) | https://www.gov.im/media/1393990/reduced-rate-notice-construction-services-6-august-2026.pdf | 2026-10-30 |
| VAT Notice: Domestic Reverse Charge, Construction Services in the Isle of Man (July 2024) | https://www.gov.im/media/1394772/domestic-reverse-charge_compressed.pdf | 2026-10-30 |
| VAT Notice 709/3A MAN, Reduced Rate: Hotel Accommodation and Similar Establishments (July 2024) | https://www.gov.im/media/1385421/vat-notice-709-3a-man_compressed.pdf | 2026-10-30 |
| VAT Notice 709/5 MAN, Isle of Man Tour Operator's Margin Scheme | https://www.gov.im/media/1385422/vat-notice-709-5-man_compressed.pdf | 2026-10-30 |
| Guidance notes on completing VAT 1 MAN (April 2026) | https://www.gov.im/media/1392505/vat-1-man-guidance-notes-uploaded-170426.pdf | 2026-10-30 |
| Exemption from using VAT Online Services (July 2026) | https://www.gov.im/media/1393738/vat-online-exemption-guidance-july-2026.pdf | 2026-10-30 |
| HMRC VAT Notice 706, Partial exemption, section 11 | https://www.gov.uk/guidance/partial-exemption-vat-notice-706 | 2026-10-30 |
| HMRC VAT Notice 700, The VAT guide | https://www.gov.uk/guidance/vat-guide-notice-700 | 2026-10-30 |
| HMRC VAT Notice 700/12, Filling in your VAT return (boxes 1 to 9) | https://www.gov.uk/guidance/how-to-fill-in-and-submit-your-vat-return-vat-notice-70012 | 2026-10-30 |

Not yet confirmed: the due date for Island VAT returns and payments (the old version of this skill said 1 month and 7 days after the period end; HMRC Notice 700/12 gives that for UK traders, but no Island source read today states it, and the Island VAT Regulations were not read); whether UK Making Tax Digital record-keeping rules apply in the Island (the old version said they do; the Island pages read today describe filing through the Island's own online portal and do not mention Making Tax Digital); the format of Island VAT numbers (the old version said GB plus 9 digits); the full layout of the Island return beyond box 10 (HMRC Notice 700/12 describes boxes 1 to 9 for the UK return); the late registration penalty amount; any other Island-only zero-rating or exemption differences from the UK (the old version flagged aircraft parts and repairs); whether postponed VAT accounting lets an Island importer declare import VAT on the return instead of paying it at the border (the old version said so; the Imports and Exports page mentions only that postponed-accounting users already have a Customs Declaration Service login).

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
