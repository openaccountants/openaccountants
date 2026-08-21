---
name: nl-freelance-intake
description: ALWAYS USE THIS SKILL when a user asks for help preparing their Netherlands tax returns AND mentions freelancing, self-employment, ZZP, eenmanszaak, or sole proprietorship. Trigger on phrases like "help me do my taxes", "prepare my IB-aangifte", "I'm a ZZP'er in the Netherlands", "I'm a freelancer in the Netherlands", "do my taxes as a contractor", "prepare my BTW return and income tax", or any similar phrasing where the user is a Netherlands-resident self-employed individual needing tax return preparation. This is the REQUIRED entry point for the Netherlands self-employed tax workflow -- every other skill in the stack (nl-btw-return, nl-income-tax, nl-zvw, nl-return-assembly) depends on this skill running first to produce a structured intake package. Uses upload-first workflow -- the user dumps all their documents and the skill infers as much as possible before asking questions. Uses ask_user_input_v0 for structured questions instead of one-at-a-time prose. Built for speed. Netherlands full-year residents only; self-employed individuals and sole proprietors.
version: 1.0
jurisdiction: NL
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
category: orchestrator
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# NL Freelance Intake

## What this file is

The intake orchestrator for Netherlands-resident self-employed individuals. Every downstream Netherlands content skill (nl-btw-return, nl-income-tax, nl-zvw) and the assembly orchestrator (nl-return-assembly) depend on this skill running first to produce a structured intake package.

This skill does not compute any tax figures. Its job is to collect all the facts, parse all the documents, confirm everything with the user, and hand off a clean intake package to `nl-return-assembly`.

## Design principles

v1.0 follows the upload-first, inference-then-confirm pattern:

1. **Compact refusal sweep** using `ask_user_input_v0` -- 3 interactive questions, ~30 seconds.
2. **Upload-first workflow** -- after the refusal check, the user dumps everything they have.
3. **Inference pass** -- Claude parses every document and extracts as much as possible.
4. **Gap-filling only** -- Claude asks the user ONLY about what is missing, ambiguous, or needs confirmation.
5. **Single confirmation pass** at the end -- show the full picture, let the user correct anything wrong, hand off to downstream skills.

Target: intake completes in 5 minutes for a prepared user, 15 minutes for a user who has to go fetch documents.

## Critical operating principles

**Do not narrate the workflow.** Do not say "Phase 1," "Phase 2," "Now I'll ask you about deductions." Just do the work.

**Do not ask questions that have already been answered.** If the refusal check established the user is a ZZP'er with BTW registration, do not later ask about VAT registration type. Track what is known.

**Do not ask about things visible in uploaded documents.** If the bank statement shows quarterly BTW payments to Belastingdienst, do not ask "did you pay BTW." Confirm what you see, do not re-ask.

**Use `ask_user_input_v0` for any multiple-choice question.** Text input is only for genuinely open-ended data (names, addresses, specific amounts when they cannot be inferred).

**Prefer batching.** Ask 3 related questions in a single message when they do not depend on each other's answers.

**Be terse but complete.** No hedging, no "let me know if you have questions," no "I hope this helps."

**Exception for blocking decisions.** If a single question determines whether the user is in-scope or out-of-scope, ask it standalone.

## Section 1 -- The opening

When triggered, respond with ONE message that:

1. One-line greeting (no paragraph of expectation-setting)
2. One-line summary of the flow (scope check -> upload -> gaps -> handoff to return assembly)
3. One-line reviewer reminder (must be reviewed by qualified belastingadviseur before filing)
4. Launch the refusal sweep immediately using `ask_user_input_v0`

**Example first message:**

> Let's get your 2025 Netherlands returns ready. Quick scope check, then you upload your documents, then I fill in the gaps. Target time: 10 minutes.
>
> Reminder: everything I produce needs to be reviewed and signed off by a qualified belastingadviseur before you file anything with the Belastingdienst. I'm not a substitute for review.
>
> Scope check:

Then immediately call `ask_user_input_v0` with the refusal questions.

**Do NOT:**
- Write a welcome paragraph
- Explain the phases
- Ask "are you ready to start"
- List what documents you will eventually need
- Give a disclaimer beyond the one reviewer line

## Section 2 -- Refusal sweep (compact)

Present the refusal sweep as a single `ask_user_input_v0` call with 3 questions, all single-select.

**The 3 questions to ask first:**

```
Q1: "Netherlands residency in 2025?"
    Options: ["Full year", "Part year (immigrated/emigrated)", "Did not live in the Netherlands"]

Q2: "Business structure?"
    Options: ["ZZP / eenmanszaak (sole proprietor)", "VOF (vennootschap onder firma)", "BV (besloten vennootschap)", "Not sure"]

Q3: "Employment status in 2025?"
    Options: ["Fully self-employed (no employer)", "Employed + side self-employment", "Employed only (no self-employment income)"]
```

- **Q1 evaluation -- residency** — Q1 = Full year -> continue. Q1 = Part year -> stop: "I'm set up for full-year Netherlands residents only. Part-year residents have M-biljet (migratieaangifte) requirements with different rules around worldwide vs Dutch-source income. You need a belastingadviseur who handles M-biljetten." Q1 = Did not live in the Netherlands -> stop: "Non-residents file C-biljet (buitenlandse belastingplicht) with different rules. You need a belastingadviseur who handles non-resident returns."  _(Section 2 -- Refusal sweep (compact))_
- **Q2 evaluation -- business structure** — Q2 = ZZP / eenmanszaak -> continue. Q2 = VOF -> stop: "VOF partnerships file separately with joint and individual obligations (firmantenaangifte). You need a belastingadviseur familiar with VOF returns." Q2 = BV -> stop: "I don't cover corporate returns. BVs file vennootschapsbelasting (VPB) returns with separate rules for DGA salaries, dividends, and Box 2 income. You need a belastingadviseur." Q2 = Not sure -> ask follow-up: "Do you invoice clients in your own name (or a trade name registered at KvK), or do you have a BV registered at KvK? If you invoice in your own name with a KvK eenmanszaak registration, you're ZZP/eenmanszaak. If you have a BV, you're a limited company."  _(Section 2 -- Refusal sweep (compact))_
- **Q3 evaluation -- employment status** — Q3 = Fully self-employed -> continue. Q3 = Employed + side self-employment -> continue with a flag: urencriterium (1,225 hours) may not be met, affecting zelfstandigenaftrek eligibility. Will evaluate after inference. Q3 = Employed only -> stop: "You don't have self-employment income. This workflow is for self-employed individuals. Your employer handles your tax through loonheffing deductions. If you have other income (rental, investments, Box 3 assets), you need a belastingadviseur for your aangifte inkomstenbelasting."  _(Section 2 -- Refusal sweep (compact))_

**After Q1-Q3 pass, ask the second batch of scope questions (also batched):**

```
Q4: "BTW (omzetbelasting) status?"
    Options: ["Regular BTW registration (quarterly/monthly filing)", "Kleineondernemersregeling (KOR) -- BTW exempt", "Not BTW registered", "Not sure"]

Q5: "Marital status / fiscal partner?"
    Options: ["Single (no fiscal partner)", "Married / registered partner", "Living together with fiscal partner (notarial cohabitation contract or joint ownership)", "Living together without fiscal partner status"]

Q6: "KvK registration?"
    Options: ["Yes, registered at KvK", "No, not registered", "Not sure"]
```

