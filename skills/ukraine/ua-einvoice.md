---
name: ua-einvoice
description: Use this skill whenever asked about Ukrainian electronic invoicing and digital tax reporting for self-employed people and small businesses. Trigger on phrases like "Ukraine tax invoice", "податкова накладна", "ЄРПН", "VAT invoice registration Ukraine", "register tax invoice Ukraine", "СЕА ПДВ", "VAT account Ukraine", "ПРРО receipt", "fiscal receipt Ukraine FOP", "blocked tax invoice", "зупинення реєстрації ПН", "СМКОР", "КЕП Ukraine", "Електронний кабінет", "SAF-T Ukraine", or any question about how a Ukrainian VAT payer or ФОП issues invoices and reports electronically. Covers the VAT tax invoice and its mandatory ЄРПН registration, the SMKOR registration-blocking system, the СЕА ПДВ electronic VAT administration system and the VAT account, ПРРО software fiscal receipts for retail, qualified electronic signatures (КЕП), the Електронний кабінет, and the status of SAF-T UA. ALWAYS read this skill before any Ukrainian e-invoicing or digital tax-reporting work.
version: 1.1
jurisdiction: UA
tax_year: 2026
last_updated: 2026-11-15
depends_on:
  - income-tax-workflow-base
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: e-invoicing
type: situation-rules
---
# Ukraine Electronic Invoicing and Digital Tax Reporting v 1.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Use this to prepare an **electronic-document and submission review brief** for Ukrainian FOPs and small legal entities: commercial invoices/primary evidence; VAT **ПН / податкова накладна**, **РК / розрахунок коригування** and **ЄРПН** registration; **СЕА ПДВ** registration limit/VAT account; **СМКОР** suspension; **РРО / ПРРО** fiscal receipts; **КЕП**, **Електронний кабінет**, and the bounded on-request **SAF-T UA** route. Currency is UAH. Contributor remains **Open Accountants Community**.

