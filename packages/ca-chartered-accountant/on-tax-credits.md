---
name: on-tax-credits
description: Use this skill for Ontario personal tax credits — Ontario Trillium Benefit (OTB), OEPTC (Ontario Energy and Property Tax Credit), Ontario Sales Tax Credit (OSTC), NOEC (Northern Ontario Energy Credit), Ontario Child Care Tax Credit (CARE), Ontario Senior Homeowners Property Tax Grant, Ontario Senior Care at Home Credit. Triggers "Ontario Trillium", "OTB", "OEPTC Ontario", "CARE credit Ontario", "Form ON479". ALWAYS read alongside ca-fed-t1-return.
jurisdiction: CA
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# ON Tax Credits

## Ontario — Personal Tax Credits & Trillium Benefit — Skill v1.0

This skill governs the computation, claim mechanics, and reviewer presentation of Ontario personal tax credits delivered through the T1 General return (Forms ON428, ON479) and the combined Ontario Trillium Benefit (OTB) delivered via Form ON-BEN. It applies to Ontario residents only. It MUST be loaded alongside `ca-fed-t1-return` because the Ontario credits depend on federal taxable income, federal net income (Line 23600), federal eligible dependants, and the federal CCB/GST credit infrastructure that the CRA uses to pay OTB monthly.

The reviewer must be a Canadian-credentialed practitioner (CPA, or registered EFILE preparer with Ontario T1 experience). The output of this skill is a worksheet and reviewer brief — never a final filed return without human sign-off.

## 1. Quick reference — credit table

**Ontario credits quick reference table**  _(Form ON-BEN, ON428, ON479, ON479-A, ON428-A)_

| Credit | Refundable? | Form line / Schedule | 2025 max amount | Income tested? | Trigger |
| --- | --- | --- | --- | --- | --- |
| OEPTC (Ontario Energy & Property Tax Credit) | Refundable (paid via OTB) | Form ON-BEN | $1,248 (non-senior); $1,421 (senior 65+) | Yes — reduced at adjusted family net income (AFNI) thresholds | Rent paid, property tax paid, energy on reserve, public LTC home accommodation |
| OSTC (Ontario Sales Tax Credit) | Refundable (paid via OTB) | Form ON-BEN (no separate claim — auto-assessed) | $360 per adult + $360 per qualified child | Yes — clawback at AFNI > $27,729 single / $34,661 family | Resident of Ontario on Dec 31 |
| NOEC (Northern Ontario Energy Credit) | Refundable (paid via OTB) | Form ON-BEN | $180 single / $277 family | Yes — clawback at AFNI thresholds | Resident of Northern Ontario (defined districts) |
| OTB (Ontario Trillium Benefit) | Refundable, monthly | Combined OEPTC + OSTC + NOEC | Sum of components | Yes (each component) | Apply via ON-BEN with T1 |
| Ontario Child Care Tax Credit (CARE) | Refundable | Schedule ON479-A | 75% of eligible child-care expenses, max effective benefit varies (cap $6,000 per child under 7, $3,750 per child 7-16, $8,250 per child with disability) | Yes — declines linearly with family income above $20,000 to zero at $150,000 | Eligible child-care expenses already claimed federally on Form T778 |
| Ontario Senior Homeowners' Property Tax Grant (OSHPTG) | Refundable | Form ON-BEN, Part D | $500 | Yes — clawback at AFNI > $35,000 single / $45,000 couple | Age 64+ on Dec 31 of prior year, owned and paid property tax |
| Ontario Senior Care at Home Tax Credit | Refundable | Schedule ON479-A | 25% × eligible medical expenses, max credit $1,500 (i.e. up to $6,000 expenses) | Yes — phase-out begins at family net income $35,000, full phase-out at $65,000 | Age 70+ at year-end, eligible medical expenses |
| Ontario non-refundable credits (basic personal amount, age amount, spousal, disability, etc.) | Non-refundable | Form ON428 | BPA $12,747 for 2025 (indexed) | n/a (some age/spousal income-tested) | Resident of Ontario on Dec 31 |
| Ontario LIFT credit (low-income individuals & families tax credit) | Non-refundable | Schedule ON428-A | $885 max (2025) | Yes — reduced 5% above $34,355 individual income | Employment income, Ontario resident |

(All amounts are 2025 program-year figures; OTB benefit year runs July 2025 – June 2026 based on 2024 tax return information. Where the user is preparing the 2025 T1, the OTB amounts on that return drive the July 2026 – June 2027 benefit year.)

