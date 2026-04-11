---
name: it-income-tax
description: >
  Use this skill whenever asked about Italian income tax for self-employed individuals (lavoratori autonomi, liberi professionisti). Trigger on phrases like "Modello Redditi PF", "Quadro RE", "IRPEF", "redditi di lavoro autonomo", "imposta sul reddito Italy", "deduzioni", "detrazioni", "addizionale regionale", "addizionale comunale", "regime ordinario", "acconti IRPEF", "no tax area", "regime forfettario comparison", or any question about filing or computing income tax for an Italian freelancer or professional. Also trigger when preparing or reviewing a Modello Redditi PF, computing deductions, or advising on regime ordinario tax obligations. This skill covers progressive IRPEF brackets, deduzioni, detrazioni, addizionali, acconti, Quadro RE structure, rivalsa INPS, and penalties. ALWAYS read this skill before touching any Italian income tax work.
version: 1.0
jurisdiction: IT
tax_year: 2025
category: international
depends_on:
  - income-tax-workflow-base
---

# Italy Income Tax (Redditi PF) -- Self-Employed Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Italy |
| Jurisdiction Code | IT |
| Primary Legislation | TUIR -- Testo Unico delle Imposte sui Redditi (DPR 917/1986), Art. 53-54 (redditi di lavoro autonomo), Art. 11-13 (IRPEF rates and detrazioni) |
| Supporting Legislation | DPR 322/1998 (filing obligations); D.Lgs. 241/1997 (versamenti e compensazioni); L. 190/2014 Art. 1 cc. 54-89 (regime forfettario); D.Lgs. 446/1997 (IRAP) |
| Tax Authority | Agenzia delle Entrate |
| Filing Portal | Fisconline / Cassetto fiscale (agenziaentrate.gov.it) |
| Contributor | Open Accountants Community |
| Validated By | Pending -- requires sign-off by a qualified Italian dottore commercialista |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: IRPEF rate table application, Quadro RE structure, acconti schedule, addizionali rates, filing deadlines. Tier 2: mixed-use expense apportionment, detrazioni calculation, regime ordinario vs forfettario comparison, rivalsa INPS treatment. Tier 3: IRAP for professionals, international income, complex financial income, trust structures. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags and presents options. Qualified dottore commercialista must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate and document.

---

## Step 0: Client Onboarding Questions

Before computing any income tax figure, you MUST know:

1. **Regime fiscale** [T1] -- regime ordinario or regime forfettario. This skill covers regime ordinario only. If forfettario, see Step 3 for boundary explanation then STOP.
2. **Tipo di attivita** [T1] -- professione (lavoro autonomo / Quadro RE) or impresa (Quadro RF/RG). This skill covers lavoro autonomo only.
3. **Compensi lordi** [T1] -- total gross fees/compensation received or receivable in the year.
4. **Rivalsa INPS 4%** [T1] -- amount of 4% INPS contribution charged to clients (treated as revenue).
5. **Spese professionali** [T1/T2] -- nature and amount of each deductible expense (T2 for mixed-use items).
6. **Contributi previdenziali versati** [T1] -- INPS Gestione Separata, Cassa professionale contributions paid.
7. **Other income** [T1] -- redditi da lavoro dipendente, redditi fondiari, redditi di capitale, redditi diversi.
8. **Regione e Comune di residenza** [T1] -- determines addizionale regionale and comunale rates.
9. **Acconti gia versati** [T1] -- IRPEF advance payments already made during the year.
10. **Ritenute d'acconto subite** [T1] -- 20% withholding tax deducted by clients on fees paid.

**If regime fiscale is unknown, STOP. Do not compute. The regime determines the entire tax treatment.**

---

## Step 1: Regime Forfettario -- Why It Is Out of Scope [T1]

**Legislation:** L. 190/2014, Art. 1, commi 54-89 (as amended by L. 197/2022)

| Parameter | Value |
|-----------|-------|
| Revenue ceiling | EUR 85,000 (ricavi/compensi) |
| Flat tax rate | 15% (or 5% for first 5 years if qualifying startup) |
| Profitability coefficient | Varies by ATECO code (e.g., 78% for professional services) |
| IVA | Exempt -- no IVA charged, no input IVA deducted |
| IRAP | Exempt |
| Addizionali | Exempt |
| Ritenute d'acconto | Not applied -- forfettario invoices carry no withholding |

