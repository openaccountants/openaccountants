---
name: malta-transfer-pricing
description: 'Use this skill whenever asked about Malta transfer pricing rules, documentation requirements, or arm''s length pricing for cross-border related-party transactions. Trigger on phrases like "transfer pricing Malta", "TP documentation", "master file Malta", "local file Malta", "arm''s length Malta", "related party transactions Malta", "CbCR Malta", "country-by-country report Malta", "BEPS Malta", "intercompany pricing Malta", or any question about transfer pricing compliance for Maltese entities within multinational groups. Covers basis year 2026: the Transfer Pricing Rules (S.L. 123.207) and the MTCA guidelines, the EUR 6,000,000 revenue and EUR 20,000,000 capital exceptions, grandfathering of pre-2024 arrangements, master file and local file on request, the TRA 135 attachment to the YA 2026 company return, unilateral rulings and APAs.'
version: 1.1
jurisdiction: MT
tax_year: 2026
last_updated: 2026-10-23
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - transfer-pricing-workflow-base
category: transfer-pricing
tier: 2
verified_by: pending
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Malta Transfer Pricing

Source-cited draft: not reviewed by an accountant. Built by Michael Cutajar and the OpenAccountants team.

Tax year: basis year 2026 (year of assessment 2027). Company tax computation is in [mt-corporate-tax](mt-corporate-tax.md).

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Malta (Republic of Malta) |
| Tax authority | Commissioner for Tax and Customs (MTCA) |
| Key TP legislation | Transfer Pricing Rules, S.L. 123.207 (Legal Notice 284 of 2022), read with the MTCA Guidelines in relation to the Transfer Pricing Rules |
| Enabling provision | Article 51A, Income Tax Act (Chapter 123) |
| OECD member? | No (enhanced engagement partner) |
| BEPS signatory? | Yes (Inclusive Framework member; MLI signatory) |
| Effective date | Basis years commencing on or after 1 January 2024. Time-limited grandfathering for arrangements entered into before 1 January 2024 that are not materially altered on or after that date (Rule 1(2)) |
| Currency | EUR |
| Documentation language | English or Maltese |
| Tax year | Basis year 2026 |
| Skill version | 1.1 |

## Section 2 -- Documentation Requirements

### 2.1 Master File

**Master File**

| Item | Detail |
| --- | --- |
| Required? | Yes, where thresholds met |
| Format | OECD Annex I to Chapter V of the TP Guidelines |
| Filing | Not filed annually; made available on MTCA request within a reasonable timeframe, in English or Maltese |
| Retention period | Part of the record-keeping duty in Article 19(1) ITMA. The Article 19(5) ITMA time limit runs from the end of the period the arrangement refers to, or the date of the arrangement, whichever is later. The skill previously said 9 years; that figure is not re-checked against Article 19(5) here |

### 2.2 Local File

**Local File**

| Item | Detail |
| --- | --- |
| Required? | Yes, where thresholds met |
| Format | OECD Annex II to Chapter V of the TP Guidelines |
| Filing | Not filed annually; made available on MTCA request within a reasonable timeframe, in English or Maltese |
| Retention period | As for the master file |

### 2.3 Low-Value-Adding Intra-Group Services

A taxpayer that uses the simplified approach for low-value-adding intra-group services prepares the information in Chapter VII of the OECD Transfer Pricing Guidelines and makes it available on request (MTCA guidelines, Rule 6(ii)).

### 2.4 Country-by-Country Report (CbCR)

**Country-by-Country Report (CbCR)**

| Item | Detail |
| --- | --- |
| Threshold | Consolidated group revenue ≥ EUR 750 million |
| Filing deadline | Within 12 months of the end of the reporting FY |
| Filing method | Electronic, to Commissioner for Tax and Customs |

### 2.5 Exceptions (Rule 9)

The Rules do not apply to transactions in a financial period where, in that period, BOTH of these aggregates stay at or below the limit. If EITHER limit is exceeded, the Rules apply. (Version 1.0 of this skill said both had to be exceeded; that was wrong.)

