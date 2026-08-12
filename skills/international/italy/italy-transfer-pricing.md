---
name: italy-transfer-pricing
description: Use this skill whenever asked about Italy transfer pricing rules, documentation requirements, or prezzi di trasferimento compliance. Trigger on phrases like "transfer pricing Italy", "Italian TP documentation", "prezzi di trasferimento", "master file Italy", "local file Italy", "penalty protection Italy", "CbCR Italy", "APA Italy", "Agenzia delle Entrate TP", or any question about intercompany pricing for Italian entities.
version: 1.0
jurisdiction: IT
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on: - transfer-pricing-workflow-base
category: transfer-pricing
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Italy Transfer Pricing

## Italy Transfer Pricing Skill v1.0

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Italy (Italian Republic) |
| Tax authority | Agenzia delle Entrate (Italian Revenue Agency) |
| Key TP legislation | Article 110, paragraph 7, TUIR (Testo Unico delle Imposte sui Redditi -- DPR 917/1986) |
| Documentation regulation | Provvedimento No. 360494 (23 November 2020); Circular 15/2021; Circular 16/2022 |
| OECD member? | Yes |
| BEPS signatory? | Yes |
| Currency | EUR |
| Documentation language | Master File: English or Italian; Local File: Italian only (Ruling 174/2024) |
| Skill version | 1.0 |

## Section 2 -- Documentation Requirements

### 2.1 Master File (Documentazione di Gruppo)

**Master File (Documentazione di Gruppo)**

| Item | Detail |
| --- | --- |
| Required? | Optional (but required for penalty protection regime) |
| Format | Per Provvedimento 360494/2020, consistent with OECD Annex I to Chapter V |
| Language | English or Italian |
| Deadline | Electronically signed + timestamped by tax return filing deadline (with 90-day extension possible) |

### 2.2 Local File (Documentazione Nazionale)

**Local File (Documentazione Nazionale)**

| Item | Detail |
| --- | --- |
| Required? | Optional (but required for penalty protection regime) |
| Format | Per Provvedimento 360494/2020, consistent with OECD Annex II to Chapter V |
| Language | Italian only (clarified by Ruling 174/2024) |
| Deadline | Electronically signed + timestamped by tax return filing deadline |
| Submission on request | Within 20 days of official request; additional info within 7 days |

### 2.3 Penalty Protection Regime

To benefit from penalty protection, ALL conditions must be met:

1. Master File and Local File prepared per Provvedimento 360494/2020
2. Electronic signature with timestamp before tax return filing deadline (31 October for calendar year; 90-day extension available via amended return)
3. Flag ticked in the corporate tax return (Quadro RS)
4. Documentation presented to tax authorities during audit

Failure on any formal requirement (including the flag) may result in loss of penalty protection.

### 2.4 Country-by-Country Report (CbCR)

**Country-by-Country Report (CbCR)**

| Item | Detail |
| --- | --- |
| Threshold | Consolidated group revenue ≥ EUR 750 million |
| Filing deadline | 12 months after end of reporting FY |
| Filing method | Electronic to Agenzia delle Entrate |

## Section 3 -- Arm's Length Standard

### 3.1 Definition

- **Arm's length standard** — Components of income from transactions with non-resident related parties are evaluated based on the arm's length value -- the price that would have been agreed between independent enterprises operating under comparable conditions.  _(Article 110(7) TUIR)_

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

No strict hierarchy; most appropriate method applies. OECD Guidelines are the primary interpretive source.

## Section 4 -- Filing Obligations

**Filing Obligations**

| Obligation | Detail |
| --- | --- |
| Master/Local File | Not filed with return; maintained and presented within 20 days of audit request |
| Tax return flag | Tick penalty protection box in Quadro RS of IRES return |
| CbCR | Annual electronic filing |
| No separate TP return | TP information disclosed through documentation, not a standalone form |

## Section 5 -- Deadlines

**Deadlines**

