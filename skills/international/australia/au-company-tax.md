---
name: au-company-tax
description: >
  Use this skill whenever asked about Australian company income tax for private small/medium
  companies -- the 25% base rate entity rate versus the 30% standard rate, base rate entity
  passive income (BREPI), aggregated turnover, franking dividends, maximum franking credits,
  the franking account, benchmark franking percentage, franking deficit tax, carry-forward tax
  losses (continuity of ownership or similar business test), company tax return due dates,
  PAYG instalments, or bucket companies receiving trust distributions. Trigger on phrases like
  "company tax rate", "base rate entity", "franking credits", "franking account", or "company
  losses". ALWAYS read this skill before touching any company tax work.
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

# Australia Company Income Tax -- Private SME Company Skill v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

> **Law-change context.** (1) General interest charge (GIC) and shortfall interest charge (SIC) incurred on or after 1 July 2025 are NO LONGER deductible -- 2025-26 returns (this lodgment season) are the first affected; add back any GIC/SIC in the ledger. (2) The temporary loss carry-back offset is **ENDED** -- it was claimable only in the 2020-21 to 2022-23 returns for losses of 2019-20 to 2022-23; carry-forward is the only mechanism for current losses. (3) Small/medium business amendment periods extended from 2 to 4 years for assessments for 2024-25 and later income years.

## Section 1 -- Quick reference

**Read this whole section before computing or classifying anything.**

| Field | Value |
|---|---|
| Country | Australia |
| Primary Legislation | ITAA 1997; ITAA 1936; Income Tax Rates Act 1986 (rates: s 23(2); BRE: ss 23AA, 23AB) |
| Tax Authority | Australian Taxation Office (ATO) |
| Income Year | 2026-27 (1 July 2026 -- 30 June 2027); lodgment season for 2025-26 |
| Base rate entity (BRE) rate | 25% (2021-22 onwards; 2025-26 and 2026-27 both 25%) |
| Standard company rate | 30% (all companies that are not BREs) |
| BRE test (BOTH limbs, current year) | Aggregated turnover < $50m AND base rate entity passive income (BREPI) <= 80% of assessable income |
| Corporate tax rate for imputation purposes | Tested on the PRIOR year's turnover/BREPI/assessable income; new entities default to BRE (25%) |
| Maximum franking credit | Distribution x (1 / gross-up rate); at 25%: distribution / 3; at 30%: distribution x 3/7 |
| Franking period (private company) | The whole income year -- one benchmark franking percentage per year |
| Franking deficit tax (FDT) | Deficit at year end -> franking account tax return + FDT by 31 July (30 June balancers) |
| Distribution statement (private company) | Within 4 months of the end of the income year of the distribution |
| Loss carry-forward | COT (s 165-12) or business continuity test (s 165-13: same business s 165-210; similar business s 165-211 for losses of years starting on/after 1 July 2015) |
| Loss carry-back | **ENDED** -- last claim year 2022-23; do not claim |
| Return due (2025-26, typical agent client) | 15 May 2027 lodge and pay (31 March 2027 if 2024-25 total income > $2m) |
| Return due (self-preparer small company) | Generally 28 February 2027 lodge and pay (31 October 2026 if prior years outstanding) |
| PAYG instalment GDP uplift | 5% for 2026-27 (4% for 2025-26) |
| Amendment period (SMB, aggregated turnover < $50m) | 4 years for 2024-25 onwards (2 years for 2023-24 and earlier); others 4 years |
| Contributor | Open Accountants |
| Validated by | Pending |

**Conservative defaults:**

