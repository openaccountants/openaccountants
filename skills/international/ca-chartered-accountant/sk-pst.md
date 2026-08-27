---
name: sk-pst
description: Use this skill for Saskatchewan Provincial Sales Tax — 6% non-harmonized sales tax. Triggers "Saskatchewan PST", "SK PST 6%", "SETS Saskatchewan", "Saskatchewan eTaxBC equivalent", "SK PST online sales".
jurisdiction: CA
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# SK PST

## Saskatchewan — Provincial Sales Tax (PST) — Skill v1.0

## 1. Quick reference

**Quick reference table**

| Item | Value |
| --- | --- |
| Standard PST rate | **6%** |
| Liquor consumption tax | 10% |
| Tobacco tax | Specific per-unit rates (not ad valorem) |
| Passenger vehicle PST | 6% (with valuation rules for used vehicles) |
| Registration threshold | **None** — any business making taxable retail sales in SK must register |
| Federal GST also applies | Yes — 5% GST + 6% PST = effective 11% on most taxable supplies |
| Administering body | Saskatchewan Ministry of Finance, Revenue Division |
| Filing portal | **SETS** — Saskatchewan eTax Services |
| Legal basis | *The Provincial Sales Tax Act* (Saskatchewan), and regulations thereunder |

Saskatchewan is a **non-harmonized** PST jurisdiction (alongside BC and Manitoba). It is **not** part of the HST system. PST stacks on top of GST and is calculated on the GST-exclusive price of the supply.

## 2. Required inputs + refusal catalogue

### Required inputs

Before preparing or advising on a SK PST return / position, collect:

1. **Vendor permit number** (PST account number issued by SK Ministry of Finance).
2. **Filing frequency** (monthly / quarterly / annually) as assigned at registration.
3. **Reporting period** (start and end dates).
4. **Gross sales** for the period, broken down by:
   - Taxable tangible personal property (TPP) sold to SK customers
   - Taxable services rendered in SK (lawn care, telecom, accommodation, legal/accounting, computer services, etc.)
   - Insurance contracts subject to PST
   - Exempt sales (groceries, prescription drugs, children's clothing, agricultural inputs, residential rent)
   - Out-of-province sales (no SK PST — but watch for nexus into BC/MB/QC)
5. **PST collected** during the period.
6. **PST self-assessed** on taxable goods/services purchased without PST charged (e.g., out-of-province purchases for own use in SK).
7. **Commission** entitlement (vendors may retain a small collection commission — confirm current rate via SETS portal).
8. **Bad debt write-offs** for which PST was previously remitted.
9. **Refunds / credits** to customers during the period.

### Refusal catalogue (route elsewhere)

- **R-SK-1** — Quebec QST or any other provincial sales tax (route to `qc-qst`, `bc-pst`, `mb-rst`).  _(R-SK-1)_
- **R-SK-2** — Federal GST/HST mechanics (route to `canada-gst-hst`).  _(R-SK-2)_
- **R-SK-3** — Liquor, tobacco, fuel, cannabis-specific commodity taxes (route to dedicated commodity-tax skills; this skill mentions liquor 10% only for rate awareness).  _(R-SK-3)_
- **R-SK-4** — Real-property transactions (PST does not apply to real property itself; PST applies to **services** to real property such as construction materials and certain contractor services — handle with care and route complex construction contract questions to a credentialed SK practitioner).  _(R-SK-4)_
- **R-SK-5** — Indigenous tax exemptions on reserve land — fact-specific, route to a credentialed practitioner.  _(R-SK-5)_
- **R-SK-6** — Insurance premium tax (a separate tax administered by Finance — not the PST on insurance contracts; do not conflate).  _(R-SK-6)_
- **R-SK-7** — Audit defence, voluntary disclosure, ruling requests — these require credentialed reviewer signoff.  _(R-SK-7)_
- **R-SK-8** — Pre-2017 reporting periods — rules expanded materially in 2017 and again 2018–2022; this skill is scoped to current law for 2025.  _(R-SK-8)_

## 3. Rate

**Rate table**

| Category | Rate | Notes |
| --- | --- | --- |
| **Standard PST** | 6% | Applies to taxable TPP, listed services, and insurance contracts |
| **Liquor consumption tax** | 10% | Replaced the previous 10% Liquor Consumption Tax structure; applied in lieu of standard PST on beverage alcohol |
| **Tobacco tax** | Specific (per cigarette / per gram) | Not ad valorem; refer to current Ministry rate schedule |
| **Passenger vehicles** | 6% | Used vehicles have valuation rules (greater of purchase price or Red Book / Black Book value, subject to thresholds) |

- **PST base and combined burden** — PST applies on the GST-exclusive consideration. Effective combined burden on a typical taxable supply: 5% GST + 6% PST = 11%.

## 4. Registration

### Who must register

- **Who must register** — A person must hold a Vendor's Licence (PST registration) if they: Regularly make retail sales of taxable goods or services in Saskatchewan, OR Are an out-of-province seller meeting the economic nexus tests (see §6), OR Operate as a contractor consuming taxable goods in SK, OR Provide taxable services in SK (lawn care, computer services, accommodation, legal, accounting, etc.).
- **Registration threshold** — None CAD (Unlike the federal GST $30,000 small-supplier threshold, SK PST registration is required from the first dollar of taxable sales in SK.)

### How to register

- **How to register** — Register via the SETS portal (Saskatchewan eTax Services) at sets.saskatchewan.ca. A vendor permit number is issued; this must appear on invoices where PST is charged.

### Casual / one-off sellers

- **Casual sellers** — A taxpayer who makes only a single isolated sale (e.g., private sale of a used personal item) generally is not required to register. The buyer may, however, owe PST self-assessed on the purchase (e.g., used-vehicle PST collected at registration with SGI).

## 5. Taxable supplies

Saskatchewan's PST base is broader than BC's or Manitoba's following the 2017 and 2018–2022 expansions.

### Taxable

- **Taxable items list** — Tangible personal property sold for consumption in SK (default rule — all TPP is taxable unless specifically exempt). Listed taxable services, including (non-exhaustive): Lawn care, snow removal, landscaping; Telecommunication services (including streaming and digital subscriptions — expanded 2022); Accommodation (hotels, short-term rentals); Legal services; Accounting and bookkeeping services; Computer services and software (including SaaS — expanded 2017); Engineering, architectural, and surveying services; Repair and installation services to TPP and to certain real property; Veterinary services for non-livestock animals; Dry cleaning and laundry; Credit reporting and collection services. Insurance contracts (most general insurance — life and health insurance are excluded; agricultural insurance and certain specified contracts have exemptions). Admissions to places of amusement (where applicable).

### Self-assessment

- **Self-assessment rule** — Where a SK resident or business purchases taxable goods or services from an out-of-province vendor that did not charge SK PST, the purchaser must self-assess and remit PST on its next return.

## 6. Online platforms / out-of-province sellers

Saskatchewan has had economic nexus rules since 2018, expanded materially in 2020.

### Who is caught

- **Who is caught** — Electronic distribution platforms (marketplaces) facilitating sales to SK customers. Online accommodation platforms (e.g., short-term rental marketplaces). Out-of-province sellers of TPP or taxable services to SK customers where the seller makes retail sales for consumption in SK.

### Threshold

- **Nexus threshold** — None — no dollar safe harbour CAD (The test is whether the seller is causing taxable goods/services to enter SK for consumption. A pattern of regular sales triggers the duty to register and collect.)

### Practical implication

- **Practical implication** — A non-Canadian or non-SK e-commerce seller shipping into SK should register for a SK Vendor's Licence as soon as it is clear sales into SK are regular. Marketplace facilitators are generally responsible for collecting PST on third-party seller transactions on their platform.

## 7. Exemptions

- **PST does not apply to** — Basic groceries (aligned conceptually with the GST zero-rating list, but defined under SK law). Prescription drugs and many medical devices. Children's clothing and footwear (subject to size / specification rules). Agricultural inputs — most farm machinery, fertilizer, seed, feed for livestock, and qualifying farm-use goods. Used goods sold privately between individuals (not in the course of business) — but PST may be self-assessed at registration (e.g., used vehicles via SGI). Residential rent and most residential real property transactions. Books (printed books with an ISBN — subject to current rules). Direct agents consumed in manufacturing (incorporated into the final product). Goods purchased for resale by a registered vendor providing a valid PST number to the supplier. Goods shipped out of province by the seller to a non-SK destination.
- **Exemption certificate requirement** — Exemption certificates / declarations must generally be obtained and retained for vendors not charging PST on exempt sales.

## 8. Filing

### Portal

- **Portal** — SETS — Saskatchewan eTax Services (sets.saskatchewan.ca). All registered vendors must file electronically via SETS unless granted an exemption.

### Frequency

**Filing frequency table**

| Annual PST collected | Filing frequency |
| --- | --- |
| > $7,200 / year (approx.) | Monthly |
| $1,200 – $7,200 / year (approx.) | Quarterly |
| < $1,200 / year (approx.) | Annually |

*Confirm current thresholds on SETS — the Ministry adjusts these from time to time.*

### Due dates

- **Due dates** — Returns and payment are due by the 20th day of the month following the reporting period end.

### Vendor commission

- **Vendor commission** — Vendors that file and pay on time may retain a small commission (a percentage of PST collected, capped per return). Verify the current commission rate and cap on the SETS portal as part of any return preparation.

### Penalties

- **Penalties** — Late filing and late payment attract penalties and interest. Persistent non-compliance can result in licence revocation and director liability for unremitted PST.

## 9. Coordination with federal GST

- **Non-harmonized coordination** — Saskatchewan is non-harmonized: 5% federal GST and 6% provincial PST apply separately and are both calculated on the GST-exclusive sale price.

### Worked rate example

- **Worked rate example** — Sale price (PST/GST exclusive): $100.00 - GST 5%: $5.00 - PST 6%: $6.00 - Total to customer: $111.00 Note: SK PST is not calculated on top of GST (no tax-on-tax). The two taxes are parallel, both applied to the base price.

### Input tax credits / refunds

- **ITC comparison** — GST: Registered businesses recover input GST via ITCs on the GST34 federal return. PST: There is no general input tax credit mechanism. PST is a true retail sales tax — businesses generally pay PST on their inputs as a final cost, except where a specific exemption applies (resale, direct agents in manufacturing, qualifying farm inputs, etc.).

This is a major contrast with GST/HST and is the single most common error among first-time SK PST advisors: do not assume PST paid on business inputs is recoverable. It generally is not.

## 10. Worked example — Regina e-commerce with SK + national customers

Prairie Threads Inc., a Regina-based online clothing retailer, in Q2 2025:

- Sells children's clothing $40,000 (national mix) — assume $5,000 to SK customers, $35,000 elsewhere in Canada.
- Sells adult clothing $60,000 — assume $10,000 to SK customers, $50,000 elsewhere in Canada.
- Sells SaaS subscriptions to an inventory-tracking app $20,000 — assume $3,000 to SK customers, $17,000 elsewhere (mostly AB).
- Purchases $2,000 of office supplies from an Alberta vendor with no PST charged.
- Purchases $4,000 of packaging materials from a SK wholesaler — packaging is consumed in the business (not resold separately).

**SK PST analysis table**

| Item | Amount | Taxable in SK? | PST collected |
| --- | --- | --- | --- |
| Children's clothing to SK customers | $5,000 | **Exempt** (children's clothing exemption) | $0 |
| Children's clothing to non-SK customers | $35,000 | Out of province — no SK PST | $0 |
| Adult clothing to SK customers | $10,000 | Taxable @ 6% | **$600** |
| Adult clothing to non-SK customers | $50,000 | Out of province — no SK PST (check destination PST) | $0 |
| SaaS to SK customers | $3,000 | Taxable @ 6% (computer services / telecom services expansion) | **$180** |
| SaaS to non-SK customers | $17,000 | Out of province — no SK PST | $0 |

