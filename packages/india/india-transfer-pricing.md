---
name: india-transfer-pricing
description: Use this skill whenever asked about India transfer pricing rules, documentation requirements, or CBDT transfer pricing compliance. Trigger on phrases like "transfer pricing India", "Indian TP documentation", "Form 3CEB", "master file India", "local file India", "CbCR India", "APA India", "Section 92", "safe harbour India", "specified domestic transactions", or any question about intercompany pricing for Indian entities.
version: 1.0
jurisdiction: IN
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: Mayur Deokar
review_status: current
depends_on:
  - transfer-pricing-workflow-base
category: transfer-pricing
tier: 1
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# India Transfer Pricing

## India Transfer Pricing Skill v1.0

## Verified rates & thresholds (accountant-reviewed)

Reviewed against the cited tax authorities by **Mayur Deokar** on 2026-06-06.
Items flagged for further clarification are tracked separately and excluded here.
This block is generated from verified `skill_facts` — edit the facts, not the prose.

### Transfer Pricing

- **Fee — unilateral** — INR 10 lakh  _(Rules 10F-10T)_
- **Fee — bilateral/multilateral** — INR 20 lakh  _(Rules 10F-10T)_
- **Duration** — 5 years prospective + 4 years rollback  _(ITA s 92CC)_
- **6+ comparables** — 35th to 65th percentile  _(Rule 10CA)_
- **< 6 comparables** — Arithmetic mean  _(Rule 10CA)_
- **Local File (Rule 10D)** — International transactions > INR 1 crore; or SDT > INR 20 crore  _(IT Rules r 10D)_
- **Master File (Form 3CEAA)** — Group revenue > INR 500 crore AND intl transactions > INR 50 crore or intangibles > INR 10 crore  _(IT Rules r 10DA)_
- **CbCR (Form 3CEAD)** — Group revenue > INR 6,400 crore  _(ITA s 286)_
- **Form 3CEB** — 31 October of AY  _(ITA s 92E)_
- **ITR (TP cases)** — 30 November of AY  _(ITA s 139)_
- **Master File** — 30 November of AY  _(IT Rules r 10DA)_
- **CbCR notification (Form 3CEAC)** — 2 months before CbCR deadline  _(ITA s 286)_
- **Failure to furnish Form 3CEB** — INR 1,00,000  _(ITA s 271BA)_
- **Failure to maintain TP docs** — 2% of transaction value  _(ITA s 271G)_
- **Failure to furnish Master File** — INR 5,00,000  _(ITA s 271AA(2))_
- **CbCR failure** — ₹5,000/day (1 mo); ₹15,000/day (beyond); ₹50,000/day (after order)  _(ITA s 286(6))_
- **Under-reporting (TP adjustment)** — 50% of tax; 200% if misreporting  _(ITA s 270A)_
- **IT/ITeS (≤ ₹200 Cr turnover)** — OP/OC ≥ 17%  _(Rule 10TD)_
- **IT/ITeS (> ₹200 Cr)** — OP/OC ≥ 18%  _(Rule 10TD)_
- **Contract R&D** — OP/OC ≥ 24%  _(Rule 10TD)_
- **Manufacturing (insignificant risk)** — OP/OC ≥ 12%  _(Rule 10TD)_
- **Corporate guarantee** — 1% p.a. (4% below investment grade)  _(Rule 10TD)_
- **Fee — unilateral** — INR 10 lakh  _(Rules 10F-10T)_
- **Fee — bilateral/multilateral** — INR 20 lakh  _(Rules 10F-10T)_
- **Duration (APA)** — 5 years prospective + 4 years rollback  _(ITA s 92CC)_
- **6+ comparables (Range Concept)** — 35th to 65th percentile  _(Rule 10CA)_
- **< 6 comparables (Range Concept)** — Arithmetic mean  _(Rule 10CA)_

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | India (Republic of India) |
| Tax authority | Central Board of Direct Taxes (CBDT); Transfer Pricing Officer (TPO) |
| Key TP legislation | Sections 92-92F, Income Tax Act, 1961; Rules 10A-10E, Income Tax Rules, 1962 |
| Documentation | Rule 10D (Local File); Rule 10DA (Master File); Section 286/Rule 10DB (CbCR) |
| Reporting | Section 92E / Form 3CEB (Accountant's Report) |
| OECD member? | No (but BEPS Inclusive Framework member) |
| BEPS signatory? | Yes (Inclusive Framework) |
| Currency | INR |
| Documentation language | English |
| Assessment Year (AY) basis | AY = FY + 1 (e.g., FY 2024-25 = AY 2025-26) |
| Skill version | 1.0 |

## Section 2 -- Documentation Requirements

### 2.1 Local File (Rule 10D Documentation)

**Local File (Rule 10D Documentation)**

| Item | Detail |
| --- | --- |
| Required? | Yes, for all entities with international transactions > INR 1 crore; or SDT > INR 20 crore |
| Format | Per Rule 10D: description of transactions, FAR analysis, method selection, comparables, financial data |
| Timing | Contemporaneous; maintained by income tax return due date |
| Retention | 8 years from end of relevant AY |

### 2.2 Master File (Form 3CEAA)

**Master File (Form 3CEAA)**

| Item | Detail |
| --- | --- |
| Required? | Yes, if: (a) consolidated group revenue > INR 500 crore AND (b) aggregate international transactions > INR 50 crore OR intangible transactions > INR 10 crore |
| Filing deadline | 30 November of AY (same as ITR due date for TP cases) |
| Content | Part A: group information, entity details; Part B: detailed master file per OECD standards |

### 2.3 Accountant's Report (Form 3CEB)

**Accountant's Report (Form 3CEB)**

| Item | Detail |
| --- | --- |
| Required? | Yes, for ALL entities with international transactions or specified domestic transactions (SDT) |
| Filed by | Independent Chartered Accountant |
| Deadline | 31 October of AY |
| Content | Certification that TP documentation maintained; details of each transaction, method, arm's length price |

### 2.4 Country-by-Country Report (Form 3CEAD)

**Country-by-Country Report (Form 3CEAD)**

| Item | Detail |
| --- | --- |
| Threshold | Consolidated group revenue > INR 6,400 crore (≈ EUR 750 million) |
| Filing deadline | 12 months after end of reporting accounting year of UPE |
| Notification | Form 3CEAC (identifying reporting entity): due 2 months before CbCR deadline |
| Content | Per OECD Annex III: jurisdiction-wise revenue, profit, tax, employees, assets |

## Section 3 -- Arm's Length Standard

### 3.1 Definition

- **Arm's length price definition** — Income from international transactions with associated enterprises shall be computed with regard to the arm's length price. Section 92B defines "international transaction" broadly.  _(Section 92(1))_

### 3.2 Accepted Methods (Section 92C)

**Accepted Methods (Section 92C)**

| Method | Accepted |
| --- | --- |
| Comparable Uncontrolled Price (CUP) | Yes |
| Resale Price Method (RPM) | Yes |
| Cost Plus Method (CPM) | Yes |
| Transactional Net Margin Method (TNMM) | Yes |
| Profit Split Method (PSM) | Yes |
| "Other Method" (including DCF) | Yes (sixth method, any method yielding most reliable result) |

### 3.3 Most Appropriate Method

- **Most Appropriate Method** — The most appropriate method considering the nature of transaction, functions/assets/risks, and availability of reliable data must be selected.  _(Rule 10C)_

### 3.4 Range Concept

- **Range Concept** — For datasets with 6+ comparable data points: arm's length range is the 35th to 65th percentile. For fewer than 6: arithmetic mean applies.

## Section 4 -- Filing Obligations

**Filing Obligations**

| Obligation | Detail |
| --- | --- |
| Form 3CEB (Accountant's Report) | Annual electronic filing; 31 October |
| Local File (Rule 10D) | Maintain; provide within 30 days of request |
| Master File (Form 3CEAA) | Annual electronic filing; 30 November |
| CbCR notification (Form 3CEAC) | Annual; 2 months before CbCR deadline |
| CbCR (Form 3CEAD) | Annual; 12 months after UPE's year-end |
| Income Tax Return | 30 November (for TP cases) |

## Section 5 -- Deadlines

**Deadlines**

| Item | Deadline |
| --- | --- |
| Form 3CEB filing | 31 October of AY |
| Income Tax Return (TP cases) | 30 November of AY |
| Local File maintenance | By ITR due date (30 November) |
| Provision on TPO request | Within 30 days |
| Master File (Form 3CEAA) | 30 November of AY |
| CbCR notification (Form 3CEAC) | 2 months before CbCR due date |
| CbCR (Form 3CEAD) | 12 months after end of UPE's reporting year |

## Section 6 -- Penalties

**Penalties**

| Offence | Section | Penalty |
| --- | --- | --- |
| Failure to furnish Form 3CEB | 271BA | INR 1,00,000 (INR 1 lakh) |
| Failure to maintain/furnish TP documentation | 271G | 2% of value of each international/SDT transaction |
| Failure to report or incorrect reporting | 271AA(1) | 2% of value of each transaction |
| Failure to furnish Master File | 271AA(2) | INR 5,00,000 (INR 5 lakh) |
| Failure to furnish CbCR (Form 3CEAD) | 286(6) | INR 5,000/day (up to 1 month); INR 15,000/day beyond 1 month; INR 50,000/day after penalty order |
| Inaccurate CbCR | 286(7) | INR 5,00,000 |
| Under-reporting of income (TP adjustment) | 270A | 50% of tax on under-reported income; 200% if misreporting |

## Section 7 -- Advance Pricing Agreements (APA)

**Advance Pricing Agreements (APA)**

| Item | Detail |
| --- | --- |
| Availability | Yes (active program since 2012) |
| Types | Unilateral, Bilateral, Multilateral |
| Governing legislation | Section 92CC-92CD ITA; Rule 10F-10T |
| Application | To CBDT; Form 3CED with prescribed fee |
| Fees | INR 10 lakh (unilateral); INR 20 lakh (bilateral/multilateral) |
| Duration | 5 years prospective |
| Rollback | Available for 4 prior AYs (subject to conditions) |
| Processing time | Unilateral: 12-18 months; Bilateral: 24-48 months |
| Annual compliance report | Required (Form 3CEF) |
| Safe Harbour interaction | Separate from APA program |

## Section 8 -- Safe Harbours

India has formal Safe Harbour Rules (Rule 10TD-10TG):

**Safe Harbours table**

| Transaction Type | Safe Harbour Margin/Rate |
| --- | --- |
| IT/ITeS services (turnover ≤ INR 200 crore) | Operating profit/operating cost ≥ 17% (to AE) or 17% (non-AE) |
| IT/ITeS services (turnover > INR 200 crore) | Operating profit/operating cost ≥ 18% |
| KPO services (turnover ≤ INR 200 crore) | Operating profit/operating cost ≥ 18% |
| KPO services (turnover > INR 200 crore) | Operating profit/operating cost ≥ 18% |
| Contract R&D (wholly/partly) | Operating profit/operating cost ≥ 24% |
| Manufacturing with insignificant risk | Operating profit/operating cost ≥ 12% |
| Intra-group loans (INR) | 1-year MCLR + 175 bps (capped at INR 100 crore) |
| Intra-group loans (Foreign currency) | 6-month SOFR + relevant spread |
| Corporate guarantee | 1% per annum (or 4% for associated enterprises with below investment grade) |

- **Safe Harbour application** — Application via Form 3CEFA; election by ITR due date.

## Section 9 -- Recent Developments

**Recent Developments**

| Date | Development |
| --- | --- |
| 2025 | Income-tax Act, 2025 (new code) receives assent; TP framework carried forward |
| 2026 | Form 3CEB proposed to be replaced by Form 48 (data-rich, machine-readable format) |
| 2025-26 | New Income-tax Rules, 2026 introduce graded penalties for delayed accountant's reports |
| 2024 | Safe Harbour Rules updated thresholds and rates |
| 2024 | Continued high volume of APA completions |
| Ongoing | India actively participating in BEPS Pillar One/Two discussions |
| Ongoing | Block assessment scheme introduced from Tax Year 2026-27 |
| 2021 | CbCR threshold revised to INR 6,400 crore (from INR 5,500 crore) |

## Section 10 -- Interaction with Other Skills

**Interaction with Other Skills**

| Related skill | Interaction |
| --- | --- |
| india-corporate-tax | TP adjustments directly affect taxable income under ITA |
| india-gst | TP adjustments may affect valuation for GST on related-party transactions |
| india-bookkeeping | Indian accounting records (Ind-AS/Indian GAAP) support TP documentation |
| Specified Domestic Transactions | SDT rules (Section 92BA) apply TP provisions to certain domestic related-party transactions |
| Form 3CEB | Gateway filing; triggers TP audit jurisdiction |
| CbCR | Used by CBDT for risk-based audit selection and case referral to TPO |

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
