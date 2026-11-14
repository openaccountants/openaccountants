---
name: optimisation-advisor
description: "Shared 2026 planning method retaining forty checks across US, UK, DE, AU, CA, IN, ES and MT. Establish actual year, eligibility, election history and contributions; recompute baseline and alternatives, distinguish permanent tax effects from deferral and cash flow, deduct actual costs, preserve unresolved rules and produce an evidence-linked reviewer workpaper. Older filing-cycle guidance is explicitly dated; approval of the method does not approve a proposed transaction."
version: 0.2
jurisdiction: GLOBAL
tax_year: 2026
type: cross-country-method
last_updated: 2026-11-14
depends_on:
  - workflow-base
category: intelligence
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: tooling
---

# Optimisation Advisor

## Optimisation Advisor v0.2

## What this file is

**Obligation category:** INTEL (Intelligence / Cross-cutting)
**Functional role:** Post-computation optimisation scanning, savings identification
**Status:** Active

This is a substantive cross-country planning method, used with the actual base computation, current country method and primary law. It preserves all forty checks and their evidence, calculations, elections, timing and reviewer tasks. It does not supply a complete worldwide rate engine. Establish the actual tax period first: US/DE/CA use the relevant 2026 year; UK and AU distinguish their tax years; India references below explicitly bridge FY 2025-2026/AY 2026-2027 and do not certify successor Act rules for tax year 2026-2027. Where only a latest detailed 2025 filing guide was read, its year remains visible.

Read the complete existing record before asking anything: baseline computation and reconciliation, income and accounting method, residence/entity and province/region, prior returns/elections, contribution statements and carryovers, other employment/plans, exact source/version, actual sign-off and proposed dates/costs. Ask only for genuine gaps. Preserve the actual named accountant and approval state of the underlying method; no model-generated scenario, T1 label or self-review approves this client transaction.

**The reviewer is the customer of this output.** All optimisation suggestions are addressed to the credentialed reviewer. The reviewer decides which opportunities to pursue and validates the calculations.

> **Disclaimer.** Optimisation suggestions are based on general statutory rules and the user's data as provided. They do not constitute tax advice, tax planning, or a recommendation to take any specific action. Every suggestion must be reviewed by a credentialed professional who can assess the user's full circumstances, including factors not captured in the data. Savings estimates are approximations and may differ from actual outcomes. Aggressive or novel positions are never suggested. OpenAccountants accepts no liability for actions taken based on these suggestions.

## Scope

### Section 1: Scope statement

This skill covers:

- **Jurisdictions:** US, UK, DE, AU, CA, IN, ES, MT (8 jurisdictions, 5 checks each = 40 checks)
- **Check categories:** Retirement contributions, entity structure, timing, elections, unclaimed credits/reliefs
- **Output:** Ranked list of savings opportunities with estimated value

This skill does NOT cover:

- Corporate tax planning, transfer pricing, or group restructuring
- Abusive tax positions or concealment; legally reportable arrangements require specialist assessment, not an assumption of illegality
- Cross-border restructuring (see cross-border skills)
- Automatic implementation of opportunities below or above the internal presentation threshold. Every legal obligation, error, deadline, refusal and eligibility gap remains visible regardless of value.
- Retrospective amendments to prior-year returns (flag for reviewer only)

## The method, step by step

### Section 2: Workflow

### Step 0 -- Gather computation outputs

This skill requires at least one of:

1. **Completed tax computation** from a content skill (e.g., Schedule C output, SA 100 computation)
2. **Income and expense summary** with enough detail to run checks
3. **Explicit user data** -- "I earned $X, my expenses were $Y, I contributed $Z to retirement"

If insufficient data, state which checks cannot be run and what data is needed.

### Step 1 -- Run optimisation checks

For each check applicable to the user's jurisdiction:

1. **Evaluate the trigger condition** -- does the check apply to this user?
2. **If triggered, run the calculation** -- compute the estimated savings
3. **Apply the internal presentation filter** only after evaluating obligations, eligibility and interactions. Keep sub-threshold items in Part C; never hide an error, deadline or legal requirement.
4. **Assign a confidence tier:**
   - T1: Mechanical arithmetic under fully evidenced facts and applicable law, with the source, exact year and assumptions shown. It is not a certainty or professional approval label.
   - T2: Conditional: judgement, missing facts, current rules, legal eligibility, future income or an election remains unresolved. Do not output an unconditional available saving or action. Add an explicit held status when no numerical result can be supported.
5. **Flag for reviewer** -- every optimisation is flagged; some require active reviewer decision

### Step 2 -- Rank and present

Recompute the complete baseline and each legal alternative using identical commercial facts and the actual year. Show tax before/after, cash invested, fees, future reversal/extraction, funding/access restrictions and interaction effects. A deduction multiplied by a marginal rate is only a screening estimate where that rate remains applicable; it is not a complete tax recomputation. Rank comparable permanent net effects separately from tax deferral, cash-flow release and interest avoided. Do not add overlapping alternatives or currencies. A smaller current payment is not automatically a smaller final liability. Present per Section 5.

### Step 3 -- Caveats

For each suggestion, state:
- What assumption was made
- What could change the result
- Whether timing matters (current year only, or can be applied retroactively)

## Section 3 -- Optimisation checks by jurisdiction

### 3.1 United States (US) -- 5 checks

#### US-OPT-1: Retirement contribution room

**US-OPT-1: Retirement contribution room**

