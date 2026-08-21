---
name: singapore-formation
description: Use this skill whenever asked about forming, incorporating, or registering a company in Singapore. Trigger on phrases like "set up a company in Singapore", "Pte Ltd", "ACRA registration", "Singapore company formation", "register a business Singapore", "BizFile+", "Singapore incorporation", "company secretary Singapore", "resident director Singapore", "Employment Pass", or any question about starting a business entity in Singapore. Covers entity types (Pte Ltd, LLP, sole proprietorship), registration process, capital requirements, costs, post-formation compliance, and bank account opening. ALWAYS read this skill before advising on Singapore company formation.
version: 1.0
jurisdiction: SG
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - company-formation-workflow-base
category: formation
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Singapore Formation

## Section 1 -- Quick Reference

**Section 1 -- Quick Reference**

| Field | Value |
| --- | --- |
| Country | Singapore (Republic of Singapore) |
| Currency | SGD |
| Company registrar | Accounting and Corporate Regulatory Authority (ACRA) -- acra.gov.sg |
| Key legislation | Companies Act 1967; Business Registration Act |
| Typical formation time | 1--2 business days (Singaporean/PR founders); 3--5 days (foreign founders) |
| Corporate tax rate | 17% (headline); effective ~8.5% on first S$200,000 for new companies (partial tax exemption) |
| Skill version | 1.0 |

## Section 2 -- Entity Types Comparison

**Section 2 -- Entity Types Comparison**

| Feature | Sole Proprietorship | Partnership / LLP | Private Limited (Pte Ltd) | Public Company (Ltd) |
| --- | --- | --- | --- | --- |
| Legal personality | No | Partnership: No / LLP: Yes | Yes | Yes |
| Liability | Unlimited | Partnership: Unlimited / LLP: Limited | Limited | Limited |
| Min. founders | 1 | 2 (Partnership/LLP) | 1 shareholder + 1 director | 1+ (no max) |
| Max. shareholders | 1 | 20 (Partnership); unlimited (LLP) | 50 | Unlimited |
| Min. share capital | N/A | N/A | S$1 | S$1 |
| Tax treatment | Personal income tax | Partners taxed individually / LLP partners taxed individually | Corporate (17%) | Corporate (17%) |
| Foreign ownership | 100% allowed | 100% allowed | 100% allowed | 100% allowed |
| Admin burden | Very low | Low | Medium | High |

**Recommended default:** Private Limited Company (Pte Ltd) for credibility, limited liability, tax incentives, and foreign ownership flexibility.

## Section 3 -- Registration Process

### Step 1: Reserve Company Name

- **Reserve company name process** — Apply via ACRA's BizFile+ portal (bizfile.gov.sg). Fee: S$15. Name reserved for 120 days (renewable for 60 days at S$10). Must be unique and not offensive or identical/similar to existing names. Certain names (bank, finance, law, school) require referral to relevant authority.  _(ACRA BizFile+)_

### Step 2: Prepare Incorporation Documents

- **Prepare incorporation documents** — Company constitution (replaces Memorandum & Articles since 2014). Can adopt ACRA's Model Constitution or draft a custom one. Details: company name, registered office, share capital, directors, shareholders, secretary provisions.  _(ACRA)_

### Step 3: Appoint Key Officers

- **Appoint key officers** — At least 1 director who is ordinarily resident in Singapore (Singapore citizen, PR, or qualifying pass holder). Company secretary must be appointed within 6 months of incorporation (must be Singapore-resident). Sole director cannot also be sole secretary.  _(ACRA)_

### Step 4: File Incorporation via BizFile+

- **File incorporation via BizFile+** — Upload: constitution, officer details, shareholder details, registered office address. All directors and shareholders must provide identity verification via Singpass (Singaporeans/PRs) or passport (foreigners). Fee: S$300 (incorporation). Total ACRA fees: S$315 (S$15 name + S$300 registration).  _(ACRA BizFile+)_

### Step 5: Receive Certificate of Incorporation

- **Receive Certificate of Incorporation** — Issued electronically via BizFile+. Includes Unique Entity Number (UEN). Company legally exists from date of incorporation.  _(ACRA)_

### Step 6: Post-Incorporation Registrations

