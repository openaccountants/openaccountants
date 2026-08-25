---
name: india-formation
description: Use this skill whenever asked about forming, incorporating, or registering a company in India. Trigger on phrases like "set up a company in India", "Pvt Ltd India", "private limited company India", "MCA registration", "SPICe+", "Indian company formation", "register a business India", "OPC India", "LLP India", "ROC filing", "DIN", "DSC", or any question about starting a business entity in India. Covers entity types (Pvt Ltd, OPC, LLP, public), registration process via SPICe+, capital requirements, costs, post-formation compliance, and bank account opening. ALWAYS read this skill before advising on Indian company formation.
version: 1.0
jurisdiction: IN
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: Mayur Deokar
review_status: current
depends_on:
  - company-formation-workflow-base
category: formation
tier: 1
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# India Formation

## India Company Formation Skill v1.0

## Verified rates & thresholds (accountant-reviewed)

Reviewed against the cited tax authorities by **Mayur Deokar** on 2026-06-06.
Items flagged for further clarification are tracked separately and excluded here.
This block is generated from verified `skill_facts` — edit the facts, not the prose.

### Company Formation

- **Paid-up capital** — ≤ ₹10 crore  _(Companies Act s 2(85))_
- **Turnover** — ≤ ₹100 crore  _(Companies Act s 2(85))_
- **Exemptions** — No cash flow statement, no CARO, no auditor rotation  _(Companies Act)_
- **Pvt Ltd — min directors** — 2 directors + 2 shareholders  _(Companies Act 2013)_
- **Pvt Ltd — min capital** — ₹1 lakh authorised (no statutory paid-up min)  _(Companies Act 2013)_
- **OPC — founders** — 1 + 1 nominee  _(Companies Act s 2(62))_
- **LLP — min partners** — 2 designated partners  _(LLP Act 2008)_
- **Public Ltd — paid-up** — No minimum paid-up capital requirement  _(Companies Amendment Act 2015)_
- **Resident director** — At least 1 director resident 182+ days in India  _(Companies Act s 149(3))_
- **Domestic company (new regime)** — 22% + surcharge + cess = ~25.17% effective  _(ITA s 115BAA)_
- **New manufacturing (set up after Oct 2019)** — 15% + surcharge + cess = ~17.16%  _(ITA s 115BAB)_
- **AGM deadline** — 6 months from FY-end (30 September)  _(Companies Act s 96)_
- **AOC-4 (financial statements)** — 30 days from AGM  _(Companies Act s 137)_
- **MGT-7A (annual return)** — 60 days from AGM  _(Companies Act s 92)_
- **DIR-3 KYC** — 30 September annually  _(MCA rules)_
- **Late filing penalty** — ₹100/day of delay (no cap)  _(Companies Act s 403)_
- **Small Company (s 2(85)) — Paid-up capital** — ≤ ₹10 crore  _(Companies Act s 2(85))_
- **Small Company (s 2(85)) — Turnover** — ≤ ₹100 crore  _(Companies Act s 2(85))_
- **Small Company (s 2(85)) — Exemptions** — No cash flow statement, no CARO, no auditor rotation  _(Companies Act)_

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | India (Republic of India) |
| Currency | INR |
| Company registrar | Ministry of Corporate Affairs (MCA) / Registrar of Companies (ROC) -- mca.gov.in |
| Key legislation | Companies Act, 2013; LLP Act, 2008 |
| Typical formation time | 7--15 working days (SPICe+ online) |
| Corporate tax rate | 22% + surcharge + cess (~25.17% effective, new regime); 15% for new manufacturing companies |
| Skill version | 1.0 |

## Section 2 -- Entity Types Comparison

**Entity Types Comparison**

| Feature | Sole Proprietorship | LLP (Limited Liability Partnership) | OPC (One Person Company) | Private Limited (Pvt Ltd) | Public Limited |
| --- | --- | --- | --- | --- | --- |
| Legal personality | No | Yes | Yes | Yes | Yes |
| Liability | Unlimited | Limited to contribution | Limited | Limited | Limited |
| Min. founders | 1 | 2 designated partners | 1 (+ 1 nominee) | 2 directors + 2 shareholders | 3 directors + 7 shareholders |
| Min. capital | N/A | No minimum | ₹1 lakh (authorised) | ₹1 lakh (authorised) | ₹5 lakh (paid-up) |
| Tax treatment | Personal | Partnership tax (30% flat or new regime) | Corporate | Corporate | Corporate |
| FDI (100% automatic) | N/A | Restricted sectors only | Yes (most sectors) | Yes (most sectors) | Yes |
| Admin burden | Very low | Low--Medium | Medium | High | Very High |
| Audit required | If turnover > ₹1 crore | If turnover > ₹40 lakh or contribution > ₹25 lakh | If turnover > ₹2 crore or paid-up > ₹50 lakh | Mandatory | Mandatory |

