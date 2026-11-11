---
name: philippines-vat
description: >
  Use this historical 2025 Philippine VAT reference to examine registration,
  output tax, input evidence, digital services and BIR return preparation for
  Philippine businesses. Match requests about Philippines VAT, Form 2550Q,
  optional Form 2550M, input VAT, invoices, percentage tax boundaries and
  nonresident digital service purchases. It preserves supplier discovery
  patterns and hypothetical transaction examples whilst requiring evidence
  of the actual supply, taxpayer status and period. Several statutory,
  regulatory and form discrepancies remain unresolved. This Tier 2 draft
  supports source checking and reviewer questions; it does not authorise
  filing, payment, a tax position or an operational VAT working paper.
version: 2.2
jurisdiction: PH
tax_year: 2025
tax_year_notes: Historical 2025 reference; period-specific law, commencement, later amendments, registration, channels and professional approval remain required. Editing in November 2026 does not establish 2026 law.
last_updated: 2026-11-05
depends_on:
  - vat-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
domain: vat-gst
---

# Philippines VAT v2.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

This reference covers Philippine VAT in PHP, historical 2025 transactions, ordinary goods/services, domestic and import input evidence, zero/exempt boundaries, registration, quarterly Form 2550Q, optional Form 2550M and purchases from digital service providers. A taxpayer may use a calendar or fiscal period; obtain the actual registered accounting period rather than assuming 31 December.

### What this file is

This is a historical country reference loaded above [vat-workflow-base](../../foundation/vat-workflow-base.md) and [workflow-base](../../foundation/workflow-base.md). Follow both bases, including the universal Section 7 and VAT Section 7 contracts, before operational work. The reviewer receives the eventual working paper and brief and must approve the position.

**Operational hold.** Canonical headings and arithmetic examples do not complete those contracts. The applicable non-EU regional layer, complete period-specific law, validated supplier classifications, every refusal/default/question slot, exact workbook and return mappings, at least 5 fully qualified universal positions and 6 fully worked VAT transaction classifications, all 14 VAT checks and all 18 universal checks remain to be demonstrated. This guide's 6 conditional transaction illustrations do not certify those requirements. Stop before producing or delivering an operational workbook, return or filing instruction whilst any required slot or source condition remains unresolved.

Earlier versions credited Jonathan I. Ruiz, CPA, for specified source corrections. That historical attribution is retained; it is not a review or approval of this version. Current professional review is pending.

## Rates, bands and thresholds

