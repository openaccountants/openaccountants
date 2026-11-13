---
name: us-form-941-940-payroll
description: "Compute and report US federal employer payroll taxes for wages paid in 2026: Form W-4 and Publication 15-T withholding, Forms 941 and 940, deposits, Forms W-2/W-3, corrections, fringe benefits and reconciliation. Includes final 2026 FUTA credit reductions and the new W-2 tip and overtime fields."
jurisdiction: US
category: payroll
tax_year: 2026
type: filing-howto
version: 0.2
last_updated: 2026-11-13
source_checked: 2026-11-13
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: payroll
---

# US federal employer payroll: withholding, deposits and Forms 941, 940 and W-2

## Scope

Use this guide for ordinary US business employers paying employees during calendar year 2026. It covers federal income tax withholding, the reporting and deposit of employment taxes, annual FUTA, employee wage statements, corrections and reconciliation. It produces a payroll working paper, filing instructions and a reviewer package.

The companion `us-social-contributions` owns employee/employer FICA, FUTA and self-employment coverage and contribution rules. This guide applies those rules to payroll and forms. Use `us-schedule-c-and-se-computation` for a sole proprietor's own earnings and `us-1099-nec-issuance` for genuine independent contractors. An owner's draw is not an employee payroll merely because cash leaves the business.

**Answer first:** collect the employer's IRS filing assignment, the pay date and taxable wage components, the employee's effective W-4, year-to-date wages, prior deposits and the lookback-period returns. A return's due date is not its tax deposit deadline.

