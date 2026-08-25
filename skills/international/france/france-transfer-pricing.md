---
name: france-transfer-pricing
description: Use this skill whenever asked about France transfer pricing rules, documentation requirements, or prix de transfert compliance. Trigger on phrases like "transfer pricing France", "French TP documentation", "prix de transfert", "master file France", "local file France", "CbCR France", "APA France", "Article L.13 AA", "Form 2257-SD", or any question about intercompany pricing for French entities.
version: 1.0
jurisdiction: FR
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - transfer-pricing-workflow-base
category: transfer-pricing
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# France Transfer Pricing

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | France (French Republic) |
| Tax authority | Direction Générale des Finances Publiques (DGFiP) |
| Key TP legislation | Articles L.13 AA, L.13 AB, L.13 B of the French Tax Procedure Code (FTPC); Article 57 of the General Tax Code (CGI) |
| Reporting | Form 2257-SD (simplified TP return); Article 223 quinquies B CGI |
| OECD member? | Yes |
| BEPS signatory? | Yes |
| Effective date (EUR 150m threshold) | FYs opened from 1 January 2024 |
| Currency | EUR |
| Documentation language | French (translation required on request) |
| Skill version | 1.0 |

## Section 2 -- Documentation Requirements

### 2.1 Master File

**Master File**

| Item | Detail |
| --- | --- |
| Required? | Yes, under Article L.13 AA FTPC |
| Threshold | Annual turnover (excl. tax) or gross assets ≥ EUR 150 million (from FY 2024; previously EUR 400 million) |
| Format | Consistent with OECD Annex I to Chapter V |
| Filing | Available on first day of tax audit; or within 30 days of formal notice |

### 2.2 Local File

**Local File**

| Item | Detail |
| --- | --- |
| Required? | Yes, under Article L.13 AA FTPC |
| Threshold | Same EUR 150 million threshold |
| Transaction threshold | Transactions exceeding EUR 100,000 per category must be documented in detail |
| Format | Consistent with OECD Annex II to Chapter V |
| Filing | Available on first day of audit; or within 30 days of formal notice |

### 2.3 Simplified TP Return (Form 2257-SD)

**Simplified TP Return (Form 2257-SD)**

| Item | Detail |
| --- | --- |
| Threshold | Annual turnover or gross assets ≥ EUR 400 million; OR entity >50% held by such company; OR entity holding >50% of such company |
| Content | Simplified version of master/local file: group info, transactions, methods |
| Filing | Within 6 months of corporate tax return filing deadline |

### 2.4 Country-by-Country Report (CbCR)

**Country-by-Country Report (CbCR)**

| Item | Detail |
| --- | --- |
| Threshold | Consolidated group revenue ≥ EUR 750 million |
| Filing deadline | 12 months after end of reporting FY |
| Legislation | Article 223 quinquies C CGI |
| Filing method | Electronic |

## Section 3 -- Arm's Length Standard

### 3.1 Definition

- **Arm's length principle (Article 57 CGI)** — Article 57 CGI: Where a French enterprise transfers profits to a related foreign entity through price manipulation, management fees, or any other means, the transferred profits are added back to taxable income. The arm's length principle applies per OECD Guidelines.  _(Article 57 CGI)_

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

- **Preferred method** — No statutory hierarchy. Most appropriate method principle applies. In practice, CUP is preferred where available; TNMM is most commonly used.

### 3.4 Finance Act 2024 Presumption

- **Finance Act 2024 presumption** — From 2024, TP documentation is "enforceable" -- if the method used by the company in practice differs from the method documented, there is a presumption of indirect profit transfer that the taxpayer must rebut.

## Section 4 -- Filing Obligations

**Filing Obligations**

| Obligation | Detail |
| --- | --- |
| Master File / Local File | Maintained; presented on first day of audit or within 30 days of formal notice |
| Form 2257-SD | Annual filing (entities ≥ EUR 400m threshold) |
| CbCR | Annual electronic filing |
| Corporate tax return | Standard CIT return (no separate TP section beyond 2257-SD) |

