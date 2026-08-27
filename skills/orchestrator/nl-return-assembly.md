---
name: nl-return-assembly
description: Final orchestrator skill that assembles the complete Netherlands filing package for Netherlands-resident self-employed individuals and sole proprietors (ZZP/eenmanszaak). Consumes outputs from all Netherlands content skills (nl-btw-return for BTW-aangifte, nl-income-tax for aangifte inkomstenbelasting Box 1/2/3, nl-zvw for zorgverzekeringswet bijdrage) to produce a single unified reviewer package containing every worksheet, every form, every brief section, all cross-skill reconciliations, and the final action list with payment instructions, filing instructions, and next-year planning. This is the capstone skill that runs last and produces the final deliverable. MUST be loaded alongside all Netherlands content skills listed above. Netherlands full-year residents only. Self-employed individuals and sole proprietors only.
version: 1.0
jurisdiction: NL
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
category: orchestrator
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# NL Return Assembly

## Netherlands Return Assembly Skill v1.0

## CRITICAL EXECUTION DIRECTIVE -- READ FIRST

When this skill is invoked, you have already passed through intake. The user has consented to the full workflow. Execute all steps without pausing for permission.

Specifically:

- Do NOT ask the user "how deep do you want me to go" or "do you want the full package" or any variant. The user asked for their tax returns. They want their tax returns. Produce them.
- Do NOT announce how many tokens or tool calls this will take. Execute.
- Do NOT ask which deliverables to prioritise. Produce all deliverables listed in Section 4. If you run out of context mid-execution, finish the computation work first (numbers, positions, flags) then produce whatever formatted outputs you can, and at the very end state clearly which deliverables were not produced and why.
- Do NOT re-validate scope that intake already validated. If `nl-freelance-intake` produced an intake package, trust it. You can cross-check specific numbers during reconciliation but do not re-interrogate the user about residency, business structure, or anything else intake already captured.
- Do NOT pause between content skills to check in. Run them in dependency order (Section 2) without prose status updates between each one. A single status message at the end is fine.
- Self-checks are targets, not blockers. If a self-check fails, note it in the reviewer brief's open flags section and continue. Do NOT halt the entire workflow because one self-check had an ambiguous answer.
- Primary source citations go in the final reviewer brief, not in intermediate computation steps.

The user has already been told (by the intake skill) that the final package requires belastingadviseur signoff before filing. State it once in the final output and move on.

Failure mode to avoid: The skill halts mid-execution and asks the user a meta-question about workflow pacing. If you feel the urge to ask "how should I proceed," the correct action is to pick the most defensible path and proceed, flagging the decision in the reviewer brief so the reviewer can challenge it.

## What this file is

The final capstone skill for Netherlands self-employed returns. Every Netherlands content skill feeds into this one. The output is the complete reviewer package that a belastingadviseur can review, sign off on, and deliver to the client along with filing instructions.

This skill coordinates execution of the content skills, verifies cross-skill consistency, and assembles the final deliverable.

## Section 1 -- Scope

Produces the complete Netherlands filing package for:
- Full-year Netherlands residents
- Self-employed individuals and sole proprietors (ZZP/eenmanszaak)
- Tax year 2025
- Filing BTW-aangifte (quarterly/monthly or KOR annual), aangifte inkomstenbelasting (IB -- Box 1, Box 2 if applicable, Box 3), ZVW bijdrage reconciliation, voorlopige aanslag 2026 recommendation

## Section 2 -- Execution order and dependency chain

