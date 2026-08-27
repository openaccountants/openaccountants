---
name: mb-rst
description: Use this skill for Manitoba Retail Sales Tax (RST) — 7% sales tax (NOT harmonized with federal GST). Triggers "Manitoba RST", "Manitoba PST 7%", "MB sales tax", "TAXcess Manitoba", "Manitoba sales tax online sales".
jurisdiction: CA
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# MB Rst

## Manitoba — Retail Sales Tax (RST) — Skill v1.0

## 1. Quick reference

**Quick reference table**

| Item | Value |
| --- | --- |
| Standard RST rate | **7%** |
| Tax base | Tangible personal property + specified taxable services |
| Federal harmonization | **No** — RST is a separate provincial tax, stacked on top of 5% federal GST |
| Effective combined rate (GST + RST) | **12%** on most taxable goods/services in MB |
| Economic nexus threshold (non-resident sellers) | **CAD $10,000** in MB taxable sales in a 12-month period |
| Portal | **TAXcess** (Manitoba Finance online services) |
| Filing frequency | Monthly / Quarterly / Annually — assigned by Taxation Division based on volume |
| Governing statute | The Retail Sales Tax Act (C.C.S.M. c. R130) |
| Regulator | Manitoba Finance — Taxation Division |

RST is administered provincially. It is NOT a value-added tax — there is no input tax credit (ITC) mechanism. Tax paid on inputs is generally a sunk cost unless a specific resale or production-input exemption applies.

## 2. Required inputs + refusal catalogue

### Required inputs before producing a return

