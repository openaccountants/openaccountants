---
name: it-inps-contributions
description: >
  Use this skill whenever asked about Italian INPS social contributions for self-employed professionals (Gestione Separata). Trigger on phrases like "INPS contributions", "Gestione Separata", "contributi previdenziali", "aliquota INPS", "rivalsa 4%", "acconto saldo INPS", "minimale contributivo", "massimale INPS", "F24 contributi", "how much INPS do I pay", or any question about Italian freelance social security obligations. Also trigger when classifying bank statement transactions showing F24 INPS payments, Gestione Separata acconti/saldo debits, or Agenzia delle Entrate INPS-related debits. ALWAYS read this skill before touching any Italian social contribution work.
version: 2.0
jurisdiction: IT
tax_year: 2025
category: international
depends_on:
  - social-contributions-workflow-base
---

# Italy INPS Contributions (Gestione Separata) -- Self-Employed Skill v2.0

## Section 1 -- Quick reference

**Read this whole section before computing or classifying anything.**

| Field | Value |
|---|---|
| Country | Italy |
| Primary Legislation | L. 335/1995 (Riforma Dini); L. 81/2017 (Jobs Act Autonomi) |
| Supporting Legislation | TUIR Art. 10 (deductibility); D.P.R. 917/1986 Art. 54 |
| Tax Authority | INPS (Istituto Nazionale della Previdenza Sociale) |
| Rate Publisher | INPS (annual circular -- Circolare n. 27 del 30 gennaio 2025) |
| Currency | EUR only |
| Aliquota (no other coverage) | 26.07% (25.00% IVS + 0.72% maternita + 0.35% ISCRO) |
| Aliquota (with other coverage/pensioned) | 24.00% |
| Massimale (income ceiling) | EUR 120,607 |
| Minimale (full year credit) | EUR 18,555 |
| Rivalsa INPS | 4% (optional, charged to clients) |
| Payment via | F24 (codici DPPI/DPP) through Modello Redditi PF |
| Saldo + primo acconto | 30 June (or 30 July with 0.40% surcharge) |
| Secondo acconto | 30 November |
| Contributor | Open Accountants |
| Validated by | Pending -- requires sign-off by Dottore Commercialista |
| Validation date | Pending |

**Conservative defaults:**

| Ambiguity | Default |
|---|---|
| Unknown whether cassa propria exists | STOP -- do not compute; must verify profession |
| Unknown other pension coverage | Apply 26.07% (higher rate); flag for reviewer |
| Unknown rivalsa 4% received | Assume zero; ask client |
| Unknown regime (ordinario vs forfettario) | Ask -- affects base computation |
| Unknown whether F24 debit is INPS or IRPEF | Flag for reviewer -- F24 combines multiple taxes |

---

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

**Minimum viable** -- professional category (Gestione Separata vs cassa propria), other pension coverage status, and net professional income.

**Recommended** -- bank statements showing F24 payments, Modello Redditi PF Quadro RR, rivalsa 4% income received, Cassetto Previdenziale INPS extract.

**Ideal** -- complete Modello Redditi PF, Quadro RE or Quadro LM, F24 payment receipts, INPS estratto conto contributivo.

### Refusal catalogue

**R-IT-INPS-1 -- Cassa propria professions.** *Trigger:* client is avvocato, commercialista, medico, ingegnere, architetto, consulente del lavoro, notaio, farmacista, psicologo, veterinario, giornalista, geometra, or infermiere. *Message:* "Professionals with a cassa propria do NOT use Gestione Separata. This skill does not cover cassa-specific rates (Cassa Forense, CNPADC, ENPAM, Inarcassa, etc.). Escalate to Dottore Commercialista."

**R-IT-INPS-2 -- Profession unclear on cassa.** *Trigger:* client is a "consulente" or ambiguous profession. *Message:* "Enrolling in the wrong scheme has severe consequences. The Dottore Commercialista must verify the profession against the cassa list before advising."

