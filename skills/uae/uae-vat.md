---
name: uae-vat
description: Use this skill whenever asked to prepare, review, or classify transactions for a UAE VAT return (VAT201 form) for any client. Trigger on phrases like "prepare VAT return", "do the VAT", "fill in VAT201", "create the return", "UAE VAT filing", "FTA return", or any request involving UAE VAT filing. Also trigger when classifying transactions for VAT purposes from bank statements, invoices, or other source data. This skill covers the UAE only and only standard VAT-registered persons filing VAT201. VAT groups, profit margin schemes, partial exemption with non-trivial exempt supplies, and Designated Zone goods movement classifications are all in the refusal catalogue. MUST be loaded alongside vat-workflow-base v0.1 or later (for workflow architecture). ALWAYS read this skill before touching any UAE VAT work.
version: 2.7
category: VAT
jurisdiction: AE
tax_year: 2026
last_updated: 2026-11-26
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: vat-gst
type: situation-rules
---

# UAE VAT: ordinary VAT201 returns for 2026

## Scope

Use this Guide for one ordinary registrant's UAE VAT201 return. Registration, ordinary service exports, purchases, invoices and return boxes are covered below. Tax Groups, government entities, charities and the specialist topics under referrals need separate advice. Load `vat-workflow-base` for the workflow. This Guide gives no accountant approval.

## Ask the client first

Obtain the registration certificate, TRN, effective date, assigned tax period and establishments; sales and purchase invoices; supplier residence and place-of-supply facts; evidence of export conditions; payment dates and intentions; private use and employee benefits; customs declarations; gifts; credit notes; old errors and the periods in which credit balances arose. Obtain the latest financial statements for any e-invoicing assessment. Resolve missing facts before filing; do not assume an unknown purchase is recoverable or an unknown sale belongs to Dubai.

## The method, step by step

### Registration and rate

| Test | Rule and conditions | Official source |
|---|---|---|
| Mandatory registration | A person resident in the UAE or another Implementing State registers when Article 19 supplies exceeded AED 375,000 in the previous 12 months or are expected to exceed it in the next 30 days. Count taxable goods/services, concerned imports, acquired-business supplies and related-party supplies where Article 19 requires; exclude supplies of capital assets. Exactly AED 375,000 alone does not trigger the test. The FTA may grant an exception on request for exclusively zero-rated supplies; it is not automatic. | VAT Law arts 13, 15, 19-20: https://tax.gov.ae/Datafolder/Files/Legislation/2025/Federal%20Decree-Law%20No.%208%20of%202017%20and%20amendments%20-%20publishing%2028%2011%202025.pdf; Regulation art 7: https://tax.gov.ae/Datafolder/Files/Legislation/2026/Law-No-8-of-2017-and-its-amendments--09-2026.pdf |
| Application and effective date | Apply within 30 days of becoming required. Under the look-back test, registration normally starts on the first day of the following month; under the look-forward test, on the date reasonable grounds exist. Both permit an earlier date agreed with the FTA and apply whether or not the person applies. A late registrant accounts for taxable supplies/imports within its registration liability; do not tax all historic trading merely because it preceded the application. | Regulation art 7(2)-(7): https://tax.gov.ae/Datafolder/Files/Legislation/2026/Law-No-8-of-2017-and-its-amendments--09-2026.pdf |
| Non-resident | A person with no residence in the UAE or an Implementing State must register for UAE supplies when nobody else must pay the VAT; no turnover threshold applies. The FTA registers it from the start of those supplies or an earlier agreed date. GCC residence/implementing-state questions are referred below. | VAT Law art 13(2): https://tax.gov.ae/Datafolder/Files/Legislation/2025/Federal%20Decree-Law%20No.%208%20of%202017%20and%20amendments%20-%20publishing%2028%2011%202025.pdf; Regulation art 7(6): https://tax.gov.ae/Datafolder/Files/Legislation/2026/Law-No-8-of-2017-and-its-amendments--09-2026.pdf |
| Voluntary registration | An otherwise non-obliged person may apply when Article 19 supplies or qualifying taxable expenses exceeded AED 187,500 in the previous 12 months, demonstrated at month-end, or are expected to exceed it in the next 30 days. Expenses must be standard-rated, incurred in the UAE by a UAE-resident person. Prove UAE business activity and intended Article 54(1)(a)-(c) supplies to the FTA; supply the evidence it requires. Effective date: first day of the month after application or an earlier date requested and agreed. Registration does not itself prove input recovery. | VAT Law art 17: https://tax.gov.ae/Datafolder/Files/Legislation/2025/Federal%20Decree-Law%20No.%208%20of%202017%20and%20amendments%20-%20publishing%2028%2011%202025.pdf; Regulation art 8: https://tax.gov.ae/Datafolder/Files/Legislation/2026/Law-No-8-of-2017-and-its-amendments--09-2026.pdf |
| Standard rate | 5% on taxable supplies/imports unless a statutory different treatment applies. A commercial lease is ordinarily standard-rated. Do not assume all receipts or all foreign customers have this treatment. | VAT Law art 3: https://tax.gov.ae/Datafolder/Files/Legislation/2025/Federal%20Decree-Law%20No.%208%20of%202017%20and%20amendments%20-%20publishing%2028%2011%202025.pdf; commercial-property examples, FTA Returns Guide p14: https://tax.gov.ae/DataFolder/Files/Pdf/VAT%20Returns%20User%20GuideEnglishV40%2015%2008%202021%20SEP2021.pdf |

