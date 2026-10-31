---
name: de-return-assembly
description: Final orchestrator skill that assembles the complete German filing package for Germany-resident self-employed individuals (Freiberufler and Gewerbetreibende). Consumes outputs from all Germany content skills (germany-vat-return for UStVA, de-einkommensteuer-freelancer for ESt + EÜR, de-social-contributions for KV/PV/RV, de-trade-tax for GewSt, de-estimated-tax for Vorauszahlungen) to produce a single unified reviewer package containing every worksheet, every form, every brief section, all cross-skill reconciliations, and the final action list with payment instructions, filing instructions, and next-year planning. This is the capstone skill that runs last and produces the final deliverable. MUST be loaded alongside all Germany content skills listed above. Germany full-year residents only. Self-employed individuals and sole proprietors only.
version: 0.2
jurisdiction: DE
tax_year: 2026
last_updated: 2026-10-31
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
drafted_by: OpenAccountants
approved_by: pending
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Assembling a German freelancer's yearly tax return package

This Guide is the last step of the German self-employed workflow. It takes the structured package from `de-freelance-intake`, runs the content Guides in order, reconciles them and assembles one reviewer package for a Steuerberater to check and sign. Figures are for tax year 2026. One source carries another year: the form names of the income tax return come from the ELSTER instructions for the **2025** return, because the 2026 instructions are not published. The Anlage EÜR line numbers are those of the **2026** form, whose instructions are published.

## CRITICAL EXECUTION DIRECTIVE: READ FIRST

**When this Guide is invoked, you have already passed through intake. The user has consented to the full workflow. Execute all steps without pausing for permission.**

- **Do NOT ask "how deep do you want me to go"** or any variant. The user asked for a tax return. Produce it.
- **Do NOT announce how many tokens or tool calls this takes.** Execute.
- **Do NOT ask which deliverables to prioritise.** Produce all of Section 4. If context runs short, finish the numbers, positions and flags first, then the outputs, and state at the end what was not produced.
- **Do NOT re-validate scope that intake validated.** Cross-check numbers, but do not re-interrogate the user about residency or business structure.
- **Do NOT pause between content Guides to check in.** Run them in the order of Section 2.
- **Self-checks are targets, not blockers.** A failed one goes in the brief's open flags and the work continues. Source citations go in the brief, not in intermediate steps.
- **A value marked `unsettled` is never resolved silently.** Carry it into `open_flags` and name it in the brief. Section 8 lists those fields.

**The intake Guide has already told the user that the package requires Steuerberater signoff before filing. State it once and move on.**

**Failure mode to avoid:** the workflow halts and asks a meta-question about pacing. Pick the most defensible path, proceed, and flag the decision.

## What this file is

The capstone Guide for German self-employed returns: every German content Guide feeds into it, and the output is the package a Steuerberater can review, sign and deliver. It sets no rate of its own. The figures below belong to the content Guides and are repeated only so the reconciliation can run.

## Section 1: Scope

- **Scope of package.** Full-year German residents (unbeschränkt steuerpflichtig) self-employed as Freiberufler (§ 18 EStG) or Gewerbetreibende (§ 15 EStG), tax year 2026, profit by cash-basis accounts (§ 4(3) EStG). Covered: advance VAT returns and the yearly Umsatzsteuererklärung; the income tax return with Anlage EÜR, Anlage S or Anlage G, and Anlage Vorsorgeaufwand; the Gewerbesteuererklärung where the client trades; next year's prepayments. https://www.gesetze-im-internet.de/estg/__18.html and https://www.gesetze-im-internet.de/estg/__15.html
- **Out of scope.** `profit_method: bilanz` means double-entry books and an E-Bilanz, not an Anlage EÜR. Route to `germany-bookkeeping` and refuse (R-DE-6).

## Section 2: Execution order and dependency chain

