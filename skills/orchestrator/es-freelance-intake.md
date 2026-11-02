---
name: es-freelance-intake
description: ALWAYS USE THIS SKILL when a user asks for help preparing their Spain tax returns AND mentions freelancing, self-employment, autónomo, working por cuenta propia, or independent professional activity. Trigger on phrases like "help me do my taxes", "prepare my Modelo 100", "I'm autónomo in Spain", "I'm a freelancer in Spain", "do my taxes as an autónomo", "prepare my IRPF return", or any similar phrasing where the user is a Spain-resident self-employed individual needing tax return preparation. This is the REQUIRED entry point for the Spain self-employed tax workflow -- every other skill in the stack (es-vat-return, es-income-tax, es-social-contributions, es-estimated-tax, es-return-assembly) depends on this skill running first to produce a structured intake package. Uses upload-first workflow -- the user dumps all their documents and the skill infers as much as possible before asking questions. Uses ask_user_input_v0 for structured questions instead of one-at-a-time prose. Built for speed. Spain full-year residents only; autónomos (self-employed individuals) only.
version: 0.4
jurisdiction: ES
tax_year: 2026
last_updated: 2026-10-31
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Spain: intake for a self-employed client (autónomo)

The entry point for the Spanish self-employed workflow. This skill gathers facts and routes; it computes nothing. It establishes residence and territory, the census position with the tax office, the RETA position with Social Security, the activity and its IAE heading, the income tax regime, the VAT position, the withholding on invoices and whether there are employees, then hands a structured package to the skills that do the work. Figures are for tax year 2026. Every figure below is only here because its answer changes which downstream skill applies or which document must be asked for; the computation of each one belongs to the skill named beside it.

## What this file is

The intake orchestrator for Spain-resident self-employed individuals (autónomos). Every downstream Spain skill (`es-vat-return`, `es-income-tax`, `es-social-contributions`, `es-estimated-tax`) and the assembly orchestrator (`es-return-assembly`) depend on this skill running first to produce a structured intake package. The whole picture of being self-employed in Spain, if the client wants the background rather than a return, is `es-autonomous-worker`.

This skill does not compute any tax figure. Its job is to collect the facts, parse the documents, confirm everything with the user, and hand a clean intake package to `es-return-assembly`.

## Design principles

Upload first, infer, then confirm:

1. **Compact refusal sweep** using `ask_user_input_v0`, three interactive questions, about thirty seconds.
2. **Upload-first workflow.** After the refusal check, the user drops in everything they have.
3. **Inference pass.** Parse every document and extract as much as possible.
4. **Gap filling only.** Ask the user ONLY about what is missing, ambiguous, or needs confirmation.
5. **Single confirmation pass** at the end: show the full picture, let the user correct anything wrong, hand off to the downstream skills.

Target: intake completes in five minutes for a prepared user, fifteen minutes for a user who has to go and fetch documents.

## Critical operating principles

**Do not narrate the workflow.** Do not say "Phase 1," "Phase 2," "Now I'll ask you about deductions." Just do the work.

**Do not ask questions that have already been answered.** If the refusal check established the user is on estimación directa, do not later ask about the tax determination method. Track what is known.

**Do not ask about things visible in uploaded documents.** If the RETA recibos show monthly contributions, do not ask "did you pay RETA." Confirm what you see, do not re-ask.

**Use `ask_user_input_v0` for any multiple-choice question.** Text input is only for genuinely open-ended data: names, addresses, and amounts that cannot be inferred.

**Prefer batching.** Ask three related questions in a single message when they do not depend on each other's answers.

**Be terse but complete.** No hedging, no "let me know if you have questions," no "I hope this helps."

**Exception for blocking decisions.** If a single question determines whether the user is in scope or out of scope, ask it standalone.

**Never state a rate or a threshold from memory.** The tables in this skill carry the ones intake needs. Everything else is the downstream skill's job.

## Section 1: the opening

When triggered, respond with ONE message that:

1. Gives a one-line greeting, with no paragraph of expectation setting.
2. Gives a one-line summary of the flow: scope check, then upload, then gaps, then handoff to return assembly.
3. Gives a one-line reviewer reminder: the work must be reviewed by a qualified asesor fiscal before filing.
4. Launches the refusal sweep immediately using `ask_user_input_v0`.

**Example first message:**

> Let's get your 2026 Spain returns ready. Quick scope check, then you upload your documents, then I fill in the gaps. Target time: ten minutes.
>
> Reminder: everything I produce needs to be reviewed and signed off by a qualified asesor fiscal or gestor before you file anything with the Agencia Tributaria. I am not a substitute for professional review.
>
> Scope check:

Then immediately call `ask_user_input_v0` with the refusal questions.

**Do NOT:**
- Write a welcome paragraph
- Explain the phases
- Ask "are you ready to start"
- List what documents you will eventually need
- Give a disclaimer beyond the one reviewer line

## Section 2: refusal sweep (compact)

Present the refusal sweep as a single `ask_user_input_v0` call with three questions, all single select.

**The three questions to ask first:**

~~~
Q1: "Were you a Spanish tax resident for 2026?"
    Options: ["Yes: more than 183 days in Spain in 2026, or my main business or economic interests are in Spain", "No: I was not resident in Spain in 2026", "I moved to or from Spain during 2026, or I am not sure"]

Q2: "Business structure?"
    Options: ["Autonomo (persona fisica, trabajador por cuenta propia)", "Sociedad Limitada (SL)", "Sociedad Anonima (SA)", "Comunidad de bienes / sociedad civil", "Not sure"]

Q3: "Alta en RETA (registered with Social Security as self-employed)?"
    Options: ["Yes, alta en RETA for all of 2026", "Yes, but only part of 2026", "No, not registered in RETA", "Not sure"]
~~~

Residence is decided for the whole calendar year, because the income tax period is the calendar year (art. 12 Ley 35/2006, outside the case of death). Under art. 9.1 of the same Law a person is resident if EITHER they spend more than 183 days of the calendar year in Spain, counting sporadic absences unless they prove tax residence in another country, OR the main centre or base of their activities or economic interests is in Spain, directly or indirectly. Residence is also presumed, unless the contrary is proved, where the spouse who is not legally separated and the dependent minor children habitually live in Spain. Law: https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764 Spain has no part-year resident: a person who moves in or out during the year is either resident for the whole of it or not resident for any of it.

