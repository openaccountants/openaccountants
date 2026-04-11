---
name: uk-freelance-intake
description: ALWAYS USE THIS SKILL when a user asks for help preparing their UK tax returns AND mentions freelancing, self-employment, sole trading, contracting, or side hustle income. Trigger on phrases like "help me do my UK taxes", "prepare my self-assessment", "I'm self-employed in the UK", "I'm a sole trader", "do my SA100", "prepare my tax return", or any similar phrasing where the user is a UK-resident self-employed individual needing tax return preparation. This is the REQUIRED entry point for the UK self-employed tax workflow -- every other skill in the stack (uk-vat-return, uk-self-employment-sa103, uk-income-tax-sa100, uk-national-insurance, uk-student-loan-repayment, uk-payments-on-account, uk-return-assembly) depends on this skill running first to produce a structured intake package. Uses upload-first workflow -- the user dumps all their documents and the skill infers as much as possible before asking questions. Uses ask_user_input_v0 for structured questions instead of one-at-a-time prose. Built for speed. UK full-year residents only; sole traders.
version: 0.1
---

# UK Self-Employed Intake Skill v0.1

## What this file is

The intake orchestrator for UK-resident sole traders. Every downstream UK content skill (uk-vat-return, uk-self-employment-sa103, uk-income-tax-sa100, uk-national-insurance, uk-student-loan-repayment, uk-payments-on-account) and the assembly orchestrator (uk-return-assembly) depend on this skill running first to produce a structured intake package.

This skill does not compute any tax figures. Its job is to collect all the facts, parse all the documents, confirm everything with the user, and hand off a clean intake package to `uk-return-assembly`.

---

## Design principles

v0.1 follows the same upload-first, inference-then-confirm pattern as mt-freelance-intake v0.1:

1. **Compact refusal sweep** using `ask_user_input_v0` -- 3-4 interactive questions, ~30 seconds.
2. **Upload-first workflow** -- after the refusal check, the user dumps everything they have.
3. **Inference pass** -- Claude parses every document and extracts as much as possible.
4. **Gap-filling only** -- Claude asks the user ONLY about what is missing, ambiguous, or needs confirmation.
5. **Single confirmation pass** at the end -- show the full picture, let the user correct anything wrong, hand off to downstream skills.

Target: intake completes in 5 minutes for a prepared user, 15 minutes for a user who has to go fetch documents.

## Critical operating principles

**Do not narrate the workflow.** Do not say "Phase 1," "Phase 2," "Now I'll ask you about deductions." Just do the work.

**Do not ask questions that have already been answered.** If the refusal check established the user is VAT registered, do not later ask about VAT status. Track what is known.

**Do not ask about things visible in uploaded documents.** If the bank statement shows quarterly VAT payments to HMRC, do not ask "are you VAT registered." Confirm what you see, do not re-ask.

**Use `ask_user_input_v0` for any multiple-choice question.** Text input is only for genuinely open-ended data (names, addresses, specific amounts when they cannot be inferred).

**Prefer batching.** Ask 3 related questions in a single message when they do not depend on each other's answers.

**Be terse but complete.** No hedging, no "let me know if you have questions," no "I hope this helps."

**Exception for blocking decisions.** If a single question determines whether the user is in-scope or out-of-scope, ask it standalone.

---

## Section 1 -- The opening

When triggered, respond with ONE message that:

1. One-line greeting (no paragraph of expectation-setting)
2. One-line summary of the flow (scope check -> upload -> gaps -> handoff to return assembly)
3. One-line reviewer reminder (must be reviewed by a chartered accountant before filing)
4. Launch the refusal sweep immediately using `ask_user_input_v0`

**Example first message:**

> Let's get your 2025/26 UK returns ready. Quick scope check, then you upload your documents, then I fill in the gaps. Target time: 10 minutes.
>
> Reminder: everything I produce needs to be reviewed and signed off by a chartered accountant or licensed tax adviser before you file anything with HMRC. I'm not a substitute for professional review.
>
> Scope check:

Then immediately call `ask_user_input_v0` with the refusal questions.