0. **BTW-aangifte** — BTW-aangifte (quarterly/monthly for regular registration, annual KOR declaration). Runs first because BTW turnover figures feed into the IB-aangifte. For regular BTW: prepare Q4 2025 BTW-aangifte if not yet filed; verify Q1-Q3 figures; check ICP opgave completeness. For KOR: verify turnover remains under EUR 20,000; prepare annual KOR declaration if required. Output: BTW-aangifte box values (rubrieken 1a through 5e), voorbelasting recovered/blocked, omzet (ex-BTW), ICP opgave data.
0. **Aangifte inkomstenbelasting** — Depends on BTW output: omzet (rubriek 1a) must use ex-BTW turnover for regular BTW clients. Depends on BTW output: blocked voorbelasting becomes a deductible bedrijfskost. Computes winst uit onderneming, ondernemersaftrek (zelfstandigenaftrek + startersaftrek), MKB-winstvrijstelling. Computes eigen woning (eigenwoningforfait minus hypotheekrenteaftrek) in Box 1. Computes Box 3 vermogensrendementsheffing. Applies heffingskortingen (algemene heffingskorting, arbeidskorting). Output: IB-aangifte values, belastbaar inkomen per box, verschuldigde inkomstenbelasting, heffingskortingen, te betalen/terug te ontvangen.
0. **Zorgverzekeringswet bijdrage** — Depends on IB: bijdrage-inkomen is based on Box 1 inkomen (winst uit onderneming + employment income). ZVW bijdrage for self-employed: 5.32% of bijdrage-inkomen up to EUR 71,628 (2025 maximum bijdrage-inkomen). Output: annual ZVW bijdrage, voorlopige aanslag ZVW paid, shortfall/overpayment.
0. **Voorlopige aanslag 2026 recommendation (forward-looking)** — Based on 2025 final IB + ZVW liability. Recommendation to request/adjust voorlopige aanslag via MijnBelastingdienst. Output: recommended voorlopige aanslag amounts for IB and ZVW. If any upstream content skill fails to produce validated output, the assembly skill notes the failure in the reviewer brief and continues with available data rather than halting entirely.

## Section 3 -- Cross-skill reconciliation

### Cross-check 1: BTW omzet matches IB winst uit onderneming gross income

**Cross-check 1: BTW omzet matches IB winst uit onderneming gross income**  _(Section 3)_

| BTW Output | IB Input | Rule |
| --- | --- | --- |
| BTW-aangifte rubriek 1a (leveringen/diensten belast met hoog tarief) + 1b (laag tarief) + 1e (leveringen/diensten belast met 0% of niet bij u belast) | IB omzet (gross receipts for winst uit onderneming) | Must match within EUR 1 |
| Regular BTW: sum of rubrieken 1a + 1b + 1c + 1d + 1e | IB omzet | Turnover is ex-BTW |
| KOR: declared turnover on annual declaration | IB omzet | Turnover is gross (no BTW separation) |

- **If mismatch** — Flag for reviewer. Common causes: timing differences (factuurstelsel vs kasstelsel), ICP diensten (rubriek 3b) not appearing in rubriek 1a, bad debt write-offs, foreign income not subject to Dutch BTW.  _(Section 3)_

### Cross-check 2: ZVW bijdrage-inkomen matches IB Box 1 income

**Cross-check 2: ZVW bijdrage-inkomen matches IB Box 1 income**  _(Section 3)_

| ZVW Input | Source | Rule |
| --- | --- | --- |
| Bijdrage-inkomen | IB Box 1 verzamelinkomen (winst + employment income, before persoonsgebonden aftrek) | ZVW is based on Box 1 income |
| Voorlopige aanslag ZVW paid | Bank statement / Belastingdienst beschikking | Reconcile against final ZVW liability |

- **If mismatch** — Verify the bijdrage-inkomen definition. Note that eigen woning aftrek (negative Box 1 component) reduces bijdrage-inkomen.  _(Section 3)_

### Cross-check 3: Voorlopige aanslag reconciliation

**Cross-check 3: Voorlopige aanslag reconciliation**  _(Section 3)_

| Voorlopige Aanslag | Source | Rule |
| --- | --- | --- |
| Voorlopige aanslag IB 2025 paid | Bank statement / beschikking | Enters IB-aangifte as voorheffing |
| Voorlopige aanslag ZVW 2025 paid | Bank statement / beschikking | Enters ZVW reconciliation |
| Final IB + ZVW liability | Computed by nl-income-tax + nl-zvw | Difference = te betalen or terug te ontvangen |

- **If mismatch** — Common cause is first year of self-employment (no voorlopige aanslag), or Belastingdienst adjusted the voorlopige aanslag mid-year.  _(Section 3)_

### Cross-check 4: BTW voorbelasting and income tax deductions consistency

**Cross-check 4: BTW voorbelasting and income tax deductions consistency**  _(Section 3)_

| Item | BTW Treatment | Income Tax Treatment |
| --- | --- | --- |
| Reclaimable voorbelasting (regular BTW) | Claimed in BTW-aangifte rubriek 5b | NOT a deduction in IB (netto bedrag only) |
| Blocked voorbelasting (regular BTW) | Not claimed | IS a deduction in IB (added to cost) |
| All BTW paid (KOR) | No recovery | IS a deduction in IB (bruto bedrag is cost) |
| Representatiekosten BTW | 100% BTW reclaimable | Only 80% of net cost deductible for IB (Art. 3.15 Wet IB 2001) |
| Privégebruik auto (BUA) | BTW correction via BUA (besluit uitsluiting aftrek) on BTW-aangifte | Separate private-use correction for IB |