- **Q1 = Resident.** Continue.
- **Q1 = Not resident.** Stop. "I'm set up for Spanish tax residents only. Non-residents are taxed under the non-resident income tax, usually on Modelo 210, with different rules. You need an asesor fiscal who handles non-resident returns." Route the reader to `es-non-resident-income-tax-irnr-and`.
- **Q1 = Moved, or not sure.** Stop. "In a year you moved, the residence test has to be applied to the whole year, and a treaty may decide which country taxes you. That needs an asesor fiscal before any return is prepared."
- **Q2 = Autónomo.** Continue.
- **Q2 = SL.** Stop. "I don't cover corporate returns. Sociedades Limitadas file Impuesto sobre Sociedades (Modelo 200) with separate rules for administrator remuneration, dividends, and corporate tax. You need an asesor fiscal familiar with corporate tax." Route the reader to `es-corporate-tax`.
- **Q2 = SA.** Stop, same reason.
- **Q2 = Comunidad de bienes.** Stop. "Comunidades de bienes and sociedades civiles have attribution-of-income rules of their own (Modelo 184). You need an asesor fiscal familiar with this structure."
- **Q2 = Not sure.** Ask one follow-up: "Do you invoice clients in your own name using your NIF? Or do you have a registered company with its own tax number? If you invoice in your own name, you're an autónomo."
- **Q3 = Yes, full year RETA.** Continue.
- **Q3 = Part year RETA.** Continue with a flag: record the dates of alta and baja, and pass them to `es-social-contributions` and `es-income-tax`. Only the cuotas shown on the recibos for the months of alta are collected.
- **Q3 = Not registered.** Stop. "If you are carrying on an economic activity without alta en RETA, that is a compliance issue that has to be resolved first. Consult a gestor or a laboralista."
- **Q3 = Not sure.** Ask one follow-up: "Do you pay a monthly cuota to the Seguridad Social, usually debited from your bank? If yes, you're alta en RETA."

**After Q1 to Q3 pass, ask the second batch of scope questions, also batched:**

~~~
Q4: "Estimacion directa type?"
    Options: ["Estimacion directa simplificada", "Estimacion directa normal", "Estimacion objetiva (modulos)", "Not sure"]

Q5: "Where is your fiscal domicile?"
    Options: ["Territorio comun (peninsula or Baleares)", "Canarias", "Ceuta", "Melilla", "Pais Vasco (Alava, Bizkaia, Gipuzkoa)", "Navarra"]

Q6: "In which year did you first register the activity?"
    Options: ["This year", "Last year", "Two years ago", "Earlier than that"]
~~~

- **Q4 = Simplificada.** Continue. The hard-to-justify deduction and the turnover limit that governs simplificada are in the Reglamento del IRPF table in Section 6.
- **Q4 = Normal.** Continue. Full accounting, and no hard-to-justify deduction.
- **Q4 = Objetiva (módulos).** Stop. "I'm set up for estimación directa only. Módulos computes the result from physical parameters, not from your books. You need a gestor familiar with estimación objetiva." Before saying anyone is outside módulos, read the warning under the two module tables in Section 6: the statute and the Agencia Tributaria page state different limits.
- **Q4 = Not sure.** Under art. 28.1 of the Reglamento del IRPF, estimación directa simplificada applies where all three conditions are met: the activity is not in estimación objetiva, the prior year's net turnover for all those activities together does not exceed the limit in the Section 6 table, and the taxpayer has not renounced the simplified method. Ask for the last filed Modelo 100 or the Modelo 036 and read it off the return rather than guessing.
- **Q5 = Territorio común.** Continue. VAT applies, and the autonomous community half of the income tax scale is that community's own.
- **Q5 = Canarias.** Continue with a flag. Art. 3 Ley 37/1992 excludes the Canary Islands from the territory where Spanish VAT applies, so an activity there charges the Canary indirect tax, IGIC, not VAT, and files no Modelo 303 for it. The IGIC general rate is in the Ley 4/2012 table in Section 6; the Canary returns themselves are outside this workflow.
- **Q5 = Ceuta or Melilla.** Continue with a flag. Art. 3 Ley 37/1992 also excludes Ceuta and Melilla from the VAT territory, and IGIC does not apply there either: these cities charge their own IPSI. There is also an income tax credit, a contribution bonification, and a cut to SOME withholding rates. For Ceuta only, in 2026 the hard-to-justify percentage in simplificada is also raised, and that raised figure counts for the Modelo 130 payments whose filing window opens from October 2026 (disposición adicional 64 Ley 35/2006): flag both for `es-income-tax` and `es-estimated-tax`. The cut is granted rule by rule, not across the board: this skill shows it only where the article that grants it is quoted, which is the professional invoice rates and the rent rate in the Section 6 tables.
- **Q5 = País Vasco or Navarra.** Stop. "The foral territories (Álava, Bizkaia, Gipuzkoa, Navarra) have their own tax agencies and their own income tax law. I'm set up for territorio común only. You need an asesor fiscal in your foral territory."
- **Q6.** Sets which withholding rate a professional invoice should carry. Under art. 95.1 of the Reglamento del IRPF the reduced rate runs for the tax period in which the professional activity starts and the two following periods, and only where no professional activity at all was carried on in the year before the start date. The rates are in the withholding table in Section 6. Do not infer the rate from the answer alone: read it off the invoices.

**Third batch, the activity and the indirect tax position:**

~~~
Q7: "What is the activity, and which IAE heading is it registered under?"
    Free text, plus: "Section one (empresarial), section two (profesional) or section three (artistic)?"

Q8: "VAT position?"
    Options: ["Regimen general", "Recargo de equivalencia (retail)", "Exempt activity (medical, teaching, insurance, financial)", "Mixed: some exempt, some taxable", "Not sure"]

Q9: "Do you have employees, or do you withhold on anything you pay out?"
    Options: ["Employees on payroll", "No employees, but I pay rent for business premises", "No employees, but I pay other professionals", "None of these"]

Q10: "Do you invoice everything to one single client, or are you registered as an economically dependent self-employed worker (TRADE)?"
    Options: ["Yes, one single client", "Yes, I am a TRADE", "No, several clients", "Not sure"]
~~~

- **Q7.** The IAE heading decides whether clients withhold. Under art. 95.2 of the Reglamento del IRPF, income from the activities in sections two AND three of the IAE tariffs is professional income, and a payer obliged to withhold applies the professional rates to it. Most section one headings are not withheld on, but not all: under art. 95.6 certain section one activities taxed under the module method are withheld on, and so are farming, livestock and forestry activities under art. 95.4 and 95.5. Check the activity against art. 95 before telling a client there is no withholding: https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820 The CNAE code is a statistics code and is asked for separately; it does not decide withholding.
- **Q8 = Régimen general.** Continue. Modelo 303 each quarter.
- **Q8 = Recargo de equivalencia.** Continue with a flag, and do not prepare a Modelo 303 for those sales. Under art. 148.Uno Ley 37/1992 the regime applies to retail traders who are individuals, or entities under the income attribution regime, in the sectors and on the conditions set by regulation. Under art. 154 the supplier charges the surcharge on the invoice; the retailer neither settles nor pays VAT on the sales the regime covers, and deducts no input VAT on goods and services used in that activity. Intra-Community acquisitions and the purchases in art. 84.Uno.2 (reverse charge) are still self-assessed. The rates and the retailer test are in the Ley del IVA table in Section 6.
- **Q8 = Exempt activity.** Continue with a flag. Medical and health care, teaching, insurance and financial services are exempt under art. 20.Uno Ley 37/1992: https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740 Input VAT on costs used for exempt supplies is generally not deductible; art. 94.Uno lists the exceptions, among them insurance and financial services that would be exempt if made in Spain, where the customer is established outside the European Union or the service is directly linked to an export out of it. A client who makes ONLY supplies exempt under art. 20 or art. 26 files neither the periodic VAT return nor the annual summary (art. 71.1 and 71.7 of the Reglamento del IVA): https://www.boe.es/buscar/act.php?id=BOE-A-1992-28925
- **Q8 = Mixed.** Flag for the reviewer: a prorrata or a separate sector of activity may apply. That is `es-vat-return` work, not intake work.
- **Q8 = Not sure.** Read it off the last Modelo 303 or off the Modelo 036. Do not assume the general regime for a shop.
- **Q9 = Employees.** Flag: the client is a withholder and files Modelo 111, which art. 108.1 of the Reglamento del IRPF sets as quarterly in the first twenty calendar days of April, July, October and January (a monthly regime applies to large businesses), and Modelo 190 annually, and is an employer with the Seguridad Social. Payroll is `spain-payroll`; the withholding return itself is `es-modelo-111`.
- **Q9 = Rent for business premises.** Flag: withholding on the rent, declared on Modelo 115, unless one of the exceptions applies. Ask for the rent paid to each landlord separately over the year, because the amount exception is tested landlord by landlord. The rate and the exceptions are in the two rent tables in Section 6.
- **Q9 = Pays other professionals.** Flag: withholding on those invoices too, on Modelo 111.
- **Q10 = One client or TRADE.** Flag for `es-income-tax`. Art. 32.2 Ley 35/2006 gives a reduction of net income to a self-employed person whose supplies all go to one single unrelated client, or who is an economically dependent self-employed worker under Ley 20/2007, and who meets the other conditions of that article. In simplificada that reduction and the hard-to-justify deduction cannot both be taken (art. 32.2.2.º.a of the Law and art. 30, rule 2.ª, of the Reglamento). Intake records the facts; the choice belongs to `es-income-tax`.

