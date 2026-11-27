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
version: 0.4
jurisdiction: AU
tax_year: 2026
last_updated: 2026-11-27
depends_on:
  - australia-gst
  - au-gst-bas
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
reviewed_by: "Ryan Duguid"
reviewed_on: 2026-11-03
tier: 1
---

# Australia BAS Preparation

> **General reference only.** This skill is general tax and accounting reference material for
> AI-assisted workflows. It has not been reviewed for any specific person's facts, documents,
> elections, deadlines, residency, filing status or local procedures. Do not rely on it to
> lodge, pay, amend or take a tax position without review by a qualified professional.

## What this file is

**Obligation category:** CT (consumption tax), WHT (withholding tax), ET (estimated tax)
**Functional role:** Preparation workflow, spanning every role reported on one activity statement

This 2026 Guide retains the original 2026–27 period (1 July 2026 to 30 June 2027) and the September 2026 worked case. All amounts are Australian dollars. This is the end-to-end preparation workflow. It sequences the work and tells you which guide owns
each rule. It does not restate the classification rules:

- GST classification of sales and purchases, the supplier pattern library and the refusal
  catalogue live in `australia-gst.md`.
- Label-level PAYG withholding, PAYG instalment and FBT instalment mechanics live in
  `au-gst-bas.md`.
- Property transactions, including the margin scheme and GST at settlement, live in
  `au-gst-property.md`.
- Lodgment dates, penalties, interest and remission live in `au-lodgment-deadlines-penalties.md`.

## Section 1 - Scope statement

This skill covers:

- The preparation sequence for a business activity statement, from source records to lodgment.
- Reconciling the GST and PAYG withholding control accounts to the ledger before any label is
  filled in.
- Choosing between Simpler BAS and full reporting, and between cash and non-cash (accruals)
  accounting for GST.
- Mapping ledger balances to the GST labels (G1, 1A, 1B), the PAYG withholding labels
  (W1 to W5, label 4), the PAYG instalment labels (T1 to T11, 5A, 5B) and the summary
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

## Section 2 - Establish the facts before you calculate

**Facts to establish before calculating**

| Fact to establish | Why it changes the answer |
| --- | --- |
| Entity and ABN | Determines who lodges and which roles are registered |
| GST registration status, required-registration position and effective dates | Check the actual obligation, including any retrospective effect; do not omit a required period merely because registration was late |
| Reporting cycle: monthly, quarterly or annual | Sets the period and the due date |
| Simpler BAS or full reporting | Simpler BAS reports only G1, 1A and 1B for GST |
| Accounting basis: cash or non-cash (accruals) | Sets the period an amount is attributed to |
| Whether G1 is reported GST-inclusive or GST-exclusive | The BAS requires the choice to be indicated |
| PAYG withholding registration and withholder size | Determines the W labels and the payment cycle |
| PAYG instalment role, and option 1 or option 2 | Determines whether T7 or T1 and T2 are used |
| FBT instalment role | Determines whether F1 applies |
| Any prior period error not yet corrected | Determines whether a correction or a revision is needed |

