---
name: ga-corporate-and-ptet
description: "Source-cited tax guide for US-GA: ga corporate and ptet. Unverified draft, pending local-accountant review."
jurisdiction: US-GA
tax_year: 2026
last_updated: 2026-09-25
authored_by: OpenAccountants team
review_status: pending_review
trust_label: By OpenAccountants
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Georgia corporate income tax, net worth tax and the pass-through entity tax election

## Scope and who this is for ([2025 IT-611 booklet](https://dor.georgia.gov/document/document/2025-it611-corporate-income-tax-instruction-booklet/download); [DOR corporate income and net worth tax](https://dor.georgia.gov/corporate-income-and-net-worth-tax))

This Guide covers Georgia tax for **tax year 2026**, with a dated section for **2025 returns**. It covers:
- the corporate income tax on Form 600;
- the corporate net worth tax, which C corporations report on Form 600 and S corporations on Form 600S;
- the election by an S corporation (Form 600S) or a partnership (Form 700) to pay Georgia income tax at the entity level. This Guide calls it the pass-through entity tax (PTET) election. DOR calls it the "election to pay tax at the entity level";
- corporate and electing-entity estimated tax, penalties and filing.

Figures are for tax year 2026 unless labelled 2025. The 2026 IT-611, IT-611S and IT-711 booklets were not published on 25 September 2026, so rules found only in the 2025 booklets are labelled 2025.

Who is subject to it:
- **Corporate income tax.** "All corporations that own property or do business in Georgia, or that have income from Georgia sources are required to file a Georgia income tax return."
  - A corporation that is a partner, limited or general, in a partnership that owns property, does business or has income in Georgia is treated as doing so itself.
- **Net worth tax.** Domestic corporations, and foreign corporations that do business, own property or are registered with the Secretary of State in Georgia.
  - It is not charged on partnerships, LLCs taxed as partnerships, or disregarded single-member LLCs. A corporate owner of a disregarded LLC with Georgia activity is charged.
  - Public Law 86-272 does not protect a corporation from the net worth tax.

It does **not** cover:
- the owner's own Form 500 (see `ga-income-tax`);
- nonresident withholding and composite returns (Form IT-CR) when no election is made;
- sales and use tax, insurance premium tax and property tax;
- the detail of Georgia credits. See "When to refuse or refer".

## Ask the client first

