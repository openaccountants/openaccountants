---
name: ns-tax-credits
description: Use this skill for Nova Scotia provincial tax credits — NS Low-Income Tax Reduction, Affordable Living Tax Credit, Age Amount Supplement, Volunteer Firefighters and Search/Rescue Tax Credit, NS Digital Media Tax Credit (refundable corporate, 25-30%), Capital Investment Tax Credit (15%), Film Industry Tax Credit. Triggers "Nova Scotia tax credits", "NS Affordable Living", "Form NS428", "NS digital media credit", "Form NSDMTC".
jurisdiction: CA
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# NS Tax Credits

## Nova Scotia — Provincial Tax Credits — Skill v1.0

This skill covers Nova Scotia's suite of provincial tax credits available to individuals and corporations in tax year 2025. NS has unusual indexation behaviour — many provincial amounts have been frozen since the early 2000s and were only partially un-frozen by Bill 37 (2024) for select brackets and the basic personal amount. Always check the Department of Finance Nova Scotia bulletins for the operative figures before signing off.

The skill is structured around the personal credits flowing through Form NS428 and the corporate credits administered via separate certification programs (NSDMTC, NSCITC, Film) that produce refundable or non-refundable amounts reported on the T2 corporate return with a Nova Scotia schedule.

## 1. Quick reference — personal and corporate credit summary

**Quick reference summary heading (no direct body, subsections follow)**

### Personal credits (Form NS428 / NS-BEN)

**Personal credits table**  _(NS ITA s. 10, 11, 13, 49, 37A, 37C, 40, 47)_

| Credit | Type | 2025 amount (approx.) | Authority |
| --- | --- | --- | --- |
| Basic personal amount (NS) | Non-refundable | $8,744 (low-income enhanced up to $11,481) | NS ITA s. 10 |
| Spouse / common-law partner | Non-refundable | $8,481 base | NS ITA s. 11 |
| Age amount (65+) | Non-refundable | $4,141 federal + **$1,465 NS supplement** | NS ITA s. 13 |
| Affordable Living Tax Credit (ALTC) | **Refundable** | $255 single + $60 per child (quarterly) | NS ITA s. 49 |
| Low-Income Tax Reduction (LITR) | Non-refundable | Up to $300 (single) / $600 (family) + $165 per child | NS ITA s. 37A |
| Volunteer Firefighter / Search & Rescue | Non-refundable | $500 ($72.50 max tax savings at 8.79%) | NS ITA s. 37C |
| Healthy Living | **Repealed** (do not claim post-2014) | n/a | n/a |
| Sport and recreation expenses for children | **Repealed** | n/a | n/a |
| Equity Tax Credit | Non-refundable | 35% of eligible investment | NS ITA s. 40 |
| Innovation Equity Tax Credit (IETC) | Non-refundable | 35% (45% in oceans tech / life sciences) | NS ITA s. 47 |

### Corporate credits

**Corporate credits table**  _(Corporate credits summary table)_

| Credit | Type | Rate | Notes |
| --- | --- | --- | --- |
| **NS Digital Media Tax Credit (NSDMTC)** | Refundable | **25%** eligible labour + **5%** geographic bonus (outside Halifax Regional Municipality) = up to **30%** | Certification by NS Dept. of Communities, Culture, Tourism and Heritage. Filed with T2 + Form NSDMTC. |
| **NS Capital Investment Tax Credit (NSCITC)** | Non-refundable | **15%** of capital cost of qualifying property | Manufacturing/processing/farming/fishing/logging in NS. Annual cap $30M cost ($4.5M credit). 20-year carryforward, 3-year carryback. |
| **NS Film Industry Tax Credit** | Refundable | **50%** eligible labour for Atlantic Canada residents (with Halifax bonus structure varying) / **25%** non-Atlantic spend | Issued via Film and Creative Industries Nova Scotia certification. |
| **Scientific Research & Experimental Development (NS SR&ED)** | Refundable (CCPC) | **15%** of qualifying SR&ED expenditures | Stacks with federal 35% / 15% SR&ED credit. |

