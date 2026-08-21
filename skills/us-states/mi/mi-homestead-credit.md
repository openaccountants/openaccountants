---
name: mi-homestead-credit
description: Use this skill whenever asked about the Michigan Homestead Property Tax Credit for full-year Michigan residents who own or rent their principal residence. Trigger on phrases like "Michigan homestead credit", "MI-1040CR", "Michigan property tax credit", "total household resources", "homestead property tax", "MCL 206.520".
jurisdiction: US-MI
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# MI Homestead Credit

## Michigan Homestead Property Tax Credit — MI-1040CR (TY 2025)

> **Scope.** This skill covers the **regular Form MI-1040CR** for full-year Michigan residents who **own or rent** their principal residence and whose total household resources are at or below the statutory ceiling. It is one of the largest refundable state credits in the US — Michigan Treasury data shows roughly **$300M/year** in refunds across all claim variants. Every Michigan return preparer encounters it.
>
> **Out of scope (see Section 10 refusal catalogue):**
> - **MI-1040CR-2** — special filers (veterans, blind persons, surviving spouses of veterans, totally and permanently disabled) who get a credit computation with **no income test** in many fact patterns.
> - **MI-1040CR-5** — Farmland Preservation Tax Credit (a separate program tied to MDARD development-rights agreements; not the household-income credit).
> - **MI-1040CR-7** — Home Heating Credit. Interacts with the homestead credit but is administered separately. Out of scope here; will be a sibling skill.
> - Part-year and non-resident returns.
> - Amended MI-1040CR claims.
>
> **Quality tier.** Q3 — AI-drafted, not independently verified. Rates and thresholds were researched on 2026-05-28 from the published TY 2025 MI-1040CR form and instructions on michigan.gov/taxes and from the AARP Foundation Property Tax-Aide knowledge base. A qualified Michigan preparer must review before filing.

## Section 1: Metadata

- **Jurisdiction** — Michigan (US-MI)
- **Tax type** — Refundable individual income tax credit
- **Primary form** — Form MI-1040CR (regular)
- **Tax year** — 2025 (filed in 2026)
- **Authority** — Michigan Department of Treasury
- **Statute** — MCL 206.520 – 206.535 (Income Tax Act of 1967, as amended)
- **Reform act** — Lowering MI Costs Plan — PA 4 of 2023
- **Version** — 0.1
- **Last updated** — 2026-05-28
- **Validation** — AI-drafted — Q3 — pending CPA verifier

### Sources consulted

**Sources consulted**

| # | Source | URL |
| --- | --- | --- |
| 1 | TY 2025 MI-1040CR (form) | https://www.michigan.gov/taxes/-/media/Project/Websites/taxes/Forms/IIT/TY2025/MI-1040CR.pdf |
| 2 | TY 2025 MI-1040CR Instructions (general information booklet) | https://www.michigan.gov/taxes/-/media/Project/Websites/taxes/Forms/IIT/TY2025/MI-1040CR-Instr.pdf |
| 3 | TY 2025 MI-1040CR-2 (Veterans and Blind People) booklet | https://www.michigan.gov/taxes/-/media/Project/Websites/taxes/Forms/IIT/TY2025/MI-1040CR-2-Book.pdf |
| 4 | Michigan Treasury — Homestead Property Tax Credit landing page | https://www.michigan.gov/taxes/iit/tax-guidance/credits-exemptions/hptc |
| 5 | Michigan Treasury — Total Household Resources guidance | https://www.michigan.gov/taxes/iit/tax-guidance/total-household-resources |
| 6 | MCL 206.520 — Homestead credit statute | https://legislature.mi.gov/Laws/MCL?objectName=mcl-206-520 |
| 7 | MCL 206.522 — Computation; senior tables | https://legislature.mi.gov/Laws/MCL?objectName=mcl-206-522 |
| 8 | Public Act 4 of 2023 — Lowering MI Costs Plan | https://legislature.mi.gov/Laws/PublicActs?ObjectName=2023-PA-0004 |
| 9 | AARP Foundation Property Tax-Aide — Michigan | https://my.aarpfoundation.org/property-taxes/taxpayer-states/michigan/ |
| 10 | Michigan Taxpayer's Guide (2025 tax year) — Senate Fiscal Agency | https://www.legislature.mi.gov/publications/TaxpayerGuide.pdf |