| Ambiguity | Default |
|---|---|
| BREPI composition unknown | Compute tax at BOTH 25% and 30%; flag -- never assume 25% |
| Trust distribution received, trust workings not sighted | Assume 100% BREPI (30% rate candidate) until the trust's income is traced |
| Prior-year figures unknown (imputation rate) | Do NOT issue distribution statements; establish the prior-year test first -- wrong-rate franking creates over/under-franking |
| Aggregated turnover near $50m | Include connected entities and affiliates before concluding; flag grouping unresolved |
| Franking account balance unknown | Rebuild from ATO ICA transactions + dividend history before franking anything |
| Company in (or possibly in) a consolidated/MEC group | STOP -- R-AU-CT-1 |
| Losses carried forward + ANY share movement | Assume COT broken until the share register is reviewed |
| GIC/SIC expense in the ledger (post-1 July 2025) | Add back -- not deductible |
| Debit shareholder/director loan balance | Route to au-div7a before the return is finalised |

## Section 2 -- Refusal catalogue

Compute nothing in these areas; document the trigger and escalate to a specialist reviewer.

| Code | Trigger | Action |
|---|---|---|
| R-AU-CT-1 | Tax consolidation: forming/joining/leaving a group, ACA calculations, single-entity questions, MEC groups | Refuse; escalate. Membership changes also shift return due dates (28 February for exits) |
| R-AU-CT-2 | Thin capitalisation / debt deduction creation rules (Div 820): foreign-controlled entity, overseas borrowings, debt deductions > $2m group-wide | Refuse; escalate |
| R-AU-CT-3 | International dealings: transfer pricing, related-party cross-border transactions, CFCs, hybrid mismatches, DPT, Pillar Two, International Dealings Schedule | Refuse; escalate |
| R-AU-CT-4 | R&D tax incentive: registration, eligible activities, offset rates, clawback, feedstock | Refuse; escalate to an R&D specialist -- registration deadlines (10 months after year end) are unforgiving |
| R-AU-CT-5 | Loss integrity beyond plain COT arithmetic: Subdiv 165-CC unrealised losses, value shifting, s 165-15 injected-income schemes, SBT/similar-business judgement calls | Compute exposure only; escalate the judgement |
| R-AU-CT-6 | Franking of deemed dividends, s 109RB requests, dividend access shares, franking credit trading / 45-day rule opinions | Refuse; escalate (Div 7A mechanics live in au-div7a) |

## Section 3 -- GL sweep library

Signs a company return needs attention. Sweep the trial balance before touching the return.

| GL pattern | Likely issue | Action |
|---|---|---|
| Dividends paid / retained earnings fall with no franking working papers | Franking account never maintained | Rebuild register; check 4-month distribution statement deadline; benchmark rule |
| Interest, rent or dividend income material relative to turnover | BREPI creeping toward 80% | Run the two-limb BRE test with actual numbers (Rule 1) |
| Trust distribution receivable / income from a related trust | Rate risk: distribution may be 100% BREPI (Rule 2); UPE questions | Trace character in the TRUST's books; UPE/loan questions -> au-div7a |
| Debit balance in shareholder/director loan account | Div 7A deemed dividend risk | STOP -- run au-div7a before lodgment day |
| Income tax refund received during the year | Franking DEBIT posted; deficit risk | Recompute franking account; FDT screen (Rule 6) |
| Carried-forward losses + movement in issued shares (ASIC forms, new share classes) | COT failure | Ownership analysis (Rule 7); escalate SBT judgement (R-AU-CT-5) |
| "ATO interest", GIC, SIC expense accounts | Non-deductible from 1 July 2025 | Add back in the return; check ICA statements for accruals |
| Fines, penalties, entertainment expense | Non-deductible add-backs | Adjust; entertainment also cross-checks to FBT (au-fbt) |
| PAYG instalments in a clearing account not reconciled to the ICA | Instalments misposted as tax expense | Reconcile; instalments credit against assessed tax, they are not the expense |
| Government grants / R&D offset receivable in P&L | R&D incentive in play | R-AU-CT-4 -- escalate |
| Foreign exchange accounts, royalties paid offshore, overseas loans | International dealings | R-AU-CT-3 -- escalate; check IDS thresholds |
| Legal/consulting fees around a share sale or restructure | Possible consolidation, rollovers, loss trigger events | R-AU-CT-1 / R-AU-CT-5 |

---

## Section 4 -- Worked examples