1. **UStVA step.** First, because turnover feeds the Anlage EÜR. Regelbesteuerung: the outstanding advance returns plus the yearly return. Kleinunternehmer: no advance return and no yearly VAT return as a rule, and BOTH limits in the Section 3 table are tested, with the start-up row for a business that started in the year. Exception: a Kleinunternehmer who owes VAT as the recipient of a supply (§ 13b(5) UStG) or on goods bought from other EU states still files for those periods (§ 18(4a) UStG, kept in force by § 19(1) sentence 2 UStG); `de-freelance-intake` has the detail. Output: advance return lines, input VAT recovered and blocked, net turnover, Sondervorauszahlung reconciliation. Guide: `germany-vat-return`.
2. **Income tax and EÜR step.** Net turnover goes to the net receipts line of the Anlage EÜR and the VAT actually received to its own receipts line (Cross-check 1). Blocked input VAT is part of the cost of the item. Covers the Anlage EÜR with the Anlage AVEÜR, Anlage S or Anlage G, Anlage Vorsorgeaufwand and depreciation. Output: taxable profit, taxable income, assessed income tax, solidarity surcharge, church tax. Guide: `de-einkommensteuer-freelancer`. Older versions named this step `germany-income-tax`, which is not a Guide.
3. **Health, care and pension step.** Depends on the profit, the main part of the income a statutory fund uses when it sets contributions finally after the assessment. A voluntary member is charged on all income, not on the profit alone: see `de-social-contributions`. Contributions paid in the year go on the Anlage Vorsorgeaufwand as special expenses. Output: the year's amounts, the basic cover amount, any arrears or refund. Guide: `de-social-contributions`.
4. **Trade tax step.** Gewerbetreibender only. Trade income is the profit plus the add-backs of § 8 GewStG less the reductions of § 9 GewStG, then the allowance and base rate in the Section 3 table, then the municipality's multiplier. The credit against income tax is four times the base amount, capped at the trade tax actually payable and at the income tax falling on the trade income; § 35 EStG prints the multiple in words ("das Vierfache"). A Freiberufler pays no trade tax: skip. Guide: `de-trade-tax`. https://www.gesetze-im-internet.de/estg/__35.html
5. **Prepayment step.** The tax office sets prepayments by notice (Vorauszahlungsbescheid); nobody self-assesses them, and no amount is stated until a notice exists. The four due dates are in § 37(1) EStG: 10 March, 10 June, 10 September, 10 December. That paragraph prints no split across the dates, so state none: read each amount from the notice and test it against the minimums in the Section 3 table. Guide: `de-estimated-tax`. https://www.gesetze-im-internet.de/estg/__37.html
6. **Upstream failure handling.** If a content Guide produces no validated output, note it in the brief and continue with the available data.

## Section 3: Cross-Guide reconciliation

Each cross-check compares one Guide's output with another's input. Line numbers are those of the 2026 Anlage EÜR, as the ministry's instructions of 1 September 2026 print them.

**Limits the cross-checks use**

| What | Value | Note | Source |
| --- | --- | --- | --- |
| Source | all figures below | https://www.gesetze-im-internet.de/ustg_1980/__19.html |  |
| Small business: total turnover of the PREVIOUS year not more than (condition 1 of 2, AND) | EUR 25,000 | "im vorangegangenen Kalenderjahr 25 000 Euro nicht überschritten hat" | https://www.gesetze-im-internet.de/ustg_1980/__19.html |
| Small business: total turnover of the CURRENT year not more than. A hard limit in-year: the supply that crosses it is already taxed | EUR 100,000 | "im laufenden Kalenderjahr 100 000 Euro nicht überschreitet" | same |

| What | Value | Note | Source |
| --- | --- | --- | --- |
| Source | all figures below | https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Einkommensteuer/2026-09-01-anlage-EUER-2026.pdf?__blob=publicationFile&v=2 |  |
| Business that STARTS during the year: total turnover of the current year must not exceed | EUR 25,000 | Instructions to Zeile 12: "darf der Gesamtumsatz im laufenden Kj. 25.000 € nicht überschreiten" | https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Einkommensteuer/2026-09-01-anlage-EUER-2026.pdf?__blob=publicationFile&v=2 |

| What | Value | Note | Source |
| --- | --- | --- | --- |
| Source | all figures below | https://www.gesetze-im-internet.de/ustg_1980/__18.html |  |
| Advance returns are monthly if the VAT payable for the previous year was more than this, quarterly otherwise. The test is the VAT, not turnover | EUR 9,000 | § 18(2): "für das vorangegangene Kalenderjahr mehr als 9 000 Euro" | https://www.gesetze-im-internet.de/ustg_1980/__18.html |
| The tax office may release the business from advance returns if that VAT was not more than | EUR 2,000 | § 18(2): "nicht mehr als 2 000 Euro" | same |

| What | Value | Note | Source |
| --- | --- | --- | --- |
| Source | all figures below | https://www.gesetze-im-internet.de/gewstg/__11.html |  |
| Trade tax allowance for a natural person or partnership, per business per year | EUR 24,500 | § 11(1): "um einen Freibetrag in Höhe von 24 500 Euro" | https://www.gesetze-im-internet.de/gewstg/__11.html |
| Base rate on trade income after the allowance. Not the tax rate: the multiplier is applied to the base amount | 3.5% | § 11(2): "Die Steuermesszahl für den Gewerbeertrag beträgt 3,5 Prozent" | same |

The solidarity surcharge has a rate, an exemption limit that differs between single and joint assessment, and a zone just above the limit (§ 3 and § 4 SolzG). Church tax has two possible state rates. All of those amounts live in `de-einkommensteuer-freelancer`: read them there, and never carry over a limit from an older package, because the surcharge limits change most years. https://www.gesetze-im-internet.de/solzg_1995/__3.html and https://www.gesetze-im-internet.de/solzg_1995/__4.html

| What | Value | Note | Source |
| --- | --- | --- | --- |
| Source | all figures below | https://www.gesetze-im-internet.de/estg/__37.html |  |
| Income tax prepayments are set only if they reach this in the year (first of two conditions, AND) | EUR 400 | § 37(5): "mindestens 400 Euro im Kalenderjahr" | https://www.gesetze-im-internet.de/estg/__37.html |
| and this for a single due date | EUR 100 | § 37(5): "mindestens 100 Euro für einen Vorauszahlungszeitpunkt betragen" | same |

