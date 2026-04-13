---
name: ch-ahv-iv
description: Use this skill whenever asked about Swiss AHV/IV (Alters- und Hinterlassenenversicherung / Invalidenversicherung) social contributions for self-employed individuals. Trigger on phrases like "AHV contributions", "Swiss social security self-employed", "AHV/IV/EO", "Beitragsverfügung", "sliding scale AHV", "Swiss self-employed insurance", or any question about social insurance obligations for a self-employed client in Switzerland. Covers the 5.371-10% sliding scale, EO, minimum contribution, and BVG voluntary pillar 2. ALWAYS read this skill before touching any Switzerland social contributions work.
version: 2.0
---

# Switzerland AHV/IV Contributions -- Self-Employed Skill v2.0

## Section 1 -- Quick reference

| Field | Value |
|---|---|
| Country | Switzerland (Swiss Confederation) |
| Authority | Ausgleichskasse (Compensation Office -- cantonal or professional) |
| Federal oversight | BSV (Bundesamt für Sozialversicherungen) |
| Primary legislation | AHVG (Bundesgesetz über die Alters- und Hinterlassenenversicherung) |
| Supporting legislation | IVG; EOG; AHVV; BVG (Berufliche Vorsorge); DBG |
| Full rate (income >= CHF 58,800) | 10.00% (AHV 8.10% + IV 1.40% + EO 0.50%) |
| Sliding scale range | CHF 9,800 -- CHF 58,800 (rates 5.371% -- 10.00%) |
| Minimum annual contribution | CHF 514 |
| Upper cap | None -- no maximum on AHV/IV/EO contributions |
| Payment frequency | Quarterly advance payments (Akontobeiträge) |
| Final settlement | Upon definitive tax assessment |
| Currency | CHF only |
| Contributor | Open Accountants |
| Validated by | Pending -- requires validation by Swiss Treuhänder or Wirtschaftsprüfer |
| Validation date | Pending |

---

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

Before computing any AHV/IV figure, you MUST obtain:

1. **Self-employment status** -- is the client recognized as selbständig erwerbend by the Ausgleichskasse?
2. **Net earned income from self-employment** -- Reineinkommen from all self-employed activities
3. **Which Ausgleichskasse?** -- cantonal or professional (e.g., Medisuisse for doctors)
4. **Age** -- contributions start at 18 (20 for employed), end at reference age (65M/65F from 2028)
5. **Any concurrent employment?** -- employer already pays AHV on wages
6. **Interest in voluntary BVG (Pillar 2)?** -- optional for self-employed

**If self-employment status is not confirmed by the Ausgleichskasse, STOP. The Ausgleichskasse determines status, not the client.**

### Refusal catalogue

**R-CH-AHV-1 -- Cantonal supplements (AG/AI).** Trigger: question about cantonal-specific AHV supplement rules. Message: "Cantonal AHV supplement rules are outside this skill's scope. Consult the relevant cantonal Ausgleichskasse."

**R-CH-AHV-2 -- Military service credits.** Trigger: question about military service contribution credits. Message: "Military service contribution credits require specialist review. Escalate to qualified Treuhänder."

### Prohibitions

- NEVER determine self-employment status yourself -- only the Ausgleichskasse can confirm this
- NEVER apply the full 10% rate to incomes below CHF 58,800 -- the sliding scale must be used
- NEVER state there is a maximum cap on AHV/IV contributions -- there is no upper cap in Switzerland
- NEVER ignore the CHF 514 minimum contribution -- it always applies regardless of income level
- NEVER confuse the self-employed contribution (full rate) with the employee half-rate (5.00%)
- NEVER forget the Freibetrag (CHF 16,800) for persons past reference age
- NEVER present AHV figures without noting that final settlement depends on the definitive tax assessment
- NEVER ignore FAK cantonal obligations -- rates and rules vary by canton

---

## Section 3 -- Contribution base

**Legislation:** AHVG art. 9; AHVV art. 17-22

```
contribution_base = net_self_employment_income
                  = gross_revenue - business_expenses - depreciation
                  + capital_gains_on_business_assets (if applicable)
```

### Key rules for the base