- **Post-incorporation registrations** — IRAS (Inland Revenue Authority of Singapore): corporate tax registration is automatic upon incorporation. GST registration: mandatory if taxable turnover exceeds S$1M; voluntary registration permitted below threshold. CPF (Central Provident Fund): register as employer if hiring Singapore citizens/PRs. Employment Pass: apply via MOM if foreign directors/employees need to work in Singapore.  _(IRAS; CPF Board; MOM)_

## Section 4 -- Capital Requirements

**Section 4 -- Capital Requirements**

| Entity Type | Min. Share Capital | Min. Paid-Up | Payment Timing | In-Kind Contributions |
| --- | --- | --- | --- | --- |
| Pte Ltd | S$1 | S$1 | At or after incorporation | Not common; shares can be issued for non-cash consideration with proper valuation |
| Public Ltd | S$1 | S$1 | At or after incorporation | Permitted |
| LLP | N/A | N/A | Per LLP agreement | N/A |

**Practical capital:** While S$1 is the legal minimum, Employment Pass applicants are advised to have S$50,000+ in paid-up capital to demonstrate business viability. Banks also prefer higher capital for account opening.

## Section 5 -- Costs Breakdown

**Section 5 -- Costs Breakdown**

| Cost Component | Amount (SGD) | Notes |
| --- | --- | --- |
| ACRA name application | S$15 | Via BizFile+ |
| ACRA registration fee | S$300 | One-time |
| **Total ACRA fees** | **S$315** | Mandatory government fees |
| Corporate secretary (first year) | S$300--S$900 | Mandatory appointment within 6 months |
| Registered office address (if using service) | S$200--S$500/year | Must be a physical Singapore address |
| Nominee resident director (if needed) | S$1,500--S$4,000/year | For fully foreign-owned companies |
| Accounting and tax filing (first year) | S$800--S$2,500 | Depends on transaction volume |
| **Total first year (foreign-owned, with nominee)** | **S$3,100--S$8,200** |  |
| **Total first year (local founder)** | **S$1,400--S$3,700** |  |

### Annual Maintenance

**Annual Maintenance**

| Item | Cost (SGD) |
| --- | --- |
| ACRA annual return filing fee | S$60 |
| Corporate secretary | S$300--S$900/year |
| Registered office (if service) | S$200--S$500/year |
| Accounting and tax filing | S$800--S$2,500/year |
| Audit (if required) | S$2,000--S$8,000/year |
| Nominee director (if needed) | S$1,500--S$4,000/year |

## Section 6 -- Post-Formation Compliance

**Section 6 -- Post-Formation Compliance**

| Obligation | Deadline | Authority |
| --- | --- | --- |
| Annual return (AR) | Within 30 days of AGM | ACRA |
| AGM | Within 6 months of financial year-end (18 months for first AGM) | Internal |
| Estimated Chargeable Income (ECI) | Within 3 months of financial year-end | IRAS |
| Corporate tax return (Form C/C-S) | 30 November of following year | IRAS |
| GST returns (if registered) | Quarterly | IRAS |
| CPF contributions | Monthly (by 14th of following month) | CPF Board |
| Financial statements | Prepare annually; file with AR | ACRA (via XBRL for larger companies) |
| Company secretary appointment | Continuously maintained | ACRA |
| Register of members, directors, secretaries | Maintain at registered office | Internal |

### Audit Exemption (Small Company Exemption)

- **Audit exemption criteria** — A private company is exempt from statutory audit if it meets at least 2 of 3 criteria for the immediate past 2 financial years: Total annual revenue ≤ S$10M; Total assets ≤ S$10M; Number of employees ≤ 50.  _(Small Company Exemption)_

## Section 7 -- Bank Account Opening

### Documents Typically Required

ACRA BizFile profile (company details); Certificate of Incorporation; Company constitution; Board resolution for account opening; ID (passport / NRIC) for all directors and shareholders (25%+); Proof of residential address for all UBOs; Business plan or description of activities; Source of funds documentation.

### Typical Timeline

1--3 days (Singapore-resident directors with clear KYC); 1--4 weeks (foreign directors, enhanced due diligence).

### Common Banks

