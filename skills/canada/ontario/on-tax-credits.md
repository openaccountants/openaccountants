---
name: on-tax-credits
description: Ontario personal refundable credits and benefit applications, separating 2026 tax-year rules from the 2026 Ontario Trillium Benefit paid July 2026-June 2027 on 2025 income. Covers OEPTC, OSTC, NOEC, CARE, senior homeowners grant, seniors care at home, coordination and actual ON479/ON-BEN fields. Load ca-fed-t1-return and on-individual-return for the federal return and Ontario non-refundable tax calculation.
jurisdiction: CA
tax_year: 2026
tax_year_notes: "2026 income-year law; latest forms are 2025-2026 filing cycle. 2026 OTB/grant uses 2025 income; 2027 benefit amounts based on 2026 income are not assumed."
last_updated: 2026-11-14
version: "2.0"
category: international
type: computation
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
---

# Ontario credits and Trillium Benefit: method v2.0

## Scope

Prepare an Ontario credit worksheet, supporting schedules and benefit applications for an individual. Load `ca-fed-t1-return` for federal net/taxable income, T778, medical-expense eligibility and filing; load `on-individual-return` for ON428 brackets, basic personal/age/spouse/disability/donation credits, surtax, LIFT and Health Premium. These are different jobs, not interchangeable credits. No return is filed without the taxpayer's approval.