1. The base is the Reineinkommen (net income) from self-employment as determined by the tax assessment
2. Personal AHV/IV/EO contributions paid are added back (50% gross-up rule): the actual base = Reineinkommen + 50% of contributions due (to approximate the employer half)
3. Interest on business capital is deducted from the base
4. The Ausgleichskasse uses the definitive tax assessment from the cantonal tax authority

---

## Section 4 -- Rates and thresholds (2025)

**Legislation:** AHVG art. 8; AHVV art. 21

### Rate components

| Component | Full rate (income >= CHF 58,800) |
|---|---|
| AHV (old-age and survivors) | 8.10% |
| IV (disability) | 1.40% |
| EO (income replacement / maternity) | 0.50% |
| **Total** | **10.00%** |

### Sliding scale (Sinkende Beitragsskala)

| Annual net income | AHV/IV/EO rate |
|---|---|
| Up to CHF 9,800 | Minimum contribution (CHF 514/year) |
| CHF 9,800 | 5.371% |
| CHF 17,400 | 5.509% |
| CHF 21,400 | 5.666% |
| CHF 25,200 | 5.859% |
| CHF 28,900 | 6.101% |
| CHF 32,600 | 6.405% |
| CHF 36,100 | 6.783% |
| CHF 39,600 | 7.226% |
| CHF 42,900 | 7.726% |
| CHF 46,200 | 8.271% |
| CHF 49,200 | 8.849% |
| CHF 52,200 | 9.444% |
| CHF 55,400 | 9.953% |
| CHF 58,800 and above | 10.000% |

### Additional charges

- **FAK (Familienausgleichskasse):** some cantons require self-employed to pay FAK contributions, typically 1-3%
- **Administration costs (Verwaltungskosten):** typically 1-5% of contributions, charged by the Ausgleichskasse

### Voluntary BVG (Pillar 2) and Pillar 3a

| Parameter | Amount (2025) |
|---|---|
| BVG minimum insured salary | CHF 22,050 |
| BVG maximum insured salary | CHF 88,200 |
| Pillar 3a with BVG | Max CHF 7,056 |
| Pillar 3a without BVG | Max 20% of net income, up to CHF 35,280 |

Self-employed persons are NOT obligatorily insured under BVG but may join voluntarily. Contribution rates are age-dependent: 7% (25-34), 10% (35-44), 15% (45-54), 18% (55-65). Confirm specific fund rules with the Stiftung before advising.

---

## Section 5 -- Computation steps

### Step 5.1 -- Determine net income and apply gross-up

```
raw_income = net_self_employment_income_per_tax_assessment
adjusted_income = raw_income + (AHV_contributions_paid x 50%)
```

In practice, the Ausgleichskasse computes this via published tables.

### Step 5.2 -- Apply sliding scale or full rate

```
IF adjusted_income <= 9,800:
    annual_contribution = 514  (minimum)
ELIF adjusted_income < 58,800:
    annual_contribution = adjusted_income x sliding_scale_rate  (from table)
ELSE:
    annual_contribution = adjusted_income x 10.00%
```

### Step 5.3 -- Add FAK if applicable

```
IF canton_requires_FAK:
    FAK = adjusted_income x cantonal_FAK_rate
    total = annual_contribution + FAK
```

### Step 5.4 -- Administration costs

The Ausgleichskasse charges Verwaltungskosten, typically 1-5% of contributions.

---

## Section 6 -- Payment schedule and tax deductibility

**Legislation:** AHVV art. 34-36; DBG art. 33(1)(d)

### Payment schedule

- Self-employed pay quarterly advance payments (Akontobeiträge)
- Advances are based on prior-year income or estimated current-year income
- Final settlement occurs after the definitive tax assessment (often 1-2 years later)
- Late payment: Verzugszinsen at 5% per annum (AHVV art. 41bis)
- Advances can be adjusted up or down upon request with justification

### Tax deductibility

| Question | Answer |
|---|---|
| Are AHV/IV/EO contributions deductible? | YES -- from income for federal and cantonal tax |
| Classification | Personal deduction (Versicherungsabzug), not business expense |
| When deductible? | In the year they relate to (accrual basis for contributions) |

---

## Section 7 -- Post-reference-age and concurrent employment

### Person approaching or past reference age

