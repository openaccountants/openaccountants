---
name: australia-financial-statements
description: Use this skill when preparing, reviewing, or advising on annual financial statements for an Australian company. Trigger on phrases like "ASIC financial report", "AASB", "Australian Accounting Standards", "general purpose financial statements", "special purpose financial statements", "large proprietary company", "small proprietary company", "directors' report Australia", "audit Australia", "Form 388", "Corporations Act 2001 reporting", or any question about preparing and filing statutory accounts under the Corporations Act 2001. Covers AASB frameworks, size thresholds (large/small proprietary), required statements, formats, notes, lodgement deadlines, and audit requirements.
version: 1.1
jurisdiction: AU
tax_year: 2025
last_updated: 2026-08-20
review_status: pending_review
depends_on:
  - financial-statements-workflow-base
category: financial-statements
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Australia Financial Statements

## Australia Financial Statements Skill v1.1

## Section 1 -- Quick Reference

**Quick Reference**

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Australia (Commonwealth of Australia) |
| Currency | AUD |
| Filing authority | Australian Securities and Investments Commission (ASIC) |
| Primary legislation | Corporations Act 2001 (Cth), Chapter 2M |
| Supporting legislation | Corporations Regulations 2001; ASIC Regulatory Guides |
| Accounting standards | Australian Accounting Standards (AASB) — substantially IFRS-equivalent |
| Financial year | Usually 1 July – 30 June; any 12-month period permitted |
| Lodgement deadline | 4 months after year-end (general); 3 months (disclosing entities) |
| Late lodgement penalty | Civil penalty; ASIC may impose up to AUD 1,110 per day |
| Digital filing | ASIC Regulatory Portal (online Form 388 lodgement) |

## Section 2 -- Reporting Framework

**Reporting Framework by entity type**

| Entity type | Applicable standard |
| --- | --- |
| Listed entities / disclosing entities | Full AASB (Tier 1 — IFRS equivalent) |
| Large proprietary companies | AASB (Tier 1 or Tier 2 — Simplified Disclosures) |
| Small proprietary companies (reporting) | AASB (usually Tier 2 — Simplified Disclosures) |
| Small proprietary companies (non-reporting) | Generally no public reporting obligation |
| Public companies | AASB (Tier 1 or Tier 2) |
| Not-for-profit (large) | AASB with NFP-specific paragraphs |

### AASB Tier system

- **Tier 1** — Full IFRS recognition, measurement, and disclosure (AASB 101–AASB 17)  _(AASB 101–AASB 17)_
- **Tier 2 — Simplified Disclosures** — Same recognition and measurement as Tier 1, reduced disclosures (AASB 1060)  _(AASB 1060)_

## Section 3 -- Size Thresholds

### Large proprietary company (s.45A Corporations Act)

- **Large company test** — A proprietary company is large for a financial year if it satisfies at least 2 of 3 criteria.  _(s.45A Corporations Act)_

**Large proprietary company thresholds**  _(s.45A Corporations Act)_

| Criterion | Threshold (from 1 July 2019) |
| --- | --- |
| Consolidated revenue | ≥ AUD 50,000,000 |
| Consolidated gross assets (year-end) | ≥ AUD 25,000,000 |
| Employees (year-end) | ≥ 100 |

- **Small company fallback** — If fewer than 2 criteria are met → small proprietary company.  _(s.45A Corporations Act)_

### Reporting obligations by entity type

**Reporting obligations by entity type**

| Entity | Must prepare financial report? | Must lodge with ASIC? | Must audit? |
| --- | --- | --- | --- |
| Large proprietary | Yes | Yes (Form 388) | Yes |
| Small proprietary (general) | No (unless directed) | No | No |
| Small proprietary (foreign-controlled) | Yes | Yes | Yes |
| Small proprietary (CSF shareholders) | Yes | Yes | Yes (or review) |
| Public company | Yes | Yes | Yes |
| Disclosing entity | Yes | Yes | Yes |

