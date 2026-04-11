---
name: cl-income-tax
description: Use this skill whenever asked about Chilean income tax for self-employed individuals. Trigger on phrases like "Impuesto Global Complementario", "Operación Renta", "boleta de honorarios", "trabajador independiente", "PPM", "retención honorarios", "gastos presuntos", "segunda categoría", "Formulario 22", or any question about filing or computing income tax for a self-employed or independent worker in Chile. This skill covers Impuesto Global Complementario (progressive 0-40%), honorarios withholding, PPM credits, gastos efectivos vs presuntos, cotizaciones previsionales, and SII filing. ALWAYS read this skill before touching any Chilean income tax work.
---

# Chile Income Tax (Renta) -- Self-Employed Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Chile |
| Jurisdiction Code | CL |
| Primary Legislation | Decreto Ley 824 (Ley sobre Impuesto a la Renta) |
| Supporting Legislation | Ley 21.133 (cotizaciones previsionales obligatorias para independientes); Circular SII 67/2025; Código Tributario |
| Tax Authority | Servicio de Impuestos Internos (SII) |
| Filing Portal | SII Portal (www.sii.cl) |
| Contributor | Open Accountants Community |
| Validated By | Pending -- requires sign-off by a Chilean Contador Auditor |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: IGC rate table, UTA values, withholding rate, PPM credit, gastos presuntos cap. Tier 2: gastos efectivos documentation, mixed-use expense apportionment, cotizaciones previsionales deductions, voluntary APV contributions. Tier 3: foreign-source income, tax treaties, FUT/RAI, corporate reorganisations. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags and presents options. Contador Auditor must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate and document.

---

## Step 0: Client Onboarding Questions

Before computing any income tax figure, you MUST know:

1. **Type of independent work** [T1] -- trabajador a honorarios (boletas), empresario individual, sociedad
2. **Gross annual honorarios** [T1] -- total bruto from boletas de honorarios issued
3. **Expense method** [T1] -- gastos efectivos (actual documented expenses) or gastos presuntos (deemed 30%)
4. **Cotizaciones previsionales paid** [T1] -- AFP, salud (Fonasa/Isapre), seguro de invalidez
5. **PPM (Pagos Provisionales Mensuales) paid/withheld** [T1] -- withholding on boletas during the year
6. **Other income sources** [T1] -- employment (2da categoría), rental, dividends, interest
7. **APV contributions (Ahorro Previsional Voluntario)** [T2] -- voluntary retirement savings (Régimen A or B)
8. **RUT** [T1] -- tax identification number

**If expense method is unknown, STOP. The choice between gastos efectivos and presuntos fundamentally changes the computation.**

---

## Step 1: Determine Applicable Rate Table [T1]

**Legislation:** DL 824, art. 52 (Impuesto Global Complementario)

### Impuesto Global Complementario (IGC) -- Tax Year 2025 (Año Tributario 2025)

The IGC uses **UTA (Unidad Tributaria Anual)** as the reference unit. The UTA value is adjusted monthly by the SII. As of December 2024, UTA was approximately CLP 807,528. Verify the applicable UTA at www.sii.cl.

| Taxable Income (UTA) | Taxable Income (CLP, approx at UTA 807,528) | Rate | Amount to Deduct (UTA) |
|----------------------|---------------------------------------------|------|----------------------|
| 0 -- 13.5 UTA | 0 -- 10,901,628 | Exempt (0%) | -- |
| 13.5 -- 30 UTA | 10,901,629 -- 24,225,840 | 4% | 0.54 UTA |
| 30 -- 50 UTA | 24,225,841 -- 40,376,400 | 8% | 1.74 UTA |
| 50 -- 70 UTA | 40,376,401 -- 56,526,960 | 13.5% | 4.49 UTA |
| 70 -- 90 UTA | 56,526,961 -- 72,677,520 | 23% | 11.14 UTA |
| 90 -- 120 UTA | 72,677,521 -- 96,903,360 | 30.4% | 17.80 UTA |
| 120 -- 310 UTA | 96,903,361 -- 250,333,680 | 35% | 23.26 UTA |
| 310+ UTA | 250,333,681+ | 40% | 38.76 UTA |

**WARNING: UTA values change monthly. Always verify the December UTA value of the tax year at www.sii.cl before computing. The CLP amounts above are illustrative.**

---

