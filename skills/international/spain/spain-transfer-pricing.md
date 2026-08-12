---
name: spain-transfer-pricing
description: Use this skill whenever asked about Spain transfer pricing rules, documentation requirements, or precios de transferencia compliance. Trigger on phrases like "transfer pricing Spain", "Spanish TP documentation", "precios de transferencia", "master file Spain", "local file Spain", "CbCR Spain", "APA Spain", "Model 232", "AEAT transfer pricing", or any question about intercompany pricing for Spanish entities.
version: 1.0
jurisdiction: ES
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on: - transfer-pricing-workflow-base
category: transfer-pricing
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Spain Transfer Pricing

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Spain (Kingdom of Spain) |
| Tax authority | Agencia Estatal de Administración Tributaria (AEAT) |
| Key TP legislation | Article 18, Corporate Income Tax Law (Ley del Impuesto sobre Sociedades -- CITL); Royal Decree 634/2015 (CIT Regulations), Articles 13-16 |
| OECD member? | Yes |
| BEPS signatory? | Yes |
| Currency | EUR |
| Documentation language | Spanish |
| Skill version | 1.0 |

## Section 2 -- Documentation Requirements

### 2.1 Master File

**Master File**

| Item | Detail |
| --- | --- |
| Required? | Yes, for groups with net turnover > EUR 45 million |
| Format | BEPS Action 13 / OECD Annex I to Chapter V |
| Filing | Available at disposal of AEAT from end of voluntary filing period |
| Simplified regime | Below EUR 45m: simplified local file applies |

### 2.2 Local File

**Local File**

| Item | Detail |
| --- | --- |
| Required? | Yes, for related-party transactions > EUR 250,000 per party per year (per transaction type) |
| Format | BEPS Action 13 / OECD Annex II to Chapter V |
| Filing | Available at disposal of AEAT from end of voluntary filing period |
| Content | Economic analysis, comparables, method selection, financial data |

### 2.3 Model 232 (Informative Declaration)

**Model 232**

| Item | Detail |
| --- | --- |
| Required? | Yes, where thresholds exceeded |
| Key thresholds | >EUR 250,000 market value with same related party; >EUR 100,000 for "specific transactions" |
| Specific transactions | Transactions with tax haven entities, transactions involving intangibles, professional services, etc. |
| Filing deadline | Month following the ten-month period after FY-end (e.g., 30 November for calendar year companies) |

### 2.4 Country-by-Country Report (CbCR -- Model 231)

**CbCR Model 231**

| Item | Detail |
| --- | --- |
| Threshold | Consolidated group revenue ≥ EUR 750 million |
| Filing deadline | 12 months after end of FY |
| Filing method | Electronic (Model 231) |

## Section 3 -- Arm's Length Standard

### 3.1 Definition

- **Arm's length standard** — Transactions between related parties must be valued at their market value -- the value that would have been agreed between independent parties under comparable circumstances.  _(Article 18.1 CITL)_

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

- **Preferred method** — No statutory hierarchy, but Article 18.4 CITL establishes a preference for CUP where applicable. Most appropriate method principle generally applies.  _(Article 18.4 CITL)_

### 3.4 AEAT Position

- **Secret comparables prohibited** — AEAT is not permitted to use "secret comparables" -- all comparables must be disclosed to the taxpayer.

## Section 4 -- Filing Obligations

**Filing Obligations**

| Obligation | Detail |
| --- | --- |
| Master File | Maintain; available to AEAT from end of voluntary filing period |
| Local File | Maintain; available to AEAT from end of voluntary filing period |
| Model 232 | Annual informative filing |
| Model 231 (CbCR) | Annual filing |
| Corporate tax return (Model 200) | Annual; includes related-party transaction disclosure |

## Section 5 -- Deadlines

**Deadlines**

| Item | Deadline |
| --- | --- |
| Documentation preparation | By end of voluntary corporate tax filing period |
| Model 232 filing | Month following 10 months after FY-end (November 30 for calendar year) |
| Model 231 (CbCR) | 12 months after end of FY |
| Corporate tax return (Model 200) | 25 days following 6 months after FY-end (July 25 for calendar year) |

