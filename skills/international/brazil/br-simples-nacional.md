---
name: br-simples-nacional
description: >
  Use this skill whenever asked about the Brazilian Simples Nacional or MEI regime. Trigger on phrases like "Simples Nacional", "MEI", "microempreendedor individual", "DAS", "DASN-SIMEI", "anexo Simples", "Simples table", "fator R", or any question about the unified tax regime for micro and small businesses in Brazil. Covers MEI fixed monthly DAS, Simples Nacional progressive tables (Anexos I-V), revenue thresholds, fator R, and annual declarations. ALWAYS read this skill before touching any Brazilian Simples Nacional or MEI work.
version: 2.0
jurisdiction: BR
tax_year: 2025
category: international
depends_on:
  - income-tax-workflow-base
---

# Brazil Simples Nacional / MEI -- Self-Employed Skill v2.0

---

## Section 1 -- Quick Reference

| Field | Value |
|---|---|
| Country | Brazil |
| Tax | Simples Nacional unified tax (DAS) covering IRPJ, CSLL, PIS, COFINS, CPP, ICMS, ISS, IPI |
| Currency | BRL only |
| Tax year | Calendar year |
| Primary legislation | Lei Complementar 123/2006 (Estatuto Nacional da Microempresa) |
| Supporting legislation | Resolucao CGSN; LC 155/2016 |
| Tax authority | Receita Federal do Brasil (RFB); Comite Gestor do Simples Nacional (CGSN) |
| Filing portal | Portal do Simples Nacional (www8.receita.fazenda.gov.br/SimplesNacional) |
| Filing deadline | DAS by 20th of following month; DEFIS by March 31; DASN-SIMEI by May 31 |
| Contributor | Open Accountants Community |
| Validated by | Pending -- requires sign-off by a Brazilian contador (CRC-registered) |
| Skill version | 2.0 |

### Revenue Thresholds

| Category | Maximum Annual Revenue |
|---|---|
| MEI | R$ 81,000 |
| Microempresa (ME) | R$ 360,000 |
| Empresa de Pequeno Porte (EPP) | R$ 4,800,000 |
| ICMS/ISS sublimit | R$ 3,600,000 |

### MEI Monthly DAS (2025)

| Activity | INSS (5% of min. wage) | ICMS | ISS | Total |
|---|---|---|---|---|
| Commerce/Industry | R$ 75.90 | R$ 1.00 | -- | R$ 76.90 |
| Services | R$ 75.90 | -- | R$ 5.00 | R$ 80.90 |
| Commerce + Services | R$ 75.90 | R$ 1.00 | R$ 5.00 | R$ 81.90 |

Based on minimum wage of R$ 1,518.00 for 2025.

### Effective Rate Formula

Effective Rate = (RBT12 x Nominal Rate - Deduction) / RBT12

### Conservative Defaults

| Ambiguity | Default |
|---|---|
| Unknown entity type | ME (not MEI -- more conservative) |
| Unknown CNAE | Anexo V (highest rates) |
| Unknown payroll for fator R | Fator R < 28% (stays in Anexo V) |
| Unknown revenue bracket | Highest band applicable |

---

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

**Minimum viable** -- entity type (MEI/ME/EPP), gross revenue last 12 months (RBT12), activity type (CNAE), current month revenue.

**Recommended** -- payroll costs (for fator R), state of registration, prior DAS payment history.

**Ideal** -- complete PGDAS-D data, segregated revenue by activity, Anexo classification confirmation, prior year DEFIS.

### Refusal Catalogue

**R-BR-S1 -- Exclusion transition.** "Revenue exceeds R$ 4,800,000. Client is excluded from Simples Nacional. Must migrate to Lucro Presumido or Lucro Real. Escalate to qualified contador."

**R-BR-S2 -- Lucro Presumido / Lucro Real.** "This skill covers Simples Nacional and MEI only. Other regimes have different computation methods."

**R-BR-S3 -- State-specific ICMS rules.** "Detailed state-specific ICMS rules for businesses above the sublimit require state-level expertise. Escalate."

---

## Section 3 -- Transaction Pattern Library

### 3.1 Revenue Patterns

| Pattern | Treatment | Notes |
|---|---|---|
| VENDA, RECEITA, PIX RECEBIDO | Include in RBT12 | Gross revenue for band determination |
| NF-E EMITIDA, NFS-E EMITIDA | Include in RBT12 | Invoice-based revenue |
| MERCADO LIVRE, MARKETPLACE | Include in RBT12 | Platform sales |
| EXPORTACAO | Include in RBT12 | Threshold test includes exports |
| DEVOLUCAO, CANCELAMENTO | Deduct from revenue | Reduces gross revenue |
| TRANSFERENCIA PROPRIA | EXCLUDE | Internal movement |

### 3.2 Tax Payment Patterns

