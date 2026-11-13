---
name: us-form-1120-c-corp
description: Prepare the 2026 Form 1120 for a US domestic C corporation, federal only. Covers the flat 21% rate under 26 U.S.C. 11(b), the income and deduction lines, the dividends received deduction (50%, 65%, 100%), the One Big Beautiful Bill Act changes that start in 2026 (the 1 percent floor and 10 percent cap on corporate charitable gifts, the interest capitalization ordering rule and the CFC inclusion carve-out from adjusted taxable income under section 163(j)), domestic research expensing under section 174A, 100% bonus depreciation (linked), the 80% NOL limit, estimated tax under section 6655 with the large corporation rule, the corporate AMT pointer, the accumulated earnings tax and the dividend or retain decision, schedules and attached forms, Form 7004, e-file and penalties. Calendar-year 2026 returns are due 15 April 2027. Trigger on "Form 1120", "C corp return", "corporate tax return", "21% corporate rate", "dividends received deduction", "corporate estimated tax", "Form 7004 corporation", "retain earnings or pay a dividend".
version: "2.0"
jurisdiction: US
tax_year: 2026
last_updated: 2026-11-13
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: corporate-tax
type: computation
---

# US Form 1120, C corporation income tax return, tax year 2026

> **Source-cited draft.** Built from the 2025 Form 1120 and its instructions (the 2026 editions are not yet published), the Instructions for Form 7004 (Rev. December 2025), Rev. Proc. 2025-32, the IRS quarterly interest rates page, Public Law 119-21 (the One Big Beautiful Bill Act) and 26 U.S.C. 1, 11, 55, 59, 163, 170, 172, 243, 246, 531, 535, 541, 1212, 1411, 6072, 6651 and 6655, read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** For a tax year beginning in 2026, a C corporation pays a flat **21%** on taxable income (Form 1120 line 30). There is no small-company band and no exempt first slice: USD 1,000 of taxable income means USD 210 of tax. A calendar-year 2026 return is due **15 April 2027**; Form 7004 extends filing (not payment) by 6 months to 15 October 2027. Estimated tax is due in four 25% installments on 15 April, 15 June, 15 September and 15 December 2026 if the year's tax is USD 500 or more. New for 2026: charitable gifts are deductible only above **1 percent** and up to **10 percent** of taxable income; the section 163(j) interest limit is applied before interest is capitalized, and CFC inclusions leave adjusted taxable income. Domestic research is deducted in full under section 174A, and 100% bonus depreciation is permanent for property acquired after 19 January 2025.

## Scope and who this is for

In scope: one domestic C corporation filing its own Form 1120 for a tax year beginning in 2026 (calendar year 2026, or a fiscal year beginning in 2026). That includes a corporation chartered under state or DC law with no S election, an LLC that elected to be taxed as a corporation on Form 8832, and an inactive corporation that still exists under state law. The skill covers the page 1 computation, Schedule C (dividends and special deductions), Schedule J (tax), the corporate-specific limits (section 163(j), the NOL rule, the charitable floor and cap, the dividends received deduction), estimated tax, the due date and extension, and the penalties.

Out of scope, and where it goes:

