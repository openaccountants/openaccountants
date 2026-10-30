---
name: moldova-income-tax
description: "Compute Moldova individual income tax for 2026 after classifying residence, citizenship, source, legal activity and the actual tax regime. Covers annual ordinary income, sole-trader and professional profit, personal/spouse/dependent exemptions, actual contribution and personal deductions, capital gains, final withholding, property rentals, foreign-tax credit and separate retail, plant-purchasing and independent-service regimes. Use for CET18, annual personal tax, self-employed tax, freelancer income, taxable investment receipts, exemption eligibility, foreign interest, capital disposals, fixed contributions and income-tax filing. This source-cited writer draft preserves predecessor subjects, identifies ordinary and specialist gaps, and requires independent whole-country review. It does not certify every treaty or special-regime implementation or claim accountant attestation."
version: 0.4
jurisdiction: MD
tax_year: 2026
last_updated: 2026-10-30
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Moldova individual income tax and self-employment, 2026 v0.4

## Who this applies to

Classify the individual, residence, citizenship, income source, legal activity and actual regime before calculating Moldova's 2026 income tax. This local source-cited writer draft covers ordinary annual individual liability, registered business/professional income, final withholding, capital gains and the separate retail, plant-purchasing and independent-service regimes. It replaces the old 2025 summary, not the need for the correct underlying documents. Whole-country independent review and accountant attestation are not yet complete. [Fiscal Code arts. 5, 13–15, 39–44, 69^1–69^26, 83][code].

An individual meets the domestic residence definition through permanent domicile, including the stated temporary overseas treatment/rest/study/duty cases, or at least 183 days in Moldova during the fiscal year. The specific diplomatic/international-organisation, exclusive treatment/rest/study and transit exclusions in art. 5(6) still matter. Do not use a foreign passport, bank account or residence permit alone as the tax conclusion. Actual treaty residence is a separate test under the operative agreement. [Art. 5(5)–(6), 79^3][code].

The charge is not identical for every resident. Resident business/professional taxpayers have art. 13(1)(a)/14(1)(a)'s worldwide business/professional scope. For non-business Moldovan citizens, domestic-source income and foreign-source income for activity in Moldova are covered, together with the separately stated foreign investment/financial income. Resident foreign citizens/stateless persons have the stated Moldova-activity/source scope with the statutory exclusion for foreign investment/financial income. Nonresidents use the specified Moldova-source and chapter-11 routes. Do not turn “resident” into an unsupported universal worldwide-income statement. [Arts. 13–14][code].

Keep distinct: ordinary employees; an individual entrepreneur; the statutory peasant farm; a justice/medical professional; independent retail; plant-product purchasing; and an ASP-registered independent service entrepreneur. The new service regime is not a universal 15% election for every freelancer. Professional sector, legal registration, approved activity, payer relationship and dates matter. A company dividend or an employee's pay is not converted into business turnover by the bank description. [Arts. 15, 44, 69^1–69^26, 88–90^1][code].

Use [payroll](moldova-payroll.md) for cumulative wage withholding and [social/medical contributions](moldova-social-contributions.md) for the contribution categories, minimums, status and reporting. Those connected drafts have explicit gaps and have not completed whole-pack review. Use [corporate tax](md-corporate-income-tax.md) for company regimes and the detailed business-expense interface; [VAT](moldova-vat.md), [TP](md-transfer-pricing.md) and [cross-border](md-cross-border.md) retain their own currency/scope until their rewrites. The old “Tier 1/Tier 2” internal headings never established accountant review.

## Rates, bands and thresholds

All amounts are MDL. Rates apply only after the statutory category/base is established.

| Item | 2026 rule | Primary authority |
|---|---|---|
| Ordinary individual/individual-entrepreneur/justice/medical professional income tax | 12% of annual taxable income | [Art. 15(a)][code] |
| Day worker | 12% of taxable income without chapter-4 exemptions | [Art. 15(a^1)][code] |
| Statutory peasant farm | 7% of taxable income; not a general agricultural-company or distribution rate | [Art. 15(c)][code] |
| Standard personal exemption | 29,700 a year; annual taxable-income test strictly below 360,000, excluding art. 90^1 income and including the stated independent-retail/plant-purchasing income | [Art. 33(1)–(1^1)][code]; [January version][jan] |
| Increased personal exemption | 34,620 a year for the exact statutory categories | [Art. 33(2)][code] |
| Qualifying spouse exemption | 21,780 a year with art. 33(2)-category spouse and non-use conditions | [Art. 34][code] |
| Ordinary qualifying dependent | 9,900 a year | [Art. 35(1)][code] |
| Specified disabled dependent | 21,780 a year under the exact disability/relationship conditions | [Art. 35][code] |
| Dependent's income condition | Not above 12,400 annually, excluding the specified State disability allowances | [Art. 35(2)(b)][code] |
| Taxable capital-gain inclusion | 50% of recognised current-period gains exceeding recognised capital losses | [Arts. 40(7), 41][code] |
| Ordinary resident-individual dividend withholding | 6%; historical 2008–2011 undistributed-profit category 15%; separate pre-2008 exemption/category check | [Art. 90^1(3^1), 20(z^10)][code] |
| Royalty final withholding | 12% for the covered individual payment, with the independent-service-entrepreneur exception | [Art. 90^1(3^1)][code] |
| Specified domestic bank/credit-issuer and similar interest | 6% final withholding under the stated payer/category rule, excluding art. 20(z^20) cases | [Art. 90^1(3^7)][code] |
| Other covered interest and preliminary resident withholding | 12% advance/creditable route under arts. 89–90, rather than assuming every interest receipt is finally taxed at 6% | [Arts. 89–90][code] |
| Property use paid by art. 90 payers | 12% final withholding for the covered movable/immovable use, excluding agricultural land rent | [Art. 90^1(3)][code] |
| Covered resident non-business immovable-property letting to other specified tenants | 7% of monthly contract value, with registration/payment duties | [Art. 90^1(3^4)][code] |
| Covered gambling | 18%, with the exact lottery/sports-bet exemption; 1% of the standard personal exemption = 297 is the relevant statutory lottery/sports reference, not a universal deduction from every gambling receipt | [Arts. 90^1(3^3), 20(p^1)][code] |
| Promotional-campaign winnings | 12% on the part above the standard personal exemption, 29,700 | [Arts. 90^1(3^3), 20(p^2)][code] |
| Independent retail | 1% of its income base; ordinary full-year minimum 3,000, with 750 quarterly and 250-per-active-month rules as applicable | [Arts. 69^10–69^12][code] |
| Retail eligibility measures | Resident individual without legal organisational form; non-excise retail; commercial area up to 50 m² and period income not above 1.2 million; current art. 69^13 adds its 1 July 2026 registration cut-off | [Arts. 69^6–69^7, 69^13][code]; [January comparison][jan] |
| Plant-product purchasing regime | 6% final withholding by covered business purchaser; annual 1.2-million ceiling and separate 12% excess route | [Arts. 69^14–69^19][code] |
| Registered independent service entrepreneur | Single tax 15% up to annual income 1.2 million and 35% on the excess | [Arts. 69^20–69^26][code] |
| Personal medical/insurance/first-home interest reference caps | One forecast monthly average salary, 17,400, for the separate statutory routes and actual conditions below | [Art. 35^2(3)–(5)][code]; [CNAS point 12.1, Government Decision 773/2025][cnas] |
| Own training/education and dependent-child education deduction | 20,000 cumulatively for the covered institutions/beneficiaries, not 20,000 per child/provider | [Art. 35^2(6), effective 1 January version][jan]; [current Code][code] |

