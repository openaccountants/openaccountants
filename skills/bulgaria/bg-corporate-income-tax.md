---
name: bg-corporate-income-tax
description: "Bulgarian corporate income tax (корпоративен данък) for tax year 2026 under the Corporate Income Tax Act (ZKPO). Covers who pays; the 10% rate; the tax result built from the accounting result with permanent and temporary differences; non-deductible expenses and hidden profit distribution; tax depreciation categories I to VII and their maximum rates; tax losses carried forward for five years; the 3:1 thin capitalisation rule (art. 43) and the 30% EBITDA interest limitation above EUR 3,000,000 (art. 43a); monthly and quarterly advance payments and their euro thresholds; the annual return (1 March to 30 June) and payment; penalties; and pointers to the expenses tax, alternative taxes, CFC rules and Pillar Two. All lev amounts are shown in euro at BGN 1.95583. Trigger phrases: Bulgaria corporate tax, ZKPO, ЗКПО, Bulgarian CIT return, авансови вноски, данъчна загуба Bulgaria. Out of scope: withholding tax, treaties and exit tax (bg-cross-border), transfer pricing (bg-transfer-pricing), individuals (bulgaria-income-tax), VAT (bulgaria-vat-return)."
version: 0.3
type: computation
jurisdiction: BG
tax_year: 2026
last_updated: 2026-11-28
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: corporate-tax
---

# Bulgaria corporate income tax (2026)

For **2026**, ordinary Bulgarian corporate income tax is **10%** of taxable profit. Build the tax result from the accounts, apply the adjustments below, then deduct available tax losses and credit advances actually paid. The normal annual return window is **1 March–30 June 2027**, with payment by **30 June 2027**. Special regimes and the non-usable outcomes below require separate work.