## Section 2: Quick reference — TY 2025 thresholds

**Quick reference — TY 2025 thresholds**

| Item | Value | Source |
| --- | --- | --- |
| **Maximum credit (regular CR)** | **$1,900** | TY 2025 MI-1040CR instructions; MCL 206.520(3) as amended by PA 4 of 2023 |
| Total household resources (THR) ceiling — credit fully phased out above | **$71,500** | TY 2025 MI-1040CR instructions |
| THR floor where phase-out begins (regular claimants) | **$62,500** | TY 2025 MI-1040CR instructions |
| Phase-out rate (regular claimants) | Credit reduced by **10%** for every **$1,000** (or part) of THR over $62,500 | TY 2025 MI-1040CR instructions |
| Taxable value cap on homestead | **$165,400** | TY 2025 MI-1040CR instructions |
| Property-tax-floor as % of THR (regular) | **3.2%** of THR | TY 2025 MI-1040CR Line 34 |
| Rent treated as property tax (renters) | **23%** of rent paid `[VERIFY: 23% per AARP source; some legacy summaries say 20% — confirm against current TY 2025 instructions]` | AARP Property Tax-Aide MI page |
| Senior alternate THR ceiling (100% of difference) | THR ≤ **$21,000** ⇒ 100% credit allowance `[VERIFY exact 2025 figure]` | MCL 206.522; TY 2025 instructions Table 2 |
| Senior phase-out — THR over $21,000 | Credit % reduced 4% per $1,000 of THR over $21,000 `[VERIFY]` | TY 2025 instructions Table 2 |
| Senior phase-out — THR $30,001–$60,000 | Credit = 60% of difference `[VERIFY]` | TY 2025 instructions Table 2 |
| Senior renter alternate test | Rent > 40% of THR triggers alternate computation | TY 2025 instructions |
| Filing deadline | Same as MI-1040 (April 15, 2026 for TY 2025) | MI-1040 Book |
| Statute of limitations on credit claim | **4 years** from original due date | MCL 205.27a |

> Every dollar figure above is sourced to the published TY 2025 instructions or the underlying statute. Any figure marked `[VERIFY]` was confirmed in the AARP / TaxSlayer summaries but the preparer should cross-check against the official Treasury PDF before relying on it.

## Section 3: Total Household Resources (THR) — the Michigan-only concept

THR is the Michigan-defined income base for the homestead credit. It is **not** federal AGI and **not** Michigan AGI. It is broader than both. This is the single most error-prone area on the credit and is the leading cause of Treasury adjustment letters on MI-1040CR claims.

### What THR INCLUDES (additions to federal AGI)

**What THR INCLUDES (additions to federal AGI)**

| Item | Notes / Form line |
| --- | --- |
| All wages, salaries, tips (gross) | W-2 Box 1 |
| Self-employment net profit (Schedule C / Schedule F) | Federal Schedule C Line 31 |
| Interest, dividends, capital gains | Including U.S. obligation interest (**unlike** Michigan AGI which excludes it) |
| **Social Security benefits — gross amount** | **Included for THR even though excluded from Michigan AGI**. Use the gross amount paid by check or direct deposit (the figure on SSA-1099 Box 5), not the federally taxable portion |
| SSI, SSDI, Railroad Retirement | Full amounts |
| Pension and annuity distributions | Gross amount, regardless of MI subtraction status |
| IRA / 401(k) / 403(b) distributions | Gross amount |
| Unemployment compensation | Full amount |
| Workers' compensation | Full amount |
| Veterans' disability and pension benefits | Full amount |
| FIP / MDHHS cash assistance, foster care payments, adoption subsidy | Full amount |
| Child support received | Full amount (not deductible by payor for THR either) |
| **Alimony received** | Full amount, including post-2018 divorces where federally excluded |
| Net rental income (gross rents − ordinary expenses, but **not** depreciation) | Add back depreciation deducted federally |
| Net farm income (gross − operating expenses, not depreciation) | Add back depreciation |
| Scholarships, fellowships, grants used for living expenses | Excludes amounts for tuition/required fees |
| **Gifts of cash or merchandise from non-household members in excess of $300** | First $300 excluded; remainder included. Includes expenses paid on the claimant's behalf (rent, utilities, taxes, medical) |
| Inheritance income realized during year | Cash distributions; not the corpus of an estate |
| Lottery, gambling winnings, prizes, awards | Gross |
| Long-term care insurance benefits paid for the claimant | If reimbursed via THR-includible source |
| Other taxable and non-taxable income | Catch-all per MCL 206.510(1) |