- **If inconsistency** — An expense claimed net of BTW on the IB while also not claimed on the BTW-aangifte means the BTW is lost. Flag for reviewer.  _(Section 3)_

### Cross-check 5: Ondernemersaftrek computation chain

**Cross-check 5: Ondernemersaftrek computation chain**  _(Section 3)_

| Step | Computation | Rule |
| --- | --- | --- |
| Winst uit onderneming (before ondernemersaftrek) | Omzet minus bedrijfskosten minus afschrijvingen | Starting point |
| Zelfstandigenaftrek | EUR 2,470 (2025) if urencriterium met | Art. 3.76 Wet IB 2001 |
| Startersaftrek | EUR 2,123 (2025) if eligible | Art. 3.76a Wet IB 2001 |
| Winst after zelfstandigenaftrek | Winst minus zelfstandigenaftrek minus startersaftrek | Intermediate |
| MKB-winstvrijstelling | 13.31% of winst after zelfstandigenaftrek | Art. 3.79a Wet IB 2001 |
| Belastbare winst | Winst after zelfstandigenaftrek minus MKB-winstvrijstelling | To Box 1 |

- **If computation error** — Verify order of operations. MKB-winstvrijstelling applies AFTER zelfstandigenaftrek, not before.  _(Section 3)_

## Section 4 -- Final reviewer package contents

### Documents

1. Executive summary -- one-page overview: filing status, winst uit onderneming, belastbaar inkomen per box, totaal verschuldigde belasting, BTW position, ZVW bijdrage, terug te ontvangen/te betalen
2. BTW-aangifte worksheet -- rubriek-by-rubriek with formulas (Q4 2025 or KOR annual)
3. IB-aangifte worksheet -- Box 1 (winst, eigen woning, employment), Box 2 (if applicable), Box 3 (vermogen), heffingskortingen, verschuldigde belasting
4. Capital allowances schedule (afschrijvingsstaat) -- asset register with aanschafwaarde, datum, afschrijvingspercentage, jaarlijkse afschrijving, boekwaarde
5. ZVW reconciliation -- bijdrage-inkomen, percentage, maximum, voorlopige aanslag paid, shortfall/overpayment
6. Voorlopige aanslag 2026 recommendation -- recommended IB and ZVW amounts
7. Cross-skill reconciliation summary -- all five cross-checks with pass/fail and notes
8. Reviewer brief -- comprehensive narrative with positions, citations, flags, self-check results
9. Client action list -- what the client needs to do, with dates and amounts

### Reviewer brief contents

