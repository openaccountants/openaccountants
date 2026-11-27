---
name: es-freelance-intake
description: ALWAYS USE THIS SKILL when a user asks for help preparing their Spain tax returns AND mentions freelancing, self-employment, autónomo, working por cuenta propia, or independent professional activity. Trigger on phrases like "help me do my taxes", "prepare my Modelo 100", "I'm autónomo in Spain", "I'm a freelancer in Spain", "do my taxes as an autónomo", "prepare my IRPF return", or any similar phrasing where the user is a Spain-resident self-employed individual needing tax return preparation. This is the REQUIRED entry point for the Spain self-employed tax workflow -- every other skill in the stack (es-vat-return, es-income-tax, es-social-contributions, es-estimated-tax, es-return-assembly) depends on this skill running first to produce a structured intake package. Uses upload-first workflow -- the user dumps all their documents and the skill infers as much as possible before asking questions. Uses ask_user_input_v0 for structured questions instead of one-at-a-time prose. Built for speed. Spain full-year residents only; autónomos (self-employed individuals) only.
version: 0.6
jurisdiction: ES
tax_year: 2026
last_updated: 2026-11-27
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: router
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
- **Q2 = Comunidad de bienes.** Stop. "This workflow covers individuals only. The entity and its members need their own classification review. Check this point with one of our partner accountants."
- **Q2 = Not sure.** Ask one follow-up: "Do you invoice clients in your own name using your NIF? Or do you have a registered company with its own tax number? Provide the census declaration and any entity documents; invoicing in your own name alone does not establish legal status."
- **Q3 = Yes, full year RETA.** Continue.
- **Q3 = Part year RETA.** Continue with a flag: record the dates of alta and baja, and pass them to `es-social-contributions` and `es-income-tax`. Collect every receipt, adjustment and refund, including payments outside the registration months; do not prorate or decide deductibility in intake.
- **Q3 = Not registered.** Stop. "Your Social Security position needs review before this RETA workflow can continue. An alternative regime or professional mutuality may need separate handling. Check this point with one of our partner accountants."
- **Q3 = Not sure.** Ask one follow-up: "Provide your Import@ss registration history or alta/baja resolutions." A bank debit is evidence of a payment, not proof of the registration period. Missing registration, an alternative professional mutual fund or another Social Security regime is a hold: "Check this point with one of our partner accountants."

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
- **Q4 = Normal.** Continue. Record the normal method; the simplified hard-to-justify deduction does not apply. Let the downstream Guide determine the bookkeeping obligations for the activity.
- **Q4 = Objetiva (módulos).** Stop. "I'm set up for estimación directa only. Módulos computes the result from physical parameters, not from your books. You need a gestor familiar with estimación objetiva." Use the current statutory limits in Section 6; being below a limit alone does not establish eligibility.
- **Q4 = Not sure.** Under art. 28.1 of the Reglamento del IRPF, estimación directa simplificada applies where all three conditions are met: the activity is not in estimación objetiva, the prior year's net turnover for all those activities together does not exceed the limit in the Section 6 table, and the taxpayer has not renounced the simplified method. Ask for the last filed Modelo 100 or the Modelo 036 and read it off the return rather than guessing. Annualise prior-year turnover where the activity started during that year; with no activity in the prior year the simplified method applies unless renounced. Normal-method activity generally brings all activities into normal, subject to the in-year new-activity exception in art. 28.3.
- **Q5 = Territorio común.** Continue. VAT applies, and the autonomous community half of the income tax scale is that community's own.
- **Q5 = Canarias.** Continue with a flag. Art. 3 Ley 37/1992 excludes the Canary Islands from the territory where Spanish VAT applies, so fiscal domicile alone cannot decide which tax a transaction bears. Record establishments, customers and place of supply; do not prepare Modelo 303 for operations outside Spanish VAT, but do not suppress an actual Spanish VAT obligation. The IGIC general rate is in the Ley 4/2012 table in Section 6; the Canary returns themselves are outside this workflow.
- **Q5 = Ceuta or Melilla.** Continue with a flag. Art. 3 Ley 37/1992 also excludes Ceuta and Melilla from the VAT territory, and IGIC does not apply there either: collect any IPSI records and refer the local indirect-tax treatment: "Check this point with one of our partner accountants." There is also an income tax credit, a contribution bonification, and a cut to SOME withholding rates. The 2026 hard-to-justify deduction has a Ceuta-specific uplift and a later national uplift, with different payment-on-account timing (disposiciones adicionales 64 and 67 Ley 35/2006, Section 6): flag both for `es-income-tax` and `es-estimated-tax`. The cut is granted rule by rule, not across the board: this skill shows it only where the article that grants it is quoted, which is the professional invoice rates and the rent rate in the Section 6 tables.
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
- **Q8 = Régimen general.** Continue. Establish the actual filing period from the census and filed returns: quarterly is the general rule, with monthly cases under art. 71.3 Reglamento del IVA. Do not apply the new annual small-business regime, which starts in 2027: https://www.boe.es/buscar/doc.php?id=BOE-A-2026-24701
- **Q8 = Recargo de equivalencia.** Continue with a flag, and do not prepare a Modelo 303 for those sales. Under art. 148.Uno Ley 37/1992 the regime applies to retail traders who are individuals, or entities under the income attribution regime, in the sectors and on the conditions set by regulation. Under art. 154 the supplier charges the surcharge on the invoice; the retailer charges the customer VAT but does not normally settle it with the Treasury, and deducts no input VAT on goods and services used in that activity. Intra-Community acquisitions, reverse-charge purchases and taxable non-exempt immovable-property disposals still require their own settlement (art. 154 and art. 71.8 Reglamento del IVA). The rates and the retailer test are in the Ley del IVA table in Section 6.
- **Q8 = Exempt activity.** Continue with a flag. Medical and health care, teaching, insurance and financial services require testing against the specific exemption conditions in art. 20.Uno Ley 37/1992; the activity label alone is insufficient: https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740 Input VAT on costs used for exempt supplies is generally not deductible; art. 94.Uno lists the exceptions, among them insurance and financial services that would be exempt if made in Spain, where the customer is established outside the European Union or the service is directly linked to an export out of it. A client who makes ONLY supplies exempt under art. 20 or art. 26 normally files neither the periodic VAT return nor the annual summary for those exempt operations (art. 71.1 and 71.7 of the Reglamento del IVA). Check acquisitions and reverse-charge transactions separately under art. 71.8; exemption is not a blanket release from all VAT declarations: https://www.boe.es/buscar/act.php?id=BOE-A-1992-28925
- **Q8 = Mixed.** Flag for the reviewer: a prorrata or a separate sector of activity may apply. That is `es-vat-return` work, not intake work.
- **Q8 = Not sure.** Read it off the last Modelo 303 or off the Modelo 036. Do not assume the general regime for a shop.
- **Q9 = Employees.** Flag: the client is a withholder and files Modelo 111, which art. 108.1 of the Reglamento del IRPF generally sets as quarterly in the first twenty calendar days of April, July, October and January (monthly cases follow art. 71.3.1.º and 2.º Reglamento del IVA); the downstream Guide must apply the actual filing calendar, and Modelo 190 annually, and is an employer with the Seguridad Social. Payroll is `spain-payroll`; the withholding return itself is `es-modelo-111`.
- **Q9 = Rent for business premises.** Flag: withholding on the rent, declared on Modelo 115, unless one of the exceptions applies. Ask for the rent paid to each landlord separately over the year, because the amount exception is tested landlord by landlord. The rate and the exceptions are in the two rent tables in Section 6.
- **Q9 = Pays other professionals.** Flag: payments subject to professional withholding under arts. 75, 76 and 95 go to Modelo 111; check the payer, payee and payment rather than treating every supplier invoice alike.
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
- Fines, gifts and client entertainment: identify separately and leave tax deductibility to `es-income-tax` and `es-vat-return`
- Potential capital items: collect cost, purchase and in-service dates, private use and prior schedules; do not invent a capitalisation threshold or depreciation rate

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