Contributions are due until the end of the month in which the client reaches reference age. After reference age, a Freibetrag of CHF 16,800/year applies -- no contributions on income below this. Above the Freibetrag, standard rates apply but only AHV/EO (no IV).

### Concurrent employment and self-employment

AHV is due separately on self-employment income. No offset between employment and self-employment contributions. Even if total employment income already exceeds the full-rate threshold, self-employment contributions are calculated independently on self-employment income alone.

### Non-cash income / benefits in kind

All income including benefits in kind must be included in the AHV contribution base at fair market value.

### Business cessation mid-year

Contributions are pro-rated for the period of activity. Minimum contribution is also pro-rated (1/12 per month of activity). Final settlement based on actual income for the partial year.

---

## Section 8 -- Edge case registry

### EC1 -- Income below minimum threshold
**Situation:** Client's net self-employment income is CHF 5,000.
**Resolution:** Minimum contribution of CHF 514/year applies. Client cannot pay less than the minimum regardless of income level.

### EC2 -- Concurrent employment and self-employment
**Situation:** Client is employed (AHV paid by employer on salary) and also self-employed.
**Resolution:** AHV is due separately on self-employment income. No offset.

### EC3 -- Capital gains on business assets
**Situation:** Client sells a business asset at a gain.
**Resolution:** Capital gains on business assets (Kapitalgewinne auf Geschäftsvermögen) are subject to AHV/IV/EO contributions as part of the self-employment income base.

### EC4 -- Persons without gainful employment
**Situation:** Client has no income but is resident in Switzerland.
**Resolution:** Non-employed persons pay AHV/IV/EO based on wealth and pension income. Minimum CHF 514/year. Calculation based on Rentnertabelle, confirm with Ausgleichskasse. Flag for reviewer.

### EC5 -- International coordination (EU/EFTA)
**Situation:** Client works in Switzerland and an EU/EFTA country.
**Resolution:** Under the Agreement on Free Movement of Persons, social insurance is generally payable in one country only. A1 certificate required. Escalate to reviewer.

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
Action Required: Qualified Treuhänder must confirm before advising client.
```

When a situation is outside skill scope:

```
ESCALATION REQUIRED
Tier: T3
Client: [name]
Situation: [description]
Issue: [outside skill scope]
Action Required: Do not advise. Refer to qualified Treuhänder. Document gap.
```

---

## Section 10 -- Test suite

### Test 1 -- Income at full rate
**Input:** Net self-employment income CHF 100,000, age 40.
**Expected output:** AHV/IV/EO = CHF 100,000 x 10.00% = CHF 10,000. Plus administration costs.

### Test 2 -- Income in sliding scale range
**Input:** Net self-employment income CHF 40,000, age 35.
**Expected output:** Approximately CHF 40,000 x ~7.2% = ~CHF 2,880 (exact rate from Ausgleichskasse table). Plus administration costs.

### Test 3 -- Minimum contribution
**Input:** Net self-employment income CHF 5,000, age 30.
**Expected output:** Minimum contribution CHF 514/year.

### Test 4 -- Very high income (no cap)
**Input:** Net self-employment income CHF 500,000, age 50.
**Expected output:** AHV/IV/EO = CHF 500,000 x 10.00% = CHF 50,000. No upper cap.

### Test 5 -- Post-reference-age with Freibetrag
**Input:** Net self-employment income CHF 25,000, age 67.
**Expected output:** Freibetrag = CHF 16,800. Contributory income = CHF 8,200. Below minimum threshold of CHF 9,800, so minimum of CHF 514 applies (AHV/EO only, no IV).

### Test 6 -- Concurrent employment + self-employment
**Input:** Employment salary CHF 80,000 (AHV paid by employer), self-employment income CHF 30,000, age 38.
**Expected output:** Self-employment AHV/IV/EO on CHF 30,000 at sliding scale rate (~6.4%) = ~CHF 1,920. Employment AHV handled separately.

### Test 7 -- Pillar 3a without BVG
**Input:** Self-employed, no BVG, net income CHF 120,000, age 42.
**Expected output:** Maximum Pillar 3a = 20% x CHF 120,000 = CHF 24,000, capped at CHF 35,280. Deductible: CHF 24,000.

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
