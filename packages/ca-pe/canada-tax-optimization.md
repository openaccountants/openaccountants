---
name: canada-tax-optimization
description: Use this skill when advising on LEGAL tax minimization strategies for Canadian taxpayers — individuals, sole proprietors, and small business owners (CCPCs). Trigger on phrases like "reduce my tax Canada", "tax planning", "RRSP vs TFSA", "salary vs dividends", "income splitting", "TOSI", "small business deduction", "LCGE", "capital gains inclusion", "CRA", or any question about structuring affairs to legally minimize Canadian tax. Covers entity selection, registered account optimization, deduction strategies, loss utilization, timing, GST/HST planning, CPP optimization, and red lines. ALWAYS read this skill before giving Canadian tax optimization advice.
version: 1.0
jurisdiction: CA
tax_year: 2026
last_updated: 2026-07-13
reviewed_by: Edgar Lautsyus
review_status: current
depends_on: - bookkeeping-workflow-base
category: tax-optimization
tier: 1
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Canada Tax Optimization

## Canada — Tax Optimization Skill v1.0

## Verified rates & thresholds (accountant-reviewed)

Reviewed against the cited tax authorities by **Nathan Wiebe** on 2026-06-21.
Items flagged for further clarification are tracked separately and excluded here.
This block is generated from verified `skill_facts` — edit the facts, not the prose.

### Tax Optimization

- **$0–$58,523** — 14%  _(CRA 2026 indexed brackets; Bill C-4 (lowest rate 14% from 2026))_
- **$58,524–$117,045** — 20.5%  _(CRA 2026 indexed brackets (T4032))_
- **$117,046–$181,440** — 26%  _(CRA 2026 payroll deductions tables (T4032); KPMG Tax Data Sheet 2026)_
- **$181,441–$258,482** — 29%  _(CRA 2026 payroll deductions tables (T4032); KPMG Tax Data Sheet 2026)_
- **$258,483+** — 33%  _(CRA 2026 payroll deductions tables (T4032))_
- **Small business rate (federal)** — 9% on first $500,000 active business income  _(ITA s.125; CRA — Corporate income tax rates)_
- **General corporate rate (federal)** — 15%  _(ITA s.123(1); CRA — Corporate income tax rates)_
- **Capital gains inclusion** — 50% (66.7% increase was cancelled)  _(PM Carney announcement Mar 21, 2025; Budget 2025; CRA — canada.ca)_
- **RRSP** — $33,810 (or 18% of prior-year earned income)  _(CRA — RRSP — canada.ca; ITA s.146(1))_
- **TFSA** — $7,000 (cumulative $109,000 since 2009)  _(CRA — TFSA — canada.ca; ITA s.207.01)_
- **FHSA** — $8,000/year ($40,000 lifetime)  _(ITA s.146.6; CRA — FHSA — canada.ca)_
- **RESP CESG** — $2,500/year to maximise $500 grant  _(ITA s.146.1; Canada Education Savings Act)_
- **Class 1** — 4% — Buildings  _(ITR Schedule II Class 1)_
- **Class 8** — 20% — Furniture, equipment  _(ITR Schedule II Class 8)_
- **Class 10** — 30% — Motor vehicles (Class 10.1 threshold $38,000 before tax for vehicles acquired on or after 1 Jan 2025)  _(Dept. of Finance — 2025 Automobile Deduction Limits (Jan 2025); CRA — Classes of depreciable property)_
- **Class 10.1** — 30% — Passenger vehicles over cost limit  _(ITR Schedule II Class 10.1; CRA — classes of depreciable property)_
- **Class 12** — 100% — Computer software, tools <$500  _(ITR Schedule II Class 12)_
- **Class 50** — 55% — Computer hardware  _(ITR Schedule II Class 50)_
- **Class 54** — Class 54 is NOT '0% (expensed)' — the rate is 30% declining balance for zero-emission passenger vehicles, with enhanced first-year deductions under AIIP/RIIP rules. The $61,000 cost cap is correct. The skill's '0% (expensed)' description is misleading.  _(ITR Schedule II Class 54; CRA — classes of depreciable property — canada.ca)_
- **Child care** — $8,000/child under 7; $5,000/child 7–16  _(ITA s.63(3))_
- **Medical expenses** — Medical expense credit rate for 2025 is 15% (NRTC). Threshold: amounts over the lesser of 3% of net income or $2,834(threshold for 2025)  _(ITA s.118.2; CRA — Medical expenses — canada.ca; Bill C-4 (14.5% credit rate for 2025))_
- **Moving expenses** — Must move ≥ 40 km closer to new work location  _(ITA s.62)_
- **LCGE (QSBC shares)** — $1,250,000  _(ITA s.110.6(2); Budget 2024; CRA — LCGE — canada.ca)_
- **GAAR** — ITA s.245  _(ITA s.245)_
- **TOSI** — ITA s.120.4 — top rate on split income to family members  _(ITA s.120.4)_
- **Superficial loss** — Repurchase within 30 days — loss denied  _(ITA s.54; ITA s.40(2)(g))_