**Why out of scope:** The forfettario is a completely separate system. There are no progressive brackets, no detrazioni, no addizionali. If the client is under forfettario, this skill does not apply. The computation is simply: compensi x coefficiente di redditivita x 15% (or 5%). This is a [T1] one-line calculation that does not require this skill.

**When to mention forfettario:** Only when comparing with regime ordinario to help the client decide. If compensi are under EUR 85,000 and the client has low real expenses, forfettario is almost always more favourable. [T2] Flag for reviewer to confirm.

---

## Step 2: IRPEF Progressive Brackets [T1]

**Legislation:** TUIR Art. 11 -- Aliquote IRPEF 2025 (as confirmed by Legge di Bilancio 2025, structural reform from 4 to 3 brackets)

| Scaglione di reddito imponibile (EUR) | Aliquota | Imposta progressiva cumulata |
|----------------------------------------|----------|------------------------------|
| Fino a EUR 28,000 | 23% | EUR 6,440 |
| Da EUR 28,001 a EUR 50,000 | 35% | EUR 14,140 |
| Oltre EUR 50,000 | 43% | -- |

**Note (2025):** The 2025 Budget Law confirmed the structural reduction from 4 to 3 brackets. The former 25% bracket (EUR 15,001-28,000) was merged into the 23% bracket. For 2026, the second bracket rate drops from 35% to 33%.

**NEVER compute IRPEF directly in Claude -- pass reddito imponibile to the deterministic engine to apply the brackets.**

---

## Step 3: Quadro RE -- Redditi di Lavoro Autonomo [T1]

**Legislation:** TUIR Art. 53, 54; Istruzioni Modello Redditi PF

| Rigo | Description | How to Populate |
|------|-------------|-----------------|
| RE1 | Ammontare lordo dei compensi | Total gross fees received/receivable |
| RE2 | Rivalsa INPS 4% | Amount of 4% INPS charged to clients (included in revenue) |
| RE3 | Compensi lordi totali | RE1 + RE2 |
| RE4-RE19 | Spese deducibili | Individual expense lines (see Step 4) |
| RE20 | Totale spese | Sum of RE4-RE19 |
| RE21 | Differenza (compensi - spese) | RE3 - RE20 |
| RE22 | Reddito (o perdita) | Final net professional income or loss |
| RE23 | Ritenute d'acconto | 20% withholding taxes suffered on fees |

### Rivalsa INPS 4% [T1]

**Rule:** Self-employed professionals enrolled in INPS Gestione Separata may charge a 4% rivalsa contribution to clients. This rivalsa is added to invoices on top of fees. It is treated as taxable revenue (included in RE2) and is also subject to IVA. The corresponding INPS contribution paid is deductible as a deduzione dal reddito complessivo (not as a professional expense).

---

## Step 4: Deductible Professional Expenses (Spese Deducibili) [T1/T2]

**Legislation:** TUIR Art. 54

### Fully Deductible [T1]

| Spesa | Treatment |
|-------|-----------|
| Affitto studio/ufficio (dedicato) | Fully deductible |
| Utenze studio dedicato (luce, gas, internet) | Fully deductible |
| Assicurazione professionale (RC professionale) | Fully deductible |
| Compensi a collaboratori / dipendenti | Fully deductible |
| Spese per prestazioni di terzi (subappalto) | Fully deductible |
| Materiale di consumo / cancelleria | Fully deductible |
| Formazione professionale | Deductible up to EUR 10,000/year |
| Software e abbonamenti professionali | Fully deductible |
| Contributi a ordini professionali | Fully deductible |

### Partially Deductible [T2]

| Spesa | Limite | Treatment |
|-------|--------|-----------|
| Telefono / mobile | 80% deductible | Art. 54, comma 3-bis |
| Autovettura (costi di gestione) | 20% deductible (1 veicolo max) | Art. 164 TUIR |
| Ammortamento autovettura | 20% of max EUR 18,076 cost | Art. 164 TUIR -- max deductible depreciation base |
| Alberghi e ristoranti | 75% deductible, capped at 2% of compensi | Art. 54, comma 5 |
| Spese di rappresentanza | 1% of compensi | Art. 54, comma 5 |
| Uso promiscuo immobile | 50% of expenses | If no dedicated studio |

