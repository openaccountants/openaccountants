---
name: pe-tax-credits
description: "Prince Edward Island 2026 credit decisions: family reduction, refundable volunteer credit, child-wellness base, amended community-equity certificate and annual-claim limits, Island Essentials Benefit and pre-commitment Labour Rebate."
jurisdiction: CA
tax_year: 2026
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
version: "2.0"
category: international
type: situation-rules
---

# Prince Edward Island tax credits v2.0

## Scope

Decide and compute Prince Edward Island credits for **calendar 2026**, in CAD, distinguishing non-refundable tax, refundable volunteer tax credit, separate quarterly benefits and discretionary labour assistance. This complements `pe-individual-return`; current law controls where the 2015 programme overview or old payroll presentation differs. No accountant approval is claimed.

### Quick reference

| Item | Figure and conditions | Official source |
|---|---|---|
| 2026 basic personal base | CAD 15,000; ordinary non-refundable credit at 9.5%; not a CAD 15,000 tax exemption for all income types | https://www.princeedwardisland.ca/sites/default/files/0432/I-01-Income%20Tax%20Act_1.pdf |
| 2026 spouse / eligible-dependant maximum | CAD 12,740 subject to status/support and the person's net income; CAD 1,274 income offset in statutory formula; not equal to the BPA | https://www.princeedwardisland.ca/sites/default/files/0432/I-01-Income%20Tax%20Act_1.pdf |
| 2026 age amount | Maximum CAD 6,510 base for qualifying age 65; reduce base by 15% of eligible income above CAD 36,600; convert at 9.5% | https://www.princeedwardisland.ca/sites/default/files/0432/I-01-Income%20Tax%20Act_1.pdf |
| 2026 pension / disability | Pension eligible base maximum CAD 1,000; certified adult disability base CAD 6,890 with separate child-supplement rules; non-refundable | https://www.princeedwardisland.ca/sites/default/files/0432/I-01-Income%20Tax%20Act_1.pdf |
| 2026 donation credit | 9.5% on first CAD 200 of qualifying gifts; 20% on eligible excess, subject to statutory gift conditions | https://www.princeedwardisland.ca/sites/default/files/0432/I-01-Income%20Tax%20Act_1.pdf |
| 2026 LITR | CAD 350 basic + CAD 350 spouse OR eligible dependant + CAD 300 each OTHER qualifying child + CAD 250 for each eligible senior spouse; less 5% of adjusted family income above CAD 23,000; non-refundable, authorised unused-spouse transfer | https://www.princeedwardisland.ca/sites/default/files/0432/I-01-Income%20Tax%20Act_1.pdf |
| Current volunteer credit | CAD 1,000 refundable dollar credit; federal firefighter/SAR eligibility required and no volunteer-services income exemption elected; qualifying residence/death rules apply | https://www.princeedwardisland.ca/sites/default/files/0432/I-01-Income%20Tax%20Act_1.pdf |
| 2026 children's wellness | Eligible shared expense base up to CAD 1,000 per qualifying child, under 18 at beginning of year; at 9.5%, derived maximum non-refundable credit CAD 95; programme and duplication tests apply | https://www.princeedwardisland.ca/sites/default/files/0432/I-01-Income%20Tax%20Act_1.pdf |
| PEI HST | 15% on ordinary taxable supplies whose place of supply is PEI; supply classification and exceptions first | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/charge-collect-place-supply.html |

| Item | Figure and conditions | Official source |
|---|---|---|
| Community-development equity certificate | 35% of eligible investment in a registered specified issue; actual Minister certificate required; cumulative certificate-entitlement cap CAD 56,000 from 1 January 2022 | https://www.princeedwardisland.ca/sites/default/files/legislation/c-13-01-community_development_equity_tax_credit_act.pdf |
| Annual income-tax claim | Maximum CAD 7,000 credit including carryovers claimed that year; limited by PEI tax; non-refundable | https://www.princeedwardisland.ca/sites/default/files/0432/I-01-Income%20Tax%20Act_1.pdf |
| Unused eligible credit | Three-year carryback, not before 2011, or seven-year carryforward, subject to applicable-year claim cap and no double use | https://www.princeedwardisland.ca/sites/default/files/0432/I-01-Income%20Tax%20Act_1.pdf |
| Holding condition | Five years from specified-issue registration date; early disposal subject to repayment and exact statutory/regulatory exceptions, not a blanket four-year investment-date rule | https://www.princeedwardisland.ca/sites/default/files/legislation/c-13-01-community_development_equity_tax_credit_act.pdf |
| Return deadline for this deduction | File the relevant return within three years after the taxation year ends; a generic adjustment facility does not waive it | https://www.princeedwardisland.ca/sites/default/files/0432/I-01-Income%20Tax%20Act_1.pdf |

