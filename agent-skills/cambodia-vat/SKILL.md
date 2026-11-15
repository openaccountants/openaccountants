---
name: cambodia-vat
description: "Prepare and review a Cambodia VAT working paper for 2026: taxable persons, domestic sales, exports, non-taxable supplies, input-credit restrictions, digital-service reverse charge and monthly reconciliation. Trigger on Cambodia VAT, GDT filing or tax on value added. Load vat-workflow-base v0.1 or later."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/cambodia-vat"
  jurisdiction: "KH"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Cambodia VAT v2.1

**General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

The filing authority is the General Department of Taxation (GDT), Ministry of Economy and Finance.

Build a Cambodian monthly VAT working paper for an ordinary self-assessment taxable person. Load **vat-workflow-base v0.1 or later** first. Produce reconciled registers and a review brief, not a return authorized for filing. QIP, SEZ and non-resident obligations remain specialist referrals. A resident business receiving digital services is distinguished from the non-resident supplier's own registration and collection obligation. The Khmer law prevails.

| Quick reference | Rate, amount or boundary | Source |
|---|---|---|
| Domestic taxable supply | 10% of VAT-exclusive taxable value, after identifying the taxable person, place and nature of supply | [Law arts 58-65](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e) |
| Export / qualifying outside-Cambodia service | 0% with actual export/place-of-supply evidence; international passenger/goods transport and related qualifying services require SD49 art 33 conditions | [Law arts 62,65](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e); [SD49 arts 27,33](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/1adcafd1-44a6-4875-b3e7-349a693b7c9c) |
| Non-taxable supply | No output VAT; related input generally unrecoverable, subject to the diplomatic-supply exception | [Law arts 63-64,68](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e) |
| VAT declaration and payment | Monthly, statutory 20th of following month; actual online calendar may differ | [Law art 71](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e) |
| Current calendar checked | October 2026 returns: manual 20 November 2026, online 25 November 2026; do not extrapolate future extensions | [GDT live calendar](https://www.tax.gov.kh/en/) |
| Input claim timing | In the receipt/import month or no later than 60 days after receipt/import, with all eligibility/document conditions | [SD49 art 12](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/1adcafd1-44a6-4875-b3e7-349a693b7c9c) |
| Invoice timing | No later than 7 days after dispatch/performance, or after payment when payment precedes them; earlier issued invoice can fix tax time | [Law art 61](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e) |
| Records | At least 10 years after completion of the last relevant transaction | [Law art 80](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e) |

## Ask the client first

Establish the entity form, residence, TIN, GDT/VAT registration, industry, actual filing month, QIP/SEZ status and any special regime. Names such as “Ltd” or “Co., Ltd” are intake clues, not registration proof. Obtain bank statements, complete sales/purchase registers and invoices, supplier TINs, customs declarations and payment receipts, prior return and credit reconciliation, export evidence and digital supplier contracts/invoices. A bank statement from ABA Bank, ACLEDA Bank, Canadia Bank, Prince Bank, Wing Bank or another bank starts reconciliation; it cannot establish credit entitlement by itself.

Confirm currency on every dual-currency entry and obtain the applicable GDT conversion instruction/rate; do not leave USD “as-is” in a KHR filing or invent an NBC conversion rule. Obtain business/private use, taxable/non-taxable use, vehicle type, petroleum product, entertainment activity, landlord invoice, credit notes and the underlying use of cash. Foreign-currency incoming funds alone do not prove export. Always reconcile brought-forward credit with the accepted prior return and adjustments.

## The method, step by step

### Classify the person, place and supply

[Law arts 57-65](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e) covers self-assessment taxable persons, resident and relevant non-resident digital suppliers, domestic supplies, imports, own use and gifts/below-cost supplies. Test goods delivery/transport origin, service performance, and the specific immovable-property and transport place rules. A foreign customer or currency is insufficient for zero rating. For goods exports retain customs and related export/payment evidence; for services establish the actual outside-Cambodia performance/place conditions. [SD49 art 33](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/1adcafd1-44a6-4875-b3e7-349a693b7c9c) specifically addresses international transport and associated passenger/goods services; its route conditions and documentary evidence must be met.

Non-taxable supplies in [Law art 63](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e) include education; public postal services; hospital/clinic, medical/dental services and incidental related goods; passenger transportation by a wholly state-owned public transport system; insurance; electrical power and clean water; locally produced unprocessed agricultural products; solid/liquid waste collection; primary financial services as defined by Prakas; qualifying duty-exempt personal imports; and recognized non-profit public-interest activities. Electrical power and clean water are not limited to residential use. Do not exempt all bank charges or every public/private transport service by name. Diplomatic/consular/international-organization supplies require [art 64](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e) confirmation, listed-personal-use and reciprocity conditions; related input has the [art 68(3)](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e) exception.

### Determine output tax and period

[Law arts 60-61,65-66](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e) and [SD49 arts 25-28](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/1adcafd1-44a6-4875-b3e7-349a693b7c9c) govern value, time and adjustments. Taxable value includes seller-charged transport and other charges and all taxes except VAT; non-cash consideration uses fair market value. Import VAT uses customs value plus customs duty and other import taxes, not an unsupported CIF-only shortcut. For a VAT-inclusive domestic amount, VAT is gross/11 and net is gross minus VAT, derived from 10%; use the actual customs assessment for imports. Used-goods margins require their special conditions and are a referral here.

Tax time is when the invoice must be issued or an earlier actual invoice. The 7-day invoice rule above applies to shipment/performance or prior payment; imports use customs declaration. Goods dispatched without an invoice need a delivery document properly recorded in the dispatch journal (Law art 61(3)). The digital reverse-charge timing exception is specified below. Continuous/multiple-payment supplies need their specific timing rules. Do not use the old blanket “earliest of invoice, payment or delivery” formula. For a cancellation, fundamental change, altered consideration or returned goods, trace the original invoice, issue/obtain the corrective debit/credit evidence and apply [SD49 art 28](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/1adcafd1-44a6-4875-b3e7-349a693b7c9c) to the affected supplier and customer. For a supply to a non-taxpayer, a downward tax adjustment requires proof that the excess VAT was refunded to that recipient (art 28(3)). Do not simply reduce whichever period is convenient.

### Admit only eligible input

Under [Law arts 68-70,78](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e) and [SD49 arts 11-19](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/1adcafd1-44a6-4875-b3e7-349a693b7c9c), require actual taxable business use, a proper VAT invoice or customs declaration and tax receipt, timing and no blocked category. Pre-registration goods/capital goods additionally must remain on hand at effective registration, be for taxable use and have been supplied/imported within 60 days before registration; use the prescribed application and payment proof (SD49 art 11). Ordinary claims follow the 60-day receipt/import limit (art 12), not a date guessed from the bank debit.

SD49 art 13 blocks entertainment, amusement/recreation unless the business supplies that activity; passenger automobiles unless the business sells or leases them; and the listed petroleum products unless the business supplies those products. Entertainment includes food, beverages, tobacco, accommodation or hospitality of any kind under art 13(4). A passenger automobile is for passengers only with no more than 10 seats. Listed products include regular/premium gasoline, diesel and lubricating oil. A transport business or documented business dinner is not, by itself, the stated exception. Current special fuel relief is not confirmed here; hold any proposed override pending its operative instrument.

Attribute taxable and non-taxable use clearly (art 14). Where the art 15 mixed-supply calculation applies, use eligible input multiplied by VAT-exclusive taxable supplies divided by taxable plus non-taxable supplies, excluding the specified non-taxable business-transfer value. Truncate that fraction to 2 decimal places without rounding: below 0.05 gives no credit, above 0.95 gives full credit, and 0.05 through 0.95 uses the fraction. Where applying art 15(1) creates difficulty, art 16 permits direct attribution where possible plus the ratio for residual input; it does not permit exempt-use input credit. Under arts 17-18 recompute the annual residual-credit position from annual totals in the first month of the following calendar year and record the difference as credit or debit then. Art 19 requires the original VAT invoice issued by the taxable supplier, or an import declaration together with the receipt evidencing payment of import VAT. Retain a method schedule for reviewer sign-off.

### Reverse charge: establish the actual legal supplier

[SD65 arts 2-7](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/1a2d9029-2e2c-494f-a078-6547b88cd42d) addresses qualifying digital goods/services/e-commerce supplied from outside Cambodia by a non-resident without a Cambodian PE. A resident taxpayer receiving a B2B supply accounts for reverse-charge VAT; a qualifying non-resident B2C supplier has a different VAT-only registration/collection route. The annex includes downloads, software, hosting, network support, advice, interactive sites, shopping portals, auctions and referrals. A brand or card descriptor does not establish the supplier's residence, PE or B2B status. Input credit is available only under the law's conditions, and SD49 art 40 concerns reverse-charge VAT paid. Reverse-charge output does not establish an equal input credit automatically. Under [SD49 arts 38-40](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/1adcafd1-44a6-4875-b3e7-349a693b7c9c), resident B2B reverse-charge tax time is the earliest of digital-goods delivery, digital-service performance, payment becoming due or payment being made (art 39(2)). The non-resident supplier rule is separately the earliest of invoice, delivery/performance or payment received (art 39(1)); do not substitute it for the resident rule. Art 40 permits credit for VAT paid under the art 38 reverse-charge mechanism; apply Law arts 68-70 eligibility conditions. Other imported-service/non-resident questions remain R-KH-3 referrals.

### Reconcile and prepare the review output

Maintain separate Output tax, Zero-rated output, Non-taxable/exempt output, Input domestic, Input imports, Digital reverse-charge output and eligible input, adjustments, credit brought forward, and Net VAT fields. Net VAT starts with output less allowable input under [Law art 66](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e); then reconcile prior liabilities and excess credit under [arts 72-74](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e). Excess first offsets prior VAT liabilities, then carries to the following month. Refund eligibility/application is separate: a taxpayer whose primary activity is export needs certified export documents and proper records; ordinary excess continuing at least 3 months permits an application after the third month, with the statutory 20-day application window for the relevant month. SD49 art 20(2) denies a refund where the applicant has not declared taxable supplies. Do not promise an automatic refund. Obtain current refund procedure/account requirements before application.

Map those working-paper fields to the current GDT E-Filing return at https://www.tax.gov.kh, check the period/channel calendar, and retain the acknowledgment/payment reference. No current box numbers are invented. Keep salary/payroll, income-tax withholding, social security, tax/licence payments and genuine financing/internal transfers separate; investigate mixed payments and import VAT separately. Retain the base skill's workbook and bank-to-register reconciliation.

### Supplier pattern library: prompts, never automatic legal conclusions

Every identity below is preserved from the old skill. Confirm the actual transaction, invoice entity and eligibility before using a pattern. The library is illustrative, not a verified supplier register.


### 1 Cambodian banks (qualify the underlying fee)

**Cambodian banks (qualify the underlying fee)**

| Pattern | Treatment | Notes | Source / boundary |
| --- | --- | --- | --- |
| ABA BANK, ABA | Check primary financial service; no blanket exclusion | Only qualifying primary financial services; inspect fee nature | [Law arts 58-63,65,68-70; transaction evidence controls](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e) |
| ACLEDA, ACLEDA BANK | Check primary financial service; no blanket exclusion | Apply the same underlying-service test | [Law arts 58-63,65,68-70; transaction evidence controls](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e) |
| CANADIA BANK, PRINCE BANK | Check primary financial service; no blanket exclusion | Apply the same underlying-service test | [Law arts 58-63,65,68-70; transaction evidence controls](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e) |
| WING, WING BANK | Check primary financial service | Payment method alone does not establish exemption | [Law arts 58-63,65,68-70; transaction evidence controls](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e) |
| ANZ ROYAL, J TRUST ROYAL | Check primary financial service | Apply the same underlying-service test | [Law arts 58-63,65,68-70; transaction evidence controls](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e) |
| INTEREST, INCOME INTEREST | EXCLUDE | Out of scope | [Law arts 58-63,65,68-70; transaction evidence controls](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e) |
| LOAN, REPAYMENT | EXCLUDE | Loan principal, out of scope | [Law arts 58-63,65,68-70; transaction evidence controls](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e) |

### 2 Government and statutory bodies (exclude)

**Government and statutory bodies (exclude)**

| Pattern | Treatment | Notes | Source / boundary |
| --- | --- | --- | --- |
| GDT, GENERAL DEPARTMENT OF TAXATION | EXCLUDE | Tax payment | [Law arts 58-63,65,68-70; transaction evidence controls](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e) |
| CUSTOMS, GDCE | EXCLUDE | Customs duty (import VAT separate) | [Law arts 58-63,65,68-70; transaction evidence controls](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e) |
| MOC, MINISTRY OF COMMERCE | EXCLUDE | Registration/licence fees | [Law arts 58-63,65,68-70; transaction evidence controls](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e) |
| NSSF, SOCIAL SECURITY | EXCLUDE | Social security contribution | [Law arts 58-63,65,68-70; transaction evidence controls](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e) |

### 3 Utilities

**Utilities**

| Pattern | Treatment | Notes | Source / boundary |
| --- | --- | --- | --- |
| EDC, ELECTRICITE DU CAMBODGE | Non-taxable | Electrical power, not limited to residential supply | [Law arts 58-63,65,68-70; transaction evidence controls](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e) |
| PHNOM PENH WATER SUPPLY | Non-taxable | Clean water, not limited to residential supply | [Law arts 58-63,65,68-70; transaction evidence controls](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e) |
| SMART, CELLCARD, METFONE | Domestic 10% | Telecoms | [Law arts 58-63,65,68-70; transaction evidence controls](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e) |

### 4 Insurance (exempt ; exclude)

**Insurance (exempt ; exclude)**

| Pattern | Treatment | Notes | Source / boundary |
| --- | --- | --- | --- |
| FORTE INSURANCE, CAMBODIA RE | EXCLUDE | Insurance services non-taxable; separate any other supply | [Law arts 58-63,65,68-70; transaction evidence controls](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e) |
| INFINITY GENERAL, ASIA INSURANCE | EXCLUDE | Apply the same underlying-service test | [Law arts 58-63,65,68-70; transaction evidence controls](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e) |

### 5 Digital payments

**Digital payments**

| Pattern | Treatment | Notes | Source / boundary |
| --- | --- | --- | --- |
| WING TRANSFER FEE | Check primary financial service; hold pending classification | Check whether the actual fee is a primary financial service | [Law arts 58-63,65,68-70; transaction evidence controls](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e) |
| PI PAY, TRUE MONEY, BAKONG | Check actual service | Apply the same underlying-service test | [Law arts 58-63,65,68-70; transaction evidence controls](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e) |

### 6 SaaS and international services

**SaaS and international services**

| Pattern | Treatment | Notes | Source / boundary |
| --- | --- | --- | --- |
| GOOGLE, MICROSOFT, META, FACEBOOK | Test B2B digital reverse charge | Only a qualifying digital/e-commerce supply by a non-resident without Cambodian PE to the resident taxpayer; confirm invoice entity | [SD65 arts 2-7](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/1a2d9029-2e2c-494f-a078-6547b88cd42d) |
| AWS, AMAZON, ZOOM, SLACK | Test B2B digital reverse charge | Apply the same underlying-service test | [SD65 arts 2-7](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/1a2d9029-2e2c-494f-a078-6547b88cd42d) |
| CANVA, FIGMA, NOTION, OPENAI | Test B2B digital reverse charge | Apply the same underlying-service test | [SD65 arts 2-7](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/1a2d9029-2e2c-494f-a078-6547b88cd42d) |

### 7 Professional services

**Professional services**

| Pattern | Treatment | Notes | Source / boundary |
| --- | --- | --- | --- |
| LAW FIRM, LEGAL, ADVOCATE | Domestic 10% | Credit only with taxable use, valid documents, timing and no blocked expense | [Law arts 58-63,65,68-70; transaction evidence controls](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e) |
| AUDIT, ACCOUNTING, CONSULTANT | Domestic 10% | Same credit conditions; business purpose alone is insufficient | [Law arts 58-63,65,68-70; transaction evidence controls](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e) |

### 8 Property and rent

**Property and rent**

| Pattern | Treatment | Notes | Source / boundary |
| --- | --- | --- | --- |
| RENT, OFFICE RENT | Domestic 10% | Commercial lease with VAT invoice | [Law arts 58-63,65,68-70; transaction evidence controls](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e) |
| RESIDENTIAL RENT | Hold classification | Residential rent exemption not confirmed from opened law | [Law arts 58-63,65,68-70; transaction evidence controls](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e) |

### 9 Payroll (exclude)

**Payroll (exclude)**

| Pattern | Treatment | Notes | Source / boundary |
| --- | --- | --- | --- |
| SALARY, WAGES, BONUS | EXCLUDE | Outside VAT scope | [Law arts 58-63,65,68-70; transaction evidence controls](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e) |
| NSSF CONTRIBUTION | EXCLUDE | Social security | [Law arts 58-63,65,68-70; transaction evidence controls](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e) |

### 10 Internal transfers

**Internal transfers**

| Pattern | Treatment | Notes | Source / boundary |
| --- | --- | --- | --- |
| OWN TRANSFER, INTERNAL | EXCLUDE | Internal movement | [Law arts 58-63,65,68-70; transaction evidence controls](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e) |
| DIVIDEND | EXCLUDE | Out of scope | [Law arts 58-63,65,68-70; transaction evidence controls](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e) |
| CASH WITHDRAWAL, ATM | Hold; obtain cash-use evidence | Default exclude | [Law arts 58-63,65,68-70; transaction evidence controls](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e) |


## Boundary and exception table

| Situation | Action |
|---|---|
| Unknown sale rate, location or counterparty | Hold the classification, obtain place/supply evidence; do not silently impose the former domestic 10% assumption. |
| Missing purchase/VAT invoice, business-use or blocking evidence | No input claimed until established; record the unresolved amount separately. |
| Vehicle/fuel/entertainment | Apply SD49 art 13 and the precise business exception; commercial use alone does not resolve it. |
| Round-number incoming funds | Obtain evidence of sale, capital or loan; no automatic owner-injection exclusion. |
| Cash withdrawal / ATM | Hold; obtain cash-use support rather than call it an expense. |
| Rent | No credit without eligible VAT documentation; the former residential-rent exemption is not confirmed here. |
| Currency / mobile money / statement format | Use actual currency and underlying transaction; Wing, Pi Pay, True Money or Bakong is a payment channel, not a VAT result. ABA/ACLEDA CSV column expectations are illustrative; inspect actual exports. |
| QIP / SEZ / diplomatic / non-resident / special sector | Refer with documents; the ordinary examples do not establish incentive eligibility. |

Internal review triggers preserved from v2.0, not tax-law thresholds: HIGH single transaction USD 5,000 or default tax difference USD 500; MEDIUM concentration above 40% of output or input, or more than 4 conservative defaults. They trigger review, never supply evidence or tax treatment. Record each assumption and its tax effect in the review brief.

## Worked cases

Hypothetical transaction amounts in USD are retained from the old April 2026 examples for classification/arithmetic only; they are not KHR return amounts or an exchange-rate instruction. Source rates and conditions are [Law arts 63,65-70](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e) and [SD65 arts 2-7](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/1a2d9029-2e2c-494f-a078-6547b88cd42d). Dates are scenario inputs.

| Date | Counterparty | Gross movement | VAT-exclusive value / VAT result | Required condition | Source |
|---|---|---|---|---|---|
| 05.04.2026 | XYZ TRADING CO | +1,100 | Sale 1,000; output 100 | Domestic taxable sale, VAT-inclusive price; art 65 | [Law arts 58-70](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e) |
| 10.04.2026 | ACLEDA SUPPLIES | -550 | Purchase 500; eligible input 50 | Valid invoice, taxable use, timely claim, no block; arts 68-70 | [Law arts 58-70](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e) |
| 15.04.2026 | THAI IMPORTS CO | +8,000 | Export 8,000; output 0 | Actual qualifying export with customs/evidence, not name alone; art 65 | [Law arts 58-70](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e) |
| 18.04.2026 | GOOGLE CLOUD | -200 | Reverse-charge output 20; input 20 only if eligible | Qualifying B2B digital supply; reverse-charge VAT paid and input conditions independently satisfied; SD49 arts 38-40 / SD65 arts 6-7 | [Law arts 58-70](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e) |
| 30.04.2026 | ABA BANK | -15 | No output/input for assumed qualifying primary financial service | Actual fee nature confirmed; art 63(9) | [Law arts 58-70](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e) |
| 25.04.2026 | EMPLOYEE SOPHEAK | -800 | Wages outside this VAT computation | Actual employment payment, not supplier service | [Law arts 58-70](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e) |

### Domestic sale and eligible purchase

With the first 2 transactions only, output 100 minus eligible input 50 leaves 50 VAT before prior credits/adjustments. The export adds no output if its evidence is complete. The salary and qualifying bank fee do not generate an input credit.

```oa-check
name: Domestic sale and eligible purchase
inputs:
  gross_sale: 1100
  purchase_gross: 550
steps:
  sale_net: gross_sale / 1.1
  output: gross_sale - sale_net
  purchase_net: purchase_gross / 1.1
  input_credit: purchase_gross - purchase_net
  vat_due: output - input_credit
expected:
  sale_net: 1000
  output: 100
  input_credit: 50
  vat_due: 50
```

### Digital cost with and without taxable-use eligibility

GOOGLE CLOUD 200 creates 20 reverse-charge output under the assumed B2B facts. If that reverse-charge VAT is paid and fully eligible for credit, input 20 leaves 0 net effect. If wholly attributable to non-taxable supplies, input 0 leaves 20 payable. This second result is why the former unconditional Output+Input pattern was unsafe.

```oa-check
name: Digital cost taxable versus non-taxable use
inputs:
  digital_value: 200
  blocked_input: 0
steps:
  reverse_output: digital_value * 0.10
  eligible_input: reverse_output
  net_taxable_use: reverse_output - eligible_input
  net_nontaxable_use: reverse_output - blocked_input
expected:
  reverse_output: 20
  net_taxable_use: 0
  net_nontaxable_use: 20
```

### Mixed-supply residual credit

For a hypothetical eligible common-input pool 1,000, taxable supplies 60,900 and total supplies 100,000, truncate 0.609 to 0.60: recover 600. A separately established wholly non-taxable cost is not made deductible by this ratio. Annual reconciliation remains required. Source: [SD49 arts 14-18](https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/1adcafd1-44a6-4875-b3e7-349a693b7c9c); every amount here is a hypothetical input or derived value.

```oa-check
name: Mixed-supply ratio truncation
inputs:
  common_input: 1000
  taxable_sales: 60900
  total_sales: 100000
steps:
  ratio_hundredths: floor(taxable_sales * 100 / total_sales)
  credit: common_input * ratio_hundredths / 100
expected:
  ratio_hundredths: 60
  credit: 600
```

## When to refuse or refer

- **R-KH-1: QIP certificate.** QIP entities have special VAT exemptions/incentives; escalate with the certificate to a qualified Cambodian practitioner. Lawart 75 domestic production-input zero rating does not validate the whole project or every purchase.
- **R-KH-2: SEZ enterprise.** Special import/export VAT treatment remains outside this ordinary working paper; refer.
- **R-KH-3: non-resident obligations.** Refer the supplier's Cambodian registration/PE/other imported-service obligations. The bounded resident B2B digital reverse-charge treatment above does not complete that analysis.
- Missing supply, invoice, currency, prior-credit, payment or classification evidence: stop the affected computation and report what is missing. Do not file from a bank statement alone.

## Sources

| Source | URL | Read on |
|---|---|---|
| 2023 Law on Taxation, arts 57-80; original Khmer pages 25-32 visually read, full corresponding English reference passages read | https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e | 2026-11-14 |
| SD49,11 March 2024: all 15 Khmer pages visually read, especially arts 11-19 credit,25-28 time/value/adjustment,29 records,33 exports,36-41 digital; OCR used only as transcription aid | https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/1adcafd1-44a6-4875-b3e7-349a693b7c9c | 2026-11-14 |
| SD65,8 April 2021, official-host unofficial English translation: all 9 pages read, arts 1-11 and complete digital/e-commerce annex | https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/1a2d9029-2e2c-494f-a078-6547b88cd42d | 2026-11-14 |
| GDT sub-decree register: SD49 and 65 valid | https://www.tax.gov.kh/en/sub-decree | 2026-11-14 |
| GDT law register: 2023 Law valid | https://www.tax.gov.kh/en/law | 2026-11-14 |
| GDT calendar: October 2026 manual 20 November/online 25 November entries only | https://www.tax.gov.kh/en/ | 2026-11-14 |

Access provenance: the [same-statute English reference](https://embindpp.gov.in/pdf/menu/Tax-Law-Cambodia-2023.pdf), read 2026-11-14 for arts 57-80, is an unofficial translation hosted by the Embassy of India in Phnom Penh. It is disclosed as a reading aid, not an alternative authority; original Khmer governs. Original-language excerpts and complete old-topic/supplier mapping are retained in the external evidence ledger.

Not yet confirmed: current GDT filing box identifiers, mandatory currency conversion instrument/rates, precise primary-financial-service implementing definitions, current refund application/account procedure, current fuel relief overrides, special used-goods method and continuous-supply details, residential-rent exemption, all QIP/SEZ conditions and non-resident obligations beyond the bounded resident B2B digital computation. These are excluded from usable calculations until their operative instruments are read.

Historical unsupported workflow proposals retained for audit, not instructions: unknown sale 10%, unknown location domestic, unknown SaaS 10%, round-number receipts owner injection, USDamounts as-is and KHRconversion at an assumed NBCrate; brand-only blanket exemption; annual mixed-use adjustment without the actual SD49 method; earliest invoice/payment/delivery timing. The former bank statement “minimum viable” meant reconciliation input, never sufficient evidence to file. v2.0 (April 2026) ten-section structure and v1.1 monolithic history are preserved here; v2.1 corrects the legal rules and makes unresolved boundaries explicit.

Built from the law. Written by Codex. Not reviewed by an accountant.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date version is maintained at [openaccountants.com](https://openaccountants.com).

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `cambodia-vat` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/cambodia-vat. If neither is available, confirm every figure against the official source pages cited above before relying on it.
