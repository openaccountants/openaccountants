---
name: construction-sector
description: "For 2026 construction contractors, subcontractors and developers: separate over-time revenue and WIP from country tax methods, UK CIS and VAT reverse-charge conditions, retentions and worker status. Retains the Australian cost-to-cost workpaper and recomputes it; holds unconfirmed national tax figures."
version: 1.0
jurisdiction: GLOBAL
tax_year: 2026
last_updated: 2026-11-14
depends_on:
  - corporate-income-tax-workflow-base
category: vertical
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: tax
type: cross-country-method
---

# Construction sector v1.0

## Quick reference and scope

For 2026 contractors, subcontractors, developers and design-build businesses. Separate financial reporting, income tax, construction withholding, VAT and worker status. Load the country income-tax and VAT jobs with `corporate-income-tax-workflow-base`. This file does not cover safety regulation, permits or engineering standards.

## Ask the client first

- Which entity, country, reporting/tax period, accounting framework and tax accounting basis apply?
- What are the contracts, modifications, enforceable rights, obligations and progress estimates?
- What costs, billings, retentions, claims and prior recognised revenue belong to each contract?
- For UK payments, what are the contractor/subcontractor, employment, CIS verification and VAT registration statuses?
- Who is the VAT customer, is there a qualifying end-user/intermediary notification, and what construction operations are supplied?
- Which subcontractor facts, overseas activity and local tax elections require separate country review?

## The method, step by step

1. Classify the entity, contract, customer and reporting framework. A construction label alone does not establish over-time recognition or tax percentage-of-completion treatment.
2. Establish the enforceable obligations, modifications, constrained transaction price and recognition basis. Select a progress measure that faithfully depicts performance, not simply billed milestones.
3. Reconcile costs, abnormal waste, uninstalled goods and estimates to complete. Measure earned revenue, distinguish unconditional receivables from conditional contract assets and explain retentions.
4. Bridge the accounts to the country's tax contract rules, elections and timing. Keep look-back interest and any small/home-construction exception separate from financial reporting.
5. For each UK payment establish worker status, CIS scope, verification, deduction base, the supplied HMRC deduction rate and VAT reverse-charge treatment independently.
6. Reconcile returns, deductions, payments, invoices and the contract ledger; give the reviewer unresolved estimates, VAT status and tax-source gaps before sign-off.

