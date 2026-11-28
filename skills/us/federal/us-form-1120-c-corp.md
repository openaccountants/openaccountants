---
name: us-form-1120-c-corp
description: Prepare the 2026 Form 1120 for a US domestic C corporation, federal only. Covers the flat 21% rate under 26 U.S.C. 11(b), the income and deduction lines, the dividends received deduction (50%, 65%, 100%), the One Big Beautiful Bill Act changes that start in 2026 (the 1 percent floor and 10 percent cap on corporate charitable gifts, the interest capitalization ordering rule and the CFC inclusion carve-out from adjusted taxable income under section 163(j)), domestic research expensing under section 174A, 100% bonus depreciation (linked), the 80% NOL limit, estimated tax under section 6655 with the large corporation rule, the corporate AMT pointer, the accumulated earnings tax and the dividend or retain decision, schedules and attached forms, Form 7004, e-file and penalties. Calendar-year 2026 returns are due 15 April 2027. Trigger on "Form 1120", "C corp return", "corporate tax return", "21% corporate rate", "dividends received deduction", "corporate estimated tax", "Form 7004 corporation", "retain earnings or pay a dividend".
version: "2.2"
jurisdiction: US
tax_year: 2026
last_updated: 2026-11-28
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: corporate-tax
type: computation
---

# US Form 1120, C corporation income tax return, tax year 2026

> **Source-cited draft.** Federal tax years beginning in 2026, with separately labelled original 2025 examples. Statutes, enacted amendments and official IRS sources were read on 28 November 2026; unchanged applicable federal proof read on 26–28 November is reused. Line references describe the identified 2025 Form 1120 edition, subject to the form-edition hold below. This correction makes no new human approval declaration.

**Answer first.** For a tax year beginning in 2026, a C corporation pays a flat **21%** on taxable income (Form 1120 line 30). There is no small-company band and no exempt first slice: USD 1,000 of taxable income means USD 210 of tax. A calendar-year 2026 return is due **15 April 2027**; Form 7004 extends filing (not payment) by 6 months to 15 October 2027. Estimated tax is due in four 25% installments on 15 April, 15 June, 15 September and 15 December 2026 if the year's tax is USD 500 or more. New for 2026: charitable gifts are deductible only above **1 percent** and up to **10 percent** of taxable income; the section 163(j) interest limit is applied before interest is capitalized, and CFC inclusions leave adjusted taxable income. Qualifying domestic research is generally expensed under section 174A, subject to elections and credit coordination. The permanent 100% bonus rate requires qualified property acquired AND placed in service after 19 January 2025; acquisition alone is insufficient.

## Scope and who this is for

In scope: one domestic C corporation filing its own Form 1120 for a tax year beginning in 2026 (calendar year 2026, or a fiscal year beginning in 2026). That includes an ordinary corporation chartered under state or DC law, an eligible LLC electing association status on Form 8832, and an inactive domestic corporation, subject to exemptions and special-return status. The skill covers the page 1 computation, Schedule C (dividends and special deductions), Schedule J (tax), the corporate-specific limits (section 163(j), the NOL rule, the charitable floor and cap, the dividends received deduction), estimated tax, the due date and extension, and the penalties.

Out of scope, and where it goes:

| Topic | Skill or action |
| --- | --- |
| Section 179 and bonus depreciation figures and rules | `us-section-179-and-bonus-depreciation` |
| Research credit (Form 6765) and section 174 / 174A mechanics in detail | `us-r-and-d-section-174-and-41` |
| GILTI (net CFC tested income), FDII and BEAT computations, including the 2026 section 250 percentages | `us-gilti-fdii-beat` |
| Form 5471 (US shareholder of a CFC) | `us-form-5471-cfc-information` |
| Form 5472 (25% foreign-owned US corporation) | `us-form-5472-foreign-owned-us` |
| Extension mechanics and the timely-mailing rule for Form 7004 | `us-corporate-extension-form-7004-and-the` |
| Shareholder's gain on qualified small business stock (section 1202) | `us-section-1202-qsbs` |
| Whether to elect S status instead | `us-s-corp-election-decision` |
| S corporation shareholder K-1 losses | `us-1120-corporation-return-schedule-ordinary-business` |
| State corporate income, franchise and gross receipts taxes | the state's corporate tax skill |
| Consolidated returns, PSCs, personal holding companies, CAMT computation, insurance companies, REITs, RICs, cooperatives, foreign corporations | refuse or refer (see When to refuse or refer) |

## Ask the client first

1. **Tax year and status.** Calendar year or fiscal year (and the year-end month); first, final or short-period return; any Form 8832 or Form 2553 election in force; member of a controlled or affiliated group, and whether a consolidated return (Form 1122) is filed.
2. **Size tests.** Taxable income for each of the three preceding tax years (the USD 1,000,000 large corporation test for estimated tax); average annual gross receipts for the three prior years (the USD 32,000,000 test under section 448(c)); total assets at year-end (USD 250,000 for Schedule L, USD 10 million for Schedule M-3 and Schedule UTP); and, for big groups, average financial statement income (CAMT) and gross receipts of at least USD 500 million (BEAT).
3. **Prior-year return.** The 2025 tax shown on Form 1120 (the estimated tax safe harbor), any NOL, capital loss, charitable, section 163(j) and section 174 carryforwards, and the accumulated earnings and profits at the end of 2025.
4. **Dividends received.** For each payer: domestic or foreign, the percentage owned (by vote and value), how long the stock was held around the ex-dividend date, and whether the stock was bought with debt.
5. **Owners and payouts.** Shareholders (individuals, foreign persons, other corporations), officer pay, dividends paid in 2026, and what the board plans to do with retained earnings (the accumulated earnings tax test).
6. **Spending that changed in 2026.** Charitable gifts, domestic and foreign research spend, interest expense (and any interest that would be capitalized), and assets acquired and placed in service.

## The method, step by step

### Rates, bands and thresholds

