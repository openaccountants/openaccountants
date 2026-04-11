---
name: ca-freelance-intake
description: ALWAYS USE THIS SKILL when a user asks for help preparing their Canadian tax returns AND mentions freelancing, self-employment, contracting, sole proprietorship, or unincorporated business. Trigger on phrases like "help me do my taxes", "prepare my T1", "I'm self-employed in Canada", "I'm a freelancer in Canada", "do my taxes as a contractor", "prepare my GST/HST return and income tax", or any similar phrasing where the user is a Canadian-resident self-employed individual needing tax return preparation. This is the REQUIRED entry point for the Canadian self-employed tax workflow -- every other skill in the stack (canada-gst-hst, ca-fed-t2125, ca-fed-t1-return, ca-fed-cpp-ei, ca-fed-instalments, ca-return-assembly) depends on this skill running first to produce a structured intake package. Uses upload-first workflow -- the user dumps all their documents and the skill infers as much as possible before asking questions. Uses ask_user_input_v0 for structured questions instead of one-at-a-time prose. Built for speed. Canadian full-year residents only; sole proprietors only (not incorporated).
version: 0.1
---

# Canada Sole Proprietor Intake Skill v0.1

## What this file is

The intake orchestrator for Canadian-resident sole proprietors. Every downstream Canadian content skill (canada-gst-hst, ca-fed-t2125, ca-fed-t1-return, ca-fed-cpp-ei, ca-fed-instalments) and the assembly orchestrator (ca-return-assembly) depend on this skill running first to produce a structured intake package.

This skill does not compute any tax figures. Its job is to collect all the facts, parse all the documents, confirm everything with the user, and hand off a clean intake package to `ca-return-assembly`.

---

## Design principles

v0.1 follows the same upload-first, inference-then-confirm pattern as mt-freelance-intake v0.1:

1. **Compact refusal sweep** using `ask_user_input_v0` -- 4 interactive questions, ~30 seconds.
2. **Upload-first workflow** -- after the refusal check, the user dumps everything they have.
3. **Inference pass** -- Claude parses every document and extracts as much as possible.
4. **Gap-filling only** -- Claude asks the user ONLY about what is missing, ambiguous, or needs confirmation.
5. **Single confirmation pass** at the end -- show the full picture, let the user correct anything wrong, hand off to downstream skills.

Target: intake completes in 5 minutes for a prepared user, 15 minutes for a user who has to go fetch documents.

## Critical operating principles

**Do not narrate the workflow.** Do not say "Phase 1," "Phase 2," "Now I'll ask you about deductions." Just do the work.

**Do not ask questions that have already been answered.** If the refusal check established the user is GST/HST registered, do not later ask about registration status. Track what is known.

**Do not ask about things visible in uploaded documents.** If the bank statement shows quarterly instalment payments to CRA, do not ask "did you pay instalments." Confirm what you see, do not re-ask.

**Use `ask_user_input_v0` for any multiple-choice question.** Text input is only for genuinely open-ended data (names, addresses, specific amounts when they cannot be inferred).

**Prefer batching.** Ask 3 related questions in a single message when they do not depend on each other's answers.

**Be terse but complete.** No hedging, no "let me know if you have questions," no "I hope this helps."

**Exception for blocking decisions.** If a single question determines whether the user is in-scope or out-of-scope, ask it standalone.

---

## Section 1 -- The opening

When triggered, respond with ONE message that:

1. One-line greeting (no paragraph of expectation-setting)
2. One-line summary of the flow (scope check -> upload -> gaps -> handoff to return assembly)
3. One-line reviewer reminder (must be reviewed by CPA or licensed professional before filing)
4. Launch the refusal sweep immediately using `ask_user_input_v0`

**Example first message:**

