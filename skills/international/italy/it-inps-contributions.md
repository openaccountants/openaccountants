---
name: it-inps-contributions
description: Use this skill whenever asked about Italian INPS social contributions for self-employed professionals (Gestione Separata). Trigger on phrases like "INPS contributions", "Gestione Separata", "contributi previdenziali", "aliquota INPS", "rivalsa 4%", "acconto saldo INPS", "minimale contributivo", "massimale INPS", "F24 contributi", "how much INPS do I pay", or any question about Italian freelance social security obligations. Also trigger when classifying bank statement transactions showing F24 INPS payments, Gestione Separata acconti/saldo debits, or Agenzia delle Entrate INPS-related debits. ALWAYS read this skill before touching any Italian social contribution work.
version: 2.0
jurisdiction: IT
tax_year: 2026
last_updated: 2026-09-22
review_status: pending_review
drafted_by: OpenAccountants
approved_by: pending
depends_on:
  - social-contributions-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# INPS contributions for self-employed professionals in Italy (gestione separata)

How an Italian self-employed professional with a VAT number (partita IVA) and no professional fund pays INPS gestione separata contributions: who is in it, rates, cap, rivalsa, Quadro RR, F24 codes and deadlines, and bank statement reading. Figures are for tax year 2026. Rates and caps come from INPS Circolare n. 8 of 3 February 2026. Payment rules come from INPS Circolare n. 62 of 27 May 2026, covering the 2025 saldo and the 2026 acconto paid in 2026, and the 2025 cap used for that saldo. The rivalsa percentage comes from INPS Messaggio n. 7751 of 7 May 2012, still the INPS text on it.

## Section 1: Quick reference

| Field | Value |
| --- | --- |
| Country | Italy |
| Primary legislation | L. 335/1995 art. 2 comma 26 (gestione separata); L. 247/2007 art. 1 comma 79 (rates); L. 662/1996 art. 1 comma 212 (rivalsa) |
| Supporting legislation | TUIR (D.P.R. 917/1986) art. 10 (deduction of contributions) and art. 53 and 54 (professional income) |
| Authority | INPS (Istituto Nazionale della Previdenza Sociale) |
| Rate publisher | INPS, yearly circular: Circolare n. 8 of 3 February 2026 for 2026 |
| Currency | EUR only |
| Rates, cap, full-year level | See the table below |
| Rivalsa INPS | Optional charge to clients, see Rule 4 |
| Payment via | F24, causale PXX (no other cover) or P10 (pensioners or other cover), from Quadro RR of Modello Redditi PF |
| Saldo and primo acconto | 30 June, or 30 July with the surcharge in the Rule 3 table |
| Secondo acconto | 30 November |
| Contributor | Open Accountants |
| Validated by | Pending: requires sign-off by a Dottore Commercialista |
| Validation date | Pending |

**INPS gestione separata 2026 (Circolare n. 8 of 3 February 2026)**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.inps.it/content/dam/inps-site/it/scorporati/circolari-e-messaggi/2026/02/Circolare_15153/Allegati/16573_Circolare-numero-8-del-03-02-2026.pdf |
| Professionals with a VAT number, no other compulsory cover, not pensioners: total rate | 26.07% | "Soggetti non assicurati presso altra forma di 26,07%" |
| of which IVS (pension) | 25% | "aliquota contributiva IVS in misura pari al 25%" |
| of which maternity, family, sickness and parental leave | 0.72% | "aliquota contributiva aggiuntiva pari allo 0,72%" |
| of which ISCRO | 0.35% | "aliquota aggiuntiva pari allo 0,35%" |
| Pensioners, or insured with another compulsory scheme | 24% | "per l’anno 2026, l’aliquota è confermata al 24%" |
| Maximum income on which contributions are due (massimale) | EUR 122,295 | "è pari a 122.295,00 euro" |
| Income needed to credit the whole year (minimale; not a minimum payment) | EUR 18,808 | "è pari a 18.808,00 euro" |
| Contribution that credits the whole year at the full rate | EUR 4,903.25 | "4.903,25 euro (di cui 4.702,00 euro ai fini pensionistici)" |
| Contribution that credits the whole year at the reduced rate | EUR 4,513.92 | "contributo annuo di 4.513,92 euro" |

