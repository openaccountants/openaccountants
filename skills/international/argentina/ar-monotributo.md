---
name: ar-monotributo
description: Use this skill whenever asked about the Argentine Monotributo simplified tax regime. Trigger on phrases like "monotributo", "regimen simplificado", "AFIP", "DAS monotributo", "categorias monotributo", "impuesto integrado", "monotributista", or any question about the unified monthly payment, category thresholds, or obligations for small self-employed individuals in Argentina. Covers the unified monthly payment (impuesto integrado + aportes jubilatorios + obra social), revenue-based categories (A through K), and exclusion rules. ALWAYS read this skill before touching any Argentine Monotributo work.
---

# Argentina Monotributo -- Self-Employed Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Argentina |
| Jurisdiction Code | AR |
| Primary Legislation | Ley 24.977 (Monotributo, Regimen Simplificado para Pequenos Contribuyentes), as amended |
| Supporting Legislation | RG AFIP; Decreto reglamentario |
| Tax Authority | Administracion Federal de Ingresos Publicos (AFIP) / ARCA |
| Filing Portal | Monotributo portal via AFIP web (afip.gob.ar) |
| Contributor | Open Accountants Community |
| Validated By | Pending -- requires sign-off by an Argentine contador publico |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Tax Year | 2025 |
| Confidence Coverage | Tier 1: category table, monthly payment computation, payment deadlines. Tier 2: recategorization triggers, mixed services/goods classification. Tier 3: exclusion consequences, transition to regimen general, international income. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags and presents options. Qualified professional must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate and document.

---

## Step 0: Client Onboarding Questions

Before computing any Monotributo figure, you MUST know:

1. **Gross revenue in the last 12 months** [T1] -- determines category
2. **Activity type** [T1] -- services (locacion de servicios) vs goods (venta de cosas muebles)
3. **Commercial premises area** [T1] -- for goods-selling categories
4. **Annual electricity consumption** [T1] -- for goods-selling categories
5. **Annual rent paid** [T1] -- for goods-selling categories
6. **Unit price of goods** [T1] -- max unit price restriction applies
7. **Number of employees** [T1] -- affects category eligibility
8. **Whether enrolled in obra social (health coverage)** [T1]

**If annual gross revenue exceeds the maximum Monotributo threshold, STOP. Client must be in the Regimen General (IVA + Ganancias). This skill does not cover the general regime.**

---

## Step 1: Monotributo Structure [T1]

**Legislation:** Ley 24.977, Art. 6-11

The Monotributo is a unified monthly payment replacing:

| Component | What It Replaces |
|-----------|-----------------|
| Impuesto integrado (integrated tax) | Income tax (Ganancias) + VAT (IVA) |
| Aportes jubilatorios (pension) | Self-employed pension contributions (SIPA) |
| Obra social (health coverage) | Mandatory health insurance contribution |

### Key Benefits [T1]

- Simplified compliance -- one monthly payment
- No separate IVA filing or Ganancias return
- No need for detailed expense tracking
- Fixed monthly cost known in advance

---

## Step 2: Category Table (2025) [T1]

**Legislation:** Ley 24.977, Art. 8; amounts updated periodically by AFIP resolution

**IMPORTANT:** These thresholds are updated semi-annually (January and July) by AFIP resolution. The amounts below are illustrative for 2025. Always verify current thresholds at afip.gob.ar.

### Services Categories [T1]

| Cat. | Max Annual Revenue (ARS) | Impuesto Integrado (ARS/month) | Aportes Jubilatorios (ARS/month) | Obra Social (ARS/month) | Total Monthly (ARS) |
|------|--------------------------|-------------------------------|--------------------------------|------------------------|-------------------|
| A | ~2,108,288 | ~1,047 | ~5,540 | ~7,402 | ~13,989 |
| B | ~3,133,941 | ~2,014 | ~6,094 | ~7,402 | ~15,510 |
| C | ~4,387,518 | ~3,441 | ~6,703 | ~7,402 | ~17,546 |
| D | ~5,449,094 | ~5,658 | ~7,374 | ~7,402 | ~20,434 |
| E | ~6,416,528 | ~8,904 | ~8,186 | ~7,402 | ~24,492 |
| F | ~8,020,660 | ~12,776 | ~8,837 | ~7,402 | ~29,015 |
| G | ~9,624,792 | ~17,029 | ~9,520 | ~7,402 | ~33,951 |
| H | ~11,916,410 | ~30,454 | ~10,510 | ~7,402 | ~48,366 |

