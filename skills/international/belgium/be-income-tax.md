---
name: be-income-tax
description: >
  Use this skill whenever asked about Belgian income tax (Personenbelasting / Impôt des personnes physiques) for self-employed individuals. Trigger on phrases like "personenbelasting", "IPP", "belastingaangifte", "belastingvrij minimum", "gemeentebelasting", "beroepskosten", "sociale bijdragen", "VAPZ", "PLCI", "Belgian income tax", "self-employed tax Belgium", "Tax-on-web", or any question about computing or filing income tax for a self-employed person in Belgium. This skill covers progressive brackets (25--50%), belastingvrij minimum, gemeentebelasting, beroepskosten (actual vs forfaitaire), sociale bijdragen deductibility, VAPZ/PLCI pension deduction, and Tax-on-web filing. ALWAYS read this skill before touching any Belgian income tax work.
version: 1.0
jurisdiction: BE
tax_year: 2025
category: international
depends_on:
  - income-tax-workflow-base
---

# Belgium Income Tax (PB/IPP) -- Self-Employed Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Belgium |
| Jurisdiction Code | BE |
| Primary Legislation | Wetboek van de inkomstenbelastingen 1992 (WIB 92) / Code des impôts sur les revenus 1992 (CIR 92) |
| Supporting Legislation | Koninklijk Besluit tot uitvoering van het WIB 92 (KB/WIB 92); Sociaal statuut der zelfstandigen (Royal Decree No. 38) |
| Tax Authority | FOD Financiën / SPF Finances |
| Filing Portal | Tax-on-web (MyMinfin) |
| Contributor | Open Accountants Community |
| Validated By | Pending -- requires sign-off by a Erkend boekhouder-fiscalist or Bedrijfsrevisor practising in Belgium |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: rate table application, belastingvrij minimum, gemeentebelasting computation, sociale bijdragen deductibility, VAPZ limits, filing deadlines. Tier 2: beroepskosten apportionment (actual vs forfait), mixed-use expenses, aftrekbare bestedingen, VAPZ optimisation. Tier 3: international structures, vennootschapsbelasting interaction, non-resident taxation, fiscale procedures. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags and presents options. Erkend boekhouder-fiscalist must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate and document.

---

## Step 0: Client Onboarding Questions

Before computing any income tax figure, you MUST know:

1. **Marital / family status** [T1] -- single (alleenstaand), married/legal cohabitant (gehuwd/wettelijk samenwonend), dependants (personen ten laste). Determines belastingvrij minimum.
2. **Municipality of residence** [T1] -- determines gemeentebelasting rate (opcentiemen).
3. **Income type** [T1] -- beroepsinkomsten (professional income) from self-employment.
4. **Gross self-employment income / turnover** [T1] -- total receipts in the year.
5. **Business expenses method** [T1/T2] -- werkelijke beroepskosten (actual) or forfaitaire beroepskosten (flat-rate).
6. **Sociale bijdragen paid** [T1] -- social contributions paid in the year.
7. **VAPZ/PLCI contributions** [T2] -- supplementary pension contributions.
8. **Other income** [T1] -- employment, rental, investment, foreign income.
9. **Capital assets acquired** [T1] -- type, cost, date first used.

**If municipality of residence is unknown, STOP. The gemeentebelasting rate cannot be determined without it.**

---

## Step 1: Determine Applicable Tax Brackets [T1]

**Legislation:** WIB 92, Art. 130 et seq. (income year 2025, assessment year 2026)

### Progressive Income Tax Rates (Income Year 2025 / Assessment Year 2026)

| Taxable Income (EUR) | Marginal Rate |
|---------------------|---------------|
| 0 -- 16,720 | 25% |
| 16,721 -- 29,510 | 40% |
| 29,511 -- 51,070 | 45% |
| Above 51,070 | 50% |

**Note:** These brackets apply to the FEDERAL component of income tax. The gemeentebelasting is levied as a surcharge on top.

---

## Step 2: Belastingvrij Minimum (Tax-Free Allowance) [T1]

**Legislation:** WIB 92, Art. 131-145

