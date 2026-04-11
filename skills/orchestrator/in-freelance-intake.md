---
name: in-freelance-intake
description: ALWAYS USE THIS SKILL when a user asks for help preparing their India tax returns AND mentions freelancing, self-employment, contracting, professional services, or independent practice. Trigger on phrases like "help me do my taxes", "prepare my ITR", "I'm self-employed in India", "I'm a freelancer in India", "do my taxes as a consultant", "prepare my income tax return", or any similar phrasing where the user is an India-resident self-employed individual needing tax return preparation. This is the REQUIRED entry point for the India self-employed tax workflow -- every other skill in the stack (india-gst, in-income-tax, in-advance-tax, in-tds-freelance, in-return-assembly) depends on this skill running first to produce a structured intake package. Uses upload-first workflow -- the user dumps all their documents and the skill infers as much as possible before asking questions. Uses ask_user_input_v0 for structured questions instead of one-at-a-time prose. Built for speed. India full-year residents only; self-employed individuals and professionals only.
version: 0.1
---

# India Self-Employed Intake Skill v0.1

## What this file is

The intake orchestrator for India-resident self-employed individuals and professionals. Every downstream India content skill (india-gst, in-income-tax, in-advance-tax, in-tds-freelance) and the assembly orchestrator (in-return-assembly) depend on this skill running first to produce a structured intake package.

This skill does not compute any tax figures. Its job is to collect all the facts, parse all the documents, confirm everything with the user, and hand off a clean intake package to `in-return-assembly`.

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

**Do not ask questions that have already been answered.** If the refusal check established the user is GST registered, do not later ask about GST registration. Track what is known.

**Do not ask about things visible in uploaded documents.** If Form 26AS shows TDS credits, do not ask "did you have TDS deducted." Confirm what you see, do not re-ask.

**Use `ask_user_input_v0` for any multiple-choice question.** Text input is only for genuinely open-ended data (names, addresses, specific amounts when they cannot be inferred).

**Prefer batching.** Ask 3 related questions in a single message when they do not depend on each other's answers.

**Be terse but complete.** No hedging, no "let me know if you have questions," no "I hope this helps."

**Exception for blocking decisions.** If a single question determines whether the user is in-scope or out-of-scope, ask it standalone.

---

## Section 1 -- The opening

When triggered, respond with ONE message that:

1. One-line greeting (no paragraph of expectation-setting)
2. One-line summary of the flow (scope check -> upload -> gaps -> handoff to return assembly)
3. One-line reviewer reminder (must be reviewed by qualified CA before filing)
4. Launch the refusal sweep immediately using `ask_user_input_v0`

**Example first message:**

> Let's get your FY 2025-26 India returns ready. Quick scope check, then you upload your documents, then I fill in the gaps. Target time: 10 minutes.
>
> Reminder: everything I produce needs to be reviewed and signed off by a Chartered Accountant before you file anything with the Income Tax Department or GST portal. I'm not a substitute for professional review.
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
Q1: "Indian residency in FY 2025-26?"
    Options: ["Resident (in India 182+ days)", "Resident but Not Ordinarily Resident (RNOR)", "Non-resident (NRI)", "Not sure"]

Q2: "Business structure?"
    Options: ["Self-employed individual / sole proprietor", "Hindu Undivided Family (HUF)", "Partnership firm / LLP", "Private limited company (Pvt Ltd)", "Not sure"]

Q3: "Nature of self-employment?"
    Options: ["Professional services (IT, consulting, legal, medical, accounting, etc.)", "Business (trading, manufacturing, retail)", "Freelance / contract work (domestic or international clients)", "Mixed (professional + business income)"]
