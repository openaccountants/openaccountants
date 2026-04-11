---
name: hu-income-tax
description: >
  Use this skill whenever asked about Hungarian income tax for self-employed individuals (egyéni vállalkozó). Trigger on phrases like "how much tax do I pay", "SZJA", "personal income tax Hungary", "KATA", "átalányadózás", "flat-rate taxation", "egyéni vállalkozó", "self-employed tax Hungary", "SZOCHO", "TB járulék", or any question about filing or computing income tax for a self-employed or freelance client in Hungary. This skill covers the flat 15% SZJA, KATA simplified tax, átalányadózás (flat-rate taxation), vállalkozói jövedelemadó, social contribution tax (SZOCHO 13%), social insurance (TB 18.5%), filing deadlines, and penalties. ALWAYS read this skill before touching any Hungarian income tax work.
version: 1.0
jurisdiction: HU
tax_year: 2025
category: international
depends_on:
  - income-tax-workflow-base
---

# Hungary Income Tax (SZJA) -- Self-Employed Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Hungary |
| Jurisdiction Code | HU |
| Primary Legislation | 1995. évi CXVII. törvény a személyi jövedelemadóról (SZJA Act) |
| Supporting Legislation | 2022. évi XIII. törvény (KATA); 2019. évi CXXII. törvény (SZOCHO); 2019. évi CXXII. törvény (TB) |
| Tax Authority | Nemzeti Adó- és Vámhivatal (NAV -- National Tax and Customs Administration) |
| Filing Portal | NAV Online / eSZJA |
| Contributor | Open Accountants Community |
| Validated By | Pending -- requires Hungarian adótanácsadó sign-off |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: SZJA rate, KATA eligibility, SZOCHO/TB rates, átalányadó cost ratios, filing deadlines. Tier 2: choosing between taxation regimes, mixed-activity cost ratios, employee vs contractor boundary. Tier 3: international income, tax treaties, group structures, crypto. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags and presents options. Qualified adótanácsadó must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate and document.

---

## Step 0: Client Onboarding Questions

Before computing any income tax figure, you MUST know:

1. **Self-employment type** [T1] -- egyéni vállalkozó (sole proprietor) or egyéni cég (individual company) or freelancer under megbízási szerződés.
2. **Chosen tax regime** [T1] -- standard vállalkozói jövedelemadó, átalányadózás (flat-rate), or KATA.
3. **Gross revenue** [T1] -- total invoiced/received in the year.
4. **Nature of clients** [T1] -- individuals only (required for KATA) or businesses.
5. **Number of employees** [T1] -- KATA requires no employees.
6. **Other income** [T1] -- employment, rental, dividends, interest.
7. **Business expenses** [T1/T2] -- if using standard regime with itemised costs.
8. **ÖVTJ activity code(s)** [T1] -- determines átalányadó cost ratio.

**If tax regime is unknown, STOP. You must determine the regime before computing.**

---

## Step 1: Determine Tax Regime [T1/T2]

**Legislation:** SZJA tv., KATA tv.

Hungary offers three main regimes for self-employed individuals:

### Option A: KATA (Kisadózó vállalkozások tételes adója) [T1]

**Legislation:** 2022. évi XIII. törvény

| Condition | Requirement |
|-----------|-------------|
| Entity type | Egyéni vállalkozó only |
| Client base | Individual customers ONLY -- invoicing to any legal entity (company) disqualifies immediately (except taxi drivers) |
| Employment | Must be main occupation (cannot work >36 hours/week elsewhere) |
| Employees | None permitted |
| Revenue limit (VAT) | HUF 12,000,000 -- above this, must register for VAT |

**KATA Tax:** HUF 50,000/month (full-rate, main occupation) or HUF 25,000/month (auxiliary, if employed elsewhere under 36 hours).

**KATA covers:** income tax + social contributions. No separate SZJA, SZOCHO, or TB payments.

**KATA does NOT cover:** VAT (if registered), local business tax (iparűzési adó).

**Critical restriction (post-2022 reform):** KATA is exclusively for B2C (business-to-consumer) activities. Receiving ANY revenue from a legal entity (even HUF 1) results in immediate loss of KATA status for the entire year. This was the major 2022 reform that eliminated KATA for most IT freelancers and consultants.

### Option B: Átalányadózás (Flat-Rate Taxation) [T1]

**Legislation:** SZJA tv. § 50-56