> Let's get your 2025 Canadian returns ready. Quick scope check, then you upload your documents, then I fill in the gaps. Target time: 10 minutes.
>
> Reminder: everything I produce needs to be reviewed and signed off by a CPA or licensed tax professional before you file anything with CRA. I'm not a substitute for review.
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
Q1: "Canadian residency in 2025?"
    Options: ["Full year", "Part year", "Did not live in Canada"]

Q2: "Business structure?"
    Options: ["Sole proprietor (unincorporated)", "Corporation (Inc. / Ltd.)", "Partnership", "Not sure"]

Q3: "Province of residence on December 31, 2025?"
    Options: ["Ontario", "British Columbia", "Quebec", "Alberta", "Manitoba", "Saskatchewan", "Nova Scotia", "New Brunswick", "PEI", "Newfoundland and Labrador", "Yukon", "NWT", "Nunavut"]

Q4: "GST/HST registered?"
    Options: ["Yes (revenue above $30K or voluntarily registered)", "No (small supplier, revenue under $30K)", "Not sure"]
```

**After the response, evaluate:**

- **Q1 = Full year** -> continue
- **Q1 = Part year or did not live in Canada** -> stop. "I'm set up for full-year Canadian residents only. Part-year or non-residents have different rules around world income and treaty exemptions. You need a CPA who handles non-resident returns."

- **Q2 = Sole proprietor** -> continue
- **Q2 = Corporation** -> stop. "I don't cover corporate returns. Corporations file T2 returns with different rules. You need a CPA familiar with corporate tax."
- **Q2 = Partnership** -> stop. "Partnerships file a T5013 information return and allocate income to partners. You need a CPA familiar with partnership returns."
- **Q2 = Not sure** -> ask one follow-up: "Do you operate under your own name (or a trade name) without incorporating? Or do you have a corporation registered with your provincial registry (Inc., Ltd., Corp.)? If you invoice under your own name with no incorporation, you're a sole proprietor."

- **Q3** -> note province for provincial tax calculation. Quebec has a separate provincial return (TP-1); all other provinces are calculated on the federal return.

- **Q4 = Yes** -> continue. GST34 returns required.
- **Q4 = No** -> continue. No GST/HST return required unless revenue crosses $30K in four consecutive quarters. Will check after inference.
- **Q4 = Not sure** -> ask one follow-up: "Do you charge GST or HST on your invoices? If yes, you're registered. If you've never collected GST/HST and your total revenue has been under $30,000 in four consecutive calendar quarters, you're likely a small supplier and not required to register."

**After Q1-Q4 pass, ask the second batch of scope questions (also batched):**

```
Q5: "Also employed (T4 income) in 2025?"
    Options: ["No, fully self-employed", "Yes, also have employment income", "Yes, multiple T4s"]

Q6: "Industry?"
    Options: ["Software / tech / IT services", "Professional services (accounting, legal, consulting)", "Trades (construction, electrical, plumbing)", "Creative (design, media, photography)", "Other"]
