---
name: maldives-gst
description: Use this skill whenever asked to prepare, review, or classify transactions for a Maldives GST return for any client. Trigger on phrases like "Maldives GST", "MIRA filing", "tourism GST", or any request involving Maldives GST. MUST be loaded alongside vat-workflow-base v0.1 or later. ALWAYS read this skill before touching any Maldives GST work.
version: 2.2
jurisdiction: MV
tax_year: 2026
last_updated: 2026-11-22
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: vat-gst
type: computation
---

# Maldives GST

## Scope

Prepare and review Maldives general GST and tourism GST working papers for 2026, from evidence of supplies and purchases. Load `vat-workflow-base` alongside this Guide. A bank statement alone supports a provisional reconciliation, not a complete GST return: invoice dates, deposits, credit sales, registration and input-tax evidence change the answer.

MIRA administers GST under Act 10/2011. The distinction is the legal supply and supplier, not the customer's name or whether a resort appears in the bank narrative. Tourism leases, Green Tax, service charge and overseas booking arrangements need the additional checks below. This Guide remains tier 2 and has no accountant approval.

## Ask the client first

1. What are the GST TIN, registered taxable activities, general/tourism sectors, effective registration dates and assigned taxable period? Obtain the certificate and any period-change approval.
2. What goods or services were supplied, where and when, by which establishment? Obtain contracts, invoices, receipts, advance-payment records, credit/debit notes and evidence of exports.
3. Are amounts GST-inclusive, and do room receipts include Green Tax, service charge, refundable deposits, agency deductions or third-party collections? Obtain the gross-sales reconciliation.
4. Which purchases support taxable, exempt, private or mixed activities? Obtain full supplier tax invoices, capital-asset information and supplier registration evidence.
5. Provide all bank/payment-platform statements for the period, the previous return, unclaimed input-tax schedule, payments and credit brought forward. Identify the currencies and exchange-rate source.

Accept statements from BML, MIB, SBI Maldives, HDFC Maldives or another bank; read the actual fields and opening/closing balances. Never assume a particular bank export format or that the bank month determines the tax period.

## The method, step by step

### 1. Identify the applicable period and registration rule [https://www.mira.gov.mv/Legislations/View/8th-amendment-to-the-gsta](https://www.mira.gov.mv/Legislations/View/8th-amendment-to-the-gsta)

