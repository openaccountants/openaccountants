---
name: hu-social-contributions
description: Use this skill whenever asked about Hungarian self-employed social contributions (társadalombiztosítás / TB and szociális hozzájárulási adó / SZOCHO). Trigger on phrases like "SZOCHO", "TB járulék", "Hungarian social contributions", "társadalombiztosítás", "egyéni vállalkozó járulékok", or any question about social contribution obligations for a self-employed client in Hungary. Covers SZOCHO 13%, TB 18.5%, minimum contribution bases. ALWAYS read this skill before touching any Hungary social contributions work.
---

# Hungary Social Contributions (TB / SZOCHO) -- Self-Employed Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Hungary |
| Jurisdiction Code | HU |
| Primary Legislation | 2019. évi CXXII. törvény (Tbj. -- Social Insurance Act) |
| Supporting Legislation | 2018. évi LII. törvény (Szocho tv. -- Social Contribution Tax Act) |
| Tax Authority | NAV (Nemzeti Adó- és Vámhivatal) |
| Contributor | Open Accountants |
| Validated By | Pending -- requires validation by Hungarian adótanácsadó or könyvvizsgáló |
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

1. **Self-employment type** [T1] -- egyéni vállalkozó (sole proprietor) vs KATA/KIVA taxpayer vs freelancer (megbízási szerződés)?
2. **Monthly income / chosen contribution base** [T1]
3. **Is the client a full-time sole proprietor or part-time (mellékállású)?** [T1] -- minimum base rules differ
4. **Does the client opt for itemized or flat-rate taxation?** [T1]
5. **Any concurrent employment?** [T1] -- affects minimum base and SZOCHO

**If self-employment type is unknown, STOP.**

---

## Step 1: Two-Layer System [T1]

**Legislation:** Tbj. 2019. évi CXXII.; Szocho tv. 2018. évi LII.

Hungary has TWO separate social contribution obligations for self-employed:

| Layer | Name | Rate | Who Pays | Nature |
|-------|------|------|----------|--------|
| 1 | TB járulék (social insurance contribution) | 18.50% | Individual (employee-side equivalent) | Insurance contribution |
| 2 | SZOCHO (szociális hozzájárulási adó) | 13.00% | Individual (employer-side equivalent for self-employed) | Tax |

**Combined rate: 31.50% of contribution base.**

---

## Step 2: Contribution Base [T1]

**Legislation:** Tbj. §36-40

### Egyéni Vállalkozó (Sole Proprietor) -- Itemized Taxation

| Base Rule | Amount |
|-----------|--------|
| TB base = at least the minimum wage | HUF 266,800/month (2025) |
| SZOCHO base = at least the minimum wage | HUF 266,800/month (2025) |
| If the client has a guaranteed minimum wage activity (skilled trade) | HUF 326,000/month (2025) |

The actual contribution base is the **higher of**: (a) the actual declared income, or (b) the minimum wage.

### Minimum vs Actual

```
contribution_base = max(actual_monthly_income, minimum_wage)
```

For guaranteed minimum wage activities (requiring qualification/diploma):

```
contribution_base = max(actual_monthly_income, guaranteed_minimum_wage)
```

### Part-time (Mellékállású) Sole Proprietor

If the client has concurrent full-time employment:

- No minimum contribution base for TB
- TB paid on actual self-employment income only
- SZOCHO: same rule -- actual income, no minimum

---

## Step 3: Rates Breakdown (2025) [T1]

### TB Járulék (18.5%)

| Component | Rate |
|-----------|------|
| Pension contribution (nyugdíjjárulék) | 10.00% |
| Health insurance in-kind (egészségbiztosítási járulék természetben) | 3.00% |
| Health insurance cash benefit (egészségbiztosítási járulék pénzbeli) | 2.00% |
| Labour market contribution (munkaerőpiaci járulék) | 1.50% |
| Sickness contribution (betegségbiztosítási járulék) | 2.00% |
| **Total TB** | **18.50%** |

### SZOCHO (13%)

| Component | Rate |
|-----------|------|
| Szociális hozzájárulási adó | 13.00% |

### Combined

