---
name: au-bas-preparation
description: >
  Use this skill to prepare, review or check an Australian business activity statement (BAS) from
  end to end, for any entity type. It covers the preparation workflow: gathering records,
  reconciling the accounts to the ledger, confirming the reporting cycle and accounting basis,
  mapping amounts to BAS labels, separating PAYG withholding from PAYG instalments, handling
  adjustments and corrections, calculating the net amount, and lodging and paying. Trigger on
  phrases like "prepare BAS", "BAS preparation", "how do I do my BAS", "Business Activity
  Statements preparation Australia GST PAYG", "BAS checklist", "reconcile BAS", "BAS labels",
  "1A 1B W1 W2 T7 5A", "net amount on BAS", "fix a BAS", "BAS due date". For the GST
  classification rules behind the labels see australia-gst; for the label-level PAYG detail see
  au-gst-bas.
version: 0.2
jurisdiction: AU
tax_year: 2026
tax_year_notes: "2026-27 (1 July 2026 to 30 June 2027)"
last_updated: 2026-09-18
review_status: pending_review
depends_on:
  - australia-gst
  - au-gst-bas
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Australia BAS Preparation v0.2

> **General reference only.** This skill is general tax and accounting reference material for
> AI-assisted workflows. It has not been reviewed for any specific person's facts, documents,
> elections, deadlines, residency, filing status or local procedures. Do not rely on it to
> lodge, pay, amend or take a tax position without review by a qualified professional.

## What this file is

**Obligation category:** CT (consumption tax), WHT (withholding tax), ET (estimated tax)
**Functional role:** Preparation workflow, spanning every role reported on one activity statement
**Status:** Source-cited draft, pending accountant review

This is the end-to-end preparation workflow. It sequences the work and tells you which guide owns
each rule. It does not restate the classification rules:

- GST classification of sales and purchases, the supplier pattern library and the refusal
  catalogue live in `australia-gst.md`.
- Label-level PAYG withholding, PAYG instalment and FBT instalment mechanics live in
  `au-gst-bas.md`.
- Property transactions, including the margin scheme and GST at settlement, live in
  `au-gst-property.md`.
- Lodgment dates, penalties, interest and remission live in `au-lodgment-deadlines-penalties.md`.

---

## Section 1 - Scope statement

This skill covers:

- The preparation sequence for a business activity statement, from source records to lodgment.
- Reconciling the GST and PAYG withholding control accounts to the ledger before any label is
  filled in.
- Choosing between Simpler BAS and full reporting, and between cash and non-cash (accruals)
  accounting for GST.
- Mapping ledger balances to the GST labels (G1, 1A, 1B), the PAYG withholding labels
  (W1 to W5, label 4), the PAYG instalment labels (T1 to T9, 5A, 5B) and the summary
  (8A, 8B, 9).
- Distinguishing PAYG withholding from PAYG instalments, which are different obligations that
  share one form.
- Adjustments, corrections of earlier errors, and when a revision is required instead.
- The lodgment and payment step, including the electronic lodgment concession.

This skill does NOT cover:

- Whether a particular supply is taxable, GST-free or input taxed. See `australia-gst.md`.
- Registration, cancellation or turnover tests. See `australia-gst.md`.
- Payroll calculation, award interpretation, superannuation guarantee or Single Touch Payroll
  reporting. See `australia-payroll.md` and `au-super-guarantee.md`.
- Fuel tax credits, wine equalisation tax and luxury car tax computation. Those labels appear on
  the BAS but their rules are outside this file.
- Income tax return preparation. PAYG instalments are prepayments only, and the return is where
  they are reconciled.

---

## Section 2 - Establish the facts before you calculate

Nothing on a BAS can be filled in reliably until these are known. Ask for them, or read them from
the client's ATO portal, before touching a number.

| Fact to establish | Why it changes the answer |
| --- | --- |
| Entity and ABN | Determines who lodges and which roles are registered |
| GST registration status and date of effect | An unregistered period has no GST labels at all |
| Reporting cycle: monthly, quarterly or annual | Sets the period and the due date |
| Simpler BAS or full reporting | Simpler BAS reports only G1, 1A and 1B for GST |
| Accounting basis: cash or non-cash (accruals) | Sets the period an amount is attributed to |
| Whether G1 is reported GST-inclusive or GST-exclusive | The BAS requires the choice to be indicated |
| PAYG withholding registration and withholder size | Determines the W labels and the payment cycle |
| PAYG instalment role, and option 1 or option 2 | Determines whether T7 or T1 and T2 are used |
| FBT instalment role | Determines whether F1 applies |
| Any prior period error not yet corrected | Determines whether a correction or a revision is needed |

