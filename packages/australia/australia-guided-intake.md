---
name: au-freelance-intake
description: ALWAYS USE THIS SKILL when a user asks for help preparing their Australian tax returns AND mentions freelancing, self-employment, contracting, sole trading, or ABN-based work. Trigger on phrases like "help me do my taxes", "prepare my ITR", "I'm a sole trader in Australia", "I'm a freelancer in Australia", "do my taxes as a contractor", "prepare my BAS and income tax", or any similar phrasing where the user is an Australian-resident self-employed individual needing tax return preparation. This is the REQUIRED entry point for the Australian self-employed tax workflow -- every other skill in the stack (australia-gst, au-individual-return, au-super-guarantee, au-medicare-levy, au-payg-instalments, au-return-assembly) depends on this skill running first to produce a structured intake package. Uses upload-first workflow -- the user dumps all their documents and the skill infers as much as possible before asking questions. Uses ask_user_input_v0 for structured questions instead of one-at-a-time prose. Built for speed. Australian full-year residents only; sole traders only.
version: 0.1
---

# Australia Sole Trader Intake Skill v0.1

## What this file is

The intake orchestrator for Australian-resident sole traders. Every downstream Australian content skill (australia-gst, au-individual-return, au-super-guarantee, au-medicare-levy, au-payg-instalments) and the assembly orchestrator (au-return-assembly) depend on this skill running first to produce a structured intake package.

This skill does not compute any tax figures. Its job is to collect all the facts, parse all the documents, confirm everything with the user, and hand off a clean intake package to `au-return-assembly`.

---

## Design principles

v0.1 follows the same upload-first, inference-then-confirm pattern as mt-freelance-intake v0.1:

1. **Compact refusal sweep** using `ask_user_input_v0` -- 3 interactive questions, ~30 seconds.
2. **Upload-first workflow** -- after the refusal check, the user dumps everything they have.
3. **Inference pass** -- Claude parses every document and extracts as much as possible.
4. **Gap-filling only** -- Claude asks the user ONLY about what is missing, ambiguous, or needs confirmation.
5. **Single confirmation pass** at the end -- show the full picture, let the user correct anything wrong, hand off to downstream skills.

Target: intake completes in 5 minutes for a prepared user, 15 minutes for a user who has to go fetch documents.

## Critical operating principles

**Do not narrate the workflow.** Do not say "Phase 1," "Phase 2," "Now I'll ask you about deductions." Just do the work.

**Do not ask questions that have already been answered.** If the refusal check established the user is GST registered, do not later ask about GST status. Track what is known.

**Do not ask about things visible in uploaded documents.** If the bank statement shows quarterly BAS payments to the ATO, do not ask "did you lodge BAS." Confirm what you see, do not re-ask.

**Use `ask_user_input_v0` for any multiple-choice question.** Text input is only for genuinely open-ended data (names, addresses, specific amounts when they cannot be inferred).

**Prefer batching.** Ask 3 related questions in a single message when they do not depend on each other's answers.

**Be terse but complete.** No hedging, no "let me know if you have questions," no "I hope this helps."

**Exception for blocking decisions.** If a single question determines whether the user is in-scope or out-of-scope, ask it standalone.

---

## Section 1 -- The opening

When triggered, respond with ONE message that:

1. One-line greeting (no paragraph of expectation-setting)
2. One-line summary of the flow (scope check -> upload -> gaps -> handoff to return assembly)
3. One-line reviewer reminder (must be reviewed by registered tax agent before filing)
4. Launch the refusal sweep immediately using `ask_user_input_v0`

**Example first message:**

> Let's get your 2025 Australian returns ready. Quick scope check, then you upload your documents, then I fill in the gaps. Target time: 10 minutes.
>
> Reminder: everything I produce needs to be reviewed and signed off by a registered tax agent before you lodge anything with the ATO. I'm not a substitute for review.
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

Present the refusal sweep as a single `ask_user_input_v0` call with 3 questions, all single-select.

**The 3 questions to ask first:**

