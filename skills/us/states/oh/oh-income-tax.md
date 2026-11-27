---
name: oh-income-tax
description: Ohio individual income tax for tax year 2026, retaining verified 2025 return rules and historical cases. Covers IT 1040 filing, residency, business income deduction and 3% business tax, exemptions, credits, adjustments, estimates and penalties. Final 2026 indexed amounts and form outputs are on hold; the original 2026 cases are conditional projections. Trigger on Ohio income tax, IT 1040, Ohio business income deduction, Ohio nonresident and Ohio estimated tax. School district and municipal returns require separate work.
version: "1.2"
jurisdiction: US-OH
tax_year: 2026
last_updated: 2026-11-27
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
---

# Ohio individual income tax (Form IT 1040), tax year 2026

Ohio keeps separate business and nonbusiness tax tracks. The business income deduction remains $250,000 ($125,000 married filing separately), with 3% on taxable business income. The statute sets a 2.75% nonbusiness rate for 2026, but its dollar band and base are subject to annual indexing. **Do not issue a final 2026 return amount or form-line output from this Guide.** The original 2026 projections below retain their assumptions explicitly; verified 2025 computations remain usable within their stated facts. [R.C. 5747.01(A)(28)](https://codes.ohio.gov/ohio-revised-code/section-5747.01), [5747.02(A)(3)–(5)](https://codes.ohio.gov/ohio-revised-code/section-5747.02).

## Scope

This Guide covers individuals: full-year residents, part-year residents and nonresidents, including sole proprietors, individual owners of disregarded single-member LLCs and pass-through owners. Start with an accurately prepared federal AGI; use `us-schedule-c-and-se-computation` for federal business and self-employment calculations and `us-quarterly-estimated-tax` for federal estimates. Federal deductions already reflected in AGI must not be deducted again. Ohio starts from federal AGI with Ohio adjustments, rather than federal taxable income. [R.C. 5747.01(A)](https://codes.ohio.gov/ohio-revised-code/section-5747.01).

## Ask the client first

Obtain the tax year, federal return and filing status; each spouse's domicile, abodes, move dates and Ohio contact periods; all income and adjustments; direct/indirect ownership throughout the entity year; depreciation add-back and recovery history; dependents and ages; prior lump-sum credit elections; each spouse's qualifying income; other-state returns and payment proof; school district and municipalities; withholding, payment dates, prior-year return and its twelve-month period. Ohio generally follows federal joint/separate filing status. [R.C. 5747.08(E)](https://codes.ohio.gov/ohio-revised-code/section-5747.08).

Residents, part-year residents and nonresidents with taxable Ohio income generally file IT 1040, subject to exceptions. No return is required when Ohio AGI is zero or less, exemptions equal/exceed Ohio AGI, or the senior citizen, lump sum distribution and joint filing credits eliminate the tax, **unless school district income tax is owed**. Other credits eliminating tax do not automatically create this exception. Entity-covered nonresident income has separate exceptions under R.C. 5747.08(L); do not assume an entity payment either requires or excuses an individual return. [R.C. 5747.08](https://codes.ohio.gov/ohio-revised-code/section-5747.08); [2025 instructions, p.12](https://dam.assets.ohio.gov/image/upload/tax.ohio.gov/forms/ohio_individual/individual/2025/it1040-booklet.pdf).

A full-year resident of Indiana, Kentucky, Michigan, Pennsylvania or West Virginia whose only Ohio income is employee compensation generally uses reciprocity. This does not exempt qualifying 20%-owner compensation treated as business income, or other Ohio income. A refund of Ohio withholding may still require filing. The 2025 instructions recommend IT 1040 or IT 10 when federal AGI exceeds $28,450 even if an exception applies; that recommendation is not a universal statutory filing threshold. [2025 instructions, pp.12,20](https://dam.assets.ohio.gov/image/upload/tax.ohio.gov/forms/ohio_individual/individual/2025/it1040-booklet.pdf).

## The method, step by step

Use the year-specific rules below, classify income, apply adjustments and the two tax tracks, then test credits and dated payments.

## Rates, bands and thresholds

| Item | Operative rule | Source |
| --- | --- | --- |
| 2025 nonbusiness base at or below $26,050 | No tax. Above $26,050 through $100,000: $342 + 2.75% of excess over $26,050. Above $100,000: $2,394.32 + 3.125% of excess over $100,000. | [5747.02(A)(3)(b)](https://codes.ohio.gov/ohio-revised-code/section-5747.02) |
| 2026 statutory nonbusiness schedule, before applicable indexing | No tax at/below $26,050; above it, $332 + 2.75% of excess over $26,050. Annual August indexing adjusts the dollar amounts, not the rate. Do not treat the unindexed dollars as final 2026 instructions. | [5747.02(A)(3)(c),(5)](https://codes.ohio.gov/ohio-revised-code/section-5747.02) |
| Business deduction and tax, 2025/2026 | Up to $250,000 business income included in federal AGI, or $125,000 married filing separately; 3% on taxable business income after the deduction and applicable exemptions. | [5747.01(A)(28)](https://codes.ohio.gov/ohio-revised-code/section-5747.01), [5747.02(A)(4)](https://codes.ohio.gov/ohio-revised-code/section-5747.02) |
| Exemption eligibility | MAGI below $750,000 for 2025; below $500,000 for 2026 onward. At the limit the exemption is zero. Someone claimable as another taxpayer's dependent gets no personal exemption. | [5747.025(A),(B)](https://codes.ohio.gov/ohio-revised-code/section-5747.025) |
| 2025 amount per qualifying taxpayer, spouse or dependent | MAGI ≤$40,000: $2,400; >$40,000 through $80,000: $2,150; >$80,000 but <$750,000: $1,900. | [2025 instructions, p.17](https://dam.assets.ohio.gov/image/upload/tax.ohio.gov/forms/ohio_individual/individual/2025/it1040-booklet.pdf) |
| Final 2026 dollar amounts/form lines | Non-usable hold: indexed nonbusiness threshold/base, per-person exemption table and final form mapping have not been established here. Check this point with one of our partner accountants. | [5747.02(A)(5)](https://codes.ohio.gov/ohio-revised-code/section-5747.02), [5747.025(C)](https://codes.ohio.gov/ohio-revised-code/section-5747.025) |

Apply the 2025 schedule as printed: neither the initial tax jump nor the change at $100,000 authorizes replacing the $342 base with a computed continuous amount. The 2026 ES worksheet uses $1,900 per exemption and the $500,000 cut-off, but prints the 2025 nonbusiness brackets. It is not proof of final 2026 return dollars. The available **draft** 2026 booklet itself refers to both $26,050 and $26,650 as the zero-tax boundary. Do not call a projection using either conflicting instruction a guaranteed sufficient estimate. [2026 ES](https://dam.assets.ohio.gov/image/upload/v1768492539/tax.ohio.gov/forms/ohio_individual/individual/2026/ites-instructions-fi.pdf); [2026 draft instructions, p.5](https://dam.assets.ohio.gov/image/upload/tax.ohio.gov/forms/DRAFTS/2026/it1040-booklet-draft.pdf).

### From federal AGI to Ohio tax

The following **line numbers belong only to the issued 2025 IT 1040 and schedules**, not a substituted 2026 return. The 2025 federal AGI source is federal Form 1040/1040-SR **line 11a**. [2025 form bundle](https://dam.assets.ohio.gov/image/upload/v1758139620/tax.ohio.gov/forms/ohio_individual/individual/2025/1040-bundle.pdf).

1. Classify income before applying the business deduction. Business income includes regular-course transactions and integral business property; it includes qualifying liquidations/goodwill. An ownership-interest sale qualifies if treated federally as an asset sale or if the seller materially participated in the sale year or any of the preceding five years. A federal Schedule C, E or D label alone does not settle classification. Unclear rentals, mixed-use property or share sales require referral. [R.C. 5747.01(B),(C)](https://codes.ohio.gov/ohio-revised-code/section-5747.01).
2. Compensation or guaranteed payments from a **qualifying entity not subject to R.C. 5733.06 tax**, to an investor holding at least 20% directly or indirectly in profits or capital **at any time during the entity year**, is treated as a distributive share. Mere constructive spouse ownership is not a direct/indirect holding. Do not automatically classify every payment from any company, or every smaller owner's guaranteed payment, using this rule. [R.C. 5733.40(A)(7)](https://codes.ohio.gov/ohio-revised-code/section-5733.40); [2025 instructions, p.24](https://dam.assets.ohio.gov/image/upload/tax.ohio.gov/forms/ohio_individual/individual/2025/it1040-booklet.pdf).
3. On the 2025 Schedule of Business Income, line 10 totals classified business income. Line 11 is the lesser of that total and federal AGI, floored at zero. Line 12 is $250,000/$125,000; line 13 is the lesser of lines 11 and 12, carried to Schedule of Adjustments line 13. Remaining business income (line 14) is capped at IT 1040 line 5 on schedule line 15, carried to IT 1040 line 6. Schedule line 16 is 3% of line 15, carried to IT 1040 line 8b. [2025 form bundle](https://dam.assets.ohio.gov/image/upload/v1758139620/tax.ohio.gov/forms/ohio_individual/individual/2025/1040-bundle.pdf).
4. Ohio AGI = federal AGI + additions − deductions (IT 1040 lines 1 + 2a − 2b = 3). Use actual adjustment conditions, never duplicate a federal/Ohio deduction. Common adjustments are below. **MAGI = Ohio AGI + the business income deduction under R.C. 5747.01(A)(28) + the qualifying-capital-gains/payroll deduction under (A)(34).** It is not always just Ohio AGI plus BID. Special capital-gains eligibility and ordering are outside the simple cases here. [R.C. 5747.01(A),(II)](https://codes.ohio.gov/ohio-revised-code/section-5747.01).
5. Apply qualifying exemptions using MAGI. IT 1040 line 5 is max(Ohio AGI − exemptions,0). Exemptions reduce nonbusiness income first and then business income. Taxable nonbusiness income, line 7, is max(line 5 − line 6,0). Compute the appropriate-year nonbusiness tax (8a), add 3% business tax (8b) to get 8c. Apply nonrefundable credits in statutory/form order, never below zero, to reach line 10. [R.C. 5747.02(A)(4)](https://codes.ohio.gov/ohio-revised-code/section-5747.02); [2025 forms](https://dam.assets.ohio.gov/image/upload/v1758139620/tax.ohio.gov/forms/ohio_individual/individual/2025/1040-bundle.pdf).
6. For 2025, line 11 is IT/SD 2210 interest penalty; 12 unpaid use tax; 13 their sum with line 10. Payments: 14 withholding, 15 estimates/extensions/prior-year carryforward and earlier payments, 16 refundable credits. Follow amended-return adjustments where applicable; 21 is late-payment interest, 22 total due, 23 overpayment. Use whole dollars on the return. These lines do not authorize computing use tax, entity credits or amendments outside this Guide. [2025 forms](https://dam.assets.ohio.gov/image/upload/v1758139620/tax.ohio.gov/forms/ohio_individual/individual/2025/1040-bundle.pdf).

### Common adjustments and depreciation

- Deduct taxable Social Security and qualifying railroad retirement benefits only to the extent included in federal AGI and not already deducted. Add non-Ohio state/local obligation interest otherwise excluded; distinguish U.S. obligations exempt from state tax, which are deductible to the extent included. Ohio public-obligation interest/gains have their own deduction. Refund/reimbursement deductions require inclusion because of prior federal itemized deductions and must be reduced for an amount already deducted by Ohio. [R.C. 5747.01(A)(1)–(5),(7),(8),(11)](https://codes.ohio.gov/ohio-revised-code/section-5747.01); [2025 adjustments, lines 1,15–18,26,28](https://dam.assets.ohio.gov/image/upload/v1758139620/tax.ohio.gov/forms/ohio_individual/individual/2025/1040-bundle.pdf).
- Uniformed-services retirement income is a specific adjustment, not a deduction for every pension. Verify qualifying benefits and inclusion; other military compensation, civilian-spouse elections and residency require separate analysis. Check this point with one of our partner accountants. [2025 adjustments, lines 32–36](https://dam.assets.ohio.gov/image/upload/v1758139620/tax.ohio.gov/forms/ohio_individual/individual/2025/1040-bundle.pdf).
- Qualifying 529 contributions not federally deducted: up to $4,000 per beneficiary per year, taxpayer and spouse **combined even if filing separately**, with excess carried forward. The statute covers qualifying programs under IRC 529, not exclusively Ohio's plan. Nonqualifying distributions can require recapture; do not issue a recapture amount here. Check this point with one of our partner accountants. [R.C. 5747.70](https://codes.ohio.gov/ohio-revised-code/section-5747.70).
- Add back ordinarily **5/6** of federal IRC 168(k) depreciation and qualifying IRC 179 expense above the December 31, 2002 allowance. An employer's qualifying Ohio income-tax withholding increase of at least 10% can reduce it to **2/3**; an increase at least equal to the relevant depreciation expenses can eliminate the add-back. Where the depreciation creates a federal NOL, the full amount is added to the extent specified by the statute. Withholding must be withheld and remitted; compare the relevant current/prior years. A holding below 5% in a pass-through entity permits a **commissioner waiver**, not automatic exclusion. [R.C. 5747.01(A)(17)](https://codes.ohio.gov/ohio-revised-code/section-5747.01).
- Recover a 5/6 add-back by 1/5 in each of five succeeding years; a 2/3 add-back by half in each of two; a full add-back by 1/6 in each of six. Only added-back amounts are recoverable. Division (A)(18)(c) denies the specified recovery to the extent the depreciation results in or increases a federal NOL carryback/carryforward; do not replace this with an unconditional rule for every unrelated NOL. Missing histories, NOL allocation/timing or waiver claims are non-usable here. Check this point with one of our partner accountants. [R.C. 5747.01(A)(18)](https://codes.ohio.gov/ohio-revised-code/section-5747.01).
- Ohio electing-PTE taxes and other-state taxes deducted under IRS notice 2020-75 have add-back rules; their business-income portions can qualify for BID/3%. IT 4738/4708/1140, IT K-1 credits, apportionment and entity-covered filing exceptions need an entity-level reconciliation. Check this point with one of our partner accountants. [R.C. 5747.01(A)(36),(41)](https://codes.ohio.gov/ohio-revised-code/section-5747.01).

### Credits

These are nonrefundable, subject to statutory ordering and remaining liability. Do not assume that every unused credit expires: lump-sum retirement has a special carryover election. Eligibility below is statutory; final 2026 form fields remain on hold.

| Credit | Conditions and computation | Source |
| --- | --- | --- |
| Retirement income | MAGI minus exemptions < $100,000; qualifying retirement income included in Ohio AGI; no disqualifying lump-sum retirement election. Per return: income ≤$500 → $0; >$500–$1,500 → $25; >$1,500–$3,000 → $50; >$3,000–$5,000 → $80; >$5,000–$8,000 → $130; >$8,000 → $200. | [5747.055(A),(B)](https://codes.ohio.gov/ohio-revised-code/section-5747.055) |
| Senior citizen | $50 per return if either spouse is at least 65 at year-end, MAGI minus exemptions < $100,000 and no disqualifying lump-sum distribution credit election. | [5747.055(F),(G)](https://codes.ohio.gov/ohio-revised-code/section-5747.055) |
| Lump-sum retirement / distribution | Both require MAGI minus exemptions below $100,000 and a qualifying lump-sum distribution. Separate elections have lifetime consequences: the retirement election generally bars annual retirement credits; the age-65 distribution election replaces the senior credit and bars later senior credits. Statutory exceptions and retirement carryover election matter. Actual election, life-expectancy amount, prior-election exception or carryover is non-usable here. Check this point with one of our partner accountants. | [5747.055(C)–(G)](https://codes.ohio.gov/ohio-revised-code/section-5747.055) |
| Child/dependent care | MAGI < $20,000: 100%; $20,000 ≤ MAGI < $40,000: 25% of the federal credit for which eligible, **without the IRC 26 limitation**. Not simply the amount actually claimed after federal tax limitation. No credit at $40,000. | [5747.054](https://codes.ohio.gov/ohio-revised-code/section-5747.054) |
| Exemption | $20 per qualifying exemption when MAGI minus exemptions < $30,000. This credit is excluded in calculating estimated payments and withholding. | [5747.022](https://codes.ohio.gov/ohio-revised-code/section-5747.022) |
| Joint filing | MFJ; each spouse has ≥$500 qualifying income included in Ohio AGI, excluding interest, dividends, capital gains, rents/royalties and amounts otherwise deducted (including BID). MAGI must be < $750,000 in 2025 or < $500,000 in 2026 onward. On tax remaining after preceding credits: 20% when MAGI minus exemptions ≤$25,000; 15% >$25,000–$50,000; 10% >$50,000–$75,000; 5% >$75,000. Maximum $650. Retain each spouse's income statement. | [5747.05(E)](https://codes.ohio.gov/ohio-revised-code/section-5747.05) |
| Earned income | 30% of the federal earned income credit allowed for an eligible individual, limited to remaining liability in the required order. | [5747.71](https://codes.ohio.gov/ohio-revised-code/section-5747.71) |
| Home instruction | Qualifying dependent student exempt for home education; lesser of $250 × qualifying students or actual qualifying education expenses. Books, supplies, software/apps/subscriptions qualify under the definition; computers/devices/accessories do not. Keep requested proof. | [5747.72](https://codes.ohio.gov/ohio-revised-code/section-5747.72) |

A qualifying Ohio educator can deduct the lesser of $300 or qualifying expenses **in excess of the federally authorized educator deduction**, without duplicate deductions; the statute's educator definition also requires the Ohio credential. [R.C. 5747.01(A)(31),(JJ)](https://codes.ohio.gov/ohio-revised-code/section-5747.01).

Campaign contributions (including the old 2025 credit and its asserted 2026 repeal), pregnancy-resource-center contributions, certificate-based/business credits and unlisted special deductions: no eligibility or amount output here. Check this point with one of our partner accountants. The existence of a 2025 form line does not prove a 2026 credit or its repeal. [2025 credit schedule](https://dam.assets.ohio.gov/image/upload/v1758139620/tax.ohio.gov/forms/ohio_individual/individual/2025/1040-bundle.pdf).

### Residency and other-state credits

Domicile governs individual residence, subject to the statutory presumptions. For a person with an Ohio abode, a contact period requires being away overnight from the outside-Ohio abode and spending part of **two consecutive days** in Ohio; it does not require sleeping in Ohio. [R.C. 5747.01(I),(J)](https://codes.ohio.gov/ohio-revised-code/section-5747.01); [5747.24(A)](https://codes.ohio.gov/ohio-revised-code/section-5747.24).

The full-year nonresident statement requires **all five**: no more than 212 Ohio contact periods; an outside-Ohio abode for the entire year with no federal depreciation deduction on it; no valid Ohio driver's license/ID during the year; no specified Ohio homestead/owner-occupied reduction for property whose tax-lien date is in the year; and no Ohio-resident tuition based on an Ohio abode. File the statement by the fifteenth day of the tenth following month. The presumption is irrebuttable **unless the statement is false** and does not cover a year of changing domicile into/out of Ohio. For 2025 use the IT 1040/IT 10 nonresident statement boxes, separately for each spouse, rather than the retired separate IT NRS. If a person with an Ohio abode lacks the statement: fewer than 213 contact periods requires rebuttal by preponderance of evidence; 213 or more requires clear and convincing evidence. [R.C. 5747.24(B)–(D)](https://codes.ohio.gov/ohio-revised-code/section-5747.24); [2025 instructions](https://dam.assets.ohio.gov/image/upload/tax.ohio.gov/forms/ohio_individual/individual/2025/it1040-booklet.pdf).

IT NRC credits the tax attributable to income not allocated/apportioned to Ohio; IT RC is limited to the lesser of qualifying other-state/DC liability and Ohio tax on that income. Both are capped by remaining liability; BID allocation, tax deducted federally and its add-back, reciprocal wages and proof of payment affect the calculation. A part-year resident may use the appropriate credits for the respective periods, but never both on the same income. The ordinary IT RC is not a state credit for municipal taxes. Actual multistate allocation/credit with uncertain sourcing, ownership-sale nexus or overlapping entity credits is non-usable here. Check this point with one of our partner accountants. [R.C. 5747.05(A)–(D)](https://codes.ohio.gov/ohio-revised-code/section-5747.05).

### Filing, estimates, interest and amendments

- Calendar-year returns are due April 15 following the year: 2025 → April 15, 2026; 2026 → April 15, 2027, subject to applicable official relief. Ohio automatically recognizes a qualifying federal extension to its later federal deadline; that ordinarily extends filing, **not payment**, unless the commissioner expressly grants payment relief. Keep extension proof and use the return's extension box. [R.C. 5747.08(G)](https://codes.ohio.gov/ohio-revised-code/section-5747.08); [O.A.C. 5703-7-05](https://codes.ohio.gov/ohio-administrative-code/rule-5703-7-05).
- Estimated-tax law covers combined individual and school district tax, after applicable credits, before withholding/estimated payments/prior-refund credit; remember the exemption-credit exclusion. A declaration is generally needed when estimated tax exceeds withholding by **more than $500**. Required annual payment is the lesser of **90% current-year tax or 100% preceding-year tax**, with the preceding-year route requiring a **filed return covering twelve months**. The law does not add a universal timely-filing condition. [R.C. 5747.09(A),(B)](https://codes.ohio.gov/ohio-revised-code/section-5747.09).
- Normal 2026 installments: April 15, June 15, September 15, 2026 and January 15, 2027; each 25% of the required annual amount. Apply withholding, prior-year credit and actual dated payments correctly; withholding ordinarily counts evenly unless actual withholding dates are established. Earlier underpayments are not automatically erased by a later payment needed for its own quarter. Annualized-income and farmers/fishermen exceptions require separate computation. [R.C. 5747.09(B)–(E)](https://codes.ohio.gov/ohio-revised-code/section-5747.09); [2026 ES instructions](https://dam.assets.ohio.gov/image/upload/v1768492539/tax.ohio.gov/forms/ohio_individual/individual/2026/ites-instructions-fi.pdf).
- **Late-prior-return conflict:** issued 2025 IT/SD 2210 instructions condition their prior-year line on a timely return, while R.C. 5747.09 uses a filed twelve-month return. The original late-$6,000-return branch below therefore has no usable automatic penalty-form conclusion. Do not assert that only the 90% route exists in law. Check this point with one of our partner accountants. [2025 IT/SD 2210](https://dam.assets.ohio.gov/image/upload/v1762982566/tax.ohio.gov/forms/ohio_individual/individual/2025/itsd2210-fi.pdf).
- Interest is calendar-year specific: **8% for 2025, 7% for 2026**, not a fixed rate for all payments on a given return. Do not extend 7% into 2027 without that year's determination. [2025 IT/SD 2210, p.4](https://dam.assets.ohio.gov/image/upload/v1762982566/tax.ohio.gov/forms/ohio_individual/individual/2025/itsd2210-fi.pdf); [R.C. 5703.47](https://codes.ohio.gov/ohio-revised-code/section-5703.47).
- Late-filing penalty **may** be imposed, not exceeding the greater of $50/month up to $500 or 5%/month up to 50% of unpaid tax as defined in the statute, using the filing due date including extensions. Thus a zero-tax/refund return does not automatically eliminate the possible dollar penalty. Late-payment penalty **may** be imposed up to **twice the applicable interest charged**, excluding estimated tax; it is not automatically a flat doubled interest-rate charge. Statutory reductions, reasonable cause/no willful neglect and cumulative penalties matter. Do not issue an assessment/abatement amount from this overview. [R.C. 5747.15(A)–(C), authenticated text](https://codes.ohio.gov/assets/laws/revised-code/authenticated/57/5747/5747.15/6-14-2022/5747.15-6-14-2022.pdf).
- Federal AGI/credit adjustments generally require an amended Ohio return within **90 days** of final determination; the R.C. 5747.01(A)(32) disability-severance adjustment has **180 days**. Federal partnership audits have separate provisions. Ordinary refund applications are limited to **four years from payment**; special federal-adjustment/entity-payment refund windows are separate. Those special windows, NOL amendments, assessments and appeals need case-specific review. Check this point with one of our partner accountants. [R.C. 5747.10](https://codes.ohio.gov/ohio-revised-code/section-5747.10); [5747.11](https://codes.ohio.gov/ohio-revised-code/section-5747.11).
- Use OH|TAX eServices/electronic check or card (fees may apply), or an OUPC with a check to Ohio Treasurer of State. Pay Ohio and school district liabilities separately. OUPC payments follow the identified SSN; spouses uncertain of joint/separate filing should pay separately. An IT 4 withholding change is another way to cover estimates. [2026 ES instructions](https://dam.assets.ohio.gov/image/upload/v1768492539/tax.ohio.gov/forms/ohio_individual/individual/2026/ites-instructions-fi.pdf).

## Worked cases

Whole-dollar return figures follow the issued 2025 form. Cents below show arithmetic, not a separate filing convention. Unless stated otherwise, cases assume no other adjustments, credits or payments, and no qualifying-capital-gains/payroll deduction.

**Current case 1; MFJ wages, 2026 compared with 2025.** Preserve wages $90,000 + $30,000, bank interest $2,000, federal AGI $122,000 and one dependent. **Conditional, non-usable 2026 projection:** retain the original $1,900 × three exemptions = $5,700 and unindexed $26,050/$332 assumptions. Base $116,300; projected 2026 tax $2,813.875 → $2,813.88 (whole-dollar $2,814). On the issued 2025 schedule, tax is $2,903.695 → $2,903.70 (whole-dollar $2,904), a raw conditional difference of $89.82 before credits. The final 2026 amount/saving is on hold. Check this point with one of our partner accountants.

```oa-check
name: Conditional 2026 MFJ projection - not a final return amount
inputs:
  fed_agi: 122000
  exemptions: 3
  exemption_amount: 1900
steps:
  - base: fed_agi - exemptions * exemption_amount
  - tax_2026: 332 + 0.0275 * (base - 26050)
  - tax_2025: 2394.32 + 0.03125 * (base - 100000)
  - saving: tax_2025 - tax_2026
expected:
  base: 116300
  tax_2026: 2813.88
  tax_2025: 2903.70
  saving: 89.82
```

**Current case 2; single, 2026 sole proprietor and investment income.** Preserve Schedule C $400,000, interest/dividends $60,000, federal AGI $460,000. BID $250,000 gives Ohio AGI $210,000 and MAGI $460,000. **Conditional, non-usable 2026 projection** using the original $1,900 exemption/unindexed schedule: base $208,100; taxable business $150,000; nonbusiness $58,100; nonbusiness tax $1,213.375 plus business tax $4,500 = $5,713.375 → $5,713.38. Prior 2025 tax $6,000 was timely filed; assume it covers twelve months. With no withholding/credits, the illustrative required annual amount is min($5,142.0375,$6,000) = $5,142.04; installments $1,285.51. These current-year-based outputs are on hold pending final 2026 amounts. The original alternative **late** 2025 return with the same $6,000 remains: the statute does not automatically remove the prior-year route, but penalty-form treatment is referred because of the conflict above. Check this point with one of our partner accountants.

```oa-check
name: Conditional 2026 business and estimate projection - not filing advice
inputs:
  business_income: 400000
  nonbusiness_income: 60000
  fed_agi: 460000
  exemption_amount: 1900
  prior_year_tax: 6000
steps:
  - bid: min(min(business_income, fed_agi), 250000)
  - ohio_agi: fed_agi - bid
  - base: ohio_agi - exemption_amount
  - taxable_business: min(business_income - bid, base)
  - taxable_nonbusiness: base - taxable_business
  - tax_nonbusiness: 332 + 0.0275 * (taxable_nonbusiness - 26050)
  - tax_business: taxable_business * 0.03
  - total_tax: tax_nonbusiness + tax_business
  - required_annual: min(total_tax * 0.9, prior_year_tax)
  - installment: required_annual * 0.25
expected:
  ohio_agi: 210000
  taxable_business: 150000
  taxable_nonbusiness: 58100
  tax_nonbusiness: 1213.38
  total_tax: 5713.38
  required_annual: 5142.04
  installment: 1285.51
```

**Historical case 1; single sole proprietor, 2025.** Schedule C $300,000, federal AGI $285,000 after the original federal SE/SEP deductions, no other adjustments/dependents. BID $250,000; Ohio AGI $35,000; MAGI $285,000; exemption $1,900; base $33,100, all taxable business income after the base cap; tax **$993**. The earlier assertion of the same $993 for 2026 remains only conditional on a final $1,900 exemption, not a final return answer. Check this point with one of our partner accountants.

**Historical case 2; MFJ, 2025 joint credit.** Wages $90,000 + $30,000, interest $2,000, federal AGI/MAGI $122,000, one dependent, no adjustments. Three $1,900 exemptions; base $116,300; whole-dollar tax $2,904. Each spouse's wages exceed $500; 5% joint credit on that tax rounds to $145, below the $650 cap. With no other credits, tax after credit **$2,759**.

```oa-check
name: Historical 2025 MFJ joint credit
inputs:
  wages_one: 90000
  wages_two: 30000
  interest: 2000
steps:
  - fed_agi: wages_one + wages_two + interest
  - base: fed_agi - 3 * 1900
  - tax: round(2394.32 + 0.03125 * (base - 100000))
  - joint_credit: round(min(tax * 0.05, 650))
  - net_tax: tax - joint_credit
expected:
  fed_agi: 122000
  base: 116300
  tax: 2904
  joint_credit: 145
  net_tax: 2759
```

**Historical case 3; retiree aged 70, 2025.** Pension/IRA $40,000 plus taxable Social Security $20,000 gives federal AGI $60,000; deduct the $20,000 Social Security: Ohio AGI/MAGI $40,000. Exemption $2,400; nonbusiness base $37,600. Tax $342 + 2.75% × $11,550 = $659.625 → $660. Assuming qualifying retirement distributions and neither disqualifying lump-sum election: retirement credit $200 + senior credit $50, leaving **$410**.

**Historical case 4; 2026 estimates.** Prior 2025 tax $3,000 on a timely filed twelve-month return, expected 2026 tax after applicable credits $4,000, no Ohio withholding or school district liability. Lesser of 90% × $4,000 = $3,600 and $3,000 is $3,000: **four $750 installments**, April 15, June 15, September 15, 2026 and January 15, 2027. The $4,000 is the original assumed annual liability, not a computation from unconfirmed 2026 bands.

```oa-check
name: Historical 2026 estimate from known prior-year tax
inputs:
  prior_year_tax: 3000
  current_year_tax: 4000
steps:
  - required_annual: min(current_year_tax * 0.9, prior_year_tax)
  - installment: required_annual / 4
expected:
  required_annual: 3000
  installment: 750
```

**Historical case 5; snowbird, 2025.** Ohio and Florida homes; 150 Ohio contact periods; the Florida abode held for the entire year and not federally depreciated; Ohio license surrendered in 2024 with no valid Ohio ID in 2025; no specified homestead/owner-occupied reduction and no Ohio-abode-based in-state tuition. Assuming no domicile change and a truthful statement, all five criteria support the nonresident statement due **October 15, 2026**. Keeping a valid Ohio license defeats that statement route; with an Ohio abode and fewer than 213 contacts, the rebuttable resident presumption can instead be overcome by preponderance of evidence.

**Historical case 6; bonus depreciation, 2025.** Federal 168(k) $60,000 on equipment, no employees and no NOL. Under the ordinary rule, assuming no qualifying withholding exception, add back 5/6 = **$50,000**; recover **$10,000 each year 2026–2030**, subject to the statutory NOL restriction. A later NOL/waiver question requires referral, not an automatic recovery amount.

## When to refuse or refer

A supplier/platform changing hands does not itself decide whether a receipt is business income; test its character and ownership using the rules above. Do not infer tax residence from a mailing address or copy a federal schedule total without classification. Common sole-proprietor, wage, retiree and estimate cases remain above; ownership sales, rental/royalty mixed activities and entity compensation need the relevant tests.

- School district tax: identify the district of residence and whether taxable income creates a liability; merely working in a district is insufficient. A liable resident files SD 100 separately and also IT 1040 even if no state tax is due. Do not assume a district rate/base. [2025 instructions, p.56](https://dam.assets.ohio.gov/image/upload/tax.ohio.gov/forms/ohio_individual/individual/2025/it1040-booklet.pdf).
- Municipal tax: identify every relevant residence/work municipality and its administrator; do not infer a rate, credit or return from this state Guide. `oh-payroll` covers employer work; separate municipal/school district returns, sales tax/CAT, fiduciary returns, PTE returns and certificate credits are outside this computation. Check this point with one of our partner accountants.
- Federal conformity, the R.C. 5701.11 election, retroactive amendments, farmers/fishermen, annualized estimates, military/spouse residency, complex multistate sourcing, NOLs, missing depreciation histories, assessments/appeals and rare deductions: no actual outcome here until case-specific authority and conditions are established. Check this point with one of our partner accountants.
- **Final 2026 indexed dollars, credit/form fields and return outputs remain non-usable here.** Do not silently substitute a 2025 form or convert the original conditional examples into final 2026 amounts. Check this point with one of our partner accountants.

Before completion: confirm year and usable output; federal filing status/AGI; each spouse's residency and statement conditions; business classification and ownership timing; MAGI including applicable A(34) deduction; exemption eligibility; depreciation history; credit conditions and order; dated payments and estimates; and separate local-tax work.

## Sources

Official law, issued 2025 forms/booklet, 2026 ES instructions and the explicitly labelled 2026 draft cited above were read on **2026-11-27**. The statute governs where the ES/penalty form or draft conflicts with it. The 2026 draft is evidence of unresolved form/indexing applicability, not final authority. Source URLs and operative subsections appear beside each rule; the worked cases use those same rules.

| Official source | URL | Read on |
| --- | --- | --- |
| Read for: Definitions, adjustments, MAGI; current text effective March 5, 2026 | https://codes.ohio.gov/ohio-revised-code/section-5747.01 | 2026-11-27 |
| Read for: 2025 rates; statutory 2026 rate and indexing | https://codes.ohio.gov/ohio-revised-code/section-5747.02 | 2026-11-27 |
| Read for: Exemption eligibility and indexing | https://codes.ohio.gov/ohio-revised-code/section-5747.025 | 2026-11-27 |
| Read for: Qualifying entity and owner compensation | https://codes.ohio.gov/ohio-revised-code/section-5733.40 | 2026-11-27 |
| Read for: Resident, nonresident and joint credits | https://codes.ohio.gov/ohio-revised-code/section-5747.05 | 2026-11-27 |
| Read for: Domicile and contact-period presumptions | https://codes.ohio.gov/ohio-revised-code/section-5747.24 | 2026-11-27 |
| Read for: Retirement, senior and lump-sum credits | https://codes.ohio.gov/ohio-revised-code/section-5747.055 | 2026-11-27 |
| Read for: Child/dependent care credit | https://codes.ohio.gov/ohio-revised-code/section-5747.054 | 2026-11-27 |
| Read for: Exemption credit and estimate exclusion | https://codes.ohio.gov/ohio-revised-code/section-5747.022 | 2026-11-27 |
| Read for: Earned income credit | https://codes.ohio.gov/ohio-revised-code/section-5747.71 | 2026-11-27 |
| Read for: Home instruction credit | https://codes.ohio.gov/ohio-revised-code/section-5747.72 | 2026-11-27 |
| Read for: 529 deductions and recapture | https://codes.ohio.gov/ohio-revised-code/section-5747.70 | 2026-11-27 |
| Read for: Return filing and due date | https://codes.ohio.gov/ohio-revised-code/section-5747.08 | 2026-11-27 |
| Read for: Estimates and underpayments | https://codes.ohio.gov/ohio-revised-code/section-5747.09 | 2026-11-27 |
| Read for: Federal-adjustment amendments | https://codes.ohio.gov/ohio-revised-code/section-5747.10 | 2026-11-27 |
| Read for: Refund windows | https://codes.ohio.gov/ohio-revised-code/section-5747.11 | 2026-11-27 |
| Read for: Annual interest-rate determination | https://codes.ohio.gov/ohio-revised-code/section-5703.47 | 2026-11-27 |
| Read for: Filing extension and payment distinction | https://codes.ohio.gov/ohio-administrative-code/rule-5703-7-05 | 2026-11-27 |
| Read for: Penalties; authenticated June 14, 2022 text, current section confirmed in chapter listing | https://codes.ohio.gov/assets/laws/revised-code/authenticated/57/5747/5747.15/6-14-2022/5747.15-6-14-2022.pdf | 2026-11-27 |
| Read for: Issued 2025 IT 1040 instructions; preserved 2025 rules | https://dam.assets.ohio.gov/image/upload/tax.ohio.gov/forms/ohio_individual/individual/2025/it1040-booklet.pdf | 2026-11-27 |
| Read for: Issued 2025 IT 1040 and schedules; 2025 form mapping only | https://dam.assets.ohio.gov/image/upload/v1758139620/tax.ohio.gov/forms/ohio_individual/individual/2025/1040-bundle.pdf | 2026-11-27 |
| Read for: Issued 2025 IT/SD 2210; calendar interest and timeliness conflict | https://dam.assets.ohio.gov/image/upload/v1762982566/tax.ohio.gov/forms/ohio_individual/individual/2025/itsd2210-fi.pdf | 2026-11-27 |
| Read for: 2026 estimated-tax worksheet; conflicting nonbusiness brackets labelled above | https://dam.assets.ohio.gov/image/upload/v1768492539/tax.ohio.gov/forms/ohio_individual/individual/2026/ites-instructions-fi.pdf | 2026-11-27 |
| Read for: DRAFT 2026 booklet; conflicting threshold, no final-return authority | https://dam.assets.ohio.gov/image/upload/tax.ohio.gov/forms/DRAFTS/2026/it1040-booklet-draft.pdf | 2026-11-27 |

Not yet confirmed: final 2026 indexed nonbusiness dollar band/base, exemption dollar amounts and return/credit form fields; resolution of the late-prior-return penalty-form conflict; rare election, credit, sourcing and assessment outputs explicitly referred above. Check this point with one of our partner accountants.
