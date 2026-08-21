---
name: fr-freelance-intake
description: ALWAYS USE THIS SKILL when a user asks for help preparing their French tax returns AND mentions freelancing, auto-entrepreneur, micro-entrepreneur, entreprise individuelle, profession libérale, or self-employment. Trigger on phrases like "aide-moi avec mes impôts", "préparer ma déclaration", "I'm a freelancer in France", "I'm an auto-entrepreneur", "prepare my 2042-C-PRO", or any similar phrasing where the user is a France-resident self-employed individual needing tax return preparation. This is the REQUIRED entry point for the French self-employed tax workflow -- every other skill in the stack (france-tva, france-income-tax, france-cotisations, fr-return-assembly) depends on this skill running first to produce a structured intake package. Uses upload-first workflow -- the user dumps all their documents and the skill infers as much as possible before asking questions. Uses ask_user_input_v0 for structured questions instead of one-at-a-time prose. Built for speed. France full-year residents only; self-employed individuals, micro-entrepreneurs, and sole proprietors.
version: 1.0
jurisdiction: FR
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
category: orchestrator
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# FR Freelance Intake

## What this file is

The intake orchestrator for France-resident self-employed individuals. Every downstream French content skill (france-tva, france-income-tax, france-cotisations, fr-estimated-tax) and the assembly orchestrator (fr-return-assembly) depend on this skill running first to produce a structured intake package.

This skill does not compute any tax figures. Its job is to collect all the facts, parse all the documents, confirm everything with the user, and hand off a clean intake package to `fr-return-assembly`.

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

**Do not ask questions that have already been answered.** If the refusal check established the user is a micro-entrepreneur, do not later ask about business structure. Track what is known.

**Do not ask about things visible in uploaded documents.** If the bank statement shows quarterly URSSAF payments, do not ask "did you pay cotisations." Confirm what you see, do not re-ask.

**Use `ask_user_input_v0` for any multiple-choice question.** Text input is only for genuinely open-ended data (names, addresses, specific amounts when they cannot be inferred).

**Prefer batching.** Ask 3 related questions in a single message when they do not depend on each other's answers.

**Be terse but complete.** No hedging, no "let me know if you have questions," no "I hope this helps."

**Exception for blocking decisions.** If a single question determines whether the user is in-scope or out-of-scope, ask it standalone.

## Section 1 -- The opening

When triggered, respond with ONE message that:

1. One-line greeting (no paragraph of expectation-setting)
2. One-line summary of the flow (scope check -> upload -> gaps -> handoff to return assembly)
3. One-line reviewer reminder (must be reviewed by expert-comptable before filing)
4. Launch the refusal sweep immediately using `ask_user_input_v0`

**Example first message:**

> Let's get your 2025 French returns ready. Quick scope check, then you upload your documents, then I fill in the gaps. Target time: 10 minutes.
>
> Reminder: everything I produce needs to be reviewed and signed off by an expert-comptable or qualified tax professional before you file anything with the DGFiP or URSSAF. I'm not a substitute for review.
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
Q1: "Business type?"
    Options: ["Micro-entrepreneur (auto-entrepreneur)", "Entreprise individuelle (EI) au réel", "EURL (gérant associé unique)", "SASU (président associé unique)", "Profession libérale", "Not sure"]

Q2: "Revenue range for 2025?"
    Options: ["Under €77,700 (services) / €188,700 (goods)", "Above €77,700 (services) / €188,700 (goods)", "Not sure"]

Q3: "TVA regime?"
    Options: ["Franchise en base (no TVA charged)", "Réel simplifié (CA12 annual + 2 acomptes)", "Réel normal (CA3 monthly/quarterly)", "Not sure"]
