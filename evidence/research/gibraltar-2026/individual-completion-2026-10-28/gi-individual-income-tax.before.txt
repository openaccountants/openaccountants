---
name: gi-individual-income-tax
description: >
  Prepare an ordinary individual income-tax comparison for the year 1 July 2026 to 30 June 2027. Includes pre-death income obligations and specified allowance reductions under section 47. Includes specified approved/imported pension rules; Category 2, HEPSS, other pension cases, frontier-worker treaty residence and special deductions require separate review. This source-cited draft supports preparation of reviewable working papers using the stated periods, evidence requirements and computation examples. Retain source evidence and effective dates; unresolved points and professional review remain explicit. Use the linked official materials when checking a case, and obtain a qualified local review before filing or making a payment. Read the explicit exclusions before applying its calculations to different facts.
jurisdiction: GI
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-23
version: "0.9"
verified_by: pending
sources:
  - url: "https://www.legislation.gov.uk/uksi/2010/51"
    title: "Inheritance Tax (Qualifying Non-UK Pension Schemes) Regulations 2010, revised regulations 2–7 and Schedule"
    as_of: "2026-10-22"
  - url: "https://www.gov.uk/hmrc-internal-manuals/inheritance-tax-manual/ihtm17025"
    title: "HMRC IHTM17025: identification of the section 271A regulations"
    as_of: "2026-10-22"
  - url: "https://www.gibraltar.gov.gi/income-tax-office/individuals-and-employees/self-employed"
    title: "Income Tax Office self-employed guidance: payments on account and balance payment"
    as_of: "2026-10-22"
  - url: "https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/1989s096/1989s096(01-07-24).pdf"
    title: "Rates of Tax Rules 1989, rules 2–3C; 1 July 2024 consolidation"
    as_of: "2026-10-22"
  - url: "https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/1992s016/1992s016(23-03-26).pdf"
    title: "Income Tax (Allowances, Deductions and Exemptions) Rules 1992, rules 6–6C, 16B–16F, 20A–20B, 24–24A and 29; 23 March 2026 consolidation"
    as_of: "2026-10-22"
  - url: "https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf"
    title: "Income Tax Act 2010, sections 28, 39, 64–65 and 74; Schedule 1; 23 March 2026 consolidation"
    as_of: "2026-10-22"
authored_by: Ryan Duguid
review_status: pending_review
trust_label: Accountant-authored
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Gibraltar individual income tax: ordinary assessment v0.9

> **Source-cited draft.** Professional review is pending. Figures are limited to the periods and assumptions below. This Guide prepares working papers; it is not authority to file or pay.

## Who this applies to

Prepare an ordinary individual income-tax comparison for the year 1 July 2026 to 30 June 2027. Includes specified approved/imported pension rules; Category 2, HEPSS, other pension cases, frontier-worker treaty residence and special deductions require separate review.

Sources were accessed on 22 October 2026. A dated rate table controls its stated period; an undated guidance page does not prove that all later amendments have been incorporated.

## Residence and filing intake

Section 74 defines ordinary residence using at least 183 days in a year of assessment or presence in a year within three consecutive years whose total exceeds 300 days. Any part of a day counts. Record all three years, not just the current one. Treaty residence requires a separate conclusion. [Income Tax Act 2010, s74](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf).

Collect employment, self-employment, pensions, rents, distributions, foreign-tax evidence and allowance documents. Determine the charging provision for each item before adding it to the calculation. A residence result does not establish the treatment of every income category.

## Rates, bands and thresholds

Rules 2 and 3A prescribe these ordinary full-year bands. The temporary overrides in rules 3B and 3C expressly concern 2022/23 and 2023/24; they are not the 2026/27 tables. The official index identifies the 1 July 2024 consolidation as current when checked on 22 October 2026.

| System | Marginal bands |
|---|---|
| ABS, taxable income after allowances | First £4,000: 14%; next £12,000: 17%; remainder: 39% |
| GIBS, assessable income at most £25,000 | First £10,000: 6%; next £7,000: 20%; remainder: 28% |
| GIBS, assessable income above £25,000 | First £17,000: 16%; next £8,000: 19%; next £15,000: 25%; next £65,000: 28%; remainder: 25% |

Source for every band: [Rates of Tax Rules, rules 2–3C](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/1989s096/1989s096(01-07-24).pdf), checked for the 2026/27 year. GIBS requires the prescribed election and remains subject to rule 3A. Rule 3A(3) requires the Commissioner to disregard the election described there if the ABS liability with the individual's allowances and deductions would be lower; compare completed calculations rather than choosing from headline rates.

