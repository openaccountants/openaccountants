---
name: japan-bookkeeping
description: Use this skill whenever asked about Japanese bookkeeping for sole proprietors (個人事業主), small corporations (中小企業), or any entity using Japanese GAAP. Trigger on phrases like "勘定科目", "chart of accounts", "bookkeeping Japan", "損益計算書", "P&L", "貸借対照表", "balance sheet", "青色申告", "白色申告", "確定申告", "仕訳", "複式簿記", "消費税", "減価償却", "少額減価償却資産", "中小会計要領", "freee", "弥生", "bank reconciliation", "expense classification", "revenue recognition", or any question about day-to-day transaction recording, financial statement preparation, or account coding for a Japanese business.
version: 1.0
jurisdiction: JP
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - bookkeeping-workflow-base
category: bookkeeping
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Japan Bookkeeping

## Japan Bookkeeping Skill (日本の記帳スキル) v1.0

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Japan (日本) |
| Currency | JPY (¥) only |
| Financial year | Corporations: any period (typically April–March or January–December); Sole proprietors: calendar year (1 January – 31 December) |
| Accounting standards | Japanese GAAP (企業会計原則); 中小会計要領 (SME Basic Accounting Guidelines); 中小会計指針 (SME Accounting Guidance) |
| Governing body | Financial Services Agency (金融庁 / FSA); Accounting Standards Board of Japan (ASBJ / 企業会計基準委員会) |
| Tax authority | National Tax Agency (国税庁 / NTA) |
| Key legislation | Companies Act (会社法) Art.431–465; Financial Instruments and Exchange Act (金商法); Income Tax Act (所得税法); Corporation Tax Act (法人税法); Consumption Tax Act (消費税法) |
| Consumption tax threshold | Taxable sales > ¥10,000,000 in base period (基準期間) → mandatory registration; Invoice System (インボイス制度) from Oct 2023 |
| Record keeping | 7 years (blue return); 5 years (white return expenses/receipts) |
| Blue return (青色申告) benefit | ¥650,000 special deduction for sole proprietors using double-entry bookkeeping with e-filing |

## Section 2 -- Standard Chart of Accounts (勘定科目)

Japanese practice uses 3-digit codes. The structure below follows the common software convention (弥生会計, freee, PCA会計).

### Assets — 資産 (100–199)

**Assets — 資産 (100–199)**

| Code | 勘定科目 | English | Type |
| --- | --- | --- | --- |
| 111 | 現金 | Cash | Current asset |
| 112 | 小口現金 | Petty Cash | Current asset |
| 121 | 当座預金 | Checking Account | Current asset |
| 131 | 普通預金 | Ordinary Savings | Current asset |
| 132 | 定期預金 | Time Deposit | Current asset |
| 140 | 受取手形 | Notes Receivable | Current asset |
| 141 | 売掛金 | Accounts Receivable | Current asset |
| 142 | クレジット売掛金 | Credit Card Receivables | Current asset |
| 150 | 貸倒引当金 | Allowance for Doubtful Accounts | Contra asset |
| 161 | 有価証券 | Marketable Securities | Current asset |
| 171 | 商品 | Merchandise Inventory | Current asset |
| 172 | 製品 | Finished Goods | Current asset |
| 173 | 原材料 | Raw Materials | Current asset |
| 174 | 仕掛品 | Work in Progress | Current asset |
| 175 | 貯蔵品 | Supplies | Current asset |
| 180 | 前払費用 | Prepaid Expenses | Current asset |
| 181 | 未収入金 | Accrued Revenue | Current asset |
| 182 | 仮払金 | Suspense Payments | Current asset |
| 183 | 短期貸付金 | Short-Term Loans Receivable | Current asset |
| 184 | 仮払消費税 | Consumption Tax Paid (Input) | Current asset |
| 191 | 建物 | Buildings | Non-current asset |
| 192 | 建物付属設備 | Building Fixtures | Non-current asset |
| 193 | 構築物 | Structures | Non-current asset |
| 194 | 機械装置 | Machinery and Equipment | Non-current asset |
| 195 | 車両運搬具 | Vehicles | Non-current asset |
| 196 | 工具器具備品 | Tools, Furniture and Fixtures | Non-current asset |
| 197 | 土地 | Land | Non-current asset |
| 198 | 建設仮勘定 | Construction in Progress | Non-current asset |
| 199 | 減価償却累計額 | Accumulated Depreciation | Contra asset |
| 211 | ソフトウェア | Software | Intangible asset |
| 212 | のれん | Goodwill | Intangible asset |
| 241 | 投資有価証券 | Investment Securities | Investments |
| 242 | 出資金 | Equity Investments | Investments |
| 248 | 保険積立金 | Insurance Reserve Fund | Investments |
| 291 | 繰延資産 | Deferred Assets | Deferred asset |