```

- **Q1 = Micro-entrepreneur** — continue. Micro-fiscal and micro-social regime. Forms: 2042, 2042-C-PRO (cases 5KO/5KP for BIC or 5HQ/5HB for BNC).
- **Q1 = EI au réel** — continue. Full accounting regime. Forms: 2042, 2042-C-PRO, plus liasse fiscale (2035 for BNC, 2031 for BIC).
- **Q1 = EURL (gérant associé unique)** — continue ONLY if gérant associé unique with IR option (impôt sur le revenu). If EURL at IS (impôt sur les sociétés), stop: "EURL at IS files a corporate return (liasse 2065). I'm set up for personal income tax filings. You need an expert-comptable who handles IS returns."
- **Q1 = SASU** — stop. "SASU is always subject to impôt sur les sociétés (IS). The président is an assimilé salarié with bulletins de paie. I'm set up for self-employed individuals filing personal income tax. You need an expert-comptable who handles corporate and payroll."
- **Q1 = Profession libérale** — continue. BNC regime. Forms: 2042, 2042-C-PRO, 2035 (déclaration contrôlée).
- **Q1 = Not sure** — ask one follow-up: "Did you register with the guichet unique (formalités.entreprises.gouv.fr) as auto-entrepreneur, or do you have a SIRET with a full accounting obligation? Check your avis de situation SIRENE or your URSSAF online account for your status."
- **Q2 = Under thresholds** — continue. Micro-entrepreneur regime is available.
- **Q2 = Above thresholds** — continue with a flag: if currently micro-entrepreneur, mandatory switch to réel for the second consecutive year above thresholds (Article 293 B and Article 50-0 CGI). Will verify after inference.  _(Article 293 B and Article 50-0 CGI)_
- **Q2 = Not sure** — continue, infer from documents.
- **Q3 = Franchise en base threshold** — €36,800 services / €91,900 goods (basic franchise), with tolerance up to €39,100 / €101,000 EUR (No TVA charged or recovered)  _(Article 293 B CGI)_
- **Q3 = Réel simplifié** — continue. Annual CA12 with two acomptes semestriels (July and December). Input TVA recovery available.
- **Q3 = Réel normal** — continue. Monthly CA3 (or quarterly if TVA < €4,000/year).
- **Q3 = Not sure** — ask one follow-up: "Do your invoices include TVA (5.5%, 10%, or 20%)? If they say 'TVA non applicable, article 293 B du CGI', you're in franchise en base. If you charge TVA and file monthly/quarterly, you're réel normal. If you file one annual TVA return with two advance payments, you're réel simplifié."

**After Q1-Q3 pass, ask the second batch of scope questions (also batched):**

```
Q4: "URSSAF registration status?"
    Options: ["Registered and paying cotisations", "Recently registered (< 12 months)", "Not registered / pending", "CIPAV-affiliated (profession libérale réglementée)"]

Q5: "Marital status and household?"
    Options: ["Single (1 part)", "Married / PACSé - déclaration commune", "Married / PACSé - déclaration séparée (year of marriage/PACS)", "Single parent (parent isolé, case T/L)"]

Q6: "Other income sources in 2025?"
    Options: ["None -- self-employment only", "Employment income (salaires)", "Rental income (revenus fonciers)", "Investment income (dividends, interest, capital gains)", "Multiple of the above"]

Q7: "Prior year filing status?"
    Options: ["Filed 2024 return on time", "Filed 2024 return late", "First year filing", "Did not file 2024"]

Q8: "Régime matrimonial (if married/PACSé)?"
    Options: ["Communauté réduite aux acquêts (default)", "Communauté universelle", "Séparation de biens", "Not married / Not applicable"]