```

**After the response, evaluate:**

- **Q1 = Resident** -> continue
- **Q1 = RNOR** -> stop. "I'm set up for ordinary residents only. RNOR status has different rules around foreign income taxation. You need a CA who handles RNOR/NRI returns."
- **Q1 = Non-resident** -> stop. "I'm set up for India-resident individuals only. NRIs have different rules around source income, DTAA benefits, and return filing. You need a CA who handles NRI returns."
- **Q1 = Not sure** -> ask one follow-up: "Were you physically present in India for 182 days or more during FY 2025-26 (April 2025 to March 2026)? If yes, you're a Resident. If no, you may be NRI or RNOR depending on prior years."

- **Q2 = Self-employed individual** -> continue
- **Q2 = HUF** -> stop. "HUFs file separately with different rules for partition, co-parcenary income, and exemptions. You need a CA familiar with HUF returns."
- **Q2 = Partnership / LLP** -> stop. "Partnerships and LLPs file separate returns (ITR-5) with different rules for partner remuneration and interest. You need a CA familiar with firm returns."
- **Q2 = Pvt Ltd** -> stop. "I don't cover corporate returns. Private limited companies file ITR-6 with separate rules for directors' remuneration, dividends, and corporate tax. You need a CA."
- **Q2 = Not sure** -> ask one follow-up: "Do you invoice clients in your own name (or a trade name) using your PAN? Or do you have a registered company/LLP with the MCA? If you invoice in your own name, you're a sole proprietor."

- **Q3 = Professional services** -> continue. Section 44ADA presumptive eligible if gross receipts under INR 75 lakh (INR 50 lakh if cash receipts exceed 5%).
- **Q3 = Business** -> continue. Section 44AD presumptive eligible if turnover under INR 3 crore (INR 2 crore if cash receipts exceed 5%).
- **Q3 = Freelance / contract** -> continue. Likely 44ADA path. Flag if foreign clients (TCS on foreign remittance may apply).
- **Q3 = Mixed** -> continue with flag: may need to track professional and business income separately for presumptive eligibility.

**After Q1-Q3 pass, ask the second batch of scope questions (also batched):**

```
Q4: "PAN status?"
    Options: ["Have PAN and it's linked to Aadhaar", "Have PAN but not linked to Aadhaar", "Don't have PAN"]

Q5: "GST registration?"
    Options: ["GST registered (regular)", "GST registered (composition scheme)", "Not GST registered", "Not sure"]

Q6: "Age as of 31 March 2026?"
    Options: ["Below 60", "60-79 (senior citizen)", "80+ (super senior citizen)"]
