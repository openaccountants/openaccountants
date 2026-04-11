---
name: pt-social-contributions
description: Use this skill whenever asked about Portuguese self-employed social contributions (contribuições para a Segurança Social). Trigger on phrases like "Segurança Social trabalhador independente", "Portuguese social contributions", "declaração trimestral SS", "contribuições independente Portugal", or any question about social contribution obligations for a self-employed client in Portugal. Covers the 21.4% rate on 70% of relevant income, quarterly declaration, and first-year exemption. ALWAYS read this skill before touching any Portugal social contributions work.
---

# Portugal Social Contributions -- Self-Employed Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Portugal |
| Jurisdiction Code | PT |
| Primary Legislation | Código Contributivo (Lei n.o 110/2009, art. 139-170) |
| Supporting Legislation | Decreto Regulamentar 1-A/2011; annual updates via Portaria |
| Tax Authority | AT (Autoridade Tributária -- for tax); ISS (Instituto da Segurança Social -- for contributions) |
| Contributor | Open Accountants |
| Validated By | Pending -- requires validation by Portuguese contabilista certificado |
| Validation Date | Pending |
| Skill Version | 1.0 |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag and present options.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess.

---

## Step 0: Client Onboarding Questions

Before computing, you MUST know:

1. **Activity type** [T1] -- trabalhador independente (self-employed), empresário em nome individual (sole proprietor), or profissional liberal?
2. **Gross quarterly income (rendimento relevante)** [T1] -- from the quarterly declaration
3. **Year of activity** [T1] -- first 12 months exempt from contributions
4. **Any concurrent employment?** [T1] -- reduced rate may apply
5. **Category of services** [T1] -- services (prestação de serviços) vs sales of goods (venda de bens)?
6. **Does the client have an accountant (contabilidade organizada)?** [T1] -- affects relevant income calculation

**If income type (services vs goods) is unknown, STOP. The relevant income percentage differs.**

---

## Step 1: Contribution Rate [T1]

**Legislation:** Código Contributivo, art. 168

| Category | Rate |
|----------|------|
| Self-employed (trabalhador independente) | **21.4%** |
| Self-employed with concurrent employment (>= minimum contribution from employment) | **21.4%** (but may be exempt -- see Step 6) |
| Empresário em nome individual (with employees) | **25.2%** (higher rate) |

---

## Step 2: Relevant Income Calculation [T1]

**Legislation:** Código Contributivo, art. 162

### Without Organized Accounting (Sem contabilidade organizada)

The contribution base is NOT the actual income but a deemed percentage:

| Income Type | Relevant Income % | Example: EUR 10,000 gross |
|-------------|-------------------|---------------------------|
| Prestação de serviços (services) | 70% of gross | EUR 7,000 |
| Produção e venda de bens (production/sale of goods) | 20% of gross | EUR 2,000 |
| Mixed (services + goods) | Apply each % to respective category | Weighted |

### With Organized Accounting (Com contabilidade organizada)

Relevant income = actual net profit from accounting records.

### Quarterly Calculation

```
quarterly_relevant_income = sum of relevant_income for the 3 months in the quarter
monthly_relevant_income = quarterly_relevant_income / 3
```

---

## Step 3: Contribution Base and Bounds [T1]

**Legislation:** Código Contributivo, art. 163

```
monthly_contribution_base = monthly_relevant_income
```

### Minimum and Maximum (2025)

| Bound | Amount | Basis |
|-------|--------|-------|
| Minimum monthly base | EUR 480.43 (= IAS) | Indexante dos Apoios Sociais (IAS) 2025 |
| Maximum monthly base | EUR 5,765.16 (= 12 x IAS) | 12 x IAS |

```
monthly_base = clamp(480.43, monthly_relevant_income, 5,765.16)
```

---

## Step 4: Computation Steps [T1]

### Step 4.1 -- Quarterly Declaration

Every quarter, the self-employed person files a Declaração Trimestral with Segurança Social, reporting gross income from the prior quarter.

