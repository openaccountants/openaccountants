---
name: it-inps-contributions
description: >
  Use this skill whenever asked about Italian INPS social contributions for self-employed professionals (Gestione Separata). Trigger on phrases like "INPS contributions", "Gestione Separata", "contributi previdenziali", "aliquota INPS", "rivalsa 4%", "acconto saldo INPS", "minimale contributivo", "massimale INPS", "F24 contributi", "how much INPS do I pay", or any question about Italian freelance social security obligations. Covers Gestione Separata rates, minimale/massimale, acconto/saldo payment schedule, rivalsa 4%, interaction with IRPEF, and casse professionali escalation. ALWAYS read this skill before touching any Italian social contribution work.
version: 1.0
jurisdiction: IT
tax_year: 2025
category: international
depends_on:
  - social-contributions-workflow-base
---

# Italy INPS Contributions (Gestione Separata) -- Self-Employed Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Italy |
| Jurisdiction Code | IT |
| Primary Legislation | Legge 8 agosto 1995 n. 335 (Riforma Dini); Legge 22 maggio 2017 n. 81 (Jobs Act Autonomi) |
| Supporting Legislation | TUIR Art. 10 comma 1 lett. e) (deductibility); D.P.R. 917/1986 Art. 54 (reddito di lavoro autonomo) |
| Tax Authority | INPS (Istituto Nazionale della Previdenza Sociale) |
| Rate Publisher | INPS (publishes annual circular -- Circolare n. 27 del 30 gennaio 2025 for 2025 rates) |
| Contributor | Open Accountants |
| Validated By | Pending -- requires sign-off by a qualified Dottore Commercialista |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: rate calculation, massimale/minimale, payment schedule, rivalsa 4%, IRPEF deductibility. Tier 2: ISCRO eligibility, regime forfettario interaction, dual-activity overlaps. Tier 3: casse professionali (Cassa Forense, CNPADC, ENPAM, Inarcassa, etc.), international social security coordination. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags and presents options. Qualified Dottore Commercialista must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate and document.

---

## Step 0: Client Onboarding Questions

Before computing any INPS contribution, you MUST know:

1. **Professional category** [T1] -- professionista senza cassa (Gestione Separata), or regulated profession with own cassa (avvocato, commercialista, medico, ingegnere, etc.)?
2. **Other pension coverage** [T1] -- is the client already enrolled in another mandatory pension scheme (altra gestione obbligatoria) or receiving a pension?
3. **Tax regime** [T1] -- regime ordinario or regime forfettario?
4. **Prior year taxable income (reddito imponibile)** [T1] -- for acconto/saldo computation
5. **Current year income estimate** [T1] -- for acconto computation
6. **First year of activity?** [T1] -- affects acconto calculation
7. **ISCRO eligibility** [T2] -- has the client applied for or received ISCRO (Indennita Straordinaria di Continuita Reddituale e Operativa)?

**If professional category is unknown, STOP. Do not compute contributions. A professionista with a cassa propria does NOT use Gestione Separata.**

---

## Step 1: Determine Applicable Rate [T1]

**Source:** INPS Circolare n. 27 del 30 gennaio 2025

### Gestione Separata -- Professionisti (Partita IVA)

| Category | Aliquota 2025 | Composition |
|----------|--------------|-------------|
| Professionisti senza cassa -- no other pension coverage, not pensioned | **26.07%** | 25.00% IVS + 0.72% maternita/malattia/degenza + 0.35% ISCRO |
| Professionisti senza cassa -- with other pension coverage or pensioned | **24.00%** | 24.00% IVS only |

### Gestione Separata -- Collaboratori e figure assimilate

| Category | Aliquota 2025 | Notes |
|----------|--------------|-------|
| Collaboratori without other coverage, with DIS-COLL | 35.03% | Includes DIS-COLL contribution |
| Collaboratori without other coverage, without DIS-COLL | 33.72% | |
| Collaboratori with other coverage or pensioned | 24.00% | |

**This skill focuses on professionisti con partita IVA. Collaboratori rates are listed for reference only.**

### Rate Split Between Client and Committente (for collaborators)

