---
name: za-income-tax
description: Use this skill whenever asked about South African income tax for self-employed individuals. Trigger on phrases like "how much tax do I pay", "ITR12", "income tax return", "SARS", "tax brackets", "provisional tax", "IRP6", "rebates", "medical credits", "retirement deduction", "turnover tax", "eFiling", or any question about filing or computing income tax for a self-employed or sole proprietor client in South Africa. ALWAYS read this skill before touching any South African income tax work.
version: 2.1
jurisdiction: ZA
tax_year: 2025
last_updated: 2026-11-27
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
reviewed_by: "Werner Britz"
reviewed_on: 2026-11-03
tier: 1
domain: income-tax
type: computation
tax_year_notes: "Preserves YoA 2025 (2024/25), original 2025/26 tests (YoA 2026), and separately labelled 2026/27 cases (YoA 2027)."
---

# ZA Income Tax

## Scope

South African individual income-tax working papers for self-employed individuals and sole proprietors. Confirm the assessment period before using a figure. This Guide preserves its original 2025 scope and the later examples; it does not turn a 2025 return into a 2027 return. Companies, close corporations, partnerships and trusts require separate work. Foreign income and capital-asset disposals must be identified before completing the individual computation; the specialist outcomes below are expressly held.

An ordinary individual's year runs from 1 March to the last day of the following February: **YoA 2025 = 1 March 2024–28 February 2025; YoA 2026 = 1 March 2025–28 February 2026 (2025/26); YoA 2027 = 1 March 2026–28 February 2027 (2026/27)**. Short years, death and residence changes need separate treatment. [SARS individual guide](https://www.sars.gov.za/wp-content/uploads/Ops/Guides/Legal-Pub-Guide-IT01-Guide-on-Income-Tax-and-the-Individual.pdf), year-of-assessment section.

