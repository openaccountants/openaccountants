---
name: am-corporate-income-tax
description: "Prepare Armenia 2026 ordinary corporate and registered-PE profit-tax workpapers: reconcile accounts to the tax base, test documented deductions and capped costs, replace book depreciation, age prior losses, compute the lower-of quarterly advance and reconcile annual credits. Includes two reproducible examples and preserved supplementary research controls covering the tax bridge, representation, depreciation, losses, instalments, interest and donations. Use for Armenian CIT, business expenses, asset amortisation and annual profit-tax returns. Maps ordinary turnover and micro eligibility, computation and transitions, and the published profit-tax return with sign and special-row limits. Specialist incentives/assets, actual portal discrepancies and professional attestation remain separate. Checked against the law."
jurisdiction: AM
tax_year: 2026
last_updated: 2026-10-27
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
version: 0.4
category: international
sources:
  - url: "https://www.arlis.am/hy/acts/215611/latest"
    title: "Current Armenian Tax Code, corporate computation and advances"
    as_of: "2026-10-24"
  - url: "https://www.arlis.am/en/acts/231892"
    title: "Official English reproduction, with current Armenian corrections"
    as_of: "2026-10-24"
  - url: "https://www.arlis.am/hy/acts/226008"
    title: "HO-234-N 2026 base amendments"
    as_of: "2026-10-24"
  - url: "https://www.arlis.am/hy/acts/228632"
    title: "HO-385-N commencement gates"
    as_of: "2026-10-24"
  - url: "https://www.arlis.am/hy/acts/226558"
    title: "749-N July 2026 return consolidation"
    as_of: "2026-10-24"
---

# Armenia corporate income tax preparation v0.4

## Who this applies to

Prepare ordinary resident-company and registered corporate-PE profit-tax workpapers for tax year 2026. Resident organisations are located in Armenia under the statutory registration test; resident corporate income includes domestic and foreign objects, while PE attribution and no-PE/non-attributed receipts have separate rules. This is not the individual entrepreneur's 23% method, the investment-fund net-assets method or a certification of special-regime eligibility. [Code Articles 20, 22–23, 103–105, 125][code]; [cross-border method](am-cross-border.md)

Establish the regime for each period before computing 18% profit tax. Article 254's ordinary turnover-tax gate includes prior-year turnover not exceeding AMD 115 million, timely declaration and exclusions, including specified legal/accounting, head-office/management and labour-supply activities. Article 267's micro gate includes AMD 24 million and extensive activity/person/relationship exclusions. Equal-to and less-than are not interchangeable. Do not treat a small turnover, broad label such as IT, or the old formation/planning summary as an election. The [regime Guide](armenia-tax-optimization.md) supplies the complete ordinary eligibility, current activity exclusions, published statements and computation map. The following transition method applies before using the ordinary profit-tax base. [254–255, 267–268][code]

For either special regime, count all relevant activities and the other special regime's turnover. Statutory 20%-ownership links in Article 30(1) exclude the regime unless the linked persons have properly declared and actually maintained suspension. SRC-decision links under 30(2) instead use the recognised group's aggregate turnover test. A division/spin-off uses the predecessor's entire turnover for each resulting entity; merger/absorption adds predecessor amounts. Annual declarations are due by 20 February; new registrations and the stated resumption/re-registration routes have their own 20-day clocks. A compulsory micro exit requires a timely new turnover election if eligible; otherwise ordinary VAT status starts at exit. [30, 59, 254–255, 267–268][code]

In turnover tax, separate each activity's base, gross tax, current eligible expense reduction and same-activity opening reduction carry. Pay the greater of gross tax minus available reduction and the activity floor; carry the unused reduction. Trade uses 10% gross/9.5% expense/1% floor, production 7%/5%/3%, catering 12%/9%/3.5%, other activity 10%/6%/4.5%. Shared administrative/sales cost uses the activity's share of all-activity turnover. Fixed/intangible acquisition, improvement, depreciation, liquidation, free inputs, travel and representation do not enter these expense reductions. Apply the other statutory rates and separate catering election rather than reclassifying them as ordinary trade. [258, 260][code]

On turnover-to-ordinary exit, calculate post-exit bases separately. Reconstruct fixed/intangible carrying value including Article 121 depreciation during turnover status; ordinary depreciation deductions start next month's first day. Prorate the specified exit-month non-production/financial costs by post-exit days including exit day over all days in the month. Apply Article 264(3)'s other-asset rule without duplicating costs covered by the turnover reductions. Convert unused tax-reduction carries into gross-income deductions at 10× trade, 20× production, 10× catering and 15× other activity. For direct micro-to-ordinary exit, Article 272 supplies the corresponding asset/depreciation method and specified administrative/sales/non-production/financial expense proration; the turnover multipliers do not apply to micro. See the [regime Guide](armenia-tax-optimization.md) for the actual statements, return-field map and the separate VAT transition. [264, 272][code]

## Rates, bands and thresholds