## Section 5 -- Deadlines

**Deadlines**

| Item | Deadline |
| --- | --- |
| Master/Local File preparation | Must be available at start of tax audit |
| Response to formal notice | 30 days (extensions possible in exceptional cases) |
| Form 2257-SD filing | 6 months after CIT return filing deadline |
| CbCR filing | 12 months after end of reporting FY |
| Corporate tax return | Within 4 months of FY-end (May 15 for calendar year companies) |

## Section 6 -- Penalties

**Penalties**

| Offence | Penalty |
| --- | --- |
| Failure to produce documentation after formal notice | Higher of: 0.5% of undocumented transaction value OR 5% of TP adjustment; minimum EUR 50,000 per audited FY (increased from EUR 10,000 in 2024) |
| Late filing of Form 2257-SD | EUR 150 |
| Errors/omissions in Form 2257-SD | EUR 15 per item; minimum EUR 60, maximum EUR 10,000 |
| Late/missing CbCR | Maximum EUR 100,000 |
| Failure under Article L.13 B (general TP information request) | EUR 10,000 per tax year |
| TP adjustment | Standard 40% penalty for bad faith; 80% for abuse of law |

## Section 7 -- Advance Pricing Agreements (APA)

**Advance Pricing Agreements (APA)**

| Item | Detail |
| --- | --- |
| Availability | Yes |
| Types | Unilateral, Bilateral, Multilateral |
| Governing authority | DGFiP / Service de la Sécurité Juridique et du Contrôle Fiscal (SJCF) |
| Application fee | No formal fee |
| Typical duration | 3-5 years prospective; rollback possible |
| Processing time | 18-36 months |
| Annual compliance report | Required |
| MAP available | Yes, under applicable tax treaties |

## Section 8 -- Safe Harbours

- **General principle** — France does not have general statutory safe harbour rules for transfer pricing.

**Safe Harbours table**

| Area | Status |
| --- | --- |
| Low-value intra-group services | No formal safe harbour; OECD simplified approach (5% cost-plus) accepted in practice |
| Interest rates | No safe harbour; market rate benchmarking required |
| Thin capitalisation | Separate rules under Article 212 CGI (debt-to-equity ratio of 1.5:1) |
| Small transactions | Transactions below EUR 100,000 per category need not be individually documented in Local File |
| General principle | France explicitly states it has no general safe harbour provisions |

### 8.1 Thin Capitalisation (Article 212 CGI)

- **Thin capitalisation framework** — While not a safe harbour per se, France's thin capitalisation rules provide a framework: - Debt-to-equity ratio: 1.5:1 - Interest rate cap: related-party loan interest capped at market reference rate - Interest coverage: net interest deduction limited to 25% of EBITDA (from 2019, ATAD transposition) These interact with but are separate from TP analysis.  _(Article 212 CGI)_

## Section 9 -- Recent Developments

**Recent Developments**

| Date | Development |
| --- | --- |
| January 2024 | EUR 150m documentation threshold (down from EUR 400m) -- significantly expands scope |
| January 2024 | Minimum penalty for documentation failure raised to EUR 50,000 (from EUR 10,000) |
| January 2024 | TP documentation made "enforceable" with presumption of indirect profit transfer |
| 2024 | Pillar Two (GloBE) implemented for FYs from 31 Dec 2023 |
| Ongoing | Increased DGFiP focus on intercompany financial transactions and intangibles |
| Ongoing | OECD Amount B: France actively monitoring |

## Section 10 -- Interaction with Other Skills

**Interaction with Other Skills**

| Related skill | Interaction |
| --- | --- |
| france-bookkeeping | Related-party disclosures; accounting records support TP documentation |
| france-corporate-tax | TP adjustments under Art. 57 CGI directly affect CIT base |
| france-vat | TP adjustments may affect customs valuation |
| Thin capitalisation | Art. 212 CGI limits interact with TP on intercompany loans |
| CbCR | Used by DGFiP for risk-based audit selection |

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