**Do NOT:**
- Write a welcome paragraph
- Explain the phases
- Ask "are you ready to start"
- List what documents you will eventually need
- Give a disclaimer beyond the one reviewer line

---

## Section 2 -- Refusal sweep (compact)

Present the refusal sweep as a single `ask_user_input_v0` call with 4 questions, all single-select.

**The 4 questions to ask first:**

```
Q1: "UK residency in 2025/26?"
    Options: ["Full year UK resident", "Part year", "Non-resident"]

Q2: "Business structure?"
    Options: ["Sole trader (self-employed individual)", "Limited company (Ltd)", "LLP / Partnership", "Not sure"]

Q3: "VAT registered?"
    Options: ["Yes -- standard VAT registered", "Yes -- Flat Rate Scheme", "Not VAT registered (below GBP 90,000 threshold)", "Not sure"]

Q4: "Employees?"
    Options: ["No employees", "1-5 employees", "More than 5 employees"]
```

**After the response, evaluate:**

- **Q1 = Full year** -> continue
- **Q1 = Part year or Non-resident** -> stop. "I'm set up for full-year UK residents only. Part-year or non-residents have split-year treatment or different sourcing rules. You need a chartered accountant who handles non-resident returns."

- **Q2 = Sole trader** -> continue
- **Q2 = Limited company (Ltd)** -> stop. "I don't cover corporate returns. Limited companies file CT600 returns with separate rules for directors' salaries and dividends. You need a chartered accountant."
- **Q2 = LLP / Partnership** -> stop. "Partnerships file SA800 partnership returns with profit-sharing arrangements. You need a chartered accountant familiar with partnership returns."
- **Q2 = Not sure** -> ask one follow-up: "Do you invoice clients in your own name and report income on your personal tax return? If so, you're a sole trader. If you have a company registered at Companies House, you're a Ltd. If you share profits with partners, you're in a partnership."

- **Q3 = Yes -- standard** -> continue. Quarterly VAT returns.
- **Q3 = Yes -- Flat Rate Scheme** -> continue with a flag: FRS percentage needed for the trade sector.
- **Q3 = Not VAT registered** -> continue with a flag: if turnover exceeds GBP 90,000 in a rolling 12-month period, registration is mandatory. Will check after inference.
- **Q3 = Not sure** -> ask one follow-up: "Do you charge VAT on your invoices? If yes, you're VAT registered. If your invoices show no VAT, you're likely not registered."

- **Q4 = No employees** -> continue
- **Q4 = 1-5** -> continue with a flag: PAYE obligations exist but are out of scope. Flag for chartered accountant review.
- **Q4 = More than 5** -> stop. "I'm set up for sole operators. With more than 5 employees, the PAYE and employment law complexity requires a dedicated chartered accountant."

**Total time:** ~30 seconds if the user taps through.

---

## Section 3 -- The dump

Once the refusal sweep passes, immediately ask for the document dump. Single message. No preamble.

**Example:**

> Scope is good. Now upload everything you have for 2025/26 (6 April 2025 to 5 April 2026) -- drop it all in at once:
>
> - Business bank statement(s) for the full tax year (CSV or PDF)
> - Sales invoices issued in 2025/26
> - Purchase invoices / receipts for business expenses
> - Prior year SA302 (tax calculation) or SA100 return
> - P60 or payslips (if you also have employment income)
> - Student loan statement (if applicable)
> - VAT returns filed during 2025/26 (if VAT registered)
> - Any HMRC correspondence or payment statements
> - Capital asset purchase receipts (computers, equipment, vehicles)
> - Anything else tax-related you have
>
> Don't worry about labeling or organizing -- I'll figure out what each file is. Drag and drop when ready.

Then wait. Do not ask any other questions while waiting.

**If the user uploads a partial dump and says "that's what I have":** move to inference. Do not demand more. Request specific missing items during gap-filling.

**If the user says "I don't know what I have":** Switch to guided mode:
> Check these places:
> - Business bank: download 2025/26 statements as PDF or CSV
> - Email: search for "invoice", "HMRC", "tax return", "P60", "student loan"
> - HMRC online account (gov.uk): download prior SA302, payment statements
> - Your accountant from last year, if you had one
> - Dropbox / Google Drive for saved invoices
> - Student Loans Company portal: download annual statement
>
> Come back when you have something to upload. I'll work with whatever you bring.