| Item | Amount or period | Tax year and primary source |
|---|---|---|
| Ordinary corporate / attributable corporate-PE tax | 18% of established taxable profit | 2026, [125(1)][code] |
| Registered Armenian investment funds (not pension or guarantee funds) and securitisation foundations | 0.01% of net assets, as the special base | 2026, [125(2)][code] |
| Representation, established business | Up to 0.5% of annual gross income, capped at AMD 5 million | 2026, [116][code] |
| Representation, registration year | Separate AMD 5 million limit; ordinary percentage restriction does not apply | 2026, [116(2)][code] |
| General qualifying charitable deductions | Up to 0.25% of annual gross income | 2026, [123(1)(5)][code] |
| Specified licensed state/community education/foundation recipients | Separate qualifying category up to 2.5% | 2026, [123(1)(5.1)][code] |
| Small depreciable asset original cost | Up to AMD 50,000 inclusive, full acquisition-year deduction | 2026, [121(2)(1)][code] |
| Ordinary loss carryforward | Five tax years following origin year, with ordering/regime/reorganisation restrictions | 2026, [123(1)(4)][code] |
| Quarterly instalment | Lower of adjusted prior-year tax × 20% and defined prior-quarter income × 2%, after exceptions | 2026, Armenian [135][code] |

The English instalment sentence is ambiguous. The Armenian Article 135(1) expressly uses the minimum of the two calculated amounts. It is not a 2%-of-revenue floor, and no old March election should be invented after paragraph 4's repeal. Other English passages, including an exceptional historical asset-period wording, need Armenian verification before use. [135, 121][code]; [English reproduction][english]

HO-234-N restates representation and changes other base rules from its specified dates. Use its July 2026 gate with the actual period. HO-385-N's general February 2027 bank-dividend provisions are not October 2026 ordinary corporate rates; its specified expense amendment has a different commencement. Do not apply all provisions of an enacted law on publication without checking the transition. [HO-234-N, especially 23–25 and commencement][july]; [HO-385-N 14][future]

## The base

### Reconcile accounts to tax once

Start with complete accrual accounts and a gross-income ledger under Articles 104–109, then distinguish tax inclusion/exclusion, timing and deductions. A practical book-profit bridge adds back non-deductible amounts and book depreciation, deducts permitted tax depreciation and other legal deductions, and reconciles to the statutory gross-income-minus-deductions result. Do not deduct a cost twice through both inventory and overhead, or treat every cash payment as a current expense. [105–106, 108–111, 121][code]

Article 111 requires the prescribed supporting documents, subject to express exceptions. Article 121(7) matches production/trading costs to supplied goods/work/services or disposals; administrative/selling/financial expenses have their stated tax-year and capitalisation rules. Preserve contract, actual transaction date, invoice, receipt, inventory and asset evidence. An invoice date in another year does not alone decide the service expense period. [55, 111, 121(7)][code]

Articles 112–113 exclude or restrict categories including equity distributions/investments, specified revaluations, public-budget/tax sanctions, costs associated with excluded income, creditable indirect taxes and expenses beyond statutory caps. **Not all fines are the same:** Article 113(1)(1) disallows its public/pension/tax-controlled sanctions, while Article 121(8)(5) separately addresses other monetary sanctions. Do not automatically disallow a private contractual compensation or deduct a tax penalty. [112–113, 121(8)][code]

Supplier regime matters. Article 113(1)(8) restricts the stated micro-entrepreneurship purchases; paragraph (10) separately restricts listed high-technology activities purchased from turnover taxpayers. Validate supplier and activity at transaction date. This is not a blanket statement that every turnover-tax supplier invoice is nondeductible. No unsupported invoice-to-bank match proves statutory deductibility. [113][code]

### Capped costs and evidence

Representation means the stated cooperation-establishment/maintenance costs, not every travel, advertising or customer expense. Retain purpose and recipient evidence before applying the gross-income percentage/absolute cap. Travel and staff benefits have separate limits. For each category, deduct the eligible supported amount up to its own limit and add back the excess once in the book-to-tax bridge. [116–120][code]

| Ordinary cost | Deduction method and condition | Primary source |
|---|---|---|
| Offshore actual management services | Article 118 applies to the specified no-PE nonresident organisation/individual providers, including the stated PE/non-attributed income case. Deduct no more than 2% of annual gross income; in the statutory registration year the cap is the greater of 2% and AMD 2 million. The definition is actual direction of the taxpayer, excluding employee work, management consultancy and trust management. Apply 118(3)'s specific IT/computer innovation nonresident-founder and international credit/grant-agreement exceptions only on their established facts. This is separate from related-party pricing, benefit evidence and withholding. | [118(1)–(4)][code] |
| Foreign business trips | Ordinarily cap total eligible trip expenses at 5% of annual gross income. The registration year excludes that percentage restriction. For work/services actually performed abroad, use the separate 80% cap on the turnover separately identified in the customer contract or customer-approved settlement documents; without that evidence, revert to the 5% branch. Apply the daily limit as well. | [117(1)(1)–(2)][code] |
| Foreign per diem | Article 117 states AMD 30,000 per calendar day unless Government establishes another amount. Determine the actual destination/year rate through 2335-N and the current Ministry list, rather than using that statutory fallback for every country. | [117(1)(2)][code]; [2335-N Annex 1, 7.1–7.4][travel]; [official 2026 list][travellist] |
| Domestic per diem for profit tax | AMD 12,000 per calendar day; construction has the additional monthly worker salary/equivalent-payment cap. This tax-deduction ceiling is distinct from the travel-reimbursement minimum or budget-funded maximum. | [117(1)(3)][code] |
| Employer's qualifying voluntary pension payment for an employee | Deduct up to 7.5% of that employee's salary and equivalent payments; excess is disallowed. This is not the employee's PIT deduction cap. | [119(1)(1)][code] |
| Non-trip employee/contractor housing and utilities | Disallowed even if the employer undertakes to pay them, unless the contract states that the person's salary/remuneration includes those expenses. Contractual inclusion must be established; a promise to pay the landlord alone is insufficient. | [120(1)(1)][code] |
| Assistance, food, social/cultural and similar costs | Deduct up to 0.25% of annual gross income; only where there is no annual gross income use 1% of annual accrued salary/equivalent payments. Do not choose whichever limit is larger. | [120(1)(2)][code] |