| Pattern | Treatment | Notes |
|---|---|---|
| DAS, SIMPLES NACIONAL | Unified tax payment | Includes all taxes |
| DAS-MEI, DASN | MEI fixed payment | Monthly fixed amount |
| ICMS FORA SIMPLES | Separate ICMS payment | Above sublimit or ICMS-ST |
| ISS FORA SIMPLES | Separate ISS payment | Above sublimit |
| INSS PATRONAL | Separate employer INSS | Anexo IV only |

### 3.3 Anexo Determination Patterns

| CNAE Activity | Typical Anexo | Notes |
|---|---|---|
| Commerce, retail | Anexo I | Goods sales |
| Manufacturing, industry | Anexo II | Includes IPI |
| General services, maintenance | Anexo III | Check fator R for V activities |
| Cleaning, security, construction | Anexo IV | No CPP in DAS |
| IT consulting, professional services | Anexo V (or III if fator R >= 28%) | Fator R is critical |

---

## Section 4 -- Worked Examples

### Example 1 -- MEI Monthly DAS (Services)

**Input:** MEI providing IT services. Minimum wage R$ 1,518.

**Computation:**
- INSS: 5% x 1,518 = R$ 75.90
- ISS: R$ 5.00
- Total DAS: R$ 80.90/month

### Example 2 -- Simples Nacional, Anexo I Commerce

**Input:** RBT12 = R$ 500,000. Current month revenue = R$ 45,000.

**Computation:**
- Band 3 (360,001 to 720,000)
- Effective rate = (500,000 x 9.50% - 13,860) / 500,000 = 6.728%
- DAS = 45,000 x 6.728% = R$ 3,027.60

### Example 3 -- Anexo V with Fator R >= 28%

**Input:** Consulting firm, RBT12 = R$ 400,000. Payroll last 12 months = R$ 130,000.

**Computation:**
- Fator R = 130,000 / 400,000 = 32.5% (>= 28%)
- Use Anexo III instead of V
- Band 3: effective rate = (400,000 x 13.50% - 17,640) / 400,000 = 9.09%

### Example 4 -- MEI Excess Revenue (Within 20%)

**Input:** MEI with annual revenue R$ 90,000 (11.1% over limit).

**Classification:**
- Excess = R$ 9,000
- DAS complementar on excess at ME Simples rates
- Transition to ME effective January of following year

---

## Section 5 -- Tier 1 Rules (When Data Is Clear)

### 5.1 MEI Eligibility

**Legislation:** LC 123/2006, Art. 18-A to 18-E

Maximum annual revenue R$ 81,000. Maximum 1 employee. Prohibited for regulated professions. Cannot be partner in another company. Cannot have branches.

### 5.2 Simples Nacional Anexos

**Legislation:** LC 123/2006, Anexos I-V (as amended by LC 155/2016)

Anexo I: Commerce (4.00% -- 19.00%). Anexo II: Industry (4.50% -- 30.00%). Anexo III: Services I (6.00% -- 33.00%). Anexo IV: Services II -- cleaning/security/construction (4.50% -- 33.00%, no CPP in DAS). Anexo V: Professional services (15.50% -- 30.50%).

### 5.3 Fator R Rule

**Legislation:** LC 123/2006, Art. 18, par. 5-J

For Anexo V activities, if fator R (payroll/revenue ratio over 12 months) >= 28%, the activity is taxed under Anexo III instead.

### 5.4 ICMS/ISS Sublimit

If revenue exceeds R$ 3,600,000 but stays under R$ 4,800,000: federal taxes remain in Simples DAS, but ICMS and ISS are paid OUTSIDE Simples at normal state/municipal rates.

### 5.5 Anexo IV Special Rule

Anexo IV does NOT include CPP (employer INSS) in the DAS. Employer INSS must be paid separately (20% on payroll).

---

## Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Fator R Computation

Requires accurate payroll data including pro-labore, salaries, FGTS, INSS, and 13th salary. Flag for reviewer.

### 6.2 Activities Spanning Multiple Anexos

Revenue must be segregated by activity. Each activity's revenue taxed under its respective Anexo, but RBT12 for rate determination is TOTAL revenue. Flag for reviewer.

### 6.3 Sublimit Exceeded

Revenue above R$ 3,600,000: significant complexity increase. Flag for contador.

### 6.4 MEI Approaching Ceiling

Revenue approaching R$ 81,000: if exceeds by more than 20%, MEI is retroactively converted to ME from January. Must hire a contador.

---

## Section 7 -- Excel Working Paper Template

