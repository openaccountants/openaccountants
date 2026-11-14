---
name: australia-gst
description: Prepare or review Australian GST returns (BAS), including Simpler and full BAS, and classify bank statements, invoices and other evidence. Use for requests to prepare BAS, do GST, fill in BAS, create the return, GST return or Activity Statement. Covers Australia only. Apply the refusal catalogue for complex partial exemption, GST groups, margin schemes and going concerns. Read before GST work.
version: 2.6
jurisdiction: AU
tax_year: 2025
last_updated: 2026-11-15
tax_year_notes: "Worked examples include 2025-26; periods vary. GST credit attribution uses the current 2026 compilation."
type: situation-rules
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
review_status: pending_review
tier: 2
domain: vat-gst
---

# Australia GST

## Who this applies to

Read the full guide, including Cross-border points, before classifying transactions or completing a workpaper. Apply the refusal catalogue before using the calculation examples.

### Section 1 -- Quick reference

| Field | Value |
| --- | --- |
| Country | [Australia (Commonwealth of Australia)](https://www.legislation.gov.au/C2004Q00685/latest) |
| Standard rate | 10% (single rate -- no reduced rates) ([GST Act s 9-70](https://www.legislation.gov.au/C2004A00446/2026-01-01/2026-01-01/text/original/epub/OEBPS/document_1/document_1.html)) |
| GST-free (zero rate equivalent) | No GST on the supply; related input tax credits may be available under the normal credit rules ([GST Act ss 9-30, 11-5 and 11-15; Division 38](https://www.legislation.gov.au/C2004A00446/2026-01-01/2026-01-01/text/original/epub/OEBPS/document_1/document_1.html)) |
| Input taxed (exempt equivalent) | No GST; related credits generally blocked, subject to financial-supply exceptions in section 5.3 ([GST Act ss 9-30 and 11-15; Divisions 40 and 70](https://www.legislation.gov.au/C2004A00446/2026-01-01/2026-01-01/text/original/epub/OEBPS/document_1/document_1.html)) |
| Return form | BAS (Business Activity Statement); use the applicable Simpler BAS, full reporting or GST instalment method ([ATO GST reporting methods](https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/business-activity-statements-bas/goods-and-services-tax-gst/gst-reporting-methods)) |
| Online filing channels | [Online services for business](https://www.ato.gov.au/online-services/businesses-and-organisations-online-services/logging-in-to-online-services-to-business), myGov for individuals and sole traders, or SBR-enabled software ([ATO BAS lodgment options](https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/business-activity-statements-bas/how-to-lodge-your-bas)) |
| Authority | [Australian Taxation Office (ATO)](https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/business-activity-statements-bas/how-to-lodge-your-bas) |
| Reporting currency | AUD; convert foreign-currency consideration using the applicable GST rules ([GST Act s 9-85](https://www.legislation.gov.au/C2004A00446/2026-01-01/2026-01-01/text/original/epub/OEBPS/document_1/document_1.html); [GSTR 2001/2, paragraph 14](https://www.ato.gov.au/law/view/document?DocID=GST/GSTR20012/NAT/ATO/00001)) |
| Filing frequencies | Monthly (GST turnover >= $20M or another mandatory/elected monthly case); Quarterly (standard); Annual (eligible voluntary registration with an annual election in effect; generally GST turnover < $75,000, or < $150,000 for a non-profit body) ([GST Act Division 151](https://www.legislation.gov.au/C2004A00446/2026-01-01/2026-01-01/text/original/epub/OEBPS/document_2/document_2.html); [registration amounts, GST Regulations rr 23-15.01 and 23-15.02](https://www.legislation.gov.au/F2019L00417/2025-11-01/2025-11-01/text/original/epub/OEBPS/document_1/document_1.html)) |
| Deadline | Ordinary due dates: monthly, 21st of the following month; quarterly, 28th after quarter except December quarter, 28 February; annual, income-tax-return due date or 28 February if no income-tax return is required. Check the actual due date and any permitted extension ([GST Act ss 31-8 and 31-10](https://www.legislation.gov.au/C2004A00446/2026-01-01/2026-01-01/text/original/epub/OEBPS/document_1/document_1.html); [ATO annual GST reporting](https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/when-and-how-to-report-and-pay-gst/annual-gst-reporting)) |
| Primary legislation | [A New Tax System (Goods and Services Tax) Act 1999 (GST Act)](https://www.legislation.gov.au/C2026C00081) |
| Supporting legislation | [Taxation Administration Act 1953 (Schedule 1)](https://www.legislation.gov.au/C1953A00001/latest/details); [GST Regulations 2019](https://www.legislation.gov.au/F2019L00417/2025-11-01/2025-11-01/text/original/epub/OEBPS/document_1/document_1.html); [LCT Act 1999](https://www.legislation.gov.au/C2004A00463/latest/details); [WET Act 1999](https://www.legislation.gov.au/C2004A00452/latest/details) |
| Contributor | Open Accounting Skills Registry |
| Validation status | Pending accountant review |
| Skill version | 2.6 |

Annual reporting requires an eligible annual tax period election in effect. The entity must not be required to register and must have no GST instalment election in effect. The offshore rights/options exception in section 151-5(2) also applies. Each member of a GST group must be eligible. Notify the Commissioner in the approved form and establish the effective period before using annual reporting. An entity using the deferred GST scheme must withdraw from that scheme. The ATO's [annual GST reporting guidance](https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/when-and-how-to-report-and-pay-gst/annual-gst-reporting) explains how to make the annual election by phone or signed written application and the applicable deadlines. [GST Act ss 151-5, 151-10, 151-15 and 151-40](https://www.legislation.gov.au/C2004A00446/2026-01-01/2026-01-01/text/original/epub/OEBPS/document_2/document_2.html).

**Read this whole section before classifying anything.**

| Label | Meaning |
| --- | --- |
| G1 | Total sales (GST-inclusive basis in this worksheet; include GST-free and input-taxed sales and indicate the basis on the BAS) |
| G2 | GST-free exports reportable at G2 under ATO instructions: qualifying exported goods at free-on-board value and specified overseas-goods repair/treatment services; exclude ordinary exported services and international freight/insurance. See export reporting allocation. |
| G3 | Other GST-free sales, including ordinary GST-free exported services and international freight/insurance excluded from G2. Include each amount once in G1 through its primary category. |
| G4 | Input taxed sales (financial supplies, residential rent -- Division 40) |
| G5 | G2 + G3 + G4 (derived) |
| G6 | G1 minus G5 (derived -- total taxable sales, the base for output GST) |
| G7 | Adjustments on sales (bad debts, price changes -- Division 19) |
| G10 | Capital purchases on the selected GST-inclusive basis, subject to motor vehicle business-use/car-limit allocation and other reporting exceptions below |
| G11 | Non-capital purchases (operational expenses, stock -- GST-inclusive) |
| G12 | G10 + G11 (derived) |
| G13 | Purchases for making input taxed sales (no credit) |
| G14 | Purchases with no GST in the price (from unregistered, GST-free, wages) |
| G15 | Estimated purchases for private use (no credit) |
| G16 | G13 + G14 + G15 (derived) |
| G17 | G12 minus G16 (derived -- total creditable purchases) |
| G18 | Adjustments on purchases (Division 19, Division 129) |
| 1A | GST on sales (output GST) |
| 1B | GST on purchases (input tax credits) |

- **Simpler BAS reporting scope** -- Simpler BAS (turnover < $10M, default since 1 July 2017): Report only G1, 1A, 1B. No need for G2-G18.  _((ATO GST reporting))_
- **Full BAS reporting scope** -- Complete the labels required by the issued BAS. G4–G9 and G12–G19 are calculation-worksheet items, not a requirement to lodge every G label. Use G1, G2, G3, G10, G11, 1A and 1B where required, plus other tax labels that apply.  _(([ATO GST reporting](https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/business-activity-statements-bas/goods-and-services-tax-gst)))_
GST = inclusive price / 11 = exclusive price x 10%; inclusive = exclusive x 1.1; exclusive = inclusive / 1.1.

**Conservative defaults -- Australian-specific**

| Ambiguity | Default |
| --- | --- |
| Unknown GST status of a sale | Taxable at 10% |
| Unknown GST status of a purchase | No input tax credit claimed |
| Unknown business-use proportion (vehicle, phone, home office) | 0% credit |
| Unknown whether food is basic or prepared | Taxable at 10% (prepared food) |
| Unknown counterparty registration status | Verify registration and supply evidence; withhold unsupported credits and keep the treatment pending |
| Unknown SaaS billing entity location | Needs Input: obtain the invoice, contracting entity, GST registration, connection and use facts; no automatic reverse charge ([GST Act ss 84-5, 84-100](https://www.legislation.gov.au/C2004A00446/2026-01-01/2026-01-01/text/original/epub/OEBPS/document_1/document_1.html)) |
| Unknown insurance type (general vs life) | Needs Input: obtain the policy and premium breakdown; withhold unsupported credit |
| Unknown property type (commercial vs residential) | Residential (input taxed, no credit) |
| Unknown whether transaction is in scope | In scope |
| Cash withdrawal purpose | Owner drawing, exclude |

**Red flag thresholds**

| Threshold | Value |
| --- | --- |
| HIGH single-transaction size | AUD $5,000 |
| HIGH tax-delta on a single conservative default | AUD $500 |
| MEDIUM counterparty concentration | >40% of output OR input |
| MEDIUM conservative-default count | >4 across the return |
| LOW absolute net GST position | AUD $10,000 |

#### Related guides

| Question | Guide |
| --- | --- |
| The end-to-end BAS preparation sequence, reconciliation, label mapping and corrections | `au-bas-preparation.md` |
| PAYG withholding, PAYG instalment and FBT instalment labels | `au-gst-bas.md` |
| Property supplies, the margin scheme and GST at settlement | `au-gst-property.md` |
| Due dates, penalties, interest and remission | `au-lodgment-deadlines-penalties.md` |
| Account coding, evidence and reconciliation controls | `australia-bookkeeping.md` |

#### Required inputs

Obtain a bank statement covering the full BAS period, in CSV, PDF or pasted text, from any Australian business bank. Bank-only evidence supports a provisional transaction list, not a complete BAS.

Recommended: period sales invoices, particularly exports and GST-free sales; purchase tax invoices above $82.50 including GST unless a lawful exception applies; evidence for every credit; the client's written 11-digit ABN and prior BAS. Ideally obtain the complete Xero, MYOB or QuickBooks export, tax invoice register and prior BAS with credits carried forward.

Withhold unsupported credits from claimable totals and list them for review. The $500 review-priority flag is not an evidence threshold. A bank statement establishes neither GST nor creditable purpose. Establish cash/non-cash basis and all attributable transactions, including unpaid invoices and non-bank acquisitions. Return Needs Input for unsupported periods or amounts. [GST Act ss 29-10 and 29-80](https://www.ato.gov.au/law/view/document?docid=PAC/19990055/29-10).

#### Australia-specific refusal catalogue

If any trigger fires, stop, output the refusal message verbatim, end the conversation. Refusal is a safety mechanism.

- **R-AU-1 -- Partial exemption complex** -- Trigger: client makes both taxable/GST-free supplies AND input taxed supplies, and the input taxed proportion is not de minimis (financial acquisitions threshold exceeded). Message: "You make both taxable and input taxed supplies. Your input tax credits must be apportioned under Division 11 (s 11-30), which requires determining the extent of creditable purpose for each acquisition. This cannot be completed without a documented apportionment methodology confirmed by a registered tax agent. Please escalate."  _((Division 11, s 11-30))_
- **R-AU-2 -- GST groups** -- Trigger: client is part of a GST group under Division 48 or asks about group registration. Message: "GST groups under Division 48 require consolidation across the group with a representative member lodging a single BAS. Intra-group supplies are disregarded. This is out of scope for this skill. Please use a registered tax agent."  _((Division 48))_
- **R-AU-3 -- Margin scheme** -- Trigger: client sells property using the margin scheme under Division 75. Message: "Margin scheme transactions under Division 75 require computing GST on the margin (sale price minus acquisition cost) and confirming eligibility based on the original acquisition. This is too fact-sensitive for this skill. Please use a registered tax agent."  _((Division 75))_
- **R-AU-4 -- Going concern** -- Trigger: client sells or buys a business as a going concern under s 38-325. Message: "Going concern supplies under s 38-325 require verification that all three conditions are met (going concern, both parties registered, written agreement). Incorrect classification results in either 10% GST on the full sale price or a missed GST-free entitlement. Please use a registered tax agent to confirm eligibility before proceeding."  _((s 38-325))_
- **R-AU-5 -- Financial supply complex (financial institution)** -- Trigger: client is a financial institution (bank, insurer, super fund) whose primary supplies are input taxed financial supplies, or client asks about Reduced Input Tax Credits (RITC). Message: "Financial institutions making predominantly input taxed supplies require specialist apportionment, RITC calculations (75%/55%), and the financial acquisitions threshold test. This is out of scope. Please use a registered tax agent specialising in financial services GST."  _((RITC 75%/55%))_

## Rates, bands and thresholds

### Registration thresholds

_(GST Act, s 23-5; s 144-5; s 9-25(5)(d), s 9-25(7) and Div 84)_

| Entity type | Threshold | Legislation |
| --- | --- | --- |
| General business | $75,000/year | GST Act ss 23-5 and 23-15; [GST Regulations r 23-15.01](https://www.legislation.gov.au/F2019L00417/2025-11-01/2025-11-01/text/original/epub/OEBPS/document_1/document_1.html) |
| Non-profit | $150,000/year | GST Act ss 23-5 and 23-15; [GST Regulations r 23-15.02](https://www.legislation.gov.au/F2019L00417/2025-11-01/2025-11-01/text/original/epub/OEBPS/document_1/document_1.html) |
| Taxi/rideshare | Registration regardless of turnover | [ATO registering for GST](https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/registering-for-gst); GST Act s 144-5 |
| Non-resident digital supplier (B2C) | Registration threshold generally $75,000, or $150,000 for non-profits, based on relevant current/projected GST turnover from Australia-connected sales; check platform responsibility and exclusions | [ATO How Australian GST works](https://www.ato.gov.au/businesses-and-organisations/international-tax-for-business/gst-for-non-resident-businesses/how-australian-gst-works); GST Act ss 9-25(5)(d) and 9-25(7), Division 84 |

- **GST turnover composition** -- GST turnover includes taxable + GST-free supplies. Excludes input taxed, not connected with Australia, capital asset sales (unless regularly dealing).  _(GST turnover composition)_

### Key thresholds summary

_(s 23-5; TAA 1953; s 29-40; s 69-10; LCT Act; TAA Schedule 1; s 31-5; s 29-70)_

| Threshold | Value | Source |
| --- | --- | --- |
| Simpler BAS eligibility | Generally GST turnover < $10M; GST instalments and optional full reporting have separate conditions | [ATO GST reporting methods](https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/business-activity-statements-bas/goods-and-services-tax-gst/gst-reporting-methods) |
| Cash basis eligibility | Apply the cash-basis conditions in The base: the SBE test uses aggregated turnover; the non-business GST turnover limit is $2M inclusive | [GST Act ss 29-40 and 29-45](https://www.legislation.gov.au/C2004A00446/2026-01-01/2026-01-01/text/original/epub/OEBPS/document_1/document_1.html); [ITAA 1997 s 328-110](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_7/document_7.html) |
| Car limit | $69,674 (2024-25 and 2025-26); $69,883 (2026-27) | [ATO historical car limits](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/depreciation-and-capital-expenses-and-allowances/simpler-depreciation-for-small-business/assets-and-exclusions); [ATO 2026-27 thresholds](https://www.ato.gov.au/businesses-and-organisations/small-business-newsroom/car-thresholds-from-1-july); GST Act s 69-10 |
| LCT threshold (other vehicles) | $80,567 (2024-25 and 2025-26); $80,809 (2026-27) | [ATO LCT rate and thresholds](https://www.ato.gov.au/rates/luxury-car-tax-rate-and-thresholds/) |
| LCT threshold (fuel-efficient vehicles) | $91,387 (2024-25 and 2025-26); $91,661 (2026-27) | [ATO LCT rate and thresholds](https://www.ato.gov.au/rates/luxury-car-tax-rate-and-thresholds/) |
| No ABN withholding exemption | Payments of $75 or less excluding GST, subject to applicable rules | [ATO withholding if ABN is not provided](https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/payg-withholding/payments-you-need-to-withhold-from/withholding-from-suppliers/withholding-if-abn-not-provided) |
| Tax invoice buyer information | Total price >= $1,000 requires the buyer's identity or ABN; below that boundary the other ordinary invoice requirements still apply | [GST Act s 29-70](https://www.legislation.gov.au/C2004A00446/2026-01-01/2026-01-01/text/original/epub/OEBPS/document_1/document_1.html); [ATO tax invoices](https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/tax-invoices) |

## The base

### Section 8 -- Australian bank statement reading guide

- **CSV mapping:** confirm columns. CBA NetBank commonly uses comma-delimited DD/MM/YYYY with Date, Amount, Description and Balance; Westpac is similar. ANZ commonly uses Date, Transaction Details, Debit, Credit and Balance; NAB is similar. Revolut and Wise use ISO dates.
- **CBA descriptions:** merchant, card suffix and location; DIRECT DEBIT, TRANSFER TO/FROM, Pay Anyone recipient or BPAY biller/reference.
- **Own-account transfers:** exclude confirmed transfers amongst the client's accounts, including TRANSFER TO [account name], INTERNAL TRANSFER and OWN ACCOUNT. A sole trader's transfer to their personal account is a drawing, not wages; exclude it from BAS.
- **Refunds/reversals:** identify REFUND, REVERSAL, CHARGEBACK or CREDIT ADJUSTMENT. Record a negative against the original BAS label in the period booked.
- **Foreign currency:** convert to AUD at the transaction-date rate, using the RBA indicative rate or bank-statement rate; record it in Transactions column L.
- **BSB/account:** the 6-digit BSB (XX-XXXX) identifies bank/branch and can help identify the counterparty; it does not determine GST.
- **ABN:** reconcile any statement ABN with GST registration.
- **Unknown descriptions:** ask the client about merchant-terminal or BPAY-only codes. Do not classify unidentified transactions.
- **ATO payments:** PAYG withholding (W2), PAYG instalments (T7) and FBT instalments (F1) are tax payments, not supplies. Exclude them from GST classification but retain them for BAS labels W1-W5, T1-T9 and F1-F3.

### Cash vs accrual basis

| Feature | Cash | Accrual |
| --- | --- | --- |
| GST on sales reported | To the extent payment is received | Generally the earlier of any consideration or an invoice, subject to special rules |
| Input credits claimed | To the extent payment is made, with required evidence | Generally the earlier of any consideration or an invoice, with required evidence and applicable attribution rules |
| Who can use | Eligible entities under GST Act ss 29-40, 29-45 and 157-5; apply the conditions below | Anyone |

Cash-basis eligibility is not a single turnover test. A business may qualify as a small business entity under ITAA 1997 section 328-110, generally using the previous-year or likely current-year aggregated turnover below $10 million, subject to that section's conditions. Qualification only under the end-of-year test in subsection 328-110(4) is excluded for this choice. A non-business entity may qualify where its GST turnover does not exceed $2 million. Other routes cover the receipts method for income tax, a kind of enterprise determined by the Commissioner or the Commissioner's permission. Establish the applicable route and effective date before selecting cash accounting. [GST Act ss 29-40 and 29-45](https://www.legislation.gov.au/C2004A00446/2026-01-01/2026-01-01/text/original/epub/OEBPS/document_1/document_1.html); [ITAA 1997 ss 328-110 and 328-115](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_7/document_7.html). A separate rule covers endorsed charities, government schools and eligible gift-deductible entities, subject to the exclusions in section 157-5(3). [GST Act s 157-5](https://www.legislation.gov.au/C2004A00446/2026-01-01/2026-01-01/text/original/epub/OEBPS/document_2/document_2.html).

### Section 3 -- Supplier pattern library (Australian vendors)

Use merchant patterns to identify candidate treatments. Confirm the actual supply, supplier registration, invoice GST and creditable purpose before computing a credit. Resolve conflicts in favour of source documents and law. A merchant name alone cannot establish taxability or business use.

**How to read this table.** Match by case-insensitive substring on the counterparty name as it appears in the bank statement. If multiple patterns match, use the most specific. If none match, fall through to Tier 1 rules in Section 5.

#### 3.1 Australian banks (classify the actual service)

Confirmed business purchases of input taxed account services go to G11 where required on Full BAS, with zero credit. Input taxed does not mean excluded from G11. A bank/payment-provider name proves no treatment: identify the actual service and normal GST conditions from terms and invoice. GST Act s 40-5 and GST Regulations rr 40-5.09/40-5.12 distinguish financial and other services. [Current law](https://www.legislation.gov.au/C2004A00446/2026-01-01/text); [regulations](https://www.legislation.gov.au/F2019L00417/2025-11-01/text); [ATO purchases instructions](https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/completing-your-bas-for-gst/complete-your-bas/step-3-purchases).

| Pattern | Treatment | Notes |
| --- | --- | --- |
| CBA, COMMONWEALTH BANK, COMMBANK, NETBANK | Classify actual service; confirmed business account service: G11, zero credit | Obtain fee terms and supporting statement/invoice. |
| WESTPAC, ST GEORGE, BANK OF MELBOURNE, BANKSA, ANZ, ANZ BANK, NAB, NATIONAL AUSTRALIA BANK, MACQUARIE, MACQUARIE BANK, BENDIGO BANK, ADELAIDE BANK, SUNCORP BANK, BOQ, BANK OF QUEENSLAND, UP BANK, ING DIRECT, ING AUSTRALIA | Same actual-service check | No automatic exclusion or GST credit from the name. |
| REVOLUT, WISE (fee lines) | Classify actual service from terms and invoice | A transaction, maintenance or subscription label alone does not settle GST. |
| INTEREST, INT PAID, INT RECEIVED | Needs Input until the payment or receipt and financial arrangement are identified | Distinguish business purchase reporting, input taxed income and other movements; do not infer treatment from this substring. |
| LOAN, HOME LOAN, PERSONAL LOAN, MORTGAGE | Exclude confirmed principal movements only | Separate interest, fees and other components before classification. |

#### 3.2 ATO and government (classify the actual payment)

Identify the payment, notice/invoice and legal basis; an agency name creates no exclusion. Division 81 distinguishes taxes/qualifying fees that are not consideration from payments that are; apply prescribed exceptions/overlap rules in rr 81-10.01, 81-15.01/02. Consideration alone establishes neither taxability nor credit: apply ordinary GST rules. Unidentified payment: Needs Input. [GST Act Division 81](https://www.legislation.gov.au/C2004A00446/2026-01-01/text); [regulations](https://www.legislation.gov.au/F2019L00417/2025-11-01/text).

| Pattern | Treatment | Notes |
| --- | --- | --- |
| ATO, AUSTRALIAN TAXATION OFFICE | Exclude a confirmed tax remittance from purchase reporting | Identify the payment; a counterparty match alone is insufficient. |
| ATO BAS, BAS PAYMENT | Exclude a confirmed GST remittance | Retain the payment for reconciliation. |
| ASIC, AUSTRALIAN SECURITIES | Check the specific fee and Division 81 treatment | Do not classify every payment from the agency name. |
| COUNCIL RATES, CITY OF, SHIRE OF | Check the notice and actual tax, fee or supply | A council may also make supplies for consideration. |
| STATE REVENUE, OSR, REVENUE NSW, SRO VIC | Check the notice and specific tax or payment | For supported stamp duty included in a purchase payment, also apply column O below. |
| CENTRELINK, SERVICES AUSTRALIA | Identify the benefit, grant or other payment and its conditions | Do not infer supply status from the agency name. |
| DEPARTMENT OF, DEPT OF | Needs Input until the actual payment is established | No blanket sovereign-act exclusion. |
| WORKCOVER, WORKSAFE, ICARE | Check the policy, premium breakdown, GST and creditable use | A workers compensation description alone does not establish a credit; exclude supported stamp duty from G10/G11 reporting. |

#### 3.3 Australian utilities (taxable 10%)

_(GST Act ss 38-285 and 38-290; GSTR 2000/25)_

| Pattern | Treatment | BAS Label | Notes |
| --- | --- | --- | --- |
| ORIGIN ENERGY, ORIGIN, AGL, AGL ENERGY, ENERGY AUSTRALIA, ENERGYAUST, ALINTA ENERGY, RED ENERGY, SIMPLY ENERGY | Domestic 10% | G11 | Electricity, gas -- overhead |
| TELSTRA, TELSTRA CORP, OPTUS, SINGTEL OPTUS | Domestic 10% | G11 | Telecommunications -- overhead |
| TPG, TPG TELECOM, VODAFONE AU, IINET | Domestic 10% | G11 | Telecommunications/broadband -- overhead |
| NBN CO, NBN | Domestic 10% | G11 | National Broadband Network -- overhead |
| SYDNEY WATER, MELBOURNE WATER, SA WATER | GST-free, subject to actual supply | G11 | Piped water and associated metering are generally GST-free; distinguish separate installation/repair services. GST Act ss 38-285 and 38-290; GSTR 2000/25 |

#### 3.4 Australian insurance (mixed treatment)

| Pattern | Treatment | Notes |
| --- | --- | --- |
| QBE, QBE INSURANCE | Domestic 10% | General insurance -- taxable, GST claimable |
| SUNCORP INSURANCE, GIO, AAMI, NRMA INSURANCE, NRMA, ALLIANZ AUSTRALIA, CGU, ZURICH AUSTRALIA | Domestic 10% | General insurance -- taxable |
| AMP LIFE, MLC LIFE, TAL LIFE | EXCLUDE | Life insurance -- input taxed, Division 40 |
| HEALTH INSURANCE, MEDIBANK, BUPA, HCF, NIB | GST-free; no GST credit | Private health insurance is generally GST-free under s 38-55; check actual policy and private use |
| WORKCOVER, WORKSAFE, ICARE | Check the policy, premium breakdown, GST and creditable use | Withhold unsupported credit; exclude supported stamp duty from G10/G11 reporting. |

#### 3.5 Australian transport (taxable 10%)

| Pattern | Treatment | BAS Label | Notes |
| --- | --- | --- | --- |
| UBER AU, UBER AUSTRALIA, UBER *AU | Domestic 10% | G11 | Rideshare -- taxable. Driver must be GST-registered regardless of turnover. |
| DIDI, DIDI AU | Domestic 10% | G11 | Rideshare -- taxable |
| 13CABS, SILVER TOP, TAXI | Domestic 10% | G11 | Taxi -- taxable (mandatory GST registration) |
| SYDNEY TRAINS, TRANSPORT NSW, OPAL | Domestic 10% | G11 | Public transport -- taxable at 10% (Australia does not zero-rate public transport) |
| METRO TRAINS MELBOURNE, MYKI, PTV | Domestic 10% | G11 | Public transport -- taxable at 10% |
| TRANSLINK, GO CARD | Domestic 10% | G11 | QLD public transport -- taxable |
| QANTAS, QANTAS AIRWAYS (domestic) | Domestic 10% | G11 | Domestic flights -- taxable at 10% |
| VIRGIN AUSTRALIA (domestic), JETSTAR (domestic) | Domestic 10% | G11 | Domestic flights -- taxable |
| QANTAS (international), VIRGIN (international) | GST-free | G11 | International flights -- GST-free export (Division 38-E). Check ticket destination. |
| TOLL, LINKT, TRANSURBAN, CITYLINK, EASTLINK | Domestic 10% | G11 | Toll road charges -- taxable |

#### 3.6 Australian food (basic food GST-free, prepared food 10%)

| Pattern | Treatment | Notes |
| --- | --- | --- |
| WOOLWORTHS, WOOLWORTHS METRO | TIER 2 -- split required | Supermarket: basic food items GST-free, non-food/prepared food at 10%. Default: treat as mixed, ask for receipt breakdown. If evidence is missing, leave any unsupported credit unclaimed pending review; do not invent a 50/50 split. |
| COLES, COLES EXPRESS | TIER 2 -- split required | Same as Woolworths |
| IGA, FOODWORKS, ALDI | TIER 2 -- split required | Same -- basic food GST-free, other items 10% |
| HARRIS FARM, FRUIT MARKET, GREENGROCER | GST-free | Basic food (fruit, vegetables) -- Division 38-A |
| UBER EATS, DOORDASH, MENULOG, DELIVEROO | Domestic 10% | Prepared/delivered food -- taxable. Delivery fee also taxable. |
| MCDONALD'S, KFC, HUNGRY JACK'S, SUBWAY, DOMINOS | Domestic 10% | Prepared food/restaurant meals -- always taxable |
| RESTAURANT, CAFE, BISTRO, PIZZERIA | Domestic 10% | Prepared food -- always taxable |
| BWS, DAN MURPHY'S, LIQUORLAND, FIRST CHOICE | Domestic 10% | Alcohol -- always taxable at 10% (plus excise/WET) |

#### 3.8 Payment processors (classify the actual service)

_([GSTR 2019/2](https://www.ato.gov.au/law/view/document?docid=GST/GSTR20192/NAT/ATO/00001))_

| Pattern | Treatment | Notes |
| --- | --- | --- |
| STRIPE AU, STRIPE PAYMENTS AUSTRALIA | Check invoice and service | Merchant payment processing is not automatically input-taxed credit; claim only verified GST for creditable use |
| PAYPAL, SQUARE AU, TYRO, EFTPOS, MERCHANT FEE | Check invoice and service | Distinguish processing services, cross-border supplies and financial supplies |
| AFTERPAY, ZIP PAY, ZIP MONEY | Check contract and invoice | Classify merchant services separately from lending and other financial supplies |

[GSTR 2019/2](https://www.ato.gov.au/law/view/document?docid=GST/GSTR20192/NAT/ATO/00001) distinguishes credit supplied to a cardholder from payment services supplied to a merchant.

#### 3.9 Professional services (taxable 10%)

| Pattern | Treatment | BAS Label | Notes |
| --- | --- | --- | --- |
| Accountant names, CPA, CA, CHARTERED ACCOUNTANT | Domestic 10% | G11 | Professional service -- always deductible if business purpose |
| TAX AGENT, BAS AGENT, BOOKKEEPER | Domestic 10% | G11 | Tax/BAS agent fees -- deductible |
| SOLICITOR, LAWYER, BARRISTER, LAW FIRM | Domestic 10% | G11 | Legal fees -- deductible if business purpose |
| ARCHITECT, ENGINEER, SURVEYOR | Domestic 10% | G11 | Professional service |
| MARKETING, ADVERTISING, DESIGN, AGENCY, CLEANER, CLEANING, OFFICE CLEANING, IT SUPPORT, COMPUTER, TECH SUPPORT | Domestic 10% | G11 | Business service |

#### 3.10 Property (commercial vs residential)

| Pattern | Treatment | Notes |
| --- | --- | --- |
| COMMERCIAL RENT, OFFICE RENT, WAREHOUSE RENT | Domestic 10% | Commercial lease -- landlord must be GST-registered. GST credit claimable. |
| RETAIL LEASE, SHOP RENT, INDUSTRIAL RENT | Domestic 10% | Commercial lease -- taxable |
| RESIDENTIAL RENT, HOME RENT, APARTMENT RENT | EXCLUDE | Residential rent -- input taxed (Division 40). No GST, no credit on related costs. |
| REAL ESTATE AGENT (rental management fee) | TIER 2 | If managing commercial property: 10% taxable, credit claimable. If managing residential property: 10% taxable, but NO credit (cost relates to input taxed supply). |
| STRATA, BODY CORPORATE, OWNERS CORP | Review supply and registration | G11 |
| AIRBNB, STAYZ, BOOKING.COM (income) | Review premises and supply | G1 or G4 as applicable |

#### 3.11 Superannuation (not a supply -- exclude)

| Pattern | Treatment | Notes |
| --- | --- | --- |
| SUPER, SUPERANNUATION, SUPER FUND | EXCLUDE | Employer SG contributions -- not a supply, out of scope for GST |
| AUSTRALIAN SUPER, REST SUPER, HOSTPLUS, SUNSUPER, CBUS, HESTA, UNISUPER | EXCLUDE | Super fund contributions -- out of scope |
| SMSF, SELF MANAGED SUPER | EXCLUDE | SMSF contributions -- out of scope |

#### 3.12 Payroll (exclude entirely)

| Pattern | Treatment | Notes |
| --- | --- | --- |
| SALARY, WAGES, PAYROLL, PAY RUN | EXCLUDE | Employment relationship -- not a supply, out of scope |
| SUPER GUARANTEE, SGC, SG PAYMENT | EXCLUDE | Superannuation contribution -- out of scope |
| WORKCOVER, WORKSAFE PREMIUM, ICARE | Check the policy, premium breakdown, GST and creditable use | Withhold unsupported credit; exclude supported stamp duty from G10/G11 reporting. |
| PAYG WITHHOLDING, TAX WITHHELD | EXCLUDE | PAYG withholding remitted to ATO -- tax payment |
| LEAVE LOADING, ANNUAL LEAVE, LONG SERVICE | EXCLUDE | Employment entitlement -- out of scope |
| DIRECTOR FEE (outgoing) | EXCLUDE | Director fees -- generally out of scope for GST |

### Section 5 -- Tier 1 classification rules

Each rule states the legal source and the BAS label mapping. Apply silently if the data is unambiguous.

#### 5.1 Taxable supplies (10%)

Under GST Act ss 9-5 and 9-70, a supply is taxable at Australia's single 10% rate only if it is for consideration, in the course or furtherance of an enterprise, connected with the indirect tax zone (Australia), and made by a supplier registered or required to register, and is neither GST-free (Division 38) nor input taxed (Division 40). There are no reduced rates. Sales map to G1 (G6 derived) and GST to 1A; capital/non-capital purchases to G10/G11 and eligible credits to 1B. Common taxable supplies include legal, accounting and consulting services, commercial rent, construction, telecommunications, general insurance, software licences, vehicle sales, restaurant/cafe meals, domestic transport, office supplies and equipment.

#### 5.2 GST-free supplies (0%, credits retained)

- **GST-free supplies overview** -- GST-free supplies attract 0% GST but the supplier retains full input tax credit entitlements on related costs. This mirrors the EU concept of zero-rated supplies. Sales: include once in G1 and use G2 or G3 as directed by the ATO sales instructions, rather than treating every export as G2. On Simpler BAS, include in G1 only.  _((GST Act, Division 38))_

_((GST Act, Division 38))_

| Category | Subdivision | Key items |
| --- | --- | --- |
| Basic food | 38-A | Bread, milk, meat, fruit, vegetables, flour, rice, eggs, butter, plain water, tea, coffee (unbrewed). EXCLUDES prepared/restaurant food, confectionery, soft drinks, snack foods, alcohol, ice cream. |
| Health services | 38-B | GP, specialist, hospital, dental, physiotherapy, chiropractic, ambulance. Must be Medicare-eligible or registered health practitioner. EXCLUDES cosmetic/elective surgery, veterinary. |
| Education | 38-C | School fees (primary/secondary), university tuition, TAFE/RTO vocational training. EXCLUDES commercial training, private tutoring. |
| Childcare | 38-D | Approved long day care, family day care, before/after school care. |
| Exports of goods | 38-E | Under section 38-185 item 1, export before or within 60 days after the earlier of receiving any consideration or issuing an invoice. Item 2 has a separate final-instalment trigger for qualifying instalment contracts. The Commissioner may allow further time. [GST Act section 38-185](https://www.ato.gov.au/law/view/document?docid=PAC/19990055/38-185) |
| Exports of services | 38-E | Services to non-resident consumed outside Australia. |
| Religious services | 38-F | By religious institution as part of religious practice. |
| Water and sewerage | 38-G | Supply of water by government/utility (basic supply). |
| Going concern | 38-J | Sale of business as going concern (both registered, written agreement) -- but R-AU-4 fires. |

_((Subdivision 38-A))_

| Food item | Treatment | Reasoning |
| --- | --- | --- |
| Fresh fruit and vegetables, Fresh meat, poultry, fish, Bread, rolls, Milk, cream, cheese, Rice, pasta, flour, Eggs, Cooking oil, margarine, butter, Baby food, infant formula, Bottled water (plain), Tea, coffee (unbrewed), Raw, unprocessed nuts | GST-free | Basic food |
| Ordinary plain biscuits (not chocolate) | Taxable 10% | GST Act Schedule 1 item 32; specified breakfast-cereal biscuits and infant/invalid rusks have exceptions |
| Confectionery (chocolate, lollies), Soft drinks, energy drinks, Ice cream, Snack foods (chips, pretzels) | Taxable 10% | Schedule 1 exclusion |
| Prepared meals (takeaway, restaurant) | Taxable 10% | Food supplied ready for consumption |
| Hot food (pies, sausage rolls heated) | Taxable 10% | Heated for consumption |
| Alcohol | Taxable 10% + excise/WET | Never GST-free |
| Chocolate-coated biscuits | Taxable 10% | Confectionery |
| Muesli bars, Honey-roasted/flavoured nuts | Taxable 10% | Snack food |

#### 5.3 Input taxed supplies and credit restrictions

Input taxed supplies: no GST is charged, and related acquisitions generally do not have a creditable purpose. Sales go to G4. Check financial-supply exceptions before treating every related purchase as a blocked G13 credit. Under section 11-15(4) and Division 189, acquisitions relating to financial supplies may remain creditable where the financial acquisitions threshold is not exceeded. Test both the $150,000 and 10% limbs over the required periods. Also check the borrowing exception in section 11-15(5) and reduced input tax credits for eligible acquisitions under Division 70. These are specific exceptions, not a general credit entitlement for residential rental costs. See [GSTR 2003/9](https://www.ato.gov.au/law/view/document?docid=GST/GSTR20039/NAT/ATO/00001). GST-free supplies, by contrast, generally preserve credit entitlement.  _([GSTR 2003/9](https://www.ato.gov.au/law/view/document?docid=GST/GSTR20039/NAT/ATO/00001))_

_((GST Act, Division 40))_

| Category | Section | Key items |
| --- | --- | --- |
| Financial supplies | 40-5 | Interest, loan fees, currency exchange margins, credit card fees (issuer), share dealings, guarantee fees, life insurance, super fund management |
| Residential rent | 40-35 | Rental of existing residential premises. Commercial rent is taxable. |
| Sale of existing residential premises | 40-65 | Previously sold as residential, not new/substantially renovated |
| Life insurance | 40-5 | General insurance is taxable |

| Supply | Treatment |
| --- | --- |
| Residential rent (existing premises) | Input taxed |
| Sale of existing residential premises | Input taxed |
| Sale of NEW residential premises | Taxable 10% (first sale after construction/substantial renovation) |
| Commercial rent (office, retail, warehouse) | Taxable 10% |
| Short-stay accommodation | Classify the premises and supply |

#### 5.4 Out-of-scope transactions (not on BAS)

| Transaction | Reason |
| --- | --- |
| Wages, salaries, superannuation | Not a supply -- employment relationship |
| Dividends | Not a supply -- return on equity |
| Loan principal repayments | Not a supply -- repayment of capital |
| GST/income tax payments to ATO | Tax payment, not a supply |
| Private transactions by individuals | Generally outside the enterprise supply/credit rules, but check section 5.5 before excluding a purchase: recipient liability, including section 84-5 item 3, can apply without creditable use |
| Owner drawings/transfers | Internal, not a supply |
| Gifts/donations (no consideration) | No consideration = not a supply |

#### 5.6 Input tax credit entitlement (Division 11)

- **Entitlement conditions** -- Establish the s 11-5 creditable acquisition conditions, including taxable supply, consideration, registration and creditable purpose. Apply the attribution rules: generally hold a valid tax invoice before claiming, subject to the $82.50 including-GST exception and other lawful exceptions/discretion. The four-year claim limit is not permission to claim before obtaining required evidence.  _(([GST Act ss 11-5, 29-10, 29-80 and 93-5](https://www.ato.gov.au/law/view/document?docid=PAC/19990055/29-10)))_
- **Blocked credits** -- Generally no credit for acquisitions relating to input taxed supplies, subject to the financial-supply exceptions in section 5.3 (s 11-15 and Division 70); no credit for private/domestic use (s 11-15), entertainment where FBT exempt (s 69-5), non-deductible fines/penalties (s 69-5).  _((s 11-15, s 69-5))_
- **Car limit** -- Where GST Act s 69-10 applies to a car purchase or importation, the credit is limited to the GST payable up to one-eleventh of the applicable car limit, reduced for partly creditable use. Check the statutory exceptions; the cap does not apply to acquisition by lease or hire. For 2024-25 and 2025-26 the car limit is $69,674 (one-eleventh is $6,334); for 2026-27 it is $69,883 (one-eleventh is $6,353). LCT paid is not itself a GST credit. [GST Act s 69-10](https://www.legislation.gov.au/C2004A00446/2026-01-01/2026-01-01/text/original/epub/OEBPS/document_1/document_1.html); [ATO purchasing a motor vehicle](https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/in-detail/your-industry/motor-vehicle-and-transport/gst-and-motor-vehicles/purchasing-a-motor-vehicle); [historical car limits](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/depreciation-and-capital-expenses-and-allowances/simpler-depreciation-for-small-business/assets-and-exclusions).

#### 5.7 Tax invoices (Division 29)

_((Division 29))_

| Ordinary supplier-issued tax invoice | Total price < $1,000 | Total price >= $1,000 |
| --- | --- | --- |
| Clearly intended to be a tax invoice | Yes | Yes |
| Supplier identity and ABN | Yes | Yes |
| Date of issue | Yes | Yes |
| What is supplied, including quantity (if applicable) and price | Yes | Yes |
| Extent to which each supply is taxable | Yes | Yes |
| GST payable for each supply | Yes | Yes |
| Recipient identity or ABN | Not normally required | Yes |

Use the total price including GST for the $1,000 boundary. A statement that the total price includes GST can replace a separate GST amount only when the GST is exactly one-eleventh of the total price. Recipient-created invoices have additional requirements, including recipient identity or ABN below $1,000. GST group and branch rules and the provisions for missing information or Commissioner acceptance can modify the ordinary requirements. [GST Act s 29-70](https://www.legislation.gov.au/C2004A00446/2026-01-01/2026-01-01/text/original/epub/OEBPS/document_1/document_1.html); [ATO tax invoices](https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/tax-invoices).

- **No ABN withholding** -- Where required, withhold 47% and report at W4, subject to the entity’s withholding reporting class. Apply exceptions, including payments of $75 or less excluding GST and valid supplier statements where relevant.  _(([ATO PAYG withholding](https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/business-activity-statements-bas/pay-as-you-go-payg-withholding)))_

#### 5.8 Adjustments (Divisions 19, 21 and 129)

An adjustment follows a change to a correctly reported supply/acquisition. Original errors use correction rules: see au-bas-preparation.md Section 7 for credit/debit error time/value limits and when revision is required.

| Direction | Net GST | Label |
| --- | --- | --- |
| Increasing | More sales GST or less purchase credit | 1A for supply; 1B for reduced credit |
| Decreasing | Less sales GST or more purchase credit | 1A for supply; 1B for increased credit |

| Event | Division | Treatment |
| --- | --- | --- |
| Later price change, cancellation or returned goods | Div 19 | Adjustment in the period the adjustment event is accounted for |
| Bad debt written off or overdue 12 months or more | Div 21 | Non-cash supplier: decreasing adjustment; unpaid recipient who claimed credit: matching increasing adjustment |
| Bad debt recovered | Div 21 | Reverse the earlier adjustment to the extent recovered |
| Creditable-purpose change | Div 129 | Compare planned/actual use over prescribed adjustment periods; value determines their number and thresholds may remove adjustment |
| Goods applied solely to private/domestic use | Div 130 | Increasing adjustment |
| Deregistration with assets on hand | Div 138 | Increasing adjustment |
| Registration with earlier-acquired assets on hand | Div 129 | May give a decreasing adjustment |

**Adjustment notes:** a decreasing adjustment from an event on a supply generally requires the supplier's adjustment note, subject to the minor-adjustment exemption and Commissioner's determinations. [GST Act ss 29-20, 29-75](https://www.ato.gov.au/law/view/document?docid=PAC/19990055/29-75).

**Attribution:** use the period the entity becomes aware of the adjustment event, rather than reopening the original supply period. An unpaid supplier debt over 12 months may require the recipient to repay GST through an increasing adjustment. Div 129 use changes, such as a development intended for sale being rented, are fact-sensitive: escalate rather than estimate.

These are separate from adjustments:

- Original reporting errors.
- Missing-invoice deferral: s 29-10(3) attributes the credit to the first period, if any, for which a GST return is given whilst holding the invoice. Check low-value/other statutory exceptions.
- Election under ss 29-10(4)-(6): move only the entitled credit omitted from the otherwise attributable period's net amount assessment to a specified later period. On a current ordinary BAS, include it at 1B; no separate notification is needed. Record the choice; it cannot be revoked or amended. Keep acquisition and choice records for at least 5 years after lodging that BAS, longer if required. Earlier claims have transitional rules from 1 January 2026. [GST Act s 29-10](https://www.legislation.gov.au/C2026C00081); [ATO procedure](https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/claiming-gst-credits/when-you-can-claim-a-gst-credit); [TAA Sch 1 s 382-5](https://www.legislation.gov.au/C2026C00468); [2025 amending Act, Sch 4 items 36-37 and 43](https://www.legislation.gov.au/C2025A00072).
- Law/rate changes: apply the rule for the transaction and period.

For either credit path, the ordinary 4-year limit runs from the return due date for the period under s 29-10(1) or (2); check s 93-10 exceptions. [GST Act Division 93](https://www.legislation.gov.au/C2026C00081).

### Comparison with EU VAT (for practitioners familiar with EU systems)

| Feature | Australian GST | EU VAT |
| --- | --- | --- |
| Number of rates | 1 (10%) | 2-4 per member state |
| Reverse charge trigger (B2B cross-border) | Apply the Division 83 or 84 conditions in Section 5.5; fully creditable use is not a blanket exemption | ALWAYS (Art. 196) |
| Intra-community regime | N/A | Zero-rated supply + acquisition |
| Entertainment credit | Follows FBT (credit if FBT paid) | Typically blocked outright |
| Motor vehicle credit | Allowed, capped at car limit | Often blocked (e.g. Malta 10th Schedule) |
| Financial supply credits | RITC at 75%/55% for certain services | No equivalent |

## Deadlines and filing

### Sheet "Transactions"

| Column | Content |
| --- | --- |
| A-D | Date, counterparty, bank direction and description |
| E | Signed AUD bank amount, unchanged for reconciliation |
| F | Net accounting amount from the invoice and verified GST |
| G | Sale liability or verified ordinary-purchase credit, signed for supported reversals. For a wholly taxable GST-inclusive amount without a special credit limit, G = M * ABS(E)/11, multiplied by creditable use for a purchase. For mixed/specially valued supplies use actual invoice GST, reporting sign and creditable proportion. GST-free/input-taxed supplies, unsupported credits and RC rows give zero; note pending credits separately. |
| H | One primary category: G1 taxable sale; G2 eligible GST-free exports reportable at G2; G3 other GST-free sales, including ordinary exported services; G4 input taxed sale; G10 capital purchase; G11 non-capital purchase; RC reverse-charge schedule; EXCLUDED. Split evidenced mixed components without duplicating the bank amount; follow export allocation below. |
| I-L | Provisional flag, question, exclusion reason and notes/evidence |
| M | 1 for ordinary sales/purchases; -1 for a supported refund/reversal. Establish the transaction, not bank direction alone. |
| N | For an ordinary row whose full bank amount is supported attributable consideration: (ABS(E) - O) * M. Purchases report positively despite a bank debit; sales have O = 0. RC gives zero here. Export reporting-only components and capital vehicles use their allocations below. Apply insurer/CTP and import gates first. |
| O | Supported stamp duty excluded from G10/G11 for this payment/full reversal. Use zero only with evidence of no duty. Require a finite non-negative amount <= ABS(E), tied to the attributable payment and invoice/notice; never subtract a whole invoice's duty from a partial payment. Unresolved component/attribution: Needs Input. Keep E and accounting expense intact; O does not determine G credit. |

N is neither an accrual ledger nor a valuation method. Establish supported periods/amounts for unpaid/accrual transactions, partial payments/refunds, currency differences and other special cases before completing BAS. Report insurance premiums less stamp duty; capital purchase duty is also excluded from G10. [ATO purchases instructions](https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/completing-your-bas-for-gst/complete-your-bas/step-3-purchases).

G13/G14/G15 describe calculation-worksheet exclusions, not replacements for H = G10/G11. Keep exclusion/creditability evidence in I-L and signed E separate from reporting amounts.

### Insurer and CTP settlement acquisitions

Do not report at G10 a capital acquisition constituted by an insurer settling an insurance-policy claim, or by a compulsory third-party scheme operator settling a scheme claim if you are not an operator. Its G10 contribution is zero: keep it out of ordinary G10/G11 rows and do not derive N from a related bank movement. Record the precise exclusion/evidence in I-L; retain the bank movement and supported accounting treatment separately.

This excludes neither all insurer money nor all cash proceeds, excesses or separately contracted repairs. Obtain the policy, settlement terms, invoices and parties' roles. Resolve any supply, credit or adjustment separately: the G10 exclusion establishes neither credit entitlement nor its absence. Unresolved characterisation/credit: Needs Input, BAS provisional. Operator treatment is outside this rule. [ATO Step 3: Purchases, G10 exclusions](https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/completing-your-bas-for-gst/complete-your-bas/step-3-purchases).

### Goods import reporting

Apply business/private-use, special-case and refusal rules first. Route imported goods away from ordinary bank-linked G/N calculations. Establish importer, capital/non-capital classification, taxable/non-taxable status, customs entry, included components, period and separate credit evidence. Supplier, customs and broker debits alone do not establish reporting; avoid counting them as duplicate purchases.

[ATO Step 3: Purchases, importations](https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/completing-your-bas-for-gst/complete-your-bas/step-3-purchases) distinguishes:

- Non-taxable imports: amounts paid/payable for goods, international transport to their Australian place of consignment and transport insurance.
- Taxable imports: specified customs value, transport/insurance, customs duty, wine tax and import GST, without duplicating included costs; alternatively, the permitted import GST x 11 route. Apply special rules, including any car limit.
- Additional import GST: x 11 at the applicable G10/G11, including additional deferred GST.

This worksheet has no import schedule. Return Needs Input until a linked import workpaper supports amount, period and credit. Keep unsupported credits pending, without inferring a credit or zero entitlement from a debit. A supplier invoice alone does not establish import credit. Retain original bank amounts and report each supported amount once.

### Motor vehicle purchase reporting

This path covers ordinary fully paid Australian taxable capital vehicle purchases. Establish GST-inclusive cost after excluded duty, year, supported business use and car-limit applicability. Bank debit alone does not establish G10. Business use differs from creditable use: determine credit separately under entitlement, invoice and car-credit rules. Credit unavailability alone does not reduce G10.

Let P = supported cost after excluded duty, B = business-use proportion from zero to one, C = applicable car limit. With H = G10, use N = M * min(P, C) * B where the ordinary reporting limit applies; otherwise, for a verified uncapped ordinary capital vehicle, N = M * P * B. Override bank-linked N and do not deduct duty/private use again. Record cost, year, use evidence and reporting basis in I-L. Keep E unchanged; derive F from supported accounting treatment and verified G credit. The reporting limit creates no second accounting entry or bank movement.

For an ordinary capped car in 2026-27, C = $69,883; the credit ceiling is $6,353 before creditable-use reductions, subject to s 69-10 and exceptions. Invoice/full business use alone does not establish credit. A verified complete reversal uses M = -1 and reverses the same supported allocation and required credit once. Wholly private purchases give no G10 or verified business credit.

Needs Input until reporting amount, attribution and credit are supported for statutory exceptions, trading stock, leases, hire purchase, imports, trade-ins, finance, part payments/refunds, changed use, special valuations or unresolved price components; do not force them into this formula. [ATO purchasing a motor vehicle, updated 3 June 2026](https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/in-detail/your-industry/motor-vehicle-and-transport/gst-and-motor-vehicles/purchasing-a-motor-vehicle); GST Act ss 11-5, 11-15 and 69-10.

### Export reporting allocation

First establish that the supply is GST-free under the applicable law, including all relevant conditions and exclusions. A foreign customer, offshore address or invoice description alone does not establish that treatment. This reporting path does not decide eligibility under sections 38-185 or 38-190. If eligibility, attribution or the reporting amount is unresolved, return Needs Input.

For Full BAS, ordinary GST-free exported consulting services belong at G3, not G2. G2 includes qualifying exported goods at their free-on-board value and the specified services involving repair, renovation, modification or treatment of goods from overseas whose destination is outside Australia. International transport and export freight/insurance are excluded from G2; report applicable GST-free amounts at G3. All amounts at G2 and G3 also contribute once to G1. Simpler BAS uses the same G1 total without lodging G2 or G3.

For ordinary fully settled GST-free exported goods with supported freight/insurance, retain parent E and accounting F, with H = EXCLUDED and G = N = 0. Explain that linked components supply the reporting, not that the sale is excluded from G1. Link receipt, invoice, free-on-board valuation and allocation evidence in I-L. Component rows have E = F = G = 0, one H category and N = supported amount x M, not ABS(E). Assign free-on-board value to G2 and related GST-free freight/insurance to G3; reconcile component N to ABS(parent E) x M. Create no duplicate accounting entries. Full supported reversals use M = -1 and negative component N, retaining actual signed bank movement. Partial receipts, valuation/currency differences, mixed treatment or unallocated charges need supported attribution/allocation; return Needs Input rather than force bank value into G2.

This synthetic case stipulates a fully settled $1,200 GST-free sale with documented $1,000 free-on-board value and $200 related GST-free freight/insurance. The accounting amounts are stipulated solely to demonstrate no duplication.

| Row | E | F | G | H | M | N |
| --- | --- | --- | --- | --- | --- | --- |
| BANK-EXPORT | 1200 | 1200 | 0 | EXCLUDED | 1 | 0 |
| BANK-EXPORT:FOB | 0 | 0 | 0 | G2 | 1 | 1000 |
| BANK-EXPORT:freight-insurance | 0 | 0 | 0 | G3 | 1 | 200 |

The exact-category summary gives G1 $1,200, G2 $1,000, G3 $200 and 1A $0; bank E and accounting F each total $1,200. [ATO Step 1: Sales](https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/completing-your-bas-for-gst/complete-your-bas/step-1-sales), current public page updated 9 September 2026, read 11 November 2026 UTC. The ordinary cash-linked allocation above does not authorise special valuations or establish export eligibility.

### Separate reverse-charge schedule

For each confirmed ordinary service under section 5.5, link one RC row to its invoice and record period, price paid/payable, 1A liability, supported 1B credit and price x 1.1 reporting amount. Report the latter once at G1 and once at G10 or G11. Linked transaction G = N = 0; keep bank E unchanged. Record the accounting journal, including non-creditable GST, separately: grossed-up reporting is neither another bank movement nor sales revenue. Unresolved liability, attribution or use: Needs Input, not ready to lodge. Refer section 5.5 special cases.

### Sheet "BAS Summary" (Full BAS)

| Label | Formula / rule |
| --- | --- |
| G1 | Sum N for H equal to G1, G2, G3 or G4, plus the reverse-charge schedule reporting amounts; exclude loans, transfers and other EXCLUDED credits |
| G2, G3 | Sum N for the corresponding H category |
| G10, G11 | Sum N for the corresponding purchase category, including purchases without credits where required, plus the schedule amount assigned to that label |
| 1A | Sum G for sales categories, plus schedule liability and supported GST adjustments |
| 1B | Sum G for G10 and G11, plus schedule credit and supported credit adjustments |
| Net GST | 1A - 1B |

Use GST-inclusive amounts. Ordinary G10 = SUMIFS(Transactions!N:N,Transactions!H:H,"G10") plus its schedule amount. Use named cells and the table's categories for G1 and 1B; never subtract non-creditable purchases again from verified credits. G4-G9 and G12-G19 are calculation-worksheet items, not all lodged BAS labels.

### Sheet "Simpler BAS"

For eligible businesses with GST turnover below $10 million, report G1, 1A and 1B using the same definitions and formulas; complete any other tax obligations on the issued statement. Confirm the G1 GST-inclusive indicator.

### Worksheet checks

- A taxable sale of $1,100 gives G1 $1,100 and 1A $100.
- A wholly creditable taxable purchase of $110 gives 1B $10 even though the bank amount is -$110. Together with the sale, net GST is $90.
- A $110 purchase with 50% creditable use gives a $5 credit if all other requirements are met. Do not exclude its private portion twice.
- A $1,000 loan deposit contributes zero to G1 and 1A. A supported $110 sales refund reduces reported sales by $110 and output GST by $10.
- A confirmed ordinary reverse-charge purchase priced at $1,000 with 60% creditable use gives schedule G1 $1,100, G11 $1,100, 1A $100, 1B $60 and net GST $40. Its transaction row retains bank E = -$1,000 with G = N = 0.
- GST-free purchases contribute no GST credit; unsupported acquisitions remain pending until entitlement and evidence are established.

[ATO reverse-charge reporting](https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/in-detail/rules-for-specific-transactions/international-transactions/reverse-charge-gst-on-offshore-goods-and-services-purchases); [ATO GST reporting](https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/business-activity-statements-bas/goods-and-services-tax-gst); GST Act ss 9-70, 11-20 and 29-10.

### Color and formatting conventions

Blue font for hardcoded values from the bank statement (column E of Transactions). Black for formulas. Green for cross-sheet references. Yellow background for any row where Default? = "Y".

### Filing deadlines (quarterly)

| Quarter | Period | Due date |
| --- | --- | --- |
| Q1 | 1 July -- 30 September | 28 October |
| Q2 | 1 October -- 31 December | 28 February |
| Q3 | 1 January -- 31 March | 28 April |
| Q4 | 1 April -- 30 June | 28 July |

- **Other deadline notes** -- Monthly GST is generally due on the 21st of the next month. Annual GST is generally due with the income-tax return, or 28 February after the year where no return is required. Check the actual statement, extensions and next-business-day rule.  _([ATO annual GST](https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/lodging-your-bas-or-annual-gst-return))_

## Penalties and interest

### Penalties

- **Failure to lodge (FTL)** -- The base penalty is one unit per 28-day period or part, capped at five units. Apply the relevant entity multipliers, dates and remission rules. The penalty unit is $364 from 1 July 2026.  _([Crimes (Amount of a Penalty Unit) Instrument 2026](https://www.legislation.gov.au/F2026N00424/asmade/text))_
- **General Interest Charge (GIC)** -- Use the published quarterly ATO rate and applicable daily compounding. GIC and SIC incurred on or after 1 July 2025 are not deductible; preserve the earlier rule only for earlier-incurred interest.  _([ATO interest](https://www.ato.gov.au/individuals-and-families/income-deductions-offsets-and-records/deductions-you-can-claim/cost-of-managing-tax-affairs/interest-charged-by-the-ato))_
- **Shortfall penalties** -- Base rates can be 25%, 50% or 75% according to the conduct. A qualifying pre-notification voluntary disclosure generally reduces the penalty by 80% where the shortfall is at least $1,000 and 100% below that amount. The qualifying post-notification reduction is 20%. Apply the statutory conditions and any other adjustments.  _([TAA Schedule 1 s 284-225](https://www.ato.gov.au/law/view/document?docid=PAC/19530001/SCH1-284-225))_

## Cross-border points

### 3.7 SaaS (verify the invoice and applicable GST route)

| Pattern | Billing entity | Treatment | Notes |
| --- | --- | --- | --- |
| GOOGLE (Ads, Workspace, Cloud) | Google Asia Pacific Pte Ltd (SG) or Google LLC (US) | Verify the contracting entity and supply | Check whether GST is lawfully charged and the acquisition is creditable. If no GST is charged, assess the applicable reverse charge conditions in Section 5.5; neither the supplier name nor fully creditable use alone decides liability. |
| MICROSOFT (365, Azure) | Microsoft Ireland Operations Ltd (IE) or Microsoft Regional Sales Pte Ltd (SG) | Non-resident supply | Same logic. Check invoice for ABN and GST charge. |
| ADOBE | Adobe Systems Software Ireland Ltd (IE) | Non-resident supply | Check invoice |
| META, FACEBOOK ADS | Meta Platforms Ireland Ltd (IE) | Non-resident supply | Check invoice for AU GST |
| SLACK, SALESFORCE | Slack Technologies / Salesforce (US or IE entity) | Non-resident supply | Check invoice |
| ATLASSIAN | Atlassian Pty Ltd (AU) | Domestic 10% | Atlassian is Australian -- domestic taxable supply, full credit |
| CANVA | Canva Pty Ltd (AU) | Domestic 10% | Australian entity -- domestic taxable supply |
| XERO | Xero Limited (NZ) or Xero Australia Pty Ltd | Check invoice | If AU entity: domestic 10%. If NZ entity: non-resident supply. |
| ZOOM | Zoom Video Communications (US) | Non-resident supply | Check invoice for AU GST registration |
| DROPBOX | Dropbox (IE or US) | Non-resident supply | Check invoice |
| AWS, AMAZON WEB SERVICES | Amazon Web Services Inc (US) or AWS Australia Pty Ltd | Check invoice | If AU entity: domestic 10%. If US entity: non-resident. |

- **Non-resident digital supplies note** -- Check the actual invoice, contracting entity, connection rules, recipient GST registration and enterprise use. An ABN alone does not establish that the recipient is outside the Australian-consumer definition. An invoice without GST does not itself establish a reverse charge liability or exemption. Apply Section 5.5 and [GST Act ss 9-25(7), 84-5 and 84-100](https://www.legislation.gov.au/C2004A00446/2026-01-01/2026-01-01/text/original/epub/OEBPS/document_1/document_1.html).

### 5.5 Reverse charge (Division 84)

An offshore/unknown supplier alone establishes no liability. For intangible supplies under s 84-5(1) items 1/2, subsection (1A) requires acquisition for an Australian enterprise and not solely for a creditable purpose. Item 3 instead has its own connection/supplier-belief conditions: check ABN/other identifier and registration declaration, ss 84-5(1B) and 84-100. Its purpose test is not subsection (1A), so fully creditable use is no blanket exemption. Section 84-10 makes the recipient liable where s 84-5 applies. Div 83's agreed reverse charge for certain connected non-resident supplies is separate. Determine liability and credit separately. [GST Act ss 83-5, 84-5, 84-10 and 84-100](https://www.legislation.gov.au/C2004A00446/2026-01-01/2026-01-01/text/original/epub/OEBPS/document_1/document_1.html).

**Ordinary services:** for a fully taxable unrelated-party service with all consideration paid/payable by the recipient, s 84-12 liability is price x 10%, not payment / 11. Determine credit separately under ss 11-5, 11-15 and 84-13 using supported creditable extent. The ATO-described reverse-charge credit needs no tax invoice, but retain supply, amount, liability, use and attribution evidence. This exception does not cover ordinary supplier-charged GST.

**BAS:** under the accounts method, include liability at 1A and entitled credit at 1B; ordinary price x 1.1 goes to G1 and, where required, G10/G11. Use the separate schedule under Deadlines and filing, retaining the bank amount and counting purchase/credit once. The G1 reporting entry is not sales revenue. [ATO reverse-charge reporting](https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/in-detail/rules-for-specific-transactions/international-transactions/reverse-charge-gst-on-offshore-goods-and-services-purchases); GST Act ss 84-12 and 84-13.

**Refer special cases:** associates/valuation, non-monetary consideration, GST-free components, branch transfers, annual apportionment, low value goods and Div 83 agreements need qualified review; the ordinary schedule does not resolve them. Apply relevant financial-supply/other refusal triggers.

**Offshore digital supplies:** s 9-25(5)(d) connects relevant supplies to Australian consumers; the usual registration threshold is at least $75,000 GST turnover. An ABN alone does not exclude Australian-consumer status: the recipient must be GST-registered and acquire wholly/partly for an enterprise. Check supplier evidence/reasonable-belief rules, including ABN/registration declaration where applicable, other connection rules and Div 84, particularly if not fully creditable. [GSTR 2017/1](https://www.ato.gov.au/law/view/document?docid=GST/GSTR20171/NAT/ATO/00001); GST Act ss 9-25(7) and 84-100.

## Two worked examples that recompute

### Section 4 -- Worked examples

These are six fully worked classifications drawn from a hypothetical CBA NetBank bank statement of an Australian self-employed IT consultant based in Sydney. They illustrate the trickiest cases. Pattern-match against these when you encounter similar lines in any real statement.

#### Example 1 -- Non-resident SaaS with no applicable reverse charge

**Input line:**
`05.04.2026 ; GOOGLE ASIA PACIFIC PTE LTD ; DEBIT ; Google Workspace Business ; AUD 21.60`

**Reasoning:**
For this hypothetical example, assume the invoice and supply evidence establish a non-resident contracting entity, a supply not connected with Australia and a wholly creditable business acquisition. Assume no Division 83 agreement applies. On those facts, item 1 of s 84-5(1) fails the purpose test and items 2 and 3 do not apply because their connection conditions are absent. No reverse charge applies to this example; treat it as a purchase with no GST in the price. A bank-statement name and fully creditable use alone would not establish that result. [GST Act ss 83-5 and 84-5](https://www.legislation.gov.au/C2004A00446/2026-01-01/2026-01-01/text/original/epub/OEBPS/document_1/document_1.html).

**Example 1 output**

| Date | Counterparty | Gross | Net | GST | Rate | BAS Label | Default? | Question? | Excluded? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 05.04.2026 | GOOGLE ASIA PACIFIC | -21.60 | 21.60 | 0 | N/A | G11 | N | -- | -- |

#### Example 2 -- Local utility, standard 10%

**Input line:**
`10.04.2026 ; TELSTRA CORP LTD ; DEBIT ; Monthly plan Apr 2026 ; AUD 99.00`

**Reasoning:**
For this example, a valid tax invoice confirms $9 GST in the $99 charge and the evidence establishes wholly creditable business use. Net expense is $90 and the positive credit is $9. If use is mixed, apportion the credit. Without the required invoice, keep it pending.

**Example 2 output**

| Date | Counterparty | Gross | Net | GST | Rate | BAS Label | Default? | Question? | Excluded? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 10.04.2026 | TELSTRA CORP LTD | -99.00 | 90.00 | 9.00 | 10% | G11 | N | -- | -- |

#### Example 3 -- Supermarket purchase (mixed GST-free and taxable)

**Input line:**
`12.04.2026 ; WOOLWORTHS 1234 SYDNEY ; DEBIT ; Grocery purchase ; AUD 87.50`

**Reasoning:**
Woolworths sells a mix of basic food (GST-free under Division 38-A) and taxable items (prepared food, confectionery, soft drinks, household goods). Without a detailed receipt, the split is unknown. Conservative default: treat entire amount as having no GST credit (safest approach -- underclaims rather than overclaims). Flag as Tier 2 -- ask client for receipt to split GST-free and taxable items. If receipt available, split accordingly.

**Example 3 output**

| Date | Counterparty | Gross | Net | GST | Rate | BAS Label | Default? | Question? | Excluded? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 12.04.2026 | WOOLWORTHS 1234 | -87.50 | 87.50 pending | 0 | -- | G11 | Y | Q1 | "Supermarket: provide receipt to split GST-free food vs taxable items" |

#### Example 4 -- Bank fee (input taxed financial supply)

**Input line:**
`15.04.2026 ; CBA ACCOUNT FEE ; DEBIT ; Monthly account keeping fee ; AUD 10.00`

**Reasoning:**
In this example, the statement and fee terms establish an input-taxed account-keeping service. Record the $10 business purchase at G11 with zero GST credit. Classify other bank services from their actual terms and invoice; the bank name alone does not settle GST.

**Example 4 output**

| Date | Counterparty | Gross | Net | GST | Rate | BAS Label | Default? | Question? | Excluded? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 15.04.2026 | CBA ACCOUNT FEE | -10.00 | 10.00 | 0 | -- | G11 | N | -- | "Input taxed financial supply" |

#### Example 5 -- Export service sale (GST-free)

**Input line:**
`20.04.2026 ; ACME CORP NZ ; CREDIT ; Invoice AU-2026-042 IT consulting April ; AUD 8,500.00`

**Reasoning:**
This reporting example stipulates that qualified review has already established the entire $8,500 consulting supply is GST-free under the applicable section 38-190 rule, including its conditions and exclusions. The NZ customer and bank description alone do not establish eligibility or entitlement to credits on related costs. If eligibility is unresolved, return Needs Input. For this stipulated GST-free ordinary consulting supply, use primary category G3 and zero GST. Full BAS derives G1 $8,500 and G3 $8,500 from that one category; G2 is zero. Simpler BAS includes the sale once in G1. [ATO Step 1: Sales](https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/completing-your-bas-for-gst/complete-your-bas/step-1-sales).

**Example 5 output**

| Date | Counterparty | Gross | Net | GST | Rate | BAS Label | Default? | Question? | Excluded? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20.04.2026 | ACME CORP NZ | +8,500.00 | +8,500.00 | 0 | 0% | G3 | N | -- | "Stipulated eligibility; otherwise Needs Input" |

#### Example 6 -- Merchant transaction fee

Input: `25.04.2026 ; STRIPE PAYMENTS AU ; DEBIT ; Transaction fees April ; AUD 145.20`.

The name does not settle the GST treatment. In this example a valid Australian tax invoice establishes a taxable processing service with $13.20 GST, wholly for creditable business use. The cash debit is $145.20, net expense $132.00 and positive GST credit $13.20. If that evidence is absent, show a pending treatment and no verified credit until resolved. A supply of credit or a different cross-border arrangement may have a different result. [GSTR 2019/2](https://www.ato.gov.au/law/view/document?docid=GST/GSTR20192/NAT/ATO/00001).

**Example 6 output**

| Date | Counterparty | Bank amount | Net expense | GST credit | Label | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| 25.04.2026 | STRIPE PAYMENTS AU | -145.20 | 132.00 | 13.20 | G11 | Valid tax invoice and wholly creditable use |

### GST credit timing examples

A business accounting for GST on a non-cash basis lodges monthly and makes a wholly creditable acquisition for $242 including GST. The supplier issues the tax invoice on 31 August, the business posts it on 1 September and no earlier consideration was provided. If the business holds the valid tax invoice at August lodgment, report $22 in August 1B. Assume no special rule applies.

```oa-check
name: August credit where invoice is held at lodgment
inputs:
  gst_inclusive: 242
  invoice_held_at_august_lodgment: 1
steps:
  - full_credit: gst_inclusive / 11
  - august_credit: full_credit * invoice_held_at_august_lodgment
expected:
  full_credit: 22
  august_credit: 22
```

If the business only obtains the valid tax invoice after lodging August, and September is the first period for which it gives a GST return whilst holding it, August 1B is $0 and September 1B is $22 under s 29-10(3). If it held the invoice at August lodgment but the assessment omitted the credit, check the separate election rules before including the amount in a later period.

```oa-check
name: Credit deferred until the first lodgment holding the invoice
inputs:
  gst_inclusive: 242
  invoice_held_at_august_lodgment: 0
  invoice_held_at_september_lodgment: 1
steps:
  - full_credit: gst_inclusive / 11
  - august_credit: full_credit * invoice_held_at_august_lodgment
  - september_credit: (full_credit - august_credit) * invoice_held_at_september_lodgment
expected:
  august_credit: 0
  september_credit: 22
```

### Export reporting worked checks

These synthetic checks assume GST-free eligibility, attribution, amounts and allocation evidence are already established. They verify the stated reporting arithmetic, not every export rule or an executed workbook.

#### Ordinary consulting export

```oa-check
name: AU ordinary GST-free consulting export uses G3 once in G1
inputs:
  consulting_receipt: 8500
  export_goods_amount: 0
  gst_due: 0
steps:
  - reporting_g3: consulting_receipt
  - reporting_g2: export_goods_amount
  - reporting_g1: reporting_g2 + reporting_g3
  - gst_1a: gst_due
expected:
  reporting_g1: 8500
  reporting_g2: 0
  reporting_g3: 8500
  gst_1a: 0
```

#### Exported goods with related freight and insurance

```oa-check
name: AU supported export components preserve bank and reporting totals
inputs:
  bank_receipt: 1200
  supported_fob: 1000
  supported_freight_insurance: 200
  parent_reporting: 0
  component_bank: 0
steps:
  - reporting_g2: supported_fob
  - reporting_g3: supported_freight_insurance
  - reporting_g1: parent_reporting + reporting_g2 + reporting_g3
  - bank_total: bank_receipt + component_bank
  - reconciliation: bank_total - reporting_g1
expected:
  reporting_g1: 1200
  reporting_g2: 1000
  reporting_g3: 200
  bank_total: 1200
  reconciliation: 0
```

#### Supported full export reversal

```oa-check
name: AU supported full export reversal preserves component signs
inputs:
  bank_refund: -1200
  supported_fob: 1000
  supported_freight_insurance: 200
  reporting_sign: -1
steps:
  - reporting_g2: supported_fob * reporting_sign
  - reporting_g3: supported_freight_insurance * reporting_sign
  - reporting_g1: reporting_g2 + reporting_g3
  - reconciliation: bank_refund - reporting_g1
expected:
  reporting_g1: -1200
  reporting_g2: -1000
  reporting_g3: -200
  reconciliation: 0
```

### Reverse-charge worked checks

These synthetic cases assume the stated liability, attribution and use facts have been established. They check arithmetic and reporting only and do not override the refusal catalogue or resolve missing facts.

#### Case 1: fully creditable offshore service

Apply the stipulated supply and use facts from retained Example 1 to a separate $21.60 service purchased in this case's 2026-27 period. The service is not connected with Australia, the acquisition is wholly creditable and no other reverse-charge route applies. Item 1's purpose test is not met. No supplier GST is payable or charged, so the input tax credit is also zero. The ordinary non-capital purchase is $21.60 at G11; there is no reverse-charge addition to G1.

```oa-check
name: AU fully creditable offshore service has no reverse charge
inputs:
  service_price: 21.60
  gst_payable_under_stipulated_facts: 0
steps:
  - purchase_g11: service_price
  - gst_1a: gst_payable_under_stipulated_facts
  - gst_1b: gst_payable_under_stipulated_facts
  - net_gst: gst_1a - gst_1b
expected:
  purchase_g11: 21.60
  gst_1a: 0
  gst_1b: 0
  net_gst: 0
```

#### Case 2: offshore service with 60% creditable use

An unrelated non-resident supplies an ordinary service for $1,000. It is not connected with Australia under sections 9-25 and 9-26 and no supplier GST is payable or charged. The registered recipient acquires it 60% for its Australian taxable enterprise activities and 40% privately, supported by a documented use allocation. Section 84-5 item 1 applies to the whole taxable service price. Recipient GST is $100; the section 84-13 credit is $60 and net GST is $40. The separate schedule contributes $1,100 to each of G1 and G11. The linked bank debit stays -$1,000 and its ordinary G and N fields are zero. A tax invoice is not required for this reverse-charge credit; the other evidence and attribution conditions remain necessary.

```oa-check
name: AU ordinary offshore reverse charge preserves liability credit and reporting
inputs:
  service_price: 1000
  creditable_percent: 60
  reverse_charge_percent: 10
steps:
  - gst_1a: pct(service_price, reverse_charge_percent)
  - gst_1b: pct(gst_1a, creditable_percent)
  - reporting_g1: service_price + gst_1a
  - purchase_g11: reporting_g1
  - net_gst: gst_1a - gst_1b
  - signed_bank_amount: 0 - service_price
expected:
  gst_1a: 100
  gst_1b: 60
  reporting_g1: 1100
  purchase_g11: 1100
  net_gst: 40
  signed_bank_amount: -1000
```

#### Case 3: supplier-charged GST with partial credit

The invoice and supply evidence establish an ordinary Australian taxable software supply for $1,100 including $100 GST. The registered recipient holds the required valid tax invoice and has supported 60% creditable use and 40% private use. No reverse charge applies. Ordinary G11 is $1,100, the purchase credit is $60 and the purchase creates no recipient liability at 1A or addition to G1. The result follows from these facts, not the software brand or the supplier's ABN alone.

```oa-check
name: AU supplier GST does not imply full input tax credit
inputs:
  invoice_including_gst: 1100
  creditable_percent: 60
steps:
  - invoice_gst: invoice_including_gst / 11
  - gst_1b: pct(invoice_gst, creditable_percent)
  - non_creditable_gst: invoice_gst - gst_1b
  - purchase_g11: invoice_including_gst
expected:
  invoice_gst: 100
  gst_1b: 60
  non_creditable_gst: 40
  purchase_g11: 1100
```

#### Case 4: private purchase with consumer-status misrepresentation

A GST-registered Australian resident makes a wholly private $100 offshore service purchase. The supply is connected solely under section 9-25(5)(d). The recipient discloses an ABN and declares GST registration; the supplier satisfies section 84-100 and treats the recipient as not an Australian consumer. All item 3 conditions are stipulated and the service is neither GST-free nor input taxed. Section 84-5 item 3 applies despite the absence of enterprise use. Recipient GST is $10 and there is no credit. The schedule supplies G1 and G11 of $110 each; the private payment remains separately identified for accounting. Do not apply the items 1 and 2 purpose test to remove this liability.

```oa-check
name: AU consumer status misrepresentation has no private use credit
inputs:
  service_price: 100
  reverse_charge_percent: 10
  creditable_percent: 0
steps:
  - gst_1a: pct(service_price, reverse_charge_percent)
  - gst_1b: pct(gst_1a, creditable_percent)
  - reporting_g1: service_price + gst_1a
  - purchase_g11: reporting_g1
  - net_gst: gst_1a - gst_1b
expected:
  gst_1a: 10
  gst_1b: 0
  reporting_g1: 110
  purchase_g11: 110
  net_gst: 10
```

**Unresolved-fact boundary.** A bank description such as GOOGLE, ATLASSIAN or XERO without the invoice, connection or use facts returns Needs Input. Retain the payment in the reconciliation, list the missing evidence and withhold unsupported credit. Do not supply a final tax classification or assume a recipient liability from the name. This is a prose decision boundary, not an executable eligibility test.

### Purchase reporting worked checks

#### Confirmed business account service

The fee terms establish an input taxed business account service, fully paid and attributable in the period. Full BAS applies. Retain bank E = -$10, accounting F = $10 and G = 0; H = G11, M = 1, O = 0 and N = $10. No recipient reverse charge or other adjustment applies.

```oa-check
name: AU input taxed account service reports purchase without credit
inputs:
  account_fee: 10
  verified_credit: 0
steps:
  - signed_bank_amount: 0 - account_fee
  - accounting_expense: account_fee - verified_credit
  - purchase_g11: account_fee
  - gst_1b: verified_credit
expected:
  signed_bank_amount: -10
  accounting_expense: 10
  purchase_g11: 10
  gst_1b: 0
```

#### Insurance premium with supported stamp duty and full reversal

A wholly business general insurance purchase is fully paid and attributable in the period. The valid invoice identifies a $110 GST-inclusive taxable premium, $20 stamp duty and exactly $10 GST, all creditable. Bank E is -$130, accounting F is $120, G is $10, H is G11, M is 1, O is $20 and N is $110. Keep the duty in the accounting expense while excluding it from purchase reporting. A separately supported full refund with the same allocation and a required credit reversal uses E = $130, F = -$120, G = -$10, M = -1, O = $20 and N = -$110. These are stipulated complete transactions; partial payments, part refunds or changed use require their own supported attribution and adjustment analysis.

```oa-check
name: AU insurance stamp duty stays out of purchase reporting and reverses once
inputs:
  bank_payment: 130
  supported_stamp_duty: 20
  invoice_gst: 10
steps:
  - purchase_g11: bank_payment - supported_stamp_duty
  - gst_1b: invoice_gst
  - accounting_expense: bank_payment - gst_1b
  - reconciled_bank_payment: accounting_expense + gst_1b
  - refund_g11: 0 - purchase_g11
  - refund_1b: 0 - gst_1b
  - refund_expense: 0 - accounting_expense
  - reconciled_refund: 0 - refund_expense - refund_1b
expected:
  purchase_g11: 110
  gst_1b: 10
  accounting_expense: 120
  reconciled_bank_payment: 130
  refund_g11: -110
  refund_1b: -10
  refund_expense: -120
  reconciled_refund: 130
```

#### Motor vehicle below the limit with partial business use

A registered business fully pays $22,000 for an ordinary Australian taxable capital vehicle in 2026-27. The valid invoice identifies $2,000 GST, no stamp duty or other price component. Supported use is 60% for taxable business activities and 40% privately; all remaining credit requirements are satisfied. The car reporting limit does not reduce this price. G10 is $13,200 and the verified 1B credit is $1,200. Retain E = -$22,000. The aggregate accounting amount after the credit is $20,800; an actual journal must separately apply the supported asset/private treatment. The $8,800 omitted from G10 is a private reporting allocation, not another bank entry.

```oa-check
name: AU capital vehicle G10 follows supported business use
inputs:
  vehicle_cost: 22000
  invoice_gst: 2000
  business_percent: 60
  creditable_percent: 60
steps:
  - purchase_g10: pct(vehicle_cost, business_percent)
  - gst_1b: pct(invoice_gst, creditable_percent)
  - private_reporting_allocation: vehicle_cost - purchase_g10
  - aggregate_accounting_amount: vehicle_cost - gst_1b
  - reconciled_bank_payment: aggregate_accounting_amount + gst_1b
expected:
  purchase_g10: 13200
  gst_1b: 1200
  private_reporting_allocation: 8800
  aggregate_accounting_amount: 20800
  reconciled_bank_payment: 22000
```

#### Ordinary car above the limit and supported full reversal

In 2026-27 a registered business fully pays $77,000 for an ordinary Australian taxable capital car subject to the reporting and credit limits, with no statutory exception, stamp duty, LCT, finance or trade-in. Its valid invoice identifies $7,000 GST. Supported use is 60% for taxable business activities and 40% privately; all other credit requirements are satisfied. G10 is 60% of $69,883, or $41,929.80. The credit is 60% of $6,353, or $3,811.80, rather than 60% of the invoice GST. Retain the $77,000 bank payment. The aggregate accounting amount after this verified credit is $73,188.20, subject to the actual asset/private journal. A separately supported full refund with the same allocation and a required complete credit reversal gives G10 -$41,929.80 and 1B -$3,811.80. These facts do not establish any partial-refund or changed-use adjustment.

```oa-check
name: AU capped car G10 and credit preserve business use and full reversal
inputs:
  vehicle_cost: 77000
  invoice_gst: 7000
  car_limit: 69883
  business_percent: 60
  creditable_percent: 60
steps:
  - capped_reporting_cost: min(vehicle_cost, car_limit)
  - purchase_g10: pct(capped_reporting_cost, business_percent)
  - credit_ceiling: car_limit / 11
  - supported_gst_before_use: min(invoice_gst, credit_ceiling)
  - gst_1b: pct(supported_gst_before_use, creditable_percent)
  - aggregate_accounting_amount: vehicle_cost - gst_1b
  - reconciled_bank_payment: aggregate_accounting_amount + gst_1b
  - refund_g10: 0 - purchase_g10
  - refund_1b: 0 - gst_1b
expected:
  capped_reporting_cost: 69883
  purchase_g10: 41929.80
  credit_ceiling: 6353
  supported_gst_before_use: 6353
  gst_1b: 3811.80
  aggregate_accounting_amount: 73188.20
  reconciled_bank_payment: 77000
  refund_g10: -41929.80
  refund_1b: -3811.80
```

## Ask the client first

### Section 6 -- Tier 2 catalogue

#### 6.1 Vehicle costs

BP, Shell, Caltex, Ampol, 7-Eleven fuel and Viva Energy identify possible fuel costs, not business use. Australia does not categorically block car GST credits; exclude private use. Default: 0% credit. Ask: "Is this fuel for a business vehicle? What percentage is business use vs private? Do you keep a logbook?"

#### 6.2 Home office

Origin Energy, AGL or Telstra at a residential address and home internet need business/private apportionment. Income tax allows actual costs or the fixed rate (70 cents/hour from 2024-25 under PCG 2023/1; 67c for 2022-23 and 2023-24). For GST, actual costs require splitting the taxable portion. Default: 0% credit until use is supported. Ask: "Do you work from home? How many hours per week? Is this a dedicated business line/service or shared personal?"

#### 6.3 Supermarket purchases

Woolworths, Coles, IGA, Aldi and other supermarkets mix GST-free basic food with taxable prepared food, confectionery, soft drinks and non-food items. Total alone cannot establish a split. Default: no verified credit pending evidence; G11 purchase. Ask: "Could you provide the receipt? I need to split GST-free food items from taxable items to claim the correct credit."

#### 6.4 Cash withdrawals

ATM, cash withdrawal, CBA cash or Westpac cash does not establish use. Default: exclude as owner drawing. Ask: "What was the cash used for? If business expenses, do you have receipts?"

#### 6.5 Insurance

Identify policy and invoice components; use actual GST, not stamp duty/other amounts in a general-insurance premium. Life insurance is generally input taxed; private health insurance generally GST-free. No verified credit pending identification. GST Act ss 38-55 and 40-5.

#### 6.6 Mixed subscriptions

Netflix, Spotify, Apple, Amazon Prime and gym names establish neither supply, use nor entitlement. Obtain invoice, connection facts and supported creditable use. Private use gives no credit; entertainment restrictions may apply. Keep unresolved subscriptions pending. Apply section 5.5 before excluding offshore private purchases: recipient liability can arise without a credit. Ask: 'What is the actual supply, who billed it and how is it used? Did you provide an ABN or registration declaration?'

#### 6.7 Short-stay accommodation

For Airbnb/Stayz income, classify residential premises versus commercial residential accommodation from premises and arrangements, not the channel or a three-month threshold. Check registration, taxable turnover and platform fees separately. Ordinary residential letting is generally input taxed. GST Act ss 40-35 and 195-1; GSTR 2012/5.

### Section 9 -- Onboarding fallback (only when inference fails)

Use available evidence first; ask only unanswered questions. Name and transaction patterns are clues, not proof.

| Field | Evidence and fallback |
| --- | --- |
| 9.1 Entity type and trading name | A sole trader's name may match the account holder; company names may end in "Pty Ltd" or "Ltd". Ask: "Are you a sole trader, partnership, company (Pty Ltd), or trust?" |
| 9.2 GST registration | Verify registration and effective date on the ABR, supported by the ATO account. A BAS request does not establish registration; check PAYG activity statements separately. |
| 9.3 ABN | Check bank-statement headers, invoices and descriptions. Ask: "What is your ABN? (11 digits)" |
| 9.4 Reporting period and method | Statement dates suggest a period; confirm it. Ask: "Which BAS period? Q1 (Jul-Sep), Q2 (Oct-Dec), Q3 (Jan-Mar), or Q4 (Apr-Jun)? Monthly or quarterly?" |
| 9.5 Simpler or Full BAS | Below $10M, Simpler BAS is generally the default. Ask: "Are you on Simpler BAS (G1, 1A, 1B only) or do you report full BAS labels?" |
| 9.6 Accounting basis | A bank statement cannot establish the basis. Ask: "Are you on cash basis or accrual basis for GST?" |
| 9.7 Industry | Counterparties and sales descriptions may suggest IT, consulting, trades, retail or hospitality. Ask: "In one sentence, what does the business do?" |
| 9.8 Input taxed supplies | Look for residential rent, lending interest and financial-service revenue. Ask: "Do you earn any income from residential property, financial services, or share trading?" If yes and non-de-minimis, R-AU-1 or R-AU-5 may fire. |
| 9.9 Employees | PAYG withholding, super guarantee and WorkCover payments are clues. Ask: "Do you have employees? If so, how many?" |
| 9.10 Exports | Foreign-currency receipts and overseas names are clues. Ask: "Do you sell goods or services to customers outside Australia?" |

### Validation status

Version 2.6 retains the April 2026 structure. Verification covers only the dated source reads and executable examples described here. Whole-guide currency, accountant approval and deployment are not established.

## Sources

UTC read dates cover only the specified checks, not whole-guide currency, accountant approval or deployment.

| Scoped source read | URL | Read on |
| --- | --- | --- |
| ATO purchases instructions, updated 9 September 2026; read for business purchases at G11, stamp-duty exclusions, the bounded G10 insurer/CTP settlement exclusion and goods-import reporting components | https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/completing-your-bas-for-gst/complete-your-bas/step-3-purchases | 2026-11-11 |
| GST Act s 40-5 and Division 81; read for financial supplies and the distinction between taxes/fees that are not consideration and prescribed exceptions | https://www.legislation.gov.au/C2004A00446/2026-01-01/text | 2026-11-11 |
| GST Regulations rr 40-5.09, 40-5.12, 81-10.01, 81-15.01 and 81-15.02; read for financial/non-financial services, prescribed government fees and overlap priorities | https://www.legislation.gov.au/F2019L00417/2025-11-01/text | 2026-11-11 |
| Current ATO sales reporting instructions; read for G2 exceptions/FOB, ordinary services and related freight/insurance at G3 and inclusion once in G1; eligibility and special valuations not cleared | https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/completing-your-bas-for-gst/complete-your-bas/step-1-sales | 2026-11-11 |
| GST Act ss 9-30, 9-75, 9-85, 27-15, 29-70, 69-10, 84-12/13: reporting currency, periods, invoice information, car-credit conditions and ordinary reverse charge; ss 29-5, 29-10, 29-80, Div 93: non-cash attribution, invoices, elections and time limits; ss 83-5, 84-5, 84-10, 84-100: distinct reverse-charge routes, item-specific purpose and supplier-belief conditions | https://www.legislation.gov.au/C2026C00081 | 2026-11-11; s 29-10 rechecked 2026-11-14 |
| GST Act Division 151 and s 157-5; read for annual-period elections and special cash-basis eligibility | https://www.legislation.gov.au/C2004A00446/2026-01-01/2026-01-01/text/original/epub/OEBPS/document_2/document_2.html | 2026-11-11 |
| GST Regulations rr 23-15.01, 23-15.02 and 29-80.01; read for registration and low-value invoice amounts | https://www.legislation.gov.au/F2019L00417/2025-11-01/2025-11-01/text/original/epub/OEBPS/document_1/document_1.html | 2026-11-11 |
| ITAA 1997 ss 328-110 and 328-115; read for the applicable small-business and aggregated-turnover tests | https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_7/document_7.html | 2026-11-11 |
| ATO annual GST reporting; read for deferred-GST withdrawal, election contact instructions and deadlines | https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/when-and-how-to-report-and-pay-gst/annual-gst-reporting | 2026-11-11 |
| ATO BAS lodgment; read for current online channels and the myGov user types | https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/business-activity-statements-bas/how-to-lodge-your-bas | 2026-11-11 |
| ATO Online services for business help; read for the current public service entry point | https://www.ato.gov.au/online-services/businesses-and-organisations-online-services/logging-in-to-online-services-to-business | 2026-11-11 |
| ATO tax invoices; read for information requirements, total-price boundary and the one-eleventh statement condition | https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/tax-invoices | 2026-11-11 |
| ATO GST reporting methods; read for GST turnover, Simpler BAS and the distinct instalment/full-reporting methods | https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/business-activity-statements-bas/goods-and-services-tax-gst/gst-reporting-methods | 2026-11-11 |
| ATO monthly reporting; read for the monthly threshold, due-date qualifications and reporting methods | https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/when-and-how-to-report-and-pay-gst/monthly-gst-reporting | 2026-11-11 |
| ATO registering for GST; read for taxi/ride-sourcing and general/non-profit registration thresholds | https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/registering-for-gst | 2026-11-11 |
| ATO purchasing a motor vehicle, updated 3 June 2026; read for G10 business-use and ordinary car-limit allocation, current credit ceiling and exceptions | https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/in-detail/your-industry/motor-vehicle-and-transport/gst-and-motor-vehicles/purchasing-a-motor-vehicle | 2026-11-11 |
| ATO assets and exclusions; read for historical car-limit table for 2024-25 and 2025-26 | https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/depreciation-and-capital-expenses-and-allowances/simpler-depreciation-for-small-business/assets-and-exclusions | 2026-11-11 |
| ATO 2026-27 car thresholds; read for car limit and current GST credit ceiling | https://www.ato.gov.au/businesses-and-organisations/small-business-newsroom/car-thresholds-from-1-july | 2026-11-11 |
| ATO LCT rate and thresholds; read for dated fuel-efficient/other-vehicle table | https://www.ato.gov.au/rates/luxury-car-tax-rate-and-thresholds/ | 2026-11-11 |
| ATO no-ABN withholding; read for the $75 excluding-GST payment boundary and exceptions | https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/payg-withholding/payments-you-need-to-withhold-from/withholding-from-suppliers/withholding-if-abn-not-provided | 2026-11-11 |
| ATO How Australian GST works; read for non-resident current/projected turnover, non-profit threshold and platform responsibility | https://www.ato.gov.au/businesses-and-organisations/international-tax-for-business/gst-for-non-resident-businesses/how-australian-gst-works | 2026-11-11 |
| ATO QC17450; read for ordinary reverse-charge BAS reporting and credit-evidence instructions; the page is dated 26 July 2022; Special valuation remains unresolved | https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/in-detail/rules-for-specific-transactions/international-transactions/reverse-charge-gst-on-offshore-goods-and-services-purchases | 2026-11-11 |
| 2025 amending Act, s 2 and Schedule 4 items 36–37 and 43; read for commencement and transition | https://www.legislation.gov.au/C2025A00072 | 2026-11-11 |
| ATO unclaimed credits; read for ordinary later-BAS choices and records | https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/claiming-gst-credits/when-you-can-claim-a-gst-credit | 2026-11-14 |
| ATO approved BAS forms; read for s 29-10(5) references, updated 25 March 2026 | https://www.ato.gov.au/forms-and-instructions/approved-forms-consolidated-list-by-tax-topic/business-activity-statements-bas | 2026-11-14 |
| TAA Sch 1 ss 382-5, 388-50; read for records, retention and combined forms | https://www.legislation.gov.au/C2026C00468 | 2026-11-14 |

Not yet confirmed: the s 29-10(5) approval date and revised-BAS elections, special reverse-charge valuation and the remaining vendor, classification, BAS and actual consumer paths. Dated rows cover only their stated checks.

Undated background references (no read date asserted): Taxation Administration Act 1953 Schedule 1, GST Regulations 2019, LCT Act 1999, WET Act 1999; A New Tax System (Goods and Services Tax) Act 1999 -- [law register](https://www.legislation.gov.au); ATO [BAS instructions](https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/lodging-your-bas), [GST registration](https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/registering-for-gst), [Simpler BAS](https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/lodging-your-bas/simpler-bas) and [food](https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/in-detail/rules-for-specific-transactions/gst-and-food).

### Known gaps

1. The supplier pattern library in Section 3 covers the most common Australian counterparties but does not cover every local SME or regional brand. Add patterns as they emerge.
2. The worked examples are drawn from a hypothetical IT consultant in Sydney. They do not cover hospitality, retail, construction, or agriculture specifically.
3. The GST-free food table covers the most common items but Schedule 1 of the GST Act is detailed -- edge cases (e.g. specific bakery items, health food products) should be flagged [T2].
4. Car limit and LCT thresholds depend on the year. Use the applicable dated table and verify later years.
5. The reverse charge section is not a complete decision procedure. Check every condition of the applicable route, including item 3 of s 84-5(1); fully creditable use alone does not establish an exemption.
6. Wine Equalisation Tax and Luxury Car Tax are noted but not fully worked -- these are specialist areas.
7. Red flag thresholds (AUD $5,000 single transaction, $500 tax-delta, $10,000 absolute position) are conservative starting values for a typical Australian self-employed client -- not empirically calibrated.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

> Contributed by Ryan Duguid.
