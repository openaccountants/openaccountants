---
name: malta-formation
description: Use this skill whenever asked about forming, incorporating, or registering a company in Malta. Trigger on phrases like "set up a company in Malta", "Malta Ltd", "Malta company formation", "register a business in Malta", "MBR registration", "Malta Business Registry", "incorporate in Malta", "Malta company costs", "Malta share capital", "Malta memorandum and articles", or any question about starting a limited liability company in Malta. Covers entity types, registration process, capital requirements, costs, post-formation compliance, and bank account opening. ALWAYS read this skill before advising on Malta company formation.
version: 1.0
jurisdiction: MT
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - company-formation-workflow-base
category: formation
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Malta Formation

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Malta (Republic of Malta) |
| Currency | EUR |
| Company registrar | Malta Business Registry (MBR) -- mbr.mt |
| Key legislation | Companies Act, Chapter 386 |
| Typical formation time | 3--5 working days (electronic filing via BAROS) |
| Corporate tax rate | 35% (effective 5% after refund system) |
| Skill version | 1.0 |

## Section 2 -- Entity Types Comparison

**Entity Types Comparison**

| Feature | Sole Trader | Private Limited (Ltd) | General Partnership (Soċjetà f'Isem Kollettiv) | Public Limited (p.l.c.) |
| --- | --- | --- | --- | --- |
| Legal personality | No | Yes | No | Yes |
| Liability | Unlimited | Limited to share capital | Unlimited (joint and several) | Limited to share capital |
| Min. shareholders | 1 | 1 (single-member) or 2+ | 2+ | 2+ |
| Min. directors | N/A | 1 | N/A | 2 |
| Company secretary | No | Yes (must be Malta-resident) | No | Yes |
| Min. authorised capital | N/A | €1,164.69 | N/A | €46,587.47 |
| Min. paid-up capital | N/A | 20% of authorised (€233) | N/A | 25% of authorised |
| Tax treatment | Personal income tax | Corporate 35% (refund system) | Partners taxed individually | Corporate 35% (refund system) |
| Admin burden | Low | Medium | Low | High |
| Audit required | No | Only if thresholds exceeded | No | Yes |

**Recommended default:** Private Limited Company (Ltd) for most commercial purposes.

### Step 1: Choose Company Name

- **Choose Company Name** — - Check availability on MBR's BAROS portal - Name must end in "Limited" or "Ltd" - Restricted words (bank, insurance, fund) require prior regulatory approval  _(MBR BAROS portal)_

### Step 2: Prepare Memorandum and Articles of Association

- **Prepare Memorandum and Articles of Association** — - Must include: company name, registered office (in Malta), objects, authorised share capital, share structure, director and secretary details - Signed by all subscribers before a legal procurator or notary  _(Companies Act, Chapter 386)_

### Step 3: Deposit Share Capital

- **Deposit Share Capital** — - Minimum 20% of each share's nominal value must be paid up on signing - Deposit into a bank account opened in the company's name (in formation) - Obtain bank deposit slip as evidence for MBR  _(Companies Act, Chapter 386)_

### Step 4: File with Malta Business Registry (MBR)

- **File with Malta Business Registry (MBR)** — - Submit memorandum and articles via BAROS (electronic) or in paper - Attach bank deposit slip, ID copies of directors/shareholders, proof of registered office - Pay registration fee  _(MBR)_

### Step 5: Obtain Certificate of Registration

- **Obtain Certificate of Registration** — - MBR issues certificate once documents satisfy all checks - Company legally exists from date stated on certificate  _(MBR)_

### Step 6: Tax Registration with Commissioner for Revenue (CFR)

- **Tax Registration with Commissioner for Revenue (CFR)** — - Register for income tax via CFR e-Services - Obtain tax registration number  _(CFR)_

### Step 7: VAT Registration

- **VAT Registration** — - Register under Article 10 (standard) or Article 11 (exempt without credit) - Mandatory if turnover exceeds €35,000 threshold or if intra-EU supplies  _(VAT Act Article 10 / Article 11)_

### Step 8: Employer Registration (if applicable)

- **Employer Registration (if applicable)** — - Register with Jobsplus for employment licences - Register for SSC Class 1 contributions with CFR  _(Jobsplus / CFR)_

## Section 4 -- Capital Requirements

**Capital Requirements**

| Entity Type | Min. Authorised Capital | Min. Paid-Up | Payment Timing | In-Kind Contributions |
| --- | --- | --- | --- | --- |
| Private Ltd | €1,164.69 | 20% (€233) | On signing of memorandum | Permitted (must be valued by independent expert) |
| Public p.l.c. | €46,587.47 | 25% | On signing of memorandum | Permitted (independent valuation required) |
| Single-member Ltd | €1,164.69 | 20% (€233) | On signing of memorandum | Permitted |

- **Full subscription requirement** — Where authorised capital equals the statutory minimum, it must be fully subscribed in the memorandum.  _(Companies Act, Chapter 386)_

## Section 5 -- Costs Breakdown

**Costs Breakdown**

| Cost Component | Amount (EUR) | Notes |
| --- | --- | --- |
| MBR registration fee (electronic) | €100 | For authorised capital up to €1,500 |
| MBR registration fee (paper) | €245 | For authorised capital up to €1,500 |
| Paid-up share capital | €233 | 20% of €1,164.69 minimum |
| Legal / CSP professional fees | €2,500--€4,000 | Preparation of memorandum and articles |
| Document certification | €100--€200 | Notarisation of signatures |
| Bank account setup | €0--€500 | Varies by bank |
| **Total initial cost** | **€3,000--€5,200** | Excluding professional fees for complex structures |

### Annual Maintenance

**Annual Maintenance**

| Item | Cost (EUR) |
| --- | --- |
| Annual return filing fee (MBR) | €100 (electronic) |
| Registered office | €500--€1,500/year (if using service provider) |
| Accountancy / audit fees | €1,500--€5,000/year |
| Company secretary fees | €500--€1,200/year |

## Section 6 -- Post-Formation Compliance

**Post-Formation Compliance**

| Obligation | Deadline | Authority |
| --- | --- | --- |
| Annual return | Within 42 days of anniversary of registration | MBR |
| Financial statements filing | Within 10 months of financial year-end | MBR |
| Income tax return | 30 June of following year (for calendar year-end) | CFR |
| VAT returns | Quarterly or as directed | CFR |
| Beneficial ownership register | Within 14 days of any change | MBR |
| AML obligations | Ongoing (if subject entity under PMLA) | FIAU |
| SSC returns | Monthly | CFR |

### Documents Typically Required

- Certificate of registration
- Memorandum and articles of association
- Board resolution authorising account opening
- ID and proof of address for all directors, shareholders, and UBOs
- Description of business activities and expected turnover
- Source of funds documentation

### Typical Timeline

- 2--6 weeks (enhanced due diligence for non-resident shareholders)

### Common Banks

- Bank of Valletta (BOV)
- HSBC Malta
- APS Bank
- MeDirect
- Sparkasse Bank Malta

## Section 8 -- Foreign Founder Considerations

**Foreign Founder Considerations**

| Question | Answer |
| --- | --- |
| Non-resident directors allowed? | Yes, but company secretary must be Malta-resident |
| Nominee shareholders permitted? | Yes |
| Nominee directors permitted? | Yes (but ultimate beneficial owners must be disclosed to MBR) |
| Apostille requirements | Foreign documents must be apostilled or legalised |
| Physical presence required? | Not strictly required; power of attorney accepted for signing |
| Foreign ownership restrictions | None for standard Ltd; regulated activities (banking, gaming, funds) require MFSA licensing |

## Section 9 -- Common Mistakes and Refusals

- **R-MT-F1 -- Shell company request** — "This skill will not assist in forming a company with no genuine economic substance in Malta. Shell structures without real operations, employees, or premises may violate AML regulations and expose founders to criminal liability. Escalate to a licensed legal practitioner."  _(R-MT-F1)_
- **R-MT-F2 -- Nominee structures without substance** — "Using nominee directors and shareholders to obscure beneficial ownership without legitimate business purpose is a red flag under Malta's PMLA. Beneficial ownership must always be disclosed to the MBR. Refuse to proceed if the client's stated purpose is to hide ownership."  _(R-MT-F2)_
- **R-MT-F3 -- Regulated activity without licensing** — "If the business involves financial services, gaming, crypto, insurance, or investment management, MFSA licensing is required before operations commence. Formation alone is insufficient. Escalate to a regulated-sector specialist."  _(R-MT-F3)_
- **R-MT-F4 -- Insufficient capital for the business plan** — "While the legal minimum is €1,165, banks and counterparties may refuse to deal with undercapitalised entities. Flag if the proposed capital is clearly insufficient for the stated business activity."  _(R-MT-F4)_

## Section 10 -- Timeline

**Timeline**

| Step | Duration | Cumulative |
| --- | --- | --- |
| Name availability check | 1 day | Day 1 |
| Draft memorandum and articles | 2--5 days | Day 3--6 |
| Open bank account and deposit capital | 1--3 weeks | Day 10--27 |
| File with MBR (electronic) | 1 day | Day 11--28 |
| MBR review and certificate of registration | 1--3 days | Day 12--31 |
| Tax registration (CFR) | 1--5 days | Day 13--36 |
| VAT registration | 1--5 days | Day 14--41 |
| Employer registration (if needed) | 1--3 days | Day 15--44 |
| **Ready to trade** |  | **~3--6 weeks** |

The bottleneck is typically the bank account opening, especially for non-resident founders.

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
