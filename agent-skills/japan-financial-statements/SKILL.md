---
name: japan-financial-statements
description: "Use this skill when preparing, reviewing, or advising on annual financial statements (計算書類 / 財務諸表) for a Japanese company. Trigger on phrases like \"計算書類\", \"財務諸表\", \"会社法\", \"金融商品取引法\", \"J-GAAP\", \"日本基準\", \"決算書\", \"貸借対照表\", \"損益計算書\", \"大会社\", \"会計監査人\", \"有価証券報告書\", or any question about preparing and filing statutory accounts under Japanese corporate law. Covers J-GAAP framework, company categories (大会社/中小), required statements, formats, notes, filing, and audit requirements."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/japan-financial-statements"
  jurisdiction: "JP"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Japan Financial Statements

> **General reference only.** This skill produces working papers for professional review. It has not been approved by an accountant for any particular person, entity, election or filing. Confirm the applicable facts and official forms before filing, paying or taking a position.

## Scope

2026 statutory-account preparation for Japanese KK and membership companies, distinguishing the Companies Act from FIEA securities reporting and tax attachments. Output a reconciled accounts pack, framework/obligation memo, approval/audit timetable and unresolved-items list. This is not a signed audit report. `japan-bookkeeping` handles ledger work; the corporate tax skill handles the tax return.

Quick reference: a KK is large if latest balance-sheet capital is at least JPY 500,000,000 or liabilities at least JPY 20,000,000,000. These are JPY 0.5 billion and JPY 20 billion, not JPY 5 billion/200 billion. Annual accounts are not generally filed at the corporate registry after the AGM. Companies Act arts.2(6),435-444 and 915, https://laws.e-gov.go.jp/law/417AC0000000086.

## Ask the client first

- KK/GK/other form, public/private share-transfer restrictions, articles, board/auditor structure and year-end.
- Latest balance sheet capital/liabilities, subsidiaries and securities-reporting status.
- J-GAAP/eligible designated IFRS/US GAAP/JMIS framework actually elected for each consolidated and separate set.
- Trial balance, opening comparatives, accounting policies, tax schedules and consolidation perimeter.
- Auditors, AGM plan, public-notice method, EDINET filings and tax-return extensions.
- Material estimates, related parties, going concern, subsequent events and changes in standards.

## The method, step by step

### Identify the statutory perimeter

| Threshold or obligation | Amount and full condition | Official source |
|---|---|---|
| Large KK capital | At least JPY 500,000,000 on latest statutory balance sheet; use formation balance sheet before first AGM | Companies Act art.2(6), https://laws.e-gov.go.jp/law/417AC0000000086 (in words on the page) |
| Large KK liabilities | At least JPY 20,000,000,000 total liabilities on that balance sheet; either test suffices | same, https://laws.e-gov.go.jp/law/417AC0000000086 (in words on the page) |
| Large KK external financial auditor | Mandatory, including private large KK; governance requirements differ for public/committee structures | Companies Act arts.327-328, https://laws.e-gov.go.jp/law/417AC0000000086 |
| KK accounting books and accounts | Retain books/important materials 10 years from closing and accounts/schedules 10 years from preparation | Companies Act arts.432,435, https://laws.e-gov.go.jp/law/417AC0000000086 (in words on the page) |
| Mandatory Companies Act consolidation | Large company at year-end AND FIEA art.24(1) annual-report filer; do not infer from size plus any subsidiary alone | Companies Act art.444(3), https://laws.e-gov.go.jp/law/417AC0000000086 |
| Domestic FIEA annual securities report | Normally within 3 months after year-end; prior approved extension available for unavoidable reason | FIEA art.24(1), https://laws.e-gov.go.jp/law/323AC0000000025 (in words on the page) |
| Ordinary listed semiannual report | Period prescribed within 45 days after first 6 months; special listed financial businesses have a 60-day category, non-listed reporters generally 3 months | FIEA art.24-5(1), https://laws.e-gov.go.jp/law/323AC0000000025 (in words on the page); confirm category/order |
| Corporate income-tax return | Normally within 2 months after year-end; approved extension considered separately | Corporate Tax Act art.74, https://laws.e-gov.go.jp/law/340AC0000000034 (in words on the page) |

