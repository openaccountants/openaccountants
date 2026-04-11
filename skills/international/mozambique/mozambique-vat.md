---
name: mozambique-vat
description: Use this skill whenever asked to prepare, review, or create a Mozambique VAT (IVA) return for any client. Trigger on phrases like "prepare VAT return", "IVA Moçambique", "AT return", "declaração do IVA", or any request involving Mozambique VAT filing. Also trigger when classifying transactions for VAT purposes from bank statements, invoices, or other source data. This skill contains the complete Mozambique IVA classification rules, return form mappings, deductibility rules, reverse charge treatment, ISPC simplified tax interaction, registration thresholds, and filing deadlines. ALWAYS read this skill before touching any Mozambique VAT-related work.
---

# Mozambique VAT (IVA) Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Mozambique (Republic of Mozambique) |
| Jurisdiction Code | MZ |
| Primary Legislation | Código do Imposto sobre o Valor Acrescentado (CIVA), Law 32/2007 as amended |
| Supporting Legislation | Regulamento do CIVA; ISPC (Imposto Simplificado para Pequenos Contribuintes); Código das Execuções Fiscais |
| Tax Authority | Autoridade Tributária de Moçambique (AT) |
| Filing Portal | https://efatura.at.gov.mz (e-Factura / e-Tributação) |
| Contributor | Open Accounting Skills Registry |
| Validated By | Pending -- requires validation by a licensed contabilista in Mozambique |
| Validation Date | Pending |
| Last Verified | 2026-04-10 (web-verified against PWC, AT Mozambique, RSM Tax Pocket Guide 2025) |
| Skill Version | 1.1 |
| Confidence Coverage | Tier 1: rate application, return mapping, registration, deadlines, blocked categories, ISPC boundary. Tier 2: partial exemption, mixed supplies, megaproject regime. Tier 3: LNG/gas sector, mining conventions, special economic zones. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag for contabilista.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate.

---

## Step 0: Client Onboarding Questions

1. **Entity name and NUIT (Número Único de Identificação Tributária)** [T1]
2. **IVA registration status** [T1] -- IVA registered, ISPC (simplified), or unregistered
3. **IVA period** [T1] -- monthly (turnover > MZN 2,500,000) or quarterly
4. **Industry/sector** [T2] -- impacts classification (agriculture, mining, megaprojects)
5. **Does the business make exempt supplies?** [T2] -- if yes, prorata required
6. **Does the business import goods?** [T1] -- customs IVA at port of Maputo/Beira/Nacala
7. **Crédito de IVA transitado** [T1] -- credit brought forward
8. **Does the business operate under a megaproject fiscal regime?** [T3] -- Sasol, LNG, etc.

**If items 1-2 are unknown, STOP.**

---

## Step 1: VAT Rate Structure [T1]

| Rate | Description | Legislation |
|------|-------------|-------------|
| 16% | Standard rate (taxa normal) | CIVA, Art. 17 |
| 5% | Reduced rate (private health, private education, vocational training) | CIVA, Art. 17-A |
| 0% | Zero rate (exports, specified supplies) | CIVA, Art. 11 |
| Exempt | Isenções (no IVA, no input recovery) | CIVA, Art. 9-10 |

### Zero-Rated Supplies [T1]
**Legislation:** CIVA, Art. 11.
- Export of goods (with customs documentation)
- Export of services consumed outside Mozambique
- International transport services
- Supplies to diplomats and international organizations

### Exempt Supplies [T1]
**Legislation:** CIVA, Art. 9-10.
- Basic foodstuffs (bread, rice, wheat flour, maize, cassava, vegetables, eggs, milk)
- Financial services (interest on loans, life insurance premiums, forex transactions)
- Medical and healthcare services (public and authorized private)
- Educational services (authorized institutions)
- Residential rental
- Public passenger transport
- Agricultural inputs (seeds, fertilizers, pesticides as specified)
- Water and electricity (domestic use below threshold)

---

## Step 2: ISPC -- Simplified Tax for Small Taxpayers [T1]

**Legislation:** ISPC Law 5/2009.

Businesses with annual turnover below MZN 2,500,000 pay ISPC instead of IVA:

| Turnover Range | ISPC Rate |
|---------------|-----------|
| Up to MZN 2,500,000 | 3% of gross turnover |

**Rules:**
- ISPC taxpayers do NOT charge IVA
- ISPC taxpayers CANNOT recover input IVA
- ISPC is filed quarterly
- If turnover exceeds MZN 2,500,000, must register for IVA

---

## Step 3: Transaction Classification Rules

