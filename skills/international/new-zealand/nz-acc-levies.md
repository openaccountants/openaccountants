---
name: nz-acc-levies
description: Use this skill whenever asked about New Zealand ACC levies for self-employed individuals. Trigger on phrases like "ACC levy", "earner levy", "work levy", "CoverPlus", "CoverPlus Extra", "accident compensation", "ACC invoice", "classification unit", or any question about ACC obligations for sole traders in New Zealand. Covers earner levy, work levy by classification unit (CU), CoverPlus/CoverPlus Extra, maximum liable earnings, and payment schedules. ALWAYS read this skill before touching any NZ ACC work.
version: 2.0
jurisdiction: NZ
tax_year: 2026
last_updated: 2026-09-22
review_status: pending_review
drafted_by: OpenAccountants
approved_by: pending
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# ACC levies in New Zealand for the self-employed and employers

How the Accident Compensation Corporation (ACC) levies work for sole traders, contractors, active look-through company owners and employers in New Zealand: the Earners' levy, the Work levy by classification unit (CU), the Working Safer levy, CoverPlus and CoverPlus Extra, maximum liable earnings, and the invoice cycle. Figures are for tax year 2026. In New Zealand that is the levy year from 1 April 2026 to 31 March 2027, which Inland Revenue calls the 2027 income year. The Earners' levy figures come from Inland Revenue's rate page and its employer's guide (IR335) for the tax year ending 31 March 2027. The average Work levy comes from the ACC levy consultation report published in the New Zealand Gazette in 2025. One limit matters most. ACC publishes the Work levy rate for each classification unit, and the Working Safer levy rate, only on its own website, which this Guide cannot link or read. So this Guide prints no industry rate. Read the client's rate from ACC's levy guidebook or from the client's ACC invoice.

## Section 1: Quick reference

**Quick reference fields**

| Field | Value |
| --- | --- |
| Country | New Zealand |
| Jurisdiction Code | NZ |
| Primary Legislation | Accident Compensation Act 2001 (AC Act) |
| Supporting Legislation | Injury Prevention, Rehabilitation, and Compensation Act 2001 |
| Authority | Accident Compensation Corporation (ACC). Inland Revenue collects the employees' Earners' levy through PAYE |
| Online account | MyACC for Business, ACC's online platform for levy accounts |
| Levy year | 1 April 2026 to 31 March 2027 (Inland Revenue: 2027 income year) |
| Currency | NZD only |
| Earners' levy rate | 1.75% (includes GST). See the Inland Revenue table below |
| Maximum liable earnings (Earners' levy) | NZD 156,641. See the Inland Revenue table below |
| Work levy rate | Set by ACC for each classification unit. Not printed here. Read it from the ACC invoice or ACC's levy guidebook |
| Working Safer levy rate | Collected by ACC on behalf of MBIE and shown on the ACC invoice. Not printed here |
| Contributor | Open Accountants Community |
| Validated By | Pending. Requires sign-off by a New Zealand chartered accountant |
| Validation Date | Pending |
| Confidence Coverage | Tier 1: Earners' levy rate and maximum, invoice cycle, who pays what. Tier 2: CU selection, CoverPlus Extra, experience rating. Tier 3: claims management, dispute resolution, complex multi-business structures |

Read this whole section before computing anything.

**ACC Earners' levy: Inland Revenue rate page**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.ird.govt.nz/income-tax/income-tax-for-individuals/acc-clients-and-carers/acc-earners-levy-rates |
| Earners' levy rate, 1 April 2026 to 31 March 2027 (this Guide's year). Flat rate on each dollar of liable earnings up to the maximum. Includes GST | 1.75% | "1 April 2026 to 31 March 2027 $1.75 per ... (1.75%)"; "These amounts include GST." |
| Maximum liable earnings, 1 April 2026 to 31 March 2027. No Earners' levy on earnings above it (a ceiling, not a cliff). Per person, per year | NZD 156,641 | "1 April 2026 to 31 March 2027 $156,641 $2,741.22" |
| Maximum Earners' levy payable, 1 April 2026 to 31 March 2027 | NZD 2,741.22 | "Maximum levy payable" |
| Earners' levy rate, 1 April 2027 to 31 March 2028 (NEXT year; do not use for 2026-27) | 1.83% | "1 April 2027 to 31 March 2028 $1.83 per ... (1.83%)" |
| Maximum liable earnings, 1 April 2027 to 31 March 2028 (NEXT year) | NZD 160,244 | "1 April 2027 to 31 March 2028 $160,244" |
| Earners' levy rate, 1 April 2025 to 31 March 2026 (last year; history) | 1.67% | "1 April 2025 to 31 March 2026 $1.67 per ... (1.67%)" |
| Maximum liable earnings, 1 April 2025 to 31 March 2026 (last year; history) | NZD 152,790 | "1 April 2025 to 31 March 2026 $152,790" |
| Maximum liable earnings, 1 April 2024 to 31 March 2025 (history; the figure the old version of this Guide used) | NZD 142,283 | "1 April 2024 to 31 March 2025 $142,283" |

