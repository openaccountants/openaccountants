---
name: thailand-vat
description: "Thailand VAT for 2026: PP.30 transaction and input-credit working papers, the enacted rate period, registration, invoice blocks, export-use conditions, PP.36 imported services, evidence-led bank patterns and corrected historical cases."
version: 2.1
jurisdiction: TH
tax_year: 2026
last_updated: 2026-11-16
depends_on:
  - vat-workflow-base
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: vat-gst
type: computation
---

# Thailand VAT and monthly working papers v2.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

**2026 answer layer:** prepare PP.30 working papers for a Thai VAT-registered business, keeping exempt supplies, zero rating, blocked input and PP.36 imported-service remittances separate. The ordinary combined rate remains period-bound; never select a tax result from a bank counterparty name alone. Load `vat-workflow-base`.

**Contributor: Open Accountants Community.** Minimum working input is the monthly bank statement or equivalent complete transaction ledger and proof of VAT registration; without transaction data, stop. Recommended evidence is all sales/purchase tax invoices, prior PP.30 and carried credit; ideal evidence also includes full ledgers, customs/export documents and asset records. A bank statement can start a provisional working paper, but input credits require proper tax documents and a substantive entitlement. No filing-ready output is produced from a statement alone.

## Rates, bands and thresholds

| Item | Amount and conditions | Period | Official source |
|---|---|---|---|
| Ordinary combined VAT | 7% including local tax; the enacted reduction fixes the Revenue Code component at 6.3% (in words on the page in Decree 807). Do not treat statutory 10% as the current ordinary combined charge | Through 30 September 2027 | [Decree 807 §§2-3 and reduced component](https://www.rd.go.th/fileadmin/user_upload/kormor/newlaw/dc807.pdf); [RD VAT explanation §4, combined rate](https://www.rd.go.th/english/6043.html); [Revenue Code §80, statutory rate](https://www.rd.go.th/5206.html) |
| Exports and other statutory zero rating | 0% only for qualifying transactions; service exports require foreign-use/payment evidence, exclude organising outbound tours, and zero-rate only the foreign-used portion for mixed use | 2026 | [Notification 105 clauses 2-3 as amended, under Revenue Code §80/1](https://www.rd.go.th/3288.html) |
| Registration threshold | Annual turnover exceeding THB 1,800,000 for regular taxable supplies; imports and special regimes have their own scope | 2026 | [RD VAT explanation §§1 and 9](https://www.rd.go.th/english/6043.html) |
| Registration timing | Register before starting where required or within 30 days after reaching the threshold; do not assume every exempt activity must register | 2026 | [RD VAT explanation §9; Revenue Code §§85-85/1](https://www.rd.go.th/english/6043.html) |
| PP.30 ordinary paper cycle | Monthly, due within the 15th of the following month; branch/consolidated filing follows actual approval | 2026 | [Revenue Code §§83-83/1 (deadline in words on the page)](https://www.rd.go.th/5207.html) |
| Late-payment surcharge | 1.5% per month or part-month on unpaid tax, excluding penalty; capped at unpaid tax, with the statutory approved-extension exception | 2026 | [Revenue Code §89/1](https://www.rd.go.th/5209.html) |
| Failure to file | Statutory civil penalty of 2 times the tax due for the month before any lawful remission; separate administrative/criminal rules can also apply | 2026 | [Revenue Code §89(2) (multiplier in words on the page)](https://www.rd.go.th/5209.html) |
| Understatement | 1 times tax discrepancy under §89(3), with separately stated output/input misstatement rules; do not assume a reduced settlement amount | 2026 | [Revenue Code §89(3)-(4) (multiplier in words on the page)](https://www.rd.go.th/5209.html) |
| Unauthorised/fake invoice or missing issue | The relevant §89(5)-(7) category can carry 2 times invoice tax, alongside other sanctions; establish the actual offence | 2026 | [Revenue Code §89(5)-(7) (multipliers in words on the page)](https://www.rd.go.th/5209.html) |

The combined ordinary 7% is stated in the [RD VAT explanation §4](https://www.rd.go.th/english/6043.html); the underlying statutory rate and Royal Decree reduction power are in [Revenue Code §80](https://www.rd.go.th/5206.html). The decree linked in the table fixes the reduced Revenue Code component and its end date.

## The base

### Compute the supply, then the input entitlement

Determine the actual supply, place and tax point before extracting tax from cash. Under the [RD VAT explanation §§3 and 5](https://www.rd.go.th/english/6043.html), the general base is consideration received/receivable excluding VAT; separately disclosed permitted discounts differ from an unexplained net bank deposit. Imported-goods base includes CIF, duty, excise and applicable taxes/fees. Goods and services have different trigger rules, and imported services turn on payment; do not automatically run VAT on a cash-basis bank total. Genuine security and advance payments require their actual contract/tax-point analysis.

For an established VAT-inclusive standard-rate amount, net is gross / 1.07 and VAT gross × 7 / 107, both derived. For an established VAT-exclusive amount, VAT is net × 7%. Do not extract embedded Thai VAT from a foreign invoice merely because its gross-looking amount ends in a familiar decimal.

Exempt differs from zero-rated: an exempt supply does not carry output VAT and ordinarily does not support attributable input credit; qualifying zero-rated taxable supplies can preserve input entitlement. [Section 81](https://www.rd.go.th/5206.html) contains detailed agriculture/food, education, healthcare, domestic land transport, qualifying professional/cultural/religious and other exemptions; rental of immovable property is distinct from every accommodation or related service. Financial-business and insurance treatment can instead involve SBT; never exempt every charge bearing a bank or insurance brand.

Before claiming input VAT, test registration, directly related taxable business purpose, full tax invoice and required particulars, actual VAT charged or remitted and the legal timing. [Section 82/5](https://www.rd.go.th/5206.html) bars, among other things, missing/defective documents, unrelated expenditure, entertainment and unauthorised invoices. [Notification 17 clause 5](https://www.rd.go.th/3409.html) expressly includes accommodation, food, drinks, entertainment and similar client hospitality, whether beneficial to the business or not. A valid restaurant tax invoice does not remove that block. Separate an ordinary non-entertainment business purchase from hospitality on its actual facts; a restaurant's own sales VAT is a different question.

For passenger cars, mixed/private use and related fuel/leases/maintenance, obtain the vehicle classification, use and the specific blocking notification before granting credit; business-use percentage alone does not cure a legal block. For mixed taxable/exempt business, [§82/6](https://www.rd.go.th/5206.html) requires apportionment under the prescribed rules. The former 'escalate only if exempt sales exceed 5%' is not a verified safe harbour; flag every unresolved mixed-use computation. This skill does not provide a fictitious percentage to bypass that review.

### Tax invoices, adjustments and supporting evidence

[Revenue Code §86/4](https://www.rd.go.th/5208.html) requires the prominent tax-invoice words, seller identity/address/tax identifier, buyer identity/address, serial number, description/quantity/value, separately shown VAT, issue date and prescribed additional particulars. Check the actual required buyer/branch identifiers and VAT status, not the old invented format rule for tax-ID prefixes. Retail abbreviated invoices follow §86/6 and the relevant input-block rules; the original THB 1,000-per-transaction permission was not established. Do not use that amount as a licence to issue or claim an abbreviated invoice.

Reconcile credit/debit notes, cancellations and corrections to their statutory event and month. [§§82/9-82/11](https://www.rd.go.th/5206.html) addresses increased/decreased consideration and qualifying bad debts; a bank refund alone is not necessarily a tax credit note. Obtain customs VAT receipts and, for eligible remittances, the official receipt treated as tax-invoice evidence under [§86/14](https://www.rd.go.th/5208.html). Preserve the audit trail between document, ledger, bank settlement and return month.

### Provisional classifications, refusals and review flags

Keep all uncertainty visible. Unknown country, B2B/B2C status or rate is pending factual classification, not automatically domestic/B2C/standard rate. An unknown export claim cannot be filed at zero without evidence; any provisional standard-rate reserve must be labelled a working assumption rather than an established liability. Unknown business use or invoice entitlement gets no provisional input claim pending proof.

- **R-TH-1, non-registered business:** verify mandatory/voluntary registration, not only turnover. Do not charge VAT or claim input as a registrant without the relevant status; imports/non-resident mechanisms still require analysis.
- **R-TH-2, SBT:** financial institutions, life insurance and other SBT activities need their own classification; a fee label does not establish which tax applies. Refer the SBT computation.
- **R-TH-3, partial exemption:** obtain annual taxable/exempt revenue and allocation evidence; refer unresolved apportionment, rather than treating all input as deductible.
- **R-TH-4, government receipts:** reconcile invoice and the actual deduction certificate. The old assertion that government customers generally withhold the entire VAT is unsupported and must not create a PP.30 credit. [§83/5](https://www.rd.go.th/5207.html) concerns auctioneers selling a registrant's property, including government auction/sale rules, not blanket government-customer withholding. Income-tax withholding is distinct.
- **R-TH-5, foreign digital B2C:** foreign electronic suppliers/platforms serving non-registered customers require the separate regime; do not run the domestic PP.30 method or claim the supplier's simplified-regime charge as domestic input by analogy.

The retained review thresholds are internal triage settings, not Thai law: HIGH transaction THB 100,000; HIGH tax difference from an assumption THB 7,000; MEDIUM counterparty concentration over 40%; MEDIUM more than 4 pending defaults per period; LOW absolute net-VAT position THB 50,000. They never make a transaction legally safe below the setting and never override an unresolved material point. Review software should show the assumption and potential tax difference, not just a traffic-light colour.

### Supplier and transaction pattern library

Use case-insensitive substring matching, most-specific first, only to create an investigation queue. All former pattern strings are retained below. They do not assign a rate, supplier residence, exemption or input credit. No public supplier-by-supplier ruling was read. Legal classifications follow the actual transaction under [§§80/1, 81 and 82/5](https://www.rd.go.th/5206.html) and [§83/6](https://www.rd.go.th/5207.html).

#### Thai banks: identify the actual fee

A bank name is a matching clue. Separate interest/financial-business charges from any taxable service and obtain the actual document. Do not mark every fee exempt or claim input VAT from the bank narrative alone.

| Retained original matching pattern | Action |
|---|---|
| ธนาคารกรุงเทพ, BANGKOK BANK, BBL | Apply the evidence test immediately above; keep unresolved classification pending. |
| ธนาคารกสิกรไทย, KASIKORNBANK, KBANK | Apply the evidence test immediately above; keep unresolved classification pending. |
| ธนาคารไทยพาณิชย์, SCB, SIAM COMMERCIAL | Apply the evidence test immediately above; keep unresolved classification pending. |
| ธนาคารกรุงไทย, KRUNGTHAI, KTB | Apply the evidence test immediately above; keep unresolved classification pending. |
| ธนาคารกรุงศรี, KRUNGSRI, BAY, BANK OF AYUDHYA | Apply the evidence test immediately above; keep unresolved classification pending. |
| ทีเอ็มบีธนชาต, TTB BANK | Apply the evidence test immediately above; keep unresolved classification pending. |
| ธนาคารออมสิน, GOVERNMENT SAVINGS BANK, GSB | Apply the evidence test immediately above; keep unresolved classification pending. |
| ธนาคารอิสลาม, ISLAMIC BANK OF THAILAND | Apply the evidence test immediately above; keep unresolved classification pending. |
| ค่าธรรมเนียม, ดอกเบี้ย, FEE, INTEREST | Apply the evidence test immediately above; keep unresolved classification pending. |

#### Government and statutory payments

A payment of tax, duty or a fund contribution itself is a remittance, not an invoice supporting input credit. Investigate separately any goods/services bought from the same authority.

| Retained original matching pattern | Action |
|---|---|
| กรมสรรพากร, REVENUE DEPARTMENT, RD | Apply the evidence test immediately above; keep unresolved classification pending. |
| ภาษีมูลค่าเพิ่ม, ภาษีเงินได้ | Apply the evidence test immediately above; keep unresolved classification pending. |
| ประกันสังคม, SOCIAL SECURITY OFFICE, SSO | Apply the evidence test immediately above; keep unresolved classification pending. |
| กรมศุลกากร, CUSTOMS DEPARTMENT | Apply the evidence test immediately above; keep unresolved classification pending. |
| กรมสรรพสามิต, EXCISE DEPARTMENT | Apply the evidence test immediately above; keep unresolved classification pending. |
| กองทุนเงินทดแทน | Apply the evidence test immediately above; keep unresolved classification pending. |

#### Utilities and communications

Obtain the actual registered seller, full tax invoice, taxable supply, tax point and business use. Only supported, directly related and non-blocked VAT can enter input credit; a merchant name does not prove a rate or invoice.

| Retained original matching pattern | Action |
|---|---|
| การไฟฟ้านครหลวง, MEA, METROPOLITAN ELECTRICITY | Apply the evidence test immediately above; keep unresolved classification pending. |
| การไฟฟ้าส่วนภูมิภาค, PEA, PROVINCIAL ELECTRICITY | Apply the evidence test immediately above; keep unresolved classification pending. |
| การประปานครหลวง, MWA, METROPOLITAN WATERWORKS | Apply the evidence test immediately above; keep unresolved classification pending. |
| การประปาส่วนภูมิภาค, PWA, PROVINCIAL WATERWORKS | Apply the evidence test immediately above; keep unresolved classification pending. |
| ปตท, PTT, PTT PUBLIC | Apply the evidence test immediately above; keep unresolved classification pending. |
| AIS, ADVANCED INFO SERVICE | Apply the evidence test immediately above; keep unresolved classification pending. |
| DTAC, TOTAL ACCESS | Apply the evidence test immediately above; keep unresolved classification pending. |
| TRUE MOVE, TRUE CORPORATION | Apply the evidence test immediately above; keep unresolved classification pending. |
| DITO THAILAND | Apply the evidence test immediately above; keep unresolved classification pending. |
| ทีโอที, TOT | Apply the evidence test immediately above; keep unresolved classification pending. |

#### Transport and logistics

Identify passenger/freight, route and actual supplier/service. Domestic land transport can be exempt; a platform commission, courier package or air service is not decided by the brand. International air/sea zero rating has the statutory provider/route conditions. The original domestic-water passenger-transport topic is retained: test the actual service under [§81(1)(ณ), domestic transport, and §81/3](https://www.rd.go.th/5206.html). Domestic water transport is within that exemption analysis, but [Royal Decree 241 §3(4), as amended by 521](https://www.rd.go.th/2382.html) permits voluntary VAT registration for domestic sea transport by seagoing vessel, including sea-to-river transport by seagoing vessel. Establish the route, vessel/service and the supplier's actual VAT election/registration before treating a water ticket as exempt or accepting an input-tax claim. A separate platform/courier/service fee does not inherit a transport exemption by name.

| Retained original matching pattern | Action |
|---|---|
| การรถไฟ, SRT, STATE RAILWAY OF THAILAND | Apply the evidence test immediately above; keep unresolved classification pending. |
| รถไฟฟ้าบีทีเอส, BTS SKYTRAIN | Apply the evidence test immediately above; keep unresolved classification pending. |
| รถไฟฟ้ามหานคร, MRT BANGKOK | Apply the evidence test immediately above; keep unresolved classification pending. |
| บริษัท ขนส่ง, TRANSPORT CO (bus) | Apply the evidence test immediately above; keep unresolved classification pending. |
| การบินไทย, THAI AIRWAYS, TG | Apply the evidence test immediately above; keep unresolved classification pending. |
| แอร์เอเชีย, AIR ASIA, FD | Apply the evidence test immediately above; keep unresolved classification pending. |
| บางกอก แอร์เวยส์, BANGKOK AIRWAYS | Apply the evidence test immediately above; keep unresolved classification pending. |
| GRAB THAILAND | Apply the evidence test immediately above; keep unresolved classification pending. |
| BOLT THAILAND | Apply the evidence test immediately above; keep unresolved classification pending. |
| LINEMAN, LINE MAN | Apply the evidence test immediately above; keep unresolved classification pending. |
| ไปรษณีย์ไทย, THAILAND POST | Apply the evidence test immediately above; keep unresolved classification pending. |
| KERRY EXPRESS, KERRY LOGISTICS | Apply the evidence test immediately above; keep unresolved classification pending. |
| FLASH EXPRESS, แฟลช เอ็กซ์เพรส | Apply the evidence test immediately above; keep unresolved classification pending. |
| J&T EXPRESS THAILAND | Apply the evidence test immediately above; keep unresolved classification pending. |

#### Food and retail

Split actual goods/services on the invoice. Qualifying unprocessed agricultural goods can be exempt even in a supermarket. Restaurant output tax does not make client entertainment input creditable. No all-items standard-rate rule follows from a store name.

| Retained original matching pattern | Action |
|---|---|
| เซเว่น-อีเลฟเว่น, 7-ELEVEN THAILAND, CPF | Apply the evidence test immediately above; keep unresolved classification pending. |
| เทสโก้ โลตัส, TESCO LOTUS, LOTUS'S | Apply the evidence test immediately above; keep unresolved classification pending. |
| บิ๊กซี, BIG C SUPERCENTER | Apply the evidence test immediately above; keep unresolved classification pending. |
| แม็คโคร, MAKRO | Apply the evidence test immediately above; keep unresolved classification pending. |
| ท็อปส์ มาร์เก็ต, TOPS MARKET | Apply the evidence test immediately above; keep unresolved classification pending. |
| ครัวบ้าน (RESTAURANT) | Apply the evidence test immediately above; keep unresolved classification pending. |
| แมคโดนัลด์, MCDONALD'S THAILAND | Apply the evidence test immediately above; keep unresolved classification pending. |
| KFC THAILAND | Apply the evidence test immediately above; keep unresolved classification pending. |

#### Locally billed SaaS and platforms

Check the actual billing entity, Thai VAT registration, service and invoice. A locally familiar platform name alone does not establish a domestic taxable invoice or input entitlement.

| Retained original matching pattern | Action |
|---|---|
| JOBBKK, จ๊อบบีเคเค | Apply the evidence test immediately above; keep unresolved classification pending. |
| JOBSDB THAILAND | Apply the evidence test immediately above; keep unresolved classification pending. |
| WONGNAI | Apply the evidence test immediately above; keep unresolved classification pending. |
| LAZADA THAILAND (local entity) | Apply the evidence test immediately above; keep unresolved classification pending. |
| SHOPEE THAILAND (local entity) | Apply the evidence test immediately above; keep unresolved classification pending. |

#### International SaaS and other services

Verify the actual contracting/billing entity and service used in Thailand. For foreign electronic B2B supplies to a registered recipient, test PP.36 remittance; for B2C test the foreign-supplier/platform regime. Former regional billing hints are preserved as historical leads, not current entity assertions.

| Retained original matching pattern | Action |
|---|---|
| GOOGLE (Workspace, Ads, Cloud); former billing hint: Google Asia Pacific | Apply the evidence test immediately above; keep unresolved classification pending. |
| MICROSOFT (365, Azure); former billing hint: Microsoft regional | Apply the evidence test immediately above; keep unresolved classification pending. |
| ADOBE; former billing hint: Adobe Inc (US) | Apply the evidence test immediately above; keep unresolved classification pending. |
| META, FACEBOOK ADS; former billing hint: Meta Ireland/US | Apply the evidence test immediately above; keep unresolved classification pending. |
| SLACK; former billing hint: Salesforce/Slack | Apply the evidence test immediately above; keep unresolved classification pending. |
| ZOOM; former billing hint: Zoom Video | Apply the evidence test immediately above; keep unresolved classification pending. |
| NOTION; former billing hint: Notion Labs (US) | Apply the evidence test immediately above; keep unresolved classification pending. |
| ANTHROPIC, CLAUDE; former billing hint: Anthropic (US) | Apply the evidence test immediately above; keep unresolved classification pending. |
| OPENAI, CHATGPT; former billing hint: OpenAI (US) | Apply the evidence test immediately above; keep unresolved classification pending. |
| AWS; former billing hint: Amazon (US/SG) | Apply the evidence test immediately above; keep unresolved classification pending. |

#### Payment processors

Split interest/financial-business treatment from processing, technology or other service fees and determine the actual foreign/local supplier. Do not blanket-exempt payment processors; a foreign service may require PP.36 analysis.

| Retained original matching pattern | Action |
|---|---|
| STRIPE (transaction fees) | Apply the evidence test immediately above; keep unresolved classification pending. |
| PAYPAL (fees) | Apply the evidence test immediately above; keep unresolved classification pending. |
| OMISE (fees) | Apply the evidence test immediately above; keep unresolved classification pending. |
| 2C2P (fees) | Apply the evidence test immediately above; keep unresolved classification pending. |

#### Internal transfers, principal and other movements

Trace the underlying event: an internal movement/loan principal is not consideration for a sale; salary is employment, not a VAT invoice. Identify dividend, security deposit versus advance consideration, or cash use from documents. Cash withdrawals remain pending, not assumed business input.

| Retained original matching pattern | Action |
|---|---|
| โอนเงินภายใน, INTERNAL TRANSFER | Apply the evidence test immediately above; keep unresolved classification pending. |
| เงินกู้, LOAN, เงินให้กู้ | Apply the evidence test immediately above; keep unresolved classification pending. |
| เงินเดือน, SALARY, ค่าจ้าง | Apply the evidence test immediately above; keep unresolved classification pending. |
| เงินปันผล, DIVIDEND | Apply the evidence test immediately above; keep unresolved classification pending. |
| เงินประกัน, DEPOSIT | Apply the evidence test immediately above; keep unresolved classification pending. |
| ถอนเงินสด, ATM | Apply the evidence test immediately above; keep unresolved classification pending. |

### Bank statement reading guide

The original export-field hints are retained as practical examples, not current specifications certified by the banks. KBank/ธ.กสิกรไทย: วันที่, รายการ, ถอน/โอนออก, ฝาก/โอนเข้า, ยอดคงเหลือ; SCB/ธ.ไทยพาณิชย์: Date, Description, Debit, Credit, Balance; BBL/ธ.กรุงเทพ: วันที่ทำรายการ, คำอธิบาย, ถอน, ฝาก, ยอดคงเหลือ; KTB/ธ.กรุงไทย: Date, Narrative, Withdrawal, Deposit, Balance; Krungsri/ธ.กรุงศรี: วันที่, รายละเอียด, เดบิต, เครดิต, ยอดเงินคงเหลือ. Check the actual header, debit/credit sign, currency and date convention in the supplied file. A Thai-style date may be BE rather than CE; subtract 543 for the calendar conversion (derived), do not change document references blindly.

โอนเงินรับ / รับโอน means incoming transfer and is only a revenue candidate; โอนเงิน / ตัดบัญชี is transfer/debit; หักค่า is auto-deduction; ดอกเบี้ย is interest; ค่าธรรมเนียม is fee; ยอดคงเหลือ is balance, not a new transaction; รายการ / คำอธิบาย is the description; ถอนเงิน / ATM is cash withdrawal requiring tracing; เงินเดือน is salary. Neither the Thai term nor an English alias proves the VAT treatment.

### Working paper and onboarding fallback

Use the following schedule with supporting-document references and an unresolved-items column. It preserves the original A/B/C structure while correcting the treatment of imported-service VAT and unsupported 'withholding VAT' credits.

```text
THAILAND VAT WORKING PAPER / แบบคำนวณภาษีมูลค่าเพิ่ม
Period (เดือน): ____  VAT Registration No.: ____  Branch/approval: ____
A. OUTPUT
 A1. Standard-rated sales, net ____
 A2. Domestic output VAT on A1 ____
 A3. Qualifying zero-rated sales ____
 A4. Exempt sales ____
 A5. PP.36 imported-service VAT remitted separately; not domestic output ____
B. INPUT
 B1. Supported domestic purchases, net ____
 B2. Eligible domestic VAT ____
 B3. Eligible customs VAT with receipt ____
 B4. Eligible PP.36 VAT with receipt, in the proper credit month ____
 B5. Total potential input B2+B3+B4 ____
 B6. Blocked/private/unsupported/apportioned-away input ____
 B7. Eligible input B5-B6 ____
C. PP.30
 C1. A2-B7 ____
 C2. Government/customer deductions: reconcile separately, no assumed VAT credit ____
 C3. Proper unclaimed prior-period carry-forward ____
 C4. Current payable/credit after supported carry-forward ____
SEPARATE CASH PAYMENT: PP.36 amount A5 ____; do not net away this remittance.
REVIEW: invoices; export use/payment evidence; government deduction certificates;
        PP.36 receipts/timing; vehicle blocks/business use; prior credits;
        private use, corrections, branch authority and tax-point dates.
```

If the client cannot answer everything immediately, first reconcile complete transactions using the pattern library as clues, list unresolved classifications without inventing country/rate, keep unsupported input unclaimed, then produce a flagged working paper. Ask for the registration/tax identifier and branch, statement month and BE/CE convention, actual export use/payment evidence, government deduction documents, vehicle facts, full tax invoices, prior excess credit and all foreign SaaS/service invoices. A provisional reserve is not an instruction to file an assumed treatment. No bank statement/equivalent ledger means hard stop; missing invoices mean provisional preparation only.

## Deadlines and filing

### PP.30 form mapping and submission

The opened official [PP.30 paper form and both-page instructions](https://www.rd.go.th/fileadmin/tax_pdf/vat/pp30_300160.pdf) has this mapping, replacing the original invented shorthand. Its URL identifies the older paper-form revision; use current e-Filing labels and reconcile any changed layout rather than asserting a signed-in 2026 screen was read.

| Paper item | Meaning | Official source |
|---|---|---|
| 1 | All sales in the month, including taxable, zero-rated and exempt sales under the instructions | [PP.30 both pages](https://www.rd.go.th/fileadmin/tax_pdf/vat/pp30_300160.pdf) |
| 2 | Deduct zero-rated sales | [PP.30 item 2](https://www.rd.go.th/fileadmin/tax_pdf/vat/pp30_300160.pdf) |
| 3 | Deduct exempt sales | [PP.30 item 3](https://www.rd.go.th/fileadmin/tax_pdf/vat/pp30_300160.pdf) |
| 4 | Standard-taxable sales after 1 minus 2 minus 3, derived | [PP.30 item 4](https://www.rd.go.th/fileadmin/tax_pdf/vat/pp30_300160.pdf) |
| 5 | Output tax from the output-tax report | [PP.30 item 5](https://www.rd.go.th/fileadmin/tax_pdf/vat/pp30_300160.pdf) |
| 6 | Purchases eligible for the current input deduction | [PP.30 item 6](https://www.rd.go.th/fileadmin/tax_pdf/vat/pp30_300160.pdf) |
| 7 | Eligible input tax, not the old item-6 shorthand | [PP.30 item 7](https://www.rd.go.th/fileadmin/tax_pdf/vat/pp30_300160.pdf) |
| 8-9 | Current tax payable or excess input respectively, derived from 5 and 7 | [PP.30 items 8-9](https://www.rd.go.th/fileadmin/tax_pdf/vat/pp30_300160.pdf) |
| 10 | Proper unrefunded prior-month excess credit; not used in an additional return under these instructions | [PP.30 item 10 and instructions](https://www.rd.go.th/fileadmin/tax_pdf/vat/pp30_300160.pdf) |
| 11-12 | Net payable or overpayment after the allowed carry-forward | [PP.30 items 11-12](https://www.rd.go.th/fileadmin/tax_pdf/vat/pp30_300160.pdf) |
| 13-16 | Surcharge, civil penalty, final payable or final excess; establish any lawful reductions independently | [PP.30 items 13-16](https://www.rd.go.th/fileadmin/tax_pdf/vat/pp30_300160.pdf) |

Reconcile sales/purchase reports, branch approval, prior credit, corrections and supporting invoices. Follow the [official e-Filing route](https://www.rd.go.th/rdeservice/63813.html), select PP.30, taxpayer, branch, tax month/BE year and original/additional return. Populate the fields by their actual labels, compare the totals with the working paper, select the lawful carry-forward/refund treatment, review and submit, pay with the generated reference, and retain the return, acknowledgement and receipt. Multi-establishment consolidated filing requires actual approval; otherwise separate filing applies under [§83](https://www.rd.go.th/5207.html). File the monthly return even when there is no tax to pay under the statutory reporting requirement.

The statutory paper due date is in the rates table. The opened [RD electronic calendar](https://www.rd.go.th/26/9835.html) specifically lists 23 September 2026 for PP.30; it is evidence for that period, not authority for an automatic date in every month. The old standing '23rd e-filing' headline must be checked against the actual month, extension instrument and holidays. PP.36 has its own remittance timing, not PP.30's paper deadline.

### Imported services and PP.36

Under [§83/6(2)](https://www.rd.go.th/5207.html), the recipient remits VAT for foreign electronic services used by a VAT registrant and for other foreign services used in Thailand by any recipient within that provision. Do not reduce this to only digital SaaS. Foreign electronic B2C is treated separately under [§82/13](https://www.rd.go.th/5206.html). Verify recipient registration and the actual supplier rather than defaulting to B2C.

Prepare PP.36 from the actual foreign-service payment, its date, currency conversion, service and supplier evidence. Remit it separately through the official service. The resulting official receipt is the evidence for an eligible input claim under §86/14, subject to substantive blocks and the proper credit period. It is not domestic output VAT and cannot be erased by a simultaneous notional input entry in PP.30. The exact current PP.36 electronic due-date extension/portal fields remain to be verified before submission.

## Penalties and interest

Use the actual default and statutory base, not a generic THB 300-500 settlement assumption. Section 89 distinguishes non-registration, no return, understated tax, output/input misstatement, missing or unauthorised/fake invoices and missing records; any remission requires the applicable instruction and facts. Section 89/1 surcharge counts a month or part and is capped; do not apply it to the penalty itself. Administrative/criminal offences under §90 and its subdivisions are separate, so an invoice default is not resolved by the original universal 'THB 2,000 per invoice' claim. Escalate fraudulent documents immediately.

## Cross-border points

For export services, [Notification 105 clauses 2-3, amended by 181](https://www.rd.go.th/3288.html) requires a foreign recipient and actual foreign use, with only the foreign-use part zero-rated where use is mixed. Clause 2(1) expressly excludes organising outbound tours from this export-service definition; foreign use and a foreign customer do not establish zero rating for that excluded activity. Evidence of payment is required subject to the no-consideration exception; the enumerated evidence is broader than foreign currency alone. Keep the contract, deliverables/use analysis, invoices and matching payment trace. A foreign payer, USD receipt or foreign bank account alone is not sufficient; neither is a missing FX receipt automatically proof of a taxable domestic supply. International air/sea transport has its specific provider conditions; domestic or international land transport follows its exemption rule, not an all-international-zero rule.

Foreign goods/import VAT, foreign services/PP.36, non-resident electronic B2C, SBT and real estate are distinct jobs. Refer their unsupported special regimes rather than labelling an overseas transfer zero-rated or financial-exempt. The legacy reference to Royal Decree 694 as the complete digital-services law is not used: the current consolidated §§82/13 and 83/6 show the amended rules directly.

## Two worked examples that recompute

The original six hypothetical bank lines are retained verbatim, dated in 2025 (BE 2568). They are historical fixtures, not evidence of live suppliers or a 2026 transaction. The ordinary rate assumption is supported for that period and the current reduction is separately bounded above. Corrected classifications follow the actual assumed facts, not the names alone.

### Original case 1: domestic IT-consulting sale

`15/04/2568  โอนเงินรับ  บริษัท เทค โซลูชั่น จำกัด  เลขที่: INV-2025-041  +535,000.00  THB`

Assume the documents establish a domestic standard-rated consulting sale and the receipt includes VAT. Net THB 500,000 and output VAT THB 35,000 follow. Issue the proper tax invoice; sales enter the appropriate PP.30 sales fields and output tax is item 5 on the opened paper form, not the old item-2 claim.

```oa-check
name: Thailand domestic inclusive sale original case
inputs:
  gross: 535000
steps:
  - net: gross / 1.07
  - output: gross - net
expected:
  net: 500000
  output: 35000
```

### Original case 2: export-service evidence

`22/04/2568  รับโอนเงินตราต่างประเทศ  ACME CORP USA  Technical consulting Q1  +USD 15,000 (THB 540,000)`

Assume an ordinary consulting service within Notification 105 clause 2(1), not outbound-tour organising, a foreign recipient, wholly foreign use and the required matching payment/use evidence, with the given documented THB conversion. Qualifying export revenue THB 540,000 has output VAT THB 0. Zero-rated sales are item 2 on the opened paper form, not the old item 3. If evidence is missing, hold the classification for review; do not describe a standard-rate reserve as proven law. The hypothetical exchange conversion is supplied, not a statutory exchange rate.

```oa-check
name: Thailand original wholly foreign-used service
inputs:
  documented_thb_value: 540000
  qualifying_rate: 0
steps:
  - output: documented_thb_value * qualifying_rate
expected:
  output: 0
```

### Original case 3: utility invoice

`10/04/2568  หักค่าไฟฟ้า  การไฟฟ้านครหลวง MEA  ค่าไฟ มีนาคม 2568  -10,700.00  THB`

Assume actual taxable business electricity, a full eligible invoice and the proper input month. THB 10,700 inclusive gives THB 10,000 net and THB 700 potential input. It enters eligible input item 7 on the opened paper form only after entitlement/timing checks; the merchant string itself proves neither.

```oa-check
name: Thailand original eligible utility invoice
inputs:
  gross: 10700
steps:
  - net: gross / 1.07
  - input: gross - net
expected:
  net: 10000
  input: 700
```

### Original case 4: foreign SaaS remittance, corrected

`08/04/2568  ตัดบัญชี  GOOGLE ASIA PACIFIC  Google Workspace April  -3,210.00  THB`

Assume the actual invoice proves a foreign service used in Thailand, a registered recipient and a VAT-exclusive price THB 3,210. PP.36 remittance is THB 224.70, not THB 225. If fully eligible and supported by the official remittance receipt in the proper month, potential input is THB 224.70. The separate cash remittance still has to be paid; do not add it as domestic PP.30 output or assume same-month recovery. The billing entity and tax-exclusive assumption require evidence.

```oa-check
name: Thailand original foreign SaaS corrected arithmetic
inputs:
  foreign_net: 3210
  rate: 0.07
steps:
  - pp36_payment: foreign_net * rate
  - potential_eligible_input: pp36_payment
  - cash_to_supplier_and_rd: foreign_net + pp36_payment
expected:
  pp36_payment: 224.7
  potential_eligible_input: 224.7
  cash_to_supplier_and_rd: 3434.7
```

### Original case 5: MRT passenger fare

`05/04/2568  ตัดบัญชี  MRT กรุงเทพ  ค่าโดยสาร  -1,200.00  THB`

Assume the ticket establishes exempt domestic land passenger transport. Expense THB 1,200 has no input VAT to recover. Exempt is not a zero-rated purchase, and the income-tax expense is a separate question.

```oa-check
name: Thailand original exempt domestic passenger fare
inputs:
  fare: 1200
  vat_shown: 0
steps:
  - input_credit: vat_shown
  - expense_before_income_tax_review: fare - input_credit
expected:
  input_credit: 0
  expense_before_income_tax_review: 1200
```

### Original case 6: client hospitality, corrected

`12/04/2568  บัตรเครดิต  ร้านอาหาร ครัวไทย  อาหารกลางวัน ลูกค้า  -3,210.00  THB`

The original narrative identifies a client lunch. Even assuming a valid standard-rated full tax invoice, supplier VAT THB 210 is blocked as entertainment under §82/5(4)/Notification 17. Recoverable input is THB 0; the unrecovered cost is THB 3,210 before separate income-tax deductibility. The former THB 210 input-credit instruction and 'never block entertainment categorically' prohibition were wrong.

```oa-check
name: Thailand original client lunch blocked input
inputs:
  gross: 3210
  blocked_fraction: 1
steps:
  - supplier_net: gross / 1.07
  - supplier_vat: gross - supplier_net
  - recoverable: supplier_vat * (1 - blocked_fraction)
  - unrecovered_cost: gross - recoverable
expected:
  supplier_net: 3000
  supplier_vat: 210
  recoverable: 0
  unrecovered_cost: 3210
```

### Decision: wholly foreign use versus substantiated mixed use

For a hypothetical ordinary consulting service within Notification 105 clause 2(1), excluding outbound-tour organising, and net fee THB 540,000, compare wholly qualifying foreign use with substantiated 70% foreign/30% Thai use. Whole foreign use gives no output VAT; mixed use gives THB 378,000 zero-rated base, THB 162,000 domestic base and THB 11,340 output VAT derived. The allocation is an evidence assumption for this case, not a statutory safe harbour. A foreign invoice address cannot choose the zero-tax answer.

```oa-check
name: Thailand foreign-use allocation decision
inputs:
  fee: 540000
  foreign_use_fraction: 0.7
steps:
  - foreign_base: fee * foreign_use_fraction
  - domestic_base: fee - foreign_base
  - mixed_output: domestic_base * 0.07
  - wholly_foreign_output: fee * 0
expected:
  foreign_base: 378000
  domestic_base: 162000
  mixed_output: 11340
  wholly_foreign_output: 0
```

## Ask the client first

- Actual VAT registration, branch/consolidation authority, tax period and BE/CE dates?
- Sales/purchase invoices, underlying supply, tax points, adjustments and carried credit?
- Export recipient, actual foreign/Thai use and payment evidence?
- Foreign-service invoices, recipient status, payment currency/date and PP.36 receipts?
- Private/vehicle/client-entertainment use or exempt business requiring blocked-input/apportionment review?
- Government deductions, customs receipts, prior filings and any notices or relief instrument?

## Sources

| Source and actual reading scope | URL | Read on |
|---|---|---|
| Royal Decree 807 B.E. 2569 (Read for all 3 rendered pages, §§2-3 and replacement Decree 646 §4: commencement, reduced component and end date; raw PDF extraction was garbled) | https://www.rd.go.th/fileadmin/user_upload/kormor/newlaw/dc807.pdf | 2026-11-16 |
| RD VAT explanation (Read for the complete substantive §§1-10 for taxable person, threshold, base, tax point, rate, invoice, calculation, refunds, registration and filing; current detailed amendments checked in the Thai Code) | https://www.rd.go.th/english/6043.html | 2026-11-16 |
| Consolidated Royal Decree 241 (Read for all operative §§1-4 and amendment notes, especially §3(4) domestic seagoing-vessel/sea-to-river transport VAT opt-in added by Decree 521; no claim to have completed a registration) | https://www.rd.go.th/2382.html | 2026-11-16 |
| Current consolidated VAT Code §§80-82 (Read for §§80/1, 81, 81/3, 82/3-82/6, 82/9-82/13 and neighbors for exemptions, input, adjustments and foreign electronic services) | https://www.rd.go.th/5206.html | 2026-11-16 |
| Director-General VAT Notification 17 (Read for all operative clauses, particularly clause 5 and its food/accommodation/benefit conditions) | https://www.rd.go.th/3409.html | 2026-11-16 |
| Director-General VAT Notification 105 as amended (Read for all operative clauses 1-4, foreign-use allocation, excluded outbound-tour operation, payment evidence and special export-production cases) | https://www.rd.go.th/3288.html | 2026-11-16 |
| Current VAT Code §§83-84 (Read for §§83-83/7 and neighboring filing/remittance provisions, including auctioneer scope and electronic/non-electronic imported-service split) | https://www.rd.go.th/5207.html | 2026-11-16 |
| Current VAT Code §§85-86 (Read for registration and §§86/4, 86/6, 86/14 with neighboring invoice provisions; not an authenticated portal read) | https://www.rd.go.th/5208.html | 2026-11-16 |
| Current VAT Code §§87-90 (Read for records, §89 offence categories, remission delegation, §89/1 surcharge and neighboring §90 offence structure; current remission instruments not read) | https://www.rd.go.th/5209.html | 2026-11-16 |
| Official PP.30 paper form and instructions, URL revision 2017 (Read for both pages, all computation items, branch/additional-return choice, carry-forward restriction and refund/carry-forward instructions; not a claim of a 2026 portal screen) | https://www.rd.go.th/fileadmin/tax_pdf/vat/pp30_300160.pdf | 2026-11-16 |
| RD filing-service index (Read for PP.30/PP.36 and other regime portal routes; no authenticated submission) | https://www.rd.go.th/rdeservice/63813.html | 2026-11-16 |
| RD electronic calendar entry (Read for the specific 23 September 2026 PP.30 entry; not every filing month) | https://www.rd.go.th/26/9835.html | 2026-11-16 |

Not yet confirmed: current PP.36 and general electronic-extension instruments and exact live portal fields; all subsidiary invoice buyer/branch particulars, abbreviated-invoice input rules and vehicle-block exceptions; detailed mixed-use apportionment, SBT and property regimes; current penalty-remission/settlement rules. Legacy THB 1,000 abbreviated-invoice threshold, THB 300-500 late-filing settlement, generic THB 2,000-per-invoice cap, government-customer blanket VAT withholding/credit, automatic same-month reverse-charge netting, 5% exempt-sales safe harbour and merchant-specific blanket exemptions are not usable instructions. Internal review flags and bank-field/pattern hints are workflow settings/examples, not enacted rules or verified supplier rulings.