For collaboratori, the contribution is split 2/3 committente + 1/3 collaboratore. For professionisti con partita IVA, the full contribution is borne by the professionista (with the optional 4% rivalsa -- see Step 4).

---

## Step 2: Massimale and Minimale [T1]

**Source:** INPS Circolare n. 27 del 30 gennaio 2025

| Threshold | 2025 Value | Notes |
|-----------|------------|-------|
| Massimale contributivo (income ceiling) | **EUR 120,607** | No contributions due on income above this amount |
| Minimale contributivo (minimum income threshold) | **EUR 18,555** | Minimum income for full year of contribution credit |

### Massimale Rule

Contributions are calculated on income up to EUR 120,607. Income above this ceiling is not subject to INPS contributions.

```
INPS contribution = min(taxable_income, EUR 120,607) x applicable_rate
```

### Minimale Rule

If the professionista's income is below EUR 18,555, they receive proportionally reduced contribution months (accredito contributivo ridotto). The contribution is still calculated on actual income, but fewer months of pension credit are accrued.

```
Months credited = (actual_income / EUR 18,555) x 12, rounded down
```

There is NO mandatory minimum contribution amount in Gestione Separata (unlike INPS Artigiani/Commercianti). A professionista with zero income pays zero INPS.

---

## Step 3: Computation Formula [T1]

**Legislation:** L. 335/1995 Art. 2 comma 26 et seq.

### Base imponibile (taxable base)

```
INPS base = Reddito netto di lavoro autonomo (net self-employment income from Quadro RE or Quadro LM)
           + Rivalsa 4% received from clients (if any)
```

**Important:** The rivalsa 4% received IS included in the INPS contribution base. It forms part of taxable income.

### Contribution calculation

```
INPS contribution = min(INPS_base, massimale) x aliquota
```

### Example (standard professionista, no other coverage)

```
Net income:          EUR 50,000
Rivalsa received:    EUR 2,000
INPS base:           EUR 52,000
Aliquota:            26.07%
INPS contribution:   EUR 52,000 x 26.07% = EUR 13,556.40
```

---

## Step 4: Rivalsa INPS 4% [T1]

**Legislation:** L. 335/1995 Art. 2 comma 26

| Parameter | Detail |
|-----------|--------|
| What | The professionista may charge clients an additional 4% of their fee as INPS contribution recovery |
| Mandatory? | NO -- it is a facolta (right), not an obligation |
| On invoice | Shown as a separate line item: "Rivalsa INPS 4% ai sensi L. 335/1995" |
| Subject to IVA? | YES -- rivalsa INPS is part of the IVA taxable base |
| Subject to ritenuta d'acconto? | YES -- the 20% withholding tax applies to the fee + rivalsa |
| Included in INPS base? | YES -- rivalsa received is added to income for INPS contribution calculation |
| Deductible for IRPEF? | The rivalsa is income for the professionista. The INPS contributions paid (including on rivalsa) are deductible. The rivalsa itself is NOT a deduction -- it is a revenue item. |

### Rivalsa Invoice Example

```
Compenso professionale:                    EUR 5,000.00
Rivalsa INPS 4%:                           EUR   200.00
Imponibile IVA:                            EUR 5,200.00
IVA 22%:                                   EUR 1,144.00
Totale fattura:                            EUR 6,344.00
Ritenuta d'acconto 20% su EUR 5,200.00:  -EUR 1,040.00
Netto a pagare:                            EUR 5,304.00
```

---

## Step 5: Payment Schedule -- Acconto and Saldo [T1]

**Legislation:** D.P.R. 917/1986; INPS circular instructions

INPS Gestione Separata contributions are paid through the tax return cycle (Modello Redditi PF), using the F24 payment form.

### Payment Structure

| Payment | Percentage | Deadline | Notes |
|---------|-----------|----------|-------|
| Saldo (prior year balance) | Residual after prior year acconti | 30 June (or 30 July with 0.40% surcharge) | Settlement of prior year |
| Primo acconto (first advance) | 40% of prior year's total contribution | 30 June (or 30 July with 0.40% surcharge) | Paid together with saldo |
| Secondo acconto (second advance) | 60% of prior year's total contribution | 30 November (1 December 2025 as 30 Nov is a Sunday) | Cannot be paid in instalments |