Inland Revenue's news item of 11 March 2025 says the Earners' levies "have now been set for the 2025-26, 2026-27 and 2027-28 tax years".

**ACC Earners' levy through PAYE: employer's guide (IR335)**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir335/ir335.pdf |
| Earners' levy rate for the tax year ending 31 March 2027. Already included in PAYE | 1.75% | "The rate for the tax year ending 31 March 2027 is 1.75%. PAYE includes ACC earners' levy already" |
| Maximum earnings per weekly pay | NZD 3,012 | "$3,012 per weekly pay" |
| Maximum earnings per fortnightly pay | NZD 6,024 | "$6,024 per fortnightly pay" |
| Maximum earnings per 4-weekly pay | NZD 12,048 | "$12,048 per 4-weekly pay" |
| Maximum earnings per monthly pay | NZD 13,053 | "$13,053 per monthly pay" |

IR335 says the maximum does not apply to PAYE on regular secondary income, casual agricultural employee payments, election day workers' earnings, or earnings taxed at the non-notified rate.

**ACC Work levy: the national average only (Gazette)**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://gazette.govt.nz/notice/id/2025-au1361 |
| AVERAGE Work levy for 2026/27, for each hundred dollars of liable earnings, as decided by the Government. An average across all industries. It is NOT the rate for any classification unit and must never be used to compute a client's levy | NZD 0.69 | "Work levy ... 2026/27 $0.69 $0.69" |

The same report says: "the levy rate for each classification unit will be updated to reflect any changes in its claim patterns. This means that the levy rates for some businesses will decrease when the average rate is increasing". A client's own Work levy can move in the opposite direction to the average.

**ACC levies explained for business: business.govt.nz**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.business.govt.nz/tax-and-money/guide-to-business-tax/acc-levies |
| Weekly compensation if unable to work because of a covered injury: up to this share of income | 80% | "ACC will pay up to 80% of your income if you're unable to work because of an injury that's covered by ACC" |

**ACC levy components**

| Levy | Who Pays | Rate |
| --- | --- | --- |
| Earners' levy (non-work injury cover) | Employees through PAYE; self-employed people on their ACC invoice | 1.75% up to NZD 156,641 (includes GST) |
| Work levy (ACC workplace cover) | Employers, for their employees; self-employed people, for themselves | Set by ACC for the classification unit (CU). Read it from the ACC invoice |
| Working Safer levy | Businesses and self-employed people; collected by ACC for MBIE to support WorkSafe NZ | Read it from the ACC invoice |

**Work levy rates by CU**

The old version of this Guide printed "illustrative" Work levy and Working Safer levy rates for seven classification units. No allowed official page prints any of them, so they are removed. The rate for a given industry is set by ACC for its classification unit and must be read from ACC's levy guidebook, ACC's levy calculators, or the client's ACC invoice. Do not quote a CU rate from memory.

**CoverPlus vs CoverPlus Extra**

| Feature | CoverPlus (Default) | CoverPlus Extra (CPX) |
| --- | --- | --- |
| Who is on it | Every sole trader starts on it automatically | Chosen by the self-employed person instead of CoverPlus |
| Compensation basis | Up to 80% of income, worked out from the last self-employed tax return | Agreed level of cover chosen by the client |
| Levy basis | Type of work (CU) and liable earnings | Agreed level of cover |
| Invoice timing | After the annual tax return is filed, usually in September | Shortly after the policy is approved, then every April when it renews |

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown CU | Flag for reviewer. The CU sets the Work levy rate. Ask for the ACC invoice |
| Unknown CoverPlus option | CoverPlus (default) |
| Unknown GST status | Do not add GST to the Earners' levy rate: Inland Revenue prints it including GST. Read the GST lines on the ACC invoice |
| Unknown liable earnings | Use the most recent income tax return figure, and say it is an estimate |