| Field | Detail |
| --- | --- |
| **Category** | Retirement contributions |
| **Trigger** | User has SE income > $0 AND has not maximised retirement contributions |
| **Vehicles** | 2026 ordinary elective 401(k) limit USD 24,500; annual additions USD 72,000 excluding eligible catch-up, subject to actual compensation/plan limits. Ordinary age-fifty catch-up USD 8,000; eligible ages sixty to sixty-three use the higher USD 11,250 instead, not both. Ordinary SIMPLE USD 17,000; certain applicable SIMPLE accounts USD 18,100. IRA USD 7,500 plus eligible catch-up USD 1,100. SEP/owner-employer and SIMPLE employer contributions follow actual plan/earned-income and employee requirements, not one percentage of raw Schedule C profit. [IRS 2026 limits](https://www.irs.gov/newsroom/401k-limit-increases-to-24500-for-2026-ira-limit-increases-to-7500) / [401(k) additions](https://www.irs.gov/retirement-plans/plan-participant-employee/retirement-topics-401k-and-profit-sharing-plan-contribution-limits) / [Owner computation](https://www.irs.gov/retirement-plans/one-participant-401k-plans) |
| **Calculation** | Calculate actual eligible remaining room after all plans/contributions, required earned-income adjustments and plan limits. Recompute the whole federal and any separately sourced state tax before/after, including QBI and deduction/credit interactions. Show contribution cash required and future withdrawal taxation separately. Roth contributions are not a current deduction. [Official source](https://www.irs.gov/retirement-plans/one-participant-401k-plans) |
| **Materiality** | > $100 federal tax savings |
| **Confidence** | T1 only for fully evidenced law/facts and mechanical comparison; otherwise T2/held. Neither confers accountant approval. |
| **Reviewer flag** | Verify all employers/plans, employee eligibility, age, compensation, deductible IRA income limits and actual Roth/catch-up treatment. Establish plan adoption, election and deposit deadlines separately: a blanket calendar-year-end adoption deadline is wrong; latest 2025-cycle Pub 560 describes special later adoption for qualifying no-employee sole proprietors. Current 2026 plan-specific deadlines/catch-up restrictions remain held until checked. [Pub 560 selected adoption paragraphs](https://www.irs.gov/publications/p560) |
| **Output** | Reviewer: report this check's actual year, facts, source and full baseline/alternative comparison using Part B. State held conditions, permanent versus timing effect, costs, deadline and required professional decision; do not implement an unresolved alternative. |

#### US-OPT-2: Entity structure -- S-Corp election

**US-OPT-2: Entity structure -- S-Corp election**

| Field | Detail |
| --- | --- |
| **Category** | Entity structure |
| **Trigger** | Sole-proprietor/SMLLC evaluating a legally available S election with evidence for salary, actual profit and costs. The old USD 60,000 screening point is internal prioritisation, not eligibility, a legal threshold or proof of savings. |
| **Calculation** | Compare complete sole-proprietor SE/income tax against S-company salary, employer/employee payroll taxes, distributions, other wages and actual combined wage-base use, Medicare/additional taxes, QBI and state taxes. Then subtract actual payroll, return, state and formation/ongoing costs. Never multiply distributions by a flat combined SE percentage: the earnings adjustment, separate bases/caps and reasonable salary change the comparison. [Official source](https://www.irs.gov/businesses/small-businesses-self-employed/s-corporation-compensation-and-medical-insurance-issues) |
| **Materiality** | > $3,000 net annual savings (to justify complexity) |
| **Confidence** | T1 only for fully evidenced law/facts and mechanical comparison; otherwise T2/held. Neither confers accountant approval. |
| **Reviewer flag** | Document services performed and defensible reasonable compensation before nonwage distributions. Confirm election/entity/shareholder eligibility, deadlines/late relief, benefits, state treatment and actual cost quotes. No invented salary or vendor fee is a current legal figure. [Official source](https://www.irs.gov/businesses/small-businesses-self-employed/s-corporation-compensation-and-medical-insurance-issues) |
| **Output** | Reviewer: report this check's actual year, facts, source and full baseline/alternative comparison using Part B. State held conditions, permanent versus timing effect, costs, deadline and required professional decision; do not implement an unresolved alternative. |

#### US-OPT-3: Timing -- income deferral / expense acceleration

**US-OPT-3: Timing -- income deferral / expense acceleration**

| Field | Detail |
| --- | --- |
| **Category** | Timing |
| **Trigger** | User is cash-basis AND (a) has invoices near year-end that could be deferred, OR (b) has deductible expenses that could be prepaid |
| **Calculation** | Model both years: current tax reduction less future tax increase and actual funding/commercial costs, with a separately stated discount assumption if presenting time value. Reconcile actual/constructive receipt and the permitted accounting method; delaying an invoice or not withdrawing funds does not by itself defer income. [Pub 538 selected cash/advance-payment sections](https://www.irs.gov/publications/p538) |
| **Materiality** | > $200 tax impact |
| **Confidence** | T1 only for fully evidenced law/facts and mechanical comparison; otherwise T2/held. Neither confers accountant approval. |
| **Reviewer flag** | Test constructive receipt, actual payment and capitalisation, related-party/inventory and method-change requirements. The twelve-month exception ends at the earlier of twelve months after the benefit begins and the end of the following tax year; it is not permission to deduct every prepayment. Existing method changes may need consent. Latest detailed guide read is the published 2025 filing cycle. [Official source](https://www.irs.gov/publications/p538) |
| **Output** | Reviewer: report this check's actual year, facts, source and full baseline/alternative comparison using Part B. State held conditions, permanent versus timing effect, costs, deadline and required professional decision; do not implement an unresolved alternative. |

#### US-OPT-4: Election -- home office method

**US-OPT-4: Election -- home office method**

| Field | Detail |
| --- | --- |
| **Category** | Elections |
| **Trigger** | User claims home office AND has not evaluated both methods |
| **Calculation** | Compare supported simplified and actual eligible deductions after their actual income limits and carryovers; recompute tax, not the absolute difference alone. Simplified uses USD 5 per qualifying square foot up to 300, computed maximum USD 1,500. Avoid double-counting separately deductible interest/taxes. [Official source](https://www.irs.gov/businesses/small-businesses-self-employed/simplified-option-for-home-office-deduction) |
| **Materiality** | > $100 tax difference between methods |
| **Confidence** | T1 only for fully evidenced law/facts and mechanical comparison; otherwise T2/held. Neither confers accountant approval. |
| **Reviewer flag** | Eligibility applies to both methods, with actual storage/daycare exceptions and separate-structure/principal-place tests. Preserve unused regular-method carryovers and actual depreciation/recapture history. Timely-original-return method choice cannot be switched for that same year; annual comparisons are not an amended-election right. [Official source](https://www.irs.gov/businesses/small-businesses-self-employed/simplified-option-for-home-office-deduction) |
| **Output** | Reviewer: report this check's actual year, facts, source and full baseline/alternative comparison using Part B. State held conditions, permanent versus timing effect, costs, deadline and required professional decision; do not implement an unresolved alternative. |

#### US-OPT-5: Unclaimed -- Self-employed health insurance deduction

**US-OPT-5: Unclaimed -- Self-employed health insurance deduction**

| Field | Detail |
| --- | --- |
| **Category** | Credits/reliefs not claimed |
| **Trigger** | User has SE income AND pays health/dental/vision premiums AND has not claimed the above-the-line deduction |
| **Calculation** | Compute deductible eligible premiums under the actual business-established plan and earned-income limit after relevant adjustments, by business and month. Recompute full tax before/after; the deduction is not automatically all premiums or a reduction of SE earnings. Latest Form 7206 instructions read are explicitly 2025-cycle guidance, not a verified 2026 update. [Official source](https://www.irs.gov/instructions/i7206) |
| **Materiality** | > $100 tax savings |
| **Confidence** | T1 only for fully evidenced law/facts and mechanical comparison; otherwise T2/held. Neither confers accountant approval. |
| **Reviewer flag** | Test employer-subsidised-plan eligibility for every month, including spouse/dependent or qualifying child employer plans, whether or not joined. Coordinate Marketplace premium tax credit through actual Form 8962/Pub 974 rules, not a blanket ban on both benefits. Check S-company insurance/payroll evidence and any long-term-care limits separately. [Official source](https://www.irs.gov/instructions/i7206) |
| **Output** | Reviewer: report this check's actual year, facts, source and full baseline/alternative comparison using Part B. State held conditions, permanent versus timing effect, costs, deadline and required professional decision; do not implement an unresolved alternative. |

### 3.2 United Kingdom (UK) -- 5 checks

#### UK-OPT-1: Pension contribution room

**UK-OPT-1: Pension contribution room**

| Field | Detail |
| --- | --- |
| **Category** | Retirement contributions |
| **Trigger** | User has not contributed the full annual allowance to a pension |
| **Calculation** | Keep pension annual allowance separate from the personal contribution earnings-relief limit. Ordinary annual allowance GBP 60,000 covers employer/employee defined-contribution input and defined-benefit growth across schemes; qualifying unused allowance from the previous three tax years may carry forward. Personal contribution relief normally follows relevant earnings with the actual low/no-earnings exception. Recompute tax including relief already given at source/net pay, country bands and any allowance charge, not all room multiplied by a top rate. [Official source](https://www.gov.uk/tax-on-your-private-pension/annual-allowance) / [Official source](https://www.gov.uk/tax-on-your-private-pension/pension-tax-relief) |
| **Materiality** | > GBP 100 tax savings |
| **Confidence** | T1 only for fully evidenced law/facts and mechanical comparison; otherwise T2/held. Neither confers accountant approval. |
| **Reviewer flag** | Taper requires both threshold income over GBP 200,000 and adjusted income over GBP 260,000, not adjusted income alone. Actual tapered floor and MPAA amount, carry-forward membership/use, relevant earnings, salary sacrifice and flexi-access must be verified before room is certified. Personal-allowance taper can increase incremental relief but is not a universal sixty-percent pension rate. [Official source](https://www.gov.uk/tax-on-your-private-pension/annual-allowance) / [Official source](https://www.gov.uk/tax-on-your-private-pension/pension-tax-relief) |
| **Output** | Reviewer: report this check's actual year, facts, source and full baseline/alternative comparison using Part B. State held conditions, permanent versus timing effect, costs, deadline and required professional decision; do not implement an unresolved alternative. |

#### UK-OPT-2: Entity structure -- incorporation

**UK-OPT-2: Entity structure -- incorporation**

| Field | Detail |
| --- | --- |
| **Category** | Entity structure |
| **Trigger** | User is sole trader AND net profit > GBP 50,000 |
| **Calculation** | For 2026-2027 compare complete actual sole-trader income tax and Class 4 contributions against company tax, salary with employer/employee NIC and dividend tax plus actual costs and future extraction. Class 2 is treated paid for qualifying profits rather than a compulsory weekly charge. Class 4 is 6% above GBP 12,570 up to GBP 50,270 then 2%. Dividend ordinary/higher/additional rates are 10.75%/35.75%/39.35%, allowance GBP 500. Corporation-tax small/main rules include marginal relief and adjusted/associated-company conditions. A salary equal to the personal allowance is not automatically optimal. [Official source](https://www.gov.uk/self-employed-national-insurance-rates) / [Official source](https://www.gov.uk/tax-on-dividends) / [Official source](https://www.gov.uk/government/publications/rates-and-allowances-corporation-tax/rates-and-allowances-corporation-tax) |
| **Materiality** | > GBP 2,000 net annual savings |
| **Confidence** | T1 only for fully evidenced law/facts and mechanical comparison; otherwise T2/held. Neither confers accountant approval. |
| **Reviewer flag** | Actual IR 35/off-payroll, company eligibility, loss relief, benefits, employer NIC, associated companies and salary/dividend/cash needs require evidence. Use actual quoted fees, not the old estimated accountancy range. The profit screening point and net-benefit floor are internal workflow settings, not law. [Official source](https://www.gov.uk/government/publications/rates-and-allowances-corporation-tax/rates-and-allowances-corporation-tax) |
| **Output** | Reviewer: report this check's actual year, facts, source and full baseline/alternative comparison using Part B. State held conditions, permanent versus timing effect, costs, deadline and required professional decision; do not implement an unresolved alternative. |

#### UK-OPT-3: Timing -- payments on account reduction

**UK-OPT-3: Timing -- payments on account reduction**

| Field | Detail |
| --- | --- |
| **Category** | Timing |
| **Trigger** | User's current-year income is expected to be significantly lower than prior year AND payments on account are based on prior-year liability |
| **Calculation** | Show supported payment-on-account reduction as temporary cash released, separate from the unchanged final tax liability. Reconcile actual statement, payments, forecast, later balancing payment and possible interest; no invented current interest percentage. [Official source](https://www.gov.uk/understand-self-assessment-bill/payments-on-account) |
| **Materiality** | > GBP 500 cash flow benefit |
| **Confidence** | T1 only for fully evidenced law/facts and mechanical comparison; otherwise T2/held. Neither confers accountant approval. |
| **Reviewer flag** | HMRC charges interest if POA reduction results in underpayment. Conservative approach: reduce only if high confidence income is lower. Form SA 303. |
| **Output** | Reviewer: report this check's actual year, facts, source and full baseline/alternative comparison using Part B. State held conditions, permanent versus timing effect, costs, deadline and required professional decision; do not implement an unresolved alternative. |

#### UK-OPT-4: Election -- cash basis vs accruals

**UK-OPT-4: Election -- cash basis vs accruals**

| Field | Detail |
| --- | --- |
| **Category** | Elections |
| **Trigger** | An eligible sole trader or non-corporate partnership comparing the current default cash basis with a supported accruals election, regardless of the retired entry turnover ceiling. [Official source](https://www.gov.uk/simpler-income-tax-cash-basis) |
| **Calculation** | Compare full computations including stock/capital items, transition adjustments and future reversal. From 2024-2025 the old turnover restriction, cash-basis-specific GBP 500 interest cap and sideways-loss restriction were removed; do not apply them in 2026-2027. Debtors less creditors alone is only an incomplete timing screen. [Finance Act 2024 Schedule 10 paragraphs 6 to 8](https://www.legislation.gov.uk/ukpga/2024/3/schedule/10) |
| **Materiality** | > GBP 200 timing benefit |
| **Confidence** | T1 only for fully evidenced law/facts and mechanical comparison; otherwise T2/held. Neither confers accountant approval. |
| **Reviewer flag** | Test excluded trades and actual opt-out/election and transition treatment. Removal of the cash-specific restrictions does not make private interest, all assets or every loss deductible. Accruals can be selected for actual commercial/reporting needs. [Official source](https://www.gov.uk/simpler-income-tax-cash-basis) / [Official source](https://www.legislation.gov.uk/ukpga/2024/3/schedule/10) |
| **Output** | Reviewer: report this check's actual year, facts, source and full baseline/alternative comparison using Part B. State held conditions, permanent versus timing effect, costs, deadline and required professional decision; do not implement an unresolved alternative. |

#### UK-OPT-5: Unclaimed -- Trading allowance

**UK-OPT-5: Unclaimed -- Trading allowance**

| Field | Detail |
| --- | --- |
| **Category** | Credits/reliefs not claimed |
| **Trigger** | Aggregate gross qualifying trading/miscellaneous income and actual exclusions across sources, including at or below GBP 1,000, or compare partial relief above that level; not one extra allowance per secondary trade. [Official source](https://www.gov.uk/guidance/tax-free-allowances-on-property-and-trading-income) |
| **Calculation** | Compare lawful allowance versus actual expenses/loss relief and the full resulting tax, never both against the same covered income. Full relief may remove a reporting duty, but actual exceptions/return notices/other reasons remain. The allowance does not create a loss. [Official source](https://www.gov.uk/guidance/tax-free-allowances-on-property-and-trading-income) |
| **Materiality** | > GBP 100 |
| **Confidence** | T1 only for fully evidenced law/facts and mechanical comparison; otherwise T2/held. Neither confers accountant approval. |
| **Reviewer flag** | Check excluded partnership, own/connected company and employer/spouse-employer income, self-assessment circumstances and retained records. Assess gross aggregate income, not profit or each source separately. [Official source](https://www.gov.uk/guidance/tax-free-allowances-on-property-and-trading-income) |
| **Output** | Reviewer: report this check's actual year, facts, source and full baseline/alternative comparison using Part B. State held conditions, permanent versus timing effect, costs, deadline and required professional decision; do not implement an unresolved alternative. |

### 3.3 Germany (DE) -- 5 checks

#### DE-OPT-1: Ruerup (Basisrente) contribution room

**DE-OPT-1: Ruerup (Basisrente) contribution room**

| Field | Detail |
| --- | --- |
| **Category** | Retirement contributions |
| **Trigger** | User has not maximised Basisrente (Ruerup) contributions |
| **Calculation** | For 2026 the general relevant pension-expense ceiling is EUR 30,826 single / EUR 61,652 jointly assessed, not the old 2025 amount. Compute actual remaining deductible room after statutory/occupational and employer adjustments; full percentage deductibility since 2023 does not mean every euro up to the ceiling is new private Basisrente room. Recompute tax/solidarity/church effects under actual facts. [Bavarian tax administration 2026 explanation](https://www.steuerberechnung.bayern.de/Alterseinkuenfte-Rechner/2026/aekr_formular.asp?VLG=2) / [EStG section 10(3)](https://www.gesetze-im-internet.de/estg/__10.html) |
| **Materiality** | > EUR 100 tax savings |
| **Confidence** | T1 only for fully evidenced law/facts and mechanical comparison; otherwise T2/held. Neither confers accountant approval. |
| **Reviewer flag** | Check contract qualification, contributions already counted and statutory employer offsets, actual joint assessment and liquidity/retirement restrictions. Do not promise access to the pension or all ceiling room solely because the contribution balance is known. [Official source](https://www.gesetze-im-internet.de/estg/__10.html) |
| **Output** | Reviewer: report this check's actual year, facts, source and full baseline/alternative comparison using Part B. State held conditions, permanent versus timing effect, costs, deadline and required professional decision; do not implement an unresolved alternative. |

#### DE-OPT-2: Entity structure -- GmbH vs Einzelunternehmen

**DE-OPT-2: Entity structure -- GmbH vs Einzelunternehmen**

| Field | Detail |
| --- | --- |
| **Category** | Entity structure |
| **Trigger** | Net business income > EUR 80,000 AND user is sole proprietor (Einzelunternehmer) |
| **Calculation** | Compare fully calculated sole-proprietor income tax with the actual limited section 35 trade-tax credit against company tax, solidarity surcharge, municipality trade tax, supported salary/social treatment and eventual distribution tax. Current KStG specifies 15% corporation tax through 2027; actual trade tax uses the statutory measurement amount and municipal multiplier, not a nationwide fourteen-percent rate. Retained-profit deferral is not permanent savings after extraction. [Official source](https://www.gesetze-im-internet.de/kstg_1977/__23.html) / [Official source](https://www.gesetze-im-internet.de/gewstg/__11.html) / [Official source](https://www.gesetze-im-internet.de/estg/__35.html) |
| **Materiality** | > EUR 3,000 net annual savings |
| **Confidence** | T1 only for fully evidenced law/facts and mechanical comparison; otherwise T2/held. Neither confers accountant approval. |
| **Reviewer flag** | Obtain actual incorporation/notarial/accounting costs, capital funding and legal capital requirements, director status, distribution treatment and hidden-distribution issues. Capital is funding, not a deductible formation expense. The natural-person/partnership trade allowance is EUR 24,500 under section 11, not a GmbH allowance. No unverified universal personal top-rate/Soli computation or dividend route is used. [Official source](https://www.gesetze-im-internet.de/gewstg/__11.html) |
| **Output** | Reviewer: report this check's actual year, facts, source and full baseline/alternative comparison using Part B. State held conditions, permanent versus timing effect, costs, deadline and required professional decision; do not implement an unresolved alternative. |

#### DE-OPT-3: Timing -- Investitionsabzugsbetrag (IAB)

**DE-OPT-3: Timing -- Investitionsabzugsbetrag (IAB)**

| Field | Detail |
| --- | --- |
| **Category** | Timing |
| **Trigger** | Planned qualifying depreciable movable fixed assets and a relevant profit that does not exceed EUR 200,000 under the actual statutory computation, not strictly below that amount. [Official source](https://www.gesetze-im-internet.de/estg/__7g.html) |
| **Calculation** | IAB may deduct up to 50% of expected qualifying cost, subject to the statutory outstanding-per-business EUR 200,000 cap across the relevant deduction/current-plus-prior-three-year window. Model subsequent addition, basis reduction/depreciation and reversal; the current reduction is not all permanent savings. The investment must be matched within the statutory following-three-financial-year period. [Official source](https://www.gesetze-im-internet.de/estg/__7g.html) |
| **Materiality** | > EUR 200 tax savings |
| **Confidence** | T1 only for fully evidenced law/facts and mechanical comparison; otherwise T2/held. Neither confers accountant approval. |
| **Reviewer flag** | Read actual eligible property, renting or almost-exclusive domestic business-use and subsequent-year conditions. Do not turn almost-exclusive use into an unverified strict greater-than-ninety boundary. Failed investment/use can trigger corrective assessments and interest; AO 238(1a) gives section 233a interest 0.15% per month/1.8% yearly from 2019, not the old 6% blanket figure. Actual interest start and exception still need calculation. [Official source](https://www.gesetze-im-internet.de/estg/__7g.html) / [Official source](https://www.gesetze-im-internet.de/ao_1977/__238.html) |
| **Output** | Reviewer: report this check's actual year, facts, source and full baseline/alternative comparison using Part B. State held conditions, permanent versus timing effect, costs, deadline and required professional decision; do not implement an unresolved alternative. |

#### DE-OPT-4: Election -- Kleinunternehmer opt-in/opt-out

**DE-OPT-4: Election -- Kleinunternehmer opt-in/opt-out**

| Field | Detail |
| --- | --- |
| **Category** | Elections |
| **Trigger** | Determine prior-year and current-year actual statutory turnover, exemption eligibility and election history. Prior-year limit EUR 25,000 and current-year EUR 100,000 are distinct; proximity to one threshold is not a free choice after a statutory breach. [Official source](https://www.gesetze-im-internet.de/ustg_1980/__19.html) |
| **Calculation** | Compare actual VAT due on taxable transactions, legally deductible input VAT, price contracts/customer recovery, transition/capital adjustments and administration. Not all supplies use the standard rate and not all input tax is recoverable; B2B status does not guarantee no pricing effect. [Official source](https://www.gesetze-im-internet.de/ustg_1980/__19.html) |
| **Materiality** | > EUR 200 annual net benefit |
| **Confidence** | T1 only for fully evidenced law/facts and mechanical comparison; otherwise T2/held. Neither confers accountant approval. |
| **Reviewer flag** | Check waiver under the current section 19(3), binding for at least five calendar years, actual effective filing/withdrawal deadline and re-entry conditions. Old section 19(2) citation is stale. Hold exact crossing/start-up supply treatment if the governing rule is not read. [Official source](https://www.gesetze-im-internet.de/ustg_1980/__19.html) |
| **Output** | Reviewer: report this check's actual year, facts, source and full baseline/alternative comparison using Part B. State held conditions, permanent versus timing effect, costs, deadline and required professional decision; do not implement an unresolved alternative. |

#### DE-OPT-5: Unclaimed -- home office deduction (Homeoffice-Pauschale)

**DE-OPT-5: Unclaimed -- home office deduction (Homeoffice-Pauschale)**

| Field | Detail |
| --- | --- |
| **Category** | Credits/reliefs not claimed |
| **Trigger** | User works from home AND has not claimed the Homeoffice-Pauschale or hauesliches Arbeitszimmer |
| **Calculation** | Current EStG 4(5)6c allows the qualifying daily amount EUR 6 capped EUR 1,260, derived maximum 210 days; actual predominant-home/no-first-workplace conditions and the permanent-no-other-workplace exception apply. Under 6b an eligible office at the centre of the entire activity can use actual costs or the EUR 1,260 annual amount with monthly reduction where conditions lapse. The annual amount is not an alternative for an office away from the centre. [Official source](https://www.gesetze-im-internet.de/estg/__4.html) |
| **Materiality** | > EUR 100 tax savings |
| **Confidence** | T1 only for fully evidenced law/facts and mechanical comparison; otherwise T2/held. Neither confers accountant approval. |
| **Reviewer flag** | No double daily/room deduction or disallowed accommodation overlap. Employee standard-expense interactions and self-employed profit deductions differ: an employee expense allowance is not a self-employed threshold. Confirm actual workdays/office facts and current employee allowance if that scenario is used; do not subtract the allowance mechanically from every homeworking claim. [Official source](https://www.gesetze-im-internet.de/estg/__4.html) |
| **Output** | Reviewer: report this check's actual year, facts, source and full baseline/alternative comparison using Part B. State held conditions, permanent versus timing effect, costs, deadline and required professional decision; do not implement an unresolved alternative. |

### 3.4 Australia (AU) -- 5 checks

#### AU-OPT-1: Superannuation contribution room

**AU-OPT-1: Superannuation contribution room**

| Field | Detail |
| --- | --- |
| **Category** | Retirement contributions |
| **Trigger** | User has not maximised concessional (pre-tax) super contributions |
| **Calculation** | Separate 2025-2026 ordinary concessional cap AUD 30,000 from 2026-2027 AUD 32,500. Remaining room counts all employer/salary-sacrifice/deducted personal contributions across funds and eligible carry-forward. Recompute actual personal tax reduction less fund contributions tax, additional Division 293 and effects/costs, rather than subtracting a percentage as though it were a cash amount. [ATO indexed cap excerpt](https://www.ato.gov.au/api/public/content/0-af5a46ad-7287-431c-be8e-4a0c9bbc5fc1) / [Division 293](https://www.ato.gov.au/api/public/content/0-6c3220ce-b973-4514-84e0-0f9f28c4d0a7) |
| **Materiality** | > AUD 150 tax savings |
| **Confidence** | T1 only for fully evidenced law/facts and mechanical comparison; otherwise T2/held. Neither confers accountant approval. |
| **Reviewer flag** | Verify total super balance at the relevant preceding year end, actual unused carry-forward from the previous five years, employer contributions, age/work/deduction-notice and fund timing, and legal preservation/access conditions. Division 293 uses its own income and low-tax-contributions definition, taxes the lesser taxable excess/contributions at 15% over AUD 250,000, and is not automatically an extra percentage on the whole contribution. Exact personal eligibility remains held. [Official source](https://www.ato.gov.au/api/public/content/0-6c3220ce-b973-4514-84e0-0f9f28c4d0a7) |
| **Output** | Reviewer: report this check's actual year, facts, source and full baseline/alternative comparison using Part B. State held conditions, permanent versus timing effect, costs, deadline and required professional decision; do not implement an unresolved alternative. |

#### AU-OPT-2: Entity structure -- company vs sole trader

**AU-OPT-2: Entity structure -- company vs sole trader**

| Field | Detail |
| --- | --- |
| **Category** | Entity structure |
| **Trigger** | Sole trader with net business income > AUD 90,000 |
| **Calculation** | Recompute actual sole-trader tax/levy against company tax, salary, payroll/super and eventual dividend/franking interaction, extraction timing and actual costs. The lower company rate 25% requires actual base-rate-entity eligibility including the passive-income condition; otherwise the ordinary full company rate is 30%. Retention is a deferral comparison and not proof of a lower lifetime rate. [Official source](https://www.ato.gov.au/api/public/content/0-11c3cbc8-adf6-4118-bc2c-0c5044452da1) |
| **Materiality** | > AUD 3,000 net annual savings |
| **Confidence** | T1 only for fully evidenced law/facts and mechanical comparison; otherwise T2/held. Neither confers accountant approval. |
| **Reviewer flag** | Test actual current turnover and passive-income definitions, PSI attribution, Division 7A, capital-gains treatment, funds available for distributions and sourced costs. Do not use old ASIC/accountancy estimates as verified figures or assume a lower corporation rate from turnover alone. [Official source](https://www.ato.gov.au/api/public/content/0-11c3cbc8-adf6-4118-bc2c-0c5044452da1) |
| **Output** | Reviewer: report this check's actual year, facts, source and full baseline/alternative comparison using Part B. State held conditions, permanent versus timing effect, costs, deadline and required professional decision; do not implement an unresolved alternative. |

#### AU-OPT-3: Timing -- prepayment of deductible expenses

**AU-OPT-3: Timing -- prepayment of deductible expenses**

| Field | Detail |
| --- | --- |
| **Category** | Timing |
| **Trigger** | A taxpayer eligible for the actual prepayment concession, including an entity that would be a small business if its turnover threshold were AUD 50 million; the old exclusive AUD 10 million screen misses eligible cases. [Official source](https://www.ato.gov.au/api/public/content/0-93638c4a-a53a-4d5b-9dca-85b8530febc4) |
| **Calculation** | For qualifying expenditure, the eligible service period must be no more than twelve months and finish by the end of the following income year. Retain conditional prepayment examples of insurance, professional subscriptions and rent, each subject to actual deductibility. Compare full deductions/tax across both periods, cash paid/funding and future reversal; a brought-forward deduction is not automatically permanent tax saved. [Official source](https://www.ato.gov.au/api/public/content/0-93638c4a-a53a-4d5b-9dca-85b8530febc4) |
| **Materiality** | > AUD 150 tax savings |
| **Confidence** | T1 only for fully evidenced law/facts and mechanical comparison; otherwise T2/held. Neither confers accountant approval. |
| **Reviewer flag** | Confirm actual expense deductibility, eligible taxpayer, paid/incurred timing under its method, service period, excluded expenditure/tax-shelter and any special employee/super rules. Do not rely on a blanket cannot-prepay list or merely an invoice date. The source read establishes concession scope, not every statutory exception. [Official source](https://www.ato.gov.au/api/public/content/0-93638c4a-a53a-4d5b-9dca-85b8530febc4) |
| **Output** | Reviewer: report this check's actual year, facts, source and full baseline/alternative comparison using Part B. State held conditions, permanent versus timing effect, costs, deadline and required professional decision; do not implement an unresolved alternative. |

#### AU-OPT-4: Election -- simplified depreciation (instant asset write-off)

**AU-OPT-4: Election -- simplified depreciation (instant asset write-off)**

| Field | Detail |
| --- | --- |
| **Category** | Elections |
| **Trigger** | User is a small business entity AND has acquired depreciable assets |
| **Calculation** | For assets first used/installed ready from July 2026, current official law/guidance provides immediate deduction for eligible cost strictly less than AUD 20,000 for qualifying small businesses with aggregated turnover below AUD 10 million. Apply actual taxable-use share, excluded assets and pooling/second-element rules; compare current and later ordinary deductions rather than assuming a permanent saving. [Official source](https://www.ato.gov.au/api/public/content/0-cd3490b1-151e-442d-9571-b0d481b340e0) / [2026 Act Schedule 2](https://www.legislation.gov.au/C2026A00071/asmade/2026-08-26/text/original/epub/OEBPS/document_1/document_1.html) |
| **Materiality** | > AUD 200 tax savings |
| **Confidence** | T1 only for fully evidenced law/facts and mechanical comparison; otherwise T2/held. Neither confers accountant approval. |
| **Reviewer flag** | Verify enacted rule, acquisition/use dates, cost not merely business fraction for the threshold, actual regime/election and pool treatment. Temporary full expensing ended June 2023 and cannot be used for newly qualifying 2026 assets. This is not permission to apply a budget announcement without enacted support. [Official source](https://www.ato.gov.au/api/public/content/0-62fc72e5-417c-4afc-ab6d-a59f6f8a1209) / [Official source](https://www.legislation.gov.au/C2026A00071/asmade/2026-08-26/text/original/epub/OEBPS/document_1/document_1.html) |
| **Output** | Reviewer: report this check's actual year, facts, source and full baseline/alternative comparison using Part B. State held conditions, permanent versus timing effect, costs, deadline and required professional decision; do not implement an unresolved alternative. |

#### AU-OPT-5: Unclaimed -- private health insurance offset

**AU-OPT-5: Unclaimed -- private health insurance offset**

| Field | Detail |
| --- | --- |
| **Category** | Credits/reliefs not claimed |
| **Trigger** | Actual eligible private-health policy and premium components/dates, family status, oldest covered person age and income for surcharge purposes; no old single-income-only eligibility shortcut. |
| **Calculation** | Use dated official tiers, not old 2024-2025 percentages. For 2026-2027 single boundaries are AUD 105,000/123,000/164,000, family 210,000/246,000/328,000 before actual child adjustments. For premiums July 2026 to March 2027 and oldest covered person under 65, rates are 24.118%/16.079%/8.038%/zero. Apply actual eligible premium and reconcile insurer reductions already received; older ages/dates need their actual table, not these rates. [ATO indexed table excerpt](https://www.ato.gov.au/api/public/content/0-e0e9fe64-117a-4024-b3d9-770218d1d67f) |
| **Materiality** | > AUD 150 |
| **Confidence** | T1 only for fully evidenced law/facts and mechanical comparison; otherwise T2/held. Neither confers accountant approval. |
| **Reviewer flag** | Reconcile actual insurer statement/benefit codes, income, family/child and age/date changes, excluded premium loading/components and amounts already claimed. Claim only the remaining entitlement, not the full rebate again. Later April 2027 rebate rates and complete older-age/eligibility rules are not certified here. [Official source](https://www.ato.gov.au/api/public/content/0-e0e9fe64-117a-4024-b3d9-770218d1d67f) |
| **Output** | Reviewer: report this check's actual year, facts, source and full baseline/alternative comparison using Part B. State held conditions, permanent versus timing effect, costs, deadline and required professional decision; do not implement an unresolved alternative. |

### 3.5 Canada (CA) -- 5 checks

#### CA-OPT-1: RRSP contribution room

**CA-OPT-1: RRSP contribution room**

| Field | Detail |
| --- | --- |
| **Category** | Retirement contributions |
| **Trigger** | User has unused RRSP contribution room |
| **Calculation** | For 2026 annual RRSP dollar limit is CAD 33,810, not the 2025 CAD 32,490. New room starts from the lesser of eighteen-percent prior earned income and that annual limit, adjusted for actual pension/PSPA/PAR and unused room; deductible room is not the same as unmade contribution capacity if unused contributions already exist. Read actual NOA/reassessment/T1028 and recompute federal/provincial tax and credits, not a nationwide combined rate. [CRA 2026 indexed table](https://www.canada.ca/en/revenue-agency/services/tax/registered-plans-administrators/pspa/mp-rrsp-dpsp-tfsa-limits-ympe.html) / [Official source](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/rrsps-related-plans/contributing-a-rrsp-prpp/contributions-affect-your-rrsp-prpp-deduction-limit.html) / [Official source](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/rrsps-related-plans/contributing-a-rrsp-prpp/where-you-find-your-rrsp-prpp-deduction-limit.html) |
| **Materiality** | > CAD 150 tax savings |
| **Confidence** | T1 only for fully evidenced law/facts and mechanical comparison; otherwise T2/held. Neither confers accountant approval. |
| **Reviewer flag** | Reconcile already-made but undeducted contributions before recommending more cash. General excess-contribution tax is 1% monthly beyond the CAD 2,000 cushion under applicable conditions; that cushion is not deductible contribution room. Latest CRA 2025-cycle guide gives actual eligible dates, so do not assume every deadline is March 1. Confirm actual 2026 deduction-period deadline and spousal attribution before use. [Official source](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/rrsps-related-plans/contributing-a-rrsp-prpp/contributions-affect-your-rrsp-prpp-deduction-limit.html) |
| **Output** | Reviewer: report this check's actual year, facts, source and full baseline/alternative comparison using Part B. State held conditions, permanent versus timing effect, costs, deadline and required professional decision; do not implement an unresolved alternative. |

#### CA-OPT-2: Entity structure -- incorporation

**CA-OPT-2: Entity structure -- incorporation**

| Field | Detail |
| --- | --- |
| **Category** | Entity structure |
| **Trigger** | Self-employed with net business income > CAD 80,000 |
| **Calculation** | Compute actual province/year personal tax/CPP against corporation eligibility, active-business/small-business limits, associated-company/passive-income adjustments, salary/payroll and dividend/extraction tax plus actual costs. Do not use one illustrative combined small-business rate for all provinces. Show retained-profit deferral separately from permanent net savings. Current federal/provincial rates and actual entity eligibility must be read before a numerical incorporation recommendation. |
| **Materiality** | > CAD 3,000 net annual savings |
| **Confidence** | T1 only for fully evidenced law/facts and mechanical comparison; otherwise T2/held. Neither confers accountant approval. |
| **Reviewer flag** | Review CCPC/PSB/TOSI status, business-limit allocation, integration, CPP and salary/dividend/cash needs. Obtain real formation/accounting quotes and recognise costs at their actual times. The old CAD 80,000 screen and net-benefit floor remain internal priorities, not a statutory safe harbour. Detailed current corporation/PSB/TOSI computation is held for the appropriate country method. |
| **Output** | Reviewer: report this check's actual year, facts, source and full baseline/alternative comparison using Part B. State held conditions, permanent versus timing effect, costs, deadline and required professional decision; do not implement an unresolved alternative. |

#### CA-OPT-3: Timing -- fiscal year-end selection

**CA-OPT-3: Timing -- fiscal year-end selection**

| Field | Detail |
| --- | --- |
| **Category** | Timing |
| **Trigger** | User is a sole proprietor considering or using an off-calendar fiscal year-end |
| **Calculation** | Use the actual alternative-fiscal-period election and T1139 additional-business-income calculation, including prior-year reversal and actual future income. It is not a generic section 34.1 reserve or a proven tax-saving election. Latest 2025 form read describes the continuing annual additional-income computation;2026 form specifics remain to be confirmed. [Actual 2025 T1139](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t1139/t1139-25e.pdf) |
| **Materiality** | > CAD 200 first-year timing benefit |
| **Confidence** | T1 only for fully evidenced law/facts and mechanical comparison; otherwise T2/held. Neither confers accountant approval. |
| **Reviewer flag** | Check eligible individual/all-individual partnership, first-return election timing, GST/HST impacts and cancellation. The actual form excludes specified nested/professional-corporation partnerships, tax-shelter cases and re-election after cancellation. No unsupported post 2017 rule or first-year-only cash advantage is certified. [Official source](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t1139/t1139-25e.pdf) |
| **Output** | Reviewer: report this check's actual year, facts, source and full baseline/alternative comparison using Part B. State held conditions, permanent versus timing effect, costs, deadline and required professional decision; do not implement an unresolved alternative. |

#### CA-OPT-4: Election -- CCA classes and immediate expensing

**CA-OPT-4: Election -- CCA classes and immediate expensing**

| Field | Detail |
| --- | --- |
| **Category** | Elections |
| **Trigger** | User has acquired depreciable property AND is a CCPC or eligible individual |
| **Calculation** | Determine asset class, actual available-for-use/acquisition dates, taxpayer, business use, designated-property/associated-group limits and enacted current rules. Compare lawful current CCA/immediate deduction with future deductions/recapture and total tax. The historical general designated-property CAD 1.5 million measure is not assumed available for every 2026 purchase. Newer class-specific incentives and proposals require separate enacted-law checks before amounts are used. |
| **Materiality** | > CAD 200 tax savings |
| **Confidence** | T1 only for fully evidenced law/facts and mechanical comparison; otherwise T2/held. Neither confers accountant approval. |
| **Reviewer flag** | Obtain current Income Tax Regulations 1100/1104 and applicable annual amendments for the particular property; verify old temporary-measure cutoffs and new class-specific rules separately. No full deduction or absence of half-year rule is certified simply from the asset cost, CCPC status or a prior announcement. The comparison workpaper and missing-law task remain required even when its final number is held. |
| **Output** | Reviewer: report this check's actual year, facts, source and full baseline/alternative comparison using Part B. State held conditions, permanent versus timing effect, costs, deadline and required professional decision; do not implement an unresolved alternative. |

#### CA-OPT-5: Unclaimed -- business-use-of-home expenses

**CA-OPT-5: Unclaimed -- business-use-of-home expenses**

| Field | Detail |
| --- | --- |
| **Category** | Credits/reliefs not claimed |
| **Trigger** | User works from home AND has not claimed business-use-of-home expenses |
| **Calculation** | Calculate actual reasonable space/time apportionment, direct/indirect supported expenses, prior carryforward and the business-income limit. Unused qualifying amounts may carry forward subject to continued eligibility; no current business loss is created/increased. Do not apply a temporary employee flat-rate method to self-employment. [Official source](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/report-business-income-expenses/completing-form-t2125/business-use-home-expenses.html) |
| **Materiality** | > CAD 150 tax savings |
| **Confidence** | T1 only for fully evidenced law/facts and mechanical comparison; otherwise T2/held. Neither confers accountant approval. |
| **Reviewer flag** | Qualify by principal place of business OR exclusive income-earning space used regularly/ongoingly to meet clients, customers or patients. Shared principal-place space needs supported time apportionment. Avoid duplicate T2125 deductions; CCA can create recapture/capital-gain and residence-exemption issues, so compare actual property facts rather than universally recommending it. [Official source](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/report-business-income-expenses/completing-form-t2125/business-use-home-expenses.html) |
| **Output** | Reviewer: report this check's actual year, facts, source and full baseline/alternative comparison using Part B. State held conditions, permanent versus timing effect, costs, deadline and required professional decision; do not implement an unresolved alternative. |

### 3.6 India (IN) -- 5 checks

#### IN-OPT-1: Section 80C and NPS deductions

**IN-OPT-1: Section 80C and NPS deductions**

| Field | Detail |
| --- | --- |
| **Category** | Retirement / savings contributions |
| **Trigger** | For the explicitly latest FY 2025-2026/AY 2026-2027 bridge only, establish actual old-regime eligibility/election and eligible payments before computing old-section deduction room. Current tax-year 2026-2027 successor-law and filing references are held. [Official source](https://www.incometax.gov.in/iec/foportal/help/individual/return-applicable-1) |
| **Calculation** | Latest AY 2026-2027 official guide retains the combined old-section 80C/80CCC/80CCD(1) INR 150,000 limit and separate qualifying 80CCD(1B) INR 50,000. Recompute both full regimes including cess/surcharge, caps, already-used room and other deductions; avoid double-counting the same contribution. These are latest-cycle figures, not certified 2026-2027 successor-Act provisions. [Official source](https://www.incometax.gov.in/iec/foportal/help/individual/return-applicable-1) |
| **Materiality** | > INR 10,000 tax savings |
| **Confidence** | T1 only for fully evidenced law/facts and mechanical comparison; otherwise T2/held. Neither confers accountant approval. |
| **Reviewer flag** | Verify old/default-regime deduction availability, employer-NPS exception under its actual limit, residence, payment/instrument and election evidence; contribution knowledge alone does not establish a deductible saving. Successor-law equivalents and deadlines for the new tax year remain held. [Official source](https://www.incometax.gov.in/iec/foportal/help/individual/return-applicable-1) |
| **Output** | Reviewer: report this check's actual year, facts, source and full baseline/alternative comparison using Part B. State held conditions, permanent versus timing effect, costs, deadline and required professional decision; do not implement an unresolved alternative. |

#### IN-OPT-2: Old vs new tax regime comparison

**IN-OPT-2: Old vs new tax regime comparison**

| Field | Detail |
| --- | --- |
| **Category** | Elections |
| **Trigger** | User has not compared old and new tax regimes |
| **Calculation** | Recompute each legally available regime using the exact year, income heads, rebate, deduction exemptions, surcharge/cess and restrictions. No universal deduction break-even exists; it depends on the whole computation. Label the currently read guide AY 2026-2027 and hold a successor-year recommendation until its law is read. [Official source](https://www.incometax.gov.in/iec/foportal/help/individual/return-applicable-1) |
| **Materiality** | > INR 10,000 difference |
| **Confidence** | T1 only for fully evidenced law/facts and mechanical comparison; otherwise T2/held. Neither confers accountant approval. |
| **Reviewer flag** | The old statement that self-employed taxpayers freely switch annually is wrong. Latest guide distinguishes non-business annual ITR choice from business/profession Form 10-IEA by the return due date, with re-entry to default available only once in a subsequent assessment year. Obtain actual election history; confirm successor-law form/transitional rules for tax-year 2026-2027 rather than relabelling old sections. [Official source](https://www.incometax.gov.in/iec/foportal/help/individual/return-applicable-1) |
| **Output** | Reviewer: report this check's actual year, facts, source and full baseline/alternative comparison using Part B. State held conditions, permanent versus timing effect, costs, deadline and required professional decision; do not implement an unresolved alternative. |

#### IN-OPT-3: Timing -- advance tax optimisation

**IN-OPT-3: Timing -- advance tax optimisation**

| Field | Detail |
| --- | --- |
| **Category** | Timing |
| **Trigger** | User pays advance tax AND has seasonal or variable income |
| **Calculation** | Build the actual required cumulative instalment schedule and due-date tax base, subtract real withholding/advance payments and test legally available income-specific exceptions before calculating interest. Seasonal income alone is not permission to spread instalments by realised cash; distinguish interest avoided from a reduction in final tax. Current successor-year section numbers/rates and all exceptions remain held. |
| **Materiality** | > INR 10,000 interest savings |
| **Confidence** | T1 only for fully evidenced law/facts and mechanical comparison; otherwise T2/held. Neither confers accountant approval. |
| **Reviewer flag** | Keep the latest-cycle presumptive advance-tax enquiry: official guide states section 44ADA taxpayers pay the whole qualifying advance-tax amount by March 15 and actual late payments can attract sections 234B/234C. The source guide/form year must remain explicit; do not transplant that reference or an unverified universal quarter-of-gain exemption into tax-year 2026-2027. [Latest ITR 4FAQ, dated cycle](https://www.incometax.gov.in/iec/foportal/help/e-filing-itr4-form-sugam-faq) |
| **Output** | Reviewer: report this check's actual year, facts, source and full baseline/alternative comparison using Part B. State held conditions, permanent versus timing effect, costs, deadline and required professional decision; do not implement an unresolved alternative. |

#### IN-OPT-4: Entity structure -- presumptive vs regular

**IN-OPT-4: Entity structure -- presumptive vs regular**

| Field | Detail |
| --- | --- |
| **Category** | Entity structure |
| **Trigger** | Latest FY 2025-2026/AY 2026-2027: verify resident eligible individual/non-LLP professional, specified profession, gross receipts and statutory cash share. The higher INR 75lakh limit uses the actual at-most-five-percent cash test; otherwise INR 50lakh. Digital receipts alone are not the legal test. [Official source](https://www.incometax.gov.in/iec/foportal/help/e-filing-itr4-form-sugam-faq) / [Official source](https://www.incometax.gov.in/iec/foportal/help/individual/return-applicable-1) |
| **Calculation** | Compare supported presumptive professional income with actual lawful business profit, all taxes, real compliance/audit/bookkeeping costs and record obligations. Presumptive method does not permit hiding higher actual income or claiming excluded expenses again. ITR 4 eligibility is separate from substantive presumptive eligibility. Retain income and payment evidence even when statutory detailed-books relief applies. [Official source](https://www.incometax.gov.in/iec/foportal/help/e-filing-itr4-form-sugam-faq) |
| **Materiality** | > INR 10,000 difference |
| **Confidence** | T1 only for fully evidenced law/facts and mechanical comparison; otherwise T2/held. Neither confers accountant approval. |
| **Reviewer flag** | The old five-year lock was asserted for 44ADA without law and is not a usable rule: do not import the distinct 44AD restriction by analogy. Obtain actual governing law/audit and income conditions if declaring below presumptive income. Current successor-Act tax-year 2026-2027 thresholds, re-entry and audit provisions remain held rather than guessed. [Official source](https://www.incometax.gov.in/iec/foportal/help/individual/return-applicable-1) |
| **Output** | Reviewer: report this check's actual year, facts, source and full baseline/alternative comparison using Part B. State held conditions, permanent versus timing effect, costs, deadline and required professional decision; do not implement an unresolved alternative. |

#### IN-OPT-5: Unclaimed -- section 80D health insurance

**IN-OPT-5: Unclaimed -- section 80D health insurance**

| Field | Detail |
| --- | --- |
| **Category** | Credits/reliefs not claimed |
| **Trigger** | User pays health insurance premiums AND is under old tax regime AND has not claimed section 80D |
| **Calculation** | Latest AY 2026-2027 guide: eligible self/spouse/dependent-child and parent categories have separate INR 25,000 limits, potentially INR 50,000 for the applicable senior-person category. Preventive check-up INR 5,000 is inside, not on top of, the category limit. Test actual premium/medical expenditure, regime, payments and eligible people; recompute tax without double-counting. [Official source](https://www.incometax.gov.in/iec/foportal/help/individual/return-applicable-1) |
| **Materiality** | > INR 10,000 tax savings |
| **Confidence** | T1 only for fully evidenced law/facts and mechanical comparison; otherwise T2/held. Neither confers accountant approval. |
| **Reviewer flag** | Check senior status, separate parent limit, actual payment-mode exception for preventive check-ups and whether premiums were already deducted. The cash restriction and successor-year rules require primary-law confirmation before a final claim; the guide read establishes latest-cycle categories/limits, not every exception. [Official source](https://www.incometax.gov.in/iec/foportal/help/individual/return-applicable-1) |
| **Output** | Reviewer: report this check's actual year, facts, source and full baseline/alternative comparison using Part B. State held conditions, permanent versus timing effect, costs, deadline and required professional decision; do not implement an unresolved alternative. |

### 3.7 Spain (ES) -- 5 checks

#### ES-OPT-1: Plan de pensiones contribution room

**ES-OPT-1: Plan de pensiones contribution room**

| Field | Detail |
| --- | --- |
| **Category** | Retirement contributions |
| **Trigger** | User has not maximised pension plan (plan de pensiones) contributions |
| **Calculation** | Current LIRPF 52 uses the lesser of thirty-percent of individual net employment/economic-activity income and the relevant monetary amount: general EUR 1,500, qualifying employer/worker increment up to EUR 8,500, qualifying self-employed increments up to EUR 4,250, with the combined increment cap EUR 8,500. Compute actual instrument/contribution limits and worker matching formula; not every employer contribution unlocks the whole increment. Recompute full IRPF and future withdrawal tax. [BOE LIRPF 52 and DA 16](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764) |
| **Materiality** | > EUR 100 tax savings |
| **Confidence** | T1 only for fully evidenced law/facts and mechanical comparison; otherwise T2/held. Neither confers accountant approval. |
| **Reviewer flag** | Validate actual plan/PPES or other qualifying instrument, employer/worker matching and income conditions, carryovers and general/financial contribution limits separately. The self-employed combined EUR 5,750 is derived from general plus eligible increment, not an unconditional personal entitlement. [Official source](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764) |
| **Output** | Reviewer: report this check's actual year, facts, source and full baseline/alternative comparison using Part B. State held conditions, permanent versus timing effect, costs, deadline and required professional decision; do not implement an unresolved alternative. |

#### ES-OPT-2: Entity structure -- Sociedad Limitada vs autónomo

**ES-OPT-2: Entity structure -- Sociedad Limitada vs autónomo**

| Field | Detail |
| --- | --- |
| **Category** | Entity structure |
| **Trigger** | Autónomo with net income > EUR 60,000 |
| **Calculation** | Use actual regional/common-or-foral IRPF, RETA, company eligibility and salary/dividend/extraction taxes plus evidenced costs. For periods beginning 2026 AEAT table gives general 25%, qualifying micro-company first EUR 50,000 base 19% and remainder 21%, qualifying reduced-size 23%, qualifying new entities 15%; do not use the old universal company 25% or attach a fictional income cap to the new-entity rate. Actual qualifying period/exclusions still need the law. [AEAT 2026 table](https://sede.agenciatributaria.gob.es/Sede/impuesto-sobre-sociedades/que-base-imponible-se-determina-sociedades/tipo-impositivo.html) |
| **Materiality** | > EUR 2,000 net annual savings |
| **Confidence** | T1 only for fully evidenced law/facts and mechanical comparison; otherwise T2/held. Neither confers accountant approval. |
| **Reviewer flag** | Confirm actual new-entity/emerging-company rules and prior/group activity, director/social classification, salary/formalities, capital funding and creditor reserves, withholding, regional savings rates and costs. The old monthly RETA range, combined personal rate, dividend band and quoted formation/accountancy prices are not verified current law. No automatic mandatory director salary or capital recommendation is made. [Official source](https://sede.agenciatributaria.gob.es/Sede/impuesto-sobre-sociedades/que-base-imponible-se-determina-sociedades/tipo-impositivo.html) |
| **Output** | Reviewer: report this check's actual year, facts, source and full baseline/alternative comparison using Part B. State held conditions, permanent versus timing effect, costs, deadline and required professional decision; do not implement an unresolved alternative. |

#### ES-OPT-3: Timing -- Modelo 130 offset planning

**ES-OPT-3: Timing -- Modelo 130 offset planning**

| Field | Detail |
| --- | --- |
| **Category** | Timing |
| **Trigger** | User files quarterly Modelo 130 AND has seasonal income |
| **Calculation** | Follow actual cumulative Form 130 instructions: general twenty-percent of positive cumulative result, actual special territorial rate, prior payments/withholding and further form adjustments. Recompute each box and annual final tax, distinguishing cash timing from permanent savings. A negative fourth-quarter return is not an immediate refund of prior instalments. [Official source](https://sede.agenciatributaria.gob.es/Sede/impuestos-tasas/impuesto-sobre-renta-personas-fisicas/modelo-130-irpf______esionales-estimacion-directa-fraccionado_/instrucciones.html) |
| **Materiality** | > EUR 200 timing benefit |
| **Confidence** | T1 only for fully evidenced law/facts and mechanical comparison; otherwise T2/held. Neither confers accountant approval. |
| **Reviewer flag** | Actual instructions route a qualifying negative first/second/third-quarter amount to later positive instalments of the same year within limits; a negative fourth quarter uses Negativa. Do not invent a cash refund, transfer an unpaid negative as tax paid, or move accrual expenses merely to a convenient bank-payment quarter. Reconcile annual return and real payments. [Official source](https://sede.agenciatributaria.gob.es/Sede/impuestos-tasas/impuesto-sobre-renta-personas-fisicas/modelo-130-irpf______esionales-estimacion-directa-fraccionado_/instrucciones.html) |
| **Output** | Reviewer: report this check's actual year, facts, source and full baseline/alternative comparison using Part B. State held conditions, permanent versus timing effect, costs, deadline and required professional decision; do not implement an unresolved alternative. |

#### ES-OPT-4: Election -- RETA contribution base optimisation

**ES-OPT-4: Election -- RETA contribution base optimisation**

| Field | Detail |
| --- | --- |
| **Category** | Elections |
| **Trigger** | User is autónomo under the new cuota system (since Jan 2023) |
| **Calculation** | Use actual 2026 net-return definition, eligible contribution-base range, chosen base, rates, time in force and annual regularisation notice. Compare provisional cash change separately from final legally required liability and actual benefit/pension effects. A lower declared estimate is not a permanent saving or permission to underdeclare income. [Social Security 2026 guide](https://portal.seg-social.gob.es/wps/portal/importass/importass/Colectivos/trabajo%2Bautonomo/guia) |
| **Materiality** | > EUR 200 annual difference |
| **Confidence** | T1 only for fully evidenced law/facts and mechanical comparison; otherwise T2/held. Neither confers accountant approval. |
| **Reviewer flag** | Base adjustments are available up to six times per year, with the relevant effective dates in March/May/July/September/November 2026 and January 2027, not six-month windows. Do not promise every regularisation occurs in October or that every higher provisional base buys extra rights; apply actual final-band/refund/retention conditions and notice/payment deadline. [Official source](https://portal.seg-social.gob.es/wps/portal/importass/importass/Colectivos/trabajo%2Bautonomo/guia) |
| **Output** | Reviewer: report this check's actual year, facts, source and full baseline/alternative comparison using Part B. State held conditions, permanent versus timing effect, costs, deadline and required professional decision; do not implement an unresolved alternative. |

#### ES-OPT-5: Unclaimed -- gastos de dificil justificacion (5% deduction)

**ES-OPT-5: Unclaimed -- gastos de dificil justificacion (5% deduction)**

| Field | Detail |
| --- | --- |
| **Category** | Credits/reliefs not claimed |
| **Trigger** | User is under estimacion directa simplificada AND has not claimed the 5% deduction |
| **Calculation** | Use the actual simplified direct-estimation positive net-result base before this adjustment, not a second subtraction of expenses. General latest guide supplies 5% capped EUR 2,000; the 2026-specific Ceuta provision read separately is 10%, not a countrywide increase. Recompute tax and actual incompatibilities rather than a fixed marginal-rate estimate. [AEAT current scoped guide](https://sede.agenciatributaria.gob.es/Sede/irpf/empresarios-individuales-profesionales/regimenes-determinar-rendimiento-actividad/estimacion-directa-simplificada.html) |
| **Materiality** | > EUR 100 tax savings |
| **Confidence** | T1 only for fully evidenced law/facts and mechanical comparison; otherwise T2/held. Neither confers accountant approval. |
| **Reviewer flag** | Check actual simplified-method eligibility, territory/year and incompatible reduction, actual provisions versus hard-to-justify allowance and cap; no double deduction. Do not say automatic only because a row was absent from an uploaded summary. The common and special 2026 source provisions are read separately; final client regime remains evidenced. [Official source](https://sede.agenciatributaria.gob.es/Sede/irpf/empresarios-individuales-profesionales/regimenes-determinar-rendimiento-actividad/estimacion-directa-simplificada.html) |
| **Output** | Reviewer: report this check's actual year, facts, source and full baseline/alternative comparison using Part B. State held conditions, permanent versus timing effect, costs, deadline and required professional decision; do not implement an unresolved alternative. |

### 3.8 Malta (MT) -- 5 checks

#### MT-OPT-1: Voluntary pension contribution

**MT-OPT-1: Voluntary pension contribution**

| Field | Detail |
| --- | --- |
| **Category** | Retirement contributions |
| **Trigger** | User has not maximised voluntary occupational pension or personal retirement scheme contributions |
| **Calculation** | For a qualifying personal retirement scheme, current SL 123.163 rule 8 gives 25% of qualifying contributions in the preceding basis year, credit capped EUR 750 per assessment year; EUR 3,000 contributing maximum for that credit is derived, not an extra deduction. Calculate actual credit already used and remaining liability/conditions without assuming two schemes double the allowance. Latest occupational-credit guidance read is explicitly basis 2025/YA 2026. [Rules 4 to 8](https://legislation.mt/getpdf/60250ba78f58ac184473f786) / [YA 2026 booklet page 35](https://mtca.gov.mt/docs/default-source/documents/personal-tax/individual/tax-return-booklet-individuals/mtca-tax-booklet-2026-eng-17-03.pdf) |
| **Materiality** | > EUR 100 tax credit |
| **Confidence** | T1 only for fully evidenced law/facts and mechanical comparison; otherwise T2/held. Neither confers accountant approval. |
| **Reviewer flag** | Check actual qualifying individual, age, Malta domicile/residence and application declarations, administrator certificate/reporting and scheme conditions under rules 4 to 7. Check current occupational rules, interaction, tax-credit nonrefund/carryforward conditions and actual credit already claimed before certifying the available cash benefit; regulation by itself does not satisfy every tax test. [Official source](https://legislation.mt/getpdf/60250ba78f58ac184473f786) |
| **Output** | Reviewer: report this check's actual year, facts, source and full baseline/alternative comparison using Part B. State held conditions, permanent versus timing effect, costs, deadline and required professional decision; do not implement an unresolved alternative. |

#### MT-OPT-2: Entity structure -- company + shareholder refund

**MT-OPT-2: Entity structure -- company + shareholder refund**

| Field | Detail |
| --- | --- |
| **Category** | Entity structure |
| **Trigger** | Self-employed with net income > EUR 35,000 |
| **Calculation** | Model the actual company/shareholder system: company tax and tax accounts, distributable after-tax income, qualifying shareholder refund/credit, actual distribution/claim dates, personal tax, substance and costs. A conditional six-sevenths refund arithmetic is not a universal five-percent all-in rate and must not have personal tax blindly added again without imputation. Residence alone does not establish either entitlement or exclusion. The particular current statutory refund/tax-account computation is held pending primary-law review. |
| **Materiality** | > EUR 2,000 net annual savings |
| **Confidence** | T1 only for fully evidenced law/facts and mechanical comparison; otherwise T2/held. Neither confers accountant approval. |
| **Reviewer flag** | Obtain actual current shareholder/refund evidence, company election/account allocation and personal tax, tax/Companies Act audit requirements separately, and actual fees. All Maltese companies needing an audit is false: LN 139/2025 rule 6 recognises specified article 185(2) exemption cases, with review-report versus no-audit distinctions. Do not confuse this with a universal audit waiver or certify eligibility from one year. [Audit Exemption Rules 2025 rule 6](https://legislation.mt/getpdf/688b3e0cbed0ef08a863ffa1) |
| **Output** | Reviewer: report this check's actual year, facts, source and full baseline/alternative comparison using Part B. State held conditions, permanent versus timing effect, costs, deadline and required professional decision; do not implement an unresolved alternative. |

#### MT-OPT-3: Timing -- provisional tax alignment

**MT-OPT-3: Timing -- provisional tax alignment**

| Field | Detail |
| --- | --- |
| **Category** | Timing |
| **Trigger** | User pays provisional tax AND current-year income differs significantly from prior year |
| **Calculation** | For an applicable ordinary basis period, PT rules 4 and 5 set due dates April 30, August 31 and December 21, with ordinary benchmark instalments twenty/thirty/fifty-percent and catch-up where the benchmark changes. Use the actual statutory benchmark/notified adjustments, payments and reduction evidence; it is not necessarily the immediately previous year income figure. Cash released by reduction does not lower final tax. [SL 372.18 rules 4 to 6](https://legislation.mt/getpdf/60225900bc8272018c0e9119) |
| **Materiality** | > EUR 200 cash flow benefit |
| **Confidence** | T1 only for fully evidenced law/facts and mechanical comparison; otherwise T2/held. Neither confers accountant approval. |
| **Reviewer flag** | Read the actual benchmark, allowed reduction/application and consequences of deficient payments before requesting a change. Reconcile all payments, future balance and interest using actual rules, not a guessed rate or a blanket last-year-income formula. The reduction route, exact current interest and special basis-period adjustments remain held until verified. [Official source](https://legislation.mt/getpdf/60225900bc8272018c0e9119) |
| **Output** | Reviewer: report this check's actual year, facts, source and full baseline/alternative comparison using Part B. State held conditions, permanent versus timing effect, costs, deadline and required professional decision; do not implement an unresolved alternative. |

#### MT-OPT-4: Election -- Article 11 vs Article 10 VAT

**MT-OPT-4: Election -- Article 11 vs Article 10 VAT**

| Field | Detail |
| --- | --- |
| **Category** | Elections |
| **Trigger** | User is near the EUR 35,000 Article 11 threshold OR is Article 11 exempt with significant input VAT |
| **Calculation** | Compare actual calendar-turnover eligibility/exclusion and exemption under article 11 against article 10 taxable transactions, deductible input tax, customer contractual price/recovery, article 12 cross-border duties, capital adjustments and actual filing/admin costs. The current domestic exemption threshold is EUR 35,000 under the SixthSchedule, but no blanket standard-rate/all-input-recovery/quarterly-period assumption follows from registration status. [Current VAT Act article 11 and SixthSchedule](https://legislation.mt/getpdf/6ac352947b5e681a8405fbf4) |
| **Materiality** | > EUR 200 annual net benefit |
| **Confidence** | T1 only for fully evidenced law/facts and mechanical comparison; otherwise T2/held. Neither confers accountant approval. |
| **Reviewer flag** | Confirm actual prior/current calendar-year tests, application/loss dates, voluntary waiver and re-entry lock using the current Act. An article 11 trader may still need article 12 acquisition/received-service obligations; EU B2B reverse-charge rules do not universally require article 10. The old three-year voluntary minimum is not certified for the new 2025 scheme. [Official source](https://legislation.mt/getpdf/6ac352947b5e681a8405fbf4) |
| **Output** | Reviewer: report this check's actual year, facts, source and full baseline/alternative comparison using Part B. State held conditions, permanent versus timing effect, costs, deadline and required professional decision; do not implement an unresolved alternative. |

#### MT-OPT-5: Unclaimed -- deductions against self-employment income

**MT-OPT-5: Unclaimed -- deductions against self-employment income**

| Field | Detail |
| --- | --- |
| **Category** | Credits/reliefs not claimed |
| **Trigger** | User has self-employment income AND has not claimed all allowable deductions |
| **Calculation** | Reconcile actual capital allowance, business share of premises, eligible training/professional costs and bad debts to legal deductibility and accounting history. SL 123.01 Schedule lists minimum periods: computers/electronic equipment four years, furniture ten, air-conditioners six; do not use old 20%/15%/10% rates or call these ITA Schedule 6. Apply actual qualifying cost, business use, timing and election rules before deriving any annual allowance. [SL 123.01 Schedule](https://legislation.mt/getpdf/602258b6bc8272018c0e18cb) |
| **Materiality** | > EUR 100 tax savings |
| **Confidence** | T1 only for fully evidenced law/facts and mechanical comparison; otherwise T2/held. Neither confers accountant approval. |
| **Reviewer flag** | Obtain actual asset dates/costs/use and current allowance method. Separate tax capital allowances from book depreciation and prevent duplicate cost deductions. Exact home-office apportionment, training and bad-debt eligibility require current primary law: no unverified universal exclusive-room rule or all-training deduction is certified. [Official source](https://legislation.mt/getpdf/602258b6bc8272018c0e18cb) |
| **Output** | Reviewer: report this check's actual year, facts, source and full baseline/alternative comparison using Part B. State held conditions, permanent versus timing effect, costs, deadline and required professional decision; do not implement an unresolved alternative. |

## Section 4: Internal presentation thresholds

**Internal materiality thresholds.** These unchanged workflow floors and the check-specific profitability/complexity screens are product settings, not statutory rates, contribution limits, taxpayer eligibility or authority to suppress a legal obligation. Show the currency, complete net-effect basis and any user override.

| Currency | Floor |
| --- | --- |
| EUR | 100 |
| USD | 100 |
| GBP | 100 |
| AUD | 150 |
| CAD | 150 |
| INR | 10,000 |

- **Presentation rule:** retain every evaluated item in Part C with its status and reason; below-floor voluntary ideas may be omitted from the headline list unless the user asks for all. Deadlines, errors, refusals and legal obligations are never suppressed.

## Section 5 -- Output format

### Part A -- Savings summary

**Part A -- Savings summary example table**

| # | Jurisdiction | Check | Category | Illustrative assumed comparison, not a quoted legal entitlement | Confidence | Priority |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | US | Retirement contribution room | Retirement | Not calculated until actual eligibility/room and full baseline are evidenced | Held | Pending |
| 2 | UK | Pension contribution and actual allowance interaction | Retirement | Not calculated from a universal taper-band percentage | Held | Pending |
| 3 | US | S-Corp election | Entity structure | Requires salary, full taxes, future extraction and actual fees | T2 | Pending |
| ... |  |  |  |  |  |  |

- **Priority definitions:** internal ranking only. HIGH is greater than five times the floor; MEDIUM is more than twice and up to five times; LOW is from the floor up to twice. The exact floor is included. Rank legally required/corrective actions separately, and keep held or non-comparable outcomes out of a fabricated numeric ranking.

### Part B -- Detailed recommendations (top 5 by savings)

For each:

```
### [Check name] -- [Jurisdiction] -- [Estimated saving]

**What:** [One-sentence description]
**Your situation:** [Current position based on user data]
**Opportunity:** [What can be done]
**Calculation:** [Full baseline versus alternative; original currency and timing; present-value assumptions if used; tax/credit interactions and actual costs; no overlapping alternatives added]
**Effect:** [Permanent reduction / deferral / cash release / interest avoided / held]
**Evidence and approval:** [Actual source/year, accountant provenance, unresolved conditions and transaction sign-off]
**Action required:** [Specific next steps]
**Deadline:** [When this must be done by, if time-sensitive]
**Confidence:** [T1/T2] -- [Basis]
**Reviewer note:** [What the reviewer must verify]
```

### Part C -- Suppressed checks

List every original check ID as not applicable / checked with no benefit / below internal headline floor / conditional / held / ready for professional decision, with factual reason, legal source and missing-evidence task. Never call an unrun or unavailable-law check completed. Preserve all five checks per jurisdiction, including those with no supported numerical result.

### Part D -- Caveats

- All savings are estimates based on current data
- Interaction effects: some optimisations affect others (e.g., retirement contributions reduce QBI income, which may reduce QBI deduction)
- No aggressive or novel positions are suggested
- The reviewer must validate all suggestions before implementation

## Section 6 -- Self-checks

Before delivering output, verify:

- [ ] User's jurisdiction is confirmed, not assumed
- [ ] All 5 checks for each applicable jurisdiction were evaluated
- [ ] Trigger conditions were checked against actual user data
- [ ] Calculations use the user's actual figures, not hypothetical amounts
- [ ] Internal presentation floor applied only to voluntary headline ideas; all errors, duties, deadlines and forty check statuses remain visible
- [ ] Confidence tiers (T1/T2) are correctly assigned
- [ ] Interaction effects between optimisations are noted
- [ ] Every suggestion is addressed to the reviewer, not the taxpayer
- [ ] No concealment, false facts or abusive schemes are suggested; lawful reportability and specialist anti-avoidance questions receive a documented referral
- [ ] Results follow actual evidenced facts and legal alternatives; no deliberately overstated tax, understated relief or invented conservative default
- [ ] Output uses the format from Section 5
- [ ] Disclaimer is included

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

## Worked cases

### A deduction brings forward cash, not its whole amount as permanent savings

Assume a legally deductible expense may lawfully be taken now or next year. Actual eligibility/timing has already been established; these are illustrative tax differences, not a source for any country's rate. The baseline taxes are 12,000 now and 8,000 next year; the supported alternative gives 9,000 now and 11,000 next year. Current cash release is 3,000, but nominal total tax reduction is zero. With an explicitly assumed ten-percent discount rate and no other costs, computed present-value benefit is approximately 272.73. Do not report 3,000 as permanent savings or the expense itself as money gained.

```oa-check
name: Timing is not a permanent tax reduction
inputs:
  baseline_now: 12000
  baseline_later: 8000
  alternative_now: 9000
  alternative_later: 11000
  assumed_discount: 0.10
steps:
  - current_cash_release: baseline_now - alternative_now
  - later_extra_tax: alternative_later - baseline_later
  - nominal_total_reduction: baseline_now + baseline_later - alternative_now - alternative_later
  - present_value_benefit: current_cash_release - later_extra_tax / (1 + assumed_discount)
expected:
  current_cash_release: 3000
  later_extra_tax: 3000
  nominal_total_reduction: 0
  present_value_benefit: 272.727272727273
```

### Incorporation compares complete owner cash outcomes

Illustrative supported computations for the same economic profit show baseline combined taxes 30,000, versus company 18,000, owner extraction 9,000 and additional actual annual costs 4,000. The company option costs 1,000 more overall, despite its lower company tax line. Formation capital is separately tracked as funding and is not automatically a deductible cost. An overlapping retirement contribution or retained-profit alternative cannot be added again as if independent.

```oa-check
name: Lower company tax alone is not incorporation savings
inputs:
  baseline_combined_tax: 30000
  company_tax: 18000
  owner_extraction_tax: 9000
  actual_additional_costs: 4000
steps:
  - alternative_tax: company_tax + owner_extraction_tax
  - apparent_tax_difference: baseline_combined_tax - company_tax
  - net_annual_effect: baseline_combined_tax - alternative_tax - actual_additional_costs
expected:
  alternative_tax: 27000
  apparent_tax_difference: 12000
  net_annual_effect: -1000
```

## When to refuse or refer

Do not implement elections, incorporate, pay premiums/contributions, file/amend returns or submit a reduction request merely because this scan found a potential difference. Hold a final numerical recommendation where actual law/year, identity/residence, eligible entity/instrument, source records, income/room, election history, payment deadline, costs or interactions are unresolved. Preserve the complete scan and exact gap. Refer actual cross-border, transfer-pricing, group/corporate restructuring or specialist law issues to their methods and qualified reviewer. Do not propose concealment, false documents, invented earnings, abusive shelters or the deliberate non-disclosure of a legally reportable arrangement. Reportability and lawful uncertainty are not themselves proof of illegality; obtain the appropriate professional decision. Existing named approval belongs to the published method, not to an unreviewed planning recommendation.

## Sources

| Official source and bounded actual read | URL | Read on |
|---|---|---|
| Read for IRS 2026 retirement announcement: read ordinary 401(k), IRA/catch-up and ordinary/applicable SIMPLE amounts; not every MAGI condition | https://www.irs.gov/newsroom/401k-limit-increases-to-24500-for-2026-ira-limit-increases-to-7500 | 2026-11-14 |
| Read for IRS 401(k) limits: read deferral, catch-up, annual additions and compensation sections | https://www.irs.gov/retirement-plans/plan-participant-employee/retirement-topics-401k-and-profit-sharing-plan-contribution-limits | 2026-11-14 |
| Read for IRS owner-only 401(k): read both owner capacities, actual earned-income adjustments and common-law-employee distinction | https://www.irs.gov/retirement-plans/one-participant-401k-plans | 2026-11-14 |
| Read for IRS Pub 560,2025 edition: read selected post-year-end adoption and employer/owner election timing paragraphs; latest detailed filing-cycle bridge, not all 2026 plan deadlines | https://www.irs.gov/publications/p560 | 2026-11-14 |
| Read for IRS S-company compensation: read reasonable-compensation duty, receipts/services analysis and factors; no full election/benefits determination | https://www.irs.gov/businesses/small-businesses-self-employed/s-corporation-compensation-and-medical-insurance-issues | 2026-11-14 |
| Read for IRS Pub 538,2025 edition: read cash/constructive receipt, advance-expense twelve-month rule and method-change consent paragraphs | https://www.irs.gov/publications/p538 | 2026-11-14 |
| Read for IRS simplified home-office: read actual eligibility/method table, income/carryforward and election distinctions, also read alongside Pub 587 in the sharedUS method | https://www.irs.gov/businesses/small-businesses-self-employed/simplified-option-for-home-office-deduction | 2026-11-14 |
| Read for IRS Form 7206 instructions 2025: read business-established coverage, excluded months, earned-income and Marketplace coordination references; not 2026 long-term-care limits | https://www.irs.gov/instructions/i7206 | 2026-11-14 |
| Read for HMRC pension relief: read personal earnings/low-income relief and relief-at-source versus additional relief, not all scheme rules | https://www.gov.uk/tax-on-your-private-pension/pension-tax-relief | 2026-11-14 |
| Read for HMRC annual allowance: read current ordinary allowance, all-scheme inputs, carry-forward and both taper income conditions; MPAA amount/floor not certified | https://www.gov.uk/tax-on-your-private-pension/annual-allowance | 2026-11-14 |
| Read for HMRC 2026-2027 self-employed NIC page: read treated-paid Class 2, voluntary distinction and Class 4 bands/rates | https://www.gov.uk/self-employed-national-insurance-rates | 2026-11-14 |
| Read for HMRC 2026-2027 dividends page: read current allowance/rate table and band interaction | https://www.gov.uk/tax-on-dividends | 2026-11-14 |
| Read for HMRC corporation-tax tables: read small/main rates and marginal relief; individual company adjusted thresholds still need assessment | https://www.gov.uk/government/publications/rates-and-allowances-corporation-tax/rates-and-allowances-corporation-tax | 2026-11-14 |
| Read for HMRC payments-on-account: read actual instalment/exception/balancing-payment explanation; no current interest percentage or reduction consent assumed | https://www.gov.uk/understand-self-assessment-bill/payments-on-account | 2026-11-14 |
| Read for HMRC cash-basis overview: read current default, excluded-company and alternative-accounting/transition discussion | https://www.gov.uk/simpler-income-tax-cash-basis | 2026-11-14 |
| Read for FinanceAct 2024 Schedule 10: read current operative cash default/election and paragraphs 6 to 8 repealing old turnover, interest and loss restrictions | https://www.legislation.gov.uk/ukpga/2024/3/schedule/10 | 2026-11-14 |
| Read for HMRC allowance: read aggregate full/partial relief, exclusions and reporting/records circumstances | https://www.gov.uk/guidance/tax-free-allowances-on-property-and-trading-income | 2026-11-14 |
| Read for Bavarian tax administration 2026 calculator explanatory text 2.2: read current Basisrente/statutory pension ceiling; no calculator submission performed | https://www.steuerberechnung.bayern.de/Alterseinkuenfte-Rechner/2026/aekr_formular.asp?VLG=2 | 2026-11-14 |
| Read for EStG 10(3): read current ceiling mechanism, employer-offset and full percentage from 2023; not every pension contract exception | https://www.gesetze-im-internet.de/estg/__10.html | 2026-11-14 |
| Read for KStG 23(1): read actual current-year corporation-tax rate and future dated changes | https://www.gesetze-im-internet.de/kstg_1977/__23.html | 2026-11-14 |
| Read for GewStG 11(1) and(2): read actual allowance and measurement amount; municipal multiplier not supplied | https://www.gesetze-im-internet.de/gewstg/__11.html | 2026-11-14 |
| Read for EStG 35(1): read actual credit mechanism and its limitation; no universal full credit assumed | https://www.gesetze-im-internet.de/estg/__35.html | 2026-11-14 |
| Read for EStG 7g(1) to(4): read exact profit boundary, property/use, deduction/outstanding caps, matching period and reversal; special depreciation not promoted | https://www.gesetze-im-internet.de/estg/__7g.html | 2026-11-14 |
| Read for AO 238: read general versus section 233a special rate, full-month and rounding provisions; actual case interest start not supplied | https://www.gesetze-im-internet.de/ao_1977/__238.html | 2026-11-14 |
| Read for UStG 19: complete paragraphs 1 to 6 read for prior/current turnover and waiver/binding conditions | https://www.gesetze-im-internet.de/ustg_1980/__19.html | 2026-11-14 |
| Read for EStG 4(5)6b and 6c: read office-centre annual alternative and daily homeworking conditions/exclusions; not employee allowance law | https://www.gesetze-im-internet.de/estg/__4.html | 2026-11-14 |
| Read for ATO indexed official prepayments guide: actual twelve-month eligibility block read, including alternative turnover scope; direct retrieval 403 and not all statutory excluded expenses | https://www.ato.gov.au/api/public/content/0-93638c4a-a53a-4d5b-9dca-85b8530febc4 | 2026-11-14 |
| Read for ATO official indexed extract actually read on this date: current concessional cap table and employer/personal contribution aggregation. Direct page retrieval 403; no full-page/carry-forward eligibility read claimed | https://www.ato.gov.au/api/public/content/0-af5a46ad-7287-431c-be8e-4a0c9bbc5fc1 | 2026-11-14 |
| Read for ATO official indexed extract read: actual income/low-tax threshold, lesser-excess/contribution and additional-rate paragraphs; direct challenge prevents a full-page read | https://www.ato.gov.au/api/public/content/0-6c3220ce-b973-4514-84e0-0f9f28c4d0a7 | 2026-11-14 |
| Read for ATO official indexed extract read: current lower/full company rates and passive-income eligibility paragraph, not all turnover/franking/PSI rules | https://www.ato.gov.au/api/public/content/0-11c3cbc8-adf6-4118-bc2c-0c5044452da1 | 2026-11-14 |
| Read for ATO official indexed extract read: enacted July 2026 permanent write-off amount, strict cost/turnover tests and first-use criterion; not every excluded asset | https://www.ato.gov.au/api/public/content/0-cd3490b1-151e-442d-9571-b0d481b340e0 | 2026-11-14 |
| Read for Australian enacted 2026 Act Schedule 2: read threshold substitutions and application provisions; not whole TaxReformAct | https://www.legislation.gov.au/C2026A00071/asmade/2026-08-26/text/original/epub/OEBPS/document_1/document_1.html | 2026-11-14 |
| Read for ATO official indexed extract read: temporary full expensing end date and no new post-end qualifying asset deduction | https://www.ato.gov.au/api/public/content/0-62fc72e5-417c-4afc-ab6d-a59f6f8a1209 | 2026-11-14 |
| Read for ATO official indexed table extract read:2026-2027 single/family boundaries and July 2026-to-March 2027 under 65 rebate row. Direct retrieval 403; complete older-age/child/component rules not claimed | https://www.ato.gov.au/api/public/content/0-e0e9fe64-117a-4024-b3d9-770218d1d67f | 2026-11-14 |
| Read for CRA official indexed table read: actual 2026 RRSP dollar limit and separately dated 2025 row; direct fresh download timed out | https://www.canada.ca/en/revenue-agency/services/tax/registered-plans-administrators/pspa/mp-rrsp-dpsp-tfsa-limits-ympe.html | 2026-11-14 |
| Read for CRA current page cached 2026-11-14: read room formula/adjustments, unused-contribution/excess distinction and latest 2025-cycle contribution-date paragraphs | https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/rrsps-related-plans/contributing-a-rrsp-prpp/contributions-affect-your-rrsp-prpp-deduction-limit.html | 2026-11-14 |
| Read for CRA current page cached 2026-11-14: read actual NOA/reassessment/T1028 deduction-limit sources; not a real taxpayer account | https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/rrsps-related-plans/contributing-a-rrsp-prpp/where-you-find-your-rrsp-prpp-deduction-limit.html | 2026-11-14 |
| Read for CRA current page cached 2026-11-14: complete operative home-expense block read, including alternative eligibility/time share, limits/carry-forward and property effects | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/report-business-income-expenses/completing-form-t2125/business-use-home-expenses.html | 2026-11-14 |
| Read for actual 2025 T1139 form: read first-page alternative-method eligibility, exclusions, continuing additional-income requirement and election/cancellation; not a2026form | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t1139/t1139-25e.pdf | 2026-11-14 |
| Read for Indian official individual guide: read AY 2026-2027 regime/business-election paragraphs and old-section 80C/NPS/80D table; employerNPS limits and successor-year rules not adopted | https://www.incometax.gov.in/iec/foportal/help/individual/return-applicable-1 | 2026-11-14 |
| Read for Indian official ITR 4FAQ, latest detailed older filing cycle: read presumptive/profession, books and March advance-tax paragraphs; wording/year limitations retained, not law for new tax-year 2026-2027 | https://www.incometax.gov.in/iec/foportal/help/e-filing-itr4-form-sugam-faq | 2026-11-14 |
| Read for BOE current consolidated LIRPF article 52 and DA 16: read complete actual income/monetary/increment/worker matching and carryover conditions, not all pension law | https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764 | 2026-11-14 |
| Read for AEAT current table updatedJune 2026: read ordinary/micro/reduced-size/new-entity 2026 rows and footnote; no full new-entity timing/exclusion law claimed | https://sede.agenciatributaria.gob.es/Sede/impuesto-sobre-sociedades/que-base-imponible-se-determina-sociedades/tipo-impositivo.html | 2026-11-14 |
| Read for AEAT current instructions: read cumulative income/expense, ordinary/special percentage, prior-payment and negative-return carry/due/refund distinctions | https://sede.agenciatributaria.gob.es/Sede/impuestos-tasas/impuesto-sobre-renta-personas-fisicas/modelo-130-irpf______esionales-estimacion-directa-fraccionado_/instrucciones.html | 2026-11-14 |
| Read for Spanish SocialSecurity 2026 guide: read provisional-base and six annual changes/effective-month paragraphs; exact notice/payment and all retention rules not supplied | https://portal.seg-social.gob.es/wps/portal/importass/importass/Colectivos/trabajo%2Bautonomo/guia | 2026-11-14 |
| Read for AEAT current simplified method guide: read eligibility, positive-base deduction/cap and separately dated 2026 Ceuta exception | https://sede.agenciatributaria.gob.es/Sede/irpf/empresarios-individuales-profesionales/regimenes-determinar-rendimiento-actividad/estimacion-directa-simplificada.html | 2026-11-14 |
| Read for current SL 123.163 rules 4 to 8: read qualifying individual/application/certificate/scheme/reporting and exact credit rule; whole article 57 refund/interaction rules not certified | https://legislation.mt/getpdf/60250ba78f58ac184473f786 | 2026-11-14 |
| Read for MTCA booklet header and printedpage 35 read: actual basis 2025/YA 2026 personal/occupational pension credits; explicitly latest filing-cycle bridge, not basis 2026 occupational rules | https://mtca.gov.mt/docs/default-source/documents/personal-tax/individual/tax-return-booklet-individuals/mtca-tax-booklet-2026-eng-17-03.pdf | 2026-11-14 |
| Read for original LN 139/2025 rules 6 to 8 and commencement: actual audit/review exceptions and CompaniesAct eligibility-reference read; no blanket 2026 company eligibility claimed | https://legislation.mt/getpdf/688b3e0cbed0ef08a863ffa1 | 2026-11-14 |
| Read for SL 372.18 rules 4 to 6: actual due dates, benchmark schedule and catch-up adjustment paragraphs read; reduction application/interest not certified | https://legislation.mt/getpdf/60225900bc8272018c0e9119 | 2026-11-14 |
| Read for current Cap 406 article 11 and SixthSchedule pages 11 to 13 and 98 to 101 read in threshold batch; no general article 10/12 complete transaction determination | https://legislation.mt/getpdf/6ac352947b5e681a8405fbf4 | 2026-11-14 |
| Read for SL 123.01 Schedule: complete listed minimum useful periods read, together with opening qualifying plant/machinery rules; final apportionment/election calculation remains case-specific | https://legislation.mt/getpdf/602258b6bc8272018c0e18cb | 2026-11-14 |

Not yet confirmed: complete current 2026 taxpayer eligibility, deductions, credit/rate interactions, pension carryovers/access and plan deadlines for all forty checks; US 2026 final detailed retirement catch-up/Roth and health-insurance instructions and every statutory method/election exception; UK actual MPAA/taper floor, carry-forward and company adjusted thresholds, reduction submission/interest and exact final-year interactions; German full pension qualification, municipal/personal/distribution rates, specific office facts and exact IAB-use/interest commencement; Australian full current carry-forward/deduction-notice/preservation, passive-income/turnover, asset exclusions/pool and private-health family/age/premium-component rules beyond the bounded official excerpts; Canadian actual 2026 RRSP contribution deadline/spousal attribution, incorporation/PSB/TOSI and provincial computation, final 2026 T1139 and enacted property-specific immediate-expensing/CCA availability; India's tax-year 2026-2027 successor-Act equivalents, elections, audit/re-entry and advance-tax/interest exceptions, plus exact older-law cash/audit cases where not read; Spanish new-company actual eligibility/duration, regional/foral rates, social-security final bands/refund/retention and relevant return exceptions; Maltese current tax-account/shareholder refund/imputation and company elections, occupational scheme interaction/nonrefund/carryforward, provisional-tax reduction/interest, VAT waiver/re-entry/article 12 details and precise home-office/training/bad-debt/allowance conditions. These tasks remain held, not replaced by a stale figure or a guessed standard tax rate. Historical generic fees, profit screens and currency floors are internal priorities/illustrations only, not current law or actual client costs.
