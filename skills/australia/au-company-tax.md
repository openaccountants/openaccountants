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
version: 1.2
jurisdiction: AU
tax_year: 2026
last_updated: 2026-11-27
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
reviewed_by: "Ryan Duguid"
reviewed_on: 2026-11-03
tier: 1
domain: income-tax
type: situation-rules
---

# Australia company income tax — private SME companies

## Scope

Ordinary Australian resident private companies preparing 2025–26 returns or computing 2026–27 income tax, BREPI, trust distributions, dividends, losses and PAYG instalments. The normal 2026–27 year is 1 July 2026 to 30 June 2027. Special-rate entities, trustees in that capacity and international/group computations need separate treatment. General reference only: verify the company's documents, eligibility, choices and recorded deadlines before filing or distributing.

## Ask the client first

Obtain current and prior-year assessable income, BREPI and aggregated-turnover workings; group/affiliate map; trust tax statements and tracing; accounting-to-tax reconciliation; ATO integrated client account (ICA), instalment notices and payments; continuous franking register and dividend statements; share register, rights and ownership timeline from each loss year's start; net exempt income; prior loss use; residency and offset eligibility; and agent/self-preparer status, balancing date, outstanding returns and the ATO-recorded due dates.

Unknown BREPI or grouping: show both possible rates without selecting one. Missing trust workings: hold the character and rate conclusion; treating all income as passive is a sensitivity, not a legal presumption. Missing prior-year figures or franking register: hold distribution statements. Any share movement triggers an ownership review; it does not automatically fail COT.

## Rates, bands and thresholds