**Total time:** about forty-five seconds if the user taps through the first two batches.

## Section 3: the dump

Once the refusal sweep passes, immediately ask for the document dump. Single message. No preamble.

**Example:**

> Scope is good. Now upload everything you have for 2026, all at once:
>
> - Business bank statements for the whole year (PDF or CSV)
> - Facturas emitidas (sales invoices issued in the year)
> - Facturas recibidas (purchase invoices and receipts for business expenses)
> - Copies of every Modelo 303 (IVA trimestral) filed so far
> - Copies of every Modelo 130 (pagos fraccionados) filed so far
> - Modelo 036 (the census declaration), and any later Modelo 036 amending it
> - RETA recibos (monthly Social Security receipts), and the resolution granting any reduced starting contribution
> - The prior year Modelo 100 (annual IRPF return) or its borrador
> - Modelo 390 (annual VAT summary) from the prior year
> - Modelo 111, 115, 190, 349 or 347 if you file any of them
> - Any Agencia Tributaria or Seguridad Social notification or correspondence
> - Capital asset purchase receipts: computers, equipment, vehicles
> - Home-related documents if you claim a despacho en casa: mortgage interest or rent, IBI, community fees, utility bills
> - Anything else tax related that you have
>
> Don't worry about labelling or organising. I'll work out what each file is. Drag and drop when ready.

Then wait. Do not ask any other question while waiting.

**If the user uploads a partial dump and says "that's what I have":** move to inference. Do not demand more. Request specific missing items during gap filling.

**If the user says "I don't know what I have":** switch to guided mode:

> Check these places:
> - Business bank: download the year's statements as PDF or CSV
> - Sede electrónica of the Agencia Tributaria: download Modelo 303, Modelo 130, Modelo 036 and the prior year Modelo 100
> - Email: search for "factura", "IVA", "IRPF", "Agencia Tributaria", "Seguridad Social"
> - Your gestor or asesor fiscal from last year, if you had one
> - Import@ss portal: download the RETA contribution history
> - Cloud storage for saved invoices
>
> Come back when you have something to upload. I'll work with whatever you bring.

## Section 4: the inference pass

When documents arrive, parse each one. For each document, extract:

**Bank statement:**
- Total deposits, as candidate gross receipts (ingresos)
- Recurring inflows, with client names
- Outflows to the Agencia Tributaria: VAT payments and pagos fraccionados, with dates
- Outflows to the Tesorería General de la Seguridad Social: RETA cuotas with dates and amounts
- Outflows to suppliers: business expenses (gastos) by category
- Equipment purchases, as candidate capital items (inmovilizado)
- Transfers to a personal account (owner draws)
- Rent payments for an office or coworking space
- Software subscriptions
- Insurance payments: responsabilidad civil, seguro de salud
- Professional body fees (colegios profesionales)

**Facturas emitidas (sales invoices):**
- Client names and amounts (base imponible)
- Which VAT rate was charged, or whether the supply was exempt
- Whether a withholding was applied, and at which rate
- Turnover reconciliation against bank deposits
- Any EU clients (intracomunitarias, reverse charge, listing on Modelo 349)
- Any non-EU clients (exports of services)
- The IAE heading the invoices are issued under
- Whether all of them go to one single client

**Facturas recibidas (purchase invoices):**
- Expense category: running cost or capital item
- Deductible input VAT amounts
- Supplier tax number
- Anything that is not deductible: fines, client entertainment
- Anything that is a capital item and therefore depreciated rather than deducted at once

**Modelo 036:**
- The date of alta in the Censo de Empresarios, Profesionales y Retenedores
- The IAE heading or headings registered
- The income tax regime and the VAT regime elected
- Whether the client is registered as a withholder, and whether the address is declared as partly used for the activity

**Prior year Modelo 100:**
- Prior year IRPF liability
- Rendimiento neto de actividades económicas
- Filing status and the deductions claimed
- The autonomous community whose scale was applied
- The depreciation schedule already running

**Modelo 303 copies (quarterly VAT):**
- Quarterly base imponible and output VAT
- Deductible input VAT
- The result of each quarter, payable or to carry forward
- Any accumulated credit carried forward

**Modelo 130 copies (pagos fraccionados):**
- Cumulative net income declared each quarter
- The pago fraccionado computed
- Withholdings deducted
- The amount paid each quarter

**RETA recibos:**
- The monthly cuota paid, amount and month
- The contribution base
- Whether a reduced starting contribution (tarifa plana) was applied, and the resolution that granted it
- The total paid for the year

Do not state a monthly amount for the reduced starting contribution. Art. 38 ter Ley 20/2007 leaves the yearly amount to each year's Ley de Presupuestos Generales del Estado; Real Decreto-ley 13/2022 fixed it only for 2023 to 2025 and left 2026 onwards to that Budget Law. This skill found no 2026 amount on any page it may cite. Read the amount off the recibo and name the recibo as the source. The rules are in `es-social-contributions`.

**After parsing everything, build an internal inference object.** Do not show the raw inference. Turn it into the compact summary in Section 5.

## Section 5: the confirmation

After inference, present a single compact summary message. Use a structure that is fast to scan. Invite the user to correct anything wrong.

The legacy worked example that once stood here was removed: every amount in it was invented for illustration, and an invented amount in a library an assistant quotes is a figure somebody will repeat. Use the template below and fill it with the client's own numbers, read off their own documents.

**Summary template:**