### 3a. Transaction Type [T1]
- Sale (IVA liquidado / output) or Purchase (IVA dedutível / input)
- Salaries, INSS contributions, IRPS, dividends = OUT OF SCOPE

### 3b. Counterparty Location [T1]
- Domestic (Mozambique)
- SADC: South Africa, Tanzania, Zimbabwe, Zambia, Malawi, etc.
- Rest of World
- **Note:** SADC has no common VAT area.

### 3c. Supply Type [T1]
- Goods / Services / Import of goods (customs) / Import of services (reverse charge)
- **Legislation:** CIVA, Art. 6 (place of supply)

---

## Step 4: VAT Return Form Structure [T1]

### Output Section

| Line | Description | Mapping |
|------|-------------|---------|
| 1 | Vendas e prestações de serviços taxáveis (16%) | Standard-rated sales |
| 2 | Operações isentas | Exempt supplies |
| 3 | Exportações (0%) | Zero-rated |
| 4 | Total volume de negócios | 1 + 2 + 3 |
| 5 | IVA liquidado (16% on Line 1) | Output IVA |
| 6 | IVA autoliquidação (reverse charge) | Self-assessed on imported services |
| 7 | Regularizações | Credit notes, adjustments |
| 8 | Total IVA a favor do Estado | 5 + 6 + 7 |

### Input Section

| Line | Description | Mapping |
|------|-------------|---------|
| 9 | IVA sobre compras locais | Input IVA on local purchases |
| 10 | IVA sobre importações | Customs IVA |
| 11 | IVA autoliquidação (input) | Reverse charge input |
| 12 | IVA sobre imobilizado | IVA on capital goods |
| 13 | Regularizações (exclusões) | Blocked items |
| 14 | Total IVA dedutível | 9 + 10 + 11 + 12 - 13 |

### Net Calculation

| Line | Description | Formula |
|------|-------------|---------|
| 15 | IVA a pagar / Crédito | 8 - 14 |
| 16 | Crédito transitado | Prior period |
| 17 | Montante a pagar / Crédito a reportar | 15 - 16 |

---

## Step 5: Reverse Charge [T1]

**Legislation:** CIVA, Art. 23 (autoliquidação).

When a Mozambique IVA-registered person receives services from a non-resident:
1. Self-assess output IVA at 16% (Line 6)
2. Claim input IVA at 16% (Line 11) if for taxable supplies
3. Net effect: zero for fully taxable businesses

---

## Step 6: Deductibility Check

### Blocked Input Tax [T1]
**Legislation:** CIVA, Art. 20-22 (exclusions).
- Vehicles for personal transport (< 9 seats), unless taxi/hire (Art. 21)
- Entertainment and hospitality (Art. 21)
- Personal use goods and services (Art. 21)
- Fuel for blocked vehicles (Art. 21)
- Purchases without valid IVA invoice with NUIT (Art. 22)

### Partial Exemption [T2]
**Legislation:** CIVA, Art. 19 (pro rata).
`Recovery % = (Taxable + Zero-Rated) / Total Turnover * 100`
**Flag for reviewer: AT may require specific method.**

---

## Step 7: Key Thresholds [T1]

| Threshold | Value | Legislation |
|-----------|-------|-------------|
| Mandatory IVA registration | MZN 2,500,000 annual turnover | CIVA, Art. 26 |
| ISPC threshold | Below MZN 2,500,000 | ISPC Law 5/2009 |
| Monthly filing | Turnover > MZN 2,500,000 and designated by AT | CIVA, Art. 32 |
| Quarterly filing | Standard | CIVA, Art. 32 |

---

## Step 8: Filing Deadlines [T1]

| Obligation | Period | Deadline | Legislation |
|-----------|--------|----------|-------------|
| IVA return (monthly) | Monthly | Last working day of following month | CIVA, Art. 32 |
| IVA return (quarterly) | Quarterly | Last working day of month following quarter | CIVA, Art. 32 |
| ISPC return | Quarterly | Last working day of month following quarter | ISPC Law |
| Payment | Same as return | Same deadline | CIVA |

### Penalties [T1]
- Late filing: MZN 5,000 - MZN 50,000 per return
- Late payment: 2% per month interest
- Failure to register: penalties per tax procedures code

---

## PROHIBITIONS [T1]