**Partial-year limitation:** rule 3A(4) reduces the specified assessable/deemed-assessable amounts by one-twelfth for each complete calendar month without the listed Gibraltar activity. Rules 2(2) and 3A(2) additionally refer to section 34(3); that reference does not align straightforwardly with section 34 in the current Act. The interaction and exact partial-year calculation need resolution before applying full-year bands to a starter, leaver or intermittent worker. The examples below assume full-year activity.

## The base: allowances are system-specific

First establish assessable income under the charging provisions. ABS taxable income is the balance after eligible deductions; GIBS is not authority to transfer ABS allowances into a gross-income calculation. These selected statutory provisions are verified, but this is not the complete relief schedule:

| Item | Rule and amount | Conditions and period |
|---|---|---|
| ABS personal allowance | Rule 6: £3,455 | Subject to rule 20 and other restrictions; reduced by 1/12 for each complete non-resident calendar month. No rule 6 deduction under GIBS. |
| ABS minimum-deductions top-up | Rule 16C: difference between £4,343 and other deductions, if lower | A top-up, not a further £4,343 allowance. Subject to system eligibility and partial-year reduction; rule 16C retains a reference to revoked rule 25. |
| ABS low-income allowance | Rule 16B: £7,107 if income ≤£11,450; £1,300 if >£11,450 and ≤£17,500; £920 if >£17,500 and ≤£18,500; £500 if >£18,500 and ≤£19,500 | Required claim and monthly non-residence reduction apply. A provisional PAYE allowance is reconciled if final income supports a smaller allowance or none. |
| ABS tax credit | Rule 6C: statutory ceiling is the greater of £300 and 2% of tax liability | Separate from a deduction from income. PAYE calculation follows the Commissioner's tax tables; reduced for complete non-resident months. This Guide does not convert the ceiling wording into an independently verified refund entitlement. |
| GIBS approved pension contribution | Rule 24A: actual contributions up to £1,500 | Deduction from earned assessable income; scheme must be approved by the Commissioner. |

Amounts above are those in the 23 March 2026 consolidation, checked for 2026/27; [Allowances Rules, rules 6, 6A, 6C, 16B, 16C and 24A](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/1992s016/1992s016(23-03-26).pdf). Rule 6A excludes its listed ABS deductions for a GIBS elector. Rule 6B separately restricts deductions where a spouse/civil partner elects GIBS, with specific historic-claim and insurance/pension exceptions and restrictions against duplicate spouse claims. Obtain both partners' elections and claim history before calculating either person's allowance entitlement; do not automatically add two personal allowances.

For a full-year eligible ABS individual whose only other deduction is £3,455, the rule 16C top-up is £4,343 − £3,455 = **£888**, giving total deductions £4,343. If eligible other deductions already total £5,000, there is no top-up. Both examples assume no rule 6B restriction and no other adjustment; they are not final tax assessments.

### Health-insurance deductions and family-policy restrictions

For ABS, rule 20A permits a deduction for premiums or contributions payable during the assessment year to an insurance policy, scheme, society or fund **approved by the Commissioner for this rule**, providing health cover for the individual, spouse/civil partner or dependent children. The aggregate annual ceiling is **£5,395**. Rule 6A excludes this deduction for a GIBS elector; the separate rule 20B instead provides the GIBS health-insurance deduction, capped at **£3,000**, for the specified approved cover. These are deductions in calculating taxable income, not cash refunds or credits of those amounts. [Allowances Rules, rules 6A and 20A–20B, pages 16–17 and 30–31](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/1992s016/1992s016(23-03-26).pdf).

Both rules reduce the deduction otherwise allowable by **one twelfth for each complete calendar month of non-residence**. Establish the eligible premium and cap first, then reduce that deduction; do not simply reduce the cap and leave a smaller premium unreduced. For an otherwise allowable £2,400 deduction and three complete non-resident months, the result is **£2,400 × 9/12 = £1,800**. This illustration concerns the deduction alone; the Guide's unresolved partial-year rate-band issue still prevents treating it as a complete part-year tax calculation. [Rules 20A(2) and 20B(2)](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/1992s016/1992s016(23-03-26).pdf).