**R-IT-INPS-3 -- ISCRO eligibility.** *Trigger:* client asks about ISCRO (Indennita Straordinaria). *Message:* "ISCRO conditions are complex and income-based. Flag for reviewer."

---

## Section 3 -- Payment pattern library

This is the deterministic pre-classifier for bank statement transactions related to INPS contributions.

### 3.1 F24 payments (combined tax and INPS)

| Pattern | Treatment | Notes |
|---|---|---|
| F24, MODELLO F24 | EXCLUDE -- combined tax/INPS | F24 can include IRPEF, INPS, addizionali, IVA -- cannot isolate INPS from bank statement |
| AGENZIA DELLE ENTRATE | EXCLUDE -- tax/INPS | F24 payments routed through AdE |
| DELEGA F24 | EXCLUDE -- F24 | Bank description for F24 submission |

### 3.2 INPS-specific F24 codici tributo

When F24 receipts (not bank statements) are available, these codes identify INPS:

| Codice | Description | Treatment |
|---|---|---|
| DPPI | Gestione Separata professionisti -- acconto | EXCLUDE -- INPS acconto |
| DPP | Gestione Separata professionisti -- saldo | EXCLUDE -- INPS saldo |
| P10, PXX | Artigiani/Commercianti codes | EXCLUDE -- not Gestione Separata (different INPS scheme) |

### 3.3 Direct INPS debits (rare for professionisti)

| Pattern | Treatment | Notes |
|---|---|---|
| INPS, ISTITUTO NAZIONALE PREVIDENZA | EXCLUDE -- INPS contribution | Direct debit to INPS (uncommon; most pay via F24) |

### 3.4 Rivalsa 4% (incoming -- revenue, not a contribution)

| Pattern | Treatment | Notes |
|---|---|---|
| RIVALSA INPS, RIVALSA 4% | NOT an INPS payment | This is income RECEIVED from clients; it is revenue, not a contribution payment. It enters the INPS computation base. |

### 3.5 Tax payments (NOT INPS)

| Pattern | Treatment | Notes |
|---|---|---|
| IRPEF, IMPOSTA SUL REDDITO | EXCLUDE -- income tax | Not INPS |
| IVA, IMPOSTA VALORE AGGIUNTO | EXCLUDE -- VAT | Not INPS |
| ADDIZIONALE REGIONALE, ADDIZIONALE COMUNALE | EXCLUDE -- local tax | Not INPS |

---

## Section 4 -- Worked examples

Six bank statement classifications for a hypothetical Italian self-employed consultant (Gestione Separata, no other pension coverage, regime ordinario).

### Example 1 -- F24 saldo + primo acconto (30 June)

**Input line:**
`30.06.2025 ; AGENZIA DELLE ENTRATE ; ADDEBITO F24 ; DELEGA F24 30/06 ; -18,978.96 ; EUR`

**Reasoning:**
Matches "AGENZIA DELLE ENTRATE" + "F24" (pattern 3.1). This is the 30 June deadline payment. The F24 combines: INPS saldo (prior year balance), INPS primo acconto (40% of current year estimate), IRPEF saldo and acconto, addizionali, and possibly IVA. Cannot isolate INPS from the bank statement. Need F24 receipt or Modello Redditi PF for breakdown.

**Classification:** EXCLUDE -- combined F24 payment. Request F24 receipt to isolate INPS (codici DPPI/DPP).

### Example 2 -- Secondo acconto INPS (30 November)

**Input line:**
`01.12.2025 ; AGENZIA ENTRATE ; ADDEBITO F24 ; DELEGA F24 01/12 ; -8,133.84 ; EUR`

**Reasoning:**
Matches F24 pattern. 1 December 2025 (because 30 November is a Sunday). This F24 likely contains the secondo acconto INPS (60% of prior year contribution) plus IRPEF secondo acconto. Cannot isolate INPS without F24 receipt.

