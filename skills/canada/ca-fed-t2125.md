---
name: ca-fed-t2125
description: >
  Prepare a Canadian sole proprietor's Form T2125 business or professional
  income working paper. Use for self-employed expenses, bank statement
  classification, gross versus net sales, GST/HST and ITCs, business number,
  NAICS, fiscal year end, home office, motor vehicle expenses, subcontractors,
  capital cost allowance, CCA and net business income. Covers 2026 estimates
  and a dated 2025 filing bridge using the actual observed 2025 form.
  Read before classifying T2125 transactions; use ca-fed-t1-return and
  ca-fed-cpp-ei for personal tax and contributions outside the business form.
version: 2.1
jurisdiction: CA
tax_year: 2026
last_updated: 2026-11-13
depends_on:
  - income-tax-workflow-base
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
---

# Canadian business and professional income: T2125 v2.1

## Scope

Prepare the income, expenses, capital allowance and home-office schedules for an individual carrying on a Canadian business or profession. Currency is CAD; retain the original currency and conversion support for foreign transactions. This skill is **Built from the law** and **Not yet approved**. It produces proposed working papers for professional sign-off, not an automatic filing or payment. [CRA T2125 catalogue](https://www.canada.ca/en/revenue-agency/services/forms-publications/forms/t2125.html).

Use current law for **2026 estimates** and the expressly dated **2025 bridge** for that income year. The annual T2125 actually inspected on November 13, 2026 is **2025**, nine pages, Parts 1 to 9 with CCA and vehicle charts. Final 2026 form presentation is **not yet confirmed**; do not relabel the 2025 PDF as 2026. The form's older “proposed” annotations do not override subsequently enacted legislation. [Actual 2025 T2125](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t2125/t2125-25e.pdf); [2026 enactment](https://laws-lois.justice.gc.ca/eng/AnnualStatutes/2026_3/page-17.html).

Read [income-tax-workflow-base](../global/methods/income-tax-workflow-base.md). This method owns the business computation. [ca-fed-t1-return](ca-fed-t1-return.md), Methods 2 to 7 and its dated tables, owns the personal federal brackets, BPA, credits, instalments and balance; [ca-fed-cpp-ei](ca-fed-cpp-ei.md) owns contribution coverage and calculation. Provincial/territorial tax and Quebec QPP/QPIP require their applicable methods. An individual partner can use T2125 from partnership financial statements or a T5013 slip; the partnership's own information return, where required, is T5013. Do not say a partnership universally files T2125 as its return. [Partnership responsibilities](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4068/guide-partnership-information-return-t5013-forms.html).

## Ask the client first

Read existing client records before repeating questions. Establish these facts and keep unanswered items open:

1. Income year; original return, estimate or amendment; business name, activity, address, province of residence and any other permanent establishment. Obtain the actual six-digit NAICS classification and fiscal start/end dates; distinguish business, professional and commission income. Prepare a separate form for each applicable business/profession. [T4002 identification](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4002/t4002-4.html).
2. Actual BN/program accounts, partnership details if applicable, GST/HST registration and effective dates, returns, reporting periods, ordinary or elected quick method and associates' taxable supplies. A nine-digit BN is different from a complete program-account identifier. Do not invent either from the other.
3. Complete bank, card and processor statements for the fiscal period, opening/closing balances, issued invoices, sales/expense ledgers, receipts and refunds. Obtain receivables, payables, inventory and prior reserves/assistance. Full-year bank statements plus activity/NAICS are useful initial intake, not sufficient filing evidence. Obtain complete books, prior T2125, CCA schedule and NOA where available. [Accounting methods](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/accounting-methods.html).
4. Home workspace eligibility, measurements, shared-use hours, business months, costs and unclaimed carryforward. Vehicle ownership/lease dates, actual cost/taxes, business and total kilometres, receipts and full/sample logbook support. Never turn missing percentages into an asserted legal 0% or 100%.
5. Capital acquisitions/disposals, invoice and available-for-use dates, prior use/ownership, related parties, grants, elections, opening UCC and actual CCA previously claimed. A verified first year can have zero opening UCC; an established pool needs reconciliation, not an assumed purchase price.
6. Subcontractor services actually paid, amounts excluding tax where relevant, recipient identity/residence, worker status and construction/other reporting facts. Do not determine employee status from a transfer label or treat every payment over $500 as the same slip.
7. T4 earnings and CPP/QPP/EI deductions, age/elections/disability facts, self-employed EI agreement and contribution history. Hand these to the contribution method; do not deduct contributions as a T2125 expense.
8. Prior assessments, instalment reminders/payments, actual GST/HST filings and outstanding amendments. Produce a missing-record list, supported subtotal and conditional alternatives where possible; do not fabricate registration, business purpose, tax treatment or approval.

## The method, step by step

### 1. Select accounting period, entity and evidence [CRA accounting methods](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/accounting-methods.html)

Ordinary business/professional self-employment income uses accrual accounting: earned sales can be income before collection and allowable incurred expenses before payment. Inventory, prepayments, capital purchases, liabilities and owner transfers prevent a bank-credit-minus-debit shortcut. Farming, fishing and qualifying self-employed commission agents have particular method options; use the appropriate method rather than extending an exception to every sole proprietor.

A Canadian individual business generally uses a December 31 fiscal end. The alternative non-calendar method requires actual eligibility and election under ITA 249.1, with T1139 reconciliation, not an unrestricted choice of any year end. Check first fiscal period, individual/all-individual partnership conditions, tax-shelter exclusion, prior election and consent requirements for changes. The observed T1139 catalogue is 2025. [ITA 249.1](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-249.1.html); [T1139](https://www.canada.ca/en/revenue-agency/services/forms-publications/forms/t1139.html).

Normalize bank signs and dates, reconcile opening plus movements to closing balances, match card payments/transfers to the underlying purchases once, separate loans/capital introduced/drawings from sales, and reconcile processors' gross sales, fees, tax, refunds and net payouts. Match T4A and other slips to booked income so the same fee is not counted twice. Record source document, business purpose, period, CAD conversion, tax status, account, allocation and unresolved facts for each entry.

### 2. Reconcile sales and GST before entering income [T2125 Parts 3A to 3D](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t2125/t2125-25e.pdf)

For business income, actual **3A** starts with gross sales/commissions/fees including tax collected or collectible. **3B** removes included GST/HST, provincial sales tax, returns, discounts, allowances and applicable adjustments; **3C = 3A - 3B**. With the quick method, **3F = 3D - 3E** is the specified tax-retention assistance calculation; **3G = 3C + 3F**. Professional income uses its separate Part 3B/3N route, including the appropriate work-in-progress/accounting adjustments. Do not use business and professional sales fields interchangeably.

**8000** receives adjusted gross sales/professional fees; **8299 = 8000 + 8290 prior reserves + 8230 other income**. Other income can include recovered bad debts, business prizes, assistance and CCA recapture. Reconcile assistance against the relevant expense/capital cost where required. The quick-method 1% credit is separately reported as other income at 8230 under CRA guidance; it is not silently lost in 3F. **Do not subtract collected GST again from 8299.** [Income and assistance instructions](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4002/t4002-4.html).

For business income, Part 3D reconciles **8300 opening inventory + 8320 net purchases + 8340 direct wages + 8360 subcontracts + 8450 other direct costs - 8500 closing inventory = 8518 cost of goods sold**. **8519 = 8299 - 8518**. Enter only the business portion and do not deduct those costs again in Part 4. Professional income follows its applicable Part 4 starting amount.

| GST/HST situation | Income-tax treatment and required evidence |
|---|---|
| Ordinary-method registrant | Reconcile collected/collectible tax to the GST liability, not ordinary sales income. Recoverable ITCs reduce the related expense/capital cost; do not claim both gross cost and the same tax credit. |
| Valid non-registrant | Tax paid can form part of an otherwise allowable business expense or capital cost. First establish registration liability/effective date; last year's small-supplier status is insufficient. |
| Unrecoverable tax | Include only the tax attributable to the allowable business cost under the applicable rules. Tax denied because the purchase is personal does not make that personal amount deductible. |
| Quick-method registrant | Confirm eligibility and election. Most operating ITCs are replaced by the remittance method, so operating costs generally include unrecovered tax. Eligible capital ITCs are separate. Reconcile retained tax through the actual form and the separate credit through other income. |
| GST refund, payment, rebate or assistance | Reconcile the liability, previously reduced/expensed costs, assistance and capital adjustments. A bank description alone does not establish income or a deduction. |

[Quick method, ITCs and credit](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4058/quick-method-accounting-gst-hst.html); [T2125 expense tax basis](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t2125/t2125-25e.pdf).

### 3. Establish GST registration rather than assuming it [ETA 148 and 240](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-148.html)

The ordinary small-supplier limit is **$30,000**, measured on worldwide taxable supplies, including zero-rated supplies, of the person and associates before expenses, with statutory exclusions for sales of capital property, financial services and goodwill on a business sale. Exempt supplies are not taxable supplies. Apply both the single-calendar-quarter and consecutive-quarter tests using actual transaction dates.

If one quarter exceeds the limit, small-supplier status ends on the crossing supply: charge tax on that supply and establish that effective registration date. If the limit is exceeded only over up to four consecutive quarters, small-supplier status generally continues through the following month; registration takes effect no later than the first taxable supply after status ends. CRA requires registration within **29 days** of the effective date. Taxi/commercial ride-sharing and voluntary registration have separate routes. Obtain place-of-supply, exemption/zero-rating and effective-date facts before assessing tax. [CRA examples](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/when-register-charge.html); [ETA 240](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-240.html).

The developer with $95,000 annual sales in Case 1 cannot simply be called unregistered because the previous year was below the threshold. Quarterly sales, associates, supply types and dates are necessary to reconstruct liability. Do not apply GST to all annual deposits or invent a remittance rate from this example.

### 4. Decide allowable current costs and actual form lines [ITA 18](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-18.html)

A cost needs an income-earning connection, the correct period and a reasonable amount; personal/living expenses and capital outlays are not ordinary current deductions. Apply specific prohibitions and limits as well as business purpose. Lasting benefit, restoration versus improvement, original condition, separate asset and the nature of rights help distinguish current from capital; there is **no universal $500 capitalization threshold**. [ITA 67](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-67.html); [ITA 20](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-20.html).

#### Current expense line map

Use the actual form, not a guessed line derived from a merchant name. [2025 T2125 Part 4](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t2125/t2125-25e.pdf).

| Line | Use, after eligibility and allocation checks |
|---|---|
| 8521 | Advertising, subject to the applicable advertising restrictions |
| 8523 | Deductible meals/entertainment amount, not automatically the full receipts |
| 8590 | Eligible bad debts |
| 8690 | Business insurance; home/vehicle components follow their own schedules |
| 8710 | Eligible interest and general bank charges; principal repayments are not expenses |
| 8760 | Business taxes, licences and memberships, not management fees |
| 8810 | Office expenses; distinguish capital equipment and stationery/supplies |
| 8811 | Office stationery and supplies |
| 8860 | Current professional fees, including eligible accounting/legal services |
| 8871 | Management and administration fees; CRA expressly includes processing-payment bank charges |
| 8910 | Business-premises rent; home costs follow Part 7 |
| 8960 | Eligible repairs/maintenance, not capital improvements |
| 9060 | Salaries, wages, benefits and employer contributions not already included as direct costs |
| 9180 | Business property taxes; home allocation follows Part 7 |
| 9200 | Eligible travel; apply the separate meals limit to food/entertainment |
| 9220 | Eligible utilities and business telephone costs; no invented line 8220 |
| 9224 | Fuel other than motor-vehicle fuel |
| 9275 | Delivery, freight and express |
| 9281 | Chart A business vehicle expenses excluding CCA |
| 9936 | Business CCA excluding the home-office CCA already claimed in Part 7 |
| 9270 | Specified other allowable expenses; not a default for unsupported spending |

Loan interest requires actual income-earning use and applicable limits. Certain financing fees are spread over five years, normally 20% annually with short-period adjustments; not every bank/legal charge is immediately deductible. Capital-acquisition legal fees may belong to asset cost. Payment processing charges can use the supported 8871 classification; general banking/interest uses 8710. Do not claim the same fee twice. [8710 timing and limits](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/report-business-income-expenses/completing-form-t2125/line-8710-interest.html); [8871](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/report-business-income-expenses/completing-form-t2125/line-8871-management-administration-fees.html).

Memberships need a business connection; recreational/dining/sporting club dues are not made deductible by that description. Recurring software/hosting costs require their actual service period, rights, purpose and business share; a vendor name does not make them professional fees. Application software acquired as capital can be Class 12, while systems software follows the relevant equipment class. Training to maintain existing skills differs from acquiring a new qualification; a conference may instead be a convention subject to ITA 20(10), including its two-convention and organization/location conditions. Do not copy the archived training bulletin's retired eligible-capital-property mechanism into current law. [ITA 18(1)(l)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-18.html); [ITA 20(10)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-20.html); [archived training interpretation](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/it357r2/archived-expenses-training.html).

#### Meals

Ordinarily deduct **50% of the lesser of actual cost and a reasonable amount** for eligible business meals/entertainment. Enter the resulting deduction at **8523**; keep the excluded amount in the reconciliation, not an invented second form add-back. Eligible long-haul drivers' food/beverages during an eligible travel period can use **80%**: the statutory driver/truck, absence and distance conditions must actually be met. Statutory exceptions can permit a full deduction, for example qualifying food-service businesses, separately identified reasonable customer reimbursements, particular employee inclusions/events/worksites or qualifying fundraising events. Apply the precise exception, not a general “business meal = 100%”. Convention packages can need a separately determined meal component. [ITA 67.1](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-67.1.html).

### 5. Use the bank pattern library as evidence prompts

Every row is an investigation prompt. Verify the invoice, contract, counterparty, purpose, accrual period, tax basis and business portion before accepting the suggested destination. A credit may be a loan, transfer, refund or customer advance; a debit may settle a liability or buy an asset. Bank text alone never establishes deductibility.

#### Income patterns

| Pattern | Route after reconciliation |
|---|---|
| CLIENT DEPOSIT, CLIENT PAYMENT, [client name] | Reconcile earned sales/customer advances and tax through Parts 3A/3B and 3C; 8299 is the resulting gross-income field, not simply deposits. |
| STRIPE PAYOUT, STRIPE TRANSFER | Reconstruct gross sales, tax, refunds, fees and settlement timing. Do not report only net payout as sales. |
| PAYPAL TRANSFER, PAYPAL PAYOUT | Same gross-to-settlement reconciliation; exclude actual own-account transfers and trace currency conversion. |
| ETRANSFER [client name], INTERAC | Check direction, counterparty and invoice before classifying business revenue. |
| GST/HST REFUND, CRA GST REFUND | Match the GST account and prior ITC/cost treatment; check assistance/rebates rather than blanket income or exclusion. |
| INTEREST, SAVINGS INTEREST | Ordinary personal investment interest routes to T1 12100; determine whether actual business-source income instead belongs in business accounts. |
| DIVIDEND | Ordinary investment dividends route to the T1 dividend method, including 12000/12010 where applicable; not customer revenue. |
| EMPLOYMENT INCOME, SALARY | Reconcile T4 employment income outside T2125; avoid counting payroll deposits as business sales. |
| CRA REFUND, TAX REFUND | Identify tax principal, interest and any business assistance separately. Personal tax-principal refunds are not business sales. |
| RENTAL INCOME | Ordinary property-source rent routes to T776; services/business facts can change its character. |
| OWN TRANSFER, SAVINGS TRANSFER | Match both accounts; actual owner transfers are not revenue. |

Personal investment and employment line routing is completed by [ca-fed-t1-return](ca-fed-t1-return.md), not a second T1 calculation here.

#### Expense patterns

| Pattern | Suggested destination and check |
|---|---|
| RENT, OFFICE RENT, COMMERCIAL LEASE | 8910 for eligible business-premises period; capital/leasehold costs and home rent need separate treatment. |
| PROPERTY TAX (business premises) | 9180, not 8810; home portion belongs to Part 7. |
| HYDRO, ELECTRICITY, GAS, ENBRIDGE, HYDRO ONE | Eligible premises utilities at 9220; qualifying home costs via Part 7, without a second claim. |
| BELL, ROGERS, TELUS, SHAW | Business telephone portion at 9220; basic home telephone cost is not a business deduction; eligible incremental business/long-distance cost needs support. |
| INTERNET, WIFI | Establish service, period and business allocation; avoid duplicating any home schedule claim. |
| INSURANCE, BUSINESS INSURANCE, LIABILITY | 8690 if allowable business insurance; distinguish personal, vehicle, home and capital/financing costs. |
| ACCOUNTING, BOOKKEEPER, CPA | Current business professional work at 8860, with capital/personal elements separated. |
| LAWYER, LEGAL FEE | 8860 for eligible current work; acquisition/financing/personal work is not automatically a current deduction. |
| OFFICE SUPPLIES, STAPLES, GRAND & TOY | Check invoice: 8811 for stationery/supplies, 8810 for appropriate office costs, capital schedule for equipment. |
| BANK FEE, MONTHLY FEE, NSF | 8710 for eligible business banking; financing timing and personal charges need separate analysis. |
| STRIPE FEE, PAYPAL FEE, SQUARE FEE | Supported processor fees at 8871; reconcile sales gross and prohibit duplicate 8710 claims. |
| INTEREST (business loan) | 8710 if actual borrowed-money use and statutory conditions support it; split principal. |
| ADVERTISING, GOOGLE ADS, META ADS, FACEBOOK | 8521 only for eligible business advertising after applicable restrictions and period checks. |
| MEALS (client entertainment) | 8523 after ordinary 50% or verified statutory exception; document attendees/purpose. |
| MEALS (business travel, alone) | Eligible travel food at 8523 with the applicable restriction; personal food is not deductible merely because paid away from home. |
| SOFTWARE, SUBSCRIPTION, SAAS | Select current office/administrative/other service category from actual rights; capital software goes to its class. No universal 8810/8860 full deduction. |
| TRAINING, COURSE, CONFERENCE | Eligible current training or convention costs, specified at 9270 or the relevant travel category without duplication; distinguish capital/personal qualification and meal limits. |
| GAS, FUEL, PETRO-CANADA, SHELL, ESSO | Vehicle Chart A/9281 with actual business allocation, not non-vehicle 9224. |
| CAR INSURANCE, AUTO INSURANCE | Chart A business portion, with supplementary business insurance treated as specified below. |
| CAR REPAIR, SERVICE, OIL CHANGE | Chart A eligible operating costs; capital improvements are separate. |
| PARKING (business) | Actual qualifying business parking added separately in Chart A; personal parking is not allowable. |
| CRA INCOME TAX, TAX INSTALMENT | Personal income-tax payments outside business expenses; reconcile to T1 payments. |
| CRA GST PAYMENT, GST REMITTANCE | GST liability settlement, with ordinary/quick-method reconciliation; not a second deduction for already booked purchases. |
| CPP CONTRIBUTION | Outside T2125; the contribution method splits the base credit and allowable deduction, rather than half of total CPP. |
| PERSONAL, GROCERY, AMAZON (personal) | Verified personal spending excluded; merchant name alone cannot settle mixed invoices or actual business supplies. |
| COMPUTER, LAPTOP, EQUIPMENT (over $500) | Test capital nature and actual class/date even below $500; the label is not a capitalization rule. |
| MEMBERSHIP, DUES, PROFESSIONAL BODY | 8760 for eligible business dues/licences, not management fees; apply club/personal exclusions. |
| SUBCONTRACTOR, CONTRACTOR PAYMENT | 8360 for actual direct subcontracts, not 8340 direct wages; determine reporting independently of deductibility. |

#### Subscription prompts

| Pattern | Review |
|---|---|
| GOOGLE WORKSPACE, MICROSOFT 365, ADOBE | Recurring service versus acquired capital rights, period and business share. |
| SLACK, ZOOM, NOTION, FIGMA, GITHUB | Same; none is automatically a professional fee because of its name. |
| AWS, HEROKU, DIGITAL OCEAN | Actual hosting/service versus asset acquisition, accrual/prepayment and business use. |
| QUICKBOOKS, XERO, FRESHBOOKS, WAVE | Accounting software service versus professional accounting work or acquired software rights. |

#### Transfers and other exclusions

| Pattern | Review |
|---|---|
| OWN TRANSFER, SAVINGS, TFSA, RRSP | Trace actual owner transfers and investment transactions; personal RRSP deductions belong in T1, not T2125. |
| MORTGAGE, RENT (personal) | Separate principal, interest and rent; only qualifying home expenses through Part 7. |
| ATM, CASH WITHDRAWAL | Trace cash use and receipts; withdrawal itself is neither proof of an expense nor a final denial of the underlying cost. |
| DONATION, CHARITY | Ordinary individual charitable gifts route to the T1 receipt/credit method; distinguish supported advertising/sponsorship rather than relabelling a gift a business expense. |

Practical statement formats vary. RBC, TD, BMO, Scotiabank and CIBC commonly supply CSV/PDF with date/description/debit/credit/balance; Desjardins may use withdrawal/deposit; Tangerine, Simplii and EQ Bank may use signed amounts; Wise/Revolut require currency/FX and transfer reconciliation. Inspect the actual export headers and period, not a promised current format. **e-Transfer/Interac** needs direction/counterparty; **PAD** only means pre-authorized debit, not deductible expense; **POS** means point of sale; **Direct Deposit** can be salary, sales or another receipt; **NSF** and **Service Charge** need the business-banking check. Preserve original records alongside the normalized ledger.

### 6. Calculate vehicle expenses and CCA separately [CRA vehicle expenses](https://www.canada.ca/en/revenue-agency/services/tax/businesses/small-businesses-self-employed-income/business-income-tax-reporting/business-expenses/motor-vehicle-expenses.html)

For each vehicle obtain total and business kilometres, actual receipts, acquisition/lease dates, passenger-vehicle classification and limits. Chart A generally multiplies allowable running costs by business kilometres / total kilometres. Add eligible business parking and supplementary business insurance separately. **9281 excludes CCA**; allowable business CCA goes to **9936**. A sole proprietor's own vehicle claim is not the employer per-kilometre allowance rate.

CRA's simplified logbook method starts with a representative full base-year log and a qualifying three-month sample in a later year, with its comparability limits. The annual estimate is `(sample-period business % / corresponding base-year-period business %) × base-year annual business %`. Check the CRA method and annual reasonableness, including the permitted range within 10 percentage points of the base-year annual business use (CRA's 49% example permits 39% to 59%), rather than treating any three months as enough. Without adequate support hold the claim open and obtain records; do not invent a business percentage. Keep separate vehicle records and avoid treating owner commuting/personal travel as proved business use.

For passenger-vehicle interest, leasing and capital cost use the actual acquisition/contract year, applicable sales-tax components and form formulas, not only a monthly headline. Chart B uses its day-based calculation; Chart C compares its lease limits. The limits below do not authorize a full deduction or erase business-use/ITC restrictions. [ITR 7307](https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/section-7307.html); [2025 form Charts B/C](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t2125/t2125-25e.pdf).

### 7. Reconcile capital cost allowance [ITA 20(1)(a)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-20.html)

CCA is discretionary up to the prescribed maximum, not compulsory accounting depreciation. Maintain class-by-class opening UCC, eligible additions and available-for-use dates, assistance/ITCs, dispositions, first-year adjustment, maximum, chosen claim and closing UCC. Establish business/personal allocation and apply actual pooling, short-year and restriction rules. Unclaimed CCA remains in UCC. Disposals can produce recapture or terminal loss; they are not automatically deductible sale losses. Class 10.1 passenger vehicles have special disposition/half-year rules and generally no ordinary recapture/terminal loss. Refer an actual disposal requiring those special calculations rather than using the acquisition examples below. [T4002 CCA and UCC](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4002/t4002-6.html).

#### Rates, bands and thresholds [ITR Schedule II](https://lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/page-91.html)

These are ordinary class rates or dated limits, not unconditional first-year write-offs. Each row's official source and year form part of the rule.

| Item | Amount / boundary | Year | Official source |
|---|---|---|---|
| Class 1 | Base 4% for qualifying buildings; eligible non-residential additional allowances can give 6%/10%, with the required election and actual conditions | 2025/2026 | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/report-business-income-expenses/claiming-capital-cost-allowance/classes.html |
| Class 8 | 20%, qualifying furniture/fixtures/equipment not in another class | 2025/2026 | https://lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/page-91.html |
| Class 10 | 30%, qualifying vehicles/equipment; distinguish 10.1 and specialized classes | 2025/2026 | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/report-business-income-expenses/claiming-capital-cost-allowance/classes.html |
| Class 10.1 | 30%, separate qualifying over-limit passenger vehicle; cost capped for its actual acquisition year | 2025/2026 | https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/section-7307.html |
| Class 12 | 100% class rate for specified property, including qualifying application software and specified tools/instruments/utensils costing less than $500; not all equipment below $500 | 2025/2026 | https://lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/page-91.html |
| Class 43 | 30%, eligible Canadian manufacturing/processing equipment outside the applicable other classes; 2016-2025 qualifying acquisitions can instead be Class 53 at 50% | Acquisition-dependent, including 2025/2026 | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/report-business-income-expenses/claiming-capital-cost-allowance/classes.html |
| Class 50 | 55%, qualifying general-purpose computer hardware/ancillary equipment and systems software; data network infrastructure can be Class 46, not automatically 50 | 2025/2026 | https://lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/page-91.html |
| Class 54 | 30%, qualifying ZEV otherwise generally Class 10/10.1; only the zero-emission passenger-vehicle subset has the passenger cost cap | 2025/2026 | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/report-business-income-expenses/claiming-capital-cost-allowance/classes-depreciable-property.html |
| Class 55 | 40%, qualifying ZEV otherwise Class 16, not all electric vehicles outside 54 | 2025/2026 | https://lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/page-91.html |
| Ordinary passenger capital-cost ceiling | $37,000 before applicable tax for 2024 acquisitions; $38,000 for 2025 | Acquisition years 2024/2025 | https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/section-7307.html |
| Announced ordinary passenger ceiling | $39,000 before applicable tax for acquisitions from January 1, 2026; current consolidated 7307 still says $38,000 after 2024, so codification is not yet confirmed | 2026 announcement versus regulation read November 13 | https://www.canada.ca/en/department-finance/news/2026/01/government-announces-the-2026-automobile-deduction-limits-and-expense-benefit-rates-for-businesses.html |
| Zero-emission passenger capital-cost ceiling | $61,000 before applicable tax; eligibility/capital-cost adjustments still apply | 2025/2026 acquisitions | https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/section-7307.html |
| Passenger interest and lease headline limits | $350/month interest; $1,100/month lease before applicable tax, using statutory/form formulas and actual contract dates | New 2025/2026 loans/leases; verify older dates separately | https://www.canada.ca/en/department-finance/news/2026/01/government-announces-the-2026-automobile-deduction-limits-and-expense-benefit-rates-for-businesses.html |

Application software's ordinary half-year rule differs from specified Class 12 items excluded from that rule. A qualifying incentive can change first-year treatment; a 100% class rate alone does not prove a full first-year deduction. Check ITR 1100(2), including its exclusions, rather than applying one rule to every Class 12 asset. [Current ITR 1100](https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/section-1100.html).

#### Select the enacted first-year route

**Do not call this CEBA.** The former eligible individual's designated immediate-expensing-property window required availability for use before 2025; that is distinct from current class-specific/enhanced CCA. Select the actual acquisition, availability, ownership/use and related-party conditions. [ITR 1104](https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/section-1104.html).

Current law distinguishes older **AIIP**, generally acquired after November 20, 2018 and before 2025 and available before 2028, from **RIIP**, acquired after 2024 and available before 2034, with the statutory prior-use/related-party tests. Classes 54 to 56 are excluded from the RIIP definition but have their own post-2024 first-year rules. The legislation was enacted March 26, 2026; applicable RIIP changes operate from January 1, 2025, with separate Class 50 provisions also addressing qualifying acquisition/availability after April 15, 2024. Older CRA “proposed” wording is not the legal status. [2026 c.3 ss103,105,106](https://laws-lois.justice.gc.ca/eng/AnnualStatutes/2026_3/page-18.html).

For a **simple full-year, no-disposition, no-other-pool-transaction case**:

- Ordinary qualifying RIIP, available before 2030, can use **1.5 × the full eligible net addition × the class rate**. That is not 1.5 times the ordinary half-year deduction. Older AIIP available in 2025/2026 can have a different phase-out result. Do not apply this ordinary factor to the excluded/special classes.
- Qualifying **Class 50** acquired and available in 2025 or 2026 can yield **100%**, from `55% × (1 + 9/11)`, subject to actual conditions. Qualifying post-April-15-2024 AIIP has its separate applicable route. A generic 82.5% laptop claim is not the current default.
- Qualifying post-2024 Class 54 and 55 ZEV first-year allowances can be **100% before 2030, 75% in 2030/2031, 55% in 2032/2033**. The added factors differ: Class 54 uses **2⅓ / 1½ / ⅚** with a 30% base; Class 55 uses **1½ / ⅞ / ⅜** with a 40% base. The CRA detailed-class page's repeated Class 54 factors under Class 55 conflict with current ITR 1100(2) A.1(h); use the legislation. Verify ZEV definition, availability, assistance, elections and used-property conditions before selecting either class.
- Eligible manufacturing equipment has its own Class 53/Class 43 transition and special first-year factors; it is not automatically the ordinary 1.5 route.

[ITR 1100(2), including A/A.1 and disposition offsets](https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/section-1100.html). For mixed additions/dispositions, assistance, short periods or special classes use the whole prescribed formula; the simple cases here are not a universal CCA engine. Check the announced 2026 passenger-limit/regulation difference before a final affected claim and record the position used.

#### Do not mix regular and administrative mixed-use CCA methods

CRA's regular method for property with a stable business-use proportion records the business part of additions in Area B/C and carries that part into the CCA pool. Its administrative method for changing annual use records full cost in the pool and allocates the calculated CCA to business use. These produce different UCC record bases even when the current deduction matches. Case 2 explicitly identifies both. Keep the chosen method, business percentage and rollforward consistent, especially on disposal; do not use full-cost CCA with a business-only opening UCC or vice versa. [T4002 Chapter 4, personal use of property](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4002/t4002-6.html).

### 8. Apply the home-office tests and income cap [ITA 18(12)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-18.html)

Qualify if the workspace is either **the principal place of business**, or used **exclusively** to earn business income **and** regularly and continuously to meet clients/customers/patients. Working at home, exclusive use by itself or an occasional meeting is not enough under the second route. Allocate eligible rent or mortgage interest, property tax, utilities, insurance and maintenance on a reasonable area basis, plus time where space is shared, and period where not used throughout the year. Mortgage principal is not interest. Basic home telephone service is not made deductible by including it in household costs. [CRA home expenses](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/report-business-income-expenses/completing-form-t2125/business-use-home-expenses.html).

Part 7 combines eligible current business costs, any properly chosen business home CCA and supported carryforward. Deduct no more than the non-negative income from the same business before this deduction. It cannot create/increase a loss; retain the unused amount for later qualifying deduction against the same business. Put the allowed claim at **9945**. Do not claim the same home costs in Part 4 or home CCA at both 9936 and Part 7. Claiming home CCA can affect principal-residence/change-of-use treatment; obtain specific review before choosing it. The area ratio alone does not establish eligibility or the income cap.

### 9. Complete net income, personal-tax handoff and review

Actual Part 4 **9368** includes allowable business CCA at 9936; **9369 = starting income/profit at 4A - 9368**. Part 5 then applies the person's share/T5013 income and applicable adjustments, including partner rebates and deductible unreimbursed partner costs, before **5D**. Apply home-office 9945 last: **9946 = 5D - 9945**. Ordinary business losses need the T1 loss rules; the home-office limitation is not a ban on all legitimate business losses. Do not bypass partnership adjustments or special deemed-zero loss rules merely because a spreadsheet subtracts expenses. [Actual form](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t2125/t2125-25e.pdf).

| T2125 output | T1 destination, actual observed 2025 layout |
|---|---|
| 8299 gross business / professional / commission income | 13499 / 13699 / 13899 respectively |
| 9946 net business / professional / commission income | 13500 / 13700 / 13900 respectively |

[ca-fed-t1-return](ca-fed-t1-return.md), “Rates, bands and thresholds” and Methods 4 to 5, supplies all five **2025** federal bands, blended first rate, BPA maximum/minimum and net-income phase-out, and the separately indexed **2026** equivalents. Use that exact dated table rather than the former incorrect 2025 bands or a rough combined provincial rate. Provincial tax is additional and depends on the actual jurisdiction; do not substitute a generic 20%-54% range for its computation.

CPP is **outside T2125**. The actual self-employed base component splits between a non-refundable credit and deduction; the first and second additional components have deduction treatment. It is not simply half of all CPP on 22200. [ca-fed-cpp-ei](ca-fed-cpp-ei.md) and [ca-fed-t1-return](ca-fed-t1-return.md), Method 3, select the year, ceilings, basic exemption, CPP2, age/months/elections and mixed T4/QPP coverage; Case 1 preserves a corrected dated comparison. Voluntary self-employed EI requires actual agreement/history. T2125 net income alone does not establish final contributions, taxable income or tax payable.

#### Spreadsheet working paper

Keep one row per source transaction and a separate tax-adjustment trail. Use these actual form destinations, not a second GST subtraction:

```text
A. Income / GST reconciliation
   3A inclusive business sales; 3B included taxes/returns/etc; 3C = 3A - 3B
   3D/3E/3F/3G quick-method reconciliation if applicable, OR professional 3N
   8000 adjusted sales/fees; 8290 prior reserves; 8230 other income
   8299 = 8000 + 8290 + 8230; hand off the appropriate T1 gross line
B. Direct costs, business part only
   8300 opening stock + 8320 purchases + 8340 direct wages + 8360 subcontracts
   + 8450 other direct costs - 8500 closing stock = 8518; 8519 = 8299 - 8518
C. Part 4 current costs and CCA
   8521 advertising; 8523 deductible meals; 8590 bad debts; 8690 insurance
   8710 interest/bank; 8760 taxes/licences/memberships; 8810 office
   8811 supplies; 8860 professional; 8871 management/admin; 8910 rent
   8960 repairs; 9060 wages/benefits; 9180 property taxes; 9200 travel
   9220 utilities; 9224 non-vehicle fuel; 9275 delivery; 9281 vehicle excluding CCA
   9936 business CCA excluding home CCA; 9270 other specified costs
   9368 = total Part 4 expenses including allowable CCA
   9369 = 4A (8299 or 8519 as applicable) - 9368
D. Capital schedule
   For each Class 1/8/10/10.1/12/43/50/54/55 or actual other class:
   opening UCC + eligible cost/adjustments - disposal adjustments
   select actual first-year method; maximum versus chosen claim; closing UCC
   business allocation and regular versus administrative method documented
E. Part 5/7
   5A actual share/sole-proprietor 9369 or T5013 input
   5B/9974 additions, 9943 partner deductions as applicable -> 5D
   home area/time/period; eligible costs + chosen home CCA + carryforward
   9945 = allowable home claim capped at max(0,5D); unclaimed carryforward retained
F. 9946 = 5D - 9945; hand off the appropriate T1 net line
   CPP/QPP/EI, RRSP and personal income tax stay outside this calculation
```

Review flags: vehicle log/receipts and allocation; home eligibility, measurements and income cap; prior UCC or verified zero opening; meals rate/exception and correct amount; unresolved classification, GST, capital/personal and reasonableness issues. Reconcile the spreadsheet to Parts 1/2 identification and Internet business activities, Part 6 partner deductions, Part 8 other partners where required and Part 9 equity details. A completed calculation is not proof that those reporting fields were completed.

## Boundary and exception table

| Situation | Action |
|---|---|
| Unknown GST status, category or business purpose | Obtain facts and isolate the pending amount; do not assert unregistered, personal or legally non-deductible as a fabricated default. |
| Missing home/vehicle/phone percentage | Obtain reasonable records, withhold an unsupported claim or show explicit conditional alternatives; do not invent the percentage. |
| Unknown CCA class or missing existing-pool UCC | Reconcile actual asset history before calculating; a first-year verified zero pool is possible. |
| Disproportionate expense | Review business connection, reasonableness and capital/personal content; no automatic merchant-based denial. |
| Quick method | Confirm valid election and eligible supplies; ordinary ITC/net-expense defaults are unsafe. |
| Tax deductions versus cash payments | Owner drawings, tax, loan principal, transfers and credit-card settlement are not new current costs. Trace the underlying event. |
| Source disagreement | Record date and hierarchy; enacted 1100/1104 prevail over stale proposed labels and the Class 55 web typo. Do not pretend the announced 2026 passenger cap is already in the consolidated text. |
| A person named on an older version | Historical credit is not approval of this substantive replacement. AI source review and a Git commit do not create accountant approval. |

## Worked cases

These are fictional component calculations, not filed returns. Costs are on the verified income-tax/GST basis stated, with no duplicate ITC claims. Every CCA case assumes a full year and no other pool transactions unless stated.

### Case 1. Developer, home office and dated CPP bridge

Reconciled adjusted business income is **$95,000**, after applicable sales-tax/return adjustments; no other income/reserves or closing stock. Direct subcontract costs are $8,000 at 8360. Eligible current software service $2,400, accounting $1,500, travel $3,000 and ordinary reasonable meals $1,200 give a $600 meals claim at 8523. GST liability/effective dates have been separately resolved; annual turnover alone does not prove registration dates.

A qualifying principal workspace is 150 of 1,200 square feet, used solely for business throughout the year. Eligible home mortgage interest $8,000 + property tax $4,000 + utilities $3,600 + insurance $1,800 = $17,400. No home CCA or carryforward. Area share 12.5% gives $2,175, below the income cap. Current/direct costs plus home claim are $17,675; net 9946 is **$77,325**. Treating subcontracts as direct costs changes the intermediate gross profit, not this final result.

```oa-check
name: T2125 developer with qualifying home office
inputs:
  revenue: 95000
  subcontract: 8000
  software: 2400
  accounting: 1500
  travel: 3000
  meals: 1200
  area: 150
  total_area: 1200
steps:
  business_share: area / total_area
  home_costs: 8000 + 4000 + 3600 + 1800
  meals_allowed: meals * 0.5
  other_costs: software + accounting + travel + meals_allowed
  direct_and_current: subcontract + other_costs
  gross_profit: revenue - subcontract
  pre_home: gross_profit - other_costs
  home_claim: min(home_costs * business_share, max(0, pre_home))
  all_deductions: direct_and_current + home_claim
  net_income: pre_home - home_claim
expected:
  business_share: 0.125
  home_costs: 17400
  meals_allowed: 600
  other_costs: 7500
  direct_and_current: 15500
  gross_profit: 87000
  pre_home: 79500
  home_claim: 2175
  all_deductions: 17675
  net_income: 77325
```

For the **same $77,325** of net earnings, the following comparison assumes full-year CPP-only self-employment, no employment earnings, no QPP, no disability/election/month adjustment and no other relevant amounts. It is outside T2125. The 2025 first band is $67,800 and upper band $6,025; 2026 first band $71,100 and upper band $2,725. Actual [2025 Schedule 8](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5000-s8/5000-s8-25e.pdf) and the contribution method control credit/deduction/payable selection.

```oa-check
name: CPP comparison outside T2125 for developer
inputs:
  earnings: 77325
steps:
  first_2025: min(max(earnings - 3500, 0), 71300 - 3500)
  upper_2025: min(max(earnings - 71300, 0), 81200 - 71300)
  base_2025: round(first_2025 * 0.099, 2)
  enhanced_2025: round(first_2025 * 0.02, 2)
  cpp2_2025: round(upper_2025 * 0.08, 2)
  total_2025: base_2025 + enhanced_2025 + cpp2_2025
  credit_base_2025: base_2025 / 2
  deduction_2025: base_2025 / 2 + enhanced_2025 + cpp2_2025
  first_2026: min(max(earnings - 3500, 0), 74600 - 3500)
  upper_2026: min(max(earnings - 74600, 0), 85000 - 74600)
  base_2026: round(first_2026 * 0.099, 2)
  enhanced_2026: round(first_2026 * 0.02, 2)
  cpp2_2026: round(upper_2026 * 0.08, 2)
  total_2026: base_2026 + enhanced_2026 + cpp2_2026
  credit_base_2026: base_2026 / 2
  deduction_2026: base_2026 / 2 + enhanced_2026 + cpp2_2026
expected:
  first_2025: 67800
  upper_2025: 6025
  base_2025: 6712.20
  enhanced_2025: 1356
  cpp2_2025: 482
  total_2025: 8550.20
  credit_base_2025: 3356.10
  deduction_2025: 5194.10
  first_2026: 71100
  upper_2026: 2725
  base_2026: 7038.90
  enhanced_2026: 1422
  cpp2_2026: 218
  total_2026: 8678.90
  credit_base_2026: 3519.45
  deduction_2026: 5159.45
```

The base-credit amounts are contribution amounts entering the credit calculation, not tax-credit dollars. Do not subtract either CPP total from 9946. [CPP ceilings](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/payroll-deductions-contributions/canada-pension-plan-cpp/cpp-contribution-rates-maximums-exemptions.html); [CPP2 ceilings](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/calculating-deductions/making-deductions/second-additional-cpp-contribution-rates-maximums.html).

### Case 2. Vehicle operating costs and three distinct CCA histories

25,000 total km and 15,000 supported business km give **60%**. Fuel $3,600 + insurance $2,400 + repairs $800 + licence $120 = $6,920; ordinary business running costs **$4,152** at 9281. No parking/supplementary business insurance is assumed.

For a Class 10 vehicle, a $36,000 purchase price does not prove a $36,000 opening UCC. Compare three separately supported histories, using CRA's **administrative full-cost pool method** with actual business use allocated after computing full-pool CCA:

- Continuing full-cost opening UCC $36,000, no additions/disposals: full-pool CCA $10,800, business $6,480, full-pool closing UCC $25,200; operating plus CCA **$10,632**.
- Eligible 2025/2026 RIIP addition $36,000, zero opening UCC, no other transactions: full-pool first-year CCA $16,200, business $9,720, full-pool closing UCC $19,800; combined deduction **$13,872**.
- Otherwise applicable non-incentive half-year addition $36,000: full-pool CCA $5,400, business $3,240, full-pool closing UCC $30,600; combined **$7,392**. Do not use this branch where an incentive actually applies.

For the RIIP case under CRA's **regular stable-use method**, the business addition is instead $21,600; maximum CCA is $9,720 and closing **business-only UCC $11,880**. It is not the $19,800 full-cost administrative balance. The deduction matches in this simplified case, but the pool records are different. Actual Class 10/10.1, cost ceiling, sales tax/ITCs, acquisition/availability, prior use, short-year and method conditions are established before any branch is selected.

```oa-check
name: Vehicle costs with explicit CCA pool bases
inputs:
  total_km: 25000
  business_km: 15000
  amount: 36000
steps:
  share: business_km / total_km
  operating: 3600 + 2400 + 800 + 120
  business_operating: operating * share
  continuing_pool_cca: amount * 0.30
  continuing_business_cca: continuing_pool_cca * share
  continuing_ucc: amount - continuing_pool_cca
  continuing_total: business_operating + continuing_business_cca
  riip_pool_cca: amount * 1.5 * 0.30
  riip_business_cca: riip_pool_cca * share
  riip_full_cost_ucc: amount - riip_pool_cca
  riip_total: business_operating + riip_business_cca
  half_pool_cca: amount * 0.5 * 0.30
  half_business_cca: half_pool_cca * share
  half_ucc: amount - half_pool_cca
  half_total: business_operating + half_business_cca
  regular_business_addition: amount * share
  regular_cca: regular_business_addition * 1.5 * 0.30
  regular_business_ucc: regular_business_addition - regular_cca
expected:
  share: 0.6
  operating: 6920
  business_operating: 4152
  continuing_pool_cca: 10800
  continuing_business_cca: 6480
  continuing_ucc: 25200
  continuing_total: 10632
  riip_pool_cca: 16200
  riip_business_cca: 9720
  riip_full_cost_ucc: 19800
  riip_total: 13872
  half_pool_cca: 5400
  half_business_cca: 3240
  half_ucc: 30600
  half_total: 7392
  regular_business_addition: 21600
  regular_cca: 9720
  regular_business_ucc: 11880
```

[CRA CCA personal-use methods](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4002/t4002-6.html); [current first-year law](https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/section-1100.html).

### Case 3. Ordinary client meals

$2,500 of eligible reasonable client-meeting restaurant costs, with no statutory full/80% exception, permits **$1,250**. Enter the allowable $1,250 at 8523 and retain $1,250 disallowed in the reconciliation. Do not enter $2,500 and invent a second T2125 add-back. This does not deny a properly established long-haul or statutory full-deduction exception.

```oa-check
name: Ordinary client meal limitation
inputs:
  actual: 2500
  reasonable: 2500
steps:
  base: min(actual, reasonable)
  allowed: base * 0.5
  disallowed: actual - allowed
expected:
  base: 2500
  allowed: 1250
  disallowed: 1250
```

[ITA 67.1](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-67.1.html).

### Case 4. $2,800 laptop, with actual acquisition history

Assume Class 50, 100% business use, full year, verified capital cost $2,800 after tax/assistance adjustments, no other pool items/disposals, maximum CCA chosen. A qualifying RIIP laptop acquired and available in **2025 or 2026** has first-year CCA **$2,800**, closing UCC **$0**. The former $2,310/remaining $490 is not its current default.

For comparison only, an eligible historical AIIP laptop acquired and available in **2023** can produce $2,310 and UCC $490. An AIIP laptop acquired **before April 16, 2024**, first available in **2025**, can have $1,540 and UCC $1,260 under the older phase-out route; a separately applicable non-incentive half-year case gives $770 and UCC $2,030. None of these historical/nonqualifying assumptions may be substituted for the facts of the 2025/2026 RIIP purchase.

```oa-check
name: Class 50 dated first-year comparisons
inputs:
  cost: 2800
  rate: 0.55
steps:
  riip_cca: min(cost, cost * rate * (1 + 9 / 11))
  riip_ucc: cost - riip_cca
  historical_2023_cca: cost * rate * 1.5
  historical_2023_ucc: cost - historical_2023_cca
  older_aiip_cca: cost * rate
  older_aiip_ucc: cost - older_aiip_cca
  non_incentive_cca: cost * rate * 0.5
  non_incentive_ucc: cost - non_incentive_cca
expected:
  riip_cca: 2800
  riip_ucc: 0
  historical_2023_cca: 2310
  historical_2023_ucc: 490
  older_aiip_cca: 1540
  older_aiip_ucc: 1260
  non_incentive_cca: 770
  non_incentive_ucc: 2030
```

[ITR 1100(2)](https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/section-1100.html); [1104 eligibility](https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/section-1104.html).

## When to refuse or refer

- A corporation requires the T2 method; do not put corporate activity on an individual's T2125.
- An individual partner may still need T2125. Obtain T5013/financial statements and refer allocations, limited/non-active partnership restrictions or special deductions requiring the partnership method. Do not reconstruct an allocation from bank distributions. [T4068](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4068/guide-partnership-information-return-t5013-forms.html).
- Non-resident/part-year, foreign permanent establishment, treaty/source/withholding and multi-jurisdiction cases require actual residence/source facts and the applicable specialist method. Domestic sole-proprietor assumptions do not settle them.
- SR&ED credits, farming **T2042** and fishing **T2121** require their separate methods/forms. A capital-versus-current classification here does not determine an SR&ED credit.
- Refuse to fabricate receipts, unsupported allocations, a registration/election, CCA eligibility or accountant approval. Present the supported work and open items for an authorized accountant to resolve before filing; do not certify the examples as the client's completed return.

## Filing and payment

T2125 accompanies the individual's T1; it is not a separately remitted income-tax payment. Use eligible certified NETFILE/EFILE or the applicable filing route; personal tax uses CRA My Account/authorized representative access, whereas GST business returns have their own business filing route. Do not request account passwords in a working paper. [T4002 filing](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4002/t4002-4.html).

| Obligation | Date / conditions | Official source |
|---|---|---|
| Qualifying self-employed 2026 T1 | June 15, 2027 filing, but April 30, 2027 balance payment; check actual business/spouse and tax-shelter conditions | https://www.canada.ca/en/services/taxes/resources-for-small-and-medium-businesses/2026-tax-deadlines-canadian-businesses-self-employed-individuals.html |
| Dated 2025 T1 bridge | June 15, 2026 qualifying filing; April 30, 2026 balance payment; use actual 2025 form/amounts | https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-150.html |
| Personal instalments | March/June/September/December 15 subject to business-day rules, actual net-tax-owing test, reminders and calculation option; follow T1 Method 7 | https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/due-dates.html |
| Ordinary T4A reporting for 2026 | Last day of February 2027 falls Sunday, so March 1, 2027 ordinarily; cessation/death or a different slip can change the due date | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/file-information-returns-slip-summaries/when-to-file.html |
| GST/HST annual individual exception | June 15 filing/April 30 payment following year only where all three conditions hold: annual filer, December 31 fiscal end, individual with business income | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/file-gst-hst-return/reporting-requirements-deadlines.html |
| Other GST/HST periods | Generally three months after year end for other annual filers; one month after period end for monthly/quarterly filers, with applicable business-day rules | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/file-gst-hst-return/reporting-requirements-deadlines.html |

**Subcontractor reporting is separate from the expense claim.** Establish actual services paid, worker status, recipient/residence and industry. Most resident service-fee reporting uses T4A **048**, excluding GST/HST/PST; CRA's dedicated payer policy says more than $500 total annual payments or any tax withheld. The general fees page's Step 2 says “at least” $500 while Step 3 and the dedicated payer page say “more than”; record the administrative-policy wording rather than inventing a universal statutory $500 exemption. Employees use T4; construction, non-resident and federal-government payments can require T5018, T4A-NR or T1204 and their own conditions/withholding. General box-048 penalty relief does not abolish reporting; CRA's 2025-onward trucking-industry CCPC policy has particular exceptions to that relief. [Fees-for-services steps](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/payroll-deductions-contributions/special-payments/fees-other-amounts-services.html); [dedicated T4A payer conditions](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/completing-filing-information-returns/t4a-information-payers/t4a-slip.html).

**Penalties and interest:** ordinary late T1 filing is 5% of unpaid tax at the filing deadline plus 1% per complete late month, maximum 12. The increased 10% plus 2% per complete month, maximum 20, requires the statutory demand and prior-penalty history within the preceding three years; a second late return alone is insufficient. Payment/instalment interest is separate and uses the actual period's prescribed rates/payment facts. The T1 method owns the detailed instalment test and computations. [ITA 162](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-162.html).

ITA 163(2) concerns a knowingly made or grossly negligent false statement/omission and imposes the **greater of $100 and 50% of the defined statutory tax/credit amount**. It is not an automatic 50% penalty for every ordinary mistake or every disallowed cost; refer an actual penalty dispute for specific advice. [ITA 163](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-163.html).

## Completion checklist

- Actual person/entity, year, residence/province, business/profession, fiscal period/election, BN/program account, NAICS and Internet reporting established.
- Bank/processor/card totals reconciled to actual accrual sales, tax, returns, receivables/payables, stock, loans and owner movements; no duplicate transfers or slip income.
- Each expense has evidence, period, business purpose/share, correct tax basis and form destination. Meals, financing, legal, training, dues and capital items receive their actual tests.
- Vehicle log/receipts and home eligibility/area/time/income cap supported; missing evidence remains an explicit open item, not an invented fact.
- CCA cost/UCC reconciled, with acquisition/availability, incentive, method, tax/assistance, dispositions and claim choice recorded; separate 9281/9936/home CCA maintained.
- 8299/8519/9368/9369/5D/9945/9946 reconciled and gross/net amounts handed to their actual T1 lines. Home carryforward and CCA closing UCC retained on their correct bases.
- Personal CPP/QPP/EI, RRSP, federal/provincial tax, credits, instalments and final balance completed by the appropriate methods, outside business expenses.
- Filing/payment and information-return obligations identified separately. Working paper is estimated/proposed where facts or final annual forms remain open, with professional sign-off before filing; no transaction, filing or payment executed by this skill.

## Sources

Primary official sources were read on **2026-11-13** for the relevant portions, not every unrelated regime on a long page. Justice's displayed consolidation is current to October 19, 2026, last amended June 18, 2026. Read dates are not tax years. Actual annual forms observed are 2025. The current statutory CCA rules, their enactment/application dates and the explicitly identified guidance conflicts control this method.

| Source / actual scope | URL | Read on |
|---|---|---|
| Read for Actual 2025 T2125, Parts 1-9, Charts A-C and CCA areas | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t2125/t2125-25e.pdf | 2026-11-13 |
| Read for T2125 annual catalogue | https://www.canada.ca/en/revenue-agency/services/forms-publications/forms/t2125.html | 2026-11-13 |
| Read for T4002 Chapter 2, identification, individual partners, Parts 3A-C and assistance | https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4002/t4002-4.html | 2026-11-13 |
| Read for Accounting methods, ordinary accrual and exceptions | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/accounting-methods.html | 2026-11-13 |
| Read for ITA 9, business profit | https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-9.html | 2026-11-13 |
| Read for ITA 18(1), current/capital/personal/club restrictions; 18(12), home | https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-18.html | 2026-11-13 |
| Read for ITA 67, reasonableness | https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-67.html | 2026-11-13 |
| Read for ITA 20(1)(a)/(c)/(e), CCA/interest/financing; 20(10), conventions | https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-20.html | 2026-11-13 |
| Read for CRA 8710 interest and fee timing | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/report-business-income-expenses/completing-form-t2125/line-8710-interest.html | 2026-11-13 |
| Read for CRA 8871 processing-payment charges | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/report-business-income-expenses/completing-form-t2125/line-8871-management-administration-fees.html | 2026-11-13 |
| Read for T4002 Chapter 3, current/capital, expense categories and home/telephone rules | https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4002/t4002-5.html | 2026-11-13 |
| Read for ITA 67.1, ordinary meals, eligible long-haul and full exceptions | https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-67.1.html | 2026-11-13 |
| Read for CRA home allocation, loss cap, carryforward and CCA consequences | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/report-business-income-expenses/completing-form-t2125/business-use-home-expenses.html | 2026-11-13 |
| Read for Vehicle expenses and full/sample logbooks | https://www.canada.ca/en/revenue-agency/services/tax/businesses/small-businesses-self-employed-income/business-income-tax-reporting/business-expenses/motor-vehicle-expenses.html | 2026-11-13 |
| Read for T4002 Chapter 4, UCC, claims/disposals and both personal-use methods | https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4002/t4002-6.html | 2026-11-13 |
| Read for ITR 1100, current rates and complete first-year formula/exclusions | https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/section-1100.html | 2026-11-13 |
| Read for ITR 1104, AIIP/RIIP and individual immediate-expensing windows | https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/section-1104.html | 2026-11-13 |
| Read for 2026 c.3 s103, actual enactment and applicability | https://laws-lois.justice.gc.ca/eng/AnnualStatutes/2026_3/page-17.html | 2026-11-13 |
| Read for 2026 c.3 ss105/106, actual RIIP definitions/application | https://laws-lois.justice.gc.ca/eng/AnnualStatutes/2026_3/page-18.html | 2026-11-13 |
| Read for ITR Schedule II, actual relevant class descriptions | https://lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/page-91.html | 2026-11-13 |
| Read for CRA common class rates and Class 1/43/53 conditions | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/report-business-income-expenses/claiming-capital-cost-allowance/classes.html | 2026-11-13 |
| Read for CRA detailed classes; Class 55 guidance conflict identified above | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/report-business-income-expenses/claiming-capital-cost-allowance/classes-depreciable-property.html | 2026-11-13 |
| Read for ITR 7307, actual passenger cost/interest/lease limits | https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/section-7307.html | 2026-11-13 |
| Read for Finance January 14, 2026 auto-limit announcement | https://www.canada.ca/en/department-finance/news/2026/01/government-announces-the-2026-automobile-deduction-limits-and-expense-benefit-rates-for-businesses.html | 2026-11-13 |
| Read for T4002 vehicle definitions, with older proposed annotations bounded by current law | https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4002/t4002-2.html | 2026-11-13 |
| Read for ETA 148, small suppliers | https://laws-lois.justice.gc.ca/eng/acts/E-15/section-148.html | 2026-11-13 |
| Read for ETA 240, registration | https://laws-lois.justice.gc.ca/eng/acts/E-15/section-240.html | 2026-11-13 |
| Read for CRA registration timing/examples | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/when-register-charge.html | 2026-11-13 |
| Read for CRA Part 3A gross/adjusted sales | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/report-business-income-expenses/completing-form-t2125/part-1-business-income.html | 2026-11-13 |
| Read for RC4058, quick method, ITCs and credit | https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4058/quick-method-accounting-gst-hst.html | 2026-11-13 |
| Read for GST/HST reporting and deadlines | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/file-gst-hst-return/reporting-requirements-deadlines.html | 2026-11-13 |
| Read for Fees-for-services reporting; actual step-wording conflict | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/payroll-deductions-contributions/special-payments/fees-other-amounts-services.html | 2026-11-13 |
| Read for T4A payer conditions | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/completing-filing-information-returns/t4a-information-payers/t4a-slip.html | 2026-11-13 |
| Read for Information-return due dates/business-day rule | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/file-information-returns-slip-summaries/when-to-file.html | 2026-11-13 |
| Read for ITA 249.1, fiscal period/election/changes | https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-249.1.html | 2026-11-13 |
| Read for T1139 observed 2025 catalogue | https://www.canada.ca/en/revenue-agency/services/forms-publications/forms/t1139.html | 2026-11-13 |
| Read for ITA 163(2), actual penalty condition/base | https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-163.html | 2026-11-13 |
| Read for Archived IT-357R2, current/capital training interpretation only | https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/it357r2/archived-expenses-training.html | 2026-11-13 |
| Read for T4068, individual partner responsibilities | https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4068/guide-partnership-information-return-t5013-forms.html | 2026-11-13 |
| Read for Actual 2025 Schedule 8, contribution split and conditions | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5000-s8/5000-s8-25e.pdf | 2026-11-13 |
| Read for CPP annual contribution limits | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/payroll-deductions-contributions/canada-pension-plan-cpp/cpp-contribution-rates-maximums-exemptions.html | 2026-11-13 |
| Read for CPP2 annual limits | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/calculating-deductions/making-deductions/second-additional-cpp-contribution-rates-maximums.html | 2026-11-13 |
| Read for 2026 income/2027 filing/payment dates | https://www.canada.ca/en/services/taxes/resources-for-small-and-medium-businesses/2026-tax-deadlines-canadian-businesses-self-employed-individuals.html | 2026-11-13 |
| Read for ITA 150(1), actual filing conditions | https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-150.html | 2026-11-13 |
| Read for ITA 162(1)/(2), ordinary/increased filing penalty | https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-162.html | 2026-11-13 |
| Read for Personal instalment dates | https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/due-dates.html | 2026-11-13 |

Not yet confirmed: the final 2026 annual T2125/T1139 presentation, codification of the announced 2026 $39,000 ordinary passenger ceiling in the consolidation inspected, and any client's missing evidence or elections. This is not a claim of accountant approval or a completed filing. Historical names/dates in Git do not approve this revised method.