Do not state a monthly amount for the reduced starting contribution. Art. 38 ter Ley 20/2007 leaves the yearly amount to each year's Ley de Presupuestos Generales del Estado; Real Decreto-ley 13/2022 fixed it only for 2023 to 2025 and left 2026 onwards to that Budget Law. The statutory delegation alone does not prove the 2026 amount; intake leaves any entitlement or assumed monthly charge on hold. "Check this point with one of our partner accountants." Read the amount off the recibo and name the recibo as the source. The rules are in `es-social-contributions`.

**After parsing everything, build an internal inference object.** Do not show the raw inference. Turn it into the compact summary in Section 5.

## Section 5: the confirmation

After inference, present a single compact summary message. Use a structure that is fast to scan. Invite the user to correct anything wrong.

Use this template with the client's own numbers and a document reference beside each one. The original 2025 illustration is retained under Worked checks as a non-usable historical fixture; its year and inputs must never be silently carried into a 2026 return.

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
> - Withholdings suffered on professional invoices, at the rate the invoices show. Only a payer who is obliged to withhold applies one. A business abroad with no establishment in Spain is one only in the cases of art. 76.1.d of the Reglamento del IRPF (employment income it pays, and income that is a deductible expense of its own Spanish-taxed income), so establish those facts before deciding whether withholding was required. Record any actual withholding even if disputed, and flag it for the reviewer.
> - Transactions with EU and non-EU customers, listed separately. Do not infer zero Spanish output VAT from the customer's country: customer status, the receiving establishment and the service determine the place of supply, including the special rules (arts. 69, 70 and 72 Ley del IVA). Hold cross-border treatment for review in `es-vat-return`
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
> - Total paid, separately reconciled to receipts, adjustments and refunds; `es-income-tax` determines the deductible amount
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