## Step 2: Honorarios Withholding (Retención) [T1]

**Legislation:** DL 824, art. 74 No. 2; Ley 21.133

### Withholding Rate Phase-In Schedule [T1]

| Year | Withholding Rate |
|------|-----------------|
| 2023 | 13% |
| 2024 | 13.75% |
| 2025 | 14.5% |
| 2026 | 15.25% |
| 2027 | 16% |
| 2028+ | 17% |

**For boletas de honorarios issued in 2025, the withholding rate is 14.5%.**

### How It Works [T1]

- When a self-employed worker issues a boleta de honorarios, the recipient withholds 14.5% (2025) and remits to SII
- This withholding covers both income tax (PPM) and mandatory cotizaciones previsionales
- The withholding is a credit (PPM) against the final IGC liability in the annual Operación Renta
- If the worker issues boletas to individuals (not companies), the worker must self-withhold and pay via Formulario 29

---

## Step 3: Gastos Efectivos vs Gastos Presuntos [T1]

**Legislation:** DL 824, art. 50

### Option 1: Gastos Presuntos (Deemed Expenses) [T1]

| Rule | Detail |
|------|--------|
| Rate | 30% of gross honorarios |
| Annual cap | 15 UTA (approximately CLP 12,112,920 at UTA 807,528) |
| Documentation | No receipts required |
| Who can use | Any trabajador a honorarios |

### Option 2: Gastos Efectivos (Actual Expenses) [T2]

| Rule | Detail |
|------|--------|
| Rate | Actual documented expenses |
| Cap | No cap -- but must pass the "necessary for income production" test |
| Documentation | Full receipts, facturas, boletas required |
| Who can use | Any trabajador a honorarios (must elect at filing time) |

### Decision Rule [T2]

- If actual expenses < 30% of gross (or < 15 UTA), use gastos presuntos (simpler, less audit risk)
- If actual expenses > 30% of gross AND > 15 UTA, gastos efectivos may be more favourable
- [T2] Flag for reviewer: confirm that documented expenses are genuine, necessary, and properly supported

---

## Step 4: Computation Structure [T1]

**Legislation:** DL 824, arts. 50, 52, 54

| Step | Description |
|------|-------------|
| A | Honorarios brutos (gross boleta income) |
| B | Less: Cotizaciones previsionales obligatorias (deducted from withholding) |
| C | Less: Gastos (presuntos 30% capped at 15 UTA, or efectivos) |
| D | Renta neta (A minus B minus C) |
| E | Add: Other income (employment, rental, dividends, interest) |
| F | Renta neta global (D plus E) |
| G | Less: APV Régimen A deduction (if applicable) |
| H | Base imponible IGC |
| I | Apply IGC progressive table to H |
| J | Less: PPM credit (withholdings on boletas during the year) |
| K | Less: Other credits (education, donations, etc.) |
| L | Tax due / (refund) |

---

## Step 5: Cotizaciones Previsionales (Mandatory Social Security) [T1]

**Legislation:** Ley 21.133

### Mandatory Contributions from Boleta Withholding [T1]

| Contribution | Approximate Rate | Notes |
|-------------|-----------------|-------|
| AFP (pension) | ~10.69% + commission (~11.5-12.5% total) | On 80% of gross honorarios (renta imponible) |
| Salud (Fonasa 7% or Isapre plan) | 7% minimum | On 80% of gross honorarios |
| Seguro de Invalidez y Sobrevivencia (SIS) | ~1.85% | On 80% of gross honorarios |
| Seguro de Accidentes del Trabajo (ATEP) | ~0.93% | On 80% of gross honorarios |

### Key Rules [T1]

- The renta imponible for cotizaciones = 80% of gross honorarios
- Subject to a monthly cap (tope imponible) = 81.6 UF for AFP / 113.5 UF for salud (verify current UF)
- Cotizaciones are deducted from the withholding before PPM credit is calculated
- Self-employed workers may opt out of health and pension coverage only if they have coverage from another source (e.g., employment) -- phase-in restrictions apply

---

## Step 6: PPM Credits [T1]

**Legislation:** DL 824, art. 84

| Rule | Detail |
|------|--------|
| PPM source | The portion of boleta withholding remaining after cotizaciones |
| Treatment | Credit against final IGC in Operación Renta |
| Excess PPM | Refunded to the taxpayer (devolución) |

