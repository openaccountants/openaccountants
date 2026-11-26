---
name: ae-corporate-tax
description: "Use this skill whenever asked about UAE Corporate Tax for freelancers, sole establishments, or small businesses. Trigger on phrases like \"how much tax do I pay in UAE\", \"corporate tax UAE\", \"CT return\", \"FTA\", \"small business relief\", \"free zone tax\", \"qualifying free zone person\", \"AED 375,000\", \"9% tax\", \"taxable income UAE\", \"corporate tax registration\", \"UAE tax return\", \"self-employed tax UAE\", \"freelancer tax Dubai\", \"EmaraTax\", or any question about computing or filing UAE corporate tax. This skill covers the 0%/9% rate structure, small business relief (revenue not exceeding AED 3M), qualifying free zone person rules, deductible and non-deductible expenses, transfer pricing, registration requirements, and filing deadlines. Wages are outside Corporate Tax; natural-person business scope has a turnover test. ALWAYS read this skill before touching any UAE corporate tax work."
version: 2.6
category: IT-CORP
jurisdiction: AE
tax_year: 2026
last_updated: 2026-11-26
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
---

# UAE Corporate Tax: 2026 computation, relief and filing

## Scope

Use this Guide to compute federal Corporate Tax for an ordinary UAE business for its 2026 tax period. A free-zone or specialist case needs the determinations identified below before a calculation is usable. VAT, excise and Emirate-level taxes require separate guidance.