| Item | Value | Note | Source |
| --- | --- | --- |---|
| Prior year net turnover of all the activities together above which estimación directa simplificada cannot be used (art. 28.1.b) | EUR 600,000 | "no supere los 600.000 euros anuales en el año inmediato anterior" | https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820 |
| 2026 hard-to-justify expenses and provisions in simplificada: percentage of net income before this item, unless the incompatible art. 32.2 reduction is chosen | 10% (derived: 5% baseline plus 5 percentage points); Ceuta qualifying income: see below | Art. 30 rule 2.ª Reglamento plus DA 67.1 Ley del IRPF; DA 67.3 applies the uplift to Q4 2026 payments | https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a30 ; https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#da-21 |
| 2026 yearly cash cap on that deduction, including the Ceuta variant | EUR 3,000 | DA 67.1: "sin que la cuantía resultante de su aplicación pueda superar 3.000 euros anuales" | https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#da-21 |
| 2026 direct-estimation payment before prior-quarter payments, withholdings and other art. 110 adjustments; qualifying Ceuta/Melilla percentage is reduced by 60% under art. 110.2 | 20% of cumulative net income from 1 January to quarter end | "el 20 por ciento del rendimiento neto correspondiente al período de tiempo transcurrido" | https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820 |
| Share of the prior year's professional-activity income that must have borne withholding or payment on account for release from that activity's quarterly payments; a new activity tests the period of the payment (art. 109.2 and 5) | 70% | "al menos el 70 por ciento de los ingresos de la actividad fueron objeto de retención" | https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820 |
| Ordinary withholding rate on a professional invoice paid by a payer obliged to withhold (art. 95.1) | 15% | "se aplicará el tipo de retención del 15 por ciento sobre los ingresos íntegros satisfechos" | https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820 |
| Professional who starts an activity: the tax period of the start and the two following periods, only where no professional activity was carried on in the year before the start date, and only once the payer has been told in writing | 7% | "el tipo de retención será del 7 por ciento en el período impositivo de inicio de actividades" | https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820 |
| Municipal collectors, insurance intermediaries who use external auxiliaries, and commercial delegates of the state lottery company, under letters a, b and c of art. 95.1. No income test applies to these three | 7% | "El tipo de retención será del 7 por ciento en el caso de rendimientos satisfechos a" | https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820 |
| Art. 95.1.d: section two groups 851, 852, 853, 861, 862, 864, 869; section three groups 01, 02, 03, 05; or the specified performing-arts/technical services; signed notice to payer required; prior-year gross income of these activities must be below this amount | EUR 15,000 | "correspondiente al ejercicio inmediato anterior sea inferior a 15.000 euros" | https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820 |
| And, for letter d only, where that income was more than this share of the person's total business and employment income in the same year. Both tests must be met | 75% | "represente más del 75 por ciento de la suma de los rendimientos íntegros de actividades económicas y del trabajo obtenidos por el contribuyente en dicho ejercicio" | https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820 |
| The professional rates in art. 95.1 are cut by this share where the income qualifies for the Ceuta and Melilla credit in art. 68.4 of the Ley del IRPF, so an invoice from a Ceuta or Melilla professional shows a lower rate and is not evidence of anything else (art. 95.1, last paragraph) | 60% | "Estos porcentajes se reducirán en un 60 por ciento cuando los rendimientos tengan derecho a la deducción en la cuota prevista en el artículo 68.4 de la Ley del Impuesto" | https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820 |
| No withholding on rent for urban premises where the rents paid by the tenant to the same landlord in the year are no more than this amount (art. 75.3.g.2.º) | EUR 900 | "Cuando las rentas satisfechas por el arrendatario a un mismo arrendador no superen los 900 euros anuales" | https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820 |

The deduction is the applicable percentage of net income before this item, limited to the annual cap; it is not a flat allowance. For 2026 the later DA 67 overrides the ordinary regulatory percentage and cap. Its extra percentage points enter Q4 payments; do not retrospectively substitute them into earlier quarterly workings. For qualifying Ceuta income the DA 64 uplift already applies to payment windows beginning after one month from its 3 September 2026 entry into force (thus the October window); DA 67 adds its further uplift for Q4. The deduction is incompatible with the single-client/TRADE reduction in art. 32.2; intake flags the choice rather than awarding either. Computation: `es-income-tax`; payments: `es-estimated-tax`.

