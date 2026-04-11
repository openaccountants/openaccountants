---
name: es-return-assembly
description: Final orchestrator skill that assembles the complete Spain filing package for Spain-resident self-employed individuals (autónomos). Consumes outputs from all Spain content skills (spain-vat-return for Modelo 303, es-income-tax for IRPF Modelo 100, es-social-contributions for RETA, es-estimated-tax for Modelo 130 pagos fraccionados) to produce a single unified reviewer package containing every worksheet, every form, every brief section, all cross-skill reconciliations, and the final action list with payment instructions, filing instructions, and next-year planning. This is the capstone skill that runs last and produces the final deliverable. MUST be loaded alongside all Spain content skills listed above. Spain full-year residents only. Autónomos (self-employed individuals) only.
version: 0.1
---

# Spain Return Assembly Skill v0.1

## CRITICAL EXECUTION DIRECTIVE -- READ FIRST

**When this skill is invoked, you have already passed through intake. The user has consented to the full workflow. Execute all steps without pausing for permission.**

Specifically:

- **Do NOT ask the user "how deep do you want me to go"** or "do you want the full package" or any variant. The user asked for their tax returns. They want their tax returns. Produce them.
- **Do NOT announce how many tokens or tool calls this will take.** Execute.
- **Do NOT ask which deliverables to prioritise.** Produce all deliverables listed in Section 4. If you run out of context mid-execution, finish the computation work first (numbers, positions, flags) then produce whatever formatted outputs you can, and at the very end state clearly which deliverables were not produced and why.
- **Do NOT re-validate scope that intake already validated.** If `es-freelance-intake` produced an intake package, trust it. You can cross-check specific numbers during reconciliation but do not re-interrogate the user about residency, business structure, or anything else intake already captured.
- **Do NOT pause between content skills to check in.** Run them in dependency order (Section 2) without prose status updates between each one. A single status message at the end is fine.
- **Self-checks are targets, not blockers.** If a self-check fails, note it in the reviewer brief's open flags section and continue. Do NOT halt the entire workflow because one self-check had an ambiguous answer.
- **Primary source citations go in the final reviewer brief, not in intermediate computation steps.**

**The user has already been told (by the intake skill) that the final package requires asesor fiscal signoff before filing. State it once in the final output and move on.**

**Failure mode to avoid:** The skill halts mid-execution and asks the user a meta-question about workflow pacing. If you feel the urge to ask "how should I proceed," the correct action is to pick the most defensible path and proceed, flagging the decision in the reviewer brief so the reviewer can challenge it.

---

## What this file is

The final capstone skill for Spain self-employed returns. Every Spain content skill feeds into this one. The output is the complete reviewer package that an asesor fiscal can review, sign off on, and deliver to the client along with filing instructions.

This skill coordinates execution of the content skills, verifies cross-skill consistency, and assembles the final deliverable.

---

## Section 1 -- Scope

Produces the complete Spain filing package for:
- Full-year Spanish residents (territorio común -- excludes País Vasco and Navarra foral regimes)
- Autónomos (self-employed individuals, personas físicas)
- Tax year 2025
- Filing Modelo 303 (IVA trimestral), IRPF Modelo 100, RETA reconciliation, Modelo 130 (pagos fraccionados)

---

## Section 2 -- Execution order and dependency chain

The skill enforces the following execution order:

1. **`spain-vat-return`** -- Modelo 303 IVA return (Q2 skill)
   - Runs first because IVA base imponible feeds into the IRPF
   - For Q4 2025: prepare Modelo 303 if not yet filed; verify Q1-Q3 figures
   - Reconcile facturas emitidas (output IVA) with facturas recibidas (input IVA)
   - Handle intracomunitarias (reverse charge, Modelo 349)
   - Output: Modelo 303 box values, IVA devengado, IVA soportado deducible, result (a ingresar / a compensar / a devolver)

2. **`es-income-tax`** -- IRPF Modelo 100 annual return (Q2 skill)
   - Depends on IVA output: rendimiento íntegro de actividades económicas must use base imponible (ex-IVA) from Modelo 303
   - Compute rendimiento neto: ingresos - gastos deducibles - amortización - RETA cuotas
   - Apply gastos de difícil justificación (5%, max EUR 2,000) for simplificada
   - Apply reducciones (if applicable)
   - Compute base imponible general + base del ahorro
   - Apply escala estatal + autonómica
   - Deduct retenciones, pagos fraccionados (Modelo 130)
   - Output: Modelo 100 key boxes, cuota líquida, resultado de la declaración

