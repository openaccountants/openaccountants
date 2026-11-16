---
name: mv-income-tax
description: Use this skill whenever asked about Maldives (Maldivian) personal/individual income tax for self-employed individuals, sole proprietors, or employees. Trigger on phrases like "how much income tax do I pay in the Maldives", "MIRA", "EWT", "employee withholding tax", "MIRA 601", "income tax return Maldives", "interim payment", "tax-free threshold MVR 720,000", "MVR 60,000 a month", "MRPS", "pension contribution Maldives", "self-employed tax Maldives", "income tax registration threshold", or any question about filing or computing income tax for a self-employed or employed client in the Maldives. Also trigger when preparing or reviewing the individual income tax return or an EWT return, computing the progressive income-tax bands, or advising on interim payments and pension. Despite stale secondary sources that claim "the Maldives has no income tax", the Maldives DOES levy a personal income tax under the Income Tax Act (Law No. 25/2019). This skill covers the progressive income-tax brackets, employee withholding tax (EWT), interim/final filing for the self-employed, registration thresholds, the Maldives Retirement Pension Scheme (MRPS), GST context, and penalties. ALWAYS read this skill before touching any Maldives income tax work.
jurisdiction: MV
tax_year: 2026
last_updated: 2026-11-16
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
version: 0.2
type: computation
---

# Maldives individual income tax

## Scope

Prepare an individual's Maldives income-tax working paper for 2026, covering employees, sole proprietors and self-employed people, including combined business and other income. Determine residence, source, exemptions and deductions before applying annual bands. The [payroll Guide](mv-payroll-social.md) owns monthly EWT and pension contribution rates; the [GST Guide](maldives-gst.md) owns general/tourism GST; [corporate income tax](mv-corporate-income-tax.md) owns non-individual returns and the non-resident withholding starting points.

The Maldives has personal income tax. Income Tax Act 25/2019 commenced taxation of income generally on 1 January 2020 and remuneration on 1 April 2020: section 78. Do not use a pre-income-tax country summary or a conflicting third-party monthly table. This tier 2 Guide is source-cited research, without an accountant's approval; a prepared calculation is not evidence that a return was filed or reviewed.

## Ask the client first

1. What are nationality, immigration/marital status, permanent home, days/intended stay and relevant moves? Establish resident, temporary-resident or non-resident status and the applicable period before choosing worldwide or Maldives-source income.
2. What income arose from employment, business/freelancing, rent, investments or other sources, including overseas accounts/platforms? Obtain all employers, business activities, contracts and source/residence facts.
3. Provide full-year bank/payment-platform statements, invoices, expense receipts, accounts, assets, loans, rental records and opening balances. Identify missing accounts, cash sales and personal/business overlap.
4. Provide the TIN, MIRA obligations, prior-year return/assessment, accounting basis and functional currency, GST status/sector, and actual MIRA registration/cancellation dates.
5. Provide gross remuneration/payslips, EWT certificates and returns, MRPS contribution records, employer-funded pension arrangements and any multiple-payer election or MIRA rate notice.
6. Provide business-use evidence for home, phone, vehicles/vessels and travel, tax-loss schedules, interim payments, foreign-tax evidence, refunds/overpayments and any MIRA arrears/enforcement notice.

These group the original intake questions rather than replacing them: the particular employer, home-office arrangement, business-use proportions, assets, registration status, pension wage and prior payments still need answers when relevant. A required fact is not satisfied by a default selected from a bank narrative.

Minimum preparation evidence is a complete-period statement plus confirmed residence and income type. Recommended evidence adds all sales/purchase invoices, employer EWT and pension records, prior return/assessment and GST details; ideal evidence is a complete set of accounts, asset register and payment/credit reconciliation. No statement or equivalent complete ledger is a stop for a statement-based computation. Without invoices, prepare only a provisional reconciliation and mark unsupported deductions/open items; do not call it filing-ready.

## The method, step by step

### 1. Establish residence, period and currency [https://www.mira.gov.mv/Legislations/View/Incometaxact](https://www.mira.gov.mv/Legislations/View/Incometaxact)

Sections 2 and 10 charge residents on domestic and foreign income, while non-residents and temporary residents use Maldives-source income. Section 11 supplies the source tests, including where employment is exercised, specified government contracts, resident directors/partnerships, business/PE, property, interest and other payments. Customer nationality, payment currency, bank location and a local account are not substitutes for those tests.

Under section 79(kk), an individual can be resident through a permanent place of living, presence/intended presence of at least 183 days in the relevant 12-month period commencing or ending in the tax year, or Maldives government employment posted overseas. Temporary residence under section 79(mm) is the defined foreigner permitted to stay under immigration law and not married to a Maldivian. Confirm the actual status; do not infer it simply from a foreign passport or one year's arrival date. Section 81 determines when residence begins.

The ordinary accounting period under Regulation section 58 is 1 January to 31 December; commencement, deregistration and special events can change it. Section 74 requires proration where a prescribed accounting-period amount relates to a nonstandard period. The annual bands below assume the full ordinary year; do not apply them unchanged to an affected short period.

Keep MVR and USD source records separate. Determine functional/presentation currency under Regulation sections 105-108, rather than converting all USD through an arbitrary daily spot rate. The original BML USD workflow remains: retain original amount/currency, relevant transaction date, permitted rate/source and translated amount. Current presentation may be USD for a non-MVR functional currency; do not assume every return is legally presented in MVR. The cases below deliberately use MVR/full-year assumptions.

### 2. Build the taxable-income computation [https://www.mira.gov.mv/Legislations/View/Incometaxact](https://www.mira.gov.mv/Legislations/View/Incometaxact)