| Total | Rate | Monthly at Minimum Wage |
|-------|------|------------------------|
| TB + SZOCHO on minimum wage (HUF 266,800) | 31.50% | HUF 84,042 |
| TB + SZOCHO on guaranteed minimum (HUF 326,000) | 31.50% | HUF 102,690 |

---

## Step 4: Computation Steps [T1]

### Step 4.1 -- Determine contribution base

```
IF mellékállású (part-time, has full-time employment):
    base = actual_self_employment_income  # no minimum
ELIF skilled_trade_or_qualification_required:
    base = max(actual_income, 326,000)  # guaranteed minimum wage
ELSE:
    base = max(actual_income, 266,800)  # minimum wage
```

### Step 4.2 -- Monthly contributions

```
TB_monthly = base × 18.50%
SZOCHO_monthly = base × 13.00%
total_monthly = TB_monthly + SZOCHO_monthly
```

### Step 4.3 -- Annual total

```
annual_total = total_monthly × 12
```

### Step 4.4 -- Quarterly advance payment

Sole proprietors pay quarterly to NAV:

```
quarterly_payment = total_monthly × 3
```

---

## Step 5: Payment Schedule [T1]

**Legislation:** Art. 50/A; Szja tv.

| Obligation | Frequency | Due Date |
|------------|-----------|----------|
| TB járulék | Monthly | 12th of following month |
| SZOCHO | Monthly | 12th of following month |
| Annual reconciliation | Annually | With income tax return (May 20) |

- Self-employed sole proprietors file monthly declarations (08-as bevallás) to NAV
- Annual reconciliation happens via the personal income tax return (SZJA bevallás)

---

## Step 6: KATA Regime (Simplified) [T1]

**Legislation:** 2022. évi XIII. törvény (new KATA from 2022)

### Current KATA (from September 2022)

| Parameter | Value |
|-----------|-------|
| Fixed monthly tax | HUF 50,000 |
| Covers | Income tax + social contributions |
| Eligibility | Individual service provider to natural persons only (not to companies) |
| Revenue limit | HUF 18,000,000/year |

**KATA replaces TB + SZOCHO + personal income tax with a single flat payment.**

Limitation: since September 2022, KATA taxpayers can ONLY invoice natural persons (individuals), not legal entities. This severely limits its applicability for B2B freelancers.

---

## Step 7: Tax Deductibility [T1]

| Question | Answer |
|----------|--------|
| Is TB deductible from income tax base? | Partially -- pension contribution (10%) is deductible |
| Is SZOCHO deductible? | YES -- deductible as a business expense for sole proprietors |
| How does this affect the calculation? | SZOCHO reduces the income tax base; TB járulék does not (except pension component) |

---

## Step 8: Edge Case Registry

### EC1 -- Mellékállású (part-time) sole proprietor [T1]
**Situation:** Client is employed full-time and has a side sole proprietorship.
**Resolution:** No minimum contribution base applies. TB and SZOCHO are calculated on actual self-employment income only. If income is zero, contributions are zero.

### EC2 -- First month of activity [T1]
**Situation:** Client registers as sole proprietor on the 15th of the month.
**Resolution:** Contributions are pro-rated for the partial month. Minimum base is also pro-rated (daily: minimum wage / 30 x days active).

### EC3 -- Sole proprietor with very high income [T1]
**Situation:** Monthly self-employment income is HUF 2,000,000.
**Resolution:** There is no upper cap on the SZOCHO base. TB also has no cap. Both apply at full rates on the entire income. TB: HUF 370,000. SZOCHO: HUF 260,000. Total: HUF 630,000/month.

### EC4 -- KATA taxpayer invoicing a company [T1]
**Situation:** KATA taxpayer receives a contract from a Kft. (company).
**Resolution:** Under the 2022 KATA rules, invoicing legal entities is NOT permitted. The client must either leave KATA or refuse the contract. Invoicing a company results in automatic exit from KATA.

### EC5 -- Suspension of activity (szüneteltetés) [T1]
**Situation:** Sole proprietor suspends activity for 3 months.
**Resolution:** During suspension (registered with NAV), no contribution obligation arises. No minimum base applies for suspended months. Health insurance coverage may lapse -- client should verify.