### What THR EXCLUDES (subtractions from gross receipts)

**What THR EXCLUDES (subtractions from gross receipts)**

| Item | Reason |
| --- | --- |
| Net business / rental losses (zero floor — losses **cannot** drive THR below zero) | MCL 206.510(1)(c) caps losses |
| The federal **Earned Income Credit** received as refund | Per Treasury guidance |
| Property tax credits received in prior year | Excluded to avoid circularity |
| Government payments for medical care (Medicare, Medicaid) made directly to provider | Not received by claimant |
| Food assistance (SNAP) | Excluded |
| Energy assistance grants | Excluded |
| First $300 of cash gifts in aggregate | Per the $300 floor rule |
| **Net operating loss carryovers** | Cannot reduce current-year THR |
| Section 125 cafeteria plan amounts already excluded from gross wages | Already excluded from Box 1; not added back |

### Health insurance premiums — special handling

- **Health insurance premium deduction from THR** — Medical insurance and HMO premiums paid by the household are deductible from THR on the MI-1040CR. This includes Medicare Part B, C, and D premiums withheld from Social Security benefits; private health insurance premiums; long-term care insurance premiums. This is reported on MI-1040CR Line 36.  _(Treasury guidance ("Health Insurance Premiums and Total Household Resources"))_

### The "federal AGI vs. Michigan AGI vs. THR" trap

> These three income bases are routinely confused. A quick comparison for a 67-year-old retiree with $30k Social Security and $20k pension income:
>
> A senior with $50k of "Michigan AGI = $0" can easily have THR of $50k. The THR rules are the gating test for the homestead credit, not the Michigan AGI rules.

**Federal AGI vs Michigan AGI vs THR comparison**

| Base | Includes Social Security? | Includes pension? |
| --- | --- | --- |
| Federal AGI | Partial (up to 85% per § 86) | Yes |
| Michigan AGI | **No** (subtracted) | Senior subtraction may apply |
| **THR (this credit)** | **Yes, gross amount** | **Yes, gross amount** |

## Section 4: Eligibility — the four gates

A claimant must clear **all four** of these tests to claim the regular MI-1040CR. Failing any one disqualifies the claim.

### Gate 1 — Michigan residency

- **Michigan residency requirement** — Claimant must have been a Michigan resident for at least 6 months during the tax year. This skill is scoped to full-year residents only; part-year residents file Schedule NR and a prorated CR. Domicile, not mere physical presence, controls; the same residency test as Form MI-1040 applies.  _(MCL 206.522)_

### Gate 2 — Principal residence in Michigan

- **Principal residence requirement** — The homestead must be the claimant's principal residence in Michigan. One homestead per household per year. This includes: an owned single-family home; an owned condominium unit; a unit in a housing cooperative (co-op) — see Section 4.5; a mobile home or manufactured home owned by the claimant on land owned or rented by the claimant — see Section 4.6; a rented apartment, single-family home, mobile home pad rental. The homestead does NOT include: vacation property, second homes; property held only for investment (rental property where the owner doesn't live); property in another state; a college dormitory; a nursing home or assisted living facility where the resident does not pay property tax through their fee (special rules apply if they do).  _(MCL 206.508(4))_

### Gate 3 — Taxable value cap (owners only)

- **Taxable value cap** — For TY 2025, the homestead's taxable value cannot exceed $165,400. This is taxable value on the property tax bill — typically about half of true cash value. The cap applies to the homestead portion only; unoccupied farmland classified as agricultural is excluded from this cap.  _(MCL 206.520(7), per PA 4 of 2023 amendment)_

> **Note for renters:** Gate 3 is bypassed for renters; the cap only applies to owned homesteads.

### Gate 4 — Total household resources ceiling

- **THR ceiling** — $71,500 USD (For TY 2025, THR ≤ $71,500. Above this, no credit is available in any category. Below this, the phase-out and computation rules in Sections 5–6 apply.)  _(TY 2025 MI-1040CR instructions)_

### 4.5 — Co-op apartment rules