A spouse's or civil partner's GIBS election also requires checking rule 6B before claiming ABS health relief. Rule 6B(1) includes rule 20A in its restrictions; subsection (2) preserves specified claims for 2006/07 made and submitted by 30 June 2007. The separate exception in subsection (3) requires an otherwise eligible policy **held solely in the claimant's name and covering only that claimant**, plus the stated absence of a historic rule 20A claim by either partner in the manner described in subsection (2). A family policy is not within that self-only exception merely because one partner pays it. Retain both partners' elections, historic claims, policy ownership and covered-person details. [Rule 6B(1)–(3), pages 17–18](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/1992s016/1992s016(23-03-26).pdf).

**Boundary examples:** assuming full-year eligibility and no spouse restriction, £6,000 of qualifying premiums reaches the ABS ceiling of £5,395. Separately, assume a GIBS individual's otherwise eligible health-insurance deduction is £3,000; three complete non-resident months reduce it to £2,250. These examples do not add ABS and GIBS deductions together. Keep the approval evidence, premium schedule, covered persons, residence calendar and rule 29 claim/supporting documents. The live claim channel and case-specific approval remain to be confirmed.

```oa-check
name: Health insurance deduction cap and non-resident month reduction
inputs:
  eligible_abs_premiums: 6000
  abs_cap: 5395
  otherwise_eligible_gibs_deduction: 3000
  smaller_eligible_deduction: 2400
  complete_nonresident_months: 3
steps:
  - full_year_abs: min(eligible_abs_premiums, abs_cap)
  - part_year_gibs: otherwise_eligible_gibs_deduction * (12 - complete_nonresident_months) / 12
  - part_year_smaller_deduction: smaller_eligible_deduction * (12 - complete_nonresident_months) / 12
expected:
  full_year_abs: 5395
  part_year_gibs: 2250
  part_year_smaller_deduction: 1800
```

### Low-income exemption and taper relief

Rule 16E(1) says an individual with **gross assessable income of £11,450 or less is not subject to tax**. This is distinct from rule 16B's allowance deducted from income. Above that exemption threshold, rule 16E prescribes reductions of assessed tax in four specific ranges; it does not provide a single continuous taper covering every amount up to £19,924. [Allowances Rules, rule 16E](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/1992s016/1992s016(23-03-26).pdf).

| Gross assessable income I | L | Full taper relief T0 |
|---|---|---|
| >£11,450 and ≤£14,286 | £11,451 | £567.20 |
| >£17,500 and ≤£17,822 | £17,501 | £64.40 |
| >£18,500 and ≤£18,856 | £18,501 | £71.20 |
| >£19,500 and ≤£19,924 | £19,501 | £84.80 |

Within the applicable range, reduced taper relief is **T0 − 0.2 × (I − L)**. Deduct the resulting relief from the assessed liability, not from income. Do not fill gaps between these ranges with an invented formula or round a boundary into a different range. The statute supplies whole-pound L values; fractional-pound boundary treatment and interaction with the Commissioner's tables require confirmation for a final assessment. [Rule 16E(2)–(4)](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/1992s016/1992s016(23-03-26).pdf).

For example, at gross assessable income £17,601, relief is £64.40 − 20% × £100 = **£44.40**. At the stated upper endpoint £17,822, the formula gives **£0.20**. At £17,823 that range no longer applies; do not continue it to produce negative relief. These are relief amounts, not the person's entire tax bill.

```oa-check
name: Low-income taper inside range and at upper endpoint
inputs:
  income: 17601
  upper_endpoint: 17822
  lower_reference: 17501
  full_relief: 64.40
steps:
  - relief: full_relief - 0.2 * (income - lower_reference)
  - endpoint_relief: full_relief - 0.2 * (upper_endpoint - lower_reference)
expected:
  relief: 44.40
  endpoint_relief: 0.20
```

Rule 16F separately specifies high-income taper relief for gross assessable income **>£99,999 and ≤£103,333**, using **£1,000 − 0.3 × (I − £100,000)**. It reduces assessed liability; it is not a new marginal tax band. At £101,000 the formula gives £700. The Commissioner can issue implementation tables under both rules. This Guide has not verified the complete current table or every interaction with other credits. [Rule 16F](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/1992s016/1992s016(23-03-26).pdf).

### Computation working paper