The January/current selected Code comparison confirms the personal/spouse/dependent amounts, strict personal-exemption gate and the 20,000 education limit. It does not certify every 2026 amendment interaction. The old claim that retail 1% expired at the end of 2025 is wrong: chapter 10^2 remains in the current Code. Keep its July registration condition distinct from the new chapter-10^4 service regime, VAT thresholds and any actual cessation. [Arts. 33–35^2, 69^6–69^26][code]; [January Code][jan].

## The base

### Ordinary annual income and registered business/professional profit

1. Establish residence/citizenship, source, legal activity, year and regime. Separate final-withholding income, exempt receipts, non-business annual income, business profit and special-regime turnover. Do not tax every bank credit or apply 12% to every activity labelled “freelance”. [Arts. 13–15, 18–21, 69^1–69^26, 90^1][code].
2. Apply the proper timing method. Non-business individuals ordinarily use cash accounting. Individual entrepreneurs can use cash or accrual under art. 44; professional-sector individual taxpayers use the specified cash method under art. 69^2, while legal entities use accrual. Do not deduct an unpaid expense simply because an invoice exists under a cash method, and do not ignore accrued income under an accrual method. Method changes require the statutory adjustment to avoid omissions/double counting. [Arts. 44, 69^2][code].
3. Include the taxable business/professional receipts, salary, rent, interest, royalties, covered debt releases, subsidies and other art. 18 sources under their applicable regime. Exclude only the exact art. 20 category and person entitled to it. State social benefits, qualifying damages/donations/inheritances, contributions to capital, specified grants and other exemptions have different conditions. Foreign payer, grant, gift or private-transfer wording alone is not the exemption. [Arts. 18–21][code].
4. For ordinary business/professional income, deduct actual ordinary necessary business expenditure under the applicable chapter-3 rules and accounting method. Preserve invoices, contract, business purpose, payment/timing and apportionment. Mixed business/private costs require art. 24(2)'s greater-business-than-private test and only the direct business portion. No default home-office, phone/internet, car, meal or travel percentage is certified. Capital purchases, private expenses, income tax, statutory fines/penalties and exempt-income costs cannot all be deducted as ordinary expenses. [Arts. 24–31, 44, 69^3][code].
5. Keep operating expenses separate from deductible personal mandatory contributions and personal allowances. Article 35^2(1)–(2) allows actual compulsory medical and social contributions paid by the person in statutory amounts during the period. The employer's social cost is not the employee's payment. Do not deduct the same premium in business expenses and again as a personal deduction. The ordinary employee 6% social deduction in the old Guide is removed. Use the actual fixed category and payments rather than assigning every self-payer the same amount. [Art. 35^2][code]; [CNAS 2026 categories][cnas]; [CET18 instruction points 33–34][cet].
6. For qualifying ordinary business tax losses, keep the article-32 origin-year ledger, following five periods, remaining amounts and chronological use. Capital losses are restricted separately to capital gains; special turnover taxes do not become profit taxes through an expense/loss deduction. Do not transfer a business loss into every household income category. [Arts. 32, 40–41, 54^2, 69^10, 69^24][code].
7. Apply actual exemptions and personal deductions only once. Compute ordinary tax at the applicable legal rate, then match allowable creditable domestic withholding/instalments and foreign-tax credit to the same taxable income/period. Final art. 90^1 withholding is not a general credit against ordinary tax. Separate an amount payable from an excess payment/refund request. [Arts. 15–16, 33–35^2, 79, 81–87, 90^1][code].

For expenses, preserve the original Guide's practical categories as evidence questions: software/cloud/SaaS and platform charges; telecom/utilities; home office/rent; travel/transport; banking/professional charges; subcontractors; equipment/capital assets; private expenditure and mixed use. Vendor names such as a software supplier or airline do not establish a deduction or the VAT result. For an asset with life above one year and value above 12,000, test the tangible depreciation regime, separate asset register, commencement, Government life and permitted method. The non-financial accelerated option is a maximum first-year 50% under its conditions, not a universal write-off. Bad debt requires the statutory compromised-debt proof; an uncollected cash-basis receipt never taxed does not automatically create a tax deduction. Interest benchmarks, one-car occupation limits, business-charity caps and supporting procedures require their actual statutory facts. [Arts. 24–26^1, 28, 31–32, 36, 44][code]; [corporate method and remaining procedure gaps](md-corporate-income-tax.md).

Transactions in foreign currency use the official MDL exchange rate at the statutory transaction date, not an invented annual average or net conversion shown by a payment platform. Article 21(3) defines transaction-date evidence, year-end debt revaluation, advances and uncoted-currency conversion. Preserve gross foreign receipts, fees, withholding, original currency, bank/platform dates and the applicable official rate independently. Match the actual accounting method and current-year FX differences rather than treating every bank conversion difference as a deductible cost. [Art. 21(3)][code].

For non-cash income, donor transactions and related-person transfers, apply the specific valuation rule. Article 21(4) deems excess cash donations by a non-business donor income to that donor over the period's income, subject to the first-degree relative/affinity and spouse exceptions. Article 40 has its separate donated-capital-asset treatment; recipient exemptions under art. 20 have their own citizenship/category conditions. Internal transfers and loan principal are reconciliation subjects, not automatically business income or an automatic tax exemption for an unexplained receipt. [Arts. 20–21, 40][code].

### Personal, spouse and dependent exemptions