UAE-incorporated or established juridical persons, including Free Zone Persons, and foreign juridical persons effectively managed and controlled in the UAE are Resident Persons under Article 11(3). The natural-person turnover threshold does not apply to them. Establish whether an Article 4 exemption applies before computing tax; exemption determinations are referred below. ([Corporate Tax Law](https://mof.gov.ae/wp-content/uploads/2026/01/Federal-Decree-Law-No.-47-of-2022-and-its-amendments-en-v13.1.26.pdf)).

A resident juridical person's base includes UAE and foreign taxable income. A resident natural person's base includes UAE and foreign income insofar as it relates to the Business conducted in the UAE (Article 12). ([Corporate Tax Law](https://mof.gov.ae/wp-content/uploads/2026/01/Federal-Decree-Law-No.-47-of-2022-and-its-amendments-en-v13.1.26.pdf)).

A natural person's UAE Business is subject to Corporate Tax only if total Business Turnover exceeds AED 1,000,000 within a Gregorian calendar year. At or below the threshold, with no other taxable Business, no Corporate Tax registration is required (Decision 49/2023, Article 2). ([Decision 49/2023](https://tax.gov.ae/DataFolder/Files/Legislation/05-06-2023/3/Cabinet%20Decision%20No.%2049%20of%202023%20-%20for%20publishing.pdf)).

Wages, Personal Investment income and Real Estate Investment income within Decision 49/2023's definitions are excluded regardless of amount. Personal Investment must be for the person's own account, neither conducted through nor requiring a UAE licence, and not a commercial business under the Commercial Transactions Law. Real Estate Investment covers investment sale, leasing, sub-leasing or renting of UAE land/property not conducted, or not required to be conducted, through a licence. Merely lacking a licence does not establish the exclusion where one is required. ([Decision 49/2023](https://tax.gov.ae/DataFolder/Files/Legislation/05-06-2023/3/Cabinet%20Decision%20No.%2049%20of%202023%20-%20for%20publishing.pdf)).

## Ask the client first

Obtain the legal structure, residence and exemption evidence; financial year and first tax period; registration and filed returns; current and all previous tax-period revenue; Business Turnover for a natural person; group membership; free-zone activities, customers, substance, accounts and elections; accounting adjustments, mixed-use costs and connected-person payments; loss origin and ownership history; interest, financing purpose and tax-adjusted EBITDA; and available credits. Retrieve existing records before requesting missing facts. Do not infer eligibility from revenue or arithmetic alone.

## The method, step by step

### Period and rates

The tax period is the Financial Year or part for which a return is required. The Financial Year is the Gregorian calendar year or the twelve-month financial-statement period. A different period or change of dates requires an application subject to the FTA's conditions (Articles 57-58). ([Corporate Tax Law](https://mof.gov.ae/wp-content/uploads/2026/01/Federal-Decree-Law-No.-47-of-2022-and-its-amendments-en-v13.1.26.pdf)).

| Person / base | Rate | Official source |
|---|---|---|
| Ordinary Taxable Person: portion of taxable income not exceeding AED 375,000 per tax period | 0% | https://tax.gov.ae/Datafolder/Files/Legislation/Corporate%20Tax/Cabinet%20Decision%20No.%20116%20of%202022%20-%20for%20publishing.pdf |
| Ordinary Taxable Person: portion exceeding AED 375,000 | 9% | https://tax.gov.ae/Datafolder/Files/Legislation/Corporate%20Tax/Cabinet%20Decision%20No.%20116%20of%202022%20-%20for%20publishing.pdf |
| QFZP: Qualifying Income, once every qualification condition is established | 0% | https://mof.gov.ae/wp-content/uploads/2026/01/Federal-Decree-Law-No.-47-of-2022-and-its-amendments-en-v13.1.26.pdf |
| QFZP: taxable income that is not Qualifying Income; no ordinary income band | 9% | https://mof.gov.ae/wp-content/uploads/2026/01/Federal-Decree-Law-No.-47-of-2022-and-its-amendments-en-v13.1.26.pdf |

The ordinary band is available once per Taxable Person per period, across all its Businesses. Artificial separation producing an excess zero-rated band is subject to the anti-abuse rule; the FTA considers commercial purpose and the financial, economic and regulatory ties (Decision 116/2022, Article 2). ([Decision 116/2022](https://tax.gov.ae/Datafolder/Files/Legislation/Corporate%20Tax/Cabinet%20Decision%20No.%20116%20of%202022%20-%20for%20publishing.pdf)).

### Small Business Relief

Revenue is gross income under accepted accounting standards, not profit; measure it at arm's length. The relevant and every previous tax period must each have revenue no greater than AED 3,000,000. A breach in any relevant or earlier period prevents an election even if revenue later falls (MD 73/2023, Article 2). ([MD 73/2023](https://tax.gov.ae/Datafolder/Files/Legislation/Corporate%20Tax/Ministerial%20Decision%20No.%2073%20of%202023%20-%20for%20publishing.pdf); [Small Business Relief Guide](https://tax.gov.ae/Datafolder/Files/Guides/CT/Small%20Business%20Relief%20Guide%20-%20EN%20-%2029%2008%202023.pdf)).

The relief window starts with periods commencing on or after 1 June 2023 and extends to periods ending on or before 31 December 2029. MD 131/2026 replaces the original end date of 31 December 2026. This extension does not change eligibility for a period ending in 2025; it does not change the revenue-history test. ([MD 131/2026](https://mof.gov.ae/wp-content/uploads/2026/08/Ministerial-Decision-No.-131-of-2026-Amending-Certain-Provisions-of-Ministerial-Decision-No.-73-of-2023-on-Small-Business-Relief-for-the-Purposes-of-Federal-Decree-Law-No.-47-of-2022-EN.pdf)).

Only a Resident Taxable Person can elect, for each period, through its return. A QFZP or Constituent Company of an MNE Group as defined in Cabinet Decision 44/2020 cannot elect. Do not substitute the transfer-pricing file threshold for that definition; unresolved group classification is referred below. Once all conditions and the election are established, the person is treated as having no taxable income. ([Corporate Tax Law](https://mof.gov.ae/wp-content/uploads/2026/01/Federal-Decree-Law-No.-47-of-2022-and-its-amendments-en-v13.1.26.pdf); [MD 73/2023](https://tax.gov.ae/Datafolder/Files/Legislation/Corporate%20Tax/Ministerial%20Decision%20No.%2073%20of%202023%20-%20for%20publishing.pdf); [Small Business Relief Guide](https://tax.gov.ae/Datafolder/Files/Guides/CT/Small%20Business%20Relief%20Guide%20-%20EN%20-%2029%2008%202023.pdf)).

In an elected relief period, the statutory exempt-income, relief, deduction, tax-loss and Article 55 documentation provisions do not apply. This does not switch off arm's-length revenue measurement. ([Corporate Tax Law](https://mof.gov.ae/wp-content/uploads/2026/01/Federal-Decree-Law-No.-47-of-2022-and-its-amendments-en-v13.1.26.pdf); [Small Business Relief Guide](https://tax.gov.ae/Datafolder/Files/Guides/CT/Small%20Business%20Relief%20Guide%20-%20EN%20-%2029%2008%202023.pdf)).

Losses incurred in a relief period cannot carry forward. Unused eligible losses from earlier non-relief periods can survive for later non-relief periods, subject to Article 37; they cannot be used in the relief period (MD 73/2023, Article 4). ([MD 73/2023](https://tax.gov.ae/Datafolder/Files/Legislation/Corporate%20Tax/Ministerial%20Decision%20No.%2073%20of%202023%20-%20for%20publishing.pdf)).

Net Interest Expenditure incurred in a relief period cannot carry forward. Earlier eligible disallowed interest can survive for later non-relief periods, subject to Article 30 (MD 73/2023, Article 5). ([MD 73/2023](https://tax.gov.ae/Datafolder/Files/Legislation/Corporate%20Tax/Ministerial%20Decision%20No.%2073%20of%202023%20-%20for%20publishing.pdf)).

Where the FTA establishes artificial separation, combined revenue exceeds the threshold, and relief was elected, the arrangement falls under Article 50. The FTA considers valid commercial purpose and financial, economic and organisational links (MD 73/2023, Article 6). ([MD 73/2023](https://tax.gov.ae/Datafolder/Files/Legislation/Corporate%20Tax/Ministerial%20Decision%20No.%2073%20of%202023%20-%20for%20publishing.pdf)).

### Accounting income and deductions

Without a relief election, start with standalone accounting income under accepted standards, then adjust for exempt income, reliefs, deductions, related-party/connected-person transactions, losses and other statutory adjustments (Article 20). Detailed accounting-standard/cash-basis elections, exemptions and incentives are referred below; do not deduct an exemption merely because an item is called a dividend. ([Corporate Tax Law](https://mof.gov.ae/wp-content/uploads/2026/01/Federal-Decree-Law-No.-47-of-2022-and-its-amendments-en-v13.1.26.pdf)).

Non-capital expenditure wholly and exclusively for Business is deductible when incurred, subject to the law. Exclude personal expenditure, exempt-income expenditure and unrelated losses. For mixed expenditure, identify the taxable-Business portion or apportion the unidentifiable portion fairly and reasonably (Article 28). ([Corporate Tax Law](https://mof.gov.ae/wp-content/uploads/2026/01/Federal-Decree-Law-No.-47-of-2022-and-its-amendments-en-v13.1.26.pdf)).

Subject to Article 28, customer, shareholder, supplier and other Business-partner entertainment is 50% deductible, including meals, accommodation, transport, admission and entertainment facilities (Article 32). ([Corporate Tax Law](https://mof.gov.ae/wp-content/uploads/2026/01/Federal-Decree-Law-No.-47-of-2022-and-its-amendments-en-v13.1.26.pdf)).

Add back any amounts already deducted for donations/grants/gifts to an entity that is not a Qualifying Public Benefit Entity; fines and penalties other than damages/breach-of-contract compensation; bribes/illicit payments; owner dividends/profit distributions; natural-person or unincorporated-partner drawings; Corporate Tax; foreign income tax; and recoverable input VAT (Article 33). ([Corporate Tax Law](https://mof.gov.ae/wp-content/uploads/2026/01/Federal-Decree-Law-No.-47-of-2022-and-its-amendments-en-v13.1.26.pdf)).

### Interest

Net Interest Expenditure includes current interest plus carried-forward disallowed net interest, less taxable interest income; interest disallowed under other rules is excluded. Article 30's general limit does not apply to banks, insurance providers, natural persons undertaking Business, or any other prescribed excluded Person. Resolve Article 31 and MD 126/2023 historical-liability/infrastructure exclusions before using the general limit; their detailed application is referred below. ([Corporate Tax Law](https://mof.gov.ae/wp-content/uploads/2026/01/Federal-Decree-Law-No.-47-of-2022-and-its-amendments-en-v13.1.26.pdf); [MD 126/2023](https://tax.gov.ae/Datafolder/Files/Pdf/2023/Ministerial%20Decision%20No.%20126%20of%202023%20on%20the%20General%20Interest%20Deduction%20Limitation%20Rule%20-%20for%20publishing.pdf)).

For an in-scope twelve-month period, eligible Net Interest Expenditure not exceeding AED 12,000,000 is outside the general cap. Above that amount, deduct the higher of AED 12,000,000 and 30% of statutory tax-adjusted EBITDA, excluding exempt income. Pro-rate the monetary amount for periods longer or shorter than twelve months (MD 126/2023, Articles 8-9). ([Corporate Tax Law](https://mof.gov.ae/wp-content/uploads/2026/01/Federal-Decree-Law-No.-47-of-2022-and-its-amendments-en-v13.1.26.pdf); [MD 126/2023](https://tax.gov.ae/Datafolder/Files/Pdf/2023/Ministerial%20Decision%20No.%20126%20of%202023%20on%20the%20General%20Interest%20Deduction%20Limitation%20Rule%20-%20for%20publishing.pdf)).

The general-limit excess carries for the subsequent ten tax periods, oldest first, subject to each later period's limits (Article 30(4)). ([Corporate Tax Law](https://mof.gov.ae/wp-content/uploads/2026/01/Federal-Decree-Law-No.-47-of-2022-and-its-amendments-en-v13.1.26.pdf)).

Article 31 separately denies related-party loan interest funding related-party dividends, share-capital returns, capital contributions or acquisition of a related-party ownership interest unless the taxpayer demonstrates that the main purpose of the loan and transaction is not a Corporate Tax advantage. No advantage is deemed where the lender's interest is subject to Corporate Tax or similar foreign tax at not less than 9%. ([Corporate Tax Law](https://mof.gov.ae/wp-content/uploads/2026/01/Federal-Decree-Law-No.-47-of-2022-and-its-amendments-en-v13.1.26.pdf)).

### Related parties, losses and credits

Related-party transactions must satisfy the arm's-length standard. Article 34 lists comparable uncontrolled price, resale price, cost-plus, transactional net margin and transactional profit split methods; an alternative needs a demonstration that none can reasonably be applied. Detailed related-party/control identification, method selection and documentation are referred below. ([Corporate Tax Law](https://mof.gov.ae/wp-content/uploads/2026/01/Federal-Decree-Law-No.-47-of-2022-and-its-amendments-en-v13.1.26.pdf)).

Connected-person payments are limited to Market Value and wholly/exclusively Business use, without prejudice to Article 28. Article 36(6) excepts recognised-stock-exchange traded taxpayers, taxpayers under competent UAE regulatory oversight, and any Cabinet-prescribed Person from Clause 1. Ordinary deductions and Article 34 where separately applicable still need review. Owners, directors/officers, their Related Parties and the specified partnership connections require screening. ([Corporate Tax Law](https://mof.gov.ae/wp-content/uploads/2026/01/Federal-Decree-Law-No.-47-of-2022-and-its-amendments-en-v13.1.26.pdf)).

Eligible tax losses can carry forward without a fixed expiry; the total offset is capped at 75% of taxable income before loss relief. ([Corporate Tax Law](https://mof.gov.ae/wp-content/uploads/2026/01/Federal-Decree-Law-No.-47-of-2022-and-its-amendments-en-v13.1.26.pdf); [FTA losses bulletin](https://tax.gov.ae/Datafolder/Files/Pdf/2026/CT-Tax-Bulletin-Corporate-Tax-Losses-EN.pdf)).

Use oldest losses first and to the fullest permitted extent; use own losses before transferred losses. Do not elect a smaller use merely to preserve more losses. ([Corporate Tax Law](https://mof.gov.ae/wp-content/uploads/2026/01/Federal-Decree-Law-No.-47-of-2022-and-its-amendments-en-v13.1.26.pdf); [FTA losses bulletin](https://tax.gov.ae/Datafolder/Files/Pdf/2026/CT-Tax-Bulletin-Corporate-Tax-Losses-EN.pdf)).

Losses before Corporate Tax commencement, before becoming taxable, or from exempt or otherwise disregarded assets/activities are ineligible (Article 37(3)). ([Corporate Tax Law](https://mof.gov.ae/wp-content/uploads/2026/01/Federal-Decree-Law-No.-47-of-2022-and-its-amendments-en-v13.1.26.pdf)).

Check ownership continuously from the beginning of the loss period to the end of utilisation. Where ownership changes by more than 50%, the same/similar Business condition applies; examine assets, core operations and development of pre-existing activities. Article 39(1)'s limitation does not apply to recognised-stock-exchange listed taxpayers. Unresolved ownership or Business continuity prevents use of the loss. ([Corporate Tax Law](https://mof.gov.ae/wp-content/uploads/2026/01/Federal-Decree-Law-No.-47-of-2022-and-its-amendments-en-v13.1.26.pdf); [FTA losses bulletin](https://tax.gov.ae/Datafolder/Files/Pdf/2026/CT-Tax-Bulletin-Corporate-Tax-Losses-EN.pdf)).

Settle tax in Article 44 order: available withholding credit, then available foreign credit, then applicable Cabinet-prescribed incentive/relief credits, then payment. Other credits require separate substantiation. ([Corporate Tax Law](https://mof.gov.ae/wp-content/uploads/2026/01/Federal-Decree-Law-No.-47-of-2022-and-its-amendments-en-v13.1.26.pdf)).

Foreign tax credit cannot exceed UAE Corporate Tax on the relevant income, cannot carry forward or back, and requires supporting records (Article 47). ([Corporate Tax Law](https://mof.gov.ae/wp-content/uploads/2026/01/Federal-Decree-Law-No.-47-of-2022-and-its-amendments-en-v13.1.26.pdf)).

### Free-zone screen

A QFZP must satisfy every Article 18 condition: adequate substance, Qualifying Income, no election to ordinary rates, and compliance with Articles 34 and 55, plus ministerial conditions including audited accounts and de minimis. A free-zone licence alone proves none of these. Detailed income/activity, beneficial-recipient, substance/outsourcing, election and distribution-report determinations are referred below. ([Corporate Tax Law](https://mof.gov.ae/wp-content/uploads/2026/01/Federal-Decree-Law-No.-47-of-2022-and-its-amendments-en-v13.1.26.pdf); [MD 229/2025](https://tax.gov.ae/Datafolder/Files/Pdf/2025/MD-No-229.pdf)).

Non-qualifying revenue must not exceed the lower of 5% of total revenue and AED 5,000,000 per period; equality passes (MD 229/2025, Article 3). ([MD 229/2025](https://tax.gov.ae/Datafolder/Files/Pdf/2025/MD-No-229.pdf)).

Before that test, exclude from both numerator and denominator the Article 4(3) categories: free-zone commercial-property transactions with Non-Free Zone Persons; free-zone non-commercial-property transactions with anyone; domestic/foreign permanent-establishment revenue; and intellectual-property revenue except revenue related to Article 7(1) Qualifying Income. Treat the establishment separately at arm's length. Unresolved attribution prevents using the percentage. ([Decision 100/2023](https://tax.gov.ae/Datafolder/Files/Legislation/Cabinet%20Decision%20No.%20100%20of%202023%20on%20Determining%20Qualifying%20Income%20for%20the%20Qualifying%20Free%20Zone%20Person%20-%20for%20publishing.pdf)).

Even for a QFZP, domestic/foreign permanent-establishment income, the specified free-zone property income, and non-qualifying/excess intellectual-property income under Articles 5-7 are taxed at 9%, without the ordinary band. Do not describe all property income as having identical treatment. ([Decision 100/2023](https://tax.gov.ae/Datafolder/Files/Legislation/Cabinet%20Decision%20No.%20100%20of%202023%20on%20Determining%20Qualifying%20Income%20for%20the%20Qualifying%20Free%20Zone%20Person%20-%20for%20publishing.pdf); [Corporate Tax Law](https://mof.gov.ae/wp-content/uploads/2026/01/Federal-Decree-Law-No.-47-of-2022-and-its-amendments-en-v13.1.26.pdf)).

Failure of a qualification condition removes QFZP status from the start of that period and the four subsequent periods (MD 229/2025, Article 5). ([MD 229/2025](https://tax.gov.ae/Datafolder/Files/Pdf/2025/MD-No-229.pdf)).

## Boundary and exception table

| Boundary | Result | Official source |
|---|---|---|
| Natural-person Business Turnover exactly AED 1,000,000 | Does not exceed the entry threshold | https://tax.gov.ae/DataFolder/Files/Legislation/05-06-2023/3/Cabinet%20Decision%20No.%2049%20of%202023%20-%20for%20publishing.pdf |
| Ordinary taxable income exactly AED 375,000 | Within the 0% portion | https://tax.gov.ae/Datafolder/Files/Legislation/Corporate%20Tax/Cabinet%20Decision%20No.%20116%20of%202022%20-%20for%20publishing.pdf |
| Revenue exactly AED 3,000,000 | Passes only the revenue limb of Small Business Relief; all other conditions and election remain necessary | https://tax.gov.ae/Datafolder/Files/Legislation/Corporate%20Tax/Ministerial%20Decision%20No.%2073%20of%202023%20-%20for%20publishing.pdf |
| Small Business Relief with a QFZP | Excluded | https://tax.gov.ae/Datafolder/Files/Legislation/Corporate%20Tax/Ministerial%20Decision%20No.%2073%20of%202023%20-%20for%20publishing.pdf |
| Net Interest Expenditure exactly AED 12,000,000 in a twelve-month period | No general cap; specific disallowances and eligibility still apply | https://tax.gov.ae/Datafolder/Files/Pdf/2023/Ministerial%20Decision%20No.%20126%20of%202023%20on%20the%20General%20Interest%20Deduction%20Limitation%20Rule%20-%20for%20publishing.pdf |

## Worked cases

These preserve the original amounts and years. Calendar-year periods apply unless stated. Computations assume ordinary taxable status, no unmentioned adjustments/credits and all stated eligibility conditions; a missing condition makes the result non-usable pending the referral.

1. **Freelance consultant, Small Business Relief.**
   - **Facts:** a UAE-resident Dubai mainland sole establishment owner, whose first Business tax period was 2024, had business revenue of AED 1,400,000 in 2024; in 2025 it was AED 2,600,000 and in 2026 it was AED 2,900,000. Turnover passed AED 1,000,000 in 2024, so she was a Taxable Person and had to register by 31 March 2025.
   - **Relief:** revenue has been AED 3,000,000 or less in 2026 and in every earlier period, the 2026 period ends before 31 December 2029, and she is not in a multinational group. Assume she is not a QFZP and no artificial separation exists. So she can elect Small Business Relief on her 2026 return, due 30 September 2027. Taxable income is treated as nil and the tax is nil.
   - **If she forgets to elect:** with taxable income of AED 900,000, tax is (AED 900,000 − AED 375,000) × 9% = AED 47,250 ([Cabinet Decision No. 116 of 2022](https://tax.gov.ae/Datafolder/Files/Legislation/Corporate%20Tax/Cabinet%20Decision%20No.%20116%20of%202022%20-%20for%20publishing.pdf)).
2. **Relief lost for good; standard computation.**
   - **Facts:** an Abu Dhabi engineering LLC had revenue of AED 3,200,000 in 2025 and AED 4,200,000 in 2026. Its 2026 taxable income after all adjustments is AED 2,380,000.
   - **Tax:** (AED 2,380,000 − AED 375,000) × 9% = AED 180,450.
   - **Relief:** if revenue fell to AED 2,400,000 in 2027, Small Business Relief would still not be available, because 2025 revenue exceeded the threshold ([Ministerial Decision No. 73 of 2023](https://tax.gov.ae/Datafolder/Files/Legislation/Corporate%20Tax/Ministerial%20Decision%20No.%2073%20of%202023%20-%20for%20publishing.pdf)).
3. **Loss cap and entertainment.**
   - **Add-backs:** a company's 2026 accounting profit is AED 800,000. It includes AED 60,000 of client entertainment and an AED 5,000 traffic fine. Add back 50% of the entertainment (AED 30,000) and the whole fine: AED 800,000 + AED 30,000 + AED 5,000 = AED 835,000.
   - **Loss cap:** assume its AED 700,000 carried-forward Tax Losses from 2024 and 2025 are eligible under Articles 37-39, with all applicable eligibility, ownership-continuity and Business-activity conditions resolved. The cap is AED 835,000 × 75% = AED 626,250. Taxable income becomes AED 835,000 − AED 626,250 = AED 208,750, which falls inside the AED 375,000 0% band, so the tax is nil. The remaining AED 73,750 of losses carries forward.
   - **If it had elected Small Business Relief instead:** had all Small Business Relief conditions and the election been satisfied for 2026, none of the AED 700,000 could be used in 2026, but all of it would survive for later non-relief years ([FTA losses bulletin](https://tax.gov.ae/Datafolder/Files/Pdf/2026/CT-Tax-Bulletin-Corporate-Tax-Losses-EN.pdf)).
4. **Interest limitation.**
   - **Facts:** assume an in-scope juridical property developer for a twelve-month period, outside Article 30(6) exclusions, with Article 31 specific-interest checks resolved. Its AED 20,000,000 is eligible Net Interest Expenditure after the historical-financial-liability and qualifying-infrastructure checks in Ministerial Decision 126/2023 Articles 11 and 14; no unresolved exclusion is included in that amount. Tax-adjusted EBITDA is AED 50,000,000.
   - **Limit:** 30% of EBITDA is AED 50,000,000 × 30% = AED 15,000,000, which is higher than AED 12,000,000, so AED 15,000,000 is deductible. The other AED 5,000,000 carries forward for up to 10 periods subject to the applicable later-period limitations and ordering rules ([Ministerial Decision No. 126 of 2023](https://tax.gov.ae/Datafolder/Files/Pdf/2023/Ministerial%20Decision%20No.%20126%20of%202023%20on%20the%20General%20Interest%20Deduction%20Limitation%20Rule%20-%20for%20publishing.pdf)).
5. **QFZP that passes de minimis, with a mainland branch.**
   - **De minimis test:** a free zone distributor has revenue of AED 20,000,000 after every Article 4(3) exclusion described above, with mainland-branch revenue excluded. Assume no further excluded property or intellectual-property revenue; a specialist has confirmed activity/customer classification and all substance, audit, documentation and distribution-report requirements; and no election out applies. Of that adjusted revenue, AED 800,000 is non-qualifying sales to individuals; the rest is qualifying distribution revenue. The de minimis limit is the lower of AED 20,000,000 × 5% = AED 1,000,000 and AED 5,000,000, so it is AED 1,000,000. AED 800,000 does not exceed it, so the test is met. If it meets the other conditions, its qualifying income is taxed at 0%.
   - **Branch:** the branch's AED 500,000 of taxable income is taxed at 9% with no AED 375,000 band: AED 500,000 × 9% = AED 45,000.
   - **If the test had failed:** holding the adjusted total revenue constant at AED 20,000,000, had sales to individuals been AED 1,200,000, it would fail and be taxed at the standard rates for 2026 and the four following periods ([MD 229/2025](https://tax.gov.ae/Datafolder/Files/Pdf/2025/MD-No-229.pdf)).
6. **Free zone software house selling to the mainland.**
   - **Facts:** a free zone software company earns AED 5,000,000, all from mainland companies.
   - **Outcome:** the mainland customer label alone does not establish income classification. Check this point with one of our partner accountants. If a specialist establishes that all AED 5,000,000 is non-qualifying ordinary development-service revenue, with no qualifying intellectual-property or other qualifying income, and no denominator exclusions, the computed de minimis limit is min(AED 5,000,000 × 5%, AED 5,000,000) = AED 250,000. That assumed non-qualifying revenue fails the test. Ordinary rates then apply to taxable income, which the facts do not supply; revenue is not taxable profit.
7. **Late registration waived.**
   - **Facts:** an ordinary UAE-incorporated taxable company incorporated on 10 February 2026 with its first tax period ending 31 December 2026 had to register within 3 months, by 10 May 2026. It registered in August 2026, so the AED 10,000 late registration penalty applies.
   - **Waiver:** if it files its first return (period ending 31 December 2026) within 7 months, by 31 July 2027, the FTA waives the penalty, or refunds it to the EmaraTax account if it was paid. The tax itself is still due within 9 months, by 30 September 2027 ([CTP006](https://tax.gov.ae/Datafolder/Files/Pdf/2025/CTP006-Waiver-of-Late-Registration-Administrative-Penalty-02-07-2025.pdf)).
8. **Freelancer below the threshold, and a salaried landlord.**
   - **Freelancer:** a UAE-resident natural-person freelance designer with no other Business and AED 750,000 of business turnover in 2026 is not subject to Corporate Tax and does not register. Monitor turnover, because once it exceeds AED 1,000,000 in a calendar year she must register by 31 March of the next year.
   - **Salaried landlord:** an employee owns two UAE flats and rents them out personally, with no other Business. Assume the rental activity neither operates through nor requires a licence. The wages and that rental income create no Corporate Tax liability or registration obligation. Wages and real estate investment income are not business income ([Cabinet Decision No. 49 of 2023](https://tax.gov.ae/DataFolder/Files/Legislation/05-06-2023/3/Cabinet%20Decision%20No.%2049%20of%202023%20-%20for%20publishing.pdf)).
9. **Late return and late payment.**
   - **Facts:** the return for the year ended 31 December 2025 was due 30 September 2026 but was filed, with AED 100,000 of tax paid, on 15 December 2026.
   - **Late filing:** AED 500 is charged on 1 October, 1 November and 1 December: 3 × AED 500 = AED 1,500.
   - **Late payment:** 14% a year, charged monthly for each month or part, on the unpaid tax. For an ordinary self-assessed return with the full tax unsettled until payment, the calculation is AED 100,000 × 14% ÷ 12 × 3 = AED 3,500. Reconcile the assessment in EmaraTax; voluntary-disclosure and tax-assessment payment clocks need separate treatment ([Cabinet Decision No. 75 of 2023](https://tax.gov.ae/Datafolder/Files/Legislation/Cabinet%20Decision%20No.%2075%20of%202023%20and%20amendments%20-%20For%20Publishing.pdf)).

```oa-check
name: Elect eligible Small Business Relief or use standard rates, Case 1 (2026)
inputs:
  taxable_income: 900000
  band: 375000
  rate: 0.09
steps:
  - tax_without_election: max(taxable_income - band, 0) * rate
  - tax_with_eligible_election: 0
  - tax_saved: tax_without_election - tax_with_eligible_election
expected:
  tax_without_election: 47250.00
  tax_with_eligible_election: 0.00
  tax_saved: 47250.00
```

```oa-check
name: Relief lost, standard computation, Case 2 (2026)
inputs:
  taxable_income: 2380000
  band: 375000
  rate: 0.09
steps:
  - tax: (taxable_income - band) * rate
expected:
  tax: 180450.00
```

```oa-check
name: Late return and late payment, Case 9
inputs:
  months_late: 3
  tax_unpaid: 100000
  filing_penalty: 500
  annual_rate: 0.14
steps:
  - late_filing: months_late * filing_penalty
  - late_payment: tax_unpaid * annual_rate / 12 * months_late
expected:
  late_filing: 1500.00
  late_payment: 3500.00
```

```oa-check
name: Cases 3 to 6 conditional arithmetic
inputs:
  profit: 800000
  entertainment: 60000
  fine: 5000
  losses: 700000
  net_interest: 20000000
  ebitda: 50000000
  adjusted_revenue: 20000000
  branch_income: 500000
  software_revenue: 5000000
steps:
  - adjusted_income: profit + entertainment * 0.5 + fine
  - loss_used: min(losses, adjusted_income * 0.75)
  - after_losses: adjusted_income - loss_used
  - losses_remaining: losses - loss_used
  - income_tax: max(after_losses - 375000, 0) * 0.09
  - interest_limit: max(12000000, ebitda * 0.3)
  - interest_carry: net_interest - interest_limit
  - distributor_limit: min(adjusted_revenue * 0.05, 5000000)
  - passing_margin: distributor_limit - 800000
  - failing_excess: 1200000 - distributor_limit
  - branch_tax: branch_income * 0.09
  - software_limit: min(software_revenue * 0.05, 5000000)
  - software_excess: software_revenue - software_limit
expected:
  adjusted_income: 835000
  loss_used: 626250
  after_losses: 208750
  losses_remaining: 73750
  income_tax: 0
  interest_limit: 15000000
  interest_carry: 5000000
  distributor_limit: 1000000
  passing_margin: 200000
  failing_excess: 200000
  branch_tax: 45000
  software_limit: 250000
  software_excess: 4750000
```

## When to refuse or refer

- Free-zone classification and implementation: Qualifying Income and beneficial recipients; all qualifying/excluded activities, including manufacturing/processing, commodities, investment securities, ships, reinsurance, funds/wealth management, headquarters, treasury/financing, aircraft, designated-zone distribution, logistics and ancillary activities; natural-person sales, banking, insurance/captive insurance, leasing and property; substance and outsourcing; intellectual-property nexus; election timing/duration; distributor agreed-upon procedures under FTA Decision 6/2026. Check this point with one of our partner accountants. The screen and arithmetic above do not determine these matters.
- Special status and relief: exemptions and their applications under FTA Decision 15/2026; government/public-benefit/investment/pension/resource businesses; unincorporated partnerships and family foundations; tax groups, loss transfers, qualifying-group transfers, restructuring and participation exemption; accounting standards/cash basis under MD 114/2023, historical-debt/infrastructure interest exclusions, R&D incentives/other credits; non-resident permanent establishment/nexus, effective-management, withholding and treaty questions; older/foreign/non-resident registration timelines and unresolved Small Business Relief MNE classification under Decision 44/2020. Check this point with one of our partner accountants.
- Transfer-pricing execution: related-party/control and connected-person identification, domestic/cross-border analysis, disclosure thresholds/categories/exceptions, master/local file inclusion/exclusions, document requests, method selection and advance pricing agreements. Check this point with one of our partner accountants.
- Domestic minimum top-up tax: scope, excluded entities, revenue-history/short-year and transition tests, effective dates, registration, GloBE computation, safe harbours, tax return and Pillar Two information-return deadlines and later implementation. Check this point with one of our partner accountants. Do not use ordinary Corporate Tax deadlines for this separate regime.
- Procedures and other penalties: incorrect returns, voluntary disclosures and non-disclosure before audit, tax assessments, record failures, deregistration, tax-record updates, reconsiderations and unfiled past periods; detailed records-content rules under FTA Decision 4/2026. Check this point with one of our partner accountants.

## Filing and payment

Subject to statutory registration exceptions, Taxable Persons must register for Corporate Tax, including those intending Small Business Relief. A separate Corporate Tax registration is needed. UAE-incorporated/established/recognised juridical persons, including Free Zone Persons, formed on or after 1 March 2024 apply within three months of incorporation/establishment/recognition (Article 51 and FTA Decision 3/2024, Article 3(3)). ([Corporate Tax Law](https://mof.gov.ae/wp-content/uploads/2026/01/Federal-Decree-Law-No.-47-of-2022-and-its-amendments-en-v13.1.26.pdf); [FTA Decision 3/2024](https://tax.gov.ae/Datafolder/Files/Legislation/RE%20FTA%20Decision%20No.%203%20of%202024%20on%20Registration%20Timeline%20for%20Corporate%20Tax%20%20-%20For%20publishing.pdf)).

A Resident natural person whose total Business Turnover exceeds AED 1,000,000 in calendar year 2024 or a later year applies by 31 March of the following year (FTA Decision 3/2024, Article 5). Other registration categories are referred above. ([FTA Decision 3/2024](https://tax.gov.ae/Datafolder/Files/Legislation/RE%20FTA%20Decision%20No.%203%20of%202024%20on%20Registration%20Timeline%20for%20Corporate%20Tax%20%20-%20For%20publishing.pdf); [Decision 49/2023](https://tax.gov.ae/DataFolder/Files/Legislation/05-06-2023/3/Cabinet%20Decision%20No.%2049%20of%202023%20-%20for%20publishing.pdf)).

File the Corporate Tax Return in EmaraTax and pay within nine months after period end, unless the FTA directs another date (Articles 48 and 53). Elect Small Business Relief in the relevant return; retain the submission receipt, computation and payment confirmation. As computed by adding nine months: period ends 31 March, 30 June, 30 September and 31 December 2026 give ordinary deadlines 31 December 2026, 31 March, 30 June and 30 September 2027 respectively. For earlier period ends 31 March, 30 June and 31 December 2025, the ordinary deadlines were 31 December 2025, 31 March and 30 September 2026. ([Corporate Tax Law](https://mof.gov.ae/wp-content/uploads/2026/01/Federal-Decree-Law-No.-47-of-2022-and-its-amendments-en-v13.1.26.pdf)).

For periods commencing on or after 1 January 2025, a non-Tax-Group Taxable Person with revenue exceeding AED 50,000,000, and every QFZP, must prepare and maintain audited financial statements (MD 84/2025, Articles 2-4). Other categories and distributor procedures need separate determination. ([MD 84/2025](https://tax.gov.ae/Datafolder/Files/Pdf/2025/MD-No-84-of-2025.pdf)).

Keep records supporting the return and readily establishing taxable income for seven years after the relevant period ends (Article 56). ([Corporate Tax Law](https://mof.gov.ae/wp-content/uploads/2026/01/Federal-Decree-Law-No.-47-of-2022-and-its-amendments-en-v13.1.26.pdf)).

Late registration attracts AED 10,000 (Decision 75/2023, item 14, as amended). ([Decision 75/2023](https://tax.gov.ae/Datafolder/Files/Legislation/Cabinet%20Decision%20No.%2075%20of%202023%20and%20amendments%20-%20For%20Publishing.pdf)).

The first-period late-registration waiver requires the Taxable Person's first return within seven months after its first tax period ends. It applies to past or future first periods only; an already-paid penalty is credited to the EmaraTax account. The ordinary tax payment deadline remains nine months (CTP006). ([CTP006](https://tax.gov.ae/Datafolder/Files/Pdf/2025/CTP006-Waiver-of-Late-Registration-Administrative-Penalty-02-07-2025.pdf)).

A registrant's late-return penalty is AED 500 for each month or part for the first twelve months, then AED 1,000 from month thirteen. It starts the day after the deadline and repeats on the same date monthly (Decision 75/2023, item 7). ([Decision 75/2023](https://tax.gov.ae/Datafolder/Files/Legislation/Cabinet%20Decision%20No.%2075%20of%202023%20and%20amendments%20-%20For%20Publishing.pdf)).

Unpaid tax attracts a monthly penalty at 14% per annum for each month or part on the unsettled amount, starting the day after payment is due and recurring monthly. Voluntary disclosures and tax assessments have separate payment-due-date rules; refer these procedures above (Decision 75/2023, item 8). ([Decision 75/2023](https://tax.gov.ae/Datafolder/Files/Legislation/Cabinet%20Decision%20No.%2075%20of%202023%20and%20amendments%20-%20For%20Publishing.pdf)).

## Completion checklist

- [ ] Structure, residence, period and exemption status evidenced.
- [ ] Registration, relief conditions/election and any free-zone determinations documented.
- [ ] Accounting adjustments, related/connected-person transactions, interest and eligible losses reconciled.
- [ ] Rates, credits, return, payment and records checked; retain confirmations.
- [ ] Every unresolved specialist point above held for a partner accountant before using its result.

## Sources

Existing completed official-source reads and their independent review are reused within their stated scope. The following authority-hosted English texts (some labelled unofficial translations) were re-opened in memory on 26 November 2026; their PDF fingerprints match the previously recorded captures. The table states the operative sections applied; it does not claim every page of a long guide was re-read.

| Source / scope applied | Official URL | Date read |
|---|---|---|
| Decision 49/2023, definitions and Article 2 | https://tax.gov.ae/DataFolder/Files/Legislation/05-06-2023/3/Cabinet%20Decision%20No.%2049%20of%202023%20-%20for%20publishing.pdf | 2026-11-26, read: Decision 49/2023, definitions and Article 2 |
| MD 73/2023, Articles 2-6, with S10 amendment | https://tax.gov.ae/Datafolder/Files/Legislation/Corporate%20Tax/Ministerial%20Decision%20No.%2073%20of%202023%20-%20for%20publishing.pdf | 2026-11-26, read: MD 73/2023, Articles 2-6, with S10 amendment |
| Small Business Relief Guide, revenue, election and exclusion sections pp 11-15; old sunset superseded | https://tax.gov.ae/Datafolder/Files/Guides/CT/Small%20Business%20Relief%20Guide%20-%20EN%20-%2029%2008%202023.pdf | 2026-11-26, read: Small Business Relief Guide, revenue, election and exclusion sections pp 11-15; old sunset superseded |
| Consolidated Corporate Tax Law, Articles 3-4, 11-12, 18-21, 28-39, 44, 47-48, 51, 53, 56-58; relevant definitions and neighbours | https://mof.gov.ae/wp-content/uploads/2026/01/Federal-Decree-Law-No.-47-of-2022-and-its-amendments-en-v13.1.26.pdf | 2026-11-26, read: Consolidated Corporate Tax Law, Articles 3-4, 11-12, 18-21, 28-39, 44, 47-48, 51, 53, 56-58; relevant definitions and neighbours |
| MD 126/2023, Articles 8-11 and 14; exclusions require specialist determination | https://tax.gov.ae/Datafolder/Files/Pdf/2023/Ministerial%20Decision%20No.%20126%20of%202023%20on%20the%20General%20Interest%20Deduction%20Limitation%20Rule%20-%20for%20publishing.pdf | 2026-11-26, read: MD 126/2023, Articles 8-11 and 14; exclusions require specialist determination |
| Decision 116/2022, Articles 2-3 | https://tax.gov.ae/Datafolder/Files/Legislation/Corporate%20Tax/Cabinet%20Decision%20No.%20116%20of%202022%20-%20for%20publishing.pdf | 2026-11-26, read: Decision 116/2022, Articles 2-3 |
| Decision 100/2023, Articles 3-8; income classification remains referred | https://tax.gov.ae/Datafolder/Files/Legislation/Cabinet%20Decision%20No.%20100%20of%202023%20on%20Determining%20Qualifying%20Income%20for%20the%20Qualifying%20Free%20Zone%20Person%20-%20for%20publishing.pdf | 2026-11-26, read: Decision 100/2023, Articles 3-8; income classification remains referred |
| MD 229/2025, Articles 3 and 5-7; detailed activities remain referred | https://tax.gov.ae/Datafolder/Files/Pdf/2025/MD-No-229.pdf | 2026-11-26, read: MD 229/2025, Articles 3 and 5-7; detailed activities remain referred |
| Losses bulletin, questions 3-6 and 9 | https://tax.gov.ae/Datafolder/Files/Pdf/2026/CT-Tax-Bulletin-Corporate-Tax-Losses-EN.pdf | 2026-11-26, read: Losses bulletin, questions 3-6 and 9 |
| CTP006, Summary and Detailed Analysis pp 2-4 | https://tax.gov.ae/Datafolder/Files/Pdf/2025/CTP006-Waiver-of-Late-Registration-Administrative-Penalty-02-07-2025.pdf | 2026-11-26, read: CTP006, Summary and Detailed Analysis pp 2-4 |
| Decision 75/2023 amended penalty table, items 7-8 and 14; other items referred | https://tax.gov.ae/Datafolder/Files/Legislation/Cabinet%20Decision%20No.%2075%20of%202023%20and%20amendments%20-%20For%20Publishing.pdf | 2026-11-26, read: Decision 75/2023 amended penalty table, items 7-8 and 14; other items referred |
| FTA Decision 3/2024, Articles 3(3), 5 and 8; other categories referred | https://tax.gov.ae/Datafolder/Files/Legislation/RE%20FTA%20Decision%20No.%203%20of%202024%20on%20Registration%20Timeline%20for%20Corporate%20Tax%20%20-%20For%20publishing.pdf | 2026-11-26, read: FTA Decision 3/2024, Articles 3(3), 5 and 8; other categories referred |
| MD 84/2025, Articles 2-5 | https://tax.gov.ae/Datafolder/Files/Pdf/2025/MD-No-84-of-2025.pdf | 2026-11-26, read: MD 84/2025, Articles 2-5 |
| MD 131/2026, whole amendment and commencement | https://mof.gov.ae/wp-content/uploads/2026/08/Ministerial-Decision-No.-131-of-2026-Amending-Certain-Provisions-of-Ministerial-Decision-No.-73-of-2023-on-Small-Business-Relief-for-the-Purposes-of-Federal-Decree-Law-No.-47-of-2022-EN.pdf | 2026-11-26, read: MD 131/2026, whole amendment and commencement |

Not yet confirmed: the detailed specialist determinations listed under "When to refuse or refer" are non-usable holds. Check this point with one of our partner accountants. No held method, exemption, election, relief or deadline may be inferred from a screening example.