**Self-assessment.** Alberta office supplies $2,000 purchased without PST and consumed in SK → self-assess **$120** SK PST.

**Inputs not recoverable.** The $4,000 packaging materials purchased from the SK wholesaler — PST of $240 was charged at the till. **No ITC mechanism** — this is a final cost (unless the packaging is incorporated into and sold with the product, in which case the "direct agent" / packaging exemption may apply; check current Ministry guidance and obtain a resale declaration).

**Q2 return summary (PST only)**

| Line | Amount |
| --- | --- |
| PST collected on sales | $780 |
| PST self-assessed | $120 |
| **Total PST payable** | **$900** |
| Less: vendor commission (if eligible) | (small amount per SETS schedule) |
| Net remittance | ~$900 |

**Federal GST.** Separately, Prairie Threads files a GST34 reporting GST collected on adult clothing nationally (children's clothing is GST zero-rated), and claims ITCs on GST paid on inputs.

## 11. Conservative defaults

- **Conservative defaults list** — When the facts are unclear, default conservatively: 1. When in doubt, register. SK has no dollar threshold; any pattern of regular SK sales argues for registration. A late registration is more painful than an early one. 2. When in doubt, charge PST. The expanded services base (post-2017 / 2022) means software, telecom, accommodation, and many professional services are taxable. If you cannot find a clear exemption, default to taxable. 3. When in doubt, self-assess. Out-of-province purchases consumed in SK without PST charged → self-assess on the next return. 4. Do not assume an input credit. Unlike GST, PST paid on business inputs is generally a final cost. Only claim a resale or direct-agent exemption where you have documentation supporting it. 5. Get a fresh rate confirmation from SETS before filing — rates and thresholds (especially filing-frequency cutoffs and vendor commission) are adjusted periodically. 6. Route complex construction, real property, indigenous, and audit-defence issues to a credentialed SK practitioner (refusals R-SK-4, R-SK-5, R-SK-7). 7. Document exemption claims — retain customer declarations, PST resale numbers, and shipping documentation for at least the statutory record-retention period.

## 12. Sources

- *The Provincial Sales Tax Act*, Saskatchewan (RSS 1978, c P-34.1, as amended) — primary legislation.
- *The Provincial Sales Tax Regulations* — regulations under the PST Act.
- **Saskatchewan Ministry of Finance, Revenue Division** — administrative bulletins ("Information Bulletins") and notices, especially:
  - Bulletins on taxable services (post-2017 expansion)
  - Bulletins on electronic distribution platforms and out-of-province sellers (2018, 2020 amendments)
  - Bulletin on exemption certificates and resale documentation
- **SETS — Saskatchewan eTax Services portal**: sets.saskatchewan.ca — current filing, registration, rate schedules, vendor commission, and filing-frequency thresholds.
- *Government of Saskatchewan — Finance — Taxes — Provincial Sales Tax* policy pages.

**Verification status.** `verified_by: pending` — this skill must be reviewed and signed off by a Saskatchewan-credentialed practitioner before being relied upon for a client engagement. Conservative defaults are applied throughout, but rates, thresholds, and the scope of taxable services are subject to legislative and administrative change; always reconcile against the current SETS portal and Ministry bulletins at the time of filing.

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