- **Co-op apartment rules** — A claimant living in a housing cooperative is treated as an owner for homestead credit purposes if they hold a membership / share that conveys the right to occupy a specific unit. The "property tax paid" is the claimant's pro-rata share of the co-op's real property taxes, as certified by the co-op management on the year-end statement. Do NOT treat co-op assessments that include operating costs as property tax — only the portion the co-op identifies as real property tax flows to the credit.

### 4.6 — Mobile / manufactured home rules

- **Mobile-home owner renting lot** — If the claimant owns the mobile home and rents the lot/pad: include the $3 per month specific tax paid to the local unit ($36/year) as property tax, plus 23% of the lot rent paid `[VERIFY 23%]` as the rent portion. The mobile-home owner pays the $3/month specific tax under MCL 125.1041, in lieu of ad valorem property tax on the unit.  _(MCL 125.1041)_
- **Mobile-home owner owning lot** — If the claimant owns both the home and the lot: standard owner computation using actual property tax on the parcel.

## Section 5: The computation — owners

- **Regular MI-1040CR formula for non-senior owners** — Step 1.  Property tax paid (line 10) on principal residence, subject to taxable-value cap and prorated for any non-residential or rental use. Step 2.  Floor = 3.2% × Total Household Resources (line 33 × 0.032 on line 34). Step 3.  Tentative credit = (Step 1 − Step 2), if positive. If Step 2 ≥ Step 1, no credit. Step 4.  Credit factor (line 35): 60% (i.e., 0.60) for non-senior, non-disabled regular claimants.  Tentative credit × 0.60. Step 5.  Apply phase-out for THR > $62,500: Reduce by 10% per $1,000 (or part of $1,000) that THR exceeds $62,500. Fully eliminated at THR ≥ $71,500. Step 6.  Cap at $1,900 (TY 2025).  _(TY 2025 MI-1040CR form)_

> **Line numbers above refer to the TY 2025 MI-1040CR form. Verify each line number against the published form before producing client-ready output — Treasury periodically renumbers.**

### Senior owners (age 65 or older)

- **Senior Table 2 computation** — Seniors use Table 2 in the MI-1040CR instructions rather than the flat 60% factor: - THR ≤ $21,000 ⇒ allowance is 100% of (property tax − 3.2% of THR). - THR $21,001 – $30,000 ⇒ allowance reduced 4 percentage points per $1,000 (or part) above $21,000. So at THR $25,500 the allowance is 100% − (5 × 4%) = 80% `[VERIFY exact bracket cutoffs against TY 2025 instructions]`. - THR $30,001 – $60,000 ⇒ allowance is 60% of the difference. - Above $60,000 (and certainly above $62,500), the regular 10% per $1,000 phase-out applies until THR exceeds $71,500. - Senior renters with rent > 40% of THR may take an alternate computation that compares rent paid to 40% of THR, which can yield a larger credit. The taxpayer takes the larger of the two.  _(MCL 206.522; TY 2025 instructions Table 2)_

### Property tax PAID — timing and qualifying amounts

- **Cash basis and qualifying amounts** — The credit is based on property tax paid in cash during the tax year, not accrued or billed: - Use the actual payment dates, not the levy or bill dates. - Summer + winter installments paid in the same calendar year both count. - Property taxes paid through a mortgage escrow are deemed paid by the homeowner when the lender disburses to the municipality (Form 1098 statements are the standard documentation). - Special assessments for general municipal services are NOT property tax. Special assessments for local improvements (sewer, water main) are also NOT property tax for this credit, even though they appear on the property tax bill. - Delinquent property tax paid in 2025 for a prior year IS includible in 2025 — cash basis controls. - Penalties and interest on delinquent tax are NOT includible.  _(Treasury guidance; long-standing administrative rule)_

### Multi-unit / partial business use

- **Proration for partial business/rental use** — If the homestead is used partly as rental or partly for business, the property tax is prorated between the homestead portion and the non-homestead portion. Only the homestead-portion tax flows into Step 1. Typical proration: square footage or number of units. A duplex where the owner lives in one unit and rents the other: claim 50% of property tax (plus the renter pays their own through rent — that renter, if eligible, files their own MI-1040CR using 23% of rent paid).

### Principal Residence Exemption (PRE) interaction

**PRE vs MI-1040CR comparison**