### Example 1 -- The two-limb BRE test and the 25% rate

Trading company, 2026-27: aggregated turnover $8.0m (no connected entities), assessable income $8.24m including $40,000 bank interest; taxable income $480,000.

```
Limb 1: $8.0m < $50m                          PASS
Limb 2: BREPI = $40,000 / $8,240,000 = 0.5%   <= 80%  PASS
Rate = 25%; tax = $480,000 x 25% = $120,000
```

Both limbs are tested on CURRENT-year figures; prior-year turnover is irrelevant to the tax rate (contrast the imputation rate, Example 4).

### Example 2 -- Franking arithmetic at 25% and at 30%

**(a) BRE for imputation purposes (25%).** Company pays a $75,000 fully franked dividend.

```
Gross-up rate = (100% - 25%) / 25% = 3.0
Maximum franking credit = $75,000 x (1 / 3.0) = $25,000
Resident shareholder (top marginal 47% incl Medicare):
  Assessable = $75,000 + $25,000 gross-up = $100,000
  Tax $47,000 - franking offset $25,000 = $22,000 net
  Total tax on the $100,000 profit = $25,000 (company) + $22,000 = $47,000
```

**(b) Standard rate for imputation purposes (30%).** Company pays a $70,000 fully franked dividend.

```
Gross-up rate = (100% - 30%) / 30% = 2.3333
Maximum franking credit = $70,000 x 3/7 = $30,000
Shareholder: assessable $100,000; tax $47,000 - $30,000 = $17,000 net
```

Imputation washes company tax out at the shareholder's marginal rate either way -- but only if the franking account actually holds the credits being attached.

### Example 3 -- Bucket company: trust distributions are usually passive income

Bucket Co's only income in 2026-27 is a $200,000 distribution from a discretionary trust. The trust's net income comprised $140,000 net rental income, $42,000 franked dividends and $18,000 franking credits.

Rent, dividends and franking credits are all BREPI in the trust's hands, and a trust distribution is BREPI **to the extent it is traceable (directly or indirectly) to BREPI of the trust** (ITRA s 23AB(1)(g); LCR 2019/5). Here 100% of Bucket Co's assessable income is BREPI -> limb 2 fails -> **30% rate**:

```
Tax = $200,000 x 30% = $60,000
Less franking offset (credits flowing on the trust's franked dividends) = $18,000
Net payable = $42,000; the $18,000 also CREDITS Bucket Co's franking account
```

**Contrast:** if the same $200,000 had been wholly referable to the trust's TRADING income, BREPI = 0% -> 25% rate -> tax $50,000. Character flows through chains of trusts level by level -- get the trust's workings, never assume. Passive-heavy bucket companies are 30% companies in most years. (UPE left unpaid? Div 7A/s 100A screens -> au-div7a.)

### Example 4 -- The imputation-rate mismatch (franking at a different rate than you pay)

Grower Pty Ltd's 2026-27 aggregated turnover is $30m with minimal BREPI -> taxed at **25%**. But its 2025-26 turnover was $55m. The imputation test uses the PRIOR year: turnover $55m >= $50m -> NOT a BRE for imputation -> franks 2026-27 distributions at **30%** (max credit = dividend x 3/7).

Reverse case: Holdco is taxed at 30% in 2026-27 (100% BREPI bucket company) but last year's figures pass the BRE test -> it must frank at **25%** (max credit = dividend / 3). Tax paid at 30% enters the franking account, but each dollar of dividend can only carry out credits at the 25% rate -- credits strand in the account until a 30%-franking year. The rate you pay and the rate you frank at are set by different years' facts; establish both every year before any distribution statement is issued.

### Example 5 -- Franking account, deficit, and the FDT offset haircut

30 June 2027 franking account of a private company (franking period = full income year):

```
Opening surplus                                    $5,000 CR
PAYG instalments paid during 2026-27              $20,000 CR
Franked distribution paid ($75,000, 25% rate)     $25,000 DR
Income tax refund received March 2027             $13,000 DR
Closing balance                                    $13,000 DR (deficit)
```

