---
name: de-return-assembly
description: Final orchestrator skill that assembles the complete German filing package for Germany-resident self-employed individuals (Freiberufler and Gewerbetreibende). Consumes outputs from all Germany content skills (germany-vat-return for UStVA, de-income-tax for ESt + EÜR, de-social-contributions for KV/PV/RV, de-trade-tax for GewSt, de-estimated-tax for Vorauszahlungen) to produce a single unified reviewer package containing every worksheet, every form, every brief section, all cross-skill reconciliations, and the final action list with payment instructions, filing instructions, and next-year planning. This is the capstone skill that runs last and produces the final deliverable. MUST be loaded alongside all Germany content skills listed above. Germany full-year residents only. Self-employed individuals and sole proprietors only.
version: 0.1
---

# Germany Return Assembly Skill v0.1

## CRITICAL EXECUTION DIRECTIVE -- READ FIRST

**When this skill is invoked, you have already passed through intake. The user has consented to the full workflow. Execute all steps without pausing for permission.**

Specifically:

- **Do NOT ask the user "how deep do you want me to go"** or "do you want the full package" or any variant. The user asked for their tax returns. They want their tax returns. Produce them.
- **Do NOT announce how many tokens or tool calls this will take.** Execute.
- **Do NOT ask which deliverables to prioritise.** Produce all deliverables listed in Section 4. If you run out of context mid-execution, finish the computation work first (numbers, positions, flags) then produce whatever formatted outputs you can, and at the very end state clearly which deliverables were not produced and why.
- **Do NOT re-validate scope that intake already validated.** If `de-freelance-intake` produced an intake package, trust it. You can cross-check specific numbers during reconciliation but do not re-interrogate the user about residency, business structure, or anything else intake already captured.
- **Do NOT pause between content skills to check in.** Run them in dependency order (Section 2) without prose status updates between each one. A single status message at the end is fine.
- **Self-checks are targets, not blockers.** If a self-check fails, note it in the reviewer brief's open flags section and continue. Do NOT halt the entire workflow because one self-check had an ambiguous answer.
- **Primary source citations go in the final reviewer brief, not in intermediate computation steps.**

**The user has already been told (by the intake skill) that the final package requires Steuerberater signoff before filing. State it once in the final output and move on.**

**Failure mode to avoid:** The skill halts mid-execution and asks the user a meta-question about workflow pacing. If you feel the urge to ask "how should I proceed," the correct action is to pick the most defensible path and proceed, flagging the decision in the reviewer brief so the reviewer can challenge it.

---

## What this file is

The final capstone skill for Germany self-employed returns. Every Germany content skill feeds into this one. The output is the complete reviewer package that a Steuerberater can review, sign off on, and deliver to the client along with filing instructions.

This skill coordinates execution of the content skills, verifies cross-skill consistency, and assembles the final deliverable.

---

## Section 1 -- Scope

Produces the complete German filing package for:
- Full-year Germany residents (unbeschränkt steuerpflichtig)
- Self-employed individuals: Freiberufler (§18 EStG) and Gewerbetreibende (§15 EStG)
- Tax year 2025
- Filing UStVA / Umsatzsteuererklärung, ESt with Anlage EÜR + Anlage S/G + Anlage Vorsorgeaufwand, Gewerbesteuererklärung (if applicable), Vorauszahlungen schedule

---

## Section 2 -- Execution order and dependency chain

The skill enforces the following execution order:

1. **`germany-vat-return`** -- UStVA (Umsatzsteuer-Voranmeldung / Umsatzsteuererklärung)
   - Runs first because VAT turnover figures feed into the EÜR
   - For Regelbesteuerung: prepare outstanding monthly/quarterly UStVA; prepare annual Umsatzsteuererklärung
   - For Kleinunternehmer: no UStVA required; verify turnover stays under EUR 22,000 prior year / EUR 50,000 current year thresholds
   - Output: UStVA line values, Vorsteuer recovered/blocked, Umsatz (netto), Sondervorauszahlung reconciliation

