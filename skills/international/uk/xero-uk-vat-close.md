---
name: xero-uk-vat-close
description: Workbench method for AI agents. Pull the quarter from Xero (connector or CSV export), compute the UK VAT return boxes from the accountant-reviewed uk-vat-return Guide, and hand back a working paper plus a Xero-ready adjustment journal for human review and filing.
jurisdiction: GB
tax_year: 2026
last_updated: 2026-09-27
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Close a UK VAT quarter from Xero and file it under Making Tax Digital (VAT periods in 2026/27)

## Scope and who this is for

This is a working method for closing one UK VAT return period from a Xero ledger (or any ledger that can export a trial balance, account transactions and a VAT report), for VAT periods ending in the 2026/27 tax year. It covers the close: cut-off, reconciliation, the nine boxes, adjustments, Making Tax Digital (MTD) filing, the deadline and penalties.

It does not restate the full box-by-box law, rates, registration thresholds or scheme eligibility. Those live in the companion Guide **uk-vat-return**. Load it before you compute anything, and take rates and thresholds from it, not from memory.

The output is a draft working paper for review. A person files the return and is responsible for it.

Two kinds of statement appear below:

- **Rules** come from HMRC guidance on gov.uk and are linked.
- **Working steps** describe how to do the job in Xero. Xero menus, report names, default account codes and import formats vary by plan, region and version, and are not HMRC rules. Confirm them in the client's own Xero file.

## Ask the client first

- Which VAT period is being closed (start and end dates), and is it quarterly, monthly or an annual accounting year?
- Which scheme applies: standard (invoice) accounting, cash accounting, Flat Rate Scheme, annual accounting, a retail or margin scheme? The boxes are filled differently under each.
- Is the business signed up for MTD, and which software submits the return (Xero itself, or bridging software)? Has HMRC granted an MTD exemption?
- Did the business import goods this period, and does it use postponed VAT accounting? Can you get the postponed import VAT statements, or the import VAT certificates (C79) if VAT was paid at the border?
- Any Northern Ireland goods trade with EU member states? Boxes 2, 8 and 9 are only for that.
- Any services bought from overseas suppliers, or building and construction services under the domestic reverse charge?
- Any exempt income (for example residential rent, insurance, finance), second-hand goods sold on a margin scheme, private fuel on company cars, or a single large asset purchase (possible capital goods scheme)?
- Any errors found in earlier returns, customers unpaid for 6 months or more, or credit notes issued or received after the period end?
- Has the previous return been filed, and was it paid on time? Any penalty points or a Time to Pay arrangement?
- Is the business in the payments on account regime (large VAT liabilities), and which interim payments were made this quarter?
- Who reviews, and who presses submit?

## The method, step by step