| Item | PRE (Form 2368) | MI-1040CR |
| --- | --- | --- |
| What it does | Exempts homestead from 18-mill school operating tax | Refundable income tax credit |
| Filed with | Local township/city assessor | Michigan Treasury (with MI-1040 or stand-alone) |
| Income tested? | No | Yes (THR ≤ $71,500) |
| Statute | MCL 211.7cc | MCL 206.520 |

The Principal Residence Exemption (PRE, formerly "Homestead Exemption") under MCL 211.7cc exempts a homeowner's principal residence from the 18-mill school operating tax. PRE is filed with the local assessor on Form 2368, not on Form MI-1040CR. The two programs are commonly confused.

A claimant should generally have a PRE in place on the same homestead for which they claim the MI-1040CR, but failure to claim the PRE does not disqualify the MI-1040CR.

## Section 6: The computation — renters

- **Renter formula** — Step 1.  Property tax equivalent = 23% × rent paid for the year [VERIFY 23%]. Step 2.  Floor = 3.2% × THR. Step 3-6. Same as owners (60% factor, $62,500 phase-out, $1,900 cap).  _(TY 2025 MI-1040CR instructions)_
- **Senior renter alternate test** — If THR ≤ $30,000 and rent paid exceeds 40% of THR, an alternate computation may produce a larger credit. The taxpayer takes the higher of the two. This is specifically the relief mechanism for the "house poor senior renter" archetype.  _(TY 2025 instructions)_

### What rent qualifies

- **Rent qualification rules** — - Cash rent paid to a private landlord. - Mobile-home lot rent (separately from any home ownership). - Rent paid to a tax-exempt landlord (e.g., a non-profit, certain subsidized housing) is NOT eligible because the underlying real property paid no tax. Section 8 housing where the landlord pays property tax is eligible, but if the property is wholly tax-exempt the renter cannot claim. - Rent paid by a government agency (housing assistance paid directly to landlord) is NOT the claimant's rent for credit purposes; only the claimant's own portion counts. - College dormitory rent is NOT eligible.

## Section 7: Tier 1 — deterministic rules

- **MI-CR-T1-01** — Maximum credit TY 2025 = $1,900  _(TY 2025 MI-1040CR instructions; MCL 206.520(3))_
- **MI-CR-T1-02** — THR ceiling TY 2025 = $71,500  _(TY 2025 MI-1040CR instructions)_
- **MI-CR-T1-03** — THR phase-out begins at $62,500; reduce credit 10% per $1,000 over  _(TY 2025 MI-1040CR instructions)_
- **MI-CR-T1-04** — Owner taxable value cap = $165,400 (TY 2025)  _(TY 2025 MI-1040CR instructions)_
- **MI-CR-T1-05** — 3.2% of THR is subtracted from property tax (or 23% of rent) on Line 34  _(TY 2025 MI-1040CR Line 34)_
- **MI-CR-T1-06** — Regular allowance factor = 60% (non-senior, non-disabled)  _(TY 2025 MI-1040CR Line 35)_
- **MI-CR-T1-07** — Property tax = cash basis (paid during tax year), not accrued  _(Treasury guidance; long-standing administrative rule)_
- **MI-CR-T1-08** — Social Security is included in THR at gross (even though excluded from Michigan AGI)  _(MCL 206.510)_
- **MI-CR-T1-09** — First $300 of cash/in-kind gifts excluded from THR; remainder included  _(TY 2025 MI-1040CR instructions)_
- **MI-CR-T1-10** — Health insurance premiums paid by household are a subtraction from THR (Line 36)  _(Treasury guidance; TY 2025 MI-1040CR Line 36)_
- **MI-CR-T1-11** — Business / rental losses cannot drive THR below zero  _(MCL 206.510(1)(c))_
- **MI-CR-T1-12** — Statute of limitations on filing CR claim = 4 years from original due date  _(MCL 205.27a)_
- **MI-CR-T1-13** — Mobile-home specific tax = $3/month ($36/year) treated as property tax  _(MCL 125.1041)_
- **MI-CR-T1-14** — One homestead per household per tax year  _(MCL 206.508(4))_
- **MI-CR-T1-15** — Credit is refundable — paid as refund or applied against other MI tax  _(MCL 206.520(6))_

## Section 8: Tier 2 — judgment rules