For the foreign rate, open the Ministry's **2026** list, published 30 December 2025 and linked on its [year archive][travellist]. Match the country and city, the daily-expense column versus overnight-stay column, currency and actual trip dates. Under 2335-N Annex 1(7.3), a trip already in progress on 1 January uses the stated arithmetic-average transition between the two annual lists. A2024 search result or a government-funded hotel maximum is not the current foreign per diem. The Ministry table is an input lookup; no particular destination rate is assumed here. [2335-N Annex 1(7.1)–(7.4)][travel]; [actual 2026 document header][travel2026]

Donation deductions under Article 123 require actual recipient-category evidence and valuation; the special 2.5% category is not every educational or charitable payment. Track each deduction without counting it again as an ordinary expense. The separate personal PIT treatment of employee benefits is in the [payroll Guide](armenia-payroll.md). [119–120,123][code]

### Interest

Article 114 applies a per-loan interest-rate limitation based on twice the **31 December** CBA bank-interest settlement rate, not whichever monetary-policy rate a website displays today. The final 31 December 2026 input is not established on this October read. The example below deliberately uses a hypothetical established closing rate. Obtain the actual official rate for the tax year before final computation. [114(1)(1)][code]

For borrowings from nonbank/noncredit providers, Article 114(1)(2) separately limits the annual interest amount to twice positive closing tax equity for ordinary taxpayers, or nine times for the stated bank/credit population. Negative equity has the stated disallowance consequence; listed international-development/public debt-placement exceptions need evidence. This provision compares **interest amounts** with the equity-based amount; do not silently substitute a debt-to-equity principal ratio. [114(1)(2)][code]

Interest-free/low-yield onward lending and capitalised borrowing costs have additional rules in Article 114(1)(3)–(4). Record time, maximum relevant borrowing rates and overlap so the same disallowance is not added twice. A TP-supported rate does not override Article 114 or prove the business expense deductible. Complex portfolios, zero equity and exceptions require further implementation; the single-loan control assumes none applies. [114, 121(7)(5)][code]; [TP method](am-transfer-pricing.md)

### Tax depreciation and capital expenses

Ordinary minimum terms under Article 121(1)(3):

| Statutory asset group | Minimum years | Source |
|---|---|---|
| Ordinary buildings/structures and stated linear infrastructure | 20 | [121(1)(3), row 1][code] |
| Specified hotel/guest-house/sanatorium/education buildings | 10 | [row 2][code] |
| Production equipment | 5 | [row 3][code] |
| Conveyors/robotic technology | 3 | [row 4][code] |
| Computer/computational and communication equipment | 1 | [row 5][code] |
| Other fixed assets | 8 | [row 6][code] |

Use per-asset original cost/selected lawful term, with different rules for statutory revaluation and changed terms. Terms can be longer, not shorter than the applicable minimum absent an actual exception. Intangibles use the established possible-use period; where it cannot be determined, the statutory ten-year rule and taxpayer-life limit apply. Small assets up to 50,000 inclusive have a separate immediate-deduction rule. Do not extend a historic acquisition-window incentive to an ordinary 2026 purchase. [121(1)–(2)][code]

For ordinary acquisition/disposal/status changes, full months use annual deduction × months/12 and incomplete months use the separately stated annual deduction × days/365. Do not round every commencement up to a full month. The worked case uses six complete months and no incomplete period. Asset nonbusiness/leased status, land, useful-life changes, revaluations and different methods for specialised assets need their own statutory route. [121(1)(6)][code]

For each asset, keep original cost (or statutory revalued cost), opening carrying amount, remaining term and dated improvement entries. Article 121(3) requires these computations:

1. An individual expense **over 5%** of original/revalued cost is capital expenditure in full, not only its excess over 5%. Track separately the individual expenses not over 5%: once their tax-year aggregate exceeds 15% of original/revalued cost, only the excess over 15% is capital. Equal-to 5% entries belong to the cumulative test. Other qualifying current expenses are deductible in their year.
2. Add capital amounts to the carrying value as of the first day of the month incurred; for the cumulative branch, use the first day of the month the threshold is crossed. Start the revised depreciation that month; do not expense the capital amount and depreciate it again.
3. Compare that month's fixed-asset capital spending with the 1 January carrying amount, or original cost for an asset acquired later that year. If spending does not exceed that comparator, retain the remaining term. If it exceeds it, use at least the asset's statutory minimum where that minimum is under 8 years, or at least 8 years where the minimum is 8 years or more; retain a longer remaining term. Intangibles use their remaining amortisation term. [121(3)(1)(a)–(d), (2)][code]

For original cost AMD 10 million, a single AMD 600,000 improvement is all capital; a single AMD 500,000 expense instead enters the small-expense cumulative test. Four separate AMD 400,000 expenses total AMD 1.6 million: AMD 1.5 million remains current and AMD 100,000 is capital when that limit is crossed, assuming no other entries or special restrictions. [121(3)][code]

For leased/leasing/gratuitous-use assets, the relevant act/contract/acceptance document must place the improvement obligation on the user. Use the provider's documented original/carrying values and remaining term under 121(3)'s stated rules. For an ordinary private-person provider or nonresident organisation without a registered Armenian PE, use documented acquisition value and statutory minimum term. Missing values default to zero, except the listed real property uses 80% of its Article 228 property-tax base. Missing remaining term uses the statutory minimum. An unamortised lease-end improvement is not automatically deductible: the stated exception is a compensated disposal to the provider. Improvements to nondepreciable fixed assets, including land, use the other-fixed-assets minimum under the same conditions. [121(3), concluding points 1–5][code]

