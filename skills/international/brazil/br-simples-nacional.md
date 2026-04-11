---
name: br-simples-nacional
description: Use this skill whenever asked about the Brazilian Simples Nacional or MEI regime. Trigger on phrases like "Simples Nacional", "MEI", "microempreendedor individual", "DAS", "DASN-SIMEI", "anexo Simples", "Simples table", "fator R", or any question about the unified tax regime for micro and small businesses in Brazil. Covers MEI fixed monthly DAS, Simples Nacional progressive tables (Anexos I-V), revenue thresholds, fator R, and annual declarations. ALWAYS read this skill before touching any Brazilian Simples Nacional or MEI work.
---

# Brazil Simples Nacional -- Self-Employed Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Brazil |
| Jurisdiction Code | BR |
| Primary Legislation | Lei Complementar 123/2006 (LC 123/2006, Estatuto Nacional da Microempresa) |
| Supporting Legislation | Resolucao CGSN (Comite Gestor do Simples Nacional); LC 155/2016 |
| Tax Authority | Receita Federal do Brasil (RFB); Comite Gestor do Simples Nacional (CGSN) |
| Portal | Portal do Simples Nacional (www8.receita.fazenda.gov.br/SimplesNacional) |
| Contributor | Open Accountants Community |
| Validated By | Pending -- requires sign-off by a Brazilian contador (CRC-registered) |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Tax Year | 2025 |
| Confidence Coverage | Tier 1: MEI DAS, revenue thresholds, Anexo selection, effective rate calculation. Tier 2: fator R computation, mixed activities, sublimits. Tier 3: exclusion procedures, ICMS/ISS state specifics, Simples to Lucro Presumido transition. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags and presents options. Qualified professional must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate and document.

---

## Step 0: Client Onboarding Questions

Before computing any Simples Nacional figure, you MUST know:

1. **Entity type** [T1] -- MEI, Microempresa (ME), or Empresa de Pequeno Porte (EPP)
2. **Gross revenue in the last 12 months (RBT12)** [T1] -- determines rate band
3. **Activity type (CNAE)** [T1] -- determines which Anexo applies
4. **Payroll costs (folha de salarios)** [T2] -- for fator R calculation (Anexo V/III)
5. **State of registration** [T2] -- for ICMS sublimit applicability
6. **Whether MEI is being exceeded** [T1] -- approaching the MEI ceiling

**If gross revenue exceeds R$ 4,800,000 in trailing 12 months, STOP. Client is excluded from Simples Nacional.**

---

## Step 1: MEI (Microempreendedor Individual) [T1]

**Legislation:** LC 123/2006, Art. 18-A to 18-E

### Eligibility [T1]

| Requirement | Detail |
|-------------|--------|
| Maximum annual revenue | **R$ 81,000** (R$ 6,750/month average) |
| Maximum employees | 1 employee earning up to 1 minimum wage or the category floor |
| Prohibited activities | Most regulated professions (lawyers, doctors, dentists, accountants, engineers) |
| Other restrictions | Cannot be partner in another company; cannot have branches |

### MEI Monthly DAS (Fixed Amount) [T1]

| Activity | INSS (5% of min. wage) | ICMS | ISS | Total (approx.) |
|----------|----------------------|------|-----|-----------------|
| Commerce/Industry | R$ 75.90 | R$ 1.00 | -- | **R$ 76.90** |
| Services | R$ 75.90 | -- | R$ 5.00 | **R$ 80.90** |
| Commerce + Services | R$ 75.90 | R$ 1.00 | R$ 5.00 | **R$ 81.90** |

**Based on minimum wage of R$ 1,518.00 for 2025. INSS = 5% x R$ 1,518 = R$ 75.90. Verify minimum wage annually.**

### MEI Obligations [T1]

| Obligation | Detail |
|------------|--------|
| DAS payment | Monthly, by the 20th of each month |
| DASN-SIMEI | Annual declaration of gross revenue, due May 31 |
| Nota fiscal | Required when selling to legal entities (PJ); optional for individuals (PF) |

---

## Step 2: Simples Nacional -- Revenue Thresholds [T1]

**Legislation:** LC 123/2006, Art. 3

| Category | Maximum Annual Revenue |
|----------|----------------------|
| MEI | R$ 81,000 |
| Microempresa (ME) | R$ 360,000 |
| Empresa de Pequeno Porte (EPP) | R$ 4,800,000 |

### ICMS/ISS Sublimit [T1]

| Sublimit | Amount |
|----------|--------|
| National sublimit for ICMS and ISS | R$ 3,600,000 |

If revenue exceeds R$ 3,600,000 but is under R$ 4,800,000, the company remains in Simples for federal taxes but pays ICMS and ISS outside Simples (at normal state/municipal rates).

---

## Step 3: Simples Nacional Anexos (Tax Tables) [T1]

**Legislation:** LC 123/2006, Anexos I-V (as amended by LC 155/2016)

### Anexo I -- Commerce (Comercio) [T1]