Trade tax prepayments have their own dates and their own minimum: see `de-trade-tax`.

### Cross-check 1: UStVA turnover = EÜR Betriebseinnahmen (net of USt)

**Cross-check 1 table**

| VAT output | Entry on the 2026 Anlage EÜR | Rule |
| --- | --- | --- |
| Net turnover at the standard and the reduced rate | Zeile 15, umsatzsteuerpflichtige Betriebseinnahmen | The net amounts agree |
| VAT charged to customers and actually received | Zeile 17, vereinnahmte Umsatzsteuer | Received VAT IS a business receipt in cash-basis accounts |
| VAT refunded or set off by the tax office | Zeile 18 | Watch the ten-day rule (§ 11(1) sentence 2 EStG) |
| Exempt turnover, turnover that is not taxable, zero-rated supplies, supplies where the customer owes the VAT (§ 13b UStG) | Zeile 16 | Kept apart from taxed turnover |
| Kleinunternehmer turnover | Zeile 12 | Gross: a small business enters the gross amount |
| Private car use and other withdrawals in kind | Zeile 20, Zeile 21 | The VAT on a withdrawal sits in Zeile 17 |
| Total business receipts | Zeile 23, carried to Zeile 77 | The starting figure of the profit calculation |

**If mismatch:** flag it. Common causes: cash accounting against invoice accounting (§ 20 UStG), intra-Community supplies, exempt turnover, VAT on private car use.

**Correction to earlier versions.** "VAT collected is NOT a Betriebseinnahme" and "Betriebseinnahmen sit in Zeile 11" are both wrong for the 2026 form: Zeile 11 asks whether land was withdrawn or sold. https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Einkommensteuer/2026-09-01-anlage-EUER-2026.pdf?__blob=publicationFile&v=2

### Cross-check 2: ESt net income feeds Sozialversicherung Beitragsbemessungsgrundlage

**Cross-check 2 table**

| Social insurance input | Source | Rule |
| --- | --- | --- |
| Profit from self-employed work or from the trade | Zeile 98 of the 2026 Anlage EÜR, steuerpflichtiger Gewinn | Part of the base: a statutory fund charges a voluntary member on all income (§ 240 SGB V), see `de-social-contributions` |
| Health and care contributions actually paid in the year | Beitragsbescheinigung or bank statements | Entered on the Anlage Vorsorgeaufwand as special expenses |

**If mismatch:** verify the profit. A fund adjusts contributions backwards once the assessment arrives: information for the client, not a filing error.

### Cross-check 3: GewSt Anrechnung reduces ESt (§35 EStG)

**Cross-check 3 table**

| Trade tax output | Income tax input | Rule |
| --- | --- | --- |
| Base amount: the base rate in the Section 3 table applied to trade income after the allowance | Credit under § 35 EStG: four times the base amount | Capped at the trade tax actually payable AND at the income tax falling on the trade income |
| Trade tax payable (base amount times the multiplier) | Not an entry in the return, but the first cap | Where the multiplier is high, part of the trade tax is a cost no credit removes |
| Base amount notice and trade tax notice | The data go on the Anlage G | Both are base notices for the credit (§ 35(3) EStG) |

**If Freiberufler:** this cross-check does not apply. Skip it.

**If mismatch:** the usual cause is add-backs or reductions moving trade income away from the profit. State no break-even multiplier and no combined rate: no official page prints one, and the two caps make any general figure wrong.

### Cross-check 4: Vorauszahlungen based on prior-year ESt

**Cross-check 4 table**

| Prepayment input | Source | Rule |
| --- | --- | --- |
| Income tax assessed for the previous year | The previous year's Steuerbescheid | Drives the amounts in the prepayment notice |
| Payments made during the tax year | Bank statements, tax office receipts | Must reconcile to the prepayments credited in the return |
| Schedule for 2027 | Income tax assessed for 2026, after credits | Drives next year's four dated amounts, once a notice sets them |

**If mismatch:** usually an amended notice during the year, or a first year of self-employment with no prepayments. Test against the minimums in the Section 3 table before expecting a notice.

### Cross-check 5: EÜR Vorsteuer consistency with UStVA

**Cross-check 5 table**

| Item | VAT treatment | Entry on the 2026 Anlage EÜR |
| --- | --- | --- |
| Input VAT paid and deductible (§ 15 UStG) | Claimed in the advance return | Zeile 58: it IS a business expense when paid |
| VAT paid over to the tax office | Settles the advance return | Zeile 59, subject to the ten-day rule |
| Blocked input VAT, for example § 15(1a) UStG | Not claimed | Not in Zeile 58: entered gross in that item's expense line. Where the expense itself is not deductible, its VAT is not either (§ 12 no. 3 EStG) |
| All VAT paid by a Kleinunternehmer | No recovery | The gross amount is the expense |
| VAT on private car use | Output VAT in the advance return | The VAT sits in Zeile 17, the private use in Zeile 20 |

**If inconsistency:** an expense entered net while the input VAT was never claimed means the input VAT is lost. Flag it.

## Section 4: Final reviewer package contents

### Documents

