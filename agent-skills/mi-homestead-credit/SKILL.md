---
name: mi-homestead-credit
description: "Compute the Michigan Homestead Property Tax Credit (Form MI-1040CR) for a homeowner or renter. The credit is the property tax levied on the homestead (or 23% of rent) above 3.2% of total household resources, times 60% for most claimants (100% for disabled claimants, a sliding 60% to 100% for seniors), reduced 10% for each $1,000 of household resources over $62,500, capped at $1,900 and not available above $71,500 of household resources or a taxable value over $165,400. Figures are the latest published (2025 claims, filed in 2026); 2026 figures are not yet out. Covers total household resources, eligible taxes and rent, seniors, the senior renter alternate credit, partial business use, duplexes and mobile homes. Trigger on \"Michigan homestead credit\", \"MI-1040CR\", \"Michigan property tax credit\", \"total household resources\", \"renter's credit Michigan\"."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/mi-homestead-credit"
  jurisdiction: "US-MI"
  tax_year: "2026"
  last_updated: "2026-11-13"
---

# Michigan homestead property tax credit (MI-1040CR), tax year 2026

> **Source-cited draft.** Built from the 2025 MI-1040CR form and its instructions, the Treasury Homestead Property Tax Credit pages and the 2025 credit information page, read on 2026-11-13. The 2026 MI-1040CR (for claims filed in 2027) was not yet published, so every figure below is the 2025 figure for the 2025-2026 filing cycle. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** A Michigan homeowner or renter can get back part of the property tax on their home. Take the property tax **levied** on the homestead for the year (renters: **23%** of the rent), subtract **3.2%** of total household resources, and multiply by **60%** (most people), **100%** (disabled claimants) or **60% to 100%** (seniors, on a sliding table). Then cut the result by 10% for every $1,000 that household resources exceed **$62,500**. The most anyone gets is **$1,900**. No credit if household resources exceed **$71,500** or, for owners, if the home's taxable value exceeds **$165,400**. These are the 2025 limits; the 2026 limits are not published yet.

## Scope and who this is for

In scope: a natural person (not a trust or company) who owned and occupied, or rented under a lease, a homestead in Michigan, was a Michigan resident for at least six months of the year, and claims the regular credit on Form MI-1040CR.

Out of scope, and where it goes:

| Topic | Skill |
| --- | --- |
| The MI-1040 itself (the credit carries to it) | `mi-income-tax` |
| Veterans and blind people who may use MI-1040CR-2 | Refused here (see refusals) |
| Home heating credit (MI-1040CR-7) | Refused here; a separate credit |
| Farmland preservation credit (MI-1040CR-5) | Refused |
| Principal residence exemption (Form 2368, filed with the assessor) | Mentioned only |

## Ask the client first

1. **Owner or renter, and the address.** Was it the principal residence, and for which months?
2. **Owners:** the property tax statements for the year (summer and winter), the **taxable value** on the statement, and any special assessments. Is the principal residence exemption in place?
3. **Renters:** the lease, the landlord's name and address, monthly rent, months rented; is any service charge paid instead of property tax (subsidized or tax-exempt housing)?
4. **Every source of household income for both spouses**, taxable or not: wages, business profit, Social Security (gross), pensions and IRAs (gross), unemployment, child support, alimony, gifts over $300, and the rest of the list below.
5. **Medical insurance and HMO premiums** the household paid.
6. **Age 65 or older, or deaf, blind, paraplegic, hemiplegic, quadriplegic or totally and permanently disabled?** Veteran or surviving spouse of a veteran?
7. **Business or rental use of the home**, a duplex, a tenant renting a room, a mobile home on a rented lot?
8. **FIP or other MDHHS benefits** received in the year?

## The method, step by step

### Rates, bands and thresholds

