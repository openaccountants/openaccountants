---
name: bermuda-tax
description: >
  Start here for any Bermuda tax question in 2026. Bermuda has no personal income tax, no
  VAT, GST or sales tax, no capital gains tax and no withholding tax on dividends, interest
  or royalties. This skill says so plainly and covers what Bermuda does charge outside
  payroll and corporate income tax, namely customs import duty under the 2026 tariff,
  duty-free allowances, stamp duty on land transfers, leases and other documents, and
  land tax on annual rental value and the 1.25% foreign currency purchase tax, and routes payroll tax, social insurance, corporate
  income tax and company formation to their own skills. Trigger phrases include Bermuda
  tax, Bermuda income tax, Bermuda VAT, Bermuda customs duty, Bermuda stamp duty, land tax.
version: "3.2"
jurisdiction: BM
tax_year: 2026
last_updated: 2026-11-15
category: international
type: situation-rules
domain: tax
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
---

# Bermuda tax v3.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Anyone asking what tax applies in Bermuda: residents, non-residents with Bermuda property, importers, buyers and tenants of land, and companies. Bermuda is a British Overseas Territory. The currency is the Bermuda dollar (BMD), at par with the US dollar. Taxes are administered by the Office of the Tax Commissioner (payroll tax, land tax, stamp duty), the Customs Department (import duty), the Department of Social Insurance and, for corporate income tax, the Corporate Income Tax Agency (CITA).

