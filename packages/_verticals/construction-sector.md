---
name: construction-sector
description: "Use this skill whenever a construction contractor, subcontractor, developer, or design-build firm asks about sector-specific tax / accounting. Trigger on phrases like \"construction industry scheme\", \"CIS\", \"CIS deduction\", \"reverse charge construction VAT\", \"domestic reverse charge construction services\", \"developer's relief\", \"long-term contract\", \"percentage of completion\", \"completed contract\", \"ASC 606 construction\", \"uninstalled materials\", \"retention\", \"subcontractor 1099\", \"USDOL prevailing wage\", \"Davis-Bacon\", \"construction VAT zero-rate new residential\", or any construction-sector tax question. Covers UK Construction Industry Scheme (CIS), UK domestic reverse charge VAT for construction services (effective 1 March 2021), US construction tax (long-term contracts under IRC §460; percentage-of-completion-capitalisable; small contractor exception), EU developer reliefs and new-build zero/reduced VAT rates, retentions and progress billing accounting. Does NOT cover: construction safety regulation, building permit procedures, or technical engineering standards."
version: 0.1
jurisdiction: GLOBAL
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - corporate-income-tax-workflow-base
category: vertical
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Construction Sector

## What this file is

A sector overlay for construction contractors, subcontractors, developers, and design-build firms.

## Section 1 — Revenue recognition for long-term contracts

### 1.1 IFRS 15 / ASC 606

- **Performance obligation satisfied over time** — if any of: Customer simultaneously receives and consumes the benefits (typically for routine services); Work creates or enhances an asset the customer controls; No alternative use to seller + enforceable right to payment for work performed to date  _([T1])_
- **Input method** — proportion of costs incurred to total expected costs — most common for construction.  _([T1])_
- **Output method** — units produced / milestones / surveys — used where measurable units.
- **Uninstalled materials** — exclude from cost-to-cost calculation to avoid overstating progress (IFRS 15 IE19 example).  _([T1])_

### 1.2 US tax — long-term contracts (IRC §460)

- **Long-term contract** — one not completed within the tax year started.  _([T1] IRC §460)_
- **Percentage of Completion Method (PCM)** — required for most contracts; based on cost-to-cost.  _([T1])_
- **Small Contractor Exception** — exempt from PCM if: Average annual gross receipts ≤ USD 30m (2025; indexed); Contract estimated to complete within 2 years  _([T1])_

Small contractor may use Completed Contract Method (CCM) or Cash method for short-duration contracts.

- **Home Construction Contract Exception** — residential construction not required to use PCM.  _([T1])_

### 1.3 Look-back interest (US)

- **§460(b)(2) look-back interest** — at completion of long-term contract, recompute PCM based on actual rather than estimated costs; if difference creates over- or under-payment, interest computed.  _([T1] §460(b)(2))_

## Section 2 — UK Construction Industry Scheme (CIS)

- **CIS overview** — A withholding regime for payments by contractors to subcontractors in construction operations.  _([T1])_

### 2.1 Contractor obligations

- **Verify subcontractor with HMRC** — Contractor must verify subcontractor with HMRC
- **Gross payment status deduction** — 0% percent
- **Registered subcontractor deduction** — 20% percent
- **Unregistered subcontractor deduction** — 30% percent
- **Monthly CIS return (CIS300)** — by 19th of month
- **Payment of CIS deducted** — by 22nd (electronic) / 19th (cheque)

### 2.2 Subcontractor

- **Register as contractor** — if employs other subbies
- **Gross payment status turnover threshold** — GBP 30k per individual / GBP 30k per partner / GBP 200k per company GBP
- **Recover CIS deductions** — Recover CIS deductions against own tax liability

### 2.3 Scope

- **Construction operations** — include site preparation, demolition, installation, building, painting/decorating, alteration. Excludes architecture, engineering, surveying.  _([T1])_
- **Mixed contracts** — full CIS applies unless the construction element is incidental and minor.  _([T1])_

## Section 3 — UK Domestic Reverse Charge for Construction VAT

- **Effective date and applicability** — Effective 1 March 2021 — domestic reverse charge applies to most construction services in the UK construction supply chain (subject to certain exceptions for end-user / intermediary supplier).  _([T1])_

### 3.1 Mechanics

- **Invoice notation** — Supplier issues invoice without VAT (notation: "reverse charge applies; customer pays VAT directly")
- **Customer VAT accounting** — Customer accounts for output VAT on their return AND recovers as input VAT (subject to standard rules)
- **Net cash effect** — nil for customer
- **Disadvantages** — smaller supplier cash flow worsens (no VAT on receipts)