```

**Evaluate Q4:**
- **PAN linked to Aadhaar** -> continue.
- **PAN not linked** -> continue with flag: PAN may be inoperative under s.139AA. TDS at higher rate (20%) may apply. Urgent: link before filing.
- **No PAN** -> stop. "You need a PAN to file income tax returns. Apply for PAN first, then come back."

**Evaluate Q5:**
- **GST registered (regular)** -> continue. GSTR-3B and GSTR-1 filing required.
- **GST registered (composition)** -> continue with flag: composition scheme limits and flat rate apply.
- **Not GST registered** -> continue with flag: if aggregate turnover exceeds INR 20 lakh (INR 10 lakh for special category states), registration is mandatory. Will check after inference.
- **Not sure** -> ask one follow-up: "Do you have a 15-digit GSTIN? Do you charge GST on your invoices? If yes, you're registered."

**Evaluate Q6:**
- **Below 60** -> standard exemption limit INR 3,00,000 (new regime) or INR 2,50,000 (old regime).
- **60-79** -> senior citizen: INR 3,00,000 old regime exemption. New regime same INR 3,00,000.
- **80+** -> super senior: INR 5,00,000 old regime exemption. New regime same INR 3,00,000. Cannot file online (ITR must be paper-filed or through authorised representative).

**Total time:** ~45 seconds if the user taps through.

---

## Section 3 -- The dump

Once the refusal sweep passes, immediately ask for the document dump. Single message. No preamble.

**Example:**

> Scope is good. Now upload everything you have for FY 2025-26 -- drop it all in at once:
>
> - Business bank statement(s) for April 2025 to March 2026 (PDF or CSV)
> - Sales invoices issued in FY 2025-26
> - Purchase invoices / receipts for business expenses
> - Form 26AS (Annual Information Statement from TRACES)
> - AIS (Annual Information Statement from income tax portal)
> - Prior year ITR (ITR-3 or ITR-4 as filed)
> - GST returns filed (GSTR-3B summaries, GSTR-1)
> - TDS certificates (Form 16A from clients)
> - Advance tax challans (Form 26QB / self-assessment challans)
> - Professional tax receipts
> - Insurance premium receipts (LIC, health insurance)
> - PPF / ELSS / NPS statements (if claiming 80C/80D/80CCD)
> - Any IT notices or correspondence
> - Anything else tax-related you have
>
> Don't worry about labeling or organizing -- I'll figure out what each file is. Drag and drop when ready.

Then wait. Do not ask any other questions while waiting.

**If the user uploads a partial dump and says "that's what I have":** move to inference. Do not demand more. Request specific missing items during gap-filling.

**If the user says "I don't know what I have":** Switch to guided mode:
> Check these places:
> - Business bank: download FY 2025-26 statements as PDF or CSV
> - Income tax portal (incometax.gov.in): download Form 26AS and AIS
> - TRACES portal: download TDS certificates
> - GST portal (gst.gov.in): download GSTR-3B and GSTR-1 filed returns
> - Email: search for "invoice", "TDS", "ITR", "GST", "advance tax"
> - Your CA from last year, if you had one
> - Google Drive / local folders for saved invoices
>
> Come back when you have something to upload. I'll work with whatever you bring.

---

## Section 4 -- The inference pass

When documents arrive, parse each one. For each document, extract:

**Bank statement:**
- Total deposits (candidate gross receipts)
- Recurring inflows (client payments with names, domestic vs international)
- Digital receipts vs cash deposits (critical for 44ADA/44AD threshold -- INR 75L/50L or INR 3Cr/2Cr)
- Outflows to Income Tax Department (advance tax payments with dates and challan numbers)
- Outflows labelled GST / CGST / SGST / IGST (GST payments)
- Outflows to professional bodies
- Equipment purchases (potential capital items)
- Transfers to personal account (owner draws)
- Rent payments (office or co-working space)
- SaaS / software subscriptions
- Insurance payments (PI, health, LIC)
- RETA / professional tax payments

**Form 26AS / AIS:**
- TDS credits by deductor (client name, TAN, amount deducted, section)
- Advance tax and self-assessment tax payments (dates and amounts)
- High-value transactions flagged by AIS (SFT information)
- Tax collected at source (TCS) entries
- Refund issued (if any from prior year)

**Sales invoices:**
- Client names and amounts
- Whether GST was charged (CGST+SGST or IGST)
- Whether invoices show "under reverse charge"
- SAC/HSN codes used
- Total turnover reconciliation against bank deposits and Form 26AS
- Foreign clients (export of services -- zero-rated under GST, FIRC/foreign remittance)

**Purchase invoices / receipts:**
- Expense category (revenue vs capital)
- GST input tax credit (ITC) amounts
- Supplier GSTIN (for ITC eligibility verification)
- Any items that are blocked ITC under s.17(5) CGST Act

**Prior year ITR:**
- Which form was filed (ITR-3 or ITR-4)
- Prior year total income and tax liability
- Old regime vs new regime elected
- Carry-forward losses (if any)
- Depreciation schedule (WDV of asset blocks)
- Whether 44ADA/44AD was opted in prior year (lock-in implications)

**GST returns (GSTR-3B / GSTR-1):**
- Monthly/quarterly turnover reported
- Output GST collected
- ITC claimed
- GST paid (cash + ITC utilisation)
- Any reverse charge liability

**TDS certificates (Form 16A):**
- Deductor details and TAN
- Amount paid and TDS deducted
- Section under which TDS deducted (194J, 194C, 194H, etc.)
- Reconciliation against Form 26AS

**After parsing everything, build an internal inference object.** Do not show the raw inference yet -- transform it into a compact summary for the user in Section 5.

---

## Section 5 -- The confirmation

After inference, present a single compact summary message. Use a structured format that is fast to scan. Invite the user to correct anything wrong.

**Example summary message:**

> Here's what I pulled from your documents. Skim and tell me what's wrong.
>
> **Identity**
> - Rajesh Kumar, age 35
> - Full-year Indian resident (Bangalore)
> - Self-employed professional, sole proprietor
> - PAN: ABCPK1234F (linked to Aadhaar)
> - GSTIN: 29ABCPK1234F1Z5 (regular registration, Karnataka)
>
> **Income (from bank statement + invoices + 26AS)**
> - Gross receipts: ~INR 38,00,000
>   - Digital receipts: INR 36,50,000 (96%)
>   - Cash receipts: INR 1,50,000 (4%)
>   - Since digital > 95%, 44ADA threshold is INR 75,00,000 -- eligible
>   - TechCorp India Pvt Ltd: INR 18,00,000 (retainer)
>   - GlobalSoft Inc (USA): INR 12,00,000 (export of services, zero-rated GST)
>   - Various domestic clients: INR 8,00,000
> - GST collected (18%): ~INR 4,68,000 (on domestic taxable supplies)
>
> **Expenses (from bank statement + purchase invoices)**
> - Co-working space rent: INR 1,80,000
> - Software / SaaS subscriptions: INR 90,000
> - Professional insurance: INR 25,000
> - CA fees: INR 30,000
> - Internet: INR 36,000 (TBD -- need business use %)
> - Mobile phone: INR 24,000 (TBD -- need business use %)
> - Laptop: INR 1,20,000 (Oct 2025) -- capital item, 40% depreciation
> - ITC claimed on purchases: ~INR 85,000
>
> **TDS credits (from Form 26AS)**
> - TechCorp: INR 1,80,000 (s.194J, 10%)
> - Other clients: INR 62,000 (s.194J)
> - Total TDS: INR 2,42,000
>
> **Advance tax paid (from 26AS / challans)**
> - 15 Jun 2025: INR 50,000
> - 15 Sep 2025: INR 50,000
> - 15 Dec 2025: INR 50,000
> - 15 Mar 2026: INR 50,000
> - Total advance tax: INR 2,00,000
>
> **GST (from GSTR-3B)**
> - Monthly GSTR-3B filed, GSTR-1 filed
> - Total output GST: INR 4,68,000
> - Total ITC utilised: INR 85,000
> - Cash GST paid: INR 3,83,000
>
> **Prior year (from FY 2024-25 ITR)**
> - Filed ITR-4 (presumptive 44ADA)
> - Total income: INR 14,50,000
> - Tax paid: INR 1,85,000
> - New tax regime elected
> - No carry-forward losses
>
> **Flags I already see:**
> 1. Phone / internet -- need business use percentage
> 2. If choosing 44ADA presumptive: 50% deemed profit, no further expense deductions allowed -- net tax may be higher than actual-profit ITR-3
> 3. Prior year was 44ADA; if switching to ITR-3 (actual profit), cannot go back to presumptive for 5 years under s.44ADA(4)
> 4. Export of services to GlobalSoft -- verify FIRC received for zero-rating
> 5. Advance tax + TDS = INR 4,42,000 -- need to check if sufficient to avoid s.234B/234C interest
>
> **Is any of this wrong? Reply "looks good" or tell me what to fix.**

---

## Section 6 -- Gap filling

After the user confirms the summary (or corrects it), ask about things that cannot be inferred from documents. Use `ask_user_input_v0` where possible.

**Things that usually cannot be inferred:**

1. **Old regime vs new regime** -- Critical decision point for FY 2025-26.
2. **Presumptive taxation (44ADA/44AD) vs actual profit** -- If eligible, user must choose.
3. **80C/80D deductions (old regime only)** -- PPF, ELSS, LIC, health insurance, NPS.
4. **Home office** -- Cannot tell from documents whether a dedicated workspace exists.
5. **Private use percentage** -- Phone, internet business-use split.
6. **Other income** -- Savings interest, FD interest, rental income, capital gains.
7. **Professional tax paid** -- Deductible under s.16(iii) / business expense.

**Tax regime gap-filling example:**

Call `ask_user_input_v0` with:

```
Q: "Tax regime for FY 2025-26?"
   Options: [
     "New tax regime (default -- lower rates, no deductions except standard)",
     "Old tax regime (higher rates, but 80C/80D/80CCD/HRA deductions available)",
     "Not sure -- help me decide"
   ]
