---
name: au-medicare-levy
description: Use this skill whenever asked about the Australian Medicare Levy, Medicare Levy Surcharge (MLS), low-income reduction thresholds, family thresholds, surcharge tiers, private health insurance (PHI) rebate interaction, or Medicare levy exemptions. Trigger on phrases like "Medicare levy", "Medicare surcharge", "MLS", "do I pay Medicare levy", "low income Medicare", "Medicare levy reduction", "Medicare levy exemption", "private health insurance rebate", "PHI rebate", "M1", "M2", or any question about Medicare-related levies on an Australian tax return. ALWAYS read this skill before touching any Medicare levy work.
version: 2.4
jurisdiction: AU
tax_year: 2025
tax_year_notes: "2025–26; separately labelled 2024–25 historical material"
type: computation
last_updated: 2026-11-27
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
reviewed_by: "Ryan Duguid"
reviewed_on: 2026-11-03
tier: 1
domain: payroll
---

# Australia Medicare Levy and Medicare Levy Surcharge v2.4

> General reference only. Prepare an estimate and working papers for professional review before filing or acting.

## Scope

Australian individual income-tax returns, including sole traders. Main coverage: **2025–26, 1 July 2025 to 30 June 2026**. The frontmatter 2025 is the coverage start year, not the year ending. Historical 2024–25 means 1 July 2024 to 30 June 2025; never substitute its figures into a 2025–26 case. These tables do not establish 2026–27 MLS or rebate tiers.

