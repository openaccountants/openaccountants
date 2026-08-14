---
name: australia-transfer-pricing
description: Use this skill whenever asked about Australia transfer pricing rules, documentation requirements, or ATO transfer pricing compliance. Trigger on phrases like "transfer pricing Australia", "Australian TP documentation", "ATO transfer pricing", "master file Australia", "local file Australia", "CbCR Australia", "APA Australia", "Subdivision 815", "International Dealings Schedule", "IDS", "significant global entity", or any question about intercompany pricing for Australian entities.
version: 1.0
jurisdiction: AU
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - transfer-pricing-workflow-base
category: transfer-pricing
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Australia Transfer Pricing

## Australia Transfer Pricing Skill v1.0

Australia Transfer Pricing Skill v1.0

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Australia (Commonwealth of Australia) |
| Tax authority | Australian Taxation Office (ATO) |
| Key TP legislation | Subdivision 815-B, Income Tax Assessment Act 1997 (ITAA 1997) |
| Documentation | Subdivision 815-D ITAA 1997; Division 284-E, Schedule 1, Tax Administration Act 1953 (TAA 1953) |
| CbCR legislation | Division 815-E ITAA 1997 |
| OECD member? | Yes |
| BEPS signatory? | Yes |
| Currency | AUD |
| Documentation language | English |
| Skill version | 1.0 |

## Section 2 -- Documentation Requirements

### 2.1 General Documentation (All Taxpayers)

**General Documentation (All Taxpayers)**

| Item | Detail |
| --- | --- |
| Required? | Yes -- all taxpayers with international related-party dealings must keep records demonstrating arm's length conditions |
| Timing | Contemporaneous -- prepared before lodging income tax return |
| Penalty relevance | Without contemporaneous documentation, cannot establish "reasonably arguable position" (RAP) |

### 2.2 Three-Tier Documentation (Significant Global Entities)

Applies to entities in groups with consolidated annual global income ≥ AUD 1 billion:

**Three-Tier Documentation (Significant Global Entities)**

| Document | Detail |
| --- | --- |
| Master File | OECD Annex I format; filed electronically |
| Local File | Australian-specific format (Short Form available for smaller dealings) |
| CbC Report | OECD Annex III format |
| Filing deadline | Within 12 months of end of income year |
| Filing method | Electronic lodgment with ATO |

### 2.3 International Dealings Schedule (IDS)

**International Dealings Schedule (IDS)**

| Item | Detail |
| --- | --- |
| Required? | Yes, for all taxpayers with material international related-party dealings |
| Filing | Annually with the corporate tax return |
| Content | Summary of related-party transactions, methods used, documentation status |

### 2.4 Short Form Local File

- **Short Form Local File availability** — Available for entities with lower-risk or less material international related-party dealings that still meet the AUD 1 billion threshold.  _(unsure)_

## Section 3 -- Arm's Length Standard

### 3.1 Definition

- **Arm's length standard definition** — Subdivision 815-B: Where conditions between entities in international dealings differ from arm's length conditions, and an entity gets a "transfer pricing benefit," the taxable income is adjusted to reflect arm's length conditions.  _(Subdivision 815-B ITAA 1997)_

### 3.2 Accepted Methods

**Accepted Methods**

| Method | Accepted |
| --- | --- |
| Comparable Uncontrolled Price (CUP) | Yes |
| Resale Price Method (RPM) | Yes |
| Cost Plus Method (CPM) | Yes |
| Transactional Net Margin Method (TNMM) | Yes |
| Profit Split Method (PSM) | Yes |
| Other reliable methods | Yes (method flexibility) |

### 3.3 Preferred Method

- **Preferred method approach** — No statutory hierarchy. ATO follows OECD "most appropriate method" approach. CUP preferred where reliable comparables exist.  _(unsure)_

### 3.4 Self-Assessment

- **Self-assessment system** — Australia operates a self-assessment system -- taxpayers must determine and apply arm's length conditions without prior ATO approval.  _(unsure)_

## Section 4 -- Filing Obligations

**Filing Obligations**