| Declaration Period | Income Period Covered | Filing Deadline |
|-------------------|-----------------------|-----------------|
| January | Oct--Dec (prior year) | By end of January |
| April | Jan--Mar | By end of April |
| July | Apr--Jun | By end of July |
| October | Jul--Sep | By end of October |

### Step 4.2 -- Calculate monthly relevant income

```
IF services_only (sem contabilidade):
    relevant_income = quarterly_gross × 70% / 3
ELIF goods_only:
    relevant_income = quarterly_gross × 20% / 3
ELIF mixed:
    relevant_income = (services_gross × 70% + goods_gross × 20%) / 3
ELIF contabilidade_organizada:
    relevant_income = quarterly_net_profit / 3
```

### Step 4.3 -- Apply bounds

```
monthly_base = max(480.43, min(relevant_income, 5,765.16))
```

### Step 4.4 -- Calculate monthly contribution

```
monthly_contribution = monthly_base × 21.4%
```

### Step 4.5 -- Contributions apply for the next quarter

The quarterly declaration determines contributions for the following 3 months.

---

## Step 5: Payment Schedule [T1]

| Obligation | Due Date |
|------------|----------|
| Monthly contribution payment | Between 10th and 20th of each month |
| Payment method | Direct debit, ATM, or Segurança Social Direta portal |

- Contributions are payable monthly even though the declaration is quarterly
- Late payment: interest at legal rate + potential loss of benefits

---

## Step 6: Exemptions and Reductions [T1]

**Legislation:** Código Contributivo, art. 157-158

### First 12 Months Exemption

New self-employed workers are **exempt from contributions for the first 12 months** of activity. After 12 months, contributions begin based on the first quarterly declaration.

### Concurrent Employment Exemption

If the self-employed person also has employment where the employer pays at least the minimum contribution base:

- **If employment income >= IAS:** self-employed contributions are reduced or may result in exemption
- **Exemption conditions:** employment contributions must be paid on at least EUR 480.43/month by the employer
- **If self-employed income >= 4 x IAS:** exemption does NOT apply, contributions are mandatory

### Pensioners

Self-employed pensioners pay a reduced rate or may be exempt depending on pension type. [T2] -- confirm with ISS.

---

## Step 7: Tax Deductibility [T1]

| Question | Answer |
|----------|--------|
| Are Segurança Social contributions deductible? | YES -- from gross income for IRS (income tax) purposes |
| Classification | Deductions to income (Category B deductions) |
| When deductible? | In the year they are paid |

---

## Step 8: Edge Case Registry

### EC1 -- First year of activity [T1]
**Situation:** Client opened activity in March 2025.
**Resolution:** Exempt from contributions until February 2026 (12 months). First quarterly declaration due in April 2026 (for Q1 2026 income). Contributions begin from the month following the first declaration.

### EC2 -- Services income below minimum [T1]
**Situation:** Client provides services with quarterly gross EUR 1,000.
**Resolution:** Relevant income = EUR 1,000 x 70% / 3 = EUR 233.33/month. Below minimum of EUR 480.43. Monthly contribution = EUR 480.43 x 21.4% = EUR 102.81.

### EC3 -- Very high income [T1]
**Situation:** Client earns EUR 30,000/quarter from services.
**Resolution:** Relevant income = EUR 30,000 x 70% / 3 = EUR 7,000/month. Capped at EUR 5,765.16. Monthly contribution = EUR 5,765.16 x 21.4% = EUR 1,233.74.

### EC4 -- Mixed services and goods [T1]
**Situation:** Client earns EUR 6,000 from services and EUR 15,000 from goods in the quarter.
**Resolution:** Relevant income = (EUR 6,000 x 70% + EUR 15,000 x 20%) / 3 = (EUR 4,200 + EUR 3,000) / 3 = EUR 2,400/month. Contribution = EUR 2,400 x 21.4% = EUR 513.60/month.

