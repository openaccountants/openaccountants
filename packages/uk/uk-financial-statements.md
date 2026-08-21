---
name: uk-financial-statements
description: Use this skill when preparing, reviewing, or advising on annual financial statements for a UK company. Trigger on phrases like "Companies House accounts", "FRS 102", "FRS 105", "micro-entity accounts", "small company accounts", "abbreviated accounts", "directors' report UK", "filing accounts UK", "audit exemption UK", "year-end adjustments UK", "iXBRL", "abridged accounts", or any question about preparing statutory accounts under the Companies Act 2006. Covers FRS 102/105 frameworks, size thresholds, required statements, P&L and balance sheet formats, notes, filing deadlines, and audit requirements.
version: 1.0
jurisdiction: GB
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: James Power
review_status: current
depends_on: - financial-statements-workflow-base
category: financial-statements
tier: 1
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# UK Financial Statements

## UK Financial Statements Skill v1.0

> **Year applicability:** Rules in this skill apply across **2024-25, 2025-26, and 2026-27** unless a specific section flags a year-dated change. The pack is read alongside the rate-bearing skills (`uk-income-tax-sa100`, `uk-national-insurance`, `uk-dividends`, etc.) which carry full 3-year tables.

## Verified rates & thresholds (accountant-reviewed)

> Reviewed against the cited tax authorities by **James Power** on 2026-06-03.
> Items flagged for further clarification are tracked separately and excluded here.
> This block is generated from verified `skill_facts` — edit the facts, not the prose.

### Financial Statements