```
Q1: "Australian residency in 2024-25?"
    Options: ["Full year", "Part year", "Did not live in Australia"]

Q2: "Business structure?"
    Options: ["Sole trader (ABN in your name)", "Partnership", "Company (Pty Ltd)", "Trust", "Not sure"]

Q3: "Do you have an ABN?"
    Options: ["Yes", "No", "Applied but not yet received"]
```

**After the response, evaluate:**

- **Q1 = Full year** -> continue
- **Q1 = Part year or did not live in Australia** -> stop. "I'm set up for full-year Australian residents only. Part-year or non-residents have different rules around foreign income and dual residency. You need a registered tax agent who handles non-resident returns."

- **Q2 = Sole trader** -> continue
- **Q2 = Partnership** -> stop. "Partnerships lodge a separate partnership return and distribute income to partners. You need a registered tax agent familiar with partnership returns."
- **Q2 = Company (Pty Ltd)** -> stop. "I don't cover company returns. Companies lodge a separate company tax return with different rules. You need a registered tax agent."
- **Q2 = Trust** -> stop. "Trust returns have separate distribution and reporting requirements. You need a registered tax agent familiar with trust returns."
- **Q2 = Not sure** -> ask one follow-up: "Do you operate under your own name (or a registered business name) with an individual ABN? Or do you have a registered company with ASIC? If you invoice under your own ABN, you're a sole trader. If you have an ACN and Pty Ltd, you're a company."

- **Q3 = Yes** -> continue
- **Q3 = No** -> stop. "You need an ABN to operate as a sole trader. Apply at abr.gov.au. Once you have your ABN, come back and we can prepare your returns."
- **Q3 = Applied but not yet received** -> continue with a flag: ABN pending, will need to confirm before lodging.

**After Q1-Q3 pass, ask the second batch of scope questions (also batched):**

```
Q4: "GST registered?"
    Options: ["Yes (turnover above $75K or voluntarily registered)", "No (turnover under $75K)", "Not sure"]

Q5: "Marital / dependant status?"
    Options: ["Single no dependants", "Single with dependants", "Married / de facto no dependants", "Married / de facto with dependants"]

Q6: "Industry?"
    Options: ["Software / tech / IT services", "Professional services (accounting, legal, consulting)", "Trades (construction, electrical, plumbing)", "Creative (design, media, photography)", "Other"]
```

**Evaluate Q4:**
- **Yes** -> continue. Standard quarterly BAS lodgement.
- **No** -> continue. No BAS required unless turnover crosses $75K threshold. Will check after inference.
- **Not sure** -> ask one follow-up: "Do you charge GST on your invoices (i.e., your prices include a 10% GST component)? If yes, you're registered. If your invoices say 'no GST' or you've never dealt with BAS, you're likely not registered. Check your ABN registration at abr.gov.au."

**Evaluate Q5:**
- All options -> note for Medicare levy surcharge and tax offset calculations. Continue.

**Evaluate Q6:**
- All options -> note for expense classification context. Continue.

**Total time:** ~45 seconds if the user taps through.

---

## Section 3 -- The dump

Once the refusal sweep passes, immediately ask for the document dump. Single message. No preamble.

**Example:**

