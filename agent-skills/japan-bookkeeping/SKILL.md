---
name: japan-bookkeeping
description: "Use this skill whenever asked about Japanese bookkeeping for sole proprietors (個人事業主), small corporations (中小企業), or any entity using Japanese GAAP. Trigger on phrases like \"勘定科目\", \"chart of accounts\", \"bookkeeping Japan\", \"損益計算書\", \"P&L\", \"貸借対照表\", \"balance sheet\", \"青色申告\", \"白色申告\", \"確定申告\", \"仕訳\", \"複式簿記\", \"消費税\", \"減価償却\", \"少額減価償却資産\", \"中小会計要領\", \"freee\", \"弥生\", \"bank reconciliation\", \"expense classification\", \"revenue recognition\", or any question about day-to-day transaction recording, financial statement preparation, or account coding for a Japanese business."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/japan-bookkeeping"
  jurisdiction: "JP"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Japan Bookkeeping

> **General reference only.** This skill produces working papers for professional review. It has not been approved by an accountant for any particular person, entity, election or filing. Confirm the applicable facts and official forms before filing, paying or taking a position.

## Scope

2026 bookkeeping for Japanese sole proprietors and companies. Prepare reconciled journals, ledgers, trial balance, closing schedules and a book-to-tax reconciliation. `japan-financial-statements` handles statutory presentation/audit and `jp-income-tax` or `japan-consumption-tax` handles tax computation. Japanese labels and JPY reporting below are a working-paper convention; retain original-currency amounts and FX evidence for foreign transactions.

Quick reference: preserve source documents, distinguish a tax deduction from an accounting expense, and do not confuse white-return simplified recording with an exemption from books. Sources: Companies Act arts.431-435, https://laws.e-gov.go.jp/law/417AC0000000086; NTA Nos.2072,2080,5930.

## Ask the client first

- Individual, KK, GK or other entity, reporting year, accounting framework and existing chart of accounts.
- Blue/white return approval, cash-basis election, e-Tax use and electronic-record preservation method.
- All banks, cards, cash, payment platforms, foreign currencies and opening balances.
- Consumption-tax exemption/elections, invoice registration, taxable/exempt/export activity and invoice evidence.
- Asset acquisition/use dates, costs, employee count, ownership group and available expensing cap.
- Payroll, family/related-party payments, private use and unusual year-end transactions.

## The method, step by step

### Capture, code and reconcile

Create chronological entries with transaction date, counterparty, nature, gross/net amount, currency, tax classification and document reference. Reconcile each bank opening balance plus deposits less payments to closing balance. Reconcile cards to transaction detail before matching the bank settlement; do not expense both. Match customer receipts to receivables, supplier settlements to payables, and transfers to the other owned account. Unexplained ATM withdrawals are not automatically deductible expenses. Review payroll, withholding, insurance and tax-control accounts separately. Companies Act art.432, https://laws.e-gov.go.jp/law/417AC0000000086; Corporate Tax Act arts.126,150-2 through NTA No.5930, https://www.nta.go.jp/taxes/shiraberu/taxanswer/hojin/5930.htm.

The following are descriptive account families, not legally mandated numeric codes: 現金/小口現金 (cash/petty cash), 当座預金/普通預金/定期預金 (bank), 受取手形/売掛金 (receivables), 商品/製品/原材料 (inventory), 建物/機械装置/車両/工具器具備品/土地/ソフトウェア (fixed assets), 仮払消費税 (input-tax control); 支払手形/買掛金/借入金/未払金/預り金/前受金/仮受消費税 (liabilities); 資本金/資本剰余金/利益剰余金/事業主借/事業主貸 (equity or proprietor accounts); 売上高/受取利息/受取配当金/雑収入 (income); 仕入高/外注費/給料手当/法定福利費/地代家賃/通信費/水道光熱費/旅費交通費/広告宣伝費/交際費/会議費/支払手数料/支払報酬/荷造運賃/保険料/修繕費/租税公課/減価償却費/貸倒損失/研究開発費/雑費 (costs); 支払利息/為替差損益/固定資産売却損益/法人税等 (other results). Retain the entity's freee, 弥生会計, PCA会計 or other existing coding. Do not assume the old 3-digit code list is an official national chart.