### Rateizzazione (instalment option)

The saldo and primo acconto (due 30 June) can be paid in monthly instalments from June to November, with monthly interest of 0.33% per instalment. The secondo acconto CANNOT be paid in instalments.

### F24 Codici Tributo

| Code | Description |
|------|-------------|
| DPPI | Gestione Separata -- professionisti: acconto contribution |
| DPP | Gestione Separata -- professionisti: saldo contribution |

### First Year Rule

In the first year of activity, there is no prior year base for acconti. The professionista may either:
- Pay nothing during the year and settle the full saldo by 30 June of the following year, OR
- Make voluntary advance payments based on estimated income (recommended to avoid a large lump sum)

---

## Step 6: Interaction with IRPEF [T1]

**Legislation:** TUIR Art. 10 comma 1 lettera e)

| Question | Answer |
|----------|--------|
| Are INPS contributions deductible? | YES -- 100% deductible from total taxable income (reddito complessivo) |
| Where deducted? | Quadro RP (oneri deducibili), Rigo RP21 of Modello Redditi PF |
| Which year? | Contributions paid in year X are deducted in year X (cash basis / principio di cassa) |
| Effect on IRPEF | Reduces taxable income before IRPEF rate application; reduces addizionali regionali and comunali too |
| Regime forfettario | Under regime forfettario (flat 15% or 5% tax), INPS contributions are deducted from the forfait income before applying the flat rate |

### Computation Sequence

```
1. Determine gross professional income (Quadro RE or LM)
2. Compute INPS contribution on that income
3. Deduct INPS contribution from reddito complessivo (Quadro RP)
4. Apply IRPEF rates to reduced taxable income
```

**Circular dependency note:** INPS is computed on income BEFORE the INPS deduction. The INPS deduction reduces IRPEF, not the INPS base itself.

---

## Step 7: Quadro RR -- Dichiarazione dei Redditi [T1]

**Legislation:** INPS instructions for Modello Redditi PF

| Parameter | Detail |
|-----------|--------|
| Where | Quadro RR, Sezione II of Modello Redditi PF |
| What is declared | INPS Gestione Separata contribution calculation: income, rate, saldo, acconti |
| Deadline | Same as Modello Redditi PF: 31 October (for 2024 income declared in 2025) |
| Effect | INPS uses Quadro RR data to reconcile the professionista's contribution position |

---

## Step 8: Regime Forfettario Interaction [T2]

**Legislation:** L. 190/2014 Art. 1 commi 54-89 (as amended)

| Parameter | Detail |
|-----------|--------|
| INPS base under forfettario | Reddito imponibile = Ricavi x coefficiente di redditivita (e.g., 78% for professionisti) |
| Rate | Same Gestione Separata rate (26.07% or 24%) |
| Reduced rate for start-ups? | The 5% flat IRPEF rate (instead of 15%) applies for first 5 years if conditions met; INPS rate is unchanged |
| Deductibility | INPS is deducted from the forfait income before applying the flat tax rate |

**Example under forfettario:**
```
Ricavi:                    EUR 60,000
Coefficiente (78%):        EUR 46,800
INPS (26.07%):             EUR 12,201
Reddito after INPS:        EUR 34,599
Flat tax (15%):            EUR 5,190
```

---

## Step 9: Casse Professionali -- Escalation [T3]

Professionals in regulated professions with a dedicated cassa previdenziale do NOT enroll in Gestione Separata. The following are all [T3] -- do not compute; escalate to the relevant cassa or Dottore Commercialista:

| Profession | Cassa |
|-----------|-------|
| Avvocati (lawyers) | Cassa Forense |
| Dottori Commercialisti / Esperti Contabili | CNPADC |
| Medici / Odontoiatri | ENPAM |
| Ingegneri / Architetti | Inarcassa |
| Consulenti del Lavoro | ENPACL |
| Notai | Cassa del Notariato |
| Farmacisti | ENPAF |
| Psicologi | ENPAP |
| Veterinari | ENPAV |
| Giornalisti | INPGI |
| Geometri | CIPAG |
| Infermieri | ENPAPI |