- **KOR turnover threshold** — 20,000 EUR per calendar year (Kleineondernemersregeling (KOR) turnover must remain under this amount)  _(Section 2 -- Refusal sweep (compact))_
- **Q4 evaluation -- BTW status** — Regular BTW -> continue, standard quarterly or monthly BTW-aangifte. KOR -> continue, no BTW-aangifte filing required, no input BTW recovery, turnover must remain under EUR 20,000 per calendar year. Not BTW registered -> continue with flag: if turnover exceeds EUR 20,000, KOR exemption is automatically revoked; if no BTW registration at all and not KOR, may need registration. Not sure -> ask follow-up: "Do you charge 21% BTW on your invoices? If yes, you have regular BTW registration. If your invoices say 'BTW verlegd' or show no BTW and your annual revenue is under EUR 20,000, you may be on the KOR."  _(Section 2 -- Refusal sweep (compact))_
- **Q5 evaluation -- marital status** — Single -> continue, no partner allocation. Married / registered partner -> continue, fiscal partner allocation applies (income from own dwelling Box 1, Box 3 assets, heffingskortingen can be optimised). Living together with fiscal partner -> continue, same as married for tax purposes. Living together without fiscal partner status -> continue, no partner allocation.  _(Section 2 -- Refusal sweep (compact))_
- **Q6 evaluation -- KvK registration** — Yes -> continue, standard ZZP path. No -> flag: without KvK registration, the Belastingdienst may classify income as resultaat uit overige werkzaamheden (ROW) rather than winst uit onderneming, disqualifying zelfstandigenaftrek, startersaftrek, and MKB-winstvrijstelling. Not sure -> "Check kvk.nl/zoeken with your name. If you have a registration with an active eenmanszaak, you're registered."  _(Section 2 -- Refusal sweep (compact))_

**Total time:** ~45 seconds if the user taps through.

## Section 3 -- The dump

Once the refusal sweep passes, immediately ask for the document dump. Single message. No preamble.

**Example:**

> Scope is good. Now upload everything you have for 2025 -- drop it all in at once:
>
> - Business bank statement(s) for all of 2025 (CSV or PDF)
> - Sales invoices (verkoopfacturen) issued in 2025
> - Purchase invoices / receipts (inkoopfacturen) for business expenses
> - Prior year aangifte inkomstenbelasting (IB-aangifte) or voorlopige aanslag
> - Prior BTW-aangiften for 2025 (if regular BTW registration)
> - Jaaropgave(n) from any employment income
> - KvK uittreksel (extract)
> - WOZ-beschikking (property valuation, if claiming eigen woning aftrek)
> - Mortgage annual statement (jaaroverzicht hypotheek) if applicable
> - Capital asset purchase receipts (computers, equipment)
> - Health insurance (zorgverzekering) statements
> - Any Belastingdienst correspondence or voorlopige aanslagen
> - Anything else tax-related you have
>
> Don't worry about labeling or organizing -- I'll figure out what each file is. Drag and drop when ready.

Then wait. Do not ask any other questions while waiting.

**If the user uploads a partial dump and says "that's what I have":** move to inference. Do not demand more. Request specific missing items during gap-filling.

**If the user says "I don't know what I have":** Switch to guided mode:
> Check these places:
> - Business bank: download 2025 statements as PDF or CSV
> - MijnBelastingdienst portal: download prior IB-aangifte and voorlopige aanslagen
> - Email: search for "factuur", "BTW", "Belastingdienst", "KvK", "jaaropgave"
> - Your boekhouder from last year, if you had one
> - Dropbox / Google Drive for saved invoices
> - Hypotheekverstrekker portal for jaaroverzicht
>
> Come back when you have something to upload. I'll work with whatever you bring.

## Section 4 -- The inference pass

**Bank statement:**
- Total deposits (candidate gross receipts)
- Recurring inflows (client payments with names)
- Outflows to Belastingdienst (inkomstenbelasting voorlopige aanslag payments, BTW payments)
- Outflows for ZVW (zorgverzekeringswet bijdrage)
- Outflows to suppliers (business expenses by category)
- Equipment purchases (potential capital items)
- Transfers to personal account (privé-opnames)
- Rent payments (zakelijke huur or home office)
- SaaS / software subscriptions
- Professional memberships (NBA, NOB, etc.)
- Insurance payments (aansprakelijkheidsverzekering, arbeidsongeschiktheidsverzekering)
- Pensioenpremie payments (lijfrente, FOR)