**Classification:** EXCLUDE -- F24 secondo acconto. Request F24 receipt for INPS breakdown.

### Example 3 -- Rivalsa 4% received from client (revenue, not contribution)

**Input line:**
`15.03.2025 ; ACME SRL ; BONIFICO ; COMPENSO PROF + RIVALSA ; +6,344.00 ; EUR`

**Reasoning:**
Client paid invoice including EUR 5,000 compenso + EUR 200 rivalsa INPS 4% + EUR 1,144 IVA. The rivalsa 4% is INCOME received, not a contribution payment. It must be included in the INPS computation base. Do not classify as an INPS debit.

**Classification:** NOT an INPS contribution. Rivalsa is revenue. Include in INPS base when computing contributions.

### Example 4 -- F24 with rateizzazione (instalment)

**Input line:**
`16.07.2025 ; AGENZIA ENTRATE ; F24 ; RATA 2/6 SALDO+1ACC ; -3,250.00 ; EUR`

**Reasoning:**
Matches F24 pattern. The saldo and primo acconto (due 30 June) can be paid in up to 6 monthly instalments with 0.33% monthly interest. This is instalment 2 of 6. Combined tax and INPS. Cannot split from bank statement.

**Classification:** EXCLUDE -- F24 rateizzazione instalment. Request F24 receipt for INPS codici.

### Example 5 -- Zero income year (no INPS due)

**Input line:**
No F24 debits with DPPI/DPP codes found in the period.

**Reasoning:**
In Gestione Separata, there is NO mandatory minimum contribution. Zero income = zero INPS. Unlike INPS Artigiani/Commercianti which has minimale contributions, Gestione Separata professionisti with zero income pay nothing.

**Classification:** No INPS payment expected. Zero months credited.

### Example 6 -- Ravvedimento operoso (late payment with penalty)

**Input line:**
`20.08.2025 ; AGENZIA ENTRATE ; F24 ; RAVVEDIMENTO DPPI ; -8,750.00 ; EUR`

**Reasoning:**
Matches F24 + "RAVVEDIMENTO" + "DPPI". This is a late INPS acconto payment with ravvedimento operoso (voluntary correction). The amount includes the original contribution plus reduced penalties and interest. The contribution portion is deductible; penalties and interest are not.

**Classification:** EXCLUDE -- INPS late payment via ravvedimento. Flag for reviewer to split contribution (deductible in Quadro RP) from penalties/interest (not deductible).

---

## Section 5 -- Tier 1 rules

### Rule 1 -- Gestione Separata rate

| Category | Rate | Composition |
|---|---|---|
| No other pension coverage, not pensioned | 26.07% | 25.00% IVS + 0.72% maternita + 0.35% ISCRO |
| With other coverage or pensioned | 24.00% | 24.00% IVS only |

### Rule 2 -- Computation formula

```
INPS base = Net professional income (Quadro RE or LM) + rivalsa 4% received
INPS contribution = min(INPS_base, EUR 120,607) x aliquota
```

### Rule 3 -- Massimale and minimale

Massimale: EUR 120,607 -- no contributions on income above this. Minimale: EUR 18,555 -- income below this earns proportionally reduced pension credit months: `months = floor(income / EUR 18,555 x 12)`. There is NO mandatory minimum contribution in Gestione Separata.

### Rule 4 -- Rivalsa INPS 4%

Optional (facolta, not obligation). Charged to clients as separate invoice line. Subject to IVA. Subject to ritenuta d'acconto. INCLUDED in INPS computation base. The rivalsa is revenue, not a deduction.

### Rule 5 -- Payment schedule (acconto/saldo)

| Payment | % | Deadline |
|---|---|---|
| Saldo (prior year balance) | Residual | 30 June (or 30 July +0.40%) |
| Primo acconto | 40% of prior year total | 30 June (or 30 July +0.40%) |
| Secondo acconto | 60% of prior year total | 30 November |

