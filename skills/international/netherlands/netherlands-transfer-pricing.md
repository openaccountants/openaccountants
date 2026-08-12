---
name: netherlands-transfer-pricing
description: Use this skill whenever asked about Netherlands transfer pricing rules, documentation requirements, or verrekenprijzen compliance. Trigger on phrases like "transfer pricing Netherlands", "Dutch TP documentation", "verrekenprijzen", "master file Netherlands", "local file Netherlands", "CbCR Netherlands", "APA Netherlands", "Article 8b DCITA", "DTA transfer pricing", or any question about intercompany pricing for Dutch entities.
version: 1.0
jurisdiction: NL
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on: - transfer-pricing-workflow-base
category: transfer-pricing
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Netherlands Transfer Pricing

## Netherlands Transfer Pricing Skill v1.0

## Section 1 -- Quick Reference

**Quick Reference table**

| Field | Value |
| --- | --- |
| Country | Netherlands (Kingdom of the Netherlands) |
| Tax authority | Dutch Tax Administration (Belastingdienst / DTA) |
| Key TP legislation | Article 8b Dutch Corporate Income Tax Act (DCITA / Wet Vpb 1969) |
| CbCR / Master/Local File legislation | Articles 29b-29h DCITA |
| Mismatch provisions | Articles 8bb, 8bc, 8bd DCITA (from 1 Jan 2022) |
| OECD member? | Yes |
| BEPS signatory? | Yes |
| Effective date (BEPS documentation) | From FY 2016 |
| Currency | EUR |
| Documentation language | Dutch or English |
| Skill version | 1.0 |

## Section 2 -- Documentation Requirements

### 2.1 General TP Documentation (All Taxpayers)

**General TP Documentation table**

| Item | Detail |
| --- | --- |
| Required? | Yes -- Article 8b(3) DCITA: all taxpayers must document and substantiate intercompany transactions |
| Threshold | No threshold -- applies to all entities regardless of size |
| Format | Free-form; must be appropriate to demonstrate arm's length character |
| Provision to DTA | On request; reasonable period (typically 4-6 weeks) |

### 2.2 Master File

**Master File table**

| Item | Detail |
| --- | --- |
| Required? | Yes, if consolidated annual group revenue ≥ EUR 50 million |
| Format | OECD Annex I to Chapter V |
| Filing | Not filed; available on request (due when CIT return filing deadline has passed) |
| Update frequency | Annually |

### 2.3 Local File

**Local File table**

| Item | Detail |
| --- | --- |
| Required? | Yes, if consolidated annual group revenue ≥ EUR 50 million |
| Format | OECD Annex II to Chapter V |
| Filing | Not filed; available on request |
| Update frequency | Annually; benchmark studies updated every 3 years (absent material business model changes) |

### 2.4 Country-by-Country Report (CbCR)

**CbCR table**

| Item | Detail |
| --- | --- |
| Threshold | Consolidated group revenue ≥ EUR 750 million |
| Filing deadline | 12 months after end of FY |
| Filing method | Electronic (XML format) to DTA |
| Notification | Annual notification required (identify filing entity) |

## Section 3 -- Arm's Length Standard

### 3.1 Definition

- **Arm's length principle** — Article 8b(1) DCITA: Conditions agreed between related parties that differ from conditions that would have been agreed between independent parties under comparable circumstances must be adjusted. The arm's length principle is applied in accordance with the OECD Transfer Pricing Guidelines.  _(Article 8b(1) DCITA)_

### 3.2 Accepted Methods

**Accepted Methods table**

| Method | Accepted |
| --- | --- |
| Comparable Uncontrolled Price (CUP) | Yes |
| Resale Price Method (RPM) | Yes |
| Cost Plus Method (CPM) | Yes |
| Transactional Net Margin Method (TNMM) | Yes |
| Profit Split Method (PSM) | Yes |

### 3.3 Preferred Method

- **Preferred method** — No statutory hierarchy. Most appropriate method based on facts and circumstances. OECD Guidelines applied as primary interpretive source.

### 3.4 Transfer Pricing Mismatch Provisions (from 2022)

- **Article 8bb** — No downward profit adjustment without corresponding upward adjustment in counterparty jurisdiction  _(Article 8bb DCITA)_
- **Article 8bc** — Asset/liability transfers -- Dutch tax base set at arm's length if no corresponding adjustment in transferor's jurisdiction  _(Article 8bc DCITA)_
- **Article 8bd** — Contributions/distributions -- Dutch CIT base capped/floored at transferor's tax base value  _(Article 8bd DCITA)_

## Section 4 -- Filing Obligations

**Filing Obligations table**