### Liabilities — 負債 (300–399)

**Liabilities — 負債 (300–399)**

| Code | 勘定科目 | English | Type |
| --- | --- | --- | --- |
| 301 | 支払手形 | Notes Payable | Current liability |
| 306 | 買掛金 | Accounts Payable (Trade) | Current liability |
| 312 | 短期借入金 | Short-Term Borrowings | Current liability |
| 320 | 未払金 | Accounts Payable (Other) | Current liability |
| 321 | 未払費用 | Accrued Expenses | Current liability |
| 322 | 未払法人税等 | Income Tax Payable | Current liability |
| 323 | 未払消費税 | Consumption Tax Payable | Current liability |
| 324 | 預り金 | Withholdings Payable | Current liability |
| 325 | 前受金 | Advances Received | Current liability |
| 326 | 前受収益 | Unearned Revenue | Current liability |
| 329 | 仮受消費税 | Consumption Tax Received (Output) | Current liability |
| 330 | 賞与引当金 | Provision for Bonuses | Current liability |
| 340 | 長期借入金 | Long-Term Borrowings | Non-current liability |
| 342 | 社債 | Bonds Payable | Non-current liability |
| 351 | 退職給付引当金 | Retirement Benefit Liability | Non-current liability |

### Equity — 純資産 (400–499)

**Equity — 純資産 (400–499)**

| Code | 勘定科目 | English | Type |
| --- | --- | --- | --- |
| 411 | 資本金 | Share Capital | Equity |
| 421 | 資本剰余金 | Capital Surplus | Equity |
| 431 | 利益剰余金 | Retained Earnings | Equity |
| 441 | 元入金 | Owner's Capital (sole prop) | Equity |
| 451 | 事業主貸 | Owner's Drawings (sole prop) | Equity |
| 452 | 事業主借 | Owner's Contributions (sole prop) | Equity |

### Revenue — 収益 (500–599)

**Revenue — 収益 (500–599)**

| Code | 勘定科目 | English | Type |
| --- | --- | --- | --- |
| 511 | 売上高 | Sales Revenue | Revenue |
| 512 | 役務収益 | Service Revenue | Revenue |
| 521 | 受取利息 | Interest Income | Non-operating revenue |
| 522 | 受取配当金 | Dividend Income | Non-operating revenue |
| 523 | 有価証券売却益 | Gain on Sale of Securities | Non-operating revenue |
| 531 | 雑収入 | Miscellaneous Income | Non-operating revenue |
| 911 | 固定資産売却益 | Gain on Sale of Fixed Assets | Extraordinary income |

### Cost of Sales — 売上原価 (600–649)

**Cost of Sales — 売上原価 (600–649)**

| Code | 勘定科目 | English | Type |
| --- | --- | --- | --- |
| 601 | 期首商品棚卸高 | Opening Inventory | COGS |
| 611 | 仕入高 | Purchases | COGS |
| 621 | 仕入値引・返品 | Purchase Returns/Allowances | Contra COGS |
| 631 | 期末商品棚卸高 | Closing Inventory | Contra COGS |
| 641 | 外注費 | Outsourcing / Subcontractor Costs | COGS |

### Selling, General & Administrative — 販売費及び一般管理費 (700–799)

