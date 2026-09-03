---
name: za-income-tax
description: Use this skill whenever asked about South African income tax for self-employed individuals. Trigger on phrases like "how much tax do I pay", "ITR12", "income tax return", "SARS", "tax brackets", "provisional tax", "IRP6", "rebates", "medical credits", "retirement deduction", "turnover tax", "eFiling", or any question about filing or computing income tax for a self-employed or sole proprietor client in South Africa. ALWAYS read this skill before touching any South African income tax work.
version: 2.0
jurisdiction: ZA
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: Werner Britz
review_status: current
tier: 1
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# ZA Income Tax

## South Africa Income Tax -- Self-Employed Skill v2.0

## Verified rates & thresholds (accountant-reviewed)

Reviewed against the cited tax authorities by Werner Britz on 2026-06-12. Items flagged for further clarification are tracked separately and excluded here. This block is generated from verified skill_facts — edit the facts, not the prose.

### Income Tax

- **Country** — South Africa
- **Tax type** — Income tax (normal tax) on trade income
- **Primary legislation** — Income Tax Act 58 of 1962
- **Supporting legislation** — Tax Administration Act 28 of 2011; Sixth Schedule (Turnover Tax); Fourth Schedule (Provisional Tax)
- **Tax authority** — SARS
- **Filing portal** — Correct portal but URL is sarsefiling.gov.za / efiling.sars.gov.za. The www.sarsefiling.co.za address is the older registered domain that redirects, but for documentation use https://www.sarsefiling.gov.za or https://www.sars.gov.za.  _(SARS website)_
- **Currency** — ZAR only
- **Tax year** — 1 March - 28 February  _(Income Tax Act s 1, definition)_
- **Return form** — ITR12
- **Provisional tax** — IRP6 (1st: 31 Aug, 2nd: last day Feb, 3rd voluntary: 30 Sep)  _(Income Tax Act Fourth Schedule)_
- **Primary rebate** — 2026/27 (YoA 2027): R17,820.  _([SARS — Rates of Tax for Individuals, 2027 tax year (read 2026-09-02)](https://www.sars.gov.za/tax-rates/income-tax/rates-of-tax-for-individuals/))_
- **Secondary rebate (65+)** — 2026/27: R9,765.  _([SARS — Rates of Tax for Individuals, 2027 tax year (read 2026-09-02)](https://www.sars.gov.za/tax-rates/income-tax/rates-of-tax-for-individuals/))_
- **Tertiary rebate (75+)** — 2026/27: R3,249.  _([SARS — Rates of Tax for Individuals, 2027 tax year (read 2026-09-02)](https://www.sars.gov.za/tax-rates/income-tax/rates-of-tax-for-individuals/))_
- **Retirement fund deduction** — Cap increased from R350,000 to R430,000 for years of assessment commencing on or after 1 March 2026 (Budget 2026). The 27.5% rate and "greater of remuneration or taxable income" base remain.  _(Income Tax Act s 11F; SARS Budget 2026 Tax Guide)_
- **Turnover tax** — Turnover limit increased to R2,300,000 from 1 March 2026 (aligned with new VAT registration threshold). Brackets also moved - see Section 1 turnover tax row below.  _(Income Tax Act Sixth Schedule; SARS Budget 2026 Tax Guide)_
- **Contributor** — Open Accountants Community

Update after sign-off by Werner Britz CA(SA).

- **R1 - R237,100 (skill)** — 2026/27 (YoA 2027): R1 - R245,100 at 18%.  _([SARS — Rates of Tax for Individuals, 2027 tax year (read 2026-09-02)](https://www.sars.gov.za/tax-rates/income-tax/rates-of-tax-for-individuals/))_
- **R237,101 - R370,500 (skill)** — 2026/27: R245,101 - R383,100. Tax R44,118 + 26% of excess above R245,100.  _([SARS — Rates of Tax for Individuals, 2027 tax year (read 2026-09-02)](https://www.sars.gov.za/tax-rates/income-tax/rates-of-tax-for-individuals/))_
- **R370,501 - R512,800** — 2026/27: R383,101 - R530,200. Tax R79,998 + 31% of excess above R383,100.  _([SARS — Rates of Tax for Individuals, 2027 tax year (read 2026-09-02)](https://www.sars.gov.za/tax-rates/income-tax/rates-of-tax-for-individuals/))_
- **R512,801 - R673,000** — 2026/27: R530,201 - R695,800. Tax R125,599 + 36% of excess above R530,200.  _([SARS — Rates of Tax for Individuals, 2027 tax year (read 2026-09-02)](https://www.sars.gov.za/tax-rates/income-tax/rates-of-tax-for-individuals/))_
- **R673,001 - R857,900** — 2026/27: R695,801 - R887,000. Tax R185,215 + 39% of excess above R695,800.  _([SARS — Rates of Tax for Individuals, 2027 tax year (read 2026-09-02)](https://www.sars.gov.za/tax-rates/income-tax/rates-of-tax-for-individuals/))_
- **R857,901 - R1,817,000** — 2026/27: R887,001 - R1,878,600. Tax R259,783 + 41% of excess above R887,000.  _([SARS — Rates of Tax for Individuals, 2027 tax year (read 2026-09-02)](https://www.sars.gov.za/tax-rates/income-tax/rates-of-tax-for-individuals/))_
- **R1,817,001+** — 2026/27: R1,878,601+. Tax R666,339 + 45% of excess above R1,878,600.  _([SARS — Rates of Tax for Individuals, 2027 tax year (read 2026-09-02)](https://www.sars.gov.za/tax-rates/income-tax/rates-of-tax-for-individuals/))_
- **Below 65** — 2026/27: R99,000.  _(SARS Budget 2026 Tax Guide)_
- **65 - 74** — 2026/27: R153,250.  _([SARS — Rates of Tax for Individuals, 2027 tax year (read 2026-09-02)](https://www.sars.gov.za/tax-rates/income-tax/rates-of-tax-for-individuals/))_
- **75+** — 2026/27: R171,300.  _([SARS — Rates of Tax for Individuals, 2027 tax year (read 2026-09-02)](https://www.sars.gov.za/tax-rates/income-tax/rates-of-tax-for-individuals/))_
- **Main member monthly** — 2026/27: R376.  _(SARS Budget 2026 Tax Guide)_
- **First dependant monthly** — 2026/27: R376.  _(SARS Budget 2026 Tax Guide)_
- **Each additional monthly** — 2026/27: R254.  _(SARS Budget 2026 Tax Guide)_
- **R0 - R335,000** — 2026/27: R0 - R600,000 at 0%. Major rebanding effective 1 March 2026.  _(Income Tax Act Sixth Schedule; SARS Budget 2026 Tax Guide)_
- **R335,001 - R500,000** — 2026/27: R600,001 - R950,000 at 1% above R600,000.  _(Sixth Schedule; SARS Budget 2026 Tax Guide)_
- **R500,001 - R750,000** — 2026/27: R950,001 - R1,400,000 at R3,500 + 2% above R950,000.  _(Sixth Schedule; SARS Budget 2026 Tax Guide)_
- **R750,001 - R1,000,000** — 2026/27: R1,400,001 - R2,300,000 at R12,500 + 3% above R1,400,000. Turnover ceiling raised from R1m to R2.3m.  _(Sixth Schedule; SARS Budget 2026 Tax Guide)_
- **Unknown age** — STOP - age determines rebates and threshold
- **Unknown expense category** — Not deductible
- **Unknown business-use proportion** — 0%
- **Unknown whether home office qualifies** — Not deductible (IN 28 strict)  _(SARS IN 28 (Issue 3, March 2022))_
- **Entertainment expenses** — See summary critical finding #8. s 23(m) restricts deductions against EMPLOYMENT income and income from holding an OFFICE; it does NOT restrict deductions against trade income of a sole proprietor. Entertainment for a sole proprietor is tested under the general deduction formula (s 11(a) plus s 23(g)): is the expenditure actually incurred in the production of income and not of a domestic, private, or capital nature? Client lunches that are bona fide marketing or business development may be deductible. The VAT block on entertainment (s 17(2)(a) VAT Act) is a separate rule and applies to all vendors. Reword the default to: "Entertainment: critically review under s 11(a) and s 23(g); conservatively disallow if no clear nexus to income production".  _(Income Tax Act s 11(a), s 23(g), s 23(m); VAT Act s 17(2)(a))_

Bank statement for the tax year. Acceptable from: FNB, Standard Bank, Nedbank, Absa, Capitec, Investec, Discovery Bank, TymeBank, fintech (Revolut, Wise)

Invoices, IRP6 payment records, medical aid statements, RA contribution certificates, vehicle logbook

Complete bookkeeping, prior year ITR12, IT34 (assessment), asset register

- **R-ZA-1: Company/CC/Trust** — This skill covers sole proprietors only. Companies file ITR14 at 27%. Trusts file ITR12T.  _(Income Tax Act s 5 and rates schedule)_
- **R-ZA-2: Foreign income** — Correct as refusal but reference is to s 10(1)(o)(ii) - the exemption for employment income earned outside SA for more than 183 days. Note the R1.25m cap was introduced in 2020. For sole proprietor trade income earned outside SA, residency and DTA rules apply (s 9D for CFCs). Different rule.  _(Income Tax Act s 10(1)(o)(ii); s 6quat; relevant DTAs)_
- **R-ZA-3: Capital gains tax** — Reasonable refusal as scope decision, but CGT events on business assets are common in sole prop work (disposal of equipment, sale of practice). Even if computation is outside scope, the skill should flag CGT triggers. Annual exclusion R40,000 (R300,000 in year of death); inclusion rate 40% for individuals. Primary residence exclusion R2m (R3m from 1 March 2026).  _(Income Tax Act Eighth Schedule; SARS Budget 2026 Tax Guide)_
- **R-ZA-4: Age unknown** — Cannot compute without age  _(Income Tax Act s 6 and s 10(1)(i))_
- **FNB, FIRST NATIONAL BANK - Bank charges** — Deductible. Business account fees  _(Income Tax Act s 11(a))_
- **STANDARD BANK, SBSA** — Bank charges deductible
- **NEDBANK** — Bank charges deductible
- **ABSA** — Bank charges deductible
- **CAPITEC** — Bank charges deductible
- **INVESTEC** — Bank charges deductible
- **DISCOVERY BANK, TYMEBANK** — Bank charges deductible
- **REVOLUT, WISE (fees)** — Deductible. Fintech fees
- **INTEREST (credit)** — Taxable income up to exemption (R23,800 <65; R34,500 65+); excess taxable  _(Income Tax Act s 10(1)(i))_
- **INTEREST (debit)** — Deductible if business loan; personal not deductible  _(Income Tax Act s 11(a), s 24J)_
- **LOAN, HOME LOAN (principal)** — EXCLUDE - principal movement
- **SARS** — EXCLUDE. Tax payment (provisional/income)
- **UIF, UNEMPLOYMENT INSURANCE** — Deductible if employer contribution. Employee-related  _(Unemployment Insurance Contributions Act)_
- **COIDA, COMPENSATION FUND** — Deductible  _(COIDA s 80)_
- **CIPC** — CIPC fees specifically related to ongoing trade (annual returns for the trade form, name changes, etc.) are deductible. Initial CIPC fees for incorporation are CAPITAL and not deductible (s 23(g)). For a sole proprietor, this is less relevant - sole props do not register with CIPC. The skill seems to assume the sole prop has a company, which would put them outside scope per R-ZA-1.  _(Income Tax Act s 23(g))_
- **ESKOM, CITY POWER, CITY OF [JHB/CPT/DBN]** — Conflates two different items. (1) ELECTRICITY (Eskom or municipal): deductible to the extent used in production of income; apportion home use. (2) RATES (property rates on a municipal bill): only deductible to the extent the property is used for trade, in proportion. For a home office user, rates are deductible only to the extent of the qualifying office area. Bundle on a single municipal bill: split rates from electricity from water from refuse.  _(Income Tax Act s 11(a); SARS IN 28)_
- **RAND WATER** — Deductible if business premises. Water  _(Income Tax Act s 11(a))_
- **VODACOM, MTN, CELL C, TELKOM, RAIN** — Deductible: business phone/internet. Mixed: apportion  _(Income Tax Act s 11(a))_
- **HOLLARD, SANTAM, OLD MUTUAL, MOMENTUM, OUTSURANCE** — Skill's row covers asset and short-term business insurance correctly. Three important related items are NOT addressed and frequently asked: KEY-PERSON / KEY-MAN insurance, income protection, and group risk cover. KEY-PERSON INSURANCE - s 11(w) framework (post-1 March 2012): three structures with very different consequences. (1) Section 11(w)(i) - "employer-paid for benefit of employee" (group life, etc.): Premiums DEDUCTIBLE for employer. Premium amount taxed as fringe benefit to the employee under para 2(k) Seventh Schedule. Effectively neutral (deduction = fringe benefit value). Proceeds taxed in employee's hands (or estate) depending on structure. (2) Section 11(w)(ii) - "conforming" key-person policy (employer is policyholder AND beneficiary): Requires (a) pure risk policy with NO cash or surrender value; (b) policy is property of the employer at time of premium payment (may be ceded as security to creditor but not assigned to employee); (c) policy agreement EXPLICITLY states that s 11(w)(ii) applies (or addendum to that effect for pre-March 2012 policies, by 31 August 2012). If election made: Premiums DEDUCTIBLE. Proceeds INCLUDED IN GROSS INCOME under para (m) of the "gross income" definition - fully taxable to the employer. (3) "Non-conforming" policy - DEFAULT if no s 11(w)(ii) election is made: Premiums NOT deductible. Proceeds EXEMPT under s 10(1)(gH) - tax-free to the employer. This is the more common structure since the 2012 amendments because (a) the cover amount needed is lower (no need to gross up for tax on payout); (b) insurers default to this unless client specifically opts in. Practitioner decision matrix: Choose CONFORMING (s 11(w)(ii)) if: company has high taxable income now wanting current deduction; expected to pay out relatively soon; comfortable that proceeds will be taxable. Choose NON-CONFORMING if: client wants tax-free payout (most cases); cash flow is fine without the upfront premium deduction; intention is to use proceeds to recover the loss of the key person (capital in nature). CONTINGENT LIABILITY POLICIES (surety cover): Post-March 2012, generally NOT deductible (SARS treats as capital expenditure). ASISA/Sanlam Group withdrew tax-deductible contingent liability plans after the 2012 amendments. BUY-AND-SELL POLICIES (funding shareholder buy-out): Typically structured as non-conforming. Premiums non-deductible; proceeds tax-free; policy excluded from deceased's estate under s 3(3)(a)(iA) Estate Duty Act if requirements met (risk policy with no surrender value, all premiums paid by partners/co-shareholders, proceeds used to acquire the interest). INCOME PROTECTION INSURANCE: NOT deductible under s 23(p) (specific prohibition since 2015). Proceeds (when paid) are exempt under s 10(1)(gI). The opposite of the pre-2015 position. SHORT-TERM ASSET INSURANCE (Hollard, Santam, OUTsurance covering business vehicles, premises, public liability, etc.): Deductible under s 11(a) where directly relating to trade. Insurance proceeds for damaged business assets are recoupments under s 8(4)(a) - taxable to extent of allowances previously claimed. PERSONAL LIFE INSURANCE / RETIREMENT ANNUITY (NOT key-person): premiums NOT deductible (RA is separately deductible under s 11F up to the cap). Proceeds tax-free.  _(Income Tax Act s 11(w)(i) and s 11(w)(ii); s 10(1)(gH); s 23(p); s 8(4)(a); s 11F; para (m) of "gross income" definition; Seventh Schedule para 2(k); Estate Duty Act s 3(3)(a)(iA); PKF SA "Key man insurance policy tax"; SAICA Integritax 1209; Dommisse Attorneys (2020); G&S Insurance Consultants commentary; SAIT "Taxation of benefits in respect of insurance policies")_
- **DISCOVERY HEALTH, BONITAS, GEMS, MEDIHELP** — NOT deductible from income. Medical = s6A/s6B credits  _(Income Tax Act s 6A and s 6B)_
- **GOOGLE, MICROSOFT, ADOBE, META** — Deductible expense. Foreign SaaS  _(Income Tax Act s 11(a))_
- **GITHUB, OPENAI, ANTHROPIC** — Deductible expense. Non-EU
- **SLACK, ZOOM, ATLASSIAN** — Deductible expense. Check entity
- **ACCOUNTANT, AUDIT, CA(SA)** — Deductible. Accounting/audit fees  _(Income Tax Act s 11(a))_
- **ATTORNEY, ADVOCATE, LAW FIRM** — Legal fees in respect of trade income are deductible. Capital-nature legal fees (acquisition of business, defence of title to capital asset) are not deductible under the s 23(g) prohibition on capital expenditure. Litigation costs of an income-producing nature are deductible (e.g. recovering trade debts) but defending a personal claim is not.  _(Income Tax Act s 11(a), s 23(g); Port Elizabeth Electric Tramway Co Ltd v CIR)_
- **TAX PRACTITIONER** — Deductible. Tax advisory  _(Income Tax Act s 11(a); SARS Tax Practitioner page)_
- **ALLAN GRAY, CORONATION, 10X, SYGNIA, NINETY ONE** — Cap R430,000 from 1 March 2026 (Budget 2026). Rate 27.5% unchanged. Base is "greater of remuneration or taxable income" - for sole props, remuneration is typically zero so taxable income is the base. Note: the s 11F deduction is calculated AFTER s 11A and BEFORE the s 18A donations deduction.  _(Income Tax Act s 11F; SARS Budget 2026 Tax Guide)_
- **OLD MUTUAL RA, MOMENTUM RA, LIBERTY RA** — Same. Cap R430,000.  _(Income Tax Act s 11F)_
- **KULULA, FLYSAFAIR, AIRLINK, SAA** — For INCOME TAX (the focus of this skill): full ticket cost deductible to the extent for business travel under s 11(a). Logbook or business purpose evidence required. NOTE on VAT cross-reference: input VAT on the ticket needs to be SPLIT by component - not all lines on the e-ticket carry VAT (base fare + fuel + PSC + insurance = 15%; SACAA + ATNS + Air Passenger Tax = no VAT). Income tax deduction does not depend on this split. Update for carriers: Kulula ceased 2022, Mango ceased 2021. Add: Lift, CemAir, FlyAirlink, FlyNamibia for regional/SA carriers.  _(Income Tax Act s 11(a); VAT Act s 11(2)(a) and s 12 (cross-reference); Customs and Excise Act s 47B)_
- **UBER, BOLT** — For income tax (which the skill addresses): rider fares deductible to the extent for trade purposes, fine. Need invoice plus business-purpose evidence. NOTE on VAT (cross-reference): the Uber/Bolt fare is EXEMPT under s 12(g) of the VAT Act, so no input VAT is claimable on the fare even by a VAT-registered business rider. Practical only for income tax. Drivers themselves: their fare income is also exempt from VAT, so they register for VAT only if they have non-fare income (incentives, referrals, marketing services) exceeding the threshold. Source: VAT Act s 12(g); Uber SA driver tax page.  _(Income Tax Act s 11(a); VAT Act s 12(g) and s 54 (cross-reference))_
- **ENGEN, SHELL, BP, SASOL, CALTEX, TOTAL** — Deductible: business vehicle portion only. Fuel; requires logbook  _(Income Tax Act s 11(a))_
- **AVIS, EUROPCAR, HERTZ** — For income tax: deductible to the extent for business. NOTE for VAT: input VAT on car rental of a "motor car" is BLOCKED under s 17(2)(c) VAT Act. The skill is income tax only and the income tax position is correct, but a practitioner should flag the VAT block when reviewing the same expense under both regimes.  _(Income Tax Act s 11(a); VAT Act s 17(2)(c) (cross-reference))_
- **SANRAL, E-TOLL** — e-tolls were effectively discontinued on the Gauteng Freeway Improvement Project (GFIP) on 12 April 2024. SANRAL toll plaza fees on the N1, N2, N3 etc. still apply.
- **INCREDIBLE CONNECTION, MATRIX, TAKEALOT** — Refined rule: ITEMS COSTING R7,000 OR LESS each: full write-off in year of acquisition under SARS BGR 7 (small-value assets full write-off). The asset is brought into use for purposes of trade and is not part of a set. CRITICAL "SET" RULE under BGR 7: cannot artificially break a single asset/set into sub-components to bring them below R7,000. A "set" is a number of items that function as a single unit (e.g. a dining table with six matching chairs; a set of matching office furniture; a complete computer with its specific monitor, keyboard, and mouse all purchased together as a configured unit). The cost of the set is aggregated for the R7,000 test. Items that are independently functional and not part of a configured set (e.g. five separate laptops bought at the same time for five employees, each functionally independent) are tested individually. ITEMS COSTING ABOVE R7,000 each (or sets aggregated above R7,000): wear-and-tear under s 11(e), straight-line over the SARS useful life per IN 47 (Issue 5). Common useful lives: computers 3 years; office furniture 6 years; office equipment 5 years; cellular phones 2 years; printers 3 years. Apportion for part-year use. ENHANCED ALLOWANCES (where applicable): s 12C for manufacturing plant (40/20/20/20 over four years for new/unused); s 12E for Small Business Corporations on new manufacturing plant (100% in year of acquisition - but s 12E is for companies, not sole proprietors); s 12B for renewable energy assets (see new row below).  _(Income Tax Act s 11(e); SARS BGR 7 (small-value assets); SARS IN 47 (Issue 5, March 2023); s 12B; s 12C; s 12E)_
- **OFFICE NATIONAL, WALTONS** — Deductible. Stationery
- **POSTNET, SA POST OFFICE** — SA Post Office was placed in business rescue in mid-2023 and provisional liquidation in mid-2025. Practical availability is limited. PostNet and TCG (The Courier Guy) still operate.
- **MAKRO, GAME** — Deductible if business supplies. Verify business purpose
- **PICK N PAY, WOOLWORTHS, CHECKERS, SPAR, SHOPRITE** — For a sole proprietor, the right test is the general deduction formula (s 11(a) read with s 23(g)): is the expenditure actually incurred in the production of income and not of a domestic, private, or capital nature? DEDUCTIBLE for income tax (sole prop) where genuine trade purpose exists: - Office tea, coffee, milk, sugar, biscuits provided to clients during consultations or meetings, or to staff during working hours (staff sustenance) - Bottled water in client meeting rooms - Refreshments at training sessions, workshops - Catering for client functions where the function is business development - Supplies for a catering business, restaurant, B&B (resale stock) NOT DEDUCTIBLE: pure personal grocery shopping; family meals; entertainment with no business nexus; alcohol for staff without trade purpose. CROSS-REFERENCE - VAT TREATMENT IS DIFFERENT: even where income tax allows the deduction (legitimate office tea/coffee), the VAT INPUT is BLOCKED under s 17(2)(a) as entertainment UNLESS the vendor is in the entertainment trade. So a typical sole prop deducts office groceries for income tax but cannot claim the VAT input. The two regimes do not move together. PRACTICAL: keep proper records - itemised receipts and notes confirming business purpose. SARS may query large grocery deductions for individuals.  _(Income Tax Act s 11(a) and s 23(g); VAT Act s 17(2)(a) (cross-reference); SARS Comprehensive Guide to the ITR12)_
- **RESTAURANT (any)** — See critical finding #8: s 23(m) does NOT apply to sole proprietors - it restricts deductions against employment income and income from holding an office. Sole prop restaurant spending tested under s 11(a) and s 23(g). DEDUCTIBLE for income tax (sole prop) where genuine trade purpose: bona fide client business development meals; meetings with clients where business is the substantial purpose; subsistence while travelling on business away from usual place of work. Practitioner should retain: date, who attended, business purpose, what was discussed. NOT DEDUCTIBLE: pure personal/social meals labelled as "client entertainment" without real business purpose; meals with family branded as business. CROSS-REFERENCE - VAT: restaurant VAT input is BLOCKED under s 17(2)(a) entertainment for the buying business. Only the restaurant itself can claim its own input on its inputs (since it IS in the entertainment trade). Income tax deduction does not depend on VAT treatment.  _(Income Tax Act s 11(a) and s 23(g); VAT Act s 17(2)(a))_
- **OWN TRANSFER, INTERNAL** — EXCLUDE - internal movement
- **DRAWINGS, OWNER** — EXCLUDE - personal drawings
- **DEPOSIT, OWN DEPOSIT** — EXCLUDE - capital injection
- **MISSING: CGT events** — Even with CGT excluded from scope (R-ZA-3), the skill should flag CGT triggers: vehicle sale, equipment disposal, sale of practice, sale of property used in trade. Pattern: large CREDIT from VEHICLE TRADER, AUCTION HOUSE, BUSINESS BUYER. Mark as "review for CGT".  _(Income Tax Act Eighth Schedule)_
- **MISSING: Donations** — Section 18A donations: deductible up to 10% of taxable income for donations to qualifying PBOs with a s 18A receipt. Common pattern: GIVENGAIN, BACKABUDDY, donation to specific charities. Need s 18A receipt with PBO number.  _(Income Tax Act s 18A)_
- **MISSING: Rental income (residential)** — Rental income from residential property is gross income for individuals. Deductions: bond interest, rates, levies, repairs (not improvements), insurance, agent commission. Add to patterns: CREDIT from "TENANT", "RENT", "PAY PROP", "RENT PROPERTY MANAGEMENT". This is a common sole prop income source.  _(Income Tax Act s 11(a); SARS IN 53 (rental))_

### Example 1: Mid-range

Computation re-run on 2026/27 SARS rates: net profit R420k; s 11F = 27.5% x R420k = R115,500 (within cap); taxable R304,500; tax R44,118 + 26% x (R304,500 - R245,100) = R44,118 + R15,444 = R59,562; less rebate R17,820 = R41,742; less medical credit R9,024 (R376 x 2 x 12) = R32,718; less provisional R40,000 = refund R7,282.

### Example 2: Turnover tax

2026/27: R650,000 turnover falls within the new R600,001 - R950,000 bracket at 1% above R600,000. Tax = 1% x R50,000 = R500. Significant reduction under new brackets.

### Example 3: Entertainment disallowed

See critical finding #8. s 23(m) does not block entertainment for sole proprietors. Test instead under s 11(a) and s 23(g). A bona fide marketing dinner with a real client where the purpose is income production may be deductible (subject to evidence). Personal social meals branded as "entertainment" are not. The right answer is "review the nexus", not "block on s 23(m)".

### Example 4: Retirement cap exceeded

2026/27 cap: R430,000. Re-run: 27.5% x R2m = R550,000, capped at R430,000. Deduction R430,000. Excess R170,000 carries forward (or adds to tax-free retirement lump sum).

### 5.1 Progressive rates

- **5.1 Progressive rates** — Apply rate table. One table for all individuals regardless of marital status  _(Income Tax Act s 5 and rates schedule)_

### 5.2 Rebates

- **5.2 Rebates** — 2026/27: Primary R17,820; Secondary R9,765 (additional, total 65+ = R27,585); Tertiary R3,249 (additional, total 75+ = R30,834). Credits against tax.  _([SARS — Rates of Tax for Individuals, 2027 tax year (read 2026-09-02)](https://www.sars.gov.za/tax-rates/income-tax/rates-of-tax-for-individuals/))_

### 5.3 Interest exemption

- **5.3 Interest exemption** — R23,800 (under 65). R34,500 (65+). Excess taxable.  _(Income Tax Act s 10(1)(i))_

### 5.4 s11F retirement deduction

- **5.4 s11F retirement deduction** — Cap R430,000 from 1 March 2026. Tax-free retirement lump sum R550,000 unchanged. Note: the "greater of" base is correctly stated, but for sole props it's almost always taxable income.  _(Income Tax Act s 11F; SARS Budget 2026)_

### 5.5 Medical tax credits (s6A)

- **5.5 Medical tax credits (s6A)** — 2026/27: R376/R376/R254.  _(Income Tax Act s 6A; SARS Budget 2026)_

### 5.6 Provisional tax (IRP6)

- **5.6 Provisional tax (IRP6)** — See Provisional Tax sheet for detail. From years of assessment commencing on or after 1 March 2026, the basic-amount safe harbour threshold is R1.8m (up from R1m). The 20% underestimation penalty also applies where the estimate is within tolerance but the payment is late (Budget 2026).  _(Income Tax Act Fourth Schedule; SARS Budget 2026)_

### 5.7 Turnover tax

- **5.7 Turnover tax** — Turnover ceiling R2.3m from 1 March 2026 (aligned with VAT registration threshold). The "non-professional services" framing is rough: the exclusion is for personal service providers (s 12E and Sixth Schedule). Turnover tax DOES replace income tax and CGT - the dividends tax inclusion is correct only insofar as dividends paid to shareholders of a micro business company carry tax under the special rules. Turnover tax does NOT replace VAT - a turnover tax taxpayer can still register voluntarily for VAT if they meet the criteria, although typically they would not register as they fall below the threshold.  _(Income Tax Act Sixth Schedule; s 12E)_

### 5.8 Wear-and-tear (s11(e))

- **5.8 Wear-and-tear (s11(e))** — IN 47 useful life IS straight-line over the period, just that the period is taken from the IN 47 table rather than being chosen by the taxpayer. The correct framing: the deduction is "such sum as the Commissioner thinks just and reasonable" representing wear-and-tear, by reference to IN 47 useful lives applied straight-line. Apportionment for part-year use. Small assets <R7,000 fully written off in year of acquisition under BGR 7.  _(Income Tax Act s 11(e); SARS IN 47; BGR 7)_

### 5.9 Entertainment

- **5.9 Entertainment** — See critical finding #8 and rows above. s 23(m) restricts EMPLOYMENT and OFFICE-HOLDER deductions, not sole prop trade deductions. Sole prop entertainment is tested under s 11(a) and s 23(g): bona fide trade purpose, not domestic/private.  _(Income Tax Act s 11(a), s 23(g), s 23(m))_

### 5.10 Home office

- **5.10 Home office** — Substantive position correct but list of expenses missing. s 23(b) requirements: (1) part of a residence occupied for trade; (2) specifically equipped for trade; (3) regularly and exclusively used for trade; (4) (for salaried employees only) duties are mainly performed there. Permitted expenses (apportioned): rent OR bond INTEREST (not capital repayments); rates and taxes; levies; electricity; water; cleaning; repairs to office portion; wear-and-tear on office-only equipment claimed in full. Formula: A/B x premises costs where A=area of office, B=total area of residence. CRITICAL CGT CONSEQUENCE (missing from skill): the area used for trade is "tainted" - on disposal of the residence, the primary residence exclusion (R2m / R3m from 1 March 2026) does NOT apply to the tainted portion; the gain is apportioned by area and period of trade use, and the tainted portion is fully subject to CGT with only the annual exclusion (R40k) available. Practitioners must warn clients before they first claim home office. Many clients consider claiming home office and then find on sale that they have generated CGT that exceeds the lifetime income tax savings.  _(Income Tax Act s 11(a), s 23(b); SARS IN 28 (Issue 3, March 2022); Eighth Schedule para 47)_

### 5.11 Record keeping

- **5.11 Record keeping** — 5 years from submission. Invoices, receipts, bank statements, logbooks, asset register.  _(TAA s 29 to s 32)_

### 6.1 Home office qualification

- **6.1 Home office qualification** — Add the CGT consequence (see 5.10 above). Also add the four s 23(b) requirements explicitly.  _(Income Tax Act s 23(b); IN 28)_

### 6.2 Motor vehicle logbook

- **6.2 Motor vehicle logbook** — Default 0% business use. Question: do you have logbook?  _(SARS Travel Allowance Guide; Income Tax Act s 8(1))_

### 6.3 Turnover tax vs normal tax

Depends on expense level and qualification. Present both.

### 6.4 s6B additional medical expenses

- **6.4 s6B additional medical expenses** — Formula: (a) 65+ or qualifying disability: 33.3% of medical scheme contributions in excess of 3 x s 6A credit, PLUS 33.3% of qualifying out-of-pocket medical. (b) Under 65 without disability: 25% of (excess medical scheme + qualifying OOP) over 7.5% of taxable income. Computational rule should be in the skill rather than escalated wholesale.  _(Income Tax Act s 6B)_

### 6.5 Bad debts

- **6.5 Bad debts** — Add: s 11(i) bad debt deduction - amount must have been included in income (so cash-basis taxpayer cannot claim bad debt; only accrual-basis taxpayers). Doubtful debt allowance under s 11(j) (revised in 2019 - now formulaic based on age of debt: 25% of debt aged 60-90 days, 40% over 90 days, with conditions). Provide the rule, not just "escalate".  _(Income Tax Act s 11(i) and s 11(j); SARS Notice 1209 (15 Nov 2019))_

### MISSING: Wear-and-tear and small assets

- **MISSING: Wear-and-tear and small assets** — Add a Tier 2 entry walking through the s 11(e) decision: (a) is it a capital asset used in trade? (b) cost under R7,000 - full write-off in year (BGR 7); (c) over R7,000 - IN 47 useful life, straight-line; (d) section 12C accelerated 40/20/20/20 for manufacturing plant; (e) s 12E small business corporation 100% on new manufacturing plant.  _(Income Tax Act s 11(e), s 12C, s 12E; SARS IN 47; BGR 7)_

### MISSING: Travel allowance / motor vehicle deduction

- **MISSING: Travel allowance / motor vehicle deduction** — For sole props using a personal vehicle for trade: deduct actual business-portion costs (fuel, repairs, insurance, finance interest, wear-and-tear at 4-year SARS rate). Maintain logbook. Alternative deemed cost: vehicle cost x fixed cost rate per Government Gazette tables. For employees with a travel allowance, different rules apply (s 8(1)(b)) but those are outside scope.  _(Income Tax Act s 11(a); SARS Travel Allowance Guide)_

### Transactions sheet structure

Columns: Date, Counterparty, Description, Amount, Category, Deductible amount, Default, Question, Notes

### ITR12 Computation sheet

Step-by-step per Section 5: gross income, deductions, taxable income, tax, rebates, medical credits, provisional tax offset

### CSV formats

FNB DD/MM/YYYY comma. Standard Bank semicolons. Nedbank, Absa various.

### DEBICHECK

- **DEBICHECK** — Authenticated debit order

### MAGTAPE

- **MAGTAPE** — Batch payment

### SASWITCH

- **SASWITCH** — ATM network

### PREPAID

- **PREPAID** — Likely personal (airtime top-up)

### MUNICIPALITY

- **MUNICIPALITY** — Same nuance as utilities: municipality bill typically combines rates (deductible to extent of trade use) with electricity/water/refuse (deductible to extent of trade use). Split the line.

### Provisional tax payments

- **Provisional tax payments** — EXCLUDE - tax payment not expense

### Medical aid debits

- **Medical aid debits** — NOT income deduction - generate s6A credits  _(Income Tax Act s 6A)_

### RA contributions

- **RA contributions** — Cap R430,000 from 1 March 2026.  _(Income Tax Act s 11F)_

### 9.1 Age

Update to "28 February 2027" for the current tax year of assessment.

### 9.2 Residency

- **9.2 Residency** — SA bank accounts suggest resident. Ask: are you a SA tax resident?  _(Income Tax Act s 1, definition of "resident")_

### 9.3 Business type

From counterparty patterns. Ask: trade/profession?

### 9.4 Turnover tax election

- **9.4 Turnover tax election** — Ask: have you elected turnover tax?  _(Sixth Schedule)_

### 9.5 Medical aid

Ask: medical aid, how many dependants?

### 9.6 RA contributions

Monthly RA debits inference. Ask: RA contributions?

### 9.7 Provisional tax paid

Ask: IRP6 amounts paid?

### MISSING: Other income sources

- **MISSING: Other income sources** — Add: dividends (DWT or exempt SA), rental, royalties, annuities, foreign income, capital gains, sale of business. These all affect taxable income.

### MISSING: Spouse and dependants

- **MISSING: Spouse and dependants** — Spouse status affects: medical credits (often combined); donations between spouses (free); CGT primary residence exclusion (one per family unit); some other reliefs.  _(Income Tax Act s 6A, s 56, Eighth Schedule)_

### MISSING: Section 18A donations

- **MISSING: Section 18A donations** — Section 18A deduction up to 10% of taxable income. Often missed.  _(Income Tax Act s 18A)_

### Test suite

All tests use 2025/26 rates and the R350k RA cap. Re-run on 2026/27 basis to validate the skill at current rates.

### Edge case registry

- **Edge case registry** — EC9 (entertainment under s 23(m)) is wrong - see critical finding #8. EC4 (home office dual use) is right on income tax but should also flag CGT consequence. EC10 (assessed loss) is correct - s 20 ring-fencing rules apply (s 20A for high-income individuals - taxable income over R1.99m with prescribed loss-making trades).  _(Income Tax Act s 20, s 20A, s 23(m))_

### NEVER compute without knowing age

- **NEVER compute without knowing age** — NEVER compute without knowing age

### NEVER apply tax below age-threshold

- **NEVER apply tax below age-threshold** — NEVER apply tax below age-threshold

### NEVER allow entertainment deductions for sole proprietors

- **NEVER allow entertainment deductions for sole proprietors** — See critical finding #8. Sole prop entertainment may be deductible under s 11(a) where bona fide for trade. Should be: "Critically review entertainment against s 11(a) and s 23(g); block under VAT s 17(2)(a) is a separate issue".  _(Income Tax Act s 11(a), s 23(g))_

### NEVER deduct RA above R350,000 cap

- **NEVER deduct RA above R350,000 cap** — Cap R430,000 from 1 March 2026.  _(Income Tax Act s 11F)_

### NEVER allow turnover tax for professional services

- **NEVER allow turnover tax for professional services** — NEVER allow turnover tax for professional services  _(Sixth Schedule)_

### NEVER use prior year income for provisional tax

- **NEVER use prior year income for provisional tax** — Prior year income is the "basic amount" benchmark for the safe harbour and underestimation penalty calculation - it is used as a reference, not as the literal estimate. The skill's underlying point (must estimate current year, not blindly reuse prior year) is correct.  _(Fourth Schedule para 19 and para 20)_

### NEVER treat medical credits as income deductions

- **NEVER treat medical credits as income deductions** — NEVER treat medical credits as income deductions

### NEVER allow home office for dual-use rooms

- **NEVER allow home office for dual-use rooms** — NEVER allow home office for dual-use rooms  _(SARS IN 28)_

### NEVER allow income tax as a deduction

- **NEVER allow income tax as a deduction** — NEVER allow income tax as a deduction  _(Income Tax Act s 23(d))_

### NEVER present calculations as definitive

- **NEVER present calculations as definitive** — NEVER present calculations as definitive

### MISSING prohibition: home office CGT consequence

- **MISSING prohibition: home office CGT consequence** — Add: "Never claim home office without warning the client of the CGT consequence on disposal of the residence."  _(Eighth Schedule para 47)_

### Income Tax Act 58 of 1962

### Tax Administration Act 28 of 2011

### SARS Interpretation Notes (IN 28, IN 47, IN 14)

- **SARS Interpretation Notes (IN 28, IN 47, IN 14)** — Add: IN 47 (wear-and-tear) currently in Issue 5 (March 2023). IN 28 (home office) Issue 3 (March 2022). IN 14 (allowances and reimbursements) Issue 4. Also add: IN 1 (provisional tax estimates), IN 33 (assessed losses), BGR 7 (small assets), BGR 9 (utility apportionment), BGR 24 (allowances and reimbursements).  _(SARS Legal Counsel publications)_

### SARS eFiling URL

Current canonical URLs: https://www.sarsefiling.gov.za or https://www.sars.gov.za.

### Disclaimer

Standard wording.

### MISSING: s 11A - Pre-trade expenditure

- **MISSING: s 11A - Pre-trade expenditure** — Section 11A allows expenditure incurred before commencement of trade to be deductible to the extent it would have been deductible under s 11 had it been incurred during the trade. Includes pre-incorporation costs, market research, initial professional fees, lease deposits (where deductible portion), opening stock, etc. The deduction is limited to income from the trade in the year it is brought to account. Any unutilised amount carries forward as an assessed loss. Common new sole prop issue.  _(Income Tax Act s 11A; SARS IN 51 (Issue 5))_

### MISSING: s 11(cA) - Restraint of trade payments

- **MISSING: s 11(cA) - Restraint of trade payments** — Section 11(cA): a taxpayer paying a restraint of trade to a natural person, labour broker, or personal service provider may deduct the payment over the LESSER of the restraint period OR 3 years (in equal annual instalments). For sole props this most commonly arises when acquiring a practice or buying out a competitor. Recipient: amount is taxable as "gross income" under para (cA) - now included in gross income since 2000 amendment. Note: for personal service provider companies, restraint may be subject to PAYE.  _(Income Tax Act s 11(cA); para (cA) of "gross income" definition)_

### MISSING: s 11D - Research and Development

- **MISSING: s 11D - Research and Development** — Section 11D: 150% deduction (100% + 50% additional) for qualifying R&D expenditure. Requires pre-approval from the Department of Science and Innovation. Aimed at innovation and new product/process development. Less commonly relevant for typical sole props but highly valuable for engineering consultants, scientific advisors, software developers producing genuine new technology. Sunset date 31 December 2033 (extended via 2024 Budget).  _(Income Tax Act s 11D; SARS IN 50)_

### MISSING: s 12B - Renewable energy assets

- **MISSING: s 12B - Renewable energy assets** — Section 12B: accelerated wear-and-tear for plant/machinery used in renewable energy generation. SOLAR PV under 1MW capacity: 100% write-off in year of bring into use - full deduction in year of acquisition under s 12B(1)(h). SOLAR PV 1MW+ and OTHER RENEWABLES (wind, hydro under 30MW, biomass): 50/30/20 over three years. TEMPORARY ENHANCED s 12BA: 125% allowance for solar PV brought into use during the limited window from 1 March 2023 to 28 February 2025 (NOW EXPIRED). Sole props with home offices or rented business premises who installed solar before 28 February 2025 should check if s 12BA was claimed. APPORTIONMENT for sole prop with home office: only the portion of solar attributable to business use (typically by reference to the home office floor area ratio under IN 28) is deductible. The household portion is private and not deductible. RECOUPMENT: on disposal of the solar asset (e.g. selling the house), recoupment applies to the business portion. Important warning to clients.  _(Income Tax Act s 12B and s 12BA; SARS Renewable Energy Tax Incentive FAQ)_

### MISSING: s 12C - Manufacturing plant accelerated wear and tear

- **MISSING: s 12C - Manufacturing plant accelerated wear and tear** — Section 12C: accelerated wear-and-tear for new or unused plant and machinery used in a process of manufacture. NEW OR UNUSED: 40% in year of acquisition + 20% in each of the next three years (40/20/20/20). USED PLANT: 20% straight-line over five years. Applies to manufacturing as defined - production, processing, transforming raw materials. Includes some hotel keepers and aircraft/ship owners (special sub-categories). Few sole props are in manufacturing but where applicable (workshop owners, food processing, light manufacturing), substantially better than s 11(e). Recoupment under s 8(4)(a) on disposal to extent allowances claimed.  _(Income Tax Act s 12C; SARS IN 14)_

### MISSING: s 12E - Small Business Corporation rules (cross-reference)

- **MISSING: s 12E - Small Business Corporation rules (cross-reference)** — Section 12E provides graduated tax rates and 100% wear-and-tear on new manufacturing plant for "Small Business Corporations". IMPORTANT: s 12E is available ONLY to companies and CCs (not sole proprietors and not trusts). However, the skill should mention this when discussing structure choice: a sole prop considering incorporation should weigh s 12E benefits. SBC must meet conditions: gross income under R20m; all shareholders are natural persons holding no interests in other companies; not a "personal service" provider; not more than 20% of receipts from investment income or personal services. 2026/27 SBC rates: 0% up to R95,750; 7% to R365,000; 21% to R550,000; 27% above.  _(Income Tax Act s 12E; SARS Budget 2026)_

### MISSING: s 12H - Learnership allowance

- **MISSING: s 12H - Learnership allowance** — Section 12H: additional tax deduction for employers (companies AND individuals including sole proprietors with employees) who enter into registered learnership agreements with a SETA under the Skills Development Act. Two components: annual allowance and completion allowance. Sunset date currently 31 March 2027 (extended Budget 2024). AMOUNTS for years of assessment ending on or after 1 March 2024: NQF 1-6 (lower priority NQF levels, more incentivised): R40,000 annual allowance per learner (pro-rated for part of year) PLUS R40,000 completion allowance. Total potential over a 1-year learnership: R80,000 per able-bodied learner. NQF 7-10 (higher priority - less incentive needed): R20,000 annual + R20,000 completion. Total R40,000. LEARNERS WITH DISABILITY: R60,000 annual + R60,000 completion for NQF 1-6; R50,000 + R50,000 for NQF 7-10. Requirements: (a) registered with relevant SETA before commencement (or registered within 12 months of year-end); (b) learnership pursuant to trade carried on by employer; (c) employee actually employed under formal employment contract; (d) "lead employer" claims (not the "host" employer where these are different); (e) not linked to SDL - available even to employers exempt from SDL. Allowance is IN ADDITION to the normal s 11(a) deduction for the learner's salary - so the employer effectively gets the salary deduction plus R40k-R120k per learner depending on qualifying type. Highly valuable for sole props with apprentices or learners.  _(Income Tax Act s 12H; SARS IN 20 (Issue 9, April 2025); SARS Guide on the Tax Incentive for Learnership Agreements)_

### MISSING: s 12L - Energy efficiency savings

- **MISSING: s 12L - Energy efficiency savings** — Section 12L: deduction of 95c per kWh of verified energy savings. Requires SANEDI (South African National Energy Development Institute) verification and certification. Specialist area; usually only worth pursuing for larger industrial energy users. Less common for typical sole props but should be flagged for manufacturing/processing operations.  _(Income Tax Act s 12L; Regulations on Energy Efficiency Savings)_

### MISSING: s 13 - Commercial / industrial buildings

- **MISSING: s 13 - Commercial / industrial buildings** — Section 13: 5% straight-line annual allowance on new buildings used wholly or mainly for manufacturing/research, hotel operations, qualifying purposes. Section 13quin: 5% on new commercial buildings (offices, retail, warehouses) - costs incurred from 1 April 2007. Section 13sex: residential rental units - 5% (10% in low-cost housing context) on new units owned by the taxpayer for letting where the taxpayer owns at least 5 such units. Section 13quat: 20% / 8% UDZ allowance in urban development zones (sunset date 31 March 2025 - now expired). All apportion for part-year use.  _(Income Tax Act s 13, s 13quat, s 13quin, s 13sex)_

### MISSING: s 13sex - Residential rental properties (specific)

- **MISSING: s 13sex - Residential rental properties (specific)** — Section 13sex specifically: 5% per annum allowance on the cost of new and unused residential units (or improvements to existing units), owned by the taxpayer, used solely for trade (residential letting), where the taxpayer owns at least 5 such units. Higher rates (10%) for low-cost residential units. Common for sole proprietors with rental portfolios - if they meet the 5-unit threshold, the s 13sex allowance is highly valuable as it is in addition to normal expenses like bond interest, rates, insurance, repairs. Cost basis is acquisition cost (not market value). Recoupment on disposal.  _(Income Tax Act s 13sex)_

### MISSING: s 18A - Donations to PBOs (expanded)

- **MISSING: s 18A - Donations to PBOs (expanded)** — Section 18A donation deduction: cash or kind donations to qualifying Public Benefit Organisations (PBOs), Public Institutions, and qualifying conduit PBOs. Deduction capped at 10% of taxable income (before s 18A but after other deductions including s 11F). Excess carries forward to subsequent years (carry-forward introduced 2014). MUST hold a valid s 18A receipt showing PBO/PI number, date of receipt, amount or description of donation, and confirmation that the donation will be used solely for s 18A purposes. From 1 March 2023, the PBO must also submit IT3(d) returns of donations to SARS, and donations are pre-populated on the donor's ITR12.  _(Income Tax Act s 18A; SARS Guide for Approved PBOs)_

### MISSING: s 20 - Assessed losses (and ring-fencing s 20A)

- **MISSING: s 20 - Assessed losses (and ring-fencing s 20A)** — Section 20: assessed losses from a trade carry forward to subsequent years and may be set off against future income from any trade (subject to s 20(2A) requirement that the taxpayer carries on the trade in the year of set-off, OR an exception applies). For COMPANIES, the s 20 loss set-off is now limited to the greater of R1m and 80% of taxable income before set-off (effective for years commencing on or after 1 April 2022). This 80% cap does NOT apply to natural persons (sole props). Section 20A: RING-FENCING for natural persons. High-income individuals (taxable income before set-off above the top marginal rate threshold - currently R1,878,600 for 2026/27) engaged in certain "suspect trades" or trades that have shown losses in 3 of the last 5 years are subject to ring-fencing: the loss can only be set off against future profits from the same trade, not other income. Suspect trades include: farming, animal-showing, rental of residential property, sport, art, racing, gambling, dealing in collectibles, rental of vehicles, aircraft or boats. Important for high-income sole props with side activities.  _([SARS — Rates of Tax for Individuals, 2027 tax year (read 2026-09-02)](https://www.sars.gov.za/tax-rates/income-tax/rates-of-tax-for-individuals/))_

### MISSING: Tax residence

- **MISSING: Tax residence** — A natural person is "resident" under s 1 of the ITA if: (a) ordinarily resident in SA, OR (b) meets the physical presence test (91 full days in current year of assessment + 91 full days in each of preceding 5 years + 915 days in aggregate over the 5 preceding years). "Ordinarily resident" is fact-based (settled home, family, intentions). Residents are taxed on WORLDWIDE income; non-residents only on SA-source. Cessation of residence triggers deemed disposal under s 9H for CGT (exit charge), excluding immovable SA property and certain other items. Important to ask sole prop client about overseas time and intentions.  _(Income Tax Act s 1 (definition) and s 9H; SARS IN 4 (Issue 5))_

### MISSING: Foreign tax credit (s 6quat)

- **MISSING: Foreign tax credit (s 6quat)** — A SA resident pays SA tax on worldwide income but may credit foreign taxes paid on foreign-source income, limited to SA tax attributable to that foreign income (per-country / per-source basket rules). Excess foreign tax credits carry forward 7 years. Alternative deduction under s 6quat(1C) in limited circumstances (e.g. SA-source income that another country has improperly taxed). Common for sole props with foreign clients, foreign rental property, or dividends from foreign companies.  _(Income Tax Act s 6quat; SARS Guide on Foreign Tax Credits)_

### MISSING: CGT depth

- **MISSING: CGT depth** — Sole prop work routinely involves CGT events: sale of business equipment, vehicle disposal, sale of practice, sale of trade premises, cessation of trade with retention of assets, death. Skill should at minimum identify CGT events and flag for specialist review. Basic 2026/27 rules for individuals: inclusion rate 40% (so effective rate up to 18% at top marginal rate of 45%). Annual exclusion R50,000 (up from R40k). Death exclusion R440,000. Primary residence exclusion R3 million (up from R2m) on first R3m of gain (NOT first R3m of proceeds). Small business CGT exclusion (s 10(1)(zJ)): R2.7m lifetime (up from R1.8m) where small business asset disposed of by person 55+, where business gross value below R15m (up from R10m). Effective from 1 March 2026.  _(Income Tax Act Eighth Schedule; s 10(1)(zJ); SARS Budget 2026)_

### MISSING: Donations tax

- **MISSING: Donations tax** — Sole prop transferring assets to family or to trusts often hits donations tax. Flat 20% on cumulative donations (since 1 March 2018) up to R30m; 25% above. Annual exemption R150,000 for natural persons (from 1 March 2026; up from R100,000 - first increase since 2007). Key exemptions: donations between spouses (RESTRICTED from 25 February 2026 to spouses who are SA tax resident at time of donation); donations to approved PBOs; donations between companies in same SA group of companies; donations under s 56 specific items. Filed on IT144 within 30 days after the end of the month in which the donation was made. 10% late payment penalty plus interest. Donee jointly and severally liable if donor fails to pay.  _(Income Tax Act s 54 to s 64; s 56; SARS Budget 2026)_

### MISSING: Estate duty interaction

- **MISSING: Estate duty interaction** — Estate duty levied on dutiable estate of SA residents (worldwide) and non-residents (SA-situated property only). Rate 20% to R30m, 25% above. Abatement R3.5m per estate (portable to surviving spouse - unused balance inherited - effective combined R7m). Section 4(q) full deduction for bequests to surviving spouse. Sole prop-specific issues: business assets included in estate; life insurance proceeds often deemed property (s 3(3)); key-man policies and buy-and-sell policies may be exempt if structured under s 3(3)(a)(iA); future tax liabilities deductible. Section 4A primary abatement plus s 4(p) settlement provisions.  _(Estate Duty Act 45 of 1955; SARS Estate Duty page)_

### MISSING: Tax-Free Savings Account (TFSA)

- **MISSING: Tax-Free Savings Account (TFSA)** — TFSA under s 12T. Contributions R46,000 per year (from 1 March 2026; up from R36,000 - first increase since 2021), R500,000 lifetime cap. Returns (interest, dividends, capital gains) inside the account are exempt. Withdrawals do not free up cap. Penalty 40% on contributions over the cap. Available to all SA residents including sole props. Routinely omitted from sole prop tax planning conversations.  _(Income Tax Act s 12T; SARS Budget 2026)_

### MISSING: Section 7 attribution rules

- **MISSING: Section 7 attribution rules** — Section 7 attributes income earned by certain related persons back to the donor where the income arises from a donation, settlement or other disposition. Critical for sole props who try to split income with spouses or minor children (e.g. by gifting income-producing assets or making low-interest loans). Key sub-rules: s 7(2) - income from donation by one spouse to another retained tax in donor's hands where solely or mainly tax-driven. s 7(3) and (4) - income for benefit of minor child of donor attributed back to donor. s 7(5) - conditional donations: income accrues but enjoyment deferred. s 7(8) - attribution where donor is non-resident and donee uses the asset. s 7C - low or no-interest loans to trusts: deemed donation equal to interest foregone (reference: SARS official rate currently 9.00%).  _(Income Tax Act s 7 and s 7C; SARS IN 96 (s 7C))_

### MISSING: Dividends and dividends tax

- **MISSING: Dividends and dividends tax** — Dividends from SA-resident companies (and non-resident companies listed on JSE) are EXEMPT from income tax in the hands of the recipient (s 10(1)(k)). Instead, the company declaring the dividend deducts dividends withholding tax at 20% under s 64E to s 64N. Net dividend received is what reaches the shareholder. Foreign dividends: not exempt from income tax. Partial exemption mechanism under s 10B - effectively brings the top marginal rate (45%) down to 20% by reducing the inclusion to 25/45 (or 8/27 for companies). For sole props who hold shares in their personal capacity: dividends tax is withheld at source; for tax purposes the dividend is exempt under s 10(1)(k). For sole prop with a rental property held in a company: dividends to extract profits suffer 20% DWT.  _(Income Tax Act s 10(1)(k); s 10B; s 64E to s 64N)_

### MISSING: Skills Development Levy

- **MISSING: Skills Development Levy** — SDL is 1% of leviable payroll (broadly remuneration). Payable monthly with PAYE/UIF on EMP201. Exempt if total annual payroll under R500,000 (most small sole props with under 5 staff are exempt). Levy goes to SETAs. Deductible under s 11(a). Note: a sole prop without employees does not pay SDL on themselves.  _(Skills Development Levies Act 9 of 1999; SARS SDL Guide)_

### MISSING: Withholding taxes paid by SA sole prop

- **MISSING: Withholding taxes paid by SA sole prop** — A SA sole prop making payments to non-residents may be required to withhold tax: (a) Royalties (s 49B): 15% on royalties paid to non-residents (may be reduced by DTA). (b) Interest (s 50B): 15% on SA-source interest paid to non-residents (exemptions for interest from SA government, banks, listed debt). (c) Sale of SA immovable property (s 35A) by non-resident seller: purchaser (or conveyancer) withholds 7.5%/10%/15% depending on seller type. (d) Foreign entertainers/sportspersons (s 47B): 15% on gross. Sole prop must register with SARS for the relevant tax type, withhold, declare on specific returns (e.g. WTI for interest, WTR for royalties), and pay over by month-end after payment.  _(Income Tax Act s 35A, s 47, s 49A-H, s 50A-H)_

### MISSING: Trust distributions to sole prop

- **MISSING: Trust distributions to sole prop** — Sole prop who is a beneficiary of a discretionary trust may receive distributions that are taxable in their hands under s 25B (the "conduit principle"). Income distributed by the trust during the year is taxed in the beneficiary's hands; retained income is taxed in the trust at the flat trust rate of 45%. Capital distributions follow para 80 of the Eighth Schedule. Anti-avoidance under s 7 may attribute distributed income back to the donor/settlor. Important consideration where sole prop family structures involve trusts.  _(Income Tax Act s 25B; Eighth Schedule para 80; s 7)_

### MISSING: Section 11(c) legal expenses

- **MISSING: Section 11(c) legal expenses** — s 11(c) deduction for legal expenses (including arbitration costs) actually incurred by a taxpayer in respect of any claim, dispute or action at law arising in the course of trade or in connection with income earned. Excludes capital-nature legal costs (acquisition of business, defence of title to capital asset). Common items: debt recovery from a customer; defence against a customer claim; employment dispute (subject to s 23(m)); regulatory compliance matter. Cross-references s 11(a) for general trade test.  _(Income Tax Act s 11(c); SARS IN 12)_

### MISSING: Personal Service Provider (PSP) detection

- **MISSING: Personal Service Provider (PSP) detection** — Where a sole prop incorporates a Pty Ltd or CC to provide services to a single client and the relationship is substantially employment-like, the entity may be a Personal Service Provider under the Fourth Schedule definition. Consequences: PAYE deduction at 27% (or 45% for trust); restricted deductions under s 23(k) (essentially only direct costs of services, salary, training, refunds, contributions to retirement funds, expenses related to the premises). Common practitioner trap when a contracting sole prop sets up a company. Tests: work performed mainly at client premises; client controls/supervises; the sole prop is one of three or fewer full-time employees of the entity.  _(Income Tax Act Fourth Schedule definition; s 23(k); SARS PSP Guide)_

### MISSING: Pre-paid expenses (s 23H)

- **MISSING: Pre-paid expenses (s 23H)** — s 23H limits deduction of pre-paid expenses where benefit extends beyond 6 months after year-end. Deductible to the extent the benefit relates to the current year; excess deferred to subsequent year(s). De minimis: R100,000 in aggregate per year may be claimed without apportionment. Common for sole props paying annual subscriptions, insurance, rent in advance, etc.  _(Income Tax Act s 23H)_

### MISSING: Contingent liabilities (s 23(e))

- **MISSING: Contingent liabilities (s 23(e))** — s 23(e) specifically prohibits deduction of contingent liabilities (amounts not unconditionally due). Provisions for warranty, leave pay, bonuses, employee benefits, etc. must be actually incurred to be deductible. Accounting accruals do not generally match the tax position. Sole prop preparing tax return from accounting records must add back provisions.  _(Income Tax Act s 23(e); leading case Edgars Stores Ltd v CIR)_

## Section 1 -- Quick reference

**Quick reference field table**  _([SARS — Rates of Tax for Individuals, 2027 tax year (read 2026-09-02)](https://www.sars.gov.za/tax-rates/income-tax/rates-of-tax-for-individuals/))_

| Field | Value |
| --- | --- |
| Country | South Africa |
| Tax type | Income tax (normal tax) on trade income |
| Primary legislation | Income Tax Act 58 of 1962 |
| Supporting legislation | Tax Administration Act 28 of 2011; Sixth Schedule (Turnover Tax); Fourth Schedule (Provisional Tax) |
| Tax authority | SARS (South African Revenue Service) |
| Filing portal | SARS eFiling (www.sars.gov.za) |
| Currency | ZAR only |
| Tax year | 1 March -- 28 February |
| Return form | ITR12 |
| Provisional tax | IRP6 (1st: 31 Aug, 2nd: last day Feb, 3rd voluntary: 30 Sep) |
| Primary rebate | R17,820 |
| Secondary rebate (65+) | R9,765 |
| Tertiary rebate (75+) | R3,249 |
| Retirement fund deduction | 27.5% of greater of remuneration/taxable income, cap R430,000 |
| Turnover tax | Available for non-professional services, turnover up to R2,300,000 |
| Contributor | Open Accountants Community |
| Validated by | Werner Britz CA(SA), Spurwing CFO |
| Validation date | May 2026 |

**Progressive tax table (2026/2027 year of assessment)**  _([SARS — Rates of Tax for Individuals, 2027 tax year (read 2026-09-02)](https://www.sars.gov.za/tax-rates/income-tax/rates-of-tax-for-individuals/))_

| Taxable income (ZAR) | Rate |
| --- | --- |
| 1--245,100 | 18% |
| 245,101--383,100 | R44,118 + 26% above R245,100 |
| 383,101--530,200 | R79,998 + 31% above R383,100 |
| 530,201--695,800 | R125,599 + 36% above R530,200 |
| 695,801--887,000 | R185,215 + 39% above R695,800 |
| 887,001--1,878,600 | R259,783 + 41% above R887,000 |
| 1,878,601+ | R666,339 + 45% above R1,878,600 |

**Tax thresholds (below = no tax)**  _([SARS — Rates of Tax for Individuals, 2027 tax year (read 2026-09-02)](https://www.sars.gov.za/tax-rates/income-tax/rates-of-tax-for-individuals/))_

| Age | Threshold |
| --- | --- |
| Below 65 | R99,000 |
| 65--74 | R153,250 |
| 75+ | R171,300 |

**Medical tax credits (s6A, 2026/2027)**  _(s6A)_

| Member | Monthly |
| --- | --- |
| Main member | R376 |
| First dependant | R376 |
| Each additional | R254 |

**Turnover tax table (Sixth Schedule)**  _(Sixth Schedule)_

| Turnover (ZAR) | Rate |
| --- | --- |
| 0--600,000 | 0% |
| 600,001--950,000 | 1% above R600,000 |
| 950,001--1,400,000 | R3,500 + 2% above R950,000 |
| 1,400,001--2,300,000 | R12,500 + 3% above R1,400,000 |

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown age | STOP -- age determines rebates and threshold |
| Unknown expense category | Not deductible |
| Unknown business-use proportion | 0% |
| Unknown whether home office qualifies | Not deductible (IN 28 strict) |
| Entertainment expenses | Critically review under s 11(a) and s 23(g); conservatively disallow if no clear nexus to income production |

**Read this whole section before classifying anything.**

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

- **Minimum viable inputs** — Bank statement for the tax year (1 March -- 28 February). Acceptable from: FNB (First National Bank), Standard Bank, Nedbank, Absa, Capitec, Investec, Discovery Bank, TymeBank, or fintech (Revolut, Wise).
- **Recommended inputs** — Invoices, IRP6 payment records, medical aid statements, RA contribution certificates, vehicle logbook.
- **Ideal inputs** — Complete bookkeeping, prior year ITR12, IT34 (assessment), asset register.

### Refusal catalogue

- **R-ZA-1 -- Company/CC/Trust** — This skill covers sole proprietors only. Companies file ITR14 at 27% corporate rate. Trusts file ITR12T. (Trigger: client is a company, close corporation, or trust.)
- **R-ZA-2 -- Foreign income** — Foreign income, s10(1)(o)(ii) exemption, and DTA analysis are outside scope. Consult a registered tax practitioner. (Trigger: significant foreign income.)
- **R-ZA-3 -- Capital gains tax** — Capital gains tax is outside scope. (Trigger: disposal of capital assets.)
- **R-ZA-4 -- Age unknown** — I cannot compute without knowing your age -- it determines rebates and tax threshold. (Trigger: age not provided.)

## Section 3 -- Transaction pattern library (the lookup table)

### 3.1 South African banks (fees and interest)

**South African banks (fees and interest)**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| FNB, FIRST NATIONAL BANK | Bank charges: deductible | Business account fees |
| STANDARD BANK, SBSA | Bank charges: deductible | Same |
| NEDBANK | Bank charges: deductible | Same |
| ABSA | Bank charges: deductible | Same |
| CAPITEC | Bank charges: deductible | Same |
| INVESTEC | Bank charges: deductible | Same |
| DISCOVERY BANK, TYMEBANK | Bank charges: deductible | Same |
| REVOLUT, WISE (fees) | Deductible | Fintech fees |
| INTEREST (credit) | Taxable income up to exemption (R23,800 <65; R34,500 65+); excess = taxable | Interest exemption applies |
| INTEREST (debit) | Deductible if business loan | Personal: NOT deductible |
| LOAN, HOME LOAN (principal) | EXCLUDE | Principal movement |

### 3.2 SA government and statutory bodies

**SA government and statutory bodies**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| SARS | EXCLUDE | Tax payment (provisional/income) |
| UIF, UNEMPLOYMENT INSURANCE | Deductible if employer contribution | Employee-related |
| COIDA, COMPENSATION FUND | Deductible | Workers compensation |
| CIPC | Deductible | Company/IP registration |

### 3.3 SA utilities and telecoms

**SA utilities and telecoms**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| ESKOM, CITY POWER, CITY OF [JHB/CPT/DBN] | Deductible if business premises | Electricity/rates; apportion if home |
| RAND WATER | Deductible if business premises | Water |
| VODACOM, MTN, CELL C, TELKOM, RAIN | Deductible: business phone/internet | Mixed: apportion |

### 3.4 Insurance

**Insurance**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| HOLLARD, SANTAM, OLD MUTUAL, MOMENTUM, OUTSURANCE | Deductible if business insurance | Personal: NOT deductible |
| DISCOVERY HEALTH, BONITAS, GEMS, MEDIHELP | NOT deductible from income | Medical = s6A/s6B credits (against tax, not income) |

### 3.5 SaaS and software -- international

**SaaS and software -- international**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| GOOGLE, MICROSOFT, ADOBE, META | Deductible expense | Foreign SaaS |
| GITHUB, OPENAI, ANTHROPIC | Deductible expense | Non-EU |
| SLACK, ZOOM, ATLASSIAN | Deductible expense | Check entity |

### 3.6 Professional services (SA)

**Professional services (SA)**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| ACCOUNTANT, AUDIT, CA(SA) | Deductible | Accounting/audit fees |
| ATTORNEY, ADVOCATE, LAW FIRM | Deductible if business | Legal fees |
| TAX PRACTITIONER | Deductible | Tax advisory |

### 3.7 Retirement contributions

**Retirement contributions**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| ALLAN GRAY, CORONATION, 10X, SYGNIA, NINETY ONE | s11F deduction: 27.5% of taxable income, cap R430,000 | RA contributions |
| OLD MUTUAL RA, MOMENTUM RA, LIBERTY RA | Same | RA fund |

### 3.8 Transport and travel

**Transport and travel**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| KULULA, FLYSAFAIR, AIRLINK, SAA | Deductible if business travel | Flights |
| UBER, BOLT | Deductible if business | Ride services |
| ENGEN, SHELL, BP, SASOL, CALTEX, TOTAL | Deductible: business vehicle portion only | Fuel; requires logbook |
| AVIS, EUROPCAR, HERTZ | Deductible if business | Rental car |
| SANRAL, E-TOLL | Deductible: business travel portion | Toll fees |

### 3.9 Office and supplies

**Office and supplies**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| INCREDIBLE CONNECTION, MATRIX, TAKEALOT | Deductible or wear-and-tear depending on value | IT equipment |
| OFFICE NATIONAL, WALTONS | Deductible | Stationery |
| POSTNET, SA POST OFFICE | Deductible | Postage/courier |
| MAKRO, GAME | Deductible if business supplies | Verify business purpose |

### 3.10 Food and entertainment

**Food and entertainment**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| PICK N PAY, WOOLWORTHS, CHECKERS, SPAR, SHOPRITE | Default: NOT deductible | Personal provisioning |
| RESTAURANT (any) | Review under s 11(a)/s 23(g) | Bona fide business meals may be deductible; VAT input blocked under s 17(2)(a) |

### 3.11 Internal transfers and exclusions

**Internal transfers and exclusions**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| OWN TRANSFER, INTERNAL | EXCLUDE | Internal movement |
| DRAWINGS, OWNER | EXCLUDE | Personal drawings |
| DEPOSIT, OWN DEPOSIT | EXCLUDE | Capital injection |

## Section 4 -- Worked examples

### Example 1 -- Standard self-employed, mid-range

**Input:** Age 35, revenue R600,000, expenses R180,000, RA R80,000, medical R3,500/mo (main + 1 dependant), provisional paid R40,000.
**Computation:** Net profit R420,000. s11F = 27.5% x R420,000 = R115,500 (within cap). Taxable = R304,500. Tax = R44,118 + 26% x R59,400 = R59,562. Less rebate R17,820. Less medical credit R9,024 (R376 x 2 x 12). Net = R32,718. Less provisional R40,000. Refund R7,282.

### Example 2 -- Turnover tax

**Input:** Non-professional sole proprietor, turnover R650,000.
**Computation:** R650,000 turnover falls within 2026/27 bracket R600,001--R950,000 at 1% above R600,000. Tax = 1% x R50,000 = R500.

### Example 3 -- Entertainment disallowed

**Input:** Client claims R15,000 client entertainment dinners. **Result:** Review under s 11(a) and s 23(g). If bona fide business development with evidence of business purpose, may be deductible. If no clear nexus to income production, disallow. s 23(m) does NOT apply to sole proprietors. VAT input on entertainment is separately blocked under s 17(2)(a) VAT Act.

### Example 4 -- Retirement cap exceeded

**Input:** Taxable income R2,000,000, RA R600,000.
**Computation:** 27.5% x R2,000,000 = R550,000 but cap R430,000. Deduction = R430,000. Excess R170,000 carries forward.

## Section 5 -- Tier 1 rules (deterministic)

### 5.1 Progressive rates

- **Progressive rates application** — Apply rate table to taxable income. One table for all individuals regardless of marital status.  _(Income Tax Act, rates schedule.)_

### 5.2 Rebates

- **Rebates** — Primary R17,820 (all). Secondary R9,765 (65+). Tertiary R3,249 (75+). Credits against tax, not deductions from income.  _([SARS — Rates of Tax for Individuals, 2027 tax year (read 2026-09-02)](https://www.sars.gov.za/tax-rates/income-tax/rates-of-tax-for-individuals/))_

### 5.3 Interest exemption

- **Interest exemption** — R23,800 (under 65). R34,500 (65+). Excess is taxable.  _(s10(1)(i))_

### 5.4 s11F retirement deduction

- **s11F retirement deduction** — 27.5% of greater of remuneration or taxable income (before deduction). Cap R430,000. Excess carries forward or adds to tax-free retirement lump sum (R550,000).  _(s11F)_

### 5.5 Medical tax credits (s6A)

- **Medical tax credits (s6A)** — Main + first dependant: R376/mo each. Additional: R254/mo. Credit against tax. NOT a deduction from income.  _(s6A)_

### 5.6 Provisional tax (IRP6)

- **Provisional tax (IRP6)** — Based on estimated current year. 1st: 31 Aug (50%). 2nd: last day Feb (top-up to 100%). 3rd voluntary: 30 Sep. Under-estimation: 20% penalty if < 90% of actual (income < R1M) or 80% (> R1M). From years of assessment commencing on or after 1 March 2026, the basic-amount safe harbour threshold is R1,800,000 (up from R1,000,000).  _(Fourth Schedule)_

### 5.7 Turnover tax

- **Turnover tax** — Non-professional services, turnover up to R2,300,000. Replaces income tax, CGT, dividends tax, VAT. Cannot claim normal deductions.  _(Sixth Schedule)_

### 5.8 Wear-and-tear (s11(e))

- **Wear-and-tear (s11(e))** — Straight-line over the useful life per SARS IN 47 (Issue 5). Items costing R7,000 or less: full write-off in year of acquisition under BGR 7 (small-value assets). Items above R7,000: straight-line over IN 47 useful life (computers 3 years; office furniture 6 years; office equipment 5 years; cellular phones 2 years; printers 3 years).  _(s 11(e), SARS IN 47, BGR 7)_

### 5.9 Entertainment

- **Entertainment** — Sole proprietor entertainment is tested under the general deduction formula: s 11(a) (actually incurred in the production of income) plus s 23(g) (not of a domestic, private, or capital nature). Bona fide client business development meals with evidence of business purpose may be deductible. s 23(m) does NOT apply to sole proprietors -- it restricts deductions against employment income only. Note: VAT input on entertainment is separately blocked under s 17(2)(a) of the VAT Act regardless of income tax treatment.  _(s 11(a), s 23(g). Cross-reference: VAT Act s 17(2)(a).)_

### 5.10 Home office

- **Home office** — Dedicated room, regularly and exclusively for trade. IN 28 is strict. Dual-use rooms: NO deduction. Proportion = room area / total home. Warning: the area used for trade is 'tainted' for CGT purposes -- on disposal of the residence, the primary residence exclusion does not apply to the tainted portion. Practitioners must warn clients before first claiming home office.  _(s11(a), IN 28)_

### 5.11 Record keeping

- **Record keeping** — 5 years from submission. Invoices, receipts, bank statements, logbooks, asset register.  _(TAA s29-32)_

## Section 6 -- Tier 2 catalogue

### 6.1 Home office qualification

- **Home office qualification** — *Why:* IN 28 requires regular and exclusive use. *Default:* NOT deductible. *Question:* "Is there a dedicated room used only for business?"

### 6.2 Motor vehicle logbook

- **Motor vehicle logbook** — *Why:* Business km unknown. *Default:* 0% business use. *Question:* "Do you have a logbook with date, destination, km, and purpose for each trip?"

### 6.3 Turnover tax vs normal tax

- **Turnover tax vs normal tax** — *Why:* Depends on expense level and qualification. *Default:* Present both. *Question:* "What are your total business expenses? Are you providing professional services?"

### 6.4 s6B additional medical expenses

- **s6B additional medical expenses** — *Why:* Complex, depends on age/disability. *Default:* Do not claim without reviewer. *Question:* "Age 65+? Disability? Out-of-pocket medical expenses?"

### 6.5 Bad debts

- **Bad debts** — *Why:* Must prove irrecoverable. *Default:* Do not claim. *Question:* "Was this debt previously included in income? Is it truly irrecoverable?"

## Section 7 -- Excel working paper template

### Sheet "Transactions"

Columns: Date, Counterparty, Description, Amount (ZAR), Category (Revenue/Expense/Wear-and-tear/RA/Medical/EXCLUDE), Deductible amount, Default?, Question, Notes.

### Sheet "ITR12 Computation"

Step-by-step per Section 5: gross income, deductions, taxable income, tax, rebates, medical credits, provisional tax offset.

## Section 8 -- Bank statement reading guide

**CSV formats.** FNB exports use comma CSV with DD/MM/YYYY. Standard Bank uses semicolons. Nedbank and Absa offer various formats. Common columns: Date, Description, Amount, Balance.

**SA-specific patterns.** "DEBICHECK" = authenticated debit order. "MAGTAPE" = batch payment. "SASWITCH" = ATM network. "PREPAID" = likely personal (airtime top-up). "MUNICIPALITY" = rates and taxes.

**Provisional tax.** Two/three payments per year to SARS. These are tax payments, not expenses. EXCLUDE.

**Medical aid.** Monthly debits to Discovery/Bonitas/etc. These are NOT deductible from income -- they generate s6A credits against tax.

**RA contributions.** Monthly debits to Allan Gray/Coronation/etc. Deductible under s11F with cap.

## Section 9 -- Onboarding fallback

### 9.1 Age

- **Age** — *Inference:* Not inferable. Always ask. *Fallback:* "What is your age at 28 February 2027?"

### 9.2 Residency

- **Residency** — *Inference:* SA bank accounts suggest resident. *Fallback:* "Are you a South African tax resident?"

### 9.3 Business type

- **Business type** — *Inference:* From counterparty patterns. *Fallback:* "What is your trade/profession?"

### 9.4 Turnover tax election

- **Turnover tax election** — *Inference:* Not inferable. *Fallback:* "Have you elected turnover tax?"

### 9.5 Medical aid

- **Medical aid** — *Inference:* Monthly medical aid debits. *Fallback:* "Are you on medical aid? How many dependants?"

### 9.6 RA contributions

- **RA contributions** — *Inference:* Monthly RA debits. *Fallback:* "Do you contribute to a retirement annuity?"

### 9.7 Provisional tax paid

- **Provisional tax paid** — *Inference:* SARS payments in statement. *Fallback:* "What IRP6 amounts have you paid?"

## Section 10 -- Reference material

### Test suite

**Test 1 -- Mid-range.** Age 35, R600K revenue, R180K expenses, R80K RA, medical R3,500/mo. Net tax R32,710.
**Test 2 -- Senior.** Age 68, R200K revenue, R50K expenses, R30K RA. Below threshold. R0 tax.
**Test 3 -- Turnover tax.** R650K turnover. Tax R500.
**Test 4 -- RA cap.** R2M taxable, R600K RA. Deduction R430,000. Excess carries forward.
**Test 5 -- Medical credits.** 6 members. R21,216/year credit (R376 x 2 + R254 x 4 = R1,768/mo x 12).
**Test 6 -- Under-estimation penalty.** R200K estimated, R450K actual. 20% penalty applies if estimate < 90% of actual (for income < R1,800,000 safe harbour threshold).

### Edge case registry

**EC1 -- Interest exemption.** R23,800 <65 / R34,500 65+. Excess taxable.
**EC2 -- Turnover tax + professional.** NOT eligible.
**EC3 -- RA exceeds cap.** Excess carries forward.
**EC4 -- Home office dual use.** NOT deductible.
**EC5 -- Provisional under-estimation.** 20% penalty.
**EC6 -- Medical credits large family.** Compute per-member.
**EC7 -- Foreign income.** ESCALATE.
**EC8 -- Turnover tax exit mid-year.** Transition rules apply.
**EC9 -- Entertainment.** Sole proprietor entertainment is tested under s 11(a) and s 23(g); s 23(m) does NOT apply to sole proprietors.
**EC10 -- Assessed loss.** Carry forward under s20; SARS may query.

### Prohibitions

- NEVER compute without knowing age
- NEVER apply tax below age-threshold
- NEVER allow entertainment deductions without evidence of business purpose under s 11(a) and s 23(g)
- NEVER deduct RA above R430,000 cap
- NEVER allow turnover tax for professional services
- NEVER use prior year income for provisional tax (SA uses estimated current year)
- NEVER treat medical credits as income deductions
- NEVER allow home office for dual-use rooms
- NEVER claim home office without warning the client of the CGT consequence on disposal of the residence (Eighth Schedule para 47)
- NEVER allow income tax as a deduction
- NEVER present calculations as definitive

### Sources

1. Income Tax Act 58 of 1962
2. Tax Administration Act 28 of 2011
3. SARS Interpretation Notes (IN 28, IN 47, IN 14)
4. SARS eFiling -- https://www.sars.gov.za

### Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a registered tax practitioner, CA(SA), or equivalent licensed practitioner in South Africa) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).

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