1. **Executive summary.** Filing status, income, tax, VAT position, social insurance, prepayments, balance due or refund.
2. **VAT worksheet**, advance returns and the yearly return, line by line with formulas.
3. **EÜR worksheet**, receipts through to the taxable profit on the 2026 line numbers, with schedules.
4. **Income tax computation:** taxable income, basic or splitting table, solidarity surcharge, church tax.
5. **Depreciation schedule (Anlageverzeichnis)** feeding the Anlage AVEÜR: cost, date, useful life, yearly depreciation, written-down value.
6. **Social insurance reconciliation:** health, care and pension amounts, and the basic cover amount.
7. **Trade tax computation** (Gewerbetreibender only): trade income, base amount, trade tax, credit.
8. **Prepayment schedule:** the four dated 2027 amounts, once a notice sets them.
9. **Cross-check summary:** the five cross-checks with pass or fail and notes.
10. **Reviewer brief:** narrative with positions, citations, flags, self-check results.
11. **Client action list:** what the client must do, dated, with amounts.

**Limits the reviewer brief refers to**

| What | Value | Note | Source |
| --- | --- | --- | --- |
| Source | all figures below | https://www.gesetze-im-internet.de/estg/__6.html |  |
| Low-value asset written off in full in the year of purchase: cost per asset, less any input VAT contained in it | EUR 800 | § 6(2): "für das einzelne Wirtschaftsgut 800 Euro nicht übersteigen" | https://www.gesetze-im-internet.de/estg/__6.html |
| An asset written off at once goes in a running register if its value is above this; the same amount is the pool floor | EUR 250 | § 6(2) sentence 4: "deren Wert 250 Euro übersteigt"; § 6(2a) | same |
| Pool method (Sammelposten): upper cost bound per asset. The pool binds every qualifying asset of the year | EUR 1,000 | § 6(2a): "250 Euro, aber nicht 1 000 Euro übersteigen" | same |

The limited deductions of § 4(5) EStG (gifts, entertainment, the home office room, the day rate for working at home) each have their own amount and their own kind of limit. Take the home office room and the day rate from `de-einkommensteuer-freelancer`, and the gift and entertainment limits from `germany-bookkeeping`, and say which limit a position used. https://www.gesetze-im-internet.de/estg/__4.html

### Reviewer brief contents

Amounts in the template are placeholders. Fill each from the computation; never ship a template amount.

~~~markdown
# Complete Return Package: [Client Name], tax year 2026

## Executive Summary
- Filing status: [Single / Married (Zusammenveranlagung/Einzelveranlagung) / Single parent]
- Residence: Germany (full-year, unbeschränkt steuerpflichtig)
- Business: Freiberufler (§18 EStG) / Gewerbetreibender (§15 EStG), Einzelunternehmer
- VAT status: Regelbesteuerung / Kleinunternehmer §19 UStG
- Bundesland: [Bundesland]
- UStVA position: [amount] Nachzahlung / [amount] Erstattung
- EÜR steuerpflichtiger Gewinn (Zeile 98): [amount]
- Zu versteuerndes Einkommen: [amount]
- Festzusetzende ESt: [amount]
- Solidaritätszuschlag: [amount]
- Kirchensteuer: [amount]
- Gewerbesteuer (if applicable): [amount]
- §35 Anrechnung (if applicable): [amount]
- Vorauszahlungen geleistet: [amount]
- ESt Nachzahlung / Erstattung: [amount]
- 2027 Vorauszahlungen total: [amount]

## Umsatzsteuer (VAT)
[Content from germany-vat-return output]
- Registration type and filing period (monatlich/vierteljährlich)
- Ausgangs-USt summary (standard rate, reduced rate, steuerfrei, innergemeinschaftlich, Drittland)
- Vorsteuer summary (abziehbar, nicht abziehbar, Eigenverbrauch)
- Sondervorauszahlung reconciliation (if Dauerfristverlängerung)
- UStVA line summary
- Umsatzsteuererklärung annual reconciliation

## Einkommensteuer (ESt + EÜR)
[Content from de-einkommensteuer-freelancer output]
- Anlage EÜR Zeile 15 and Zeile 17: turnover and VAT received, by client
- Anlage EÜR Zeilen 24 to 76: Betriebsausgaben schedule
- Anlage EÜR Zeile 98: steuerpflichtiger Gewinn
- Anlage S (Freiberufler) or Anlage G (Gewerbetreibender)
- Anlage Vorsorgeaufwand: KV/PV Basisabsicherung, Altersvorsorge
- Anlage AVEÜR: asset register with depreciation schedule
- Sonderausgaben: Vorsorgeaufwendungen, Kirchensteuer, Spenden
- Zu versteuerndes Einkommen computation
- ESt nach Grundtabelle/Splittingtabelle
- SolZ: rate and Freigrenze per de-einkommensteuer-freelancer
- KiSt: state rate per de-einkommensteuer-freelancer

## Sozialversicherung
[Content from de-social-contributions output]
- GKV or PKV status
- Annual KV premium and Basisabsicherung amount
- Annual PV premium
- RV (if applicable: freiwillig or KSK)
- Beitragsbemessungsgrundlage for the GKV income adjustment
- Sonderausgaben entry amounts for Anlage Vorsorgeaufwand

