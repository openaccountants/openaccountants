---
name: es-freelance-intake
description: ALWAYS USE THIS SKILL when a user asks for help preparing their Spain tax returns AND mentions freelancing, self-employment, autónomo, working por cuenta propia, or independent professional activity. Trigger on phrases like "help me do my taxes", "prepare my Modelo 100", "I'm autónomo in Spain", "I'm a freelancer in Spain", "do my taxes as an autónomo", "prepare my IRPF return", or any similar phrasing where the user is a Spain-resident self-employed individual needing tax return preparation. This is the REQUIRED entry point for the Spain self-employed tax workflow -- every other skill in the stack (spain-vat-return, es-income-tax, es-social-contributions, es-estimated-tax, es-return-assembly) depends on this skill running first to produce a structured intake package. Uses upload-first workflow -- the user dumps all their documents and the skill infers as much as possible before asking questions. Uses ask_user_input_v0 for structured questions instead of one-at-a-time prose. Built for speed. Spain full-year residents only; autónomos (self-employed individuals) only.
version: 0.1
---

# Spain Self-Employed Intake Skill v0.1

## What this file is

The intake orchestrator for Spain-resident self-employed individuals (autónomos). Every downstream Spain content skill (spain-vat-return, es-income-tax, es-social-contributions, es-estimated-tax) and the assembly orchestrator (es-return-assembly) depend on this skill running first to produce a structured intake package.

This skill does not compute any tax figures. Its job is to collect all the facts, parse all the documents, confirm everything with the user, and hand off a clean intake package to `es-return-assembly`.

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

**Do not ask questions that have already been answered.** If the refusal check established the user is on estimación directa, do not later ask about the tax determination method. Track what is known.

**Do not ask about things visible in uploaded documents.** If the RETA recibos show monthly contributions, do not ask "did you pay RETA." Confirm what you see, do not re-ask.

**Use `ask_user_input_v0` for any multiple-choice question.** Text input is only for genuinely open-ended data (names, addresses, specific amounts when they cannot be inferred).

**Prefer batching.** Ask 3 related questions in a single message when they do not depend on each other's answers.

**Be terse but complete.** No hedging, no "let me know if you have questions," no "I hope this helps."

**Exception for blocking decisions.** If a single question determines whether the user is in-scope or out-of-scope, ask it standalone.

---

## Section 1 -- The opening

When triggered, respond with ONE message that:

1. One-line greeting (no paragraph of expectation-setting)
2. One-line summary of the flow (scope check -> upload -> gaps -> handoff to return assembly)
3. One-line reviewer reminder (must be reviewed by qualified asesor fiscal before filing)
4. Launch the refusal sweep immediately using `ask_user_input_v0`

**Example first message:**

> Let's get your 2025 Spain returns ready. Quick scope check, then you upload your documents, then I fill in the gaps. Target time: 10 minutes.
>
> Reminder: everything I produce needs to be reviewed and signed off by a qualified asesor fiscal or gestor before you file anything with the AEAT. I'm not a substitute for professional review.
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
Q1: "Spanish residency in 2025?"
    Options: ["Full year (183+ days in Spain)", "Part year", "Did not live in Spain"]

Q2: "Business structure?"
    Options: ["Autónomo (persona física, trabajador por cuenta propia)", "Sociedad Limitada (SL)", "Sociedad Anónima (SA)", "Comunidad de bienes / Sociedad civil", "Not sure"]

Q3: "Alta en RETA (registered with Social Security as self-employed)?"
    Options: ["Yes, alta en RETA for all of 2025", "Yes, but only part of 2025", "No, not registered in RETA", "Not sure"]