```markdown
# Complete Return Package: [Client Name] -- Tax Year 2025

## Executive Summary
- Filing status: [Single / Fiscal partner]
- Residence: Netherlands (full-year)
- Business: ZZP / eenmanszaak (KvK [number])
- BTW registration: Regular / KOR
- BTW-aangifte position (Q4 or annual): EUR X te betalen / EUR X terug
- Winst uit onderneming (before aftrekken): EUR X
- Zelfstandigenaftrek: EUR X
- Startersaftrek: EUR X
- MKB-winstvrijstelling: EUR X
- Belastbare winst uit onderneming: EUR X
- Eigen woning aftrek: EUR X
- Belastbaar inkomen Box 1: EUR X
- Belastbaar inkomen Box 3: EUR X
- Verschuldigde inkomstenbelasting: EUR X
- Heffingskortingen: EUR X
- Voorlopige aanslag IB paid: EUR X
- Te betalen / terug te ontvangen IB: EUR X
- ZVW bijdrage: EUR X
- Voorlopige aanslag ZVW paid: EUR X
- Te betalen / terug te ontvangen ZVW: EUR X
- Total te betalen / terug te ontvangen: EUR X

## BTW-aangifte
[Content from nl-btw-return output]
- Registration type and period
- Rubriek 1a: Leveringen/diensten belast met hoog tarief (21%)
- Rubriek 1b: Leveringen/diensten belast met laag tarief (9%)
- Rubriek 1c: Leveringen/diensten belast met overige tarieven
- Rubriek 1d: Privégebruik
- Rubriek 1e: Leveringen/diensten belast met 0% of niet bij u belast
- Rubriek 2a: Verleggingsregelingen
- Rubriek 3a/3b: Prestaties naar/in het buitenland (ICP)
- Rubriek 4a/4b: Prestaties vanuit het buitenland
- Rubriek 5a: Verschuldigde omzetbelasting
- Rubriek 5b: Voorbelasting
- Rubriek 5c/5d/5e: Subtotaal, vermindering, totaal
- BUA correctie (besluit uitsluiting aftrek voorbelasting)
- ICP opgave reconciliation

## Aangifte Inkomstenbelasting

### Box 1 -- Inkomen uit werk en woning
[Content from nl-income-tax output]
- Winst uit onderneming:
  - Omzet: EUR X
  - Bedrijfskosten: EUR X
  - Afschrijvingen: EUR X
  - Winst vóór ondernemersaftrek: EUR X
  - Zelfstandigenaftrek: EUR X
  - Startersaftrek: EUR X
  - MKB-winstvrijstelling: EUR X
  - Belastbare winst: EUR X
  - FOR dotatie: EUR X (if applicable)
- Inkomsten uit dienstbetrekking: EUR X (if applicable)
- Eigen woning:
  - WOZ-waarde: EUR X
  - Eigenwoningforfait: EUR X
  - Hypotheekrente aftrek: EUR X
  - Eigen woning saldo: EUR X
- Inkomen Box 1: EUR X

### Box 2 -- Inkomen uit aanmerkelijk belang
- Not applicable for eenmanszaak (flag if any AB income discovered)

### Box 3 -- Inkomen uit sparen en beleggen
- Peildatum 1 januari 2025:
  - Banktegoeden: EUR X
  - Beleggingen: EUR X
  - Overige bezittingen: EUR X
  - Schulden: EUR X
  - Rendementsgrondslag: EUR X
- Peildatum 1 januari 2026: [same structure]
- Heffingsvrij vermogen: EUR X (EUR 57,000 single / EUR 114,000 fiscal partners -- 2025)
- Voordeel uit sparen en beleggen: EUR X
- Verschuldigde belasting Box 3: EUR X (36% in 2025)

### Heffingskortingen
- Algemene heffingskorting: EUR X (income-dependent phase-out)
- Arbeidskorting: EUR X (income-dependent, for winst uit onderneming)
- Total heffingskortingen: EUR X

### Verschuldigde belasting
- Box 1 belasting (schijventarief): EUR X
  - Schijf 1 (EUR 0 - 38,441): 36.97%
  - Schijf 2 (EUR 38,441 - 75,624): 49.50%
- Box 3 belasting: EUR X
- Totaal verschuldigde belasting: EUR X
- Minus heffingskortingen: EUR X
- Minus voorlopige aanslag IB: EUR X
- Te betalen / terug te ontvangen: EUR X

## Zorgverzekeringswet (ZVW)
[Content from nl-zvw output]
- Bijdrage-inkomen: EUR X
- ZVW percentage: 5.32%
- Maximum bijdrage-inkomen: EUR 71,628 (2025)
- ZVW bijdrage: EUR X
- Voorlopige aanslag ZVW paid: EUR X
- Te betalen / terug te ontvangen: EUR X

## Voorlopige Aanslag 2026
- Based on 2025 final IB + ZVW liability
- Recommended voorlopige aanslag IB 2026: EUR X
- Recommended voorlopige aanslag ZVW 2026: EUR X
- Action: request via MijnBelastingdienst or wait for Belastingdienst to issue

## Cross-skill Reconciliation
- BTW omzet vs IB winst omzet: [pass/fail]
- ZVW bijdrage-inkomen vs IB Box 1: [pass/fail]
- Voorlopige aanslag reconciliation: [pass/fail]
- BTW voorbelasting vs IB deductions: [pass/fail]
- Ondernemersaftrek computation chain: [pass/fail]

## Reviewer Attention Flags
[Aggregated from all upstream skills]
- T2 items requiring belastingadviseur confirmation
- Mixed-use expense percentages (auto, telefoon, internet)
- Werkruimte deduction (if claimed)
- Urencriterium confirmation
- Startersaftrek eligibility
- Any turnover approaching EUR 20,000 KOR threshold
- Any income approaching schijf boundary (EUR 38,441)
- FOR dotatie appropriateness
- Box 3 vermogen composition and categorisation (sparen vs beleggen vs overig)

## Positions Taken
[List with legislation citations]
- e.g., "Zelfstandigenaftrek claimed: EUR 2,470 -- Art. 3.76 Wet IB 2001, urencriterium confirmed by client"
- e.g., "Auto zakelijk gebruik 75% -- client-stated, kilometeradministratie available -- Art. 3.16 Wet IB 2001"
- e.g., "Laptop capitalised and depreciated at 20% p.a. over 5 years -- Art. 3.30 Wet IB 2001"
- e.g., "MKB-winstvrijstelling 13.31% applied -- Art. 3.79a Wet IB 2001"
- e.g., "Representatiekosten 80% limitation applied -- Art. 3.15 Wet IB 2001"

## Planning Notes for 2026
- Voorlopige aanslag recommendation (IB + ZVW)
- KOR threshold monitoring (if approaching EUR 20,000)
- Capital allowances continuing into 2026 (boekwaarde schedule)
- FOR stand and conversion planning (lijfrente aankoop)
- Any legislative changes affecting 2026 (Belastingplan 2026 measures, schijventarief changes)
- Urencriterium documentation reminder

## Client Action List

### Immediate (before 1 May 2026 -- IB filing deadline):
1. Review this return package with your belastingadviseur
2. File aangifte inkomstenbelasting via MijnBelastingdienst
3. Pay any te betalen amount for IB and ZVW
4. File Q4 2025 BTW-aangifte (if not yet filed) -- deadline was 31 January 2026
5. Request/adjust voorlopige aanslag 2026 via MijnBelastingdienst

### BTW filing calendar (quarterly):
- Q1 2026 (Jan-Mar): file by 30 April 2026
- Q2 2026 (Apr-Jun): file by 31 July 2026
- Q3 2026 (Jul-Sep): file by 31 October 2026
- Q4 2026 (Oct-Dec): file by 31 January 2027

### ICP opgave (if applicable):
- Monthly or quarterly (aligned with BTW filing frequency)
- Due same date as BTW-aangifte

### Ongoing:
1. Issue BTW-compliant facturen for all sales (Art. 35a Wet OB 1968)
2. Retain all purchase invoices and receipts (7-year bewaarplicht -- Art. 52 AWR)
3. Maintain kilometeradministratie if claiming auto expenses
4. Maintain urenadministratie for urencriterium
5. Monitor turnover for KOR threshold (EUR 20,000)
6. Track capital assets in the afschrijvingsstaat
7. Monitor FOR stand and plan lijfrente conversion before AOW-leeftijd
```