FDT = $13,000, payable with a franking account tax return by **31 July 2027**. The FDT is creditable against future income tax, but the offset is REDUCED by 30% where the deficit exceeds 10% of the franking credits that AROSE during the year (here $20,000 of instalment credits -- the opening surplus is a balance, not a credit arising; $20,000 x 10% = $2,000; $13,000 > $2,000):

```
FDT offset available = $13,000 x 70% = $9,100 (the $3,900 haircut is permanent)
```

Exclusions (e.g. events outside the entity's control, Commissioner's discretion) exist -- escalate before conceding the haircut. Anti-deferral: a tax refund received within 3 months after year end is pushed back into the year for FDT purposes (return + payment due within 14 days of the refund).

### Example 6 -- Carried-forward loss, ownership change, similar business test

Retailer Pty Ltd carries forward a $300,000 tax loss from 2023-24. In February 2026 its founders sold 60% of the shares to an investor. For a 2026-27 recoupment the ownership test period runs from 1 July 2023 to 30 June 2027 -- continuity of more than 50% of voting power, dividend rights and capital rights fails at the February 2026 sale (s 165-12).

Fallback (s 165-13): the business continuity test at the test time. The company still sells the same product lines but added an online channel -- a **similar business** analysis under s 165-211 is available because the loss arose in a year starting on/after 1 July 2015 (LCR 2019/1 factors: same assets, same activities generating income, identity of the business). If satisfied:

```
2026-27 taxable income before losses  $450,000
Less prior-year loss                  $300,000
Taxable income $150,000 x 25% = $37,500
```

The SBT conclusion is a judgement call -- document the four LCR 2019/1 factors and escalate (R-AU-CT-5). Losses are deducted in the order incurred, and a company may CHOOSE how much loss to deduct (s 36-17) -- e.g. leaving income taxable to absorb franking offsets rather than wasting them.

---

## Section 5 -- Tier 1 rules

### Rule 1 -- The rate: two limbs, tested every year (ITRA ss 23AA-23AB)

25% applies for an income year only if BOTH: (1) aggregated turnover for THAT year (company + connected entities + affiliates, worked out at year end) < $50m; and (2) BREPI <= 80% of the company's own assessable income. Otherwise 30%. BREPI (s 23AB): corporate distributions and their franking credits; royalties and rent; interest (limited exceptions); gains on qualifying securities; net capital gains; and trust/partnership amounts traceable to any of those. No Commissioner discretion exists. Limb 2 tests the company's OWN income only; limb 1 is the grouped test. Companies taxed at special rates (NFP shade-in, life insurance, PDFs) are outside this skill.

### Rule 2 -- Trust and partnership distributions keep their character

A distribution is BREPI to the extent traceable, directly or through a chain, to BREPI at the source level (LCR 2019/5): apply the test at each tier, apportion expenses reasonably, and treat streamed franked dividends as retaining dividend character. A dividend paid through a trust is never a "non-portfolio dividend" (the 10% voting exception cannot apply -- the dividend is not paid to a company). Practical effect: passive-investment bucket companies are almost always 30% companies (Example 3).

### Rule 3 -- Corporate tax rate for imputation purposes (prior-year test)

