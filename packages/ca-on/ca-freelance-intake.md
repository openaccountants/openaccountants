---
name: ca-freelance-intake
description: Collect and reconcile the records for a Canadian-resident sole proprietor's tax work before preparing returns. Read available records first, confirm the year, residence, business and tax accounts, distinguish evidence from assumptions, fill only material gaps, and hand a complete or explicitly incomplete intake to ca-return-assembly. Includes employment and other income, GST/HST and Quebec coordination, fiscal periods, expenses, assets, home and vehicle use, RRSP records, contributions and instalments. Covers 2026 planning with a dated 2025 filing bridge; a focused question does not require an entire return intake.
version: 0.2
jurisdiction: CA
tax_year: 2026
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
category: orchestrator
type: filing-howto
---

# Canada: freelance tax intake

## Scope

Prepare an evidence-backed intake for a full-year Canadian-resident individual operating an unincorporated sole proprietorship or professional practice. Collect facts, reconcile records, resolve gaps and hand off the actual package. This method does not itself calculate the final T1, business profit, GST/HST return or contribution liability. Each applicable calculation still needs its current method and actual inputs. Canadian income reporting includes employment, each business, property and other relevant sources; no employment slip does not mean business income is the whole return. [F12] [F33] [F37]

**Start with the work requested.** For a full return, use the whole intake below. For a specific question, existing record correction or one instalment decision, reuse known facts and collect only the facts that change that answer; load the relevant component directly. Do not force a full return, another upload or questions already answered merely because the person is self-employed. If a full package is requested, keep every relevant income source and required return in its completion register.

**Year control:** this version covers 2026 planning and intake, with an explicitly dated 2025 filing/amendment bridge. Preserve the actual requested year, business fiscal periods, GST periods, contribution dates and any different instalment year. A 2025 form, receipt period or filing date is not a final 2026 form. Recheck the actual annual forms and filing channel before describing output as filing-ready. [F25] [F26] [F40]

**The accountant behind the method:** record the returned version, year, source dates, actual approval label and approving accountant for each method consumed. Preserve `Approved by [name]` or `Not yet approved` exactly as returned for that version. At the 14 November 2026 source audit, no approving name was supplied for this replacement; use the actual current returned approval rather than treating that dated audit record as a permanent status. A country directory, an accountant working on another skill, an AI source review, the preparer's identity or a historic approval does not approve this intake, its children or the user's return. A professional preparing a client's work receives the working paper for their own actual review; do not redirect them to another accountant as a mandatory step.

Read the whole available case, prior intake, documents, correspondence and previous outputs before asking. Resolve contradictions against the evidence; ask only for what remains missing or conflicting. Use available structured questions where helpful and ordinary grouped questions otherwise. No particular assistant, unavailable tool name, local path or fixed number of turns is required. Never invent zero, false, a date or an election to make the handoff look complete.

## Ask the client first

After reading the record, obtain missing facts in these six groups. Keep a confirmed fact; do not repeat the opening sweep at each component.

1. **Task, year and residence:** full return, estimate, amendment or focused question; relevant year and any later instalment year; full-year tax residence and moves; year-end province and business locations; actual taxpayer/entity and whether a professional acts for a client.
2. **Business and tax accounts:** each sole proprietorship/profession and industry; start/stop dates, ownership and actual fiscal periods; GST/HST and QST status, account, registration/cancellation dates, reporting periods and elections; associations, taxable supply history and exceptional activities where relevant.
3. **Income and records:** business books, bank/card records, invoices, receivables/payables and inventory; all employment, investment, rental, capital, foreign and other income; amended/missing slips and any outstanding returns or assessments.
4. **Expenses and assets:** receipts, contracts and business purpose, private use, capital additions/disposals, UCC and carryforwards; home qualification/costs and vehicle logs, including base/sample records if applicable.
5. **Personal and contribution facts:** family/dependant circumstances that affect the requested work; RRSP statements, previously reported unused contributions and receipts; all CPP/QPP/second-tier, EI/QPIP slips and coverage/pension/election/participation dates.
6. **Payments and handoff:** current and prior assessments/reminders, actual withholding, instalment receipts and account allocation; unresolved facts and who can supply them; required outputs and any existing review or filing authorization.

The relevant forms and official rules determine which facts are material. [F01] [F10] [F12] [F14] [F16] [F23] [F27] [F28] [F35] [F50] [F49] [F40]

## The method, step by step

### 1. Open briefly and establish the actual scope

A suitable opening, adapted to what is already known:

> I'll read the records you have for the requested year, confirm the gaps, and prepare the intake for the return work.

Do not promise a completion time, a prepared workbook before it exists, or an automatic filing. Do not require a universal CPA sign-off as a statement of Canadian tax law. Record the actual service/review agreement and filing channel; T183 is authorization for an electronic filer, not approval supplied by this intake. [F50]

The original six opening subjects remain. Offer options only for unanswered questions, and use the person's documents rather than an unsupported default:

| Subject | Useful choices or evidence | Consequence |
|---|---|---|
| Residence | Established full-year Canadian tax residence; part-year; non-resident; uncertain. Record dates and supporting facts. | Full-year sole-proprietor computation can proceed within this scope. An unresolved or different residence route stays visible and needs the appropriate method before final tax is settled. Physical presence alone is not the residence decision. [F49](https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/information-been-moved/determining-your-residency-status.html) |
| Structure | Sole proprietor/professional practice; incorporated business; partnership; unclear. Read incorporation/registration records, agreements and who earns the income. | A trade name or personal invoice does not prove the entity. Keep corporate/partnership work separate; continue supported personal-income collection. [F15](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4068/guide-partnership-information-return-t5013-forms.html) [F33](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/personal-income/self-employment-income-lines-13499-14299-gross-income-lines-13500-14300-net-income.html) [F37](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-2.html) [F43](https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/section-229.html) [F44](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/corporations/corporation-income-tax-return/who-file-a-corporation-income-tax-return.html) |
| Province | Ontario, British Columbia, Quebec, Alberta, Manitoba, Saskatchewan, Nova Scotia, New Brunswick, Prince Edward Island, Newfoundland and Labrador, Yukon, Northwest Territories or Nunavut; actual dated moves. | Confirm year-end province for the personal return, business establishments for multi-jurisdiction work, and supply facts separately for GST/HST. [F08](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/charge-collect-place-supply.html) [F34](https://www.canada.ca/en/revenue-agency/services/forms-publications/forms/t2203.html) |
| GST/HST | Account/effective status supported by records; not registered; uncertain. Preserve normal versus simplified status and QST separately. | Tax on an invoice is a clue, not proof of valid registration; no tax on an invoice is not proof of exemption or small-supplier status. [F05](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-240.html) [F06](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-166.html) [F07](https://www.canada.ca/en/revenue-agency/services/e-services/digital-services-businesses/confirming-a-gst-hst-account-number.html) |
| Employment | No known employment; one or several slips; amended/missing slips; uncertain. | A confirmed absence can settle that item, not every other income source. Obtain actual contribution tiers and other income. [F12](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-3.html) [F27](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/tax-slips/understand-your-tax-slips/t4-slips/t4-statement-remuneration-paid.html) |
| Industry | Software/IT; professional services including accounting, legal or consulting; trades; creative work; other/multiple. | Use for business descriptions, records and relevant questions, not automatic expense deduction, employee/self-employed status or zero-rating. [F14](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/business-records.html) [F33](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/personal-income/self-employment-income-lines-13499-14299-gross-income-lines-13500-14300-net-income.html) |

Do not say that every partnership must file T5013. The CRA guide distinguishes the regulation from its administrative filing policy, including the financial thresholds and partner/tiered/resource/request branches. Obtain the agreement, actual partners, ownership/allocations and T5013 or financial statements as applicable; route the partnership return separately. An individual partner's own reporting remains a distinct job. [F15]

### 2. Collect available records first

Ask for what the user has for the actual year/period. Accept a partial set, index it and work from it; do not demand every item before doing useful independent work.

- Business bank and card statements, CSV exports, invoices, sales records, contracts and cash records. Include accounts used for the business even if personally named.
- Purchase receipts, expense records, refunds and credit notes; loans, transfers, owner contributions/draws, advances and assistance.
- Prior T1/NOA/NOR and business schedules, current reassessments, loss/credit balances, UCC and home-office carryforwards. A prior assessment is not the complete underlying return or an instalment reminder.
- Employment T4/RL and other applicable slips, including amendments; investment, pension/benefit, rental, capital, foreign and other-income records.
- GST/HST/QST registration notices, account and reporting-period records, elections, filed/draft returns, assessments, refunds, payment evidence and correspondence.
- RRSP/PRPP/SPP receipts, the latest deduction-limit/unused-contribution statement, prior Schedule 7, transfers and HBP/LLP records.
- Vehicle expenses, acquisition/lease/finance documents and total/business travel logs; full base and matching sample records where relevant.
- Home workspace facts, area/time records, qualifying-use evidence and actual rent or ownership expenses.
- Capital purchase/disposal invoices, available-for-use dates and prior class/pool history.
- Any other CRA/RQ notices, filings, authorizations and relevant records already held.

For discovery, point to the person's existing bank exports, CRA/RQ accounts, invoices/email, prior accountant, or their document storage. Do not claim an account was accessed or a file read when it was unavailable. Use redacted records where sufficient for the calculation; a full SIN is not necessary to demonstrate a business-income estimate. Retain the SIN field for an actually authorized filing workflow without copying it into ordinary summaries.

Create a document index with ID, owner/entity, type, period, currency, version/amendment, pages/rows actually read, source and any missing/unreadable portion. Retain source documents and separate businesses; a transport/download success is not a reading or reconciliation. [F14]

### 3. Extract facts and reconcile, without turning clues into conclusions

Use an evidence status for each material fact: **document-supported, user-confirmed, provisional, missing, conflict or not applicable**. These are working statuses, not public trust labels. A source document can itself conflict with another source; document-supported does not mean every legal condition has been established.

| Record | Extract and retain | Reconciliation and missing-data control |
|---|---|---|
| Bank/card/cash records | Dates, signed amounts, currency, counterparty/reference, account, recurring receipts, refunds, transfers, CRA/RQ payments, RRSP-provider payments and possible expense/asset items. | Deposits are candidate receipts, not automatically taxable sales. Separate loans, capital, draws, internal transfers, GST, customer receipts and prior/current-period balances; trace invoices and receivables/payables. Merchant names do not prove deductibility, a contribution or the tax-payment account/year. [F13](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/accounting-methods.html) [F14](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/business-records.html) [F35](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/claim-amounts-tax-return.html) [F36](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/how-pay.html) |
| Sales invoices/contracts | Business/customer, supply type/date/place, address evidence, currency, gross/net/tax, registration evidence, credit notes, amounts earned/unpaid and foreign customers. | No universal rate from the seller's province. A foreign name alone does not prove zero-rating. Match turnover to books and bank/cash with timing, currency and non-sales adjustments. [F08](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/charge-collect-place-supply.html) [F13](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/accounting-methods.html) [F14](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/business-records.html) |
| Expenses | Supplier, receipt, business purpose, dates, amount/currency/tax, reimbursement, business/private allocation, current/capital distinction and evidence of recoverable GST/HST. | Categorize supplies, subscriptions, memberships, insurance, accounting, rent, travel, meals and equipment without promising deductions. Keep personal/club/non-business items separately; use the current T2125/GST methods for eligibility and limitations. [F09](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-169.html) [F14](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/business-records.html) [F18](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/report-business-income-expenses/completing-form-t2125/business-use-home-expenses.html) [F41](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-18.html) [F42](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-67.1.html) |
| Prior returns/assessments | Actual year/version, net income 23600, taxable income 26000, tax/withholding/balance, each business result, RRSP statement, losses, CCA/UCC, home carryforward and reassessments. | A refund or T1 balance is not instalment NTO or the prescribed base; an NOA is not INNS1. Do not copy an old year into the current estimate. [F23](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/rrsps-related-plans/contributing-a-rrsp-prpp/where-you-find-your-rrsp-prpp-deduction-limit.html) [F28](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-22200-deduction-cpp-qpp-contributions-on-self-employment-other-earnings.html) [F35](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/claim-amounts-tax-return.html) |
| T4/RL and contribution records | All slips and amendment status; employment income, CPP/QPP first and second tiers, EI, RPP, tax withheld, pension adjustment, dues, pensionable/insurable earnings, QPIP and employment province. | Preserve separate components and coverage dates rather than subtracting one total from a self-employed maximum. Confirm DOB, pension, disability and elections before applicable forms/proration. Quebec and mixed CPP/QPP have distinct routes. [F27](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/tax-slips/understand-your-tax-slips/t4-slips/t4-statement-remuneration-paid.html) [F28](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-22200-deduction-cpp-qpp-contributions-on-self-employment-other-earnings.html) [F29](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/cpp/canada-pension-plan-cpp-contributions-cpp-working-beneficiaries.html) [F30](https://www.revenuquebec.ca/en/citizens/income-tax-return/completing-your-income-tax-return/line-by-line-help/400-to-447-income-tax-and-contributions/line-445/) [F31](https://www.revenuquebec.ca/en/citizens/income-tax-return/completing-your-income-tax-return/line-by-line-help/400-to-447-income-tax-and-contributions/line-439/) |
| GST/HST/QST returns | Entity/account, actual period, normal/Quick Method/elections, filed or draft status, source line amounts, adjustments, instalments, rebates/debits, final balance/refund and acknowledgements/payments. | For the regular method, 105 includes 103 and 104; 108 includes 106 and 107; 109 is net tax, not necessarily final cash due. Keep 110 and other balance adjustments separately. Do not describe every registered business as an annual paper GST34 filer. [F10](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/calculate-prepare-report/instructions-preparing-return.html) [F11](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/file-gst-hst-return/reporting-requirements-deadlines.html) |
| RRSP/PRPP/SPP | Actual receipt/plan/annuitant/contributor, contribution date, amounts, own/spousal/group plan, latest statement year, prior unused contributions, transfers, HBP/LLP designations and refunds. | Bank outflow alone is not a contribution receipt. Contribution, deduction, unused contribution and new available room are different. Preserve actual periods and prevent double reporting of first-60-day or previously reported amounts. [F22](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/rrsps-related-plans/contributing-a-rrsp-prpp/what-unused-rrsp-prpp-contributions.html) [F23](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/rrsps-related-plans/contributing-a-rrsp-prpp/where-you-find-your-rrsp-prpp-deduction-limit.html) [F24](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/rrsps-related-plans/contributing-a-rrsp-prpp/contributions-affect-your-rrsp-prpp-deduction-limit.html) [F40](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5000-s7/5000-s7-25e.pdf) |

The actual 2025 T4 bridge includes boxes **14, 16/17, 16A/17A, 18, 20, 22, 24, 26, 44, 52 and 55/56**, where present. Preserve original slip IDs and field names; do not combine second CPP/QPP with first-tier amounts or omit QPIP. Final-year form labels must be rechecked. [F27]

Ordinary self-employment generally uses accrual accounting; farm/fish/commission branches need their actual applicable method. Capture income earned but unpaid, expenses incurred but unpaid, inventory, prepayments, refunds and adjustments. A bank-only profit or “no T4, T2125 only” conclusion is insufficient. [F12] [F13] [F33]

### 4. Resolve the tax switches before a confident handoff

#### Rates, bands and thresholds

These rows identify intake decisions, not a substitute national tax calculator. Money is CAD. Use the current linked component for its full computation; a figure repeated in a worked case is conditional on that case's facts.

| Switch | Rule or value with conditions | Applicable period | Official source |
|---|---|---|---|
| Ordinary GST/HST small-supplier threshold | Relevant worldwide taxable supplies of the person and associates, including zero-rated supplies, with statutory exclusions; **30,000** ordinary threshold. Both a single-quarter breach and the rolling-quarter route matter. Registered and special-activity cases require separate facts. | Current registration decision; actual supply/effective dates | [F01](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-148.html) [F02](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/when-register-charge.html) [F05](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-240.html) [F06](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-166.html) |
| Registration timing | Generally apply within **29 days** of the effective date; a single-quarter breach includes its triggering supply, while the rolling route has a following-month interval and first subsequent supply. Taxi/commercial ride-share has its own start-date rule. | Actual account/supply dates | [F02](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/when-register-charge.html) [F05](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-240.html) |
| T5013 administrative filing-policy financial tests | Absolute revenue plus absolute expenses **over 2 million**, or asset cost **over 5 million**, with the separate tiered/partner/resource/written-request branches. These do not make every partnership a filer. | Actual partnership fiscal period | [F15](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4068/guide-partnership-information-return-t5013-forms.html) |
| Home workspace | Principal place of business **or** exclusive business use plus regular/continuous client/customer/patient meetings; reasonable cost/use allocation and business-income cap/carryforward. No employee-style flat/simplified option is created by sharing the room. | Actual business/fiscal period | [F03](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-18.html) [F18](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/report-business-income-expenses/completing-form-t2125/business-use-home-expenses.html) |
| Simplified vehicle record method | Full **12-month** base, representative matching **3-month** sample and actual formula; CRA's **49%** base example permits **39%-59%**, not a relative 10% band. | Actual base/sample and later year | [F19](https://www.canada.ca/en/revenue-agency/services/tax/businesses/small-businesses-self-employed-income/business-income-tax-reporting/business-expenses/motor-vehicle-expenses.html) |
| Designated individual immediate-expensing window | Conditional **1.5 million** limit, including association and other restrictions; individual property must become available for use **before 2025**. This is not AIIP and does not automatically apply to new 2025/2026 purchases. | Historical eligible acquisition/availability | [F04](https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/section-1104.html) |
| Class 50 distinction | Ordinary class rate **55%**; qualifying special AIIP/RIIP first-year rules can produce **100%**, with actual acquisition/availability, ownership, use and pool conditions. “Not the old immediate-expensing window” does not mean no accelerated allowance. | Applicable 2025/2026 allowance, not an automatic election | [F04](https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/section-1104.html) [F20](https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/section-1100.html) [F21](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/report-business-income-expenses/claiming-capital-cost-allowance/classes.html) |
| Actual 2025 RRSP receipts | Schedule 7 ordinary Part A separates **March 4-December 31, 2025** from **January 1-March 2, 2026**. Prior unused contributions and HBP/LLP designations are separate. | Dated 2025 filing bridge only | [F23](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/rrsps-related-plans/contributing-a-rrsp-prpp/where-you-find-your-rrsp-prpp-deduction-limit.html) [F24](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/rrsps-related-plans/contributing-a-rrsp-prpp/contributions-affect-your-rrsp-prpp-deduction-limit.html) [F40](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5000-s7/5000-s7-25e.pdf) |

**Registration and supplies.** Identify exempt versus taxable/zero-rated supplies and the statutory exclusions for financial services, sales of capital property and specified goodwill when assembling the threshold records. Obtain actual account status/effective/cancellation dates and the relevant taxable supply history, including associates and exceptional activities. A normal voluntarily registered small supplier still has collection/filing obligations while registered; ETA 148(3)(a)'s specific simplified-regime reference does not exclude every ordinary voluntary registrant from small-supplier status. Confirm the relevant registration record, dates and normal versus simplified supplier status. Do not claim the registry was searched unless it was. [F01] [F02] [F05] [F06] [F07]

Personal year-end province, business establishments and the place of each supply are different facts. Ontario residence does not prove that all invoices bear Ontario HST; actual service/goods/export and customer/place facts control. Use `canada-gst-hst` for the decision and `qc-qst-return` for any applicable Quebec sales-tax work, inspecting each current method and its actual approval rather than assuming its readiness. [F08] [F34]

**Fiscal period.** Retain the actual start/end and previous filings/elections for each business. Calendar-year rules have an eligible alternative-method branch under ITA 249.1; use actual T1139 and the current T2125/assembly methods for the required additional-income reconciliation, prior-year amount and election/revocation history. Do not force every sole proprietor to December 31, change their year-end silently, or assume a free change without required concurrence. [F16] [F17]

**Home.** Ask whether the workspace is the principal place of business; if not, establish both exclusive business use and regular/continuous meetings with clients/customers/patients. Collect area, actual time/days, eligible household costs, rented/owned status, related reimbursements and carryforwards. Shared space needs reasonable time allocation and qualifying facts, not an automatic “simplified method.” Mortgage principal is not deductible; renters collect their rent and eligible costs, not their landlord's mortgage interest. Record the income cap and any carryforward; home CCA has possible later capital-gain/recapture consequences. The actual deduction belongs in `ca-fed-t2125`. [F03] [F18]

**Vehicle.** Preserve all four branches: full log; partial log; no log but other available records; no business vehicle use. For each vehicle obtain total/business distance, trip evidence, expenses, ownership/lease/finance, dates, business parking and supplementary insurance separately. For a sample method obtain the full base and matching period; do not treat every partial log or a guessed percentage as accepted. Reconstruct from reliable contemporaneous evidence where possible and flag unresolved support. Do not invent a percentage or universally disallow useful records. [F19]

**Assets.** For a computer or other equipment obtain the invoice, actual owner, class/type, acquisition and available-for-use dates, prior use/relationship, business use, recoverable taxes, assistance, opening UCC and disposals. Offer supported calculations from `ca-fed-t2125`, not “immediate expense or standard CCA” as an unconditional preference. AIIP, RIIP, designated immediate expensing and special class allowances differ. A low price does not establish eligibility or the best claim. Record the actual supported choice and any effects needing professional judgement. [F04] [F20] [F21]

**RRSP.** Obtain the latest statement and receipts, prior reported unused contributions and amounts already deducted/designated/refunded, plus spouse/group plans, transfers, pension adjustments and HBP/LLP facts if applicable. Do not label deduction limit minus one bank outflow as proven new room or proof of no excess. For the actual 2025 bridge, the inspected Schedule 7 controls the ordinary periods above; Part B may include January 1, 2025-March 2, 2026 repayments with exclusions, so collect all relevant 2025 receipts and preserve prior-year allocation. One CRA unused-contributions page still says March 1 for the ordinary period; it does not override the actual form's March 4. Use the final-year form and T1 method to allocate/deduct once. [F22] [F23] [F24] [F25] [F40]

**Contributions and other personal facts.** Preserve all slips, CPP/QPP coverage, first/second tiers, age/pension/disability/election dates and self-employed EI agreement/withdrawal/benefit history. An EI benefit waiting condition is not an exemption from premiums. Quebec QPP/QPIP and mixed-province routes remain explicit work items, not a blanket refusal or a federal CPP default. Collect spouse/dependant facts, support/living arrangements, relevant income and existing claims before any credit is calculated; do not infer entitlement from marital status alone. [F27] [F28] [F29] [F30] [F31] [F32] [F38]

### 5. Show one consolidated factual summary, then fill material gaps

Present a compact summary grouped as identity/year/scope, business and fiscal periods, all income, accounts/GST periods, expenses/assets, contributions/RRSP, payments and unresolved flags. Name the document or answer next to each material figure. Distinguish recorded amounts from estimates, disputed items and final calculation outputs. Ask the user to correct the picture; “looks good” confirms their response, not every tax condition or third-party record.

Carry forward the original example's useful flags: phone/internet use, vehicle records, computer class/availability/allowance, meals purpose/limits, RRSP records, fiscal-year/election status, GST/ITC evidence, other income and provincial/Quebec work. Do not say “eligible” or “no excess” before the evidence supports it. A missing material fact blocks the affected result; it does not erase unrelated supported work.

For gaps, use these grouped prompts as needed:

- Home: principal business location or exclusive meeting-space facts; area/time, rented/owned costs and carryforward.
- Private use: phone/internet and each vehicle; what contemporaneous records support the split?
- Vehicle: full or sample/base logs, other reconstruction records, dates and distance/cost totals.
- Capital: actual acquisition/use/class/prior UCC and tax recovery; then a supported choice from the calculation method.
- Province: actual year-end residence/moves, employment province and business establishments; supply location separately.
- Other income: employment, investments, rental, gains, foreign and special activity, including records not yet received.
- Personal: spouse/dependants, support and relevant income/claims.
- RRSP/contributions/payments: actual statements, receipt periods, agreements, coverage/elections and authority/account/year allocations.

Batch independent questions. An uncertain answer stays uncertain. Do not ask questions already answered by reliable records, but ask for missing proof when a bank label or invoice could mean several things. Avoid narrating numbered phases to the end user; provide actual findings and next actions.

### 6. Produce the full handoff, with an honest completion state

Build the structured package below, a short evidence/open-item summary and a required-work register. Preserve each business, person, year, currency and account-period identity. The downstream assembler must receive all applicable work, not a false “intake complete” sentence that hides unknown income or unsupported balances.

For every dependency actually loaded, record slug, returned version/year, source/read date, actual approval label/name, why applicable, input status and outputs if any. A method not applicable needs a factual reason; a missing suitable method stays open. Do not carry a named accountant from one method onto another.

| Workstream | Current method or handoff | Required control |
|---|---|---|
| Books and each business/profession | `ca-fed-t2125` with reconciled per-business records | Actual accounting/fiscal period, earned income, expenses, CCA/home/vehicle and unresolved evidence. [F13](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/accounting-methods.html) [F14](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/business-records.html) [F16](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-249.1.html) [F17](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t1139/t1139-25e.pdf) |
| Each GST/HST reporting period | `canada-gst-hst` | Registration, supplies, normal/Quick Method, ITC/adjustments, actual final balance and payments; separate QST if applicable. [F05](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-240.html) [F08](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/charge-collect-place-supply.html) [F09](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-169.html) [F10](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/calculate-prepare-report/instructions-preparing-return.html) [F11](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/file-gst-hst-return/reporting-requirements-deadlines.html) |
| CPP/QPP and eligible EI/QPIP | `ca-fed-cpp-ei` plus actual Quebec calculation where needed | Full employment/self-employment, coverage and election/participation evidence; no guessed residual maximum or total half split. [F27](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/tax-slips/understand-your-tax-slips/t4-slips/t4-statement-remuneration-paid.html) [F28](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-22200-deduction-cpp-qpp-contributions-on-self-employment-other-earnings.html) [F29](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/cpp/canada-pension-plan-cpp-contributions-cpp-working-beneficiaries.html) [F30](https://www.revenuquebec.ca/en/citizens/income-tax-return/completing-your-income-tax-return/line-by-line-help/400-to-447-income-tax-and-contributions/line-445/) [F31](https://www.revenuquebec.ca/en/citizens/income-tax-return/completing-your-income-tax-return/line-by-line-help/400-to-447-income-tax-and-contributions/line-439/) [F32](https://www.canada.ca/en/services/benefits/ei/ei-self-employed-workers/eligibility.html) |
| Federal personal return and all income | `ca-fed-t1-return` | Complete income, deductions, RRSP/unused contributions, credits, withholding and actual instalment credits; special-income schedules remain visible. [F12](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-3.html) [F23](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/rrsps-related-plans/contributing-a-rrsp-prpp/where-you-find-your-rrsp-prpp-deduction-limit.html) [F24](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/rrsps-related-plans/contributing-a-rrsp-prpp/contributions-affect-your-rrsp-prpp-deduction-limit.html) [F33](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/personal-income/self-employment-income-lines-13499-14299-gross-income-lines-13500-14300-net-income.html) [F35](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/claim-amounts-tax-return.html) [F40](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5000-s7/5000-s7-25e.pdf) |
| Province/territory and Quebec | Applicable current provincial skill; Quebec TP-1/contributions and QST as required | Year-end residence plus actual business-establishment/multi-jurisdiction facts. Unresolved required provincial work keeps the package incomplete. [F30](https://www.revenuquebec.ca/en/citizens/income-tax-return/completing-your-income-tax-return/line-by-line-help/400-to-447-income-tax-and-contributions/line-445/) [F31](https://www.revenuquebec.ca/en/citizens/income-tax-return/completing-your-income-tax-return/line-by-line-help/400-to-447-income-tax-and-contributions/line-439/) [F34](https://www.canada.ca/en/revenue-agency/services/forms-publications/forms/t2203.html) |
| Income-tax instalments | `ca-fed-instalments` for the actual requested year | Prior/current assessments and reminders, complete history, payment/credit allocation; do not confuse with GST or the prior T1 balance. [F35](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/claim-amounts-tax-return.html) [F36](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/how-pay.html) |
| Assembly | `ca-return-assembly` | Explicitly hand over JSON, document/evidence index, open items and required-work register; preserve current approval for each consumed method. |

A suitable handoff states what was collected, which facts remain unresolved and which method is next. For a full package, the assembler prepares and checks the workbook/working papers, reviewer brief with sources/positions/open items, and filing/payment calendar. Where actual spreadsheet tools are available, produce and inspect the file there; otherwise identify the missing artifact and give the usable supported schedules without claiming that an Excel file exists. An intake, a workbook and an actual filing acknowledgement are different things. [F14] [F50]

Use `INTAKE READY` only when all facts material to the agreed next computation are supported or explicitly accepted as labelled estimates for planning, with no hidden conflicts. Otherwise use `INTAKE INCOMPLETE` with the affected task, missing evidence, owner and next action. A partial handoff is useful but must keep the overall return/package incomplete where required work remains. Even an intake ready for an estimate is not a filed return, paid tax or accountant-approved return.

### 7. Structured intake package

Keep the original field paths for downstream interpretation, using null for unknown scalar values and evidence/status records instead of forced defaults. The old `contributions_2025` and `contributions_first_60_days_2026` are historical bridge fields only; the year-tagged receipt ledger is authoritative for any actual year. The legacy single-business summaries are populated only from reconciled compatible records; multiple businesses and GST periods stay separate.

An empty array below is a template awaiting inventory, not evidence that the population is empty. Record a supported zero, false or absence only with the relevant evidence and completeness status. An unresolved date does not default to December 31, and an unresolved tax rate does not default to zero.
```json
{
  "jurisdiction": "CA",
  "tax_year": null,
  "taxpayer": {
    "name": null,
    "date_of_birth": null,
    "marital_status": null,
    "residency": null,
    "sin": null,
    "province": null,
    "gst_hst_registered": null,
    "gst_hst_number": null,
    "employment_status": null,
    "industry": null,
    "entity_type": null,
    "fiscal_year_end": null,
    "residence_evidence_ids": [],
    "residency_changes": [],
    "business_establishments": [],
    "spouse_income": null,
    "dependants": []
  },
  "business_income": {
    "gross_revenue_ex_gst": null,
    "gst_hst_collected": null,
    "client_breakdown": []
  },
  "employment_income": {
    "t4_slips": [],
    "total_employment_income": null,
    "total_cpp_deducted": null,
    "total_ei_deducted": null,
    "total_tax_deducted": null,
    "total_cpp2_deducted": null,
    "total_qpp_deducted": null,
    "total_qpp2_deducted": null,
    "total_qpip_deducted": null,
    "slip_inventory_complete": null
  },
  "other_income": {
    "interest": null,
    "dividends_eligible": null,
    "dividends_other": null,
    "rental": null,
    "capital_gains": null
  },
  "expenses": {
    "fully_deductible": [],
    "mixed_use": [],
    "blocked": [],
    "meals_entertainment_gross": null,
    "cca_items": [],
    "immediate_expensing_items": []
  },
  "gst_hst": {
    "returns_filed": [],
    "total_collected": null,
    "total_itc": null,
    "net_tax": null,
    "rate": null
  },
  "rrsp": {
    "contributions_2025": null,
    "contributions_first_60_days_2026": null,
    "deduction_limit": null,
    "room_remaining": null,
    "receipt_ledger": [],
    "statement_year": null,
    "statement_document_ids": [],
    "previously_reported_unused_contributions": null,
    "transfers": [],
    "hbp_llp_designations": [],
    "chosen_deduction": null
  },
  "instalments": {
    "quarterly_amounts": [],
    "total_paid": null,
    "prior_year_instalment_base": null,
    "payment_ledger": [],
    "reminders": [],
    "history_by_year": [],
    "unallocated_payments": []
  },
  "home_office": {
    "qualifies": null,
    "method": null,
    "workspace_sqft": null,
    "total_home_sqft": null,
    "home_expenses": {},
    "percentage": null,
    "qualification_basis": null,
    "business_hours": null,
    "total_period_hours": null,
    "carryforward": null,
    "document_ids": []
  },
  "motor_vehicle": {
    "has_log": null,
    "total_km": null,
    "business_km": null,
    "business_pct": null,
    "total_expenses": null,
    "vehicles": []
  },
  "prior_year": {
    "net_income": null,
    "taxable_income": null,
    "tax_payable": null,
    "net_business_income": null,
    "instalment_base": null,
    "rrsp_deduction_limit": null,
    "loss_carryforwards": null,
    "cca_schedule": []
  },
  "open_flags": [],
  "refusals_triggered": [],
  "documents_received": [],
  "schema_version": "0.2",
  "task": {
    "requested_work": [],
    "preparation_mode": null,
    "instalment_year": null,
    "status": "INTAKE INCOMPLETE"
  },
  "businesses": [],
  "tax_accounts": [],
  "income_inventory": [],
  "field_evidence": {},
  "method_provenance": [],
  "required_workstreams": [],
  "authorization": {
    "filing_status": "not established",
    "payment_status": "not established",
    "document_ids": []
  },
  "contribution_history": {
    "coverage_periods": [],
    "pension_records": [],
    "disability_periods": [],
    "elections": [],
    "ei_participation": {
      "agreement_date": null,
      "active_status": null,
      "withdrawal_date": null,
      "benefit_history": [],
      "document_ids": []
    },
    "qpip_records": []
  }
}
```

### 8. Field and record contracts

The JSON is a working-paper interchange format, not an additional filing form. Extend its arrays with actual records, not fictional sample rows.

| Field/group | Required record and interpretation |
|---|---|
| `taxpayer` and `tax_year` | Actual identity/year, DOB, residence/status evidence and changes, business structure and period. Marital status must support the actual annual return, including single, married, common-law, separated, divorced or widowed and relevant dates/spouse information; do not collapse it to the old three choices. Keep full identifiers in authorized records, not routine display. [F45](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-r/5006-r-25e.pdf) |
| `businesses[]` | Business ID/name/activity, ownership, actual start/end and fiscal/election history, books/currency, earned revenue and timing adjustments, expenses/assets, GST recovery and document IDs. Maintain separate activity results before any compatible legacy summary. [F13](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/accounting-methods.html) [F14](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/business-records.html) [F16](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-249.1.html) [F17](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t1139/t1139-25e.pdf) [F47](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/report-business-income-expenses/completing-form-t2125.html) |
| Legacy `business_income` / `expenses` / `prior_year` | Preserve all original paths. They are sourced summaries for a specified business/year or reconciled compatible totals. `fully_deductible` cannot mean “merchant category looked plausible”; retain eligibility evidence and the calculating method. Keep prior net/taxable income, tax payable, business income, instalment base, RRSP/loss/CCA history distinct. [F12](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-3.html) [F14](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/business-records.html) [F23](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/rrsps-related-plans/contributing-a-rrsp-prpp/where-you-find-your-rrsp-prpp-deduction-limit.html) [F35](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/claim-amounts-tax-return.html) [F41](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-18.html) [F45](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-r/5006-r-25e.pdf) |
| `tax_accounts[]` / `gst_hst` | Owner/entity, authority, program/account, normal/simplified status, effective/cancellation dates, reporting period, method/election, returns and acknowledgements, original form lines and adjustments, actual payments/rebates/balance and evidence. An account has a BN/program/reference identity; do not invent an RT0001 suffix or confuse RT, RP and RC. A single `rate` is null where it is not a supported single-rate summary. [F05](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-240.html) [F07](https://www.canada.ca/en/revenue-agency/services/e-services/digital-services-businesses/confirming-a-gst-hst-account-number.html) [F10](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/calculate-prepare-report/instructions-preparing-return.html) [F11](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/file-gst-hst-return/reporting-requirements-deadlines.html) [F48](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/business-registration/business-number-program-account/need-program-accounts.html) |
| `income_inventory[]` / `employment_income` / `other_income` | One row per income source: owner, category, year/period, currency, amount/status, slips/records, method and missing work. All original interest, dividend, rental and capital-gain fields remain; add other applicable sources rather than forcing them into business income or zero. Store original T4/RL fields and first/second contribution components separately. [F12](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-3.html) [F27](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/tax-slips/understand-your-tax-slips/t4-slips/t4-statement-remuneration-paid.html) [F28](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-22200-deduction-cpp-qpp-contributions-on-self-employment-other-earnings.html) [F33](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/personal-income/self-employment-income-lines-13499-14299-gross-income-lines-13500-14300-net-income.html) |
| `rrsp.receipt_ledger[]` | Receipt ID, plan/contributor/annuitant, actual contribution date, year/period, amount/currency, prior reported/deducted/designated/refunded amount, transfer/HBP/LLP treatment and document IDs. Store the latest statement's year, limit, previously unused contributions, current choice and evidence separately. Historical 2025/early-2026 fields are never relabelled to a later year. [F22](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/rrsps-related-plans/contributing-a-rrsp-prpp/what-unused-rrsp-prpp-contributions.html) [F23](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/rrsps-related-plans/contributing-a-rrsp-prpp/where-you-find-your-rrsp-prpp-deduction-limit.html) [F24](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/rrsps-related-plans/contributing-a-rrsp-prpp/contributions-affect-your-rrsp-prpp-deduction-limit.html) [F40](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5000-s7/5000-s7-25e.pdf) |
| Contribution coverage, EI and Quebec | Capture coverage jurisdiction and dates, CPP/QPP first/second tiers, age/pension/disability/election records, employment pensionable/insurable earnings and EI/QPIP amounts. Record self-employed EI agreement, cancellation/withdrawal, benefit history and evidence. The full-year premium and withdrawal rules belong to the actual current child method. [F27](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/tax-slips/understand-your-tax-slips/t4-slips/t4-statement-remuneration-paid.html) [F28](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-22200-deduction-cpp-qpp-contributions-on-self-employment-other-earnings.html) [F29](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/cpp/canada-pension-plan-cpp-contributions-cpp-working-beneficiaries.html) [F30](https://www.revenuquebec.ca/en/citizens/income-tax-return/completing-your-income-tax-return/line-by-line-help/400-to-447-income-tax-and-contributions/line-445/) [F31](https://www.revenuquebec.ca/en/citizens/income-tax-return/completing-your-income-tax-return/line-by-line-help/400-to-447-income-tax-and-contributions/line-439/) [F32](https://www.canada.ca/en/services/benefits/ei/ei-self-employed-workers/eligibility.html) [F51](https://www.canada.ca/en/services/benefits/ei/ei-self-employed-workers/premiums.html) [F52](https://www.canada.ca/en/services/benefits/ei/ei-self-employed-workers/withdraw.html) |
| `instalments.payment_ledger[]` | Owner, authority/account, tax year/period, actual amount/currency, bank/receipt/posted dates, reference, allocation/transfer/refund status and proof. Separate INNS1 reminder amounts, INNS2 summaries and actual payments. Keep current/two-prior-year assessments/history for the instalment method. `total_paid` never includes merely scheduled or unallocated money. [F35](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/claim-amounts-tax-return.html) [F36](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/how-pay.html) |
| `home_office` / `motor_vehicle.vehicles[]` | Qualification basis, actual space/time and costs/carryforward; or each vehicle, actual travel/cost records and base/sample conditions. Use fractions from 0 to 1 for numeric use ratios, displaying percentages separately. Keep original legacy fields and source IDs; an unsupported fraction remains null. [F03](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-18.html) [F18](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/report-business-income-expenses/completing-form-t2125/business-use-home-expenses.html) [F19](https://www.canada.ca/en/revenue-agency/services/tax/businesses/small-businesses-self-employed-income/business-income-tax-reporting/business-expenses/motor-vehicle-expenses.html) |
| `field_evidence` | Map a path to status, source/document/answer IDs, relevant dates, conflicting values, resolution and reviewer/owner if needed. `user_confirmed` is not the same as verified registration or tax eligibility. Empty or missing records do not certify absence. |
| `method_provenance[]` | Actual slug/version/year, applicable scope, source/read date, returned approval label and approving name if any, facts supplied, outputs used and unresolved items. No directory-level approval inheritance. |
| `required_workstreams[]` / `open_flags[]` | Task/return/period, why required, method/owner, evidence state, consequence and next action. A flag has the fact, source, affected result, materiality and resolution; do not hide an uncomputed required return in a “reviewer to check” footnote. |
| `documents_received[]` and `authorization` | Actual document inventory/read coverage and amendment history; separate evidence of filing/payment authorization from actual filing/payment receipts. Preparing intake gives neither. [F14](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/business-records.html) [F50](https://www.canada.ca/en/revenue-agency/services/forms-publications/forms/t183.html) |

Keep the required contribution coverage, pension/disability, election, EI participation/withdrawal and QPIP records in `contribution_history`, linked to field-evidence records; never discard them because an old aggregate field is too small. Likewise, retain the actual personal-return deductions/benefit facts required by the client's full case. CCB is a separate benefit, and dependant/spouse facts may matter beyond an eligible-dependant credit; no benefit entitlement or amount is inferred here. [F38] [F39]

Before passing to an older consumer, state the schema version and nullable-field contract. If it cannot preserve unknowns, statuses or separate businesses/periods, keep the actual values in the evidence register and do not silently coerce them to zero, false, one tax rate or a fictional fiscal date. The actual assembler must understand the handoff before the package can be described as complete.

## Boundary and exception table

| Finding | Continue with | Hold or route |
|---|---|---|
| Focused query; full record already held | Relevant component and missing facts only. | Do not rerun an entire return intake for one payment question. |
| Partial documents or unreadable pages | Document index, supported extraction, explicit missing-page requests and independent work. | Affected values remain missing/conflicting; do not call the total return complete. [F14](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/business-records.html) |
| Residence uncertain, part-year or non-resident | Collect relevant dates/ties and supported records; appropriate residency/special return method. | This full-year sole-proprietor path cannot settle the whole return by assuming residence or treating physical travel as decisive. [F37](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-2.html) [F49](https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/information-been-moved/determining-your-residency-status.html) |
| Corporation discovered | Preserve personal employment/dividend/shareholder records and identify the separate entity's work. | Route actual corporate return obligations; do not put corporate revenue into personal T2125 or demand a universal CPA-only filing route. [F44](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/corporations/corporation-income-tax-return/who-file-a-corporation-income-tax-return.html) |
| Partnership discovered | Ownership/agreement/allocations, actual T5013 or financial statements and separable personal income. | Check regulation and actual CRA filing policy; separate partnership return and individual partner work. [F15](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4068/guide-partnership-information-return-t5013-forms.html) [F43](https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/section-229.html) |
| Quebec or more than one business jurisdiction | Federal personal work plus actual TP-1/QPP/QPIP and sales-tax inputs; business-establishment facts. | Do not substitute federal CPP or one provincial-residence calculation for required Quebec/multi-jurisdiction work. [F28](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-22200-deduction-cpp-qpp-contributions-on-self-employment-other-earnings.html) [F30](https://www.revenuquebec.ca/en/citizens/income-tax-return/completing-your-income-tax-return/line-by-line-help/400-to-447-income-tax-and-contributions/line-445/) [F31](https://www.revenuquebec.ca/en/citizens/income-tax-return/completing-your-income-tax-return/line-by-line-help/400-to-447-income-tax-and-contributions/line-439/) [F34](https://www.canada.ca/en/revenue-agency/services/forms-publications/forms/t2203.html) |
| Registered but low revenue or nil period | Actual account/method/period and filing obligations, including valid nil returns. | Do not cancel registration or skip a return based on annual bank revenue alone. [F05](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-240.html) [F06](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-166.html) [F11](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/file-gst-hst-return/reporting-requirements-deadlines.html) |
| Unregistered, uncertain or threshold crossed | Supply/associate/date analysis, account verification and effective-date correction work. | No “no tax/no return” conclusion from a bare annual revenue figure or invoice pattern. [F01](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-148.html) [F02](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/when-register-charge.html) [F07](https://www.canada.ca/en/revenue-agency/services/e-services/digital-services-businesses/confirming-a-gst-hst-account-number.html) |
| Cash-only books, multiple accounts/currencies | Reconcile source records, accrual/currency and period adjustments with evidence. | No final profit from deposits or blended periods without the required bridge. [F13](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/accounting-methods.html) [F14](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/business-records.html) |
| Foreign, rental, capital, farm/fish, employment or other income | Preserve the income and route the applicable method. | Missing special work prevents whole-return completion; do not suppress it or force it into an ordinary freelance schedule. [F12](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-3.html) [F33](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/personal-income/self-employment-income-lines-13499-14299-gross-income-lines-13500-14300-net-income.html) |
| Capital or mixed-use support incomplete | Assets/UCC/use records, options calculated by the current component and exact missing facts. | No guessed deduction, universal 1.5m election, personal percentage or “best” claim. [F03](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-18.html) [F04](https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/section-1104.html) [F19](https://www.canada.ca/en/revenue-agency/services/tax/businesses/small-businesses-self-employed-income/business-income-tax-reporting/business-expenses/motor-vehicle-expenses.html) [F20](https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/section-1100.html) [F41](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-18.html) |
| RRSP statements/receipt periods conflict | Read the actual annual Schedule 7, latest statement and prior reported/deducted records. | No double claim, guessed unused room or “no excess” certification. Actual 2025 form resolves the stale ordinary-period webpage date. [F22](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/rrsps-related-plans/contributing-a-rrsp-prpp/what-unused-rrsp-prpp-contributions.html) [F23](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/rrsps-related-plans/contributing-a-rrsp-prpp/where-you-find-your-rrsp-prpp-deduction-limit.html) [F24](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/rrsps-related-plans/contributing-a-rrsp-prpp/contributions-affect-your-rrsp-prpp-deduction-limit.html) [F40](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5000-s7/5000-s7-25e.pdf) |
| Bank tax or RRSP outflow is ambiguous | Keep the amount/source as provisional and request exact receipt/account/year/allocation. | Do not count it as a deduction, contribution or income-tax instalment merely from its description. [F14](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/business-records.html) [F35](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/claim-amounts-tax-return.html) [F36](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/how-pay.html) |
| Runtime lacks an expected question/spreadsheet tool | Available grouped questions, supported schedules and an honest artifact status. | No invented tool call, workbook, professional sign-off, filing or payment. [F50](https://www.canada.ca/en/revenue-agency/services/forms-publications/forms/t183.html) |

## Worked cases

All cases are synthetic audit examples, not client records. The 2025 figures below preserve and correct the original dated example. They do not replace current component calculations or imply that final 2026 forms have been published. Executable blocks check arithmetic; legal eligibility, source completeness and method selection need the stated evidence.

### Case 1. Preserve the original Marc intake without inventing profit or ITCs

A fictional 2025 Toronto sole proprietor, Marc Tremblay, is single and has a confirmed calendar fiscal period and no employment income after a complete income inventory. The original records show client amounts 72,000, 30,000 and 18,000; expense candidates 1,800 office supplies, 3,600 software, 1,400 insurance, 2,000 accounting, 2,400 phone/internet, 5,200 vehicle costs, a 2,800 Dell laptop acquired in June 2025, and 1,600 meals. The example also records 12,000 RRSP receipts, an 18,500 deduction-limit statement, four 2,500 instalment entries, 2024 business net income 95,000, net income 23600 of 83,000, tax payable 14,200 and an asserted instalment base of 10,000. Retain each amount, owner, date and source; the last four prior-year amounts are distinct inputs, not an arithmetic proof of the current instalment base. [F14] [F23] [F35] [F45]

The client amounts sum to **120,000**. Only if actual registered status, taxable Ontario supplies, period, pricing and the regular method are established would a uniform 13% illustration give **15,600** collected and **135,600** gross. A printed 13% invoice or Toronto address alone does not establish all those conditions. The original **1,450** ITC total remains provisional until invoice, registration, use and period evidence establishes it. [F05] [F07] [F08] [F09] [F10]

The fixed expense candidates sum to **8,800**. For a deliberately simplified arithmetic comparison only, suppose those costs are fully eligible on consistent net-of-recoverable-tax bases, phone/vehicle are entirely business costs, the ordinary supported meals limit gives 800, and the current method confirms a 2,800 maximum computer allowance with that entire amount claimed. That would total **20,000** and produce **100,000** before other adjustments, not the original unsupported **98,000**. This comparison is not the actual profit: the real business-use, tax recovery, capital eligibility/claim, accrual and other adjustments remain to be established. [F13] [F20] [F41] [F42] [F46]

Show the actual factual summary and flags, not “RRSP within limit, no excess,” “eligible for AIIP immediate expensing,” “all ITCs claimable” or “year-end must be December 31.” Ask only for the missing phone split, vehicle evidence, asset/CCA facts, meals purpose/exception, RRSP unused/contribution history, fiscal election, GST support and other-income gaps. [F04] [F16] [F19] [F23] [F24] [F42]

```oa-check
name: Dated 2025 original intake arithmetic, eligibility still separate
inputs:
  client_a: 72000
  client_b: 30000
  client_c: 18000
  stipulated_hst_rate: 0.13
  supplies: 1800
  software: 3600
  insurance: 1400
  accounting: 2000
  phone_if_fully_allowed: 2400
  vehicle_if_fully_allowed: 5200
  computer_if_confirmed_claim: 2800
  supported_ordinary_meals: 1600
  original_unsupported_net: 98000
steps:
  - revenue: client_a + client_b + client_c
  - conditional_hst: revenue * stipulated_hst_rate
  - conditional_gross: revenue + conditional_hst
  - fixed_costs: supplies + software + insurance + accounting
  - conditional_meals: supported_ordinary_meals * 0.5
  - hypothetical_expenses: fixed_costs + phone_if_fully_allowed + vehicle_if_fully_allowed + computer_if_confirmed_claim + conditional_meals
  - hypothetical_net: revenue - hypothetical_expenses
  - old_net_gap: hypothetical_net - original_unsupported_net
expected:
  revenue: 120000
  conditional_hst: 15600
  conditional_gross: 135600
  fixed_costs: 8800
  conditional_meals: 800
  hypothetical_expenses: 20000
  hypothetical_net: 100000
  old_net_gap: 2000
```

### Case 2. Registration is a dated decision, not one annual revenue question

Assume a normal Canadian consulting business, no prior/voluntary registration, no special exception or associates, and relevant taxable supplies measured on the statutory basis. In a single quarter, 29,500 is followed by a taxable supply with **750 of tax-exclusive consideration** on September 10, 2026. The total is 30,250. The triggering supply, not merely the 250 excess, starts the charging branch. If its actual place/rate is Ontario 13%, the illustrative tax on that supply is **97.50**, not 32.50. Confirm the actual effective date/account and registration action; this example does not register anyone. [F01] [F02] [F05] [F08]

Compare a rolling case with 9,500, 9,500, 9,500 and 2,000 across the four quarters ending September 30, 2026, with no single-quarter breach. The total is 30,500. On the stated ordinary facts the small-supplier period runs through October 31; if the first later taxable supply is November 5, that date starts the ordinary registration/charging route. It does not retrospectively tax every receipt in the earlier quarters or waive a different exception. Use the linked rule for the actual application deadline and preserve the dates. [F01] [F02]

If the owner is already voluntarily registered, or operates a taxi/commercial ride-share business, neither low total above resolves their actual obligations. If invoices show tax but account evidence is missing, status is **unresolved**, not automatically registered. [F02] [F05] [F06] [F07]

```oa-check
name: Single-quarter versus rolling registration arithmetic
inputs:
  ordinary_threshold: 30000
  earlier_quarter_supplies: 29500
  triggering_supply: 750
  stipulated_ontario_rate: 0.13
  rolling_q1: 9500
  rolling_q2: 9500
  rolling_q3: 9500
  rolling_q4: 2000
steps:
  - single_quarter_total: earlier_quarter_supplies + triggering_supply
  - excess: single_quarter_total - ordinary_threshold
  - conditional_triggering_tax: triggering_supply * stipulated_ontario_rate
  - wrong_excess_only_tax: excess * stipulated_ontario_rate
  - rolling_total: rolling_q1 + rolling_q2 + rolling_q3 + rolling_q4
  - rolling_excess: rolling_total - ordinary_threshold
expected:
  single_quarter_total: 30250
  excess: 250
  conditional_triggering_tax: 97.50
  wrong_excess_only_tax: 32.50
  rolling_total: 30500
  rolling_excess: 500
```

### Case 3. RRSP limit and previously unused contributions

For a bounded 2025 illustration, the latest statement confirms an 18,500 ordinary deduction limit. Receipts support 12,000 new ordinary contributions in the appropriate period. If there are no prior unused contributions or other relevant adjustments, the simple residual is 6,500. If **4,000** previously reported but undeducted contributions also occupy that room, the same simple residual is **2,500**, not 6,500. The intake must collect that prior amount. Actual plan eligibility, transfers, pension adjustments, overcontribution exposure and the chosen deduction still belong to the complete T1/Schedule 7 work; this subtraction alone is not “no excess.” [F22] [F23] [F24] [F40]

Keep receipts from early 2025 even where already reported for 2024, and do not put them into the ordinary 2025 contribution total again. Actual 2025 Schedule 7 Part A uses March 4-December 31, 2025 plus January 1-March 2, 2026, with prior unused contributions separately. Part B's January 1 start for eligible repayment designations is a separate branch with exclusions; the two windows must not be conflated. [F40]

```oa-check
name: Prior unused contributions change the RRSP room question
inputs:
  stipulated_ordinary_limit: 18500
  new_ordinary_contributions: 12000
  prior_unused: 4000
steps:
  - naive_residual: stipulated_ordinary_limit - new_ordinary_contributions
  - total_ordinary_contributions: prior_unused + new_ordinary_contributions
  - residual_with_prior: stipulated_ordinary_limit - total_ordinary_contributions
  - overstatement: naive_residual - residual_with_prior
expected:
  naive_residual: 6500
  total_ordinary_contributions: 16000
  residual_with_prior: 2500
  overstatement: 4000
```

### Case 4. Shared workspace and a vehicle sample need different evidence

A synthetic workspace is 200 square feet in a 2,000-square-foot home, shared for 40 business hours in a 168-hour week. On an explicitly consistent full-period basis, the area/time ratio is **1/42**, about **2.380952%**. Applying that ratio to 21,000 stipulated eligible household costs gives a **500 pre-limit allocation**. This is not a completed deduction. Principal-place or the alternative qualification, actual costs/period, income cap, carryforward and use evidence must be resolved by the T2125 method; a shared room does not create a flat simplified deduction. [F03] [F18] [F46]

For the separate vehicle record, a full representative base has annual business use 49% and matching three-month use 46%; the later three-month sample shows 51%. The formula gives about **54.326087%**, shown as 54% in CRA's example, within its **39%-59%** range in the absence of contradictory evidence. With a 60% later sample, the same formula gives about **63.913043%**, outside that range. The sample alone then does not establish the whole later year. Do not invent a log, use a simple relative 10% tolerance, or claim the arithmetic proves representativeness. [F19]

```oa-check
name: Intake checks shared-space allocation and vehicle sample evidence
inputs:
  workspace_area: 200
  home_area: 2000
  weekly_business_hours: 40
  weekly_total_hours: 168
  stipulated_eligible_home_costs: 21000
  base_annual_use: 0.49
  base_matching_use: 0.46
  later_sample_use: 0.51
  changed_sample_use: 0.60
steps:
  - area_fraction: workspace_area / home_area
  - time_fraction: weekly_business_hours / weekly_total_hours
  - combined_fraction: area_fraction * time_fraction
  - allocation_before_limits: stipulated_eligible_home_costs * combined_fraction
  - annual_vehicle_fraction: later_sample_use / base_matching_use * base_annual_use
  - lower_boundary: base_annual_use - 0.10
  - upper_boundary: base_annual_use + 0.10
  - changed_vehicle_fraction: changed_sample_use / base_matching_use * base_annual_use
expected:
  area_fraction: 0.1
  time_fraction: 0.2380952380952381
  combined_fraction: 0.02380952380952381
  allocation_before_limits: 500
  annual_vehicle_fraction: 0.5432608695652174
  lower_boundary: 0.39
  upper_boundary: 0.59
  changed_vehicle_fraction: 0.6391304347826087
tolerance: 0.00000001
```

### Case 5. Return lines are not interchangeable

Use synthetic values already supported by the relevant GST/HST component: tax collected/collectible 15,600 at 103, added adjustment 100 at 104, eligible ITCs 1,450 at 106, deductible adjustment 50 at 107, actual instalments 10,000 at 110, no rebates, and other supported debits 200 and 300. Then 105 is **15,700**, 108 is **1,500**, 109 is **14,200**, and the final positive balance after those other credits/debits is **4,700**. Calling 105 merely “collected,” 108 merely “ITCs,” or 109 the final cash due loses the distinction. These amounts are explicit inputs, not approval of the old unsupported 1,450 estimate. [F09] [F10]

```oa-check
name: Reconcile the meaning of GST return totals in the intake
inputs:
  tax_collected: 15600
  added_adjustment: 100
  supported_itc: 1450
  deducted_adjustment: 50
  actual_instalments: 10000
  rebates: 0
  other_debit_a: 200
  other_debit_b: 300
steps:
  - line_105: tax_collected + added_adjustment
  - line_108: supported_itc + deducted_adjustment
  - line_109: line_105 - line_108
  - line_112: actual_instalments + rebates
  - line_113a: line_109 - line_112
  - line_113b: other_debit_a + other_debit_b
  - line_113c: line_113a + line_113b
expected:
  line_105: 15700
  line_108: 1500
  line_109: 14200
  line_112: 10000
  line_113a: 4200
  line_113b: 500
  line_113c: 4700
```

### Case 6. A reminder or bank label is not a paid instalment

The original four 2,500 entries total **10,000** only as an actual income-tax credit if receipts/account records confirm their year and allocation. Suppose bank outflows to the authorities total 11,250, proof identifies those 10,000 income-tax instalments and 1,000 GST/HST payments, and 250 remains unallocated. Preserve all 11,250 in the payment reconciliation, but do not put 11,250 or the reminder amount on T1 47600. Keep the 250 unresolved with its owner and next action; do not silently expense it or treat it as tax paid. Keep the separate GST payment under its actual account/period. [F35] [F36]

```oa-check
name: Preserve bank outflows without inventing a T1 credit
inputs:
  supported_instalment_a: 2500
  supported_instalment_b: 2500
  supported_instalment_c: 2500
  supported_instalment_d: 2500
  supported_gst_payment: 1000
  bank_outflows: 11250
steps:
  - supported_t1_paid: supported_instalment_a + supported_instalment_b + supported_instalment_c + supported_instalment_d
  - supported_allocated: supported_t1_paid + supported_gst_payment
  - unallocated: bank_outflows - supported_allocated
expected:
  supported_t1_paid: 10000
  supported_allocated: 11000
  unallocated: 250
```

### Case 7. The computer allowance needs the right legal basis

For a stipulated eligible new Class 50 computer acquired and available in June 2025, with net capital cost 2,800, full business use, a full 365-day fiscal period, zero opening class UCC and no other pool additions/dispositions/adjustments, the current enacted RIIP/class rule can produce the 55% rate on an adjusted basis using the 9/11 factor, giving a **2,800 maximum allowance**. A smaller claim may be chosen on the actual facts. This is not proof that every asset under 1.5 million qualifies for designated immediate expensing, and the old individual pre-2025 window does not supply the legal basis. The calculation method must establish classification, eligibility, dates, taxes and claim before intake marks it settled. The 770 half-year result below is a hypothetical comparison, not the applicable maximum for these stipulated eligible facts. [F04] [F20] [F21]

```oa-check
name: Distinguish the actual eligible Class 50 basis from an unsupported AIIP label
inputs:
  stipulated_eligible_cost: 2800
  class_rate: 0.55
steps:
  - enhanced_basis: stipulated_eligible_cost * (1 + 9 / 11)
  - conditional_maximum: enhanced_basis * class_rate
  - hypothetical_half_year_comparison: stipulated_eligible_cost * 0.5 * class_rate
  - difference: conditional_maximum - hypothetical_half_year_comparison
expected:
  enhanced_basis: 5090.909090909091
  conditional_maximum: 2800
  hypothetical_half_year_comparison: 770
  difference: 2030
tolerance: 0.00000001
```

### Decision and handoff regressions

| Input | Correct next action |
|---|---|
| User already supplied a complete record and asks only about instalments | Reuse it, get the actual instalment method and missing history/payment facts; no compulsory full return sweep. |
| No T4 is known, but a rental statement exists | Preserve rental income/required schedule; do not claim T2125 is the whole return. [F12](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-3.html) |
| T4 box 16 is present but 16A, other slips or QPP fields are unread | Preserve first-tier amount, mark the missing inventory, and hold the affected contribution result. Do not infer zero second-tier or select a province solely from the bank. [F27](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/tax-slips/understand-your-tax-slips/t4-slips/t4-statement-remuneration-paid.html) [F28](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-22200-deduction-cpp-qpp-contributions-on-self-employment-other-earnings.html) |
| Quebec resident or mixed CPP/QPP, even when bank payments say CRA | Get actual federal and provincial contribution routes and slips; preserve QPIP and QST work where applicable. [F28](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-22200-deduction-cpp-qpp-contributions-on-self-employment-other-earnings.html) [F30](https://www.revenuquebec.ca/en/citizens/income-tax-return/completing-your-income-tax-return/line-by-line-help/400-to-447-income-tax-and-contributions/line-445/) [F31](https://www.revenuquebec.ca/en/citizens/income-tax-return/completing-your-income-tax-return/line-by-line-help/400-to-447-income-tax-and-contributions/line-439/) |
| A full resident temporarily travelled abroad | Do not convert travel alone into non-residence; inspect actual ties/status and applicable treaty facts. [F49](https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/information-been-moved/determining-your-residency-status.html) |
| RRSP provider outflow is visible, no receipt or statement | Ask for the precise missing proof, not whether any record exists; keep amount provisional. [F22](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/rrsps-related-plans/contributing-a-rrsp-prpp/what-unused-rrsp-prpp-contributions.html) [F23](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/rrsps-related-plans/contributing-a-rrsp-prpp/where-you-find-your-rrsp-prpp-deduction-limit.html) |
| Individual has a supported non-calendar fiscal period/election | Preserve it and the T1139/prior additional-income work; do not overwrite December 31. [F16](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-249.1.html) [F17](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t1139/t1139-25e.pdf) |
| A task is complete but another required income source/method is unresolved | Pass supported work with an explicit incomplete whole-package register, not an unqualified final handoff. |
| Client says “looks good,” or the calculation blocks pass | Record that actual confirmation/check; do not invent accountant approval, tax eligibility, a filing receipt or payment. [F50](https://www.canada.ca/en/revenue-agency/services/forms-publications/forms/t183.html) |

## When to refuse or refer

Stop an affected computation or submission when identity, residence, entity, a material fact, conflicting source or required method remains unresolved. State the specific missing evidence and the appropriate next method/person, preserve the records and continue cleanly separable work. Do not guide the user to change answers to fit the scope.

For a corporation, partnership, part-year/non-resident situation or unhandled special income, route the required work accurately. A scoped sole-proprietor method is not authority to drop the person's other income or claim no help is possible. Use a suitable professional for unresolved specialist work where needed, without fabricating a universal CPA-only legal rule. If the user is the accountant, identify the judgement/evidence for their review. [F12] [F15] [F37] [F43] [F44] [F49] [F50]

Refuse an instruction to falsify an account status, deduction, source, approval, filing, receipt or payment. No missing runtime tool permits an invented result or an unsafe legal default.

## Filing and payment

This intake neither files a return nor moves money. Preserve a calendar for each actual year, return, GST/QST period and instalment year, with the official rule and source. A filing due date and payment due date are separate fields.

For the dated **2025** individual return bridge, the ordinary payment date is **April 30, 2026** and qualifying self-employed filing is **June 15, 2026**, subject to the actual special facts and conditions. Do not extend payment to the later filing date. The actual annual GST/HST sole-proprietor exception also depends on calendar fiscal year and business-income conditions; other reporting periods use their actual deadlines. Use the current T1, GST and instalment methods for the complete applicable dates/rules, not this illustration as every person's calendar. [F11] [F26]

Collect actual filing authorizations and acknowledgements only for an authorized filing task, separately from intake confirmation. T183's purpose is to allow an electronic filer to transmit the return; completing intake supplies no such authority. Record a proposed filing/payment instruction as proposed, an actual submission as submitted, and a successful acknowledgement or matched payment only when the receipt exists. [F50]

## Completion checklist

All thirteen original control purposes remain, with unsupported runtime, speed and universal sign-off gates corrected.

| Check | Pass condition |
|---|---|
| IN1 | Scope questions are grouped where independent; no needless one-at-a-time replay. Already known facts are reused. |
| IN2 | The available question mechanism works for the current runtime; no dependence on unavailable `ask_user_input_v0` and no invented tool call. |
| IN3 | Available records are requested/read before tax-content gap questions, unless one genuinely necessary scope fact blocks collection. A focused task does not require a second full dump. |
| IN4 | Actual read coverage, extraction and a factual summary precede follow-up; unread pages and provisional conclusions are visible. [F14](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/business-records.html) |
| IN5 | Questions request only missing/conflicting evidence. A visible bank label does not excuse a missing receipt or account/year check. [F23](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/rrsps-related-plans/contributing-a-rrsp-prpp/where-you-find-your-rrsp-prpp-deduction-limit.html) [F35](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/claim-amounts-tax-return.html) [F36](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/how-pay.html) |
| IN6 | Every material ambiguity has an open flag, source, affected result, owner and next action. Unknown scalar values stay null; supported zeros/false values have evidence. |
| IN7 | The actual `ca-return-assembly` handoff is explicit for a full package, with JSON/evidence/register and actual current child methods. A focused request uses its relevant component. |
| IN8 | Actual approval/name, review and filing-authorization status are recorded separately. No universal CPA rule, approval inheritance or guessed professional sign-off. [F50](https://www.canada.ca/en/revenue-agency/services/forms-publications/forms/t183.html) |
| IN9 | Scope boundaries are truthful and specific, supported independent work continues, and no required income disappears in a referral. [F12](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-3.html) [F37](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-2.html) |
| IN10 | User-facing updates describe findings/actions, without internal phase narration or promised completion before evidence. |
| IN11 | Avoidable turn count is minimized with reuse and batching; record actual unresolved work rather than declaring failure/completion at a fixed minute/turn target. |
| IN12 | Actual registration/effective dates, account/method/period and supply facts are established where needed; not from the invoice or bare annual turnover alone. [F01](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-148.html) [F05](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-240.html) [F07](https://www.canada.ca/en/revenue-agency/services/e-services/digital-services-businesses/confirming-a-gst-hst-account-number.html) [F10](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/calculate-prepare-report/instructions-preparing-return.html) [F11](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/file-gst-hst-return/reporting-requirements-deadlines.html) |
| IN13 | Actual year-end residence, moves/business establishments and Quebec work are retained; GST/HST place-of-supply facts remain separate. [F08](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/charge-collect-place-supply.html) [F30](https://www.revenuquebec.ca/en/citizens/income-tax-return/completing-your-income-tax-return/line-by-line-help/400-to-447-income-tax-and-contributions/line-445/) [F31](https://www.revenuquebec.ca/en/citizens/income-tax-return/completing-your-income-tax-return/line-by-line-help/400-to-447-income-tax-and-contributions/line-439/) [F34](https://www.canada.ca/en/revenue-agency/services/forms-publications/forms/t2203.html) [F49](https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/information-been-moved/determining-your-residency-status.html) |

Before handoff, also check all income/business inventories, duplicate/amended records, actual expense/asset bases and prior pools/carryforwards, all contribution tiers, RRSP periods and unused contributions, payment allocations, current method provenance and the actual artifact/completion state. A passed structure or arithmetic block does not establish legal eligibility, full records or professional approval.

## Sources

Read on **2026-11-14** for the portions named below. This is a bounded intake audit, not every Canadian tax rule, a complete provincial/residency/benefit engine or verification of a real taxpayer's accounts. The actual 2025 forms remain dated references; final 2026 annual form layouts are not represented as read.

| ID | Source and portion read | Official URL | Read on |
|---|---|---|---|
| F01 | Read for ETA 148: worldwide taxable supplies, associates, timing and the specific simplified-regime exception | [Official source](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-148.html) | 2026-11-14 |
| F02 | Read for CRA registration: ordinary single/rolling tests, effective dates, voluntary and taxi branches | [Official source](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/when-register-charge.html) | 2026-11-14 |
| F03 | Read for ITA 18(12): qualifying workspace, income cap and conditional carryforward | [Official source](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-18.html) | 2026-11-14 |
| F04 | Read for ITR 1104: designated immediate-expensing, AIIP and RIIP definitions/windows | [Official source](https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/section-1104.html) | 2026-11-14 |
| F05 | Read for ETA 240: general registration, exceptions, taxi and voluntary branches | [Official source](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-240.html) | 2026-11-14 |
| F06 | Read for ETA 166: small supplier who is not a registrant, with stated exceptions | [Official source](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-166.html) | 2026-11-14 |
| F07 | Read for CRA registry: name, number and transaction-date evidence; no live query performed | [Official source](https://www.canada.ca/en/revenue-agency/services/e-services/digital-services-businesses/confirming-a-gst-hst-account-number.html) | 2026-11-14 |
| F08 | Read for CRA place of supply: supply type/location, not a universal residence-based rate | [Official source](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/charge-collect-place-supply.html) | 2026-11-14 |
| F09 | Read for ETA 169: commercial-use ITCs and required documentation | [Official source](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-169.html) | 2026-11-14 |
| F10 | Read for CRA GST/HST return: actual method, line meanings, adjustments and final balance | [Official source](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/calculate-prepare-report/instructions-preparing-return.html) | 2026-11-14 |
| F11 | Read for CRA GST/HST periods, nil returns and conditional annual sole-proprietor dates | [Official source](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/file-gst-hst-return/reporting-requirements-deadlines.html) | 2026-11-14 |
| F12 | Read for ITA 3: complete income-source computation | [Official source](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-3.html) | 2026-11-14 |
| F13 | Read for CRA accounting methods: accrual and specified cash-method branches | [Official source](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/accounting-methods.html) | 2026-11-14 |
| F14 | Read for CRA business records: income, expenses, assets and separate-business evidence | [Official source](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/business-records.html) | 2026-11-14 |
| F15 | Read for CRA T5013 guide: filing policy and individual partner information | [Official source](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4068/guide-partnership-information-return-t5013-forms.html) | 2026-11-14 |
| F16 | Read for ITA 249.1: calendar default, eligible alternative, revocation and change concurrence | [Official source](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-249.1.html) | 2026-11-14 |
| F17 | Read for Actual 2025 T1139: instructions and Parts 1/2/4/5/6; no final 2026 form claimed | [Official source](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t1139/t1139-25e.pdf) | 2026-11-14 |
| F18 | Read for CRA home expenses: actual-cost allocation, limits, carryforward and CCA consequences | [Official source](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/report-business-income-expenses/completing-form-t2125/business-use-home-expenses.html) | 2026-11-14 |
| F19 | Read for CRA vehicle expenses: full/base/sample logs, formula and actual tolerance example | [Official source](https://www.canada.ca/en/revenue-agency/services/tax/businesses/small-businesses-self-employed-income/business-income-tax-reporting/business-expenses/motor-vehicle-expenses.html) | 2026-11-14 |
| F20 | Read for ITR 1100(2): allowance base/factors including conditional Class 50 | [Official source](https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/section-1100.html) | 2026-11-14 |
| F21 | Read for CRA CCA classes: actual 10/10.1/12/50 descriptions and rates | [Official source](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/report-business-income-expenses/claiming-capital-cost-allowance/classes.html) | 2026-11-14 |
| F22 | Read for CRA unused RRSP contributions: statement/unused amounts; date corrected by Schedule 7 | [Official source](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/rrsps-related-plans/contributing-a-rrsp-prpp/what-unused-rrsp-prpp-contributions.html) | 2026-11-14 |
| F23 | Read for CRA RRSP statement: latest assessment/reassessment and actual available information | [Official source](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/rrsps-related-plans/contributing-a-rrsp-prpp/where-you-find-your-rrsp-prpp-deduction-limit.html) | 2026-11-14 |
| F24 | Read for CRA RRSP limit: deduction limit, unused amounts, receipt period and exclusions | [Official source](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/rrsps-related-plans/contributing-a-rrsp-prpp/contributions-affect-your-rrsp-prpp-deduction-limit.html) | 2026-11-14 |
| F25 | Read for Schedule 7 catalogue: actual 2025 form links, not final 2026 availability | [Official source](https://www.canada.ca/en/revenue-agency/services/forms-publications/forms/5000-s7.html) | 2026-11-14 |
| F26 | Read for CRA annual dates: actual 2025 contribution, filing and payment bridge | [Official source](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/important-dates-individuals.html) | 2026-11-14 |
| F27 | Read for CRA T4 help: actual contribution tiers, EI, pension, withholding and QPIP fields | [Official source](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/tax-slips/understand-your-tax-slips/t4-slips/t4-statement-remuneration-paid.html) | 2026-11-14 |
| F28 | Read for CRA line 22200: CPP/QPP/RC381 routes, mixed income and proration facts | [Official source](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-22200-deduction-cpp-qpp-contributions-on-self-employment-other-earnings.html) | 2026-11-14 |
| F29 | Read for CRA working beneficiaries: employee, self-employed and mixed election routes | [Official source](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/cpp/canada-pension-plan-cpp-contributions-cpp-working-beneficiaries.html) | 2026-11-14 |
| F30 | Read for RQ line 445: Schedule U versus LE-35-V; dated form guidance | [Official source](https://www.revenuquebec.ca/en/citizens/income-tax-return/completing-your-income-tax-return/line-by-line-help/400-to-447-income-tax-and-contributions/line-445/) | 2026-11-14 |
| F31 | Read for RQ line 439: Schedule R/QPIP input route; no current maximum copied | [Official source](https://www.revenuquebec.ca/en/citizens/income-tax-return/completing-your-income-tax-return/line-by-line-help/400-to-447-income-tax-and-contributions/line-439/) | 2026-11-14 |
| F32 | Read for Self-employed EI: agreement and benefit-eligibility conditions | [Official source](https://www.canada.ca/en/services/benefits/ei/ei-self-employed-workers/eligibility.html) | 2026-11-14 |
| F33 | Read for CRA self-employment income: categories, partnership and fiscal-period routes | [Official source](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/personal-income/self-employment-income-lines-13499-14299-gross-income-lines-13500-14300-net-income.html) | 2026-11-14 |
| F34 | Read for T2203 catalogue: multi-jurisdiction business income, not all form instructions | [Official source](https://www.canada.ca/en/revenue-agency/services/forms-publications/forms/t2203.html) | 2026-11-14 |
| F35 | Read for CRA instalment credits: actual 2025 payments, summaries, corrections and Quebec moves | [Official source](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/claim-amounts-tax-return.html) | 2026-11-14 |
| F36 | Read for CRA payment proof: actual account allocation and confirmation | [Official source](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/how-pay.html) | 2026-11-14 |
| F37 | Read for ITA 2: residence/non-residence and taxable-income scope | [Official source](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-2.html) | 2026-11-14 |
| F38 | Read for CRA eligible dependant: facts/conditions, not an automatic award | [Official source](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-30400-amount-eligible-dependant.html) | 2026-11-14 |
| F39 | Read for CRA CCB eligibility and continuing payments; no benefit amount calculated | [Official source](https://www.canada.ca/en/revenue-agency/services/child-family-benefits/canada-child-benefit/who-apply.html) | 2026-11-14 |
| F40 | Read for Actual 2025 Schedule 7: Parts A-D and E/F input categories; ordinary versus repayment dates | [Official source](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5000-s7/5000-s7-25e.pdf) | 2026-11-14 |
| F41 | Read for ITA 18(1)(a)/(b)/(h)/(l): purpose, capital, personal and specified club restrictions | [Official source](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-18.html) | 2026-11-14 |
| F42 | Read for ITA 67.1: ordinary meal limitation, reasonable cost and conditional exceptions | [Official source](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-67.1.html) | 2026-11-14 |
| F43 | Read for ITR 229: partnership information-return framework, with actual administrative policy | [Official source](https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/section-229.html) | 2026-11-14 |
| F44 | Read for CRA corporation filing: resident/non-resident branches and exceptions | [Official source](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/corporations/corporation-income-tax-return/who-file-a-corporation-income-tax-return.html) | 2026-11-14 |
| F45 | Read for Actual 2025 Ontario T1: identification, marital/residence and observed income/settlement fields | [Official source](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-r/5006-r-25e.pdf) | 2026-11-14 |
| F46 | Read for Actual 2025 T2125: expenses, CCA, home expenses and final business-income interface | [Official source](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t2125/t2125-25e.pdf) | 2026-11-14 |
| F47 | Read for CRA separate T2125 requirement for each business or professional activity | [Official source](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/report-business-income-expenses/completing-form-t2125.html) | 2026-11-14 |
| F48 | Read for CRA BN/program-account identity and companion overview | [Official source](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/business-registration/business-number-program-account/need-program-accounts.html) | 2026-11-14 |
| F49 | Read for CRA residence: ties, temporary absence and treaty-status paragraphs only | [Official source](https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/information-been-moved/determining-your-residency-status.html) | 2026-11-14 |
| F50 | Read for T183 catalogue: electronic-filer authorization purpose, not full signature/field requirements | [Official source](https://www.canada.ca/en/revenue-agency/services/forms-publications/forms/t183.html) | 2026-11-14 |
| F51 | Read for Self-employed EI premiums: agreement-year duties and current method handoff | [Official source](https://www.canada.ca/en/services/benefits/ei/ei-self-employed-workers/premiums.html) | 2026-11-14 |
| F52 | Read for Self-employed EI withdrawal: cancellation/withdrawal/benefit-history branches | [Official source](https://www.canada.ca/en/services/benefits/ei/ei-self-employed-workers/withdraw.html) | 2026-11-14 |

Not yet confirmed: actual taxpayer facts, registration and account status, receipt allocations and current professional approval; final 2026 annual form presentation and filing-channel availability; unresolved specialist/provincial work; actual generated artifacts, filing authorization and payment receipts.

Additional official pages read in F39 and F48: [CCB continuing payments](https://www.canada.ca/en/revenue-agency/services/child-family-benefits/canada-child-benefit/get-payments.html) and [BN/program-account overview](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/business-registration/business-number-program-account.html), read on 2026-11-14. These are input/identity references, not authority to award a benefit or activate an account.

The source reads distinguish a current statute from a dated return or guidance illustration. One failed URL, a blocked download or a catalogue link alone was not counted as reading the operative rule. The actual 2025 Schedule 7 resolves the ordinary contribution-period discrepancy; the final-year form and taxpayer record still control an actual claim.

[F01]: https://laws-lois.justice.gc.ca/eng/acts/E-15/section-148.html
[F02]: https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/when-register-charge.html
[F03]: https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-18.html
[F04]: https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/section-1104.html
[F05]: https://laws-lois.justice.gc.ca/eng/acts/E-15/section-240.html
[F06]: https://laws-lois.justice.gc.ca/eng/acts/E-15/section-166.html
[F07]: https://www.canada.ca/en/revenue-agency/services/e-services/digital-services-businesses/confirming-a-gst-hst-account-number.html
[F08]: https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/charge-collect-place-supply.html
[F09]: https://laws-lois.justice.gc.ca/eng/acts/E-15/section-169.html
[F10]: https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/calculate-prepare-report/instructions-preparing-return.html
[F11]: https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/file-gst-hst-return/reporting-requirements-deadlines.html
[F12]: https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-3.html
[F13]: https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/accounting-methods.html
[F14]: https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/business-records.html
[F15]: https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4068/guide-partnership-information-return-t5013-forms.html
[F16]: https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-249.1.html
[F17]: https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t1139/t1139-25e.pdf
[F18]: https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/report-business-income-expenses/completing-form-t2125/business-use-home-expenses.html
[F19]: https://www.canada.ca/en/revenue-agency/services/tax/businesses/small-businesses-self-employed-income/business-income-tax-reporting/business-expenses/motor-vehicle-expenses.html
[F20]: https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/section-1100.html
[F21]: https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/report-business-income-expenses/claiming-capital-cost-allowance/classes.html
[F22]: https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/rrsps-related-plans/contributing-a-rrsp-prpp/what-unused-rrsp-prpp-contributions.html
[F23]: https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/rrsps-related-plans/contributing-a-rrsp-prpp/where-you-find-your-rrsp-prpp-deduction-limit.html
[F24]: https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/rrsps-related-plans/contributing-a-rrsp-prpp/contributions-affect-your-rrsp-prpp-deduction-limit.html
[F25]: https://www.canada.ca/en/revenue-agency/services/forms-publications/forms/5000-s7.html
[F26]: https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/important-dates-individuals.html
[F27]: https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/tax-slips/understand-your-tax-slips/t4-slips/t4-statement-remuneration-paid.html
[F28]: https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-22200-deduction-cpp-qpp-contributions-on-self-employment-other-earnings.html
[F29]: https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/cpp/canada-pension-plan-cpp-contributions-cpp-working-beneficiaries.html
[F30]: https://www.revenuquebec.ca/en/citizens/income-tax-return/completing-your-income-tax-return/line-by-line-help/400-to-447-income-tax-and-contributions/line-445/
[F31]: https://www.revenuquebec.ca/en/citizens/income-tax-return/completing-your-income-tax-return/line-by-line-help/400-to-447-income-tax-and-contributions/line-439/
[F32]: https://www.canada.ca/en/services/benefits/ei/ei-self-employed-workers/eligibility.html
[F33]: https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/personal-income/self-employment-income-lines-13499-14299-gross-income-lines-13500-14300-net-income.html
[F34]: https://www.canada.ca/en/revenue-agency/services/forms-publications/forms/t2203.html
[F35]: https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/claim-amounts-tax-return.html
[F36]: https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/how-pay.html
[F37]: https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-2.html
[F38]: https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-30400-amount-eligible-dependant.html
[F39]: https://www.canada.ca/en/revenue-agency/services/child-family-benefits/canada-child-benefit/who-apply.html
[F40]: https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5000-s7/5000-s7-25e.pdf
[F41]: https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-18.html
[F42]: https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-67.1.html
[F43]: https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/section-229.html
[F44]: https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/corporations/corporation-income-tax-return/who-file-a-corporation-income-tax-return.html
[F45]: https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-r/5006-r-25e.pdf
[F46]: https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t2125/t2125-25e.pdf
[F47]: https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/report-business-income-expenses/completing-form-t2125.html
[F48]: https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/business-registration/business-number-program-account/need-program-accounts.html
[F49]: https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/information-been-moved/determining-your-residency-status.html
[F50]: https://www.canada.ca/en/revenue-agency/services/forms-publications/forms/t183.html
[F51]: https://www.canada.ca/en/services/benefits/ei/ei-self-employed-workers/premiums.html
[F52]: https://www.canada.ca/en/services/benefits/ei/ei-self-employed-workers/withdraw.html

## Moved / Not moved

- Moved: no file or unique supported job moved to a new slug. Actual calculations remain with their existing named components.
- Not moved: scope intake, upload/discovery, every original document/inference family, factual confirmation, gap options, per-business handoff, all legacy schema paths, Quebec/provincial work, dependencies and thirteen control purposes remain here.
- Corrected or retired: invoice/bank-label proof shortcuts, unknown-to-zero defaults, unconditional asset and RRSP conclusions, mandatory December 31 and universal T5013/CPA claims, unavailable-tool gates, unsupported 98,000 profit, duplicated blanket disclaimer and unmeasured minute/turn promises. Their supported collection, review, efficiency and authorization purposes remain in the method and evidence map.
- Version 0.2, 14 November 2026: substantive source-audited replacement of v0.1. No new skill, professional approval or production account action is supplied by this change.