```

If option 1 -> continue with new regime. No 80C/80D questions needed.
If option 2 -> continue with old regime. Ask about 80C/80D/80CCD deductions.
If option 3 -> flag for comparison computation: "I'll compute under both regimes and show you which is lower. For now, I need to know your potential deductions." Then ask about 80C/80D.

**Presumptive vs actual profit example:**

Call `ask_user_input_v0` with:

```
Q: "Presumptive taxation (44ADA) or actual profit (ITR-3)?"
   Options: [
     "Presumptive 44ADA -- declare 50% of gross receipts as profit, no expense deductions, no audit",
     "Actual profit (ITR-3) -- claim actual expenses, maintain books, possible audit if profit < 50%",
     "Not sure -- help me decide"
   ]
```

If option 1 -> presumptive path. Skip detailed expense categorisation.
If option 2 -> actual profit path. Full expense schedule needed.
If option 3 -> compute both and compare.

**80C deductions example (old regime only):**

Call `ask_user_input_v0` with:

```
Q: "Section 80C investments in FY 2025-26? (max INR 1,50,000)"
   Options: [
     "PPF contribution",
     "ELSS mutual funds",
     "Life insurance premium (LIC)",
     "5-year FD",
     "NPS (80CCD(1) within 80C limit)",
     "Multiple of the above",
     "None / don't want to claim"
   ]
