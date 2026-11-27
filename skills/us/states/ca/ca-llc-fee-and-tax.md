---
name: ca-llc-fee-and-tax
description: Compute a California partnership-classified or disregarded LLC's 2026 annual tax and total-income fee, with statutory exceptions. Covers FTB 3522 and 3536, Form 568 deadlines by owner, the four fee bands, estimated-fee penalty and prior-year protection, doing-business tests, short years and cancellation. Preserves separately dated 2025 cases and the enacted 2027-2029 first-year rule. Trigger on "California LLC fee", "$800 annual tax", "FTB 3522", "FTB 3536", "Form 568 fee". There are explicit holds for unresolved cases.
version: "2.1"
jurisdiction: US-CA
tax_year: 2026
last_updated: 2026-11-27
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
---

# California LLC annual tax and LLC fee: Form 3522, Form 3536 and Form 568 (tax year 2026)

For a non-exempt LLC within this Guide, the 2026 charge is the **$800 annual tax plus any LLC fee** in the table below; apply the exceptions before computing it. Sources were read on 27 November 2026. [R&TC §§17941](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17941.), [17942](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17942.).

## Scope and who this is for

This Guide computes the annual tax and LLC fee for **partnership-classified and disregarded LLCs**, including SMLLCs, organized, registered or doing business in California. An LLC taxable as a corporation follows the corporation return and tax rules instead. Entities exempt under §23701h or §23701x are excluded from the §17941 definition. [R&TC §17941(a), (b), (d)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17941.); [§18633.5(h), (i)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=18633.5.).

Formation and the Statement of Information use `ca-formation`; SMLLC return preparation uses `ca-smllc-form-568`; member tax, withholding and the separate election use `ca-pte-elective-tax` and the member's return Guide. This Guide does not determine those liabilities.


## Ask the client first

- Is the LLC organized in California, registered with the Secretary of State (SOS) as a foreign LLC, or neither? Get the exact SOS filing or registration date.
- How is it classified (disregarded, partnership, or corporation)? For a disregarded LLC, who is the owner (individual, C corporation, S corporation, partnership) and what is the owner's tax year?
- Which taxable year is in question: 2025 or 2026, calendar or fiscal?
- If it is neither organized nor registered in California: what are its California sales, property and payroll, and total sales, property and payroll? Does it actively engage in any transaction in California? Does it hold interests in partnerships or S corporations with California activity?
- What was its total income, including cost of goods sold, and how much of that is assigned to California customers?
- What LLC fee was owed for the **preceding** taxable year, and what was paid on forms 3522 and 3536, and on which dates?
- Has it stopped doing business? Has it filed a final Form 568, or a certificate of cancellation (or dissolution) with the SOS, and on which dates?
- Is it a series LLC, or one of several LLCs with the same owners?
- Is the sole owner a member of the US Armed Forces who has been deployed?

## The method, step by step

1. **Classify.** Confirm the LLC is disregarded or a partnership. If it is taxed as a corporation, stop here and use the corporation rules.
2. **Test who owes.** Apply the three triggers below: organized in California, registered with the SOS, or doing business in California under §23101. Any one is enough.
3. **Check the exceptions.** Look at the 15-day short year (§17946), the first-year rules (§17941(g)), the deployed-military exemption (§17941(f)), and short-form cancellation.
4. **Annual tax.** Fix the amount ($800, or $400 for a qualifying first year from 2027) and the due date: the 15th day of the 4th month of the taxable year. Pay with form 3522 ([R&TC §17941](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17941.)).
5. **LLC fee.** Build California total income as gross income plus cost of goods sold, assigned to California under the sales rules, excluding amounts from lower-tier LLCs already subject to the fee. Read the fee from the table.
6. **Estimate.** Pay the estimated fee with form 3536 by the 15th day of the 6th month. Compare the payment with the prior-year fee to test the 10% penalty ([R&TC §17942(d)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17942.)).
7. **Return.** File Form 568 by the due date for the LLC's classification and owner. Pay any fee balance by the **original** due date. An extension extends only the time to file.
8. **Stopping.** If the business has ended, file the final Form 568 and the SOS cancellation within the time limits below.

### Who owes the tax and fee ([R&TC §17941](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17941.))

An LLC owes the annual tax for a taxable year if **any** of these is true:

- **Organized in California.** The SOS has accepted its articles of organization (§17941(b)(1)).
- **Registered in California.** The SOS has issued it a certificate of registration as a foreign LLC (§17941(b)(1)). Registration alone is enough, even with no California business.
- **Doing business in California**, as defined in §23101 (§17941(a)). This applies even if the LLC never registered.

An organized or registered LLC owes the tax "for each taxable year, or part thereof, until a certificate of cancellation of registration or of articles of organization is filed" with the SOS (§17941(b)(1)). It is owed whether or not the LLC is active or profitable. Every LLC that owes the annual tax also owes the LLC fee if its California total income reaches the first band (§17942(a)).