The computation below is for ordinary income, not retirement lump sums, withdrawal benefits or severance benefits. For YoA 2027 the announced ordinary brackets, rebates and medical-fee credits operate under the temporary announcement provisions in ITA ss 5(2), 6(6) and 6A(5), conditional on implementing legislation within twelve months. This is not a statement that the 2026 Bill has been enacted. [Act 23/2018, ss 3–5](https://www.sars.gov.za/wp-content/uploads/Legal/AmendActs/LAPD-LPrim-AA-2018-03-Taxation-Laws-Amend-Act-23-of-2018-GG-42172.pdf). Future use outside that period: Check this point with one of our partner accountants.

## Ask the client first

Read the existing records before asking for missing information. Obtain the actual assessment year; age at its last day (28 February 2026 for the original 2025/26 tests, 28 February 2027 for the later cases); residence history; trade and entity type; other income; tax-registration/election records; annual accounts; invoices and statements; asset register and first-use dates; supported business/private allocation and vehicle logbook; actual retirement contributions and unused-contribution history; medical-scheme certificate, covered persons and eligible months, payer, disability and unreimbursed medical receipts; donations receipts; PAYE certificates and actual IRP6 payments; prior return and assessment/basic amount.

Ask about rental income, royalties, annuities, dividends, foreign receipts, asset/business sales, spouse/dependants, related-party loans, trust distributions and employees. A South African account or a recurring debit proves neither residence nor entitlement. Unknown age stops the tax calculation; an unknown expense purpose or allocation stays unresolved and excluded from a **provisional** deductible subtotal, rather than being declared legally non-deductible or assigned an invented 0% fact.

## The method, step by step

### Ordinary rates and reliefs

Use the column matching the **year of assessment**. Apply each marginal rate only to the excess stated. Values are ZAR. [SARS ordinary-income tables](https://www.sars.gov.za/tax-rates/income-tax/rates-of-tax-for-individuals/); ITA s 5 and annual rates legislation.

| Band | YoA 2025 and 2026 | YoA 2027 | Official source |
|---|---|---|---|
| First | Up to R237,100: 18% | Up to R245,100: 18% | https://www.sars.gov.za/tax-rates/income-tax/rates-of-tax-for-individuals/ |
| Second | R237,101–R370,500: R42,678 + 26% above R237,100 | R245,101–R383,100: R44,118 + 26% above R245,100 | https://www.sars.gov.za/tax-rates/income-tax/rates-of-tax-for-individuals/ |
| Third | R370,501–R512,800: R77,362 + 31% above R370,500 | R383,101–R530,200: R79,998 + 31% above R383,100 | https://www.sars.gov.za/tax-rates/income-tax/rates-of-tax-for-individuals/ |
| Fourth | R512,801–R673,000: R121,475 + 36% above R512,800 | R530,201–R695,800: R125,599 + 36% above R530,200 | https://www.sars.gov.za/tax-rates/income-tax/rates-of-tax-for-individuals/ |
| Fifth | R673,001–R857,900: R179,147 + 39% above R673,000 | R695,801–R887,000: R185,215 + 39% above R695,800 | https://www.sars.gov.za/tax-rates/income-tax/rates-of-tax-for-individuals/ |
| Sixth | R857,901–R1,817,000: R251,258 + 41% above R857,900 | R887,001–R1,878,600: R259,783 + 41% above R887,000 | https://www.sars.gov.za/tax-rates/income-tax/rates-of-tax-for-individuals/ |
| Seventh | Above R1,817,000: R644,489 + 45% above R1,817,000 | Above R1,878,600: R666,339 + 45% above R1,878,600 | https://www.sars.gov.za/tax-rates/income-tax/rates-of-tax-for-individuals/ |

Rebates reduce tax, not taxable income. Add the secondary to the primary at age 65 and the tertiary to both at age 75, using age on the last day of the assessment year. Published tax thresholds concern normal tax, not permission to omit a return. [ITA s 6; Act 19/2023 s 3](https://www.sars.gov.za/wp-content/uploads/Legal/AmendActs/Legal-LPrim-AA-2023-01-Rates-and-Monetary-Amounts-and-Amendment-of-Revenue-Laws-Act-19-of-2023-GG-49948-Notice-4228-22-December-2023.pdf).

| Relief, ordinary full year | YoA 2025 and 2026 | YoA 2027 | Official source |
|---|---|---|---|
| Primary rebate | R17,235 | R17,820 | https://www.sars.gov.za/tax-rates/income-tax/rates-of-tax-for-individuals/ |
| Additional secondary, 65+ | R9,444 | R9,765 | https://www.sars.gov.za/tax-rates/income-tax/rates-of-tax-for-individuals/ |
| Additional tertiary, 75+ | R3,145 | R3,249 | https://www.sars.gov.za/tax-rates/income-tax/rates-of-tax-for-individuals/ |
| Published threshold, under 65 | R95,750 | R99,000 | https://www.sars.gov.za/tax-rates/income-tax/rates-of-tax-for-individuals/ |
| Published threshold, 65–74 | R148,217 | R153,250 | https://www.sars.gov.za/tax-rates/income-tax/rates-of-tax-for-individuals/ |
| Published threshold, 75+ | R165,689 | R171,300 | https://www.sars.gov.za/tax-rates/income-tax/rates-of-tax-for-individuals/ |
| SA-source interest exemption, under 65 | R23,800 annually | R23,800 annually | https://www.sars.gov.za/tax-rates/income-tax/interest-and-dividends/ |
| SA-source interest exemption, 65+ | R34,500 annually | R34,500 annually | https://www.sars.gov.za/tax-rates/income-tax/interest-and-dividends/ |
| Medical-fee credit, first qualifying person/month | R364 | R376 | https://www.sars.gov.za/tax-rates/medical-tax-credit-rates/ |
| Medical-fee credit, first two combined/month | R728 | R752 | https://www.sars.gov.za/tax-rates/medical-tax-credit-rates/ |
| Medical-fee credit, each further dependant/month | R246 | R254 | https://www.sars.gov.za/tax-rates/medical-tax-credit-rates/ |

Interest above the applicable personal exemption is taxable; do not describe the exempt part as taxable or apply this SA-source exemption to foreign interest. Tax-free investment income needs its separate regime.

### Trade profit and transaction classification

Reconcile receipts/accruals to accounts and source documents. For ordinary expenditure, ITA s 11(a) requires actual incurrence in producing income and excludes capital expenditure; s 23(g) limits it to trade purpose, and s 23(b) excludes private/domestic costs. These are the tests for bona fide business meals as well as other trade costs. A merchant name never establishes a deduction. [Statutory text, IN 45 Issue 5, Annexure](https://www.sars.gov.za/wp-content/uploads/Legal/Notes/Legal-IntR-IN-45-Deduction-of-security-expenditure.pdf).

| Original transaction family | Working-paper action |
|---|---|
| FNB/FIRST NATIONAL BANK, STANDARD BANK/SBSA, NEDBANK, ABSA, CAPITEC, INVESTEC, DISCOVERY BANK, TYMEBANK, REVOLUT, WISE | Separate charges, credit interest, debit interest and principal. Apply the trade test to actual business fees; establish borrowed-fund use and timing before deducting interest. Principal is not an ordinary trading expense. |
| SARS; OWN TRANSFER/INTERNAL; DRAWINGS/OWNER; DEPOSIT/OWN DEPOSIT | Reconcile income/provisional-tax payments against the tax account, outside trade expenses. Trace own transfers/capital/drawings so neither income nor expense is duplicated. Other SARS tax types/refunds require their underlying classification. |
| ESKOM, CITY POWER, CITY OF JHB/CPT/DBN, RAND WATER, MUNICIPALITY; VODACOM, MTN, CELL C, TELKOM, RAIN | Separate rates, power, water, refuse and telecoms. Document actual trade use and allocation; do not deduct the whole mixed bill. |
| HOLLARD, SANTAM, OLD MUTUAL, MOMENTUM, OUTSURANCE | Ordinary revenue cover of trade assets/liabilities: apply the general trade test. Policy elections, life/income protection and proceeds are held below. |
| GOOGLE, MICROSOFT, ADOBE, META, GITHUB, OPENAI, ANTHROPIC, SLACK, ZOOM, ATLASSIAN | Check invoice, service period, trade nexus and revenue/capital character. Supplier location alone creates no deduction. Prepayments are held below. |
| ACCOUNTANT/AUDIT/CA(SA), TAX PRACTITIONER, ATTORNEY/ADVOCATE/LAW FIRM | Review purpose and invoice. Capital acquisition/title costs and private disputes are not ordinary revenue trade expenditure; specific s 11(c) applications are held below. |
| ALLAN GRAY, CORONATION, 10X, SYGNIA, NINETY ONE, OLD MUTUAL RA, MOMENTUM RA, LIBERTY RA | Reconcile fund certificates to actual contributions; use the separate retirement step. |
| DISCOVERY HEALTH, BONITAS, GEMS, MEDIHELP | Use the separate medical-credit step, not an ordinary income deduction. |
| KULULA, FLYSAFAIR, AIRLINK, SAA; UBER, BOLT; AVIS, EUROPCAR, HERTZ; ENGEN, SHELL, BP, SASOL, CALTEX, TOTAL; SANRAL/E-TOLL | Labels for investigating actual travel/fuel/hire/tolls, with journey, invoice and business/private evidence. No assertion that a named carrier or service currently operates. Deemed employee travel rates do not establish a sole-trader deduction. |
| INCREDIBLE CONNECTION, MATRIX, TAKEALOT; OFFICE NATIONAL, WALTONS; POSTNET, SA POST OFFICE; MAKRO, GAME | Distinguish consumables, stock and assets. Test actual purchases; use wear-and-tear rules for qualifying assets. No operating-status inference for postal providers. |
| PICK N PAY, WOOLWORTHS, CHECKERS, SPAR, SHOPRITE; RESTAURANT | Identify private groceries/family meals versus genuine evidenced trade spending. Do not apply a blanket sole-proprietor entertainment prohibition. VAT treatment requires separate review. |
| UIF, COIDA/COMPENSATION FUND, CIPC; TENANT/RENT/PAY PROP/RENT PROPERTY MANAGEMENT; GIVENGAIN/BACKABUDDY; VEHICLE TRADER/AUCTION HOUSE/BUSINESS BUYER | Flag the employer, entity/capital, rental, donation or disposal topic; use the named holds below where applicable. |

### Home office and wear-and-tear

A part of a dwelling must be specifically equipped for the trade and regularly and exclusively used for it (s 23(b)); a dual-use room does not qualify. Employee/office-holder restrictions are additional tests for employment, not a substitute for the sole-trader rule. Establish qualifying area and actual expense categories before allocating premises expenses; do not claim loan principal. Home-loan interest and disposal/primary-residence CGT outcomes require separate review before the first claim. [Statutory text, IN 45 Annexure](https://www.sars.gov.za/wp-content/uploads/Legal/Notes/Legal-IntR-IN-45-Deduction-of-security-expenditure.pdf).

For a qualifying trade asset under s 11(e), use cost on the appropriate VAT basis, excluding finance charges; do not duplicate another asset allowance. Under BGR 7 Issue 4, small-item immediate write-off requires **cost strictly below R7,000**, independent function, no set, acquisition and bringing into use in the year, and no acquisition by a lessor for letting. Exactly R7,000 fails the concession. A table with six chairs cannot be split artificially. Independently functioning laptops are tested individually; a configured computer set requires actual functional evidence. [BGR 7, 4.2 and 4.3.5](https://www.sars.gov.za/wp-content/uploads/Legal/Rulings/BGR/LAPD-IntR-R-BGR-2012-07-Wear-And-Tear-Depreciation-Allowance.pdf).

BGR 7 allows a choice of straight-line or diminishing-value method; keep records. Apportion wear-and-tear for part-year trade use and private use. Used assets require their remaining expected life. Printers/unlisted items need supported classification/life, not an invented standard period. The following are SARS's straight-line periods for the stated classes, not automatic periods for every used asset. [BGR 7, 4.3.2–4.3.10 and Annexure](https://www.sars.gov.za/wp-content/uploads/Legal/Rulings/BGR/LAPD-IntR-R-BGR-2012-07-Wear-And-Tear-Depreciation-Allowance.pdf).

| Asset class | Years | Official source |
|---|---|---|
| Personal computers / mainframe computers and servers | 3 / 5 | https://www.sars.gov.za/wp-content/uploads/Legal/Rulings/BGR/LAPD-IntR-R-BGR-2012-07-Wear-And-Tear-Depreciation-Allowance.pdf |
| Furniture and fittings / cellular telephones | 6 / 2 | https://www.sars.gov.za/wp-content/uploads/Legal/Rulings/BGR/LAPD-IntR-R-BGR-2012-07-Wear-And-Tear-Depreciation-Allowance.pdf |
| Electronic / mechanical office equipment | 3 / 5 | https://www.sars.gov.za/wp-content/uploads/Legal/Rulings/BGR/LAPD-IntR-R-BGR-2012-07-Wear-And-Tear-Depreciation-Allowance.pdf |
| Passenger cars / delivery vehicles | 5 / 4 | https://www.sars.gov.za/wp-content/uploads/Legal/Rulings/BGR/LAPD-IntR-R-BGR-2012-07-Wear-And-Tear-Depreciation-Allowance.pdf |

### Retirement contributions: actual payment first

For ordinary full-year YoA 2025/2026 cases, s 11F allows actual qualifying member contributions (plus a substantiated eligible carry-in), limited to the least of: **R350,000; 27.5% of the greater of qualifying remuneration and taxable income; and taxable income before taxable capital gains**. Both income bases exclude retirement lump-sum/withdrawal and severance benefits and are determined before deductions under ss 11F, 6quat(1C) and 18A. Do not manufacture a contribution equal to the percentage limit. [Act 17/2017 s 21, inserting s 11F](https://www.gov.za/sites/default/files/gcis_document/201712/act-17-of2017g41342gon1451.pdf); [Act 23/2018 s 26, correcting the bases](https://www.sars.gov.za/wp-content/uploads/Legal/AmendActs/LAPD-LPrim-AA-2018-03-Taxation-Laws-Amend-Act-23-of-2018-GG-42172.pdf).

Unused qualifying contributions carry forward only to the extent not already deducted, used against a lump sum, or taken into account for s 10C exemption. They do not create a fresh automatic tax-free lump-sum allowance. For multiple short years within the March-to-February cycle, the statutory combined ceiling must be considered; do not give a full ceiling in each return. [Act 17/2017 s 21](https://www.gov.za/sites/default/files/gcis_document/201712/act-17-of2017g41342gon1451.pdf); [Act 23/2018 s 26](https://www.sars.gov.za/wp-content/uploads/Legal/AmendActs/LAPD-LPrim-AA-2018-03-Taxation-Laws-Amend-Act-23-of-2018-GG-42172.pdf); [Act 17/2023 s 13](https://www.sars.gov.za/wp-content/uploads/Legal/AmendActs/Legal-LPrim-AA-2023-03-Taxation-Laws-Amendment-Act-17-of-2023-GG-49894-Notice-4226-22-December-2023.pdf).

**YoA 2027 cap-change hold:** the old Guide's R430,000 claim is not an unconditional enacted ceiling here. SARS publishes that figure, but B34/2026 clause 7 still proposes replacing R350,000 and its short-year ceiling. No enacted replacement was established in this proof. Cases depending on the increase stay non-usable; do not substitute R350,000 as a purported current administrative instruction either. Check this point with one of our partner accountants. The R80,000 contribution in Example 1 is below both ceilings, so the disputed increase does not change that ordinary full-year example. [SARS Bills register](https://www.sars.gov.za/legal-counsel/preparation-of-legislation/bills/); [B34/2026, clause 7, proposal only](https://www.sars.gov.za/legal-lprep-bills-2026-03-rates-and-monetary-amounts-and-amendment-of-revenue-laws-bill-b34-2026-21-october-2026/).

### Medical credits

Claim s 6A against normal tax for eligible months of actual qualifying fees paid to a registered medical scheme or qualifying equivalent foreign fund for the taxpayer/dependants. Use payer certificates; if more than one person pays, apportion the credit by the statutory fee-payment ratio. Taxable employer contributions can be deemed paid by the individual; a bank debit alone does not prove this. Credits cannot exceed normal tax before PAYE/provisional offsets, cannot create a negative normal-tax liability, and unused credits do not carry forward. [SARS medical-credit guide, 2.2, 2.5 and Annexure A s 6A](https://www.sars.gov.za/wp-content/uploads/Ops/Guides/Legal-Pub-Guide-IT07-Guide-on-the-Determination-of-Medical-Tax-Credits.pdf).

For s 6B, let F be qualifying scheme fees paid, M the s 6A credit, Q qualifying unreimbursed medical expenses actually paid, and T taxable income excluding retirement lump sums, withdrawal benefits and severance benefits. Count only qualifying expenses under the statutory definition, not every medical or insurance payment. For under-65 taxpayers without the qualifying disability condition, the additional credit is **25% × max(0, max(0, F − 4M) + Q − 7.5% × T)**. For age 65+ or disability of the taxpayer, spouse or statutory child, it is **33.3% × (max(0, F − 3M) + Q)**. Other dependants' disability does not alone activate that second formula. Confirm the statutory child/disability definition, diagnosis and prescribed expenditure before applying it; disputed eligibility remains held. [ITA s 6B, reproduced in Annexure A; guide 3.1–3.6](https://www.sars.gov.za/wp-content/uploads/Ops/Guides/Legal-Pub-Guide-IT07-Guide-on-the-Determination-of-Medical-Tax-Credits.pdf).

### Turnover tax and normal tax comparison

Keep qualifying turnover, taxable turnover and normal-tax profit distinct. Do not deduct ordinary expenses from the turnover-tax base. Establish actual registration and the full Sixth Schedule eligibility tests before comparing liabilities; a non-professional label or turnover alone is insufficient. The old blanket ban on any professional receipts and statement that turnover tax automatically eliminates VAT are withdrawn. Election, professional-service receipts test, connected interests, asset disposals, other-income treatment, VAT coexistence, entry/exit and temporary excess require a complete eligibility review: **Check this point with one of our partner accountants.** [SARS administration guide](https://www.sars.gov.za/guide-to-administration-of-turnover-tax/).

For a **registered qualifying microbusiness in YoA 2025 or 2026**, apply the following to its established taxable turnover. [Act 19/2023 s 2(4), Schedule I para 8](https://www.sars.gov.za/wp-content/uploads/Legal/AmendActs/Legal-LPrim-AA-2023-01-Rates-and-Monetary-Amounts-and-Amendment-of-Revenue-Laws-Act-19-of-2023-GG-49948-Notice-4228-22-December-2023.pdf).

| Taxable turnover | YoA 2025/2026 tax | Official source |
|---|---|---|
| Up to R335,000 | Nil | https://www.sars.gov.za/wp-content/uploads/Legal/AmendActs/Legal-LPrim-AA-2023-01-Rates-and-Monetary-Amounts-and-Amendment-of-Revenue-Laws-Act-19-of-2023-GG-49948-Notice-4228-22-December-2023.pdf |
| Above R335,000 to R500,000 | 1% above R335,000 | https://www.sars.gov.za/wp-content/uploads/Legal/AmendActs/Legal-LPrim-AA-2023-01-Rates-and-Monetary-Amounts-and-Amendment-of-Revenue-Laws-Act-19-of-2023-GG-49948-Notice-4228-22-December-2023.pdf |
| Above R500,000 to R750,000 | R1,650 + 2% above R500,000 | https://www.sars.gov.za/wp-content/uploads/Legal/AmendActs/Legal-LPrim-AA-2023-01-Rates-and-Monetary-Amounts-and-Amendment-of-Revenue-Laws-Act-19-of-2023-GG-49948-Notice-4228-22-December-2023.pdf |
| Above R750,000, while eligible | R6,650 + 3% above R750,000 | https://www.sars.gov.za/wp-content/uploads/Legal/AmendActs/Legal-LPrim-AA-2023-01-Rates-and-Monetary-Amounts-and-Amendment-of-Revenue-Laws-Act-19-of-2023-GG-49948-Notice-4228-22-December-2023.pdf |

**YoA 2027 turnover-change hold:** the later original R650,000 case used the published R600,000 nil band and 1% next band to obtain R500. Its full rate/eligibility commencement was not established against operative legislation. The SARS main page says 1 April 2026; its administration guide distinguishes 1 March for individuals and 1 April for companies. The former R2.3m, R950,000, R1.4m and R12,500 matrix and the R500 outcome are **not usable filing advice** pending that reconciliation. Do not use the historical table for a current return. Check this point with one of our partner accountants. [SARS turnover page](https://www.sars.gov.za/types-of-tax/turnover-tax/); [administration guide, Summary](https://www.sars.gov.za/guide-to-administration-of-turnover-tax/).

### Computation order and provisional tax

Prepare trade profit, then other income/exemptions and substantiated statutory deductions, then taxable income, ordinary tax, age rebates and medical credits, and finally actual PAYE/provisional payments. Keep unresolved specialist adjustments separate. IRP6 is an estimate/advance payment of normal tax, not an extra tax or an income deduction. Use the current year's estimate; retain the latest qualifying prior assessment/basic amount for its separate statutory function. Do not simply repeat last year's income or prohibit all use of it. [SARS provisional guide, 2, 5 and 9](https://www.sars.gov.za/wp-content/uploads/Ops/Guides/GEN-PT-01-G01-Guide-for-Provisional-Tax-External-Guide.pdf).

For the ordinary resident case, let A be normal tax on the annual estimate after applicable rebates and medical credits. First instalment: A/2 less first-period PAYE and qualifying s 6quat credit proved payable by that period's end. Second instalment: full-year A less annual PAYE, **first instalment actually paid**, and qualifying annual s 6quat credit. Foreign-credit entitlement and remission are separate held decisions. [Guide 9.1, statutory Fourth Schedule calculation](https://www.sars.gov.za/wp-content/uploads/Ops/Guides/GEN-PT-01-G01-Guide-for-Provisional-Tax-External-Guide.pdf).

For an ordinary March–February year, first provisional payment is nominally 31 August, second the last day of February; a voluntary interest-reducing top-up is nominally 30 September after that year. Advance weekend/public-holiday payment dates to the preceding working day. Thus the YoA 2027 second payment is ordinarily **26 February 2027**, because 28 February is Sunday, absent a specific extension. Short years and alternative accounting cycles need their own calculation. [Guide 10, especially 10(j)](https://www.sars.gov.za/wp-content/uploads/Ops/Guides/GEN-PT-01-G01-Guide-for-Provisional-Tax-External-Guide.pdf).

**Underestimation, late-payment and interest hold:** the original R1.8m safe-harbour assertion conflicts with the later SARS guide's R1m discussion. The original estimate R200,000 versus actual R450,000 does not establish a penalty without the applicable basic amount, payments/withholding, operative year rules and possible relief. Do not output the original R12,406, an automatic 20% penalty, or treat a late payment as automatically attracting an underestimation penalty. Check this point with one of our partner accountants. [Guide 14](https://www.sars.gov.za/wp-content/uploads/Ops/Guides/GEN-PT-01-G01-Guide-for-Provisional-Tax-External-Guide.pdf).

### Pre-trade costs and records

ITA s 11A requires commencement of the particular trade, actual expenditure before and in preparation for it, satisfaction of the specified post-commencement deduction test, and no prior deduction. Excess is ring-fenced to that trade; it is not automatically an assessed loss available against unrelated income. Deposits, incorporation, initial stock and professional fees each need their own underlying classification. [IN 51 Issue 6, quoted s 11A and 4.1, 4.4, 4.6](https://www.sars.gov.za/wp-content/uploads/Legal/Notes/Legal-IN-51-Pre-trade-expenditure-and-losses.pdf).

Retain invoices, certificates, bank reconciliations, logbooks, asset records and working papers. The ordinary submitted-return period is five years from submission; missing returns and notified/known audit or investigation require additional retention. As a working-paper safeguard, do not destroy disputed records before the matter is final or while any applicable longer retention applies. [SARS records page](https://www.sars.gov.za/client-segments/record-keeping/). Determining the disposal date for non-filed, disputed, capital-asset or exceptional records: Check this point with one of our partner accountants.

## Worked cases

These preserve the original inputs. Ordinary-income cases assume a full year, qualifying documented expenses/contributions, no carry-in, no other income, taxable capital gains, lump sums or deductions, no disability and no qualifying out-of-pocket medical costs unless stated. Medical fees are paid by this taxpayer for all covered months. A numeric result is a working-paper result subject to those facts, not a filing declaration.

### Example 1 and Test 1: original mid-range inputs

Age **35**, revenue **R600,000**, expenses **R180,000**, RA paid **R80,000**, medical fees **R3,500/month** for the member and **one dependant**, provisional tax actually paid **R40,000**. Net profit is R420,000. The percentage ceiling is R115,500, but only **R80,000** was contributed, so taxable income is **R340,000**.

For the later **2026/27 (YoA 2027)** example: basic tax R68,792, primary rebate R17,820, s 6A R9,024, s 6B nil, normal tax **R41,948**, leaving **R1,948 payable** after R40,000 provisional. The previous R32,718/R7,282 refund and Test 1's R32,710 are withdrawn: the deduction cannot exceed the actual contribution. [Rate table](https://www.sars.gov.za/tax-rates/income-tax/rates-of-tax-for-individuals/); [s 11F](https://www.gov.za/sites/default/files/gcis_document/201712/act-17-of2017g41342gon1451.pdf); [s 6B](https://www.sars.gov.za/wp-content/uploads/Ops/Guides/Legal-Pub-Guide-IT07-Guide-on-the-Determination-of-Medical-Tax-Credits.pdf).

```oa-check
name: YoA2027 original mid-range, cap-independent R80000 contribution
steps:
  - profit: 600000 - 180000
  - limit: 0.275 * profit
  - retirement: min(80000, 350000, limit, profit)
  - taxable: profit - retirement
  - basic: 44118 + 0.26 * (taxable - 245100)
  - medical: 376 * 2 * 12
  - additional: 0.25 * max(0, max(0, 3500 * 12 - 4 * medical) - 0.075 * taxable)
  - normal: max(0, basic - 17820 - medical - additional)
  - balance: normal - 40000
expected:
  profit: 420000
  limit: 115500
  retirement: 80000
  taxable: 340000
  basic: 68792
  additional: 0
  normal: 41948
  balance: 1948
```

The R350,000 in this **minimum test** establishes that the R80,000 result does not depend on a disputed higher 2027 ceiling; it does not instruct the use of that old ceiling for a current cap-dependent claim.

For the explicitly original **2025/26 (YoA 2026)** test, the same inputs give basic tax R69,432, rebate R17,235, s 6A R8,736, s 6B nil, normal tax **R43,461** and **R3,461 payable** after the original provisional payment. The April historical R34,231/R5,769 refund also deducted the ceiling rather than the contribution and is withdrawn. These same ordinary-rate figures apply to the frontmatter's **YoA 2025** on these full-year facts. [Historical rates](https://www.sars.gov.za/tax-rates/income-tax/rates-of-tax-for-individuals/); [medical rates](https://www.sars.gov.za/tax-rates/medical-tax-credit-rates/).

```oa-check
name: YoA2025 and YoA2026 original mid-range inputs
steps:
  - profit: 600000 - 180000
  - retirement: min(80000, 350000, 0.275 * profit, profit)
  - taxable: profit - retirement
  - basic: 42678 + 0.26 * (taxable - 237100)
  - medical: 364 * 2 * 12
  - additional: 0.25 * max(0, max(0, 3500 * 12 - 4 * medical) - 0.075 * taxable)
  - normal: max(0, basic - 17235 - medical - additional)
  - result_3: normal - 40000
expected:
  basic: 69432
  normal: 43461
  result_3: 3461
```

### Example 2 and Test 3: turnover R650,000

Original inputs: **non-professional sole proprietor, R650,000 turnover**. The original words do not establish registration or the taxable-turnover base; do not infer them. **If registration, eligibility and R650,000 taxable turnover are independently established for 2025/26**, tax is R1,650 + 2% × R150,000 = **R4,650**, as in the April historical case. [Act 19/2023 Schedule I para 8](https://www.sars.gov.za/wp-content/uploads/Legal/AmendActs/Legal-LPrim-AA-2023-01-Rates-and-Monetary-Amounts-and-Amendment-of-Revenue-Laws-Act-19-of-2023-GG-49948-Notice-4228-22-December-2023.pdf).

```oa-check
name: YoA2026 conditional registered microbusiness R650000
steps:
  - historical_tax: 1650 + 0.02 * (650000 - 500000)
expected:
  historical_tax: 4650
```

The later **2026/27** version's R500 is preserved solely as the arithmetic (650,000 − 600,000) × 1% = 500 for its **held** rate assumptions. Its eligibility/commencement and final tax outcome remain non-usable. Check this point with one of our partner accountants. Do not silently assign that case to 2025/26 or deduct invented expenses to compare normal tax.

### Example 3: R15,000 client-entertainment dinners

Keep the supplied **R15,000**. Decide trade purpose, actual incurrence and private/capital exclusions from evidence under ss 11(a), 23(b) and 23(g). Do not automatically deny a sole proprietor's bona fide trade meals under the employee restriction, and do not approve every labelled client dinner. No evidenced deductible portion was supplied: **no final deduction is computed**. VAT is separately held. [Quoted law, IN 45 Annexure](https://www.sars.gov.za/wp-content/uploads/Legal/Notes/Legal-IntR-IN-45-Deduction-of-security-expenditure.pdf).

### Example 4 and Test 4: contribution above the ceiling

Keep **R2,000,000 taxable income before retirement deduction** and **R600,000 actual RA contributions**, with no other adjustments. For the original **2025/26** period: 27.5% × R2m = R550,000; the R350,000 ceiling gives **R350,000 deducted and R250,000 unused**, subject to the carryforward/no-double-use conditions. [ITA s 11F](https://www.gov.za/sites/default/files/gcis_document/201712/act-17-of2017g41342gon1451.pdf).

```oa-check
name: YoA2026 original retirement-cap inputs
steps:
  - deduction: min(600000, 350000, 0.275 * 2000000, 2000000)
  - unused: 600000 - deduction
expected:
  deduction: 350000
  unused: 250000
```

For the later **2026/27** case, the original **R430,000 deduction and R170,000 excess** depend on the held R430,000 ceiling. The subtraction recomputes, but those are **non-usable conditional figures**, not a verified 2027 deduction. Check this point with one of our partner accountants.

### Original Test 2: senior

Age **68**, revenue **R200,000**, expenses **R50,000**, actual RA **R30,000**. Full-year profit R150,000; percentage ceiling R41,250; taxable income R120,000; basic tax R21,600. Original **2025/26** primary-plus-secondary rebates R26,679 reduce normal tax to **nil**; later **2026/27** cumulative rebates R27,585 also give nil. No payment/refund inference is made without tax-payment records. [Rates/rebates](https://www.sars.gov.za/tax-rates/income-tax/rates-of-tax-for-individuals/).

```oa-check
name: YoA2026 and YoA2027 original senior inputs
steps:
  - profit: 200000 - 50000
  - retirement: min(30000, 350000, 0.275 * profit, profit)
  - basic: 0.18 * (profit - retirement)
  - result_4: max(0, basic - 17235 - 9444)
  - result_5: max(0, basic - 17820 - 9765)
expected:
  profit: 150000
  retirement: 30000
  basic: 21600
  result_4: 0
  result_5: 0
```

### Original Test 5: six covered persons

Keep **six members** and assume qualifying paid fees for twelve months and one payer. **2025/26:** (R364 × 2 + R246 × 4) × 12 = **R20,544**. Later **2026/27:** (R376 × 2 + R254 × 4) × 12 = **R21,216**. Actual allowed credit remains limited to normal tax; it does not create a refund independently of payments. [Medical rates](https://www.sars.gov.za/tax-rates/medical-tax-credit-rates/).

```oa-check
name: Original six-member medical case, distinct assessment periods
steps:
  - historical: (364 * 2 + 246 * 4) * 12
  - later: (376 * 2 + 254 * 4) * 12
expected:
  historical: 20544
  later: 21216
```

### Original Test 6: estimate R200,000; actual R450,000

Inputs and original periods remain **R200,000 estimated and R450,000 actual**, for the original **2025/26** test and later **2026/27** version. Missing basic amount, payments/withholding and operative penalty conditions prevent a tax-penalty calculation. The old **R12,406**, subsequent automatic **20%** conclusion, and **R1.8m** threshold are withdrawn from usable outputs. Check this point with one of our partner accountants.

## Boundary and exception table

| Original edge | Destination and safe action |
|---|---|
| EC1 interest | Use the SA-source personal exemption in the relief table; establish residence/source. |
| EC2 professional turnover receipts | Eligibility hold below; no blanket professional-services ban. |
| EC3 excess retirement | Retirement/carryforward conditions above; cap-dependent 2027 outcome held. |
| EC4 dual-use home office | Fails exclusive-use test; separately review home-loan/CGT outcome. |
| EC5 provisional underestimation | Test 6 and penalty hold; no automatic percentage or amount. |
| EC6 large medical family | Test 5 and actual payment/month/tax limits. |
| EC7 foreign income | Residence, source, treaty and foreign-credit hold below. |
| EC8 midyear turnover exit | Registration/transition hold; do not splice regimes automatically. |
| EC9 entertainment | Example 3 trade-purpose decision; VAT separately held. |
| EC10 assessed loss | Section 20/20A hold below; no automatic cross-trade set-off. |

## When to refuse or refer

The following topics from the original current/historical text remain present as **non-usable holds**, with no entitlement, tax rate or filing outcome implied. Do not use a former headline amount or bank pattern to bypass a hold. The accountant needs the actual policy, asset, contract, group, residence, election and timing facts as applicable.

- **Insurance structures and proceeds:** key-person/group-risk s 11(w)(i)/(ii), elections and security cessions, contingent-liability/surety and buy-and-sell cover, personal life and income-protection premiums/proceeds, fringe benefits, recoupments and estate exclusions. No “default tax-free” policy or structure recommendation. Check this point with one of our partner accountants.
- **VAT and transport cross-references:** airfare component VAT, passenger transport/platform fares and non-fare incentives, motor-car hire input blocks and entertainment exceptions. Income-tax trade purpose does not determine input VAT. Check this point with one of our partner accountants.
- **Home-office loan and disposal consequences:** establish ownership, bond purpose, actual trade-use apportionment and primary-residence/CGT effects before claiming; do not promise that only an annual exclusion applies. Check this point with one of our partner accountants.
- **Specific trade-interest and legal-cost rules:** borrowed-fund use, s 24J/s 11G timing/limitations and specific s 11(c) disputes/arbitration. Check this point with one of our partner accountants.
- **Restraint of trade:** payer spreading under s 11(cA), recipient inclusion and PAYE; the old “shorter of restraint period or three years” instruction is not usable. Check this point with one of our partner accountants.
- **R&D s 11D:** entity gateway, approval, expenditure and sunset; do not apply the company incentive to a sole proprietor merely because the activity is innovative. Check this point with one of our partner accountants.
- **Renewables s 12B/12BA:** solar capacity boundaries including exactly 1MW, hydro including exactly 30MW, bringing-into-use dates, the original 1 March 2023–28 February 2025 temporary window, actual trade/private use, cost and recoupment. Floor area is not an automatic generation-use allocation. No new 2026 installation is treated as inside that historical window. Check this point with one of our partner accountants.
- **Manufacturing/special asset s 12C:** new/unused versus used plant, qualifying manufacture, hotel/aircraft/ship categories and recoupments; no general accelerated entitlement. Check this point with one of our partner accountants.
- **Small business corporations s 12E/structure choice:** entity/shareholding/income/services gates, current rate bands and manufacturing allowance. Do not import company relief into the individual computation. Check this point with one of our partner accountants.
- **Learnership s 12H:** registered agreement, employee/lead-host employer, NQF/disability, annual/completion amounts, duration/proration, registration timing, sunset and SDL interaction. Check this point with one of our partner accountants.
- **Energy savings s 12L:** certification/baseline, qualifying savings, concurrent incentives and claim amount. Check this point with one of our partner accountants.
- **Buildings:** s 13 industrial/hotel, s 13quin commercial, s 13quat UDZ including extension and municipality/certificate, s 13sex new/unused residential/low-cost units and portfolio threshold; cost/deemed-cost, use, part-year treatment and recoupment. Do not apply one depreciation rate or universal part-year proration to all categories. Check this point with one of our partner accountants.
- **Donations deduction s 18A:** approved recipient/purpose, cash/kind valuation, valid receipt/certificate, income-base order/limit, excess and IT3(d) reporting/prepopulation. A charity platform debit alone is insufficient. Check this point with one of our partner accountants.
- **Assessed losses/ring-fencing ss 20/20A:** natural-person trade continuation, maximum-rate income entry test, multi-year loss tests, listed/suspect activities and exceptions/escape clauses, same-trade set-off and carryforward. Do not import the company loss cap or use a stale high-income threshold. Check this point with one of our partner accountants.
- **Residence, overseas income and credits:** ordinary residence, physical-presence boundaries/part days, cessation/330-day rule, treaty tie-break, foreign trade versus employment exemption, s 9H exit events, s 6quat credits/deduction, source/limitation/carryforward and elections. A bank account does not establish residence. Check this point with one of our partner accountants.
- **Capital gains:** equipment/vehicle/property/practice/business sale, home-office use, cessation/death, recoupment, inclusion, annual/death/primary-residence and small-business relief/age/asset-value/holding conditions. No disposal computation without proceeds, base cost and relevant use history. Check this point with one of our partner accountants.
- **Donations tax:** donor/donee, resident-spouse and other exemptions, cumulative rates, annual exemption/effective date, IT144, payment/filing dates, joint liability and penalties. Check this point with one of our partner accountants.
- **Estate duty:** resident/non-resident asset population, deemed insurance property, spouse deduction, abatement/portability, rate bands and deductible liabilities. Check this point with one of our partner accountants.
- **Tax-free investments s 12T:** account qualification, annual/lifetime caps and effective dates, excess-contribution tax, exempt returns and withdrawal/redeposit history. No ordinary deduction for a labelled savings debit. Check this point with one of our partner accountants.
- **Family attribution/trusts:** ss 7, 7C and 25B, conditional/minor/spouse transfers, resident donor/non-resident recipient direction, trust-loan exclusions/official interest and beneficiary residence, income/capital distributions and Eighth Schedule para 80. Do not apply a former “current 9%” assumption or an unconditional conduit rule. Check this point with one of our partner accountants.
- **Dividends:** domestic exemption exceptions/REITs, dividends withholding, foreign full/partial exemptions (including which fraction is exempt), shareholding, treaty and credit limits. Check this point with one of our partner accountants.
- **Employer obligations:** payroll/PAYE, UIF, COIDA, SDL remuneration and exemption threshold, returns and deductions; owner drawings are not proof of employee remuneration. Check this point with one of our partner accountants.
- **Non-resident withholding:** royalties, interest, immovable-property sellers and foreign entertainers/sportspersons; payer/source/exemptions/treaty, seller type, returns and distinct payment periods. Do not apply a universal month-end due date. Check this point with one of our partner accountants.
- **Personal service providers:** incorporation/employment-like tests, client control and income concentration, qualifying unrelated full-time employee exception, PAYE and deduction restrictions. No classification by “three or fewer employees”. Check this point with one of our partner accountants.
- **Prepayments/contingencies:** s 23H service period and aggregate exceptions, s 23(e), leave/bonus/warranty provisions and actual unconditional obligations. Accounting accruals alone are not a tax deduction. Check this point with one of our partner accountants.
- **Bad and doubtful debts:** s 11(i) inclusion/irrecoverability and exceptions; s 11(j) accounting-method, ageing and security rules, including the former 60/90-day versus 120-day conflict. No deduction from an uncollected bank receipt alone. Check this point with one of our partner accountants.
- **CIPC/entity fees and rental portfolios:** distinguish initial capital/entity costs, ongoing costs, ordinary letting receipts/expenses, repairs versus improvements, mixed use and building allowances. No blanket “CIPC deductible” or “all rent net of any bond payment” rule. Check this point with one of our partner accountants.

## Filing and payment

Use the individual **ITR12** for the actual assessment year and the **IRP6** provisional process when applicable. Enter trade figures and supported retirement/medical/donation/other-income details in their respective sections; reconcile prepopulated certificates and payments to source records. Obtain professional review before filing. Enter eFiling through the official [SARS site](https://www.sars.gov.za); the SARS provisional guide identifies the eFiling channel and IRP6. Do not rely on the old asserted redirect history of a portal domain. After submission retain acknowledgement and assessment and reconcile the assessed balance/payment reference. Return deadlines, assessment-specific payment dates and any relief or missing historical notices must be confirmed for that return: Check this point with one of our partner accountants.

## Completion checklist

Keep the original working-paper structure: **Transactions** columns Date, Counterparty, Description, Amount (ZAR), Category (Revenue/Expense/Wear-and-tear/RA/Medical/EXCLUDE), Deductible amount, Default?, Question, Notes; **ITR12 Computation** follows the computation order above. Treat bank CSV date/delimiter, DEBICHECK, MAGTAPE, SASWITCH, PREPAID and MUNICIPALITY as fields/labels to inspect in the actual export, not fixed deductibility or residency rules. Verify signs, dates, duplicates and balances. Monthly debit patterns only prompt certificate reconciliation.

Before handoff, trace every input to records, check period-specific rates and reliefs, recompute examples, list held adjustments and missing evidence, and retain the review record. Never claim professional approval, a definitive liability or a filed return from this working paper.

### Historical attribution record

The following existing credit/metadata text is preserved verbatim as historical provenance. It does not assert that this revision has received a new professional sign-off or that the former generated block was proven:

```text
Reviewed against the cited tax authorities by Werner Britz on 2026-06-12. Items flagged for further clarification are tracked separately and excluded here. This block is generated from verified skill_facts — edit the facts, not the prose.
Update after sign-off by Werner Britz CA(SA).
| Validated by | Werner Britz CA(SA), Spurwing CFO |
| Validation date | May 2026 |
```

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a registered tax practitioner, CA(SA), or equivalent licensed practitioner in South Africa) before filing or acting upon.

> Contributed by Brandon Iverach.


## Sources

Read scope is the listed sections, not the entire document. Existing exact statutory/rate quotes from the private rate-card ledger read 2026-11-26 are reused once for unchanged periods and conditions. The 2026-11-22 findings were read first; their absent exact quotes were not treated as completed proof. New reads below supply the operative words where guidance had been incomplete. A Bill is evidence of a proposal only.

| Source and read scope | URL | Read on |
|---|---|---|
| Individual rates: YoA 2025/2026/2027 bands, rebates, thresholds; unchanged exact rate-card quotes reused | https://www.sars.gov.za/tax-rates/income-tax/rates-of-tax-for-individuals/ | 2026-11-26 reused; 2026-11-27 applicability |
| Individual income-tax guide: year-of-assessment definition and ordinary income; exact quote reused | https://www.sars.gov.za/wp-content/uploads/Ops/Guides/Legal-Pub-Guide-IT01-Guide-on-Income-Tax-and-the-Individual.pdf | 2026-11-26 reused |
| Interest: SA-source personal exemptions, unchanged exact quote reused | https://www.sars.gov.za/tax-rates/income-tax/interest-and-dividends/ | 2026-11-26 reused |
| Medical rates: qualifying-person/month table, unchanged exact quotes reused | https://www.sars.gov.za/tax-rates/medical-tax-credit-rates/ | 2026-11-26 reused |
| Act 23/2018: ss 3–5 temporary budget effect and s 26 retirement bases/carry-in | https://www.sars.gov.za/wp-content/uploads/Legal/AmendActs/LAPD-LPrim-AA-2018-03-Taxation-Laws-Amend-Act-23-of-2018-GG-42172.pdf | 2026-11-26 temporary-effect quotes reused; 2026-11-27 s 26 read |
| Act 19/2023: s 3 age rebates; s 2(4), Schedule I para 8 historical turnover table | https://www.sars.gov.za/wp-content/uploads/Legal/AmendActs/Legal-LPrim-AA-2023-01-Rates-and-Monetary-Amounts-and-Amendment-of-Revenue-Laws-Act-19-of-2023-GG-49948-Notice-4228-22-December-2023.pdf | 2026-11-26 s 3 reused; 2026-11-27 turnover sections read |
| Act 17/2017 s 21: full inserted s 11F actual contributions, three ceilings and carry-in | https://www.gov.za/sites/default/files/gcis_document/201712/act-17-of2017g41342gon1451.pdf | 2026-11-27 |
| Act 17/2023 s 13: retirement short-year aggregate ceiling and employer-contribution condition | https://www.sars.gov.za/wp-content/uploads/Legal/AmendActs/Legal-LPrim-AA-2023-03-Taxation-Laws-Amendment-Act-17-of-2023-GG-49894-Notice-4226-22-December-2023.pdf | 2026-11-27 |
| Medical guide Issue 18: 2.2/2.5, 3.1–3.6 and Annexure A ss 6A/6B, statutory definitions/formulas | https://www.sars.gov.za/wp-content/uploads/Ops/Guides/Legal-Pub-Guide-IT07-Guide-on-the-Determination-of-Medical-Tax-Credits.pdf | 2026-11-27 |
| IN 45 Issue 5: Annexure ss 11(a)/(e), 23(b)/(g), actual trade and home-office gates | https://www.sars.gov.za/wp-content/uploads/Legal/Notes/Legal-IntR-IN-45-Deduction-of-security-expenditure.pdf | 2026-11-27 |
| BGR 7 Issue 4: 4.2, 4.3.2–4.3.10 and named Annexure classes | https://www.sars.gov.za/wp-content/uploads/Legal/Rulings/BGR/LAPD-IntR-R-BGR-2012-07-Wear-And-Tear-Depreciation-Allowance.pdf | 2026-11-27 |
| IN 51 Issue 6: quoted s 11A, 4.1/4.4/4.6 and quoted ss 11(a)/23(g) | https://www.sars.gov.za/wp-content/uploads/Legal/Notes/Legal-IN-51-Pre-trade-expenditure-and-losses.pdf | 2026-11-27 |
| Provisional guide rev 28: 2, 5, 9.1, 10 and 14; exact unchanged formulas/date rules reused; penalty conflicts remain held | https://www.sars.gov.za/wp-content/uploads/Ops/Guides/GEN-PT-01-G01-Guide-for-Provisional-Tax-External-Guide.pdf | 2026-11-26 formula quotes reused; 2026-11-27 2/10/14 read |
| Records: submitted/non-filed/audit/investigation cases; no “whichever first” disposal shortcut adopted | https://www.sars.gov.za/client-segments/record-keeping/ | 2026-11-27 |
| Bills register and B34 clause 7: proposal/status only, no enacted-cap proof | https://www.sars.gov.za/legal-counsel/preparation-of-legislation/bills/ ; https://www.sars.gov.za/legal-lprep-bills-2026-03-rates-and-monetary-amounts-and-amendment-of-revenue-laws-bill-b34-2026-21-october-2026/ | 2026-11-27 |
| Turnover main/admin pages: actual conflicting commencement/eligibility text read, not final-law clearance | https://www.sars.gov.za/types-of-tax/turnover-tax/ ; https://www.sars.gov.za/guide-to-administration-of-turnover-tax/ | 2026-11-27 |

Not yet confirmed: **Non-usable holds**, not operative guidance: 2027 retirement-ceiling enactment/short-year implementation; 2027 turnover commencement/eligibility and cap-dependent outcomes; provisional penalty thresholds/basic amount/remission/interest; short years and filing-specific dates; home-office loan/CGT; every specialist topic expressly listed under “When to refuse or refer”; exact bank-export/network and historical carrier/postal operating-status claims. All original case inputs and assessment-period labels remain above, including held numerical outcomes. Check this point with one of our partner accountants.