> Here's what I pulled from your documents. Skim it and tell me what's wrong.
>
> **Identity**
> - Name, NIF
> - Residency and fiscal domicile, including the autonomous community
> - Autónomo, and which estimación directa method
> - Date of alta in the Censo (Modelo 036) and date of alta en RETA
> - IAE heading, and whether it is section one, two or three
> - VAT position: general, recargo de equivalencia, exempt or mixed
>
> **Ingresos** (from the bank statement and the facturas emitidas)
> - Ingresos brutos, base imponible, with the client breakdown
> - Output VAT charged, by rate
> - Withholdings suffered on professional invoices, at the rate the invoices show. Only a payer who is obliged to withhold applies one. A business abroad with no establishment in Spain is one only in the cases of art. 76.1.d of the Reglamento del IRPF (employment income it pays, and income that is a deductible expense of its own Spanish-taxed income), so an invoice to such a client normally carries none and does not belong in this line; if it does carry one, keep it and flag it.
> - Intra-Community supplies and exports, listed separately. Neither carries Spanish output VAT, so keep both out of the output VAT line above
>
> **Gastos** (from the bank statement and the facturas recibidas)
> - Each category with its total, and the invoice behind it
> - Deductible input VAT
> - Capital items, with the purchase date, for depreciation in `es-income-tax`
> - Anything with a private use element, marked as unresolved
>
> **RETA** (from the recibos)
> - Monthly cuota and contribution base, month by month
> - Months of alta in the year
> - Total paid, which is a deductible expense in the income tax return
>
> **Modelo 303** (from the filed returns)
> - Which quarters are filed and which are outstanding
> - Any credit carried forward
>
> **Modelo 130** (from the filed returns)
> - Which quarters are filed and which are outstanding
> - Cumulative payments made
>
> **Prior year** (from the last Modelo 100)
> - Prior year liability and rendimiento neto
> - Autonomous community
> - Depreciation schedule still running
>
> **Flags I already see:** list every unresolved item, one line each.
>
> **Is any of this wrong? Reply "looks good" or tell me what to fix.**

## Section 6: gap filling

After the user confirms the summary, or corrects it, ask about the things that cannot be inferred from documents. Use `ask_user_input_v0` where possible.

**Things that usually cannot be inferred:**

1. **Home office (despacho en casa).** Documents rarely show whether a dedicated workspace exists.
2. **Private use share** of phone, internet and vehicle.
3. **Capital items from earlier years** still being depreciated.
4. **Exempt activities**, where the invoices do not say so on their face.
5. **Personal deductions**: pension contributions, and the community deductions in `es-irpf-deductions`.
6. **Other income**: employment, rent, capital gains, savings income.

The tables in this section carry the figures that decide which of these questions has to be asked and what has to be collected. The computations sit in the skills named beside each table.

**Income tax regime, the simplified deduction, withholding on invoices and the quarterly payment (Reglamento del IRPF, RD 439/2007)**

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820 |
| Prior year net turnover of all the activities together above which estimación directa simplificada cannot be used (art. 28.1.b) | EUR 600,000 | "no supere los 600.000 euros anuales en el año inmediato anterior" |
| Hard-to-justify expenses and provisions in simplificada: percentage of net income before this item (art. 30, rule 2.ª) | 5% | "se cuantificará aplicando el porcentaje del 5 por ciento sobre el rendimiento neto" |
| Yearly cash cap on that deduction | EUR 2,000 | "sin que la cuantía resultante pueda superar 2.000 euros anuales" |
| Quarterly payment on account in direct estimation, on net income from 1 January to the end of the quarter (art. 110.1.a) | 20% | "el 20 por ciento del rendimiento neto correspondiente al período de tiempo transcurrido" |
| Share of the prior year's activity income that must have borne withholding for a professional to be released from filing the quarterly return (art. 109.2) | 70% | "al menos el 70 por ciento de los ingresos de la actividad fueron objeto de retención" |
| Ordinary withholding rate on a professional invoice paid by a payer obliged to withhold (art. 95.1) | 15% | "se aplicará el tipo de retención del 15 por ciento sobre los ingresos íntegros satisfechos" |
| Professional who starts an activity: the tax period of the start and the two following periods, only where no professional activity was carried on in the year before the start date, and only once the payer has been told in writing | 7% | "el tipo de retención será del 7 por ciento en el período impositivo de inicio de actividades" |
| Municipal collectors, insurance intermediaries who use external auxiliaries, and commercial delegates of the state lottery company, under letters a, b and c of art. 95.1. No income test applies to these three | 7% | "El tipo de retención será del 7 por ciento en el caso de rendimientos satisfechos a" |
| The activities in letter d of art. 95.1, named there by their business tax group numbers and by the performing arts cases, but only where the prior year gross income of those activities was below this amount | EUR 15,000 | "correspondiente al ejercicio inmediato anterior sea inferior a 15.000 euros" |
| And, for letter d only, where that income was more than this share of the person's total business and employment income in the same year. Both tests must be met | 75% | "represente más del 75 por ciento de la suma de los rendimientos íntegros de actividades económicas y del trabajo obtenidos por el contribuyente en dicho ejercicio" |
| The professional rates in art. 95.1 are cut by this share where the income qualifies for the Ceuta and Melilla credit in art. 68.4 of the Ley del IRPF, so an invoice from a Ceuta or Melilla professional shows a lower rate and is not evidence of anything else (art. 95.1, last paragraph) | 60% | "Estos porcentajes se reducirán en un 60 por ciento cuando los rendimientos tengan derecho a la deducción en la cuota prevista en el artículo 68.4 de la Ley del Impuesto" |
| No withholding on rent for urban premises where the rents paid by the tenant to the same landlord in the year are no more than this amount (art. 75.3.g.2.º) | EUR 900 | "Cuando las rentas satisfechas por el arrendatario a un mismo arrendador no superen los 900 euros anuales" |

The hard-to-justify deduction is a cap, not an allowance: it is the percentage of net income, up to the cash cap. For an activity carried on in Ceuta in 2026 the percentage is the one in the Ley del IRPF table below, not the one above; disposición adicional 64 names only the percentage and says nothing about the cash cap in the row above; whether that cap still applies to the raised percentage is for the accountant to settle. It cannot be taken by a taxpayer who opts for the reduction in art. 26.1 of the same Reglamento, which is the reduction for a single-client or economically dependent self-employed person in art. 32.2 of the Ley del IRPF (Q10 above). The computation is `es-income-tax`; the quarterly return is `es-estimated-tax`.

The reduced starting rate has to be notified to the payer in writing, and the payer keeps the signed notice. An invoice carrying a reduced rate from the table above is therefore not proof of a new autónomo: the payee may be one of the listed groups instead. Ask.

Art. 75.3.g lists two more cases with no rent withholding, which carry no figure: housing let by a company to its own employees, and a landlord whose activity is classified in group 861 of section one of the business tax tariffs, or in another heading allowing the letting or subletting of urban property, where applying the group 861 quota rules to the cadastral value of the let property would not have given a nil quota. That landlord has to prove it to the tenant.