Three documents serve different purposes: a commercial **рахунок-фактура / invoice**, a registered VAT **ПН**, and a fiscal **фіскальний чек** are not substitutes. A non-VAT FOP does not issue an ordinary VAT ПН merely because a customer asks for an “invoice”; that does not remove primary-record, fiscal-settlement or special imported-service tax obligations. An unknown VAT status blocks the decision, rather than defaulting to non-VAT. [201.8,208.1-.4](https://tax.gov.ua/nk/); [fiscal-document FAQ](https://tax.gov.ua/baneryi/programni-rro/aktualni-zapitannya-vidpovidi).

**Dating:** reviewed 15 November 2026 in the precise source scopes below. The first-event and registration rules are subject to actual transaction/category exceptions. Martial-law rules have **different sunset provisions**; the special registration deadlines do not simply end on the day martial law ends. This is not a signed filing, legal appeal, automatic unblocking service or complete export-assurance/special VAT computation. No authenticated taxpayer session or actual schema submission was tested.

## Ask the client first

1. Legal form, taxpayer identifiers and **actual VAT-register status/effective dates**, single-tax group and election, original/corrected document and reporting period. Reuse the documented register extract; no “non-VAT until proven otherwise” default.
2. Contract, customer/supplier status and country, taxable/exempt/outside-scope transaction classification, goods/service codes, quantities/net/gross/VAT, payment/advance dates and supply/service-document dates. Record any cash method, continuous/rhythmic supply, consolidated invoice or export-assurance branch.
3. Is the document an ordinary seller ПН, seller or buyer РК, recipient-created imported-service ПН, commercial invoice, or fiscal receipt? For a decreasing РК, obtain the buyer's receipt date and original ПН date.
4. Actual channel: direct bank-IBAN credit transfer, acquiring/card/payment link/QR, cash, remote service payment or another instrument; goods versus services, group eligibility, stock and fiscal exemptions.
5. Current certificate and signer authority, correct taxpayer role, file/schema, actual sending/receipt timestamps, ЄРПН result/query, ΣНакл components and VAT-account statement. Distinguish inadequate limit, technical rejection and suspension.
6. For suspension: receipt/reason code, risky-taxpayer decision, positive-history result, accepted/not-accepted Table, contracts/stock/labor/assets/payment/transport evidence, all decision/receipt dates and whether court proceedings have started. Escalate before a deadline, do not promise success.
7. For SAF-T: legal-person/PE status, actual large-taxpayer register periods, audit and request, requested periods/deadline, then-current XSD/technical description and actual validation/receipt. VAT registration or “large enterprise” financial-reporting size alone is not the large-taxpayer test.

## The method, step by step

### 1. Route VAT status, primary documents and fiscal settlements

| Status | Electronic-document route and boundary | Official source |
|---|---|---|
| Confirmed ordinary non-VAT FOP | Commercial invoice/contracts/acts and bank/primary records; no ordinary supplier VAT ПН/ЄРПН. Keep the applicable tax-return and fiscal-receipt workflow. No ordinary supplier invoice means no ordinary supplier СМКОР case, not immunity from all tax or digital duties | [201.8;208.4](https://tax.gov.ua/nk/); [Cabinet modules](https://cabinet.tax.gov.ua/help/intro.html) |
| VAT-registered FOP or legal person | Applicable ПН/РК, registration/receipt, ΣНакл/account and suspension checks. VAT registration does not itself remove retail-fiscalisation duties | [201.1/.7-.10,200-1](https://tax.gov.ua/nk/); [PRRO FAQ](https://tax.gov.ua/baneryi/programni-rro/aktualni-zapitannya-vidpovidi) |
| VAT-registration question | Ordinary 181.1 threshold is **over UAH 1000000**, VAT excluded, taxable supplies in the last **12 calendar months**, with the **single-tax Groups 1-3 carveout**; voluntary 182.1 and import/nonresident-service routes remain separate. It is not a universal turnover threshold for every simplified taxpayer | [180.2,181.1-.2,182.1,208](https://tax.gov.ua/nk/) |
| Eligible Group 3 election | **3% single tax with VAT** versus **5% with VAT included in single tax**; actual eligibility, registration and effective dates are owned by `ua-single-tax`. Do not infer VAT status from occupation or a proposed election | [293.3](https://tax.gov.ua/nk/) |
| Imported services | Under 208, a VAT-registered recipient may create/register its own ПН. A non-VAT recipient does not create a ПН under 208.4 but can owe the separate prescribed calculation/payment. Apply 208.1 electronic-service and other statutory exclusions through `ukraine-vat`/`ua-cross-border` | [208.1-.7](https://tax.gov.ua/nk/) |

The ordinary VAT rate is **20%**; **0%/7%/14%** require the specific statutory transaction, authorization/classification and period. No foreign-client invoice is automatically zero-rated. The VAT owner must establish the actual rate/place/base before this mechanical workflow uses it. [193.1,194,195](https://tax.gov.ua/nk/).

Preserve the old six safe-process defaults in corrected form: confirm unknown status; register early; test fiscalisation/exemptions before taking settlements; identify the statutory registering party instead of “seller for everything”; treat blocks urgently; use the legally relevant date and source for each amount, **not a blanket 1 January 2026 minimum-wage index**.

### 2. Create the correct VAT document and identify who registers it

Under ordinary **187.1**, the liability date is the **earlier** of the specified payment receipt/advance and goods shipment or service-supply document date. For an electronic service document, the date stated as its preparation date matters independently of a later signature. Cash-method construction/first-housing and other special regimes require their own owner decision; not every transaction follows the shorthand. A ПН covers full/partial supplies and advances under 201.7, with the statutory consolidated/special branches. [187.1,201.4/.7](https://tax.gov.ua/nk/).

On that liability date the authorized taxpayer prepares the electronic ПН and signs it using a qualified signature or qualifying advanced signature based on a qualified certificate. Validate the then-effective form under 201.2. Check number/date, actual seller/buyer names and tax identifiers, description/quantity, net price, rate/VAT/gross and goods/service code. The ordinary permission to shorten codes to **at least 4 digits (4 in words on the page)** excludes excisable/imported goods; export customs/contract/forward fields also have specific rules. These are checks, not approval of every current form cell. [201.1-.3](https://tax.gov.ua/nk/).

| Document | Who registers / important exception | Source |
|---|---|---|
| Ordinary supplier ПН | VAT-registered supplier; buyer does not register that supplier's original ПН | [201.8/.10](https://tax.gov.ua/nk/) |
| РК to a ПН issued to a VAT-registered buyer: increase or no net compensation change | Supplier, subject to actual statutory facts | [192.1](https://tax.gov.ua/nk/) |
| РК to that buyer: compensation reduction | **Buyer** registers the seller-created РК; obtain actual receipt date. This corrects the old blanket “only seller registers in ЄРПН” | [192.1](https://tax.gov.ua/nk/) |
| Recipient-created ПН for qualifying nonresident services | VAT-registered recipient under 208.2; not an attempt to register the foreign supplier's Ukrainian ПН | [208.1-.4](https://tax.gov.ua/nk/) |
| Other adjustments, non-buyer invoices, pre 2015 cases, consolidated/special invoices | Apply the exact 192/201/category rules and original dates; do not extend the ordinary party/deadline shorthand automatically | [192.1,201.4/.10](https://tax.gov.ua/nk/) |

Invoices not supplied to the buyer and invoices for exempt supplies also require registration where 201.10 applies. Separate taxable/exempt ПН rules remain. Registration is the ordinary buyer's invoice-based credit evidence, but **198.6/201.11/.12 also recognize specified other documents and exceptions**; do not say every conceivable VAT credit requires a seller ПН. An unregistered ordinary supplier ПН does not provide that invoice-based credit and does not erase the seller's liability. [201.5/.10-.12,198.6](https://tax.gov.ua/nk/).

### 3. Determine the registration deadline and preserve evidence

The **XX.2.89** special deadlines apply during martial law **and 6 months (in words on the page) after the month in which martial law ends/cancels**. Do not revert immediately on its ending date. [89 duration and bands](https://tax.gov.ua/nk/).

| Document/date band | Special 89 deadline | Baseline 201.10, when actually applicable | Official source |
|---|---|---|---|
| Ordinary ПН/РК dated 1-15 inclusive | By **calendar day 5 inclusive of next month** | Last day inclusive of same month | [89,201.10](https://tax.gov.ua/nk/) |
| Ordinary ПН/РК dated 16-last day inclusive | By **calendar day 18 inclusive of next month** | By **calendar day 15 inclusive of next month** | [89,201.10](https://tax.gov.ua/nk/) |
| Seller-created decreasing РК to registered buyer | **18 calendar days from buyer's receipt** | **15 calendar days from buyer's receipt** | [89,201.10](https://tax.gov.ua/nk/) |
| Special consolidated 198.5/199.1, export assurance or another special class | Identify its actual category and operative special rule.201.10 separately describes **20 calendar days after month-end** for those specified consolidated invoices; no ordinary 1-15/16-end assumption | [201.10; special 97 referral](https://tax.gov.ua/nk/) |

Current **11 November 2026** official 1246 explanation gives ordinary operating days **08:00-20:00** on working days; a registration deadline falling on a weekend/holiday/nonworking day is an operating day. During the wartime 1246 p 26 period, a **deadline day runs 00:00-24:00**, and registration/receipt for a deadline-day submission may occur **no later than the next operating day**. These operational rules have their own duration, not automatically 89's six-month tail. Emergency/unscheduled technical work can affect availability. The older ZIR 42060 answer expired 30 October 2026 after 1335; use the current explanation, not the archived answer as present authority. [Current operating-day/receipt rules](https://evp.tax.gov.ua/media-ark/news-ark/1067602.html).

Send early, retain the actual signed file, receipt timestamp/result and ЄРПН query. A local “sent” message is insufficient.201.10 contains a deemed-registration provision where no acceptance/rejection/suspension receipt is sent during the operating day, but reconcile it with the special deadline-day timing and actual system evidence; do not claim automatic acceptance at midnight merely because an expected message is missing. Escalate unexplained absence promptly. [201.10](https://tax.gov.ua/nk/); [current receipt guidance](https://evp.tax.gov.ua/media-ark/news-ark/1067602.html).

**Do not use 365 days as a universal outer registration limit.** The source uses **365 calendar days** for ordinary input-credit carryforward/late-registered credit, subject to cash-method and suspension exceptions; it also uses 365 for certain complaint/explanation processes.192.1 separately limits a РК to **1095 calendar days from the original ПН's preparation date**, with period-specific historical/suspension analysis still necessary. The exact final registration right for an old original ПН remains held for qualified review; no filing-safe outer date is invented. [192.1,198.6,201.10](https://tax.gov.ua/nk/).

The 198.6 credit clock is interrupted for the registration-suspension period. Its cash-method exception addresses credit following actual payment, with a **60 calendar-day** limit from payment/other compensation in the stated conditions. Refer old/cash/blocked invoices and transition periods to the VAT owner rather than discarding credit on a bare 365-day calculation. [198.6](https://tax.gov.ua/nk/).

### 4. Distinguish delay penalties from suspension and nonregistration

For delay of the **89 deadline**, **90** gives the following VAT-amount bands during the same martial-law/six-month-tail period. The taxpayer legally responsible for registration and actual delayed period matter; this is not a final assessment of every invoice class. [89-90,120-1](https://tax.gov.ua/nk/).

| Days late |90 penalty rate on affected invoice VAT | Official source |
|---|---|---|
| Up to 15 calendar days | **2%** | [90](https://tax.gov.ua/nk/) |
|16-30 calendar days | **5%** | [90](https://tax.gov.ua/nk/) |
|31-60 calendar days | **10%** | [90](https://tax.gov.ua/nk/) |
|61-365 calendar days | **15%** | [90](https://tax.gov.ua/nk/) |
|366 or more calendar days | **25%** | [90](https://tax.gov.ua/nk/) |

120-1 has separate baseline/special invoice classes, nonregistration/inspection rules and a suspension-period exception. The old “2%-25% for everything, heavier if never registered” is a warning only, not a complete liability engine. Confirm applicable 90 versus 120-1, excluded/special categories, actual suspension/restoration period, other relief and notices before a penalty output; the complete final client assessment and all nonregistration procedures are **Not yet confirmed** here. Do not treat war or an unresolved block as a blanket waiver. [120-1.1/.2 relevant paragraphs,89-90](https://tax.gov.ua/nk/).

### 5. Reconcile ΣНакл and the electronic VAT account

200-1.2 automatically opens the electronic account; its Treasury payments and the registration limit are different concepts. The exact 200-1.3 formula is:

**ΣНакл = ΣНаклОтр + ΣМитн + ΣПопРах + ΣОвердрафт - ΣНаклВид - ΣВідшкод - ΣПеревищ.** [200-1.2-.3](https://tax.gov.ua/nk/).

Incoming registered invoice/adjustment VAT, including qualifying 208.2 recipient invoices, import VAT, qualifying account top-ups and the statutory overdraft component add to it; issued registered VAT, claimed refunds and defined excess subtract. **Do not subtract the whole VAT return amount again**, as the old simplified formula suggested. Each component has its statutory scope, timing and adjustment rules; overdraft is a defined historic average with registration/quarterly rules, not a bank credit line or money available to spend. [200-1.3](https://tax.gov.ua/nk/).

Under 201.10 an insufficient ordinary limit requires the needed transfer from the taxpayer's own bank/payment-service account to the electronic VAT account. Incoming registrations can change the limit; the specific 200-1.9 excess mechanism is a separate conditional route. Do not tell every blocked taxpayer that depositing money will cure СМКОР, or recompute a live limit from bank balance alone. Verify the current component extract and any conditional 200-1.9 route; the arithmetic case below deliberately freezes other components. This is a cash-flow risk to flag early. [200-1.3/.7/.9,201.10](https://tax.gov.ua/nk/).

### 6. Triage СМКОР and preserve appeal rights

201.16 allows Cabinet-defined suspension. Resolution **1165** is the procedural reference; its complete current text was not recovered directly. Current official explanations identify **unconditional-registration checks, taxpayer-risk criteria, positive tax history and transaction-risk criteria**. The old three-layer summary omitted positive-history conditions; neither a code mismatch nor “same director” alone proves every legal criterion. Obtain the actual reason/decision and current rule. [201.16](https://tax.gov.ua/nk/); [2026 four-check explanation](https://kh.tax.gov.ua/zahodi-dlya-platnikiv/print-990566.html); [October 2026 questions 1-8](https://kr.tax.gov.ua/media-ark/publichni-zahodi/1056851.html).

A shortage of ΣНакл, a technical rejection, a suspended invoice, a taxpayer-risk decision and a Table decision are separate problems. A suspended invoice is awaiting a registration decision, not automatically a final refusal; invoice-based credit is not released merely because documents were uploaded. Keep the old “bought bricks, sold construction services” example as a **diagnostic illustration only**, not proof that genuine conversion of inputs to services must block. The old claim that risk is automatically inherited through a director/founder/accountant is **unconfirmed and held**, pending the actual criterion/evidence. [Risk sequence and code/stock example](https://kr.tax.gov.ua/media-ark/publichni-zahodi/1056851.html).

The **Таблиця даних платника** records normal KVED activities and goods/service input/output codes. Submit it with the required activity explanation linked to tax/financial reports and relevant labor/assets/permits; supporting copies should explain the actual activity, not blindly duplicate everything DPS already holds. An accepted Table is a preventive tool with conditions, **not immunity from every later block or risky status**. Conditional automatic registration of certain previously suspended invoices depends on **all** current 1165 conditions; no unconditional promise is given. [Table explanation](https://lg.tax.gov.ua/media-ark/news-ark/print-1025248.html); [October questions 2/3/5](https://kr.tax.gov.ua/media-ark/publichni-zahodi/1056851.html).

For a suspended ПН/РК, the current official explanation gives **365 calendar days following the liability date shown in it** for explanations/documents under Order 520. This clock is **not** a universal late-registration allowance. Supply relevant contracts/authority, primary supply/stock/transport/invoice/act, settlement/bank and required quality evidence; the list is not exhaustive. Regional decisions and any additional-document request must be diarized separately; the full current regional-response sequence is held for a practitioner rather than guessed. [October questions 1/4](https://kr.tax.gov.ua/media-ark/publichni-zahodi/1056851.html).

A regional refusal may be challenged administratively **within 10 working days following the regional decision date** in the cited current explanation, or judicially; a decision already challenged in court is not simultaneously administratively appealable. Central review is **10 calendar days following receipt** without a requested participation, or **30 calendar days** with participation, with no extension in the explanation. Court limitation/route and every actual service/date/exception require a qualified practitioner. Risky-taxpayer status needs its own evidence challenge; a Table alone does not settle it. [October questions 6-8](https://kr.tax.gov.ua/media-ark/publichni-zahodi/1056851.html).

Do not draft a litigation strategy, certify a Data Table or promise unblocking. Preserve all receipts, the actual decision date, underlying evidence and the qualified practitioner's deadline/action plan.

### 7. Apply РРО/ПРРО by settlement facts, not an obsolete turnover threshold

PRRO is registered software fiscalisation, alongside hardware RRO, using the DPS fiscal server. DPS supplies a free software solution; third-party products also exist and are not universally free. Fiscal receipts are paper/electronic settlement documents, **not** VAT ПН. Confirm registered business unit/PRRO, authorized cashier certificate and actual settlement before use. [Official PRRO FAQ](https://tax.gov.ua/baneryi/programni-rro/aktualni-zapitannya-vidpovidi).

| Taxpayer / settlement | Required test and correction | Official source |
|---|---|---|
| Genuine eligible Group 1 single-tax FOP |296.10 exempts Group 1 from RRO/PRRO. First establish narrow group/activity eligibility. The old “all high-risk goods override every Group 1 exemption” is not a substitute for that statutory test | [296.10,291.4/.7](https://tax.gov.ua/nk/) |
| Groups 2/3, general-system FOP or company taking cash/card settlement transactions | Fiscalise where Law 265 applies, subject to the actual statutory exceptions. The old **220 minimum wages / approximatelyUAH 1900000** trigger is withdrawn as a 2026 permission to avoid RRO; it is not a current general small-business safe harbor | [PRRO FAQ](https://tax.gov.ua/baneryi/programni-rro/aktualni-zapitannya-vidpovidi); [current payment-method explanation](https://tr.tax.gov.ua/media-ark/news-ark/print-1055743.html) |
| Direct credit transfer to seller's bank current-account IBAN | Current October guidance distinguishes the full bank-IBAN transfer route from another electronic payment instrument; preserve the actual account/payment evidence | [2 October 2026 QR/IBAN](https://tr.tax.gov.ua/media-ark/news-ark/print-1055743.html) |
| Card/acquiring/electronic instrument/QR/payment link | A QR label alone is not decisive; fiscalise the applicable instrument route on the general basis. Inspect the actual payment flow | [2 October 2026 QR/IBAN](https://tr.tax.gov.ua/media-ark/news-ark/print-1055743.html) |
| Services paid exclusively through qualifying remote-banking/transfer-service channels | Original 9(14)service-only exception is preserved as a review branch. The opened official 2023 explanation is historical; exact current conditions and product-specific/mixed-payment treatment remain held. It is not a general exemption for all online goods/cards | [2023 official explanation, dated scope](https://nvp.tax.gov.ua/media-ark/news-ark/725416.html) |

Medicines/medical devices, technically complex warranty goods, jewellery/precious metals and excisable goods remain **activity/group-eligibility, stock, licensing and fiscal-exception review flags**. Do not convert them into a blanket claim overriding actual 296.10 or every Law 265 exception. Exact current stock/goods-law exceptions remain held for the records/fiscal owner. [296.10/291](https://tax.gov.ua/nk/); [PRRO FAQ](https://tax.gov.ua/baneryi/programni-rro/aktualni-zapitannya-vidpovidi).

Issue a complete fiscal receipt at the applicable settlement, paper or electronic; a nonfiscal slip/bank acquiring receipt alone does not replace it. Operate with the authorized certificate, send receipts to the fiscal server and generate the required daily Z-report for settlement days. The old **5-10 minute** card-to-fiscal-receipt tolerance is **unconfirmed**, not a safe delay. Authorized offline ranges/caps/emergency rules and later transmission need the current actual conditions; stop and refer if lawful operation cannot be established. [Settlement timing and receipt](https://zp.tax.gov.ua/media-ark/news-ark/print-1009759.html); [daily Z-report](https://rv.tax.gov.ua/media-ark/local-news/1040850.html); [PRRO FAQ, stated scopes](https://tax.gov.ua/baneryi/programni-rro/aktualni-zapitannya-vidpovidi).

For specified incomplete/nonfiscal/no-receipt violations, the current 2026 explanation describes **100%** of affected sales value for the first and **150%** for each subsequent violation from **1 August 2025**. Establish actual violation count, activity, date, territory/relief/force-majeure and scope; full relief and the actual penalty remain held. These are sales-value fiscal penalties, not the VAT-amount late-ЄРПН bands above. [Law 265 art 17(1),29 April 2026 explanation](https://poltava.tax.gov.ua/kampaniya-prro/print-1005661.html).

### 8. Verify electronic identity, authority and receipts

The official Cabinet has public and private parts. Its current help also warns of **wartime identification restrictions on public-register access**, so “public” does not guarantee anonymous access to every register. Modules cover tax returns, ПН/РК/ЄРПН, СЕА, monitoring, PRRO, liabilities and SAF-T according to taxpayer/role. [Official introduction and restriction](https://cabinet.tax.gov.ua/help/intro.html).

Login documentation describes **file/hardware КЕП, MobileID/BankID through id.gov.ua, cloud signatures and Дія.Підпис**. Identification is not proof of signature authority for every document. Validate certificate, role, taxpayer, signing rights and required signature sequence; a seal key is not a person's login signature. ПН201.1 and the electronic-exchange rules allow qualifying advanced signatures based on qualified certificates as specified, not only an unsupported “one signature product for everything”. [Login/authority instructions](https://cabinet.tax.gov.ua/help/login.html); [201.1](https://tax.gov.ua/nk/); [Order 557 procedure](https://cv.tax.gov.ua/media-ark/news-ark/print-1040075.html).

Original provider pointers **ПриватБанк, Privat24, Дія and Вчасно** are retained, but no current accreditation, universal free issuance or pricing claim is certified here. Official documentation supports login methods; it does not prove every bank/Diia/provider offers a free certificate to every applicant. Choose an accepted actual signer and preserve first/second or specific ЄРПН receipts as applicable. No paid provider is required by this skill.

### 9. Route SAF-T UA by actual audit/request status

SAF-T UA is the standardized XML accounting/audit-data file, **not an ordinary periodic tax return** in the current 2026 DPS explanation. The confirmed 85.2 route concerns a **large taxpayer** during a documentary audit, on a request, with electronic documents due **within 2 working days (2 in words on the page) following receipt**. The requested periods and actual large-taxpayer register status matter; the explanation limits the request to periods when the taxpayer was included in that register. Other taxpayers' ordinary audit-record obligations are not waived. [85.2](https://tax.gov.ua/nk/); [2026 DPSquestions 1-3](https://tax.gov.ua/baneryi/saf-t-ua/rozyasnennya--pitannya-vidpovidi/print-980417.html).

**Large taxpayer 14.1.24:** legal person or nonresident PE in Ukraine, last **4 consecutive quarters (4 in words on the page)** with income **over EUR 50000000**, or relevant state-budget tax/fee/payments **over EUR 1500000**, excluding customs payments, converted using the specified weighted-average NBU rate for that same period. This replaces the old **UAH 500000000** revenue test; it is not the financial-reporting enterprise-size threshold. Actual register inclusion and requested periods must also be checked. [14.1.24](https://tax.gov.ua/nk/); [DPSquestion 2](https://tax.gov.ua/baneryi/saf-t-ua/rozyasnennya--pitannya-vidpovidi/print-980417.html).

The official February explanation states **version 2.0 was published 6 November 2024**, and discusses 2024 as the first calendar year it could request under that explanation. Confirm the **then-current actual XSD/technical specification** for an actual request; this is not an assertion that the February package is the latest November 2026 schema. [DPSquestion 1](https://tax.gov.ua/baneryi/saf-t-ua/rozyasnennya--pitannya-vidpovidi/print-980417.html).

The April instructions describe the Cabinet incoming request, separate files for requested periods, archive/XSD checks, authorized electronic signature and a **second receipt accepting or rejecting** the file. A successful upload is not sufficient evidence of acceptance. [Official submission procedure](https://tax.gov.ua/diyalnist-/natsionalna-strategiya-dohodiv/print-1003531.html).

Do not invent a routine SAF-T filing duty for a typical FOP/small taxpayer merely because they are VAT-registered. The old **mid 2025 withdrawal**, “all VAT payers byJanuary 2027” rollout history and **1 January 2026 system launch** claims remain **unconfirmed historical/planning pointers**, not operative mandates or proof of permanent exemption. Future 2027 requirements, individual applicability and actual schema/testing require current official evidence; refer before advising.

## Worked cases

### Original 1: Olena's non-VAT Group 3 foreign-client consulting

**Olena** is a Group 3 FOP on the **5% non-VAT** path, an IT consultant invoicing a foreign client. Confirm actual status/place/transaction, contract, commercial invoice/act and bank evidence. No ordinary supplier ПН/ЄРПН/СЕА/СМКОР from that confirmed non-VAT sale. For a documented direct bank-IBAN credit transfer the fiscal route above applies; “foreign client” alone does not prove a fiscal exemption or a VAT place-of-supply result. Cash/card later changes the settlement analysis. File the applicable single-tax return using an accepted authorized signature/channel; **free Діяissuance is not assumed**. [201.8](https://tax.gov.ua/nk/); [QR/IBAN](https://tr.tax.gov.ua/media-ark/news-ark/print-1055743.html); [login](https://cabinet.tax.gov.ua/help/login.html).

### Original 2: Petro's 8 May 2026 VAT supply

**Petro** is a Group 3 FOP on **3%+VAT**, supplying services on **8 May 2026** for **UAH 120000 including 20%VAT**. Assume 8 May is the ordinary first event (no earlier payment and no cash/special method), standard 20%rate is established and this is an ordinary supplier ПН. Net is **UAH 100000**, VAT **UAH 20000**, derived. It is in the 1-15 band, so 89 gives **5 June 2026** inclusive, derived from the confirmed rule. The buyer's actual credit conditions and registration evidence still need checking; this illustration does not declare registration achieved.

If an actual extract shows only **UAH 18000** available and other components remain fixed, the ordinary shortfall is **UAH 2000**, derived. The needed qualifying top-up is not proof of successful registration or unblocking. Submit early, check the result/query and retain evidence. [187.1,193.1,201.10,89](https://tax.gov.ua/nk/).

```oa-check
name: Petro standard VAT extraction and ordinary registration shortfall
inputs:
  gross: 120000
  vat_rate: 0.20
  available_limit: 18000
steps:
  net: gross / (1 + vat_rate)
  invoice_vat: gross - net
  required_top_up: invoice_vat - available_limit
expected:
  net: 100000
  invoice_vat: 20000
  required_top_up: 2000
```

### Original 3: Petro's suspended invoice

The same **Petro** submits an invoice with output-service codes differing from historic input codes and receives a suspension receipt. Obtain the actual criterion; a genuine transformation of inputs does not itself establish abuse. He and the practitioner prepare explanations/evidence within the applicable 520 clock, evaluate a properly supported Table, separately challenge risky status if present, and preserve refusal/appeal dates. An accepted Table or an uploaded explanation **does not guarantee** every invoice registers. The old “registration restored” outcome is a possible result requiring the actual decision/receipt, not an assumed fact. [October questions 1-8](https://kr.tax.gov.ua/media-ark/publichni-zahodi/1056851.html); [Table](https://lg.tax.gov.ua/media-ark/news-ark/print-1025248.html).

### Original 4: Mariya's Group 2 café card settlements

**Mariya** is a non-VAT Group 2 FOP running a café. Confirm eligibility and the actual cash/card acquiring flow. No ordinary supplier VAT ПН, but applicable fiscal settlements require a registered RRO/PRRO and complete receipts, authorized operation and required daily Z-report. A bank acquiring slip is insufficient. Do not allow an invented 5-10 minute tolerance or the obsolete 220 minimum-wage exemption. The 100%/150% fiscal-violation route is conditional on actual breaches/relief, not an automatically imposed client fine. [296.10/291,201.8](https://tax.gov.ua/nk/); [PRRO](https://tax.gov.ua/baneryi/programni-rro/aktualni-zapitannya-vidpovidi); [payment route](https://tr.tax.gov.ua/media-ark/news-ark/print-1055743.html); [penalties](https://poltava.tax.gov.ua/kampaniya-prro/print-1005661.html).

### Additional arithmetic: reconcile every ΣНакл component

Hypothetical verified component inputs are incomingVAT 25000, importVAT 10000, qualifyingtop-ups 15000, statutoryoverdraft 3000, issuedVAT 30000, refund 2000 and excess 1000. With no other adjustment, limit is **UAH 20000**, derived. A new ordinary invoice with **UAH 24000 VAT** needs **UAH 4000** more qualifying top-up; holding every other component fixed gives 24000 before registration and 0 after it, derived. Actual component movements/special 200-1.9 eligibility or suspension require their own review. This is registration capacity, not a VAT-return liability or unrestricted cash balance. [200-1.3/.9,201.10](https://tax.gov.ua/nk/).

```oa-check
name: Full SEA formula and separate ordinary invoice registration capacity
inputs:
  received: 25000
  customs: 10000
  top_ups: 15000
  overdraft: 3000
  issued: 30000
  refund: 2000
  excess: 1000
  next_invoice_vat: 24000
steps:
  registration_limit: received + customs + top_ups + overdraft - issued - refund - excess
  additional_top_up: next_invoice_vat - registration_limit
  limit_before_registration: registration_limit + additional_top_up
  remaining_limit: limit_before_registration - next_invoice_vat
expected:
  registration_limit: 20000
  additional_top_up: 4000
  limit_before_registration: 24000
  remaining_limit: 0
```

## When to refuse or refer

1. Do not issue a VAT ПН for a confirmed non-VAT FOP's ordinary sale or confuse it with a commercial invoice/fiscal receipt. Confirm unknown status; preserve 208 special imported-service obligations rather than promising no VAT duties.
2. Do not tell an ordinary buyer to register the seller's original ПН. Identify buyer-decreasing РК and recipient-created 208.2 exceptions before saying “seller only”.
3. Do not release a deadline without the actual document/category,89 period/tail,201.10 baseline and current operating-day/receipt rules. Old 365 registration backstop is not usable.
4. Do not issue final late-registration/nonregistration/fiscal penalties or a fiscal-turnover/SAF-T threshold from old approximations; use the actual statutory base, date, scope and relief. No 220 minimum-wage general 2026 safe harbor.
5. Do not present SAF-T as routine periodic reporting for all FOPs or all VAT payers, or promise permanent immunity. Actual audit/request/register/XSD/future-year evidence controls.
6. Refer СМКОР explanations, Data Tables, risky-status removal, refusals and litigation to a qualified Ukrainian practitioner. No guaranteed unblock, fabricated invoices or invented evidence; do not miss a deadline while waiting.
7. Do not finalize an electronic filing without the authorized accepted signature/form and required receipt/registration evidence. Cabinet is the official workflow here; lawful accepted other software routes are not automatically prohibited.
8. Do not replace qualified review/sign-off. Refer complex export assurance, cash-method/old-credit, adjustment history, offline fiscalisation, special sectors and unresolved status/source gaps to their domain owner.

Before completion, confirm VAT/group/effective dates; the legal document, registering party, first event, rate and base; the actual deadline and operating time; valid certificate and signer rights; primary and fiscal proof; current limit, components and top-up; actual registration and receipt; separate suspension, risky-status, Table and appeal plans; and any actual SAF-T request/register obligation. Never fill a missing fact with zero or assume a sent file was accepted. Register early as a process control, not an invented shorter legal deadline.

## Sources

| Official source | Read for | Read date |
|---|---|---|
| [Tax Code,official DPS consolidation](https://tax.gov.ua/nk/) | Read for 187.1 first event, service-document and cash-method neighbors;192.1 registering parties/RK 1095;198.6 credit 365/cash 60/suspension;200-1.2/.3 formula/components/overdraft/.7/.9;201.1-.3/.5/.7-.10 relevant fields, registration, credit, receipt, deadlines and top-up;201.16;208.1-.7;14.1.24/85.2; complete XX.2.89-.90;120-1.1 exceptions/suspension and 120-1.2 opening. Genuine same-day 181/182/193/293/296.10 reads reused. Not whole Code, all special regimes, entire penalty procedures or later-law commencement. | 2026-11-15 |
| [DPS,11 November 2026: operating day/receipts](https://evp.tax.gov.ua/media-ark/news-ark/1067602.html) | Read for Full operative 65-85: current 1246 ordinary 08-20 hours, maintenance exceptions, weekend deadline, wartime deadline-day 00-24 hours, next-operating-day receipt, query and evidence. Print failed; normal public body read. | 2026-11-15 |
| [DPS,12 March 2026: risk checks](https://kh.tax.gov.ua/zahodi-dlya-platnikiv/print-990566.html) | Read for Whole 18 lines: four checks, positive history and preventive Table concept. No approval of every numeric threshold/exception in its example. | 2026-11-15 |
| [DPS,6 October 2026: suspension questions](https://kr.tax.gov.ua/media-ark/publichni-zahodi/1056851.html) | Read for Full Q 1-Q 8, operative 68-126:365-day explanation clock, Table evidence, risk sequence, documents, conditional Table effect, refusal appeal 10 working days, central review 10/30 calendar days and risky-status challenge. Not all Q 9/remainder, full 1165/520 or court limitation law. | 2026-11-15 |
| [DPS,30 June 2026: Table explanation](https://lg.tax.gov.ua/media-ark/news-ark/print-1025248.html) | Read for Full 29 lines:1165 Table, activity/input/output codes, mandatory explanation, reports/resources, optional copies and no repeat accepted codes. | 2026-11-15 |
| [DPS,10 February 2026: SAF-T questions](https://tax.gov.ua/baneryi/saf-t-ua/rozyasnennya--pitannya-vidpovidi/print-980417.html) | Read for All 3 questions/36 lines:85.2 audit request,2 working days,1393,2.0 published 6 November 2024, first year 2024, register periods,14.1.24, not a tax return and general-liability boundary. No current XSD execution. | 2026-11-15 |
| [DPS,22 April 2026: SAF-T submission](https://tax.gov.ua/diyalnist-/natsionalna-strategiya-dohodiv/print-1003531.html) | Read for Whole 55 lines: private incoming request, separate-period archives, XSD, signature/right checks, second receipt and 2-level validation. No authenticated client test. | 2026-11-15 |
| [Official Cabinet introduction](https://cabinet.tax.gov.ua/help/intro.html) | Read for Operative 55-214: public/private parts, wartime register-identification warning and PN/RK, SEA, risk, PRRO and SAF-T modules. No authenticated session. | 2026-11-15 |
| [Official Cabinet login](https://cabinet.tax.gov.ua/help/login.html) | Read for Whole operative 59-150: file/hardware/cloud/Diia/BankID/MobileID, authority, certificate and seal boundary. Not all provider prices or actual signup. | 2026-11-15 |
| [DPS PRRO FAQ](https://tax.gov.ua/baneryi/programni-rro/aktualni-zapitannya-vidpovidi) | Read for Genuine same-day bookkeeping reading reused: FAQ 3/7-11/15/18-19 plus applicable receipt/Z/offline questions; software/hardware, free DPS option, registration, certificates and receipts. Complete current offline caps/exceptions held. | 2026-11-15 |
| [DPS,2 October 2026: QR and IBAN](https://tr.tax.gov.ua/media-ark/news-ark/print-1055743.html) | Read for Genuine same-day full operative body: bank-IBAN credit transfer distinguished from another payment instrument; QR alone is not decisive. | 2026-11-15 |
| [DPS,29 April 2026: fiscal penalties](https://poltava.tax.gov.ua/kampaniya-prro/print-1005661.html) | Read for Genuine same-day full operative body: specified Law 265 art 17(1) violations 100/150 from 1 August 2025; old 25/50 route ended 31 July 2025 with conditions. Not complete current relief or client assessment. | 2026-11-15 |
| [DPS,7 November 2023: service exception](https://nvp.tax.gov.ua/media-ark/news-ark/725416.html) | Read for Genuine same-day full 2023 body:9(14) remote-bank/transfer-service-only branch and goods/mixed limits. Historical explanation, not current product-specific assurance. | 2026-11-15 |
| [DPS: Order 557 electronic procedure](https://cv.tax.gov.ua/media-ark/news-ark/print-1040075.html) | Read for Genuine same-day full assembly source: qualified/qualifying advanced signature, seal if present, authority, format and first/second receipts. Login does not prove authority to sign every filing. | 2026-11-15 |

| [DPS: settlement methods and receipt timing](https://zp.tax.gov.ua/media-ark/news-ark/print-1009759.html) | Read for Genuine same-day full bookkeeping source: actual payment chain, applicable Law 265 exceptions, bank slip versus fiscal document and receipt timing. Not every brand or current stock exception certified. | 2026-11-15 |
| [DPS: daily Z-report and interruption](https://rv.tax.gov.ua/media-ark/local-news/1040850.html) | Read for Genuine same-day full bookkeeping source: daily Z where settlements occurred, vending exception and interruption/next-working-day conditions. No universal outage waiver. | 2026-11-15 |

Not yet confirmed: full current 1165/520/1246 statutory texts and all numeric risk, unconditional-registration, Table and automatic-release conditions; the actual risky-status inheritance criterion; full regional additional-document/decision sequence and court limitation rules; final registration right for an old original PN, including period-specific stops and transitions; complete 120-1/90 interaction, relief, nonregistration and final penalties; exact current Law 265 stock/goods, service-only, offline and emergency exceptions; the old 5-10 minute receipt tolerance; all provider accreditation and free-certificate claims; mid 2025 SAF-T withdrawal, the all-VAT-by-January 2027 rollout history and 1 January 2026 launch; actual current XSD/testing and 2027 mandates; individual VAT status, place, rate, document, schema, signature, receipt and unblocking facts. No inaccessible response, archived answer or search snippet was counted as current operative authority.

The original **PwC Worldwide Tax Summaries** reference is retained as a withdrawn secondary research pointer, not authority or a claim it was read. Current rules above use the named official sources. Old May 2026“research-verified” wording is not inherited as a current review claim.

## Disclaimer

This is bounded source-cited reference material contributed by the Open Accountants Community. It records actual source scopes and unresolved branches; rules, forms, registry operations and martial-law measures change. Every actual output needs current applicable evidence and qualified review before filing or action.

It is **pending sign-off by a qualified Ukrainian accountant or auditor** and is **not** a substitute for professional advice or for credentialed review of any specific filing. Use at your own risk. Part of the openaccountants.com open-source skill library.