### EC5 -- Concurrent employment with salary above IAS [T1]
**Situation:** Client is employed at EUR 1,200/month and self-employed with EUR 3,000/quarter services.
**Resolution:** Employment salary > IAS. Self-employed relevant income = EUR 3,000 x 70% / 3 = EUR 700/month. Since this is < 4 x IAS (EUR 1,921.72), the employment exemption applies. Self-employed contributions: EUR 0.

### EC6 -- Self-employed with organized accounting [T2]
**Situation:** Client has contabilidade organizada and reports quarterly net profit.
**Resolution:** Relevant income = actual net profit (not deemed %). If net profit is negative, minimum base still applies. [T2] -- confirm profit calculation methodology with contabilista.

### EC7 -- Recibos verdes (green receipts) income [T1]
**Situation:** Client issues recibos verdes for freelance services.
**Resolution:** This IS self-employed income. Standard 70% relevant income rule applies. All recibos verdes amounts are reported in the quarterly declaration.

### EC8 -- Cross-border EU worker [T2]
**Situation:** Client is a Portuguese resident providing services in Spain.
**Resolution:** Under EU Regulation 883/2004, social insurance in one country. [T2] -- A1 certificate required.

---

## Step 9: Test Suite

### Test 1 -- Standard services, mid-range
**Input:** Quarterly gross services EUR 9,000, no employment, established.
**Expected output:** Relevant income = EUR 9,000 x 70% / 3 = EUR 2,100/month. Contribution = EUR 2,100 x 21.4% = EUR 449.40/month. Annual: EUR 5,392.80.

### Test 2 -- Minimum base applies
**Input:** Quarterly gross services EUR 1,500.
**Expected output:** Relevant income = EUR 1,500 x 70% / 3 = EUR 350/month. Below minimum. Base = EUR 480.43. Contribution = EUR 102.81/month.

### Test 3 -- Maximum base applies
**Input:** Quarterly gross services EUR 30,000.
**Expected output:** Relevant income = EUR 7,000/month. Capped at EUR 5,765.16. Contribution = EUR 1,233.74/month.

### Test 4 -- First year exempt
**Input:** Activity opened 4 months ago, quarterly gross EUR 12,000.
**Expected output:** Exempt from contributions (within first 12 months). Contributions = EUR 0.

### Test 5 -- Goods-only income
**Input:** Quarterly gross goods sales EUR 20,000, no employment.
**Expected output:** Relevant income = EUR 20,000 x 20% / 3 = EUR 1,333.33/month. Contribution = EUR 1,333.33 x 21.4% = EUR 285.33/month.

### Test 6 -- Concurrent employment, exemption applies
**Input:** Employment salary EUR 1,500/month, self-employed quarterly services EUR 2,000.
**Expected output:** Self-employed relevant income = EUR 466.67/month (below 4 x IAS). Employment exemption applies. Self-employed contributions = EUR 0.

### Test 7 -- Empresário em nome individual
**Input:** Sole proprietor with employees, quarterly services EUR 15,000.
**Expected output:** Rate = 25.2% (not 21.4%). Relevant income = EUR 3,500/month. Contribution = EUR 3,500 x 25.2% = EUR 882.00/month.

---

## PROHIBITIONS

- NEVER apply 21.4% to gross income directly -- the relevant income percentage (70% for services, 20% for goods) must be applied first
- NEVER forget the first 12 months exemption for new self-employed
- NEVER ignore the minimum base of EUR 480.43 (IAS) -- even with zero income, this minimum applies after the exemption period
- NEVER confuse the self-employed rate (21.4%) with the empresário rate (25.2%)
- NEVER present quarterly declaration income as the contribution base -- it must be converted to monthly
- NEVER forget to clamp at the maximum of 12 x IAS (EUR 5,765.16)
- NEVER state that contributions are NOT tax-deductible -- they ARE deductible from IRS income
- NEVER advise on concurrent employment exemption without verifying the 4 x IAS threshold
- NEVER advise on cross-border situations without flagging for reviewer

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
