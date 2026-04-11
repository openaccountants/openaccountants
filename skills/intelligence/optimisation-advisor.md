---
name: optimisation-advisor
description: >
  Intelligence skill that identifies tax savings opportunities after the base computation is complete. Runs 40 optimisation checks across 8 jurisdictions (US, UK, DE, AU, CA, IN, ES, MT) covering retirement contributions, entity structure, timing, elections, and unclaimed reliefs. Each check has a trigger condition, calculation formula, materiality threshold (EUR/USD 100 minimum), and reviewer flag.
version: 0.1
category: intelligence
depends_on:
  - workflow-base
triggers:
  - tax savings
  - optimisation
  - optimization
  - how can I save tax
  - reduce my tax
  - tax planning
  - deductions I missed
  - am I missing anything
---

# Optimisation Advisor v0.1

## What this file is

**Obligation category:** INTEL (Intelligence / Cross-cutting)
**Functional role:** Post-computation optimisation scanning, savings identification
**Status:** Active

This is an intelligence skill that loads on top of `workflow-base`. It runs after a base tax computation is complete (or after sufficient income/expense data is available) and scans for savings opportunities the user may not have claimed or considered.

**The reviewer is the customer of this output.** All optimisation suggestions are addressed to the credentialed reviewer. The reviewer decides which opportunities to pursue and validates the calculations.

> **Disclaimer.** Optimisation suggestions are based on general statutory rules and the user's data as provided. They do not constitute tax advice, tax planning, or a recommendation to take any specific action. Every suggestion must be reviewed by a credentialed professional who can assess the user's full circumstances, including factors not captured in the data. Savings estimates are approximations and may differ from actual outcomes. Aggressive or novel positions are never suggested. OpenAccountants accepts no liability for actions taken based on these suggestions.

---

## Section 1 -- Scope statement

This skill covers:

- **Jurisdictions:** US, UK, DE, AU, CA, IN, ES, MT (8 jurisdictions, 5 checks each = 40 checks)
- **Check categories:** Retirement contributions, entity structure, timing, elections, unclaimed credits/reliefs
- **Output:** Ranked list of savings opportunities with estimated value

This skill does NOT cover:

- Corporate tax planning, transfer pricing, or group restructuring
- Aggressive tax positions, tax shelters, or schemes requiring DOTAS/GAAR disclosure
- Cross-border restructuring (see cross-border skills)
- Opportunities below the materiality threshold (EUR/USD 100 or local equivalent)
- Retrospective amendments to prior-year returns (flag for reviewer only)

---

## Section 2 -- Workflow

### Step 0 -- Gather computation outputs

This skill requires at least one of:

1. **Completed tax computation** from a content skill (e.g., Schedule C output, SA100 computation)
2. **Income and expense summary** with enough detail to run checks
3. **Explicit user data** -- "I earned $X, my expenses were $Y, I contributed $Z to retirement"

If insufficient data, state which checks cannot be run and what data is needed.

### Step 1 -- Run optimisation checks

For each check applicable to the user's jurisdiction:

1. **Evaluate the trigger condition** -- does the check apply to this user?
2. **If triggered, run the calculation** -- compute the estimated savings
3. **Apply the materiality filter** -- suppress if savings < threshold
4. **Assign a confidence tier:**
   - T1: Deterministic -- savings calculation is mechanical and certain
   - T2: Reviewer judgment -- savings depend on facts the skill cannot verify
5. **Flag for reviewer** -- every optimisation is flagged; some require active reviewer decision

### Step 2 -- Rank and present

Sort all triggered checks by estimated savings (descending). Present per Section 5.

### Step 3 -- Caveats

For each suggestion, state:
- What assumption was made
- What could change the result
- Whether timing matters (current year only, or can be applied retroactively)

---

## Section 3 -- Optimisation checks by jurisdiction

### 3.1 United States (US) -- 5 checks

#### US-OPT-1: Retirement contribution room

| Field | Detail |
|---|---|
| **Category** | Retirement contributions |
| **Trigger** | User has SE income > $0 AND has not maximised retirement contributions |
| **Vehicles** | Solo 401(k): $23,500 employee + 20% of net SE income employer (total cap $70,000). SEP-IRA: 20% of net SE income (cap $70,000). SIMPLE IRA: $16,500 + 3% match. Traditional IRA: $7,000. Age 50+ catch-up: +$7,500 (401k), +$1,000 (IRA). Age 60-63 super catch-up: +$11,250 (401k). |
| **Calculation** | `savings = (contribution_room_remaining) x marginal_federal_rate`. Example: $30,000 remaining room x 32% = $9,600 federal tax savings. Add state savings if applicable. |
| **Materiality** | > $100 federal tax savings |
| **Confidence** | T1 if contribution amounts are known; T2 if estimated |
| **Reviewer flag** | Verify no other employer plans. Check MAGI limits for traditional IRA deductibility. Confirm plan establishment deadlines (Solo 401k by Dec 31; SEP-IRA by filing deadline + extensions). |
| **Output** | "You can contribute $[X] more to a [Solo 401(k)/SEP-IRA] and save approximately $[Y] in federal tax (plus $[Z] in [state] tax)." |

#### US-OPT-2: Entity structure -- S-Corp election

| Field | Detail |
|---|---|
| **Category** | Entity structure |
| **Trigger** | Net SE income > $60,000 AND user is filing as sole prop or SMLLC |
| **Calculation** | Estimate SE tax savings from S-Corp election: `se_savings = (net_se_income - reasonable_salary) x 15.3%`, capped at OASDI limit. Subtract S-Corp costs: payroll processing (~$2,000/yr), additional return (Form 1120-S ~$1,500), state fees. `net_savings = se_savings - additional_costs`. |
| **Materiality** | > $3,000 net annual savings (to justify complexity) |
| **Confidence** | T2 -- reasonable salary determination requires judgment |
| **Reviewer flag** | Reasonable salary must be defensible. QBI deduction impact must be modelled (W-2 wages affect QBI calculation). State-level implications vary. Late S-Corp election (Form 2553) may require relief. |
| **Output** | "At your income level ($[X] net SE income), an S-Corp election could save approximately $[Y]/year in self-employment tax after accounting for additional costs of ~$[Z]. Reviewer: reasonable salary determination required." |