```

**After the response, evaluate:**

- **Q1 = Full year** -> continue
- **Q1 = Part year** -> stop. "I'm set up for full-year Spanish residents only. Part-year residents have different rules around imputación temporal and may need to file in two jurisdictions. You need an asesor fiscal who handles non-resident or part-year returns."
- **Q1 = Did not live in Spain** -> stop. "I'm set up for Spanish tax residents only. Non-residents file Modelo 210 with different rules. You need an asesor fiscal who handles non-resident returns."

- **Q2 = Autónomo** -> continue
- **Q2 = SL** -> stop. "I don't cover corporate returns. Sociedades Limitadas file Impuesto sobre Sociedades (Modelo 200) with separate rules. You need an asesor fiscal familiar with corporate tax."
- **Q2 = SA** -> stop. "I don't cover corporate returns. Sociedades Anónimas file Impuesto sobre Sociedades with separate rules. You need an asesor fiscal."
- **Q2 = Comunidad de bienes** -> stop. "Comunidades de bienes and sociedades civiles have specific attribution-of-income rules (Modelo 184). You need an asesor fiscal familiar with this structure."
- **Q2 = Not sure** -> ask one follow-up: "Do you invoice clients in your own name using your NIF (DNI/NIE)? Or do you have a registered company (SL/SA) with a CIF? If you invoice in your own name, you're an autónomo."

- **Q3 = Yes, full year** -> continue
- **Q3 = Part year** -> continue with flag: RETA cuotas only deductible for months of alta. Prorate.
- **Q3 = Not registered** -> stop. "If you are performing economic activity without alta en RETA, that is a compliance issue that needs to be resolved first. Consult a gestor or laboralista."
- **Q3 = Not sure** -> ask one follow-up: "Do you pay a monthly cuota to the Seguridad Social (typically debited from your bank)? If yes, you're alta en RETA."

**After Q1-Q3 pass, ask the second batch of scope questions (also batched):**

```
Q4: "Estimación directa type?"
    Options: ["Estimación directa simplificada (default for most autónomos)", "Estimación directa normal", "Estimación objetiva (módulos)", "Not sure"]

Q5: "Comunidad autónoma (where you have your fiscal domicile)?"
    Options: ["Madrid", "Cataluña", "Andalucía", "Valencia", "País Vasco / Navarra (foral regime)", "Other (I'll specify)"]

Q6: "How long have you been autónomo?"
    Options: ["First year (2025)", "Second year", "Third year", "More than 3 years"]