| Band | Revenue (RBT12) | Nominal Rate | Deduction |
|------|-----------------|-------------|-----------|
| 1 | Up to R$ 180,000 | 4.00% | 0 |
| 2 | 180,000.01 to 360,000 | 7.30% | R$ 5,940 |
| 3 | 360,000.01 to 720,000 | 9.50% | R$ 13,860 |
| 4 | 720,000.01 to 1,800,000 | 10.70% | R$ 22,500 |
| 5 | 1,800,000.01 to 3,600,000 | 14.30% | R$ 87,300 |
| 6 | 3,600,000.01 to 4,800,000 | 19.00% | R$ 378,000 |

### Anexo II -- Industry (Industria) [T1]

| Band | Revenue (RBT12) | Nominal Rate | Deduction |
|------|-----------------|-------------|-----------|
| 1 | Up to 180,000 | 4.50% | 0 |
| 2 | 180,000.01 to 360,000 | 7.80% | R$ 5,940 |
| 3 | 360,000.01 to 720,000 | 10.00% | R$ 13,860 |
| 4 | 720,000.01 to 1,800,000 | 11.20% | R$ 22,500 |
| 5 | 1,800,000.01 to 3,600,000 | 14.70% | R$ 85,500 |
| 6 | 3,600,000.01 to 4,800,000 | 30.00% | R$ 720,000 |

### Anexo III -- Services I (general services, maintenance, etc.) [T1]

| Band | Revenue (RBT12) | Nominal Rate | Deduction |
|------|-----------------|-------------|-----------|
| 1 | Up to 180,000 | 6.00% | 0 |
| 2 | 180,000.01 to 360,000 | 11.20% | R$ 9,360 |
| 3 | 360,000.01 to 720,000 | 13.50% | R$ 17,640 |
| 4 | 720,000.01 to 1,800,000 | 16.00% | R$ 35,640 |
| 5 | 1,800,000.01 to 3,600,000 | 21.00% | R$ 125,640 |
| 6 | 3,600,000.01 to 4,800,000 | 33.00% | R$ 648,000 |

### Anexo IV -- Services II (cleaning, security, construction) [T1]

| Band | Revenue (RBT12) | Nominal Rate | Deduction |
|------|-----------------|-------------|-----------|
| 1 | Up to 180,000 | 4.50% | 0 |
| 2 | 180,000.01 to 360,000 | 9.00% | R$ 8,100 |
| 3 | 360,000.01 to 720,000 | 10.20% | R$ 12,420 |
| 4 | 720,000.01 to 1,800,000 | 14.00% | R$ 39,780 |
| 5 | 1,800,000.01 to 3,600,000 | 22.00% | R$ 183,780 |
| 6 | 3,600,000.01 to 4,800,000 | 33.00% | R$ 828,000 |

**Note:** Anexo IV does NOT include CPP (employer INSS) in the DAS. Employer INSS must be paid separately (20% on payroll).

### Anexo V -- Services III (intellectual, technical, professional) [T1]

| Band | Revenue (RBT12) | Nominal Rate | Deduction |
|------|-----------------|-------------|-----------|
| 1 | Up to 180,000 | 15.50% | 0 |
| 2 | 180,000.01 to 360,000 | 18.00% | R$ 4,500 |
| 3 | 360,000.01 to 720,000 | 19.50% | R$ 9,900 |
| 4 | 720,000.01 to 1,800,000 | 20.50% | R$ 17,100 |
| 5 | 1,800,000.01 to 3,600,000 | 23.00% | R$ 62,100 |
| 6 | 3,600,000.01 to 4,800,000 | 30.50% | R$ 540,000 |

---

## Step 4: Effective Rate Calculation [T1]

**Legislation:** LC 123/2006, Art. 18

### Formula [T1]

Effective Rate = (RBT12 x Nominal Rate - Deduction) / RBT12

Where RBT12 = gross revenue in the last 12 months.

### Example [T1]

RBT12 = R$ 500,000 (Anexo I, Band 3):
- Effective rate = (500,000 x 9.50% - 13,860) / 500,000
- = (47,500 - 13,860) / 500,000
- = 33,640 / 500,000
- = **6.728%**

Monthly DAS = Current month revenue x Effective rate

---

## Step 5: Fator R (Payroll Factor) [T2]

**Legislation:** LC 123/2006, Art. 18, par. 5-J

### Rule [T2]

For activities listed in Anexo V, if the payroll-to-revenue ratio (fator R) >= 28%, the activity is taxed under Anexo III (lower rates) instead of Anexo V.

Fator R = Total payroll (last 12 months) / Gross revenue (last 12 months)

| Fator R | Applicable Anexo |
|---------|-----------------|
| >= 28% | Anexo III |
| < 28% | Anexo V |

[T2] Flag for reviewer: fator R calculation requires accurate payroll data including pro-labore, salaries, FGTS, INSS, and 13th salary.

---

## Step 6: DAS Payment and Filing [T1]