### Losses, bad debts and incentives

Calculate current-year expenses/losses first, then eligible prior losses oldest first within five following tax years. General-system losses do not stop aging while the taxpayer uses a special regime; losses generated in that special regime are not ordinary carryforwards. Division/separation/consolidation/absorption have explicit different rules; neither all succession nor all forfeiture is automatic. Retain origin-year tax returns, use, expiry, corrections and regime/reorganisation history. [123(1)(4)][code]

Book impairments are not automatically tax bad debts. The ordinary implementing rule is **1373-N Annex 1**, excluding its stated finance and utility populations and budget-tax/other excluded balances. Maintain debtor-level unpaid principal, due date, origin date, repayments, reserve, legal event and prior deductions. When a due date is absent, paragraph 4 uses the 60th day after the underlying event; partial payment does not postpone the unpaid balance's deadline. Unidentified repayments use oldest debt first under paragraph 6. [123(1)(2)][code]; [1373-N Annex 1, 2–10][baddebt]

If the taxpayer forms the permitted tax reserve, it covers only overdue receivables for delivered goods, works and services. Paragraph 12 uses cumulative percentages of the unpaid debt: days 1–90: 0%; 91–180: 25%; 181–270: 50%; 271–365: 75%. Compare the legally determined closing reserve with opening reserve: the increase is an other deduction and the decrease is gross income, rather than deducting the whole closing stock each year. A debt reaching day 366 without qualifying as hopeless requires reversal of its earlier reserve into income under paragraph 16. [1373-N Annex 1, 11–16][baddebt]

**Date gate:** HO-19-N, effective 3 March 2025, and 994-N both limit the new 300,000 threshold/enforcement wording to obligations arising **after 1 January 2025**. In that branch, total debt of a debtor not exceeding AMD 300,000 becomes hopeless from day 366; above AMD 300,000 use the specified effective judicial/payment-order, binding notarial-order or arbitral-award event, excluding the stated forgiveness/no-demand decisions. Paragraph 15(3) separately covers the listed bankruptcy, liquidation, deregistration, suspended-notary and death events. Test the debt's origin and actual legal event; do not apply 300,000 retroactively to every legacy balance. The separate pre-2025 threshold and legal-event method is supplied below. [123(1)(2)][code]; [HO-19-N 1–2][debtstatute]; [994-N 1–2][debtchange]; [1373-N Annex 1, 15][baddebt]

Without a tax reserve, deduct the qualifying hopeless debt in its write-off year under paragraph 19. With a reserve, deduct only the previously unreserved qualifying portion, applying paragraph 18's timing and paragraph 16's reversal where relevant; never deduct both the reserve and the same full debt. Later recovery or the specified forgiveness/assignment event restores the previously deducted amount to income. Ordinary hopeless payables have their separate day 366 income/write-off rule and a later payment deduction, subject to the stated Government exceptions. [123(1)(2)][code]; [1373-N Annex 1, 18–26][baddebt]

**Earlier obligations have a different threshold.** For obligations arising before 1 January 2025, preserve the prior **100,000** test rather than applying the new 300,000 test retroactively. The actual pre-amendment 1373-N consolidation, 13 October 2023–25 July 2025, gives day 366 recognition where the debtor's total debt does not exceed 100,000, and the qualified final court-act route above 100,000. Bankruptcy/liquidation/deregistration/notary cessation/death have their separately stated 15(3)/18 conditions. A new 2026 write-off does not itself change the obligation's origin date. Keep the originating contract/invoice and due date, debtor-total aggregation, reserve reversals, qualifying legal event and later collections together. [Prior 1373-N Annex 1, 15–20][baddebtprior]; [994-N 2][debtchange]; [HO-19-N 2][debtstatute]

The old constitutional annotation is not a current blanket write-off exemption. Actual **SDO-1436**, 27 November 2018, upheld the challenged Code provisions but held the then-Government 3(1)/(2) and 15(2) restrictions unconstitutional, with 1 May 2019 as the invalidation deadline. Subsequent **HO-68-N 30** expressly inserted the above 100,000 court-act condition into Code 123; its 71 expressly starts 30 the day after official publication. HO-19-N and 994-N then supply the distinct post 1 January 2025 threshold/enforcement changes. Do not treat a surviving annotation beside later amended text as proof that these later statutory conditions vanished. Reopening an actual pre 2019 assessment/dispute requires its own historical law/decision analysis. [SDO-1436 conclusions 1–7][debtcourt]; [HO-68-N 30/71][debt2019]; [HO-19-N][debtstatute]

### Inventory and asset losses: classify, substantiate, then deduct

Actual **1261-N** supplies the documentation procedure for quality, accidental, technological and other losses. Natural shrinkage has a separate **1467-N** schedule lookup. A management write-off or reserve is not itself one of these legal events. Retain the property class, quantities/book records, actual shortage, cause, dated evidence and applicable tax period. [122][code]; [1261-N Annex 1–12][lossdocs]; [1467-N][naturalloss]