- **Required inputs list** — 1. **RST Number** (7-digit account number issued by Manitoba Finance). 2. **Filing period** (start and end date) and assigned filing frequency. 3. **Gross sales in Manitoba** for the period, split between: Taxable sales (TPP + taxable services delivered to MB customers); Exempt / zero-rated sales (groceries, prescriptions, residential rent, children's clothing, etc.); Sales to other provinces / export (out-of-scope for MB RST). 4. **RST collected** from MB customers during the period. 5. **Taxable purchases on which RST was not paid at source** (self-assessed RST on imports / out-of-province purchases used in MB). 6. **Accommodation revenue** separately, because the 5% lodging tax is reported in its own field. 7. **Commission entitlement** — vendors who file and remit on time may claim a small collection commission (capped); confirm whether the client is electing it.

### Refusal catalogue (out of scope for v1.0)

**Refusal catalogue table**

| Code | Refusal | Reason |
| --- | --- | --- |
| R-MB-1 | Insurance premium RST (auto, group life, property) | Specialized RST rules under the Act and bulletins; route to insurance specialist. |
| R-MB-2 | Tobacco, fuel, cannabis, liquor taxes | Separate Manitoba tax statutes (Tobacco Tax Act, Fuel Tax Act, Liquor Gaming and Cannabis Control Act). |
| R-MB-3 | Mining, oil & gas, electricity production input exemptions | Sector-specific certificates and bulletins; specialist review required. |
| R-MB-4 | Real property contracts (RPCs) and the contractor / installer rules | Contractor pays RST on materials; intricate self-assessment regime — refer to Bulletin 005. |
| R-MB-5 | Used vehicle and aircraft transfers between private parties | Valuation rules (Red Book / appraisal) and Autopac collection mechanics out of scope. |
| R-MB-6 | Bundled / mixed supplies where >10% of value is a taxable service inside an otherwise exempt supply | Apportionment requires fact-specific analysis. |
| R-MB-7 | First Nations on-reserve sales claiming s. 87 Indian Act exemption | Documentation and delivery-to-reserve evidence required; refer to Bulletin 047. |
| R-MB-8 | Voluntary disclosure / arrears / audit defense filings | Requires direct negotiation with Taxation Division. |

- **R-MB-1** — Insurance premium RST (auto, group life, property)  _(Specialized RST rules under the Act and bulletins; route to insurance specialist.)_
- **R-MB-2** — Tobacco, fuel, cannabis, liquor taxes  _(Separate Manitoba tax statutes (Tobacco Tax Act, Fuel Tax Act, Liquor Gaming and Cannabis Control Act).)_
- **R-MB-3** — Mining, oil & gas, electricity production input exemptions  _(Sector-specific certificates and bulletins; specialist review required.)_
- **R-MB-4** — Real property contracts (RPCs) and the contractor / installer rules  _(Contractor pays RST on materials; intricate self-assessment regime — refer to Bulletin 005.)_
- **R-MB-5** — Used vehicle and aircraft transfers between private parties  _(Valuation rules (Red Book / appraisal) and Autopac collection mechanics out of scope.)_
- **R-MB-6** — Bundled / mixed supplies where >10% of value is a taxable service inside an otherwise exempt supply  _(Apportionment requires fact-specific analysis.)_
- **R-MB-7** — First Nations on-reserve sales claiming s. 87 Indian Act exemption  _(Documentation and delivery-to-reserve evidence required; refer to Bulletin 047.)_
- **R-MB-8** — Voluntary disclosure / arrears / audit defense filings  _(Requires direct negotiation with Taxation Division.)_
- **Escalation rule** — If any of the above is present, stop and route to a credentialed Manitoba tax practitioner.

## 3. Rate structure

**Rate structure table**

| Supply | Rate | Notes |
| --- | --- | --- |
| Standard taxable supplies (TPP + taxable services) | **7%** | Applied to the selling price exclusive of GST. |
| Liquor (retail) | 7% RST | Stacked with the federal excise + liquor markup. |
| Tobacco | Tobacco Tax (specific per-unit) | RST does NOT apply on top — Tobacco Tax Act governs. **Refusal R-MB-2**. |
| Fuel | Fuel Tax (specific per-litre) | Separate Act. **Refusal R-MB-2**. |
| Accommodations (hotels, short-term rentals) | **7% RST + 5% Lodging Tax** = 12% provincial layer | Lodging tax reported separately on the RST return. |
| Insurance premiums (taxable lines) | 7% | **Refusal R-MB-1**. |
| Electricity / natural gas (residential) | Exempt | Commercial use generally taxable. |

- **Standard taxable supplies (TPP + taxable services)** — **7%**  _(Applied to the selling price exclusive of GST.)_
- **Liquor (retail)** — 7% RST  _(Stacked with the federal excise + liquor markup.)_
- **Tobacco** — Tobacco Tax (specific per-unit)  _(RST does NOT apply on top — Tobacco Tax Act governs. **Refusal R-MB-2**.)_
- **Fuel** — Fuel Tax (specific per-litre)  _(Separate Act. **Refusal R-MB-2**.)_
- **Accommodations (hotels, short-term rentals)** — **7% RST + 5% Lodging Tax** = 12% provincial layer  _(Lodging tax reported separately on the RST return.)_
- **Insurance premiums (taxable lines)** — 7%  _(**Refusal R-MB-1**.)_
- **Electricity / natural gas (residential)** — Exempt  _(Commercial use generally taxable.)_
- **Base for RST** — **Base for RST**: the *selling price before GST*. RST is NOT calculated on the GST-inclusive price. Do not compound.

Worked: a CAD $1,000 software licence sold to a Winnipeg customer: GST (5%) = $50.00; RST (7%) = $70.00 (on the $1,000 base, NOT on $1,050); Customer pays $1,120.00

## 4. Registration

### Who must register

- **Registration requirements** — A person must register and collect RST if they: 1. **Carry on business in Manitoba** and make taxable sales of goods or taxable services, OR 2. **Are a non-resident / out-of-province vendor** that meets the **economic nexus** test introduced effective **1 December 2021** under amendments to the Retail Sales Tax Act: Makes taxable retail sales in Manitoba exceeding **CAD $10,000** in the prior 12 months, AND Solicits orders from Manitoba purchasers (e.g., via website, advertising), AND Causes goods to be delivered to Manitoba. 3. **Online accommodation platforms** (e.g., short-term rental marketplaces) must register and collect RST + lodging tax on accommodations situated in Manitoba. 4. **Marketplace facilitators** that enable third-party sales of taxable goods to Manitoba purchasers must register and collect RST on facilitated sales (post-2021 rules). 5. **Audio and video streaming services** with Manitoba subscribers — explicit listing as taxable specified service post-2021.  _(amendments to the Retail Sales Tax Act, effective 1 December 2021)_

### Process

- **Registration process** — Register through **TAXcess** (online) or paper Form MBT-RL1. No registration fee. Manitoba Finance issues a 7-digit RST number. Assigns filing frequency on registration based on expected tax to collect.

## 5. Taxable supplies — what RST applies to

### Tangible personal property (TPP)

- **TPP default rule** — Default: all sales of TPP delivered to a Manitoba purchaser are taxable unless an exemption applies.

### Specified taxable services (key for software / professional services firms)

Manitoba taxes **more services than most other PST provinces**. Notable taxable services:

**Specified taxable services table**

| Service | Taxable? | Note |
| --- | --- | --- |
| **Legal services** | Yes — 7% | Manitoba is one of the few provinces taxing legal services. |
| **Accounting services** | Yes — 7% | Bookkeeping, tax prep, audit, advisory — RST applies. |
| **Security and investigation services** | Yes — 7% |  |
| **Telecommunications** | Yes — 7% | Includes wireless, internet, long-distance. |
| **Audio / video streaming services** | Yes — 7% | Post-2021. |
| **Software** — packaged / shrink-wrap | Yes — 7% |  |
| **Software** — custom-developed for a single customer | **Exempt** if the development is bespoke and not resold | Strict test; see Bulletin 057. |
| **Software-as-a-Service (SaaS)** | Yes — 7% | Treated as taxable software / specified service when accessed by MB users. |
| **Cloud computing / data storage** | Generally taxable | Where the customer is in MB. |
| **Architectural / engineering services** | **Exempt** (services), but TPP components taxable |  |
| **Personal services** (haircuts, massage) | Exempt | Unlike Saskatchewan. |
| **Repair / installation services to TPP** | Yes — 7% |  |
| **Dry cleaning / laundry** | Yes — 7% |  |

- **Legal services** — Yes — 7%  _(Manitoba is one of the few provinces taxing legal services.)_
- **Accounting services** — Yes — 7%  _(Bookkeeping, tax prep, audit, advisory — RST applies.)_
- **Security and investigation services** — Yes — 7%
- **Telecommunications** — Yes — 7%  _(Includes wireless, internet, long-distance.)_
- **Audio / video streaming services** — Yes — 7%  _(Post-2021.)_
- **Software — packaged / shrink-wrap** — Yes — 7%
- **Software — custom-developed for a single customer** — **Exempt** if the development is bespoke and not resold  _(Strict test; see Bulletin 057.)_
- **Software-as-a-Service (SaaS)** — Yes — 7%  _(Treated as taxable software / specified service when accessed by MB users.)_
- **Cloud computing / data storage** — Generally taxable  _(Where the customer is in MB.)_
- **Architectural / engineering services** — **Exempt** (services), but TPP components taxable
- **Personal services (haircuts, massage)** — Exempt  _(Unlike Saskatchewan.)_
- **Repair / installation services to TPP** — Yes — 7%
- **Dry cleaning / laundry** — Yes — 7%

This breadth — particularly **legal, accounting, security, telecom, SaaS, and streaming** — is the single biggest difference between MB RST and the more limited Saskatchewan PST base.

## 6. Exemptions

Common exemptions (this is not exhaustive — confirm against current MB Finance bulletins): **Basic groceries** (parallels GST zero-rating; prepared meals and snack food remain taxable). **Prescription drugs and dispensing fees**; certain over-the-counter drugs where Schedule listed. **Medical and dental devices** prescribed (insulin, prosthetics, hearing aids, eyeglasses with prescription). **Residential rent** (long-term housing). **Children's clothing and footwear** (sized for children up to age 14, within Bulletin 027 size schedule). **Books** — printed books with an ISBN are exempt. **Farm implements and production inputs** held under a valid Farm Use Certificate. **Manufacturing production equipment** under the production-input exemption (Bulletin 030). **Goods purchased for resale** — provide RST number on the purchase order (resale exemption). **Sales to status Indians / First Nations on-reserve** with delivery to reserve (**Refusal R-MB-7** if facts are not clear). **Sales exported out of Manitoba** with documented delivery to another jurisdiction. When relying on an exemption, document it: certificate, RST number of the purchaser, delivery records, or prescription as applicable. Audit risk is concentrated here.

## 7. Filing — TAXcess

### Mechanics

- **Filing mechanics** — File and pay through **TAXcess** (`https://taxcess.gov.mb.ca/`). Return due **on or before the 20th day of the month following the end of the reporting period**. Late filing: penalty (typically 10% of tax owing) + interest. Returns must be filed even if **NIL** (no sales / no tax collected).  _(https://taxcess.gov.mb.ca/)_

### Frequencies

**Filing frequencies table**

| Annual RST collected | Frequency |
| --- | --- |
| > CAD $5,000 / month average | Monthly |
| CAD $500 – $5,000 / month | Quarterly |
| < CAD $500 / month | Annually |

- **> CAD $5,000 / month average** — Monthly
- **CAD $500 – $5,000 / month** — Quarterly
- **< CAD $500 / month** — Annually

Manitoba Finance reassesses frequency periodically.

### Key boxes on the return

- **Return line items** — 1. Gross sales 2. Less: exempt / non-taxable sales 3. Net taxable sales 4. RST collected (line 3 × 7%, reconciled to books) 5. Taxable purchases — self-assessed RST 6. Total tax payable 7. Less: vendor commission (if applicable and on-time) 8. Net remittance 9. Accommodation / lodging tax (separate line — 5%)

## 8. Combined GST + RST

Manitoba did NOT harmonize with the federal GST. The two taxes are **stacked, not combined**: 5% federal GST/HST (administered by CRA); 7% provincial RST (administered by Manitoba Finance); **Effective rate on a standard taxable supply = 12%**

- **Critical practitioner points** — 1. RST is calculated on the **price excluding GST** — do not compound the two taxes. 2. There is **no input tax credit** for RST. Tax paid on business inputs is a cost of doing business, unless a resale or production exemption applies and a valid exemption was claimed at the time of purchase. 3. A registrant must file **two separate returns**: GST/HST return with CRA, and RST return with Manitoba Finance (TAXcess). Reconcile the gross sales line between the two — auditors compare. 4. Invoices to Manitoba customers should show GST and RST as separate line items.

## 9. Worked example — Winnipeg software company

**Facts** Acme Software Inc. is a Manitoba corporation with its office in Winnipeg. Quarterly RST filer. Q1 2025 (Jan 1 – Mar 31):

**Revenue streams table**

| Revenue stream | Gross | Customer location | RST treatment |
| --- | --- | --- | --- |
| SaaS subscriptions to MB-based clients | $80,000 | MB | Taxable @ 7% |
| SaaS subscriptions to Ontario clients | $120,000 | ON | Out-of-scope for MB RST (ON has HST, separate analysis) |
| Custom software development for one Winnipeg client (bespoke, not resold) | $40,000 | MB | **Exempt** under custom-software carve-out (Bulletin 057) — document the bespoke nature |
| Off-the-shelf software licences sold to MB clients | $15,000 | MB | Taxable @ 7% |
| Telecom resale (managed Wi-Fi) to MB clients | $5,000 | MB | Taxable @ 7% (telecom is a specified taxable service) |
| Sales to a Saskatchewan client | $10,000 | SK | Out-of-scope for MB RST (SK PST analysis separate) |
| **Total** | **$270,000** |  |  |

Self-assessed RST on out-of-province purchases used in MB: Cloud hosting from a US vendor not registered for MB RST: $8,000 of MB-attributable usage → self-assess 7% = $560.

**Computation table**

| Line | Amount |
| --- | --- |
| Gross sales | $270,000 |
| Less: exempt / out-of-scope sales (ON + SK + custom dev exempt) | $(170,000) |
| **Net MB taxable sales** | **$100,000** ($80k SaaS MB + $15k off-the-shelf + $5k telecom) |
| RST collected (7% × $100,000) | $7,000 |
| Self-assessed RST on imports | $560 |
| **Total RST payable** | **$7,560** |
| Less: vendor commission (capped; assume $58 entitled if filing on time) | $(58) |
| **Net remittance** | **$7,502** |

**Filing** Return + payment due **20 April 2025** via TAXcess. File even if NIL. Reconcile gross sales ($270,000) to the GST/HST return filed with CRA for the same period — gross figures must agree.

**Documentation to retain** Invoices showing GST and RST separately for the MB taxable streams. Engagement letters / development contracts evidencing the bespoke nature of the $40,000 custom development (to support the exemption on audit). Out-of-province delivery / customer-location evidence for the $120,000 ON and $10,000 SK sales (IP logs, billing address, signed delivery certificates). Workpaper showing the self-assessment computation for the cloud hosting.

## 10. Conservative defaults

- **Conservative default rules** — When preparing an MB RST return, default to the more cautious treatment whenever facts are ambiguous: 1. **Customer location uncertain** → treat as MB and tax at 7%. Document the basis; refund mechanism exists if later substantiated as out-of-province. 2. **Service category uncertain** (e.g., is it custom software or off-the-shelf?) → treat as taxable. The exemption is the carve-out; the default rule is taxability for the specified service categories. 3. **Bundled supplies** with a taxable element ≥10% of value → tax the entire bundle unless apportionment is clearly supportable (and if it isn't, escalate per **R-MB-6**). 4. **Self-assessment on imports** → when in doubt, self-assess. Under-assessment penalties exceed the cost of capital on a slight over-remittance. 5. **Exemption certificates** → do not accept verbal claims. Require the purchaser's RST number or a signed exemption certificate retained for **6 years** (statutory retention period under the Act). 6. **Filing NIL returns** → file even when no tax was collected. Missed NIL returns trigger non-filer penalties. 7. **Reconciliation to GST/HST** → always reconcile gross taxable sales between the federal and provincial returns before filing. Discrepancies are the #1 audit trigger. 8. **Vendor commission** → only claim if return AND remittance are on time. Late filings forfeit the commission and add penalty. 9. **Marketplace facilitators** → if the client sells through a marketplace, confirm whether the marketplace is collecting RST on the client's behalf. Double-collection or double-non-collection are both common errors post-2021. 10. **Out-of-province sellers** approaching the $10,000 threshold → register before crossing it; back-registration with collected-but-unremitted tax is materially worse than proactive registration.  _(Retail Sales Tax Act — statutory retention period)_

## 11. Sources

**The Retail Sales Tax Act**, C.C.S.M. c. R130 — primary statute. **The Retail Sales Tax Regulation**, Man. Reg. 75/88 R. **Manitoba Finance — Taxation Division**, RST information bulletins, including: Bulletin No. 005 — Information for Contractors (Real Property); Bulletin No. 027 — Children's Clothing and Footwear; Bulletin No. 030 — Manufacturing Production Equipment; Bulletin No. 047 — Sales to First Nations and First Nations Persons; Bulletin No. 057 — Computer Software (custom vs off-the-shelf); Bulletin No. 064 — Specified Services (legal, accounting, security). **TAXcess online portal** — `https://taxcess.gov.mb.ca/` — registration, filing, and payment. **Budget 2021 (Manitoba)** — economic nexus / marketplace facilitator amendments effective 1 December 2021. **Manitoba Finance Notices** issued periodically for rate, base, and procedural changes — always check for notices issued after this skill's tax year (2025) before filing.

## Skill version footer

*Skill version 1.0 — tax year 2025. Verification pending (Canadian provincial sales tax specialist). Federal GST/HST handled by the CRA / `ca-gst-hst` skill; this skill covers Manitoba RST only.*

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