## Gewerbesteuer (if Gewerbetreibender)
[Content from de-trade-tax output]
- Gewinn aus Gewerbebetrieb (from the Anlage EÜR)
- Hinzurechnungen §8 GewStG (if any)
- Kürzungen §9 GewStG (if any)
- Gewerbeertrag
- Freibetrag EUR 24,500
- Steuermessbetrag (3.5%)
- Hebesatz ([municipality], [rate])
- GewSt payable
- §35 EStG Anrechnung (four times the Steuermessbetrag, capped)
- Net GewSt burden after Anrechnung

## Vorauszahlungen (2027)
[Content from de-estimated-tax output]
- Based on the 2026 festgesetzte ESt, as the Vorauszahlungsbescheid sets it
- Q1: 10 March 2027, [amount] (ESt) + [amount] (SolZ) + [amount] (KiSt)
- Q2: 10 June 2027, [amount] (ESt) + [amount] (SolZ) + [amount] (KiSt)
- Q3: 10 September 2027, [amount] (ESt) + [amount] (SolZ) + [amount] (KiSt)
- Q4: 10 December 2027, [amount] (ESt) + [amount] (SolZ) + [amount] (KiSt)
- Total 2027 Vorauszahlungen: [amount]

## Cross-Guide Reconciliation
- UStVA Umsatz vs Anlage EÜR Zeile 15 and Zeile 17: [pass/fail]
- ESt Gewinn vs SV Beitragsbemessungsgrundlage: [pass/fail]
- GewSt Anrechnung vs ESt (§35): [pass/fail] (or N/A if Freiberufler)
- Vorauszahlungen vs prior year ESt: [pass/fail]
- Anlage EÜR Vorsteuer vs UStVA Vorsteuer: [pass/fail]

## Reviewer Attention Flags
[Aggregated from all upstream Guides]
- Every field the intake package marked unsettled
- T2 items requiring Steuerberater confirmation
- Mixed-use expense percentages (Kfz, Telefon, Internet)
- Arbeitszimmer or Tagespauschale claim, and which of the two was used
- AfA classification (GWG, Sammelposten, reguläre AfA, Sonderabschreibung §7g)
- Bewirtungskosten limit applied correctly
- Geschenke limit per recipient per year, a cliff not an allowance
- Kleinunternehmer threshold monitoring (approaching EUR 25,000 or EUR 100,000)
- Gewerbesteuer Freibetrag and Anrechnung computation
- Any income near a change of tariff zone

## Positions Taken
[List with legislation citations]
- e.g., "Tagespauschale claimed for [number] days, total [amount], §4 Abs. 5 Satz 1 Nr. 6c EStG"
- e.g., "Kfz: list-price method, Bruttolistenpreis [amount], private use addition [amount] for the year, §6 Abs. 1 Nr. 4 Satz 2 EStG"
- e.g., "[Asset] capitalised, depreciated over the useful life in the ministry depreciation table, §7 Abs. 1 EStG"
- e.g., "GewSt Anrechnung §35 EStG: four times the Steuermessbetrag = [amount], capped at the GewSt actually payable [amount]"
- e.g., "KV Basisabsicherung [amount] als Sonderausgaben, §10 Abs. 1 Nr. 3 Buchst. a EStG"

## Planning Notes for 2027
- Prepayment schedule (four dated amounts, from the notice)
- GKV Beitrag adjustment once the 2026 Steuerbescheid arrives
- Kleinunternehmer threshold monitoring (if approaching EUR 25,000 or EUR 100,000)
- AfA continuing into 2027 (written-down value schedule)
- Any legislative change affecting 2027
- GewSt Vorauszahlungen (if Gewerbetreibender)

## Client Action List

### Immediate (before the end of July 2027: ESt filing deadline without Steuerberater):
1. Review this return package with your Steuerberater.
2. File the Einkommensteuererklärung through the portal.
3. Pay any income tax balance of [amount] to the Finanzamt.
4. File the Umsatzsteuererklärung for 2026.
5. File the Gewerbesteuererklärung for 2026 (if Gewerbetreibender).

### If filing via Steuerberater (extended deadline: the last day of February 2028):
1. Provide this package to your Steuerberater.
2. The Steuerberater files by the last day of February 2028.

### Quarterly 2027: Vorauszahlungen (amounts from the Vorauszahlungsbescheid):
1. 10 March 2027: [amount] (ESt + SolZ + KiSt)
2. 10 June 2027: [amount] (ESt + SolZ + KiSt)
3. 10 September 2027: [amount] (ESt + SolZ + KiSt)
4. 10 December 2027: [amount] (ESt + SolZ + KiSt)

### UStVA filing calendar (if Regelbesteuerung):
- Monthly or quarterly advance return, by the 10th day after the period, or with Dauerfristverlängerung by the 10th day of the second month
- Umsatzsteuererklärung for 2027: due with the income tax return

### GewSt Vorauszahlungen (if Gewerbetreibender):
- 15 February 2027, 15 May 2027, 15 August 2027, 15 November 2027. 15 May 2027 is a Saturday and 15 August 2027 a Sunday: a date that falls on a Saturday, Sunday or public holiday moves to the next working day (§ 108(3) AO)

