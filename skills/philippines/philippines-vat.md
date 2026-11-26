---
name: philippines-vat
description: Prepare or review Philippine VAT for 2025, classify supplies and input tax, and apply the registration, quarterly filing and foreign digital services rules.
version: 2.1
jurisdiction: PH
tax_year: 2025
tax_year_notes: "2025 transactions in calendar-year and fiscal 2025-26 VAT reporting periods. The examples use April 2025; check the law on the transaction date for subsequent changes."
last_updated: 2026-11-26
depends_on:
  - vat-workflow-base
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: vat-gst
type: computation
---

# Philippines VAT

## Scope

Use this guide to classify 2025 Philippine VAT transactions and prepare the corresponding quarterly workpaper in PHP. Confirm the taxpayer's actual fiscal or calendar quarter before filing.

## Rates, bands and thresholds

**Quick reference table**  _(RA 10963 s.37; RMC 52-2023; RR 1-2024. Corrected by Jonathan I. Ruiz (CPA, Philippines))_

| Rule | Treatment | Authority |
| --- | --- | --- |
| VAT periods | The taxpayer's calendar or fiscal quarters | [Form 2550Q instructions](https://bir-cdn.bir.gov.ph/BIR/pdf/RMC%20No.%2068-2024%20Attachment.pdf) |
| Standard rate | 12% | [NIRC sections 106 and 108](https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/2/96948) |
| Zero rate | 0% for qualifying exports, eligible supplies to exporters and registered enterprises, and specified international operations | [RR 10-2025](https://bir-cdn.bir.gov.ph/BIR/pdf/RR%20No.%2010-2025%20%281%29.pdf) |
| Exempt | Specified agricultural products, qualified educational and medical services, certain financial transactions and eligible residential dwellings sold for up to PHP 3,600,000 | [NIRC section 109](https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/2/3896), [RR 1-2024](https://bir-cdn.bir.gov.ph/BIR/pdf/RR%20No.%201-2024.pdf) |
| Registration threshold | PHP 3,000,000 of relevant gross sales in the past 12 months or reasonably expected in the next 12 months. Mandatory registration applies above the threshold. | [NIRC section 236(F)](https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/2/96948), [RR 3-2024](https://bir-cdn.bir.gov.ph/BIR/pdf/RR%20No.3-%202024.pdf) |
| Non-VAT percentage tax | Generally 3% of quarterly gross sales for non-VAT taxpayers exempt under section 109(CC), with Form 2551Q. Check statutory exemptions and the qualifying 8% income-tax election. | [NIRC sections 24 and 116](https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/2/80559), [RR 3-2024](https://bir-cdn.bir.gov.ph/BIR/pdf/RR%20No.3-%202024.pdf) |
| Monthly return | Optional Form 2550M from 1 January 2023. No prescribed monthly deadline. | [RMC 52-2023](https://bir-cdn.bir.gov.ph/local/pdf/RMC%20No.%2052-2023%20(1).pdf) |
| Quarterly return | Required Form 2550Q within 25 days after each taxable quarter | [RMC 52-2023](https://bir-cdn.bir.gov.ph/local/pdf/RMC%20No.%2052-2023%20(1).pdf) |
| Tax invoice | A valid VAT invoice, including a properly converted legacy document where permitted | [RR 7-2024](https://bir-cdn.bir.gov.ph/BIR/pdf/RR%20No.%207-%202024.pdf), [RR 11-2024](https://bir-cdn.bir.gov.ph/BIR/pdf/RR%2011-2024.pdf) |
| TIN | Nine-digit tax identification number. Use the applicable branch-code format requested by the form or system. | [RR 7-2024](https://bir-cdn.bir.gov.ph/BIR/pdf/RR%20No.%207-%202024.pdf) |

Use [eFPS](https://efps.bir.gov.ph) or eBIRForms as applicable. Confirm the relevant BIR registration and payment instructions. The Revenue District Office (RDO) is the taxpayer's registered district.

## Form 2550Q and review flags

### Form 2550Q mapping

Use the applicable form revision. In the [April 2024 ENCS return](https://bir-cdn.bir.gov.ph/BIR/pdf/2550Q%20%20April%202024%20ENCS_Final.pdf), tax calculation is in Part IV and schedules are in Part V. Part II shows net VAT, credits, payments and penalties.

| Item | Meaning |
| --- | --- |
| 31–34 | Taxable, zero-rated and exempt sales and output VAT |
| 35–37 | Output VAT adjustments and total adjusted output tax |
| 38–60 | Available input tax, purchases by type, adjustments and allowable input tax |
| 61 | Net VAT payable or excess input tax |
| 15–21 | Net VAT, creditable VAT withheld, advance VAT, other payments and balance |
| 22–26 | Applicable penalties and total payable or excess credits |

### Conservative defaults

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown rate on a sale | Flag for classification. Use 12% only as a provisional estimate for a potentially standard-rated sale. |
| Unknown counterparty country | Obtain country, consumption and business evidence before assigning final VAT treatment. |
| Unknown export/zero-rate qualification | 12% until evidence confirmed |
| Unknown business-use % (vehicle, phone) | 0% input VAT |
| Missing valid VAT invoice | Hold the input credit until qualifying evidence is obtained. |
| Unknown B2B vs B2C for digital services | Identify buyer status before deciding who remits the VAT. |
| Unknown registered-enterprise eligibility | Hold zero-rating pending certification and evidence of qualifying use. |

### Red flag thresholds

These cut-offs prioritise review in the workpaper. Apply the statutory tests independently.

**Red flag thresholds**

| Threshold | Value |
| --- | --- |
| HIGH single transaction | PHP 500,000 |
| HIGH tax delta on single default | PHP 60,000 |
| MEDIUM counterparty concentration | >40% of output or input |
| MEDIUM conservative default count | >4 per period |
| LOW absolute net VAT position | PHP 200,000 |

## Ask the client first

### Required inputs

**Minimum viable** – sales and purchases records or the VAT invoices needed to establish the transactions, taxpayer identification number and VAT registration details from BIR Form 2303. Use bank statements to reconcile payment and identify transactions for follow-up.

**Recommended** – VAT invoices for sales and purchases, evidence of withheld VAT and the prior-period excess credit.

**Ideal** – complete sales/purchase journal, import entries, prior quarterly return, EFPS filing confirmation.

**Refusal if minimum missing.** Hold the filing computation until the source records establish the period, amounts and tax treatment. A bank statement is a reconciliation aid. Use invoices and the sales/purchases journals to determine taxable sales, and use the appropriate supporting documentation for input VAT.

### Refusal catalogue

- **R-PH-1 Non-VAT taxpayers.** A non-VAT taxpayer exempt under section 109(CC) generally uses Form 2551Q and pays 3% of quarterly gross sales. Check the 8% election and other exceptions. A qualifying taxpayer may elect VAT registration, generally for at least three years.
- **R-PH-2 Registered-enterprise purchases.** Verify the buyer's applicable eligibility, certification, project or export activity, and whether the purchase is directly attributable to that activity.
- **R-PH-3 Mixed supplies.** Directly attribute input VAT where possible. Allocate residual common input tax using the applicable taxable, zero-rated and exempt sales proportions. Obtain the period records before filing.
- **R-PH-4 Withholding VAT.** The ordinary 5% government VAT withholding is creditable from 1 January 2021. Check exceptions and separate nonresident rules. Qualifying foreign digital services have their own reverse-charge rules.
- **R-PH-5 Foreign digital services.** Check Philippine consumption, supplier registration, applicable exemptions and whether the Philippine customer acts in business. The domestic buyer may have a withholding obligation even if it is not VAT-registered.

## The method, step by step

Use the supplier patterns to suggest follow-up. Confirm the actual supply and invoice. Match by case-insensitive substring on counterparty name or reference, using the most specific match. If no pattern applies, classify the transaction using the statutory rules below.

### 3.1 Philippine banks – fees and charges (exempt / exclude)

**Philippine banks – fees and charges**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| BDO UNIBANK, BANCO DE ORO | EXCLUDE (fee lines) | Financial service – VAT exempt |
| BANK OF THE PHILIPPINE ISLANDS, BPI | EXCLUDE (fee lines) | Same |
| METROBANK, METROPOLITAN BANK | EXCLUDE (fee lines) | Same |
| UNIONBANK OF THE PHILIPPINES | EXCLUDE (fee lines) | Same |
| SECURITY BANK | EXCLUDE (fee lines) | Same |
| LANDBANK OF THE PHILIPPINES, LBP | EXCLUDE (fee lines) | Same |
| PHILIPPINE NATIONAL BANK, PNB | EXCLUDE (fee lines) | Same |
| CHINA BANKING, CHINABANK | EXCLUDE (fee lines) | Same |
| RCBC, RIZAL COMMERCIAL BANKING | EXCLUDE (fee lines) | Same |
| GCASH, G-XCHANGE (GXI) | Check invoice and fee type | Separate money movements and any regulated financial or taxable processing fee. |
| MAYA, PAYMAYA | Check invoice and fee type | Separate money movements and any regulated financial or taxable processing fee. |
| SEABANK | EXCLUDE (fee lines) | Digital bank – financial service |
| SERVICE CHARGE, BANK FEE, INTEREST | EXCLUDE | Bank charges/interest – exempt |

### 3.2 Philippine government and statutory (exclude)

**Philippine government and statutory**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| BUREAU OF INTERNAL REVENUE, BIR | EXCLUDE | Tax payment |
| BUREAU OF CUSTOMS, BOC | EXCLUDE | Customs duty |
| SOCIAL SECURITY SYSTEM, SSS | EXCLUDE | Social insurance |
| PHILHEALTH | EXCLUDE | Health insurance |
| PAG-IBIG, HDMF | EXCLUDE | Housing fund |
| SEC PHILIPPINES | EXCLUDE | Regulatory fee |
| LGU, BARANGAY, CITY HALL | EXCLUDE | Local government fee |

### 3.3 Philippine utilities (taxable at 12%)

**Philippine utilities**

| Pattern | Treatment | Rate | Notes |
| --- | --- | --- | --- |
| MERALCO, MANILA ELECTRIC | Check invoice | 12% on taxable components | Use the VAT shown on the invoice and identify exempt or pass-through charges. |
| CEPALCO (Cagayan de Oro electric) | Check invoice | 12% on taxable components | Use the VAT shown on the invoice and identify exempt or pass-through charges. |
| VECO (Visayas Electric) | Check invoice | 12% on taxable components | Use the VAT shown on the invoice and identify exempt or pass-through charges. |
| MANILA WATER | Check invoice | 12% on taxable components | Use the VAT shown on the invoice and identify exempt or pass-through charges. |
| MAYNILAD WATER SERVICES | Check invoice | 12% on taxable components | Use the VAT shown on the invoice and identify exempt or pass-through charges. |
| PLDT, PHILIPPINE LONG DISTANCE | Input 12% | 12% | Telecom/internet – taxable |
| GLOBE TELECOM | Input 12% | 12% | Mobile/internet – taxable |
| SMART COMMUNICATIONS, SMART | Input 12% | 12% | Mobile – taxable |
| DITO TELECOMMUNITY | Input 12% | 12% | Mobile – taxable |
| CONVERGE ICT | Input 12% | 12% | Internet – taxable |

### 3.4 Transport and logistics

**Transport and logistics**

| Pattern | Treatment | Rate | Notes |
| --- | --- | --- | --- |
| PHILIPPINE AIRLINES, PAL | Check route and carrier | 0%/12%/exempt | Domestic legs generally 12%. Check qualifying outbound domestic-carrier service and the distinct international-carrier exemption. |
| CEBU PACIFIC | Check route and carrier | 0%/12%/exempt | Domestic legs generally 12%. Check qualifying outbound domestic-carrier service and the distinct international-carrier exemption. |
| AIRASIA PHILIPPINES | Check route and carrier | 0%/12%/exempt | Domestic legs generally 12%. Check qualifying outbound domestic-carrier service and the distinct international-carrier exemption. |
| PHILIPPINE NATIONAL RAILWAYS, PNR | Check the transaction | Depends on operator and service | Identify the actual rail operator, service and invoice. |
| LRT, MRT (Metro Rail Transit) | Check the transaction | Depends on operator and service | Identify the actual rail operator, route and invoice. |
| GRAB PHILIPPINES | Check the transaction | Depends on operator and service | Distinguish the platform charge and underlying passenger fare. Check the operator's franchise and invoice. |
| ANGKAS | Check the transaction | Depends on operator and service | Check the operator's passenger-transport classification and invoice. |
| LBC EXPRESS | Input 12% | 12% | Courier – taxable |
| JRS EXPRESS | Input 12% | 12% | Courier – taxable |
| DHL PHILIPPINES | Input 12% | 12% | Courier – taxable |
| FEDEX PHILIPPINES | Input 12% | 12% | Courier – taxable |
| 2GO EXPRESS | Input 12% | 12% | Courier – taxable |
| NINJA VAN PHILIPPINES | Input 12% | 12% | Courier – taxable |
| J&T EXPRESS PHILIPPINES | Input 12% | 12% | Courier – taxable |

### 3.5 Food and retail

**Food and retail**

| Pattern | Treatment | Rate | Notes |
| --- | --- | --- | --- |
| SM SUPERMARKET, SM MARKETS | Input 12% | 12% | Supermarket – 12% on non-exempt items |
| ROBINSONS SUPERMARKET | Check each product | 12% on taxable items | Verify taxable and exempt lines on the invoice. |
| PUREGOLD | Check each product | 12% on taxable items | Verify taxable and exempt lines on the invoice. |
| S&R MEMBERSHIP SHOPPING | Check each product | 12% on taxable items | Verify taxable and exempt lines on the invoice. |
| MERCURY DRUG | Check each product | Mixed | Only products qualifying under the specific FDA/BIR exemption are VAT-exempt. |
| WATSONS PHILIPPINES | Check each product | Mixed | Verify the invoice and any exempt medicine line. |
| 7-ELEVEN PHILIPPINES | Check each product | 12% on taxable items | Verify taxable and exempt lines on the invoice. |
| JOLLIBEE (eat-in) | Check invoice | 12% on ordinary taxable restaurant sales | Check purchaser eligibility and any specific exemption. |
| MCDONALD'S PHILIPPINES | Check invoice | 12% on ordinary taxable restaurant sales | Check purchaser eligibility and any specific exemption. |

### 3.6 Foreign digital services

Republic Act 12023 applies 12% VAT to covered digital services consumed in the Philippines. The nonresident regime started on 2 June 2025. Check whether the taxable supplier exceeds the statutory registration threshold and whether an exemption applies. For a covered B2B purchase, the Philippine business buyer withholds and remits the 12% on Form 1600-VT by the 10th day after the end of the month of withholding. A VAT-registered buyer supports an eligible input credit with the filed 1600-VT. An eligible non-VAT buyer treats the withheld VAT as cost or expense. For B2C, the covered nonresident provider files and remits via the BIR's digital services portal. [RA 12023](https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/2/97876), [RR 3-2025](https://bir-cdn.bir.gov.ph/BIR/pdf/RR%20No.%203-2025.pdf), [RMC 47-2025](https://bir-cdn.bir.gov.ph/BIR/pdf/RMC%20No.%2047-2025.pdf).

### 3.7 Payment processors

Reconcile settlement amounts and separately invoiced fees. Payment processing is a digital-service category under [RR 3-2025](https://bir-cdn.bir.gov.ph/BIR/pdf/RR%20No.%203-2025.pdf). A specific banking or non-bank financial-intermediary exemption depends on the provider's status and the activity. Confirm the fee's legal treatment and evidence for the actual supply.

### 3.8 Professional services (VAT-registered)

**Professional services**

| Pattern | Treatment | Rate | Notes |
| --- | --- | --- | --- |
| CPA FIRM, ACCOUNTING FIRM | Input 12% | 12% | Professional services – taxable |
| LAW FIRM, ATTY, ATTORNEY | Input 12% | 12% | Legal services – taxable |
| NOTARY PUBLIC | Input 12% | 12% | Notarial services – taxable |
| ADVERTISING AGENCY | Input 12% | 12% | Marketing – taxable |

### 3.9 Internal transfers and exclusions

**Internal transfers and exclusions**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| INTER-ACCOUNT TRANSFER, OWN ACCOUNT | EXCLUDE | Internal movement |
| LOAN PROCEEDS, LOAN REPAYMENT | EXCLUDE | Loan principal – out of scope |
| SALARY, PAYROLL | EXCLUDE | Wages – outside VAT scope |
| DIVIDEND | EXCLUDE | Out of scope |
| SECURITY DEPOSIT, ADVANCE DEPOSIT | Tier 2 – check | May trigger VAT if applied to taxable supply |
| ATM WITHDRAWAL, CASH WITHDRAWAL | Tier 2 – ask | Default exclude |

## Worked cases

Six classifications from a hypothetical VAT-registered Manila IT consultant. The taxable April transactions are assumed to be invoiced during that quarter. The sample bank movements reconcile payment and do not establish the tax point.

### Example 1 – Domestic B2B revenue (12%)

**Input line:**
`04/15/2025  CREDIT  ABC TECH SOLUTIONS INC  REF INV-2025-041  PHP 1,120,000.00  PHP 5,000,000.00`

**Reasoning:**
PHP 1,120,000 is the VAT-inclusive amount of an April 2025 consulting invoice to a Philippine company. PHP 1,120,000 ÷ 1.12 gives PHP 1,000,000 gross sales excluding VAT and PHP 120,000 output VAT. Report it under taxable sales in Part IV of quarterly Form 2550Q. Issue a registered VAT invoice.

**Classification:** Output VAT 12% – PHP 120,000. Net sales: PHP 1,000,000.

```oa-check
name: VAT-inclusive domestic consulting sale
inputs:
  gross: 1120000
steps:
  base: gross / 1.12
  output_vat: gross - base
expected:
  base: 1000000
  output_vat: 120000
```

### Example 2 – Zero-rated export service

**Input line:**
`04/22/2025  CREDIT  ACME CORPORATION USA  USD 10,000 (PHP 560,000.00)  PHP 5,560,000.00`

**Reasoning:**
Assume the client conducts business outside the Philippines, the consultant rendered the services in the Philippines and the consideration was paid in acceptable foreign currency and accounted for under BSP rules. The illustrative USD 10,000 is recorded at PHP 560,000 for this case. Report PHP 560,000 as zero-rated sales in Part IV of quarterly Form 2550Q. Output VAT is PHP 0. Obtain evidence of the client's foreign operations and the payment.

**Classification:** Zero-rated – PHP 560,000. Output VAT: PHP 0.

```oa-check
name: Qualifying zero-rated export service
inputs:
  base: 560000
steps:
  output_vat: base * 0
expected:
  output_vat: 0
```

### Example 3 – Utility expense (12%, input credit)

**Input line:**
`04/10/2025  DEBIT  MERALCO  April 2025 Electric Bill  -PHP 11,200.00  PHP 4,988,800.00`

**Reasoning:**
Assume the entire PHP 11,200 invoice is for taxable electricity and all the VAT is attributable to the consultant's taxable business. PHP 11,200 ÷ 1.12 gives PHP 10,000 before VAT and PHP 1,200 creditable input VAT. Use the supplier's VAT invoice and report the input VAT in Part IV of Form 2550Q.

**Classification:** Input VAT 12% – PHP 1,200. Net expense: PHP 10,000.

```oa-check
name: Wholly taxable electricity bill
inputs:
  gross: 11200
steps:
  base: gross / 1.12
  input_vat: gross - base
expected:
  base: 10000
  input_vat: 1200
```

### Example 4 – Domestic flight (12%)

**Input line:**
`04/08/2025  DEBIT  CEBU PACIFIC AIR  Manila-Cebu ticket  -PHP 4,480.00  PHP 4,984,320.00`

**Reasoning:**
The domestic flight is taxable at 12%. Assume the fare is wholly taxable and the consultant has a valid VAT invoice for a business trip. PHP 4,480 ÷ 1.12 gives PHP 4,000 before VAT and PHP 480 creditable input VAT.

**Classification:** Input VAT 12% – PHP 480. Net expense: PHP 4,000.

```oa-check
name: Wholly taxable domestic air fare
inputs:
  gross: 4480
steps:
  base: gross / 1.12
  input_vat: gross - base
expected:
  base: 4000
  input_vat: 480
```

### Example 5 – Statutory SSS contribution

**Input line:**
`04/25/2025  DEBIT  SOCIAL SECURITY SYSTEM  SSS April 2025  -PHP 4,500.00  PHP 4,979,820.00`

**Reasoning:**
SSS employer contribution. Government social insurance – EXCLUDE from VAT return entirely. Not a supply of goods or services. No input VAT. This is a payroll-related obligation, not a business expense generating input credit.

**Classification:** EXCLUDE – outside VAT scope. Statutory employer obligation.

```oa-check
name: SSS contribution carries no VAT
inputs:
  contribution: 4500
steps:
  input_vat: contribution * 0
expected:
  input_vat: 0
```

### Example 6 – Client lunch

**Input line:**
`04/12/2025  DEBIT  JOLLIBEE FOODS CORP  Client lunch  -PHP 1,120.00  PHP 4,978,700.00`

**Reasoning:**
Assume the restaurant supply is wholly taxable, the purchase is in the consultant's taxable business and there is a valid VAT invoice. PHP 1,120 ÷ 1.12 gives PHP 1,000 before VAT and PHP 120 possible input VAT. Document the business purpose and exclude any personal or otherwise noncreditable amount. The separate income-tax deduction cap does not calculate input VAT.

**Classification:** PHP 120 input VAT on the stated assumptions. Hold the credit if the evidence or business attribution is missing.

```oa-check
name: Wholly taxable client meal with qualifying evidence
inputs:
  gross: 1120
steps:
  base: gross / 1.12
  input_vat: gross - base
expected:
  base: 1000
  input_vat: 120
```

## Section 5 – VAT rules

### 5.1 Standard rate 12%

- **Standard rate** – 12%

### 5.2 Zero rate – exports and qualifying supplies

- **Zero-rated supplies.** Verify actual export and payment evidence where required. Services supplied in the Philippines to a business conducted outside the Philippines, or a non-business nonresident outside the Philippines when performed, qualify under section 108(B)(2) only with acceptable foreign-currency consideration accounted for under BSP rules. PEZA/BOI registration alone does not establish zero-rating. Check the applicable export or registered project, direct attribution and the prescribed certificate. A domestic air or sea carrier's qualifying outbound transport is zero-rated. An international carrier's qualifying outbound transport is VAT-exempt. [RR 10-2025](https://bir-cdn.bir.gov.ph/BIR/pdf/RR%20No.%2010-2025%20%281%29.pdf), [RMC 66-2025](https://bir-cdn.bir.gov.ph/BIR/pdf/RMC%20No.%2066-2025.pdf).

### 5.3 Exempt supplies

- **Exempt supplies.** Section 109 covers specified original-state agricultural and marine food products, qualifying education and medical services, qualifying books and periodicals, and other listed supplies. Professional medical services are excluded from the general medical-services exemption. A residential dwelling sale covered by RR 1-2024 is exempt at or below PHP 3,600,000 from 1 January 2024, with the next triennial adjustment scheduled for 2027. The residential lease exemption covers rent at or below PHP 15,000 monthly per unit. Check listed medicine products, the specific import exemption and the activity's percentage-tax treatment instead of assuming a class exemption.

<!-- Superseded source line retained for its original attribution.
- **Exempt supplies** — Agricultural products in original state; educational services; medical/hospital services; literary/musical compositions; housing below PHP 3,600,000 (RR 1-2024 — re-indexed from PHP 3,199,200; next CPI re-index due 2027 per NIRC s.109(P)); lease of residential unit below PHP 15,000/month; life insurance premiums; common carriers below threshold; importation of basic necessities.  _(NIRC Section 109; RR No. 1-2024. Corrected by Jonathan I. Ruiz (CPA, Philippines))_
-->

### 5.4 VAT invoice evidence

- **Invoice requirements.** Issue a registered VAT invoice for each covered sale, whether cash or on account. Show the issuer, TIN and branch code, transaction details, consideration, VAT and transaction classification. A VAT-registered purchaser's name, address and TIN are required when the sale is at least PHP 1,000. A standalone official receipt is supplementary. A properly converted unused receipt with the applicable Invoice stamp and required details can still support input VAT. Section 113(D) governs the narrow erroneous or incomplete invoice rules. [RR 7-2024](https://bir-cdn.bir.gov.ph/BIR/pdf/RR%20No.%207-%202024.pdf), [RR 11-2024](https://bir-cdn.bir.gov.ph/BIR/pdf/RR%2011-2024.pdf).

### 5.5 Input VAT limitations

- **Input tax.** Credit qualifying VAT in the course of taxable business with appropriate evidence. Attribute exempt and personal-use amounts separately. For passenger vehicles, check the business substantiation requirement, the restrictions in RR 12-2012 and the specialised transport-business exception. A defective invoice can require correction or the narrow statutory section 113(D) analysis. [RA 11976](https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/2/96948), [RR 12-2012](https://bir-cdn.bir.gov.ph/BIR/pdf/65716RR%20No%2012-2012.pdf).

### 5.6 Transitional input VAT

- **Transitional input VAT.** A qualifying new or voluntarily registered VAT taxpayer submits its inventory as prescribed and may claim 2% of the value of eligible beginning inventory or the actual VAT paid on the inventory, whichever is higher.

### 5.7 Filing deadlines

**Filing deadlines**  _(RA 10963 (TRAIN Law) s.37; RR 13-2018; RMC 52-2023. Corrected by Jonathan I. Ruiz (CPA, Philippines))_

| Return | Period | Due date |
| --- | --- | --- |
| Form 2550Q (quarterly) – the ONLY mandatory VAT return | Quarterly | 25 days after quarter-end |
| Form 2550M (monthly) – optional since 1 January 2023 | Monthly, at the taxpayer's choice | No prescribed deadline. File the quarterly 2550Q even if 2550M was filed. [RMC 52-2023](https://bir-cdn.bir.gov.ph/local/pdf/RMC%20No.%2052-2023%20%281%29.pdf). |
| Payment | Same as filing | Same deadline |

### 5.8 Penalties

**Penalties**

| Offence | Penalty |
| --- | --- |
| Ordinary late filing/payment with tax due | General surcharge 25% where section 248(A) applies. Covered micro and small taxpayers generally use 10%, subject to the timing and assessment rules. |
| Interest | Generally 12% per year on unpaid tax, or 6% for qualifying micro and small taxpayers. Apply the relevant tax base and period. |
| Information-return failure | Generally PHP 1,000 per failure, maximum PHP 25,000 per calendar year. Covered micro and small taxpayers use PHP 500 and PHP 12,500. Check statutory notice and reasonable cause. |
| Invoice offences | Classify the actual failure. Failure to issue a required invoice has its own statutory consequences. The 50% surcharge can apply to a specified erroneous VAT invoice, or to wilful neglect or false/fraudulent filing under section 248(B). |

## When to refuse or refer

### 6.1 Entertainment expense input VAT limit

- **Entertainment expenses.** Check the VAT invoice and connection with taxable business. The 0.5% of net sales and 1% of net revenue limits apply to the income-tax deduction for eligible entertainment, amusement and recreation expenses. Assess input VAT separately under section 110. [RR 10-2002](https://bir-cdn.bir.gov.ph/BIR/pdf/2294rr10_02.pdf).

### 6.2 Zero-rating for services to non-residents

- **Foreign-client services.** Verify the section 108(B)(2) client and service conditions, acceptable foreign currency and accounting under BSP rules. Bank credit advice can be evidence. Hold the treatment until these facts are available.

### 6.3 PEZA zero-rating

- **Registered buyers.** Confirm eligibility and certification from the appropriate authority. Check direct attribution to the eligible activity and the applicable incentive period.

### 6.4 Digital services – foreign provider VAT status

- **Foreign digital services.** Establish the purchaser's B2B/B2C status and any exemption. For covered B2B supplies, obtain the supplier invoice and the filed Form 1600-VT to support the buyer's applicable input VAT claim.

### 6.5 Motor vehicle expenses

- **Motor vehicle expenses.** Determine actual taxable business use, check the invoice and apply the passenger-vehicle limitations. Hold any input credit until the facts support it.

## Section 7 – Excel working paper template

```
PHILIPPINES VAT WORKING PAPER
Period: ____________  TIN: ____________  RDO: ____________

A. OUTPUT VAT
  A1. Taxable sales at 12% (net)               ___________
  A2. Output VAT at 12% (A1 × 12%)             ___________
  A3. Zero-rated sales (exports/non-resident)  ___________
  A4. Exempt sales (net)                        ___________

B. INPUT VAT
  B1. Domestic purchases – 12% (net)           ___________
  B2. Input VAT at 12% (B1 × 12%)              ___________
  B3. Importation input VAT                    ___________
  B4. Total input VAT (B2+B3)                  ___________
  B5. Disallowed input (blocked items)         ___________
  B6. Net input VAT (B4 − B5)                  ___________

C. NET VAT PAYABLE
  C1. Net VAT (A2 − B6)                         ___________
  C2. Excess credit from prior period           ___________
  C3. Creditable VAT withheld and eligible VAT payments ___________
  C4. Net payable / excess credits (C1 − C2 − C3) ___________

REVIEWER FLAGS:
  [ ] VAT invoices and required withholding VAT evidence verified?
  [ ] Foreign-client and BSP payment evidence confirmed where applicable?
  [ ] Applicable registered-enterprise certification and direct attribution verified?
  [ ] Digital service provider VAT registration confirmed?
  [ ] Motor vehicle input VAT blocked where applicable?
  [ ] Entertainment input VAT supported by evidence and taxable business use?
```

## Section 8 – Bank statement reading guide

### Common Philippine bank statement formats

**Common Philippine bank statement formats**

| Bank | Key columns | Date format | Amount |
| --- | --- | --- | --- |
| BDO | Date, Reference, Description, Debit, Credit, Balance | MM/DD/YYYY | PHP with 2 decimals |
| BPI | Date, Transaction Reference, Description, Withdrawal, Deposit, Balance | MM/DD/YYYY | PHP |
| Metrobank | Date, Description, Debit, Credit, Balance | MM/DD/YYYY | PHP |
| UnionBank | Date, Description, Debit, Credit, Available Balance | MM/DD/YYYY | PHP |
| Landbank | Posting Date, Description, Debit, Credit, Running Balance | MM/DD/YYYY | PHP |

### Key Philippine banking terms

**Key Philippine banking terms**

| Term | Meaning | Classification hint |
| --- | --- | --- |
| CREDIT / DEPOSIT | Incoming funds | Potential revenue |
| DEBIT / WITHDRAWAL | Outgoing payment | Potential expense |
| INWARD REMITTANCE | Foreign currency receipt | Potential zero-rated export |
| SERVICE CHARGE | Bank fee | Exempt |
| INTEREST | Bank interest | Exempt |
| BALANCE | Running balance | Ignore |
| ATM WITHDRAWAL | Cash withdrawal | Tier 2 – ask |
| PAYROLL DEBIT | Salary payment | Out of VAT scope |

## Section 9 – Onboarding fallback

If the client provides a bank statement but cannot answer all questions immediately:

1. Classify all transactions using the pattern library (Section 3)
2. Apply conservative defaults (Section 1)
3. Mark Tier 2 items as "PENDING – reviewer must confirm"
4. Generate working paper with flags

Reconcile the provisional entries to the VAT invoices, journals and other applicable records before completing the return.

```
PHILIPPINES VAT ONBOARDING – MINIMUM QUESTIONS
1. TIN (Tax Identification Number) and RDO (Revenue District Office)?
2. Certificate of Registration (BIR Form 2303) – VAT registered? What is the effective date?
3. Confirm calendar or fiscal quarters, filing platform and any optional 2550M already paid.
4. Do you have any exports or services to non-resident clients?
   If yes: is the customer eligible and is allowable foreign-currency payment accounted for under BSP rules?
5. Do you have any PEZA-registered customers?
6. Motor vehicle expenses – are vehicles exclusively for business?
7. Any digital services from nonresident providers? Check buyer status and any 1600-VT remittance.
8. Prior period excess input VAT credit carried forward?
```

## Sources

### Key legislation

**Key legislation**  _(RA 12023 (VAT on Digital Services Law, Oct 2024). Corrected by Jonathan I. Ruiz (CPA, Philippines))_

| Source | URL | What was read | Read on |
| --- | --- | --- | --- |
| NIRC and EOPT | [RA 8424](https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/2/3896), [RA 11976](https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/2/96948) | Sections 105–110, 112–114, 116–118, 128, 236–237, 248 and 250 for the taxable base, invoices, credits, filing and penalties. | 2026-11-24 |
| TRAIN and implementation | [RA 10963](https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/2/80559), [RR 13-2018](https://bir-cdn.bir.gov.ph/local/pdf/RR%20No.%2013-2018%20Corrected%20Copy.pdf) | Section 37, taxable transport, exemptions and the quarterly return transition. | 2026-11-24 |
| EOPT VAT and invoicing | [RR 3-2024](https://bir-cdn.bir.gov.ph/BIR/pdf/RR%20No.3-%202024.pdf), [RR 7-2024](https://bir-cdn.bir.gov.ph/BIR/pdf/RR%20No.%207-%202024.pdf), [RR 11-2024](https://bir-cdn.bir.gov.ph/BIR/pdf/RR%2011-2024.pdf) | Registration threshold, accrual, section 3 invoice evidence and converted stock. | 2026-11-24 |
| Filing | [RMC 52-2023](https://bir-cdn.bir.gov.ph/local/pdf/RMC%20No.%2052-2023%20(1).pdf), [Form 2550Q](https://bir-cdn.bir.gov.ph/BIR/pdf/2550Q%20%20April%202024%20ENCS_Final.pdf) | Read for the optional 2550M, mandatory quarterly return, Part IV calculation and Part II payment. | 2026-11-24 |
| Dwellings and zero-rating | [RR 1-2024](https://bir-cdn.bir.gov.ph/BIR/pdf/RR%20No.%201-2024.pdf), [RR 10-2025](https://bir-cdn.bir.gov.ph/BIR/pdf/RR%20No.%2010-2025%20%281%29.pdf), [RMC 66-2025](https://bir-cdn.bir.gov.ph/BIR/pdf/RMC%20No.%2066-2025.pdf) | Sections 2–4 of the dwelling regulation and the eligible export, registered project and certification rules. | 2026-11-24 |
| Digital services | [RA 12023](https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/2/97876), [RR 3-2025](https://bir-cdn.bir.gov.ph/BIR/pdf/RR%20No.%203-2025.pdf), [RMC 47-2025](https://bir-cdn.bir.gov.ph/BIR/pdf/RMC%20No.%2047-2025.pdf) | Sections 108-A, 108-B, 114(D) and 236(F); foreign supplier, buyer and withholding evidence requirements. | 2026-11-24 |
| Penalties and deductions | [RR 6-2024](https://bir-cdn.bir.gov.ph/BIR/pdf/RR%206-2024%20%28final%29.pdf), [RR 21-2018](https://bir-cdn.bir.gov.ph/local/pdf/RR%20No%2021-2018.pdf), [RR 12-2012](https://bir-cdn.bir.gov.ph/BIR/pdf/65716RR%20No%2012-2012.pdf), [RR 10-2002](https://bir-cdn.bir.gov.ph/BIR/pdf/2294rr10_02.pdf) | Read for reduced penalties, interest, vehicles and the separate section 34 entertainment deduction. | 2026-11-24 |

Not yet confirmed. The VAT status of a named counterparty, platform fee or service needs the invoice and the actual transaction. The eFPS sign-in workflow requires authorised taxpayer access.

### Known gaps

- PEZA zero-rating complex structures – escalate to CPA
- Government VAT withholding and separate nonresident withholding rules require the payer and transaction details.
- Percentage tax (non-VAT registered) – separate Form 2551Q; different skill
- Import VAT (Bureau of Customs process) – coordinate with customs broker
- Digital Economy VAT implementation – verify BIR RMC for latest guidance

### Self-check before filing

- [ ] VAT invoices and any qualifying withholding-return evidence held for input VAT.
- [ ] Client status and BSP payment evidence held for applicable export services.
- [ ] Registered-enterprise certification and attribution evidence held when required.
- [ ] Digital service VAT registration confirmed for foreign suppliers
- [ ] Prior period excess credit correctly applied
- [ ] Entertainment input VAT has valid evidence and a documented business purpose.

### Changelog

**Changelog**

| Version | Date | Change |
| --- | --- | --- |
| 1.0 | 2024 | Initial release |
| 2.0 | April 2026 | Full v2.0 rewrite: pattern library, worked examples, Digital Economy Act note, no inline tier tags |
| 2.1 | November 2026 | Verified the 2025 filing, invoice, registration, reverse-charge, supply and penalty rules. |

## Prohibitions

- Confirm appropriate invoice or remittance evidence and eligibility before claiming input VAT.
- Verify all statutory export-service conditions before applying zero-rating.
- Verify registered-enterprise eligibility, certification and direct attribution before applying zero-rating.
- Verify the reverse-charge remittance and other applicable evidence for an input VAT claim on foreign B2B digital services.
- NEVER apply 12% to exempt supplies (unprocessed agriculture, medical, education, etc.)
- NEVER present calculations as definitive – direct to a Philippine CPA or BIR-accredited tax practitioner

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for errors, omissions, or outcomes. All outputs must be reviewed by a qualified professional before filing.

The most up-to-date version is maintained at openaccountants.com.