| Full-year individual taxable-income slice | Marginal rate | Period and condition | Official source |
|---|---|---|---|
| First MVR 720,000 | 0% | 2026 ordinary full accounting period | [Income Tax Act section 7(a)](https://www.mira.gov.mv/Legislations/View/Incometaxact) |
| Above MVR 720,000 to MVR 1,200,000 | 5.5% | Same | [Income Tax Act section 7(a)](https://www.mira.gov.mv/Legislations/View/Incometaxact) |
| Above MVR 1,200,000 to MVR 1,800,000 | 8% | Same | [Income Tax Act section 7(a)](https://www.mira.gov.mv/Legislations/View/Incometaxact) |
| Above MVR 1,800,000 to MVR 2,400,000 | 12% | Same | [Income Tax Act section 7(a)](https://www.mira.gov.mv/Legislations/View/Incometaxact) |
| Above MVR 2,400,000 | 15% | Same | [Income Tax Act section 7(a)](https://www.mira.gov.mv/Legislations/View/Incometaxact) |

Apply each slice separately and add the results, as section 7(b) requires. The zero-rate slice is part of the bracket structure, not a second personal allowance to subtract before applying the same bands. Derived cumulative tax at the upper ends of the positive-rate slices is MVR 26,400, MVR 74,400 and MVR 146,400 respectively; those amounts come from the band arithmetic, not an additional statutory charge.

Section 3 lists remuneration, business income, rents, dividends, interest, pensions/benefits, beneficiary income, technical fees, commissions, royalties, disposal gains and other gains. Identify the actual head and test section 12 exemptions before combining taxable amounts. Employment income does not disappear from an annual computation merely because an employer already withheld tax; a separate return exemption may apply.

Important exceptions for the original transaction classes include resident-to-resident company dividends under section 12(a), the limited non-business interest exemption under section 12(f)(2), qualifying Pension Act pension/annuity receipts under section 12(l), and government grants to individuals under section 12(u). The interest exemption is up to MVR 5,000 per accounting period for the specified non-business interest; do not exempt all business financing receipts or all investment income. Government grant/subsidy classification is not a universal capital-versus-revenue exclusion: identify the recipient and precise section 12 category. Exempt receipts need their own record and associated expenses cannot automatically reduce taxable income.

Remove collected GST from a registered person's income only to the extent it is the actual tax on the supply. Do not deduct recoverable input GST again as an income-tax expense. Unrecoverable tax may form part of the underlying allowable cost, subject to the ordinary expense/capital rules. Refer GST sector, exemption and registration issues to the owning Guide.

### 3. Reconstruct business revenue without netting away receipts [https://www.mira.gov.mv/Legislations/View/Income-Tax-Regulation](https://www.mira.gov.mv/Legislations/View/Income-Tax-Regulation)

Reconcile client invoices and gross platform sales to payouts. Stripe, PayPal, Wise, Upwork, Fiverr and Toptal payouts can be net of commissions, refunds and reserves. Record the gross underlying revenue and the separately supported allowable fee, not both gross invoices and payouts as revenue or the net payout plus the same fee deducted a second time. Match withheld amounts, balances in platform wallets, chargebacks, debts and advances to the correct period and accounting basis.

Accounts normally use accrual principles under Act section 13 and Regulation sections 57-59. Cash basis is an election available only when the current section 59(e) conditions are satisfied, including annual income and actual/estimated non-current-asset costs. It is not an automatic right for every person using a bank statement. A cash election does not remove capital-gain, capital-allowance or other statutory adjustments. Prepare one resident's accounts for all their businesses as section 59(a) requires, rather than giving every activity a separate personal band.

Loans, own transfers and personal capital introduced are not ordinary sales merely because the bank shows a credit. Keep contracts/counter-entries and trace the true consideration. A tax refund can reverse a prior tax-account balance or include a distinct component; establish the original posting before excluding the whole receipt. Previously deducted expenses reimbursed or bad debts recovered can be income under Act sections 14-15.

### 4. Test revenue expenses and business/private allocation [https://www.mira.gov.mv/Legislations/View/Incometaxact](https://www.mira.gov.mv/Legislations/View/Incometaxact)

Act section 17 permits expenditure incurred in the period wholly and exclusively to produce total income; mixed expenses require the income-producing proportion. Regulation section 67 requires a just and reasonable basis plus an explanation and calculation. Missing business-use evidence is an open item, not legal proof of a permanent zero allowance. Do not substitute an arbitrary home-office, telephone, car or vessel percentage.

| Expense/adjustment | Governing test | Official source |
|---|---|---|
| Office rent, professional insurance, accountancy/legal fees, supplies, subscriptions and other recurring trade costs | Actual expense for producing taxable income, correctly timed and supported; distinguish capital/private/exempt-income components | [Income Tax Act sections 16-17, 32](https://www.mira.gov.mv/Legislations/View/Incometaxact) |
| Home office, shared utilities, internet and phone | Just and reasonable evidenced business allocation; dedicated space is evidence, not an invented universal exclusive-room rule | [Income Tax Act section 17; Regulation section 67](https://www.mira.gov.mv/Legislations/View/Income-Tax-Regulation) |
| Travel, fuel, vehicle/vessel costs | Document business purpose and journey/use; exclude private use and ordinary commuting | [Income Tax Act sections 17, 32(b)(2)](https://www.mira.gov.mv/Legislations/View/Incometaxact) |
| Training/CPD | Test direct connection with business; degree/tertiary qualification costs are excluded by the specific rule even if connected | [Income Tax Act section 32(b)(4)](https://www.mira.gov.mv/Legislations/View/Incometaxact) |
| Entertainment/client meals | Establish business purpose and private/exempt components; do not invent an absolute income-tax ban from a merchant name or a GST input restriction | [Income Tax Act sections 17 and 32](https://www.mira.gov.mv/Legislations/View/Incometaxact) |
| Private living, income tax, fines/penalties and drawings | Private costs, income tax and statutory fines are disallowed; drawings are not an incurred business cost | [Income Tax Act section 32](https://www.mira.gov.mv/Legislations/View/Incometaxact) |
| Recoverable GST | No separate income-tax deduction for deductible input tax | [Income Tax Act section 32(a)(5)](https://www.mira.gov.mv/Legislations/View/Incometaxact) |
| Loan repayment | Separate principal from interest; financing deductions need the statutory tests and limitations | [Income Tax Act sections 17, 22, 71 and 79(t)](https://www.mira.gov.mv/Legislations/View/Incometaxact) |

Home-office working papers identify the actual premises, period, area/use, bills and calculation; justify any allocation, including a shared room, on the evidence. Do not automatically claim the whole household rent/utilities or automatically prohibit every dual-use space. Vehicle/vessel papers separate purchase cost, finance principal/interest, running costs, private journeys and capital allowances. Use a log or equivalent reliable evidence; do not make a vessel fully deductible because its narrative includes DHONI.

Keep professional/subscription, marketing, travel and training categories even when a statement shows only a merchant. Annual/prepaid SaaS may require period allocation; perpetual licences or acquired rights may be capital. Foreign suppliers may also raise income-tax withholding, independently of whether a cost is deductible and independently of GST. Cross-border tax collection is not decided by the bank card's merchant-country field.

### 5. Handle capital, debts, rent, pension and losses separately [https://www.mira.gov.mv/Legislations/View/Income-Tax-Regulation](https://www.mira.gov.mv/Legislations/View/Income-Tax-Regulation)

Act section 25 and Regulation Chapter 11 govern assets. Maintain an asset register with invoice, acquisition/first-use dates, cost, class, business use, prior allowances, disposal and tax written-down value. The ordinary rates below apply to the asset's cost, with eligibility, part-period, business-use and exhaustion restrictions; do not substitute accounting depreciation, a foreign pooling system or a guessed percentage.

| Asset/condition | Rate or limit | Period | Official source |
|---|---|---|---|
| Office equipment, including a qualifying computer/printer class | 20% annual cost-based allowance | 2026; classify the actual asset | [Income Tax Regulation section 83(a)(1), (b)](https://www.mira.gov.mv/Legislations/View/Income-Tax-Regulation) |
| Furniture and fittings | 10% | Same | [Income Tax Regulation section 83(a)(1)](https://www.mira.gov.mv/Legislations/View/Income-Tax-Regulation) |
| Motor vehicles | 20% | Same; apportion private use | [Income Tax Regulation sections 77, 83](https://www.mira.gov.mv/Legislations/View/Income-Tax-Regulation) |
| Wooden marine vessels / other marine vessels | 7% / 5% respectively | Same; actual material/class and use required | [Income Tax Regulation section 83(a)(1)](https://www.mira.gov.mv/Legislations/View/Income-Tax-Regulation) |
| Computer software | 33⅓% | Same; distinguish service subscription and acquired asset | [Income Tax Regulation section 83(a)(1)](https://www.mira.gov.mv/Legislations/View/Income-Tax-Regulation) |
| First-period use | At least 183 days in a full accounting period under the more-than-half-period rule | Acquisition-period ordinary allowance | [Income Tax Regulation section 76](https://www.mira.gov.mv/Legislations/View/Income-Tax-Regulation) |
| Low-value assets acquired together with like assets | Cost no more than MVR 5,000, with aggregate immediate deductions capped at MVR 100,000 per accounting period | Section 78(a)-(b) route | [Income Tax Regulation section 78](https://www.mira.gov.mv/Legislations/View/Income-Tax-Regulation) |
| Qualifying cash-basis taxpayer's separate low-capital-expenditure route | Aggregate expenditure less than MVR 50,000; apply section 78(c)'s actual conditions | Section 78(c), not a universal per-asset threshold | [Income Tax Regulation section 78(c)](https://www.mira.gov.mv/Legislations/View/Income-Tax-Regulation) |

For an intangible asset not in a specific category, Regulation section 84 uses useful-life principles with its own conditions. Capital allowances stop at the permitted total; disposal can produce a balancing charge or allowance under Act sections 25 and 29 and the Regulation. Costs before business commencement and 2020 transition assets need their specific rules; do not blindly write off an old purchase in the current year. Rates applicable from 2027 are separately labelled in the consolidated regulation and do not replace the 2026 table early.

Bad debt under Act section 23 requires prior inclusion in income (or the specified finance-business case), exhausted reasonable collection steps, reasonable irrecoverability and a write-off in the accounts, with collateral/guarantee, pending-court and pre-commencement exclusions. A bank chargeback or late invoice alone is insufficient. Include a later recovery under section 14; keep proof of the earlier deduction.

For immovable-property rent, Act section 28 allows a qualifying cash-basis taxpayer to elect a 20% deduction from total rental income instead of other rental-expense deductions. The election has a five-year restriction on change without approval, with the Regulation section 91-2 procedure; do not claim both the percentage and the actual costs/capital allowances on the same rent. Obtain the lease, receipts, property/location, accounting basis and election history before computing rent. Rental income can be business income under the Act's definitions; a bank label does not settle the return category.

MRPS payments are deductible under Act section 19. For employment EWT, section 54(c) already subtracts the employee's remuneration-funded contribution before applying monthly bands; use gross annual remuneration and the proper annual deduction without duplicating that deduction or treating withheld EWT as an expense. Employer-funded contributions and self-employed payments need their actual participant/payer records. Separate pension liability remittances from deductible employer expense and personal pension deductions; a bank debit alone does not show which treatment applies. Contribution rates/base, eligibility and employer-funded alternatives are in the payroll Guide.

Business losses carry forward under Act section 33 for up to five years, earliest first, limited to positive income and the actual conditions; Regulation section 72 limits their use to business income. Do not set a business loss against capital gain merely because both belong to the individual. Act section 34 and Regulation section 95 separately restrict capital loss to capital gains and apply their carry-forward period. Keep original year, use, expiry and the distinction between an accounting loss and a tax loss.

### 6. Preserve the narrative library as evidence cues

Use case-insensitive matching to locate a possible category and inspect the most specific match. The old instruction to classify automatically and never second-guess is withdrawn: a merchant/narrative is evidence of neither deductibility nor tax residence. Keep the original statement line beside the proposed category, document link, reason, GST component, business allocation and reviewer flag.

| Credit patterns | Proposed investigation and treatment |
|---|---|
| Client name + TRANSFER, DEPOSIT, PAYMENT RECEIVED | Match invoice, cash/credit timing, deposits and GST. Include actual business revenue; an own transfer is not a sale. |
| FEES, PROFESSIONAL FEES, CONSULTANCY, SERVICE FEE | Business/service revenue if earned independently; check employment relationship, source, refunds and tax components. |
| STRIPE PAYOUT, PAYPAL PAYOUT, WISE PAYOUT | Reconcile gross underlying receipts, platform commissions, refunds, reserves and net settlement. |
| UPWORK, FIVERR, TOPTAL | Keep platform gross-revenue/fee reconciliation and source facts; do not assume the net payout is gross turnover. |
| SALARY, REMUNERATION, EMPLOYER [name], MUSAARA | Obtain payslip, gross remuneration, benefits, employee pension and EWT; annual return exemption is a separate question. |
| RENT RECEIVED, KUYYEE | Obtain the lease, property/source and rent-election history; determine the actual business/other-income return classification. |
| INTEREST RECEIVED | Identify business versus non-business and any actual exemption; Islamic-finance profit requires the underlying instrument. |
| DIVIDEND | Identify payer and recipient residence, exemption/withholding and certificate; do not include an exempt resident-to-resident dividend automatically. |
| MIRA REFUND, TAX REFUND | Match prior tax-account balance and any distinct receipt component; do not count repayment of income tax as new business sales. |
| GOVERNMENT GRANT, SUBSIDY | Check section 12 recipient/category and actual grant terms rather than a universal capital/revenue shortcut. |

| Debit patterns | Proposed investigation and treatment |
|---|---|
| OFFICE RENT, COMMERCIAL RENT | Business premises and period; separate deposit/capital/private portions. |
| PI INSURANCE, PROFESSIONAL INDEMNITY | Business insurance policy, covered period and purpose. |
| ACCOUNTANT, AUDITOR, BOOKKEEP, ACCA, CA FEES | Business professional costs where supported; distinguish personal qualification/degree costs and capital work. |
| LAWYER, LEGAL, ADVOCATE | Identify current business advice versus acquisition/capital, personal litigation and exempt-income work. |
| OFFICE SUPPLIES, STATIONERY | Ordinary consumables versus capital equipment and private purchases. |
| MARKETING, GOOGLE ADS, META ADS, FACEBOOK ADS | Advertising for current taxable business, with invoice and any separate withholding analysis. |
| TRAINING, CPD, COURSE, SEMINAR, CONFERENCE | Relevant continuing-business training; check the degree/tertiary exclusion and private components. |
| BANK FEE, BANK CHARGE, SERVICE CHARGE | Business bank/finance service, not every merchant's unrelated service charge; identify tax treatment and actual cost. |
| STRIPE FEE, PAYPAL FEE, STRIPE, PAYPAL, TRANSACTION FEE | Supported processing fee, reconciled separately from gross sales and net payouts. |
| DOMAIN, HOSTING, CLOUDFLARE, AWS, DIGITALOCEAN | Current business services or capital rights as appropriate; match period and invoice. |
| GOOGLE WORKSPACE, MICROSOFT 365, OFFICE 365 | Recurring business software/service; allocate mixed/prepaid use and examine foreign-payment obligations. |
| ADOBE, CANVA, FIGMA, NOTION, SLACK, ZOOM | Same current-service test, not automatic deduction from vendor identity alone. |
| ANTHROPIC, OPENAI, GITHUB, ATLASSIAN, DROPBOX | Same business-purpose, period and support tests; no personal-use assumption. |
| PERPETUAL SOFTWARE LICENCE, PERPETUAL SOFTWARE | Acquisition/right classification and applicable capital treatment; do not assume every licence is SaaS. |
| STELCO, FENAKA, MWSC | Business portion of actual utilities cost; GST exemption does not itself determine income-tax deduction. |
| DHIRAAGU, OOREDOO, MOBILE, DHIRAAGU MOBILE, OOREDOO MOBILE | Actual business communications portion, supported by use rather than a default percentage. |
| MALDIVIAN, FLYME, EMIRATES, QATAR AIRWAYS | Business travel evidence, purpose, traveller and any private/commuting portion. |
| HOTEL, GUESTHOUSE, BOOKING.COM, AIRBNB | Business trip or other underlying supply, excluding private holidays; platform name alone is not proof. |
| FERRY, MTCC FERRY, SPEEDBOAT, TAXI | Business journey support; exclude ordinary commute/private use. |
| FUEL, PETROL, DIESEL | Match actual business vehicle/vessel use and log. |
| RESTAURANT, CAFE, ENTERTAINMENT, CLIENT MEAL | Review business purpose/private components and separate GST restrictions; no invented blanket income-tax class ban. |
| PERSONAL, GROCERIES, SUPERMARKET | Identify private living costs and disallow; genuine documented business goods need their actual category. |
| FINE, PENALTY, MIRA FINE | Statutory fine/penalty disallowed, kept outside deductible expenses. |
| INCOME TAX, MIRA TAX PAYMENT | Income tax and payment/credit reconciliation; not a deduction against income. |
| DRAWINGS, PERSONAL WITHDRAWAL, ATM (personal) | Drawings/cash/private control, not a business expense merely because money left the account. |

| Capital/movement patterns | Required control |
|---|---|
| LAPTOP, COMPUTER, MACBOOK, DESKTOP | Asset register; verify office-equipment class, capital/low-value route, dates and business use. |
| PRINTER, SCANNER, COPIER | Office-equipment register and applicable allowance conditions. |
| FURNITURE, DESK, CHAIR | Furniture/fittings register, business use and allowance history. |
| VEHICLE, CAR, VESSEL, DHONI (business) | Distinguish motor vehicle, wooden vessel and other vessel; acquisition, running costs and private use separated. |
| INTERNAL TRANSFER, OWN ACCOUNT, BETWEEN ACCOUNTS | Match both sides and exclude duplicate income/expense; investigate any real underlying consideration separately. |
| LOAN REPAYMENT, PERSONAL LOAN | Principal control, with separately identified interest subject to its own tests. |
| MRPS, PENSION CONTRIBUTION, MPAO | Pension schedule matching payer, participant and month; deductible contribution or liability remittance as appropriate, never a duplicate cost. |
| GST PAYMENT, MIRA GST | GST liability settlement; not income tax expense or new input tax. |
| EWT PAYMENT, MIRA 601 | Match employee credit/withheld-liability remittance and certificate; do not deduct from taxable income. |
| INTERIM PAYMENT, MIRA INCOME TAX INTERIM | Credit against final liability, matched to tax year and actual payment. |

BML/Bank of Maldives narratives may contain TRANSFER, DD, SO, CARD and CHARGES; MIB/Maldives Islamic Bank may use TRANSFER, PROFIT and CHARGE; HBL Maldives/SBI Maldives may use PAYMENT, TRF and FEE. These preserve the original reading aids, not a guarantee about a bank's current export layout. Read the actual CSV/PDF/text columns, sign convention, currency and date format; the original DD/MM/YYYY convention is a check to confirm, not a universal parser. BML USD CARD PAYMENT/TRANSFER records require the proper currency workflow above.

| Original illustrative bank-export aid | Fields to look for and reconcile |
|---|---|
| BML PDF/CSV | Date, Description, Debit, Credit, Balance; locate counterparty/reference in the actual description and confirm the date convention. |
| MIB PDF | Date, Particulars, Withdrawal, Deposit; inspect the underlying instrument where the description says profit rather than interest. |
| HBL Maldives PDF/CSV | Value Date, Description, Amount, Balance; inspect the description for the counterparty. |
| SBI Maldives PDF | Date, Narration, Debit, Credit; confirm signs and any separate balance field in the supplied export. |
| BML USD CSV | Date, Description, Amount (USD), Balance; retain the USD amount and the legally supported conversion working. |

These are retained legacy preparation examples, not independently verified current bank specifications. A different export can supply equivalent evidence; do not reject it or invent missing fields. The former approximate USD 1 = MVR 15.4 shortcut is not a verified filing exchange rate and must not replace the applicable tax-currency rules.

Dhivehi/transliterated cues retained: MUSAARA suggests salary, KUYYEE rent, FAISA/TRANSFER needs direction/context, MRPS/MPAO pension, EWT/MIRA 601 employee withholding, GST/MIRA 105 GST registration, STELCO/FENAKA utilities, and DHIRAAGU/OOREDOO telecoms. MIRA 105 is the registration form, not the GST return. Translate or obtain clarification where a description is insufficient; do not infer legal character from one word.

### 7. Combine income and reconcile credits [https://www.mira.gov.mv/Legislations/View/Incometaxact](https://www.mira.gov.mv/Legislations/View/Incometaxact)

Combine taxable business profit with taxable remuneration, rental/investment and other income after the correct source/exemption/deduction rules. Apply personal deductions and loss relief in the proper categories without duplication, then the annual marginal bands. Compare total income-tax liability with verified EWT, interim payments and any other permitted credits; do not assume a refund from a negative working-paper balance without the tax-account and refund process.

Section 72 permits a resident's foreign tax credit only for qualifying foreign income tax on foreign-source income also taxable in Maldives, limited to the lesser of tax paid abroad and Maldives tax on the net foreign-source income. Apply it separately by income type/country, keep supporting documents and the statutory claim/amendment timing. A foreign tax or a gross overseas receipt is not by itself evidence of a full credit. Treaty relief, residence conflicts and foreign-entity attribution require their actual instruments and facts.

## Boundary and exception table

| Missing fact or special branch | Safe preparation response |
|---|---|
| Residence/source uncertain | Stop tax-base selection; collect home, presence, immigration/marital and source facts. Never assume all uncertain non-resident receipts are domestic. |
| Employee versus independent contractor uncertain | Inspect relationship/contract and remuneration definition; do not choose the preferred rate by narrative. |
| Business/private split or expense category unproved | Keep an unresolved item and provisional adjustment; obtain evidence before an allowance, rather than declaring permanent non-deductibility. |
| GST registration unknown | Obtain actual registration and legal-trigger facts; do not assume unregistered status from the absence of a number on the statement. |
| Pensionable wage unclear | Obtain the contract and apply the statutory fallback in the payroll Guide; basic salary alone is not always the answer. |
| Tourism operations | Individual business profit remains within this job, but resort GST, Green Tax and service-charge bases need the specialist handoff. |
| Capital asset, bad debt, loss or rent election | Apply the separate schedule/conditions; do not use a bank-only general expense total. |
| Corporate/partnership/bank taxpayer or final NWT income | Change to the correct taxpayer/regime, including any elective-return branch; do not apply the individual bands to an entity. |

## Worked cases

The original statement dates and company descriptions below are preserved as historical fixtures; the individual annual-band cases apply the verified 2026 full-year rules. Historical statement fixtures require the law for their actual period when used in a real filing. These are conditional working-paper examples, not evidence of a real client's records or professional approval.

### Case 1: self-employed taxable income MVR 1,500,000

Assume a full-year individual taxable-income figure already reconciled after allowable adjustments, no special relief and no credits. Compute only each positive marginal slice, then add. Tax is MVR 50,400; it is not the headline rate multiplied by all income. At MVR 1,500,000 the taxed slices are MVR 480,000 at the second band and MVR 300,000 at the third; at MVR 900,000 the positive slice is MVR 180,000. [Income Tax Act section 7](https://www.mira.gov.mv/Legislations/View/Incometaxact).

```oa-check
name: Annual individual income 1500000
inputs:
  income: 1500000
steps:
  - b1: max(min(income, 1200000) - 720000, 0) * 0.055
  - b2: max(min(income, 1800000) - 1200000, 0) * 0.08
  - b3: max(min(income, 2400000) - 1800000, 0) * 0.12
  - b4: max(income - 2400000, 0) * 0.15
  - tax: b1 + b2 + b3 + b4
expected:
  tax: 50400
```

### Case 2: self-employed taxable income MVR 900,000

Assume a full-year individual taxable-income figure already reconciled after allowable adjustments, no special relief and no credits. Compute only each positive marginal slice, then add. Tax is MVR 9,900; it is not the headline rate multiplied by all income. At MVR 1,500,000 the taxed slices are MVR 480,000 at the second band and MVR 300,000 at the third; at MVR 900,000 the positive slice is MVR 180,000. [Income Tax Act section 7](https://www.mira.gov.mv/Legislations/View/Incometaxact).

```oa-check
name: Annual individual income 900000
inputs:
  income: 900000
steps:
  - b1: max(min(income, 1200000) - 720000, 0) * 0.055
  - b2: max(min(income, 1800000) - 1200000, 0) * 0.08
  - b3: max(min(income, 2400000) - 1800000, 0) * 0.12
  - b4: max(income - 2400000, 0) * 0.15
  - tax: b1 + b2 + b3 + b4
expected:
  tax: 9900
```

### Case 3: monthly remuneration and the original bank credit

Input: `28/02/2025 ; BML CREDIT ; EMPLOYER ATOLL CONSULTING PVT LTD ; SALARY FEB ; +116,200.00 ; MVR`.

Assume ordinary monthly gross remuneration MVR 120,000, no other taxable benefits/payments and no employee-funded pension deducted from that remuneration. For example, the employer may fund the full pension contribution itself, as the Pension Act allows. EWT is MVR 2,200 + MVR 1,600 = MVR 3,800 and cash pay is MVR 116,200. If an employee pension contribution was instead deducted from remuneration, both the EWT base and net cash would change; the original claim that this same net also included an employee pension deduction was arithmetically inconsistent. Do not reverse-engineer gross pay solely from the bank credit. [Income Tax Act section 54](https://www.mira.gov.mv/Legislations/View/Incometaxact); pension conditions in [payroll](mv-payroll-social.md).

```oa-check
name: Historical payroll bank-credit reconciliation
inputs:
  gross: 120000
steps:
  - ewt: 40000 * 0.055 + 20000 * 0.08
  - net: gross - ewt
expected:
  ewt: 3800
  net: 116200
```

### Case 4: GST-inclusive consulting fee

Input: `15/03/2025 ; BML TRANSFER IN ; RESORT HOLDINGS PVT LTD ; INV-2025-007 ; +108,000.00 ; MVR`.

Assume a registered general-sector consultant's ordinary taxable fee including the applicable general GST. Business revenue is MVR 100,000 and GST liability is MVR 8,000; a resort customer does not itself turn the consultant into a tourism-sector supplier. Record the gross receipt, net revenue and tax separately. The [GST Guide](maldives-gst.md) supplies sector/registration/time-of-supply conditions; [Act section 12(t)](https://www.mira.gov.mv/Legislations/View/Incometaxact) excludes tax imposed under law from taxable income.

```oa-check
name: Historical general-GST consulting receipt
inputs:
  gross: 108000
steps:
  - revenue: gross / 1.08
  - gst: gross - revenue
expected:
  revenue: 100000
  gst: 8000
```

### Case 5: monthly software subscription

Input: `01/04/2025 ; BML CARD ; ADOBE SYSTEMS ; CREATIVE CLOUD APR ; -462.00 ; MVR`.

Assume the invoice supports a current monthly subscription used wholly for the taxable business, with no recoverable GST or prepaid/private component in the stated amount. Deductible expense is MVR 462. A capital licence, private subscription, creditable tax or different period changes this conclusion; the merchant name alone proves none of the assumptions. [Income Tax Act sections 17 and 32](https://www.mira.gov.mv/Legislations/View/Incometaxact).

```oa-check
name: Supported current-business software expense
inputs:
  paid: 462
  business_fraction: 1
steps:
  - deduction: paid * business_fraction
expected:
  deduction: 462
```

### Case 6: pension debit and payroll reconciliation

Input: `05/03/2025 ; BML DD ; MPAO MRPS CONTRIBUTION ; FEB ; -5,600.00 ; MVR`.

For an eligible employee with MVR 80,000 pensionable basic salary under a compliant contract and the ordinary split, employee and employer contributions are MVR 5,600 each, total MVR 11,200. The debit equals one share, not proof that both shares were remitted or that it is a fresh deductible expense of the account holder. Match employer statement, employee payslip and accepted pension record. The [payroll Guide](mv-payroll-social.md) owns the rates and contract fallback; [Income Tax Act section 19](https://www.mira.gov.mv/Legislations/View/Incometaxact) supplies the deduction, applied once.

```oa-check
name: Pension contribution control
inputs:
  basic: 80000
steps:
  - employee_share: basic * 0.07
  - employer_share: basic * 0.07
  - total: employee_share + employer_share
expected:
  employee_share: 5600
  employer_share: 5600
  total: 11200
```

### Case 7: transfer to own savings

Input: `15/05/2025 ; BML TRANSFER ; OWN ACCOUNT - SAVINGS ; ; -20,000.00 ; MVR`.

The original fixture's separator punctuation is normalized; its date, narrative, blank reference, amount and currency are otherwise retained. Assume evidence confirms transfer between the individual's own accounts. Match the corresponding credit and exclude the MVR 20,000 from both revenue and deductible expenses. It is not proof of a business purchase or a tax credit. [Income Tax Act sections 3 and 17](https://www.mira.gov.mv/Legislations/View/Incometaxact).

```oa-check
name: Own-account movement
inputs:
  transfer: 20000
steps:
  - taxable_receipt: transfer * 0
  - deductible_expense: transfer * 0
expected:
  taxable_receipt: 0
  deductible_expense: 0
```

### Cases 8-10: original annual boundary checks

These retain the original nil-band, upper-band and middle-band test cases. Each assumes full-year taxable income already determined, no credits and no special regime. The figures below are recomputed by the same marginal-band method rather than a flat rate.

Case 8: MVR 720,000 taxable income produces MVR 0 tax. [Income Tax Act section 7](https://www.mira.gov.mv/Legislations/View/Incometaxact).

```oa-check
name: Annual boundary 720000
inputs:
  income: 720000
steps:
  - b1: max(min(income, 1200000) - 720000, 0) * 0.055
  - b2: max(min(income, 1800000) - 1200000, 0) * 0.08
  - b3: max(min(income, 2400000) - 1800000, 0) * 0.12
  - b4: max(income - 2400000, 0) * 0.15
  - tax: b1 + b2 + b3 + b4
expected:
  tax: 0
```

Case 9: MVR 3,000,000 taxable income produces MVR 236,400 tax. [Income Tax Act section 7](https://www.mira.gov.mv/Legislations/View/Incometaxact).

```oa-check
name: Annual boundary 3000000
inputs:
  income: 3000000
steps:
  - b1: max(min(income, 1200000) - 720000, 0) * 0.055
  - b2: max(min(income, 1800000) - 1200000, 0) * 0.08
  - b3: max(min(income, 2400000) - 1800000, 0) * 0.12
  - b4: max(income - 2400000, 0) * 0.15
  - tax: b1 + b2 + b3 + b4
expected:
  tax: 236400
```

Case 10: MVR 2,000,000 taxable income produces MVR 98,400 tax. [Income Tax Act section 7](https://www.mira.gov.mv/Legislations/View/Incometaxact).

```oa-check
name: Annual boundary 2000000
inputs:
  income: 2000000
steps:
  - b1: max(min(income, 1200000) - 720000, 0) * 0.055
  - b2: max(min(income, 1800000) - 1200000, 0) * 0.08
  - b3: max(min(income, 2400000) - 1800000, 0) * 0.12
  - b4: max(income - 2400000, 0) * 0.15
  - tax: b1 + b2 + b3 + b4
expected:
  tax: 98400
```

### Case 11: rental deduction election versus actual allowable costs

Assume an eligible cash-basis individual has MVR 500,000 rental receipts, MVR 150,000 substantiated allowable rental costs and MVR 800,000 other taxable income. The percentage election permits MVR 100,000 rental deduction, so combined taxable income is MVR 1,200,000 and tax MVR 26,400. If the actual-cost method is available and all stated costs qualify, combined income is MVR 1,150,000 and tax MVR 23,650, MVR 2,750 lower. Election history, its five-year restriction and other facts can prevent simply changing method this year; the comparison is not permission to disregard that restriction. Do not combine both deduction methods. [Income Tax Act sections 7 and 28](https://www.mira.gov.mv/Legislations/View/Incometaxact).

```oa-check
name: Qualifying rental methods compared
inputs:
  rent: 500000
  actual_costs: 150000
  other_taxable: 800000
steps:
  - election_costs: rent * 0.2
  - election_base: rent - election_costs + other_taxable
  - actual_base: rent - actual_costs + other_taxable
  - election_tax: (election_base - 720000) * 0.055
  - actual_tax: (actual_base - 720000) * 0.055
  - difference: election_tax - actual_tax
expected:
  election_costs: 100000
  election_base: 1200000
  actual_base: 1150000
  election_tax: 26400
  actual_tax: 23650
  difference: 2750
```

## When to refuse or refer

- **R-MV-1: residency unknown.** Stop choosing the income base until resident/temporary/non-resident and source facts are established. Preserve a transaction inventory while the tax computation is held.
- **R-MV-2: company, partnership or bank.** This job covers individuals. Route an entity to the correct corporate/specialist computation and return, preserving its separate status and liability.
- **R-MV-3: non-resident withholding.** Covered dividends, interest, royalties and managerial/technical/consultancy or other service payments need the payment-class, residence, treaty, gross-up and finality analysis in the corporate Guide or a specialist review. Do not reuse the old unsupported generic range.
- **R-MV-4: tourism.** Ordinary individual business income remains in scope. Resort TGST, Green Tax, service-charge bases and other tourism levies require the GST/specialist handoff before a combined filing is finalized.
- **R-MV-5: arrears/enforcement.** Preserve notices, due dates, balances, payments and disputes and refer the period-by-period penalty/enforcement calculation; do not use the former BPT caps as an assumed income-tax limit.
- **R-MV-6: GST filing requested.** Load the dedicated GST Guide; MIRA 105 is registration and the actual GST returns differ. A personal income-tax working paper is not a GST return.

Also refer an unsubstantiated foreign credit/treaty position, complex asset disposal, controlled-foreign-entity income, uncertain financing limitation, unusual trust/beneficiary income or a proposed departure/deregistration with special filing consequences. Do not invent a missing figure or leave a qualified calculation labelled definitive. A professional must review the final facts, classification and supporting evidence before filing.

## Filing and payment

### Registration and return obligations [https://www.mira.gov.mv/Legislations/View/Income-Tax-Regulation](https://www.mira.gov.mv/Legislations/View/Income-Tax-Regulation)

Separate registration, return filing and tax payable. Under Regulation section 4, a person required to register a business or holding the relevant permit/licence can be required to register with MIRA independently of a personal tax band. For other specified individuals/deemed partnerships, the business gross-revenue trigger is average monthly revenue exceeding MVR 40,000 in the relevant period, not a universal MVR 60,000 business threshold. MIRA 117 is the registration/change form, with the Ministry-business-registration exception in section 3(b).

Remuneration registration follows section 7: employer registration at the estimated/actual monthly taxable-remuneration triggers, the additional recipient category once an employer has a qualifying recipient, and the recipient's multiple-payer or unregistered-person self-registration tests. The payroll Guide holds these monthly figures and MIRA 118/election process. Do not assume employment EWT registration completes registration for later independent business/rental income; section 11 requires changes to be notified.

Act section 65 sets registration periods, including ordinary post-commencement income/business/employer events and the override requiring registration before the first return/payment due date. Regulation section 11 requires the specified changes in information/employment/other income to be notified within 15 days, using MIRAconnect/MIRA 117 as applicable. Confirm the relevant trigger rather than applying a date from an old one-off commencement transition.

An individual's ordinary annual-return exemption under Regulation section 101(a) requires all four conditions: current and preceding taxable income each at or below MVR 720,000, and current and preceding total income each at or below MVR 2,000,000. Nonstandard periods require proration. Section 101(d) separately covers sole remuneration from one payer and the specified following no-income year. Section 101(f) overrides exemptions for listed cases, including specified foreign-employer income with tax liability and the current/non-current-asset tests at MVR 30,000,000; section 101(h) has its own excluded entities. A low current tax bill alone does not prove exemption. An eligible single-employer person may elect to file under Act section 50(b), for example to reconcile a supported overpayment; do not invent a guaranteed refund.

For financial statements, Regulation sections 57 and 102 require the relevant accounts/attachments. Cash-basis/audit exceptions now require the income and actual/estimated non-current-asset conditions together; do not use a turnover-only audit shortcut. The exact MVR 30,000,000 return-filing trigger can apply even at a boundary where a cash-basis accounting election is separately permitted. Non-companies do not supply a company directors' report merely because the form checklist includes it.

### Interim and final return/payment [https://www.mira.gov.mv/Legislations/View/Incometaxact](https://www.mira.gov.mv/Legislations/View/Incometaxact)

| Obligation and conditions | Statutory date/amount rule | Period | Official source |
|---|---|---|---|
| First interim return/payment where required | 31 July of the tax year | Ordinary 2026 calendar | [Income Tax Act section 42(a)](https://www.mira.gov.mv/Legislations/View/Incometaxact) |
| Second interim return/payment where required | 31 January following | Same | [Income Tax Act section 42(b)](https://www.mira.gov.mv/Legislations/View/Incometaxact) |
| Final income-tax return/payment where required | 30 June following | Same | [Income Tax Act section 42(c)](https://www.mira.gov.mv/Legislations/View/Incometaxact) |
| First liable year's ordinary interim computation | Each payment is half estimated annual tax | Apply withholding-credit and exemption conditions | [Income Tax Act sections 43(a), 49](https://www.mira.gov.mv/Legislations/View/Incometaxact) |
| Later year's ordinary interim computation | Each payment is half prior-year tax, with period-length adjustment; permitted lower estimate subject to underestimation rule | Actual first/later year and lawful estimate established | [Income Tax Act section 43(b)-(f)](https://www.mira.gov.mv/Legislations/View/Incometaxact) |

Section 49's no-interim branch requires its current interim/prior-year tax conditions, including the MVR 20,000 tests, or the relevant return-exemption route; do not treat every self-employed person as automatically liable to two cash instalments. Section 43(e) tests underestimation by reference to the stated 20% margin. Retain forecast, prior-year computation and any EWT credit allocation. Section 44 deducts actual interim payments and the remaining permitted withholding credit from final liability, once.

Use MIRA 603 for interim returns and [MIRA 604 v26.1](https://www.mira.gov.mv/Files/GetFile/08ee0850-211a-4b32-910a-a351dffb791b) for the ordinary annual return, under Regulation sections 99-100. Determine required filing first, then complete assessment and schedules before the front page. The current form has taxpayer/residence/period, accounting basis, functional/presentation currency and attachments; individual liability is computed in Section C and transferred to the front-page liability. Front-page fields separately identify foreign tax credit, EWT/NWT/CGWT, first/second interims, existing overpayments, final payment and amount paid. Reconcile each field to supporting schedules rather than inventing an authenticated screen box.

Use [MIRAconnect](https://www.mira.gov.mv) for the actual taxpayer, year and return. Regulation section 103 prescribes online returns/payments with the limited individual/deemed-partnership return exception based on preceding-year income and the separate payment-channel exception; the generic website's income-only summary does not replace the regulation's period and taxpayer conditions. Submit the authorized declaration, save acknowledgement/reference, pay the correct liability with the actual TIN/period/reference and retain the receipt/account reconciliation. A prepared return, scheduled transfer or unconfirmed payment is not a completed filing.

For employment, MIRA 601 and the monthly obligations/remaining nil months are in the payroll Guide. EWT already withheld is a personal tax credit where permitted, not a deduction from income and not proof that every person's annual filing is unnecessary. Check all employers and other income; retain certificates. Any MIRA 650 reconciliation notice applies to its own return and deadline.

### Penalties, amendments and unresolved employment matters [https://www.mira.gov.mv/Legislations/View/tax-admin-act-consolidated](https://www.mira.gov.mv/Legislations/View/tax-admin-act-consolidated)

Tax Administration Act section 65 covers specified non-filing/information/registration offences: the civil formula includes 0.5% of tax payable for the period and a daily fine not exceeding MVR 50. Section 66 charges 0.05% per day on outstanding tax after the required date. Determine the actual offence/base/date, MIRA decision and applicable relief. The former nil-return and late-payment caps were drawn from BPT material; no current personal-income-tax cap is asserted here. Serious inaccuracy/evasion and enforcement need their own legal analysis.

An incorrect return may require amendment within the Act's permitted period and the appropriate MIRA process; keep original acknowledgement, corrected computation, reason and credit/payment effect. Do not quietly overwrite a filed working paper or label an adjustment a new current-year expense. A public-holiday/extension notice can change an operational deadline; confirm the actual applicable notice without inventing a new statutory calendar.

Minimum-wage/employment compliance is retained as a separate payroll fact to establish, not a personal income-tax exemption. The official 2021 Minimum Wage Order was read: it uses employer-category hourly rates and specified included/excluded remuneration, effective until modified/revoked/replaced. That does not substantiate the old draft's universal monthly floors or its tourism-size shortcut for every 2026 worker. Current classification, applicability and any later instrument remain held below and in the payroll handoff. Do not use an unverified minimum wage as the actual pension or EWT base.

## Completion checklist

### Working-paper structure

The original Excel-style schema is retained below as a working-paper specification, not a set of official return box numbers. Actual return presentation currency and category mapping must follow the current form/law. Add supporting schedules rather than forcing every tax adjustment into one expense total.

```text
MALDIVES INDIVIDUAL INCOME TAX WORKING PAPER
Tax year: 2026; accounting period: ____; functional/presentation currencies: ____
Person/TIN: ____; resident / temporary resident / non-resident: ____
Income type: self-employed / employee / both / other: ____

A. BUSINESS INCOME
A1 Client revenue net of actual collected GST
A2 Platform gross revenue reconciled to payouts, fees, reserves and refunds
A3 Other business income; A4 total business income

B. ALLOWABLE BUSINESS DEDUCTIONS
B1 Office rent; B2 professional insurance; B3 accountancy/legal
B4 Office supplies; B5 current software subscriptions
B6 Marketing/advertising; B7 business bank/processing fees
B8 Training/CPD after the statutory exclusions
B9 Business travel, flights/ferry/accommodation
B10 Business telecoms portion; B11 supported home-office costs
B12 Business vehicle/vessel running costs
B13 Statutory capital allowances, separately supported asset schedule
B14 Other lawful expenses/adjustments; B15 total allowed business deductions
C. BUSINESS PROFIT: A4 minus B15, with separate tax adjustments/loss schedule

D. OTHER/COMBINED INCOME
D1 Gross taxable employment remuneration before EWT
D2 Rental receipts and their actual/elected deduction, correctly categorized
D3 Investment receipts after exemptions; D4 total taxable other income
E. TAXABLE INCOME: combine C and D4; adjust personal MRPS/other permitted
   deductions and category-restricted losses without double counting
   Resident worldwide; temporary/non-resident Maldives-source only
F. ANNUAL INCOME TAX: separately compute each marginal slice in the rates table
F1 Total liability before tax credits

G. CREDITS AND PAYMENTS
G1 Verified EWT credits; G2 actual interim payments
G3 Qualifying foreign credit with separate limitation evidence
G4 Total permitted credits/payments, used once; other lawful credits separately
H. BALANCE: F1 less permitted credits/payments and verified overpayments
   Reconcile to actual MIRA final payment/refund position and tax account
```

Final review flags preserve the original checks: residence/source; proper business-versus-remuneration registration trigger; actual GST registration; home-office, vehicle/vessel and telecom business evidence; correct capital class/rate and asset history; pension eligibility/base/contributions and deduction once; entertainment purpose and private elements; employer MIRA 601/other returns and credits. Also check all accounts, gross platform reconciliation, accounting basis, current/prior filing exemption, losses, foreign credit, currency, interims and tax-account balances. Unsupported deductions and missing facts remain expressly flagged, not hidden in a neat final total.

Never state that Maldives has no personal income tax, use an unverified third-party rate table, choose an unconfirmed residence/source base, add collected GST to taxable revenue, deduct private costs/income tax/fines/drawings, duplicate pension or withholding credits, or treat a merchant/AI calculation as accountant approval. Capital allowances and pension deductions are now governed by the actual official provisions above rather than the former blanket research-gap prohibitions.

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.


## Sources

| Source and actual material read | Official URL | Read on |
|---|---|---|
| Income Tax Act 25/2019, MIRA-hosted English unofficial translation consolidated 31 August 2026: sections 2-3, 7, 10-19, 22-35, 41-51, 54, 64-65, 71-74, 78-81; scope/source/exemptions, individual bands, expenses/pension, assets/rent/losses and filing provisions cited above | https://www.mira.gov.mv/Legislations/View/Incometaxact | 2026-11-16 |
| Income Tax Regulation 2020/R-21, consolidated 20 August 2026: sections 3-11, 41-43, 57-60, 67, 72, 73-91, 95-108; registration/change, accounting/cash basis, capital allowances, rent/losses, forms, return exemption, audit and currency clauses cited above | https://www.mira.gov.mv/Legislations/View/Income-Tax-Regulation | 2026-11-16 |
| MIRA 604 v26.1: assessment, accounting/presentation information, individual computation and front-page credits/payment; linked current form read | https://www.mira.gov.mv/Files/GetFile/08ee0850-211a-4b32-910a-a351dffb791b | 2026-11-16 |
| MIRA annual filing page: form/portal and published assistance/filing routes, read with the fuller consolidated regulation | https://www.mira.gov.mv/Pages/View/ictindividualshowtofile | 2026-11-16 |
| Tax Administration Act, consolidated 31 August 2026: sections 65-67 civil offence/payment provisions | https://www.mira.gov.mv/Legislations/View/tax-admin-act-consolidated | 2026-11-16 |
| Ministry's official English unofficial Minimum Wage Order: scope, effective date/continuation and hourly category/remuneration structure; not treated as proof of every 2026 employment category | https://trade.gov.mv/wp-content/uploads/2023/05/minimum-wage-order-en-v01.pdf | 2026-11-16 |

MIRA's native downloads were blocked; the official English HTML and linked form text were actually read through the web reader. Authority-hosted English legal texts are labelled unofficial translations and the Dhivehi original prevails. Reading an English official translation does not mean the Dhivehi original or a live authenticated return was inspected. The earlier secondary-source brackets are superseded by the actual official text read for this revision.

Not yet confirmed: live MIRAconnect field layout and actual payment/reference/refund workflow for this taxpayer; treaty/foreign-entity/financing outcomes and specific foreign-credit evidence; the current voluntary/self-employed MRPS ceiling and any applicable employee maximum beyond the identified ordinary rules; exact capital class/useful life of an unidentified asset and any claimed pooling method; current minimum-wage category/monthly conversion, tourism shortcut or later employment instrument; current penalty mitigation/cap beyond the cited general provisions. Missing client evidence for business use, residence/source, expense purpose, pension funding or a return election remains a factual hold, not permission to invent a default.