| Item | Amount, 2025-2026 filing cycle | Source |
| --- | --- | --- |
| Maximum credit | $1,900 | [2025 Homestead Property Tax Credit Information](https://www.michigan.gov/taxes/iit/tax-guidance/credits-exemptions/hptc/tax-year-credit-information/2025) |
| Total household resources limit (no credit above it) | $71,500 | [2025 Homestead Property Tax Credit Information](https://www.michigan.gov/taxes/iit/tax-guidance/credits-exemptions/hptc/tax-year-credit-information/2025) |
| Phase-out begins when total household resources exceed | $62,500 | [2025 Homestead Property Tax Credit Information](https://www.michigan.gov/taxes/iit/tax-guidance/credits-exemptions/hptc/tax-year-credit-information/2025) |
| Maximum taxable value of an owned homestead (excluding unoccupied farmland classified agricultural) | $165,400 | [2025 Homestead Property Tax Credit Information](https://www.michigan.gov/taxes/iit/tax-guidance/credits-exemptions/hptc/tax-year-credit-information/2025) |
| Share of total household resources not refundable, general claimants | 3.2% | [2025 MI-1040CR instructions, line 34 and Table 2](https://www.michigan.gov/taxes/-/media/Project/Websites/taxes/Forms/IIT/TY2025/MI-1040CR-Instr.pdf) |
| Same, seniors and disabled claimants with household resources of $3,000 or less / $3,001 to $4,000 / $4,001 to $5,000 / $5,001 to $6,000 / over $6,000 | 0% / 1% / 2% / 3% / 3.2% | [2025 MI-1040CR instructions, Table 2](https://www.michigan.gov/taxes/-/media/Project/Websites/taxes/Forms/IIT/TY2025/MI-1040CR-Instr.pdf) |
| Share of rent treated as property tax | 23% | [2025 MI-1040CR instructions, "Rent Eligible for Credit"](https://www.michigan.gov/taxes/-/media/Project/Websites/taxes/Forms/IIT/TY2025/MI-1040CR-Instr.pdf) |
| Housing with a service charge instead of property tax | 10% of gross rent | [2025 MI-1040CR instructions, "Rent Eligible for Credit"](https://www.michigan.gov/taxes/-/media/Project/Websites/taxes/Forms/IIT/TY2025/MI-1040CR-Instr.pdf) |
| Allowance, all other claimants (Section C) | 60% | [2025 MI-1040CR, line 41](https://www.michigan.gov/taxes/-/media/Project/Websites/taxes/Forms/IIT/TY2025/MI-1040CR.pdf) |
| Allowance, disabled claimants (Section B) | 100% | [2025 MI-1040CR, line 39](https://www.michigan.gov/taxes/-/media/Project/Websites/taxes/Forms/IIT/TY2025/MI-1040CR.pdf) |
| Allowance, seniors (Table A): household resources $21,000 or less | 100%, falling 4 points for each $1,000 to 64% at $29,001 to $30,000 | [2025 MI-1040CR instructions, Table A](https://www.michigan.gov/taxes/-/media/Project/Websites/taxes/Forms/IIT/TY2025/MI-1040CR-Instr.pdf) |
| Allowance, seniors with household resources $30,001 to $71,500 | 60% | [2025 MI-1040CR instructions, Table A](https://www.michigan.gov/taxes/-/media/Project/Websites/taxes/Forms/IIT/TY2025/MI-1040CR-Instr.pdf) |
| Phase-out (Table B): reduction for each $1,000 or part over $62,500 | 10 points (90% at $62,501 to $63,500 down to 0% at $71,501) | [2025 MI-1040CR instructions, Table B](https://www.michigan.gov/taxes/-/media/Project/Websites/taxes/Forms/IIT/TY2025/MI-1040CR-Instr.pdf) |
| Senior renter alternate credit: rent above this share of household resources | 40% | [2025 MI-1040CR instructions, Worksheet 5](https://www.michigan.gov/taxes/-/media/Project/Websites/taxes/Forms/IIT/TY2025/MI-1040CR-Instr.pdf) |
| First gifts, and first gambling, lottery and prize winnings, left out of household resources | $300 each | [2025 MI-1040CR instructions](https://www.michigan.gov/taxes/-/media/Project/Websites/taxes/Forms/IIT/TY2025/MI-1040CR-Instr.pdf) |

### Gate 1: who can claim

All of: a natural person; a Michigan homestead (owned or rented); a Michigan resident for at least six months of the year; total household resources within the limit; an owner's taxable value within the limit (the cap does not apply to renters); owning and occupying the homestead, or occupying it under a lease. Source: [Homestead Property Tax Credit](https://www.michigan.gov/taxes/iit/tax-guidance/credits-exemptions/hptc).

### Step 1: total household resources (line 33)

Total household resources are the total income, taxable and nontaxable, of both spouses or of a single person keeping a household: **AGI, excluding net business and farm losses, net rent and royalty losses and any net operating loss carryover, plus all income exempt or excluded from AGI**, less medical insurance and HMO premiums paid for the household (line 31). Source: [2025 MI-1040CR instructions](https://www.michigan.gov/taxes/-/media/Project/Websites/taxes/Forms/IIT/TY2025/MI-1040CR-Instr.pdf).

Included (beyond what the form lists): gain on the sale of the home even if federally exempt; damages for personal injury or sickness; an inheritance (except from a spouse); life insurance proceeds (except on a spouse); employer death benefits; a minister's housing allowance; forgiven debt even if excluded from AGI; reimbursements from dependent care and medical spending accounts; scholarships, stipends and grants (except government payments made directly to third parties); forgiven PPP loans net of the related unclaimed expenses. Social Security, pensions and IRA distributions count in full, not only the federally taxable part.

Not included: NOL deductions; foster grandparent and senior companion payments; energy assistance grants; government payments made directly to third parties (unless taken from the claimant's own benefit, such as MDHHS paying rent to the landlord); government money to repair the home; food assistance; state and city income tax refunds and homestead credits; chore service payments; the first $300 of gambling, bingo, lottery, awards or prizes; the first $300 of gifts of cash or merchandise or expenses paid on the claimant's behalf by others; Medicare premiums deducted from Social Security or Railroad Retirement; employer-paid life, health and accident premiums; loan proceeds; an inheritance or life insurance from a spouse; long-term care policy payments made to a care facility; most Step Forward Michigan payments; compensation for wrongful imprisonment.

### Step 2: the tax that counts (line 10, or 23% of rent)

**Owners:** ad valorem property taxes **levied** on the homestead for the year (plus collection fees up to 1% of the taxes), whenever paid; add taxes from a corrected or supplemental bill issued in the year; deduct any refund received in the year from a corrected bill of an earlier year. Do not include: adjacent property that is occupied or classed as commercial, industrial, residential or timber-cutover; delinquent taxes of earlier years; penalty and interest; water and sewer bills; cottages and second homes; association dues; most special assessments (only those levied across the whole taxing unit, or for police, fire or advanced life support township-wide, at a uniform millage on taxable value, count). Business use of the home: only the living area's tax counts (attach federal Form 8829). Owner-occupied duplex with equal units: 50% of the tax on both units, after removing school operating taxes. Owner renting a room or unit: the lower of two figures, including the tax minus 23% of rent collected.

**Renters:** 23% of rent paid under a lease or rental contract for the homestead. Service-charge housing: 10% of gross rent. Special housing facilities: rent only, not other services. Rent on land under a mobile home also qualifies at 23%.

Source for step 2: [2025 MI-1040CR instructions](https://www.michigan.gov/taxes/-/media/Project/Websites/taxes/Forms/IIT/TY2025/MI-1040CR-Instr.pdf).

### Step 3: the computation (lines 34 to 44)

1. Line 34: total household resources times 3.2% (or the Table 2 share for low-income seniors and disabled claimants).
2. Line 35: tax that counts minus line 34. If zero or less, no credit.
3. Allowance: senior (Section A) line 35 times the Table A share; disabled (Section B) line 35 in full; all others (Section C) line 35 times 60%. Maximum $1,900.
4. FIP or MDHHS benefits: prorate by (household resources minus those benefits) divided by household resources (Worksheet 4).
5. Line 43: Table B share (100% up to $62,500 of household resources, down 10 points per $1,000 or part).
6. Line 44: the credit = allowance times the Table B share. It carries to MI-1040 line 26, or is claimed alone on the MI-1040CR.
7. **Seniors who rent:** Worksheet 5 alternate: rent paid minus 40% of household resources. The credit is the larger of the line 42 amount (after Table B) and the alternate, maximum $1,900.

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Taxable value over the cap (owner) | No credit |
| Household resources over $71,500 | No credit |
| Landlord pays no property tax (fully exempt) | No credit on that rent |
| Moved during the year | Prorate the tax and rent of each homestead by the time lived there |
| Married, living apart in separate homesteads | Each claims on their own share; flag for review |
| Divorced or separated during the year | Each claims for the time in each homestead; flag |
| Home used partly for business | Exclude the business portion of the tax |
| Duplex, owner in one equal unit | 50% after school operating taxes |
| Mobile home on a rented lot | 23% of lot rent, plus any property tax or specific tax on the home |
| Nursing home or adult foster care resident | Share of the facility's tax or rent; refused here |
| Delinquent prior-year taxes paid this year | Not eligible |
| Senior renter with high rent and low income | Run the Worksheet 5 alternate |

### Defaults when a fact is missing

| Missing fact | Default, and flag it |
| --- | --- |
| Taxable value | No claim until the statement is seen |
| Untaxed income (gross Social Security, child support) | Ask: a claim built on AGI alone overstates the credit |
| Medical premiums | Zero; ask for Medicare and insurance statements |
| Whether special assessments qualify | Exclude them |

### Red flags to raise with the client

| Flag | Why it matters |
| --- | --- |
| Household resources near $62,500 or $71,500 | Each $1,000 changes the credit by 10 points |
| Household resources that look too low to live on | Treasury asks for proof of other resources |
| Rent paid to a relative | The lease must be real; may be challenged |
| Claim built from federal AGI only | Most adjustment letters come from missing nontaxable income |

## Worked cases

**Case 1, homeowner under 65.** Household resources $40,000; property tax levied on the homestead $3,000; taxable value under the cap. Line 34: $40,000 x 3.2% = $1,280. Line 35: $3,000 - $1,280 = $1,720. Section C: $1,720 x 60% = $1,032. Table B: 100% (resources under $62,500). Credit $1,032.

```oa-check
name: MI homestead credit, homeowner, general claimant
inputs:
  thr: 40000
  property_tax: 3000
steps:
  - line_34: thr * 0.032
  - line_35: max(property_tax - line_34, 0)
  - allowance: min(line_35 * 0.6, 1900)
  - table_b: clamp(1 - ceil(max(thr - 62500, 0) / 1000) * 0.1, 0, 1)
  - credit: allowance * table_b
expected:
  line_34: 1280
  line_35: 1720
  allowance: 1032
  credit: 1032
```

**Case 2, a decision: regular or alternate credit for a senior renter.** A renter aged 70 has household resources of $15,000 and pays $9,000 of rent. Regular credit: 23% x $9,000 = $2,070; minus 3.2% x $15,000 = $480, leaves $1,590; Table A share 100% (resources $21,000 or less): $1,590. Alternate (Worksheet 5): $9,000 - 40% x $15,000 = $3,000. Take the larger, capped at $1,900: the alternate gives $1,900, $310 more than the regular credit.

```oa-check
name: MI homestead credit, senior renter, regular against alternate
inputs:
  thr: 15000
  rent: 9000
  table_a_share: 1.0
steps:
  - regular: max(rent * 0.23 - thr * 0.032, 0) * table_a_share
  - alternate: max(rent - thr * 0.4, 0)
  - credit: min(max(regular, alternate), 1900)
  - gain_from_alternate: credit - min(regular, 1900)
expected:
  regular: 1590
  alternate: 3000
  credit: 1900
  gain_from_alternate: 310
```

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| MI-CR-R-01 | Veteran, blind person or veteran's surviving spouse who may claim on MI-1040CR-2 | Refuse: different form and rules |
| MI-CR-R-02 | Farmland preservation credit (MI-1040CR-5) | Refuse |
| MI-CR-R-03 | Home heating credit (MI-1040CR-7) | Refuse here; a separate credit with its own tables |
| MI-CR-R-04 | Part-year resident (prorated claim, annualized resources) | Refuse |
| MI-CR-R-05 | Amended claim | Refer; claims can be filed up to four years after the year |
| MI-CR-R-06 | Homestead held in a trust or by an LLC | Refuse: only natural persons claim |
| MI-CR-R-07 | Nursing home, adult foster care or special housing resident | Refer |
| MI-CR-R-08 | Claim for a deceased taxpayer | Refer: annualization and representative rules |
| MI-CR-R-09 | Home owned with someone outside the household | Refer: prorated shares |
| MI-CR-R-10 | Foreclosure, short sale or debt forgiveness in the year | Refer: forgiven debt counts in household resources |
| MI-CR-R-11 | Fully tax-exempt landlord | Refuse: no eligible rent |
| MI-CR-R-12 | Homestead outside Michigan | Refuse |

## Filing and payment

File the MI-1040CR with the MI-1040 (due 15 April 2027 for the 2026 claim) or on its own; the credit is paid as a refund or reduces the MI-1040 balance. A claim may be filed up to four years after the year it could first be claimed. File through Michigan Treasury eServices or approved software. Keep the tax statements or lease and rent receipts. Source: [Homestead Property Tax Credit](https://www.michigan.gov/taxes/iit/tax-guidance/credits-exemptions/hptc).

## Completion checklist

- Resident at least six months; natural person; Michigan homestead.
- Taxable value within the cap (owners).
- Total household resources include every nontaxable item and both spouses.
- Taxes are those levied for the year, without delinquent taxes, penalties or most special assessments.
- Business share, duplex and room-rental adjustments made.
- Right allowance section (A, B or C) and Table B share applied; $1,900 cap.
- Senior renters tested on Worksheet 5.
- Principal residence exemption confirmed with the assessor.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Treasury, 2025 Homestead Property Tax Credit Information. Read for $165,400, $71,500, $62,500 and $1,900. | https://www.michigan.gov/taxes/iit/tax-guidance/credits-exemptions/hptc/tax-year-credit-information/2025 | 2026-11-13 |
| 2025 MI-1040CR instructions. Read for total household resources, eligible taxes and rent (23%, 10%), Tables 2, A and B, Worksheets 4 and 5 (40%), the $300 exclusions and the four-year limit. | https://www.michigan.gov/taxes/-/media/Project/Websites/taxes/Forms/IIT/TY2025/MI-1040CR-Instr.pdf | 2026-11-13 |
| 2025 MI-1040CR form. Read for lines 33 to 44, Section B (100%) and Section C (60%). | https://www.michigan.gov/taxes/-/media/Project/Websites/taxes/Forms/IIT/TY2025/MI-1040CR.pdf | 2026-11-13 |
| Treasury, Homestead Property Tax Credit. Read for who qualifies (natural person, six months' residency, taxable value cap, renters) and the four-year filing window. | https://www.michigan.gov/taxes/iit/tax-guidance/credits-exemptions/hptc | 2026-11-13 |

Not yet confirmed: every 2026 figure (the 2026 MI-1040CR and the 2026 credit information page were not published; Treasury's 2026 page returned "not found"), so the 2025 limits apply to the 2025-2026 filing cycle only; the mobile home specific tax amount (the old file said $3 a month; not re-read); MCL 206.501 to 206.532 themselves (legislature.mi.gov returned errors).

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `mi-homestead-credit` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/mi-homestead-credit. If neither is available, confirm every figure against the official source pages cited above before relying on it.