1. Establish assessable income and classify each proposed allowance or deduction.
2. Select the correct GIBS table using assessable income. Do not treat the £25,000 switch as an additional band.
3. Apply each marginal rate only to its slice. Separately compute ABS on the reviewed taxable-income base.
4. Apply only documented credits and special adjustments after confirming eligibility. Keep a separate column for them; the examples below exclude them.
5. Compare the completed liabilities, then reconcile withholding and payments. A lower preliminary subtotal is not a final assessment.

**Arithmetic examples, before credits and with the stated bases:** GIBS gross/base £40,000 gives £2,720 + £1,520 + £3,750 = **£7,990**. ABS taxable base £20,000 gives £560 + £2,040 + £1,560 = **£4,160**. These use different assumed bases and are not a comparison for one taxpayer. At the GIBS switch, test £25,000 and £25,001 separately; do not smooth a discontinuity without a sourced adjustment.

## Deadlines and filing

Section 28(1) requires a full return by **30 November immediately following the assessment-year end**, subject to its exceptions. For the year ending 30 June 2027 this gives 30 November 2027, unless an applicable legal change or authorised extension alters it. Section 28(2)'s exclusion for foreign income relieved to nil requires the Commissioner's discretionary confirmation; a taxpayer cannot simply omit the income on that assumption. [Income Tax Act, section 28](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf).

### Payments on account and the balance

For individuals, section 39(2) bases two instalments on **50% each of the preceding assessment year's relevant tax liability**. The relevant income is Schedule 1 Table A paragraph 2 (property income) and Table B paragraph 2 (trade/business/profession/vocation income). For this calculation, the listed income is treated as charged after income subject to PAYE withholding. Do not automatically take 50% of a mixed-income taxpayer's entire prior-year tax bill. [Income Tax Act, section 39(2); Schedule 1](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf).

