---
name: at-income-tax
description: >
  Use this skill whenever asked about Austrian income tax (Einkommensteuer) for self-employed individuals filing form E1. Trigger on phrases like "Einkommensteuer", "ESt", "E1 Erklärung", "Gewinnfreibetrag", "Betriebsausgabenpauschale", "Absetzbeträge", "Sonderausgaben", "selbständig Steuer Österreich", "Austrian income tax", "self-employed tax Austria", or any question about computing or filing income tax for a self-employed person in Austria. This skill covers progressive tax brackets (0--55%), Gewinnfreibetrag, Betriebsausgabenpauschale, Sonderausgaben, außergewöhnliche Belastungen, Absetzbeträge, SV deductibility, and E1/E1a structure. ALWAYS read this skill before touching any Austrian income tax work.
version: 1.0
jurisdiction: AT
tax_year: 2025
category: international
depends_on:
  - income-tax-workflow-base
---

# Austria Income Tax (ESt E1) -- Self-Employed Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Austria |
| Jurisdiction Code | AT |
| Primary Legislation | Einkommensteuergesetz 1988 (EStG 1988) |
| Supporting Legislation | Bundesabgabenordnung (BAO); Gewerbliches Sozialversicherungsgesetz (GSVG); Umsatzsteuergesetz 1994 (UStG) for VAT interaction |
| Tax Authority | Bundesministerium für Finanzen (BMF) |
| Filing Portal | FinanzOnline (finanzonline.bmf.gv.at) |
| Contributor | Open Accountants Community |
| Validated By | Pending -- requires sign-off by a Steuerberater or Wirtschaftsprüfer practising in Austria |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: rate table application, Gewinnfreibetrag (Grundfreibetrag), Betriebsausgabenpauschale, SV deductibility, filing deadlines. Tier 2: investitionsbedingter GFB, mixed-use expense apportionment, außergewöhnliche Belastungen, Sonderausgaben limits. Tier 3: partnerships, group taxation, non-resident income, international structures, Finanzamt audits. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags and presents options. Steuerberater must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate and document.

---

## Step 0: Client Onboarding Questions

Before computing any income tax figure, you MUST know:

1. **Marital / family status** [T1] -- single, married/partnered, sole earner (Alleinverdiener), sole carer (Alleinerzieher). Determines Absetzbeträge eligibility.
2. **Income type** [T1] -- Einkünfte aus Gewerbebetrieb (s.23 EStG) or selbständiger Arbeit (s.22 EStG).
3. **Profit determination method** [T1] -- Einnahmen-Ausgaben-Rechnung (E/A, cash basis) or Bilanzierung (accrual/double-entry).
4. **Gross self-employment income / turnover** [T1] -- total receipts in the year.
5. **Business expenses** [T1/T2] -- nature and amount (actual or Pauschale).
6. **Sozialversicherung (SV) paid** [T1] -- SVS contributions paid in the year.
7. **Capital assets acquired** [T1] -- type, cost, date first used.
8. **Sonderausgaben** [T2] -- church tax, donations, pension contributions.
9. **Außergewöhnliche Belastungen** [T2] -- disability, illness, catastrophe costs.
10. **Other income** [T1] -- employment, rental, capital, foreign income.

**If income type (Gewerbebetrieb vs selbständige Arbeit) is unknown, STOP. This determines the Betriebsausgabenpauschale rate.**

---

## Step 1: Determine Applicable Tax Brackets [T1]

**Legislation:** EStG 1988, s.33 (as adjusted for 2025 cold progression)

### Progressive Income Tax Rates (2025)

| Taxable Income (EUR) | Marginal Rate | Notes |
|---------------------|---------------|-------|
| 0 -- 13,308 | 0% | Tax-free threshold (adjusted for cold progression) |
| 13,309 -- 21,617 | 20% | |
| 21,618 -- 35,836 | 30% | |
| 35,837 -- 69,166 | 40% | |
| 69,167 -- 103,072 | 48% | |
| 103,073 -- 1,000,000 | 50% | |
| Above 1,000,000 | 55% | Extended through 2025 (originally temporary) |

**Note (2025):** Since 2023, tariff levels are adjusted annually by two-thirds of the inflation rate to counteract cold progression (kalte Progression). The 55% rate for income above EUR 1M was originally temporary (2016--2025) and is still in effect for 2025.

**Austria does not have a separate personal allowance -- the 0% band IS the tax-free threshold (Steuerfreibetrag).**

---

## Step 2: Gewinnfreibetrag (Profit Allowance) [T1/T2]

**Legislation:** EStG 1988, s.10

### Structure (2025)