```

If "Multiple" -> ask for amounts as text input.

**Home office gap-filling example:**

Call `ask_user_input_v0` with:

```
Q: "Home office?"
   Options: [
     "Dedicated room, used ONLY for work",
     "Dedicated corner/desk, used ONLY for work",
     "Shared space (kitchen table, living room)",
     "Separate business premises (co-working / rented office)",
     "No fixed workspace"
   ]
```

If option 1 -> ask for room count or area percentage. Deductible as business expense (rent proportion, electricity, internet).
If option 2 -> flag for reviewer: partial home office may qualify but documentation is key.
If option 3 -> "A shared space is difficult to defend as a business deduction. I'll skip this."
If option 4 -> rent is already captured in expenses. No home office calculation needed.
If option 5 -> skip home office entirely.

Flag all private-use percentages for reviewer confirmation.

---

## Section 7 -- The final handoff

Once gap-filling is done, produce a final handoff message and hand off to `in-return-assembly`.

**Example handoff message:**

> Intake complete. Here's what's going to the return assembly:
>
> Self-employed professional, resident individual, age 35, GST registered (regular). Gross receipts INR 38,00,000, choosing 44ADA presumptive -- deemed profit INR 19,00,000.
>
> I'm now going to run the full India return preparation. This covers:
> 1. GST returns reconciliation (GSTR-3B + GSTR-1)
> 2. Income tax return (ITR-4 if presumptive, ITR-3 if actual profit)
> 3. Advance tax reconciliation and s.234B/234C interest computation
> 4. TDS credit reconciliation
>
> You'll get back:
> 1. An Excel working paper with all computations and live formulas
> 2. A reviewer brief with positions, citations, and flags for your CA
> 3. A filing calendar with all upcoming deadlines
>
> Starting now.

Then internally invoke `in-return-assembly` with the structured intake package.

---

## Section 8 -- Structured intake package (internal format)

The downstream skill (`in-return-assembly`) consumes a JSON structure. It is internal and not shown to the user unless they ask. Key fields:

```json
{
  "jurisdiction": "IN",
  "financial_year": "2025-26",
  "assessment_year": "2026-27",
  "taxpayer": {
    "name": "",
    "age": 0,
    "age_category": "below_60 | senior_60_79 | super_senior_80_plus",
    "residency": "resident",
    "pan": "",
    "aadhaar_linked": true,
    "gstin": "",
    "gst_registration_type": "regular | composition | unregistered",
    "nature_of_profession": "",
    "entity_type": "sole_proprietor"
  },
  "regime": {
    "tax_regime": "new | old",
    "presumptive": true,
    "presumptive_section": "44ADA | 44AD | none",
    "itr_form": "ITR-3 | ITR-4"
  },
  "income": {
    "gross_receipts": 0,
    "digital_receipts": 0,
    "cash_receipts": 0,
    "digital_percentage": 0,
    "deemed_profit_percentage": 50,
    "deemed_profit": 0,
    "other_income": 0,
    "client_breakdown": []
  },
  "expenses": {
    "fully_deductible": [],
    "mixed_use": [],
    "blocked": [],
    "capital_items": [],
    "total_actual_expenses": 0
  },
  "gst": {
    "gstr3b_filed": [],
    "gstr1_filed": [],
    "output_gst_collected": 0,
    "itc_claimed": 0,
    "gst_cash_paid": 0,
    "reverse_charge_liability": 0,
    "export_services": 0
  },
  "tds": {
    "tds_credits": [],
    "total_tds": 0,
    "tds_by_section": {}
  },
  "advance_tax": {
    "payments": [],
    "total_advance_tax_paid": 0
  },
  "deductions_old_regime": {
    "section_80c": 0,
    "section_80d": 0,
    "section_80ccd_1b": 0,
    "section_80ccd_2": 0,
    "professional_tax": 0,
    "other_deductions": []
  },
  "prior_year": {
    "itr_form_filed": "",
    "total_income": 0,
    "tax_liability": 0,
    "regime_used": "",
    "presumptive_used": false,
    "carry_forward_losses": [],
    "depreciation_schedule": []
  },
  "home_office": {
    "qualifies": false,
    "percentage": 0,
    "method": "rooms | floor_area"
  },
  "private_use": {
    "phone_business_pct": 0,
    "internet_business_pct": 0
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

> Stop -- you operate through a Private Limited Company. I'm set up for self-employed individuals and sole proprietors only. Pvt Ltd companies file ITR-6 with separate rules for directors' salary, dividend distribution tax, and corporate tax rates. You need a CA familiar with corporate returns.
>
> I can't help with this one.

---

## Section 10 -- Self-checks

**Check IN1 -- No one-question-at-a-time prose in the refusal sweep.** If the skill asked "Question 1 of 10" or walked through questions as separate messages, check fails.

**Check IN2 -- Refusal sweep used ask_user_input_v0.** The first substantive interaction used the interactive tool, not prose questions.

**Check IN3 -- Upload-first flow honoured.** After refusal sweep, the skill asked for a document dump before asking any content questions.

**Check IN4 -- Documents were parsed and inferred before asking questions.** The inference summary (Section 5) was shown before gap-filling questions (Section 6).

**Check IN5 -- Gap-filling only asked about things NOT visible in documents.** If the skill asked "did you pay advance tax" after Form 26AS showed challan entries, check fails.

**Check IN6 -- Open flags captured.** Anything ambiguous, risky, or attention-worthy during inference is in the `open_flags` list in the handoff package.

**Check IN7 -- Handoff to `in-return-assembly` is explicit.** The user was told "I'm now going to run the return preparation," and the downstream orchestrator was explicitly invoked with the intake package.

**Check IN8 -- Reviewer step was stated upfront and reiterated before handoff.** The opening message mentioned CA signoff.

**Check IN9 -- Refusals were clean.** No hedging. Stop means stop.

**Check IN10 -- No meta-commentary about workflow phases.** The skill did not say "Phase 1," "Phase 2," etc.

**Check IN11 -- Total user-facing turn count is low.** Target: 8 turns or fewer from start to handoff for a prepared user (1 refusal batch + 1 upload + 1 confirmation + 1-3 gap fills + 1 handoff). More than 12 turns for a normal intake is a check failure.

**Check IN12 -- Tax regime and presumptive status established.** Old vs new regime and 44ADA/44AD decision confirmed before handoff, as it changes the entire computation.

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

**Outputs:** Structured intake package consumed by `in-return-assembly`.

**Downstream skills triggered (via in-return-assembly):**
- `india-gst` -- GSTR-3B + GSTR-1 reconciliation
- `in-income-tax` -- ITR-3 or ITR-4 return
- `in-advance-tax` -- Quarterly advance tax reconciliation and interest computation
- `in-tds-freelance` -- TDS credit reconciliation and reporting

---

### Change log

- **v0.1 (April 2026):** Initial draft. Upload-first, inference-then-confirm pattern modelled on mt-freelance-intake v0.1.

## End of Intake Skill v0.1


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a Chartered Accountant, tax practitioner, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