1. **Load the law.** Read the uk-vat-return Guide from OpenAccountants for rates, box definitions, scheme rules and blocked input tax. If a figure you need is not there, say so; do not use a remembered number.
2. **Confirm the period and scheme in Xero (working step).** Check the VAT registration number, the scheme and the return period set up in Xero's VAT settings against the client's answers and HMRC's online account. A wrong period end or scheme setting makes every figure wrong.
3. **Pull the data (working step).** From a Xero connection or by CSV export: the trial balance at period end, the VAT control account transactions for the period, the VAT return report for the period (or sales and purchases by tax rate), aged receivables and payables at period end, and bank reconciliation status. If a report is missing, name the export you need; never estimate ledger data.
4. **Finish the bookkeeping for the period (working step).** All bank accounts reconciled to the period end; no unreconciled statement lines dated in the period; sales invoices and supplier bills dated in the period approved, not left in draft or awaiting approval; nothing coded to a no-VAT rate by mistake.
5. **Test cut-off by tax point.** Output VAT belongs in the period of the tax point. Check sales invoices dated in the first 14 days after the period end, and supplies completed just before it (see the tax point rows in the boundary table). Under cash accounting, test payment dates instead.
6. **Review each tax rate code.** Scan the VAT report by rate: standard, reduced, zero, exempt, no VAT, reverse charge, postponed import VAT. Look for sales with no VAT that should carry it, input VAT claimed on blocked items (business entertainment, cars, private use), and purchases without a valid VAT invoice. The uk-vat-return Guide carries the input tax rules.
7. **Bring in off-ledger figures.** Postponed import VAT from the monthly statements for the months in the period; fuel scale charges; partial exemption adjustments; corrections of earlier errors; bad debt relief. Enter each as a total per type of adjustment, with a description. The calculation may be done outside the software, but the total must be recorded in the MTD software.
8. **Compute the nine boxes** in a table with two references for each figure: where it came from in the ledger (report, account, period) and which rule defines it.
9. **Reconcile.** Box 5 should agree to the movement on the VAT control account for the period, after allowing for the previous return's payment or repayment. List every reconciling item (late-posted bills, manual journals, rounding, adjustments). Do not absorb a difference silently.
10. **Sense-check.** If all outputs are standard-rated, box 1 should be 20% of box 6 ([VAT Notice 700/12, 7.1](https://www.gov.uk/guidance/how-to-fill-in-and-submit-your-vat-return-vat-notice-70012)). Postponed import VAT, reverse charges and corrections will move box 1 away from that; explain each.
11. **Produce the three outputs.** (a) The working paper: period, scheme, box table with both references, reconciliation, open questions. (b) A draft adjustment journal, only if reconciling items need posting: tell the user to confirm the column headings against their own Xero import screen, import it as a draft, and approve it in Xero themselves. (c) A filing checklist with the deadline.
12. **Stop at the flash points** in "When to refuse or refer" and hand the item to the reviewer with the data.
13. **File from the MTD software.** Submit from the software that holds the digital records, or through bridging software fed by a digital link. Do not re-key or copy and paste the working paper's totals into another product. Once submitted, the return cannot be amended.
14. **Lock the period (working step).** After filing, set a lock date in Xero at the period end so filed transactions cannot be changed. A transaction for a filed period that turns up later is corrected under the error correction rules, not by editing the filed period.
15. **Hand over.** Present the result as "draft for review by a licensed accountant", never as "ready to file", and say who is reviewing.

## Figures and rules for 2026/27 closes

Rates, registration thresholds, scheme limits and the full content of each box are in the uk-vat-return Guide. The rules below are the ones a close most often gets wrong.

### The nine boxes: what the close must get right ([VAT Notice 700/12](https://www.gov.uk/guidance/how-to-fill-in-and-submit-your-vat-return-vat-notice-70012))

| Box | Close-specific points |
| --- | --- |
| 1 | Output VAT on sales, less VAT on credit notes you issued. Include VAT due on imports under postponed VAT accounting, reverse charge output VAT and fuel scale charges |
| 2 | VAT due on acquisitions of goods brought into Northern Ireland from EU member states only. For a Great Britain business this is normally 0.00 |
| 3 | Box 1 plus box 2 |
| 4 | Input VAT reclaimed, less VAT on credit notes you received. Include VAT reclaimed on postponed VAT accounting imports, reverse charge input VAT and bad debt relief. Needs a proper VAT invoice (or import evidence) |
| 5 | Box 3 minus box 4. If box 3 is more than box 4, the difference is payable. If box 3 is less than box 4, HMRC credit the account and repay the balance. In the working paper show the signed result and say which way it goes. On the return itself box 5 is never negative: a paper return must not carry a minus sign, and the MTD submission sends box 5 as the positive absolute difference, with HMRC working out whether it is due or repayable. Compliant software does this for you |
| 6 | Value of all sales and other outputs excluding VAT, including zero-rated, reduced-rate and exempt supplies and services outside the scope under the place of supply rules. Not capital introduced, loans, dividends or insurance claims |
| 7 | Value of all purchases excluding VAT, including imports. Not wages, PAYE and National Insurance, drawings, loans, dividends, MOT certificates or vehicle licence duty |
| 8 | Goods (and related costs) supplied from Northern Ireland to EU member states only; also in box 6 |
| 9 | Goods (and related costs) acquired into Northern Ireland from EU member states only; also in box 7 |

**Pence and signs on the MTD submission** ([HMRC VAT (MTD) API specification](https://developer.service.hmrc.gov.uk/api-documentation/docs/api/service/vat-api/1.0/oas/file); [VAT Notice 700/12, 3.1](https://www.gov.uk/guidance/how-to-fill-in-and-submit-your-vat-return-vat-notice-70012)):

- Boxes 1 to 5 carry pence. Box 5 is sent as "the absolute difference" between box 3 and box 4, with a minimum of 0; HMRC decide whether it is due or repayable.
- Boxes 6 to 9 are whole pounds: the API accepts them only "to 2 zeroed decimal places" (pence shown as .00). The paper form similarly says "0 if no pence is required".
- Show boxes 6 to 9 in the working paper rounded the same way the software will submit them, so the working paper and the filed return agree.

**Reverse charges** ([VAT Notice 700/12](https://www.gov.uk/guidance/how-to-fill-in-and-submit-your-vat-return-vat-notice-70012)):

| Reverse charge | Supplier | Customer |
| --- | --- | --- |
| International services (and gold) | Box 6 (value of the supply) | Box 1 (output VAT), box 4 (input VAT), box 6 (value of the deemed supply) and box 7 (purchase value) |
| Domestic reverse charge, including building and construction services | Box 6 (value of the supply) | Box 1, box 4 and box 7 only; nothing in box 6 |

**Schemes** ([VAT Notice 700/12, section 4](https://www.gov.uk/guidance/how-to-fill-in-and-submit-your-vat-return-vat-notice-70012)):

- **Cash accounting:** boxes 1, 4, 6 and 7 are based on payments received and made, not invoices; other boxes are completed as normal. Imports cannot go through cash accounting; account for them in the normal way and add them to the cash figures.
- **Flat Rate Scheme:** box 6 is the turnover the flat rate percentage was applied to, **including VAT**, plus the VAT-exclusive value of anything accounted for outside the scheme. Input VAT is not normally claimed in box 4, except on qualifying capital goods.
- **Annual accounting:** box 5 is not reduced by instalments paid; the balancing payment is box 5 minus the instalments.
- **Payments on account:** a business with an annual VAT liability of more than £2.3 million makes interim payments at the end of the second and third months of each quarter. Do not change any box for them; the amount paid with the return is the box 5 liability less the payments on account already made.

### Postponed import VAT ([check when you can use it](https://www.gov.uk/guidance/check-when-you-can-account-for-import-vat-on-your-vat-return); [complete your VAT Return for import VAT](https://www.gov.uk/guidance/complete-your-vat-return-to-account-for-import-vat); [get your statement](https://www.gov.uk/guidance/get-your-postponed-import-vat-statement))

- Available to VAT-registered businesses for goods imported into Great Britain from anywhere outside the UK, and into Northern Ireland from outside the UK and EU. No approval is needed. It is chosen on the import declaration, which cannot be changed once submitted.
- Account for it on the return for the period that covers the **date of import**: VAT due in box 1, VAT reclaimed in box 4 (normal input tax rules apply), and the value of imported goods excluding VAT in box 7.
- The figures come from the monthly postponed import VAT statement in the Customs Declaration Service, usually available by the 10th working day of the month. A statement can only be viewed for 6 months from publication, so download and keep each one. If the declaration was delayed and there is no statement, estimate and adjust later.
- If the amount later changes, correct a nil-net error (box 1 equals box 4) on the next return, or use the error correction procedure.
- Flat Rate Scheme: leave postponed import VAT out of flat rate turnover, and add the VAT due to box 1 after the flat rate calculation. Cash accounting cannot be used for imports.
- Consignments over £135 sent through Royal Mail Group postal services cannot use postponed VAT accounting.
- If VAT was paid at the border instead, the evidence for box 4 is the import VAT certificate (C79).
- Working step: the statement comes from the Customs Declaration Service, not from a bank feed or supplier bill, so check that the monthly totals have been entered in Xero for every month in the period (using whatever postponed-VAT tax rate or journal the client's file uses) and attach the statement.

### Making Tax Digital records and links ([VAT Notice 700/22](https://www.gov.uk/government/publications/vat-notice-70022-making-tax-digital-for-vat/vat-notice-70022-making-tax-digital-for-vat))

- The business must keep its "electronic account" in functional compatible software: business name, principal place of business, VAT number and schemes used; for each supply made and received, the time of supply (tax point), the value excluding VAT and the rate of VAT; and summary data for each return, including each type of adjustment.
- Records can sit across more than one product, but data moving between them must travel by digital link: linked spreadsheet cells, CSV or XML import and export, emailing a spreadsheet for import, automated transfer or API. HMRC does not accept cut and paste or copy and paste as a digital link.
- The return itself must always be sent to HMRC through an API (MTD software or bridging software).
- Adjustments: record the **total for each type of adjustment** in the software. The calculation behind it (for example partial exemption or a capital goods scheme adjustment) can be done outside the software, and the inputs to that calculation do not need digital links.
- Invoices found after the software period has been closed: you may enter the figures as an adjustment so the return is correct, but you must still record the invoices in the software to complete the digital records.
- A supplier statement can be recorded as totals if all supplies on it fall in the same VAT period and the VAT at each rate is shown; the individual invoices must still be cross-referenced to it.
- Petty cash: purchases each under £50 including VAT can be recorded as a total, but no single entry may exceed £500 including VAT.
- Flat Rate Scheme users need not record purchases digitally, except capital goods on which input tax is claimed.

What this means for the method: the agent's working paper is a review document. The figures HMRC receive must come out of the MTD software. If the working paper finds an error, fix it in Xero (a transaction or an adjustment entered there), then let Xero or the bridging software produce the return.

### Tax point and cut-off ([VAT Notice 700, section 14](https://www.gov.uk/guidance/vat-guide-notice-700); [VAT Notice 700/22, 3.3.2](https://www.gov.uk/government/publications/vat-notice-70022-making-tax-digital-for-vat/vat-notice-70022-making-tax-digital-for-vat))

- **Basic tax point:** goods, usually the date they are sent to or taken away by the customer (or made available, if not moved); services, the date the service is performed, normally when all work except invoicing is complete.
- **Earlier invoice or payment:** if a VAT invoice is issued, or payment received, before the basic tax point, the tax point is the earlier of those dates for the amount invoiced or received.
- **14-day rule:** if a VAT invoice is issued up to 14 days after the basic tax point, the invoice date becomes the tax point (unless an earlier invoice or payment already created one). An invoice issued later than 14 days without HMRC approval to extend the rule leaves the tax point at the basic tax point. A business may choose not to use the 14-day rule, but must tell HMRC in writing; ask the client whether it has.
- **Cash accounting:** VAT on sales when payment is received; input tax when you pay.
- **Reverse charge services from abroad:** a single supply's tax point is when the service is completed, or when it is paid for if earlier.

### Records ([VAT Notice 700/21](https://www.gov.uk/guidance/record-keeping-for-vat-notice-70021))

- Keep business records for VAT purposes for at least 6 years. Keep the working paper, the downloaded postponed import VAT statements and C79 certificates with them.

## Boundary and exception table ([VAT Notice 700/12](https://www.gov.uk/guidance/how-to-fill-in-and-submit-your-vat-return-vat-notice-70012); [VAT Notice 700/22](https://www.gov.uk/government/publications/vat-notice-70022-making-tax-digital-for-vat/vat-notice-70022-making-tax-digital-for-vat); [VAT Notice 700/45](https://www.gov.uk/guidance/how-to-correct-vat-errors-and-make-adjustments-or-claims-vat-notice-70045); [import VAT](https://www.gov.uk/guidance/complete-your-vat-return-to-account-for-import-vat))

| Situation | Treatment |
| --- | --- |
| Box 3 is less than box 4 | A repayment. The working paper states the direction; the MTD submission still sends box 5 as a positive figure and HMRC treat it as repayable |
| Invoice issued in the next period, within 14 days after the work was finished (the basic tax point) | Tax point is the invoice date, so it falls in the next period (unless paid or invoiced earlier, or the business has opted out of the 14-day rule) |
| Invoice dated more than 14 days after the work was finished | Tax point is the basic tax point, inside the period being closed, unless HMRC approved a longer rule |
| Bill for the period posted after the return was filed | Do not edit the filed period. Treat it as an error in the earlier return: method 1 or method 2 depending on size (rows below) |
| Net earlier errors not more than £10,000 | Correct on the current return (method 1) |
| Net errors between £10,000 and £50,000, not more than 1% of current box 6 | Method 1 allowed |
| Net errors between £10,000 and £50,000 and more than 1% of box 6, over £50,000, or deliberate | Separate error correction notification to HMRC (method 2) |
| Postponed import VAT statement not yet downloaded | Download it before closing; after 6 months it is archived |
| Imports under cash accounting | Cannot use cash accounting for imports; account in the normal way |
| Flat Rate Scheme business with postponed import VAT | Leave out of flat rate turnover; add the VAT to box 1 after the flat rate calculation |
| Great Britain exports or imports | Not in boxes 8 or 9; these boxes are only for Northern Ireland goods trade with the EU |
| Submitted return has a mistake | Cannot be amended; correct it later under the error rules |

## Worked cases ([VAT Notice 700/12](https://www.gov.uk/guidance/how-to-fill-in-and-submit-your-vat-return-vat-notice-70012); [import VAT on the return](https://www.gov.uk/guidance/complete-your-vat-return-to-account-for-import-vat); [VAT Notice 700](https://www.gov.uk/guidance/vat-guide-notice-700); [VAT Return deadlines](https://www.gov.uk/vat-returns/deadlines); [VAT Notice 700/45](https://www.gov.uk/guidance/how-to-correct-vat-errors-and-make-adjustments-or-claims-vat-notice-70045))

All amounts are illustrations, not client data.

**Case 1: building the boxes, with an import.** A Great Britain trading company on standard accounting closes the quarter to 30 September 2026. Xero's VAT report shows standard-rated sales of £50,000 net with £10,000 VAT, one credit note issued for £1,000 net with £200 VAT, and standard-rated purchases of £20,000 net with £4,000 VAT. The July postponed import VAT statement shows £1,000 of import VAT on goods valued at £5,000, and the client confirms there were no imports in August or September.

- Box 1 = £10,000 less £200 plus £1,000 = £10,800
- Box 2 = 0.00; box 3 = £10,800
- Box 4 = £4,000 plus £1,000 = £5,000
- Box 5 = £10,800 less £5,000 = £5,800 payable
- Box 6 = £50,000 less £1,000 = £49,000
- Box 7 = £20,000 plus £5,000 = £25,000
- Boxes 8 and 9 = 0.00

Sense check: 20% of £49,000 is £9,800. Box 1 is £1,000 higher, and the difference is exactly the postponed import VAT, so the check passes with that item explained.

**Case 2: a repayment return.** A business buys equipment in the quarter. Box 3 is £2,000 and box 4 is £3,500. Box 5 = £2,000 less £3,500, a repayment of £1,500 to the business. The MTD submission sends box 5 as £1,500, the absolute difference, and HMRC work out that it is repayable. The working paper must still say "repayment of £1,500" so the reviewer and the client know which way the money moves.

**Case 3: cut-off on a service.** A consultant finishes a project on 28 September 2026 (quarter end 30 September) and has not been paid or invoiced. If she issues the VAT invoice on 8 October 2026, within 14 days, the tax point is 8 October and the VAT goes in the October to December quarter. If she issues it on 20 October 2026 (more than 14 days later, no extension agreed with HMRC), the tax point stays at 28 September and the VAT belongs in the quarter being closed, even though Xero shows an October invoice date. Under cash accounting, the VAT goes in whichever quarter she is paid.

**Case 4: deadline.** For the quarter ending 30 September 2026, the return and payment are due by 7 November 2026, one calendar month and 7 days later. That date is a Saturday; the payment must still reach HMRC's account by then, so allow for bank processing time.

**Case 5: an error found at the close.** While reconciling, the preparer finds a sales invoice from the April to June 2026 quarter that was never posted, with £3,000 of VAT. The net error is not more than £10,000, so it can be corrected on the current return (method 1): add £3,000 to box 1 of the current return. Record the invoice in Xero as well (the digital record must be complete) without reopening the filed quarter, and keep a note of the correction. A method 1 correction is not a disclosure for penalty purposes, so the reviewer decides whether the error was careless and, if so, whether to disclose it separately in writing. Had the net error been more than £50,000, or deliberate, it would need a separate error correction notification (method 2).

## When to refuse or refer

- Partial exemption (any exempt income beyond incidental amounts), special methods and annual adjustments.
- Margin schemes (second-hand goods, Tour Operators' Margin Scheme) and retail schemes.
- Fuel scale charges where the charge or the private use is disputed.
- Capital goods scheme items (large land and building or civil engineering expenditure): the uk-vat-return Guide carries the current thresholds and the July 2026 change.
- Northern Ireland businesses moving goods to or from the EU (boxes 2, 8 and 9).
- Construction reverse charge cases where end-user status, zero-rated new-build work or mixed supplies are unclear.
- Postponed import VAT statements that do not agree to the client's import records, missing statements, or imports declared under another company's EORI number.
- A control account difference that cannot be explained by listed items.
- Earlier errors that need method 2, deliberate errors, HMRC compliance checks, penalty appeals, insolvency, or a late registration.
- Any request to file, or to present the working paper as final, without a named person reviewing it.

## Filing and payment

### Deadline ([VAT Return deadlines](https://www.gov.uk/vat-returns/deadlines); [VAT Notice 700/12](https://www.gov.uk/guidance/how-to-fill-in-and-submit-your-vat-return-vat-notice-70012))

- A return is usually due every 3 months, and must be sent even if there is nothing to pay or reclaim.
- The online deadline is usually one calendar month and 7 days after the end of the period. That is also the payment deadline: payment must reach HMRC's account by then, even if the date falls on a weekend or bank holiday. Check the client's VAT online account for the exact dates.
- Annual accounting has different deadlines; see the uk-vat-return Guide.

### Late submission penalty points ([penalty points](https://www.gov.uk/guidance/penalty-points-and-penalties-if-you-submit-your-vat-return-late); [removing points](https://www.gov.uk/guidance/remove-penalty-points-youve-received-after-submitting-your-vat-return-late))

- One point for each late return, including nil and repayment returns. The threshold is 2 points for annual returns, 4 for quarterly and 5 for monthly.
- At the threshold there is a £200 penalty, and a further £200 for each later late return while at the threshold.
- Below the threshold, a point expires automatically on the last day of the month 24 months after the month of the missed deadline (25 months if the deadline was the last day of a month). At the threshold, all points are removed only after a period of compliance with every return on time, plus all outstanding returns for the previous 24 months submitted.

### Late payment penalties and interest ([late payment penalties](https://www.gov.uk/guidance/how-late-payment-penalties-work-if-you-pay-vat-late); [late payment interest](https://www.gov.uk/guidance/late-payment-interest-if-you-do-not-pay-vat-or-penalties-on-time); [HMRC interest rates](https://www.gov.uk/government/publications/rates-and-allowances-hmrc-interest-rates-for-late-and-early-payments/rates-and-allowances-hmrc-interest-rates))

| Days overdue | Penalty |
| --- | --- |
| 1 to 15 | No penalty (interest still runs) |
| 16 to 30 | First penalty: 3% of the VAT still owed at day 15 |
| 31 or more | First penalty: 3% of the VAT owed at day 15 plus 3% of the VAT owed at day 30; second penalty: a daily rate of 10% a year on the balance from day 31 until paid |

- Agreeing a Time to Pay arrangement early can stop the next stage of penalty.
- Late payment interest runs from the day after the due date until payment, at Bank of England base rate plus 4% (from 6 April 2025; previously plus 2.5%). HMRC's table shows 7.75% from 9 January 2026; check it for any later change.

### Correcting errors from earlier periods ([VAT Notice 700/45](https://www.gov.uk/guidance/how-to-correct-vat-errors-and-make-adjustments-or-claims-vat-notice-70045))

- Method 1 (on the current return, in box 1 or box 4): net errors not more than £10,000, or between £10,000 and £50,000 but not more than 1% of box 6 of the return in which they are found.
- Method 2 (separate notification to HMRC): anything above those limits, or any deliberate error. Method 2 may be used for any error.
- Time limit: 4 years from the end of the period in which the error occurred (output tax, and input tax over-claimed); for under-claimed input tax, 4 years from the due date of the return for the period in which the error occurred.
- A method 1 correction is not a disclosure for penalty purposes. If the error was careless, the maximum penalty reduction needs a separate written disclosure as well.

## Completion checklist ([VAT Notice 700/12](https://www.gov.uk/guidance/how-to-fill-in-and-submit-your-vat-return-vat-notice-70012); [VAT Notice 700/22](https://www.gov.uk/government/publications/vat-notice-70022-making-tax-digital-for-vat/vat-notice-70022-making-tax-digital-for-vat))

- The uk-vat-return Guide was loaded in this session and every rate used appears in it.
- Period dates, return frequency, scheme and VAT number agree between Xero, HMRC's online account and the client.
- Bank accounts reconciled to period end; nothing dated in the period left in draft or awaiting approval.
- Tax point cut-off tested, including invoices in the first 14 days after period end (or payment dates under cash accounting).
- Each tax rate reviewed; blocked input VAT removed; valid invoices held for claims.
- Postponed import VAT statements downloaded for every month in the period and entered; C79s held for VAT paid at the border.
- Reverse charges entered in the right boxes (services from abroad: 1, 4, 6, 7; construction customer: 1, 4, 7).
- Box arithmetic: box 3 = box 1 plus box 2; box 5 = box 3 minus box 4, with its direction (pay or repay) stated in the working paper and submitted as a positive figure.
- Boxes 6 to 9 in whole pounds (pence as .00), matching what the software will submit.
- Boxes 2, 8 and 9 are zero unless there is Northern Ireland goods trade with the EU.
- Box 1 compared with 20% of box 6 where all sales are standard-rated, with differences explained.
- Box 5 reconciled to the VAT control account, with every reconciling item listed.
- Every box figure carries a ledger reference and a rule reference; anything missing either is flagged as unsourced.
- Any adjustment journal balances to zero, uses account codes that exist in the client's chart, is imported as a draft, and is approved in Xero by a person.
- Adjustments recorded in the software as totals per type; late-found invoices recorded as well.
- Earlier-period errors checked against the method 1 limits.
- Flash points in "When to refuse or refer" cleared or handed to the reviewer.
- Return submitted from MTD software or via a digital link, not re-keyed; payment arranged to reach HMRC by the deadline.
- Lock date set in Xero after filing (working step); working paper and statements kept for at least 6 years.
- Output labelled "draft for review by a licensed accountant", with the reviewer named.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