**Selling, General & Administrative — 販売費及び一般管理費 (700–799)**

| Code | 勘定科目 | English | Type |
| --- | --- | --- | --- |
| 711 | 役員報酬 | Director's Compensation | SGA Expense |
| 712 | 給料手当 | Salaries and Allowances | SGA Expense |
| 713 | 賞与 | Bonuses | SGA Expense |
| 714 | 法定福利費 | Statutory Benefits (social insurance) | SGA Expense |
| 715 | 福利厚生費 | Employee Welfare | SGA Expense |
| 721 | 地代家賃 | Rent and Lease | SGA Expense |
| 722 | 賃借料 | Equipment Rental | SGA Expense |
| 723 | 水道光熱費 | Utilities (Water, Gas, Electricity) | SGA Expense |
| 731 | 通信費 | Telephone and Internet | SGA Expense |
| 732 | 旅費交通費 | Travel and Transportation | SGA Expense |
| 733 | 消耗品費 | Consumables and Supplies | SGA Expense |
| 734 | 事務用品費 | Office Supplies | SGA Expense |
| 735 | 新聞図書費 | Books and Subscriptions | SGA Expense |
| 738 | 車両費 | Vehicle Expenses | SGA Expense |
| 741 | 広告宣伝費 | Advertising | SGA Expense |
| 745 | 接待交際費 | Entertainment Expenses | SGA Expense |
| 746 | 会議費 | Meeting Expenses (incl. light meals) | SGA Expense |
| 751 | 支払手数料 | Fees and Commissions | SGA Expense |
| 752 | 支払報酬 | Professional Fees Paid | SGA Expense |
| 754 | 荷造運賃 | Packing and Shipping | SGA Expense |
| 755 | 保険料 | Insurance Premiums | SGA Expense |
| 761 | 修繕費 | Repairs and Maintenance | SGA Expense |
| 763 | 租税公課 | Taxes and Public Charges | SGA Expense |
| 764 | 減価償却費 | Depreciation Expense | SGA Expense |
| 765 | 貸倒引当金繰入 | Bad Debt Provision | SGA Expense |
| 766 | 貸倒損失 | Bad Debt Losses | SGA Expense |
| 771 | 研究開発費 | R&D Expenses | SGA Expense |
| 781 | 雑費 | Miscellaneous Expenses | SGA Expense |

### Non-Operating Expenses — 営業外費用 (800–899)

**Non-Operating Expenses — 営業外費用 (800–899)**

| Code | 勘定科目 | English | Type |
| --- | --- | --- | --- |
| 811 | 支払利息 | Interest Expense | Non-operating expense |
| 812 | 有価証券売却損 | Loss on Sale of Securities | Non-operating expense |
| 813 | 為替差損 | Foreign Exchange Loss | Non-operating expense |
| 821 | 雑損失 | Miscellaneous Losses | Non-operating expense |

### Extraordinary Items — 特別損益 (900–999)

**Extraordinary Items — 特別損益 (900–999)**

| Code | 勘定科目 | English | Type |
| --- | --- | --- | --- |
| 911 | 固定資産売却益 | Gain on Sale of Fixed Assets | Extraordinary income |
| 915 | 固定資産売却損 | Loss on Sale of Fixed Assets | Extraordinary loss |
| 921 | 固定資産除却損 | Loss on Disposal of Fixed Assets | Extraordinary loss |
| 931 | 法人税等 | Corporate Income Tax | Tax expense |
| 932 | 法人税等調整額 | Deferred Tax Adjustment | Tax expense |

## Section 3 -- Revenue Recognition

### Recognition Standards

**Recognition Standards**  _(Under 企業会計原則 (Corporate Accounting Principles) and the Revenue Recognition Standard (ASBJ No.29 / 収益認識基準, effective from April 2021 for large companies))_

