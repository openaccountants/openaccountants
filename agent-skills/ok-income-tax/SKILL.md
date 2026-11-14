---
name: ok-income-tax
description: "Compute Oklahoma 2026 resident Form 511 income tax, including sole proprietors and disregarded LLCs. Covers 0%/2.5%/3.5%/4.5% schedules, state deductions/exemptions, corrected federal-tax-paid prohibition, adjustments, credits and estimated payments. Trigger on OK Form 511, Oklahoma resident income or state self-employment return."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/ok-income-tax"
  jurisdiction: "US-OK"
  tax_year: "2026"
  last_updated: "2026-11-13"
---

# Oklahoma resident individual income tax, tax year 2026

> **Source-cited draft.** Written by Codex. Not reviewed by an accountant. This skill supports a professional working paper; review the taxpayer facts and current forms before filing. Circular 230 section 10.37: this material is not a legal opinion or a substitute for reasonable factual and legal inquiry.

**Answer first.** Oklahoma’s 2026 income schedule has a zero band and three positive rates ending at 4.5%. Start with federal AGI, apply Oklahoma modifications and state deductions/exemptions, and never deduct federal income tax paid.

## Scope and who this is for

Full-year Oklahoma resident individuals, including sole proprietors and disregarded single-member LLCs. `us-schedule-c-and-se-computation` owns the federal business and self-employment calculation; `us-federal-return-assembly` owns federal assembly. Published 2026 legislation and electronic-filing specifications establish the new rates and deductions. Detailed exclusions, credits and return-line mechanics below use the explicitly labeled **2025-2026 filing cycle** Form 511 packet until the final 2026 packet is confirmed.

## Ask the client first

1. What domicile, moves, filing status, spouse residency, dependents, age and blindness facts apply?
2. What completed federal AGI, Schedule C/SE and Schedule A amounts support the state starting point and deduction method?
3. What bond interest, Social Security, military/civil-service/other retirement, out-of-state business/property income and state-specific adjustments exist?
4. What depreciation, section 179, Oklahoma NOL, asset elections and conformity adjustments carry forward?
5. What credit eligibility, household income, federal credit worksheets, other-state returns and withholding/estimate/extension payments exist?

## The method, step by step

### Rates, bands and thresholds