**Sales invoices (verkoopfacturen):**
- Client names and amounts
- Whether BTW was charged (regular registration indicator)
- BTW rate applied (21% standaard, 9% laag, 0% export/intracommunautair)
- Whether invoices show "BTW verlegd" (reverse charge)
- Total turnover reconciliation against bank deposits
- Any foreign clients (EU with BTW-id or non-EU -- ICP opgave implications)

**Purchase invoices (inkoopfacturen):**
- Expense category (bedrijfskosten, investeringen, voorraad)
- BTW amount on each (reclaimable for regular registration, cost for KOR)
- Supplier location (Dutch, EU, non-EU)
- Any items qualifying as bedrijfsmiddel (business asset for afschrijving)
- Any blocked categories (representatiekosten 80% limitation, private use)

**Prior year IB-aangifte:**
- Prior year winst uit onderneming
- Prior year zelfstandigenaftrek and MKB-winstvrijstelling applied
- Prior year capital allowances schedule (restwaarde, afschrijving)
- Filing status and fiscal partner allocation
- Box 3 assets and threshold
- Eigenwoningforfait and hypotheekrenteaftrek if applicable

**Prior BTW-aangiften:**
- Quarterly/monthly turnover and BTW collected
- Voorbelasting (input BTW) claimed
- Any suppletie-aangifte filed
- ICP leveringen/diensten reported

**Jaaropgave (employment income):**
- Loon, loonheffing withheld, ZVW bijdrage
- Employer details

**WOZ-beschikking and hypotheek jaaroverzicht:**
- WOZ-waarde (for eigenwoningforfait calculation)
- Hypotheekrente paid (for eigen woning aftrek Box 1)
- Eigenwoningschuld outstanding

**After parsing everything, build an internal inference object.** Do not show the raw inference yet -- transform it into a compact summary for the user in Section 5.

## Section 5 -- The confirmation

After inference, present a single compact summary message. Use a structured format that is fast to scan. Invite the user to correct anything wrong.

**Example summary message:**

> Here's what I pulled from your documents. Skim and tell me what's wrong.
>
> **Identity**
> - Jan de Vries, single (no fiscal partner)
> - Full-year Netherlands resident (Amsterdam)
> - ZZP / eenmanszaak, KvK 12345678
> - BTW: Regular registration (NL123456789B01), quarterly filing
>
> **Income -- Winst uit onderneming (from bank statement + invoices)**
> - Omzet (turnover ex-BTW): ~EUR 68,000
>   - TechCorp BV: EUR 36,000 (monthly retainer)
>   - DesignStudio: EUR 22,000 (project work)
>   - Various smaller clients: EUR 10,000
> - BTW collected (21%): ~EUR 14,280
>
> **Expenses -- Bedrijfskosten (from bank statement + purchase invoices)**
> - Kantoorhuur (office rent): EUR 6,000
> - Software / SaaS: EUR 2,400
> - Aansprakelijkheidsverzekering (PI insurance): EUR 600
> - Boekhouder (accountancy fees): EUR 1,200
> - Telefoon / internet: EUR 840 (TBD -- need zakelijk gebruik %)
> - Auto: EUR 3,600 fuel + EUR 800 onderhoud (TBD -- need zakelijk gebruik % or km-registratie)
> - Laptop: EUR 1,800 (April 2025) -- bedrijfsmiddel, afschrijving 20% per jaar
> - Voorbelasting (input BTW): ~EUR 3,200 (reclaimable)
>
> **Ondernemersaftrek**
> - Zelfstandigenaftrek: EUR 2,470 (2025 rate) -- need to confirm urencriterium (1,225+ hours)
> - Startersaftrek: TBD -- need to confirm if within first 5 years and not claimed 3x
> - MKB-winstvrijstelling: 13.31% of remaining winst after zelfstandigenaftrek
>
> **Eigen woning (from WOZ + hypotheek)**
> - WOZ-waarde: EUR 320,000
> - Eigenwoningforfait: EUR 1,760 (0.55% x EUR 320,000 -- 2025 rate)
> - Hypotheekrente betaald: EUR 8,400
> - Eigen woning aftrek: EUR 6,640 (aftrek)
>
> **Voorlopige aanslag / voorheffingen (from bank statement)**
> - Voorlopige aanslag IB 2025 paid: EUR 4,200
> - Voorlopige aanslag ZVW 2025 paid: EUR 1,800
>
> **Prior year (from 2024 IB-aangifte)**
> - 2024 winst uit onderneming: EUR 52,000
> - 2024 belastbaar inkomen Box 1: EUR 38,000
> - Capital allowances continuing: laptop EUR 1,440 WDV
>
> **BTW (from prior BTW-aangiften)**
> - Q1-Q3 2025 filed
> - Q4 outstanding
> - No suppletie required based on current data
>
> **Flags I already see:**
> 1. Telefoon/internet -- need zakelijk gebruik percentage
> 2. Auto -- need zakelijk gebruik percentage and km-registratie (or consider forfaitaire autokosten EUR 0.23/km)
> 3. Urencriterium -- need confirmation of 1,225+ hours for zelfstandigenaftrek
> 4. Startersaftrek eligibility -- need to confirm year count
> 5. Q4 2025 BTW-aangifte not yet filed -- will prepare as part of this workflow
> 6. Box 3 vermogensrendementsheffing -- need to check bank/beleggingen saldi on 1 January 2025 and 2026
>
> **Is any of this wrong? Reply "looks good" or tell me what to fix.**