Accounting authority: [AASB 15, paragraphs 18-45, 50-59, 98 and 105-109](https://standards.aasb.gov.au/aasb-15-dec-2022). UK payment authority is linked at each specific step below. Australian and other national adoption requirements remain separate from the global method.

## What this file is

A sector overlay for construction contractors, subcontractors, developers, and design-build firms.

## Section 1 :  Revenue recognition for long-term contracts

### 1.1 IFRS 15 / ASC 606

- **Performance obligation satisfied over time** :  if any of: Customer simultaneously receives and consumes the benefits (typically for routine services); Work creates or enhances an asset the customer controls; No alternative use to seller + enforceable right to payment for work performed to date  _([T1])_
- **Input method** :  proportion of costs incurred to total expected costs :  most common for construction.  _([T1])_
- **Output method** :  units produced / milestones / surveys :  used where measurable units.
- **Uninstalled materials**: assess whether the cost input faithfully depicts progress. Where paragraph B19(b) conditions are met, transferred goods can require revenue equal to cost; a blanket exclusion from both cost and revenue is wrong. [AASB 15, paragraphs 39-45 and B18-B19](https://standards.aasb.gov.au/aasb-15-dec-2022).

### 1.2 United States: tax contract method handoff

Keep the original questions for IRC section 460, the definition of a long-term contract, tax percentage of completion, the small-contractor exception, home-construction contracts, completed-contract/cash eligibility and look-back interest at completion. The country job must establish the current statutory scope, indexed receipts test, estimated completion test, elections and form. This edition does not carry forward the old receipts threshold or treat all residential construction as automatically exempt from tax PCM. Missing current law leaves these items held in Sources, not decided from the IFRS accounting conclusion.

## Section 2 :  UK Construction Industry Scheme (CIS)

- **CIS overview** :  A withholding regime for payments by contractors to subcontractors in construction operations.  _([T1])_

### 2.1 Contractor obligations

Verify the subcontractor with HMRC before applying a deduction status. A CIS registration does not prove employment status: establish that the worker is not an employee before using the scheme. Build the deduction base from the gross invoice, excluding VAT and the permitted evidenced materials and other items described by HMRC; do not apply a rate indiscriminately to the full invoice.

| Item | Value and condition | Source |
| --- | --- | --- |
| HMRC-verified registered subcontractor deduction | 20% of the CIS deduction base | [HMRC deduction instructions](https://www.gov.uk/what-you-must-do-as-a-cis-contractor/make-deductions-and-pay-subcontractors) |
| Unregistered subcontractor deduction | 30% of that base, as notified on verification | [HMRC deduction instructions](https://www.gov.uk/what-you-must-do-as-a-cis-contractor/make-deductions-and-pay-subcontractors) |
| Gross payment status | 0% deduction only where the verification/status supports it | [HMRC deduction instructions](https://www.gov.uk/what-you-must-do-as-a-cis-contractor/make-deductions-and-pay-subcontractors) |
| Monthly return | By the 19th following the tax month | [HMRC monthly returns](https://www.gov.uk/what-you-must-do-as-a-cis-contractor/file-your-monthly-returns) |
| Monthly payment to HMRC | By the 22nd, or the 19th by post; confirm the PAYE/CIS scheme's actual monthly or permitted quarterly arrangement | [HMRC payment instructions](https://www.gov.uk/what-you-must-do-as-a-cis-contractor/pay-deductions-to-hmrc) |
| Payment/deduction statement | Within 14 days of the tax month end | [HMRC paying subcontractors](https://www.gov.uk/what-you-must-do-as-a-cis-contractor/make-deductions-and-pay-subcontractors) |

Use HMRC's CIS online service or compatible filing software for the monthly return. Reconcile each subcontractor, payment, material exclusion and deduction; include the required employment declaration. For a month with no payments, file a nil return or obtain an inactivity arrangement. Keep the receipt and reconcile the remittance with the PAYE/CIS liability and deduction statements. Refer penalties, quarterly eligibility and disputed status to the current country filing job rather than inventing a date.

### 2.2 Subcontractor and gross payment status

Being paid gross does not exempt the subcontractor's income from tax. Establish registration as a contractor as well if the business makes payments to other subcontractors. Recover deductions through the correct individual/partnership/company route; do not net a company's CIS suffered against any tax at will.

HMRC's turnover test looks at the preceding twelve months, excluding VAT and materials, alongside compliance and business tests. The form depends on whether the applicant is an individual, partnership or company.

| Gross payment turnover test | Condition | Source |
| --- | --- | --- |
| Sole trader | At least GBP 30,000 | [HMRC gross payment status](https://www.gov.uk/what-you-must-do-as-a-cis-subcontractor/gross-payment-status) |
| Partnership | GBP 30,000 per partner or at least GBP 100,000 for the partnership | [HMRC gross payment status](https://www.gov.uk/what-you-must-do-as-a-cis-subcontractor/gross-payment-status) |
| Company | GBP 30,000 per director or at least GBP 100,000 for the company; HMRC also identifies the per-person test for a company controlled by five or fewer people | [HMRC gross payment status](https://www.gov.uk/what-you-must-do-as-a-cis-subcontractor/gross-payment-status) |

Do not use the previous standalone company turnover figure. Apply the actual HMRC eligibility tests and verification outcome before instructing gross payment.

### 2.3 Scope

- **Construction operations**: establish the actual operation and contract, including preparatory, integral and finishing work. Standalone professional architecture, engineering and surveying must be distinguished from a mixed contract. [HMRC CISR14240](https://www.gov.uk/hmrc-internal-manuals/construction-industry-scheme-reform/cisr14240) and [CISR14030](https://www.gov.uk/hmrc-internal-manuals/construction-industry-scheme-reform/cisr14030).
- **Mixed contracts**: if any part includes or relates to construction operations, HMRC treats all payments under that contract as caught, including payments for non-construction work. Splitting invoices does not split the contract. Do not import the VAT reverse-charge small-element concession into the CIS test. [CISR14030, Mixed contracts](https://www.gov.uk/hmrc-internal-manuals/construction-industry-scheme-reform/cisr14030).

## Section 3 :  UK Domestic Reverse Charge for Construction VAT

- **Effective date and applicability** :  Effective 1 March 2021 :  domestic reverse charge applies to most construction services in the UK construction supply chain (subject to certain exceptions for end-user / intermediary supplier).  _([T1])_

### 3.1 Mechanics

- **Invoice notation** :  Supplier issues invoice without VAT (notation: "reverse charge applies; customer pays VAT directly")
- **Customer VAT accounting** :  Customer accounts for output VAT on their return AND recovers as input VAT (subject to standard rules)
- **Net cash effect**: only potentially neutral where the customer can recover all the relevant input VAT in the same period. Partial exemption, non-business use and timing can prevent neutrality.
- **Disadvantages** :  smaller supplier cash flow worsens (no VAT on receipts)

### 3.2 Scope

- **Reverse charge scope**: establish standard/reduced-rated construction services, UK VAT and CIS status and the actual supply chain. It is not identical to CIS: employment-business staff supplies are a specific distinction. End-user and qualifying intermediary-supplier exceptions require their own conditions and written notification; an intermediary is not every business that buys and resells work. [HMRC scope guide](https://www.gov.uk/guidance/vat-domestic-reverse-charge-for-building-and-construction-services) and [technical guide](https://www.gov.uk/guidance/vat-reverse-charge-technical-guide).

### 3.3 End-user / intermediary supplier notification

- **Notification requirement**: an end user or qualifying intermediary supplier must give written notification for the exclusion. Where the customer does not notify and the other reverse-charge conditions are met, the supplier applies the reverse charge, not normal VAT. Retain the notification and status checks with the invoice. [HMRC technical guide, End users and intermediary supplier businesses](https://www.gov.uk/guidance/vat-reverse-charge-technical-guide).

## Section 4 :  Construction VAT

### 4.1 New build, renovation and land: country handoff

Keep distinct workpapers for UK qualifying new residential construction, eligible renovations/empty property, energy-saving materials and commercial land/options to tax. Zero rating and reduced rating have different building, use, supplier and transaction conditions; they are not established by the word "residential". Energy-saving materials must not be assumed to share the same rate as every renovation.

For France, Germany, Italy and Spain, retain the original new-build, social housing, first-home purchase, renovation and land questions, but obtain the current national legal article and transaction conditions. A land sale, an exempt property transfer and a taxable builder's service are different supplies. The old national percentage list, UK renovation percentage and "most land exempt" claim are held in Sources, not usable global rules. The EU VAT Directive permits some reduced-rate categories but does not itself grant every national relief.

### 5.1 Retention

- **Retention**: use the actual contract percentage and conditions. Classify an earned amount as a receivable when only time must pass before payment, or as a contract asset if another performance condition remains. Release of cash retention is not necessarily the date a receivable first exists. Assess credit impairment separately. [AASB 15, paragraphs 105-109](https://standards.aasb.gov.au/aasb-15-dec-2022).

### 5.2 Progress billing

- **Progress billing treatment** :  Issue progress invoice based on completion; Recognise revenue on % completion (not invoice timing); Variance between billed amount and earned revenue → contract asset (earned > billed) or contract liability (billed > earned)  _([T1])_

### 5.3 Australian worked WIP review: cost-to-cost

Apply this example only after a reviewer establishes the contract, performance obligations,
over-time recognition criteria and a cost input method that faithfully depicts progress under
AASB 15. It is a financial reporting workpaper, not an Australian income-tax calculation. Identify
the reporting period, currency, contract version, approved modifications, variable consideration
assessment, costs to date, estimate to complete, prior recognised revenue and cumulative billings.
Missing estimates or an unassessed recognition basis leave the calculation incomplete.

**Fabricated case, AUD, cumulative at the reporting date:** one contract and one performance
obligation qualify for over-time recognition. The transaction price is $1,000,000. A separate
$100,000 unapproved variation is excluded in full on the reviewer's supplied enforceability and
variable-consideration assessment; no automatic percentage of an unapproved claim is included.
Costs incurred are $320,000, including $20,000 of abnormal wasted material that does not depict
progress and was not reflected in the contract price. The remaining eligible costs to complete
are $300,000. Assume there are no receipts, advances or other contract balances beyond those
described below. There are no uninstalled materials, capitalised contract costs or other adjustments
in this example. All incurred costs are expensed here.

| Calculation | Working | Result |
| --- | --- | --- |
| Eligible costs incurred | $320,000 less $20,000 abnormal waste | $300,000 |
| Eligible total costs | $300,000 incurred plus $300,000 to complete | $600,000 |
| Progress | $300,000 / $600,000 | 50% |
| Cumulative revenue | $1,000,000 x 50% | $500,000 |
| Current-period revenue, if prior cumulative revenue was $450,000 | $500,000 less $450,000 | $50,000 |
| Cumulative margin under the stated expense assumption | $500,000 less $320,000 | $180,000 |
| Forecast total margin, including abnormal waste | $1,000,000 less ($320,000 + $300,000) | $380,000 |
| Margin fade from a prior forecast of $400,000 | $380,000 less $400,000 | $20,000 decrease |

Assume cumulative billings of $450,000 are unconditional receivables and the remaining earned
consideration is conditional on further performance. The unbilled contract asset is $50,000;
any unpaid billed receivable is presented separately. If the otherwise identical contract had
billings of $600,000, it would instead have a $100,000 contract liability. Apply the presentation
assessment at the contract level, including any required contract combination; do not offset an
asset on one unrelated contract against a liability on another.

**Reviewer controls and acceptance cases:**

- Removing the abnormal waste from progress does not erase the expense or improve the forecast
  margin. Including it in both progress numerator and denominator would give $320,000 / $620,000
  and would not depict progress on the stated facts.
- Do not treat every uninstalled-material cost as zero revenue. AASB 15 B19(b) can require revenue
  equal to the cost of transferred goods when its conditions are met. Assess control, procurement
  and the relevant conditions separately before adjusting progress and revenue.
- An unsupported estimate to complete, missing prior cumulative revenue or unresolved variation
  assessment must remain visible. Do not default missing costs to zero or call the margin verified.
- Reconcile contract revenue, billings, assets/liabilities and incurred costs to the ledger. Explain
  changes in estimate and assess loss-making contracts under applicable requirements separately;
  this example does not calculate an onerous-contract provision or tax adjustment.

Primary authority: [AASB 15, December 2022 compilation](https://standards.aasb.gov.au/aasb-15-dec-2022),
paragraphs 18-19 and 22-35 (modifications and performance obligations), 39-45 and B18-B19
(progress), 50-59 (variable consideration), 98(b) (waste) and 105-109 (presentation). Check the
[AASB standards index](https://standards.aasb.gov.au/accounting-standards) for the compilation and
amendments applicable to the reporting period. The index read on 14 November 2026 identifies the December 2022
compilation alongside the amendment applicable from 1 July 2026;
[AASB 2022-9, paragraph 18](https://www.legislation.gov.au/F2023L00015/asmade/2023-01-04/text/original/pdf)
deletes Aus5.3, the public-sector-insurance exception, without changing this example's provisions.
The amounts above are fabricated arithmetic, not statutory thresholds.


```oa-check
name: Australian cumulative WIP excluding abnormal waste
inputs:
  price: 1000000
  incurred: 320000
  waste: 20000
  to_complete: 300000
  prior_revenue: 450000
  billings: 450000
  prior_forecast_margin: 400000
steps:
  progress_cost: incurred - waste
  progress_total: progress_cost + to_complete
  progress: progress_cost / progress_total
  cumulative_revenue: price * progress
  current_revenue: cumulative_revenue - prior_revenue
  cumulative_margin: cumulative_revenue - incurred
  forecast_margin: price - incurred - to_complete
  fade: prior_forecast_margin - forecast_margin
  contract_asset: cumulative_revenue - billings
expected:
  progress: 0.5
  cumulative_revenue: 500000
  current_revenue: 50000
  cumulative_margin: 180000
  forecast_margin: 380000
  fade: 20000
  contract_asset: 50000
```

## Section 6 :  Subcontractor classification

- **Employment vs self-employed status** :  material in construction: US: §530 relief; misclassification penalties; specific Department of Labor (Davis-Bacon) prevailing wage requirements on federal contracts; UK: IR35 test for personal service companies; off-payroll worker rules; Many jurisdictions: "deemed employment" tests for construction subcontractors  _([T1])_

## Section 7 :  Reviewer brief

1. Contract register :  every active project
2. Revenue recognition :  PCM input method calculation per contract
3. Uninstalled materials exclusion documented
4. CIS register (UK) :  subcontractor list with status, deductions, monthly returns
5. Domestic reverse charge VAT (UK) :  supply chain map, end-user notifications
6. New-build VAT zero/reduced rate claim support
7. Contract assets / liabilities reconciliation
8. Retention schedule by project / customer
9. Long-term contract look-back interest (US)
10. Subcontractor employment status assessments
11. Reviewer questions :  [T2]/[T3] items

## Section 8 :  Self-checks

- [ ] Financial-reporting over-time criteria and faithful progress measure established; country tax contract method assessed separately
- [ ] Uninstalled goods and abnormal waste treated under their actual progress/revenue conditions
- [ ] Small contractor exception applied where eligible (US)
- [ ] CIS subcontractor verification current (UK)
- [ ] CIS return CIS300 filed monthly
- [ ] Domestic reverse charge applied where required (UK)
- [ ] End-user notification documented (UK)
- [ ] New-build zero/reduced rate VAT supported with HMRC notice/EU PVD reference
- [ ] Retention receivable versus conditional contract asset classified from the enforceable rights
- [ ] Look-back interest computed at contract completion (US)
- [ ] Subcontractor employment status documented (IR35 / §530 / Davis-Bacon)
- [ ] Output flags every [T2]/[T3] item for reviewer judgement

## When to refuse or refer

- Missing enforceability, transaction-price or cost-to-complete support: leave the WIP calculation incomplete.
- Unsupported subcontractor employment status, gross-payment status or end-user notification: do not manufacture a withholding/VAT conclusion.
- Unconfirmed US exception, national VAT rate or specialised overseas contract: retain the exact question for the country job and specialist reviewer.

## Sources

| Source | URL | Read on | Read for |
| --- | --- | --- | --- |
| AASB 15, December 2022 compilation | https://standards.aasb.gov.au/aasb-15-dec-2022 | 2026-11-14 | Read for Recognition/progress sections; paragraphs 18-45, 50-59, 98(b), 105-109 and B18-B19; fabricated WIP case method |
| AASB current standards index | https://standards.aasb.gov.au/accounting-standards | 2026-11-14 | Read for Calendar-year 2026 table and July 2026 public-sector insurance amendment, not a new tax rate |
| HMRC, CIS deductions | https://www.gov.uk/what-you-must-do-as-a-cis-contractor/make-deductions-and-pay-subcontractors | 2026-11-14 | Read for Deduction rates, excluded invoice items, verification and deduction statements |
| HMRC, monthly returns | https://www.gov.uk/what-you-must-do-as-a-cis-contractor/file-your-monthly-returns | 2026-11-14 | Read for Filing service, employment declaration, nil/inactive arrangements and deadline |
| HMRC, paying deductions | https://www.gov.uk/what-you-must-do-as-a-cis-contractor/pay-deductions-to-hmrc | 2026-11-14 | Read for PAYE/CIS payment route and postal/electronic due dates |
| HMRC, gross payment status | https://www.gov.uk/what-you-must-do-as-a-cis-subcontractor/gross-payment-status | 2026-11-14 | Read for Compliance/business/turnover conditions for each entity form and application route |
| HMRC CISR14030 | https://www.gov.uk/hmrc-internal-manuals/construction-industry-scheme-reform/cisr14030 | 2026-11-14 | Read for Mixed contracts and invoice-splitting sections |
| HMRC CISR14240 | https://www.gov.uk/hmrc-internal-manuals/construction-industry-scheme-reform/cisr14240 | 2026-11-14 | Read for Preparatory, integral and finishing construction operations |
| HMRC reverse-charge scope | https://www.gov.uk/guidance/vat-domestic-reverse-charge-for-building-and-construction-services | 2026-11-14 | Read for Covered/excluded construction operations and employment-business distinction |
| HMRC reverse-charge technical guide | https://www.gov.uk/guidance/vat-reverse-charge-technical-guide | 2026-11-14 | Read for End-user and intermediary notification sections, invoice/accounting and mixed-supply boundaries |

Not yet confirmed: current US section 460 contract definition, indexed receipts/estimated-duration exceptions, home-construction scope, completed-contract/cash eligibility and look-back interest procedure; detailed US GAAP comparison; France/Germany/Italy/Spain construction, social housing, first-home, renovation and land VAT regimes; UK new-build/empty-property/energy-saving-material VAT rates and full relief conditions; CIS recovery routes, quarterly-payment eligibility and penalties; country worker-classification, IR35, section 530 and Davis-Bacon details; AASB 2022-9 paragraph-level amendment text beyond the index's listed scope. These topics remain held rather than inheriting unsupported old values.

## Section 9 :  Disclaimer

Construction sector taxation is highly fact-specific. Outputs must be reviewed by credentialed construction sector practitioners. The most up-to-date version is at [openaccountants.com](https://openaccountants.com).

> Contributed by Ryan Duguid.