The eighth amendment commenced on 31 August 2026. The ninth amendment commenced on 19 November 2026 and withdrew the overseas inbound-tourism GST regime from 1 October 2026, with a refund obligation for previously charged tax. Apply the registration and cancellation dates separately. [Ninth amendment sections 8, 10, 14 and 16](https://www.mira.gov.mv/Files/GetFile/1c2c70cf-4c2c-4fee-a585-ed454689c1e7) · [MIRA circular, 22 November 2026](https://www.mira.gov.mv/Files/GetFile/351826dd-9c00-4a9a-92ce-3c4c42851949).

| Item and conditions | Amount or deadline | Period | Official source |
|---|---|---|---|
| General-sector supplies outside Act section 15, unless exempt or zero-rated | 8% | 2026 | [GST Act section 16(c)](https://www.mira.gov.mv/Legislations/View/Goods-And-Services-Act-consolidated) |
| Tourism goods/services within section 15(a), unless exempt or zero-rated | 17%; the former 16% period ended 30 June 2025 | 2026 | [GST Act sections 15(b)(5)-(6)](https://www.mira.gov.mv/Legislations/View/Goods-And-Services-Act-consolidated) |
| Overseas supplier without a fixed Maldives place of business: inbound tourism products and related booking or agency services formerly within section 15(a)(6) | The special charge was repealed with effect for those supplies from 1 October 2026. Refund any GST charged under the former rule to the person charged. | Ninth amendment in force 19 November 2026 | [Ninth amendment sections 3–4 and 14](https://www.mira.gov.mv/Files/GetFile/1c2c70cf-4c2c-4fee-a585-ed454689c1e7) · [MIRA circular](https://www.mira.gov.mv/Files/GetFile/351826dd-9c00-4a9a-92ce-3c4c42851949) |
| Qualifying exports, listed essential goods and qualifying going-concern transfer | 0%; satisfy the relevant category's conditions | 2026 | [GST Act section 22; GST Regulation sections 41-42](https://www.mira.gov.mv/Legislations/View/Goods-and-Services-Tax-Regulation-consolidated) |
| General registration turnover test for a person carrying on taxable activity; from 31 August 2026, through a fixed Maldives place of business | Supplies exceeding MVR 1,000,000 in the relevant preceding period, or expected to exceed it in the following 12 months; apply by the end of the following month after the month-end trigger | Before 31 August: section 51(a)–(i). From 31 August to 31 December 2026: section 51(k)–(m). A new turnover test applies from 1 January 2027. | [GST Act section 51](https://www.mira.gov.mv/Legislations/View/Goods-And-Services-Act-consolidated) · [Ninth amendment section 8](https://www.mira.gov.mv/Files/GetFile/1c2c70cf-4c2c-4fee-a585-ed454689c1e7#page=4) |
| Tourism supplies; commercial importers other than State institutions under the August rule | Registration independent of turnover. New tourism suppliers apply within 30 days and new commercial importers apply before importing. | 31 August to 31 December 2026. Existing persons were subject to the transitional rule. Registrations generally continue, except for deregistration under the November offshore repeal. | [GST Act sections 51(j)–(o), 54(b)](https://www.mira.gov.mv/Legislations/View/Goods-And-Services-Act-consolidated) · [MIRA circular](https://www.mira.gov.mv/Files/GetFile/351826dd-9c00-4a9a-92ce-3c4c42851949) |
| Registered person's ordinary taxable period | Quarterly below MVR 1,000,000 supplies per month; monthly at or above that monthly amount; monthly election requires approval | 2026; use the assigned period | [GST Act section 24](https://www.mira.gov.mv/Legislations/View/Goods-And-Services-Act-consolidated) |
| Return and payment | 28th of the following month; public holiday moves statutory due date to next working day | Each taxable period | [GST Act sections 28, 31, 61](https://www.mira.gov.mv/Legislations/View/Goods-And-Services-Act-consolidated) |

Before the August amendment, section 51 separately required registration of tourism suppliers and importers. Assess those events under the earlier law. Voluntary registration is possible for a qualifying licensed business under section 53. A person required to register remains liable even if unregistered under section 57. From 1 January 2027, the turnover registration test rises to MVR 1,500,000 and the ordinary turnover cancellation test becomes less than MVR 750,000 in each of the preceding and forecast 12 months, subject to the other statutory conditions. [Ninth amendment sections 8–10](https://www.mira.gov.mv/Files/GetFile/1c2c70cf-4c2c-4fee-a585-ed454689c1e7#page=4).

### 2. Determine the supply, time and tax base [https://www.mira.gov.mv/Legislations/View/Goods-And-Services-Act-consolidated](https://www.mira.gov.mv/Legislations/View/Goods-And-Services-Act-consolidated)

Match each bank line to the underlying invoice or supply. Under section 17(a), ordinary time of supply is the earlier of invoice issuance and full or partial payment, subject to the specific exceptions. From the August amendment, invoice/receipt issuance for goods and completed services is subject to the three-day rules and deemed issuance in sections 17(d)-(f). A bank-only cash total can omit credit sales and double-count deposits later settled against invoices.

For an ordinary GST-inclusive consideration, net value = gross / (1 + rate), and GST = gross - net. For a GST-exclusive value, output GST = net × rate: section 19. Separate actual pass-through taxes under section 36(a); do not treat the whole tourism receipt as room consideration without reconciling its components. Under Regulation section 52(a), a service charge on a supply is taxed at the same rate as that supply; it is not automatically a deductible tax or discount. Reconcile the actual bill and refer complex combined-levy or service-charge distribution disputes rather than silently excluding it.

The ninth amendment also removed the former offshore margin rule in section 19(e), the separate input-tax restriction in section 37(f) and the offshore place-of-supply limb in section 5-2(b)(3). MIRA deregistered covered suppliers and revoked their certificates from 19 November 2026. For the period from 1 October to 19 November the refund to the person charged is the remaining obligation under the special regime. Identify the contracting parties and apply the remaining place-of-supply and charging rules to the underlying supplies, including a local hotel’s own taxable accommodation. [Ninth amendment sections 1–7 and 14](https://www.mira.gov.mv/Files/GetFile/1c2c70cf-4c2c-4fee-a585-ed454689c1e7) · [MIRA circular, 22 November 2026](https://www.mira.gov.mv/Files/GetFile/351826dd-9c00-4a9a-92ce-3c4c42851949).

### 3. Separate exemption, zero-rating and non-supplies [https://www.mira.gov.mv/Legislations/View/Goods-and-Services-Tax-Regulation-consolidated](https://www.mira.gov.mv/Legislations/View/Goods-and-Services-Tax-Regulation-consolidated)

| Boundary | Treatment and evidence | Official source |
|---|---|---|
| Electricity, water, sewerage, education and health | Exempt when provided by the relevant registered/authorized provider; a supplier may also sell other goods or services | [GST Act section 20(a)-(g)](https://www.mira.gov.mv/Legislations/View/Goods-And-Services-Act-consolidated) |
| Bank and Islamic financial services | Only the defined financial service is exempt; consultancy or unrelated purchases through a bank are not automatically exempt | [GST Act section 20(j); GST Regulation section 35](https://www.mira.gov.mv/Legislations/View/Goods-and-Services-Tax-Regulation-consolidated) |
| Rent from immovable property | Apply the defined rent exemption and its boundaries; do not extend it to tourism accommodation merely because the contract says rent | [GST Act section 20(k); GST Regulation section 36](https://www.mira.gov.mv/Legislations/View/Goods-and-Services-Tax-Regulation-consolidated) |
| Exempt supply | No output GST; related input tax is not deductible | [GST Act section 21](https://www.mira.gov.mv/Legislations/View/Goods-And-Services-Act-consolidated) |
| Exported fish or other goods | Qualifying Customs export/re-export evidence required; a foreign buyer's name is insufficient | [GST Act section 22(b); GST Regulation section 41(a)](https://www.mira.gov.mv/Legislations/View/Goods-and-Services-Tax-Regulation-consolidated) |
| Exported services | A GST-registered Maldives supplier's service must satisfy the defined outside-consumption and recipient tests, including the conditions and exceptions immediately below; an overseas address alone is insufficient | [GST Regulation section 41(b)-(h)](https://www.mira.gov.mv/Legislations/View/Goods-and-Services-Tax-Regulation-consolidated) |
| Salary, wages and employment | Employment activity excluded; do not treat payroll payments as input purchases | [GST Act section 13(b)](https://www.mira.gov.mv/Legislations/View/Goods-And-Services-Act-consolidated) |
| Own transfers, loan principal and cash movements | Moving money alone is not the underlying sale or purchase; trace the real transaction separately | [GST Act sections 3-5, 12-13](https://www.mira.gov.mv/Legislations/View/Goods-And-Services-Act-consolidated) |

**Exported-service conditions, section 41(c)-(h).** For an ordinary non-telecommunications service, the recipient must be non-resident under Income Tax Act section 79(ll) and outside the Maldives when the service is performed. Irrespective of the contractual recipient's location, the actual physical flow must not be to a person in the Maldives receiving or benefiting from the service, and the service must not be supplied directly in connection with property situated in the Maldives when performed. Section 41(d) disapplies only the property-connection restriction for information or advice supplied to a non-resident outside the Maldives at that time; it does not remove the other recipient/consumption tests.

Telecommunications follow section 41(e)-(g), rather than the ordinary section 41(c) test. A service from a Maldives telecommunications provider to a foreign provider enabling the foreign provider's customer to access the Maldives provider's network counts as consumed outside the Maldives. The reverse provider-to-provider service enabling a Maldives provider's customer to access the foreign provider's network counts as consumed in the Maldives. A Maldives provider is one registered with the relevant government telecommunications authority; a foreign provider is one outside that definition. Under section 41(h)(2), a person with an employee or other representative present in the Maldives in connection with performance of the service is deemed to be in the Maldives. Retain evidence of the actual recipient, beneficiary/flow, property connection, timing and representative presence before treating a service as exported. [GST Regulation section 41(c)-(h)](https://www.mira.gov.mv/Legislations/View/Goods-and-Services-Tax-Regulation-consolidated).

### 4. Use narratives as investigation cues

The following preserves the transaction library. Each result depends on the evidence and legal categories above; a match is not an instruction to ignore contrary facts.

| Narrative patterns | Working-paper action |
|---|---|
| BML; BANK OF MALDIVES; MIB; MALDIVES ISLAMIC BANK; SBI MALDIVES; HDFC MALDIVES | For an authorized account-operation or other defined financial fee, classify exempt. Read the fee description; a payment through the bank can buy any kind of supply. |
| INTEREST; LOAN; REPAYMENT | Split principal, financing charges and purchases. Do not extract input GST from principal or an exempt financing service. |
| MIRA; INLAND REVENUE | Match tax payment to the liability account and period; no purchase credit from a tax remittance. |
| CUSTOMS; MALDIVES CUSTOMS | Match duty and import documents. Customs duty is not input GST. Do not manufacture GST on CIF plus duty or claim an import credit without an actual statutory tax invoice/supply. |
| PENSION; MRPS | Pension remittance; reconcile payroll, not GST input tax. |
| STELCO; STATE ELECTRIC; FENAKA | Identify qualifying electricity, ordinarily exempt under section 20(a). Correct the former automatic general-rate classification. |
| MWSC; MALE WATER | Identify qualifying water/sewerage, ordinarily exempt under section 20(b)/(d), rather than assuming standard-rated utilities. |
| DHIRAAGU; OOREDOO MALDIVES | Inspect the actual telecom supply, GST invoice and business use; do not classify from the merchant name alone. |
| GOOGLE; MICROSOFT; META; AWS; ZOOM; SLACK; CANVA | Determine contracting supplier, establishment, place of supply and registration. No blanket foreign-service self-assessment; income-tax withholding is a separate analysis. |
| BOOKING.COM; EXPEDIA; AGODA | Obtain agency contracts, gross accommodation revenue and commission invoices. Distinguish local hotel revenue from overseas booking or agency supplies and check whether the November repeal requires a refund. |
| TRIPADVISOR | Identify advertising versus booking/agency services. A tourism customer does not itself turn every marketing invoice into tourism GST. |
| SALARY; WAGES | Payroll, outside the employment taxable-activity definition. |
| OWN TRANSFER; INTERNAL | Match both sides, exclude duplicate money movement from sales and purchases. |
| CASH WITHDRAWAL | Put cash in the cash-control account, then classify the documented use. Ask for vouchers; an ATM debit proves neither a purchase nor input GST. |

Unclear sector, place, tax-inclusive status, supplier status or cash purpose stays in an unresolved schedule. Do not default unknown suppliers to domestic, unknown tourism items to a rate, or missing invoices to permanent non-deductibility. A provisional claim of no input credit pending evidence does not extinguish a later lawful claim.

### 5. Test and allocate input tax [https://www.mira.gov.mv/Legislations/View/Goods-and-Services-Tax-Regulation-consolidated](https://www.mira.gov.mv/Legislations/View/Goods-and-Services-Tax-Regulation-consolidated)

For each potential credit, confirm the recipient is registered, the supplier issued a full valid tax invoice, the supply is made in Maldives, the activity is taxable and the time limit is satisfied. Hold the invoice when filing. A statement, pro forma invoice, invoice without required purchaser details, or invented reverse charge is insufficient: Act section 37(d), Regulation sections 44 and 84.

Attribute direct costs first. Disallow exempt/private/non-business use and the other categories in Regulation section 45; apportion shared taxable/exempt costs on a reasonable evidenced basis. Keep sector/activity allocations so a mixed tourism/general business does not duplicate the same input credit. The ordinary unclaimed-input limit is 12 months under Act section 37(e) and Regulation section 44; capital costs have their own schedule.

Under Regulation section 46, gross capital expenditure on similar products or the same purpose at or below MVR 500,000 can be claimed in full within the prescribed period; above that amount, spread input tax equally over 36 months, with the output-tax limit and commencement/carry-forward conditions in subsections (a)(3)-(5). Do not claim the whole asset's input GST automatically. Section 46(b) permits a capital-input deduction only after output tax arises from that activity's primary business operations. Submit the prescribed capital-expenditure details with the return for the period incurred: section 46(c) prevents deduction without that submission. Apply the taxable/exempt allocation in section 46(d), and keep the capital-input information sheet and month-by-month balance.

Regulation section 47 excludes pre-registration purchases. Section 48 requires the unpaid proportion of a previously claimed input amount to be treated as output tax when the agreed payment obligation is not met; a later payment can restore the specified credit. Section 49 permits full input credit without exempt-use adjustment only where exempt supplies are both less than 5% of total supplies and less than MVR 10,000 per month. Test both conditions; this is not a general exemption for every small business.

### 6. Reconcile the working paper and the return [https://www.mira.gov.mv/Files/GetFile/0799ce24-cec8-4ab1-80ae-9302e7c2dcd6](https://www.mira.gov.mv/Files/GetFile/0799ce24-cec8-4ab1-80ae-9302e7c2dcd6)

Create a transaction schedule with date, bank reference, invoice/supply date, counterparty, gross amount, currency, net amount, output GST, eligible input GST, activity/sector, classification, source document and unresolved flag. Add separate controls for tourism output, general output, zero-rated sales, exempt sales, out-of-scope movements, domestic input tax, imported goods/duties, capital-input instalments and carry-forward credit. The imported-goods control is not an automatic import-input-tax box.

Reconcile gross sales to invoices and platforms, then to bank receipts after deposits, debtors, withheld commissions and timing differences. Reconcile purchases to creditors and input-tax evidence. Output tax less eligible input tax, after lawful adjustments, gives the period liability. Carry-forward balances and actual payments require a separate reconciliation; never deduct a bank tax payment as new input tax.

## Boundary and exception table

| Trigger | Decision |
|---|---|
| Tourism/general mixed operations or exempt rental alongside room supplies | Split legal supplies and input attribution; refer disputed resort/strata/vessel lease treatment. |
| Overseas booking or agency arrangements | Check contracting capacity, actual place of supply and the November repeal and refund rule. |
| Green Tax and service charge collected with accommodation | Reconcile separately; refer before finalizing the combined tax base or service-charge distribution. |
| USD and MVR receipts | Keep separate currency totals, then convert to the applicable return/payment currency using the legally permitted exchange source and date. |
| No sales but still registered | Check nil filing; registration does not lapse merely because the bank is quiet. |
| Cancellation | Until 31 December 2026, the ordinary turnover route requires less than MVR 500,000 in each of the trailing and forecast 12 months and no other registration trigger. Check the separate cessation route and obtain MIRA's effective cancellation date under section 55. |

## Worked cases

These retain the original transaction facts. Amounts below show the transaction calculation before the whole-currency return rounding required by the published forms.

### Case 1: resort room receipt in April 2026

Input: `05.04.2026 ; RESORT GUEST ; CREDIT ; Room revenue ; USD 1,160`.
Assume the entire amount is an ordinary GST-inclusive tourism accommodation supply, with no separately collected Green Tax or other component. The current tourism rate applies: USD 1,160 / 1.17 = USD 991.45 net and USD 168.55 GST. Reconcile the receipt components before using this result. The former USD 160 answer used a rate that had ended before this transaction. [GST Act sections 15 and 19](https://www.mira.gov.mv/Legislations/View/Goods-And-Services-Act-consolidated).

```oa-check
name: April 2026 tourism receipt
inputs:
  gross: 1160
steps:
  - net: round(gross / 1.17, 2)
  - gst: gross - net
expected:
  net: 991.45
  gst: 168.55
```

### Case 2: consulting receipt

Input: `10.04.2026 ; LOCAL CLIENT ; CREDIT ; Consulting ; MVR 108,000`.
Assume a registered general-sector consultant's ordinary GST-inclusive domestic service, with no exemption. Net = MVR 100,000; output GST = MVR 8,000. A resort purchasing the same general-sector service would not by itself change the supplier's sector. [GST Act sections 15-16 and 19](https://www.mira.gov.mv/Legislations/View/Goods-And-Services-Act-consolidated).

```oa-check
name: General consulting receipt
inputs:
  gross: 108000
steps:
  - net: gross / 1.08
  - gst: gross - net
expected:
  net: 100000
  gst: 8000
```

### Case 3: export or unproved foreign sale

Input: `15.04.2026 ; SRI LANKAN BUYER ; CREDIT ; Exported fish ; MVR 500,000`.
If the Customs export records substantiate the qualifying export, output GST is nil and the export consideration is MVR 500,000. If only the narrative is available, keep the item unresolved and obtain export evidence; do not infer an export merely from a Sri Lankan buyer. Reclassification requires the actual goods and domestic/essential-goods rules, not an automatic standard rate. [Regulation section 41](https://www.mira.gov.mv/Legislations/View/Goods-and-Services-Tax-Regulation-consolidated).

```oa-check
name: Documented fish export
inputs:
  consideration: 500000
steps:
  - output_gst: consideration * 0
expected:
  output_gst: 0
```

### Case 4: monthly bank fee

Input: `30.04.2026 ; BML ; DEBIT ; Monthly fee ; MVR -200`.
If this is an authorized current-account operation fee, the financial-service exemption applies and there is no input GST to claim. If it is payment for an unrelated taxable service, obtain the actual invoice before classification. [Regulation section 35(a)(1)](https://www.mira.gov.mv/Legislations/View/Goods-and-Services-Tax-Regulation-consolidated).

```oa-check
name: Exempt account operation fee
inputs:
  fee: 200
steps:
  - input_gst: fee * 0
expected:
  input_gst: 0
```

## When to refuse or refer

- **R-MV-1: resort lease and TGST complexity.** Resort operations with mixed tourism/general supplies, strata/room leases, vessel arrangements or disputed input allocation require specialist analysis. Preserve the schedules and refer the unresolved legal classification.
- **R-MV-2: Green Tax and service charge interaction.** Where accommodation receipts combine these amounts with GST, refer the levy base and distribution issues. Do not substitute a bank narrative for the guest bill or service-charge register.
- No invoices, no confirmed sector or no reliable opening credit: prepare the reconciliation and unresolved list, but stop before presenting a filing-ready liability. For overseas inbound products, check the repeal and any customer refund separately from the local supplier’s own liability.

## Filing and payment

Use [MIRAconnect](https://www.mira.gov.mv) and the registered taxable activity/period. The published [MIRA 205 general GST form](https://www.mira.gov.mv/Files/GetFile/0799ce24-cec8-4ab1-80ae-9302e7c2dcd6) and [MIRA 206 tourism GST form](https://www.mira.gov.mv/Files/GetFile/ecd5edc5-7180-4c28-a310-0865a45de2cb) use boxes 1-4 for GST-inclusive standard-rated, zero-rated, exempt and out-of-scope sales; box 5 totals sales; box 6 is output tax; box 7 is eligible input tax; box 8 is the specified bad-debt/rate-change credit adjustment; box 9 is GST collected in excess; box 10 = box 6 - box 7 - box 8 + box 9; box 11 records the payment. Complete the taxable-activity table first and attach the input/output statements required for the return.

The forms label general GST in MVR and tourism GST in USD, rounded to the nearest unit of that currency. Keep transaction calculations at adequate precision and reconcile the rounding adjustment. For other-currency transactions, Regulation section 95(b)-(c) permits a rate within ±2% of the MMA rate at time of supply and requires a consistent source; retain the conversion schedule. Tax-payment currencies are governed by Act section 62.

The published forms also carry plastic-bag-fee fields and a service-charge schedule. Complete them when applicable using their own records; do not count them as ordinary GST or fabricate a return field called import GST. For supplies covered by the November overseas inbound repeal, reconcile refunds to the person charged.

Review the return totals against the signed working paper; submit the authorized declaration, retain the acknowledgement, pay the matching liability with the correct TIN/period/reference, and retain the receipt and account reconciliation. File even where a registered period has no income; [MIRA's filing page](https://www.mira.gov.mv/Pages/View/gsthowto) identifies the nil-return route. Never mark submission complete merely because the draft or payment instruction was saved.

Late filing/information and late payment may engage [Tax Administration Act sections 65-67](https://www.mira.gov.mv/Legislations/View/tax-admin-act-consolidated). Section 65 provides the tax-related civil fine plus a daily fine not exceeding MVR 50; section 66 provides 0.05% per day on outstanding tax. Do not apply the old BPT penalty caps to GST without a current applicable authority. Refer arrears, deliberate inaccuracies and enforcement notices for a period-by-period legal calculation.

## Completion checklist

- Registration, sector, period, contracts, supply dates and bank completeness established.
- Gross sales, platform deductions, credit sales and deposits reconciled without duplication.
- Zero-rated/exempt/out-of-scope classifications and every input claim supported.
- Shared costs, capital inputs, credit notes and carry-forward balances separately controlled.
- Correct currency, exchange evidence, form fields, rounding and payment references reviewed.
- Unresolved items and specialist referrals disclosed; acknowledgement and payment receipt retained.

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. All outputs must be reviewed by a qualified professional before filing.

The most up-to-date version is maintained at [openaccountants.com](https://openaccountants.com).

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.


## Sources

| Source and actual material read | Official URL | Read on |
|---|---|---|
| MIRA-hosted English unofficial translation of GST Act 10/2011, consolidated 31 August 2026: sections 2-5, 8, 12-24, 27-29, 31-32, 36-48, 51-63 and definition of inbound tourism product | https://www.mira.gov.mv/Legislations/View/Goods-And-Services-Act-consolidated | 2026-11-16 |
| Eighth amendment 10/2026: August registration changes, original offshore charging date and commencement section 31 | https://www.mira.gov.mv/Legislations/View/8th-amendment-to-the-gsta | 2026-11-16 |
| Ninth amendment 19/2026: sections 1–10, 14 and 16, including repeal, refunds and the 2027 registration and cancellation transition | https://www.mira.gov.mv/Files/GetFile/1c2c70cf-4c2c-4fee-a585-ed454689c1e7 | 2026-11-24 |
| MIRA circular 220-TD/CIR/2026/07: repeal, prior charges and deregistration of affected suppliers | https://www.mira.gov.mv/Files/GetFile/351826dd-9c00-4a9a-92ce-3c4c42851949 | 2026-11-24 |
| MIRA English unofficial GST Regulation: sections 35-36, 41, 44-49, 52, 84-85 and 95; capital input restrictions and exchange conditions read | https://www.mira.gov.mv/Legislations/View/Goods-and-Services-Tax-Regulation-consolidated | 2026-11-16 |
| MIRA 205 v25.1, all three pages: general GST computation, taxable activities and service-charge schedule | https://www.mira.gov.mv/Files/GetFile/0799ce24-cec8-4ab1-80ae-9302e7c2dcd6 | 2026-11-16 |
| MIRA 206 v25.1, all three pages: tourism GST computation, taxable activities and service-charge schedule | https://www.mira.gov.mv/Files/GetFile/ecd5edc5-7180-4c28-a310-0865a45de2cb | 2026-11-16 |
| MIRA GST filing page: portal, nil returns and return/statement links | https://www.mira.gov.mv/Pages/View/gsthowto | 2026-11-16 |
| MIRA-hosted English unofficial Tax Administration Act consolidated 31 August 2026: sections 65-67 | https://www.mira.gov.mv/Legislations/View/tax-admin-act-consolidated | 2026-11-16 |

The legislation references include MIRA-hosted English translations and the gazetted Dhivehi ninth amendment. The Dhivehi legal text prevails if a translation differs.

Not yet confirmed: live MIRAconnect screen labels and payment-reference generation; exact service-charge/Green Tax treatment for a particular guest bill or lease; any current GST penalty relief or cap beyond the cited general provisions. Obtain the missing official determination before finalizing an affected filing.