### Ongoing:
1. Issue invoices that meet §14 UStG, and receive e-invoices.
2. Keep the records for the periods in §147 AO.
3. Keep a Fahrtenbuch if claiming car costs by actual cost.
4. Track Anlagevermögen in the AfA schedule.
5. Monitor Umsatz against both Kleinunternehmer limits (if applicable).
6. Report an income change to the Krankenkasse if GKV.
~~~

## Section 5: Refusals

- **R-DE-1.** A content Guide did not run. Name it. A warning, not a stop: continue and flag the gap.
- **R-DE-2.** An upstream self-check failed. Name it, note it in the brief, continue.
- **R-DE-3.** A cross-check failed. Name it, describe the difference, flag it, continue.
- **R-DE-4.** Intake incomplete: missing items prevent computation. List them and ask for them.
- **R-DE-5.** An out-of-scope item appears: rental income (Anlage V), investment income (Anlage KAP), crypto disposals, foreign income (Anlage AUS). Flag it, exclude it, route to `de-rental-income`, `de-capital-gains` or `de-crypto-tax`. Foreign income and treaty relief need a Steuerberater.
- **R-DE-6.** The intake package says `profit_method: bilanz`. This Guide assembles cash-basis packages only. Stop and route to `germany-bookkeeping`.
- **R-DE-7.** The client is a company or a partnership: they file their own returns under their own rules. Refer to a Steuerberater.

## Section 6: Self-checks

- **Check DE1.** All content Guides ran: `germany-vat-return`, `de-einkommensteuer-freelancer`, `de-social-contributions`, `de-estimated-tax`; `de-trade-tax` ran or was skipped for a Freiberufler.
- **Check DE2.** VAT turnover agrees with the net receipts line and the VAT received is entered separately. Any difference is explained, not averaged.
- **Check DE3.** The social insurance section uses the taxable profit from Zeile 98.
- **Check DE4.** Prepayments credited match the payments made, and next year's amounts come from a notice, not a division.
- **Check DE5.** Regelbesteuerung: net turnover in Zeile 15, VAT received in Zeile 17, input VAT paid in Zeile 58, VAT paid over in Zeile 59, blocked input VAT inside the item's cost.
- **Check DE6.** Kleinunternehmer: no VAT charged on own sales, gross amounts throughout, receipts in Zeile 12, BOTH limits in the Section 3 table tested (the start-up row if the business started in the year), and any VAT owed as recipient under § 13b UStG declared.
- **Check DE7.** Assets classified against the limits in Section 4: written off at once, in the register, or in the pool, which binds the whole cost band once chosen.
- **Check DE8.** The basic cover part of the health and care contributions is on the Anlage Vorsorgeaufwand, from the certificate, not the total premium.
- **Check DE9.** Single means Grundtabelle, married assessed together means Splittingtabelle.
- **Check DE10.** The calendar is complete: advance returns, income tax, trade tax, prepayments, each dated.
- **Check DE11.** The credit is four times the base amount, capped at the trade tax payable and at the income tax on the trade income, with § 35 EStG cited.
- **Check DE12.** Every position cites a paragraph of EStG, UStG, GewStG, AO or SGB.
- **Check DE13, solidarity surcharge limit.** Nil unless the income tax the surcharge is measured on (§ 3(2) SolzG: worked out with the child allowances in every case) passes the limit for the assessment type, with the zone just above it applied. Limits from `de-einkommensteuer-freelancer`.
- **Check DE14, church tax rate.** The rate in `taxpayer.kirchensteuer_rate`, read from the client's Steuerbescheid, or nil for a non-member. A `null` rate is flagged, not guessed.
- **Check DE15, unsettled values.** Every field marked `unsettled` appears in the brief, none resolved silently.

## Section 7: Output files

The final output is **three files**:

1. **`[client_slug]_2026_germany_master.xlsx`.** One workbook. Sheets: Cover, UStVA (periods plus the yearly return), EÜR on the 2026 line numbers, income tax computation, asset register for the Anlage AVEÜR, expense detail, social insurance, trade tax where it applies, prepayments for 2027, cross-check summary. Use live formulas: the receipts line references the VAT sheet, the Anlage Vorsorgeaufwand the social insurance sheet, the § 35 credit the trade tax sheet. Verify no `#REF!` errors before shipping.
2. **`reviewer_brief.md`.** Every part of Section 4: executive summary, VAT, income tax and EÜR, social insurance, trade tax, prepayments, cross-check results, flags, positions, planning notes.
3. **`client_action_list.md`.** Filings and payments due now, the 2027 calendar, ongoing duties.

**If execution runs out of context mid-build:** produce what is complete, then state which files are missing or partial.

**All files go to `/mnt/user-data/outputs/` and are presented with the `present_files` tool at the end.**

## Section 8: Cross-Guide references

**Inputs:** `de-freelance-intake` (the structured package, JSON); `germany-vat-return`; `de-einkommensteuer-freelancer` (older versions named this `germany-income-tax`, which is not a Guide); `de-social-contributions`; `de-trade-tax`; `de-estimated-tax`; `germany-bookkeeping`.