## Section 4 -- Required Financial Statements

- **Statutory basis** — Under s.295 and s.296 Corporations Act + AASB standards  _(s.295, s.296 Corporations Act)_

**Required Financial Statements**  _(s.295, s.296, s.298–300, s.295(4) Corporations Act)_

| Document | Tier 1 (Full AASB) | Tier 2 (Simplified) |
| --- | --- | --- |
| Statement of Financial Position (Balance sheet) | Required | Required |
| Statement of Profit or Loss and Other Comprehensive Income | Required | Required |
| Statement of Changes in Equity | Required | Required |
| Statement of Cash Flows | Required | Required |
| Notes to the Financial Statements | Required (full IFRS) | Required (reduced — AASB 1060) |
| Directors' Report (s.298–300) | Required | Required |
| Directors' Declaration (s.295(4)) | Required | Required |
| Auditor's Report | Required | Required |

## Section 5 -- Year-End Adjustments Checklist

**Year-End Adjustments Checklist**

| # | Adjustment | Australia-specific notes |
| --- | --- | --- |
| 1 | Depreciation | AASB 116; systematic allocation; annual review of useful life and residual value |
| 2 | Provisions | AASB 137; present obligation, probable outflow, reliable estimate |
| 3 | Employee benefits | AASB 119; annual leave, long service leave (probability-weighted for LSL < 7 years) |
| 4 | Impairment | AASB 136; compare carrying amount to recoverable amount |
| 5 | Expected credit losses | AASB 9; simplified approach for trade receivables (lifetime ECL) |
| 6 | Inventory | AASB 102; lower of cost (FIFO/weighted average) and NRV; no LIFO |
| 7 | Deferred tax | AASB 112; temporary differences; company rate 25% (base rate entity) or 30% |
| 8 | Lease accounting | AASB 16; right-of-use asset + lease liability (exemptions for short-term/low-value) |
| 9 | Revenue recognition | AASB 15; five-step model; performance obligations |
| 10 | Financial instruments | AASB 9; classification and measurement; hedge accounting |
| 11 | Foreign currency | AASB 121; monetary items at closing rate |
| 12 | Government grants | AASB 120; recognised when reasonable assurance of compliance |

## Section 6 -- Statement of Profit or Loss Format

AASB 101 permits classification by nature or function. By function (most common for corporates):

```
Revenue
Cost of sales
  ─── Gross profit ───
Other income
Distribution expenses
Administrative expenses
Other expenses
  ─── Operating profit ───
Finance income
Finance costs
Share of profit of associates/JVs
  ─── Profit before income tax ───
Income tax expense
  ─── Profit from continuing operations ───
Profit from discontinued operations (net of tax)
  ─── Profit for the year ───

Other comprehensive income:
  Items that will not be reclassified to profit or loss
  Items that may be reclassified to profit or loss
  ─── Total comprehensive income for the year ───
```

## Section 7 -- Statement of Financial Position Format

AASB 101 — current/non-current distinction:

```
ASSETS

Current assets
  Cash and cash equivalents
  Trade and other receivables
  Inventories
  Current tax assets
  Other current assets

Non-current assets
  Property, plant and equipment
  Right-of-use assets
  Investment properties
  Intangible assets
  Goodwill
  Investments in associates
  Deferred tax assets
  Other non-current assets

Total assets

─────────────────────────────────────

LIABILITIES

Current liabilities
  Trade and other payables
  Borrowings (current portion)
  Lease liabilities (current)
  Current tax liabilities
  Provisions (current)
  Other current liabilities

Non-current liabilities
  Borrowings
  Lease liabilities
  Deferred tax liabilities
  Provisions (non-current)
  Other non-current liabilities

Total liabilities

─────────────────────────────────────

NET ASSETS

EQUITY
  Issued capital
  Reserves
  Retained earnings
Total equity
```

## Section 8 -- Notes to Financial Statements