The reduced starting rate and the special art. 95.1.d rate require communication to the payer, who keeps the signed notice. An invoice carrying a reduced rate from the table above is therefore not proof of a new autónomo: the payee may be one of the listed groups instead. Ask.

Art. 75.3.g lists two more cases with no rent withholding, which carry no figure: housing let by a company to its own employees, and a landlord whose activity is classified in group 861 of section one of the business tax tariffs, or in another heading allowing the letting or subletting of urban property, where applying the group 861 quota rules to the cadastral value of the let property would not have given a nil quota. That landlord has to prove it to the tenant.

**Withholding the client applies to rent, and expenses that need a client answer (Ley del IRPF, Ley 35/2006)**

| Item | Value | Note | Source |
| --- | --- | --- |---|
| Withholding on rent paid for urban property, declared on Modelo 115 (art. 101.8) | 19% | "subarrendamiento de bienes inmuebles urbanos, cualquiera que sea su calificación, será del 19 por ciento" | https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764 |
| That rate is cut by this share where the let property is in Ceuta or Melilla, on the terms of art. 68.4 of the same Law (art. 101.8) | 60% | "Este porcentaje se reducirá en un 60 por ciento cuando el inmueble esté situado en Ceuta o Melilla" | https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764 |
| Where the main home is partly used for the activity: the deductible share of water, gas, electricity, telephone and internet is this percentage applied to the proportion of square metres used, unless a higher or lower share is proved (art. 30.2.5.ª.b) | 30% | "en el porcentaje resultante de aplicar el 30 por ciento a la proporción existente entre los metros cuadrados" | https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764 |
| Health insurance for the worker, the spouse and children under twenty-five living with them, per insured person per year (art. 30.2.5.ª.a) | EUR 500 | "El límite máximo de deducción será de 500 euros por cada una de las personas" | https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764 |
| The same limit for each of those insured people who has a disability | EUR 1,500 | "o de 1.500 euros por cada una de ellas con discapacidad" | https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764 |
| Ceuta only, 2026 simplified activities carried on there whose income qualifies for art. 68.4; DA 64 baseline plus DA 67 uplift | 15% annually (derived: 10% plus 5 percentage points), capped at EUR 3,000; further uplift applies to Q4 payments | DA 64.1 and 3; DA 67.1 and 3 | https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#da-18 ; https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#da-21 |

**Pension contributions, the reduction limit (Ley del IRPF, art. 52)**

| Item | Value | Note | Source |
| --- | --- | --- |---|
| The reduction is the lower of this share of the net employment and business income earned individually in the year, and the cash limit below | 30% | "El 30 por 100 de la suma de los rendimientos netos del trabajo y de actividades económicas" | https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764 |
| Cash limit | EUR 1,500 | "b) 1.500 euros anuales" | https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764 |
| Increase where it comes from employer contributions, or from the worker's own contributions to the same instrument within the amounts the article sets against the employer contribution | EUR 8,500 | "En 8.500 euros anuales, siempre que tal incremento provenga de contribuciones empresariales" | https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764 |
| Increase where it comes from a self-employed person's contributions to a sectoral plan, to a simplified employment plan for the self-employed, or from the individual entrepreneur's or professional's own contributions to an employment plan they promote and belong to, or to a provident society of which they are a member; also their qualifying own business social-welfare plan or collective dependency insurance as policyholder and insured (art. 52.1.b.2.º) | EUR 4,250 | "En 4.250 euros anuales, siempre que tal incremento provenga de aportaciones a los planes de pensiones sectoriales" | https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764 |
| The two increases taken together cannot exceed this amount | EUR 8,500 | "la cuantía máxima de reducción por aplicación de los incrementos previstos en los números 1.º y 2.º anteriores será de 8.500 euros" | https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764 |

For an autónomo the relevant increase is usually the sectoral or self-employed plan one, not the employer one. Ask which plan the contributions went to, not just the amount.

**Value added tax: the rates, the retailer test and the vehicle presumption (Ley del IVA, Ley 37/1992)**

