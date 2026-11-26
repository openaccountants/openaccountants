---
name: fl-corporate-income-tax
description: "Source-cited tax guide for US-FL: fl corporate income tax. Unverified draft, pending local-accountant review."
jurisdiction: US-FL
tax_year: 2025
tax_year_notes: "2025–2026 filing cycle: 2025 taxable-year computations and returns filed in 2026; not 2026 taxable-year guidance."
last_updated: 2026-11-26
version: "1.2"
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
reviewed_by: "Rob Hoffman"
reviewed_on: 2026-11-03
tier: 1
domain: income-tax
type: computation
---

# FL Corporate Income Tax

This Guide covers ordinary Florida corporate income tax for tax year 2025 and the related 2026 filing cycle. The ordinary rate is **5.5%**, after the available **$50,000 income exemption**. [DOR tax base and rates](https://floridarevenue.com/taxes/taxesfees/Pages/corporate.aspx); [section 220.14](https://www.flsenate.gov/Laws/Statutes/2025/220.14).

> **Accountant approval hold:** The existing approval fields are preserved. They do not approve this changed version. Accountant approval of the changes remains required. Conditional examples are not completed returns.

## Required inputs

Obtain the actual tax year and year-end, federal classification and return, ownership chain and controlled-group members, Florida activities, federal taxable income and deductions, depreciation schedules and asset dates, prior Florida loss/recovery schedules, Florida/everywhere factor amounts, nonbusiness income, credit approvals, payments and extension confirmations. Do not infer missing eligibility from a company name or a hypothetical calculation.

## Who this applies to

- Corporations conducting business, deriving income or existing within Florida are subject to Florida corporate income/franchise tax. An LLC classified as a corporation for both Florida and federal income-tax purposes must file a corporate return. Incorporation outside Florida does not itself remove the obligation. [DOR](https://floridarevenue.com/taxes/taxesfees/Pages/corporate.aspx).
- A single-member LLC disregarded for federal and Florida income-tax purposes has no separate Florida corporate return. A direct or indirect corporate owner must report both its own and the LLC's income, even if ownership is its only activity. Disregarded status does not universally mean Schedule C. [DOR](https://floridarevenue.com/taxes/taxesfees/Pages/corporate.aspx).
- An LLC classified as a partnership for Florida and federal purposes files F-1065 if any owner is a corporation; the corporate owner also files a corporate income-tax return. Other partnership structures and ownership chains: **Check this point with one of our partner accountants.** [DOR](https://floridarevenue.com/taxes/taxesfees/Pages/corporate.aspx).
- S corporations paying federal income tax on Form 1120-S line 23c must file; their Florida starting income is only the income subject to federal corporate-level tax. Built-in gains, LIFO recapture, excess passive income and conversion computations: **Check this point with one of our partner accountants.** [F-1120N, pp. 2 and 5](https://floridarevenue.com/Forms_library/current/f1120n.pdf).
- Tax-exempt organizations with federal unrelated trade or business taxable income are subject to Florida corporate income tax and must file. [F-1120N, p. 2](https://floridarevenue.com/Forms_library/current/f1120n.pdf).
- Natural-person sole proprietors do not pay Florida personal income tax. This does not establish freedom from sales, employer or other taxes and fees. [DOR personal-income-tax statement](https://www.floridarevenue.com/taxes/compliance/Pages/violations.aspx).

Invalid elections, QSubs, trust ownership and remote-business nexus (including P.L. 86-272): **Check this point with one of our partner accountants.**

## Rates, bands and thresholds

| Item | Rule and operative condition | Official source |
| --- | --- | --- |
| Ordinary 2025 tax rate | 5.5% of Florida net income after the available exemption; AMT is a separate question | [DOR rate table](https://floridarevenue.com/taxes/taxesfees/Pages/corporate.aspx) |
| Exemption | $50,000 of net income, subject to section 220.14's federal-credit proviso and the short-period/group limits below | [Section 220.14(1)](https://www.flsenate.gov/Laws/Statutes/2025/220.14) |
| Historical amended-return rates | Taxable years beginning before 2019: 5.5%; beginning in 2019–2020: 4.458%; beginning in 2021: 3.535%; beginning in 2022–2025: 5.5% | [DOR rate table](https://floridarevenue.com/taxes/taxesfees/Pages/corporate.aspx) |

For a taxable year shorter than 12 months, prorate the exemption by days in that year divided by 365. A consolidated return receives one exemption. Separately filing Florida members of an IRC section 1563 controlled group also share one exemption, equally unless all such members consent to a different allocation under the prescribed procedure. [Section 220.14(2)–(4)](https://www.flsenate.gov/Laws/Statutes/2025/220.14).

AMT/CAMT applicability, historical refunds and the rate-reduction mechanism: **Check this point with one of our partner accountants.**

## The base

For an ordinary separate C-corporation return, start F-1120 line 1 with federal Form 1120 line 30, not an amount before the federal NOL deduction. A separate Florida filer in a federal consolidated group needs a separate-company federal computation and reconciliation. [F-1120N, p. 5](https://floridarevenue.com/Forms_library/current/f1120n.pdf).

Add state income taxes deducted federally, including Florida and DC; exclude gross-receipts taxes and city/county income taxes from this line. Add the federal NOL deduction separately on Schedule I line 3. [F-1120N, pp. 5–6](https://floridarevenue.com/Forms_library/current/f1120n.pdf).

**Ordinary bonus-depreciation recovery:** Once an applicable non-QIP bonus addback is established, subtract one-seventh in the addition year and each of the six following years. Do not defer the first recovery to the following year. QIP placed in service on or after January 1, 2018 has a separate recovery rule and is not covered by that seven-year instruction. [Section 220.13(1)(e)](https://www.flsenate.gov/Laws/Statutes/2025/220.13); [F-1120N, p. 8](https://floridarevenue.com/Forms_library/current/f1120n.pdf).

Current conformity/pro forma applicability to a particular 2025 return, section 179, historical federal-refund/intangible-tax adjustments, bond interest, Treasury income, WOTC wages, foreign dividends, Subpart F, GILTI and section 965: **Check this point with one of our partner accountants.** This Guide does not clear those adjustments or assume that every 2026 change applies to every 2025 return.

For a multistate ordinary-method return, remove nonbusiness income before apportionment and add the portion allocated to Florida afterward; do not apportion it and then add it again. Compute adjusted federal income, the Florida portion and allocated income, then deduct the available exemption and apply the ordinary rate before allowable credits. Use the return's schedules, including Florida carryover deductions, rather than assuming the federal loss deduction is the Florida amount. [F-1120N, pp. 5, 8, 11 and 15](https://floridarevenue.com/Forms_library/current/f1120n.pdf).

## Cross-border points

Where all three ordinary factors have meaningful nonzero denominators and no special method applies, the weights are property 25%, payroll 25%, sales 50%: `(property + payroll + 2 × sales) / 4`. If two denominators are zero or DOR determines them insignificant, the remaining factor is 100%; if sales is absent, property/payroll become 50% each; if property or payroll is absent, the other is 33⅓% and sales 66⅔%. [Section 220.15(1)](https://www.flsenate.gov/Laws/Statutes/2025/220.15).

Detailed property valuation/rent netting, employee-location/payroll sourcing, inventory/idle/construction property, sponsored research, tangible-sales exceptions, multistate service/SaaS/IP sourcing and nonbusiness character/allocation: **Check this point with one of our partner accountants.** Customer location alone does not supply the missing factor analysis in these examples.

Transportation activities use the revenue-mile fraction under section 220.151(2), rather than electing the ordinary formula for convenience. GulfCoast's mixed activities require the missing activity split and miles. Banks, financial organizations, insurance, telecom, citrus elections, consolidated returns and alternative-apportionment petitions: **Check this point with one of our partner accountants.** [Section 220.151](https://www.flsenate.gov/Laws/Statutes/2025/220.151).

## Net operating losses

After applying other Florida carryover deductions, for a 2025 NOL deduction apply available pre-2018 Florida NOLs first against 100% of Florida tentative apportioned adjusted federal income, then post-2017 Florida NOLs against 80% of the remainder. Pre-2018 losses carry for up to 20 taxable years; post-2017 losses carry indefinitely. Florida does not permit an NOL carryback. [F-1120N, p. 4](https://floridarevenue.com/Forms_library/current/f1120n.pdf).

Support the deduction with year-by-year Florida loss and usage schedules. Entirely Florida businesses use Schedule II line 3; businesses doing business outside Florida enter zero there and use Schedule IV line 4. [F-1120N, p. 4](https://floridarevenue.com/Forms_library/current/f1120n.pdf).

Exact loss creation, ownership-change limits and S-election/built-in-gains interaction: **Check this point with one of our partner accountants.**

## Deadlines and filing

1. **Return:** File F-1120 even if no tax is due. The ordinary due date is the later of the first day of the fifth month after year-end or the fifteenth day after the related federal return's unextended due date. For a year beginning before January 1, 2026 and ending June 30, substitute the fourth month. Calendar-year 2025 is due May 1, 2026. Weekend/holiday filing dates move to the next business day. [Section 220.222(1)](https://www.flsenate.gov/Laws/Statutes/2025/220.222); [F-1120N, p. 2](https://floridarevenue.com/Forms_library/current/f1120n.pdf).
2. **Extension:** Timely file F-7004 and pay tentative tax by the original due date. A federal extension alone is insufficient and filing time does not extend payment time. The ordinary extension is six months; the pre-2026 June 30 branch is seven months. The ordinary calendar-2025 extended filing date is November 2, 2026 because November 1 is Sunday. [F-1120N, p. 2](https://floridarevenue.com/Forms_library/current/f1120n.pdf); [section 220.222(2)](https://www.flsenate.gov/Laws/Statutes/2025/220.222).
3. **Extension validity:** Section 220.222(2)(d) treats an underpayment as material when it exceeds the greater of $2,000 or 30% of tax shown on the filed return. For this test add the specified scholarship, Strong Families, New Worlds Reading and Live Local credits back to the tax shown. A small final shortfall does not automatically void the extension; tentative underpayment can still incur penalty. [Section 220.222(2)(d)](https://www.flsenate.gov/Laws/Statutes/2025/220.222).
4. **Electronic filing/payment:** Mandatory if at least $5,000 of corporate income tax was paid in Florida's prior fiscal year (July 1–June 30), or if federal electronic filing was required. F-1120 can be filed through approved IRS MeF transmitters; DOR's online service also handles payments, F-1120ES and F-7004. Initiate electronic payments and obtain confirmation by 5 p.m. ET on the business day before the due date. [F-1120N, pp. 1–2](https://floridarevenue.com/Forms_library/current/f1120n.pdf).
5. **Short form:** F-1120A requires all of: Florida net income $45,000 or less; all business in Florida; no additions/subtractions except NOL and/or state income taxes; no inclusion in a federal or Florida consolidated return; no credits except tentative/estimated payments. Line 6 tax due must be less than $2,500. Federal NOLD is added on line 2 and Florida NOLD subtracted on line 3. Complete both sides. [F-1120A, p. 1](https://floridarevenue.com/Forms_library/current/f1120a.pdf).

## Estimated payments

Make a declaration/payment on F-1120ES when expected current-year liability exceeds $2,500; the prior-year result alone is not the trigger. The ordinary four-equal-installment calendar pattern is May 31, June 30, September 30 and December 31 of the tax year. Apply weekends/holidays; if a June payment otherwise falls on the last Saturday or Sunday of June, pay by the last Friday. Later first-liability dates have the fewer-installment branches in section 220.33. Do not annualize regular payments. [F-1120N, p. 3](https://floridarevenue.com/Forms_library/current/f1120n.pdf); [section 220.33](https://www.flsenate.gov/Laws/Statutes/2025/220.33).

Prior-year/current-year safe-harbor computations, short years and actual payment calendars: **Check this point with one of our partner accountants.**

## Penalties and interest

- Late return: 10% of unpaid tax due per month or fraction, maximum 50%. With no tax due: $50 per month or fraction, maximum $300. [DOR](https://floridarevenue.com/taxes/taxesfees/Pages/corporate.aspx).
- Negligence/intentional disregard without fraud: 10% of the deficiency. Fraud: 100% of the deficiency in place of that negligence penalty. [Section 220.803](https://www.flsenate.gov/Laws/Statutes/2025/220.803).
- Underpayment of tentative tax: 12% per year on the underpaid amount during the extension period, computed from the original due date. Underpayment of estimated tax: 12% per year; use F-2220. These penalties are separate from floating interest. [F-1120N, p. 3](https://floridarevenue.com/Forms_library/current/f1120n.pdf).
- Deficiency/late-payment interest is period-specific: 12% for January–December 2025 and 11% for January–December 2026. Split periods when the rate changes; the return's tax year does not select one rate for the entire balance. [TIP 26ADM-02, pp. 1–3](https://floridarevenue.com/taxes/tips/Documents/TIP_26ADM-02.pdf).

Standalone late-payment penalties and an actual assessment calculation: **Check this point with one of our partner accountants.**

## Credits

Do not assume a contribution cancels tax dollar for dollar. Section 220.1875 reduces the scholarship credit by the specified federal corporate-tax difference and applies it after other allowable credits. Section 220.13(1)(a)11 requires the scholarship-credit addback to income, without adding the same expense back more than once, so the base must also be recomputed. If that credit was already added in an earlier year and the same expense is deducted federally now, section 220.13(1)(a)1.b prevents a duplicate current-year addition. [Section 220.1875](https://www.flsenate.gov/Laws/Statutes/2025/220.1875); [section 220.13](https://www.flsenate.gov/Laws/Statutes/2025/220.13).

Scholarship allocation, eligible contributions, carryforward/timing, federal deductibility and final credit; capital investment; R&D; contaminated-site cleanup; hazardous-waste facilities; community contribution; New Markets; Strong Families; renewable energy; internship/experiential learning; child-care credits; and the complete credit ordering: **Check this point with one of our partner accountants.** No program eligibility is inferred from its name.

## Two worked examples that recompute

Five original cases are retained below; each calculation states its limits.

### 1. SunCode Inc.

SunCode is a Florida C-corporation developing custom software from Tampa: 10 W-2 developers and 1 owner-CEO; all work, R&D, management and support in Florida; customers in 35 states, 12% of revenue from Florida and 88% outside. For 2025, federal Form 1120 line 30 income is $480,000, including $0 federal NOLD; supplied bonus depreciation is $30,000 on servers placed in service in 2025, and supplied prior one-seventh recovery is $5,000. Property is $50,000 Florida/everywhere, payroll $1,200,000 Florida/everywhere, receipts $3,500,000 Florida/everywhere.

Conditional on the $30,000 ordinary non-QIP addback, $5,000 recovery, full exemption and all-Florida factors being valid, the current recovery is $30,000 / 7 = $4,285.714286. The base is $480,000 + $30,000 − $5,000 − $4,285.714286 − $50,000 = $450,714.285714; ordinary tax is $24,789.29, or $24,789 whole-dollar. The addition's applicability and complete return adjustments remain undetermined. [Section 220.13(1)(e)](https://www.flsenate.gov/Laws/Statutes/2025/220.13); [F-1120N, pp. 8–10](https://floridarevenue.com/Forms_library/current/f1120n.pdf).

The California relocation comparison using the 12% customer share and actual return/estimate obligations: **Check this point with one of our partner accountants.**

```oa-check
name: Conditional SunCode ordinary bonus recovery
inputs:
  federal_income: 480000
  current_addition: 30000
  prior_recovery: 5000
  exemption: 50000
steps:
  current_recovery: current_addition / 7
  adjusted_income: federal_income + current_addition - prior_recovery - current_recovery
  base: adjusted_income - exemption
  tax: base * 0.055
expected:
  current_recovery: 4285.714286
  adjusted_income: 500714.285714
  tax: 24789.285714
```

### 2. TechFlow Inc.

Delaware C-corporation, Boston headquarters; SaaS with all servers, employees and operations in Massachusetts; no Florida office, property or employees. For 2025, federal income is $2,000,000 and Florida customers generate $800,000 of $10,000,000 total revenue. Also retain the counterfactual of one Florida remote sales employee. Nexus and SaaS/IP/service classification and sourcing are not settled by these facts: **Check this point with one of our partner accountants.** No no-filing or zero-tax conclusion is supplied.

The former zero-factor computation only shows that assumed factors of zero produce zero; it does not establish the factors:

```oa-check
name: TechFlow assumed factors only; no legal zero-tax result
inputs:
  federal_income: 2000000
  property: 0
  payroll: 0
  sales: 0
steps:
  factor: (property + payroll + 2 * sales) / 4
  apportioned: federal_income * factor
expected:
  factor: 0
  apportioned: 0
```

### 3. Maria Santos / Coral Reef Consulting LLC

Florida SMLLC formed in 2023, no Form 8832 corporate election; Maria is the sole natural-person owner and reports its 2025 $145,000 net profit on Schedule C. On those stipulated classifications the LLC has no separate F-1120 and Maria has no Florida personal income tax. [DOR entity guidance](https://floridarevenue.com/taxes/taxesfees/Pages/corporate.aspx); [DOR personal-income-tax statement](https://www.floridarevenue.com/taxes/compliance/Pages/violations.aspx).

For the ordinary 2025 Schedule SE calculation, assume this is her sole SE income, no Social Security wages/tips or railroad compensation, no church earnings or optional method. Net earnings are $133,907.50; the 12.4% Social Security part plus 2.9% Medicare part gives $20,487.8475, or $20,488 whole-dollar. This is not a complete federal liability or an Additional Medicare Tax calculation. [2025 Schedule SE, lines 2–12](https://www.irs.gov/pub/irs-prior/f1040sse--2025.pdf).

The original $24,300 federal-income-tax estimate, $138.75 annual-report fee and May 1, 2026 deadline, and New York/California comparison of $8,500–$12,000 remain unverified proposed amounts, not usable rules. Adding the estimate to conditional SE tax gives $44,787.8475 arithmetically, not a verified total. Federal income tax, half-SE deduction/QBI, sales tax, annual reports, S-election planning and other-state comparisons: **Check this point with one of our partner accountants.** No all-tax-zero conclusion is supplied.

```oa-check
name: Maria conditional Schedule SE; income-tax estimate unverified
inputs:
  schedule_c_profit: 145000
  held_income_tax_estimate: 24300
steps:
  net_earnings: schedule_c_profit * 0.9235
  social_security: net_earnings * 0.124
  medicare: net_earnings * 0.029
  se_tax: social_security + medicare
  unverified_combined_estimate: held_income_tax_estimate + se_tax
expected:
  net_earnings: 133907.50
  social_security: 16604.53
  medicare: 3883.3175
  se_tax: 20487.8475
  unverified_combined_estimate: 44787.8475
```

### 4. Atlantic Manufacturing Inc.

Florida C-corporation with projected 2025 Florida tax of $40,000 and a proposed $40,000 contribution to Step Up For Students. The simple subtraction is zero, but establishes neither the allowable credit nor final tax after the federal-benefit reduction and state addback. Actual approval, contribution timing, eligibility, federal deduction and resulting balance: **Check this point with one of our partner accountants.** [Section 220.1875](https://www.flsenate.gov/Laws/Statutes/2025/220.1875); [section 220.13(1)(a)11](https://www.flsenate.gov/Laws/Statutes/2025/220.13).

```oa-check
name: Atlantic arithmetic only; credit and balance undetermined
inputs:
  projected_tax: 40000
  gross_contribution: 40000
steps:
  original_gross_subtraction: projected_tax - gross_contribution
expected:
  original_gross_subtraction: 0
```

### 5. GulfCoast Logistics Inc.

Florida C-corporation with trucking/warehousing in Florida, Georgia and Alabama. For 2025: federal income $1,200,000; property FL $2,000,000, GA $500,000, AL $300,000 (total $2,800,000); payroll FL $4,000,000, GA $800,000, AL $600,000 (total $5,400,000); services originating FL $6,000,000, GA $1,500,000, AL $700,000 (total $8,200,000).

The following is arithmetic conditional on ordinary factors using those numerators, not GulfCoast's filing method. Round each ratio and then each weighted factor to six decimals: property weight 0.178572, payroll 0.185185, sales 0.365854; sum 0.729611. Apportioned income is $875,533.20; less a stipulated full $50,000 exemption gives $825,533.20; at 5.5%, $45,404.326, or $45,404 whole-dollar. [F-1120N, p. 10](https://floridarevenue.com/Forms_library/current/f1120n.pdf).

Transportation activity requires revenue miles; the activity split/miles and actual service sourcing are missing. Florida/Georgia/Alabama filing results and total tax: **Check this point with one of our partner accountants.** [Section 220.151(2)](https://www.flsenate.gov/Laws/Statutes/2025/220.151).

```oa-check
name: GulfCoast conditional ordinary factors; transportation method unresolved
inputs:
  income: 1200000
  property_fl: 2000000
  property_all: 2800000
  payroll_fl: 4000000
  payroll_all: 5400000
  sales_fl: 6000000
  sales_all: 8200000
  exemption: 50000
steps:
  property_ratio: round(property_fl / property_all, 6)
  payroll_ratio: round(payroll_fl / payroll_all, 6)
  sales_ratio: round(sales_fl / sales_all, 6)
  property_weight: round(property_ratio * 0.25, 6)
  payroll_weight: round(payroll_ratio * 0.25, 6)
  sales_weight: round(sales_ratio * 0.5, 6)
  factor: property_weight + payroll_weight + sales_weight
  apportioned: income * factor
  base: apportioned - exemption
  tax: base * 0.055
expected:
  property_weight: 0.178572
  payroll_weight: 0.185185
  sales_weight: 0.365854
  factor: 0.729611
  apportioned: 875533.20
  tax: 45404.326
```

## Other taxes and fees

Sales/use, reemployment, insurance premiums, documentary stamps on deeds/notes/mortgages and DR-225, annual reports, minimum/net-worth/capital-stock/gross-receipts taxes and local fees are not cleared by the income-tax calculation. **Check this point with one of our partner accountants.**

## Ask the client first

Use the required inputs above. Resolve corporate ownership, year boundaries, exemption sharing, depreciation/conformity, loss history, activity sourcing and payment evidence before selecting a return or final amount. Refer unresolved matters using the instructions above.

Circular 230 §10.37: this Guide is general information; a filing position requires the taxpayer's actual facts, applicable law and professional judgment.

## Sources

Completed bounded reads from November 22 and 25, 2026 are reused where their propositions and tax-year applicability are unchanged. Exact sentences missing from the old record were recovered from the operative passages on November 26. This is not a claim of a fresh full-document review or renewed accountant approval.

| Official authority | Scope read / reused | Read date |
| --- | --- | --- |
| [DOR corporate tax](https://floridarevenue.com/taxes/taxesfees/Pages/corporate.aspx) | Read entity/owner gateways, dated rate table, late-return penalties; unchanged earlier scope reused | 2026-11-22; wording recovered 2026-11-26 |
| [DOR personal-income-tax statement](https://www.floridarevenue.com/taxes/compliance/Pages/violations.aspx) | Read explicit statement that Florida has no personal income tax | 2026-11-26 |
| [Section 220.14](https://www.flsenate.gov/Laws/Statutes/2025/220.14) | Read all four exemption subsections and controlled-group allocation | 2026-11-22; wording recovered 2026-11-26 |
| [2025 F-1120N R.01/26](https://floridarevenue.com/Forms_library/current/f1120n.pdf) | Read bounded entity, filing, estimates, penalties, NOL, return lines, bonus recovery, factor-rounding and transportation passages; not all pages/programs | 2026-11-22; follow-up 2026-11-25; wording recovered 2026-11-26 |
| [Section 220.13](https://www.flsenate.gov/Laws/Statutes/2025/220.13) | Read ordinary bonus/QIP distinction and scholarship-credit addition | 2026-11-22; wording recovered 2026-11-26 |
| [Section 220.15](https://www.flsenate.gov/Laws/Statutes/2025/220.15) | Read ordinary weights/reweighting; complete special sourcing is referred | 2026-11-22; wording recovered 2026-11-26 |
| [Section 220.151](https://www.flsenate.gov/Laws/Statutes/2025/220.151) | Read transportation subsection (2); no taxpayer miles established | 2026-11-22; wording recovered 2026-11-26 |
| [Section 220.222](https://www.flsenate.gov/Laws/Statutes/2025/220.222) | Read filing/June-year-end branches, extensions and material-underpayment/credit test | 2026-11-22; wording recovered 2026-11-26 |
| [Section 220.33](https://www.flsenate.gov/Laws/Statutes/2025/220.33) | Read ordinary/later-liability installments and June-weekend acceleration | 2026-11-22; wording recovered 2026-11-26 |
| [Section 220.803](https://www.flsenate.gov/Laws/Statutes/2025/220.803) | Read negligence, fraud and definition of deficiency | 2026-11-22; wording recovered 2026-11-26 |
| [TIP 26ADM-02](https://floridarevenue.com/taxes/tips/Documents/TIP_26ADM-02.pdf) | Read deficiency/late-payment rates and cross-period method, pp. 1–3 | 2026-11-25; wording recovered 2026-11-26 |
| [F-1120A](https://floridarevenue.com/Forms_library/current/f1120a.pdf) | Read page 1 eligibility, tax-due restriction and back-of-form instruction | 2026-11-22; follow-up 2026-11-25; wording recovered 2026-11-26 |
| [Section 220.1875](https://www.flsenate.gov/Laws/Statutes/2025/220.1875) | Read federal-benefit reduction/ordering; full credit computation referred | 2026-11-22; wording recovered 2026-11-26 |
| [2025 Schedule SE](https://www.irs.gov/pub/irs-prior/f1040sse--2025.pdf) | Read page 1 ordinary net-earnings/wage-base/rate computation for Maria only | 2026-11-22; wording recovered 2026-11-26 |

Not yet confirmed: the explicitly referred questions and case-specific eligibility/adjustments; the proposed annual-report/other-state amounts in Maria's facts are not usable law. No all-tax clearance, actual return, payment, professional approval or 2026 taxable-year computation is established.