```

**Evaluate Q5:**
- **No** -> continue (T2125 only, no T4 income)
- **Yes / Multiple T4s** -> continue. Will need T4 slips for employment income. CPP contributions from employment reduce self-employed CPP owing.

**Evaluate Q6:**
- All options -> note for expense classification context. Continue.

**Total time:** ~45 seconds if the user taps through.

---

## Section 3 -- The dump

Once the refusal sweep passes, immediately ask for the document dump. Single message. No preamble.

**Example:**

> Scope is good. Now upload everything you have for 2025 -- drop it all in at once:
>
> - Business bank statement(s) for all of 2025 (CSV or PDF)
> - Sales invoices issued in 2025
> - Purchase invoices / receipts for business expenses
> - Prior year T1 return (2024) or at least the Notice of Assessment (NOA)
> - T4 slips (if also employed)
> - T5 slips (investment income, if any)
> - GST/HST return copies for 2025 (if registered)
> - RRSP contribution receipts
> - Motor vehicle expense receipts and kilometre log
> - Home office expense records (if claiming)
> - Capital asset purchase receipts (computers, equipment)
> - Any CRA correspondence or notices
> - Anything else tax-related you have
>
> Don't worry about labeling or organizing -- I'll figure out what each file is. Drag and drop when ready.

Then wait. Do not ask any other questions while waiting.

**If the user uploads a partial dump and says "that's what I have":** move to inference. Do not demand more. Request specific missing items during gap-filling.

**If the user says "I don't know what I have":** Switch to guided mode:
> Check these places:
> - Business bank: download 2025 statements as PDF or CSV
> - CRA My Account: download NOA, T4s, T5s, prior T1, instalment statements
> - Revenu Quebec (if QC): download RL slips and prior TP-1
> - Email: search for "invoice", "GST", "CRA", "RRSP", "T4"
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
- Outflows to CRA (instalment payments with dates)
- Outflows to CRA (GST/HST payments with dates)
- Outflows to RRSP providers (contribution amounts and dates)
- Outflows to suppliers (business expenses by category)
- Equipment purchases (potential CCA or immediate expensing items)
- Transfers to personal account (owner draws)
- Any rent payments (potential home office or business premises)
- SaaS / software subscriptions
- Professional memberships
- Insurance payments (business, motor, E&O)

**Sales invoices:**
- Client names and amounts
- Whether GST/HST was charged (registered indicator)
- GST vs HST rate used (indicates province of supply)
- Whether invoices show no tax (small supplier indicator)
- Total revenue reconciliation against bank deposits
- Any foreign clients (zero-rated export implications)

**Purchase invoices / receipts:**
- Expense category (current expense vs capital)
- GST/HST paid on each (input tax credit for registered filers)
- CCA class for capital items (Class 10, 10.1, 50, 12, etc.)
- Any blocked categories (personal, club dues, 50% meals/entertainment)

**Prior year T1 / NOA:**
- Prior year net income (line 23600) and taxable income (line 26000)
- Prior year tax payable and balance owing/refund
- Prior year T2125 net business income
- Instalment reminder amounts from NOA
- Any loss carryforwards
- RRSP deduction limit from NOA

**T4 slips (if also employed):**
- Gross employment income (Box 14)
- CPP contributions (Box 16)
- EI premiums (Box 18)
- Income tax deducted (Box 22)
- RPP contributions (Box 20)
- Union dues (Box 44)

**GST/HST returns:**
- Revenue reported (line 101)
- GST/HST collected (line 105)
- Input tax credits claimed (line 108)
- Net tax owing/refund (line 109)
- Instalment payments

**RRSP receipts:**
- Contribution amounts and dates
- First 60 days of 2026 contributions (applicable to 2025)
- RRSP deduction limit from prior NOA

**After parsing everything, build an internal inference object.** Do not show the raw inference yet -- transform it into a compact summary for the user in Section 5.

---

## Section 5 -- The confirmation

After inference, present a single compact summary message. Use a structured format that is fast to scan. Invite the user to correct anything wrong.

**Example summary message:**

> Here's what I pulled from your documents. Skim and tell me what's wrong.
>
> **Identity**
> - Marc Tremblay, single
> - Full-year Canadian resident (Toronto, Ontario)
> - Sole proprietor, fiscal year end December 31
> - GST/HST registered (HST at 13% -- Ontario)
>
> **Business Income (from bank statement + invoices)**
> - Gross business revenue (ex-HST): ~$120,000
>   - BigTech Inc.: $72,000 (monthly retainer)
>   - StartupCo: $30,000 (project work)
>   - Various smaller clients: $18,000
> - HST collected (13%): ~$15,600
>
> **Employment Income (from T4)**
> - None (fully self-employed)
>
> **Expenses (from bank statement + purchase invoices)**
> - Office supplies: $1,800
> - Software / SaaS subscriptions: $3,600
> - Professional insurance (E&O): $1,400
> - Accounting fees: $2,000
> - Phone / internet: $2,400 (TBD -- need business use %)
> - Motor vehicle: $5,200 fuel + insurance + maintenance (TBD -- need km log)
> - Equipment: Dell laptop $2,800 (June 2025) -- CCA Class 50 (55%) or immediate expensing
> - Meals and entertainment: $1,600 (50% deductible)
> - ITC on purchases: ~$1,450 (claimable)
>
> **RRSP Contributions**
> - 2025 contributions: $12,000
> - RRSP deduction limit (from 2024 NOA): $18,500
> - Room remaining: $6,500
>
> **Instalments Paid (from bank statement / NOA)**
> - Q1: $2,500, Q2: $2,500, Q3: $2,500, Q4: $2,500
> - Total paid: $10,000
>
> **Prior Year (from 2024 T1 / NOA)**
> - 2024 net business income: $95,000
> - 2024 net income (line 23600): $83,000 (after RRSP)
> - 2024 tax payable: $14,200
> - 2024 instalment base: $10,000
>
> **Flags I already see:**
> 1. Phone / internet -- need business use percentage
> 2. Motor vehicle -- need kilometre log (business km vs total km)
> 3. Dell laptop $2,800 -- eligible for immediate expensing (AIIP) or CCA Class 50
> 4. Meals and entertainment at 50% deduction -- standard rule
> 5. RRSP within limit -- no excess issue
> 6. Fiscal year end must be December 31 for sole proprietors
>
> **Is any of this wrong? Reply "looks good" or tell me what to fix.**

---

## Section 6 -- Gap filling

After the user confirms the summary (or corrects it), ask about things that cannot be inferred from documents. Use `ask_user_input_v0` where possible.

**Things that usually cannot be inferred:**

1. **Home office** -- Cannot tell from documents whether a workspace exists and which method.
2. **Private use percentage** -- Phone, internet, motor vehicle business-use split.
3. **Vehicle kilometre log** -- Business km vs total km driven.
4. **CCA claims** -- Whether to claim immediate expensing (AIIP) or standard CCA on capital items.
5. **Province** -- Already established in refusal sweep, but confirm if near year-end move.
6. **Other income** -- Interest, dividends, rental, capital gains.
7. **Dependants** -- For credits (Canada Child Benefit is separate, but eligible dependant amount matters).

**Home office gap-filling example:**

Call `ask_user_input_v0` with:

```
Q: "Home office?"
   Options: [
     "Dedicated room used ONLY for work (detailed method -- T2125 Part 7)",
     "Shared space used regularly for work (simplified method)",
     "I work from a separate business premises (not home)",
     "I don't work from home",
     "Not sure"
   ]
