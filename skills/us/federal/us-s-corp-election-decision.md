---
name: us-s-corp-election-decision
description: Decide whether a US sole proprietor or single-member LLC should elect S corporation status (Form 2553, 26 U.S.C. 1362) for 2026 or 2027. Covers who can elect, reasonable compensation and the IRS power to recharacterize distributions as wages, the payroll tax saved (self-employment tax against FICA on salary only, with the 2026 Social Security wage base of $184,500), the added costs, the QBI deduction interaction under section 199A (salary is not QBI, but it is W-2 wages), other wages above the wage base, the Form 2553 deadline (2 months and 15 days, so 16 March 2026 for a calendar-year 2026 election and 15 March 2027 for 2027), late-election relief under Rev. Proc. 2013-30, revocation and the five-year bar, and state entity-level taxes flagged to the state skills. Trigger on "should I elect S corp", "S corp election", "Form 2553", "LLC taxed as S corp", "reasonable salary", "save self-employment tax", "late S election", "Rev. Proc. 2013-30". Federal only.
version: "1.0"
jurisdiction: US
tax_year: 2026
last_updated: 2026-11-13
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: decision
---

# US S corporation election for a sole proprietor or single-member LLC, tax year 2026

> **Source-cited draft.** Built from the Instructions for Form 2553 (Rev. December 2020), Form 2553 (Rev. December 2017), Rev. Proc. 2013-30, IRS Pub. 15 (2026), Rev. Proc. 2025-32, the IRS page on S corporation compensation, Public Law 119-21 section 70105, and 26 U.S.C. 199A, 1361, 1362, 1401, 1402, 6413(c) and 7503, read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before an election is filed.

**Answer first.** An S corporation saves payroll tax only on the profit paid out as distributions instead of salary. As a sole proprietor the owner pays 15.3% self-employment tax on 92.35% of profit (the 12.4% part up to **$184,500** for 2026). As an S corporation shareholder-employee the owner pays 15.3% FICA (employer plus employee) only on a salary that must be **reasonable compensation** for the work done. From that saving take off the added costs (payroll, Form 1120-S, state fees and taxes) and the income tax effect: salary is not qualified business income, so below the section 199A threshold the S corporation usually cuts the 20% QBI deduction. When the owner's other wages already pass $184,500, the saving falls to the 2.9% Medicare part and usually disappears. For a calendar-year entity the 2026 election deadline was **16 March 2026** (15 March was a Sunday); the 2027 deadline is **15 March 2027**. A missed 2026 election can be saved only through Rev. Proc. 2013-30 (intent from the start, reasonable cause, within 3 years and 75 days).

## Scope and who this is for

In scope: one individual who now files Schedule C (a sole proprietor or a single-member LLC disregarded for federal tax) and is deciding whether to have the business taxed as an S corporation from 2026 or 2027; or who already has an S election and is deciding whether to keep it. The output is a decision brief for the reviewer: the payroll tax saved at a stated salary, the added costs, the QBI effect, state flags, the deadline and a recommendation with its conditions. It does not file Form 2553, run payroll or prepare Form 1120-S.

Out of scope, and where it goes:

| Topic | Skill |
| --- | --- |
| Schedule C profit and Schedule SE self-employment tax, line by line | `us-schedule-c-and-se-computation` |
| The QBI deduction, its 2026 thresholds and phase-in, SSTB rules | `us-qbi-deduction` |
| Running payroll after the election: Forms 941, 940, W-2, FUTA | `us-form-941-940-payroll` |
| State payroll, unemployment insurance and new-hire rules | `us-state-payroll-matrix`, `us-state-new-hire-reporting-matrix` |
| Forming the LLC or corporation in a state | `us-state-formation-matrix` |
| Retirement contribution limits for salary against Schedule C earnings | `us-self-employed-retirement` |
| Health insurance of a more-than-2% shareholder | `us-self-employed-health-insurance` |
| Elective pass-through entity taxes (SALT workaround) | `us-pte-state-matrix` |
| C corporation compared with S corporation | `us-form-1120-c-corp` |
| Partnerships and multi-member LLCs | `us-form-1065-partnership` |
| State entity-level taxes on S corporations | the state skill named in the state table below |

## Ask the client first