| Item | Operative rule and source |
|---|---|
| Ordinary company rate, 2025–26 and 2026–27 | 25% only if BOTH current-year BRE limbs pass; otherwise 30%. Special-rate entities excluded. [ITRA s 23(2), ss 23AA–23AB](https://www.legislation.gov.au/C2004A03348/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_1/document_1.html) |
| Turnover limb | Aggregated turnover strictly less than $50 million; equality fails. Use the grouped statutory measure, not accounting revenue. [ITRA s 23AA](https://www.legislation.gov.au/C2004A03348/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_1/document_1.html) |
| Passive-income limb | BREPI no more than 80% of the company's own assessable income; equality passes. [ITRA s 23AA](https://www.legislation.gov.au/C2004A03348/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_1/document_1.html) |
| Imputation rate | Prior-year turnover, BREPI AND assessable income are substituted into the current-year rate test. If the entity did not exist in the prior year, 25%. [ITAA 1997 s 995-1](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_10/document_10.html) |
| Maximum credit | Derived from distribution × rate/(1−rate): dividend/3 at 25%; dividend × 3/7 at 30%. [ss 202-55–202-65](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_5/document_5.html); [s 995-1](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_10/document_10.html) |
| Private-company franking period | The whole income year. [s 203-45](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_5/document_5.html) |
| PAYG amount-method GDP adjustment | 4% for 2025–26; 5% for 2026–27. SAP years starting January–March 2026 retain 4%; years starting from April 2026 use 5%. Not an uplift to the rate method or annual instalments. [ATO GDP adjustment](https://softwaredevelopers.ato.gov.au/GDPupliftfactor) |
| Division 7A benchmark interest | 8.37% for year ended 30 June 2026; 8.77% for year ended 30 June 2027. SAPs require their own relevant rate. [ATO rate table](https://www.ato.gov.au/tax-rates-and-codes/division-7a-benchmark-interest-rate) |

## The method, step by step

### 1. Establish the current-year tax rate and trace bucket-company income

Apply both BRE limbs before multiplying taxable income by a rate. Aggregated turnover includes the relevant annual business turnovers of connected entities and affiliates, excludes statutory intra-group dealings and periods outside the relationship, and uses the annual-turnover adjustments. Apply the full control/affiliate tests, including discretionary-trust and indirect-control rules and exceptions; a directorship or business relationship alone is insufficient. See [ITAA 1997 ss 328-115–328-130](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_7/document_7.html). The $45m–$55m triage band is a workflow flag, not another legal threshold.

BREPI comprises corporate distributions other than qualifying non-portfolio dividends, their franking credits, non-share dividends, interest or interest-like payments, royalties, rent, qualifying-security gains, net capital gains and trust/partnership amounts referable directly or indirectly to those categories. Apply the interest exclusions for the specified finance/licensee entities and equity returns. See [ITRA s 23AB](https://www.legislation.gov.au/C2004A03348/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_1/document_1.html).

Trace trust/partnership amounts through each tier using tax workings, including reasonable expense apportionment and streaming. A franked dividend paid to a trustee and streamed to a company is not that company's non-portfolio dividend. The direct non-portfolio exception requires the statutory voting-interest conditions; do not apply it simply because the beneficiary owns an interest in a trust. Mixed licence, royalty, rent/service and interest-like receipts near the passive-income limit need classification before the rate can be used. Check this point with one of our partner accountants. See [LCR 2019/5, paragraphs 20–23](https://www.ato.gov.au/law/view/document?DocID=COG%2FLCR20195%2FNAT%2FATO%2F00001&PiT=99991231235958).

### 2. Reconcile profit, losses, tax offsets and instalments

Start with accounting profit, reconcile each income/deduction difference, deduct eligible prior losses, apply the current-year company rate, deduct eligible offsets and reconcile PAYG instalment credits to the ICA. Instalment payments are prepayments, not the accounting tax expense. Do not assume a provision is deductible when booked; check its governing deduction and timing rule. Entertainment/FBT, fines, accounting versus tax depreciation, prepayments and provisions each need separate reconciliation; this is not a universal add-back list. For an unresolved deduction treatment: Check this point with one of our partner accountants.

GIC/SIC deductions are denied for assessments for income years starting on or after 1 July 2025. For a normal 30 June balancer, remove GIC/SIC incurred from 1 July 2025; an old underlying debt does not preserve a deduction. Check the SAP's starting date rather than applying the calendar cutoff to every SAP. See [s 26-5(1A)](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html) and [ATO fact sheet, application and SAP examples](https://www.ato.gov.au/law/view/document?docid=AFS/deductions-for-ato-interest/00001).

For franked distributions received, gross-up and offset depend on Division 207 entitlement, residency and integrity conditions, including qualified-person/holding-period rules. Trust entitlement must also be established; a tax statement alone does not settle every entitlement issue. Ordinary company franking offsets are non-refundable; excess franking offsets convert to a tax loss under the statutory method, including the net-exempt-income adjustment, rather than a cash refund. See [Div 207](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_5/document_5.html) and [s 36-55](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html).

### 3. Keep the separate dividend and franking-account calculations

Compute the prior-year imputation rate separately from the current tax rate. Use the exact fraction, not a rounded gross-up factor. Stated credits above the statutory maximum are limited to the maximum. See [ss 202-60–202-65](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_5/document_5.html).

Under [ss 205-15–205-35](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_5/document_5.html), credits include eligible PAYG/income-tax liability payments, eligible direct/indirect franked receipts and FDT liability incurred. Payment includes a credit or RBA surplus applied to an existing liability; voluntary overpayments and accrued accounting tax expense do not create the same credit. Apply residency/franking-entity conditions and the R&D refund reduction before posting. Debits include credits attached to distributions, relevant income-tax refunds, under-franking and other specifically enumerated events. Ceasing with a surplus has its own debit; over-franking tax is not a generic account debit. Specialist events are a hold pending review. Check this point with one of our partner accountants.

The first frankable distribution, including one franked at zero, sets the benchmark. Later frankable distributions in the same period must match, subject to a permitted departure. Above benchmark gives over-franking tax; below benchmark gives an additional franking debit. Notify benchmark differences exceeding the statutory tolerance (20 percentage points multiplied by the relevant period count, including intervening empty periods); use ss 204-70–204-75 for the notice and timing. See [ss 203-20–203-55 and 204-70–204-75](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_5/document_5.html).

Private-company distribution statements normally must be given before the end of four months after the distribution's income year, or the later time determined by the Commissioner. That retrospective permission does not apply if the allocated credits create or increase year-end FDT; then the ordinary on-or-before-distribution deadline applies. Changes to an already issued statement require the statutory process. See [ss 202-75–202-85](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_5/document_5.html).

### 4. Check the deficit and FDT offset

A year-end deficit, or a deficit immediately before ceasing as a franking entity, triggers FDT equal to the deficit. For ordinary year-end FDT, the return/payment is normally due by the last day of the next month: nominal 31 July for a June balancer. Apply the next-business-day rule below; nominal 31 July 2027 is a Saturday. A refund within three months is deemed received before year end only if it creates or increases that deficit. The resulting return/payment generally has a 14-day refund window, with the earlier return/payment interactions in ss 214-105 and 214-150 checked separately. See [ss 205-45–205-50 and Div 214](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_5/document_5.html) and [ATO FDT guidance](https://www.ato.gov.au/businesses-and-organisations/corporate-tax-measures-and-assurance/imputation/paying-dividends-and-other-distributions/franking-account/franking-deficit-tax).

FDT creates a franking-account credit and, subject to residency and tax-offset priority, a non-refundable income-tax offset; unused offset carries forward. Reduce only the FDT attributable to s 205-70(8) debits by 30% if that attributable part exceeds 10% of the year's credits arising. Item 2 refund debits join the reduction calculation only if item 1, 3, 5 or 6 debits also exist in that year. Opening surplus is not a credit arising. The private company's first taxable year exception requires the statutory tax liability to be at least 90% of its deficit; the Commissioner can also determine in writing, on approved-form application, that the excess arose outside its control. A mixed or disputed attribution is non-usable pending review. Check this point with one of our partner accountants. See [s 205-70](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_5/document_5.html).

### 5. Carry forward losses only after continuity and deduction limits

Under [ss 165-12–165-15](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_4/document_4.html), test more than 50% voting power, dividend rights AND capital rights throughout the period from loss-year start to deduction-year end. Trace indirect ownership and apply the same-share rule and its statutory relief; do not infer rights from a bare share-count percentage. Control-purpose integrity can independently block a loss.

If COT fails or cannot practicably be shown, test business continuity throughout the claim year against the business immediately before the statutory test time. Same business is one route; similar business is available for losses of years starting on or after 1 July 2015. Its four non-exclusive factors are assets, activities/operations, identity, and development/commercialisation of the former business; the pre-test-time anti-purpose rule also applies. Net capital losses have the parallel s 165-96 restrictions. Complex trust tracing, same-share relief, control changes, Subdivision 165-CC unrealised losses and business-continuity judgements: Check this point with one of our partner accountants. See [ss 165-13, 165-96, 165-165 and 165-210–165-211](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_4/document_4.html).

Deduct eligible losses oldest first. The s 36-17 choice may be nil, but cannot create excess franking offsets; if there would already be excess franking offsets before losses the choice is nil. Net exempt income must first absorb losses as prescribed. Do not deduct an already utilised loss. See [ss 36-17 and 36-55](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html).

For 2025–26 returns, the losses schedule is required for combined tax/net capital losses carried forward over $100,000, or COT-passing losses deducted/applied over $100,000. These are not the only triggers: business continuity, unrealised net losses and relevant CFC/life-company conditions can require it regardless of the first threshold. Use all applicable instructions. See [ATO company return 2026, losses schedule](https://www.ato.gov.au/api/public/content/0-3286eec0-b61a-424a-a213-d15ed4908cdd).

### 6. Select the right loss carry-back scheme

The former temporary scheme covered losses for 2019–20 to 2022–23, with claims in 2020–21 to 2022–23 returns; historical amendments need a time-limit check. It does not govern a 2026–27 loss. The replacement was assented to on 26 August 2026, commenced on 1 October 2026 and applies to assessments for income years starting on or after 1 July 2026. The statement dated 22 September that it had not yet commenced was historical. See [Tax Reform No. 2 Act 2026 s 2 and Schedule 1 item 11](https://www.legislation.gov.au/C2026A00071/asmade/2026-08-26/text/original/epub/OEBPS/document_1/document_1.html).

For the replacement [Division 160](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_4/document_4.html):

1. Confirm corporate-tax-entity status throughout the current loss year, disregarding periods before existence; the entity must not be a significant global entity.
2. Choose either or both of the two immediately preceding years that have an income-tax liability and corporate-tax-entity status throughout (disregarding pre-existence periods).
3. Current and each of five prior years must have a lodged return, no obligation to lodge, or a Commissioner assessment.
4. Make the approved-form loss carry-back choice by current-return lodgment or a later permitted day. Allocate only available current-year loss; exclude transferred losses and loss generated by excess franking offsets under s 160-25, and apply s 160-30 scheme integrity.
5. For each selected year, reduce the carried-back loss by that year's net exempt income not already utilised, multiply by the loss-year corporate rate, and cap at that earlier year's tax liability not already used for a carry-back offset.
6. Add components and cap at the current year-end franking balance. The s 160-10(3) foreign-resident exception depends on residency for more than half of each selected earlier year and excludes NZ franking companies; international cases remain R-AU-CT-3.

Original carry-back case: a qualifying 25% company carries a $100,000 2026–27 loss against 2025–26, with no net exempt income, at least $25,000 unused earlier tax liability and a $20,000 year-end franking balance. Potential component $25,000; offset $20,000, provided every eligibility, choice, lodgment and integrity condition above is met.

### 7. File and pay for the actual company population

For ordinary full-self-assessment June-balancing agent clients' 2025–26 returns, the following are the ATO's **nominal program dates**, subject to earlier requirements, individual recorded dates and concessions. See [ATO companies program](https://www.ato.gov.au/tax-and-super-professionals/for-tax-professionals/prepare-and-lodge/registered-agent-lodgment-program/due-dates-for-tax-returns-by-client-type/companies-and-super-funds).

| Population | Nominal lodge / pay dates | Source |
|---|---|---|
| Prior-year returns outstanding at 30 June 2026; notified early/prosecution cases | 31 October 2026 / 1 December 2026 | [ATO program](https://www.ato.gov.au/tax-and-super-professionals/for-tax-professionals/prepare-and-lodge/registered-agent-lodgment-program/due-dates-for-tax-returns-by-client-type/companies-and-super-funds) |
| Large/medium, 2025 return taxable, unless earlier | 31 January 2027 / 1 December 2026 | [ATO program](https://www.ato.gov.au/tax-and-super-professionals/for-tax-professionals/prepare-and-lodge/registered-agent-lodgment-program/due-dates-for-tax-returns-by-client-type/companies-and-super-funds) |
| Large/medium non-taxable or qualifying new registrant; group exits | 28 February 2027 / 28 February 2027; group computations referred | [ATO program](https://www.ato.gov.au/tax-and-super-professionals/for-tax-professionals/prepare-and-lodge/registered-agent-lodgment-program/due-dates-for-tax-returns-by-client-type/companies-and-super-funds) |
| 2024–25 total income over $2m, unless earlier | 31 March 2027 / 31 March 2027 | [ATO program](https://www.ato.gov.au/tax-and-super-professionals/for-tax-professionals/prepare-and-lodge/registered-agent-lodgment-program/due-dates-for-tax-returns-by-client-type/companies-and-super-funds) |
| Remaining agent clients | 15 May 2027 / 15 May 2027 | [ATO program](https://www.ato.gov.au/tax-and-super-professionals/for-tax-professionals/prepare-and-lodge/registered-agent-lodgment-program/due-dates-for-tax-returns-by-client-type/companies-and-super-funds) |
| Eligible nominal May clients non-taxable/refund in both years | 5 June 2027 concession, excluding large/medium and consolidated head companies; not a new statutory due date | [ATO program](https://www.ato.gov.au/tax-and-super-professionals/for-tax-professionals/prepare-and-lodge/registered-agent-lodgment-program/due-dates-for-tax-returns-by-client-type/companies-and-super-funds) |
| Self-preparing company, unless earlier | Generally 28 February 2027; prior-year non-lodgment can bring forward to 31 October 2026 | [ATO February income-tax instructions](https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/reports-and-returns/due-dates-for-lodging-and-paying/due-dates-by-month/february) |

When a lodgment/payment date falls on a weekend or a whole-state/territory public holiday, the next business day applies. This includes a whole-state holiday even for taxpayers elsewhere. Check recorded dates and holidays; do not treat nominal dates as adjusted business-day dates. See [ATO weekend/public-holiday rule](https://www.ato.gov.au/tax-and-super-professionals/for-tax-professionals/prepare-and-lodge/registered-agent-lodgment-program/lodgment-and-payment-dates-on-weekends-or-public-holidays). SAPs, non-full-self-assessment entities and special notices require separate dates. Check this point with one of our partner accountants.

### 8. Reconcile PAYG and vary carefully

A company enters automatically if **any** company criterion applies: latest instalment income at least $2m, notional tax at least $500, or consolidated head-company status. Most pay quarterly; ordinary nominal June-balancer dates are 28 October, 28 February, 28 April and 28 July, subject to the notice and concessions. See [ATO PAYG instalments](https://www.ato.gov.au/print/section/4b6d5184-5815-43dc-9cb6-7b3f3500889f).

Monthly liability uses the MPR test and base assessment instalment income: at least $20m, with the statutory quarterly-GST branch generally preserving quarterly PAYG below $100m for a non-head company. ATO guidance also describes the annual-GST branch. Group head companies do not inherit the quarterly-GST exemption. The ordinary MPR date is the first day of the third-last month of the previous income year (1 April for a June balancer); first-entry timing and TOFA gross-income adjustments must also be checked. Monthly reporting/payment is electronic, normally due the 21st of the next month, or the 28th for deferred BAS payers. See [Schedule 1 ss 45-136–45-138](https://www.legislation.gov.au/C1953A00001/2026-05-21/2026-05-21/text/original/epub/OEBPS/document_2/document_2.html) and [ATO detailed monthly PAYG section](https://www.ato.gov.au/print/section/4b6d5184-5815-43dc-9cb6-7b3f3500889f).

The annual option is not automatic at notional tax below $8,000: at the first reporting quarter's end, check the notified tax, that the first-quarter statement has not been lodged, GST non-registration or voluntary annual-remitter status, and exclusion of instalment-group companies, consolidated heads and GST joint-venture participants. Elect through the required process. Apply the amount-method GDP factor only in its stated scope. See [ATO annual eligibility and GDP sections](https://www.ato.gov.au/print/section/4b6d5184-5815-43dc-9cb6-7b3f3500889f).

A downward variation can trigger GIC: the law compares a varied rate to 85% of the Commissioner's benchmark rate, or an estimated benchmark-tax amount to 85% of benchmark tax, with different shortfall methods. It does not impose GIC automatically on the whole difference from final total tax. Model and document the estimate; a later top-up can affect the statutory shortfall and remission may be available. Do not use a draft dynamic-instalment ruling as an operative safe harbour. For a disputed variation charge or remission: Check this point with one of our partner accountants. See [Schedule 1 ss 45-230–45-235](https://www.legislation.gov.au/C1953A00001/2026-05-21/2026-05-21/text/original/epub/OEBPS/document_2/document_2.html).

### 9. Amendments and company/shareholder boundary

The ordinary two-year amendment period for an eligible small/medium business company is subject to s 170(1) item 2's partnership, trust-beneficiary, trustee, scheme and regulatory exceptions. Turnover below $50m alone does not prove eligibility. Where items 1–3 do not apply, item 4 generally gives four years; fraud/evasion and objection/review rules are separate. For 2024–25 and later assessments, item 3A permits a taxpayer's approved-form request within four years where the ordinary two-year item applied and has expired; the amendment gives effect to that application, not an unrestricted ATO review extension. Amended assessments/extensions require their own analysis. See [ITAA 1936 s 170](https://www.legislation.gov.au/C1936A00027/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_3/document_3.html).

Payments, loans, private asset use, debt forgiveness, debit director/shareholder accounts and UPEs (including post-Bendel questions) route to **au-div7a** before sign-off. Deemed dividends are generally unfrankable, with s 109RB/109RC exceptions; loan-interest assessability and UPE/s 100A outcomes require their own facts. This Guide supplies the benchmark-rate cross-reference, not a shareholder-arrangement assessment. Check this point with one of our partner accountants. See [s 202-45(g)](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_5/document_5.html).

## Worked cases

All original case years and amounts below are retained. A conditional arithmetic result does not establish missing legal inputs.

### Example 1 — current-year BRE test

2026–27 trading company: aggregated turnover $8.0m, no connected entities, assessable income $8.24m including $40,000 bank interest, taxable income $480,000. Assume no affiliates or other BREPI. Turnover is below $50m; BREPI is $40,000/$8,240,000 = 0.4854369%, rounded to 0.5%; both limbs pass. Tax is $120,000. Source: [ss 23(2), 23AA–23AB](https://www.legislation.gov.au/C2004A03348/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_1/document_1.html).


```oa-check
name: BRE 2026-27
inputs:
  income: 8240000
  passive: 40000
  taxable: 480000
steps:
  - brepi_percent: passive / income * 100
  - tax: taxable * 0.25
expected:
  brepi_percent: 0.4854369
  tax: 120000
```

### Example 2 — dividend arithmetic

(a) At 25% imputation, a $75,000 fully franked dividend carries at most $25,000 credits, grossed up to $100,000. (b) At 30% imputation, a $70,000 fully franked dividend carries $30,000 credits (exact fraction 3/7), again $100,000 grossed up. Assume credits available, frankability, benchmark compliance and a resident qualified shareholder entitled to the offset. At the **given assumed marginal rate of 47% including Medicare on this increment**, tax on the increment is $47,000; additional shareholder tax is respectively $22,000/$17,000; combined company/shareholder tax $47,000. This is not progressive tax on an isolated $100,000 salary. Source: [ss 202-60, 207-20 and Div 207](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_5/document_5.html).


```oa-check
name: Dividends at both imputation rates
inputs:
  dividend25: 75000
  dividend30: 70000
  marginal: 0.47
steps:
  - credit25: dividend25 / 3
  - credit30: dividend30 * 3 / 7
  - shareholder25: (dividend25 + credit25) * marginal - credit25
  - shareholder30: (dividend30 + credit30) * marginal - credit30
expected:
  credit25: 25000
  credit30: 30000
  shareholder25: 22000
  shareholder30: 17000
```

### Example 3 — bucket company

The original 2026–27 $200,000 trust tax allocation consists of $140,000 net rent, $42,000 franked dividends and $18,000 franking credits. Assume these are the company's correctly attributed assessable amounts, including gross-up, with no other deductions/income, and offset entitlement established. All is traceable BREPI; the passive limb fails: $60,000 tax less $18,000 eligible offset = $42,000. The indirect franking-account credit follows statutory entitlement and timing, not merely the trust's cash-payment date. Contrast the same $200,000 wholly traceable to trading income: passive income zero; tax $50,000 **only if** current grouped turnover is below $50m. Bucket-company status alone never decides the rate. Sources: [ss 23AA–23AB](https://www.legislation.gov.au/C2004A03348/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_1/document_1.html); [ss 205-15(1) item 4 and (2), Div 207](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_5/document_5.html).


```oa-check
name: Bucket company conditional comparison
inputs:
  rent: 140000
  dividend: 42000
  credit: 18000
steps:
  - income: rent + dividend + credit
  - passive_tax: income * 0.30 - credit
  - trading_tax: income * 0.25
expected:
  income: 200000
  passive_tax: 42000
  trading_tax: 50000
```

### Example 4 — different tax and imputation rates

Grower Pty Ltd: 2026–27 grouped turnover $30m and minimal BREPI; assume both current limbs pass, giving 25% tax. Its 2025–26 grouped turnover $55m fails the prior-year threshold: 30% imputation, maximum dividend × 3/7. Reverse: Holdco is at 30% tax on 100% BREPI in 2026–27 but its prior-year figures pass both limbs: 25% imputation, dividend/3. Credits remaining are not legally stranded until a 30% year. For example, $5,000 more credits can accompany a further $15,000 frankable dividend at 25%, if profits/cash, benchmark and all distribution conditions permit. Sources: [s 995-1](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_10/document_10.html); [s 202-60](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_5/document_5.html).

### Example 5 — deficit and conditional reduction

At 30 June 2027: $5,000 opening surplus + $20,000 paid PAYG credits − $25,000 credits on a $75,000 dividend at 25% − $13,000 March 2027 income-tax refund = $13,000 deficit. Assume these are all eligible account entries. FDT $13,000; nominal due date 31 July 2027, next-business-day rule applies. If resident offset conditions hold, no first-taxable-year exception/discretion applies and all deficit is attributable to s 205-70(8) debits, $13,000 > 10% × $20,000 ($2,000): offset $9,100, reduction $3,900. The dividend debit makes the refund debit relevant to that reduction; a refund-only deficit cannot be treated identically. Future income-tax availability limits use of the offset. Source: [ss 205-45 and 205-70](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_5/document_5.html).


```oa-check
name: FDT conditional offset
inputs:
  opening: 5000
  payg: 20000
  dividendcredit: 25000
  refund: 13000
steps:
  - closing: opening + payg - dividendcredit - refund
  - gate: payg * 0.10
  - offset: 13000 * 0.70
  - reduction: 13000 - offset
expected:
  closing: -13000
  gate: 2000
  offset: 9100
  reduction: 3900
```

### Example 6 — loss and ownership change

Retailer Pty Ltd: $300,000 loss from 2023–24, founders sell 60% of shares in February 2026; recoupment sought in 2026–27. Ownership period 1 July 2023–30 June 2027. Original inputs do not specify share rights/tracing; do not conclude COT fails from share count alone. With equal ordinary rights and no qualifying relief, the sale fails continuity. Same products plus a new online channel do not by themselves prove similar business: assess all four factors and anti-purpose rule against the statutory test time throughout the claim year. **Non-usable eligibility hold:** Check this point with one of our partner accountants.

Retain the original conditional arithmetic: $450,000 before losses − $300,000 eligible loss = $150,000; at 25% tax $37,500, but only after loss eligibility, deduction choice, net exempt income, offset limits AND both current BRE limbs are established. Sources: [ss 165-12–165-13 and 165-211](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_4/document_4.html); [s 36-17](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html).


```oa-check
name: Original conditional loss and carry-back inputs
inputs:
  income: 450000
  loss: 300000
  carryloss: 100000
  prior_tax: 25000
  franking: 20000
steps:
  - taxable: income - loss
  - tax: taxable * 0.25
  - carryback: min(carryloss * 0.25, prior_tax, franking)
  - extra_credit: 15000 / 3
expected:
  taxable: 150000
  tax: 37500
  carryback: 20000
  extra_credit: 5000
```

### Original test cases 1–10

1. Turnover $8m, BREPI 0.5%, taxable $480,000: 25%/$120,000 if turnover is properly grouped and BREPI complete.
2. Turnover $30m, BREPI 100% from trust rent/dividends: 30%.
3. $75,000 dividend, 25% imputation: maximum $25,000, gross-up $100,000 if entitled.
4. $70,000 dividend, 30% imputation: maximum $30,000.
5. Current 25% tax, prior-year turnover $55m: 30% imputation.
6. Entity did not exist in prior year, maiden dividend: 25% imputation; frankability, credits and benchmark still checked.
7. Deficit $13,000, credits arising $20,000: FDT $13,000; **$9,100 offset only under Example 5's attribution/eligibility assumptions**, not from these two totals alone.
8. First interim franked 100%, later final proposed 50% in same private-company year: under-franking debit unless permitted departure; do not ignore first unfranked distributions.
9. Loss $300,000 from 2023–24, sale 60% February 2026: preserve Example 6's rights/continuity hold; similar-business route potentially available, not proven.
10. Carry back 2026–27 loss against 2025–26: run replacement Division 160, not the ended temporary scheme; distinguish commencement and application.

## When to refuse or refer

The following boundaries retain the original refusal identifiers. Do not compute specialist outcomes. Each is a non-usable hold: **Check this point with one of our partner accountants.**

| Code | Trigger / destination |
|---|---|
| R-AU-CT-1 | Consolidation, MEC, joining/leaving, ACA and single-entity questions; confirm group-specific dates |
| R-AU-CT-2 | Thin capitalisation/debt-deduction creation, foreign control, overseas borrowings; original $2m group-debt-deduction screen is a triage flag, not proof of liability |
| R-AU-CT-3 | Transfer pricing, related-party cross-border dealings, CFC, hybrids, DPT, Pillar Two, IDS and foreign-resident carry-back |
| R-AU-CT-4 | R&D registration, eligibility, offsets, feedstock and clawback; original ten-month registration reminder is a non-usable hold until the relevant deadline/extensions are confirmed |
| R-AU-CT-5 | Loss integrity, same-share relief, trust tracing, control-purpose issues, unrealised losses/value shifting and business-continuity judgement |
| R-AU-CT-6 | Deemed-dividend franking, s 109RB, dividend access shares and credit trading/holding-period opinions; use au-div7a for shareholder arrangements |

Retain T2 controls: $45m–$55m grouping review, borderline BREPI classification, franking rebuild, dual-rate governance, ownership timeline and documented instalment variation. Sweep the GL for trust income/UPE, shareholder debit accounts, tax refunds, losses/equity movements, ATO interest, deduction timing, PAYG clearing balances, grants/R&D and foreign dealings. These are review signals, not automatic tax conclusions.

The working paper must show: each current BRE limb and prior-year imputation limb; profit-to-tax adjustments and eligibility holds; losses/net exempt income and offsets in statutory order; PAYG/ICA reconciliation; opening franking balance, each dated credit/debit and closing balance; benchmark and distribution statements; FDT attribution/offset and confirmed deadlines; all R-AU-CT-1..6 flags. If only statements/trial balance are supplied, label the result provisional and list missing grouping, trust, ownership, franking and instalment evidence; no return or distribution statement is ready while a material hold remains.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, CA, tax agent, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

> Contributed by Ryan Duguid.

> Contributed by Ryan Duguid.

## Sources

Read 2026-11-27: the provisions and substantive ATO sections identified in each row. The 21 November historical ledger was reused for unchanged applicability; missing exact quotes and operative conditions were filled by the targeted reads above. Direct ATO requests returned 403; substantive official indexed text was read for the ATO rows, rather than treating the blocked responses as evidence. The source texts contain the operative sentences; derived example arithmetic is identified as such.

| Source and material read | Official URL | Read date |
|---|---|---|
| Rates, BRE and BREPI (s 23(2), ss 23AA–23AB) | [Rates, BRE and BREPI (s 23(2), ss 23AA–23AB)](https://www.legislation.gov.au/C2004A03348/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_1/document_1.html) | 2026-11-27 |
| Grouping and annual turnover (ss 328-115–328-130) | [Grouping and annual turnover (ss 328-115–328-130)](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_7/document_7.html) | 2026-11-27 |
| Prior-year imputation and gross-up definitions (s 995-1) | [Prior-year imputation and gross-up definitions (s 995-1)](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_10/document_10.html) | 2026-11-27 |
| Franking/offsets/return-payment provisions (ss 202-45–202-85, Divs 203–205, 207, 214) | [Franking/offsets/return-payment provisions (ss 202-45–202-85, Divs 203–205, 207, 214)](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_5/document_5.html) | 2026-11-27 |
| Loss continuity and replacement carry-back (Divs 160, 165) | [Loss continuity and replacement carry-back (Divs 160, 165)](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_4/document_4.html) | 2026-11-27 |
| Loss deduction, excess offsets and GIC (ss 26-5, 36-17, 36-55) | [Loss deduction, excess offsets and GIC (ss 26-5, 36-17, 36-55)](https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html) | 2026-11-27 |
| Carry-back enactment, commencement and application (s 2, Sch 1 item 11) | [Carry-back enactment, commencement and application (s 2, Sch 1 item 11)](https://www.legislation.gov.au/C2026A00071/asmade/2026-08-26/text/original/epub/OEBPS/document_1/document_1.html) | 2026-11-27 |
| Trust tracing, streaming and expense allocation (LCR 2019/5 paragraphs 20–23) | [Trust tracing, streaming and expense allocation (LCR 2019/5 paragraphs 20–23)](https://www.ato.gov.au/law/view/document?DocID=COG%2FLCR20195%2FNAT%2FATO%2F00001&PiT=99991231235958) | 2026-11-27 |
| PAYG entry, quarterly, monthly, annual and GDP sections | [PAYG entry, quarterly, monthly, annual and GDP sections](https://www.ato.gov.au/print/section/4b6d5184-5815-43dc-9cb6-7b3f3500889f) | 2026-11-27 |
| Monthly and variation operative rules (Sch 1 ss 45-136–45-138, 45-230–45-235) | [Monthly and variation operative rules (Sch 1 ss 45-136–45-138, 45-230–45-235)](https://www.legislation.gov.au/C1953A00001/2026-05-21/2026-05-21/text/original/epub/OEBPS/document_2/document_2.html) | 2026-11-27 |
| GDP factor and SAP branches, 2025–26 and 2026–27 | [GDP factor and SAP branches, 2025–26 and 2026–27](https://softwaredevelopers.ato.gov.au/GDPupliftfactor) | 2026-11-27 |
| Company June-balancer agent program rows and concession | [Company June-balancer agent program rows and concession](https://www.ato.gov.au/tax-and-super-professionals/for-tax-professionals/prepare-and-lodge/registered-agent-lodgment-program/due-dates-for-tax-returns-by-client-type/companies-and-super-funds) | 2026-11-27 |
| February self-preparer company income-tax branch | [February self-preparer company income-tax branch](https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/reports-and-returns/due-dates-for-lodging-and-paying/due-dates-by-month/february) | 2026-11-27 |
| Next-business-day and whole-state holiday rule | [Next-business-day and whole-state holiday rule](https://www.ato.gov.au/tax-and-super-professionals/for-tax-professionals/prepare-and-lodge/registered-agent-lodgment-program/lodgment-and-payment-dates-on-weekends-or-public-holidays) | 2026-11-27 |
| Year-end FDT and post-year refund timing | [Year-end FDT and post-year refund timing](https://www.ato.gov.au/businesses-and-organisations/corporate-tax-measures-and-assurance/imputation/paying-dividends-and-other-distributions/franking-account/franking-deficit-tax) | 2026-11-27 |
| GIC/SIC application and SAP examples | [GIC/SIC application and SAP examples](https://www.ato.gov.au/law/view/document?docid=AFS/deductions-for-ato-interest/00001) | 2026-11-27 |
| Company return 2026 losses-schedule triggers | [Company return 2026 losses-schedule triggers](https://www.ato.gov.au/api/public/content/0-3286eec0-b61a-424a-a213-d15ed4908cdd) | 2026-11-27 |
| Benchmark-interest table and SAP rule | [Benchmark-interest table and SAP rule](https://www.ato.gov.au/tax-rates-and-codes/division-7a-benchmark-interest-rate) | 2026-11-27 |
| Company amendment table items 2, 3A, 4–6 (s 170) | [Company amendment table items 2, 3A, 4–6 (s 170)](https://www.legislation.gov.au/C1936A00027/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_3/document_3.html) | 2026-11-27 |

Historical carry-back only: [replacement Act](https://www.legislation.gov.au/C2026A00071/asmade/2026-08-26/text/original/epub/OEBPS/document_1/document_1.html) was read operatively; former-scheme years were cross-checked against [ATO former-scheme instructions](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/losses/loss-carry-back-tax-offset/how-to-claim-the-tax-offset), read 2026-11-27.

Not yet confirmed: no usable result is offered for the specialist holds, the original ten-month R&D reminder, disputed deduction treatment or Example 6 eligibility. The original inputs remain visible; these holds use the partner-accountant referral above.