Interpret bank 摘要 as a lead, not proof: 振込 may settle a debtor; カード identifies a merchant; 口座振替 may be utility, insurance or tax; 給与振込 points to payroll; 利息 to interest; 手数料 to fees; 国税/消費税/法人税 to tax-control reconciliation; 社会保険料 to insurance payable; 自動送金 to a standing payment; クレジットカード引落 to card settlement; ATM引出し to cash/private-use investigation; 振替 to own-account matching. Bank CSV/PDF field names must be checked on the actual MUFG, SMBC, Mizuho, Resona, Japan Post Bank, Rakuten Bank or PayPay Bank export. These are workflow labels, not tax conclusions.

### Close the ledgers and map to statements

Reconcile opening equity, sales cut-off, receivables, payables, cash, inventory and assets; accrue unpaid business expenses and reverse prepaid/future-period amounts. Prepare sales less cost of sales equals gross profit; deduct selling/general/administrative costs for operating profit; add non-operating income and deduct non-operating costs for ordinary profit (経常利益); include extraordinary gains/losses and tax for net profit. Reconcile assets to liabilities plus equity, including opening equity, contributions, distributions and profit. These are working-paper identities, not a replacement for framework recognition rules.

Carry a separate schedule for depreciation, bad debts/provisions, retirement benefits, inventory valuation, FX, leases, impairment, deferred charges, securities, consumption tax and deferred tax. Determine eligibility for SME basic accounting (中小会計要領) rather than applying listed-company standards automatically. The guidelines target companies outside FIEA reporting and outside Companies Act financial-auditor companies, and can also be used by special limited and membership companies. Its official provisions govern revenue realisation, inventory, fixed assets, provisions, foreign currency and financial-statement forms. Never make cash receipt the universal recognition trigger or equate book depreciation to deductible tax depreciation. SME Basic Accounting Guidelines, https://www.nichizeiren.or.jp/wp-content/uploads/doc/cpta/business/tyushoushien/indicator/chusyokaikeiyouryou120201.pdf.

Book business taxes, income taxes, penalties, donations, entertainment, officer compensation, repairs/capital improvements and mixed private use in the right accounts, then test tax deductibility separately. A bank description saying tax paid does not establish that the tax is deductible. Prepare 別表四 book-to-tax adjustments, depreciation and entertainment schedules, and the sole-proprietor 青色申告決算書/appropriate income statement from reconciled books; do not use an obsolete form-B label as the filing instruction.

### Bookkeeping-linked tax boundaries

| Item | Conditions and amount | Official source |
|---|---|---|
| Blue deduction JPY 550,000 | Qualifying business/business-scale rental income; regular double-entry, balance sheet/P&L and timely return; limited to positive eligible income; cash-basis special election excluded ; monetary amounts derived from Japanese 万/億 units | Special Measures Act art.25-2; NTA No.2072, https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/2072.htm |
| Blue deduction JPY 650,000 | All JPY 550,000 conditions plus timely e-Tax transmission of return/statements, or qualifying excellent electronic journals/ledger and required notice; software use alone is insufficient ; monetary amounts derived from Japanese 万/億 units | same, https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/2072.htm |
| Other blue deduction JPY 100,000 | Eligible blue filers not meeting higher-deduction requirements; positive income limit and allocation order apply ; monetary amounts derived from Japanese 万/億 units | same, https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/2072.htm |
| Cash-basis special election | Prior-prior-year business plus real-estate income no more than JPY 3,000,000, with notice; not a gross-revenue test; higher blue deduction unavailable ; monetary amounts derived from Japanese 万/億 units | NTA No.2072, https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/2072.htm |
| Corporate low-value expense | Cost below JPY 100,000, or ordinary useful period below 1 year; unit-of-transaction test, business use and same-year expense entry; non-main-business rental exception ; monetary amounts derived from Japanese 万/億 units | Corporation Tax Order art.133; NTA No.5403, https://www.nta.go.jp/taxes/shiraberu/taxanswer/hojin/5403.htm |
| Corporate pooled write-off | Cost below JPY 200,000, optional 3-year pool; rental exception applies ; monetary amounts derived from Japanese 万/億 units | Corporation Tax Order art.133-2; NTA No.5403, https://www.nta.go.jp/taxes/shiraberu/taxanswer/hojin/5403.htm |
| SME corporate expensing through 31 March 2026 | Cost below JPY 300,000; blue-return qualifying SME/group restrictions and old employee test, annual cap JPY 3,000,000 ; monetary amounts derived from Japanese 万/億 units | Special Measures Act art.67-5; NTA No.5408 revision notes, https://www.nta.go.jp/taxes/shiraberu/taxanswer/hojin/5408.htm |
| SME corporate expensing from 1 April 2026 | Cost below JPY 400,000 for assets acquired/used under the amended regime; blue-return qualifying SME, generally no more than 400 employees (specified corporations 300), group/exclusion tests, annual cap JPY 3,000,000 pro-rated for short years ; monetary amounts derived from Japanese 万/億 units | same, https://www.nta.go.jp/taxes/shiraberu/taxanswer/hojin/5408.htm |

