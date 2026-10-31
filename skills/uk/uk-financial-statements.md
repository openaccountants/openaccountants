---
name: uk-financial-statements
description: Use this skill when preparing, reviewing, or advising on annual financial statements for a UK company. Trigger on phrases like "Companies House accounts", "FRS 102", "FRS 105", "micro-entity accounts", "small company accounts", "abbreviated accounts", "directors' report UK", "filing accounts UK", "audit exemption UK", "year-end adjustments UK", "iXBRL", "abridged accounts", "identity verification Companies House", "software filing April 2028", or any question about preparing statutory accounts under the Companies Act 2006. Covers FRS 102/105 frameworks (Periodic Review 2024 in force from 1 January 2026), the size thresholds raised for financial years beginning on or after 6 April 2025, required statements, P&L and balance sheet formats, notes, filing deadlines, late filing penalties, audit requirements, and the Economic Crime and Corporate Transparency Act changes in force in 2026 or due from April 2028. Position at 30 October 2026.
version: 1.3
jurisdiction: GB
tax_year: 2026
last_updated: 2026-10-31
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
source_checked: 2026-10-16
depends_on:
  - financial-statements-workflow-base
category: financial-statements
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# UK Financial Statements

## UK Financial Statements Skill v1.3

> **Year applicability:** This version gives the position at 30 October 2026. The size thresholds apply to financial years beginning on or after 6 April 2025, so they govern accounts for 2025/26 and 2026/27 year ends. FRS 102 and FRS 105 changes from the Periodic Review 2024 apply to accounting periods beginning on or after 1 January 2026. Where a rule changes on a later date (April 2028 filing reforms), the date is given. Read alongside uk-corporation-tax (the CT600 and its iXBRL accounts) and uk-formation (identity verification and other Companies House rules at formation).

## Rates and thresholds

These figures were re-read against the Companies Act 2006 and the regulations on legislation.gov.uk on 30 October 2026.

### Financial Statements