2. **`de-income-tax`** -- ESt + EÜR (Einkommensteuererklärung with Anlage EÜR)
   - Depends on VAT output: Betriebseinnahmen in EÜR must use netto turnover for Regelbesteuerte (USt is durchlaufender Posten)
   - Depends on VAT output: blocked Vorsteuer becomes a Betriebsausgabe in EÜR
   - Includes: Anlage EÜR (Zeilen 11-90), Anlage S (Freiberufler) or Anlage G (Gewerbetreibender), Anlage Vorsorgeaufwand, AfA-Tabelle
   - Output: EÜR Gewinn, zu versteuerndes Einkommen, festzusetzende ESt, Solidaritätszuschlag, Kirchensteuer

3. **`de-social-contributions`** -- KV/PV/RV (Kranken-, Pflege-, Rentenversicherung)
   - Depends on EÜR: Gewinn determines KV/PV Beitragsbemessungsgrundlage for GKV (for following year's Beiträge)
   - KV/PV premiums paid during 2025 enter Anlage Vorsorgeaufwand as Sonderausgaben
   - Output: annual KV/PV/RV amounts, Basisabsicherung for Sonderausgaben, any Nachzahlung/Erstattung from Einkommensanpassung

4. **`de-trade-tax`** -- Gewerbesteuer (GewSt) -- only if Gewerbetreibender
   - Depends on EÜR: Gewinn aus Gewerbebetrieb is the starting point for Gewerbeertrag
   - **Status check:** de-trade-tax is currently a Q4 stub. If the stub has substantive computation content, use it. If it is still a placeholder, compute Gewerbesteuer using: Gewerbeertrag = EÜR Gewinn + Hinzurechnungen (§8 GewStG) - Kürzungen (§9 GewStG), Freibetrag EUR 24,500, Steuermesszahl 3.5%, then apply Hebesatz. Flag in the reviewer brief that the dedicated skill was not available.
   - GewSt Anrechnung on ESt: §35 EStG allows credit of 4.0x Steuermessbetrag against ESt (capped at actual GewSt paid)
   - If Freiberufler: skip entirely. Freiberufler are not subject to Gewerbesteuer.
   - Output: Gewerbeertrag, Steuermessbetrag, GewSt payable, §35 EStG Anrechnung amount

5. **`de-estimated-tax`** -- Vorauszahlungen (estimated tax payments for 2026)
   - Depends on ESt: Vorauszahlungen for next year are based on current year's festgesetzte ESt
   - **Status check:** de-estimated-tax is currently a Q4 stub. If the stub has substantive computation content, use it. If it is still a placeholder, compute Vorauszahlungen using: quarterly ESt Vorauszahlung = festgesetzte ESt / 4 (adjusted for Anrechnungsbeträge), quarterly SolZ = festgesetzter SolZ / 4, quarterly KiSt = festgesetzte KiSt / 4. Due dates: 10 Mar, 10 Jun, 10 Sep, 10 Dec. Finanzamt may adjust via Vorauszahlungsbescheid. Flag in the reviewer brief that the dedicated skill was not available.
   - Output: four quarterly instalment amounts (ESt + SolZ + KiSt) and dates for 2026

If any upstream content skill fails to produce validated output, the assembly skill notes the failure in the reviewer brief and continues with available data rather than halting entirely.

---

## Section 3 -- Cross-skill reconciliation

### Cross-check 1: UStVA turnover = EÜR Betriebseinnahmen (net of USt)

| VAT Output | EÜR Input | Rule |
|-----------|-----------|------|
| UStVA total Umsatz (netto) | EÜR Zeile 11 Betriebseinnahmen | Must match within EUR 1 |
| Regelbesteuerung: sum of Umsätze at 19% + 7% (netto) | EÜR Betriebseinnahmen (excl. USt as durchlaufender Posten) | USt collected is NOT Betriebseinnahmen in EÜR |
| Kleinunternehmer: declared Umsatz | EÜR Betriebseinnahmen (brutto = netto, no USt separation) | Turnover is gross |

**If mismatch:** Flag for reviewer. Common causes: timing differences (Ist- vs Soll-Versteuerung), innergemeinschaftliche Leistungen, steuerfreie Umsätze, private Kfz-Nutzung (USt on Eigenverbrauch).

### Cross-check 2: ESt net income feeds Sozialversicherung Beitragsbemessungsgrundlage

| SV Input | Source | Rule |
|-----------|--------|------|
| Gewinn aus selbständiger Arbeit/Gewerbebetrieb | EÜR Zeile 90 | GKV Beitragsbemessungsgrundlage for Einkommensanpassung |
| Current year KV/PV premiums paid | Beitragsbescheinigung / bank statement | Enter Anlage Vorsorgeaufwand as Sonderausgaben |

**If mismatch:** Verify the Gewinn figure. GKV adjusts Beiträge retroactively based on Steuerbescheid -- this is informational for the client, not a filing error.

### Cross-check 3: GewSt Anrechnung reduces ESt (§35 EStG)

| GewSt Output | ESt Input | Rule |
|-------------|-----------|------|
| Steuermessbetrag (3.5% of Gewerbeertrag above Freibetrag) | ESt Anrechnung: 4.0x Steuermessbetrag | Capped at actual GewSt paid AND at ESt on gewerbliche Einkünfte |
| GewSt payable (Steuermessbetrag x Hebesatz) | Not directly in ESt, but cap for §35 credit | If Hebesatz > 400%, excess GewSt is non-creditable cost |

**If Freiberufler:** This cross-check does not apply. Skip.

**If mismatch:** Common cause is Hebesatz rounding or Hinzurechnungen/Kürzungen affecting the Gewerbeertrag differently from the EÜR Gewinn.

### Cross-check 4: Vorauszahlungen based on prior-year ESt

| Vorauszahlung Input | Source | Rule |
|--------------------|--------|------|
| Prior year festgesetzte ESt | Prior year Steuerbescheid | Drives Vorauszahlungsbescheid amounts |
| Payments made during 2025 | Bank statement / Finanzamt receipts | Must reconcile to ESt-Erklärung Vorauszahlungen line |
| 2026 schedule | Current year festgesetzte ESt (after all credits) | Drives next year's quarterly amounts |

**If mismatch:** Common cause is Finanzamt adjusting Vorauszahlungen mid-year via amended Vorauszahlungsbescheid, or first year of self-employment (no Vorauszahlungen in prior year).

### Cross-check 5: EÜR Vorsteuer consistency with UStVA

| Item | VAT Treatment | EÜR Treatment |
|------|--------------|---------------|
| Reclaimable Vorsteuer (Regelbesteuerung) | Claimed in UStVA | NOT a Betriebsausgabe (netto amount only in EÜR) |
| Blocked Vorsteuer (Regelbesteuerung, e.g., §15 Abs. 1a UStG) | Not claimed | IS a Betriebsausgabe (added to cost in EÜR) |
| All USt paid (Kleinunternehmer) | No recovery | IS a Betriebsausgabe (gross amount is cost in EÜR) |
| USt on Eigenverbrauch (private Kfz-Nutzung) | Output USt in UStVA | Corresponding private use is Entnahme in EÜR |

**If inconsistency:** An expense claimed netto in the EÜR while also not claimed in the UStVA means the Vorsteuer is lost. Flag for reviewer.

---

## Section 4 -- Final reviewer package contents

### Documents

1. **Executive summary** -- one-page overview: filing status, income, tax liability, USt position, Sozialversicherung, Vorauszahlungen, Nachzahlung/Erstattung
2. **UStVA / Umsatzsteuererklärung worksheet** -- line-by-line with formulas
3. **EÜR worksheet** -- Zeile 11 through Zeile 90 with formulas and supporting schedules
4. **ESt computation** -- zu versteuerndes Einkommen, Grundtabelle/Splittingtabelle, SolZ, KiSt
5. **AfA schedule (Anlageverzeichnis)** -- asset register with Anschaffungskosten, Datum, Nutzungsdauer, jährliche AfA, Restwert
6. **Sozialversicherung reconciliation** -- KV/PV/RV amounts, Basisabsicherung for Sonderausgaben
7. **Gewerbesteuer computation** (if Gewerbetreibender) -- Gewerbeertrag, Steuermessbetrag, GewSt, §35 Anrechnung
8. **Vorauszahlungen schedule** -- 2026 quarterly instalment calculation
9. **Cross-skill reconciliation summary** -- all five cross-checks with pass/fail and notes
10. **Reviewer brief** -- comprehensive narrative with positions, citations, flags, self-check results
11. **Client action list** -- what the client needs to do, with dates and amounts

### Reviewer brief contents

```markdown
# Complete Return Package: [Client Name] -- Tax Year 2025

## Executive Summary
- Filing status: [Single / Married (Zusammenveranlagung/Einzelveranlagung) / Single parent]
- Residence: Germany (full-year, unbeschränkt steuerpflichtig)
- Business: Freiberufler (§18 EStG) / Gewerbetreibender (§15 EStG), Einzelunternehmer
- VAT status: Regelbesteuerung / Kleinunternehmer §19 UStG
- Bundesland: [Bundesland]
- UStVA position: EUR X Nachzahlung / EUR X Erstattung
- EÜR Gewinn (Zeile 90): EUR X
- Zu versteuerndes Einkommen: EUR X
- Festzusetzende ESt: EUR X
- Solidaritätszuschlag: EUR X
- Kirchensteuer: EUR X
- Gewerbesteuer (if applicable): EUR X
- §35 Anrechnung (if applicable): EUR X
- Vorauszahlungen geleistet: EUR X
- ESt Nachzahlung / Erstattung: EUR X
- 2026 Vorauszahlungen total: EUR X

## Umsatzsteuer (VAT)
[Content from germany-vat-return output]
- Registration type and filing period (monatlich/vierteljährlich)
- Ausgangs-USt summary (19%, 7%, steuerfrei, innergemeinschaftlich, Drittland)
- Vorsteuer summary (abziehbar, nicht abziehbar, Eigenverbrauch)
- Sondervorauszahlung reconciliation (if Dauerfristverlängerung)
- UStVA line summary
- Umsatzsteuererklärung annual reconciliation

## Einkommensteuer (ESt + EÜR)
[Content from de-income-tax output]
- EÜR Zeile 11: Betriebseinnahmen breakdown by client
- EÜR Zeile 12-85: Betriebsausgaben schedule
- EÜR Zeile 90: Gewinn
- Anlage S (Freiberufler) or Anlage G (Gewerbetreibender)
- Anlage Vorsorgeaufwand: KV/PV Basisabsicherung, Altersvorsorge
- AfA-Tabelle: asset register with depreciation schedule
- Sonderausgaben: Vorsorgeaufwendungen, Kirchensteuer, Spenden
- Zu versteuerndes Einkommen computation
- ESt nach Grundtabelle/Splittingtabelle
- SolZ (5.5% of ESt, Freigrenze EUR 18,130 / EUR 36,260 Splitting)
- KiSt (8% or 9% of ESt)

## Sozialversicherung
[Content from de-social-contributions output]
- GKV or PKV status
- Annual KV premium and Basisabsicherung amount
- Annual PV premium
- RV (if applicable -- freiwillig or KSK)
- Beitragsbemessungsgrundlage for GKV Einkommensanpassung
- Sonderausgaben entry amounts for Anlage Vorsorgeaufwand

## Gewerbesteuer (if Gewerbetreibender)
[Content from de-trade-tax output, or computed if stub]
- Gewinn aus Gewerbebetrieb (from EÜR)
- Hinzurechnungen §8 GewStG (if any)
- Kürzungen §9 GewStG (if any)
- Gewerbeertrag
- Freibetrag EUR 24,500
- Steuermessbetrag (3.5%)
- Hebesatz ([municipality] -- [rate]%)
- GewSt payable
- §35 EStG Anrechnung (4.0x Steuermessbetrag, capped)
- Net GewSt burden after Anrechnung

## Vorauszahlungen (2026)
[Content from de-estimated-tax output, or computed if stub]
- Based on 2025 festgesetzte ESt (after Anrechnungen)
- Q1: 10 March 2026 -- EUR X (ESt) + EUR X (SolZ) + EUR X (KiSt)
- Q2: 10 June 2026 -- EUR X (ESt) + EUR X (SolZ) + EUR X (KiSt)
- Q3: 10 September 2026 -- EUR X (ESt) + EUR X (SolZ) + EUR X (KiSt)
- Q4: 10 December 2026 -- EUR X (ESt) + EUR X (SolZ) + EUR X (KiSt)
- Total 2026 Vorauszahlungen: EUR X

## Cross-skill Reconciliation
- UStVA Umsatz vs EÜR Betriebseinnahmen: [pass/fail]
- ESt Gewinn vs SV Beitragsbemessungsgrundlage: [pass/fail]
- GewSt Anrechnung vs ESt (§35): [pass/fail] (or N/A if Freiberufler)
- Vorauszahlungen vs prior year ESt: [pass/fail]
- EÜR Vorsteuer vs UStVA Vorsteuer: [pass/fail]

## Reviewer Attention Flags
[Aggregated from all upstream skills]
- T2 items requiring Steuerberater confirmation
- Mixed-use expense percentages (Kfz, Telefon, Internet)
- Arbeitszimmer / Tagespauschale claim
- AfA classification (GWG vs reguläre AfA vs Sonderabschreibung §7g)
- Bewirtungskosten 70% limit applied correctly
- Geschenke EUR 50 limit per recipient per year
- Kleinunternehmer threshold monitoring (approaching EUR 22,000)
- Gewerbesteuer Freibetrag and Anrechnung computation
- Any income approaching Progressionsstufen boundaries

## Positions Taken
[List with legislation citations]
- e.g., "Arbeitszimmer Tagespauschale claimed at EUR 1,260 (210 days x EUR 6) -- §4 Abs. 5 Satz 1 Nr. 6c EStG"
- e.g., "Kfz 1%-Regelung applied, Bruttolistenpreis EUR 35,000, private use addition EUR 4,200/year -- §6 Abs. 1 Nr. 4 Satz 2 EStG"
- e.g., "MacBook Pro capitalised, AfA over 3 years per AfA-Tabelle Gruppe 6.14.3 -- §7 Abs. 1 EStG"
- e.g., "GewSt Anrechnung §35 EStG: 4.0x Steuermessbetrag = EUR X, capped at actual GewSt EUR X"
- e.g., "KV Basisabsicherung EUR X als Sonderausgaben -- §10 Abs. 1 Nr. 3 Buchst. a EStG"

## Planning Notes for 2026
- Vorauszahlungen schedule (four quarterly amounts and dates)
- GKV Beitrag adjustment based on 2025 Steuerbescheid
- Kleinunternehmer threshold monitoring (if approaching EUR 22,000)
- AfA continuing into 2026 (Restwert schedule)
- Any legislative changes affecting 2026 (Wachstumschancengesetz, rate changes)
- GewSt Vorauszahlungen (if Gewerbetreibender)

## Client Action List

### Immediate (before 31 July 2026 -- ESt filing deadline without Steuerberater):
1. Review this return package with your Steuerberater
2. File ESt-Erklärung via ELSTER
3. Pay ESt Nachzahlung of EUR X to Finanzamt
4. File Umsatzsteuererklärung 2025 via ELSTER
5. File Gewerbesteuererklärung 2025 via ELSTER (if Gewerbetreibender)

### If filing via Steuerberater (extended deadline -- end of February 2027):
1. Provide this package to your Steuerberater
2. Steuerberater files via ELSTER by end of February 2027

### Quarterly 2026 -- Vorauszahlungen:
1. 10 March 2026: EUR X (ESt + SolZ + KiSt)
2. 10 June 2026: EUR X (ESt + SolZ + KiSt)
3. 10 September 2026: EUR X (ESt + SolZ + KiSt)
4. 10 December 2026: EUR X (ESt + SolZ + KiSt)

### UStVA filing calendar (if Regelbesteuerung):
- Monthly or quarterly UStVA via ELSTER (10th of month following period, or with Dauerfristverlängerung: 10th of second month)
- Umsatzsteuererklärung 2026: due with ESt filing

### GewSt Vorauszahlungen (if Gewerbetreibender):
- 15 February 2026, 15 May 2026, 15 August 2026, 15 November 2026

### Ongoing:
1. Issue §14 UStG-compliant invoices for all sales
2. Retain all Belege (6-year retention for Geschäftsunterlagen, 10-year for Buchungsbelege)
3. Maintain Fahrtenbuch if claiming Kfz expenses via actual cost method
4. Track Anlagevermögen in the AfA schedule
5. Monitor Umsatz for Kleinunternehmer threshold (if applicable)
6. Report Einkommensänderung to Krankenkasse if GKV
```

---

## Section 5 -- Refusals

**R-DE-1 -- Upstream skill did not run.** Name the specific skill. Note: this is a warning, not a hard stop. Continue with available data and flag the gap.

**R-DE-2 -- Upstream self-check failed.** Name the specific check and note it in the reviewer brief. Continue.

**R-DE-3 -- Cross-skill reconciliation failed.** Name the specific reconciliation and describe the discrepancy. Flag for reviewer but continue.

**R-DE-4 -- Intake incomplete.** Specific missing intake items prevent computation. List what is missing and ask the user for the specific data point.

**R-DE-5 -- Out-of-scope item discovered during assembly.** E.g., rental income requiring Anlage V, Kapitalerträge requiring Anlage KAP, foreign source income requiring Anlage AUS. Flag and exclude from computation.

---

## Section 6 -- Self-checks

**Check DE1 -- All upstream skills executed.** germany-vat-return, de-income-tax, de-social-contributions all produced output. de-trade-tax produced output or was skipped (Freiberufler) or was computed from EÜR Gewinn if stub. de-estimated-tax produced output or was computed from festgesetzte ESt.

**Check DE2 -- UStVA Umsatz matches EÜR Betriebseinnahmen.** Within EUR 1 tolerance (netto for Regelbesteuerung, brutto for Kleinunternehmer).

**Check DE3 -- SV uses correct Gewinn figure.** EÜR Gewinn matches the figure used for KV/PV Beitragsbemessungsgrundlage information.

**Check DE4 -- Vorauszahlungen match prior-year ESt.** Quarterly amounts x 4 = prior year festgesetzte ESt (approximately, Finanzamt may round).

**Check DE5 -- Regelbesteuerung USt treatment correct.** Ausgangs-USt excluded from EÜR Betriebseinnahmen (durchlaufender Posten); reclaimable Vorsteuer excluded from Betriebsausgaben; blocked Vorsteuer included in Betriebsausgaben.

**Check DE6 -- Kleinunternehmer treatment correct.** No Ausgangs-USt charged; all Vorsteuer included in Betriebsausgaben (brutto = Aufwand); turnover under EUR 22,000 prior year confirmed.

**Check DE7 -- AfA correctly classified.** Items <= EUR 800 netto as GWG (sofort abgeschrieben); items EUR 250-800 netto as GWG or Pool; items > EUR 800 netto per AfA-Tabelle Nutzungsdauer.

**Check DE8 -- KV/PV Basisabsicherung entered in Anlage Vorsorgeaufwand.** Amount from Beitragsbescheinigung, not total premium.

**Check DE9 -- Grundtabelle or Splittingtabelle correctly applied.** Single = Grundtabelle; married Zusammenveranlagung = Splittingtabelle.

**Check DE10 -- Filing calendar is complete.** All deadlines for UStVA, ESt, GewSt, and Vorauszahlungen are listed with specific dates and amounts.

**Check DE11 -- GewSt Anrechnung correctly computed (if Gewerbetreibender).** 4.0x Steuermessbetrag, capped at actual GewSt and at ESt on gewerbliche Einkünfte. §35 EStG cited.

**Check DE12 -- Reviewer brief contains legislation citations.** Every position taken references the specific paragraph of EStG, UStG, GewStG, or SGB.

**Check DE13 -- SolZ Freigrenze correctly applied.** SolZ = 0 if ESt <= EUR 18,130 (Grundtabelle) or EUR 36,260 (Splittingtabelle). Gleitzone above Freigrenze correctly computed.

**Check DE14 -- Kirchensteuer correctly computed.** 8% (Bayern, Baden-Württemberg) or 9% (all other Bundesländer) of festgesetzte ESt, or EUR 0 if no church membership.

---

## Section 7 -- Output files

The final output is **three files**:

1. **`[client_slug]_2025_germany_master.xlsx`** -- Single master workbook containing every worksheet and form. Sheets include: Cover, UStVA (monthly/quarterly + annual Umsatzsteuererklärung), EÜR (Zeile 11-90), ESt Computation, AfA Schedule (Anlageverzeichnis), Betriebsausgaben Detail, Sozialversicherung, Gewerbesteuer (if applicable), Vorauszahlungen 2026, Cross-Check Summary. Use live formulas where possible -- e.g., EÜR Betriebseinnahmen references the UStVA Umsatz cell; Anlage Vorsorgeaufwand references the SV sheet; §35 Anrechnung references the GewSt sheet. Verify no `#REF!` errors. Verify computed values match the computation model within EUR 1 before shipping.

2. **`reviewer_brief.md`** -- Single markdown file covering all sections from Section 4 above: executive summary, USt, ESt + EÜR, Sozialversicherung, Gewerbesteuer, Vorauszahlungen, cross-skill reconciliation, flags, positions, planning notes.

3. **`client_action_list.md`** -- Single markdown file with step-by-step actions: immediate filings and payments, quarterly calendar for 2026, ongoing compliance reminders.

**If execution runs out of context mid-build:** produce whatever is complete, then state at the end which of the three files were not produced or are partial.

**All files are placed in `/mnt/user-data/outputs/` and presented to the user via the `present_files` tool at the end.**

---

## Section 8 -- Cross-skill references

**Inputs:**
- `de-freelance-intake` -- structured intake package (JSON)
- `germany-vat-return` -- UStVA line values and classification output
- `de-income-tax` -- ESt + EÜR computation output
- `de-social-contributions` -- KV/PV/RV reconciliation output
- `de-trade-tax` -- GewSt computation output (or fallback computation, or N/A if Freiberufler)
- `de-estimated-tax` -- Vorauszahlungen schedule (or fallback computation)

**Outputs:** The final reviewer package. No downstream skill.

---

## Section 9 -- Known gaps

1. PDF form filling is not automated. The reviewer uses the worksheets to fill official forms on ELSTER.
2. E-filing is handled by the reviewer via ELSTER portal, not by this skill.
3. Payment execution is the client's responsibility; the skill only provides instructions and amounts.
4. Zusammenveranlagung (joint filing for married couples) is partially supported -- the skill can compute the Splittingtabelle but does not handle the spouse's separate income in detail. Flag for Steuerberater.
5. Multi-year AfA tracking assumes the prior year schedule is provided. If not, only current-year acquisitions are depreciated.
6. de-trade-tax is a Q4 stub. Until it is fleshed out, Gewerbesteuer is computed using the rules in Section 2 step 4. This is a redundancy, not a gap -- the rules are deterministic (GewStG §§6-11).
7. de-estimated-tax is a Q4 stub. Until it is fleshed out, Vorauszahlungen are computed from festgesetzte ESt. Deterministic per §37 EStG.
8. Foreign source income is out of scope (no DBA / Progressionsvorbehalt computation).
9. Rental income (Anlage V) is out of scope.
10. Kapitalerträge (Anlage KAP) are out of scope -- Abgeltungsteuer normally handles this.
11. Künstlersozialkasse (KSK) membership affects RV -- flagged but detailed KSK computation is not automated.
12. The package is complete only for the 2025 tax year; 2026 appears only as prospective planning.

### Change log
- **v0.1 (April 2026):** Initial draft. Modelled on mt-return-assembly v0.1 adapted for Germany jurisdiction with five content skills (UStVA, ESt+EÜR, SV, GewSt, Vorauszahlungen).

## End of skill


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a Steuerberater, Wirtschaftsprüfer, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