---

## Section 4 -- The inference pass

When documents arrive, parse each one. For each document, extract:

**Bank statement:**
- Total deposits (candidate gross turnover)
- Recurring inflows (client payments with names)
- Outflows to HMRC (Self Assessment payments with dates -- payments on account + balancing payment)
- Outflows to HMRC (VAT payments with dates)
- Outflows to suppliers (business expenses by category)
- Equipment purchases (potential capital allowances)
- Transfers to personal account (drawings)
- Any rent payments (business premises or potential use of home)
- SaaS / software subscriptions
- Professional memberships (ICAS, ICAEW, CIMA, etc.)
- Insurance payments (PI, motor, etc.)
- Telephone / broadband payments
- Motor vehicle expenses (fuel, maintenance, insurance)

**Sales invoices:**
- Client names and amounts
- Whether VAT was charged (VAT registration indicator)
- Total turnover reconciliation against bank deposits
- Any non-UK clients (reverse charge / outside scope of UK VAT)
- CIS deductions shown (Construction Industry Scheme -- flag)

**Purchase invoices / receipts:**
- Expense category (revenue, capital, disallowable)
- VAT amount on each (reclaimable if VAT registered)
- Any items qualifying for Annual Investment Allowance (AIA)
- Any disallowable categories (entertainment, non-business)

**Prior year SA302 / SA100:**
- Prior year total tax liability (drives payments on account)
- Prior year net self-employment income
- Prior year capital allowances schedule
- Prior year payments on account made
- Any balancing payment or refund

**P60 / payslips (if also employed):**
- Gross employment income
- Tax deducted via PAYE
- NIC deducted (Class 1)
- Tax code used
- Student loan deductions via PAYE

**Student loan statement:**
- Plan type (Plan 1, Plan 2, Plan 4, Plan 5, Postgraduate)
- Outstanding balance
- Repayments made via PAYE (if employed)

**VAT returns:**
- Quarterly turnover and VAT collected (output tax)
- Input VAT claimed
- Flat Rate Scheme percentage applied (if FRS)
- Any VAT owed / refund per quarter

**After parsing everything, build an internal inference object.** Do not show the raw inference yet -- transform it into a compact summary for the user in Section 5.

---

## Section 5 -- The confirmation

After inference, present a single compact summary message. Use a structured format that is fast to scan. Invite the user to correct anything wrong.

**Example summary message:**

> Here's what I pulled from your documents. Skim and tell me what's wrong.
>
> **Identity**
> - Jane Smith, single
> - Full-year UK resident (Manchester)
> - Sole trader (freelance software developer)
> - VAT: standard registered (GB 123 4567 89)
>
> **Turnover (from bank statement + invoices)**
> - Gross turnover (ex-VAT): ~GBP 72,000
>   - TechCo Ltd: GBP 42,000 (monthly retainer)
>   - DesignHub: GBP 20,000 (project work)
>   - Various smaller clients: GBP 10,000
> - VAT collected (20%): ~GBP 14,400
> - Non-UK clients (outside scope): GBP 5,000
>
> **Expenses (from bank statement + purchase invoices)**
> - Software / SaaS: GBP 2,400
> - Professional insurance: GBP 600
> - Accountancy fees: GBP 900
> - Telephone / broadband: GBP 840 (TBD -- need business use %)
> - Motor vehicle: GBP 2,800 fuel + GBP 500 maintenance (TBD -- simplified expenses or actual costs?)
> - MacBook Pro GBP 1,800 (March 2026) -- capital item, AIA
> - Input VAT on purchases: ~GBP 1,500 (reclaimable)
>
> **Employment income (from P60)**
> - Gross employment income: GBP 15,000 (part-time role)
> - Tax deducted via PAYE: GBP 1,200
> - Class 1 NIC deducted: GBP 720
>
> **Student loan (from P60 + SLC statement)**
> - Plan 2, threshold GBP 27,295
> - GBP 400 repaid via PAYE
> - Additional repayment due on SA
>
> **Payments on account (from bank statement / SA302)**
> - 1st payment on account (31 Jan 2026): GBP 3,000
> - 2nd payment on account (31 Jul 2025): GBP 3,000
> - Total paid: GBP 6,000
>
> **Prior year (from 2024/25 SA302)**
> - 2024/25 total SA liability: GBP 8,500
> - 2024/25 net self-employment profit: GBP 48,000
> - Payments on account for 2025/26 based on 2024/25: GBP 4,250 x 2 = GBP 8,500
>
> **VAT (from VAT returns)**
> - Q1-Q3 2025/26 filed
> - Q4 outstanding (Jan-Mar 2026)
>
> **Flags I already see:**
> 1. Telephone / broadband -- need business use percentage
> 2. Motor vehicle -- simplified expenses (45p/mile) or actual costs?
> 3. MacBook Pro GBP 1,800 -- qualifies for AIA, full deduction in year of purchase
> 4. Q4 VAT return not yet filed -- will prepare as part of this workflow
> 5. Student loan Plan 2 -- additional repayment due via Self Assessment
> 6. Employment income present -- will need SA102 (employment supplement)
>
> **Is any of this wrong? Reply "looks good" or tell me what to fix.**