| Loss class | Ordinary tax method and timing |
|---|---|
|Natural shrinkage|Physical/chemical/mechanical/biological reduction during storage/transport. Deduct actual loss only up to the **applicable Government norm** in the occurrence/discovery year. **No established Government norm means no deduction under this limb**; excess is not an automatic other-loss deduction. Match commodity, process, storage/transport conditions, unit and period. |
|Documented quality loss|Ordinary property: cap at **1%of the loss occurrence/discovery year's gross income**, in that year, with 1261-N withdrawal/defect evidence. Expired/deteriorated/prohibited goods and specified manufacturing defects/returned warranty goods have the statutory definition; exclude defective goods for which supplier compensation is received or receivable. |
|Accidental loss|Full documented loss in occurrence/discovery year for the listed extraordinary events, with inventory reconciliation and the appropriate competent authority's event evidence. Theft/shortage is not automatically a documented fire or other extraordinary event. |
|Technological loss|Documented process/material loss within the taxpayer's supported production norm or legally prescribed norm is a material-cost element matched under 121(7), rather than a second immediate overhead deduction. No norm/excess follows 122(7)'s event route. |
|Other actual loss / technological excess or no norm|Deduct in the year of actual full/partial voluntary compensation by the responsible person, qualifying investigation suspension/termination for failure to identify the person, or entry into force of the stated court act on guilt/innocence. Use the actual 122(7) event and amount, not merely the year a shortage was booked. |

[122(1)–(8)][code]. **Midyear specialist gate:** HO-234-N 26 adds the separate **2%** annual-gross-income quality-loss branch for the stated stampable dairy/ice-cream tariff codes 0401–0406 and 210500, from **1 July 2026** under 33(1). The ordinary 1%branch remains for other property. Do not backdate the new clause or manufacture two additive annual allowances; a mixed-period dairy calculation needs the actual periods/commodity evidence. [HO-234-N 26/33][july]

Under 1261-N, quality loss needs the defect/withdrawal act and actual write-off; accidental/other loss needs inventory lists and book-versus-physical comparison. Technological loss needs process documentation/material-use report and the actual-loss or defect act, separately by property type. Accidental events additionally need competent-authority evidence; historical ministry names in the procedure are not a verified 2026 agency directory. The written-off goods must be destroyed/transferred or remain actually available, except property actually lost/destroyed. Record destruction/transfer date/place/method, names/quantities, participants and signatures; inventory documents also record start/end dates and committee/material-responsibility details. Documents are signed by the responsible head/substitute or duly authorised person. There is no invented compulsory prior SRCapproval or unsupported destruction notification in this procedure. [1261-N 3–12][lossdocs]

For natural shrinkage, current 1467-N identifies 12 commodity schedules. Use the exact current annex/row, not a universal percentage of turnover. Its Annex 2 construction-material formula is **norm quantity = recorded quantity × applicable percent /100**, bounded by actual shortage; supplier-arranged transport loss is calculated at the supplier under paragraph 4. For cement, actual Annex 2 row 1 gives storage 0.2%, rail 0.5%, road 0.4% of natural quantity. These do not excuse breaches of handling/storage rules. Current Annex 9 fresh-produce rules were replaced by 1326-N for relationships from 1 January 2025; general paragraph 5 permits the limit only after an actual shortage and prohibits advance write-offs. Detailed commodity/temperature/time catalogues are separate specialist inputs, not invented global rates. [1467-N 1/Annex 2, 1–4/row 1][naturalloss]; [1326-N 1–2/Annex 1–5][naturallossamend]

Once the permitted tax loss is established, reconcile the VAT consequence separately under 73(6): nondeductible acquisition losses do not support input credit, and annual norms require the year's last VAT-period true-up. The profit-tax deduction and input-VAT correction are separate entries; do not claim loss value and its blocked VAT twice. [73(6)/122][code]; [VAT method](armenia-vat.md)

Resident dividends and enhanced disability/technology/R&D deductions have separate statutory provisions. Technology/R&D benefits require current activity/occupation lists, status/commission evidence, applicable date and base caps; no automatic deduction is granted merely because a company develops software. Specific banks/funds, mining, agriculture, films, border-area and other relief need dedicated implementation. Future bank-dividend rules must be reconciled separately. [123–127][code]; [HO-385-N][future]

## Deadlines and filing

The ordinary annual resident/PE profit-tax return and payment are due by 20 April inclusive of the following tax year under Articles 134(1)/136(1). Thus the statutory date for 2026 is 20 April 2027, before separately established calendar adjustments/extensions. Quarterly advances are due by the 20th of the quarter's last month. Keep annual tax, advances calculated/paid, credits and the authority ledger separate. [130–136][code]

For each advance, compute the lower of 20% of **adjusted** prior-year tax and 2% of Article 135's defined prior-quarter supply/work/service income. The prior-tax limb excludes the listed special-regime, relief, non-attributed PE, foreign-tax and audit amounts; the income limb uses the specified VAT/excise-return bases submitted by the advance deadline, with rules for later corrections. The new prior-year return affects the next advance under paragraph 2.1; paragraph 3 supplies the pre-filing fallback. Do not substitute accounting turnover or divide an annual liability by four. [135(1)–(3)][code]

Paragraphs 5–8 address registration year, VAT-status changes, a later authority finding, properly declared inactivity and different reorganisations. Do not turn these into a blanket no-advance election. Keep the declaration and dates; an inactive bank account is not an inactivity filing. [135(5)–(8)][code]

### Actual published return structure

The actual 749-N **July 2026 consolidation**, not its earlier 2018–2024 text, provides Annex 1 for ordinary resident/PE profit tax. Prepare a positive-value workpaper and deliberately translate deductions into the form's parenthesised/sign convention. [749-N Annex 1 and instructions][return]