| Item and conditions | Amount / treatment | Official source |
| --- | --- | --- |
| 2026 single/MFS: first $3,750 | 0% | [HB 2764, section 2, 68 O.S.2355(D)](https://www.oklegislature.gov/cf_pdf/2025-26%20ENR/hB/HB2764%20ENR.PDF) |
| Single/MFS: over $3,750 to $4,900 | 2.5% excess over $3,750 | [HB 2764, section 2, 68 O.S.2355(D)](https://www.oklegislature.gov/cf_pdf/2025-26%20ENR/hB/HB2764%20ENR.PDF) |
| Single/MFS: over $4,900 to $7,200 | $28.75 + 3.5% excess over $4,900 | [HB 2764, section 2, 68 O.S.2355(D)](https://www.oklegislature.gov/cf_pdf/2025-26%20ENR/hB/HB2764%20ENR.PDF) |
| Single/MFS: over $7,200 | $109.25 + 4.5% excess over $7,200 | [HB 2764, section 2, 68 O.S.2355(D)](https://www.oklegislature.gov/cf_pdf/2025-26%20ENR/hB/HB2764%20ENR.PDF) |
| 2026 joint/HOH/qualifying surviving spouse: first $7,500 | 0% | [HB 2764, section 2, 68 O.S.2355(D)](https://www.oklegislature.gov/cf_pdf/2025-26%20ENR/hB/HB2764%20ENR.PDF) |
| Joint/HOH/QSS: over $7,500 to $9,800 | 2.5% excess over $7,500 | [HB 2764, section 2, 68 O.S.2355(D)](https://www.oklegislature.gov/cf_pdf/2025-26%20ENR/hB/HB2764%20ENR.PDF) |
| Joint/HOH/QSS: over $9,800 to $14,400 | $57.50 + 3.5% excess over $9,800 | [HB 2764, section 2, 68 O.S.2355(D)](https://www.oklegislature.gov/cf_pdf/2025-26%20ENR/hB/HB2764%20ENR.PDF) |
| Joint/HOH/QSS: over $14,400 | $218.50 + 4.5% excess over $14,400 | [HB 2764, section 2, 68 O.S.2355(D)](https://www.oklegislature.gov/cf_pdf/2025-26%20ENR/hB/HB2764%20ENR.PDF) |
| 2026 state standard deduction | Single/MFS $6,350; joint/QSS $12,700; HOH $9,350 | [Appendix B](https://oklahoma.gov/content/dam/ok/en/tax/documents/resources/publications/software-developers/2026MeFDeveloperGuide.pdf) |
| 2026 personal exemption | $1,000 per qualifying exemption; dependent/age/blind conditions apply | [2026 annual report p.1](https://oklahoma.gov/content/dam/ok/en/tax/documents/resources/reports/annual-reports/otc/AR-2026.pdf) |
| State itemized deduction limit | $17,000 other eligible deductions, plus eligible medical and charity outside that cap; state/local income OR sales taxes removed | [Appendix B](https://oklahoma.gov/content/dam/ok/en/tax/documents/resources/publications/software-developers/2026MeFDeveloperGuide.pdf) |
| Federal income taxes paid | No deduction; Schedule 511-D is itemized deductions, not a federal-tax-paid optimizer | [HB 2764, section 2, 68 O.S.2355(D)](https://www.oklegislature.gov/cf_pdf/2025-26%20ENR/hB/HB2764%20ENR.PDF) |
| Estimates trigger and ordinary safe harbor | $500 or more tax above withholding and withholding below smaller of 70% current liability or 100% prior 12-month liability | [official text](https://oklahoma.gov/tax/individuals/pay-taxes.html) |

### Establish the resident return and income base

1. Establish domicile and status. The Form 511 packet defines a full-year resident by Oklahoma domicile for the entire year; it does not establish the former automatic “more than seven months” residence shortcut. Nonresident/part-year cases use **Form 511-NR**, not a fictitious Schedule 511-NR attached to a resident return. Mixed-residency spouses can require special allocation or elections. Source: [2025-2026 filing cycle pp.3,7-9](https://oklahoma.gov/content/dam/ok/en/tax/documents/forms/individuals/current/511-Pkt.pdf).
2. Start from final **federal AGI**, not federal taxable income. Federal self-employment adjustments already reflected in AGI flow through once; do not deduct them again. Federal QBI is below AGI, so do not invent an Oklahoma AGI add-back for a deduction absent from AGI. Resolve state depreciation/section 179 and other conformity adjustments separately instead of assuming every federal change flows through. Sources: [Form 511 line 1 and Schedules A-C](https://oklahoma.gov/content/dam/ok/en/tax/documents/forms/individuals/current/511-Pkt.pdf); federal owners above.
3. Reconcile Oklahoma subtractions, additions and adjustments in a working paper. The prior-cycle packet separately subtracts federally taxed Social Security, permits military retirement exclusion and conditional qualifying retirement exclusions, and adds non-Oklahoma state/local bond interest where required. Do not treat every retirement distribution as eligible: early distributions and plan-specific restrictions matter. Remove state/local income or sales taxes from the **itemized deduction**, rather than adding that Schedule A amount to AGI a second time. Source: [pp.9-10,16-25; 2025-2026 filing cycle](https://oklahoma.gov/content/dam/ok/en/tax/documents/forms/individuals/current/511-Pkt.pdf).
4. Separate out-of-state real/tangible property and business income from wages/personal services. The prior-cycle line 4 subtraction does not simply exempt all out-of-state earnings; wages may instead require the other-state-tax credit and an allocation of deductions/exemptions. Source: [line 4, line 16 and Schedule 511-E; 2025-2026 filing cycle](https://oklahoma.gov/content/dam/ok/en/tax/documents/forms/individuals/current/511-Pkt.pdf).

### Deduction, exemptions and 2026 schedule

5. Follow the **federal deduction method**: federal standard means Oklahoma standard; federal itemized means Oklahoma itemized. This is not a free comparison/election. For itemizers, start from federal Schedule A, remove the state/local income or sales tax actually included in the allowed federal total, isolate eligible medical and charitable amounts, cap the remaining eligible deductions at $17,000, then add medical/charity back. Special out-of-state allocations still apply. Source: [Appendix B](https://oklahoma.gov/content/dam/ok/en/tax/documents/resources/publications/software-developers/2026MeFDeveloperGuide.pdf).
6. Subtract the qualifying $1,000 exemptions and clamp taxable income at zero. A person claimable as a dependent cannot automatically claim a personal exemption for themselves; qualifying dependents, spouse, age and blindness conditions are separate. Additional age exemptions have income limits in the prior-cycle packet. Sources: [2026 report p.1](https://oklahoma.gov/content/dam/ok/en/tax/documents/resources/reports/annual-reports/otc/AR-2026.pdf), [pp.8-10; 2025-2026 filing cycle](https://oklahoma.gov/content/dam/ok/en/tax/documents/forms/individuals/current/511-Pkt.pdf).
7. Apply the 2026 schedule for the correct status. The single rate-schedule formula is 2.5% x min(max(T - 3,750,0),1,150) + 3.5% x min(max(T - 4,900,0),2,300) + 4.5% x max(T - 7,200,0). Double the thresholds and slice widths for joint/HOH/QSS. Use the final year’s prescribed tax table when required; the examples below are schedule computations. Source: [HB 2764, section 2, 68 O.S.2355(D)](https://www.oklegislature.gov/cf_pdf/2025-26%20ENR/hB/HB2764%20ENR.PDF), [2026 bracket table p.6](https://oklahoma.gov/content/dam/ok/en/tax/documents/resources/publications/legislation/2025LegislativeUpdate.pdf).

**Source reconciliation:** the 2026 MeF appendix’s joint 3.5% row prints an “over $4,900” entry. The enrolled law gives a zero first $7,500 and next $2,300 at 2.5%, so that band starts at **$9,800**, as OTC’s legislative table confirms: (9,800 - 7,500) x 2.5% = **$57.50**, then $57.50 + (14,400 - 9,800) x 3.5% = **$218.50**. Use $9,800, not the inconsistent software-publication entry. Sources: [HB 2764, section 2, 68 O.S.2355(D)](https://www.oklegislature.gov/cf_pdf/2025-26%20ENR/hB/HB2764%20ENR.PDF), [official text](https://oklahoma.gov/content/dam/ok/en/tax/documents/resources/publications/legislation/2025LegislativeUpdate.pdf), [official text](https://oklahoma.gov/content/dam/ok/en/tax/documents/resources/publications/software-developers/2026MeFDeveloperGuide.pdf).

### Credits and payments

The **2025-2026 filing cycle** packet places the earned-income credit with refundable credits/payments, and computes 5% of a specially reconstructed federal credit under the 2020 requirements, with state proration. The old blanket “5% of current federal EITC, nonrefundable” is incorrect. Use the applicable 511-EIC worksheet; federal eligibility/amounts remain with the federal owner. The packet also has a child care/child tax credit, contrary to the former claim that none exists: for eligible federal AGI at or below $100,000, it uses the greater of 20% of eligible federal child-care credit or 5% of federal child/additional child credit, subject to state proration and tax limits. These credit mechanics require final 2026 confirmation. Source: [pp.11,15 and Schedules F-G](https://oklahoma.gov/content/dam/ok/en/tax/documents/forms/individuals/current/511-Pkt.pdf).

Form 538-S sales-tax relief is a separate income/household eligibility computation, not an automatic result of a grocery purchase. The prior-cycle packet uses full-year residence and gross household income, with exceptions for dependents, age and disability, plus benefit/institution exclusions. Keep it for screening and confirm the final year’s limits. Source: [p.15 and 538-S; 2025-2026 filing cycle](https://oklahoma.gov/content/dam/ok/en/tax/documents/forms/individuals/current/511-Pkt.pdf).

Do not use the old $54,670/0.00056 “federal deduction cap,” payment-timing rule or optimizer. The enacted 2026 law expressly prohibits a deduction for federal income taxes paid. **Schedule 511-D calculates Oklahoma itemized deductions.** Sources: [HB 2764, section 2, 68 O.S.2355(D)](https://www.oklegislature.gov/cf_pdf/2025-26%20ENR/hB/HB2764%20ENR.PDF), [Appendix B](https://oklahoma.gov/content/dam/ok/en/tax/documents/resources/publications/software-developers/2026MeFDeveloperGuide.pdf).

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Taxable income in zero band | Income tax can be zero; filing requirement still depends on gross income and other obligations. |
| Federal itemizer | Must use state itemized method; state cap and SALT removal still apply. |
| Social Security/military/other retirement | Preserve separate eligibility tests and amounts included in AGI; do not subtract untaxed amounts. |
| Out-of-state business/property versus wages | Separate subtraction, credit and deduction allocation rules. |
| Nonresident/part-year or mixed-residency couple | Use 511-NR or the specified spouse allocation/election; refer beyond this full-year case. |
| Future revenue-trigger reduction | Not automatic for 2026. HB 2764 requires certification and later effective dates; do not project another cut. |
| Credit/conformity or depreciation not established | Hold the final computation until the final 2026 rule/form is confirmed. |

Sources: [HB 2764, section 2, 68 O.S.2355(D)](https://www.oklegislature.gov/cf_pdf/2025-26%20ENR/hB/HB2764%20ENR.PDF), [official text](https://oklahoma.gov/content/dam/ok/en/tax/documents/resources/publications/software-developers/2026MeFDeveloperGuide.pdf), [2025-2026 filing cycle](https://oklahoma.gov/content/dam/ok/en/tax/documents/forms/individuals/current/511-Pkt.pdf).

## Worked cases

**Case 1.** A single resident with final Oklahoma AGI $107,350, federal/state standard method, one qualifying exemption and no credits has taxable income $107,350 - $6,350 - $1,000 = **$100,000**. Rate-schedule tax is $109.25 + 4.5% x $92,800 = **$4,285.25**, or $4,285 when the return rounds to whole dollars. No federal income-tax-paid deduction is allowed.

```oa-check
name: OK2026 resident single schedule
inputs:
  ok_agi: 107350
  deduction: 6350
  exemption: 1000
steps:
- taxable: max(ok_agi-deduction-exemption,0)
- tax: min(max(taxable-3750,0),1150)*0.025 + min(max(taxable-4900,0),2300)*0.035 + max(taxable-7200,0)*0.045
- return_tax: floor(tax+0.5)
expected:
  taxable: 100000
  tax: 4285.25
  return_tax: 4285
```

**Case 2, method decision.** A federal itemizer has $30,000 Schedule A deductions including $6,000 allowed SALT, $2,000 medical and $4,000 charity. Other eligible state deductions are $18,000, capped at $17,000; state itemized total is **$23,000**. If otherwise identical single taxpayers used the federal standard method instead, the state method would be the **$6,350** standard. This shows both method branches; taxpayers cannot switch state methods merely to get a larger deduction.

```oa-check
name: OK2026 deduction-method decision
inputs:
  federal_itemized: 30000
  salt: 6000
  medical: 2000
  charity: 4000
  state_standard: 6350
steps:
- other: federal_itemized-salt-medical-charity
- itemized_branch: min(other,17000)+medical+charity
- standard_branch: state_standard
expected:
  other: 18000
  itemized_branch: 23000
  standard_branch: 6350
```


## When to refuse or refer

Refer nonresident/part-year, mixed-status spouses, uncertain domicile, tribal exclusions, special retirement, capital-gain/NOL, depreciation and conformity, unconfirmed credits, audit and penalty matters. Do not use the former federal-tax-paid method at all.

## Filing and payment

Use the final 2026 Form 511 and required schedules with the federal return and supporting evidence; retain state acceptance and payment confirmation. The published 2026 MeF specifications confirm resident 511/nonresident 511-NR, credit attachments and whole-dollar entries. Detailed prior-cycle mapping is: line 1 federal AGI; line 2 Schedule A subtractions; line 4 eligible out-of-state income; line 6 Schedule B additions; line 8 Schedule C adjustments; lines 10-12 deductions/exemptions; line 13 taxable income; line 14a tax. This replaces the incorrect former map, but is labeled **2025-2026 filing cycle** until final 2026 forms are read. Sources: [official text](https://oklahoma.gov/content/dam/ok/en/tax/documents/resources/publications/software-developers/2026MeFDeveloperGuide.pdf), [official text](https://oklahoma.gov/content/dam/ok/en/tax/documents/forms/individuals/current/511-Pkt.pdf).

The ordinary individual due date is April 15 after year-end; final 2026 filing-season electronic concessions/calendar notices are pending. Pay through OkTAP or the appropriate 511-V voucher. Make estimates where the published $500/70%-or-prior-year test applies; farming exceptions and annualization require their own worksheet. The OTC pay page states 5% delinquent penalty when less than 90% was paid by the original date, and 1.25% monthly interest on unpaid tax; an extension does not make an unpaid balance interest-free. Source: [official text](https://oklahoma.gov/tax/individuals/pay-taxes.html).

## Completion checklist

- Establish status/domicile and tie federal AGI once.
- Reconcile each state addition/subtraction and deduction method.
- Apply the correct 2026 schedule and final prescribed tax table.
- Verify current credits/conformity, reconcile payments and retain acknowledgments.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Enrolled HB 2764 section 2. Read for 68 O.S.2355(D)-(F), actual 2026 rate slices, prohibition of federal-tax-paid deduction and future certification. | https://www.oklegislature.gov/cf_pdf/2025-26%20ENR/hB/HB2764%20ENR.PDF | 2026-11-13 |
| OTC 2025 legislative update. Read for p.6, 2026 thresholds and joint 3.5% band over $9,800. | https://oklahoma.gov/content/dam/ok/en/tax/documents/resources/publications/legislation/2025LegislativeUpdate.pdf | 2026-11-13 |
| OTC 2026 MeF publication. Read for 2026 accepted forms, whole-dollar entries and Appendices A-C deductions, filing requirements and schedules; joint row inconsistency reconciled above. | https://oklahoma.gov/content/dam/ok/en/tax/documents/resources/publications/software-developers/2026MeFDeveloperGuide.pdf | 2026-11-13 |
| OTC FY2026 annual report. Read for p.1, actual 2026 rates, deductions, $1,000 personal exemption and corporate rate. | https://oklahoma.gov/content/dam/ok/en/tax/documents/resources/reports/annual-reports/otc/AR-2026.pdf | 2026-11-13 |
| OTC Form 511 packet. Read for 2025-2026 filing cycle pp.3,7-11,15-25 and forms: domicile, AGI modifications, retirement, deduction method, correct line map, credits and allocation. | https://oklahoma.gov/content/dam/ok/en/tax/documents/forms/individuals/current/511-Pkt.pdf | 2026-11-13 |
| OTC pay taxes. Read for estimates $500/70%-or-prior-year test, payments, delinquency and interest; its 2025 rate table is not used for 2026. | https://oklahoma.gov/tax/individuals/pay-taxes.html | 2026-11-13 |

Not yet confirmed: Final 2026 Form 511/511-NR packets, prescribed tax-table bands, credit worksheets/limits and filing-season concessions; exact 2026 conformity for section 179/bonus/other federal changes; special age-exemption limits, detailed retirement and capital-gain/NOL eligibility, Form 538-S household limits/exclusions and mixed-state allocation. Prior-cycle $10,000 qualifying retirement exclusion and full military/Social Security exclusions are preserved as screening topics, not asserted as final 2026 determinations. The old seven-month residence test and federal-tax-paid deduction are withdrawn, not pending alternatives.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `ok-income-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/ok-income-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
