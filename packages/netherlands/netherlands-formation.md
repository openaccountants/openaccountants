---
name: netherlands-formation
description: Use this skill whenever asked about forming, incorporating, or registering a company in the Netherlands. Trigger on phrases like "set up a company in the Netherlands", "Dutch BV", "BV formation", "KvK registration", "Kamer van Koophandel", "Dutch company formation", "register a business Netherlands", "besloten vennootschap", "eenmanszaak", "VOF", "NV formation", "DGA salary", or any question about starting a business entity in the Netherlands. Covers entity types (BV, NV, eenmanszaak, VOF, CV), registration process, capital requirements, costs, post-formation compliance, and bank account opening. ALWAYS read this skill before advising on Dutch company formation.
version: 1.0
jurisdiction: NL
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - company-formation-workflow-base
category: formation
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Netherlands Formation

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Netherlands (Kingdom of the Netherlands) |
| Currency | EUR |
| Company registrar | Kamer van Koophandel (KvK) -- kvk.nl |
| Key legislation | Burgerlijk Wetboek (Boek 2); Flex-BV Act (2012); Handelsregisterwet |
| Typical formation time | 1--5 working days (notary to KvK registration) |
| Corporate tax rate | 19% (first €200,000 profit); 25.8% (above €200,000) |
| Skill version | 1.0 |

## Section 2 -- Entity Types Comparison

**Entity Types Comparison**

| Feature | Eenmanszaak (Sole Trader) | VOF (General Partnership) | BV (Private Ltd) | NV (Public Ltd) |
| --- | --- | --- | --- | --- |
| Legal personality | No | No | Yes | Yes |
| Liability | Unlimited | Unlimited (joint and several) | Limited to share capital | Limited to share capital |
| Min. founders | 1 | 2 | 1 | 1 |
| Min. share capital | N/A | N/A | €0.01 | €45,000 |
| Tax treatment | Income tax (IB) | Partners taxed via IB | Corporate tax (VPB) | Corporate tax (VPB) |
| Notary required | No | No | Yes | Yes |
| DGA salary requirement | N/A | N/A | €58,000/year (2026) | €58,000/year (2026) |
| Admin burden | Low | Low | Medium--High | Very High |
| Audit required | No | No | Only if thresholds exceeded | Only if thresholds exceeded |

**Recommended default:** BV (besloten vennootschap) for businesses expecting profit above €58,000 and desiring limited liability.

### Step 1: Engage a Civil-Law Notary (Notaris)

- **Notaris requirement** — A Dutch notaris is mandatory for BV formation. The notaris drafts the deed of incorporation (akte van oprichting) and articles of association (statuten). You cannot self-register a BV with KvK.

### Step 2: Prepare Articles and Shareholder Agreement

- **Articles and shareholder agreement** — Statuten define governance, share classes, transfer restrictions, voting rights. Since Flex-BV (2012): flexible share classes, no minimum capital, no bank statement required. Shareholder agreement (aandeelhoudersovereenkomst) recommended but not mandatory.  _(Flex-BV Act (2012))_

### Step 3: Execute Deed of Incorporation

- **Deed of incorporation execution** — All founders appear before notaris (or via power of attorney). Notaris verifies identity (ID/passport), legal capacity, and compliance with Wwft (AML). Minimum share capital: €0.01.  _(Wwft)_

### Step 4: KvK Registration

- **KvK registration details** — Notaris registers the BV with KvK (Handelsregister). KvK registration fee: €85.15 (from 1 January 2026). KvK number and RSIN issued immediately upon registration. BV legally exists from date of notarial deed (not KvK registration).

### Step 5: Tax Registration (Belastingdienst)

- **Tax registration process** — Automatic notification from KvK to Belastingdienst. BV receives VAT number (BTW-nummer) and corporate tax number. DGA (directeur-grootaandeelhouder) must set up payroll for own salary.  _(Belastingdienst)_

### Step 6: UBO Register

- **UBO register updates** — Beneficial owners automatically registered via KvK. Must be updated within 7 days of changes.  _(KvK)_

### Step 7: Open Business Bank Account

- **Bank account opening requirement** — Required for operations (minimum €0.01 capital deposit). Increasingly strict KYC for foreign-owned structures.

## Section 4 -- Capital Requirements

**Capital Requirements**