3. **`es-social-contributions`** -- RETA cotizaciones sociales (Q2 skill)
   - Depends on IRPF: RETA cuotas are a gasto deducible in the rendimiento neto computation
   - Reconcile actual cuotas paid vs the new income-based contribution system (since 2023)
   - Verify base de cotización is appropriate for income level
   - Flag if regularisation is expected (TGSS adjusts RETA based on actual income, with potential refund or additional payment)
   - Output: annual RETA paid, base de cotización, regularisation estimate, deductibility confirmation

4. **`es-estimated-tax`** -- Modelo 130 pagos fraccionados (Q4 stub, compute 20% quarterly)
   - Depends on IRPF: pagos fraccionados are computed as 20% of rendimiento neto acumulado minus retenciones acumuladas
   - **Status check:** es-estimated-tax is currently a Q4 stub. If the stub has substantive computation content, use it. If it is still a placeholder, compute Modelo 130 using the standard formula (Art. 110 LIRPF: 20% x rendimiento neto acumulado - retenciones - pagos fraccionados anteriores) and flag in the reviewer brief that the dedicated skill was not available.
   - Output: Q4 2025 Modelo 130 computation, and 2026 quarterly schedule

If any upstream content skill fails to produce validated output, the assembly skill notes the failure in the reviewer brief and continues with available data rather than halting entirely.

---

## Section 3 -- Cross-skill reconciliation

### Cross-check 1: Modelo 303 base imponible = IRPF ingresos de actividades económicas

| IVA Output | IRPF Input | Rule |
|-----------|-----------|------|
| Modelo 303 total base imponible (annual) | Modelo 100 rendimiento íntegro actividades económicas | Must match within EUR 1 |
| Domestic supplies base imponible | IRPF ingresos with IVA repercutido | Ex-IVA amount |
| Intracomunitarias (reverse charge) | IRPF ingresos | Included in income, IVA neutral |
| Exportaciones (non-EU) | IRPF ingresos | Included in income, IVA exempt with right to deduction |

**If mismatch:** Flag for reviewer. Common causes: timing differences (devengo vs cobro if using criterio de caja), autoconsumo, corrective invoices (facturas rectificativas).

### Cross-check 2: RETA cuotas = gasto deducible in IRPF

| RETA Output | IRPF Input | Rule |
|------------|-----------|------|
| Total RETA cuotas paid in 2025 | Gastos de Seguridad Social in Modelo 100 | Must match exactly |
| Tarifa plana months (if applicable) | Lower cuota for those months | Correctly reflected |
| Regularisation payment/refund | Included in year paid / received | Adjusts deductible amount |

**If mismatch:** Verify months of alta. Part-year alta means prorated cuotas. If regularisation happened in 2025 for prior year, it is deductible in 2025.

### Cross-check 3: Retenciones credit against final IRPF cuota

| Source | Amount | Treatment |
|--------|--------|-----------|
| Retenciones soportadas on facturas emitidas | Sum from facturas / Modelo 190 data | Credit against cuota íntegra in Modelo 100 |
| Retenciones from employment (if any) | From nómina / Modelo 190 | Credit against cuota íntegra |
| Retenciones from capital income (if any) | From bank certificates | Credit against cuota íntegra |

**Rule:** Total retenciones deducted in Modelo 100 must equal the sum of all retenciones from all sources. If retenciones exceed cuota íntegra, the result is a devolver (refund).

**If mismatch:** Common cause is retención not actually withheld (client paid gross despite invoice showing retención). Flag for reviewer: income still declared at gross, but retención credit requires actual withholding.

### Cross-check 4: Modelo 130 pagos fraccionados credit against final IRPF

| Source | Amount | Treatment |
|--------|--------|-----------|
| Modelo 130 Q1-Q4 payments | Sum of four quarterly payments | Credit against cuota líquida in Modelo 100 |
| Formula: 20% x rendimiento neto acumulado - retenciones acumuladas - pagos anteriores | Per quarter | Standard computation |

**Rule:** If retenciones on professional invoices cover > 70% of income, Modelo 130 filing is not required (Art. 110.3.c RIRPF). Check this condition.

**If mismatch between computed Modelo 130 and amounts actually paid:** Flag for reviewer. If underpaid, no separate penalty (it washes into the annual IRPF), but cash flow impact. If overpaid, credit against IRPF.

---

## Section 4 -- Final reviewer package contents

### Documents

