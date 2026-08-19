---
name: canada-transfer-pricing
description: Use this skill whenever asked about Canada transfer pricing rules, documentation requirements, or CRA transfer pricing compliance. Trigger on phrases like "transfer pricing Canada", "Canadian TP documentation", "CRA transfer pricing", "master file Canada", "local file Canada", "CbCR Canada", "APA Canada", "Section 247", "Form T106", "contemporaneous documentation Canada", or any question about intercompany pricing for Canadian entities.
version: 1.0
jurisdiction: CA
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: Edgar Lautsyus
review_status: current
depends_on:
  - transfer-pricing-workflow-base
category: transfer-pricing
tier: 1
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Canada Transfer Pricing

## Canada Transfer Pricing Skill v1.0

## Verified rates & thresholds (accountant-reviewed)

Reviewed against the cited tax authorities by **Nathan Wiebe** on 2026-06-21.
Items flagged for further clarification are tracked separately and excluded here.
This block is generated from verified `skill_facts` — edit the facts, not the prose.

### Transfer Pricing

- **TP provision** — Section 247, ITA  _(ITA s.247; CRA — Transfer pricing — canada.ca)_
- **Arm's length standard** — ITA s.247(2)  _(ITA s.247(2))_
- **Recharacterization power** — ITA s.247(2)(b)(c)(d)  _(ITA s.247(2)(b)(c)(d))_
- **Documentation threshold** — Aggregate transactions > CAD $1M with any single non-resident related party  _(ITA s.247(4); CRA — Transfer pricing memorandum TPM-09)_
- **Timing** — By documentation-due date (tax return filing deadline)  _(ITA s.247(4)(a))_
- **Provision to CRA on request** — 3 months (30 days for years beginning after 4 Nov 2025)  _(ITA s.247(4)(b); Finance Canada draft legislation Aug 2025)_
- **Form T106** — If aggregate NR related-party transactions > $1M  _(ITA s.233.1; Form T106 instructions)_
- **Form T106 deadline** — 6 months after taxation year-end  _(ITA s.233.1(4))_
- **CbCR (Form RC4649)** — EUR 750M+ consolidated group revenue  _(ITA Part XVIII; Form RC4649 instructions)_
- **CbCR deadline** — 12 months after fiscal year-end  _(ITA s.233.8(3))_
- **TP penalty threshold** — The skill correctly states the threshold is being updated. For taxation years beginning BEFORE November 4, 2025: lesser of $5M or 10% of gross revenue. For years beginning AFTER November 4, 2025: lesser of $10M or 10% of gross revenue.  _(ITA s.247(3); Finance Canada draft legislation Aug 2025)_
- **Penalty rate** — 10% of TP adjustment above threshold  _(ITA s.247(3))_
- **Reasonable efforts defence** — No penalty if reasonable efforts made  _(ITA s.247(3); CRA — IC 87-2R)_
- **Documentation failure** — Deemed NOT reasonable efforts  _(ITA s.247(3)(b))_
- **Late T106** — $25/day, min $100, max $2,500  _(ITA s.162(7); CRA)_
- **Types** — Unilateral, Bilateral, Multilateral  _(CRA — Advance pricing arrangement — canada.ca; IC 94-4R)_
- **Duration** — Typically 5 years prospective; rollback up to 5 prior years  _(CRA — IC 94-4R)_
- **Application fee** — None  _(CRA — IC 94-4R)_
- **Processing time** — 2–4 years (bilateral longer)  _(CRA — APA program statistics)_
- **Formal safe harbour?** — None — Canada has no statutory TP safe harbour  _(ITA s.247; CRA — IC 87-2R)_
- **Low-value services** — No formal rule; CRA may accept 5% cost-plus in low-risk  _(CRA — IC 87-2R; OECD TP Guidelines Chapter VII)_
- **Form T106 de minimis** — ≤ $1M aggregate: no filing required  _(ITA s.233.1)_

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Canada |
| Tax authority | Canada Revenue Agency (CRA) |
| Key TP legislation | Section 247, Income Tax Act (ITA) |
| Documentation | Subsection 247(4) ITA -- contemporaneous documentation |
| CbCR | Form RC4649; Part XVIII of the ITA |
| OECD member? | Yes |
| BEPS signatory? | Yes |
| Currency | CAD |
| Documentation language | English or French |
| Skill version | 1.0 |