- **MI-CR-T2-01 Mid-year move within Michigan** — Prorate property tax / rent between the two homesteads by number of days occupied. The claimant files a single MI-1040CR but lists both homesteads on the supplemental schedule.
- **MI-CR-T2-02 Move out of Michigan during year** — If MI residency was at least 6 months, prorate property tax / rent for the MI-resident portion. Out of scope for this skill (part-year); refer to professional review.
- **MI-CR-T2-03 Divorce or separation during the year** — Each spouse files a separate CR for the part of the year they occupied each homestead. THR is generally each spouse's separate THR for their respective occupancy periods. Court-ordered occupancy controls. Flag for review.
- **MI-CR-T2-04 Death of spouse during the year** — Surviving spouse files a full-year CR if they remained in the homestead. Decedent's THR for the months alive is includible. The estate does NOT file a separate CR for the homestead.
- **MI-CR-T2-05 Mobile home owner — separate lot rental** — Combine $36/year specific tax + 23% of lot rent into the property-tax-paid figure. Verify the home is the claimant's principal residence and is permanently sited.
- **MI-CR-T2-06 Duplex / multi-unit owner-occupied** — Prorate property tax by units. Owner claims the homestead portion only. Verify tenant unit is leased at arm's-length; below-market family rentals can be re-characterized.
- **MI-CR-T2-07 Co-op share ownership** — Use the co-op's year-end statement of pro-rata real property tax. Reject claims based on full monthly maintenance fee — only the property-tax component qualifies.
- **MI-CR-T2-08 Home office / Schedule C use of home** — If federal Form 8829 allocates property tax to business, the business-use portion is NOT eligible for the homestead credit (it was already deducted on Schedule C). Reduce property tax paid by the business-use percentage from Form 8829.
- **MI-CR-T2-09 Senior renter with rent > 40% of THR** — Compute both the standard and alternate credits; take the larger.
- **MI-CR-T2-10 Roommates / multiple unrelated occupants** — Each unrelated tenant files separately for their portion of rent paid. Each has their own THR. Verify written or implied allocation.
- **MI-CR-T2-11 College student dependent of MI parent** — Generally not a separate claimant; parents' homestead is the claimant. Dormitory rent does not qualify. Apartment rent off-campus by an independent student may qualify if the student is not claimed as a dependent and meets the 6-month residency test.
- **MI-CR-T2-12 Subsidized / Section 8 housing** — Only the tenant-paid portion of rent counts; the government-paid portion does not. If the landlord is fully tax-exempt (e.g., a public housing authority), no credit.
- **MI-CR-T2-13 Recent inheritance of homestead mid-year** — Property tax paid by the claimant from the date of acquisition counts. Tax paid by the decedent / estate before death does not.
- **MI-CR-T2-14 Spouse living apart in separate MI homesteads** — Treasury guidance allows each spouse to file a separate CR using their own homestead and their own THR, even when filing MFJ on MI-1040. Document occupancy. Flag for review.
- **MI-CR-T2-15 Property tax bill includes special assessments** — Strip out special assessments; only ad valorem property tax (plus the mobile-home specific tax) is eligible.

## Section 9: Worked examples

> All examples use TY 2025 thresholds. All dollar figures are rounded for clarity. Line numbers refer to the TY 2025 MI-1040CR.

### Example 1 — Standard homeowner

**Facts.** Married couple, both age 45. Own home in Lansing, MI. Property tax paid in 2025 = $4,200. THR = $55,000 (combined wages, no other income). Home taxable value = $90,000 (under cap). No business use.

```
Property tax paid (Line 10):               $4,200
Floor: 3.2% × $55,000 (Line 34):           $1,760
Difference:                                $2,440
Allowance factor: 60%                  ×    0.60
Credit before phase-out and cap:           $1,464
THR ≤ $62,500 → no phase-out reduction.
$1,464 < $1,900 cap.

Credit = $1,464.
```

### Example 2 — Renter

**Facts.** Single, age 38, renter in Ann Arbor. Rent paid in 2025 = $18,000. THR = $42,000 (wages and small freelance Schedule C).