**If the taxpayer's IGC liability is less than the total PPM withheld, the difference is refunded. Many lower-income workers a honorarios receive refunds during Operación Renta.**

---

## Step 7: Filing and Deadlines [T1]

**Legislation:** Código Tributario; SII calendar

| Filing / Payment | Deadline |
|-----------------|----------|
| Operación Renta (Formulario 22, annual return) | April of the following year (typically April 1-30) |
| Formulario 29 (monthly, if self-withholding) | 12th of following month |
| Cotizaciones previsionales (monthly) | By employer/payer or via previred.com |
| Declaraciones juradas (informational returns) | March (before Operación Renta) |

### Filing Method [T1]

- Via SII portal (www.sii.cl) -- Operación Renta
- SII pre-populates much of the F22 from boletas electrónicas and employer information
- Taxpayer reviews, corrects, and submits
- Refunds typically paid within 30-60 days of filing

---

## Step 8: Penalties [T1]

**Legislation:** Código Tributario, arts. 97, 200

| Offence | Penalty |
|---------|---------|
| Late filing of F22 | 10% of tax due + 2% additional per month (up to 30%) |
| Late payment | Interest at 1.5% per month on unpaid tax |
| Failure to issue boleta | 50-500% of the amount of the boleta |
| Incorrect return (unintentional) | 5-20% of the tax difference |
| Tax evasion (intentional) | 50-300% of evaded tax + potential criminal prosecution |
| Failure to keep records | 1 UTA to 1 UTA per infraction |

---

## Step 9: Record Keeping [T1]

**Legislation:** Código Tributario, art. 17

| Requirement | Detail |
|-------------|--------|
| Minimum retention | 6 years from the tax year |
| What to keep | Boletas de honorarios (electronic), facturas, receipts, bank statements, contracts |
| Format | Electronic (boleta electrónica is mandatory since 2021) |
| Boletas electrónicas | Issued via SII portal -- all records maintained electronically |

---

## Step 10: Edge Case Registry

### EC1 -- Gastos presuntos exceed 15 UTA cap [T1]
**Situation:** Client has gross honorarios of CLP 80,000,000. Claims 30% = CLP 24,000,000 as gastos presuntos.
**Resolution:** Cap at 15 UTA (approx CLP 12,112,920). Deduction = CLP 12,112,920, not CLP 24,000,000.

### EC2 -- Worker opts out of cotizaciones but has no other coverage [T1]
**Situation:** Trabajador a honorarios wants to opt out of AFP and salud to keep more cash.
**Resolution:** Under Ley 21.133 phase-in, workers must contribute unless they have coverage from another source (employment). Verify eligibility to opt out. If not eligible, cotizaciones are mandatory and deducted from withholding.

### EC3 -- Mixed income (employment + honorarios) [T2]
**Situation:** Client has employment income of CLP 30,000,000 and honorarios of CLP 15,000,000.
**Resolution:** Both incomes aggregate in the IGC (renta neta global). Employment income goes in as sueldo bruto less social security. Honorarios go in as net after gastos and cotizaciones. The combined amount determines the IGC bracket. PPM from both sources are credits. [T2] Flag for reviewer to confirm aggregation.

### EC4 -- PPM excess leads to large refund [T1]
**Situation:** Low-income worker with CLP 5,000,000 gross honorarios. Withholding 14.5% = CLP 725,000. After cotizaciones, PPM credit of ~CLP 300,000. IGC = 0 (below 13.5 UTA).
**Resolution:** Full PPM is refunded. Tax = CLP 0. Refund = PPM amount (~CLP 300,000).

### EC5 -- Gastos efectivos with inadequate documentation [T2]
**Situation:** Client elects gastos efectivos claiming CLP 10,000,000 but only has receipts for CLP 6,000,000.
**Resolution:** Only CLP 6,000,000 is deductible. Undocumented CLP 4,000,000 must be removed. SII may audit and reject unsupported expenses. [T2] Flag for reviewer.

### EC6 -- APV Régimen A vs Régimen B confusion [T2]
**Situation:** Client contributes to APV and wants to know tax treatment.
**Resolution:** Régimen A: contribution is deductible from taxable income (reduces IGC now, taxed on withdrawal). Régimen B: no deduction now, but 15% bonus from state on withdrawal. [T2] Flag for reviewer to confirm which regime is more favourable given client's marginal rate.