| Item | Figure and conditions | Official source |
|---|---|---|
| PEI Labour Rebate | Up to 25% of approved incremental eligible full-time wages; application before any legal/financial project commitment; discretionary, not an automatic tax refund | https://www.princeedwardisland.ca/en/service/pei-labour-rebate |
| Labour employee eligibility | Eligible incremental full-time position: at least 1,850 hours/year and CAD 35,000 annual wage, PEI-resident employee; not an owner and not another government-funded position | https://www.princeedwardisland.ca/en/service/pei-labour-rebate |
| Current general/small-business provincial corporate rates | 15% general and 1% eligible small-business rate; provincial business limit CAD 600,000 from 1 July 2025, subject to eligibility, group reductions and stub-year allocation; federal limit/rates separate | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/corporations/provincial-territorial-corporation-tax/prince-edward-island-provincial-corporation-tax.html |

## Ask the client first

1. Which tax year and benefit-payment period, and which province on the last day of the year? Obtain arrival, departure, death and interprovincial moving dates, Canadian residence status and every business permanent establishment.
2. What are taxable income, net income and adjusted family net income, separately? Obtain all slips, foreign income, deductions, CPP/EI details and the spouse's return. Do not default an unknown marital status to single.
3. Which age, dependant, disability, pension, tuition, medical, donation, volunteer and investment facts apply? Obtain certificates, receipts, shared claims and carryover assessments before using a credit.
4. Is this an individual, an unincorporated business or a corporation? Identify self-employment, farming/fishing, instalments and prior assessments. A corporate credit cannot be placed on a personal return.
5. What is the requested output: a planning estimate, the actual annual filing or a separate CRA-administered benefit calculation? Do not call a partial provincial computation a final refund.

Also obtain each investment's registered specified issue, Minister's certificate and registration date, share class/payment, investor age/residence/control, earlier share disposals, associated entities, assistance and all certificate entitlements since 2022. Labour work needs a pre-commitment application, signed project terms, eligible job/wage/residence records and all other funding. Child-wellness claims need the child's age at the start of the year and programme/invoice/assistance details. Volunteer work needs the actual federal eligibility and compensation election.

## The method, step by step

### Family low-income reduction