**Keep three dates separate.** Tax year 2026 means income earned in 2026. The latest published forms here are the **2025 return / 2026 filing cycle**. The **2026 OTB** and 2026 senior homeowners grant use **2025** income/housing costs: the OTB benefit year is July 2026-June 2027. A 2026 return will ordinarily feed July 2027-June 2028, but do not use the indexed 2026 benefit figures as unpublished 2027 figures. Continuing statutory CARE and seniors-care rules below apply under the current Act; final 2026 form layout must be checked when published. [Taxation Act, 2007](https://www.ontario.ca/laws/statute/07t11), [CRA current Ontario guide](https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/ontario/5006-pc.html).

## Ask the client first

- Obtain both spouses' complete federal returns, line 23600 net income, line 26000 taxable income, line 21400 child-care deduction and line 23500 social benefits repayment; these income measures are not interchangeable.
- Confirm residence on December 31 of the base year and on the first of each payment month, moves, dates of birth, marriage/common-law/separation, children and custody arrangements, and incarceration. Do not default an unknown spouse to single or a missing dependant to zero in a final claim.
- Obtain principal-residence addresses, postal codes, months occupied, rent receipts and payments made by others, landlord identity and whether the dwelling was subject to municipal/school property tax. For owners obtain actual property tax paid, not unpaid/deferred bills or an assumed condo-fee percentage.
- Identify designated student residence, public/non-profit versus fully property-taxed private care accommodation, itemised room/board, reserve home energy, mobile/land-lease home and ownership. Do not reject a related landlord without testing actual eligible rent.
- For NOEC confirm Algoma, Cochrane, Kenora, Manitoulin, Nipissing, Parry Sound, Rainy River, Sudbury including Greater Sudbury, Thunder Bay or Timiskaming, at the relevant dates.
- For CARE obtain each child's T778 eligibility, receipts/provider details, lower-income-spouse and earned-income restriction outputs, all supporting persons and their adjusted incomes. A raw receipt total is not the credit base.
- For senior homeowners grant confirm age 64 or over on December 31, 2025 for the 2026 grant, ownership/occupation and tax paid. For seniors care obtain ON428 line 58769, ages of both spouses, survivor facts, family income and all medical/disability-support reimbursements.
- Confirm bankruptcy/death and any requested late correction or delayed-OTB election. Keep the CRA benefit notice and any debt offsets separate from the T1 refund.

## The method, step by step

### 1. Route each credit to the correct return or benefit

| Job | Calculation and destination | Applicable period | Official source |
|---|---|---|---|
| OEPTC | Energy plus property-tax component, income-tested; apply ON-BEN 61020 | 2026 benefit / 2025 base | https://www.canada.ca/en/revenue-agency/services/child-family-benefits/provincial-territorial-programs/ontario-energy-property-tax-credit-questions-answers.html |
| OSTC | Automatic from filed return, up to $378 per adult/qualified child; not an ON-BEN application | July 2026-June 2027 | https://www.canada.ca/en/revenue-agency/services/child-family-benefits/provincial-territorial-programs/province-ontario.html |
| NOEC | Up to $189 single without children or $290 family, a household amount; ON-BEN 61040 | 2026 benefit / 2025 base | https://www.canada.ca/en/revenue-agency/services/child-family-benefits/provincial-territorial-programs/northern-ontario-energy-credit-questions-answers.html |
| CARE | Eligible federal child-care deduction times actual stepped statutory rate; ON479-A to ON479 63050 | Current continuing law; latest form 2025 | https://www.ontario.ca/laws/statute/07t11 ; https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-tca/5006-tca-25e.pdf |
| Senior homeowners grant | Lesser of eligible property tax and $500 before income reduction; ON-BEN 61070, separate payment | 2026 grant / 2025 base | https://www.canada.ca/en/revenue-agency/services/child-family-benefits/provincial-territorial-programs/ontario-senior-homeowners-property-tax-grant-oshptg-questions-answers.html |
| Seniors care at home | ON428 net allowable medical amount, 25%, maximum $1,500 before family-income reduction; ON479 63095 | Continuing law; latest form 2025 | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-tc/5006-tc-25e.pdf |
| ON428 and LIFT | Non-refundable tax calculation, not an OTB component; load on-individual-return | 2026 income | https://www.ontario.ca/laws/statute/07t11 |

The law at section 103.3 was amended in April 2026: the old **$360** single-payment cutoff belongs to earlier base years. For the 2025 and later base years the current cutoff is **$500**, consistent with the current CRA Q&A. Do not follow an old PDF footer that still says $360. [Act 103.3(3), (3.0.1)](https://www.ontario.ca/laws/statute/07t11), [OTB Q&A](https://www.canada.ca/en/revenue-agency/services/child-family-benefits/provincial-territorial-programs/ontario-trillium-benefit-questions-answers.html).

### 2. Establish eligibility and select the benefit worksheet

OEPTC and NOEC normally require base-year December 31 residence, eligible housing/energy payments, monthly residence and the age-18/spouse/parent route. OSTC has its own **age-19**/spouse/parent rule and is automatically assessed from the return; it does not require an OEPTC application or housing costs. A child under 19 can count for OSTC, but the OEPTC custody worksheets distinguish children under 18. Do not call these the same as the federal CCB under-18 definition. [CRA Ontario guide, benefit eligibility](https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/ontario/5006-pc.html), [Act 103.4-103.6](https://www.ontario.ca/laws/statute/07t11).

The OEPTC worksheet choice uses marital status on December 31, 2025 and the children's situation at the beginning of each payment month. Both spouses under 64 use the non-senior couple worksheet; a spouse aged 64 or older at that date switches the couple to the senior worksheet. Use single/no-child, sole-care or shared-care variants as appropriate. A changed child situation may require monthly calculations on different sheets; aggregate monthly results, not an assumed unchanged annual result. [2026 worksheet index](https://www.canada.ca/en/revenue-agency/services/child-family-benefits/provincial-territorial-programs/ontario-energy-property-tax-credit-oeptc-calculation-sheets/2026-ontario-energy-property-tax-credit-calculation-sheets.html).

Only one spouse applies for the couple's OEPTC, NOEC and senior homeowners grant, using the same applicant; where only one is 64 or older at the base-year end, that spouse applies. OSTC normally goes to the spouse whose return is assessed first, subject to the senior-recipient rules. Involuntary separation for medical reasons can permit separate claims; use ON-BEN **61080** and Part C, do not assume a family claim or a marital breakdown. [ON-BEN](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-tg/5006-tg-25e.pdf), [seniors OSTC Q&A](https://www.canada.ca/en/revenue-agency/services/child-family-benefits/provincial-territorial-programs/province-ontario/ostc-seniors-income-threshold-qa.html).

### 3. Compute OEPTC using occupancy cost, not the maximum alone

For the ordinary 2026 non-senior calculation let occupancy cost be **20% of eligible rent + actual eligible property tax + $25 for a designated student residence**. Energy is the lesser of **$290** and occupancy cost minus the student-residence $25, plus **20% of qualifying public/non-profit LTC accommodation** and reserve home-energy payments. Property credit is the lesser of occupancy cost and **$73 + min(10% of occupancy cost, $944)**. The combined maximum is **$1,307**, not a guarantee to every renter. Floor negative entitlement at zero. [Non-senior couple sheet](https://www.canada.ca/en/revenue-agency/services/child-family-benefits/provincial-territorial-programs/ontario-energy-property-tax-credit-oeptc-calculation-sheets/2026-ontario-energy-property-tax-credit-calculation-sheets/2026-ontario-energy-property-tax-credit-calculation-sheet-married-common-laws-no-children.html), [OEPTC Q&A](https://www.canada.ca/en/revenue-agency/services/child-family-benefits/provincial-territorial-programs/ontario-energy-property-tax-credit-questions-answers.html).

| 2026 OEPTC condition | Figure or rule | Official source |
|---|---|---|
| Non-senior energy / property maxima | $290 / $1,017; property is capped occupancy calculation above | https://www.canada.ca/en/revenue-agency/services/child-family-benefits/provincial-territorial-programs/ontario-energy-property-tax-credit-questions-answers.html |
| Senior energy / property maxima | $290 / $1,198; senior property formula uses $617 + min(10% of occupancy cost, $581), limited to occupancy cost | https://www.canada.ca/en/revenue-agency/services/child-family-benefits/provincial-territorial-programs/ontario-energy-property-tax-credit-questions-answers.html ; https://www.canada.ca/en/revenue-agency/services/child-family-benefits/provincial-territorial-programs/ontario-energy-property-tax-credit-oeptc-calculation-sheets/2026-ontario-energy-property-tax-credit-calculation-sheets/2026-ontario-energy-property-tax-credit-calculation-sheet-single-senior-no-children.html |
| Non-senior single with no children income reduction | 2% above adjusted net income $29,047 | https://www.canada.ca/en/revenue-agency/services/child-family-benefits/provincial-territorial-programs/ontario-energy-property-tax-credit-oeptc-calculation-sheets/2026-ontario-energy-property-tax-credit-calculation-sheets/2026-ontario-energy-property-tax-credit-calculation-sheet-single-individuals-no-children.html |
| Non-senior couple or sole-care parent income reduction | 2% above adjusted family net income $36,309 | https://www.canada.ca/en/revenue-agency/services/child-family-benefits/provincial-territorial-programs/ontario-energy-property-tax-credit-oeptc-calculation-sheets/2026-ontario-energy-property-tax-credit-calculation-sheets/2026-ontario-energy-property-tax-credit-calculation-sheet-married-common-laws-no-children.html ; https://www.canada.ca/en/revenue-agency/services/child-family-benefits/provincial-territorial-programs/ontario-energy-property-tax-credit-oeptc-calculation-sheets/2026-ontario-energy-property-tax-credit-calculation-sheets/2026-ontario-energy-property-tax-credit-calculation-sheet-single-individuals-sole-care-one-child.html |
| Senior single with no children income reduction | 2% above adjusted net income $36,309 | https://www.canada.ca/en/revenue-agency/services/child-family-benefits/provincial-territorial-programs/ontario-energy-property-tax-credit-oeptc-calculation-sheets/2026-ontario-energy-property-tax-credit-calculation-sheets/2026-ontario-energy-property-tax-credit-calculation-sheet-single-senior-no-children.html |
| Senior shared-care worksheet thresholds | Average the single and family components at $36,309 / $43,571; do not take a blanket half of one result | https://www.canada.ca/en/revenue-agency/services/child-family-benefits/provincial-territorial-programs/ontario-energy-property-tax-credit-oeptc-calculation-sheets/2026-ontario-energy-property-tax-credit-calculation-sheets/2026-ontario-energy-property-tax-credit-calculation-sheet-single-seniors-share-care-all-children.html |
| Non-senior shared-care thresholds | Half of each applicable single/family component at $29,047 / $36,309 | https://www.canada.ca/en/revenue-agency/services/child-family-benefits/provincial-territorial-programs/ontario-energy-property-tax-credit-oeptc-calculation-sheets/2026-ontario-energy-property-tax-credit-calculation-sheets/2026-ontario-energy-property-tax-credit-calculation-sheet-single-individuals-share-care-children.html |

For senior couples and senior sole-care parents, obtain the exact selected worksheet from the index rather than borrowing the single threshold. Where the homeowner grant applies, complete **Step 5**: prevent the property-related grant plus credit from exceeding occupancy cost, after allowing the energy component. Both programmes may apply, but their maxima cannot simply be added. [Senior worksheet Step 5](https://www.canada.ca/en/revenue-agency/services/child-family-benefits/provincial-territorial-programs/ontario-energy-property-tax-credit-oeptc-calculation-sheets/2026-ontario-energy-property-tax-credit-calculation-sheets/2026-ontario-energy-property-tax-credit-calculation-sheet-single-senior-no-children.html), [Act 103.10-103.11](https://www.ontario.ca/laws/statute/07t11).

#### Housing and accommodation boundaries

- Eligible rent depends on a principal residence subject to municipal/school property tax, not a universal arm's-length-landlord test. Board, services and care are not automatically all rent. A private LTC/retirement-type institution that pays full property taxes can have eligible rent; a public/non-profit home uses the accommodation-cost box. Where room/board is not itemised the current guide permits up to 75% under the applicable route, not both routes on the same bill.
- Designated university/college/private-school residence is flagged at 61140 and receives the special $25 treatment; do not enter that residence's fees as ordinary rent. Other qualifying housing during the year can still be reported separately.
- Co-tenants claim only eligible rent actually paid by or for them; spouses use the couple rules. Document the allocation and exclude services or someone else's duplicate claim. Property-tax deferral counts only when tax was actually paid. Follow the special mobile/land-lease/farm-home-one-acre rules instead of claiming all land or a guessed condo-fee allocation.
- Reserve electricity/heating costs and qualifying public/non-profit LTC accommodation affect the energy computation; do not add the full LTC bill as property tax. Keep receipts, residence months, suppliers and any subsidised-housing tax-status confirmation. [OEPTC Q&A questions 9-15](https://www.canada.ca/en/revenue-agency/services/child-family-benefits/provincial-territorial-programs/ontario-energy-property-tax-credit-questions-answers.html), [CRA housing instructions](https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/ontario/5006-pc.html).

### 4. Compute OSTC and NOEC independently

For 2026 OSTC start with **$378 per adult and per qualified child**, then normally reduce by **4%** of AFNI above **$29,047 single/no-child** or **$36,309 family**. For a qualifying senior family in this benefit year, the special threshold is **$37,273**, not the ordinary family threshold; use the senior recipient rules. Shared custody requires the appropriate portion for each parent, not two full child entitlements. [Ontario programmes](https://www.canada.ca/en/revenue-agency/services/child-family-benefits/provincial-territorial-programs/province-ontario.html), [senior threshold](https://www.canada.ca/en/revenue-agency/services/child-family-benefits/provincial-territorial-programs/province-ontario/ostc-seniors-income-threshold-qa.html).

For NOEC start with **$189 single/no-child** or **$290 family**, reduce by **1%** above **$50,833** or **$65,356** respectively and floor at zero. The family maximum is one household amount, not per child. Require Northern Ontario residence and qualifying housing/energy costs; do not award it solely for an address. Apply the monthly, custody, incarceration and involuntary-separation rules in its Q&A. [NOEC questions 2-7](https://www.canada.ca/en/revenue-agency/services/child-family-benefits/provincial-territorial-programs/northern-ontario-energy-credit-questions-answers.html).

AFNI is the statutory adjusted income measure, not CARE's family adjusted income below. Use the applicable CRA adjustment for UCCB/RDSP income and repayments rather than simply summing taxable income. Confirm the base-year returns and all income adjustments. [Act 103.4](https://www.ontario.ca/laws/statute/07t11), [CRA worksheets](https://www.canada.ca/en/revenue-agency/services/child-family-benefits/provincial-territorial-programs/ontario-energy-property-tax-credit-oeptc-calculation-sheets/2026-ontario-energy-property-tax-credit-calculation-sheets.html).

### 5. OTB payment and application fields

Complete the applicable ON-BEN application boxes: **61020 OEPTC**, **61040 NOEC**, **61070 grant**; then housing boxes **61100 rent**, **61120 property tax**, **61140 student residence**, **61210 reserve energy**, **61230 public/non-profit LTC accommodation**. Complete Parts A and B, address/month/payment/supplier information, and Part C if 61080 medical separation applies. OSTC needs no application. ON-BEN is an application, not an amount added to T1 line 47900. [Latest ON-BEN, 2025 return](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-tg/5006-tg-25e.pdf).

Annual OTB is the sum of the eligible monthly components. Normally CRA pays on the **10th**, or preceding working day for a weekend/holiday. **$500 or less** is paid in the first payment month, usually July; **$2 or less** is not paid; above $2 but below $10 is topped to $10. The explicit end-of-benefit-year election (**61060**) postpones an entitlement over $500 to June 2027 for the 2026 benefit. Make it only on the initial 2025 return, by December 31, 2026, not an amended return. Bankruptcy, departure, death or qualifying incarceration can revoke it. [Act 103.3](https://www.ontario.ca/laws/statute/07t11), [OTB questions 9-14](https://www.canada.ca/en/revenue-agency/services/child-family-benefits/provincial-territorial-programs/ontario-trillium-benefit-questions-answers.html).

CRA calculates the entitlement and sends a benefit notice separately from the tax refund. Keep direct-deposit/address details current and report changed circumstances promptly; do not assume a generic 30-day deadline applies to every change or recompute a base-year marital status merely from a later marriage. Debt offsets can reduce cash paid. OTB is non-taxable and bears no interest on over/underpayments. For omitted prior-year applications request an adjustment with the correct year's ON-BEN through My Account/T1-ADJ, not a second original return; the Q&A generally allows the prior ten calendar years. [OTB questions 18-22](https://www.canada.ca/en/revenue-agency/services/child-family-benefits/provincial-territorial-programs/ontario-trillium-benefit-questions-answers.html).

### 6. CARE: federal expense base, different family-income measure

Complete federal **T778 / line 21400** first. The normal federal annual limits are $8,000 under 7, $5,000 for other eligible children and $11,000 where the disability conditions apply, subject to the earned-income/lower-income-spouse and supporting-person rules; consume the actual allowed deduction, not the theoretical per-child caps or gross invoices. The eligible child must be under 16 at some time in the year unless the impairment/dependency exception applies. [ON479-A](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-tca/5006-tca-25e.pdf); federal deduction eligibility remains in `ca-fed-t1-return` and [ITA63](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-63.html).

Under **Taxation Act 103.0.2**, family adjusted income adds back the child-care deduction and social-benefits repayment and applies the statutory split-income adjustment. On the latest form, add **line 23600 + line 21400 + line 23500** for the claimant/supporting persons, floor the individual adjusted amount at zero, and follow the multiple-supporting-person rules on page 1. It is not simply both spouses' line 23600. [Act 103.0.2(1)](https://www.ontario.ca/laws/statute/07t11), [ON479-A lines 1-5](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-tca/5006-tca-25e.pdf).

The statutory equivalent is 75% up to $20,000; above $20,000 to $40,000 subtract 2 percentage points for each $2,500 **or part thereof**; above $40,000 to $60,000 start at 59% and subtract 2 points for each $5,000 or part; above $60,000 start at 51% and subtract 2 points for each $3,600 or part, floored at zero. The final 1% band includes exactly $150,000. [Act 103.0.2, tax credit rate definition](https://www.ontario.ca/laws/statute/07t11). The following is the actual interval table printed on page 2 of the latest ON479-A, rather than a linear approximation.

| Family adjusted income | CARE rate | Official source |
|---|---|---|
| $0 to $20,000 | 75% | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-tca/5006-tca-25e.pdf |
| More than $20,000 to $22,500 | 73% | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-tca/5006-tca-25e.pdf |
| More than $22,500 to $25,000 | 71% | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-tca/5006-tca-25e.pdf |
| More than $25,000 to $27,500 | 69% | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-tca/5006-tca-25e.pdf |
| More than $27,500 to $30,000 | 67% | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-tca/5006-tca-25e.pdf |
| More than $30,000 to $32,500 | 65% | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-tca/5006-tca-25e.pdf |
| More than $32,500 to $35,000 | 63% | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-tca/5006-tca-25e.pdf |
| More than $35,000 to $37,500 | 61% | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-tca/5006-tca-25e.pdf |
| More than $37,500 to $40,000 | 59% | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-tca/5006-tca-25e.pdf |
| More than $40,000 to $45,000 | 57% | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-tca/5006-tca-25e.pdf |
| More than $45,000 to $50,000 | 55% | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-tca/5006-tca-25e.pdf |
| More than $50,000 to $55,000 | 53% | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-tca/5006-tca-25e.pdf |
| More than $55,000 to $60,000 | 51% | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-tca/5006-tca-25e.pdf |
| More than $60,000 to $63,600 | 49% | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-tca/5006-tca-25e.pdf |
| More than $63,600 to $67,200 | 47% | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-tca/5006-tca-25e.pdf |
| More than $67,200 to $70,800 | 45% | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-tca/5006-tca-25e.pdf |
| More than $70,800 to $74,400 | 43% | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-tca/5006-tca-25e.pdf |
| More than $74,400 to $78,000 | 41% | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-tca/5006-tca-25e.pdf |
| More than $78,000 to $81,600 | 39% | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-tca/5006-tca-25e.pdf |
| More than $81,600 to $85,200 | 37% | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-tca/5006-tca-25e.pdf |
| More than $85,200 to $88,800 | 35% | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-tca/5006-tca-25e.pdf |
| More than $88,800 to $92,400 | 33% | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-tca/5006-tca-25e.pdf |
| More than $92,400 to $96,000 | 31% | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-tca/5006-tca-25e.pdf |
| More than $96,000 to $99,600 | 29% | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-tca/5006-tca-25e.pdf |
| More than $99,600 to $103,200 | 27% | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-tca/5006-tca-25e.pdf |
| More than $103,200 to $106,800 | 25% | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-tca/5006-tca-25e.pdf |
| More than $106,800 to $110,400 | 23% | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-tca/5006-tca-25e.pdf |
| More than $110,400 to $114,000 | 21% | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-tca/5006-tca-25e.pdf |
| More than $114,000 to $117,600 | 19% | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-tca/5006-tca-25e.pdf |
| More than $117,600 to $121,200 | 17% | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-tca/5006-tca-25e.pdf |
| More than $121,200 to $124,800 | 15% | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-tca/5006-tca-25e.pdf |
| More than $124,800 to $128,400 | 13% | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-tca/5006-tca-25e.pdf |
| More than $128,400 to $132,000 | 11% | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-tca/5006-tca-25e.pdf |
| More than $132,000 to $135,600 | 9% | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-tca/5006-tca-25e.pdf |
| More than $135,600 to $139,200 | 7% | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-tca/5006-tca-25e.pdf |
| More than $139,200 to $142,800 | 5% | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-tca/5006-tca-25e.pdf |
| More than $142,800 to $146,400 | 3% | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-tca/5006-tca-25e.pdf |
| More than $146,400 to $150,000 | 1% | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-tca/5006-tca-25e.pdf |
| More than $150,000 | 0% | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-tca/5006-tca-25e.pdf |

Do not linearly interpolate or apply a 2021-only top-up. Multiply the actual federal deduction (ON479-A line 6) by the selected rate (line 7), carry line 8 to **ON479 63050**. The maximum theoretical 75%-of-cap amounts are $6,000/$3,750/$8,250, but only if all federal restrictions and family-income conditions permit. The same properly allowed child-care expense supports both the federal deduction and CARE; it must not be duplicated across children or also deducted as disability supports. Bankruptcy can eliminate CARE; death is not an automatic exclusion. [Act 103.0.2(2)-(4)](https://www.ontario.ca/laws/statute/07t11), [CRA CARE instructions](https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/ontario/5006-pc.html).

### 7. Senior homeowners grant

For the **2026 grant** use age **64 or over on December 31, 2025**, Ontario residence, actual eligible 2025 tax payments and ownership/occupation, including the qualifying life-lease/fully-paid long-lease routes. One spouse applies, normally the senior; use **61070** and **61120**, not a non-existent ON-BEN Part D. It is a separate lump sum, not monthly OTB. [Act 104.1](https://www.ontario.ca/laws/statute/07t11), [grant Q&A](https://www.canada.ca/en/revenue-agency/services/child-family-benefits/provincial-territorial-programs/ontario-senior-homeowners-property-tax-grant-oshptg-questions-answers.html).

Grant before the small-payment rule is **min($500, eligible property tax) - 3.33% of adjusted income above $35,000 single / $45,000 couple**, floored at zero. The law specifies no grant at **$0.50 or less**, and a minimum **$25** where the computed grant is greater than $0.50 but below $25. The CRA describes no entitlement at $50,000 single/$60,000 couple; do not round 3.33% to an exact one-thirtieth and then ignore the statutory small-payment rule. Omitted claims, death, involuntary separation and joint ownership require their actual grant rules. Coordinate with OEPTC Step 5 rather than adding both maxima blindly. [Act 104.1(3),(7)-(8)](https://www.ontario.ca/laws/statute/07t11), [grant Q&A questions 1-8](https://www.canada.ca/en/revenue-agency/services/child-family-benefits/provincial-territorial-programs/ontario-senior-homeowners-property-tax-grant-oshptg-questions-answers.html).

### 8. Seniors care at home: preserve the medical credit

Eligibility includes Ontario year-end residence and the statutory senior/spouse/survivor routes in **103.0.6(2)**: the individual was at least 69 at the preceding December 31, or the year-end spouse is at least 70, or the deceased-spouse condition applies. The latest return instructions use age 70 at year-end for taxpayer or spouse. Bankruptcy makes this credit nil. [Act 103.0.6](https://www.ontario.ca/laws/statute/07t11), [CRA senior care instructions](https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/ontario/5006-pc.html).

The base is **ON428 line 58769**, the allowable medical amount after the relevant medical-income threshold and allocations, not raw home-care receipts. Compute **min($1,500, 25% of that allowable amount)**, less **5% of family net income above $35,000**, floored at zero. A maximum-sized credit reaches nil at $65,000; a smaller base can disappear earlier. Use ON479 **lines 3-13 / 63095**, not Schedule ON479-A. [ON479](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-tc/5006-tc-25e.pdf), [Act 103.0.6(3)-(4)](https://www.ontario.ca/laws/statute/07t11).

**The same eligible medical expense can support the federal and Ontario medical credits and this credit.** Section 103.0.6(7) expressly permits coordination. Do not allocate receipts to whichever programme has the highest headline percentage and delete the other valid claim. Prescription drugs, medical travel and qualifying care-facility expenses are not excluded merely because they were not spent at home; apply actual medical eligibility, reimbursements, disability-support and attendant-care/DTC restrictions first. Home nursing, attendant care, qualifying therapy, medical equipment and diabetic supplies require the same evidence. [Act 103.0.6(7)](https://www.ontario.ca/laws/statute/07t11), [CRA senior-care section](https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/ontario/5006-pc.html).

### 9. Complete the remaining forms without confusing tax and refunds

Compute ON428 under `on-individual-return`, including non-refundable credits at the Ontario lowest rate, surtax on the specified Ontario-tax base, tax reduction, LIFT and Health Premium. The old statement describing surtax as 5.05% times thresholds was wrong. LIFT belongs on **ON428-A**, not ON479-A, and its actual statutory maximum is **$875**, not $885; use the complete income/employment/AMT/bankruptcy conditions in the companion rather than a single guessed threshold. [Act 16 and 21.1](https://www.ontario.ca/laws/statute/07t11).

The latest ON479 includes CARE, seniors care, seniors transit, political contributions, focused flow-through share expenses and the **co-operative education credit for qualifying unincorporated businesses/partners**, not corporations only. It also includes the newer fertility-treatment credit. Use the current year's actual law/form and programme-specific receipts and worksheet; do not award an unlisted credit because a past form had it. CARE flows through 63050, seniors care through 63095, and the ON479 total to **T1 47900**. ON428 tax flows to **42800**. ON-BEN benefit payments remain separate. [CRA ON479 section](https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/ontario/5006-pc.html), [ON479](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-tc/5006-tc-25e.pdf).

### Coordination and evidence checklist

| Same item | Correct treatment | Official source |
|---|---|---|
| Allowed T778 child-care expense | Federal deduction and CARE both possible; use supporting-person income add-backs, not duplicate receipts | https://www.ontario.ca/laws/statute/07t11 ; https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-tca/5006-tca-25e.pdf |
| Medical or attendant-care expense | Medical credits and seniors-care credit may coexist; resolve disability-support/DTC restrictions and reimbursements first | https://www.ontario.ca/laws/statute/07t11 ; https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/ontario/5006-pc.html |
| Property tax and homeowner grant | Both grant and OEPTC can apply, subject to the worksheet occupancy-cost limit | https://www.ontario.ca/laws/statute/07t11 ; https://www.canada.ca/en/revenue-agency/services/child-family-benefits/provincial-territorial-programs/ontario-energy-property-tax-credit-oeptc-calculation-sheets/2026-ontario-energy-property-tax-credit-calculation-sheets/2026-ontario-energy-property-tax-credit-calculation-sheet-single-senior-no-children.html |
| Rent and care accommodation | Eligible route depends on actual tax status and room/board evidence; do not claim the same amount twice as rent and LTC accommodation | https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/ontario/5006-pc.html |
| Charitable donation | Federal and Ontario donation credits normally coordinate through their respective forms; not an OTB item | https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/ontario/5006-pc.html |

## Worked cases

### Case 1: Sara and Marco, corrected same facts

Sara, 35, and Marco, 36, lived in Toronto for all of **2025** with children aged 4 and 8. Their line 23600 amounts are $50,000/$30,000. Eligible rent is $24,000; the residence is subject to property tax. There are no owner tax, reserve, care-home or Northern Ontario costs. The federal T778 deduction actually allowed to Marco is $11,000 ($8,000 for the younger child and $3,000 for the other); there is no social-benefits repayment.

For **2026 OTB**, AFNI is assumed to be $80,000 with no further adjustments. Occupancy cost is $4,800, energy $290 and property **$73 + $480 = $553**, not the $1,017 maximum. The $843 total less 2% of $43,691 is nil. OSTC starts at 4 x $378 = $1,512, less 4% of $43,691, also nil; NOEC is nil. The old $341.22 OTB result was wrong.

CARE uses a different income: $80,000 + $11,000 = **$91,000**. The statutory table rate is **33%**, so CARE is **$3,630**, not the old linear estimate of about $4,442. That amount is on the 2025 return's ON479; it is not itself an OTB payment. A 2026-income case needs that year's expense/return data and the published 2027 benefit figures separately. [OEPTC couple sheet](https://www.canada.ca/en/revenue-agency/services/child-family-benefits/provincial-territorial-programs/ontario-energy-property-tax-credit-oeptc-calculation-sheets/2026-ontario-energy-property-tax-credit-calculation-sheets/2026-ontario-energy-property-tax-credit-calculation-sheet-married-common-laws-no-children.html), [OSTC](https://www.canada.ca/en/revenue-agency/services/child-family-benefits/provincial-territorial-programs/province-ontario.html), [CARE table](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-tca/5006-tca-25e.pdf).

```oa-check
name: Sara and Marco, 2025 return and 2026 benefit cycle
inputs:
  rent: 24000
  otb_afni: 80000
  federal_childcare_deduction: 11000
steps:
  - occupancy: rent * 0.20
  - energy: min(290, occupancy)
  - property_credit: min(occupancy, 73 + min(occupancy * 0.10, 944))
  - oeptc: max(0, energy + property_credit - max(0, otb_afni - 36309) * 0.02)
  - ostc: max(0, 4 * 378 - max(0, otb_afni - 36309) * 0.04)
  - otb: oeptc + ostc
  - care_income: otb_afni + federal_childcare_deduction
  - care_rate: max(0, 0.51 - ceil(max(0, care_income - 60000) / 3600) * 0.02)
  - care: federal_childcare_deduction * care_rate
expected:
  occupancy: 4800
  property_credit: 553
  oeptc: 0
  ostc: 0
  otb: 0
  care_income: 91000
  care_rate: 0.33
  care: 3630
```

### Case 2: senior medical credit and CARE boundary decisions

My Ontario client is 72 in 2026 with no spouse. The completed current Ontario medical computation gives **$4,000 at ON428 line 58769**, already after medical eligibility/thresholds. Family net income is $40,000. Seniors care starts at $1,000 and reduces by $250 to **$750**. The valid underlying federal/Ontario medical credits are retained. At $65,000 income, even a $6,000 base reaches nil; no new $1,500 credit is added on top of that ceiling.

For a separate CARE client whose actual allowed T778 deduction is $5,000 and adjusted income is **$40,000**, the rate is 59%, credit $2,950. At **$40,001**, the next partial $5,000 block counts, rate 57%, credit $2,850. This shows why interpolation and the word "full" would give the wrong answer at a boundary. [Act 103.0.2 and 103.0.6](https://www.ontario.ca/laws/statute/07t11), [latest form reconciliation](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-tca/5006-tca-25e.pdf ; https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-tc/5006-tc-25e.pdf).

```oa-check
name: 2026 continuing-law senior credit and CARE boundary
inputs:
  allowable_medical: 4000
  family_net_income: 40000
  care_expense: 5000
steps:
  - senior_base: min(1500, allowable_medical * 0.25)
  - senior_reduction: max(0, family_net_income - 35000) * 0.05
  - senior_credit: max(0, senior_base - senior_reduction)
  - care_at_40000: care_expense * 0.59
  - care_at_40001: care_expense * (0.59 - ceil((40001 - 40000) / 5000) * 0.02)
  - senior_at_upper_income: max(0, min(1500, 6000 * 0.25) - (65000 - 35000) * 0.05)
expected:
  senior_credit: 750
  care_at_40000: 2950
  care_at_40001: 2850
  senior_at_upper_income: 0
```

## When to refuse or refer

Preserve these review routes, with corrected legal reasons:

- **R-ON-1**: part-year/moving residents, monthly entitlement and custody changes; calculate only the periods established by evidence.
- **R-ON-2**: related-party rent, non-resident landlord or unclear property-tax status; investigate actual eligible housing payments, do not assume related rent is prohibited.
- **R-ON-3**: undocumented co-tenant allocations or gifts/payments by others; no duplicate rent claim.
- **R-ON-4**: mixed public/private care and room/board; establish the tax-status route and eligible portion, not a categorical private-home ban.
- **R-ON-5**: trusts, death, bankruptcy or survivor claims; apply each credit's law. CARE/senior-care bankruptcy exclusions do not imply every benefit or final-return claim is prohibited.
- **R-ON-6**: reserve energy combined with off-reserve housing; establish periods/costs without double counting.
- **R-ON-7**: disputed T778 provider/SIN, camp, child eligibility, earned-income or supporting-person facts; resolve the federal expense before CARE.
- **R-ON-8**: attendant-care, DTC or disability-support overlap; resolve actual restrictions without falsely excluding valid simultaneous medical/seniors-care claims.
- **R-ON-9**: designated student residence; use its special amount and any separately eligible other housing, not all residence fees as rent.
- **R-ON-10**: expired or different-year credits. The staycation credit was limited to 2022; do not use it for 2026. Route a valid omitted prior-year claim to the actual year and adjustment process. [Act 103.0.5](https://www.ontario.ca/laws/statute/07t11).

With missing information, withhold the final claim rather than insert a false single status, zero spouse income, maximum credit or adverse presumed medical allocation. Show a clearly labelled provisional worksheet only on explicit assumptions. Use the statutory stepped tables and actual base year. Keep evidence of receipt eligibility, tax status and applicant choice; obtain the CPA/experienced Ontario preparer's review before filing.

## Sources

- https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-63.html. Read for subsections 1-3, annual child-care amounts, earned-income ceiling, supporting-person restrictions and eligible-child definition, 2026-11-14.

| Official source | Read date | What was read |
|---|---|---|
| https://www.ontario.ca/laws/statute/07t11 | 2026-11-14 | Read for ss.16/21.1 routing, 103.0.2 CARE definitions/stepped rates/bankruptcy, 103.0.6 medical-credit base/coordination, 103.2-103.13 benefit mechanics and 104.1 grant; 2026 amended payment cutoff |
| https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/ontario/5006-pc.html | 2026-11-14 | Read for 2025-2026 filing-cycle ON428/ON479/ON-BEN instructions, care coordination, housing and private/public LTC routes; old deeper URL incorrectly served a 2022 guide and was rejected |
| https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-tca/5006-tca-25e.pdf | 2026-11-14 | Read for latest 2025 ON479-A pages 1-2, supporting persons, adjusted-income add-backs, line fields and every stepped-rate interval |
| https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-tc/5006-tc-25e.pdf | 2026-11-14 | Read for latest 2025 ON479 pages 1-2, seniors care lines 3-13, refundable credit destinations and co-op route |
| https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-tg/5006-tg-25e.pdf | 2026-11-14 | Read for 2026 benefit application on 2025 return, applicant rules, boxes 61020-61230, Parts A-C |
| https://www.canada.ca/en/revenue-agency/services/child-family-benefits/provincial-territorial-programs/ontario-trillium-benefit-questions-answers.html | 2026-11-14 | Read for OTB questions 1-5,9-22: period, automatic OSTC,500 cutoff, election, minimum, changes, debt offsets and corrections |
| https://www.canada.ca/en/revenue-agency/services/child-family-benefits/provincial-territorial-programs/ontario-energy-property-tax-credit-questions-answers.html | 2026-11-14 | Read for OEPTC questions 2-15, eligibility,1307/1488 maxima, residence and rent/LTC/property-tax definitions |
| https://www.canada.ca/en/revenue-agency/services/child-family-benefits/provincial-territorial-programs/province-ontario.html | 2026-11-14 | Read for 2026 OSTC adult/child amount and single/family reduction thresholds |
| https://www.canada.ca/en/revenue-agency/services/child-family-benefits/provincial-territorial-programs/northern-ontario-energy-credit-questions-answers.html | 2026-11-14 | Read for NOEC questions 2-7: districts, housing,189/290 maxima,50833/65356 reduction thresholds and applicant choice |
| https://www.canada.ca/en/revenue-agency/services/child-family-benefits/provincial-territorial-programs/ontario-energy-property-tax-credit-oeptc-calculation-sheets/2026-ontario-energy-property-tax-credit-calculation-sheets.html | 2026-11-14 | Read for worksheet selection and monthly/custody changes; senior-couple and senior-sole-care calculations require their selected complete sheet |
| https://www.canada.ca/en/revenue-agency/services/child-family-benefits/provincial-territorial-programs/ontario-energy-property-tax-credit-oeptc-calculation-sheets/2026-ontario-energy-property-tax-credit-calculation-sheets/2026-ontario-energy-property-tax-credit-calculation-sheet-married-common-laws-no-children.html | 2026-11-14 | Read for non-senior couple occupancy, energy, property formula and income reduction, Steps 1-4 |
| https://www.canada.ca/en/revenue-agency/services/child-family-benefits/provincial-territorial-programs/ontario-energy-property-tax-credit-oeptc-calculation-sheets/2026-ontario-energy-property-tax-credit-calculation-sheets/2026-ontario-energy-property-tax-credit-calculation-sheet-single-individuals-no-children.html | 2026-11-14 | Read for non-senior single/no-child income threshold and Steps 1-4 |
| https://www.canada.ca/en/revenue-agency/services/child-family-benefits/provincial-territorial-programs/ontario-energy-property-tax-credit-oeptc-calculation-sheets/2026-ontario-energy-property-tax-credit-calculation-sheets/2026-ontario-energy-property-tax-credit-calculation-sheet-single-individuals-share-care-children.html | 2026-11-14 | Read for non-senior shared-care half-single/half-family calculation |
| https://www.canada.ca/en/revenue-agency/services/child-family-benefits/provincial-territorial-programs/ontario-energy-property-tax-credit-oeptc-calculation-sheets/2026-ontario-energy-property-tax-credit-calculation-sheets/2026-ontario-energy-property-tax-credit-calculation-sheet-single-individuals-sole-care-one-child.html | 2026-11-14 | Read for non-senior sole-care parent worksheet |
| https://www.canada.ca/en/revenue-agency/services/child-family-benefits/provincial-territorial-programs/ontario-energy-property-tax-credit-oeptc-calculation-sheets/2026-ontario-energy-property-tax-credit-calculation-sheets/2026-ontario-energy-property-tax-credit-calculation-sheet-single-senior-no-children.html | 2026-11-14 | Read for senior single/no-child property/energy formula and grant coordination Step 5 |
| https://www.canada.ca/en/revenue-agency/services/child-family-benefits/provincial-territorial-programs/ontario-energy-property-tax-credit-oeptc-calculation-sheets/2026-ontario-energy-property-tax-credit-calculation-sheets/2026-ontario-energy-property-tax-credit-calculation-sheet-single-seniors-share-care-all-children.html | 2026-11-14 | Read for senior shared-care thresholds and grant coordination; its stray old grant-year label is not used |
| https://www.canada.ca/en/revenue-agency/services/child-family-benefits/provincial-territorial-programs/ontario-senior-homeowners-property-tax-grant-oshptg-questions-answers.html | 2026-11-14 | Read for 2026 grant questions 1-8, ownership, tax paid and income reduction, cross-checked Act 104.1 minimum rules |
| https://www.canada.ca/en/revenue-agency/services/child-family-benefits/provincial-territorial-programs/province-ontario/ostc-seniors-income-threshold-qa.html | 2026-11-14 | Read for 2026 OSTC senior-family 37273 threshold and recipient/redetermination rules |

Not yet confirmed: final 2026 ON479/ON479-A/ON-BEN layouts and the indexed 2027 OTB maxima/thresholds based on 2026 income. Do not substitute the 2026 benefit figures. Client-specific eligible care/child-care/medical amounts and periods require the underlying federal methods. Senior-couple and senior-sole-care OEPTC formulas are routed to the selected official calculation sheet, not supplied from memory here. Blocked/obsolete Ontario policy URLs and the old CRA OTB/deep 2022 guide URLs were not used as current evidence; current law, CRA guide and actual calculation bodies above replace them. No CPA approval is asserted by this rewrite.
