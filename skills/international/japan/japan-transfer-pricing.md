---
name: japan-transfer-pricing
description: Use this skill whenever asked about Japan transfer pricing rules, documentation requirements, or 移転価格税制 compliance. Trigger on phrases like "transfer pricing Japan", "Japanese TP documentation", "移転価格", "master file Japan", "local file Japan", "CbCR Japan", "APA Japan", "Article 66-4 ASMT", "NTA transfer pricing", or any question about intercompany pricing for Japanese entities.
version: 1.0
jurisdiction: JP
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on: - transfer-pricing-workflow-base
category: transfer-pricing
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Japan Transfer Pricing

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Japan |
| Tax authority | National Tax Agency (NTA -- 国税庁) |
| Key TP legislation | Article 66-4, Act on Special Measures concerning Taxation (ASMT -- 租税特別措置法) |
| Documentation | Articles 66-4 (Local File), 66-4-4 (CbCR), 66-4-5 (Master File) ASMT |
| Administrative guidance | Commissioner's Directive on the Operation of Transfer Pricing (CDOTP) |
| OECD member? | Yes |
| BEPS signatory? | Yes |
| Effective date (three-tier) | FYs beginning on/after 1 April 2016 (CbCR/Master File); 1 April 2017 (Local File contemporaneous requirement) |
| Currency | JPY |
| Documentation language | Japanese or English (Master File/CbCR in English; Local File preferably Japanese) |
| Skill version | 1.0 |

## Section 2 -- Documentation Requirements

### 2.1 Master File (マスターファイル)

**Master File**

| Item | Detail |
| --- | --- |
| Required? | Yes, where consolidated group revenue of UPE ≥ JPY 100 billion (≈ EUR 750m) in prior FY |
| Format | OECD Annex I to Chapter V |
| Language | Japanese or English |
| Filing | Electronic submission to competent District Director within 1 year after UPE's FY-end |
| Penalty for non-submission | Fine up to JPY 300,000 |

### 2.2 Local File (ローカルファイル)

**Local File**

| Item | Detail |
| --- | --- |
| Required? | Yes -- contemporaneous preparation required where thresholds met |
| Thresholds for contemporaneous preparation | Transactions ≥ JPY 5 billion (tangible); OR intangible transactions ≥ JPY 300 million |
| Preparation deadline | By final tax return filing due date |
| Retention | 7 years |
| Submission | On request during tax examination; within appointed period |
| Penalty for non-submission | No monetary penalty, but tax authorities may use estimation (secret comparables) |

### 2.3 Below-Threshold Transactions

- **Below-threshold Local File handling** — For transactions below JPY 5 billion / JPY 300 million, contemporaneous Local File preparation is not legally required, but documentation is strongly recommended. Without it, tax authorities can: Use estimated taxation methods; Apply secret comparables

### 2.4 Country-by-Country Report (CbCR -- 国別報告書)

**CbCR**

| Item | Detail |
| --- | --- |
| Threshold | UPE consolidated revenue ≥ JPY 100 billion (prior FY) |
| Filing deadline | Within 1 year after UPE's FY-end |
| Filing method | Electronic (e-Tax) to competent District Director |
| Notification (NUPE) | Japanese constituent entities must notify the District Director of UPE identity |
| Notification deadline | By last day of UPE's FY |
| Penalty for late CbCR | Fine up to JPY 300,000 |

## Section 3 -- Arm's Length Standard

### 3.1 Definition

- **Arm's length standard definition** — Article 66-4(1) ASMT: Where the price of a transaction between a corporation and a foreign related party differs from the arm's length price, the corporation's taxable income is computed using the arm's length price.  _(Article 66-4(1) ASMT)_

### 3.2 Accepted Methods

**Accepted Methods**

| Method | Japanese Term | Accepted |
| --- | --- | --- |
| Comparable Uncontrolled Price | 独立価格比準法 (CUP) | Yes |
| Resale Price Method | 再販売価格基準法 (RPM) | Yes |
| Cost Plus Method | 原価基準法 (CPM) | Yes |
| Transactional Net Margin Method | 取引単位営業利益法 (TNMM) | Yes |
| Profit Split Method | 利益分割法 (PSM) | Yes |
| Residual Profit Split | 残余利益分割法 | Yes |
| Discounted Cash Flow | DCF法 | Yes (for hard-to-value intangibles) |

### 3.3 Preferred Method

- **Preferred method principle** — The "most appropriate method" principle applies. Article 66-4(2) provides the methods in order but the NTA applies the best method rule consistent with OECD Guidelines.  _(Article 66-4(2))_