- **Which tax year, and is it a calendar year?** The rate is set by the year the taxable period **begins**, and it is not prorated for fiscal years (2025 IT-611). A fiscal year beginning in 2025 uses the 2025 rate for the whole year.
- **Entity type for federal purposes:** C corporation, S corporation (and any QSub), partnership or LLC taxed as one, or a disregarded single-member LLC.
- **For an S corporation: any nonresident shareholders?** Each must sign Form 600S-CA, or Georgia does not recognise the S election (see the boundary table).
- **Where the company is incorporated,** or whether it has domesticated in Georgia. This decides whether net worth tax is on 100% of net worth or on a Georgia ratio ([2025 IT-611](https://dor.georgia.gov/document/document/2025-it611-corporate-income-tax-instruction-booklet/download)).
- **Georgia activity:** property, employees, and whether sales activity goes beyond solicitation of orders for tangible goods (Public Law 86-272).
- **Gross receipts** by customer location (Georgia and everywhere) for the apportionment ratio.
- **Federal taxable income and the book-tax detail:**
  - section 168(k) bonus depreciation claimed, now or in earlier years;
  - research costs under sections 174 and 174A;
  - business interest (section 163(j));
  - dividends, intangible expenses and interest paid to related members (these may need addback);
  - state income taxes deducted federally.
- **Net operating losses** by loss year. Record whether each loss year ended after 31 December 2017 (carryback and carryforward rules) and whether it began on or after 1 January 2018 (80% limit). Note any farm or insurance-company losses ([2025 IT-611](https://dor.georgia.gov/document/document/2025-it611-corporate-income-tax-instruction-booklet/download)).
- **Balance sheet** (federal Schedule L) at the end of the year, including issued capital stock, paid-in surplus and retained earnings, for the net worth tax.
- **Prior-year Georgia tax,** and whether that return covered 12 months. This drives the estimated-tax safe harbour.
- **Affiliated group?** Whether it files a federal consolidated return and whether it has elected, or had permission, to file a Georgia consolidated return.
- **For an S corporation or partnership: does it want the entity-level election?** Collect:
  - the owners and their residence;
  - any owner estimated payments already made;
  - whether any owner wants the Georgia income taxed at the owner level instead.

  The election binds all owners.
- **Credits:** any Georgia credit claimed, purchased or carried forward. Credit returns must be filed electronically.

## The method, step by step

1. **Pick the rate by the start of the taxable year.** 2025: 5.19% ([HB 111](https://gov.georgia.gov/document/2025-signed-legislation/hb-111/download)). 2026: 4.99% ([HB 463](https://gov.georgia.gov/document/2026-signed-legislation/hb-463/download)). The corporate rate is tied by statute to the individual rate for the corresponding taxable year (see "Figures, with years").
2. **Decide which return.**
   - C corporation: Form 600.
   - S corporation: Form 600S, unless a nonresident shareholder has not consented on Form 600S-CA. In that case, file Form 600 and pay the regular corporate tax.
   - Partnership: Form 700.
   - Disregarded single-member LLC: included in the owner's return.
3. **Start from federal taxable income** and make the Georgia additions and subtractions (Form 600 Schedules 4 and 5). Apply the HB 1199 conformity rules. The main business items:
   - add back section 168(k) bonus depreciation and use Georgia depreciation;
   - apply section 174 and section 163(j) as they stood before the 2017 federal act, and treat section 174A as not in effect;
   - add back income taxes of other states, the United States and foreign countries deducted federally;
   - add back intangible expenses, related interest and captive REIT expenses paid to related members, unless an exception is shown on Form IT-Addback or IT-REIT;
   - add back payments of more than $600 in a year to unauthorized employees ([2025 IT-611](https://dor.georgia.gov/document/document/2025-it611-corporate-income-tax-instruction-booklet/download)).
4. **Separate nonbusiness income, then apportion.**
   - Allocate investment interest, investment rents and non-business gains as the 2025 IT-611 describes.
   - Apportion the rest by the single **gross receipts factor**: Georgia gross receipts divided by gross receipts everywhere.
   - Receipts other than sales of tangible goods are Georgia receipts "if received from customers within this State, or if the receipts are otherwise attributable to this State's marketplace" (Reg. 560-7-7-.03 has the detail).
   - A partner in a partnership or joint venture includes its pro rata share of the partnership's gross receipts.
5. **Apply the NOL.** Use Schedule 9 and Form IT-552.
   - Losses from years beginning before 2018 apply first, without the 80% limit ([2025 IT-611](https://dor.georgia.gov/document/document/2025-it611-corporate-income-tax-instruction-booklet/download), NOL worksheet).
   - Losses from years beginning on or after 1 January 2018 (except those of certain insurance companies) may offset no more than 80% of Georgia income before NOLs ([2025 IT-611](https://dor.georgia.gov/document/document/2025-it611-corporate-income-tax-instruction-booklet/download)).
   - Carry the Georgia apportioned loss, not the federal loss.
6. **Compute income tax** at the year's rate. Then apply credits (Schedule 10) and prepayments.
7. **Compute net worth tax** from the net worth table (see below).
   - Domestic and domesticated corporations use 100% of net worth ([2025 IT-611](https://dor.georgia.gov/document/document/2025-it611-corporate-income-tax-instruction-booklet/download)).
   - Foreign corporations use the Georgia ratio from property and gross receipts (Schedule 8 on Form 600).
8. **For an S corporation or partnership considering the election:**
   - compute tax on its Georgia-apportioned and allocated net income at the year's rate;
   - tick the election box and complete the entity-level schedules by the due date or extended due date;
   - make estimated payments as a C corporation would;
   - tell the owners to exclude the taxed income on Form 500 (PTEDED), not to claim a credit.
9. **Check estimated tax and penalties** on Form 600 UET, and file by the due date. Tax is due by the original due date, even with an extension.

## Figures, with years ([HB 111 of 2025](https://gov.georgia.gov/document/2025-signed-legislation/hb-111/download); [HB 463 of 2026](https://gov.georgia.gov/document/2026-signed-legislation/hb-463/download); [HB 1023 of 2024](https://gov.georgia.gov/document/2024-signed-legislation/hb-1023/download); [DOR important tax updates](https://dor.georgia.gov/taxes/important-tax-updates))

**Corporate and entity-level income tax rate**

| Taxable years beginning | Rate | Authority |
| --- | --- | --- |
| On or after 1 January 2025 | 5.19% | HB 111 (2025), O.C.G.A. § 48-7-20(a.1); 2025 IT-611, IT-611S and IT-711 |
| On or after 1 January 2026 | 4.99% | HB 463 (2026), which states it reduces "the rates of taxation on corporate and partnership income" |
| From 1 January 2027 | 0.125 points lower each year until 3.99% | HB 463, subject to the delays below |

- **Why the corporate rate follows the individual rate.** HB 1023 (2024) rewrote O.C.G.A. § 48-7-21(a). Corporations now pay tax "at the same rate of the tax imposed on individuals under subsection (a.1) of Code Section 48-7-20 for the corresponding taxable year". It did the same for electing S corporations (§ 48-7-21(b)(7)(C)(ii)) and electing partnerships (§ 48-7-23(b)(3)). It applies to taxable years beginning on or after 1 January 2024.
- **Future cuts can be delayed.** Each scheduled cut is delayed by one year for each year that any of these is true as of 1 December:
  - the Governor's revenue estimate for the next fiscal year is not at least 3% above the estimate for the present fiscal year;
  - the prior fiscal year's net revenue collection was not higher than each of the three preceding fiscal years;
  - the Revenue Shortfall Reserve does not hold more than the projected revenue cost of the cut.

  The Office of Planning and Budget reports its determinations by 1 December each year. Treat any 2027 rate below 4.99% as unconfirmed until then.
- **DOR's corporate page and the 2025 booklets still show 5.19%** because they describe tax year 2025. DOR's "2026 Income Tax Changes" note confirms the 4.99% flat rate for 2026.

**Net worth tax table** ([2025 IT-611 booklet](https://dor.georgia.gov/document/document/2025-it611-corporate-income-tax-instruction-booklet/download); [DOR corporate income and net worth tax](https://dor.georgia.gov/corporate-income-and-net-worth-tax))

| Net worth (domestic: total; foreign: employed in Georgia) | Tax |
| --- | --- |
| Not exceeding $100,000 | $0 (return still required) |
| Over $100,000, not exceeding $150,000 | $125 |
| Over $150,000, not exceeding $200,000 | $150 |
| Over $200,000, not exceeding $300,000 | $200 |
| Over $300,000, not exceeding $500,000 | $250 |
| Over $500,000, not exceeding $750,000 | $300 |
| Over $750,000, not exceeding $1,000,000 | $500 |
| Over $1,000,000, not exceeding $2,000,000 | $750 |
| Over $2,000,000, not exceeding $4,000,000 | $1,000 |
| Over $4,000,000, not exceeding $6,000,000 | $1,250 |
| Over $6,000,000, not exceeding $8,000,000 | $1,500 |
| Over $8,000,000, not exceeding $10,000,000 | $1,750 |
| Over $10,000,000, not exceeding $12,000,000 | $2,000 |
| Over $12,000,000, not exceeding $14,000,000 | $2,500 |
| Over $14,000,000, not exceeding $16,000,000 | $3,000 |
| Over $16,000,000, not exceeding $18,000,000 | $3,500 |
| Over $18,000,000, not exceeding $20,000,000 | $4,000 |
| Over $20,000,000, not exceeding $22,000,000 | $4,500 |
| Over $22,000,000 | $5,000 |

- **The $100,000 exemption dates from 2018, not HB 1023.** DOR: "For net worth years beginning on or after January 1, 2018 (those reported on the 2017 income tax return), corporations with a net worth of $100,000 or less are not subject to tax but must file a return." HB 1023 (2024) dealt with the rate link and the corporate extension, not net worth.
- **What counts as net worth:** issued capital stock, paid-in surplus and retained earnings. Treasury stock is not deducted. A deficit net worth still requires a return but owes no tax.
- **Which balance sheet.** The net worth tax on a return is for the following net worth year. DOR: the net worth tax dates "would be one year later than the income tax beginning and ending dates". It is measured on the net worth at the first day of that net worth year, which is the prior year's ending balance sheet.
- **Initial return.** A new corporation files an initial net worth return based on its opening balance sheet. If the period is shorter than six months, 50% of the tax is due.
  - The 2025 IT-611 gives the due date as the 15th day of the **fourth** month after incorporation or qualification for C corporations.
  - The 2025 IT-611S gives the **third** month for S corporations.
- **Short periods** (other than initial or final returns) use the short period's ending balance sheet, and the tax is prorated by months.
- **Final return.** A liquidated corporation filing its final income tax return owes no net worth tax and gets no refund of net worth tax already paid.

**Federal conformity (HB 1199 of 2026)** ([HB 1199](https://gov.georgia.gov/document/2026-signed-legislation/hb-1199/download))

- **Conformity date.** For taxable years beginning on or after 1 January 2025, "Internal Revenue Code" means the IRC as "provided for in federal law enacted on or before January 1, 2026". Section 1 applies "to all taxable years beginning on or after January 1, 2025". So both 2025 and 2026 start from an IRC that includes P.L. 119-21, apart from the listed exceptions.
- **Treated as not in effect** (selected business items):
  - section 168(k) (bonus depreciation);
  - section 174A;
  - section 179(d)(1)(B)(ii);
  - section 199;
  - section 163(h)(4);
  - CARES Act changes to sections 172 and 461(l).

  The full list is longer; read the HB 1199 text for any other section in play.
- **Applied as before the 2017 federal act:** sections 118, 163(j), 174 and 382(k)(1). The 2025 IT-611 says Georgia "does not follow I.R.C Section 174 under the 2017 Tax Cuts and Jobs Act for research and experimental expenditures paid or incurred in tax years beginning after December 31, 2021".
- **The 2025 booklets predate HB 1199** (signed 20 March 2026). They point to DOR's federal tax changes page for conformity. Where an OBBBA change moves federal taxable income on a 2025 return, follow HB 1199, and check that page for DOR guidance before filing.

## Apportionment, NOLs and consolidated returns ([2025 IT-611 booklet](https://dor.georgia.gov/document/document/2025-it611-corporate-income-tax-instruction-booklet/download))

- **Single factor.** "For tax years beginning on or after January 1, 2008, the Georgia apportionment ratio shall be computed by applying only the gross receipts factor."
- **Which receipts go in the factor:**
  - a company that both makes or sells tangible goods and does other business includes gross receipts from both activities;
  - a company with no tangible-goods business includes only gross receipts "from activities which constitute the company's regular trade or business".
- **NOLs:**
  - losses incurred in taxable years **ending** after 31 December 2017: no carryback and an unlimited carryforward;
  - NOLs for tax years beginning on or after 1 January 2018 (except those of certain insurance companies) may offset no more than 80% of Georgia income before NOLs;
  - farm losses have a 2-year carryback;
  - certain insurance-company losses have a 2-year carryback and 20-year carryforward;
  - Georgia did not adopt the 2020 CARES Act NOL changes;
  - Georgia follows IRC sections 108, 381, 382 and 384 (since 2005).
- **Consolidated returns.**
  - Affiliated corporations that file a federal consolidated return file separate Georgia returns, unless they have Georgia approval or are required to file consolidated.
  - For tax years beginning on or after 1 January 2023, a group may elect a Georgia consolidated return on an original return. The parent ticks "Consolidated GA Parent Return" and each subsidiary files Form 600 ticking "GA Consolidated Subsidiary".
  - Each subsidiary still files its own net worth return.
  - Credits and NOLs are tracked company by company for credit limitation.

## The pass-through entity tax election ([DOR HB 149 PTET FAQ](https://dor.georgia.gov/hb-149-pass-through-entity-tax-faq); [2025 IT-711 booklet](https://dor.georgia.gov/document/document/2025-it-711-partnership-income-tax-booklet/download); [2025 IT-611S booklet](https://dor.georgia.gov/document/document/2025-it-611s-s-corporation-income-tax-booklet/download))

- **Who can elect.**
  - The election has been available for taxable years beginning on or after 1 January 2022.
  - For taxable years beginning on or after 1 January 2023, "all partnerships are eligible to make the election to pay tax at the entity level, regardless of who owns or controls the partnership".
  - S corporations are eligible.
  - "Single-member LLCs not taxed as a Partnership or S Corporation are not eligible to make the election."
  - For 2022 only, a partnership had to be 100% owned by persons eligible to be S corporation shareholders.
- **How and when.**
  - Tick the box and complete the schedules on Form 600S (S corporation) or Form 700 (partnership).
  - The election "must be made by the due date or extended due date of the entity's income tax return and is irrevocable after the applicable due date passes".
  - It is annual; each year stands alone.
- **Rate and base.** The electing entity pays at the individual rate for the corresponding year: 5.19% for 2025 and 4.99% for 2026. The base is the entity's net income allocated and apportioned under O.C.G.A. § 48-7-31 (HB 1023).
  - The entity cannot deduct "taxes that are based on or measured by gross or net income or any other variant thereof" in computing that income.
- **Binds everyone.** "The election to pay tax at the entity level is binding on all the owners including the nonresident owners". Do not file a composite return for the nonresident owners.
  - An S corporation that elects is also outside the nonresident-member withholding rule.
- **How owners report it: an exclusion, not a credit.** On Form 500:
  - owners enter their share of income taxed at the entity level on Schedule 1, Line 12, described PTEDED (a subtraction);
  - they enter their share of loss apportioned and allocated at the entity level on Schedule 1, Line 5, described PTEADD (an addition);
  - "The owners are not eligible to claim a credit for taxes paid to Georgia with respect to income taxed at the entity level by Georgia."
- **Owner income not taxed at the entity level by Georgia** (for example a resident owner's share of income apportioned to other states) stays taxable to the owner.
  - The owner may claim the credit for taxes paid to other states on it, if O.C.G.A. § 48-7-28 is met.
  - Or the owner may take the § 48-7-27(d) adjustment where another state taxed it at entity level.
- **Tax attributes stay with the entity.** Credits and NOLs do not pass through, even if the entity does not elect in a later year.
  - An electing entity may make an irrevocable election to pass through credits generated in the year.
  - That credit pass-through is not available for the Qualified Education Expense credit, the Qualified Education Donation credit or the Qualified Rural Hospital Expense credit.
  - NOLs are handled as for C corporations.
- **Composite overpayments** from an earlier year cannot be claimed on the electing entity's return; request a refund instead.
- **Federal side** ([IRS Notice 2020-75](https://www.irs.gov/pub/irs-drop/n-20-75.pdf)).
  - An S corporation or partnership that makes a "Specified Income Tax Payment" is "allowed a deduction for the Specified Income Tax Payment in computing its taxable income for the taxable year in which the payment is made".
  - It is not a separately stated item for owners, and it "is not taken into account in applying the SALT deduction limitation" to any partner or shareholder.
  - The deduction follows the **payment year**. A 2026 balance paid in 2027 is a 2027 federal deduction.
  - Whether electing saves tax now depends on each owner's own federal itemized-deduction position. Model it per owner.

## Estimated tax ([2025 IT-611 booklet](https://dor.georgia.gov/document/document/2025-it611-corporate-income-tax-instruction-booklet/download); [2026 Form 602-ES](https://dor.georgia.gov/document/document/2026-602es-corporate-and-partnership-estimated-tax/download); [Form 600 UET, 2025 and later](https://dor.georgia.gov/document/document/beginning-or-after-january-1-2025-600-uet-underpayment-estimated-tax/download); [DOR HB 149 PTET FAQ](https://dor.georgia.gov/hb-149-pass-through-entity-tax-faq))

- **Who must pay.**
  - Every corporation subject to Georgia tax, if its net income for the year "can reasonably be expected to exceed Twenty-Five Thousand Dollars ($25,000.00)".
  - An electing S corporation or partnership "is required to make estimated tax payments in the same manner as a C Corporation", using Form 602-ES or the Georgia Tax Center. A partnership must register its account on the Georgia Tax Center to pay online.
- **Due dates (calendar year 2026):** 15 April, 15 June, 15 September and 15 December 2026, each 25% of the estimated tax, if the requirement is first met before the fourth month.
  - If the requirement is first met later, fewer installments are due:
    - after the third month and before the sixth month: one third each at the 6th, 9th and 12th months;
    - after the fifth month and before the ninth month: 50% at each of the 9th and 12th months;
    - after the eighth month and before the twelfth month: 100% at the 12th month.
  - Fiscal-year filers use the 15th day of the 4th, 6th, 9th and 12th months.
- **Required amount (Form 600 UET).** Each installment is the lesser of:
  - 100% of the immediately preceding year's tax, if that return covered a 12-month period, divided by the number of installments;
  - 70% of the current year's tax after credits, divided by the number of installments.
- **Exception:** the annualized-income exception applies if payments to date equal or exceed 70% of the tax on annualized income for the months before the installment.
- **Penalty:** 9% a year on each underpaid installment. DOR booklets also warn of "a penalty of 5% of the income tax for failure to pay estimated tax".
  - The penalty period runs to the payment date or 15 April, whichever is earlier; for S corporations and partnerships, 15 March.
- **Electing entities in their first election year.** The prior-year safe harbour is not simply $0. DOR's FAQ says the entity "must compute the penalty on Form 600 UET assuming the tax for the prior year was equal to 5.75% of the prior's year's income".
  - 5.75% is the pre-2024 rate that HB 1023 struck out of the statute. The FAQ has not been updated for the lower rates, so ask DOR which rate it applies before relying on this.
  - Owners' own estimated payments cannot be transferred to the entity. The entity may tick "UET Annualization Exception Attached" and compute the penalty as if those payments were its own.
- **Electronic payment.** Quarterly payments of more than $10,000 must be made by electronic funds transfer. There is a 10% penalty if not paid through the Georgia Tax Center.

## Boundary and exception table ([2025 IT-611 booklet](https://dor.georgia.gov/document/document/2025-it611-corporate-income-tax-instruction-booklet/download); [2025 IT-611S booklet](https://dor.georgia.gov/document/document/2025-it-611s-s-corporation-income-tax-booklet/download); [DOR net worth tax FAQ](https://dor.georgia.gov/net-worth-tax-corporations-faq); [DOR HB 149 PTET FAQ](https://dor.georgia.gov/hb-149-pass-through-entity-tax-faq))

| Situation | Rule |
| --- | --- |
| Net worth exactly $100,000 | No tax ("Not exceeding $100,000"), but the return is still due. |
| Net worth $100,001 | $125 (over $100,000). |
| Fiscal year beginning 1 July 2025 | 5.19% for the whole year; the rate is not prorated. |
| Corporation expects net income of exactly $25,000 | No estimated tax required. The test is "exceed" $25,000. |
| Prior-year Georgia return covered 9 months | The 100%-of-prior-year option is unavailable. Use 70% of the current year's tax. |
| S corporation with a nonresident shareholder who did not sign Form 600S-CA | Georgia does not recognise the S election. The corporation files Form 600 and pays the regular corporate tax. |
| S corporation, no election, nonresident shareholders | Withholding applies unless (a) a composite return (Form IT-CR) is filed, (b) the members' aggregate annual share of Georgia-sourced taxable income is less than $1,000, or (c) the shareholder has a properly executed Form 600S-CA, in which case withholding is not due provided the shareholder reports the income and pays the tax. |
| Protected by Public Law 86-272 | No income tax (enter zero on Schedule 1, Line 8, and attach a statement), but the net worth tax still applies and Form 600 or 600S must be filed. |
| Single-member LLC disregarded federally | Not eligible for the PTET election, and not subject to net worth tax. Its corporate owner may be. |
| Partnership wants to elect after the extended due date has passed | Too late for that year. The election is irrevocable once the due date passes. |
| Owner of an electing entity asks for a Georgia credit for the entity's tax | Not allowed. The owner excludes the income (PTEDED) instead. |
| Consolidated group, net worth tax | Each subsidiary files its own net worth return; no consolidation of net worth. |

## Worked cases ([HB 463](https://gov.georgia.gov/document/2026-signed-legislation/hb-463/download); [2025 IT-611 booklet](https://dor.georgia.gov/document/document/2025-it611-corporate-income-tax-instruction-booklet/download); [Form 600 UET](https://dor.georgia.gov/document/document/beginning-or-after-january-1-2025-600-uet-underpayment-estimated-tax/download); [DOR HB 149 PTET FAQ](https://dor.georgia.gov/hb-149-pass-through-entity-tax-faq))

Amounts described as client facts are hypothetical inputs.

**Case 1: 2026, calendar-year C corporation incorporated in Georgia.**

Client facts:
- Georgia taxable income before apportionment (after additions and subtractions) of $1,000,000.
- Georgia gross receipts of $3,000,000 out of $10,000,000 everywhere.
- 2025 Georgia tax on a 12-month return of $16,000.
- Net worth on the 31 December 2026 balance sheet of $2,500,000.

Working:
- Apportionment ratio: $3,000,000 / $10,000,000 = 30%. Georgia taxable income is $300,000.
- Tax: $300,000 times 4.99% = $14,970.
- Estimated tax: 100% of the prior year is $16,000, and 70% of the current year is $10,479. The required amount is the lesser, $10,479, or $2,619.75 per installment.
  - In April the 2026 tax is not known, so paying $4,000 a quarter (100% of 2025) is the safe route.
- Net worth tax on the same Form 600: $2,500,000 falls in the "over $2,000,000, not exceeding $4,000,000" band, so $1,000.

**Case 2: 2025 return, C corporation using a post-2017 NOL.**

Client facts: Georgia income before NOL of $450,000, and Georgia NOL carryforward of $600,000, all from years beginning after 2017.
- NOL allowed: 80% of $450,000 = $360,000.
- Georgia taxable income: $90,000.
- Tax: $90,000 times 5.19% = $4,671.
- NOL carried forward: $600,000 minus $360,000 = $240,000, with no expiry.

**Case 3: 2026, S corporation electing to pay at the entity level.**

Client facts: two Georgia-resident shareholders at 50% each, and all income from Georgia. Georgia net income of $500,000. No nonresident shareholders.
- Entity-level tax: $500,000 times 4.99% = $24,950.
- Election: tick the box on the 2026 Form 600S by its due date or extended due date.
- Estimated tax: net income is expected to exceed $25,000, so the entity pays estimates like a C corporation.
  - 70% of $24,950 is $17,465, so paying $4,366.25 a quarter meets the current-year test.
  - For the prior-year test in a first election year, see the FAQ rule above.
- Each shareholder's share of income is $250,000. Each enters it on the 2026 Form 500 as a PTEDED subtraction and claims no Georgia credit for the entity's tax.
- Federal: the S corporation deducts the Georgia tax in the year it pays it.

**Case 4: net worth tax boundaries.**
- Domestic corporation with net worth of $100,000: $0, but it files.
- Domestic corporation with net worth of $150,000: $125, because the band is "not exceeding $150,000".
- Foreign corporation with total net worth of $10,000,000 and a Georgia ratio (Schedule 8) of 25%:
  - net worth employed in Georgia is $2,500,000, so the tax is $1,000;
  - it would pay $1,750 on the full $10,000,000 if it domesticated.
- DOR's own short-period example: net worth of $900,000 falls in the $500 band. For a three-month short period, $500 times 3/12 = $125.

**Case 5: S corporation with a nonresident shareholder who has not consented.**

Client facts: a 2025 Form 600S with one nonresident shareholder who did not sign Form 600S-CA.
- Georgia disregards the S election.
- The corporation files Form 600 and pays corporate income tax at 5.19% on its Georgia taxable income, plus net worth tax.
- Get the consent signed before filing if the shareholders want S treatment.

## When to refuse or refer

- **Nexus in doubt,** including whether activity goes beyond solicitation under Public Law 86-272, and remote sellers of services.
- **Sourcing of services and intangibles** where customer location is unclear. Reg. 560-7-7-.03 governs; refer.
- **Consolidated return elections** and terminations, and intercompany transactions.
- **Section 381 and 382 limits** after an ownership change, and any insurance-company or farm NOL.
- **Georgia credits.** HB 463 repealed several income tax credits for taxable years beginning on or after 1 January 2026. These include the port activity credits (§§ 48-7-40.15 and 40.15A), the headquarters credit (§ 48-7-40.18) and the alternative-fuel and electric-vehicle-charger credits (§ 48-7-40.16). Carryforwards, the film credit, credit purchases and transfers need a specialist and DOR's credit pages.
- **The PTET decision for owners with large non-Georgia income,** credits for taxes paid to other states, or other states' entity-level elections (§ 48-7-27(d)).
- **Federal audit adjustments and partnership audit elections.** Amended Georgia returns are due within 180 days of the final federal determination.
- **Insurance companies, financial institutions, exempt organizations (Form 600-T), and fiduciaries (Form 501).**

## Filing and payment ([2025 IT-611 booklet](https://dor.georgia.gov/document/document/2025-it611-corporate-income-tax-instruction-booklet/download); [2025 IT-611S booklet](https://dor.georgia.gov/document/document/2025-it-611s-s-corporation-income-tax-booklet/download); [2025 IT-711 booklet](https://dor.georgia.gov/document/document/2025-it-711-partnership-income-tax-booklet/download); [DOR penalty and interest rates](https://dor.georgia.gov/penalty-and-interest-rates))

- **Due dates:**
  - **Form 600:** the 15th day of the 4th month after year-end (15 April for a calendar year).
  - **Form 600S:** the 15th day of the 3rd month.
  - **Form 700:** the 15th day of the 3rd month (15 March for a calendar year).
  - A due date falling on a weekend or holiday moves to the next business day.
- **Extensions:**
  - **Corporations (Form 600 and Form 600S):** no Georgia extension request is needed with an automatic federal extension. There is no late-filing penalty if the return is received within the federal extended period **plus one additional month**, with Form 7004 attached. This applies from tax years beginning 1 January 2025 (HB 1023). Georgia law prohibits an extension of more than seven months.
  - **Partnerships (Form 700):** file within the federal extended period with Form 7004 attached. There is no extra month; Georgia law prohibits an extension of more than six months.
  - Without a federal extension, use Form IT-303. Tick the "Extension" box, or a late-filing penalty is assessed.
- **Payment is not extended.** Pay by the original due date with Form IT-560C (claimed on Form 600 Schedule 3, Line 2, or Form 600S Schedule 4, Line 2). Late payment penalty and interest run from the statutory due date regardless of any extension.
- **Income tax penalties:**
  - late filing: 5% of the tax not paid by the original due date for each month or part month, up to 25%;
  - late payment: 1/2 of 1% per month, up to 25%, but not due if the return is amended because of an IRS audit;
  - the late filing and late payment penalties together cannot exceed 25% of the tax not paid by the original due date;
  - negligent underpayment: 5%;
  - fraudulent underpayment: 50%.
- **Net worth tax penalties:** late filing 10% of the tax due, and late payment 10% of the tax due.
- **Interest** accrues at the Federal Reserve prime rate plus 3%, reviewed each January.
- **Electronic filing** is required if payments are made by electronic funds transfer, if the federal counterpart must be e-filed, or if the return uses any series 100 credit.
- **Attachments:** a complete copy of the federal return, including Schedule L even if not required federally.
- **Refund claims:** within three years of the later of the payment date and the return's due date, including extensions.

**2025 returns still open (as of 25 September 2026).**
- **Rate:** 5.19% for C corporations, electing S corporations and electing partnerships.
- **A calendar-2025 C corporation on federal extension** avoids Georgia late-filing penalties if the return is received within one month after the federal extended date and Form 7004 is attached. The tax was due 15 April 2026, and interest and late-payment penalty run from then.
- **A calendar-2025 S corporation or partnership that wants the 2025 election** must make it on the 2025 Form 600S or Form 700 by that return's due date or extended due date.
  - DOR has not said whether the extra month for corporations extends the S corporation election deadline.
  - Make the election by the federal extended due date to be safe.
- **For 2025 returns, HB 1199 conformity applies** (IRC as of 1 January 2026), even though the 2025 booklets predate it.

## Completion checklist ([2025 IT-611 booklet](https://dor.georgia.gov/document/document/2025-it611-corporate-income-tax-instruction-booklet/download); [DOR HB 149 PTET FAQ](https://dor.georgia.gov/hb-149-pass-through-entity-tax-faq))

- **Year and rate:** 5.19% for years beginning in 2025, 4.99% for 2026, not prorated for fiscal years.
- **Right form:** Form 600, 600S or 700. Form 600S-CA is signed by every nonresident S corporation shareholder.
- **Additions:** 168(k) addback and Georgia depreciation, other-state income taxes, related-member intangible, interest and REIT addbacks.
- **Apportionment:** gross receipts only; services and intangibles by customer location or market; partnership receipts included pro rata.
- **NOL:** no carryback for losses from years ending after 31 December 2017; 80% limit for years beginning on or after 1 January 2018 (insurance-company exception checked).
- **Net worth tax:** 100% for domestic and domesticated corporations, the Georgia ratio for foreign corporations; correct band; return filed even at $0.
- **PTET:** box ticked by the due date or extended due date; estimates paid as a C corporation; no composite return; owners told to use PTEDED or PTEADD and claim no Georgia credit.
- **Estimated tax:** the $25,000 test checked; Form 600 UET attached with the exception box if used; EFT used where quarterly payments exceed $10,000.
- **Payment and extension:** paid by the original due date with IT-560C; extension box ticked; Form 7004 attached.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