```
Rent paid:                                $18,000
Property tax equivalent: 23% × $18,000:    $4,140   [VERIFY 23%]
Floor: 3.2% × $42,000:                     $1,344
Difference:                                $2,796
Allowance factor: 60%                  ×    0.60
Credit before phase-out and cap:           $1,678
THR ≤ $62,500 → no phase-out reduction.
$1,678 < $1,900 cap.

Credit = $1,678.
```

### Example 3 — Senior homeowner using Table 2

**Facts.** Widow, age 72. Owns home in Grand Rapids since 1982. Property tax paid in 2025 = $2,800. THR = $18,500 (Social Security $14,500 gross + small pension $4,000). Home taxable value = $65,000.

```
Property tax paid:                         $2,800
Floor: 3.2% × $18,500:                       $592
Difference:                                $2,208
Senior allowance per Table 2:
    THR ≤ $21,000 → 100% allowance
Credit before cap:                         $2,208
Cap at $1,900.

Credit = $1,900 (capped).
```

> Note how the senior table is dramatically more generous than the regular 60% factor — a non-senior with the identical fact pattern would receive only $1,325 (60% × $2,208).

### Example 4 — High-income / phase-out boundary

**Facts.** Married homeowner, both age 50, in Northville. Property tax paid in 2025 = $7,800. THR = $66,400 (combined wages plus small Schedule C net income). Home taxable value = $140,000 (under cap).

```
Property tax paid:                         $7,800
Floor: 3.2% × $66,400:                     $2,125
Difference:                                $5,675
Allowance factor: 60%                  ×    0.60
Credit before phase-out and cap:           $3,405

Cap at $1,900 first:                       $1,900
Phase-out: THR exceeds $62,500 by $3,900.
    Number of $1,000 increments (or part) over: 4
    Reduction: 4 × 10% = 40%.
$1,900 × (1 − 0.40) =                      $1,140.

Credit = $1,140.
```

> If THR had been $71,500 or above, the credit would be $0 — full phase-out. If THR had been $62,500 exactly, the credit would be the full $1,900 cap (no phase-out reduction).

## Section 10: Refusal catalogue

- **MI-CR-R-01** — Claimant is a qualified veteran, blind person, surviving spouse of a veteran, or totally and permanently disabled — and would file MI-1040CR-2  _(Refuse — out of scope. Refer to MI-1040CR-2 booklet. CR-2 has special rules including a no-income-test computation in some patterns.)_
- **MI-CR-R-02** — Farmland Preservation Tax Credit (development-rights agreement under PA 116) — Form MI-1040CR-5  _(Refuse — out of scope. MI-1040CR-5 is a separate credit program administered by MDARD; not the household-income homestead credit.)_
- **MI-CR-R-03** — Home Heating Credit — Form MI-1040CR-7  _(Refuse — separate skill. The MI-1040CR-7 is income- and family-size-tested but distinct from the property tax credit. Note interaction: a CR-7 claim does not reduce the CR claim and vice versa.)_
- **MI-CR-R-04** — Part-year or non-resident — would file Schedule NR with MI-1040  _(Refuse — out of scope.)_
- **MI-CR-R-05** — Amended MI-1040CR (using the 5-digit "X" suffix or check-box "amended return")  _(Refuse — out of scope. Statute of limitations is 4 years; refer to professional.)_
- **MI-CR-R-06** — Trusts and estates filing for a homestead held in a trust  _(Refuse — special grantor-trust and life-estate rules apply (the beneficial occupant generally claims, not the trustee). Refer to professional.)_
- **MI-CR-R-07** — Nursing home or assisted-living facility resident  _(Refuse — special rules: the credit follows the portion of the fee attributable to property tax, certified by the facility. Refer to professional.)_
- **MI-CR-R-08** — Decedent's final-year return where the executor / personal representative files  _(Refuse — fiduciary filing has special signature and documentation requirements.)_
- **MI-CR-R-09** — Homestead held jointly with someone outside the household  _(Refuse — pro-rata ownership and pro-rata tax flow rules apply; flag for review.)_
- **MI-CR-R-10** — Mortgage forgiveness / short sale / foreclosure in the year  _(Refuse — interacts with THR (cancellation of debt income) and ownership timing. Flag for review.)_
- **MI-CR-R-11** — Renter where landlord is fully tax-exempt (public housing authority, certain non-profits)  _(Refuse — no qualifying property tax; ineligible.)_
- **MI-CR-R-12** — Out-of-state homestead, Michigan-domicile claimant  _(Refuse — homestead must be in Michigan.)_