| Condition | Requirement |
|-----------|-------------|
| Revenue limit | HUF 36,000,000 for listed retail activities; HUF 24,000,000 for all others |
| Employees | Maximum 1 |
| Activity | Must be registered ÖVTJ activity |

**Cost Ratios (applied to gross revenue to determine deemed expenses):**

| Activity Type | Cost Ratio | Max Revenue for Ratio |
|--------------|-----------|----------------------|
| Retail trade (non-food service) | 90% | 50x annual minimum wage |
| Listed activities (hairdressing, repair, taxi, etc.) by ÖVTJ code | 80% | No separate cap |
| All other activities | 40% | Standard cap applies |

**Taxable income = Gross revenue x (1 - cost ratio).** Then taxed at 15% SZJA.

**Example:** IT consultant, revenue HUF 20,000,000, cost ratio 40%. Taxable income = HUF 12,000,000. SZJA = HUF 1,800,000.

### Option C: Standard Regime (Vállalkozói jövedelemadó) [T1]

**Legislation:** SZJA tv. § 44-49

Two-layer taxation:

| Layer | Rate | Base |
|-------|------|------|
| Vállalkozói jövedelemadó | 9% | Net profit (revenue minus documented costs) |
| Vállalkozói osztalékalap utáni adó (dividend-equivalent SZJA) | 15% | Withdrawn profit (amount taken for personal use) |

**The 9% rate applies to the entrepreneurial profit.** When the entrepreneur withdraws profit for personal use, an additional 15% SZJA applies on the withdrawn amount (treated as dividend-equivalent).

**Cost deduction:** Actual documented expenses OR the 10% deemed cost ratio (not both).

---

## Step 2: SZJA Rate [T1]

**Legislation:** SZJA tv. § 8

| Income Type | Rate |
|-------------|------|
| All personal income (general) | 15% flat |
| Vállalkozói jövedelemadó (entrepreneurial profit) | 9% |
| Dividend-equivalent withdrawal | 15% |

**Hungary uses a flat 15% SZJA rate. There are no progressive bands.**

---

## Step 3: Social Contributions [T1]

**Legislation:** 2019. évi CXXII. törvény (SZOCHO); Tbj. (TB)

### Rates

| Contribution | Rate | Paid By | Base |
|-------------|------|---------|------|
| Szociális hozzájárulási adó (SZOCHO) | 13% | Self-employed (as deemed employer) | Declared income or minimum base |
| Társadalombiztosítási járulék (TB) | 18.5% | Self-employed | Declared income or minimum base |

### TB Components (18.5% total)

| Component | Rate |
|-----------|------|
| Pension (nyugdíjjárulék) | 10% |
| Health insurance (egészségbiztosítási járulék) | 4% |
| Labour market (munkaerőpiaci járulék) | 3% |
| Work accident | 1.5% |

### Minimum Contribution Base (2025) [T1]

| Category | Monthly Base (HUF) |
|----------|-------------------|
| Minimum wage (no qualification required) | 290,800 |
| Guaranteed minimum wage (qualification required) | 348,800 |

**Self-employed persons must pay SZOCHO and TB on at least the minimum wage (or guaranteed minimum wage if the activity requires qualifications), regardless of actual income.**

### Átalányadó Contribution Rules

For flat-rate taxpayers, the SZOCHO and TB base is the declared átalányadó income (i.e., revenue x (1 - cost ratio)), subject to the minimum base.

### KATA Contribution Rules

KATA covers social contributions -- no separate SZOCHO or TB payment required.

---

## Step 4: Local Business Tax (Iparűzési adó -- IPA) [T1/T2]

**Legislation:** 1990. évi C. törvény (local taxes)

| Item | Detail |
|------|--------|
| Rate | Up to 2% (set by municipality) |
| Base | Net revenue (gross revenue minus cost of goods sold and subcontractor costs) |
| Filing | Annual, by 31 May |

- IPA applies to ALL self-employed, including KATA and átalányadó taxpayers
- KATA taxpayers: IPA base = actual revenue (no special KATA exemption)
- IPA is deductible from the SZJA tax base for standard-regime taxpayers

---

## Step 5: Filing Deadlines [T1]

**Legislation:** Art. tv.; SZJA tv.