### 3.2 Scope

- **Reverse charge scope** — Same as CIS for "construction services" between VAT-registered parties — supplier must charge reverse charge to other contractors. Excludes: Supplies to "end-users" (the final customer in the chain — typically the developer or building owner); Supplies to "intermediary suppliers" (those who acquire and on-supply construction services to end-users)  _([T1])_

### 3.3 End-user / intermediary supplier notification

- **Notification requirement** — End-user / intermediary must notify supplier in writing; failure to notify means supplier should charge VAT normally.

## Section 4 — Construction VAT

### 4.1 New-build residential

- **UK** — Zero-rated (Item 2(a) Group 5 Schedule 8 VATA)  _([T1] Item 2(a) Group 5 Schedule 8 VATA)_
- **France new-build residential VAT** — Reduced rate 5.5% for social housing (HLM); 10% for certain renovations  _([T1])_
- **Germany new-build residential VAT** — Standard 19% on most; some construction services in residential sector exempt  _([T1])_
- **Italy new-build residential VAT** — 4% on first-home purchase; 10% on non-first-home new build  _([T1])_
- **Spain new-build residential VAT** — Reduced 10% on new residential  _([T1])_

### 4.2 Renovation

- **UK renovation VAT** — Reduced rate 5% for certain residential renovation (over-2-years empty; energy-saving materials)  _([T1])_
- **EU renovation VAT** — Reduced rates per Annex III PVD allowed  _([T1])_

### 4.3 Land

- **Land VAT treatment** — Most jurisdictions exempt sale of unimproved land. UK option to tax permitted for commercial land.  _([T1])_

### 5.1 Retention

- **Retention practice and accounting** — Construction contracts typically retain 5-10% of each progress payment for defects liability period. Accounting: Contract asset (under IFRS 15 / ASC 606) for amount earned but not billed; Retention receivable recognised when retention released; Bad debt provision for retention if collection uncertain  _([T1])_

### 5.2 Progress billing

- **Progress billing treatment** — Issue progress invoice based on completion; Recognise revenue on % completion (not invoice timing); Variance between billed amount and earned revenue → contract asset (earned > billed) or contract liability (billed > earned)  _([T1])_

## Section 6 — Subcontractor classification

- **Employment vs self-employed status** — material in construction: US: §530 relief; misclassification penalties; specific Department of Labor (Davis-Bacon) prevailing wage requirements on federal contracts; UK: IR35 test for personal service companies; off-payroll worker rules; Many jurisdictions: "deemed employment" tests for construction subcontractors  _([T1])_

## Section 7 — Reviewer brief

1. Contract register — every active project
2. Revenue recognition — PCM input method calculation per contract
3. Uninstalled materials exclusion documented
4. CIS register (UK) — subcontractor list with status, deductions, monthly returns
5. Domestic reverse charge VAT (UK) — supply chain map, end-user notifications
6. New-build VAT zero/reduced rate claim support
7. Contract assets / liabilities reconciliation
8. Retention schedule by project / customer
9. Long-term contract look-back interest (US)
10. Subcontractor employment status assessments
11. Reviewer questions — [T2]/[T3] items

## Section 8 — Self-checks

- [ ] Long-term contracts on PCM input cost-to-cost
- [ ] Uninstalled materials excluded from cost-to-cost
- [ ] Small contractor exception applied where eligible (US)
- [ ] CIS subcontractor verification current (UK)
- [ ] CIS return CIS300 filed monthly
- [ ] Domestic reverse charge applied where required (UK)
- [ ] End-user notification documented (UK)
- [ ] New-build zero/reduced rate VAT supported with HMRC notice/EU PVD reference
- [ ] Retention receivable recognised when contractually due
- [ ] Look-back interest computed at contract completion (US)
- [ ] Subcontractor employment status documented (IR35 / §530 / Davis-Bacon)
- [ ] Output flags every [T2]/[T3] item for reviewer judgement

## Section 9 — Disclaimer

Construction sector taxation is highly fact-specific. Outputs must be reviewed by credentialed construction sector practitioners. The most up-to-date version is at [openaccountants.com](https://openaccountants.com).

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is
different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your
jurisdiction — **no liability on either side until you and the accountant sign
a formal engagement letter** — book a free 30-minute call:

**→ [Book a call](https://calendly.com/openaccountants-info/30min)**

We'll route you to the named verifier covering your country or state. You can
also see the full list of verified accountants at
[openaccountants.com/network](https://openaccountants.com/network).

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