- **Micro — turnover** — ≤ £1,000,000  _(CA 2006 s.384A)_
- **Micro — balance sheet** — ≤ £500,000  _(CA 2006)_
- **Micro — employees** — ≤ 10  _(CA 2006)_
- **Small — turnover** — ≤ £15,000,000  _(CA 2006 s.382)_
- **Small — balance sheet** — ≤ £7,500,000  _(CA 2006)_
- **Small — employees** — ≤ 50  _(CA 2006)_
- **Medium — turnover** — ≤ £54,000,000  _(CA 2006 s.465)_
- **Medium — balance sheet** — ≤ £27,000,000  _(CA 2006)_
- **Medium — employees** — ≤ 250  _(CA 2006)_
- **Test** — 2 out of 3 criteria in current + preceding year  _(CA 2006)_
- **Private company deadline** — 9 months after year-end  _(CA 2006 s.442)_
- **Public company deadline** — 6 months after year-end  _(CA 2006)_
- **Late filing penalty (private)** — £150 to £1,500  _(CA 2006 s.453)_
- **Micro/small company** — Exempt from audit  _(CA 2006 s.477)_
- **Medium/large company** — Required  _(CA 2006)_
- **10% shareholder request** — Overrides small company exemption  _(CA 2006 s.476)_

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | United Kingdom |
| Currency | GBP |
| Filing authority | Companies House |
| Primary legislation | Companies Act 2006 |
| Supporting regulations | The Small Companies and Groups (Accounts and Directors' Report) Regulations 2008; The Large and Medium-sized Companies and Groups (Accounts and Reports) Regulations 2008 |
| Accounting standards | FRS 102 (full / Section 1A); FRS 105 (micro); UK-adopted IFRS (listed/choice) |
| Financial year | Any period up to 18 months; usually 12 months |
| Filing deadline | 9 months after year-end (private); 6 months (public) |
| Late filing penalty | £150 to £1,500 (private); £750 to £7,500 (public) |
| Digital filing | iXBRL tagging required for corporation tax; online filing via Companies House |

## Section 2 -- Reporting Framework

**Reporting Framework**

| Entity category | Applicable standard | Key features |
| --- | --- | --- |
| Micro-entity | FRS 105 | Highly simplified; no notes beyond statutory minimum; no true and fair override |
| Small entity | FRS 102 Section 1A | Simplified disclosures; abridged formats permitted |
| Medium entity | FRS 102 (full) | Full FRS 102 disclosures; some exemptions from filing certain information |
| Large entity | FRS 102 (full) or UK-adopted IFRS | Full disclosure requirements |
| Listed / AIM (with IFRS) | UK-adopted IFRS | Mandatory for consolidated accounts of listed groups |
| Qualifying subsidiary | FRS 101 | IFRS recognition/measurement with reduced disclosures |

## Section 3 -- Size Thresholds

Effective for accounting periods beginning on or after 6 April 2025:

**Size Thresholds (current)**

| Criterion | Micro | Small | Medium |
| --- | --- | --- | --- |
| Turnover | ≤ £1,000,000 | ≤ £15,000,000 | ≤ £54,000,000 |
| Balance sheet total | ≤ £500,000 | ≤ £7,500,000 | ≤ £27,000,000 |
| Employees | ≤ 10 | ≤ 50 | ≤ 250 |

- **Classification test** — Must meet 2 out of 3 criteria in the current and preceding year. Companies exceeding "medium" thresholds are classified as large.

**Previous thresholds (periods beginning before 6 April 2025)**

| Criterion | Micro | Small | Medium |
| --- | --- | --- | --- |
| Turnover | ≤ £632,000 | ≤ £10,200,000 | ≤ £36,000,000 |
| Balance sheet total | ≤ £316,000 | ≤ £5,100,000 | ≤ £18,000,000 |
| Employees | ≤ 10 | ≤ 50 | ≤ 250 |

## Section 4 -- Required Financial Statements

**Required Financial Statements**

| Document | Micro (FRS 105) | Small (s1A) | Medium/Large |
| --- | --- | --- | --- |
| Profit and loss account | Required (very simple) | Required (abridged option) | Required (full) |
| Balance sheet | Required (very simple) | Required (abridged option) | Required (full) |
| Statement of changes in equity | Not required | Not required (optional) | Required |
| Cash flow statement | Not required | Not required | Required |
| Notes to accounts | Statutory minimum only | Reduced disclosures | Full |
| Directors' report | Not required (statutory presumption) | Required | Required |
| Strategic report | Not required | Not required | Required (large only) |
| Auditor's report | Not required | Not required (if exempt) | Required (medium with audit) |

## Section 5 -- Year-End Adjustments Checklist

**Year-End Adjustments Checklist**

| # | Adjustment | UK-specific notes |
| --- | --- | --- |
| 1 | Depreciation | FRS 102 Section 17; useful life basis; annual review of residual value |
| 2 | Accruals | Audit/accountancy fees, bonuses, utilities |
| 3 | Prepayments | Insurance, rent, software licences |
| 4 | Provisions | FRS 102 Section 21; present obligation, reliable estimate |
| 5 | Bad debt provision | Expected credit loss model (FRS 102 Section 11 simplified) |
| 6 | Inventory | Lower of cost and estimated selling price less costs to sell |
| 7 | Deferred tax | FRS 102 Section 29; timing differences approach (not temporary differences) |
| 8 | Holiday pay accrual | Required under FRS 102 — untaken leave at year-end |
| 9 | Lease accounting | FRS 102 Section 20 (finance/operating distinction — not IFRS 16) |
| 10 | R&D costs | Capitalise development costs meeting criteria (Section 18) or expense |
| 11 | Government grants | Accruals model or performance model (Section 24) |
| 12 | Director's loan account | S.455 CTA 2010 tax charge if overdrawn at year-end |

## Section 6 -- Profit and Loss Account Format

Companies Act 2006 Schedule 1 — Format 1 (vertical, by function) most common:

```
Turnover
Cost of sales
  ─── Gross profit ───
Distribution costs
Administrative expenses
Other operating income
  ─── Operating profit ───
Income from shares in group undertakings
Other interest receivable and similar income
Interest payable and similar expenses
  ─── Profit on ordinary activities before taxation ───
Tax on profit on ordinary activities
  ─── Profit for the financial year ───
```

Format 2 (by nature — alternative):

```
Turnover
Change in stocks of finished goods and WIP
Own work capitalised
Other operating income
Raw materials and consumables
Staff costs
Depreciation and other amounts written off assets
Other operating charges
  ─── Operating profit ───
(continue as Format 1)
```

## Section 7 -- Balance Sheet Format

Companies Act 2006 Schedule 1 — Format 1 (vertical):

```
Fixed assets
  Intangible assets
  Tangible assets
  Investments

Current assets
  Stocks
  Debtors
  Investments
  Cash at bank and in hand

Creditors: amounts falling due within one year
  ─── Net current assets ───

Total assets less current liabilities

Creditors: amounts falling due after more than one year
Provisions for liabilities
  ─── Net assets ───

Capital and reserves
  Called up share capital
  Share premium account
  Revaluation reserve
  Other reserves
  Profit and loss account
  ─── Shareholders' funds ───
```

## Section 8 -- Notes to Accounts

### Minimum disclosures by entity size

**Minimum disclosures by entity size**

| # | Disclosure | Micro (FRS 105) | Small (s1A) | Medium/Large |
| --- | --- | --- | --- | --- |
| 1 | Accounting policies | Statutory only | Required | Full |
| 2 | Fixed assets movements | Not required | Required | Required |
| 3 | Financial commitments | Not required | Required | Required |
| 4 | Guarantees/contingencies | Required (on balance sheet) | Required | Required |
| 5 | Related party transactions | Not required | Required (s1A.12) | Required (Section 33) |
| 6 | Employee numbers | Not required | Average number only | Full breakdown + costs |
| 7 | Directors' remuneration | Not required | Required (total) | Required (detailed) |
| 8 | Audit fees | Not required | Not required | Required |
| 9 | Financial instruments | Not required | Basic only | Full (Section 11/12) |
| 10 | Deferred tax | Not required | If material | Required (Section 29) |
| 11 | Share capital | Not required | Required | Required |
| 12 | Dividends | Not required | Required | Required |

## Section 9 -- Filing Requirements

**Filing Requirements**

| Item | Detail |
| --- | --- |
| Filing authority | Companies House |
| Filing method | Online (Software filing, Companies House WebFiling, or third-party) |
| Private company deadline | 9 months after accounting reference date |
| Public company deadline | 6 months after accounting reference date |
| First accounts | 21 months from incorporation (private); 18 months (public) |
| Documents filed (small) | Abridged balance sheet + notes (P&L can be omitted from public record) |
| Documents filed (micro) | Balance sheet only (with statutory footnotes) |
| Documents filed (medium/large) | Full accounts + directors' report + auditor's report |
| iXBRL | Required for corporation tax filing to HMRC (not Companies House) |
| Language | English or Welsh |

### Late Filing Penalties (private companies)

**Late Filing Penalties (private companies)**

| Delay | Penalty |
| --- | --- |
| Up to 1 month | £150 |
| 1–3 months | £375 |
| 3–6 months | £750 |
| Over 6 months | £1,500 |

- **Public company penalties** — Public company penalties are doubled.

## Section 10 -- Audit Requirements

**Audit Requirements**

| Category | Audit requirement |
| --- | --- |
| Micro-entity | Exempt (unless part of non-small group) |
| Small company | Exempt (same thresholds as small company classification) |
| Medium company | Required |
| Large company | Required |
| Public company | Always required |
| Charity (income > £1m) | Required |
| Member of non-small group | Required (even if company itself is small) |

### Conditions that override small company audit exemption:

- **Override conditions** — Public company or member of group containing a public company; Regulated (banking, insurance, financial services); Shareholders holding ≥10% request audit (s.476 CA 2006); Part of an ineligible group (group exceeds small thresholds)  _(s.476 CA 2006)_

### Auditor qualification

- **Registered Auditor** — Must be a Registered Auditor (member of a Recognised Supervisory Body: ICAEW, ICAS, CAI, ACCA).

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