### Goods Categories (higher thresholds) [T1]

Categories A through K apply for goods sales, with higher revenue ceilings but additional physical parameters (premises area, electricity, rent). Categories I, J, K are goods-only.

| Cat. | Max Annual Revenue (ARS) |
|------|--------------------------|
| I | ~13,337,213 |
| J | ~15,285,088 |
| K | ~16,957,968 |

**All amounts are approximate. AFIP updates these semi-annually. Verify at afip.gob.ar.**

---

## Step 3: Physical Parameter Limits (Goods) [T1]

**Legislation:** Ley 24.977, Art. 8

| Parameter | Limits (vary by category) |
|-----------|--------------------------|
| Premises area (superficie afectada) | From 30 m2 (Cat A) to 200 m2 (Cat K) |
| Electricity consumed (energia electrica) | From 3,330 kW (Cat A) to 20,000 kW (Cat K) |
| Rent paid (alquileres devengados) | Increasing ceilings per category |
| Unit price of goods | Max ~ARS 180,589 per unit (verify -- updated regularly) |

Services categories do NOT have premises, electricity, or rent parameters.

---

## Step 4: Recategorization [T1]

**Legislation:** Ley 24.977, Art. 9

| Rule | Detail |
|------|--------|
| Frequency | Semi-annual (January and July) |
| Basis | Revenue and parameters over the preceding 12 months |
| Deadline | January 20 and July 20 |
| Automatic | AFIP may recategorize automatically based on electronic invoice data |
| Effect | New category applies from the month following recategorization |

If the client remains in the same category, no action is needed.

---

## Step 5: Exclusion Rules [T1/T3]

**Legislation:** Ley 24.977, Art. 20-21

### Causes for Exclusion [T1]

| Cause | Effect |
|-------|--------|
| Revenue exceeds Cat H (services) or Cat K (goods) | Automatic exclusion |
| Unit price exceeds limit | Exclusion |
| More than 3 simultaneous business locations | Exclusion |
| Imports in the last 12 months exceed threshold | Exclusion |
| More than specified number of employees | Exclusion |

### Consequences of Exclusion [T3]

- ESCALATE. Client must transition to Regimen General (IVA + Ganancias)
- Retroactive effect from the date the exclusion cause arose
- Must register for IVA and file Ganancias returns
- [T3] Refer to contador publico for transition planning

---

## Step 6: Payment and Compliance [T1]

| Item | Detail |
|------|--------|
| Payment deadline | 20th of each month |
| Payment method | Via VEP (Volante Electronico de Pago), debito automatico, or Pago Facil/Rapipago |
| Electronic invoicing | Mandatory -- must issue facturas electronicas via AFIP (Factura C for Monotributo) |
| Invoice type | Factura C (no IVA discrimination) |
| Annual informativa | Declaracion jurada informativa (annual informational return) -- some categories |

### Factura C Requirements [T1]

| Element | Detail |
|---------|--------|
| CUIT of issuer | Tax ID |
| Category letter | Current Monotributo category |
| Description of service/goods | Sufficient detail |
| Total amount | No separate IVA line (IVA is included in Monotributo) |
| CAE (Codigo de Autorizacion Electronico) | From AFIP's online invoicing system |

---

## Step 7: Edge Case Registry

### EC1 -- Revenue approaching category ceiling [T2]
**Situation:** Freelancer in Category D with 11 months of revenue at ARS 5,200,000. One month remaining.
**Resolution:** If 12-month rolling revenue exceeds Category D ceiling, must recategorize to E at next semi-annual window. If it exceeds all ceilings, exclusion applies. [T2] Flag for reviewer to monitor and advise.