## Section 2: Required inputs and refusal catalogue

### Required inputs

- **Required inputs before computing ACC levy.** Before computing any ACC levy figure, you MUST know: (1) status: sole trader, partner, contractor on schedular payments, active or passive look-through company owner, shareholder-employee, or employer; (2) the client's classification unit and its Work levy rate, from the ACC invoice; (3) liable earnings, from the income tax return; (4) CoverPlus or CoverPlus Extra; (5) whether the No Claims Discount or Experience Rating Programme changes the Work levy; (6) the levy year, because self-employed invoices are usually based on the year before.
- **PAYE employee only.** If the client only earns salary or wages, their Earners' levy is already deducted through PAYE and they get no ACC invoice of their own. Their employer pays the Work levy for them. STOP: there is nothing to compute beyond what PAYE already took.
- **Contractors on schedular payments.** Withholding tax is deducted from schedular payments, but not the Earners' levy (IR335). These contractors are self-employed for ACC and get an ACC invoice. business.govt.nz lists "not realising you'll get an ACC invoice" as a common mistake.

### Refusal catalogue

- **R-NZ-ACC-1: Claims management.** Trigger: client asks about managing an ACC claim or rehabilitation. Message: "ACC claims management and rehabilitation are outside this Guide's scope. Please contact ACC directly on 0800 101 996."
- **R-NZ-ACC-2: Dispute resolution.** Trigger: client disputes an ACC levy or classification. Message: "ACC levy disputes and CU reclassification require direct engagement with ACC. This Guide cannot advise on dispute procedures. Please escalate to a qualified New Zealand chartered accountant."
- **R-NZ-ACC-3: Complex multi-business structures.** Trigger: client has several business entities in different CUs. Message: "Multi-entity ACC structuring requires case-specific analysis. Please escalate to a qualified New Zealand chartered accountant."

## Section 3: Payment pattern library

This is the deterministic pre-classifier for bank statement entries related to ACC. Match by case-insensitive substring.

### 3.1 ACC levy payments

**ACC levy payments patterns**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| ACC, ACCIDENT COMPENSATION | ACC LEVY PAYMENT | Yearly levy payment, one-off or instalment |
| ACC LEVY, ACC INVOICE | ACC LEVY PAYMENT | Same |
| ACC COVERPLUS, COVERPLUS EXTRA | ACC LEVY PAYMENT | CoverPlus or CoverPlus Extra invoice payment |

### 3.2 ACC provisional invoicing

**ACC provisional invoicing patterns**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| ACC PROVISIONAL, ACC ESTIMATE | PROVISIONAL LEVY | Employers: estimate for the current year, based on the previous year's liable earnings and expected wages |
| ACC ADJUSTMENT, ACC REFUND | LEVY ADJUSTMENT | Difference for the previous year: an extra invoice if underpaid, a credit on the account if overpaid |

### 3.3 GST treatment

**GST treatment pattern**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| ACC invoice with a GST line | CHECK GST | Inland Revenue prints the Earners' levy rate including GST. Whether the GST on an ACC invoice is claimable as input tax is not shown on an allowed page: confirm before claiming |

### 3.4 IRD payments (income return triggers ACC)

**IRD payment patterns**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| IRD, INLAND REVENUE NZ | TAX PAYMENT | Not an ACC levy. ACC gets income details from Inland Revenue |
| IR3 FILED | ACC TRIGGER | Filing the income tax return triggers the CoverPlus invoice |

## Section 4: Levy computation rules

### 4.1 Levy computation steps (Tier 1)

**Levy computation steps** _(Accident Compensation Act 2001; rates as set for each levy year)_

| Step | Action |
| --- | --- |
| 4.1 | Determine liable earnings: net self-employment income from the income tax return (for CoverPlus, usually the year before) |
| 4.2 | For the Earners' levy, cap earnings at the maximum for the levy year (NZD 156,641 for 2026-27) |
| 4.3 | Earners' levy = capped liable earnings x 1.75%. This rate already includes GST: do not add GST again |
| 4.4 | Work levy = liable earnings x the Work levy rate for the client's CU, taken from the ACC invoice or ACC's levy guidebook. Never use the Gazette average |
| 4.5 | Working Safer levy = liable earnings x the Working Safer rate on the ACC invoice |
| 4.6 | Adjust the Work levy for any No Claims Discount or Experience Rating shown on the invoice |
| 4.7 | Total = the three levies. Label every total an estimate until the ACC invoice arrives |