## 2. Required inputs + refusal catalogue

### 2.1 Inputs the skill MUST have before computing

- **Required inputs list** — Federal Line 23600 (net income) for taxpayer and spouse/common-law partner; Federal Line 26000 (taxable income); Marital status on Dec 31, 2025; Residency: was the taxpayer resident in Ontario on Dec 31, 2025? Was the taxpayer resident in Northern Ontario? (If yes, list of qualifying districts: Algoma, Cochrane, Kenora, Manitoulin, Nipissing, Parry Sound, Rainy River, Sudbury (incl. City of Greater Sudbury), Thunder Bay, Timiskaming.); Number of qualified dependent children under 19 and their dates of birth; Rent paid in Ontario during 2025 (amount + months + landlord name + address); Property tax paid on principal residence in Ontario during 2025; Long-term care home accommodation amount paid (public LTC only, not retirement-home rent — the public/non-profit portion of the bill); Home energy costs paid on a reserve (where applicable); Eligible child-care expenses already claimed federally on Form T778 (need both amount and the child it relates to); Age of taxpayer and spouse on Dec 31, 2025; For Senior Homeowners' Property Tax Grant: age on Dec 31, 2024 (because the grant is based on prior-year age and prior-year property tax); For Senior Care at Home: itemized eligible medical expenses where the recipient is age 70+  _(§2.1)_

### 2.2 Refusal catalogue — out of scope (refer to a credentialed Ontario preparer)

- **R-ON-1** — Part-year Ontario residents — the OTB requires Ontario residency on the first day of each payment month; prorations are non-trivial and require manual CRA reconciliation. Refer.  _(R-ON-1)_
- **R-ON-2** — Non-resident landlords or rent paid to a related party — the rent eligibility test under OEPTC requires landlord arm's-length and Ontario property. Refer.  _(R-ON-2)_
- **R-ON-3** — Co-tenants splitting rent unevenly — only the rent the taxpayer actually paid counts; verbal splits and gift-of-rent arrangements need documentation. Refer if not documented.  _(R-ON-3)_
- **R-ON-4** — Long-term care accommodation where the bill is mixed public and private — the OEPTC eligible amount is the public-pay portion only; private retirement residences are not eligible. Refer.  _(R-ON-4)_
- **R-ON-5** — Trusts, deceased taxpayer (final T1), or bankruptcy returns — OTB and CARE entitlement rules differ. Refer.  _(R-ON-5)_
- **R-ON-6** — Reserve residents claiming both home energy on reserve and property tax off reserve — uncommon and requires CRA confirmation. Refer.  _(R-ON-6)_
- **R-ON-7** — Child-care expense disputes (e.g. unlicensed provider without SIN, summer camp eligibility questions) — refer to federal T778 reviewer before the Ontario CARE credit is computed.  _(R-ON-7)_
- **R-ON-8** — Senior Care at Home credit where the "eligible medical expenses" include attendant care that is also being claimed under the federal disability supports deduction (Line 21500) or the federal medical expense tax credit METC — no-double-claim rule applies; refer to a senior tax specialist.  _(R-ON-8)_
- **R-ON-9** — OEPTC claimed by a person who lived in a designated Ontario university/college residence — only the $25 student residence amount applies, never the rent figures. Flag and refer.  _(R-ON-9)_
- **R-ON-10** — Anything involving Ontario tax credits not on the 2025 ON428/ON479/ON-BEN forms (e.g. the Ontario Staycation Tax Credit, which was a 2022-only temporary credit and is NOT available for 2025) — refuse and explain.  _(R-ON-10)_

## 3. Ontario Trillium Benefit (OTB) — combined monthly payment

The OTB is a combined monthly payment of three otherwise-separate refundable credits:

- **OEPTC** — Ontario Energy and Property Tax Credit
- **OSTC** — Ontario Sales Tax Credit
- **NOEC** — Northern Ontario Energy Credit (only for Northern Ontario residents)

### 3.1 Application mechanics