The ordinary tax period is the calendar year; new-company and other statutory short periods need their own dates (ZKPO art.21). Bulgaria adopted the euro on **1 January 2026**. Divide lev values by **1.95583**, using the complete rate, and normally round to cents half-up; a specific statutory replacement or rounding rule takes priority (Euro Act arts.11–13). Do not convert an expressly euro-denominated **EUR3,000,000** interest threshold again. Historical BGN amounts and case years below remain as originally given. [Euro Act](https://www.evroto.bg/upload/1068/ZVERB.pdf); [Council Regulation2025/1409, arts.1–2](https://eur-lex.europa.eu/eli/reg/2025/1409/oj/eng/pdf).

## Scope

- **Resident companies** (ZKPO art. 3): legal entities incorporated under Bulgarian law, and SEs and SCEs with their seat in Bulgaria and entered in a Bulgarian register. They are taxed on profits from all sources.
- **Foreign companies** with a Bulgarian place of business (permanent establishment) are taxed on the profit of that establishment and file the same annual return (arts. 1(3), 2(1)(2)). Their other Bulgarian-source income is taxed by withholding (see `bg-cross-border`).
- **Non-profit legal entities** are covered for the specified commercial/rental profits, subject to statutory exemptions. **Sole traders** (ЕТ) are not ordinary company-CIT filers on that basis alone: art.2(1)(3) brings them into specified withholding/PIT-linked cases. Their own income-tax computation belongs in `bulgaria-income-tax`; do not apply this company rate automatically.
- **Alternative regimes** apply only to activities actually covered by them. Do not assume all gambling is outside CIT: online machine/casino games are within CIT (art.242(2)). Budget-enterprise and elective shipping regimes are separate; other activities can remain within CIT (arts.5,218). Actual special-regime eligibility/calculations are held below.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Corporate income tax rate | 10% of taxable profit | 2026 | ZKPO arts. 19, 20, [official NRA text](https://nra.bg/wps/wcm/connect/nra.bg25863/ed10ff12-b25a-4b07-827c-915979acef42/ZAKON%2BZA%2BKORPORATIVNOTO%2BPODOHODNO%2BOBLAGANE_60.pdf?CACHEID=ROOTWORKSPACE.Z18_PPGAHG8009LJC0QTR5C2HH30I6-ed10ff12-b25a-4b07-827c-915979acef42-nEJyDbV&MOD=AJPERES) |
| Ordinary tangible / acquired nonfinancial intangible asset threshold | Lower of the applicable accounting-policy threshold and BGN700 (EUR357.90); tangible assets must meet the statutory depreciable-asset criteria; acquired intangibles need use beyond12months and a limited useful life. Separate lease/subsequent-expenditure cases need review | 2026 | ZKPO arts. 50(1), 51(1); Euro Introduction Act arts. 12, 13, https://nra.bg/wps/wcm/connect/nra.bg25863/ed10ff12-b25a-4b07-827c-915979acef42/ZAKON%2BZA%2BKORPORATIVNOTO%2BPODOHODNO%2BOBLAGANE_60.pdf?CACHEID=ROOTWORKSPACE.Z18_PPGAHG8009LJC0QTR5C2HH30I6-ed10ff12-b25a-4b07-827c-915979acef42-nEJyDbV&MOD=AJPERES |
| Depreciation, category I: massive buildings, investment property, facilities, power and communication lines | Up to 4% a year | 2026 | ZKPO art. 55(1), (2), https://nra.bg/wps/wcm/connect/nra.bg25863/ed10ff12-b25a-4b07-827c-915979acef42/ZAKON%2BZA%2BKORPORATIVNOTO%2BPODOHODNO%2BOBLAGANE_60.pdf?CACHEID=ROOTWORKSPACE.Z18_PPGAHG8009LJC0QTR5C2HH30I6-ed10ff12-b25a-4b07-827c-915979acef42-nEJyDbV&MOD=AJPERES |
| Category II: machines, production equipment, apparatus | Up to 30%; ordinary 50% exception requires factory-new, never previously used assets forming an initial investment. Special art.55(6) energy-efficiency cases require separate review | 2026 | ZKPO art. 55(2), (3), https://nra.bg/wps/wcm/connect/nra.bg25863/ed10ff12-b25a-4b07-827c-915979acef42/ZAKON%2BZA%2BKORPORATIVNOTO%2BPODOHODNO%2BOBLAGANE_60.pdf?CACHEID=ROOTWORKSPACE.Z18_PPGAHG8009LJC0QTR5C2HH30I6-ed10ff12-b25a-4b07-827c-915979acef42-nEJyDbV&MOD=AJPERES |
| Category III: transport vehicles other than cars; road and runway surfaces | Up to 10% | 2026 | ZKPO art. 55(2), https://nra.bg/wps/wcm/connect/nra.bg25863/ed10ff12-b25a-4b07-827c-915979acef42/ZAKON%2BZA%2BKORPORATIVNOTO%2BPODOHODNO%2BOBLAGANE_60.pdf?CACHEID=ROOTWORKSPACE.Z18_PPGAHG8009LJC0QTR5C2HH30I6-ed10ff12-b25a-4b07-827c-915979acef42-nEJyDbV&MOD=AJPERES |
| Category IV: computers, peripherals, software and rights to use software, mobile phones | Up to 50% (100% for software on the list in VAT Act art. 118(16) and devices running it) | 2026 | ZKPO art. 55(2), (7), https://nra.bg/wps/wcm/connect/nra.bg25863/ed10ff12-b25a-4b07-827c-915979acef42/ZAKON%2BZA%2BKORPORATIVNOTO%2BPODOHODNO%2BOBLAGANE_60.pdf?CACHEID=ROOTWORKSPACE.Z18_PPGAHG8009LJC0QTR5C2HH30I6-ed10ff12-b25a-4b07-827c-915979acef42-nEJyDbV&MOD=AJPERES |
| Category V: cars | Up to 25%; special 50% maximum for electric cars acquired on or after 1 January 2026 (2026 amending Act applicability provision) | 2026 | ZKPO art. 55(2), (8) as amended by ДВ 30/2026, https://nra.bg/wps/wcm/connect/nra.bg25863/ed10ff12-b25a-4b07-827c-915979acef42/ZAKON%2BZA%2BKORPORATIVNOTO%2BPODOHODNO%2BOBLAGANE_60.pdf?CACHEID=ROOTWORKSPACE.Z18_PPGAHG8009LJC0QTR5C2HH30I6-ed10ff12-b25a-4b07-827c-915979acef42-nEJyDbV&MOD=AJPERES |
| Category VI: assets with a contractual or legal limit on use | 100 / years of the limit, capped at 33 1/3% | 2026 | ZKPO art. 55(2), https://nra.bg/wps/wcm/connect/nra.bg25863/ed10ff12-b25a-4b07-827c-915979acef42/ZAKON%2BZA%2BKORPORATIVNOTO%2BPODOHODNO%2BOBLAGANE_60.pdf?CACHEID=ROOTWORKSPACE.Z18_PPGAHG8009LJC0QTR5C2HH30I6-ed10ff12-b25a-4b07-827c-915979acef42-nEJyDbV&MOD=AJPERES |
| Category VII: all other depreciable assets | Up to 15% | 2026 | ZKPO art. 55(2), https://nra.bg/wps/wcm/connect/nra.bg25863/ed10ff12-b25a-4b07-827c-915979acef42/ZAKON%2BZA%2BKORPORATIVNOTO%2BPODOHODNO%2BOBLAGANE_60.pdf?CACHEID=ROOTWORKSPACE.Z18_PPGAHG8009LJC0QTR5C2HH30I6-ed10ff12-b25a-4b07-827c-915979acef42-nEJyDbV&MOD=AJPERES |
| Tax loss carry-forward | Next 5 years, oldest first, up to the positive tax result; election starts in the first eligible profitable year | 2026 | ZKPO arts. 70, 71, 72, https://nra.bg/wps/wcm/connect/nra.bg25863/ed10ff12-b25a-4b07-827c-915979acef42/ZAKON%2BZA%2BKORPORATIVNOTO%2BPODOHODNO%2BOBLAGANE_60.pdf?CACHEID=ROOTWORKSPACE.Z18_PPGAHG8009LJC0QTR5C2HH30I6-ed10ff12-b25a-4b07-827c-915979acef42-nEJyDbV&MOD=AJPERES |
| R&D extra deduction | Further 25% of qualifying current R&D expense; market terms for commissioned work, no public funding including at group level, and all other statutory conditions; capitalized development follows art.69(2)–(3), not an immediate extra deduction | 2026 | ZKPO art. 69 as amended by ДВ 30/2026, https://nra.bg/wps/wcm/connect/nra.bg25863/ed10ff12-b25a-4b07-827c-915979acef42/ZAKON%2BZA%2BKORPORATIVNOTO%2BPODOHODNO%2BOBLAGANE_60.pdf?CACHEID=ROOTWORKSPACE.Z18_PPGAHG8009LJC0QTR5C2HH30I6-ed10ff12-b25a-4b07-827c-915979acef42-nEJyDbV&MOD=AJPERES |
| Thin capitalisation (art. 43) applies when | Average debt is more than 3 times average equity | 2026 | ZKPO art. 43(6), https://nra.bg/wps/wcm/connect/nra.bg25863/ed10ff12-b25a-4b07-827c-915979acef42/ZAKON%2BZA%2BKORPORATIVNOTO%2BPODOHODNO%2BOBLAGANE_60.pdf?CACHEID=ROOTWORKSPACE.Z18_PPGAHG8009LJC0QTR5C2HH30I6-ed10ff12-b25a-4b07-827c-915979acef42-nEJyDbV&MOD=AJPERES |
| Thin capitalisation allowance | Relevant net interest above 75% of the accounting result before interest is disallowed, carried forward; omit a negative pre-interest result from the formula | 2026 | ZKPO art. 43(1), (2), https://nra.bg/wps/wcm/connect/nra.bg25863/ed10ff12-b25a-4b07-827c-915979acef42/ZAKON%2BZA%2BKORPORATIVNOTO%2BPODOHODNO%2BOBLAGANE_60.pdf?CACHEID=ROOTWORKSPACE.Z18_PPGAHG8009LJC0QTR5C2HH30I6-ed10ff12-b25a-4b07-827c-915979acef42-nEJyDbV&MOD=AJPERES |
| Interest limitation (art. 43a) applies when | Exceeding borrowing costs are more than EUR 3,000,000 | 2026 | ZKPO art. 43a(7), wording set by Euro Introduction Act § 36, https://nra.bg/wps/wcm/connect/nra.bg25863/ed10ff12-b25a-4b07-827c-915979acef42/ZAKON%2BZA%2BKORPORATIVNOTO%2BPODOHODNO%2BOBLAGANE_60.pdf?CACHEID=ROOTWORKSPACE.Z18_PPGAHG8009LJC0QTR5C2HH30I6-ed10ff12-b25a-4b07-827c-915979acef42-nEJyDbV&MOD=AJPERES |
| Interest limitation allowance | 30% of tax EBITDA; excess carried forward with no time limit | 2026 | ZKPO art. 43a(1), (5), https://nra.bg/wps/wcm/connect/nra.bg25863/ed10ff12-b25a-4b07-827c-915979acef42/ZAKON%2BZA%2BKORPORATIVNOTO%2BPODOHODNO%2BOBLAGANE_60.pdf?CACHEID=ROOTWORKSPACE.Z18_PPGAHG8009LJC0QTR5C2HH30I6-ed10ff12-b25a-4b07-827c-915979acef42-nEJyDbV&MOD=AJPERES |
| Donations | Deductible up to 10% of positive accounting profit for listed recipients; 50% for the specified NHIF child-treatment/assisted-reproduction recipients, 15% qualifying patronage; overall cap65%. No direct/indirect benefit to those directing the donation; receipt must be evidenced; EU/EEA equivalent recipients need the prescribed legalized status document and sworn Bulgarian translation | 2026 | ZKPO art. 31, https://nra.bg/wps/wcm/connect/nra.bg25863/ed10ff12-b25a-4b07-827c-915979acef42/ZAKON%2BZA%2BKORPORATIVNOTO%2BPODOHODNO%2BOBLAGANE_60.pdf?CACHEID=ROOTWORKSPACE.Z18_PPGAHG8009LJC0QTR5C2HH30I6-ed10ff12-b25a-4b07-827c-915979acef42-nEJyDbV&MOD=AJPERES |
| No advance payments | Net sales in the year before the preceding year up to BGN 300,000 (EUR 153,387.56); and new companies in their first year and the next, except companies formed by a transformation | 2026 | ZKPO art. 83(2), https://nra.bg/wps/wcm/connect/nra.bg25863/ed10ff12-b25a-4b07-827c-915979acef42/ZAKON%2BZA%2BKORPORATIVNOTO%2BPODOHODNO%2BOBLAGANE_60.pdf?CACHEID=ROOTWORKSPACE.Z18_PPGAHG8009LJC0QTR5C2HH30I6-ed10ff12-b25a-4b07-827c-915979acef42-nEJyDbV&MOD=AJPERES |
| Monthly advance payments | Net sales in the year before the preceding year above BGN 3,000,000 (EUR 1,533,875.64) | 2026 | ZKPO art. 84, https://nra.bg/wps/wcm/connect/nra.bg25863/ed10ff12-b25a-4b07-827c-915979acef42/ZAKON%2BZA%2BKORPORATIVNOTO%2BPODOHODNO%2BOBLAGANE_60.pdf?CACHEID=ROOTWORKSPACE.Z18_PPGAHG8009LJC0QTR5C2HH30I6-ed10ff12-b25a-4b07-827c-915979acef42-nEJyDbV&MOD=AJPERES |
| Quarterly advance payments | Other mandatory payers: sales above EUR153,387.56 through EUR1,533,875.64 inclusive. Exempt persons may opt for quarterly advances without art.89 interest | 2026 | ZKPO art. 85, https://nra.bg/wps/wcm/connect/nra.bg25863/ed10ff12-b25a-4b07-827c-915979acef42/ZAKON%2BZA%2BKORPORATIVNOTO%2BPODOHODNO%2BOBLAGANE_60.pdf?CACHEID=ROOTWORKSPACE.Z18_PPGAHG8009LJC0QTR5C2HH30I6-ed10ff12-b25a-4b07-827c-915979acef42-nEJyDbV&MOD=AJPERES |
| Expenses tax on representation costs and social costs in kind | 10% | 2026 | ZKPO arts. 204(1)(1), (2), 216(1), https://nra.bg/wps/wcm/connect/nra.bg25863/ed10ff12-b25a-4b07-827c-915979acef42/ZAKON%2BZA%2BKORPORATIVNOTO%2BPODOHODNO%2BOBLAGANE_60.pdf?CACHEID=ROOTWORKSPACE.Z18_PPGAHG8009LJC0QTR5C2HH30I6-ed10ff12-b25a-4b07-827c-915979acef42-nEJyDbV&MOD=AJPERES |
| Expenses tax on assets given for personal use | 3% | 2026 | ZKPO arts. 204(1)(4), 216(2), https://nra.bg/wps/wcm/connect/nra.bg25863/ed10ff12-b25a-4b07-827c-915979acef42/ZAKON%2BZA%2BKORPORATIVNOTO%2BPODOHODNO%2BOBLAGANE_60.pdf?CACHEID=ROOTWORKSPACE.Z18_PPGAHG8009LJC0QTR5C2HH30I6-ed10ff12-b25a-4b07-827c-915979acef42-nEJyDbV&MOD=AJPERES |
| Tonnage tax (shipping, elective) | 10% of the tonnage-based base only after statutory qualification/election; actual eligibility/base is held | 2026 | ZKPO arts. 254, 258, https://nra.bg/wps/wcm/connect/nra.bg25863/ed10ff12-b25a-4b07-827c-915979acef42/ZAKON%2BZA%2BKORPORATIVNOTO%2BPODOHODNO%2BOBLAGANE_60.pdf?CACHEID=ROOTWORKSPACE.Z18_PPGAHG8009LJC0QTR5C2HH30I6-ed10ff12-b25a-4b07-827c-915979acef42-nEJyDbV&MOD=AJPERES |
| Pillar Two minimum tax applies to groups with | Consolidated revenue of at least EUR750,000,000 in two of the four preceding periods, including excluded-entity revenue; adjust non-12-month periods. This is a screening trigger, not complete eligibility: entity exclusions and actual top-up computation are held | 2026 | ZKPO art. 260a(2), https://nra.bg/wps/wcm/connect/nra.bg25863/ed10ff12-b25a-4b07-827c-915979acef42/ZAKON%2BZA%2BKORPORATIVNOTO%2BPODOHODNO%2BOBLAGANE_60.pdf?CACHEID=ROOTWORKSPACE.Z18_PPGAHG8009LJC0QTR5C2HH30I6-ed10ff12-b25a-4b07-827c-915979acef42-nEJyDbV&MOD=AJPERES |

## The method, step by step

**Start from the accounts.** The tax result (данъчен финансов резултат) is the accounting result adjusted by permanent differences, temporary differences and other amounts the ZKPO names (art. 22). A permanent difference changes the result once and never reverses (art. 23). A temporary difference is an item recognised for tax in a different year from the accounts; apply the statutory direction and reversal condition rather than a general timing assumption (art.24). Taxable profit is the positive tax result less tax losses carried forward (art. 19).

**Common add-backs (permanent).** ZKPO art. 26 disallows:
- expenses not connected with the business, and expenses without proper documents;
- fines, confiscations and other sanctions, and late-payment interest on public debts;
- donations beyond art. 31;
- withholding tax the payer bears itself;
- hidden profit distributions (item 11), and bribes.
Shortages/scrap are ordinarily disallowed; art.28 has specific exceptions including force majeure, qualifying normal technological change, statutory/company-standard expiry and limited retail shortages. Actual exceptional allowance/classification needs review, not a blanket write-off deduction.

**Common deductions (permanent).** Dividends from Bulgarian companies and from companies resident in another EU or EEA state are taken out of the result (art. 27(1)(1)). The exclusion does not apply to dividends from the licensed special-investment companies specified in art.27(2)(1), hidden profit distributions, or amounts deductible/reducing the distributing entity's tax result (art.27(2)). Article44 adjusts qualifying financial-instrument gains down and losses up, using the specific §1(21) definition; it does not exempt every security just because a market is mentioned. Actual instrument/market and treaty-exemption eligibility is held below.

**Hidden profit distribution** (§ 1, item 5 of the additional provisions). Amounts not connected with the business or above market levels paid in any form to shareholders, partners or their related parties; and accrued interest meeting at least three of four tests (loan above the payer's equity at the preceding 31 December; repayment of principal or interest not limited by a fixed term; repayment or interest/interest amount depending on profits; principal repayment depending on other creditors or dividends), except loan conditions required by law. Do not reduce this definition to related-party pricing alone. It is not deductible (art. 26(11)), it is not exempt as a dividend at the recipient (art. 27(2)(2)), and a company that does not declare it pays a sanction of 20% of the amount (art. 267). For prices between related parties, see `bg-transfer-pricing`.

**Temporary differences.** Revaluations/impairments are ordinarily not recognized in the booking year. Article35 reverses relevant amounts on derecognition, subject to its inventory and non-deductible-shortage exceptions. Receivables follow art.37's earliest statutory event, including prescribed limitation periods, transfer, specified insolvency/court outcomes, statutory extinguishment, debtor deletion or earlier settlement; actual difficult cases require review. From 2026, revaluations of cash items in another currency at the BNB euro reference rate are recognised as they arise (art. 34(2), as amended by ДВ 30/2026). Unused leave reverses to the extent actually paid; related compulsory contributions reverse when those contributions are paid, with capitalization/no-profit-reduction exceptions (art.41). Article42 concerns unpaid income of resident individuals, with exceptions including basic salary, mandatory additional remuneration/compensation and sole-trader income; do not add back every unpaid wage. Actual exceptional timing outcomes are held.

**Depreciation.** Accounting depreciation is always added back and tax depreciation deducted instead (art. 54). Every company keeps a tax depreciation plan listing each asset (art. 52). Annual tax depreciation = depreciable value x annual rate x months in use / 12, starting from the month the asset is put into use or the next month (art. 58). The company picks its rate once a year, up to the applicable maximum (art.55(2)); total depreciation cannot exceed depreciable value (art.53(3)). Goodwill from a business combination is not depreciable for tax (art. 49).

**Losses.** Elect loss carry-forward in the first subsequent year with a positive tax result before losses; after election carry it forward consecutively over the next five years, using losses in order of origin (arts.70–72). Being within five years alone does not prove availability. There is no carry-back and no cap other than the positive result for the year (art. 71(1)). Foreign-source loss restrictions have exceptions: art.73(3) covers a closing EU/EEA PE, and art.74(3) disapplies its credit-method ring-fence for EU/EEA sources. Do not apply a blanket foreign-loss ring-fence. Actual foreign allocation/closure outcomes are held (arts.73–74).

**Interest: two rules, one result.**
1. **Thin capitalisation** (art. 43). Applies only if average debt (1 January and 31 December) is more than three times average equity (art. 43(6)). Disallowed interest = relevant interest costs - interest income - 75% x accounting result before all interest, with no negative disallowance; omit the pre-interest result if negative (art.43(1),(5)). The art.43(4) bank/finance-lease exclusion has related-party/guarantee/security/direction exceptions; joint borrower/related-party collateral can require proportional exclusion rather than including all interest. Penalty interest, amounts already disallowed elsewhere and capitalized borrowing costs also have specific treatment. Actual mixed-collateral calculations are held. Disallowed interest is recognised in later years within the same formula (art. 43(2)).
2. **Interest limitation** (art. 43a, the ATAD rule). Exceeding borrowing costs = relevant borrowing costs less recognized taxable interest/equivalent income under art.43a(2)–(4), not merely the net interest caption in the accounts. Where they exceed EUR 3,000,000, the excess over 30% of tax EBITDA is disallowed (art. 43a(1), (7)). Tax EBITDA = tax result before losses and before arts. 43 and 43a, plus tax depreciation, less interest income, plus borrowing costs (art. 43a(3)). Omit negative tax EBITDA from the disallowance/reversal formulas (art.43a(6)). Disallowed costs carry forward under the future-capacity formula without a stated year limit (art.43a(5)); interaction with art.43 carry-forwards prevents double relief.
Where both rules bite, the larger disallowance applies (art. 43a(9)). Banks are outside both rules (arts. 43(7), 43a(10)).

**CFC.** CFC ownership, low-tax, substance and profit-inclusion outcomes under arts.47в–47г require separate review in `bg-cross-border`. This Guide supplies no usable CFC inclusion calculation.

**Expenses tax** (pointer). Representation costs, social benefits in kind and assets given to staff for personal use are deductible in full (art. 206(1)) but bear a separate final expenses tax of 10% or 3% (art. 216), declared in the annual return and paid by 30 June (art. 217). Voluntary-insurance exemption: up to BGN60 (EUR30.68) per employee/month, subject to the month-end enforceable-public-debt condition (art.208). Electronic food vouchers: up to BGN200 (EUR102.26) per employee/month, with the remuneration-maintenance, public-debt and authorized-operator conditions in art.209a(1). These must be qualifying social benefits in kind; actual benefit classification/private-use election or allocation is held.

**Alternative taxes** (pointer). The specified gambling activities, budget-enterprise income and qualified shipping have distinct regimes. The budget-enterprise income rate is generally3%, but municipalities have2% (art.250); shipping is10% of the statutory tonnage base, not ordinary accounting profit. Do not use these rates to decide eligibility or assume every gambling activity is outside CIT. Actual special-regime returns/bases are held.

**Pillar Two** (pointer). Groups at or above EUR 750,000,000 of consolidated revenue in two of the four preceding years fall under ZKPO Part Five "a" (arts. 260a onwards): the income inclusion rule, the undertaxed profits rule and the Bulgarian domestic top-up tax. Excluded entities and non-standard period adjustments matter; the15% minimum is not a replacement general CIT rate. Actual IIR/UTPR/domestic-top-up eligibility and calculation are non-usable here and require separate review.

## Deadlines and filing

| Obligation | When | Source |
|---|---|---|
| Declare the 2026 advance payments (forecast profit) | 1 March to 15 April 2026 | ZKPO art. 87a(1)  [official text](https://nra.bg/wps/wcm/connect/nra.bg25863/ed10ff12-b25a-4b07-827c-915979acef42/ZAKON%2BZA%2BKORPORATIVNOTO%2BPODOHODNO%2BOBLAGANE_60.pdf?CACHEID=ROOTWORKSPACE.Z18_PPGAHG8009LJC0QTR5C2HH30I6-ed10ff12-b25a-4b07-827c-915979acef42-nEJyDbV&MOD=AJPERES) |
| Monthly advances, January to March | By 15 April 2026 | ZKPO art. 90(1)(1)  [official text](https://nra.bg/wps/wcm/connect/nra.bg25863/ed10ff12-b25a-4b07-827c-915979acef42/ZAKON%2BZA%2BKORPORATIVNOTO%2BPODOHODNO%2BOBLAGANE_60.pdf?CACHEID=ROOTWORKSPACE.Z18_PPGAHG8009LJC0QTR5C2HH30I6-ed10ff12-b25a-4b07-827c-915979acef42-nEJyDbV&MOD=AJPERES) |
| Monthly advances, April to November | By the 15th of each month | ZKPO art. 90(1)(2)  [official text](https://nra.bg/wps/wcm/connect/nra.bg25863/ed10ff12-b25a-4b07-827c-915979acef42/ZAKON%2BZA%2BKORPORATIVNOTO%2BPODOHODNO%2BOBLAGANE_60.pdf?CACHEID=ROOTWORKSPACE.Z18_PPGAHG8009LJC0QTR5C2HH30I6-ed10ff12-b25a-4b07-827c-915979acef42-nEJyDbV&MOD=AJPERES) |
| Monthly advance for December | By 1 December 2026 | ZKPO art. 90(1)(3)  [official text](https://nra.bg/wps/wcm/connect/nra.bg25863/ed10ff12-b25a-4b07-827c-915979acef42/ZAKON%2BZA%2BKORPORATIVNOTO%2BPODOHODNO%2BOBLAGANE_60.pdf?CACHEID=ROOTWORKSPACE.Z18_PPGAHG8009LJC0QTR5C2HH30I6-ed10ff12-b25a-4b07-827c-915979acef42-nEJyDbV&MOD=AJPERES) |
| Quarterly advances, Q1 and Q2 | By 15 April and 15 July 2026 | ZKPO art. 90(2)  [official text](https://nra.bg/wps/wcm/connect/nra.bg25863/ed10ff12-b25a-4b07-827c-915979acef42/ZAKON%2BZA%2BKORPORATIVNOTO%2BPODOHODNO%2BOBLAGANE_60.pdf?CACHEID=ROOTWORKSPACE.Z18_PPGAHG8009LJC0QTR5C2HH30I6-ed10ff12-b25a-4b07-827c-915979acef42-nEJyDbV&MOD=AJPERES) |
| Quarterly advance, Q3 | By 1 December 2026; no Q4 advance | ZKPO art. 90(2)  [official text](https://nra.bg/wps/wcm/connect/nra.bg25863/ed10ff12-b25a-4b07-827c-915979acef42/ZAKON%2BZA%2BKORPORATIVNOTO%2BPODOHODNO%2BOBLAGANE_60.pdf?CACHEID=ROOTWORKSPACE.Z18_PPGAHG8009LJC0QTR5C2HH30I6-ed10ff12-b25a-4b07-827c-915979acef42-nEJyDbV&MOD=AJPERES) |
| Change the advances up or down | Statutory15 November2026; because Sunday, **16 November2026** under DOPK art.22(7) | ZKPO art. 88(1)  [official text](https://nra.bg/wps/wcm/connect/nra.bg25863/ed10ff12-b25a-4b07-827c-915979acef42/ZAKON%2BZA%2BKORPORATIVNOTO%2BPODOHODNO%2BOBLAGANE_60.pdf?CACHEID=ROOTWORKSPACE.Z18_PPGAHG8009LJC0QTR5C2HH30I6-ed10ff12-b25a-4b07-827c-915979acef42-nEJyDbV&MOD=AJPERES) |
| Annual return for 2026, with the annual activity report | 1 March to 30 June 2027, to the NRA directorate where the company is registered | ZKPO art. 92(1) to (3)  [official text](https://nra.bg/wps/wcm/connect/nra.bg25863/ed10ff12-b25a-4b07-827c-915979acef42/ZAKON%2BZA%2BKORPORATIVNOTO%2BPODOHODNO%2BOBLAGANE_60.pdf?CACHEID=ROOTWORKSPACE.Z18_PPGAHG8009LJC0QTR5C2HH30I6-ed10ff12-b25a-4b07-827c-915979acef42-nEJyDbV&MOD=AJPERES) |
| Payment of 2026 corporate tax, less advances paid | By 30 June 2027 | ZKPO art. 93(1)  [official text](https://nra.bg/wps/wcm/connect/nra.bg25863/ed10ff12-b25a-4b07-827c-915979acef42/ZAKON%2BZA%2BKORPORATIVNOTO%2BPODOHODNO%2BOBLAGANE_60.pdf?CACHEID=ROOTWORKSPACE.Z18_PPGAHG8009LJC0QTR5C2HH30I6-ed10ff12-b25a-4b07-827c-915979acef42-nEJyDbV&MOD=AJPERES) |
| Payment of the 2026 expenses tax | By 30 June 2027 | ZKPO art. 217(2)  [official text](https://nra.bg/wps/wcm/connect/nra.bg25863/ed10ff12-b25a-4b07-827c-915979acef42/ZAKON%2BZA%2BKORPORATIVNOTO%2BPODOHODNO%2BOBLAGANE_60.pdf?CACHEID=ROOTWORKSPACE.Z18_PPGAHG8009LJC0QTR5C2HH30I6-ed10ff12-b25a-4b07-827c-915979acef42-nEJyDbV&MOD=AJPERES) |

The original monthly/quarterly formula material in arts.86–87 did not extract from either the official PDF text or the PDF-named DOCX mirror. **Actual forecast-to-installment computation is non-usable here: Check this point with one of our partner accountants.** The original case below retains its arithmetic and stated determined/paid advances as conditional inputs; it does not authorize an advance declaration from an unreadable equation. A company with no activity under the Accountancy Act ordinarily files neither return nor activity report, but files a return if corporate/expenses tax is due or it wishes to declare other form-provided circumstances (art.92(4)). Foreign-tax evidence accompanies the return except treaty-exemption-with-progression cases (art.92(6)). File through the NRA e-services route with the required electronic signature; actual2026 return form/box mapping for filing in2027 is a future-form hold, not an invented form number.

Statutory dates above roll to the next working day when they fall on a non-working day (DOPK art.22(7)); for2026 this also affects the August and November monthly15th dates. Keep the statutory15November cutoff distinct from its16November2026 working-day application. [DOPK art.22](https://www.minfin.bg/upload/4418/%09%09%09DANYCNOOSIGURITELEN_PROCESUALEN_KODEKS.pdf%09%09%09).

## Penalties and interest

| Failure | Penalty | Source |
|---|---|---|
| Return not filed, filed late, or data understating the tax | BGN 500 to 3,000 (EUR 255.65 to 1,533.88); repeat BGN 1,000 to 6,000 (EUR 511.29 to 3,067.75) | ZKPO art. 261  [official text](https://nra.bg/wps/wcm/connect/nra.bg25863/ed10ff12-b25a-4b07-827c-915979acef42/ZAKON%2BZA%2BKORPORATIVNOTO%2BPODOHODNO%2BOBLAGANE_60.pdf?CACHEID=ROOTWORKSPACE.Z18_PPGAHG8009LJC0QTR5C2HH30I6-ed10ff12-b25a-4b07-827c-915979acef42-nEJyDbV&MOD=AJPERES) |
| Annex to the annual return missing or wrong | BGN 100 to 1,000 (EUR 51.13 to 511.29); repeat BGN 200 to 2,000 (EUR 102.26 to 1,022.58) | ZKPO art. 262  [official text](https://nra.bg/wps/wcm/connect/nra.bg25863/ed10ff12-b25a-4b07-827c-915979acef42/ZAKON%2BZA%2BKORPORATIVNOTO%2BPODOHODNO%2BOBLAGANE_60.pdf?CACHEID=ROOTWORKSPACE.Z18_PPGAHG8009LJC0QTR5C2HH30I6-ed10ff12-b25a-4b07-827c-915979acef42-nEJyDbV&MOD=AJPERES) |
| Transaction booked against the accounting policy, distorting the result | BGN 100 to 1,000 (EUR 51.13 to 511.29) per breach; repeat BGN 200 to 2,000 (EUR 102.26 to 1,022.58) | ZKPO art. 263  [official text](https://nra.bg/wps/wcm/connect/nra.bg25863/ed10ff12-b25a-4b07-827c-915979acef42/ZAKON%2BZA%2BKORPORATIVNOTO%2BPODOHODNO%2BOBLAGANE_60.pdf?CACHEID=ROOTWORKSPACE.Z18_PPGAHG8009LJC0QTR5C2HH30I6-ed10ff12-b25a-4b07-827c-915979acef42-nEJyDbV&MOD=AJPERES) |
| The company's representative who allowed a breach of arts. 261 to 263 | BGN 200 to 1,000 (EUR 102.26 to 511.29); repeat BGN 400 to 2,000 (EUR 204.52 to 1,022.58) | ZKPO art. 264  [official text](https://nra.bg/wps/wcm/connect/nra.bg25863/ed10ff12-b25a-4b07-827c-915979acef42/ZAKON%2BZA%2BKORPORATIVNOTO%2BPODOHODNO%2BOBLAGANE_60.pdf?CACHEID=ROOTWORKSPACE.Z18_PPGAHG8009LJC0QTR5C2HH30I6-ed10ff12-b25a-4b07-827c-915979acef42-nEJyDbV&MOD=AJPERES) |
| Hidden profit distribution not declared in the return | 20% of the hidden distribution | ZKPO art. 267  [official text](https://nra.bg/wps/wcm/connect/nra.bg25863/ed10ff12-b25a-4b07-827c-915979acef42/ZAKON%2BZA%2BKORPORATIVNOTO%2BPODOHODNO%2BOBLAGANE_60.pdf?CACHEID=ROOTWORKSPACE.Z18_PPGAHG8009LJC0QTR5C2HH30I6-ed10ff12-b25a-4b07-827c-915979acef42-nEJyDbV&MOD=AJPERES) |
| Advances too low: the annual tax exceeds the monthly advances by more than 25%, or 75% of the annual tax exceeds the quarterly advances (Q1 to Q3) by more than 25% | Interest on the excess over125% of **determined**, not merely paid, advances; ordinarily16April–31December. Transformations have a separate starting date (art.89(5)) | ZKPO art. 89  [official text](https://nra.bg/wps/wcm/connect/nra.bg25863/ed10ff12-b25a-4b07-827c-915979acef42/ZAKON%2BZA%2BKORPORATIVNOTO%2BPODOHODNO%2BOBLAGANE_60.pdf?CACHEID=ROOTWORKSPACE.Z18_PPGAHG8009LJC0QTR5C2HH30I6-ed10ff12-b25a-4b07-827c-915979acef42-nEJyDbV&MOD=AJPERES) |
| Late payment of the tax | Statutory interest (законна лихва); actual current rate/payoff held | [DOPK art.175](https://www.minfin.bg/upload/4418/%09%09%09DANYCNOOSIGURITELEN_PROCESUALEN_KODEKS.pdf%09%09%09) |

The euro figures above are the lev amounts still written in the ZKPO, converted at BGN 1.95583 and rounded to the cent as Euro Introduction Act arts. 12 and 13 require.

## Cross-border points

- **Dividends paid out.** Domestic dividends to foreign legal entities are generally subject to5% withholding, excluding amounts realized through a Bulgarian PE and subject to the statutory/treaty exemptions. Dividends to a company resident in another EU or EEA state are exempt, **except hidden profit distributions** (ZKPO art. 194(3)(3)). Withholding detail, treaty relief and the DOPK procedure are in `bg-cross-border`.
- **Dividends received.** Apply the art.27 exceptions above, not a universal EU/EEA exemption. Other foreign-dividend tax and credit/treaty outcomes require separate work; credits are country/income-specific and capped by Bulgarian tax, not automatic full recovery (arts.13–14).
- **Interest to related non-residents.** Interest/royalty withholding has a statutory10% baseline where art.195 applies, but exemptions/treaties and PE/source/beneficial-owner conditions matter. The historical EU-associated-company25%/two-year test is not sufficient on its own; art.195(7)–(12) includes further conditions and exceptions. Actual withholding/exemption outputs are held and routed to `bg-cross-border`; apply the proved interest-deduction and arm's-length rules separately.
- **Foreign permanent establishment of a Bulgarian company.** Its profit is included subject to the applicable treaty/credit treatment. Apply the foreign-loss exceptions above; actual foreign-PE outcomes are held.
- **Moving assets or residence out of Bulgaria.** Exit taxation and any EU/EEA installment/deferral conditions require separate review under arts.155–155г in `bg-cross-border`; no usable exit-tax amount or automatic deferral is supplied here.

## Worked cases

### Example 1: trading company, ordinary year with a loss brought forward

Struma Trade OOD has an accounting profit for 2026 of EUR 200,000. Its accounts include EUR 30,000 of accounting depreciation and a EUR 2,000 traffic fine. Its tax depreciation plan gives EUR 45,000 for 2026. It has the original stated EUR50,000 remaining2023 loss, still within five years: this is the2026 euro carrying amount supplied in the case, not an invented original2023 euro ledger. Assume the loss election was properly exercised and the amount remains available; the original2023 BGN record was not supplied. The EUR10,000 representation expense is assumed already included in accounting profit, business-related and properly documented.

The fine is added back (art. 26(6)); accounting depreciation is replaced by tax depreciation (art. 54). The tax result is EUR 187,000. After the 2023 loss, taxable profit is EUR 137,000 and corporate tax is EUR 13,700. Representation costs stay deductible but bear 10% expenses tax, EUR 1,000.

Its 2024 net sales were BGN 1,800,000, which is EUR 920,325.39: above EUR 153,387.56 and below EUR 1,533,875.64, so it pays quarterly advances. It declared a forecast profit of EUR 120,000 by 15 April 2026, and the original fixture uses three determined and paid quarterly advances of EUR3,000 (EUR9,000 in all). Its forecast/4 arithmetic is retained below for historical reproducibility; actual installment determination is the explicit source-equation hold above. The balance of EUR 4,700 is due by 30 June 2027 with the expenses tax. No interest under art. 89: 75% of the annual tax is EUR 10,275, below 125% of the advances (EUR 11,250).

```oa-check
name: Bulgarian OOD, 2026 CIT with loss, quarterly advances, expenses tax
inputs:
  accounting_profit: 200000
  accounting_depreciation: 30000
  fine: 2000
  tax_depreciation: 45000
  loss_2023: 50000
  representation: 10000
  net_sales_2024_bgn: 1800000
  forecast_profit: 120000
steps:
  - tax_result: accounting_profit + accounting_depreciation + fine - tax_depreciation
  - loss_used: min(loss_2023, tax_result)
  - taxable_profit: tax_result - loss_used
  - cit: taxable_profit * 0.10
  - expenses_tax: representation * 0.10
  - net_sales_2024_eur: round(net_sales_2024_bgn / 1.95583, 2)
  - quarterly_advance: forecast_profit / 4 * 0.10
  - advances_paid: quarterly_advance * 3
  - balance_due: cit - advances_paid
  - interest_base: max(0, 0.75 * cit - advances_paid * 1.25)
expected:
  tax_result: 187000
  loss_used: 50000
  taxable_profit: 137000
  cit: 13700
  expenses_tax: 1000
  net_sales_2024_eur: 920325.39
  quarterly_advance: 3000
  advances_paid: 9000
  balance_due: 4700
  interest_base: 0
```

### Example 2: holding company with a large shareholder loan, both interest rules tested

Balkan Holding EAD is financed by a EUR 60,000,000 loan from its foreign parent; its equity averages EUR 10,000,000. In 2026 it books EUR 6,000,000 of interest to the parent and EUR 200,000 of interest income. Its accounting profit is EUR 3,500,000. Its tax result under the general rules, before losses and before arts. 43 and 43a, is EUR 4,000,000, and its tax depreciation is EUR 1,000,000.

For this original arithmetic case assume ordinary arm's-length borrowing, no hidden distribution/hybrid adjustment, no excluded or capitalized costs, and no prior interest carry-forwards; these assumptions do not establish real-client eligibility. Debt is six times equity, so thin capitalisation is tested. The accounting result before interest is EUR 9,300,000; 75% of that is EUR 6,975,000, which exceeds net interest of EUR 5,800,000, so art. 43 disallows nothing. Exceeding borrowing costs of EUR 5,800,000 are above EUR 3,000,000, so art. 43a applies. Tax EBITDA is EUR 10,800,000; 30% is EUR 3,240,000. EUR 2,560,000 is disallowed this year and carried forward. Because the art. 43a amount is the larger, only it applies (art. 43a(9)(1)). Taxable profit is EUR 6,560,000 and corporate tax EUR 656,000.

```oa-check
name: Bulgarian holding, thin cap and 30% EBITDA interest limitation, 2026
inputs:
  debt_avg: 60000000
  equity_avg: 10000000
  interest_cost: 6000000
  interest_income: 200000
  accounting_profit: 3500000
  tax_result_before_rules: 4000000
  tax_depreciation: 1000000
  threshold: 3000000
steps:
  - debt_equity_ratio: debt_avg / equity_avg
  - result_before_interest: accounting_profit + interest_cost - interest_income
  - thin_cap_disallowed: max(0, interest_cost - interest_income - 0.75 * result_before_interest)
  - exceeding_costs: interest_cost - interest_income
  - tax_ebitda: tax_result_before_rules + tax_depreciation - interest_income + interest_cost
  - atad_disallowed: max(0, exceeding_costs - 0.30 * tax_ebitda)
  - disallowed: max(thin_cap_disallowed, atad_disallowed)
  - taxable_profit: tax_result_before_rules + disallowed
  - cit: taxable_profit * 0.10
expected:
  debt_equity_ratio: 6
  result_before_interest: 9300000
  thin_cap_disallowed: 0
  exceeding_costs: 5800000
  tax_ebitda: 10800000
  atad_disallowed: 2560000
  disallowed: 2560000
  taxable_profit: 6560000
  cit: 656000
```

## Ask the client first

1. **Net sales for 2024 (and 2025 for next year), and the year the company was formed.** They decide no advances, quarterly or monthly (arts. 83, 84).
2. **Tax losses by year since 2021.** Confirm first eligible profitable year/election, use and expiry, not just the year label; ordinary2026 loss-year range begins2021 (arts.70–72).
3. **The fixed asset register and the tax depreciation plan.** Category and rate chosen for each asset, and any electric cars bought from 2026 (art. 55).
4. **Loans: lender, relation to the company, guarantees, interest, and opening and closing debt and equity.** They decide whether thin capitalisation or the EUR 3,000,000 interest limitation bites (arts. 43, 43a).
5. **Payments to shareholders or their related parties beyond salary and declared dividends.** Possible hidden profit distribution (§ 1, item 5; arts. 26(11), 267).
6. **Representation costs, staff benefits in kind and assets used privately.** Expenses tax base (art. 204).

## When to refuse or refer

These outcomes are **not usable from this Guide**. Keep the original facts, amounts, currencies and years. **Check this point with one of our partner accountants.**

- Actual forecast-to-installment equation/output; actual2026 annual-form/box/software mapping for filing in2027, special short-period/cessation/transformation filings, unusual deadline relief, interest-rate/payoff calculations and contested sanctions. Ordinary computation/deadlines remain available above.
- Actual CFC, Pillar Two, gambling/budget/shipping eligibility and return calculations; transfer-pricing, hybrid, financial-instrument/market, foreign PE/loss and exit-tax/deferral outcomes.
- Actual complex donation recipients, R&D classification/funding/capitalization, special energy-efficiency depreciation, mixed-collateral loans, prior interest carry-forward interaction and exceptional unpaid-personnel timing cases.
- Actual withholding/treaty/beneficial-owner exemptions, including historical2025 dividend, interest/royalty and EU-associated-company outcomes. The25%/two-year shorthand alone is not a usable exemption test.
- Actual social-benefit classification/exemptions/private-use elections or allocations and disputed historical BGN-to-euro opening balances. In Example1 the given2023 loss balance is assumed already correctly carried into2026 euros; no missing BGN input is invented.

## Sources

| Official source | Operative material actually read | Read on |
| --- | --- | --- |
| [NRA ZKPO consolidated text](https://nra.bg/wps/wcm/connect/nra.bg25863/ed10ff12-b25a-4b07-827c-915979acef42/ZAKON%2BZA%2BKORPORATIVNOTO%2BPODOHODNO%2BOBLAGANE_60.pdf?CACHEID=ROOTWORKSPACE.Z18_PPGAHG8009LJC0QTR5C2HH30I6-ed10ff12-b25a-4b07-827c-915979acef42-nEJyDbV&MOD=AJPERES) | Arts.1–4,13–14,18–28,31,34–37,41–44,49–58,69–74,83–93,194–195,200,204–209a,216–218,242,250,254/258,260a–260в,261–264,267 and §1(5), relevant provisions quoted privately. Published version includes ДВ30/2026; this is not a claim that an unavailable later consolidation was read. | 2026-11-28 |
| [Official NRA document mirror](https://nra.web.egov.bg/upload/364/8105a0ea28ca676d06795be14d6f442626108465/%D0%97%D0%9A%D0%9F%D0%9E.pdf) | Arts.86–87 surrounding text only; equation content did not extract. This PDF-named resource supplies DOCX bytes. Actual installment calculation remains held; no source files saved. | 2026-11-28 |
| [2026 amending Act, ДВ30/2026](https://dv.parliament.bg/DVWeb/showMaterialDV.jsp?idMat=242046) | Official indexed applicability sentence limiting electric-car50% treatment to acquisitions on/after1January2026; full page returned503. Remaining operative amendments read in NRA text. | 2026-11-28 bounded excerpt |
| [Euro Introduction Act, official government publication](https://www.evroto.bg/upload/1068/ZVERB.pdf) | Arts.11–13 conversion/rounding and §36 ZKPO euro amendment. | 2026-11-28 |
| [Council Regulation2025/1409](https://eur-lex.europa.eu/eli/reg/2025/1409/oj/eng/pdf) | Recitals3–4 and arts.1–2: adoption/date and full conversion rate. Authentic English text; Bulgarian legislative quotes are retained for domestic law. | 2026-11-28 |
| [DOPK official text](https://www.minfin.bg/upload/4418/%09%09%09DANYCNOOSIGURITELEN_PROCESUALEN_KODEKS.pdf%09%09%09) | Art.22(7) non-working-day rule; art.175 unpaid-public-debt interest. No numerical current payoff rate established. | 2026-11-28 |
| [NRA advance-payment guidance](https://nra.bg/wps/portal/nra/taxes/korporativen-danak/avansovi-vnoski/avansovi-vnoski) | Accessible indexed expanded NRA page: exact2026 euro thresholds/inclusive boundaries, voluntary/transformation conditions, declaration/payment schedule and e-signature route. Short page route itself was inaccessible. | 2026-11-28 |

Historical2025 scope: the former Guide's BGN300,000/3,000,000 advance thresholds used the **year before the preceding year**, hence2023 sales for2025, not an unqualified prior-year test. Its ordinary annual2025 filing/payment dates are1March–30June2026/payment30June2026; do not relabel those as2026 income. Historical withholding topics remain routed/held above, with their original conditions retained in the private topic map.

Not yet confirmed: outcomes explicitly listed under **When to refuse or refer**, including future annual-form mapping, current interest/payoff, complex special regimes and actual cross-border/benefit outcomes. These are non-usable holds. Check this point with one of our partner accountants.

> Contributed by Michael Cutajar.