## Section 1 — Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Canada |
| Currency | CAD |
| Tax year | Calendar year (1 January – 31 December) |
| Primary legislation | Income Tax Act (R.S.C., 1985, c. 1 (5th Supp.)) |
| Anti-avoidance | GAAR (s 245 ITA); TOSI (s 120.4) |
| Tax authority | Canada Revenue Agency (CRA) |
| Filing deadline | 30 April (employees); 15 June (self-employed, but tax owing still due 30 April) |
| Individual top federal rate | 33% (on income >$258,482) |
| Combined top rate (varies by province) | ~50–54% |
| CCPC small business rate (federal) | 9% on first $500,000 active business income |
| General corporate rate (federal) | 15% |
| Capital gains inclusion rate | 50% (66.7% increase was cancelled) |
| GST rate | 5% (HST varies by province: 13%–15%) |

### Federal Tax Brackets (2026)

**Federal Tax Brackets (2026)**

| Taxable Income (CAD) | Rate |
| --- | --- |
| 0 – 57,375 | 14% |
| 57,376 – 114,750 | 20.5% |
| 117,045 – 181,440 | 26% |
| 181,440 – 258,482 | 29% |
| 258,482+ | 33% |

Note: The lowest bracket rate was reduced to 14% (from 15%) effective 2026 via Bill C-4.

## Section 2 — Income Splitting & Structuring

### Sole Proprietor vs CCPC

- **Sole proprietor** — All business income taxed at personal marginal rates. Simple, low compliance cost. Business losses offset personal income. No payroll remittances (except CPP).
- **Canadian-Controlled Private Corporation (CCPC)** — First $500,000 of active business income taxed at 9% federal (+ provincial, typically 2–4% = ~11–13% combined). Profits retained at corporate rate; extracted via salary or dividends. Integration principle: in theory, combined corporate + personal tax approximates personal tax alone. In practice, small gaps create planning opportunities.
- **When to incorporate** — Generally beneficial when annual business profit consistently exceeds ~$70,000–$80,000 and the owner can leave profits in the corporation. Below that, sole proprietorship is simpler and equally tax-efficient.

### Salary vs Dividends (CCPC Owner-Manager)

**Salary vs Dividends (CCPC Owner-Manager)**

| Factor | Salary | Dividends |
| --- | --- | --- |
| Corporate deduction | Yes | No |
| CPP contributions | Yes (creates room) | No |
| RRSP room created | Yes (18% of earned income) | No |
| Childcare expense room | Yes | No |
| Personal tax treatment | Marginal rates | Gross-up + dividend tax credit |
| Payroll admin | Required (T4, remittances) | Minimal (T5) |

- **Optimal mix** — Pay enough salary to maximise RRSP room ($33,810 limit for 2026 → requires ~$187,833 salary). If RRSP room is not needed, eligible dividends may produce slightly lower combined tax. Model annually — provincial rates create different break-even points.

### TOSI (Tax on Split Income) — s 120.4

- **TOSI** — Income paid to family members (spouse, children) from a related business is subject to top marginal tax rate unless an exclusion applies.  _(s 120.4)_
- **Excluded business** — Family member works ≥20 hours/week in the business  _(s 120.4)_
- **Excluded shares** — Family member aged 25+, owns shares of a corporation where <90% of income is from services, 10%+ equity  _(s 120.4)_
- **Reasonable return** — Compensation proportional to labour, capital, risk contributed  _(s 120.4)_
- **Prescribed rate loans** — Lend funds to spouse at CRA prescribed rate (3% Q1 2026); spouse invests, attributes interest income back to lender, keeps excess returns  _(s 120.4)_

## Section 3 — Deductions Most People Miss

**Deductions Most People Miss**