| Item | Value | Note | Source |
| --- | --- | --- |---|
| General rate (art. 90.Uno) | 21% | "El Impuesto se exigirá al tipo del 21 por ciento" | https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740 |
| Reduced rate (art. 91.Uno) | 10% | "Se aplicará el tipo del 10 por ciento a las operaciones siguientes" | https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740 |
| Super-reduced rate (art. 91.Dos) | 4% | "Se aplicará el tipo del 4 por ciento a las operaciones siguientes" | https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740 |
| Recargo de equivalencia on goods at the general rate (art. 161) | 5.2% | "Con carácter general, el 5,2 por ciento" | https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740 |
| Recargo de equivalencia on goods at the reduced rate | 1.4% | "el 1,4 por ciento" | https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740 |
| Recargo de equivalencia on goods at the super-reduced rate | 0.5% | "el 0,50 por ciento" | https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740 |
| Recargo de equivalencia on manufactured tobacco | 1.75% | "Para las entregas de bienes objeto del Impuesto Especial sobre las Labores del Tabaco, el 1,75 por ciento" | https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740 |
| Retailer test: a trader is a retailer only if, among the other conditions of art. 149.Uno, the prior year's supplies of those goods to non-business customers and to the Social Security system were more than this share of all supplies of them. The same article lifts this test for some traders classed as retailers under the business tax rules | 80% | "hubiese excedido del 80 por 100 del total de las entregas realizadas" | https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740 |
| Share of a car, its trailer, a moped or a motorcycle presumed used in the business, for deducting input VAT (art. 95.Tres.2.ª) | 50% | "se presumirán afectados al desarrollo de la actividad empresarial o profesional en la proporción del 50 por 100" | https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740 |
| Share presumed for the vehicles the same rule lists: mixed vehicles carrying goods, passenger transport for consideration, driver and pilot instruction for consideration, manufacturers' testing and sales promotion, the professional travel of commercial representatives and agents, and security services | 100% | "los vehículos que se relacionan a continuación se presumirán afectados al desarrollo de la actividad empresarial o profesional en la proporción del 100 por 100" | https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740 |

Both shares are presumptions, and rule 3 of the same article requires the deduction to be adjusted, either way, once the real degree of business use is proved. The presumption is a VAT rule only. For income tax a car counts as used in the activity only if it is used exclusively for it, with the narrow list of exceptions in art. 22.4 of the Reglamento del IRPF, which names much the same kinds of vehicle. Never carry one answer across to the other tax. The VAT work is `es-vat-return`. These presumptions require actual business use and the normal deduction conditions, evidence and invoices; ownership alone does not establish a deduction.

**Module method limits: the 2026 statutory extension**

| Limit | Value | Conditions and source |
| --- | --- | --- |
| Prior-year non-agricultural activity income | EUR 250,000 | Replaces the permanent EUR 150,000 figure for 2016 to 2027 inclusive, DT 32 Ley 35/2006 as amended by RDL 43/2026 art. 2.3: https://www.boe.es/buscar/doc.php?id=BOE-A-2026-24701 |
| Within that income, operations requiring an invoice to a business/professional acting as such | EUR 125,000 | Replaces EUR 75,000 for the same years; DT 32 and art. 31.1.3.ª: https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#dttrigesimasegunda |
| Prior-year purchases of goods and services, excluding capital assets | EUR 250,000 | Replaces EUR 150,000 for the same years; DT 32: https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#dttrigesimasegunda |

The former statute/authority discrepancy is resolved by RDL 43/2026, effective for these limits from 1 January 2026 and in force from 26 November 2026. These are exclusion limits, not a complete eligibility test: activity eligibility, annualisation, related-family aggregation, renunciation and other art. 31 conditions still matter. This workflow continues to refer all módulos cases; it must not force someone into direct estimation using the superseded permanent limits. "Check this point with one of our partner accountants."

**Reporting thresholds the intake has to test (RD 1065/2007)**

| Item | Value | Note | Source |
| --- | --- | --- |---|
| Ordinary Modelo 347 screening threshold per counterparty/year; exceeding it is a review trigger, not proof a declaration is due (arts. 32 and 33 exemptions apply); the separate professional-fee collection-on-behalf-of-members rule is held for specialist review | EUR 3,005.06 | "3.005,06 euros durante el año natural correspondiente" | https://www.boe.es/buscar/act.php?id=BOE-A-2007-15984 |
| Foreign-account screening: aggregate 31 December balances AND aggregate last-quarter averages are tested separately; this threshold exemption needs both within the limit. Other art. 42 bis exemptions and repeat-filing/cessation rules remain to be checked; do not infer an automatic declaration | EUR 50,000 | "no superen, conjuntamente, los 50.000 euros, y la misma circunstancia concurra en relación con los saldos medios" | https://www.boe.es/buscar/act.php?id=BOE-A-2007-15984 |

**Territory: the Canary Islands indirect tax (art. 51 Ley 4/2012, wording in force since 1 January 2024)**

| Item | Value | Note | Source |
| --- | --- | --- |---|
| Canary Islands general IGIC rate, charged instead of VAT on supplies not covered by any other IGIC rate | 7% | "El tipo general del 7 por ciento, aplicable a las entregas de bienes y prestaciones de servicios" | https://www.boe.es/buscar/act.php?id=BOE-A-2012-9282 |

**Territory: the Ceuta and Melilla income tax credit (art. 68.4 Ley 35/2006)**

| Item | Value | Note | Source |
| --- | --- | --- |---|
| Credit against the tax on income earned in Ceuta or Melilla by someone habitually and effectively resident there | 60% | "se deducirán el 60 por ciento de la parte de la suma de las cuotas íntegras" | https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764 |