```

If option 1 -> ask for: total home sq ft, workspace sq ft, and home expenses (rent/mortgage interest, utilities, insurance, property tax, maintenance). Note: mortgage principal is never deductible; only interest portion qualifies for renters or owners.
If option 2 -> ask for percentage of home used and hours per week. Flag as T2 for reviewer: must be principal place of business or used exclusively for business on a regular and continuous basis (s18(12) ITA).
If option 3 -> rent is already captured in expenses. No home office calculation needed.
If option 4 -> skip home office entirely.
If option 5 -> explain the two conditions under s18(12): (a) principal place of business, or (b) used exclusively and on a regular and continuous basis for meeting clients. If neither applies, no claim.

**Motor vehicle gap-filling example:**

Call `ask_user_input_v0` with:

```
Q: "Motor vehicle -- do you have a kilometre log?"
   Options: [
     "Yes, I tracked business vs personal km for the full year",
     "Partial log (some months only)",
     "No log, but I can estimate business km",
     "No vehicle used for business"
   ]
```

If option 1 -> ask for total km and business km (text input). Business % = business km / total km.
If option 2 -> flag as T2: CRA expects a full-year log. Partial log may be accepted if representative. Ask for available figures.
If option 3 -> flag as T2: CRA requires a log to support vehicle claims. Ask for best estimate and warn that a log should be maintained going forward.
If option 4 -> skip vehicle entirely.

Flag all private-use percentages as T2 -- CPA must confirm the percentage is reasonable and supported.

**CCA / immediate expensing example:**

Call `ask_user_input_v0` with:

```
Q: "Capital equipment -- claim method?"
   Options: [
     "Immediate expensing (AIIP -- deduct full cost in year of purchase)",
     "Standard CCA (depreciate over time)",
     "Not sure -- recommend the best option"
   ]