**Notes to Financial Statements**

| # | Disclosure | Tier 1 (Full) | Tier 2 (Simplified) |
| --- | --- | --- | --- |
| 1 | Basis of preparation and accounting policies | Required (AASB 101) | Required (AASB 1060) |
| 2 | Revenue disaggregation | Required (AASB 15) | Simplified |
| 3 | Employee benefits | Required (AASB 119) | Simplified |
| 4 | Income tax | Required (AASB 112) | Simplified |
| 5 | Property, plant and equipment | Required (AASB 116) | Simplified |
| 6 | Leases | Required (AASB 16) | Simplified |
| 7 | Financial instruments | Required (AASB 7) | Significantly reduced |
| 8 | Related party transactions | Required (AASB 124) | Required |
| 9 | Contingencies and commitments | Required (AASB 137) | Required |
| 10 | Subsequent events | Required (AASB 110) | Required |
| 11 | Key management personnel compensation | Required (AASB 124) | Required |
| 12 | Segment information | Required (AASB 8) — listed only | Not required |

## Section 9 -- Filing (Lodgement) Requirements

**Filing (Lodgement) Requirements**  _(s.340)_

| Item | Detail |
| --- | --- |
| Filing authority | ASIC |
| Filing form | Form 388 (Copy of Financial Statements and Reports) |
| Lodgement method | ASIC Regulatory Portal (online) |
| Deadline — disclosing entities | 3 months after financial year-end |
| Deadline — all others | 4 months after financial year-end |
| Documents lodged | Financial report + directors' report + auditor's report |
| Fee | No filing fee for Form 388 |
| Late lodgement | Civil penalty provisions; ASIC may impose administrative penalties |
| Annual review fee | Separate from lodgement (AUD 342 for proprietary companies from 1 July 2026; 2025-26: AUD 329) |
| Extension | Possible by application to ASIC under s.340 |

### Small proprietary companies — exceptions requiring lodgement

- **Foreign-controlled** — Foreign-controlled (s.292(2)(b))  _(s.292(2)(b))_
- **ASIC direction** — ASIC direction (s.294)  _(s.294)_
- **Shareholder direction** — Shareholder direction (≥5% vote, s.293)  _(s.293)_
- **CSF shareholders** — CSF shareholders (s.292(2)(c))  _(s.292(2)(c))_

## Section 10 -- Audit Requirements

**Audit Requirements**  _(s.292)_

| Category | Requirement |
| --- | --- |
| Large proprietary company | Mandatory audit |
| Small proprietary (general) | No audit required |
| Small proprietary (foreign-controlled) | Audit required (unless ASIC relief) |
| Public company | Mandatory audit |
| Disclosing entity | Mandatory audit |
| Registered scheme | Mandatory audit |
| Small proprietary (CSF shareholders) | Audit or review (s.292) |

### ASIC relief instruments

- **ASIC Corporations (Audit Relief) Instrument 2016/784** — Allows certain large proprietary companies controlled by a foreign parent to obtain audit relief if consolidated accounts of the foreign parent are lodged  _(ASIC Corporations (Audit Relief) Instrument 2016/784)_
- **ASIC Corporations (Foreign-Controlled Company Reports) Instrument 2017/204** — Relief for certain small foreign-controlled proprietary companies  _(ASIC Corporations (Foreign-Controlled Company Reports) Instrument 2017/204)_

### Auditor qualification

- **Registered company auditor** — Registered company auditor under Part 9.2 of the Corporations Act (registered with ASIC). For audit of disclosing entities, the auditor must meet additional independence requirements under Part 2M.4 Division 3.  _(Part 9.2 Corporations Act; Part 2M.4 Division 3 Corporations Act)_

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is
different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your
jurisdiction — no liability on either side until you and the accountant sign
a formal engagement letter — book a free 30-minute call:

→ [Book a call](https://calendly.com/openaccountants-info/30min)

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