| Item | Amount, 2026 | Source |
| --- | --- | --- |
| Corporate income tax rate (section 11(b)) | 21% | [26 U.S.C. 11(b)](https://uscode.house.gov/us/usc/t26/s11/) |
| Dividends received deduction, less than 20% owned domestic payer | 50% | [26 U.S.C. 243(a)(1)](https://uscode.house.gov/us/usc/t26/s243/) |
| Dividends received deduction, 20% or more owned domestic payer | 65% | [26 U.S.C. 243(c)(1)](https://uscode.house.gov/us/usc/t26/s243/) |
| Dividends received deduction, qualifying dividends from an affiliated group member | 100% | [26 U.S.C. 243(a)(3)](https://uscode.house.gov/us/usc/t26/s243/); [Form 1120 (2025), Schedule C line 11](https://www.irs.gov/pub/irs-pdf/f1120.pdf) |
| Dividends on preferred stock of public utilities, Schedule C lines 4 and 5 | 23.3% and 26.7% | [Form 1120 (2025), Schedule C](https://www.irs.gov/pub/irs-pdf/f1120.pdf) |
| Charitable deduction floor, corporations (taxable years beginning after 31 December 2025) | 1 percent | [Public Law 119-21, section 70426](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| Charitable deduction cap, corporations | 10 percent | [Public Law 119-21, section 70426](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| Business interest limit, share of adjusted taxable income | 30 percent | [26 U.S.C. 163(j)(1)(B)](https://uscode.house.gov/us/usc/t26/s163/) |
| Gross receipts test (section 448(c)): exempts a corporation from section 163(j) | USD 32,000,000 | [Rev. Proc. 2025-32](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Domestic research expensing (section 174A) applies to amounts paid or incurred in taxable years beginning after | December 31, 2024 | [Public Law 119-21, section 70302](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| Section 174A(c) election: amortize domestic research over not less than | 60 months | [Public Law 119-21, section 70302](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| NOL deduction limit, losses from taxable years beginning after 2017 | 80 percent of taxable income | [26 U.S.C. 172(a)(2)](https://uscode.house.gov/us/usc/t26/s172/) |
| Estimated tax: no penalty if the year's tax is less than | USD 500 | [26 U.S.C. 6655(f)](https://uscode.house.gov/us/usc/t26/s6655/) |
| Estimated tax: each installment | 25 percent of the required annual payment | [26 U.S.C. 6655(d)(1)(A)](https://uscode.house.gov/us/usc/t26/s6655/) |
| Large corporation: taxable income in any of the 3 preceding years of | USD 1,000,000 or more | [26 U.S.C. 6655(g)(2)](https://uscode.house.gov/us/usc/t26/s6655/) |
| Corporate AMT rate on adjusted financial statement income (applicable corporations) | 15 percent | [26 U.S.C. 55(b)(2)](https://uscode.house.gov/us/usc/t26/s55/) |
| Applicable corporation: 3-year average financial statement income over | USD 1,000,000,000 | [26 U.S.C. 59(k)(1)(B)](https://uscode.house.gov/us/usc/t26/s59/) |
| Foreign-parented group member: BOTH group > USD 1bn and own 3-year average of | USD 100,000,000 or more | [26 U.S.C. 59(k)(1)(B)(ii)](https://uscode.house.gov/us/usc/t26/s59/) |
| Accumulated earnings tax rate | 20 percent | [26 U.S.C. 531](https://uscode.house.gov/us/usc/t26/s531/) |
| Accumulated earnings credit, minimum (USD 150,000 for health, law, engineering, architecture, accounting, actuarial, performing arts or consulting corporations) | USD 250,000 less accumulated E&P at the end of the prior year | [26 U.S.C. 535(c)(2)](https://uscode.house.gov/us/usc/t26/s535/) |
| Personal holding company tax rate | 20 percent | [26 U.S.C. 541](https://uscode.house.gov/us/usc/t26/s541/) |
| Failure to file: per month or part month, capped at 25% | 5 percent | [26 U.S.C. 6651(a)(1)](https://uscode.house.gov/us/usc/t26/s6651/) |
| Failure to pay: per month or part month, capped at 25% | 0.5 percent | [26 U.S.C. 6651(a)(2)](https://uscode.house.gov/us/usc/t26/s6651/) |
| Minimum failure-to-file penalty, return more than 60 days late, returns required to be filed in 2027 | lesser of USD 535 or 100% of the tax | [Rev. Proc. 2025-32, section 4.52](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Underpayment interest, 4th quarter 2026 (corporate and non-corporate) | 7% | [IRS quarterly interest rates](https://www.irs.gov/payments/quarterly-interest-rates) |
| Large corporate underpayment interest, 4th quarter 2026 | 9% | [IRS quarterly interest rates](https://www.irs.gov/payments/quarterly-interest-rates) |
| Form 1125-E required if total receipts (line 1a plus lines 4 to 10) are | USD 500,000 or more | [Instructions for Form 1120 (2025), line 12](https://www.irs.gov/pub/irs-pdf/i1120.pdf) |
| Schedule L, M-1 and M-2 not required if total receipts and total assets are both less than | USD 250,000 | [Instructions for Form 1120 (2025), Schedule K question 13](https://www.irs.gov/pub/irs-pdf/i1120.pdf) |
| Schedule M-3 instead of M-1 at year-end total assets of | USD 10 million or more | [Instructions for Form 1120 (2025), Schedule M-3](https://www.irs.gov/pub/irs-pdf/i1120.pdf) |
| Schedule UTP: total assets of (with audited statements and a reportable position) | USD 10 million or more | [Instructions for Form 1120 (2025), Schedule K question 14](https://www.irs.gov/pub/irs-pdf/i1120.pdf) |
| Form 8991 filing screen (not BEAT liability): group gross receipts in any of the 3 preceding years of at least | USD 500 million | [Instructions for Form 1120 (2025), Schedule K question 22](https://www.irs.gov/pub/irs-pdf/i1120.pdf) |
| E-file required if the corporation files, in the calendar year, returns of any type numbering | 10 or more | [Instructions for Form 1120 (2025), Electronic Filing](https://www.irs.gov/pub/irs-pdf/i1120.pdf) |
| Form 7004 automatic extension (tax years beginning in 2026, including June 30 year-ends) | 6 months | [Instructions for Form 7004 (Rev. December 2025)](https://www.irs.gov/pub/irs-pdf/i7004.pdf) |

Bonus depreciation is 100 percent for qualified property acquired and placed in service after 19 January 2025, and the section 179 limit for 2026 is set by Rev. Proc. 2025-32: both are owned by `us-section-179-and-bonus-depreciation`. The 2026 section 250 percentages for FDII and net CFC tested income are owned by `us-gilti-fdii-beat`. The statutory percentages above are not indexed; the USD 32,000,000, USD 535 and interest rates change each year or quarter.

### Step 1: who files, and for which period

1. Unless exempt under section 501, domestic corporations must file whether or not they have taxable income, including corporations in bankruptcy, unless required or electing to file a special return. Inactivity alone is no exemption. Dissolution generally requires a final return; do not assume dissolution is the sole possible change of federal filing status. [IRS instructions, Who Must File](https://www.irs.gov/pub/irs-pdf/i1120.pdf).
2. An eligible LLC electing association status files Form 8832 and attaches a copy to the return for the election year. Generally the election cannot take effect more than 75 days before filing or later than 12 months afterward. A classification-change election generally prevents another change by election for 60 months; the formation-date first election is excepted, and IRS-consent/late-election relief has separate conditions. Use the effective date for the first corporate period. [Form 8832 and instructions](https://www.irs.gov/pub/irs-pdf/f8832.pdf).
3. Identify the corporation’s established tax year and first/final/short period before computing tax. Calendar, fiscal and 52/53-week years, changes using Form 1128, and personal-service-corporation section 444/Form 8716/Form 8752 elections remain relevant original topics. **NON-USABLE HOLD:** this Guide does not determine eligibility for a non-calendar year, permission to change, or special short-year annualization. Check this point with one of our partner accountants.
4. **Form edition.** The form actually read is Form 1120 (2025). Its instructions cover calendar 2025 and fiscal years beginning in 2025, and expressly permit a short year beginning AND ending in 2026 if the 2026 form is unavailable when that return is required to be filed: show the 2026 period and apply 2026 law. That permission does not establish the edition for an ordinary calendar-2026 return. **NON-USABLE HOLD:** final 2026 form/line mapping and year-specific form thresholds must be checked against the applicable released edition before filing; do not treat the 2025 mapping as approval of a 2026 filing. Check this point with one of our partner accountants.

### Step 2: page 1, income (lines 1a to 11)

5. **Line 1a** gross receipts; **1b** returns and allowances; **1c** = 1a minus 1b.
6. **Line 2** cost of goods sold from Form 1125-A (attach whenever there is COGS). **Line 3** gross profit = 1c minus 2.
7. **Line 4** dividends and inclusions, gross, from Schedule C line 23. The dividends received deduction comes off later, on line 29b.
8. **Line 5** taxable interest. Tax-exempt interest is not here; it goes on Schedule K.
9. **Lines 6 and 7** gross rents and royalties.
10. **Line 8** capital gain net income from Schedule D (Form 1120). For an ordinary C corporation, capital losses offset capital gains: a net capital loss generally carries back 3 years and forward 5 years as short-term loss, earliest year first. A carryback cannot create or increase an NOL. Foreign-expropriation and RIC exceptions require separate treatment. Source: [26 U.S.C. 1212(a)](https://uscode.house.gov/us/usc/t26/s1212/).
11. **Line 9** Form 4797 Part II (ordinary gain and loss, section 1245 and 1250 recapture). Apply depreciation recapture and the section 1231(c) five-preceding-year non-recaptured ordinary-loss lookback before treating remaining net section 1231 gain as capital. A net section 1231 loss is ordinarily an ordinary loss.
12. **Line 10** other income with a statement (recoveries of amounts deducted earlier, refunds of taxes deducted, section 481(a) adjustments). **Line 11** total income = lines 3 to 10.

### Step 3: page 1, deductions (lines 12 to 27)

| Line | Item | What to check |
| --- | --- | --- |
| 12 | Compensation of officers | Form 1125-E if total receipts are USD 500,000 or more (name, SSN, % of time, % of stock, pay); pay must be reasonable (see Boundary table) |
| 13 | Salaries and wages | Less employment credits (for example the work opportunity credit) |
| 14 | Repairs and maintenance | Improvements are capitalized under section 263(a) and Reg. 1.263(a)-3 |
| 15 | Bad debts | Debts worthless wholly or partly during the year; cash-method amounts must previously have been included in income. Partial-worthlessness charge-off and small-bank section 585 reserve exceptions need their own conditions; no blanket reserve deduction |
| 16 | Rents | Allowable rents; related-party section 267 timing requires separate fact review |
| 17 | Taxes and licenses | State income tax, property tax, employer payroll tax, excise. Federal income tax is not deductible; exclude acquisition-related taxes, foreign taxes credited and amounts deducted elsewhere |
| 18 | Interest | After the section 163(j) limit (Step 5); Form 8990 if subject to it |
| 19 | Charitable contributions | After the 1 percent floor and 10 percent cap (Step 4) |
| 20 | Depreciation from Form 4562 | Not already in COGS; bonus and section 179 per `us-section-179-and-bonus-depreciation` |
| 21 | Depletion | Cost or percentage |
| 22 | Advertising | Includes website costs not capitalized |
| 23 | Pension, profit-sharing plans | Section 404 timing |
| 24 | Employee benefit programs | Health, group term life, dependent care not deducted elsewhere |
| 25 | Energy efficient commercial buildings deduction | Form 7205 (section 179D) |
| 26 | Other deductions, with a statement | Allowable insurance, utilities, professional fees and travel; ordinarily eligible non-entertainment business meals are 50%, subject to section 274 conditions/exceptions. For amounts paid or incurred after 2025, section 274(o) denies specified employer-convenience meals/facility costs except statutory exceptions; do not automatically apply 50%. Software, bank fees and research require the correct expense/capital classification |
| 27 | Total deductions | |

13. **Line 28** = line 11 minus line 27: taxable income before the NOL deduction and special deductions.

### Step 4: the 2026 charitable deduction (line 19)

14. Compute "taxable income" for the limit without the charitable deduction itself, without the special deductions of part VIII (the dividends received deduction, section 250; section 248 organizational costs stay in), without any NOL or capital loss carryback, and without section 199A(g). Source: [26 U.S.C. 170(b)(2)(D)](https://uscode.house.gov/us/usc/t26/s170/). If the corporation has an NOL carryover, the limit is applied to taxable income after the NOL deduction. Source: [Instructions for Form 1120 (2025), line 19](https://www.irs.gov/pub/irs-pdf/i1120.pdf).
15. For a taxable year beginning after 31 December 2025, the year's gifts are deductible only to the extent they exceed **1 percent** of that taxable income and do not exceed **10 percent** of it: deduction = the smaller of the gifts and 10% of taxable income, minus 1% of taxable income, not below zero. Source: [Public Law 119-21, section 70426(a)](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm), amending section 170(b)(2)(A).
16. **Carryforward.** For ordinary section 170(b)(2)(A) gifts, disallowed amounts above the cap carry to the five succeeding tax years in order, subject to each later year’s applicable limitation and current-year gifts first. Gifts lost under the 1 percent floor carry forward **only** in a year in which the 10 percent cap is also exceeded; in any other year they are lost for good. A carryover is cut to the extent it would increase an NOL carryover. Source: Public Law 119-21, section 70426(b), new section 170(d)(2)(A) to (D).
17. An accrual-method corporation can treat a gift paid by the original due date (not extensions) as paid in the tax year if the board authorized it during the year; attach a declaration with the date of the resolution. Source: [Instructions for Form 1120 (2025), line 19](https://www.irs.gov/pub/irs-pdf/i1120.pdf), section 170(a)(2)(B).
18. For ordinary 2025 corporate gifts the cap is 10% with no new floor; the 2026 floor must not be applied to the historical 2025 case. Verify section 170(c) recipient eligibility, value/property reductions and records before using the band. Cash gifts require a bank/written record, and gifts of USD 250 or more require timely contemporaneous written acknowledgment. Qualified farmer/rancher and Native Corporation conservation gifts have different statutory limits; enhanced/property gifts and Form 8283 requirements are **NON-USABLE HOLD** for an actual deduction here. Check this point with one of our partner accountants.

### Step 5: business interest (line 18, section 163(j))

19. **Exemption.** A corporation whose average annual gross receipts for the 3 prior tax years do not exceed USD 32,000,000 (2026, section 448(c)) is not subject to the limit and generally does not file Form 8990, unless it is a tax shelter. Apply section 448(c) aggregation, predecessor, short-year annualization and years-in-existence rules; do not test each entity in isolation. Source: [Rev. Proc. 2025-32](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf). Electing real property trades or businesses and electing farming businesses (section 163(j)(7)(B) and (C), irrevocable) are also out, but must use the alternative depreciation system for certain property; only utility trades meeting section 163(j)(7)(A)(iv)’s regulated-rate conditions are excluded.
20. **Limit.** Deductible business interest = business interest income + **30 percent** of adjusted taxable income (ATI not below zero for this component) + floor plan financing interest. Disallowed interest carries forward indefinitely (tracked on Form 8990). Source: [26 U.S.C. 163(j)(1)](https://uscode.house.gov/us/usc/t26/s163/).
21. **Adjusted taxable income (ATI)** starts from taxable income computed without business interest expense or income, the NOL deduction or the section 199A deduction, and adds back depreciation, amortization and depletion. The add-back was restored for taxable years beginning after 31 December 2024 (Public Law 119-21, section 70303). For taxable years beginning after 31 December 2025, ATI excludes section 951(a), 951A(a) and 78 inclusions, the section 245A(a) deduction by reason of section 964(e)(4), and the section 250(a)(1)(B) deduction,not every section 245A or section 250 deduction (section 70342). Nonbusiness items are also excluded under the statutory definition. The floor-plan expansion to qualifying trailers/campers designed as living quarters and towed or affixed to motor vehicles applies for years beginning after 2024 (section 70303). Source: [Public Law 119-21](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm).
22. **New for 2026, capitalized interest.** For taxable years beginning after 31 December 2025 the limit applies to business interest whether it would be deducted or capitalized (for example under section 263A), and the amount allowed is applied **first** to the interest that would be capitalized and only then to interest that would be deducted. Carried-forward interest is never treated as capitalizable. Interest capitalized under section 263(g) or 263A(f) is not business interest. Source: Public Law 119-21, section 70341, new section 163(j)(10) and amended 163(j)(5). Effect: a corporation with self-constructed assets or inventory carrying costs may find its line 18 deduction smaller than before, because the allowance is used up on the capitalized interest first.

### Step 6: research, depreciation and the other 2026 cost-recovery points

23. **Domestic research (section 174A).** Domestic research or experimental expenditures paid or incurred in taxable years beginning after December 31, 2024 are deducted in the year paid or incurred (line 26 with a statement). Alternatively the corporation can elect under section 174A(c) to capitalize them and amortize over not less than 60 months from the month benefits are first realized, only for eligible otherwise-capital expenditures not chargeable to depreciable/depletable property. Elect by the return deadline including extensions; the adopted method/period binds later years absent IRS consent, and does not reach earlier-year expenditures. Source: [Public Law 119-21, section 70302](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm); [Instructions for Form 1120 (2025), What's New](https://www.irs.gov/pub/irs-pdf/i1120.pdf). The activity must qualify as research or experimentation; a spending label alone does not prove deductible labor, materials or overhead. Software development is expressly included; land and research-property acquisition/improvement and mineral exploration are excluded, while eligible depreciation/depletion allowances may count. The earlier section 174 regulatory definition used an uncertainty test, included qualifying patent-development costs and excluded ordinary quality-control testing, efficiency/management/consumer surveys and advertising; testing design uncertainty differed from ordinary quality control. These historical definitions do not by themselves settle a current section 174A method or expense allocation. Actual disputed allocation/classification is a **NON-USABLE HOLD**. Check this point with one of our partner accountants.
24. **Foreign research** attributable to foreign research under section 41(d)(4)(F) remains capitalized and amortized over 15 years starting at the midpoint of the expenditure year. Section 174 exclusions and software rule apply. Disposition/retirement/abandonment does not accelerate the deduction or reduce amount realized; the amended foreign disposition rule applies after 12 May 2025, separately from section 174A’s expenditure-year commencement. [26 U.S.C. 174](https://uscode.house.gov/us/usc/t26/s174/).
25. **The 2022 to 2024 domestic balance.** Domestic research capitalized in taxable years beginning in 2022 to 2024 keeps amortizing unless the corporation elected (section 70302(f)(2)) to deduct the unamortized balance in its first taxable year beginning after 31 December 2024, or ratably over that year and the next. A calendar-year corporation that chose the two-year option deducts the second half on its 2026 return. Procedures: Rev. Proc. 2025-28 (named in the Form 1120 instructions). Small businesses meeting the section 448(c) test could instead apply section 174A back to 2022 by amended returns, using the section 448(c) test for the first year beginning after 2024 (not the 2026 USD 32 million amount), excluding prohibited tax shelters. The statute provides an election within one year after 4 July 2025; that ordinary window is past as of this read. Exact timely-filing holiday/procedural or late-relief eligibility is a **NON-USABLE HOLD**. Check this point with one of our partner accountants. For material research spend, load `us-r-and-d-section-174-and-41` alongside.
26. **Research credit coordination.** The section 174A deduction is reduced by the section 41 credit allowed unless the reduced-credit election under section 280C(c)(2) is made on the timely return including extensions using Form 6765. It is irrevocable for that year; the reduction covers otherwise deductible OR capitalized domestic expenditure.
27. **Depreciation.** 100% bonus depreciation requires qualified property acquired and placed in service after 19 January 2025. The historical earlier-acquisition cohort is not automatically eligible for this rate. Section 168(n) production-property qualification/election is a **NON-USABLE HOLD** in this Guide: it is not blanket immediate expensing of a building. Check this point with one of our partner accountants. Use `us-section-179-and-bonus-depreciation` for the amounts, the binding-contract rule and the section 179 limit. Report on Form 4562 and line 20.

### Step 7: NOL and special deductions (lines 29a to 30)

28. **Line 29a, NOL.** Losses from taxable years beginning after 2017 are carried forward without time limit and are not carried back (farming and insurance exceptions aside; the historical 2018–2020 five-year carryback provisions and any remaining procedural rights require a separate vintage-specific review). They offset at most **80 percent** of taxable income computed without the NOL, section 199A and section 250 deductions, after any pre-2018 NOLs are used. Pre-2018 NOLs had a 20-year carryforward and no 80% limit; a calendar-2017 loss’s twentieth succeeding calendar year is 2037 (a calendar-2005 loss’s is 2025). Fiscal-year counting must follow the actual loss year; these are not universal calendar deadlines. Source: [26 U.S.C. 172(a) and (b)](https://uscode.house.gov/us/usc/t26/s172/). After an ownership change of more than 50 percentage points in 3 years, section 382 limits the use of pre-change losses each year (equity value times the long-term tax-exempt rate, plus built-in gain adjustments): refer.
29. **Line 29b, special deductions** from Schedule C line 24: mainly the dividends received deduction (Step 8) and the section 250 deduction (Form 8993, Schedule C line 22).
30. **Line 30** taxable income = line 28 minus line 29c.

### Step 8: Schedule C, the dividends received deduction

31. Enter each dividend at gross in column (a) and the percentage in column (b): 50% for a less than 20% owned domestic payer (line 1), 65% for 20% or more owned (line 2), 100% for qualifying dividends from an affiliated group member (line 11, at least 80% by vote and value under section 1504(a), applying its stock exclusions and section 243(b) dividend/E&P membership conditions, no consolidated return; inside a consolidated return intercompany dividends are eliminated). Debt-financed stock (line 3) gets a reduced percentage under section 246A. Preferred stock of public utilities: 23.3% and 26.7% (lines 4 and 5). Foreign payers: lines 6 to 8 and 13 (the section 245A 100% deduction for the foreign-source portion of dividends from a specified 10%-owned foreign corporation). Subpart F inclusions (lines 16a to 16c) and GILTI (line 17) are inclusions, not dividends, and get no dividends received deduction except line 16a. Source: [Form 1120 (2025), Schedule C](https://www.irs.gov/pub/irs-pdf/f1120.pdf).
32. **Holding period.** No deduction for a dividend on stock held 45 days or less in the 91-day period beginning 45 days before the ex-dividend date (90 days in a 181-day period for certain preferred stock), with days of reduced risk (hedges, short positions) not counted. Source: [26 U.S.C. 246(c)](https://uscode.house.gov/us/usc/t26/s246/). A common audit point for portfolio holders.
33. **Taxable income limit (section 246(b)).** The 50% and 65% deductions are limited to 50% and 65% of taxable income computed without the section 172, 199A, 243(a)(1), 245(a)/(b) and 250 deductions, without section 1059 adjustments and without the relevant section 1212(a)(1) capital-loss carryback, unless the full-deduction NOL test actually produces an NOL; reducing taxable income to exactly zero does not itself create one. Apply the 65% class first, then the 50% class with its statutory reduction for dividends from 20%-owned payers. Use the worksheet for Schedule C lines 9 and 22 in the Form 1120 instructions. The 100% affiliated-group deduction is not limited.
34. Line 23 (total dividends and inclusions) goes to page 1 line 4; line 24 (total special deductions) goes to line 29b.

### Step 9: Schedule J, the tax

35. **Line 1a** = line 30 times 21%. Lines 1b to 1z add other chapter 1 taxes (section 1291 PFIC tax on line 1c, BEAT from Form 8991 on line 1f, and so on). **Line 3** is the corporate AMT from Form 4626 (applicable corporations only). **Lines 5a to 5f** are credits: foreign tax credit (Form 1118), general business credit (Form 3800), prior-year minimum tax credit (Form 8827). **Line 8** is the personal holding company tax (Schedule PH). **Line 12** total tax goes to page 1 line 31. Source: [Form 1120 (2025), Schedule J](https://www.irs.gov/pub/irs-pdf/f1120.pdf).
36. **Corporate AMT.** The domestic statutory status test generally requires average annual AFSI over USD 1 billion for the relevant three-year test period ending with a prior tax year ending after 2021; prior applicable status can persist. A foreign-parented multinational member must meet BOTH the group USD 1 billion test AND the member USD 100 million-or-more test, with the statutory aggregation, short-period, predecessor and years-in-existence rules. The status test disregards the financial-statement NOL deduction. For an applicable corporation, tentative minimum tax is 15% of adjusted AFSI after usable financial-statement NOLs, less CAMT foreign tax credit; CAMT is the excess over regular tax plus BEAT, not below zero. Section 53 credit is limited in later years, not an automatic refund. **Form 4626 normally determines status even if no CAMT is payable**: omit it only under an actual filing exclusion, including a properly chosen applicable simplified method; previous applicable status restricts that exception. [Sections 55/59](https://uscode.house.gov/us/usc/t26/s59/), [Form 4626 instructions](https://www.irs.gov/instructions/i4626). Actual status/adjustments/credit and simplified-method eligibility remain **NON-USABLE HOLD** here. Check this point with one of our partner accountants.
37. **Payments (Schedule J lines 13 to 23):** prior-year overpayment credited, 2026 estimated tax, any quick refund applied for on Form 4466, tax deposited with Form 7004, withholding, refundable credits. Page 1 line 34 is the estimated tax penalty (Form 2220); line 35 amount owed; line 36 overpayment; line 37 refund or credit to 2027 estimated tax.

### Step 10: estimated tax for 2026 (section 6655)

38. If the 2026 tax (regular tax plus CAMT and BEAT, less credits) is USD 500 or more, four installments are due on the 15th day of the 4th, 6th, 9th and 12th months of the tax year: for a calendar year **15 April, 15 June, 15 September and 15 December 2026** (all weekdays). Source: [26 U.S.C. 6655(c) and (f)](https://uscode.house.gov/us/usc/t26/s6655/).
39. Each installment is 25 percent of the required annual payment: the lesser of 100% of the 2026 tax and 100% of the tax shown on the 2025 return. The prior-year option is not available if 2025 was a short year or the 2025 return showed no liability (or was not filed). There is no 110% rule for corporations. Source: 26 U.S.C. 6655(d)(1).
40. **Large corporation** (taxable income of USD 1,000,000 or more in any of the 3 preceding tax years, including predecessors, without NOL/capital-loss carryovers or carrybacks and with the controlled-group allocation): it may use the prior-year tax only for the 1st installment, and any shortfall is added to the 2nd; installments 2 to 4 must be based on current-year tax. Source: 26 U.S.C. 6655(d)(2) and (g)(2).
41. **Annualized or seasonal method** (section 6655(e)) lowers installments for uneven income: the standard periods are the first 3, 3, 6 and 9 months (annualization factors 4, 4, 2 and 12/9), and other periods can be elected on Form 8842. Computed on Form 2220.
42. Reconcile installment timing and determine any section 6655 underpayment. Form 2220 is NOT universally required merely because an installment was short: the IRS generally figures and bills the penalty. The instructions require attachment for the annualized/adjusted seasonal method, a large corporation using prior-year tax for its first installment, and the stated 2025 CAMT-relief procedure. Notice 2025-27 relief concerns the 2025 CAMT portion, not all regular-tax underpayments. **NON-USABLE HOLD:** no conclusion here that CAMT penalty relief does or does not apply in 2026; establish the actual year’s relief and form instructions. Check this point with one of our partner accountants.
43. Pay all federal tax deposits electronically (EFTPS or IRS business payment options).

### How the result flows on

The year's after-tax earnings feed earnings and profits, which decide whether a later distribution is a taxable dividend to the shareholder. An ordinary shareholder dividend generally is not deductible to the corporation; reasonable owner pay for services can be. Statutory exceptions such as qualifying ESOP dividends require their own conditions and are not assumed in the comparison. Because the rate is flat, timing income into a lower band no longer helps; what is left is deferral (NOLs, accelerated deductions) and the choice between deductible pay and a nondeductible dividend. The decision between paying a dividend and keeping the money in the company is Worked case 1.

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Corporation had no income or activity | Inactivity alone does not remove the ordinary domestic filing duty; verify exemption or special-return status |
| Tax under USD 500 for the year | No estimated tax penalty (section 6655(f)) |
| Fiscal year ending 30 June, year beginning in 2025 (ends 30 June 2026) | Due 15th day of the 3rd month (15 September 2026); Form 7004 gives 7 months (to 15 April 2027) |
| Fiscal year ending 30 June, year beginning in 2026 (ends 30 June 2027) | Ordinary rule: 15th day of the 4th month (15 October 2027); Form 7004 gives 6 months |
| Short year ending in June | Apply the year-beginning transition: the pre-2026 June exception must not be applied to a year beginning in 2026 |
| Due date on a Saturday, Sunday or legal holiday | Next business day (section 7503) |
| Charitable gifts under 1 percent of taxable income in 2026 | No deduction, and no carryforward (the cap was not exceeded) |
| Charitable gifts over 10 percent | Deduction = 10% minus 1%; the excess over 10% and the floor amount both carry forward 5 years |
| Average gross receipts USD 32,000,000 or less | Apply the 2026 section 448(c) aggregation/annualization and tax-shelter conditions first; no automatic entity-by-entity exemption |
| Dividend on stock held 45 days or less around the ex-date | No dividends received deduction (section 246(c)) |
| Taxable income small relative to dividends | Section 246(b) caps the 50% / 65% deduction unless the full deduction creates or increases an NOL |
| Owner-employee pay well above market | Section 162(a)(1) allows reasonable compensation for services actually rendered. Actual reasonableness, constructive-dividend characterization and fact-specific case-law factors are a **NON-USABLE HOLD**. Check this point with one of our partner accountants. |
| Publicly held corporation / related-group remuneration | Section 162(m) generally limits covered-employee deductions to USD 1 million. For years beginning after 2025, section 162(m)(7) aggregates remuneration and allocates the limitation across the statutory controlled group; a private member can be affected. The separate additional-five-highest-paid rule begins after 2026. Covered-employee/group/transition analysis is a **NON-USABLE HOLD** for actual pay. Check this point with one of our partner accountants. |
| Change-in-control / excess parachute payments | Sections 280G and 4999 remain an original topic, including the historical 20% recipient-excise claim. **NON-USABLE HOLD:** no deduction or recipient-tax output without proving the transaction, exemptions and thresholds. Check this point with one of our partner accountants. |
| Retained earnings beyond the reasonable needs of the business | Accumulated earnings tax of 20 percent on accumulated taxable income (section 531); see Worked case 1 |
| Possible personal holding company | Section 541 imposes 20% on statutorily defined undistributed PHC income, not automatically on all passive income. The earlier five-or-fewer / over-half ownership screen alone is not a completed section 542 test. **NON-USABLE HOLD:** classification and Schedule PH computation. Check this point with one of our partner accountants. |
| LLC elects corporation status | Form 8832 describes a deemed contribution of the disregarded entity’s assets/liabilities for stock; for a partnership, deemed asset contribution followed by distribution of stock. Tax-free section 351 treatment, gain from liabilities/boot, basis, holding-period tacking and transferability of earlier owner/partnership losses are **NON-USABLE HOLD**, not automatic. Existing entity EIN versus a new entity/owner EIN must be distinguished. Check this point with one of our partner accountants. |
| Partnership conversion / Rev. Rul. 84-111 alternatives | Preserve the transaction-form and basis/gain issue; no automatic loss transfer or tax-free result. **NON-USABLE HOLD.** Check this point with one of our partner accountants. |
| Corporation files fewer than 10 returns of all types in the calendar year | Paper filing allowed; e-file still recommended |
| No tax due on a late return | No section 6651 filing penalty (nothing to apply the 5% to) |

### Further worked figures (2026 models; separate original 2025 cases below)

- **NOL at 80%.** A USD 1,000,000 post-2017 NOL carryforward and 2026 taxable income before the NOL of USD 800,000: the NOL deduction is the smaller of USD 1,000,000 and 80% x USD 800,000 = USD 640,000. Taxable income USD 160,000, tax USD 33,600, and USD 360,000 carries to 2027.
- **Section 163(j).** Taxable income computed without business interest expense and income is USD 4,950,000; depreciation of USD 1,500,000 is added back (the 2025 onward rule), so ATI is USD 6,450,000. Limit: 30% x USD 6,450,000 = USD 1,935,000 plus USD 50,000 of business interest income = USD 1,985,000. Interest expense of USD 1,800,000 is fully deductible; with USD 2,500,000 of interest, USD 515,000 carries forward. (No other ATI adjustments or capitalizable interest are assumed in this arithmetic model; the distinct original 2025 USD 5 million/USD 3 million case is preserved below.)
- **Dividends received deduction.** USD 100,000 from a 5% holding (50%) gives USD 50,000; USD 200,000 from a 30% holding (65%) gives USD 130,000; USD 500,000 from a 100% affiliated subsidiary (100%) gives USD 500,000; total USD 680,000 on Schedule C line 24, assuming all payer, affiliation, holding, risk and financing conditions and sufficient limitation base. The same original 2025 dividend inputs remain a 2025 model as well. If taxable income before the deduction were USD 50,000 and only the 50% dividend existed, section 246(b) would cap it at USD 25,000 unless the NOL exception applies.
- **Corporate AMT.** An applicable corporation with financial statement income of USD 1,100,000,000, a usable financial statement NOL of USD 200,000,000 (within the 80% limit) and regular taxable income of USD 300,000,000: tentative minimum tax 15% x USD 900,000,000 = USD 135,000,000; regular tax 21% x USD 300,000,000 = USD 63,000,000; CAMT USD 72,000,000, which becomes a minimum tax credit carryforward. This 2026 arithmetic model assumes no CAMT foreign credit, BEAT or other tax/credit adjustments. AFSI does not prove prior regular taxable income for the estimated-tax large-corporation test. Actual status, usable losses, credit and installments are **NON-USABLE HOLD**. Check this point with one of our partner accountants.

## Worked cases

**Case 1, a decision: pay a dividend or keep the earnings in the company?** A calendar-year C corporation has 2026 taxable income of USD 500,000. Its sole shareholder is single, already has taxable income above USD 545,500 (the 2026 top of the 15% band for qualified dividends, Rev. Proc. 2025-32) and modified AGI above the USD 200,000 net investment income tax threshold. Accumulated E&P at the end of 2025 is USD 1,200,000. The board has a documented plan to spend USD 300,000 on equipment in 2027.

**Conditional comparison, not a distribution recommendation.** The supplied MAGI being above USD 200,000 does not prove that the whole dividend bears NIIT: section 1411 taxes the lesser of net investment income and MAGI excess. The following preserves the original 23.8% maximum-rate model, conditional on qualified-dividend eligibility and a full NIIT base. Actual shareholder tax is a **NON-USABLE HOLD** until those facts are established. Check this point with one of our partner accountants.

Corporate tax: USD 500,000 x 21% = USD 105,000, leaving USD 395,000 after tax. If all of it is paid out as a qualified dividend, the shareholder pays 20% (section 1(h)(1)(D)) plus 3.8% (section 1411) = 23.8%, which is USD 94,010, and keeps USD 300,990. The combined federal rate is 39.802% (USD 199,010 of USD 500,000).

For a cash retention comparison with no shareholder distribution now, the model defers dividend tax. Accumulated earnings tax additionally requires section 532’s avoidance-purpose conditions and section 535’s adjustments; after-tax cash is not automatically accumulated taxable income. The accumulated earnings credit is the greater of the applicable reasonable-needs credit and the statutory minimum credit, not their sum. In these inputs the minimum is zero (USD 250,000 less USD 1,200,000 of prior E&P), so only the USD 300,000 tied to the documented plan is sheltered. If the IRS finds the other USD 95,000 retained beyond reasonable needs, the accumulated earnings tax is 20% x USD 95,000 = USD 19,000, on top of the dividend tax the shareholder still pays when the money comes out later. (This assumes no other section 535(b) adjustments to accumulated taxable income.)

The middle course: keep USD 300,000 for the plan and pay a USD 95,000 dividend in 2026. The dividends paid deduction removes the USD 95,000 from accumulated taxable income, so the accumulated earnings tax is zero; the shareholder pays USD 22,610 now. These are conditional outputs: the equipment plan must qualify as reasonable business needs, the dividends-paid deduction must be available and the other statutory adjustments must be established. Actual AET and any recommendation are a **NON-USABLE HOLD**. Check this point with one of our partner accountants. Keeping everything saves USD 22,610 of shareholder tax this year but risks USD 19,000 of company tax that never comes back; paying everything out costs USD 71,400 more shareholder tax now (USD 94,010 less USD 22,610) and gives up the deferral on money the company needs.

```oa-check
name: Dividend or retain at 21% (2026)
inputs:
  taxable_income: 500000
  shareholder_rate: 0.238
  documented_needs: 300000
  prior_ep: 1200000
steps:
  - corp_tax: taxable_income * 0.21
  - after_tax: taxable_income - corp_tax
  - pay_all_shareholder_tax: after_tax * shareholder_rate
  - pay_all_net: after_tax - pay_all_shareholder_tax
  - combined_rate: (corp_tax + pay_all_shareholder_tax) / taxable_income
  - min_credit: max(250000 - prior_ep, 0)
  - retain_all_aet: max(after_tax - max(documented_needs, min_credit), 0) * 0.20
  - split_dividend: after_tax - documented_needs
  - split_shareholder_tax: split_dividend * shareholder_rate
  - split_aet: max(after_tax - split_dividend - max(documented_needs, min_credit), 0) * 0.20
expected:
  corp_tax: 105000.00
  after_tax: 395000.00
  pay_all_shareholder_tax: 94010.00
  pay_all_net: 300990.00
  combined_rate: 0.39802
  min_credit: 0.00
  retain_all_aet: 19000.00
  split_dividend: 95000.00
  split_shareholder_tax: 22610.00
  split_aet: 0.00
```

**Case 2, the 2026 charitable floor and cap, a dividends received deduction and estimated tax.** A calendar-year corporation has 2026 taxable income of USD 1,200,000 computed without the charitable deduction and the dividends received deduction (section 170(b)(2)(D)). That includes a USD 40,000 dividend from a domestic company in which it owns 10%, held all year. It gave USD 150,000 to public charities in 2026. Its 2025 return showed tax of USD 180,000, and its taxable income was below USD 1,000,000 in each of 2023, 2024 and 2025.

The following model assumes ordinary eligible gifts with the required records, an eligible non-debt-financed dividend with no related-payment restriction, no other tax/credit adjustments and a filed 12-month 2025 return showing the stated liability. These are conditions for the outputs, not additional supplied taxpayer facts.

Charitable: the floor is 1% x USD 1,200,000 = USD 12,000 and the cap is 10% = USD 120,000. Deduction = USD 120,000 minus USD 12,000 = USD 108,000 on line 19. Because the 10% cap was exceeded, both the USD 30,000 above the cap and the USD 12,000 under the floor carry forward: USD 42,000 for up to 5 years. Line 28 = USD 1,092,000. Dividends received deduction: 50% x USD 40,000 = USD 20,000; the section 246(b) limit (50% x USD 1,092,000 = USD 546,000) does not bind. Line 30 = USD 1,072,000; tax = USD 225,120. Under the 2025 rule (10% cap, no floor) the deduction would have been USD 120,000: the floor costs USD 2,520 of tax this year, though here the USD 12,000 is carried forward rather than lost.

Estimated tax: the corporation was not a large corporation for 2026, so the required annual payment is the lesser of USD 225,120 and USD 180,000 = USD 180,000, or USD 45,000 per installment. Provided this is section 6655(g)(2) taxable income with the required group/predecessor and loss adjustments, its 2026 income makes it a large corporation for 2027: only the first 2027 installment may be based on the 2026 tax.

```oa-check
name: Charitable floor and cap, DRD and estimated tax (2026)
inputs:
  ti_for_charity: 1200000
  gifts: 150000
  dividend_10pct_owned: 40000
  prior_year_tax: 180000
steps:
  - floor: ti_for_charity * 0.01
  - cap: ti_for_charity * 0.10
  - charity_deduction: max(min(gifts, cap) - floor, 0)
  - carryforward: gifts - charity_deduction
  - line_28: ti_for_charity - charity_deduction
  - drd: min(dividend_10pct_owned * 0.50, line_28 * 0.50)
  - line_30: line_28 - drd
  - tax: line_30 * 0.21
  - cost_of_floor: (min(gifts, cap) - charity_deduction) * 0.21
  - required_annual_payment: min(tax, prior_year_tax)
  - installment: required_annual_payment / 4
expected:
  floor: 12000.00
  cap: 120000.00
  charity_deduction: 108000.00
  carryforward: 42000.00
  line_28: 1092000.00
  drd: 20000.00
  line_30: 1072000.00
  tax: 225120.00
  cost_of_floor: 2520.00
  required_annual_payment: 180000.00
  installment: 45000.00
```

## Original 2025 cases and historical destinations

**Historical filing periods.** Retain the original 31 December 2025 return due 15 April 2026 (ordinary 7004 extension to 15 October 2026), and 31 January 2026 fiscal return due 15 May 2026. For the original 30 June 2026 fiscal year beginning 1 July 2025, the correct due date is **15 September 2026**, with seven-month extension to 15 April 2027; the old 15 October 2026 original due date was wrong. The 30 June 2027 year beginning in 2026 uses the fourth-month rule, 15 October 2027, with six-month filing extension subject to holiday rules. Original calendar-2025 estimate dates remain 15 April, **16 June** (15 June was Sunday), 15 September and 15 December 2025.

**Earlier screens and mappings withdrawn.** Revenue below USD 500 million or AFSI around USD 700 million, or a foreign parent’s USD 1 billion revenue, never independently proves a CAMT exemption; use the statutory AFSI tests and actual filing exclusions. A foreign-incorporated entity’s Form 8832 election does not establish a usable domestic-1120 filing conclusion in this Guide. The old M-1 suggestion to subtract section 250 on line 8 was wrong: special deductions follow line 28 on line 29b; do not count federal income-tax expense twice. Earlier Schedule B question-number/ownership/like-kind-exchange assertions are not a usable substitute for the actual edition.

**Other original cost/foreign topics.** The enacted 2025 section 179 base limit USD 2.5 million and phase-out USD 4 million apply for property placed in service in tax years beginning after 2024, with later indexing handled by the depreciation companion. Old USD 1.25 million / USD 3.13 million pre-amendment figures are historical context, not current limits. Original research five-year domestic / fifteen-year foreign capitalization for 2022–24 and the later transition remain distinct. The earlier USD 50,000 research-spend triage trigger was workflow policy, not a statutory expense threshold. Section 250’s property-disposition exclusion applies to dispositions after **16 June 2025**, including the specified deemed dispositions; its interest/R&E expense exclusion applies to years beginning after **31 December 2025**, not the same disposition date. Actual international outcomes remain held.


These retain their original years and inputs, separately from the 2026 models. A conditional calculation is not an actual return conclusion.

### Historical A , Acme Widgets, Inc., Delaware only, calendar 2025

Original inputs: sales USD 4,200,000; COGS USD 2,300,000; shareholder-CEO compensation USD 400,000; other salaries USD 800,000; rent USD 120,000; depreciation USD 90,000; other operating expenses USD 180,000; state income-tax expense USD 35,000; book federal income-tax expense USD 130,000; interest income USD 5,000; charitable gifts USD 30,000; no dividends or foreign operations; year-end assets USD 1,200,000; estimates paid USD 130,000. Original prior-2024 tax assumption USD 115,000; book net income USD 120,000.

Gross profit USD 1,900,000; total income USD 1,905,000. Non-charity deductions USD 1,625,000; charitable base USD 280,000. The ordinary 2025 10% cap, without the new floor, gives line 19 USD 28,000 and USD 2,000 carryforward to 2026 subject to that year's rules. Total deductions USD 1,653,000; line 28/30 USD 252,000; 21% tax USD 52,920. Original provisional deductions USD 1,655,000 / income USD 250,000 are superseded by the gift correction. M-1: USD 120,000 + USD 130,000 + USD 2,000 = USD 252,000; no additional meal adjustment was supplied.

Ordinary annual-payment model: min(USD 115,000, USD 52,920) = USD 52,920; quarterly USD 13,230. Payments USD 130,000 less tax USD 52,920 = USD 77,080 overpayment before penalties/other credits. This does not prove timely installments. No supplied prior-three-year income facts establish large-corporation status; the lower current-year-tax calculation needs no invented prior income.

The 2025 edition requires J/K and L/M-1/M-2 on these facts, plus Forms 1125-A, 1125-E and 4562. Assets USD 1.2 million do not require M-3/UTP; original unconditional Schedule B “yes” was wrong. No controlled-group facts or dividends were supplied. Calendar-2025 due date was 15 April 2026. The original assertion of more than 10 W-2/1099 returns was unsupported by the inputs. **NON-USABLE HOLD:** actual e-file return count/exemption, expense eligibility, reasonable CEO compensation and timing penalty. Check this point with one of our partner accountants.

### Historical B , GlobalTech Inc. / GlobalTech Ireland Ltd., calendar 2025

Original inputs: Delaware C corporation; 100% Irish CFC ownership; US revenue USD 80 million, including USD 30 million described as foreign-derived deduction-eligible income; pre-section-250 taxable income USD 20,000,000; CFC tested income USD 5,000,000; QBAI USD 8,000,000 and its 10% return USD 800,000; supplied net GILTI USD 4,200,000; section 78 gross-up USD 500,000; supplied FDII after allocation USD 4,000,000; foreign credits assumed usable after the historical 80% deemed-paid-credit restriction and sourcing.

2025 rate model ONLY, conditional on the USD 20 million including all required inclusions, the supplied bases being valid and the income-component limit not binding: 50% × (USD 4,200,000 + USD 500,000) = USD 2,350,000; 37.5% × USD 4,000,000 = USD 1,500,000. Total deduction USD 3,850,000; taxable income USD 16,150,000; 21% tax USD 3,391,500 before FTC. Earlier USD 3,600,000 deduction / USD 16,400,000 income / USD 3,444,000 tax omitted the eligible gross-up from the deduction. Section 250(a)(2) limits income components before percentages, not merely the resulting deduction.

The 2025 form maps GILTI to Schedule C line 17 and gross-up to line 18, not the old example's lines 14/16. Forms 5471/8992/8993/1118 are relevant screens, not completed filings. Revenue does not prove the USD 10 million asset conditions for M-3/UTP. **NON-USABLE HOLD:** actual GILTI/QBAI/net-interest calculation, foreign-derived qualification, gross-up, FTC amount/limitation and information-return duties. Check this point with one of our partner accountants.

Preserve the original isolated 2026 comparison: if a supplied USD 4.2 million inclusion base alone were unchanged, 40% is USD 1,680,000 instead of 50% × USD 4.2 million = USD 2,100,000; the USD 420,000 deduction difference times 21% is USD 88,200. This is a rate-only comparison, not this company's tax change: post-2025 net CFC tested income removes the old QBAI reduction, related gross-up matters, and the foreign-derived deduction is 33.34%. The former scheduled post-2025 37.5%/21.875% sunset is superseded.

### Historical C , MegaCorp, Inc., Delaware, calendar 2025

Original inputs: average AFSI for 2022/2023/2024 USD 1,200,000,000; 2025 AFSI before FSNOL USD 1,100,000,000; available FSNOL USD 200,000,000; regular taxable income USD 300,000,000; BEAT assumed zero. The original described regular income as reduced by depreciation, research amortization and FDII, without supplying additional deduction amounts.

Conditional arithmetic: 80% × USD 1.1 billion = USD 880 million, so a legally usable USD 200 million FSNOL fits; adjusted AFSI USD 900 million. Assuming no CAMT foreign credit, TMT USD 135 million; regular tax USD 63 million; additional CAMT USD 72 million; total USD 135 million. Ratios: 45% of regular taxable income and 15% of adjusted AFSI. USD 72 million enters section 53's credit mechanism, subject to future limits, not an automatic refund.

The original USD 33,750,000 quarter is USD 135 million / 4 BEFORE relief or alternative installment rules. The 2025 instructions provide Notice 2025-27 CAMT penalty relief and a Form 2220 procedure; the unrelieved figure is not an established actual 2025 installment. AFSI does not establish prior taxable income over USD 1 million. No supplied assets, audited-position facts, foreign-return facts or combined return count establish M-3, UTP, Forms 5471/5472/8990/8991/8993/8975 or mandatory e-file merely because the corporation is economically large. **NON-USABLE HOLD:** actual CAMT status/adjustments, FSNOL, credit, estimates/relief and those filing duties. Check this point with one of our partner accountants.

### Historical NOL, interest and dividend models

- **2024 loss / 2025 use:** original 2024 NOL USD 1,000,000 and 2025 pre-NOL taxable income USD 800,000. With the ordinary post-2017 limit and no other adjustments, deduction USD 640,000; income USD 160,000; tax USD 33,600; balance USD 360,000 to **2026**. Separate from current 2026 use / 2027 balance.
- **2025 interest:** original income **before the interest-expense deduction** USD 5,000,000 (including USD 50,000 interest income), depreciation already deducted USD 1,500,000, interest expense USD 1,800,000 and floor-plan interest USD 0. Correct ATI: USD 5,000,000 − USD 50,000 + USD 1,500,000 = USD 6,450,000; limit USD 1,985,000; USD 1.8 million fits. The original alternative expense **USD 3,000,000** gives USD **1,015,000** disallowed, holding the stated pre-interest income fixed. Old USD 8,300,000 ATI / USD 2,540,000 limit / USD 460,000 carryforward double-counted interest and are withdrawn. Do not substitute current 2026 USD 4,950,000 base / USD 2,500,000 alternative.
- **2025 DRD:** original USD 100,000/5%, USD 200,000/30% and USD 500,000/100%-affiliate dividends give conditional USD 50,000 + USD 130,000 + USD 500,000 = USD 680,000, as in the current illustration, subject to full eligibility and limitation-base facts. The separate 50%-class USD 50,000 taxable-income variant caps the deduction at USD 25,000: a full USD 50,000 deduction leaves zero, not an NOL. The original mixed-class variant supplies taxable income before DRD of USD 260,000 and provisional caps 50% × USD 260,000 = USD 130,000 and 65% × USD 260,000 = USD 169,000. Those independent cap tests omit class ordering and the NOL test: with all the stated dividends eligible, the full USD 680,000 deduction against USD 260,000 produces a USD 420,000 NOL, so section 246(b)(2) removes its cap. Verify that the supplied base is the statutory worksheet base; do not treat the two provisional caps as the worksheet.

### Where every earlier topic goes

| Earlier topic | Destination or explicit hold |
| --- | --- |
| Entity/status, inactivity, special returns, consolidated/PSC and controlled groups | Scope, Step 1, boundary/referral tables; actual special-status returns held |
| Year selection, 52/53-week, first/final/short periods, 8832, 1128, 8716/8752, EIN, conversion basis/gain/losses | Step 1 and boundary table; eligibility/transaction consequences held, no automatic 351 result |
| Rate; all page-1 income/COGS/capital/1231/recapture; deductions and officer pay | Steps 2–3 and 7–9; specialist deduction eligibility held where indicated |
| Charity, ordinary 2025 cap / 2026 floor, records and special property | Step 4; historical A; special-property amount held |
| DRD classes, affiliation, holding/risk, debt financing and foreign dividends; original example | Step 8 and historical models; special foreign/debt-financed outcomes held |
| NOL vintages, historical 2005/2017 expiry years, 2018–2020 carryback; 382 and old approximate 4% rate | Step 7 and historical NOL; actual 382 rate/value/built-in gain/5%-shareholder classification held, approximate 4% not usable |
| Interest; original 2024 USD 30m / 2025 USD 31m / 2026 USD 32m thresholds; 2022–24 EBIT and restored add-back | Step 5 / historical interest; historical USD 30m (2024) and USD 31m (2025) use their own tax-year tests and the same operative aggregation/tax-shelter gates; no backward substitution of USD 32m |
| Research/software/foreign costs, 2022–24 balances, retroactivity, credit; depreciation/179/production property | Step 6 / companion Guides; separate commencement/elections, actual special-property output held |
| GILTI/FDII/QBAI, DEI disposition restriction, PTEP credit denial, BEAT versus 8991 filing | Historical B / international referral / companion; 40%/33.34% not backward-applied, actual foreign computation held |
| CAMT/FSNOL/minimum credit, 2025 relief / 2026 uncertainty | Steps 9–10 / historical C / separate current 2026 model |
| Estimates, USD 500, large-corporation USD 1m, annualized/seasonal/8842 and payment timing | Step 10 / current cases / historical A and C |
| Schedules B/C/J/K/L/M-1/M-2/M-3/O/UTP and attached forms; book/tax | Filing section / historical A–C; actual special schedules need edition and facts |
| Reasonable pay, 162(m), 280G/4999, PHC, accumulated earnings/dividends | Boundary table / current Case 1; factual outputs held |
| Deadlines/7004/June transition, e-file/signatures, penalties/cause/interest and 6699 | Filing section; old assets-alone e-file rule and individual installment-agreement reduction withdrawn |
| QSBS issuer versus shareholder | Companion us-section-1202-qsbs: original USD 50m/75m issuer-asset boundaries, USD 10m/15m shareholder dollar limbs and 3/4/5-year 50%/75%/100% regime depend on acquisition-date/tacking versus issuance-date asset gates. **NON-USABLE HOLD** for an actual exclusion here. Check this point with one of our partner accountants. |
| States/decoupling, buyback 7208, country-by-country 8975, health-insurer special compensation and other special cases | Explicit non-usable holds below; no assumed USD 850m group classification, quarterly buyback filing rule, state conformity or special compensation result |
| Original provenance / historical professional attribution | Original Git ancestry, authors and AuthorDates retained; removed historical approval/person fields are not restored to current public metadata |

**Specialist holds.** Every referral below is a **NON-USABLE HOLD** for its actual classification, amount, election or filing. This includes consolidated/SRLY/intercompany rules, PSC year elections, special-return status, ownership-change section 382 (including the historical approximate 4% and built-in-gain/5-year claims), debt-financed/foreign DRD, PHC, public buybacks, country-by-country reporting, health-insurer compensation and state decoupling. No old unsupported figure is a usable fallback. Check this point with one of our partner accountants.

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-1120-CONSOL | Member of an affiliated group filing a consolidated return (sections 1501 to 1504, Reg. 1.1502, Forms 851 and 1122) | Refer: SRLY limits, intercompany transactions (Reg. 1.1502-13), excess loss accounts, consolidated section 163(j) and CAMT are outside this skill. If no consolidated election, each member files its own Form 1120 under this skill |
| R-1120-PSC | Personal service corporation (calendar year under section 441(i) unless a section 444 election, Forms 8716 and 8752) | Refer for review |
| R-1120-PHC | Possible personal holding company (Schedule PH) | Refer |
| R-1120-SPECIAL | REIT, RIC, cooperative, insurance company, FSC, REMIC, tax-exempt organization, foreign corporation | Wrong form: 1120-REIT, 1120-RIC, 1120-C, 1120-L, 1120-PC, 1120-FSC, 1066, 990-T or 1120-F |
| R-1120-CAMT | Possible applicable corporation under section 59(k) | Refer the Form 4626 computation (proposed regulations REG-112129-23 run to several hundred pages) |
| R-1120-INTL | CFCs, net CFC tested income/FDDEI, BEAT, Form 1118 and Form 8975. Section 960(d)(4) denies 10% of specified foreign taxes on section 951A-related PTEP; the amendment keys to the statutory inclusion-after-28-June-2025 wording, not a blanket distribution-date test | Use `us-gilti-fdii-beat`, `us-form-5471-cfc-information`; refer Form 1118 and Form 8975 |
| R-1120-382 | Ownership change of more than 50 percentage points in 3 years with NOLs or built-in gains | Refer: section 382 limitation |
| R-1120-BUYBACK | Public company stock repurchases (section 4501, Form 7208) | Refer: separate excise tax return, not part of Form 1120 |
| R-1120-UTP | Schedule UTP positions to rank and describe | Prepare the schedule only with the tax provision team; this skill flags the duty |
| R-1120-STATE | State corporate tax | The state's skill |

## Filing and payment

| Item | Calendar year 2026 |
| --- | --- |
| Return due | 15 April 2027 (15th day of the 4th month after year-end, 26 U.S.C. 6072(a)) |
| Extended due date with Form 7004 | 15 October 2027 |
| Tax due | 15 April 2027, with or without an extension |
| Estimated tax installments | 15 April, 15 June, 15 September, 15 December 2026 |

- **Due date.** The 15th day of the 4th month after the end of the tax year, including for a short-period return and for a dissolved corporation (after the date it dissolved); a June 30 fiscal year beginning before 2026 uses the 3rd month. Sources: [26 U.S.C. 6072(a)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap61-subchapA-partV-sec6072.htm); [Instructions for Form 1120 (2025), When To File](https://www.irs.gov/pub/irs-pdf/i1120.pdf).
- **Form 7004.** File by the original due date with a proper estimate of the tax, and pay the balance. The extension is automatic (6 months; 7 months for a June 30 year beginning before 2026); the IRS no longer confirms approval and writes only if it disallows the request. It extends filing only: late-payment penalty and interest run from the original due date on any unpaid tax. Source: [Instructions for Form 7004 (Rev. December 2025)](https://www.irs.gov/pub/irs-pdf/i7004.pdf). Mailing rules: `us-corporate-extension-form-7004-and-the`.
- **E-file.** Required if the corporation files 10 or more returns of any type in the calendar year (income, employment, excise and information returns, counted together), with a waiver procedure. Source: [Instructions for Form 1120 (2025), Electronic Filing](https://www.irs.gov/pub/irs-pdf/i1120.pdf); Reg. 301.6011-5. Filing goes through Modernized e-File and an authorized provider. For the officer-PIN/ERO route, use Form 8879-CORP and the ERO retains it before transmission; an officer not using it uses Form 8453-CORP under those instructions. Do not present 8879-CORP as the only route. [Official authorization instructions](https://www.irs.gov/pub/irs-pdf/f8879crp.pdf).
- **Penalties.** Late filing: 5% of the unpaid tax for each month or part month, to 25%. Late payment: 0.5% a month, to 25% (the reduced rate during an installment agreement is for individuals only). In a month when both apply, the filing penalty is reduced by the payment penalty, so the ordinary percentage-rate combined cap, apart from minimum-penalty and other special rules, is 47.5% (22.5% plus 25%). A return more than 60 days late that is required to be filed in 2027 carries a minimum filing penalty of the lesser of USD 535 or the tax due. Relief requires reasonable cause AND absence of willful neglect; an adviser’s involvement or a hardship label alone proves neither. The Form 7004 instructions also describe a late-payment-penalty exception where at least 90% is timely paid and the balance is paid by the extended deadline; interest still runs. Sources: [26 U.S.C. 6651](https://uscode.house.gov/us/usc/t26/s6651/); [Rev. Proc. 2025-32, section 4.52](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf). The S-corporation per-shareholder section 6699 penalty is not the C-corporation tax-based section 6651 penalty; partnership penalties are a separate subject. Ordinary nonfraudulent rates here do not cover fraud or the section 6651(d) post-levy-notice increase.
- **Interest** runs from the original due date at the applicable quarterly rate (Q4 2026: 7%, or 9% for a section 6621(c) large corporate underpayment after its applicable notice date). That test requires a C-corporation tax-period underpayment over USD 100,000 and statutory notice/payment conditions; it is distinct from section 6655’s USD 1 million income test. Q4 rates do not establish 2027 rates. Source: [IRS quarterly interest rates](https://www.irs.gov/payments/quarterly-interest-rates).

**Schedules and forms to attach.**

| Schedule or form | When |
| --- | --- |
| Schedule C | Any dividends, inclusions or special deductions |
| Schedule J, Schedule K | Every return |
| Schedule L, M-1, M-2 | Unless total receipts and total assets are both under USD 250,000 (Schedule K question 13); Schedule L must tie to the books |
| Schedule M-3 (instead of M-1) | Total assets USD 10 million or more at year-end; under USD 50 million it may complete Part I only plus Schedule M-1 |
| Schedule B (Form 1120) | Generally required M-3 filers; exemption for required filers with assets under USD 50 million and voluntary M-3 filers per the June-2025 M-3 instructions |
| Schedule UTP | Total assets USD 10 million or more, audited financial statements, and a reportable position |
| Schedule O | Member of a controlled group (apportionment of the accumulated earnings credit and other items) |
| Schedule D, Form 4797 | Capital gains and losses; business property sales |
| Form 1125-A | Any cost of goods sold |
| Form 1125-E | Total receipts USD 500,000 or more |
| Form 4562 | Depreciation, section 179, amortization (including capitalized research, section 195 and section 197) |
| Form 8990 | Subject to section 163(j) |
| Form 8993 | Any section 250 deduction |
| Form 4626 | Determines applicable status and computes CAMT unless an actual filing exclusion applies; see Step 9 |
| Form 8991 | Gross receipts of at least USD 500 million in any of the 3 preceding years |
| Form 2220 | Annualized/adjusted seasonal method, large corporation using prior tax for first installment, or applicable year-specific CAMT procedure; not every short installment |
| Form 3800, Form 6765, Form 1118 | Business credits, research credit, foreign tax credit |
| Form 5471, Form 5472 | Screen CFC shareholder / 25% foreign-owned corporation facts; actual filing categories, reportable transactions and exceptions are **NON-USABLE HOLD**. Check this point with one of our partner accountants. |
| Form 8832 copy | Year an LLC's corporate election takes effect |
| Form 1128 | Change of tax year |
| Form 7205 | Section 179D deduction |

Under the identified 2025 mapping, Schedule M-1 reconciles net income per books to line 28: add federal income tax expense, excess capital losses, income taxed but not booked and expenses booked but not deducted (the actually nondeductible portion of meals, fines, political/lobbying costs, club dues, section 162(m) excess and charitable amounts; apply each item’s exceptions before adding back); subtract income booked but not taxed (tax-exempt interest, qualifying tax-exempt life insurance proceeds) and deductions not booked (tax depreciation above book, bonus depreciation). Schedule K also asks about foreign ownership of 25% or more (Form 5472), section 163(j) status, BEAT, section 267A hybrid payments and CAMT status.

## Completion checklist

- Correct actual form edition/period established; the unverified final 2026 mapping is a non-usable filing hold.
- Prior three years' taxable income and gross receipts on file (large corporation and USD 32,000,000 tests).
- Charitable deduction after the 1 percent floor and 10 percent cap; carryforward schedule updated, and floor amounts kept only where the cap was exceeded.
- Section 163(j): exempt, or Form 8990 with ATI excluding CFC inclusions and the capitalized interest ordering applied.
- Domestic research deducted under section 174A (or the 174A(c) election documented); foreign research amortized over 15 years; any 2022 to 2024 balance handled per the election made.
- NOL deduction no more than 80% of taxable income for post-2017 losses; section 382 flagged if ownership changed.
- Every dividend tested for holding period, debt financing and the section 246(b) limit.
- CAMT status documented (applicable corporation or not).
- Estimates reconciled; Form 2220 attachment tested under its actual triggers, not simply a short installment.
- Retained earnings reviewed against documented business needs (accumulated earnings tax).
- Form 7004 filed and tax paid by 15 April 2027 if the return will be late.

## Sources

| Official authority | URL | Read date / applicable reused read |
| --- | --- | --- |
| U.S. Code section 11 | https://uscode.house.gov/us/usc/t26/s11/ | 2026-11-26 |
| Official IRS authority | https://www.irs.gov/pub/irs-pdf/i1120.pdf | 2026-11-28 |
| Official IRS authority | https://www.irs.gov/pub/irs-pdf/f8832.pdf | 2026-11-28 |
| Official IRS authority | https://www.irs.gov/businesses/small-businesses-self-employed/do-you-need-a-new-ein | 2026-11-28 |
| Official IRS authority | https://www.irs.gov/pub/irs-pdf/f1120.pdf | 2026-11-28 |
| U.S. Code section 1212 | https://uscode.house.gov/us/usc/t26/s1212/ | 2026-11-28 |
| U.S. Code section 1231 | https://uscode.house.gov/us/usc/t26/s1231/ | 2026-11-28 |
| U.S. Code section 162 | https://uscode.house.gov/us/usc/t26/s162/ | 2026-11-28 |
| U.S. Code section 274 | https://uscode.house.gov/us/usc/t26/s274/ | 2026-11-28 |
| Enacted public law | https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm | 2026-11-26; 2026-11-27; 2026-11-28 |
| U.S. Code section 170 | https://uscode.house.gov/us/usc/t26/s170/ | 2026-11-28 |
| Official IRS authority | https://www.irs.gov/pub/irs-drop/rp-25-32.pdf | 2026-11-27; 2026-11-28 |
| U.S. Code section 448 | https://uscode.house.gov/us/usc/t26/s448/ | 2026-11-28 |
| U.S. Code section 163 | https://uscode.house.gov/us/usc/t26/s163/ | 2026-11-28 |
| Official IRS authority | https://www.irs.gov/irb/2023-48_IRB | 2026-11-28 |
| Official U.S. publication | https://www.govinfo.gov/content/pkg/CFR-2025-title26-vol4/pdf/CFR-2025-title26-vol4-sec1-174-2.pdf | 2026-11-28 |
| U.S. Code section 174 | https://uscode.house.gov/us/usc/t26/s174/ | 2026-11-28 |
| U.S. Code section 280C | https://uscode.house.gov/us/usc/t26/s280C/ | 2026-11-28 |
| Official IRS authority | https://www.irs.gov/publications/p946 | 2026-11-27 |
| U.S. Code section 172 | https://uscode.house.gov/us/usc/t26/s172/ | 2026-11-28 |
| U.S. Code section 243 | https://uscode.house.gov/us/usc/t26/s243/ | 2026-11-28 |
| U.S. Code section 1504 | https://uscode.house.gov/us/usc/t26/s1504/ | 2026-11-28 |
| U.S. Code section 246 | https://uscode.house.gov/us/usc/t26/s246/ | 2026-11-28 |
| U.S. Code section 59 | https://uscode.house.gov/us/usc/t26/s59/ | 2026-11-28 |
| Official IRS authority | https://www.irs.gov/instructions/i4626 | 2026-11-28 |
| U.S. Code section 55 | https://uscode.house.gov/us/usc/t26/s55/ | 2026-11-28 |
| U.S. Code section 56A | https://uscode.house.gov/us/usc/t26/s56A/ | 2026-11-28 |
| U.S. Code section 53 | https://uscode.house.gov/us/usc/t26/s53/ | 2026-11-28 |
| U.S. Code section 59A | https://uscode.house.gov/us/usc/t26/s59A/ | 2026-11-26 |
| Official IRS authority | https://www.irs.gov/instructions/i8991 | 2026-11-26 |
| U.S. Code section 6655 | https://uscode.house.gov/us/usc/t26/s6655/ | 2026-11-28 |
| U.S. Code section 531 | https://uscode.house.gov/us/usc/t26/s531/ | 2026-11-28 |
| U.S. Code section 532 | https://uscode.house.gov/us/usc/t26/s532/ | 2026-11-28 |
| U.S. Code section 535 | https://uscode.house.gov/us/usc/t26/s535/ | 2026-11-28 |
| U.S. Code section 541 | https://uscode.house.gov/us/usc/t26/s541/ | 2026-11-28 |
| Official U.S. publication | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap2A-sec1411.htm | 2026-11-28 |
| Official U.S. publication | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partI-sec1.htm | 2026-11-28 |
| Official U.S. publication | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVIII-sec250.htm | 2026-11-28 |
| Official U.S. publication | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partIII-subpartF-sec951A.htm | 2026-11-26 |
| U.S. Code section 250 | https://uscode.house.gov/us/usc/t26/s250/ | 2026-11-26 |
| Official IRS authority | https://www.irs.gov/instructions/i1120sm3 | 2026-11-28 |
| Official U.S. publication | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap61-subchapA-partV-sec6072.htm | 2026-11-28 |
| Official U.S. publication | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap62-subchapA-sec6151.htm | 2026-11-28 |
| Official IRS authority | https://www.irs.gov/pub/irs-pdf/i7004.pdf | 2026-11-28 |
| Enacted public law | https://www.govinfo.gov/content/pkg/PLAW-114publ41/html/PLAW-114publ41.htm | 2026-11-28 |
| Official IRS authority | https://www.irs.gov/pub/irs-pdf/f8879crp.pdf | 2026-11-28 |
| U.S. Code section 6651 | https://uscode.house.gov/us/usc/t26/s6651/ | 2026-11-28 |
| Official IRS authority | https://www.irs.gov/payments/quarterly-interest-rates | 2026-11-28 |
| U.S. Code section 6621 | https://uscode.house.gov/us/usc/t26/s6621/ | 2026-11-28 |
| U.S. Code section 960 | https://uscode.house.gov/us/usc/t26/s960/ | 2026-11-26 |
| U.S. Code section 1202 | https://uscode.house.gov/us/usc/t26/s1202/ | 2026-11-28 |
| Official U.S. publication | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapP-partI-sec1202.htm | 2026-11-28 |
| Official IRS research-method procedure | https://www.irs.gov/pub/irs-drop/rp-25-28.pdf | 2026-11-28 |
| U.S. Code section 6699 | https://uscode.house.gov/us/usc/t26/s6699/ | 2026-11-28 |
| U.S. Code section 1211 | https://uscode.house.gov/us/usc/t26/s1211/ | 2026-11-28 |
| U.S. Code section 168, electing-business ADS dependency | https://uscode.house.gov/us/usc/t26/s168/ | 2026-11-28 |
| IRS ordinary shareholder-dividend treatment | https://www.irs.gov/businesses/small-businesses-self-employed/forming-a-corporation | 2026-11-28 |

Not yet confirmed: The final 2026 form mapping, actual 2026 CAMT penalty relief and 2027 quarterly interest rates are not established here. Explicit non-usable holds preserve the specialist and fact-dependent topics. Check this point with one of our partner accountants.