**Territory: the Ceuta and Melilla contribution bonification before 1 October 2026 (art. 36 Ley 20/2007 as worded by Real Decreto-ley 1/2023)**

| Item | Value | Note | Source |
| --- | --- | --- |---|
| Bonification of the common contingencies contribution, listed sectors, for self-employed workers who live and work in Ceuta or Melilla | 50% | "tendrán derecho a una bonificación del 50 por ciento de la cuota por contingencias comunes" | https://www.boe.es/buscar/act.php?id=BOE-A-2023-625 |

**Territory: the Ceuta and Melilla contribution bonification from 1 October 2026 (art. 36 Ley 20/2007 as worded by Real Decreto-ley 22/2026)**

| Item | Value | Note | Source |
| --- | --- | --- |---|
| Bonification of the common contingencies contribution, listed sectors, for cuotas accrued from 1 October 2026 | 75% | "tendrán derecho a una bonificación del 75 por ciento de la cuota por contingencias comunes" | https://www.boe.es/buscar/act.php?id=BOE-A-2007-13409 |

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
- **Option 2.** Collect the workspace plan, actual exclusive use, census declaration and costs. Do not decide entitlement from a room label or the census declaration alone. Art. 22.3 Reglamento requires a separately and independently usable part. Leave disputed use on hold: "Check this point with one of our partner accountants."
- **Option 3.** Shared/private use is unresolved; collect the facts and hold the deduction. "Check this point with one of our partner accountants."
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

Collect the invoice, contracting party, business purpose and actual use. A separately contracted exclusive business line is considered for deduction by `es-income-tax`; an invoice alone does not prove eligibility. Do not apply a chosen business-use percentage to an indivisible mixed-use item: art. 22.2 and 3 Reglamento limits affectation. The statutory home-utilities rule is separate. Mixed phone/internet use remains non-usable until reviewed: "Check this point with one of our partner accountants."

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

If yes, ask for the amount and which plan received it. The limit and the two increases are in the pension table above. The EUR 8,500 increase is not a standalone total allowance; the employer/employee matching limits, including the salary condition, need the actual contribution certificate. Do not award an increase merely because the user selects “employer plan”. Unresolved matching: "Check this point with one of our partner accountants."

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

Then invoke `es-return-assembly` with the structured intake package. Include only the returns actually required after transaction-level territorial and exemption checks; fiscal domicile or an exempt activity label alone must not suppress Modelo 303 or a non-periodic settlement.

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

Pass `territory` as `ceuta` or `melilla` distinctly, together with the actual location of activities and evidence of art. 68.4 eligibility; a city label alone does not establish the Ceuta uplift.

## Section 9: refusal handling

Refusals fire either from the refusal sweep in Section 2 or during inference, for example when a company structure turns up in the documents.

For every referral below or elsewhere, state: "Check this point with one of our partner accountants." Do not present a held outcome as usable.

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

**Check IN5.** Gap filling asked only about things not visible in documents. Reconcile actual payments, but establish registration dates from registration evidence, not bank debits.

**Check IN6.** Open flags captured. Anything ambiguous, risky or attention worthy during inference is in the `open_flags` list in the handoff package.

**Check IN7.** The handoff to `es-return-assembly` is explicit. The user was told the return preparation is starting, and the orchestrator was invoked with the intake package.

**Check IN8.** The reviewer step was stated at the start and repeated before the handoff.

**Check IN9.** Refusals were clean. No hedging. Stop means stop.

**Check IN10.** No meta-commentary about workflow phases.

**Check IN11.** The user-facing turn count is low. Target: eight turns or fewer from start to handoff for a prepared user. More than twelve turns for a normal intake is a failure.

**Check IN12.** The estimación directa method is established, the IAE section is established, and the withholding rate on the client's invoices was read off the invoices rather than inferred, before the handoff.

**Check IN13.** Territory and transactions are established; no VAT return was suppressed solely because of fiscal domicile, recargo or an exempt activity label.

**Check IN14.** No assumed 2026 reduced monthly contribution was stated; actual receipt amounts and the held historical fixture are clearly distinguished.

**Check IN15.** Módulos is referred using the current statutory extension, with no false unresolved discrepancy or automatic eligibility decision.

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
- **v0.5 (14 November 2026):** declared as a router; every figure row now carries its official URL, and every quoted figure was found again on the consolidated BOE and Agencia Tributaria pages on 14 November 2026; Sources say what each page was read for.
- **v0.6 (27 November 2026):** incorporated the new 2026 deduction and módulos amendments; corrected evidence, territorial, exemption and mixed-use shortcuts; preserved original calculations and held historical case inputs.

## End of the intake skill

## The method, step by step