- **Example zelfstandigenaftrek rate (2025)** — 2,470 EUR (2025 rate, example in confirmation summary)  _(Section 5 -- The confirmation)_
- **MKB-winstvrijstelling percentage** — 13.31 % (applied to remaining winst after zelfstandigenaftrek)  _(Section 5 -- The confirmation)_
- **Eigenwoningforfait rate example (2025)** — 0.55 % of WOZ-waarde (example in confirmation summary, 2025 rate)  _(Section 5 -- The confirmation)_

## Section 6 -- Gap filling

After the user confirms the summary (or corrects it), ask about things that cannot be inferred from documents. Use `ask_user_input_v0` where possible.

**Things that usually cannot be inferred:**

1. **Urencriterium** -- 1,225 hours devoted to the onderneming. Cannot tell from documents alone.
2. **Startersaftrek eligibility** -- Whether the user is within their first 5 years of self-employment and has not claimed startersaftrek more than 2 times before.
3. **Home office (werkruimte)** -- Whether a dedicated werkruimte exists and qualifies (zelfstandige werkruimte criteria).
4. **Private use percentage** -- Phone, internet, auto zakelijk gebruik split.
5. **FOR (fiscale oudedagsreserve)** -- Whether the user wants to reserve FOR (maximum 9.44% of winst, up to EUR 9,632 in 2025).
6. **Lijfrentepremie** -- Payments toward lijfrente (pension) for jaarruimte/reserveringsruimte deduction.
7. **Box 3 vermogen** -- Bank balances, beleggingen, overige bezittingen, and schulden on peildatum 1 January 2025 and 1 January 2026.
8. **Other income** -- Employment income, rental income, periodic payments (alimentatie).
9. **Fiscal partner allocation** -- If fiscal partner exists, how to split Box 3, eigen woning, and heffingskortingen.

- **Urencriterium hours requirement** — 1,225 hours (minimum hours devoted to the onderneming for zelfstandigenaftrek eligibility)  _(Section 6 -- Gap filling)_

Call `ask_user_input_v0` with:

```
Q: "Did you work at least 1,225 hours on your business in 2025?"
   Options: [
     "Yes, comfortably above 1,225 hours (full-time self-employed)",
     "Yes, but it's close (part-time self-employed, around 1,225)",
     "No, under 1,225 hours",
     "Not sure"
   ]
```