**Withholding the client applies to rent, and expenses that need a client answer (Ley del IRPF, Ley 35/2006)**

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764 |
| Withholding on rent paid for urban property, declared on Modelo 115 (art. 101.8) | 19% | "subarrendamiento de bienes inmuebles urbanos, cualquiera que sea su calificación, será del 19 por ciento" |
| That rate is cut by this share where the let property is in Ceuta or Melilla, on the terms of art. 68.4 of the same Law (art. 101.8) | 60% | "Este porcentaje se reducirá en un 60 por ciento cuando el inmueble esté situado en Ceuta o Melilla" |
| Where the main home is partly used for the activity: the deductible share of water, gas, electricity, telephone and internet is this percentage applied to the proportion of square metres used, unless a higher or lower share is proved (art. 30.2.5.ª.b) | 30% | "en el porcentaje resultante de aplicar el 30 por ciento a la proporción existente entre los metros cuadrados" |
| Health insurance for the worker, the spouse and children under twenty-five living with them, per insured person per year (art. 30.2.5.ª.a) | EUR 500 | "El límite máximo de deducción será de 500 euros por cada una de las personas" |
| The same limit for each of those insured people who has a disability | EUR 1,500 | "o de 1.500 euros por cada una de ellas con discapacidad" |
| Ceuta only, tax year 2026: the hard-to-justify percentage in simplificada for activities carried on in Ceuta whose income qualifies for the art. 68.4 credit (disposición adicional 64, added by Real Decreto-ley 22/2026, convalidated 16 September 2026) | 10% | "será, durante el período impositivo 2026, del 10 por ciento" |

**Pension contributions, the reduction limit (Ley del IRPF, art. 52)**

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764 |
| The reduction is the lower of this share of the net employment and business income earned individually in the year, and the cash limit below | 30% | "El 30 por 100 de la suma de los rendimientos netos del trabajo y de actividades económicas" |
| Cash limit | EUR 1,500 | "b) 1.500 euros anuales" |
| Increase where it comes from employer contributions, or from the worker's own contributions to the same instrument within the amounts the article sets against the employer contribution | EUR 8,500 | "En 8.500 euros anuales, siempre que tal incremento provenga de contribuciones empresariales" |
| Increase where it comes from a self-employed person's contributions to a sectoral plan, to a simplified employment plan for the self-employed, or from the individual entrepreneur's or professional's own contributions to an employment plan they promote and belong to, or to a provident society of which they are a member | EUR 4,250 | "En 4.250 euros anuales, siempre que tal incremento provenga de aportaciones a los planes de pensiones sectoriales" |
| The two increases taken together cannot exceed this amount | EUR 8,500 | "la cuantía máxima de reducción por aplicación de los incrementos previstos en los números 1.º y 2.º anteriores será de 8.500 euros" |

For an autónomo the relevant increase is usually the sectoral or self-employed plan one, not the employer one. Ask which plan the contributions went to, not just the amount.

**Value added tax: the rates, the retailer test and the vehicle presumption (Ley del IVA, Ley 37/1992)**

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740 |
| General rate (art. 90.Uno) | 21% | "El Impuesto se exigirá al tipo del 21 por ciento" |
| Reduced rate (art. 91.Uno) | 10% | "Se aplicará el tipo del 10 por ciento a las operaciones siguientes" |
| Super-reduced rate (art. 91.Dos) | 4% | "Se aplicará el tipo del 4 por ciento a las operaciones siguientes" |
| Recargo de equivalencia on goods at the general rate (art. 161) | 5.2% | "Con carácter general, el 5,2 por ciento" |
| Recargo de equivalencia on goods at the reduced rate | 1.4% | "el 1,4 por ciento" |
| Recargo de equivalencia on goods at the super-reduced rate | 0.5% | "el 0,50 por ciento" |
| Recargo de equivalencia on manufactured tobacco | 1.75% | "Para las entregas de bienes objeto del Impuesto Especial sobre las Labores del Tabaco, el 1,75 por ciento" |
| Retailer test: a trader is a retailer only if, among the other conditions of art. 149.Uno, the prior year's supplies of those goods to non-business customers and to the Social Security system were more than this share of all supplies of them. The same article lifts this test for some traders classed as retailers under the business tax rules | 80% | "hubiese excedido del 80 por 100 del total de las entregas realizadas" |
| Share of a car, its trailer, a moped or a motorcycle presumed used in the business, for deducting input VAT (art. 95.Tres.2.ª) | 50% | "se presumirán afectados al desarrollo de la actividad empresarial o profesional en la proporción del 50 por 100" |
| Share presumed for the vehicles the same rule lists: mixed vehicles carrying goods, passenger transport for consideration, driver and pilot instruction for consideration, manufacturers' testing and sales promotion, the professional travel of commercial representatives and agents, and security services | 100% | "los vehículos que se relacionan a continuación se presumirán afectados al desarrollo de la actividad empresarial o profesional en la proporción del 100 por 100" |

Both shares are presumptions, and rule 3 of the same article requires the deduction to be adjusted, either way, once the real degree of business use is proved. The presumption is a VAT rule only. For income tax a car counts as used in the activity only if it is used exclusively for it, with the narrow list of exceptions in art. 22.4 of the Reglamento del IRPF, which names much the same kinds of vehicle. Never carry one answer across to the other tax. The VAT work is `es-vat-return`.

**Module method limits, the statute (art. 31.1.3.ª Ley 35/2006)**

| Limit | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764 |
| Prior year income from all activities except farming, livestock and forestry, above which the module method cannot be used | EUR 150,000 | "excepto las agrícolas, ganaderas y forestales, 150.000 euros anuales" |
| Of that, income from operations invoiced to businesses and professionals, above which the module method cannot be used | EUR 75,000 | "supere 75.000 euros" |
| Prior year purchases of goods and services, capital assets excluded, above which the module method cannot be used | EUR 150,000 | "excluidas las adquisiciones de inmovilizado, en el ejercicio anterior supere la cantidad de 150.000 euros" |

**Module method limits, the Agencia Tributaria page (page dated 13 October 2026)**

| Limit | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://sede.agenciatributaria.gob.es/Sede/empresarios-individuales-profesionales/contribuyentes-modulos/quien-se-aplica/irpf.html |
| Prior year income from all activities except farming, on that page | EUR 250,000 | "Desde 2016 hasta 2026 inclusive los límites de 150.000 € y 75.000 € pasan a ser 250.000 € y 125.000 € respectivamente" |
| Of that, invoiced to businesses and professionals, on that page | EUR 125,000 | "pasan a ser 250.000 € y 125.000 € respectivamente" |
| Prior year purchases, capital assets excluded, on that page | EUR 250,000 | "Desde 2016 hasta 2026 inclusive el volumen de compras en bienes y servicios en el año inmediato anterior no puede superar los 250.000 €" |

The two official sources disagree. The higher limits sit in disposición transitoria 32 of Ley 35/2006, whose heading still reads "en los ejercicios 2016 a 2024"; three Real Decreto-ley tried to extend them and each was left without effect. The Agencia Tributaria page still states the higher limits for 2016 to 2026 inclusive. **Never place a client inside or outside the module method on one of these sources alone.** If the client's prior year income or purchases fall between the two, stop the intake and say so. Tell the client in plain words that two official sources set different limits for this year, that which one governs decides whether they are taxed under the module method or under direct estimation, and that a gestor or asesor fiscal has to settle it with the Agencia Tributaria before any return is prepared. Name the two limits the client sits between. Do not pick a side and do not carry on under either method.