### Classify sales

For ordinary service exports under Regulation Article 31(1)(a), zero rating requires **all** of these: the recipient has no residence in an Implementing State and is outside the UAE when the work is performed; no direct connection to UAE real estate/improvements or movable assets in the UAE when performed; and no UAE/Designated Zone performance under VAT Law Articles 30(3)-(8) and 31. A presence of less than 30 days counts as outside only when not effectively connected to the supply. Article 31(3) denies this route when it is reasonably foreseeable that another person in the UAE will receive the services and cannot fully recover the input tax. Services actually performed outside the Implementing States, or arranging those services, have the separate Article 31(1)(b) route. [Regulation art 31](https://tax.gov.ae/Datafolder/Files/Legislation/2026/Law-No-8-of-2017-and-its-amendments--09-2026.pdf).

A transfer of a whole or independent business part to a taxable person to continue that business is not a supply; nor is issuing/selling a voucher unless consideration exceeds its advertised monetary value. Pure salary, dividend or loan-principal movements are not evidence of a taxable sale by themselves: establish whether any separate goods/services were supplied. [VAT Law arts 2, 5-7](https://tax.gov.ae/Datafolder/Files/Legislation/2025/Federal%20Decree-Law%20No.%208%20of%202017%20and%20amendments%20-%20publishing%2028%2011%202025.pdf). Other zero-rated/exempt classifications are referred below.

### Purchases and input recovery

Input tax must relate to taxable supplies (including zero-rated supplies) or overseas supplies that would be taxable in the UAE. Article 54(1)(c)'s specified overseas exempt-equivalent supplies need separate advice. Keep the tax invoice, or legally permitted alternative; for imported goods retain invoices/import documents, and for imported services retain supplier invoices. Retain electronic invoices in the system when required or issued electronically. Claim in the first period satisfying Article 55, or the subsequent period if missed. [VAT Law arts 54-55](https://tax.gov.ae/Datafolder/Files/Legislation/2025/Federal%20Decree-Law%20No.%208%20of%202017%20and%20amendments%20-%20publishing%2028%2011%202025.pdf).

Recovery relates to consideration paid; an intention to pay **before six months expire after the agreed payment date** is treated as payment. An unpaid invoice without that intention does not qualify. [Regulation art 54(1)-(2)](https://tax.gov.ae/Datafolder/Files/Legislation/2026/Law-No-8-of-2017-and-its-amendments--09-2026.pdf).

| Cost | Treatment for an ordinary business | Official source |
|---|---|---|
| Non-employee entertainment | Block hospitality for customers, potential customers, officials, shareholders/owners and investors: accommodation, food/drink outside the normal course of a meeting, shows/events and pleasure trips. Ordinary meeting refreshments are not entertainment; other recovery conditions still apply. | Regulation art 53(1)(a),(2)(a): https://tax.gov.ae/Datafolder/Files/Legislation/2026/Law-No-8-of-2017-and-its-amendments--09-2026.pdf |
| Motor vehicles | Block purchased/rented/leased business vehicles available for personal use by anyone. The definition covers road vehicles designed/adapted for at most 10 people including the driver, excluding trucks, forklifts, hoists and similar vehicles. Licensed taxis, vehicles registered and used for emergency services, and vehicles rented to customers in a rental business are excepted from the private-availability rule. Ordinary recovery conditions still apply. | Regulation art 53(1)(b),(2)(b),(4): https://tax.gov.ae/Datafolder/Files/Legislation/2026/Law-No-8-of-2017-and-its-amendments--09-2026.pdf |

Free personal employee benefits, their exceptions and the October changes require the referral below. Do not claim merely because a benefit is in an employment contract.

From 1 January 2026 Article 54(bis) requires the FTA to reject input deduction where a supply chain involved tax evasion and the taxpayer knew; it may reject where the taxpayer should have known. Failure to perform the FTA's prescribed validity/integrity checks is part of that test. Before input deduction for supplies within the October supplier-check regime, obtain the specialist review below; this Guide does not execute Decision 13's supplier, supply, timing, policy or exception tests. [VAT Law art 54(bis)](https://tax.gov.ae/Datafolder/Files/Legislation/2025/Federal%20Decree-Law%20No.%208%20of%202017%20and%20amendments%20-%20publishing%2028%2011%202025.pdf).

### Imported services and goods

A taxable person importing concerned goods/services for its business accounts for due VAT as a deemed supply to itself. **From 1 January 2026 it need not issue a self-invoice**; retain the supplier invoice for imported services. Establish residence, place of supply and liability; absence or presence of a TRN alone does not settle reverse charge. Ordinary domestic standard-rated purchase VAT goes to Box 9; imported-services output tax goes to Box 3 and eligible recovery to Box 10. Customs goods use Boxes 6/7 and eligible recovery in Box 10. Domestic special reverse charges are referred below. [VAT Law arts 48(1), 55(1)(a)](https://tax.gov.ae/Datafolder/Files/Legislation/2025/Federal%20Decree-Law%20No.%208%20of%202017%20and%20amendments%20-%20publishing%2028%2011%202025.pdf); [FTA Returns Guide pp15-23](https://tax.gov.ae/DataFolder/Files/Pdf/VAT%20Returns%20User%20GuideEnglishV40%2015%2008%202021%20SEP2021.pdf).

### Gifts and invoices

Free business goods can be deemed supplies where input tax was recovered. Samples/commercial gifts do not count as deemed supplies when their value per recipient in the preceding 12-month period does not exceed AED 500. For an ordinary supplier, total output tax on deemed supplies in that period is relieved up to AED 2,000; only the excess is payable. The government/charity threshold is outside scope. A taxable deemed supply belongs in Box 1 and requires an invoice delivered to the recipient or retained if there is none. [VAT Law arts 11-12, 65(2)](https://tax.gov.ae/Datafolder/Files/Legislation/2025/Federal%20Decree-Law%20No.%208%20of%202017%20and%20amendments%20-%20publishing%2028%2011%202025.pdf); [Regulation art 5](https://tax.gov.ae/Datafolder/Files/Legislation/2026/Law-No-8-of-2017-and-its-amendments--09-2026.pdf); [FTA Returns Guide p14](https://tax.gov.ae/DataFolder/Files/Pdf/VAT%20Returns%20User%20GuideEnglishV40%2015%2008%202021%20SEP2021.pdf).

Ordinary tax invoices are due within 14 days of supply; simplified invoices on the date of supply; summary invoices are issued and delivered within 14 days after the supply month ends, subject to any other FTA-specified case. Convert foreign currency to AED at the Central Bank-approved rate on the supply date. [VAT Law arts 67, 69](https://tax.gov.ae/Datafolder/Files/Legislation/2025/Federal%20Decree-Law%20No.%208%20of%202017%20and%20amendments%20-%20publishing%2028%2011%202025.pdf); [Regulation art 59(13)](https://tax.gov.ae/Datafolder/Files/Legislation/2026/Law-No-8-of-2017-and-its-amendments--09-2026.pdf).

A full invoice needs “Tax Invoice”; supplier name/address/TRN; registered recipient name/address/TRN; sequential or unique identifying number; issue and (if different) supply dates; description; each item's unit price, quantity/volume, rate and amount in AED; discounts; gross amount; VAT in AED and conversion rate; and the recipient-accounting statement and legal reference for a reverse-charge supply. [Regulation art 59(1)](https://tax.gov.ae/Datafolder/Files/Legislation/2026/Law-No-8-of-2017-and-its-amendments--09-2026.pdf).

Outside reverse charge and mandatory/voluntary Electronic Invoicing, simplified invoices may be used for an unregistered recipient or a registered recipient whose consideration is at most AED 10,000. They require “Tax Invoice”, supplier name/address/TRN, issue date, description, total consideration and VAT in AED. FTA directions may still require a full invoice. With sufficient records, wholly zero-rated supplies ordinarily need no invoice; Article 59(16) switches off that exemption and the simplified rules for Electronic Invoices. Buyer-created invoices and electronic-system compliance are referred below. From 1 October 2026 the credit note must say “Tax Credit Note”; full credit-note requirements still need review. [Regulation arts 59(2)-(5),(15)-(16), 60(1)(a)](https://tax.gov.ae/Datafolder/Files/Legislation/2026/Law-No-8-of-2017-and-its-amendments--09-2026.pdf).

### VAT201 and filing

Use the FTA's 2021 VAT Returns Guide for the following box mechanics only. Its old penalties and unlimited carry-forward wording are superseded by later law. Current authenticated EmaraTax screens/payment references are not proven here: arrange that check before submission. Amounts are in AED; reconcile to invoices and customs, obtain authorised-signatory declaration/submission and retain confirmation. Submission does not prove payment. [FTA Returns Guide pp8-27](https://tax.gov.ae/DataFolder/Files/Pdf/VAT%20Returns%20User%20GuideEnglishV40%2015%2008%202021%20SEP2021.pdf).

| Box | Entry | Official source |
|---|---|---|
| 1a-1g | Standard-rated net sales and VAT by Emirate: Abu Dhabi, Dubai, Sharjah, Ajman, Umm Al Quwain, Ras Al Khaimah, Fujairah. For a UAE fixed establishment use the one most closely connected to the supply; without a fixed establishment but with a UAE place of establishment use that place; non-established businesses use where the supply is received. The separate e-commerce exception is referred below. | Guide pp13-14: https://tax.gov.ae/DataFolder/Files/Pdf/VAT%20Returns%20User%20GuideEnglishV40%2015%2008%202021%20SEP2021.pdf; Regulation art 72(2)-(6): https://tax.gov.ae/Datafolder/Files/Legislation/2026/Law-No-8-of-2017-and-its-amendments--09-2026.pdf |
| 2 | Tourist refunds, prepopulated for enrolled retailers; specialist scheme referred below. | Guide p15: https://tax.gov.ae/DataFolder/Files/Pdf/VAT%20Returns%20User%20GuideEnglishV40%2015%2008%202021%20SEP2021.pdf |
| 3 | Reverse-charge supplies' full net value and output VAT, excluding customs imports reported in Box 6. | Guide pp15-16: https://tax.gov.ae/DataFolder/Files/Pdf/VAT%20Returns%20User%20GuideEnglishV40%2015%2008%202021%20SEP2021.pdf |
| 4 | Zero-rated net supplies. | Guide p16: https://tax.gov.ae/DataFolder/Files/Pdf/VAT%20Returns%20User%20GuideEnglishV40%2015%2008%202021%20SEP2021.pdf |
| 5 | Exempt net supplies. | Guide pp16-17: https://tax.gov.ae/DataFolder/Files/Pdf/VAT%20Returns%20User%20GuideEnglishV40%2015%2008%202021%20SEP2021.pdf |
| 6 and 7 | Customs imports paid via the return: check prepopulated net value and VAT in 6; justify positive/negative corrections in 7, including imports not subject to the default standard rate. | Guide pp17-18: https://tax.gov.ae/DataFolder/Files/Pdf/VAT%20Returns%20User%20GuideEnglishV40%2015%2008%202021%20SEP2021.pdf |
| 9 | Standard-rated purchases' net amounts and VAT eligible for recovery; exclude blocked amounts. | Guide pp21-22: https://tax.gov.ae/DataFolder/Files/Pdf/VAT%20Returns%20User%20GuideEnglishV40%2015%2008%202021%20SEP2021.pdf |
| 10 | Recoverable VAT declared as output in 3/6/7; show full net expense value when entitled to some recovery, with only eligible VAT. Do not recover blocked tax just to cancel the output entry. | Guide p23: https://tax.gov.ae/DataFolder/Files/Pdf/VAT%20Returns%20User%20GuideEnglishV40%2015%2008%202021%20SEP2021.pdf |
| 8 and 11 | Automatic output and input totals respectively. | Guide pp18,24: https://tax.gov.ae/DataFolder/Files/Pdf/VAT%20Returns%20User%20GuideEnglishV40%2015%2008%202021%20SEP2021.pdf |
| 12-14 | Due tax in 12, recoverable tax in 13, net payable/recoverable difference in 14. | Guide pp24-25: https://tax.gov.ae/DataFolder/Files/Pdf/VAT%20Returns%20User%20GuideEnglishV40%2015%2008%202021%20SEP2021.pdf |
| 15 | Refund choice; selecting yes requires a separate VAT311 after VAT201. Carry-forward remains subject to the current statutory time limit below. | Guide p25: https://tax.gov.ae/DataFolder/Files/Pdf/VAT%20Returns%20User%20GuideEnglishV40%2015%2008%202021%20SEP2021.pdf |

Credit notes issued/received reduce the relevant sales/purchase entries. Output Adjustment columns are for bad-debt relief and relevant commercial-property tax already paid by the buyer; input Adjustment columns are for supplier bad-debt relief, annual apportionment and capital-asset adjustments. The latter specialist computations are referred below. [FTA Returns Guide pp11-12,19-20](https://tax.gov.ae/DataFolder/Files/Pdf/VAT%20Returns%20User%20GuideEnglishV40%2015%2008%202021%20SEP2021.pdf).

For supplier bad-debt relief, a buyer reduces previously deducted input tax where the supplier has validly reduced its output tax and notified the buyer of the write-off, the buyer received the goods/services and deducted the input tax, and the consideration remains unpaid in whole or part for over six months. Reduce tax on the amount written off; this is separate from the six-month payment-intention test. [VAT Law art 64](https://tax.gov.ae/Datafolder/Files/Legislation/2025/Federal%20Decree-Law%20No.%208%20of%202017%20and%20amendments%20-%20publishing%2028%2011%202025.pdf).

Standard tax periods are three calendar months, but the FTA may assign shorter/longer periods. File every period, including nil periods, and a final return on deregistration. The return **and payment** must reach the FTA by the 28th day after period-end or another FTA-directed date; the Returns Guide extends weekend/national-holiday deadlines to the next business day. [Regulation arts 62, 64](https://tax.gov.ae/Datafolder/Files/Legislation/2026/Law-No-8-of-2017-and-its-amendments--09-2026.pdf); [FTA Returns Guide pp4-5,29](https://tax.gov.ae/DataFolder/Files/Pdf/VAT%20Returns%20User%20GuideEnglishV40%2015%2008%202021%20SEP2021.pdf).

### Errors and credit balances

If payable tax was understated by **more than AED 10,000**, disclose within 20 business days of discovery. For **AED 10,000 or less**, use the earliest previous-period return not yet due or the discovery-period return; where no return can correct it, disclose within 20 business days. An overstatement may be voluntarily disclosed. [Tax Procedures Regulation art 10](https://tax.gov.ae/Datafolder/Files/Legislation/Cabinet%20Decision%20No.%2074%20of%202023%20on%20Executive%20Regulation%20of%20Federal%20Decree-Law%20No.%2028%20of%202022%20on%20Tax%20Procedures%20-%20For%20Publishing.pdf); [Tax Procedures Law art 10(3)](https://tax.gov.ae/Datafolder/Files/Legislation/2025/Federal%20Decree-Law%20No.%2028%20of%202022%20-%20publishing%2003%2012%202025.pdf).

From 1 January 2026, VAT Law Article 74 offsets excess recoverable VAT against payable tax/penalties and limits unused carry-forward to five years from the end of the period **in which the excess arose**, after which the right lapses. The refund application has its own clock under Tax Procedures Law Article 38(2): five years from the end of the period in which excess payment occurred, the return/disclosure was submitted or assessment issued, or the credit otherwise arose, as applicable. Do not assume those are the same dates. Article 38(3)-(4) allows one year for a late-arising FTA-decision credit or 90 days for other late-arising credits where they arise after the five years or in its final 90 days. [VAT Law art 74](https://tax.gov.ae/Datafolder/Files/Legislation/2025/Federal%20Decree-Law%20No.%208%20of%202017%20and%20amendments%20-%20publishing%2028%2011%202025.pdf); [Tax Procedures Law art 38](https://tax.gov.ae/Datafolder/Files/Legislation/2025/Federal%20Decree-Law%20No.%2028%20of%202022%20-%20publishing%2003%2012%202025.pdf).

Transitional balances whose five-year period had already elapsed may be refunded/used within one year from 1 January 2026. The linked transitional disclosure may be made within two years of the refund application only while the FTA has not decided it. Obtain advice before applying these exceptional rules. [Decree-Law 17/2025 art 3, reproduced in Tax Procedures Law footnotes 12 and 15](https://tax.gov.ae/Datafolder/Files/Legislation/2025/Federal%20Decree-Law%20No.%2028%20of%202022%20-%20publishing%2003%2012%202025.pdf).

## Boundary and exception table

| Facts | Result | Official source |
|---|---|---|
| Foreign-company director visits Dubai for 10 days, unrelated to the service | The short presence does not prevent zero rating if **every** Article 31(1)(a) condition and the Article 31(3) exclusion test are satisfied. | Regulation art 31: https://tax.gov.ae/Datafolder/Files/Legislation/2026/Law-No-8-of-2017-and-its-amendments--09-2026.pdf |
| Valuation of a Dubai warehouse for a foreign customer | Direct UAE-real-estate connection defeats ordinary service-export zero rating. Foreseeable receipt by UAE staff who cannot fully recover VAT also defeats the Article 31(1)(a) route. | Regulation art 31: https://tax.gov.ae/Datafolder/Files/Legislation/2026/Law-No-8-of-2017-and-its-amendments--09-2026.pdf |
| Registered-customer ordinary invoice of AED 10,000 versus AED 10,001 (computed boundary: 10,000 + 1) | Simplified may be used at the first amount; full at the second. Reverse charge, Electronic Invoicing and FTA directions remain excluded as above. | Regulation art 59: https://tax.gov.ae/Datafolder/Files/Legislation/2026/Law-No-8-of-2017-and-its-amendments--09-2026.pdf |
| Pool car taken home versus pickup truck/forklift | Personal availability blocks the car; verify that the pickup is legally a truck. A truck/forklift is excluded from the motor-vehicle definition, but still needs all other recovery conditions. | Regulation art 53: https://tax.gov.ae/Datafolder/Files/Legislation/2026/Law-No-8-of-2017-and-its-amendments--09-2026.pdf |
| Client lunch versus tea/sandwiches in a normal business meeting | Entertainment lunch is blocked; ordinary meeting refreshments are not entertainment. Ordinary recovery conditions still apply. | Regulation art 53: https://tax.gov.ae/Datafolder/Files/Legislation/2026/Law-No-8-of-2017-and-its-amendments--09-2026.pdf |
| Supplier write-off notice; invoice unpaid 7 months after supply | Reduce previously recovered input VAT only when **all** Article 64(2) conditions above hold. | VAT Law art 64: https://tax.gov.ae/Datafolder/Files/Legislation/2025/Federal%20Decree-Law%20No.%208%20of%202017%20and%20amendments%20-%20publishing%2028%2011%202025.pdf |

## Worked cases

**Case 1: mandatory registration.** A Dubai mainland trading LLC, not registered, has taxable supplies of AED 390,000 in the 12 months to 30 June 2026. That exceeds AED 375,000, so it must apply within 30 days of becoming required to register. The FTA registers it from the first day of the month after the month in which it became required to register, or an earlier date agreed with the FTA, whether or not it applies, and it owes VAT on its taxable supplies from that date. A late application is a penalty of AED 10,000.

**Case 2: voluntary registration.** Assume a UAE-resident start-up carries on Business in the UAE and proves to the FTA its intention to make supplies within VAT Law Article 54(1)(a)-(c). Its qualifying Standard-Rated expenses incurred in the UAE are AED 200,000 in the last 12 months, and the Article 8(5)-(6) evidence and eligibility requirements are satisfied. This exceeds AED 187,500 for voluntary registration; expenses alone do not trigger mandatory registration. Any input recovery separately requires the ordinary Article 55 conditions, qualifying use and applicable recovery restrictions; registration alone does not establish recovery.

**Case 3: reverse charge on software.** A registered Dubai consultancy pays a US software company AED 3,672 for a subscription. Assume the supplier has no UAE place of residence, no UAE TRN and charges no VAT. Box 3: amount AED 3,672, VAT 3,672 x 5% = AED 183.60. Assume all ordinary input-recovery and evidence/payment conditions are met. Box 10: the same amounts, because the consultancy makes only taxable supplies. Net effect nil. For a supply received after 1 January 2026 no self-invoice is issued; the supplier's invoice is kept.

**Case 4: a quarterly return.** Same consultancy, quarter 1 July to 30 September 2026. Assume the overseas service satisfies every Article 31 export condition, no anti-avoidance exception applies, and the tax invoices, payment intention and ordinary input-recovery conditions are met:

| Line | Amount (AED) | VAT on return (AED) | Box | Source |
| --- | --- | --- | --- | --- |
| Services to Dubai clients | 400,000 | 20,000 | 1b | https://tax.gov.ae/Datafolder/Files/Legislation/2025/Federal%20Decree-Law%20No.%208%20of%202017%20and%20amendments%20-%20publishing%2028%2011%202025.pdf; form boxes https://tax.gov.ae/DataFolder/Files/Pdf/VAT%20Returns%20User%20GuideEnglishV40%2015%2008%202021%20SEP2021.pdf |
| Services to a foreign client outside the UAE (zero-rated) | 100,000 | 0 | 4 | https://tax.gov.ae/Datafolder/Files/Legislation/2025/Federal%20Decree-Law%20No.%208%20of%202017%20and%20amendments%20-%20publishing%2028%2011%202025.pdf; form boxes https://tax.gov.ae/DataFolder/Files/Pdf/VAT%20Returns%20User%20GuideEnglishV40%2015%2008%202021%20SEP2021.pdf |
| Software from US supplier (Case 3) | 3,672 | 183.60 | 3 and 10 | https://tax.gov.ae/Datafolder/Files/Legislation/2025/Federal%20Decree-Law%20No.%208%20of%202017%20and%20amendments%20-%20publishing%2028%2011%202025.pdf; form boxes https://tax.gov.ae/DataFolder/Files/Pdf/VAT%20Returns%20User%20GuideEnglishV40%2015%2008%202021%20SEP2021.pdf |
| Local business purchases with tax invoices | 200,000 | 10,000 | 9 | https://tax.gov.ae/Datafolder/Files/Legislation/2025/Federal%20Decree-Law%20No.%208%20of%202017%20and%20amendments%20-%20publishing%2028%2011%202025.pdf; form boxes https://tax.gov.ae/DataFolder/Files/Pdf/VAT%20Returns%20User%20GuideEnglishV40%2015%2008%202021%20SEP2021.pdf |
| Client dinner (blocked, not reported) | 1,200 | 0 | none | https://tax.gov.ae/Datafolder/Files/Legislation/2025/Federal%20Decree-Law%20No.%208%20of%202017%20and%20amendments%20-%20publishing%2028%2011%202025.pdf; form boxes https://tax.gov.ae/DataFolder/Files/Pdf/VAT%20Returns%20User%20GuideEnglishV40%2015%2008%202021%20SEP2021.pdf |

Box 12 = 20,000 + 183.60 = 20,183.60. Box 13 = 10,000 + 183.60 = 10,183.60. Box 14 = 20,183.60 - 10,183.60 = 10,000. The return and AED 10,000 must reach the FTA by 28 October 2026.

For Case 3, compare the same taxable imported service used wholly for taxable business supplies with one whose input tax is blocked as a free personal staff benefit, with no exception. Output VAT remains AED 183.60 in both; full recovery leaves nil payable, whereas blocked recovery leaves AED 183.60 payable. Decide from the use and exceptions, not from the nil-net assumption.

```oa-check
name: Full business recovery versus personal-benefit block on imported service (2026)
inputs:
  import_value: 3672
  rate: 0.05
steps:
  - due_tax: import_value * rate
  - payable_if_fully_recoverable: due_tax - due_tax
  - payable_if_recovery_blocked: due_tax
expected:
  due_tax: 183.60
  payable_if_fully_recoverable: 0.00
  payable_if_recovery_blocked: 183.60
```

```oa-check
name: Reverse charge on a software subscription, Case 3 (2026)
inputs:
  subscription: 3672
  rate: 0.05
steps:
  - box_3_vat: subscription * rate
  - box_10_vat: box_3_vat
  - net_effect: box_3_vat - box_10_vat
expected:
  box_3_vat: 183.60
  box_10_vat: 183.60
  net_effect: 0.00
```

```oa-check
name: Quarterly VAT201, Case 4 (quarter to 30 September 2026)
inputs:
  local_sales: 400000
  reverse_charge_base: 3672
  local_purchases: 200000
  rate: 0.05
steps:
  - box_1b_vat: local_sales * rate
  - box_3_vat: reverse_charge_base * rate
  - box_9_vat: local_purchases * rate
  - box_12: box_1b_vat + box_3_vat
  - box_13: box_9_vat + box_3_vat
  - box_14: box_12 - box_13
expected:
  box_12: 20183.60
  box_13: 10183.60
  box_14: 10000.00
```

**Case 5: gift limit.** In the 12 months to 31 August 2026 a business gives commercial gifts of goods on which it recovered input tax. One customer receives goods costing AED 400: no deemed supply (not above AED 500). Another receives goods costing AED 700: the recipient gift exemption does not apply. Test the separate AED 2,000 aggregate output-tax relief before charging/reporting payable deemed-supply VAT; the facts do not state the supplier’s other deemed supplies. Do not infer payable VAT merely from the AED 700 gift.

**Case 6: correcting an error.** In September 2026 a business finds it under-declared output tax of AED 12,000 in the quarter to 31 March 2026. That is above AED 10,000, so it files a voluntary disclosure within 20 business days of finding the error. If the difference had been AED 8,000 it would use the earliest eligible not-yet-due return or discovery-period return; if neither is available, it would disclose within 20 business days.

## When to refuse or refer

For **each** topic below: **Check this point with one of our partner accountants.** Do not execute these methods from this Guide.

- **Special taxpayers and places:** Tax Groups (including intra-group/consolidation issues), government entities and charities; Designated Zone identification, residence, goods movements/consumption and service/shipping exceptions; GCC implementing-state transactions; e-commerce Emirate reporting.
- **Special sale classifications:** exports of goods; international transport and related means/services; investment precious metals; new, charitable or converted residential buildings; residential-sale/lease exemptions; bare land; margin-based financial services and life insurance; local passenger transport; education; healthcare and related goods; crude oil/natural gas. Composite supplies and the October amendment also need classification advice. The list identifies topics, not automatic exemptions or zero rates.
- **Special purchase methods:** partial-exemption apportionment (including the future method), capital-asset scope/adjustments (including the old building example of AED 5,000,000 excluding VAT, on which VAT is payable, with a useful life of 10 years or more), oil/gas/hydrocarbon and other domestic reverse charges; tourist refunds; profit margin eligibility, margin base/purchase costs, documents and notification.
- **Employee benefits:** free personal goods/services; labour-law, health-insurance and deemed-supply exceptions; contractual/documented-policy cases for transport, food/drink, accommodation, temporary new-starter accommodation, phones/internet and parking. The changes from 1 October 2026 and historical wording require separate review; do not execute the former shortened exceptions here.
- **Supplier checks:** Decision 13 of 2026 supplier identity, business location, risk indicators, bank evidence, public information, commercial reasons, payment/pricing, licensed activity, goods authenticity/ownership, intermediaries, third-party/foreign-bank payments, first dealing/renewals, retained evidence/policy and small-supply exceptions. Resolve these **before** taking input credit where applicable.
- **Cash payments:** the October input-tax restriction depends on a Ministerial decision setting the amount and controls; that decision was not established. Do not infer a safe cash amount or either recovery result.
- **Invoices:** buyer-created arrangements, electronic invoice issue/transmission/retention, full credit-note particulars and zero-rated/electronic exceptions outside the ordinary rules above. Electronic-invoicing scope, revenue, pilot/voluntary participation, provider and implementation dates, consumer-only exclusions and separate invoice/credit-note/system/data penalties require current confirmation. The MoF Decision 66 PDF has publication-dependent commencement and unfilled publication dates; this Guide does not establish its gazette date or an operative amended timetable.
- **Penalties and disputes:** historical and current registration/deregistration, return/payment, incorrect return, voluntary disclosure/audit, records/Arabic, tax-record changes, displayed prices, margin notification, invoice/credit-note, Designated Zone and import penalties; notices, audits, objections and reconsiderations. The consolidated penalty decision dates the new tables to 14 April 2026; transition for earlier violations is not settled here. Case 1's AED 10,000 late-registration figure is the current Table 1 item 3 amount, not a computation of every possible penalty. [https://tax.gov.ae/Datafolder/Files/Legislation/2025/Cabinet%20Decision%20No.%2040%20of%202017%20and%20its%20amendments%20-%20publishing%2011%202025.pdf](https://tax.gov.ae/Datafolder/Files/Legislation/2025/Cabinet%20Decision%20No.%2040%20of%202017%20and%20its%20amendments%20-%20publishing%2011%202025.pdf).
- **Historic periods and portal:** apply the period's operative law. Pre-2026 reverse-charge self-invoices and pre-October employee-benefit wording remain unverified historical methods. Current signed-in EmaraTax labels, declaration, payment reference and successful receipt of payment need separate confirmation.

## Filing and record keeping

Keep supplies/imports, issued/received invoices and credit notes or permitted alternatives, non-business-use and blocked-purchase records, exports, corrections/adjustments and the tax account. Retain for five years following the relevant tax period, **15 years for VAT real-estate records**. Add four years (or until final settlement if later) for disputes; four years for an ongoing audit or timely audit notice. A fifth-year voluntary disclosure has an additional one-year period from submission. Do not destroy records while an extension applies. The FTA may request Arabic translations, approved under the translation law and within its specified period. [VAT Law art 78](https://tax.gov.ae/Datafolder/Files/Legislation/2025/Federal%20Decree-Law%20No.%208%20of%202017%20and%20amendments%20-%20publishing%2028%2011%202025.pdf); [Regulation art 71](https://tax.gov.ae/Datafolder/Files/Legislation/2026/Law-No-8-of-2017-and-its-amendments--09-2026.pdf); [Tax Procedures Regulation arts 3-5](https://tax.gov.ae/Datafolder/Files/Legislation/Cabinet%20Decision%20No.%2074%20of%202023%20on%20Executive%20Regulation%20of%20Federal%20Decree-Law%20No.%2028%20of%202022%20on%20Tax%20Procedures%20-%20For%20Publishing.pdf).

## Sources

The prior completed official-source reads and independent partial-scope review of 1 November 2026 are reused for unchanged claims. On 26 November the retained sentences and necessary neighbouring conditions were checked against the same authority-hosted bytes; fingerprints matched. English statutory texts identify themselves as unofficial translations. No full UAE-law or current-portal review is claimed.

| Source | Scope actually used | Read date |
|---|---|---|
| [VAT Law, consolidated](https://tax.gov.ae/Datafolder/Files/Legislation/2025/Federal%20Decree-Law%20No.%208%20of%202017%20and%20amendments%20-%20publishing%2028%2011%202025.pdf) | Arts 2-7, 11-20, 48, 54-55, 64-69, 74, 78; amendment heading/effective notes | 2026-11-01 completed read reused; 2026-11-26 retained sentences/conditions checked |
| [VAT Executive Regulation, consolidated September 2026](https://tax.gov.ae/Datafolder/Files/Legislation/2026/Law-No-8-of-2017-and-its-amendments--09-2026.pdf) | Arts 5, 7-8, 31, 53-54, 59-60, 62, 64, 71-72 and amendment dates; no apportionment method | 2026-11-01 completed read reused; 2026-11-26 retained sentences/conditions checked |
| [Tax Procedures Regulation, Decision 74/2023](https://tax.gov.ae/Datafolder/Files/Legislation/Cabinet%20Decision%20No.%2074%20of%202023%20on%20Executive%20Regulation%20of%20Federal%20Decree-Law%20No.%2028%20of%202022%20on%20Tax%20Procedures%20-%20For%20Publishing.pdf) | Arts 3-5, 10: records, extensions, Arabic and errors | 2026-11-01 completed read reused; 2026-11-26 retained sentences/conditions checked |
| [Tax Procedures Law, consolidated](https://tax.gov.ae/Datafolder/Files/Legislation/2025/Federal%20Decree-Law%20No.%2028%20of%202022%20-%20publishing%2003%2012%202025.pdf) | Arts 10(3), 38, 46(6), transitional footnotes 12 and 15 | 2026-11-01 completed read reused; 2026-11-26 credit-balance clocks and transition checked |
| [FTA VAT Returns Guide, August 2021](https://tax.gov.ae/DataFolder/Files/Pdf/VAT%20Returns%20User%20GuideEnglishV40%2015%2008%202021%20SEP2021.pdf) | Period/deadline pp4-5; boxes and workflow pp8-27; final return p29; superseded penalty/carry-forward text excluded | 2026-11-01 completed read reused; 2026-11-26 retained box sentences checked |
| [Consolidated penalties, Decision 40/2017 as amended](https://tax.gov.ae/Datafolder/Files/Legislation/2025/Cabinet%20Decision%20No.%2040%20of%202017%20and%20its%20amendments%20-%20publishing%2011%202025.pdf) | Effective-date heading; Table 1 item 3 for Case 1; other penalties referred | 2026-11-01 completed read reused; 2026-11-26 heading/item checked |

| [MoF Ministerial Decision 66/2026](https://mof.gov.ae/wp-content/uploads/2026/05/Ministerial-Resolution-No.-66-of-2026-Amending-Certain-Provisions-of-Ministerial-Resolution-No.-244-of-2025-Regarding-the-Implementation-of-the-Electronic-Invoicing-System-En-20260514.pdf) | Article Three publication-dependent commencement and unfilled date fields; not proof of gazette publication or current implementation dates | 2026-11-01 prior limitation reused; 2026-11-26 precise text checked |

Not yet confirmed: all referral methods above are non-operative here, including special classifications/taxpayers, zone/GCC/e-commerce rules, employee benefits, supplier checks, cash limit, margin/apportionment/capital assets, historical rules, penalty transition, current e-invoicing timetable/commencement and authenticated portal/payment screens. They require partner-accountant review before use.