### NOT Deductible [T1]

| Spesa | Reason |
|-------|--------|
| IRPEF | Tax on income cannot deduct itself |
| Sanzioni e penalita | Public policy |
| Spese personali / familiari | Not professional |
| IRAP (if applicable) | Not deductible against IRPEF (with limited exceptions) |

---

## Step 5: Deduzioni vs Detrazioni [T1/T2]

**Legislation:** TUIR Art. 10 (deduzioni), Art. 12-16 (detrazioni)

### Deduzioni dal Reddito Complessivo (reduce taxable income) [T1]

| Deduzione | Treatment |
|-----------|-----------|
| Contributi previdenziali obbligatori (INPS, Cassa) | Fully deductible without ceiling |
| Contributi previdenziali volontari | Deductible within specific ceilings |
| Assegni al coniuge (ex-spouse maintenance) | Deductible (not child maintenance) |
| Spese mediche per disabili | Deductible |
| Contributi a fondi pensione complementare | Max EUR 5,164.57/year |

### Detrazioni d'Imposta (reduce tax payable) [T1/T2]

| Detrazione | Tasso | Condizioni |
|------------|-------|------------|
| Detrazione lavoro autonomo | EUR 1,265 max | For reddito up to EUR 5,500; decreasing above |
| Spese sanitarie | 19% over EUR 129.11 franchigia | Must be traceable payments (no cash) |
| Interessi passivi mutuo prima casa | 19% up to EUR 4,000 | Primary residence only |
| Spese istruzione | 19% up to EUR 800/child | Kindergarten through university |
| Premi assicurazione vita/infortuni | 19% up to EUR 530 | Life/accident insurance |
| Spese funebri | 19% up to EUR 1,550/event | |
| Erogazioni liberali (onlus) | 26% or 30% depending on entity | |
| Spese ristrutturazione edilizia | 50% in 10 years (Bonus Casa) | Subject to legislative changes |
| Superbonus residuo | 65% (2025 rate for condominiums) | [T3] -- highly complex |

### No Tax Area [T1]

| Categoria | Soglia reddito | Detrazione massima |
|-----------|----------------|--------------------|
| Lavoratori autonomi | EUR 5,500 | EUR 1,265 |
| Lavoratori dipendenti | EUR 8,500 | EUR 1,955 |
| Pensionati | EUR 8,500 | EUR 1,955 |

For self-employed: if reddito complessivo does not exceed EUR 5,500, the detrazione of EUR 1,265 fully offsets the IRPEF (23% x EUR 5,500 = EUR 1,265), creating a de facto no tax area.

---

## Step 6: Addizionale Regionale e Comunale [T1]

**Legislation:** D.Lgs. 446/1997 (regionale); D.Lgs. 360/1998 (comunale)

### Addizionale Regionale [T1]

| Range | Note |
|-------|------|
| 1.23% -- 3.33% | Varies by region. Base rate is 1.23%. Many regions apply higher rates. |

**Common regional rates (2025, indicative):**

| Regione | Aliquota |
|---------|----------|
| Lombardia | 1.23% -- 1.74% (progressive) |
| Lazio | 1.73% -- 3.33% (progressive) |
| Campania | 2.03% -- 3.33% (progressive) |
| Veneto | 1.23% |
| Piemonte | 1.62% -- 3.33% (progressive) |

**Rule:** The addizionale regionale is calculated on the same reddito imponibile as IRPEF, AFTER deduzioni but BEFORE detrazioni. Check the specific region's delibera for the current rates.

### Addizionale Comunale [T1]

| Range | Note |
|-------|------|
| 0% -- 0.9% | Set by each Comune. Some Comuni apply 0%. |

**Rule:** Same base as addizionale regionale. Check the specific Comune's delibera on the MEF website (www1.finanze.gov.it).

[T2] Flag for reviewer: always confirm regione and comune rates from the official delibere, as they change annually.

---

## Step 7: Acconti IRPEF [T1]

**Legislation:** DPR 917/1986; D.Lgs. 241/1997; Art. 17 DPR 435/2001

### Acconti Schedule

| Acconto | Percentuale | Scadenza |
|---------|-------------|----------|
| Primo acconto | 40% of prior year IRPEF | 30 June (or 31 July with 0.4% interest) |
| Secondo acconto | 60% of prior year IRPEF | 30 November |
| Total acconti | 100% of prior year IRPEF | -- |