```

**Evaluate Q4:**
- **Simplificada** -> continue. Standard method for most autónomos. 5% gastos de difícil justificación (max EUR 2,000).
- **Normal** -> continue. Full accounting required, no simplified expense allowance.
- **Objetiva (módulos)** -> stop. "I'm set up for estimación directa only. Módulos uses a different calculation method based on physical parameters (surface, employees, kW). You need a gestor familiar with estimación objetiva."
- **Not sure** -> "If your turnover is under EUR 600,000 and you haven't specifically elected estimación directa normal, you're on simplificada by default."

**Evaluate Q5:**
- **Madrid through Other** -> note for IRPF autonómica tramo. Continue.
- **País Vasco / Navarra** -> stop. "The foral territories (Bizkaia, Gipuzkoa, Araba, Navarra) have their own tax agencies and different income tax rules (IRPF foral). I'm set up for territorio común (AEAT) only. You need an asesor fiscal in your foral territory."

**Evaluate Q6:**
- **First year / Second year / Third year** -> flag: retención reducida del 7% on professional invoices (instead of 15%) applies for the year of alta and the two following calendar years.
- **More than 3 years** -> standard 15% retención on professional invoices.

**Total time:** ~45 seconds if the user taps through.

---

## Section 3 -- The dump

Once the refusal sweep passes, immediately ask for the document dump. Single message. No preamble.

**Example:**

> Scope is good. Now upload everything you have for 2025 -- drop it all in at once:
>
> - Business bank statement(s) for all of 2025 (PDF or CSV)
> - Facturas emitidas (sales invoices issued in 2025)
> - Facturas recibidas (purchase invoices / receipts for business expenses)
> - Copies of Modelo 303 (IVA trimestral) filed for Q1-Q3 2025
> - Modelo 130 copies (pagos fraccionados IRPF) filed for Q1-Q3 2025
> - RETA recibos (monthly Social Security contribution receipts)
> - Prior year Modelo 100 (IRPF annual return) or borrador
> - Modelo 390 (IVA annual summary) from prior year
> - Any AEAT notifications or correspondence
> - Capital asset purchase receipts (computers, equipment, vehicles)
> - Home-related documents if claiming despacho en casa (mortgage interest, IBI, community fees, utility bills)
> - Anything else tax-related you have
>
> Don't worry about labeling or organizing -- I'll figure out what each file is. Drag and drop when ready.

Then wait. Do not ask any other questions while waiting.

**If the user uploads a partial dump and says "that's what I have":** move to inference. Do not demand more. Request specific missing items during gap-filling.

**If the user says "I don't know what I have":** Switch to guided mode:
> Check these places:
> - Business bank: download 2025 statements as PDF or CSV
> - Sede electrónica AEAT (agenciatributaria.gob.es): download Modelo 303, 130, prior 100
> - Email: search for "factura", "IVA", "IRPF", "AEAT", "Seguridad Social"
> - Your gestor or asesor fiscal from last year, if you had one
> - Import@ss portal: download RETA contribution history
> - Cloud storage for saved invoices
>
> Come back when you have something to upload. I'll work with whatever you bring.

---

## Section 4 -- The inference pass

When documents arrive, parse each one. For each document, extract:

**Bank statement:**
- Total deposits (candidate gross receipts / ingresos)
- Recurring inflows (client payments with names)
- Outflows to AEAT (IVA payments, pagos fraccionados, with dates)
- Outflows to Seguridad Social / TGSS (RETA cuotas with dates and amounts)
- Outflows to suppliers (business expenses / gastos by category)
- Equipment purchases (potential capital items / inmovilizado)
- Transfers to personal account (owner draws)
- Rent payments (office or coworking space)
- SaaS / software subscriptions
- Insurance payments (responsabilidad civil, seguro de salud)
- Professional body fees (colegios profesionales)

**Facturas emitidas (sales invoices):**
- Client names and amounts (base imponible)
- Whether IVA was charged (21%, 10%, 4%, or exento)
- Whether retención was applied (15% or 7% for new autónomos)
- Total turnover reconciliation against bank deposits
- Any EU clients (intracomunitarias -- reverse charge, ROI listing)
- Any non-EU clients (exportaciones de servicios)
- SAC / CNAE activity codes

**Facturas recibidas (purchase invoices):**
- Expense category (gasto corriente vs inmovilizado)
- IVA soportado (deducible) amounts
- Supplier NIF/CIF
- Any items that are gastos no deducibles (entertainment/gifts above limits, fines)
- Any items above capital threshold (inmovilizado -- amortización)

**Prior year Modelo 100:**
- Prior year IRPF liability
- Rendimiento neto de actividades económicas
- Filing status and applicable deductions
- Comunidad autónoma tramo rates applied
- Amortisation schedule (continuing depreciation)

**Modelo 303 copies (quarterly IVA):**
- Quarterly base imponible and IVA devengado (output IVA)
- IVA soportado deducible (deductible input IVA)
- Result per quarter (a ingresar or a compensar)
- Any accumulated credit (saldo a compensar)

**Modelo 130 copies (pagos fraccionados):**
- Quarterly rendimiento neto acumulado
- 20% pago fraccionado computed
- Retenciones acumuladas deducted
- Amount paid per quarter

**RETA recibos:**
- Monthly RETA cuota paid (amount and month)
- Base de cotización (contribution base)
- Whether tarifa plana was applied (EUR 80/month for new autónomos in first year)
- Total annual RETA paid

**After parsing everything, build an internal inference object.** Do not show the raw inference yet -- transform it into a compact summary for the user in Section 5.

---

## Section 5 -- The confirmation

After inference, present a single compact summary message. Use a structured format that is fast to scan. Invite the user to correct anything wrong.

**Example summary message:**

> Here's what I pulled from your documents. Skim and tell me what's wrong.
>
> **Identity**
> - María García López, NIF: 12345678A
> - Full-year Spanish resident (Madrid)
> - Autónoma, estimación directa simplificada
> - Alta en RETA since March 2023 (more than 3 years -- 15% retención)
> - IAE/CNAE: 8411 -- Servicios de consultoría de gestión
>
> **Ingresos (from bank statement + facturas emitidas)**
> - Ingresos brutos (base imponible): ~EUR 48,000
>   - Consultoría ABC SL: EUR 24,000 (retainer mensual)
>   - Tech Solutions GmbH (Germany): EUR 12,000 (intracomunitaria, reverse charge)
>   - Various domestic clients: EUR 12,000
> - IVA repercutido (21%): ~EUR 7,560 (on domestic supplies)
> - Retenciones soportadas (15%): ~EUR 5,400 (on domestic professional invoices)
>
> **Gastos (from bank statement + facturas recibidas)**
> - Alquiler oficina / coworking: EUR 3,600
> - Software / SaaS: EUR 1,200
> - Seguro de responsabilidad civil: EUR 350
> - Gestoría: EUR 600
> - Teléfono / internet: EUR 720 (TBD -- need business use %)
> - Material de oficina: EUR 400
> - Laptop: EUR 1,500 (June 2025) -- inmovilizado, amortización 25%
> - IVA soportado deducible: ~EUR 1,350
> - Gastos de difícil justificación (5%): TBD after net income calc (max EUR 2,000)
>
> **RETA (from recibos)**
> - Monthly cuota: EUR 300 x 12 = EUR 3,600
> - Base de cotización: EUR 1,000/month
> - Total 2025 RETA: EUR 3,600 (gasto deducible in IRPF)
>
> **Modelo 303 (IVA trimestral -- from filed returns)**
> - Q1-Q3 filed
> - Q4 outstanding
> - Accumulated IVA a compensar: EUR 0
>
> **Modelo 130 (pagos fraccionados -- from filed returns)**
> - Q1-Q3 filed
> - Q4 outstanding
> - Pagos fraccionados acumulados: EUR 2,100 (20% of net x 3 quarters)
>
> **Retenciones (from facturas emitidas)**
> - Total retenciones soportadas: EUR 5,400
> - These credit against final IRPF cuota
>
> **Prior year (from 2024 Modelo 100)**
> - 2024 IRPF cuota líquida: EUR 5,200
> - 2024 rendimiento neto actividades: EUR 28,000
> - Comunidad autónoma: Madrid
>
> **Flags I already see:**
> 1. Phone / internet -- need business use percentage
> 2. EU client (Germany) -- verify ROI inscription and Modelo 349 filing
> 3. Q4 2025 Modelo 303 not yet filed -- will prepare as part of this workflow
> 4. Q4 2025 Modelo 130 not yet filed -- will prepare
> 5. Home office -- not yet established if despacho en casa applies
>
> **Is any of this wrong? Reply "looks good" or tell me what to fix.**

---

## Section 6 -- Gap filling

After the user confirms the summary (or corrects it), ask about things that cannot be inferred from documents. Use `ask_user_input_v0` where possible.

**Things that usually cannot be inferred:**

1. **Home office (despacho en casa)** -- Cannot tell from documents whether a dedicated workspace exists.
2. **Private use percentage** -- Phone, internet, vehicle business-use split.
3. **Capital items from prior years** -- Continuing amortisation on assets acquired before 2025.
4. **Exempt activities** -- Whether any income is IVA-exempt (medical, educational, financial).
5. **Personal deductions** -- Aportaciones a planes de pensiones, deducción por vivienda habitual (if pre-2013 mortgage), deducción por maternidad, etc.
6. **Other income** -- Employment income, rental income, capital gains, savings income.

**Home office gap-filling example:**

Call `ask_user_input_v0` with:

```
Q: "Home office (despacho en casa)?"
   Options: [
     "Dedicated room, used ONLY for work, declared in Modelo 036/037",
     "Dedicated corner/desk, used ONLY for work",
     "Shared space (kitchen table, living room)",
     "Separate business premises (not at home)",
     "No fixed workspace"
   ]
