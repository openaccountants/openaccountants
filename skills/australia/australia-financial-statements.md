---
name: australia-financial-statements
description: Use this skill when preparing, reviewing, or advising on annual financial statements for an Australian company. Trigger on phrases like "ASIC financial report", "AASB", "Australian Accounting Standards", "general purpose financial statements", "special purpose financial statements", "large proprietary company", "small proprietary company", "directors' report Australia", "audit Australia", "Form 388", "Corporations Act 2001 reporting", or any question about preparing and filing statutory accounts under the Corporations Act 2001. Covers AASB frameworks, size thresholds (large/small proprietary), required statements, formats, notes, lodgement deadlines, and audit requirements.
version: 1.3
jurisdiction: AU
tax_year: 2025
last_updated: 2026-11-26
depends_on:
  - financial-statements-workflow-base
category: financial-statements
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: financial-statements
---

# Australia Financial Statements

## Australia Financial Statements Skill v1.3

## Section 1 -- Quick Reference

**Quick Reference**

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Australia (Commonwealth of Australia) |
| Currency | Determine functional and presentation currencies under AASB 121 |
| Filing authority | Australian Securities and Investments Commission (ASIC) |
| Primary legislation | Corporations Act 2001 (Cth), Chapter 2M |
| Supporting legislation | Corporations Regulations 2001; ASIC Regulatory Guides |
| Accounting standards | Australian Accounting Standards (AASB) — substantially IFRS-equivalent |
| Financial year | Often 1 July to 30 June. Apply the first-year, subsequent-year and consolidation rules in section 323D |
| Lodgement deadline | Generally 4 months from year-end. Disclosing entities, registered schemes, registrable superannuation entities and notified foreign passport funds generally have 3 months |
| Late lodgement | ASIC late lodgement fees depend on how long the document is overdue. Check section 319 for separate consequences |
| Digital filing | Form 388 in the ASIC company officeholder, registered agent or auditor portal where applicable |

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