1. **Executive summary** -- one-page overview: filing status, income, tax liability, IVA position, RETA, pagos fraccionados, resultado de la declaración
2. **Modelo 303 worksheet** -- box-by-box with formulas (Q4 2025 or annual reconciliation)
3. **IRPF Modelo 100 worksheet** -- rendimiento neto computation, base imponible, escala estatal + autonómica, cuota líquida, resultado
4. **Amortisation schedule** -- asset register with cost, date, coefficient máximo, annual amortisation, valor neto contable
5. **RETA reconciliation** -- cuotas paid, base de cotización, regularisation estimate
6. **Modelo 130 worksheet** -- Q4 2025 computation and 2026 quarterly schedule
7. **Cross-skill reconciliation summary** -- all four cross-checks with pass/fail and notes
8. **Reviewer brief** -- comprehensive narrative with positions, citations, flags, self-check results
9. **Client action list** -- what the client needs to do, with dates and amounts

### Reviewer brief contents

```markdown
# Complete Return Package: [Client Name] -- Tax Year 2025

## Executive Summary
- Filing status: [Individual -- Resident]
- Comunidad autónoma: [Madrid / Cataluña / etc.]
- Business: Autónomo, estimación directa [simplificada / normal]
- IVA registration: Standard (régimen general)
- Modelo 303 Q4 position: EUR X a ingresar / a compensar
- IRPF rendimiento neto actividades: EUR X
- IRPF base imponible general: EUR X
- IRPF cuota íntegra: EUR X
- Retenciones: EUR X
- Pagos fraccionados (Modelo 130): EUR X
- IRPF resultado declaración: EUR X a ingresar / a devolver
- RETA annual cuotas: EUR X
- 2026 Modelo 130 quarterly schedule: EUR X per quarter

## IVA Return (Modelo 303)
[Content from spain-vat-return output]
- Registration type and period
- IVA devengado (output IVA) by rate (21%, 10%, 4%)
- IVA soportado deducible (deductible input IVA)
- Intracomunitarias (Modelo 349 summary)
- Prorrata (if applicable)
- Result per quarter and annual summary
- Modelo 390 annual summary reconciliation

## Income Tax Return (IRPF Modelo 100)
[Content from es-income-tax output]
- Rendimiento íntegro de actividades económicas
- Gastos deducibles schedule (with gastos de difícil justificación if simplificada)
- Amortización schedule
- RETA cuotas deducted
- Rendimiento neto de actividades
- Reducciones (if applicable)
- Other income heads (rendimientos del trabajo, del capital, ganancias patrimoniales)
- Base imponible general
- Base del ahorro (if applicable)
- Mínimo personal y familiar
- Escala estatal + escala autonómica ([comunidad])
- Cuota íntegra
- Deducciones (planes de pensiones, vivienda habitual, maternidad, etc.)
- Cuota líquida
- Retenciones deducted
- Pagos fraccionados deducted
- Resultado: a ingresar / a devolver

## Social Contributions (RETA)
[Content from es-social-contributions output]
- Alta date and months of contribution
- Base de cotización declared
- Monthly cuota and annual total
- Tarifa plana (if applicable)
- Income-based regularisation estimate (new system since 2023)
- Deductibility confirmed in IRPF

## Estimated Tax (Modelo 130)
[Content from es-estimated-tax output, or computed from standard formula if stub]
- Q4 2025 computation: 20% x rendimiento neto acumulado - retenciones acumuladas - pagos anteriores
- Check: if retenciones > 70% of ingresos, Modelo 130 not required
- 2026 quarterly schedule based on 2025 results
- Q1 2026: 1-20 April 2026
- Q2 2026: 1-20 July 2026
- Q3 2026: 1-20 October 2026
- Q4 2026: 1-30 January 2027

## Cross-skill Reconciliation
- Modelo 303 base imponible vs IRPF ingresos: [pass/fail]
- RETA cuotas vs IRPF gasto deducible: [pass/fail]
- Retenciones credit vs IRPF cuota: [pass/fail]
- Modelo 130 pagos vs IRPF credit: [pass/fail]

## Reviewer Attention Flags
[Aggregated from all upstream skills]
- Estimación directa type confirmed (simplificada vs normal)
- Gastos de difícil justificación applied at 5% (max EUR 2,000)
- Mixed-use expense percentages (phone, internet, vehicle)
- Home office deduction (despacho en casa -- if claimed, verify Modelo 036 declaration)
- EU clients -- Modelo 349 filing obligation
- Retención rate (7% new autónomo vs 15% standard)
- RETA regularisation exposure (income-based system adjustment)
- Vehicle IVA deduction at 50% default (higher requires exclusive business use proof)
- Any turnover approaching thresholds (e.g., EUR 600,000 for estimación directa simplificada)

## Positions Taken
[List with legislation citations]
- e.g., "Estimación directa simplificada applied -- Art. 30 LIRPF, Art. 28-30 RIRPF"
- e.g., "Gastos de difícil justificación: 5% of rendimiento neto previo, max EUR 2,000 -- Art. 30.2.4a LIRPF"
- e.g., "RETA cuotas deducted as gasto de actividad -- Art. 28.1 LIRPF"
- e.g., "Retención del 7% applied (autónoma in first 3 years) -- Art. 95.1 RIRPF"
- e.g., "Despacho en casa: 30% of proportional suministros -- Art. 30.2.5a LIRPF (from 2018)"
- e.g., "Laptop amortised at 25% per Tabla de Amortización Simplificada, Grupo 5"
- e.g., "Export of services to EU (Germany): exenta con derecho a deducción -- Art. 21 LIVA"

## Planning Notes for 2026
- Modelo 130 quarterly schedule (amounts and dates)
- Modelo 303 quarterly filing calendar
- RETA base de cotización review (income-based adjustment)
- Amortisation schedule continuing into 2026
- Modelo 349 recapitulativo (if EU intracomunitarias)
- Modelo 390 annual IVA summary (January 2027)
- Any legislative changes affecting 2026 (Presupuestos Generales del Estado)

## Client Action List

### Immediate (before filing deadlines):
1. Review this return package with your asesor fiscal
2. File Q4 2025 Modelo 303 (deadline: 30 January 2026 -- ALREADY PASSED, check if filed)
3. File Q4 2025 Modelo 130 (deadline: 30 January 2026 -- ALREADY PASSED, check if filed)
4. File Modelo 100 IRPF 2025 (campaign opens April 2026, deadline: 30 June 2026)
5. Pay IRPF resultado a ingresar of EUR X (or request devolución)
6. Option: split IRPF payment 60/40 (60% at filing, 40% by 5 November 2026)

### Modelo 303 filing calendar 2026:
- Q1 2026 (Jan-Mar): file 1-20 April 2026
- Q2 2026 (Apr-Jun): file 1-20 July 2026
- Q3 2026 (Jul-Sep): file 1-20 October 2026
- Q4 2026 (Oct-Dec): file 1-30 January 2027

### Modelo 130 filing calendar 2026:
- Q1 2026: file 1-20 April 2026
- Q2 2026: file 1-20 July 2026
- Q3 2026: file 1-20 October 2026
- Q4 2026: file 1-30 January 2027

### Modelo 349 (if EU intracomunitarias):
- Quarterly or annual depending on volume (annual if < EUR 35,000)

### RETA:
- Monthly auto-debit continues
- Review base de cotización in light of 2025 actual income
- Regularisation may occur in H2 2026 for 2025 income

### Ongoing:
1. Issue facturas conforming to Reglamento de Facturación (RD 1619/2012)
2. Maintain libro de ingresos and libro de gastos (estimación directa simplificada)
3. File Modelo 303 and 130 quarterly
4. Retain all facturas and justificantes for 4 years (prescripción tributaria)
5. Monitor RETA base de cotización vs actual income
6. File Modelo 390 (annual IVA summary) by 30 January following year
7. File Modelo 347 (operaciones con terceros > EUR 3,005.06) by 28 February
```

