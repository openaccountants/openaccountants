---
name: uk-financial-statements
description: Use this skill when preparing, reviewing, or advising on annual financial statements for a UK company. Trigger on phrases like "Companies House accounts", "FRS 102", "FRS 105", "micro-entity accounts", "small company accounts", "abbreviated accounts", "directors' report UK", "filing accounts UK", "audit exemption UK", "year-end adjustments UK", "iXBRL", "abridged accounts", "identity verification Companies House", "software filing April 2028", or any question about preparing statutory accounts under the Companies Act 2006. Covers FRS 102/105 frameworks (Periodic Review 2024 in force from 1 January 2026), the size thresholds raised for financial years beginning on or after 6 April 2025, required statements, P&L and balance sheet formats, notes, filing deadlines, late filing penalties, audit requirements, and the Economic Crime and Corporate Transparency Act changes in force in 2026 or due from April 2028. Position at 14 November 2026.
version: "2.0"
type: situation-rules
jurisdiction: GB
tax_year: 2026
last_updated: 2026-11-14
source_checked: 2026-11-14
depends_on:
  - financial-statements-workflow-base
category: financial-statements
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: financial-statements
---

# UK Financial Statements

> **Year applicability:** This version gives the position at 14 November 2026 (2026/27). The size thresholds apply to financial years beginning on or after 6 April 2025, so they govern accounts for 2025/26 and 2026/27 year ends. FRS 102 and FRS 105 changes from the Periodic Review 2024 apply to accounting periods beginning on or after 1 January 2026. Where a rule changes on a later date (April 2028 filing reforms), the date is given. Read alongside uk-corporation-tax (the CT600 and its iXBRL accounts) and uk-formation (identity verification and other Companies House rules at formation). Every figure below was read on the official page on 14 November 2026.

## Scope

This skill covers the annual statutory accounts of a UK company under the Companies Act 2006: which size class it falls in, which framework applies (FRS 105, FRS 102 Section 1A, full FRS 102, FRS 101, UK-adopted IFRS), what must be prepared and filed, the formats, the year-end adjustments, filing deadlines and penalties, audit exemption, and the ECCTA filing changes.

Out of scope: the corporation tax computation and CT600 (`uk-corporation-tax`), formation and registered office rules (`uk-formation`), charity SORP accounts beyond the audit threshold, and the audit itself.

### Quick reference