### Base Amount (Income Year 2025)

| Category | Amount (EUR) |
|----------|-------------|
| Base belastingvrij minimum | 10,910 |
| Supplement for 1 dependant child | 1,850 |
| Supplement for 2 dependant children | 4,760 |
| Supplement for 3 dependant children | 10,660 |
| Supplement for 4+ dependant children | +6,180 per additional child |
| Supplement for disabled dependant | 1,850 per person |

### How It Works [T1]

- The belastingvrij minimum is NOT deducted from income. Instead, it is converted to a tax reduction at the rate of 25% (the lowest bracket rate).
- Tax reduction = EUR 10,910 x 25% = EUR 2,727.50 (base, single, no dependants).
- This reduction is applied AFTER computing the gross federal tax.
- For married couples / legal cohabitants, each partner has their own belastingvrij minimum.

---

## Step 3: Gemeentebelasting (Municipal Surcharge) [T1]

**Legislation:** WIB 92, Art. 466-470

### Rules

- Each of Belgium's 581 municipalities sets its own rate (opcentiemen / centimes additionnels).
- Rates range from 0% to 9% of the federal income tax (Rijksbelasting / impôt d'État).
- Average rate is approximately 7%.
- The gemeentebelasting is calculated on the federal tax AFTER applying the belastingvrij minimum reduction and other credits.

### Formula [T1]

```
Gemeentebelasting = Federal tax payable x Municipal rate (%)
Total tax = Federal tax payable + Gemeentebelasting
```

**NEVER estimate the gemeentebelasting without knowing the municipality. Use the actual published rate.**

---

## Step 4: Beroepskosten (Professional Expenses) [T1/T2]

**Legislation:** WIB 92, Art. 49-66

### Option A: Werkelijke Beroepskosten (Actual Expenses) [T1/T2]

The taxpayer may deduct all actual business expenses that meet the test: incurred to acquire or maintain professional income, proven by documentation, and incurred during the tax year.

| Expense | Tier | Treatment |
|---------|------|-----------|
| Office rent (dedicated) | T1 | Fully deductible |
| Professional insurance | T1 | Fully deductible |
| Accountancy fees | T1 | Fully deductible |
| Office supplies / materials | T1 | Fully deductible |
| Software subscriptions | T1 | Fully deductible |
| Marketing / advertising | T1 | Fully deductible |
| Bank charges (business account) | T1 | Fully deductible |
| Professional development | T1 | Fully deductible |
| Travel (business purpose) | T1 | Fully deductible |
| Sociale bijdragen | T1 | Fully deductible (see Step 5) |
| Phone / internet | T2 | Business use portion only |
| Motor vehicle running costs | T2 | Business use portion; fuel 75% max deductible; other costs per CO2 deductibility rules |
| Home office | T2 | Proportional -- dedicated workspace required |
| Restaurant meals (business purpose) | T1 | 69% deductible |
| Representation / gifts | T2 | 50% deductible for business gifts; conditions apply |

### Option B: Forfaitaire Beroepskosten (Flat-Rate Expenses) [T1]

If the taxpayer does not claim actual expenses, a flat-rate deduction applies:

| Income Bracket (EUR) | Forfaitaire Rate |
|---------------------|-----------------|
| 0 -- 19,620 | 30% |
| 19,621 -- 38,900 | 11% |
| 38,901 -- 64,770 | 3% |
| Above 64,770 | 0% |

Maximum forfaitaire deduction: approximately EUR 5,750 (indexed for 2025).

### NOT Deductible [T1]

| Expense | Reason |
|---------|--------|
| Personal living expenses | Not business-related |
| Fines and penalties (boetes) | Public policy |
| Income tax itself (personenbelasting) | Tax on income |
| Capital expenditure | Goes through afschrijvingen (depreciation) |
| Clothing (unless specific professional uniform) | Personal |

---

## Step 5: Sociale Bijdragen (Social Contributions) Deductibility [T1]

**Legislation:** Royal Decree No. 38; WIB 92

### Rules

- Self-employed individuals pay quarterly social contributions to a social insurance fund (sociaal verzekeringsfonds).
- Contributions are calculated on net professional income from 3 years prior (with provisional amounts in the first 3 years).
- Rate: approximately 20.5% on income up to EUR 73,632, then 14.16% on income between EUR 73,632 and EUR 108,565, then 0% above (2025 approximate thresholds -- verify with social fund).
- ALL sociale bijdragen paid are FULLY deductible as professional expenses.
- They reduce net professional income BEFORE applying tax brackets.

---

## Step 6: VAPZ/PLCI (Supplementary Pension) [T2]

**Legislation:** WIB 92, Art. 52-53; Programmawet 24 December 2002

### Vrij Aanvullend Pensioen voor Zelfstandigen (VAPZ) / Pension Libre Complémentaire pour Indépendants (PLCI)

| Type | Maximum Deduction |
|------|------------------|
| Gewoon VAPZ / PLCI ordinaire | 8.17% of reference income (max approx. EUR 3,965 for 2025) |
| Sociaal VAPZ / PLCI sociale | 9.40% of reference income (max approx. EUR 4,562 for 2025) |

### Rules [T2]

- Reference income = net professional income from 3 years prior (indexed).
- VAPZ contributions are deductible as social contributions (not as Sonderausgaben).
- The sociaal VAPZ provides additional social cover (disability, hospitalisation).
- [T2] Flag for reviewer: confirm reference income and maximum limit.

---

## Step 7: Afschrijvingen (Depreciation) [T1]

**Legislation:** WIB 92, Art. 61-65

### Standard Depreciation (Straight-Line)

| Asset Type | Useful Life | Annual Rate |
|-----------|-------------|-------------|
| Computer hardware | 3 years | 33.3% |
| Computer software | 3 years | 33.3% |
| Office furniture | 10 years | 10% |
| Motor vehicles | 5 years | 20% |
| Office equipment | 5 years | 20% |
| Buildings (commercial) | 33 years | 3% |

### Rules [T1]

- Depreciation is generally straight-line (lineair / linéaire).
- Declining balance (degressief / dégressif) is permitted for certain assets at up to double the straight-line rate.
- In the year of acquisition, pro-rata depreciation applies based on the period of use within the year.
- Small companies may apply declining balance depreciation.

---

## Step 8: Computation Walkthrough [T1]

### Step-by-Step

1. **Gross professional income** (beroepsinkomsten).
2. **Less: Beroepskosten** (actual or forfaitaire -- not both).
3. **Less: Sociale bijdragen** (if using actual expenses method, included in beroepskosten).
4. **Net professional income** (netto beroepsinkomen).
5. **Add other income** (employment, rental, investment, foreign).
6. **Total net income** (totaal netto inkomen).
7. **Apply progressive tax brackets** (Step 1).
8. **Gross federal tax**.
9. **Less: Belastingvrij minimum reduction** (EUR 10,910 x 25% = EUR 2,727.50 base).
10. **Less: Other tax reductions** (VAPZ, long-term savings, etc.).
11. **Federal tax payable**.
12. **Add: Gemeentebelasting** (Federal tax x municipal rate).
13. **Total tax liability**.
14. **Less: Voorafbetalingen (advance payments) and withholding tax**.
15. **Balance due / refund**.

---

## Step 9: Voorafbetalingen (Advance Tax Payments) [T1]

**Legislation:** WIB 92, Art. 157-168

### Rules

Self-employed individuals who do not make sufficient advance payments face a tax increase (vermeerdering / majoration).

| Quarter | Payment Deadline | Benefit Percentage (2025 approx.) |
|---------|-----------------|----------------------------------|
| VA1 | 10 April | 12% |
| VA2 | 10 July | 10% |
| VA3 | 10 October | 8% |
| VA4 | 20 December | 6% |

### Key Rule [T1]

- The vermeerdering (increase for insufficient advance payments) is approximately 9% of the tax due (2025).
- Making advance payments earns a bonification that offsets this increase.
- Self-employed individuals should make quarterly advance payments to avoid the surcharge.

---

## Step 10: Filing Deadlines [T1]

**Legislation:** WIB 92; FOD Financiën administrative guidance

| Filing / Payment | Deadline |
|-----------------|----------|
| Tax-on-web (self-filing) | 30 June of the following year (for income year 2025: 30 June 2026) |
| Paper filing | End of June of the following year |
| Filing with accountant (mandataris) | Typically extended to mid-October of the following year |
| Voorafbetalingen | Q1: 10 April, Q2: 10 July, Q3: 10 October, Q4: 20 December |

### Late Filing [T1]

| Offence | Penalty |
|---------|---------|
| Late filing (first offence) | EUR 50 per month delay (can increase for repeat offences) |
| Late payment | Interest (nalatigheidsinterest) currently 4% per year (2025) |
| Non-filing / serious offence | Administrative fine EUR 50 -- EUR 1,250; tax increase 10%--200% |

---

## Step 11: Record Keeping [T1]

**Legislation:** WIB 92; Wetboek van economisch recht

| Requirement | Detail |
|-------------|--------|
| Minimum retention period | 7 years from 1 January of the year following the tax period |
| What to keep | All sales invoices, purchase invoices, bank statements, receipts, contracts, asset register |
| Format | Paper or digital (FOD Financiën accepts digital records) |

---

## Step 12: Edge Case Registry

### EC1 -- Forfaitaire vs actual expenses [T2]
**Situation:** Client has turnover EUR 40,000 and actual expenses EUR 3,000 (excluding sociale bijdragen).
**Resolution:** Forfaitaire deduction: EUR 19,620 x 30% + EUR 20,380 x 11% = EUR 5,886 + EUR 2,241.80 = EUR 8,127.80. Actual: EUR 3,000. Forfaitaire is more favourable. [T2] Flag for reviewer to confirm.

### EC2 -- Gemeentebelasting without known municipality [T1]
**Situation:** Client does not specify municipality of residence.
**Resolution:** STOP. Do not estimate. The gemeentebelasting rate ranges from 0% to 9%. Ask the client for their municipality before computing total tax.

### EC3 -- Restaurant meals deductibility [T1]
**Situation:** Client includes EUR 2,000 restaurant meals (business purpose) in full deductions.
**Resolution:** Restaurant meals with a business purpose are 69% deductible. Deductible amount = EUR 2,000 x 69% = EUR 1,380. Reduce deduction by EUR 620.

### EC4 -- Motor vehicle CO2 deductibility [T2]
**Situation:** Client drives a diesel car with CO2 emissions of 150 g/km.
**Resolution:** From 2025, the deductibility percentage for cars with CO2 emissions is calculated using a formula based on CO2 and fuel type. For high-emission cars, deductibility can drop significantly. [T2] Flag for reviewer to compute exact deductibility using the formula: 120% - (0.5% x coefficient x CO2 g/km).

### EC5 -- Sociale bijdragen in first 3 years [T2]
**Situation:** Client is in the first year of self-employment. Social fund calculates provisional contributions on minimum basis.
**Resolution:** Deduct actual contributions paid. When regularisation happens (based on actual income), additional amounts or refunds are deductible/taxable in the year of payment/receipt. [T2] Flag for reviewer.

### EC6 -- VAPZ exceeds maximum [T1]
**Situation:** Client pays EUR 5,000 into gewoon VAPZ.
**Resolution:** Maximum gewoon VAPZ for 2025 is approximately EUR 3,965. Excess EUR 1,035 is NOT deductible.

### EC7 -- Vermeerdering for no advance payments [T1]
**Situation:** Self-employed client made no voorafbetalingen during 2025.
**Resolution:** A vermeerdering (increase) of approximately 9% of the tax due will be added to the assessment. Advise client to make advance payments in future years.

### EC8 -- Mixed income: employment + self-employment [T1]
**Situation:** Client has EUR 40,000 employment income and EUR 20,000 self-employment profit.
**Resolution:** Both incomes are combined for progressive rate calculation. Total EUR 60,000 goes through the brackets. Employment income tax credits (werkbonus, etc.) apply only to employment income. Self-employment deductions apply only to self-employment income.

### EC9 -- Business gifts deductibility [T2]
**Situation:** Client gives EUR 500 in gifts to business clients.
**Resolution:** Business gifts are 50% deductible (EUR 250). Must be documented with business purpose. [T2] Flag for reviewer.

---

## Step 13: Reviewer Escalation Protocol

When Claude identifies a [T2] situation:

```
REVIEWER FLAG
Tier: T2
Client: [name]
Situation: [description]
Issue: [what is ambiguous]
Options: [possible treatments]
Recommended: [most likely correct treatment and why]
Action Required: Erkend boekhouder-fiscalist must confirm before filing.
```

When Claude identifies a [T3] situation:

```
ESCALATION REQUIRED
Tier: T3
Client: [name]
Situation: [description]
Issue: [outside skill scope]
Action Required: Do not advise. Refer to erkend boekhouder-fiscalist. Document gap.
```

---

## Step 14: Test Suite

### Test 1 -- Standard single self-employed, mid-range income
**Input:** Single, resident in Antwerp (gemeentebelasting 8.4%), turnover EUR 50,000, actual beroepskosten EUR 10,000 (including sociale bijdragen EUR 5,500), no VAPZ, no other income.
**Expected output:** Net income = EUR 40,000. Tax: EUR 16,720 x 25% + EUR 12,790 x 40% + EUR 10,490 x 45% = EUR 4,180 + EUR 5,116 + EUR 4,720.50 = EUR 14,016.50. Less belastingvrij minimum reduction EUR 2,727.50 = EUR 11,289. Gemeentebelasting: EUR 11,289 x 8.4% = EUR 948.28. Total = EUR 12,237.28.

### Test 2 -- Forfaitaire vs actual comparison
**Input:** Turnover EUR 30,000, actual expenses EUR 2,000.
**Expected output:** Forfaitaire: EUR 19,620 x 30% + EUR 10,380 x 11% = EUR 5,886 + EUR 1,141.80 = EUR 7,027.80. Actual: EUR 2,000. Forfaitaire is better by EUR 5,027.80.

### Test 3 -- Restaurant meals partially deductible
**Input:** Client claims EUR 3,000 restaurant meals as full deduction.
**Expected output:** Only 69% deductible. Allowable = EUR 2,070. Remove EUR 930 from deductions.

### Test 4 -- VAPZ cap applied
**Input:** Client contributes EUR 5,000 to gewoon VAPZ. Maximum for 2025 is EUR 3,965.
**Expected output:** Deductible VAPZ = EUR 3,965. Excess EUR 1,035 not deductible.

### Test 5 -- Gemeentebelasting computation
**Input:** Federal tax payable EUR 8,000. Municipality rate 7%.
**Expected output:** Gemeentebelasting = EUR 8,000 x 7% = EUR 560. Total = EUR 8,560.

### Test 6 -- Vermeerdering for no advance payments
**Input:** Total tax due EUR 10,000, no voorafbetalingen made.
**Expected output:** Vermeerdering approximately EUR 900 (9% of EUR 10,000). Total due = EUR 10,900.

---

## PROHIBITIONS

- NEVER compute gemeentebelasting without knowing the municipality of residence and its actual rate
- NEVER compute final tax figures directly -- pass taxable income to the deterministic engine to apply brackets, belastingvrij minimum, and gemeentebelasting
- NEVER allow both werkelijke beroepskosten AND forfaitaire beroepskosten simultaneously
- NEVER deduct restaurant meals at 100% -- the maximum is 69% for business-purpose meals
- NEVER allow income tax (personenbelasting) itself as a deduction
- NEVER allow fines or penalties as a deduction
- NEVER allow VAPZ contributions above the applicable maximum
- NEVER ignore the vermeerdering for missing advance payments
- NEVER present tax calculations as definitive -- always label as estimated and direct client to their boekhouder-fiscalist for confirmation
- NEVER advise on FOD Financiën audit or dispute situations without escalating to a qualified practitioner

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