| Deduction | Provision | Notes |
| --- | --- | --- |
| Home office expenses | s 8(1)(f), 8(1)(i), 18(12) | Employees: T2200 required. Self-employed: proportion of rent/mortgage interest, utilities, insurance, property tax |
| Moving expenses | s 62 | Must move ≥40 km closer to new work/business location. Deduct against income at new location |
| Carrying charges | s 20(1)(c) | Interest on money borrowed to earn investment income. Includes investment counsel fees |
| Medical expenses | s 118.2 | Tax credit at 15% federal on expenses >3% of net income or $2,834 (lesser, 2025 threshold). Include premiums, dental, prescriptions, travel for treatment |
| Disability tax credit | s 118.3 | $9,872 federal credit (2026). Transferable to supporting person. Unlocks RDSP eligibility |
| Northern residents deduction | s 110.7 | Residency deduction + travel benefits for prescribed zones |
| Capital cost allowance (CCA) on rental property | s 20(1)(a), Sch II | Class 1 (4%), Class 8 (20%). Accelerated Investment Incentive (triple declining balance in year 1) |
| Apprentice mechanic tools | s 8(1)(s) | Cost exceeding $1,368 (2026 indexed) |
| Union/professional dues | s 8(1)(i) | Full deduction |
| Child care expenses | s 63 | $8,000/child under 7; $5,000/child 7–16. Must be claimed by lower-income spouse (exceptions apply) |

## Section 4 — Capital Allowances Optimization

### Accelerated Investment Incentive (AII)

- **AII** — For assets acquired after 20 November 2018 and available for use before 2028: enhanced first-year CCA. Effectively 1.5× the normal CCA rate in Year 1 (eliminates the half-year rule and adds a 50% bonus). Applies to most CCA classes.

### Key CCA Classes

**Key CCA Classes**

| Class | Rate | Assets |
| --- | --- | --- |
| 1 | 4% | Buildings acquired after 1987 |
| 8 | 20% | Furniture, fixtures, equipment, machinery |
| 10 | 30% | Motor vehicles (passenger vehicle Class 10.1 threshold $38,000 before tax for 2025 acquisitions) |
| 10.1 | 30% | Passenger vehicles over cost limit (separate class per vehicle) |
| 12 | 100% | Computer software, tools <$500 |
| 50 | 55% | Computer hardware and systems software |
| 54 | 30% (declining balance, enhanced first-year deductions under AIIP/RIIP) | Zero-emission vehicles up to $61,000 + tax |

### Immediate Expensing (CCPCs)

- **Immediate expensing** — CCPCs can immediately expense up to $1.5 million per year of eligible property (Classes 2–6, 8, 10, 12, etc.) acquired after 18 April 2021 and available for use before 2025 — verify ongoing extensions.

## Section 5 — Loss Utilization

### Non-Capital Losses

- **Non-capital losses** — Carry back 3 years or carry forward 20 years (s 111(1)(a)). Business losses of a sole proprietor offset all personal income in the current year. Corporate losses stay in the corporation.  _(s 111(1)(a))_

### Capital Losses

- **Capital losses** — Net capital losses carry back 3 years or forward indefinitely (s 111(1)(b)). Can only offset capital gains. At death, net capital losses can offset any income in the year of death and prior year.  _(s 111(1)(b))_

### Allowable Business Investment Losses (ABIL)

- **ABIL** — Loss on shares or debt of a small business corporation (s 38(c)). 50% of the loss is an ABIL, deductible against all income (not just capital gains). Excess becomes a non-capital loss.  _(s 38(c))_

### Loss Planning

- **Time capital gains and losses** — Time capital gains and losses in the same year to offset
- **Crystallise unrealised losses** — Crystallise unrealised losses before year-end (beware superficial loss rule: 30-day rule, s 54)  _(s 54)_
- **Spousal transfer** — Consider transferring losing investments to a spouse at FMV to trigger loss (but attribution rules may apply)

## Section 6 — Timing Strategies

**Timing Strategies**

| Strategy | Detail |
| --- | --- |
| RRSP contribution by March 1 | Contributions made by 1 March deductible in prior tax year. Carry forward deduction if in lower bracket now |
| Defer income | Self-employed: delay invoicing past 31 December. Employees: defer bonuses to January |
| Accelerate deductions | Prepay deductible expenses before 31 December. Purchase CCA-eligible assets before year-end |
| Charitable donations | Carry forward donations up to 5 years. Consolidate to one spouse for higher credit rate (29%/33% on amounts >$200) |
| Capital gains deferral | Hold assets >1 year (no discount, but defer realisation). Use CCPC to shelter passive income until extraction |
| LCGE crystallisation | Trigger capital gain on QSBC shares up to $1,250,000 LCGE while still eligible. Useful before selling active business |
| Prescribed rate loan before rate increase | Lock in lower CRA prescribed rate before quarterly adjustments |