The Companies Act calls for generally accepted Japanese accounting practice, not an instruction to impose every listed-company ASBJ standard on every small private company. Assess 中小会計要領 or 中小会計指針 eligibility and the entity's existing framework. The basic guidelines target companies outside FIEA reporting and outside Companies Act financial-auditor companies; they also contemplate special limited and membership companies. FIEA reporting, including eligible designated IFRS, US GAAP or JMIS consolidated accounts, needs the applicable regulatory eligibility and actual election; a listed company cannot casually relabel separate statutory accounts as IFRS. Companies Act art.431, https://laws.e-gov.go.jp/law/417AC0000000086; SME guidelines, https://www.nichizeiren.or.jp/wp-content/uploads/doc/cpta/business/tyushoushien/indicator/chusyokaikeiyouryou120201.pdf. The detailed alternate-framework eligibility is a referral boundary below.

### Assemble and reconcile the statements

For KK, prepare balance sheet (貸借対照表), P&L (損益計算書), statement of changes in shareholders' equity (株主資本等変動計算書), notes (個別注記表), business report (事業報告) and required supplementary schedules (附属明細書). The business report is a related statutory document, not a substitute financial statement. For membership companies, use the relevant Companies Act/Accounting Regulations provisions, not the KK shareholder/board process. Sources: Companies Act arts.435,617-618, https://laws.e-gov.go.jp/law/417AC0000000086; Companies Accounting Regulations arts.59,61, https://laws.e-gov.go.jp/law/418M60000010013.

Build the balance sheet from current assets, fixed tangible/intangible/investment assets and deferred charges where permitted; liabilities from current and long-term obligations; equity from capital, capital/retained surplus, treasury shares and other required valuation/translation components. Show receivable and related allowance together with traceable gross/allowance support. P&L flow is sales less cost of sales, gross profit less SG&A, operating profit plus/minus non-operating results, ordinary profit plus/minus extraordinary results, pre-tax profit less current/deferred taxes, net profit. These are presentation working papers; determine recognition and the permitted classifications from the applicable framework. Sources: Companies Accounting Regulations arts.73-97, https://laws.e-gov.go.jp/law/418M60000010013; SME guidelines financial-statement formats, https://www.nichizeiren.or.jp/wp-content/uploads/doc/cpta/business/tyushoushien/indicator/chusyokaikeiyouryou120201.pdf.

Reconcile each balance to the trial balance and prior closing accounts. Prepare adjustment schedules for depreciation and tax useful lives, bonus/retirement/bad-debt provisions, inventory cost/NRV, temporary differences and deferred tax, FX monetary/non-monetary balances, leases, impairment, deferred costs, trading/other securities and consumption tax. A tax deduction ceiling is not an accounting valuation rule. Use the actual enacted combined tax rate in a deferred-tax calculation rather than a generic percentage.

Check the standard version before signing off lease treatment. ASBJ Statement 34 was issued for the new lease model; paragraph 58 provides mandatory application for years beginning on/after 1 April 2027 with early application for years beginning on/after 1 April 2025. A 2026 entity may therefore have early adopted; do not state categorically that J-GAAP has no new lease model. Source: ASBJ Statement 34, para.58, https://www.asb-j.jp/jp/wp-content/uploads/sites/4/lease_20240913_02.pdf.

### Notes, audit and approval