To set the franking rate for year Y, assume turnover, assessable income and BREPI equal year Y-1 actuals: if those pass the BRE test (against year Y's $50m threshold), frank at 25%; if not, 30%. An entity that did not exist in Y-1 franks at 25%. Maximum franking credit = distribution x (1 / applicable gross-up rate), gross-up rate = (100% - imputation rate) / imputation rate -> divide by 3 at 25%; multiply by 3/7 at 30%. Attaching more than the maximum: the account is debited only the maximum and the shareholder only gets the maximum. The tax rate and the imputation rate regularly diverge (Example 4) -- compute both, every year.

### Rule 4 -- The franking account

A rolling ledger, not a year-end invention. CREDITS: income tax and PAYG instalments paid (to the extent they relate to taxed profits), franking credits on distributions received (directly or through trusts/partnerships), FDT liability incurred. DEBITS: franking credits on distributions paid, income tax refunds received, over/under-franking adjustments, ceasing to be a franking entity. Only tax actually PAID supports credits -- accrued tax expense is irrelevant. Companies receiving franked dividends gross up and claim a NON-REFUNDABLE offset; excess franking offsets convert into a tax loss (s 36-55) rather than a refund.

### Rule 5 -- Benchmark rule (private companies: one percentage per year)

A private company's franking period is its whole income year. The franking percentage on the FIRST frankable distribution in the period sets the benchmark; every later frankable distribution in the period must be franked to the same percentage. Franking above benchmark = over-franking tax (equal to the excess credits, not creditable to anyone); below benchmark = under-franking debit (credits wasted -- debited as if fully franked at benchmark without reaching shareholders). Disclose to the ATO where the benchmark moves by more than 20 percentage points (x intervening periods) between successive franking periods with frankable distributions. Plan the year's dividends BEFORE the first statement is issued.

### Rule 6 -- Franking deficit tax

Deficit at year end (or on ceasing to be a franking entity) -> FDT equal to the deficit; lodge a franking account tax return and pay by the last day of the month after year end (31 July for 30 June balancers). FDT liability credits the account back to nil. FDT offsets future income tax, reduced 30% where the deficit exceeds 10% of the year's franking credits (exclusions and a discretion exist -- escalate). Refunds received within 3 months of year end count as pre-year-end for the deficit calculation (14-day lodge-and-pay window). Never frank against anticipated credits without modelling the year-end balance.

### Rule 7 -- Loss carry-forward: COT then business continuity

Tax losses carry forward indefinitely but are deductible only if the company satisfies the continuity of ownership test -- persons holding more than 50% of voting power, dividend rights AND capital rights at all times from the start of the loss year to the end of the claim year (s 165-12; trace through interposed entities; same-share rule s 165-165) -- or, failing COT, the business continuity test at s 165-13: same business (s 165-210) or, for losses of income years starting on/after 1 July 2015, similar business (s 165-211; LCR 2019/1). Net capital losses follow parallel rules (s 165-96). Deduct in order incurred; s 36-17 choice as to amount (Example 6). Anti-injection rules (s 165-15) and Subdiv 165-CC escalate (R-AU-CT-5).

### Rule 8 -- Loss carry-back: ENDED

The refundable loss carry-back offset applied to losses of 2019-20 to 2022-23, claimable ONLY in the 2020-21 to 2022-23 returns (against tax paid for 2018-19 onwards, capped at the franking account surplus). It has sunset. Any current-year claim is wrong; historical claims surface only via amendment questions -- escalate those (amendment periods have largely closed).

### Rule 9 -- Lodgment and payment (2025-26 returns, 30 June balancers)

Company income tax is full self-assessment: payment is due with lodgment per the program, not on a notice. Registered agent program: 31 October 2026 lodge / 1 December 2026 pay where prior-year returns were outstanding at 30 June 2026; 31 January 2027 lodge / 1 December 2026 pay for large-medium taxpayers taxable in 2024-25; 28 February 2027 for large-medium non-taxable and new registrant large-medium; 31 March 2027 where 2024-25 total income > $2m; **15 May 2027** for the rest; 5 June 2027 concession where both years are non-taxable/refund. Self-preparer small companies: generally 28 February 2027. Late lodgment risks FTL penalties and GIC -- and GIC from 1 July 2025 is non-deductible, so late payment now costs pre-tax dollars.

### Rule 10 -- PAYG instalments interaction

Companies enter automatically with instalment income >= $2m in the latest return, notional tax >= $500, or as head of a consolidated group. Default quarterly (typically 28 October / 28 February / 28 April / 28 July); instalment income > $20m -> monthly (21st of the following month); notional tax < $8,000 -> annual option (conditions apply). Amount method instalments are uplifted by the GDP factor: **5% for 2026-27** (4% for 2025-26). Variation is allowed but a variation below 85% of the actual liability attracts GIC on the shortfall. Instalments are credited against the assessed tax in the calculation statement -- reconcile the ICA before finalising; the 2026-27 instalments raised after the 2025-26 assessment are based on that return.

### Rule 11 -- Return mechanics and add-backs

Reconcile accounting profit to taxable income on the return: add back non-deductibles (GIC/SIC from 1 July 2025, fines and penalties, entertainment not subject to FBT, accounting depreciation) and adjust for tax timing (tax depreciation, prepayments, provisions -- deductible when incurred, not provided). Franked dividends received: gross up and offset (Rule 4). Distribution statements to shareholders within 4 months of year end (private companies). Amendment periods: SMB 4 years for 2024-25 onwards (2 years for 2023-24 and earlier); other taxpayers 4 years. Keep the losses schedule and flag it where losses > $100,000 are claimed or carried.

### Rule 12 -- Div 7A boundary (cross-reference, do not duplicate)

Any payment, loan, debt forgiveness or private asset use flowing from the company to shareholders/associates, any debit loan account, and any UPE question (including post-*Bendel* treatment) is **au-div7a** territory -- run that skill before this return is signed off. The only company-return touchpoints here: deemed dividends are generally unfrankable, Div 7A loan interest is assessable income, and the 2026-27 benchmark interest rate is 8.77%.

---

## Section 6 -- Tier 2 catalogue

### T2-1 -- Turnover hovering at the $50m threshold

**Trigger:** aggregated turnover $45m-$55m, or connected-entity/affiliate status unclear. **Issue:** grouping swings both the 25% rate and SMB concessions. **Action:** map the group per the s 328-125/328-130 tests; flag; do not conclude alone.

### T2-2 -- BREPI classification edges

**Trigger:** income that resists classification -- interest-like returns, mixed licence fees vs royalties, rent vs services (serviced offices, storage). **Issue:** LCR 2019/5 characterisation drives the rate near the 80% line. **Action:** compute the ratio both ways; escalate if the rate flips.

### T2-3 -- Franking account rebuild

**Trigger:** no franking register; dividends paid historically. **Issue:** deficits and benchmark breaches may already exist; distribution statements may never have been issued. **Action:** rebuild from ICA transactions and dividend documentation since the last verified balance; flag FDT/OFT exposure.

### T2-4 -- Dual rate governance

**Trigger:** rate for tax differs from rate for imputation (Example 4), or the company's BRE status flip-flops year to year. **Issue:** distribution statements issued at the wrong rate create over/under-franking and shareholder amendments. **Action:** minute both rates at year start; re-check before each dividend.

### T2-5 -- Loss schedule with ownership noise

**Trigger:** losses claimed plus any equity movement, share buy-back, new class of shares, or trustee shareholders. **Issue:** COT tracing through trusts is technical (family trust elections change the analysis). **Action:** build the ownership timeline; escalate FTE/SBT questions (R-AU-CT-5).

### T2-6 -- Instalment variations in a falling year

**Trigger:** client wants instalments varied down mid-year. **Issue:** variation below 85% of actual attracts GIC -- now non-deductible. **Action:** model the full-year estimate before varying; document the basis.

---

## Section 7 -- Excel working paper template

```
AUSTRALIA COMPANY TAX -- RETURN WORKING PAPER
Company: [name]   Income year: [2025-26 / 2026-27]   Balancer: 30 June
Prepared: [date]

RATE TEST (CURRENT YEAR -- Rule 1)
  Aggregated turnover (co + connected + affiliates): AUD [____]  < $50m? [Y/N]
  Assessable income:               AUD [____]
  BREPI (dividends+credits, rent, royalties, interest,
         net capital gain, traceable trust/partnership amounts): AUD [____]
  BREPI %:                         [____]%  <= 80%? [Y/N]
  RATE: [25% / 30%]

IMPUTATION RATE TEST (PRIOR YEAR -- Rule 3)
  Prior-year turnover / BREPI % :  AUD [____] / [____]%
  Imputation rate: [25% / 30%]   Max credit per $ of dividend: [1/3 | 3/7]

TAXABLE INCOME RECONCILIATION
  Accounting profit:               AUD [____]
  + GIC/SIC (post-1 Jul 2025), fines, entertainment, accounting depn: AUD [____]
  - Tax depreciation / other timing: AUD [____]
  + Franking credit gross-up on dividends received: AUD [____]
  - Prior-year losses applied (COT/BCT confirmed, order incurred): AUD [____]
  Taxable income:                  AUD [____]
  Tax @ [25/30]%:                  AUD [____]
  - Franking offsets (non-refundable; excess -> loss s 36-55): AUD [____]
  - PAYG instalments credited (per ICA): AUD [____]
  Payable / (refundable):          AUD [____]

FRANKING ACCOUNT
  Opening balance:                 AUD [____]
  + Tax/instalments paid; credits on dividends received: AUD [____]
  - Credits on dividends paid; refunds received: AUD [____]
  Closing balance:                 AUD [____]  Deficit? -> FDT by 31 July
  Benchmark % this franking period: [____]%  All distributions at benchmark? [Y/N]
  Distribution statements issued within 4 months? [Y/N]

FLAGS
  Div 7A candidates routed to au-div7a: [____]
  Refusal triggers hit (R-AU-CT-1..6): [____]
```

---

## Section 8 -- Reading guide

1. Rate first, return second: run both limbs of the BRE test on real numbers before any tax computation -- and run the SEPARATE prior-year test before any dividend is franked.
2. Trust distributions: character is set in the trust's books, not the company's. No trust workings = assume passive = 30% until proven otherwise.
3. The franking account is continuous. Every instalment, refund and dividend moves it; the year-end balance decides FDT, not intentions.
4. Losses: the share register is the evidence, not the client's memory. Any transfer, issue or redemption inside the ownership test period reopens the analysis.
5. Payment dates are lodgment-linked for most SMEs (full self-assessment) -- lodging early does not delay payment beyond the program date, and lodging late compounds FTL penalties with non-deductible GIC.

---

## Section 9 -- Onboarding fallback

If the client provides only financial statements and a trial balance:

1. Run the Section 3 sweep; list rate-risk income lines and Div 7A candidates
2. Compute the BRE test both years (rate + imputation rate) from the figures given
3. Draft the taxable income reconciliation with add-backs visible
4. Rebuild the franking account from the ICA and any dividend statements sighted
5. **Flag:** "Computed from financial statements only. Aggregated turnover grouping, trust distribution character, share register continuity, franking history and instalment reconciliation not verified. Reviewer must confirm before lodgment or any distribution statement is issued."

---

## Section 10 -- Reference material

### Key figures (2025-26 and 2026-27)

| Item | 2025-26 | 2026-27 |
|---|---|---|
| BRE rate / standard rate | 25% / 30% | 25% / 30% |
| Aggregated turnover threshold | $50m | $50m |
| BREPI limb | <= 80% of assessable income | <= 80% |
| Max franking credit (25% / 30% imputation rate) | dividend/3 or dividend x 3/7 | same |
| FDT due (30 June balancer) | 31 July 2026 | 31 July 2027 |
| PAYG GDP uplift | 4% | 5% |
| Div 7A benchmark rate (see au-div7a) | 8.37% | 8.77% |
| GIC/SIC deductibility | Not deductible (from 1 Jul 2025) | Not deductible |
| Loss carry-back | ENDED | ENDED |

### Primary sources (verified 20 August 2026)

| Topic | Source |
|---|---|
| Rates and BRE definition | Income Tax Rates Act 1986 ss 23(2), 23AA, 23AB; ato.gov.au Changes to company tax rates (QC 54063, updated 27 May 2026) |
| BREPI and trust tracing | LCR 2019/5 Base rate entities and base rate entity passive income; TR 2019/1 |
| Imputation rate and max credit | ato.gov.au Allocating franking credits (QC 47305); ITAA 1997 Div 202, s 995-1 (corporate tax rate for imputation purposes) |
| Franking account / FDT | ITAA 1997 Div 205; ato.gov.au Franking deficit tax (QC 47303); Franking account tax return and instructions 2026 |
| Benchmark rule / franking periods | ITAA 1997 Div 203, s 204-75; ato.gov.au Benchmark rule and Franking period pages |
| Distribution statements | ITAA 1997 Subdiv 202-E; ato.gov.au Issuing distribution statements (4-month private company rule) |
| Losses | ITAA 1997 Div 36 (ss 36-17, 36-55), Div 165 (ss 165-12, 165-13, 165-96, 165-210, 165-211); LCR 2019/1 |
| Loss carry-back (ENDED) | Former Div 160 ITAA 1997; ato.gov.au Loss carry back tax offset (2019-20 to 2022-23 only) |
| Lodgment program | ato.gov.au Companies and super funds -- agent lodgment program (QC 34562, updated 1 July 2026); Income tax return -- companies (28 February self-preparer) |
| PAYG instalments | ato.gov.au PAYG instalments (entry $2m/$500; monthly > $20m); GDP adjustment 5% for 2026-27 |
| Amendment periods | ato.gov.au Request an amendment to a business or super tax return (SMB 4 years from 2024-25) |
| GIC/SIC deduction denial | Treasury Laws Amendment (Tax Incentives and Integrity) Act 2025 (No. 29, 2025) Sch 2; ato.gov.au QC 73746 -- GIC/SIC incurred from 1 July 2025 not deductible |

### Test suite

**Test 1:** Turnover $8m, BREPI 0.5%, taxable income $480,000. -> 25%; tax $120,000.

**Test 2:** Turnover $30m, BREPI 100% (all trust-sourced rent/dividends). -> Limb 2 fails; 30%.

**Test 3:** $75,000 dividend at 25% imputation rate. -> Max credit $25,000; shareholder grosses up to $100,000.

**Test 4:** $70,000 dividend at 30% imputation rate. -> Max credit $30,000 ($70,000 x 3/7).

**Test 5:** Taxed at 25% this year; prior-year turnover $55m. -> Franks at 30% regardless of current rate.

**Test 6:** New company incorporated this year pays a maiden dividend. -> No prior year -> BRE for imputation -> franks at 25%.

**Test 7:** Franking account deficit $13,000; credits arising in the year $20,000. -> FDT $13,000 by 31 July; deficit > 10% of credits -> offset reduced to $9,100.

**Test 8:** First interim dividend franked 100%; final dividend proposed at 50%. -> Benchmark breach: under-franking debit on the final (credits wasted); same-year distributions must match the benchmark.

**Test 9:** $300,000 loss from 2023-24; 60% share sale Feb 2026. -> COT fails; similar business test available (loss year starts post-1 July 2015); escalate the SBT judgement.

**Test 10:** Client asks to carry back a 2026-27 loss against 2025-26 tax. -> Refuse: carry-back ENDED (last claim year 2022-23); carry forward instead.

### Prohibitions

- NEVER apply 25% without BOTH current-year limbs verified (turnover grouped; BREPI traced)
- NEVER set the franking rate from current-year status -- the imputation rate uses PRIOR-year figures
- NEVER frank above the maximum credit or away from the period's benchmark percentage
- NEVER treat a trust distribution as active income without the trust's workings
- NEVER claim loss carry-back -- the measure has ENDED
- NEVER deduct GIC or SIC incurred on or after 1 July 2025
- NEVER deduct carried-forward losses across an ownership change without COT/BCT analysis on the share register
- NEVER issue distribution statements while the franking account balance is unverified
- NEVER compute consolidation, thin cap, transfer pricing or R&D claims -- escalate (Section 2)
- NEVER present figures as definitive

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, CA, tax agent, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://www.openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

> Contributed by Ryan Duguid.

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