## Section 2 -- Documentation Requirements

### 2.1 Contemporaneous Documentation (Section 247(4))

**Contemporaneous Documentation (Section 247(4))**

| Item | Detail |
| --- | --- |
| Required? | Yes, for all taxpayers with non-arm's length transactions with non-residents (where Form T106 filed) |
| Threshold | Aggregate transactions > CAD 1 million with any single non-resident related party |
| Timing | Must be prepared or obtained by the "documentation-due date" (tax return filing deadline) |
| Content | Six prescribed items per s.247(4)(a): parties, terms, method, assumptions, comparable data, adjustments |
| Provision to CRA | Within 3 months of written request (reducing to 30 days for years beginning after 4 Nov 2025) |

### 2.2 Form T106 -- Information Return

**Form T106 -- Information Return**

| Item | Detail |
| --- | --- |
| Required? | Yes, if total non-arm's length transactions with non-residents > CAD 1 million in tax year |
| Filing deadline | 6 months after end of taxation year (aligns with corporate tax return) |
| Content | Summary of all non-arm's length transactions by non-resident party |

### 2.3 Master File / Local File

Canada does not formally mandate OECD-style Master File / Local File (no separate filing). However, the 2025 draft legislation introduces enhanced documentation aligning with OECD standards for years beginning after November 4, 2025.

### 2.4 Country-by-Country Report (Form RC4649)

**Country-by-Country Report (Form RC4649)**

| Item | Detail |
| --- | --- |
| Threshold | Consolidated group revenue ≥ EUR 750 million |
| Filing deadline | 12 months after fiscal year-end |
| Applies to | Canadian ultimate parent entities of qualifying MNE groups |
| Notification | Required (CBC2 notification form) |

## Section 3 -- Arm's Length Standard

### 3.1 Definition

- **Arm's length standard definition** — Section 247(2) ITA: Where terms/conditions between a taxpayer and a non-arm's length non-resident differ from those that would have been made between arm's length parties, adjustments are made to reflect arm's length conditions.  _(Section 247(2) ITA)_

### 3.2 Accepted Methods

**Accepted Methods**

| Method | Accepted |
| --- | --- |
| Comparable Uncontrolled Price (CUP) | Yes |
| Resale Price Method (RPM) | Yes |
| Cost Plus Method (CPM) | Yes |
| Transactional Net Margin Method (TNMM) | Yes |
| Profit Split Method (PSM) | Yes |

### 3.3 Preferred Method

No statutory hierarchy. CRA accepts most appropriate method per OECD Guidelines. IC 87-2R provides administrative guidance.

### 3.4 Recharacterization Power

- **Recharacterization Power** — Section 247(2)(b)(c)(d): CRA can recharacterize transactions if they would not have been entered into at all between arm's length parties (not just reprice them).  _(Section 247(2)(b)(c)(d))_

## Section 4 -- Filing Obligations

**Filing Obligations**

| Obligation | Detail |
| --- | --- |
| Contemporaneous documentation | Prepared by documentation-due date; provided within 3 months (30 days from 2025+) of CRA request |
| Form T106 | Annual information return (if threshold met) |
| Form T1134 | Information return for foreign affiliates |
| Form RC4649 (CbCR) | Annual filing (EUR 750m+ groups) |
| CBC2 notification | Annual notification |
| Corporate tax return (T2) | Annual self-assessment |

## Section 5 -- Deadlines

**Deadlines**

| Item | Deadline |
| --- | --- |
| Documentation preparation | By documentation-due date (corporate: 6 months after year-end) |
| Provision to CRA on request | 3 months from written request (30 days for years beginning after 4 Nov 2025) |
| Form T106 | 6 months after taxation year-end |
| CbCR (RC4649) | 12 months after fiscal year-end |
| T2 corporate tax return | 6 months after taxation year-end |
| T2 tax payment | 2-3 months after year-end (depending on entity type) |

## Section 6 -- Penalties

### 6.1 Transfer Pricing Penalty (s.247(3))

**Transfer Pricing Penalty (s.247(3))**

