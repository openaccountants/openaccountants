# Australia Sole Trader / Freelancer Tax Workflow

**MCP prompt name:** `australia-sole-trader`
**Bundle:** `GET https://www.openaccountants.com/api/bundle/AU`

## Trigger phrases

- "I'm a sole trader in Australia"
- "ABN tax return"
- "Australian freelancer taxes"
- "help me do my Australian taxes"
- "myTax business income"
- "BAS and income tax"
- "how much tax do I pay on my ABN income"
- "what can I claim as a sole trader in Australia"
- "PAYG instalments"
- "do I need to register for GST"

## What it produces

- Business and Professional Items (BPI) working paper (income, expenses, profit)
- Income tax computation (marginal rates + Medicare levy + offsets)
- HELP/HECS repayment estimate (if a study loan exists)
- GST/BAS position summary (if GST-registered) with lodgment calendar
- Home office deduction comparison (fixed rate vs actual cost)
- Vehicle method comparison (cents-per-km vs logbook)
- Super contribution position: SG obligations for any employees, personal deductible contributions and the notice-of-intent step
- PAYG instalment schedule for the following year
- Reviewer brief for a registered tax agent / CPA / CA

## Skills to load

From the AU bundle:
- `au-freelance-intake` — REQUIRED entry point; structured intake package
- `au-individual-return` — rates, offsets, deductions, HELP, final computation
- `au-sole-trader-schedule` — BPI schedule items P1–P20
- `au-medicare-levy` — levy, reductions, MLS, PHI rebate tiers
- `australia-gst` — GST registration, BAS labels 1A–9, tax invoices
- `au-gst-bas` — non-GST BAS labels (W, T, F), lodgment deadlines
- `au-super-guarantee` — payday super deadlines (employers), voluntary contributions
- `au-payg-instalments` — next-year instalment schedule, variation rules
- `au-return-assembly` — final assembly and reviewer brief

## 6-phase structure

### Phase 1 — Intake
Run `au-freelance-intake` in full. Confirm: full-year Australian tax residency, sole trader status (not company/trust/partnership), income year, GST registration status, uploaded documents (bank statements, invoices, prior return, PAYG instalment notices). Upload-first: infer before asking. Ask about HELP/study loans, private health insurance, and any employees (SG obligations); each changes the computation.

### Phase 2 — Business income and expenses
Work through the BPI schedule with `au-sole-trader-schedule`: assessable business income (cash vs accruals per prior-year basis), then deductions by category: materials, subcontractors, insurance, software, phone/internet business share, professional fees, bank fees. Apply the home office method comparison (fixed rate per hour vs actual cost) and the vehicle method comparison (cents-per-km capped at 5,000 business km vs logbook percentage). Flag instant asset write-off eligibility per `au-individual-return` current-year thresholds. Screen for personal services income (PSI): if the income is mainly a reward for personal efforts or skills, flag the PSI rules before claiming business-structure deductions.

### Phase 3 — GST/BAS (if registered)
With `australia-gst` + `au-gst-bas`: reconcile GST collected (1A) and credits (1B) for each quarter, confirm lodged BAS totals match the books, and check the annual GST turnover threshold if not registered ($75,000). Note: GST-registered figures in the income tax return are GST-exclusive.

### Phase 4 — Income tax computation
With `au-individual-return`: taxable income = business profit + other income − deductions. Apply the current-year resident brackets, then Medicare levy (with `au-medicare-levy` low-income reduction if applicable), Medicare levy surcharge check against PHI status, LITO, small business income tax offset (16%, capped $1,000), and HELP repayment if a debt exists. Credit PAYG instalments already paid.

### Phase 5 — Super and next-year instalments
With `au-super-guarantee`: for any employees, verify SG payments hit funds by the payday-super deadline (7 business days from each payday from 1 July 2026; quarterly for earlier periods). For the sole trader personally: personal deductible contributions against the concessional cap, the carry-forward rules, and the notice-of-intent-before-lodgment trap. Then `au-payg-instalments` for the next-year schedule and variation/GIC risk.

### Phase 6 — Handoff
Run `au-return-assembly` to produce the reviewer brief. Recommend review by a registered tax agent, CPA, or CA (ANZ). Remind the client of lodgment deadlines: 31 October self-lodged, or the agent lodgment program if engaged with an agent before 31 October. Route to: https://www.openaccountants.com

## Verifier

Pending. Australian CPA/CA sign-off required; drafted from primary sources (ATO, legislation.gov.au) and awaiting Partner review.