- **Tier 1** — Apply all relevant recognition, measurement, presentation and disclosure requirements of Australian Accounting Standards.  _([AASB 1053](https://standards.aasb.gov.au/aasb-1053-may-2022))_
- **Tier 2 — Simplified Disclosures** — Same recognition and measurement as Tier 1, reduced disclosures (AASB 1060)  _(AASB 1060)_
- **Which tier applies** — Apply the legislation and the public accountability criteria in AASB 1053. Select the AASB 1060 compilation applicable to the start of the reporting period.  _([AASB 1053](https://standards.aasb.gov.au/aasb-1053-may-2022), [AASB 1060 versions](https://standards.aasb.gov.au/superseded-versions?pronouncement=3895&standard_no=88))_
- **AASB 18 and Tier 2 transition** — AASB 18 replaces AASB 101 for relevant for-profit Tier 1 entities for annual periods beginning on or after 1 January 2027. The Tier 2 presentation amendments in AASB 2026-6 apply to annual periods beginning on or after 1 July 2030. Earlier application is permitted.  _([AASB 18](https://standards.aasb.gov.au/aasb-18-jun-2024), [AASB 2026-6](https://standards.aasb.gov.au/sites/default/files/2026-11/AASB2026-6_10-26.pdf))_

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
- **Measure on the statutory basis** — Apply the consolidated thresholds at the statutory measurement dates with the controlled-entity rules, and record the company type, ownership and control, reporting period, fundraising history and any regulator or member direction, because each can create a reporting duty independently of size.  _([ASIC, Company financial reports](https://www.asic.gov.au/for-business-and-companies/companies/company-financial-reports))_

### Reporting obligations by entity type

**Reporting obligations by entity type**

| Entity | Must prepare financial report? | Must lodge with ASIC? | Must audit? |
| --- | --- | --- | --- |
| Large proprietary | Yes | Yes (Form 388) | Yes |
| Small proprietary (general) | No (unless directed) | No | No |
| Small proprietary (foreign-controlled) | If section 292(2)(b) applies and ASIC relief is unavailable | Generally yes when required to report | Generally yes when required to report, subject to audit relief |
| Small proprietary (CSF shareholders) | Yes | Yes | If at least $3 million has been raised from all CSF offers by year-end or another audit requirement applies |
| Public company | Generally yes | Generally yes | Generally yes, subject to separate rules for companies limited by guarantee and charities |
| Disclosing entity | Yes | Yes | Yes |

## Section 4 -- Required Financial Statements

- **Statutory basis** — Under s.295 and s.296 Corporations Act + AASB standards  _(s.295, s.296 Corporations Act)_
- **Presentation choices** — Include comparatives, check permitted exceptions such as the AASB 1060 option for a combined statement of income and retained earnings, and analyse functional and presentation currency under AASB 121; Australian dollar presentation is not compulsory in every case. Public companies also check the consolidated entity disclosure statement requirements.  _([ASIC, Company financial reports](https://www.asic.gov.au/for-business-and-companies/companies/company-financial-reports))_

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
| Auditor's Report | Separate report where a statutory audit or review is required | Same statutory test as Tier 1 |

## Section 5 -- Year-End Adjustments Checklist

**Year-End Adjustments Checklist**

| # | Adjustment | Australia-specific notes |
| --- | --- | --- |
| 1 | Depreciation | AASB 116; systematic allocation; annual review of useful life and residual value |
| 2 | Provisions | AASB 137; present obligation, probable outflow, reliable estimate |
| 3 | Employee benefits | AASB 119. Measure long service leave using expected benefit payments, including the probability of employees qualifying where relevant. |
| 4 | Impairment | AASB 136; compare carrying amount to recoverable amount |
| 5 | Expected credit losses | AASB 9 paragraph 5.5.15. Use lifetime expected credit losses for qualifying trade receivables without a significant financing component. For receivables with such a component, check the accounting policy election. |
| 6 | Inventory | AASB 102; lower of cost (FIFO/weighted average) and NRV; no LIFO |
| 7 | Deferred tax | AASB 112. Apply enacted or substantively enacted rates expected when the asset is realised or the liability settled. Ordinary company rates are 25% for base rate entities and 30% for other companies. |
| 8 | Lease accounting | AASB 16; right-of-use asset + lease liability (exemptions for short-term/low-value) |
| 9 | Revenue recognition | AASB 15; five-step model; performance obligations |
| 10 | Financial instruments | AASB 9; classification and measurement; hedge accounting |
| 11 | Foreign currency | AASB 121; monetary items at closing rate |
| 12 | Government grants | AASB 120. Recognise a grant when there is reasonable assurance the entity will comply with its conditions and receive the grant. |

- **Reconcile and support each adjustment** — Reconcile the trial balance to ledgers and external evidence, and review revenue cut-off, inventories, receivables, leases, asset values, provisions, employee benefits, tax, related parties, subsequent events and going concern against the relevant standard rather than copying tax depreciation or deductibility into the accounts. For each adjustment retain the calculation, evidence, accounting conclusion and disclosure effect, and reconcile opening balances to the approved prior report and closing cash to the cash flow statement.

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
| 12 | Segment information | Required within AASB 8 scope, including publicly traded instruments and financial statements filed to issue instruments in a public market | Not required under AASB 1060 |

## Section 9 -- Filing (Lodgement) Requirements

**Filing (Lodgement) Requirements**  _(s.340)_

| Item | Detail |
| --- | --- |
| Filing authority | ASIC |
| Filing form | Form 388 (Copy of Financial Statements and Reports) |
| Lodgement method | Company officeholder, registered agent or auditor portal. Check market operator relief separately. |
| Deadline for disclosing entities, registered schemes, registrable superannuation entities and notified foreign passport funds | 3 months after financial year-end |
| Deadline for other entities required to lodge | 4 months after financial year-end |
| Documents lodged | Financial report + directors' report + auditor's report |
| Fee | No ordinary filing fee for a company lodging on time. Check the applicable form and fee schedule for other entity types. |
| Late lodgement | For lodgements from 1 July 2025 through 30 June 2026, the standard fee was AUD 98 up to 1 month late or AUD 411 beyond 1 month. Apply the schedule in force at lodgement. |
| Annual review fee | A separate fee. From 1 July 2025 through 30 June 2026 it was AUD 329 for a proprietary company other than a special purpose company. |
| Extension | Possible by application to ASIC under s.340 |

- **Half-year and sustainability reports** — Disclosing entities also lodge half-year reports, generally within 75 days of the half-year end. Screen separately for mandatory climate-related sustainability reporting under Chapter 2M, which commences in phases and is a separate statutory report.  _([ASIC, Users of financial reports](https://www.asic.gov.au/regulatory-resources/financial-reporting-and-audit/users-of-financial-reports); [ASIC Regulatory Guide 280](https://download.asic.gov.au/media/j4rhwyiz/rg280-published-31-march-2025.pdf))_

For a company's first financial year, apply the default 12 months from registration or the period set by directors up to 18 months. Later years ordinarily run for 12 months from the previous year-end. Section 323D provides exceptions for adjustments of up to 7 days, a qualifying shorter year and consolidation alignment. [Corporations Act section 323D](https://www.legislation.gov.au/C2004A00818/2025-02-21/2025-02-21/text/original/epub/OEBPS/document_2/document_2.html) · [Corporations (Fees) Regulations regulation 3](https://www.legislation.gov.au/F2001B00275/2025-01-01/2025-01-01/text/original/epub/OEBPS/document_1/document_1.html) · [ASIC Form 388 instructions](https://www.asic.gov.au/regulatory-resources/forms/forms-folder/388-copy-of-financial-statements-and-reports)

### Small proprietary companies with a reporting obligation

- **Foreign-controlled** — Section 292(2)(b) applies if the company was foreign-controlled for all or part of the year and was not included for that period in qualifying consolidated financial statements lodged with ASIC. Check instrument relief before concluding a report must be lodged.
- **ASIC direction** — ASIC direction (s.294)  _(s.294)_
- **Shareholder direction** — Shareholders with at least 5% of votes may give a signed direction within 12 months after year-end under section 293. Section 319(2) generally exempts reports prepared solely in response to that direction from ASIC lodgement.
- **CSF shareholders** — CSF shareholders (s.292(2)(c))  _(s.292(2)(c))_
- **CSF audit threshold** — A small proprietary company with a CSF shareholder at any time during the year prepares annual financial and directors' reports. The audit threshold is at least $3 million raised from all CSF offers by year-end. Check any separate ASIC or shareholder direction requiring audit.  _([ASIC, Crowd-sourced funding](https://www.asic.gov.au/crowd-sourced-funding))_
- **Companies limited by guarantee and charities** — Public companies limited by guarantee and ACNC-registered charities follow their own reporting rules, and foreign-controlled company relief has conditions and procedural requirements. Retain the legal basis and evidence for any exemption relied on.  _([ASIC, Company financial reports](https://www.asic.gov.au/for-business-and-companies/companies/company-financial-reports))_

## Section 10 -- Audit Requirements

**Audit Requirements**  _(s.301)_

| Category | Requirement |
| --- | --- |
| Large proprietary company | Audit required unless relief applies |
| Small proprietary (general) | Check any ASIC or shareholder direction and other reporting triggers |
| Small proprietary (foreign-controlled) | Audit required (unless ASIC relief) |
| Public company | Generally required. Check the company limited by guarantee and ACNC rules. |
| Disclosing entity | Mandatory audit |
| Registered scheme | Mandatory audit |
| Small proprietary (CSF shareholders) | Audit when the $3 million threshold or another audit requirement applies |

### ASIC relief instruments

- **Audit relief** — For the 2025 reporting year, Instrument 2016/784 applied to eligible large proprietary companies and small foreign-controlled proprietary companies. Conditions included unanimous resolutions of members and directors, timely lodgement of the company's reports and ASIC notices where required. For later reporting years check Instrument 2026/469, including its transition rules.  _([2016/784 sections 5–7](https://www.legislation.gov.au/F2016L01542/2021-10-29/2021-10-29/text/original/epub/OEBPS/document_1/document_1.html), [2026/469 sections 13–17](https://www.legislation.gov.au/F2026L01229/latest))_
- **Foreign-controlled company reporting relief** — For 2025, Instrument 2017/204 had conditions for eligible small foreign-controlled proprietary companies, including group size, director resolution and filing rules. For later reporting years check Instrument 2026/468, including its transition rules.  _([2017/204](https://www.legislation.gov.au/F2017L00307/asmade), [2026/468](https://www.legislation.gov.au/F2026L01228/latest))_

### Auditor qualification

- **Registered company auditor** — Registered company auditor under Part 9.2 of the Corporations Act (registered with ASIC). For audit of disclosing entities, the auditor must meet additional independence requirements under Part 2M.4 Division 3.  _(Part 9.2 Corporations Act; Part 2M.4 Division 3 Corporations Act)_
- **Appointment and sign-off sequence** — Confirm the auditor's appointment and engagement early, resolve audit adjustments before the directors approve the report, and retain the signed report, directors' approval, audit report, member delivery evidence and lodgement receipt. Do not describe an unaudited draft as audited, and confirm that the lodged document is the approved version.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

> Contributed by Ryan Duguid.