| Item | Detail |
|------|--------|
| DAS generation | Via Portal do Simples Nacional (PGDAS-D) |
| Payment deadline | 20th of the following month |
| Annual declaration | DEFIS (Declaracao de Informacoes Socioeconomicas e Fiscais) -- due March 31 |
| MEI annual declaration | DASN-SIMEI -- due May 31 |

---

## Step 7: Edge Case Registry

### EC1 -- MEI exceeding R$ 81,000 [T1]
**Situation:** MEI earned R$ 95,000 in the year.
**Resolution:** If revenue exceeds by up to 20% (up to R$ 97,200), MEI pays a DAS difference on the excess amount. If exceeds by more than 20%, MEI is retroactively converted to ME from January of that year, with all taxes recalculated under Simples Nacional tables. Must hire a contador.

### EC2 -- Fator R just below 28% [T2]
**Situation:** Software consultancy with fator R = 26%.
**Resolution:** Taxed under Anexo V (higher rates). If feasible, increasing pro-labore or hiring could push fator R above 28%, qualifying for Anexo III. [T2] Flag for reviewer -- this is a planning decision.

### EC3 -- Activities spanning multiple Anexos [T2]
**Situation:** Company does both commerce (Anexo I) and consulting (Anexo V).
**Resolution:** Revenue must be segregated by activity. Each activity's revenue is taxed under its respective Anexo, but the RBT12 for rate determination is the TOTAL revenue (all activities combined). [T2] Flag for reviewer.

### EC4 -- Revenue exceeds R$ 3,600,000 sublimit [T1]
**Situation:** EPP with R$ 4,200,000 revenue.
**Resolution:** Still in Simples for federal taxes. ICMS and ISS are paid OUTSIDE Simples at normal state/municipal rates. Additional complexity. [T2] Flag for reviewer or escalate.

### EC5 -- Simples Nacional exclusion [T3]
**Situation:** Revenue exceeds R$ 4,800,000.
**Resolution:** EXCLUDED from Simples Nacional from the following January (or month following excess if > 20% over). Must migrate to Lucro Presumido or Lucro Real. ESCALATE to qualified contador.

### EC6 -- MEI with regulated profession [T1]
**Situation:** Accountant wants to register as MEI.
**Resolution:** NOT eligible. Regulated professions (CRC, OAB, CRM, CREA, etc.) are excluded from MEI. Must use ME/EPP under Simples or other regime.

---

## Step 8: Test Suite

### Test 1 -- MEI monthly DAS (services)
**Input:** MEI providing IT services. Minimum wage R$ 1,518.
**Expected output:**
- INSS: 5% x 1,518 = R$ 75.90
- ISS: R$ 5.00
- Total DAS: R$ 80.90/month

### Test 2 -- Simples Nacional, Anexo I commerce
**Input:** RBT12 = R$ 500,000. Current month revenue = R$ 45,000.
**Expected output:**
- Band 3 (360,001 to 720,000)
- Effective rate = (500,000 x 9.50% - 13,860) / 500,000 = 6.728%
- DAS = 45,000 x 6.728% = R$ 3,027.60

### Test 3 -- Anexo V with fator R >= 28%
**Input:** Consulting firm, RBT12 = R$ 400,000. Payroll last 12 months = R$ 130,000.
**Expected output:**
- Fator R = 130,000 / 400,000 = 32.5% (>= 28%)
- Use Anexo III instead of V
- Band 3: effective rate = (400,000 x 13.50% - 17,640) / 400,000 = 9.09%
- Much lower than Anexo V Band 3 rate

### Test 4 -- Anexo V with fator R < 28%
**Input:** Same firm, payroll = R$ 100,000.
**Expected output:**
- Fator R = 100,000 / 400,000 = 25% (< 28%)
- Use Anexo V
- Band 3: effective rate = (400,000 x 19.50% - 9,900) / 400,000 = 17.025%

### Test 5 -- MEI excess revenue (within 20%)
**Input:** MEI with annual revenue R$ 90,000 (11.1% over limit).
**Expected output:**
- Excess = R$ 9,000
- DAS complementar on excess at ME Simples rates
- Transition to ME effective January of following year

---

## PROHIBITIONS

- NEVER apply Simples Nacional rates to businesses above R$ 4,800,000 -- they are excluded
- NEVER allow regulated professionals (CRC, OAB, CRM, etc.) to register as MEI
- NEVER ignore the fator R when computing Anexo V activities -- it may reduce the rate significantly
- NEVER use total revenue of ONLY the current activity for band determination -- use RBT12 across ALL activities
- NEVER forget that Anexo IV does NOT include employer INSS in the DAS -- it must be paid separately
- NEVER treat MEI DAS amounts as fixed across years -- they change with the minimum wage
- NEVER omit the ICMS/ISS sublimit check for businesses above R$ 3,600,000
- NEVER present calculations as definitive -- always label as estimated and direct client to a CRC-registered contador

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CRC-registered contador or equivalent licensed practitioner in Brazil) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
