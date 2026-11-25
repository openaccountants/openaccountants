---
name: canada-tax-optimization
description: Use this skill when advising on LEGAL tax minimization strategies for Canadian taxpayers — individuals, sole proprietors, and small business owners (CCPCs). Trigger on phrases like "reduce my tax Canada", "tax planning", "RRSP vs TFSA", "salary vs dividends", "income splitting", "TOSI", "small business deduction", "LCGE", "capital gains inclusion", "CRA", or any question about structuring affairs to legally minimize Canadian tax. Covers entity selection, registered account optimization, deduction strategies, loss utilization, timing, GST/HST planning, CPP optimization, and red lines. ALWAYS read this skill before giving Canadian tax optimization advice.
version: 1.1
jurisdiction: CA
tax_year: 2026
last_updated: 2026-11-25
source_checked: 2026-11-21
depends_on:
  - bookkeeping-workflow-base
category: tax-optimization
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
reviewed_by: "Nathan Wiebe"
reviewed_on: 2026-11-03
tier: 1
domain: tax-optimization
---

# Canada Tax Optimization

## Canada — Tax Optimization Skill v1.1

This is a 2026 planning workpaper. **HOLD** means that the affected recommendation or saving must not be used until its stated conditions and inputs are resolved. It does not mean zero tax or an automatic disallowance. No universal optimal strategy or personal filing result is certified.

## Rates and thresholds

Reviewed against the cited tax authorities by **Nathan Wiebe** on 2026-06-21.
The historical attribution above is preserved; it does not approve this proposed correction. Unresolved planning and calculation conditions remain non-usable holds.

### Tax Optimization