Whether the Work levy and Working Safer levy are also capped at the maximum liable earnings is not printed on an allowed page. Read it from the ACC invoice or guidebook.

### 4.2 CoverPlus (Default) (Tier 1)

- **CoverPlus compensation basis.** ACC pays up to the share of income in the business.govt.nz table if the client cannot work because of a covered injury. ACC calculates it from income in the last self-employed tax return. The levy is based on the type of work and liable earnings, and the invoice arrives after the tax return is filed, usually in September.

### 4.3 CoverPlus Extra (Tier 2)

- **CoverPlus Extra compensation basis.** The self-employed person agrees a level of cover with ACC, which gives more control over how much income ACC covers. The levy is invoiced against that agreed level shortly after the policy is approved, then every April when it renews. Flag for reviewer: cover can end up higher or lower than actual earnings. Advise the client to review it every year.

## Section 5: Payment and invoicing

### 5.1 Invoicing (Tier 1)

**Invoicing details** (source: https://www.business.govt.nz/tax-and-money/guide-to-business-tax/acc-levies)

| Detail | Value |
| --- | --- |
| Self-employed on CoverPlus | Once a year, after the income tax return is filed, usually in September. Usually based on the year before |
| Self-employed on CoverPlus Extra | Every April, when the policy renews |
| Employers and shareholder-employers | First invoice usually after the tax return is filed, then once a year, usually in July |
| Payment options | Internet banking, credit card (a service fee applies), or direct debit, as a one-off payment or in instalments |
| Due date | The due date on the invoice. Pay by it even while waiting for a reassessment |
| Late payment | "you may face a penalty for late payment" |

### 5.2 Provisional invoicing (Tier 1)

- **Provisional invoicing process.** An employer's yearly invoice has two parts: a provisional levy for the current year (an estimate based on the previous year's liable earnings and the wages expected in the coming year) and an adjustment for the previous year (an extra invoice if too little was paid, a credit if too much). If circumstances change, the employer can ask ACC to reassess using form ACC4618. A self-employed person on CoverPlus is invoiced after filing, based on the earnings of the year before.

## Section 6: GST and deductibility

### 6.1 GST treatment (Tier 1)

- **GST treatment on ACC levies.** Inland Revenue prints its table of Earners' levy rates under the words "These amounts include GST" (see the first table). The maximum levy is that rate applied to the maximum earnings. The old version of this Guide said all levies were GST-exclusive with GST added on top; for the Earners' levy that is contradicted and is removed. How GST appears on the Work levy and Working Safer levy lines, and whether a GST-registered person can claim the GST on an ACC invoice as input tax, is not printed on an allowed page. Read the invoice and confirm before claiming.

### 6.2 Income tax deductibility (Tier 2)