| Item | Deadline |
| --- | --- |
| Tax return filing | 31 October (for calendar-year companies; extended by 15 days from 2024) |
| Documentation signing/timestamping | By tax return filing deadline |
| 90-day extension | Via filing amended return within 90 days of ordinary deadline |
| Documentation submission on audit request | 20 days |
| Additional information | 7 days from request |
| CbCR filing | 12 months after end of reporting FY |

## Section 6 -- Penalties

**Penalties**

| Scenario | Penalty |
| --- | --- |
| TP adjustment WITHOUT penalty protection | 70% of additional tax assessed (from 1 September 2024; previously 90-180%) |
| TP adjustment WITH valid penalty protection | No penalty on TP adjustment (interest still applies) |
| Failure to maintain documentation | Standard penalties for inadequate records |
| CbCR non-compliance | Administrative penalties per general provisions |

### Important Note on Penalty Reform

From violations committed from 1 September 2024 onward (i.e., FY2023 returns filed after September 2024), the penalty rate for TP adjustments without proper documentation is reduced to 70% of additional tax. For prior violations, the range was 90-180%.

## Section 7 -- Advance Pricing Agreements (APA)

**Advance Pricing Agreements (APA)**

| Item | Detail |
| --- | --- |
| Availability | Yes |
| Types | Unilateral, Bilateral, Multilateral |
| Governing legislation | Article 31-ter DPR 600/1973 |
| Application | To Agenzia delle Entrate, Direzione Centrale Grandi Contribuenti |
| Duration | 5 years prospective; rollback for up to 3 prior years possible |
| Fees | No formal application fee |
| Processing time | 12-24 months (unilateral); longer for bilateral |
| Annual compliance report | Required |

## Section 8 -- Safe Harbours

- **No formal safe harbours** — Italy does not have formal safe harbour provisions for transfer pricing.

**Safe Harbours table**

| Area | Status |
| --- | --- |
| Low-value intra-group services | No statutory safe harbour; OECD simplified approach may be accepted in practice |
| Interest rates | No formal safe harbour; market benchmarking required |
| General | All controlled transactions must be supported by arm's length analysis |
| Penalty protection | While not a "safe harbour" per se, the penalty protection regime provides certainty on penalty exposure |

### 8.1 Penalty Protection as Practical Safe Harbour

The Italian penalty protection regime functions as a practical substitute for safe harbours:
- Properly documented transactions enjoy zero penalty on adjustments
- This incentivises comprehensive documentation rather than simplified pricing rules
- Taxpayers must demonstrate they applied appropriate methods even if the result is later adjusted

### 8.2 Low-Value Intra-Group Services

- **Low-value intra-group services cost-plus mark-up** — While Italy has no formal rule, the Agenzia generally accepts: 5% cost-plus mark-up for routine/low-value services (consistent with OECD Chapter VII); This must still be supported by documentation demonstrating the services were actually rendered and the cost base is correct  _(OECD Chapter VII)_

## Section 9 -- Recent Developments

**Recent Developments**

| Date | Development |
| --- | --- |
| September 2024 | Penalty rate reduced to 70% (from 90-180%) for TP adjustments without documentation |
| August 2024 | Ruling 174/2024: Local File must be in Italian; Master File in English permitted |
| November 2020 | Provvedimento 360494/2020: current documentation structure established |
| 2024 | Pillar Two (GloBE) implementation for FYs from 31 Dec 2023 |
| 2024 | 90-day extension mechanism for documentation signing confirmed |
| Ongoing | Agenzia focus on intercompany financial transactions and IP arrangements |

## Section 10 -- Interaction with Other Skills

**Interaction with Other Skills**

| Related skill | Interaction |
| --- | --- |
| italy-bookkeeping | TP documentation relies on Italian accounting records; related-party disclosures |
| italy-corporate-tax (IRES/IRAP) | TP adjustments increase IRES and potentially IRAP tax base |
| italy-vat | TP adjustments may affect customs valuation for import VAT |
| CbCR | Used by Agenzia for risk-based audit targeting |
| Financial statements | Italian GAAP/IFRS related-party disclosures should align with TP positions |

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