Determine disclosures from entity category and applicable regulations. The checklist includes significant policies, estimates, balance-sheet and P&L detail, contingent liabilities, related parties, equity/per-share matters, subsequent events, segments, tax effects, financial instruments, retirement benefits, asset retirement and revenue recognition. Do not use a blanket SME-versus-large yes/no matrix without checking which notes the actual entity can omit. Companies Accounting Regulations arts.98 onward, https://laws.e-gov.go.jp/law/418M60000010013; SME guidelines, https://www.nichizeiren.or.jp/wp-content/uploads/doc/cpta/business/tyushoushien/indicator/chusyokaikeiyouryou120201.pdf.

Obtain the statutory auditors' and financial auditor's work where required. A non-large KK can still require a financial auditor because of its committee structure or articles; do not infer exemption from size alone. A financial auditor is a qualified CPA or audit corporation under Companies Act art.337. FIEA art.193-2 requires the applicable CPA/audit-corporation certification for securities reporting, with its statutory exceptions. Companies Act arts.327-328,337,436, https://laws.e-gov.go.jp/law/417AC0000000086; FIEA art.193-2, https://laws.e-gov.go.jp/law/323AC0000000025.

Board companies approve the required accounts and report at board level following the applicable audits. Submit/provide the financial statements to the annual shareholder meeting for approval; the art.439 audited-company exception permits reporting instead when its regulatory conditions are met. Report the business report to shareholders. The Companies Act calls for an AGM at a certain time after each year-end; it does not universally impose an AGM within 3 months. Articles, record date, tax deadline and listed-company obligations must be reconciled. Companies Act arts.296,436,438-439, https://laws.e-gov.go.jp/law/417AC0000000086.

## Boundary and exception table

| Case | Action |
|---|---|
| KK public notice | After AGM without delay, publish balance sheet; large KK also P&L. Gazette/newspaper summary and prescribed electronic alternatives differ; FIEA art.24(1) filers are exempt under art.440(4). Companies Act art.440, https://laws.e-gov.go.jp/law/417AC0000000086 |
| Electronic balance-sheet alternative | Maintain prescribed public access for 5 years after AGM; assess registration and technical requirements. Companies Act art.440(3), https://laws.e-gov.go.jp/law/417AC0000000086 (in words on the page) |
| Registry change | A change to directors/address/capital or other registered matter can trigger 2-week registration; no general accounts-deposit deadline at the registry. Companies Act art.915, https://laws.e-gov.go.jp/law/417AC0000000086 (in words on the page) |
| GK/other membership company | Prepare and preserve required accounts; do not impose KK annual financial public notice or KK financial-auditor mandate automatically. Companies Act arts.617-618, https://laws.e-gov.go.jp/law/417AC0000000086 |
| Legacy special limited company (有限会社) | Verify its transitional status and applicable statutory exception; do not assume all KK reporting/audit rules transfer unchanged |
| Securities reporter | Use the current EDINET form/taxonomy and applicable annual/semiannual audit or review; do not file obsolete quarterly statutory reports as though replacement starts only in 2025 |

## Worked cases

A hypothetical KK has capital JPY 499,999,999 and liabilities JPY 19,999,999,999. Both tests are below threshold by JPY 1, so size alone does not make it large. Increasing capital by JPY 1 reaches the capital threshold even if liabilities remain unchanged. Another KK with capital JPY 100,000,000 and liabilities JPY 20,000,000,000 is large solely from liabilities. The decision is disjunctive, not the sum of capital and liabilities.

```oa-check
name: Exact large-company capital and liability boundaries
inputs:
  capital: 499999999
  liabilities: 19999999999
steps:
  - capital_gap: 500000000 - capital
  - liabilities_gap: 20000000000 - liabilities
  - capital_after: capital + 1
expected:
  capital_gap: 1
  liabilities_gap: 1
  capital_after: 500000000
```

Hypothetical closing assets are JPY 85,000,000, liabilities JPY 35,000,000, opening equity JPY 42,000,000 and distributions JPY 2,000,000. Required closing equity is JPY 50,000,000 and current-year profit must be JPY 10,000,000 if no other equity movements exist. If P&L profit is only JPY 9,000,000, JPY 1,000,000 remains unexplained; do not plug it into retained earnings.