| Published field | Workpaper reconciliation |
|---|---|
| 6–40, total 41 | Income by statutory category, not bank credits |
| 42–61, total 62 | Permitted current costs after caps, timing and document checks |
| 63–66, total 67 | Qualified current losses |
| 76 | Eligible prior five-year losses, with special-regime aging preserved |
| 68–82 / totals 83–84 | Other deductions and total deductions; special items need exact mapping |
| 85–88 | Tax profit/loss, relief and computed annual tax |
| 93–96 | Resident foreign-credit opening/current/use/carry, under Article 20 |
| 97 | Stated tax-agent withholding credit for PE-attributed income |
| 98–100 | Tax after the stated reductions, plus non-PE-attributed income tax if applicable, produces total tax 100 |
| 101–102 | Calculated annual advances 101 are a parenthesised deduction; 102 is the positive remaining balance |
| 103–105 | Only qualifying resident organisations use historic minimum-tax carry under 451(7), with 104 payment and 105 carry; not a general new credit |
| 106 | Negative result of its expressly listed signed components is the return's reimbursable amount; it is not automatically a bank refund |
| 107 | Separate monthly profit tax for the specified turnover-tax entrepreneur, not another company deduction |

Source: [actual 749-N form and instructions 1/19–36][return]. Translate positive workpaper deductions into signed/parenthesised values deliberately. Without foreign/PE/special credits or historic minimum-tax carry, tax 100 less calculated advances 101 gives positive payment 104, or the corresponding signed excess in 106. Reconcile calculated advances with cash and the authority account; an unpaid calculated advance does not prove a refundable cash payment. Printed special-deduction row discrepancies do not change the statute. No taxpayer return was submitted.

### Foreign credit: legal cap first, then signed return reconciliation

Only **resident taxpayers** complete 749-N 93–96. Start with evidence of corresponding foreign tax actually collected. ApplyCode 20(3)'s Armenian tax on the foreign object as the first limit; foreign tax excluded at this step is not an eligible carryforward. Keep each source/object/year separately. Then add only eligible opening carry to the current eligible credit; use no more than the corresponding year's Armenian tax liability, carrying eligible unused amounts under 20(4). Do not refund the excess as cash or duplicate an amount already used. [20/130(1)(2)][code]; [749-N instructions 24–25][return]

For the ordinary resident-company branch without competing relief/credits, define positive workpaper values `opening_eligible`, `current_eligible` and `liability_before_foreign_credit`. Then `available = opening_eligible + current_eligible`; `used = min(available, liability_before_foreign_credit)`; `carry = available − used`; `remaining_tax = liability_before_foreign_credit − used`. Carry amounts retain their originating-year/object records and are not a second current expense. PE withholding in 97 is a different credit, not a foreign-credit opening balance. [20(2)–(4)/130][code]; [749-N instructions 24–27][return]

The published form marks 93/94/95/96 as parenthesised deductions. Reconcile 93 to negative opening eligible, 94 to negative current eligible, 95 to negative **used**, 96 to negative unused **carry**, and 98 to the remaining positive liability. **Printed formula defect:** field 95 compares the signed sum 93+94 with positive 92; mechanically applying it to negative deduction inputs selects the whole available amount even when its magnitude exceeds the year's liability. That contradictsCode 20's limited-use/carry method and can consume carry incorrectly. The statutory workpaper above controls; retain the discrepancy and verify the actual electronic field behaviour before filing. Do not invent that the portal has corrected it, enter a positive credit to hide it, or let an excessive negative credit generate a cash refund. [20(3)–(4)][code]; [actual 749-N fields 92–98/instructions 1/24–27][return]

### Ordinary correction and cash refund

Correct an independently discovered error in the **original reporting period** under 54, preserving original/amended income, deduction, loss and credit registers. Under 54(4), a correction which creates/increases liability gives the stated under-declaration-fine relief; it is not a blanket late-payment-interest or late-filing waiver. Apply 53(10)–(12)'s already-checked/studied and period restrictions, with 53(10.1)'s distinct liability-increasing/credit-reducing route. Ordinary three-year restrictions are not the TPfive-year branch. Retain the 53(7) electronic receipt and reconcile submission-date liability/account movements; a saved draft is not a filed amendment. [53–54][code]

Return 106 or an unallocated bank credit does not itself establish cash refundable. First reconcile actual available unified-account/administrative-act-account funds after 325 allocation, including pension priority, and distinguish calculated advances from cash remitted. Apply for the **available requested amount** under 327(2) using current **246-N Annex 2**, operative 1 January 2025 onward: taxpayer TIN/name/address, public-service identifier for the applicable individual branch, bank/Treasury and account route, requested AMD amount/total and responsible-person signature/name. Current form item 4 is repealed, although the older instruction still describes that line; do not invent a mandatory deleted field. Special successor/heir/no-account columns require their specified legal population. [325/327(2)][code]; [246-N Annex 2/form/instructions 1–10][refundform]

The ordinary statutory refund period is **20 days after application receipt**, or **10 days** with the current law-abiding-taxpayer certificate. Treasury transfers through the authorised bank/account route. Neither period begins merely when a loss, negative annual return or nominal credit is computed.327 has a separate delayed-refund-compensation test; the marked HO-344-N change begins 1 January 2027 and is not substituted for current 2026 law. No actual refund application/acceptance is claimed. A nonresident's treaty-refund approval/settlement remains a separate procedure, not proof that a foreign recipient can use the Armenian agent's available account balance directly. [327(2)][code]; [cross-border method](am-cross-border.md)