```
BRAZIL SIMPLES NACIONAL -- Working Paper
Period: [Month]

A. REVENUE
  A1. RBT12 (gross revenue, last 12 months)        ___________
  A2. Current month revenue                         ___________
  A3. Activity type / CNAE                          ___________
  A4. Applicable Anexo                              ___________

B. RATE COMPUTATION
  B1. Revenue band                                  ___________
  B2. Nominal rate                                  ___________
  B3. Deduction                                     ___________
  B4. Effective rate = (A1 x B2 - B3) / A1          ___________

C. DAS COMPUTATION
  C1. DAS = A2 x B4                                 ___________

D. FATOR R (if Anexo V activity)
  D1. Total payroll (last 12 months)                ___________
  D2. Fator R = D1 / A1                             ___________
  D3. >= 28%? If yes, use Anexo III                  ___________

REVIEWER FLAGS:
  [ ] Entity type confirmed (MEI/ME/EPP)?
  [ ] CNAE verified for Anexo selection?
  [ ] Fator R computed (if Anexo V)?
  [ ] Sublimit check (R$ 3,600,000)?
  [ ] Exclusion check (R$ 4,800,000)?
```

---

## Section 8 -- Bank Statement Reading Guide

### Brazilian Bank Statement Formats

| Bank | Format | Key Fields |
|---|---|---|
| Banco do Brasil, Caixa, Itau | CSV, PDF, OFX | Data, Historico, Valor, Saldo |
| Bradesco, Santander | CSV, PDF | Data, Descricao, Debito, Credito |
| Nubank, Inter, C6 | CSV | Data, Descricao, Valor |

### Key Terms

| Term | Hint |
|---|---|
| PIX RECEBIDO | Income -- include in revenue |
| DAS, SIMPLES | Tax payment |
| PGDAS-D | Simples computation system |
| DASN-SIMEI | MEI annual declaration |
| DEFIS | Simples annual declaration |

---

## Section 9 -- Onboarding Fallback

```
ONBOARDING QUESTIONS -- BRAZIL SIMPLES NACIONAL
1. Entity type: MEI, ME, or EPP?
2. Gross revenue in the last 12 months (RBT12)?
3. CNAE code(s)?
4. Payroll costs (folha de salarios) -- last 12 months?
5. State of registration?
6. If MEI: approaching the R$ 81,000 ceiling?
7. Do you have activities spanning multiple Anexos?
8. Prior year DEFIS or DASN-SIMEI available?
9. Any ICMS-ST products?
10. Any employees?
```

---

## Section 10 -- Reference Material

### Anexo Tables (Full)

**Anexo I -- Commerce:** Band 1: 4.00% (up to 180K). Band 2: 7.30% (180-360K, ded. 5,940). Band 3: 9.50% (360-720K, ded. 13,860). Band 4: 10.70% (720K-1.8M, ded. 22,500). Band 5: 14.30% (1.8-3.6M, ded. 87,300). Band 6: 19.00% (3.6-4.8M, ded. 378,000).

**Anexo II -- Industry:** Band 1: 4.50%. Band 2: 7.80% (ded. 5,940). Band 3: 10.00% (ded. 13,860). Band 4: 11.20% (ded. 22,500). Band 5: 14.70% (ded. 85,500). Band 6: 30.00% (ded. 720,000).

**Anexo III -- Services I:** Band 1: 6.00%. Band 2: 11.20% (ded. 9,360). Band 3: 13.50% (ded. 17,640). Band 4: 16.00% (ded. 35,640). Band 5: 21.00% (ded. 125,640). Band 6: 33.00% (ded. 648,000).

**Anexo IV -- Services II:** Band 1: 4.50%. Band 2: 9.00% (ded. 8,100). Band 3: 10.20% (ded. 12,420). Band 4: 14.00% (ded. 39,780). Band 5: 22.00% (ded. 183,780). Band 6: 33.00% (ded. 828,000).

**Anexo V -- Services III:** Band 1: 15.50%. Band 2: 18.00% (ded. 4,500). Band 3: 19.50% (ded. 9,900). Band 4: 20.50% (ded. 17,100). Band 5: 23.00% (ded. 62,100). Band 6: 30.50% (ded. 540,000).

### Key Legislation

| Topic | Reference |
|---|---|
| Simples Nacional statute | LC 123/2006 |
| Anexo tables | LC 123/2006, Anexos I-V (amended by LC 155/2016) |
| MEI | LC 123/2006, Art. 18-A to 18-E |
| Fator R | LC 123/2006, Art. 18, par. 5-J |
| Revenue thresholds | LC 123/2006, Art. 3 |
| ICMS/ISS sublimit | LC 123/2006, Art. 13, 18 |

---

## PROHIBITIONS

- NEVER apply Simples Nacional rates to businesses above R$ 4,800,000
- NEVER allow regulated professionals to register as MEI
- NEVER ignore the fator R when computing Anexo V activities
- NEVER use only current activity revenue for band determination -- use RBT12 across ALL activities
- NEVER forget that Anexo IV does NOT include employer INSS in the DAS
- NEVER treat MEI DAS amounts as fixed across years -- they change with the minimum wage
- NEVER omit the ICMS/ISS sublimit check for businesses above R$ 3,600,000
- NEVER present calculations as definitive -- always label as estimated and direct client to a CRC-registered contador

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CRC-registered contador or equivalent licensed practitioner in Brazil) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