## Section 6 -- Penalties

### 6.1 No TP Adjustment by AEAT

**No TP Adjustment penalties**

| Offence | Penalty |
| --- | --- |
| Failure/incomplete documentation | EUR 1,000 per data item; EUR 10,000 per set of data |
| Cap | Lower of: 10% of aggregate related-party transaction value OR 1% of net revenue |

### 6.2 With TP Adjustment by AEAT

**With TP Adjustment penalties**

| Offence | Penalty |
| --- | --- |
| Documentation failure + adjustment | 15% of the adjustment amount (additional to tax + interest) |
| Transactions with non-cooperative jurisdictions | 20% of the adjustment amount |

### 6.3 Model 232 Penalties

**Model 232 Penalties**

| Offence | Penalty |
| --- | --- |
| Late/incorrect filing | EUR 20 per omitted data item; minimum EUR 300, maximum EUR 20,000 |

## Section 7 -- Advance Pricing Agreements (APA)

**Advance Pricing Agreements**

| Item | Detail |
| --- | --- |
| Availability | Yes |
| Types | Unilateral, Bilateral, Multilateral |
| Governing legislation | Article 18.9 CITL; Articles 21-29 CIT Regulations |
| Application | To AEAT; must include proposed methodology and comparables |
| Duration | Up to 4 years prospective; prior years may be included |
| Fees | No formal fee |
| Processing time | Variable; historically lengthy but improving |
| Annual compliance report | Required |
| Binding | Binding on AEAT for covered period |

## Section 8 -- Safe Harbours

Spain has very limited safe harbour provisions:

## Section 8 -- Safe Harbours

**Safe Harbours**

| Area | Detail |
| --- | --- |
| Professional partnerships (Art. 18.6 CITL) | Safe harbour where ≥75% of income allocated to partners, subject to conditions (company has resources; >75% from professional activities) |
| Low-value intra-group services | No formal safe harbour; 5% cost-plus benchmark approach may be applied but doesn't exempt from analysis |
| General transactions | No safe harbour; all must be at arm's length with supporting analysis |
| Interest rates | No safe harbour; arm's length market rate must be demonstrated |

### 8.1 Professional Partnerships Safe Harbour (Art. 18.6)

- **Professional partnerships safe harbour conditions** — This is Spain's only formal safe harbour: Entity allocates ≥75% of income to professional partners; Entity has human and material resources to carry out the work; More than 75% of income comes from professional activities; When conditions met: transaction deemed valued at market value without further analysis required  _(Art. 18.6 CITL)_

### 8.2 No General Safe Harbours

- **No general safe harbours** — Spain explicitly does not publish TP safe harbours, norms, or deemed margins. AEAT insists on case-by-case arm's length analysis based on facts and circumstances. Secret comparables are not permitted.

## Section 9 -- Recent Developments

**Recent Developments**

| Date | Development |
| --- | --- |
| 2024 | Pillar Two (GloBE) implemented via transposition of EU Minimum Tax Directive |
| FY2025 | Public CbCR requirement expected (EU directive transposition) |
| 2024 | AEAT increased TP audit activity, particularly on intangibles and financial transactions |
| Ongoing | OECD Pillar One Amount B: Spain monitoring implementation |
| 2022 | Model 232 thresholds and instructions updated |
| Ongoing | Spain does not publish TP safe harbours or norms; case-by-case approach |

## Section 10 -- Interaction with Other Skills

**Interaction with Other Skills**

| Related skill | Interaction |
| --- | --- |
| spain-bookkeeping | TP documentation supported by PGC accounting records; related-party disclosures |
| spain-corporate-tax | TP adjustments under Art. 18 directly affect CIT (Impuesto sobre Sociedades) base |
| spain-vat | TP adjustments may affect customs valuation |
| Model 232 | Annual informative obligation separate from but related to TP documentation |
| CbCR (Model 231) | Global risk assessment used by AEAT for audit selection |

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