- **Country:** United Kingdom
- **Currency:** GBP
- **Filing authority:** Companies House
- **Primary legislation:** Companies Act 2006
- **Supporting regulations:** The Small Companies and Groups (Accounts and Directors' Report) Regulations 2008; The Large and Medium-sized Companies and Groups (Accounts and Reports) Regulations 2008
- **Accounting standards:** FRS 102 (full / Section 1A); FRS 105 (micro); UK-adopted IFRS (listed/choice). Periodic Review 2024 amendments apply to periods beginning on or after 1 January 2026 ([FRC, FRS 102](https://www.frc.org.uk/library/standards-codes-policy/accounting-and-reporting/uk-accounting-standards/frs-102/))
- **Financial year:** usually 12 months; an accounting reference period may not be extended beyond 18 months (CA 2006 s.392(5))
- **Filing deadline:** 9 months after the end of the accounting reference period (private); 6 months (public) (CA 2006 s.442)
- **Late filing penalty:** GBP 150 to GBP 1,500 (private); GBP 750 to GBP 7,500 (public); doubled if the previous year's accounts were also late (SI 2008/497 reg 4)
- **Digital filing:** HMRC: accounts and CT600 in iXBRL through commercial software from 1 April 2026. Companies House: software, WebFiling or paper today; software only (iXBRL) for accounts from April 2028
- **Identity verification:** compulsory for directors and PSCs since 18 November 2025 (see Filing and payment)

## Ask the client first

- What are the turnover, balance sheet total (gross assets) and average number of employees for this year and last year? Was last year the first financial year?
- Is the company public, a member of a group (with a public company or one above the small thresholds), or in banking, insurance, e-money, MiFID investment or UCITS management?
- Is it a parent or a subsidiary? Does it prepare group accounts, or could it use the s.479A parent guarantee exemption?
- What is the accounting reference date, is this the first period, and has the period been shortened or extended?
- Were last year's accounts filed late?
- Has any member holding 10% or more asked for an audit?
- Does the company have leases (as lessee), customer contracts with timing questions, development costs, government grants, or an overdrawn director's loan account?
- Have all directors and PSCs verified their identity with Companies House?
- Who files: the company or an agent (an ACSP)? With which software?

## The method, step by step

1. **Size the company** with the 2-of-3 test against the thresholds in force (rates table), applying the two-consecutive-years rule and the look-back in SI 2024/1303 reg 3. Groups use the net or gross group limits.
2. **Check the exclusions** (public, regulated, ineligible group) that take a small company out of the small regime or out of audit exemption.
3. **Pick the framework**: FRS 105 for a micro-entity choosing it, FRS 102 Section 1A for small, full FRS 102 or UK-adopted IFRS for medium and large, FRS 101 for qualifying subsidiaries and parents.
4. **Make the year-end adjustments** (checklist below), including the Periodic Review 2024 lease and revenue changes for periods beginning on or after 1 January 2026.
5. **Prepare the statements** in the statutory formats with the notes the size class needs.
6. **Decide on audit**: exemption under s.477 (small) or s.479A (subsidiary), unless excluded or a s.476 notice was given.
7. **File** by the deadline, in the documents the size class must file, with iXBRL where required.

### Rates, bands and thresholds

Size thresholds apply to financial years beginning on or after 6 April 2025.

| Item | Figure | Applies | Official source |
| --- | --- | --- | --- |
| Micro-entity limits | Turnover not more than GBP 1 million; balance sheet total not more than GBP 500,000; employees not more than 10 | 2 or more of the 3 | https://www.legislation.gov.uk/ukpga/2006/46/section/384A |
| Small company limits | Turnover not more than GBP 15 million; balance sheet total not more than GBP 7.5 million; employees not more than 50 | 2 or more of the 3; change counts only if in two consecutive financial years | https://www.legislation.gov.uk/ukpga/2006/46/section/382 |
| Medium company limits | Turnover not more than GBP 54 million; balance sheet total not more than GBP 27 million; employees not more than 250 | 2 or more of the 3 | https://www.legislation.gov.uk/ukpga/2006/46/section/465 |
| Previous limits replaced by SI 2024/1303 | Micro GBP 632,000 and GBP 316,000; small GBP 10.2 million and GBP 5.1 million; medium GBP 36 million and GBP 18 million | Financial years beginning before 6 April 2025 | https://www.legislation.gov.uk/uksi/2024/1303/made |
| Small group limits | GBP 15 million net (GBP 18 million gross) turnover; GBP 7.5 million net (GBP 9 million gross) balance sheet total | From 6 April 2025 | same |
| Medium group limits | GBP 54 million net (GBP 64 million gross) turnover; GBP 27 million net (GBP 32 million gross) balance sheet total | From 6 April 2025 | same |
| Filing deadline | Private: nine months; public: six months after the end of the accounting reference period | CA 2006 s.442(2) | https://www.legislation.gov.uk/ukpga/2006/46/section/442 |
| First accounts over twelve months | Nine or six months from the first anniversary of incorporation, or three months after the period end, whichever is later | CA 2006 s.442(3) | same |
| Maximum accounting reference period | 18 months; no further extension less than five years after an earlier extended period | CA 2006 s.392 | https://www.legislation.gov.uk/ukpga/2006/46/section/392 |
| Late filing penalty, private | GBP 150 (up to 1 month), GBP 375 (1 to 3), GBP 750 (3 to 6), GBP 1,500 (over 6) | Doubled if the previous year was also late | https://www.legislation.gov.uk/uksi/2008/497/regulation/4 |
| Late filing penalty, public | GBP 750, GBP 1,500, GBP 3,000, GBP 7,500 for the same bands | Doubled if the previous year was also late | same |
| Members' audit notice | Members holding at least 10% in nominal value of issued share capital (or of a class), or 10% of members | Given not later than one month before the year end | https://www.legislation.gov.uk/ukpga/2006/46/section/476 |
| Charity audit, England and Wales | Gross income over GBP 1.5 million, or over GBP 500,000 with gross assets over GBP 5 million (before: GBP 1 million; GBP 250,000 with GBP 3.26 million) | Financial years ending on or after 30 September 2026 | https://www.legislation.gov.uk/uksi/2026/427/made |
| Charity audit, the statute as amended | Gross income exceeds GBP 1.5 million | Charities Act 2011 s.144 | https://www.legislation.gov.uk/ukpga/2011/25/section/144 |
| HMRC free accounts and tax return service | Closed 31 March 2026 | CT600 and iXBRL accounts by commercial software | https://www.gov.uk/guidance/closure-of-the-service-to-file-your-company-accounts-and-tax-return |

### Reporting framework

| Entity category | Applicable standard | Key features |
| --- | --- | --- |
| Micro-entity | FRS 105 | Highly simplified. Where the accounts contain only the micro-entity minimum accounting items, the directors disregard any accounting standard requirement to give more information (CA 2006 s.393(1A)) |
| Small entity | FRS 102 Section 1A | Simplified disclosures (FRS 102 para 1AC.35 and the rest of Section 1A); abridged formats permitted (SI 2008/409 Sch 1 para 1A) |
| Medium entity | FRS 102 (full) | Full FRS 102 disclosures. Files full accounts, strategic report and directors' report, with the auditor's report unless exempt (CA 2006 s.445(1), (2)) |
| Large entity | FRS 102 (full) or UK-adopted IFRS | Full disclosure requirements. Any company may choose IAS individual accounts (CA 2006 s.395(1)) |
| Parent with securities on a UK regulated market | UK-adopted IFRS | Mandatory for its group accounts (CA 2006 s.403(1)) |
| Subsidiaries and ultimate parents (individual accounts) | FRS 101 | Recognition and measurement of adopted IFRS with disclosure exemptions ([FRC, FRS 101](https://www.frc.org.uk/library/standards-codes-policy/accounting-and-reporting/uk-accounting-standards/frs-101/)) |

- **Periodic Review 2024.** The FRC's amendments to FRS 102 and FRS 105 take effect for accounting periods beginning on or after 1 January 2026, with early application allowed only if all amendments are applied together. The two big changes are a revenue model based on the five-step model in IFRS 15 (in FRS 102 and FRS 105) and an on-balance-sheet lease model for lessees based on IFRS 16 (in FRS 102). A calendar-year company first applies them in its accounts for the year ending 31 December 2026 ([FRC, FRS 102](https://www.frc.org.uk/library/standards-codes-policy/accounting-and-reporting/uk-accounting-standards/frs-102/)).
- **Next FRC change.** Amendments for entities that adapt the balance sheet or profit and loss formats (following IFRS 18) take effect from 1 January 2027 (same page).

### Size thresholds

Effective for financial years beginning on or after 6 April 2025 (SI 2024/1303 reg 2(2)):

| Criterion | Micro | Small | Medium | Source |
| --- | --- | --- | --- | --- |
| Turnover | not more than GBP 1 million | not more than GBP 15 million | not more than GBP 54 million | https://www.legislation.gov.uk/uksi/2024/1303/made |
| Balance sheet total | not more than GBP 500,000 | not more than GBP 7.5 million | not more than GBP 27 million | same |
| Employees | not more than 10 | not more than 50 | not more than 250 | https://www.legislation.gov.uk/ukpga/2006/46/section/465 |

- **Classification test**: must meet 2 or more of the 3 criteria. In the first financial year that year alone counts; after that, meeting or ceasing to meet the criteria only changes the size category if it occurs in two consecutive financial years. Companies exceeding "medium" thresholds are classified as large (CA 2006 s.382).
- **Looking back at earlier years**: when sizing a company for a financial year beginning on or after 6 April 2025, it is treated as having qualified in any earlier year in which it would have qualified had the new thresholds applied then. So a company that was medium last year under the old limits can count last year as small under the new ones (SI 2024/1303 reg 3).
- **Parent companies and groups**: small group not more than GBP 15 million net (GBP 18 million gross) turnover and GBP 7.5 million net (GBP 9 million gross) balance sheet total; medium group not more than GBP 54 million net (GBP 64 million gross) and GBP 27 million net (GBP 32 million gross); employee limits as above (SI 2024/1303 regs 9 and 10).
- **LLPs**: the same raised thresholds apply to limited liability partnerships (SI 2024/1303 reg 11).

**Previous thresholds (financial years beginning before 6 April 2025)**

| Criterion | Micro | Small | Medium | Source |
| --- | --- | --- | --- | --- |
| Turnover | not more than GBP 632,000 | not more than GBP 10.2 million | not more than GBP 36 million | https://www.legislation.gov.uk/uksi/2024/1303/made |
| Balance sheet total | not more than GBP 316,000 | not more than GBP 5.1 million | not more than GBP 18 million | same |
| Employees | not more than 10 | not more than 50 | not more than 250 | https://www.legislation.gov.uk/ukpga/2006/46/section/465 |

### Required financial statements

Sources: [CA 2006 s.414A](https://www.legislation.gov.uk/ukpga/2006/46/section/414A), [s.415](https://www.legislation.gov.uk/ukpga/2006/46/section/415).

| Document | Micro (FRS 105) | Small (s1A) | Medium/Large |
| --- | --- | --- | --- |
| Profit and loss account | Required (very simple) | Required (abridged option) | Required (full) |
| Balance sheet | Required (very simple) | Required (abridged option) | Required (full) |
| Statement of changes in equity | Not required | Not required (optional) | Required |
| Cash flow statement | Not required | Not required | Required |
| Notes to accounts | Statutory minimum only | Reduced disclosures | Full |
| Directors' report | Not required (CA 2006 s.415(1A)) | Required | Required |
| Strategic report | Not required | Not required (s.414A(2)) | Required (medium and large) |
| Auditor's report | Not required | Not required (if exempt) | Required (medium with audit) |

- Small companies no longer have to include the disclosure on the employment of disabled persons in the directors' report, and large and medium companies have fewer directors' report items, for financial years beginning on or after 6 April 2025 ([SI 2024/1303, Explanatory Note, Part 2](https://www.legislation.gov.uk/uksi/2024/1303/made)).

### Year-end adjustments checklist

Source: [FRS 102, September 2024 edition](https://www.frc.org.uk/documents/7668/FRS_102_September_2024_tmKYWO6.pdf), which includes the Periodic Review 2024 amendments.

| # | Adjustment | UK-specific notes |
| --- | --- | --- |
| 1 | Depreciation | FRS 102 Section 17; useful life basis. Review residual value, useful life and method when there is an indication they have changed since the last reporting date, and treat a change as a change in estimate (para 17.19) |
| 2 | Accruals | Audit/accountancy fees, bonuses, utilities |
| 3 | Prepayments | Insurance, rent, software licences |
| 4 | Provisions | FRS 102 Section 21: recognise only for an obligation at the reporting date from a past event, where a transfer of economic benefits is probable and the amount can be estimated reliably (para 21.4) |
| 5 | Bad debt provision | Incurred loss model: impair where there is objective evidence of impairment (FRS 102 Section 11, para 11.21); no expected credit loss model |
| 6 | Inventory | Lower of cost and estimated selling price less costs to complete and sell (FRS 102 para 13.4) |
| 7 | Deferred tax | FRS 102 Section 29; recognised on timing differences (para 29.6), not temporary differences |
| 8 | Holiday pay accrual | Recognise the expected cost of accumulating compensated absences, such as untaken leave carried forward (FRS 102 para 28.6) |
| 9 | Lease accounting | FRS 102 Section 20: for accounting periods beginning on or after 1 January 2026, lessees follow an on-balance-sheet model based on IFRS 16, with simplifications. The FRC expects this to affect most entities that are lessees under operating leases |
| 10 | Revenue | FRS 102 Section 23 and FRS 105: for periods beginning on or after 1 January 2026, revenue follows a five-step model based on IFRS 15, with simplifications. Review contracts with customers for timing changes |
| 11 | R&D costs | Development costs meeting the criteria may be capitalised as a policy choice, or expensed (FRS 102 para 18.8H) |
| 12 | Government grants | Accrual model or performance model (FRS 102 para 24.4) |
| 13 | Director's loan account | S.455 CTA 2010 tax charge if overdrawn at year-end (see uk-dividends) |

### Profit and loss account format

The Small Companies and Groups (Accounts and Directors' Report) Regulations 2008 (SI 2008/409), Schedule 1, Part 1, Section B. A company shows the items in either format. Format 1 (by function) is the most common:

```
1. Turnover
2. Cost of sales
3. Gross profit or loss
4. Distribution costs
5. Administrative expenses
6. Other operating income
7. Income from shares in group undertakings
8. Income from participating interests
9. Income from other fixed asset investments
10. Other interest receivable and similar income
11. Amounts written off investments
12. Interest payable and similar expenses
13. Tax on profit or loss
14. Profit or loss after taxation
19. Other taxes not shown under the above items
20. Profit or loss for the financial year
```

Format 2 (by nature):

```
1. Turnover
2. Change in stocks of finished goods and in work in progress
3. Own work capitalised
4. Other operating income
5. (a) Raw materials and consumables (b) Other external charges
6. Staff costs: (a) wages and salaries (b) social security costs (c) other pension costs
7. (a) Depreciation and other amounts written off tangible and intangible fixed assets
   (b) Amounts written off current assets, to the extent that they exceed write-offs which are normal in the undertaking concerned
8. Other operating expenses
9 to 22. As Format 1 items 7 to 20
```

Operating profit is not a format item; many companies add it as a subtotal.

### Balance sheet format

SI 2008/409, Schedule 1, Part 1, Section B, Format 1 (main headings):

```
A. Called up share capital not paid
B. Fixed assets
   I. Intangible assets   II. Tangible assets   III. Investments
C. Current assets
   I. Stocks   II. Debtors   III. Investments   IV. Cash at bank and in hand
D. Prepayments and accrued income
E. Creditors: amounts falling due within one year
F. Net current assets (liabilities)
G. Total assets less current liabilities
H. Creditors: amounts falling due after more than one year
I. Provisions for liabilities
J. Accruals and deferred income
K. Capital and reserves
   I. Called up share capital   II. Share premium account   III. Revaluation reserve
   IV. Other reserves   V. Profit and loss account
```

Items A, D and J can be shown elsewhere as the notes to the formats allow (for example, prepayments within debtors, accruals within creditors).

### Notes to accounts: minimum disclosures by entity size

Source: [FRC, FRS 102](https://www.frc.org.uk/library/standards-codes-policy/accounting-and-reporting/uk-accounting-standards/frs-102/).

| # | Disclosure | Micro (FRS 105) | Small (s1A) | Medium/Large |
| --- | --- | --- | --- | --- |
| 1 | Accounting policies | Statutory only | Required | Full |
| 2 | Fixed assets movements | Not required | Required | Required |
| 3 | Financial commitments | Not required | Required | Required |
| 4 | Guarantees/contingencies | Required (on balance sheet) | Required | Required |
| 5 | Related party transactions | Not required | Required (FRS 102 para 1AC.35, applying paras 33.9 and 33.14) | Required (Section 33) |
| 6 | Employee numbers | Not required | Average number only | Full breakdown + costs |
| 7 | Directors' remuneration | Not required | No explicit FRS 102 requirement for periods beginning on or after 1 January 2026; disclose remuneration not concluded under normal market conditions (SI 2008/409 Sch 1 para 66) and use true and fair judgement (CA 2006 s.393) | Required (detailed) |
| 8 | Audit fees | Not required | Not required | Required |
| 9 | Financial instruments | Not required | Basic only | Full (Section 11/12) |
| 10 | Deferred tax | Not required | If material | Required (Section 29) |
| 11 | Share capital | Not required | Required | Required |
| 12 | Dividends | Not required | Required | Required |

## Boundary and exception table

### Audit requirements

Sources: [CA 2006 s.477](https://www.legislation.gov.uk/ukpga/2006/46/section/477), [s.478](https://www.legislation.gov.uk/ukpga/2006/46/section/478), [s.479A](https://www.legislation.gov.uk/ukpga/2006/46/section/479A); [Charities Act 2011 s.144](https://www.legislation.gov.uk/ukpga/2011/25/section/144).

| Category | Audit requirement |
| --- | --- |
| Micro-entity | Exempt (unless part of non-small group) |
| Small company | Exempt (same thresholds as small company classification) |
| Medium company | Required |
| Large company | Required |
| Public company | Always required (excluded from the small company exemption, s.478(a)) |
| Banking, insurance, e-money, MiFID investment firm, UCITS manager | Required (excluded, s.478(b)) |
| Charity in England & Wales, financial years ending on or after 30 September 2026 | Required if gross income is more than GBP 1.5 million, or more than the GBP 500,000 accounts threshold with gross assets over GBP 5 million (before: GBP 1 million, and GBP 250,000 with GBP 3.26 million) |
| Member of non-small group | Required (even if company itself is small) |
| Subsidiary of a UK parent | Can be exempt if all members agree, the parent guarantees its liabilities and it is consolidated (s.479A) |

### Conditions that override the small company audit exemption

- **Override conditions**: public company or member of a group containing a public company; regulated (banking, insurance, financial services); shareholders holding at least 10% in nominal value of the issued share capital (or of any class), or 10% of members if no share capital, give notice requiring an audit (s.476 CA 2006); part of an ineligible group (group exceeds small thresholds) ([s.476 CA 2006](https://www.legislation.gov.uk/ukpga/2006/46/section/476)).
- **Timing of a s.476 notice**: not before the financial year it relates to, and not later than one month before the end of that year (s.476(3) CA 2006).
- **From April 2028**: every company claiming audit exemption must give a strengthened eligibility statement ([Companies House, 23 October 2026](https://www.gov.uk/government/news/companies-house-update-to-accounts-filing-from-april-2028)).

### Auditor qualification

- **Registered Auditor**: must be a Registered Auditor (member of a Recognised Supervisory Body: ICAEW, ICAS, CAI, ACCA). The FRC lists these four as the current RSBs for statutory audit ([FRC, Recognition of RSBs and RQBs](https://www.frc.org.uk/library/supervision/professional-bodies-supervision/supervision-of-audit/recognition-of-rsbs-and-rqbs/)).

### Edge cases

| Situation | Treatment |
| --- | --- |
| First financial year | That year's figures alone decide the size class |
| Company crosses a limit in one year only | Size class does not change until the second consecutive year |
| Company was medium under the old limits | Look back: count last year as small if it would have qualified under the new limits (SI 2024/1303 reg 3) |
| Small company in a group with a public company | Excluded from the small regime and from audit exemption |
| Micro-entity accounts with only the minimum items | Directors disregard any standard requiring more information (s.393(1A)) |

## Worked cases

All amounts are illustrations, not client data. Each criterion counts as met (1) when the figure is not more than the limit, and not met (0) when it is above: met = max(0, min(1, floor((limit - figure) / limit) + 1)).

**Case 1 (decision, both ways): micro-entity or small company?** A private company in its third year has turnover of GBP 900,000 and a balance sheet total of GBP 550,000 in both this year and last year. With 8 employees in both years it meets 2 of the 3 micro limits (turnover and employees; the balance sheet total is over GBP 500,000), so it is a micro-entity and may prepare FRS 105 accounts and file a balance sheet only. With 12 employees in both years it meets only 1 micro limit (turnover), so it is not a micro-entity; it meets all 3 small limits, so it is small and prepares FRS 102 Section 1A accounts. The deciding figure is the employee count against the limit of 10.

```oa-check
name: Micro or small, 8 employees against 12 (limits from 6 April 2025)
inputs:
  turnover: 900000
  balance_sheet: 550000
  employees_a: 8
  employees_b: 12
  micro_turnover: 1000000
  micro_balance: 500000
  micro_employees: 10
  small_turnover: 15000000
  small_balance: 7500000
  small_employees: 50
steps:
  - t_micro: max(0, min(1, floor((micro_turnover - turnover) / micro_turnover) + 1))
  - b_micro: max(0, min(1, floor((micro_balance - balance_sheet) / micro_balance) + 1))
  - e_micro_a: max(0, min(1, floor((micro_employees - employees_a) / micro_employees) + 1))
  - e_micro_b: max(0, min(1, floor((micro_employees - employees_b) / micro_employees) + 1))
  - micro_met_a: t_micro + b_micro + e_micro_a
  - micro_met_b: t_micro + b_micro + e_micro_b
  - is_micro_a: min(1, floor(micro_met_a / 2))
  - is_micro_b: min(1, floor(micro_met_b / 2))
  - t_small: max(0, min(1, floor((small_turnover - turnover) / small_turnover) + 1))
  - b_small: max(0, min(1, floor((small_balance - balance_sheet) / small_balance) + 1))
  - e_small_b: max(0, min(1, floor((small_employees - employees_b) / small_employees) + 1))
  - small_met_b: t_small + b_small + e_small_b
  - is_small_b: min(1, floor(small_met_b / 2))
expected:
  micro_met_a: 2
  micro_met_b: 1
  is_micro_a: 1
  is_micro_b: 0
  small_met_b: 3
  is_small_b: 1
```

**Case 2: late filing penalty, late two years running.** A private company with a 31 December 2025 year end must file by 30 September 2026 (nine months). It files on 15 January 2027, more than 3 but not more than 6 months late. The table penalty is GBP 750; because its 2024 accounts were also filed late, the penalty is doubled to GBP 1,500.

```oa-check
name: Private company penalty, 3 to 6 months late, previous year also late
inputs:
  table_penalty: 750
  previous_year_late: 1
steps:
  - multiplier: 1 + previous_year_late
  - penalty: table_penalty * multiplier
expected:
  multiplier: 2
  penalty: 1500
```

## When to refuse or refer

- Refer the audit itself to a Registered Auditor; this skill only decides whether one is needed.
- Refer group accounts for a parent with securities on a UK regulated market (UK-adopted IFRS) to a specialist.
- Refer charities beyond the audit test (SORP accounts, independent examination) to a charity specialist.
- Refer where the size class turns on disputed figures (for example the average employee count or group aggregation) until the figures are settled.
- Refer regulated entities (banking, insurance, e-money, MiFID, UCITS) to a specialist.
- Do not sign or file accounts on behalf of directors without their approval: the directors approve and sign.

### Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

## Filing and payment

### Filing requirements

Sources: [CA 2006 s.442](https://www.legislation.gov.uk/ukpga/2006/46/section/442), [s.444](https://www.legislation.gov.uk/ukpga/2006/46/section/444).

| Item | Detail |
| --- | --- |
| Filing authority | Companies House |
| Filing method | Today: commercial software, Companies House WebFiling (signed in with GOV.UK One Login since 13 October 2025) or paper. From April 2028: accounts by commercial software in iXBRL only; web and paper filing close for accounts |
| Private company deadline | 9 months after the end of the accounting reference period |
| Public company deadline | 6 months after the end of the accounting reference period |
| First accounts (first period longer than 12 months) | 9 months (private) or 6 months (public) from the first anniversary of incorporation, or 3 months after the end of the accounting reference period if that is later. For a private company this is usually 21 months after incorporation |
| Shortened accounting reference period | The normal deadline, or 3 months from the date of the notice changing the date, whichever is later (s.442(4)) |
| Extension by the Secretary of State | Must be applied for before the deadline; cannot take the deadline beyond 12 months after the end of the period (s.442(5A)) |
| Extending the period | Not more than 18 months; not again within 5 years of an earlier extension, with group exceptions (s.392(3) and (5)) |
| Documents filed (small) | Balance sheet and notes; the profit and loss account and directors' report can be left off the public record ("filleted"). Abridged accounts need a statement that all members consented (s.444(2A)). Both options continue after April 2028 |
| Documents filed (micro) | Balance sheet only (with statutory footnotes) |
| Documents filed (medium/large) | Full accounts + directors' report + strategic report + auditor's report |
| iXBRL | Required for corporation tax filing to HMRC, through commercial software since HMRC's free filing service closed on 31 March 2026. Required at Companies House for accounts from April 2028 |
| Language | English or Welsh |

### Late filing penalties

Sources: [SI 2008/497 reg 4](https://www.legislation.gov.uk/uksi/2008/497/regulation/4); [gov.uk](https://www.gov.uk/annual-accounts/penalties-for-late-filing).

| Delay | Penalty (private company) | Source |
| --- | --- | --- |
| Up to 1 month | GBP 150 | https://www.gov.uk/annual-accounts/penalties-for-late-filing |
| 1 to 3 months | GBP 375 | same |
| 3 to 6 months | GBP 750 | same |
| Over 6 months | GBP 1,500 | same |

- **Public company penalties**: GBP 750, GBP 1,500, GBP 3,000 and GBP 7,500 for the same bands. Any company pays double if it also failed to file on time for the previous financial year (SI 2008/497 reg 4).
- The penalty is a civil penalty on the company (CA 2006 s.453). No change to these amounts had been made by 14 November 2026.

### Companies House: identity verification and the ECCTA filing changes

The Economic Crime and Corporate Transparency Act 2023 (ECCTA) changes how companies file. What is in force on 14 November 2026, and what is fixed for later:

**In force now**

- **Identity verification is a legal requirement since 18 November 2025.** Each director gives their Companies House personal code with the company's next confirmation statement, for each company they direct. A new company gives each director's code in the registration filing. An overseas company confirms all directors have verified by the anniversary of its UK establishment's registration ([when you need to verify](https://www.gov.uk/guidance/when-you-need-to-verify-your-identity-for-companies-house)).
- **People with significant control (PSCs)** verify and give their code within a 14-day window. A PSC who is also a director: 14 days from the day after the confirmation statement date. A PSC who is not a director: the first 14 days of their birth month. A PSC added after 18 November 2025: on being added or within 14 days (same page).
- **Agents.** Accountants who want to verify clients' identities register as Authorised Corporate Service Providers (ACSPs). Companies House says businesses filing for clients will in future also need to register (same page).
- **Not yet in force:** identity verification for people who file at Companies House, limited partnerships, corporate directors, corporate members of LLPs and officers of corporate PSCs (same page).
- **WebFiling sign-in** has used GOV.UK One Login since 13 October 2025 ([filing online](https://www.gov.uk/guidance/filing-your-companies-house-information-online)).
- Registered email address, appropriate registered office and the lawful purpose statement (in force since 4 March 2024: ECCTA ss.2, 28 and 29, brought into force by [SI 2024/269 reg 2](https://www.legislation.gov.uk/uksi/2024/269/made)) are covered in uk-formation.

**From April 2028 (announced 23 October 2026)** ([Companies House](https://www.gov.uk/government/news/companies-house-update-to-accounts-filing-from-april-2028)):

- All UK companies file accounts in iXBRL using commercial software. Web and paper filing close for accounts; WebFiling stays open for confirmation statements and other non-accounts filings.
- A strengthened eligibility statement for every company claiming audit exemption.
- The component parts of the accounts and reports must be filed together.
- A limit on how many times a company can shorten its accounting reference period.
- **Paused:** the requirement for small companies and micro-entities to file a profit and loss account. Abridged accounts and "filleting" stay available after 1 April 2028.
- The new filing rules in CA 2006 s.444 (substituted by ECCTA s.54) are not yet in force, except the power to make regulations ([CA 2006 s.444](https://www.legislation.gov.uk/ukpga/2006/46/section/444)).

## Completion checklist

- [ ] Size class set with the 2-of-3 test, the two-year rule and the look-back; group limits applied for a parent.
- [ ] Exclusions checked (public, regulated, ineligible group).
- [ ] Framework chosen and Periodic Review 2024 changes applied for periods from 1 January 2026.
- [ ] Year-end adjustments made (leases, revenue, provisions, deferred tax, holiday pay, director's loan account).
- [ ] Statements in the statutory formats, with the notes the size class needs.
- [ ] Audit exemption decided; any s.476 notice checked.
- [ ] Filing deadline worked out (first period, shortened period, extension).
- [ ] Directors and PSCs verified; filing agent registered as ACSP where needed.
- [ ] iXBRL accounts and CT600 filed through commercial software.

## Sources

| Source | What was read | URL | Read on |
|---|---|---|---|
| Companies Act 2006 s.382 | Read for the small limits (GBP 15 million, GBP 7.5 million, 50) and the two consecutive years rule | https://www.legislation.gov.uk/ukpga/2006/46/section/382 | 2026-11-14 |
| Companies Act 2006 s.384A | Read for the micro limits (GBP 1 million, GBP 500,000, 10) | https://www.legislation.gov.uk/ukpga/2006/46/section/384A | 2026-11-14 |
| Companies Act 2006 s.465 | Read for the medium limits (GBP 54 million, GBP 27 million, 250) | https://www.legislation.gov.uk/ukpga/2006/46/section/465 | 2026-11-14 |
| SI 2024/1303 | Read for the replaced limits, the group net and gross limits and the 6 April 2025 start | https://www.legislation.gov.uk/uksi/2024/1303/made | 2026-11-14 |
| Companies Act 2006 s.392 | Read for the 18-month limit and the five-year bar on another extension | https://www.legislation.gov.uk/ukpga/2006/46/section/392 | 2026-11-14 |
| Companies Act 2006 s.414A | Read for the strategic report and the small company exemption | https://www.legislation.gov.uk/ukpga/2006/46/section/414A | 2026-11-14 |
| Companies Act 2006 s.415 | Read for the directors' report and the micro-entity exemption | https://www.legislation.gov.uk/ukpga/2006/46/section/415 | 2026-11-14 |
| Companies Act 2006 s.442 | Read for nine and six months, first accounts over twelve months and three months after the period end | https://www.legislation.gov.uk/ukpga/2006/46/section/442 | 2026-11-14 |
| Companies Act 2006 s.444 | Read for the small company filing options and the ECCTA substitution not yet in force | https://www.legislation.gov.uk/ukpga/2006/46/section/444 | 2026-11-14 |
| Companies Act 2006 s.445 | Read for filing by medium-sized companies | https://www.legislation.gov.uk/ukpga/2006/46/section/445 | 2026-11-14 |
| Companies Act 2006 s.453 | Read for the civil penalty on the company | https://www.legislation.gov.uk/ukpga/2006/46/section/453 | 2026-11-14 |
| SI 2008/497 reg 4 | Read for the private and public penalty bands and doubling | https://www.legislation.gov.uk/uksi/2008/497/regulation/4 | 2026-11-14 |
| GOV.UK, Penalties for late filing | Read for GBP 150, 375, 750, 1,500 and doubling when late 2 years in a row | https://www.gov.uk/annual-accounts/penalties-for-late-filing | 2026-11-14 |
| Companies Act 2006 s.476 | Read for the 10% members' notice and the one-month timing | https://www.legislation.gov.uk/ukpga/2006/46/section/476 | 2026-11-14 |
| Companies Act 2006 s.477 | Read for the small company audit exemption | https://www.legislation.gov.uk/ukpga/2006/46/section/477 | 2026-11-14 |
| Companies Act 2006 s.478 | Read for the companies excluded from the small company exemption | https://www.legislation.gov.uk/ukpga/2006/46/section/478 | 2026-11-14 |
| Companies Act 2006 s.479A | Read for the subsidiary audit exemption with a parent guarantee | https://www.legislation.gov.uk/ukpga/2006/46/section/479A | 2026-11-14 |
| Charities Act 2011 s.144 | Read for the GBP 1.5 million charity audit threshold as amended | https://www.legislation.gov.uk/ukpga/2011/25/section/144 | 2026-11-14 |
| SI 2026/427, Charities Acts 1992 and 2011 (Substitution of Sums) Order 2026 | Read for GBP 1 million to 1.5 million, GBP 250,000 to 500,000, GBP 3.26 million to 5 million, and years ending on or after 30 September 2026 | https://www.legislation.gov.uk/uksi/2026/427/made | 2026-11-14 |
| FRC, FRS 102 page | Read for the Periodic Review 2024 effective date and the 2027 format amendments | https://www.frc.org.uk/library/standards-codes-policy/accounting-and-reporting/uk-accounting-standards/frs-102/ | 2026-11-14 |
| FRC, Amendments to FRS 102 and other FRSs: Periodic Review 2024 | Read for the summary of the revenue and lease changes | https://www.frc.org.uk/documents/7128/Amendments_to_FRS_102_and_other_FRSs.pdf | 2026-11-14 |
| FRC, FRS 102 (September 2024 edition) | Read for paras 1AC.35, 11.21, 13.4, 17.19, 18.8H, 21.4, 24.4, 28.6, 29.6 | https://www.frc.org.uk/documents/7668/FRS_102_September_2024_tmKYWO6.pdf | 2026-11-14 |
| FRC, FRS 101 Reduced Disclosure Framework | Read for the scope of FRS 101 | https://www.frc.org.uk/library/standards-codes-policy/accounting-and-reporting/uk-accounting-standards/frs-101/ | 2026-11-14 |
| Companies House, update to accounts filing from April 2028 (23 October 2026) | Read for software-only filing, the audit exemption statement, the shortening limit and profit and loss filing after 1 April 2028 | https://www.gov.uk/government/news/companies-house-update-to-accounts-filing-from-april-2028 | 2026-11-14 |
| Companies House, When you need to verify your identity | Read for 18 November 2025, the 14-day PSC windows and the birth month rule | https://www.gov.uk/guidance/when-you-need-to-verify-your-identity-for-companies-house | 2026-11-14 |
| Companies House, Filing your Companies House information online | Read for GOV.UK One Login from 13 October 2025 | https://www.gov.uk/guidance/filing-your-companies-house-information-online | 2026-11-14 |
| Companies House, Filing your Companies House accounts | Read for the accounts filing guidance and the notice period for changes | https://www.gov.uk/government/publications/filing-your-companies-house-accounts | 2026-11-14 |
| HMRC, Closure of the service to file company accounts and tax return | Read for the closure on 31 March 2026 | https://www.gov.uk/guidance/closure-of-the-service-to-file-your-company-accounts-and-tax-return | 2026-11-14 |
| SI 2008/409 Schedule 1 | Read for the profit and loss and balance sheet formats | https://www.legislation.gov.uk/uksi/2008/409/schedule/1 | 2026-11-14 |
| Companies Act 2006 s.393 | Read for the true and fair view and s.393(1A) for micro-entities | https://www.legislation.gov.uk/ukpga/2006/46/section/393 | 2026-11-14 |
| Companies Act 2006 s.395 | Read for the individual accounts framework choice | https://www.legislation.gov.uk/ukpga/2006/46/section/395 | 2026-11-14 |
| Companies Act 2006 s.403 | Read for IFRS group accounts for parents on a UK regulated market | https://www.legislation.gov.uk/ukpga/2006/46/section/403 | 2026-11-14 |
| SI 2024/269 (ECCTA Commencement No. 1) reg 2 | Read for the 4 March 2024 commencement | https://www.legislation.gov.uk/uksi/2024/269/made | 2026-11-14 |
| FRC, Recognition of RSBs and RQBs | Read for the four recognised supervisory bodies | https://www.frc.org.uk/library/supervision/professional-bodies-supervision/supervision-of-audit/recognition-of-rsbs-and-rqbs/ | 2026-11-14 |

Not yet confirmed: the exact date in April 2028 for the Companies House changes (the announcement says "from April 2028" and "after 1 April 2028"); the content of the strengthened audit-exemption statement and the limit on shortening periods (regulations not yet read); the disclosure table rows other than related parties and directors' remuneration (carried from the previous version, not re-read against FRS 102 Section 1A, FRS 105 or SI 2008/409); the previous version's statements that FRS 105 has "no true and fair override" and that AIM groups must use IFRS (removed in v1.3: the Companies Act sets the IFRS requirement only for parents on a UK regulated market, s.403(1); the AIM requirement was not checked).