**Recommended default:** Private Limited Company (Pvt Ltd) for startups and businesses seeking funding. LLP for professional firms and partnership structures.

## Section 3 -- Registration Process

### Step 1: Obtain Digital Signature Certificate (DSC)

- **DSC requirement** — Class 3 DSC required for each proposed director; Cost: ₹1,000--₹2,000 per person; Issued by licensed Certifying Authorities (e.g., eMudhra, Sify, NSDL); Processing: 1--3 days

### Step 2: Reserve Company Name (SPICe+ Part A or RUN)

- **Name reservation process** — Apply via MCA V3 portal using RUN (Reserve Unique Name) form; Fee: ₹1,000; Can propose up to 2 names; valid for 20 days if approved; Name must include "Private Limited" at the end

### Step 3: File SPICe+ (INC-32) Form

- **SPICe+ integrated form contents** — Integrated form that handles: Incorporation application; DIN (Director Identification Number) allotment (up to 3 directors); PAN and TAN application; GST registration (optional); EPFO (Employees' Provident Fund) registration; ESIC (Employees' State Insurance) registration; Bank account opening request. Attach: MoA (INC-33), AoA (INC-34), declarations, ID/address proofs, registered office proof. Pay government fees + stamp duty online

### Step 4: MCA Processing and Certificate of Incorporation

- **MCA processing** — ROC verifies documents and approves; Certificate of Incorporation (CoI) issued with company PAN, TAN, and CIN; Typically 7--10 working days from filing

### Step 5: Open Bank Account

- **Bank account opening** — CoI triggers bank account opening (applied via AGILE-PRO-S in SPICe+); Deposit initial share capital

### Step 6: Issue Share Certificates

- **Share certificate issuance** — Must be issued within 60 days of incorporation; Maintain statutory registers

## Section 4 -- Capital Requirements

**Capital Requirements**

| Entity Type | Min. Authorised Capital | Min. Paid-Up Capital | Payment Timing | In-Kind Contributions |
| --- | --- | --- | --- | --- |
| Pvt Ltd | ₹1 lakh (commonly used) | No statutory minimum paid-up | On or after incorporation | Not permitted at incorporation via SPICe+ (cash subscription only initially) |
| OPC | ₹1 lakh | No statutory minimum paid-up | On or after incorporation | Same as Pvt Ltd |
| Public Ltd | ₹5 lakh (paid-up minimum) | ₹5 lakh | On or after incorporation | Permitted (valuation report required) |
| LLP | No minimum | No minimum | Per LLP agreement | Permitted |

**Note:** There is no statutory minimum paid-up capital for Pvt Ltd since the Companies (Amendment) Act 2015 removed the ₹1 lakh paid-up requirement. However, authorised capital of ₹1 lakh is standard practice as it determines filing fees and stamp duty.

## Section 5 -- Costs Breakdown

**Costs Breakdown**

| Cost Component | Amount (INR) | Notes |
| --- | --- | --- |
| DSC (per director, 2 directors) | ₹2,000--₹4,000 | Class 3 digital signature |
| RUN name reservation | ₹1,000 | Non-refundable |
| SPICe+ filing fee (up to ₹1 lakh authorised capital) | ₹500 | Scales with authorised capital |
| SPICe+ filing fee (₹1--₹5 lakh authorised capital) | ₹4,000 |  |
| INC-22 (registered office) | ₹400 |  |
| AGILE-PRO-S | ₹600 |  |
| Stamp duty (MoA + AoA) | ₹200--₹12,600 | Varies dramatically by state |
| PAN and TAN | ₹0 | Issued via SPICe+ |
| **Total government fees** | **₹4,700--₹18,600** | Depending on state and capital |
| Professional fees (CA/CS) | ₹3,000--₹15,000 | Optional; recommended |
| **Total all-in** | **₹7,700--₹30,000** |  |

### State Stamp Duty Variation (Select States)

**State Stamp Duty Variation (Select States)**

| State | Approximate Stamp Duty (₹1 lakh capital) |
| --- | --- |
| Maharashtra | ₹2,500--₹5,000 |
| Delhi | ₹1,000--₹2,000 |
| Karnataka | ₹5,000--₹6,000 |
| Tamil Nadu | ₹3,000--₹4,000 |
| Jammu & Kashmir | ₹100--₹200 |
| Madhya Pradesh | ₹10,000--₹12,600 |

### Annual Maintenance

**Annual Maintenance**