```

- **Evaluate Q4 - Registered and paying** — continue. Standard micro-social or cotisations au réel.
- **Evaluate Q4 - Recently registered** — continue with flag: ACRE (Aide à la Création ou à la Reprise d'Entreprise) may apply for first 3 years. Reduced cotisations rates: ~50% reduction year 1 for micro-entrepreneurs.
- **Evaluate Q4 - Not registered / pending** — continue with flag: registration required. Will note in action items.
- **Evaluate Q4 - CIPAV-affiliated** — continue with flag: CIPAV handles retirement for certain professions libérales réglementées (architectes, ingénieurs-conseils, etc.). Different cotisation structure.
- **Evaluate Q5** — All options -> note for quotient familial calculation. Parts fiscales: 1 (single), 2 (married/PACSé joint), special allocation for children and parent isolé.
- **Evaluate Q6** — All options -> note for multi-schedule return. Employment income goes to 2042 traitements et salaires. Rental to 2044 or micro-foncier. Investment to 2042 revenus de capitaux mobiliers or prélèvement forfaitaire unique (PFU 30%).
- **Evaluate Q7** — All options -> note for penalty/interest risk and prior year reference amounts.
- **Evaluate Q8** — Affects whether business assets are common property. Communauté regimes may expose the non-business spouse's share to business debts.

**Total time:** ~60 seconds if the user taps through.

## Section 3 -- The dump

Once the refusal sweep passes, immediately ask for the document dump. Single message. No preamble.

**Example:**

> Scope is good. Now upload everything you have for 2025 -- drop it all in at once:
>
> - Business bank account statements for all of 2025 (CSV or PDF)
> - Sales invoices issued in 2025 (or accounting software export)
> - Purchase invoices / receipts for business expenses
> - Prior year tax return (avis d'imposition 2024 sur revenus 2024, or 2042/2042-C-PRO)
> - Prior TVA returns for 2025 (CA3 or CA12)
> - URSSAF attestation or cotisation statements
> - Déclaration sociale des indépendants (DSI) if applicable
> - URSSAF micro-entrepreneur quarterly/monthly declarations
> - CFE (Cotisation Foncière des Entreprises) avis d'imposition
> - Any DGFiP or URSSAF correspondence
> - Capital asset purchase receipts (computers, equipment, vehicles)
> - Anything else tax-related you have
>
> Don't worry about labeling or organizing -- I'll figure out what each file is. Drag and drop when ready.

Then wait. Do not ask any other questions while waiting.

**If the user uploads a partial dump and says "that's what I have":** move to inference. Do not demand more. Request specific missing items during gap-filling.

**If the user says "I don't know what I have":** Switch to guided mode:
> Check these places:
> - Business bank: download 2025 statements as PDF or CSV
> - impots.gouv.fr: download prior year avis d'imposition and déclarations
> - autoentrepreneur.urssaf.fr (if micro): download annual attestation and declaration history
> - Email: search for "facture", "TVA", "URSSAF", "impôts", "CFE"
> - Your expert-comptable from last year, if you had one
> - Accounting software (Pennylane, Indy, Tiime, FreeBe, etc.): export grand livre or FEC
>
> Come back when you have something to upload. I'll work with whatever you bring.

## Section 4 -- The inference pass

When documents arrive, parse each one. For each document, extract:

**Bank statement:**
- Total deposits (candidate chiffre d'affaires / recettes)
- Recurring inflows (client payments with names)
- Outflows to URSSAF (cotisations sociales with dates and amounts)
- Outflows to DGFiP / Trésor Public (income tax payments, acomptes)
- Outflows to DGFiP TVA account (TVA payments)
- Outflows to suppliers (business expenses by category)
- CFE payment (usually October/November direct debit or December 15 deadline)
- Equipment purchases (potential immobilisations)
- Transfers to personal account (prélèvements de l'exploitant)
- SaaS / software subscriptions
- Professional memberships (ordre professionnel, syndicat)
- Insurance payments (RC Pro, prévoyance, Madelin)
- Cotisation foncière des entreprises (CFE)

**Sales invoices:**
- Client names and amounts HT (hors taxes) and TTC (toutes taxes comprises)
- Whether TVA was charged (and at what rate: 20%, 10%, 5.5%)
- Whether invoices contain "TVA non applicable, article 293 B du CGI" (franchise en base indicator)
- Total chiffre d'affaires reconciliation against bank deposits
- Any foreign clients (EU or non-EU -- autoliquidation implications)
- Any invoices with retenue à la source (withholding)

**Purchase invoices / receipts:**
- Expense category (charges courantes, immobilisations, achats de marchandises)
- TVA amount on each (récupérable for réel, cost for franchise/micro)
- Supplier location (France, EU, non-EU)
- Any items qualifying as immobilisations (typically > €500 HT)
- Any blocked categories (dépenses somptuaires: chasse, pêche, résidences de plaisance per Article 39-4 CGI)

**Prior year tax return (avis d'imposition / 2042):**
- Prior year revenu fiscal de référence (RFR)
- Prior year impôt net
- Nombre de parts fiscales
- Prior year BIC/BNC amounts declared
- Any déficits reportables (carryforward losses)
- Prélèvement à la source (PAS) rate applied
- Prior year acomptes contemporains

**Prior TVA returns (CA3/CA12):**
- Periodic turnover and TVA collected (TVA collectée)
- Input TVA claimed (TVA déductible)
- Any crédit de TVA carried forward
- CA3 monthly/quarterly box structure
- CA12 annual summary with acomptes paid

**URSSAF statements / micro-entrepreneur declarations:**
- Quarterly or monthly chiffre d'affaires declared to URSSAF
- Cotisations sociales paid (and rate applied)
- ACRE benefit if applicable (50% reduction)
- Versement libératoire de l'impôt sur le revenu if opted in (1.0% BIC vente, 1.7% BIC services, 2.2% BNC)
- Any régularisation (adjustment) from prior years

**CFE avis:**
- Amount of CFE paid for 2025
- Commune and base d'imposition

**After parsing everything, build an internal inference object.** Do not show the raw inference yet -- transform it into a compact summary for the user in Section 5.

## Section 5 -- The confirmation

After inference, present a single compact summary message. Use a structured format that is fast to scan. Invite the user to correct anything wrong.

**Example summary message:**

> Here's what I pulled from your documents. Skim and tell me what's wrong.
>
> **Identity**
> - Marie Dupont, married (déclaration commune), 2 parts + 1 demi-part (1 child)
> - Full-year France resident (Lyon)
> - Micro-entrepreneur, SIRET: 123 456 789 00010
> - Activité: conseil en informatique (BNC)
> - TVA: franchise en base (article 293 B)
>
> **Income (from bank statement + invoices)**
> - Chiffre d'affaires (recettes encaissées): €58,000
>   - Client A SARL: €30,000 (monthly retainer)
>   - Client B GmbH (Germany): €18,000 (project, EU service)
>   - Various smaller clients: €10,000
> - No TVA collected (franchise en base)
>
> **Micro-entrepreneur declarations (from URSSAF)**
> - Q1: €14,000 declared, cotisations paid: €3,094 (22.1%)
> - Q2: €15,500 declared, cotisations paid: €3,426
> - Q3: €14,500 declared, cotisations paid: €3,205
> - Q4: €14,000 declared, cotisations paid: €3,094
> - Total declared: €58,000 -- matches bank deposits
> - Total cotisations: €12,819
> - Versement libératoire IR: opted in (2.2% BNC = €1,276)
>
> **CFE**
> - CFE 2025: €412 (Lyon)
>
> **Prior year (from 2024 avis d'imposition)**
> - 2024 RFR: €42,000
> - 2024 impôt net: €3,200
> - Parts: 2.5
> - PAS rate: 7.5%
>
> **Spouse income**
> - Not yet captured -- will ask in gap-filling if déclaration commune
>
> **Flags I already see:**
> 1. EU client (Germany) -- services to EU business: autoliquidation by client, but need to verify DEB/DES declaration obligation (déclaration européenne de services) if > €0 in services to EU
> 2. CA approaching franchise en base BNC threshold (€36,800 basic / €39,100 tolérance) -- at €58,000 she should have been charging TVA. **Red flag: franchise en base not available above threshold. Needs immediate TVA registration.**
> 3. If versement libératoire IR was opted in, verify RFR N-2 eligibility: RFR per part must be ≤ €27,478 (2025 threshold on 2023 RFR)
>
> **Is any of this wrong? Reply "looks good" or tell me what to fix.**

## Section 6 -- Gap filling

After the user confirms the summary (or corrects it), ask about things that cannot be inferred from documents. Use `ask_user_input_v0` where possible.

**Things that usually cannot be inferred:**

1. **Spouse's income** -- If déclaration commune, the spouse's salary, retirement, or other income is needed for the full 2042.
2. **Children and dependents** -- Number, ages, shared custody (garde alternée), for parts fiscales calculation.
3. **Home office (local professionnel)** -- Whether a dedicated workspace exists, proportion of home used.
4. **Frais réels vs abattement forfaitaire** -- For employment income (if applicable): keep the 10% abattement or declare actual commuting/professional expenses.
5. **Réductions and crédits d'impôt** -- Dons aux associations (66% or 75%), emploi à domicile, frais de garde d'enfants, investissement locatif (Pinel, Denormandie), transition énergétique.
6. **Madelin / loi Madelin contracts** -- Prévoyance, mutuelle, retraite complémentaire for TNS (travailleurs non salariés). Deductible from BNC/BIC but within ceilings.
7. **Déficits antérieurs** -- Carryforward losses from prior years (not always on avis d'imposition).

Call `ask_user_input_v0` with:

```
Q: "Professional workspace?"
   Options: [
     "Dedicated room at home, used ONLY for work",
     "Shared space at home (not exclusively professional)",
     "Separate business premises (bureau, coworking)",
     "No fixed workspace / work at client sites"
   ]