**GST reporting cycle.** Quarterly applies where GST turnover is less than $20 million and the
ATO has not directed monthly reporting. Monthly is compulsory at $20 million or more, and is
available by choice below that. Annual reporting is available only to an entity that is
voluntarily registered, that is, turnover under $75,000, or under $150,000 for a not-for-profit
body. [ATO, Due dates for lodging and paying your BAS](https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/business-activity-statements-bas/due-dates-for-lodging-and-paying-your-bas)

**Accounting basis.** On a cash basis, an amount is attributed to the period in which payment
was received or made, and may be part of the sale price. On a non-cash (accruals) basis, an
amount is attributed to the earlier of the period in which any payment is received or made and
the period in which an invoice is issued or received.
[ATO, Identify your accounting basis](https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/in-detail/managing-gst-in-your-business/reporting-paying-and-activity-statements/completing-your-bas-for-gst/identify-your-accounting-basis);
[GST Act ss 29-5, 29-10](https://www.ato.gov.au/law/view/document?docid=PAC/19990055/29-5)

**Do not assume the basis from the accounting file.** A file set to accrual reporting for
management accounts can still be registered to report GST on a cash basis, and the reverse is
common after a change of adviser. Confirm the registered basis, not the software setting.

---

## Section 3 - Step 1: Gather the records

Collect, for the exact period being reported:

1. The trial balance and general ledger for the period, after the period is closed to new entries.
2. Bank statements for every business account, including credit cards and loan accounts, covering
   the full period.
3. Sales records: invoices issued, point-of-sale summaries, platform settlement reports.
4. Purchase records: tax invoices for acquisitions where a credit will be claimed.
5. Payroll records for the period: the payroll register and the Single Touch Payroll year-to-date
   figures at the period end.
6. Any ATO correspondence for the period, including the pre-filled instalment amount or rate.
7. Any adjustment notes issued or received, and any credit notes.
8. Records of assets bought or sold, including trade-ins.

**Evidence rule for credits.** A GST credit generally requires a valid tax invoice held at the
time the claim is made. The exception applies to acquisitions of $82.50 including GST or less.
The four-year credit time limit is not permission to claim before the required evidence exists.
[GST Act ss 11-5, 29-10, 29-70, 93-5](https://www.ato.gov.au/law/view/document?docid=PAC/19990055/29-10)

---

## Section 4 - Step 2: Reconcile before you report

Reconciliation is what turns the ledger into evidence. The ATO reports that incorrect timing,
miscalculation and transcription errors, unsubstantiated credit claims, credits on private-use
purchases and missed registration thresholds together make up more than half of all GST
corrections, and a reconciliation catches most of them. Complete all five before filling in a
label.

1. **Bank reconciliation.** Every business account reconciled to the statement closing balance at
   the period end, with the unpresented items listed.
2. **GST control accounts.** The GST collected and GST paid control account balances at the period
   end must agree with the GST calculated from the transaction listing for the period. An
   unexplained difference is an error, not a rounding item.
3. **PAYG withholding liability account.** The balance must agree with amounts withheld per the
   payroll register for the period, less amounts already remitted.
4. **Sales reconciliation.** Total sales per the profit and loss for the period must agree with
   G1, after allowing for the reporting basis and for items excluded from G1.
5. **Balance sheet sanity check.** Clearing and suspense accounts must be zero or fully explained.
   A transaction sitting in suspense has no GST classification, so it cannot have been reported
   correctly.

**Common source of a false reconciliation.** Transactions processed outside accounts payable or
accounts receivable, such as a direct bank entry or a journal, are often classified incorrectly
and never reach the GST control accounts. Review journals posted to revenue, expense and asset
accounts for the period before signing off the reconciliation.

---

## Section 5 - Step 3: Map GST amounts to labels

Classify every transaction first, using `australia-gst.md`. Then map.

### 5.1 Simpler BAS

If GST turnover is less than $10 million, the entity reports only three GST labels:

| Label | What goes in it |
| --- | --- |
| G1 | Total sales for the period. Indicate whether the figure includes or excludes GST |
| 1A | Total GST payable on sales for the period, including GST adjustments |
| 1B | Total GST credits on purchases for the period, including credit adjustments |

[ATO, Simpler BAS GST bookkeeping guide](https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/business-activity-statements-bas/goods-and-services-tax-gst/simpler-bas-gst-bookkeeping-guide)

### 5.2 Full reporting

Full reporting adds the G labels. Two methods are available and both are acceptable:

- **Accounts method.** Take 1A and 1B directly from the GST control accounts, which requires GST
  to be separately recorded for supplies and acquisitions.
- **Calculation worksheet method.** Complete the ATO GST calculation worksheet and transfer G9 to
  1A and G20 to 1B. The worksheet is not lodged.

[ATO, Complete your BAS: Step 5 summary](https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/in-detail/managing-gst-in-your-business/reporting-paying-and-activity-statements/completing-your-bas-for-gst/complete-your-bas/step-5-summary)

### 5.3 What is excluded from the GST labels entirely

Wages and salaries, superannuation contributions, drawings and owner contributions, loan principal,
dividends, internal transfers between the entity's own accounts, and stamp duty. These have no
GST classification. Reporting them as purchases at G11 is a recurring error.

---

## Section 6 - Step 4: PAYG withholding is not PAYG instalments

These are two separate obligations that happen to share one form. Treating them as one is a
recurring conceptual error, and it changes both the amount payable and who bears the liability.

| Feature | PAYG withholding | PAYG instalments |
| --- | --- | --- |
| Whose tax is it | The payee's (employee, contractor without an ABN, some investors) | The entity's own income tax |
| What triggers it | Making a payment from which the law requires withholding | The ATO entering the entity into the instalment system |
| Labels | W1, W2, W3, W4, W5, then label 4 | T1 to T9, then 5A or 5B |
| Effect on the entity | The entity holds and remits someone else's money | A prepayment of the entity's own tax |
| Where it is reconciled | The payee's tax return, and the entity's STP finalisation | The entity's own income tax return |
| Consequence of underpaying | Withheld amounts not remitted can attract director penalties | A shortfall is payable on assessment, with possible interest |

### 6.1 PAYG withholding labels

| Label | Content |
| --- | --- |
| W1 | Gross salary, wages and other payments subject to withholding, including payments with no amount withheld; exclusions below |
| W2 | Amounts withheld from the payments shown at W1 |
| W3 | Other amounts withheld that do not belong at W2 or W4 |
| W4 | Amounts withheld from invoices where no ABN was quoted |
| W5 | Total amounts withheld, being W2 plus W3 plus W4 |
| 4 | The W5 total, transferred to the summary |

W1 is a gross payments figure. Exclude salary sacrifice amounts, superannuation contributions
and payments whose withholding belongs at W3 or W4. Include wages below the withholding
threshold even when no tax was withheld.

W3 includes withholding from investment distributions where no TFN was quoted, interest,
dividends and royalties paid to foreign residents, departing Australia superannuation payments,
and payments to foreign residents for entertainment, sports, construction and casino gaming
junket activities.

**Large withholders:** complete only W1, and omit W1 as well if reporting through Single Touch
Payroll (STP). Leave W2, W3, W4, W5 and label 4 blank; remit withheld amounts electronically.
For other withholders, reconcile W1 and W2 to the payroll register and relevant STP figures
for the period, and investigate any difference before lodging.
[ATO, PAYG withholding: activity statement labels and large withholders](https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/business-activity-statements-bas/pay-as-you-go-payg-withholding)

### 6.2 PAYG instalment labels

| Option | Labels used | How it works |
| --- | --- | --- |
| Option 1, instalment amount | T7, and T8, T9, T4 if varying | Pay the amount the ATO calculated at T7. Enter it at 5A |
| Option 2, instalment rate | T1, T2, and T3, T4 if varying | Multiply instalment income at T1 by the rate at T2. Enter the result at 5A |

If a varied amount at T9 is negative, a credit may be claimed at 5B.
[ATO, PAYG instalments: how to complete your activity statement](https://www.ato.gov.au/forms-and-instructions/payg-instalments-how-to-complete-your-activity-statement)

**Varying carries a risk.** If varied instalments come to less than 85% of the total tax payable
on instalment income for the year, general interest charge can apply to the difference, and
penalties are possible.
[ATO, How to vary your PAYG instalments](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/payg-instalments/how-to-vary-your-payg-instalments)

**Instalment notices.** Where the entity receives an instalment notice rather than an activity
statement, and does not wish to vary, the amount can simply be paid. No lodgment is required.

---

## Section 7 - Step 5: Adjustments and corrections

These are three different things. Treat them separately.

### 7.1 Adjustments

An adjustment arises because circumstances changed after the original reporting, not because the
original reporting was wrong. Examples: a price change, a cancelled supply, a bad debt written off,
a change in the extent of creditable purpose, goods applied to private use. Adjustments belong in
the period in which the adjustment event is accounted for, and they flow into 1A or 1B.
[GST Act Div 19, Div 21, Div 129](https://www.ato.gov.au/law/view/document?docid=PAC/19990055/19-10)

An adjustment note is generally required before a decreasing adjustment on a supply is claimed.

### 7.2 Correcting an earlier GST error on a later BAS

An error is a mistake in the earlier reporting. Most can be corrected on a later BAS instead of
revising the earlier one, which generally avoids interest and penalties.

| Condition | Credit error (too much GST reported) | Debit error (too little GST reported) |
| --- | --- | --- |
| Time limit | Correct on a later BAS lodged within the period of review for the earlier period, being 4 years and one day from the day the earlier BAS was lodged | Turnover under $20 million: within 18 months of the due date of the BAS containing the error. Turnover $20 million or more: within 12 months |
| Value limit | None | Under $20m: less than $12,500. $20m to under $100m: less than $25,000. $100m to under $500m: less than $50,000. $500m to under $1b: less than $100,000. $1b and over: less than $560,000 |
| Other conditions | Cannot claim additional GST credits after the four-year credit time limit has ended | Must not result from recklessness or intentional disregard of a GST law |

The value limit applies to the net sum of debit errors less credit errors on the same BAS. Where
the net sum exceeds the limit, correct up to the limit on the later BAS and revise the original
period for the excess.
[ATO, Types of GST errors](https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/in-detail/managing-gst-in-your-business/reporting-paying-and-activity-statements/correcting-gst-errors/types-of-gst-errors);
[LI 2023/32, Correcting GST Errors Determination 2023](https://www.legislation.gov.au/F2023L01284/latest)

An error cannot be corrected on a later BAS while the entity is subject to an ATO audit or other
compliance activity for the relevant period.

### 7.3 Revising an earlier BAS

Where the correction rules do not permit a later-BAS correction, revise the earlier activity
statement. The ATO treats a revised BAS as an application to amend an assessment. If the revision
increases tax or reduces a credit, it is generally treated as a voluntary disclosure, which
usually attracts concessional treatment of penalties and interest.
[ATO, Revising an earlier business activity statement](https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/fix-a-mistake-or-amend-your-tax-return/correct-an-activity-statement/revising-an-earlier-activity-statement)

---

## Section 8 - Step 6: Calculate the result

The summary is arithmetic, not judgement, once the labels are right.

```
8A  Total amounts you owe the ATO   = 1A + 4 + 5A + 6A + 7 (+ other liability labels)
8B  Total the ATO owes you          = 1B + 5B + 6B (+ other credit labels)
9   Net amount                      = 8A - 8B
```

If 9 is positive it is payable. If negative it is refundable, subject to offsetting against other
ATO debts.

A BAS must be lodged for every period in which the entity is registered, even where the net amount
is nil and no GST was payable on any supply.
[GST Act s 31-5](https://www.ato.gov.au/law/view/document?docid=PAC/19990055/31-5)

---

## Section 9 - Step 7: Lodge and pay

| Cycle | Due date | Notes |
| --- | --- | --- |
| Monthly | 21st day of the month after the period ends | No electronic lodgment concession |
| Quarter 1, July to September | 28 October | Online lodgment may allow an extra 2 weeks |
| Quarter 2, October to December | 28 February | No further extension, the date already includes one month |
| Quarter 3, January to March | 28 April | Online lodgment may allow an extra 2 weeks |
| Quarter 4, April to June | 28 July | Online lodgment may allow an extra 2 weeks |

A due date falling on a weekend or public holiday moves to the next business day. A registered tax
or BAS agent may have a different lodgment program date, which is a concession attached to the
agent's client list and is not an automatic right of the taxpayer.
[ATO, Due dates for lodging and paying your BAS](https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/business-activity-statements-bas/due-dates-for-lodging-and-paying-your-bas)

Entities with GST turnover of $20 million or more must lodge electronically.
[GST Act s 31-25](https://www.ato.gov.au/law/view/document?docid=PAC/19990055/31-25)

**Lodgment and payment are separate obligations.** Lodging on time does not stop general interest
charge accruing on an unpaid amount. If the amount cannot be paid, lodge anyway and contact the
ATO about a payment arrangement before the due date. See `au-lodgment-deadlines-penalties.md`.

---

## Section 10 - Worked example

**Facts.** Coastline Joinery Pty Ltd, a quarterly GST lodger with GST turnover of $1.4 million, so
it uses Simpler BAS. It accounts for GST on a non-cash (accruals) basis and reports G1 including
GST. It has four employees and is registered for PAYG withholding as a small withholder. It pays
PAYG instalments using option 1. The period is the quarter ended 30 September 2026. All figures
are synthetic.

**Transactions for the quarter.**

| Item | Amount | GST treatment |
| --- | --- | --- |
| Taxable sales, including GST | $451,000 | Taxable, 1/11 is GST |
| Export of a custom joinery unit | $22,000 | GST-free, in G1, no GST |
| CNC router purchased and installed | $88,000 incl GST | Creditable acquisition |
| Other taxable purchases and expenses | $209,000 incl GST | Creditable acquisitions |
| Salaries and wages paid | $96,000 | No GST, excluded from GST labels |
| Bank account fees | $1,200 | Input taxed supply to the entity, no credit |
| Customer debt written off as bad | $5,500 incl GST | Decreasing adjustment |
| Supplier credit note received for returned goods | $1,100 incl GST | Increasing adjustment, reduces credits |
| Amounts withheld from wages | $18,400 | PAYG withholding |
| ATO instalment amount at T7 | $6,200 | PAYG instalment |

**Step 1, GST on sales.**

```
GST on taxable sales          451,000 / 11    =  41,000
Less decreasing adjustment (bad debt)
                                5,500 / 11    =    (500)
1A GST on sales                               =  40,500
```

**Step 2, GST credits.**

```
Capital acquisition            88,000 / 11    =   8,000
Other acquisitions            209,000 / 11    =  19,000
Less increasing adjustment (credit note)
                                1,100 / 11    =    (100)
1B GST on purchases                           =  26,900
```

**Step 3, G1 total sales.**

```
Taxable sales including GST                   = 451,000
GST-free export                               =  22,000
G1 Total sales (GST-inclusive basis indicated)= 473,000
```

**Step 4, PAYG withholding.**

```
W1 Total salary, wages and other payments     =  96,000
W2 Amounts withheld from W1                   =  18,400
W3 and W4                                     =       0
W5 Total amounts withheld                     =  18,400
4  PAYG tax withheld                          =  18,400
```

**Step 5, PAYG instalment.**

```
T7 ATO instalment amount                      =   6,200
5A PAYG income tax instalment                 =   6,200
```

**Step 6, summary.**

```
8A = 1A 40,500 + 4 18,400 + 5A 6,200          =  65,100
8B = 1B 26,900                                =  26,900
9  = 8A - 8B                                  =  38,200 payable
```

**Step 7, lodgment.** The quarter ended 30 September 2026, so the standard due date is
28 October 2026. If the company lodges online it may be entitled to an extra two weeks, and its
registered agent may have a different lodgment program date. The $38,200 must be paid by the
applicable due date, whether or not the statement is lodged on time.

**What the example shows.** Net GST of $13,600 is just over a third of the amount payable. The company
must fund $18,400 of employees' withheld tax and $6,200 of its own income tax prepayment out of
the same quarter's cash. A business that budgets for net GST alone will be short on the
due date.

---

## Section 11 - Common errors

Drawn from the ATO's published analysis of GST corrections and from recurring practice issues.

**Classification errors**

- Claiming GST credits on GST-free purchases such as basic food, most exports and some health
  services, and on bank fees, stamp duty and third party insurance levies.
- Claiming a credit on a purchase for private use, or failing to apportion a mixed-use purchase.
- Treating a government fee or charge as a taxable purchase.
- Claiming a full credit on a car costing more than the car limit, where the credit is capped.
  Confirm the car limit for the relevant income year on ato.gov.au before claiming.

**Timing errors**

- Reporting in the wrong period for the registered accounting basis.
- Claiming the whole credit on a lease or hire agreement in the period the goods are delivered
  rather than as payments become due.
- Claiming a credit on a real estate purchase at contract date rather than at settlement.

**Evidence errors**

- Claiming a credit with no valid tax invoice held, where the $82.50 exception does not apply.
- Tax invoices made out to the wrong entity, which is common in group structures.

**Process errors**

- Transactions processed outside accounts payable or accounts receivable and never captured in the
  GST control accounts.
- Incorrect default GST codes in the accounting file after a chart of accounts change.
- Not reconciling the GST control accounts to the BAS at all.
- Failing to recognise an adjustment event, such as a settlement discount taken by a customer.

**Threshold and registration errors**

- Not noticing that the $75,000 registration threshold has been passed. Registration is required
  within 21 days of exceeding it.
- Changing from monthly to quarterly reporting in the first 12 months of operation without ATO
  approval.

**PAYG errors**

- Reporting superannuation contributions at W1.
- Entering the instalment rate at 5A instead of the calculated instalment.
- Varying an instalment down without support, then falling under the 85% threshold.

[ATO, Managing GST in your business](https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/in-detail/managing-gst-in-your-business)

---

## Section 12 - Self-checks

Before lodging, confirm:

- [ ] The period, the entity and the ABN on the statement match the records used.
- [ ] Every business bank account is reconciled to the period end.
- [ ] The GST control account balances agree with the transaction listing for the period.
- [ ] G1 agrees with total sales per the profit and loss, after basis and exclusion differences.
- [ ] The G1 GST-inclusive or GST-exclusive choice is indicated and matches the figure entered.
- [ ] 1A and 1B include every adjustment for the period and no corrections that are out of time.
- [ ] Where W1 and W2 reporting is required, the amounts reconcile to the payroll register and relevant STP figures for the period.
- [ ] Where these labels apply, W5 equals W2 plus W3 plus W4, and label 4 equals W5. Large withholders follow Section 6.1 instead.
- [ ] 5A comes from T7, or from T9 if the amount was varied, or from T1 multiplied by T2.
- [ ] 8A less 8B equals label 9, recalculated independently.
- [ ] Any correction of a prior period error is within its time and value limits.
- [ ] Suspense and clearing accounts are nil or fully explained.
- [ ] The due date has been identified, including any electronic or agent concession.

---

## Section 13 - Sources

- A New Tax System (Goods and Services Tax) Act 1999, especially ss 11-5, 29-5, 29-10, 29-70,
  31-5, 31-25, 93-5, and Divisions 19, 21 and 129.
- Taxation Administration Act 1953, Schedule 1, Parts 2-5 (PAYG withholding) and 2-10
  (PAYG instalments).
- LI 2023/32, A New Tax System (Goods and Services Tax) (Correcting GST Errors) Determination
  2023, https://www.legislation.gov.au/F2023L01284/latest
- ATO, Due dates for lodging and paying your BAS,
  https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/business-activity-statements-bas/due-dates-for-lodging-and-paying-your-bas
- ATO, Identify your accounting basis,
  https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/in-detail/managing-gst-in-your-business/reporting-paying-and-activity-statements/completing-your-bas-for-gst/identify-your-accounting-basis
- ATO, Simpler BAS GST bookkeeping guide,
  https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/business-activity-statements-bas/goods-and-services-tax-gst/simpler-bas-gst-bookkeeping-guide
- ATO, Types of GST errors,
  https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/in-detail/managing-gst-in-your-business/reporting-paying-and-activity-statements/correcting-gst-errors/types-of-gst-errors
- ATO, PAYG instalments: how to complete your activity statement,
  https://www.ato.gov.au/forms-and-instructions/payg-instalments-how-to-complete-your-activity-statement
- ATO, How to vary your PAYG instalments,
  https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/payg-instalments/how-to-vary-your-payg-instalments

Sources were checked on 16 September 2026. Rates, thresholds and administrative processes change;
confirm each figure against the cited page for the period being reported.

---

## Section 14 - Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do
not constitute tax, legal or financial advice. Open Accountants and its contributors accept no
liability for any errors, omissions or outcomes arising from the use of this skill. All outputs
must be reviewed and signed off by a qualified professional in the relevant jurisdiction before
lodging or acting upon them.

The most up-to-date version of this skill is maintained at
[openaccountants.com](https://www.openaccountants.com).

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
