---
name: ch-federal-income-tax
description: >
  Use this skill whenever asked about Swiss federal income tax (direkte Bundessteuer / impôt fédéral direct) for self-employed individuals. Trigger on phrases like "Bundessteuer", "direkte Bundessteuer", "impôt fédéral direct", "Steuererklärung Schweiz", "selbständig Steuern Schweiz", "Swiss federal income tax", "self-employed tax Switzerland", "AHV deduction", "Säule 3a", "BVG", "Geschäftsaufwand", or any question about computing or filing FEDERAL income tax for a self-employed person in Switzerland. This skill covers FEDERAL progressive brackets only (0--11.5%), Geschäftsaufwand, AHV/IV/EO deductibility, BVG/Säule 3a deductions, and federal filing. Cantonal and municipal taxes are [T3] and out of scope. ALWAYS read this skill before touching any Swiss federal income tax work.
version: 1.0
jurisdiction: CH
tax_year: 2025
category: international
depends_on:
  - income-tax-workflow-base
---

# Switzerland Federal Income Tax (Direkte Bundessteuer) -- Self-Employed Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Switzerland (Federal level only) |
| Jurisdiction Code | CH |
| Primary Legislation | Bundesgesetz über die direkte Bundessteuer (DBG), SR 642.11 |
| Supporting Legislation | Bundesgesetz über die Alters- und Hinterlassenenversicherung (AHVG); Bundesgesetz über die berufliche Vorsorge (BVG); Verordnung über die steuerliche Abzugsberechtigung für Beiträge an Vorsorgeeinrichtungen (BVV 3) |
| Tax Authority | Eidgenössische Steuerverwaltung (ESTV) / Administration fédérale des contributions (AFC) |
| Filing Portal | Cantonal tax portal (varies by canton -- federal tax is filed with cantonal return) |
| Contributor | Open Accountants Community |
| Validated By | Pending -- requires sign-off by a Treuhänder or Steuerberater practising in Switzerland |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: federal rate table application, AHV/IV/EO deductibility, Säule 3a limits, Geschäftsaufwand categories, federal filing. Tier 2: mixed-use expense apportionment, BVG voluntary contributions, home office, business vehicle. Tier 3: cantonal/municipal taxes, international structures, Quellensteuer, interkantonale Steuerausscheidung, Steuererlass. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags and presents options. Treuhänder must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate and document.

---

## Step 0: Client Onboarding Questions

Before computing any federal income tax figure, you MUST know:

1. **Marital status** [T1] -- single (ledig/geschieden/verwitwet) or married (verheiratet). Determines which federal tariff applies (Grundtarif vs Verheiratetentarif).
2. **Canton and municipality of residence** [T1] -- determines cantonal/municipal taxes [T3] and filing portal. Federal tax is the same nationwide.
3. **Income type** [T1] -- Einkünfte aus selbständiger Erwerbstätigkeit (self-employment income, Art. 18 DBG).
4. **Gross self-employment income / turnover** [T1] -- total receipts in the year.
5. **Geschäftsaufwand (business expenses)** [T1/T2] -- nature and amount.
6. **AHV/IV/EO contributions paid** [T1] -- amount paid in the year.
7. **BVG / Säule 3a contributions** [T1] -- amounts contributed.
8. **Capital assets** [T1] -- type, cost, date first used.
9. **Other income** [T1] -- employment, rental, securities, foreign income.
10. **Children / dependants** [T1] -- for Kinderabzug.

**If marital status is unknown, STOP. Do not apply a tariff. Marital status determines which federal rate schedule applies.**

---

## Step 1: Determine Applicable Federal Tax Tariff [T1]

**Legislation:** DBG Art. 214 (Grundtarif -- single), Art. 214 Abs. 2 (Verheiratetentarif -- married)

### Federal Tax -- Grundtarif (Single Persons) -- Simplified Bracket Summary (2025)