| Entity Type | Min. Share Capital | Min. Paid-Up | Payment Timing | In-Kind Contributions |
| --- | --- | --- | --- | --- |
| BV | €0.01 | No separate paid-up minimum | At or after incorporation | Permitted (beschrijving required; auditor's statement if no bank confirmation) |
| NV | €45,000 | 25% (€11,250) | Before registration | Permitted (auditor's statement required) |
| BV i.o. (in oprichting) | N/A | N/A | Can trade before deed; founders personally liable | N/A |

- **DGA salary is the real capital requirement** — For profitable BVs, the director-major shareholder (DGA) must pay themselves at least €58,000 in 2026 (€56,000 in 2025). This is the largest financial commitment, not the share capital.

## Section 5 -- Costs Breakdown

**Costs Breakdown**

| Cost Component | Amount (EUR) | Notes |
| --- | --- | --- |
| Notary fees | €500--€1,500 | Standard BV deed; complex structures higher |
| KvK registration fee | €85.15 | One-time (2026 rate) |
| Share capital | €0.01 (minimum) | Practical: €100--€1,000 recommended |
| Payroll setup (DGA salary) | €200--€500 | Accountant or payroll service |
| **Total initial cost** | **€785--€2,600** | Government fees + notary |

### Annual Maintenance

**Annual Maintenance**

| Item | Cost (EUR) |
| --- | --- |
| Accountant (jaarrekening + tax returns) | €1,500--€5,000/year |
| Payroll administration (DGA) | €300--€600/year |
| KvK extract | €15.20 per extract (online) |
| Audit fees (if required) | €5,000--€15,000/year |

## Section 6 -- Post-Formation Compliance

**Post-Formation Compliance**

| Obligation | Deadline | Authority |
| --- | --- | --- |
| Jaarrekening (annual accounts) deposit | Within 8 days of approval; max 12 months after year-end | KvK |
| Vennootschapsbelasting (corporate tax return) | Within 5 months of year-end (extension possible) | Belastingdienst |
| BTW-aangifte (VAT return) | Quarterly (monthly if elected) | Belastingdienst |
| Loonheffing (payroll tax) | Monthly | Belastingdienst |
| DGA salary compliance | Annually (minimum €58,000 in 2026) | Belastingdienst |
| UBO register update | Within 7 days of changes | KvK |
| Shareholders register | Maintain internally; update with notaris on transfers | Internal |

### Documents Typically Required

- KvK extract (uittreksel Handelsregister)
- Notarial deed of incorporation
- ID (passport) of all directors and shareholders (25%+)
- Proof of address for UBOs
- Business plan or activity description
- Source of funds documentation (for larger deposits)

### Typical Timeline

- Dutch digital banks (Bunq Business, Mollie): 1--5 days
- Traditional banks (ING, ABN AMRO, Rabobank): 2--6 weeks
- Non-resident founders: 4--8 weeks (enhanced due diligence)

### Common Banks

- ING, ABN AMRO, Rabobank (traditional)
- Bunq Business, Revolut Business NL (digital)

## Section 8 -- Foreign Founder Considerations

**Foreign Founder Considerations**

| Question | Answer |
| --- | --- |
| Non-resident directors allowed? | Yes, but DGA salary rules still apply if 5%+ shareholder |
| Nominee directors permitted? | Yes (but Wwft/AML due diligence applies; UBO must be disclosed) |
| Physical presence required? | No -- power of attorney accepted for notarial deed |
| Apostille requirements | Foreign documents require apostille + certified Dutch or English translation |
| BSN requirement | DGA must obtain a BSN (citizen service number) for payroll; obtainable at municipality |
| EU/non-EU differences | Non-EU directors may need work permit if managing from NL; remote management from abroad is possible |
| 30% ruling | Highly skilled migrants may qualify for 30% tax-free allowance (5 years, conditions apply) |

## Section 9 -- Common Mistakes and Refusals

- **R-NL-F1 -- Ignoring DGA salary obligation** — The minimum DGA salary of €58,000 (2026) applies to any BV where the director holds 5%+ of shares. Failure to comply results in Belastingdienst correcting the salary upwards and assessing additional tax + penalties. If the BV cannot yet afford this, apply for dispensation (beschikking lager gebruikelijk loon) proactively.  _(Belastingdienst)_
- **R-NL-F2 -- €0.01 capital without working capital** — While the legal minimum is €0.01, starting a BV with no working capital is impractical. The BV needs funds for operations, the DGA salary, and professional fees. Directors may face personal liability under article 2:248 BW if the company trades while effectively insolvent.  _(article 2:248 BW)_
- **R-NL-F3 -- Shell company or letterbox entity** — The Netherlands has substance requirements for holding and financing companies (anti-abuse directives). A BV without real economic activity, employees, or office space may not qualify for treaty benefits and may trigger scrutiny from Belastingdienst.  _(anti-abuse directives)_
- **R-NL-F4 -- Failing to file annual accounts** — Every BV must file annual accounts with KvK within 12 months of year-end. Failure to file within 13 months creates a presumption of mismanagement in case of bankruptcy (article 2:248 BW).  _(article 2:248 BW)_

## Section 10 -- Timeline

**Timeline**

| Step | Duration | Cumulative |
| --- | --- | --- |
| Engage notaris and prepare documents | 1--5 days | Day 1--5 |
| Execute deed of incorporation | 1 day | Day 2--6 |
| KvK registration (by notaris) | Same day or 1 day | Day 2--7 |
| Belastingdienst registration (automatic) | 1--3 weeks | Day 9--28 |
| Open bank account | 1--5 days (digital) / 2--6 weeks (traditional) | Day 3--49 |
| DGA payroll setup | 1--5 days | Day 4--54 |
| **Ready to trade** |  | **As fast as 1 week (digital bank + simple structure)** |

The Netherlands offers one of the fastest BV formation processes in Europe thanks to the Flex-BV Act.

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