1. Run the refusal sweep in Section 2 before anything else, and stop where it says stop. Residence for the whole calendar year (art. 9 Ley 35/2006), structure and alta en RETA decide whether this workflow applies at all: https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764 A non-resident is taxed under the non-resident income tax and a company files Modelo 200; neither is this workflow.
2. Establish the census position from the client's Modelo 036: the date of alta in the Censo de Empresarios, Profesionales y Retenedores, the IAE heading, the income tax regime and the VAT regime. The census obligations are in RD 1065/2007: https://www.boe.es/buscar/act.php?id=BOE-A-2007-15984 The form is Modelo 036 only; Modelo 037 was suppressed by Orden HAC/1526/2024, in force from 3 February 2025: https://www.boe.es/buscar/doc.php?id=BOE-A-2025-410
3. Establish RETA dates from registration history or alta/baja resolutions, and reconcile the base and cuota month by month against receipts and any reduced-contribution resolution. Do not state an amount for that contribution. The rules are in art. 38 ter Ley 20/2007: https://www.boe.es/buscar/act.php?id=BOE-A-2007-13409
4. Take the document dump in Section 3, then run the inference pass in Section 4 before asking a single content question.
5. Fix the income tax regime against art. 28 and art. 30 of the Reglamento del IRPF and the turnover limit in the Section 6 table: https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820 If the client says módulos, stop and use the current statutory extension in that section when explaining the referral. Record whether the client has one single client or is a TRADE, for art. 32.2 Ley 35/2006.
6. Fix the VAT position: general, recargo de equivalencia under arts. 148 to 163, exempt under art. 20.Uno, or mixed. Ley 37/1992: https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740 Art. 3 excludes Canarias, Ceuta and Melilla from Spanish VAT territory; check the place and nature of each transaction before selecting or suppressing any return.
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

### Original 2025 intake and handoff fixture: non-usable hold

This preserves the original illustration's inputs, not a client return or a 2026 position. All eligibility, classifications, depreciation and tax conclusions below remain non-usable. "Check this point with one of our partner accountants."

- **Year and identity facts.** 2025; Madrid; individual autónomo; stated simplified estimation; RETA alta March 2023; activity code 8411 as originally labelled. Neither the classification nor the original “more than 3 years” inference is established.
- **Activity income.** EUR 48,000: EUR 24,000 domestic retainer, EUR 12,000 German customer, EUR 12,000 other domestic clients. Customer VAT status and receiving establishment remain unproven.
- **Original invoice totals.** Domestic base EUR 36,000; illustrative 21% VAT EUR 7,560; illustrative 15% withholding EUR 5,400. Arithmetic is checked below; applicability remains held.
- **Running costs.** Office/coworking EUR 3,600; software EUR 1,200; liability insurance EUR 350; accountancy EUR 600; phone/internet EUR 720 with unresolved use; office supplies EUR 400. Deductibility is not established by the list.
- **Laptop.** EUR 1,500, purchased June 2025; original 25% depreciation assertion held. Collect the in-service date, applicable table and any election before calculating depreciation.
- **RETA and VAT input.** Stated EUR 300 monthly for 12 months, total EUR 3,600; stated contribution base EUR 1,000 monthly; stated input VAT EUR 1,350. These are fixture amounts, not statutory rates or proven deductible amounts.
- **Filed/remaining returns.** Q1 to Q3 2025 Modelo 303/130 said to be filed; Q4 outstanding; stated VAT credit EUR 0; stated cumulative payments EUR 2,100. Preserve as inputs; the original description as a simple multiplication of quarterly net income is not a verified computation.
- **Prior year and handoff.** 2024 liability EUR 5,200; 2024 net activity income EUR 28,000; the original handoff's approximately EUR 32,000 net income is held, not recomputed as fact.
- **Original outstanding facts.** Phone/internet use; German customer/ROI/Modelo 349; Q4 2025 VAT and IRPF payments; home workspace. Retain each in `open_flags`; no historic amount is copied into a current return.