**Reporting thresholds the intake has to test (RD 1065/2007)**

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2007-15984 |
| Operations with one other person or entity in the calendar year: there is no Modelo 347 duty for a taxpayer whose operations with each of them, taken together, were no more than this amount (art. 32.c) | EUR 3,005.06 | "3.005,06 euros durante el año natural correspondiente" |
| Accounts held abroad (Modelo 720): no duty to report any account where both the 31 December balances and the average balances, taken together, are no more than this figure; passing either means reporting every account (art. 42 bis.4.e) | EUR 50,000 | "no superen, conjuntamente, los 50.000 euros, y la misma circunstancia concurra en relación con los saldos medios" |

**Territory: the Canary Islands indirect tax (art. 51 Ley 4/2012, wording in force since 1 January 2024)**

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2012-9282 |
| Canary Islands general IGIC rate, charged instead of VAT on supplies not covered by any other IGIC rate | 7% | "El tipo general del 7 por ciento, aplicable a las entregas de bienes y prestaciones de servicios" |

**Territory: the Ceuta and Melilla income tax credit (art. 68.4 Ley 35/2006)**

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764 |
| Credit against the tax on income earned in Ceuta or Melilla by someone habitually and effectively resident there | 60% | "se deducirán el 60 por ciento de la parte de la suma de las cuotas íntegras" |

**Territory: the Ceuta and Melilla contribution bonification before 1 October 2026 (art. 36 Ley 20/2007 as worded by Real Decreto-ley 1/2023)**

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2023-625 |
| Bonification of the common contingencies contribution, listed sectors, for self-employed workers who live and work in Ceuta or Melilla | 50% | "tendrán derecho a una bonificación del 50 por ciento de la cuota por contingencias comunes" |

**Territory: the Ceuta and Melilla contribution bonification from 1 October 2026 (art. 36 Ley 20/2007 as worded by Real Decreto-ley 22/2026)**

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.boe.es/buscar/act.php?id=BOE-A-2007-13409 |
| Bonification of the common contingencies contribution, listed sectors, for cuotas accrued from 1 October 2026 | 75% | "tendrán derecho a una bonificación del 75 por ciento de la cuota por contingencias comunes" |

A Ceuta or Melilla intake in this tax year therefore spans two contribution periods and two wordings of the sector list. The earlier wording, in the services item, reads "excepto el transporte aéreo de ala fija, construcción de edificios"; the later wording ends that item at "excepto el transporte aéreo de ala fija". Whether building construction is in or out of the earlier bonification is not settled by the text alone, so flag it for the reviewer for any client in that sector. Collect the RETA recibos for the whole year and let `es-social-contributions` split them. No IPSI rate is stated anywhere in this skill: those rates are set by each city and are on no site this skill may cite.

**The questions to ask, in `ask_user_input_v0` form:**

~~~
Q: "Home office (despacho en casa)?"
   Options: [
     "Dedicated room, used ONLY for work, declared on Modelo 036",
     "Dedicated corner or desk, used ONLY for work",
     "Shared space (kitchen table, living room)",
     "Separate business premises, not at home",
     "No fixed workspace"
   ]
~~~

- **Option 1.** Ask for the proportion of the home used, as square metres of the workspace over total square metres. Collect the rent or mortgage interest, IBI, community fees and utility bills. The deductible share of the utilities is the percentage in the Ley del IRPF table above, applied to that proportion.
- **Option 2.** Flag for the reviewer: a part of the home used for work without the address being declared on Modelo 036 is weak.
- **Option 3.** "A shared space is very hard to defend with the Agencia Tributaria. I'll skip this deduction."
- **Option 4.** The rent is already captured as an expense. No home office computation is needed, but check whether the client should be withholding on that rent.
- **Option 5.** Skip the home office entirely.

~~~
Q: "Phone and internet: business use?"
   Options: [
     "Exclusive business line, separate from personal",
     "Mostly business",
     "About half and half",
     "Mostly personal"
   ]
~~~

An exclusive business line is deductible in full. Otherwise only the business share is deductible, and only if it can be shown. The official pages set no default split for a mixed use item other than the home utilities rule above, so nothing is deducted without evidence. Never invent a percentage.

~~~
Q: "Aportaciones a planes de pensiones this year?"
   Options: [
     "Yes, to a sectoral or self-employed plan",
     "Yes, to an employer plan",
     "Yes, to an individual plan only",
     "No contributions",
     "Not sure"
   ]
~~~

If yes, ask for the amount and which plan received it. The limit and the two increases are in the pension table above.

## Section 7: the final handoff

Once gap filling is done, produce a final handoff message and hand off to `es-return-assembly`.

**Example handoff message:**

> Intake complete. Here's what's going to the return assembly: your residence and community, your census and RETA position, your activity and IAE heading, your income tax regime, your VAT position, the income and expenses I read off your documents, the withholdings suffered, and the flags still open.
>
> I'm now going to run the full Spain return preparation. That covers:
> 1. Modelo 303, the quarterly VAT return
> 2. Modelo 100, the annual income tax return
> 3. RETA reconciliation
> 4. Modelo 130, the quarterly payment on account
>
> You'll get back:
> 1. A working paper with all computations and live formulas
> 2. A reviewer brief with positions, citations, and flags for your asesor fiscal
> 3. A filing calendar with the upcoming deadlines
>
> Reminder: all of it has to be reviewed by your asesor fiscal or gestor before anything is filed. Starting now.

Then invoke `es-return-assembly` with the structured intake package. For a client in Canarias, Ceuta or Melilla, or a client who makes only exempt supplies, leave Modelo 303 out of the list.

## Section 8: structured intake package (internal format)

The downstream skill `es-return-assembly` consumes a JSON structure. It is internal and not shown to the user unless they ask. Key fields:

~~~json
{
  "jurisdiction": "ES",
  "tax_year": 2026,
  "taxpayer": {
    "name": "",
    "nif": "",
    "residency": "resident",
    "comunidad_autonoma": "",
    "territory": "comun | canarias | ceuta | melilla",
    "censo_alta_date": "",
    "censo_form": "036",
    "alta_reta_date": "",
    "baja_reta_date": "",
    "first_year_of_activity": 0,
    "estimacion": "directa_simplificada | directa_normal",
    "entity_type": "autonomo",
    "iae_epigrafe": "",
    "iae_seccion": "one | two | three",
    "cnae": "",
    "single_client_or_trade": false,
    "retencion_rate_on_invoices": "read off the invoices"
  },
  "income": {
    "ingresos_brutos": 0,
    "iva_repercutido": 0,
    "retenciones_soportadas": 0,
    "intracomunitarias": 0,
    "exportaciones": 0,
    "exempt_supplies": 0,
    "other_income": 0,
    "client_breakdown": []
  },
  "expenses": {
    "gastos_deducibles": [],
    "gastos_mixed_use": [],
    "gastos_no_deducibles": [],
    "inmovilizado": [],
    "hard_to_justify_applies": false,
    "total_gastos": 0
  },
  "iva": {
    "regimen": "general | recargo_equivalencia | exento | mixto",
    "modelo_303_filed": [],
    "iva_devengado_total": 0,
    "iva_soportado_deducible_total": 0,
    "saldo_compensar": 0,
    "exempt_activities": false,
    "prorrata": false,
    "modelo_349_required": false,
    "modelo_347_required": false
  },
  "reta": {
    "monthly_cuota": [],
    "base_cotizacion": [],
    "months_alta": 0,
    "reduced_starting_contribution": false,
    "reduced_contribution_resolution": "",
    "total_reta_paid": 0
  },
  "withholder": {
    "employees": false,
    "modelo_111_filed": [],
    "modelo_115_filed": [],
    "modelo_190_filed": false
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
    "share_of_square_metres": 0,
    "declared_on_036": false,
    "rent_or_mortgage": 0,
    "ibi": 0,
    "comunidad": 0,
    "suministros_total": 0
  },
  "private_use": {
    "phone_business_share": 0,
    "internet_business_share": 0,
    "vehicle_business_share": 0
  },
  "personal_deductions": {
    "planes_pensiones": 0,
    "plan_type": "",
    "other": []
  },
  "open_flags": [],
  "refusals_triggered": [],
  "documents_received": []
}
~~~

