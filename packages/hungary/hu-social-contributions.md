---
name: hu-social-contributions
description: Use this skill whenever asked about Hungarian self-employed social contributions (társadalombiztosítás / TB and szociális hozzájárulási adó / SZOCHO). Trigger on phrases like "SZOCHO", "TB járulék", "Hungarian social contributions", "társadalombiztosítás", "egyéni vállalkozó járulékok", or any question about social contribution obligations for a self-employed client in Hungary. Covers SZOCHO 13%, TB 18.5%, minimum contribution bases. ALWAYS read this skill before touching any Hungary social contributions work.
version: 2.0
---

# Hungary Social Contributions (TB / SZOCHO) -- Self-Employed Skill v2.0

## Section 1 -- Quick reference

| Field | Value |
|---|---|
| Country | Hungary |
| Authority | NAV (Nemzeti Adó- és Vámhivatal) |
| Primary legislation | 2019. évi CXXII. törvény (Tbj. -- Social Insurance Act) |
| Supporting legislation | 2018. évi LII. törvény (Szocho tv.); 2022. évi XIII. törvény (KATA) |
| TB járulék rate | 18.50% (employee-side equivalent) |
| SZOCHO rate | 13.00% (employer-side equivalent) |
| Combined rate | 31.50% |
| Minimum wage (2025) | HUF 266,800/month |
| Guaranteed minimum (skilled) | HUF 326,000/month |
| KATA monthly tax | HUF 50,000 (B2C only) |
| TB payment deadline | 12th of following month |
| Currency | HUF only |
| Contributor | Open Accountants |
| Validated by | Pending -- requires validation by Hungarian adótanácsadó or könyvvizsgáló |
| Validation date | Pending |

---

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

Before computing, you MUST obtain:

1. **Self-employment type** -- egyéni vállalkozó (sole proprietor) vs KATA taxpayer vs freelancer?
2. **Monthly income / chosen contribution base**
3. **Is the client full-time (főállású) or part-time (mellékállású)?** -- minimum base rules differ
4. **Does the client opt for itemized or flat-rate taxation?**
5. **Any concurrent employment?** -- affects minimum base

**If self-employment type is unknown, STOP.**

### Refusal catalogue

**R-HU-SOC-1 -- Cross-border worker.** Trigger: client works in Hungary and another EU state. Message: "EU Regulation 883/2004 requires A1 certificate determination. Escalate."

### Prohibitions

- NEVER compute without knowing főállású vs mellékállású -- minimum base rules differ completely
- NEVER apply a cap on TB or SZOCHO -- there is no upper ceiling
- NEVER confuse SZOCHO (13%, tax) with TB járulék (18.5%, insurance contribution)
- NEVER advise a KATA taxpayer to invoice companies -- only natural persons since September 2022
- NEVER forget the minimum base is minimum wage (HUF 266,800) or guaranteed minimum (HUF 326,000)
- NEVER state that mellékállású has a minimum base -- it does not
- NEVER present KATA as available for B2B freelancers
- NEVER ignore pro-rating for partial months

---

## Section 3 -- Two-layer contribution system

**Legislation:** Tbj. 2019. évi CXXII.; Szocho tv. 2018. évi LII.

| Layer | Name | Rate | Nature |
|---|---|---|---|
| 1 | TB járulék | 18.50% | Insurance contribution |
| 2 | SZOCHO | 13.00% | Tax |

### TB járulék components

| Component | Rate |
|---|---|
| Pension (nyugdíjjárulék) | 10.00% |
| Health in-kind | 3.00% |
| Health cash benefit | 2.00% |
| Labour market | 1.50% |
| Sickness | 2.00% |
| **Total TB** | **18.50%** |

---

## Section 4 -- Contribution base and minimum rules (2025)

**Legislation:** Tbj. Sections 36-40

### Főállású (full-time) sole proprietor

```
contribution_base = max(actual_monthly_income, minimum_wage)
```

For skilled trade / qualification required:

```
contribution_base = max(actual_monthly_income, guaranteed_minimum_wage)
```

| Minimum base | Monthly |
|---|---|
| Minimum wage | HUF 266,800 |
| Guaranteed minimum (skilled) | HUF 326,000 |

### Mellékállású (part-time, concurrent employment)

- No minimum contribution base
- TB and SZOCHO on actual self-employment income only
- If income is zero, contributions are zero

---

## Section 5 -- Computation steps

### Step 5.1 -- Determine contribution base

```
IF mellékállású:
    base = actual_self_employment_income
ELIF skilled_trade:
    base = max(actual_income, 326,000)
ELSE:
    base = max(actual_income, 266,800)
```

### Step 5.2 -- Monthly contributions