Read this whole section before computing or classifying anything.

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown whether a cassa propria applies | STOP; check the profession and whether the client pays the fund's contributo soggettivo |
| Unknown other pension cover | Apply the full rate above; flag for reviewer |
| Unknown whether rivalsa was charged | Assume none; ask the client |
| Unknown regime (ordinario vs forfettario) | Ask; it changes which return line is the base |
| Unknown whether an F24 debit is INPS or IRPEF | Flag for reviewer; one F24 combines several taxes |

## Section 2: Required inputs and refusal catalogue

### Required inputs

**Minimum viable.** Professional category (gestione separata or cassa propria), other pension cover or pension status, and net professional income.

**Recommended.** Bank statements showing F24 payments, Modello Redditi PF Quadro RR, invoices showing any rivalsa, the INPS "Cassetto previdenziale per liberi professionisti" extract.

**Ideal.** Complete Modello Redditi PF, Quadro RE or Quadro LM, F24 receipts, INPS estratto conto contributivo.

### Refusal catalogue

- **R-IT-INPS-1: Cassa propria professions.** A professional who pays the contributo soggettivo to an autonomous professional fund (D.Lgs. 509/1994 and 103/1996) is not in the gestione separata and does not fill in Quadro RR section II (Circolare n. 62/2026, link in the method section). Fund rates (Cassa Forense, CNPADC, ENPAM, Inarcassa and others) are out of scope; escalate to a Dottore Commercialista. (Trigger: avvocato, commercialista, medico, ingegnere, architetto, consulente del lavoro, notaio, farmacista, psicologo, veterinario, giornalista, geometra, infermiere.)
- **R-IT-INPS-2: Profession unclear on cassa.** A professional on an Albo who does not pay, or only partly pays, the fund's contributo soggettivo (INPS gives Inarcassa engineers and the commercialisti fund as examples) must pay the gestione separata instead (Circolare n. 62/2026); the Dottore Commercialista must check this before advising. (Trigger: "consulente" or any ambiguous profession.)
- **R-IT-INPS-3: ISCRO eligibility.** ISCRO is the income-continuity benefit funded by the ISCRO part of the rate; its conditions are not in this Guide. Flag for reviewer.

## Section 3: Payment pattern library

### 3.1 F24 payments (combined tax and INPS)

| Pattern | Treatment | Notes |
| --- | --- | --- |
| F24, MODELLO F24 | EXCLUDE: combined tax and INPS | One F24 can carry IRPEF, INPS, addizionali and IVA. The bank line cannot isolate INPS |
| AGENZIA DELLE ENTRATE | EXCLUDE: tax and INPS | F24 payments routed through the Agenzia |
| DELEGA F24 | EXCLUDE: F24 | Bank description for an F24 submission |

### 3.2 INPS-specific F24 codici tributo