No rate or threshold goes into this package. The downstream skill reads those from its own tables; intake passes facts, dates and amounts read off documents.

The `territory` value in this package, `ceuta` or `melilla`, is what `es-income-tax` reads to tell the two apart, because in 2026 they get different answers for the hard-to-justify percentage.

## Section 9: refusal handling

Refusals fire either from the refusal sweep in Section 2 or during inference, for example when a company structure turns up in the documents.

When a refusal fires:
1. Stop the workflow.
2. State the specific reason in one sentence.
3. Recommend the path forward, naming the kind of practitioner.
4. Offer to continue with partial help ONLY if the out-of-scope item is cleanly separable, which is rare.

**Do not:**
- Apologise at length
- Try to work around the refusal
- Suggest the user "might be able to" fit into scope if they answer differently
- Continue silently

**Sample refusal:**

> Stop. You operate through a Sociedad Limitada, and I'm set up for autónomos (personas físicas) only. An SL files Impuesto sobre Sociedades (Modelo 200), with separate rules for administrator remuneration, dividends and corporate tax. You need an asesor fiscal familiar with corporate returns.
>
> I can't help with this one.

## Section 10: self-checks

**Check IN1.** No one-question-at-a-time prose in the refusal sweep. If the intake asked "Question 1 of 10" or walked through questions as separate messages, the check fails.

**Check IN2.** The refusal sweep used `ask_user_input_v0`. The first substantive interaction used the interactive tool, not prose questions.

**Check IN3.** Upload-first flow honoured. After the refusal sweep, the intake asked for a document dump before asking any content questions.

**Check IN4.** Documents were parsed and inferred before questions were asked. The inference summary in Section 5 was shown before the gap-filling questions in Section 6.

**Check IN5.** Gap filling asked only about things not visible in the documents. If the intake asked "did you pay RETA" after the bank statements showed Seguridad Social debits, the check fails.

**Check IN6.** Open flags captured. Anything ambiguous, risky or attention worthy during inference is in the `open_flags` list in the handoff package.

**Check IN7.** The handoff to `es-return-assembly` is explicit. The user was told the return preparation is starting, and the orchestrator was invoked with the intake package.

**Check IN8.** The reviewer step was stated at the start and repeated before the handoff.

**Check IN9.** Refusals were clean. No hedging. Stop means stop.

**Check IN10.** No meta-commentary about workflow phases.

**Check IN11.** The user-facing turn count is low. Target: eight turns or fewer from start to handoff for a prepared user. More than twelve turns for a normal intake is a failure.

**Check IN12.** The estimación directa method is established, the IAE section is established, and the withholding rate on the client's invoices was read off the invoices rather than inferred, before the handoff.

**Check IN13.** The territory is established, and if it is Canarias, Ceuta or Melilla the intake did not ask for a Modelo 303.

**Check IN14.** No monthly amount was stated for the reduced starting contribution.

**Check IN15.** If the client's prior year income or purchases fall between the statutory module limit and the higher one the Agencia Tributaria publishes, the intake stopped rather than deciding.

**Check IN16.** Residence was settled for the whole calendar year. No client was treated as a part-year resident, and a client who moved in or out during the year was referred.

## Section 11: performance targets

For a prepared user, with documents in a folder ready to upload:
- **Refusal sweep:** forty-five seconds, one to three interactive turns
- **Document upload:** two minutes, one upload turn
- **Inference and confirmation:** one minute of processing, one turn for the user to confirm
- **Gap filling:** two minutes, two to three interactive turns
- **Handoff:** immediate
- **Total:** about six minutes

For an unprepared user who has to fetch documents:
- Refusal sweep: the same
- Document discovery: ten to twenty minutes offline
- The rest: the same
- **Total:** fifteen to twenty-five minutes

## Section 12: cross-skill references

**Inputs:** user-provided documents and answers.

**Outputs:** a structured intake package consumed by `es-return-assembly`.

**Downstream skills, reached through `es-return-assembly`:**

| Skill | What it does |
| --- | --- |
| `es-vat-return` | Modelo 303, the quarterly VAT return |
| `es-income-tax` | Modelo 100, the annual income tax return |
| `es-social-contributions` | RETA contributions, the bands and the regularisation |
| `es-estimated-tax` | Modelo 130, the quarterly payment on account |
| `es-return-assembly` | Assembles the working paper and the reviewer brief |

**Skills to route to when the intake finds something outside this workflow:**

| Finding | Skill |
| --- | --- |
| The client wants the whole self-employed picture rather than a return | `es-autonomous-worker` |
| The client was not resident in Spain for the year | `es-non-resident-income-tax-irnr-and` |
| The client has employees | `spain-payroll`, and `es-modelo-111` for the withholding return |
| The client operates through a company | `es-corporate-tax` |
| Rental income alongside the activity | `es-rental-income` |
| Autonomous community deductions | `es-irpf-deductions` |

The VAT return is `es-vat-return` and nothing else: never route VAT work to any other slug.

### Change log

- **v0.1 (April 2026):** initial draft. Upload first, infer, then confirm.
- **v0.2 (September 2026):** refreshed against the official pages. Tax year moved to 2026. Modelo 037 removed: it was suppressed with effect from 3 February 2025 and only Modelo 036 exists. A retired VAT routing target replaced by `es-vat-return`. The monthly amount for the reduced starting contribution removed, because no allowed official page states one for this year. The invented worked example replaced by a template. Questions added for the IAE heading, the VAT position including recargo de equivalencia and exempt activities, employees and withholding obligations, and the territory.
- **v0.3 (October 2026):** the residence question rewritten to the two tests in art. 9.1 Ley 35/2006 (more than 183 days, or the centre of economic interests); the part-year resident route removed, because the tax period is the calendar year. Section three of the IAE tariffs added as professional income for withholding. The art. 26.1 reduction correctly identified as the single-client or dependent self-employed reduction, with a new question for it. The Ceuta and Melilla withholding cut limited to the rules that grant it. The exempt-only filing rule tied to art. 71 of the Reglamento del IVA. Contribution bonification rows dated to the two 2026 periods. Non-resident routing added.

## End of the intake skill

## The method, step by step