For the SME corporate special deduction, ordinarily capital no more than JPY 100,000,000 is only the starting point: test controlling ownership, excluded businesses, group taxation and the other statutory restrictions. Exclude non-main-business rental assets; expense the elected amount when placed in use and attach 別表16(7). Do not combine the same asset's special expensing with the alternative special depreciation/credit or pooled deduction. This corporate rule is not automatically the sole-proprietor rule. NTA No.5408, https://www.nta.go.jp/taxes/shiraberu/taxanswer/hojin/5408.htm.

## Boundary and exception table

| Boundary | Action |
|---|---|
| Blue versus white individual | Both keep records. For white returns, statutory income/expense book 7 years; voluntary books and supporting documents generally 5 years. Income Tax Act arts.120, 148, 232; https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/2080.htm |
| Corporate retention | Generally 7 years from the day after final-return due date; qualifying loss years 10 years, with historical 9-year exception. Keep longer where company law requires it. NTA No.5930, https://www.nta.go.jp/taxes/shiraberu/taxanswer/hojin/5930.htm |
| KK company-law retention | Accounting books/important materials 10 years from closure; financial statements/schedules 10 years from creation. Companies Act arts.432,435, https://laws.e-gov.go.jp/law/417AC0000000086 (in words on the page) |
| Related-party support in years beginning from 1 April 2026 | If existing transaction records lack detail needed to compute consideration, create/obtain the missing specified-detail documents by the return deadline and retain as required; NTA No.5930, https://www.nta.go.jp/taxes/shiraberu/taxanswer/hojin/5930.htm |
| Consumption tax | Tag standard/reduced, non-taxable and export-exempt supplies separately; reconcile input/output control accounts and qualified invoices. Do not infer complete credit entitlement from a bank payment or ignore transitional exceptions |
| Payroll and social insurance | Reconcile expense, employer share, employee deductions and remittances; load the actual year/locality payroll rates rather than a fixed national approximation |

## Worked cases

Hypothetical bank reconciliation: opening JPY 500,000 plus receipts JPY 1,200,000 less payments JPY 900,000 gives JPY 800,000. JPY 100,000 is an own-account transfer, so business expense represented by the other payments is JPY 800,000, subject to document and tax classification. Record the transfer in both cash accounts.

```oa-check
name: Bank reconciliation separates an internal transfer
inputs:
  opening: 500000
  receipts: 1200000
  payments: 900000
  own_transfer: 100000
steps:
  - closing: opening + receipts - payments
  - other_payments: payments - own_transfer
expected:
  closing: 800000
  other_payments: 800000
```

Hypothetical eligible blue-return company acquires and uses a JPY 350,000 asset in April 2026. It has already elected JPY 2,800,000 of special-expensing assets in a full year. Only JPY 200,000 of annual cap remains; the entire JPY 350,000 asset cannot fit. It must select assets within the cap, rather than splitting this indivisible transaction to claim JPY 200,000 under the special rule. Compare normal depreciation; the asset is too expensive for the below-JPY 200,000 pool.