| Obligation | Detail |
| --- | --- |
| TP documentation (Art. 8b) | Maintain in administration; provide on request |
| Master File / Local File | Maintain; available after CIT return filing deadline |
| CbCR (Art. 29b-29h) | Annual electronic filing |
| CbCR notification | Annual notification to DTA |
| Corporate tax return | No separate TP form; self-assessment |

## Section 5 -- Deadlines

**Deadlines table**

| Item | Deadline |
| --- | --- |
| General TP documentation | Available on request (4-6 weeks reasonable period) |
| Master/Local File availability | By CIT return filing deadline |
| CbCR filing | 12 months after end of FY |
| CbCR notification | Before CbCR filing deadline |
| Corporate tax return | Generally 5 months after FY-end (extensions available up to ~12 months) |

## Section 6 -- Penalties

**Penalties table**

| Offence | Penalty |
| --- | --- |
| No specific TP documentation penalty | N/A -- Netherlands does not have dedicated TP documentation fines |
| Burden of proof shift | Shifts to taxpayer where documentation is inadequate |
| General corporate penalties for incorrect returns | Standard penalties apply (up to 100% of additional tax for deliberate non-compliance) |
| CbCR non-compliance (general) | Up to EUR 25,750 |
| CbCR non-compliance (severe/deliberate) | Up to EUR 1,030,000 (2025 levels) |
| Late CbCR notification | Administrative penalties |

## Section 7 -- Advance Pricing Agreements (APA)

**APA table**

| Item | Detail |
| --- | --- |
| Availability | Yes (well-established program) |
| Types | Unilateral, Bilateral, Multilateral |
| Governing authority | DTA (Belastingdienst) |
| Application | No formal fee |
| Typical duration | 4-5 years prospective; rollback negotiable |
| Processing time | Unilateral: 6-12 months; Bilateral: 18-36 months |
| Annual compliance report | Required |
| Renewal | Possible; simplified process for renewals |
| ICAP participation | Yes (International Compliance Assurance Programme) |

The Netherlands has a long history of providing advance certainty on TP through its ruling practice.

## Section 8 -- Safe Harbours

The Netherlands does not have formal statutory safe harbour rules.

**Safe Harbours table**

| Area | Detail |
| --- | --- |
| Low-value intra-group services | OECD simplified approach (5% cost-plus) generally accepted |
| Interest rates | No safe harbour; market-based approach required |
| SMEs (< EUR 50m revenue) | No Master/Local File obligation, but general documentation still required |
| Benchmark study updates | Accepted every 3 years if no material changes |
| Innovation box | Qualifying IP income taxed at effective 9% rate; TP required for nexus approach |

### 8.1 Practical Simplifications for SMEs

- **SME simplifications** — For companies below EUR 50 million group revenue: No prescribed form for TP documentation; Documentation should be "appropriate" to substantiate arm's length character; DTA policy grants 4-6 weeks to produce documentation on request; Benchmark studies from other group entities may be leveraged with local adjustments

### 8.2 Benchmark Study Refresh Cycle

- **Benchmark study refresh cycle** — The Netherlands accepts benchmark studies updated every three years, provided: No material changes to the business model; No significant changes to functions, assets, or risks; Financial data updated annually even if benchmark not refreshed

## Section 9 -- Recent Developments

**Recent Developments table**

| Date | Development |
| --- | --- |
| 2024-2025 | Clarifications on TP mismatch provisions (Art. 8bb-8bd) |
| 2024 | Pillar Two (GloBE) implemented via Wet minimumbelasting 2024 |
| 2024 | Public CbCR implementation (EU Directive) |
| 2024 | OECD Amount B: Netherlands actively participating in implementation |
| 2022 | TP mismatch legislation (Art. 8bb, 8bc, 8bd) entered into force |
| Ongoing | Dutch case law on profit allocation and TP continues to develop |
| Ongoing | EU Transfer Pricing Directive under discussion |

## Section 10 -- Interaction with Other Skills

**Interaction with Other Skills table**

| Related skill | Interaction |
| --- | --- |
| netherlands-bookkeeping | TP documentation supported by Dutch GAAP/IFRS records |
| netherlands-corporate-tax | TP adjustments affect CIT (vennootschapsbelasting) base |
| netherlands-vat | TP adjustments may affect customs valuation |
| Innovation box | Qualifying IP income regime interacts with TP for IP-related transactions |
| Fiscal unity | TP applies to transactions with entities outside the fiscal unity |
| CbCR | Risk assessment tool for DTA |

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your jurisdiction — no liability on either side until you and the accountant sign a formal engagement letter — book a free 30-minute call:

→ [Book a call](https://calendly.com/openaccountants-info/30min)

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