| Criterion | Rule |
| --- | --- |
| Sale of goods | When goods are delivered and control transfers (出荷基準 shipping point or 検収基準 acceptance basis) |
| Services | When performance obligation is satisfied (progress or completion) |
| Construction | Percentage of completion (工事進行基準) or completion method |
| Small entities (中小会計要領) | Permitted to use realization basis (実現主義) — when cash or receivable is established |

### Sole Proprietors — 青色申告 vs 白色申告

**Sole Proprietors — 青色申告 vs 白色申告**

| Method | 青色申告 (Blue Return) | 白色申告 (White Return) |
| --- | --- | --- |
| Bookkeeping | Double-entry (複式簿記) required for ¥650,000 deduction | Single-entry (簡易簿記) allowed |
| Special deduction | ¥650,000 (e-filing + double-entry) or ¥100,000 (simplified) | None |
| Accrual/Cash | Accrual basis standard; cash basis permitted for small businesses (現金主義 — taxable income < ¥3m and revenue < ¥3m prior 2 years) | Simplified recording |
| Loss carryforward | 3 years | Not available |
| Family employee salaries | Deductible (事前届出) | Limited (事業専従者控除: max ¥500,000/860,000) |

## Section 4 -- Expense Classification

### Key Categories for Tax Return

**Key Categories for Tax Return**

| Category (科目) | Tax Treatment | Notes |
| --- | --- | --- |
| 接待交際費 (Entertainment) | Corporations: ¥8m annual limit deductible (中小法人) or 50% of entertaining expenses, whichever is higher; sole proprietors: fully deductible if business-related | Must be clearly business purpose |
| 会議費 (Meetings) | Fully deductible | Per-person meal ≤ ¥10,000 (from 2024; was ¥5,000) classifies as 会議費 not 交際費 |
| 福利厚生費 (Welfare) | Fully deductible | Must be for all employees equally (not selective) |
| 減価償却費 (Depreciation) | Per statutory useful lives | Cannot exceed statutory limit for tax purposes |
| 租税公課 (Taxes/Duties) | Deductible: business tax, property tax, stamp duty, auto tax | NOT deductible: income tax, resident tax, penalties |
| 寄付金 (Donations) | Limited deductibility based on formula | Special treatment for government/designated donations |

### Non-Deductible Items (法人税法上の損金不算入)

- **Non-deductible items list** — 法人税・住民税 — Corporate/resident income tax; 延滞税・加算税 — Late payment penalties and surcharges; 役員賞与 (excessive) — Director bonuses exceeding pre-filed limits; 交際費 exceeding ¥8m limit (中小法人) — Entertainment over cap; 減価償却超過額 — Depreciation exceeding statutory rate; 引当金繰入超過額 — Provision amounts exceeding tax-law limits  _(法人税法上の損金不算入)_

## Section 5 -- Asset vs Expense Thresholds

### Depreciation Thresholds

**Depreciation Thresholds**

| Acquisition Cost | Treatment |
| --- | --- |
| < ¥100,000 | Immediate expense (消耗品費 or 雑費) — no capitalization required |
| ¥100,000 – ¥199,999 | Option: 3-year straight-line write-off (一括償却資産) regardless of useful life |
| ¥200,000 – ¥299,999 | Normal depreciation; OR use 少額減価償却資産特例 (see below) |
| ≥ ¥300,000 (¥400,000 from Apr 2026) | Must capitalize and depreciate over statutory useful life |

### 少額減価償却資産の特例 (SME Immediate Expensing)

**少額減価償却資産の特例 (SME Immediate Expensing)**

| Item | Current (to Mar 2026) | Revised (from Apr 2026) |
| --- | --- | --- |
| Threshold per asset | < ¥300,000 | < ¥400,000 |
| Annual cap | ¥3,000,000 total | ¥3,000,000 total |
| Eligible entities | Blue-return SMEs (資本金 ≤ ¥100m, employees ≤ 500) | Blue-return SMEs (employees ≤ 400) |

### Depreciation Methods

**Depreciation Methods**