For the personal exemption, including the increased art. 33(2) amount, verify the resident's statutory annual taxable-income test strictly below 360,000, excluding art. 90^1 income and taking account of the specified chapter-10^2/10^3 income. Exactly 360,000 fails a “less than” test. Do not use only salary or blindly multiply the latest net/gross bank payment by twelve. The employer is not required to track the employee's loss of entitlement under art. 88(1); annual reconciliation remains necessary. [Arts. 33(1)–(2), 83, 88][code]; [Government Decision 693/2018 annex 2 point 21^1][personalreg].

The increased personal amount requires the exact listed Chernobyl/qualifying war/disability or rehabilitated-repression category and evidence. The spouse relief requires a spouse in art. 33(2)'s category who is not using the personal exemption; it is not a standard allowance transferable by every couple. The dependent must meet the cumulative relationship and income requirements, including the specified guardian/curator route; the annual 12,400 income test excludes only the specified State disability allowances. Dependents' age alone does not answer the relationship/income test. Spouse/dependent rights arise from the next month under arts. 34–35. The current regulation applies the personal-exemption annual-income gate to art. 33 and expressly preserves the separate art. 34–35 spouse/dependent tests. The increased personal amount is not an exception to that gate. The personal exemption and dependent/spouse routes must be tested separately. [Annex 2 point 21^1][personalreg]. [Arts. 33–35][code]; [payroll regulation points 9–35 and evidence tables][reg].

For payroll, use the actual signed application, one permitted location, supporting documents and start/withdrawal month. No valid claim/evidence means no payroll exemptions; a mid-year hire does not automatically receive twelve months. The annual twelfths are 2,475 standard, 2,885 increased and 825/1,815 for the relevant dependent/spouse categories in eligible months. Special-regime months restrict relief under art. 35^1; the regulation has the separate mixed-month rule. Annual claims, newly acquired residence, divorce, death, maternity and a dependent's income changes need their own reconciliation, not a permanent default amount. [Arts. 34–35^1, 88][code]; [regulation points 9–26, 38–48][reg]; [payroll method](moldova-payroll.md).

### Actual personal deductions

Article 35^2 permits actual mandatory health premiums and mandatory social contributions paid within the legal amounts. Its separate personal routes cover voluntary medical insurance or qualifying medical services from one provider for an insured person; covered life/health/fire/natural-disaster insurance contracts with the stated combined cap; and interest paid for the first home on a qualifying non-State-programme credit, apportioned by ownership share for jointly owned property. The forecast-salary cap is 17,400 for the stated 2026 routes. Do not create two independent medical caps merely because CET18 has separate E3/E4 fields, deduct a loan's principal as home-loan interest, or deduct a premium paid by somebody else as this person's expenditure. [Art. 35^2(1)–(5)][code]; [CNAS point 12.1][cnas]; [CET18 points 33–35^1][cet].

For own education/professional training and covered dependent-child education at the statutory institutions, art. 35^2(6) sets a **20,000 aggregate cap** for all covered education/training and beneficiaries. The January 2026 version explicitly records this change operative 1 January. Retain provider, beneficiary, contract/invoice and payment evidence. Current CET18 point 34^6 refers to this Code amount, but generic point 34^7 still says one forecast salary for E3–E7. Follow the statute's 20,000 for the 2026 education working paper and record the inconsistency; do not reduce the legal cap to 17,400 or certify the portal's 2026 filing implementation without checking it. The directly read Government proof requirements and January/June change are set out below; the separate current form/portal inconsistency is not certified as resolved. [Art. 35^2(6), January version][jan]; [current Code][code]; [CET18 points 34^6–35^1][cet].

**Keep an evidence schedule for each personal deduction.** Government Decision 693/2018 annex 2 is the regulation for resident Moldovan citizens; apply its scope and the Code's actual taxpayer/eligibility rules, rather than extending resident relief to every nonresident. Its point 35 permits the article-35^2 claim through the annual return or, from **18 June 2026**, during a tax inspection. That procedural change does not turn an unpaid invoice into an expense or establish a particular taxpayer's eligibility. [Annex 2 points 1–5, 16–18, 35][personalreg]; [Decision 321/2026 points 2.2.2, 3][personalamend]; [Code arts. 13–14, 35^2, 74][code].

| Personal deduction | Required proof under regulation point 35^1 | Keep the statutory limit and facts separate |
|---|---|---|
| Voluntary medical premium or qualifying medical services | Tax invoice or another document confirming actual payment | Establish insured status, the eligible service/provider route and the article-35^2(3) cap; an unpaid bill or separate E3/E4 boxes does not create a second cap. [Point 35^1(1)][personalreg]; [Code art. 35^2(3)][code] |
| Covered life/health/fire/natural-disaster insurance premium | Insurance contract **and** tax invoice or another document confirming actual payment | Reconcile the covered contracts and actual personal payments together under article 35^2(4). [Point 35^1(2)][personalreg]; [Code art. 35^2(4)][code] |
| First-home interest outside State programmes | Credit contract **and** bank-account statement showing interest paid during the tax period | Principal is not interest. Establish first-home and credit eligibility, the person's paid interest, beneficiary status and ownership share before applying the statutory limit. [Point 35^1(3)][personalreg]; [Code art. 35^2(5)][code] |
| Covered own education/professional training or dependent-child education | From 18 June: provider contract **or another document identifying both provider and beneficiary**, plus actual-payment proof. For cash payment, obtain the provider's confirmation stating the payment date | Identify the qualified institution/service, actual payer, beneficiary/dependency and tax-period payment. The Code's **20,000 aggregate limit** is shared across covered education/training and all beneficiaries. Proof alone does not make every course or family member eligible. [Point 35^1(4)][personalreg]; [Code art. 35^2(6)][code] |

**Education commencement.** The January regulation's point 35^1(4) referred only to dependent-child education, a contract with the educational institution and an invoice/other actual-payment proof. The January Code already permits the covered own education/training and the 20,000 aggregate limit from **1 January 2026**. Decision 321/2026 replaces the Government proof paragraph on **18 June**, adding the provider/beneficiary identification alternative and express cash-provider confirmation. Do not start the statutory own-education right or 20,000 limit in June merely because the regulation was aligned then. Retain payment dates and the applicable proof version; the current CET18 generic-cap inconsistency remains a separate implementation gap. [January Code art. 35^2(6)][jan]; [January regulation point 35^1(4)][personalregjan]; [Decision 321/2026 points 2.2.3, 3][personalamend].