### Rules [T1]

- Acconti are due only if the prior year IRPEF (after detrazioni, deduzioni, and ritenute) exceeds EUR 51.65
- If the acconto totale does not exceed EUR 257.52, it is paid in a single instalment by 30 November
- Acconti can be reduced using the metodo previsionale if current year income is expected to be lower [T2]
- Acconti are paid via Modello F24 using codice tributo 4033 (primo) and 4034 (secondo)

### Saldo and Acconti Payment Flow

| Payment | Codice Tributo | Scadenza |
|---------|----------------|----------|
| Saldo IRPEF anno precedente | 4001 | 30 June |
| Primo acconto anno corrente | 4033 | 30 June |
| Secondo acconto anno corrente | 4034 | 30 November |
| Addizionale regionale saldo | 3801 | 30 June |
| Addizionale comunale saldo | 3844 | 30 June |
| Addizionale comunale acconto | 3843 | 30 June (30%) + 30 November (70%) |

---

## Step 8: Filing Deadlines [T1]

**Legislation:** DPR 322/1998; Art. 2 DPR 435/2001

| Filing / Payment | Deadline |
|-----------------|----------|
| Modello Redditi PF (telematico) | 31 October of the following year |
| Modello 730 (for employees/pensioners, not typical for autonomi) | 30 September |
| Saldo IRPEF + primo acconto | 30 June (or 31 July with 0.4% surcharge) |
| Secondo acconto IRPEF | 30 November |
| Certificazione Unica (CU) received from clients | 16 March (issued by the client/withholding agent) |
| Dichiarazione IVA annuale | 30 April |

---

## Step 9: Penalties [T1]

**Legislation:** D.Lgs. 472/1997; D.Lgs. 471/1997

| Offence | Penalty |
|---------|---------|
| Omessa dichiarazione (non-filing) | 120% -- 240% of tax due (minimum EUR 250) |
| Dichiarazione infedele (inaccurate return) | 90% -- 180% of additional tax due |
| Tardiva dichiarazione (late filing within 90 days) | EUR 25 (1/10 of minimum EUR 250, with ravvedimento) |
| Omesso versamento (late payment) | 30% of unpaid tax (reduced to 15% within 90 days) |
| Interessi legali | Variable rate set annually (2.5% for 2025) |
| Ravvedimento operoso (voluntary correction) | Reduced penalties: 1/10 to 1/5 of base penalty depending on timing |

**Ravvedimento operoso:** Italy allows voluntary correction with significantly reduced penalties. The earlier the correction, the lower the surcharge. [T1] Always calculate and present the ravvedimento cost when a deadline has been missed.

---

## Step 10: Record Keeping [T1]

**Legislation:** DPR 600/1973, Art. 19; TUIR Art. 54

