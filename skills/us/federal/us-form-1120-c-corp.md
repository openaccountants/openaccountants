---
name: us-form-1120-c-corp
description: >
  Prepare the working papers for a domestic C corporation's 2026 Form 1120.
  Covers the regular corporate tax computation, dividends-received deductions,
  losses, interest, domestic and foreign research costs, section 250, CAMT,
  BEAT screening, estimated tax, filing schedules, officer compensation and
  LLC classification elections. Includes recomputing domestic, research-election,
  multinational, loss, interest and CAMT examples. Use with the US tax workflow
  base and route consolidated returns and specialized corporate regimes
  separately.
jurisdiction: US
category: federal
domain: tax
type: computation
tax_year: 2026
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
last_updated: 2026-11-13
version: 1.0
---

# US Form 1120 C corporation v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

**Circular 230 disclosure:** Written tax advice must use reasonable factual and legal assumptions, establish the relevant facts, consider all relevant circumstances and apply the law to those facts. It cannot rely on the chance that a return escapes audit or that an issue will not be raised. [31 CFR 10.37(a)](https://www.ecfr.gov/current/title-31/section-10.37).

**Coverage:** tax years beginning in 2026, with transition rules explicitly identified. Built from the law; no professional approval is asserted for this version. Load with `us-tax-workflow-base`. The output is a reconciled computation and filing checklist for professional review.

**Form-version control:** the IRS Form 1120 instructions available and read on 2026-11-13 are the **2025** instructions. References to their page-one lines and schedules below identify that published layout, not an assertion that the final 2026 form is identical. Apply the current statutes and 2026 inflation figures here; before filing, obtain the final form and instructions for the actual return year and remap every line and attachment. [IRS Form 1120](https://www.irs.gov/forms-pubs/about-form-1120).

## Who this applies to

A domestic C corporation generally files Form 1120 even if it has no taxable income, is inactive, or is in bankruptcy. This includes an eligible **domestic** LLC classified as an association taxable as a corporation, unless a valid S election or another specialized filing regime applies. Domestic status ordinarily follows creation or organization in the United States or under US or state law. A foreign-organized entity's Form 8832 election changes its federal entity classification; it does not by itself make the entity domestic. [Form 1120 instructions, Who Must File](https://www.irs.gov/instructions/i1120); [IRC 7701(a)(4)-(5)](https://uscode.house.gov/us/usc/t26/s7701/).

| Facts | Treatment and boundary |
|---|---|
| Ordinary standalone domestic C corporation, calendar or fiscal year | Apply this computation; obtain prior returns, accounting method, opening tax attributes and a complete trial balance. |
| Parent and subsidiaries considering or filing a consolidated return | Route for consolidated-return analysis. The affiliated-group ownership test generally requires at least 80% voting power **and** value, with excluded entities and stock rules. Do not consolidate merely because the accounts are consolidated. [IRC 1504(a)-(b)](https://uscode.house.gov/us/usc/t26/s1504/). |
| S corporation or proposed S election | Use the S corporation and election-decision guides. Do not put an S corporation's ordinary income through the C corporation tax calculation. |
| Personal service corporation | Form 1120 may apply, but required tax-year and special compensation/distribution rules need separate review. |
| Personal holding company | Evaluate Schedule PH and the separate personal holding company tax. Ordinary income tax alone is incomplete. |
| Exempt organization, REIT, RIC, cooperative, insurer, FSC or REMIC | Establish the applicable specialized return, including Form 990/990-T, 1120-REIT, 1120-RIC, 1120-C, 1120-L, 1120-PC, 1120-FSC or 1066. |
| Foreign corporation with US activity or income | Evaluate Form 1120-F, effectively connected income, treaty protection and any protective return. |
| Foreign-owned US disregarded entity | Consider a **pro forma** Form 1120 with Form 5472 under its special rules; this does not convert the entity into a C corporation for general income-tax purposes. |
| Foreign ownership, subsidiaries, branches or related-party payments | Complete the cross-border screen below; information reporting can be required even when income tax is zero. |
| State or local corporation tax | Use the relevant state guide. Federal elections, research deductions, losses and depreciation do not establish state conformity. |

The specialized-return boundaries above follow [Form 1120 instructions, Who Must File and Other Forms and Statements](https://www.irs.gov/instructions/i1120).

### Tax year and first corporate year

Establish the actual start and end dates, including short years, before computing deductions or due dates. A corporation may generally use an allowable calendar, fiscal or 52-53-week year. Personal service corporations have a required year unless an exception applies; review Forms 1128 and 8716 and any section 280H consequences instead of assuming a free fiscal-year choice. [Form 1120 instructions, Accounting Period](https://www.irs.gov/instructions/i1120).

For an eligible LLC's Form 8832 election:

- The specified effective date ordinarily may be no more than **75 days before filing** or **12 months after filing**. Evaluate late-election relief separately; it is not automatic.
- A classification change generally prevents another elective classification change for **60 months**. The regulation contains exceptions, including an initial election effective on formation and specified permission cases.
- A disregarded entity electing association status is deemed to contribute its assets and liabilities to the corporation for stock. A partnership electing association status is deemed to contribute its assets and liabilities for stock and then liquidate by distributing that stock to its partners. These are not interchangeable descriptions.
- Test the deemed transactions under the applicable Code provisions, including sections 351 and 357; liabilities, built-in gains, ownership and basis can prevent a wholly tax-free result. Reconcile the closing pre-election books and opening corporate tax basis.
- Attach the required copy of Form 8832 to the applicable return and retain the IRS election evidence. Determine the EIN requirement from the entity's actual continuity and formation facts rather than assuming every election needs a new EIN.

[26 CFR 301.7701-3(c)(1), (g)(1)-(3)](https://www.ecfr.gov/current/title-26/section-301.7701-3).

For a qualifying deemed section 351 transfer, corporate basis generally carries over with recognized-gain adjustments, and holding-period tacking follows section 1223. The individual's pre-election losses remain the individual's and do not become corporate NOLs. [IRC 362(a)](https://uscode.house.gov/us/usc/t26/s362/); [IRC 1223(1)-(2)](https://uscode.house.gov/us/usc/t26/s1223/); [IRS single-member LLC treatment](https://www.irs.gov/businesses/small-businesses-self-employed/single-member-limited-liability-companies).

An existing entity keeps its EIN after classification changes: "Any entity that has an EIN will retain that EIN". If it never had its own EIN, obtain one instead of using the owner's identifier. The IRS may permit another classification election within 60 months if "more than 50%" of interests are held by persons with no interest at the prior election's effective or filing date; initial elections effective on formation are excepted. [Form 8832 instructions, page 6](https://www.irs.gov/pub/irs-pdf/f8832.pdf); [26 CFR 301.7701-3(c)(1)(iv)](https://www.ecfr.gov/current/title-26/section-301.7701-3).

## Rates, bands and thresholds

These are federal rules for the stated period. A threshold is usable only with its adjacent conditions.

| Item | Amount and period | Conditions and official source |
|---|---|---|
| Regular corporate income tax | **21%**, 2026 | Applies to taxable income under section 11; credits, CAMT and other taxes are separate. [IRC 11(b)](https://uscode.house.gov/us/usc/t26/s11/). |
| Domestic dividends-received deduction (DRD) | Generally **50%**, **65%**, or qualifying **100%**, 2026 | 65% requires at least 20% vote and value; 100% requires the qualifying affiliated-dividend or other statutory category, not ownership alone. Holding periods and limitations apply. [IRC 243(a)-(c)](https://uscode.house.gov/us/usc/t26/s243/). |
| Post-2017 NOL deduction | Generally **80%** of the applicable modified taxable-income base; indefinite carryforward | Use pre-2018 NOLs first; special farming and insurance rules remain. [IRC 172(a)-(b)](https://uscode.house.gov/us/usc/t26/s172/). |
| Business interest limitation | Business interest income + **30%** of adjusted taxable income (ATI) + floor-plan financing interest | Exempt trades/businesses, aggregation, carryforwards and 2026 changes require the analysis below. [IRC 163(j)](https://uscode.house.gov/us/usc/t26/s163/); [Form 8990 instructions](https://www.irs.gov/instructions/i8990). |
| Small-business gross-receipts test | Prior **3-year** average annual gross receipts **not over $32 million**, years beginning in 2026 | Apply section 448(c) aggregation and special-period rules. A tax shelter does not qualify for the section 163(j) small-business exception merely because receipts are small. [Rev. Proc. 2025-32, section 4.30](https://www.irs.gov/irb/2025-45_IRB); [Form 8990 instructions](https://www.irs.gov/instructions/i8990). |
| Section 179 election | Maximum **$2,560,000**; phaseout begins when qualifying property cost exceeds **$4,090,000**, years beginning in 2026 | Eligible property, investment phaseout, business-income limit, aggregation and carryforward rules apply; separate vehicle restrictions remain. [Rev. Proc. 2025-32, section 4.24](https://www.irs.gov/irb/2025-45_IRB). |
| Domestic research | Current deduction by default; elective amortization over **at least 60 months** | Section 174A applies for years beginning after 2024; elective amortization begins with the first month benefits are realized. [IRC 174A(a)-(c) and effective-date notes](https://uscode.house.gov/us/usc/t26/s174A/). |
| Foreign research | Capitalize and amortize over **15 years**, beginning at the year's midpoint | Research location controls; software development is included. [IRC 174(a)-(c)](https://uscode.house.gov/us/usc/t26/s174/). |
| Section 250 deduction | **33.34%** of FDDEI; **40%** of NCTI plus its related section 78 gross-up, years beginning in 2026 | Apply eligibility, expense-allocation and taxable-income limitation rules. The old 37.5%/50% rates do not govern a 2026-start year. [IRC 250(a)-(b) and 2025 amendment notes](https://uscode.house.gov/us/usc/t26/s250/). |
| Corporate charitable gifts | **1% floor** and **10% ceiling** of statutory modified taxable income, years beginning after 2025 | Below-floor amounts do not automatically carry forward. Apply section 170(d)(2) and special contribution categories. [IRC 170(b)(2), (d)(2)](https://uscode.house.gov/us/usc/t26/s170/). |
| CAMT | **15%** of AFSI less the corporate AMT foreign tax credit, before comparison with regular tax plus BEAT | Applicable-corporation test generally uses prior **3-year** average AFSI **over $1 billion**; a foreign-parented multinational has the additional **$100 million or more** corporation-side test. [IRC 55(b)(2)](https://uscode.house.gov/us/usc/t26/s55/); [IRC 59(k)](https://uscode.house.gov/us/usc/t26/s59/). |
| CAMT financial statement NOL deduction | Lesser of available FSNOL carryovers or **80%** of pre-FSNOL AFSI | Only qualifying financial statement losses, with the statutory adjustments, enter this separate attribute ledger. [IRC 56A(d)](https://uscode.house.gov/us/usc/t26/s56A/). |
| BEAT | **10.5%**, years beginning after 2025; specified bank/securities groups add **1 percentage point** | Screen average annual gross receipts of at least **$500 million** over the prior **3 years** and base-erosion percentage at least **3%**, or **2%** for specified bank/securities groups. Aggregation, exclusions and credit adjustments apply. [IRC 59A(b), (e)](https://uscode.house.gov/us/usc/t26/s59A/). |
| Estimated-tax trigger and ordinary installments | Expected tax **$500 or more**; ordinarily **25%** of required annual payment per installment | Apply corporate prior-year and large-corporation restrictions below. [Form 2220 instructions, Who Must File and Required Annual Payment](https://www.irs.gov/instructions/i2220). |
| Form 1125-E | Total receipts **$500,000 or more**, **and** an officer-compensation deduction | Attach when both conditions apply; use the form's definition of receipts. [Form 1125-E instructions](https://www.irs.gov/instructions/i1125e). |
| Schedules L, M-1 and M-2 small-return exception | Both total receipts and year-end assets **less than $250,000** | Complete the corresponding Schedule K answer; equality at the threshold fails the exception. [Form 1120 instructions, Schedules L and M-1](https://www.irs.gov/instructions/i1120). |
| Schedule M-3 | Year-end assets **$10 million or more** | Required filers below **$50 million**, and voluntary filers, may use Part I plus M-1 instead of M-3 Parts II and III. These categories also have the Schedule B exception. [Schedule M-3 instructions, Who Must File and Schedule B](https://www.irs.gov/instructions/i1120sm3). |
| Schedule UTP | Assets **$10 million or more**, plus audited statements and reportable tax positions | Apply all conditions, including the related-party statement rules; size alone is insufficient. [Form 1120 instructions, Schedule K question 14](https://www.irs.gov/instructions/i1120). |
| Electronic filing | Generally **10 or more** returns of any type during the calendar year | Aggregate relevant income, employment, excise and information returns. Hardship waivers and religious exemptions have their own procedures; there is no additional asset minimum. [Form 1120 instructions, Electronic Filing](https://www.irs.gov/instructions/i1120). |

Source wording checks: section 11(b) says “21 percent”; section 250(a)(1)(A) says “33.34 percent”; section 250(a)(1)(B) says “40 percent”; section 59A(b)(1)(A) says “10.5 percent”; and Rev. Proc. 2025-32 section 4.30 states “$32,000,000.” Each amount above is applied with its statutory base and effective period.

## The base

### Build the return from the books

Do not multiply net book income by the tax rate. Start with a reconciled trial balance, separate permanent and timing differences, and retain schedules that reproduce each tax adjustment. The published 2025 Form 1120 uses page-one line 11 for total income, line 27 for deductions before NOL and special deductions, line 28 for the resulting subtotal, lines 29a/29b for NOL/special deductions and line 30 for taxable income. Use those labels to map the finalized 2026 form. [Form 1120 instructions, Income and Deductions](https://www.irs.gov/instructions/i1120).

1. Reconcile gross receipts, returns and allowances to the sales ledger. Compute inventory and cost of goods sold on Form 1125-A where applicable, applying inventory-method and capitalization rules. Gross profit is net sales less tax COGS, not total cash receipts.
2. Bring dividends and inclusions through Schedule C; separately identify interest, rents, royalties, capital gains, Form 4797 business-property gains and other taxable income. Identify tax-exempt interest for the book reconciliation instead of including it as ordinary taxable interest.
3. Classify recoveries. A refund of previously deducted state tax may produce taxable income under the tax-benefit rule; a federal income-tax refund is not automatically taxable income when the tax was nondeductible. Refund interest is separately considered.
4. Deduct ordinary and necessary costs only when allowable under the accounting method and substantive rule. Check salaries/officer compensation, repairs, rents, taxes, interest, bad debts, depreciation, depletion, retirement plans and benefits. Capital expenditures and section 263A costs belong in the proper basis or inventory account.
5. Reconcile related-party accruals under section 267, reserve-based book bad debts versus tax write-offs, federal income-tax expense, penalties, lobbying, entertainment, meals and other nondeductible items. Ordinary qualifying non-entertainment business meals are generally **50%** deductible; an employee must be present and the expense must not be lavish. Other categories and post-2025 employer-provided meal restrictions need their own section 274 analysis. [Form 1120 instructions, Other Deductions](https://www.irs.gov/instructions/i1120); [IRC 274](https://uscode.house.gov/us/usc/t26/s274/).
6. Compute the separate interest, research, charitable-gift, NOL and special-deduction limitations below in their prescribed order. A single generic “taxable income” figure is not the base for every limitation.
7. Compute regular tax, then applicable credits, CAMT, BEAT and other taxes through Schedule J. Reconcile estimated payments, credits carried forward, extension payments and withholding to payment records. Determine balance due, refund or election to apply an overpayment to the next year. Do not reuse old page-one payment line numbers without checking the final form.

Coordinate section 280C(a) wage/salary deduction reductions for applicable employment credits, including section 51. [IRC 280C(a)](https://uscode.house.gov/us/usc/t26/s280C/).

File Form 7205 when claiming section 179D: the instructions say "must file Form 7205 to claim the deduction". [Form 7205 instructions, Who Must File](https://www.irs.gov/instructions/i7205).

Use Form 4562 for applicable depreciation, section 179 and amortization. Determine acquisition, binding-contract, placed-in-service, business-use and election facts before choosing bonus depreciation; transition property can differ from newly acquired property. Section 179D also needs construction-start evidence: the deduction terminates for property whose construction begins **after June 30, 2026**. [Form 1120 instructions, Depreciation and Other Deductions](https://www.irs.gov/instructions/i1120); [Rev. Proc. 2025-32, section 2.11](https://www.irs.gov/irb/2025-45_IRB).

### Dividends-received deduction

Keep the gross dividend, payor classification, ownership percentage, holding-period evidence and deduction category together.

- For an eligible domestic dividend, use the applicable section 243 rate from the table. Qualifying affiliated dividends require the statutory group, earnings-and-profits and election conditions; an 80%-owned investment alone does not establish the full deduction.
- Section 246(c) generally requires holding the shares for **more than 45 days** during the **91-day** period beginning **45 days before** the ex-dividend date. For specified preferred dividends attributable to periods totaling more than **366 days**, substitute **90** and **181 days**, with the window beginning **90 days before** the ex-dividend date. Count only qualifying risk-bearing holding days. [IRC 246(c)](https://uscode.house.gov/us/usc/t26/s246/).
- Debt-financed portfolio stock can reduce the deduction under section 246A. Certain public-utility preferred dividends use special Schedule C percentages rather than the ordinary tiers. Foreign dividends require section 245 or 245A analysis; neither a CFC inclusion nor every foreign dividend is an ordinary domestic DRD. [Form 1120 instructions, Schedule C](https://www.irs.gov/instructions/i1120).
- Apply section 246(b)'s ordered, aggregate taxable-income limitations using the Schedule C worksheet. Do not independently multiply the same taxable-income figure by each DRD percentage and add the results. The higher-percentage tier is evaluated first, with the statutory adjustment for the lower tier. Check the NOL exception to the income limitation. [IRC 246(b)](https://uscode.house.gov/us/usc/t26/s246/).

A simple unlimited case: eligible dividends of $100,000 in the ordinary lower tier, $200,000 in the qualifying higher tier and $500,000 of fully qualifying affiliated dividends produce $50,000 + $130,000 + $500,000 = **$680,000** of DRD, assuming sufficient modified taxable income and all holding-period and other requirements. These are illustrative facts, not alternative ownership tests.

Eligible public-utility preferred dividends use the special "23.3% deduction" for the less-than-20%-owned category or "26.7% deduction" for the 20%-or-more-owned category; apply their conditions separately. [Form 1120 instructions, Schedule C lines 4-5](https://www.irs.gov/instructions/i1120).

Section 245A can deduct 100% of the foreign-source portion of a dividend from a specified 10%-owned foreign corporation to a domestic corporate US shareholder: "an amount equal to the foreign-source portion of such dividend". Exclusions, hybrid-dividend restrictions and section 246(c)(5) holding/status/risk conditions apply. The holding requirement is more than "365 days" in a "731-day period" beginning 365 days before the ex-dividend date. [IRC 245A(a)-(e)](https://uscode.house.gov/us/usc/t26/s245A/); [IRC 246(c)(5)](https://uscode.house.gov/us/usc/t26/s246/).

### Capital losses, NOLs and ownership changes

Corporate net capital loss does not offset ordinary income. Ordinary corporate capital-loss carrybacks run **3 years** and carryforwards **5 years**, generally as short-term losses, using the earliest available year first. Carrybacks cannot create or increase an NOL. Foreign expropriation losses have special treatment. [IRC 1211(a)](https://uscode.house.gov/us/usc/t26/s1211/); [IRC 1212(a)](https://uscode.house.gov/us/usc/t26/s1212/).

Maintain NOL ledgers by origin year, ownership-change limitation and expiry. Pre-2018 NOLs generally have a **20-year** carryforward and are not subject to the post-2017 percentage limit. Post-2017 NOLs generally carry forward indefinitely; their deduction is limited to the amount in the rates table after the statutory adjustments, including the prior-year bucket ordering. Current ordinary corporate losses generally do not carry back, but farming losses and nonlife insurers have special rules; the **2018-2020** losses had special **5-year** carryback rules. [IRC 172(a)-(b)](https://uscode.house.gov/us/usc/t26/s172/).

Screen every financing, stock issuance, redemption, acquisition and restructuring for section 382. A shift of more than **50 percentage points** among relevant **5% shareholders** over the testing period can cause an ownership change. The ordinary testing period is **3 years**, subject to statutory adjustments. The basic annual limitation is the old loss corporation's value multiplied by the applicable long-term tax-exempt rate; use the rate for the actual change date, not a fixed historical rate. Built-in items, continuity, bankruptcy, short years and unused-limit carryforwards need separate analysis. [IRC 382(a)-(b), (f)-(i)](https://uscode.house.gov/us/usc/t26/s382/).

For eligible recognized built-in gains/losses, the section 382 recognition period is "the 5-year period beginning on the change date"; apply section 382(h), including its limitations. [IRC 382(h)(7)](https://uscode.house.gov/us/usc/t26/s382/).

### Business interest: section 163(j)

First identify the trades or businesses, tax-shelter status, gross-receipts aggregation, prior elections and interest carryforwards. If the small-business exception applies, document the test instead of assuming all small corporations are exempt. Electing real-property and farming businesses generally incur ADS depreciation consequences; the election is a substantive choice. Certain regulated utilities have a statutory exception. [Form 8990 instructions, Who Must File, Exceptions and Definitions](https://www.irs.gov/instructions/i8990).

For an in-scope corporation:

1. Reconcile business interest income, current business interest expense, carryforwards and eligible floor-plan financing interest. Do not treat all book interest as the same category.
2. Compute ATI under section 163(j), excluding the items the statute specifies. Depreciation, amortization and depletion deductions are added back for years beginning after 2024. For years beginning after 2025, applicable US-shareholder CFC inclusions are excluded from ATI; an old EBITDA worksheet that leaves them in can overstate capacity.
3. For years beginning after 2025, include interest otherwise capitalized in the limitation analysis, except interest capitalized under sections 263(g) and 263A(f). Reconcile the capitalization sequence to Form 8990.
4. Apply the limit from the table; deduct allowable interest and maintain disallowed carryforwards. Coordinate section 382 and other restrictions rather than assuming every carryforward is freely usable.

[IRC 163(j), including 2025 amendment notes](https://uscode.house.gov/us/usc/t26/s163/); [Form 8990 instructions, What's New and ATI](https://www.irs.gov/instructions/i8990).

The real-property/farming section 163(j) election is generally irrevocable: "This is an irrevocable election". ADS applies to affected property, including nonresidential real property, residential rental property and qualified improvement property for the real-property election. [Form 8990 instructions, Elections](https://www.irs.gov/instructions/i8990).

### Domestic and foreign research

Identify where the research is conducted, not merely where the corporation is organized or where an invoice is paid. Research and experimental costs include qualifying software development, but do not include every cost labeled “R&D” in the accounts. Equipment acquisition, depreciable property and mineral exploration have separate treatment. Record direct costs, allocations, contractor location and project evidence.

For domestic costs in a 2026-start year, section 174A generally permits a current deduction. Alternatively, elect capitalization and amortization using the table's minimum period, starting with the month benefits are first realized. The election must meet the statutory timing and consistency rules. Foreign research remains subject to section 174 capitalization and midpoint amortization. Disposition, retirement or abandonment of foreign-research property does not itself produce an immediate deduction of the unamortized amount. [IRC 174A(a)-(d)](https://uscode.house.gov/us/usc/t26/s174A/); [IRC 174(a)-(d)](https://uscode.house.gov/us/usc/t26/s174/).

For domestic costs capitalized in years beginning **2022-2024**, inspect the transition choice already made: remaining unamortized costs could be recovered in the first year beginning after 2024 or ratably over that year and the following year. Thus a 2026 computation may include the second transition deduction. The separate retroactive small-business election has its own eligibility, procedural and timing rules; do not present it as an indefinitely available 2026 election. [IRC 174A statutory notes, Transition Rules](https://uscode.house.gov/us/usc/t26/s174A/).

The section 41 research credit and research-cost recovery are different analyses. Form 6765 is used when claiming the credit, not automatically whenever research costs exist. Under section 280C(c), reduce the relevant domestic research deduction or capital account by the credit unless a valid reduced-credit election is made. Reconcile Form 6765, section 174A, tax basis and any method-change statements to prevent double benefit. [IRC 280C(c)](https://uscode.house.gov/us/usc/t26/s280C/).

Without a valid retroactive or transition election, domestic costs capitalized for 2022-2024 continue their original 5-year midpoint amortization schedules. The prior rule required recovery "over a 5-year" period "beginning with the midpoint of the taxable year". [Rev. Proc. 2025-28, section 2.02](https://www.irs.gov/pub/irs-drop/rp-25-28.pdf); [section 174A transition notes](https://uscode.house.gov/us/usc/t26/s174A/).

### Corporate charitable contributions

Compute the section 170 modified taxable-income base separately, using its prescribed exclusions for the charitable deduction, relevant special deductions and carrybacks. For years beginning after 2025, ordinary corporate contributions are deductible only subject to both the floor and ceiling in the table. Do not deduct all gifts below the ceiling without applying the floor.

Track contribution category, payment timing, substantiation, property valuation and carryovers by year. Excess-ceiling amounts generally have a **5-year** carryforward; amounts denied solely by the floor are carried forward only under the statutory rule for a year in which the ceiling is also exceeded. Apply current contributions and carryovers in the required order and coordinate the NOL rule. Special contribution categories can have different treatment. [IRC 170(b)(2), (d)(2)](https://uscode.house.gov/us/usc/t26/s170/); [IRS business-provisions explanation, Corporate Charitable Contributions](https://www.irs.gov/newsroom/understanding-the-working-families-tax-cuts-business-tax-provisions-youtube-video-text-script).

### Officer compensation and distributions

Reasonable compensation for services actually rendered can be deductible; a distribution to shareholders is not transformed into deductible compensation by its label. Document duties, time, comparable pay, company results, approvals, related-party timing and payroll reporting. Conversely, excess compensation can be recharacterized as a distribution. Evaluate shareholder-level tax and employment-tax consequences separately from the corporate rate. [IRC 162(a)(1)](https://uscode.house.gov/us/usc/t26/s162/).

Prepare Form 1125-E when the dual conditions in the table are met, including officer identities, ownership, time devoted, compensation and amounts included elsewhere to avoid double deduction. For a publicly held corporation, section 162(m) generally limits the deduction for remuneration to a covered employee to **$1 million**. For 2026, covered employees include the principal executive and financial officers, the other "3 highest compensated officers" under the statutory reporting test, and prior covered employees of the corporation or predecessor from years beginning "after December 31, 2016". New controlled-group remuneration aggregation applies for years beginning after 2025; do not give each payer an independent full limit. The expansion to the next **5** highest-compensated employees starts with years beginning after 2026, not the ordinary 2026 year. [Form 1125-E instructions](https://www.irs.gov/instructions/i1125e); [IRC 162(m)(1)-(3), (7) and effective-date notes](https://uscode.house.gov/us/usc/t26/s162/).

For change-in-control payments, route section 280G excess-parachute deductibility and section 4999 recipient excise-tax analysis separately. A compensation deduction on the trial balance does not resolve either rule. [Form 1120 instructions, Limitations on Deductions](https://www.irs.gov/instructions/i1120).

The recipient generally owes a separate 20% excise tax on an excess parachute payment: "a tax equal to 20 percent of the amount of such payment". [IRC 4999(a)](https://uscode.house.gov/us/usc/t26/s4999/).

### Schedules, attachments and reconciliation

Apply the return-year instructions to each trigger; do not attach every form merely because it appears in this table.

| Schedule/form | Work to complete |
|---|---|
| Schedule C | Reconcile gross dividends and inclusions, DRD categories, section 250 and other special deductions. Carry the gross and deduction totals separately to page one. |
| Schedule J | Compute regular income tax, applicable credits, CAMT, BEAT and other tax; reconcile payments and refundable credits. Keep tax liability separate from payment credits. |
| Schedule K | Answer ownership, accounting method, related-party, foreign activity, reporting, size and other questions from evidence. These answers drive additional schedules. |
| Schedules L and M-2 | Balance sheet and retained-earnings reconciliation per books unless the stated small-return exception applies. Assets must equal liabilities plus equity; explain distributions, capital contributions and prior-period adjustments. |
| Schedule M-1 | Reconcile book income to the return subtotal **before** the NOL and special deductions. Add back federal income-tax expense once, handle timing/permanent differences, and reconcile the endpoint. Do not deduct section 250 or the DRD here if it is already a later special deduction. |
| Schedule M-3 | Apply the asset test and permitted Part I/M-1 alternative above. Distinguish permanent and temporary differences and document the financial statements used. |
| Schedule B (Form 1120) | Additional information for required M-3 filers, with the below-$50-million and voluntary-filer exceptions stated above. It is not a universal 1120 schedule. |
| Schedule O | Controlled-group consent/apportionment when required. A group may need allocation analysis even though its members file separately. |
| Schedule UTP | Evaluate the full reporting conditions and reportable positions, including positions for which no reserve was recorded because the corporation expects to litigate. Do not equate “no reserve” with “no reporting.” |
| Form 1125-A; Form 1125-E | Tax COGS/inventory where required; officer compensation under its dual trigger. |
| Form 4562; Form 4797; Schedule D and Form 8949 | Depreciation/amortization; business-property dispositions; capital transactions. Reconcile basis, recapture and capital-loss limitations. |
| Form 8990 | Section 163(j) computation or reporting when required, including relevant carryforwards and pass-through interests. |
| Forms 8992, 8993, 5471 and 1118 | Applicable CFC inclusion, section 250, CFC information and foreign-tax-credit computations. Use the correct year and effective rules. |
| Form 5472 | Foreign-owned reporting corporations and other specified filers with reportable transactions; the ownership screen alone is not the complete filing test. |
| Form 4626; Form 8827 | CAMT computation/status reporting as required; minimum-tax-credit carryforward and permitted utilization. |
| Form 8991 | BEAT. This is not the business-interest limitation form. |
| Forms 6765 and 3800 | Research credit and general-business-credit computation when applicable, with deduction/basis coordination. |
| Form 7004; Form 2220 | Timely filing extension; estimated-tax penalty computation when required or useful. Form 2220 is not mandatory on every 1120. |
| Forms 8832, 1128 and 8716 | Classification election evidence or accounting-period applications/elections where applicable. |
| Form 7208 with Form 720 | Stock-repurchase excise tax is reported through the separate excise-tax filing process, not as a routine quarterly 1120 attachment. |
| Form 8975 and Schedule A | Country-by-country report for a qualifying US ultimate parent, not every corporation with foreign operations. |

Authorities: [Form 1120 instructions, Other Forms and Statements; Schedules C/J/K/L/M-1/M-2](https://www.irs.gov/instructions/i1120); [Schedule M-3 instructions](https://www.irs.gov/instructions/i1120sm3); [Form 7208 instructions](https://www.irs.gov/instructions/i7208); [Form 8975 instructions](https://www.irs.gov/instructions/i8975).

## Deadlines and filing

| Obligation | Timing, conditions and source |
|---|---|
| Form 1120 | Generally the **15th day of the 4th month** after year-end. For a calendar 2026 year, the ordinary date is **April 15, 2027**, subject to holidays and applicable relief. [IRC 6072(a)](https://uscode.house.gov/us/usc/t26/s6072/); [Form 1120 instructions, When To File](https://www.irs.gov/instructions/i1120). |
| June 30 fiscal-year transition | For years beginning **before January 1, 2026**, the special third-month original deadline still applies; years beginning after 2025 move to the fourth-month rule. Do not select the rule from the return's ending year alone. [IRC 6072 effective-date notes](https://uscode.house.gov/us/usc/t26/s6072/); [Form 7004 instructions](https://www.irs.gov/instructions/i7004). |
| Form 7004 | File by the original deadline with a proper tax estimate. Ordinarily extends filing **6 months**; the specified pre-2026 June 30 year has a **7-month** extension. Payment is still due by the original payment deadline. [Form 7004 instructions, General Instructions and Part II](https://www.irs.gov/instructions/i7004). |
| Estimated installments | **15th day of months 4, 6, 9 and 12** of the tax year. Calendar 2026 ordinary dates are **April 15, June 15, September 15 and December 15, 2026**, subject to relief. Short-year rules require a separate schedule. [Form 2220 instructions](https://www.irs.gov/instructions/i2220). |
| Stock-repurchase excise return | Form 7208 is filed annually with Form 720 for the **first full calendar quarter after the corporation's tax year ends**. Determine the corresponding Form 720 due date and payment separately. [Form 7208 instructions, When To File](https://www.irs.gov/instructions/i7208). |
| Country-by-country report | A qualifying US ultimate parent generally attaches Form 8975 and its Schedules A to its timely income-tax return, including extensions. Prior reporting-period annual group revenue must meet the **$850 million** threshold, with the form's definitions. [Form 8975 instructions](https://www.irs.gov/instructions/i8975). |

The ERO retains signed Form 8879-CORP; do not routinely send it to the IRS. Retain it for 3 years from the return due date or IRS received date, whichever is later: "The ERO must retain Form 8879-CORP". [Form 8879-CORP, page 2](https://www.irs.gov/pub/irs-pdf/f8879crp.pdf).

### Estimated-tax decision and Form 2220

For an ordinary corporation, required annual payment is generally the smaller of **100% of current-year tax** or **100% of prior-year tax**. The prior-year alternative requires a return for a full **12-month** preceding year showing a tax liability. A loss year with no tax does not supply a zero prior-year safe harbor. There is no general individual-style 110% corporate safe harbor. [Form 2220 instructions, Required Annual Payment](https://www.irs.gov/instructions/i2220).

A “large corporation” generally had modified taxable income of at least **$1 million** in any of the **3 preceding tax years**, with predecessor and controlled-group rules. It may use the prior-year alternative only for the first installment, then catches up the shortfall in the second installment. Recompute the later installments from current-year tax. [Form 2220 instructions, Large corporations](https://www.irs.gov/instructions/i2220).

Compare ordinary equal installments with the annualized-income or adjusted-seasonal method when supported by the actual income pattern. The standard annualized periods are the first **3, 3, 6 and 9 months**; alternative periods **2, 4, 7 and 10** or **3, 5, 8 and 11 months** require the prescribed Form 8842 election timing. The adjusted-seasonal method is a separate eligibility/computation rule, not another name for those alternative annualization periods. Preserve interim income and deduction workpapers. [Form 2220 instructions, Schedule A Parts I-II](https://www.irs.gov/instructions/i2220).

Generally the IRS can compute the estimated-tax penalty without Form 2220. Attach it when the instructions require it, including use of annualized/seasonal installments or the large-corporation first-installment prior-year rule, even when those calculations produce no penalty. Do not import CAMT estimated-tax relief for a prior year into 2026 without an applicable current-year authority.

Use the IRS-approved electronic tax-payment method for the corporation and payment type, with the correct EIN, tax period and payment designation. EFTPS is an available method, not a reason to ignore other methods the current IRS instructions permit. Save confirmations and reconcile the taxpayer account. Obtain the authorized corporate signature and, where applicable, Form 8879-CORP authorization through the electronic return originator. [Form 1120 instructions, Electronic Deposit Requirement, Tax Payments and Who Must Sign](https://www.irs.gov/instructions/i1120).

## Penalties and interest

| Failure | General rule and limiting conditions | Official source |
|---|---|---|
| Late filing | **5%** of the relevant unpaid tax per month or part, up to **25%**, absent reasonable cause. A valid extension changes the filing due date. | [IRC 6651(a)(1), (b)](https://uscode.house.gov/us/usc/t26/s6651/). |
| Return more than **60 days** late | For returns required to be filed in **2027**, minimum is the lesser of **$535** or **100%** of the tax required to be shown. This filing-year figure is not selected simply from the income-tax year printed on the return. | [Rev. Proc. 2025-32, section 4.52](https://www.irs.gov/irb/2025-45_IRB). |
| Late payment | Generally **0.5%** per month or part of unpaid tax, up to **25%**; statutory rate changes and reasonable-cause relief may apply. A filing extension does not itself extend payment. | [IRC 6651(a)(2), (c)-(d)](https://uscode.house.gov/us/usc/t26/s6651/). |
| Concurrent late filing and late payment | Reduce the filing penalty by the payment penalty for an overlapping month; do not charge both full rates on the same base. Under the ordinary unchanged rates, the combined maximum can reach **47.5%**, not 50%. | [IRC 6651(c)(1)](https://uscode.house.gov/us/usc/t26/s6651/). |
| Estimated-tax underpayment | Compute separately by installment and period using Form 2220; a large payment at year-end does not erase an earlier underpayment period. | [Form 2220 instructions](https://www.irs.gov/instructions/i2220). |
| Underpayment of reported tax | Interest runs from the applicable original payment due date and uses the rate for each period, with daily compounding and a special large-corporate-underpayment rule. Do not hard-code one annual rate. | [IRS Interest](https://www.irs.gov/payments/interest). |
| Accuracy-related or information-return failures | Assess the actual penalty provision, documentation and defenses. Forms 5471/5472 and other information returns can have separate consequences despite no income-tax balance. | [Form 1120 instructions, Interest and Penalties; Other Forms](https://www.irs.gov/instructions/i1120). |

Reasonable cause requires documented facts and the applicable standard; an adviser relationship is not automatic relief. Form 7004 instructions describe conditional late-payment relief for a timely extended return with the required timely payment and balance paid by the extended deadline; interest remains a separate charge. Section 6699 is the S corporation return penalty and is not the ordinary C corporation late-filing provision. [Form 7004 instructions, Interest and Penalties](https://www.irs.gov/instructions/i7004); [IRC 6699](https://uscode.house.gov/us/usc/t26/s6699/).

The 0.25% installment-agreement late-payment rate under section 6651(h) applies only to qualifying individuals, not corporations (statutory wording: "individual" and "0.25"). [IRC 6651(h)](https://uscode.house.gov/us/usc/t26/s6651/).

Ordinary underpayment interest is the federal short-term rate plus "3 percentage points". Large-corporate underpayments that exceed $100,000 (statutory wording: "exceeds $100,000") use plus "5 percentage points" after the statutory applicable date, generally the "30th day" after the relevant letter or notice, with payment and small-notice exceptions. Determine the applicable base, start date and quarterly rate; the higher rate does not merely apply immediately to the slice above the threshold. [IRC 6621(a)(2), (c)](https://uscode.house.gov/us/usc/t26/s6621/).

## Cross-border points

### Section 250, CFC inclusions and foreign tax credits

For a domestic C corporation's 2026-start year, determine foreign-derived deduction eligible income (FDDEI), net CFC tested income (NCTI) and the related section 78 gross-up before applying section 250. The 2026 section 951A computation removes the former QBAI-based deemed tangible return; do not subtract an old QBAI amount from the 2026 NCTI example or carry forward a GILTI/FDII worksheet unchanged. Match the CFC's applicable year and statutory effective dates for fiscal-year structures. [IRC 951A(a)-(c) and effective-date notes](https://uscode.house.gov/us/usc/t26/s951A/); [IRC 250(a)-(b)](https://uscode.house.gov/us/usc/t26/s250/).

FDDEI requires qualifying foreign sales, licenses or services and evidence of foreign use, customer status and related-party conditions. It is not all foreign revenue. Section 250 excludes specified income categories from deduction eligible income, including CFC inclusions, specified dividends, foreign branch income and other statutory categories. The 2025 amendments exclude gain from specified intangible and depreciable/amortizable/depletable property dispositions after **June 16, 2025**. For years beginning after 2025, the statutory expense-allocation rule excludes interest and research/experimental expenditures from the deductions allocated for this calculation. [IRC 250(b), amendment and effective-date notes](https://uscode.house.gov/us/usc/t26/s250/).

Apply the taxable-income limit **to the bases**: if FDDEI plus NCTI exceeds taxable income computed without section 250, reduce those bases proportionately as section 250(a)(2) directs, then apply their respective deduction percentages. Do not simply cap the initially computed deduction at taxable income. Handle the associated section 78 amount under the statutory computation and Form 8993 instructions. Reconcile the deduction through Schedule C to the special-deduction line; do not subtract it again in M-1.

Foreign tax credits require Form 1118 basket, sourcing, expense-allocation and limitation analysis. The 2026 NCTI deemed-paid rule generally uses **90%** of the qualifying tested foreign income taxes times the inclusion percentage; it does not guarantee a credit of that amount after all limitations. Section 960(d)(4) separately disallows **10%** of specified taxes on distributions excluded under section 959(a) because of section 951A inclusions; the 10% PTEP-tax credit disallowance applies to PTEP resulting from a section 951A inclusion in a US shareholder tax year ending after June 28, 2025. The distribution date alone does not determine applicability. Notice 2025-77 uses "a taxable year ending after June 28, 2025". [Notice 2025-77, section 3.01(2)](https://www.irs.gov/irb/2025-52_IRB#NOT-2025-77); [Form 1118 instructions, What's New](https://www.irs.gov/instructions/i1118). Do not turn either percentage into a universal effective tax rate. Route the CFC/PTEP ledgers, foreign branch, hybrid, treaty and section 245A issues for the corresponding international computation. [IRC 960(d) and effective-date notes](https://uscode.house.gov/us/usc/t26/s960/); [Form 1120 instructions, Schedule C and Form 1118](https://www.irs.gov/instructions/i1120).

### CAMT and BEAT

For CAMT, test applicable-corporation status using the prior-year statutory lookback, aggregation and foreign-parented group rules. This is an **AFSI** test, not a gross-revenue test. An applicable corporation does not automatically cease to be applicable merely because a later year's income falls. Determine whether an authorized simplified method applies under the current instructions and its reliance conditions. The Form 4626 instructions read for this version include interim guidance and proposed-rule methods; do not describe all of those rules as final regulations. [IRC 59(k)](https://uscode.house.gov/us/usc/t26/s59/); [Form 4626 instructions, Applicable Corporation and Simplified Methods](https://www.irs.gov/instructions/i4626).

Build AFSI from the applicable financial statements, applying statutory and applicable guidance adjustments for tax versus financial-statement depreciation, consolidation, partnerships, CFCs, foreign taxes, pensions and other items. Reconcile the FSNOL ledger separately from regular-tax NOLs. Compute:

```text
tentative minimum tax = 15% × AFSI after permitted FSNOL deduction − corporate AMT FTC
CAMT = max(0, tentative minimum tax − (regular tax for section 55 purposes + BEAT))
```

BEAT is **subtracted together with regular tax** in that comparison. Adding BEAT after subtracting regular tax would overstate CAMT. Use the statutory regular-tax definition and the Form 4626 regular-tax/FTC mapping, not an arbitrary pre-credit tax figure. A CAMT minimum-tax-credit carryforward is governed by section 53 and Form 8827; it is not automatically refundable. [IRC 55(a)-(c)](https://uscode.house.gov/us/usc/t26/s55/); [Form 4626 instructions, Tax Computation](https://www.irs.gov/instructions/i4626).

Screen BEAT under the thresholds in the table, group aggregation, related-foreign-person payments, exclusions and base-erosion-percentage rules. Form 8991 computes modified taxable income, tax benefits and the regular-tax/credit comparison; multiplying ordinary taxable income by the BEAT rate is insufficient. Transfer-pricing support does not by itself eliminate BEAT, and BEAT does not replace section 482. [IRC 59A](https://uscode.house.gov/us/usc/t26/s59A/).

Unused section 53 minimum-tax credit carries forward without a fixed expiry ("all prior taxable years"); annual use is limited to regular tax after the specified credits exceeding "the tentative minimum tax for the taxable year". [IRC 53(b)-(c)](https://uscode.house.gov/us/usc/t26/s53/).

### Reporting, withholding and shareholder planning

Obtain the ownership chain and transactions for Forms 5471 and 5472, foreign accounts and operations, Forms 8992/8993/1118 and any Form 8975 filing. Review outbound dividends, interest, royalties and service payments for withholding, documentation and information returns under the relevant cross-border guide. A treaty claim needs the actual treaty, residence, beneficial ownership, limitation-on-benefits and filing facts; the domestic corporation rate does not answer the payee's withholding treatment. Use `us-transfer-pricing` for controlled-transaction pricing and documentation.

For Form 5472, screen a US corporation with at least one direct or indirect 25% foreign shareholder at any time in the year, by vote or value ("at least 25% of either"); then apply reportable-related-party-transaction rules and exceptions. [Form 5472 instructions, Definitions and Who Must File](https://www.irs.gov/instructions/i5472).

A C corporation may issue stock whose **noncorporate shareholder** later qualifies for section 1202; the corporation itself does not claim that gain exclusion on Form 1120. For qualifying stock acquired after **July 4, 2025**, the exclusion schedule is **50% after at least 3 years**, **75% after at least 4 years**, and **100% after at least 5 years**. The new dollar limb is **$15 million**, adjusted for prior and specified same-year eligible gains, compared with the alternative **10-times-basis** limit. Stock acquired earlier has its own date-dependent percentages, holding period and dollar limit. For stock issued after July 4, 2025, the issuer gross-asset ceiling is **$75 million**, tested before and immediately after issuance with statutory aggregation and contributed-property valuation. Do not confuse the acquisition-date transition with the issuance-date transition. Inflation indexing of the new amounts begins after 2026. [IRC 1202(a)-(d) and effective-date notes](https://uscode.house.gov/us/usc/t26/s1202/).

Maintain original-issue, capitalization, redemption, asset and active-business records. Substantially all of the holding period must satisfy the relevant C corporation/active-business conditions, and excluded businesses and other restrictions remain. An issuance meeting the size threshold alone does not establish QSBS.

## Two worked examples that recompute

All amounts below are fictional US-dollar facts for tax years beginning in 2026. The first two give a normal return and an election decision; the additional cases preserve the separate loss, interest, multinational and CAMT checks. They do not establish a client's elections or entitlement.

### Example 1: ordinary domestic corporation with the charitable floor

Acme has sales of $4,200,000, COGS of $2,300,000 and taxable interest of $5,000. Allowable noncharitable deductions are officer pay $400,000, salaries $800,000, rent $120,000, depreciation $90,000, other expenses $180,000 and state tax $35,000. All costs are assumed substantiated and otherwise allowable. There are no NOLs, special deductions, credits, CAMT or other taxes.

Total income is **$1,905,000** and the noncharitable subtotal is **$280,000**. A current $20,000 qualifying cash gift is below the ceiling; the $2,800 floor leaves **$17,200** deductible. Taxable income is **$262,800** and regular tax **$55,188**. The floor-denied amount does not acquire a carryforward merely because it was disallowed in this below-ceiling case. With $130,000 of verified estimated payments, the overpayment is **$74,812**. Payment timeliness still needs the separate installment test.

For the book reconciliation, assume book income after a $130,000 federal tax provision is $130,000. Adding back that provision once and the $2,800 nondeductible gift reaches the $262,800 return subtotal. [IRC 170(b)(2), (d)(2)](https://uscode.house.gov/us/usc/t26/s170/); [IRC 11(b)](https://uscode.house.gov/us/usc/t26/s11/).

```oa-check
name: Domestic C corporation charitable floor and return reconciliation
inputs:
  sales: 4200000
  cogs: 2300000
  interest_income: 5000
  officer_pay: 400000
  salaries: 800000
  rent: 120000
  depreciation: 90000
  other_expenses: 180000
  state_tax: 35000
  gift: 20000
  estimated_payments: 130000
  book_income: 130000
  federal_tax_provision: 130000
steps:
  - total_income: sales - cogs + interest_income
  - noncharitable_deductions: officer_pay + salaries + rent + depreciation + other_expenses + state_tax
  - contribution_base: total_income - noncharitable_deductions
  - contribution_floor: contribution_base * 0.01
  - deductible_gift: gift - contribution_floor
  - taxable_income: contribution_base - deductible_gift
  - regular_tax: taxable_income * 0.21
  - overpayment: estimated_payments - regular_tax
  - m1_subtotal: book_income + federal_tax_provision + contribution_floor
expected:
  total_income: 1905000
  contribution_base: 280000
  deductible_gift: 17200
  taxable_income: 262800
  regular_tax: 55188
  overpayment: 74812
  m1_subtotal: 262800
```

### Example 2: current domestic research deduction or elective amortization

A calendar-year corporation has $2,000,000 of taxable income before $1,200,000 of qualifying domestic research costs. It has no other limitations, losses, credits, section 250 deduction or CAMT. All research costs are eligible for section 174A, and benefits begin in January.

The default current deduction produces **$800,000** taxable income and **$168,000** regular tax. A valid election to amortize over 60 months produces 12 months of deduction, **$240,000**, taxable income **$1,760,000**, tax **$369,600** and an unamortized balance of **$960,000**. Current expensing reduces this year's regular tax by **$201,600** in these facts. The election choice may differ when credits, other deduction limitations, future taxable income or state treatment change; the comparison is not a universal recommendation. [IRC 174A(a), (c)](https://uscode.house.gov/us/usc/t26/s174A/).

```oa-check
name: Domestic research current deduction versus 60 month election
inputs:
  income_before_research: 2000000
  research_cost: 1200000
  amortization_months: 60
  benefit_months_this_year: 12
steps:
  - immediate_taxable_income: income_before_research - research_cost
  - immediate_tax: immediate_taxable_income * 0.21
  - elected_deduction: research_cost / amortization_months * benefit_months_this_year
  - elected_taxable_income: income_before_research - elected_deduction
  - elected_tax: elected_taxable_income * 0.21
  - remaining_basis: research_cost - elected_deduction
  - current_year_tax_difference: elected_tax - immediate_tax
expected:
  immediate_taxable_income: 800000
  immediate_tax: 168000
  elected_deduction: 240000
  elected_taxable_income: 1760000
  elected_tax: 369600
  remaining_basis: 960000
  current_year_tax_difference: 201600
```

### Additional check: NOL ordering without a pre-2018 bucket

The corporation has $800,000 of modified taxable income before its NOL and $1,000,000 of qualifying post-2017 NOL carryforwards, no pre-2018 NOL, no section 382 restriction and no other adjustments. The deduction is **$640,000**, leaving taxable income **$160,000**, tax **$33,600** and NOL carryforward **$360,000**. [IRC 172(a)](https://uscode.house.gov/us/usc/t26/s172/).

```oa-check
name: Post 2017 NOL deduction without ownership change
inputs:
  modified_income: 800000
  available_nol: 1000000
steps:
  - allowed_nol: min(available_nol, modified_income * 0.80)
  - taxable_income: modified_income - allowed_nol
  - regular_tax: taxable_income * 0.21
  - remaining_nol: available_nol - allowed_nol
expected:
  allowed_nol: 640000
  taxable_income: 160000
  regular_tax: 33600
  remaining_nol: 360000
```

### Additional check: ATI and interest income are not double counted

An in-scope corporation's income **before business interest expense** is $5,000,000, already including $50,000 of business interest income and after $1,500,000 of depreciation/amortization. Assume no other ATI adjustments, foreign inclusions, capitalized-interest complications, floor-plan interest or carryforwards. ATI is $5,000,000 + $1,500,000 - $50,000 = **$6,450,000**. The limit is **$1,985,000**, including business interest income. With $3,000,000 of current business interest expense, **$1,015,000** carries forward. If the expense were only $1,800,000, all would fit within the same limit. [IRC 163(j)](https://uscode.house.gov/us/usc/t26/s163/); [Form 8990 instructions](https://www.irs.gov/instructions/i8990).

```oa-check
name: 2026 ATI with depreciation addback and business interest income
inputs:
  income_before_interest_expense: 5000000
  depreciation_amortization: 1500000
  business_interest_income: 50000
  business_interest_expense: 3000000
  alternative_interest_expense: 1800000
steps:
  - ati: income_before_interest_expense + depreciation_amortization - business_interest_income
  - interest_limit: business_interest_income + ati * 0.30
  - allowed_interest: min(business_interest_expense, interest_limit)
  - disallowed_interest: business_interest_expense - allowed_interest
  - alternative_allowed: min(alternative_interest_expense, interest_limit)
expected:
  ati: 6450000
  interest_limit: 1985000
  allowed_interest: 1985000
  disallowed_interest: 1015000
  alternative_allowed: 1800000
```

### Additional check: 2026 section 250

A domestic corporation has $20,000,000 of taxable income before section 250, including $5,000,000 of NCTI and a related $500,000 section 78 gross-up. Properly substantiated FDDEI is $4,000,000. Assume both relevant years begin in 2026, no taxable-income limitation or other adjustment and no credits in this illustrative regular-tax subtotal. Do not subtract a former QBAI return.

The FDDEI deduction is **$1,333,600** and the NCTI/gross-up deduction **$2,200,000**, total **$3,533,600**. Taxable income is **$16,466,400** and regular tax **$3,457,944 before foreign tax credits**. The $20,000,000 input already includes the gross-up; it is not added to income a second time. [IRC 250(a)](https://uscode.house.gov/us/usc/t26/s250/); [IRC 951A](https://uscode.house.gov/us/usc/t26/s951A/).

```oa-check
name: 2026 FDDEI and NCTI deductions including section 78 grossup
inputs:
  income_before_250: 20000000
  fddei: 4000000
  ncti: 5000000
  related_grossup: 500000
steps:
  - fddei_deduction: fddei * 0.3334
  - ncti_deduction: (ncti + related_grossup) * 0.40
  - total_deduction: fddei_deduction + ncti_deduction
  - taxable_income: income_before_250 - total_deduction
  - tax_before_credits: taxable_income * 0.21
expected:
  fddei_deduction: 1333600
  ncti_deduction: 2200000
  total_deduction: 3533600
  taxable_income: 16466400
  tax_before_credits: 3457944
```

### Additional check: CAMT interaction with BEAT

Assume applicable-corporation status was established under the prior-year tests. Current AFSI before FSNOL is $1,100,000,000, available FSNOL is $200,000,000, corporate AMT FTC is zero, regular tax for section 55 purposes is $63,000,000 and BEAT is $10,000,000. No other credits or taxes alter this example.

Permitted FSNOL is **$200,000,000**, leaving AFSI **$900,000,000** and tentative minimum tax **$135,000,000**. CAMT is $135,000,000 - ($63,000,000 + $10,000,000) = **$62,000,000**; combined regular tax, BEAT and CAMT is **$135,000,000**. With zero BEAT, CAMT would be **$72,000,000** and the same combined amount in these facts. [IRC 55(a)-(b)](https://uscode.house.gov/us/usc/t26/s55/); [IRC 56A(d)](https://uscode.house.gov/us/usc/t26/s56A/).

```oa-check
name: CAMT subtracts regular tax and BEAT in the same comparison
inputs:
  afsi_before_fsnol: 1100000000
  available_fsnol: 200000000
  camt_foreign_tax_credit: 0
  regular_tax: 63000000
  beat: 10000000
steps:
  - fsnol_deduction: min(available_fsnol, afsi_before_fsnol * 0.80)
  - afsi: afsi_before_fsnol - fsnol_deduction
  - tentative_minimum_tax: afsi * 0.15 - camt_foreign_tax_credit
  - camt: max(0, tentative_minimum_tax - regular_tax - beat)
  - combined_tax: regular_tax + beat + camt
  - camt_without_beat: max(0, tentative_minimum_tax - regular_tax)
expected:
  fsnol_deduction: 200000000
  afsi: 900000000
  tentative_minimum_tax: 135000000
  camt: 62000000
  combined_tax: 135000000
  camt_without_beat: 72000000
```

## Ask the client first

1. What is the entity's place of organization, federal classification, election history, exact tax year and group/ownership structure, including foreign owners and any ownership changes?
2. Can the client provide the trial balance, financial statements, prior returns, payment confirmations, tax-basis schedules, NOL/credit/interest/charitable carryovers and prior elections?
3. What are current and prior-period receipts, year-end assets and AFSI, after applicable aggregation, and does tax-shelter or specialized-corporation status apply?
4. Which research, software, asset, interest and charitable expenditures occurred, where was research conducted, and what are the acquisition, construction, payment and benefit-start dates?
5. What foreign operations, CFC/branch income, related-party payments, distributions, stock repurchases and uncertain tax positions exist, and what supporting information returns and withholding records are available?
6. What officer/shareholder compensation, stock issuances/redemptions, accounting-method changes, filing extensions, instalment choices and known notices need review before the return is finalized?

## Sources

All sources below were read on **2026-11-13**. Read scope is stated so a reviewer can reproduce the checks. Statutory figures take precedence over superseded figures in prior-year form instructions. Final 2026 Form 1120 and related annual instruction layouts remain unconfirmed as noted above; do not treat that outstanding form-version check as a verified filing layout.

| Official source | Provisions or instruction sections read and used | Read on |
|---|---|---|
| [IRS Form 1120 instructions](https://www.irs.gov/instructions/i1120) | Read for Published 2025 instructions: What's New; Who Must File; entity elections; electronic filing; accounting periods; filing/payment; interest and penalties; income and deductions; Schedule C and DRD worksheet; Schedules J/K/L/M-1/M-2; attached forms. | 2026-11-13 |
| [IRS Form 2220 instructions](https://www.irs.gov/instructions/i2220) | Read for Who Must File; required annual payment; large corporations; installment dates; annualized and seasonal methods; Form 8842 election periods. | 2026-11-13 |
| [IRS Form 7004 instructions](https://www.irs.gov/instructions/i7004) | Read for Filing/extension conditions; June 30 transition; payment and penalty rules. | 2026-11-13 |
| [Rev. Proc. 2025-32, IRB 2025-45](https://www.irs.gov/irb/2025-45_IRB) | Read for Sections 2.11, 4.24, 4.30 and 4.52: 179D termination, 2026 section 179 and gross-receipts figures, 2027 filing-penalty minimum. | 2026-11-13 |
| [IRC 11](https://uscode.house.gov/us/usc/t26/s11/), [7701](https://uscode.house.gov/us/usc/t26/s7701/), [6072](https://uscode.house.gov/us/usc/t26/s6072/) | Read for Corporate rate; domestic/foreign definitions; corporate filing deadline and effective-date notes. | 2026-11-13 |
| [26 CFR 301.7701-3](https://www.ecfr.gov/current/title-26/section-301.7701-3) | Read for Paragraphs (b), (c)(1) and (g): eligible-entity classification, election timing, repeated elections, return copy and deemed transactions. | 2026-11-13 |
| [IRC 243](https://uscode.house.gov/us/usc/t26/s243/), [246](https://uscode.house.gov/us/usc/t26/s246/) | Read for DRD tiers, qualifying affiliated dividends, aggregate income limits, NOL exception and holding periods. | 2026-11-13 |
| [IRC 172](https://uscode.house.gov/us/usc/t26/s172/), [1212](https://uscode.house.gov/us/usc/t26/s1212/), [382](https://uscode.house.gov/us/usc/t26/s382/) | Read for NOL buckets and exceptions; corporate capital-loss carry periods; ownership-change definition, basic limitation and testing period. | 2026-11-13 |
| [Form 8990 instructions](https://www.irs.gov/instructions/i8990), [IRC 163](https://uscode.house.gov/us/usc/t26/s163/) | Read for Section 163(j), exclusions/exemptions, ATI, carryforwards and 2025/2026 statutory changes. | 2026-11-13 |
| [IRC 174A](https://uscode.house.gov/us/usc/t26/s174A/), [174](https://uscode.house.gov/us/usc/t26/s174/), [280C](https://uscode.house.gov/us/usc/t26/s280C/) | Read for Domestic/foreign research; elective amortization and transition notes; research-credit deduction coordination. | 2026-11-13 |
| [IRC 170](https://uscode.house.gov/us/usc/t26/s170/), [IRS business-provisions explanation](https://www.irs.gov/newsroom/understanding-the-working-families-tax-cuts-business-tax-provisions-youtube-video-text-script) | Read for Corporate floor/ceiling and carryover rules in sections 170(b)(2), (d)(2); IRS explanation of floor-only disallowance. | 2026-11-13 |
| [IRC 162](https://uscode.house.gov/us/usc/t26/s162/), [Form 1125-E instructions](https://www.irs.gov/instructions/i1125e) | Read for Reasonable compensation; section 162(m) covered employees, new controlled-group rule and effective dates; officer form filing trigger. | 2026-11-13 |
| [Schedule M-3 instructions](https://www.irs.gov/instructions/i1120sm3) | Read for Who Must File; permitted M-1 alternative; Schedule B exception; financial-statement and balance-sheet alignment. | 2026-11-13 |
| [IRC 250](https://uscode.house.gov/us/usc/t26/s250/), [951A](https://uscode.house.gov/us/usc/t26/s951A/), [960](https://uscode.house.gov/us/usc/t26/s960/) | Read for Current section 250 rates/base limit and DEI changes; NCTI without QBAI; deemed-paid credit and PTEP haircut, with effective-date notes. | 2026-11-13 |
| [IRC 55](https://uscode.house.gov/us/usc/t26/s55/), [56A](https://uscode.house.gov/us/usc/t26/s56A/), [59](https://uscode.house.gov/us/usc/t26/s59/), [Form 4626 instructions](https://www.irs.gov/instructions/i4626) | Read for Corporate tentative minimum tax and regular-tax/BEAT comparison; AFSI/FSNOL; section 59(k) status tests; interim simplified methods and return computation. | 2026-11-13 |
| [IRC 59A](https://uscode.house.gov/us/usc/t26/s59A/) | Read for BEAT rate, bank/securities increment, modified base, applicable-taxpayer thresholds and aggregation. | 2026-11-13 |
| [Forms 7208](https://www.irs.gov/instructions/i7208) and [8975](https://www.irs.gov/instructions/i8975) instructions | Read for Annual stock-repurchase excise filing through Form 720; US ultimate-parent CbC revenue threshold and filing deadline. | 2026-11-13 |
| [IRC 1202](https://uscode.house.gov/us/usc/t26/s1202/) | Read for Noncorporate exclusion; new holding-period percentages, dollar/basis limits, gross assets, issuance/acquisition transitions and active-business conditions. | 2026-11-13 |
| [IRC 6651](https://uscode.house.gov/us/usc/t26/s6651/), [IRS Interest](https://www.irs.gov/payments/interest) | Read for Filing/payment penalties, overlap rule, reasonable cause and interest framework. | 2026-11-13 |
| [31 CFR 10.37](https://www.ecfr.gov/current/title-31/section-10.37) | Read for Written-advice factual/legal standards and prohibition on audit-lottery reasoning. | 2026-11-13 |
| [Official source](https://uscode.house.gov/us/usc/t26/s245A/) | Read for participation exemption, specified foreign corporation and exclusions | 2026-11-13 |
| [Official source](https://www.irs.gov/pub/irs-drop/rp-25-28.pdf) | Read for section2.02 prior research amortization and transition procedures | 2026-11-13 |
| [Official source](https://uscode.house.gov/us/usc/t26/s4999/) | Read for recipient excess-parachute excise rate | 2026-11-13 |
| [Official source](https://www.irs.gov/instructions/i5472) | Read for 25% ownership, related-party transaction reporting and exceptions | 2026-11-13 |
| [Official source](https://www.irs.gov/irb/2025-52_IRB#NOT-2025-77) | Read for section3.01(2) PTEP inclusion-tax-year cutoff | 2026-11-13 |
| [Official source](https://www.irs.gov/instructions/i1118) | Read for PTEP deemed-paid credit changes in What's New | 2026-11-13 |
| [Official source](https://uscode.house.gov/us/usc/t26/s53/) | Read for minimum-tax credit carryforward and annual ceiling | 2026-11-13 |
| [Official source](https://www.irs.gov/pub/irs-pdf/f8879crp.pdf) | Read for page2 ERO retention period and no-routine-submission rule | 2026-11-13 |
| [Official source](https://www.irs.gov/instructions/i7205) | Read for Who Must File and section179D form requirement | 2026-11-13 |
| [Official source](https://uscode.house.gov/us/usc/t26/s6621/) | Read for ordinary and large-corporate interest, thresholds and applicable dates | 2026-11-13 |
| [Official source](https://uscode.house.gov/us/usc/t26/s362/) | Read for section362(a) corporate carryover basis | 2026-11-13 |
| [Official source](https://uscode.house.gov/us/usc/t26/s1223/) | Read for paragraphs1-2 holding-period tacking | 2026-11-13 |
| [Official source](https://www.irs.gov/businesses/small-businesses-self-employed/single-member-limited-liability-companies) | Read for owner taxation of disregarded activity | 2026-11-13 |
| [Official source](https://www.irs.gov/pub/irs-pdf/f8832.pdf) | Read for page6 EIN retention and repeat-election exceptions | 2026-11-13 |

### Exact source evidence

The following short verbatim fragments support the figures; conditions and effective periods remain in the operative sections.

| Source scope | Exact source fragments | Official source | Read on |
|---|---|---|---|
| Read for Affiliation | “80-percent voting and value test” | [IRC 1504](https://uscode.house.gov/us/usc/t26/s1504/) | 2026-11-13 |
| Read for Tax year | “varying from 52 to 53 weeks” | [IRC 441](https://uscode.house.gov/us/usc/t26/s441/) | 2026-11-13 |
| Read for Classification timing | “75 days”; “12 months”; “60 months” | [26 CFR 301.7701-3](https://www.ecfr.gov/current/title-26/section-301.7701-3) | 2026-11-13 |
| Read for Corporate rate | “21 percent” | [IRC 11](https://uscode.house.gov/us/usc/t26/s11/) | 2026-11-13 |
| Read for DRD tiers | “50 percent”; “100 percent”; “65 percent”; “20-percent owned corporation” | [IRC 243](https://uscode.house.gov/us/usc/t26/s243/) | 2026-11-13 |
| Read for NOL deduction and carry periods | “80 percent”; “20 taxable years”; “each taxable year following”; “5 taxable years preceding” | [IRC 172](https://uscode.house.gov/us/usc/t26/s172/) | 2026-11-13 |
| Read for Capital losses | “3 taxable years preceding”; “5 taxable years succeeding” | [IRC 1212](https://uscode.house.gov/us/usc/t26/s1212/) | 2026-11-13 |
| Read for Interest limitation | “30 percent” | [IRC 163](https://uscode.house.gov/us/usc/t26/s163/) | 2026-11-13 |
| Read for Domestic research election | “not less than 60 months” | [IRC 174A](https://uscode.house.gov/us/usc/t26/s174A/) | 2026-11-13 |
| Read for Foreign research | “15-year period”; “midpoint” | [IRC 174](https://uscode.house.gov/us/usc/t26/s174/) | 2026-11-13 |
| Read for Corporate gifts | “1 percent”; “10 percent”; “5-year carryforward” | [IRC 170](https://uscode.house.gov/us/usc/t26/s170/) | 2026-11-13 |
| Read for Inflation amounts | “$2,560,000”; “$4,090,000”; “$32,000,000”; “$535” | [Rev. Proc. 2025-32 §§4.24, 4.30, 4.52](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) | 2026-11-13 |
| Read for Section 250 | “33.34 percent”; “40 percent” | [IRC 250](https://uscode.house.gov/us/usc/t26/s250/) | 2026-11-13 |
| Read for CAMT | “15 percent” | [IRC 55](https://uscode.house.gov/us/usc/t26/s55/) | 2026-11-13 |
| Read for CAMT status thresholds | “3-taxable-year period”; “exceeds $1,000,000,000”; “$100,000,000 or more” | [IRC 59](https://uscode.house.gov/us/usc/t26/s59/) | 2026-11-13 |
| Read for FSNOL limit | “80 percent” | [IRC 56A](https://uscode.house.gov/us/usc/t26/s56A/) | 2026-11-13 |
| Read for BEAT | “10.5 percent”; “one percentage point”; “$500,000,000”; “3 percent”; “2 percent” | [IRC 59A](https://uscode.house.gov/us/usc/t26/s59A/) | 2026-11-13 |
| Read for Officer-compensation attachment | “$500,000 or more, and deducts compensation for officers” | [Form 1125-E instructions](https://www.irs.gov/instructions/i1125e) | 2026-11-13 |
| Read for Small-return exception and e-file | “$250,000”; “10 or more returns” | [Form 1120 instructions](https://www.irs.gov/instructions/i1120) | 2026-11-13 |
| Read for Schedule M-3 | “$10 million or more”; “less than $50 million” | [Schedule M-3 instructions](https://www.irs.gov/instructions/i1120sm3) | 2026-11-13 |
| Read for Schedule UTP | “assets that equal or exceed $10 million” | [Schedule UTP instructions](https://www.irs.gov/instructions/i1120utp) | 2026-11-13 |
| Read for Country-by-country reporting | “$850 million or more” | [Form 8975 instructions](https://www.irs.gov/instructions/i8975) | 2026-11-13 |
| Read for Annual buyback filing | “first full quarter after the close of your tax year” | [Form 7208 instructions](https://www.irs.gov/instructions/i7208) | 2026-11-13 |
| Read for Income-tax return deadline | “15th day of April”; “15th day of the fourth month” | [IRC 6072](https://uscode.house.gov/us/usc/t26/s6072/) | 2026-11-13 |
| Read for Extension | “generally 6 months”; “automatic 7-month extension”; “before January 1, 2026” | [Form 7004 instructions](https://www.irs.gov/instructions/i7004) | 2026-11-13 |
| Read for Estimated-tax rules | “less than $500”; “25 percent”; “100 percent”; “12 months”; “$1,000,000 or more”; “3 taxable years” | [IRC 6655](https://uscode.house.gov/us/usc/t26/s6655/) | 2026-11-13 |
| Read for Calendar installments | “April 15”; “June 15”; “September 15”; “December 15” | [IRC 6655(c)(2)](https://uscode.house.gov/us/usc/t26/s6655/) | 2026-11-13 |
| Read for Annualization periods | “3 months”; “6 months”; “9 months”; “2 months”; “4 months”; “7 months”; “10 months”; “5 months”; “8 months”; “11 months” | [IRC 6655(e)(2)(A), (C)](https://uscode.house.gov/us/usc/t26/s6655/) | 2026-11-13 |
| Read for Penalties | “5 percent”; “25 percent”; “0.5 percent”; “60 days” | [IRC 6651](https://uscode.house.gov/us/usc/t26/s6651/) | 2026-11-13 |
| Read for Ordinary qualifying meals | “50 percent” | [IRC 274](https://uscode.house.gov/us/usc/t26/s274/) | 2026-11-13 |
| Read for NCTI credit and PTEP haircut | “90 percent”; “10 percent” | [IRC 960](https://uscode.house.gov/us/usc/t26/s960/) | 2026-11-13 |
| Read for QSBS | “3 years”; “50%”; “4 years”; “75%”; “5 years or more”; “100%”; “$15,000,000”; “10 times”; “$75,000,000” | [IRC 1202](https://uscode.house.gov/us/usc/t26/s1202/) | 2026-11-13 |

Not yet confirmed: final 2026 Form 1120 and related annual instruction field layouts. The guide labels known 2025 layout references and provides current 2026 substantive law; verify the final forms before filing. Taxpayer-specific elections, treaties, credits and special-regime eligibility require the actual records.

Refresh the actual return-year forms, inflation amounts, enacted-law effective dates and applicable relief before preparing a filing. Retain the source version, computations, unresolved facts and professional review record with the workpapers.