| Immediate decision | Rule for this guide | Official source |
|---|---|---|
| Year covered | Wages paid in 2026; ordinary annual wage reporting is due February 1, 2027 | [2026 W-2/W-3 instructions, When to file and furnishing copies](https://www.irs.gov/instructions/iw2w3) |
| Withholding method | Use the employee's actual W-4 and the matching 2026 Publication 15-T worksheet and table | [Publication 15-T, Form W-4 and section 1](https://www.irs.gov/publications/p15t) |
| Ordinary deposit schedule | Monthly if the relevant lookback liability is $50,000 or less; semiweekly if more | [Publication 15, section 11](https://www.irs.gov/publications/p15) |
| Accelerated deposit | Accumulating $100,000 within a deposit period triggers a next-business-day deposit, before subtracting nonrefundable credits | [Publication 15, section 11, Next-Day Deposit Rule](https://www.irs.gov/publications/p15) |
| Small quarterly liability | Current **or** preceding quarter's Form 941 line 12 below $2,500, with no current-quarter next-day obligation, permits timely payment with the return | [2026 Form 941 instructions, line 12](https://www.irs.gov/instructions/i941) |
| Information-return e-filing | Aggregate the information returns covered by the regulations; 10 or more generally requires electronic W-2 filing unless an exception or approved waiver applies | [2026 W-2/W-3 instructions, E-filing](https://www.irs.gov/instructions/iw2w3) |

The actual editions read were Publication 15, 15-A, 15-B and 15-T for 2026; Form 941 instructions revised March 2026; Form 941-X instructions revised April 2026; and W-2/W-3 and Form 8027 instructions for 2026. The live final Form 940 instructions still identify **2025**. Its line map below is explicitly a 2025-form reference; the 2026 FUTA calculation is supported by 2026 Publication 15 and the final DOL 2026 determination. Use the final 2026 Form 940 and Schedule A when submitting the 2026 return.

## Ask the client first

- What is the legal employer, EIN, entity type and IRS-required return: 941 or 944? Is there farm labor, household employment, an acquisition, a common paymaster, a PEO or a reporting agent?
- For every payday, what are cash wages, bonuses, reported tips, service charges, fringe benefits, reimbursements, retirement deferrals and cafeteria-plan deductions? Obtain the written benefit plans and ownership information.
- What effective W-4 does each worker have, including its year, filing status, multiple-jobs election, credits, other income, deductions, additional withholding and any IRS lock-in letter?
- What are each employee's year-to-date wages and taxes, including records from a payroll-provider change or qualifying predecessor? Which workers have foreign, family-member, statutory-employee or other special coverage?
- What liabilities were originally reported in the deposit lookback period, what deposits and prior credits have actually posted, and were any daily accumulation limits reached?
- In which states were FUTA wages subject to state unemployment tax, was that tax paid timely, and are there missing returns, disputed classifications or corrections to earlier wages or withholding?

## The method, step by step

### 1. Confirm the employee and return

Federal employment-tax status turns on the actual relationship. Consider behavioral control, financial control and the type of relationship; an agreement calling someone an independent contractor does not determine the answer. A corporate officer providing services is ordinarily an employee. Statutory employee and statutory nonemployee rules can change the result. Use Form SS-8 or refer for a determination when status is disputed. [Publication 15-A, sections 1 and 2](https://www.irs.gov/publications/p15a)

**AUDIT FLASH POINT**: worker misclassification. Wage-and-hour classification and federal employment-tax classification are distinct inquiries. Do not infer a FICA result from a DOL classification alone.

Section 530 relief requires reporting consistency, substantive consistency and a reasonable basis for the treatment. It is relief from the employer's liability, not a determination that the worker is an independent contractor. The technical-services staffing exception must be checked. [Publication 15-A, Misclassification of Employees](https://www.irs.gov/publications/p15a)

An eligible employer considering voluntary prospective reclassification can apply through Form 8952 under VCSP. The settlement payment is 10% of the employment-tax liability on the most recent year's compensation, computed using section 3509(a)'s reduced rates; it is not 10% of wages. Eligibility, audit exclusions and agreement terms require separate review. [IRS VCSP, Eligibility and Participation](https://www.irs.gov/businesses/small-businesses-self-employed/voluntary-classification-settlement-program)

| Return | Route and limits | Official source |
|---|---|---|
| Form 941 | Ordinary quarterly return for employee federal income tax withholding and FICA; continue filing unless an applicable exception, final return or seasonal treatment applies | [2026 Form 941 instructions, Who Must File](https://www.irs.gov/instructions/i941) |
| Form 944 | Annual alternative only after IRS notification; expected annual employment-tax liability of $1,000 or less can support a request, but the employer cannot switch unilaterally | [2026 Form 941 instructions, Requests to change filing requirement](https://www.irs.gov/instructions/i941) |
| Request to change 941/944 assignment | For 2026, telephone January 1 through April 1, or written request postmarked January 1 through March 16; obtain the IRS's written approval | [2026 Form 941 instructions, Requests to change filing requirement](https://www.irs.gov/instructions/i941) |
| Form 943 | Farm wages: generally cash wages of at least $150 to one employee, or at least $2,500 total cash and noncash farm wages to all employees, subject to the seasonal hand-harvest and family exceptions | [Publication 15, section 9, farmwork tests](https://www.irs.gov/publications/p15) |
| Form 945 | Nonpayroll federal income tax withholding, such as pensions, gambling and backup withholding; do not put employee wage withholding here | [Publication 15, Nonpayroll income tax withholding and section 12](https://www.irs.gov/publications/p15) |
| Backup withholding | 24% when its conditions apply; keep deposits and reporting separate from payroll. The 2026 reportable-payment threshold change does not eliminate other backup-withholding triggers | [Publication 15, What's New and nonpayroll withholding](https://www.irs.gov/publications/p15) |
| Household or special employment | Route to Schedule H, agricultural, government, religious, railroad or other applicable rules rather than assuming ordinary business payroll | [Publication 15, sections 3, 9 and 15](https://www.irs.gov/publications/p15) |

The seasonal hand-harvest exception applies to annual cash wages below $150 only when all conditions are met: hand-harvest agricultural work, customary piece-rate pay, daily commuting from the permanent home and fewer than 13 weeks of agricultural employment in the preceding year. Those wages still count toward the employer's $2,500 test. [Publication 15, section 9](https://www.irs.gov/publications/p15)

Forms 941-SS and 941-PR and Publications 51, 80 and 179 were discontinued after 2023. Do not direct a current filer to those obsolete forms or a nonexistent 2025 Publication 51. [2026 Form 941 instructions, Reminders](https://www.irs.gov/instructions/i941)

### 2. Build the taxable wages before calculating tax

Use wages **paid**, not merely earned or booked as an expense. Keep separate federal income-tax, Social Security, Medicare and FUTA bases. Apply exemptions and annual caps employee by employee. A provider change does not reset the employer's year-to-date base. Unrelated employers generally each apply their own base; qualifying successor-employer and common-paymaster rules require documented eligibility. Do not combine wages merely because businesses share an owner. [Publication 15, sections 5 and 9](https://www.irs.gov/publications/p15); [Publication 15-A, Common paymaster](https://www.irs.gov/publications/p15a)

The ordinary fringe-benefit treatments below assume a qualifying plan, employee eligibility and the applicable limit. They are not blanket exclusions for owners, discriminatory plans or excess contributions.

| Component | Federal income-tax wages | FICA wages | Reporting or condition | Official source |
|---|---|---|---|---|
| Traditional 401(k) and 403(b) employee elective deferral | Generally excluded | Included | Relevant Box 12 code; employer contributions are different | [W-2/W-3 instructions, Boxes 1, 3, 5 and 12](https://www.irs.gov/instructions/iw2w3) |
| Governmental 457(b) deferral | Generally excluded | Special deferred-compensation timing applies | Check vesting and section 3121(v)(2), rather than treating every deferral alike | [Publication 15-A, Nonqualified deferred compensation](https://www.irs.gov/publications/p15a) |
| Designated Roth employee contribution | Included | Included | Use the relevant Roth Box 12 code | [W-2/W-3 instructions, Codes AA, BB and EE](https://www.irs.gov/instructions/iw2w3) |
| Qualified cafeteria-plan health premium | Generally excluded | Generally excluded | Confirm a written section 125 plan and participant eligibility | [Publication 15-B, Cafeteria plans and Table 2-1](https://www.irs.gov/publications/p15b) |
| Qualified dependent-care assistance | Excluded within the applicable limit | Excluded within the applicable limit | Report total dependent-care benefits in Box 10; report taxable excess as wages | [W-2/W-3 instructions, Box 10](https://www.irs.gov/instructions/iw2w3) |
| Employer HSA contribution, including an employee salary reduction through a cafeteria plan | Excluded if the employee qualifies and the contribution is excludable | Excluded on those conditions | Box 12 code W; a genuine employer contribution need not arise under a cafeteria plan to qualify | [Publication 15-B, HSAs](https://www.irs.gov/publications/p15b) |
| Employee HSA contribution from after-tax pay or personal funds | Does not reduce payroll wages | Does not reduce payroll wages | Personal deduction is considered on the individual's return; do not report personal contributions as employer code W amounts | [W-2/W-3 instructions, Code W](https://www.irs.gov/instructions/iw2w3) |
| Ordinary group-term life insurance | Cost of coverage above $50,000 generally included in income, although federal income-tax withholding is not required | Taxable cost of excess coverage included, subject to special rules | Value using the IRS premium table, not face value or the premium alone; code C; special former-employee rules below | [Publication 15-B, Group-term life insurance](https://www.irs.gov/publications/p15b) |
| Qualified adoption assistance | Generally excluded from income-tax withholding within applicable conditions | Included | Box 12 code T; employee income exclusion has its own limits | [Publication 15-B, Adoption assistance and Table 2-1](https://www.irs.gov/publications/p15b) |
| Qualified transportation fringe | Generally excluded within the applicable limit | Generally excluded within the applicable limit | Apply the current benefit-specific limit and conditions | [Publication 15-B, Transportation benefits](https://www.irs.gov/publications/p15b) |
| Educational assistance | Up to $5,250 under a qualifying program; excess is taxable unless another exclusion, such as a working-condition benefit, applies | Same ordinary exclusion | Check program, nondiscrimination and owner conditions | [Publication 15-B, Educational assistance](https://www.irs.gov/publications/p15b) |
| Nonqualified deferred compensation | Income inclusion depends on the arrangement and section 409A | Special section 3121(v)(2) timing | Refer uncertain vesting, valuation or section 409A failures; do not automatically treat payment-year and vesting-year wages alike | [Publication 15-A, Nonqualified deferred compensation](https://www.irs.gov/publications/p15a) |

**Owner exception:** a more-than-2% S-corporation shareholder cannot participate as an ordinary employee in a cafeteria plan. Do not give that shareholder an ordinary employee's pretax health-premium or HSA salary-reduction treatment. The health-benefit income-tax and FICA treatments can differ. Confirm the ownership attribution and applicable benefit-specific rule. [Publication 15-B, Cafeteria plans, Accident and Health Benefits and HSAs](https://www.irs.gov/publications/p15b)

For ordinary employees, group-term life cost above the exclusion is included in Boxes 1, 3 and 5 and code C. Former-employee uncollected Social Security and Medicare taxes on that cost use codes M and N; those uncollected amounts are not entered as tax withheld in Boxes 4 and 6. Do not report uncollected Additional Medicare Tax with code N. [W-2/W-3 instructions, Codes C, M and N](https://www.irs.gov/instructions/iw2w3)

An accountable reimbursement must meet business-connection, substantiation and return-of-excess requirements; otherwise include the taxable amount in wages. Code L is not a general label for every reimbursement: it reports the substantiated part in the special allowance situation described in the W-2 instructions. [Publication 15, section 5](https://www.irs.gov/publications/p15); [W-2/W-3 instructions, Code L](https://www.irs.gov/instructions/iw2w3)

For FUTA, qualified employee salary deferrals to a 401(k) or 403(b) remain wages (Publication 15: "Taxable."), while qualifying employer retirement contributions are treated separately. Qualifying cafeteria-plan health/HSA exclusions also apply to FUTA; ordinary group-term life insurance is "Exempt" from FUTA even when excess-coverage cost is FICA wages. [Publication 15, section 15](https://www.irs.gov/publications/p15); [Publication 15-B, Table 2-1 and Group-term life](https://www.irs.gov/publications/p15b).

### 3. Apply the W-4 and 2026 withholding method

Obtain a signed W-4 when employment begins. For a new employee who provides none, use Single or Married filing separately with no other entries. A valid older W-4 can remain effective; do not translate an old allowance count into a new dollar deduction without Publication 15-T's permitted procedure. Honor an IRS lock-in letter and its effective date. [Publication 15, section 9](https://www.irs.gov/publications/p15); [Publication 15-T, Form W-4](https://www.irs.gov/publications/p15t)

A replacement W-4 must be implemented no later than the start of the first payroll period ending on or after the 30th day after receipt. An exemption claim requires no federal income-tax liability for the prior year and none expected for the current year and must be renewed annually under the instructions. It does not exempt FICA. Use the current W-4's deadline and holiday rules when administering the renewal. [Publication 15, section 9, Effective date and Exemption](https://www.irs.gov/publications/p15)

Read each field: Step 1(c) filing status; Step 2 multiple jobs; Step 3 annual credits; Step 4(a) annual other income; Step 4(b) annual deductions; Step 4(c) additional withholding **per pay period**. Use the actual current Step 3 entry; do not impose the old guide's preprinted child-credit amount on a 2026 certificate. [Publication 15-T, Form W-4](https://www.irs.gov/publications/p15t)

For an ordinary employee with a 2020-or-later W-4, Worksheet 1A works as follows:

1. Enter this pay period's federal income-tax wages on line 1a and annual pay periods on 1b; multiply for annual wages on 1c.
2. Add Step 4(a). Subtract Step 4(b) and the Worksheet 1A line 1g adjustment. The adjustment is zero if Step 2's box is checked; otherwise it is $12,900 for married filing jointly or $8,600 for the other statuses. Floor the adjusted annual wage amount at zero.
3. Use the **2026 Annual Percentage Method** schedule for the filing status and Step 2 setting. Use the standard schedule when the box is not checked and the Step 2 checkbox schedule when it is. Find the row containing the adjusted annual wages, compute its base tax plus its marginal percentage of the excess, then divide by pay periods.
4. Divide Step 3 credits by pay periods and subtract, flooring at zero.
5. Add Step 4(c)'s additional per-period withholding. Retain the worksheet and consistent rounding.

Source for the adjustments, order and table selection: [Publication 15-T, Worksheet 1A and 2026 Annual Percentage Method Tables](https://www.irs.gov/publications/p15t). Use the table itself for the full filing-status and higher-income schedules; individual Form 1040 tax brackets are not a substitute.

| Worksheet 1A item used in the examples | 2026 value | Official source |
|---|---|---|
| Monthly / semimonthly / biweekly / weekly annual pay periods | 12 / 24 / 26 / 52 | [Publication 15-T, Worksheet 1A Table 3](https://www.irs.gov/publications/p15t) |
| Other listed standard periods | Semiannual 2; quarterly 4; daily 260 | [Publication 15-T, Worksheet 1A Table 3](https://www.irs.gov/publications/p15t) |
| Standard Single/MFS adjusted annual wages from $19,900 to below $57,900 | $1,240 plus 12% of the excess over $19,900 | [Publication 15-T, section 1, Standard Single/MFS table](https://www.irs.gov/publications/p15t) |
| Separately identified supplemental wages within the statutory annual threshold, when the regular-wage withholding condition is met | Optional flat 22%, or the permitted aggregate method | [Publication 15, section 7](https://www.irs.gov/publications/p15) |
| Supplemental wages exceeding $1 million during the calendar year | Mandatory 37% on the excess, applying the related-business aggregation rules | [Publication 15, section 7](https://www.irs.gov/publications/p15) |

For the optional flat supplemental method, federal income tax must have been withheld from regular wages in the current or immediately preceding calendar year. If the condition is absent, use the required aggregate procedure. If supplemental and regular pay are combined without separately identifying the amounts, treat the total as one regular payment. FICA and FUTA still apply independently. [Publication 15, section 7](https://www.irs.gov/publications/p15)

For manual payroll, select the Publication 15-T wage-bracket or percentage worksheet matching the W-4's year and pay frequency. When the wage-bracket table cannot accommodate the wages or allowance count, use the applicable percentage method. Nonresident-alien adjustments require the special Publication 15-T procedure; refer rather than applying an ordinary resident calculation. [Publication 15-T, sections 1 through 5 and Nonresident Alien Employees](https://www.irs.gov/publications/p15t)

The 2026 certificate's Step 3 uses "$2,200" per qualifying child "under age 17" and "$500" per other dependent when the stated total-income condition is met: "$200,000 or less" or "$400,000 or less" for joint filing. Payroll uses the employee's actual signed Step 3 total. The 2026 W-4 specifies renewal by "February 16, 2027" to continue an exemption into 2027. If an exemption expires without renewal, resume prescribed default withholding; a later exempt certificate changes future wages without refunding withholding from the expired interval. [2026 Form W-4, pages 1-2](https://www.irs.gov/pub/irs-pdf/fw4.pdf); [Publication 15, section 9](https://www.irs.gov/publications/p15).

### 4. Apply contributions and keep liability dates

Load `us-social-contributions` for coverage, bases, exemptions and totalization. For ordinary covered wages in 2026, the Form 941 computational operands are:

| Form reporting operand | 2026 rule | Official source |
|---|---|---|
| Social Security | 6.2% employee and 6.2% employer; annual covered wage-and-tip base $184,500 per employee under the applicable employer rules | [2026 Form 941 instructions, lines 5a and 5b](https://www.irs.gov/instructions/i941) |
| Regular Medicare | 1.45% employee and 1.45% employer, with no wage cap | [2026 Form 941 instructions, line 5c](https://www.irs.gov/instructions/i941) |
| Additional Medicare withholding | Employee-only 0.9% on wages and tips this employer pays above $200,000 in the calendar year, regardless of filing status | [2026 Form 941 instructions, line 5d](https://www.irs.gov/instructions/i941) |

The employer does not match Additional Medicare Tax and does not substitute the employee's joint-return threshold for its withholding trigger. The employee reconciles the final liability on Form 8959.

Record tax liability on **payday**. A December wage paid in January belongs to the January wage-reporting year; a December wage with its deposit due in January remains December wages. Merely depositing in the following month cannot explain a mismatch between annual W-2 wages and the corresponding year's 941 wages. [Publication 15, sections 5 and 11](https://www.irs.gov/publications/p15)

### 5. Choose and execute the deposit schedule

For ordinary 2026 Form 941 filers, use the originally reported line 12 liabilities for July 1, 2024 through June 30, 2025. Amended return adjustments do not change this lookback calculation. A filer with Form 944 in either preceding year uses the special calendar-year lookback; for 2026 this is 2024. Forms 943, 944 and 945 also use the applicable second-preceding-calendar-year rule. Keep payroll and nonpayroll deposit obligations separate. [Publication 15, section 11, Lookback period](https://www.irs.gov/publications/p15)

| Depositor or event | Deposit timing | Official source |
|---|---|---|
| Monthly | By the 15th of the next month | [Publication 15, section 11, Monthly Deposit Schedule](https://www.irs.gov/publications/p15) |
| Semiweekly, payday Wednesday through Friday | Following Wednesday | [Publication 15, section 11, Semiweekly Deposit Schedule](https://www.irs.gov/publications/p15) |
| Semiweekly, payday Saturday through Tuesday | Following Friday | [Publication 15, section 11, Semiweekly Deposit Schedule](https://www.irs.gov/publications/p15) |
| Business-day protection | Apply legal-holiday/weekend rules; semiweekly depositors receive at least three business days after the close of the semiweekly period | [Publication 15, section 11, Deposits Due on Business Days Only](https://www.irs.gov/publications/p15) |
| Next-day trigger | $100,000 accumulated within the deposit period: next business day; start a new accumulation the next day and do not combine separate deposit periods | [Publication 15, section 11, Next-Day Deposit Rule](https://www.irs.gov/publications/p15) |
| Monthly filer triggers next-day rule | Becomes semiweekly on the next day for the rest of the current year and the following year | [Publication 15, section 11, Next-Day Deposit Rule](https://www.irs.gov/publications/p15) |
| Permitted shortfall | No more than the greater of $100 or 2% of the required deposit, with payment by the applicable makeup date | [Publication 15, section 11, Accuracy of Deposits Rule](https://www.irs.gov/publications/p15) |

For the shortfall rule, monthly depositors make up the difference by the return due date. Semiweekly depositors use the earlier of the return due date or the first Wednesday or Friday on or after the 15th of the following month. This is a limited penalty exception, not permission to budget deliberate underpayments. [Publication 15, section 11](https://www.irs.gov/publications/p15)

A new employer usually begins with zero pre-business lookback liability, but it can trigger the next-day rule immediately. Deposit frequency does not determine payroll frequency or return frequency. If a semiweekly period crosses a quarter boundary, preserve separate quarter deposits and reporting. [Publication 15, section 11](https://www.irs.gov/publications/p15)

Make federal deposits by electronic funds transfer. The current instructions allow EFTPS, IRS Direct Pay or an IRS business tax account, or an authorized provider or financial institution. Verify the available payment type, EIN, form, tax period and amount before submission. Keep the acknowledgment and confirm settlement; an accepted return is not proof of payment. [2026 Form 941 instructions, Federal tax deposits](https://www.irs.gov/instructions/i941)

The 2026 Publication 15 says EFTPS accepts same-day payments of **$1 million or less** submitted before **3:00 p.m. Eastern** on a business day. For larger payments, submit by **8:00 p.m. Eastern the preceding day**. Providers may impose earlier cutoffs. A same-day bank wire is another option, subject to the bank's process and cutoff. Do not rely on the old guide's universal preceding-day cutoff or its promised enrollment time. [Publication 15, section 11, Depositing on time and Same-day wire](https://www.irs.gov/publications/p15)

### 6. Complete Form 941 and Schedule B

Use the actual March 2026 form instructions:

| Field | Entry and check | Official source |
|---|---|---|
| Header | Correct EIN, legal name, year and quarter; identify aggregate filer status where applicable | [2026 Form 941 instructions, identification and aggregate filers](https://www.irs.gov/instructions/i941) |
| Line 1 | Employees receiving wages for the pay period including March 12, June 12, September 12 or December 12; observe listed exclusions | [2026 Form 941 instructions, line 1](https://www.irs.gov/instructions/i941) |
| Lines 2 and 3 | Federal income-tax wages and federal income tax actually withheld | [2026 Form 941 instructions, lines 2 and 3](https://www.irs.gov/instructions/i941) |
| Line 4 | Check only if no wages, tips or compensation are subject to Social Security or Medicare | [2026 Form 941 instructions, line 4](https://www.irs.gov/instructions/i941) |
| Lines 5a and 5b | Separate capped Social Security wages and reported tips in column 1; multiply each by 0.124 for column 2 | [2026 Form 941 instructions, lines 5a and 5b](https://www.irs.gov/instructions/i941) |
| Line 5c | Medicare wages and tips in column 1; multiply by 0.029 | [2026 Form 941 instructions, line 5c](https://www.irs.gov/instructions/i941) |
| Line 5d | Additional Medicare wages and tips above the employer threshold in column 1; multiply by 0.009 | [2026 Form 941 instructions, line 5d](https://www.irs.gov/instructions/i941) |
| Lines 5e, 5f and 6 | Sum column 2 of 5a through 5d; add any section 3121(q) Notice and Demand tax on 5f; line 6 also includes line 3 | [2026 Form 941 instructions, lines 5e through 6](https://www.irs.gov/instructions/i941) |
| Lines 7 through 10 | Apply actual fractions-of-cents, third-party sick-pay and tips/group-term-life adjustments; combine 6 through 9 on 10 | [2026 Form 941 instructions, lines 7 through 10](https://www.irs.gov/instructions/i941) |
| Line 11 | Qualified small-business payroll research credit from Form 8974; attach the form | [2026 Form 941 instructions, line 11](https://www.irs.gov/instructions/i941) |
| Line 12 | Line 10 less line 11, not below zero | [2026 Form 941 instructions, line 12](https://www.irs.gov/instructions/i941) |
| Line 13 | Actual deposits and applicable prior overpayment credits | [2026 Form 941 instructions, line 13](https://www.irs.gov/instructions/i941) |
| Line 14 | Balance due if line 12 exceeds 13; verify that payment with the return is permitted | [2026 Form 941 instructions, line 14](https://www.irs.gov/instructions/i941) |
| Lines 15a through 15e | Overpayment; apply/refund election; routing number, account type and account number for direct deposit | [2026 Form 941 instructions, lines 15a through 15e](https://www.irs.gov/instructions/i941) |
| Line 16 / Schedule B | Check the appropriate small-liability, monthly or semiweekly treatment; liability totals must equal line 12 | [2026 Form 941 instructions, line 16](https://www.irs.gov/instructions/i941) |
| Remaining parts | Final/seasonal return information, designee if used and authorized signature | [2026 Form 941 instructions, Parts 3 through 5](https://www.irs.gov/instructions/i941) |

Schedule B records **daily tax liabilities, not deposits**. A mid-quarter next-day trigger requires semiweekly treatment and the appropriate Schedule B. Apply any payroll research credit to the liability schedule using the instructions; do not simply spread it evenly across the quarter. [2026 Form 941 instructions, line 16 and Qualified small business payroll tax credit](https://www.irs.gov/instructions/i941)

The payroll research-credit election can be up to $500,000; the Social Security portion is subject to the $250,000 per-quarter limitation and the remaining permitted amount applies against employer Medicare under Form 8974's rules. Eligibility and the income-tax-return election belong with the research-credit guide; do not claim a credit solely because the employer incurred research costs. [2026 Form 941 instructions, Qualified small business payroll tax credit](https://www.irs.gov/instructions/i941)

COVID-era sick/family-leave lines are not current Form 941 lines. Only qualifying leave from the statutory historical periods can support the applicable credit; follow Form 941-X and the limitation-period instructions. Do not add obsolete 5a(i), 5a(ii), 11a or 13a calculations to the current form. [2026 Form 941 instructions, Reminders](https://www.irs.gov/instructions/i941)

### 7. Compute FUTA and Form 940

FUTA is an employer tax, not an employee deduction. The ordinary nonfarm, nonhousehold test is wages of at least $1,500 in any quarter of the current or preceding year, or one or more employees for some part of a day in at least 20 weeks of either year. Farm and household employment have separate tests; nonprofit and other exemptions must be checked. [Publication 15, section 14](https://www.irs.gov/publications/p15)

For routing, household FUTA applies when total household cash wages reach "$1,000 or more" in a quarter of the current or preceding year. Farm FUTA applies at "$20,000 or more" cash wages in a quarter or "10 or more farmworkers" for part of a day in "20 or more different weeks" of either year. H-2A wages count toward those farm coverage tests but remain exempt from FUTA. [Publication 15, section 14](https://www.irs.gov/publications/p15).

Apply the first $7,000 of FUTA wages per employee, subject to the applicable wage exclusions and qualifying successor-employer rule. The gross rate is 6%; the normal credit can be up to 5.4%, leaving 0.6% when the conditions are satisfied. Late state unemployment tax, wages excluded from state UI, and credit-reduction states change the result. Do not assume every employer's effective rate is 0.6%. [Publication 15, section 14](https://www.irs.gov/publications/p15)

| Final 2026 federal credit-reduction treatment | Credit reduction | Effective rate when the normal full credit otherwise applies | Official source |
|---|---|---|---|
| California | 1.5%; BCR add-on waiver approved | 2.1% | [DOL final 2026 workbook, B4 and H13](https://oui.doleta.gov/unemploy/docs/final_credit_states_2026.xlsx) |
| US Virgin Islands | 0%; advances repaid before the determining date | 0.6% | [DOL final 2026 workbook, B4 and H14](https://oui.doleta.gov/unemploy/docs/final_credit_states_2026.xlsx) |
| Other jurisdictions | No 2026 credit reduction | 0.6% subject to the ordinary credit conditions | [DOL final 2026 workbook](https://oui.doleta.gov/unemploy/docs/final_credit_states_2026.xlsx) |

The workbook is headed “Final 2026 FUTA Credit Reductions,” updated November 10, 2026. The DOL index was updated November 12. Do not use the earlier potential BCR reduction as a final rate. [DOL credit-reduction index](https://oui.doleta.gov/unemploy/futa_credit.asp)

At the ordinary 0.6% effective rate, maximum FUTA is $42 per employee ($7,000 x 0.006), before credit adjustments. The statutory basic credit reduction increases in 0.3 percentage-point steps after the second consecutive January 1 with outstanding advances, with separate possible add-ons and relief; use DOL's final determination. Its workbook describes an "additional 0.3% reduction in their FUTA credit." [Publication 15, section 14](https://www.irs.gov/publications/p15); [DOL final 2026 workbook, notes B23-B24](https://oui.doleta.gov/unemploy/docs/final_credit_states_2026.xlsx).

For multiple states, identify the FUTA-taxable wages attributable to each credit-reduction jurisdiction under Schedule A's allocation instructions. Do not apply a California reduction to all company wages merely because the company has a California office.

**Form 940 line map, latest final 2025 edition:** Part 1 identifies state unemployment and multistate/credit-reduction status. Part 2 reports total payments, exemptions and payments above the federal base, producing taxable FUTA wages and the normal-credit calculation. Part 3 adjusts for wages excluded from state unemployment tax, late state payments and Schedule A credit reduction. Part 4 totals tax, deposits, balance or overpayment. Part 5 reports quarterly liability when required. Confirm these fields against the final 2026 form before submission; do not file a draft. [2025 Form 940 instructions, Parts 1 through 5](https://www.irs.gov/instructions/i940)

Accumulate ordinary FUTA each quarter. If accumulated undeposited tax is **more than $500**, deposit by the last day of the following month; otherwise carry it forward. At year end, $500 or less may be deposited or paid with the timely return. Credit-reduction tax is a fourth-quarter liability even though its base includes the year's affected wages. [Publication 15, section 14](https://www.irs.gov/publications/p15); [2025 Form 940 instructions, When Must You Deposit](https://www.irs.gov/instructions/i940)

For historical corrections only, final 2024 Schedule A lists California and New York at "0.009 (0.9%)" and USVI at "0.042 (4.2%)": effective rates 1.5%, 1.5% and 4.8% with ordinary full credit, with no Connecticut reduction. Final 2025 Schedule A lists California at "0.012 (1.2%)" and USVI at "0.045 (4.5%)"; the 2025 Form 940 was due February 2, 2026, or February 10 if all deposits were timely. Use these only for their stated historical years, not 2026. [2024 Schedule A, page 2](https://www.irs.gov/pub/irs-prior/f940sa--2024.pdf); [2025 Schedule A, page 2](https://www.irs.gov/pub/irs-prior/f940sa--2025.pdf); [2025 Form 940 instructions](https://www.irs.gov/instructions/i940).

### 8. Prepare W-2, W-3 and tip reporting

File a W-2 when income tax or FICA was withheld, when withholding would have been required absent the applicable W-4 exemption, or when the separate wage-reporting threshold applies. For 2026 that threshold is $2,000 when no federal income, Social Security or Medicare tax was withheld; it is not a general exemption for wages below $2,000. [2026 W-2/W-3 instructions, Who Must File](https://www.irs.gov/instructions/iw2w3)

| W-2 field | Treatment | Official source |
|---|---|---|
| Boxes a through f | Correct employee SSN/name and employer EIN/name/address | [2026 W-2/W-3 instructions, identification boxes](https://www.irs.gov/instructions/iw2w3) |
| Boxes 1 and 2 | Federal income-tax wages and actual income tax withheld | [2026 W-2/W-3 instructions, Boxes 1 and 2](https://www.irs.gov/instructions/iw2w3) |
| Boxes 3 and 7 | Social Security wages excluding reported tips, and separately reported tips; combined annual base limit applies | [2026 W-2/W-3 instructions, Boxes 3 and 7](https://www.irs.gov/instructions/iw2w3) |
| Box 4 | Employee Social Security tax withheld; not the employer share | [2026 W-2/W-3 instructions, Box 4](https://www.irs.gov/instructions/iw2w3) |
| Boxes 5 and 6 | Medicare wages/tips; employee regular and Additional Medicare tax actually withheld | [2026 W-2/W-3 instructions, Boxes 5 and 6](https://www.irs.gov/instructions/iw2w3) |
| Box 8 | Allocated tips; do not duplicate them as employer-reported cash tips or automatically include them in Boxes 1, 3, 5 or 7 | [2026 W-2/W-3 instructions, Box 8](https://www.irs.gov/instructions/iw2w3) |
| Box 10 | Total dependent-care benefits, with taxable excess also reported as wages | [2026 W-2/W-3 instructions, Box 10](https://www.irs.gov/instructions/iw2w3) |
| Box 13 | Check statutory employee, retirement plan and third-party sick-pay boxes only when their respective rules apply | [2026 W-2/W-3 instructions, Box 13](https://www.irs.gov/instructions/iw2w3) |
| Box 14a | The 2026 “Other” field: separately label optional items such as after-tax premiums, union dues, state disability withholding or applicable government pension contributions | [2026 W-2/W-3 instructions, Box 14a](https://www.irs.gov/instructions/iw2w3) |
| Box 14b | Treasury Tipped Occupation Code(s) when code TP is reported; up to two codes, including “000” if any tips arose in a nonqualifying occupation | [2026 W-2/W-3 instructions, Box 14b](https://www.irs.gov/instructions/iw2w3) |
| Boxes 15 through 20 | State identity, state wages/tax, local wages/tax and locality; obtain the state/local treatment separately | [2026 W-2/W-3 instructions, Boxes 15 through 20](https://www.irs.gov/instructions/iw2w3) |

Box 12 is a code system, not a set of equivalent deductions. Preserve the applicable code and amount; use an additional W-2 if more than four code entries are needed on Copy A. [2026 W-2/W-3 instructions, Box 12](https://www.irs.gov/instructions/iw2w3)

| Codes | Meaning and essential distinction | Official source |
|---|---|---|
| A, B | Uncollected employee Social Security/RRTA and Medicare tax on tips | [2026 W-2/W-3 instructions, Codes A and B](https://www.irs.gov/instructions/iw2w3) |
| C; M, N | Taxable group-term-life cost; uncollected former-employee Social Security and Medicare taxes on that cost | [2026 W-2/W-3 instructions, Codes C, M and N](https://www.irs.gov/instructions/iw2w3) |
| D, E, F, G, H, S | Respective 401(k), 403(b), SARSEP, 457(b), section 501(c)(18)(D) and SIMPLE amounts; code G includes the specified employer contributions, and code H is included in Box 1 | [2026 W-2/W-3 instructions, individual Box 12 codes](https://www.irs.gov/instructions/iw2w3) |
| J, K | Nontaxable sick pay; 20% excise tax on excess golden-parachute payments | [2026 W-2/W-3 instructions, Codes J and K](https://www.irs.gov/instructions/iw2w3) |
| L, P, Q | Substantiated allowance amount in the prescribed reimbursement case; qualifying military/intelligence-community moving reimbursement; nontaxable combat pay | [2026 W-2/W-3 instructions, Codes L, P and Q](https://www.irs.gov/instructions/iw2w3) |
| R, T, V, W | Employer Archer MSA contributions; adoption benefits; nonstatutory stock-option income; employer HSA contributions including cafeteria-plan salary reductions | [2026 W-2/W-3 instructions, Codes R, T, V and W](https://www.irs.gov/instructions/iw2w3) |
| Y, Z | Optional reporting of section 409A deferrals; income from a noncompliant nonqualified deferred-compensation plan, respectively | [2026 W-2/W-3 instructions, Codes Y and Z](https://www.irs.gov/instructions/iw2w3) |
| AA, BB, EE | Designated Roth contributions to the respective 401(k), 403(b) and governmental 457(b) plans | [2026 W-2/W-3 instructions, Codes AA, BB and EE](https://www.irs.gov/instructions/iw2w3) |
| DD, FF | Reportable employer-sponsored health-coverage cost; permitted QSEHRA benefit, which is not merely cash reimbursed | [2026 W-2/W-3 instructions, Codes DD and FF](https://www.irs.gov/instructions/iw2w3) |
| GG, HH, II | Section 83(i) income; aggregate section 83(i) deferrals; excluded Medicaid-waiver payments | [2026 W-2/W-3 instructions, Codes GG, HH and II](https://www.irs.gov/instructions/iw2w3) |
| TA | Employer contributions under a section 128 Trump account contribution program | [2026 W-2/W-3 instructions, Code TA](https://www.irs.gov/instructions/iw2w3) |
| TP | Total cash tips reported to the employer; pair with the applicable Box 14b occupation code(s) | [2026 W-2/W-3 instructions, Code TP](https://www.irs.gov/instructions/iw2w3) |
| TT | Qualified overtime compensation: the qualifying FLSA-required premium above the regular rate, not all overtime wages | [2026 W-2/W-3 instructions, Code TT](https://www.irs.gov/instructions/iw2w3) |

Do not use retired code CC. Do not put ordinary employer retirement matching contributions into employee elective-deferral codes. Preserve separate prior-year USERRA contribution reporting where required. [2026 W-2/W-3 instructions, Box 12](https://www.irs.gov/instructions/iw2w3)

**Tips and overtime remain payroll wages under the ordinary rules.** The individual's deduction does not remove them from FICA or automatically eliminate income-tax withholding. Mandatory service charges are wages, not voluntary tips. For reported tips, apply the monthly reporting and collection rules, including the $20 monthly threshold. [Publication 15, sections 5 and 6](https://www.irs.gov/publications/p15); [2026 W-2/W-3 instructions, Codes TP and TT](https://www.irs.gov/instructions/iw2w3)

For Form 8027, test whether tipping is customary and the employer normally employed more than ten employees under the IRS hours-based test. Aggregate the relevant food/beverage operations for the test, then file separately for each qualifying establishment. The optional prior-year worksheet tests whether the computed average exceeds 80 hours; the new-business test uses the specified two consecutive months. If reported tips are below 8% of allocable gross receipts, or an approved lower rate, use the prescribed allocation method and report allocated tips in Box 8. The lower-rate approval and allocation method must be documented. [2026 Form 8027 instructions, Who Must File, worksheet and allocation](https://www.irs.gov/instructions/i8027)

An IRS section 3121(q) Notice and Demand for employer tax on unreported tips is reported on Form 941 line 5f. It is not an instruction to invent employee withholding. [2026 Form 941 instructions, line 5f](https://www.irs.gov/instructions/i941)

One W-2 accommodates "two states and two localities"; use a second W-2 for more. [W-2/W-3 instructions, Boxes 15-20](https://www.irs.gov/instructions/iw2w3).

### 9. Reconcile and correct

Reconcile the annual W-2/W-3 totals to the four Forms 941 and any adjustments before submission:

- W-3 Box 1 to total 941 line 2; Box 2 to line 3.
- Box 3 to line 5a column 1, Box 7 to line 5b column 1, and Box 5 to line 5c column 1.
- Employee Social Security tax to the employee portion of the combined tax, including tips and documented uncollected-tax adjustments.
- Employee Medicare tax to the employee regular portion plus Additional Medicare withholding, allowing documented sick-pay and other adjustments.
- Schedule B or monthly line 16 liabilities to line 12; deposits independently to line 13 and the IRS account.

Source: [2026 Form 941 instructions, Reconciling Forms 941 With Form W-3](https://www.irs.gov/instructions/i941); [2026 W-2/W-3 instructions, Reconciling Forms W-2, W-3, 941 and 943](https://www.irs.gov/instructions/iw2w3).

Document third-party sick pay, benefit timing, deferred-compensation FICA timing and genuine corrections. Do not force a difference into a rounding adjustment or assume all Social Security wages must be below Medicare wages for every special class of employment. For ordinary employees with identical coverage, an unexplained reversal is a useful error flag.

Additional wages first paid now, such as back pay, ordinarily belong to the current payment period. An error in a return's report of wages or taxes already paid is a correction to that period. [Publication 15, section 5, Back pay](https://www.irs.gov/publications/p15); [Form 941-X instructions](https://www.irs.gov/instructions/i941x)

For underreported tax, file Form 941-X by the due date of the return for the quarter in which the error was discovered and "pay the amount you owe by the time you file"; timely filing alone does not satisfy interest-free correction requirements. [941-X instructions, Underreported tax](https://www.irs.gov/instructions/i941x).

File a separate Form 941-X for each affected quarter. For underreported tax, use the adjusted-return process and satisfy the ascertainment, filing and payment deadlines for interest-free correction. Overreported tax may use adjustment or refund procedures, with the required employee repayments, reimbursements, consents and certifications. Income-tax and Additional Medicare corrections have important same-year and administrative-error restrictions; do not promise an employer refund of tax actually withheld in a prior year. [April 2026 Form 941-X instructions, Correcting federal income tax and Choosing a process](https://www.irs.gov/instructions/i941x)

Generally, an overreporting correction must be filed within three years after filing or two years after payment, whichever is later; underreporting corrections generally use the three-year period. Timely early-filed quarterly returns are treated as filed on April 15 of the next year for this purpose. Special credit and fraud rules require separate checking. [April 2026 Form 941-X instructions, Is There a Deadline](https://www.irs.gov/instructions/i941x)

Correct wage statements using W-2c/W-3c as appropriate. Use the instructions' special handling for an incorrect EIN, tax year, employee name or SSN rather than assuming one correction procedure fits every error. Supply corrected employee copies and retain SSA acceptance. FUTA corrections use an amended Form 940 with the amended box checked; there is no Form 940-X. [2026 W-2/W-3 instructions, Correcting wage reports](https://www.irs.gov/instructions/iw2w3); [2025 Form 940 instructions, Amended return](https://www.irs.gov/instructions/i940)

## Boundary and exception table

| Situation | Action | Official source |
|---|---|---|
| Resident alien employee performing ordinary US services | Ordinary federal payroll generally applies, subject to specific exemptions | [Publication 15, section 15](https://www.irs.gov/publications/p15) |
| Nonresident, treaty claim, foreign services or totalization | Determine coverage and withholding separately; use `us-cross-border-tax` and `us-social-contributions`; Forms 8233/1042 and special wage procedures are not interchangeable with ordinary W-4 payroll | [Publication 15, Nonresident aliens and section 15](https://www.irs.gov/publications/p15) |
| Family employee | Check the employer's legal form, relationship, age and specific FICA/FUTA exception; route the coverage analysis to `us-social-contributions` | [Publication 15, section 3](https://www.irs.gov/publications/p15) |
| Statutory employee | Apply the category's conditions; FICA can apply without ordinary federal income-tax withholding; use Box 13 correctly | [Publication 15-A, Statutory employees](https://www.irs.gov/publications/p15a) |
| PEO, CPEO or section 3504 agent | Establish the legal allocation of responsibilities, aggregate-filer identification and Schedule R requirements | [2026 Form 941 instructions, Aggregate return filers](https://www.irs.gov/instructions/i941) |
| Fringe benefit with uncertain eligibility or value | Obtain the plan and benefit facts; do not exclude the amount solely because payroll software labels it pretax | [Publication 15-B](https://www.irs.gov/publications/p15b) |
| State/local wages, tax or unemployment contributions | Route to the applicable state guide; federal FUTA credits do not determine state UI rates or filing obligations | [Publication 15, section 14](https://www.irs.gov/publications/p15) |

## Worked cases

### Case 1: 2026 monthly withholding with credits and extra withholding

A resident employee has $4,000 monthly federal taxable wages. Their current W-4 is Single, Step 2 unchecked, Step 3 $600, Steps 4(a) and 4(b) blank and Step 4(c) $25.

Annual wages are $48,000. Subtracting the Worksheet 1A $8,600 adjustment gives $39,400. The applicable standard Single/MFS row gives $1,240 + 12% × ($39,400 − $19,900) = $3,580 annually. Divide by twelve, subtract $50 of per-period credits and add $25: withhold $273.33. FICA is computed separately. [Publication 15-T, Worksheet 1A and Standard Single/MFS table](https://www.irs.gov/publications/p15t)

```oa-check
name: 2026 monthly withholding with W-4 credits
inputs:
  wage: 4000
  periods: 12
  adjustment: 8600
  credit: 600
  extra: 25
steps:
  - annual: wage * periods - adjustment
  - tentative: 1240 + (annual - 19900) * 0.12
  - withheld: round(max(0, tentative / periods - credit / periods) + extra, 2)
expected:
  annual: 39400
  tentative: 3580
  withheld: 273.33
```

### Case 2: choose an allowed supplemental-wage method

An employee earns $4,000 monthly and receives a separately identified $1,000 bonus. Their W-4 is Single with no adjustments and Step 2 unchecked. The employer has withheld income tax from regular wages this year and annual supplemental wages remain below the mandatory-rate threshold.

The optional flat method withholds $220 on the bonus. The aggregate method computes $418.33 on the combined $5,000, less $298.33 regular-pay withholding, leaving $120 on the bonus. Both methods are permitted on these facts; the $100 cash-flow difference does not change the employee's ultimate income-tax liability. Record the chosen method consistently and compute FICA/FUTA independently. [Publication 15, section 7](https://www.irs.gov/publications/p15); [Publication 15-T, Worksheet 1A](https://www.irs.gov/publications/p15t)

```oa-check
name: 2026 supplemental wages flat versus aggregate
inputs:
  wage: 4000
  bonus: 1000
  periods: 12
steps:
  - regular: round((1240 + (wage * periods - 8600 - 19900) * 0.12) / periods, 2)
  - combined: round((1240 + ((wage + bonus) * periods - 8600 - 19900) * 0.12) / periods, 2)
  - aggregate_bonus: combined - regular
  - flat_bonus: bonus * 0.22
  - difference: flat_bonus - aggregate_bonus
expected:
  regular: 298.33
  combined: 418.33
  aggregate_bonus: 120
  flat_bonus: 220
  difference: 100
```

### Case 3: three ordinary employees and a quarterly 941

A C-corporation's three ordinary employees receive Q2 2026 gross wages of $46,200, traditional employee 401(k) deferrals of $2,200 and qualifying cafeteria-plan health deductions of $2,000. Actual income tax withheld from their individual payroll calculations totals $5,960. None reaches a contribution cap; there are no tips, credits, sick-pay adjustments or other differences. These are not more-than-2% S-corporation shareholder benefits.

Income-tax wages are $42,000; FICA wages are $44,200. Combined Social Security tax is $5,480.80 and combined Medicare is $1,281.80. Form 941 line 12 is $12,722.60. Employee net pay is $32,658.70. The employer must report actual payday liabilities, not divide this total into three invented monthly amounts. [Publication 15-B, Table 2-1](https://www.irs.gov/publications/p15b); [2026 Form 941 instructions, lines 2 through 12](https://www.irs.gov/instructions/i941)

```oa-check
name: 2026 quarterly payroll wages and combined tax
inputs:
  gross: 46200
  retirement: 2200
  cafeteria: 2000
  fit: 5960
steps:
  - fit_wages: gross - retirement - cafeteria
  - fica_wages: gross - cafeteria
  - ss: fica_wages * 0.124
  - medicare: fica_wages * 0.029
  - line12: fit + ss + medicare
  - employee_fica: (ss + medicare) / 2
  - net_pay: gross - retirement - cafeteria - fit - employee_fica
expected:
  fit_wages: 42000
  fica_wages: 44200
  ss: 5480.80
  medicare: 1281.80
  line12: 12722.60
  net_pay: 32658.70
```

### Case 4: annual cap, Additional Medicare and W-2 reconciliation

An executive receives $25,000 monthly throughout 2026, with no exclusions or deferrals. Annual wages are $300,000. Social Security wages stop at $184,500; August's taxable Social Security wages are only $9,500, producing $589 employee tax. Additional Medicare withholding begins in September, after August brings year-to-date wages to $200,000.

The annual W-2 shows Box 3 $184,500, Box 4 $11,439, Box 5 $300,000 and Box 6 $5,250: regular Medicare $4,350 plus Additional Medicare $900. The corresponding annual combined 941 Social Security tax is $22,878; combined regular and Additional Medicare is $9,600. Do not double the Additional Medicare amount. [2026 Form 941 instructions, lines 5a through 5d](https://www.irs.gov/instructions/i941); [2026 W-2/W-3 instructions, Boxes 3 through 6](https://www.irs.gov/instructions/iw2w3)

```oa-check
name: 2026 executive wage cap and annual wage statement
inputs:
  wages: 300000
  cap: 184500
steps:
  - box3: min(wages, cap)
  - box4: box3 * 0.062
  - regular_medicare: wages * 0.0145
  - additional: max(wages - 200000, 0) * 0.009
  - box6: regular_medicare + additional
  - combined_ss: box4 * 2
  - combined_medicare: regular_medicare * 2 + additional
  - august_ss: max(0, min(25000, cap - 175000)) * 0.062
expected:
  box3: 184500
  box4: 11439
  regular_medicare: 4350
  additional: 900
  box6: 5250
  combined_ss: 22878
  combined_medicare: 9600
  august_ss: 589
```

### Case 5: final 2026 California FUTA and quarterly deposits

Twelve California employees each receive $6,000 FUTA wages in Q1 and at least another $1,000 in Q2. All wages are subject to California UI, state contributions are timely, the normal full credit otherwise applies, and there are no adjustments or prior balances.

Annual FUTA wages are $84,000. The ordinary 0.6% amount is $504; the final 1.5% California credit reduction adds $1,260, giving $1,764. Q1 ordinary FUTA is $432, carried because it does not exceed $500. Q2 adds $72, so deposit $504 by July 31, 2026. The $1,260 credit reduction is Q4 liability, deposited by February 1, 2027. It is not spread across the earlier quarters. [Publication 15, section 14](https://www.irs.gov/publications/p15); [DOL final 2026 workbook](https://oui.doleta.gov/unemploy/docs/final_credit_states_2026.xlsx)

```oa-check
name: 2026 California FUTA final credit reduction
inputs:
  employees: 12
  wage_base: 7000
  q1_per_worker: 6000
  base_rate: 0.006
  reduction: 0.015
steps:
  - taxable: employees * wage_base
  - base_tax: taxable * base_rate
  - credit_reduction: taxable * reduction
  - total: base_tax + credit_reduction
  - q1: employees * q1_per_worker * base_rate
  - q2: base_tax - q1
  - q2_deposit: q1 + q2
  - q4_deposit: credit_reduction
expected:
  taxable: 84000
  base_tax: 504
  credit_reduction: 1260
  total: 1764
  q1: 432
  q2: 72
  q2_deposit: 504
  q4_deposit: 1260
```

## When to refuse or refer

Refer disputed classification, section 530/VCSP settlements, unresolved ownership or benefit-plan treatment, foreign coverage, treaty claims, religious/government/railroad exceptions, complex deferred compensation, research-credit eligibility, historical COVID credits and contested correction periods to the relevant specialist.

This guide does not prepare state/local returns, pension-plan Form 5500, ACA Forms 1094-C/1095-C, garnishment orders, immigration advice or a complete household/agricultural payroll engagement. It preserves the routing tests above so those cases are identified before applying ordinary business rules.

**Circular 230 section 10.37 disclosure:** this is unapproved general educational guidance, not an engagement or a signed professional tax opinion. A practitioner must evaluate the actual facts, applicable law and reasonable assumptions before relying on a position or filing a return. Do not use audit risk as a reason to omit wages or tax.

## Filing and payment

| Return or obligation | 2026 period deadline | Official source |
|---|---|---|
| Form 941 Q1 | April 30, 2026; May 11 if all required deposits were timely and complete | [2026 Form 941 instructions, When Must You File](https://www.irs.gov/instructions/i941) |
| Form 941 Q2 | July 31, 2026; August 10 on the timely-deposit condition | [2026 Form 941 instructions, When Must You File](https://www.irs.gov/instructions/i941) |
| Form 941 Q3 | November 2, 2026; November 10 on the timely-deposit condition | [2026 Form 941 instructions, When Must You File](https://www.irs.gov/instructions/i941) |
| Form 941 Q4 | February 1, 2027; February 10 on the timely-deposit condition | [2026 Form 941 instructions, When Must You File](https://www.irs.gov/instructions/i941) |
| Annual Forms 943/944/945 for 2026 | February 1, 2027; February 10 if all taxes were deposited timely and in full | Regulation: "last day of the first calendar month" / "10th day of the second calendar month", with weekend adjustment; [26 CFR 31.6071(a)-1(a)(1),(d)](https://www.ecfr.gov/current/title-26/chapter-I/subchapter-C/part-31/subpart-G/section-31.6071(a)-1); [2026 Form 945 instructions](https://www.irs.gov/instructions/i945) explicitly give "February 1, 2027" / "February 10, 2027" |
| Annual FUTA return | January 31 following the wage year, adjusted to February 1, 2027; February 10 if all required deposits were timely | [Publication 15, section 14, Reporting FUTA](https://www.irs.gov/publications/p15); [2025 Form 940 instructions, general filing rule](https://www.irs.gov/instructions/i940) |
| W-2 employee copies and SSA filing | February 1, 2027, for 2026 | [2026 W-2/W-3 instructions, filing and furnishing](https://www.irs.gov/instructions/iw2w3) |
| Form 8027 | March 1, 2027 on paper; March 31 electronically | [2026 Form 8027 instructions, When To File](https://www.irs.gov/instructions/i8027) |

The adjusted Form 941 dates above apply the instructions' stated due dates and weekend/holiday rule. A filing extension does not defer a deposit. Verify separately any disaster postponement applicable to the taxpayer and obligation.

File employment returns through authorized IRS e-file software/provider procedures, or the applicable paper address when permitted. Obtain the employer's signature authorization, transmit the correct period and schedules, retain the acceptance acknowledgment, and resolve a rejection. An IRS payment portal does not by itself file the return. [2026 Form 941 instructions, Electronic filing and payment](https://www.irs.gov/instructions/i941)

For W-2, use SSA Business Services Online's wage-reporting service. Confirm access and employer authorization; enter or upload the year's wage records, verify employee identifiers and totals, submit, retain the submission receipt and monitor processing. Correct rejected records. Electronic filing supplies the transmittal information without a separate paper W-3. When paper filing is permitted, use official scannable Copy A with W-3; a printed web sample is not an acceptable scannable substitute. Furnish employee copies separately. [2026 W-2/W-3 instructions, BSO, E-filing and Paper forms](https://www.irs.gov/instructions/iw2w3)

The 10-return test aggregates covered information returns, not just W-2s. An approved hardship waiver or applicable exception can change the electronic requirement. Requests to extend filing and requests to extend employee furnishing are distinct; use Form 8809 for the applicable filing request and Form 15397 for furnishing relief under their conditions, rather than assuming an automatic extension. [2026 W-2/W-3 instructions, E-filing and Extensions](https://www.irs.gov/instructions/iw2w3)

### Penalties, interest and relief

| Failure | Ordinary rule | Official source |
|---|---|---|
| Deposit 1 through 5 calendar days late | 2% of the affected underdeposit | [Publication 15, section 11, Deposit Penalties; IRC 6656](https://www.irs.gov/publications/p15) |
| Deposit 6 through 15 days late | 5% | [Publication 15, section 11](https://www.irs.gov/publications/p15) |
| Deposit at least 16 days late, before the specified notice escalation | 10% | [Publication 15, section 11](https://www.irs.gov/publications/p15) |
| Required deposit paid directly with a return when no exception permits it | 10% | [Publication 15, section 11](https://www.irs.gov/publications/p15) |
| Still unpaid after the notice threshold | 15% after ten days from the first notice or the day immediate notice and demand is received, whichever is earlier | [Publication 15, section 11](https://www.irs.gov/publications/p15) |
| Late return | Generally 5% per whole or part month of unpaid tax, up to 25%; reduce the filing penalty by the concurrent payment penalty | [Publication 15, section 12; IRC 6651](https://www.irs.gov/publications/p15) |
| Late payment | Generally 0.5% per whole or part month, up to 25%, subject to statutory adjustments | [Publication 15, section 12; IRC 6651](https://www.irs.gov/publications/p15) |
| Willful failure by a responsible person to collect/account for/pay trust taxes | Trust Fund Recovery Penalty can equal 100% of unpaid trust-fund tax; responsibility and willfulness are factual tests | [Publication 15, section 11; IRC 6672](https://www.irs.gov/publications/p15) |
| Incorrect/late W-2 filing or furnishing, including improper paper filing | Separate information-return penalties may apply under sections 6721 and 6722; use the applicable filing-year table and correction timing | [2026 W-2/W-3 instructions, Penalties](https://www.irs.gov/instructions/iw2w3) |

Interest is separate; use the IRS rate for the relevant period and account balance rather than hard-coding one annual rate.

Reasonable-cause relief requires facts and evidence, not simply blaming a payroll provider. The IRS's current administrative-relief page describes First Time Abate and the Automatic Exemption from Penalty transition beginning in summer 2026. AEP covers eligible original 2026 quarterly returns, with three years or twelve consecutive quarters of timely compliance and additional business criteria. Check the actual IRS notice and account treatment; unpaid tax and interest remain due. Do not repeat the old guide's unsupported “once per taxpayer” lifetime restriction. [IRS administrative penalty relief, eligibility and business requirements](https://www.irs.gov/payments/administrative-penalty-relief)

## Completion checklist

- Confirm the employer, return assignment, employee status, benefit eligibility and year.
- Recompute federal withholding using each effective W-4 and the correct 2026 table.
- Reconcile gross pay to each tax base, employee deductions, employer taxes and net pay.
- Preserve year-to-date wages across provider changes and document any successor or common-paymaster treatment.
- Match payday liabilities to deposits, the lookback schedule, any next-day rule and the IRS payment record.
- Reconcile 941 line 12 to monthly liabilities or Schedule B and line 13 to actual deposits/credits.
- Reconcile annual W-2/W-3 wages and employee tax to the quarterly returns, explaining differences.
- Use the 2026 W-2 codes TP, TT and applicable TA and the 14a/14b fields where required.
- Apply final 2026 FUTA credit reductions and the actual state-credit conditions; use the final year's return at filing.
- Retain return acceptance, payment confirmation, employee-copy evidence, corrections and unresolved reviewer questions.
- For notices, follow the response deadline printed on the actual notice; do not assume a universal discrepancy-response period.

## Sources

Read dates describe the sections examined, not merely successful HTTP responses. IRS publications are primary administrative guidance; the statute controls if a conflict is identified.

| Source and portions read | URL | Read on |
|---|---|---|
| Read for Publication 15 (2026): What's New; employee status, family employment, wages, tips, supplemental pay, W-4, farmwork tests, deposits, filing, penalties and FUTA sections 2 through 15 | https://www.irs.gov/publications/p15 | 2026-11-13 |
| Read for Publication 15-T (2026): W-4 administration, nonresident adjustment, Worksheet 1A, annual percentage tables and manual-method routing | https://www.irs.gov/publications/p15t | 2026-11-13 |
| Read for Publication 15-A (2026): employee/statutory classifications, classification relief, common paymaster, third-party sick pay and deferred-compensation routing | https://www.irs.gov/publications/p15a | 2026-11-13 |
| Read for Publication 15-B (2026): cafeteria plans, Table 2-1, owner exceptions, educational assistance, group-term life and HSA treatment | https://www.irs.gov/publications/p15b | 2026-11-13 |
| Read for Form 941 instructions, March 2026: current line map, refund fields, filing calendar, payment methods, deposits, Schedule B, research credit and discontinued forms | https://www.irs.gov/instructions/i941 | 2026-11-13 |
| Read for Form 941-X instructions, April 2026: adjustment/refund processes, employee certification, income-tax restrictions and limitation periods | https://www.irs.gov/instructions/i941x | 2026-11-13 |
| Read for Form 940 instructions, 2025 final edition: return line map, credit adjustments, deposit rules, filing rule and historical 2025 figures; not represented as a final 2026 edition | https://www.irs.gov/instructions/i940 | 2026-11-13 |
| Read for W-2/W-3 instructions (2026): reporting threshold, filing/furnishing, e-file aggregation, boxes, new codes, corrections and reconciliation | https://www.irs.gov/instructions/iw2w3 | 2026-11-13 |
| Read for Form 8027 instructions (2026): hours-based employer test, establishment reporting, allocation and filing dates | https://www.irs.gov/instructions/i8027 | 2026-11-13 |
| Read for DOL credit-reduction index: final 2026 workbook link and November 12 page update | https://oui.doleta.gov/unemploy/futa_credit.asp | 2026-11-13 |
| Read for DOL Final 2026 FUTA Credit Reductions, updated November 10: workbook heading, B4 explanation, California H13 and USVI H14, and credit notes B19 through B21 | https://oui.doleta.gov/unemploy/docs/final_credit_states_2026.xlsx | 2026-11-13 |
| Read for IRS VCSP: eligibility, Form 8952 and payment calculated at 10% of liability under reduced section 3509(a) rates | https://www.irs.gov/businesses/small-businesses-self-employed/voluntary-classification-settlement-program | 2026-11-13 |
| Read for IRS administrative penalty relief: FTA/AEP transition, eligible returns, compliance history and additional business requirements | https://www.irs.gov/payments/administrative-penalty-relief | 2026-11-13 |
| Read for 2026 Form W-4, Steps 3 and exemption renewal | https://www.irs.gov/pub/irs-pdf/fw4.pdf | 2026-11-13 |
| Read for annual filing dates and deposit-compliance extension | https://www.ecfr.gov/current/title-26/chapter-I/subchapter-C/part-31/subpart-G/section-31.6071(a)-1 | 2026-11-13 |
| Read for 2026 Form 945 due dates and timely-deposit extension | https://www.irs.gov/instructions/i945 | 2026-11-13 |
| Read for historical 2024 credit-reduction states and rates, page 2 | https://www.irs.gov/pub/irs-prior/f940sa--2024.pdf | 2026-11-13 |
| Read for historical 2025 credit-reduction states and rates, page 2 | https://www.irs.gov/pub/irs-prior/f940sa--2025.pdf | 2026-11-13 |

### Exact source evidence

Short fragments below are separate verbatim excerpts; the operative sections supply conditions and derived computations.

| Source scope | Exact official wording | Official URL | Read on |
|---|---|---|---|
| Read for SS individual/employer rate and 2026 base | "6.2% each for the employee and employer"; "$184,500" | https://www.irs.gov/instructions/i941 | 2026-11-13 |
| Read for Regular Medicare | "1.45% each for the employee and employer"; "There is no wage base limit for Medicare tax." | https://www.irs.gov/instructions/i941 | 2026-11-13 |
| Read for Additional Medicare | "in excess of $200,000"; "0.9%"; "There is no employer share of Additional Medicare Tax." | https://www.irs.gov/instructions/i941 | 2026-11-13 |
| Read for Small quarterly liability | "less than $2,500 or line 12 on the prior quarterly return was less than $2,500" | https://www.irs.gov/instructions/i941 | 2026-11-13 |
| Read for Form 944 eligibility and request windows | "$1,000 or less"; "January 1, 2026, and April 1, 2026"; "January 1, 2026, and March 16, 2026" | https://www.irs.gov/instructions/i941 | 2026-11-13 |
| Read for Form 941 line 1 snapshot | "March 12, June 12, September 12, or December 12" | https://www.irs.gov/instructions/i941 | 2026-11-13 |
| Read for Form 941 combined factors | "x 0.124"; "x 0.029"; "x 0.009" | https://www.irs.gov/instructions/i941 | 2026-11-13 |
| Read for Research payroll-credit election / SS portion | "$500,000 for tax years beginning after 2022"; "up to $250,000 per quarter" | https://www.irs.gov/instructions/i941 | 2026-11-13 |
| Read for Payroll schedule threshold | "$50,000 or less"; "more than $50,000" | https://www.irs.gov/publications/p15 | 2026-11-13 |
| Read for Monthly deposit | "15th day of the following month" | https://www.irs.gov/publications/p15 | 2026-11-13 |
| Read for Semiweekly payday/deposit | "Wednesday, Thursday, and/or Friday"; "Wednesday"; "Saturday, Sunday, Monday, and/or Tuesday"; "Friday" | https://www.irs.gov/publications/p15 | 2026-11-13 |
| Read for Next-day and shortfall | "$100,000 or more"; "greater of $100 or 2%" | https://www.irs.gov/publications/p15 | 2026-11-13 |
| Read for EFTPS cutoffs | "$1 million or less"; "before 3:00 p.m. Eastern time"; "by 8:00 p.m. Eastern time the day before" | https://www.irs.gov/publications/p15 | 2026-11-13 |
| Read for Supplemental wages | "Withhold a flat 22%"; "exceeds $1 million"; "37%" | https://www.irs.gov/publications/p15 | 2026-11-13 |
| Read for Backup withholding | "The backup withholding rate remains 24%" | https://www.irs.gov/publications/p15 | 2026-11-13 |
| Read for Farm FICA tests | "$150 or more"; "$2,500 or more"; "less than 13 weeks" | https://www.irs.gov/publications/p15 | 2026-11-13 |
| Read for W-4 replacement | "30th day" | https://www.irs.gov/publications/p15 | 2026-11-13 |
| Read for FUTA standard tests/rates/base | "$1,500 or more"; "20 or more different weeks"; "6.0%"; "first $7,000"; "5.4%"; "0.6%" | https://www.irs.gov/publications/p15 | 2026-11-13 |
| Read for FUTA quarterly deposit threshold | "over $500" | https://www.irs.gov/publications/p15 | 2026-11-13 |
| Read for FUTA credit reduction timing | "incurred in the fourth quarter" | https://www.irs.gov/publications/p15 | 2026-11-13 |
| Read for Deposit penalty bands | "2%" / "1 to 5 days late"; "5%" / "6 to 15 days late"; "10%" / "16 or more days late"; "15%" / "more than 10 days after" | https://www.irs.gov/publications/p15 | 2026-11-13 |
| Read for Filing/payment penalty and TFRP | "5% of the unpaid tax"; "25%"; "0.5% per month"; "100% of the unpaid trust fund tax" | https://www.irs.gov/publications/p15 | 2026-11-13 |
| Read for Worksheet 1A offsets | "$12,900"; "$8,600"; "enter -0-" | https://www.irs.gov/publications/p15t | 2026-11-13 |
| Read for Annual pay periods (Table 3) | "2"; "4"; "12"; "24"; "26"; "52"; "260" | https://www.irs.gov/publications/p15t | 2026-11-13 |
| Read for Single/MFS standard bracket used | "$19,900"; "$57,900"; "$1,240.00"; "12%"; "$19,900" | https://www.irs.gov/publications/p15t | 2026-11-13 |
| Read for GTL exclusion and education | "$50,000"; "$5,250" | https://www.irs.gov/publications/p15b | 2026-11-13 |
| Read for S-corp shareholder condition | "more than 2%" | https://www.irs.gov/publications/p15b | 2026-11-13 |
| Read for W-2 threshold, e-file, tip reporting | "$2,000 or more"; "at least 10 returns"; "$20 or more per month" | https://www.irs.gov/instructions/iw2w3 | 2026-11-13 |
| Read for Code K and 14b | "20% excise tax"; "up to two code(s)"; "000" | https://www.irs.gov/instructions/iw2w3 | 2026-11-13 |
| Read for Form 8027 tests | "more than 10 employees"; "greater than 80 (hours)"; "2 consecutive calendar months"; "8%" | https://www.irs.gov/instructions/i8027 | 2026-11-13 |
| Read for Form 8027 due dates | "March 1, 2027"; "March 31, 2027" | https://www.irs.gov/instructions/i8027 | 2026-11-13 |
| Read for 941-X limitations | "within 3 years"; "2 years"; "whichever is later"; "April 15 of the succeeding year" | https://www.irs.gov/instructions/i941x | 2026-11-13 |
| Read for AEP start/history | "summer 2026"; "2026 quarterly returns"; "three prior years (or 12 consecutive quarters" | https://www.irs.gov/payments/administrative-penalty-relief | 2026-11-13 |
| Read for VCSP settlement | "10 percent of the employment tax liability"; "most recent tax year" | https://www.irs.gov/businesses/small-businesses-self-employed/voluntary-classification-settlement-program | 2026-11-13 |
| Read for Final 2026 CA/USVI | "1.5% credit reduction"; H14 numeric "0"; "0.6% + the FUTA credit reduction" | https://oui.doleta.gov/unemploy/docs/final_credit_states_2026.xlsx | 2026-11-13 |

Not yet confirmed: the final 2026 Form 940 and Schedule A field layout was not available in the final instructions opened; use the verified 2026 substantive calculation above and check the final form before filing. Client-specific treaty eligibility, benefit-plan validity, special coverage, disaster relief, penalty-abatement entitlement and individual account balances require the client's evidence. No unpublished draft-form field or potential FUTA rate is treated as final guidance.

This version is tier 2 and has not been approved by a named accountant.
