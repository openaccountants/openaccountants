---
name: malta-financial-statements
description: Use this skill when preparing, reviewing, or advising on annual financial statements for a Maltese company. Trigger on phrases like "annual accounts Malta", "financial statements Malta", "Companies Act filing", "MBR filing", "balance sheet format", "profit and loss format", "directors' report", "audit exemption Malta", "small company Malta", "abridged accounts", "year-end adjustments", or any question about preparing statutory accounts under the Malta Companies Act (Cap. 386). Covers reporting frameworks, size thresholds, required statements, P&L and balance sheet formats, notes disclosures, filing deadlines, and audit requirements.
version: 1.0
jurisdiction: MT
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - financial-statements-workflow-base
category: financial-statements
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Malta Financial Statements

## Malta Financial Statements Skill v1.0

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Malta (Republic of Malta) |
| Currency | EUR |
| Filing authority | Malta Business Registry (MBR) |
| Primary legislation | Companies Act, Chapter 386 |
| Supporting legislation | Accountancy Profession Act (Cap. 281); Income Tax Management Act (Cap. 372) |
| Accounting standards | IFRS as adopted by the EU (default); GAPSME for qualifying entities |
| Financial year | Any 12-month period (calendar year common but not mandatory) |
| Filing deadline | 10 months from year-end for approval; 42 days after approval for filing |
| Late filing penalty | EUR 250 per year of delay (Registry surcharge) |
| Digital filing | Yes — MBR Online portal |

## Section 2 -- Reporting Framework

**Reporting Framework**

| Entity type | Applicable standard |
| --- | --- |
| Public interest entities / listed companies | Full IFRS as adopted by the EU |
| Large private companies | Full IFRS as adopted by the EU |
| Small and medium private companies | GAPSME (General Accounting Principles for Smaller Entities) permitted as alternative to IFRS |
| Micro-entities (Art. 185(2) criteria met) | GAPSME with further simplifications |

GAPSME is based on IFRS for SMEs with Malta-specific adaptations. Companies may always elect to use full IFRS even if eligible for GAPSME.

## Section 3 -- Size Thresholds

### Small Company (Article 185(2) Companies Act)

- **Small company qualification rule** — A private company qualifies as small if it does not exceed at least two of the following three thresholds on its balance sheet date.  _(Article 185(2) Companies Act)_

**Small Company thresholds**  _(Article 185(2) Companies Act)_

| Criterion | Threshold |
| --- | --- |
| Balance sheet total | EUR 4,000,000 |
| Turnover | EUR 8,000,000 |
| Average employees | 50 |

### Audit Exemption Micro-Thresholds (Article 185(2) — 2025 rules)

**Audit Exemption Micro-Thresholds**  _(Article 185(2) Companies Act, 2025 rules)_

| Criterion | Threshold |
| --- | --- |
| Balance sheet total | EUR 46,600 |
| Turnover | EUR 93,000 |
| Average employees | 2 |

- **Micro-threshold audit outcome** — Companies not exceeding 2 of 3 above: review report only. Companies not exceeding all 3: no audit or review required (effective for periods starting on/after 1 January 2025).  _(Article 185(2) Companies Act, 2025 rules)_

### Small Group (Article 185(5))

**Small Group thresholds**  _(Article 185(5) Companies Act)_

| Criterion | Threshold (net) | Threshold (gross) |
| --- | --- | --- |
| Balance sheet total | EUR 4,000,000 | EUR 4,800,000 |
| Turnover | EUR 8,000,000 | EUR 9,600,000 |
| Average employees | 50 | 50 |

## Section 4 -- Required Financial Statements

**Required Financial Statements**

| Document | Large | Small | Micro |
| --- | --- | --- | --- |
| Statement of Financial Position (Balance Sheet) | Required | Required | Required |
| Statement of Comprehensive Income (P&L) | Required | Required (abridged permitted) | Required (abridged) |
| Statement of Changes in Equity | Required | Required | Not required |
| Statement of Cash Flows | Required | Not required | Not required |
| Notes to the Financial Statements | Required (full) | Required (reduced) | Minimal |
| Directors' Report | Required | Required | Required |
| Auditor's Report | Required | See audit exemption | See audit exemption |

## Section 5 -- Year-End Adjustments Checklist

**Year-End Adjustments Checklist**