---

## Section 5 -- Refusals

**R-ES-1 -- Upstream skill did not run.** Name the specific skill. Note: this is a warning, not a hard stop. Continue with available data and flag the gap.

**R-ES-2 -- Upstream self-check failed.** Name the specific check and note it in the reviewer brief. Continue.

**R-ES-3 -- Cross-skill reconciliation failed.** Name the specific reconciliation and describe the discrepancy. Flag for reviewer but continue.

**R-ES-4 -- Intake incomplete.** Specific missing intake items prevent computation. List what is missing and ask the user for the specific data point.

**R-ES-5 -- Out-of-scope item discovered during assembly.** E.g., rental income requiring separate rendimiento del capital inmobiliario computation, capital gains requiring ganancias patrimoniales schedule, or imputación de rentas inmobiliarias for empty properties. Flag and exclude from computation.

---

## Section 6 -- Self-checks

**Check ES-A1 -- All upstream skills executed.** spain-vat-return, es-income-tax, es-social-contributions all produced output. es-estimated-tax produced output or was computed from standard formula.

**Check ES-A2 -- Modelo 303 base imponible matches IRPF ingresos.** Within EUR 1 tolerance.

**Check ES-A3 -- RETA cuotas deducted in IRPF match actual payments.** Exact match.

**Check ES-A4 -- Retenciones in IRPF match sum of all retenciones from sources.** Retenciones from professional activity + employment + capital = total deducted.