- **OTB application and payment mechanics** — The taxpayer applies for OTB by filing Form ON-BEN with the T1 General. Filing the T1 alone is not enough — the ON-BEN tick-boxes and rent/property-tax entries are required. The benefit year runs from July of the year after the tax year, through June of the second year after. So the 2025 T1 drives the July 2026 – June 2027 OTB. CRA pays OTB monthly on the 10th of each month (or prior business day). Annual entitlement under $360 is paid as a single July lump sum. Taxpayers may also elect a single June lump-sum payment by ticking the box on Form ON-BEN. Direct deposit and address on file with CRA must be current. Marital status changes mid-benefit-year affect entitlement — the taxpayer must notify CRA within 30 days. OTB is administered by CRA on behalf of the Province of Ontario. It is not subject to Ontario tax (it is non-taxable income).  _(§3.1)_

### 3.2 Eligibility framework (all OTB components)

- **OTB eligibility framework** — Eligibility for each component is tested on the first day of each payment month. The skill computes annual entitlement from the 2025 T1; CRA prorates monthly entitlement based on eligibility on the first of each month. Common eligibility floor for all three components: the taxpayer must be a resident of Ontario on Dec 31, 2025, and at least one of: age 18+; have or had a spouse or common-law partner; or be a parent who lived with their child.  _(§3.2)_

### 3.3 Total OTB on the return

- **Annual OTB entitlement output** — The skill outputs the annual OTB entitlement as a single figure on the reviewer brief. CRA will split into 12 monthly payments. The skill does NOT estimate monthly payments — it estimates the annual figure and notes the payment frequency.  _(§3.3)_

## 4. OEPTC — Ontario Energy and Property Tax Credit

### 4.1 Two sub-components

- **OEPTC energy and property tax components** — OEPTC has an energy component and a property-tax component, summed and then income-tested. Energy component (2025): Up to $282 (non-senior, non-reserve, non-LTC) — based on whether the taxpayer paid rent or property tax in Ontario in 2025. Up to $321 (senior 65+). For on-reserve home energy: enter actual home-energy costs paid on a reserve; the credit calculation is the lesser of $282/$321 or the energy costs. Property tax component (2025): Non-senior under 65: up to $966. Senior 65+: up to $1,100. Computed as the lesser of: (rent paid × 20%) + property tax paid + $25 (if student residence) + LTC accommodation amount, or the maximum.  _(§4.1)_

### 4.2 Combined OEPTC maximum (2025)

- **Combined OEPTC maximum** — Non-senior: $1,248 (= $282 energy + $966 property tax); Senior 65+: $1,421 (= $321 energy + $1,100 property tax)  _(§4.2)_

### 4.3 Income test (clawback)

- **OEPTC phase-out formula** — OEPTC begins to phase out at adjusted family net income (AFNI) above: $27,729 for single individuals (no children, no spouse); $34,661 for families (with spouse and/or qualified children). Phase-out rate: 2% of AFNI in excess of the threshold reduces the OEPTC. Adjusted family net income = sum of federal Line 23600 of taxpayer and spouse (where applicable), minus UCCB and RDSP income reported (legacy carve-out — UCCB has not existed since 2016 but the formula text retains the language).  _(§4.3)_

### 4.4 Eligible payments

- **OEPTC eligible payments definitions** — Rent: paid for principal residence in Ontario, to a non-related arm's-length landlord, for housing subject to municipal property tax. Rent paid to a family member who owns the property is allowed only if the landlord actually pays property tax on it. University/college residence: only the $25 flat student residence amount applies. Property tax: paid to a municipality on the taxpayer's principal residence in Ontario. Includes condo property tax (the portion of condo fees that is property tax — typically itemized on the annual condo statement). Long-term care accommodation: the public/non-profit portion of the accommodation bill from a licensed Ontario long-term care home. Does NOT include private retirement homes. Reserve home energy: heating fuel, electricity, water for a principal residence on a reserve.  _(§4.4)_

### 4.5 Rent paid by multiple occupants

- **Rent-sharing rule** — If two or more unrelated occupants share rent and the landlord agrees, each can claim their portion. Spouses/common-law partners are treated as one household — only one person claims OEPTC.  _(§4.5)_

### 5.1 Base amount (2025 program year)

- **OSTC base amount** — $360 per adult (taxpayer); +$360 per spouse/common-law partner; +$360 per qualified child under 19 (same qualified-child definition as the federal CCB). A family of four (2 adults + 2 kids) has a base OSTC of $1,440 before clawback.  _(§5.1)_

### 5.2 Income test

- **OSTC phase-out formula** — Single, no children: phase-out begins at AFNI $27,729, reduced 4% of excess AFNI. Family (with spouse and/or children): phase-out begins at AFNI $34,661, reduced 4% of excess AFNI.  _(§5.2)_