## 2. Required inputs and refusal catalogue

### Required inputs (personal)

- **Required personal inputs** — Tax year 2025 Nova Scotia residency confirmation as at December 31, 2025; T1 General with line 23600 net income, line 26000 taxable income; Adjusted family net income (line 23600 + spouse's line 23600 minus certain UCCB / RDSP amounts); Number of children under 19 in the household at December 31; Marital status at December 31, 2025; For LITR / ALTC: dependent children eligibility for Canada Child Benefit; For Volunteer Firefighter credit: certification letter from the fire chief / search and rescue authority confirming ≥ 200 hours; For Age Amount Supplement: date of birth (must be 65 or older on December 31, 2025)  _(NS ITA)_

### Required inputs (corporate)

- **Required corporate inputs** — For NSDMTC: certificate of registration + certificate of completion from Nova Scotia Department of Communities, Culture, Tourism and Heritage; eligible labour schedule; geographic apportionment between Halifax Regional Municipality and outside-HRM. For NSCITC: capital cost of qualifying property, in-service date, prescribed use confirmation (manufacturing/processing/farming/fishing/logging), evidence property was new. For Film Tax Credit: Film and Creative Industries Nova Scotia certificate, Atlantic Canada residency declarations for cast/crew, Halifax vs. outside-Halifax spend allocation. T2 corporate return with Schedule 5 (provincial credits) and the relevant NS schedules.  _(NS ITA)_

### Refusal catalogue

**Refusal catalogue table**

| Code | Refusal trigger |
| --- | --- |
| R-NS-CR-1 | Part-year residents — Form NS428 has special proration that this skill v1.0 does not handle. Escalate. |
| R-NS-CR-2 | Deceased taxpayer final return — survivor benefit / ALTC entitlement rules out of scope. |
| R-NS-CR-3 | NSDMTC where the corporation is not a "taxable Canadian corporation" or lacks a permanent establishment in NS — defer to specialist. |
| R-NS-CR-4 | NSCITC where the property is used outside NS for any part of the year — apportionment rules out of scope. |
| R-NS-CR-5 | Film Tax Credit on co-productions involving non-Canadian treaty co-producers — escalate. |
| R-NS-CR-6 | Equity Tax Credit / Innovation Equity Tax Credit recapture events (early disposition within 4 years) — escalate. |
| R-NS-CR-7 | Claims for credits that have been repealed (Healthy Living, Sport & Recreation, Volunteer Emergency First Aid) — refuse and educate the client. |
| R-NS-CR-8 | Anything involving the now-repealed Food Bank Tax Credit for Farmers transitional rules — refuse. |
| R-NS-CR-9 | NSDMTC where the product is "interactive digital media" but consists primarily of news, current affairs, weather, sports reporting, or advertising — these are excluded. |
| R-NS-CR-10 | Stacking analysis where the federal credit is at issue (e.g. SR&ED interaction with NSDMTC labour) — refer to a federal SR&ED specialist before signing. |

- **R-NS-CR-1** — Part-year residents — Form NS428 has special proration that this skill v1.0 does not handle. Escalate.
- **R-NS-CR-2** — Deceased taxpayer final return — survivor benefit / ALTC entitlement rules out of scope.
- **R-NS-CR-3** — NSDMTC where the corporation is not a "taxable Canadian corporation" or lacks a permanent establishment in NS — defer to specialist.
- **R-NS-CR-4** — NSCITC where the property is used outside NS for any part of the year — apportionment rules out of scope.
- **R-NS-CR-5** — Film Tax Credit on co-productions involving non-Canadian treaty co-producers — escalate.
- **R-NS-CR-6** — Equity Tax Credit / Innovation Equity Tax Credit recapture events (early disposition within 4 years) — escalate.
- **R-NS-CR-7** — Claims for credits that have been repealed (Healthy Living, Sport & Recreation, Volunteer Emergency First Aid) — refuse and educate the client.
- **R-NS-CR-8** — Anything involving the now-repealed Food Bank Tax Credit for Farmers transitional rules — refuse.
- **R-NS-CR-9** — NSDMTC where the product is "interactive digital media" but consists primarily of news, current affairs, weather, sports reporting, or advertising — these are excluded.
- **R-NS-CR-10** — Stacking analysis where the federal credit is at issue (e.g. SR&ED interaction with NSDMTC labour) — refer to a federal SR&ED specialist before signing.

## 3. NS Affordable Living Tax Credit (ALTC)

### Statutory authority

- **ALTC statutory authority** — Nova Scotia Income Tax Act s. 49; administered by CRA on behalf of NS under the tax collection agreement. Paid quarterly with the federal GST/HST credit cycle (July, October, January, April).  _(NS ITA s. 49)_

### 2025 amounts (per benefit year July 2025 – June 2026, based on 2024 net income)

- **ALTC base amount** — $255 per family unit per year ($63.75 per quarterly payment)  _(NS ITA s. 49)_
- **ALTC child supplement** — $60 per dependent child under 19 per year ($15 per quarter)  _(NS ITA s. 49)_
- **ALTC phase-out threshold** — $30,000 adjusted family net income  _(NS ITA s. 49)_
- **ALTC phase-out rate** — 5% of family net income above $30,000  _(NS ITA s. 49)_

Confirm 2025 indexation — the ALTC base has been $255 since 2012; the 2024 NS budget announced an indexation review effective 2026 onwards, so the **operating assumption for 2025 is $255 unchanged**. Verify against the Nova Scotia Department of Finance Tax Measures bulletin for fiscal 2025-26 before signing.

### Eligibility

- **ALTC eligibility** — Resident of NS at the beginning of the payment month; 19 or older, OR married/common-law, OR a parent living with a child; Filed a 2024 T1 return (the ALTC is auto-calculated by CRA from the T1 — no separate form); Family net income below approximately $35,100 (single, no kids) or higher with children  _(NS ITA s. 49)_

### Worked snippet (single parent, 2 children, $25,000 family net income)

Base: $255
Children: $60 × 2 = $120
Total entitlement: $375
Phase-out: none (income < $30,000)
Quarterly payment: $93.75

### Worked snippet (couple, 1 child, $40,000 family net income)

Base + supplement: $255 + $60 = $315
Phase-out: ($40,000 − $30,000) × 5% = $500
Reduced credit: max($315 − $500, $0) = **$0**
This family is **above the ALTC ceiling** — no entitlement.

## 4. NS Low-Income Tax Reduction (LITR)

### Statutory authority

- **LITR statutory authority** — NS Income Tax Act s. 37A. Non-refundable; reduces NS provincial tax payable to zero before being clawed back. Calculated on Form NS428 Step 3.  _(NS ITA s. 37A)_

### 2025 amounts (frozen since 2010; verify against current NS428 form)

- **LITR single individual maximum** — $300 maximum  _(NS ITA s. 37A)_
- **LITR married/common-law maximum** — $300 + $300 spousal = $600 maximum per couple  _(NS ITA s. 37A)_
- **LITR per dependent child under 19** — $165  _(NS ITA s. 37A)_
- **LITR phase-out threshold (single)** — $15,000 net income  _(NS ITA s. 37A)_
- **LITR phase-out threshold (family)** — $18,000 family net income  _(NS ITA s. 37A)_
- **LITR phase-out rate** — 5% of net income above the threshold  _(NS ITA s. 37A)_

### Mechanics on Form NS428

- **LITR computation mechanics** — 1. Compute NS tax payable (Step 2 of NS428) at the four-bracket NS rate schedule. 2. Apply non-refundable credits (basic personal, spouse, age, CPP, EI, etc.) at 8.79%. 3. Compute LITR on Form NS428 Step 3: - Sum: $300 + $300 (if spouse) + $165 × children - Less: 5% × (net income − threshold) - LITR equals this amount, capped at NS tax otherwise payable. 4. Subtract LITR from NS tax payable. LITR **cannot reduce NS tax below zero**. The Affordable Living Tax Credit (Section 3) is the refundable companion that pays out when the taxpayer has no NS tax liability.  _(NS ITA s. 37A)_

### Worked snippet (single, no kids, $18,000 net income)

LITR notional: $300
Phase-out: ($18,000 − $15,000) × 5% = $150
LITR claimable: $300 − $150 = **$150**
This $150 offsets NS tax otherwise payable on the slice of income above the NS basic personal amount.

## 5. NS Age Amount Supplement

### Statutory authority

- **Age Amount Supplement statutory authority** — NS Income Tax Act s. 13. **In addition to** the federal age amount on line 30100 of the T1 and the NS age amount on Form NS428.  _(NS ITA s. 13)_

### 2025 amounts

- **Federal age amount (line 30100)** — $9,028 (for context — not claimed on NS428)  _(NS ITA s. 13)_
- **NS age amount on NS428** — $4,141 (frozen)  _(NS ITA s. 13)_
- **NS Age Amount Supplement** — additional $1,465 added to the NS age amount where the senior's income is at or below the NS LITR phase-out range (low-income test)  _(NS ITA s. 13)_

### Eligibility

- **Age Amount Supplement eligibility** — 65 or older on December 31, 2025; Net income at or below the NS Age Amount Supplement income threshold (approximately $24,000; confirm against CRA NS428 instructions for 2025 — the threshold tracks the federal age amount phase-out start adjusted to NS); Supplement is **fully clawed back** at higher incomes via the standard 15% reduction once net income exceeds the threshold  _(NS ITA s. 13)_

### Mechanics

- **Age Amount Supplement mechanics** — The supplement is built into the NS age amount line on Form NS428 — there is no separate line. The taxpayer enters their full age amount including the supplement; CRA's NETFILE calculator applies the income test automatically. Reviewers should verify the calculation manually for low-income seniors because tax software occasionally omits the supplement.  _(NS ITA s. 13)_

### Conservative default

If the client is 65+ and net income is below $25,000, **always check** whether the supplement has been applied. If software omits it, file a T1-ADJ with the corrected NS428.

## 6. NS Volunteer Firefighter and Search & Rescue Tax Credit

### Statutory authority

- **Volunteer Firefighter credit statutory authority** — NS Income Tax Act s. 37C. Non-refundable; introduced 2007.  _(NS ITA s. 37C)_

### 2025 amount

- **Volunteer Firefighter credit base amount and rate** — $500 credit base amount; Applied at NS lowest bracket rate of 8.79% → maximum tax saving of $43.95. (Note: the federal Volunteer Firefighters Amount on line 31220 is separately $6,000 base × 15% = $900 federal saving; the NS credit is a standalone provincial benefit, not stacked at the federal rate.)  _(NS ITA s. 37C)_

### Eligibility

- **Volunteer Firefighter credit eligibility** — Performed at least 200 hours of eligible volunteer service in the year as a volunteer firefighter or volunteer search and rescue volunteer; Service certified in writing by the fire chief or by an authorized representative of the search and rescue organization; Cannot have received more than $1,000 in honoraria for the same service (the credit is intended for unpaid or nominally-paid volunteers; honoraria above $1,000 disqualify under the federal rule and NS follows); Reported on Form NS428 line 5829 (verify line number against current-year form)  _(NS ITA s. 37C)_

### Documentation to retain

- **Documentation to retain for Volunteer Firefighter credit** — Certification letter from the chief / authority, naming the volunteer, the organization, total hours, and the year; Confirmation that combined hours of firefighter and search-and-rescue service total ≥ 200 (the two activities can be aggregated under the federal/provincial rules but the volunteer can claim only one of the two federal credits, and similarly only one NS credit — they are not stackable across the two roles)  _(NS ITA s. 37C)_

## 7. NS Digital Media Tax Credit (NSDMTC)

### Statutory authority

- **NSDMTC statutory authority** — NS Income Tax Act s. 47A and 47B; Digital Media Tax Credit Regulations under the NS ITA. Administered jointly by the NS Department of Finance and Treasury Board (tax administration) and the Department of Communities, Culture, Tourism and Heritage (certification).  _(NS ITA s. 47A, 47B)_

### Rate (2025)

- **NSDMTC base rate** — 25% of eligible Nova Scotia labour expenditures  _(NS ITA s. 47A, 47B)_
- **NSDMTC geographic bonus** — additional 5% for labour incurred outside the Halifax Regional Municipality (HRM)  _(NS ITA s. 47A, 47B)_
- **NSDMTC maximum effective rate** — 30% for fully outside-HRM productions  _(NS ITA s. 47A, 47B)_
- **NSDMTC alternative computation cap** — 50% of eligible labour OR 25% of total eligible expenditure, whichever is less (this cap operates as a labour-intensity floor — productions that are not predominantly labour-driven default to the 25% of total cost limit)  _(NS ITA s. 47A, 47B)_

### Refundability

- **NSDMTC refundability** — Fully refundable — paid out by CRA to the corporation after assessment of the T2, regardless of whether NS corporate tax is otherwise payable.  _(NS ITA s. 47A, 47B)_

### Eligibility — corporation

- **NSDMTC corporate eligibility** — Taxable Canadian corporation; Permanent establishment in Nova Scotia; Primary business: development of interactive digital media products; Not controlled directly or indirectly by tax-exempt persons or non-residents (subject to specific safe harbours)  _(NS ITA s. 47A, 47B)_

### Eligibility — product

- **Eligible interactive digital media product** — An eligible interactive digital media product is a product that: 1. Is intended to educate, inform, or entertain; 2. Achieves its purpose by presenting information in at least two of: text, sound, images; 3. Is interactive (the user can choose paths, modify content, or otherwise affect the presentation); 4. Is developed for commercial exploitation  _(Digital Media Tax Credit Regulations, NS Reg. under the NS Income Tax Act)_

### Exclusions

- **NSDMTC exclusions** — News, current events, public affairs, weather, market reporting, sports; Advertising and promotional products; Operating systems; Adult content; Products produced for in-house use only by the corporation; Products that are predominantly databases or reference works without interactive narrative  _(Digital Media Tax Credit Regulations, NS Reg. under the NS Income Tax Act)_

### Eligible labour expenditures

- **NSDMTC eligible labour expenditures** — Salaries and wages paid to NS-resident employees for work performed in NS on the eligible product, during the development period; Amounts paid to NS-resident contractors for personal services; Pro-rated where the employee works on both eligible and ineligible products; Excludes: bonuses paid out of profits, stock-based compensation, related-party amounts exceeding fair market value, signing bonuses unconnected to development work  _(Digital Media Tax Credit Regulations, NS Reg. under the NS Income Tax Act)_

### Certification process

- **NSDMTC certification process** — 1. Registration Certificate: filed with NS Department of Communities, Culture, Tourism and Heritage before development begins (or within early development phase). Confirms product eligibility in principle. 2. Completion Certificate: filed within 30 months of the corporation's year-end in which development was completed. Confirms actual eligible spend. 3. T2 filing: file Form NSDMTC along with the corporate T2 return for each taxation year of the development period. The credit is claimed per year, not only at completion.  _(NSDMTC certification guidelines, NS Department of Communities, Culture, Tourism and Heritage)_

### Worked snippet (Halifax studio, $1M total spend, $700k NS labour, all in HRM)

Eligible NS labour: $700,000
25% labour rate: $175,000
Geographic bonus: $0 (all in HRM)
Cap test 1 (50% of labour): $350,000 — not binding
Cap test 2 (25% of total eligible spend): $250,000 — not binding (credit $175k < $250k cap)
**NSDMTC**: **$175,000 refundable**

### Worked snippet (Sydney studio, $500k spend, $400k NS labour, all outside HRM)

Eligible NS labour: $400,000
25% labour: $100,000
5% geographic bonus: $20,000
Subtotal: $120,000
Cap test 1 (50% of labour): $200,000 — not binding
Cap test 2 (25% of total spend): $125,000 — not binding
**NSDMTC**: **$120,000 refundable**

### Sunset clause

The NSDMTC has been renewed in successive provincial budgets. As of the 2024 NS Budget the credit was extended through December 31, 2025. Verify the post-2025 status against the most recent provincial budget bulletin before quoting the credit to clients planning new productions — re-extension is likely but not automatic.

## 8. NS Capital Investment Tax Credit (NSCITC)

### Statutory authority

- **NSCITC statutory authority** — NS Income Tax Act s. 47C. Administered by the Department of Finance and Treasury Board with NETFILE T2 processing through CRA.  _(NS ITA s. 47C)_

### Rate

- **NSCITC rate and cap** — 15% of the capital cost of qualifying property acquired and made available for use in Nova Scotia; Annual capital cost cap per associated group: $100 million of qualifying property (so maximum annual credit = $15M before the lifetime cap; older guidance referenced a $30M annual cost cap — confirm current cap with NS Department of Finance for 2025)  _(NS ITA s. 47C)_

### Refundability

- **NSCITC refundability** — Non-refundable. Reduces NS Part I tax otherwise payable. Unused amounts: Carryback: 3 years (cannot carry back to a year prior to the credit's enactment); Carryforward: 20 years  _(NS ITA s. 47C)_

### Qualifying property

- **NSCITC qualifying property definition** — Property is qualifying property if it: 1. Was acquired after the enactment date (current program: post-2014 acquisitions); 2. Is prescribed property — i.e. Class 8, 29, 43, 53 capital cost allowance classes used primarily in qualifying activity in NS; 3. Used primarily in NS for one of: Manufacturing or processing of goods for sale or lease, Farming, Fishing, Logging; 4. Was new when acquired (used property does not qualify, with limited exceptions for refurbishment programs); 5. Was acquired from an arm's-length supplier (or at fair market value if non-arm's-length)  _(Capital Investment Tax Credit Regulations, NS Reg. under the NS Income Tax Act)_

### Exclusions

- **NSCITC exclusions** — Property used primarily for non-qualifying activity (administrative offices, retail, distribution to consumers); Property eligible for the Atlantic Investment Tax Credit at the federal level may still qualify for NSCITC (the two credits can stack, subject to the general anti-avoidance rules) — but verify each property's classification; Property leased to a person not engaged in qualifying activity in NS  _(Capital Investment Tax Credit Regulations, NS Reg. under the NS Income Tax Act)_

### Mechanics

- **NSCITC computation mechanics** — 1. Compute capital cost of qualifying property acquired in the year (net of GIA / government assistance other than NSCITC itself). 2. Apply 15% rate. 3. Reduce by any associated-corporation allocation under the $100M annual cap. 4. Claim on T2 Schedule 5 (provincial and territorial credits) with the NSCITC schedule. 5. Track unused balance on the corporation's continuity schedule for the 20-year carryforward.  _(NS ITA s. 47C)_

### Worked snippet (Lunenburg seafood processor, $2M new processing line)

Capital cost of qualifying property: $2,000,000
NSCITC at 15%: $300,000
Carryback potentially available against NS Part I tax in the three prior years
Remaining balance carried forward up to 20 years if unused

## 9. NS Film Industry Tax Credit

### Status note

- **Film Industry Tax Credit status note** — The original NS Film Industry Tax Credit was discontinued effective July 1, 2015 and replaced by the Nova Scotia Film and Television Production Incentive Fund — which is a direct grant program, not a tax credit. A separate Nova Scotia Film Industry Tax Credit Refund mechanism remains for productions that had already commenced under the pre-2015 regime, with limited transitional rules.

### Current film-related tax measures in NS (2025)

**Current film-related tax measures table**

| Program | Type | Rate / structure |
| --- | --- | --- |
| Film and Television Production Incentive Fund | **Direct grant** (not tax credit) | Up to 25% of all eligible expenditure + Nova Scotia content/regional bonuses |
| Co-Production Incentive | Direct grant | Similar structure, applied to certified treaty co-productions |
| **NSDMTC** (Section 7 above) | Refundable tax credit | 25-30% labour — applies to interactive digital media, **not** linear film/TV |

### Practitioner note

If a client asks about the "Nova Scotia Film Tax Credit", clarify whether they mean:
- The legacy 50% / 25% labour-based tax credit (now closed to new productions) — refuse and escalate; or
- The current Film and Television Production Incentive Fund — refer to Film and Creative Industries Nova Scotia. This is a grant treated as government assistance on the corporate income tax return (reduces eligible cost / increases income), not a credit claimed on the T2.

If asked to compute, refuse under R-NS-CR-5 / R-NS-CR-7 and refer to a film-specialist accountant.

## 10. Form NS428 and the NS-BEN combined benefit form

### Form NS428 — Nova Scotia Tax and Credits

- **Form NS428 structure** — Form NS428 is the provincial schedule to the T1 General. Three steps: - Step 1 — NS tax on taxable income: applies the 2025 NS tax brackets to line 26000. - Step 2 — Non-refundable provincial credits: enters NS basic personal amount, spousal amount, age amount (with supplement where applicable), CPP/QPP, EI, NS volunteer firefighter, NS adoption expense, NS medical, NS donations, etc. Sum is multiplied by 8.79% (the lowest NS bracket rate). - Step 3 — Low-Income Tax Reduction: applies the LITR (Section 4) to reduce Step 2 NS tax to zero where applicable.

### Form NS-BEN — Application for Nova Scotia Affordable Living Tax Credit and Poverty Reduction Credit

- **Form NS-BEN details** — ALTC (Section 3) is auto-computed from the T1; no separate application required for residents who filed a T1. Poverty Reduction Credit (PRC): separate from ALTC; targeted at income assistance recipients; outside scope of this skill — escalate if claimed. NS-BEN is used principally by new residents who did not file a prior-year NS T1 to register for the ALTC payment stream. File NS-BEN at the same time as the first NS T1.

## 11. Worked example — Halifax family, $60,000 income, 1 volunteer firefighter parent, 2 children

### Facts

Halifax resident family, both parents age 42
Parent A: employment income $40,000, volunteer firefighter (220 hours certified)
Parent B: employment income $20,000
Two children, ages 8 and 11
Family net income: $60,000
Each parent files Form NS428

### Step 1: ALTC (refundable, family-level)

Base $255 + 2 × $60 = $375
Phase-out: ($60,000 − $30,000) × 5% = $1,500
Reduced credit: max($375 − $1,500, 0) = **$0**
ALTC entitlement: nil at this income level.

### Step 2: LITR (non-refundable, Parent A)

Threshold (family, $18,000): exceeded
Phase-out: ($60,000 − $18,000) × 5% = $2,100
LITR notional: $300 + $300 + 2 × $165 = $930
Reduced LITR: max($930 − $2,100, 0) = **$0**
LITR: nil. (Note: in NS the LITR phase-out is calculated on family net income for couples, then allocated between the two NS428 forms — but at $60k family income the reduction zeroes the entire credit before allocation.)

### Step 3: Volunteer Firefighter credit (Parent A only)

$500 × 8.79% = **$43.95**
Claimed on Parent A's NS428.

### Step 4: NS tax on Parent A's $40,000 taxable income

Bracket 1 (up to $29,590): $29,590 × 8.79% = $2,601.96
Bracket 2 ($29,590 to $59,180): ($40,000 − $29,590) × 14.95% = $1,556.30
Subtotal: $4,158.26
Less basic personal credit: $8,744 × 8.79% = $768.60
Less CPP/EI credits (approx): say $400
Less volunteer firefighter: $43.95
**Parent A NS tax**: approximately $2,946

### Step 5: NS tax on Parent B's $20,000

Bracket 1: $20,000 × 8.79% = $1,758
Less basic personal: $768.60
Less CPP/EI credits: say $200
**Parent B NS tax**: approximately $789

### Step 6: Combined household NS provincial outcome

Total NS tax: ~$3,735
ALTC refund: $0
LITR offset: $0
Volunteer firefighter saving: $43.95 (already absorbed into Parent A's NS tax computation)
Net NS tax paid: **~$3,735**

This household is above all the low-income relief thresholds and benefits only from the volunteer firefighter credit on the NS side. The bulk of household benefit comes through the federal Canada Child Benefit and the federal Volunteer Firefighters Amount (line 31220, $6,000 × 15% = $900), neither of which is computed in this skill.

## 12. Conservative defaults

- **Indexation**: if you cannot confirm whether a 2024 figure has been re-indexed for 2025, use the 2024 figure and flag the uncertainty in the reviewer brief. NS has a long history of frozen credit amounts (LITR amounts unchanged since 2010, ALTC base unchanged since 2012, NS age amount unchanged since 2010). Do not assume CPI indexation.
- **NSDMTC certification status**: never claim the credit on a T2 until the Registration Certificate has been issued. Filing a T2 with the credit before certification is a deficient return and will be reassessed.
- **NSCITC carryforward**: maintain a continuity schedule for every corporate client with NSCITC. The 20-year carryforward is generous but easily lost during reorganizations (acquisition of control limits under federal s. 111(4) apply to NSCITC via NS s. 47C(7) — escalate any AOC event).
- **LITR allocation between spouses**: NS allows either spouse to claim the LITR, but only one spouse may claim it. Verify the higher-tax-payable spouse claims the full amount.
- **Volunteer firefighter hours**: 199 hours = zero credit. There is no partial credit. If the certification letter shows 199 hours, refuse the credit and document the refusal.
- **Repealed credits**: if prior-year filings claimed the Healthy Living or Sport and Recreation credit, do not repeat the claim; flag the prior-year filing for potential T1-ADJ if within three years.
- **Provincial vs. federal stacking**: NSDMTC and federal SR&ED on the same labour cost — the federal SR&ED treats NSDMTC as government assistance, reducing federal qualifying expenditure. Always model both credits together before recommending which to maximize.
- **Reviewer sign-off**: this skill produces a working draft only. A Canadian-licensed practitioner (CPA Canada / CPA Nova Scotia member, or a licensed tax preparer registered with CRA EFILE) must review and sign every output.

## 13. Sources

- **Nova Scotia Income Tax Act**, RSNS 1989, c. 217, as amended — primary authority for all NS personal and corporate credits. Sections cited: s. 10 (basic personal), s. 11 (spousal), s. 13 (age amount and supplement), s. 37A (LITR), s. 37C (volunteer firefighter / S&R), s. 40 (Equity Tax Credit), s. 47 (Innovation Equity Tax Credit), s. 47A–B (NSDMTC), s. 47C (NSCITC), s. 49 (Affordable Living Tax Credit).
- **Digital Media Tax Credit Regulations**, NS Reg. under the NS Income Tax Act — definitions of eligible product, eligible labour, certification process.
- **Capital Investment Tax Credit Regulations**, NS Reg. under the NS Income Tax Act — definitions of qualifying property, prescribed activity.
- **Nova Scotia Department of Finance and Treasury Board** — annual Tax Measures bulletins, especially the 2024-25 and 2025-26 Budget bulletins for current-year amount confirmations and indexation status.
- **Nova Scotia Department of Communities, Culture, Tourism and Heritage** — NSDMTC certification guidelines, eligible product determination guidance.
- **Film and Creative Industries Nova Scotia** — Film and Television Production Incentive Fund (grant program, not a tax credit).
- **Canada Revenue Agency** — Form NS428 (Nova Scotia Tax and Credits), Form NS-BEN (NS Affordable Living and Poverty Reduction Credits application), Form T2 Schedule 5 (provincial credits including NSDMTC and NSCITC line entries), and Provincial Income Tax Folio for Nova Scotia.
- **Federal Income Tax Act** — incorporated by reference into NS ITA for most computational provisions; relevant sections include 110.1 (donations), 118 (personal credits), 118.06 (federal volunteer firefighter), 127.41 (provincial credits as government assistance).

## Skill footer disclaimer

Skill v1.0 — pending verification by Nova Scotia-licensed reviewer. Tax year 2025. All amounts subject to confirmation against the 2025-26 NS Budget Tax Measures bulletin before client-facing use.

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