| Method | Application |
| --- | --- |
| 定額法 (Straight-line) | Default for corporations (from 2012 acquisitions); always for buildings/structures/intangibles |
| 定率法 (Declining balance — 200% DB) | Optional for machinery, vehicles, furniture; default for sole proprietors pre-election |
| Statutory useful lives (耐用年数) | Set by MOF ordinance — must follow for tax depreciation |

### Common Statutory Useful Lives

**Common Statutory Useful Lives**

| Asset | Useful Life | SL Rate |
| --- | --- | --- |
| 鉄筋コンクリート建物 (RC building) — office | 50 years | 2.0% |
| 木造建物 (Wooden building) — office | 24 years | 4.2% |
| 建物付属設備 (Fixtures — electrical) | 15 years | 6.7% |
| 機械装置 (General machinery) | 7–12 years | Varies |
| 車両 (Motor vehicles) — standard car | 6 years | 16.7% (SL) / 33.3% (DB) |
| 工具器具備品 (Furniture/Equipment) | 5–15 years | Varies |
| パソコン (Computers — server) | 5 years | 20.0% |
| パソコン (Computers — other) | 4 years | 25.0% |
| ソフトウェア (Software — for own use) | 5 years | 20.0% |
| ソフトウェア (Software — for sale copies) | 3 years | 33.3% |

## Section 6 -- P&L Format (損益計算書)

### Standard Format (Japanese GAAP — Reporting Style)

```
損益計算書
自 20XX年4月1日 至 20XX年3月31日
                                        ¥           ¥
Ⅰ 売上高 (Sales)                                  xxx
Ⅱ 売上原価 (COGS)
    期首商品棚卸高                   xxx
    当期商品仕入高                   xxx
    合計                             xxx
    期末商品棚卸高                  (xxx)
                                                   (xxx)
                                                   ────
    売上総利益 (Gross Profit)                        xxx

Ⅲ 販売費及び一般管理費 (SGA)
    給料手当                         xxx
    法定福利費                       xxx
    地代家賃                         xxx
    減価償却費                       xxx
    その他                           xxx
                                                   (xxx)
                                                   ────
    営業利益 (Operating Income)                      xxx

Ⅳ 営業外収益 (Non-Operating Revenue)
    受取利息                         xxx
    雑収入                           xxx
                                                    xxx
Ⅴ 営業外費用 (Non-Operating Expenses)
    支払利息                         xxx
    雑損失                           xxx
                                                   (xxx)
                                                   ────
    経常利益 (Ordinary Income)                       xxx

Ⅵ 特別利益 (Extraordinary Gains)                    xxx
Ⅶ 特別損失 (Extraordinary Losses)                  (xxx)
                                                   ────
    税引前当期純利益 (Pre-Tax Income)                xxx
    法人税等 (Income Taxes)                         (xxx)
                                                   ────
    当期純利益 (Net Income)                          xxx
                                                   ════
```

### Key Feature — 経常利益 (Ordinary Income)

Japanese P&L uniquely separates operating from non-operating activities to derive 経常利益 before extraordinary items. This is the most-watched profitability metric for Japanese businesses.

## Section 7 -- Balance Sheet Format (貸借対照表)

### Standard Format (Account Form / 勘定式)

```
貸借対照表
20XX年3月31日現在

【資産の部】                              【負債の部】
Ⅰ 流動資産                               Ⅰ 流動負債
  現金及び預金        xxx                   支払手形          xxx
  受取手形            xxx                   買掛金            xxx
  売掛金              xxx                   短期借入金        xxx
  有価証券            xxx                   未払金            xxx
  商品                xxx                   未払法人税等      xxx
  前払費用            xxx                   未払消費税        xxx
  その他              xxx                   預り金            xxx
  貸倒引当金         (xxx)                  前受金            xxx
  ──────                                    賞与引当金        xxx
  流動資産合計        xxx                   ──────
                                            流動負債合計      xxx
Ⅱ 固定資産
 (1)有形固定資産                           Ⅱ 固定負債
  建物                xxx                   長期借入金        xxx
  機械装置            xxx                   退職給付引当金    xxx
  車両運搬具          xxx                   ──────
  工具器具備品        xxx                   固定負債合計      xxx
  土地                xxx                   ──────
  ──────                                    負債合計          xxx
  有形固定資産合計    xxx
                                           【純資産の部】
 (2)無形固定資産                           Ⅰ 株主資本
  ソフトウェア        xxx                   資本金            xxx
  のれん              xxx                   資本剰余金        xxx
  ──────                                    利益剰余金        xxx
  無形固定資産合計    xxx                   ──────
                                            株主資本合計      xxx
 (3)投資その他の資産
  投資有価証券        xxx                   ──────
  出資金              xxx                   純資産合計        xxx
  保険積立金          xxx
  ──────
  投資その他合計      xxx
  ──────
  固定資産合計        xxx

Ⅲ 繰延資産
  創立費              xxx
  ──────
  繰延資産合計        xxx
──────
資産合計              xxx                   負債純資産合計    xxx
════                                        ════
```