_(When F24 receipts, not bank statements, are available, these INPS-section causali identify gestione separata payments. INPS F24 page: https://www.inps.it/it/it/dettaglio-approfondimento.schede-informative.49920.F24-per-professionisti-iscritti-alla-Gestione-Separata.html)_

| Causale | Description | Treatment |
| --- | --- | --- |
| PXX | Saldo or acconto, professional with no other cover and not a pensioner, single payment | EXCLUDE: INPS gestione separata |
| P10 | Saldo or acconto, pensioner or professional with other compulsory cover, single payment | EXCLUDE: INPS gestione separata |
| PXXR, P10R | The same, paid in instalments | EXCLUDE: INPS gestione separata |
| DPPI | Interest: the 30-day deferral surcharge or instalment interest | EXCLUDE: interest, not contribution |
| DPP | Code used until 31 December 2000 for the no-other-cover saldo or acconto | Historic only |
| AP, APR, CP, CPR (and API, CPI) | Artigiani and commercianti codes | EXCLUDE: not gestione separata (different INPS scheme) |

### 3.3 Direct INPS debits (rare for professionisti)

| Pattern | Treatment | Notes |
| --- | --- | --- |
| INPS, ISTITUTO NAZIONALE PREVIDENZA | EXCLUDE: INPS contribution | Direct debit to INPS (uncommon; professionals pay by F24) |

### 3.4 Rivalsa 4% (incoming: revenue, not a contribution)

| Pattern | Treatment | Notes |
| --- | --- | --- |
| RIVALSA INPS, RIVALSA | NOT an INPS payment | Income RECEIVED from clients as part of the fee. It is revenue, already inside the compensi of Quadro RE. See Rule 4 |

### 3.5 Tax payments (NOT INPS)

| Pattern | Treatment | Notes |
| --- | --- | --- |
| IRPEF, IMPOSTA SUL REDDITO | EXCLUDE: income tax | Not INPS |
| IVA, IMPOSTA VALORE AGGIUNTO | EXCLUDE: VAT | Not INPS |
| ADDIZIONALE REGIONALE, ADDIZIONALE COMUNALE | EXCLUDE: local tax | Not INPS |

## Section 4: Worked examples

Six bank statement classifications for a hypothetical Italian consultant (gestione separata, no other cover, regime ordinario).

### Example 1: F24 saldo + primo acconto (30 June)

**Input line:**
`30.06.2026 ; AGENZIA DELLE ENTRATE ; ADDEBITO F24 ; DELEGA F24 30/06 ; -18,978.96 ; EUR`

**Reasoning:**
Matches "AGENZIA DELLE ENTRATE" and "F24" (pattern 3.1), the 30 June date. The F24 combines the INPS saldo, the INPS primo acconto, IRPEF and possibly IVA; the bank line cannot isolate INPS.

**Classification:** EXCLUDE: combined F24 payment. Request the F24 receipt to isolate INPS (causale PXX or P10).

### Example 2: Secondo acconto INPS (30 November)

**Input line:**
`30.11.2026 ; AGENZIA ENTRATE ; ADDEBITO F24 ; DELEGA F24 30/11 ; -8,133.84 ; EUR`

**Reasoning:**
Matches the F24 pattern. 30 November is the secondo acconto date (Circolare n. 62/2026); in 2025, a Sunday, INPS moved it to 1 December. Likely holds both the INPS and IRPEF secondo acconto; cannot be isolated without the receipt.

**Classification:** EXCLUDE: F24 secondo acconto. Request the F24 receipt for the INPS breakdown.

### Example 3: Rivalsa 4% received from client (revenue, not contribution)

**Input line:**
`15.03.2026 ; ACME SRL ; BONIFICO ; COMPENSO PROF + RIVALSA ; +6,344.00 ; EUR`

**Reasoning:**
Invoice of fee, rivalsa on the fee, and IVA on both. The rivalsa is income received, already inside the compensi and the INPS base; do not add it again or classify it as an INPS debit.

**Classification:** NOT an INPS contribution. Rivalsa is revenue.

### Example 4: F24 with rateizzazione (instalment)

**Input line:**
`16.07.2026 ; AGENZIA ENTRATE ; F24 ; 2A RATA SALDO+1ACC ; -3,250.00 ; EUR`

**Reasoning:**
Matches the F24 pattern. This is an instalment of the saldo/primo acconto (Rule 5); interest goes on a separate DPPI line. Combined tax and INPS; cannot split from the bank statement.

**Classification:** EXCLUDE: F24 rateizzazione instalment. Request the F24 receipt for the INPS causali.

### Example 5: Zero income year (no INPS due)

**Input line:**
No F24 debits with PXX or P10 causali found in the period.

**Reasoning:**
The gestione separata has no fixed minimum contribution: it is a percentage of income, so zero income means zero contribution (unlike artigiani/commercianti, who pay a fixed minimale contribution). Quadro RR section II must still be filed at zero income or a loss (Circolare n. 62/2026).

**Classification:** No INPS payment expected. Fewer than twelve months are credited (see Rule 3).

### Example 6: Ravvedimento operoso (late payment with penalty)

**Input line:**
`20.08.2026 ; AGENZIA ENTRATE ; F24 ; RAVVEDIMENTO ; -8,750.00 ; EUR`

**Reasoning:**
Matches F24 plus "RAVVEDIMENTO": a late payment of tax, INPS, or both. DPPI is the interest causale for deferral or instalments, not a late-payment code. The pages read do not say how INPS charges a late payment; the split must come from the F24 receipt.

**Classification:** EXCLUDE: late payment. Flag for reviewer to split the contribution (deductible) from penalties and interest.

## Section 5: Tier 1 rules

### Rule 1: Gestione separata rate

- Rates are in the Section 1 table: the full rate applies to a VAT-number professional with no other compulsory cover who is not a pensioner; the reduced rate applies to a pensioner or one insured with another compulsory scheme (for example, also an employee).
- Collaborators (co.co.co.), company directors and similar pay different rates, split one third worker and two thirds client, paid by the client by the 16th of the following month (Circolare n. 8/2026); not covered here, see T2-4.

### Rule 2: Computation formula

- **INPS computation formula.** Contribution = the rate in the Section 1 table, applied to the income base, up to the massimale. The base is the professional income declared for IRPEF: Quadro RE rigo RE23 (or RE25 after prior losses); income from an association of professionals or a società semplice in Quadro RH (RH15, RH17 or RH18 column 1); or for a forfettario the gross income of Quadro LM rigo LM34 column 2 less the losses in LM37 column 2 (Circolare n. 62/2026). The total goes in Quadro RR rigo RR5, and is reported even when negative. Other income already charged to the gestione separata (as a collaborator, for example) counts towards the same massimale.

### Rule 3: Massimale and minimale

- **Massimale.** No contributions above the massimale in the Section 1 table (yearly). The 2025 saldo, paid in 2026, uses the 2025 cap in the table below.
- **Minimale.** The minimale in the Section 1 table is the income that credits the whole year, not a minimum payment; income below it credits fewer months. The circular does not print the formula for months credited; check the client's INPS statement.

**2025 figures used in 2026 (Circolare n. 62 of 27 May 2026)**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.inps.it/content/dam/inps-site/it/scorporati/circolari-e-messaggi/2026/05/Circolare_15271/Allegati/16793_Circolare-numero-62-del-27-05-2026.pdf |
| Massimale for 2025, used for the 2025 saldo | EUR 120,607 | "per l’anno 2025, a 120.607,00 euro" |
| Surcharge for paying saldo and primo acconto in the 30 days after 30 June, up to 30 July | 0.40% | "la maggiorazione dello 0,40% a titolo di interesse corrispettivo" |
| Occasional self-employment (TUIR art. 67(1)(l)) counts towards the massimale only above an allowance of | EUR 5,000 | "al netto della franchigia pari a 5.000,00 euro" |

### Rule 4: Rivalsa INPS (4%)

**Rivalsa (INPS Messaggio n. 7751 of 7 May 2012)**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.inps.it/content/dam/inps-site/it/scorporati/circolari-e-messaggi/2012/05/Circolare_10983/Allegati/7928_Messaggio-numero-7751-del-07-05-2012.pdf |
| Rivalsa a gestione separata professional may add to the gross fee | 4% | "nella misura del 4 per cento dei compensi lordi" |

- **Rivalsa INPS.** A right, not a duty (L. 662/1996 art. 1 comma 212): the professional alone owes the contributions, whether or not the client pays it. Same for everyone, including pensioners and those with other cover; charged on gross fees with no cap.
- Where the fee itself bears the withholding under D.P.R. 600/1973 art. 25 and IVA, the rivalsa bears them too (Messaggio n. 7751/2012). A forfettario's fees are not subject to that withholding: see `it-income-tax`.
- It is revenue, not a deduction, and already inside the INPS base as part of the fees.

### Rule 5: Payment schedule (acconto/saldo)

| Payment | Deadline in 2026 | Source |
| --- | --- | --- |
| Saldo for 2025 | 30 June 2026, or 30 July 2026 with the surcharge in the Rule 3 table | https://www.inps.it/content/dam/inps-site/it/scorporati/circolari-e-messaggi/2026/05/Circolare_15271/Allegati/16793_Circolare-numero-62-del-27-05-2026.pdf |
| Primo acconto for 2026 | Same dates as the saldo | Circolare n. 62/2026 |
| Secondo acconto for 2026 | 30 November 2026 | Circolare n. 62/2026 |

- **Instalment rules.** The saldo and the primo acconto can be paid in instalments. The first instalment is due on the saldo date (30 June, or 30 July with the surcharge); the others fall on the 16th of each month, and all must be paid by 16 December of the year the return is filed. Interest goes on its own F24 line with causale DPPI. The circular allows instalments only for the saldo and the primo acconto, not the secondo acconto.

**Acconti for 2026 (Istruzioni Modello Redditi 2026 PF, Fascicolo 2, Appendice)**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.agenziaentrate.gov.it/portale/documents/d/guest/pf2_istruzioni_2026_agg-13-05-2026 |
| Share of the 2025 professional income on which the total 2026 acconti are worked out | 80% | "sull’80% del reddito di lavoro" |

- **Acconto amount.** Two acconti of equal amount, paid on the IRPEF acconto dates. Their total is the 2026 rate applied to the share in the table above of the 2025 professional income (the Rule 2 base), within the 2026 massimale (Agenzia instructions, Appendice, "Contributi previdenziali dovuti dai liberi professionisti iscritti alla gestione separata"; Circolare n. 62/2026 confirms the 2026 rates and cap). Each acconto is half of that total. The acconti paid are then subtracted from the contribution due in Quadro RR to give the saldo.

### Rule 6: F24 codici tributo

- **F24 causali.** PXX: saldo or acconto, no other cover. P10: same, pensioner or other cover. Add R (PXXR, P10R) for instalments. DPPI: interest for deferral or instalments, on its own line. Period fields show the year (e.g. 012026 to 122026). Source: the INPS F24 page linked in 3.2, and Circolare n. 62/2026.

### Rule 7: Tax deductibility (IRPEF)

- **Tax deductibility (IRPEF).** Compulsory social contributions paid under the law are deducted from total income as oneri deducibili (TUIR art. 10(1)(e): "versati in ottemperanza a disposizioni di legge"), in the year they are paid. They go in Quadro RP (rigo RP21 in the Redditi 2026 PF form, Fascicolo 1; check the next year's form). Under the regime forfettario, the compulsory contributions are deducted from the income worked out with the coefficient; any excess is deductible from total income (Agenzia forfettario page).

### Rule 8: Quadro RR

- **Quadro RR.** Gestione separata contributions are declared in Quadro RR, section II, of Modello Redditi PF, with totals in section IV; section II is compulsory even at zero income or a loss. Filed online by 31 October of the following year (D.P.R. 322/1998 art. 2).

### Rule 9: First year rule

- **First year rule.** A professional who started work in the year must send the INPS enrolment request as a libero professionista through the "Cassetto previdenziale per liberi professionisti", if not already done (Circolare n. 62/2026). The acconti are worked out on the prior year's professional income (Rule 5). With no professional income in the prior year that base is zero, so no acconto falls due in the first year and the whole first year is paid as saldo the following June. This is our reading of the Rule 5 rule, not a sentence printed on the page; confirm.

### Rule 10: INPS is computed on income BEFORE the INPS deduction

- **INPS computed before deduction.** The base is net professional income from Quadro RE, RH or LM (Rule 2), not gross fees. Contributions are not a cost in Quadro RE; they are deducted later from total income for IRPEF, so the deduction reduces IRPEF, not the INPS base.

## Section 6: Tier 2 catalogue

### T2-1: Regime forfettario interaction

**Trigger:** Client is under the regime forfettario.
**Issue:** The base is the forfettario income of Quadro LM (fees times the activity coefficient, less the losses in LM37 column 2); the same gestione separata rates apply, and contributions are then deducted from the forfettario income before the substitute tax.
**Action:** Flag for reviewer to confirm the coefficient and conditions. See `it-income-tax`.

### T2-2: Rivalsa 4% dispute

**Trigger:** Client charged rivalsa but the customer refuses to pay.
**Issue:** Rivalsa is a right, not a duty; the professional owes the full contribution regardless (Messaggio n. 7751/2012).
**Action:** Flag for reviewer if the dispute affects the figures.

### T2-3: ISCRO eligibility

**Trigger:** Client asks about ISCRO (income continuity benefit).
**Issue:** Its income-based conditions are not on the pages used here.
**Action:** Escalate to a Dottore Commercialista.

### T2-4: Collaboratori vs professionisti

**Trigger:** Unclear whether the client is a professional with a VAT number, a collaborator, or doing occasional work.
**Issue:** Collaborators split one third/two thirds (worker/client), paid by the client. Occasional self-employment has the allowance in the Rule 3 table.
**Action:** Flag for reviewer.

### T2-5: Mid-year opening of partita IVA

**Trigger:** Client opened a partita IVA mid-year.
**Issue:** The full rate applies to actual income, with no pro-rata; the whole-year level in the Section 1 table decides how many months are credited. The client must enrol with INPS (Rule 9).
**Action:** Confirm the start date. For acconti in the first year see Rule 9.

## Section 7: Excel working paper template

~~~
ITALY INPS GESTIONE SEPARATA: WORKING PAPER
Client: [name]
Tax Year: [year]
Prepared: [date]

INPUT DATA
  Professional category:          [Gestione separata / Cassa propria -> STOP]
  Other pension cover:            [YES/NO]
  Pensioner:                      [YES/NO]
  Applicable rate:                [full rate / reduced rate, Section 1 table]
  Net professional income:        [____] (RE23 or RE25, or LM34 col. 2 less losses)
  Rivalsa charged in invoices:    [____] (already inside compensi; do not add)
  Tax regime:                     [Ordinario / Forfettario]

COMPUTATION
  INPS base:                      [____]
  Capped at massimale:            [____]
  INPS contribution:              [____]

PAYMENT SCHEDULE
  Prior year saldo:               [____] (due 30 June, causale PXX or P10)
  Primo acconto:                  [____] (half of the acconto total, Rule 5; due 30 June)
  Secondo acconto:                [____] (the other half; due 30 November)

TAX DEDUCTIBILITY
  Contributions paid in the year, Quadro RP:  [____]

MONTHS CREDITED
  Income vs minimale:             [____] (check INPS statement)

REVIEWER FLAGS
  [List any Tier 2 flags]
~~~

## Section 8: Bank statement reading guide

### How INPS payments appear on Italian bank statements

**F24 payments (most common):**
- Description: "F24", "DELEGA F24", "AGENZIA DELLE ENTRATE", "AGENZIA ENTRATE".
- Timing: 30 June/30 July (saldo, primo acconto), 30 November (secondo acconto), or, in instalments, the first on the saldo date and then the 16th monthly (Rule 5).
- Amount: COMBINED with IRPEF, addizionali, IVA. INPS is one component.
- INPS cannot be isolated from the bank statement; the F24 receipt is needed.

**Direct INPS debits (uncommon for professionisti):**
- Description: "INPS" or "ISTITUTO NAZIONALE". Rare: professionals pay by F24.

**Key identification tips:**
1. The secondo acconto (30 November) is usually paired with the IRPEF secondo acconto.
2. Instalments follow Rule 5: first on the saldo date, then monthly on the 16th to 16 December.
3. Late payments add penalties; flag for reviewer to split.

## Section 9: Onboarding fallback

If the client provides only a bank statement:

1. **Identify F24 debits.** Dates near 30 June, 30 July and 30 November are key.
2. **Note the combined nature.** F24 combines INPS, IRPEF, addizionali and IVA (Section 3.1); it cannot be isolated on the bank statement.
3. **Request F24 receipts** for the causali (Section 3.2).
4. **Check for rivalsa income** (Section 3.4): revenue already in the fees.
5. **Flag** that Quadro RR or the F24 receipt is needed; a bank statement alone is not enough.

## Section 10: Reference material

### Key figures (2026)

Section 1 table. 2025 massimale, surcharge, occasional-work allowance: Rule 3 table. Rivalsa: Rule 4 table.

### Casse professionali (all T3: escalate)

_(Legacy list, not exhaustive and not checked against an official register; other professions also have funds. Membership of a fund is shown by the fund's own statement.)_

| Profession | Cassa |
| --- | --- |
| Avvocati | Cassa Forense |
| Commercialisti | CNPADC |
| Medici/Odontoiatri | ENPAM |
| Ingegneri/Architetti | Inarcassa |
| Consulenti del Lavoro | ENPACL |
| Notai | Cassa del Notariato |
| Farmacisti | ENPAF |
| Psicologi | ENPAP |
| Veterinari | ENPAV |
| Giornalisti | INPGI |
| Geometri | CIPAG |
| Infermieri | ENPAPI |

### Test suite

Expected results are rules, not amounts.

**Test 1:** Professional, no other cover, RE income that includes rivalsa received. Full rate on the RE figure as declared; rivalsa not added again.

**Test 2:** Professional who is also an employee. Reduced rate, causale P10.

**Test 3:** Net income above the 2026 massimale. Contribution only up to the massimale.

**Test 4:** Income zero, partita IVA open. No contribution; Quadro RR section II still filed; fewer months credited.

**Test 5:** Forfettario professional. Base is LM34 column 2 less LM37 column 2; contributions deducted from the forfettario income before the substitute tax.

**Test 6:** Pensioner with freelance income. Reduced rate, causale P10.

**Test 7:** Architect paying the contributo soggettivo to Inarcassa. No gestione separata; refuse (R-IT-INPS-1).

### Prohibitions

- NEVER compute for cassa propria professions using gestione separata rates
- NEVER add rivalsa on top of net income: it is already inside the fees
- NEVER tell a client the rivalsa is deductible: it is revenue
- NEVER apply the full rate to a client with other compulsory cover or a pension
- NEVER suggest there is a fixed minimum contribution in the gestione separata
- NEVER compute on income above the massimale
- NEVER allow the secondo acconto in instalments
- NEVER forget Quadro RR section II, even at zero income
- NEVER treat DPPI as a contribution: it is interest
- NEVER present figures as definitive

## The method, step by step

1. **Check who pays where.** A professional who pays the contributo soggettivo to an autonomous fund is out; one on an Albo who does not pay it is in the gestione separata (INPS Circolare n. 62/2026, section 2.2). https://www.inps.it/content/dam/inps-site/it/scorporati/circolari-e-messaggi/2026/05/Circolare_15271/Allegati/16793_Circolare-numero-62-del-27-05-2026.pdf
2. **Fix the base.** Take the professional income from Quadro RE (RE23 or RE25), Quadro RH for associated practices, or Quadro LM (LM34 column 2 less LM37 column 2), and other gestione separata income for the cap (Circolare n. 62/2026, same link).
3. **Pick the rate and apply the cap.** Full or reduced rate and the massimale from INPS Circolare n. 8/2026. https://www.inps.it/content/dam/inps-site/it/scorporati/circolari-e-messaggi/2026/02/Circolare_15153/Allegati/16573_Circolare-numero-8-del-03-02-2026.pdf
4. **Declare in Quadro RR.** Section II (and IV) of Modello Redditi PF: contribution due less acconti paid gives the saldo. File online by 31 October (D.P.R. 322/1998 art. 2). https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1998-07-22;322~art2!vig=2026-06-30
5. **Pay by F24.** Causale PXX or P10 (R for instalments, DPPI for interest), on 30 June or 30 July, and 30 November. https://www.inps.it/it/it/dettaglio-approfondimento.schede-informative.49920.F24-per-professionisti-iscritti-alla-Gestione-Separata.html
6. **Deduct for IRPEF.** Contributions paid in the year are oneri deducibili (TUIR art. 10(1)(e)). https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917~art10!vig=2026-06-30 For forfettari, deduct from the forfettario income: https://www.agenziaentrate.gov.it/portale/regime-forfetario-le-regole-2020-/infogen-regime-forfetario-le-regole-2020-

## Ask the client first

- Are you enrolled in a professional fund (cassa), and do you pay its contributo soggettivo?
- Are you already a pensioner, or insured with another compulsory scheme (for example, as an employee)?
- Are you in the regime forfettario or the regime ordinario?
- Did you add the rivalsa to your invoices, and is it included in the fees you declared?
- Did you have other gestione separata income in the year, as a collaborator or from occasional work?
- When did you open your partita IVA, and have you enrolled with INPS as a libero professionista?

## When to refuse or refer

- Members of an autonomous professional fund: fund rates are not covered.
- Artigiani and commercianti (different INPS scheme, fixed contribution on a minimale).
- Collaborators, company directors and other parasubordinati: the client pays and the rates differ.
- Amateur sports workers (Quadro RR section III): special base rules.
- ISCRO claims, suspension for illness or injury, and refunds of excess contributions.
- Late payments, INPS penalties, and disputes over contributions due.
- Concordato preventivo biennale choices for the contribution base.

## Sources

- INPS Circolare n. 8 of 3 February 2026: https://www.inps.it/content/dam/inps-site/it/scorporati/circolari-e-messaggi/2026/02/Circolare_15153/Allegati/16573_Circolare-numero-8-del-03-02-2026.pdf
- INPS Circolare n. 62 of 27 May 2026: https://www.inps.it/content/dam/inps-site/it/scorporati/circolari-e-messaggi/2026/05/Circolare_15271/Allegati/16793_Circolare-numero-62-del-27-05-2026.pdf
- INPS Messaggio n. 7751 of 7 May 2012: https://www.inps.it/content/dam/inps-site/it/scorporati/circolari-e-messaggi/2012/05/Circolare_10983/Allegati/7928_Messaggio-numero-7751-del-07-05-2012.pdf
- Agenzia delle Entrate, Istruzioni Redditi 2026 PF, Fascicolo 2 (Appendice): https://www.agenziaentrate.gov.it/portale/documents/d/guest/pf2_istruzioni_2026_agg-13-05-2026
- INPS, F24 per professionisti iscritti alla Gestione Separata: https://www.inps.it/it/it/dettaglio-approfondimento.schede-informative.49920.F24-per-professionisti-iscritti-alla-Gestione-Separata.html
- TUIR art. 10: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917~art10!vig=2026-06-30
- D.P.R. 322/1998 art. 2: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1998-07-22;322~art2!vig=2026-06-30
- Agenzia delle Entrate, regime forfetario: https://www.agenziaentrate.gov.it/portale/regime-forfetario-le-regole-2020-/infogen-regime-forfetario-le-regole-2020-

## Disclaimer

This Guide and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this Guide. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date version of this Guide is maintained at openaccountants.com. Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

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