The ordinary levy is 2% of taxable income before applicable reductions and exemptions. Private health insurance does not remove that ordinary levy. MLS is a separate charge, selected using income for surcharge purposes and calculated on a different base. [MLA ss 6–9](https://www.legislation.gov.au/C2004A03351/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_1/document_1.html).

## Ask the client first

Obtain taxable income; tax residency and exact change dates; spouse/de facto status and dates (including separation or death); each spouse's taxable income and surcharge-income components; children’s ages, residency, study, maintenance, ATI and care/FTB facts; actual SAPTO entitlement; hospital-cover statements for every family member, excess and covered dates; Medicare exemption evidence and any family agreement; and PHI premium/rebate statement rows and the oldest insured person's age. Unknown is a missing input: do not default to resident, single, uninsured, no SAPTO, or zero adjustments.

Bank descriptions are investigation prompts only. ATO/AUSTRALIAN TAXATION OFFICE, ATO INTEGRATED CLIENT ACCOUNT, REFUND - ATO and TAX REFUND require the assessment/account reconciliation; do not infer a levy amount from the payment. MEDIBANK/MEDIBANK PRIVATE, BUPA/BUPA HI PTY, HCF/HOSPITALS CONTRIBUTION FUND, NIB/NIB HEALTH FUNDS, HBF/HBF HEALTH, AHSA/AHM/AUSTRALIAN HEALTH, TEACHERS HEALTH/DEFENCE HEALTH, FRANK HEALTH/GMHBA and HEALTH INSURANCE/PRIVATE HOSPITAL require an insurer statement: a premium payment alone proves neither appropriate hospital cover nor rebate entitlement. MEDICARE/SERVICES AUSTRALIA, PBS/PHARMACEUTICAL BENEFITS and BULK BILL/MEDICAL CENTRE are not evidence of a levy payment. Confirm the underlying document before classifying.

## Rates, bands and thresholds

All amounts are AUD. SAPTO thresholds require entitlement to an amount of the offset, not age alone. Individual thresholds apply before the family reduction and exemption calculations.

| 2025–26 ordinary levy category | Lower threshold: nil levy at or below | Individual phase-in limit / family worksheet limit | Source |
|---|---|---|---|
| Individual, general | $28,011 | $35,013 | [MLA ss 3, 7](https://www.legislation.gov.au/C2004A03351/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_1/document_1.html) |
| Individual, SAPTO-entitled | $44,268 | $55,335 | [MLA ss 3, 7](https://www.legislation.gov.au/C2004A03351/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_1/document_1.html) |
| Eligible family, general | $47,238 + $4,338 per eligible child | $59,047 + $5,423 per eligible child; eligibility screening, not the levy formula | [MLA s 8](https://www.legislation.gov.au/C2004A03351/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_1/document_1.html); [M1 worksheets](https://www.ato.gov.au/forms-and-instructions/individual-tax-return-2026-instructions/medicare-levy-questions-m1-m2-individual-tax-return-2026/m1-medicare-levy-reduction-or-exemption-2026) |
| Eligible family, SAPTO-entitled relevant person | $61,623 + $4,338 per eligible child | $77,028 + $5,423 per eligible child; eligibility screening, not the levy formula | [MLA s 8(7)](https://www.legislation.gov.au/C2004A03351/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_1/document_1.html); [M1](https://www.ato.gov.au/forms-and-instructions/individual-tax-return-2026-instructions/medicare-levy-questions-m1-m2-individual-tax-return-2026/m1-medicare-levy-reduction-or-exemption-2026) |

The 2026 amendment applies these ordinary-levy thresholds to assessments for 2025–26 and later years despite the compilation's 1 July 2026 date. [Schedule 5 item 14](https://www.legislation.gov.au/C2026A00058/asmade/2026-06-30/text/original/epub/OEBPS/document_1/document_1.html).

| 2025–26 MLS tier | Single surcharge income | Family surcharge income before child increases | Rate |
|---|---|---|---|
| Base | At most $101,000 | At most $202,000 | 0%; [ATO M2](https://www.ato.gov.au/forms-and-instructions/individual-tax-return-2026-instructions/medicare-levy-questions-m1-m2-individual-tax-return-2026/m2-medicare-levy-surcharge-2026) |
| Tier 1 | Over $101,000 to $118,000 | Over $202,000 to $236,000 | 1%; [ATO M2](https://www.ato.gov.au/forms-and-instructions/individual-tax-return-2026-instructions/medicare-levy-questions-m1-m2-individual-tax-return-2026/m2-medicare-levy-surcharge-2026) |
| Tier 2 | Over $118,000 to $158,000 | Over $236,000 to $316,000 | 1.25%; [ATO M2](https://www.ato.gov.au/forms-and-instructions/individual-tax-return-2026-instructions/medicare-levy-questions-m1-m2-individual-tax-return-2026/m2-medicare-levy-surcharge-2026) |
| Tier 3 | Over $158,000 | Over $316,000 | 1.5%; [ATO M2](https://www.ato.gov.au/forms-and-instructions/individual-tax-return-2026-instructions/medicare-levy-questions-m1-m2-individual-tax-return-2026/m2-medicare-levy-surcharge-2026) |

Increase **every family boundary** by $1,500 per MLS-dependent child after the first. [PHI Act ss 22-30–22-45](https://www.legislation.gov.au/C2007A00031/2026-09-19/2026-09-19/text/original/epub/OEBPS/document_1/document_1.html); [MLA ss 3A, 8B–8D](https://www.legislation.gov.au/C2004A03351/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_1/document_1.html).

## The method, step by step

### Ordinary levy: individual and family reduction

1. For taxable income x at or below the applicable individual lower threshold L, the levy is nil. Above L and at or below the individual phase-in limit, use the lesser of 2% × x and 10% × (x − L). Above that limit use 2% × x. This cap matters at a rounded phase-in boundary. [MLA s 7](https://www.legislation.gov.au/C2004A03351/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_1/document_1.html).
2. Check family eligibility: married/de facto at year end (living separately and apart is excluded; the statutory deceased-spouse rule can apply), or the child tax-offset/notional-offset conditions in s 8(1). An eligible sole parent has family income equal to their own taxable income; a year-end couple uses the sum of taxable incomes, not MLS add-backs. Negative taxable income is entered as zero in M1. [MLA ss 3(3), 8](https://www.legislation.gov.au/C2004A03351/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_1/document_1.html); [M1](https://www.ato.gov.au/forms-and-instructions/individual-tax-return-2026-instructions/medicare-levy-questions-m1-m2-individual-tax-return-2026/m1-medicare-levy-reduction-or-exemption-2026).
3. Establish eligible children using M1, not the MLS definition. For reduction purposes a maintained Australian-resident child is under 21 and not a full-time student, or a full-time student under 25. Full-year ATI must be **less than** $1,786 for the first non-student child or each student, and $1,410 for an additional non-student child; part-year limits are $282 + $28.92 per maintained week, or $282 + $21.70 for an additional non-student child. A single/separated year-end parent counts only children for whom FTB was payable during all or part of the year. Sole care requires full day-to-day responsibility; unresolved special-care facts need professional review. [M1 dependent children and sole care](https://www.ato.gov.au/forms-and-instructions/individual-tax-return-2026-instructions/medicare-levy-questions-m1-m2-individual-tax-return-2026/m1-medicare-levy-reduction-or-exemption-2026); MLA s 8(5)–(6).
4. For each qualifying relevant person, set T to their applicable family lower threshold. If family income F ≤ T, their ordinary levy is nil. If F > T, compute the positive reduction R = max(0, 0.02 × T − 0.08 × (F − T)), then subtract it from their individual levy. If the year-end spouse also has an individual levy before ss 8 and 9, reduce R by R × spouse taxable income / F; if the resulting reduction exceeds the relevant person's levy, apply the excess to the spouse under s 8(4). Do not subtract an unallocated full R from both spouses. Establish each person's SAPTO threshold separately. [MLA s 8(1)–(4), including its formula](https://www.legislation.gov.au/C2004A03351/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_1/document_1.html).
5. Apply ordinary-levy exemption days after reductions. For confirmed full and half exemption days dF and dH, the remaining estimate is reduced levy × (365 − dF − dH/2) / 365 for 2025–26. Count overlapping days once, with full exemption taking priority. [MLA s 9](https://www.legislation.gov.au/C2004A03351/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_1/document_1.html); [ITAA 1936 s 251U(3)](https://www.legislation.gov.au/C1936A00027/2026-04-01/2026-04-01/text/original/epub/OEBPS/document_4/document_4.html); [M1](https://www.ato.gov.au/forms-and-instructions/individual-tax-return-2026-instructions/medicare-levy-questions-m1-m2-individual-tax-return-2026/m1-medicare-levy-reduction-or-exemption-2026).

### Exemptions and cross-border points

A full-year foreign tax resident pays no ordinary Medicare levy. A part-year foreign resident can claim full exemption for the non-resident period only if they have no dependants then or all dependants are in exemption categories. A temporary resident for Medicare purposes needs a Services Australia Medicare Entitlement Statement for that year and period, plus the same dependent condition. Visa status or non-enrolment alone is insufficient. [ITAA 1936 ss 251S–251U](https://www.legislation.gov.au/C1936A00027/2026-04-01/2026-04-01/text/original/epub/OEBPS/document_4/document_4.html); [M1 categories 2 and 3](https://www.ato.gov.au/forms-and-instructions/individual-tax-return-2026-instructions/medicare-levy-questions-m1-m2-individual-tax-return-2026/m1-medicare-levy-reduction-or-exemption-2026).

Medical category means a blind pensioner or entitlement to full free treatment for all conditions under the applicable Defence/Veterans arrangements, not any medical condition or blindness alone. Full exemption applies with no dependants, or where all dependants are exempt or pay levy; joint-child/spouse rules can also establish full exemption. An otherwise eligible medical person with a non-exempt dependant who need not pay levy can have half exemption. If both medically exempt spouses have joint non-exempt children, a qualifying written family agreement allocates one full and one half exemption; sign before the full-exemption claimant lodges, retain it, and apply the statutory retention rule (normally 5 years from lodgment). Shared-care days and family agreements must be settled before using full/half day counts. [ITAA 1936 ss 251R, 251U](https://www.legislation.gov.au/C1936A00027/2026-04-01/2026-04-01/text/original/epub/OEBPS/document_4/document_4.html); [M1 category 1](https://www.ato.gov.au/forms-and-instructions/individual-tax-return-2026-instructions/medicare-levy-questions-m1-m2-individual-tax-return-2026/m1-medicare-levy-reduction-or-exemption-2026).

Exemption dependants and MLS dependants are different from reduction children: read the applicable definition. For exemption, maintained resident spouse/children under 21 qualify, and students aged 21–24 have the notional-offset/ATI test; MLS disregards that income restriction. A half ordinary-levy exemption is not automatically a half MLS exemption. [ITAA 1936 ss 251R, 251V–251VA](https://www.legislation.gov.au/C1936A00027/2026-04-01/2026-04-01/text/original/epub/OEBPS/document_4/document_4.html).

### MLS: three separate decisions

1. Work out annual **income for surcharge purposes**: taxable income excluding assessable FHSS released amounts, plus reportable fringe benefits, reportable employer and deductible personal super contributions, total net financial-investment/rental losses and relevant amounts subject to family trust distribution tax. Apply the s 301-20 low-rate-cap super lump-sum reduction where entitled; child support paid is not a general deduction. Exempt foreign employment income, trustee-assessed spouse income and lump sums in arrears require their special instructions, below. [ITAA 1997 s 995-1](https://www.legislation.gov.au/C2004A05138/2026-04-01/2026-04-01/text/original/epub/OEBPS/document_10/document_10.html); [M2 worksheet 1](https://www.ato.gov.au/forms-and-instructions/individual-tax-return-2026-instructions/medicare-levy-questions-m1-m2-individual-tax-return-2026/m2-medicare-levy-surcharge-2026).
2. Determine **liability for each period** using MLA ss 8B–8D. For a single without dependants compare their annual income with the single base; for a single with dependants compare with the family base. For someone married all year compare combined annual income with the family base, but that person has no MLS if their own surcharge income is at most $28,011. When married only part of the year, the married-period liability test compares their own annual income with the family base; do not automatically add the former/new spouse's income for that test. Choose the rate using the statutory year-end tier rules, separately from period liability. Spouse death, separation and family-status changes require the M2 period rules. [MLA ss 3, 3A, 8B–8D](https://www.legislation.gov.au/C2004A03351/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_1/document_1.html); [M2 changing circumstances](https://www.ato.gov.au/forms-and-instructions/individual-tax-return-2026-instructions/medicare-levy-questions-m1-m2-individual-tax-return-2026/m2-medicare-levy-surcharge-2026).
3. For liable days, charge the selected rate on each person's **statutory base**: taxable income plus total reportable fringe benefits and relevant family-trust distribution amounts, with applicable exclusions/adjustments. Reportable super and net investment loss are tier add-backs, not base add-backs. Multiply by liable days / 365, summing periods as necessary. [MLA ss 8B–8D](https://www.legislation.gov.au/C2004A03351/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_1/document_1.html); [Fringe Benefits Surcharge Act ss 11–16](https://www.legislation.gov.au/C2004A00412/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_1/document_1.html); [M2](https://www.ato.gov.au/forms-and-instructions/individual-tax-return-2026-instructions/medicare-levy-questions-m1-m2-individual-tax-return-2026/m2-medicare-levy-surcharge-2026).

Appropriate cover is a complying registered-insurer policy for private hospital treatment in Australia, with excess no more than $750 in any 12 months for one insured person or $1,500 for other policies. Extras alone do not qualify. Check all relevant family members on each day, allowing the statutory prescribed-person/treated-as-covered exceptions; do not assume cover held by one spouse protects that spouse when another non-exempt family member lacks cover. [MLA s 3(5)](https://www.legislation.gov.au/C2004A03351/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_1/document_1.html); [PHI Act s 45-1](https://www.legislation.gov.au/C2007A00031/2026-09-19/2026-09-19/text/original/epub/OEBPS/document_1/document_1.html); [M2](https://www.ato.gov.au/forms-and-instructions/individual-tax-return-2026-instructions/medicare-levy-questions-m1-m2-individual-tax-return-2026/m2-medicare-levy-surcharge-2026).

For MLS, a dependant is a maintained Australian-resident spouse (including registered or genuine domestic de facto relationship), child under 21, or full-time student child aged 21–24, regardless of income. A policy's own dependent-person definition is not the tax definition. [ITAA 1936 ss 251R, 251V](https://www.legislation.gov.au/C1936A00027/2026-04-01/2026-04-01/text/original/epub/OEBPS/document_4/document_4.html); [M2 dependants](https://www.ato.gov.au/forms-and-instructions/individual-tax-return-2026-instructions/medicare-levy-questions-m1-m2-individual-tax-return-2026/m2-medicare-levy-surcharge-2026).

### PHI rebate interaction

A complying policy can cover hospital, extras, or both for rebate purposes, although extras alone cannot avoid MLS. Rebate entitlement also requires Medicare eligibility and beneficiary status and is income-tested. Use the oldest insured person's age, eligible premiums excluding lifetime-health-cover loading, and each adult's share. Allocate shared adult premiums equally before income-testing each adult. Obtain the insurer statement; do not estimate entitlement from a bank debit. The rebate can be received through reduced premiums or the tax return, with an excess rebate recovered or a shortfall credited on assessment. [PHI Act ss 22-5–22-25](https://www.legislation.gov.au/C2007A00031/2026-09-19/2026-09-19/text/original/epub/OEBPS/document_1/document_1.html); [ATO eligibility](https://www.ato.gov.au/individuals-and-families/medicare-and-private-health-insurance/private-health-insurance-rebate/private-health-insurance-rebate-eligibility); [ATO rates](https://www.ato.gov.au/individuals-and-families/medicare-and-private-health-insurance/private-health-insurance-rebate/income-thresholds-and-rates-for-the-private-health-insurance-rebate).

For the rebate family-tier test, a spouse at 30 June means combined annual income. Substantially maintaining a qualifying PHI-dependent child on any day during the year also invokes the family tiers under s 22-30(1)(b), even if the child is no longer dependent on 30 June. Establish qualifying dependent-person status before using that test. A person with neither family trigger uses single tiers and their own income. A spouse who died during the year is included under the special rule. Other dependent-person/child-only policies need the beneficiary and family-tier provisions checked before an amount is used. The rebate and MLS share indexed income boundaries, but their family/period tests are not interchangeable. [PHI Act s 22-30](https://www.legislation.gov.au/C2007A00031/2026-09-19/2026-09-19/text/original/epub/OEBPS/document_1/document_1.html); [ATO rates](https://www.ato.gov.au/individuals-and-families/medicare-and-private-health-insurance/private-health-insurance-rebate/income-thresholds-and-rates-for-the-private-health-insurance-rebate).

| 2025–26 premium payment period and oldest insured age | Base rebate | Tier 1 | Tier 2 | Tier 3 | Source |
|---|---|---|---|---|---|
| 1 July 2025–31 March 2026; under 65 | 24.288% | 16.192% | 8.095% | 0% | [ATO](https://www.ato.gov.au/individuals-and-families/medicare-and-private-health-insurance/private-health-insurance-rebate/income-thresholds-and-rates-for-the-private-health-insurance-rebate) |
| Same period; 65–69 | 28.337% | 20.240% | 12.143% | 0% | [ATO](https://www.ato.gov.au/individuals-and-families/medicare-and-private-health-insurance/private-health-insurance-rebate/income-thresholds-and-rates-for-the-private-health-insurance-rebate) |
| Same period; 70+ | 32.385% | 24.288% | 16.192% | 0% | [ATO](https://www.ato.gov.au/individuals-and-families/medicare-and-private-health-insurance/private-health-insurance-rebate/income-thresholds-and-rates-for-the-private-health-insurance-rebate) |
| 1 April–30 June 2026; under 65 | 24.118% | 16.079% | 8.038% | 0% | [ATO](https://www.ato.gov.au/individuals-and-families/medicare-and-private-health-insurance/private-health-insurance-rebate/income-thresholds-and-rates-for-the-private-health-insurance-rebate) |
| Same period; 65–69 | 28.139% | 20.098% | 12.058% | 0% | [ATO](https://www.ato.gov.au/individuals-and-families/medicare-and-private-health-insurance/private-health-insurance-rebate/income-thresholds-and-rates-for-the-private-health-insurance-rebate) |
| Same period; 70+ | 32.158% | 24.118% | 16.079% | 0% | [ATO](https://www.ato.gov.au/individuals-and-families/medicare-and-private-health-insurance/private-health-insurance-rebate/income-thresholds-and-rates-for-the-private-health-insurance-rebate) |

Annual percentage adjustment is on 1 April under PHI Act s 22-15(5A)–(5D), not a guarantee that the percentage always falls. Buying appropriate cover can remove MLS for covered days; it does not guarantee a rebate or that premiums cost less than the tax saved. Compare actual premiums, rebate entitlement and MLS avoided for the relevant dates.

## Deadlines and filing

Use the income-tax return for the relevant year. At M1 use the reduction instructions: a person below the individual lower threshold leaves the reduction fields blank; eligible family cases report dependent children at Y and spouse taxable income at Spouse details O. Exemptions use full days V, half days W and claim type C for a qualifying Medicare Entitlement Statement; complete spouse details if applicable. ATO calculates the reduction/exemption. [M1](https://www.ato.gov.au/forms-and-instructions/individual-tax-return-2026-instructions/medicare-levy-questions-m1-m2-individual-tax-return-2026/m1-medicare-levy-reduction-or-exemption-2026).

M2 is compulsory. Answer full-year appropriate cover at E; complete policy details. If not fully covered, determine exemption and write at A the number of days **not liable** for MLS: 365 for no liable days and zero for full-year liability. Complete income tests, IT8 dependent children and required spouse details. An M1 exemption does not dispense with M2. Reconcile the final levy, surcharge and rebate adjustment with the notice of assessment. [M2 completing your tax return](https://www.ato.gov.au/forms-and-instructions/individual-tax-return-2026-instructions/medicare-levy-questions-m1-m2-individual-tax-return-2026/m2-medicare-levy-surcharge-2026).

## Worked cases

All current examples are **2025–26**. Unless an example states otherwise, assume full-year resident status, the stated relationship throughout the year, no exemption, and no unlisted surcharge-income/base adjustment. Hospital cover means appropriate hospital cover for every required person. General-threshold cases have no SAPTO entitlement. Family reduction children meet the M1 conditions; MLS children meet the separate M2 definition. These are conditional estimates.

| Original case | Inputs preserved | Result and conditions |
|---|---|---|
| EC1 | Foreign resident 3 months, resident 9 months | Use exact dates, not 3/12. Full exemption for foreign-resident days requires no dependants or all exempt during that period. Apply the day fraction after the full-year-income levy reduction calculation; the facts do not determine a dollar amount. |
| EC2 | One spouse covered, the other uninsured | Both can be liable on their separate bases for uncovered-family days if income tests apply; exempt family members and the individual low-income rule can change this. No income was supplied, so no dollar conclusion. |
| EC3 | Single taxable income $29,000 | min($580, ($29,000 − $28,011) × 10%) = $98.90. |
| EC4 | Single taxable income $90,000, deducted rental loss $15,000 | Surcharge income $105,000, base $90,000: full-year uncovered MLS = $900 at 1%. |
| EC5 | Age 68, taxable income $45,000, entitled to SAPTO | Assuming single and actual SAPTO entitlement: min($900, ($45,000 − $44,268) × 10%) = $73.20. |
| EC6 | Family, 4 eligible children, combined taxable income $55,000 | T = $47,238 + 4 × $4,338 = $64,590; nil ordinary levy for qualifying family members. |
| EC7 | Single, 200 covered/165 uncovered days, taxable/surcharge income and base $120,000 | $120,000 × 1.25% × 165/365 = $678.08 MLS; no other exemption. |
| Test 1 | Single resident, $80,000, PHI | Ordinary levy $1,600; MLS nil. |
| Test 2 | Single, $30,000, no spouse | min($600, ($30,000 − $28,011) × 10%) = $198.90. |
| Test 3 | Single, $25,000 | Nil ordinary levy. |
| Test 4 | Single, income/base $105,000, no cover all year | Ordinary $2,100 + MLS $1,050 = $3,150. |
| Test 5 | Single, income/base $200,000, no cover all year | Ordinary $4,000 + MLS $3,000 = $7,000. |
| Test 6 | Family, 2 eligible children, taxable income $50,000 | T = $47,238 + 2 × $4,338 = $55,914; nil ordinary levy. |
| Test 7 | Foreign resident whole year, Australian-source taxable income $60,000 | Nil ordinary levy; report full exemption days in M1 and complete M2. |
| Test 8 | Married couple, 3 children, each income/base $105,000, combined $210,000, no cover/exemptions all year | Family base $202,000 + 2 × $1,500 = $205,000; each pays MLS $1,050, combined $2,100. |
| Distinct-base check 1 | Single, taxable $100,000 + reportable super $10,000, no cover all year | Tier income $110,000; base $100,000; MLS $1,000. |
| Distinct-base check 2 | Single, taxable $110,000 + reportable super $15,000, no cover all year | Tier income $125,000; base $110,000; MLS $1,375. |

The case calculations apply [MLA ss 6–9](https://www.legislation.gov.au/C2004A03351/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_1/document_1.html) and [M1](https://www.ato.gov.au/forms-and-instructions/individual-tax-return-2026-instructions/medicare-levy-questions-m1-m2-individual-tax-return-2026/m1-medicare-levy-reduction-or-exemption-2026) / [M2](https://www.ato.gov.au/forms-and-instructions/individual-tax-return-2026-instructions/medicare-levy-questions-m1-m2-individual-tax-return-2026/m2-medicare-levy-surcharge-2026). A historical version gave only combined family income for Test 8: that establishes a tier, not either spouse's dollar liability. The separately stated $105,000 bases are essential to the current dollar illustration.

```oa-check
name: Original ordinary levy cases, 2025–26
inputs:
  ec3: 29000
  ec5: 45000
  ec6_income: 55000
  test1: 80000
  test2: 30000
  test3: 25000
  test6_income: 50000
  foreign_income: 60000
steps:
  ec3_levy: min(ec3 * 0.02, max(0, ec3 - 28011) * 0.10)
  ec5_levy: min(ec5 * 0.02, max(0, ec5 - 44268) * 0.10)
  ec6_threshold: 47238 + 4338 * 4
  ec6_levy: max(0, min(ec6_income * 0.02, (ec6_income - ec6_threshold) * 0.10))
  test1_levy: test1 * 0.02
  test2_levy: min(test2 * 0.02, max(0, test2 - 28011) * 0.10)
  test3_levy: min(test3 * 0.02, max(0, test3 - 28011) * 0.10)
  test6_threshold: 47238 + 4338 * 2
  test6_levy: max(0, min(test6_income * 0.02, (test6_income - test6_threshold) * 0.10))
  foreign_levy: foreign_income * 0.02 * (365 - 365) / 365
expected:
  ec3_levy: 98.90
  ec5_levy: 73.20
  ec6_threshold: 64590
  ec6_levy: 0
  test1_levy: 1600
  test2_levy: 198.90
  test3_levy: 0
  test6_threshold: 55914
  test6_levy: 0
  foreign_levy: 0
```

```oa-check
name: Original MLS cases and separate threshold income, 2025–26
inputs:
  rental_taxable: 90000
  rental_loss: 15000
  part_year_base: 120000
  covered_days: 200
  uncovered_days: 165
  test4: 105000
  test5: 200000
  spouse1: 105000
  spouse2: 105000
  children: 3
  taxable1: 100000
  super1: 10000
  taxable2: 110000
  super2: 15000
steps:
  rental_tier_income: rental_taxable + rental_loss
  rental_mls: rental_taxable * 0.01
  part_year_mls: part_year_base * 0.0125 * uncovered_days / (covered_days + uncovered_days)
  test4_ordinary: test4 * 0.02
  test4_mls: test4 * 0.01
  test4_total: test4_ordinary + test4_mls
  test5_ordinary: test5 * 0.02
  test5_mls: test5 * 0.015
  test5_total: test5_ordinary + test5_mls
  family_threshold: 202000 + 1500 * (children - 1)
  family_income: spouse1 + spouse2
  spouse1_mls: spouse1 * 0.01
  spouse2_mls: spouse2 * 0.01
  combined_mls: spouse1_mls + spouse2_mls
  tier_income1: taxable1 + super1
  mls1: taxable1 * 0.01
  tier_income2: taxable2 + super2
  mls2: taxable2 * 0.0125
expected:
  rental_tier_income: 105000
  rental_mls: 900
  part_year_mls: 678.08
  test4_ordinary: 2100
  test4_mls: 1050
  test4_total: 3150
  test5_ordinary: 4000
  test5_mls: 3000
  test5_total: 7000
  family_threshold: 205000
  family_income: 210000
  spouse1_mls: 1050
  spouse2_mls: 1050
  combined_mls: 2100
  tier_income1: 110000
  mls1: 1000
  tier_income2: 125000
  mls2: 1375
```

### Historical 2024–25 tables and cases

These figures belong only to **1 July 2024–30 June 2025**, including the historical snapshots whose frontmatter misleadingly said 2025. [2025 amendment Schedule 2 item 14](https://www.legislation.gov.au/C2025A00028/asmade/2025-03-27/text/original/epub/OEBPS/document_1/document_1.html).

| Historical ordinary category | Lower threshold | Individual phase-in limit | Source |
|---|---|---|---|
| General individual | $27,222 | $34,027 | [MLA ss 3, 7, 2025 compilation](https://www.legislation.gov.au/C2004A03351/2025-03-28/2025-03-28/text/original/epub/OEBPS/document_1/document_1.html) |
| SAPTO individual | $43,020 | $53,775 | [MLA ss 3, 7](https://www.legislation.gov.au/C2004A03351/2025-03-28/2025-03-28/text/original/epub/OEBPS/document_1/document_1.html) |
| Eligible general family | $45,907 + $4,216 per eligible child | Apply s 8 method | [MLA s 8](https://www.legislation.gov.au/C2004A03351/2025-03-28/2025-03-28/text/original/epub/OEBPS/document_1/document_1.html) |
| SAPTO relevant-person family | $59,886 + $4,216 per eligible child | Apply s 8 method; the old $63,486 was wrong and must not be used | [MLA s 8(7)](https://www.legislation.gov.au/C2004A03351/2025-03-28/2025-03-28/text/original/epub/OEBPS/document_1/document_1.html) |

| Historical MLS tier | Single income | Family income before $1,500 per child after first | Rate |
|---|---|---|---|
| Base | At most $97,000 | At most $194,000 | 0%; [ATO historical table](https://www.ato.gov.au/individuals-and-families/medicare-and-private-health-insurance/private-health-insurance-rebate/income-thresholds-and-rates-for-the-private-health-insurance-rebate); [MLA ss 8B–8D](https://www.legislation.gov.au/C2004A03351/2025-03-28/2025-03-28/text/original/epub/OEBPS/document_1/document_1.html) |
| Tier 1 | Over $97,000 to $113,000 | Over $194,000 to $226,000 | 1%; [ATO](https://www.ato.gov.au/individuals-and-families/medicare-and-private-health-insurance/private-health-insurance-rebate/income-thresholds-and-rates-for-the-private-health-insurance-rebate); [MLA](https://www.legislation.gov.au/C2004A03351/2025-03-28/2025-03-28/text/original/epub/OEBPS/document_1/document_1.html) |
| Tier 2 | Over $113,000 to $151,000 | Over $226,000 to $302,000 | 1.25%; [ATO](https://www.ato.gov.au/individuals-and-families/medicare-and-private-health-insurance/private-health-insurance-rebate/income-thresholds-and-rates-for-the-private-health-insurance-rebate); [MLA](https://www.legislation.gov.au/C2004A03351/2025-03-28/2025-03-28/text/original/epub/OEBPS/document_1/document_1.html) |
| Tier 3 | Over $151,000 | Over $302,000 | 1.5%; [ATO](https://www.ato.gov.au/individuals-and-families/medicare-and-private-health-insurance/private-health-insurance-rebate/income-thresholds-and-rates-for-the-private-health-insurance-rebate); [MLA](https://www.legislation.gov.au/C2004A03351/2025-03-28/2025-03-28/text/original/epub/OEBPS/document_1/document_1.html) |

| Historical PHI premium payment period and oldest insured age | Base | Tier 1 | Tier 2 | Tier 3 | Source |
|---|---|---|---|---|---|
| 1 July 2024–31 March 2025; under 65 | 24.608% | 16.405% | 8.202% | 0% | [ATO](https://www.ato.gov.au/individuals-and-families/medicare-and-private-health-insurance/private-health-insurance-rebate/income-thresholds-and-rates-for-the-private-health-insurance-rebate) |
| Same period; 65–69 | 28.710% | 20.507% | 12.303% | 0% | [ATO](https://www.ato.gov.au/individuals-and-families/medicare-and-private-health-insurance/private-health-insurance-rebate/income-thresholds-and-rates-for-the-private-health-insurance-rebate) |
| Same period; 70+ | 32.812% | 24.608% | 16.405% | 0% | [ATO](https://www.ato.gov.au/individuals-and-families/medicare-and-private-health-insurance/private-health-insurance-rebate/income-thresholds-and-rates-for-the-private-health-insurance-rebate) |
| 1 April–30 June 2025; under 65 | 24.288% | 16.192% | 8.095% | 0% | [ATO](https://www.ato.gov.au/individuals-and-families/medicare-and-private-health-insurance/private-health-insurance-rebate/income-thresholds-and-rates-for-the-private-health-insurance-rebate) |
| Same period; 65–69 | 28.337% | 20.240% | 12.143% | 0% | [ATO](https://www.ato.gov.au/individuals-and-families/medicare-and-private-health-insurance/private-health-insurance-rebate/income-thresholds-and-rates-for-the-private-health-insurance-rebate) |
| Same period; 70+ | 32.385% | 24.288% | 16.192% | 0% | [ATO](https://www.ato.gov.au/individuals-and-families/medicare-and-private-health-insurance/private-health-insurance-rebate/income-thresholds-and-rates-for-the-private-health-insurance-rebate) |

Historical EC1 (3 months foreign/9 resident) and EC2 (only one spouse covered) retain the conditional methods above. Historical EC3 has **$28,000**, not the newer $29,000: ($28,000 − $27,222) × 10% = $77.80 versus full levy $560. Historical EC4 retains taxable $90,000 and rental loss $15,000: tier income $105,000; assuming full-year single/no cover and no other adjustments, MLS $900 on its $90,000 base. Historical EC5 retains age 68/SAPTO/taxable $45,000: levy $198 versus $900 full levy. Historical EC6 retains 4 children/$55,000 income: threshold $62,771, nil levy if eligible. Historical Test 2 at $30,000 gives $277.80; Test 3 at $25,000 gives nil; Test 6 at $50,000 with 2 children has threshold $54,339 and nil levy. Historical Test 1 ($80,000/PHI) gives ordinary $1,600 with appropriate cover; Test 7 (full-year foreign resident/$60,000 Australian income) gives nil ordinary levy. [Historical MLA ss 6–9](https://www.legislation.gov.au/C2004A03351/2025-03-28/2025-03-28/text/original/epub/OEBPS/document_1/document_1.html).

Historical EC7 specified only MLS income $120,000 and 200 covered/165 uncovered days; historical Tests 4/5 specified only MLS income $105,000/$200,000, and Test 8 only combined MLS income $200,000 with 3 children/no PHI (family base $197,000). These inputs establish the 1.25%/1%/1.5%/1% tiers respectively, but do **not** establish taxable income or either spouse's base and dollar liability. The old dollar conclusions are non-usable until those missing inputs are established. Check this point with one of our partner accountants. The later Test 8 snapshot with only combined $210,000 likewise cannot establish dollars; only the current separately specified $105,000 spouse bases do so.

```oa-check
name: Original historical ordinary-levy inputs, 2024–25
inputs:
  single: 28000
  senior: 45000
  family4: 55000
  family2: 50000
  single_test2: 30000
  single_test3: 25000
steps:
  single_levy: min(single * 0.02, max(0, single - 27222) * 0.10)
  senior_levy: min(senior * 0.02, max(0, senior - 43020) * 0.10)
  family4_threshold: 45907 + 4216 * 4
  family4_levy: max(0, min(family4 * 0.02, (family4 - family4_threshold) * 0.10))
  family2_threshold: 45907 + 4216 * 2
  family2_levy: max(0, min(family2 * 0.02, (family2 - family2_threshold) * 0.10))
  test2_levy: min(single_test2 * 0.02, max(0, single_test2 - 27222) * 0.10)
  test3_levy: min(single_test3 * 0.02, max(0, single_test3 - 27222) * 0.10)
expected:
  single_levy: 77.80
  senior_levy: 198
  family4_threshold: 62771
  family4_levy: 0
  family2_threshold: 54339
  family2_levy: 0
  test2_levy: 277.80
  test3_levy: 0
```

## When to refuse or refer

Do not compute a usable amount with missing residency, family, SAPTO, cover, income or day evidence. Report the missing input and retain the original case. Record the issue, evidence, options and unresolved point for professional review; never invent a default or an approval.

Diplomatic or prescribed overseas-forces exemptions, Norfolk Island transitional provisions, unresolved multiple visa/residency changes (including the old trigger of more than two changes), non-standard medical/shared-care/family-agreement eligibility, PHI child-only/sibling-dependent arrangements, and special exempt-foreign-employment, trustee or lump-sum-arrears adjustments are non-usable here until resolved from their operative conditions. Check this point with one of our partner accountants.

Reciprocal-health-agreement entitlement is not the tax-residency test. The earlier visitor list (UK, Ireland, New Zealand, Sweden, Netherlands, Belgium, Finland, Italy, Norway, Slovenia, Malta) is retained only as a list of **cases needing an entitlement check**, not proof of any visitor's eligibility. Do not use it to impose levy on a confirmed full-year foreign tax resident or to grant an exemption to a tax resident. Check this point with one of our partner accountants.

Never equate taxable income with MLS income or a bank premium with cover. Never use ordinary-reduction dependent rules for MLS. Never remove ordinary levy solely because of PHI, use general thresholds for a person actually entitled to SAPTO, or treat an estimate as the final assessment.

This Guide and its outputs are informational and computational material. All outputs must be reviewed and signed off by a qualified professional before filing or acting.

> Contributed by Ryan Duguid.

> Contributed by Ryan Duguid.

> Contributed by Ryan Duguid.

## Sources

| Official source and portion read | URL | Read on |
|---|---|---|
| Medicare Levy Act 1986, ss 3, 3A, 6–9 and statutory formula alternative text | https://www.legislation.gov.au/C2004A03351/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_1/document_1.html | 2026-11-27 |
| 2026 amending Act, Schedule 5 including application item 14 | https://www.legislation.gov.au/C2026A00058/asmade/2026-06-30/text/original/epub/OEBPS/document_1/document_1.html | 2026-11-27 |
| ITAA 1936 Part VIIB, ss 251R–251VA (exemptions and differing dependant rules) | https://www.legislation.gov.au/C1936A00027/2026-04-01/2026-04-01/text/original/epub/OEBPS/document_4/document_4.html | 2026-11-27 |
| ITAA 1997 s 995-1, income for surcharge purposes definition | https://www.legislation.gov.au/C2004A05138/2026-04-01/2026-04-01/text/original/epub/OEBPS/document_10/document_10.html | 2026-11-27 |
| Fringe Benefits Surcharge Act 1999, ss 11–16 | https://www.legislation.gov.au/C2004A00412/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_1/document_1.html | 2026-11-27 |
| PHI Act 2007, ss 22-5–22-45, 45-1; existing operative tier/rebate provisions, not later premium-regulation changes | https://www.legislation.gov.au/C2007A00031/2026-09-19/2026-09-19/text/original/epub/OEBPS/document_1/document_1.html | 2026-11-27 |
| ATO M1 2026: thresholds, both worksheets, definitions, exemption categories and completion | https://www.ato.gov.au/forms-and-instructions/individual-tax-return-2026-instructions/medicare-levy-questions-m1-m2-individual-tax-return-2026/m1-medicare-levy-reduction-or-exemption-2026 | 2026-11-27 |
| ATO M2 2026: tiers, bases, definitions, period rules and completion | https://www.ato.gov.au/forms-and-instructions/individual-tax-return-2026-instructions/medicare-levy-questions-m1-m2-individual-tax-return-2026/m2-medicare-levy-surcharge-2026 | 2026-11-27 |
| ATO rebate rates: 2024–25 and 2025–26 tables, dates, ages, family status and premium shares | https://www.ato.gov.au/individuals-and-families/medicare-and-private-health-insurance/private-health-insurance-rebate/income-thresholds-and-rates-for-the-private-health-insurance-rebate | 2026-11-27 |
| ATO rebate eligibility, policy and income tests | https://www.ato.gov.au/individuals-and-families/medicare-and-private-health-insurance/private-health-insurance-rebate/private-health-insurance-rebate-eligibility | 2026-11-27 |
| Historical MLA ss 3, 7–8 and 2025 amendment Schedule 2 application | https://www.legislation.gov.au/C2004A03351/2025-03-28/2025-03-28/text/original/epub/OEBPS/document_1/document_1.html; https://www.legislation.gov.au/C2025A00028/asmade/2025-03-27/text/original/epub/OEBPS/document_1/document_1.html | 2026-11-27 |

Not yet confirmed: the referred special cases and incomplete historical dollar outcomes above are non-usable holds. Check this point with one of our partner accountants. Main ordinary levy, family reduction, standard exemptions, MLS methods and dated PHI tables are supported as stated. ATO direct fetch returned 403; the relevant pages were read in the normal browser.