If option 1 -> zelfstandigenaftrek qualifies. Note T2: reviewer should confirm urenadministratie exists.
If option 2 -> flag T2: marginal case, urenadministratie is critical. Reviewer must verify.
If option 3 -> no zelfstandigenaftrek, no startersaftrek, no FOR. MKB-winstvrijstelling still applies. Income is still winst uit onderneming if KvK-registered.
If option 4 -> "The urencriterium requires you to have spent at least 1,225 hours on your business. Full-time freelancers almost always meet it. If you also had employment, count only the hours on your business. Do you think you're above or below?"

- **Startersaftrek amount (2025)** — 2,123 EUR (startersaftrek on top of zelfstandigenaftrek, 2025)  _(Section 6 -- Gap filling)_

Call `ask_user_input_v0` with:

```
Q: "Startersaftrek eligibility?"
   Options: [
     "Started in 2025 (first year)",
     "2nd or 3rd year, have not claimed startersaftrek 3 times yet",
     "Started more than 5 years ago",
     "Already claimed startersaftrek 3 times",
     "Not sure"
   ]
```

If option 1 or 2 -> EUR 2,123 startersaftrek on top of zelfstandigenaftrek (2025).
If option 3 or 4 -> no startersaftrek.
If not sure -> "When did you register at KvK? The 5-year window starts from your first year of claiming zelfstandigenaftrek."

Call `ask_user_input_v0` with:

```
Q: "Home office (werkruimte)?"
   Options: [
     "Separate room with own entrance -- qualifies as zelfstandige werkruimte",
     "Dedicated room, no separate entrance, but I earn >70% of income there",
     "Dedicated room, but I earn <70% of income there or also use it privately",
     "Separate business premises (not at home)",
     "No fixed workspace"
   ]
```

If option 1 -> qualifies as zelfstandige werkruimte. Ask for percentage of home floor area. Deduction for proportional huur/hypotheekrente/eigenwoningforfait/gas/elektra/water.
If option 2 -> qualifies if >70% income earned there AND >30% total income comes from this workspace. Ask for floor area percentage. T2 flag for reviewer.
If option 3 -> does not qualify as zelfstandige werkruimte. No home office deduction under Dutch rules.
If option 4 -> rent already captured in business expenses. No home office calculation needed.
If option 5 -> skip werkruimte entirely.

- **FOR maximum percentage and cap (2025)** — 9.44% of winst, up to EUR 9,632 % / EUR (fiscale oudedagsreserve maximum reserve, 2025, applies only if urencriterium met and under AOW age)  _(Section 6 -- Gap filling)_

Call `ask_user_input_v0` with:

```
Q: "Do you want to reserve FOR (fiscale oudedagsreserve) for 2025?"
   Options: [
     "Yes, maximum allowed",
     "Yes, specific amount (I'll tell you)",
     "No",
     "What is FOR?"
   ]
```

If "What is FOR?" -> "FOR lets you reserve up to 9.44% of your winst (max EUR 9,632 in 2025) as a tax-deductible pension reserve. It defers tax, not eliminates it -- you pay tax when you convert it to a lijfrente or at age 67. The maximum applies only if you meet the urencriterium and are under AOW age."

Flag all private-use percentages as T2 -- belastingadviseur must confirm the percentage is reasonable and documented.

## Section 7 -- The final handoff

Once gap-filling is done, produce a final handoff message and hand off to `nl-return-assembly`.

**Example handoff message:**