## Section 5 -- Refusals

- **R-NL-1** — Upstream skill did not run. Name the specific skill. Note: this is a warning, not a hard stop. Continue with available data and flag the gap.  _(Section 5)_
- **R-NL-2** — Upstream self-check failed. Name the specific check and note it in the reviewer brief. Continue.  _(Section 5)_
- **R-NL-3** — Cross-skill reconciliation failed. Name the specific reconciliation and describe the discrepancy. Flag for reviewer but continue.  _(Section 5)_
- **R-NL-4** — Intake incomplete. Specific missing intake items prevent computation. List what is missing and ask the user for the specific data point.  _(Section 5)_
- **R-NL-5** — Out-of-scope item discovered during assembly. E.g., Box 2 aanmerkelijk belang income, foreign source income requiring voorkoming dubbele belasting, or partnership income. Flag and exclude from computation.  _(Section 5)_

## Section 6 -- Self-checks

- **Check NL1 -- All upstream skills executed** — nl-btw-return, nl-income-tax, nl-zvw all produced output.  _(Section 6)_
- **Check NL2 -- BTW omzet matches IB winst omzet** — Within EUR 1 tolerance.  _(Section 6)_
- **Check NL3 -- ZVW uses correct bijdrage-inkomen** — Box 1 verzamelinkomen matches the figure used for ZVW computation.  _(Section 6)_
- **Check NL4 -- Ondernemersaftrek computation order correct** — Zelfstandigenaftrek applied before MKB-winstvrijstelling. MKB-winstvrijstelling percentage applied to winst AFTER zelfstandigenaftrek.  _(Section 6)_
- **Check NL5 -- Regular BTW treatment correct** — Output BTW excluded from omzet; reclaimable voorbelasting excluded from bedrijfskosten; blocked voorbelasting included in bedrijfskosten.  _(Section 6)_
- **Check NL6 -- KOR treatment correct** — No output BTW charged; all input BTW included in bedrijfskosten (bruto = cost).  _(Section 6)_
- **Check NL7 -- Box 3 vermogensrendementsheffing computed correctly** — Heffingsvrij vermogen applied. Correct categorisation of banktegoeden, beleggingen, overige bezittingen. 2025 forfaitaire rendementen applied per category.  _(Section 6)_
- **Check NL8 -- Heffingskortingen correctly computed** — Algemene heffingskorting phased out based on income. Arbeidskorting computed on winst uit onderneming + employment income. Inkomensafhankelijke combinatiekorting if applicable.  _(Section 6)_
- **Check NL9 -- Schijventarief correctly applied** — 2025 rates: 36.97% up to EUR 38,441; 49.50% above EUR 38,441.  _(Section 6)_
- **Check NL10 -- Filing calendar is complete** — All deadlines for BTW, IB, ICP, and voorlopige aanslag are listed with specific dates.  _(Section 6)_
- **Check NL11 -- No form numbers in user-facing messages** — Internal notes can reference rubrieken and artikelen; user-facing messages use plain Dutch/English where possible.  _(Section 6)_
- **Check NL12 -- Reviewer brief contains legislation citations** — Every position taken references the specific article of the relevant Wet (Wet IB 2001, Wet OB 1968, ZVW, AWR).  _(Section 6)_