The instalments fall due on **31 January and 30 June within the assessment year** and are credited against the return liability. For 1 July 2026–30 June 2027, those dates are **31 January 2027 and 30 June 2027**. Section 39(1) supplies the general November payment rule, subject to its exceptions; the Income Tax Office explains that self-employed taxpayers pay the remaining balance when submitting the return, no later than **30 November**. For this year the balance deadline is therefore **30 November 2027**. A weekend adjustment is not assumed here. [Section 39(1)–(3)](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf); [Income Tax Office payment guidance](https://www.gibraltar.gov.gi/income-tax-office/individuals-and-employees/self-employed).

A taxpayer expecting the required instalments to exceed the current year's liability can apply for full or partial discharge under section 39(5). The Commissioner decides under subsection (6); an application is not itself an approved reduction. Subsection (7) applies surcharges to unpaid instalments and treats a subsequently established shortfall after a reduction claim as due on the original instalment date. Keep the claim, calculation, decision and actual payments. [Section 39(5)–(7)](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf).

**Instalment example:** assume the correctly identified preceding-year relevant liability is £6,000, with no approved reduction. Each instalment is £3,000. If final current-year liability is £7,500 and both instalments were paid, the remaining balance is **£1,500**. If final liability instead is £5,000, payments exceed it by **£1,000**, to be reconciled as a repayment position; this is not an extra negative payment instalment. Assume no other withholding, credit, surcharge or offset in either illustration.

```oa-check
name: Individual payments on account and final reconciliation
inputs:
  preceding_relevant_liability: 6000
  higher_final_liability: 7500
  lower_final_liability: 5000
steps:
  - each_instalment: preceding_relevant_liability * 0.5
  - paid: each_instalment * 2
  - balance_due: max(0, higher_final_liability - paid)
  - overpayment: max(0, paid - lower_final_liability)
expected:
  each_instalment: 3000
  balance_due: 1500
  overpayment: 1000
```

The live submission form/channel for the 2026/27 return and special assessment payment cases remain to be verified. Keep return delivery, individual tax payments and employer PAYE remittances separate. See the [payroll Guide](gi-payroll-social-insurance.md) for employer reporting. The self-employed webpage labels its allowance table 2021/22 and 2022/23; that table is not used here to establish current allowance figures.

## Approved pensions and imported-pension exceptions

Rule 3A covers pensions from a statutory scheme or provident/other fund approved by the Commissioner where the individual is **60 or over**, or meets one of the specified earlier-retirement categories. Those include the stated compulsory Pensions Act retirement, Royal Gibraltar Regiment retirement at 55 or over, and listed customs, port, fire/rescue and defence-police retirements between 55 and 60. Do not turn the list into an exemption for every retired person aged 55. [Rule 3A(1)](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/1992s016/1992s016(23-03-26).pdf).

Qualifying pension income is taxed at **0%**, subject to the section 14A exception. Other chargeable income remains separately taxable under the prescribed bands after applicable apportioned allowances/deductions. The pension rule does not exempt rental, trading or employment income merely because its recipient is retired. Verify the fund approval and individual category, not just the payer's description of the transfer. [Rule 3A(2)–(3)](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/1992s016/1992s016(23-03-26).pdf).

Section 14A instead taxes its specified imported-pension income at **2.5% insofar as it forms part of taxable income**, notwithstanding contrary provisions of the Act/allowance rules. The source must be a Commissioner-approved fund receiving the relevant funds or benefit entitlement transferred from the specified overseas pension scheme. Although subsection (2) uses European Union terminology, subsection (5) expressly defines it for this section as **the United Kingdom**. Do not extend this rule to every EU or foreign pension from the heading alone. [Section 14A(1)–(2), (5)](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf).

Approval requires irrevocably binding fund rules restricting commutation to **30%** of the relevant assets, subject to a higher/lower percentage set by the Commissioner having regard to origin-country law; preventing benefits before **55** except qualifying ill-health retirement; and restricting onward transfers to approved funds or funds containing equivalent irrevocable provisions. For ill health, the administrator needs registered-medical-practitioner evidence of inability to carry on the occupation through mental or physical illness. These are Gibraltar approval conditions, not certification of UK transfer eligibility or freedom from UK charges. [Section 14A(3)–(4)](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf).

Section 14B provides a separate 2.5% route for an approved fund conforming to the UK statutory instrument made under section 271A of the Inheritance Tax Act 1984, with its own stated fund restrictions. The referenced instrument is the **Inheritance Tax (Qualifying Non-UK Pension Schemes) Regulations 2010, SI 2010/51**: the official revised text and HMRC IHTM17025 identify its requirements. Identification of that instrument does not establish any particular fund's conformity or Gibraltar approval. [Section 14B(1)–(5)](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf).

### Section 14B: evidence for the UK scheme requirements

Use the [revised SI 2010/51](https://www.legislation.gov.uk/uksi/2010/51) when checking the cross-reference. The original 2010 PDF is an as-made text; the retrieved revised XML records a version effective from 31 December 2020. [HMRC IHTM17025](https://www.gov.uk/hmrc-internal-manuals/inheritance-tax-manual/ihtm17025) also identifies SI 2010/51 as the regulations under section 271A. This Guide checks the instrument's qualification structure, not a fund's status or UK inheritance-tax liability.

Regulation 4 provides two routes. The ordinary route requires **both** tax recognition under regulation 5 and compliance with regulation 6. The international-organisation route requires an organisation within regulation 4(2), a scheme for benefits relating to past employment with that organisation, and regulation 7. Do not replace the ordinary route with a general assertion that the scheme is regulated. [Regulations 3–4](https://www.legislation.gov.uk/uksi/2010/51/regulation/4).

For the ordinary route, prepare an evidence schedule:

| Test | Evidence and conditions |
|---|---|
| Regulation 5, Primary Condition 1 | Scheme is open to residents of its country or territory of establishment. |
| Regulation 5, Primary Condition 2 | Country has the specified personal-income-tax system providing pension relief, plus one of the statutory alternatives: no member contribution relief of the stated kind; taxable scheme income/gains **and** a Schedule-specified scheme; or taxation of all/most benefits paid to members not in serious ill-health. Tax relief includes exemption. |
| Regulation 5, Condition A or B | A: approval, recognition or registration by the relevant tax authority. B applies where no such system exists and requires local scheme residence, at least 70% of relevant scheme funds designated for lifetime income, and benefits/lump sums no earlier than pension rule 1 permits. For a deceased member the designation condition looks immediately before death. |
| Regulation 6 | The relevant local regulator regulates this occupational or non-occupational scheme. If neither regulatory route applies **solely because no such body exists**, regulation 6(4) provides its specified geographical alternative or the lifetime-income/benefit-timing alternative. Failure to obtain registration where a regulator exists is not that exception. |

Source: [regulations 5–6 and Schedule](https://www.legislation.gov.uk/uksi/2010/51). The Schedule's specified scheme is an Australian complying superannuation plan as defined there; the taxable-income/gains alternative is not open to every taxed pension fund. The geographical alternative in regulation 6(4)(a) names an EU member State, Norway, Iceland or Liechtenstein; do not read the as-made phrase “another member State” as proof that Gibraltar qualifies. Regulation 7 separately imposes the 70% lifetime-income and pension-rule-1 timing requirements on the international-organisation route. [Regulation 7](https://www.legislation.gov.uk/uksi/2010/51/regulation/7).

The **70% test is route-specific**, rather than a universal stand-alone certification of QNUPS status. It uses “relevant scheme funds” as defined in regulation 2, not automatically every asset in a member's pension portfolio. Where pension rule 1 is incorporated, verify its applicable version and any relevant protection before selecting a benefit date; Gibraltar's domestic age-55 condition alone does not resolve that UK cross-reference. Keep the scheme's establishment, tax recognition, regulation, rules and chosen statutory route on file. Actual scheme conformity, Gibraltar section 14B approval, UK transfer eligibility/charges and inheritance-tax consequences remain separate determinations.

**Computation example:** assume an individual's established taxable amount within section 14A is £20,000. Tax on that component is **£20,000 × 2.5% = £500**. If a different £20,000 pension satisfies rule 3A and is outside the overriding imported-pension provisions, its rule 3A tax is £0. These are alternative classifications; the taxpayer cannot elect the cheaper result simply by describing the same pension differently. Neither figure is the person's total tax bill.

```oa-check
name: Gibraltar approved versus imported pension component
inputs:
  established_taxable_pension_component: 20000
steps:
  - section_14a_component_tax: established_taxable_pension_component * 0.025
  - qualifying_rule_3a_component_tax: established_taxable_pension_component * 0
expected:
  section_14a_component_tax: 500
  qualifying_rule_3a_component_tax: 0
```

Keep approval evidence, scheme rules, origin and transfer history, age/retirement evidence, any commutation variation and the taxable-income calculation. Actual lump-sum treatment, amounts outside these provisions, UK transfer restrictions, approval/claim channels and treaty interactions require separate verification. See the [UK employment and pensions treaty Guide](gi-uk-employment-pensions-treaty.md); a domestic rate does not settle treaty allocation.

## Death during the tax year

Section 47 transfers the deceased individual's rights, duties and tax liabilities concerning **income arising before death** to the executor, subject to its assessment limit. Tax payable by the executor under that section is a debt payable out of the deceased's estate. The section does not by itself classify income arising to the estate after death or establish inheritance-tax treatment. Separate pre-death income from later estate income and retain the executor's authority. [Section 47(1)](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf).

An assessment or additional assessment on that pre-death income must not be made later than the **end of the third year of assessment following the year in which death occurred**. This is not a three-year anniversary measured from the death date, nor a three-year extension for submitting every return. Keep ordinary return, payment, appeal and refund deadlines separately. [Section 47(2)](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf).

**Assessment-period example:** a death on 15 October 2026 falls in the year ending 30 June 2027. The three following years end on 30 June 2028, 2029 and 2030, so the section 47(2) endpoint is **30 June 2030**. This does not say that an existing tax debt disappears on that date or that no return is required until then.

Section 47(3) reduces deductions allowable under **rules 6–19** of the Income Tax (Allowances, Deductions and Exemptions) Rules 1992 by **one twelfth for each complete calendar month** by which death precedes the assessment-year end. Check the particular deduction's legal basis and eligibility first. Do not extend this specific cross-reference to every relief, calculate a daily fraction, or apply it as a reduction of gross income under both tax systems. [Section 47(3)](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf).

**Allowance example:** assume a deduction within that rule range has an otherwise established annual amount of £6,000. For death on 15 October in a year ending the following 30 June, November–June gives eight complete calendar months. The reduction is **£6,000 × 8/12 = £4,000**, leaving **£2,000**. For death on 15 June, there are no complete calendar months before 30 June and this particular reduction is zero. The £6,000 is an illustrative input, not a published allowance amount.

```oa-check
name: Gibraltar specified deduction reduction after death
inputs:
  otherwise_allowable_annual_deduction: 6000
  complete_months_october_case: 8
  complete_months_june_case: 0
steps:
  - october_reduction: otherwise_allowable_annual_deduction * complete_months_october_case / 12
  - october_remaining: otherwise_allowable_annual_deduction - october_reduction
  - june_reduction: otherwise_allowable_annual_deduction * complete_months_june_case / 12
expected:
  october_reduction: 4000
  october_remaining: 2000
  june_reduction: 0
```

Recommended records: death date, executor authority, income cut-off, year-by-year assessments/payments, each deduction's governing rule and complete-month computation. Notification and final-return channels, post-death estate income and treatment of each specialised deduction still require verification. See [assessment appeals and refund claims](gi-income-tax-assessment-appeals.md) for the separate procedural clocks; no estate-wide tax clearance is established by this section.

## Penalties and interest

For failure to complete and deliver a section 28 return, section 65 provides **£50**, a further **£300** if failure continues after three months beginning with the filing date, and another **£500** after six months. All three amount to **£850**, not £500 total. The Commissioner can set aside one or more penalties if satisfied a reasonable excuse existed throughout the default; relief is not automatic. [Section 65(1), (2), (4)–(5)](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf).

Section 64 imposes a **10%** surcharge on tax unpaid on the day after its due date. If the tax and first surcharge remain unpaid at the statutory 90-day point, a further **20% of the outstanding tax and surcharge** becomes due. With £1,000 wholly unpaid throughout, the first surcharge is £100, then £220, leaving **£1,320**; it is not a flat 30% addition to principal. Establish the actual payment due date and any payments before using this example. Appeal/postponement rules are addressed in the [assessment and appeals Guide](gi-income-tax-assessment-appeals.md). [Section 64](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf).

These are return and payment provisions, not an exhaustive account of incorrect-return, notice, fraud or criminal penalties. No interest rate is asserted here.

## Cross-border points

Ordinary residence, source of income and treaty residence are separate determinations. Rule 3 generally specifies **17% on the first £16,000 of taxable income and 39% on the remainder** for non-resident individuals, subject to GIBS and its express exclusions. It excludes persons covered by Allowances Rules 24(1), which concerns non-residents receiving a Gibraltar-accruing pension. Rule 24(2)–(3) limits that relief by reference to total worldwide income and specifies treatment of foreign-tax relief. Do not apply the ordinary resident ABS table or full personal allowances to every frontier worker. [Rates Rules, rule 3](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/1989s096/1989s096(01-07-24).pdf); [Allowances Rules, rule 24](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/1992s016/1992s016(23-03-26).pdf).

Treaty eligibility, pension exemptions, employment-location allocation and foreign relief require separate conclusions; see the [foreign-tax relief Guide](gi-foreign-tax-relief.md). These rules alone do not resolve a Spain–Gibraltar residence case.

### Non-resident pensioner relief: worldwide-income limit

Rule 24(1) permits a **non-resident individual receiving a pension accruing in Gibraltar** to claim the deductions, allowances and reliefs in rules 6–21 as if resident throughout the assessment year, subject to the Rules and the limit below. It does not grant that treatment to every non-resident employee or make a pension taxable where an exemption or treaty excludes it. Establish pension source, chargeability, system eligibility and each relief's conditions before applying the limit. [Allowances Rules, rule 24(1)](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/1992s016/1992s016(23-03-26).pdf).

For the rule 24(2) comparison, record **W**, total income from all sources including income outside Gibraltar's tax charge; **G**, income subject to the Gibraltar tax charge; and **H**, the hypothetical tax if total worldwide income were chargeable. The permitted relief cannot reduce the amount payable below **H × G / W**. Compute both actual and hypothetical tax **without foreign-tax relief** for this comparison, as rule 24(3) requires. This is a restriction on the specified relief, not a separate charge on otherwise exempt foreign income. Do not use the foreign country's tax bill as H or subtract a foreign credit before testing the floor. Foreign-tax relief needs its separate legal analysis. [Rule 24(2)–(3)](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/1992s016/1992s016(23-03-26).pdf).

**Illustrative comparison:** assume W = £50,000, G = £20,000 and an independently established hypothetical tax H = £10,000. The floor is £4,000. If the otherwise calculated liability after the claimed relief is £3,000, relief must be restricted by £1,000 to leave £4,000 before foreign-tax relief. If that liability is £5,000, the floor requires no adjustment. These assumed tax amounts illustrate the restriction; they are not computed liabilities for a particular pensioner, approved pension or tax system. With W = 0, do not divide by zero or invent a liability; revisit the charging and income facts.

```oa-check
name: Non-resident pensioner worldwide-income relief floor
inputs:
  worldwide_income: 50000
  chargeable_income: 20000
  hypothetical_worldwide_tax: 10000
  liability_below_floor: 3000
  liability_above_floor: 5000
steps:
  - floor: hypothetical_worldwide_tax * chargeable_income / worldwide_income
  - restriction_below: max(0, floor - liability_below_floor)
  - restricted_liability: liability_below_floor + restriction_below
  - restriction_above: max(0, floor - liability_above_floor)
expected:
  floor: 4000
  restriction_below: 1000
  restricted_liability: 4000
  restriction_above: 0
```

Rule 29 requires a claim in a return on the proper form, or another form and manner prescribed by the Commissioner, with the particulars and supporting proof required. Record worldwide income evidence, the Gibraltar-source pension, each relief claimed, both tax computations and the separate foreign-credit analysis. A working-paper calculation is not a submitted claim; the current form, channel and any case-specific evidence request remain to be verified. [Rule 29](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/1992s016/1992s016(23-03-26).pdf).

## Two worked examples that recompute

**Example 1: full-year GIBS before other adjustments.** With established assessable income £40,000, the higher-income table gives £17,000 × 16% + £8,000 × 19% + £15,000 × 25% = **£7,990**. This assumes the election and full-year treatment apply; no additional deduction or credit is assumed.

```oa-check
name: Full-year GIBS income 40000
inputs:
  income: 40000
steps:
  - first: min(income, 17000) * 0.16
  - second: min(max(income - 17000, 0), 8000) * 0.19
  - third: min(max(income - 25000, 0), 15000) * 0.25
  - fourth: min(max(income - 40000, 0), 65000) * 0.28
  - remainder: max(income - 105000, 0) * 0.25
  - tax: first + second + third + fourth + remainder
expected:
  tax: 7990
```

**Example 2: full-year ABS top-up and tax before credit.** Assume £24,343 assessable income, only the £3,455 personal deduction, full eligibility for the £888 top-up and no other deductions. Taxable income is £20,000; tax before the separately determined rule 6C credit is **£4,160**. This is a different taxpayer/base from Example 1, not an ABS-versus-GIBS comparison for one person.

```oa-check
name: ABS minimum deduction top-up and pre-credit liability
inputs:
  assessable: 24343
  personal: 3455
  minimum_deductions: 4343
steps:
  - topup: max(0, minimum_deductions - personal)
  - taxable: max(0, assessable - personal - topup)
  - first: min(taxable, 4000) * 0.14
  - second: min(max(taxable - 4000, 0), 12000) * 0.17
  - remainder: max(taxable - 16000, 0) * 0.39
  - tax_before_credit: first + second + remainder
expected:
  topup: 888
  taxable: 20000
  tax_before_credit: 4160
```

## Ask the client first

1. Which days were spent in Gibraltar across the relevant three years, and which complete months had no Gibraltar work/activity?
2. What income arose by category and location, and what tax was withheld or paid abroad?
3. Which system was elected by the taxpayer and spouse/civil partner, and what earlier claims or approvals exist?
4. What documents support each allowance, approved pension contribution and credit?
5. Are there special-status certificates, pensions, a return notice, an extension or an outstanding assessment?

## Sources and remaining verification

Primary legislation and [self-employed payment guidance](https://www.gibraltar.gov.gi/income-tax-office/individuals-and-employees/self-employed) read on **22 October 2026**: [Income Tax Act](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf), [Rates of Tax Rules](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/1989s096/1989s096(01-07-24).pdf), [Allowances Rules](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/1992s016/1992s016(23-03-26).pdf). Frontmatter records the same versions. Remaining work includes the complete relief schedule and GIBS deductions, current submission and payment channels, special assessment dates, the partial-year cross-reference, exact credit application, special regimes and independent source/professional review. The dates on the legislation index are evidence of the displayed consolidation, not a guarantee against later amendments.

## Self-checks and output

- Retain the relevant source version, the applicable period and the facts establishing scope.
- Reconcile every input to the client's records; keep estimates separate from actual amounts.
- Recompute the example and boundary cases before applying the method.
- Record exclusions and unresolved points explicitly. Do not convert a missing source into an exemption.
- Deliver a calculation, evidence list, filing calendar and reviewer questions. Record the exact revision reviewed.

## Disclaimer

General tax and accounting reference material only. These drafts have not been professionally attested. A qualified professional in the relevant jurisdiction must check the facts, current law, elections and deadlines before anyone files, pays or acts on an output.

> Contributed by Ryan Duguid.

<!-- openaccountants-cta-block -->

---

## Talk to an accountant

Find the current Guide and professional-review status at [OpenAccountants](https://www.openaccountants.com).