Saldo and primo acconto can be paid in instalments (monthly, Jun-Nov, +0.33%/month). Secondo acconto CANNOT be paid in instalments.

### Rule 6 -- F24 codici tributo

DPPI = acconto Gestione Separata professionisti. DPP = saldo Gestione Separata professionisti.

### Rule 7 -- Tax deductibility (IRPEF)

INPS contributions are 100% deductible from reddito complessivo. Deducted in Quadro RP, Rigo RP21. Cash basis: contributions paid in year X deducted in year X. Under regime forfettario: INPS deducted from forfait income before flat rate applied.

### Rule 8 -- Quadro RR

INPS Gestione Separata contributions declared in Quadro RR, Sezione II of Modello Redditi PF. Deadline: 31 October (for prior year income).

### Rule 9 -- First year rule

No prior year base for acconti. Pay nothing during the year and settle full saldo by 30 June following year, OR make voluntary advance payments.

### Rule 10 -- INPS is computed on income BEFORE the INPS deduction

Circular dependency resolved: INPS base = gross professional income. INPS deduction reduces IRPEF, not the INPS base itself.

---

## Section 6 -- Tier 2 catalogue

### T2-1 -- Regime forfettario interaction

**Trigger:** Client is under regime forfettario.
**Issue:** INPS base = ricavi x coefficiente di redditivita. Same Gestione Separata rate applies. INPS deducted before flat tax.
**Action:** Flag for reviewer to confirm coefficient and verify forfettario conditions are met.

### T2-2 -- Rivalsa 4% dispute

**Trigger:** Client charged rivalsa but customer refuses to pay.
**Issue:** Rivalsa is facolta. If not charged or not received, professionista bears full INPS cost without recovery.
**Action:** Flag for reviewer if dispute affects contribution calculation.

### T2-3 -- ISCRO eligibility

**Trigger:** Client asks about ISCRO (income continuity benefit).
**Issue:** Complex income-based conditions: income must have dropped 70%+ compared to average of last 3 years.
**Action:** Escalate to Dottore Commercialista.

### T2-4 -- Collaboratori vs professionisti

**Trigger:** Unclear whether client is professionista con partita IVA or collaboratore.
**Issue:** Different rates and contribution splits (collaboratore: 2/3 committente + 1/3 collaboratore).
**Action:** Flag for reviewer.

### T2-5 -- Mid-year opening of partita IVA

**Trigger:** Client opened partita IVA mid-year.
**Issue:** Full rate applies on actual income. No pro-rata of rate. Minimale of EUR 18,555 still applies for full-year credit assessment.
**Action:** Confirm start date and first-year acconto strategy.

---

## Section 7 -- Excel working paper template

```
ITALY INPS GESTIONE SEPARATA -- WORKING PAPER
Client: [name]
Tax Year: [year]
Prepared: [date]

INPUT DATA
  Professional category:          [Gestione Separata / Cassa propria -> STOP]
  Other pension coverage:         [YES/NO]
  Pensioned:                      [YES/NO]
  Applicable rate:                [26.07% / 24.00%]
  Net professional income:        EUR [____]
  Rivalsa 4% received:            EUR [____]
  Tax regime:                     [Ordinario / Forfettario]

COMPUTATION
  INPS base (income + rivalsa):   EUR [____]
  Capped at massimale:            EUR [____]
  INPS contribution:              EUR [____]

PAYMENT SCHEDULE
  Prior year saldo:               EUR [____] (due 30 June)
  Primo acconto (40%):            EUR [____] (due 30 June)
  Secondo acconto (60%):          EUR [____] (due 30 November)

TAX DEDUCTIBILITY
  INPS in Quadro RP Rigo RP21:   EUR [____] (100% deductible)

MONTHS CREDITED
  Income vs minimale:             [____] months (floor(income / EUR 18,555 x 12))

REVIEWER FLAGS
  [List any Tier 2 flags]
```