```oa-check
name: Accounts reconciliation detects an unexplained equity movement
inputs:
  assets: 85000000
  liabilities: 35000000
  opening_equity: 42000000
  distributions: 2000000
  reported_profit: 9000000
steps:
  - closing_equity: assets - liabilities
  - required_profit: closing_equity - opening_equity + distributions
  - unexplained: required_profit - reported_profit
expected:
  closing_equity: 50000000
  required_profit: 10000000
  unexplained: 1000000
```

## When to refuse or refer

Do not issue a signed auditor opinion, invent disclosure exemptions or approve an unbalanced statement. Refer alternate-framework eligibility, consolidation exemptions, regulated issuers, special limited companies and complex valuations. Missing current standard text means the affected accounting policy stays unresolved, not presumed tax-basis treatment.

## Filing and payment

Produce final financial statements and approval/audit record. Complete required public notice or documented exemption. Keep accounts available at the head office and branches as prescribed by Companies Act art.442, https://laws.e-gov.go.jp/law/417AC0000000086. File applicable securities reports through EDINET and attach statements/schedules to the actual e-Tax/local tax returns. Record accepted submissions and payment separately; AGM approval does not establish tax payment. Up to JPY 1,000,000 administrative fine can apply for failure to register, notify or disclose under Companies Act art.976, https://laws.e-gov.go.jp/law/417AC0000000086 (in words on the page); no generic FIEA late-filing criminal figure is supplied here.

## Completion checklist

Document entity/large-company/reporting perimeter, applicable framework and lease election; tie balances and consolidation; clear estimates/disclosure exceptions; obtain audits and approvals; complete notice/EDINET/tax handoffs; preserve signed versions, receipts and retention dates.

## Sources

| Source | URL | Read on |
|---|---|---|
| Companies Act; Read for arts.2(6),296,327-328,337,431-444,617-618,915,976 and neighboring exceptions | https://laws.e-gov.go.jp/law/417AC0000000086 | 2026-11-14 |
| Companies Accounting Regulations; Read for arts.59,61,73-98 statutory statements, classification and notes framework | https://laws.e-gov.go.jp/law/418M60000010013 | 2026-11-14 |
| Financial Instruments and Exchange Act; Read for arts.24,24-5,193-2 annual/half-year reporting, scope, exceptions and auditor certification | https://laws.e-gov.go.jp/law/323AC0000000025 | 2026-11-14 |
| Corporate Tax Act; Read for art.74 ordinary return timing | https://laws.e-gov.go.jp/law/340AC0000000034 | 2026-11-14 |
| SME Basic Accounting Guidelines; Read for scope, accounting and statement forms | https://www.nichizeiren.or.jp/wp-content/uploads/doc/cpta/business/tyushoushien/indicator/chusyokaikeiyouryou120201.pdf | 2026-11-14 |
| ASBJ Statement 34; Read for para.58 effective date/early adoption and surrounding provisions | https://www.asb-j.jp/jp/wp-content/uploads/sites/4/lease_20240913_02.pdf | 2026-11-14 |

Not yet confirmed: Detailed FIEA eligibility for IFRS, US GAAP and JMIS; FIEA cash-flow/consolidated statement presentation requirements and current EDINET taxonomy; each entity-specific note omission; full measurement rules under ASBJ Statements 6,9,13,26,27,29; generic deferred-tax rate near 30%; universal consolidation for every large company with subsidiaries; special limited-company transitional exemptions; unsupported March-year-end prevalence near 70%; generic JPY 5,000,000 criminal late-filing penalty. These old topics are excluded from usable guidance pending their specific official text. The former universal AGM-within-3-months and accounts-registry-within-2-weeks claims are rejected, not postponed.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `japan-financial-statements` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/japan-financial-statements. If neither is available, confirm every figure against the official source pages cited above before relying on it.