A voluntary pension-fund contribution, annuity, donation or other deduction needs the actual statutory route and proof. The form's historic examples are not proof that every current payment qualifies. Keep contributions, personal relief, business expenses, final-withholding receipts and credits in separate schedules. [Arts. 21, 24–36, 64–69, 81–82][code]; [CET18 deduction instructions][cet].

### Capital gains, property and financial receipts

Identify the capital asset and the type/date of disposal. Article 39 covers the specified participation/debt/property/land/option assets. Under art. 40, gross monetary/non-monetary disposal value less documented adjusted cost produces each recognised gain/loss. Use the broker report for the specified exchange transactions. Only 50% of recognised gains above recognised current-period losses enters the income base; capital losses cannot reduce unrelated ordinary income. Do not apply 12% to the full sale proceeds or assume every investment gain is finally withheld. [Arts. 39–42][code]; [CET18 capital table K, points 60–67][cet].

Cost must be established under art. 42 and the applicable documentation rule. Purchase/self-build, gifts/inheritance/lifetime maintenance, exchanges, privatisation, contributions to capital and stock-option awards have different bases. The statute includes zero cost where supporting documents are absent, with its specific self-constructed-property cadastral route rather than an invented estimate. Keep capital changes and historical ownership records; an untaxed receipt's market value is not automatically the cost of every asset. [Art. 42][code].

**Allocate proceeds and cost before applying the 50% inclusion.** Government Decision 693/2018 annex 2 point 39 allocates a single acquisition price among multiple capital assets in proportion to each asset's market value on the transaction date. Under point 40, jointly owned disposal proceeds **and adjusted cost** follow each owner's share; for undivided common ownership, the written common agreement identifies one owner as the taxpayer under that route. Do not allocate only proceeds, use the full joint cost for every owner, or infer that a written reporting agreement changes every substantive ownership rule. [Code arts. 40–42][code]; [annex 2 points 38–40][personalreg].

For instalment consideration spanning tax periods, point 44 requires a calculation in each period according to the contract's shares, or equal shares if it specifies none, with the corresponding proportional cost allocation. Keep cumulative proceeds and cost already used so the same full basis is not deducted against every instalment. Point 43 separately states an arithmetic-average basis for the specified differently valued equity/debt/ownership positions in the same business; do not invent a universal FIFO or apply that paragraph to unrelated property. Post-1998 capital contributions use the documented monetary contribution, including subsequent contributions; older property/shares have their own 1 January 1998/31 December 1997 basis provisions. Adjust actual capital withdrawals/increases under Code art. 42(4). [Code art. 42][code]; [annex 2 points 41–44][personalreg].

**Obtain the correct cost documents.** MF Order 40/2018 approves the capital-cost proof list; its approval page was read, but the separate annex was not retrieved. For inherited property, the SFS's published Order 13/2025 interpretation, question 29.2.4.18, confirms the legal-heir certificate together with either a competent valuation report establishing market value on acquisition, or the property-value certificate from the State property-register authority. This supports the specific inheritance route, rather than certifying the entire unretained annex. The same official page's question 29.2.4.4 says a cash-register fiscal receipt alone proves cash collection and is insufficient to establish capital-asset cost. Match the acquisition route and Code art. 42 exception before applying a zero basis; the self-built-property cadastral route remains distinct. [Code art. 42(1)][code]; [MF Order 40/2018 approval][capitalorder]; [SFS questions 29.2.4.4, 29.2.4.18][capitalproof].


Test non-recognition precisely: qualifying spouse/divorce redistribution, specified issuer redemptions, exercise/conversion of options, first-degree/spouse capital gifts, and the main-home and specified car conditions. A main home requires at least three years' ownership and the stated last-three-years domicile/residence test, including its at-most-90-day cancellation rule. The car rule requires at least three years' ownership and excludes historical/ethnographic collector vehicles. Joint marital-property disposal and stock-option transactions have specific calculation rules. Do not infer a home exemption merely from occupancy on sale day. [Arts. 5(46), 39–42][code].

For resident non-business rentals, identify the tenant/payer. Covered art. 90 payers withhold 12% finally for the stated property-use income, excluding agricultural land. Covered immovable-property letting to other specified tenants uses the person's 7%-of-monthly-contract-value route, contract registration within seven days and the payment rules below. Do not apply the latter resident route to every foreign/nonresident lessor. Agricultural land and nonresident property income have separate provisions. [Arts. 90^1(3), (3^4), 74][code].

Separate ordinary/preliminary and final withholding. Resident dividends ordinarily use 6%, with 2008–2011 and pre-2008 profit-origin distinctions; royalties use the stated 12% final route and new independent-service exception; specified bank/credit-issuer/crowdfunding interest uses 6% final withholding, while other art. 89 interest uses its 12% preliminary route. Covered cash gifts, natural farm-produce sales, consignment sales and plant-purchaser income have their own final categories. Do not credit an art. 90^1 final tax again or report its covered receipts as ordinary annual income merely because the bank shows gross and net. [Arts. 16, 20(z^10), 69^18, 89–90^1][code].

Gambling, lottery/sports-bet and promotional winnings are different categories. Apply the exact art. 20(p^1)/90^1(3^3) lottery/sports exemption and electronic-communications exception, rather than deducting 297 from every gambling win. Promotional winnings have the separate 12% rule on the part above 29,700. Confirm the organiser, type, channel, individual winning and withholding evidence; ambiguous lottery boundary/online mechanics are not guessed in this draft. [Arts. 20(p^1)–(p^2), 90^1(3^3)][code].

### Professional practice and separate turnover regimes

**Justice/medical professionals.** Apply chapter 10^1's actual subject, cash method for individual taxpayers, business deductions and chapter-4 personal relief. Tax is annual; quarterly payments are due by the 25th after the relevant quarter, and the declaration by 25 March following the year. The return and electronic method are separately prescribed; do not label every professional return CET18. Foreign-tax credit remains subject to art. 82. Fixed social/medical categories are a separate liability and deduction schedule. [Arts. 69^1–69^5][code]; [social/medical Guide](moldova-social-contributions.md).

**Independent retail.** Verify resident status, absence of a legal organisational form, non-excise retail activity, commercial unit no larger than 50 m², period income no higher than 1.2 million and the actual SFS registration. The January version lacked the later registration cut-off sentence; the current Code requires registration satisfying art. 69^13(3)'s statutory 1 July 2026 cut-off. The 1% regime itself did not expire at the end of 2025. Do not apply a later entry condition retrospectively to a January registration decision without its amendment history. Current-period eligibility after the cut-off requires the actual register record. [Arts. 69^6–69^7, 69^13][code]; [January version][jan].