1. **What is the entity today?** A sole proprietor with no entity cannot elect: only a corporation, or an entity eligible to be treated as one (an LLC), can file Form 2553. When was it formed, and does anyone other than the owner (or the owner's spouse) hold an interest? Is any owner a nonresident alien, a partnership or a corporation?
2. **Expected 2026 and 2027 profit** before any owner salary, and how steady it is. One good year is not enough: the costs recur every year.
3. **What the owner does and what that work would cost to hire:** duties, hours, who produces the revenue (the owner personally, staff, or equipment and capital), and any market pay data. This sets the reasonable salary.
4. **Other wages:** W-2 wages from any job in 2026 (Form W-2 boxes 3 and 5), and the spouse's wages and self-employment income. Wages above $184,500 remove most of the saving.
5. **Filing status, other income and deductions**, enough to place taxable income against the QBI threshold in `us-qbi-deduction` and to know the marginal rate.
6. **State of residence and of the business**, and quotes for the added costs: payroll provider, Form 1120-S preparation, state fees and unemployment insurance.

## The method, step by step

### Rates, bands and thresholds

| Item | Amount, 2026 | Source |
| --- | --- | --- |
| Social Security part of self-employment tax | 12.4 percent | [26 U.S.C. 1401(a)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap2-sec1401.htm) |
| Medicare part of self-employment tax | 2.9 percent | [26 U.S.C. 1401(b)(1)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap2-sec1401.htm) |
| Self-employment tax rate in total | 15.3% | [IRS, self-employment tax](https://www.irs.gov/businesses/small-businesses-self-employed/self-employment-tax-social-security-and-medicare-taxes) |
| Net earnings factor (Schedule SE line 4a) | 92.35% | [Schedule SE (Form 1040) 2026](https://www.irs.gov/pub/irs-pdf/f1040sse.pdf) |
| Social Security wage base (wages plus net self-employment earnings) | USD 184,500 | [IRS Pub. 15 (2026)](https://www.irs.gov/pub/irs-pdf/p15.pdf) |
| Social security tax on salary, each for employer and employee | 6.2% | [IRS Pub. 15 (2026)](https://www.irs.gov/pub/irs-pdf/p15.pdf) |
| Medicare tax on salary, each for employer and employee, no wage base | 1.45% | [IRS Pub. 15 (2026)](https://www.irs.gov/pub/irs-pdf/p15.pdf) |
| Additional Medicare Tax on wages and self-employment income above the threshold | 0.9 percent | [26 U.S.C. 1401(b)(2)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap2-sec1401.htm) |
| Additional Medicare Tax threshold, single, head of household | USD 200,000 | [26 U.S.C. 1401(b)(2)(A)(iii)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap2-sec1401.htm) |
| Additional Medicare Tax threshold, married filing jointly | USD 250,000 | [26 U.S.C. 1401(b)(2)(A)(i)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap2-sec1401.htm) |
| Additional Medicare Tax threshold, married filing separately | USD 125,000 | [IRS Additional Medicare Tax Q&A](https://www.irs.gov/businesses/small-businesses-self-employed/questions-and-answers-for-the-additional-medicare-tax) |
| QBI deduction rate, on qualified business income and capped at 20 percent of taxable income less net capital gain; made permanent by Public Law 119-21 section 70105(b) | 20 percent | [26 U.S.C. 199A(a), (b)(2)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVI-sec199A.htm), [Public Law 119-21](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| Standard deduction, single (used in Case 1) | USD 16,100 | [Rev. Proc. 2025-32](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Top of the single 22% band (used in Case 1) | USD 105,700 | [Rev. Proc. 2025-32](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Form 2553 window for the year it takes effect | no more than 2 months and 15 days after the tax year begins, or any time in the preceding tax year | [26 U.S.C. 1362(b)(1)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapS-partI-sec1362.htm), [Instructions for Form 2553](https://www.irs.gov/pub/irs-pdf/i2553.pdf) |
| Calendar year 2026 election, last day (15 March 2026 was a Sunday) | 16 March 2026 | [26 U.S.C. 7503](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap77-sec7503.htm) |
| Calendar year 2027 election, last day (a Monday) | 15 March 2027 | [26 U.S.C. 1362(b)(1)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapS-partI-sec1362.htm) |
| Late-election relief, time limit from the intended effective date | 3 years and 75 days | [Rev. Proc. 2013-30, section 4.02(2)](https://www.irs.gov/pub/irs-drop/rp-13-30.pdf) |
| Re-election after a revocation or termination, without IRS consent | not before the 5th tax year after the first year the termination is effective | [26 U.S.C. 1362(g)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapS-partI-sec1362.htm) |
| Shareholder limit | 100 | [26 U.S.C. 1361(b)(1)(A)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapS-partI-sec1361.htm) |

The statutory rates and the Additional Medicare Tax thresholds are not indexed. The wage base, the standard deduction and the bands change each year. The QBI thresholds and phase-in amounts for 2026 are in `us-qbi-deduction`; FUTA and state unemployment rates are in `us-form-941-940-payroll` and `us-state-payroll-matrix`.

### Step 1: can this business elect at all?

1. **There must be an entity.** Form 2553 is filed by "a corporation or other entity eligible to elect to be treated as a corporation" ([Instructions for Form 2553](https://www.irs.gov/pub/irs-pdf/i2553.pdf)). A sole proprietor forms an LLC or a corporation first (`us-state-formation-matrix`).
2. **A single-member LLC does not need Form 8832.** An eligible entity that files a timely Form 2553 and meets the tests is treated as a corporation from the S election's effective date (Instructions for Form 2553, Purpose of Form; deemed classification election in Treas. Reg. 301.7701-3(c)(1)(v)(C)).
3. **The small business corporation tests** ([26 U.S.C. 1361(b)(1)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapS-partI-sec1361.htm)): a domestic corporation that is not an ineligible corporation (certain banks, insurance companies, DISCs), with no more than 100 shareholders, only individuals, estates, certain trusts and certain exempt organizations as shareholders, no nonresident alien shareholder, and no more than one class of stock (differences in voting rights alone are allowed). The tax year must be a calendar year or one of the permitted fiscal years. Every shareholder consents (Form 2553 column K).

If any test fails, stop: the S election is not available (see the refusal table).

### Step 2: set the reasonable salary first

4. **The rule.** "S corporations must pay reasonable compensation to a shareholder-employee in return for services that the employee provides to the corporation before non-wage distributions may be made" ([IRS, S corporation compensation and medical insurance issues](https://www.irs.gov/businesses/small-businesses-self-employed/s-corporation-compensation-and-medical-insurance-issues)). Distributions to an officer are wages to the extent they are reasonable compensation (Pub. 15 (2026), Officers or shareholders of an S corporation), and the IRS can reclassify them, with employment tax, penalties and interest. Courts have upheld this: Joly v. Commissioner, T.C. Memo. 1998-361, aff'd 211 F.3d 1269 (6th Cir. 2000); Veterinary Surgical Consultants, P.C. v. Commissioner, 117 T.C. 141 (2001); Joseph M. Grey Public Accountant, P.C. v. Commissioner, 119 T.C. 121 (2002); David E. Watson, P.C. v. United States, 668 F.3d 1008 (8th Cir. 2012) (all as listed on the IRS page).
5. **Where the money comes from.** The IRS looks at the source of gross receipts: the shareholder's own services, the services of non-shareholder employees, and capital and equipment. Receipts from the owner's personal services (and the owner's management of staff and assets) point to wages; receipts from staff and equipment can support distributions. A solo service business with no staff and little equipment has the least room.
6. **The IRS factors:** training and experience; duties and responsibilities; time and effort devoted; dividend history; payments to non-shareholder employees; timing and manner of paying bonuses to key people; what comparable businesses pay for similar services; compensation agreements; the use of a formula. Reasonable compensation never exceeds what the shareholder actually received.
7. **Document it:** a job description, market pay data for the role and place (for example the Bureau of Labor Statistics occupational wage data), hours, and a written compensation decision; then pay it through payroll every month or quarter with withholding.
8. **No percentage rule exists.** Old rules of thumb ("60% of profit") are not law and are not in any IRS source. Use the evidence; if there is none, assume the salary is close to profit and say so in the brief.

### Step 3: payroll tax as a sole proprietor against as an S corporation

9. **Sole proprietor** (Schedule SE, see `us-schedule-c-and-se-computation`): net earnings = profit x 92.35%; tax = 12.4% on net earnings up to whatever remains of USD 184,500 after the owner's other Social Security wages, plus 2.9% on all net earnings.
10. **S corporation:** on the salary W, employer 6.2% plus 1.45% and employee 6.2% plus 1.45% (15.3% in total below the wage base); distributions carry no Social Security or Medicare tax. The employer half is a deduction of the corporation.
11. **Other wages above the wage base.** If the owner also has a job, the S corporation is a second employer. It must still pay the employer 6.2% on the salary. The employee 6.2% withheld by both employers above USD 184,500 comes back as a credit on Form 1040 ([26 U.S.C. 6413(c)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap65-subchapB-sec6413.htm), "a credit or refund" of the section 3101(a) tax only), but the employer share is never refunded. As a sole proprietor, Schedule SE line 9 would be zero and only 2.9% applies. So with other wages at or above the base, the S corporation usually costs more payroll tax, not less (Case 2).
12. **Additional Medicare Tax** (0.9%) applies to salary and to self-employment income above the threshold, but not to S corporation distributions. Count it in both columns when wages plus profit pass USD 200,000 (single) or USD 250,000 (joint).

### Step 4: added costs

13. List the client's quotes, each year: payroll service (and quarterly Form 941, annual Form 940 and Forms W-2), Form 1120-S and Schedule K-1 preparation, FUTA and state unemployment insurance on the salary (`us-form-941-940-payroll`, `us-state-payroll-matrix`), workers' compensation where the state requires it, state annual reports, franchise taxes or entity-level taxes (state table below), and extra bookkeeping. Do not use national averages; this skill holds no official cost figures.

### Step 5: the income tax effect, mainly QBI

14. **Salary is not QBI.** QBI does not include "reasonable compensation paid to the taxpayer by any qualified trade or business of the taxpayer" ([26 U.S.C. 199A(c)(4)(A)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVI-sec199A.htm)). The S corporation's QBI is profit less salary, less the employer payroll tax, less the added costs. The sole proprietor's QBI is profit less the deductible half of self-employment tax and other deductions attributable to the business (`us-qbi-deduction`).
15. **Below the QBI threshold** (taxable income under the 2026 amount in `us-qbi-deduction`), the deduction is 20% of QBI, capped at 20% of taxable income less net capital gain. The S corporation usually lowers it, because the salary leaves QBI. Price that at the marginal rate (Case 1).
16. **Above the threshold**, the deduction for a non-SSTB is limited by W-2 wages and property. The owner's salary is W-2 wages ([26 U.S.C. 199A(b)(4)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVI-sec199A.htm)), so for a high earner with no staff and no property the S corporation can restore a deduction that is zero as a sole proprietor. For an SSTB above the phase-in range, no QBI deduction is left either way. Run both cases in `us-qbi-deduction`; never assume QBI favours the S corporation.
17. **Other income tax differences** are small and go the same way in both columns: the deductible half of self-employment tax against the deductible employer payroll tax. Count them only if the reviewer asks.

### Step 6: the deadline

18. **Timely election** ([26 U.S.C. 1362(b)(1)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapS-partI-sec1362.htm)): "at any time during the preceding taxable year, or ... on or before the 15th day of the 3d month of the taxable year". The instructions count it as 2 months and 15 days from the day the year begins: a corporation whose first year begins 7 January must file by 21 March (Instructions for Form 2553, Example 1). An election made in that window is pushed to the next year if, on any earlier day of the year, the entity was not eligible or a then-shareholder did not consent (1362(b)(2)). An election made after the window applies from the next year (1362(b)(3)).
19. **For 2026 and 2027.** An existing calendar-year entity had until **16 March 2026** for 2026 (15 March was a Sunday; 26 U.S.C. 7503 moves the day to the next business day). It can file at any time now, until **15 March 2027**, for 2027. A new entity formed in 2026 or 2027 counts its 2 months and 15 days from the earliest of: first having shareholders, first having assets, or beginning business (Instructions for Form 2553, item E).
20. **Late election for 2026: Rev. Proc. 2013-30.** All of these must hold ([Rev. Proc. 2013-30, sections 4.02 and 5](https://www.irs.gov/pub/irs-drop/rp-13-30.pdf); Instructions for Form 2553, Relief for Late Elections):
    - the entity intended to be an S corporation as of the effective date entered on line E;
    - it fails to qualify solely because Form 2553 was not filed on time;
    - it has reasonable cause and acted diligently to correct the mistake once found (stated on line I of Form 2553 or an attached statement);
    - Form 2553 is filed within 3 years and 75 days of the line E date; and
    - every person who was a shareholder in that period gives a statement that they reported income consistently with the S election for that year and all later years (column K does this).
    Write "FILED PURSUANT TO REV. PROC. 2013-30" at the top of page 1. For an LLC, the same procedure also covers the late corporate classification election, and the entity must also have filed every Form 1120-S consistently (or the first one must not yet be due). A corporation (not an LLC) past 3 years and 75 days can still get relief if it and every shareholder filed as an S corporation from the start, at least 6 months have passed since the first Form 1120-S, and the IRS raised no problem within 6 months of that return (section 5.04). Otherwise the only route is a private letter ruling with a user fee.
21. **A decision made late in 2026 is not intent from 1 January.** Relief is for a business that meant to be an S corporation and missed the filing. A business that decides in November 2026 to look back has no reasonable cause, and in any case paid no salary during 2026: the brief recommends 2027 instead, unless there is evidence of the earlier intent (refusal code R-SC-LATE).
22. **Filing.** Send the signed original or fax it to the service center listed for the entity's state in the Instructions for Form 2553; keep proof. The IRS should answer within 60 days; if nothing comes within 2 months, call 1-800-829-4933.

### Step 7: decide and write the brief

23. **Net annual saving** = sole proprietor self-employment tax less S corporation payroll tax, less added costs, less (or plus) the income tax change from Step 5. Recommend the election only when the net saving is clearly positive at a salary the evidence supports, for profit the client expects to keep earning. When it is small or rests on a low salary, say "marginal", and say what would change it.
24. Also in the brief: state flags (below), the loss of Social Security earnings record on the salary gap (flag, do not compute), retirement contribution room under each structure (`us-self-employed-retirement`), and that revoking later bars a new election for five years.

### State entity-level taxes (flag only; figures in the state skill)

| State | What to flag | Skill |
| --- | --- | --- |
| California | An S corporation owes California tax at entity level as well as the shareholder's personal tax; compare it with the LLC fee and tax the LLC pays now | `ca-llc-fee-and-tax`; no OpenAccountants skill yet holds the California S corporation rate (refer) |
| New York State | A federal S corporation is taxed as a New York C corporation unless it also makes the New York S election | `ny-corporate-franchise-article-9a` |
| New York City | The city does not recognise S status: a sole proprietor pays the unincorporated business tax, an S corporation pays the city's business corporation tax | `nyc-ubt`, `nyc-unincorporated-business-tax` |
| New Hampshire | Business profits tax and business enterprise tax apply to the entity | `nh-bpt-bet` |
| New Jersey | A federal S corporation must also elect New Jersey S status, or it is taxed as a New Jersey C corporation | `nj-cbt-and-bait` |
| Texas | Franchise (margin) tax applies to the LLC whether or not it elects S status; check the no-tax-due threshold | `tx-franchise-tax`, `tx-margin-tax` |
| Tennessee | Franchise and excise tax applies to LLCs and corporations alike | no OpenAccountants skill yet (refer) |
| Every state | State unemployment insurance on the new salary; some states require workers' compensation for an owner-employee | `us-state-payroll-matrix` |

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Sole proprietor with no entity | Must form an LLC or corporation first; the election runs from the later of formation and the effective date chosen |
| Profit low, or close to a reasonable salary | Little or no gap to save on; fixed costs usually exceed the saving. Recommend against |
| Profit swings widely between years | The costs recur in the low years; compare at least two years, including a low one |
| Owner's other W-2 wages at or above USD 184,500 | Sole proprietor pays only 2.9%; the S corporation adds a non-refundable employer 6.2% on salary. Usually recommend against (Case 2) |
| Other wages below the base but wages plus profit above it | Recompute line 9 of Schedule SE; the 12.4% saving applies only to the base left |
| Owner's spouse also works in the business | Each spouse who works needs a salary and payroll; a qualified joint venture (two Schedules C) must first become one entity |
| Business with staff or substantial equipment | Stronger case for a salary below profit, because part of the receipts come from others' work or capital |
| High income, non-SSTB, no staff, no property, above the QBI phase-in | Salary creates W-2 wages that can restore the QBI deduction; run both cases in `us-qbi-deduction` |
| SSTB fully above the QBI phase-in | No QBI deduction either way; decision rests on payroll tax and costs |
| Substantial qualified property (high UBIA) | The property prong may already support the QBI deduction as a sole proprietor; the S corporation's wages add less |
| Election effective mid-year (new LLC) | Short years: Schedule C before the effective date, Form 1120-S after; prorate salary, savings and costs |
| Losses expected | S corporation losses are limited by stock and debt basis (loans must be from the shareholder directly), at-risk and passive rules; a sole proprietor's loss flows straight to Schedule C |
| Owner plans to sell the business | S corporation sale (stock or assets) is more complex; refer before electing |
| Several businesses | Each S corporation is its own payroll and Form 1120-S |
| Health insurance paid for the owner | For a more-than-2% shareholder it goes on the W-2 as wages, but is not Social Security or Medicare wages if under a plan (IRS compensation page); see `us-self-employed-health-insurance` |
| Solo 401(k) or SEP | Employer contributions are based on salary, not on profit; a low salary cuts the room (`us-self-employed-retirement`) |
| Spouse is a nonresident alien | The spouse must not hold shares (1361(b)(1)(C)); check community property states, where the spouse may own shares by law |
| Existing S election, income has dropped | Revocation needs consent of shareholders holding more than half the shares; made by the 15th day of the 3rd month it is effective from the 1st day of that year, otherwise from the next year, unless a later date is specified (1362(d)(1)); then no new election for five years (1362(g)) |
| Additional Medicare Tax as the only reason | Not a reason on its own: the 0.9% still applies to salary above the threshold; it saves only on the distribution part |

## Worked cases

**Case 1, a decision: a single consultant with USD 120,000 profit and a USD 70,000 salary.** A single filer, no other income, standard deduction, a non-SSTB business in a state with no entity-level tax on S corporations. 2026 profit before any owner pay is USD 120,000. Market data supports a salary of USD 70,000. Quotes for the added costs (payroll service, Form 1120-S, FUTA and state unemployment) total USD 3,000.

Sole proprietor: net earnings USD 120,000 x 92.35% = USD 110,820, all under the USD 184,500 base; self-employment tax 15.3% = USD 16,955.46; deductible half USD 8,477.73. QBI = USD 111,522.27. Taxable income before QBI: USD 120,000 less USD 8,477.73 less USD 16,100 = USD 95,422.27. QBI deduction: the smaller of 20% of QBI (USD 22,304.45) and 20% of taxable income (USD 19,084.45), so USD 19,084.45. Taxable income USD 76,337.82.

S corporation: FICA on salary USD 70,000 x 15.3% = USD 10,710 (employer half USD 5,355 deducted by the corporation). K-1 income USD 120,000 less 70,000 less 5,355 less 3,000 = USD 41,645, which is the QBI. Taxable income before QBI USD 70,000 plus 41,645 less 16,100 = USD 95,545; QBI deduction 20% of USD 41,645 = USD 8,329. Taxable income USD 87,216.

The decision: payroll tax saved USD 16,955.46 less USD 10,710 = USD 6,245.46. Less added costs USD 3,000. Taxable income is USD 10,878.18 higher with the S corporation, mostly because the salary left QBI; both figures sit in the 22% band (under USD 105,700), so income tax rises USD 2,393.20. Net saving: **USD 852.26 a year**. The election is marginal: recommend it only if profit is expected to grow, or if evidence supports a lower salary. Without the QBI step the saving would have looked like USD 3,245.46, which is the common mistake.

```oa-check
name: S corporation decision, single, profit 120,000, salary 70,000 (2026)
inputs:
  profit: 120000
  salary: 70000
  added_costs: 3000
  standard_deduction: 16100
  marginal_rate: 0.22
steps:
  - se_tax: profit * 0.9235 * 0.153
  - half_se: se_tax * 0.5
  - ti_before_qbi_sp: profit - half_se - standard_deduction
  - qbi_sp: min((profit - half_se) * 0.2, ti_before_qbi_sp * 0.2)
  - taxable_sp: ti_before_qbi_sp - qbi_sp
  - fica: salary * 0.153
  - k1_income: profit - salary - salary * 0.0765 - added_costs
  - ti_before_qbi_s: salary + k1_income - standard_deduction
  - qbi_s: min(k1_income * 0.2, ti_before_qbi_s * 0.2)
  - taxable_s: ti_before_qbi_s - qbi_s
  - payroll_tax_saved: se_tax - fica
  - extra_income_tax: (taxable_s - taxable_sp) * marginal_rate
  - net_saving: payroll_tax_saved - added_costs - extra_income_tax
expected:
  se_tax: 16955.46
  qbi_sp: 19084.45
  taxable_sp: 76337.82
  fica: 10710.00
  k1_income: 41645.00
  qbi_s: 8329.00
  taxable_s: 87216.00
  payroll_tax_saved: 6245.46
  extra_income_tax: 2393.20
  net_saving: 852.26
```

**Case 2, a decision: a side business on top of a job above the wage base.** A married couple filing jointly. One spouse earns USD 190,000 of W-2 wages (boxes 3 and 5) from an employer and has a side LLC with 2026 profit of USD 60,000; the other spouse has no income. A reasonable salary for the side work is USD 35,000; added costs are quoted at USD 2,500.

Sole proprietor: net earnings USD 60,000 x 92.35% = USD 55,410. Schedule SE line 9: USD 184,500 less USD 190,000 is below zero, so zero; no 12.4%. Self-employment tax is 2.9% only: USD 1,606.89. Additional Medicare Tax: the USD 250,000 joint threshold less USD 190,000 of wages leaves USD 60,000, above USD 55,410, so none.

S corporation on a USD 35,000 salary: employer 6.2% plus 1.45% = USD 2,677.50; employee Medicare 1.45% = USD 507.50; employee social security 6.2% = USD 2,170 is withheld but comes back as the excess social security credit on Form 1040, because the job already withheld on the full USD 184,500 (26 U.S.C. 6413(c)). Payroll tax borne USD 3,185. Wages total USD 225,000, under USD 250,000, so no Additional Medicare Tax either. With the added costs: USD 5,685.

The decision: the S corporation costs **USD 4,078.11 more each year** in payroll tax and costs. Below the joint QBI threshold the S corporation's QBI (USD 60,000 less salary, employer tax and costs) is also smaller than the sole proprietor's, so income tax does not rescue it. Recommend against the election.

```oa-check
name: S corporation decision, other wages above the wage base, joint (2026)
inputs:
  profit: 60000
  salary: 35000
  other_wages: 190000
  wage_base: 184500
  added_costs: 2500
steps:
  - line_4a: profit * 0.9235
  - line_9: max(wage_base - other_wages, 0)
  - se_tax: min(line_4a, line_9) * 0.124 + line_4a * 0.029
  - employer_tax: salary * 0.0765
  - employee_medicare: salary * 0.0145
  - employee_ss_withheld: salary * 0.062
  - employee_ss_credited: min(employee_ss_withheld, max(other_wages + salary - wage_base, 0) * 0.062)
  - scorp_payroll_tax: employer_tax + employee_medicare + employee_ss_withheld - employee_ss_credited
  - scorp_total: scorp_payroll_tax + added_costs
  - extra_cost_of_election: scorp_total - se_tax
expected:
  line_4a: 55410.00
  se_tax: 1606.89
  employer_tax: 2677.50
  employee_ss_credited: 2170.00
  scorp_payroll_tax: 3185.00
  scorp_total: 5685.00
  extra_cost_of_election: 4078.11
```

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-SC-INELIG | An owner is a nonresident alien, a partnership, a corporation or an ineligible trust; more than 100 shareholders; or more than one class of stock | Refuse: no S election is possible; refer the structure question |
| R-SC-MULTI | Multi-member LLC or partnership converting | Refer: `us-form-1065-partnership` and a reviewer; different rules |
| R-SC-CCORP | Existing C corporation electing S status | Refer: built-in gains tax (26 U.S.C. 1374) and earnings and profits issues are outside this skill |
| R-SC-ZEROSAL | Client wants no salary or a token salary while working in the business | Refuse to recommend it: the IRS reclassifies distributions as wages (IRS compensation page and cases above) |
| R-SC-LATE | Late 2026 election without evidence of intent from the effective date, or past 3 years and 75 days | Refer: Rev. Proc. 2013-30 may not apply; a private letter ruling has a user fee; usually elect for the next year instead |
| R-SC-REVOKE | Existing election to be revoked | Refer for full analysis before acting: the five-year bar (1362(g)) makes it hard to undo |
| R-SC-SALE | Business sale planned within a few years | Refer: S corporation sale mechanics |
| R-SC-STATE | California S corporation tax, Tennessee franchise and excise tax, or any state without an OpenAccountants skill | Flag and refer; do not put a state figure in the brief without the state source |
| R-SC-SSA | Client asks how much Social Security benefit they lose | Flag only: benefit projections are outside this skill |

The skill never chooses "the" salary on its own, never guarantees a saving, never files Form 2553, and never treats the QBI effect as always favouring the S corporation.

## Filing and payment

- **Form 2553** for 2027: any time up to **15 March 2027** for an existing calendar-year entity; a new entity within 2 months and 15 days of the start of its first year. Signed by an officer and consented to by every shareholder (column K). Sent to the service center or fax number for the entity's state listed in the [Instructions for Form 2553](https://www.irs.gov/pub/irs-pdf/i2553.pdf). A late election under Rev. Proc. 2013-30 can be filed alone or attached to a Form 1120-S, with the headings above.
- **After acceptance:** payroll from the first month, Form 941 quarterly and Form 940 yearly (`us-form-941-940-payroll`), Forms W-2 by 31 January, and Form 1120-S with Schedules K-1 by the 15th day of the 3rd month after the year ends (15 March 2028 for 2027; extension by Form 7004, see `us-corporate-extension-form-7004-and-the`).
- **The owner's own tax:** the salary is withheld through payroll; K-1 income still needs estimated tax (`us-quarterly-estimated-tax`).

## Completion checklist

- Entity exists and passes every 1361(b)(1) test; every shareholder can consent.
- Salary chosen from evidence (duties, hours, market data, source of receipts), with the evidence named in the brief.
- Self-employment tax computed with the owner's other wages on Schedule SE line 8a.
- S corporation payroll tax at that salary, with the employer share counted in full when other wages pass USD 184,500.
- Added costs from quotes, every year, including state items.
- QBI computed both ways in `us-qbi-deduction`, priced at the marginal rate.
- State flags from the table, each sent to its state skill.
- Deadline stated: 15 March 2027 for 2027, or a new entity's 2 months and 15 days; Rev. Proc. 2013-30 tested before any late 2026 election.
- Recommendation with confidence level and what would change it.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Instructions for Form 2553 (Rev. December 2020). Read for Who May Elect (tests 1 to 8), When To Make the Election (2 months and 15 days, Examples 1 to 3), Relief for Late Elections (both lists, the "FILED PURSUANT TO REV. PROC. 2013-30" heading, the 3 years and 75 days and 6-month rules), Where To File, and the 60-day and 2-month follow-up. | https://www.irs.gov/pub/irs-pdf/i2553.pdf | 2026-11-13 |
| Form 2553 (Rev. December 2017). Read for line E (effective date), line I (reasonable cause declaration) and column K (consents). | https://www.irs.gov/pub/irs-pdf/f2553.pdf | 2026-11-13 |
| Rev. Proc. 2013-30. Read for section 4.02 (intent, 3 years and 75 days, solely late filing, reasonable cause and diligence) and section 5 (Form 2553 signatures, shareholder statements, section 5.04 relief where all returns were filed as an S corporation). | https://www.irs.gov/pub/irs-drop/rp-13-30.pdf | 2026-11-13 |
| IRS, S corporation compensation and medical insurance issues. Read for the reasonable compensation rule, the cases listed, the sources-of-receipts test, the factors, and the more-than-2% shareholder health insurance treatment. | https://www.irs.gov/businesses/small-businesses-self-employed/s-corporation-compensation-and-medical-insurance-issues | 2026-11-13 |
| IRS Pub. 15 (2026). Read for the social security wage base ($184,500), the 6.2% and 1.45% rates and the S corporation officer row in the special classes table. | https://www.irs.gov/pub/irs-pdf/p15.pdf | 2026-11-13 |
| Schedule SE (Form 1040) 2026. Read for line 4a (92.35%) and lines 7 to 9. | https://www.irs.gov/pub/irs-pdf/f1040sse.pdf | 2026-11-13 |
| IRS, self-employment tax page. Read for the 15.3% total rate. | https://www.irs.gov/businesses/small-businesses-self-employed/self-employment-tax-social-security-and-medicare-taxes | 2026-11-13 |
| IRS, Additional Medicare Tax questions and answers. Read for the $125,000 married filing separately threshold. | https://www.irs.gov/businesses/small-businesses-self-employed/questions-and-answers-for-the-additional-medicare-tax | 2026-11-13 |
| Rev. Proc. 2025-32. Read for the 2026 single standard deduction ($16,100) and the single 22% band (to $105,700). | https://www.irs.gov/pub/irs-drop/rp-25-32.pdf | 2026-11-13 |
| 26 U.S.C. 1401 (govinfo). Read for (a) 12.4 percent, (b)(1) 2.9 percent, (b)(2) 0.9 percent and the thresholds. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap2-sec1401.htm | 2026-11-13 |
| 26 U.S.C. 1361 (govinfo). Read for (b)(1)(A) to (D): 100 shareholders, eligible shareholders, no nonresident alien, one class of stock. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapS-partI-sec1361.htm | 2026-11-13 |
| 26 U.S.C. 1362 (govinfo). Read for (b)(1) to (5) timing and late-election authority, (d)(1) revocation and (g) the five-year bar. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapS-partI-sec1362.htm | 2026-11-13 |
| 26 U.S.C. 199A (govinfo, 2024 edition). Read for (a) the taxable income cap, (b)(2) the 20 percent, (b)(4) W-2 wages and (c)(4) reasonable compensation excluded from QBI. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVI-sec199A.htm | 2026-11-13 |
| Public Law 119-21, section 70105. Read for the replacement of 199A(i) (the old end date) by the minimum deduction, which makes the deduction permanent, and the wider phase-in. | https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm | 2026-11-13 |
| 26 U.S.C. 6413(c) (govinfo). Read for the credit or refund of employee social security tax withheld by more than one employer above the base. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap65-subchapB-sec6413.htm | 2026-11-13 |
| 26 U.S.C. 7503 (govinfo). Read for the next-business-day rule (16 March 2026). | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap77-sec7503.htm | 2026-11-13 |

Not yet confirmed: the private letter ruling user fee in Rev. Proc. 2026-1 (the IRS PDF link did not open, so no amount is given); the California S corporation tax rate and minimum tax (no state skill and not read here); IRS Fact Sheet FS-2008-25 (not opened; the IRS compensation page is used instead); the rows of the state table are flags taken from the named state skills, not read at the state source here, and the Tennessee row has no state skill behind it; Treas. Reg. 301.7701-3(c)(1)(v)(C) is cited as named in the Form 2553 instructions, not read on eCFR.