## Section 7 -- Balance Sheet Format (貸借対照表)

The Japanese balance sheet traditionally uses the horizontal (account) format (勘定式) with Assets on the left, Liabilities + Equity on the right. Report format (報告式, vertical) is also acceptable.

## Section 8 -- Bank Reconciliation Patterns

### Common Japanese Bank Formats

**Common Japanese Bank Formats**

| Bank | Export Format | Key Fields |
| --- | --- | --- |
| MUFG (三菱UFJ) | CSV, PDF | 取引日, 摘要, 支払金額, 預入金額, 残高 |
| SMBC (三井住友) | CSV, PDF | 日付, お取引内容, お引出し, お預入れ, 残高 |
| Mizuho (みずほ) | CSV, PDF | 取引日, 摘要, 出金額, 入金額, 残高 |
| Resona (りそな) | CSV, PDF | 日付, 摘要, 支払金額, 受入金額, 残高 |
| Japan Post Bank (ゆうちょ) | CSV | 日付, 取引内容, 出金, 入金, 残高 |
| Rakuten Bank (楽天) | CSV | 取引日, 入出金内容, 出金額, 入金額, 残高 |
| PayPay Bank | CSV | 日付, 内容, 出金, 入金, 残高 |

### Common Transaction Descriptions (摘要)

**Common Transaction Descriptions (摘要)**

| Pattern | Likely Classification |
| --- | --- |
| 振込 (furikomi) + company name | Income — customer payment (売掛金回収) |
| カード (card) + merchant | Expense — check merchant for category |
| 口座振替 (kōza furikae) | Direct debit — utility, insurance, tax |
| 給与振込 (kyūyo furikomi) | Payroll payment (給料手当) |
| 利息 (risoku) | Interest income (受取利息) or expense (支払利息) |
| 手数料 (tesūryō) | Bank fee (支払手数料) |
| 国税 / 消費税 / 法人税 | Tax payment — not deductible expense |
| 社会保険料 (shakai hoken ryō) | Social insurance — 法定福利費 |
| クレジットカード引落 | Credit card settlement — match to individual transactions |
| 自動送金 (jidō sōkin) | Standing transfer — check payee (rent, loan) |
| ATM引出し | Cash withdrawal — petty cash or owner drawings |
| 振替 between own accounts | Internal transfer — exclude |

## Section 9 -- Micro-Entity / Small Business Simplifications

### 中小会計要領 (SME Basic Accounting Guidelines)

**中小会計要領 (SME Basic Accounting Guidelines)**  _(Developed for small and medium enterprises not requiring audited financial statements)_

| Simplification | Detail |
| --- | --- |
| No tax-effect accounting | 税効果会計 not required |
| No consolidated statements | Individual entity statements only |
| Retirement benefits | Simplified calculation or tax-basis |
| Financial instruments | At cost (no fair value for unlisted) |
| Revenue recognition | Realization basis (実現主義) permitted |
| Inventory valuation | Last purchase price method accepted |
| Scope | All SMEs; encouraged by Japan Federation of CPAs and tax professionals |

### 青色申告 Sole Proprietor Simplifications

**青色申告 Sole Proprietor Simplifications**