| Taxable Income (CHF) | Approximate Marginal Rate | Notes |
|----------------------|---------------------------|-------|
| 0 -- 17,800 | 0% | Tax-free threshold |
| 17,801 -- 31,600 | 0.77% | On excess above CHF 17,800 |
| 31,601 -- 41,400 | 0.88% -- 2.64% | Progressive within band |
| 41,401 -- 55,200 | 2.97% | |
| 55,201 -- 72,500 | 5.94% | |
| 72,501 -- 78,100 | 6.60% | |
| 78,101 -- 103,600 | 8.80% | |
| 103,601 -- 134,600 | 11.00% | |
| 134,601 -- 176,000 | 13.20% | |
| 176,001 -- 755,200 | 11.50% (flat on whole income) | Overall effective rate |
| Above 755,200 | 11.50% | Maximum effective rate |

**IMPORTANT:** The Swiss federal tax uses a unique progressive system where the marginal rates are applied in narrow bands and the statutory schedule is expressed as tax amounts at specific income thresholds, not simple bracket percentages. The rates above are approximations. For exact computation, use the official ESTV Tarif tables or a deterministic engine.

### Verheiratetentarif (Married Persons)

- Separate, more favourable tariff with wider bands.
- Tax-free threshold approximately CHF 30,800.
- Maximum effective rate 11.5% reached at approximately CHF 912,600.
- Married couples are taxed jointly on combined income (Faktorenaddition).

**NEVER compute Swiss federal tax manually from these approximate brackets -- always use the official ESTV tax table or deterministic engine.**

---

## Step 2: Geschäftsaufwand (Business Expenses) [T1/T2]

**Legislation:** DBG Art. 27-31

### Deductible Expenses

| Expense | Tier | Treatment |
|---------|------|-----------|
| Office rent (dedicated Geschäftsräume) | T1 | Fully deductible |
| Professional insurance (Berufshaftpflicht) | T1 | Fully deductible |
| Accountancy / Treuhand fees | T1 | Fully deductible |
| Office supplies / materials | T1 | Fully deductible |
| Software subscriptions | T1 | Fully deductible |
| Marketing / advertising | T1 | Fully deductible |
| Bank charges (business account) | T1 | Fully deductible |
| Professional development (Weiterbildung) | T1 | Fully deductible (up to CHF 12,900 for job-related) |
| Travel (business purpose) | T1 | Fully deductible |
| AHV/IV/EO contributions | T1 | Fully deductible (see Step 4) |
| Telephone / internet | T2 | Business use portion only |
| Motor vehicle (Geschäftsfahrzeug) | T2 | Business use portion only; private use = taxable benefit |
| Home office (Arbeitszimmer) | T2 | Proportional -- dedicated workspace required |
| Business meals / entertainment | T2 | Business-purpose meals deductible; purely private entertainment not deductible |

### NOT Deductible [T1]

| Expense | Reason |
|---------|--------|
| Personal living expenses (Lebenshaltungskosten) | Art. 34 DBG -- not business-related |
| Fines and penalties (Bussen) | Public policy |
| Federal/cantonal/municipal income tax itself | Tax on income |
| Capital expenditure | Goes through Abschreibungen (depreciation) |
| Private portion of mixed-use expenses | Must be separated out |

---

## Step 3: Abschreibungen (Depreciation) [T1]

**Legislation:** DBG Art. 28; Merkblatt ESTV

### Standard Depreciation Rates (Straight-Line or Reducing Balance)

| Asset Type | Straight-Line Rate | Reducing Balance Rate |
|-----------|--------------------|-----------------------|
| Computer hardware / software | 40% | 50% |
| Office furniture | 12.5% | 25% |
| Motor vehicles | 20% | 40% |
| Machines / equipment | 12.5%--20% | 25%--40% |
| Commercial buildings | 2%--4% | 3%--7% |

### Rules [T1]

- The taxpayer may choose straight-line (linear) or reducing balance (degressiv) depreciation, but must be consistent for the asset.
- Depreciation starts in the year of acquisition.
- Swiss practice permits flexible depreciation rates within reason; the rates above are ESTV guidelines. The cantonal tax office may challenge excessive rates.
- Geringfügige Anschaffungen (low-value assets): assets under approximately CHF 1,000 may be expensed immediately.

---

## Step 4: AHV/IV/EO Deductibility [T1]