**Check ES-A5 -- Pagos fraccionados (Modelo 130) correctly credited in IRPF.** Sum of Q1-Q4 payments deducted against cuota líquida.

**Check ES-A6 -- Gastos de difícil justificación correctly applied (simplificada only).** 5% of rendimiento neto previo (before this deduction), max EUR 2,000.

**Check ES-A7 -- Escala estatal + autonómica correctly applied.** Correct comunidad autónoma rates used for the autonómica tramo.

**Check ES-A8 -- Vehicle IVA deduction at appropriate rate.** Default 50% unless exclusive business use demonstrated.

**Check ES-A9 -- Home office (if claimed) correctly computed.** Proportional m2 applied to eligible costs; suministros at 30% of proportional share (simplificada rule from 2018).

**Check ES-A10 -- Retención rate correct.** 7% for first 3 calendar years from alta; 15% thereafter. Check alta date.

**Check ES-A11 -- Filing calendar is complete.** All deadlines for Modelo 303, 130, 100, 349, 390, and 347 are listed with specific dates.

**Check ES-A12 -- Reviewer brief contains legislation citations.** Every position taken references the specific article of LIRPF, RIRPF, LIVA, RIVA, or relevant regulation.

---

## Section 7 -- Output files

The final output is **three files**:

1. **`[client_slug]_2025_spain_master.xlsx`** -- Single master workbook containing every worksheet and computation. Sheets include: Cover, Modelo 303 (Q4 or annual reconciliation), IRPF Modelo 100 (rendimiento neto, base imponible, escala, cuota, resultado), Amortisation Schedule, Gastos Detail, RETA Reconciliation, Modelo 130 (Q4 2025 + 2026 schedule), Cross-Check Summary. Use live formulas where possible -- e.g., IRPF ingresos cell references the Modelo 303 base imponible cell; RETA gasto references the RETA sheet total; Modelo 130 references IRPF rendimiento neto. Verify no `#REF!` errors. Verify computed values match within EUR 1 before shipping.

2. **`reviewer_brief.md`** -- Single markdown file covering all sections from Section 4 above: executive summary, IVA return, IRPF, RETA, Modelo 130, cross-skill reconciliation, flags, positions, planning notes.

3. **`client_action_list.md`** -- Single markdown file with step-by-step actions: immediate filings and payments, quarterly calendar for 2026, ongoing compliance reminders.

**If execution runs out of context mid-build:** produce whatever is complete, then state at the end which of the three files were not produced or are partial.

**All files are placed in `/mnt/user-data/outputs/` and presented to the user via the `present_files` tool at the end.**

---

## Section 8 -- Cross-skill references

**Inputs:**
- `es-freelance-intake` -- structured intake package (JSON)
- `spain-vat-return` -- Modelo 303 box values and classification output
- `es-income-tax` -- IRPF Modelo 100 computation output
- `es-social-contributions` -- RETA reconciliation output
- `es-estimated-tax` -- Modelo 130 computation (or fallback computation)

**Outputs:** The final reviewer package. No downstream skill.

---

## Section 9 -- Known gaps

1. PDF form filling is not automated. The reviewer uses the worksheets to fill official AEAT forms on the Sede Electrónica.
2. E-filing is handled by the reviewer via AEAT Sede Electrónica (with certificado digital or Cl@ve), not by this skill.
3. Payment execution is the client's responsibility; the skill only provides instructions and amounts.
4. es-estimated-tax is a Q4 stub. Until it is fleshed out, Modelo 130 is computed using the standard formula (Art. 110 LIRPF). This is a redundancy, not a gap -- the formula is deterministic.
5. Multi-year amortisation tracking assumes the prior year schedule is provided. If not, only current-year acquisitions are amortised.
6. Rental income (rendimiento del capital inmobiliario) is out of scope.
7. Capital gains (ganancias patrimoniales) are out of scope beyond noting them as other income.
8. Imputación de rentas inmobiliarias (imputed income on empty properties) is out of scope.
9. Modelo 720 (overseas assets declaration) is out of scope.
10. The package is complete only for tax year 2025; 2026 appears only as prospective planning.
11. País Vasco and Navarra foral regimes are out of scope -- territorio común (AEAT) only.

### Change log
- **v0.1 (April 2026):** Initial draft. Modelled on mt-return-assembly v0.1 adapted for Spain jurisdiction with four content skills (IVA Modelo 303, IRPF Modelo 100, RETA, Modelo 130).

## End of skill


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as an asesor fiscal, gestor administrativo, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