## Section 7 — GST/HST Optimization

**GST/HST Optimization**

| Topic | Detail |
| --- | --- |
| Small supplier exemption | Gross revenue ≤$30,000 in 4 consecutive quarters → no mandatory registration. But voluntary registration allows ITCs |
| Quick method | Simplified GST remittance for businesses ≤$400,000 revenue. Remit a reduced percentage; keep the difference. Often advantageous for service businesses with few inputs |
| Input Tax Credits (ITCs) | Claim GST/HST on business purchases. Documentation requirements: supplier name/BN, invoice date, total, GST amount |
| ITCs on vehicles | Claim proportional to business use. Maintain logbook |
| Real property | Self-supply rules on real property conversions. New residential property GST/HST rebate ($350,000–$450,000 threshold) |
| Place of supply | GST vs HST depends on province of delivery. Optimise for lower-rate provinces where legitimately possible |
| Zero-rated exports | Exports are zero-rated (0% GST) but ITCs on inputs still claimable |

## Section 8 — CPP/EI & Social Security Optimization

### CPP Contributions (2026)

- **CPP1** — 5.95% employee + 5.95% employer on pensionable earnings $3,500–$73,200 (max employee contribution ~$4,147)
- **CPP2** — 4% employee + 4% employer on earnings $73,200–$81,200 (second ceiling)
- **Self-employed CPP** — Self-employed pay both halves (11.9% CPP1 + 8% CPP2)
- **CCPC owner-manager dividends only** — No CPP contributions → no CPP pension accrual. Trade-off: lower current cost vs lower retirement benefit

### EI Premiums

- **Employees** — 1.64% on insurable earnings up to $65,700 (2026)
- **Self-employed** — Can opt in for special benefits (maternity, sickness)
- **CCPC dividends** — No EI — but also no EI eligibility

### Optimisation

- **Dividends avoid premiums** — If owner-manager does not need CPP/EI benefits, dividends avoid these premiums (~$6,000+ annual saving)
- **Building CPP entitlement** — If building CPP entitlement, pay minimum salary to maximise CPP credits
- **RRSP room balance** — Balance against RRSP room generation (requires earned income)

## Section 9 — Investment & Retirement

**Investment & Retirement**

| Account | 2026 Limit | Tax Treatment |
| --- | --- | --- |
| RRSP | $33,810 (or 18% of prior-year earned income) | Contributions deductible; growth tax-deferred; withdrawals taxed as income |
| TFSA | $7,000 (cumulative $109,000 since 2009) | No deduction; growth and withdrawals tax-free |
| FHSA | $8,000/year ($40,000 lifetime) | Deductible like RRSP + tax-free withdrawal for first home (like TFSA). Best of both worlds |
| RESP | $2,500/year to maximise CESG ($500 grant) | No deduction; growth tax-deferred; grants from government; withdrawals taxed to student |
| RDSP | Up to $200,000 lifetime | Government grants/bonds up to $3,500/year. Must have DTC |

### Strategy Framework

- **1. FHSA first** — If qualifying first-time buyer — deductible AND tax-free withdrawal
- **2. Employer RRSP match** — Capture free money before any other investment
- **3. TFSA** — Fill annually, especially if in a lower bracket now (preserve RRSP room for higher-income years)
- **4. RRSP** — Maximise in years with high marginal rate, plan to withdraw in lower-rate retirement
- **5. RESP** — Trigger CESG grant ($500/child/year)
- **6. Non-registered** — Use Canadian eligible dividends and capital gains (50% inclusion) for tax efficiency

## Section 10 — Red Lines (GAAR & Scrutiny Triggers)

### GAAR (s 245 ITA)

- **GAAR test** — Applies when a transaction (i) results in a tax benefit, (ii) is an avoidance transaction (not primarily for bona fide non-tax purposes), and (iii) is abusive — misuses or frustrates the provisions of the Act. Consequence: tax benefit denied; potential penalties.  _(s 245 ITA)_

### CRA Scrutiny Triggers

**CRA Scrutiny Triggers**