Section 32 applies to an eligible year-end PEI resident who is at least 19, married/common-law or a parent. Build adjusted family income using the statutory additions/exclusions, including spouse income; do not simply substitute taxable income. The components are in the table: spouse OR eligible dependant, then other qualifying children without double counting, with separate qualifying senior additions. Deduct 5% of adjusted family income above CAD 23,000, floor at zero and limit current use to eligible PEI tax. Select one family applicant and record only the permitted unused-spouse transfer. A remaining single-person balance is not a refund or an ordinary carryforward. Non-resident/part-year world income, prison, death and bankruptcy have specific statutory rules; do not ignore them or automatically refuse all such returns. [Income Tax Act section 32](https://www.princeedwardisland.ca/sites/default/files/0432/I-01-Income%20Tax%20Act_1.pdf).

Retain the old single-parent/CAD 19,500 example but check whether the eligible-dependant addition applies. With one qualifying eligible dependant, the family reduction is CAD 700, not CAD 650 (the latter treats the child only as an “other child”). If available PEI tax is CAD 480, current use is CAD 480 and tax zero; the unused CAD 220 is not refunded. Do not add both CAD 350 eligible-dependant and CAD 300 other-child components for that same child.

### Island Essentials Benefit replaces the old sales-credit formula

The old PEI sales-credit amounts cannot be carried into July 2026 onward. Current section 36.3 and the updated provincial page govern the Island Essentials Benefit. For an otherwise eligible ordinary full-period person, start with CAD 310 annually, add CAD 55 for a qualifying spouse or the specified single-parent case, add no phase-in amount (the statutory C maximum is zero), and subtract 1% of adjusted income over CAD 95,000. The ordinary quarterly calculation is one quarter of that result, subject to the statutory minimum **CAD 43.75 per specified month** and the actual eligible-person/payment rules. Do not infer eligibility for a high-income person from the minimum alone. The statute's federal consumption-tax-benefit definitions, residence, return/application, shared-custody and small-payment handling still apply. [Section 36.3](https://www.princeedwardisland.ca/sites/default/files/0432/I-01-Income%20Tax%20Act_1.pdf); [updated provincial explanation](https://www.princeedwardisland.ca/en/information/finance-and-affordability/provincial-personal-income-tax).

For a tax year, the specified payments are July/October of the following year and January/April of the second following year; use the actual source/assessment for the benefit period rather than the calendar in which a T1 happens to be filed. Residence changes, qualified relation/dependant status and shared custody can alter the result. Do not add an old CAD 60 child amount that does not appear in the current formula, or deduct this cash benefit from PE428 tax. The old 2025 annual guide still describes the prior sales-tax-credit name; that is a period difference, not authority to reverse the enacted replacement.

### Volunteer credit: refundable CAD 1,000 and federal coordination

Section 36.2 requires entitlement to the federal firefighter or search/rescue deduction and no exclusion of volunteer-service payments under federal section 81(4). Check eligible hours/services, certificates and the compensation/exemption election using the federal rules; the provincial credit is not an independent benefit for anyone who calls themselves a volunteer. Resident on 31 December, or at qualifying death, can meet the residence limb. Specified separate returns are excluded. Current provincial tax use plus any excess refundable amount must total the eligible CAD 1,000 before any lawful setoff against Crown liabilities. Do not multiply a CAD 500 base by a provincial rate or forbid the linked federal claim. [Section 36.2](https://www.princeedwardisland.ca/sites/default/files/0432/I-01-Income%20Tax%20Act_1.pdf).

### Children's wellness, separate from a teacher supply credit

Section 11.1 permits the eligible expense base up to CAD 1,000 per qualifying child, converted at 9.5%, limited by provincial tax. A qualifying child is under 18 at the beginning of the taxation year. The programme must be outside the school curriculum and meet its weekly eight-consecutive-week or at least five-consecutive-day test, or the prescribed mixed-use/membership allocation, with qualifying artistic/cultural/recreational/developmental or physical activity. A camp's name or a casual hobby receipt is insufficient. The law excludes motorised activities under the physical-activity definition and includes horseback riding. [Section 11.1(3)-(6)](https://www.princeedwardisland.ca/sites/default/files/0432/I-01-Income%20Tax%20Act_1.pdf).

Qualifying registration/membership fees can contain integral administration, instruction, facilities and permitted equipment/uniform components; ordinary equipment bought separately does not automatically qualify. Remove accommodation, travel, food/beverages, reimbursements and expenditure already deducted or used for an incompatible credit. Split claims cannot exceed the shared child cap. The old CAD 500 wellness base is not current, and its blanket exclusion of every uniform/equipment cost was too broad. This is different from a teacher school-supply programme; no provincial CAD 500 teacher credit is established by the sources read, and the federal educator credit cannot be labelled PEI relief without its own law.

### Community-development equity: issuer and investee are different

The credit is for a registered **community economic-development business (CEDB) specified issue**, not every private “eligible business corporation”. The 2026 Act's eligible investor is resident in PEI and at least 19 at the time of investment. Eligible shares are fully paid, newly issued voting common shares with the prescribed non-redeemable/non-convertible/participation conditions, or the eligible association membership share, issued no later than 28 February 2027. Replacement shares and tax-credit-avoidance arrangements are excluded. Registration, valid specified issue, permitted use of funds, securities compliance and the Minister's certificate are essential; a shareholder cannot create the credit by printing a certificate. [Community Development Act sections 1-4](https://www.princeedwardisland.ca/sites/default/files/legislation/c-13-01-community_development_equity_tax_credit_act.pdf).

The **CEDB issuer** has its own section 3 criteria, including PEI head office, provincial payroll, assets/revenue below CAD 3 million including affiliates, active business/investment mandate and professional-practice exclusions. A qualifying **underlying investee** under section 5(2) has a different ceiling: fewer than 500 full-time-equivalent employees and assets below CAD 65 million including affiliates, at least 75% PEI wages and active-business/property conditions. The old overview's CAD 25 million/100 employees is outdated for the amended investee test; the larger investee ceiling does not replace the issuer's CAD 3 million criterion. Registration also has the statutory specified-shareholder/control restriction and must be checked against the full holding structure. [Act sections 2-5](https://www.princeedwardisland.ca/sites/default/files/legislation/c-13-01-community_development_equity_tax_credit_act.pdf).

Prohibited uses include lending, impermissible securities, shareholder debt/dividend payouts, replacement-share/redemption arrangements, certain acquisition funding and above-market-value related transfers. Programme recognition does not approve the commercial investment or remove those restrictions. Retain the use-of-proceeds/registration/financial/securities records. General Regulations sections 2-6 include the plan, specified issue, governance, staged investment/compliance and revocation conditions; these are not replaced by a “PEI payroll 75%” check alone. [Act sections 4-5](https://www.princeedwardisland.ca/sites/default/files/legislation/c-13-01-community_development_equity_tax_credit_act.pdf); [General Regulations](https://www.princeedwardisland.ca/sites/default/files/legislation/c13-01g-community_development_equity_tax_credit_act_general_regulations.pdf).

Section 6 gives a 35% certificate formula and cumulative entitlement cap CAD 56,000 for certificates applied for from 1 January 2022, plus other prescribed limits and assistance restrictions. It has an express exception for the federal RRSP deduction in subsection 146(5), so the old blanket RRSP refusal is wrong. The current consolidated Regulations define the qualifying RRSP trust conditions. Other credits/deductions/assistance still need the actual prohibition and permitted exceptions; this is not blanket stacking permission. [Act section 6](https://www.princeedwardisland.ca/sites/default/files/legislation/c-13-01-community_development_equity_tax_credit_act.pdf); [Regulations section 1](https://www.princeedwardisland.ca/sites/default/files/legislation/c13-01g-community_development_equity_tax_credit_act_general_regulations.pdf).

The 2015 programme overview still states a CAD 20,000 annual investment maximum. The amended Act/current consolidation read instead set the certificate formula, cumulative limit and prescribed-limit conditions, while the available Regulations do not establish that old overview amount as a current annual certificate cap. **Do not approve a new larger certificate or assume the old page is current**: obtain the current Minister's issue/certificate conditions or a current prescribed cap before accepting the investment entitlement. The annual **income-tax use** is independently and explicitly capped at CAD 7,000 in Income Tax Act section 36.1. Do not confuse that claim cap with either a new certificate entitlement or a maximum investment. [Old programme overview, dated 2015](https://www.princeedwardisland.ca/en/information/finance/community-economic-development-business-program); [Act section 6](https://www.princeedwardisland.ca/sites/default/files/legislation/c-13-01-community_development_equity_tax_credit_act.pdf); [income-tax section 36.1](https://www.princeedwardisland.ca/sites/default/files/0432/I-01-Income%20Tax%20Act_1.pdf).

General Regulations section 9 requires the CEDB certificate application by the tenth day of the month following issue. For income-tax use, file the relevant return within three years after year end, retain/attach the Minister's certificate as required, and claim the lesser of eligible credit available, applicable annual CAD 7,000 cap and tax. Track carrybacks/forwards by origin year and prior use; unused balances have three years back (not before 2011)/seven forward and the destination-year cap. A generic ten-year tax-adjustment facility does not waive these programme conditions. [Regulations section 9](https://www.princeedwardisland.ca/sites/default/files/legislation/c13-01g-community_development_equity_tax_credit_act_general_regulations.pdf); [section 36.1](https://www.princeedwardisland.ca/sites/default/files/0432/I-01-Income%20Tax%20Act_1.pdf).

The holding clock is **five years from registration of the specified issue**, not four years from Janet's purchase. Early disposal requires the Act section 7 repayment analysis. Regulations section 10 gives specific death, qualifying RRSP/RRIF transfer, financial-failure and qualifying share-exchange exceptions; a non-failure wind-up has the prescribed 60-month proration, and Ministerial waiver/proration needs an actual decision. Do not assume all early sales qualify for proration or all RRSP transfers trigger repayment. Retain both registration and acquisition dates. [Act section 7](https://www.princeedwardisland.ca/sites/default/files/legislation/c-13-01-community_development_equity_tax_credit_act.pdf); [Regulations section 10](https://www.princeedwardisland.ca/sites/default/files/legislation/c13-01g-community_development_equity_tax_credit_act_general_regulations.pdf).

### Labour Rebate: apply before committing, do not invent a T2 entitlement

The current PEI Labour Rebate is discretionary business assistance for approved incremental full-time jobs in eligible export-oriented/strategic activities. The headline is **up to** 25% of eligible wages, not a flat statutory refund of all T4/T4A/benefits. Eligible employees must be PEI residents in qualifying incremental full-time positions, at least 1,850 hours and CAD 35,000 annual wages, excluding owners and positions receiving other government labour funding. The eligible-expense period is at most one year; the rebate may be paid on a prorated basis over up to ten years under the actual agreement. [Current programme](https://www.princeedwardisland.ca/en/service/pei-labour-rebate).

Apply to Innovation PEI through its programme process before any financial or legal project commitment. Provide business/project plan, financial/ownership information, proposed job/wage/residence records, financing and all assistance; obtain written approval/terms before budgeting a receipt. Keep payroll evidence and submit the actual claim/report under the agreement. Do not turn contractors, owner remuneration, old jobs or every benefit into eligible incremental wages, impose an unsupported CAD 500,000 annual cap or book a T2 refundable credit from this overview. Federal SR&ED, other funding and assistance/expense tax treatment need their own reconciliation; there is no free stacking. [Current programme](https://www.princeedwardisland.ca/en/service/pei-labour-rebate).

### Corporate-rate context and return administration

The current PEI general corporate rate is 15%, and the eligible small-business provincial rate is 1% with a CAD 600,000 provincial limit from July 2025. The federal small-business limit is a separate test; a blanket “combined 10% on the first 600,000” is wrong if the federal deduction only covers a smaller amount. Apply eligible active-business, allocation, associated-group, taxable-capital/passive-income and stub-year rules before comparing incorporation. The old 16% provincial/31% combined general, lowest-in-Canada claim and unsupported 38.67% passive-income claim do not justify advice. [Act sections 37 and 37.11.7](https://www.princeedwardisland.ca/sites/default/files/0432/I-01-Income%20Tax%20Act_1.pdf); [current provincial corporate table](https://www.princeedwardisland.ca/en/information/finance/provincial-corporate-income-taxes).

The 2025 annual filing map uses PE428 Parts A-C after federal T1 steps, with the actual credit instructions and T1 provincial destinations. Do not invent a generic PE479 route for every credit or reinsert the abolished surtax. Use current certified software/NETFILE, review generated schedules, obtain approval, save confirmation and compare the assessment and carryovers; provincial labour and investment-certificate applications remain separate. Corrections after assessment follow the actual CRA change-return route and do not extend programme dates. [Historical 2025 annual guide](https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/prince-edward-island/5002-pc.html); [CRA change-return process](https://www.canada.ca/en/services/taxes/income-tax/personal-income-tax/after-you-file/change-return.html).

### Filing dates and the actual form year

For ordinary 2026 individual returns, ITA section 150(1)(d) gives the following-year filing rule: 30 April 2027 ordinarily; 15 June 2027 where the individual or their spouse/common-law partner carried on a qualifying business, subject to the statutory exceptions. Deaths and other special returns have different clocks. The later business filing date does not itself extend the balance-payment deadline. [ITA section 150](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-150.html).

The annual provincial instructions read for this rewrite are the **2025 tax year, 2025-2026 filing cycle**, not final 2026 annual forms. Those instructions are used below only for the explicitly dated filing map and historical credit details. Do not put a 2026 figure on a 2025 return or assume a 2025 line number is final for 2026. Verify the released 2026 package before filing. For payments, current interest, instalment requirements and penalties, load the current federal filing/payment rules and the taxpayer's CRA account notices; the old guide's unsupported penalty/interest estimate is not a payment instruction.

## Worked cases

### Retained single-parent reduction: distinguish eligible dependant from other child

Assume 2026 eligibility, adjusted family income CAD 19,500, one child for whom the claimant is entitled to the eligible-dependant addition, no other children/senior additions and CAD 480 available PEI tax. Reduction is CAD 350 + CAD 350 = CAD 700; phase-out is zero because AFNI is below CAD 23,000. Use CAD 480, leaving tax zero. CAD 220 unused is not a refundable amount and there is no spouse to transfer it to. The old CAD 650/170 result used the other-child component instead of the applicable eligible-dependant component. [Section 32](https://www.princeedwardisland.ca/sites/default/files/0432/I-01-Income%20Tax%20Act_1.pdf).

```oa-check
name: PEI single parent eligible-dependant decision 2026
inputs:
  afni: 19500
  tax_before: 480
steps:
  - reduction: max(0, 350 + 350 - max(0, afni - 23000) * 0.05)
  - used: min(tax_before, reduction)
  - tax_after: tax_before - used
  - unused_not_refunded: reduction - used
expected:
  reduction: 700
  used: 480
  tax_after: 0
  unused_not_refunded: 220
```

### Janet's CAD 100,000 subscription: verify entitlement, then apply the annual claim cap

Retain Janet, net income CAD 185,000, her October 1, 2025 CAD 100,000 Atlantic Bioscience Inc. investment and purported certificate 2025-ETC-0142. Those facts **do not establish** that the company is a registered CEDB, that this specified issue qualifies or that a new CAD 35,000 certificate is valid under the current prescribed/issue limits. The old overview's annual-investment statement also needs reconciliation with the amended law. Hold that real entitlement pending the actual Minister's certificate/registration conditions; do not approve it by assumption or invent a larger current entitlement.

To show the independent annual **claim** rule, assume instead the documented eligible credit balance already available across valid certificates/carryovers is CAD 35,000 and available PEI tax is CAD 22,800. Current claim is limited to CAD 7,000, leaving CAD 15,800 tax and a CAD 28,000 balance subject to its actual origin-year expiry. It is not zero tax with CAD 12,200 left, and the next year cannot automatically use CAD 12,200 because that year's cap still applies. This bounded workpaper does not certify Janet's new-subscription entitlement. Her holding date also follows specified-issue registration, not an invented October-2029 four-year release. [Income-tax section 36.1](https://www.princeedwardisland.ca/sites/default/files/0432/I-01-Income%20Tax%20Act_1.pdf); [Community Development Act sections 6-7](https://www.princeedwardisland.ca/sites/default/files/legislation/c-13-01-community_development_equity_tax_credit_act.pdf).

```oa-check
name: Janet PEI annual use cap on independently valid credit balance
inputs:
  eligible_balance: 35000
  tax_before: 22800
  annual_limit: 7000
steps:
  - used: min(eligible_balance, tax_before, annual_limit)
  - tax_after: tax_before - used
  - balance_after: eligible_balance - used
expected:
  used: 7000
  tax_after: 15800
  balance_after: 28000
```

### Wellness versus volunteer: base and refundable dollars are different

For one eligible child, assume CAD 1,200 net qualifying programme fees, no duplicate claims and sufficient provincial tax. The shared wellness base stops at CAD 1,000; 9.5% produces CAD 95 non-refundable credit. In a separate fully eligible volunteer case with CAD 300 PEI tax before the volunteer credit, the CAD 1,000 dollar credit eliminates that tax and leaves CAD 700 refundable before any lawful setoff. Do not multiply the volunteer credit by 9.5%, or refund the unused child-wellness base. [Sections 11.1 and 36.2](https://www.princeedwardisland.ca/sites/default/files/0432/I-01-Income%20Tax%20Act_1.pdf).

```oa-check
name: PEI credit base versus refundable dollar credit 2026
inputs:
  qualifying_fees: 1200
  volunteer_tax_before: 300
steps:
  - wellness_base: min(qualifying_fees, 1000)
  - wellness_credit: wellness_base * 0.095
  - volunteer_used: min(volunteer_tax_before, 1000)
  - volunteer_refund_before_setoff: 1000 - volunteer_used
expected:
  wellness_credit: 95
  volunteer_used: 300
  volunteer_refund_before_setoff: 700
```

## When to refuse or refer

- Stop the final calculation when residence, year, taxable income, family status, credit evidence or a current source needed for the answer is missing. State the exact missing fact; do not invent a conservative numeric default or relabel a prior-year amount as current.
- Refer special returns, disputed residence, multiple-province business allocation, treaty income, minimum tax, tax on split income, Indigenous tax exemptions, trusts and corporate claims to the relevant specialist workflow. Do not turn “outside this ordinary computation” into an unsupported statement that no relief exists.
- Do not substitute payroll withholding for annual tax, cash benefits for non-refundable credits, a provincial label for a federal credit, or a corporation's incentive for its shareholder's personal credit.
- Do not promise a refund, investment eligibility, programme funding, investment value or professional approval. Obtain the relevant certificate and calculate tax and cash payments separately. Keep records supporting shared claims, carryovers, amendments and recapture.

Additional stops: missing registered specified issue/Minister certificate, unresolved annual entitlement limit, connected ownership, replacement shares, prohibited assistance or a proposed early disposal means hold the investment claim. A late labour application cannot be assumed accepted. Do not apply federal emergency-services exemption and the incompatible provincial volunteer claim together; do not prohibit the linked federal volunteer deduction itself. Children's fees, school-supply costs and senior assistance require the right programme evidence rather than a catch-all PEI credit.

## Sources

| Official source and scope actually read | URL | Read on |
|---|---|---|
| Read for: PEI Income Tax Act current July 1, 2026: sections 7-18, 31-32, 36.1-36.4, 37 and 37.11.7 read for current credits, annual equity use, refundability, benefit formula and corporate rates | https://www.princeedwardisland.ca/sites/default/files/0432/I-01-Income%20Tax%20Act_1.pdf | 2026-11-14 |
| Read for: PEI updated personal-income-tax page: current 2026 amounts, six bands and Island Essentials replacement | https://www.princeedwardisland.ca/en/information/finance-and-affordability/provincial-personal-income-tax | 2026-11-14 |
| Read for: Community Development Equity Tax Credit Act current May 29, 2026, sections 1-7: issuer versus investee, definitions, certificate formula/cumulative limit and five-year clock | https://www.princeedwardisland.ca/sites/default/files/legislation/c-13-01-community_development_equity_tax_credit_act.pdf | 2026-11-14 |
| Read for: Community Development General Regulations current January 1, 2022, sections 1-12: RRSP trust definition, registration/compliance, certificate deadline and exact repayment exceptions | https://www.princeedwardisland.ca/sites/default/files/legislation/c13-01g-community_development_equity_tax_credit_act_general_regulations.pdf | 2026-11-14 |
| Read for: 2015 CEDB overview: read to identify its outdated investee figures and old annual-investment statement, not used to override amended law | https://www.princeedwardisland.ca/en/information/finance/community-economic-development-business-program | 2026-11-14 |
| Read for: Current Labour Rebate page: discretionary rate, employee tests, pre-commitment application, period/payment and funding exclusions | https://www.princeedwardisland.ca/en/service/pei-labour-rebate | 2026-11-14 |
| Read for: CRA provincial corporation tax: current PEI 1% and 15% rates, CAD 600,000 business limit, July 2025 change and day allocation; separate Schedule 322 and Schedule 5 line 210 | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/corporations/provincial-territorial-corporation-tax/prince-edward-island-provincial-corporation-tax.html | 2026-11-14 |
| Read for: Current provincial corporate-tax page: July 2025 rate/limit changes, corroborating current Act | https://www.princeedwardisland.ca/en/information/finance/provincial-corporate-income-taxes | 2026-11-14 |
| Read for: CRA 2025 PEI annual guide: historical filing order, special-return and credit form instructions | https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/prince-edward-island/5002-pc.html | 2026-11-14 |
| Read for: ITA section 150(1)(b),(d): ordinary, business and death filing clocks | https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-150.html | 2026-11-14 |
| Read for: CRA change-return instructions: assessed-return correction procedure | https://www.canada.ca/en/services/taxes/income-tax/personal-income-tax/after-you-file/change-return.html | 2026-11-14 |
| Read for: CRA GST/HST place-of-supply opening rules: ordinary PEI participating-province rate | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/charge-collect-place-supply.html | 2026-11-14 |

Not yet confirmed: Final 2026 annual PE428/other forms and box mapping; current prescribed annual equity-certificate entitlement/issue cap where the 2015 programme overview says CAD 20,000 investment but the amended Act/available regulation specify different cumulative/claim limits, before accepting a new larger entitlement; taxpayer-specific registration and Minister conditions for Janet/Atlantic Bioscience; any current provincial teacher-school-supply or senior-independence programme; full corporate passive-income/federal extraction rates, federal small-business deduction and labour/SR&ED assistance interactions beyond the scoped provincial law; property-transfer and housing relief. No current entitlement or final return is inferred from a fictional case.