**De Minimis Thresholds**

| Criterion | Threshold |
| --- | --- |
| Revenue items (aggregate arm's length value of all cross-border P&L items) | EUR 6,000,000 |
| Capital items (aggregate arm's length value of all cross-border B/S items) | EUR 20,000,000 |

Dividends paid to an associated enterprise are left out of the revenue aggregate; distributions in kind may need to be considered. If a long-running arrangement first crosses a limit in a later year, documentation (including the intercompany agreement) is needed from that year (MTCA guidelines, Example 4).

### 2.6 Scope of Application

**Scope of Application**

| Criterion | Detail |
| --- | --- |
| Relationship test (general) | >75% direct/indirect participating rights (not re-checked against the Rule text in this update) |
| Relationship test (MNE constituents) | >50% participating rights (not re-checked against the Rule text in this update) |
| Entities out of scope | SMEs as defined in EU State Aid Rules (not re-checked against the Rule text in this update) |
| Transaction type | Cross-border arrangements only (domestic transactions not in scope) |

## Section 3 -- Arm's Length Standard

### 3.1 Definition

- **Arm's length amount**: The arm's length amount is the consideration that would have been agreed between independent parties dealing at arm's length in comparable circumstances.

### 3.2 Accepted Methods

Malta follows OECD TP Guidelines. All five OECD methods are accepted:

**Accepted Methods**

| Method | Type |
| --- | --- |
| Comparable Uncontrolled Price (CUP) | Traditional transaction |
| Resale Price Method (RPM) | Traditional transaction |
| Cost Plus Method (CPM) | Traditional transaction |
| Transactional Net Margin Method (TNMM) | Transactional profit |
| Transactional Profit Split Method (PSM) | Transactional profit |

### 3.3 Preferred Method

- **Preferred Method**: The preferred methods are those in Chapter II of the OECD Transfer Pricing Guidelines (2022 edition). Other methods may be accepted under paragraph 2.9 of those Guidelines. One method is generally enough; in complex cases evidence from several methods may be used together (MTCA guidelines, Rule 5).

### 3.4 Interaction with notional interest deduction

The Transfer Pricing Rules apply first, then the Notional Interest Deduction Rules (S.L. 123.176). If the Rules price a nominally interest-free loan at an arm's length rate, that loan is no longer risk capital for the notional interest deduction (MTCA guidelines, Rule 3, Example 1).

## Section 4 -- Filing Obligations

**Filing Obligations**

| Obligation | Detail |
| --- | --- |
| TP return / declaration | No separate TP return required |
| Annual filing of documentation | No; documentation must be maintained and available on request |
| Attachment to corporate tax return | Yes, from the YA 2026 company return: MTCA introduced tax return attachment TRA 135 because of the Transfer Pricing Rules. What TRA 135 asks for is not confirmed in this skill |
| CbCR notification | Required where applicable |
| CbCR filing | Electronic filing with MTCA |

## Section 5 -- Deadlines

**Deadlines**

| Item | Deadline |
| --- | --- |
| Documentation preparation | Have it ready by the time the company return is filed; TRA 135 goes in with the return |
| Documentation submission on request | Within reasonable timeframe upon MTCA request |
| CbCR filing | Within 12 months of end of reporting FY |
| CbCR notification | As per EU DAC requirements |
| Corporate tax return | Generally within 9 months of FY-end |

## Section 6 -- Penalties

**Penalties**

| Offence | Penalty |
| --- | --- |
| TP documentation failure | No TP-specific penalty appears in the MTCA guidelines (read 23 October 2026); general Income Tax Acts penalties apply to any additional tax |
| CbCR non-compliance | EUR 200 to EUR 50,000 (under EU DAC implementation; not re-checked in this update) |
| General non-compliance | Standard income tax penalties may apply if TP adjustments lead to additional tax |
| Estimated assessment | MTCA may estimate income where documentation is inadequate |

## Section 7 -- Advance Pricing Agreements (APA)

**Advance Pricing Agreements (APA)**

| Item | Detail |
| --- | --- |
| APA availability | Yes. Under the Rules, an APA is agreed between the Maltese Competent Authority and a foreign Competent Authority under the treaty MAP article, before the cross-border arrangement (MTCA APA page). Version 1.0 of this skill said APAs were not established; that was wrong |
| Unilateral transfer pricing ruling | Yes. The Commissioner issues unilateral rulings in advance of an arrangement. A ruling that makes a downward adjustment without a primary adjustment abroad is only considered if it is arm's length in principle and amount, avoids double taxation, and is exchanged with the other tax administration (MTCA guidelines, Rule 11) |
| Fees | Not confirmed in this skill |
| Alternative mechanism | Mutual Agreement Procedure (MAP) under Malta's tax treaties |
| MAP scope | Transfer pricing disputes covered under applicable DTAs |
| MAP fees | No fees charged |
| MAP timeline | Varies; depends on treaty partner cooperation |

## Section 8 -- Safe Harbours

Malta does not currently have formal safe harbour provisions for transfer pricing.

**Safe Harbours**

| Area | Detail |
| --- | --- |
| Low-value intra-group services | OECD Chapter VII simplified approach (5% cost-plus) may be accepted but is not a statutory safe harbour |
| Interest rates | No safe harbour; arm's length rate must be demonstrated (an interest-free loan to or from an associated enterprise abroad is priced like any other loan) |
| Routine services | No simplified pricing rule; standard TP analysis required |
| SME exemption | SMEs (per EU State Aid Rules) are entirely outside scope of the TP Rules |
| Exceptions | Rule 9: the Rules do not apply in a period where revenue items are at or below EUR 6m AND capital items are at or below EUR 20m |

### 8.1 SME Exclusion as Practical Relief

The exclusion of SMEs from the scope of S.L. 123.207 (not re-checked against the Rule text in this update) provides significant practical relief for Malta's predominantly SME economy. SME definitions follow EU State Aid Rules:
- Fewer than 250 employees
- Annual turnover ≤ EUR 50 million OR balance sheet total ≤ EUR 43 million
- Not more than 25% owned by non-SME entities

## Section 9 -- Recent Developments

**Recent Developments**

| Date | Development |
| --- | --- |
| November 2022 | S.L. 123.207 Transfer Pricing Rules introduced (LN 284/2022) |
| January 2024 | Rules apply for basis years from 1 January 2024; pre-2024 arrangements not materially altered are grandfathered for a limited time (Rule 1(2)) |
| 2024 | MTCA Guidelines in relation to the Transfer Pricing Rules published (Article 96(2) ITA) |
| Not confirmed | End date of the Rule 1(2) grandfathering. Version 1.0 said January 2027; the MTCA pages read on 23 October 2026 do not state a date, and legislation.mt was unavailable |
| 7 May 2026 | YA 2026 company return: new attachment TRA 135 for the Transfer Pricing Rules |
| Ongoing | BEPS Pillar Two: Malta implementing GloBE rules (15% minimum tax) via EU Minimum Tax Directive |
| Ongoing | No BEPS Pillar One Amount B adoption announced |

## Section 10 -- Interaction with Other Skills

**Interaction with Other Skills**

| Related skill | Interaction |
| --- | --- |
| mt-corporate-tax | TP adjustments change the company's chargeable income |
| malta-vat-return | TP adjustments may affect the value of supply for VAT purposes |
| Corporate tax (general) | TP rules apply when determining the total income of a company from cross-border arrangements |
| Financial statements | Related-party disclosures under IAS 24 should be consistent with TP documentation |
| CbCR | Feeds into global TP risk assessment by tax authorities |

## Section 11 -- Worked Examples

### Example 1 -- Does a company fall inside the Rules in 2026?

A Malta company has cross-border arrangements with associated enterprises in its 2026 financial period. Revenue items (sales, services, interest, excluding dividends paid) total EUR 4,500,000 at arm's length. Capital items (loans and asset transfers) total EUR 25,000,000. Revenue stays under EUR 6,000,000, but capital goes over EUR 20,000,000. Rule 9 only takes a period out of scope when both stay within their limits, so the Rules apply for 2026. The company needs a master file and local file ready on request and completes TRA 135 with its return.

```oa-check
name: Rule 9 exception test, revenue EUR 4.5m and capital EUR 25m
inputs:
  revenue_items: 4500000
  capital_items: 25000000
  revenue_limit: 6000000
  capital_limit: 20000000
steps:
  - revenue_excess: max(0, revenue_items - revenue_limit)
  - capital_excess: max(0, capital_items - capital_limit)
  - total_excess: revenue_excess + capital_excess
expected:
  revenue_excess: 0
  capital_excess: 5000000
  total_excess: 5000000
```

Any total_excess above zero means the period is in scope.

### Example 2 -- Interest-free loan to a foreign associate

A Malta company that is in scope lends EUR 2,000,000 interest-free to its parent abroad on 1 January 2026, a new arrangement after 1 January 2024, so no grandfathering applies. The benchmarking study sets an arm's length rate of 3% (the rate used in the MTCA guidelines' own example). The company adds the arm's length interest to its chargeable income for basis year 2026. The tax on it follows [mt-corporate-tax](mt-corporate-tax.md).

```oa-check
name: Interest-free loan priced at 3% for a full year
inputs:
  principal: 2000000
  rate_pct: 3
  months: 12
steps:
  - arm_length_interest: pct(principal, rate_pct) * months / 12
expected:
  arm_length_interest: 60000.00
```

## Section 12 -- Ask the Client First

- Total arm's length value of cross-border revenue items and capital items with associated enterprises in the financial period (Rule 9).
- When each arrangement was entered into, and whether it was changed on or after 1 January 2024 (price or method, rights and risks, or duration).
- Group structure and shareholding percentages, to test associated enterprise status.
- Whether the company is an SME under the EU definition.
- Whether any foreign tax authority has made or proposed a primary adjustment.
- Whether the group already has master file and local file content.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

## Sources

| Source | URL | Read on |
|---|---|---|
| MTCA, Transfer Pricing Overview | https://mtca.gov.mt/business-tax/InternationalAffairs/international-direct-taxation/transfer-pricing/transfer-pricing-overview | 2026-10-23 |
| MTCA, Guidelines in relation to the Transfer Pricing Rules (S.L. 123.207) | https://mtca.gov.mt/docs/default-source/documents/business-tax/international-affairs/international-direct-taxation/transfer-pricing/useful-links/guidelines---transfer-pricing-rules.pdf | 2026-10-23 |
| MTCA, Advance Pricing Arrangements | https://mtca.gov.mt/business-tax/InternationalAffairs/international-direct-taxation/transfer-pricing/advanced-pricing-arrangements-(apa) | 2026-10-23 |
| MTCA, Year of Assessment 2026 Tax Return for Companies (TRA 135), 7 May 2026 | https://mtca.gov.mt/news-results-page/2026/05/07/year-of-assessment-2026-tax-return-for-companies | 2026-10-23 |
| Transfer Pricing Rules, S.L. 123.207 | https://legislation.mt/eli/sl/123.207/eng | Site unavailable on 2026-10-23 |

Not yet confirmed: the end date of the Rule 1(2) grandfathering; the SME exclusion and the 75% / 50% associated enterprise tests against the Rule text; whether Legal Notice 9 of 2024 amended the Rules as earlier versions said; the Article 19(5) ITMA retention period; CbCR penalty amounts; APA and ruling fees; the content of TRA 135. legislation.mt was unavailable on 23 October 2026, so the Rule text itself was not read.

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