### EC2 -- Mixed services and goods [T2]
**Situation:** Client provides consulting (services) and sells physical products (goods).
**Resolution:** AFIP considers the primary activity. If goods sales are incidental, services categories apply. If both are significant, the higher threshold (goods) categories may apply, but all physical parameters must also be met. [T2] Flag for reviewer.

### EC3 -- Monotributo Social [T1]
**Situation:** Low-income client asks about Monotributo Social.
**Resolution:** Monotributo Social is a reduced-cost version for vulnerable populations, cooperatives, and social economy workers. Different eligibility criteria. Reduced or zero impuesto integrado. [T2] Verify eligibility with AFIP or social services.

### EC4 -- Client receives income from abroad [T2]
**Situation:** Freelance developer invoices US clients.
**Resolution:** Foreign-source income IS included in Monotributo revenue thresholds. Client must issue Factura E (exportacion de servicios). Currency conversion at official rate. [T2] Flag for reviewer -- foreign exchange regulations (CEPO) may affect receipt of funds.

### EC5 -- Client wants to leave Monotributo voluntarily [T1]
**Situation:** Client growing rapidly, wants to transition to Regimen General before forced exclusion.
**Resolution:** Can voluntarily renounce Monotributo and register for IVA + Ganancias. Effective from the first day of the month following renunciation. Cannot return to Monotributo for 3 years.

### EC6 -- Late payment penalties [T1]
**Situation:** Client missed 3 months of Monotributo payments.
**Resolution:** Interest accrues on unpaid amounts. After prolonged non-payment, AFIP may suspend the CUIT and the client loses obra social coverage. Must regularize through AFIP's payment plan system (Mis Facilidades).

---

## Step 8: Test Suite

### Test 1 -- Standard services freelancer, Category D
**Input:** Freelance consultant, annual revenue ARS 5,000,000, services only.
**Expected output:**
- Category D (revenue <= ~5,449,094)
- Monthly payment: ~ARS 20,434 (impuesto integrado ~5,658 + aportes ~7,374 + obra social ~7,402)
- Annual cost: ~ARS 245,208

### Test 2 -- Low-income Category A
**Input:** Freelance tutor, annual revenue ARS 1,500,000.
**Expected output:**
- Category A (revenue <= ~2,108,288)
- Monthly payment: ~ARS 13,989
- Annual cost: ~ARS 167,868

### Test 3 -- Goods seller, Category I
**Input:** Online retailer, annual revenue ARS 12,000,000, premises 80 m2, unit price ARS 50,000.
**Expected output:**
- Category I (goods, revenue <= ~13,337,213)
- Must verify premises area, electricity, rent are within limits
- Monthly payment per Category I table

### Test 4 -- Exclusion trigger
**Input:** Services freelancer, 12-month revenue ARS 13,000,000.
**Expected output:**
- Exceeds Category H ceiling (~11,916,410) for services
- EXCLUDED from Monotributo
- Must register for Regimen General (IVA + Ganancias)
- ESCALATE to contador publico

### Test 5 -- Recategorization needed
**Input:** Currently Category B. Trailing 12-month revenue = ARS 4,000,000.
**Expected output:**
- Exceeds Category B (~3,133,941) but within Category C (~4,387,518)
- Must recategorize to C at next semi-annual window
- New monthly payment: ~ARS 17,546

---

## PROHIBITIONS

- NEVER allow Monotributo for revenue exceeding the maximum category threshold -- client must be in Regimen General
- NEVER issue Factura A or B from a Monotributo taxpayer -- Monotributo uses Factura C (or E for exports)
- NEVER discriminate IVA on a Monotributo invoice -- IVA is embedded in the unified payment
- NEVER ignore physical parameters for goods sellers -- revenue alone is insufficient
- NEVER treat Monotributo amounts as fixed forever -- they are updated semi-annually by AFIP
- NEVER allow a client excluded from Monotributo to continue making Monotributo payments
- NEVER ignore the 3-year lockout when voluntarily leaving Monotributo
- NEVER present calculations as definitive -- always label as estimated and direct client to a contador publico

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a contador publico or equivalent licensed practitioner in Argentina) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