**Legislation:** AHVG; DBG Art. 33 Abs. 1 lit. d and f

### Self-Employed AHV/IV/EO Contributions

| Component | Rate (2025) |
|-----------|-------------|
| AHV (old age / survivors) | 8.1% |
| IV (disability) | 1.4% |
| EO (income compensation) | 0.5% |
| Total AHV/IV/EO | 10.0% |

**Note:** Self-employed individuals pay the full contribution (no employer share). The rate is 10.0% on income above CHF 10,100, with a declining scale for income between CHF 10,100 and CHF 58,800.

### Rules [T1]

- AHV/IV/EO contributions are FULLY deductible from taxable income.
- Contributions are calculated on net self-employment income (income minus business expenses).
- The contribution is itself deductible, creating a circular calculation. In practice, the AHV fund (Ausgleichskasse) determines the contribution based on the tax assessment.

---

## Step 5: BVG and Säule 3a Deductions [T1]

**Legislation:** BVG; BVV 3; DBG Art. 33 Abs. 1 lit. e

### Säule 3a (Pillar 3a) Maximum Contributions (2025)

| Category | Maximum (CHF) |
|----------|--------------|
| Self-employed WITH BVG (Pensionskasse) | 7,258 |
| Self-employed WITHOUT BVG | 20% of net earned income, max 36,288 |

### BVG (Pillar 2 -- Occupational Pension)

- Self-employed individuals may voluntarily join a BVG scheme (Pensionskasse) or the Stiftung Auffangeinrichtung BVG.
- Contributions are fully deductible.
- If no BVG coverage, the higher Säule 3a limit of CHF 36,288 applies.
- [T2] Flag for reviewer to confirm BVG status and applicable Säule 3a limit.

### Rules [T1]

- Säule 3a contributions are deducted from taxable income.
- The maximum is a hard cap -- contributions above the limit are NOT deductible.
- Net earned income = gross self-employment income minus business expenses minus AHV/IV/EO contributions.

---

## Step 6: Other Deductions [T1/T2]

**Legislation:** DBG Art. 33, 33a, 35

### Personal Deductions (Federal)

| Deduction | Amount (CHF) | Notes |
|-----------|-------------|-------|
| Married couple deduction | 2,800 | Dual-income married couples |
| Kinderabzug (child deduction) | 6,700 per child | Under 18 or in education |
| Unterstützungsabzug (support deduction) | Up to 7,050 | For supporting persons unable to work |
| Insurance premiums / Säule 3a | See Step 5 | |
| Disability-related costs | Actual costs | [T2] documentation required |

### Separate Taxation of Spouses

- Since 2024, Switzerland continues to use joint taxation for married couples (Faktorenaddition with the Verheiratetentarif).
- A reform introducing individual taxation has been discussed but is not yet in force for 2025.

---

## Step 7: Computation Walkthrough [T1]

### Step-by-Step (Federal Tax Only)

1. **Gross self-employment income** (Einkünfte aus selbständiger Erwerbstätigkeit).
2. **Less: Geschäftsaufwand** (business expenses, including depreciation).
3. **Net self-employment income**.
4. **Less: AHV/IV/EO contributions** (fully deductible).
5. **Less: BVG contributions** (if applicable).
6. **Less: Säule 3a contributions** (within maximum).
7. **Add other income** (employment, rental, securities, foreign).
8. **Total income**.
9. **Less: Personal deductions** (Kinderabzug, insurance, etc.).
10. **Taxable income (steuerbares Einkommen)**.
11. **Apply federal tariff** (Grundtarif or Verheiratetentarif).
12. **Federal tax payable (direkte Bundessteuer)**.

**Cantonal and municipal taxes are separate computations with different rates and deductions [T3]. This skill covers federal tax only.**

---

## Step 8: Filing Deadlines [T1]

**Legislation:** DBG Art. 124; cantonal procedural law

| Filing / Payment | Deadline |
|-----------------|----------|
| Steuererklärung (standard) | 31 March of the following year (varies by canton) |
| Extension (Fristerstreckung) | Typically available on request; varies by canton (often to 30 Sep or 30 Nov) |
| Filing with Treuhänder | Extensions commonly granted to end of September or later |
| Provisional tax bills (Bundessteuer) | Issued by canton -- typically due within 30 days of notice |

