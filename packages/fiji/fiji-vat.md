---
name: fiji-vat
description: Prepare a 2026 Fiji VAT reconciliation from invoices, customs entries and bank transactions. Apply the current standard rate, distinguish zero-rated and exempt supplies, check imported services, preserve unresolved evidence and prepare TPOS return working papers. Load vat-workflow-base alongside this skill; supplier names alone do not establish tax treatment.
version: 2.1
jurisdiction: FJ
category: vat-gst
tax_year: 2026
last_updated: 2026-11-16
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: vat-gst
type: filing-howto
depends_on:
  - vat-workflow-base
---

# Fiji VAT v2.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Prepare the Fiji VAT return and transaction working paper for a registered person's taxable activity. The currency is FJD. This file covers ordinary domestic supplies, exports, purchases, imports, imported services, credit notes and evidence-based bank classification. It does not decide a special customs concession, tax-free-zone entitlement or a tourism operator's complete tax position.

Load **vat-workflow-base**, originally required at version 0.1 or later, alongside this file. The current base supplies the reconciliation, questions, workbook checks and reviewer brief, not Fiji law. Apply the actual Fiji period and legislation below. A bank statement starts an evidence inventory; it cannot establish tax invoices, entitlement to deductions, an export or a return ready for filing.

### Quick reference