DBS, OCBC, UOB (local Big 3); HSBC Singapore, Standard Chartered, Citibank (international); Aspire, Airwallex (digital/fintech).

## Section 8 -- Foreign Founder Considerations

**Section 8 -- Foreign Founder Considerations**

| Question | Answer |
| --- | --- |
| Non-resident directors allowed? | Yes, but at least 1 director must be ordinarily resident in Singapore (citizen, PR, or EP/S Pass holder) |
| 100% foreign ownership? | Yes, permitted in virtually all sectors |
| Nominee director service | Available; recommended for fully foreign-owned companies without an EP holder |
| Employment Pass (EP) requirement | Foreign individuals working in Singapore must hold an EP; minimum salary S$5,600/month (S$6,200 for financial services) in 2026 |
| Physical presence required? | Not for incorporation (BizFile+ accepts remote filing); required for EP application |
| Apostille requirements | Foreign documents may need notarisation; Singapore is a Hague Convention member |
| Registered office | Must be a physical address in Singapore; residential address acceptable if permitted by URA zoning |
| Tax incentives for startups | 75% exemption on first S$100,000 + 50% on next S$100,000 of chargeable income for first 3 years (conditions apply) |

## Section 9 -- Common Mistakes and Refusals

- **R-SG-F1 -- No resident director** — At least one director must be ordinarily resident in Singapore. A Pte Ltd cannot be incorporated without this. If no founder qualifies, a nominee director service must be engaged.  _(R-SG-F1)_
- **R-SG-F2 -- Forgetting company secretary** — A company secretary must be appointed within 6 months of incorporation. The sole director cannot also serve as sole secretary. Failure to appoint results in ACRA penalties and potential strike-off.  _(R-SG-F2)_
- **R-SG-F3 -- S$1 capital and EP application** — While S$1 is the legal minimum capital, the Ministry of Manpower (MOM) evaluates EP applications based on company viability. Very low capital signals insufficient substance. Recommend S$50,000+ paid-up capital for EP-linked companies.  _(R-SG-F3)_
- **R-SG-F4 -- Shell company without substance** — Singapore takes anti-money-laundering seriously. ACRA and MAS (Monetary Authority of Singapore) actively scrutinise companies without genuine business activity. This skill will not assist in forming a company intended solely as a conduit without real operations.  _(R-SG-F4)_
- **R-SG-F5 -- Missing ECI filing** — ECI must be filed within 3 months of financial year-end, even if estimated income is nil. Failure to file triggers IRAS penalties and a Notice of Assessment based on IRAS's own estimate.  _(R-SG-F5)_
- **R-SG-F6 -- Operating without EP** — Foreign individuals performing work in Singapore (including as company directors managing day-to-day operations) without a valid work pass violate the Employment of Foreign Manpower Act, which carries criminal penalties.  _(R-SG-F6)_

## Section 10 -- Timeline

**Section 10 -- Timeline**

| Step | Duration | Cumulative |
| --- | --- | --- |
| Reserve company name (BizFile+) | 1 day (often instant) | Day 1 |
| Prepare constitution and officer details | 1--3 days | Day 2--4 |
| File incorporation (BizFile+) | 1 day | Day 3--5 |
| ACRA processes incorporation | 1--2 days (straightforward) | Day 4--7 |
| Certificate of Incorporation received | Same day as approval | Day 4--7 |
| Open corporate bank account | 1--3 days (resident) / 1--4 weeks (non-resident) | Day 5--35 |
| IRAS corporate tax file number (automatic) | 1--2 weeks | Day 11--21 |
| Apply for EP (if needed) | 3--8 weeks | Day 7--63 |
| Appoint company secretary | Within 6 months | Day 1--180 |
| **Ready to trade** |  | **As fast as 1 week (Singapore-resident founder)** |

Singapore consistently ranks among the fastest and most efficient jurisdictions globally for company incorporation.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute legal, tax, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your jurisdiction — **no liability on either side until you and the accountant sign a formal engagement letter** — book a free 30-minute call:

**→ [Book a call](https://calendly.com/openaccountants-info/30min)**

We'll route you to the named verifier covering your country or state. You can also see the full list of verified accountants at [openaccountants.com/network](https://openaccountants.com/network).

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