1. Run the refusal sweep in Section 2 before anything else, and stop where it says stop. Residence for the whole calendar year (art. 9 Ley 35/2006), structure and alta en RETA decide whether this workflow applies at all: https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764 A non-resident is taxed under the non-resident income tax and a company files Modelo 200; neither is this workflow.
2. Establish the census position from the client's Modelo 036: the date of alta in the Censo de Empresarios, Profesionales y Retenedores, the IAE heading, the income tax regime and the VAT regime. The census obligations are in RD 1065/2007: https://www.boe.es/buscar/act.php?id=BOE-A-2007-15984 The form is Modelo 036 only; Modelo 037 was suppressed by Orden HAC/1526/2024, in force from 3 February 2025: https://www.boe.es/buscar/doc.php?id=BOE-A-2025-410
3. Establish the RETA position from the recibos: the months of alta, the base and the cuota each month, and whether a reduced starting contribution was granted. Do not state an amount for that contribution. The rules are in art. 38 ter Ley 20/2007: https://www.boe.es/buscar/act.php?id=BOE-A-2007-13409
4. Take the document dump in Section 3, then run the inference pass in Section 4 before asking a single content question.
5. Fix the income tax regime against art. 28 and art. 30 of the Reglamento del IRPF and the turnover limit in the Section 6 table: https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820 If the client says módulos, stop and read the module warning in the same section. Record whether the client has one single client or is a TRADE, for art. 32.2 Ley 35/2006.
6. Fix the VAT position: general, recargo de equivalencia under arts. 148 to 163, exempt under art. 20.Uno, or mixed. Ley 37/1992: https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740 In Canarias, Ceuta and Melilla, which art. 3 of the same Law leaves outside the VAT territory, there is no Modelo 303 for the activity carried on there.
7. Fix the withholding position both ways: what the client's own invoices carry under art. 95 of the Reglamento del IRPF, read off the invoices, and what the client must withhold from staff, from rent or from other professionals: https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820
8. Confirm the whole picture with the user using the Section 5 template, then fill the gaps in Section 6 that the documents cannot answer.
9. Hand the package in Section 8 to `es-return-assembly`, with every unresolved item in `open_flags`. An unresolved item passed on as resolved is the one failure this skill can cause on its own.

## Worked checks

These checks confirm a routing answer. They are not a computation of the client's tax.

### Release from Modelo 130

A professional had EUR 100,000 of activity income last year, of which EUR 72,000 bore withholding. 72% is at least 70%, so art. 109.2 of the Reglamento del IRPF releases them from the quarterly payment for those activities.

```oa-check
name: Spain 2026 intake professional release from Modelo 130
inputs:
  activity_income: 100000
  income_with_withholding: 72000
  test_percent: 70
steps:
  share_percent: income_with_withholding / activity_income * 100
  headroom: share_percent - test_percent
expected:
  share_percent: 72
  headroom: 2
```

### Reading a professional invoice

An established professional invoices EUR 1,000 plus 21% VAT to a business payer who must withhold 15% (art. 95.1). The invoice shows 210 VAT, 150 withholding and 1,060 to collect. A qualifying new professional at 7% withholds 70 and collects 1,140.

```oa-check
name: Spain 2026 intake invoice withholding read
inputs:
  base: 1000
  vat_rate: 0.21
  standard_rate: 0.15
  starting_rate: 0.07
steps:
  vat: base * vat_rate
  collect_standard: base + vat - base * standard_rate
  collect_starting: base + vat - base * starting_rate
expected:
  vat: 210
  collect_standard: 1060
  collect_starting: 1140
```

## Ask the client first

- Were you resident in Spain for the whole of 2026 on the art. 9 tests, and did you move in or out during the year? A move year is referred, because Spain has no part-year resident.
- Where is your fiscal domicile: territorio común, Canarias, Ceuta, Melilla, or a foral territory? It decides the indirect tax, the credit and half the income tax scale.
- Which IAE heading are you registered under, and is it section one, two or three? Sections two and three are professional income and are withheld on by a payer obliged to withhold.
- In which tax period did the activity start, and had you carried on any professional activity in the year before that? Together they decide whether the reduced withholding rate applies.
- What is your VAT position: general, recargo de equivalencia, exempt, or a mix? A retailer in recargo de equivalencia files no Modelo 303 for those sales and deducts no input VAT on them.
- Do you have employees, pay rent for business premises, or pay other professionals? Each makes you a withholder with returns of your own.

## When to refuse or refer

- Anyone who is not a Spanish tax resident for the year, anyone who moved to or from Spain during the year, and anyone who is not an autónomo.
- Any client whose fiscal domicile is in the Basque Country or Navarra. Their income tax is foral law.
- Any client in estimación objetiva (módulos), and any client whose prior year income or purchases fall between the statutory module limit and the higher one the Agencia Tributaria publishes. Refer both to a gestor or asesor fiscal who works with the module method, and tell the second which two limits they sit between.
- Any autonomous community deduction or the community half of the scale. No national page carries them: `es-irpf-deductions`.
- Any IPSI rate or return for Ceuta or Melilla, and any IGIC return for the Canary Islands.
- A Ceuta or Melilla client in building construction, for the contribution bonification before 1 October 2026: the wording does not settle it.
- Any monthly amount for the reduced starting contribution in this tax year, until a Budget Law sets one.
- A prorrata or a separate sector of activity for a mixed exempt and taxable business. That is `es-vat-return` work and needs a reviewer.
- Anything with a foreign element: a client abroad, work abroad, a treaty, or a move in or out of Spain.
- A licence, a permit or a local business tax. Those are municipal law.

## Sources

| Official source | Scope read | Read on |
|---|---|---|
| [Ley 35/2006, Ley del IRPF](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764) | Arts. 30, 68.4, 101.8 | 2026-10-31 |
| [RD 439/2007, Reglamento del IRPF](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820) | Arts. 30, 95, 109, 110 | 2026-10-31 |
| [Ley 37/1992, Ley del IVA](https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740) | Art. 107 only | 2026-10-31 |
| [RD 1624/1992, Reglamento del IVA](https://www.boe.es/buscar/act.php?id=BOE-A-1992-28925) | Art. 81 | 2026-10-31 |
| [RD 1065/2007, gestión e inspección](https://www.boe.es/buscar/act.php?id=BOE-A-2007-15984) | EUR 3,005.06 | 2026-10-31 |
| [Orden HAC/1526/2024, suppressing Modelo 037](https://www.boe.es/buscar/doc.php?id=BOE-A-2025-410) | Page opened only | 2026-10-31 |
| [Ley 20/2007, Estatuto del trabajo autónomo](https://www.boe.es/buscar/act.php?id=BOE-A-2007-13409) | Page opened only | 2026-10-31 |
| [Real Decreto-ley 1/2023](https://www.boe.es/buscar/act.php?id=BOE-A-2023-625) | Page opened only | 2026-10-31 |
| [Ley 4/2012 de Canarias, IGIC rates](https://www.boe.es/buscar/act.php?id=BOE-A-2012-9282) | Page opened only | 2026-10-31 |
| [Agencia Tributaria, who the module method applies to](https://sede.agenciatributaria.gob.es/Sede/empresarios-individuales-profesionales/contribuyentes-modulos/quien-se-aplica/irpf.html) | Module limits 150,000, 75,000, 250,000, 125,000 | 2026-10-31 |

Not yet confirmed: figures from sources marked "Page opened only" and table rows not named in the scope column were not re-read on 2026-10-31; they carry the skill's October 2026 refresh, whose exact read date is not recorded.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as an asesor fiscal, gestor administrativo, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

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