#### US-OPT-3: Timing -- income deferral / expense acceleration

| Field | Detail |
|---|---|
| **Category** | Timing |
| **Trigger** | User is cash-basis AND (a) has invoices near year-end that could be deferred, OR (b) has deductible expenses that could be prepaid |
| **Calculation** | `savings = deferred_income x marginal_rate` (if income will be taxed at a lower rate next year) OR `savings = accelerated_expense x marginal_rate` |
| **Materiality** | > $200 tax impact |
| **Confidence** | T2 -- depends on next-year income projection |
| **Reviewer flag** | Constructive receipt doctrine: income is taxable when available, not when collected. Cannot defer income already earned and available. Prepaid expenses: 12-month rule for cash basis. |
| **Output** | "Deferring $[X] of invoicing to next period could save $[Y] if your marginal rate drops. Caution: constructive receipt rules apply -- reviewer should confirm eligibility." |

#### US-OPT-4: Election -- home office method

| Field | Detail |
|---|---|
| **Category** | Elections |
| **Trigger** | User claims home office AND has not evaluated both methods |
| **Calculation** | Compare: (a) Simplified method: $5/sq ft x min(sq_ft, 300) = max $1,500. (b) Actual method (Form 8829): (business_pct x (mortgage_interest + property_tax + insurance + utilities + repairs + depreciation)). `savings = abs(method_a - method_b) x marginal_rate`. |
| **Materiality** | > $100 tax difference between methods |
| **Confidence** | T1 if actual expenses are known; T2 if estimated |
| **Reviewer flag** | Actual method requires exclusive and regular use. Depreciation recapture on sale of home. Simplified method has no recapture but caps at $1,500. |
| **Output** | "Switching from [simplified/actual] to [actual/simplified] home office method would save $[X] in tax this year. [If actual is better: 'Note: depreciation recapture applies on future sale.']" |

#### US-OPT-5: Unclaimed -- Self-employed health insurance deduction