For qualifying retail, use the defined income base, reducing current-period returns/discounts including those from earlier sales. The ordinary full-year minimum is 3,000. The first three quarterly assessments use 1% of sales with the stated 750 minimum; the fourth reconciles the annual amount against prior assessments. The short-year rule uses at least 250 for each registered active month. The first-period cash-register equipment tax reduction excludes compensated costs; do not assume it is also an ordinary expense deduction. SFS assesses/notifies under art. 69^12; keep the notices, recorded sales, cash-register data, goods-provenance documents and purchase register. Registration, five-day cessation notice, one-year provenance-document retention and annual purchase-register submission are specific duties, not a universal exemption from records. [Arts. 69^7–69^13][code].

**Plant-product purchasing.** The regime concerns the listed Moldovan-harvested plant/horticultural/vegetal products bought from non-business individuals for sale to businesses. Check the Ministry's actual product list and SFS registration. The business purchaser withholds 6% finally on the defined sale income; if the person's calendar-year sale income exceeds 1.2 million, the Code requires a return and 12% on the excess without crediting the already withheld tax as though it discharged that excess rule. Preserve the mandated source/quantity/location transaction documents even where the statute disapplies ordinary accounting/statistical requirements. [Arts. 69^14–69^19][code].

**Independent service entrepreneur.** The 2026 regime requires ASP registration/state identifier and an activity within the Code annex, not a general “freelancer” description. The rendered annex lists the exact CAEM entries 15.1, 23.13, 23.41, 23.44, 23.49, 32.1, 32.2, 32.3, 32.4, 33.1, 43.22, 58.1, 58.2, 59.1, 59.2, 62.01, 62.02, 63.1, 63.91, 70.21, 71.11, 71.12, 73.20, 74.1, 74.2, 74.3, 79.9, 81.2, 81.3, 82.19, 82.3, 85.5, 88.9, 90.01, 90.02, 90.03, 93.11, 93.12, 93.19 and 96.09, with the stated exclusions for the last entry. Match the actual activity description, not only a similar code. [Arts. 69^20–69^21 and annex][code].

SFS records the service activity from the prescribed connected cash-register data and dedicated payment accounts. Cash operations require the approved cash register/receipt, and multiple dedicated accounts in permitted currencies are possible. The no-ordinary-accounting/no-tax/statistical-return rule in art. 69^22 does not waive registration, payment, cash records or evidence of the income base. Compute 15% on annual cumulative income up to 1.2 million and 35% on the excess; current-month returns/discounts reduce the month's defined receipts. Do not deduct ordinary business expenses as if this were a 12% profit regime or charge a second tax merely because the same money moves between dedicated accounts. Keep the statutory base and actual SFS notice reconciled. [Arts. 69^22–69^26][code].

The single tax includes income tax, social, medical and local taxes, allocated 26.3%/53.3%/15.4%/5.0% respectively. These are portions of the tax, not additional percentages of gross income. SFS sends the next-month notice by the 10th; payment is by the 25th. If annual medical allocation does not cover the statutory reduced fixed amount for the referenced health category, the person pays the difference on the additional notice by 25 February of the following notice year; the notice is sent by 25 January. The current medical-budget art. 4 sets the referenced eligible amount at 2,527, not the Finance Ministry overview's 2,572 typo. This top-up is separate from the 15%/35% computation, and category/status/year facts must be verified. [Arts. 69^25–69^26][code]; [medical budget art. 4][medicalbudget].

Company-payer deductibility and employee reclassification remain distinct checks: art. 24(11^1)'s specific small-employer/payroll-cap or listed-main-activity route and art. 88(8) must be tested before treating a service-entrepreneur payment as outside payroll. IT-park/company SME rules are separate regimes and are not elective substitutes chosen from whichever headline rate is lowest. Full registration/cessation implementing rules, cumulative-band adjustments and actual payment-account/cash-register procedures remain explicit gaps for the country review. [Arts. 24(11^1), 54^1, 69^20–69^26, 88(8)][code].

### Bank classification and the annual working paper

Retain gross receipt, original currency, fee, withholding, VAT component where legally established, date, counterparty and purpose for each movement. “SALARIU”/“SALARIZARE”/“AVANS” are wage/advance search hints; invoice/client/platform references are possible business receipts; “DIVIDENDE”, “DOBANDA”, “ROYALTY” and “CHIRIE” require their specific income classification. “CNAS”/“BASS”/“CONTRIBUTIE SOCIALA FIXA” and “CNAM”/“FAOAM”/“PRIMA ASIGURARE MEDICALA” require payer/category/year proof before a deduction. A statutory remittance is not automatically a business expense, and a net platform payout does not prove gross revenue.

Use software/cloud/SaaS, utilities, telecom, professional/bank charges, travel, rent, contractors and equipment descriptions to gather invoices/contracts and business-use evidence, not to auto-approve a deduction. Transfers between own accounts, capital injections, loan proceeds/principal repayments, refunds, private gifts and asset sales require their own reconciliation. Do not infer taxable turnover, deductible business expenses or VAT from the direction of the bank movement alone. The old bank-format references (Maib/Moldova Agroindbank, MICB/Moldindconbank, OTP/Mobiasbanca and Victoriabank) are possible statement labels; Romanian debit/credit, sold/balance, comision, transfer, incasare and plata wording are parsing cues, not legal categories.

For a bank-only intake, reconcile accounts and transfers, request legal registration/residence/activity facts, gross-versus-net invoices/platform reports and expense documents, then identify what can actually be computed. No unverified maximum business-use percentage, automatic personal exemption, arbitrary “conservative” legal category or guessed fixed contribution is certified. Flag unresolved items individually with the fact/source needed to settle them.

The annual working paper keeps taxpayer identity/residence/citizenship; period and regime registration; income by legal category/source and timing method; original-currency/MDL conversion; ordinary profit and deduction schedules; actual compulsory contributions; personal/spouse/dependent evidence and months; personal education/medical/insurance/home-interest evidence/caps; capital disposals, cost, recognised gains/losses and 50% inclusion; final/preliminary withholding; foreign credit by income and period; instalments; the correct return/form fields; payment/acceptance receipts; and remaining questions. Keep separate retail/plant/service and IT-park schedules. Reconcile cash to taxable income rather than presenting cash flow as the return.

## Deadlines and filing

