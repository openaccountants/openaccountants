---
name: xero-uk-vat-close
description: "Close a UK VAT period ending in 2026/27 from Xero or ledger exports: tax points, nine boxes, reverse charges, imports, digital records, reconciliation, draft adjustment journals, filing, deadlines, penalties and corrections. Produce a working paper for a named human reviewer and filer."
version: "2.1"
type: filing-howto
jurisdiction: GB
tax_year: 2026
last_updated: 2026-11-27
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: vat-gst
---

# Close a UK VAT quarter from Xero (VAT periods ending in 2026/27)

## Scope

Prepare one VAT close for a period ending from 6 April 2026 to 5 April 2027, using Xero or ledger exports. The output is a draft working paper, any proposed adjustment journal and a filing checklist. A named person reviews and files it.

Load [uk-vat-return](https://www.openaccountants.com/skills/uk-vat-return) before computing for rates, registration thresholds, scheme eligibility and blocked input tax. Follow its cited primary sources; do not assume an approval label or invent a missing figure. This Guide supplies the close workflow and its specific controls.

## Ask the client first

- Period dates, return frequency and scheme: invoice, cash, Flat Rate, annual accounting, retail or margin scheme?
- VAT number, HMRC obligations, software connection, any MTD exemption and any payments-on-account schedule?
- Imports, postponed VAT statements, C79s, overseas services, construction reverse charges or Northern Ireland/EU goods movements?
- Exempt income, private use, vehicles, fuel, property, large assets, unpaid debts or credit notes requiring specialist adjustments?
- Previous filing/payment status, old errors, penalty points or an agreed Time to Pay arrangement?
- Who reviews, who posts adjustments and who files?

## The method, step by step

1. **Gather evidence.** Read the companion Guide, confirm period and scheme against HMRC, and obtain the trial balance, VAT-account transactions and VAT return detail by box/tax rate. Add aged receivables/payables and bank reconciliation evidence. A connector is optional: request the missing exports instead of estimating ledger data. Use the client's actual account codes, not an assumed default VAT code.
2. **Complete bookkeeping.** Reconcile bank accounts through period end, resolve draft/unapproved invoices and bills, and review credit notes and tax codes. Investigate zero, exempt and No VAT coding; assess input-tax entitlement with the companion Guide rather than treating every entertainment, car or private-use cost identically.
3. **Review Xero's return.** Connect Xero to HMRC and check the VAT scheme/number in financial settings. In **Reporting → All reports → UK VAT Return**, review the earliest outstanding obligation, then **Transactions by VAT box** and **Transactions by tax rate**. HMRC supplies the filing periods; a custom-date transaction list is not a return and excludes late claims. [Xero filing documentation](https://central.xero.com/0/article/The-VAT-Return).
4. **Test cut-off.** Apply the tax-point rules below, including invoices in the first 14 days after period end. For eligible cash-accounting transactions test payments instead. Review Xero's late claims: first returns, pre-conversion transactions and scheme changes need particular checking for omissions or double counting. Software inclusion does not determine legal entitlement or the correct error-correction method.
5. **Build all nine boxes.** For each amount show the ledger/report/account/period and the relevant rule/source. Use the box and scheme tables below. Bring in supported import VAT and approved specialist adjustments; retain each calculation.
6. **Reconcile.** Bridge the signed VAT liability (box 3 minus box 4) to the VAT control account. Show opening balance, current postings, HMRC payments/refunds, prior-period liabilities, cash-versus-accrual differences, late claims, direct postings and adjustments. Do not compare a cumulative balance or an absolute repayment amount to a period movement without this bridge. [Xero discrepancies](https://central.xero.com/0/article/Troubleshoot-VAT-report-discrepancies).
7. **Sense-check.** For wholly standard-rated outputs, compare box 1 with 20% of box 6; explain imports, reverse charges, corrections and other departures. This is a diagnostic, not a substitute for the transaction review. [VATA 1994 s2](https://www.legislation.gov.uk/ukpga/1994/23/section/2); [Notice 700/12 §7](https://www.gov.uk/guidance/how-to-fill-in-and-submit-your-vat-return-vat-notice-70012).
8. **Prepare three outputs.** Produce the working paper, a proposed adjustment journal only where needed, and the dated filing/payment checklist. Label them **draft for review by a licensed accountant**, naming the reviewer. Resolve or clearly hold every unexplained difference before filing.
9. **Apply reviewed adjustments once.** Follow the Xero journal/return-adjustment instructions below, then re-run the return and reconciliation. A change to the accounts alone does not prove that the VAT return changed.
10. **Human filing.** A person with Xero's edit VAT returns permission opens the reviewed obligation, selects **Submit to HMRC**, reads and accepts the declaration, then submits. Save the VAT receipt and the filed return export; record acceptance, amount, deadline and payment arrangements. If bridging software is used, preserve the required digital links. [Xero filing documentation](https://central.xero.com/0/article/The-VAT-Return).
11. **Close.** Have the authorised administrator set the appropriate lock date and retain the working paper, evidence and receipt. A lock is a control with exceptions, not an immutable filed return. Deal with later discoveries through the rules below.

### Tax point and cut-off

For ordinary single supplies, goods usually follow removal or availability and services follow performance. An earlier VAT invoice or payment creates a tax point for the amount covered. A VAT invoice within 14 days after the basic tax point moves that part to the invoice date, unless already covered by an earlier tax point or the supplier elected out in writing. HMRC can approve a longer interval. [VATA 1994 s6(2)–(6)](https://www.legislation.gov.uk/ukpga/1994/23/section/6).

Cash accounting uses payments for eligible supplies, with the cheque-date rule in regulation 57; imports and Northern Ireland acquisitions remain outside it. Check the companion Guide's other excluded transactions. Continuous supplies, special tax points and the tax point for reverse-charge services from abroad need their own analysis: **Check this point with one of our partner accountants.** [Regulation 57](https://www.legislation.gov.uk/uksi/1995/2518/regulation/57); [Notice 700/12 §4.2](https://www.gov.uk/guidance/how-to-fill-in-and-submit-your-vat-return-vat-notice-70012).

### The nine boxes

The standard-accounting table follows [Notice 700/12 §§3.2–3.10](https://www.gov.uk/guidance/how-to-fill-in-and-submit-your-vat-return-vat-notice-70012). Apply the scheme variations separately.

| Box | Close rule |
| --- | --- |
| 1 | Output VAT due, less VAT on credit notes issued; include applicable postponed import VAT, reverse charges and fuel scale charges. Exclude HMRC assessments. |
| 2 | VAT on acquisitions of goods and related costs into Northern Ireland from EU member states. A GB establishment alone does not rule out NI movements; follow where the goods moved. |
| 3 | Box 1 plus box 2. |
| 4 | Deductible input VAT, less VAT on credit notes received; include allowable import VAT, reverse-charge input tax and bad debt relief only when entitled. Hold the invoice/import evidence or another HMRC-permitted form of evidence. No automatic full recovery. |
| 5 | Signed working-paper result = box 3 minus box 4: positive payable, negative repayable subject to HMRC enquiries. Submit the absolute difference, including zero. |
| 6 | Business sales/outputs excluding VAT, including zero/reduced/exempt supplies and relevant outside-scope services; deduct relevant credit notes. Exclude capital introduced, loans, dividends, gifts of money, insurance claims and Stock Exchange dealings except for a financial institution. |
| 7 | Purchases/expenses excluding VAT, including imports and relevant reverse-charge inputs. Exclude wages, PAYE/NI, drawings, loans/dividends/gifts of money, insurance claims, ordinary Stock Exchange dealings, MOT certificates, vehicle licence duty, local authority rates and amounts that are not consideration for a supply. |
| 8 | Qualifying goods and contract-related costs dispatched from Northern Ireland to EU member states, including relevant non-sale movements; also in box 6. Exclude separate services and processing goods. Have the reviewer settle the Notice's specific dispatch exceptions. |
| 9 | Qualifying goods acquired into Northern Ireland from VAT-registered EU suppliers and contract-related costs; also in box 7. Exclude separate services and processing goods. |

Boxes 1–5 use pence; boxes 6–9 are whole pounds (API precision: two zero decimal places). Reconcile the working paper to the software's submitted figures; do not invent a rounding convention. [HMRC VAT API, VATReturnDeclaration](https://developer.service.hmrc.gov.uk/api-documentation/docs/api/service/vat-api/1.0/oas/file).

### Reverse charges and schemes

Under [Notice 700/12 §4.6](https://www.gov.uk/guidance/how-to-fill-in-and-submit-your-vat-return-vat-notice-70012), once applicability is established:

| Transaction | Supplier | Customer |
| --- | --- | --- |
| International services / gold reverse charge | Box 6 | Boxes 1, 4 (only deductible amount), 6 and 7 |
| Domestic reverse charge, including construction | Box 6 | Boxes 1, 4 (only deductible amount) and 7; no deemed output in box 6 |

For construction end-user/intermediary notifications, zero-rated work, staff supplies and mixed contracts, do not infer applicability from the tax code: **Check this point with one of our partner accountants.**

- **Cash:** eligible payments drive boxes 1, 4, 6 and 7; other boxes follow normal rules, including NI acquisitions and imports. [Notice 700/12 §4.2](https://www.gov.uk/guidance/how-to-fill-in-and-submit-your-vat-return-vat-notice-70012).
- **Flat Rate:** box 6 includes the turnover to which the flat rate was applied **including VAT**, plus VAT-exclusive supplies outside the scheme and any box 8 amount. Box 4 is not an ordinary claim for all purchase VAT: exceptions include eligible capital goods, pre-registration claims, reverse charges and bad debt relief. Box 7 also has scheme-specific rules. For a disputed capital-goods boundary or other uncertain claim: **Check this point with one of our partner accountants.** [Notice 700/12 §4.1](https://www.gov.uk/guidance/how-to-fill-in-and-submit-your-vat-return-vat-notice-70012); [regulation 55E](https://www.legislation.gov.uk/uksi/1995/2518/regulation/55E).
- **Annual accounting:** complete boxes normally; do not deduct instalments from box 5. Deduct them when computing the actual balancing payment. Use the scheme's own deadline. [Notice 700/12 §4.3](https://www.gov.uk/guidance/how-to-fill-in-and-submit-your-vat-return-vat-notice-70012).
- **Payments on account:** the £2.3 million test uses the statutory reference/basic periods, not current-quarter turnover. Follow HMRC's payment schedule; interim payments normally fall on the last working day of months 2 and 3. Do not alter the boxes for instalments; subtract relevant payments only from the amount payable. These businesses do not receive the ordinary 7-day payment extension; standard-date balancing payments clear by month end. [1993 Order arts 4–6](https://www.legislation.gov.uk/uksi/1993/2001/article/5); [HMRC payments on account](https://www.gov.uk/guidance/vat-payments-on-account).

### Postponed import VAT

[HMRC eligibility](https://www.gov.uk/guidance/check-when-you-can-account-for-import-vat-on-your-vat-return) and [2019 Regulations 4–5](https://www.legislation.gov.uk/uksi/2019/60/regulation/4): a UK VAT-registered business can use PVA for goods imported into GB from outside the UK or NI from outside the UK/EU, subject to the business/disposal and declaration conditions. No separate approval is needed. Include the VAT number on the declaration; instruct an importing agent in writing beforehand. Select PVA on the declaration; the selection cannot be changed after submission. For wholly non-business goods, special procedures or other exceptional eligibility: **Check this point with one of our partner accountants.**

- Account in the period covering the import: VAT due in box 1, deductible amount in box 4, import value excluding VAT in box 7. Paying VAT at the border instead requires the relevant import evidence (normally C79). [Import return instructions](https://www.gov.uk/guidance/complete-your-vat-return-to-account-for-import-vat); [regulation 29(2)](https://www.legislation.gov.uk/uksi/1995/2518/regulation/29).
- Download each monthly statement from the Customs Declaration Service; usually available by the 10th working day, accessible for 6 months, then archived. Each VAT-group importer sends its own EORI statement to the representative member. [Statement guidance](https://www.gov.uk/guidance/get-your-postponed-import-vat-statement).
- If statements cannot be accessed, HMRC permits an accurate estimate from goods and related costs, followed by an adjustment on the next return once available. Do not estimate merely because the preparer has not downloaded an available statement. A missing entry, wrong EORI or unexplained discrepancy stays held for the reviewer. [Statement guidance](https://www.gov.uk/guidance/get-your-postponed-import-vat-statement).
- Correct a subsequent nil-net import error on the next return where box 1 and box 4 adjustments are equal; otherwise follow the error-correction procedure. For current Flat Rate periods, exclude postponed import VAT from flat rate turnover and add VAT due to box 1 after the flat rate calculation; do not assume input recovery. Imports cannot use cash accounting. [Import return instructions](https://www.gov.uk/guidance/complete-your-vat-return-to-account-for-import-vat).
- Royal Mail Group **postal** consignments over £135 (including Parcelforce where not acting as express operator) cannot use PVA. Commercial non-postal services may offer PVA on request. [HMRC eligibility](https://www.gov.uk/guidance/check-when-you-can-account-for-import-vat-on-your-vat-return).

### Digital records and links

For businesses subject to MTD, keep the electronic account in functional compatible software. [Regulation 32A](https://www.legislation.gov.uk/uksi/1995/2518/regulation/32A) requires business name/address/VAT number/schemes; supplies made by time, value and VAT rate; supplies received by time, value and **deductible input tax**, not a mandatory input-rate breakdown; and VAT-account totals, output categories and adjustment totals. Preserve invoices/evidence as well.

[Notice 700/22 §§3.2–3.6](https://www.gov.uk/government/publications/vat-notice-70022-making-tax-digital-for-vat/vat-notice-70022-making-tax-digital-for-vat):

- Transfers within/between products forming the electronic account need digital links, for example linked cells, CSV/XML imports, emailed files imported into software or APIs. Copy/paste or re-keying that data is not a digital link; initial source capture and permitted adjustment calculations are different.
- Record each adjustment type as a separate total. Calculations may be outside the software without digital links for their inputs. A pre-submission invoice found after software-period closure still needs a digital record even if added through an adjustment.
- Supplier-statement totals are permitted only when all supplies are on the same return and VAT at each rate is shown; cross-reference every supply to its invoice.
- Petty-cash purchases **below £50 including VAT each** can be aggregated, maximum **£500 including VAT per entry**.
- Flat Rate businesses need not keep digital purchase records except capital expenditure goods on which input tax can be claimed; retain other required evidence.
- MTD returns go through an API, directly or through bridging software. An exemption changes this route: use HMRC's authorised alternative, and continue the usual filing method while an exemption decision/appeal is pending.

### Draft journals, VAT adjustments and lock dates

Use [Xero's UK journal instructions](https://central.xero.com/0/article/Add-import-and-post-manual-journals-UK): **Reporting → All reports → Journal Report → Go to manual journals → Import → Download template file**. Populate that template, retaining its headings. Core fields map to `Narration, Date, Description, AccountCode, TaxRate, Amount`; use actual permitted account codes, full tax-rate names, debits positive and credits negative. Total debits must equal credits. Import to draft, have the human reviewer check the tax-inclusive/exclusive setting, tax rate and cash-basis-report option where relevant, then post. A person needs the applicable manual-journal permission. Do not manufacture a balancing entry to hide a difference.

For a return-box adjustment, [Xero](https://central.xero.com/0/article/Adjust-the-amounts-on-a-VAT-return) offers **Adjust**, amount and reason. For the **standard rate VAT scheme only**, **Create accounting transaction** also posts a journal to the accounts; a box-only adjustment does not do that. Do not post a second journal for the same adjustment. Xero excludes boxes 2, 3 and 5 from this accounting-transaction route; box-only adjustments exclude boxes 3 and 5. Reconcile the effect on both accounts and return.

After filing, an administrator can set the lock through **Accounting → Accounting settings → Financial settings → Lock Dates**. The lock can cover all users or exclude administrators, can be changed/removed, and does not prevent draft documents. Record its actual coverage; do not describe it as an absolute prohibition. [Xero lock dates](https://central.xero.com/0/article/Set-up-and-work-with-lock-dates).

## Boundary and exception table

| Situation | Treatment and source |
| --- | --- |
| Box 3 below box 4 | Show the repayment direction and send the absolute difference; see the nine-box table/API. |
| Invoice after period end | Apply basic/earlier/14-day tax points, not the invoice-date filter alone; see s6 above. |
| Purchase invoice first received after filing | Under regulation 29(1), claim in the first period holding the required evidence; it is not automatically an earlier-return error. If the evidence was held earlier and the claim omitted, use the correction rules. [Regulation 29](https://www.legislation.gov.uk/uksi/1995/2518/regulation/29). |
| No NI/EU goods movement | No figures in boxes 2, 8 or 9 solely because there was GB trade or a service. Test actual movement, not business-address labels. |
| Filed return wrong | Do not resubmit/amend the filed VAT return; use the correction procedure below and preserve the audit trail. [HMRC errors](https://www.gov.uk/guidance/how-to-correct-vat-errors-and-make-adjustments-or-claims-vat-notice-70045). |
| A missing PVA statement | Use the download/archive/estimation conditions above, not an unsupported guessed figure. |

## Worked cases

Rules from [VAT Notice 700/12](https://www.gov.uk/guidance/how-to-fill-in-and-submit-your-vat-return-vat-notice-70012); [import VAT on the return](https://www.gov.uk/guidance/complete-your-vat-return-to-account-for-import-vat); [VAT Notice 700](https://www.gov.uk/guidance/vat-guide-notice-700); [VAT Return deadlines](https://www.gov.uk/vat-returns/deadlines); [VAT Notice 700/45](https://www.gov.uk/guidance/how-to-correct-vat-errors-and-make-adjustments-or-claims-vat-notice-70045).
All amounts are illustrations, not client data. Assume valid evidence, full input-tax entitlement, no other transactions or errors, and ordinary quarterly deadlines unless stated otherwise.

**Case 1: building the boxes, with an import.** A Great Britain trading company on standard accounting closes the quarter to 30 September 2026. Xero's VAT report shows standard-rated sales of £50,000 net with £10,000 VAT, one credit note issued for £1,000 net with £200 VAT, and standard-rated purchases of £20,000 net with £4,000 VAT. The July postponed import VAT statement shows £1,000 of import VAT on goods valued at £5,000, and the client confirms there were no imports in August or September.

- Box 1 = £10,000 less £200 plus £1,000 = £10,800
- Box 2 = 0.00; box 3 = £10,800
- Box 4 = £4,000 plus £1,000 = £5,000
- Box 5 = £10,800 less £5,000 = £5,800 payable
- Box 6 = £50,000 less £1,000 = £49,000
- Box 7 = £20,000 plus £5,000 = £25,000
- Boxes 8 and 9 = 0.00

Sense check: 20% of £49,000 is £9,800. Box 1 is £1,000 higher, and the difference is exactly the postponed import VAT, so the check passes with that item explained.

```oa-check
name: Quarter to 30 September 2026, boxes with a credit note and postponed import VAT
inputs:
  sales_vat: 10000
  credit_note_vat: 200
  import_vat: 1000
  purchase_vat: 4000
  sales_net: 50000
  credit_note_net: 1000
  purchases_net: 20000
  import_value: 5000
steps:
  - box1: sales_vat - credit_note_vat + import_vat
  - box2: 0
  - box3: box1 + box2
  - box4: purchase_vat + import_vat
  - box5: box3 - box4
  - box6: sales_net - credit_note_net
  - box7: purchases_net + import_value
  - sense_gap: box1 - box6 * 0.20
expected:
  box3: 10800.00
  box4: 5000.00
  box5: 5800.00
  box6: 49000.00
  box7: 25000.00
  sense_gap: 1000.00
```

**Case 2: a repayment return.** A business buys equipment in the quarter. Box 3 is £2,000 and box 4 is £3,500. Box 5 = £2,000 less £3,500, a repayment of £1,500 to the business. The MTD submission sends box 5 as £1,500, the absolute difference, and HMRC work out that it is repayable. The working paper must still say "repayment of £1,500" so the reviewer and the client know which way the money moves.

**Case 3: cut-off on a service.** A consultant finishes a project on 28 September 2026 (quarter end 30 September) and has not been paid or invoiced. If she issues the VAT invoice on 8 October 2026, within 14 days, the tax point is 8 October and the VAT goes in the October to December quarter. If she issues it on 20 October 2026 (more than 14 days later, no extension agreed with HMRC), the tax point stays at 28 September and the VAT belongs in the quarter being closed, even though Xero shows an October invoice date. Assume she has not elected out of the 14-day rule. Under cash accounting, if the supply qualifies for that scheme, the VAT follows payment instead.

**Case 4: deadline.** For the quarter ending 30 September 2026, the return and payment are due by 7 November 2026, one calendar month and 7 days later. That date is a Saturday. Use the deadline in the HMRC account and allow for the payment method: payment normally needs to clear on the preceding working day unless Faster Payments applies; a properly established Direct Debit is collected under its own timetable.

**Case 5: an error found at the close.** While reconciling, the preparer finds a sales invoice from the April to June 2026 quarter that was never posted, with £3,000 of VAT. Assume it was not deliberate, the tax point was in that earlier quarter and no correction has already been made. The net error is not more than £10,000, so it can be corrected on the current return (method 1): add £3,000 to box 1 of the current return. Record the invoice in Xero as well (the digital record must be complete) without reopening the filed quarter, and keep a note of the correction. A method 1 correction is not a disclosure for penalty purposes, so the reviewer decides whether the error was careless and, if so, whether to disclose it separately in writing. Had the net error been more than £50,000, or deliberate, it would need a separate error correction notification (method 2).

**Case 6 (decision): method 1 or method 2?** Assume the errors were not deliberate and are within the ordinary correction time limit. A larger client finds a net error of £18,000 of under-declared output VAT from an earlier quarter. Box 6 of the current return is £2,400,000. The error is above £10,000, so the 1% test decides: 1% of £2,400,000 is £24,000, which is below £50,000, so the method 1 ceiling is £24,000. £18,000 is within it, so the preparer may correct it on the current return (method 1). Had box 6 been £1,500,000, 1% would be £15,000 and the £18,000 error would need method 2. A deliberate error goes to method 2 whatever its size.

```oa-check
name: Error correction, method 1 ceiling against the 1% of box 6 test
inputs:
  box6: 2400000
  net_error: 18000
  box6_smaller: 1500000
steps:
  - ceiling: min(50000, max(10000, box6 * 0.01))
  - headroom: ceiling - net_error
  - ceiling_smaller: min(50000, max(10000, box6_smaller * 0.01))
  - headroom_smaller: ceiling_smaller - net_error
expected:
  ceiling: 24000.00
  headroom: 6000.00
  ceiling_smaller: 15000.00
  headroom_smaller: -3000.00
```

A non-negative headroom permits method 1 under these assumptions; a negative headroom requires method 2.

**Historical case 7: quarter to 30 June 2026.** The folded-in predecessor used box 1 £2,000, box 2 £0 and deductible input VAT in box 4 £800. Box 3 = £2,000; box 5 = £1,200 payable. The ordinary return deadline is 7 August 2026; check the payment method and actual HMRC deadline.

```oa-check
name: VAT return box arithmetic, quarter to 30 June 2026
inputs:
  box1: 2000
  box2: 0
  box4: 800
steps:
  - box3: box1 + box2
  - box5: box3 - box4
expected:
  box3: 2000.00
  box5: 1200.00
```

## When to refuse or refer

Do not use unresolved specialist outcomes for filing: partial exemption and annual adjustments; retail/margin/Tour Operators schemes; disputed fuel/private use; capital-goods adjustments and property; NI goods exceptions; unclear construction reverse charges; bad-debt relief eligibility; missing import evidence/wrong EORI; unexplained control-account differences; late registration, insolvency, compliance checks or penalty appeals. Preserve the facts and calculations: **Check this point with one of our partner accountants.** A named reviewer must clear the relevant hold; the rest of the close remains usable.

## Filing and payment

### Deadline

Ordinary monthly/quarterly online returns are usually due one calendar month and 7 days after period end, including nil/repayment returns. Confirm the actual obligation and payment deadline in HMRC's account. Annual accounting and payments on account have different timetables. Allow for weekends/bank holidays and the payment method; do not apply the ordinary deadline blindly. [Deadlines](https://www.gov.uk/vat-returns/deadlines); [paying VAT](https://www.gov.uk/pay-vat/print); [regulation 25A(20)](https://www.legislation.gov.uk/uksi/1995/2518/regulation/25A).

### Penalties and interest

| Item | Rule and conditions | Official source |
| --- | --- | --- |
| Late submission | Periods beginning from 1 January 2023: one point per late return until the threshold; annual 2, quarterly 4, monthly 5. £200 on reaching it and £200 per subsequent late return while at it. First return after registration, final deregistration return and specified one-off returns are excluded. Non-standard periods/frequency changes need separate checking. | https://www.gov.uk/guidance/penalty-points-and-penalties-if-you-submit-your-vat-return-late; https://www.legislation.gov.uk/ukpga/2021/26/schedule/24/paragraph/5; https://www.legislation.gov.uk/ukpga/2021/26/schedule/24/paragraph/15 |
| Points expiry | Below threshold: normally last day of month 24 months after the deadline, or 25 months when due on month end. To reset all points, complete the compliance period (annual 24 months, quarterly 12, monthly 6) and submit all outstanding returns due in the previous 24 months. Confirm HMRC's reset dates. | https://www.gov.uk/guidance/remove-penalty-points-youve-received-after-submitting-your-vat-return-late; https://www.legislation.gov.uk/ukpga/2021/26/schedule/24/paragraph/8 |
| First late payment penalty | For VAT periods beginning on/after 1 April 2025: none through day 15; if 16–30 days late, 3% outstanding at day 15; if 31+ days late, add 3% outstanding at day 30. These rates do not apply to the excluded earlier periods. Payments-on-account and annual-accounting instalments are excluded from these penalties. | https://www.legislation.gov.uk/uksi/2025/589/made; https://www.gov.uk/guidance/how-late-payment-penalties-work-if-you-pay-vat-late |
| Second late payment penalty | For the same periods, daily at 10% a year on the outstanding amount from day 31. Long-outstanding tax and early assessment rules need specific analysis: Check this point with one of our partner accountants. | https://www.legislation.gov.uk/uksi/2025/589/made; https://www.gov.uk/guidance/how-late-payment-penalties-work-if-you-pay-vat-late |
| Time to Pay | A timely proposal can protect against further penalties only if HMRC agrees and the arrangement is honoured. Breach can restore penalties as if it never existed. Interest continues. | https://www.gov.uk/guidance/how-late-payment-penalties-work-if-you-pay-vat-late |
| Late payment interest | From first overdue day until paid; base rate plus 4% from 6 April 2025 (previously plus 2.5%). Dated rates: 7.75% from 9 January through 23 November 2026; 8.00% from 24 November 2026. Split any calculation at rate changes and check for later changes. | https://www.gov.uk/guidance/late-payment-interest-if-you-do-not-pay-vat-or-penalties-on-time; https://www.gov.uk/government/publications/rates-and-allowances-hmrc-interest-rates-for-late-and-early-payments/rates-and-allowances-hmrc-interest-rates |

### Earlier-return errors

Under [regulation 34](https://www.legislation.gov.uk/uksi/1995/2518/regulation/34) and [Notice 700/45 §§4.1–4.8](https://www.gov.uk/guidance/how-to-correct-vat-errors-and-make-adjustments-or-claims-vat-notice-70045):

- Aggregate all discovered earlier-return errors and take the absolute net amount. Method 1 adjusts the current VAT account/return (box 1 and/or box 4) for net errors no more than £10,000, or up to £50,000 where no more than 1% of current box 6. Identify the affected earlier returns and evidence; do not double-correct Xero late claims.
- Method 2 notifies HMRC separately for larger errors or deliberate errors of any size; it can also be chosen below the limits. Use HMRC's online error notification or the written route in the Notice. Do not include a method 2 correction again in the current return.
- Ordinary limit: four years from period end for output-tax errors/overclaimed input tax; underclaimed input tax has a return-due-date limit under regulation 29(1A). Adjacent-period tax-point mistakes and deliberate errors have special rules; do not reject or process them from this summary: **Check this point with one of our partner accountants.**
- A method 1 adjustment is not itself a penalty disclosure. A careless error needs separate disclosure for the maximum reduction; errors despite reasonable care do not require a disclosure solely because method 1 is used. Record the reviewer's decision and correct promptly.

## Completion checklist

- Companion Guide and primary sources loaded; period, scheme, VAT number, obligations and reviewer confirmed.
- Bookkeeping, tax points, input entitlement, imports, reverse charges and specialist holds checked; missing data identified.
- Nine boxes have ledger and rule references; arithmetic/sign/precision checked against the software.
- Signed return liability reconciles through an explicit VAT-account bridge; no unexplained balancing entry.
- Adjustments posted once, accounts and return re-run, draft journal balances with permitted codes and tax settings.
- Human declaration/filing, receipt, payment method and deadlines recorded; earlier errors use the correct route.
- Lock coverage recorded; evidence and working paper retained with VAT records, normally at least 6 years. [Notice 700/21 §2.4](https://www.gov.uk/guidance/record-keeping-for-vat-notice-70021).

## Sources

| Source | What was read | URL | Read on |
| --- | --- | --- | --- |
| VATA 1994 | s2 standard rate; s6(2)–(6) ordinary tax points; Schedule 11 para6 preservation power | https://www.legislation.gov.uk/ukpga/1994/23/section/6; https://www.legislation.gov.uk/ukpga/1994/23/section/2; https://www.legislation.gov.uk/ukpga/1994/23/schedule/11/paragraph/6 | 2026-11-27; s2 proof reused 2026-11-22 |
| VAT Regulations 1995 | regs25/25A filing and additional time, 29 evidence/late claims, 31/32/32A records and totals, 34 corrections, 55E capital-goods boundary, 57 cash dates | https://www.legislation.gov.uk/uksi/1995/2518/regulation/25A; https://www.legislation.gov.uk/uksi/1995/2518/regulation/29; https://www.legislation.gov.uk/uksi/1995/2518/regulation/31; https://www.legislation.gov.uk/uksi/1995/2518/regulation/32; https://www.legislation.gov.uk/uksi/1995/2518/regulation/32A; https://www.legislation.gov.uk/uksi/1995/2518/regulation/34; https://www.legislation.gov.uk/uksi/1995/2518/regulation/55E; https://www.legislation.gov.uk/uksi/1995/2518/regulation/57 | 2026-11-27 |
| Payments on Account Order 1993 | arts4–6 duty/basic-period threshold and art9 nonstandard periods | https://www.legislation.gov.uk/uksi/1993/2001/article/4; https://www.legislation.gov.uk/uksi/1993/2001/article/5; https://www.legislation.gov.uk/uksi/1993/2001/article/6; https://www.legislation.gov.uk/uksi/1993/2001/article/9 | 2026-11-27 |
| Import VAT Regulations 2019 | regs4–7 PVA election, declaration conditions and accounting | https://www.legislation.gov.uk/uksi/2019/60/regulation/4; https://www.legislation.gov.uk/uksi/2019/60/regulation/5 | 2026-11-27 |
| Finance Act 2021 Schedule24 | paras5–8 and 15–16 point thresholds, expiry/reset and monetary penalty | https://www.legislation.gov.uk/ukpga/2021/26/schedule/24/paragraph/5; https://www.legislation.gov.uk/ukpga/2021/26/schedule/24/paragraph/7; https://www.legislation.gov.uk/ukpga/2021/26/schedule/24/paragraph/8; https://www.legislation.gov.uk/ukpga/2021/26/schedule/24/paragraph/15 | 2026-11-27 |
| 2025 penalty increase Regulations | operative date/exclusions and 3%/3%/10% changes | https://www.legislation.gov.uk/uksi/2025/589/made | 2026-11-27 |
| HMRC Notice700/12 | §§3–4 box rules/schemes, §7 checks | https://www.gov.uk/guidance/how-to-fill-in-and-submit-your-vat-return-vat-notice-70012 | 2026-11-27; unchanged quotes reused 2026-11-22 |
| HMRC Notice700/22 | §§2,3.2–3.6 MTD exemptions, links, received supplies, statement/petty-cash concessions, adjustments and Flat Rate records | https://www.gov.uk/government/publications/vat-notice-70022-making-tax-digital-for-vat/vat-notice-70022-making-tax-digital-for-vat | 2026-11-27 |
| HMRC Notice700/45 | §§4.1–4.8 corrections, disclosure, time-limit exceptions | https://www.gov.uk/guidance/how-to-correct-vat-errors-and-make-adjustments-or-claims-vat-notice-70045 | 2026-11-27 |
| HMRC Notice700/21 | §2.4 ordinary six-year retention | https://www.gov.uk/guidance/record-keeping-for-vat-notice-70021 | 2026-11-27 |
| HMRC deadlines and payment | usual deadline and payment-method exceptions | https://www.gov.uk/vat-returns/deadlines; https://www.gov.uk/pay-vat/print | 2026-11-22 proof reused |
| HMRC payments on account | threshold, schedule, working-day and balancing-payment deadlines | https://www.gov.uk/guidance/vat-payments-on-account | 2026-11-27 |
| HMRC late submission/removing points | thresholds, exclusions, 24/25-month expiry and compliance conditions | https://www.gov.uk/guidance/penalty-points-and-penalties-if-you-submit-your-vat-return-late; https://www.gov.uk/guidance/remove-penalty-points-youve-received-after-submitting-your-vat-return-late | 2026-11-27 |
| HMRC late payment/interest | staged penalties, instalment exclusions, TTP and daily interest | https://www.gov.uk/guidance/how-late-payment-penalties-work-if-you-pay-vat-late; https://www.gov.uk/guidance/late-payment-interest-if-you-do-not-pay-vat-or-penalties-on-time | 2026-11-27 penalty page; interest proof reused 2026-11-22 |
| HMRC interest table | VAT row: 7.75% from9Jan and8% from24Nov; base-rate margin | https://www.gov.uk/government/publications/rates-and-allowances-hmrc-interest-rates-for-late-and-early-payments/rates-and-allowances-hmrc-interest-rates | 2026-11-27 |
| HMRC PVA eligibility/return/statements | business/declaration conditions, postal exclusion, boxes1/4/7, FRS/cash, EORI, inaccessible-statement estimates | https://www.gov.uk/guidance/check-when-you-can-account-for-import-vat-on-your-vat-return; https://www.gov.uk/guidance/complete-your-vat-return-to-account-for-import-vat; https://www.gov.uk/guidance/get-your-postponed-import-vat-statement | 2026-11-27 |
| HMRC VAT API | VATReturnDeclaration sign and precision fields | https://developer.service.hmrc.gov.uk/api-documentation/docs/api/service/vat-api/1.0/oas/file | 2026-11-27 |
| Xero UK VAT return | report/review/late-claim/file/receipt/export workflow | https://central.xero.com/0/article/The-VAT-Return | 2026-11-27, full indexed primary article read; direct page unreadable |
| Xero journals | UK template fields, draft import, posting, tax and cash settings | https://central.xero.com/0/article/Add-import-and-post-manual-journals-UK | 2026-11-27, full indexed primary article read |
| Xero return adjustments | box-only vs accounting adjustment and excluded boxes | https://central.xero.com/0/article/Adjust-the-amounts-on-a-VAT-return | 2026-11-27, indexed primary article read; direct page unreadable |
| Xero discrepancies | cumulative/basis/No VAT/late-claim differences | https://central.xero.com/0/article/Troubleshoot-VAT-report-discrepancies | 2026-11-27, full indexed primary article read |
| Xero locks | administrator, editable lock and draft exceptions | https://central.xero.com/0/article/Set-up-and-work-with-lock-dates | 2026-11-27, full indexed primary article read; direct page unreadable |

Not yet confirmed: no unresolved tax claim is offered as usable guidance. Specialist cases identified above are explicit non-usable holds pending a partner accountant. Xero instructions were read in primary documentation, not exercised in a client's organisation; use its actual template, permissions and settings before import or filing.
