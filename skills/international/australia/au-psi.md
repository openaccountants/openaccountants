---
name: au-psi
description: >
  Use this skill whenever asked about Australian personal services income -- PSI, the PSI rules,
  Divisions 84 to 87 ITAA 1997, personal services entities, personal services business tests, the
  results test, the 80% rule, unrelated clients, employment or business premises tests, PSB
  determinations, attribution of PSI, PSI deduction limits, contractors invoicing through companies
  or trusts, income splitting or profit retention by consultants, PCG 2025/5, or Part IVA exposure
  for PSBs. Trigger on phrases like "PSI", "personal services", "PSB", "results test", "80% rule",
  "attribution", or a GL showing an entity invoicing one individual's skills. ALWAYS read this
  skill before any PSI work.
version: 1.0
jurisdiction: AU
tax_year: 2026
tax_year_notes: "2026-27"
last_updated: 2026-08-20
review_status: pending_review
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Australia Personal Services Income (PSI) -- Divisions 84-87 Skill v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

> **Law-change context.** Two 2025-26 developments reshape PSI work. (1) The ATO finalised draft PCG 2024/D2 as **PCG 2025/5** (issued 28 November 2025): qualifying as a personal services business does NOT immunise income splitting or profit retention from Part IVA -- Rule 11 carries the low-risk / higher-risk framework, including the ATO's statement that it will not pursue Part IVA compliance where a taxpayer makes a genuine attempt to move to a low-risk arrangement by 30 June 2027. (2) The $1,000 standard deduction for work-related expenses (Treasury Laws Amendment (Tax Reform No. 1) Act 2026, from 1 July 2026) does NOT extend to PSI earners -- Rule 12.

## Section 1 -- Quick reference

**Read this whole section before classifying any income or computing anything.**