| Field | Detail |
|---|---|
| **Category** | Credits/reliefs not claimed |
| **Trigger** | User has SE income AND pays health/dental/vision premiums AND has not claimed the above-the-line deduction |
| **Calculation** | `savings = eligible_premiums x marginal_rate`. Eligible premiums cannot exceed net SE income. Cannot claim if eligible for employer-subsidised plan (including spouse's). |
| **Materiality** | > $100 tax savings |
| **Confidence** | T1 if premiums and eligibility are known; T2 otherwise |
| **Reviewer flag** | Check months of eligibility. Cannot overlap with Premium Tax Credit (Form 8962). Spouse's employer plan disqualifies for months coverage is available. |
| **Output** | "You paid $[X] in health insurance premiums but did not claim the self-employed health insurance deduction. This could save $[Y] in tax." |

---

### 3.2 United Kingdom (UK) -- 5 checks

#### UK-OPT-1: Pension contribution room

| Field | Detail |
|---|---|
| **Category** | Retirement contributions |
| **Trigger** | User has not contributed the full annual allowance to a pension |
| **Calculation** | Annual allowance: GBP 60,000 (or 100% of relevant UK earnings if lower). Carry-forward: unused allowance from prior 3 tax years. `savings = unused_allowance x marginal_rate`. At 40% rate: GBP 10,000 contribution = GBP 4,000 tax relief. At 45%: GBP 4,500. Bonus: if income is in GBP 100,000--125,140 band, effective relief is 60% due to PA taper. |
| **Materiality** | > GBP 100 tax savings |
| **Confidence** | T1 if contribution and income data known; T2 if carry-forward amounts are estimated |
| **Reviewer flag** | Tapered annual allowance for adjusted income > GBP 260,000 (reduces to min GBP 10,000). Money purchase annual allowance (GBP 10,000) if flexibly accessed pension. Check carry-forward availability. |
| **Output** | "You can contribute GBP [X] more to your pension and save approximately GBP [Y] in income tax. [If in taper band: 'Contributions in the GBP 100,000--125,140 band are especially valuable at an effective 60% relief rate.']" |

#### UK-OPT-2: Entity structure -- incorporation

| Field | Detail |
|---|---|
| **Category** | Entity structure |
| **Trigger** | User is sole trader AND net profit > GBP 50,000 |
| **Calculation** | Compare: (a) Sole trader: income tax at marginal rates + Class 2 (GBP 3.45/wk) + Class 4 NICs (6%/2%). (b) Ltd company: corporation tax at 25% (or 19% small profits rate if profit < GBP 50,000) + salary (NIC-optimised at GBP 12,570) + dividends (8.75%/33.75%/39.35%). `net_savings = sole_trader_total_tax - ltd_total_tax - additional_costs`. Additional costs: accountancy (~GBP 1,500-3,000), Companies House fees, payroll. |
| **Materiality** | > GBP 2,000 net annual savings |
| **Confidence** | T2 -- depends on profit extraction strategy and IR35 status |
| **Reviewer flag** | IR35/off-payroll rules. Loss of sole trader loss relief flexibility. Employer's NIC on salary. Dividend allowance (GBP 500). Associated company rules for CT rate. |
| **Output** | "At your profit level (GBP [X]), incorporating as a limited company could save approximately GBP [Y]/year. Reviewer: IR35 status and profit extraction strategy must be assessed." |

#### UK-OPT-3: Timing -- payments on account reduction

| Field | Detail |
|---|---|
| **Category** | Timing |
| **Trigger** | User's current-year income is expected to be significantly lower than prior year AND payments on account are based on prior-year liability |
| **Calculation** | `cash_flow_benefit = (prior_year_POA - estimated_current_year_POA)`. Not a permanent tax saving but a timing benefit. Interest at HMRC late-payment rate if reduction is excessive. |
| **Materiality** | > GBP 500 cash flow benefit |
| **Confidence** | T2 -- depends on income projection accuracy |
| **Reviewer flag** | HMRC charges interest if POA reduction results in underpayment. Conservative approach: reduce only if high confidence income is lower. Form SA303. |
| **Output** | "Your payments on account are based on last year's higher income. You could apply to reduce them by GBP [X], improving cash flow. Reviewer: confirm income projection before filing SA303." |

#### UK-OPT-4: Election -- cash basis vs accruals

| Field | Detail |
|---|---|
| **Category** | Elections |
| **Trigger** | User is sole trader with turnover < GBP 150,000 AND has not evaluated cash basis |
| **Calculation** | Cash basis: income recognised when received, expenses when paid. Benefit if year-end debtors > year-end creditors (defer tax). Limitation: no loss relief against other income, limited interest deduction (GBP 500). `tax_timing_benefit = (debtors - creditors) x marginal_rate`. |
| **Materiality** | > GBP 200 timing benefit |
| **Confidence** | T2 -- depends on debtor/creditor position |
| **Reviewer flag** | Cash basis is default for eligible traders from 2024-25. Must opt out if accruals preferred. Capital expenditure treatment differs. Loss restriction. |
| **Output** | "Under cash basis accounting, your tax liability would be [higher/lower] by GBP [X] this year due to your debtor/creditor position. [Recommendation based on analysis.]" |

#### UK-OPT-5: Unclaimed -- Trading allowance

| Field | Detail |
|---|---|
| **Category** | Credits/reliefs not claimed |
| **Trigger** | User has gross trading income < GBP 1,000 from a secondary source AND has not claimed the trading allowance |
| **Calculation** | GBP 1,000 trading allowance: if gross income < GBP 1,000, no need to report or pay tax. If gross > GBP 1,000, can deduct GBP 1,000 instead of actual expenses. `savings = min(gross_income, 1000) x marginal_rate` if not reporting, or `savings = (1000 - actual_expenses) x marginal_rate` if GBP 1,000 > actual expenses. |
| **Materiality** | > GBP 100 |
| **Confidence** | T1 |
| **Reviewer flag** | Cannot use alongside actual expenses for same source. Does not apply to income from own company or partnership. |
| **Output** | "You have GBP [X] in secondary trading income. The GBP 1,000 trading allowance means [no tax is due / you can deduct GBP 1,000 instead of your actual expenses of GBP [Y], saving GBP [Z]]." |

---

### 3.3 Germany (DE) -- 5 checks

#### DE-OPT-1: Ruerup (Basisrente) contribution room

| Field | Detail |
|---|---|
| **Category** | Retirement contributions |
| **Trigger** | User has not maximised Basisrente (Ruerup) contributions |
| **Calculation** | Max deductible: EUR 29,344 (single) / EUR 58,688 (married) for 2025. 100% deductible since 2023 (Wachstumschancengesetz). `savings = unused_room x marginal_rate`. At 42% top rate: EUR 10,000 contribution = EUR 4,200 tax savings. |
| **Materiality** | > EUR 100 tax savings |
| **Confidence** | T1 if contribution amounts known |
| **Reviewer flag** | Ruerup is illiquid (no early withdrawal). Gesetzliche Rentenversicherung contributions reduce available room. Check Zusammenveranlagung status. |
| **Output** | "You can contribute EUR [X] more to a Ruerup/Basisrente and save approximately EUR [Y] in income tax." |

#### DE-OPT-2: Entity structure -- GmbH vs Einzelunternehmen

| Field | Detail |
|---|---|
| **Category** | Entity structure |
| **Trigger** | Net business income > EUR 80,000 AND user is sole proprietor (Einzelunternehmer) |
| **Calculation** | Compare: (a) Sole prop: ESt at marginal rates (up to 45% + Soli 5.5% = 47.475%) + Gewerbesteuer (offset via section 35 EStG credit). (b) GmbH: KSt 15% + Soli 0.825% + GewSt ~14% = ~30% on retained earnings. Distribution taxed at 25% KapESt + Soli = 26.375% (Abgeltungsteuer) or Teileinkuenfteverfahren (60% taxable at marginal rate). `net_savings = sole_prop_tax - (gmbh_corp_tax + distribution_tax) - formation_costs_amortised`. |
| **Materiality** | > EUR 3,000 net annual savings |
| **Confidence** | T2 -- depends on profit retention vs distribution strategy |
| **Reviewer flag** | Notarisation costs (~EUR 1,000+). EUR 25,000 minimum share capital. Managing director salary (subject to Lohnsteuer + social insurance). Verdeckte Gewinnausschuettung risks. Gewerbesteuer Freibetrag (EUR 24,500) lost for GmbH. |
| **Output** | "At your income level (EUR [X]), a GmbH structure could reduce your overall tax burden by approximately EUR [Y]/year if you retain significant profits. Reviewer: salary optimisation and distribution strategy required." |

#### DE-OPT-3: Timing -- Investitionsabzugsbetrag (IAB)

| Field | Detail |
|---|---|
| **Category** | Timing |
| **Trigger** | User plans to acquire business assets within the next 3 years AND net profit < EUR 200,000 |
| **Calculation** | IAB allows deduction of up to 50% of planned acquisition cost (max EUR 200,000 total IAB). `savings = IAB_amount x marginal_rate`. Must actually acquire the asset within 3 years or reverse. |
| **Materiality** | > EUR 200 tax savings |
| **Confidence** | T2 -- depends on actual future acquisition |
| **Reviewer flag** | Asset must be used >90% for business. If not acquired within 3 years, IAB reversed + interest (6% p.a. under section 233a AO). Applies to moveable assets only. |
| **Output** | "If you plan to purchase business equipment costing EUR [X], you can claim an Investitionsabzugsbetrag of EUR [Y] (50%) now and save EUR [Z] in tax this year. The asset must be acquired within 3 years." |

#### DE-OPT-4: Election -- Kleinunternehmer opt-in/opt-out

| Field | Detail |
|---|---|
| **Category** | Elections |
| **Trigger** | User is near the EUR 25,000 Kleinunternehmer threshold OR is currently Kleinunternehmer with significant input VAT |
| **Calculation** | Compare: (a) Kleinunternehmer: no VAT charged, no input VAT recovered. (b) Regelbesteuerung: charge 19% VAT, recover all input VAT. `net_benefit = annual_input_vat_recoverable - admin_cost_estimate`. If B2B clients (who recover VAT anyway): Regelbesteuerung is usually neutral on price. |
| **Materiality** | > EUR 200 annual net benefit |
| **Confidence** | T2 -- depends on client mix (B2B vs B2C) and input VAT |
| **Reviewer flag** | Opting into Regelbesteuerung binds for 5 calendar years (section 19(2) UStG). B2C pricing impact: prices effectively rise 19% or margin drops. |
| **Output** | "You are currently [Kleinunternehmer/Regelbesteuerung]. Switching to [the other] could [save/cost] EUR [X]/year. [If Kleinunternehmer with high input VAT: 'You are forgoing EUR [X] in recoverable input VAT.'] Reviewer: 5-year binding period applies." |

#### DE-OPT-5: Unclaimed -- home office deduction (Homeoffice-Pauschale)

| Field | Detail |
|---|---|
| **Category** | Credits/reliefs not claimed |
| **Trigger** | User works from home AND has not claimed the Homeoffice-Pauschale or hauesliches Arbeitszimmer |
| **Calculation** | Homeoffice-Pauschale: EUR 6/day, max 210 days = EUR 1,260/year (no dedicated room required). Hauesliches Arbeitszimmer (dedicated room): actual costs pro-rata, or EUR 1,260 flat if room is not centre of activity. Full deduction if room is centre of professional activity. `savings = deduction x marginal_rate`. |
| **Materiality** | > EUR 100 tax savings |
| **Confidence** | T1 for Pauschale; T2 for dedicated room (requires exclusive use) |
| **Reviewer flag** | Pauschale reduces the Werbungskostenpauschale (EUR 1,230) -- only beneficial if total Werbungskosten exceed EUR 1,230. Dedicated room requires proof of exclusive business use. |
| **Output** | "You worked [X] days from home. The Homeoffice-Pauschale of EUR [Y] (EUR 6 x [X] days, max EUR 1,260) would save EUR [Z] in tax. [If dedicated room: 'A dedicated home office may allow a higher deduction.']" |

---

### 3.4 Australia (AU) -- 5 checks

#### AU-OPT-1: Superannuation contribution room

| Field | Detail |
|---|---|
| **Category** | Retirement contributions |
| **Trigger** | User has not maximised concessional (pre-tax) super contributions |
| **Calculation** | Concessional cap: AUD 30,000/year (2024-25). Carry-forward: unused cap from prior 5 years if total super balance < AUD 500,000. `savings = unused_cap x marginal_rate - 15%_contributions_tax`. At 37% marginal rate: AUD 10,000 contribution saves AUD 2,200 (37% - 15%). |
| **Materiality** | > AUD 150 tax savings |
| **Confidence** | T1 if contribution and balance data known; T2 if carry-forward estimated |
| **Reviewer flag** | Division 293 tax: additional 15% on concessional contributions if income + contributions > AUD 250,000. Preservation rules (generally no access until age 60). Check employer SG contributions count toward cap. |
| **Output** | "You can contribute AUD [X] more in concessional super contributions and save approximately AUD [Y] in tax (your marginal rate [Z]% less 15% contributions tax)." |

#### AU-OPT-2: Entity structure -- company vs sole trader

| Field | Detail |
|---|---|
| **Category** | Entity structure |
| **Trigger** | Sole trader with net business income > AUD 90,000 |
| **Calculation** | Compare: (a) Sole trader: marginal rates up to 45% + 2% Medicare levy. (b) Company: 25% flat rate (base rate entity if aggregated turnover < AUD 50M). Distribution via franked dividends taxed at marginal rate with franking credit offset. `savings = sole_trader_tax - (company_tax + dividend_tax) - additional_costs`. Additional costs: ASIC fees (~AUD 310/yr), extra accounting (~AUD 2,000-5,000). |
| **Materiality** | > AUD 3,000 net annual savings |
| **Confidence** | T2 -- depends on profit retention and distribution strategy |
| **Reviewer flag** | PSI rules may attribute company income back to individual. Division 7A loan rules. Loss of CGT discount (companies get no 50% discount). Retained profits trapped in company. |
| **Output** | "At your income level (AUD [X]), operating through a company could save approximately AUD [Y]/year if you retain profits. Reviewer: PSI rules and Division 7A implications must be assessed." |

#### AU-OPT-3: Timing -- prepayment of deductible expenses

| Field | Detail |
|---|---|
| **Category** | Timing |
| **Trigger** | User is a small business entity (turnover < AUD 10M) AND has expenses that could be prepaid before 30 June |
| **Calculation** | 12-month prepayment rule: small business can deduct prepaid expenses covering a period of 12 months or less ending in the next income year. `savings = prepayment_amount x marginal_rate`. Common: income protection insurance, professional subscriptions, rent. |
| **Materiality** | > AUD 150 tax savings |
| **Confidence** | T2 -- depends on whether prepayment is genuine and within 12-month rule |
| **Reviewer flag** | Must be paid (not just invoiced) before 30 June. Period covered must end before 30 June of next year. Cannot prepay wages or super. |
| **Output** | "Prepaying AUD [X] in [expense type] before 30 June could bring forward a deduction worth AUD [Y] in tax savings at your marginal rate." |

#### AU-OPT-4: Election -- simplified depreciation (instant asset write-off)

| Field | Detail |
|---|---|
| **Category** | Elections |
| **Trigger** | User is a small business entity AND has acquired depreciable assets |
| **Calculation** | Instant asset write-off: full deduction in the year of first use/installation for assets costing less than the applicable threshold (check current legislation -- threshold has changed frequently). Temporary full expensing may apply. `savings = (instant_writeoff - normal_depreciation_year1) x marginal_rate`. |
| **Materiality** | > AUD 200 tax savings |
| **Confidence** | T1 if asset cost and SBE status confirmed; T2 if threshold uncertain |
| **Reviewer flag** | Threshold changes frequently -- verify current year's limit. Asset must be first used or installed ready for use in the income year. Pooling rules for assets above threshold. |
| **Output** | "Your [asset] costing AUD [X] qualifies for instant asset write-off, giving you a full deduction of AUD [X] this year instead of depreciating over [Y] years. Tax saving: AUD [Z]." |

#### AU-OPT-5: Unclaimed -- private health insurance offset

| Field | Detail |
|---|---|
| **Category** | Credits/reliefs not claimed |
| **Trigger** | User has private health insurance AND income < AUD 151,000 (single) AND has not claimed the rebate |
| **Calculation** | Rebate tiers (2024-25): Base tier (<$97,000): 24.608%. Tier 1 ($97,001-$113,000): 16.405%. Tier 2 ($113,001-$151,000): 8.202%. Tier 3 (>$151,000): 0%. `savings = annual_premium x rebate_percentage`. Can be claimed as premium reduction or tax offset. |
| **Materiality** | > AUD 150 |
| **Confidence** | T1 if income tier and premium known |
| **Reviewer flag** | If claimed as premium reduction (via insurer), do not also claim as tax offset. Age-based tiers (higher rebate for 65+). Income is for surcharge purposes (includes reportable fringe benefits, super contributions). |
| **Output** | "You are entitled to a [X]% private health insurance rebate worth AUD [Y]/year. [If not claimed as premium reduction: 'Claim as a tax offset on your return.']" |

---

### 3.5 Canada (CA) -- 5 checks

#### CA-OPT-1: RRSP contribution room

| Field | Detail |
|---|---|
| **Category** | Retirement contributions |
| **Trigger** | User has unused RRSP contribution room |
| **Calculation** | RRSP limit: 18% of prior-year earned income, max CAD 32,490 (2025). Unused room carries forward indefinitely. `savings = contribution x marginal_rate`. Federal + provincial combined. At 33% combined marginal: CAD 10,000 = CAD 3,300 savings. |
| **Materiality** | > CAD 150 tax savings |
| **Confidence** | T1 if Notice of Assessment (NOA) room is known; T2 if estimated |
| **Reviewer flag** | Over-contribution penalty: 1% per month on amount > CAD 2,000 buffer. RRSP deadline: 60 days after year-end (typically Mar 1). Spousal RRSP attribution rules (3-year rule). |
| **Output** | "You have CAD [X] in unused RRSP contribution room. Contributing would save approximately CAD [Y] in combined federal and provincial tax." |

#### CA-OPT-2: Entity structure -- incorporation

| Field | Detail |
|---|---|
| **Category** | Entity structure |
| **Trigger** | Self-employed with net business income > CAD 80,000 |
| **Calculation** | Compare: (a) Sole prop: personal marginal rates (up to ~53% combined federal+provincial). (b) CCPC: small business rate ~12.2% combined (federal 9% + provincial ~3.2%, varies) on first CAD 500,000. Distribution via salary or dividends. `savings = sole_prop_tax - (corp_tax + personal_tax_on_extraction) - additional_costs`. Additional costs: incorporation (~CAD 1,000), additional accounting (~CAD 3,000-5,000/yr). |
| **Materiality** | > CAD 3,000 net annual savings |
| **Confidence** | T2 -- depends on extraction strategy and province |
| **Reviewer flag** | TOSI (Tax on Split Income) rules. PSB (Personal Services Business) risk. Integration principle: total tax should be similar long-term. Benefit is mainly tax deferral on retained earnings. CPP implications. |
| **Output** | "At your income level (CAD [X]), incorporating could allow tax deferral of approximately CAD [Y]/year on retained earnings. Reviewer: PSB and TOSI rules must be assessed." |

#### CA-OPT-3: Timing -- fiscal year-end selection

| Field | Detail |
|---|---|
| **Category** | Timing |
| **Trigger** | User is a sole proprietor considering or using an off-calendar fiscal year-end |
| **Calculation** | Sole proprietors can elect a non-calendar fiscal year-end (but must include additional business income via section 34.1 reserve). `timing_benefit` in first year only; neutralised in subsequent years. Generally not beneficial for sole props post-2017 changes. |
| **Materiality** | > CAD 200 first-year timing benefit |
| **Confidence** | T2 |
| **Reviewer flag** | Alternative method (section 249.1(4)) requires additional business income inclusion. New businesses: evaluate if calendar year-end is simpler. |
| **Output** | "Fiscal year-end planning: [analysis of whether non-calendar year-end provides any benefit]. In most cases, a December 31 year-end is simplest for sole proprietors." |

#### CA-OPT-4: Election -- CCA classes and immediate expensing

| Field | Detail |
|---|---|
| **Category** | Elections |
| **Trigger** | User has acquired depreciable property AND is a CCPC or eligible individual |
| **Calculation** | Immediate expensing: eligible persons can immediately expense up to CAD 1,500,000 per year of designated property (certain CCA classes). `savings = (immediate_deduction - normal_CCA_year1) x marginal_rate`. |
| **Materiality** | > CAD 200 tax savings |
| **Confidence** | T1 if asset and eligibility confirmed; T2 if uncertain |
| **Reviewer flag** | Immediate expensing rules: check current year availability (originally introduced 2022, extended). Not all CCA classes eligible. Half-year rule does not apply to immediately expensed property. |
| **Output** | "Your [asset] costing CAD [X] may qualify for immediate expensing, giving a full deduction this year instead of CCA over [Y] years. Tax saving: CAD [Z]." |

#### CA-OPT-5: Unclaimed -- business-use-of-home expenses

| Field | Detail |
|---|---|
| **Category** | Credits/reliefs not claimed |
| **Trigger** | User works from home AND has not claimed business-use-of-home expenses |
| **Calculation** | Proportional: (business sq ft / total sq ft) x (heat, electricity, insurance, maintenance, rent or mortgage interest, property tax). Cannot create a business loss (carry forward unused). `savings = deduction x marginal_rate`. |
| **Materiality** | > CAD 150 tax savings |
| **Confidence** | T1 if expenses and proportion known; T2 if estimated |
| **Reviewer flag** | Must be principal place of business OR used regularly and continuously for meeting clients. CCA on home not recommended (recapture risk on sale + principal residence exemption impact). Flat rate method (CAD 2/day, max CAD 500) available as alternative. |
| **Output** | "You can deduct CAD [X] in business-use-of-home expenses (based on [Y]% business use), saving approximately CAD [Z] in tax. [If flat rate is better: 'The flat rate method (CAD 2/day) gives CAD [W] -- use whichever is higher.']" |

---

### 3.6 India (IN) -- 5 checks

#### IN-OPT-1: Section 80C and NPS deductions

| Field | Detail |
|---|---|
| **Category** | Retirement / savings contributions |
| **Trigger** | User is under old tax regime AND has not maximised section 80C (INR 1.5 lakh) or section 80CCD(1B) (additional INR 50,000 for NPS) |
| **Calculation** | `savings = unused_80C_room x marginal_rate + unused_80CCD1B x marginal_rate`. At 30% rate: INR 50,000 NPS = INR 15,000 savings. Total potential: INR 2,00,000 x 30% = INR 60,000. |
| **Materiality** | > INR 10,000 tax savings |
| **Confidence** | T1 if contributions known; T2 if old vs new regime not confirmed |
| **Reviewer flag** | Only beneficial under old tax regime. New tax regime (section 115BAC) does not allow 80C/80CCD deductions (except employer NPS under 80CCD(2)). Compare old vs new regime total liability first. |
| **Output** | "Under the old tax regime, you can invest INR [X] more in [80C instruments/NPS] and save approximately INR [Y] in tax. [If new regime might be better: 'Reviewer: compare old vs new regime first.']" |

#### IN-OPT-2: Old vs new tax regime comparison

| Field | Detail |
|---|---|
| **Category** | Elections |
| **Trigger** | User has not compared old and new tax regimes |
| **Calculation** | New regime (default from AY 2024-25): lower rates, fewer deductions. Old regime: higher rates, more deductions (80C, 80D, HRA, etc.). Compute tax under both. `savings = abs(old_regime_tax - new_regime_tax)`. New regime is generally better if total deductions < ~INR 3.75 lakh. |
| **Materiality** | > INR 10,000 difference |
| **Confidence** | T1 if all deductions known; T2 if some deductions estimated |
| **Reviewer flag** | Self-employed persons can switch regime every year. Salaried persons: new regime is default, must opt out. Business income: once old regime chosen, switching back is restricted. |
| **Output** | "The [old/new] tax regime saves you INR [X] compared to the [other] regime. [Breakdown of key differences.]" |

#### IN-OPT-3: Timing -- advance tax optimisation

| Field | Detail |
|---|---|
| **Category** | Timing |
| **Trigger** | User pays advance tax AND has seasonal or variable income |
| **Calculation** | Interest under section 234C: 1% per month on shortfall if advance tax paid < required percentage per quarter (15%, 45%, 75%, 100%). Optimise quarterly payments to match actual income accrual. `savings = interest_avoided`. For presumptive taxation (44ADA): can pay entire advance tax in Q4 (by Mar 15). |
| **Materiality** | > INR 10,000 interest savings |
| **Confidence** | T2 -- depends on income projection accuracy |
| **Reviewer flag** | Section 234C interest is not a penalty -- it is mandatory interest. Presumptive taxpayers have single-instalment privilege. Capital gains: advance tax due in quarter of gain. |
| **Output** | "By aligning your advance tax payments with actual quarterly income, you can avoid approximately INR [X] in section 234C interest. [If presumptive: 'Under section 44ADA, you can pay all advance tax by March 15.']" |

#### IN-OPT-4: Entity structure -- presumptive vs regular

| Field | Detail |
|---|---|
| **Category** | Entity structure |
| **Trigger** | User is a professional with gross receipts < INR 75 lakh (digital) and actual profit margin < 50% |
| **Calculation** | Presumptive (44ADA): 50% deemed profit, no books, no audit. Regular: actual profit (could be lower than 50%). `savings = (presumptive_tax - regular_tax)` if regular is lower, but add compliance cost of regular (~INR 20,000-50,000 for bookkeeping + audit if applicable). Net comparison needed. |
| **Materiality** | > INR 10,000 difference |
| **Confidence** | T2 -- actual profit margin must be known |
| **Reviewer flag** | Once opted out of presumptive, cannot re-enter for 5 years. Audit required under section 44AB if opting out and income > basic exemption limit. |
| **Output** | "Your actual profit margin ([X]%) is [higher/lower] than the 50% presumptive rate. [If lower: 'Regular filing could save INR [Y], but adds compliance cost of approximately INR [Z] and triggers audit requirements.']" |

#### IN-OPT-5: Unclaimed -- section 80D health insurance

| Field | Detail |
|---|---|
| **Category** | Credits/reliefs not claimed |
| **Trigger** | User pays health insurance premiums AND is under old tax regime AND has not claimed section 80D |
| **Calculation** | Deduction: INR 25,000 for self/family (INR 50,000 if senior citizen). Additional INR 25,000/50,000 for parents. Preventive health check-up: INR 5,000 (within 80D limit). `savings = eligible_premium x marginal_rate`. |
| **Materiality** | > INR 10,000 tax savings |
| **Confidence** | T1 if premiums known; T2 if old regime not confirmed |
| **Reviewer flag** | Only under old tax regime. Cash payment for insurance is not eligible (except preventive check-up). Parents' premium: separate limit. |
| **Output** | "You paid INR [X] in health insurance premiums. Under section 80D, you can deduct INR [Y] and save approximately INR [Z] in tax." |

---

### 3.7 Spain (ES) -- 5 checks

#### ES-OPT-1: Plan de pensiones contribution room

| Field | Detail |
|---|---|
| **Category** | Retirement contributions |
| **Trigger** | User has not maximised pension plan (plan de pensiones) contributions |
| **Calculation** | Individual limit: EUR 1,500/year (reduced from EUR 8,000 in 2022). Employment plan (plan de empleo): additional EUR 8,500 if employer contributes. `savings = contribution x marginal_rate`. At 37% marginal: EUR 1,500 = EUR 555 savings. |
| **Materiality** | > EUR 100 tax savings |
| **Confidence** | T1 if contribution data known |
| **Reviewer flag** | Individual limit is very low (EUR 1,500) -- savings are modest. Autónomo plans de pensiones de empleo simplificados (PPES): additional EUR 4,250 for self-employed since 2023. Combined limit: EUR 5,750 for autónomos. |
| **Output** | "You can contribute EUR [X] more to your plan de pensiones [and PPES if autónomo] and save approximately EUR [Y] in IRPF." |

#### ES-OPT-2: Entity structure -- Sociedad Limitada vs autónomo

| Field | Detail |
|---|---|
| **Category** | Entity structure |
| **Trigger** | Autónomo with net income > EUR 60,000 |
| **Calculation** | Compare: (a) Autónomo: IRPF at marginal rates (up to 47% + regional surcharge) + RETA contributions (~EUR 300-530/month depending on income). (b) SL: Impuesto de Sociedades 25% (15% for first 2 years on first EUR 300,000). Distribution via dividends taxed at 19-28%. Salary: IRPF + social security. `net_savings = autonomo_total - sl_total - additional_costs`. Additional costs: formation (~EUR 600-1,500), accounting (~EUR 2,000-4,000/yr), Registro Mercantil. |
| **Materiality** | > EUR 2,000 net annual savings |
| **Confidence** | T2 -- depends on salary/dividend mix and RETA vs Regimen General |
| **Reviewer flag** | Sociedad limitada unipersonal (SLU) requires "SLU" on all documents. Capital requirement: EUR 1 (since Ley Crea y Crece 2022, but EUR 3,000 recommended). Administrador salary may be mandatory. 15% IRPF withholding on professional invoices lost. |
| **Output** | "At your income level (EUR [X]), operating through an SL could save approximately EUR [Y]/year. Reviewer: salary/dividend extraction strategy and RETA implications required." |

#### ES-OPT-3: Timing -- Modelo 130 offset planning

| Field | Detail |
|---|---|
| **Category** | Timing |
| **Trigger** | User files quarterly Modelo 130 AND has seasonal income |
| **Calculation** | Modelo 130 uses cumulative method: 20% of cumulative net income minus prior payments. If Q4 income is low, Q4 payment may be negative (refund of overpaid). Plan expense timing to accelerate deductions into high-income quarters. `timing_benefit = tax_deferred x time_value`. |
| **Materiality** | > EUR 200 timing benefit |
| **Confidence** | T2 |
| **Reviewer flag** | Modelo 130 is cumulative -- timing within the year affects cash flow, not final liability (Modelo 100 settles up). Benefit is cash flow, not permanent savings. |
| **Output** | "By timing deductible expenses into Q[X], you can reduce your Modelo 130 payment by EUR [Y] this quarter, improving cash flow." |

#### ES-OPT-4: Election -- RETA contribution base optimisation

| Field | Detail |
|---|---|
| **Category** | Elections |
| **Trigger** | User is autónomo under the new cuota system (since Jan 2023) |
| **Calculation** | New system: RETA contributions based on declared net income tranche. Underdeclaring triggers regularisation. Overdeclaring: higher RETA but better future pension. Compare actual income vs declared tranche. `over/underpayment = (declared_tranche_contribution - correct_tranche_contribution) x 12`. |
| **Materiality** | > EUR 200 annual difference |
| **Confidence** | T2 -- depends on income projection and tranche boundaries |
| **Reviewer flag** | Annual regularisation in October of following year. Declaring too low: surcharge. Declaring too high: higher contributions but better pension rights. Six-month adjustment windows. |
| **Output** | "Your current RETA tranche implies net income of EUR [X]-[Y], but your actual projected income is EUR [Z]. [If mismatch: 'Adjusting your tranche could save/cost EUR [W]/year in contributions.']" |

#### ES-OPT-5: Unclaimed -- gastos de dificil justificacion (5% deduction)

| Field | Detail |
|---|---|
| **Category** | Credits/reliefs not claimed |
| **Trigger** | User is under estimacion directa simplificada AND has not claimed the 5% deduction |
| **Calculation** | 5% of net income (rendimiento neto previo - gastos deducibles), max EUR 2,000/year. `savings = min(net_income x 5%, 2000) x marginal_rate`. At 37% marginal: EUR 2,000 = EUR 740 savings. |
| **Materiality** | > EUR 100 tax savings |
| **Confidence** | T1 -- automatic for simplified method |
| **Reviewer flag** | Only available under estimacion directa simplificada (not normal). Should be automatically applied but verify it is included. Incompatible with estimacion objetiva (modulos). |
| **Output** | "The 5% deduction for hard-to-justify expenses (gastos de dificil justificacion) gives you EUR [X] in additional deductions, saving EUR [Y] in IRPF. [If not claimed: 'This appears to be missing from your computation.']" |

---

### 3.8 Malta (MT) -- 5 checks

#### MT-OPT-1: Voluntary pension contribution

| Field | Detail |
|---|---|
| **Category** | Retirement contributions |
| **Trigger** | User has not maximised voluntary occupational pension or personal retirement scheme contributions |
| **Calculation** | Tax credit: 25% of contributions, max credit EUR 750/year (i.e., contributions up to EUR 3,000). `savings = min(contribution, 3000) x 25%`. Not a deduction -- it is a credit against tax. |
| **Materiality** | > EUR 100 tax credit |
| **Confidence** | T1 if contribution known |
| **Reviewer flag** | Must be an approved scheme (MFSA regulated). Credit is non-refundable -- cannot reduce tax below zero. Check if already claimed via employer scheme. |
| **Output** | "Contributing EUR [X] to an approved pension scheme would give you a tax credit of EUR [Y] (25% of contribution, max EUR 750)." |

#### MT-OPT-2: Entity structure -- company + shareholder refund

| Field | Detail |
|---|---|
| **Category** | Entity structure |
| **Trigger** | Self-employed with net income > EUR 35,000 |
| **Calculation** | Malta imputation system: company pays 35% tax. On dividend distribution, shareholder claims 6/7ths refund (for trading income) = effective 5% corporate rate. Personal tax on net dividend at marginal rates with tax credit. Complex interaction. `savings = self_employed_tax - (effective_corp_tax + personal_tax_on_dividend) - additional_costs`. Additional costs: company formation (~EUR 1,500), audit requirement (statutory for all Ltd), accounting (~EUR 3,000-5,000/yr). |
| **Materiality** | > EUR 2,000 net annual savings |
| **Confidence** | T2 -- depends on whether refund system applies (primarily non-resident shareholders; resident shareholders get partial refund or credit) |
| **Reviewer flag** | The 6/7ths refund is primarily beneficial for non-resident shareholders. Resident Maltese shareholders: partial refund may apply but interaction with personal tax is complex. Substance requirements. Anti-avoidance (GAAR). Company must be a Malta tax-resident trading company. Audit requirement for all Malta companies. |
| **Output** | "At your income level (EUR [X]), operating through a Malta company could reduce your effective tax rate. Reviewer: the refund system's benefit depends heavily on residency status and must be modelled in detail." |

#### MT-OPT-3: Timing -- provisional tax alignment

| Field | Detail |
|---|---|
| **Category** | Timing |
| **Trigger** | User pays provisional tax AND current-year income differs significantly from prior year |
| **Calculation** | Provisional tax is based on prior-year liability (20% Apr, 30% Aug, 50% Dec). If current-year income is lower, can apply to CfR to reduce provisional tax. `cash_flow_benefit = (prior_year_based_PT - estimated_current_year_PT)`. |
| **Materiality** | > EUR 200 cash flow benefit |
| **Confidence** | T2 -- depends on income estimate accuracy |
| **Reviewer flag** | If provisional tax reduced and actual liability is higher, interest applies on underpayment. Conservative approach: reduce only with high confidence. Application to Commissioner for Revenue. |
| **Output** | "Your provisional tax payments are based on last year's income (EUR [X]). If this year's income is significantly lower, you can apply to reduce provisional tax and free up EUR [Y] in cash flow. Reviewer: confirm income projection." |

#### MT-OPT-4: Election -- Article 11 vs Article 10 VAT

| Field | Detail |
|---|---|
| **Category** | Elections |
| **Trigger** | User is near the EUR 35,000 Article 11 threshold OR is Article 11 exempt with significant input VAT |
| **Calculation** | Compare: (a) Article 11: no VAT charged, no input VAT recovered, annual declaration only. (b) Article 10: charge 18% VAT, recover input VAT, quarterly VAT3 returns. `net_benefit = input_vat_recoverable - admin_cost`. If primarily B2B: Article 10 is usually neutral (clients recover VAT). |
| **Materiality** | > EUR 200 annual net benefit |
| **Confidence** | T2 -- depends on client mix and input VAT |
| **Reviewer flag** | Voluntary Article 10 registration is available even below threshold. Once registered, minimum 3-year period. B2C pricing: VAT adds 18% to price. EU supply implications: Article 10 needed for B2B reverse-charge mechanism. |
| **Output** | "You are currently under Article [10/11]. [If Article 11 with high input VAT: 'You are forgoing EUR [X] in recoverable input VAT. Voluntary Article 10 registration would recover this at the cost of quarterly VAT returns.']" |

#### MT-OPT-5: Unclaimed -- deductions against self-employment income

| Field | Detail |
|---|---|
| **Category** | Credits/reliefs not claimed |
| **Trigger** | User has self-employment income AND has not claimed all allowable deductions |
| **Calculation** | Common unclaimed deductions: (a) Capital allowances (wear and tear): 20% on computer equipment, 15% on furniture, 10% on A/C. (b) Home office proportion of rent/utilities. (c) Professional development and training. (d) Bad debts (if accruals basis). `savings = unclaimed_deduction x marginal_rate`. At 35%: EUR 1,000 unclaimed = EUR 350. |
| **Materiality** | > EUR 100 tax savings |
| **Confidence** | T1 if expenses known; T2 if estimated |
| **Reviewer flag** | Capital allowances: ITA Schedule 6 rates. Home office: must be used exclusively for business (CfR practice). Private use portion not deductible. Depreciation vs capital allowances: Malta uses capital allowances (not accounting depreciation) for tax. |
| **Output** | "You may have unclaimed deductions of EUR [X], including: [list items]. This would reduce your tax by approximately EUR [Y]. Reviewer: verify exclusivity of business use for home office claim." |

---

## Section 4 -- Materiality thresholds

Do not surface an optimisation if the estimated annual tax saving is below the following floor:

| Currency | Floor |
|---|---|
| EUR | 100 |
| USD | 100 |
| GBP | 100 |
| AUD | 150 |
| CAD | 150 |
| INR | 10,000 |

If estimated savings fall below the floor, suppress the suggestion unless the user explicitly asks "show me everything."

---

## Section 5 -- Output format

### Part A -- Savings summary

```
| # | Jurisdiction | Check | Category | Estimated saving | Confidence | Priority |
|---|---|---|---|---|---|---|
| 1 | US | Retirement contribution room | Retirement | $9,600 | T1 | HIGH |
| 2 | UK | Pension contribution (PA taper band) | Retirement | GBP 6,000 | T1 | HIGH |
| 3 | US | S-Corp election | Entity structure | $8,200 | T2 | MEDIUM |
| ... | | | | | | |
```

Priority: HIGH (> 5x materiality floor), MEDIUM (2-5x floor), LOW (1-2x floor).

### Part B -- Detailed recommendations (top 5 by savings)

For each:

```
### [Check name] -- [Jurisdiction] -- [Estimated saving]

**What:** [One-sentence description]
**Your situation:** [Current position based on user data]
**Opportunity:** [What can be done]
**Calculation:** [Step-by-step formula with user's numbers]
**Action required:** [Specific next steps]
**Deadline:** [When this must be done by, if time-sensitive]
**Confidence:** [T1/T2] -- [Basis]
**Reviewer note:** [What the reviewer must verify]
```

### Part C -- Suppressed checks

List checks that were not triggered or fell below materiality, so the reviewer knows they were considered.

### Part D -- Caveats

- All savings are estimates based on current data
- Interaction effects: some optimisations affect others (e.g., retirement contributions reduce QBI income, which may reduce QBI deduction)
- No aggressive or novel positions are suggested
- The reviewer must validate all suggestions before implementation

---

## Section 6 -- Self-checks

Before delivering output, verify:

- [ ] User's jurisdiction is confirmed, not assumed
- [ ] All 5 checks for each applicable jurisdiction were evaluated
- [ ] Trigger conditions were checked against actual user data
- [ ] Calculations use the user's actual figures, not hypothetical amounts
- [ ] Materiality filter applied -- sub-threshold items suppressed
- [ ] Confidence tiers (T1/T2) are correctly assigned
- [ ] Interaction effects between optimisations are noted
- [ ] Every suggestion is addressed to the reviewer, not the taxpayer
- [ ] No aggressive positions, tax shelters, or GAAR-triggering schemes are suggested
- [ ] Savings estimates are conservative (better to understate than overstate)
- [ ] Output uses the format from Section 5
- [ ] Disclaimer is included