> Scope is good. Now upload everything you have for 2024-25 -- drop it all in at once:
>
> - Business bank statement(s) for all of 2024-25 (1 July 2024 - 30 June 2025) (CSV or PDF)
> - Sales invoices issued in 2024-25
> - Purchase invoices / receipts for business expenses
> - Prior year tax return (2023-24 ITR, or at least last year's notice of assessment)
> - PAYG payment summary / income statement from any employer (if also employed)
> - Private health insurance statement (from your insurer)
> - HELP/HECS statement (if applicable)
> - BAS lodgements for 2024-25 (if GST registered)
> - Superannuation statements (personal contributions)
> - Motor vehicle logbook (if claiming vehicle expenses)
> - Any ATO correspondence or notices
> - Anything else tax-related you have
>
> Don't worry about labeling or organizing -- I'll figure out what each file is. Drag and drop when ready.

Then wait. Do not ask any other questions while waiting.

**If the user uploads a partial dump and says "that's what I have":** move to inference. Do not demand more. Request specific missing items during gap-filling.

**If the user says "I don't know what I have":** Switch to guided mode:
> Check these places:
> - Business bank: download 2024-25 statements as PDF or CSV (1 July 2024 - 30 June 2025)
> - myGov / ATO online: download income statement, prior returns, NOA
> - Email: search for "invoice", "BAS", "ATO", "super", "health insurance"
> - Your health insurer's portal: download the annual tax statement
> - Your super fund's portal: download the annual statement
> - Your accountant from last year, if you had one
> - Dropbox / Google Drive for saved invoices
>
> Come back when you have something to upload. I'll work with whatever you bring.

---

## Section 4 -- The inference pass

When documents arrive, parse each one. For each document, extract:

**Bank statement:**
- Total deposits (candidate gross receipts)
- Recurring inflows (client payments with names)
- Outflows to ATO (PAYG instalment payments with dates)
- Outflows to ATO (BAS/GST payments with dates)
- Outflows to super funds (personal super contributions with dates and amounts)
- Outflows to suppliers (business expenses by category)
- Equipment purchases (potential instant asset write-off or depreciation items)
- Transfers to personal account (owner draws)
- Any rent payments (potential home office or business premises)
- SaaS / software subscriptions
- Professional memberships
- Insurance payments (PI, motor, income protection)

**Sales invoices:**
- Client names and amounts
- Whether GST was charged (registered indicator)
- Whether invoices say "no GST" (unregistered indicator)
- Total turnover reconciliation against bank deposits
- Any foreign clients (withholding tax implications)

**Purchase invoices / receipts:**
- Expense category (revenue, capital)
- GST amount on each (claimable input tax credit for GST registered)
- Any items eligible for instant asset write-off (under $20,000 threshold for 2024-25)
- Any items that must be depreciated (above threshold or excluded assets)
- Any blocked categories (entertainment, personal, non-deductible fines/penalties)

**Prior year ITR / Notice of Assessment:**
- Prior year taxable income (drives PAYG instalment calculation)
- Prior year tax liability
- Prior year capital allowances / depreciation schedule
- Any carried-forward losses
- PAYG instalment rate or amount from NOA

**PAYG payment summary / income statement:**
- Gross salary/wages from employment (if also employed)
- Tax withheld by employer
- Reportable fringe benefits
- Reportable super contributions

**Private health insurance statement:**
- Insurer name
- Level of cover (hospital, extras, combined)
- Days covered
- PHI rebate tier (age-based)
- Whether rebate was claimed as a premium reduction or will be claimed on the return

**HELP/HECS statement:**
- Outstanding HELP debt balance
- Compulsory repayment income threshold

**BAS lodgements:**
- Quarterly GST collected (1A)
- Quarterly GST paid (1B)
- PAYG instalment amounts
- Net GST position per quarter

**Super statements:**
- Concessional contributions (employer + salary sacrifice + personal deductible)
- Non-concessional contributions
- Total super balance (for Division 293 check if income + super > $250K)

**After parsing everything, build an internal inference object.** Do not show the raw inference yet -- transform it into a compact summary for the user in Section 5.

---

## Section 5 -- The confirmation

After inference, present a single compact summary message. Use a structured format that is fast to scan. Invite the user to correct anything wrong.

**Example summary message:**

> Here's what I pulled from your documents. Skim and tell me what's wrong.
>
> **Identity**
> - Jane Smith, single no dependants
> - Full-year Australian resident (Sydney, NSW)
> - Sole trader, ABN 12 345 678 901
> - GST registered
>
> **Business Income (from bank statement + invoices)**
> - Gross business income (ex-GST): ~$95,000
>   - TechCorp Pty Ltd: $48,000 (monthly retainer)
>   - DesignHub: $30,000 (project work)
>   - Various smaller clients: $17,000
> - GST collected (10%): ~$9,500
>
> **Employment Income (from PAYG summary)**
> - None (fully self-employed)
>
> **Expenses (from bank statement + purchase invoices)**
> - Software / SaaS subscriptions: $2,400
> - Professional insurance: $1,200
> - Accounting fees: $1,500
> - Phone / internet: $1,800 (TBD -- need business use %)
> - Motor vehicle: $4,200 fuel + maintenance (TBD -- method and business use %)
> - Equipment: MacBook Pro $3,200 (Nov 2024) -- instant asset write-off eligible (under $20K)
> - GST credits on purchases: ~$1,100 (claimable)
>
> **Super Contributions (from super statement)**
> - Personal deductible contributions: $8,000
> - Concessional cap remaining: $22,000 (of $30,000 cap)
>
> **PAYG Instalments (from BAS)**
> - Q1 instalment: $1,200
> - Q2 instalment: $1,200
> - Q3 instalment: $1,200
> - Q4 instalment: $1,200
> - Total PAYG instalments paid: $4,800
>
> **Private Health Insurance (from insurer statement)**
> - Combined hospital + extras, full year cover
> - Rebate tier: Base tier (under 65, income under $97K single -- TBD after final taxable income)
> - Rebate claimed as premium reduction
>
> **HELP Debt**
> - Outstanding balance: $18,500
> - Compulsory repayment will depend on repayment income
>
> **Flags I already see:**
> 1. Phone / internet -- need business use percentage
> 2. Motor vehicle -- need method (cents-per-km or logbook) and business use %
> 3. MacBook Pro $3,200 -- eligible for instant asset write-off under $20K threshold
> 4. Super contributions well within $30K concessional cap -- no excess issue
> 5. PHI rebate tier may shift depending on final taxable income
> 6. HELP compulsory repayment to be calculated from repayment income
>
> **Is any of this wrong? Reply "looks good" or tell me what to fix.**

---

## Section 6 -- Gap filling

After the user confirms the summary (or corrects it), ask about things that cannot be inferred from documents. Use `ask_user_input_v0` where possible.

**Things that usually cannot be inferred:**

1. **Home office** -- Cannot tell from documents whether a dedicated workspace exists and which method is used.
2. **Private use percentage** -- Phone, internet, motor vehicle business-use split.
3. **Motor vehicle method** -- Cents-per-km (max 5,000 km) or logbook method.
4. **Instant asset write-off items** -- Confirm any assets purchased are used for business and eligible.
5. **PHI tier** -- May need confirmation if income is near a tier boundary.
6. **HELP repayment plan** -- Confirm outstanding balance.
7. **Other income** -- Interest, dividends, rental, capital gains.

**Home office gap-filling example:**

Call `ask_user_input_v0` with:

```
Q: "Home office claim method?"
   Options: [
     "Fixed rate method (67c/hr) -- I track hours worked from home",
     "Actual cost method -- I have records of running expenses and floor area",
     "I work from a separate business premises (not home)",
     "I don't work from home",
     "Not sure which method"
   ]
```

If option 1 -> ask for total hours worked from home during 2024-25 (text input).
If option 2 -> flag as complex: actual cost method requires detailed records of electricity, gas, internet, phone, depreciation of furniture. Ask for floor area percentage of dedicated workspace.
If option 3 -> rent is already captured in expenses. No home office calculation needed.
If option 4 -> skip home office entirely.
If option 5 -> recommend fixed rate method (67c/hr) as simpler. Ask for hours.

Note: The 2024-25 rate is 67 cents per hour (revised rate effective 1 July 2022). This replaces the old 52c/hr method.

**Motor vehicle gap-filling example:**

Call `ask_user_input_v0` with:

```
Q: "Motor vehicle method?"
   Options: [
     "Cents-per-km (85c/km, max 5,000 business km)",
     "Logbook method (I kept a logbook for 12+ weeks)",
     "No vehicle used for business"
   ]
```

If option 1 -> ask for estimated business kilometres driven in 2024-25 (max 5,000). Rate is 85 cents/km for 2024-25.
If option 2 -> ask for logbook business-use percentage and total car expenses.
If option 3 -> skip vehicle entirely.

Flag all private-use percentages as T2 -- registered tax agent must confirm the percentage is reasonable and documented.

**Other income:**

Call `ask_user_input_v0` with:

```
Q: "Any other income in 2024-25?"
   Options: [
     "Interest income (bank accounts)",
     "Dividend income (shares)",
     "Rental income (investment property)",
     "Capital gains (sold shares, crypto, property)",
     "None of the above",
     "Multiple of the above"
   ]
```

If any selected -> ask for amounts as text input. Flag rental income and capital gains as potentially out of scope for this workflow (complex supplementary schedules).

---

## Section 7 -- The final handoff

Once gap-filling is done, produce a final handoff message and hand off to `au-return-assembly`.

**Example handoff message:**

> Intake complete. Here's what's going to the return assembly:
>
> Sole trader, single, GST registered, full-year Australian resident. Gross business income $95,000 (ex-GST), estimated net ~$78,000 before super deduction.
>
> I'm now going to run the full Australian return preparation. This covers:
> 1. BAS reconciliation (Q4 if outstanding, or full-year summary)
> 2. Individual tax return (ITR)
> 3. Super guarantee / voluntary contribution reconciliation
> 4. Medicare levy and surcharge calculation
> 5. PAYG instalment reconciliation and next-year schedule
>
> You'll get back:
> 1. An Excel working paper with all forms and live formulas
> 2. A reviewer brief with positions, citations, and flags for your tax agent
> 3. A filing calendar with all upcoming deadlines
>
> Starting now.

Then internally invoke `au-return-assembly` with the structured intake package.

---

## Section 8 -- Structured intake package (internal format)

The downstream skill (`au-return-assembly`) consumes a JSON structure. It is internal and not shown to the user unless they ask. Key fields:

```json
{
  "jurisdiction": "AU",
  "tax_year": "2024-25",
  "taxpayer": {
    "name": "",
    "date_of_birth": "",
    "marital_status": "single | single_dependants | married | married_dependants",
    "residency": "full_year",
    "abn": "",
    "tfn": "",
    "gst_registered": true,
    "employment_status": "self_employed | employed_plus_side",
    "industry": "",
    "entity_type": "sole_trader",
    "state": ""
  },
  "business_income": {
    "gross_income_ex_gst": 0,
    "gst_collected": 0,
    "client_breakdown": []
  },
  "employment_income": {
    "gross_salary": 0,
    "tax_withheld": 0,
    "reportable_fringe_benefits": 0,
    "reportable_super": 0
  },
  "other_income": {
    "interest": 0,
    "dividends": 0,
    "franking_credits": 0,
    "rental": 0,
    "capital_gains": 0
  },
  "expenses": {
    "fully_deductible": [],
    "mixed_use": [],
    "blocked": [],
    "instant_asset_writeoff": [],
    "depreciating_assets": []
  },
  "gst": {
    "quarterly_bas_lodged": [],
    "gst_collected_total": 0,
    "gst_credits_total": 0,
    "net_gst_position": 0
  },
  "super": {
    "personal_deductible_contributions": 0,
    "employer_contributions": 0,
    "salary_sacrifice": 0,
    "total_concessional": 0,
    "concessional_cap": 30000,
    "non_concessional": 0,
    "total_super_balance": 0
  },
  "payg_instalments": {
    "instalment_rate": 0,
    "quarterly_amounts": [],
    "total_paid": 0,
    "prior_year_noa_rate": 0
  },
  "phi": {
    "has_phi": false,
    "cover_type": "",
    "days_covered": 0,
    "rebate_tier": "",
    "rebate_claimed_as_reduction": false
  },
  "help": {
    "has_help_debt": false,
    "outstanding_balance": 0
  },
  "home_office": {
    "method": "fixed_rate | actual_cost | none",
    "hours_worked_from_home": 0,
    "rate_per_hour": 0.67,
    "floor_area_pct": 0
  },
  "motor_vehicle": {
    "method": "cents_per_km | logbook | none",
    "business_km": 0,
    "rate_per_km": 0.85,
    "logbook_business_pct": 0,
    "total_car_expenses": 0
  },
  "prior_year": {
    "taxable_income": 0,
    "tax_liability": 0,
    "carried_forward_losses": 0,
    "depreciation_schedule": []
  },
  "open_flags": [],
  "refusals_triggered": [],
  "documents_received": []
}
```

---

## Section 9 -- Refusal handling

Refusals fire from either the refusal sweep (Section 2) or during inference (e.g., company structure discovered in documents).

When a refusal fires:
1. Stop the workflow
2. State the specific reason in one sentence
3. Recommend the path forward (specific practitioner type)
4. Offer to continue with partial help ONLY if the out-of-scope item is cleanly separable (rare)

**Do not:**
- Apologise profusely
- Try to work around the refusal
- Suggest the user "might be able to" fit into scope if they answer differently
- Continue silently

**Sample refusal:**

> Stop -- you have a registered Pty Ltd company. I'm set up for sole traders only. Companies lodge company tax returns with different rules for franking, dividends, and corporate tax rates. You need a registered tax agent familiar with company returns.
>
> I can't help with this one.

---

## Section 10 -- Self-checks

**Check IN1 -- No one-question-at-a-time prose in the refusal sweep.** If the skill asked "Question 1 of 10" or walked through questions as separate messages, check fails.

**Check IN2 -- Refusal sweep used ask_user_input_v0.** The first substantive interaction used the interactive tool, not prose questions.

**Check IN3 -- Upload-first flow honoured.** After refusal sweep, the skill asked for a document dump before asking any content questions.

**Check IN4 -- Documents were parsed and inferred before asking questions.** The inference summary (Section 5) was shown before gap-filling questions (Section 6).

**Check IN5 -- Gap-filling only asked about things NOT visible in documents.** If the skill asked "did you pay super" after the bank statement showed super fund payments, check fails.

**Check IN6 -- Open flags captured.** Anything ambiguous, risky, or attention-worthy during inference is in the `open_flags` list in the handoff package.

**Check IN7 -- Handoff to `au-return-assembly` is explicit.** The user was told "I'm now going to run the return preparation," and the downstream orchestrator was explicitly invoked with the intake package.

**Check IN8 -- Reviewer step was stated upfront and reiterated before handoff.** The opening message mentioned registered tax agent signoff.

**Check IN9 -- Refusals were clean.** No hedging. Stop means stop.

**Check IN10 -- No meta-commentary about workflow phases.** The skill did not say "Phase 1," "Phase 2," etc.

**Check IN11 -- Total user-facing turn count is low.** Target: 8 turns or fewer from start to handoff for a prepared user (1 refusal batch + 1 upload + 1 confirmation + 1-3 gap fills + 1 handoff). More than 12 turns for a normal intake is a check failure.

**Check IN12 -- GST registration status was established.** GST registered vs unregistered was confirmed before inference, as it changes how every transaction is classified.

---

## Section 11 -- Performance targets

For a prepared user (documents in a folder, ready to upload):
- **Refusal sweep**: 45 seconds (1-2 interactive turns)
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

**Outputs:** Structured intake package consumed by `au-return-assembly`.

**Downstream skills triggered (via au-return-assembly):**
- `australia-gst` -- BAS quarterly GST return
- `au-individual-return` -- Individual tax return (ITR)
- `au-super-guarantee` -- Super contributions reconciliation
- `au-medicare-levy` -- Medicare levy and surcharge
- `au-payg-instalments` -- PAYG instalment schedule

---

### Change log

- **v0.1 (April 2026):** Initial draft. Upload-first, inference-then-confirm pattern modelled on mt-freelance-intake v0.1.

## End of Intake Skill v0.1


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