| Feature | Simplified Bookkeeping (簡易簿記) | Full Double-Entry (複式簿記) |
| --- | --- | --- |
| Deduction | ¥100,000 | ¥650,000 (with e-filing via e-Tax/freee) |
| Books required | Cash book + fixed asset ledger + sales/purchases ledger | General journal + general ledger + all subsidiary ledgers |
| Statements | Income/expense statement (収支内訳書) | P&L (損益計算書) + Balance Sheet (貸借対照表) |

### Corporate Filing Simplifications

**Corporate Filing Simplifications**

| Entity Size | Requirements |
| --- | --- |
| 大会社 (Large company — capital ≥ ¥500m or liabilities ≥ ¥20b) | Full audit, consolidated, ASBJ standards |
| 中小会社 (SME — below thresholds) | 中小会計要領 or 中小会計指針, tax-basis accounting for many items, compilation by tax accountant (税理士) typical |
| 合同会社 (LLC — Gōdō Kaisha) | Same accounting rules as KK, but no share capital disclosure structure |

## Section 10 -- Interaction with Tax Skills

### Income Tax — Sole Proprietors (確定申告書B / 青色申告決算書)

- **Sole proprietor income tax filing process** — 決算書: P&L + Balance Sheet feed into 確定申告書; Key schedules: 減価償却費の計算 (depreciation schedule), 地代家賃の内訳 (rent details); Add back: excess depreciation, personal expenses, penalties; Deduct: 青色申告特別控除 ¥650,000 (if qualified); Filing deadline: March 15 of following year (振替納税 auto-debit = ~April 20)  _(確定申告書B / 青色申告決算書)_

### Corporate Tax (法人税確定申告)

- **Corporate tax filing process** — Start with accounting profit (当期純利益); 別表四: adjustments (加算: add back non-deductible items; 減算: deduct allowable items); 別表十六: depreciation schedule (compare book vs tax depreciation); 別表十五: 交際費 entertainment expense limit calculation; Effective combined tax rate (法人実効税率): ~33.6% for SMEs on income > ¥8m; ~23.2% for SMEs on first ¥8m  _(法人税確定申告)_

### Consumption Tax (消費税申告)

**Consumption Tax (消費税申告)**

| Item | Description | CoA Mapping |
| --- | --- | --- |
| 課税売上 | Taxable sales (10% standard / 8% reduced rate) | 511, 512 |
| 非課税売上 | Non-taxable sales (land, financial services, etc.) | 511 (flagged) |
| 輸出免税売上 | Export exempt sales (0%) | 511 (flagged) |
| 課税仕入 | Taxable purchases (input tax) | 184 (仮払消費税) |
| 控除対象外消費税 | Non-creditable input tax (proportional rule) | 763 (租税公課) |
| 仕入税額控除 | Input tax credit (仕入税額) | Net against 329 (仮受消費税) |

### Invoice System (インボイス制度 — from October 2023)

- **Invoice system rules** — Registered invoice issuers (適格請求書発行事業者) must issue qualified invoices with registration number; Buyers can only claim input tax credit with qualified invoices; Small business transitional measure (2割特例): eligible businesses can pay 20% of output tax as simplified calculation (through Sep 2026); 簡易課税 (Simplified tax calculation): if base-period sales ≤ ¥50m, use deemed purchase ratio by industry (50%–90%)  _(インボイス制度 — from October 2023)_

### Social Insurance and Payroll

**Social Insurance and Payroll**

| Item | Employer Burden | Nominal Code |
| --- | --- | --- |
| 健康保険 (Health Insurance) | ~5% of salary | 714 法定福利費 |
| 厚生年金 (Pension) | ~9.15% of salary | 714 |
| 雇用保険 (Employment Insurance) | 0.95% (general industry) | 714 |
| 労災保険 (Workers' Comp) | 0.25–8.8% (industry-specific) | 714 |
| 子ども・子育て拠出金 | 0.36% (employer only) | 714 |

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a 公認会計士, 税理士, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

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
