---
name: or-cat
description: "Oregon 2026 CAT: taxpayer and unitary group, nexus conflict, separate registration/filing/payment gates, sourced receipts, eligible labor/COGS subtraction, estimates and retained worked cases."
jurisdiction: US-OR
category: state-tax
domain: tax
tax_year: 2026
tier: 2
type: computation
version: "0.2"
last_updated: 2026-11-13
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Oregon Corporate Activity Tax, 2026

> **General reference only.** This skill provides working papers and a filing brief, not accountant approval. Apply cited law to verified facts, identify assumptions and unresolved issues, and obtain qualified professional review before filing or acting. Circular 230 section 10.37 requires reasonable factual and legal analysis.

## Scope

Oregon (US-OR) Corporate Activity Tax for tax year 2026, including sole proprietors, partnerships, LLCs, S corporations, C corporations and mandatory unitary groups. Despite the name, CAT is not limited to corporations. It is separate from individual income tax, corporate excise/income tax, local business taxes, employer transit and general sales tax. This skill produces the commercial-activity and subtraction workpaper, threshold decisions and filing brief.

The statute and current DOR CAT page support the ongoing structure. Published Form OR-CAT boxes and detailed procedural examples below are the **2025-2026 filing cycle**, pending final 2026 instructions. The 2025 edition of ORS carries later-operative versions and 2026 amendment notices; do not treat every displayed provision or former exclusion as automatically effective throughout 2026. Specialized pharmacy, construction and utility changes require the operative enactment before claiming an exclusion.

Federal business income, COGS and deductions are inputs from `us-schedule-c-and-se-computation`, `us-form-1065-partnership` or `us-form-1120-c-corp`, as appropriate. Federal CAT deductibility is resolved there, not asserted here as an automatic same-year deduction. Use `or-income-tax` for owners, `or-corporate-tax` for corporate net-income tax and `or-payroll` for employment/transit contributions. No federal numerical threshold is copied here.

## Ask the client first

- What legal/tax entities, ownership percentages, functional integration, reporting entity and year-end apply?
- What Oregon property, people, customers, services, authorization and recurring market activity establish nexus?
- What total and Oregon-source receipts, exclusions, returns/allowances, transferred property and accounting method are supported?
- What eligible COGS/farming inputs, employee-level compensation, owner payments and excluded-receipt costs are documented?
- What general/substitute apportionment method, Oregon/total activity ratio, non-U.S. members or special-industry factors apply?
- What registration date, prior liability, estimated payments, extension, short year and agency notices affect compliance?

## The method, step by step

### 1. Establish taxpayer, group and nexus before thresholds

Determine excluded-person status, including qualifying exempt/governmental entities and applicable unrelated business income. An exempt legal label does not excuse taxable unrelated activity automatically. The entity list includes federally disregarded entities; decide CAT's taxpayer/group before using a federal return identity. Sole proprietors and pass-throughs can owe CAT at the business/group level even when income tax flows to owners. [ORS 317A.100(4),(14),(17)](https://www.oregonlegislature.gov/bills_laws/ors/ors317A.html); [DOR CAT who is subject](https://www.oregon.gov/dor/programs/businesses/Pages/corporate-activity-tax.aspx).