| Profit Range (EUR) | Rate | Type | Investment Required? |
|--------------------|----- |------|---------------------|
| 0 -- 33,000 | 15% | Grundfreibetrag (basic) | No |
| 33,001 -- 178,000 | 13% | Investitionsbedingter GFB | Yes [T2] |
| 178,001 -- 353,000 | 7% | Investitionsbedingter GFB | Yes [T2] |
| 353,001 -- 583,000 | 4.5% | Investitionsbedingter GFB | Yes [T2] |

### Maximum Gewinnfreibetrag: EUR 46,400

### Rules [T1]

- The Grundfreibetrag (15% of first EUR 33,000 = max EUR 4,950) is automatic. No investment required.
- The investitionsbedingter GFB (above EUR 33,000) requires the purchase of qualifying physical assets (Wirtschaftsgüter with useful life of 4+ years) or qualifying securities (Wertpapiere per s.14 Abs 7 Z 4 EStG).
- The GFB reduces the taxable profit BEFORE applying the tax brackets.
- [T2] Flag for reviewer: confirm qualifying investments have been made if claiming the investment-related portion.

---

## Step 3: Betriebsausgabenpauschale (Flat-Rate Business Expenses) [T1]

**Legislation:** EStG 1988, s.17

### Rates

| Category | Flat-Rate % | Conditions |
|----------|------------|------------|
| Gewerbebetrieb (trade/business) | 12% of turnover | Max EUR 26,400 |
| Certain professions (writers, scientists, artists, consultants) | 6% of turnover | Max EUR 13,200 |

### Rules [T1]

- The Pauschale is an ALTERNATIVE to claiming actual business expenses. You choose one or the other, not both.
- If claiming the Pauschale, you may STILL deduct: SV contributions, the Gewinnfreibetrag, and contributions to employee pension funds.
- The Pauschale is attractive when actual business expenses are low relative to turnover.
- [T2] Flag for reviewer if actual expenses would produce a better result than the Pauschale.

---

## Step 4: Allowable Business Expenses (Betriebsausgaben) [T1/T2]

**Legislation:** EStG 1988, s.4 Abs 4

### Deductible Expenses

| Expense | Tier | Treatment |
|---------|------|-----------|
| Office rent (dedicated) | T1 | Fully deductible |
| Professional insurance | T1 | Fully deductible |
| Accountancy / Steuerberatung fees | T1 | Fully deductible |
| Office supplies / materials | T1 | Fully deductible |
| Software subscriptions | T1 | Fully deductible |
| Marketing / advertising | T1 | Fully deductible |
| Bank charges (business account) | T1 | Fully deductible |
| Professional development / Fortbildung | T1 | Fully deductible |
| Travel (Dienstreisen) | T1 | Per diem rates (Taggelder) apply: EUR 26.40/day domestic |
| Sozialversicherung (SVS) | T1 | Fully deductible as Betriebsausgabe |
| Telephone / internet | T2 | Business use portion only |
| Motor vehicle (Kfz) | T2 | Business use portion, max EUR 40,000 Anschaffungskosten for luxury cap (Luxustangente) |
| Home office (Arbeitszimmer) | T2 | Must be dedicated room, centre of professional activity |
| Representation / Bewirtung | T2 | 50% deductible if business purpose documented; 0% if purely entertainment |

### NOT Deductible [T1]

| Expense | Reason |
|---------|--------|
| Personal living expenses (Lebenshaltungskosten) | Not business-related |
| Fines and penalties (Geldstrafen) | Public policy |
| Income tax itself (Einkommensteuer) | Tax on income |
| Capital expenditure | Goes through Absetzung für Abnutzung (AfA) |
| Donations (unless to listed organisations) | Only qualifying donations deductible as Sonderausgaben |

---

## Step 5: Absetzung für Abnutzung (AfA -- Depreciation) [T1]

**Legislation:** EStG 1988, s.7, s.8

### Standard Depreciation (Straight-Line)

| Asset Type | Useful Life | Annual Rate |
|-----------|-------------|-------------|
| Computer hardware | 3 years | 33.3% |
| Computer software | 3 years | 33.3% |
| Office furniture | 10 years | 10% |
| Motor vehicles | 8 years | 12.5% |
| Plant and machinery | 5--15 years | 6.7%--20% |
| Buildings (business) | 33 years (commercial) | 3% |
| Buildings (residential rental) | 67 years | 1.5% |

### Rules [T1]