What Bermuda does not charge, for individuals and for companies outside an in-scope multinational group: income tax, capital gains tax, VAT, GST or general sales tax, and withholding tax on dividends, interest or royalties. It does charge a 1.25% foreign currency purchase tax when a resident buys foreign currency from a Bermuda bank, which often bites when money is sent abroad ([Foreign Currency Purchase Tax Act 1975](https://www.bermudalaws.bm/Laws/Consolidated%20Law/1975/Foreign%20Currency%20Purchase%20Tax%20Act%201975)). There is no income tax return for individuals and no VAT registration, return or reverse charge. The tax on employment income is the employee portion of payroll tax, and indirect tax is collected mainly as customs duty at import ([Payroll tax](https://www.gov.bm/payroll-tax); [Customs Tariff 2026](https://www.gov.bm/files/media-library/20260413/753f0169-2026_bermuda_customs_tariff_2026.03.27v1r0_0.pdf)).

What changed: since fiscal years beginning on or after 1 January 2025, Bermuda constituent entities of multinational groups with EUR 750 million revenue pay 15% corporate income tax ([gov.bm, corporate income tax](https://www.gov.bm/articles/cit)). The old statement that a tax assurance guarantees no income tax until 2035 is wrong for those groups: the CIT applies notwithstanding any assurance under the Exempted Undertakings Tax Protection Act 1966 (CIT Act 2023 s.4(4)).

Which skill to load:

| Question | Skill |
|---|---|
| Payroll tax, employer and employee portions, social insurance | [bm-payroll-social](bm-payroll-social.md) |
| 15% corporate income tax for large groups, transfer pricing | [bm-corporate-income-tax](bm-corporate-income-tax.md) |
| Forming a company, beneficial ownership, economic substance declaration | [bm-company-formation](bm-company-formation.md) |
| Customs duty, stamp duty, land tax, foreign currency purchase tax, no income tax, no VAT | this skill |

## Rates, bands and thresholds

| Item | 2026 figure and conditions | Official source |
|---|---|---|
| Personal income tax, capital gains tax, VAT or sales tax | None; employment income bears the payroll tax employee portion instead | [Payroll tax](https://www.gov.bm/payroll-tax) |
| Customs duty, most common ad valorem rate | 25% of value, for example portable computers (8471.300) and colour televisions (8528.720); rate is per tariff line | [Customs Tariff 2026](https://www.gov.bm/files/media-library/20260413/753f0169-2026_bermuda_customs_tariff_2026.03.27v1r0_0.pdf) |
| Customs duty, other cameras (8525.890) | 10% | same |
| Customs duty, cotton T-shirts (6109.100) and footwear (6403.990) | 6.5% | same |
| Customs duty, prescription-only medicaments (3004.901) | 0%; other medicaments (3004.909) 25% | same |
| Customs duty, milk powder (0402.100) | 0% | same |
| Customs duty, small cars up to 1,000 cc valued BMD 10,000 or less (8703.217) | 75%; other vehicle lines carry their own value-banded rates | same |
| Passenger allowance, visitor | Up to BMD 50 on other accompanied personal goods that will remain in Bermuda (9801.420), plus 200 cigarettes, 50 cigars, 0.5 kg tobacco, 1 litre wine and 1 litre spirits; the alcohol and tobacco allowances only for an importer aged 18 or over, one aggregate quantity per person | [Duty free allowances](https://www.gov.bm/articles/duty-free-allowances); [Customs Tariff 2026, Chapter 98](https://www.gov.bm/files/media-library/20260413/753f0169-2026_bermuda_customs_tariff_2026.03.27v1r0_0.pdf) |
| Passenger allowance, resident (islander) | Up to BMD 300 on other accompanied personal goods acquired outside Bermuda (9801.415), plus the same tobacco and alcohol limits | same |
| Accompanied goods above the allowances | Spirits BMD 12.89 a litre (9801.103), wine BMD 6.00 a litre (9801.104), cigarettes BMD 80.00 per 200 (9801.209), other tobacco BMD 500.00 a kg (9801.303), other cigars 35% (9801.309), other goods 25% (9801.419 islanders, 9801.490 visitors) | [Customs Tariff 2026, heading 98.01](https://www.gov.bm/files/media-library/20260413/753f0169-2026_bermuda_customs_tariff_2026.03.27v1r0_0.pdf) |
| Chapter 98 against the ordinary heading | Goods classifiable under heading 98.01 (accompanied) or 98.02 (unaccompanied) and another heading go under 98.01 or 98.02, unless the other heading's rate is 0% or a percentage greater than 25% (Special Rules of interpretation 1 and 2) | [Customs Tariff Act 1970, First Schedule 2026](https://www.gov.bm/files/media-library/20260413/e1311751-2026_customs_tariff_act_1970_first_schedule_final_2026.03.31v1r0.pdf) |
| Customs traveller declaration, from 1 October 2026 | Declare on arrival accompanied goods not covered by allowances, restricted or prohibited goods, and cash, negotiable instruments, precious metals or stones with a total value greater than BMD 10,000; leaving Bermuda with more than BMD 10,000 of these needs Customs Form 98 | [Revenue (Customs Traveller Declaration) Amendment Notice 2026, BR 109/2026](https://www.bermudalaws.bm/Document/%7B68161f46-0415-4638-9f13-8aec2993708b%7D) |
| Retail shops capital investment relief | Approved scheme, listed goods and Ministerial approval needed; import cutoff extended from 31 March 2026 to 31 March 2031 (deemed in force 1 April 2026); the written claim must reach the Collector not later than one calendar month after 31 March 2031, or a later date the Minister allows (principal Act s 7(2)) | [Retail Shops (Temporary Customs Duty Relief for Capital Investments) Amendment Act 2026, 2026:17](https://www.bermudalaws.bm/Laws/Annual%20Law/Acts/2026/Retail%20Shops%20%28Temporary%20Customs%20Duty%20Relief%20For%20Capital%20Investments%29%20Amendment%20Act%202026) |
| Stamp duty, conveyance or transfer on sale of Bermuda land, first BMD 100,000 | 2.1% | [Stamp duty](https://www.gov.bm/articles/stamp-duty-tax-legal-transactions) |
| Stamp duty, next BMD 400,000 (to 500,000) | 3.15% | same |
| Stamp duty, next BMD 500,000 (to 1,000,000) | 4.20% | same |
| Stamp duty, next BMD 500,000 (to BMD 1.5 million) | 6.3% | same |
| Stamp duty, over BMD 1.5 million | 7.35% | same |
| Stamp duty, conveyance on sale of property that is not Bermuda property (Head 15) | 1.05% of the consideration under the Act; the gov.bm page prints 1%, the Act governs | [Stamp Duties Act 1976, Schedule Head 15](https://www.bermudalaws.bm/Laws/Consolidated%20Law/1976/Stamp%20Duties%20Act%201976) |
| Stamp duty, time for stamping a land conveyance | 30 days after execution; all persons executing are liable (Head 14) | [Stamp Duties Act 1976, Schedule Head 14](https://www.bermudalaws.bm/Laws/Consolidated%20Law/1976/Stamp%20Duties%20Act%201976) |
| Stamp duty, first time homeowner (Head 14(b)) | First BMD 1,000,000 of consideration exempt where all conditions are met: entire freehold or leasehold interest in a house, condominium or building plot; all purchasers individuals with Bermudian status (or a Bermudian and a non-Bermudian spouse) who have never held more than 25% of the market value of any Bermuda residential property or land; consideration at fair market value and wholly in money or mortgage money; the Tax Commissioner's s 22 opinion; the signed declarations. The old three-year residence condition was repealed from 20 October 2022 | [Stamp Duties Act 1976, Schedule Head 14(b)](https://www.bermudalaws.bm/Laws/Consolidated%20Law/1976/Stamp%20Duties%20Act%201976); [Stamp Duties Amendment (No. 2) Act 2023](https://www.bermudalaws.bm/Laws/Annual%20Law/Acts/2023/Stamp%20Duties%20Amendment%20(No.%202)%20Act%202023); [Stamp Duties Amendment Act 2022](https://www.bermudalaws.bm/Laws/Annual%20Law/Acts/2022/Stamp%20Duties%20Amendment%20Act%202022) |
| Stamp duty, conveyance under a granted pre-qualification first time homeowner notice (Head 14(c)) | Nil on the first BMD 1,000,000; 6.3% on the next BMD 500,000; 7.35% thereafter (from 1 April 2023) | [Stamp Duties Amendment (No. 2) Act 2023](https://www.bermudalaws.bm/Laws/Annual%20Law/Acts/2023/Stamp%20Duties%20Amendment%20(No.%202)%20Act%202023) |
| Stamp duty, lease up to three years | 1.05% of aggregate rent for the term | [Stamp duty](https://www.gov.bm/articles/stamp-duty-tax-legal-transactions) |
| Stamp duty, lease over three years | 1.05% of aggregate rent for the first three years plus 0.5% of aggregate rent for the remaining period | same |
| Stamp duty, duplicate copies | BMD 27 each | same |
| Stamp duty, mortgage refinanced to another institution | No duty on the first BMD 1,000,000; excess at 0.5% | same |
| Adjudication fee (Tax Commissioner's opinion on duty), from 1 April 2023 | BMD 212 per item | same |
| Stamp duty, late stamping penalty (only with the Tax Commissioner's special permission, s 10) | Within three months: double the deficient duty or BMD 10, whichever is greater; after three months: four times the deficient duty or BMD 25, whichever is greater; maximum BMD 500; the Commissioner may remit; payable in addition to the duty | [Stamp Duties Act 1976, s 10](https://www.bermudalaws.bm/Laws/Consolidated%20Law/1976/Stamp%20Duties%20Act%201976) |
| Stamp duty, offence of failing to stamp (s 67) | On summary conviction, a fine of BMD 200 or four times the unpaid duty, whichever is greater (a maximum, separate from the duty and the s 10 penalty) | same |
| Stamp duty, rounding (s 76) | Percentage duty with a fraction of a cent is rounded up to the next whole cent | same |
| Land tax, private dwelling, ARV not over BMD 22,000 | BMD 150 a year (base rate cut from BMD 300 from 1 January 2026) | [Land Tax Amendment Act 2025](https://www.bermudalaws.bm/Laws/Annual%20Law/Acts/2025/Land%20Tax%20Amendment%20Act%202025); [Land Tax Act 1967, s 2](https://www.bermudalaws.bm/Laws/Consolidated%20Law/1967/Land%20Tax%20Act%201967) |
| Land tax, private dwelling, ARV over BMD 22,000 | Every band below is charged on its slice of the ARV, starting from the first band (0.80% on 0 to 11,000), plus the BMD 150 base; the low bands are not skipped | same |
| Land tax, private dwelling ARV bands | 0.80% (0 to 11,000), 1.80% (11,001 to 22,000), 3.50% (22,001 to 33,000), 6.50% (33,001 to 44,000), 17.00% (44,001 to 90,000), 35.00% (90,001 to the next band), 55.00% (120,001 and over) | [Land tax](https://www.gov.bm/land-tax) |
| Land tax, commercial property from 1 July 2019 | 9.5% of ARV (other units, s 2(c)(ii)); a unit other than a private dwelling in an Economic Empowerment Zone 7% (s 2A); tourist units: see Not yet confirmed | [Land Tax Act 1967, ss 2 and 2A](https://www.bermudalaws.bm/Laws/Consolidated%20Law/1967/Land%20Tax%20Act%201967) |
| Land tax, interest on arrears | At the statutory rate, calculated monthly, on tax not paid within 30 days beginning on the due date in the demand note (s 39A); the statutory rate is 3.5% a year unless an order prescribes another (gov.bm's land tax page says 7%; see Not yet confirmed) | [Land Valuation and Tax Act 1967, s 39A](https://www.bermudalaws.bm/Laws/Consolidated%20Law/1967/Land%20Valuation%20and%20Tax%20Act%201967); [Interest and Credit Charges (Regulation) Act 1975, s 1](https://www.bermudalaws.bm/Laws/Consolidated%20Law/1975/Interest%20and%20Credit%20Charges%20(Regulation)%20Act%201975) |
| Land tax special concessionary basis, owner-occupier aged 65 or over with Bermudian status (s 3A) | On application to the Tax Commissioner: no tax where the ARV does not exceed BMD 45,500; above that, tax on the full ARV minus the tax on a private dwelling with ARV BMD 45,500 (BMD 1,791 a year, derived; gov.bm prints the same figure) | [Land Tax Act 1967, s 3A](https://www.bermudalaws.bm/Laws/Consolidated%20Law/1967/Land%20Tax%20Act%201967); [Land tax](https://www.gov.bm/land-tax) |
| Land tax, valuation list | The 2015 Valuation List (in effect from 1 January 2016) continues until 31 December 2026; the next draft list is due by 31 December 2026 | [Land Valuation and Tax (Special Provisions and Postponement of Preparation of Draft Valuation List) Act 2025](https://www.bermudalaws.bm/Document/%7B82ba68fb-4024-459a-80d2-0b7c9934476c%7D) |
| Foreign currency purchase tax | 1.25% of every Bermuda dollar a resident pays to buy foreign currency from a bank, from 1 April 2019; the bank collects and remits it | [Foreign Currency Purchase Tax Act 1975, s 2 and First Schedule](https://www.bermudalaws.bm/Laws/Consolidated%20Law/1975/Foreign%20Currency%20Purchase%20Tax%20Act%201975); [Amendment Act 2019](https://www.bermudalaws.bm/Laws/Annual%20Law/Acts/2019/Foreign%20Currency%20Purchase%20Tax%20Amendment%20Act%202019); [gov.bm, foreign currency purchase tax](https://www.gov.bm/foreign-currency-tax) |
| Foreign currency purchase tax, exempt transactions | Transactions for their own account by the Government, the Bermuda Monetary Authority, Bermuda Housing Corporation, Bermuda Hospitals Board, Bermuda Tourism Authority, Bermuda Deposit Insurance Corporation, a bank, a licensed deposit company, a licensed credit union or an unlimited trust licence holder (acting for another person, including an affiliate, is not own account); premium remittances by insurers and pension contribution remittances, each with the Controller's permission; one named solar project (Saturn Solar Bermuda 1 Ltd) | [Foreign Currency Purchase Tax Act 1975, Second Schedule](https://www.bermudalaws.bm/Laws/Consolidated%20Law/1975/Foreign%20Currency%20Purchase%20Tax%20Act%201975) |

## The base

- **Customs duty** is charged on the value of goods imported for home use at the rate on the tariff line (Customs Tariff Act 1970 and its Schedules, updated to 1 April 2026). Classify the goods to the exact tariff code before applying a rate; the 25% common rate is not a default for every good, and broad labels such as "electronics" do not settle the rate (a camera under 8525.890 is 10%, a portable computer under 8471.300 is 25%). The customs value is the transaction value with the required additions, but it excludes the cost of transport to Bermuda, the loading, unloading and handling charges of that transport, and insurance ([Revenue Act 1898, Second Schedule](https://www.bermudalaws.bm/Laws/Consolidated%20Law/1898/Revenue%20Act%201898)). Personal goods can fall under Chapter 98 (accompanied, unaccompanied, or post and licensed courier under heading 98.03), and the Collector can reject a Chapter 98 classification and require the ordinary heading; do not pick the heading with the lowest rate. Goods imported duty-free as used personal baggage (9801.411 or 9802.101) may not be sold for gain within six months ([Customs Tariff 2026, s.2A and Chapter 98 notes](https://www.gov.bm/files/media-library/20260413/753f0169-2026_bermuda_customs_tariff_2026.03.27v1r0_0.pdf)). Some lines carry specific rates instead of a percentage, for example wine (2204.210) at BMD 6.00 a litre. When goods fall under heading 98.01 or 98.02 and also under an ordinary heading, Chapter 98 wins unless the ordinary heading's rate is 0% or above 25% ([First Schedule, Special Rules 1 and 2](https://www.gov.bm/files/media-library/20260413/e1311751-2026_customs_tariff_act_1970_first_schedule_final_2026.03.31v1r0.pdf)). So a resident bringing back a BMD 5,000 camera for personal use (ordinary line 8525.890 at 10%) uses 98.01: BMD 300 allowance, then 25% on BMD 4,700, which is BMD 1,175 (derived), not the BMD 500 the ordinary line would give; a camera imported commercially uses the ordinary 10%. Relief notices are narrow: for example BR 131/2026 makes only the Bermuda International Mediation and Arbitration Centre an approved business under CPC 4237 for its qualifying goods, from 12 November 2026 to 31 March 2028 ([BR 131/2026](https://www.bermudalaws.bm/Laws/Annual%20Law/Statutory%20Instruments/2026/Customs%20Tariff%20%28Approved%20Businesses%20-%20CPC%204237%29%20Temporary%20%28No.%207%29%20Notice%202026)); a notice for one beneficiary is not general relief.
- **Stamp duty** is charged on instruments: conveyances, leases, mortgages, trust deeds, the affidavit of value of a deceased estate, powers of attorney, insurance policies, share transfers, memoranda of association and others on the Office's list. Unstamped documents are not received in evidence. Land transfer duty is charged slice by slice on the consideration on the date of the instrument (Head 14): never apply the top rate to the whole price. The Tax Commissioner may value the consideration (s 15), and splitting a transaction to stay under a band is prohibited (s 20). A first time homeowner relief is a set of conditions, not a label: every Head 14(b) condition must be met and declared, and the Head 14(c) schedule applies only where the Commissioner has actually granted the pre-qualification notice ([Stamp Duties Act 1976](https://www.bermudalaws.bm/Laws/Consolidated%20Law/1976/Stamp%20Duties%20Act%201976)). Under a granted notice, a BMD 1,200,000 purchase pays 6.3% on BMD 200,000, BMD 12,600 ([gov.bm, stamp duty relief](https://www.gov.bm/stamp-duty-relief)), against BMD 48,300 at the ordinary scale (derived). Late stamping is possible only with the Commissioner's special permission (no intent to evade, and urgent necessity, accident or other justifying circumstances), plus the s 10 penalty.
- **Land tax** is charged on the annual rental value (ARV) set by the Department of Land Valuation, not on the purchase price or the actual rent. It is payable by the owner as the Land Valuation and Tax Act 1967 defines it: the sole proprietor, a life tenant, a leaseholder for three years or more, a mortgagee in possession, or a periodic tenant of Government property. Tax periods begin on 1 January and 1 July and each bears half the annual tax (s 32); unpaid tax is a charge on the unit and a later owner can be liable for it (s 70). Classify the unit as at the start of the period: private dwelling, tourist unit or other unit. The 65 and over concession needs an application and the Tax Commissioner's satisfaction that the unit is a private dwelling occupied by an owner aged 65 or over with Bermudian status, during any part of the period; age alone is not enough ([Land Tax Act 1967, s 3A](https://www.bermudalaws.bm/Laws/Consolidated%20Law/1967/Land%20Tax%20Act%201967)). A zero ARV entry does not by itself remove the BMD 150 base.
- **Foreign currency purchase tax** is charged whenever a resident (as the Exchange Control Regulations 1973 deem one) buys foreign currency from a bank licensed under the Banks and Deposit Companies Act 1999, at 1.25% of the Bermuda dollars paid. The purchaser pays; the bank collects and remits. It is not a withholding tax on the dividend, interest or other payment being sent; it is a charge on the currency purchase ([Foreign Currency Purchase Tax Act 1975, ss 1A to 3](https://www.bermudalaws.bm/Laws/Consolidated%20Law/1975/Foreign%20Currency%20Purchase%20Tax%20Act%201975)). Residence for this tax follows exchange control rules, not incorporation or corporate income tax residence; settle it from the Regulations and any Controller direction before charging or exempting.
- **No estate or gift tax as such:** Bermuda has no inheritance tax; an estate meets stamp duty through the affidavit of value of the deceased estate, which is on the Office's list of dutiable documents (rate not confirmed here).
- **No income base:** profits, salaries, dividends, interest and gains of individuals and of companies outside an in-scope CIT group are not taxed on income.

## Deadlines and filing

| Tax | When and how | Source |
|---|---|---|
| Payroll tax | Quarterly, 15 January, 15 April, 15 July and 15 October; see [bm-payroll-social](bm-payroll-social.md) | [Payroll tax](https://www.gov.bm/payroll-tax) |
| Land tax | Twice a year, in March and September, on the date in the Tax Commissioner's demand note; pay online, in person, by mail (cheque) or through a bank | [Land tax](https://www.gov.bm/land-tax) |
| Land tax, legal due date | The later of the date in the demand note and seven days after the demand note is served or deemed served (s 36); the Tax Commissioner may postpone only by written notice for good cause (s 37); an objection to a demand note goes to the Commissioner within seven days of service and does not by itself postpone payment | [Land Valuation and Tax Act 1967, ss 36, 37 and 41](https://www.bermudalaws.bm/Laws/Consolidated%20Law/1967/Land%20Valuation%20and%20Tax%20Act%201967) |
| Stamp duty | Before the document is relied on; documents must be dated and signed before stamping; pay the Accountant General by cheque or cash | [Stamp duty](https://www.gov.bm/articles/stamp-duty-tax-legal-transactions) |
| Stamp duty, land conveyance | Within 30 days after execution (Head 14), counted from the last signature; instruments executed outside Bermuda and escrow deliveries have their own rules (ss 3 and 64) | [Stamp Duties Act 1976](https://www.bermudalaws.bm/Laws/Consolidated%20Law/1976/Stamp%20Duties%20Act%201976) |
| Foreign currency purchase tax | The bank collects at purchase and remits; a bank the Tax Commissioner authorises by written notice renders weekly, monthly or quarterly returns and remits with each return (s 4) | [Foreign Currency Purchase Tax Act 1975, s 4](https://www.bermudalaws.bm/Laws/Consolidated%20Law/1975/Foreign%20Currency%20Purchase%20Tax%20Act%201975) |
| Customs duty | At import, on the customs declaration; refunds of duty paid in error by letter to the Collector of Customs | [Customs Department](https://www.gov.bm/department/customs) |
| Corporate income tax | Two instalments and an annual return; see [bm-corporate-income-tax](bm-corporate-income-tax.md) | [CITA deadlines](https://www.cita.bm/assets/images/files/Filing%20%26%20Payment%20Deadlines%2005.06.2026.pdf) |

## Penalties and interest

- Land tax not paid within 30 days of the due date carries interest at the statutory rate, calculated monthly ([Land Valuation and Tax Act 1967, s 39A](https://www.bermudalaws.bm/Laws/Consolidated%20Law/1967/Land%20Valuation%20and%20Tax%20Act%201967)); the Act's statutory rate is 3.5% a year unless an order prescribes another, while gov.bm's land tax page says 7% ([Land tax](https://www.gov.bm/land-tax)). Do not compute an interest amount until the rate for the period is confirmed.
- Stamp duty stamped late with permission carries the s 10 penalty (double the deficiency or BMD 10 within three months, four times or BMD 25 after, at most BMD 500), on top of the duty. Failing to stamp is also an offence with a maximum fine of BMD 200 or four times the unpaid duty, whichever is greater (s 67), and a prosecution needs the Commissioner's sanction (s 71) ([Stamp Duties Act 1976](https://www.bermudalaws.bm/Laws/Consolidated%20Law/1976/Stamp%20Duties%20Act%201976)).
- Foreign currency purchase tax: a bank that knowingly fails to collect and remit faces a fine of BMD 5,000 or three times the tax, whichever is greater (s 5(1)); a knowingly false return or evidence, up to 6 months' imprisonment or a BMD 500 fine or both (s 5(2)); a false exemption claim, up to 6 months' imprisonment or a fine of BMD 1,000 or three times the tax, whichever is greater, or both (s 6) ([Foreign Currency Purchase Tax Act 1975](https://www.bermudalaws.bm/Laws/Consolidated%20Law/1975/Foreign%20Currency%20Purchase%20Tax%20Act%201975)). These are maxima on conviction, not automatic charges.
- An unstamped document cannot be used in evidence in any proceedings ([Stamp duty](https://www.gov.bm/articles/stamp-duty-tax-legal-transactions)).
- Customs decisions about duty and civil penalties can be reviewed by the Customs Department and then appealed to the Tax Appeal Tribunal ([Customs Department](https://www.gov.bm/department/customs)).
- Payroll tax and CIT penalties are in their own skills.

## Cross-border points

- Bermuda levies no withholding tax on dividends, interest or royalties paid abroad (no Bermuda statute read for this skill charges one). Bermuda does have tax agreements: double taxation conventions with Bahrain (in force 29 January 2012; amended by a protocol signed on 17 April 2026), Qatar and Seychelles ([gov.bm, Bahrain DTA protocol](https://www.gov.bm/news/bermuda-signs-amendment-double-taxation-agreement-kingdom-bahrain)), the 1986 tax convention with the United States ([USA-Bermuda Tax Convention Act 1986](https://www.cita.bm//assets/images/files/U.S.A.-Bermuda-Tax-Convention-Act-1986.pdf)), and many bilateral tax information exchange agreements listed on the Government's January 2022 list ([Bilateral TIEAs and DTAs](https://www.gov.bm/media/019f1ea9-0b84-722c-bb88-65a37c07e154)). Do not tell a client Bermuda has no tax treaties. CITA administers the Common Reporting Standard, Country-by-Country Reporting, FATCA and economic substance from 2026 ([gov.bm, corporate income tax](https://www.gov.bm/articles/cit)).
- A Bermuda resident who is a citizen or resident of another country (for example a US citizen) may owe that country's income tax; that is the other country's skill.
- Foreign contractors and subcontractors working in Bermuda pay payroll tax ([Payroll tax](https://www.gov.bm/payroll-tax)).
- Stamp duty on a conveyance on sale of property that is not Bermuda property is 1.05% under Head 15 of the Stamp Duties Act 1976 (the gov.bm page prints 1%).
- Sending money abroad: no withholding tax applies, but a resident who buys the foreign currency from a Bermuda bank pays 1.25% foreign currency purchase tax on the Bermuda dollars paid, unless the transaction is exempt. A BMD 100,000 purchase costs BMD 1,250 (derived).

## Two worked examples that recompute

### Example 1: stamp duty on a BMD 2,000,000 house purchase

2,100 on the first 100,000; 12,600 on the next 400,000; 21,000 on the next 500,000; 31,500 on the next 500,000; 36,750 on the last 500,000. Total 103,950. (The old version of this skill used 2%, 4%, 6% and 8% and gave 128,000; those rates are not the current ones.)

```oa-check
name: Bermuda land transfer stamp duty, BMD 2,000,000, 2026
inputs:
  price: 2000000
steps:
  - b1: min(price, 100000) * 0.021
  - b2: max(0, min(price, 500000) - 100000) * 0.0315
  - b3: max(0, min(price, 1000000) - 500000) * 0.042
  - b4: max(0, min(price, 1500000) - 1000000) * 0.063
  - b5: max(0, price - 1500000) * 0.0735
  - duty: b1 + b2 + b3 + b4 + b5
expected:
  duty: 103950
```

### Example 2 (decision): sign a three-year or a five-year lease at BMD 60,000 a year

A three-year lease: 1.05% of 180,000 = 1,890. A five-year lease: 1.05% of the first three years' rent (1,890) plus 0.5% of the remaining 120,000 (600) = 2,490. The longer lease costs 600 more stamp duty up front but secures two more years; two successive three-year leases would cost 1,890 each, 3,780 over six years. Choose on the business need; the duty favours the single longer lease.

```oa-check
name: Bermuda lease stamp duty, three years against five years
inputs:
  annual_rent: 60000
steps:
  - three_year: annual_rent * 3 * 0.0105
  - five_year: annual_rent * 3 * 0.0105 + annual_rent * 2 * 0.005
  - extra_for_five: five_year - three_year
  - two_three_year_leases: three_year * 2
expected:
  three_year: 1890
  five_year: 2490
  extra_for_five: 600
  two_three_year_leases: 3780
```

### Example 3: land tax on a private dwelling with ARV BMD 50,000, with and without the 65 and over concession

Without the concession: 88 (0.80% of 11,000) + 198 (1.80% of 11,000) + 385 (3.50% of 11,000) + 715 (6.50% of 11,000) + 1,020 (17% of 6,000) + 150 base = 2,556 a year, 1,278 each half-year. With the concession granted for both periods: 2,556 minus the 1,791 tax on ARV 45,500 = 765 a year. At ARV 22,000 the tax is the BMD 150 base; at ARV 22,100 it is 150 + 88 + 198 + 3.50 = 439.50, because every band applies once the ARV passes 22,000 (all derived).

```oa-check
name: Bermuda land tax, private dwelling, ARV BMD 50,000, 2026
inputs:
  arv: 50000
steps:
  - band1: min(arv, 11000) * 0.008
  - band2: max(0, min(arv, 22000) - 11000) * 0.018
  - band3: max(0, min(arv, 33000) - 22000) * 0.035
  - band4: max(0, min(arv, 44000) - 33000) * 0.065
  - band5: max(0, min(arv, 90000) - 44000) * 0.17
  - annual_tax: band1 + band2 + band3 + band4 + band5 + 150
  - half_year: annual_tax / 2
  - tax_at_45500: 11000 * 0.008 + 11000 * 0.018 + 11000 * 0.035 + 11000 * 0.065 + 1500 * 0.17 + 150
  - concession_tax: annual_tax - tax_at_45500
expected:
  annual_tax: 2556
  half_year: 1278
  tax_at_45500: 1791
  concession_tax: 765
```

## Ask the client first

1. Are you an individual or a company, and is the company part of a group with EUR 750 million consolidated revenue?
2. Do you employ anyone or work for yourself in Bermuda (payroll tax and social insurance)?
3. Are you importing goods? What are they, and what is their value?
4. Are you buying, selling or leasing property, and is it Bermuda property? What is the price or rent and the lease term?
5. Do you own or occupy a home, are you 65 or over, and do you have Bermudian status (land tax concession)? What ARV does the demand note show, and when was it served?
6. For a first home purchase: do all purchasers have Bermudian status (or a Bermudian and spouse), has any of you held more than 25% of any Bermuda residential property or land, and has the Tax Commissioner granted a pre-qualification notice?
7. Do you buy foreign currency from a Bermuda bank, and are you resident under exchange control rules?
8. Are you a citizen or resident of another country that taxes worldwide income?

## Sources

| Source | URL | Read on |
|---|---|---|
| Office of the Tax Commissioner, payroll tax: read for the statement that payroll tax is the tax on remuneration and applies to foreign contractors | https://www.gov.bm/payroll-tax | 2026-11-14 |
| Customs Department, Bermuda Customs Tariff 2026 (PDF, schedules to 1 April 2026): read for the tariff lines 0402.100, 2204.210, 3004.901, 3004.909, 6109.100, 6403.990, 8471.300, 8525.890, 8528.720 and 8703.217, s.2A and Chapter 98 (headings 98.01 to 98.03 and notes) and the frequency of the 25% rate | https://www.gov.bm/files/media-library/20260413/753f0169-2026_bermuda_customs_tariff_2026.03.27v1r0_0.pdf | 2026-11-14 |
| Customs Department, duty free allowances: read for the visitor and resident allowances and the tobacco and alcohol limits | https://www.gov.bm/articles/duty-free-allowances | 2026-11-14 |
| Customs Department, department page: read for refunds, reviews and appeals | https://www.gov.bm/department/customs | 2026-11-14 |
| Office of the Tax Commissioner, stamp duty on legal transactions (last updated 6 July 2026): read for the land transfer scale, non-Bermuda property, leases, duplicates, mortgage refinancing and the adjudication fee | https://www.gov.bm/articles/stamp-duty-tax-legal-transactions | 2026-11-14 |
| Office of the Tax Commissioner, land tax (last updated 6 July 2026): read for the ARV bands, the flat charge, commercial and tourist rates, due dates, interest and senior relief | https://www.gov.bm/land-tax | 2026-11-15 |
| Government of Bermuda, corporate income tax: read for the 1 January 2025 start and CITA's role for CRS and CbCR | https://www.gov.bm/articles/cit | 2026-11-14 |
| Revenue Act 1898 (consolidated), Second Schedule customs valuation: read for the exclusion of transport, loading and handling, and insurance from customs value | https://www.bermudalaws.bm/Laws/Consolidated%20Law/1898/Revenue%20Act%201898 | 2026-11-14 |
| Revenue (Customs Traveller Declaration) Amendment Notice 2026, BR 109/2026: read for the declaration categories and the BMD 10,000 cash and instruments line, operative 1 October 2026 | https://www.bermudalaws.bm/Document/%7B68161f46-0415-4638-9f13-8aec2993708b%7D | 2026-11-14 |
| Retail Shops (Temporary Customs Duty Relief for Capital Investments) Amendment Act 2026: read for the 31 March 2031 import cutoff | https://www.bermudalaws.bm/Laws/Annual%20Law/Acts/2026/Retail%20Shops%20%28Temporary%20Customs%20Duty%20Relief%20For%20Capital%20Investments%29%20Amendment%20Act%202026 | 2026-11-14 |
| Government of Bermuda, Bahrain DTA protocol press release (published 22 April 2026): read for the existing DTA and the 17 April 2026 protocol | https://www.gov.bm/news/bermuda-signs-amendment-double-taxation-agreement-kingdom-bahrain | 2026-11-14 |
| Government of Bermuda, update on bilateral TIEAs and DTAs (January 2022, PDF): read for the DTCs with Bahrain, Qatar and Seychelles and the TIEA list | https://www.gov.bm/media/019f1ea9-0b84-722c-bb88-65a37c07e154 | 2026-11-14 |
| USA-Bermuda Tax Convention Act 1986 (CITA copy): read for the existence of the US convention | https://www.cita.bm//assets/images/files/U.S.A.-Bermuda-Tax-Convention-Act-1986.pdf | 2026-11-14 |
| Government of Bermuda, types of taxes in Bermuda (updated 14 July 2026): read for the statement that individuals pay no personal income tax (its 6% employee figure is out of date and not used) | https://www.gov.bm/articles/types-taxes-bermuda | 2026-11-14 |
| CITA, filing and payment deadlines (PDF): read for the CIT due dates referred to | https://www.cita.bm/assets/images/files/Filing%20%26%20Payment%20Deadlines%2005.06.2026.pdf | 2026-11-14 |
| Land Tax Act 1967 (consolidated): read for s 1 definitions, the s 2 private dwelling rule (base rate where ARV does not exceed 22,000, every band plus the base above it), 8% tourist and 9.5% other units, s 2A 7% EEZ rate, the s 3A concession and the Schedule bands | https://www.bermudalaws.bm/Laws/Consolidated%20Law/1967/Land%20Tax%20Act%201967 | 2026-11-15 |
| Land Tax Amendment Act 2025, 2025:8: read for the base rate cut from BMD 300 to BMD 150 and the third column correction, operative 1 January 2026 | https://www.bermudalaws.bm/Laws/Annual%20Law/Acts/2025/Land%20Tax%20Amendment%20Act%202025 | 2026-11-15 |
| Land Valuation and Tax Act 1967 (consolidated): read for half-yearly tax periods (s 32), the due date rule (s 36), written postponement (s 37), interest on arrears (s 39A), demand objections (s 41) and subsequent owner liability (s 70) | https://www.bermudalaws.bm/Laws/Consolidated%20Law/1967/Land%20Valuation%20and%20Tax%20Act%201967 | 2026-11-15 |
| Land Valuation and Tax (Special Provisions and Postponement of Preparation of Draft Valuation List) Act 2025, 2025:15: read for the 2015 Valuation List continuing to 31 December 2026 | https://www.bermudalaws.bm/Document/%7B82ba68fb-4024-459a-80d2-0b7c9934476c%7D | 2026-11-15 |
| Interest and Credit Charges (Regulation) Act 1975 (consolidated): read for the statutory rate of 3.5% a year or a prescribed rate | https://www.bermudalaws.bm/Laws/Consolidated%20Law/1975/Interest%20and%20Credit%20Charges%20(Regulation)%20Act%201975 | 2026-11-15 |
| Stamp Duties Act 1976 (consolidated): read for Heads 14 and 15 (rates, 1.05% on non-Bermuda property, time for stamping, persons liable, first time homeowner conditions), ss 10, 67 and 76 | https://www.bermudalaws.bm/Laws/Consolidated%20Law/1976/Stamp%20Duties%20Act%201976 | 2026-11-15 |
| Stamp Duties Amendment (No. 2) Act 2023, 2023:13: read for the first BMD 1,000,000 exemption wording and the Head 14(c) notice schedule (nil, 6.3%, 7.35%), operative 1 April 2023 | https://www.bermudalaws.bm/Laws/Annual%20Law/Acts/2023/Stamp%20Duties%20Amendment%20(No.%202)%20Act%202023 | 2026-11-15 |
| Stamp Duties Amendment Act 2022, 2022:29: read for the repeal of the old Head 14(b)(C) residence condition, 20 October 2022 | https://www.bermudalaws.bm/Laws/Annual%20Law/Acts/2022/Stamp%20Duties%20Amendment%20Act%202022 | 2026-11-15 |
| Government of Bermuda, stamp duty relief (updated 13 April 2026): read for the BMD 12,600 duty on a BMD 1,200,000 first home purchase | https://www.gov.bm/stamp-duty-relief | 2026-11-15 |
| Foreign Currency Purchase Tax Act 1975 (consolidated): read for ss 1A to 6, the 1.25% First Schedule rate and the Second Schedule exemptions | https://www.bermudalaws.bm/Laws/Consolidated%20Law/1975/Foreign%20Currency%20Purchase%20Tax%20Act%201975 | 2026-11-15 |
| Foreign Currency Purchase Tax Amendment Act 2019, 2019:4: read for the change from 1.00% to 1.25% from 1 April 2019 | https://www.bermudalaws.bm/Laws/Annual%20Law/Acts/2019/Foreign%20Currency%20Purchase%20Tax%20Amendment%20Act%202019 | 2026-11-15 |
| Government of Bermuda, foreign currency purchase tax (updated 6 July 2026): read for the 1.25% rate on purchases by residents from a local bank | https://www.gov.bm/foreign-currency-tax | 2026-11-15 |
| Customs Tariff Act 1970, First Schedule as at 1 April 2026 (PDF): read for Special Rules of interpretation 1 and 2 (Chapter 98 against other headings) | https://www.gov.bm/files/media-library/20260413/e1311751-2026_customs_tariff_act_1970_first_schedule_final_2026.03.31v1r0.pdf | 2026-11-15 |
| Retail Shops (Temporary Customs Duty Relief for Capital Investments) Act 2008 (consolidated): read for s 7(2), the written claim and the one calendar month claim date | https://www.bermudalaws.bm/Laws/Consolidated%20Law/2008/Retail%20Shops%20%28Temporary%20Customs%20Duty%20Relief%20for%20Capital%20Investments%29%20Act%202008 | 2026-11-15 |
| Customs Tariff (Approved Businesses - CPC 4237) Temporary (No. 7) Notice 2026, BR 131/2026: read for its single named beneficiary, operative 12 November 2026, expiring 31 March 2028 | https://www.bermudalaws.bm/Laws/Annual%20Law/Statutory%20Instruments/2026/Customs%20Tariff%20%28Approved%20Businesses%20-%20CPC%204237%29%20Temporary%20%28No.%207%29%20Notice%202026 | 2026-11-15 |

Not yet confirmed: the full current list of Bermuda's double taxation agreements and TIEAs and whether the April 2026 Bahrain protocol is in force (the official treaty list seen is dated January 2022); the absence of withholding tax rests on no charging statute being found, not on an official page saying so; the land tax rate for tourist units (the Land Tax Act s 2(c)(i) consolidation says 8%, gov.bm's land tax page says 8.9%; no later amending Act was found, so no tourist unit computation is given); the land tax interest rate (the Act's statutory rate is 3.5% a year unless an order under the Interest and Credit Charges (Regulation) Act 1975 s 12 prescribes another, gov.bm says 7%; no such order was checked); how fractions of a dollar of ARV are rounded for land tax; the exchange control residence tests for foreign currency purchase tax (Exchange Control Regulations 1973 reg 3, including the 80% Bermudian ownership test for exempted companies and the permit company wording) were not opened for this skill; the old Customs Form 4/16 transition after BR 109/2026; the old file's customs rates for "food 0% to 10%", "electronics 25%" as a category and "motor vehicles 33.5%" (food and vehicles have many lines; only the lines listed above were checked, and 33.5% was not found for cars); stamp duty rates for the affidavit of value and other instruments other than conveyances, leases and mortgages; whether any customs duty relief applies to a given business (relief notices under the CPC codes carry their own beneficiary, goods and period conditions; none is applied here); wharfage and processing charges on imports; the 1 and 2 August 2026 social insurance transition (see bm-payroll-social).