| Field | Value |
|---|---|
| Country | Australia |
| Primary Legislation | ITAA 1997 Part 2-42: Div 84 (definition), Div 85 (individuals' deduction limits), Div 86 (attribution + entity deduction limits), Div 87 (PSB tests) |
| Tax Authority | Australian Taxation Office (ATO) |
| Income Year | 2026-27 (1 July 2026 -- 30 June 2027); lodgment season under way for 2025-26 |
| PSI definition | Income mainly (**more than 50%**) a reward for an individual's personal efforts or skills (s 84-5) |
| Results test | All 3 conditions met for **at least 75%** of the individual's PSI (s 87-18) |
| 80% rule | **80% or more** of PSI from one client + its associates blocks self-assessment on the other three tests (s 87-15(3)) -- results test or PSBD only |
| Other PSB tests | Unrelated clients (s 87-20), employment (s 87-25), business premises (s 87-30) -- each needs the 80% rule met |
| PSB determination | ss 87-60 (individuals) / 87-65 (entities); unusual-circumstances gateway |
| Attribution | Net PSI included in the individual's assessable income (s 86-15); NANE to the entity (s 86-30) |
| PAYG on attributed PSI | TAA 1953 Sch 1 Div 13 (attributed amounts) and Div 12 (salary actually paid) |
| Core ATO ruling | TR 2022/3 (replaced TR 2001/7 and TR 2001/8) |
| Part IVA guideline | PCG 2025/5 (issued 28 Nov 2025; applies before and after issue) |
| Contributor | Open Accountants |
| Validated by | Pending |

**Conservative defaults:**

| Ambiguity | Default |
|---|---|
| Entity's fee income traced to one individual's work | Treat as PSI of that individual until the >50% "mainly" analysis says otherwise |
| Hourly or daily-rate contract | Assume the results test FAILS (not paid for a result) until the contract shows otherwise |
| Client concentration unknown | Assume the 80% rule FAILS; only the results test or a PSBD can then save PSB status |
| "We advertise" claimed for unrelated clients test | Assume NOT satisfied until offers/invitations to the public are evidenced (website, tenders, ads -- not a labour-hire panel) |
| Home office claimed as business premises | Assume the business premises test FAILS (not physically separate, rarely exclusive) |
| PSB status asserted, low salary + retained profits visible | Treat as PCG 2025/5 HIGHER RISK; run the Rule 11 screen and escalate |
| Employee-like engagement (one payer, their tools, their control) | Flag employee/contractor characterisation and sham-contracting risk before any PSI analysis (Rule 12, R-AU-PSI-5) |

## Section 2 -- The five-step decision flow

Work every engagement, per individual, per income year, in this order. Never skip a step.

1. **Is any income PSI?** More than 50% of the reward under each contract/invoice for an individual's personal efforts or skills -> PSI (Rule 1). Test each contract separately.
2. **Is the individual/entity a PSB under the results test?** (Rule 4). If yes for >= 75% of PSI -> PSI rules do not apply (go to step 5 anyway).
3. **Is less than 80% of the PSI from one client and its associates?** If no -> PSI rules apply unless a PSBD is obtained (Rule 8). If yes -> test unrelated clients, employment, business premises (Rules 5-7).
4. **No test met, no PSBD?** PSI rules apply: deduction limits (Rule 10), attribution (Rule 9), PAYG (Rule 9).
5. **PSB after all?** The income keeps its PSI character; ordinary rules plus Part IVA apply -- run the PCG 2025/5 risk screen (Rule 11).

## Section 3 -- GL sweep library

PSI work starts with the ledger and the debtor list, not the client's self-assessment.

| GL pattern | Likely issue | Action |
|---|---|---|
| Company/trust service fees generated by ONE individual's skills | PSE candidate | Run the Section 2 flow per individual; check invoices for goods/asset components |
| One debtor >= 80% of fee income | 80% rule fails | Results test or PSBD are the only PSB routes; else attribution |
| Low director salary + material retained profits | PCG 2025/5 higher-risk retention | Verify PSB status first, then Rule 11 screen; escalate structuring (R-AU-PSI-6) |
| Dividends/distributions to non-working spouse or family members | Higher-risk income splitting | Rule 11; document services actually provided; escalate (R-AU-PSI-6) |
| Rent, mortgage interest, rates paid to the individual/associate for their residence | Denied: s 85-15 / s 86-60 | Add back in the attribution computation |
| Salary or "admin fee" to an associate | Deductible only for principal work (s 85-20); admin support denied | Add back non-principal amounts; test reasonableness |
| Two or more cars with private use by the individual | One-car limit (s 85-25 / s 86-70) | Add back the excess |
| Nil PAYG remitted but attribution applies | TAA Sch 1 Div 13 breach | Quantify; flag urgently |
| Contract income billed hourly with timesheets | Results test likely failing | Evidence check before any PSB claim |

---

## Section 4 -- Worked examples

### Example 1 -- IT contractor, 90% one client, attribution arithmetic

BitWorks Pty Ltd derives $220,000 (GST-exclusive) in 2026-27 from the programming services of Dev, its sole director. Contracts are hourly-rate, the client supplies the dev environment, and BitWorks bears no rectification liability: **results test fails** (0% of PSI meets the s 87-18 conditions -- needs >= 75%). One bank supplies 90% of the income: **80% rule fails**, so the unrelated clients / employment / business premises tests cannot be self-assessed and no PSBD is held. The PSI rules apply.

BitWorks paid Dev $100,000 salary (Div 12 PAYG withheld) and incurred: laptop and software $4,000; professional indemnity insurance $1,500; bookkeeping and ASIC fees $800 (entity maintenance); rent to Dev's spouse for the home office $12,000 (**denied** s 86-60/s 85-15); spouse "admin salary" $20,000 for non-principal work (**denied** s 86-60/s 85-20).

```
Attributed PSI (s 86-15, reduced per s 86-20)
  PSI received                          $220,000
  less salary promptly paid to Dev      (100,000)
  less deductible outgoings:
    equipment                             (4,000)
    professional indemnity                (1,500)
    entity maintenance (s 86-65)            (800)
  Denied amounts NOT subtracted: rent to associate $12,000,
    associate non-principal salary $20,000
  = Net PSI attributed to Dev           $113,700
Dev's assessable income = $100,000 salary + $113,700 attribution = $213,700
```

The attributed $113,700 is neither assessable nor exempt income of BitWorks (s 86-30). BitWorks must have remitted PAYG on the attributed income quarterly under TAA 1953 Sch 1 Div 13 and reports the attributed amount to Dev. The spouse's $20,000 stays assessable to the spouse even though the company's deduction is denied -- flag the double-tax sting for the reviewer.

### Example 2 -- Consultant passing the unrelated clients test

Mia, a sole-trader marketing consultant, earns $180,000 of PSI in 2026-27 from five unrelated clients won through her website and competitive tenders: A $81,000 (45%), B $45,000 (25%), C $27,000 (15%), D $18,000 (10%), E $9,000 (5%).

No client (with associates) reaches 80% -> the 80% rule is met. Services were provided to 2+ non-associated entities as a direct result of offers to the public (website, tenders) -> **unrelated clients test met (s 87-20)**; Mia self-assesses as a PSB. Consequences: no deduction limits, no attribution (she is the individual anyway). The income **retains its PSI character** -- she declares it at the PSI labels of her return, and the $1,000 standard deduction is unavailable against it (Rule 12). Had Mia sourced the same five clients solely through a labour-hire firm's panel, s 87-20(2) would deny the "offers to the public" limb -- see R-AU-PSI-2.

### Example 3 -- Company retains PSB profits: Part IVA risk zones

EngCo Pty Ltd (a base rate entity) derives $300,000 from the engineering services of Priya, who genuinely passes the results test -- EngCo is a PSB, so no attribution. EngCo pays Priya a $90,000 salary, retains the balance, and pays franked dividends to Priya's non-working spouse, a 50% shareholder.

```
2026-27 comparison (resident rates, 15% first bracket from 1 Jul 2026)
  Tax if Priya earned $300,000 directly:
    $100,870 + Medicare $6,000              = $106,870
  Arrangement as structured:
    Priya on $90,000: $17,520 + $1,800      = $19,320
    EngCo on $210,000 profit at 25%         = $52,500
    Combined                                 = $71,820
  Immediate saving/deferral                  = $35,050
```

PCG 2025/5 higher-risk indicators present: salary not commensurate with the value of Priya's services; retention of net PSI in a lower-taxed entity without a commercial purpose; splitting to a non-working associate (Guideline Examples 10-17). The 25% rate assumes EngCo is a base rate entity in the year -- service fees are trading income, not base rate entity passive income, so a pure-services company under the $50m turnover limb ordinarily qualifies; if retained profits later generate passive income above 80% of assessable income, the rate flips to 30% (see au-company-tax). Franking on eventual distribution reduces but does not erase the benefit (deferral + choice of recipient). This file computes exposure only -- restructuring advice escalates (R-AU-PSI-6). A genuine move to a low-risk arrangement (full net PSI to Priya, taxed at her marginal rate) by 30 June 2027 is inside the ATO's stated transitional compliance approach (PCG 2025/5 para 11).

---

## Section 5 -- Tier 1 rules

### Rule 1 -- What PSI is (s 84-5)

Ordinary or statutory income that is **mainly** -- more than 50% -- a reward for an individual's personal efforts or skills. Assess contract by contract on the substance of what the payment rewards, not the invoice label. Only individuals have PSI, but a company, partnership or trust (a **personal services entity**, PSE) can receive it; the rules then operate per test individual. Almost any profession can earn PSI: IT contractors, engineers, medical practitioners, consultants, construction professionals.

### Rule 2 -- What PSI is not

Income mainly from: **supplying or selling goods**; **granting the use of income-producing assets** (e.g. plant hire, a truck where the payment mainly rewards the vehicle); or a **business structure** (substantial employees/practice assets generating the income rather than one person's exertion). A structure is not "business structure income" merely because a company exists, carries on a business, or qualifies as a PSB (PCG 2025/5 paras 18-20). Salary of a genuine employee is outside the PSI regime entirely (s 84-10 works the other way too -- see Rule 12). Professional firms with genuine structure income are PCG 2021/4 territory, not this file.

### Rule 3 -- The gateway and the 80% rule (s 87-15)

A PSE/individual conducts a PSB in an income year only if: the **results test** is met; or **less than 80%** of the individual's PSI comes from one client and its associates AND at least one of the other three tests is met; or a **PSB determination** is in force. At 80%-or-more concentration the unrelated clients, employment and business premises tests are unavailable to self-assessment no matter how clearly they would be satisfied -- only the results test or a PSBD helps. Apply the 80% rule per individual, aggregating each client with its associates.

### Rule 4 -- Results test (s 87-18)

Met if **at least 75% of the individual's PSI** for the year satisfies ALL three conditions, judged against custom or practice for independent contractors (s 87-18(4)):

1. the income is for producing a **result** (payment contingent on outcome -- hourly/daily rates generally fail);
2. the individual/entity is required to **supply the plant, equipment or tools of trade** needed to do the work (where the work genuinely needs none, the condition can still be satisfied -- TR 2022/3); and
3. the individual/entity **is or would be liable for the cost of rectifying defective work** (a real exposure to rectify at own cost, not a right of the client to terminate).

The results test is the only test available regardless of client concentration. Mixed contract books are common: measure the percentage of PSI dollars meeting all three limbs, not the number of contracts.

### Rule 5 -- Unrelated clients test (s 87-20)

Both limbs, in the income year: (a) PSI from **2 or more clients** who are not associates of each other or of the individual/PSE; and (b) the services are provided **as a direct result of making offers or invitations to the public or a section of the public** -- advertising, a public website, competitive tenders; word-of-mouth referrals can qualify in narrow, specialised markets (TR 2022/3). **Statutory carve-out:** merely being available through an entity whose business is arranging for persons to provide services to its clients (labour-hire firms, some agencies/platforms) is NOT making offers to the public (s 87-20(2)). Failing limb (b) with otherwise-plentiful clients is the most common practitioner error.

### Rule 6 -- Employment test (s 87-25)

Met if the entity/individual engages one or more others who perform **at least 20% (by market value) of the principal work** for the year, or has **one or more apprentices for at least half the year**. The test individual never counts toward it; for individuals, non-individual associates count only where the work is performed by others. "Principal work" is the work generating the PSI, not administration or bookkeeping.

### Rule 7 -- Business premises test (s 87-30)

**At all times** during the income year, the individual/PSE maintains AND uses business premises: (a) at which the PSI-producing activities are mainly conducted; (b) of which they have **exclusive use**; (c) **physically separate from private premises** of the individual/associates; and (d) **physically separate from the premises of the client** (and client's associates). The premises need not be the same all year, but there must be qualifying premises for every day. Home offices fail (c); a rented room without exclusive use fails (b); shared reception areas do not count.

### Rule 8 -- PSB determinations (ss 87-60, 87-65)

When self-assessment is unavailable -- typically 80%+ concentration, or a test narrowly missed -- the PSE/individual can apply for a **PSBD**. The Commissioner may make one where satisfied a test was met or **could reasonably be expected to be met but for unusual circumstances** (e.g. starting out while genuinely advertising to the public with a reasonable expectation of unrelated clients; temporary loss of a client; natural disasters interrupting premises -- TR 2022/3 example of flood-delayed premises). For the results/unrelated-clients routes at 80%+ concentration the ATO also looks to whether the income could have come from unrelated clients. Determinations operate for specified years and can be revoked on changed facts. **Preparing or lodging an actual PSBD application escalates -- R-AU-PSI-4.** This file only identifies candidacy.

### Rule 9 -- Consequences: attribution and PAYG (Div 86; TAA 1953 Sch 1 Divs 12-13)

Where the PSI rules apply to PSI received by a PSE:

- **Attribution (s 86-15):** the individual's assessable income includes the entity's income that is that individual's PSI, EXCEPT amounts promptly paid to the individual as salary (within 14 days after the end of the relevant PAYG payment period) -- those are salary in the ordinary way.
- **Net amount (s 86-20):** the attributed amount is reduced by the entity's deductions relating to that PSI (after the Rule 10 limits). If deductions exceed the PSI, the excess flows to the individual (s 86-27).
- **No double tax (s 86-30):** attributed income is neither assessable nor exempt income of the entity.
- **PAYG:** the entity withholds under Div 12 on salary actually paid AND must pay amounts to the Commissioner under **Div 13** in respect of attributed (alienated) PSI quarterly, reporting the attributed income to the individual annually. Missed Div 13 obligations are a standing audit flag.
- Sole traders whose PSI is caught face the Rule 10 deduction limits directly (no attribution needed) and report at the PSI labels.

### Rule 10 -- Consequences: deduction limits (Div 85; Subdiv 86-B)

The organising principle: **no better than an employee**. Against PSI, the individual (s 85-10) -- and derivatively the PSE (s 86-60) -- can deduct only what an employee earning that income could deduct, plus a short statutory list. Specifically DENIED:

- **rent, mortgage interest, rates, land tax** for the residence of the individual or an associate used for PSI work (s 85-15) -- the classic home-office occupancy claim;
- **payments to associates** (salary, super) for **non-principal work** -- admin, bookkeeping, secretarial support (s 85-20); payments to associates for principal work remain deductible;
- **car expenses beyond one car** used partly privately at a time (s 85-25; s 86-70);
- general entity running costs beyond **entity maintenance deductions** -- the allowed list is narrow: financial-institution account fees, s 25-5 tax-related expenses, Corporations Act document/lodgment costs, statutory fees (s 86-65, applied first against the entity's other income).

Still DEDUCTIBLE (s 85-10(2) and TR 2022/3): costs of gaining work (advertising, tendering, quoting), insuring against income loss, public liability and professional indemnity premiums, GST-related amounts, engaging others (non-associates, or associates for principal work), super for those workers, and the employee-style claims themselves (running expenses for a home work area, tools, self-education with nexus). s 85-30 switches Div 85 off where the individual is conducting a PSB; s 85-35 keeps employees and office-holders out of Div 85 entirely.

### Rule 11 -- PSB does not mean safe: Part IVA and PCG 2025/5

Passing a PSB test switches off Divs 85-86 only. The note to s 86-10, TR 2022/3 (para 161's income-splitting considerations) and **PCG 2025/5** (issued 28 November 2025, finalising PCG 2024/D2; applies before and after issue) all confirm **Part IVA of the ITAA 1936** can still cancel the tax benefit from alienation arrangements -- income splitting or retention of profits -- where the dominant purpose is a tax benefit (s 177D eight-factor test; *Tupicoff*, *Gulland*, *Mochkin*, *Hart*).

| PCG 2025/5 zone | Markers | ATO posture |
|---|---|---|
| **Low risk** (Examples 1-9) | Entire net PSI assessed to the doing individual in the year earned, at marginal rates; remuneration commensurate with services; associate wages reasonable for bona fide work; superannuation for the individual; temporary retention with a genuine commercial purpose carried out; deferrals explained by events outside control (illness) | Compliance resources will not be applied |
| **Higher risk** (Examples 10-17) | Net PSI diverted so it is taxed at an overall lower rate; individual's remuneration below the value of their services; nil distribution to the doer; splitting to lower-taxed associates; associate pay not commensurate with their actual services; retention beyond commercial needs -- retention of PSI is of itself a higher-risk indicator, including where retained funds return via complying Div 7A loans | Increased likelihood of review and Part IVA consideration; materiality of the diverted amount drives prioritisation |

There is **no safe percentage of diversion** (para 41). Record-keeping expectations are extensive (contracts, timesheets, minutes, resolutions, contemporaneous purpose notes -- paras 43-47). Transitional: no Part IVA compliance pursuit for genuine moves to low-risk arrangements by **30 June 2027** (para 11). Spousal partnerships sit outside the Guideline's focus but artificial no-contribution partnerships still raise Part IVA (paras 16-17). Screening against the table is in scope; **any Part IVA position or restructure design escalates (R-AU-PSI-6)**.

### Rule 12 -- Boundaries: employees, sham contracting, and the $1,000 standard deduction

- **PSI rules do not make anyone an employee** (s 84-10): super guarantee, payroll tax, workers comp and Fair Work status are decided under their own laws.
- **Employee in substance?** If the "contractor" is actually an employee (contract-rights analysis per *Personnel Contracting* [2022] HCA 1; TR 2023/4), the payer has PAYG/SG obligations and the PSI analysis is moot. Representing an employment relationship as independent contracting risks **sham contracting** penalties (Fair Work Act ss 357-359). Reclassification questions escalate (R-AU-PSI-5).
- **Standard deduction excluded:** the up-to-**$1,000 standard deduction** for work-related expenses (Treasury Laws Amendment (Tax Reform No. 1) Act 2026 Sch 4; from 1 July 2026, first applying to 2026-27 returns) is for employment-style work income and does **not** apply to taxpayers whose relevant income is PSI or business income -- substantiated actual claims continue for them. Never net it against PSI or attributed amounts.

---

## Section 6 -- Tier 2 catalogue and refusal codes

### T2-1 / R-AU-PSI-1 -- Agents regime (s 87-40)

**Trigger:** commission agents (financial services, insurance, real estate) representing a principal but bearing entrepreneurial risk. **Issue:** s 87-40 modifies the 80% rule and unrelated clients test so the principal's customers count as the agent's clients -- but only where the agent is not an employee, receives at least **75% of the income as commission/results-based payments** (retainers count against the 75%), actively seeks customers, and does not work from the principal's premises except at arm's length. **Action:** identify the pattern, cite the conditions, REFUSE the detailed analysis and escalate.

### T2-2 / R-AU-PSI-2 -- Labour-hire and platform engagements

**Trigger:** income sourced through labour-hire firms, recruitment agencies or intermediary platforms. **Issue:** s 87-20(2) blocks the offers-to-the-public limb; separate labour-hire PAYG rules (TAA Sch 1) may apply to the payer; the worker may be an employee of the labour-hire firm. **Action:** flag that the unrelated clients test is generally unavailable; refuse characterisation of the tripartite arrangement; escalate.

### T2-3 / R-AU-PSI-3 -- Foreign PSI and non-residents

**Trigger:** PSI earned overseas, foreign residents earning Australian PSI, or attribution across borders. **Issue:** residency, source, DTA article interactions (income from employment vs independent personal services vs business profits) sit on top of Divs 84-87. **Action:** REFUSE; collect the contract, residency and location facts; escalate to a cross-border specialist.

### T2-4 / R-AU-PSI-4 -- PSBD applications

**Trigger:** client asks to apply for a PSB determination, or self-assessment is unavailable and a PSBD looks arguable. **Issue:** applications turn on evidence of unusual circumstances and forward expectations; a wrong application invites review of prior years. **Action:** identify candidacy and assemble the fact pattern only; REFUSE to prepare or lodge; escalate to the reviewer/tax agent.

### T2-5 / R-AU-PSI-5 -- Employee reclassification / sham contracting

**Trigger:** single payer, payer's tools and premises, payer control, no delegation right, or the payer asks how to "make them a contractor". **Action:** REFUSE structuring; flag PAYG, SG, payroll tax and Fair Work exposure; escalate.

### T2-6 / R-AU-PSI-6 -- Part IVA positions and alienation restructures

**Trigger:** designing salary levels, dividend/distribution flows or retention policies for a PSB; responding to an ATO Part IVA review; reliance on low-risk status for a marginal arrangement. **Action:** compute exposure and map the arrangement against the Rule 11 tables ONLY; REFUSE dominant-purpose opinions and restructure design; escalate. Check Div 7A whenever retained profits fund loans to the individual (see au-div7a).

---

## Section 7 -- Excel working paper template

```
AUSTRALIA PSI -- DECISION AND ATTRIBUTION REGISTER
Entity/individual: [name]   Test individual(s): [names]   Income year: 2026-27
Prepared: [date]

STEP 1 -- PSI IDENTIFICATION (per contract)
  Contract / client:                [____]
  Amount:                           AUD [____]
  Mainly (>50%) reward for personal efforts/skills? [Y/N -- basis]
  Goods / asset-use / business-structure component: AUD [____]

STEP 2 -- PSB TESTS (per test individual)
  Results test: % of PSI meeting result + tools + defect liability: [__%]  (need >= 75%)
  Client concentration: largest client + associates share: [__%]  (>= 80% blocks other tests)
  Unrelated clients: 2+ non-associated clients? [Y/N]  Offers to public evidenced? [Y/N]
  Employment: others perform >= 20% of principal work by market value? [Y/N]
  Business premises: mainly-PSI / exclusive / separate from home / separate from client,
    at ALL times? [Y/N x 4]
  PSBD in force? [Y/N -- years covered]
  CONCLUSION: PSB? [Y/N -- which test]

STEP 3 -- IF PSI RULES APPLY
  PSI received by entity:            AUD [____]
  less salary promptly paid (14-day rule): AUD [____]
  less deductible outgoings (employee-style + s 86-65 list): AUD [____]
  add back DENIED items:
    rent/mortgage/rates to associate residence: AUD [____]
    associate non-principal work payments:      AUD [____]
    second-car expenses:                        AUD [____]
  = NET PSI ATTRIBUTED (s 86-15/86-20): AUD [____]
  Div 13 PAYG remitted on attributed amounts? [Y/N -- amounts]

STEP 4 -- IF PSB: PCG 2025/5 SCREEN
  Net PSI assessed to the doing individual this year? [Y/N]
  Remuneration commensurate with services? [Y/N]
  Retention -- amount, stated commercial purpose, carried out? [____]
  Distributions to associates -- recipient, services provided, amount: [____]
  Zone assessment: [LOW / HIGHER -- indicators]

REVIEWER FLAGS
  [R-AU-PSI codes triggered; unresolved facts]
```

---

## Section 8 -- Reading guide

1. Identify PSI contract-by-contract before any test: the >50% "mainly" question comes first, and goods/asset components can split a single invoice.
2. The 80% rule is a gate on self-assessment, not a definition of PSI -- clients conflate them constantly.
3. Hourly rates are the tell: they usually sink the results test's first limb regardless of how skilled the work is.
4. For the unrelated clients test, count only clients won by offers to the public -- the labour-hire carve-out (s 87-20(2)) is the most-missed subsection in the Division.
5. PSB status ends the Div 85/86 analysis and starts the Part IVA one. Never write "PSI rules don't apply" without the PCG 2025/5 screen attached.

---

## Section 9 -- Reference material

### Key figures

| Item | Value |
|---|---|
| "Mainly" threshold (PSI definition) | More than 50% of the reward (s 84-5) |
| Results test coverage | >= 75% of the individual's PSI, all 3 conditions (s 87-18) |
| 80% rule | < 80% from one client + associates to self-assess the other tests (s 87-15(3)) |
| Employment test | >= 20% of principal work by market value, or apprentice(s) >= half the year (s 87-25) |
| Business premises test | All 4 conditions at all times in the year (s 87-30) |
| Salary carve-out from attribution | Paid as salary within 14 days after the PAYG payment period (s 86-15(4)) |
| Agents regime commission floor | >= 75% commission/results-based (s 87-40) |
| Standard deduction (2026-27) | Up to $1,000; work expenses; EXCLUDES PSI/business-only earners |
| PCG 2025/5 transition | Genuine move to low-risk arrangement by 30 June 2027 |

### Primary sources (verified 20 August 2026)

| Topic | Source |
|---|---|
| Statute | ITAA 1997 Part 2-42: Divs 84, 85, 86, 87 (ss 84-5, 85-10 to 85-35, 86-15, 86-20, 86-30, 86-60 to 86-70, 87-15, 87-18, 87-20, 87-25, 87-30, 87-40, 87-60, 87-65); ITAA 1936 Part IVA |
| Core ruling | TR 2022/3 Income tax: personal services income and personal services businesses |
| Part IVA guideline | PCG 2025/5 Personal services businesses and Part IVA (issued 28 Nov 2025; finalised PCG 2024/D2); PS LA 2005/24; IT 2121, IT 2330, IT 2503, IT 2639; TR 2003/6 |
| PAYG on attributed PSI | TAA 1953 Sch 1 Divs 12 and 13 |
| ATO guidance pages | PSI hub QC 16906; results test QC 46006; self-assessing/80% rule QC 46014; PSI-rules flow QC 70976; PSI decision tool QC 47696 |
| Standard deduction | Treasury Laws Amendment (Tax Reform No. 1) Act 2026 (Sch 4); ATO new-legislation page QC 107405 (updated 26 June 2026) |
| Employee/contractor | *CFMMEU v Personnel Contracting* [2022] HCA 1; *ZG Operations v Jamsek* [2022] HCA 2; TR 2023/4; Fair Work Act 2009 ss 357-359 |

### Test suite

**Test 1:** Company invoices $150,000 for its director's consulting, hourly rate, client's tools, no defect liability. -> PSI; results test fails; check 80% rule next.

**Test 2:** 75% of PSI dollars meet all three s 87-18 limbs, one client pays 95% of income. -> Results test met at exactly 75%; PSB despite concentration.

**Test 3:** Four unrelated clients (largest 40%) all sourced from a recruiter's panel. -> 80% rule met but s 87-20(2) defeats the offers-to-public limb; unrelated clients test fails.

**Test 4:** Contractor's spouse does 25% (market value) of the principal design work as an employee. -> Employment test met; PSB if <80% concentration.

**Test 5:** "Business premises" is a dedicated home-office wing. -> Fails s 87-30(c) physical separation; test not met.

**Test 6:** PSE with $200,000 PSI, $120,000 prompt salary, $10,000 deductible costs, $15,000 rent paid to the individual for his house. -> Attribution = 200,000 - 120,000 - 10,000 = $70,000; the $15,000 is denied and ignored.

**Test 7:** Deductions relating to PSI exceed the PSI by $5,000. -> Excess flows to the individual (s 86-27).

**Test 8:** PSB company pays the doer 100% of net PSI as salary + super at the cap. -> PCG 2025/5 low risk (superannuation for the individual is a low-risk indicator).

**Test 9:** PSB trust distributes 60% of net PSI to a non-working beneficiary. -> Higher risk (splitting, remuneration not commensurate); escalate R-AU-PSI-6.

**Test 10:** Employee asks to claim the $1,000 standard deduction; sole trader with only PSI asks the same. -> Employee yes (2026-27 onward); PSI earner no.

### Prohibitions

- NEVER treat an ABN, company or trust as taking income outside PSI -- structure is irrelevant to the s 84-5 definition
- NEVER use the 80% rule as the PSI definition -- "mainly" (>50%) defines PSI; 80% only gates self-assessment
- NEVER self-assess the unrelated clients, employment or business premises tests at >= 80% single-client concentration
- NEVER pass the results test on an hourly-rate contract without documented result-basis, tools and defect liability
- NEVER count labour-hire or agency panel availability as offers to the public
- NEVER deduct rent/mortgage interest to the individual or an associate, associate non-principal wages, or a second private-use car against PSI
- NEVER claim the $1,000 standard deduction against PSI
- NEVER treat PSB status as Part IVA protection -- run the PCG 2025/5 screen every time
- NEVER design salary/distribution/retention levels, prepare PSBD applications, or opine on dominant purpose -- compute, flag, escalate
- NEVER present figures as definitive

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, CA, tax agent, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://www.openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

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