| Filing / Payment | Deadline |
|-----------------|----------|
| SZJA annual return (Form 2353) | 20 May of following year |
| KATA monthly payment | 12th of each month |
| SZOCHO/TB monthly advance | 12th of each month |
| Local business tax (IPA) advance | 15 March and 15 September |
| IPA annual return | 31 May |
| VAT return (if applicable) | Monthly or quarterly depending on threshold |

---

## Step 6: Penalties [T1]

**Legislation:** Art. tv.

| Offence | Penalty |
|---------|---------|
| Late filing | Up to HUF 500,000 for individuals |
| Late payment | Late payment interest at central bank base rate + 5% |
| Tax shortfall (self-correction) | 50% of the shortfall amount |
| Tax shortfall (NAV audit) | 50% of shortfall, or 200% if concealment |
| KATA disqualification (invoicing to company) | Retroactive loss of KATA for full year; all income re-taxed under standard regime |

---

## Step 7: Edge Case Registry

### EC1 -- KATA freelancer receives invoice from a company [T1]
**Situation:** KATA taxpayer IT freelancer invoices a Kft. (LLC) for consulting work.
**Resolution:** Immediate disqualification from KATA. ALL income for the year must be re-taxed under standard vállalkozói jövedelemadó or átalányadó. The taxpayer must file a full SZJA return and pay SZOCHO/TB for the entire year. This is the #1 KATA trap since the 2022 reform.

### EC2 -- Átalányadó revenue exceeds limit [T1]
**Situation:** Flat-rate taxpayer's revenue reaches HUF 25,000,000 (over the HUF 24,000,000 limit).
**Resolution:** Átalányadó status is lost for the following year. The taxpayer must switch to standard regime from 1 January of the next year. Income for the current year remains under átalányadó.

### EC3 -- Choosing between átalányadó and standard regime [T2]
**Situation:** IT consultant earns HUF 20,000,000 with real expenses of HUF 10,000,000.
**Resolution:** Under átalányadó (40% cost ratio): taxable = HUF 12,000,000. SZJA = HUF 1,800,000. Under standard: profit = HUF 10,000,000. Vállalkozói adó (9%) = HUF 900,000 + SZJA on withdrawal (15%) = HUF 1,500,000. Total standard = HUF 2,400,000. Átalányadó is cheaper. But SZOCHO/TB bases differ -- [T2] flag for full comparison including social contributions.

### EC4 -- SZOCHO/TB on minimum wage when income is low [T1]
**Situation:** Self-employed person earns HUF 100,000/month but must pay contributions on at least HUF 290,800.
**Resolution:** SZOCHO = 13% x 290,800 = HUF 37,804/month. TB = 18.5% x 290,800 = HUF 53,798/month. Total = HUF 91,602/month even though income is only HUF 100,000. This is a common trap for low-earning self-employed.

### EC5 -- Dual activity KATA + employment [T2]
**Situation:** Person works 30 hours/week as employee and wants KATA for side business.
**Resolution:** Eligible for auxiliary KATA (HUF 25,000/month) since employed <36 hours/week. But KATA income must still be B2C only. [T2] Verify employment hours and that all KATA clients are individuals.

### EC6 -- IPA deductibility under standard regime [T1]
**Situation:** Self-employed pays HUF 200,000 IPA and wants to deduct it.
**Resolution:** IPA is deductible from the entrepreneurial income under the standard regime. It reduces the vállalkozói jövedelemadó base. It is NOT deductible under KATA or átalányadó (where costs are deemed, not actual).

### EC7 -- VAT registration threshold interaction with KATA [T1]
**Situation:** KATA taxpayer's revenue approaches HUF 12,000,000.
**Resolution:** At HUF 12,000,000, VAT registration becomes mandatory. KATA status is NOT lost by VAT registration alone, but the taxpayer must charge and remit VAT separately. The HUF 50,000/month KATA payment does not cover VAT.

### EC8 -- Year-end regime switch timing [T2]
**Situation:** Freelancer wants to switch from standard regime to átalányadó.
**Resolution:** Must notify NAV by 31 December of the prior year (or at registration). Cannot switch mid-year. [T2] Verify eligibility conditions are met and that the switch is beneficial after comparing total tax + contribution burden.

---

## Step 8: Reviewer Escalation Protocol

When Claude identifies a [T2] situation:

```
REVIEWER FLAG
Tier: T2
Client: [name]
Situation: [description]
Issue: [what is ambiguous]
Options: [possible treatments]
Recommended: [most likely correct treatment and why]
Action Required: Qualified adótanácsadó must confirm before filing.
```