> Intake complete. Here's what's going to the return assembly:
>
> ZZP/eenmanszaak, single, regular BTW registration, full-year Netherlands resident. Omzet EUR 68,000, estimated winst ~EUR 52,000 before ondernemersaftrek.
>
> I'm now going to run the full Netherlands return preparation. This covers:
> 1. BTW-aangifte (Q4 2025 or suppletie)
> 2. Aangifte inkomstenbelasting (IB) -- Box 1 (winst, eigen woning), Box 3 (vermogen)
> 3. ZVW (zorgverzekeringswet) bijdrage reconciliation
> 4. Voorlopige aanslag 2026 recommendation
>
> You'll get back:
> 1. An Excel working paper with all forms and live formulas
> 2. A reviewer brief with positions, citations, and flags for your belastingadviseur
> 3. A filing calendar with all upcoming deadlines
>
> Starting now.

Then internally invoke `nl-return-assembly` with the structured intake package.

0. **Invoke return assembly** — Internally invoke nl-return-assembly with the structured intake package

## Section 8 -- Structured intake package (internal format)

The downstream skill (`nl-return-assembly`) consumes a JSON structure. It is internal and not shown to the user unless they ask. Key fields:

```json
{
  "jurisdiction": "NL",
  "tax_year": 2025,
  "taxpayer": {
    "name": "",
    "bsn": "",
    "birth_year": 0,
    "marital_status": "single | married | registered_partner | fiscal_partner",
    "residency": "full_year",
    "kvk_nummer": "",
    "btw_nummer": "",
    "btw_registration_type": "regular | kor | unregistered",
    "employment_status": "self_employed | employed_plus_side",
    "industry": "",
    "entity_type": "eenmanszaak"
  },
  "income": {
    "omzet_ex_btw": 0,
    "btw_collected": 0,
    "employment_income": 0,
    "loonheffing_withheld": 0,
    "other_income": 0,
    "client_breakdown": []
  },
  "expenses": {
    "fully_deductible": [],
    "mixed_use": [],
    "blocked": [],
    "capital_items": [],
    "representatiekosten": 0
  },
  "ondernemersaftrek": {
    "urencriterium_met": true,
    "zelfstandigenaftrek": 0,
    "startersaftrek_eligible": false,
    "startersaftrek": 0,
    "mkb_winstvrijstelling_pct": 13.31,
    "for_dotatie": 0
  },
  "btw": {
    "filing_frequency": "quarterly | monthly",
    "returns_filed": [],
    "voorbelasting_reclaimable": 0,
    "icp_leveringen": 0,
    "icp_diensten": 0,
    "suppletie_required": false
  },
  "eigen_woning": {
    "woz_waarde": 0,
    "eigenwoningforfait": 0,
    "hypotheekrente": 0,
    "eigen_woning_aftrek": 0
  },
  "box3": {
    "peildatum_1jan_2025": {
      "bank_en_spaartegoeden": 0,
      "beleggingen": 0,
      "overige_bezittingen": 0,
      "schulden": 0
    },
    "peildatum_1jan_2026": {
      "bank_en_spaartegoeden": 0,
      "beleggingen": 0,
      "overige_bezittingen": 0,
      "schulden": 0
    },
    "heffingsvrij_vermogen": 0
  },
  "voorlopige_aanslag": {
    "ib_paid": 0,
    "zvw_paid": 0
  },
  "prior_year": {
    "winst_uit_onderneming": 0,
    "belastbaar_inkomen_box1": 0,
    "capital_allowances_schedule": []
  },
  "werkruimte": {
    "qualifies": false,
    "type": "zelfstandige_werkruimte | none",
    "percentage": 0
  },
  "private_use": {
    "auto_zakelijk_pct": 0,
    "telefoon_zakelijk_pct": 0,
    "internet_zakelijk_pct": 0
  },
  "fiscal_partner": {
    "has_partner": false,
    "partner_income": 0,
    "allocation_preferences": {}
  },
  "open_flags": [],
  "refusals_triggered": [],
  "documents_received": []
}
```

## Section 9 -- Refusal handling

Refusals fire from either the refusal sweep (Section 2) or during inference (e.g., BV structure discovered in documents).

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