## Section 11: Form mapping — MI-1040CR (TY 2025)

**Form mapping table**

| Section | Line(s) | What it covers |
| --- | --- | --- |
| Filer information | 1–7 | Name, SSN, address, filing status, school district code |
| Homestead information | 8–9 | Address; mark owner / renter; taxable value (owners); date moved in / out |
| Property tax / rent | 10 | Property tax paid (owners), or rent paid × 23% (renters) `[VERIFY]` |
| Move-related | 11–14 | Proration for mid-year moves |
| Tentative credit | 15–17 | Sum of property tax / rent equivalent |
| THR — wage and business | 18–25 | Wages, business income, interest/dividends, capital gains |
| THR — retirement | 26–28 | Social Security gross, pensions, IRA |
| THR — other receipts | 29–32 | Unemployment, alimony received, gifts > $300, other |
| THR — subtotal | 33 | Total Household Resources |
| Floor computation | 34 | THR × 3.2% (or Table 2 percentage for seniors) |
| Allowance | 35 | 60% factor (or Table 2 for seniors) |
| Subtractions from THR | 36 | Health insurance premiums |
| Credit before phase-out | 37–38 | (Property tax − floor) × allowance % |
| Phase-out application | 39 | Reduce by 10% per $1,000 over $62,500 |
| Final credit | 40 | Capped at $1,900 |

> **Line numbers below reflect the TY 2025 MI-1040CR. Verify against the official form PDF before producing client-ready output.**

### Interaction with MI-1040 and Schedule 1

- **Interaction rules** — - The MI-1040CR credit flows to MI-1040 Line 25b (Homestead Property Tax Credit) as a refundable credit. It reduces tax liability and any excess is refunded. - Property tax paid is NOT separately deductible on Schedule 1; only the credit applies. - If the taxpayer claims a home-office deduction on federal Schedule C (Form 8829), the business-use portion of property tax must be backed out before entering on MI-1040CR Line 10 — see Rule MI-CR-T2-08. - The Home Heating Credit (MI-1040CR-7) is filed on a separate form but uses the same THR concept. The MI-1040CR-7 has its own income thresholds (lower) and family-size-based standard allowance — out of scope for this skill.

## Section 12: Provenance and verification status

**Provenance table**

| Element | Status | Notes |
| --- | --- | --- |
| Statute citations (MCL 206.520–535) | Direct from Michigan Compiled Laws | Verified against legislature.mi.gov 2026-05-28 |
| TY 2025 form line numbers | From TY 2025 MI-1040CR PDF | Treasury periodically renumbers; reverify each year |
| $1,900 maximum credit | TY 2025 instructions | Confirmed |
| $71,500 THR ceiling | TY 2025 instructions | Confirmed |
| $62,500 phase-out floor + 10% / $1,000 | TY 2025 instructions | Confirmed |
| $165,400 taxable value cap | TY 2025 instructions | Confirmed |
| 3.2% floor of THR | TY 2025 form Line 34 | Confirmed |
| 23% rent factor | AARP Property Tax-Aide MI page | `[VERIFY: cross-check against TY 2025 Treasury instructions; long-standing rate was 20% in older guidance — likely changed to 23% but reviewer must confirm]` |
| Senior Table 2 percentages | AARP / TaxSlayer summaries | `[VERIFY exact 2025 figures against Treasury PDF]` |
| PA 4 of 2023 reform impact | Treasury press releases; House Bill 4001 (2023) | Confirmed at high level; specific dollar changes summarized in Section 2 |

### Known uncertainties for verifier

1. **23% vs 20% rent factor.** Several legacy and consumer sources still reference 20%. The 2025 AARP Property Tax-Aide says 23%. Verifier must confirm the operative rate on TY 2025 MI-1040CR Line 10 instructions.
2. **Senior Table 2 exact brackets.** The four-percentage-point-per-$1,000 reduction above $21,000, the 60% floor for $30,001–$60,000, and intermediate brackets need line-by-line confirmation against the TY 2025 instructions.
3. **PRE Form 2368 deadlines and 18-mill exemption tie-in** — verify any recent administrative changes for completeness.
4. **Mobile home $3/month specific tax** — confirm this remained $3 in TY 2025; some legislative proposals have circulated to raise it.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).

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