| Topic | Skill or action |
| --- | --- |
| Section 179 and bonus depreciation figures and rules | `us-section-179-and-bonus-depreciation` |
| Research credit (Form 6765) and section 174 / 174A mechanics in detail | `us-r-and-d-section-174-and-41` |
| GILTI (net CFC tested income), FDII and BEAT computations, including the 2026 section 250 percentages | `us-gilti-fdii-beat`, `us-cfc-gilti` |
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
| Corporate income tax rate (section 11(b)) | 21% | [26 U.S.C. 11(b)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partII-sec11.htm) |
| Dividends received deduction, less than 20% owned domestic payer | 50% | [26 U.S.C. 243(a)(1)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVIII-sec243.htm) |
| Dividends received deduction, 20% or more owned domestic payer | 65% | [26 U.S.C. 243(c)(1)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVIII-sec243.htm) |
| Dividends received deduction, qualifying dividends from an affiliated group member | 100% | [26 U.S.C. 243(a)(3)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVIII-sec243.htm); [Form 1120 (2025), Schedule C line 11](https://www.irs.gov/pub/irs-pdf/f1120.pdf) |
| Dividends on preferred stock of public utilities, Schedule C lines 4 and 5 | 23.3% and 26.7% | [Form 1120 (2025), Schedule C](https://www.irs.gov/pub/irs-pdf/f1120.pdf) |
| Charitable deduction floor, corporations (taxable years beginning after 31 December 2025) | 1 percent | [Public Law 119-21, section 70426](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| Charitable deduction cap, corporations | 10 percent | [Public Law 119-21, section 70426](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| Business interest limit, share of adjusted taxable income | 30 percent | [26 U.S.C. 163(j)(1)(B)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVI-sec163.htm) |
| Gross receipts test (section 448(c)): exempts a corporation from section 163(j) | USD 32,000,000 | [Rev. Proc. 2025-32](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Domestic research expensing (section 174A) applies to amounts paid or incurred in taxable years beginning after | December 31, 2024 | [Public Law 119-21, section 70302](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| Section 174A(c) election: amortize domestic research over not less than | 60 months | [Public Law 119-21, section 70302](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| NOL deduction limit, losses from taxable years beginning after 2017 | 80 percent of taxable income | [26 U.S.C. 172(a)(2)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVI-sec172.htm) |
| Estimated tax: no penalty if the year's tax is less than | USD 500 | [26 U.S.C. 6655(f)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapA-partI-sec6655.htm) |
| Estimated tax: each installment | 25 percent of the required annual payment | [26 U.S.C. 6655(d)(1)(A)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapA-partI-sec6655.htm) |
| Large corporation: taxable income in any of the 3 preceding years of | USD 1,000,000 or more | [26 U.S.C. 6655(g)(2)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapA-partI-sec6655.htm) |
| Corporate AMT rate on adjusted financial statement income (applicable corporations) | 15 percent | [26 U.S.C. 55(b)(2)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partVI-sec55.htm) |
| Applicable corporation: 3-year average financial statement income over | USD 1,000,000,000 | [26 U.S.C. 59(k)(1)(B)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partVI-sec59.htm) |
| Foreign-parented group member: own 3-year average of | USD 100,000,000 or more | [26 U.S.C. 59(k)(1)(B)(ii)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partVI-sec59.htm) |
| Accumulated earnings tax rate | 20 percent | [26 U.S.C. 531](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapG-partI-sec531.htm) |
| Accumulated earnings credit, minimum (USD 150,000 for health, law, engineering, architecture, accounting, actuarial, performing arts or consulting corporations) | USD 250,000 less accumulated E&P at the end of the prior year | [26 U.S.C. 535(c)(2)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapG-partI-sec535.htm) |
| Personal holding company tax rate | 20 percent | [26 U.S.C. 541](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapG-partII-sec541.htm) |
| Failure to file: per month or part month, capped at 25% | 5 percent | [26 U.S.C. 6651(a)(1)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapA-partI-sec6651.htm) |
| Failure to pay: per month or part month, capped at 25% | 0.5 percent | [26 U.S.C. 6651(a)(2)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapA-partI-sec6651.htm) |
| Minimum failure-to-file penalty, return more than 60 days late, returns required to be filed in 2027 | lesser of USD 535 or 100% of the tax | [Rev. Proc. 2025-32, section 3.52](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Underpayment interest, 4th quarter 2026 (corporate and non-corporate) | 7% | [IRS quarterly interest rates](https://www.irs.gov/payments/quarterly-interest-rates) |
| Large corporate underpayment interest, 4th quarter 2026 | 9% | [IRS quarterly interest rates](https://www.irs.gov/payments/quarterly-interest-rates) |
| Form 1125-E required if total receipts (line 1a plus lines 4 to 10) are | USD 500,000 or more | [Instructions for Form 1120 (2025), line 12](https://www.irs.gov/pub/irs-pdf/i1120.pdf) |
| Schedule L, M-1 and M-2 not required if total receipts and total assets are both less than | USD 250,000 | [Instructions for Form 1120 (2025), Schedule K question 13](https://www.irs.gov/pub/irs-pdf/i1120.pdf) |
| Schedule M-3 instead of M-1 at year-end total assets of | USD 10 million or more | [Instructions for Form 1120 (2025), Schedule M-3](https://www.irs.gov/pub/irs-pdf/i1120.pdf) |
| Schedule UTP: total assets of (with audited statements and a reportable position) | USD 10 million or more | [Instructions for Form 1120 (2025), Schedule K question 14](https://www.irs.gov/pub/irs-pdf/i1120.pdf) |
| BEAT (Form 8991) test: gross receipts in any of the 3 preceding years of at least | USD 500 million | [Instructions for Form 1120 (2025), Schedule K question 22](https://www.irs.gov/pub/irs-pdf/i1120.pdf) |
| E-file required if the corporation files, in the calendar year, returns of any type numbering | 10 or more | [Instructions for Form 1120 (2025), Electronic Filing](https://www.irs.gov/pub/irs-pdf/i1120.pdf) |
| Form 7004 automatic extension (tax years beginning in 2026, including June 30 year-ends) | 6 months | [Instructions for Form 7004 (Rev. December 2025)](https://www.irs.gov/pub/irs-pdf/i7004.pdf) |

Bonus depreciation is 100 percent for property acquired after 19 January 2025, and the section 179 limit for 2026 is set by Rev. Proc. 2025-32: both are owned by `us-section-179-and-bonus-depreciation`. The 2026 section 250 percentages for FDII and net CFC tested income are owned by `us-gilti-fdii-beat`. The statutory percentages above are not indexed; the USD 32,000,000, USD 535 and interest rates change each year or quarter.

### Step 1: who files, and for which period

1. Every domestic corporation in existence for any part of the tax year files, whether or not it had income or activity, unless it is exempt under section 501 or files a special return (1120-S, 1120-REIT, 1120-RIC, 1120-C, 1120-L, 1120-PC, 1120-F and so on). Source: [Instructions for Form 1120 (2025), Who Must File](https://www.irs.gov/pub/irs-pdf/i1120.pdf). The only way out for a dormant company is dissolution under state law, then a final return with the "Final return" box checked.
2. An LLC that elected corporate status files Form 1120 and attaches a copy of Form 8832 to the return for the year of the election (same source). The election can be effective up to 75 days before and 12 months after it is filed; once made, the entity generally cannot change again for 60 months (Reg. 301.7701-3(c)(1)(iv)). The first return covers the period from the effective date and should carry a statement noting the election and its date.
3. The tax year is set by the first return: calendar year, any fiscal year ending on the last day of a month, or a 52/53-week year (section 441(f)). A change needs Form 1128. A short first year runs from incorporation (or the Form 8832 effective date) to the chosen year-end and is due by the 15th day of the 4th month after it ends.
4. **Which form edition.** The 2026 Form 1120 is not yet published. The 2025 form is for calendar 2025 and fiscal years beginning in 2025. Line references below are from the 2025 form and must be checked against the 2026 edition when it is released.

### Step 2: page 1, income (lines 1a to 11)

5. **Line 1a** gross receipts; **1b** returns and allowances (treat cash discounts the same way every year); **1c** = 1a minus 1b.
6. **Line 2** cost of goods sold from Form 1125-A (attach whenever there is COGS). **Line 3** gross profit = 1c minus 2.
7. **Line 4** dividends and inclusions, gross, from Schedule C line 23. The dividends received deduction comes off later, on line 29b.
8. **Line 5** taxable interest. Tax-exempt interest is not here; it goes on Schedule K.
9. **Lines 6 and 7** gross rents and royalties.
10. **Line 8** capital gain net income from Schedule D (Form 1120). A corporation's capital losses offset only capital gains; a net capital loss is carried back 3 years and forward 5 years. Source: [26 U.S.C. 1212(a)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapP-partII-sec1212.htm).
11. **Line 9** Form 4797 Part II (ordinary gain and loss, section 1245 and 1250 recapture). A net section 1231 gain goes to Schedule D; a net section 1231 loss is ordinary.
12. **Line 10** other income with a statement (recoveries of amounts deducted earlier, refunds of taxes deducted, section 481(a) adjustments). **Line 11** total income = lines 3 to 10.

### Step 3: page 1, deductions (lines 12 to 27)

| Line | Item | What to check |
| --- | --- | --- |
| 12 | Compensation of officers | Form 1125-E if total receipts are USD 500,000 or more (name, SSN, % of time, % of stock, pay); pay must be reasonable (see Boundary table) |
| 13 | Salaries and wages | Less employment credits (for example the work opportunity credit) |
| 14 | Repairs and maintenance | Improvements are capitalized under section 263(a) and Reg. 1.263(a)-3 |
| 15 | Bad debts | Specific charge-off only; no reserve method (section 166) |
| 16 | Rents | Related-party rents: section 267 timing |
| 17 | Taxes and licenses | State income tax, property tax, employer payroll tax, excise. Federal income tax is never deductible. The individual SALT cap does not apply to a C corporation |
| 18 | Interest | After the section 163(j) limit (Step 5); Form 8990 if subject to it |
| 19 | Charitable contributions | After the 1 percent floor and 10 percent cap (Step 4) |
| 20 | Depreciation from Form 4562 | Not already in COGS; bonus and section 179 per `us-section-179-and-bonus-depreciation` |
| 21 | Depletion | Cost or percentage |
| 22 | Advertising | Includes website costs not capitalized |
| 23 | Pension, profit-sharing plans | Section 404 timing |
| 24 | Employee benefit programs | Health, group term life, dependent care not deducted elsewhere |
| 25 | Energy efficient commercial buildings deduction | Form 7205 (section 179D) |
| 26 | Other deductions, with a statement | Insurance, utilities, professional fees, travel, business meals at 50% (section 274(n)), software, bank fees, domestic research expensed under section 174A, amortization of capitalized research |
| 27 | Total deductions | |

13. **Line 28** = line 11 minus line 27: taxable income before the NOL deduction and special deductions.

### Step 4: the 2026 charitable deduction (line 19)

14. Compute "taxable income" for the limit without the charitable deduction itself, without the special deductions of part VIII (the dividends received deduction, section 250; section 248 organizational costs stay in), without any NOL or capital loss carryback, and without section 199A(g). Source: [26 U.S.C. 170(b)(2)(D)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVI-sec170.htm). If the corporation has an NOL carryover, the limit is applied to taxable income after the NOL deduction. Source: [Instructions for Form 1120 (2025), line 19](https://www.irs.gov/pub/irs-pdf/i1120.pdf).
15. For a taxable year beginning after 31 December 2025, the year's gifts are deductible only to the extent they exceed **1 percent** of that taxable income and do not exceed **10 percent** of it: deduction = the smaller of the gifts and 10% of taxable income, minus 1% of taxable income, not below zero. Source: [Public Law 119-21, section 70426(a)](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm), amending section 170(b)(2)(A).
16. **Carryforward.** Gifts above the 10 percent cap carry forward 5 years, first in first out; current-year gifts are taken before carryovers. Gifts lost under the 1 percent floor carry forward **only** in a year in which the 10 percent cap is also exceeded; in any other year they are lost for good. A carryover is cut to the extent it would increase an NOL carryover. Source: Public Law 119-21, section 70426(b), new section 170(d)(2)(A) to (D).
17. An accrual-method corporation can treat a gift paid by the original due date (not extensions) as paid in the tax year if the board authorized it during the year; attach a declaration with the date of the resolution. Source: [Instructions for Form 1120 (2025), line 19](https://www.irs.gov/pub/irs-pdf/i1120.pdf), section 170(a)(2)(B).
18. Before 2026 the rule was a 10% cap with no floor; a 2025 return is not affected by the floor.

### Step 5: business interest (line 18, section 163(j))

19. **Exemption.** A corporation whose average annual gross receipts for the 3 prior tax years do not exceed USD 32,000,000 (2026, section 448(c)) is not subject to the limit and generally does not file Form 8990, unless it is a tax shelter. Source: [Rev. Proc. 2025-32](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf). Electing real property trades or businesses and electing farming businesses (section 163(j)(7)(B) and (C), irrevocable) are also out, but must use the alternative depreciation system for certain property; regulated utilities are excluded.
20. **Limit.** Deductible business interest = business interest income + **30 percent** of adjusted taxable income + floor plan financing interest. Disallowed interest carries forward indefinitely (tracked on Form 8990). Source: [26 U.S.C. 163(j)(1)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVI-sec163.htm).
21. **Adjusted taxable income (ATI)** starts from taxable income computed without business interest expense or income, the NOL deduction or the section 199A deduction, and adds back depreciation, amortization and depletion. The add-back was restored for taxable years beginning after 31 December 2024 (Public Law 119-21, section 70303). For taxable years beginning after 31 December 2025, ATI also excludes subpart F (section 951(a)), GILTI (section 951A(a)) and section 78 gross-up inclusions and the related section 245A and section 250 deductions (section 70342). Floor plan financing now includes towable trailers and campers (section 70303(b)). Source: [Public Law 119-21](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm).
22. **New for 2026, capitalized interest.** For taxable years beginning after 31 December 2025 the limit applies to business interest whether it would be deducted or capitalized (for example under section 263A), and the amount allowed is applied **first** to the interest that would be capitalized and only then to interest that would be deducted. Carried-forward interest is never treated as capitalizable. Interest capitalized under section 263(g) or 263A(f) is not business interest. Source: Public Law 119-21, section 70341, new section 163(j)(10) and amended 163(j)(5). Effect: a corporation with self-constructed assets or inventory carrying costs may find its line 18 deduction smaller than before, because the allowance is used up on the capitalized interest first.

### Step 6: research, depreciation and the other 2026 cost-recovery points

23. **Domestic research (section 174A).** Domestic research or experimental expenditures paid or incurred in taxable years beginning after December 31, 2024 are deducted in the year paid or incurred (line 26 with a statement). Alternatively the corporation can elect under section 174A(c) to capitalize them and amortize over not less than 60 months from the month benefits are first realized. Source: [Public Law 119-21, section 70302](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm); [Instructions for Form 1120 (2025), What's New](https://www.irs.gov/pub/irs-pdf/i1120.pdf). Research costs include direct labor and materials, software development, allocated overhead and patent costs; they exclude market research, quality control, advertising, management studies and routine data collection.
24. **Foreign research** (performed outside the United States) stays capitalized under section 174 and is amortized over 15 years.
25. **The 2022 to 2024 domestic balance.** Domestic research capitalized in taxable years beginning in 2022 to 2024 keeps amortizing unless the corporation elected (section 70302(f)(2)) to deduct the unamortized balance in its first taxable year beginning after 31 December 2024, or ratably over that year and the next. A calendar-year corporation that chose the two-year option deducts the second half on its 2026 return. Procedures: Rev. Proc. 2025-28 (named in the Form 1120 instructions). Small businesses meeting the section 448(c) test could instead apply section 174A back to 2022 by amended returns, an election due within 1 year of enactment (4 July 2025), so it has closed. For material research spend, load `us-r-and-d-section-174-and-41` alongside.
26. **Research credit coordination.** The section 174A deduction is reduced by the section 41 credit allowed unless the reduced-credit election under section 280C(c)(2) is made on Form 6765.
27. **Depreciation.** 100% bonus depreciation is permanent for property acquired after 19 January 2025, and section 168(n) adds an elective 100% allowance for qualified production property. Use `us-section-179-and-bonus-depreciation` for the amounts, the binding-contract rule and the section 179 limit. Report on Form 4562 and line 20.

### Step 7: NOL and special deductions (lines 29a to 30)

28. **Line 29a, NOL.** Losses from taxable years beginning after 2017 are carried forward without time limit and are not carried back (farming and insurance exceptions aside; the CARES Act carryback window for 2018 to 2020 losses is closed). They offset at most **80 percent** of taxable income computed without the NOL, section 199A and section 250 deductions, after any pre-2018 NOLs are used. Pre-2018 NOLs had a 20-year carryforward and no 80% limit; the last ones (2017) can be used through 2037. Source: [26 U.S.C. 172(a) and (b)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVI-sec172.htm). After an ownership change of more than 50 percentage points in 3 years, section 382 limits the use of pre-change losses each year (equity value times the long-term tax-exempt rate, plus built-in gain adjustments): refer.
29. **Line 29b, special deductions** from Schedule C line 24: mainly the dividends received deduction (Step 8) and the section 250 deduction (Form 8993, Schedule C line 22).
30. **Line 30** taxable income = line 28 minus line 29c.

### Step 8: Schedule C, the dividends received deduction

31. Enter each dividend at gross in column (a) and the percentage in column (b): 50% for a less than 20% owned domestic payer (line 1), 65% for 20% or more owned (line 2), 100% for qualifying dividends from an affiliated group member (line 11, 80% by vote and value under section 1504(a), no consolidated return; inside a consolidated return intercompany dividends are eliminated). Debt-financed stock (line 3) gets a reduced percentage under section 246A. Preferred stock of public utilities: 23.3% and 26.7% (lines 4 and 5). Foreign payers: lines 6 to 8 and 13 (the section 245A 100% deduction for the foreign-source portion of dividends from a specified 10%-owned foreign corporation). Subpart F inclusions (lines 16a to 16c) and GILTI (line 17) are inclusions, not dividends, and get no dividends received deduction except line 16a. Source: [Form 1120 (2025), Schedule C](https://www.irs.gov/pub/irs-pdf/f1120.pdf).
32. **Holding period.** No deduction for a dividend on stock held 45 days or less in the 91-day period beginning 45 days before the ex-dividend date (90 days in a 181-day period for certain preferred stock), with days of reduced risk (hedges, short positions) not counted. Source: [26 U.S.C. 246(c)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVIII-sec246.htm). A common audit point for portfolio holders.
33. **Taxable income limit (section 246(b)).** The 50% and 65% deductions are limited to 50% and 65% of taxable income computed without the dividends received deduction, the NOL deduction, section 250 and certain capital loss carrybacks, unless taking the full deduction creates or increases an NOL. Use the worksheet for Schedule C lines 9 and 22 in the Form 1120 instructions. The 100% affiliated-group deduction is not limited.
34. Line 23 (total dividends and inclusions) goes to page 1 line 4; line 24 (total special deductions) goes to line 29b.

### Step 9: Schedule J, the tax

35. **Line 1a** = line 30 times 21%. Lines 1b to 1z add other chapter 1 taxes (section 1291 PFIC tax on line 1c, BEAT from Form 8991 on line 1f, and so on). **Line 3** is the corporate AMT from Form 4626 (applicable corporations only). **Lines 5a to 5f** are credits: foreign tax credit (Form 1118), general business credit (Form 3800), prior-year minimum tax credit (Form 8827). **Line 8** is the personal holding company tax (Schedule PH). **Line 12** total tax goes to page 1 line 31. Source: [Form 1120 (2025), Schedule J](https://www.irs.gov/pub/irs-pdf/f1120.pdf).
36. **Corporate AMT pointer.** The 15 percent minimum tax on adjusted financial statement income applies only to an applicable corporation: one whose average annual financial statement income for a 3-year period ending with an earlier taxable year (ending after 31 December 2021) exceeded USD 1,000,000,000, or, for a member of a foreign-parented group, USD 100,000,000 or more of its own. Financial statement income starts from book net income with the section 56A adjustments (tax depreciation in place of book, federal income tax added back, a financial statement NOL). The tax is paid only to the extent it exceeds regular tax plus BEAT, and it creates a minimum tax credit that reduces later regular tax. For every other corporation, record the conclusion that it is not an applicable corporation and skip Form 4626 (Schedule K asks the question). The Form 1120 instructions for 2025 point to an interim simplified method in Notice 2025-27 for the status test. Source: [26 U.S.C. 55(b)(2) and 59(k)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partVI-sec59.htm). Any actual computation: refer.
37. **Payments (Schedule J lines 13 to 23):** prior-year overpayment credited, 2026 estimated tax, any quick refund applied for on Form 4466, tax deposited with Form 7004, withholding, refundable credits. Page 1 line 34 is the estimated tax penalty (Form 2220); line 35 amount owed; line 36 overpayment; line 37 refund or credit to 2027 estimated tax.

### Step 10: estimated tax for 2026 (section 6655)

38. If the 2026 tax (regular tax plus CAMT and BEAT, less credits) is USD 500 or more, four installments are due on the 15th day of the 4th, 6th, 9th and 12th months of the tax year: for a calendar year **15 April, 15 June, 15 September and 15 December 2026** (all weekdays). Source: [26 U.S.C. 6655(c) and (f)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapA-partI-sec6655.htm).
39. Each installment is 25 percent of the required annual payment: the lesser of 100% of the 2026 tax and 100% of the tax shown on the 2025 return. The prior-year option is not available if 2025 was a short year or the 2025 return showed no liability (or was not filed). There is no 110% rule for corporations. Source: 26 U.S.C. 6655(d)(1).
40. **Large corporation** (taxable income of USD 1,000,000 or more in any of the 3 preceding tax years): it may use the prior-year tax only for the 1st installment, and any shortfall is added to the 2nd; installments 2 to 4 must be based on current-year tax. Source: 26 U.S.C. 6655(d)(2) and (g)(2).
41. **Annualized or seasonal method** (section 6655(e)) lowers installments for uneven income: the standard periods are the first 3, 3, 6 and 9 months (annualization factors 4, 4, 2 and 12/9), and other periods can be elected on Form 8842. Computed on Form 2220.
42. If any installment was short, compute the penalty on Form 2220 and attach it; the IRS instructions treat this as the corporation's job. The IRS waived the section 6655 penalty attributable to CAMT for tax year 2025 (Notice 2025-27); whether that relief continues for 2026 is not yet confirmed.
43. Pay all federal tax deposits electronically (EFTPS or IRS business payment options).

### How the result flows on

The year's after-tax earnings feed earnings and profits, which decide whether a later distribution is a taxable dividend to the shareholder. A dividend paid by a C corporation is not deductible to it; owner pay that is reasonable is. Because the rate is flat, timing income into a lower band no longer helps; what is left is deferral (NOLs, accelerated deductions) and the choice between deductible pay and a nondeductible dividend. The decision between paying a dividend and keeping the money in the company is Worked case 1.

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Corporation had no income or activity | Still files; only dissolution under state law ends the duty |
| Tax under USD 500 for the year | No estimated tax penalty (section 6655(f)) |
| Fiscal year ending 30 June, year beginning in 2025 (ends 30 June 2026) | Due 15th day of the 3rd month (15 September 2026); Form 7004 gives 7 months (to 15 April 2027) |
| Fiscal year ending 30 June, year beginning in 2026 (ends 30 June 2027) | Ordinary rule: 15th day of the 4th month (15 October 2027); Form 7004 gives 6 months |
| Short year ending any time in June | Treated as ending 30 June for the due date |
| Due date on a Saturday, Sunday or legal holiday | Next business day (section 7503) |
| Charitable gifts under 1 percent of taxable income in 2026 | No deduction, and no carryforward (the cap was not exceeded) |
| Charitable gifts over 10 percent | Deduction = 10% minus 1%; the excess over 10% and the floor amount both carry forward 5 years |
| Average gross receipts USD 32,000,000 or less | Section 163(j) does not apply; no Form 8990 in most cases |
| Dividend on stock held 45 days or less around the ex-date | No dividends received deduction (section 246(c)) |
| Taxable income small relative to dividends | Section 246(b) caps the 50% / 65% deduction unless the full deduction creates or increases an NOL |
| Owner-employee pay well above market | IRS may recast the excess as a constructive dividend: no deduction to the company, dividend to the owner. Courts look at role, hours, industry pay, the company's pay policy and whether an independent investor would accept the return on equity (Mayson Mfg., Charles Schneider, Menard; Exacto Spring, 7th Cir. 1999). Flag for review |
| Publicly held corporation, covered employee pay over USD 1,000,000 | Excess not deductible (section 162(m), all forms of pay, no performance-pay exception; private companies are not affected); from taxable years beginning after 31 December 2025 pay from other controlled group members is aggregated and the USD 1,000,000 is shared pro rata (Public Law 119-21, section 70603); the next five highest paid become covered employees for taxable years beginning after 2026 (ARPA) |
| Change-in-control payments | Section 280G may deny the deduction for excess parachute payments (and section 4999 taxes the recipient); flag any acquisition year |
| Retained earnings beyond the reasonable needs of the business | Accumulated earnings tax of 20 percent on accumulated taxable income (section 531); see Worked case 1 |
| Mainly passive income and 5 or fewer owners hold over half the stock | Possible personal holding company (20 percent tax, Schedule PH): refer |
| LLC converts from disregarded entity to corporation | Deemed section 351 transfer: carryover basis (section 362), holding period tacks (section 1223); the owner's earlier Schedule C losses stay with the owner. Same EIN |
| Partnership converts to corporation | One of the three forms in Rev. Rul. 84-111 decides basis and gain: refer if material |
| Corporation files fewer than 10 returns of all types in the calendar year | Paper filing allowed; e-file still recommended |
| No tax due on a late return | No section 6651 filing penalty (nothing to apply the 5% to) |

### Further worked figures (prose only, from the earlier version, corrected for 2026)

- **NOL at 80%.** A USD 1,000,000 post-2017 NOL carryforward and 2026 taxable income before the NOL of USD 800,000: the NOL deduction is the smaller of USD 1,000,000 and 80% x USD 800,000 = USD 640,000. Taxable income USD 160,000, tax USD 33,600, and USD 360,000 carries to 2027.
- **Section 163(j).** Taxable income computed without business interest expense and income is USD 4,950,000; depreciation of USD 1,500,000 is added back (the 2025 onward rule), so ATI is USD 6,450,000. Limit: 30% x USD 6,450,000 = USD 1,935,000 plus USD 50,000 of business interest income = USD 1,985,000. Interest expense of USD 1,800,000 is fully deductible; with USD 2,500,000 of interest, USD 515,000 carries forward. (The earlier version added interest back to a figure already before interest and left out the depreciation add-back.)
- **Dividends received deduction.** USD 100,000 from a 5% holding (50%) gives USD 50,000; USD 200,000 from a 30% holding (65%) gives USD 130,000; USD 500,000 from a 100% affiliated subsidiary (100%) gives USD 500,000; total USD 680,000 on Schedule C line 24. If taxable income before the deduction were USD 50,000 and only the 50% dividend existed, section 246(b) would cap it at USD 25,000 unless the NOL exception applies.
- **Corporate AMT.** An applicable corporation with financial statement income of USD 1,100,000,000, a usable financial statement NOL of USD 200,000,000 (within the 80% limit) and regular taxable income of USD 300,000,000: tentative minimum tax 15% x USD 900,000,000 = USD 135,000,000; regular tax 21% x USD 300,000,000 = USD 63,000,000; CAMT USD 72,000,000, which becomes a minimum tax credit carryforward. As a large corporation, its installments must be based on current-year tax.

## Worked cases

**Case 1, a decision: pay a dividend or keep the earnings in the company?** A calendar-year C corporation has 2026 taxable income of USD 500,000. Its sole shareholder is single, already has taxable income above USD 545,500 (the 2026 top of the 15% band for qualified dividends, Rev. Proc. 2025-32) and modified AGI above the USD 200,000 net investment income tax threshold. Accumulated E&P at the end of 2025 is USD 1,200,000. The board has a documented plan to spend USD 300,000 on equipment in 2027.

Corporate tax: USD 500,000 x 21% = USD 105,000, leaving USD 395,000 after tax. If all of it is paid out as a qualified dividend, the shareholder pays 20% (section 1(h)(1)(D)) plus 3.8% (section 1411) = 23.8%, which is USD 94,010, and keeps USD 300,990. The combined federal rate is 39.802% (USD 199,010 of USD 500,000).

If all USD 395,000 is kept, the shareholder pays nothing now. But the minimum accumulated earnings credit is zero (USD 250,000 less USD 1,200,000 of prior E&P), so only the USD 300,000 tied to the documented plan is sheltered. If the IRS finds the other USD 95,000 retained beyond reasonable needs, the accumulated earnings tax is 20% x USD 95,000 = USD 19,000, on top of the dividend tax the shareholder still pays when the money comes out later. (This assumes no other section 535(b) adjustments to accumulated taxable income.)

The middle course: keep USD 300,000 for the plan and pay a USD 95,000 dividend in 2026. The dividends paid deduction removes the USD 95,000 from accumulated taxable income, so the accumulated earnings tax is zero; the shareholder pays USD 22,610 now. Recommend this unless the board can document needs for the whole USD 395,000. Keeping everything saves USD 22,610 of shareholder tax this year but risks USD 19,000 of company tax that never comes back; paying everything out costs USD 71,400 more shareholder tax now (USD 94,010 less USD 22,610) and gives up the deferral on money the company needs.

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
  - retain_all_aet: max(after_tax - documented_needs - min_credit, 0) * 0.20
  - split_dividend: after_tax - documented_needs
  - split_shareholder_tax: split_dividend * shareholder_rate
  - split_aet: max(after_tax - split_dividend - documented_needs - min_credit, 0) * 0.20
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

Charitable: the floor is 1% x USD 1,200,000 = USD 12,000 and the cap is 10% = USD 120,000. Deduction = USD 120,000 minus USD 12,000 = USD 108,000 on line 19. Because the 10% cap was exceeded, both the USD 30,000 above the cap and the USD 12,000 under the floor carry forward: USD 42,000 for up to 5 years. Line 28 = USD 1,092,000. Dividends received deduction: 50% x USD 40,000 = USD 20,000; the section 246(b) limit (50% x USD 1,092,000 = USD 546,000) does not bind. Line 30 = USD 1,072,000; tax = USD 225,120. Under the 2025 rule (10% cap, no floor) the deduction would have been USD 120,000: the floor costs USD 2,520 of tax this year, though here the USD 12,000 is carried forward rather than lost.

Estimated tax: the corporation was not a large corporation for 2026, so the required annual payment is the lesser of USD 225,120 and USD 180,000 = USD 180,000, or USD 45,000 per installment. With 2026 taxable income above USD 1,000,000, it is a large corporation for 2027: only the first 2027 installment may be based on the 2026 tax.

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

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-1120-CONSOL | Member of an affiliated group filing a consolidated return (sections 1501 to 1504, Reg. 1.1502, Forms 851 and 1122) | Refer: SRLY limits, intercompany transactions (Reg. 1.1502-13), excess loss accounts, consolidated section 163(j) and CAMT are outside this skill. If no consolidated election, each member files its own Form 1120 under this skill |
| R-1120-PSC | Personal service corporation (calendar year under section 441(i) unless a section 444 election, Forms 8716 and 8752) | Refer for review |
| R-1120-PHC | Possible personal holding company (Schedule PH) | Refer |
| R-1120-SPECIAL | REIT, RIC, cooperative, insurance company, FSC, REMIC, tax-exempt organization, foreign corporation | Wrong form: 1120-REIT, 1120-RIC, 1120-C, 1120-L, 1120-PC, 1120-FSC, 1066, 990-T or 1120-F |
| R-1120-CAMT | Possible applicable corporation under section 59(k) | Refer the Form 4626 computation (proposed regulations REG-112129-23 run to several hundred pages) |
| R-1120-INTL | CFCs, GILTI or FDII, BEAT, foreign tax credit (Form 1118, including the 10% haircut on PTEP-related foreign taxes for distributions after 28 June 2025), country-by-country report (Form 8975) | Use `us-gilti-fdii-beat`, `us-cfc-gilti`, `us-form-5471-cfc-information`; refer Form 1118 and Form 8975 |
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
- **E-file.** Required if the corporation files 10 or more returns of any type in the calendar year (income, employment, excise and information returns, counted together), with a waiver procedure. Source: [Instructions for Form 1120 (2025), Electronic Filing](https://www.irs.gov/pub/irs-pdf/i1120.pdf); Reg. 301.6011-5. Filing goes through Modernized e-File and an authorized provider. An authorized officer signs Form 8879-CORP for an e-filed return; the electronic return originator keeps it.
- **Penalties.** Late filing: 5% of the unpaid tax for each month or part month, to 25%. Late payment: 0.5% a month, to 25% (the reduced rate during an installment agreement is for individuals only). In a month when both apply, the filing penalty is reduced by the payment penalty, so the most for both together is 47.5% (22.5% plus 25%). A return more than 60 days late that is required to be filed in 2027 carries a minimum filing penalty of the lesser of USD 535 or the tax due. Reasonable cause, documented at the time, can remove either. Sources: [26 U.S.C. 6651](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapA-partI-sec6651.htm); [Rev. Proc. 2025-32, section 3.52](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf). The per-shareholder penalty for late S corporation and partnership returns (section 6699) does not apply to a C corporation.
- **Interest** runs from the original due date at the underpayment rate (7% in the 4th quarter of 2026; 9% for the large corporate underpayment rate), set quarterly. Source: [IRS quarterly interest rates](https://www.irs.gov/payments/quarterly-interest-rates).

**Schedules and forms to attach.**

| Schedule or form | When |
| --- | --- |
| Schedule C | Any dividends, inclusions or special deductions |
| Schedule J, Schedule K | Every return |
| Schedule L, M-1, M-2 | Unless total receipts and total assets are both under USD 250,000 (Schedule K question 13); Schedule L must tie to the books |
| Schedule M-3 (instead of M-1) | Total assets USD 10 million or more at year-end; under USD 50 million it may complete Part I only plus Schedule M-1 |
| Schedule B (Form 1120) | Additional information for Schedule M-3 filers |
| Schedule UTP | Total assets USD 10 million or more, audited financial statements, and a reportable position |
| Schedule O | Member of a controlled group (apportionment of the accumulated earnings credit and other items) |
| Schedule D, Form 4797 | Capital gains and losses; business property sales |
| Form 1125-A | Any cost of goods sold |
| Form 1125-E | Total receipts USD 500,000 or more |
| Form 4562 | Depreciation, section 179, amortization (including capitalized research, section 195 and section 197) |
| Form 8990 | Subject to section 163(j) |
| Form 8993 | Any section 250 deduction |
| Form 4626 | Applicable corporation (CAMT) |
| Form 8991 | Gross receipts of at least USD 500 million in any of the 3 preceding years |
| Form 2220 | Any estimated tax installment short |
| Form 3800, Form 6765, Form 1118 | Business credits, research credit, foreign tax credit |
| Form 5471, Form 5472 | CFC shareholder; 25% foreign-owned corporation |
| Form 8832 copy | Year an LLC's corporate election takes effect |
| Form 1128 | Change of tax year |
| Form 7205 | Section 179D deduction |

Schedule M-1 reconciles net income per books to line 28: add federal income tax expense, excess capital losses, income taxed but not booked and expenses booked but not deducted (the nondeductible half of meals, fines, political and lobbying costs, club dues, section 162(m) excess, charitable amounts over the limit); subtract income booked but not taxed (tax-exempt interest, life insurance proceeds) and deductions not booked (tax depreciation above book, bonus depreciation). Schedule K also asks about foreign ownership of 25% or more (Form 5472), section 163(j) status, BEAT, section 267A hybrid payments and CAMT status.

## Completion checklist

- Correct form and edition for the tax year; 2026 Form 1120 line numbers checked once the IRS publishes it.
- Prior three years' taxable income and gross receipts on file (large corporation and USD 32,000,000 tests).
- Charitable deduction after the 1 percent floor and 10 percent cap; carryforward schedule updated, and floor amounts kept only where the cap was exceeded.
- Section 163(j): exempt, or Form 8990 with ATI excluding CFC inclusions and the capitalized interest ordering applied.
- Domestic research deducted under section 174A (or the 174A(c) election documented); foreign research amortized over 15 years; any 2022 to 2024 balance handled per the election made.
- NOL deduction no more than 80% of taxable income for post-2017 losses; section 382 flagged if ownership changed.
- Every dividend tested for holding period, debt financing and the section 246(b) limit.
- CAMT status documented (applicable corporation or not).
- Estimated tax installments reconciled; Form 2220 attached if any were short.
- Retained earnings reviewed against documented business needs (accumulated earnings tax).
- Form 7004 filed and tax paid by 15 April 2027 if the return will be late.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| 26 U.S.C. 11 (govinfo). Read for (b): the tax is 21 percent of taxable income. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partII-sec11.htm | 2026-11-13 |
| 26 U.S.C. 243 (govinfo). Read for (a)(1) 50 percent, (c)(1) 65 percent for 20-percent owned payers, (a)(3) qualifying dividends. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVIII-sec243.htm | 2026-11-13 |
| 26 U.S.C. 246 (govinfo). Read for (b) the taxable income limit and (c) the 45-day holding period in the 91-day window. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVIII-sec246.htm | 2026-11-13 |
| 26 U.S.C. 163 (govinfo, 2024 edition). Read for (j)(1): business interest income plus 30 percent of adjusted taxable income plus floor plan interest. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVI-sec163.htm | 2026-11-13 |
| 26 U.S.C. 170 (govinfo, 2024 edition). Read for (b)(2)(D), how taxable income is computed for the corporate limit. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVI-sec170.htm | 2026-11-13 |
| 26 U.S.C. 172 (govinfo). Read for (a)(2) the 80 percent limit and (b)(1)(A) the 20-year and indefinite carryforwards. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVI-sec172.htm | 2026-11-13 |
| 26 U.S.C. 1212 (govinfo). Read for (a)(1): corporate net capital loss carried back 3 years and forward 5. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapP-partII-sec1212.htm | 2026-11-13 |
| 26 U.S.C. 55 (govinfo). Read for (b)(2)(A): 15 percent of adjusted financial statement income for applicable corporations. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partVI-sec55.htm | 2026-11-13 |
| 26 U.S.C. 59 (govinfo). Read for (k): the USD 1,000,000,000 and USD 100,000,000 average income tests. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partVI-sec59.htm | 2026-11-13 |
| 26 U.S.C. 531 (govinfo). Read for the 20 percent accumulated earnings tax. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapG-partI-sec531.htm | 2026-11-13 |
| 26 U.S.C. 535 (govinfo). Read for (c)(2): minimum credit of USD 250,000 (USD 150,000 for listed service corporations) less prior E&P. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapG-partI-sec535.htm | 2026-11-13 |
| 26 U.S.C. 541 (govinfo). Read for the 20 percent personal holding company tax. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapG-partII-sec541.htm | 2026-11-13 |
| 26 U.S.C. 1 (govinfo). Read for (h)(1)(D): 20 percent on adjusted net capital gain (qualified dividends) above the 15% band. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partI-sec1.htm | 2026-11-13 |
| 26 U.S.C. 1411 (govinfo). Read for 3.8 percent and the USD 200,000 / USD 250,000 thresholds. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap2A-sec1411.htm | 2026-11-13 |
| 26 U.S.C. 6072 (govinfo). Read for (a): 15th day of the fourth month after the fiscal year (subsection (b) is partnerships and S corporations). | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap61-subchapA-partV-sec6072.htm | 2026-11-13 |
| 26 U.S.C. 6651 (govinfo). Read for (a)(1) 5 percent a month to 25 percent and (a)(2) 0.5 percent a month. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapA-partI-sec6651.htm | 2026-11-13 |
| 26 U.S.C. 6655 (govinfo). Read for (c) due dates, (d)(1) 25 percent and 100 percent, (d)(2) large corporations, (e) annualization periods, (f) USD 500, (g)(2) USD 1,000,000. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapA-partI-sec6655.htm | 2026-11-13 |
| Public Law 119-21 (One Big Beautiful Bill Act). Read for sections 70302 (section 174A, 60 months, transition elections), 70303 (ATI add-back, trailers), 70341 (capitalized interest), 70342 (CFC inclusions out of ATI), 70426 (1 percent floor, 10 percent cap, carryforward), 70603 (section 162(m) controlled groups), 70321 and 70331 (effective dates for section 250 and BEAT). | https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm | 2026-11-13 |
| Rev. Proc. 2025-32. Read for the section 448(c) amount (USD 32,000,000) and section 3.52 (USD 535 minimum penalty, returns required to be filed in 2027). | https://www.irs.gov/pub/irs-drop/rp-25-32.pdf | 2026-11-13 |
| Form 1120 (2025). Read for page 1 lines 1a to 37, Schedule C lines 1 to 24 and percentages, Schedule J lines 1a to 23. | https://www.irs.gov/pub/irs-pdf/f1120.pdf | 2026-11-13 |
| Instructions for Form 1120 (2025). Read for What's New (section 174A, CAMT relief, USD 525 penalty for 2026 filings), Who Must File, Electronic Filing (10 returns), When To File (June 30 rule), line 12 (USD 500,000), line 19, Schedule M-3 (USD 10 million, USD 50 million), Schedule K questions 13, 14 and 22. | https://www.irs.gov/pub/irs-pdf/i1120.pdf | 2026-11-13 |
| Instructions for Form 7004 (Rev. December 2025). Read for the 6-month extension, the 7-month June 30 rule for years beginning before 2026, and no approval notice. | https://www.irs.gov/pub/irs-pdf/i7004.pdf | 2026-11-13 |
| IRS quarterly interest rates. Read for 2026 4th quarter underpayment 7% and large corporate underpayment 9%. | https://www.irs.gov/payments/quarterly-interest-rates | 2026-11-13 |

Not yet confirmed: the 2026 Form 1120, its instructions and the 2026 Form 2220 were not published when read, so line numbers and the USD 500,000, USD 250,000 and USD 10 million form thresholds are taken from the 2025 editions; whether the IRS extends the CAMT estimated tax penalty relief (Notice 2025-27) to 2026; interest rates for 2027 quarters; the section 382 long-term tax-exempt rate for 2026 ownership changes (not opened); Reg. 301.7701-3, Rev. Rul. 84-111, sections 162(m) (beyond the Public Law 119-21 text), 246A, 280G and 441 were not reopened today and are carried from the earlier version of this skill; 26 U.S.C. 6621 on govinfo could not be opened (page not found), so interest rates come from the IRS page only.