## Section 7 -- Output files

The final output is three files:

1. `[client_slug]_2025_nl_master.xlsx` -- Single master workbook containing every worksheet. Sheets include: Cover, BTW-aangifte (Q4 or Annual), IB-aangifte (Box 1/2/3), Afschrijvingsstaat, Bedrijfskosten Detail, ZVW Reconciliation, Voorlopige Aanslag 2026, Ondernemersaftrek Berekening, Cross-Check Summary. Use live formulas where possible -- e.g., IB omzet references the BTW turnover cell; ondernemersaftrek chain is formula-driven; Box 3 references peildatum amounts. Verify no `#REF!` errors. Verify computed values match the Python/computation model within EUR 1 before shipping.

2. `reviewer_brief.md` -- Single markdown file covering all sections from Section 4 above: executive summary, BTW, IB (all boxes), ZVW, voorlopige aanslag, cross-skill reconciliation, flags, positions, planning notes.

3. `client_action_list.md` -- Single markdown file with step-by-step actions: immediate filings and payments, quarterly BTW calendar for 2026, ongoing compliance reminders.

If execution runs out of context mid-build: produce whatever is complete, then state at the end which of the three files were not produced or are partial.

All files are placed in `/mnt/user-data/outputs/` and presented to the user via the `present_files` tool at the end.

## Section 8 -- Cross-skill references

Inputs:
- `nl-freelance-intake` -- structured intake package (JSON)
- `nl-btw-return` -- BTW-aangifte rubriek values and classification output
- `nl-income-tax` -- IB-aangifte values and computation output (Box 1/2/3)
- `nl-zvw` -- ZVW bijdrage reconciliation output

Outputs: The final reviewer package. No downstream skill.

## Section 9 -- Known gaps

1. PDF form filling is not automated. The reviewer uses the worksheets to fill the official aangifte on MijnBelastingdienst.
2. E-filing is handled by the reviewer via MijnBelastingdienst portal, not by this skill.
3. Payment execution is the client's responsibility; the skill only provides instructions and amounts.
4. VOF (vennootschap onder firma) returns are not supported -- only eenmanszaak.
5. Box 2 (aanmerkelijk belang) is out of scope for eenmanszaak; flagged if discovered.
6. Multi-year capital allowance tracking assumes the prior year afschrijvingsstaat is provided. If not, only current-year acquisitions are depreciated.
7. Voorkoming dubbele belasting (double taxation relief) is out of scope.
8. Toeslagen (zorgtoeslag, huurtoeslag, kindgebonden budget) are not computed -- these are separate applications via Belastingdienst/Toeslagen.
9. The package is complete only for the 2025 tax year; 2026 appears only as prospective planning.
10. Box 3 vermogensrendementsheffing uses the 2025 forfaitaire rendementen; actual rendementen may differ under the Wet rechtsherstel box 3 if applicable.

### Change log

v1.0 (May 2026): Initial draft. Modelled on mt-return-assembly v0.1 adapted for Netherlands jurisdiction with three content skills (BTW-aangifte, IB-aangifte, ZVW).

## End of skill

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