When Claude identifies a [T3] situation:

```
ESCALATION REQUIRED
Tier: T3
Client: [name]
Situation: [description]
Issue: [outside skill scope]
Action Required: Do not advise. Refer to adótanácsadó. Document gap.
```

---

## Step 9: Test Suite

### Test 1 -- Átalányadó IT consultant, standard cost ratio
**Input:** IT consultant (40% cost ratio), revenue HUF 18,000,000, single, no children.
**Expected output:** Deemed costs = 40% x HUF 18,000,000 = HUF 7,200,000. Taxable income = HUF 10,800,000. SZJA = 15% x HUF 10,800,000 = HUF 1,620,000. SZOCHO = 13% x HUF 10,800,000 = HUF 1,404,000. TB = 18.5% x HUF 10,800,000 = HUF 1,998,000.

### Test 2 -- KATA hairdresser, compliant B2C
**Input:** Hairdresser, all individual clients, main occupation, revenue HUF 8,000,000.
**Expected output:** KATA applies. Monthly tax = HUF 50,000. Annual = HUF 600,000. No SZJA return required. No SZOCHO/TB separately. IPA still due (municipality rate x revenue).

### Test 3 -- KATA disqualification mid-year
**Input:** Freelance photographer on KATA invoices HUF 500,000 to a Kft. in March. Total annual revenue HUF 6,000,000.
**Expected output:** KATA lost for entire year. Must file standard SZJA. Under átalányadó (if eligible, 80% code): taxable = HUF 1,200,000. SZJA = HUF 180,000. Plus SZOCHO + TB on at least minimum wage for 12 months.

### Test 4 -- Standard regime, two-layer tax
**Input:** Consultant, standard regime, revenue HUF 30,000,000, documented expenses HUF 12,000,000, withdraws HUF 10,000,000 for personal use.
**Expected output:** Profit = HUF 18,000,000. Vállalkozói jövedelemadó = 9% x HUF 18,000,000 = HUF 1,620,000. Dividend-equivalent SZJA on withdrawal = 15% x HUF 10,000,000 = HUF 1,500,000. SZOCHO on withdrawal = 13% x HUF 10,000,000 = HUF 1,300,000. TB = 18.5% x HUF 10,000,000 = HUF 1,850,000.

### Test 5 -- Minimum contribution base trap
**Input:** Part-time self-employed, revenue HUF 1,500,000/year, no employees, no qualification required.
**Expected output:** Monthly income = HUF 125,000. But minimum base = HUF 290,800. Monthly SZOCHO = HUF 37,804. Monthly TB = HUF 53,798. Annual contributions = HUF 1,099,224. This exceeds 73% of gross revenue -- flag as potentially unviable.

### Test 6 -- Átalányadó with 80% listed activity
**Input:** Taxi driver, ÖVTJ listed activity (80% cost ratio), revenue HUF 15,000,000.
**Expected output:** Deemed costs = 80% x HUF 15,000,000 = HUF 12,000,000. Taxable = HUF 3,000,000. SZJA = HUF 450,000. SZOCHO = 13% x HUF 3,000,000 = HUF 390,000. TB = 18.5% x HUF 3,000,000 = HUF 555,000.

---

## PROHIBITIONS

- NEVER allow KATA for a taxpayer who invoices legal entities (companies) -- this is the #1 error since the 2022 reform
- NEVER apply progressive tax rates -- Hungary uses a flat 15% SZJA (or 9% vállalkozói jövedelemadó)
- NEVER ignore the minimum contribution base -- SZOCHO and TB must be paid on at least the minimum wage even if income is lower
- NEVER combine KATA with separate SZOCHO/TB payments -- KATA covers social contributions
- NEVER allow a regime switch mid-year -- regime changes take effect from 1 January
- NEVER forget IPA -- it applies to ALL self-employed including KATA and átalányadó
- NEVER deduct actual expenses under átalányadó -- the cost ratio IS the expense deduction
- NEVER advise on international structures, tax treaties, or crypto -- escalate to T3
- NEVER present tax calculations as definitive -- always label as estimated and direct client to their adótanácsadó for confirmation
- NEVER confuse the 9% vállalkozói jövedelemadó with the 15% SZJA -- they are separate layers in the standard regime

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as an adótanácsadó or equivalent licensed practitioner in Hungary) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