A foreign LLC that is **not** registered and **not** doing business in California, but has California-source income, files Form 565 (if it is a partnership) instead of Form 568, and does not owe these charges. A single-member, nonregistered, disregarded foreign LLC in that position need not file Form 565 or Form 568 ([FTB LLC page](https://www.ftb.ca.gov/file/business/types/limited-liability-company/index.html); [2025 Form 568 booklet](https://www.ftb.ca.gov/forms/2025/2025-568-booklet.html)).

#### Doing business: the §23101 tests ([R&TC §23101](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=23101.))

An LLC is doing business in California for a taxable year if **any** one of these is met:

- **(a) Active conduct.** It actively engages in a transaction in California for financial or pecuniary gain or profit.
- **(b)(1) Organized or commercially domiciled** in California.
- **(b)(2) Sales.** California sales **exceed** the lesser of the indexed sales amount or **25%** of total sales. Sales by an agent or independent contractor count. Sales are assigned under §25135 and §25136, so services go to where the customer receives the benefit.
- **(b)(3) Property.** California real and tangible personal property **exceeds** the lesser of the indexed property amount or **25%** of total property.
- **(b)(4) Payroll.** California compensation **exceeds** the lesser of the indexed payroll amount or **25%** of total compensation.
- **Pass-through shares count.** The LLC's pro rata or distributive share of the sales, property and payroll of partnerships and S corporations is included (§23101(d)).

"Exceed" means more than. An amount exactly equal to the lesser figure does not meet that test.

**Indexed amounts, by year** ([FTB: Doing business in California](https://www.ftb.ca.gov/file/business/doing-business-in-california.html)). The FTB revises the statutory dollar amounts annually under §23101(c); use the amount for the taxable year, and the **lesser** of that amount and the applicable **25%** figure. Exact equality does not satisfy an “exceeds” test.

| Year | Sales exceed | Property exceeds | Payroll exceeds |
|---|---|---|---|
| 2025 | $757,070 | $75,707 | $75,707; [FTB table](https://www.ftb.ca.gov/file/business/doing-business-in-california.html) |
| 2026 | Not published on the FTB page when read on 27 November 2026; no usable dollar amount | Not yet published | Not yet published |

**2026 dollar-threshold hold:** no 2026 row was on the cited FTB page when read. Do not use 2025 amounts as 2026 amounts or issue a nexus conclusion that depends on an unpublished 2026 amount. Check this point with one of our partner accountants.

Public Law 86-272 protection concerns taxes based on **net income**; do not assume it eliminates the LLC annual tax or fee. A disputed immunity or passive-interest nexus position is held for referral below. [FTB doing-business page](https://www.ftb.ca.gov/file/business/doing-business-in-california.html).

### Thresholds and figures, tax year 2026

#### Annual LLC tax ([R&TC §17941](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17941.))

- **Amount.** The tax equals the minimum franchise tax in §23153(d), which is **$800** ([R&TC §23153](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=23153.)). There is no proration for a short year. It is owed in full even when the LLC fee is nil. The two charges are added together.
- **Due date.** On or before the 15th day of the 4th month of the taxable year (§17941(c)). For a calendar-year LLC in its second and later years, that is 15 April. For 2026, form FTB 3522 is the voucher for the $800 annual tax for taxable year 2026 ([2026 FTB 3522 instructions](https://www.ftb.ca.gov/forms/2026/2026-3522.pdf)).
- **First year.** The FTB counts from the SOS filing date: "You have until the 15th day of the 4th month from the date you file with the SOS to pay your first-year annual tax." Its example: an LLC registered on 18 June 2020 has its first tax due on 15 September 2020 ([FTB LLC page](https://www.ftb.ca.gov/file/business/types/limited-liability-company/index.html)). So the month of filing counts as month 1.
- **Disregarded LLC.** Its taxable year is the owner's taxable year ([R&TC §18633.5](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=18633.5.)).
- **Foreign LLC that starts later.** If the 15th day of the 4th month of an existing foreign LLC's year has already passed when it starts business in California or registers, pay the annual tax immediately (2026 FTB 3522 instructions).

#### First-year rules ([R&TC §17941(g)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17941.))

| Applicable first-year condition (see the foreign LLC hold below) | First-year annual tax | Source |
|---|---|---|
| Organizes or registers with SOS on or after 1 January 2021 and before 1 January 2024; statutory budget condition met | First-year annual-tax exemption under §17941(g)(1); historical relief only | [§17941(g)(1)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17941.) |
| First year begins in 2024, 2025 or 2026 | $800 ordinary annual tax; other statutory exceptions below still apply | [§17941](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17941.) |
| First taxable year **beginning** on or after 1 January 2027 and before 1 January 2030 | **$400** instead of $800, first taxable year only, for an LLC required to file under §18633.5 | [§17941(g)(2)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17941.) |

The enacted first-year reduction does not change the separate fee. A domestic LLC filing articles on 16 December 2026 begins its first taxable year in 2026; 2027 is its second year. The §17941(g)(2) first-year reduction does not apply to that second year. [§17941(g)(2)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17941.).

**Foreign-LLC future-relief hold:** the 2026 voucher says a foreign LLC's first taxable year begins when organized in its home state. Preserve the original example of a Delaware LLC organized in **2022** and registering in California in **2027**, but do not issue a payment instruction for its 2027 first-year reduction from 2026 instructions alone. Check this point with one of our partner accountants. [2026 FTB 3522](https://www.ftb.ca.gov/forms/2026/2026-3522.pdf).

## Rates, bands and thresholds

| California total income for the taxable year | Fee and source |
|---|---|
| Less than $250,000 | No fee [R&TC §17942(a)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17942.) |
| $250,000 or more, but less than $500,000 | $900 [R&TC §17942(a)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17942.) |
| $500,000 or more, but less than $1,000,000 | $2,500 [R&TC §17942(a)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17942.) |
| $1,000,000 or more, but less than $5,000,000 | $6,000 [R&TC §17942(a)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17942.) |
| $5,000,000 or more | $11,790 [R&TC §17942(a)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17942.) |

- **Flat amounts.** Each band is a fixed amount, not a percentage. Income of exactly $250,000 is in the $900 band. Income of exactly $500,000 is in the $2,500 band. The FTB applies the table to California total income "rounded to the nearest whole dollar" ([FTB LLC page](https://www.ftb.ca.gov/file/business/types/limited-liability-company/index.html)).
- **The base.** "Total income from all sources derived from or attributable to this state" means gross income, as defined in R&TC §24271, **plus** cost of goods sold paid or incurred in the trade or business (§17942(b)(1)(A)). Cost of goods sold is not subtracted, and neither are operating expenses. For a reseller, the base is therefore close to gross sales, not gross profit.
- **Lower-tier LLCs.** The base excludes allocations, attributions of income or gain, and distributions the LLC receives as a member of, or holder of an economic interest in, another LLC, **if** they are attributable to income already subject to the LLC fee (§17942(b)(1)(A)).
- **Assigning to California.** Use the sales-assignment rules of §25135 and §25136 (including their exceptions), as modified by regulations under §25137, "other than those provisions that exclude receipts from the sales factor" (§17942(b)(1)(B)). For ordinary tangible-goods sales, delivery to a California purchaser other than the US government is assigned here; §25135 also has a shipment-from-California rule. Services follow where the purchaser receives the benefit; intangibles follow use, with a customer-location rule for marketable securities. [§25135](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=25135.); [§25136](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=25136.). Schedule IW computes the figure ([2025 Form 568 booklet](https://www.ftb.ca.gov/forms/2025/2025-568-booklet.html)).
- **Common control.** Do not compute each LLC in isolation where §17942(b)(2) aggregation could apply (same persons owning directly or indirectly more than 50% of capital or profits interests and formation primarily to reduce the fee). The provision permits one group determination and joint and several liability. Check this point with one of our partner accountants.
- **Due.** The fee is due on the date the return is required to be filed under §18633.5, which is the **original** due date (§17942(c)). An extension does not move it.

#### Estimated fee and the 10% penalty ([R&TC §17942(d)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17942.))

- **Estimate.** Estimate and pay the fee by the 15th day of the 6th month of the current taxable year (§17942(d)(1)). For a calendar-year LLC that is 15 June 2026. Use form FTB 3536. If no fee is owed, do not file form 3536 ([2026 FTB 3536 instructions](https://www.ftb.ca.gov/forms/2026/2026-3536.pdf)).
- **Short first year.** If the taxable year ends before the 15th day of its 6th month, no estimated payment is due. The fee is then due with the return (2026 FTB 3536 instructions).
- **Penalty.** A penalty of **10%** of the underpayment is added to the fee. The underpayment is the fee for the year minus the amount paid by the 15th day of the 6th month (§17942(d)(2)).
- **Safe harbor.** There is no penalty if the amount paid by that date is **equal to or greater than** the LLC's total fee for the **preceding** taxable year (§17942(d)(2)). A new LLC has no preceding year, so it has no safe harbor and must estimate.
- **Balance.** Any fee not paid as an estimate is still due by the original return due date, with form 3536, or form 3537 if filing on extension ([2025 Form 568 booklet](https://www.ftb.ca.gov/forms/2025/2025-568-booklet.html)).

#### Other penalties ([2025 Form 568 booklet](https://www.ftb.ca.gov/forms/2025/2025-568-booklet.html))

- **Late payment** ([§19132](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=19132.)). Unless reasonable cause and no willful neglect are shown, this is 5% of total tax unpaid plus 0.5% per month or fraction on the remaining unpaid balance for up to 40 months, capped at 25% of total tax unpaid. For the annual tax it runs from the 15th day of the 4th month. For the unpaid fee it runs from the original return due date.
- **Late filing** ([§19131](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=19131.)). For an ordinary, nonfraudulent failure, unless reasonable cause and no willful neglect are shown, this is 5% of the unpaid tax, which includes the LLC fee, for each month or part of a month, up to 25%. If the return is filed after the extended date, the penalty runs from the original due date. The late-payment amount is reduced by the late-filing and demand penalties under §19132(b); do not simply add both full amounts. Fraud and penalty-relief claims are held below.
- **Per-member penalty** (§19172). This applies to an LLC classified as a partnership that files late or files an incomplete return: **$18** times all persons who were members at any time in the taxable year, for each month or part of a month, up to 12 months. It is charged on top of the other penalties, unless the failure is due to reasonable cause ([R&TC §19172](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=19172.)).
- **Unregistered foreign LLC or suspended domestic LLC** (§19135). **$2,000** per taxable year is charged when a foreign LLC that has not registered (or whose powers, rights and privileges are forfeited), or a domestic LLC that has been suspended, is doing business in California and fails to file a return within 60 days after the FTB sends a notice and demand, unless the failure is due to reasonable cause and not willful neglect ([R&TC §19135](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=19135.)). It is charged in addition to other penalties.
- Interest on unpaid tax runs from the original payment due date; filing extensions do not stop it. No historical rate is usable here. For a dated interest or abatement computation: Check this point with one of our partner accountants.

## Boundary and exception table

| Situation | Rule | Result |
|---|---|---|
| Taxable year of **15 days or less** and **no business** in California in that period | §17946 | Not subject to the annual tax or fee for that year, and no Form 568 is required for it. For a calendar-year LLC, that means filing with the SOS on 17 December or later. |
| Filed with the SOS on 16 December (a 16-day year) | §17946 not met | $800 for that year, due by the 15th day of the 4th month counting from December (15 March, subject to weekend/holiday adjustment) |
| Any business done in the short year | §17946 not met | No §17946 exemption; test the other statutory exceptions before charging the ordinary full tax |
| Domestic short-form cancellation (LLC-4/8) | §17941(e); Corporations Code §17707.02 | Non-usable eligibility hold: do not rely on the former “majority”/“no debts other than tax” checklist alone. Check this point with one of our partner accountants. |
| Deployed sole-owner small business | [§17941(f)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17941.) | For years beginning 2020 through 2029: sole owner must be deployed in the statutory sense, California total income no more than $250,000, and the LLC operates at a loss (expenses exceed receipts) or ceases operation during deployment year. No annual tax. “Deployed” means active duty/service during a Presidential Executive order specifying combat or homeland defense; training/processing-only duty and permanent changes of station are excluded. The 2025 booklet directs zero on lines 2 and 3 for the exemption; do not carry those line numbers to an unread 2026 form. |
| Series LLC | Non-usable series-classification hold | Separate-series treatment depends on the governing arrangements. Check this point with one of our partner accountants. |
| LLC taxed as a corporation | §17941(d); §18633.5(h) | Not within §17941 or §17942. Files as a corporation |
| California sales exactly equal to the lesser §23101 amount | "exceed" | Sales test not met. Check the other tests |

**Short-year/future-relief hold:** for an exempt year immediately before 2027, no conclusion here authorizes either $400 or $800 as the following year's payment. Do not use the former “pay $800 and reclaim later” suggestion. Check this point with one of our partner accountants.

## Worked cases

### Case A: consulting SMLLC, ordinary (2026) ([R&TC §17942](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17942.))

- **Facts.** A California disregarded LLC, formed in 2024, owned by an individual with a calendar year. In 2026 it earns $310,000 of consulting fees, all from California clients. It has no cost of goods sold. Its 2025 California total income was below $250,000, so its 2025 fee was nil.
- **Annual tax.** $800, due 15 April 2026 with form 3522.
- **Fee.** Assuming the services benefited the purchasers in California (client address alone does not establish assignment), California total income is $310,000, which falls in the $250,000 to $500,000 band, so the fee is $900.
- **Estimate.** The prior-year fee was nil, so any payment by 15 June 2026, including none, avoids the 10% penalty. The $900 is still due by 15 April 2027, the original due date of the return.
- **Total entity-level charge for 2026:** $800 + $900 = $1,700.

```oa-check
name: CA LLC 2026, consulting SMLLC, annual tax plus fee
inputs:
  annual_tax: 800
  ca_total_income: 310000
  fee_band_900: 900
steps:
  - total_charge: annual_tax + fee_band_900
  - headroom_to_next_band: 500000 - ca_total_income
expected:
  total_charge: 1700
  headroom_to_next_band: 190000
```

### Case B: reseller, cost of goods sold added back (boundary) ([R&TC §17942](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17942.))

- **Facts.** An LLC classified as a partnership sells goods delivered only to California buyers. 2026 gross sales are $1,200,000 and cost of goods sold is $900,000, so gross income is $300,000.
- **Base.** Gross income $300,000 plus cost of goods sold $900,000 gives $1,200,000.
- **Fee.** $1,200,000 is in the $1,000,000 to $5,000,000 band, so the fee is $6,000, not the $900 that gross profit alone would suggest.

```oa-check
name: CA LLC 2026, reseller, cost of goods sold added back to the fee base
inputs:
  gross_sales: 1200000
  cogs: 900000
steps:
  - gross_income: gross_sales - cogs
  - fee_base: gross_income + cogs
  - over_1m_band: fee_base - 1000000
expected:
  gross_income: 300000
  fee_base: 1200000
  over_1m_band: 200000
```

### Case C: underpaid estimate (penalty) ([R&TC §17942(d)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17942.))

- **Facts.** The 2025 fee was $2,500. The 2026 fee turns out to be $6,000. By 15 June 2026 the LLC paid $1,000 on form 3536.
- **Test.** $1,000 is less than the $2,500 prior-year fee, so the safe harbor fails.
- **Penalty.** The underpayment is $6,000 minus $1,000 = $5,000. The penalty is 10% x $5,000 = $500.
- **Had it paid $2,500 by 15 June,** there would be no penalty. The $3,500 balance would then be due by the original due date of the return.

**The decision.** Paying the USD 2,500 prior-year fee by 15 June, instead of USD 1,000, costs USD 1,500 more cash in June and saves the USD 500 penalty. Recommend paying at least the prior-year fee whenever the current-year fee is uncertain.

```oa-check
name: CA LLC 2026, estimate decision, pay USD 1,000 or the USD 2,500 safe harbor
inputs:
  fee_2026: 6000
  fee_2025: 2500
  paid_low: 1000
steps:
  - penalty_low: (fee_2026 - paid_low) * 0.10
  - penalty_safe_harbor: 0
  - extra_cash_in_june: fee_2025 - paid_low
  - saving: penalty_low - penalty_safe_harbor
expected:
  penalty_low: 500
  extra_cash_in_june: 1500
  saving: 500
```

### Case D: year-end formation, 2026 into 2027 (boundary) ([R&TC §17941](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17941.))

- **16 December 2026.** Articles filed on 16 December 2026 give a 16-day 2026 year. §17946 does not apply, so $800 is due for 2026 by 15 March 2027. 2027 is the second taxable year, so another $800 is due by 15 April 2027. The $400 rate is not available.
- **4 January 2027.** Articles filed on 4 January 2027 give a first taxable year beginning in 2027. The first-year tax is $400 under §17941(g)(2), due by 15 April 2027 (4th month, counting January). 2028 is $800.
- **17 December 2026, no business until January.** The 2026 year is exempt under §17946. The following-year $400/$800 outcome is non-usable pending the future-relief hold above. Check this point with one of our partner accountants.

### Case E: out-of-state LLC under the sales test (exclusion) ([R&TC §23101](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=23101.))

- **Facts.** A Nevada LLC, not registered in California, with no California property or payroll and no other California activity. 2025 total sales are $3,000,000, of which $600,000 is assigned to California customers.
- **Sales test for 2025.** 25% of total sales is $750,000. That is less than the 2025 indexed amount of $757,070, so the lesser figure is $750,000. $600,000 does not exceed it.
- **Result.** It is not doing business under §23101(b) on these facts, and it owes no annual tax or fee for 2025. If it registers with the SOS, it owes the $800 from then on, whatever its sales.

## Historical cases: original inputs retained

These are separately dated **2025** cases, not replacements for Cases A–E above. Tax results use the cited charge, assignment and due-date rules; member and federal conclusions remain held.

- **Historical A, Bay Code Studio:** individual-owned SMLLC formed **5 January 2024**; **2025** California consulting receipts **$310,000**, expenses **$40,000**, arithmetic remainder **$270,000**, no COGS; **2024** receipts **$230,000** and fee **$0**. Assuming service benefit was received in California, annual tax **$800**, fee **$900**, total **$1,700**; zero prior-year fee avoids the estimate penalty even with zero timely estimate. Fee balance and individual-owned SMLLC return due **15 April 2026**, not March. Federal profit, deductibility, SALT and Form 540 conclusions are non-usable here. Check this point with one of our partner accountants. [§17942](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17942.); [§18633.5(i)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=18633.5.).
- **Historical B, Salish Robotics:** Delaware LLC registered in California; three members, California resident **40%**, Oregon resident **30%**, Washington corporation **30%**. **2025** services receipts **$1,400,000**: California **$800,000**, Oregon **$400,000**, Washington **$200,000**; COGS input **$300,000**. Preserve that COGS input: gross income **$1,100,000** plus COGS **$300,000** reconstructs **$1,400,000**, not **$1,700,000**. Assuming the stated California receipts represent benefit received here, assigned fee-base income is **$800,000**, fee **$2,500**, annual tax **$800**, total **$3,300**. Prior **2024** fee **$2,500**, paid **15 June 2025**, protects from the estimate penalty (deadline **16 June**). Form 568 and any fee balance due **16 March 2026**. No member's residency alone is substituted for LLC nexus. Member withholding, Schedule T and corporate-member returns remain held. Check this point with one of our partner accountants. [§17942](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17942.); [§25136](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=25136.); [2025 FTB 3536](https://www.ftb.ca.gov/forms/2025/2025-3536.pdf).
- **Historical C, Aspen Analytics:** Colorado LLC, no California registration, office or employees, all members Colorado residents; **2025** SaaS sales **$4,200,000**, with benefit received in California on **$1,100,000**. The lesser sales threshold is **$757,070** (25% of total is **$1,050,000**), so nexus is met. On those stated assignment facts, fee **$6,000** plus annual tax **$800** = **$6,800**. The **$2,000** penalty is not automatic: §19135's entity, business and notice/60-day tests must all be met. Back returns, registration, voluntary disclosure and abatement outcomes are held. Check this point with one of our partner accountants. [§23101](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=23101.); [§17942](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17942.); [§19135](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=19135.).
- **Historical D, Pacific Yields:** articles **22 December 2025**, no business, receipts or expenses through **31 December 2025**; bank account opened **4 January 2026**. The **10-day** 2025 year with no business meets §17946: no 2025 annual tax, fee or Form 568. This does not erase the existence of that taxable year. Ordinary **2026** annual tax is **$800**, due **15 April 2026**. The 2026 return date depends on classification/owner; apply the filing table, not the old unconditional March date. [§17946](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17946.); [2025 booklet, D](https://www.ftb.ca.gov/forms/2025/2025-568-booklet.html); [2026 FTB 3522](https://www.ftb.ca.gov/forms/2026/2026-3522.pdf).
- **Historical E, Saguaro Software:** formed **2022**, Form 2553 effective **1 January 2025**, **2025** receipts **$1,200,000**, owner salary **$90,000**, stated pass-through income **$400,000**. If corporation classification is effective, this LLC-fee computation is excluded. The old **$490,000** base, **1.5%**, **$6,000** corporate tax, **$6,800** comparison and **$800** annual savings are **non-usable**, as is its reasonable-salary conclusion. Do not treat the historical **17 March 2025** pre-election filing date as established for an owner/classification not supplied. Check this point with one of our partner accountants. [§17941(d)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17941.); [§18633.5(h)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=18633.5.).

**Other original illustrations:** the **2024 $2,500** prior fee / **2025 $1,300,000** fee-base case gives a **$6,000** fee, **$3,500** balance after **$2,500** paid by **16 June 2025**, or **$600** estimate penalty after a zero timely payment. The original **10-member, 12-month** partnership failure gives **$18 × 10 × 12 = $2,160** absent reasonable cause. [§17942(d)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17942.); [§19172](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=19172.).

For the original formation illustrations: **5 June 2025** means first payment **15 September 2025**, not October; **18 June 2020** means **15 September 2020**. **18 December 2025** gives **14 days**; **17 June–30 June** gives **14 days** in the stated fiscal illustration. The no-business condition is required for either short-year exemption; no following-year amount is inferred for an unspecified fiscal year. **16 December 2025** gives **16 days**, ordinary **$800** tax due **16 March 2026** after the Sunday adjustment, not April. An LLC formed **2019**, inactive since **2022**, remains subject to the ordinary annual charge until qualifying termination; inactivity alone does not stop it. [FTB first-year example](https://www.ftb.ca.gov/file/business/types/limited-liability-company/index.html); [2025 FTB 3522](https://www.ftb.ca.gov/forms/2025/2025-3522.pdf); [§17946](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17946.); [§17941(b)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17941.).

```oa-check
name: Historical inputs, five-case charge arithmetic and other original illustrations
inputs:
  consulting_receipts_2025: 310000
  consulting_expenses: 40000
  reseller_receipts: 1400000
  reseller_cogs: 300000
  ca_services: 800000
  all_saas: 4200000
  ca_saas: 1100000
  indexed_sales_2025: 757070
  fee_2024: 2500
  fee_2025: 6000
  members: 10
  months_late: 12
steps:
  - arithmetic_remainder_not_federal_tax_profit: consulting_receipts_2025 - consulting_expenses
  - hist_a_total: 800 + 900
  - hist_b_gross_income: reseller_receipts - reseller_cogs
  - hist_b_fee_base_before_assignment: hist_b_gross_income + reseller_cogs
  - hist_b_total: 800 + 2500
  - hist_c_sales_threshold: min(indexed_sales_2025, all_saas * 0.25)
  - hist_c_excess: ca_saas - hist_c_sales_threshold
  - hist_c_total: 800 + 6000
  - safe_balance: fee_2025 - fee_2024
  - zero_estimate_penalty: fee_2025 * 0.10
  - per_member_penalty: 18 * members * months_late
expected:
  arithmetic_remainder_not_federal_tax_profit: 270000
  hist_a_total: 1700
  hist_b_gross_income: 1100000
  hist_b_fee_base_before_assignment: 1400000
  hist_b_total: 3300
  hist_c_sales_threshold: 757070
  hist_c_excess: 342930
  hist_c_total: 6800
  safe_balance: 3500
  zero_estimate_penalty: 600
  per_member_penalty: 2160
```

## When to refuse or refer

For each of these, issue no numeric conclusion on the held point: **Check this point with one of our partner accountants.**

- Disputed nexus or immunity, passive or investment-partnership interests, Swart-type interests, agent/staff activity and Public Law 86-272 positions.
- Back years, voluntary disclosure, revivor, fraud, first-time or reasonable-cause abatement, a dated interest computation, or disaster postponements.
- Series LLCs; commonly controlled or unitary groups; conversion, merger, dissolution complexities; short-form cancellation eligibility; the future-relief holds above; LLPs and LPs.
- Member returns, consent/nonconsent liability, Form 592/592-B withholding, K-1 allocations, PTE election and credits, federal/California deductibility or SALT limits, corporate elections/revocations and corporate/S-corporation liability or savings.
- The older cannabis, real-property reassessment, “small business deduction” and income-component exclusions (municipal-bond interest, deferred exchanges, capital/§1231 gains, guaranteed payments, interest, dividends, royalties and rents) are non-usable holds; do not infer a tax result from these names.

## Filing and payment

Return-date law: [R&TC §18633.5(a), (i)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=18633.5.). Procedures: [2025 Form 568 booklet, E](https://www.ftb.ca.gov/forms/2025/2025-568-booklet.html). The 2025 layout below is historical; it does not establish 2026 form content.

| Step | Form | Due |
|---|---|---|
| Annual tax | FTB 3522 | 15th day of the 4th month of the taxable year (15 April 2026 for calendar 2026). First year: 15th day of the 4th month counting from the SOS filing date [Source](https://www.ftb.ca.gov/forms/2026/2026-3522.pdf) |
| Estimated LLC fee | FTB 3536 | 15th day of the 6th month of the taxable year (15 June 2026 for calendar 2026) [Source](https://www.ftb.ca.gov/forms/2026/2026-3536.pdf) |
| Return: LLC classified as a partnership | Form 568 | 15th day of the 3rd month after the year ends [Source](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=18633.5.) |
| Return: disregarded LLC owned by a pass-through entity (S corporation, partnership, or LLC classified as a partnership) | Form 568 | 15th day of the 3rd month after the year ends [Source](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=18633.5.) |
| Return: any other disregarded LLC (for example, owned by an individual) | Form 568 | 15th day of the 4th month after the owner's year ends [Source](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=18633.5.) |
| Fee balance | FTB 3536, or FTB 3537 for an extension payment | Original due date of the return; annual tax retains its earlier FTB 3522 deadline [Source](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17942.) |

- **Weekends and holidays.** When a due date falls on a weekend or holiday, it moves to the next business day.
- **Extensions.** No application is needed. An LLC in good standing that is classified as a partnership gets an automatic **seven-month** extension to file. A disregarded LLC gets **six months**, except one owned by a partnership or an LLC classified as a partnership, which gets seven months. Suspended or forfeited LLCs get none. An extension does not extend the time to pay ([R&TC §18567](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=18567.)).
- **2025 disregarded LLC return content only.** Complete Form 568 Side 1, Side 2, Side 3 and Side 7 (Schedule IW), and pay the tax and any fee. Schedules B and K are also required if either test is met: Schedule B income or loss (line 1 or lines 3 to 11) is $3,000,000 or more; or Schedule K line 21a (total distributive income/payment items) is $3,000,000 or more, or minus $3,000,000 or less. Schedule T is required if a nonresident owner has not signed the consent. Do not reuse the sides, $3,000,000 tests or Schedule T instructions for a 2026 return without reading its form: Check this point with one of our partner accountants.
- **Paying.** Pay by Web Pay, electronic funds withdrawal, card, or by mail with the voucher. Do not send the annual tax with Form 568; use form 3522.

### Stopping the tax: cancellation

File the final Form 568 with its Final Return box checked and the required SOS termination documents; a final return alone does not stop the annual charge. To obtain the following-year relief under [§17947](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17947.), file a **timely** final return for the preceding year (including an allowed extension), do no California business after that final year, and file the prescribed SOS dissolution/cancellation before the end of the 12-month period beginning on the final-return filing date. A return requiring another subsequent return to reflect chapter tax is not a qualifying final return.

The FTB identifies **LLC-4/7** and, for domestic dissolution, **LLC-3**; the appropriate SOS documents depend on the circumstances. If the termination timing or short-form eligibility is in doubt, apply the referral above rather than promise that the next year's tax stops. [2025 booklet, Q](https://www.ftb.ca.gov/forms/2025/2025-568-booklet.html); [§17941(b), (e)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17941.).

### 2025 returns, including those filed on extension in autumn 2026 ([FTB: Doing business in California](https://www.ftb.ca.gov/file/business/doing-business-in-california.html))

- The annual tax ($800), the fee bands and the 10% estimate penalty were the same for 2025 as for 2026. The 2025 annual tax was due 15 April 2025 (calendar year), and the 2025 estimated fee **16 June 2025**, because 15 June was Sunday ([2025 FTB 3536](https://www.ftb.ca.gov/forms/2025/2025-3536.pdf)).
- The 2025 doing-business amounts are $757,070 (sales), $75,707 (property) and $75,707 (payroll).
- An LLC formed in 2024 or 2025 had no first-year waiver.
- For calendar 2025, partnership-classified and pass-through-owned SMLLC returns are due **16 March 2026** after the Sunday adjustment; other SMLLC returns are due **15 April 2026**. The ordinary extended date is **15 October 2026** for partnership-classified LLCs and individual-owned SMLLCs; an S-corporation-owned SMLLC has the six-month extension from its March due date, not the seven-month partnership extension. Amounts unpaid after their original payment deadlines are late. [§18633.5](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=18633.5.); [2025 booklet, E](https://www.ftb.ca.gov/forms/2025/2025-568-booklet.html).

Federal tax discussion is general information tied to the stated facts; this state-charge computation gives no federal filing conclusion.

## Completion checklist

Record classification, tax year, nexus trigger, exceptions, the California income build-up, band, both payments and dates, prior-year fee and penalty test, return/extension date, cancellation status and any holds. Return a liability summary, form/voucher details and a short reviewer brief; never prepare held conclusions as usable filing instructions.

## Sources

| Official source | Passages read and purpose | Read on |
|---|---|---|
| [R&TC §17941](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17941.) | Whole section: triggers, definition/exempt organizations, ordinary due date, cancellation, military definition, historical waiver/budget condition and enacted first-year reduction. Browser read; direct fetch returned 403. | 2026-11-27 |
| [R&TC §23153](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=23153.) | Whole section, relying on (d)(1) for the ordinary $800 amount incorporated by §17941(a). Corporate concessions are not generalized to LLCs. | 2026-11-27 |
| [R&TC §17942](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17942.) | Whole section: four bands, gross-income/COGS definition, lower-tier exclusion, assignment, group aggregation, due date and estimate penalty protection. Browser read. | 2026-11-27 |
| [R&TC §24271](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=24271.) | Whole section: gross-income dependency; special components held rather than infer exclusions. | 2026-11-27 |
| [R&TC §23101](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=23101.) | Whole section: activity, domicile, separate sales/property/payroll tests, annual indexing and pass-through shares. | 2026-11-27 |
| [R&TC §17946](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17946.) | Whole section: both no-business and 15-days-or-less conditions. | 2026-11-27 |
| [R&TC §18633.5](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=18633.5.) | Whole section: partnership return date, corporate exclusion, disregarded filing, owner-year substitution, owner-dependent due dates and consent dependency. | 2026-11-27 |
| [R&TC §18567](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=18567.) | Whole section: extension authority and no extension of payment. | 2026-11-27 |
| [R&TC §19131](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=19131.) | Whole section: ordinary filing penalty, reasonable cause/no willful neglect, tax reduction and distinct fraud rule. | 2026-11-27 |
| [R&TC §19132](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=19132.) | Whole section: payment penalty, monthly balance/cap and interaction with filing/demand penalties. | 2026-11-27 |
| [R&TC §19172](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=19172.) | Whole section: partnership filing/information failures, all persons members during year, monthly amount, 12-month cap and reasonable cause. | 2026-11-27 |
| [R&TC §19135](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=19135.) | Whole section: entity status, California business, notice, 60 days and reasonable-cause/no-willful-neglect tests. | 2026-11-27 |
| [R&TC §17947](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17947.) | Whole section: following-year termination relief and definition of timely final return. | 2026-11-27 |
| [Corporations Code §17707.02](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CORP&sectionNum=17707.02.) | Whole section: short cancellation's voting, debt, asset, investor-payment and return conditions; eligibility is referred, not replaced with a partial checklist. | 2026-11-27 |
| [R&TC §25135](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=25135.) and [§25136](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=25136.) | Whole sections: goods delivery/shipment rules and market assignment for services/intangibles, including securities exception. Complex assignments referred. | 2026-11-27 |
| [2026 FTB 3522](https://www.ftb.ca.gov/forms/2026/2026-3522.pdf) and [2025 FTB 3522](https://www.ftb.ca.gov/forms/2025/2025-3522.pdf) | One-page instructions and voucher for each year: ordinary annual tax, due date, first taxable year, late-entering foreign LLC, payment channels and voucher-year control. | 2026-11-27 |
| [2026 FTB 3536](https://www.ftb.ca.gov/forms/2026/2026-3536.pdf) and [2025 FTB 3536](https://www.ftb.ca.gov/forms/2025/2025-3536.pdf) | One-page instructions and voucher for each year: estimate/balance, no-fee/short-year rules, penalty, timely prior-fee protection, 2026 line 2 estimate and actual 16 June 2025 voucher date. | 2026-11-27 |
| [FTB LLC page](https://www.ftb.ca.gov/file/business/types/limited-liability-company/index.html) | Annual tax and first-year June example, fee rounding/table, classification, nonregistered foreign partnership and cancellation passages. | 2026-11-27 |
| [FTB doing-business page](https://www.ftb.ca.gov/file/business/doing-business-in-california.html) | Entire nexus/threshold and Public Law 86-272 passages; table ends at 2025, with 2025 figures $757,070/$75,707/$75,707. | 2026-11-27 |
| [2025 Form 568 booklet](https://www.ftb.ca.gov/forms/2025/2025-568-booklet.html) | D, E, F, G, Q, S and specific lines 1–3: filing exceptions, extensions by owner, payment, penalties, cancellation, historical SMLLC sides/Schedule T and B/K tests. 2025 layout only. | 2026-11-27 |
| [FTB business due dates](https://www.ftb.ca.gov/file/when-to-file/due-dates-business.html) | LLC sections: owner/classification dates, extension dates and weekend/holiday rule. | 2026-11-27 |

Not yet confirmed: usable 2026 indexed nexus amounts; 2026 Form 568 layout; applying the future reduction to the 2022-organized/2027-registered foreign example or after a 15-day exempt 2026 year. These and the other expressly held topics above are **non-usable**, not filing advice. Check this point with one of our partner accountants.