### 3.4 Estimation by Tax Authorities

- **Estimation by tax authorities** — If taxpayer does not provide Local File documentation within the specified period, tax authorities can: Use secret comparables (data not available to taxpayer); Estimate taxable income to taxpayer's disadvantage

## Section 4 -- Filing Obligations

**Filing Obligations**

| Obligation | Detail |
| --- | --- |
| Local File | Contemporaneous preparation (if thresholds met); submit on request during audit |
| Master File | Electronic filing within 1 year of UPE FY-end |
| CbCR | Electronic filing within 1 year of UPE FY-end |
| NUPE notification | By last day of UPE's FY |
| Corporate tax return | Annual self-assessment (no separate TP form) |
| TP-related schedule | Supplementary schedule for related-party transactions (別表17(4)) |

## Section 5 -- Deadlines

**Deadlines**

| Item | Deadline |
| --- | --- |
| Local File preparation | By final tax return filing due date (2 months after FY-end; extension to 3 months available) |
| Local File submission on audit | Within period appointed by tax examiner (typically 45-60 days) |
| Master File submission | Within 1 year after UPE's FY-end |
| CbCR submission | Within 1 year after UPE's FY-end |
| NUPE notification | Last day of UPE's FY |
| Corporate tax return | 2 months after FY-end (extension to 3 months; additional month for e-filing) |

## Section 6 -- Penalties

**Penalties**

| Offence | Penalty |
| --- | --- |
| Late/missing Master File submission | Fine up to JPY 300,000 |
| Late/missing CbCR submission | Fine up to JPY 300,000 |
| Late/missing NUPE notification | Fine up to JPY 300,000 |
| Failure to submit Local File on request | No direct monetary penalty; triggers estimation/secret comparables |
| TP adjustment | Additional tax + interest; no specific TP surcharge but underpayment penalties apply |
| Concealment/fraud penalties | 35-40% additional tax for deliberate underpayment |

## Section 7 -- Advance Pricing Agreements (APA)

**Advance Pricing Agreements**

| Item | Detail |
| --- | --- |
| Availability | Yes (one of the most active APA programs globally) |
| Types | Unilateral, Bilateral, Multilateral |
| Governing authority | NTA (Mutual Agreement Division and regional tax offices) |
| Application | To District Director; pre-filing consultation recommended |
| Duration | 3-5 years prospective; rollback to prior open years possible |
| Fees | No application fee |
| Processing time | Unilateral: 12-24 months; Bilateral: 24-36 months |
| Annual compliance report | Required |
| Statistics | Japan processes one of the highest volumes of APAs globally (~130-150/year) |

## Section 8 -- Safe Harbours

- **Safe harbours overview** — Japan does not have broad formal safe harbour rules for transfer pricing.

## Section 8 -- Safe Harbours

**Safe Harbours**

| Area | Detail |
| --- | --- |
| Low-value intra-group services | No statutory safe harbour; OECD simplified approach may be applied |
| Documentation thresholds | Below JPY 5bn/JPY 300m: no mandatory contemporaneous Local File (but documentation recommended) |
| Small-scale transactions | NTA exercises administrative discretion for immaterial transactions |
| SSA (Simplified and Streamlined Approach) | Japan has NOT implemented Amount B / SSA as of 2025 |

## Section 9 -- Recent Developments

**Recent Developments**

| Date | Development |
| --- | --- |
| 2025 | NTA FAQ on Simplified and Streamlined Approach (SSA): confirms Japan has NOT adopted Amount B |
| 2024 | Continued high volume of APAs; bilateral APAs with US, UK, China remain active |
| 2024 | Pillar Two (GloBE) implementation via domestic legislation |
| 2023 | NTA enhanced focus on digital economy and intangible transactions |
| 2017 | Contemporaneous Local File requirement introduced (JPY 5bn/300m thresholds) |
| 2016 | Three-tier documentation (Master File, CbCR) introduced |
| Ongoing | Active participation in OECD BEPS developments; MAP inventory management |

## Section 10 -- Interaction with Other Skills

**Interaction with Other Skills**

| Related skill | Interaction |
| --- | --- |
| japan-bookkeeping | TP documentation builds on J-GAAP/IFRS accounting records |
| japan-corporate-tax | TP adjustments affect corporation tax (法人税) base |
| japan-consumption-tax | TP adjustments may affect customs value and consumption tax |
| Thin capitalisation | Interest limitation rules under Art. 66-5 ASMT interact with TP for loans |
| CbCR | Used by NTA for risk-based audit selection |
| PE profit attribution | Related TP methodology applies to permanent establishment profits |

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