| Obligation | Detail |
| --- | --- |
| International Dealings Schedule (IDS) | Filed with income tax return |
| Master File (SGEs) | Electronic lodgment within 12 months of year-end |
| Local File (SGEs) | Electronic lodgment within 12 months of year-end |
| CbC Report (SGEs) | Electronic lodgment within 12 months of year-end |
| Reportable Tax Position (RTP) | Large taxpayers must disclose TP positions |
| Income tax return | Annual self-assessment |

## Section 5 -- Deadlines

**Deadlines**

| Item | Deadline |
| --- | --- |
| TP documentation preparation | Before lodging income tax return |
| IDS filing | With income tax return (varies by entity type; generally 15 January for large) |
| Master/Local/CbC Report | 12 months after end of income year |
| Income tax return (companies) | Generally due by 15 January following year (for 30 June year-end) with extensions |

## Section 6 -- Penalties

### 6.1 Transfer Pricing Shortfall Penalties

**Transfer Pricing Shortfall Penalties**

| Scenario | Penalty Rate |
| --- | --- |
| Reasonably arguable position (RAP) established | No penalty |
| No RAP, no dominant tax purpose | 25% of tax shortfall |
| No RAP, dominant tax purpose | 50% of tax shortfall |
| Uplift for repeat behaviour | Additional 20% |
| SGE multiplier | Doubled penalties for SGEs |

### 6.2 Documentation Impact

- **Documentation impact on RAP** — Without contemporaneous TP documentation prepared before lodging the return, a taxpayer is statutorily denied a reasonably arguable position.  _(unsure)_

### 6.3 Failure to Lodge (SGEs)

**Failure to Lodge (SGEs)**

| Offence | Penalty |
| --- | --- |
| Failure to lodge Local File, Master File, or CbC Report | Up to AUD 825,000 per failure |
| Shortfall interest charge | Applies on underpaid tax |

## Section 7 -- Advance Pricing Agreements (APA)

**Advance Pricing Agreements (APA)**  _(TR 95/23; PCG 2019/1)_

| Item | Detail |
| --- | --- |
| Availability | Yes (well-established program) |
| Types | Unilateral, Bilateral, Multilateral |
| Governing guidance | TR 95/23; Practical Compliance Guideline PCG 2019/1 |
| Application | To ATO; Expression of Interest followed by formal application |
| Duration | Typically 3-5 years prospective; rollback possible |
| Fees | No formal fee |
| Processing time | 12-24 months (bilateral may be longer) |
| Annual compliance report | Required |
| Critical assumptions | APA subject to critical assumptions; non-compliance may revoke |

## Section 8 -- Safe Harbours

**Safe Harbours**

| Area | Detail |
| --- | --- |
| Low-value intra-group services | Mark-up approach accepted (5% cost-plus per OECD simplified approach) |
| Low-level inbound/outbound loans | Interest-rate safe harbours available (PCG guidance) |
| Small taxpayers (turnover < AUD 50m) | Low-risk dealings may have simplified documentation |
| Distributors with limited related-party dealings | Materiality-based simplification |
| Management/technical services | Threshold-based simplification |

ATO publishes Practical Compliance Guidelines indicating risk zones for various transaction types.

## Section 9 -- Recent Developments

**Recent Developments**

| Date | Development |
| --- | --- |
| 2024-2025 | Updated Local File instructions (Part A and Part B) |
| 2024 | Enhanced ATO compliance focus on intangibles and financial transactions |
| 2023 | Pillar Two (GloBE) legislation enacted |
| 2022 | Multinational Tax Integrity Package -- increased penalties for SGEs |
| Ongoing | ATO PCGs on profit allocation to permanent establishments |
| Ongoing | OECD Amount B: Australia participating in design; implementation timeline TBC |
| Ongoing | Tax Avoidance Taskforce targeting multinationals |

## Section 10 -- Interaction with Other Skills

**Interaction with Other Skills**

| Related skill | Interaction |
| --- | --- |
| australia-bookkeeping | TP documentation relies on Australian accounting records |
| australia-corporate-tax | TP adjustments directly affect taxable income |
| australia-gst | TP adjustments may affect customs value and GST on imports |
| Thin capitalisation | Separate rules limit debt deductions; interact with TP for financial transactions |
| Diverted Profits Tax (DPT) | 40% rate for diverted profits; TP documentation relevant |
| CbCR | ATO uses CbCR for risk-based audit selection |

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