**Outputs:** the final reviewer package. No downstream Guide.

**Fields this Guide reads from the intake package.** Use these names exactly: they are what `de-freelance-intake` writes.

- `tax_year`: must be 2026 here.
- `taxpayer.business_type`: `freiberufler`, `gewerbetreibender`, `unsettled`. Chooses Anlage S or Anlage G and whether step 4 runs. `unsettled` means the trade question is open: run the income tax step, do not decide it, flag it.
- `taxpayer.profit_method`: `euer`, `bilanz`. `bilanz` triggers R-DE-6.
- `taxpayer.vat_status`: `regelbesteuerung`, `kleinunternehmer`, `unsettled`. Chooses the rows used in Cross-checks 1 and 5 and the receipts line. `unsettled` means intake could not settle it: test both turnover fields against the Section 3 limits, say in the brief which status the worksheets assume and why, and flag it.
- `taxpayer.kirchensteuer`, `taxpayer.kirchensteuer_rate`: membership and the rate. The rate stays `null` until it is read from the client's Steuerbescheid: never fill it from memory of the federal state. While it is `null`, church tax is an open flag.
- `vat.gesamtumsatz_prior_year`, `vat.gesamtumsatz_current_year`: tested against both small-business limits. `null` means not yet known, never zero: a `null` field leaves the test open, so flag it and do not confirm Kleinunternehmer status.
- `vat.ustva_period`: `monthly`, `quarterly`, `released`, `none`. Must agree with the VAT tests in the Section 3 table. A mismatch is a flag, not a silent fix.
- `vat.kleinunternehmer_waived`, `vat.dauerfristverlaengerung`, `vat.sondervorauszahlung`, `vat.vorsteuer_reclaimable`: the VAT worksheet and its reconciliation.
- `sozialversicherung.rentenversicherung.type`: `none`, `freiwillig`, `pflicht_ksk`, `pflicht_other`, `unsettled`.
- `home_office.type`: `mittelpunkt`, `tagespauschale`, `unsettled`, `none`. Chooses which home-office claim in `de-einkommensteuer-freelancer` applies, never two for one day.
- `private_use.kfz_method`: `fahrtenbuch`, `1pct_regelung`, `cost_share`, `km_pauschale`, `none`. `cost_share` is a car at or below the business share that opens the list-price method: intake flags it T2, so carry the flag.
- `gewerbesteuer.applies` (`true`, `false`, or `null` while unknown), `gewerbesteuer.hebesatz`, `gewerbesteuer.municipality`: step 4 and Cross-check 3. `null` is not `false`: do not skip step 4 silently, flag it.
- `prior_year.festgesetzte_est`, `prior_year.gewinn`, `prior_year.afa_schedule`, `vorauszahlungen.*`: Cross-check 4 and the depreciation schedule.
- `open_flags`, `refusals_triggered`, `documents_received`: into the brief unchanged.

## Section 9: Known gaps

1. Filling the PDF forms is not automated. The reviewer uses the worksheets to fill the forms in the portal.
2. Filing is done by the reviewer. Electronic filing is a duty for business income under § 25(4) EStG, for VAT under § 18(3) UStG and for trade tax under § 14a GewStG; the tax office can waive it in hardship. https://www.gesetze-im-internet.de/estg/__25.html and https://www.gesetze-im-internet.de/gewstg/__14a.html
3. Paying is the client's job. This Guide gives instructions and amounts only.
4. Joint assessment is partly supported: the splitting table can be applied, but the spouse's own income is not worked through.
5. Multi-year depreciation assumes the previous year's schedule is supplied. Without it, only the year's purchases are depreciated.
6. Trade tax is computed by `de-trade-tax`. The earlier note that it was a stub no longer holds: reconcile it in Cross-check 3, do not recompute it here.
7. Prepayments are computed by `de-estimated-tax`. That stub note no longer holds either, and it does not divide a yearly figure by four.
8. Foreign income is out of scope: no treaty relief, no exemption with progression.
9. Rental income (Anlage V): `de-rental-income`. Investment income (Anlage KAP): `de-capital-gains`. Crypto disposals: `de-crypto-tax`.
10. Membership of the artists' social fund changes the pension position. It is flagged, not computed.
11. The Anlage EÜR line numbers are the 2026 ones; the form names of the income tax return come from the instructions for the 2025 return. Check each line number against the live form before filing.

### Change log

- **v0.2 (September 2026):** refreshed for tax year 2026. Routing corrected to `de-einkommensteuer-freelancer`. Anlage EÜR line numbers corrected to the 2026 form. VAT treatment in cash-basis accounts corrected. Figures brought to 2026. Sample amounts replaced with placeholders.
- **v0.1 (April 2026):** initial draft, modelled on the Malta return assembly Guide and adapted for Germany.

## The method, step by step