- Depreciation is straight-line (linear) based on cost (Anschaffungs- or Herstellungskosten).
- In the year of acquisition, pro-rata depreciation applies based on the date of first use (Halbjahresregel: if acquired in second half, only half-year AfA).
- Geringwertige Wirtschaftsgüter (GWG -- low-value assets): assets with cost up to EUR 1,000 (net) may be expensed immediately in the year of acquisition.
- Motor vehicles: Luxustangente applies -- cost capped at EUR 40,000 for AfA purposes. If car costs EUR 50,000, AfA is calculated on EUR 40,000 only.

---

## Step 6: Sozialversicherung (SV) Deductibility [T1]

**Legislation:** GSVG; EStG 1988, s.4 Abs 4

### SVS Contributions (Self-Employed -- Sozialversicherungsanstalt der Selbständigen)

| Component | Rate (2025 approx.) | Ceiling |
|-----------|---------------------|---------|
| Krankenversicherung (health) | 6.80% | Subject to Höchstbeitragsgrundlage |
| Pensionsversicherung (pension) | 18.50% | Subject to Höchstbeitragsgrundlage |
| Unfallversicherung (accident) | Fixed monthly amount | Approx. EUR 11.35/month |
| Selbständigenvorsorge | 1.53% | Subject to ceiling |

### Rules [T1]

- ALL SVS contributions are fully deductible as Betriebsausgaben (business expenses).
- SVS contributions are deducted BEFORE computing the Gewinnfreibetrag.
- In the first three years of self-employment, preliminary SV contributions are based on estimated minimum basis. Actual reconciliation happens later.
- [T2] Flag: if SV contributions are recalculated retrospectively, the adjustment goes in the year of payment/refund.

---

## Step 7: Sonderausgaben (Special Expenses) [T2]

**Legislation:** EStG 1988, s.18

| Sonderausgabe | Deduction | Notes |
|---------------|-----------|-------|
| Kirchenbeitrag (church tax) | Up to EUR 600/year | [T1] |
| Spenden (donations to listed organisations) | Up to 10% of prior year income | [T2] verify organisation is on BMF list |
| Steuerberatungskosten | Unlimited | Also qualifiable as Betriebsausgabe |
| Freiwillige Weiterversicherung (voluntary pension) | Actual amount | [T2] |
| Nachkauf von Versicherungszeiten | Actual amount | [T2] |

### Sonderausgabenpauschale

If no specific Sonderausgaben are claimed, a flat EUR 60/year is automatically deducted.

---

## Step 8: Außergewöhnliche Belastungen (Extraordinary Burdens) [T2]

**Legislation:** EStG 1988, s.34, s.35

- Deductible only to the extent they exceed the Selbstbehalt (deductible threshold), which depends on income and family status (6--12% of income).
- Categories: medical costs not covered by insurance, disability costs, catastrophe damage.
- No Selbstbehalt for disability-related costs if disability is documented.
- [T2] Always flag for reviewer -- documentation and threshold calculation required.

---

## Step 9: Absetzbeträge (Tax Credits) [T1]

**Legislation:** EStG 1988, s.33

### Credits (2025, adjusted for cold progression)

| Absetzbetrag | Amount (EUR) | Conditions |
|--------------|-------------|------------|
| Verkehrsabsetzbetrag (commuter credit) | 463 | For employees; self-employed may qualify if also employed |
| Erhöhter Verkehrsabsetzbetrag | 798 | Income below EUR 16,832, commuter |
| Alleinverdienerabsetzbetrag (sole earner) | 572 (no child), 746 (1 child), +255 per additional child | Partner income max EUR 6,937 |
| Alleinerzieherabsetzbetrag (sole carer) | 572 (1 child), 746 (2 children), +255 per additional child | Single parent |
| Unterhaltsabsetzbetrag (maintenance) | 35/52/69 per month | For children not in same household |
| Kindermehrbetrag | Up to 700 | If no tax liability to offset Kinderabsetzbetrag |
| SV-Rückerstattung (SV refund for low earners) | Up to 55% of SV | If income is below tax threshold |

### Rules [T1]

- Absetzbeträge reduce the TAX PAYABLE, not the taxable income.
- They are applied AFTER computing tax from the rate table.

---

## Step 10: Computation Walkthrough [T1]

### Step-by-Step

1. **Compute profit** from self-employment (Einkünfte aus Gewerbebetrieb or selbständiger Arbeit).
2. **Deduct SVS contributions** (Betriebsausgabe).
3. **Deduct business expenses** (actual or Pauschale -- not both).
4. **Apply Gewinnfreibetrag** (15% Grundfreibetrag automatic; investment GFB if qualifying assets purchased).
5. **Add other income** (employment, rental, capital, foreign).
6. **Total income (Gesamtbetrag der Einkünfte)**.
7. **Less: Sonderausgaben** (church tax, donations, etc.).
8. **Less: Außergewöhnliche Belastungen** (above Selbstbehalt).
9. **Taxable income (Einkommen)**.
10. **Apply progressive tax brackets** (Step 1).
11. **Less: Absetzbeträge** (Step 9).
12. **Income tax payable (Einkommensteuer)**.