---

## Section 8 -- Bank statement reading guide

### How INPS payments appear on Italian bank statements

**F24 payments (most common):**
- Description: "F24", "DELEGA F24", "AGENZIA DELLE ENTRATE", "AGENZIA ENTRATE"
- Timing: 30 June (saldo + primo acconto), 30 November (secondo acconto), or monthly if rateizzazione
- Amount: COMBINED with IRPEF, addizionali, IVA -- INPS is one component
- Cannot isolate INPS from bank statement -- need F24 receipt

**Direct INPS debits (uncommon for professionisti):**
- Description: "INPS" or "ISTITUTO NAZIONALE"
- Rare -- most professionisti pay via F24

**Key identification tips:**
1. F24 is the universal Italian tax payment form -- it combines ALL tax and contribution obligations
2. The bank statement shows a single F24 debit; the F24 receipt breaks down codici tributo (DPPI, DPP for Gestione Separata)
3. The secondo acconto (30 November) is typically a pure INPS + IRPEF acconto
4. Rateizzazione instalments (Jul-Nov) have progressively smaller amounts with interest
5. Ravvedimento operoso adds penalties -- flag for reviewer to split

---

## Section 9 -- Onboarding fallback

If the client provides only a bank statement:

1. **Identify F24 debits** -- dates around 30 June and 30 November are key
2. **Note combined nature:** "F24 payments combine INPS, IRPEF, addizionali, and IVA. The bank statement cannot isolate the INPS component."
3. **Request F24 receipts** -- these show codici tributo (DPPI/DPP for Gestione Separata)
4. **Check for rivalsa income** -- invoices received (credits) with "rivalsa" indicate INPS base includes 4% recovery
5. **Flag:** "INPS contribution estimate requires the F24 receipt or Modello Redditi PF Quadro RR. Bank statement alone is insufficient for accurate INPS classification."

---

## Section 10 -- Reference material

### Key figures (2025)

| Item | Value |
|---|---|
| Aliquota (no other coverage) | 26.07% |
| Aliquota (with coverage/pensioned) | 24.00% |
| Massimale | EUR 120,607 |
| Minimale (full year credit) | EUR 18,555 |
| Rivalsa | 4% (optional) |

### Casse professionali (all T3 -- escalate)

| Profession | Cassa |
|---|---|
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

**Test 1:** Professionista, no other coverage, income EUR 50,000, rivalsa EUR 2,000. -> Base: EUR 52,000. INPS: EUR 13,556.40.

**Test 2:** Professionista with employment (altra gestione), freelance income EUR 30,000. -> Rate 24.00%. INPS: EUR 7,200.

**Test 3:** Income EUR 150,000. -> Capped at EUR 120,607. INPS: EUR 31,442.24.

**Test 4:** Income EUR 0, partita IVA open. -> INPS: EUR 0. No minimale in Gestione Separata.

**Test 5:** Forfettario, ricavi EUR 60,000, coefficient 78%. -> Base: EUR 46,800. INPS: EUR 12,200.76. After deduction: EUR 34,599.24. Flat tax 5%: EUR 1,729.96.

**Test 6:** Pensioner, freelance EUR 20,000. -> Rate 24.00%. INPS: EUR 4,800.

**Test 7:** Income EUR 10,000. -> INPS: EUR 2,607. Months credited: 6.

### Prohibitions

- NEVER compute for cassa propria professions using Gestione Separata rates
- NEVER omit rivalsa 4% from the INPS base if received
- NEVER tell client rivalsa 4% is deductible -- it is revenue
- NEVER apply 26.07% to client with other mandatory coverage -- rate is 24.00%
- NEVER suggest there is a minimum contribution in Gestione Separata
- NEVER compute on income above massimale
- NEVER allow secondo acconto in instalments
- NEVER forget Quadro RR in Modello Redditi PF
- NEVER advise on ISCRO without escalating
- NEVER present figures as definitive

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