### 5.3 Claim mechanics

- **OSTC claim mechanics** — The taxpayer does NOT need to apply specifically for OSTC. Filing a T1 (with or without ON-BEN) automatically triggers OSTC assessment if the taxpayer ticks the OTB application box on ON-BEN. CRA computes OSTC from the return data — taxpayer cannot manually override the calculation.  _(§5.3)_

### 5.4 Qualified child rule

- **OSTC qualified child definition** — A "qualified child" for OSTC matches the federal CCB definition: Under 19 at the start of the payment month; Lives with the taxpayer; Taxpayer is the primary caregiver; Child is a Canadian resident. In shared-custody situations, the federal shared-custody rule applies — each parent receives 50% of the per-child amount.  _(§5.4)_

### 6.1 Northern Ontario definition

- **Northern Ontario districts** — The taxpayer must be a resident on Dec 31, 2025 of one of these districts: Algoma, Cochrane, Kenora, Manitoulin, Nipissing, Parry Sound, Rainy River, Sudbury (including the City of Greater Sudbury), Thunder Bay, Timiskaming.  _(§6.1)_

### 6.2 Base amounts (2025)

- **NOEC base amounts** — $180 single (no children, no spouse); $277 family (taxpayer with spouse and/or one or more qualified children). (Note — the family amount of $277 is a single household amount, not "per child". The OSTC and OEPTC are the per-child credits; NOEC is per household.)  _(§6.2)_

### 6.3 Income test

- **NOEC phase-out formula** — Single: phase-out begins at AFNI $48,520, reduced 1% of excess. Family: phase-out begins at AFNI $62,386, reduced 1% of excess. (NOEC phase-out thresholds are higher than OEPTC/OSTC because NOEC is targeted at energy cost relief for the entire Northern Ontario household economic strata.)  _(§6.3)_

### 6.4 Eligibility checks

- **NOEC eligibility checks** — Same residency tests as OEPTC plus the Northern Ontario district requirement. Either rent paid OR property tax paid OR LTC accommodation OR on-reserve home energy is required. NOEC is not paid in the absence of housing-cost evidence.  _(§6.4)_

### 7.1 Mechanism

- **CARE credit mechanism** — The Ontario CARE credit is a refundable top-up on top of the federal child-care expense deduction (Form T778). It is calculated as a percentage of the amount the taxpayer already claimed federally on Line 21400. Filed via Schedule ON479-A.  _(§7.1)_

### 7.2 Eligible expenses cap (already capped federally)

- **Federal T778 eligible expense caps** — The federal T778 caps eligible expenses at: $8,000 per child under age 7 at year-end; $5,000 per child age 7-16 at year-end; $11,000 per child eligible for the Disability Tax Credit (any age). The Ontario CARE credit applies its rate to these federally-determined eligible expenses (after the lower-income-spouse rule, the 2/3 earned-income limit, etc.). The skill MUST consume the federal T778 output, not raw receipts.  _(§7.2)_

### 7.3 Rate

- **CARE rate schedule** — Maximum rate: 75% of eligible expenses, declining linearly as family income rises. Rate by family income (Line 23600 of both spouses, summed): Family income ≤ $20,000: 75%; Family income $20,001 – $40,000: 75% reduced by 2% for each full $2,500 of family income above $20,000; Family income $40,001 – $60,000: rate continues to decline along the same gradient; ...; Family income ≥ $150,000: 0%. Practical effect: the credit is fully phased out at family income of $150,000.  _(§7.3)_

### 7.4 No-double-claim rule

- **CARE no-double-claim rule** — Same expense cannot be claimed: on the federal child-care deduction (Line 21400) AND not eligible for CARE (incorrect — the federal claim is the input to CARE; double-counting refers to using the same receipt for two different children, or for both child care and the disability supports deduction Line 21500). The skill must reconcile against the federal T778 to confirm only eligible federally-claimed amounts feed into the CARE base.  _(§7.4)_

### 7.5 Examples in §12 below

### 8.1 Amount and trigger

- **OSHPTG amount and trigger** — Maximum grant: $500. Refundable, paid as a single lump-sum (not monthly like OTB). Triggered by Form ON-BEN, Part D.  _(§8.1)_

### 8.2 Eligibility