```
TB_monthly = base x 18.50%
SZOCHO_monthly = base x 13.00%
total_monthly = TB_monthly + SZOCHO_monthly
```

### Step 5.3 -- Annual and quarterly

```
annual_total = total_monthly x 12
quarterly_payment = total_monthly x 3
```

---

## Section 6 -- Payment schedule and tax deductibility

### Payment schedule

| Obligation | Frequency | Due date |
|---|---|---|
| TB járulék | Monthly | 12th of following month |
| SZOCHO | Monthly | 12th of following month |
| Annual reconciliation | Annually | With SZJA return (May 20) |

Monthly declarations (08-as bevallás) filed to NAV.

### Tax deductibility

| Question | Answer |
|---|---|
| Is TB deductible? | Partially -- pension component (10%) is deductible |
| Is SZOCHO deductible? | YES -- business expense for sole proprietors |

---

## Section 7 -- KATA regime and flat-rate taxation

### KATA (from September 2022)

| Parameter | Value |
|---|---|
| Fixed monthly tax | HUF 50,000 |
| Covers | Income tax + social contributions |
| Eligibility | Individual service provider to natural persons only |
| Revenue limit | HUF 18,000,000/year |

KATA replaces TB + SZOCHO + income tax. Invoicing legal entities NOT permitted since September 2022.

### Flat-rate taxation (átalányadó)

Income tax base determined by fixed percentage of revenue. TB and SZOCHO still calculated on at least minimum wage base. Flag for reviewer to confirm base interaction.

---

## Section 8 -- Edge case registry

### EC1 -- Mellékállású, zero income
**Situation:** Employed full-time, side self-employment income HUF 0.
**Resolution:** Base = HUF 0. Contributions = HUF 0.

### EC2 -- First month, partial activity
**Situation:** Registered on the 15th of the month.
**Resolution:** Pro-rated. Minimum base = minimum wage / 30 x days active.

### EC3 -- Very high income, no cap
**Situation:** Monthly income HUF 2,000,000.
**Resolution:** TB: HUF 370,000. SZOCHO: HUF 260,000. Total: HUF 630,000. No cap.

### EC4 -- KATA taxpayer invoicing a company
**Situation:** KATA taxpayer receives contract from a Kft.
**Resolution:** NOT permitted. Client must leave KATA or refuse the contract.

### EC5 -- Suspension of activity (szüneteltetés)
**Situation:** Sole proprietor suspends activity for 3 months.
**Resolution:** No contributions during suspension. Health coverage may lapse.

### EC6 -- Multiple self-employed activities
**Situation:** Two sole proprietorships.
**Resolution:** One set of minimum contributions. Combined income, minimum applied once.

---

## Section 9 -- Reviewer escalation protocol

When a situation requires reviewer judgement:

```
REVIEWER FLAG
Tier: T2
Client: [name]
Situation: [description]
Issue: [what is ambiguous]
Options: [possible treatments]
Recommended: [most likely correct treatment and why]
Action Required: Qualified adótanácsadó must confirm before advising client.
```

When a situation is outside skill scope:

```
ESCALATION REQUIRED
Tier: T3
Client: [name]
Situation: [description]
Issue: [outside skill scope]
Action Required: Do not advise. Refer to qualified adótanácsadó. Document gap.
```

---

## Section 10 -- Test suite

### Test 1 -- Standard at minimum wage
**Input:** Főállású, income HUF 200,000 (below min wage), no qualification, age 35.
**Expected output:** Base HUF 266,800. TB HUF 49,358. SZOCHO HUF 34,684. Total HUF 84,042. Annual HUF 1,008,504.

### Test 2 -- Above minimum wage
**Input:** Főállású, income HUF 500,000, age 40.
**Expected output:** Base HUF 500,000. TB HUF 92,500. SZOCHO HUF 65,000. Total HUF 157,500.

### Test 3 -- Guaranteed minimum wage
**Input:** Skilled trade, income HUF 300,000, age 38.
**Expected output:** Base HUF 326,000. TB HUF 60,310. SZOCHO HUF 42,380. Total HUF 102,690.

### Test 4 -- Mellékállású
**Input:** Employed full-time, side income HUF 100,000, age 30.
**Expected output:** Base HUF 100,000. Total HUF 31,500.

### Test 5 -- Mellékállású zero income
**Input:** Employed, side income HUF 0, age 28.
**Expected output:** Total HUF 0.

### Test 6 -- KATA taxpayer
**Input:** B2C services, turnover HUF 10,000,000.
**Expected output:** Monthly HUF 50,000. Annual HUF 600,000.

### Test 7 -- High income
**Input:** Főállású, income HUF 3,000,000, age 50.
**Expected output:** TB HUF 555,000. SZOCHO HUF 390,000. Total HUF 945,000.

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