| Obligation | Method/deadline | Primary source |
|---|---|---|
| Ordinary non-business individual annual return | 30 April following the tax year when art. 83 requires filing; 2026 ordinary income therefore uses the following-year deadline | [Art. 83(2), (4)(b)][code] |
| Individual entrepreneur/other resident organisational form | Separate art. 83(4)(a) 25th-of-third-month route; art. 83(11) unified return applies to the specified non-VAT individual entrepreneur/peasant farm with annual average staff not above 5 | [Art. 83][code] |
| Justice/medical professional return and payments | Annual return by 25 March; quarterly payments by the 25th after the relevant quarter | [Art. 69^5][code] |
| Ordinary final payment | By the statutory return due date; a filing extension does not automatically extend payment | [Art. 87(1)][code] |
| Change of permanent domicile abroad | File for the resident part of the period; CET18 A2 instructions require filing by the last working day before departure | [Art. 83(7)][code]; [CET18 point 7][cet] |
| Specified nonresident cessation | Art. 74's covered nonresident files/pays within three days of ending activity; this is not a universal foreign-citizen deadline | [Art. 74(4)][code]; [CET18 point 7][cet] |
| Covered resident private letting | Register the contract within 7 days; pay the 7% tax by the 25th of the current month, with the specified post-25th first-month exception | [Art. 90^1(3^4)][code] |
| Retail assessment/payment | SFS quarterly notice by the 25th after the quarter; payment by the 25th of the month following the notice-presentation deadline; preserve quarterly/annual minimum and short-year rules | [Art. 69^12][code] |
| Retail purchase register/cessation | Register submitted by the 25th after the year; cessation information within 5 days of the decision | [Arts. 69^7–69^8][code] |
| Independent service entrepreneur | Notice by next-month 10th, tax by next-month 25th; medical top-up notice by following-year 25 January and payment by 25 February of that notice year | [Art. 69^26][code] |
| Payroll reports/remittance | Separate monthly payment/withholding and contribution-accrual rules in the payroll/social Guides, rather than treating all three components as one bank amount | [Arts. 88, 92][code]; [payroll](moldova-payroll.md) |

Article 83 obliges the relevant individuals with tax payable, professionals regardless of tax, the stated percentage-designation cases and other specific categories. Someone entitled to a refund can file under art. 83(5). The separate art. 83(2)(a^2) filing trigger says annual taxable income **above** 360,000 after personal-exemption use; that does not change art. 33's strict entitlement test. At the exact boundary, calculate the actual liability and apply the general tax-payable filing rule rather than inventing an exemption or ignoring an unpaid liability. [Arts. 33, 83][code].

Use the correct annual form for the legal category. CET18 is approved by Order 150/2018 for its stated resident/nonresident individual scope, not every sole-trader/professional/special-regime return. The currently read April 2026 instructions require the relevant identity and category, actual source income even when documentation is incomplete, and amounts in lei/bani. Electronic filing requires an accepted receipt; paper/postal/electronic alternatives have the instruction's identity/signature/acceptance conditions. This Guide does not authorise any filing or message. The form/version applicable to reporting 2026 income must be checked before actual filing. [CET18 points 1–18, 69][cet].

For covered resident CET18, C1 records wages and withholding; C2 takes taxable capital gains from K8; C3 records the specified foreign investment/financial income and capped foreign tax; C4 other taxable income; C5 totals. D records actual personal/spouse/dependent relief, E actual legal deductions and evidence; F calculates taxable income, any required donor adjustment, tax, credits/self-paid amounts and payable/excess. Capital table K records asset/type/date/proceeds/cost, gains/losses and the 50% net inclusion. Do not copy final-withholding art. 90^1 receipts into ordinary gross or put an unverified deduction into “other”. Resolve the education-cap instruction conflict above, retain the Government Decision 693 evidence schedule, and obtain the remaining Order 40 cost-document annex and current return attachments before certifying all return lines. [CET18 points 19–46, 60–67][cet]; [Code arts. 21, 33–35^2, 39–42, 81–82, 90^1][code].

A non-business person can request a reasonable filing extension in writing before the deadline under art. 83(8); final payment still follows art. 87. A refund, amendment, late filing or departure case needs the actual accepted form, assessment and account movements. Do not substitute the historic 2025 filing example for 2026's return period. Actual UNIF/professional form instructions, all special-regime entry/cessation details and portal implementation remain open below.

## Penalties and interest

**Calendar-2026 ordinary tax late charge.** Code art. 228(3) and the BNM decision of 6 November 2025, point 1, supply the calculation: the retained **6.00%** short-term policy rate, rounded up to a whole percent, plus **5 percentage points**, divided by **365 days**, gives **0.0301% per delayed day** after rounding the daily percentage to four decimal places. The decimal multiplier is **0.000301**. Apply it to the established outstanding principal for each chargeable day; split changes in principal and calendar year. This calculation concerns debts governed by art. 228 and does not replace a separate statutory regime's rate or establish case-specific relief. [Code art. 228(2)–(3)](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro); [BNM decision, point 1](https://bnm.md/en/node/69226).

**Medical and social rates remain separate.** Medical Law 1593 art. 30(1)–(1^1) applies the Code method from **1 January 2026**, as recorded in the January text and Law 146/2025 commencement annotations, so the above 2026 medical daily rate is **0.0301%**. Preserve art. 30(2)'s documented inter-account-transfer examination exception. Social-contribution late charges retain the separate **0.1%** annual-budget rate; do not use it for ordinary tax or medical premiums. [Current Law 1593 art. 30](https://www.legis.md/cautare/getResults?doc_id=152955&lang=ro); [January art. 30 and commencement](https://www.legis.md/cautare/getResults?doc_id=149273&lang=ro); [Law 320/2025 art. 4](https://www.legis.md/cautare/getResults?doc_id=156540&lang=ro).

For ordinary tax late payment, art. 228 charges from the day after due date through payment inclusive, subject to actual debt movements, the statutory BNM-derived annual daily-rate formula and exceptions. Do not compound by automatically adding late charges to principal. Social and medical contribution arrears have separate statutory routes, with social's annual-budget 0.1% and the medical tax-code reference described in the social Guide. [Code art. 228][code]; [Law 489 art. 28][social]; [Law 1593 art. 30][health].

Identify the art. 232 taxpayer category before a filing fine. Article 260(1) distinguishes 200–400 per declaration and a 2,000 total cap for the specified non-business individual category from 500–1,000 and 10,000 for its other stated categories. Understatement through untrue return information has art. 261(4)'s separate 20%–30% sanction and qualifying self-correction exception; evasion has its 80%–100% rule. A registered entrepreneur or professional cannot assume the non-business fine category merely because the taxpayer is a natural person. Retain the actual notice, period, offence, correction and payment facts. [Arts. 232, 260–261][code].