## Penalties and interest

Current Article 401 ordinarily charges 0.075% late-payment interest per day, with its 730-day maximum/scope. Article 402 charges 5% of calculated tax for each completed 15-day late-return interval subject to its stop rules and cap at calculated tax. Article 403 provides ordinary under-declaration sanctions of 50%, and 100% for the specified recurrence, with exceptions. Classify actual offence, original due date, correction and assessment before combining amounts. Private contractual damages are a separate deduction question. [401–403][code]

Full amended-return relief, administrative offences, service/audit/appeal/suspension, interest interaction and enforcement need actual procedural evidence. No guessed appeal period, penalty waiver or filing-extension payment holiday. [54, 401–403][code]

## Cross-border points

Foreign objects/credits, PE attribution, nonresident withholding and treaty relief have distinct bases and clocks. Use the [cross-border method](am-cross-border.md) for the source/attribution/credit bridge and the [TP method](am-transfer-pricing.md) for related transactions. Preserve the actual treaty/protocol/MLI and relief procedure; neither treaty presence nor TP arm's-length pricing establishes a CIT deduction. The TP Guide supplies the prescribed 1032-N controlled-transaction adjustment return. Specialist asset/exit and international anti-avoidance methods remain outside this ordinary method. [20, 27, 107, 125, 130–133, Chapter 73][code]

## Two worked examples that recompute

Hypothetical AMD, ordinary established 2026 corporate scope, no unmentioned relief or competing credits. Inputs described as eligible/allowable require their own evidence.

### 1. Book-to-tax bridge and annual balance

Book profit 30 million already includes public tax fine 500,000 and book depreciation 3 million. Add them back; replace with established tax depreciation 4 million. Current tax result 29.5 million; eligible prior loss 5 million leaves taxable profit 24.5 million. At 18%, annual tax 4.41 million; established credited advances 3 million leave 1.41 million. No second deduction of the same depreciation/loss. [110–113, 121, 123, 125, 130][code]

```oa-check
name: Armenia ordinary corporate book to tax bridge
inputs:
  book_profit: 30000000
  public_tax_fine: 500000
  book_depreciation: 3000000
  established_tax_depreciation: 4000000
  eligible_prior_loss: 5000000
  credited_advances: 3000000
steps:
  - current_tax_result: book_profit + public_tax_fine + book_depreciation - established_tax_depreciation
  - prior_loss_used: min(eligible_prior_loss, max(current_tax_result, 0))
  - taxable_profit: max(current_tax_result - prior_loss_used, 0)
  - annual_tax: taxable_profit * 0.18
  - remaining_payment: max(annual_tax - credited_advances, 0)
expected:
  current_tax_result: 29500000
  taxable_profit: 24500000
  annual_tax: 4410000
  remaining_payment: 1410000
```

### 4. Loss expiry and oldest-first use

After current-year deductions, 2026 positive result 10 million. Ordinary verified unused 2021 loss 8 million is in its fifth following tax year; 2023 loss 6 million remains eligible. Use 8 million then 2 million, leaving 2023 balance 4 million. A separate 2020 balance expired before 2026 and is excluded; no special-regime pause or reorganisation. [123(1)(4)][code]

```oa-check
name: Armenia loss aging and oldest first use
inputs:
  current_result_after_current_deductions: 10000000
  eligible_loss_2021: 8000000
  eligible_loss_2023: 6000000
steps:
  - use_2021: min(current_result_after_current_deductions, eligible_loss_2021)
  - profit_after_2021: max(current_result_after_current_deductions - use_2021, 0)
  - use_2023: min(profit_after_2021, eligible_loss_2023)
  - remaining_loss_2023: eligible_loss_2023 - use_2023
  - taxable_profit: max(profit_after_2021 - use_2023, 0)
expected:
  use_2021: 8000000
  use_2023: 2000000
  remaining_loss_2023: 4000000
  taxable_profit: 0
```

## Ask the client first

- What legal form, tax regime, activity codes, elections, registrations and transitions apply for each period?
- Which ledgers, inventory, invoices, asset commencement dates and supplier regimes support income and deductions?
- Which representation/travel/benefit/donation/interest amounts need a cap or legal-status check?
- What tax loss origins, prior use, special-regime years or reorganisations affect carryforward?
- What VAT-return bases, prior CIT returns, advances, foreign credits, relief decisions and assessments exist?

Handoff: accounts-to-tax bridge; cap/deduction registers; asset/improvement roll-forward; dated debt/reserve/write-off ledger; tax-loss aging; exact advance calculation/history; signed form/credit mapping and payment/authority reconciliation. The ordinary small-business turnover/micro eligibility, transition and computation method is supplied here and in the linked regime Guide. Loss documentation, legacy debt threshold, statutory foreign-credit reconciliation and general correction/refund routes are supplied. Specialist incentives and industry assets are separately excluded. Independent country review and named accountant attestation remain pending.

## Sources

Read **24 October 2026**: targeted current Armenian Code Articles 103–125, 130–136, 254/267 screening, 401–403; English supporting translation; actual HO-234-N change/commencement and HO-385-N date gates; published 749-N July 2026 ordinary form and targeted instructions. No accepted filing, actual year-end CBA input, taxpayer facts, real benefit eligibility or professional attestation obtained.