---

## Step 11: Filing Deadlines [T1]

**Legislation:** BAO; EStG 1988

| Filing / Payment | Deadline |
|-----------------|----------|
| E1 (paper filing) | 30 April of the following year |
| E1 (FinanzOnline e-filing) | 30 June of the following year |
| E1 (with Steuerberater representation) | End of February of the second following year (i.e., for 2025: 28 Feb 2027) |
| Einkommensteuervorauszahlungen (quarterly) | 15 Feb, 15 May, 15 Aug, 15 Nov |

### Late Filing [T1]

| Offence | Penalty |
|---------|---------|
| Late filing (Verspätungszuschlag) | Up to 10% of assessed tax |
| Late payment (Säumniszuschlag) | 2% of unpaid amount (first instance) |
| Repeated late payment | Additional 1% each (2nd and 3rd) |

---

## Step 12: Einkommensteuervorauszahlungen (Quarterly Prepayments) [T1]

**Legislation:** EStG 1988, s.45

### Rules

- Based on the most recent tax assessment (Bescheid).
- Finanzamt sets the quarterly amounts by notice.
- Payable in four instalments: 15 Feb, 15 May, 15 Aug, 15 Nov.
- Taxpayer may apply for reduction (Herabsetzungsantrag) if income has dropped significantly. [T2] Flag for reviewer.

---

## Step 13: Edge Case Registry

### EC1 -- Gewinnfreibetrag without qualifying investment [T1]
**Situation:** Client has profit of EUR 50,000 and claims full GFB without purchasing qualifying assets.
**Resolution:** Only the Grundfreibetrag is automatic: 15% of EUR 33,000 = EUR 4,950. The investment-related GFB on EUR 17,000 (EUR 50,000 - EUR 33,000) x 13% = EUR 2,210 requires qualifying investments. If no investments made, GFB = EUR 4,950 only.

### EC2 -- Betriebsausgabenpauschale vs actual expenses [T2]
**Situation:** Client has turnover of EUR 80,000 and actual expenses of EUR 6,000 (excluding SV).
**Resolution:** Pauschale = 12% x EUR 80,000 = EUR 9,600. Actual expenses = EUR 6,000. Pauschale is more favourable. But SV is deductible in ADDITION to the Pauschale. [T2] Flag for reviewer to confirm which method is optimal.

### EC3 -- Luxustangente motor vehicle [T1]
**Situation:** Client buys a car for EUR 55,000 and claims full AfA.
**Resolution:** INCORRECT. AfA is capped at EUR 40,000 (Luxustangente). Annual AfA = EUR 40,000 / 8 years = EUR 5,000, multiplied by business-use percentage.

### EC4 -- GWG immediate expensing [T1]
**Situation:** Client buys office equipment for EUR 800 net.
**Resolution:** Asset qualifies as geringwertiges Wirtschaftsgut (under EUR 1,000 net). May be expensed immediately in the year of acquisition. No multi-year AfA required.

### EC5 -- First year SV contributions [T2]
**Situation:** Client starts self-employment in 2025. SVS sets preliminary contributions based on minimum basis.
**Resolution:** Deduct actual SV paid in 2025. When SVS recalculates based on actual income (usually 2--3 years later), any additional payment or refund is deductible/taxable in the year of payment/receipt. [T2] Flag for reviewer.

### EC6 -- Dual income: Pauschale and employment [T1]
**Situation:** Client is employed and has self-employment income. Wants to use Pauschale for self-employment.
**Resolution:** The Pauschale applies only to self-employment turnover. Employment income is taxed under standard PAYE rules. Both income types are combined for the progressive rate calculation.

### EC7 -- Bewirtung (business entertainment) [T2]
**Situation:** Client takes a client to dinner (EUR 150) and wants to deduct it.
**Resolution:** 50% deductible (EUR 75) if a clear business purpose (Werbezweck) is documented and the entertainment has an advertising character. Purely social entertainment is 0% deductible. [T2] Flag for reviewer to assess purpose.

### EC8 -- Sonderausgaben church tax cap [T1]
**Situation:** Client paid EUR 900 Kirchenbeitrag.
**Resolution:** Deductible up to EUR 600. Excess EUR 300 is not deductible.

