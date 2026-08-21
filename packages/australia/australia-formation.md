---
name: australia-formation
description: Use this skill whenever asked about forming, incorporating, or registering a company in Australia. Trigger on phrases like "set up a company in Australia", "Pty Ltd", "ASIC registration", "Australian company formation", "register a business Australia", "ABN", "ACN", "proprietary limited", "sole trader Australia", "partnership Australia", or any question about starting a business entity in Australia. Covers entity types (Pty Ltd, Ltd, sole trader, partnership, trust), registration process, costs, post-formation compliance, and bank account opening. ALWAYS read this skill before advising on Australian company formation.
version: 1.0
jurisdiction: AU
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on: - company-formation-workflow-base
category: formation
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Australia Formation

## Australia Company Formation Skill v1.0

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Australia (Commonwealth of Australia) |
| Currency | AUD |
| Company registrar | Australian Securities and Investments Commission (ASIC) -- asic.gov.au |
| Key legislation | Corporations Act 2001 (Cth) |
| Typical formation time | 1--3 business days (online via BRS) |
| Corporate tax rate | 25% (base rate entities, turnover < $50M); 30% (all others) |
| Skill version | 1.0 |

## Section 2 -- Entity Types Comparison

**Entity Types Comparison**

| Feature | Sole Trader | Partnership | Pty Ltd (Proprietary) | Public Company (Ltd) | Trust (with corporate trustee) |
| --- | --- | --- | --- | --- | --- |
| Legal personality | No | No | Yes | Yes | No (trustee is legal person) |
| Liability | Unlimited | Unlimited (joint and several) | Limited to share capital | Limited | Trustee liability (limited if Pty Ltd trustee) |
| Min. founders | 1 | 2 | 1 shareholder + 1 director | 1 shareholder + 3 directors + 1 secretary | 1 settlor + 1 trustee |
| Min. share capital | N/A | N/A | No minimum (commonly $1) | No minimum | N/A |
| Max. shareholders | 1 | N/A | 50 (non-employee) | Unlimited | N/A |
| Tax treatment | Personal income tax | Partners taxed individually | Company tax rate | Company tax rate | Trust distributions taxed in beneficiaries' hands |
| Admin burden | Very low | Low | Medium | High | Medium--High |
| ASIC registration | No | No (ABN only) | Yes ($611) | Yes | Only if trustee is a company |
| Audit required | No | No | Only if large proprietary | Yes | No (unless regulated) |

**Recommended default:** Proprietary company limited by shares (Pty Ltd) for most commercial purposes.

## Section 3 -- Registration Process

### Step 1: Choose Company Name

- **Choose Company Name** — Check availability on ASIC's company name check tool; Must include "Pty Ltd" or "Proprietary Limited"; Can reserve name for 2 months ($62 fee) or register directly; Identical or near-identical names will be rejected

### Step 2: Obtain Consent from Officeholders

- **Obtain Consent from Officeholders** — All proposed directors and secretaries must consent in writing before registration; At least 1 director must ordinarily reside in Australia (for Pty Ltd)

### Step 3: Prepare Company Details

- **Prepare Company Details** — Registered office address (must be in Australia; can be accountant's or agent's office); Principal place of business; Share structure (number and class of shares, rights); Details of shareholders, directors, secretary (if any)

### Step 4: Register via Business Registration Service (BRS)

- **Register via BRS** — Go to register.business.gov.au; Can simultaneously apply for: company registration, ABN, TFN, GST, PAYG withholding; Fee: $611 (Pty Ltd, 2025--26 financial year); ASIC processes and issues ACN (Australian Company Number) typically within 1--3 days

### Step 5: Receive Certificate of Registration

- **Receive Certificate of Registration** — Certificate confirms ACN, company name, date of registration, type; Company legally exists from date on certificate

### Step 6: Apply for ABN (Australian Business Number)

- **Apply for ABN** — Free via Australian Business Register (ABR); Required for tax invoices, GST, and dealing with other businesses; Can be applied for during BRS registration

### Step 7: Register for GST (if applicable)

- **GST registration threshold** — $75,000 (or will be); $150,000 for non-profits AUD (Mandatory if annual turnover is or will be at threshold; voluntary registration permitted below threshold)

### Step 8: Register for PAYG Withholding (if employing)

- **Register for PAYG Withholding** — Required before paying employees or directors; Register via BRS or ATO

## Section 4 -- Capital Requirements

**Capital Requirements**