| Primary source | URL | Read on |
|---|---|---|
| Native Code, complete small-business Articles 30, 254–270, 272 and Annex 3; targeted VAT status 59(1) | https://www.arlis.am/hy/acts/215611/latest | 2026-10-26 |
| Native Code, complete Article 118 offshore management cost, registration-year cap, exceptions and definition | https://www.arlis.am/hy/acts/215611/latest | 2026-10-26 |
| Current Armenian Tax Code | https://www.arlis.am/hy/acts/215611/latest | 2026-10-24 |
| English translation, read with current Armenian corrections | https://www.arlis.am/en/acts/231892 | 2026-10-24 |
| HO-234-N 2026 base changes | https://www.arlis.am/hy/acts/226008 | 2026-10-24 |
| HO-385-N future dividend changes | https://www.arlis.am/hy/acts/228632 | 2026-10-24 |
| 749-N return, current July 2026 consolidation | https://www.arlis.am/hy/acts/226558 | 2026-10-24 |
| Targeted current native 117,119–121(3), 123(1)(2), 135; supporting English read against native | https://www.arlis.am/hy/acts/215611/latest | 2026-10-25 |
| 1373-N current ordinary Annex 1, reserve and debt methods | https://www.arlis.am/hy/acts/183923/latest | 2026-10-25 |
| 994-N threshold/enforcement amendment and origin-date transition | https://www.arlis.am/hy/acts/209809/latest | 2026-10-25 |
| HO-19-N 1–2, statutory threshold/enforcement and origin-date transition | https://www.arlis.am/hy/acts/203083 | 2026-10-25 |
| 2335-N current Annex 1, targeted 7/7.1–7.4 travel method | https://www.arlis.am/hy/acts/219376/latest | 2026-10-25 |
| Ministry official travel-list archive and 2026 document header/column structure | https://welfare.gov.am/travel-expense-rates | 2026-10-25 |
| 749-N Annex 1, targeted ordinary settlement fields and instructions 30–36 | https://www.arlis.am/hy/acts/226558/latest | 2026-10-25 |

| Fresh native 20/130 and current 749-N Annex 1 fields 92–98/instructions 1/24–27: eligible foreign-credit use/carry, signed mapping and explicit printed 95 comparison defect | https://www.arlis.am/hy/acts/215611/latest ; https://www.arlis.am/hy/acts/226558/latest |2026-10-26|

| Fresh current native 122 in full, 123(1)(2), 73(6), 53–54/325/327(2): loss classes/caps/events, original-period amendments, available-account refund and clocks | https://www.arlis.am/hy/acts/215611/latest |2026-10-26|
| Current 1261-N complete Annex 1–12 and actual 1928-N operative amendment/2022 transition | https://www.arlis.am/hy/acts/171651/latest ; https://www.arlis.am/hy/acts/171646/latest |2026-10-26|
| Current 1467-N operative 1/metadata, complete Annex 2 construction-material method/table, targeted current Annex 9 general 1–5; actual 1326-N 1–2/2025 transition | https://www.arlis.am/hy/acts/127175/latest ; https://www.arlis.am/hy/acts/212429/latest |2026-10-26|
| Fresh current HO-234-N 26/33: special 2%quality-loss category and 1 July 2026 gate; ordinary 1%remains separate | https://www.arlis.am/hy/acts/226008/latest |2026-10-26|
| Prior 1373-N Annex 1, 15–20 and 13 October 2023–25 July 2025 metadata, compared with current paragraph 15/2025 origin-date transition | https://www.arlis.am/hy/acts/183923 ; https://www.arlis.am/hy/acts/183923/latest |2026-10-26|
| Actual SDO-1436 operative conclusions 1–7, 27 November 2018; subsequent HO-68-N 30 and targeted 71 commencement, not a current blanket exemption from later statute | https://www.arlis.am/hy/acts/126792/latest ; https://www.arlis.am/hy/acts/131962/latest |2026-10-26|
|246-N Annex 2 ordinary refund form/instructions reread from actual 25 Octoberretrieval; no fresh 26 Octoberretrieval claimed | https://www.arlis.am/hy/acts/144655/latest |2026-10-26|

[code]: https://www.arlis.am/hy/acts/215611/latest
[english]: https://www.arlis.am/en/acts/231892
[july]: https://www.arlis.am/hy/acts/226008
[future]: https://www.arlis.am/hy/acts/228632
[return]: https://www.arlis.am/hy/acts/226558
[baddebt]: https://www.arlis.am/hy/acts/183923/latest
[debtchange]: https://www.arlis.am/hy/acts/209809/latest
[debtstatute]: https://www.arlis.am/hy/acts/203083
[travel]: https://www.arlis.am/hy/acts/219376/latest
[travellist]: https://welfare.gov.am/travel-expense-rates
[travel2026]: https://welfare.gov.am/api/assets/7568427a-3fe6-4852-9e5d-348e3a87d25d

[lossdocs]: https://www.arlis.am/hy/acts/171651/latest

[naturalloss]: https://www.arlis.am/hy/acts/127175/latest

[naturallossamend]: https://www.arlis.am/hy/acts/212429/latest

[baddebtprior]: https://www.arlis.am/hy/acts/183923

[debtcourt]: https://www.arlis.am/hy/acts/126792/latest

[debt2019]: https://www.arlis.am/hy/acts/131962/latest

[refundform]: https://www.arlis.am/hy/acts/144655/latest

**Not yet confirmed:** actual electronic resolution of the printed foreign-credit 95 formula defect. Reopening pre 2019 debt assessments, exhaustive commodity norms, mixed-period specialist dairy losses and sector incentives require their separate instruments/facts. Specialist schemes and actual taxpayer facts require their stated separate evidence; no professional attestation has been obtained.

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