1. **Read the intake package and stop if it is out of scope.** Check `taxpayer.profit_method`, the entity and the residence. Cash-basis accounts under § 4(3) EStG are the scope; books and an E-Bilanz are not. https://www.gesetze-im-internet.de/estg/__4.html
2. **Run the VAT step and fix the turnover.** Settle the open advance returns and the yearly return, and set the rhythm from the previous year's VAT against the limits in the Section 3 table. For a small business, test both limits of § 19 UStG. https://www.gesetze-im-internet.de/ustg_1980/__18.html
3. **Run the income tax step and build the Anlage EÜR.** Receipts in Zeilen 12 to 22 with the total in Zeile 23, expenses in Zeilen 24 to 76, profit in Zeilen 77 to 98. Send the Anlage AVEÜR with it: the instructions call it a necessary part of the accounts. The same holds for the Anlage SZ of a sole trader once loan interest, other than interest on loans for fixed assets, passes the amount those instructions print: flag it. https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Einkommensteuer/2026-09-01-anlage-EUER-2026.pdf?__blob=publicationFile&v=2
4. **Run social insurance, then trade tax for a Gewerbetreibender, then prepayments.** Take the allowance and base rate from the Section 3 table (§ 11 GewStG) and the credit from § 35 EStG. https://www.gesetze-im-internet.de/gewstg/__11.html
5. **Run the five cross-checks in Section 3, then the self-checks in Section 6.** A failed check is written into the brief; it does not stop the build.
6. **Assemble the three files and set the calendar.** For the 2026 return the deadline is seven months after the end of the calendar year, so the end of July 2027; 31 July 2027 is a Saturday, and a period ending on a Saturday, Sunday or public holiday ends on the next working day. Filed by a tax adviser: the last day of February 2028. The longer pandemic periods ended with tax year 2024. https://www.gesetze-im-internet.de/ao_1977/__149.html and https://www.gesetze-im-internet.de/ao_1977/__108.html and https://www.gesetze-im-internet.de/aoeg_1977/art_97__36.html

## Ask the client first

- **Is a Steuerberater filing this, or are you?** It moves the deadline from the end of July 2027 to the last day of February 2028 and changes the action list.
- **Freiberufler or Gewerbetreibender, and is a trade registration in place?** It decides Anlage S against Anlage G and whether trade tax and the credit apply, and it is the commonest open question in the intake package.
- **Which municipality, and what is its multiplier?** Without it neither the trade tax nor the credit cap can be finished.
- **Are you in a church that levies church tax, and in which federal state?** The state sets the rate.
- **Did any income arrive that is not from the business?** Rent, investments, crypto disposals and foreign income each need their own form and Guide (R-DE-5).
- **Has a Vorauszahlungsbescheid arrived for 2027?** Without one there is no prepayment amount to state.

## When to refuse or refer

- A company or a partnership of any kind, including a one-person company, and any client who keeps double-entry books, or must keep them, and files an E-Bilanz.
- Part-year residence, a move in or out of Germany during the year, or income taxed in another country.
- A permanent establishment abroad, or a second business not in the package.
- An open dispute: an objection, an appeal, an audit, or a voluntary disclosure.
- Any request to file, sign or transmit. This Guide prepares a package for a Steuerberater to check and sign. It does not file.

```oa-check
name: DE sole trader 2026, base amount after the allowance
inputs:
  trade_income: 30000
steps:
  - base: (trade_income - 24500) * 0.035
expected:
  base: 192.50
```

```oa-check
name: DE sole trader 2026, trade tax at multiplier 410%
inputs:
  trade_income: 40000
  hebesatz: 4.1
steps:
  - base: (trade_income - 24500) * 0.035
  - trade_tax: base * hebesatz
expected:
  trade_tax: 2224.25
```

## Sources

- https://www.gesetze-im-internet.de/estg/__4.html , https://www.gesetze-im-internet.de/estg/__6.html , https://www.gesetze-im-internet.de/estg/__15.html , https://www.gesetze-im-internet.de/estg/__18.html , https://www.gesetze-im-internet.de/estg/__25.html , https://www.gesetze-im-internet.de/estg/__35.html , https://www.gesetze-im-internet.de/estg/__37.html (read 2026-10-31)
- https://www.gesetze-im-internet.de/ustg_1980/__18.html , https://www.gesetze-im-internet.de/ustg_1980/__19.html (read 2026-10-31)
- https://www.gesetze-im-internet.de/gewstg/__11.html , https://www.gesetze-im-internet.de/gewstg/__14a.html (read 2026-10-31)
- https://www.gesetze-im-internet.de/solzg_1995/__3.html , https://www.gesetze-im-internet.de/solzg_1995/__4.html (read 2026-10-31)
- https://www.gesetze-im-internet.de/ao_1977/__108.html , https://www.gesetze-im-internet.de/ao_1977/__149.html , https://www.gesetze-im-internet.de/aoeg_1977/art_97__36.html (read 2026-10-31)
- https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Einkommensteuer/2026-09-01-anlage-EUER-2026.pdf?__blob=publicationFile&v=2
- https://www.elster.de/eportal/helpGlobal?themaGlobal=help_est_ufa_10_2025 (read 2026-10-31)

## End of Guide

## Disclaimer

This Guide and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this Guide. All outputs must be reviewed and signed off by a qualified professional (such as a Steuerberater, Wirtschaftsprüfer, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

> Contributed by OpenAccountants.

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