**If the client belongs to a regulated profession, STOP. This skill does not cover cassa propria contribution rates or rules.**

---

## Step 10: Penalties [T1]

**Legislation:** L. 388/2000 Art. 116 commi 8-10

| Penalty | Rate |
|---------|------|
| Late payment (within 15 days) | 1.50% of unpaid amount |
| Late payment (16-90 days) | 3.75% of unpaid amount (ravvedimento breve) |
| Late payment (91 days - 1 year) | 6.00% of unpaid amount (ravvedimento intermedio) |
| Late payment (beyond 1 year) | 7.50% of unpaid amount |
| Interest | Legal interest rate (2.50% for 2025) accrues daily |
| Omitted registration | All unpaid contributions + sanctions + interest retroactively |

**Ravvedimento operoso (voluntary correction) reduces penalties significantly if the taxpayer self-corrects before INPS assessment.**

---

## Step 11: Edge Case Registry

### EC1 -- Professionista with both Gestione Separata and employment income [T1]
**Situation:** Client is a part-time employee (INPS Gestione Ordinaria via employer) and also has a partita IVA with freelance income.
**Resolution:** The client pays Gestione Separata at the REDUCED rate of 24.00% on freelance income (because they have altra gestione obbligatoria from employment). Employment contributions continue separately.

### EC2 -- Income exceeds massimale [T1]
**Situation:** Client earns EUR 150,000 net from freelance activity.
**Resolution:** Contributions are calculated on EUR 120,607 only (massimale 2025). INPS = EUR 120,607 x 26.07% = EUR 31,434. Income above the massimale is not subject to contributions.

### EC3 -- Zero income year [T1]
**Situation:** Client earned zero income. Partita IVA remains open.
**Resolution:** Zero INPS contributions due (no minimale contribution in Gestione Separata). Zero months of pension credit accrue. No payment required. The partita IVA can remain open without triggering minimum contributions.

### EC4 -- Pensioner with freelance income [T1]
**Situation:** Client receives an INPS pension and continues freelancing with partita IVA.
**Resolution:** Gestione Separata at the reduced rate of 24.00%. No ISCRO component. Contributions are fully deductible from IRPEF.

### EC5 -- Rivalsa 4% charged but client disputes it [T2]
**Situation:** Client charged rivalsa 4% to a corporate customer who refuses to pay it.
**Resolution:** Rivalsa is a facolta, not enforceable if not agreed in the contract. If not charged, the professionista bears the full INPS cost. If charged and paid, it enters the INPS base. [T2] flag for reviewer if dispute affects contribution calculation.

### EC6 -- Mid-year opening of partita IVA [T1]
**Situation:** Client opens partita IVA on 1 July 2025. Earns EUR 30,000 in 6 months.
**Resolution:** Full 26.07% rate applies on the EUR 30,000. No pro-rata reduction of the rate. Minimale of EUR 18,555 still applies for full-year credit; if EUR 30,000 > EUR 18,555, full 12 months credited. Saldo due by 30 June 2026; no acconti in the first year unless voluntary.

### EC7 -- Profession liberale unsure if cassa propria exists [T3]
**Situation:** Client is a "consulente" but unclear whether a cassa propria covers their profession.
**Resolution:** [T3] escalate. Enrolling in the wrong scheme has severe consequences. The Dottore Commercialista must verify the profession against the list of casse before advising.

---

## Step 12: Reviewer Escalation Protocol

When Claude identifies a [T2] situation:

```
REVIEWER FLAG
Tier: T2
Client: [name]
Situation: [description]
Issue: [what is ambiguous]
Options: [possible treatments]
Recommended: [most likely correct treatment and why]
Action Required: Qualified Dottore Commercialista must confirm before advising client.
```

When Claude identifies a [T3] situation:

```
ESCALATION REQUIRED
Tier: T3
Client: [name]
Situation: [description]
Issue: [outside skill scope]
Action Required: Do not advise. Refer to qualified Dottore Commercialista. Document gap.
```