### EC6 -- Flat-rate taxation (átalányadó) [T2]
**Situation:** Client opts for flat-rate taxation.
**Resolution:** Under átalányadó, the income tax base is determined by a fixed percentage of revenue (40%/80%/90% depending on activity). However, TB and SZOCHO are still calculated on at least the minimum wage base. [T2] -- confirm whether the átalányadó base or minimum wage applies for contributions.

### EC7 -- Cross-border worker [T2]
**Situation:** Client lives in Hungary but provides services in Austria.
**Resolution:** Under EU Regulation 883/2004, social insurance is generally paid in one country. [T2] -- A1 certificate determination required.

### EC8 -- Multiple self-employed activities [T1]
**Situation:** Client has two sole proprietorships.
**Resolution:** Only one set of minimum contributions applies. TB and SZOCHO are calculated on the combined income from all self-employed activities, with the minimum base applied once.

---

## Step 9: Reviewer Escalation Protocol

When Claude identifies a [T2] situation:

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

---

## Step 10: Test Suite

### Test 1 -- Standard sole proprietor at minimum wage base
**Input:** Full-time egyéni vállalkozó, actual income HUF 200,000/month (below minimum wage), no qualification required, age 35.
**Expected output:** Base = HUF 266,800 (minimum wage floor). TB: HUF 49,358. SZOCHO: HUF 34,684. Monthly total: HUF 84,042. Annual: HUF 1,008,504.

### Test 2 -- Sole proprietor above minimum wage
**Input:** Full-time egyéni vállalkozó, actual income HUF 500,000/month, age 40.
**Expected output:** Base = HUF 500,000. TB: HUF 92,500. SZOCHO: HUF 65,000. Monthly total: HUF 157,500. Annual: HUF 1,890,000.

### Test 3 -- Guaranteed minimum wage activity
**Input:** Full-time, skilled trade requiring qualification, actual income HUF 300,000/month, age 38.
**Expected output:** Base = HUF 326,000 (guaranteed minimum). TB: HUF 60,310. SZOCHO: HUF 42,380. Monthly total: HUF 102,690. Annual: HUF 1,232,280.

### Test 4 -- Mellékállású (part-time)
**Input:** Employed full-time, side self-employment income HUF 100,000/month, age 30.
**Expected output:** Base = HUF 100,000 (actual, no minimum). TB: HUF 18,500. SZOCHO: HUF 13,000. Monthly total: HUF 31,500. Annual: HUF 378,000.

### Test 5 -- Mellékállású zero income
**Input:** Employed full-time, side self-employment income HUF 0/month, age 28.
**Expected output:** Base = HUF 0. TB: HUF 0. SZOCHO: HUF 0. No contribution obligation.

### Test 6 -- KATA taxpayer
**Input:** Individual services to natural persons only, turnover HUF 10,000,000/year.
**Expected output:** Monthly KATA payment: HUF 50,000. Annual: HUF 600,000. No separate TB or SZOCHO.

### Test 7 -- High income, no cap
**Input:** Full-time egyéni vállalkozó, income HUF 3,000,000/month, age 50.
**Expected output:** TB: HUF 555,000. SZOCHO: HUF 390,000. Monthly total: HUF 945,000. Annual: HUF 11,340,000.

---

## PROHIBITIONS

- NEVER compute without knowing főállású vs mellékállású status -- minimum base rules differ completely
- NEVER apply a cap on TB or SZOCHO -- there is no upper ceiling on contribution bases
- NEVER confuse SZOCHO (13%, tax) with TB járulék (18.5%, insurance contribution) -- they are separate obligations
- NEVER advise a KATA taxpayer to invoice companies -- only natural persons are permitted under post-2022 KATA
- NEVER forget that the minimum base is the minimum wage (HUF 266,800) or guaranteed minimum (HUF 326,000)
- NEVER state that mellékállású has a minimum base -- it does not
- NEVER present KATA as available for B2B freelancers -- it is restricted to B2C since September 2022
- NEVER ignore pro-rating for partial months of activity
- NEVER advise on cross-border situations without flagging for reviewer

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