The special rental registration/assessment, special-regime notice duties and fiscal estimation provisions are not replaced by these ordinary fine summaries. Do not conclude criminal/administrative exposure or complete settlement from a bank statement alone. Full special-offence/appeal implementation remains a gap; use the actual decision and governing provision.

## Cross-border points

Apply the actual residence/citizenship and income-source categories in arts. 5, 13–14. A Moldovan citizen's taxable foreign financial income is not automatically exempt because it was retained abroad; a resident foreign citizen's non-business foreign investment/financial income has the stated statutory exclusion. Business/professional worldwide income, services performed in Moldova for a foreign payer, employment, management remuneration and nonresident Moldova-source income require their distinct statutory/treaty routes. Do not apply the employee “183-day” residence definition as a treaty employment exemption. [Arts. 5, 13–14, 71, 74, 79^3][code].

For art. 82 foreign-tax credit, establish that the same foreign income is included in Moldova in the relevant period, obtain actual competent-authority-certified payment/withholding, translate unless English/Russian, and cap the credit at Moldova's tax on that income. Keep gross foreign income and allowable foreign tax separately in the annual schedule. A larger foreign tax does not create an unrestricted Moldova refund, and a final domestic withholding is not an additional foreign credit. [Arts. 16, 81–82][code]; [CET18 point 22][cet].

Treaty relief needs the operative agreement/protocol, income article, entitlement and residence evidence. For an individual nonresident, art. 79^3 requires the competent foreign residence certificate in original paper/electronic form by payment, subject to its translation, validity, changed-status and first-60-days provisions. Without the certificate use domestic law; the later-certificate recalculation/refund route has its own conditions and corrected reporting. Obtain actual coverage/certificates separately for social insurance. No treaty-rate range, country-specific exemption or automatic foreign-tax refund is certified by this draft. [Art. 79^3][code]; [social Guide](moldova-social-contributions.md).

## Two worked examples that recompute

### 1. Ordinary registered individual entrepreneur, paid contributions and personal relief

Assume a resident ordinary individual entrepreneur using the cash method, outside the retail, plant-purchasing, independent-service, IT-park and other special regimes. The verified business receipts are 300,000 and actually paid qualifying ordinary operating expenses 50,000, excluding the personal contributions below. No loss, capital asset, VAT adjustment or other deduction. The person actually paid the correctly classified compulsory fixed social contribution 22,878 and eligible medical premium 2,527; neither was deducted elsewhere. The standard personal exemption is available for the full period, with the statutory income test satisfied, and amounts to 29,700. Taxable income is 194,895; 12% tax is 23,387.40. Creditable evidenced advances of 20,000 leave 3,387.40 payable. Select the entity's actual return under art. 83 rather than automatically labelling it CET18; the example is the tax working paper. [Arts. 15, 24, 33, 35^2, 44, 81–87][code]; [CNAS fixed category][cnas]; [medical budget art. 4][medicalbudget].

```oa-check
name: Moldova 2026 ordinary individual entrepreneur with actual paid contributions
inputs:
  business_cash_receipts: 300000
  qualifying_paid_business_expenses: 50000
  compulsory_social_paid: 22878
  qualifying_medical_paid: 2527
  eligible_personal_exemption: 29700
  pit_rate: 0.12
  creditable_advances: 20000
steps:
  business_profit_before_personal_deductions: business_cash_receipts - qualifying_paid_business_expenses
  income_after_paid_contributions: business_profit_before_personal_deductions - compulsory_social_paid - qualifying_medical_paid
  ordinary_taxable_income: max(0, income_after_paid_contributions - eligible_personal_exemption)
  annual_tax: ordinary_taxable_income * pit_rate
  balance_payable: max(0, annual_tax - creditable_advances)
expected:
  income_after_paid_contributions: 224595
  ordinary_taxable_income: 194895
  annual_tax: 23387.40
  balance_payable: 3387.40
```

### 2. Resident citizen: foreign-interest ceiling and net capital-gain inclusion

Assume a resident Moldovan citizen outside business/special regimes receives 450,000 of taxable foreign interest included in the annual ordinary base. Qualifying certified foreign tax is 60,000, no treaty excludes the income and all same-period credit conditions are established. A separate non-exempt capital disposal has proceeds 200,000 and documented adjusted cost 140,000; other recognised current-period capital losses are 10,000. Net capital gain 50,000 gives 25,000 taxable inclusion. No other deduction/exemption is available or claimed on the established facts; the standard personal-income condition is not satisfied. Ordinary taxable income is 475,000 and tax 57,000. Moldova's tax on the same foreign interest is 54,000, so the foreign credit is capped at 54,000, leaving 3,000 payable. The excess foreign tax is not credited against the separate capital-gain tax. [Arts. 13–15, 33, 39–42, 81–82][code]; [CET18 points 21–22, 60–67][cet].

```oa-check
name: Moldova 2026 resident citizen foreign interest and capital gain credit ceiling
inputs:
  foreign_interest: 450000
  certified_foreign_tax: 60000
  disposal_proceeds: 200000
  documented_adjusted_cost: 140000
  recognised_other_capital_losses: 10000
  capital_inclusion_fraction: 0.50
  pit_rate: 0.12
steps:
  recognised_gain: disposal_proceeds - documented_adjusted_cost
  net_recognised_capital_gain: max(0, recognised_gain - recognised_other_capital_losses)
  taxable_capital_inclusion: net_recognised_capital_gain * capital_inclusion_fraction
  annual_taxable_income: foreign_interest + taxable_capital_inclusion
  annual_tax: annual_taxable_income * pit_rate
  moldova_tax_same_foreign_income: foreign_interest * pit_rate
  allowable_foreign_credit: min(certified_foreign_tax, moldova_tax_same_foreign_income)
  balance_payable: annual_tax - allowable_foreign_credit
expected:
  recognised_gain: 60000
  net_recognised_capital_gain: 50000
  taxable_capital_inclusion: 25000
  annual_taxable_income: 475000
  annual_tax: 57000
  allowable_foreign_credit: 54000
  balance_payable: 3000
```

The archived predecessor's seven transaction examples and eight tax tests remain individually mapped in the ledger, including ordinary self-employment, loss of personal relief, statutory farming, justice fixed contributions, dividend withholding, the VAT invoice, independent-retail minimum and internal transfers. The employee 6% social model, “retail expired in 2025”, blanket 297 gambling subtraction and legal-year/eligibility assumptions are not recertified. The old VAT-inclusive bank illustration does not prove a 2026 VAT rate or place of supply. Old 2025 fixed contribution amounts are preserved as historical subjects; 2026 uses the actual category and primary annual law. Only the two blocks above are this Guide's current executable examples.