```oa-check
name: Historical Spain 2025 intake fixture arithmetic only, tax outcomes held
inputs:
  retainer: 24000
  german_customer: 12000
  other_domestic: 12000
  vat_rate: 0.21
  withholding_rate: 0.15
  monthly_reta: 300
  months: 12
steps:
  total_income: retainer + german_customer + other_domestic
  domestic_base: retainer + other_domestic
  illustrative_vat: domestic_base * vat_rate
  illustrative_withholding: domestic_base * withholding_rate
  receipt_total: monthly_reta * months
expected:
  total_income: 48000
  domestic_base: 36000
  illustrative_vat: 7560
  illustrative_withholding: 5400
  receipt_total: 3600
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
- Any client whose fiscal domicile is in the Basque Country or Navarra. Use a practitioner who establishes the applicable foral residence/competence rules; a postal address alone is not the legal test.
- Any client in estimación objetiva (módulos), or whose eligibility is uncertain: "Check this point with one of our partner accountants." The current statutory extension in Section 6 replaces the former conflicting-limits hold.
- Any autonomous community deduction or the community half of the scale; collect the applicable regional law and use `es-irpf-deductions`.
- Any IPSI rate or return for Ceuta or Melilla, and any IGIC return for the Canary Islands.
- A Ceuta or Melilla client in building construction, for the contribution bonification before 1 October 2026: the wording does not settle it.
- Any assumed monthly amount or entitlement for the reduced starting contribution in this tax year: "Check this point with one of our partner accountants." Read actual payments from receipts.
- A prorrata or a separate sector of activity for a mixed exempt and taxable business. That is `es-vat-return` work and needs a reviewer.
- Anything with a foreign element: a client abroad, work abroad, a treaty, or a move in or out of Spain.
- A licence, a permit or a local business tax: collect the competent authority and the applicable local rules; do not infer them here.

## Sources

The provisions named below were read on 2026-11-27. This is a 2026 intake: amendments expressly effective in 2027 are not used for 2026. Consolidated texts were checked against the amending act where timing changes the answer.

| Official source | Scope read | Read on |
|---|---|---|
| [Ley 35/2006, Ley del IRPF](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764) | Read arts. 9, 12, 30, 32.2, 52, 68.4, 101.8, DA 64 and 67, DT 32; uplift, cap and payment timing | 2026-11-27 |
| [RD 439/2007, Reglamento del IRPF](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820) | Read arts. 22, 28 to 30, 75, 76, 95, 108 to 110; distinguish 2027-only changes | 2026-11-27 |
| [Ley 37/1992, Ley del IVA](https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740) | Read arts. 3, 69, 90, 91, 94, 95, 148, 149, 154, 161; exemption eligibility is referred under art. 20 | 2026-11-27 |
| [RD 1624/1992, Reglamento del IVA](https://www.boe.es/buscar/act.php?id=BOE-A-1992-28925) | Read art. 71.1, 3, 7 and 8: periodic filings, exempt-only exclusion and non-periodic exceptions | 2026-11-27 |
| [RD 1065/2007, gestión e inspección](https://www.boe.es/buscar/act.php?id=BOE-A-2007-15984) | Read arts. 9, 32.c and 42 bis: census and screening thresholds, exemptions and repeat filing | 2026-11-27 |
| [Orden HAC/1526/2024, suppressing Modelo 037](https://www.boe.es/buscar/doc.php?id=BOE-A-2025-410) | Read for the suppression of Modelo 037 and its entry into force | 2026-11-27 |
| [Ley 20/2007, Estatuto del trabajo autónomo](https://www.boe.es/buscar/act.php?id=BOE-A-2007-13409) | Read for art. 38 ter and the 75% Ceuta and Melilla bonification from 1 October 2026 | 2026-11-27 |
| [Real Decreto-ley 1/2023](https://www.boe.es/buscar/act.php?id=BOE-A-2023-625) | Read for the 50% Ceuta and Melilla bonification of common contingencies | 2026-11-27 |
| [Ley 4/2012 de Canarias, IGIC rates](https://www.boe.es/buscar/act.php?id=BOE-A-2012-9282) | Read art. 51.1.d, general IGIC rate and other-rate condition | 2026-11-27 |
| [RDL 13/2022, DT 5](https://www.boe.es/buscar/doc.php?id=BOE-A-2022-12482) | Read the 2023 to 2025 fixed contribution and the distinct 2026 Budget Law delegation; no 2026 amount inferred | 2026-11-27 |
| [AEAT, withholding obligations](https://sede.agenciatributaria.gob.es/Sede/irpf/retenciones-ingresos-cuenta-pagos-fraccionados/retenciones-ingresos-cuenta/obligaciones-retenedor.html) | Read the payment and annual-summary model routing, including rent summary | 2026-11-27 |
| [RDL 43/2026, art. 2 and entry into force](https://www.boe.es/buscar/doc.php?id=BOE-A-2026-24701) | Read 2026 expense uplift/cap and Q4 timing, extended módulos limits, and 2027-only IRPF/VAT amendments | 2026-11-27 |

Not yet confirmed: a usable 2026 reduced RETA monthly amount/entitlement; the pre-October Ceuta/Melilla construction-sector bonification outcome; mixed-use phone/internet deductions; the historical 2025 case's eligibility, depreciation and final tax result. Each stays on a non-usable hold: "Check this point with one of our partner accountants." Módulos limits themselves are now established by DT 32; full regime eligibility remains a specialist referral. Local IPSI/IGIC filing, foral law, foreign treatment and personal/community deductions remain outside this intake's calculations, with the routes above preserved.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as an asesor fiscal, gestor administrativo, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.