- **$0–$58,523** — 14%  _(CRA 2026 indexed brackets; Bill C-4 (lowest rate 14% from 2026))_
- **$58,524–$117,045** — 20.5%  _(CRA 2026 indexed brackets (T4032))_
- **$117,046–$181,440** — 26%  _([CRA 2026 payroll deductions tables](https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/t4032-payroll-deductions-tables/t4032on-jan/t4032on-january-general-information.html))_
- **$181,441–$258,482** — 29%  _([CRA 2026 payroll deductions tables](https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/t4032-payroll-deductions-tables/t4032on-jan/t4032on-january-general-information.html))_
- **$258,483+** — 33%  _(CRA 2026 payroll deductions tables (T4032))_
- **Small business rate (federal)** — 9% on first $500,000 active business income  _(ITA s.125; CRA — Corporate income tax rates)_
- **General corporate rate (federal)** — 15%  _(ITA s.123(1); CRA — Corporate income tax rates)_
- **Capital gains inclusion** — 50% (66.7% increase was cancelled)  _(PM Carney announcement Mar 21, 2025; Budget 2025; CRA — canada.ca)_
- **RRSP** — $33,810 (or 18% of prior-year earned income)  _(CRA — RRSP — canada.ca; ITA s.146(1))_ **HOLD:** The ceiling is not a free choice versus 18% or the total accumulated room; apply lesser-of, carryforward and pension adjustments. [Official source](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/rrsps-related-plans/contributing-a-rrsp-prpp/contributions-affect-your-rrsp-prpp-deduction-limit.html)
- **TFSA** — $7,000 (cumulative $109,000 since 2009)  _(CRA — TFSA — canada.ca; ITA s.207.01)_ **HOLD:** The cumulative annual total assumes eligibility in every relevant year and is not everyone's remaining room. [Official source](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/tax-free-savings-account/contributing/before.html)
- **FHSA** — $8,000/year ($40,000 lifetime)  _(ITA s.146.6; CRA — FHSA — canada.ca)_ **HOLD:** Annual participation depends on carryforward/adjustments; qualifying-withdrawal and deduction conditions remain unresolved. [Official source](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/first-home-savings-account/contributing-your-fhsa.html)
- **RESP CESG** — $2,500/year to maximise $500 grant  _(ITA s.146.1; Canada Education Savings Act)_ **HOLD:** The $2,500/$500 figures describe the ordinary basic grant, not an annual RESP ceiling or a universal grant maximum; additional/catch-up entitlement matters. [Official source](https://www.canada.ca/en/services/benefits/education/education-savings/estimating-amounts.html)
- **Class 1** — 4% — Buildings  _(ITR Schedule II Class 1)_
- **Class 8** — 20% — Furniture, equipment  _(ITR Schedule II Class 8)_
- **Class 10** — 30% — Motor vehicles. Passenger-vehicle Class 10.1 cost limit $38,000 + tax for 2025 acquisitions, $39,000 + tax for 2026; Class 10 itself has no per-vehicle cap  _(Dept. of Finance — 2025 Automobile Deduction Limits (Jan 2025); CRA — Classes of depreciable property)_
- **Class 10.1** — 30% — Passenger vehicles over cost limit  _(ITR Schedule II Class 10.1; CRA — classes of depreciable property)_
- **Class 12** — 100% — Computer software, tools <$500  _(ITR Schedule II Class 12)_
- **Class 50** — 55% — Computer hardware  _(ITR Schedule II Class 50)_
- **Class 54** — 30% declining balance — zero-emission passenger vehicles (cost cap $61,000 + tax), with enhanced first-year deductions under AIIP/RIIP  _(ITR Schedule II Class 54; CRA — classes of depreciable property — canada.ca)_ **HOLD:** The $61,000 ceiling is passenger-specific. First-year relief depends on property/cohort and actual operative conditions. [Official source](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/report-business-income-expenses/claiming-capital-cost-allowance/classes-depreciable-property.html)
- **Child care** — $8,000/child under 7; $5,000/child 7–16; $11,000 for a child eligible for the disability tax credit  _(ITA s.63(3))_ **HOLD:** Apply the actual age-timing, infirmity, earned-income/cost caps and spouse exceptions before using these limits. [Official source](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-63.html)
- **Medical expenses** — Medical expense credit rate for 2025 is 14.5% (NRTC; 14% for 2026). Threshold: amounts over the lesser of 3% of net income or $2,834(threshold for 2025)  _([ITA s.118.2; CRA — Medical expenses — canada.ca; Bill C-4 (14.5% credit rate for 2025)](https://www.canada.ca/en/department-finance/services/publications/report-impact-reducing-lowest-marginal-personal-income-tax-rate-non-refundable-tax-credits.html))_
- **Moving expenses** — Must move ≥ 40 km closer to new work location  _(ITA s.62)_
- **LCGE (QSBC shares)** — $1,275,000 (2026; $1,250,000 for 2025)  _([ITA s.110.6(2); Budget 2024; CRA — LCGE — canada.ca](https://www.canada.ca/en/revenue-agency/services/tax/individuals/frequently-asked-questions-individuals/adjustment-personal-income-tax-benefit-amounts.html))_
- **GAAR** — ITA s.245  _(ITA s.245)_
- **TOSI** — ITA s.120.4 — top rate on split income to family members  _(ITA s.120.4)_
- **Superficial loss** — You or an affiliated person acquire identical property in the period 30 days before to 30 days after the sale, and still own it at the end of that period: loss denied  _([ITA s.54; ITA s.40(2)(g)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-54.html))_

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
| Combined top rate (varies by province) | ~50–54% **HOLD:** The old ~50–54% range is not a verified nationwide range; select actual province, income type and year before a result. [Official source](https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/current-year.html) |
| CCPC small business rate (federal) | 9% on first $500,000 active business income |
| General corporate rate (federal) | 15% |
| Capital gains inclusion rate | 50% (66.7% increase was cancelled) |
| GST rate | 5% (HST varies by province: 13%–15%) |

### Federal Tax Brackets (2026)

**Federal Tax Brackets (2026)**

| Taxable Income (CAD) | Rate |
| --- | --- |
| 0 – 58,523 | 14% |
| 58,524 – 117,045 | 20.5% |
| 117,045 – 181,440 | 26% |
| 181,440 – 258,482 | 29% |
| 258,482+ | 33% |

For 2026 the full-year lowest rate is 14%; the annual 2025 rate was 14.5%, reflecting the midyear change. Do not apply the 2026 table to a 2025 return. [Official source](https://www.canada.ca/en/department-finance/services/publications/report-impact-reducing-lowest-marginal-personal-income-tax-rate-non-refundable-tax-credits.html)

## Section 2 — Income Splitting & Structuring

### Sole Proprietor vs CCPC

- **Sole proprietor** — All business income taxed at personal marginal rates. Simple, low compliance cost. Business losses offset personal income. No payroll remittances (except CPP). **HOLD:** The old loss-offset/no-remittance shorthand is not a complete individual filing rule; preserve loss restrictions and distinguish self-employed CPP from payroll remittances. [Official source](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-111.html)
- **Canadian-Controlled Private Corporation (CCPC)** — First $500,000 of active business income taxed at 9% federal (+ provincial, typically 2–4% = ~11–13% combined). Profits retained at corporate rate; extracted via salary or dividends. Integration principle: in theory, combined corporate + personal tax approximates personal tax alone. In practice, small gaps create planning opportunities. **HOLD:** The provincial 2–4% / combined 11–13% ranges are not universal. Bind actual jurisdiction/fiscal period, association, business-limit allocation/reductions and income qualification before a tax result. [Official source](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/corporations/corporation-tax-rates.html)
- **When to incorporate** — Generally beneficial when annual business profit consistently exceeds ~$70,000–$80,000 and the owner can leave profits in the corporation. Below that, sole proprietorship is simpler and equally tax-efficient. **HOLD:** The $70,000–$80,000 threshold is an unsupported planning heuristic, not a statutory break-even or guaranteed optimum.

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

- **Optimal mix** — Pay enough salary to maximise RRSP room ($33,810 limit for 2026 → requires ~$187,833 of 2025 earned income; salary paid in 2026 creates room under the 2027 limit of $35,390). If RRSP room is not needed, eligible dividends may produce slightly lower combined tax. Model annually — provincial rates create different break-even points.  _(https://www.canada.ca/en/revenue-agency/services/tax/registered-plans-administrators/whats-new.html)_ **HOLD:** No universal salary/dividend optimum follows from the RRSP ceiling. Establish personal room/adjustments, actual corporate period, dividend status, objective and matched cash cost before advice. [Official source](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/rrsps-related-plans/contributing-a-rrsp-prpp/contributions-affect-your-rrsp-prpp-deduction-limit.html)

### TOSI (Tax on Split Income) — s 120.4

- **TOSI** — Covered split income from a related business can be subject to top-rate tax unless an exclusion applies. Direct salary is not TOSI merely because the recipient is a family member or its amount is excessive; deduction reasonableness is a separate issue under [ITA 67](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-67.html). **HOLD:** determine the actual income category and exclusion conditions. [ITA 120.4](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-120.4.html); [CRA income categories](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-40424-federal-tax-on-split-income.html)
- **Excluded business** — Family member works ≥20 hours/week in the business  _(s 120.4)_ **HOLD:** The 20-hour shorthand omits regular involvement, current/five-prior-year and average-hours/operating-period conditions; no automatic exclusion is certified. [Official source](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-120.4.html)
- **Excluded shares** — Family member aged 25+, owns shares of a corporation (not a professional corporation) where <90% of income is from services, 10%+ of votes and value  _([s 120.4](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/federal-government-budgets/income-sprinkling/guidance-split-income-rules-adults/excluded-shares.html))_ **HOLD:** Bind direct ownership, measurement year and other-related-business-income conditions; the age/votes/value/service numbers alone do not qualify the recipient. [Official source](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/federal-government-budgets/income-sprinkling/guidance-split-income-rules-adults/excluded-shares.html)
- **Reasonable return** — Compensation proportional to labour, capital, risk contributed  _(s 120.4)_ **HOLD:** Age and operative exclusion conditions remain unresolved; proportional compensation alone is not an automatic TOSI exclusion. [Official source](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-120.4.html)
- **Prescribed rate loans** — Lend funds to spouse at CRA prescribed rate (3% Q1 2026); spouse invests, attributes interest income back to lender, keeps excess returns  _(s 74.5(2))_ **HOLD:** The 3% figure is Q1 2026 only. Section 74.5(2) rate and interest-payment conditions, including the 30-day-after-year-end requirement, must be bound before applying the attribution exception; s120.4 alone is not the loan rule. [Official source](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-74.5.html)

## Section 3 — Deductions Most People Miss

**Deductions Most People Miss**  _(https://www.canada.ca/en/department-finance/services/publications/report-impact-reducing-lowest-marginal-personal-income-tax-rate-non-refundable-tax-credits.html)_

| Deduction | Provision | Notes |
| --- | --- | --- |
| Home office expenses | s 8(1)(f), 8(1)(i), 18(12) | Employees: T2200 required. Self-employed: proportion of rent/mortgage interest, utilities, insurance, property tax **HOLD:** Employee/self-employed eligibility and complete operative expense limits were not verified here; do not infer a universal T2200 or deduction result. |
| Moving expenses | s 62 | Must move ≥40 km closer to new work/business location. Deduct against income at new location |
| Carrying charges | s 20(1)(c) | Interest on money borrowed to earn investment income. Includes investment counsel fees **HOLD:** Interest tracing and investment-counsel fees use distinct provisions/conditions; s20(1)(c) alone does not prove all fees deductible. |
| Medical expenses | s 118.2 | Tax credit at 14% federal (2026; 14.5% for 2025) on expenses >3% of net income or $2,834 (lesser, 2025 threshold). Include premiums, dental, prescriptions, travel for treatment **HOLD:** $2,834 and 14.5% are explicitly 2025 figures; the 2026 ceiling is $2,890 with a 14% ordinary credit rate, subject to qualifying expenses/persons and any top-up/limits. [Official source](https://www.canada.ca/en/revenue-agency/services/tax/individuals/frequently-asked-questions-individuals/adjustment-personal-income-tax-benefit-amounts.html) |
| Disability tax credit | s 118.3 | $10,341 federal credit (2026). Transferable to supporting person. Unlocks RDSP eligibility **HOLD:** $10,341 is the 2026 base amount, not that much cash refund; ordinary 14% value is $1,447.74 before limitations/top-up. Qualification and transfer conditions remain unresolved. [Official source](https://www.canada.ca/en/revenue-agency/services/tax/individuals/frequently-asked-questions-individuals/adjustment-personal-income-tax-benefit-amounts.html) |
| Northern residents deduction | s 110.7 | Residency deduction + travel benefits for prescribed zones **HOLD:** Full zone/residency/travel eligibility and limits were not read in this unit. |
| Capital cost allowance (CCA) on rental property | s 20(1)(a), Sch II | Class 1 (4%), Class 8 (20%). Accelerated Investment Incentive (triple declining balance in year 1) **HOLD:** The universal triple/1.5-times shorthand is not a complete first-year calculation. Bind property, acquisition/available-for-use cohort and rental-loss restrictions before computing. |
| Apprentice mechanic tools | s 8(1)(s) | Cost exceeding the greater of $1,000 plus the s.118(10) amount (Canada employment amount) and 5% of apprenticeship income (s 8(1)(r)) **HOLD:** Apply the actual paragraph 8(1)(r) formula and interactions; the 2026 Budget publicity does not prove enacted changes. [Official source](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-22900-other-employment-expenses.html) |
| Union/professional dues | s 8(1)(i) | Full deduction **HOLD:** Full operative eligibility and deduction limits were not verified in this unit. |
| Child care expenses | s 63 | $8,000/child under 7; $5,000/child 7–16; $11,000 if DTC-eligible. Must be claimed by lower-income spouse (exceptions apply) **HOLD:** Apply the actual age-timing, infirmity, earned-income/cost caps and higher-income-spouse exceptions; the listed amounts are not automatic entitlements. [Official source](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-63.html) |

## Section 4 — Capital Allowances Optimization

### Accelerated Investment Incentive (AII)

- **AII** — For assets acquired after 20 November 2018 and available for use before 2028: enhanced first-year CCA. Effectively 1.5× the normal CCA rate in Year 1 (eliminates the half-year rule and adds a 50% bonus). Applies to most CCA classes. **HOLD:** Original AIIP phaseout and restored cohorts differ. No universal multiplier applies across the dates in the old shorthand; bind cohort, available-for-use and enacted relief.

### Key CCA Classes

**Key CCA Classes**

| Class | Rate | Assets |
| --- | --- | --- |
| 1 | 4% | Buildings acquired after 1987 |
| 8 | 20% | Furniture, fixtures, equipment, machinery |
| 10 | 30% | Motor vehicles (passenger vehicle Class 10.1 cost limit $38,000 + tax for 2025 acquisitions, $39,000 + tax for 2026) |
| 10.1 | 30% | Passenger vehicles over cost limit (separate class per vehicle) |
| 12 | 100% | Computer software, tools <$500 |
| 50 | 55% | Computer hardware and systems software |
| 54 | 30% base declining-balance rate; enhanced first-year computation held | Eligible zero-emission vehicles; the $61,000 plus tax ceiling is passenger-specific, not a cap on every Class 54 asset. **HOLD:** apply actual vehicle/cohort/relief conditions before computing. [CRA classes](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/report-business-income-expenses/claiming-capital-cost-allowance/classes-depreciable-property.html) |

### Immediate Expensing (CCPCs)

- **Historical immediate expensing** — The old $1.5 million framework **excludes Classes 1–6, 14.1, 17, 47, 49 and 51**. The CCPC cohort generally used acquisitions on/after 19 April 2021 and availability before 1 January 2024; individual/eligible-partnership acquisition starts after 31 December 2021, with availability before 2025. **HOLD:** sharing, proration and actual eligible-property conditions must be established. This does not certify later class-specific relief or turn a 2026 proposal into enacted law. [ITR 1104 definitions](https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/section-1104.html); [historical Finance explanation](https://www.canada.ca/en/department-finance/news/2022/02/expansion-of-the-eligibility-for-tax-support-for-business-investments.html)

## Section 5 — Loss Utilization

### Non-Capital Losses

- **Non-capital losses** — Carry back 3 years or carry forward 20 years (s 111(1)(a)). Business losses of a sole proprietor offset all personal income in the current year. Corporate losses stay in the corporation.  _(s 111(1)(a))_ **HOLD:** The ordinary three-back/twenty-forward period does not settle restricted categories or loss events. [Official source](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-111.html)

### Capital Losses

- **Capital losses** — Net capital losses carry back 3 years or forward indefinitely (s 111(1)(b)). Can only offset capital gains. At death, net capital losses can offset any income in the year of death and prior year.  _(s 111(1)(b))_ **HOLD:** The ordinary capital-gain limitation/periods do not establish death-year/prior-year other-income offsets; amount and prior-exemption constraints remain unresolved. [Official source](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-111.html)

### Allowable Business Investment Losses (ABIL)

- **ABIL** — Loss on shares or debt of a small business corporation (s 38(c)). 50% of the loss is an ABIL, deductible against all income (not just capital gains). Excess becomes a non-capital loss.  _(s 38(c))_ **HOLD:** Small-business share/debt status alone does not establish a business investment loss. Qualification, prior exemptions and special carryforward/conversion conditions remain unresolved. [Official source](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-111.html)

### Loss Planning

- **Time capital gains and losses** — Time capital gains and losses in the same year to offset
- **Crystallise unrealised losses** — Crystallise unrealised losses before year-end (beware superficial loss rule: 30-day rule, s 54)  _(s 54)_
- **Spousal transfer** — A transfer at FMV does not by itself secure a current loss. A spouse is affiliated; acquisition and retained ownership or rights at the end of the statutory period can trigger superficial-loss denial. **HOLD:** apply the full definition, exceptions and any attribution/rollover treatment before recommending a transaction. [ITA 54](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-54.html); [ITA 40(2)(g)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-40.html); [ITA 251.1](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-251.1.html)

## Section 6 — Timing Strategies

**Timing Strategies**  _(https://www.canada.ca/en/revenue-agency/services/tax/individuals/frequently-asked-questions-individuals/adjustment-personal-income-tax-benefit-amounts.html)_

| Strategy | Detail |
| --- | --- |
| RRSP contribution by March 1 | Contributions made by 1 March deductible in prior tax year. Carry forward deduction if in lower bracket now **HOLD:** The date depends on the deduction year: 2025-income deadline was 2 March 2026; 2026-income deadline is 1 March 2027. This does not certify an individual's available deduction room. [CRA dates](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/rrsps-related-plans/important-dates-rrsp-rrif-rdsp.html); [CRA contribution years](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/completing-slips-summaries/financial-slips-summaries/rrsp-contribution-receipt-return/contribution-year.html) |
| Defer income | Delaying an invoice does not by itself defer accrual-method business income; cash-method eligibility cannot be assumed. **HOLD:** determine the recognition method and actual earning/payment facts. Employee bonus and owner-salary timing need their own receipt/deduction checks. [CRA accounting methods](https://www.canada.ca/en/revenue-agency/services/tax/businesses/small-businesses-self-employed-income/business-income-tax-reporting/accounting-your-earnings.html) |
| Accelerate deductions | Prepay deductible expenses before 31 December. Purchase CCA-eligible assets before year-end **HOLD:** Prepaid-period restrictions, actual incurrence and available-for-use/cohort conditions prevent automatic deductions from a December payment or purchase. [Official source](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-18.html) |
| Charitable donations | Carry forward donations up to 5 years. Consolidate to one spouse for higher credit rate (29%/33% on amounts >$200) **HOLD:** The 29%/33% rate is not a free choice; full 2026 claim/spouse/income-limit application remains unresolved. The read CRA rate table was dated 2025; ordinary five-year carryforward alone is confirmed. [Official source](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-34900-donations-gifts/how-much-claim.html) |
| Capital gains deferral | Hold assets >1 year (no discount, but defer realisation). Use CCPC to shelter passive income until extraction **HOLD:** This is planning policy, not a one-year holding discount or exemption from corporate passive-income taxation. [ITA 38 — inclusion framework only, not approval of the strategy](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-38.html) |
| LCGE crystallisation | Trigger capital gain on QSBC shares up to $1,275,000 LCGE (2026) while still eligible. Useful before selling active business **HOLD:** Personal remaining exemption, QSBC/residency/CNIL/loss constraints and AMT must be resolved before a transaction or saving. [Official source](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-110.6.html) |
| Prescribed rate loan before rate increase | Lock in lower CRA prescribed rate before quarterly adjustments **HOLD:** Use the actual quarter and payment/attribution-exception conditions, not just a headline rate. [Official source](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-74.5.html) |

## Section 7 — GST/HST Optimization

**GST/HST Optimization**

| Topic | Detail |
| --- | --- |
| Small supplier exemption | Gross revenue ≤$30,000 in 4 consecutive quarters → no mandatory registration. But voluntary registration allows ITCs **HOLD:** Single-quarter/four-quarter timing, associates, exceptions and registration type must be resolved; $30,000 alone does not decide registration. |
| Quick method | Simplified GST remittance for businesses ≤$400,000 revenue. Remit a reduced percentage; keep the difference. Often advantageous for service businesses with few inputs **HOLD:** The $400,000 test is not generic revenue eligibility; tax-inclusive/associate/period tests and excluded services apply. |
| Input Tax Credits (ITCs) | Claim GST/HST on business purchases. Documentation requirements: supplier name/BN, invoice date, total, GST amount **HOLD:** Different consideration tiers require different documentation fields; this short list is not a complete ITC-document test. |
| ITCs on vehicles | Claim proportional to business use. Maintain logbook **HOLD:** Capital-property/passenger-vehicle rules differ; do not calculate every vehicle ITC by a simple business-use percentage. |
| Real property | Self-supply rules on real property conversions. New residential property GST/HST rebate ($350,000–$450,000 threshold) **HOLD:** The federal new-housing phaseout/cohort computation and other rebate programs are not resolved by the $350,000–$450,000 range on its own. |
| Place of supply | GST vs HST depends on province of delivery. Optimise for lower-rate provinces where legitimately possible **HOLD:** Service/address and other place-of-supply rules prevent a universal physical-delivery test or elective lower-province treatment. |
| Zero-rated exports | Exports are zero-rated (0% GST) but ITCs on inputs still claimable **HOLD:** Apply actual export/recipient/property/service conditions before zero-rating or an ITC conclusion. |

## Section 8 — CPP/EI & Social Security Optimization

### CPP Contributions (2026)

- **CPP1** — 5.95% employee + 5.95% employer on pensionable earnings $3,500–$74,600 (max employee contribution $4,230.45)  _(https://www.canada.ca/en/services/benefits/publicpensions/cpp/contributions.html)_
- **CPP2** — 4% employee + 4% employer on earnings $74,600–$85,000 (second ceiling)  _(https://www.canada.ca/en/services/benefits/publicpensions/cpp/contributions.html)_
- **Self-employed CPP** — Self-employed pay both halves (11.9% CPP1 + 8% CPP2)
- **CCPC owner-manager dividends only** — No CPP contributions → no CPP pension accrual. Trade-off: lower current cost vs lower retirement benefit **HOLD:** Dividend payments alone do not establish total pension/benefit eligibility; past contributions, other employment, age and individual facts remain relevant.

### EI Premiums

- **Employees** — 1.63% on insurable earnings up to $68,900 (2026)  _(https://www.canada.ca/en/employment-social-development/news/2025/09/canada-employment-insurance-commission-sets-the-2026-employment-insurance-premium-rate.html)_
- **Self-employed** — Can opt in for special benefits (maternity, sickness)
- **CCPC dividends** — No EI — but also no EI eligibility **HOLD:** Salary/voting-owner and self-employed special-benefit exceptions prevent a universal no-EI-eligibility conclusion. [Official source](https://www.canada.ca/en/revenue-agency/services/tax/canada-pension-plan-cpp-employment-insurance-ei-rulings/cpp-ei-explained/employees-self-employed-workers-responsibilities-benefits-entitlements.html)

### Optimisation

- **Dividends avoid premiums** — If owner-manager does not need CPP/EI benefits, dividends avoid these premiums (~$6,000+ annual saving) **HOLD:** The $6,000-plus saving is not universal or computed. Sole voting-owner salary is already outside regular EI; age, other work and opt-in conditions matter. [Official source](https://www.canada.ca/en/revenue-agency/services/tax/canada-pension-plan-cpp-employment-insurance-ei-rulings/cpp-ei-explained/employees-self-employed-workers-responsibilities-benefits-entitlements.html)
- **Building CPP entitlement** — If building CPP entitlement, pay minimum salary to maximise CPP credits **HOLD:** This is planning policy; actual contribution history, coverage, room and objectives are required before recommending salary.
- **RRSP room balance** — Balance against RRSP room generation (requires earned income)

## Section 9 — Investment & Retirement

**Investment & Retirement**  _(https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4460/registered-disability-savings-plan.html)_

| Account | 2026 Limit | Tax Treatment |
| --- | --- | --- |
| RRSP | $33,810 (or 18% of prior-year earned income) | Contributions deductible; growth tax-deferred; withdrawals taxed as income **HOLD:** $33,810 is the 2026 new-room ceiling, not a choice between that and 18% or a universal cap on accumulated room; apply lesser-of, carryforward and adjustments. [Official source](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/rrsps-related-plans/contributing-a-rrsp-prpp/contributions-affect-your-rrsp-prpp-deduction-limit.html) |
| TFSA | $7,000 (cumulative $109,000 since 2009) | No deduction; growth and withdrawals tax-free **HOLD:** $109,000 assumes eligibility for each year's annual room; personal room depends on age, residency and transactions. Tax-free treatment also has operative conditions. [Official source](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/tax-free-savings-account/contributing/before.html) |
| FHSA | $8,000/year ($40,000 lifetime) | Deductible like RRSP + tax-free withdrawal for first home (like TFSA). Best of both worlds **HOLD:** Carryforward/adjustments can alter annual participation capacity; deduction and qualifying-withdrawal eligibility must be established separately. [Official source](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/first-home-savings-account/contributing-your-fhsa.html) |
| RESP | $2,500 yields the ordinary $500 basic CESG; this is not an annual RESP contribution ceiling or every grant maximum | Returned contributions are tax-free; educational assistance payments are income of the beneficiary; accumulated income payments have separate subscriber treatment. **HOLD:** establish payment type and grant/withdrawal eligibility before a personal result. [Official source](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/registered-education-savings-plans-resps/payments-resp.html); [CESG conditions](https://www.canada.ca/en/services/benefits/education/education-savings/estimating-amounts.html) |
| RDSP | Up to $200,000 lifetime | Government grants up to $3,500/year plus bonds up to $1,000/year. Must have DTC **HOLD:** DTC alone is not sufficient; age/income/contribution rules apply and unused entitlements can alter annual grants/bonds. The headline maxima are not automatic personal entitlements. [Official source](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4460/registered-disability-savings-plan.html) |

### Strategy Framework

- **1. FHSA first** — If qualifying first-time buyer — deductible AND tax-free withdrawal
- **2. Employer RRSP match** — Capture free money before any other investment
- **3. TFSA** — Fill annually, especially if in a lower bracket now (preserve RRSP room for higher-income years)
- **4. RRSP** — Maximise in years with high marginal rate, plan to withdraw in lower-rate retirement
- **5. RESP** — Trigger CESG grant ($500/child/year)
- **6. Non-registered** — Use Canadian eligible dividends and capital gains (50% inclusion) for tax efficiency

## Section 10 — Red Lines (GAAR & Scrutiny Triggers)

### GAAR (s 245 ITA)

- **GAAR test** — Applies when a transaction (i) results in a tax benefit, (ii) is an avoidance transaction under the current subsection 245(3) main-purpose test, and (iii) is abusive — misuses or frustrates the provisions of the Act. Consequence: the tax benefit may be denied. **HOLD:** apply the full operative test, application dates and any penalty/disclosure conditions before a conclusion. [ITA 245](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-245.html)

### CRA Scrutiny Triggers

**CRA Scrutiny Triggers**  _(https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/information-been-moved/foreign-reporting/questions-answers-about-form-t1135.html)_

| Trigger | Risk |
| --- | --- |
| TOSI-offending dividends to family members | Top-rate tax + interest |
| Superficial losses (repurchase within 30 days) | Loss denied (s 54) **HOLD:** Apply the full before/after window, end ownership/rights and exceptions; a repurchase alone does not settle every denial. [Official source](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-54.html) |
| Excessive salary to family members not working in business | Deduction reasonableness may be challenged under [ITA 67](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-67.html); direct salary is not on that basis covered split income for TOSI. [ITA 120.4](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-120.4.html); [CRA categories](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-40424-federal-tax-on-split-income.html) |
| Personal expenses through corporation | Shareholder benefit (s 15(1)) or deemed dividend (s 15(2)) **HOLD:** Full section 15 characterization was not read here; an income inclusion is not automatically a deemed dividend. |
| Automobile benefits | Standby charge + operating benefit if personal use not properly reported **HOLD:** Complete operative automobile-benefit application was not verified here. |
| Non-arm's length transactions at non-FMV | Transfer pricing rules (s 69, s 247) **HOLD:** The actual section 69/247 scope and transaction facts were not verified here; do not apply a generic transfer-pricing conclusion. |
| Foreign reporting non-compliance | T1135 (specified foreign property with total cost amount of more than $100,000 at any time in the year). Penalties: $2,500/year late filing **HOLD:** $2,500 is an ordinary late-penalty maximum, not a flat annual charge; actual days, minimum and enhanced regimes must be applied. |
| Underground economy / unreported income | CRA uses third-party data matching **HOLD:** No complete operative applicability or quantified scrutiny probability was verified here. |
| RRSP over-contribution | 1% per month penalty tax on excess >$2,000 |
| Aggressive tax shelters | CRA mandatory disclosure rules (s 237.3, 237.4) — expanded 2023 **HOLD:** Full reportable/notifiable/application and penalty conditions remain unresolved. |

### Absolute Prohibitions

- **Personal expenses as business deductions** — NEVER advise claiming personal expenses as business deductions
- **Hiding income/assets offshore** — NEVER advise hiding income or assets offshore without proper disclosure (T1135, T1134)
- **Ignoring TOSI** — NEVER advise ignoring TOSI rules when splitting income with family members
- **Superficial loss repurchase** — NEVER advise repurchasing securities within 30 days to trigger a loss (superficial loss) **HOLD:** This conduct warning is not a substitute for the complete statutory definition, end ownership/rights and exceptions. [Official source](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-54.html)
- **Backdating documents** — NEVER advise backdating transactions or documentation

## Section 11 — Annual Tax Planning Calendar

**Annual Tax Planning Calendar**

These include planning reminders, not only statutory deadlines. Tax-year 2026 personal filing/payment dates fall in 2027; special cases and holiday adjustments remain separate. June 30 is only a chosen corporate year-end, not a universal requirement.

| When | Action |
| --- | --- |
| January | New TFSA room available ($7,000). Review prescribed rate for spousal loans. Ensure FHSA contribution on track |
| February | Planning reminder, not a fixed legal deadline: 2025-income RRSP deadline was 2 March 2026; 2026-income deadline is 1 March 2027. Model RRSP/TFSA using actual room and equal cash costs. [CRA dates](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/rrsps-related-plans/important-dates-rrsp-rrif-rdsp.html); [CRA contribution years](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/completing-slips-summaries/financial-slips-summaries/rrsp-contribution-receipt-return/contribution-year.html) |
| 2 March 2026 / 1 March 2027 | Respective RRSP contribution deadlines for a 2025 / 2026 deduction, subject to actual room/eligibility. [CRA dates](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/rrsps-related-plans/important-dates-rrsp-rrif-rdsp.html); [CRA contribution years](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/completing-slips-summaries/financial-slips-summaries/rrsp-contribution-receipt-return/contribution-year.html) |
| April 30 | Personal tax return filing deadline. Tax balance owing due. CPP/EI self-employed remittance due |
| June 15 | Filing deadline for self-employed (but tax was due April 30) |
| June 30 | CCPC fiscal year-end (if elected). Review salary vs dividend mix |
| September | Model year-end tax position. Review quarterly instalment obligations |
| October–November | Execute capital gains/loss harvesting. Make charitable donations. Prepay deductible expenses |
| December 31 | **Critical date.** TFSA contributions. RESP contributions to trigger CESG. SRS/RRSP contributions for current year. Year-end trust distributions. Ensure T5013 / T3 slips timing. Pay salary/bonus before year-end for earned income **HOLD:** RRSP first-60-days rules prevent treating this as a universal RRSP deadline; SRS is undefined. Other account/trust/return/slip dates require their own conditions. [Official source](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/rrsps-related-plans/important-dates-rrsp-rrif-rdsp.html) |

## Section 12 — Cash Impact Examples

### Example 1 — CCPC Salary vs Dividend Mix (Ontario, 2026)

**Scenario:** CCPC earns $200,000 active business income. Owner is sole shareholder.

**All salary ($200,000):** For an ordinary full-year non-Quebec CPP contributor reaching both 2026 maxima, employee CPP is **$4,230.45 + $416 = $4,646.45**; employer CPP is the same, so combined CPP is **$9,292.90**. A $200,000 gross salary therefore costs the corporation **$204,646.45** before any other employer costs, exceeding this scenario's $200,000 income budget. The historical $8,300 CPP estimate is not either of those totals. **HOLD:** personal tax, deductible corporate costs, actual CPP eligibility and a matched corporate cash budget are not supplied, so no salary take-home or tax saving is certified. The old personal-tax and take-home estimates are not usable results; compute them only after the missing individual and corporate inputs are established. New 2027 RRSP room is conditionally min($200,000 × 18%, $35,390) = $35,390 before pension adjustments. [CPP contributions](https://www.canada.ca/en/services/benefits/publicpensions/cpp/contributions.html); [2026 formulas](https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/payroll-deductions-t4127-payroll-deductions-formulas/t4127-jan-122nd-edition-effective-january-1-2026/t4127-jan-payroll-deductions-formulas-computer-programs.html); [owner EI treatment](https://www.canada.ca/en/revenue-agency/services/tax/canada-pension-plan-cpp-employment-insurance-ei-rulings/cpp-ei-explained/employees-self-employed-workers-responsibilities-benefits-entitlements.html)

**All eligible dividends — HOLD:** the old 12.2%/$24,400 corporate tax, $175,600 residual, $25,200 personal tax, $150,400 net and $12,400 saving are not verified results. Ontario's lower corporate rate changed on 1 July 2026; establish the actual fiscal period and SBD eligibility. Eligible-dividend treatment also requires sufficient GRIP, which is not established merely by SBD-taxed income. Match the corporate cash budgets and actual owner inputs before comparing. Dividends themselves do not create earned-income RRSP room or CPP contributions. [CRA corporate rates](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/corporations/corporation-tax-rates.html); [CRA GRIP](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/corporations/eligible-dividends/general-rate-income-pool-grip.html)

**Proposed blend, not an optimum:** $100,000 salary plus the remainder as dividends is an illustration to test against RRSP room, CPP history, fiscal period, dividend status and equal corporate cash cost. **HOLD:** no objective or optimization calculation establishes it as best.



```oa-check
name: 2026 owner salary CPP illustration, ordinary full-year eligibility assumed
inputs:
  gross_salary: 200000
  cpp_max: 4230.45
  cpp2_max: 416
steps:
  employee_cpp: cpp_max + cpp2_max
  employer_cpp: employee_cpp
  combined_cpp: employee_cpp + employer_cpp
  corporate_salary_cost: gross_salary + employer_cpp
  new_rrsp_room_before_adjustments: min(gross_salary * 0.18, 35390)
expected:
  employee_cpp: 4646.45
  employer_cpp: 4646.45
  combined_cpp: 9292.90
  corporate_salary_cost: 204646.45
  new_rrsp_room_before_adjustments: 35390
```

### Example 2 — TFSA vs RRSP

**Profile:** 30-year-old earning $60,000 (20.5% federal bracket).

**RRSP $7,000:** If the $60,000 is taxable income before this deduction and other effects are held constant, the deduction crosses the $58,523 band: $1,477 × 20.5% + $5,523 × 14% = **$1,076.005**, about **$1,076.01 of federal tax reduction** (round half up to cents), not a guaranteed refund or complete provincial result. At an assumed annual 6% compound return for 30 years, $7,000 × 1.06^30 = **$40,204.44** before withdrawal tax. Under the example's assumed flat 14% withdrawal tax only, net is **$34,575.82**. **HOLD:** actual taxable income, available deduction room, future taxes and the unsupported $8,102 taxable-account comparison need their own inputs. [CRA indexed amounts](https://www.canada.ca/en/revenue-agency/services/tax/individuals/frequently-asked-questions-individuals/adjustment-personal-income-tax-benefit-amounts.html)

**TFSA $7,000:** assuming a permitted contribution/qualifying tax-free account and the same hypothetical growth, future value is **$40,204.44**. The arithmetic difference from the assumed flat-14% RRSP withdrawal is **$5,628.62**, not an established account-selection advantage. **HOLD:** a fair comparison must include equal cash costs and RRSP-refund reinvestment; no actual future return or tax rate is predicted. [CRA TFSA eligibility/room](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/tax-free-savings-account/contributing/before.html)



```oa-check
name: Conditional RRSP deduction, Decimal half-up rounding; flat withdrawal tax assumed
inputs:
  taxable_income_before_rrsp: 60000
  rrsp_deduction: 7000
  federal_first_ceiling: 58523
steps:
  deduction_in_second_band: min(rrsp_deduction, max(0, taxable_income_before_rrsp - federal_first_ceiling))
  deduction_in_first_band: rrsp_deduction - deduction_in_second_band
  federal_reduction: round(deduction_in_second_band * 0.205 + deduction_in_first_band * 0.14, 2)
  hypothetical_value_unrounded: 7000 * 1.06 * 1.06 * 1.06 * 1.06 * 1.06 * 1.06 * 1.06 * 1.06 * 1.06 * 1.06 * 1.06 * 1.06 * 1.06 * 1.06 * 1.06 * 1.06 * 1.06 * 1.06 * 1.06 * 1.06 * 1.06 * 1.06 * 1.06 * 1.06 * 1.06 * 1.06 * 1.06 * 1.06 * 1.06 * 1.06
  hypothetical_value: round(hypothetical_value_unrounded, 2)
  assumed_rrsp_net: round(hypothetical_value_unrounded * 0.86, 2)
  conditional_gap: hypothetical_value - assumed_rrsp_net
expected:
  deduction_in_second_band: 1477
  deduction_in_first_band: 5523
  federal_reduction: 1076.01
  hypothetical_value: 40204.44
  assumed_rrsp_net: 34575.82
  conditional_gap: 5628.62
```

### Example 3 — LCGE on Business Sale

Owner sells qualifying small business corporation shares with a **$1,000,000 gain**. The nominal 2026 lifetime ceiling is **$1,275,000**, but this does not establish the seller's remaining exemption or eligibility. **HOLD:** QSBC status, residency, CNIL/loss limits, prior claims and AMT must be resolved. $1,000,000 × 50% × an assumed flat 33% = **$165,000** is conditional arithmetic only; it is not certified cash saved under progressive federal/provincial tax. [ITA 110.6](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-110.6.html); [CRA minimum-tax guidance](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/deductions-credits-expenses/line-41700-minimum-tax.html)

```oa-check
name: LCGE example arithmetic only, actual eligibility and cash saving held
inputs:
  gain: 1000000
  assumed_inclusion: 0.50
  assumed_flat_federal_rate: 0.33
steps:
  conditional_amount: gain * assumed_inclusion * assumed_flat_federal_rate
expected:
  conditional_amount: 165000
```


## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, CA, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.


## Sources

This correction reuses the completed **21 November 2026** audit against the unchanged source blob. The 21 November dates identify reused bounded operative reads. Two 25 November RRSP follow-ups resolve actual review-source gaps; they are not a new whole-source review. A confirmed nominal rate does not confirm every planning strategy built around it. Direct-access restrictions, archived editions, displayed historical years and unresolved individual conditions remain explicit.

| Official source | Scope of completed read reused | Date read |
| --- | --- | --- |
| [Indexed amounts](https://www.canada.ca/en/revenue-agency/services/tax/individuals/frequently-asked-questions-individuals/adjustment-personal-income-tax-benefit-amounts.html) | Read bounded text: 2026 federal brackets, credit bases and LCGE; distinguish explicit historical 2025 amounts | 2026-11-21 |
| [Finance credit-rate report](https://www.canada.ca/en/department-finance/services/publications/report-impact-reducing-lowest-marginal-personal-income-tax-rate-non-refundable-tax-credits.html) | Read bounded text: 2025 annual 14.5% versus 2026 14% ordinary credit/rate context; not every personal credit computation | 2026-11-21 |
| [registered-plan limit table](https://www.canada.ca/en/revenue-agency/services/tax/registered-plans-administrators/pspa/mp-rrsp-dpsp-tfsa-limits-ympe.html) | Read bounded text: 2026/2027 indexed ceilings; nominal limits not personal available room | 2026-11-21 |
| [RRSP room formula](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/rrsps-related-plans/contributing-a-rrsp-prpp/contributions-affect-your-rrsp-prpp-deduction-limit.html) | Read bounded text: Lesser-of new room, prior earned income, carryforward and pension-adjustment conditions | 2026-11-21 |
| [CRA RRSP dates](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/rrsps-related-plans/important-dates-rrsp-rrif-rdsp.html) | Read bounded text: 2026-income contribution deadline of 1 March 2027; not the source for the 2025-income date | 2026-11-21; bounded follow-up 2026-11-25 |
| [CRA contribution-year table](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/completing-slips-summaries/financial-slips-summaries/rrsp-contribution-receipt-return/contribution-year.html) | Read bounded text: 2025 row ends 2 March 2026. The 2026 deadline is supported by the separate CRA dates page; the independent reader did not reproduce the writer's 2026 contribution-table row | 2026-11-21; bounded follow-up 2026-11-25 |
| [TFSA annual table](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/tax-free-savings-account/contributing/before.html) | Read bounded text: Annual room table and cumulative $109,000 arithmetic; age/residency/transactions remain individual | 2026-11-21 |
| [FHSA actual participation formulas](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/first-home-savings-account/contributing-your-fhsa.html) | Read bounded text: Participation-room/carryforward adjustments, deduction and withdrawal distinctions | 2026-11-21 |
| [2026 CESG table/catch-up conditions](https://www.canada.ca/en/services/benefits/education/education-savings/estimating-amounts.html) | Read bounded text: Basic/additional/catch-up grant conditions, not a $2,500 annual RESP ceiling | 2026-11-21 |
| [CRA operative payment rules](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/registered-education-savings-plans-resps/payments-resp.html) | Read bounded text: Tax-free returned contributions versus beneficiary EAP and subscriber AIP treatment | 2026-11-21 |
| [RDSP operative contribution/grant/bond/carryforward sections](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4460/registered-disability-savings-plan.html) | Read bounded text: Contribution, ordinary grant/bond and carryforward passages; amounts are not automatic entitlements | 2026-11-21 |
| [Quarter1 prescribed rate](https://www.canada.ca/en/revenue-agency/services/tax/prescribed-interest-rates/2026-q1.html) | Read bounded text: Q1 2026 loan rate only, not a year-round prescribed rate | 2026-11-21 |
| [loan exception74.5(2)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-74.5.html) | Read bounded text: Rate and interest-payment timing conditions for the spousal-loan exception | 2026-11-21 |
| [TOSI law](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-120.4.html) | Read bounded text: Covered split-income definitions, excluded business/share and age/return conditions | 2026-11-21 |
| [excluded-share gross-income/ownership conditions](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/federal-government-budgets/income-sprinkling/guidance-split-income-rules-adults/excluded-shares.html) | Read bounded text: Direct ownership, measurement year and other-related-business income conditions | 2026-11-21 |
| [CRA operative income categories](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-40424-federal-tax-on-split-income.html) | Read bounded text: Covered split-income categories; salary treatment rests on ITA 120.4, and deduction reasonableness on ITA 67 | 2026-11-21 |
| [Childcare 63(3)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-63.html) | Read bounded text: Qualifying expense limits and age/disability conditions; individual claim remains held | 2026-11-21 |
| [moving-expense conditions](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-21900-moving-expenses.html) | Read bounded text: 40km shortest-public-route/new ordinary-residence and eligible-income conditions | 2026-11-21 |
| [CRA apprentice formula](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-22900-other-employment-expenses.html) | Read bounded text: Operative tool formula and paragraph 8(1)(r) interactions; proposals not treated as enacted | 2026-11-21 |
| [loss periods 111(1)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-111.html) | Read bounded text: Ordinary carryback/forward periods; complete death/ABIL/personal application remains held | 2026-11-21 |
| [prepaid expense18(9)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-18.html) | Read bounded text: Prepaid-period restriction; paying in December alone does not decide deduction | 2026-11-21 |
| [Donation carryforward/rate page](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-34900-donations-gifts/how-much-claim.html) | Read bounded text: Ordinary carryforward and displayed 2025 rates; complete 2026 claim application held | 2026-11-21 |
| [operative ITR1104(3.1)](https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/section-1104.html) | Read bounded text: Historical immediate-expensing property definitions/exclusions and cohorts; sharing/proration still require inputs | 2026-11-21 |
| [2022 Finance source](https://www.canada.ca/en/department-finance/news/2022/02/expansion-of-the-eligibility-for-tax-support-for-business-investments.html) | Read bounded text: Historical excluded classes and acquisition/availability framework, not current open-ended relief | 2026-11-21 |
| [ITA 54](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-54.html) | Read bounded text: Superficial-loss window, end ownership/rights and exceptions | 2026-11-21 |
| [40(2)(g)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-40.html) | Read bounded text: Loss-denial provision read with the section 54 definition | 2026-11-21 |
| [251.1(1)(a)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-251.1.html) | Read bounded text: Spousal affiliation; FMV alone does not secure a current deductible loss | 2026-11-21 |
| [current245(3)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-245.html) | Read bounded text: Current main-purpose avoidance-transaction threshold, separately from misuse/abuse | 2026-11-21 |
| [CRA accounting-source read from unit7](https://www.canada.ca/en/revenue-agency/services/tax/businesses/small-businesses-self-employed-income/business-income-tax-reporting/accounting-your-earnings.html) | Read bounded text: Accrual/cash recognition and limited cash-method eligibility; unchanged applicable unit7 read reused | 2026-11-21 |
| [cited CPP source](https://www.canada.ca/en/services/benefits/publicpensions/cpp/contributions.html) | Read bounded text: Ordinary 2026 contribution bands/maxima reconciled with payroll tables where page label differed | 2026-11-21 |
| [CRA 2026 formulas](https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/payroll-deductions-t4127-payroll-deductions-formulas/t4127-jan-122nd-edition-effective-january-1-2026/t4127-jan-payroll-deductions-formulas-computer-programs.html) | Read bounded text: Archived Jan 2026 payroll formulas and Ontario bracket/credit parameters used for illustrative checks; not final T1 certification | 2026-11-21 |
| [CRA owner-insurability guidance](https://www.canada.ca/en/revenue-agency/services/tax/canada-pension-plan-cpp-employment-insurance-ei-rulings/cpp-ei-explained/employees-self-employed-workers-responsibilities-benefits-entitlements.html) | Read bounded text: Sole voting-owner/regular EI distinction; no universal dividends premium saving | 2026-11-21 |
| [Current Ontario corporate-rate evidence](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/corporations/corporation-tax-rates.html) | Read bounded text: Actual provincial rates and 1 July 2026 Ontario change; no universal provincial range | 2026-11-21 |
| [CRA GRIP rule](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/corporations/eligible-dividends/general-rate-income-pool-grip.html) | Read bounded text: Eligible-dividend capacity; SBD-taxed income alone does not demonstrate sufficient GRIP | 2026-11-21 |
| [Current 110.6](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-110.6.html) | Read bounded text: Deduction/remaining-room constraints, not automatic exemption or actual cash saved | 2026-11-21 |
| [CRA minimum-tax guidance](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/deductions-credits-expenses/line-41700-minimum-tax.html) | Read bounded text: AMT applicability; displayed $177,882 was 2025 and not copied as 2026 threshold | 2026-11-21 |
| [The Guide's own EI release](https://www.canada.ca/en/employment-social-development/news/2025/09/canada-employment-insurance-commission-sets-the-2026-employment-insurance-premium-rate.html) | Read bounded text: 2026 non-Quebec EI rate and insurable-earnings ceiling; individual coverage still needed | 2026-11-21 |
| [Mega Deduction announcement](https://www.canada.ca/en/department-finance/news/2026/09/government-of-canada-introduces-new-productivity-mega-deduction-to-boost-canadas-advantage-as-the-most-competitive-g7-country-for-new-business-inve.html) | Read bounded text: September 2026 announced proposals; announcement is not proof of enacted relief | 2026-11-21 |
| [CRA depreciable-property classes](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/report-business-income-expenses/claiming-capital-cost-allowance/classes-depreciable-property.html) | Read bounded text reused from completed related accounting research: base class rates, vehicle scope and acquisition cohorts; complete enhanced/rental computations remain held | 2026-11-21 |
| [CRA Quick Method](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4058/quick-method-accounting-gst-hst.html) | Read operative eligibility/associate/period/tax-inclusive and excluded-service sections reused from completed related GST research; not an unqualified revenue-only election | 2026-11-21 |
| [ITC documentation regulation](https://laws-lois.justice.gc.ca/eng/regulations/SOR-91-45/section-3.html) | Read operative documentary tiers reused from completed GST work; short invoice list is not sufficient for every claim | 2026-11-21 |
| [ITA 67](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-67.html) | Complete operative section read: otherwise deductible outlays/expenses are limited to amounts reasonable in the circumstances; no individual salary deduction is certified | 2026-11-25 |

**Not yet confirmed:** unresolved applications remain limited or held; adjacent HOLDs identify the affected advice. In particular: national combined-rate ranges and universal incorporation/optimal-strategy claims; actual personal RRSP/TFSA/FHSA/RESP/RDSP room and eligibility; TOSI/loan operative application; home-office/interest/fees/northern/dues/tool/childcare conditions; medical/disability personal credit and transfer limits; complete enhanced/rental CCA and later enacted-relief availability; death/ABIL/loss outcomes; timing/constructive-receipt and donation applications; actual LCGE/QSBC/CNIL/loss/residency/AMT outcomes; GST registration/Quick Method/documentation/vehicle/real-property/place-of-supply/export computations; CPP/EI personal entitlement and claimed savings; shareholder/automobile/non-arm's-length/foreign-reporting/disclosure liability; and the actual salary/dividend, taxable-account and withdrawal-tax comparisons. Planning-policy sequences and conduct reminders are not statutory verification. The old salary/dividend comparison, taxable-account advantage and LCGE cash saving must not be used as verified outputs. No client return or investment recommendation was verified.