| Trigger | Risk |
| --- | --- |
| TOSI-offending dividends to family members | Top-rate tax + interest |
| Superficial losses (repurchase within 30 days) | Loss denied (s 54) |
| Excessive salary to family members not working in business | TOSI + reasonableness challenge |
| Personal expenses through corporation | Shareholder benefit (s 15(1)) or deemed dividend (s 15(2)) |
| Automobile benefits | Standby charge + operating benefit if personal use not properly reported |
| Non-arm's length transactions at non-FMV | Transfer pricing rules (s 69, s 247) |
| Foreign reporting non-compliance | T1135 (≥$100,000 foreign property). Penalties: $2,500/year late filing |
| Underground economy / unreported income | CRA uses third-party data matching |
| RRSP over-contribution | 1% per month penalty tax on excess >$2,000 |
| Aggressive tax shelters | CRA mandatory disclosure rules (s 237.3, 237.4) — expanded 2023 |

### Absolute Prohibitions

- **Personal expenses as business deductions** — NEVER advise claiming personal expenses as business deductions
- **Hiding income/assets offshore** — NEVER advise hiding income or assets offshore without proper disclosure (T1135, T1134)
- **Ignoring TOSI** — NEVER advise ignoring TOSI rules when splitting income with family members
- **Superficial loss repurchase** — NEVER advise repurchasing securities within 30 days to trigger a loss (superficial loss)
- **Backdating documents** — NEVER advise backdating transactions or documentation

## Section 11 — Annual Tax Planning Calendar

**Annual Tax Planning Calendar**

| When | Action |
| --- | --- |
| January | New TFSA room available ($7,000). Review prescribed rate for spousal loans. Ensure FHSA contribution on track |
| February | Final month for prior-year RRSP contribution (deadline 1 March). Model optimal RRSP vs TFSA split |
| March 1 | RRSP contribution deadline for prior-year deduction |
| April 30 | Personal tax return filing deadline. Tax balance owing due. CPP/EI self-employed remittance due |
| June 15 | Filing deadline for self-employed (but tax was due April 30) |
| June 30 | CCPC fiscal year-end (if elected). Review salary vs dividend mix |
| September | Model year-end tax position. Review quarterly instalment obligations |
| October–November | Execute capital gains/loss harvesting. Make charitable donations. Prepay deductible expenses |
| December 31 | **Critical date.** TFSA contributions. RESP contributions to trigger CESG. SRS/RRSP contributions for current year. Year-end trust distributions. Ensure T5013 / T3 slips timing. Pay salary/bonus before year-end for earned income |

## Section 12 — Cash Impact Examples

### Example 1 — CCPC Salary vs Dividend Mix (Ontario, 2026)

**Scenario:** CCPC earns $200,000 active business income. Owner is sole shareholder.

**All salary ($200,000):** Corporate tax $0 (fully deductible). Personal tax ~$52,700 (Ontario combined). CPP: ~$8,300. RRSP room created: $33,810. **Net after tax: ~$138,000.**

**All eligible dividends:** Corporate tax at ~12.2% = $24,400. Remaining $175,600 as dividends. Personal tax on grossed-up dividends ~$25,200. No CPP. No RRSP room. **Net after tax: ~$150,400. Saving: ~$12,400** but no CPP accrual or RRSP room.

**Optimal blend:** $100,000 salary + remainder as dividend. Balance of RRSP room, CPP accrual, and tax efficiency.

### Example 2 — TFSA vs RRSP

**Profile:** 30-year-old earning $60,000 (20.5% federal bracket).

**RRSP $7,000:** tax refund ~$1,435 (20.5%). Invested for 30 years at 6% → $40,159 (pre-tax). Withdrawal at 14% bracket → $34,537 net. **Advantage: $8,102 vs taxable.**

**TFSA $7,000:** no refund. Same growth → $40,159. Withdrawal tax-free = $40,159 net. **Advantage: $5,622 more than RRSP if future bracket is similar.**

### Example 3 — LCGE on Business Sale

Owner sells qualifying small business corporation shares. Capital gain: $1,000,000. LCGE shelters the full gain (within $1,250,000 lifetime limit). Tax at 50% inclusion × 33% rate = $165,000 avoided. **Cash saving: $165,000.**

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, CA, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is
different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your
jurisdiction — **no liability on either side until you and the accountant sign
a formal engagement letter** — book a free 30-minute call:

**→ [Book a call](https://calendly.com/openaccountants-info/30min)**

We'll route you to the named verifier covering your country or state. You can
also see the full list of verified accountants at
[openaccountants.com/network](https://openaccountants.com/network).

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