---

## Step 13: Test Suite

### Test 1 -- Standard professionista senza cassa, no other coverage
**Input:** Professionista. Net income: EUR 50,000. Rivalsa received: EUR 2,000. No other pension coverage. Not pensioned.
**Expected output:**
- INPS base: EUR 52,000
- Aliquota: 26.07%
- INPS contribution: EUR 52,000 x 26.07% = EUR 13,556.40
- Primo acconto (40%): EUR 5,422.56 (due 30 June)
- Secondo acconto (60%): EUR 8,133.84 (due 30 November)
- Fully deductible from IRPEF in Quadro RP

### Test 2 -- Professionista with other pension coverage (employed part-time)
**Input:** Professionista also employed part-time. Net freelance income: EUR 30,000. No rivalsa.
**Expected output:**
- INPS base: EUR 30,000
- Aliquota: 24.00% (reduced -- altra gestione obbligatoria)
- INPS contribution: EUR 30,000 x 24.00% = EUR 7,200.00

### Test 3 -- Income above massimale
**Input:** Professionista. Net income: EUR 150,000. No rivalsa. No other coverage.
**Expected output:**
- INPS base: min(EUR 150,000, EUR 120,607) = EUR 120,607
- Aliquota: 26.07%
- INPS contribution: EUR 120,607 x 26.07% = EUR 31,442.24
- Income above EUR 120,607 (EUR 29,393) is not subject to INPS

### Test 4 -- Zero income, partita IVA open
**Input:** Professionista. Net income: EUR 0. Partita IVA active.
**Expected output:**
- INPS contribution: EUR 0
- Months credited: 0
- No payment due. No minimale in Gestione Separata.

### Test 5 -- Regime forfettario professionista
**Input:** Professionista under regime forfettario. Ricavi: EUR 60,000. Coefficiente di redditivita: 78%. No other coverage. First 5 years (5% flat rate).
**Expected output:**
- Reddito imponibile: EUR 60,000 x 78% = EUR 46,800
- INPS (26.07%): EUR 46,800 x 26.07% = EUR 12,200.76
- Reddito after INPS deduction: EUR 46,800 - EUR 12,200.76 = EUR 34,599.24
- Flat tax (5%): EUR 34,599.24 x 5% = EUR 1,729.96

### Test 6 -- Pensioner with freelance activity
**Input:** Pensioner receiving INPS pension. Freelance net income: EUR 20,000. No rivalsa.
**Expected output:**
- Aliquota: 24.00% (pensionato)
- INPS contribution: EUR 20,000 x 24.00% = EUR 4,800.00
- Fully deductible from IRPEF

### Test 7 -- Income below minimale
**Input:** Professionista. Net income: EUR 10,000. No other coverage.
**Expected output:**
- INPS contribution: EUR 10,000 x 26.07% = EUR 2,607.00
- Months credited: floor(EUR 10,000 / EUR 18,555 x 12) = floor(6.46) = 6 months
- Reduced pension credit accrual

---

## PROHIBITIONS

- NEVER compute contributions for a professionista with a cassa propria using Gestione Separata rates -- this is [T3], escalate
- NEVER omit rivalsa 4% from the INPS computation base if the client received rivalsa income
- NEVER tell a client that rivalsa 4% is deductible from IRPEF as a separate deduction -- it is revenue, not a deduction (the INPS contributions on it are deductible)
- NEVER apply the 26.07% rate to a client who has other mandatory pension coverage or is pensioned -- the rate is 24.00%
- NEVER suggest there is a minimum contribution in Gestione Separata -- there is no minimale contribution (unlike Artigiani/Commercianti)
- NEVER compute contributions on income above the massimale (EUR 120,607 for 2025)
- NEVER allow the secondo acconto to be paid in instalments -- only the saldo and primo acconto are eligible for rateizzazione
- NEVER forget to include INPS in the Quadro RR of Modello Redditi PF
- NEVER advise on ISCRO eligibility without [T2] escalation -- conditions are complex and income-based
- NEVER present contribution figures as definitive -- always label as estimated and direct client to their Dottore Commercialista for confirmation

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