```

If option 1 -> ask for the room area and total home area (for prorata calculation). Deductible share of rent/mortgage interest, electricity, internet, property tax (taxe foncière) proportional to area.
If option 2 -> flag as reviewer item: shared use reduces the deductible percentage. Often 10-30% accepted by the administration.
If option 3 -> rent is already captured in expenses. No home office calculation needed.
If option 4 -> skip home office entirely.

- **Children / dependents parts calculation** — Each child: +0.5 part for 1st and 2nd, +1 part from 3rd child onwards. Garde alternée: half the parts (0.25 / 0.25 / 0.5).

Call `ask_user_input_v0` with:

```
Q: "Dependents for quotient familial?"
   Options: [
     "No children or dependents",
     "1 child",
     "2 children",
     "3+ children (specify in follow-up)",
     "Children in garde alternée (shared custody)"
   ]
```

Call `ask_user_input_v0` with:

```
Q: "Any of these apply?"
   Options: [
     "Dons aux associations / organismes d'intérêt général",
     "Emploi d'un salarié à domicile",
     "Frais de garde d'enfants (< 6 ans)",
     "Cotisations Madelin (prévoyance, retraite, mutuelle)",
     "None of these"
   ]
```

Flag all crédits/réductions with limits for reviewer confirmation.

## Section 7 -- The final handoff

Once gap-filling is done, produce a final handoff message and hand off to `fr-return-assembly`.

**Example handoff message:**

> Intake complete. Here's what's going to the return assembly:
>
> Micro-entrepreneur BNC, married with 1 child (2.5 parts), franchise en base TVA (but threshold exceeded -- TVA registration flag). Chiffre d'affaires €58,000, cotisations sociales €12,819, versement libératoire IR €1,276.
>
> I'm now going to run the full French return preparation. This covers:
> 1. TVA analysis and registration obligation assessment
> 2. Déclaration de revenus (2042 / 2042-C-PRO)
> 3. Cotisations sociales reconciliation (URSSAF)
> 4. CFE verification
> 5. Prélèvement à la source rate update for 2026
>
> You'll get back:
> 1. A working paper with all forms and computations
> 2. A reviewer brief with positions, citations, and flags for your expert-comptable
> 3. A filing calendar with all upcoming deadlines
>
> Starting now.

Then internally invoke `fr-return-assembly` with the structured intake package.

## Section 8 -- Structured intake package (internal format)

The downstream skill (`fr-return-assembly`) consumes a JSON structure. It is internal and not shown to the user unless they ask. Key fields:

```json
{
  "jurisdiction": "FR",
  "tax_year": 2025,
  "taxpayer": {
    "name": "",
    "date_of_birth": "",
    "marital_status": "single | married_joint | married_separate | pacs_joint | pacs_separate | single_parent",
    "parts_fiscales": 0,
    "children": [],
    "residency": "full_year",
    "siret": "",
    "activity_code_ape": "",
    "business_type": "micro_entrepreneur | ei_reel | eurl_ir | profession_liberale",
    "regime_fiscal": "micro_bnc | micro_bic | declaration_controlee | reel_simplifie_bic | reel_normal_bic",
    "regime_tva": "franchise_en_base | reel_simplifie | reel_normal",
    "urssaf_status": "registered | recently_registered | cipav",
    "acre_eligible": false,
    "versement_liberatoire_ir": false,
    "regime_matrimonial": "communaute_acquets | communaute_universelle | separation_biens | na"
  },
  "income": {
    "chiffre_affaires_ht": 0,
    "chiffre_affaires_ttc": 0,
    "tva_collected": 0,
    "client_breakdown": [],
    "eu_services": 0,
    "non_eu_services": 0,
    "other_income": {
      "salaires": 0,
      "revenus_fonciers": 0,
      "revenus_capitaux_mobiliers": 0,
      "plus_values": 0
    },
    "spouse_income": {
      "salaires": 0,
      "other": 0
    }
  },
  "expenses": {
    "charges_courantes": [],
    "immobilisations": [],
    "charges_mixtes": [],
    "blocked": [],
    "cotisations_madelin": {
      "prevoyance": 0,
      "retraite": 0,
      "mutuelle": 0
    }
  },
  "tva": {
    "regime": "franchise | reel_simplifie | reel_normal",
    "returns_filed": [],
    "tva_collectee_total": 0,
    "tva_deductible_total": 0,
    "credit_tva_bf": 0,
    "franchise_threshold_exceeded": false
  },
  "cotisations_sociales": {
    "regime": "micro_social | tns_reel",
    "declarations": [],
    "total_cotisations_paid": 0,
    "acre_applied": false,
    "cipav_affiliated": false,
    "versement_liberatoire_ir_paid": 0
  },
  "cfe": {
    "amount_paid": 0,
    "commune": ""
  },
  "prior_year": {
    "rfr": 0,
    "impot_net": 0,
    "parts_fiscales": 0,
    "pas_rate": 0,
    "deficits_reportables": 0,
    "bnc_bic_declared": 0
  },
  "home_office": {
    "qualifies": false,
    "percentage": 0,
    "method": "surface | forfait"
  },
  "credits_reductions": {
    "dons": 0,
    "emploi_domicile": 0,
    "garde_enfants": 0,
    "other": []
  },
  "open_flags": [],
  "refusals_triggered": [],
  "documents_received": []
}
```

## Section 9 -- Refusal handling

Refusals fire from either the refusal sweep (Section 2) or during inference (e.g., corporate structure discovered in documents).

- **R-FR-1 -- SASU / SAS** — "SASU and SAS are subject to impôt sur les sociétés. The dirigeant is an assimilé salarié. I'm set up for self-employed individuals filing personal income tax. You need an expert-comptable who handles IS returns and paie."
- **R-FR-2 -- EURL at IS** — "EURL at IS files corporate returns (liasse 2065). I handle personal income tax filings only."
- **R-FR-3 -- SCI** — "SCI (Société Civile Immobilière) has its own filing requirements (2072). This is outside my scope."
- **R-FR-4 -- SAS/SARL with >10 employees** — "Companies with more than 10 employees have complex payroll, DSN, and social obligations I don't cover. You need an expert-comptable with a cabinet social."
- **R-FR-5 -- Agricultural activity** — "Agricultural income (bénéfices agricoles) is filed on 2342/2143 and subject to MSA, not URSSAF. Different regime entirely. You need a CGA or expert-comptable specialising in agriculture."
- **R-FR-6 -- Non-resident** — "Non-residents file with the SIP des non-résidents and have different rules. I'm set up for full-year France residents only."
- **R-FR-7 -- Association** — "Associations (loi 1901) have separate filing obligations. Not in scope."

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

## Section 10 -- Self-checks

**Check IN1 -- No one-question-at-a-time prose in the refusal sweep.** If the skill asked "Question 1 of 10" or walked through questions as separate messages, check fails.

**Check IN2 -- Refusal sweep used ask_user_input_v0.** The first substantive interaction used the interactive tool, not prose questions.

**Check IN3 -- Upload-first flow honoured.** After refusal sweep, the skill asked for a document dump before asking any content questions.

**Check IN4 -- Documents were parsed and inferred before asking questions.** The inference summary (Section 5) was shown before gap-filling questions (Section 6).

**Check IN5 -- Gap-filling only asked about things NOT visible in documents.** If the skill asked "did you pay URSSAF" after the bank statement showed URSSAF debits, check fails.

**Check IN6 -- Open flags captured.** Anything ambiguous, risky, or attention-worthy during inference is in the `open_flags` list in the handoff package.

**Check IN7 -- Handoff to `fr-return-assembly` is explicit.** The user was told "I'm now going to run the return preparation," and the downstream orchestrator was explicitly invoked with the intake package.

**Check IN8 -- Reviewer step was stated upfront and reiterated before handoff.** The opening message mentioned expert-comptable signoff.

**Check IN9 -- Refusals were clean.** No hedging. Stop means stop.

**Check IN10 -- No meta-commentary about workflow phases.** The skill did not say "Phase 1," "Phase 2," etc.

**Check IN11 -- Total user-facing turn count is low.** Target: 8 turns or fewer from start to handoff for a prepared user (1 refusal batch + 1 upload + 1 confirmation + 1-3 gap fills + 1 handoff). More than 12 turns for a normal intake is a check failure.

- **Check IN12 -- TVA regime established** — Franchise en base vs réel simplifié vs réel normal was confirmed before inference, as it changes how every transaction is classified.
- **Check IN13 -- Franchise en base threshold verified** — €36,800 (services) or €91,900 (goods) EUR (If micro-entrepreneur CA exceeds these amounts, the franchise en base is lost and TVA registration is mandatory. This must be flagged.)

## Section 11 -- Performance targets

For a prepared user (documents in a folder, ready to upload):
- **Refusal sweep**: 60 seconds (1-2 interactive turns)
- **Document upload**: 2 minutes (1 upload turn)
- **Inference and confirmation display**: 1 minute Claude processing + 1 turn for user confirmation
- **Gap filling**: 2 minutes (2-3 interactive turns)
- **Handoff**: immediate
- **Total**: ~7 minutes

For an unprepared user (has to go fetch documents):
- Refusal sweep: same
- Document discovery: 10-20 minutes offline
- Rest: same
- **Total**: 15-25 minutes

## Section 12 -- Cross-skill references

**Inputs:** User-provided documents and answers.

**Outputs:** Structured intake package consumed by `fr-return-assembly`.

**Downstream skills triggered (via fr-return-assembly):**
- `france-tva` -- TVA return (CA3/CA12) or franchise en base verification
- `france-income-tax` -- Déclaration de revenus (2042 / 2042-C-PRO / 2035 / 2031)
- `france-cotisations` -- Cotisations sociales (URSSAF micro-social or TNS réel)
- `fr-estimated-tax` -- Prélèvement à la source rate update and acomptes contemporains

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