- NEVER confuse IVA with ISPC -- they are separate regimes
- NEVER let AI guess return line assignment
- NEVER allow ISPC taxpayers to charge IVA or recover input IVA
- NEVER allow recovery on blocked categories
- NEVER confuse zero-rated with exempt
- NEVER apply reverse charge to out-of-scope categories
- NEVER compute numbers -- engine handles arithmetic
- NEVER file without checking crédito transitado
- NEVER accept invoices without valid NUIT
- NEVER apply standard IVA rules to megaproject companies without verifying their fiscal regime

---

## Step 9: Edge Case Registry

### EC1 -- Import of services (SaaS) [T1]
**Situation:** Company subscribes to Google Workspace. Monthly USD 50.
**Resolution:** Autoliquidação at 16%. Output Line 6, Input Line 11. Net zero.
**Legislation:** CIVA, Art. 23.

### EC2 -- Export of prawns (zero-rated) [T1]
**Situation:** Exporter ships prawns to Spain.
**Resolution:** Zero-rated. Line 3. No output IVA. Input IVA recoverable.
**Legislation:** CIVA, Art. 11.

### EC3 -- Motor vehicle (blocked) [T1]
**Situation:** Company buys sedan for manager.
**Resolution:** Input IVA BLOCKED. Cost includes irrecoverable IVA.
**Legislation:** CIVA, Art. 21.

### EC4 -- ISPC taxpayer boundary [T1]
**Situation:** Small business under ISPC exceeds MZN 2,500,000 turnover.
**Resolution:** Must register for IVA. Switch from ISPC to IVA regime.
**Legislation:** CIVA, Art. 26; ISPC Law.

### EC5 -- Megaproject (LNG) [T3]
**Situation:** Company supplies goods to Mozambique LNG project.
**Resolution:** Escalate. Megaprojects operate under specific fiscal regimes negotiated with government. IVA treatment varies by contract.
**Legislation:** Petroleum Law; specific EPCCs/concession agreements.

### EC6 -- Mixed supply (prorata) [T2]
**Situation:** Company provides taxable consulting and exempt financial services.
**Resolution:** Pro rata applies. Flag for reviewer.
**Legislation:** CIVA, Art. 19.

### EC7 -- Basic foodstuffs (exempt) [T1]
**Situation:** Wholesaler sells rice and bread.
**Resolution:** Exempt. Line 2. No output IVA. Input IVA on procurement NOT recoverable.
**Legislation:** CIVA, Art. 9.

### EC8 -- Credit note [T1]
**Situation:** Supplier issues nota de crédito for returned goods.
**Resolution:** Reduce output IVA. Line 7. Customer adjusts input IVA.
**Legislation:** CIVA, Art. 37.

---

## Step 10: Reviewer Escalation Protocol

```
REVIEWER FLAG / ESCALATION REQUIRED
[Standard format]
```

---

## Step 11: Test Suite

### Test 1 -- Standard sale [T1]
**Input:** Company sells goods MZN 1,000,000 net.
**Expected output:** Line 1 = MZN 1,000,000. Line 5 = MZN 160,000 (16%).

### Test 2 -- Local purchase [T1]
**Input:** Company buys supplies. Invoice: MZN 500,000 + MZN 80,000 IVA.
**Expected output:** Line 9 = MZN 80,000. Recoverable.

### Test 3 -- Reverse charge [T1]
**Input:** Company receives services from South African firm. MZN 3,000,000.
**Expected output:** Line 6 = MZN 480,000 (16% output). Line 11 = MZN 480,000 (input). Net zero.

### Test 4 -- Export [T1]
**Input:** Exporter ships goods MZN 50,000,000.
**Expected output:** Line 3 = MZN 50,000,000. IVA = 0. Input IVA recoverable.

### Test 5 -- Blocked (entertainment) [T1]
**Input:** Company hosts event. MZN 200,000 + MZN 32,000 IVA.
**Expected output:** Input IVA = 0 (BLOCKED). Cost = MZN 232,000.

### Test 6 -- ISPC taxpayer [T1]
**Input:** Small retailer under ISPC. Quarterly sales MZN 400,000.
**Expected output:** ISPC = 3% of MZN 400,000 = MZN 12,000. No input IVA recovery.

---

## Step 12: Out of Scope -- Direct Tax [T3]

- **IRPC (Corporate Income Tax):** 32%.
- **IRPS (Personal Income Tax):** Progressive rates 10%-32%.
- **INSS:** Social security. Employer 4% + employee 3%. Separate from IVA.

---

## Contribution Notes

Mozambique-specific elements include the 16% rate, ISPC simplified regime, megaproject fiscal regimes, and Portuguese-language terminology (IVA, NUIT, autoliquidação).

**A skill may not be published without sign-off from a licensed contabilista in Mozambique.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
