---
name: on-eht
description: >
  Calculate, reconcile and prepare Ontario Employer Health Tax for 2026.
  Use for Ontario EHT, Ontario payroll tax, the 1 million exemption,
  5 million exemption threshold, 1.2 million instalment threshold,
  associated employers, qualifying charity campuses, Ontario permanent
  establishments, stock-option remuneration, ONT-TAXS, annual returns
  and the 2262E exemption allocation. Read alongside canada-payroll.
version: 1.1
jurisdiction: CA
tax_year: 2026
last_updated: 2026-11-13
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
category: payroll
domain: payroll
type: computation
---

# Ontario employer health tax v1.1

## Scope

Prepare a calendar-2026 Ontario Employer Health Tax (EHT) computation, payroll reconciliation, instalment schedule and annual-return working paper. Amounts are CAD. The Ontario Ministry of Finance administers this employer tax under the Employer Health Tax Act, RSO 1990, chapter E.11. It is separate from employee withholding, CPP/EI, WSIB and British Columbia EHT. This skill is **Built from the law** and **Not yet approved**. [Act sections 1-5](https://www.ontario.ca/laws/statute/90e11); [current ministry guide](https://www.ontario.ca/document/employer-health-tax-eht).

Always read [canada-payroll](../canada-payroll.md) for the same payroll's federal deductions, remittances, T4s and ROEs. For BC use [bc-eht](../british-columbia/bc-eht.md); do not transfer BC's exemption, association date, instalment rules or interest compounding into Ontario. Prepare proposed filings and postings for an authorized person to approve. Do not submit a return, make a payment or post to a ledger merely because the working paper is complete.

## Ask the client first

1. Which calendar year and legal employer? Obtain the registration notice, **15-digit Business Number as shown on the EHT account/return**, all EHT accounts and extensions such as TE0001/TE0002, prior returns, assessments and notices. Confirm authorized ONT-TAXS access without requesting passwords in the working paper. Do not invent a separate seven-digit account. [Main guide](https://www.ontario.ca/document/employer-health-tax-eht); [allocation form instructions](https://forms.mgcs.gov.on.ca/dataset/2630e112-e9e1-49bb-9f09-7dac17b803d8/resource/cb7acbb8-bd66-4d76-b394-1db38c7e3ed2/download/2262e.pdf).
2. Obtain calendar-year and monthly payroll registers, T4/T4A slips and summaries, taxable-benefit and option records, termination settlements and the payroll/ledger reconciliation. Identify current employees, former employees and officeholders; employee residence alone does not establish EHT treatment. [Act section 1](https://www.ontario.ca/laws/statute/90e11).
3. Where and when did the employer have actual or deemed Ontario permanent establishments (PEs)? For each employee obtain physical reporting, attachment, supervisor, paying-establishment and outside-Ontario facts. Record the dates on which the employer both had an Ontario PE and was an eligible employer. [PE guidance](https://www.ontario.ca/document/employer-health-tax-eht/permanent-establishment); [exemption guidance](https://www.ontario.ca/document/employer-health-tax-eht/tax-exemption).
4. Obtain ownership/control and relationship records for the whole year, group Ontario payroll, acquisitions/disposals and all signed exemption allocations. Was any entity a registered charity, publicly controlled body, partnership, trust or non-share corporation? For charity campuses obtain charity status, leases/deeds, occupancy periods, exclusive use, public advertising or the relevant exception, and ministry registration. [Association](https://www.ontario.ca/document/employer-health-tax-eht/associated-employers); [charities](https://www.ontario.ca/document/employer-health-tax-eht/registered-charities).
5. Obtain actual 2025 Ontario remuneration, the 2026 payroll estimate and monthly cumulative totals, actual payments/credits and dates received. Identify the first and second consecutive years subject to tax, any successor transaction, cessation, bankruptcy or ITA section 87 amalgamation and its exact date. Prior-year **tax** is not the instalment trigger. [Act sections 3, 5, 7 and 30](https://www.ontario.ca/laws/statute/90e11).

Missing facts stay open. Show the conditional result and the fact needed; do not turn uncertainty into an exemption, taxable payroll, invented monthly payment obligation or purported professional approval.

## The method, step by step

### 1. Establish Ontario connection before counting payroll

Apply the EHT Act's own PE and employee tests. The base includes remuneration of employees who report for work at the employer's Ontario PE, and employees who report at none of the employer's PEs but are paid from or through its Ontario PE. Reporting includes reasonable attachment without physical attendance. Consider the actual supervision, duties, instructions, equipment and reporting relationships. A home office is not automatically the employer's PE; an associated company's premises is not automatically this employer's PE. [Act section 1(1)-(3.1)](https://www.ontario.ca/laws/statute/90e11); [PE guidance](https://www.ontario.ca/document/employer-health-tax-eht/permanent-establishment).

If a worker reports to the employer's Ontario and outside-Ontario PEs during the year, section 1(1.3) generally includes the whole year's remuneration. Section 1(1.4) permits exclusion where the Minister is satisfied the worker reports outside Ontario for all or substantially all the year; the ministry administratively describes this as generally 90% or more. Do not substitute a residence test, automatic workday split or the CRA withholding province. Document the actual exception before excluding the pay. [Act section 1(1.3)-(1.4)](https://www.ontario.ca/laws/statute/90e11); [PE guidance](https://www.ontario.ca/document/employer-health-tax-eht/permanent-establishment).

A non-resident employer can have an actual or deemed Ontario PE, for example through the statutory contracting-agent rule or qualifying substantial machinery/equipment use. Section 4 also has a conditional deemed-employer rule for foreign personnel supplied to a connected Ontario person. Intermittent presence alone does not prove all those conditions. Establish the employer, arrangement and PE before concluding liability; refer a disputed foreign/remote arrangement. [Act sections 1(2), 4 and 21](https://www.ontario.ca/laws/statute/90e11).

### 2. Build and reconcile total Ontario remuneration

Start with the Ontario-connected gross employment amounts under federal Income Tax Act sections 5, 6 and 7, including amounts that would be employment income if a non-resident employee were resident. Include salaries, wages, bonuses, commissions, vacation pay, taxable allowances, taxable benefits, office/directors' fees and relevant current/former-employee option benefits. Include amounts once, even if a benefit appears both in the benefits register and T4 Box 14. [Act section 1, including subsection (6)](https://www.ontario.ca/laws/statute/90e11); [remuneration guidance](https://www.ontario.ca/document/employer-health-tax-eht/remuneration).

Separate termination components. Pay in lieu of notice, unused vacation, bonuses, commissions, overtime and salary continuance can remain taxable employment remuneration. An actual retiring allowance, employer-paid pension/annuity/superannuation after retirement, or a properly non-taxable business-expense reimbursement is not included merely because money was paid to a former worker. The label “severance” alone does not decide. Document the statutory character and T4/T4A reporting of every component. [Act section 1 definitions](https://www.ontario.ca/laws/statute/90e11); [remuneration: termination pay and retiring allowances](https://www.ontario.ca/document/employer-health-tax-eht/remuneration).

For options, obtain the agreement, issuer/employer connection, acquisition/exercise/disposition dates, value and employment/PE history. Apply the designated-year rules in section 2(3.1)-(3.5):

- For the qualifying CCPC case in section 2(3.5)(a), both the person agreeing to issue/sell and the share must satisfy the specified CCPC conditions at the agreement and acquisition times, and federal paragraph 7(1)(a), as modified by subsection 7(1.1), must apply. Use the resulting designated benefit year.
- In another paragraph 7(1)(a) case, section 2(3.5)(b) uses the year the employee acquired the security, even if federal treatment defers income. Other section 7 benefits follow section 2(3.5)(c).
- The ministry's Ontario-connection guidance looks at remuneration being subject to EHT when the employee exercises; for former employees it looks at the connection when employment ceased. Do not allocate by the option's vesting-period workdays. A federal section 110 deduction does not reduce the EHT base.

The ministry's general CCPC summary is broader than the conditions enacted in section 2(3.5)(a). If the issuer ceased to be a CCPC between grant and acquisition, or the year/connection is disputed, resolve the actual statutory facts with the Ministry and an Ontario practitioner before choosing a year. Historical section 2.2 options relief applies to years **before 2010**, not the current year and not exemption sharing. [Act sections 2(3.1)-(3.5), 2.2](https://www.ontario.ca/laws/statute/90e11); [current option guidance](https://www.ontario.ca/document/employer-health-tax-eht/remuneration).

Reconcile each payroll account to T4 Box 14 totals, relevant T4A/former-employee amounts, benefits, options, interprovincial/foreign exclusions and the payroll control accounts. List each difference by worker, amount, tax year and legal reason. There is no general 2% tolerance in this method. Do not add all benefits to Box 14 or treat every Box 14 dollar as Ontario remuneration. Resolve unexplained differences before finalizing.

### 3. Determine exemption eligibility, days and the payroll gate

A full-year, unassociated **eligible employer** can claim up to **1,000,000** for 2026 if its total Ontario remuneration is **no more than 5,000,000**. Above the applicable gate the ordinary exemption is **nil for the year**, not merely nil on the excess. At exactly 5,000,000 the statutory gate is satisfied. Registered charities have separate treatment below. [Act section 2.1(1)-(2), (5), (7)](https://www.ontario.ca/laws/statute/90e11).

Eligibility is the legal test in section 1, not simply the words private/public on a payroll file. Public bodies, non-taxable Crown agencies, specified government-appointed bodies and the listed federal section 149 classes can be excluded. Taxable Crown corporations and organizations funded but not controlled by government can qualify. Government/municipal appointment powers, governing legislation, bylaws and income-tax status matter. Charity registration by itself does not override a government-control exclusion. If status is uncertain, show the alternatives and refer the classification rather than declaring every public-looking entity ineligible. [Act eligible-employer definition](https://www.ontario.ca/laws/statute/90e11); [ministry eligibility guidance](https://www.ontario.ca/document/employer-health-tax-eht/tax-exemption).

For a part-year employer, let **d** be the actual number of days it was both an eligible employer and had an Ontario PE; **D** is the actual number of days in that calendar year. Subject to the payroll gate and allocation rules:

- available unassociated exemption = **1,000,000 × d / D**;
- payroll gate = **5,000,000 × d / D**.

Compare actual annual Ontario remuneration with the prorated gate before granting the exemption. Do not divide by months, count a partial month as a whole month, or prorate only the exemption. A seasonal business can retain a full-year exemption if its actual employer/PE/eligibility facts support the full year; corporate existence alone is insufficient. In bankruptcy the ministry excludes the bankruptcy date from the pre-bankruptcy day count. New/predecessor/successor entities and group members need their own dates. Keep precision in the calculation; show rounded presentation separately from any actual return's entry convention. [Act section 2.1(2), (7)-(8.1)](https://www.ontario.ca/laws/statute/90e11); [part-year guidance](https://www.ontario.ca/document/employer-health-tax-eht/tax-exemption).

The exemption was increased from 490,000 for 2020 as a temporary response and made permanent in 2021. Enacted amounts are 1,000,000 for **2020-2028**; the next scheduled inflation adjustment begins **January 1, 2029**. Do not invent a new 2026 indexed amount. [Act sections 2.1(2), 2.1.1](https://www.ontario.ca/laws/statute/90e11); [exemption history](https://www.ontario.ca/document/employer-health-tax-eht/tax-exemption).

### 4. Resolve association and the actual allocation

Ontario tests association **at any time during the year**, under section **1(5.1)** and the incorporated/modified federal section 256 rules, including extensions to individuals, partnerships and trusts and the third-employer connection. The federal election not to be associated for small-business-deduction purposes does not let an employer opt out of Ontario EHT association. Common ownership, relationships and control can matter even if businesses operate independently. [Act section 1(5.1)](https://www.ontario.ca/laws/statute/90e11); [association guide](https://www.ontario.ca/document/employer-health-tax-eht/associated-employers).

For 2026 apply the **post-2024** group rules in section 2.1(0.1), (3.1), (4.0.1)-(4.0.4) and (8.1). Check each relevant group and its actual payroll gate. An acquisition may place BoughtCo in one group with its seller and another with its buyer. Do not combine buyer and seller into a single group if they were not all associated at the same time. Do not give BoughtCo two unrestricted exemptions: its combined allocations remain limited by its own statutory maximum. Ministry examples contain arithmetic inconsistencies, so recompute their totals rather than copying their outcomes. [Act section 2.1](https://www.ontario.ca/laws/statute/90e11); [current acquisition guidance](https://www.ontario.ca/document/employer-health-tax-eht/associated-employers).

For each group:

1. Establish total relevant Ontario remuneration and each member's own qualifying days/gate. The group's gate and maximum shared exemption follow the **highest qualifying member amount**, ordinarily the member with the longest qualifying period. Do not assemble a full year by adding different members' non-overlapping days.
2. Above the group's applicable gate its allocable exemption is nil. Within the gate, obtain an actual agreement. Each member is limited by its allocated amount and its own unassociated statutory exemption calculation, including its own payroll gate; the form also limits allocation to its Ontario remuneration.
3. One member files **Associated Employers Exemption Allocation, form 2262E**, by the return deadline. Include all required Ontario-associated members, including nil allocations and relevant ceased/nil-payroll members. Identify the 15-digit BN, legal name and allocated amount. The form has an amendment box; it is not automatically irrevocable. Missing/incomplete group filing can deny group relief. Do not allocate to the largest payroll automatically.
4. Each employer uses its **own** total Ontario remuneration to choose its tax rate; this differs from combining multiple accounts of the **same legal employer** for the rate. Allocate that employer's exemption across its accounts without duplicating it. A Multiple Accounts Schedule is no longer required.

A ceasing associated employer initially claims no exemption on its final return under ministry guidance; after the group files annual returns/allocation it may amend for its proper allocation. Eligible registered-charity payroll/sharing is treated separately; removing a charity from the ordinary sharing calculation does not necessarily break the association between its other related employers. [Act section 2.1](https://www.ontario.ca/laws/statute/90e11); [association and filing guide](https://www.ontario.ca/document/employer-health-tax-eht/associated-employers); [form 2262E, 2025/02](https://forms.mgcs.gov.on.ca/dataset/2630e112-e9e1-49bb-9f09-7dac17b803d8/resource/cb7acbb8-bd66-4d76-b394-1db38c7e3ed2/download/2262e.pdf); [O Reg 423/16 section 2](https://www.ontario.ca/laws/regulation/160423).

### 5. Apply registered-charity campus rules separately

First prove registered-charity status and eligible-employer status. An ordinary nonprofit without registered-charity status does not obtain the charity's exemption from the 5,000,000 gate or multiple-campus rules. An eligible registered charity can claim relief notwithstanding that gate and is not required to share ordinary group relief with non-charitable associated employers. [Act section 2.1(9)-(10)](https://www.ontario.ca/laws/statute/90e11); [charity guide](https://www.ontario.ca/document/employer-health-tax-eht/registered-charities).

Where there are **two or more qualifying charity campuses**, apply O Reg 423/16 section 3, not one exemption per physical address:

- Locations must be Ontario PEs or parts of PEs, exclusively occupiable by the charity, used/occupied solely by it and for its charitable activities. Group locations on one parcel, contiguous parcels or units of the same property into the proper campus.
- Notify the Ministry in writing and supply the composition/occupancy information. At least one location must be publicly advertised unless the regulation's emergency-shelter, group-home or intensive-support-residence exception applies. Keep the ministry registration and evidence of legal status/control, leases/deeds, locations, occupancy dates and advertising/exception.
- For each campus calculate its applicable **1,000,000** amount, prorated for days it qualified and the employer was eligible. Its deductible exemption is the **lesser of that amount and remuneration of employees reporting there**. Unused campus relief cannot shelter head-office or non-qualifying-location payroll.
- Subtract the sum of allowed campus exemptions from employer Ontario remuneration. Choose the rate using the employer's combined Ontario payroll before exemptions. File a return for each qualifying campus annually even if its tax is nil; apply the employer's combined payroll for the instalment threshold.

The charity webpage still contains a 490,000 paragraph, while its current examples and official return instructions use 1,000,000 for 2020-2028. Use the current-year amount supported by those instructions and the Act, preserving the regulation's qualification/attribution conditions. Do not reuse the stale paragraph. A complex campus classification remains a referral, not an extra allowance created from an address list. [O Reg 423/16 section 3](https://www.ontario.ca/laws/regulation/160423); [charity filing/registration guidance](https://www.ontario.ca/document/employer-health-tax-eht/registered-charities); [official 2272E instructions, exemption table](https://forms.mgcs.gov.on.ca/dataset/8cbf9517-7f61-47d9-a942-421699ab8b67/resource/d7351997-3c9f-4af9-a418-d0b9f8c15464/download/2272e.pdf).

### 6. Select one rate and calculate annual tax

Choose the rate from **total Ontario remuneration before exemption**. Apply that single rate to taxable remuneration after the valid exemption. This is not a progressive marginal-bracket computation. For multiple accounts combine the same employer's payroll to determine the rate; associated separate employers use their own remuneration. [Act section 2(2)](https://www.ontario.ca/laws/statute/90e11); [official return instructions, line 4](https://forms.mgcs.gov.on.ca/dataset/8cbf9517-7f61-47d9-a942-421699ab8b67/resource/d7351997-3c9f-4af9-a418-d0b9f8c15464/download/2272e.pdf).

| Total Ontario remuneration, before exemption | 2026 rate applied to the whole taxable base |
|---|---|
| Up to 200,000.00 | 0.98% |
| 200,000.01-230,000.00 | 1.101% |
| 230,000.01-260,000.00 | 1.223% |
| 260,000.01-290,000.00 | 1.344% |
| 290,000.01-320,000.00 | 1.465% |
| 320,000.01-350,000.00 | 1.586% |
| 350,000.01-380,000.00 | 1.708% |
| 380,000.01-400,000.00 | 1.829% |
| Over 400,000.00 | 1.95% |

**Annual EHT = max(0, total Ontario remuneration − valid exemption) × selected rate.** No general 200,000 liability/registration floor exists for a non-eligible employer. A non-eligible employer with 175,000 of Ontario remuneration owes 1,715 at 0.98%. Keep the liability, registration and return-duty questions distinct. [Act sections 2 and 2.1](https://www.ontario.ca/laws/statute/90e11); [main guide](https://www.ontario.ca/document/employer-health-tax-eht).

### 7. Build the actual monthly instalment schedule

For 2026, an employer whose **current-year total Ontario remuneration exceeds 1,200,000** must make monthly instalments. Exactly 1,200,000 does not exceed the statutory threshold. Prior-year EHT of 600 is not the test; the historical pre-2021 payroll threshold was 600,000. Combine accounts of the same employer and apply the charity aggregation rules, not unrelated employers' individual payrolls. [Act section 3(1)](https://www.ontario.ca/laws/statute/90e11); [main guide, monthly instalments](https://www.ontario.ca/document/employer-health-tax-eht).

Follow the ministry's cumulative timing method: track payroll during the year; when cumulative payroll first **exceeds 1,200,000**, the first required instalment catches up the taxable remuneration **above the actual allowable exemption**, not just the amount above 1,200,000. Pay by the **15th of the following month**; thereafter account for each month's taxable remuneration. Do not spread a 1,000,000 exemption over twelve monthly twelfths. Do not start payments just because cumulative payroll has consumed the exemption while still below the instalment threshold. [Current worked timing example](https://www.ontario.ca/document/employer-health-tax-eht).

The statutory monthly computation in section 3(4)-(4.02) is **(S − E) × R**, with S the month's Ontario remuneration and E the available exemption, limited to the unused annual amount/month's remuneration. Rate R uses the current-year estimate for the first and second consecutive years subject to tax and the prior-year remuneration rate in later years. Apply the cumulative first-payment catch-up explained above and subtract amounts already accounted for; do not duplicate earlier taxable pay. Obtain actual prior payroll to select the statutory rate even when the current payroll decides whether instalments are required. [Act section 3](https://www.ontario.ca/laws/statute/90e11).

If eligibility, the allocation or the payroll gate changes, revise the exemption and catch up required payments at the next applicable instalment date, rather than waiting for the annual return. The ministry advises against taking an upfront exemption if the expected payroll exceeds the gate or no group member operated for a full year; calculate and reconcile the eventual allowable amount. Retain the monthly remittance statement and proof of receipt. If a due date falls on a weekend/public holiday, the ministry permits the next business day. [Exemption adjustments](https://www.ontario.ca/document/employer-health-tax-eht/tax-exemption); [association catch-up](https://www.ontario.ca/document/employer-health-tax-eht/associated-employers); [filing how-tos](https://www.ontario.ca/document/employer-health-tax-eht/filing-how-tos); [Regulation 319](https://www.ontario.ca/laws/regulation/900319).

A prior-year payroll of 1,200,000 or less can protect against **instalment interest** under section 7(1.1.1) and **late-statement penalty** under section 30(2.1.1), but specified amalgamation/transfer/winding-up predecessor rules can remove those protections. Those provisions do not replace the current-year instalment trigger. Test the actual prior year and successor rules separately before estimating sanctions. [Act sections 7(1.1.1), (1.3.1), 30(2.1.1)-(2.3.1)](https://www.ontario.ca/laws/statute/90e11).

### 8. Register, complete the right return and reconcile payment

Register when the legal employer must account for EHT. Do not wait for a fictitious 200,000 non-eligible threshold. The ministry requires an annual return where payroll exceeds the available exemption, a personalized return was received, the employer is non-eligible and has Ontario payroll, instalments were remitted, or an associated group's cumulative payroll exceeds the exemption. Charity campuses have their separate annual duty. A sole eligible, full-year, unassociated employer wholly covered by its exemption and with no other filing trigger is different from an employer sent a personalized return. Do not ignore a nil return merely because no tax is due. [Main guide: who needs to file](https://www.ontario.ca/document/employer-health-tax-eht); [charity returns](https://www.ontario.ca/document/employer-health-tax-eht/registered-charities).

Use the actual personalized return, ONT-TAXS or the official annual-return portal. **ON00150E is the annual-return replacement**, not the associated-employer allocation. The actual allocation is **2262E**. The old claim that the annual return is “6076E” is unsupported. Do not confuse the 2272E completion instructions with a personalized return. [Annual-return registry](https://forms.mgcs.gov.on.ca/en/dataset/on00150); [allocation registry](https://forms.mgcs.gov.on.ca/en/dataset/013-2262).

Complete a working paper matching the official 2272E line instructions, then map it to the actual current return/account:

| Return item | Working-paper content |
|---|---|
| Line 1 | Total Ontario remuneration for employees/former employees in the calendar year |
| Line 2 | Actual allowable exemption for this employer/account, including group/campus/day limits |
| Line 3 | Line 1 less line 2, entered as zero if negative |
| Line 4 | Rate based on total employer Ontario remuneration before exemption |
| Line 5 | Line 3 × line 4: annual tax |
| Line 6 | Actual instalments received and applicable prior-year credits used, excluding interest and penalty payments |
| Line 7 | Line 5 less line 6: balance or refund |
| Line 8 | Actual payment accompanying the return, if any |
| A / B | Association declaration / choice to apply overpayment to next year |
| Voucher 1 | Certification, authorized identity/title/date and the return itself |
| Voucher 2 | Payment only where return is filed separately; not a substitute for the return |

Check account/year, all payroll accounts, exemption totals, association form, signing authority and actual payments before certification. A Multiple Accounts Schedule is no longer required. The ON00150E download is an Adobe dynamic form; its registry establishes its identity, while the table above comes from the readable official completion instructions. Do not invent additional online fields from a PDF extraction that only shows a viewer notice. [2272E instructions, lines 1-8 and vouchers](https://forms.mgcs.gov.on.ca/dataset/8cbf9517-7f61-47d9-a942-421699ab8b67/resource/d7351997-3c9f-4af9-a418-d0b9f8c15464/download/2272e.pdf); [ON00150E](https://forms.mgcs.gov.on.ca/en/dataset/on00150).

Prepare the annual liability as employer EHT expense/payable, clear actual payments against the payable, and reconcile the closing balance to line 7 and the Ministry account. An accrual pattern for management accounts does not alter the legal instalment schedule. When ledger access is read-only, give the proposed journal/import and return working paper to the authorized accountant for approval; never treat a proposal as a posted entry.

## Rates, bands and thresholds

| Item | Calendar-2026 rule | Source |
|---|---|---|
| Ordinary eligible full-year exemption | 1,000,000, subject to eligibility, own/group gate, actual allocation and day limits  [Act sections 2-5](https://www.ontario.ca/laws/statute/90e11) |
| Ordinary full-year payroll gate | 5,000,000; relief lost above it, prorated when required  [Act sections 2-5](https://www.ontario.ca/laws/statute/90e11) |
| Rate | One of the nine rates above, from 0.98% to 1.95%  [Act sections 2-5](https://www.ontario.ca/laws/statute/90e11) |
| Required instalment threshold | Current annual employer Ontario remuneration **over 1,200,000**; cumulative first-payment method  [Act sections 2-5](https://www.ontario.ca/laws/statute/90e11) |
| Ordinary return and balance | **March 15, 2027** for calendar 2026  [Act sections 2-5](https://www.ontario.ca/laws/statute/90e11) |
| Next scheduled exemption indexing | January 1, 2029; do not assume an amount in advance  [Act sections 2-5](https://www.ontario.ca/laws/statute/90e11) |

Sources: [Act sections 2-5](https://www.ontario.ca/laws/statute/90e11); [current guide](https://www.ontario.ca/document/employer-health-tax-eht); [official exemption/rate table](https://forms.mgcs.gov.on.ca/dataset/8cbf9517-7f61-47d9-a942-421699ab8b67/resource/d7351997-3c9f-4af9-a418-d0b9f8c15464/download/2272e.pdf).

## Deadlines and filing

Ordinary 2026 annual return and final balance: **March 15, 2027**, a Monday. An instalment payment does not file the annual return. File/pay through [ONT-TAXS](https://www.ontario.ca/page/ont-taxs-online), or use the [EHT Annual Return Portal](https://services.fin.gov.on.ca/OTP/Gentax/_/) to **file without payment**; the ministry says no login/password is needed for that portal. Obtain the correct business/account information and authorized certification, not credentials from a public chat. Keep return confirmation and separate payment receipt. [Main guide and filing channels](https://www.ontario.ca/document/employer-health-tax-eht).

If online filing is unavailable, use the original preprinted return where possible, a designated ServiceOntario location or the current ministry mailing instructions. The main guide's annual-return mailing address is **Ministry of Finance, 33 King Street West, PO Box 620, Oshawa ON L1H 8E9**. Form 2262E prints a different allocation-form address; charity-registration correspondence has its own instructions. Use the address for the actual document, not one address copied onto every mailing. Returns are treated as received, not merely posted. [Main guide](https://www.ontario.ca/document/employer-health-tax-eht); [Act section 29(5)](https://www.ontario.ca/laws/statute/90e11); [2262E](https://forms.mgcs.gov.on.ca/dataset/2630e112-e9e1-49bb-9f09-7dac17b803d8/resource/cb7acbb8-bd66-4d76-b394-1db38c7e3ed2/download/2262e.pdf).

Use a supported payment channel such as ONT-TAXS, online banking or electronic funds transfer. **From December 1, 2026, financial institutions stop accepting paper remittance vouchers for in-person bill payments.** Arrange another permitted method before then; this change does not itself abolish paper returns. Annual/final/special returns are not filed at the bank. [Current payment notice](https://www.ontario.ca/document/employer-health-tax-eht); [payment options](https://www.ontario.ca/page/pay-ontario-taxes-and-charges).

Special returns require the event-specific rule rather than the ordinary March date:

- **Cessation:** section 5(2) and Regulation 319 section 3(2) require the return within **40 days** after the employer ceases to have an Ontario PE; stopping seasonal payroll alone is not that event. Ministry closure guidance covers the final return/payment; an associated employer's exemption may need a later amendment after group allocation.
- **ITA section 87 amalgamation, starting with tax year 2026:** predecessor return deadline is the **earlier of six months after amalgamation and March 15 of the following year**, under section 5(2.0.1). The old 2022 instructions' 40-day amalgamation wording is superseded. Record predecessor/successor accounts and prorate their own qualifying days/gates. A share sale alone does not change the legal employer and does not automatically require a final return.
- **Bankruptcy:** section 5(2.1) requires the pre-bankruptcy portion and applicable preceding-year return within **40 days**; section 5(6.1) gives the trustee a separate **10-day notice from appointment** rule. Section 5(12) treats pre-bankruptcy payment differently from the ordinary balance-with-return rule. Do not assume corporate dissolution, bankruptcy and amalgamation have identical payment duties.
- **All remuneration paid in one calendar month:** do not use the old 2022 PDF's special 15-day return/instalment exception for 2026. Act section 3(2)(b) was repealed effective January 1, 2025, and amended section 5(1) now states the ordinary March 15 deadline directly. Regulation 319 section 3(1)(a) still refers to the repealed clause; it does not establish that current employers satisfy it. Use the current Act's annual and instalment duties, subject to any separately applicable cessation, amalgamation, bankruptcy or actual Ministry demand.

[Act section 5](https://www.ontario.ca/laws/statute/90e11); [2026 filing how-tos](https://www.ontario.ca/document/employer-health-tax-eht/filing-how-tos); [2272E special returns](https://forms.mgcs.gov.on.ca/dataset/8cbf9517-7f61-47d9-a942-421699ab8b67/resource/d7351997-3c9f-4af9-a418-d0b9f8c15464/download/2272e.pdf).

### Penalties, interest and corrections

Under section 30(1.1), late-return penalty applies when the defined outstanding amount **D is at least 1,000**: **5% × D + 1% × D for each complete late month, maximum 12 months**. D is the section 7(1) excess amount at the due date before this penalty, not automatically total annual tax. The repeat penalty under section 30(1.2) replaces it with **10% + 2% per complete month, maximum 20**, only when the statutory demand and prior-three-year assessed-penalty conditions are met and D is at least 1,000. Section 30(1) was repealed in 2025; do not use it as current authority. [Act section 30](https://www.ontario.ca/laws/statute/90e11).

The late monthly-statement penalty is **5%** of the unpaid required instalment/portion where it is at least **1,000**, subject to the prior-payroll/successor protections described in method 7. Missing return/statement information can attract the greater of **1%** of the relevant tax/instalment and **50**, capped at **200**; other required documents have a **50** penalty. A knowing or grossly negligent incorrect statement/omission can attract **25%** of the additional tax under section 30(4). These are distinct assessed penalties, not automatic additions to every late account. [Act section 30(2)-(4)](https://www.ontario.ca/laws/statute/90e11).

Interest is **computed and compounded daily** under Ontario section 7. Obtain the actual Ministry rates for each relevant period and the actual receipt dates; rates can change quarterly. Do not use BC's monthly compounding, freeze a present rate for every period or invent an assessment without payment/history inputs. [Act section 7](https://www.ontario.ca/laws/statute/90e11); [official tax interest rate dataset](https://data.ontario.ca/dataset/tax-interest-rates).

For amendments/refunds, use ONT-TAXS or the current ministry amendment instructions and provide the reconciled return, year/account and explanation. Ministry guidance generally requires the amendment request within **four years of the return due date**. Separately, section 6(1.1) allows the Minister to refund an overpayment assessed by the Minister where a written refund application is made within **90 days after that assessment**. Do not present that assessed-overpayment route as an unlimited extension for every correction. Voluntary disclosure requires its own conditions, including approaching before audit/enforcement; it does not guarantee relief from all tax, interest or penalties. Refer an assessment dispute, proposed disclosure, arrears settlement or contested association/option/PE classification with the actual notice and dates. Do not promise a waiver or submit a disclosure from this working paper. [Act section 6](https://www.ontario.ca/laws/statute/90e11); [filing how-tos](https://www.ontario.ca/document/employer-health-tax-eht/filing-how-tos).

## Worked cases

### Case 1. Toronto tech company: correct annual tax and payment timing

Fictional AcmeDev Inc. has 12 Toronto employees, one Ontario PE and full-year eligible status. It has no associated employer or other payroll account. Calendar-2026 Ontario remuneration is **1,500,000**, comprising salaries 1,380,000, taxable benefits 90,000 and bonuses 30,000, all counted once. Monthly payroll is evenly 125,000. It validly claims 1,000,000 and its applicable instalment rate is 1.95% under the first/second-year estimate or later prior-remuneration rule. Annual tax is **9,750**. A prior-year tax figure of 4,800 would not establish the instalment trigger. [Act sections 2, 2.1 and 3](https://www.ontario.ca/laws/statute/90e11); [ministry cumulative instalment example](https://www.ontario.ca/document/employer-health-tax-eht).

September cumulative payroll is 1,125,000, below the instalment threshold. October cumulative payroll is 1,250,000: first required instalment catches up **250,000 taxable × 1.95% = 4,875**, due **November 16, 2026**, because November 15 is Sunday. November and December each generate **2,437.50**, due December 15, 2026 and January 15, 2027. Assuming those amounts were actually received, line 6 totals 9,750 and the March 15, 2027 balance is zero. Twelve payments of 812.50 would have the right annual sum but the wrong required timing. [Current timing rule](https://www.ontario.ca/document/employer-health-tax-eht); [next-business-day guidance](https://www.ontario.ca/document/employer-health-tax-eht/filing-how-tos).

Prepare the 9,750 employer expense/payable, clear the actual three payments and reconcile payroll, T4/T4A items and the EHT account. The 1,500,000 Box 14 total matches only if all facts support that result; record any actual reconciling items, with no 2% tolerance. An accountant approves the proposed entries and return.

```oa-check
name: 2026 Ontario Toronto payroll annual tax and cumulative instalments
inputs:
  salaries: 1380000
  benefits: 90000
  bonus: 30000
  exemption: 1000000
  monthly_pay: 125000
steps:
  - payroll: salaries + benefits + bonus
  - taxable: payroll - exemption
  - annual_tax: round(taxable * 0.0195, 2)
  - september_pay: monthly_pay * 9
  - october_pay: monthly_pay * 10
  - first_instalment: round((october_pay - exemption) * 0.0195, 2)
  - later_instalment: round(monthly_pay * 0.0195, 2)
  - paid: first_instalment + later_instalment * 2
  - balance: annual_tax - paid
expected:
  payroll: 1500000
  taxable: 500000
  annual_tax: 9750
  september_pay: 1125000
  october_pay: 1250000
  first_instalment: 4875
  later_instalment: 2437.50
  paid: 9750
  balance: 0
```

### Case 2. Non-eligible employers: all nine rate entries

Assume each separate employer has proven non-eligible status, the stated full-year Ontario remuneration and no exemption. Use its one selected rate on the entire base. At 175,000, tax is **1,715** despite payroll below 200,000. Exactly 200,000 uses 0.98%; the next cent enters 1.101%. Exactly 400,000 uses 1.829%; over it uses 1.95%. Do not blend marginal brackets or apply the top rate merely because eligibility is unknown. [Act section 2(2)](https://www.ontario.ca/laws/statute/90e11).

```oa-check
name: 2026 Ontario all nine single-rate entries and low-payroll liability
inputs:
  low: 175000
steps:
  - low_tax: round(low * 0.0098, 2)
  - band1: round(200000 * 0.0098, 2)
  - band2: round(230000 * 0.01101, 2)
  - band3: round(260000 * 0.01223, 2)
  - band4: round(290000 * 0.01344, 2)
  - band5: round(320000 * 0.01465, 2)
  - band6: round(350000 * 0.01586, 2)
  - band7: round(380000 * 0.01708, 2)
  - band8: round(400000 * 0.01829, 2)
  - band9: round(400001 * 0.0195, 2)
expected:
  low_tax: 1715
  band1: 1960
  band2: 2532.30
  band3: 3179.80
  band4: 3897.60
  band5: 4688
  band6: 5551
  band7: 6490.40
  band8: 7316
  band9: 7800.02
```

### Case 3. Full-year ordinary exemption boundaries

Each entity is independently eligible, unassociated and established for the full year, with no charity treatment. At 1,000,000 tax is nil. At 1,200,000 tax is 3,900, payable annually absent another payment event; exactly 1,200,000 does not require monthly instalments. At 5,000,000 the exemption remains available and tax is 78,000. At 5,000,001 the ordinary exemption is lost for the whole year, producing **97,500.02**. [Act sections 2.1 and 3](https://www.ontario.ca/laws/statute/90e11).

```oa-check
name: 2026 Ontario ordinary exemption and exact payroll gate
inputs:
  exemption: 1000000
steps:
  - fully_exempt: max(0, 1000000 - exemption) * 0.0195
  - at_instalment_threshold: round((1200000 - exemption) * 0.0195, 2)
  - at_gate: round((5000000 - exemption) * 0.0195, 2)
  - above_gate_no_exemption: round(5000001 * 0.0195, 2)
expected:
  fully_exempt: 0
  at_instalment_threshold: 3900
  at_gate: 78000
  above_gate_no_exemption: 97500.02
```

### Case 4. July start: actual days and both prorated limits

A new unassociated eligible employer first has its qualifying Ontario employer/PE facts on **July 1, 2026**, continuing through December 31: **184 of 365 days**. Ontario remuneration is 700,000. Its raw exemption is 504,109.589041... and gate 2,520,547.945205..., so it qualifies. Retaining precision and displaying cents, tax is **3,819.86**. Six-twelfths would incorrectly use a 500,000 exemption. The displayed cents are this working paper's presentation, not a claim that every return field has that rounding convention. [Act section 2.1(2), (7)](https://www.ontario.ca/laws/statute/90e11); [part-year guidance](https://www.ontario.ca/document/employer-health-tax-eht/tax-exemption).

```oa-check
name: 2026 Ontario July start daily exemption and payroll gate
inputs:
  days: 184
  year_days: 365
  payroll: 700000
steps:
  - exemption_raw: 1000000 * days / year_days
  - gate_raw: 5000000 * days / year_days
  - exemption_display: round(exemption_raw, 2)
  - gate_display: round(gate_raw, 2)
  - tax: round((payroll - exemption_raw) * 0.0195, 2)
expected:
  exemption_display: 504109.59
  gate_display: 2520547.95
  tax: 3819.86
```

### Case 5. Associated employers with an actual agreement

Two separate full-year eligible employers, associated during 2026, have Ontario payroll of 900,000 and 600,000. Group payroll 1,500,000 is within the full-year 5,000,000 gate. A valid agreement allocates 800,000 and 200,000, and the required 2262E is filed. Each selects 1.95% from its own payroll. Tax is **1,950 + 7,800 = 9,750**. Neither individual payroll exceeds 1,200,000, so aggregation for exemption sharing does not itself require monthly instalments. [Act sections 2, 2.1 and 3](https://www.ontario.ca/laws/statute/90e11); [association guide](https://www.ontario.ca/document/employer-health-tax-eht/associated-employers).

```oa-check
name: 2026 Ontario associated employers actual agreed allocation
inputs:
  a_pay: 900000
  b_pay: 600000
  a_share: 800000
  b_share: 200000
steps:
  - group_pay: a_pay + b_pay
  - allocated: a_share + b_share
  - a_tax: round((a_pay - a_share) * 0.0195, 2)
  - b_tax: round((b_pay - b_share) * 0.0195, 2)
  - total_tax: a_tax + b_tax
expected:
  group_pay: 1500000
  allocated: 1000000
  a_tax: 1950
  b_tax: 7800
  total_tax: 9750
```

### Case 6. Charity campuses cannot shelter unrelated head-office payroll

Assume an actual eligible registered charity with two proven full-year qualifying campuses and separately identified head-office payroll. Campus A has 1,400,000, campus B 600,000 and head office 200,000. Allowed campus exemptions are **1,000,000 and 600,000**, not two unrestricted millions. Combined Ontario payroll is 2,200,000, taxable base 600,000 and tax **11,700**, using the combined employer rate of 1.95%. Both campuses still have annual returns. The employer's instalment test uses combined payroll, not each campus separately. This example assumes qualification evidence; an ordinary nonprofit or shared venue would require a different computation. [O Reg 423/16 section 3(7)](https://www.ontario.ca/laws/regulation/160423); [current charity examples](https://www.ontario.ca/document/employer-health-tax-eht/registered-charities); [2020-2028 exemption instructions](https://forms.mgcs.gov.on.ca/dataset/8cbf9517-7f61-47d9-a942-421699ab8b67/resource/d7351997-3c9f-4af9-a418-d0b9f8c15464/download/2272e.pdf).

```oa-check
name: 2026 Ontario charity campus capped exemptions and head office
inputs:
  campus_a: 1400000
  campus_b: 600000
  head_office: 200000
steps:
  - total_pay: campus_a + campus_b + head_office
  - a_exemption: min(campus_a, 1000000)
  - b_exemption: min(campus_b, 1000000)
  - taxable: total_pay - a_exemption - b_exemption
  - annual_tax: round(taxable * 0.0195, 2)
expected:
  total_pay: 2200000
  a_exemption: 1000000
  b_exemption: 600000
  taxable: 600000
  annual_tax: 11700
```

### Case 7. Conditional late-return penalties, before interest

Assume statutory D is 10,000 and three complete months have elapsed. Ordinary late-return penalty is **800**. If the separate demand and prior-three-year assessed-penalty conditions are proved, the replacement repeat penalty is **1,600**; do not add both. At D = 999, this particular late-return penalty is not imposed by section 30(1.1), but other obligations, interest and sanctions are not thereby cancelled. These examples exclude interest and do not decide the liability from incomplete account history. [Act section 30(1.1)-(1.2)](https://www.ontario.ca/laws/statute/90e11).

```oa-check
name: 2026 Ontario ordinary and qualifying repeat late-return penalties
inputs:
  due_amount: 10000
  complete_months: 3
steps:
  - ordinary: round(due_amount * (0.05 + min(complete_months, 12) * 0.01), 2)
  - qualifying_repeat: round(due_amount * (0.10 + min(complete_months, 20) * 0.02), 2)
expected:
  ordinary: 800
  qualifying_repeat: 1600
```

## Boundary checks

- Confirm the employer, account, year, PE and employee connection before treating residence or a payroll address as Ontario remuneration.
- Establish legal eligibility and actual days before granting relief. Exactly the gate is different from above it; a change in control can change the allocation and require catch-up.
- Use current-year payroll for the instalment trigger, cumulative payroll for first-payment timing, and the separate statutory prior-remuneration/first-years rate rule. Prior-year tax of 600 is irrelevant.
- Distinguish the 2262E allocation, ON00150E annual return, 2272E instructions, remittance statement and payment voucher. Filing and paying are separate jobs.
- Reconcile all actual payroll/T4/T4A/option differences, all payments and all accounts. No invented 2% allowance or default allocation.
- A completed source review does not identify a professionally approving accountant. This version remains Not yet approved until a real approved accountant stands behind the actual method.

### WSIB is a separate job

| Question | Ontario EHT | WSIB |
|---|---|---|
| Governing regime | Employer Health Tax Act; Ministry of Finance | Workplace Safety and Insurance Act; WSIB |
| Base | Ontario employment remuneration, without a general per-worker earnings cap | Its own insurable earnings/coverage rules and applicable maximum |
| 2026 worker earnings ceiling | No equivalent general EHT ceiling | **121,700** maximum insurable earnings, compared with 117,000 for 2025 |
| Rate | Selected EHT rate above | Employer classification/actual WSIB rate; not the EHT rate |
| Coverage and filings | Eligibility, tax and return tests in this method | Determine coverage, reporting frequency and separate reconciliation duty; annual/quarterly reporters do not automatically need annual reconciliation |

WSIB coverage is generally mandatory for Schedule 1 Part I and Schedule 2 activities unless excluded; Schedule 1 Part II businesses may apply for coverage. Schedule 1 employers contribute to the insurance fund; Schedule 2 employers instead pay their own benefit costs and administration charges. This boundary is not a classification decision for a particular business. [WSIB coverage-status policy](https://www.wsib.ca/en/operational-policy-manual/coverage-status).

Never use the EHT base to calculate WSIB without its own inclusions/exclusions and cap. Refer coverage, premium classification, rates, clearance and reconciliation to the WSIB method or an Ontario payroll specialist. The current cap is provided only to correct the old comparison, not as a full WSIB computation. [WSIB 2026 premium rates](https://www.wsib.ca/en/2026premiumrates); [premium/earnings calculation](https://www.wsib.ca/en/businesses/premiums-and-payment/how-calculate-your-premium-and-insurable-earnings); [reconciliation](https://www.wsib.ca/en/reconcileyouraccount).

## When to refuse or refer

Prepare supported routine work, but stop the affected conclusion and give the accountant the facts, alternatives, source and deadline where there is contested public/quasi-public eligibility, a complex campus qualification, disputed association or overlapping acquisition groups, options timing/valuation or changing CCPC status, unclear partnership/JV/foreign-employer arrangements, bankruptcy/receivership, an assessment dispute, voluntary disclosure or arrears settlement. Do not substitute an arbitrary “conservative” charge for a legal classification. WSIB compliance remains separate. [Act sections 1-7 and 30](https://www.ontario.ca/laws/statute/90e11); [filing/correction guidance](https://www.ontario.ca/document/employer-health-tax-eht/filing-how-tos).

Give the authorized accountant the proposed return and journal/import, source-year/version, legal eligibility/PE analysis, payroll reconciliation, actual allocation, instalment/payment history, balance/refund, unresolved items and filing dates. Obtain approval to certify, submit, pay or post; a read-only ledger can still receive the completed proposed work for human sign-off.

## Sources

Read **November 13, 2026**. Current official enacted law and ministry instructions are used above; historical material is identified by year. The law's consolidation is from November 27, 2025, with the displayed e-Laws currency date November 10, 2026. Direct automated HTML requests returned 403 for some Ontario pages; their public pages were actually read in the ordinary browser, and the official Word Act and readable PDF instructions were downloaded. No login, access control bypass or live filing was used.

1. [Employer Health Tax Act, RSO 1990, c E.11](https://www.ontario.ca/laws/statute/90e11): definitions/PE/remuneration/association section 1; rates and option designated years section 2; exemption and post-2024 groups sections 2.1-2.1.1; instalments section 3; foreign personnel section 4; returns section 5; daily-compounded interest section 7; received delivery section 29; conditional penalties section 30. Section 2.2 is historical options relief, not group sharing.
2. [Current EHT guide](https://www.ontario.ca/document/employer-health-tax-eht), [tax exemption](https://www.ontario.ca/document/employer-health-tax-eht/tax-exemption), [associated employers](https://www.ontario.ca/document/employer-health-tax-eht/associated-employers), [permanent establishment](https://www.ontario.ca/document/employer-health-tax-eht/permanent-establishment), [remuneration](https://www.ontario.ca/document/employer-health-tax-eht/remuneration), [registered charities](https://www.ontario.ca/document/employer-health-tax-eht/registered-charities), [filing how-tos](https://www.ontario.ca/document/employer-health-tax-eht/filing-how-tos). Resolve stale charity amount, overly broad CCPC summary and arithmetic examples as described above; the current 2026 amalgamation rule supersedes the old instruction PDF. The old single-pay-month exception was repealed effective 2025 despite the stale regulation/PDF cross-reference.
3. [O Reg 423/16, registered charities](https://www.ontario.ca/laws/regulation/160423), [Regulation 319, general](https://www.ontario.ca/laws/regulation/900319), [2025 c 15, Schedule 9](https://www.ontario.ca/laws/statute/s25015) amending amalgamation deadlines.
4. [2272E return completion instructions, edition 2022/12](https://forms.mgcs.gov.on.ca/dataset/8cbf9517-7f61-47d9-a942-421699ab8b67/resource/d7351997-3c9f-4af9-a418-d0b9f8c15464/download/2272e.pdf): readable lines, rates, 2020-2028 amount, vouchers and historical special-return instructions; its amalgamation deadline and one-pay-month exception are superseded. [2262E allocation, edition 2025/02](https://forms.mgcs.gov.on.ca/dataset/2630e112-e9e1-49bb-9f09-7dac17b803d8/resource/cb7acbb8-bd66-4d76-b394-1db38c7e3ed2/download/2262e.pdf): actual allocation fields/instructions. [ON00150E annual-return registry](https://forms.mgcs.gov.on.ca/en/dataset/on00150): annual-return identity; the dynamic PDF's fields were not exposed by text extraction. No Form 6076E was verified.
5. [Ontario tax interest rates](https://data.ontario.ca/dataset/tax-interest-rates) for the actual relevant periods, not a fixed assumed assessment rate; [WSIB 2026 rates/earnings ceiling](https://www.wsib.ca/en/2026premiumrates) and [WSIB reconciliation](https://www.wsib.ca/en/reconcileyouraccount) for the separate scope boundary.

**Not yet confirmed:** the actual authenticated account screen and final calendar-2026 personalized return layout, assessment-period interest rates for a specific case, and any disputed CCPC transition, public-control or campus facts. Use the readable official field instructions without claiming the dynamic replacement PDF was field-inspected. No named accountant has approved this version.