- **OSHPTG eligibility** — Age 64+ on Dec 31 of the prior year (i.e. 64+ on Dec 31, 2024 to receive the grant in the 2025 T1 cycle, paid in late 2026); Owned and occupied a principal residence in Ontario; Paid Ontario property tax on that residence.  _(§8.2)_

### 8.3 Income test

- **OSHPTG income test** — Single (no spouse): full $500 up to AFNI $35,000; phase-out 3.33% of AFNI above $35,000 (fully phased out around AFNI $50,000). Couple: full $500 up to AFNI $45,000; phase-out 3.33% of AFNI above $45,000 (fully phased out around AFNI $60,000).  _(§8.3)_

### 8.4 Coordination

- **OSHPTG and OEPTC coordination** — OSHPTG can be claimed in addition to the OEPTC property-tax component. The same property tax payment can support both credits.  _(§8.4)_

### 9.1 Mechanism

- **Senior Care at Home mechanism** — A refundable credit equal to 25% of eligible medical expenses incurred by a senior on attendant care, home nursing, in-home therapy, and related care expenses. Filed on Schedule ON479-A.  _(§9.1)_

### 9.2 Caps

- **Senior Care at Home caps** — Eligible expenses cap: $6,000 per senior (so maximum credit is 25% × $6,000 = $1,500). The senior must be age 70+ at year-end (Dec 31, 2025).  _(§9.2)_

### 9.3 Eligible expenses

- **Senior Care at Home eligible/excluded expenses** — Eligible expenses are a subset of the federal medical expense tax credit (METC) basket — specifically the in-home care / attendant care / home-based medical expenses. Examples: Attendant care wages (with attendant SIN); Home nursing services; Home-based occupational, physiotherapy, speech therapy services; Hospital beds and home oxygen rented for use at home; Diabetic care supplies used at home. Excluded: Long-term care home accommodation (handled by OEPTC); Prescription drugs (handled by federal METC only); Travel medical expenses (federal METC only).  _(§9.3)_

### 9.4 Income test

- **Senior Care at Home income test** — Phase-out begins at family net income $35,000. Reduction rate: 5% of family net income in excess of $35,000. Fully phased out at family net income $65,000.  _(§9.4)_

### 9.5 No-double-claim rule

- **Senior Care at Home optimization rule** — The same medical receipt cannot be claimed for: the federal METC (Schedule 1, Line 33099 or 33199) AND the Ontario Senior Care at Home credit. The skill MUST tag each receipt to one program or the other. As a general optimization, if the senior's marginal federal METC benefit is lower than 25%, route to the Ontario Senior Care at Home credit. If the federal METC benefit (combined federal 15% + Ontario non-refundable 5.05%) exceeds 25% effective return, route to METC. This is the senior-care optimization rule the skill must apply and surface to the reviewer.  _(§9.5)_

### 10.1 Form ON428 (Ontario Tax)

- **Form ON428 mechanics** — Computes Ontario non-refundable credits (BPA, age, spousal, dependant, disability, donations, etc.) and Ontario tax payable on taxable income. Reviewer brief must show Ontario taxable income, Ontario tax before credits, non-refundable credits at 5.05% (lowest Ontario bracket rate), Ontario surtax (5.05%×Ontario tax thresholds), and Ontario health premium. The LIFT credit is on Schedule ON428-A and reduces Ontario tax (non-refundable).  _(§10.1)_

### 10.2 Form ON479 (Ontario Credits)

- **Form ON479 mechanics** — Houses refundable credits that are not part of OTB. For 2025, ON479 includes: Ontario Political Contribution Tax Credit; Ontario Focused Flow-Through Share Tax Credit; Ontario Co-operative Education Tax Credit (corporations only — not on personal ON479 in 2025); etc. The personally-relevant 2025 ON479 line items the skill must check: Ontario political contributions. Schedule ON479-A houses CARE and the Senior Care at Home credit.  _(§10.2)_

### 10.3 Form ON-BEN (Application for the 2026 OTB and OSHPTG)

- **Form ON-BEN mechanics** — Filed with the 2025 T1. Drives the July 2026 – June 2027 OTB benefit year and the 2026 OSHPTG. Required entries: tick-box to apply; rent paid + landlord name + landlord address; property tax paid + municipality; LTC accommodation paid + home name; Northern Ontario tick-box. Without ON-BEN, no OTB or OSHPTG is paid even if the taxpayer is eligible.  _(§10.3)_