| Item | Rule and conditions | Official source |
|---|---|---|
| Standard domestic VAT | 12.5% on a registered person's taxable supply in Fiji, effective from 1 August 2025; distinguish exempt and zero-rated supplies | [VAT Act s. 15; Act 10 of 2025 s. 5](https://www.parliament.gov.fj/wp-content/uploads/2025/08/Act-10-Value-Added-Tax-Budget-Amendment-Act-2025.pdf) |
| Tax-inclusive extraction | Derived: VAT = inclusive consideration / 9; net = inclusive consideration minus that VAT, only for a confirmed standard-rated inclusive amount | [FRCS calculation notice](https://frcs.org.fj/public-notice/value-added-tax-vat-calculation-notice/) |
| Zero rate | 0% only where the actual Schedule 2 description and conditions are satisfied, not merely because a customer is overseas | [VAT Act s. 15(2), Schedule 2](https://frcs.org.fj/files/2026/06/VALUE-ADDED-TAX-ACT-1991-Revised-to-1-August-2025.pdf) |
| Compulsory registration | FJD 100,000 taxable supplies under the retrospective or prospective rolling period tests for a person other than a produce supplier; apply the cessation/capital-asset exceptions and statutory conditions | [VAT Act s. 22](https://frcs.org.fj/files/2026/06/VALUE-ADDED-TAX-ACT-1991-Revised-to-1-August-2025.pdf) |
| Registration application | Within 21 days of becoming liable, including the specified forward-looking trigger | [VAT Act s. 22(3); FRCS guide](https://frcs.org.fj/our-services/taxation-section/non-individuals/reporting-and-paying-taxes/vat-guide/) |
| Return category | Monthly by default; quarterly requires CEO placement on application, with FJD 300,000 taxable-supplies test, not automatic placement from bank turnover | [VAT Act s. 32](https://frcs.org.fj/files/2026/06/VALUE-ADDED-TAX-ACT-1991-Revised-to-1-August-2025.pdf) |
| Return and payment | Last day of the month following the taxable period, including the input-tax schedule; do not substitute a general last-business-day rule | [VAT Act ss. 33, 40](https://frcs.org.fj/files/2026/06/VALUE-ADDED-TAX-ACT-1991-Revised-to-1-August-2025.pdf) |
| Imports | 12.5% on the statutory import value unless a specific relief or zero-rated import provision applies | [Act 10 of 2025 s. 4; VAT Act s. 14](https://www.parliament.gov.fj/wp-content/uploads/2025/08/Act-10-Value-Added-Tax-Budget-Amendment-Act-2025.pdf) |
| Imported services | Section 21 applies to the defined relevant services from a supplier belonging abroad to a recipient belonging in Fiji for its taxable activity; do not infer this solely from a brand | [VAT Act ss. 17, 21; Schedule 2 para. 14](https://frcs.org.fj/files/2026/06/VALUE-ADDED-TAX-ACT-1991-Revised-to-1-August-2025.pdf) |
| Tourism services tax | Separate 5% on a covered tourism business with annual gross turnover over FJD 2 million, effective 1 September 2026; show separately and do not charge VAT on the tax itself | [Tourism Services Tax Act ss. 1-4, Schedule](https://www.parliament.gov.fj/wp-content/uploads/2026/07/Act-20-Tourism-Services-Tax-Act-2026.pdf?ver=1794354122) |
| Hotel VAT tax point | Checkout or end of stay from 1 August 2026; distinguish earlier supplies and other timing rules | [Act 15 of 2026 ss. 1, 3](https://www.parliament.gov.fj/wp-content/uploads/2026/07/Act-15-Value-Added-Tax-Budget-Amendment-Act-2026.pdf?ver=1794354122) |

## Ask the client first

Obtain the client's FRCS TIN, registration status and effective date, exact return period and TPOS category, approved accounting basis, opening credit/refund position and prior returns. Ask what the business sells, where each activity is carried on, whether it exports, whether it has tourism/duty-free operations and whether any special concession is claimed.

Request bank statements for the complete period, sales and purchase ledgers, issued and received tax invoices with supplier TINs, credit/debit notes, customs entries, evidence of import VAT paid, export declarations and shipping records, and overseas-service contracts. BSP, HFC, ANZ Fiji, Westpac Fiji and Bred Bank statements are acceptable source records; no bank's CSV layout is assumed universal. Ask for the actual invoice entity, establishment, service, currency and purpose for every overseas subscription.

Resolve missing facts from the records first. Where registration, rate, supplier location or business-use allocation remains unknown, retain an open item and exclude the unsupported conclusion from the filing-ready totals. Do not assume a sale is standard rated or a supplier is domestic to fill a gap. Do not claim input tax until entitlement and documents are established. A held deduction is not a legal ruling that the purchase can never qualify.

## The method, step by step

### 1. Set the period, basis and tax point

Read the TPOS registration and return obligation before classifying. Section 32 makes monthly the default; a qualifying quarterly category needs the CEO's decision. Do not use the old FJD 500,000 monthly/quarterly split. Reconcile the actual taxable period to opening balances and prior filings. The compulsory registration limb expressly excludes a produce supplier. Apply the current definition: direct cultivation, harvest or farming, the required supply proportion and its statutory exceptions; a produce middleman does not qualify merely because it sells produce. Voluntary registration and cancellation have separate conditions. [VAT Act ss. 2, 22-23](https://frcs.org.fj/files/2026/06/VALUE-ADDED-TAX-ACT-1991-Revised-to-1-August-2025.pdf); [Act 10 of 2025 s. 2](https://www.parliament.gov.fj/wp-content/uploads/2025/08/Act-10-Value-Added-Tax-Budget-Amendment-Act-2025.pdf). [VAT Act ss. 32-33](https://frcs.org.fj/files/2026/06/VALUE-ADDED-TAX-ACT-1991-Revised-to-1-August-2025.pdf).

The ordinary tax point is the earliest of invoice, payment or delivery, with specific rules for deposits, periodic/progressive supplies, construction and other arrangements. From August the hotel/accommodation rule uses checkout or end of stay. A bank settlement date does not automatically replace the statutory point. Invoice accounting is the default; payments accounting requires a direction under section 36. [VAT Act ss. 18, 36-38](https://frcs.org.fj/files/2026/06/VALUE-ADDED-TAX-ACT-1991-Revised-to-1-August-2025.pdf); [Act 15 of 2026 s. 3](https://www.parliament.gov.fj/wp-content/uploads/2026/07/Act-15-Value-Added-Tax-Budget-Amendment-Act-2026.pdf?ver=1794354122).

### 2. Establish the supply before selecting a rate

Confirm that a payment represents a supply, who supplied it, where it is supplied, its consideration and the applicable tax point. Goods movements and services use different place-of-supply rules; the supplier's or recipient's relevant establishment matters for services. [VAT Act ss. 3, 15-19](https://frcs.org.fj/files/2026/06/VALUE-ADDED-TAX-ACT-1991-Revised-to-1-August-2025.pdf).

| Original classification topic | Correct treatment and evidence boundary | Official source |
|---|---|---|
| Ordinary domestic sale | Apply 12.5% only after taxable supply, registration, place and date are established | [Act 10 of 2025 s. 5; VAT Act ss. 15-18](https://www.parliament.gov.fj/wp-content/uploads/2025/08/Act-10-Value-Added-Tax-Budget-Amendment-Act-2025.pdf) |
| Exports | Zero-rated only under the relevant Schedule 2 entry; obtain export and remitted-earnings evidence, not just a foreign customer name | [VAT Act Schedule 2 chapeau and paras. 1-4, 14](https://frcs.org.fj/files/2026/06/VALUE-ADDED-TAX-ACT-1991-Revised-to-1-August-2025.pdf) |
| Basic food and essential items | Match the actual item and tariff description in Schedule 2 para. 31; the old phrase basic foodstuffs is not a blanket zero rate | [VAT Act Schedule 2 para. 31](https://frcs.org.fj/files/2026/06/VALUE-ADDED-TAX-ACT-1991-Revised-to-1-August-2025.pdf) |
| Prescription medicines | Do not use the repealed Schedule 2 para. 17 as current authority; hold any claim for special relief until the actual current item/concession is read | [VAT Act Schedule 2 para. 17 and s. 14](https://frcs.org.fj/files/2026/06/VALUE-ADDED-TAX-ACT-1991-Revised-to-1-August-2025.pdf) |
| Educational materials | The special educational-items entry in para. 26 has an expired limited period; distinguish exempt education by an eligible educational institution from retail supplies of books or stationery | [VAT Act Schedule 1 paras. 8-9 and definition; Schedule 2 para. 26](https://frcs.org.fj/files/2026/06/VALUE-ADDED-TAX-ACT-1991-Revised-to-1-August-2025.pdf) |
| Residential rent | Exempt where the dwelling is predominantly used as a place of residence or abode; distinguish commercial/hotel accommodation | [VAT Act Schedule 1 para. 2 and dwelling definition](https://frcs.org.fj/files/2026/06/VALUE-ADDED-TAX-ACT-1991-Revised-to-1-August-2025.pdf) |
| Medical services and insurance | No blanket medical-services exemption was established by reading Schedule 1; medical insurance is a specified exemption, a different transaction | [VAT Act Schedule 1 para. 1(b)](https://frcs.org.fj/files/2026/06/VALUE-ADDED-TAX-ACT-1991-Revised-to-1-August-2025.pdf) |
| Public transport | Qualifying licensed omnibus carriage is zero-rated under its specific entry, not generally exempt; other carriage needs its own analysis | [VAT Act Schedule 2 para. 27](https://frcs.org.fj/files/2026/06/VALUE-ADDED-TAX-ACT-1991-Revised-to-1-August-2025.pdf) |
| General versus life insurance | Identify the policy and premium: life/medical insurance and specified indemnity payments have limited exemptions; do not exempt all general-insurance premiums | [VAT Act s. 2 and Schedule 1 para. 1(b)](https://frcs.org.fj/files/2026/06/VALUE-ADDED-TAX-ACT-1991-Revised-to-1-August-2025.pdf) |

### 3. Use the supplier library as a queue, not a tax decision

| Bank description or supplier pattern | Review action |
|---|---|
| BSP, BANK SOUTH PACIFIC, HFC BANK, HFC, ANZ FIJI, WESTPAC FIJI, BRED BANK | Check whether the actual charge is an exempt banking/account operation under Schedule 1 para. 1(a). A bank may also sell taxable services. |
| INTEREST, LOAN, REPAYMENT | Separate loan principal, exempt credit/interest, fees and any other supply. Do not turn every line containing repayment into an excluded transaction. |
| FRCS, FIJI REVENUE | Match a tax payment to its liability and period; it is not an input-tax invoice merely because money left the account. |
| FNPF, FIJI NATIONAL PROVIDENT | Match pension contributions and adjustments to payroll; do not claim VAT on a pension remittance. |
| CUSTOMS, FIJI CUSTOMS | Split duty, import VAT and other charges from the assessed customs entry. Duty alone is not deductible input VAT. |
| EFL, ENERGY FIJI; WAF, WATER AUTHORITY; VODAFONE, DIGICEL | Read the bill and supplying entity. State water/sewerage has a specific Schedule 2 entry; ordinary electricity/telecommunications do not inherit one another's treatment. |
| SUN INSURANCE, FMF INSURANCE, QBE | Read the insurance contract, premium and levy breakdown; the brand does not identify the exemption. |
| GOOGLE, MICROSOFT, META, FACEBOOK, AMAZON, AWS, ZOOM, SLACK, CANVA, FIGMA | Read invoice entity and service scope, then apply sections 16-17 and 21; an overseas-looking name does not prove imported services. |
| SALARY, WAGES, OWN TRANSFER, DIVIDEND, CASH WITHDRAWAL | Match payroll, own-account transfers, distribution records or cash receipts; determine the underlying transaction. Withdrawal itself is not proof of a deductible purchase. |

The legal classification basis is VAT Act sections 2-3, 14-17, 21 and Schedule 1 para. 1, Schedule 2 para. 23. A supplier-pattern match is an internal workflow aid, never a statutory finding. [VAT Act](https://frcs.org.fj/files/2026/06/VALUE-ADDED-TAX-ACT-1991-Revised-to-1-August-2025.pdf).

Preserve the original workflow escalation flags: a single transaction of FJD 10,000 or a proposed tax difference of FJD 500 receives heightened review. These are **internal review controls**, not legal thresholds. A smaller unsupported classification also remains held.

### 4. Calculate output tax and eligible deductions separately

For a confirmed standard-rated tax-exclusive value multiply by the rate; for an inclusive amount use the tax fraction. Do not remove a VAT component from a foreign invoice that did not charge Fiji VAT. A foreign-currency amount must be expressed in FJD at the time of supply; section 83 does not establish a blanket RBF exchange-rate rule for every transaction. Retain conversion date, rate, evidence and any customs conversion separately. [VAT Act ss. 15, 19, 83](https://frcs.org.fj/files/2026/06/VALUE-ADDED-TAX-ACT-1991-Revised-to-1-August-2025.pdf); [FRCS inclusive/exclusive calculation](https://frcs.org.fj/public-notice/value-added-tax-vat-calculation-notice/).

Input tax is defined by reference to tax charged on a supply **to** the registered person, or import tax on goods, principally for its taxable activity. Attribute input wholly to taxable supplies, exclude that wholly attributable to non-taxable supplies and apportion common input under section 39, including any CEO-approved alternative basis and the limited de minimis test. Hold the required tax invoice or qualifying adjustment document before claiming; a debit on the bank statement is not enough. [VAT Act s. 2 input-tax definition, s. 39(2), (5), (7), ss. 41-42](https://frcs.org.fj/files/2026/06/VALUE-ADDED-TAX-ACT-1991-Revised-to-1-August-2025.pdf).

Private consumption, entertainment, passenger vehicles, taxis/rental vehicles and mixed-use costs must each be tested for taxable-activity purpose and deduction conditions. This reading did **not** establish the old blanket vehicle/entertainment prohibition or automatic taxi/rental exception. Record purpose, actual use, invoices and any applicable special rule. Until that evidence is sufficient, no deduction enters the ready-to-file total. Do not represent an evidential hold as a universal statutory block. [VAT Act ss. 2, 39](https://frcs.org.fj/files/2026/06/VALUE-ADDED-TAX-ACT-1991-Revised-to-1-August-2025.pdf).

For import VAT, use the customs value plus applicable duties, import excise and other specified charges, excluding VAT itself, subject to actual relief. Do not reduce the law to an unconditional CIF-plus-duty shortcut. From the enacted amendment's relevant commencement dates, the electric-vehicle concession paragraph was deleted and the drug-rehabilitation concession was added; a tariff code or concession must be checked against the actual date and authorisation. [VAT Act s. 14(1)-(4A)](https://frcs.org.fj/files/2026/06/VALUE-ADDED-TAX-ACT-1991-Revised-to-1-August-2025.pdf); [Act 15 of 2026 ss. 1-2](https://www.parliament.gov.fj/wp-content/uploads/2026/07/Act-15-Value-Added-Tax-Budget-Amendment-Act-2026.pdf?ver=1794354122).

### 5. Test imported services without manufacturing a matching input claim

Section 21 covers its defined relevant services, including the specified ICT/data-processing/professional categories, received for a taxable activity by a recipient belonging in Fiji from a supplier belonging abroad. Intra-entity foreign/Fiji establishments are treated separately and open-market-value rules can apply. Read the contract and the statutory service description. Use actual consideration, not a fictional VAT-inclusive net. [VAT Act s. 21(1)-(6), Schedule 2 para. 14](https://frcs.org.fj/files/2026/06/VALUE-ADDED-TAX-ACT-1991-Revised-to-1-August-2025.pdf).

The old automatic Output + Input posting is unsafe. The consolidation records that the express deduction language and subsection 21(3) were removed in 2020. A self-supplied output-tax liability does not itself prove tax on a supply **to** the recipient within the input-tax definition. Do not offset imported-service output with equal input merely to make the transaction tax neutral. Establish any separate deduction entitlement from the actual law and documents first; otherwise retain the output assessment and a held deduction separately. [VAT Act s. 2 input-tax definition, s. 21 legislative history, s. 39](https://frcs.org.fj/files/2026/06/VALUE-ADDED-TAX-ACT-1991-Revised-to-1-August-2025.pdf).

### 6. Apply adjustments and build the working paper

Link credit/debit notes to the original supply and reason. A supplier credit reduces output, a supplier debit increases it; the recipient makes the matching input adjustment only to the extent the original input deduction was available/claimed. On invoice accounting, use the period of issue under section 39(2)(c) and (3)(b), rather than backdating every note. For a registered person directed to use payments accounting under section 36, section 39(4) instead attributes the adjustment to payments made or received in the taxable period. That payments-basis rule does not apply to a hire-purchase agreement under which property passes to the bailee, a financial lease with an express purchase requirement or option at a guaranteed residual value or nil, or a supply between persons who are not independent of each other. Retain the actual accounting-basis direction and classify those exceptions before choosing the adjustment period. Bad-debt relief has separate accounting, recovery and CEO-satisfaction conditions. [VAT Act ss. 36, 39(2)-(4), 42-43](https://frcs.org.fj/files/2026/06/VALUE-ADDED-TAX-ACT-1991-Revised-to-1-August-2025.pdf).

Build a workbook with transaction/source ID, date, invoice and settlement dates, supplier/customer legal entity and TIN, description, FJD gross, tax-exclusive value, rate, output VAT, input VAT claimed, input held, business-use basis, domestic/imported goods/imported services category, standard/zero/exempt/outside-scope distinction, return field, evidence link and unresolved question. Keep opening credit, adjustments and refund claims separate. Reconcile sales, purchases, bank movements, customs records and the return summary without double counting.

The original Fiji summary fields remain: standard output, zero-rated output, exempt supplies, domestic input, import input and net VAT. Add imported-service output and any separately supported deduction visibly. Do not invent TPOS box numbers: open the actual period's return, map each ledger category to its displayed field and keep the preview before submission.

Check bank CSV delimiters, date order and credit/debit signs from actual statements; do not assume every BSP/HFC export uses one format. Match transfers between the client's own BSP/HFC/ANZ accounts on both sides. Investigate missing invoices and cash purchases rather than classifying them from narration alone. See the companion base for the full workbook controls.

### 7. File, pay and preserve the result

In FRCS TPOS select the client's VAT obligation and exact period. Complete the required return and input-tax schedule from the reconciled workbook, check the displayed totals and liability, and obtain the qualified review of the actual return before filing or payment. Record submission acknowledgement, assessment/payment reference and the next obligation. This instruction does not authorise an agent to submit a live return.

The return and ordinary payment deadline is the statutory month-end following the period. Keep nil/credit positions and the actual obligation visible; do not assume a refund or carried-forward credit has already been granted. Retain invoices, schedules, returns and relevant records for the statutory retention period. Late filing/payment and evasion fall under the Tax Administration Act and relevant VAT provisions; do not copy penalties from an undated summary or invent an automatic charge. [VAT Act ss. 33, 39-41, 65, 79](https://frcs.org.fj/files/2026/06/VALUE-ADDED-TAX-ACT-1991-Revised-to-1-August-2025.pdf); [FRCS filing/recordkeeping guide](https://frcs.org.fj/our-services/taxation-section/non-individuals/reporting-and-paying-taxes/vat-guide/).

## Worked cases

All original bank inputs are retained exactly. The added facts below are stated assumptions for each case, not facts proved by the bank line. Amounts are FJD and money outputs are rounded to cents.

### Case 1: standard domestic sale

**Original input:** `05.04.2026 ; PACIFIC TRADING LTD ; CREDIT ; Invoice FJ-041 ; FJD 1,090`

Assume the invoice proves a registered supplier's standard-rated domestic sale, gross consideration includes VAT and this is the correct period under its accounting basis. VAT is 121.11 and net sales 968.89. The old 1,000 net plus 90 VAT used the superseded rate. [Act 10 of 2025 s. 5](https://www.parliament.gov.fj/wp-content/uploads/2025/08/Act-10-Value-Added-Tax-Budget-Amendment-Act-2025.pdf); [FRCS calculation notice](https://frcs.org.fj/public-notice/value-added-tax-vat-calculation-notice/).

```oa-check
name: Fiji inclusive standard domestic sale
inputs:
  gross: 1090
steps:
  - vat: round(gross / 9, 2)
  - net_sales: gross - vat
expected:
  vat: 121.11
  net_sales: 968.89
```

### Case 2: exported produce

**Original input:** `15.04.2026 ; NZ IMPORTS LTD ; CREDIT ; Exported produce ; FJD 5,000`

Assume the goods export and remittance conditions are proved, this is an actual taxable export by the supplier, and the consideration is not a deposit for an uncompleted export. Net zero-rated sales are 5,000 and VAT is zero. Without the shipping/customs and earnings evidence this remains a held zero-rate classification, not a proven export from the customer name. [VAT Act Schedule 2 chapeau and paras. 1-4](https://frcs.org.fj/files/2026/06/VALUE-ADDED-TAX-ACT-1991-Revised-to-1-August-2025.pdf).

```oa-check
name: Fiji qualifying export with evidence
inputs:
  export_sales: 5000
steps:
  - output_vat: export_sales * 0
  - zero_rated_sales: export_sales
expected:
  output_vat: 0
  zero_rated_sales: 5000
```

### Case 3: Azure imported service

**Original input:** `18.04.2026 ; MICROSOFT ; DEBIT ; Azure April ; FJD -218`

The raw line alone is held: it does not identify the contracting entity, service description, establishments or whether Fiji VAT was charged. For a **separate conditional computation**, assume the invoice proves qualifying relevant services supplied by a person belonging abroad, received for the Fiji recipient's taxable activity, and consideration of 218 **excluding Fiji VAT**. Section 21 output tax is 27.25. The foreign charge remains 218, not the old invented net of 200. No matching input claim is supported by these facts; keep it out of deductible input. The additional tax increases the cash cost to 245.25 under those assumptions. If domestic Fiji VAT was actually charged, reclassify from the invoice instead. [VAT Act ss. 2, 17, 21, 39](https://frcs.org.fj/files/2026/06/VALUE-ADDED-TAX-ACT-1991-Revised-to-1-August-2025.pdf); [Act 10 of 2025 s. 5](https://www.parliament.gov.fj/wp-content/uploads/2025/08/Act-10-Value-Added-Tax-Budget-Amendment-Act-2025.pdf).

```oa-check
name: Fiji conditional foreign service no automatic input offset
inputs:
  signed_bank_amount: -218
  confirmed_exclusive_consideration: 218
steps:
  - bank_cost: abs(signed_bank_amount)
  - output_vat: round(confirmed_exclusive_consideration * 0.125, 2)
  - supported_input_vat: 0
  - additional_vat: output_vat - supported_input_vat
  - total_cost: bank_cost + additional_vat
expected:
  bank_cost: 218
  output_vat: 27.25
  supported_input_vat: 0
  total_cost: 245.25
```

### Case 4: account-operation fee

**Original input:** `30.04.2026 ; BSP ; DEBIT ; Account fee ; FJD -25`

Assume the statement and bank invoice establish an exempt current-account-operation fee under Schedule 1 para. 1(a), not taxable advice or another service. Record expense 25, no input VAT and a separately identified exempt purchase. A different service sold by that bank must be classified independently. [VAT Act Schedule 1 para. 1(a)](https://frcs.org.fj/files/2026/06/VALUE-ADDED-TAX-ACT-1991-Revised-to-1-August-2025.pdf).

```oa-check
name: Fiji confirmed exempt account-operation fee
inputs:
  signed_bank_amount: -25
steps:
  - expense: abs(signed_bank_amount)
  - deductible_input: 0
expected:
  expense: 25
  deductible_input: 0
```

## When to refuse or refer

- **R-FJ-1: duty-free or tax-free-zone operations.** Stop the special-concession classification. Obtain the actual customs approval, tariff/concession code, dates and movements and refer the special treatment; a zone name is not a general VAT exemption.
- **R-FJ-2: tourism levies and mixed supplies.** Preserve this referral trigger for hotels/resorts and other tourism services, but replace the obsolete instruction to stack STT/ECAL. The enacted Tourism Services Tax applies from September, separately from VAT; its tax itself is outside the VAT base. The VAT hotel tax point also changed from August. Identify the covered service, turnover and period before producing a tourism return. [Tourism Services Tax Act ss. 1-4 and Schedule](https://www.parliament.gov.fj/wp-content/uploads/2026/07/Act-20-Tourism-Services-Tax-Act-2026.pdf?ver=1794354122); [VAT amendment s. 3](https://www.parliament.gov.fj/wp-content/uploads/2026/07/Act-15-Value-Added-Tax-Budget-Amendment-Act-2026.pdf?ver=1794354122).
- Refer unresolved registration, establishment, export evidence, imported-service deduction, private/mixed use, vehicle/entertainment entitlement, missing invoice, opening credit or disputed period. Keep quantified alternatives and source records for the reviewer; do not guess a filing number.

## Sources

The following sources were opened and read on the dates shown. The scopes distinguish the provisions read from the rest of a long document. Enacted amendments take precedence over legislative-history text, old notices or bills. No accountant approval is added by this rewrite.

| Source and actual scope read | Official URL | Read date |
|---|---|---|
| Read for VAT Act consolidation: definitions of input tax, produce supplier and insurance; selected operative provisions and neighbours in ss. 3-4, 14-22, 32-43, 65, 79, 83; Schedules 1-2, including historical/repealed entries and neighbours | https://frcs.org.fj/files/2026/06/VALUE-ADDED-TAX-ACT-1991-Revised-to-1-August-2025.pdf | 2026-11-16 |
| Read for Act 10 of 2025: complete enacted amendment; commencement, standard/import rates, produce-supplier definition, concessions, refund provisions and payment-service/harvester entries | https://www.parliament.gov.fj/wp-content/uploads/2025/08/Act-10-Value-Added-Tax-Budget-Amendment-Act-2025.pdf | 2026-11-16 |
| Read for Act 15 of 2026: complete enacted amendment; distinct commencement dates, concessions and hotel tax point | https://www.parliament.gov.fj/wp-content/uploads/2026/07/Act-15-Value-Added-Tax-Budget-Amendment-Act-2026.pdf?ver=1794354122 | 2026-11-16 |
| Read for Tourism Services Tax Act 2026: complete enacted Act and Schedule; rate, threshold, tax base, invoice separation, payment/return and commencement | https://www.parliament.gov.fj/wp-content/uploads/2026/07/Act-20-Tourism-Services-Tax-Act-2026.pdf?ver=1794354122 | 2026-11-16 |
| Read for FRCS calculation notice: pre/post-change calculations and inclusive/exclusive examples | https://frcs.org.fj/public-notice/value-added-tax-vat-calculation-notice/ | 2026-11-16 |
| Read for FRCS VAT guide: registration, rates/history, taxpayer obligations, TPOS, records and payment instructions; historical rate tables are not current rules | https://frcs.org.fj/our-services/taxation-section/non-individuals/reporting-and-paying-taxes/vat-guide/ | 2026-11-16 |

Not yet confirmed: The actual client's TPOS fields and obligation, invoice/establishment facts, specific imported-service input entitlement, disputed special concessions, vehicle/entertainment special-rule claims and medicine-specific relief. These remain explicit holds; the general pattern library is not evidence of those facts.

Version 2.1 corrects the obsolete rate, return-category threshold, blanket supplier/exemption rules, imported-service arithmetic and tourism treatment. The four original raw inputs and all original topic/referral categories remain. Duplicate disclaimers and repeated compressed headings are consolidated into the notice and operative steps rather than repeated as separate rules.

The most up-to-date version is maintained at [openaccountants.com](https://openaccountants.com).