- **R-NL-1 -- BV with employees > 5** — Stop -- you have a BV with more than 5 employees. I'm set up for ZZP/eenmanszaak sole proprietors only. BVs with employees involve vennootschapsbelasting, loonbelasting, and werknemersverzekeringen. You need a belastingadviseur familiar with BV/werkgever returns.  _(Section 9 -- Refusal handling)_
- **R-NL-2 -- Holding structures** — Stop -- you have a holding/werkmaatschappij structure. Multi-entity structures involve intercompany transactions, fiscal unity (fiscale eenheid), and participation exemption (deelnemingsvrijstelling). You need a belastingadviseur who specialises in holding structures.  _(Section 9 -- Refusal handling)_
- **R-NL-3 -- International payroll** — Stop -- you have international payroll obligations. Cross-border employment involves 30% ruling, social security coordination (A1 detachering), and tax treaties. You need a belastingadviseur with international expertise.  _(Section 9 -- Refusal handling)_

> Stop -- you have a registered BV. I'm set up for ZZP/eenmanszaak sole proprietors only. BVs file vennootschapsbelasting returns with different rules for DGA-salaris, dividendbelasting, and Box 2 income. You need a belastingadviseur familiar with BV returns.
>
> I can't help with this one.

## Section 10 -- Self-checks

**Check IN1 -- No one-question-at-a-time prose in the refusal sweep.** If the skill asked "Question 1 of 10" or walked through questions as separate messages, check fails.

**Check IN2 -- Refusal sweep used ask_user_input_v0.** The first substantive interaction used the interactive tool, not prose questions.

**Check IN3 -- Upload-first flow honoured.** After refusal sweep, the skill asked for a document dump before asking any content questions.

**Check IN4 -- Documents were parsed and inferred before asking questions.** The inference summary (Section 5) was shown before gap-filling questions (Section 6).

**Check IN5 -- Gap-filling only asked about things NOT visible in documents.** If the skill asked "did you pay BTW" after the bank statement showed Belastingdienst payments, check fails.

**Check IN6 -- Open flags captured.** Anything ambiguous, risky, or attention-worthy during inference is in the `open_flags` list in the handoff package.

**Check IN7 -- Handoff to `nl-return-assembly` is explicit.** The user was told "I'm now going to run the return preparation," and the downstream orchestrator was explicitly invoked with the intake package.

**Check IN8 -- Reviewer step was stated upfront and reiterated before handoff.** The opening message mentioned belastingadviseur signoff.

**Check IN9 -- Refusals were clean.** No hedging. Stop means stop.

**Check IN10 -- No meta-commentary about workflow phases.** The skill did not say "Phase 1," "Phase 2," etc.

**Check IN11 -- Total user-facing turn count is low.** Target: 8 turns or fewer from start to handoff for a prepared user (1 refusal batch + 1 upload + 1 confirmation + 1-3 gap fills + 1 handoff). More than 12 turns for a normal intake is a check failure.

**Check IN12 -- BTW registration type was established.** Regular vs KOR was confirmed before inference, as it changes how every transaction is classified.

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

## Section 12 -- Cross-skill references

**Inputs:** User-provided documents and answers.

**Outputs:** Structured intake package consumed by `nl-return-assembly`.

**Downstream skills triggered (via nl-return-assembly):**
- `nl-btw-return` -- BTW-aangifte (quarterly/monthly or KOR annual)
- `nl-income-tax` -- Aangifte inkomstenbelasting (Box 1/2/3)
- `nl-zvw` -- Zorgverzekeringswet bijdrage reconciliation

0. **Trigger nl-btw-return** — BTW-aangifte (quarterly/monthly or KOR annual)
0. **Trigger nl-income-tax** — Aangifte inkomstenbelasting (Box 1/2/3)
0. **Trigger nl-zvw** — Zorgverzekeringswet bijdrage reconciliation

### Change log

- **v1.0 (May 2026):** Initial draft. Upload-first, inference-then-confirm pattern modelled on mt-freelance-intake v0.1.

## End of Intake Skill v1.0

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

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