- **GST reporting cycle.** Ordinary quarters end on 31 March, 30 June, 30 September and 31 December. Monthly applies under an effective election or Commissioner determination; the turnover threshold is $20 million. Check the actual registered periods and any special regime. Annual reporting requires an eligible election: the entity must not be required to register and must not have an effective GST-instalment election; the offshore-rights exclusion in s 151-5(2) also applies. A representative GST-group member must check every member’s eligibility, and deferred-GST users must leave that scheme before annual reporting. The ordinary voluntary-registration thresholds are under $75,000, or under $150,000 for not-for-profits, but threshold alone does not establish eligibility. [GST Act ss 27-5 to 27-15](https://www.legislation.gov.au/C2004A00446/2026-01-01/2026-01-01/text/original/epub/OEBPS/document_1/document_1.html); [annual election, s 151-5](https://www.legislation.gov.au/C2004A00446/2026-01-01/2026-01-01/text/original/epub/OEBPS/document_2/document_2.html); [ATO annual reporting](https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/when-and-how-to-report-and-pay-gst/annual-gst-reporting).
- **Accounting basis.** Under the ordinary cash rules, attribute GST and credits only to the extent payment is received or made in the period. Under the ordinary non-cash rules, use the period of any consideration or, if earlier, invoice **issue** relating to the supply/acquisition, not simply invoice receipt. Credits also require the evidence below. Particular attribution rules and special transactions can override these rules. [GST Act ss 29-5, 29-10, 29-25, 29-39](https://www.legislation.gov.au/C2004A00446/2026-01-01/2026-01-01/text/original/epub/OEBPS/document_1/document_1.html).

**Do not assume the basis from the accounting file.** A file set to accrual reporting for management accounts can still be registered to report GST on a cash basis, and the reverse is common after a change of adviser. Confirm the registered basis, not the software setting.

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

- **Evidence rule for credits.** First establish a creditable acquisition: creditable purpose, taxable supply to the entity, consideration provided or payable, and registration or required registration. A tax invoice is generally needed when lodging the return claiming the credit; if missing, defer to the first lodged return for which it is held, subject to applicable exceptions. The small-supply exception is value no more than $75 excluding GST ($82.50 including GST for a wholly taxable supply); retain other supporting evidence. The ordinary credit entitlement expires four years after the due date for the period to which it would be attributable under s 29-10(1)/(2), subject to s 93-10 exceptions. The time limit does not excuse missing evidence. [GST Act ss 11-5, 29-10, 29-80, 93-5/10](https://www.legislation.gov.au/C2004A00446/2026-01-01/2026-01-01/text/original/epub/OEBPS/document_1/document_1.html); [reg 29-80.01](https://www.legislation.gov.au/F2019L00417/2025-11-01/2025-11-01/text/original/pdf).

### 3.1 Invoice population and evidence register

An invoice sample supports conclusions about the documents inspected. It does not establish that
the purchase population is complete or that the BAS credit total is correct. Record the entity,
period, registered GST basis, export time, report filters, row count and GST control totals. Bridge
the purchase listing to the GST transaction report and ledger, including credit notes, journals,
cash transactions, duplicates and excluded items. Explain timing differences rather than forcing
the totals to agree. If only a sample was supplied, state the selection method and coverage and
leave the population reconciliation unperformed.

Keep one row per exception:

| Document / transaction | Check performed and evidence | Result | Missing fact / amount affected | Owner and next action | Status |
| --- | --- | --- | --- | --- | --- |
| Invoice or RCTI reference | Source file, issue date, GST registration evidence and reconciliation reference | Supported / exception / not checked | Identify the affected claim without guessing its treatment | Named reviewer and requested evidence | Open / resolved with evidence |

Apply these Australian invoice controls before treating an affected credit as supported:

- **RCTIs:** check eligibility and all applicable requirements in the 2023 determination, not just
  the presence of the words 'recipient created'. Both supplier and recipient must be GST registered
  when the RCTI is issued. The eligible recipient category matters; an 'other business entity' must
  determine the value of the supply. Check the current agreement, specified supplies, registration
  acknowledgements and cessation notifications. A compliant agreement may be separate or embedded
  in the RCTI under its distinct requirements. Retain dated evidence of the checks as a preparation
  control. As a preparation control, check registration before the first RCTI and periodically
  thereafter; automated checking at issue is a useful control.
  Sources: [RCTI Determination 2023, ss 6-9](https://www.legislation.gov.au/F2023L00785)
  and [ATO tax invoices, RCTI issuer responsibilities](https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/tax-invoices).
- **Current authority:** apply the 2023 determination for current RCTIs. Check all ss 6–9 requirements, including document content, issue within 28 days of supply (or later value determination), five-year retention, the written agreement, any embedded-agreement rejection, continuing compliance and reasonable taxation-law compliance. GSTR 2026/D2 is still a draft as checked on 27 November 2026; it identifies GSTR 2000/10 as withdrawn and the old determinations as inapplicable after 14 June 2023. The former Guide's **29 July 2026 withdrawal-date assertion is not verified and must not be used**; that date is the draft's publication date. Check this point with one of our partner accountants. [Draft, paras 2–3](https://www.ato.gov.au/law/view/document?DocID=DGS%2FGSTR2026D2%2FNAT%2FATO%2F00001); [operative determination](https://www.legislation.gov.au/F2023L00785/asmade/2023-06-14/text/original/epub/OEBPS/document_1/document_1.html).

- **eInvoices:** an invoice issued under the A-NZ specification through Peppol with the required
  mandatory data can satisfy the intended-tax-invoice requirement without the literal words
  'Tax Invoice'. A PDF received by email does not establish those conditions. Preserve the received
  electronic record and provenance under the firm's retention policy; do not invent a statutory
  requirement for a particular retained file format.
  See [ATO tax invoices, eInvoicing](https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/tax-invoices).
- **Payment details:** compare changes with independently verified supplier instructions using a
  trusted contact channel. Agreement between an invoice and a supplier master is insufficient if
  both could contain the same unauthorised change. Missing verification remains an open payment
  control exception; invoice validity alone does not clear it.

**Fabricated acceptance cases:**

1. Ten invoices have been checked, but no complete purchase listing or GST report was supplied.
   Report '10 documents inspected; population tie-out not performed', list the missing exports and
   leave the BAS purchase-credit reconciliation open. Do not report 'all purchases verified'.
2. An RCTI for $1,100 including $100 GST has an agreement and the supplier's current registration
   screenshot, but no evidence of either party's registration at issue. Record the missing dated
   evidence and $100 affected credit for review. Do not infer historical registration or silently
   claim the credit; consider any applicable invoice exception through the existing GST guide.
   This case does not establish a usable credit. Check this point with one of our partner accountants.

```oa-check
name: Original RCTI evidence case - arithmetic only, entitlement remains on hold
inputs:
  invoice_including_gst: 1100
steps:
  - affected_gst: invoice_including_gst / 11
expected:
  affected_gst: 100
```

## Section 4 - Step 2: Reconcile before you report

Complete these five preparation controls before filling in labels. They are working-paper instructions, not evidence that any actual ledger has been reconciled.

1. **Bank reconciliation.** Every business account reconciled to the statement closing balance at the period end, with the unpresented items listed.
2. **GST control accounts.** Bridge opening balances, current-period GST transactions, adjustments/corrections, ATO settlements and other journals to closing balances. Reconcile the period activity to the BAS transaction report; a closing balance is not automatically the period amount. Investigate every unexplained difference.
3. **PAYG withholding liability account.** Bridge the opening liability plus amounts actually withheld for the period, less remittances and any other supported movements, to the closing liability. Reconcile period withholding to the payroll register and relevant STP reports.
4. **Sales reconciliation.** Total sales per the profit and loss for the period must agree with G1, after allowing for the reporting basis and for items excluded from G1.
5. **Balance sheet sanity check.** Clearing and suspense accounts must be zero or fully explained. Inspect each suspense transaction and its GST code; its account name alone does not establish correct or incorrect GST treatment.

**Common source of a false reconciliation.** Transactions processed outside accounts payable or accounts receivable, such as a direct bank entry or a journal, are often classified incorrectly and never reach the GST control accounts. Review journals posted to revenue, expense and asset accounts for the period before signing off the reconciliation.

## Section 5 - Step 3: Map GST amounts to labels

Classify every transaction first, using `australia-gst.md`. Then map.

### 5.1 Simpler BAS

Simpler BAS is normally the default below $10 million GST turnover; confirm the recorded reporting method. Below that threshold, aggregated turnover over $10 million or a main input-taxed activity can allow a choice of Simpler or full reporting. GST instalments are a separate method. [ATO reporting methods](https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/business-activity-statements-bas/goods-and-services-tax-gst/gst-reporting-methods).

| Label | What goes in it | Official source |
| --- | --- | --- |
| G1 | Total sales; indicate whether GST-inclusive or GST-exclusive | [ATO bookkeeping guide](https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/business-activity-statements-bas/goods-and-services-tax-gst/simpler-bas-gst-bookkeeping-guide) |
| 1A | GST payable, including increasing adjustments under the accounts method | [ATO adjustments](https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/completing-your-bas-for-gst/making-adjustments-on-your-activity-statements/how-to-make-adjustments) |
| 1B | Eligible GST credits, including decreasing adjustments under the accounts method | [ATO adjustments](https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/completing-your-bas-for-gst/making-adjustments-on-your-activity-statements/how-to-make-adjustments) |

### 5.2 Full reporting

At $10 million or more GST turnover use full reporting: G1, G2, G3, G10, G11, 1A and 1B. Check other obligations shown on the issued form. [ATO reporting methods](https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/business-activity-statements-bas/goods-and-services-tax-gst/gst-reporting-methods).

- **Accounts method:** take GST amounts from reconciled records, including adjustments at the correct labels.
- **Calculation worksheet:** transfer G9 to 1A and G20 to 1B; retain the worksheet rather than lodging it. [ATO summary instructions](https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/completing-your-bas-for-gst/complete-your-bas/step-5-summary).

### 5.3 What is excluded from the GST labels entirely

- **Items excluded for GST reporting:** salary/wages, superannuation, drawings, owner contributions, loan principal, dividends received, internal transfers and stamp duty are not taxable purchase amounts. Apply the relevant method's detailed instructions; do not infer that every GST-free or input-taxed purchase is excluded from full-reporting G11. [ATO bookkeeping guide, items not reported](https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/business-activity-statements-bas/goods-and-services-tax-gst/simpler-bas-gst-bookkeeping-guide).

## Section 6 - Step 4: PAYG withholding is not PAYG instalments

**PAYG withholding vs PAYG instalments**

| Feature | PAYG withholding | PAYG instalments |
| --- | --- | --- |
| Whose tax is it | The payee's (employee, contractor without an ABN, some investors) | The entity's own income tax |
| What triggers it | Making a payment from which the law requires withholding | The ATO entering the entity into the instalment system |
| Labels | W1, W2, W3, W4, W5, then label 4 | T1 to T11, then 5A or 5B |
| Effect on the entity | The entity holds and remits someone else's money | A prepayment of the entity's own tax |
| Where it is reconciled | The payee's tax return and applicable payer reporting | The entity's own income tax return |
| Review boundary | Director-penalty exposure requires a separate liability and notice review | Review the variation risk below |

Director-penalty outcomes are not established by this workflow. Check this point with one of our partner accountants.

### 6.1 PAYG withholding labels

**PAYG withholding labels**

| Label | Content |
| --- | --- |
| W1 | Gross salary, wages and other payments subject to withholding, including payments with no amount withheld; exclusions below |
| W2 | Amounts withheld from the payments shown at W1 |
| W3 | Other amounts withheld that do not belong at W2 or W4 |
| W4 | Amounts withheld from invoices where no ABN was quoted |
| W5 | Total amounts withheld, being W2 plus W3 plus W4 |
| 4 | The W5 total, transferred to the summary; on a withholding-only form without a summary, report the total at 9 instead |

- **W1 gross payments detail** — W1 is a gross payments figure. Exclude salary sacrifice amounts, superannuation contributions and payments whose withholding belongs at W3 or W4. Include wages below the withholding threshold even when no tax was withheld.
- **W3 inclusions** — W3 includes withholding from investment distributions where no TFN was quoted, interest, dividends and royalties paid to foreign residents, departing Australia superannuation payments, and payments to foreign residents for entertainment, sports, construction and casino gaming junket activities.
- **Large withholders** — **Large withholders:** complete only W1, and omit W1 as well if reporting through Single Touch Payroll (STP). Leave W2, W3, W4, W5 and label 4 blank; remit withheld amounts electronically. For other withholders, reconcile W1 and W2 to the payroll register and relevant STP figures for the period, and investigate any difference before lodging.  _([ATO, PAYG withholding: activity statement labels and large withholders](https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/business-activity-statements-bas/pay-as-you-go-payg-withholding))_

### 6.2 PAYG instalment labels

**PAYG instalment options**  _([ATO, PAYG instalments: how to complete your activity statement](https://www.ato.gov.au/forms-and-instructions/payg-instalments-how-to-complete-your-activity-statement))_

| Option | Labels used | How it works |
| --- | --- | --- |
| Option 1, instalment amount | T7; T8 annual estimate, T9 period amount and T4 reason if varying | Unvaried T7 to 5A; varied T9 to 5A, subject to the zero/credit rule below |
| Option 2, instalment rate | T1, T2; T3 varied rate and T4 reason if varying; T11 | T11 = instalment income T1 × displayed T2 or newly varied T3; transfer T11 to 5A. T2 can already contain an earlier varied rate |

- **Negative varied amount:** if the calculated option-1 variation is nil or negative, enter **0 at T9 and 5A**. A qualifying credit for earlier instalments in the same financial year may be claimed at **5B as a positive amount**, without a minus sign.  _([ATO, PAYG instalments: how to complete your activity statement](https://www.ato.gov.au/forms-and-instructions/payg-instalments-how-to-complete-your-activity-statement))_
- **Varying carries a risk:** for the amount method, an estimate below 85% of benchmark tax can trigger general interest charge on a positive statutory shortfall. For the rate method, the test is a varied rate below 85% of the benchmark instalment rate. Lodge a variation by its due date and before the year's tax return. Do not apply one aggregate-instalments test to both options. [TAA Sch 1 ss 45-230/232](https://www.legislation.gov.au/C1953A00001/2025-07-01/2025-07-01/text/original/epub/OEBPS/document_2/document_2.html); [ATO variation instructions](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/payg-instalments/how-to-vary-your-payg-instalments).

- **Instalment notices** — **Instalment notices.** Where the entity receives an instalment notice rather than an activity statement, and does not wish to vary, the amount can simply be paid. No lodgment is required.

## Section 7 - Step 5: Adjustments and corrections

These are three different things. Treat them separately.

### 7.1 Adjustments

An adjustment responds to changed circumstances after original attribution, rather than an error in the original BAS. Review price changes, cancelled supplies, bad debts, changes in creditable purpose and private application under the relevant adjustment division. Generally attribute an adjustment when you **become aware** of it. For a cash-basis adjustment event requiring you to provide consideration, attribute only as that consideration is provided. A decreasing adjustment from an adjustment event is generally deferred until the required adjustment note is held when lodging, subject to small-adjustment and Commissioner exceptions. Special attribution rules, including Division 129 adjustment periods, must also be checked; the bookkeeping posting date alone does not decide the period. [GST Act ss 29-20, 29-25, 29-39, 29-80 and relevant adjustment divisions](https://www.legislation.gov.au/C2004A00446/2026-01-01/2026-01-01/text/original/epub/OEBPS/document_1/document_1.html).

Under the **accounts method**, increasing adjustments go to **1A** and decreasing adjustments to **1B**, including where the underlying transaction was a purchase or sale respectively. [ATO adjustments](https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/completing-your-bas-for-gst/making-adjustments-on-your-activity-statements/how-to-make-adjustments).

### 7.2 Correcting an earlier GST error on a later BAS

Use the operative [Correcting GST Errors Determination 2023, ss 4, 6–8](https://www.legislation.gov.au/F2023L01284/asmade/2023-09-25/text/original/pdf), rather than assuming that every reporting mistake qualifies. The earlier period must start on or after **1 July 2012**; lodge the later return within the earlier assessment's actual period of review, and do not correct an error already corrected to any extent in another period. The definition excludes expired Division 93 input credits and restricted historical overpaid-GST refunds. An assessment must actually be overstated/understated; GST Act s 142-10 can prevent an excess-GST error arising until its conditions are met. A correction cannot be made by amending an assessment for a later period.

| Condition | Credit error (net GST overstated) | Debit error (net GST understated) | Official source |
| --- | --- | --- | --- |
| Review period | Normally four years and one day after lodging the original BAS; check the actual period, including any refreshed review period | Same review-period condition, plus the shorter debit time limits below | [ATO errors](https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/completing-your-bas-for-gst/correcting-gst-errors/types-of-gst-errors); [s 6](https://www.legislation.gov.au/F2023L01284/asmade/2023-09-25/text/original/pdf) |
| Value | No debit-value limit; input-credit time limits still apply | Strictly below the applicable net debit limit | [ss 4, 7](https://www.legislation.gov.au/F2023L01284/asmade/2023-09-25/text/original/pdf) |
| Conduct | Other s 6 conditions still apply | Must not result from recklessness or intentional disregard of GST law | [ss 6–7](https://www.legislation.gov.au/F2023L01284/asmade/2023-09-25/text/original/pdf) |

| Current GST turnover | Later BAS must be lodged within this time from original BAS due date | Net debit errors must be less than | Official source |
| --- | --- | --- | --- |
| Under $20 million | 18 months | $12,500 | [s 7](https://www.legislation.gov.au/F2023L01284/asmade/2023-09-25/text/original/pdf) |
| $20 million to under $100 million | 12 months | $25,000 | [s 7](https://www.legislation.gov.au/F2023L01284/asmade/2023-09-25/text/original/pdf) |
| $100 million to under $500 million | 12 months | $50,000 | [s 7](https://www.legislation.gov.au/F2023L01284/asmade/2023-09-25/text/original/pdf) |
| $500 million to under $1 billion | 12 months | $100,000 | [s 7](https://www.legislation.gov.au/F2023L01284/asmade/2023-09-25/text/original/pdf) |
| $1 billion and over | 12 months | $560,000 | [s 7](https://www.legislation.gov.au/F2023L01284/asmade/2023-09-25/text/original/pdf) |

Net debit errors means the debit error amounts less the credit error amounts included on that same later BAS. For a GST group use the group's current turnover under s 188-15(2). Relevant notified compliance activity normally prevents correction, **unless the Commissioner notifies you in writing that the error may be corrected under the determination**. Check the matter and period covered by the notice. [ss 4, 6–7](https://www.legislation.gov.au/F2023L01284/asmade/2023-09-25/text/original/pdf).

**Non-usable boundary:** some ATO worked examples allow correction exactly at the value limit, while operative s 7(c) says **less than**. Do not use equality or the former instruction to correct 'up to the limit' and revise only the excess as an established entitlement. Preserve the full error and original period for review. Check this point with one of our partner accountants.

### 7.3 Revising an earlier BAS

- **Revising an earlier BAS** — Where the correction rules do not permit a later-BAS correction, revise the earlier activity statement. The ATO treats a revised BAS as an application to amend an assessment. If the revision increases tax or reduces a credit, it is generally treated as a voluntary disclosure, which usually attracts concessional treatment of penalties and interest.  _([ATO, Revising an earlier business activity statement](https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/fix-a-mistake-or-amend-your-tax-return/correct-an-activity-statement/revising-an-earlier-activity-statement))_

## Section 8 - Step 6: Calculate the result

Use only applicable labels on the issued BAS, including other obligations where present:

```
8A = 1A + 4 + 5A + 6A + applicable other liability labels (such as 7C)
8B = 1B + 5B + 6B + applicable other credit labels (such as 7D)
9  = 8A - 8B
```

Do not add gross W1 payments or annual estimates to the summary. A positive result is a payment; a negative result is a potential refund, subject to ATO processing and debt offset. See [ATO BAS summary](https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/completing-your-bas-for-gst/complete-your-bas/step-5-summary) and the label-specific instructions in Section 6. Retain the lodgment receipt and payment/refund working paper; check the account after processing.

- **Nil BAS:** ordinary registered entities must lodge GST returns for their applicable periods even when nil; check special regimes rather than applying the rule to every entity. An unvaried instalment notice follows Section 6 instead. [GST Act ss 31-5, 31-99](https://www.legislation.gov.au/C2004A00446/2026-01-01/2026-01-01/text/original/epub/OEBPS/document_1/document_1.html).

## Section 9 - Step 7: Lodge and pay

Review the completed statement and lodge through the entity's authorised ATO online service or registered tax/BAS agent; individuals and sole traders may use ATO services linked to myGov, other businesses Online services for business. Confirm the entity, period and actual due dates; retain the submission receipt. Use the statement's payment instructions and correct unique payment reference number for the relevant account, and retain payment confirmation. For a refund, verify account details through a trusted channel and check the processed account for offsets. [ATO lodgment options](https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/business-activity-statements-bas/how-to-lodge-your-bas); [payment instructions](https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/business-activity-statements-bas/due-dates-for-lodging-and-paying-your-bas).

**Due dates by cycle**  _([ATO, Due dates for lodging and paying your BAS](https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/business-activity-statements-bas/due-dates-for-lodging-and-paying-your-bas))_

| Cycle | Due date | Notes | Official source |
| --- | --- | --- | --- |
| Monthly | 21st day of the following month | Ordinary quarterly online two-week offer does not apply; check actual notices and agent/individual deferrals | [ATO due dates](https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/business-activity-statements-bas/due-dates-for-lodging-and-paying-your-bas) |
| Quarter 1, July to September | 28 October | Online lodgment may allow an extra 2 weeks | [ATO due dates](https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/business-activity-statements-bas/due-dates-for-lodging-and-paying-your-bas) |
| Quarter 2, October to December | 28 February | No additional quarterly online two weeks; check any separately granted deferral | [ATO due dates](https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/business-activity-statements-bas/due-dates-for-lodging-and-paying-your-bas) |
| Quarter 3, January to March | 28 April | Online lodgment may allow an extra 2 weeks | [ATO due dates](https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/business-activity-statements-bas/due-dates-for-lodging-and-paying-your-bas) |
| Quarter 4, April to June | 28 July | Online lodgment may allow an extra 2 weeks | [ATO due dates](https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/business-activity-statements-bas/due-dates-for-lodging-and-paying-your-bas) |

- **Weekend/holiday and agent program** — A due date falling on a weekend or public holiday moves to the next business day. A registered tax or BAS agent may have a different lodgment program date, which is a concession attached to the agent's client list and is not an automatic right of the taxpayer.  _([ATO, Due dates for lodging and paying your BAS](https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/business-activity-statements-bas/due-dates-for-lodging-and-paying-your-bas))_
- **Electronic lodgment threshold** — Entities meeting the $20 million electronic-lodgment turnover threshold must lodge electronically unless the Commissioner approves otherwise.  _([GST Act s 31-25](https://www.legislation.gov.au/C2004A00446/2026-01-01/2026-01-01/text/original/epub/OEBPS/document_1/document_1.html))_

**Lodgment and payment are separate obligations.** Lodging on time does not stop general interest charge accruing on an unpaid amount. If the amount cannot be paid, lodge anyway and contact the ATO about a payment arrangement before the due date. See `au-lodgment-deadlines-penalties.md`.

## Section 10 - Worked example

**Facts.** Coastline Joinery Pty Ltd, a quarterly GST lodger with GST turnover of $1.4 million, so it uses Simpler BAS. It accounts for GST on a non-cash (accruals) basis and reports G1 including GST. It has four employees and is registered for PAYG withholding as a small withholder. It pays PAYG instalments using option 1. The period is the quarter ended 30 September 2026. All figures are synthetic. Assume the export satisfies the GST-free requirements in the existing GST Guide, the router and other purchases are wholly creditable taxable acquisitions with required invoices held, and the $1,200 bank-account fees contain no GST. The bad debt is unpaid consideration for a previously attributed taxable sale, now validly written off under s 21-5; the supplier return cancels/reduces a previously credited acquisition under ss 19-70/80, not a return merely for repair. Both adjustments are attributable in this quarter. These assumptions must be established from evidence in a real BAS; they are not established by the amounts alone. [GST Act ss 11-5, 19-10/70/80, 21-5 and 29-20](https://www.legislation.gov.au/C2004A00446/2026-01-01/2026-01-01/text/original/epub/OEBPS/document_1/document_1.html).

**Transactions for the quarter**

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
Plus increasing adjustment (supplier return)
                                1,100 / 11    =     100
1A GST on sales                               =  41,100
```

**Step 2, GST credits.**

```
Capital acquisition            88,000 / 11    =   8,000
Other acquisitions            209,000 / 11    =  19,000
Plus decreasing adjustment (bad debt)
                                5,500 / 11    =     500
1B GST on purchases                           =  27,500
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
W3 and W4                                     =       0 (nil; follow blank-field instructions)
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
8A = 1A 41,100 + 4 18,400 + 5A 6,200          =  65,700
8B = 1B 27,500                                =  27,500
9  = 8A - 8B                                  =  38,200 payable
```

**Step 7, lodgment.** The quarter ended 30 September 2026, so the standard due date is 28 October 2026. If the company lodges online it may be entitled to an extra two weeks, and its registered agent may have a different lodgment program date. The $38,200 must be paid by the applicable due date, whether or not the statement is lodged on time.

**What the example shows.** Net GST of $13,600 is just over a third of the amount payable. The company must fund $18,400 of employees' withheld tax and $6,200 of its own income tax prepayment out of the same quarter's cash. A business that budgets for net GST alone will be short on the due date.

```oa-check
name: Coastline Joinery - original September 2026 inputs, corrected accounts-method labels
inputs:
  taxable_sales: 451000
  export_sales: 22000
  router: 88000
  other_purchases: 209000
  wages: 96000
  bank_fees: 1200
  bad_debt: 5500
  supplier_return: 1100
  withheld: 18400
  instalment: 6200
steps:
  - sales_gst: taxable_sales / 11
  - router_gst: router / 11
  - other_gst: other_purchases / 11
  - decreasing: bad_debt / 11
  - increasing: supplier_return / 11
  - label_1a: sales_gst + increasing
  - label_1b: router_gst + other_gst + decreasing
  - g1: taxable_sales + export_sales
  - w1: wages
  - label_4: withheld
  - label_5a: instalment
  - label_8a: label_1a + label_4 + label_5a
  - label_8b: label_1b
  - label_9: label_8a - label_8b
  - net_gst: label_1a - label_1b
  - gst_percent: net_gst / label_9 * 100
expected:
  sales_gst: 41000
  router_gst: 8000
  other_gst: 19000
  decreasing: 500
  increasing: 100
  label_1a: 41100
  label_1b: 27500
  g1: 473000
  w1: 96000
  label_4: 18400
  label_5a: 6200
  label_8a: 65700
  label_8b: 27500
  label_9: 38200
  net_gst: 13600
  gst_percent: 35.6021
```

## Section 11 - Common errors

Use these checks; no claim is made about how frequently they occur.

**Classification and evidence**

- Establish the taxable/creditable character under Section 3 before claiming a credit. A private-use portion is not creditable; apportion a mixed-purpose acquisition. Check the entity and required information on the invoice, including any applicable group/agency exception. An invoice above the small-supply exception without required evidence is not cleared merely because it was paid.
- Basic food, exports, health services, bank charges, stamp duty, third-party insurance levies and government fees are not one uniform class. Use the existing GST Guide's classification and any applicable special rule; a generic list must not decide liability or the G11 entry. Car-credit limits require the actual vehicle, acquisition date, year and exception facts. **Specific outcomes for these classification/car-limit cases are not established here.** Check this point with one of our partner accountants.

**Timing**

- Apply the confirmed cash/non-cash basis, invoice evidence and special attribution rules, not the software posting date.
- Distinguish a lease from hire purchase. The former blanket refusal of an upfront credit on every 'lease or hire' is withdrawn; hire-purchase agreements on or after 1 July 2012 have different credit timing, including for cash-basis taxpayers. Obtain the agreement and apply [ATO hire purchase and leasing](https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/in-detail/rules-for-specific-transactions/agent-consignment-and-progressive-transactions/gst-hire-purchase-and-leasing). **The particular agreement's credit amount/period is not established here.** Check this point with one of our partner accountants.
- For real estate, do not use the former contract-versus-settlement shortcut as a universal rule. Check the contract, deposits, invoice, consideration and special attribution through the existing property Guide. **A particular property-credit period is not established here.** Check this point with one of our partner accountants.

**Process errors**

- Transactions processed outside accounts payable or accounts receivable and never captured in the GST control accounts.
- Incorrect default GST codes in the accounting file after a chart of accounts change.
- Not reconciling the GST control accounts to the BAS at all.
- Failing to recognise an adjustment event, such as a settlement discount taken by a customer.

**Threshold and registration errors**

- Registration: the original $75,000 / 21-day shortcut is not a complete test. Under GST Act ss 23-5, 25-1 and 188-10, consider the enterprise, current/projected GST turnover, statutory exclusions and special registration rules. Apply the existing GST Guide before deciding when an entity must register; 21 days runs after becoming required, not merely after a cash-sales counter passes a figure. [GST Act](https://www.legislation.gov.au/C2004A00446/2026-01-01/2026-01-01/text/original/epub/OEBPS/document_1/document_1.html).
- Monthly elections: the ordinary withdrawal date cannot be earlier than 12 months after the **election took effect**, and must be an allowed quarter-start date; the turnover restriction still applies. The Commissioner can revoke earlier on approved-form request under s 27-22, subject to its conditions. Do not measure the 12 months from business commencement. [GST Act ss 27-20/22](https://www.legislation.gov.au/C2004A00446/2026-01-01/2026-01-01/text/original/epub/OEBPS/document_1/document_1.html).

**PAYG errors**

- Reporting superannuation contributions at W1.
- Entering the instalment rate at 5A instead of the calculated instalment.
- Varying an instalment down without support, then falling under the 85% threshold.

[ATO, Managing GST in your business](https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/in-detail/managing-gst-in-your-business)

## Section 12 - Self-checks

Before lodging, confirm:

- [ ] The period, the entity and the ABN on the statement match the records used.
- [ ] Every business bank account is reconciled to the period end.
- [ ] The GST opening-to-closing bridge and period transaction listing reconcile to the BAS.
- [ ] G1 agrees with total sales per the profit and loss, after basis and exclusion differences.
- [ ] The G1 GST-inclusive or GST-exclusive choice is indicated and matches the figure entered.
- [ ] 1A and 1B include every adjustment for the period and no corrections that are out of time.
- [ ] Where W1 and W2 reporting is required, the amounts reconcile to the payroll register and relevant STP figures for the period.
- [ ] Where these labels apply, W5 equals W2 plus W3 plus W4, and label 4 equals W5. Large withholders follow Section 6.1 instead.
- [ ] 5A comes from T7 or varied T9 (zero if nil/negative), or rate-method T11 = T1 × T2/T3 as applicable; any eligible 5B credit is positive.
- [ ] 8A less 8B equals label 9, recalculated independently.
- [ ] Any correction of a prior period error is within its time and value limits.
- [ ] Suspense and clearing accounts are nil or fully explained.
- [ ] The due date has been identified, including any electronic or agent concession.

## Sources

Read/reuse scope on 27 November 2026: the operative GST Act attribution, credit evidence/time limits, adjustments, return and electronic-lodgment provisions; RCTI ss 6–9; correcting-errors ss 4, 6–8; substantive ATO label, method, adjustment, evidence and revision sections. Unchanged completed GST cycle, deadline and PAYG reads and exact quotes are reused from the companion Guide's proof of 27 November, with applicability checked. Direct ATO access blocks and the register's direct-fetch challenge page were not counted as law reads; substantive official indexed text was read. The historical 16 September 2026 source stamp and 21 October 2026 draft check are provenance only, not a current source read.

| Source | Provisions or content used | Read / applicable completed read reused |
| --- | --- | --- |
| [GST Act, volume 1](https://www.legislation.gov.au/C2004A00446/2026-01-01/2026-01-01/text/original/epub/OEBPS/document_1/document_1.html) | ss 11-5/15/25, 19-10/70/80, 21-5, 23-5, 25-1, 27-5 to 27-22, 29-5/10/20/25/39/80, 31-5/25, 35-5, 93-5/10 | Read 2026-11-27 |
| [GST Act, volume 2](https://www.legislation.gov.au/C2004A00446/2026-01-01/2026-01-01/text/original/epub/OEBPS/document_2/document_2.html) | ss 129-90, 151-5 and 188-10; special-rule dependencies | Read 2026-11-27 |
| [GST regulations](https://www.legislation.gov.au/F2019L00417/2025-11-01/2025-11-01/text/original/pdf) | regs 23-15.01/02 and 29-80.01/02, operative text read | Read 2026-11-27 |
| [TAA Schedule 1](https://www.legislation.gov.au/C1953A00001/2025-07-01/2025-07-01/text/original/epub/OEBPS/document_2/document_2.html) | PAYG instalment liability and ss 45-230/232; completed operative quotes reused | Read 2026-11-27 |
| [RCTI determination](https://www.legislation.gov.au/F2023L00785/asmade/2023-06-14/text/original/epub/OEBPS/document_1/document_1.html) | ss 6–9, current document and agreement requirements | Read 2026-11-27 |
| [Correcting GST Errors Determination](https://www.legislation.gov.au/F2023L01284/asmade/2023-09-25/text/original/pdf) | definitions and all ss 6–8 conditions, five turnover bands | Read 2026-11-27 |
| [ATO GST reporting methods](https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/business-activity-statements-bas/goods-and-services-tax-gst/gst-reporting-methods) and [annual reporting](https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/when-and-how-to-report-and-pay-gst/annual-gst-reporting) | Simpler/full method and qualified annual election | Read 2026-11-27 |
| [ATO bookkeeping guide](https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/business-activity-statements-bas/goods-and-services-tax-gst/simpler-bas-gst-bookkeeping-guide) | exclusions and transaction classification cautions | Read 2026-11-27 |
| [ATO summary](https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/completing-your-bas-for-gst/complete-your-bas/step-5-summary) and [adjustments](https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/completing-your-bas-for-gst/making-adjustments-on-your-activity-statements/how-to-make-adjustments) | G9/G20 transfers and accounts-method adjustment labels | Read 2026-11-27 |
| [ATO tax invoices](https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/tax-invoices) and [draft GSTR 2026/D2](https://www.ato.gov.au/law/view/document?DocID=DGS%2FGSTR2026D2%2FNAT%2FATO%2F00001) | Peppol conditions; draft status and old-authority transition, not withdrawal-day proof | Read 2026-11-27 |
| [ATO PAYG withholding](https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/business-activity-statements-bas/pay-as-you-go-payg-withholding) | W-label content and large-withholder exceptions, completed quotes reused | Read 2026-11-27 |
| [ATO PAYG statement instructions](https://www.ato.gov.au/forms-and-instructions/payg-instalments-how-to-complete-your-activity-statement) and [variation](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/payg-instalments/how-to-vary-your-payg-instalments) | T-label mapping, zero/credit entry and variation deadlines, completed quotes reused | Read 2026-11-27 |
| [ATO types of GST errors](https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/completing-your-bas-for-gst/correcting-gst-errors/types-of-gst-errors) and [revision](https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/fix-a-mistake-or-amend-your-tax-return/correct-an-activity-statement/revising-an-earlier-activity-statement) | review periods, source conflict and revision treatment | Read 2026-11-27 |
| [ATO due dates](https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/business-activity-statements-bas/due-dates-for-lodging-and-paying-your-bas) and [lodgment options](https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/business-activity-statements-bas/how-to-lodge-your-bas) | standard cycles, concessions, payment and authorised channels | Read 2026-11-27 |
| [ATO hire purchase/leasing](https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/in-detail/rules-for-specific-transactions/agent-consignment-and-progressive-transactions/gst-hire-purchase-and-leasing) | distinction from the withdrawn blanket timing rule | Read 2026-11-27 |

Not yet confirmed: **non-usable** specific withdrawal day, equality/partial-excess correction entitlement, director-penalty outcome, car/special-classification outcomes, and particular lease/hire/property attribution. Each is expressly held above with the partner-accountant sentence. Original inputs and dates remain for review; none is presented as a filing conclusion.

## Section 14 - Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional in the relevant jurisdiction before lodging or acting upon them.

> Contributed by Ryan Duguid.