```

If option 1 -> apply immediate expensing under the Accelerated Investment Incentive Property rules (AIIP limit $1.5M for CCPCs and unincorporated businesses, per year).
If option 2 -> apply standard CCA rates (half-year rule if not AIIP eligible).
If option 3 -> recommend immediate expensing if total capital purchases are well under the $1.5M limit (they will be for a freelancer). Flag for reviewer.

---

## Section 7 -- The final handoff

Once gap-filling is done, produce a final handoff message and hand off to `ca-return-assembly`.

**Example handoff message:**

> Intake complete. Here's what's going to the return assembly:
>
> Sole proprietor, single, HST registered, full-year Ontario resident. Gross business revenue $120,000 (ex-HST), estimated net ~$98,000 before RRSP.
>
> I'm now going to run the full Canadian return preparation. This covers:
> 1. GST/HST return (GST34 -- annual or outstanding quarters)
> 2. T2125 Statement of Business Activities
> 3. T1 federal return
> 4. CPP/CPP2/EI self-employed contributions
> 5. Instalment schedule for 2026
> 6. Ontario provincial tax (calculated on the T1)
>
> You'll get back:
> 1. An Excel working paper with all forms and live formulas
> 2. A reviewer brief with positions, citations, and flags for your CPA
> 3. A filing calendar with all upcoming deadlines
>
> Starting now.

Then internally invoke `ca-return-assembly` with the structured intake package.

---

## Section 8 -- Structured intake package (internal format)

The downstream skill (`ca-return-assembly`) consumes a JSON structure. It is internal and not shown to the user unless they ask. Key fields:

```json
{
  "jurisdiction": "CA",
  "tax_year": 2025,
  "taxpayer": {
    "name": "",
    "date_of_birth": "",
    "marital_status": "single | married | common_law",
    "residency": "full_year",
    "sin": "",
    "province": "",
    "gst_hst_registered": true,
    "gst_hst_number": "",
    "employment_status": "self_employed | employed_plus_side",
    "industry": "",
    "entity_type": "sole_proprietor",
    "fiscal_year_end": "12-31"
  },
  "business_income": {
    "gross_revenue_ex_gst": 0,
    "gst_hst_collected": 0,
    "client_breakdown": []
  },
  "employment_income": {
    "t4_slips": [],
    "total_employment_income": 0,
    "total_cpp_deducted": 0,
    "total_ei_deducted": 0,
    "total_tax_deducted": 0
  },
  "other_income": {
    "interest": 0,
    "dividends_eligible": 0,
    "dividends_other": 0,
    "rental": 0,
    "capital_gains": 0
  },
  "expenses": {
    "fully_deductible": [],
    "mixed_use": [],
    "blocked": [],
    "meals_entertainment_gross": 0,
    "cca_items": [],
    "immediate_expensing_items": []
  },
  "gst_hst": {
    "returns_filed": [],
    "total_collected": 0,
    "total_itc": 0,
    "net_tax": 0,
    "rate": 0
  },
  "rrsp": {
    "contributions_2025": 0,
    "contributions_first_60_days_2026": 0,
    "deduction_limit": 0,
    "room_remaining": 0
  },
  "instalments": {
    "quarterly_amounts": [],
    "total_paid": 0,
    "prior_year_instalment_base": 0
  },
  "home_office": {
    "qualifies": false,
    "method": "detailed | simplified | none",
    "workspace_sqft": 0,
    "total_home_sqft": 0,
    "home_expenses": {},
    "percentage": 0
  },
  "motor_vehicle": {
    "has_log": false,
    "total_km": 0,
    "business_km": 0,
    "business_pct": 0,
    "total_expenses": 0
  },
  "prior_year": {
    "net_income": 0,
    "taxable_income": 0,
    "tax_payable": 0,
    "net_business_income": 0,
    "instalment_base": 0,
    "rrsp_deduction_limit": 0,
    "loss_carryforwards": 0,
    "cca_schedule": []
  },
  "open_flags": [],
  "refusals_triggered": [],
  "documents_received": []
}
```

---

## Section 9 -- Refusal handling

Refusals fire from either the refusal sweep (Section 2) or during inference (e.g., incorporated structure discovered in documents).

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

> Stop -- you have an incorporated business. I'm set up for sole proprietors only. Corporations file T2 returns with different rules for shareholder remuneration, dividends, and corporate tax. You need a CPA familiar with corporate returns.
>
> I can't help with this one.

---

## Section 10 -- Self-checks

**Check IN1 -- No one-question-at-a-time prose in the refusal sweep.** If the skill asked "Question 1 of 10" or walked through questions as separate messages, check fails.

**Check IN2 -- Refusal sweep used ask_user_input_v0.** The first substantive interaction used the interactive tool, not prose questions.

**Check IN3 -- Upload-first flow honoured.** After refusal sweep, the skill asked for a document dump before asking any content questions.

**Check IN4 -- Documents were parsed and inferred before asking questions.** The inference summary (Section 5) was shown before gap-filling questions (Section 6).

**Check IN5 -- Gap-filling only asked about things NOT visible in documents.** If the skill asked "did you contribute to RRSP" after the bank statement showed RRSP payments, check fails.

**Check IN6 -- Open flags captured.** Anything ambiguous, risky, or attention-worthy during inference is in the `open_flags` list in the handoff package.

**Check IN7 -- Handoff to `ca-return-assembly` is explicit.** The user was told "I'm now going to run the return preparation," and the downstream orchestrator was explicitly invoked with the intake package.

**Check IN8 -- Reviewer step was stated upfront and reiterated before handoff.** The opening message mentioned CPA/professional signoff.

**Check IN9 -- Refusals were clean.** No hedging. Stop means stop.

**Check IN10 -- No meta-commentary about workflow phases.** The skill did not say "Phase 1," "Phase 2," etc.

**Check IN11 -- Total user-facing turn count is low.** Target: 8 turns or fewer from start to handoff for a prepared user (1 refusal batch + 1 upload + 1 confirmation + 1-3 gap fills + 1 handoff). More than 12 turns for a normal intake is a check failure.

**Check IN12 -- GST/HST registration status was established.** Registered vs small supplier was confirmed before inference, as it changes how every transaction is classified.

**Check IN13 -- Province was established.** Province determines GST vs HST rate, provincial tax calculation method, and whether a separate provincial return is needed (Quebec).

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

**Outputs:** Structured intake package consumed by `ca-return-assembly`.

**Downstream skills triggered (via ca-return-assembly):**
- `canada-gst-hst` -- GST34 return
- `ca-fed-t2125` -- Statement of Business or Professional Activities
- `ca-fed-t1-return` -- Federal T1 individual return
- `ca-fed-cpp-ei` -- CPP/CPP2 and EI self-employed contributions
- `ca-fed-instalments` -- Instalment schedule for next year
- Provincial return (Quebec TP-1 if applicable; other provinces calculated on T1)

---

### Change log

- **v0.1 (April 2026):** Initial draft. Upload-first, inference-then-confirm pattern modelled on mt-freelance-intake v0.1.

## End of Intake Skill v0.1


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