```

If option 1 -> ask for proportion of home used (m2 of office / m2 total). Deductible: proportional share of rent/mortgage interest, IBI, comunidad, utilities (30% of proportional share for suministros under simplificada).
If option 2 -> flag for reviewer: partial home office without Modelo 036 declaration is weak.
If option 3 -> "A shared space is very difficult to defend as despacho en casa with the AEAT. I'll skip this deduction."
If option 4 -> rent is already captured in expenses. No home office calculation needed.
If option 5 -> skip home office entirely.

**Private use percentage example:**

Call `ask_user_input_v0` with:

```
Q: "Phone / internet -- business use?"
   Options: [
     "Exclusive business line (separate from personal)",
     "80%+ business use",
     "50-80% business use",
     "Under 50% business use"
   ]
```

For phone: if exclusive business line, 100% deductible. Otherwise apply percentage.
For vehicle: autónomos in estimación directa can deduct 50% IVA by default on vehicle (unless exclusively business use proven). Flag as standard treatment.

**Personal deductions example:**

Call `ask_user_input_v0` with:

```
Q: "Aportaciones a planes de pensiones in 2025?"
   Options: [
     "Yes -- I'll provide the amount",
     "No aportaciones",
     "Not sure"
   ]
```

If yes -> ask for amount (max EUR 1,500 individual, or EUR 8,500 if empresa plan).

---

## Section 7 -- The final handoff

Once gap-filling is done, produce a final handoff message and hand off to `es-return-assembly`.

**Example handoff message:**

> Intake complete. Here's what's going to the return assembly:
>
> Autónoma, full-year Madrid resident, estimación directa simplificada. Ingresos brutos EUR 48,000, estimated rendimiento neto ~EUR 32,000 after gastos and RETA.
>
> I'm now going to run the full Spain return preparation. This covers:
> 1. Modelo 303 (IVA trimestral -- Q4 2025)
> 2. IRPF Modelo 100 (annual income tax return 2025)
> 3. RETA reconciliation (cotizaciones sociales)
> 4. Modelo 130 (pagos fraccionados -- Q4 2025)
>
> You'll get back:
> 1. An Excel working paper with all computations and live formulas
> 2. A reviewer brief with positions, citations, and flags for your asesor fiscal
> 3. A filing calendar with all upcoming deadlines
>
> Starting now.

Then internally invoke `es-return-assembly` with the structured intake package.

---

## Section 8 -- Structured intake package (internal format)

The downstream skill (`es-return-assembly`) consumes a JSON structure. It is internal and not shown to the user unless they ask. Key fields:

```json
{
  "jurisdiction": "ES",
  "tax_year": 2025,
  "taxpayer": {
    "name": "",
    "nif": "",
    "residency": "full_year",
    "comunidad_autonoma": "",
    "alta_reta_date": "",
    "years_as_autonomo": 0,
    "estimacion": "directa_simplificada | directa_normal",
    "entity_type": "autonomo",
    "iae_cnae": "",
    "retencion_rate": "15 | 7"
  },
  "income": {
    "ingresos_brutos": 0,
    "iva_repercutido": 0,
    "retenciones_soportadas": 0,
    "intracomunitarias": 0,
    "exportaciones": 0,
    "other_income": 0,
    "client_breakdown": []
  },
  "expenses": {
    "gastos_deducibles": [],
    "gastos_mixed_use": [],
    "gastos_no_deducibles": [],
    "inmovilizado": [],
    "gastos_dificil_justificacion_pct": 5,
    "total_gastos": 0
  },
  "iva": {
    "modelo_303_filed": [],
    "iva_devengado_total": 0,
    "iva_soportado_deducible_total": 0,
    "saldo_compensar": 0,
    "exempt_activities": false,
    "prorrata": false
  },
  "reta": {
    "monthly_cuota": 0,
    "base_cotizacion": 0,
    "months_alta": 12,
    "tarifa_plana": false,
    "total_reta_paid": 0
  },
  "pagos_fraccionados": {
    "modelo_130_filed": [],
    "total_pagos": 0,
    "retenciones_deducted": 0
  },
  "prior_year": {
    "irpf_cuota_liquida": 0,
    "rendimiento_neto": 0,
    "amortisation_schedule": []
  },
  "home_office": {
    "qualifies": false,
    "percentage_m2": 0,
    "declared_036": false,
    "rent_or_mortgage": 0,
    "ibi": 0,
    "comunidad": 0,
    "suministros_total": 0
  },
  "private_use": {
    "phone_business_pct": 0,
    "internet_business_pct": 0,
    "vehicle_business_pct": 0
  },
  "personal_deductions": {
    "planes_pensiones": 0,
    "vivienda_habitual": 0,
    "maternidad": false,
    "other": []
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

> Stop -- you operate through a Sociedad Limitada. I'm set up for autónomos (personas físicas) only. SLs file Impuesto sobre Sociedades (Modelo 200) with separate rules for administrator remuneration, dividends, and corporate tax. You need an asesor fiscal familiar with corporate returns.
>
> I can't help with this one.

---

## Section 10 -- Self-checks

**Check IN1 -- No one-question-at-a-time prose in the refusal sweep.** If the skill asked "Question 1 of 10" or walked through questions as separate messages, check fails.

**Check IN2 -- Refusal sweep used ask_user_input_v0.** The first substantive interaction used the interactive tool, not prose questions.

**Check IN3 -- Upload-first flow honoured.** After refusal sweep, the skill asked for a document dump before asking any content questions.

**Check IN4 -- Documents were parsed and inferred before asking questions.** The inference summary (Section 5) was shown before gap-filling questions (Section 6).

**Check IN5 -- Gap-filling only asked about things NOT visible in documents.** If the skill asked "did you pay RETA" after bank statements showed TGSS debits, check fails.

**Check IN6 -- Open flags captured.** Anything ambiguous, risky, or attention-worthy during inference is in the `open_flags` list in the handoff package.

**Check IN7 -- Handoff to `es-return-assembly` is explicit.** The user was told "I'm now going to run the return preparation," and the downstream orchestrator was explicitly invoked with the intake package.

**Check IN8 -- Reviewer step was stated upfront and reiterated before handoff.** The opening message mentioned asesor fiscal signoff.

**Check IN9 -- Refusals were clean.** No hedging. Stop means stop.

**Check IN10 -- No meta-commentary about workflow phases.** The skill did not say "Phase 1," "Phase 2," etc.

**Check IN11 -- Total user-facing turn count is low.** Target: 8 turns or fewer from start to handoff for a prepared user (1 refusal batch + 1 upload + 1 confirmation + 1-3 gap fills + 1 handoff). More than 12 turns for a normal intake is a check failure.

**Check IN12 -- Estimación directa type and retención rate established.** Simplificada vs normal confirmed, and 7% vs 15% retención determined, before handoff.

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

**Outputs:** Structured intake package consumed by `es-return-assembly`.

**Downstream skills triggered (via es-return-assembly):**
- `spain-vat-return` -- Modelo 303 quarterly IVA return
- `es-income-tax` -- IRPF Modelo 100 annual return
- `es-social-contributions` -- RETA cotizaciones sociales
- `es-estimated-tax` -- Modelo 130 pagos fraccionados

---

### Change log

- **v0.1 (April 2026):** Initial draft. Upload-first, inference-then-confirm pattern modelled on mt-freelance-intake v0.1.

## End of Intake Skill v0.1


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as an asesor fiscal, gestor administrativo, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
