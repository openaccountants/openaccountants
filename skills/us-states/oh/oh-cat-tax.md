---
name: oh-cat-tax
description: Triggers when the taxpayer operates a business in Ohio with gross receipts potentially exceeding the Commercial Activity Tax (CAT) threshold. Covers CAT registration, filing, computation at 0.26% on taxable gross receipts above the exclusion amount ($6 million for 2025+), quarterly filing requirements, and the 2024 reform changes under HB 33.
version: "0.1"
jurisdiction: US-OH
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# OH Cat Tax

## Ohio Commercial Activity Tax (CAT) Skill — Self-Employed / Sole Proprietor

> **Scope.** Ohio Commercial Activity Tax for sole proprietors and businesses with Ohio taxable gross receipts potentially exceeding the filing threshold. Covers the CAT as reformed by Am. Sub. HB 33 (2023), effective for tax periods beginning January 1, 2024 and after.
> **Quality tier.** Q3 — AI-drafted, not independently verified. All rates and thresholds have been researched from primary sources but must be confirmed by a qualified professional before use.

## Section 1: Metadata

- **Tax year covered** — 2025 and after
- **Primary form** — CAT Annual/Quarterly Return (filed via Ohio Business Gateway)
- **Tax authority** — [Ohio Department of Taxation](https://tax.ohio.gov/business/ohio-business-taxes/commercial-activities)
- **Tax type** — Gross receipts tax
- **Filing threshold** — Taxable gross receipts (TGR) > $6,000,000 (2025+)
- **Currency date** — May 2026
- **https://codes.ohio.gov/ohio-revised-code/chapter-5751** — https://codes.ohio.gov/ohio-revised-code/chapter-5751  _(Ohio Revised Code § 5751 (CAT statute))_
- **https://dam.assets.ohio.gov/image/upload/tax.ohio.gov/commercial_activities/information_releases/CAT_2023-01_info_release.pdf** — https://dam.assets.ohio.gov/image/upload/tax.ohio.gov/commercial_activities/information_releases/CAT_2023-01_info_release.pdf  _(Ohio Information Release CAT 2023-01)_
- **https://tax.ohio.gov/business/ohio-business-taxes/commercial-activities/changes_to_ohios_commercial_activity_tax** — https://tax.ohio.gov/business/ohio-business-taxes/commercial-activities/changes_to_ohios_commercial_activity_tax  _(Ohio CAT Changes Page)_
- **https://www.legislature.ohio.gov/legislation/135/hb33** — https://www.legislature.ohio.gov/legislation/135/hb33  _(Am. Sub. HB 33, 135th General Assembly)_

**Section 1: Metadata table**

| Field | Value |
| --- | --- |
| Tax year covered | 2025 and after |
| Primary form | CAT Annual/Quarterly Return (filed via Ohio Business Gateway) |
| Tax authority | [Ohio Department of Taxation](https://tax.ohio.gov/business/ohio-business-taxes/commercial-activities) |
| Tax type | Gross receipts tax |
| Filing threshold | Taxable gross receipts (TGR) > $6,000,000 (2025+) |
| Currency date | May 2026 |

**Primary sources**

| Source | URL |
| --- | --- |
| Ohio Revised Code § 5751 (CAT statute) | https://codes.ohio.gov/ohio-revised-code/chapter-5751 |
| Ohio Information Release CAT 2023-01 | https://dam.assets.ohio.gov/image/upload/tax.ohio.gov/commercial_activities/information_releases/CAT_2023-01_info_release.pdf |
| Ohio CAT Changes Page | https://tax.ohio.gov/business/ohio-business-taxes/commercial-activities/changes_to_ohios_commercial_activity_tax |
| Am. Sub. HB 33, 135th General Assembly | https://www.legislature.ohio.gov/legislation/135/hb33 |

## Section 2: Quick reference — rates and thresholds

### CAT rate and exclusion by year

**CAT rate and exclusion by year**

| Calendar year | Exclusion amount | Annual minimum tax | Tax rate on TGR above exclusion | Filing required? |
| --- | --- | --- | --- | --- |
| Pre-2024 | $1,000,000 | $150 – $2,600 (tiered) | 0.26% | TGR > $150,000 |
| 2024 | $3,000,000 | Eliminated | 0.26% | TGR > $3,000,000 |
| 2025 and after | $6,000,000 | Eliminated | 0.26% | TGR > $6,000,000 |

### What this means for most sole proprietors

The vast majority of sole proprietors will **not** owe any CAT starting in 2025. Only businesses with more than $6 million in Ohio taxable gross receipts are subject to the tax. A typical sole proprietor or freelancer with annual revenue well under $6 million has no CAT obligation.

### CAT computation formula (2025+)

- **CAT computation formula (2025+)** — If Ohio TGR ≤ $6,000,000: CAT = $0 (no filing required) If Ohio TGR > $6,000,000: CAT = 0.26% × (Ohio TGR − $6,000,000)  _(Section 2: Quick reference — rates and thresholds)_

## Section 3: Key concepts

### What are "taxable gross receipts"?

- **Taxable gross receipts (TGR)** — Taxable gross receipts (TGR) include all gross receipts sitused to Ohio, with limited exclusions. For a sole proprietor, this generally means total revenue from sales of goods or services to Ohio customers. **Included:** - Revenue from sale of goods/services to Ohio customers - Gross receipts from Ohio-sitused transactions (based on where the customer receives the benefit) **Excluded (not exhaustive):** - Receipts from sales of motor fuel (subject to motor fuel tax) - Receipts from sales of a business or substantial assets in a single transaction - Interest income from federal obligations - Certain insurance premiums - Receipts from qualifying exempt organizations

### Situsing rules

- **Situsing rules** — **Tangible personal property:** Sitused to Ohio if delivered to or received by the customer in Ohio. **Services:** Sitused to Ohio if the benefit of the service is received in Ohio. **Real property:** Sitused to Ohio if the property is in Ohio.

### Relationship to Ohio income tax

- **Relationship to Ohio income tax** — The CAT is a separate tax from Ohio income tax. It is a **gross receipts tax**, not an income tax. A business may owe both CAT and Ohio income tax. CAT payments are NOT deductible on the Ohio income tax return (ORC § 5747.01(A) excludes the CAT from the definition of "taxes" for deduction purposes). However, CAT payments may be deductible on the federal return as a business expense.  _(ORC § 5747.01(A))_

## Section 4: Filing requirements (2025+)

### Registration

- **Registration requirements** — Businesses must register for CAT within 30 days of exceeding $6 million in Ohio TGR. Registration is done via the Ohio Business Gateway or Form CAT 1. Failure to register timely: penalty of up to $100/month, not to exceed $1,000.

### Filing frequency

- **Quarterly returns only** — Quarterly returns only (annual filing was eliminated after the 2023 annual return). Quarterly returns are due by the last day of the second month after the quarter ends.

**Quarterly filing schedule**

| Quarter | Period | Due date |
| --- | --- | --- |
| Q1 | Jan 1 – Mar 31 | May 10 |
| Q2 | Apr 1 – Jun 30 | Aug 10 |
| Q3 | Jul 1 – Sep 30 | Nov 10 |
| Q4 | Oct 1 – Dec 31 | Feb 10 (following year) |

### Cancellation

- **Cancellation of CAT account** — Businesses with $6 million or less in TGR for 2025 can cancel their CAT account via the Ohio Business Gateway or by submitting a Business Account Update Form (BA-UF). A final return is required.

## Section 5: 2024 reform summary (HB 33)

Am. Sub. HB 33 of the 135th Ohio General Assembly made the following changes:

1. **Exclusion amount tripled (2024):** Increased from $1 million to $3 million.
2. **Exclusion amount doubled again (2025+):** Increased to $6 million.
3. **Annual minimum tax eliminated:** The tiered minimum tax ($150–$2,600) was eliminated entirely starting 2024.
4. **Annual filing eliminated:** Only quarterly returns are accepted for tax periods beginning 2024+.
5. **Tax rate unchanged:** The 0.26% rate was NOT changed.

**Net effect:** Approximately 90% of previously filing CAT taxpayers are now exempt from the tax.

## Section 6: Refusal catalogue

- **REFUSE-CAT-1** — REFUSE to prepare a CAT return for a combined/consolidated group without complete group member information. Combined reporting for affiliated groups requires specialized handling.  _(REFUSE-CAT-1)_
- **REFUSE-CAT-2** — REFUSE to determine situsing for complex multi-state service transactions without reviewer guidance. The benefit-of-the-service-received test can be ambiguous for services provided remotely.  _(REFUSE-CAT-2)_
- **REFUSE-CAT-3** — REFUSE to advise on whether a specific receipt category is excluded from TGR without confirming against ORC § 5751.01(F)(2) exclusion list.  _(REFUSE-CAT-3 / ORC § 5751.01(F)(2))_

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

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