- **Micro: turnover**: not more than £1,000,000  _([CA 2006 s.384A](https://www.legislation.gov.uk/ukpga/2006/46/section/384A))_
- **Micro: balance sheet total**: not more than £500,000  _([CA 2006 s.384A](https://www.legislation.gov.uk/ukpga/2006/46/section/384A))_
- **Micro: employees**: not more than 10  _([CA 2006 s.384A](https://www.legislation.gov.uk/ukpga/2006/46/section/384A))_
- **Small: turnover**: not more than £15,000,000  _([CA 2006 s.382](https://www.legislation.gov.uk/ukpga/2006/46/section/382))_
- **Small: balance sheet total**: not more than £7,500,000  _([CA 2006 s.382](https://www.legislation.gov.uk/ukpga/2006/46/section/382))_
- **Small: employees**: not more than 50  _([CA 2006 s.382](https://www.legislation.gov.uk/ukpga/2006/46/section/382))_
- **Medium: turnover**: not more than £54,000,000  _([CA 2006 s.465](https://www.legislation.gov.uk/ukpga/2006/46/section/465))_
- **Medium: balance sheet total**: not more than £27,000,000  _([CA 2006 s.465](https://www.legislation.gov.uk/ukpga/2006/46/section/465))_
- **Medium: employees**: not more than 250  _([CA 2006 s.465](https://www.legislation.gov.uk/ukpga/2006/46/section/465))_
- **Test**: 2 or more of the 3 criteria; the first financial year on its own, then a change only counts if it occurs in two consecutive financial years  _([CA 2006 s.382](https://www.legislation.gov.uk/ukpga/2006/46/section/382))_
- **Private company deadline**: 9 months after the end of the accounting reference period  _([CA 2006 s.442](https://www.legislation.gov.uk/ukpga/2006/46/section/442))_
- **Public company deadline**: 6 months after the end of the accounting reference period  _([CA 2006 s.442](https://www.legislation.gov.uk/ukpga/2006/46/section/442))_
- **Late filing penalty (private)**: £150 to £1,500  _([SI 2008/497 reg 4](https://www.legislation.gov.uk/uksi/2008/497/regulation/4))_
- **Late filing penalty (public)**: £750 to £7,500  _([SI 2008/497 reg 4](https://www.legislation.gov.uk/uksi/2008/497/regulation/4))_
- **Small company (including micro)**: exempt from audit, unless excluded  _([CA 2006 s.477](https://www.legislation.gov.uk/ukpga/2006/46/section/477), [s.478](https://www.legislation.gov.uk/ukpga/2006/46/section/478))_
- **Medium/large company**: audit required  _([CA 2006 s.477](https://www.legislation.gov.uk/ukpga/2006/46/section/477))_
- **10% shareholder request**: overrides the small company exemption  _([CA 2006 s.476](https://www.legislation.gov.uk/ukpga/2006/46/section/476))_

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | United Kingdom |
| Currency | GBP |
| Filing authority | Companies House |
| Primary legislation | Companies Act 2006 |
| Supporting regulations | The Small Companies and Groups (Accounts and Directors' Report) Regulations 2008; The Large and Medium-sized Companies and Groups (Accounts and Reports) Regulations 2008 |
| Accounting standards | FRS 102 (full / Section 1A); FRS 105 (micro); UK-adopted IFRS (listed/choice). Periodic Review 2024 amendments apply to periods beginning on or after 1 January 2026 Source: https://www.frc.org.uk/library/standards-codes-policy/accounting-and-reporting/uk-accounting-standards/frs-102/ (tax year 2026) (read 2026-10-31) |
| Financial year | Usually 12 months; an accounting reference period may not be extended beyond 18 months (CA 2006 s.392(5)) Source: https://www.legislation.gov.uk/ukpga/2006/46/section/392 (tax year 2026) (read 2026-10-31) |
| Filing deadline | 9 months after the end of the accounting reference period (private); 6 months (public) Source: https://www.gov.uk/government/publications/filing-your-companies-house-accounts (tax year 2026) (read 2026-10-31) |
| Late filing penalty | £150 to £1,500 (private); £750 to £7,500 (public); doubled if the previous year's accounts were also late Source: https://www.legislation.gov.uk/uksi/2008/497/regulation/4 (tax year 2026) (read 2026-10-31) |
| Digital filing | HMRC: accounts and CT600 in iXBRL through commercial software from 1 April 2026. Companies House: software, WebFiling or paper today; software only (iXBRL) for accounts from April 2028 Sources: https://www.gov.uk/guidance/closure-of-the-service-to-file-your-company-accounts-and-tax-return (HMRC) and https://www.gov.uk/government/news/companies-house-update-to-accounts-filing-from-april-2028 (Companies House) (tax year 2026) (read 2026-10-31) |
| Identity verification | Compulsory for directors and PSCs since 18 November 2025 (Section 11) |

## Section 2 -- Reporting Framework

**Reporting Framework**

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

## Section 3 -- Size Thresholds

Effective for financial years beginning on or after 6 April 2025 (SI 2024/1303 reg 2(2)):

**Size Thresholds (current)**

| Criterion | Micro | Small | Medium |
| --- | --- | --- | --- |
| Turnover | ≤ £1,000,000 | ≤ £15,000,000 | ≤ £54,000,000 |
| Balance sheet total | ≤ £500,000 | ≤ £7,500,000 | ≤ £27,000,000 |
| Employees | ≤ 10 | ≤ 50 | ≤ 250 |

- **Classification test**: must meet 2 or more of the 3 criteria. In the first financial year that year alone counts; after that, meeting or ceasing to meet the criteria only changes the size category if it occurs in two consecutive financial years. Companies exceeding "medium" thresholds are classified as large.  _([CA 2006 s.382](https://www.legislation.gov.uk/ukpga/2006/46/section/382))_
- **Looking back at earlier years**: when sizing a company for a financial year beginning on or after 6 April 2025, it is treated as having qualified in any earlier year in which it would have qualified had the new thresholds applied then. So a company that was medium last year under the old limits can count last year as small under the new ones.  _([SI 2024/1303 reg 3](https://www.legislation.gov.uk/uksi/2024/1303/made))_
- **Parent companies and groups**: small group not more than £15 million net (£18 million gross) turnover and £7.5 million net (£9 million gross) balance sheet total; medium group not more than £54 million net (£64 million gross) and £27 million net (£32 million gross); employee limits as above.  _([SI 2024/1303 regs 9 and 10](https://www.legislation.gov.uk/uksi/2024/1303/made))_
- **LLPs**: the same raised thresholds apply to limited liability partnerships.  _([SI 2024/1303 reg 11](https://www.legislation.gov.uk/uksi/2024/1303/made))_

**Previous thresholds (financial years beginning before 6 April 2025)**

| Criterion | Micro | Small | Medium |
| --- | --- | --- | --- |
| Turnover | ≤ £632,000 | ≤ £10,200,000 | ≤ £36,000,000 |
| Balance sheet total | ≤ £316,000 | ≤ £5,100,000 | ≤ £18,000,000 |
| Employees | ≤ 10 | ≤ 50 | ≤ 250 |

## Section 4 -- Required Financial Statements

**Required Financial Statements**  _([CA 2006 s.414A](https://www.legislation.gov.uk/ukpga/2006/46/section/414A), [s.415](https://www.legislation.gov.uk/ukpga/2006/46/section/415))_

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

## Section 5 -- Year-End Adjustments Checklist

**Year-End Adjustments Checklist**  _([FRS 102, September 2024 edition](https://www.frc.org.uk/documents/7668/FRS_102_September_2024_tmKYWO6.pdf), which includes the Periodic Review 2024 amendments)_

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

## Section 6 -- Profit and Loss Account Format

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

## Section 7 -- Balance Sheet Format

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

## Section 8 -- Notes to Accounts

### Minimum disclosures by entity size

**Minimum disclosures by entity size**  _([FRC, FRS 102](https://www.frc.org.uk/library/standards-codes-policy/accounting-and-reporting/uk-accounting-standards/frs-102/))_

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

## Section 9 -- Filing Requirements

**Filing Requirements**  _([CA 2006 s.442](https://www.legislation.gov.uk/ukpga/2006/46/section/442), [s.444](https://www.legislation.gov.uk/ukpga/2006/46/section/444))_

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

### Late Filing Penalties (private companies)

**Late Filing Penalties (private companies)**  _([SI 2008/497 reg 4](https://www.legislation.gov.uk/uksi/2008/497/regulation/4); [gov.uk](https://www.gov.uk/annual-accounts/penalties-for-late-filing))_

| Delay | Penalty |
| --- | --- |
| Up to 1 month | £150 |
| 1 to 3 months | £375 |
| 3 to 6 months | £750 |
| Over 6 months | £1,500 |

- **Public company penalties**: £750, £1,500, £3,000 and £7,500 for the same bands. Any company pays double if it also failed to file on time for the previous financial year.  _([SI 2008/497 reg 4](https://www.legislation.gov.uk/uksi/2008/497/regulation/4))_
- The penalty is a civil penalty on the company (CA 2006 s.453). No change to these amounts had been made by 30 October 2026.

## Section 10 -- Audit Requirements

**Audit Requirements**  _([CA 2006 s.477](https://www.legislation.gov.uk/ukpga/2006/46/section/477), [s.478](https://www.legislation.gov.uk/ukpga/2006/46/section/478), [s.479A](https://www.legislation.gov.uk/ukpga/2006/46/section/479A); [Charities Act 2011 s.144](https://www.legislation.gov.uk/ukpga/2011/25/section/144))_

| Category | Audit requirement |
| --- | --- |
| Micro-entity | Exempt (unless part of non-small group) |
| Small company | Exempt (same thresholds as small company classification) |
| Medium company | Required |
| Large company | Required |
| Public company | Always required (excluded from the small company exemption, s.478(a)) |
| Banking, insurance, e-money, MiFID investment firm, UCITS manager | Required (excluded, s.478(b)) |
| Charity in England & Wales, financial years ending on or after 30 September 2026 | Required if gross income is more than £1.5 million, or more than the £500,000 accounts threshold with gross assets over £5 million (before: £1 million, and £250,000 with £3.26 million) |
| Member of non-small group | Required (even if company itself is small) |
| Subsidiary of a UK parent | Can be exempt if all members agree, the parent guarantees its liabilities and it is consolidated (s.479A) |

### Conditions that override small company audit exemption:

- **Override conditions**: public company or member of a group containing a public company; regulated (banking, insurance, financial services); shareholders holding at least 10% in nominal value of the issued share capital (or of any class), or 10% of members if no share capital, give notice requiring an audit (s.476 CA 2006); part of an ineligible group (group exceeds small thresholds)  _([s.476 CA 2006](https://www.legislation.gov.uk/ukpga/2006/46/section/476))_
- **Timing of a s.476 notice**: not before the financial year it relates to, and not later than one month before the end of that year.  _([s.476(3) CA 2006](https://www.legislation.gov.uk/ukpga/2006/46/section/476))_
- **From April 2028**: every company claiming audit exemption must give a strengthened eligibility statement.  _([Companies House, 23 October 2026](https://www.gov.uk/government/news/companies-house-update-to-accounts-filing-from-april-2028))_

### Auditor qualification

- **Registered Auditor**: must be a Registered Auditor (member of a Recognised Supervisory Body: ICAEW, ICAS, CAI, ACCA). The FRC lists these four as the current RSBs for statutory audit ([FRC, Recognition of RSBs and RQBs](https://www.frc.org.uk/library/supervision/professional-bodies-supervision/supervision-of-audit/recognition-of-rsbs-and-rqbs/)).

## Section 11 -- Companies House: identity verification and the ECCTA filing changes

The Economic Crime and Corporate Transparency Act 2023 (ECCTA) changes how companies file. What is in force on 30 October 2026, and what is fixed for later:

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

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

## Sources

| Source | URL | Read on |
|---|---|---|
| Companies Act 2006 s.382 (small: qualifying conditions) | https://www.legislation.gov.uk/ukpga/2006/46/section/382 | 2026-10-30 |
| Companies Act 2006 s.384A (micro-entities) | https://www.legislation.gov.uk/ukpga/2006/46/section/384A | 2026-10-30 |
| Companies Act 2006 s.465 (medium-sized) | https://www.legislation.gov.uk/ukpga/2006/46/section/465 | 2026-10-30 |
| SI 2024/1303, Companies (Accounts and Reports) (Amendment and Transitional Provision) Regulations 2024 | https://www.legislation.gov.uk/uksi/2024/1303/made | 2026-10-30 |
| Companies Act 2006 s.392 (accounting reference date) | https://www.legislation.gov.uk/ukpga/2006/46/section/392 | 2026-10-30 |
| Companies Act 2006 s.414A (strategic report) | https://www.legislation.gov.uk/ukpga/2006/46/section/414A | 2026-10-30 |
| Companies Act 2006 s.415 (directors' report) | https://www.legislation.gov.uk/ukpga/2006/46/section/415 | 2026-10-30 |
| Companies Act 2006 s.442 (period for filing) | https://www.legislation.gov.uk/ukpga/2006/46/section/442 | 2026-10-30 |
| Companies Act 2006 s.444 (filing: small companies) | https://www.legislation.gov.uk/ukpga/2006/46/section/444 | 2026-10-30 |
| Companies Act 2006 s.453 (civil penalty) | https://www.legislation.gov.uk/ukpga/2006/46/section/453 | 2026-10-30 |
| Companies Act 2006 s.392 (accounting reference date, 18-month limit) | https://www.legislation.gov.uk/ukpga/2006/46/section/392 | 2026-10-31 |
| SI 2008/497 reg 4 (late filing penalties) | https://www.legislation.gov.uk/uksi/2008/497/regulation/4 | 2026-10-31 |
| GOV.UK, Penalties for late filing | https://www.gov.uk/annual-accounts/penalties-for-late-filing | 2026-10-30 |
| Companies Act 2006 s.476, s.477, s.478, s.479A (audit) | https://www.legislation.gov.uk/ukpga/2006/46/section/477 | 2026-10-30 |
| Charities Act 2011 s.144 (charity audit) | https://www.legislation.gov.uk/ukpga/2011/25/section/144 | 2026-10-30 |
| SI 2026/427, Charities Acts 1992 and 2011 (Substitution of Sums) Order 2026 | https://www.legislation.gov.uk/uksi/2026/427/made | 2026-10-30 |
| FRC, FRS 102 page (Periodic Review 2024, small entity directors' remuneration, 2027 amendments) | https://www.frc.org.uk/library/standards-codes-policy/accounting-and-reporting/uk-accounting-standards/frs-102/ | 2026-10-31 |
| FRC, Amendments to FRS 102 and other FRSs: Periodic Review 2024 (summary) | https://www.frc.org.uk/documents/7128/Amendments_to_FRS_102_and_other_FRSs.pdf | 2026-10-30 |
| Companies House, news story "Companies House update to accounts filing from April 2028", published 23 October 2026 | https://www.gov.uk/government/news/companies-house-update-to-accounts-filing-from-april-2028 | 2026-10-31 |
| Companies House, When you need to verify your identity | https://www.gov.uk/guidance/when-you-need-to-verify-your-identity-for-companies-house | 2026-10-30 |
| Companies House, Filing your Companies House information online | https://www.gov.uk/guidance/filing-your-companies-house-information-online | 2026-10-30 |
| Companies House, Filing your Companies House accounts | https://www.gov.uk/government/publications/filing-your-companies-house-accounts | 2026-10-31 |
| HMRC, Closure of the service to file company accounts and tax return | https://www.gov.uk/guidance/closure-of-the-service-to-file-your-company-accounts-and-tax-return | 2026-10-31 |
| FRC, FRS 102 (September 2024 edition), paras 1AC.35, 11.21, 13.4, 17.19, 18.8H, 21.4, 24.4, 28.6, 29.6 | https://www.frc.org.uk/documents/7668/FRS_102_September_2024_tmKYWO6.pdf | 2026-10-31 |
| FRC, FRS 101 Reduced Disclosure Framework | https://www.frc.org.uk/library/standards-codes-policy/accounting-and-reporting/uk-accounting-standards/frs-101/ | 2026-10-30 |
| SI 2008/409 Schedule 1 (formats) | https://www.legislation.gov.uk/uksi/2008/409/schedule/1 | 2026-10-30 |
| Companies Act 2006 s.393 (true and fair view; micro-entities) | https://www.legislation.gov.uk/ukpga/2006/46/section/393 | 2026-10-30 |
| Companies Act 2006 s.395 (individual accounts framework) | https://www.legislation.gov.uk/ukpga/2006/46/section/395 | 2026-10-30 |
| Companies Act 2006 s.403 (group accounts framework) | https://www.legislation.gov.uk/ukpga/2006/46/section/403 | 2026-10-30 |
| Companies Act 2006 s.445 (filing: medium-sized companies) | https://www.legislation.gov.uk/ukpga/2006/46/section/445 | 2026-10-30 |
| SI 2024/269 (ECCTA Commencement No. 1) reg 2 | https://www.legislation.gov.uk/uksi/2024/269/made | 2026-10-30 |
| FRC, Recognition of RSBs and RQBs | https://www.frc.org.uk/library/supervision/professional-bodies-supervision/supervision-of-audit/recognition-of-rsbs-and-rqbs/ | 2026-10-30 |

Not yet confirmed: the exact date in April 2028 for the Companies House changes (the announcement says "from April 2028" and "after 1 April 2028"); the content of the strengthened audit-exemption statement and the limit on shortening periods (regulations not yet read); the disclosure table rows other than related parties and directors' remuneration (carried from the previous version, not re-read against FRS 102 Section 1A, FRS 105 or SI 2008/409); the previous version's statements that FRS 105 has "no true and fair override" and that AIM groups must use IFRS (removed: the Companies Act sets the IFRS requirement only for parents on a UK regulated market, s.403(1); the AIM requirement was not checked).

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