### Important Notes

- The federal tax return is filed TOGETHER with the cantonal return through the cantonal tax authority.
- Deadlines are set by each canton. 31 March is the statutory default in many cantons, but extensions are routinely available.
- Some cantons (e.g., Zürich) use 31 March; others (e.g., Bern) may differ.

### Late Filing [T1]

| Offence | Consequence |
|---------|-------------|
| Late filing (Mahnung) | Reminder with fee (typically CHF 30--80); potential estimated assessment (Ermessenseinschätzung) |
| Persistent non-filing | Estimated assessment + Busse (fine) up to CHF 1,000 |
| Tax evasion (Steuerhinterziehung) | Fine of 33.3% to 300% of evaded tax (DBG Art. 175) |
| Tax fraud (Steuerbetrug) | Criminal prosecution; imprisonment possible |

---

## Step 9: Provisional Tax Payments [T1]

**Legislation:** DBG Art. 161-163; cantonal procedural law

### Rules

- Provisional federal tax is billed by the canton based on the prior year's assessment or estimated current year income.
- Paid in instalments as invoiced by the canton (schedules vary).
- Interest is charged on underpayment and credited on overpayment (Ausgleichszins).
- No federal penalty for insufficient provisional payments, but interest applies.

---

## Step 10: Edge Case Registry

### EC1 -- Säule 3a without BVG [T1]
**Situation:** Self-employed client without BVG contributes CHF 7,258 to Säule 3a.
**Resolution:** INCORRECT. Without BVG, the limit is 20% of net earned income up to CHF 36,288. The client is under-contributing. Advise that up to CHF 36,288 is deductible (subject to the 20% income cap).

### EC2 -- Säule 3a with BVG, over limit [T1]
**Situation:** Client with BVG contributes CHF 10,000 to Säule 3a.
**Resolution:** Maximum with BVG = CHF 7,258. Excess CHF 2,742 is NOT deductible and should not be contributed (or will not receive tax benefit).

### EC3 -- Cantonal tax question [T3]
**Situation:** Client asks "how much total tax do I pay in Zurich?"
**Resolution:** ESCALATE. This skill covers FEDERAL tax only. Cantonal and municipal taxes require a separate cantonal skill or consultation with a local Treuhänder. Do not estimate cantonal rates.

### EC4 -- Private use of business vehicle [T2]
**Situation:** Client uses a business vehicle 30% for private purposes.
**Resolution:** 30% of vehicle costs are NOT deductible as Geschäftsaufwand. Alternatively, private use must be added back as income (Naturallohn). [T2] Flag for reviewer to determine the appropriate method (expense reduction vs income addition).

### EC5 -- AHV declining scale [T1]
**Situation:** Client has net self-employment income of CHF 30,000.
**Resolution:** AHV/IV/EO contributions follow a declining scale for income between CHF 10,100 and CHF 58,800. The rate is less than 10.0% at this income level. Use the official AHV contribution table or Ausgleichskasse notice.

### EC6 -- Joint taxation, one spouse self-employed [T1]
**Situation:** Married couple: spouse A is self-employed (CHF 80,000), spouse B is employed (CHF 50,000).
**Resolution:** Both incomes are combined (Faktorenaddition) and taxed jointly using the Verheiratetentarif. Business deductions apply only to spouse A's self-employment income. Both spouses can claim individual Säule 3a deductions.

### EC7 -- Home office deduction [T2]
**Situation:** Client works exclusively from home and wants to deduct a portion of rent.
**Resolution:** Deductible if the workspace is used predominantly for business AND the client does not have a separate business premises. Proportion based on floor area of dedicated workspace vs total living area. [T2] Flag for reviewer to confirm eligibility and proportion.

### EC8 -- Low-value asset immediate expensing [T1]
**Situation:** Client buys office equipment for CHF 800.
**Resolution:** Asset is below approximately CHF 1,000. May be expensed immediately in the year of purchase. No multi-year depreciation required.