| # | Adjustment | Malta-specific notes |
| --- | --- | --- |
| 1 | Depreciation | IAS 16 rates; no statutory rates prescribed (tax depreciation per 6th Schedule ITA is separate) |
| 2 | Accruals | Audit fees, bonuses, utilities, professional fees |
| 3 | Prepayments | Insurance, rent, licences spanning year-end |
| 4 | Provisions | Warranty, legal claims, restructuring (IAS 37 criteria) |
| 5 | Bad debt provision | Specific + expected credit loss model (IFRS 9) |
| 6 | Inventory valuation | Lower of cost and NRV; FIFO or weighted average |
| 7 | Deferred tax | Temporary differences at 35% corporate rate |
| 8 | Foreign exchange | Monetary items at closing rate; P&L differences |
| 9 | Lease accounting | IFRS 16 right-of-use assets (large companies) |
| 10 | Revenue cut-off | IFRS 15 performance obligations |
| 11 | Investment property | Fair value or cost model (IAS 40) |
| 12 | Employee benefits | Retirement benefits, accumulated leave |

## Section 6 -- Profit and Loss Format

The Companies Act Fourth Schedule prescribes formats. Most Maltese companies use the "by nature" classification:

```
Revenue
Cost of sales
  ─── Gross profit ───
Other operating income
Administrative expenses
Distribution costs
Other operating expenses
  ─── Operating profit ───
Finance income
Finance costs
  ─── Profit before tax ───
Income tax expense
  ─── Profit for the year ───

Other comprehensive income:
  Items that will not be reclassified to P&L
  Items that may be reclassified to P&L
  ─── Total comprehensive income ───
```

## Section 7 -- Balance Sheet Format

Companies Act Fourth Schedule format (vertical presentation):

```
ASSETS
Non-current assets
  Intangible assets
  Property, plant and equipment
  Investment property
  Right-of-use assets
  Investments in subsidiaries/associates
  Deferred tax assets

Current assets
  Inventories
  Trade and other receivables
  Current tax assets
  Cash and cash equivalents

Total assets

EQUITY AND LIABILITIES
Equity
  Share capital
  Share premium
  Retained earnings
  Other reserves

Non-current liabilities
  Borrowings
  Lease liabilities
  Deferred tax liabilities
  Provisions

Current liabilities
  Trade and other payables
  Current tax liabilities
  Current portion of borrowings
  Bank overdrafts

Total equity and liabilities
```

## Section 8 -- Notes to Accounts

### Minimum required disclosures

**Minimum required disclosures**

| # | Disclosure | Large | Small | Micro |
| --- | --- | --- | --- | --- |
| 1 | Accounting policies | Full | Full | Summary |
| 2 | Property, plant and equipment movements | Full | Abbreviated | Not required |
| 3 | Related party transactions | Full (IAS 24) | Key management only | Not required |
| 4 | Financial instruments | Full (IFRS 7) | Simplified | Not required |
| 5 | Revenue disaggregation | By category/geography | Summary | Not required |
| 6 | Employee information | Average numbers + costs | Average numbers | Average numbers |
| 7 | Directors' emoluments | Required | Required | Not required |
| 8 | Contingent liabilities | Required | Required | Not required |
| 9 | Commitments | Required | Summary | Not required |
| 10 | Events after reporting period | Required | Required | Required |
| 11 | Share capital details | Required | Required | Required |
| 12 | Tax reconciliation | Required | Not required | Not required |

## Section 9 -- Filing Requirements

**Filing Requirements**

| Item | Detail |
| --- | --- |
| Filing authority | Malta Business Registry (MBR) |
| Filing method | Online via MBR e-services portal |
| Approval deadline | Within 10 months from accounting year-end (private company) |
| Filing deadline | Within 42 days from date of approval by shareholders |
| Documents to file | Annual return + financial statements + directors' report + auditor's report (if applicable) |
| Filing fee | EUR 100 (standard); EUR 20 (micro) |
| Late filing penalty | EUR 250 annual surcharge |
| Language | English or Maltese |
| Format | PDF upload via MBR portal |
| XBRL requirement | Not currently required |

## Section 10 -- Audit Requirements

**Audit Requirements**

| Category | Requirement |
| --- | --- |
| All 3 micro-thresholds met (Art. 185(2)) | No audit or review required (from FY starting 1 Jan 2025) |
| 2 of 3 micro-thresholds met | Review engagement required (ISRE 2400) |
| 1 or 0 micro-thresholds met | Full statutory audit required |
| Public interest entities | Always full audit |
| Groups preparing consolidated accounts | Audit required unless small group |
| Auditor qualification | Warranted accountant holding practising certificate (MIA registered) |

### Income Tax Override (Cap. 372)

- **Income Tax Management Act audit override** — Article 19(4)(a) of the Income Tax Management Act historically required audited accounts for income tax purposes regardless of Companies Act exemptions. The 2025 Audit Exemption Rules (L.N. 139 of 2025) have aligned income tax requirements with Companies Act exemptions for qualifying companies.  _(Article 19(4)(a) Income Tax Management Act (Cap. 372); L.N. 139 of 2025)_

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