| Item | Amount or rule | Source and limit |
| --- | --- | --- |
| Ordinary standard VAT | 12% of the legally established base | Form instructions for goods/services/imports; [RA 12023 s 2/NIRC 108](https://lawphil.net/statutes/repacts/ra2024/pdf/ra_12023_2024.pdf) for services. Actual supply, commencement and later law must be confirmed. No sale defaults to 12% because its facts are unknown. |
| Zero rate | 0% only after the relevant conditions are established | [TRAIN ss 31/33 displayed amendments to NIRC 106/108](https://lawphil.net/statutes/repacts/ra2017/ra_10963_2017.html) and the form distinguish zero-rated sales. They are not a complete 2025 export/incentive chain. Foreign payment, a nonresident name, PEZA/BOI status or international transport alone does not establish entitlement. |
| Reduced rate | Unverified: no separate ordinary reduced rate qualified by this source set | Do not treat exemption as a reduced rate or invent one for a transaction. |
| Residual turnover exemption/registration | EOPT NIRC 109(CC) displays PHP 3,000,000 and CPI adjustment every 3 years; NIRC 236(F) uses past/expected next 12-month tests and specified exempt-sales exclusions | [EOPT ss 18/34](https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/2/96948), later [RA 12023 s 11](https://lawphil.net/statutes/repacts/ra2024/pdf/ra_12023_2024.pdf). Actual indexed amount, effectivity and taxpayer classification remain unconfirmed. Do not use a calendar-year PHP 3 million shortcut to cancel registration or decide liability. Optional registration and its 3-year restriction require the actual conditions. |
| Percentage tax boundary | EOPT NIRC 116 displays 3% of covered gross quarterly sales, with its cooperative exception and historical 1% interval ending 30 June 2023 | [EOPT s 24](https://lawphil.net/statutes/repacts/ra2024/pdf/ra_11976_2024.pdf). Complete eligibility, any income-tax election and later amendments remain required. Do not impose 3% on every person below the threshold. |
| Housing selling-price threshold | RR 1-2024 expressly adjusts the relevant house-and-lot/other residential-dwelling threshold from PHP 3,199,200 to PHP 3,600,000, stated from 1 January 2024 | [Full RR 1-2024 ss 1–6](https://bir-cdn.bir.gov.ph/BIR/pdf/RR%20No.%201-2024.pdf). Property type, statutory conditions, commencement/publication and later law still matter. This is not a general exemption for every property below the figure or a qualified 2027 amount. |
| Residential rent and other exemptions | Earlier TRAIN displayed PHP 15,000 monthly residential-unit rent and specified exemptions | [TRAIN s 34/NIRC 109](https://lawphil.net/statutes/repacts/ra2017/ra_10963_2017.html). Current-period housing/rent, agriculture, education, medical/hospital, literary/musical works, life insurance, common carriers, medicines and import exemptions need the complete operative conditions. The former blanket lists are listed individually in the topic-conditions table and Not yet confirmed line. |

The inherited PHP 500,000 single-transaction, PHP 60,000 single-position tax-difference, >40% counterparty concentration and PHP 200,000 absolute net-position thresholds are **editorial review signals**, not tax law or permission to omit smaller issues. Retain the former >4-default signal as a count of unresolved factual items, without defaulting law or classifying unknown transactions. Every material uncertainty is asked regardless of size; the small-value question-filter threshold and complete base question contract remain unvalidated.

## The base

### Step 1 : Establish the supply, period and base

Separate consideration from transfers, principal, statutory payments and genuinely refundable deposits using actual documents. A bank credit is not automatically a sale, an inward remittance not automatically an export and a payment not automatically an expense or input claim. Track advances, security deposits, applied deposits, refunds and reversals to the actual contract and recognition rule.

[EOPT ss 16–17](https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/2/96948) and [full RR 3-2024 ss 2–3](https://naro.law.upd.edu.ph/storage/01JT27FB5GV836PNJHD2B7EMAT.pdf) change goods/services to gross-sales/accrual rules with defined bases, exclusions, returns/allowances/discounts and service-performance conditions. For qualifying long-term contracts of at least 1 year, the monthly invoicing provision matters. Do not carry forward an unqualified receipts basis or recognise every service invoice regardless of performance. RR 3 s 7 separately addresses pre-effectivity receivables. Exact commencement and the entire later chain remain held.

For an **already established** wholly standard-rated VAT-inclusive amount, net = gross / 1.12 and VAT = gross − net. For an established exclusive base, VAT = base × 0.12. Do not use these formulae to decide whether an invoice, pass-through charge, foreign exchange item, mixed supply or tax-inclusive contract is taxable. Import VAT uses the customs base and evidence in the form instructions, rather than a bank transfer divided by 1.12.

### Step 2 : Qualify input, invoices and adjustments

Read [full RR 7-2024 ss 2–6](https://naro.law.upd.edu.ph/storage/01JT28MCBF1J9NSBJX7WGXCMT6.pdf), [full RR 11-2024](https://bir-cdn.bir.gov.ph/BIR/pdf/RR%20No.%2011-2024.pdf) and [full RMC 77-2024](https://naro.law.upd.edu.ph/storage/01JW7NJJTNTTCY1EK1P4SH8PZ7.pdf) together. VAT invoices are required regardless of value. Supplementary receipts are not generally input support; proper converted documents and NRDSP invoices have specific exceptions.

For non-VAT sellers, RR 7 s 6(A) and RMC 77 A2 state PHP 500 or more, with an invoice at any amount on buyer request. RR 7 also requires a day-end invoice for subthreshold sales totalling at least PHP 500, whereas RMC 77 A3 prints 'more than PHP 500' and an aggregate that 'exceeded' PHP 500. Hold the exact-PHP-500 boundary and applicable indexation for professional resolution. VAT-registered sellers must still invoice every sale regardless of amount.

RR 7 s 3(D) and RMC 77 A28–29 contain purchaser-credit rules for erroneous nonregistered-seller VAT invoices and certain missing particulars. Do not use a blanket 'unregistered seller means no input' or 'any defect means no input' rule. Check the exact rule and its conditions, including the essential sales amount, VAT amount, registered names/TINs, description and date. Preserve mixed-sales breakdown, buyer-detail qualifications, VAT journals, ticket requirements, ATP/loose-leaf/CAS differences and record-retention conditions. RMC 77 A14–16 distinguishes billing from collection and prevents a duplicate invoice merely on collection. Electronic invoice compliance is not established by calling a provider 'eFPS registered'. Later electronic-invoicing mandates remain unreviewed.

**Service-input timing conflict:** EOPT s 19/NIRC 110 describes VAT accrued on services; later RA 12023 s 6 expressly repeats credit upon payment for services/lease/use. Signed text confirms the payment wording, rather than merely an HTML typo. This reference does not choose a universal accrual or payment rule. Identify the transaction, dates, applicable amendments and professional resolution before taking the credit.

**Uncollected receivables:** EOPT NIRC 110(D) and RR 3 s 5 permit the seller's output deduction in the next quarter after the agreed period lapses, subject to the actual conditions: post-effectivity credit sale, written term, separate VAT, specific sales-list reporting, timely output declaration, elapsed agreed/extended period, full VAT payment and no VAT-component bad-debt deduction. Restore output in the recovery period. This is not a universal buyer-input reversal, bad-debt deduction or permission to implement fields 55/58. Their complete authority and the printed formula discrepancy remain held.

Direct attribution and mixed exempt allocation, imports, business/private use, vehicles, entertainment, transitional inventory input, presumptive input, capital-goods legacy amortisation, carryforward, withholding credits and refund/TCC claims each require their own entitlement and timing evidence. Do not turn the form's existence of a field into permission to claim it. The old universal vehicle exclusivity rule and income-tax entertainment ceilings are not established as VAT recovery rules by this source set.

### Reconciliation step: Reconcile the working paper before output

The earlier A/B/C sketch was a workpaper, not the statutory form. Replace its automatic input allowance, generic CWT subtraction and 'refund' result with qualified components in the actual form map. Reconcile sales, adjusted output, current and carried input, separate adjustments, applicable VAT credits, amended payments and penalties. Explain every difference to the ledger, bank, invoices and previous return. An excess-input balance, excess-payment balance, credit carryforward and refund application are distinct outcomes.

The eventual workbook must meet the base's Transactions, Box Summary and Return Form layout, supporting worksheets and reviewer brief. Record the actual return version and valid box codes in the country mapping. Preserve flags for invoice proof, export evidence, incentive certification, digital withholding, vehicle restrictions and entertainment analysis, without treating any single checkbox as entitlement. No workbook template, filing total or deliverable is approved by this reference whilst the operational hold remains.

### Topic conditions and remaining source gaps

| Preserved topic | Required qualification or specific hold |
| --- | --- |
| Exports, foreign services, PEZA/BOI and international transport | The complete period-specific NIRC 106/108 and CREATE/CREATE MORE/incentive amendment chain, transaction/activity, recipient, use, documentary and FX conditions are not established. No automatic zero-rating from a foreign receipt, remittance, certificate or flight description. |
| Agriculture, education, medicine and medical/hospital services | Read the actual product/service, institution/accreditation, recipient and exemption/amendment conditions. The old 'prescription exempt/OTC taxable' shortcut and broad basic-necessities import exemption are withdrawn pending the applicable complete units. Digital education/platform rules do not settle ordinary medical/education supplies. |
| Literary/musical works, life insurance, common carriers and financial services | Complete applicable exemption/type-of-supply conditions and later amendments remain unconfirmed. A supplier name or financial-looking fee does not qualify the exemption. |
| Housing and residential rent | RR 1-2024's specified selling-price adjustment is read. Other property conditions, rent's complete operative chain and actual later indexation remain held. Do not generalise this threshold to all real estate. |
| Vehicles, private/mixed use and entertainment | Obtain actual use, invoice and complete VAT restriction/allocation law. Neither universal exclusive-business-use wording nor income-tax entertainment deduction ceilings is qualified as a VAT rule. Do not label an undocumented expense personal merely to close it. |
| Transitional inventory, presumptive input and capital goods | Former '2% or actual, whichever higher' inventory wording requires complete NIRC 111 and implementing conditions, not yet read. Historical capital input and amortisation require acquisition dates, period-specific law, remaining schedules and no duplication; a current form line does not revive an expired regime. |
| Carryforward, allocation, withholding and refunds | Trace prior balances to returns and claim/payment evidence. Full allocation and refund law/claims procedures are not established. Government VAT withholding is not all final withholding; income-tax CWT is not automatically a VAT credit. |
| Invoice transitions and electronic systems | RR 11 modifies the original RR 7 cut-offs and differentiates converted manual/loose-leaf from machine/system documents. Read actual conversion, particulars, inventory, notice and extension conditions. RMC 77's Annex C still prints a 31 December 2024 limit, unlike its manual-conversion answers; A22 names E/F whilst Q22/table name C/D. These printed discrepancies were visually confirmed and remain disclosed, not silently repaired. Later electronic-invoicing rules and exact period availability remain unreviewed. |

### Supplier discovery library

All 76 original named pattern rows are retained below, in their original 9 groups. Case-insensitive, most-specific matching is only a discovery aid. Every row maps to **Needs Input** under its group rule; it establishes no contracting entity, rate, residence, exemption or credit. Do not override verified transaction facts with a brand match. Missing fuel, hotel, office-supply, coworking and insurance categories, plus full coverage of Adobe, Apple, Dropbox, LinkedIn and Atlassian, remain explicit library gaps. The minimum library categories and mandatory operational country-slot qualification remain held; adding names does not establish the required legal classifications.


#### 3.1 Banks and wallets: discovery only

| Pattern | Treatment |
| --- | --- |
| BDO UNIBANK, BANCO DE ORO | Needs Input under group 3.1 rule below. |
| BANK OF THE PHILIPPINE ISLANDS, BPI | Needs Input under group 3.1 rule below. |
| METROBANK, METROPOLITAN BANK | Needs Input under group 3.1 rule below. |
| UNIONBANK OF THE PHILIPPINES | Needs Input under group 3.1 rule below. |
| SECURITY BANK | Needs Input under group 3.1 rule below. |
| LANDBANK OF THE PHILIPPINES, LBP | Needs Input under group 3.1 rule below. |
| PHILIPPINE NATIONAL BANK, PNB | Needs Input under group 3.1 rule below. |
| CHINA BANKING, CHINABANK | Needs Input under group 3.1 rule below. |
| RCBC, RIZAL COMMERCIAL BANKING | Needs Input under group 3.1 rule below. |
| GCASH, G-XCHANGE (GXI) | Needs Input under group 3.1 rule below. |
| MAYA, PAYMAYA | Needs Input under group 3.1 rule below. |
| SEABANK | Needs Input under group 3.1 rule below. |
| SERVICE CHARGE, BANK FEE, INTEREST | Needs Input under group 3.1 rule below. |

#### 3.2 Government and statutory names: discovery only

| Pattern | Treatment |
| --- | --- |
| BUREAU OF INTERNAL REVENUE, BIR | Needs Input under group 3.2 rule below. |
| BUREAU OF CUSTOMS, BOC | Needs Input under group 3.2 rule below. |
| SOCIAL SECURITY SYSTEM, SSS | Needs Input under group 3.2 rule below. |
| PHILHEALTH | Needs Input under group 3.2 rule below. |
| PAG-IBIG, HDMF | Needs Input under group 3.2 rule below. |
| SEC PHILIPPINES | Needs Input under group 3.2 rule below. |
| LGU, BARANGAY, CITY HALL | Needs Input under group 3.2 rule below. |

#### 3.3 Utilities and telecoms: discovery only

| Pattern | Treatment |
| --- | --- |
| MERALCO, MANILA ELECTRIC | Needs Input under group 3.3 rule below. |
| CEPALCO (Cagayan de Oro electric) | Needs Input under group 3.3 rule below. |
| VECO (Visayas Electric) | Needs Input under group 3.3 rule below. |
| MANILA WATER | Needs Input under group 3.3 rule below. |
| MAYNILAD WATER SERVICES | Needs Input under group 3.3 rule below. |
| PLDT, PHILIPPINE LONG DISTANCE | Needs Input under group 3.3 rule below. |
| GLOBE TELECOM | Needs Input under group 3.3 rule below. |
| SMART COMMUNICATIONS, SMART | Needs Input under group 3.3 rule below. |
| DITO TELECOMMUNITY | Needs Input under group 3.3 rule below. |
| CONVERGE ICT | Needs Input under group 3.3 rule below. |

#### 3.4 Transport and logistics: discovery only

| Pattern | Treatment |
| --- | --- |
| PHILIPPINE AIRLINES, PAL | Needs Input under group 3.4 rule below. |
| CEBU PACIFIC | Needs Input under group 3.4 rule below. |
| AIRASIA PHILIPPINES | Needs Input under group 3.4 rule below. |
| PHILIPPINE NATIONAL RAILWAYS, PNR | Needs Input under group 3.4 rule below. |
| LRT, MRT (Metro Rail Transit) | Needs Input under group 3.4 rule below. |
| GRAB PHILIPPINES | Needs Input under group 3.4 rule below. |
| ANGKAS | Needs Input under group 3.4 rule below. |
| LBC EXPRESS | Needs Input under group 3.4 rule below. |
| JRS EXPRESS | Needs Input under group 3.4 rule below. |
| DHL PHILIPPINES | Needs Input under group 3.4 rule below. |
| FEDEX PHILIPPINES | Needs Input under group 3.4 rule below. |
| 2GO EXPRESS | Needs Input under group 3.4 rule below. |
| NINJA VAN PHILIPPINES | Needs Input under group 3.4 rule below. |
| J&T EXPRESS PHILIPPINES | Needs Input under group 3.4 rule below. |

#### 3.5 Food and retail: discovery only

| Pattern | Treatment |
| --- | --- |
| SM SUPERMARKET, SM MARKETS | Needs Input under group 3.5 rule below. |
| ROBINSONS SUPERMARKET | Needs Input under group 3.5 rule below. |
| PUREGOLD | Needs Input under group 3.5 rule below. |
| S&R MEMBERSHIP SHOPPING | Needs Input under group 3.5 rule below. |
| MERCURY DRUG | Needs Input under group 3.5 rule below. |
| WATSONS PHILIPPINES | Needs Input under group 3.5 rule below. |
| 7-ELEVEN PHILIPPINES | Needs Input under group 3.5 rule below. |
| JOLLIBEE (eat-in) | Needs Input under group 3.5 rule below. |
| MCDONALD'S PHILIPPINES | Needs Input under group 3.5 rule below. |

#### 3.6 Digital supplier names: discovery only

| Pattern | Treatment |
| --- | --- |
| GOOGLE (Workspace, Ads, Cloud) | Needs Input under group 3.6 rule below. |
| MICROSOFT (365, Azure) | Needs Input under group 3.6 rule below. |
| META, FACEBOOK ADS | Needs Input under group 3.6 rule below. |
| NETFLIX | Needs Input under group 3.6 rule below. |
| ZOOM | Needs Input under group 3.6 rule below. |
| SLACK | Needs Input under group 3.6 rule below. |
| NOTION, OPENAI, ANTHROPIC | Needs Input under group 3.6 rule below. |
| AWS | Needs Input under group 3.6 rule below. |

#### 3.7 Payment processors: discovery only

| Pattern | Treatment |
| --- | --- |
| PAYPAL (transaction fees) | Needs Input under group 3.7 rule below. |
| STRIPE (transaction fees) | Needs Input under group 3.7 rule below. |
| GCASH (transaction fees) | Needs Input under group 3.7 rule below. |
| PAYMONGO (fees) | Needs Input under group 3.7 rule below. |
| DRAGONPAY (fees) | Needs Input under group 3.7 rule below. |

#### 3.8 Professional service names: discovery only

| Pattern | Treatment |
| --- | --- |
| CPA FIRM, ACCOUNTING FIRM | Needs Input under group 3.8 rule below. |
| LAW FIRM, ATTY, ATTORNEY | Needs Input under group 3.8 rule below. |
| NOTARY PUBLIC | Needs Input under group 3.8 rule below. |
| ADVERTISING AGENCY | Needs Input under group 3.8 rule below. |

#### 3.9 Transfers and payment descriptions: discovery only

| Pattern | Treatment |
| --- | --- |
| INTER-ACCOUNT TRANSFER, OWN ACCOUNT | Needs Input under group 3.9 rule below. |
| LOAN PROCEEDS, LOAN REPAYMENT | Needs Input under group 3.9 rule below. |
| SALARY, PAYROLL | Needs Input under group 3.9 rule below. |
| DIVIDEND | Needs Input under group 3.9 rule below. |
| SECURITY DEPOSIT, ADVANCE DEPOSIT | Needs Input under group 3.9 rule below. |
| ATM WITHDRAWAL, CASH WITHDRAWAL | Needs Input under group 3.9 rule below. |

Group rules: **3.1 banks:** establish the actual financial service and qualifying institution; do not exempt every payment to a bank or wallet. **3.2 government/statutory:** establish the tax, contribution, fee or purchased supply; separately identify customs VAT, which may require its own input proof. **3.3 utilities:** inspect the actual issuer, bill components, applicable tax and business-use/invoice conditions; a utility name proves no credit. **3.4 transport/logistics:** establish route, mode, carrier, freight/passenger service, pass-throughs and ticket/invoice before choosing a rule; land/mass-transit names do not establish 12%. **3.5 food/retail:** inspect each product/service and exemption conditions; do not classify the whole basket or every prescription by brand. **3.6 digital:** apply Step 3 to the actual seller, buyer, supply, consumption, contract and payment; hold any statutory-scope issue. **3.7 processors:** identify actual fee/service and qualifying financial-institution conditions; PayPal/Stripe/payment-gateway labels alone do not establish exemption. **3.8 professionals:** determine the actual supplier, tax status, service, invoice and any applicable erroneous-invoice exception. **3.9 transfers:** prove internal movement, principal, wage, distribution or deposit treatment; do not infer it from text. Security/advance deposits require application and recognition facts; cash withdrawals require the underlying use.


### Bank exports and language cues

The earlier formats below are illustrative, unverified export conventions, not current product specifications. Read the actual header, dates, signs, currencies, posting/value dates and balance arithmetic before importing. Preserve source text and avoid duplicates, sign reversal, currency mixing or invented VAT from a bank column.

| Earlier bank label | Illustrative columns/date cue |
| --- | --- |
| BDO | Date, Reference, Description, Debit, Credit, Balance; MM/DD/YYYY |
| BPI | Date, Transaction Reference, Description, Withdrawal, Deposit, Balance; MM/DD/YYYY |
| Metrobank | Date, Description, Debit, Credit, Balance; MM/DD/YYYY |
| UnionBank | Date, Description, Debit, Credit, Available Balance; MM/DD/YYYY |
| Landbank | Posting Date, Description, Debit, Credit, Running Balance; MM/DD/YYYY |

All 8 original terms remain discovery cues: CREDIT/DEPOSIT may be incoming funds; DEBIT/WITHDRAWAL may be outgoing; INWARD REMITTANCE may be foreign receipt; SERVICE CHARGE and INTEREST need the actual service/institution analysis; BALANCE is a control amount; ATM WITHDRAWAL requires the underlying use; PAYROLL DEBIT requires confirmation as wages rather than a purchased service. None determines VAT by itself.

## Deadlines and filing

The [April 2024 Form 2550Q instructions](https://bir-cdn.bir.gov.ph/BIR/pdf/2550Q%20guidelines%20April%202024_final.pdf) name both VAT-registered persons and persons required to register who failed. They state that filing continues until cancellation, including quarters with no taxable transactions or sales below the threshold, and prescribe a consolidated head-office return including branches. Imports use the relevant customs form. Confirm the actual taxpayer's obligations and later rules.

| Return or event | Qualified historical rule and remaining condition |
| --- | --- |
| Form 2550Q | General filing/payment within 25 days after each taxable quarter: [TRAIN s 37](https://lawphil.net/statutes/repacts/ra2017/ra_10963_2017.html), [EOPT s 22](https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/2/96948) and the form instructions. Determine the actual period, weekends/holidays, applicable eFPS issuance and special relief before stating a calendar date. |
| Optional Form 2550M | [Full RMC 5-2023](https://bir-cdn.bir.gov.ph/local/pdf/RMC%20No.%205-2023%20(1).pdf) removes the monthly requirement from 1 January 2023. [Full RMC 52-2023](https://bir-cdn.bir.gov.ph/local/pdf/RMC%20No.%2052-2023%20(1).pdf) permits monthly filing/payment without a prescribed monthly deadline; switching does not itself attract a penalty. Quarterly filing/payment remains required. Its incorporated procedures and actual monthly form version are not fully qualified here. |
| Payment/cancellation | The instructions prescribe payment with the quarterly return and a separate return/payment within 25 days of cancellation. Confirm effective cancellation, liabilities and the applicable channel. Ordinary quarterly VAT is not the taxpayer's only possible return: digital withholding, percentage tax and other obligations require their own analysis. |

### Channels, attachments and actual form

The instructions contemplate electronic platforms, manual filing when unavailable and electronic or authorised manual payment. [RMC 68-2024, all 3 pages](https://bir-cdn.bir.gov.ph/BIR/pdf/RMC%20No.%2068-2024.pdf) describes a dated rollout: existing electronic versions generally, but the revised manual form where new fields 35, 36, 55 or 58 apply. It lists payment channels and conditions. It does not establish availability of those channels or versions for a later engagement. The circular's body date is 30 May 2024; receipt stamps say 19 June. Do not substitute one for the other.

Check the actual eFPS/eBIRForms/manual return, authorised payment route, operating cut-offs, acknowledgements and conditional attachments before filing. The form instructions list VAT-withholding certificates, SAWT where applicable, approved debit/credit documents, amended-return payment proof and representative authority. Those documents are not interchangeable. The form/instructions use a 14-digit TIN including a 5-digit branch code; the old 9/12-digit shorthand is insufficient for populating this form.

The [actual April 2024 Form 2550Q](https://bir-cdn.bir.gov.ph/BIR/pdf/RMC%20No.%2068-2024%20Annex%20A.pdf) has Part I background, Part II total payable, Part III payment, Part IV computation and Part V schedules. The old schematic Parts I-A through VIII did not match this form or establish Form 2550M fields.

| Actual field | Meaning; qualification |
| --- | --- |
| 31A/31B, 32A, 33A | VATable sales/output, zero-rated sales and exempt sales. Classify and time each supply first. |
| 34B, 35B, 36B, 37B | Output, qualified uncollected-receivable deduction, recovery add-back and adjusted output. Eligibility is separate from the boxes. |
| 38B–43B | Previous-quarter input, legacy deferred capital input, transitional input, presumptive input, other specified input and subtotal. Reconcile and qualify each component. |
| 44A/B, 45A/B, 46A/B, 47A/B | Domestic purchases, nonresident services, imports and other specified purchases/input. Invoice totals are not automatically allowable input. |
| 48A, 49A, 50A/B, 51B | Domestic purchases with no input, exempt imports, current totals and available-input subtotal. |
| 52B–57B | Capital deferral, exempt attribution, refund/TCC claimed, unpaid-payables adjustment, other adjustments and deductions subtotal. Historical amortisation, allocation and claims require separate proof. |
| 58B, 59B, 60B | Settled-payables adjustment, adjusted deductions and allowable input. **Formula/eligibility hold:** the printed item 59 says sum of 57B and 58B, whilst item 60 subtracts 59B. This was visually confirmed. Complete unpaid/settled-payables authority and reconciliation remain missing; do not silently change the sign or implement this path. |
| 61B → 15 | Net VAT/excess input transferred to Part II. A negative amount is not an automatic cash-refund entitlement. |
| 16–21 | Creditable VAT withheld, advance VAT, prior amended-return payment, other specified credits, total credits and remaining payable/excess. Do not use generic income-tax CWT as a VAT credit. |
| 22–26 | Separate surcharge, interest and compromise, total penalties and total payable/excess. Determine the applicable taxpayer class and actual offence first. |
| Part V Schedules 1–4 | Legacy capital input, exempt attribution, creditable VAT withheld and advance VAT. Match each supporting schedule to its specified field. |

## Penalties and interest

The earlier 4 penalty subjects are retained as qualified review questions. The form instructions and RR 6-2024 distinguish medium/large and micro/small taxpayers, ordinary 25%/10% surcharges, fraud/wilful-neglect rules, interest and conditional compromise concessions. The former PHP 1,000 plus 25%, flat 12% interest, universal 50% invoice surcharge and automatic criminal-liability table are withdrawn as unsupported universal rules. Determine the actual offence, taxpayer class, governing provisions, notices and dates; no penalty amount is computed here.

Source: [April 2024 Form 2550Q penalty instructions](https://bir-cdn.bir.gov.ph/BIR/pdf/2550Q%20guidelines%20April%202024_final.pdf) and [RR 6-2024 all 10 sections](https://naro.law.upd.edu.ph/storage/01JT28JRH6YRBG857QWTQ0JJFH.pdf). The exact offence, classification, commencement, interest and compromise conditions remain Needs Input; no universal penalty or actual amount is established.

## Cross-border points

### Step 3 : Analyse digital services separately

[RA 12023 ss 1–11/14](https://lawphil.net/statutes/repacts/ra2024/pdf/ra_12023_2024.pdf), [full RR 3-2025 ss 1–17](https://bir-cdn.bir.gov.ph/BIR/pdf/RR%20No.%203-2025.pdf), [full RR 14-2025 ss 1–4](https://bir-cdn.bir.gov.ph/BIR/pdf/RR%20NO.%2014-2025.pdf) and [full RMC 47-2025 A1–30](https://bir-cdn.bir.gov.ph/BIR/pdf/RMC%20No.%2047-2025.pdf) must be read together.

- Establish an essentially automated digital supply, actual contracting seller, residence/physical presence, Philippine consumption and buyer's business/government and VAT status. Physical imports follow the import regime. Conflicting location evidence requires the regulation's non-conflicting evidence test. Foreign currency or a supplier name does not establish these facts.
- RR 14 expressly substitutes a 120-day registration transition, states registration by 1 June 2025 and VAT from 2 June 2025, and permits further extensions. Its body/effectivity text is dated 2 April; posting/receipt is 25 April. The specific dates agree with RMC 47; this does not prove the entire publication or later-extension history.
- **Statutory scope hold:** RA 12023's NIRC 108-B/114(D) uses VAT registration in allocating buyer/seller responsibility. RR 3 ss 6(B)(1)/6(C) and RMC 47 A13/A18 describe business/government buyers including non-VAT businesses, with registered and unregistered seller cases. Do not resolve the difference merely by stating that the guide follows the regulation. Refer the affected buyer/seller facts and legal interaction for professional resolution.
- The regulation describes 12% buyer withholding/remittance within 10 days after the withholding month, using Form 1600-VT in RMC 47, whilst the NRDSP's own B2C return/payment uses Form 2550-DS and the quarterly 25-day rule. These are distinct liabilities. A seller's registration or failure to show VAT does not alone decide the buyer's duty. RMC 47 A13's USD 112 contract/100 seller/12 withholding differs from A16's USD 100 annotated invoice; establish who bears VAT and the contractual base before calculating.
- RR 3 s 7 and RMC 47 A28 distinguish a VAT-registered buyer's potential input, supported by filed 1600-VT, from a non-VAT buyer's cost. Do not require the foreign seller's BIR registration as an automatic prerequisite, or infer entitlement from remittance alone. NRDSPs cannot claim creditable input.
- NRDSP invoices have the specific date, reference, buyer identity, description and VAT-inclusive amount particulars, English/translation and mixed-component conditions under RR 3 s 8. They need not carry ordinary Philippine BIR registration/ATP. Do not apply the ordinary invoice rule without this exception.
- For B2C, RR 3 s 6(B)(2) gives a seller a good-faith, reasonable-efforts buyer-status presumption. It is not an unrestricted buyer default. Resident DSPs follow their own ordinary rules and any marketplace withholding duties. Marketplace control, the merchant's residence, ordering/delivery and payment facts matter; separately analyse the platform's own fee. RMC 47 A20's double-payment correction/carryover is not a general refund rule.
- RMC 47 A29's fully prepaid January–December contract without VAT places the stated post-2-June liability on the NRDSP because the buyer no longer controls payment. Do not automatically apply that answer to a different payment schedule. A30 addresses shared costs for digital services actually consumed by a Philippine subsidiary and describes its B2B withholding; the subsidiary's facts and statutory-scope hold still matter.
- Education/online subscriptions and banking/financial services carry institution, accreditation, recipient and activity conditions. RMC 47 A26's incentive/export-enterprise rule includes specified enterprise/activity, direct-attribution and certification conditions. A24's platform/teleconsultation distinction is not a blanket medical exemption. NRDSP PHP FX conventions in RR 3 s 3(D), including election/evidence/consistency conditions, do not automatically establish the Philippine buyer's method.

## Two worked examples that recompute

### Step 4 : Preserve the 6 hypothetical transaction positions

These are synthetic BDO-style lines for a hypothetical Manila IT consultant, not client data or evidence of any named supplier's practice. Dates, amounts and each original subject are retained. Balances are contextual bank data and not a chain of journal entries. Arithmetic is conditional; each unresolved entitlement or recognition issue remains Needs Input.

1. **Domestic B2B revenue:** `04/15/2025 CREDIT ABC TECH SOLUTIONS INC REF INV-2025-041 PHP 1,120,000.00 PHP 5,000,000.00`. If the reviewed contract and invoice establish wholly standard-rated VAT-inclusive consideration for services already rendered in the relevant quarter, net is PHP 1,000,000 and output PHP 120,000, mapped to 31A/31B. Confirm performance, invoice date, base, status and period; payment alone does not establish recognition.
2. **Foreign-client receipt:** `04/22/2025 CREDIT ACME CORPORATION USA USD 10,000 (PHP 560,000.00) PHP 5,560,000.00`. The implied conversion is PHP 56/USD, not a prescribed rate. If the complete export conditions and applicable conversion/period are professionally established, the illustrative zero-rated base is PHP 560,000 and VAT PHP 0 at 32A. On the stated bank evidence alone, zero-rating and the filing amount remain Needs Input. Do not substitute 12% because export evidence is missing.
3. **Utility payment:** `04/10/2025 DEBIT MERALCO April 2025 Electric Bill -PHP 11,200.00 PHP 4,988,800.00`. If an actual invoice separately establishes a wholly standard-rated VAT-inclusive supply, arithmetic net is PHP 10,000 and VAT component PHP 1,200. Brand recognition does not prove the invoice, taxable components, business use, timing or allowable credit. Hold input until those are qualified; then consider 44A/B.
4. **Domestic airline ticket:** `04/08/2025 DEBIT CEBU PACIFIC AIR Manila-Cebu ticket -PHP 4,480.00 PHP 4,984,320.00`. On an established wholly 12% VAT-inclusive fare, net is PHP 4,000 and VAT component PHP 480. Confirm actual route, carrier/supply, taxes and pass-throughs, ticket-as-invoice requirements, business use and credit timing. Do not infer a fully creditable invoice from the carrier or divide a mixed ticket total automatically.
5. **Statutory contribution:** `04/25/2025 DEBIT SOCIAL SECURITY SYSTEM SSS April 2025 -PHP 4,500.00 PHP 4,979,820.00`. If documents establish exactly an employer statutory contribution and no purchased supply/import VAT, classify as a payroll/statutory payment, no input VAT and no sale or purchase VAT box for that payment. The amount alone does not establish contribution rates or other payroll obligations; a payment merely bearing 'SSS' remains unresolved.
6. **Client lunch:** `04/12/2025 DEBIT JOLLIBEE FOODS CORP Client lunch -PHP 1,120.00 PHP 4,978,700.00`. If the invoice establishes a wholly 12% VAT-inclusive purchase, net is PHP 1,000 and VAT component PHP 120. Actual credit remains held pending invoice, business purpose, applicable input restrictions and timing. Neither 'no absolute block' nor the income-tax 0.5%/1% entertainment ceilings establishes VAT entitlement.

### Arithmetic fixtures for the established assumptions

The checks verify arithmetic only, not the missing legal or factual conditions.

```oa-check
name: PH2025 established VAT inclusive domestic revenue arithmetic
inputs:
  gross: 1120000
steps:
  - net: gross / 1.12
  - vat: gross - net
expected:
  net: 1000000
  vat: 120000
```

```oa-check
name: PH2025 conditional export receipt conversion arithmetic
inputs:
  usd: 10000
  assumed_php_per_usd: 56
steps:
  - php_base: usd * assumed_php_per_usd
  - conditional_zero_vat: php_base * 0
expected:
  php_base: 560000
  conditional_zero_vat: 0
```

```oa-check
name: PH2025 established utility VAT component arithmetic
inputs:
  gross: 11200
steps:
  - net: gross / 1.12
  - vat_component: gross - net
expected:
  net: 10000
  vat_component: 1200
```

```oa-check
name: PH2025 established domestic airfare VAT component arithmetic
inputs:
  gross: 4480
steps:
  - net: gross / 1.12
  - vat_component: gross - net
expected:
  net: 4000
  vat_component: 480
```

```oa-check
name: PH2025 confirmed statutory contribution no purchased VAT arithmetic
inputs:
  confirmed_contribution: 4500
steps:
  - input_vat: confirmed_contribution * 0
expected:
  input_vat: 0
```

```oa-check
name: PH2025 established lunch VAT component arithmetic
inputs:
  gross: 1120
steps:
  - net: gross / 1.12
  - vat_component: gross - net
expected:
  net: 1000
  vat_component: 120
```

### Additional decision case: optional monthly or quarterly-only filing

A hypothetical VAT-registered business asks whether choosing optional monthly Form 2550M removes its quarterly Form 2550Q. It does not: full RMC 52-2023 permits the monthly choice but expressly retains the quarterly filing/payment obligation. Either route still requires the quarter return. Assume the reviewer separately establishes quarterly liability of PHP 120,000 for both alternatives. Under the quarterly-only alternative, establish no eligible advance payments: PHP 120,000 less PHP 0 leaves PHP 120,000 payable. Under the optional-monthly alternative, establish PHP 120,000 of eligible monthly VAT payments already credited to the same period: PHP 120,000 less PHP 120,000 leaves PHP 0. Total tax payments are PHP 120,000 in either illustration; a zero remaining balance does not remove the return. These are alternative hypothetical payment facts, not a tax saving or a preferred filing route. Without verified eligible payment amounts, do not subtract a bank payment or infer zero payments or a filing balance. Actual form fields, reconciliation and channel conditions remain held. [RMC 52-2023 both pages](https://bir-cdn.bir.gov.ph/local/pdf/RMC%20No.%2052-2023%20(1).pdf).

```oa-check
name: PH2025 conditional quarterly-only versus monthly payments both retain quarterly filing
inputs:
  quarterly_liability: 120000
  quarterly_only_advance_payments: 0
  eligible_monthly_payments: 120000
steps:
  - quarterly_only_remaining: quarterly_liability - quarterly_only_advance_payments
  - monthly_remaining: quarterly_liability - eligible_monthly_payments
  - quarterly_only_total_payments: quarterly_only_advance_payments + quarterly_only_remaining
  - monthly_total_payments: eligible_monthly_payments + monthly_remaining
expected:
  quarterly_only_remaining: 120000
  monthly_remaining: 0
  quarterly_only_total_payments: 120000
  monthly_total_payments: 120000
```

## Ask the client first

The 6 fact groups that change the answer are: entity/jurisdiction and activity; actual period/accounting year; registration/status/elections; sales and supply/customer characteristics; invoices, imports and input use; and digital/incentive/withholding/payment facts. Obtain these before computing.

### Intake and order of work

1. Read the bases and confirm all applicable companions. Obtain the transaction data before inferring a profile; never infer tax status from a brand or bank alone.
2. Confirm the entity, Philippine connection, period, accounting year, TIN including branch code, RDO, COR/Form 2303, VAT registration/cancellation effective dates, activities, expected and past 12-month sales, taxable/exempt mix and relevant elections. Ask the factual profile questions together.
3. Run refusals, gather supporting invoices and ask the transaction questions before calculations or output construction. An unanswered material question remains **Needs Input**. A bank-only schedule may identify questions; it cannot establish an input claim, exemption, recognition date or filing amount.
4. Reconcile invoice/service/import dates, consideration and payment to the journals and bank. Record source, legal provision, conditions, classification, period and reviewer disposition for every transaction. Do not insert an invented tax rate, country, entitlement or personal-use classification to finish a calculation.

| Input level | Documents and consequence |
| --- | --- |
| Minimum | Period transaction data in CSV, PDF or text, actual taxpayer/profile confirmation, COR and registration dates, sales/purchase evidence sufficient to determine the requested position. Missing bank/ledger data, status, applicable law or a material invoice means stop that position. The former bank-only soft warning does not permit provisional tax credits. |
| Recommended | Complete sales/purchase journals, invoices and corrections, service-performance evidence, contracts/payment terms, import entries and customs VAT proof, previous return and reconciled input carryforward, withholding returns/certificates and filing/payment acknowledgements. |
| Ideal | Complete reconciliations, registration/election history, exemption/export/incentive documents, allocation schedules, credit/refund history, electronic channel/version evidence and a credentialed reviewer's signed brief. |

### Refusals and boundaries

Retain the bases' refusal catalogue. These local codes add questions and holds; they do not replace any base code.

| Code | Trigger and required action |
| --- | --- |
| R-PH-1 | Ordinary non-VAT/percentage-tax position: determine actual liability and registration dates before routing to Form 2551Q. A low turnover or non-VAT COR does not by itself settle all obligations. Non-VAT business purchases from an NRDSP require the separate digital analysis under Cross-border points; this is not a blanket exclusion of that buyer. |
| R-PH-2 | PEZA/BOI/other incentive claim: obtain the applicable law, enterprise/activity status, certification and direct attribution. A certificate or ecozone address alone is insufficient. Hold zero-rating until the complete period-specific conditions are verified by the reviewer. |
| R-PH-3 | Mixed taxable/exempt activity: obtain direct attribution and the legally applicable allocation period/ratio. The old unexplained annual-ratio requirement is withdrawn. Form Schedule 2 is evidence of a calculation layout, not the complete allocation law. |
| R-PH-4 | Government or nonresident withholding: separate creditable government withholding, nonresident withholding and digital reverse charge. Do not describe all as final withholding or subtract income-tax withholding from VAT. Obtain the actual source, return, certificate and remittance evidence. |
| R-PH-5 | NRDSP's own registration, marketplace liability or Form 2550-DS: specialist workflow required. A Philippine buyer's analysis may be considered here, subject to its own buyer-status, statutory-scope, invoice and payment holds. |
| R-PH-6 | Unresolved source conflict, compulsory companion/slot, material taxpayer fact, invoice or return-version condition: stop the affected position and operational output. Disclose the particular missing evidence; a general disclaimer cannot clear it. |

### Transaction questions and defaults

Ask material questions before calculating or constructing output. Retain all 5 earlier question topics:

| Ambiguity | Ask and explain what the answer changes | Pending result |
| --- | --- | --- |
| Entertainment | What was purchased, for whose business purpose, under which invoice, and what VAT restriction/allocation and timing applies? Income-tax deduction limits answer a separate question. | Needs Input for actual VAT recovery; no invented personal-use finding. |
| Foreign service revenue | Who is the recipient, where is the activity/use, what is the complete applicable zero-rating rule and documentary/FX trail, and when was the service rendered? | Needs Input for rate/base/period; no automatic 12% default. |
| Incentive buyer | What enterprise/activity status, operative incentive law, certificate and direct attribution apply to this supply and period? | Hold zero-rating; do not replace it with an invented rate. |
| Foreign digital purchase | Who is the seller and buyer, their residence/business/VAT status, actual consumption, contractual VAT allocation, service/payment dates and filed 1600-VT evidence? Does a stated statutory/regulatory conflict affect them? | Needs Input; seller registration/invoice VAT alone does not decide withholding or credit. |
| Vehicle | What is the asset/supply, ownership, business/private use, invoice, applicable restriction/allocation and timing? | Hold the credit; do not invent exclusive use or label mixed use automatically blocked. |

The 7 former defaults are replaced by explicit holds: unknown sale rate, country, export qualification, business-use percentage, invoice compliance, digital buyer status and PEZA status all remain unresolved for the affected position. Do not treat 0% credit as a substantive exemption, or an unresolved output rate as an assessed 12% liability. A separately labelled arithmetic scenario may show established assumptions whilst the actual position remains held.

### Onboarding fallback and delivery controls

If context is sparse, request the entity/activity, period and accounting year, jurisdiction, TIN/RDO/COR and registration history, transaction data, invoice/journal evidence, export/incentive/mixed-supply facts and digital purchase details together. Explain which positions remain unresolved and the source required to clear each. Do not create a workbook first and seek answers afterwards.

Prohibitions retained and clarified: no invented rate or liability; no unqualified input without applicable evidence and entitlement; no automatic foreign/export or PEZA treatment; no conflation of resident and nonresident digital suppliers; no calculation or operational deliverable before material intake/refusal questions are cleared; and no filing/payment or tax position without qualified professional approval. The original six filing-check subjects remain in Reconciliation step, with corrected legal limits.

### Completion checks

- [ ] The exact taxpayer, historical period, accounting year and registration dates are established; no unknown country/status/rate was replaced by a default.
- [ ] Actual primary law, amendments, commencement and transaction conditions support each applied rule. Every unresolved source condition has a specific Needs Input disposition.
- [ ] Invoices, contracts, journals, customs documents, withholding proof and bank reconcile without duplicate sales, collection invoices or credit claims.
- [ ] Actual return version/boxes, channels, cut-offs, attachments and any relief are verified. No unsupported Form 2550M mapping or printed-form sign correction is implemented.
- [ ] All 6 illustrations retain their stated assumptions and holds; arithmetic does not claim entitlement. Every original supplier row is a discovery cue rather than a tax decision.
- [ ] All 5 question topics, 7 former defaults, 5 attention signals, 3 filing-event rows, 4 former penalty subjects and 8 bank terms are preserved or expressly corrected above.
- [ ] The universal and VAT contracts, applicable regional layer, required positions/outputs and all 18/14 checks are met before operational delivery. Otherwise retain the operational hold and state the missing slot.
- [ ] A credentialed Philippine reviewer has reviewed and signed the actual position before anyone files, pays, amends or acts. This draft has no such approval.

## Sources

### Actual read limits

The read date below is 5 November 2026 in Australia/Sydney. Download/extraction does not establish full law, commencement, later continuity or taxpayer entitlement. Displayed amending units containing `x x x` are not complete consolidated NIRC provisions. Signed sources take precedence over malformed HTML transcription; unresolved legal interactions remain held.

| Source | URL | Read on |
| --- | --- | --- |
| TRAIN RA 10963 | <https://lawphil.net/statutes/repacts/ra2017/ra_10963_2017.html> | 2026-11-05; complete displayed Act ss 31–38, 40 and 72 selected for VAT/registration. Substantial quoted NIRC text omitted; selected signed pages do not authenticate every VAT unit. |
| EOPT RA 11976 | <https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/2/96948><br><https://lawphil.net/statutes/repacts/ra2024/pdf/ra_11976_2024.pdf> | 2026-11-05; complete displayed Act ss 16–24, 29 and 34. Selected signed pages corroborate 114/116, not every VAT/input/registration unit. HTML has known section-label/transcription defects. |
| RR 3-2024, official filed copy | <https://naro.law.upd.edu.ph/issuances/3811><br><https://naro.law.upd.edu.ph/storage/01JT27FB5GV836PNJHD2B7EMAT.pdf> | 2026-11-05; ss 1–11, all 7 pages in OCR, including complete uncollected-receivable conditions. Publication/commencement not independently established. |
| RR 7-2024, official filed copy | <https://naro.law.upd.edu.ph/issuances/3822><br><https://naro.law.upd.edu.ph/storage/01JT28MCBF1J9NSBJX7WGXCMT6.pdf> | 2026-11-05; ss 1–11, all 17 pages in OCR. Read with amendments, not as unchanged transition law. |
| RR 11-2024 | <https://bir-cdn.bir.gov.ph/BIR/pdf/RR%20No.%2011-2024.pdf> | 2026-11-05; ss 1–6, all 5 pages. Full signed-source capture distinct from digest. Later extensions not exhaustively reviewed. |
| RMC 77-2024, official filed copy | <https://naro.law.upd.edu.ph/issuances/5226><br><https://naro.law.upd.edu.ph/storage/01JW7NJJTNTTCY1EK1P4SH8PZ7.pdf> | 2026-11-05; Read for Q/A 1–33 and all annexes in 23-page OCR. Printed discrepancies on pages 2, 9 and 22 visually confirmed; remaining diagrams/table layouts not fully qualified. |
| RR 1-2024 | <https://bir-cdn.bir.gov.ph/BIR/pdf/RR%20No.%201-2024.pdf> | 2026-11-05; ss 1–6, both pages, specific housing adjustment. Not the entire property/exemption chain. |
| RMC 5-2023 and 52-2023 full copies | <https://bir-cdn.bir.gov.ph/local/pdf/RMC%20No.%205-2023%20(1).pdf><br><https://bir-cdn.bir.gov.ph/local/pdf/RMC%20No.%2052-2023%20(1).pdf> | 2026-11-05; Read for the complete 1/2-page general/optional filing text; RMC 5's transitory table has not been visually mapped or adopted as a later-period calendar. Incorporated procedures remain limited. |
| Actual 2550Q and instructions, April 2024 | <https://bir-cdn.bir.gov.ph/BIR/pdf/RMC%20No.%2068-2024%20Annex%20A.pdf><br><https://bir-cdn.bir.gov.ph/BIR/pdf/2550Q%20guidelines%20April%202024_final.pdf> | 2026-11-05; Part I–V, both form pages and full instruction page. Form page 2 visually checked; printed item 59 discrepancy held. |
| RMC 68-2024 | <https://bir-cdn.bir.gov.ph/BIR/pdf/RMC%20No.%2068-2024.pdf> | 2026-11-05; Read in full: all 3 pages, dated form rollout only. |
| RA 12023 | <https://lawphil.net/statutes/repacts/ra2024/ra_12023_2024.html><br><https://lawphil.net/statutes/repacts/ra2024/pdf/ra_12023_2024.pdf> | 2026-11-05; ss 1–18, complete HTML body and signed text, exact units qualified in the evidence read log. Service-input and buyer-status interactions remain unresolved; malformed HTML is not silently substituted for signed text. |
| RR 3-2025 | <https://bir-cdn.bir.gov.ph/BIR/pdf/RR%20No.%203-2025.pdf> | 2026-11-05; ss 1–17, all 10 pages in OCR; missing B2C line and invoice particulars visually recovered on pages 1/8. |
| RR 14-2025 full copy | <https://bir-cdn.bir.gov.ph/BIR/pdf/RR%20NO.%2014-2025.pdf> | 2026-11-05; ss 1–4, both pages. Actual full copy now read, superseding the earlier access gap; posting and body dates distinguished. |
| RMC 47-2025 | <https://bir-cdn.bir.gov.ph/BIR/pdf/RMC%20No.%2047-2025.pdf> | 2026-11-05; Read for Q/A 1–30 in all 11 OCR pages; A30 page 11 visually confirmed. Diagrams not fully spatially qualified. |
| RR 6-2024, inherited qualified penalty source | <https://naro.law.upd.edu.ph/storage/01JT28JRH6YRBG857QWTQ0JJFH.pdf> | 2026-11-05; prior scoped work read ss 1–10. Exact taxpayer classification, application and later interest law remain required; no penalty calculation adopted here. |


Not yet confirmed: full operative 2025 amendment and commencement chains; actual threshold/indexation and registration/election facts; service-input accrual/payment interaction; non-VAT digital buyer statutory/regulatory allocation; unpaid/settled-payable authority and printed item 59 formula; all export/incentive, housing/rent, agriculture, education/medical/medicine, literary/musical, insurance, carrier and financial-service conditions; vehicle/private-use/entertainment input restrictions; NIRC 111 inventory/presumptive input, historical capital amortisation, allocation, withholding, carryforward and refund qualification; invoice-transition printed discrepancies and later electronic-invoicing rules; exact penalties/interest; Form 2550M fields and incorporated procedures; current period-specific channels/attachments/relief; supplier/library category coverage and actual bank-format specifications; every universal/VAT/regional companion slot, universal 5-position and VAT 6-classification qualification and 18/14 check; professional review, taxpayer entitlement and operational filing/payment approval. Each affected position remains Needs Input.

### Version history

Version 1.0 was the 2024 initial reference. The earlier history records a 2.0 rewrite in April 2026 and digital-source correction on 31 October 2026. Version 2.1, 1 November 2026, corrected optional monthly filing, invoices and the housing threshold. Version 2.2 preserves the legacy subjects and 6 positions in the canonical template, replaces unsafe brand/default/form shortcuts, reads actual full source copies and discloses remaining source and operational holds. Earlier review attribution does not approve this repair.

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.