### EC9 -- Federal tax only, client expects total [T1]
**Situation:** Client receives federal tax computation and says "this seems too low."
**Resolution:** Federal tax represents approximately 20--35% of total income tax burden. Cantonal and municipal taxes (which are [T3] in this skill) typically account for the majority. Clarify that this computation is FEDERAL ONLY.

### EC10 -- Separate taxation reform [T1]
**Situation:** Married client asks about individual taxation.
**Resolution:** As of 2025, married couples are still taxed jointly with the Verheiratetentarif. A reform to introduce individual taxation has been approved in principle but is not yet in force. Apply current joint taxation rules.

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
Action Required: Treuhänder must confirm before filing.
```

When Claude identifies a [T3] situation:

```
ESCALATION REQUIRED
Tier: T3
Client: [name]
Situation: [description]
Issue: [outside skill scope -- likely cantonal/municipal tax or international structure]
Action Required: Do not advise. Refer to Treuhänder. Document gap.
```

---

## Step 12: Test Suite

### Test 1 -- Single self-employed, federal tax only
**Input:** Single, net self-employment income CHF 100,000 after business expenses, AHV/IV/EO paid CHF 10,000, Säule 3a CHF 7,258 (has BVG), no other income, no children.
**Expected output:** Taxable income = CHF 100,000 - CHF 10,000 - CHF 7,258 = CHF 82,742. Apply Grundtarif. Federal tax approximately CHF 3,500--4,000 (use official table for exact amount). Note: this is federal tax only.

### Test 2 -- Married, joint taxation
**Input:** Married, spouse A self-employed CHF 120,000 net, spouse B employed CHF 60,000, AHV/IV/EO CHF 12,000 (spouse A), Säule 3a CHF 7,258 each, 2 children.
**Expected output:** Combined income = CHF 180,000. Less deductions: AHV CHF 12,000, Säule 3a CHF 14,516, Kinderabzug CHF 13,400 = CHF 39,916. Taxable income = CHF 140,084. Apply Verheiratetentarif. Federal tax lower than Grundtarif equivalent.

### Test 3 -- Säule 3a without BVG, maximum contribution
**Input:** Self-employed without BVG, net earned income CHF 200,000 after AHV.
**Expected output:** Säule 3a max = 20% x CHF 200,000 = CHF 40,000, but capped at CHF 36,288. Deductible amount = CHF 36,288.

### Test 4 -- Säule 3a without BVG, income cap applies
**Input:** Self-employed without BVG, net earned income CHF 30,000 after AHV.
**Expected output:** Säule 3a max = 20% x CHF 30,000 = CHF 6,000 (below CHF 36,288 cap). Deductible amount = CHF 6,000.

### Test 5 -- Low-value asset immediate expensing
**Input:** Client buys CHF 900 printer for business.
**Expected output:** Expense immediately as Geschäftsaufwand. No depreciation schedule required.

### Test 6 -- Cantonal question escalated
**Input:** Client asks "what is my tax in Basel?"
**Expected output:** ESCALATION REQUIRED. This skill covers federal tax only. Cantonal/municipal rates for Basel-Stadt are [T3]. Refer to Treuhänder.

---

## PROHIBITIONS

- NEVER compute Swiss federal tax manually from approximate bracket tables -- always use the official ESTV tariff tables or a deterministic engine
- NEVER apply the Grundtarif to a married client or the Verheiratetentarif to a single client
- NEVER estimate cantonal or municipal taxes -- this skill covers FEDERAL tax only; cantonal/municipal is [T3]
- NEVER allow Säule 3a contributions above the applicable maximum (CHF 7,258 with BVG / CHF 36,288 without BVG or 20% of net earned income)
- NEVER allow income tax itself as a deduction
- NEVER allow fines or penalties (Bussen) as a deduction
- NEVER allow capital expenditure directly as a Geschäftsaufwand -- it must go through Abschreibungen
- NEVER present federal tax as the total tax burden -- always clarify that cantonal and municipal taxes are additional and typically larger
- NEVER present tax calculations as definitive -- always label as estimated and direct client to their Treuhänder for confirmation
- NEVER advise on cantonal tax disputes, Steuererlass, or international structures without escalating

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