---

## Section 6 -- Gap filling

After the user confirms the summary (or corrects it), ask about things that cannot be inferred from documents. Use `ask_user_input_v0` where possible.

**Things that usually cannot be inferred:**

1. **Scottish taxpayer** -- Cannot tell from documents (address alone may not determine HMRC's view). Affects income tax rates (Scottish rates differ from rUK rates).
2. **Simplified expenses election** -- Whether the user uses HMRC simplified expenses for vehicles, use of home, or living at business premises.
3. **Cash basis** -- Whether the user uses cash basis accounting (default for most sole traders under GBP 150,000 turnover) or traditional accruals.
4. **Student loan plan** -- Plan type determines repayment threshold and rate.
5. **Use of home** -- Cannot tell from documents whether a home office is used. Simplified flat rate (GBP 10-26/month based on hours) or actual costs apportionment.
6. **Capital allowances from prior years** -- Continuing WDA on assets in the pool (unless prior SA103 has the schedule).
7. **Marriage Allowance** -- Whether transfer of GBP 1,260 personal allowance to/from spouse applies.
8. **Pension contributions** -- Personal pension payments not visible in business bank (relief at source or net pay).

**Scottish taxpayer:**

Call `ask_user_input_v0` with:

```
Q: "Scottish taxpayer?"
   Options: [
     "Yes -- my main home is in Scotland (Scottish income tax rates apply)",
     "No -- England, Wales, or Northern Ireland",
     "Not sure"
   ]
```

If yes -> Scottish rates apply: starter 19%, basic 20%, intermediate 21%, higher 42%, advanced 45%, top 48%.
If no -> rUK rates apply: basic 20%, higher 40%, additional 45%.
If not sure -> "Where is your main home? If it's in Scotland, Scottish rates apply. HMRC determines this based on your address."

**Simplified expenses:**

Call `ask_user_input_v0` with:

```
Q: "Motor vehicle expenses method?"
   Options: [
     "Simplified expenses (flat rate 45p/mile first 10,000, then 25p/mile)",
     "Actual costs (fuel, insurance, maintenance, depreciation -- need business use %)",
     "No vehicle used for business"
   ]
```

If simplified -> ask for total business miles driven in 2025/26.
If actual -> ask for total miles, business miles, and total vehicle costs. Compute business %.
If none -> skip.

**Use of home:**

Call `ask_user_input_v0` with:

```
Q: "Use of home for business?"
   Options: [
     "Simplified flat rate (GBP 10-26/month based on hours worked at home)",
     "Actual costs apportionment (proportion of rent/mortgage, utilities, broadband)",
     "Separate business premises (not at home)",
     "No home office claim"
   ]
```

If simplified -> ask for average hours per month worked at home. 25-50 hrs = GBP 10/month, 51-100 hrs = GBP 18/month, 101+ hrs = GBP 26/month.
If actual -> ask for total household costs and business use percentage.
If separate premises -> rent already captured in expenses.
If none -> skip.

**Cash basis:**

Call `ask_user_input_v0` with:

```
Q: "Accounting basis?"
   Options: [
     "Cash basis (record income when received, expenses when paid -- most sole traders)",
     "Traditional accruals basis (record income when earned, expenses when incurred)"
   ]
```

Cash basis is the default for sole traders with turnover under GBP 150,000. Most sole traders should use cash basis.

Flag all private-use percentages as T2 -- chartered accountant must confirm the percentage is reasonable and documented.

---

## Section 7 -- The final handoff

Once gap-filling is done, produce a final handoff message and hand off to `uk-return-assembly`.

**Example handoff message:**

> Intake complete. Here's what's going to the return assembly:
>
> Sole trader, single, VAT registered (standard), full-year UK resident (England). Turnover GBP 72,000, estimated net profit ~GBP 58,000 before capital allowances.
>
> I'm now going to run the full UK return preparation. This covers:
> 1. VAT return (Q4 2025/26)
> 2. SA103 self-employment pages (trading income)
> 3. SA100 main return (personal tax computation)
> 4. Class 2 + Class 4 National Insurance
> 5. Student loan repayment (if applicable)
> 6. Payments on account for 2026/27
>
> You'll get back:
> 1. An Excel working paper with all forms and live formulas
> 2. A reviewer brief with positions, citations, and flags for your accountant
> 3. A filing calendar with all upcoming deadlines
>
> Starting now.

Then internally invoke `uk-return-assembly` with the structured intake package.

---

## Section 8 -- Structured intake package (internal format)

The downstream skill (`uk-return-assembly`) consumes a JSON structure. It is internal and not shown to the user unless they ask. Key fields:

```json
{
  "jurisdiction": "UK",
  "tax_year": "2025/26",
  "taxpayer": {
    "name": "",
    "birth_year": 0,
    "marital_status": "single | married | civil_partner",
    "residency": "full_year",
    "scottish_taxpayer": false,
    "utr": "",
    "ni_number": "",
    "vat_number": "",
    "vat_status": "standard | flat_rate_scheme | unregistered",
    "flat_rate_pct": 0,
    "entity_type": "sole_trader",
    "industry": "",
    "accounting_basis": "cash | accruals"
  },
  "income": {
    "gross_turnover_ex_vat": 0,
    "vat_collected": 0,
    "outside_scope_income": 0,
    "employment_income": 0,
    "paye_tax_deducted": 0,
    "class1_nic_deducted": 0,
    "other_income": 0,
    "client_breakdown": []
  },
  "expenses": {
    "fully_deductible": [],
    "mixed_use": [],
    "disallowable": [],
    "capital_items": []
  },
  "vat": {
    "quarterly_returns_filed": [],
    "input_vat_reclaimable": 0,
    "flat_rate_scheme": false,
    "flat_rate_pct": 0
  },
  "student_loan": {
    "has_loan": false,
    "plan_type": "plan_1 | plan_2 | plan_4 | plan_5 | postgraduate",
    "repaid_via_paye": 0,
    "outstanding_balance": 0
  },
  "payments_on_account": {
    "prior_year_sa_liability": 0,
    "first_poa_paid": 0,
    "second_poa_paid": 0,
    "total_paid": 0
  },
  "prior_year": {
    "total_sa_liability": 0,
    "net_self_employment_profit": 0,
    "capital_allowances_pool": 0
  },
  "home_office": {
    "method": "simplified | actual | none",
    "hours_per_month": 0,
    "actual_costs": 0,
    "business_pct": 0,
    "annual_amount": 0
  },
  "private_use": {
    "motor_vehicle_method": "simplified | actual | none",
    "business_miles": 0,
    "motor_vehicle_business_pct": 0,
    "phone_business_pct": 0,
    "broadband_business_pct": 0
  },
  "pension": {
    "personal_contributions": 0,
    "relief_method": "relief_at_source | net_pay"
  },
  "marriage_allowance": {
    "transfer_to_spouse": false,
    "transfer_from_spouse": false
  },
  "open_flags": [],
  "refusals_triggered": [],
  "documents_received": []
}
```

---

## Section 9 -- Refusal handling

Refusals fire from either the refusal sweep (Section 2) or during inference (e.g., Ltd company discovered in documents).

When a refusal fires:
1. Stop the workflow
2. State the specific reason in one sentence
3. Recommend the path forward (specific practitioner type)
4. Offer to continue with partial help ONLY if the out-of-scope item is cleanly separable (rare)

**Do not:**
- Apologize profusely
- Try to work around the refusal
- Suggest the user "might be able to" fit into scope if they answer differently
- Continue silently

**Sample refusal:**

> Stop -- you have a registered limited company. I'm set up for sole traders only. Limited companies file CT600 returns with separate rules for corporation tax, directors' remuneration, and dividends. You need a chartered accountant familiar with Ltd company returns.
>
> I can't help with this one.

---

## Section 10 -- Self-checks

**Check IN1 -- No one-question-at-a-time prose in the refusal sweep.** If the skill asked "Question 1 of 10" or walked through questions as separate messages, check fails.

**Check IN2 -- Refusal sweep used ask_user_input_v0.** The first substantive interaction used the interactive tool, not prose questions.

**Check IN3 -- Upload-first flow honoured.** After refusal sweep, the skill asked for a document dump before asking any content questions.

**Check IN4 -- Documents were parsed and inferred before asking questions.** The inference summary (Section 5) was shown before gap-filling questions (Section 6).

**Check IN5 -- Gap-filling only asked about things NOT visible in documents.** If the skill asked "are you VAT registered" after the bank statement showed HMRC VAT payments, check fails.

**Check IN6 -- Open flags captured.** Anything ambiguous, risky, or attention-worthy during inference is in the `open_flags` list in the handoff package.

**Check IN7 -- Handoff to `uk-return-assembly` is explicit.** The user was told "I'm now going to run the return preparation," and the downstream orchestrator was explicitly invoked with the intake package.

**Check IN8 -- Reviewer step was stated upfront and reiterated before handoff.** The opening message mentioned chartered accountant signoff.

**Check IN9 -- Refusals were clean.** No hedging. Stop means stop.

**Check IN10 -- No meta-commentary about workflow phases.** The skill did not say "Phase 1," "Phase 2," etc.

**Check IN11 -- Total user-facing turn count is low.** Target: 8 turns or fewer from start to handoff for a prepared user (1 refusal batch + 1 upload + 1 confirmation + 1-3 gap fills + 1 handoff). More than 12 turns for a normal intake is a check failure.

**Check IN12 -- VAT status was established.** Standard vs FRS vs unregistered was confirmed before inference, as it changes how every transaction is classified.

**Check IN13 -- Scottish taxpayer status was established.** Determines which income tax rate table applies.

---

## Section 11 -- Performance targets

For a prepared user (documents in a folder, ready to upload):
- **Refusal sweep**: 30 seconds (1-2 interactive turns)
- **Document upload**: 2 minutes (1 upload turn)
- **Inference and confirmation display**: 1 minute Claude processing + 1 turn for user confirmation
- **Gap filling**: 2 minutes (2-3 interactive turns)
- **Handoff**: immediate
- **Total**: ~6 minutes

For an unprepared user (has to go fetch documents):
- Refusal sweep: same
- Document discovery: 10-20 minutes offline
- Rest: same
- **Total**: 15-25 minutes

---

## Section 12 -- Cross-skill references

**Inputs:** User-provided documents and answers.

**Outputs:** Structured intake package consumed by `uk-return-assembly`.

**Downstream skills triggered (via uk-return-assembly):**
- `uk-vat-return` -- VAT100 quarterly return (if VAT registered)
- `uk-self-employment-sa103` -- SA103 self-employment pages (trading income)
- `uk-income-tax-sa100` -- SA100 main return (personal tax computation)
- `uk-national-insurance` -- Class 2 + Class 4 NIC
- `uk-student-loan-repayment` -- Student loan repayment via Self Assessment (if applicable)
- `uk-payments-on-account` -- Payments on account for 2026/27

---

### Change log

- **v0.1 (April 2026):** Initial draft. Upload-first, inference-then-confirm pattern modelled on mt-freelance-intake v0.1.

## End of Intake Skill v0.1


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a chartered accountant, ACCA member, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