| Item | Detail |
| --- | --- |
| Trigger threshold | Net TP adjustment exceeds lesser of: CAD 5 million OR 10% of gross revenue (for taxation years beginning before 4 Nov 2025); lesser of CAD 10 million OR 10% of gross revenue (for taxation years beginning after 4 Nov 2025) |
| Penalty rate | 10% of the TP adjustment amount exceeding the threshold |
| Reasonable efforts defence | No penalty if taxpayer made "reasonable efforts" to determine arm's length pricing |
| Documentation impact | Failure to meet s.247(4) requirements = deemed NOT to have made reasonable efforts |

### 6.2 Other Penalties

**Other Penalties**

| Offence | Penalty |
| --- | --- |
| Late filing Form T106 | CAD 25/day, minimum CAD 100, maximum CAD 2,500 |
| Failure to file Form T106 | Up to CAD 2,500 per return |
| Late CbCR | Standard administrative penalties |

## Section 7 -- Advance Pricing Agreements (APA)

**Advance Pricing Agreements (APA)**

| Item | Detail |
| --- | --- |
| Availability | Yes (active program) |
| Types | Unilateral, Bilateral, Multilateral |
| Governing guidance | IC 94-4R (International Circular) |
| Application | To CRA Competent Authority Division |
| Duration | Typically 5 years prospective; rollback for up to 5 prior years |
| Fees | No application fee |
| Processing time | 2-4 years (bilateral takes longer) |
| Annual compliance report | Required |
| Key benefit | Eliminates penalty exposure for covered transactions |

## Section 8 -- Safe Harbours

Canada does not have formal statutory safe harbour rules for transfer pricing.

## Section 8 -- Safe Harbours

**Safe Harbours**

| Area | Detail |
| --- | --- |
| Low-value services | No formal safe harbour; CRA may accept 5% cost-plus in low-risk scenarios |
| Interest rates | No safe harbour; market benchmarking required (thin cap rules separate) |
| Simplified documentation (2025+) | Draft legislation introduces simplified requirements where prescribed conditions met |
| Small transactions | No de minimis; all related-party transactions should be at arm's length |
| Form T106 threshold | Aggregate transactions ≤ CAD 1 million: no Form T106 filing required |

### 8.1 Practical Risk Assessment

CRA uses a risk-based approach to TP audits, focusing on:
- Large/complex transactions with high-risk jurisdictions
- Transactions involving intangibles and cost-sharing arrangements
- Financial transactions (intercompany loans, guarantees)
- Entities with thin capitalisation concerns
- Losses sustained over multiple years in Canada

### 8.2 2025 Simplified Documentation

Draft legislation for taxation years beginning after November 4, 2025 introduces:
- Simplified contemporaneous documentation for taxpayers meeting prescribed conditions
- Conditions and scope still being finalized through consultation
- Intended to reduce compliance burden for lower-risk transactions

## Section 9 -- Recent Developments

**Recent Developments**

| Date | Development |
| --- | --- |
| August 2025 | Draft legislation: enhanced TP documentation requirements (OECD-aligned analytical framework) |
| November 2025 | New rules effective for taxation years beginning after 4 November 2025 |
| Nov 2025 | Penalty threshold increased to lesser of CAD 10 million or 10% of gross revenue (for taxation years beginning after 4 Nov 2025; lesser of CAD 5 million or 10% of gross revenue before that date) |
| 2025 | Response time for documentation reduced from 3 months to 30 days |
| 2024 | Pillar Two implementation underway |
| Ongoing | CRA increased TP audit activity on intangibles and financial transactions |
| Ongoing | Simplified documentation measures for prescribed conditions introduced |

## Section 10 -- Interaction with Other Skills

**Interaction with Other Skills**

| Related skill | Interaction |
| --- | --- |
| canada-bookkeeping | TP documentation relies on Canadian accounting records |
| canada-corporate-tax | TP adjustments under s.247 directly affect taxable income |
| canada-gst-hst | TP adjustments may affect customs value |
| Thin capitalisation | Separate debt-to-equity rules (s.18(4)) interact with TP for intercompany loans |
| Form T106 | Annual information return; compliance gateway for TP |
| CbCR | Used by CRA for risk-based audit selection |

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

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