| Entity Type | Min. Share Capital | Min. Paid-Up | Payment Timing | In-Kind Contributions |
| --- | --- | --- | --- | --- |
| Pty Ltd | No statutory minimum ($1 common) | No minimum | As specified in share terms | Permitted (no independent valuation required for proprietary companies) |
| Public Ltd | No statutory minimum | No minimum | As specified | Permitted (expert's report required for non-cash consideration over threshold) |

- **No minimum capital requirement** — Australia has no minimum capital requirements for company formation.

## Section 5 -- Costs Breakdown

**Costs Breakdown**

| Cost Component | Amount (AUD) | Notes |
| --- | --- | --- |
| ASIC company registration | $611 | One-time (Pty Ltd, 2025--26) |
| Name reservation (optional) | $62 | Valid 2 months |
| Business name registration (if different from company name) | $45/year or $104/3 years | Only if trading under a different name |
| ABN registration | Free | Via ABR |
| GST registration | Free | Via ATO |
| ASIC annual review fee | $329/year | Pty Ltd (2025--26) |
| **Total initial cost (government)** | **$611--$673** | Excluding professional fees |
| Legal / accountant setup fees | $500--$2,000 | Constitution, shareholder agreement, tax setup |
| **Total with professional help** | **$1,100--$2,700** |  |

### Annual Maintenance

**Annual Maintenance**

| Item | Cost (AUD) |
| --- | --- |
| ASIC annual review fee | $329 |
| Accountant / tax agent fees | $1,500--$5,000/year |
| Business name renewal (if applicable) | $45/year |
| Registered office service (if using) | $200--$600/year |
| ASIC late fees | $98 (≤1 month) / $411 (>1 month) |

## Section 6 -- Post-Formation Compliance

**Post-Formation Compliance**

| Obligation | Deadline | Authority |
| --- | --- | --- |
| ASIC annual review | Annual (on registration anniversary) | ASIC |
| Company tax return | Due date varies (usually by 15 May via tax agent for 30 June year-end) | ATO |
| BAS (Business Activity Statement) | Quarterly or monthly (GST, PAYG, instalment) | ATO |
| PAYG summaries / STP finalisation | 14 July following the financial year | ATO |
| Superannuation guarantee | Quarterly (28 days after quarter end) | Super fund / ATO |
| Change notifications to ASIC | Within 28 days of change | ASIC |
| Financial records | Maintain for 7 years | Internal |
| Directors' duties | Ongoing (s180--184 Corporations Act) | ASIC |

## Section 7 -- Bank Account Opening

### Documents Typically Required

- **Documents Typically Required** — Certificate of registration (ACN); Company constitution or replaceable rules; ABN confirmation; ID (passport / driver's licence) for all directors; Proof of address for directors and shareholders

### Typical Timeline

- **Typical Timeline** — 1--3 days (Big 4 banks and digital banks for Australian residents); 1--3 weeks (non-resident directors, enhanced KYC)

### Common Banks

Commonwealth Bank (CBA), Westpac, ANZ, NAB (Big 4); Macquarie, Bendigo (mid-tier); Airwallex, Wise Business (digital/international)

## Section 8 -- Foreign Founder Considerations

**Foreign Founder Considerations**

| Question | Answer |
| --- | --- |
| Non-resident directors allowed? | Yes, but at least 1 director must ordinarily reside in Australia |
| Resident director requirement | At least 1 (for Pty Ltd); at least 2 of 3 for public companies |
| Nominee directors | Permitted (ASIC register shows actual director names) |
| Physical presence required? | No (online registration); resident director must be genuinely resident |
| Foreign ownership restrictions | Foreign Investment Review Board (FIRB) approval may be required for certain sectors and thresholds |
| ABN for foreign entities | Foreign companies can register an ARBN ($506) and apply for ABN |
| Tax treaty benefits | Australia has extensive DTA network; check withholding rates |

## Section 9 -- Common Mistakes and Refusals

- **R-AU-F1 -- No Australian-resident director** — Every Pty Ltd must have at least one director who ordinarily resides in Australia. A company cannot be registered without this. Advise the client to appoint a local director or use a resident director service (with proper governance).  _(R-AU-F1)_
- **R-AU-F2 -- Failing to pay ASIC annual review fee** — ASIC charges $329/year. If the annual review is not completed and fee is not paid, ASIC will deregister the company. Late fees apply: $98 within 1 month, $411 after 1 month.  _(R-AU-F2)_
- **R-AU-F3 -- GST threshold ignorance** — If annual turnover reaches $75,000, GST registration is mandatory. Failing to register when required results in penalties and backdated GST assessments.  _(R-AU-F3)_
- **R-AU-F4 -- Superannuation non-compliance** — Employers must pay at least 11.5% (2025--26) superannuation guarantee on top of ordinary time earnings. Non-payment results in the Superannuation Guarantee Charge (SGC), which is not tax-deductible.  _(R-AU-F4)_
- **R-AU-F5 -- Shell company without substance** — This skill will not assist in forming a company with no genuine business activity in Australia. ASIC and the ATO actively pursue sham structures.  _(R-AU-F5)_

## Section 10 -- Timeline

**Timeline**

| Step | Duration | Cumulative |
| --- | --- | --- |
| Prepare documents and officer consents | 1--2 days | Day 1--2 |
| Register via BRS (ABN + company + GST) | 1 day | Day 2--3 |
| ASIC issues ACN and certificate | 1--3 days | Day 3--6 |
| Open business bank account | 1--3 days (resident) / 1--3 weeks (non-resident) | Day 4--27 |
| ATO registrations confirmed | 1--28 days | Day 4--34 |
| **Ready to trade** |  | **As fast as 3--5 days (Australian-resident founders)** |

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute legal, tax, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).

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