| Item | Cost (INR) |
| --- | --- |
| ROC annual return (MGT-7A) | ₹200--₹400 |
| Financial statements filing (AOC-4) | ₹200--₹400 |
| Income tax return | Included in accountant fees |
| Accountant / CS fees | ₹15,000--₹50,000/year |
| Statutory audit (mandatory) | ₹10,000--₹50,000/year |
| Director KYC (DIR-3 KYC) | Free (if on time); ₹5,000 (if late) |

## Section 6 -- Post-Formation Compliance

**Post-Formation Compliance**

| Obligation | Deadline | Authority |
| --- | --- | --- |
| Annual return (MGT-7A) | Within 60 days of AGM | ROC (MCA) |
| Financial statements (AOC-4) | Within 30 days of AGM | ROC (MCA) |
| AGM (Annual General Meeting) | Within 6 months of financial year-end (first AGM within 9 months of incorporation) | Internal |
| Board meetings | Minimum 4 per year (gap ≤ 120 days) | Internal |
| Income tax return | 31 October (if audit required) / 31 July (otherwise) | Income Tax Department |
| GST returns | Monthly (GSTR-1, GSTR-3B) or quarterly (QRMP) | GST portal |
| TDS returns | Quarterly | Income Tax Department |
| DIR-3 KYC (director verification) | 30 September annually | MCA |
| Statutory audit | Mandatory for all companies | ICAI-registered CA |

### Documents Typically Required

Certificate of Incorporation (CoI)
MoA and AoA
PAN card of company
Board resolution for account opening
ID and address proof of all directors
Proof of registered office
SPICe+ application (bank account request embedded)

### Typical Timeline

3--7 days (with SPICe+ bank integration)
1--2 weeks (manual process)

### Common Banks

State Bank of India (SBI), HDFC Bank, ICICI Bank, Axis Bank (major)
Kotak Mahindra, IndusInd (private sector)
RazorpayX, Open (neo-banking for startups)

## Section 8 -- Foreign Founder Considerations

**Foreign Founder Considerations**

| Question | Answer |
| --- | --- |
| Non-resident directors allowed? | Yes, but at least 1 director must be resident in India (stayed in India for ≥182 days in the previous calendar year) |
| DIN for foreign directors | Obtainable via SPICe+ with passport and foreign address proof |
| DSC for foreign nationals | Available from Indian Certifying Authorities via video KYC |
| 100% FDI allowed? | Yes, in most sectors under automatic route; some sectors require government approval |
| Physical presence required? | Not for incorporation (online via MCA portal); resident director must be physically present in India |
| Apostille requirements | Foreign documents require apostille + notarised translation |
| FEMA compliance | FDI inflows must comply with FEMA regulations; FC-GPR filing within 30 days of allotment |
| Repatriation of profits | Permitted under automatic route for most sectors (subject to transfer pricing) |

## Section 9 -- Common Mistakes and Refusals

- **R-IN-F1 -- No Indian-resident director** — At least one director must have been resident in India for at least 182 days in the preceding calendar year. A company cannot be incorporated without this. Foreign founders must appoint a qualifying resident director.
- **R-IN-F2 -- Ignoring annual compliance** — Indian companies face heavy penalties for non-filing: ₹100/day for late annual return, disqualification of directors after 3 years of non-filing (s164(2)), and potential strike-off by ROC.  _(s164(2))_
- **R-IN-F3 -- DIR-3 KYC missed** — Every director must file DIR-3 KYC annually by 30 September. Missing this results in DIN deactivation (₹5,000 penalty to reactivate) and inability to file any MCA forms.
- **R-IN-F4 -- Shell company formation** — MCA actively identifies and strikes off shell companies under s248. This skill will not assist in forming a company with no genuine business activity. Dormant company status (s455) exists for genuine temporary inactivity.  _(s248; s455)_
- **R-IN-F5 -- Authorised capital too low** — Starting with ₹1 lakh authorised capital is common, but increasing it later costs ₹15,000+ in fees. If the business plan requires significant capitalisation, advise higher authorised capital upfront.

## Section 10 -- Timeline

**Timeline**

| Step | Duration | Cumulative |
| --- | --- | --- |
| Obtain DSC for directors | 1--3 days | Day 1--3 |
| Reserve name (RUN) | 2--3 days | Day 3--6 |
| Prepare MoA, AoA, and supporting documents | 2--5 days | Day 5--11 |
| File SPICe+ on MCA portal | 1 day | Day 6--12 |
| ROC processing | 5--10 working days | Day 11--22 |
| Certificate of Incorporation + PAN + TAN | Same as ROC approval | Day 11--22 |
| Open bank account | 3--7 days | Day 14--29 |
| GST registration (if applied via AGILE) | 3--7 working days | Day 14--29 |
| **Ready to trade** |  | **~2--4 weeks** |

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