- **Deductibility of ACC levies.** Inland Revenue says this only on its page for ACC carers: "If you're self employed, you can claim vehicle expenses and ACC levies as expenses" (https://www.ird.govt.nz/income-tax/income-tax-for-individuals/acc-clients-and-carers/acc-carers). The same page adds that most carers are not treated as self employed. No allowed page states a general rule for every self-employed person or employer, or says which levies it covers. Flag for reviewer: a New Zealand chartered accountant should confirm deductibility before it is relied on.

## Section 7: Edge case registry

### EC1: Multiple business activities (Tier 2)

Situation: Client runs a software consultancy and a construction side business.
Resolution: ACC assigns the CU from the Business Industry Classification (BIC) code, which the client chooses for their main work activity when registering for GST or filing a tax return (business.govt.nz). How ACC treats two activities of similar size is not on an allowed page. Flag for reviewer.

### EC2: First year of self-employment (Tier 1)

Situation: Client started freelancing in March 2026. No earlier income tax return.
Resolution: The first ACC invoice is triggered when the first individual income tax return is filed, which is usually in the second year of business. After that the client is invoiced yearly, usually on the earnings of the year before (business.govt.nz). Warn the client to set money aside. The old version of this Guide said ACC "will estimate levies or use the minimum"; no allowed page says so.

### EC3: Self-employed AND employee (Tier 1)

Situation: Client has PAYE employment and a freelance side business.
Resolution: PAYE already includes the Earners' levy on the wages. The Work levy on the job is the employer's. The self-employment income is invoiced by ACC for the Earners' levy, Work levy and Working Safer levy. How the Earners' levy maximum is shared between the two sources is not printed on an allowed page. Flag for reviewer.

### EC4: Earnings exceed maximum (Tier 1)

Situation: Consultant's net self-employment income for 2026-27 is well above the maximum liable earnings.
Resolution: The Earners' levy is charged only up to NZD 156,641 and cannot exceed NZD 2,741.22 (first table). The old version of this Guide capped at NZD 142,283 which was the 2024-25 maximum.

### EC5: Client disputes CU classification (Tier 2)

Situation: Client classified as building construction but mainly does office-based project management.
Resolution: The CU follows the BIC code. business.govt.nz says to tell ACC if the business activity has changed. The CU sets the Work levy rate and can change costs a lot. Flag for reviewer.

### EC6: GST on ACC levies (Tier 1)

Situation: GST-registered sole trader receives an ACC invoice.
Resolution: Do not add GST on top of the Earners' levy rate: Inland Revenue prints it including GST. Read the GST shown on the invoice. The input tax claim is not confirmed on an allowed page (Section 6.1).

### EC7: Look-through company owner (Tier 2)

Situation: Client owns shares in a look-through company.
Resolution: A passive investor pays no ACC levies on look-through company income. An owner who plays an active part in generating the income is self-employed for ACC, and ACC invoices them directly (https://www.ird.govt.nz/income-tax/income-tax-for-businesses-and-organisations/income-tax-for-companies/look-through-companies/acc-levies-for-a-look-through-company). For a working owner's salary, Inland Revenue's pages differ. The look-through company page says the earners' levy "will be deducted as part of PAYE from your salary or wages". The employer's guide IR335, page 18, lists "salaries to working owners of a look-through company" among payments not to deduct the ACC earners' levy from (https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir335/ir335.pdf). Flag for reviewer.

### EC8: Shareholder-employee without PAYE (Tier 1)

Situation: A close company pays a shareholder-employee salary with no PAYE deducted.
Resolution: ACC invoices the close company employer for the Earners' levy on that remuneration, based on the shareholder-employee remuneration declared in the company's IR4 return (IR335, page 18).

## Section 8: Reviewer escalation protocol

When a Tier 2 situation is identified:

~~~
REVIEWER FLAG
Tier: T2
Client: [name]
Situation: [description]
Issue: [what is ambiguous]
Options: [possible treatments]
Recommended: [most likely correct treatment and why]
Action Required: Qualified NZ chartered accountant must confirm before advising client.
~~~

When a Tier 3 situation is identified:

~~~
ESCALATION REQUIRED
Tier: T3
Client: [name]
Situation: [description]
Issue: [outside Guide scope]
Action Required: Do not advise. Refer to qualified NZ chartered accountant. Document gap.
~~~

## Section 9: Test suite

The old tests used Work levy and Working Safer rates that no allowed page prints, so their totals are removed. These tests check method, not amounts.

### Test 1: Standard software consultant

Input: sole trader on CoverPlus, liable earnings below the maximum, CU rate unknown.
Expected output: Earners' levy = earnings x 1.75%, no GST added. Work levy and Working Safer levy: ask for the ACC invoice; do not use the Gazette average. Total labelled an estimate.

### Test 2: High earner hitting cap

Input: liable earnings for 2026-27 well above the maximum.
Expected output: Earners' levy capped at NZD 2,741.22 on NZD 156,641. Not the 2024-25 maximum of NZD 142,283 and not the 2027-28 rate of 1.83%.

### Test 3: Builder (high-risk CU)

Input: builder on CoverPlus, no invoice supplied.
Expected output: Earners' levy as in Test 1. Refuse to print a Work levy rate; explain that the builder's CU rate comes from ACC's levy guidebook or invoice and may differ a lot from the average.

### Test 4: Low-income first-year freelancer

Input: freelancer in the first year of business, no tax return filed yet.
Expected output: no ACC invoice yet; the first invoice follows the first income tax return, usually in the second year. Advise setting money aside.

## Section 10: Prohibitions and disclaimer

### Prohibitions

- NEVER assume Work levy rates are the same for all industries. They vary by classification unit
- NEVER use the Gazette average Work levy as a client's rate
- NEVER print a CU rate or Working Safer rate from memory or from an old version of this Guide
- NEVER charge the Earners' levy on earnings above the maximum liable earnings
- NEVER add GST on top of the Earners' levy rate Inland Revenue publishes: it already includes GST
- NEVER use the 2027-28 row of Inland Revenue's table for 2026-27
- NEVER confuse CoverPlus (default, based on earnings) with CoverPlus Extra (agreed level of cover)
- NEVER omit the Earners' levy. It applies to employees through PAYE and to the self-employed on their invoice
- NEVER present calculations as definitive. Label them estimates and direct the client to the ACC invoice or a qualified New Zealand chartered accountant

## The method, step by step

1. Place the person. Employee only: PAYE already includes the Earners' levy (IR335: https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir335/ir335.pdf). Sole trader, contractor on schedular payments or active look-through company owner: self-employed for ACC and invoiced directly (https://www.ird.govt.nz/income-tax/income-tax-for-businesses-and-organisations/income-tax-for-companies/look-through-companies/acc-levies-for-a-look-through-company).
2. Take liable earnings from the individual income tax return (IR3), because ACC gets its income details from Inland Revenue and CoverPlus invoices usually use the year before (https://www.business.govt.nz/tax-and-money/guide-to-business-tax/acc-levies).
3. Apply the Earners' levy rate and maximum for the right levy year, read from the right row of Inland Revenue's table (https://www.ird.govt.nz/income-tax/income-tax-for-individuals/acc-clients-and-carers/acc-earners-levy-rates). Do not add GST.
4. Read the CU, the Work levy rate, the Working Safer rate and any discount or loading from the client's ACC invoice or ACC's levy guidebook. The Gazette average (https://gazette.govt.nz/notice/id/2025-au1361) is context only.
5. Check timing and payment: CoverPlus after the return (usually September), CoverPlus Extra in April, employers usually July; pay by the invoice due date (https://www.business.govt.nz/tax-and-money/guide-to-business-tax/acc-levies).
6. For an employer, confirm payroll deducts the Earners' levy only from payments IR335 lists and only up to the per-pay maximum (https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir335/ir335.pdf).

## Ask the client first

- Are you an employee, a sole trader, a contractor paid schedular payments, a look-through company owner (active or passive), or an employer?
- Can you send your latest ACC invoice? It shows your classification unit, Work levy rate and Working Safer levy.
- Are you on CoverPlus or CoverPlus Extra, and at what agreed level of cover?
- Which income tax return has been filed most recently, and what were the net self-employment earnings in it?
- Has your main business activity (your BIC code) changed since you registered?
- Are you GST-registered?

## When to refuse or refer

- Claims, rehabilitation or weekly compensation disputes: refer to ACC (R-NZ-ACC-1).
- Disputed levy or CU classification, or a request to reassess: refer to ACC and a New Zealand chartered accountant (R-NZ-ACC-2).
- Several entities or activities in different CUs: refer (R-NZ-ACC-3).
- A request for a specific industry's Work levy rate without the ACC invoice: refuse to state a rate and point to ACC's levy guidebook or the invoice.
- Whether GST on an ACC invoice may be claimed as input tax: refer until confirmed (see the `new-zealand-gst` Guide for GST generally).
- Income tax on the business itself: see `nz-income-tax-ir3` and `nz-provisional-tax`.

## Sources

- Inland Revenue, ACC earners' levy rates: https://www.ird.govt.nz/income-tax/income-tax-for-individuals/acc-clients-and-carers/acc-earners-levy-rates
- Inland Revenue, Employer's guide IR335: https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir335/ir335.pdf
- Inland Revenue, ACC levies for a look-through company: https://www.ird.govt.nz/income-tax/income-tax-for-businesses-and-organisations/income-tax-for-companies/look-through-companies/acc-levies-for-a-look-through-company
- Inland Revenue, ACC carers: https://www.ird.govt.nz/income-tax/income-tax-for-individuals/acc-clients-and-carers/acc-carers
- New Zealand Gazette, ACC levy consultation report for businesses: https://gazette.govt.nz/notice/id/2025-au1361
- business.govt.nz, ACC levies: https://www.business.govt.nz/tax-and-money/guide-to-business-tax/acc-levies

### Disclaimer

This Guide and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this Guide. All outputs must be reviewed and signed off by a qualified professional (such as a New Zealand Chartered Accountant or equivalent licensed practitioner) before filing or acting upon.

> Contributed by OpenAccountants.

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