```oa-check
name: Eligible asset does not fit the annual special-expensing cap
inputs:
  annual_cap: 3000000
  prior_elections: 2800000
  asset: 350000
steps:
  - remaining_cap: annual_cap - prior_elections
  - excess_if_selected: prior_elections + asset - annual_cap
expected:
  remaining_cap: 200000
  excess_if_selected: 150000
```

## When to refuse or refer

Do not fabricate missing transactions, apply a national software code as law, deduct personal expenditure or treat e-filing alone as blue-return approval. Do not apply an SME asset concession without ownership, employee, period and election evidence. Refer unidentified opening balances, unsupported assets, mixed private/business use and unusual related-party dealings. Return an exceptions list with quantified unreconciled balances.

## Filing and payment

Produce reconciled trial balance and schedules for professional review; map them to the actual current e-Tax return and statements, and retain submission receipt and payment confirmation. Corporate return timing follows Corporate Tax Act art.74, normally 2 months after year-end before any approved extension, https://laws.e-gov.go.jp/law/340AC0000000034 (in words on the page). Individual blue-deduction timing follows the statutory return deadline and the NTA requirements above. Do not use an approximate April bank-debit date as a payment instruction.

## Completion checklist

All cash/card accounts reconciled; debtors/creditors/inventory/assets tied; payroll/tax controls matched; private-use and non-deductible items scheduled; accounting policy consistent; blue and SME conditions documented; source records preserved; financial statements tie to the trial balance; exact filing/payment dates and receipts recorded.

## Sources

| Source | URL | Read on |
|---|---|---|
| Companies Act; Read for arts.431-435 recording, accounting convention and retention | https://laws.e-gov.go.jp/law/417AC0000000086 | 2026-11-14 |
| NTA No.5930; Read for ordinary/loss retention and new related-party detail requirement | https://www.nta.go.jp/taxes/shiraberu/taxanswer/hojin/5930.htm | 2026-11-14 |
| NTA No.2080; Read for white-return statutory/voluntary books and documents | https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/2080.htm | 2026-11-14 |
| NTA No.2072; Read for all deduction requirements, cash-basis exclusion, income ceiling and electronic alternative | https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/2072.htm | 2026-11-14 |
| NTA No.5403; Read for unit threshold, rental exclusion, expense entry and optional pool | https://www.nta.go.jp/taxes/shiraberu/taxanswer/hojin/5403.htm | 2026-11-14 |
| NTA No.5408; Read for 2026 threshold/employee changes, exclusions, cap, short-year rule and filing | https://www.nta.go.jp/taxes/shiraberu/taxanswer/hojin/5408.htm | 2026-11-14 |
| SME Basic Accounting Guidelines; Read for scope and recognition/measurement/statement provisions | https://www.nichizeiren.or.jp/wp-content/uploads/doc/cpta/business/tyushoushien/indicator/chusyokaikeiyouryou120201.pdf | 2026-11-14 |
| Corporate Tax Act; Read for art.74 filing period | https://laws.e-gov.go.jp/law/340AC0000000034 | 2026-11-14 |

Not yet confirmed: Legacy software-specific 3-digit account numbers and export-field promises; listed-company revenue/construction recognition details; family-worker deduction amounts/loss relief; entertainment JPY 8,000,000/50% choice and meal JPY 10,000 conditions; useful-life/rate list for buildings, cars, equipment, servers and software; blanket depreciation-method defaults; tax-effect/consolidation/retirement and inventory simplifications beyond the SME source; standalone individual asset concessions; effective corporate-tax approximations; consumption-tax rates, simplified-method deemed purchase ratios, invoice transitional percentages/endpoints and credit exceptions; payroll/insurance percentages. These topics require their specific official rule before computation and are excluded from usable numerical guidance here.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `japan-bookkeeping` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/japan-bookkeeping. If neither is available, confirm every figure against the official source pages cited above before relying on it.