### EC7 -- Boleta issued to individual (no company withholding) [T1]
**Situation:** Self-employed worker issues boleta to an individual (persona natural without accounting books). No withholding by recipient.
**Resolution:** The worker must self-withhold via Formulario 29 (monthly). The 14.5% must be paid by the worker by the 12th of the following month. Failure = penalties.

### EC8 -- UTA value applied incorrectly [T1]
**Situation:** Client uses January UTA for Operación Renta calculation.
**Resolution:** INCORRECT. The IGC table uses the December UTA of the tax year (e.g., December 2024 UTA for Año Tributario 2025). Always use the December value.

---

## Step 11: Reviewer Escalation Protocol

When Claude identifies a [T2] situation:

```
REVIEWER FLAG
Tier: T2
Client: [name]
Situation: [description]
Issue: [what is ambiguous]
Options: [possible treatments]
Recommended: [most likely correct treatment and why]
Action Required: Contador Auditor must confirm before filing.
```

When Claude identifies a [T3] situation:

```
ESCALATION REQUIRED
Tier: T3
Client: [name]
Situation: [description]
Issue: [outside skill scope]
Action Required: Do not advise. Refer to Contador Auditor. Document gap.
```

---

## Step 12: Test Suite

### Test 1 -- Standard honorarios with gastos presuntos
**Input:** Gross honorarios CLP 25,000,000. Gastos presuntos 30%. Cotizaciones CLP 2,500,000. No other income.
**Expected output:** Gastos = 30% x 25,000,000 = 7,500,000 (below 15 UTA cap). Renta neta = 25,000,000 - 2,500,000 - 7,500,000 = CLP 15,000,000. At UTA ~807,528, this is ~18.6 UTA. IGC: first 13.5 UTA exempt. 13.5-18.6 UTA at 4%. Tax ~= 4% x (15,000,000 - 10,901,628) - rebate = small amount. PPM credit likely covers it -- probable refund.

### Test 2 -- High earner with gastos efectivos
**Input:** Gross honorarios CLP 120,000,000. Gastos efectivos CLP 40,000,000 (documented). Cotizaciones at tope imponible. No other income.
**Expected output:** Renta neta = 120,000,000 - cotizaciones - 40,000,000. Apply IGC at higher brackets (likely 30.4% or 35%). PPM = 14.5% x 120,000,000 less cotizaciones. Compare tax to PPM to determine balance due or refund.

### Test 3 -- Gastos presuntos cap hit
**Input:** Gross honorarios CLP 60,000,000. Gastos presuntos.
**Expected output:** 30% x 60,000,000 = 18,000,000 but cap = 15 UTA (~12,112,920). Deduction = CLP 12,112,920.

### Test 4 -- Low-income refund scenario
**Input:** Gross honorarios CLP 8,000,000. Withholding 14.5% = CLP 1,160,000.
**Expected output:** Renta neta below 13.5 UTA after gastos and cotizaciones. IGC = 0. Full PPM refunded after cotizaciones deduction.

### Test 5 -- Mixed employment and honorarios
**Input:** Employment income CLP 20,000,000. Honorarios CLP 15,000,000. Gastos presuntos on honorarios.
**Expected output:** Renta neta global = employment net + honorarios net. Apply IGC to combined amount. Credits = PAYE from employment + PPM from honorarios. Result: tax due or refund depending on combined bracket.

---

## PROHIBITIONS

- NEVER use an incorrect UTA value -- always verify the December UTA for the relevant tax year at www.sii.cl
- NEVER allow gastos presuntos above 15 UTA, regardless of gross income
- NEVER apply the withholding rate from a different year -- verify the phase-in schedule (14.5% for 2025)
- NEVER ignore cotizaciones previsionales -- they are mandatory for workers a honorarios under Ley 21.133
- NEVER treat PPM withholdings as a final tax -- they are credits against the IGC
- NEVER allow gastos efectivos without proper documentation (facturas, boletas, receipts)
- NEVER use January UTA for IGC computation -- use December UTA of the tax year
- NEVER advise on APV regime choice without flagging for reviewer -- the optimal regime depends on marginal rate
- NEVER present tax calculations as definitive -- always label as estimated and direct client to a Contador Auditor for confirmation

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a Contador Auditor or equivalent licensed practitioner in Chile) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