### EC9 -- Home office (Arbeitszimmer) [T2]
**Situation:** Client works from a room at home and wants to deduct proportional costs.
**Resolution:** Deductible only if the room is the centre of professional activity (Mittelpunkt der Tätigkeit) and used exclusively for business. A dual-use room does not qualify. [T2] Flag for reviewer to confirm workspace arrangement.

### EC10 -- 55% rate applicability [T1]
**Situation:** Client has taxable income of EUR 1,200,000.
**Resolution:** The 55% rate applies to income above EUR 1,000,000. Tax on the portion EUR 1,000,001 to EUR 1,200,000 = EUR 200,000 x 55% = EUR 110,000. Verify that the 55% rate remains in force for 2025 (it was extended from the original temporary period).

---

## Step 14: Reviewer Escalation Protocol

When Claude identifies a [T2] situation:

```
REVIEWER FLAG
Tier: T2
Client: [name]
Situation: [description]
Issue: [what is ambiguous]
Options: [possible treatments]
Recommended: [most likely correct treatment and why]
Action Required: Steuerberater must confirm before filing.
```

When Claude identifies a [T3] situation:

```
ESCALATION REQUIRED
Tier: T3
Client: [name]
Situation: [description]
Issue: [outside skill scope]
Action Required: Do not advise. Refer to Steuerberater. Document gap.
```

---

## Step 15: Test Suite

### Test 1 -- Standard self-employed, mid-range income
**Input:** Single, turnover EUR 60,000, actual expenses EUR 12,000, SVS paid EUR 8,000, no other income.
**Expected output:** Revenue EUR 60,000 - expenses EUR 12,000 - SV EUR 8,000 = EUR 40,000 profit. Grundfreibetrag: 15% x EUR 33,000 = EUR 4,950. Taxable income: EUR 35,050. Tax: EUR 0 + (EUR 21,617 - EUR 13,308) x 20% + (EUR 35,050 - EUR 21,617) x 30% = EUR 1,661.80 + EUR 4,029.90 = EUR 5,691.70 (before Absetzbeträge).

### Test 2 -- Betriebsausgabenpauschale comparison
**Input:** Gewerbebetrieb, turnover EUR 50,000, actual expenses EUR 4,000, SVS EUR 6,500.
**Expected output:** Pauschale method: EUR 50,000 - EUR 6,000 (12% Pauschale) - EUR 6,500 (SV) = EUR 37,500 profit. Actual method: EUR 50,000 - EUR 4,000 - EUR 6,500 = EUR 39,500 profit. Pauschale is more favourable.

### Test 3 -- Luxustangente applied
**Input:** Client buys car for EUR 60,000, 80% business use.
**Expected output:** AfA capped at EUR 40,000. Annual AfA = EUR 40,000 / 8 = EUR 5,000 x 80% = EUR 4,000.

### Test 4 -- GWG immediate write-off
**Input:** Client buys EUR 900 office chair.
**Expected output:** Immediate full deduction in the year of purchase (GWG under EUR 1,000).

### Test 5 -- Gewinnfreibetrag with investment
**Input:** Profit EUR 80,000, client purchased EUR 10,000 qualifying Wertpapiere.
**Expected output:** Grundfreibetrag: EUR 4,950. Investment GFB available: (EUR 80,000 - EUR 33,000) x 13% = EUR 6,110. But limited to actual qualifying investment of EUR 10,000 -- so EUR 6,110 is fully covered. Total GFB = EUR 4,950 + EUR 6,110 = EUR 11,060.

### Test 6 -- Kirchenbeitrag exceeds cap
**Input:** Client paid EUR 800 church tax.
**Expected output:** Sonderausgaben deduction for Kirchenbeitrag capped at EUR 600. EUR 200 excess not deductible.

---

## PROHIBITIONS

- NEVER apply tax brackets without confirming the income type (Gewerbebetrieb vs selbständige Arbeit)
- NEVER compute final tax figures directly -- pass taxable income to the deterministic engine to apply the progressive rate table
- NEVER allow both the Betriebsausgabenpauschale AND actual expense deductions simultaneously (except SV and GFB which are additional)
- NEVER apply the investitionsbedingter Gewinnfreibetrag without confirmed qualifying investments
- NEVER apply motor vehicle AfA above the EUR 40,000 Luxustangente
- NEVER allow income tax (Einkommensteuer) itself as a deduction
- NEVER allow fines or penalties as a deduction
- NEVER allow a GWG-eligible asset (under EUR 1,000) to be depreciated over multiple years unless the client specifically elects to do so
- NEVER present tax calculations as definitive -- always label as estimated and direct client to their Steuerberater for confirmation
- NEVER advise on Finanzamt audit or appeal situations without escalating to a Steuerberater

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