A CAT unitary group requires **more than 50%** direct/indirect common ownership and a unitary business. Exactly 50% is not enough on that ownership test. Unitary evidence includes centralized management, shared administration/economies of scale or functional integration/flows of goods, capital or services. Common brand/purchasing/back office are factual evidence, not an automatic conclusion for every holding company. Federal consolidation or a federal affiliate definition does not by itself establish CAT membership. [ORS 317A.100(19)-(20),106](https://www.oregonlegislature.gov/bills_laws/ors/ors317A.html).

Register, file and pay as a single unitary taxpayer through the designated CAT entity. Exclude qualifying intermember receipts and related intermember expenses together; do not subtract internal costs after eliminating internal revenue. Members are jointly and severally liable. Submit OR-AF-CAT for required affiliates. The annual modified-group election can exclude non-U.S. members only if they have neither Oregon commercial activity nor excluded amounts otherwise sourced to Oregon. Keep the excluded-member list. If entities qualify for multiple unitary groups, apply DOR's group-priority rule rather than filing the same entity twice. [ORS 317A.106,113](https://www.oregonlegislature.gov/bills_laws/ors/ors317A.html); [DOR unitary FAQ](https://www.oregon.gov/dor/programs/businesses/Pages/corporate-activity-tax.aspx).

**Nexus conflict, not a safe harbor.** ORS 317A.116(3)-(4) lists property/payroll/activity and percentage bright-line presence as statutory sufficient nexus, together with Oregon residence/domicile and broader constitutional nexus. DOR's current FAQ nevertheless says it will not apply a bright-line nexus test and instead examines substantial/significant economic presence and regular use of Oregon's economy. Therefore amounts below the statutory lines are not a no-nexus conclusion; assess actual economic/physical facts and refer a disputed application. No Oregon office does not mean no CAT nexus. P.L. 86-272 does not protect CAT, because CAT is not a net-income tax. [ORS 317A.116](https://www.oregonlegislature.gov/bills_laws/ors/ors317A.html); [DOR nexus FAQ](https://www.oregon.gov/dor/programs/businesses/Pages/corporate-activity-tax.aspx).

| Item / condition | Rate, amount or threshold | Official source |
|---|---|---|
| Statutory sufficient property presence, not DOR safe harbor | At least $50,000 Oregon property; owned property original cost, rented property eight times net annual rent; alternative nexus can apply below this | https://www.oregonlegislature.gov/bills_laws/ors/ors317A.html |
| Statutory sufficient payroll presence, not DOR safe harbor | At least $50,000 Oregon payroll under the statute, including specified controlled/service payments | https://www.oregonlegislature.gov/bills_laws/ors/ors317A.html |
| Statutory sufficient activity presence, not DOR safe harbor | At least $750,000 Oregon commercial activity, or at least 25% Oregon property/payroll/activity; broader nexus can apply | https://www.oregonlegislature.gov/bills_laws/ors/ors317A.html |
| Mandatory CAT group ownership | More than 50%, plus unitary business; not exactly 50% and not a federal consolidation shortcut | https://www.oregonlegislature.gov/bills_laws/ors/ors317A.html |
| Statutory registration trigger | Commercial activity in excess of $750,000 in the tax year; the DOR summary also describes registration at $750,000 | https://www.oregonlegislature.gov/bills_laws/ors/ors317A.html |
| Annual filing trigger | Oregon commercial activity after exclusions, before subtraction, in excess of $1 million | https://www.oregonlegislature.gov/bills_laws/ors/ors317A.html |
| Tax-payment threshold | Taxable Oregon commercial activity after subtraction in excess of $1 million; no tax at or below $1 million | https://www.oregonlegislature.gov/bills_laws/ors/ors317A.html |
| CAT when tax-payment threshold met | $250 plus 0.57% of taxable commercial activity above $1 million | https://www.oregonlegislature.gov/bills_laws/ors/ors317A.html |
| Ordinary subtraction | 35% of greater eligible cost inputs or eligible labor, apportioned under applicable method; cap 95% of Oregon commercial activity | https://www.oregonlegislature.gov/bills_laws/ors/ors317A.html |
| Ordinary full-year employee labor ceiling | $500,000 compensation per employee; partners/LLC members receiving guaranteed/distributive income are not employees | https://www.oregonlegislature.gov/bills_laws/ors/ors317A.html |
| Estimated-payment trigger | Expected annual CAT liability at least $5,000, including base amount when due | https://www.oregon.gov/dor/programs/businesses/Pages/corporate-activity-tax.aspx |

### 2. Separate registration, return and tax decisions

The statute's excluded-person/registration language uses “does not exceed”/“in excess of” $750,000, while DOR's public table says both $750,000-or-less excluded and $750,000 must register. Those statements conflict at equality. The statutory rule is **over $750,000**; at exact equality document the conflict and confirm account handling rather than assert both. Operationally track the threshold and register promptly, with the source's thirty-day requirement and underlying crossing date. Registration is generally once, except mergers/reorganizations or DOR direction. [ORS 317A.100(4)(j),131](https://www.oregonlegislature.gov/bills_laws/ors/ors317A.html); [DOR registration FAQ](https://www.oregon.gov/dor/programs/businesses/Pages/corporate-activity-tax.aspx).

Filing uses Oregon commercial activity before the subtraction, while payment uses taxable commercial activity after the subtraction. A registered business with $900,000 Oregon activity ordinarily has no annual return solely from registration. A business with $1.2 million Oregon activity and a $350,000 subtraction must file but has no CAT due. It does not owe a flat $250 merely because gross activity exceeds $1 million. At exactly $1 million taxable activity, tax is zero; above it the base tax enters. [ORS 317A.125,137](https://www.oregonlegislature.gov/bills_laws/ors/ors317A.html); [DOR threshold table](https://www.oregon.gov/dor/programs/businesses/Pages/corporate-activity-tax.aspx).

For ordinary continuing taxpayers the CAT tax year follows the federal annual accounting period, including fiscal and 52-53-week years; it has not been universally calendar-only since 2021. Use the federal accounting method for commercial activity, inputs and labor consistently, and notify DOR of a year change. The cycle-specific instructions generally prorate short-year thresholds and employee labor limits, but newly formed/dissolved entities not engaged in activity for the full year have an exception. Do not prorate every short year or apply the exception to a continuing entity changing accounting period. [ORS 317A.100(18),103](https://www.oregonlegislature.gov/bills_laws/ors/ors317A.html); [OR-CAT p.7](https://www.oregon.gov/dor/forms/FormsPubs/form-or-cat-instr_106-003-1_2025.pdf).

### 3. Build commercial activity and exclusions

Begin with amounts realized from regular-course business transactions, before business expenses, under the taxpayer's accounting method. Money, property, forgiven debt and services can be receipts. Special financial institution and insurer definitions use different bases. CAT is imposed on the business, not a sales tax on each customer. A separately stated CAT recovery charged to a customer generally enters the business's commercial activity, rather than being netted as a tax collected for the state. Vehicle dealers have a specific statutory collection provision. [ORS 317A.100,116](https://www.oregonlegislature.gov/bills_laws/ors/ors317A.html); [DOR pass-through/receipts FAQ](https://www.oregon.gov/dor/programs/businesses/Pages/corporate-activity-tax.aspx).

Map each exclusion to its operative statutory paragraph and retain source records; excluded receipts are not the same as a deduction for normal expenses. The following screening list does not make every transaction in that industry exempt. [ORS 317A.100(1)(b)](https://www.oregonlegislature.gov/bills_laws/ors/ors317A.html).

| Receipt / fact | Screening treatment and condition | Official source |
|---|---|---|
| Interest | Generally excluded, but credit-sale interest and specified financial institution interest/service charges are exceptions | https://www.oregonlegislature.gov/bills_laws/ors/ors317A.html |
| Loan principal, capital contributions, qualifying equity/debt transactions | Apply the particular statutory exclusion, not a net-proceeds shortcut to ordinary sales | https://www.oregonlegislature.gov/bills_laws/ors/ors317A.html |
| Qualifying capital/business asset receipts | Check the exact statutory asset exclusion and federal classification; ordinary inventory sales are not automatically excluded | https://www.oregonlegislature.gov/bills_laws/ors/ors317A.html |
| Tax refunds and specified tax-benefit/CAT reimbursements | Use the paragraph's relationship and payment conditions | https://www.oregonlegislature.gov/bills_laws/ors/ors317A.html |
| Groceries | Statutory wholesale/retail grocery sales, including qualifying grocery consignee compensation; defined groceries exclude cannabis edibles/seeds | https://www.oregonlegislature.gov/bills_laws/ors/ors317A.html |
| Motor vehicle fuel | Defined covered fuel receipts; electricity, batteries and vehicle components are not simply motor fuel under this definition | https://www.oregonlegislature.gov/bills_laws/ors/ors317A.html |
| Agent receipts | Document agency and amounts received for another, rather than excluding the agent's own service fee | https://www.oregon.gov/dor/programs/businesses/Pages/corporate-activity-tax.aspx |
| Unitary intermember transactions | Eliminate qualifying receipts and corresponding ineligible subtraction expenses | https://www.oregonlegislature.gov/bills_laws/ors/ors317A.html |
| Agricultural cooperative sales / qualifying fluid milk receipts | Check named exclusions and farm certification/industry-average sourcing procedure | https://www.oregonlegislature.gov/bills_laws/ors/ors317A.html |
| Residential care/in-home care | Qualifying medical-assistance/Medicare compensation, not all rental or care receipts | https://www.oregon.gov/dor/programs/businesses/Pages/corporate-activity-tax.aspx |
| Receipts outside Oregon | Determine sourcing first; preserve worldwide amounts needed by subtraction method | https://www.oregonlegislature.gov/bills_laws/ors/ors317A.html |

Refunds/returns/allowances offset commercial activity in the year made as ORS 317A.116(2) specifies; do not automatically amend the original sale year for every later refund. Bad-debt credit/refund has its separate ORS 317A.140(3) condition tied to qualifying deductible debts. Avoid deducting the same refund or bad debt twice. Loan forgiveness, debt discharge and unusual noncash receipts require the exact exclusion rather than general accounting labels. [ORS 317A.116,140](https://www.oregonlegislature.gov/bills_laws/ors/ors317A.html).

The prior blanket residential-rent exclusion is not established here. Rental real estate receipts can be Oregon commercial activity; entity, regular-course and specific exclusion facts decide it. Similarly, no general construction-industry or professional-service exemption is inferred. Former 15% residential construction subcontractor labor and small-pharmacy prescription-drug provisions have time-limited notes in the compiled statute. This skill does not claim them for 2026 without confirming later operative law. The legislature's 2026 amendment-table PDF could not be opened by the research tool or a normal browser (connection closed); that access gap is explicit. A search surfaced proposed pharmacy/construction amendments, which are not treated as enacted law without the final act and effective date. [ORS 317A.122-123 and applicability notes](https://www.oregonlegislature.gov/bills_laws/ors/ors317A.html).

The 2025-2026 filing-cycle grocery instructions require separating qualifying grocery receipts from prepared/hot food, alcohol, tobacco, fuel and other sales rather than exempting an entire convenience store. Wholesale grocery exclusion requires qualifying food for resale without processing for home consumption and written purchaser certification, subject to the stated qualified SNAP-store exceptions with retained eligibility documentation. The source also uses a hot/prepared-food receipts test and other facts for a store's retail grocery status; no universal “all food” exclusion applies. Excluding all ordinary receipts can remove tax, rather than leave a mandatory $250 on excluded activity. [OR-CAT grocery instructions pp.3-4](https://www.oregon.gov/dor/forms/FormsPubs/form-or-cat-instr_106-003-1_2025.pdf).

The old broad paragraphs on lawsuit damages, insurance proceeds versus interruption coverage, dividends, nondealer vehicle/vessel/aircraft sales and federal preemption require the precise operative statutory exclusion and receipt classification before use. P.L. 86-272 is expressly unavailable for CAT. Timber, hospitals/long-term care, agricultural cooperatives, digital advertising and marketplace receipts require specialized review. No unsupported historical bill identifier, named litigation holding or claim that no constitutional challenge has succeeded is used as a tax conclusion. Those former topics remain recorded as unresolved boundaries. [ORS 317A definitions/exclusions and 116](https://www.oregonlegislature.gov/bills_laws/ors/ors317A.html).

### 4. Source each receipt, independently of subtraction apportionment

| Transaction | Oregon source rule | Official source |
|---|---|---|
| Real property sale/rent/lease/license | To extent property is in Oregon | https://www.oregonlegislature.gov/bills_laws/ors/ors317A.html |
| Tangible property rent/lease/license | To extent property is located in Oregon | https://www.oregonlegislature.gov/bills_laws/ors/ors317A.html |
| Tangible goods sale | To extent delivered to Oregon purchaser | https://www.oregonlegislature.gov/bills_laws/ors/ors317A.html |
| Services | To extent delivered to an Oregon location | https://www.oregonlegislature.gov/bills_laws/ors/ors317A.html |
| Intangible sale/rent/lease/license | To extent used in Oregon, including right-to-use allocation when receipts reflect that right | https://www.oregonlegislature.gov/bills_laws/ors/ors317A.html |
| Other financial institution/insurer activity | Oregon business under the statutory special rule | https://www.oregonlegislature.gov/bills_laws/ors/ors317A.html |

Preserve contract, delivery, user/customer location and allocation evidence. Headquarters, billing address, customer domicile and place the worker performs services need not all identify the location to which the service is delivered. For B2B SaaS or multistate services, billing address alone does not prove Oregon delivery and there is no blanket DOR acceptance stated here. If the statutory result does not fairly represent activity, ORS 317A.128(2) permits a requested/required/permitted alternative; detailed reasonable-approximation hierarchies require their actual rules. Do not silently swap billing for delivery or substitute labor location. [ORS 317A.128](https://www.oregonlegislature.gov/bills_laws/ors/ors317A.html).

Farmers can establish Oregon/outside sales through qualifying broker/processor/wholesaler certificates or the statutory prior-year industry-average method; retain the supporting method and commodity facts. Specialized insurer/financial sourcing and mixed methods require their own schedules. [ORS 317A.102,128](https://www.oregonlegislature.gov/bills_laws/ors/ors317A.html).

### 5. Compute eligible inputs and labor before subtraction

Cost inputs generally start from federally computed COGS, not all operating expenses or every SaaS hosting/API charge. A qualifying farming operation that does not report federal COGS uses operating expenses excluding labor under the statutory special definition. Validate capitalization, asset/expense classification and the federal workpaper first. [ORS 317A.100(2),102](https://www.oregonlegislature.gov/bills_laws/ors/ors317A.html); [OR-CAT pp.8-9](https://www.oregon.gov/dor/forms/FormsPubs/form-or-cat-instr_106-003-1_2025.pdf).

Labor includes eligible employee compensation such as wages, health/retirement/fringe benefits, capped per employee for the relevant period. The published return instructions expressly exclude the **employer's payroll taxes**. The FAQ's wording about employees' payroll taxes is not authority to deduct employer taxes or to subtract payroll withholding twice from gross employee wages. Partners/LLC members receiving guaranteed payments/distributive income, specified statutory employees and independent contractors are not eligible employees for this subtraction. Do not cap a partner's payment at $500,000 and call the remainder employee labor. [OR-CAT p.8](https://www.oregon.gov/dor/forms/FormsPubs/form-or-cat-instr_106-003-1_2025.pdf); [DOR labor FAQ](https://www.oregon.gov/dor/programs/businesses/Pages/corporate-activity-tax.aspx).

Under the general method, remove costs associated with noncommercial/excluded receipts and intermember transactions before comparing eligible cost inputs and labor. Costs paid by a precious-metal dealer for qualifying precious-metal items have a specific exclusion. Do not sum COGS and labor or take both 35% amounts. Preserve employee caps and excluded-receipt allocations in the workpaper even when COGS is ultimately larger. [ORS 317A.119](https://www.oregonlegislature.gov/bills_laws/ors/ors317A.html).

The **general** subtraction apportionment follows applicable ORS 314 methods/special industries, not necessarily a simple Oregon receipts/worldwide gross revenue fraction. The **substitute method** is an election approximating eligible costs with a defined commercial activity ratio: Oregon activity divided by commercial activity everywhere plus the specified excluded categories in the instructions, excluding unitary intermember transactions from both numerator and denominator. Cost treatment differs between methods. A simple Oregon/total activity ratio is appropriate in the worked cases only because they expressly assume substitute-method eligibility/election, no specified denominator exclusions and no mixed-industry method. [ORS 317A.119(3)-(6)](https://www.oregonlegislature.gov/bills_laws/ors/ors317A.html); [OR-CAT pp.8-9](https://www.oregon.gov/dor/forms/FormsPubs/form-or-cat-instr_106-003-1_2025.pdf).

The cycle-specific line 7 percentage is shown to four decimal places **as a percent**, with a calculation attachment; 85.7143% is not 0.8571%. Omission can disallow the subtraction. Mixed-method unitary subgroups require assignment of eligible costs and separate factors, then the permitted combined subtraction. An alternative apportionment request is different from the substitute election and cannot be used before DOR written approval. [OR-CAT p.9](https://www.oregon.gov/dor/forms/FormsPubs/form-or-cat-instr_106-003-1_2025.pdf).

Compute the ordinary full-year subtraction as min(35% x eligible greater cost amount x applicable factor, 95% x Oregon commercial activity). Then taxable activity is Oregon commercial activity less subtraction and any separately authorized applicable adjustment. Tax is zero if taxable activity does not exceed $1 million; otherwise $250 + 0.0057 x (taxable activity - $1 million). Use the actual year's short-period/adjustment rules rather than hardcoding that full-year model for every return. [ORS 317A.119,125](https://www.oregonlegislature.gov/bills_laws/ors/ors317A.html).

### 6. Map the workpaper onto the correct return

This is a **2025-2026 filing-cycle** map, not a claim that final 2026 boxes are published. Complete designated entity, FEIN/SSN as applicable, year dates, first/final/short indicators, federal/Oregon group differences, modified-group election, affiliates and special-industry information. Do not use a federal consolidated group list as the entire CAT group analysis. [OR-CAT pp.7-9](https://www.oregon.gov/dor/forms/FormsPubs/form-or-cat-instr_106-003-1_2025.pdf).

| Published Form OR-CAT field | Workpaper / attachment | Official source |
|---|---|---|
| Line 1 | Oregon sourced activity plus exclusions later entered on line 2 | https://www.oregon.gov/dor/forms/FormsPubs/form-or-cat-instr_106-003-1_2025.pdf |
| Line 2 | Exclusions with OR-EXC-CAT descriptions/codes and substantiation | https://www.oregon.gov/dor/forms/FormsPubs/form-or-cat-instr_106-003-1_2025.pdf |
| Line 3 | Oregon commercial activity, line 1 less line 2; filing threshold uses this stage | https://www.oregon.gov/dor/forms/FormsPubs/form-or-cat-instr_106-003-1_2025.pdf |
| Lines 4-5 | Eligible cost inputs and labor using elected general/substitute method | https://www.oregon.gov/dor/forms/FormsPubs/form-or-cat-instr_106-003-1_2025.pdf |
| Lines 6-8 | Greater-cost 35% calculation, supported factor and apportioned subtraction | https://www.oregon.gov/dor/forms/FormsPubs/form-or-cat-instr_106-003-1_2025.pdf |
| Later taxable activity/threshold/base-tax fields | Apply 95% cap and any authorized adjustment, then the zero-tax gate before base tax | https://www.oregon.gov/dor/forms/FormsPubs/form-or-cat-instr_106-003-1_2025.pdf |
| Tax/prepayment/penalty/refund fields | Reconcile full tax, actual estimated/extension payments, notices and requested refund/forward credit | https://www.oregon.gov/dor/forms/FormsPubs/form-or-cat-instr_106-003-1_2025.pdf |
| OR-AF-CAT | Required affiliate information for combined return | https://www.oregon.gov/dor/forms/FormsPubs/form-or-cat-instr_106-003-1_2025.pdf |

Do not assign an unconfirmed 2026 field number for a temporary construction/pharmacy adjustment or assume the prepayment schedule proves filing. The detailed final 2026 line map remains a stated gap. Keep books-to-receipts, exclusions, source, costs, factor, tax and payment reconciliations as separate schedules.

### 7. Estimates and final payment

Expected CAT of at least $5,000 requires quarterly estimates. For years from 2022, the cycle instructions describe a required-installment alternative based on 90% of current annual liability, prior-year liability, or qualifying annualized/seasonal methods, with each ordinary installment generally 25% of the selected annual amount. Apply the actual qualifying prior-year and method rules; the old universal 80% statement is not current. Annualization needs the prescribed period computation and seasonal method its eligibility evidence. A growing first year is not automatically penalty-free. [OR-CAT estimated payments pp.5-6, Form OR-QUP-CAT instructions](https://www.oregon.gov/dor/forms/FormsPubs/form-or-cat-instr_106-003-1_2025.pdf).

Calendar-year statutory dates are April 30, July 31, October 31 and January 31 following year-end, shifted for weekends/holidays. Actual 2026 dates are April 30, July 31, November 2, 2026 and February 1, 2027. Fiscal years use the last day of months four, seven and ten and the first month following year-end. The annual CAT return is generally due the fifteenth day of the fourth month after year-end; it is not the later corporate excise return due date. [ORS 317A.137](https://www.oregonlegislature.gov/bills_laws/ors/ors317A.html); [DOR payment FAQ](https://www.oregon.gov/dor/programs/businesses/Pages/corporate-activity-tax.aspx).

## Boundary and exception table

| Facts | Result / next work |
|---|---|
| Exactly $750,000 activity | Statute registration trigger is “in excess”; DOR summary conflicts at equality, document and confirm account handling. |
| Over registration but no more than filing threshold | Registration does not independently mandate an annual return. |
| More than filing threshold before subtraction, at/below payment threshold after it | File required return; zero CAT rather than automatic base tax. |
| No Oregon employees/property | Test significant economic presence; no P.L. 86-272 CAT defense. |
| Partner paid more than employee ceiling | Exclude guaranteed/distributive payment from employee labor; ceiling does not convert it to wages. |
| Short-year change of accounting period | Test proration; newly formed/dissolved exception cannot be assumed. |
| Refund after sale year | Apply return/allowance timing and avoid duplicate relief. |
| Claimed special construction/pharmacy/utility exclusion | Confirm operative 2026 enactment/effective date before taking it. |
| CAT and corporate income tax | Separate tax bases, ownership, nexus, returns and estimates; one payment does not satisfy the other. |

## Worked cases

All three former named business examples are retained and corrected for 2026. Scenario receipt/expense figures are invented inputs, not source-derived law. Assume full year, ordinary included taxpayer, established nexus, valid substitute-method election, no specified extra denominator exclusions, no intermember costs and no special adjustments. Workpaper precision is shown before actual form whole-dollar/percentage rounding.

### Case 1: Cascade Hardware LLC, Bend retailer

Retain $1.5 million Oregon activity, $900,000 verified COGS and $200,000 compensation/payroll-related cost total. Employer payroll taxes are ineligible labor and must be separated; even treating the entire $200,000 as an upper bound, COGS remains larger. All activity is Oregon. Subtraction is $315,000, below the $1,425,000 cap; taxable activity is $1,185,000. Tax is $1,304.50, below the estimated-payment trigger. Registration already exists, annual filing is required, and the balance is payable by the applicable return payment date. Federal deductibility and the owner's separate income tax are sent to their owner skills.

```oa-check
name: Oregon Cascade Hardware CAT 2026
inputs:
  oregon_activity: 1500000
  eligible_cogs: 900000
  labor_upper_bound: 200000
  factor: 1
steps:
  - subtraction: min(max(eligible_cogs, labor_upper_bound) * factor * 0.35, oregon_activity * 0.95)
  - taxable_activity: oregon_activity - subtraction
  - excess: max(taxable_activity - 1000000, 0)
  - cat: 250 + excess * 0.0057
expected:
  subtraction: 315000
  taxable_activity: 1185000
  excess: 185000
  cat: 1304.5
```

### Case 2: Willamette Strategy Partners LLC, Portland/Eugene services

Retain $3.5 million worldwide/$3 million Oregon activity, zero COGS, $2.4 million total compensation, eighteen employees and the $750,000 rainmaker partner payment. Clarify that the partner amount is guaranteed/distributive income included in the stated total and the other $1.65 million is eligible employee compensation, each employee below the cap with no employer payroll taxes included. The **whole partner payment is excluded**, not just $250,000 over the employee ceiling. Ratio is 3/3.5; apportioned labor is $1,414,285.714286, subtraction $495,000, taxable activity $2,505,000 and CAT $8,828.50. Estimates are required; equal payments of the full projected liability would be $2,207.125 before payment rounding. A qualifying 90%-current method has a different required amount and timing; do not conflate it with paying 100%.

```oa-check
name: Oregon Willamette partner compensation correction
inputs:
  world_activity: 3500000
  oregon_activity: 3000000
  compensation_total: 2400000
  partner_payment: 750000
steps:
  - eligible_labor: compensation_total - partner_payment
  - factor: oregon_activity / world_activity
  - subtraction: min(eligible_labor * factor * 0.35, oregon_activity * 0.95)
  - taxable_activity: oregon_activity - subtraction
  - cat: 250 + max(taxable_activity - 1000000, 0) * 0.0057
  - full_projection_quarter: cat / 4
expected:
  eligible_labor: 1650000
  subtraction: 495000
  taxable_activity: 2505000
  cat: 8828.5
  full_projection_quarter: 2207.125
```

### Case 3: PineCloud Inc., Delaware corporation headquartered in Austin

Retain $25 million worldwide activity, $1.95 million proposed Oregon activity, approximately 280 customer organizations, $3 million purported COGS, $14 million eligible employee compensation, 250 employees (the stated total averages $56,000 each) and the $480,000 CTO. The ratio is **7.8%**, not an exact 8%. Confirm the $1.95 million is delivered/used in Oregon using actual customer facts; Oregon billing addresses alone are not that proof. Assume verified eligible labor with no employer payroll taxes and no other employee over the ceiling; the CTO is below it. Hosting/API “COGS” must be reconciled federally, but even the stated $3 million upper bound is below eligible labor.

With those explicit assumptions, Oregon-apportioned labor is $1,092,000 and the subtraction $382,200, below the $1,852,500 cap. Taxable activity is $1,567,800 and CAT $3,486.46. Annual filing is required but ordinary quarterly estimates are not, because expected tax is below $5,000. Reevaluate if facts change; do not invent an 80% estimate requirement. Corporate excise/income nexus is a separate analysis in `or-corporate-tax`, not automatically the CAT sales threshold.

```oa-check
name: Oregon PineCloud sourced activity assumption
inputs:
  world_activity: 25000000
  oregon_activity: 1950000
  eligible_labor: 14000000
  cogs_upper_bound: 3000000
steps:
  - factor: oregon_activity / world_activity
  - oregon_labor: eligible_labor * factor
  - subtraction: min(max(eligible_labor, cogs_upper_bound) * factor * 0.35, oregon_activity * 0.95)
  - taxable_activity: oregon_activity - subtraction
  - cat: 250 + max(taxable_activity - 1000000, 0) * 0.0057
expected:
  factor: 0.078
  oregon_labor: 1092000
  subtraction: 382200
  taxable_activity: 1567800
  cat: 3486.46
```

### Case 4: return required, zero tax after subtraction

An invented ordinary full-year business has $1.2 million Oregon activity and $1 million eligible apportioned COGS. Its $350,000 subtraction leaves $850,000 taxable activity. Filing is required from pre-subtraction activity; payment is zero from post-subtraction activity. An alternative with only $100,000 eligible costs leaves $1,165,000 taxable activity and $1,190.50 CAT. Numeric tax-gate flags below document those already established legal scenarios; the flags are not a nexus or filing classifier.

```oa-check
name: Oregon CAT filing versus payment decision
inputs:
  activity: 1200000
  eligible_costs_a: 1000000
  eligible_costs_b: 100000
  tax_gate_a: 0
  tax_gate_b: 1
steps:
  - sub_a: min(eligible_costs_a * 0.35, activity * 0.95)
  - sub_b: min(eligible_costs_b * 0.35, activity * 0.95)
  - taxable_a: activity - sub_a
  - taxable_b: activity - sub_b
  - tax_a: (250 + max(taxable_a - 1000000, 0) * 0.0057) * tax_gate_a
  - tax_b: (250 + max(taxable_b - 1000000, 0) * 0.0057) * tax_gate_b
expected:
  taxable_a: 850000
  taxable_b: 1165000
  tax_a: 0
  tax_b: 1190.5
```

## When to refuse or refer

Refer disputed nexus, group composition or foreign elections, excluded-receipt classifications, construction/pharmacy/utility 2026 changes, special financial/insurance bases, material SaaS/user sourcing, mixed apportionment, short periods, mergers and successor collection. With incomplete receipts or labor records, do not “solve” tax with the revenue total alone. Claims for local Portland/Multnomah taxes or federal deductibility go to separate work, without unverified local rates or a guessed direct CAT credit.

## Filing and payment

Register/pay through Revenue Online where permitted, but **CAT returns cannot be filed in Revenue Online**. Use an approved e-file vendor or the correct paper return/address. Attach required affiliate/exclusion schedules and factor workpapers. Keep accepted filing separate from payment authorization and bank confirmation. The published instructions require whole-dollar return/schedule entries, with ordinary nearest-dollar rounding; examples here retain calculation precision before that reporting step. Refund claims generally use the later of three years from unextended return due date or two years after payment under the DOR FAQ, with special facts/limitations referred. An estimate overpayment alone is not a filed refund claim. For amended returns use the correct year's form/checkbox and full corrected schedules; do not amend only the net dollar difference. [DOR filing FAQ](https://www.oregon.gov/dor/programs/businesses/Pages/corporate-activity-tax.aspx); [OR-CAT pp.3-5,7-9](https://www.oregon.gov/dor/forms/FormsPubs/form-or-cat-instr_106-003-1_2025.pdf).

For years beginning in 2024 onward a seven-month filing extension is available. A federal extension automatically qualifies without a separate CAT request; retain it. For Oregon-only extension, submit OR-EXT-CAT by the original due date. This is not an extension to pay, and an OR-CAT-V payment voucher is not an extension request. Pay through Revenue Online, approved ACH or the current voucher channel, allocating the payment to the correct CAT account/year. [DOR extension/payment FAQ](https://www.oregon.gov/dor/programs/businesses/Pages/corporate-activity-tax.aspx).

Late registration can cost $100 per month up to $1,000 for the tax year, beginning no earlier than thirty days after the statutory threshold is crossed. Late payment generally adds 5% unpaid tax. In the 2025-2026 filing-cycle instructions, an extension-related exception requires a valid extension, at least 90% tax after credits paid by the original due date, timely filing within extension, full balance paid with filing and timely payment of the interest. A filing extension alone is insufficient. Failure to file more than three months after original/extended return due date can add 20%; an unheeded demand can add 25%; three consecutive nonfiling years can trigger 100%, with the FAQ's overall delinquency penalty limit. These are different triggers, not an automatic combined maximum of 25%. Interest uses the annually established rate and actual dates. The precise 2026 CAT interest-rate application is not inferred from the former erroneous “2025 8%” statement. [ORS 317A.131](https://www.oregonlegislature.gov/bills_laws/ors/ors317A.html); [DOR penalty FAQ](https://www.oregon.gov/dor/programs/businesses/Pages/corporate-activity-tax.aspx).

Estimated underpayment has a separate 5% quarterly penalty under the published instructions, with applicable prior/current-year/annualized/seasonal alternatives and a documented reasonable good-faith effort exception. It is not a universal first-year grace period or the former 80% rule. Fraud/substantial understatement amounts and stacking cannot be copied from the prior unsupported paragraph; determine them under actual governing law/notices. [OR-CAT pp.5-6, Form OR-QUP-CAT instructions](https://www.oregon.gov/dor/forms/FormsPubs/form-or-cat-instr_106-003-1_2025.pdf).

Keep receipts, invoices, source/exclusion support, cost and employee-cap records, accounting method, group lists, factors, returns and payment evidence as ORS 317A.134 requires. The prior specific six-year retention claim is unconfirmed; do not discard carryover, amendment, assessment or audit support merely because that period passed. A business sale/closure has separate successor liability/payment/notice rules under ORS 317A.146 and final-return facts. CAT's local-tax preemption has statutory exceptions; it does not mean all preexisting local income/license taxes disappear. [ORS 317A.134,146,158](https://www.oregonlegislature.gov/bills_laws/ors/ors317A.html).

## Completion checklist

- Decide included taxpayer, mandatory group and nexus with the statutory/DOR conflict recorded.
- Reconcile pre-subtraction activity, exclusions and source evidence.
- Test registration, filing and payment thresholds independently.
- Separate eligible labor/COGS, owner payments, excluded costs, chosen factor method and cap.
- Preserve all three former business scenarios with corrected arithmetic and assumptions.
- Reconcile installments, extensions, return acceptance, payment and unresolved matters.

## Sources

| Official source / section read | URL | Read on |
|---|---|---|
| ORS chapter 317A, 2025 compilation with later-operative text and 2026 amendment notices, sections 100-158. Read for definitions/exclusions, group, accounting period, nexus, sourcing, subtraction/cap, distinct thresholds, records and successor rules. | https://www.oregonlegislature.gov/bills_laws/ors/ors317A.html | 2026-11-13 |
| DOR Corporate Activity Tax page, threshold/nexus, receipts, unitary, labor, extension, payment, penalties and filing FAQ. Read for current administration, source conflicts, partner exclusion, seven-month extension, payment gate and return channel. | https://www.oregon.gov/dor/programs/businesses/Pages/corporate-activity-tax.aspx | 2026-11-13 |
| DOR 2025 Form OR-CAT instructions, pp.2-9 and estimated-payment sections; 2025-2026 filing cycle. Read for general/substitute methods, eligible labor versus employer taxes, percentage rounding, short-year exception, line map and estimates. | https://www.oregon.gov/dor/forms/FormsPubs/form-or-cat-instr_106-003-1_2025.pdf | 2026-11-13 |

Not yet confirmed: final 2026 CAT instructions/line map and complete 2026 amendment/effective-date audit, especially construction/pharmacy sunsets and utility paragraph versions; legislature 2026 amendment-table PDF returned access error, so no claim that these special exclusions continue or expire definitively in 2026; exact equality registration administration despite statutory over-$750,000 language; disputed statutory bright-line versus DOR economic-presence application; detailed SaaS/intangible reasonable-approximation hierarchy, residential-rent exclusions, damages/insurance/dividend/nondealer-asset classifications, timber/digital-advertising/marketplace special cases, historical enactment identifiers and constitutional-case claims; special insurer/financial/healthcare/agent/debt-discharge facts; mixed-group and substitute denominator details outside stated scenarios; complete 2026 CAT interest/fraud/substantial-understatement/stacking rules, numeric retention period, special first-year/prior-year estimate exceptions and notice-based relief. No old unsupported item is a usable default exemption or safe harbor.