### 10.4 Schedule ON479-A

- **Schedule ON479-A contents** — CARE credit computation (children, eligible expenses, family income). Senior Care at Home credit computation (senior age, eligible expenses, family income).  _(§10.4)_

### 10.5 Sequence on the T1

- **T1 sequence for Ontario credits** — 1. Compute federal taxable income (Line 26000). 2. Compute Form ON428 — Ontario tax, non-refundable credits, surtax, health premium → Ontario tax payable Line 42800 of T1. 3. Compute Form ON479 + Schedule ON479-A — Ontario refundable credits → flow to Line 47900 of T1. 4. Complete Form ON-BEN — application only; benefit is paid separately, NOT a line on the T1 itself.  _(§10.5)_

## 11. Coordination with federal credits — no-double-claim rules

**No-double-claim coordination table**  _(§11)_

| Same expense | Federal claim | Ontario claim | Rule |
| --- | --- | --- | --- |
| Child-care receipt | Line 21400 deduction (T778) | CARE refundable credit (ON479-A) | Both allowed — CARE is computed AS A FUNCTION of the federal deduction. This is not double-counting. |
| Attendant care for senior | METC (Line 33099) OR Disability Supports (Line 21500) | Senior Care at Home (ON479-A) | Cannot claim same receipt twice. Choose program based on effective rate (see §9.5). |
| Property tax | n/a federally for principal residence | OEPTC property-tax component + OSHPTG | Both Ontario credits use same payment — allowed (different programs, no federal overlap). |
| Rent paid | n/a federally | OEPTC property-tax component | Allowed. No federal interaction. |
| Long-term care home accommodation | METC eligible (portion attributable to medical care) | OEPTC | Can claim METC on the medical portion and OEPTC on the public-pay accommodation portion if separately allocated by the LTC home. Most LTC homes itemize. |
| Donations | Line 34900 federal | Ontario donation credit on ON428 | Both allowed (this is the normal federal+provincial split). |

## 12. Worked example — Toronto family with 2 kids, $80k income, $24k rent

Sara, age 35, resident of Toronto (not Northern Ontario) all of 2025. Spouse Marco, age 36, resident of Toronto all of 2025. Two children, ages 4 and 8. Sara's Line 23600 = $50,000; Marco's Line 23600 = $30,000; AFNI = $80,000. Rent paid in 2025 = $24,000 ($2,000/month × 12), Toronto, arm's-length landlord, property is subject to municipal tax. Eligible child-care expenses already claimed on federal T778 = $11,000 (for the 4-year-old, $8,000 cap met; plus $3,000 for the 8-year-old). No property tax paid (renters). No long-term care, no reserve energy, not Northern Ontario.

### 12.1 OEPTC

- **OEPTC calculation for Sara and Marco** — Energy component (non-senior, no on-reserve costs): rent paid → eligible for energy component max $282. Property tax component: rent × 20% = $24,000 × 20% = $4,800; capped at $966 (non-senior max). So property tax component = $966. Combined OEPTC before clawback: $282 + $966 = $1,248. AFNI = $80,000; family threshold = $34,661; excess = $45,339. Phase-out = 2% × $45,339 = $906.78. OEPTC after clawback = $1,248 − $906.78 = $341.22.  _(§12.1)_

### 12.2 OSTC

- **OSTC calculation for Sara and Marco** — Base: 2 adults × $360 + 2 qualified children × $360 = $1,440. AFNI = $80,000; family threshold = $34,661; excess = $45,339. Phase-out = 4% × $45,339 = $1,813.56. OSTC after clawback = max(0, $1,440 − $1,813.56) = $0.  _(§12.2)_

### 12.3 NOEC

- **NOEC calculation for Sara and Marco** — Not Northern Ontario — NOEC = $0.  _(§12.3)_

### 12.4 OTB total (annual)

- **OTB total for Sara and Marco** — OEPTC $341.22 + OSTC $0 + NOEC $0 = $341.22 annual OTB. Because annual entitlement is under $360, CRA will pay this as a single July 2026 lump sum (not split into 12 monthly payments).  _(§12.4)_

### 12.5 CARE credit