| Requirement | Detail |
|-------------|--------|
| Minimum retention period | 5 years from the filing deadline (10 years if litigation) |
| What to keep | All invoices issued and received, bank statements, contracts, Modello Redditi and attachments, F24 payment receipts |
| Registri obbligatori (regime ordinario) | Registro IVA acquisti, Registro IVA vendite, Registro incassi e pagamenti |
| Fatturazione elettronica | Mandatory since 2024 for all VAT subjects (including ex-forfettari above EUR 25K) |
| Conservazione sostitutiva | Digital archiving must comply with CAD (Codice dell'Amministrazione Digitale) |

---

## Step 11: Edge Case Registry

### EC1 -- Rivalsa INPS 4% omitted from revenue [T1]
**Situation:** Client invoices EUR 10,000 in fees plus EUR 400 rivalsa INPS 4%. Client reports only EUR 10,000 as compensi on Quadro RE.
**Resolution:** The rivalsa INPS 4% IS taxable revenue. RE1 = EUR 10,000, RE2 = EUR 400, RE3 = EUR 10,400. The EUR 400 must be included.

### EC2 -- Vehicle expenses exceeding 20% limit [T1]
**Situation:** Client claims EUR 8,000 in car expenses as fully deductible.
**Resolution:** Only 20% is deductible = EUR 1,600. For depreciation, the depreciable base is capped at EUR 18,076, and only 20% of the depreciation is deductible. One vehicle maximum.

### EC3 -- Restaurant expenses exceeding 2% cap [T2]
**Situation:** Client has EUR 60,000 compensi and claims EUR 3,000 in restaurant expenses.
**Resolution:** Restaurant expenses are 75% deductible = EUR 2,250. But this is further capped at 2% of compensi = EUR 1,200. Deductible amount = EUR 1,200. [T2] Flag for reviewer to confirm compensi figure used for the cap.

### EC4 -- Forfettario ceiling breached mid-year [T2]
**Situation:** Forfettario client has already earned EUR 80,000 by September and expects to exceed EUR 85,000 by year end.
**Resolution:** If compensi exceed EUR 85,000 in the year, the forfettario regime ceases to apply from the FOLLOWING year (not mid-year). If they exceed EUR 100,000, exit is immediate and IVA applies from the invoice that breaches EUR 100,000. [T2] Flag for reviewer: confirm threshold and transition rules.

### EC5 -- Ritenuta d'acconto on forfettario invoice [T1]
**Situation:** A client applies the 20% ritenuta d'acconto to a forfettario professional's invoice.
**Resolution:** INCORRECT. Forfettario professionals are exempt from ritenuta d'acconto. The invoice should explicitly state the exemption ("operazione effettuata ai sensi dell'art. 1, commi 54-89, L. 190/2014 -- non soggetta a ritenuta"). Correct with the client.

### EC6 -- Addizionale regionale on zero IRPEF [T1]
**Situation:** Client's reddito imponibile is EUR 4,000, resulting in zero IRPEF after detrazioni (no tax area).
**Resolution:** If IRPEF is zero, addizionale regionale and comunale are also zero. The addizionali are not independent taxes -- they depend on a positive IRPEF liability.

### EC7 -- Acconti reduced using metodo previsionale, but income increases [T2]
**Situation:** Client reduced acconti expecting lower income, but actual income exceeded prior year.
**Resolution:** If acconti paid are less than what would have been due based on actual income, a sanzione of 30% applies to the underpayment. Ravvedimento operoso can reduce this. [T2] Flag for reviewer: calculate the shortfall and ravvedimento cost.

### EC8 -- Spese sanitarie paid in cash [T1]
**Situation:** Client claims EUR 2,000 in medical expenses, but EUR 800 was paid in cash.
**Resolution:** Since 2020, the 19% detrazione for most expenses (including medical) requires traceable payment (bonifico, carta, assegno). Cash payments for medical expenses are deductible ONLY for purchases at pharmacies and for medical devices. The EUR 800 cash portion paid elsewhere is NOT deductible. Deductible = EUR 1,200.

### EC9 -- Double counting of INPS contributions [T1]
**Situation:** Client deducts INPS contributions both as a professional expense in Quadro RE and as a deduzione dal reddito complessivo.
**Resolution:** INPS contributions are deducted ONLY as a deduzione dal reddito complessivo (Quadro RP / Quadro E), NOT as a professional expense in Quadro RE. Remove from RE and ensure they appear in the deduzioni section.

### EC10 -- First year, no prior year for acconti [T1]
**Situation:** New professional registered partita IVA in 2025. No prior year Redditi PF exists.
**Resolution:** No acconti are due for the first year (no base year). Full IRPEF is paid as saldo by 30 June 2026 (or 31 July with 0.4%). From the second year, acconti apply based on the first year's actual liability.

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
Action Required: Qualified dottore commercialista must confirm before filing.
```

When Claude identifies a [T3] situation:

```
ESCALATION REQUIRED
Tier: T3
Client: [name]
Situation: [description]
Issue: [outside skill scope]
Action Required: Do not advise. Refer to dottore commercialista. Document gap.
```

---

## Step 13: Test Suite

### Test 1 -- Standard self-employed professional, mid-range income
**Input:** Compensi EUR 60,000, rivalsa INPS EUR 2,400, spese deducibili EUR 15,000, INPS Gestione Separata paid EUR 7,800, ritenute d'acconto subite EUR 12,000. Residente in Lombardia (addizionale 1.58%), Comune di Milano (addizionale 0.8%). No other income.
**Expected output:** RE3 = EUR 62,400. RE20 = EUR 15,000. RE22 = EUR 47,400. Reddito complessivo = EUR 47,400. Deduzioni (INPS) = EUR 7,800. Reddito imponibile = EUR 39,600. IRPEF: EUR 6,440 + (EUR 39,600 - EUR 28,000) x 35% = EUR 6,440 + EUR 4,060 = EUR 10,500. Addizionale regionale: EUR 39,600 x 1.58% = EUR 626. Addizionale comunale: EUR 39,600 x 0.8% = EUR 317. Total tax = EUR 11,443. Less ritenute EUR 12,000. Refund = EUR 557.

### Test 2 -- Low income, no tax area applies
**Input:** Compensi EUR 5,000, rivalsa INPS EUR 200, no expenses. INPS paid EUR 1,300. Reddito imponibile = EUR 5,200 - EUR 1,300 = EUR 3,900.
**Expected output:** IRPEF lorda = EUR 3,900 x 23% = EUR 897. Detrazione lavoro autonomo = EUR 1,265 (at this income level). EUR 1,265 > EUR 897, so IRPEF netta = EUR 0. No addizionali due. No tax payable.

### Test 3 -- High income, top bracket
**Input:** Compensi EUR 150,000, rivalsa EUR 6,000, spese EUR 30,000, INPS EUR 15,000. Reddito imponibile = EUR 126,000 - EUR 15,000 = EUR 111,000. Residente in Lazio (3.33%), Comune di Roma (0.9%).
**Expected output:** IRPEF: EUR 6,440 + EUR 7,700 + (EUR 111,000 - EUR 50,000) x 43% = EUR 6,440 + EUR 7,700 + EUR 26,230 = EUR 40,370. Addizionale regionale: EUR 111,000 x 3.33% = EUR 3,696. Addizionale comunale: EUR 111,000 x 0.9% = EUR 999. Total = EUR 45,065.

### Test 4 -- Vehicle expense cap correctly applied
**Input:** Client claims EUR 12,000 in car expenses (fuel, insurance, maintenance). Compensi EUR 80,000.
**Expected output:** Deductible = EUR 12,000 x 20% = EUR 2,400. The remaining EUR 9,600 is NOT deductible.

### Test 5 -- Acconti calculation for following year
**Input:** 2025 IRPEF netta (after detrazioni and ritenute) = EUR 8,000.
**Expected output:** Primo acconto 2026 = EUR 8,000 x 40% = EUR 3,200, due 30 June 2026. Secondo acconto 2026 = EUR 8,000 x 60% = EUR 4,800, due 30 November 2026. Total acconti = EUR 8,000.

### Test 6 -- Rivalsa INPS correctly included in revenue
**Input:** Fees invoiced EUR 50,000. Rivalsa INPS 4% = EUR 2,000. Client reports only EUR 50,000.
**Expected output:** INCORRECT. RE3 must be EUR 52,000 (EUR 50,000 + EUR 2,000). The rivalsa is taxable revenue.

### Test 7 -- Ravvedimento operoso for late payment
**Input:** Saldo IRPEF EUR 5,000 due 30 June, paid 15 September (77 days late).
**Expected output:** Sanzione base = 15% (within 90 days). Ravvedimento (within 90 days) = 1/8 of 15% = 1.875%. Sanzione = EUR 5,000 x 1.875% = EUR 94. Interessi legali = EUR 5,000 x 2.5% x 77/365 = EUR 26. Total extra cost = EUR 120 approximately.

---

## PROHIBITIONS

- NEVER compute IRPEF without knowing the regime fiscale (ordinario vs forfettario)
- NEVER compute IRPEF directly -- pass reddito imponibile to the deterministic engine
- NEVER omit rivalsa INPS 4% from taxable revenue in Quadro RE
- NEVER deduct INPS contributions as a professional expense in Quadro RE -- they are deduzioni dal reddito complessivo
- NEVER apply addizionali without confirming the specific regione and comune rates
- NEVER deduct vehicle expenses at more than 20%
- NEVER treat detrazioni as deduzioni or vice versa -- they operate at different stages of the computation
- NEVER allow cash-paid medical expenses as detrazioni (except pharmacy and medical devices)
- NEVER advise on regime forfettario computations within this skill -- explain and redirect
- NEVER present tax calculations as definitive -- always label as estimated and direct client to their dottore commercialista for confirmation
- NEVER ignore the distinction between Modello 730 (employees) and Modello Redditi PF (self-employed)

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a dottore commercialista, ragioniere commercialista, or consulente del lavoro licensed in Italy) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