## Ask the client first

- What are the person's citizenship, domestic/treaty residence, domicile/travel dates, work locations and any departure/arrival? Supply the supporting records and residence certificates.
- Which exact legal activity/regime and registration apply, on which dates, with which activity code, unit area, customers/payers, income ceiling, employee count and VAT status?
- Supply gross income by category/source/date, foreign currency and fees, withholding certificates, business invoices/expenses, accounting method and actual payments. Identify own-account transfers, loans, gifts, benefits and property transactions separately.
- Supply personal/spouse/dependent evidence and dates, signed payroll applications/non-use, annual-income facts, actual compulsory contributions and medical/insurance/home-interest/education payment/provider documents.
- Supply asset cost/ownership/main-home records, disposal proceeds, broker reports, gains/losses and certified foreign taxes for the same taxed income/period.
- Supply accepted returns/notices, instalments/withholding, SFS/CNAS/CNAM account statements, payment/refund receipts and any corrections or assessments. Do not finalise from bank totals alone.

## Sources

Read 30 October 2026. The [individual-income ledger](../../../ledgers/moldova-income-tax.md) retains statutory bindings, complete predecessor-topic destinations and assumed cases. These are local writer checks, not independent pack review or accountant attestation. Attribution and stamped CTA are preserved; no generated bundle is edited.

| Primary source | Actually read scope and limitation | Read on |
|---|---|---|
| [BNM monetary-policy decision, 6 November 2025, point 1](https://bnm.md/en/node/69226) | Fetched 6.00% short-term base input; calendar-2026 daily percentage derived with Code 228(3), rather than copied from an old rate. | 2026-10-30 |
| [Current Fiscal Code][code] | Selected residence/source, income/exemption/deduction, capital, professional/special-regime, withholding, credit, filing and enforcement provisions cited above | 2026-10-30 |
| [January Code][jan] | Personal/spouse/dependent/deduction and retail-registration comparison; current art. 69^13 includes a later cut-off sentence absent in January | 2026-10-30 |
| [Government Decision 693/2018 current annex 2][personalreg], [January version][personalregjan] and [amending Decision 321/2026][personalamend] | Directly read personal scope, annual-income gate, actual deduction proof and capital-allocation methods; January/June proof change; the statute controls conflicting general summaries | 2026-10-30 |
| [MF Order 40/2018 approval][capitalorder] and [SFS Order 13/2025 published interpretations][capitalproof] | Approval page only for the unretained Order 40 annex; SFS questions 29.2.4.4 and 29.2.4.18 directly support the cash-receipt and inheritance-proof statements | 2026-10-30 |
| [Order 150/2018 CET18, 3 April 2026 consolidation][cet] | Scope/identity/departure, ordinary resident income/deduction/credit fields, capital table and signature/acceptance instructions; complete current form attachment and remaining nonresident fields are not certified | 2026-10-30 |
| [Government Decision 697/2014, 2026 payroll regulation][reg] | Applications, exemptions/evidence and cumulative payroll method; attached forms and image formula remain limited as stated in payroll Guide | 2026-10-30 |
| [CNAS 2026 instructions][cnas] | Contribution categories, actual fixed amounts and forecast salary input; not a substitute for individual income-tax entitlement | 2026-10-30 |
| [Medical budget Law 321/2025 art. 4][medicalbudget] | Current eligible 2,527/12,636 and 9% category rules; 2,572 overview discrepancy not adopted | 2026-10-30 |
| [Law 489/1999][social]; [Law 1593/2002][health] | Selected social/medical framework retained in the connected Guide/ledger; full amendment/implementing-chain gaps remain explicit there | 2026-10-30 |

Not yet confirmed: complete 2026 commencement chain beyond the selected January/current transitions, including the retail-registration cut-off amendment's enactment/application history; approved UNIF/professional return instructions and every special-regime registration/cessation/notification procedure; current CET18 attachment/portal handling of the 20,000 education cap versus generic point 34^7, the full separate Order 40 capital-cost document list beyond the cited inheritance/receipt interpretation; remaining individual-business home-office/mixed-use, car, bad-debt and charity implementation beyond the statutory tests and the corporate companion’s sourced ordinary travel/asset/benefit methods; unavailable annex values and actual forms remain gaps; voluntary pension/annuity and other specialist deductions; annual form implementation of unused/birth/death-dependent relief, including the apparent tension between regulation point 33 and Code art. 35(4), whose statutory next-month rule controls this draft; precise lottery/sports/online and exceptional final-withholding implementation; all tax/social treaty agreements, posting certificates and foreign-tax refund procedures; full offence/appeal implementation and taxpayer-specific historic medical-penalty transitions; all IT-park/software-worker/special incentive methods. The old 2025 minimum 5,500/forecast 16,100, fixed social 20,518 or justice 27,772 and monthly rounding claims are historical/unconfirmed for their own year, not reused as 2026 rates. Old VAT 20% and registration 1.2/1.5/1.7-million claims require the VAT Guide's statutory reconciliation. All predecessor rules/examples are retained, corrected or explicitly unconfirmed in the destination ledger. Ordinary gaps and whole-country independent review keep this domain partial.

[code]: https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro
[jan]: https://www.legis.md/cautare/getResults?doc_id=149766&lang=ro
[cet]: https://www.legis.md/cautare/getResults?doc_id=153807&lang=ro
[reg]: https://www.legis.md/cautare/getResults?doc_id=152473&lang=ro
[cnas]: https://cnas.gov.md/sites/default/files/2026-10/Particularitati2026.pdf
[medicalbudget]: https://www.legis.md/cautare/getResults?doc_id=156542&lang=ro
[social]: https://www.legis.md/cautare/getResults?doc_id=156677&lang=ro
[health]: https://www.legis.md/cautare/getResults?doc_id=152955&lang=ro

[personalreg]: https://www.legis.md/cautare/getResults?doc_id=154927&lang=ro
[personalregjan]: https://www.legis.md/cautare/getResults?doc_id=150441&lang=ro
[personalamend]: https://www.legis.md/cautare/getResults?doc_id=154909&lang=ro
[capitalorder]: https://www.legis.md/cautare/getResults?doc_id=105006&lang=ro
[capitalproof]: https://www.sfs.md/ro/ordinele-de-baze-de-date-de-generalizare/1215

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