- **CARE credit calculation for Sara and Marco** — Eligible expenses (from federal T778, already capped): $11,000. Family income = $80,000. Rate: starts at 75% at $20,000 family income, declines linearly to 0% at $150,000. Range: $20,000 to $150,000 = $130,000 span. Family income above $20,000 = $60,000. Reduction fraction: $60,000 / $130,000 ≈ 46.15%. Rate = 75% × (1 − 0.4615) = 75% × 0.5385 ≈ 40.38%. CARE credit = $11,000 × 40.38% ≈ $4,442. (The exact reduction schedule on Schedule ON479-A is published as a stepped table; the skill must use the published table rather than the linear approximation above for the final return. The linear approximation is shown here for reviewer intuition.)  _(§12.5)_

### 12.6 Total Ontario refundable benefit for the household

OTB (annual): $341. CARE: $4,442. Total: ~$4,783. The CARE credit is by far the dominant Ontario benefit for this family. The skill must flag that the federal T778 claim allocation between Sara and Marco affects this — the lower-income spouse (Marco at $30,000) typically must claim federally, but the CARE credit is computed on family income regardless, so the lower-income-spouse rule's only effect is the federal deduction, not the CARE rate.

## 13. Conservative defaults

- **Conservative defaults list** — When inputs are ambiguous, the skill applies these defaults and flags them on the reviewer brief: 1. Default to no claim, not maximum claim. If a rent receipt is unverified or a landlord is not arm's-length, default the OEPTC rent input to $0 and flag. 2. Default to single, not family, threshold when marital status on Dec 31, 2025 is unconfirmed (single thresholds are lower → more conservative entitlement). 3. Default LTC accommodation to retirement-home/ineligible unless the bill is from a designated public/non-profit Ontario long-term care home with itemized accommodation amount. 4. Senior medical receipts default to federal METC unless the effective-rate optimization clearly favors Senior Care at Home (see §9.5). This avoids losing federal METC value when income data is uncertain. 5. Default the Northern Ontario tick-box to "No" unless residency district is confirmed. 6. Default the OTB lump-sum-vs-monthly election to monthly (the CRA default) unless the taxpayer expressly elects June lump-sum. 7. If federal Line 23600 of spouse is missing, refuse to compute OSTC/OEPTC family threshold — do not estimate spouse income. Request the spouse's T1 net income and stop. 8. Phase-out tables: use the published Ontario tables, not linear approximations, for the final return. Linear approximations are for reviewer-brief intuition only. 9. No retroactive amendments for prior years' OTB or CARE within this skill — refer to the federal T1-ADJ workflow. 10. Always state the source year — for 2025 T1 work, the OTB benefit year driven is July 2026 – June 2027, not the 2025 OTB payments (which were driven by the 2024 T1).  _(§13)_

## 14. Sources

Ministry of Finance Ontario — Personal income tax credits page: <https://www.ontario.ca/page/tax-credits-and-benefits>
Ministry of Finance Ontario — Ontario Trillium Benefit: <https://www.ontario.ca/page/ontario-trillium-benefit>
Ministry of Finance Ontario — Ontario Energy and Property Tax Credit: <https://www.ontario.ca/page/ontario-energy-and-property-tax-credit-questions-and-answers>
Ministry of Finance Ontario — Ontario Sales Tax Credit: <https://www.ontario.ca/page/ontario-sales-tax-credit-questions-and-answers>
Ministry of Finance Ontario — Northern Ontario Energy Credit: <https://www.ontario.ca/page/northern-ontario-energy-credit-questions-and-answers>
Ministry of Finance Ontario — Ontario Child Care Tax Credit (CARE): <https://www.ontario.ca/page/ontario-child-care-tax-credit>
Ministry of Finance Ontario — Ontario Senior Care at Home Tax Credit: <https://www.ontario.ca/page/ontario-senior-care-home-tax-credit>
Ministry of Finance Ontario — Ontario Senior Homeowners' Property Tax Grant: <https://www.ontario.ca/page/ontario-senior-homeowners-property-tax-grant>
CRA — Ontario Trillium Benefit (federal administration): <https://www.canada.ca/en/revenue-agency/services/child-family-benefits/ontario-trillium-benefit.html>
CRA — Form ON-BEN (2025): T1 General — Provincial Worksheet, Form ON-BEN
CRA — Form ON479 (2025) and Schedule ON479-A (2025)
CRA — Form ON428 (2025) and Schedule ON428-A (2025)
Taxation Act, 2007 (Ontario), S.O. 2007, c. 11, Schedule A — sections governing OEPTC, OSTC, NOEC, CARE, OSHPTG, Senior Care at Home

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
