---
name: jp-income-tax
description: >
  Use this skill whenever asked about Japanese income tax for self-employed individuals filing a final tax return (確定申告 Kakutei Shinkoku). Trigger on phrases like "how much tax do I pay in Japan", "kakutei shinkoku", "確定申告", "blue return", "青色申告", "white return", "白色申告", "business income Japan", "事業所得", "necessary expenses", "必要経費", "basic deduction", "基礎控除", "reconstruction tax", "resident tax", "住民税", "self-employed tax Japan", "e-Tax", "Rakuten Bank", "Japan Post Bank", "freee Japan", "Misoca", or any question about filing or computing income tax for a self-employed individual in Japan. This skill covers progressive brackets (5%-45%), blue vs white return, special deductions, reconstruction surtax, resident tax, necessary expenses, social insurance, and filing deadlines. ALWAYS read this skill before touching any Japan income tax work.
version: 2.0
jurisdiction: JP
tax_year: 2025
category: international
depends_on:
  - income-tax-workflow-base
---

# Japan Income Tax (確定申告) -- Self-Employed Skill v2.0

---

## Section 1 -- Quick Reference

| Field | Value |
|---|---|
| Country | Japan (日本) |
| Tax | Shotokuzei (所得税) + Fukko Tokubetsu Shotokuzei (復興特別所得税 2.1%) + Juminzei (住民税 10%) |
| Currency | JPY only |
| Tax year | Calendar year (1 January -- 31 December) |
| Primary legislation | Shotokuzeiho (所得税法 Income Tax Act) |
| Tax authority | National Tax Agency (国税庁 NTA) |
| Filing portal | e-Tax (国税電子申告・納税システム) |
| Filing deadline | 15 March of the following year |
| Contributor | Open Accountants Community |
| Validated by | Pending -- requires sign-off by a Japanese 税理士 (Zeirishi) |
| Skill version | 2.0 |

### National Income Tax Rate Table (2025) [T1]

| Taxable Income (JPY) | Rate | Deduction Amount (控除額) |
|---|---|---|
| 0 -- 1,950,000 | 5% | 0 |
| 1,950,001 -- 3,300,000 | 10% | 97,500 |
| 3,300,001 -- 6,950,000 | 20% | 427,500 |
| 6,950,001 -- 9,000,000 | 23% | 636,000 |
| 9,000,001 -- 18,000,000 | 33% | 1,536,000 |
| 18,000,001 -- 40,000,000 | 40% | 2,796,000 |
| 40,000,001+ | 45% | 4,796,000 |

**Shortcut formula:** Tax = (Taxable Income x Rate) - Deduction Amount.

**Reconstruction Surtax:** All national income tax x 2.1% (2013--2037). Total national tax = income tax x 102.1%.

**Resident Tax:** Flat 10% of taxable income (4% prefectural + 6% municipal) + per-capita levy ~5,000/year + forest environment tax 1,000 (from 2024). Assessed by municipality from the final return data.

### Blue Return Special Deduction (2025) [T1]

| Condition | Deduction (JPY) |
|---|---|
| Double-entry (複式簿記) + e-Tax filing | 650,000 |
| Double-entry + paper filing | 550,000 |
| Simplified bookkeeping (簡易簿記) | 100,000 |
| White return | 0 |

### Conservative Defaults [T1]

| Ambiguity | Default |
|---|---|
| Return type unknown | White return (0 special deduction) |
| Bookkeeping method unknown | Simplified (100,000 deduction) |
| Home office apportionment unknown | 0% deduction until confirmed |
| Business vs personal expense unclear | Non-deductible |
| Withholding tax credit not confirmed | Exclude until verified |

### Red Flag Thresholds [T1]

| Flag | Threshold |
|---|---|
| Consumption tax registration required | Annual revenue > JPY 10,000,000 in prior 2 years |
| Withholding applies to professional fees | Client is a corporation paying > JPY 1,000 per payment |
| Blue return requires advance application | Form 144 (青色申告承認申請書) by 15 March of target year |
| Loss carry-forward | Blue return only -- 3 years |
| Blue return asset expensing limit | JPY 300,000/item (aggregate JPY 3,000,000/year) |

---

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

**Minimum viable:** Bank statement for the full calendar year (January--December) in CSV, PDF, or pasted text. Confirmation of return type (blue/white) and bookkeeping method.

**Recommended:** All invoices issued (Misoca, freee, MF Cloud), withholding tax certificates (源泉徴収票) from clients, national pension payment receipts (国民年金), national health insurance receipts (国民健康保険).

**Ideal:** Complete double-entry general ledger, asset register, prior year return (申告書 copy), e-Tax filing confirmation, iDeCo/small enterprise mutual aid (小規模企業共済) contribution statements.

### Refusal Catalogue

**R-JP-1 -- Non-residents (非居住者).** "Non-resident taxation has different sourcing rules and treaty interactions. Out of scope -- escalate."

**R-JP-2 -- Corporate entities (法人).** "Corporations file Corporate Tax (法人税), not income tax. Out of scope."

**R-JP-3 -- Real estate capital gains / inherited property.** "Separate computation with different rates. Escalate."

**R-JP-4 -- Cryptocurrency (暗号資産).** "Crypto profits are 'miscellaneous income' (雑所得) taxed up to 55% including resident tax. Complex classification rules apply. Escalate."

**R-JP-5 -- Non-permanent resident status (非永住者).** "Non-permanent residents have limited worldwide income taxation. Requires specialist review. Escalate."

---

## Section 3 -- Transaction Pattern Library

This is the deterministic pre-classifier. When a bank statement line matches a pattern, apply the treatment directly. If no pattern matches, fall through to Tier 1 rules in Section 5.

### 3.1 Income Patterns (Credits -- 入金)

| Pattern | Tax Line | Treatment | Notes |
|---|---|---|---|
| 振込 [client name] / 入金 [client company] | 事業収入 (business revenue) | Gross revenue | Professional fee from client |
| 銀行振込 [sender] / 普通振込 | 事業収入 | Revenue | Standard bank transfer from client |
| STRIPE PAYOUT / STRIPE TRANSFER | 事業収入 | Revenue | Stripe Japan / international clients -- match to invoices |
| PAYPAL TRANSFER / ペイパル | 事業収入 | Revenue | International client payments |
| freee PAYMENT / フリー支払 | 事業収入 | Revenue | freee Payments platform settlement |
| Amazon Pay 振込 / Amazonペイ | 事業収入 | Revenue | E-commerce platform payout |
| BASE SETTLEMENT / BASE振込 | 事業収入 | Revenue | BASE (JP e-commerce) settlement |
| メルカリ振込 / MERCARI | 事業収入 | Revenue | Mercari business seller payout |
| 報酬振込 [client] | 事業収入 | Revenue | Honorarium / professional fee |
| 源泉徴収後振込 [amount] | 事業収入 (gross-up required) | Revenue -- GROSS UP | Client withheld 10.21%; gross up to full invoice amount |
| 給与振込 [employer] | 給与所得 (employment income) | NOT business income | Employment wage -- separate Anlage equivalent: 給与所得 |
| 利子 / 利息 [bank] | 利子所得 (interest income) | NOT business income | Bank interest -- separate income category |
| 配当金 [company] | 配当所得 (dividend income) | NOT business income | Dividend |
| 還付金 国税局 / 税金還付 | EXCLUDE | Not income | Tax refund not taxable |
| 贈与 / 振込 PERSONAL | EXCLUDE | Personal transfer | Personal gifts / personal transfers |

### 3.2 Expense Patterns (Debits -- 出金)

| Pattern | Tax Line (必要経費) | Treatment | Notes |
|---|---|---|---|
| 事務所賃料 / オフィス家賃 [landlord] | 地代家賃 (rent) | Fully deductible | Dedicated business premises |
| 電気料金 [TEPCO/関西電力/中部電力/九州電力] | 水道光熱費 (utilities) | Business portion deductible | Home office: apportion by floor area or time |
| 水道料金 / 水道局 | 水道光熱費 | Business portion | Apportion if home office |
| インターネット [NURO/フレッツ/au/ドコモ光] | 通信費 (communications) | Business portion only | Default: ask client for % |
| 携帯電話 [ドコモ/au/SoftBank/楽天モバイル] | 通信費 | Business portion only | Mixed use: apportion |
| 交通費 [JR/東京メトロ/新幹線/バス] | 旅費交通費 (travel) | Fully deductible if business | IC card statements are acceptable |
| 航空券 [ANA/JAL/LCC] | 旅費交通費 | Fully deductible if business purpose | Keep booking confirmation |
| 接待 [restaurant] / 飲食 | 接待交際費 (entertainment) | Deductible if business purpose | No statutory cap for sole proprietors; document names, purpose |
| 書籍 [Amazon Japan/紀伊國屋/丸善] | 新聞図書費 (books/publications) | Fully deductible if professional | |
| セミナー [event] / 研修費 | 研修費 (training) | Fully deductible | |
| ソフトウェア [Adobe/Microsoft/Figma/Notion] | 消耗品費 or 減価償却費 | Under JPY 100,000: fully deductible; over: depreciate | Subscription vs perpetual licence distinction |
| 広告費 [Google Ads/Meta Ads] | 広告宣伝費 (advertising) | Fully deductible | |
| 税理士報酬 / 会計士報酬 | 税理士・弁護士費用 | Fully deductible | Professional adviser fees |
| 損害保険 [business] | 損害保険料 (insurance) | Fully deductible | Business liability only |
| 外注費 / フリーランス費用 | 外注工賃 (subcontracting) | Fully deductible | |
| 銀行手数料 / 振込手数料 | 雑費 (miscellaneous) | Fully deductible | Business account only |
| 国民年金 / 国民年金保険料 | 社会保険料控除 (NOT 必要経費) | EXCLUDE from business expenses | Deducted as income deduction (所得控除), not business expense |
| 国民健康保険 / 国保料 | 社会保険料控除 (NOT 必要経費) | EXCLUDE from business expenses | Same -- income deduction, not business expense |
| 所得税 振替 / 住民税 口座振替 | EXCLUDE | Tax payments | Not deductible |
| 生命保険 [Nippon Life/Dai-ichi/明治安田] | 生命保険料控除 (NOT 必要経費) | EXCLUDE from business expenses | Personal insurance = income deduction |
| プライベート引き出し / ATM出金 | EXCLUDE | Personal withdrawal | Drawings -- not business expense; ask what it was for |

### 3.3 SaaS / Cloud Service Patterns

| Pattern | Treatment | Notes |
|---|---|---|
| Adobe Systems / Adobe Creative Cloud | 消耗品費 (operating expense) | Subscription: fully deductible. Check if annual or monthly. |
| Microsoft / Office 365 / M365 | 消耗品費 | Subscription: deductible |
| Google Workspace / G Suite | 消耗品費 | Subscription: deductible |
| freee / Money Forward Cloud / Yayoi | 消耗品費 | Accounting software: deductible |
| Slack / Notion / Figma | 消耗品費 | Business SaaS: deductible |
| AWS Japan / Amazon Web Services | 消耗品費 | Cloud hosting: deductible |

---

## Section 4 -- Worked Examples

### Example 1 -- Client Wire Transfer (Bank Transfer Income)

**Input line (三菱UFJ Bank / Mitsubishi UFJ Bank statement):**
`2025/03/15 | 振込入金 デザインスタジオABC | +350,000 | 残高 1,240,500`

**Reasoning:**
Wire transfer from a business client for design services. This is 事業収入 (business revenue). If client is a corporation and fee ≥ JPY 1,000, they are required to withhold 10.21% (source tax). Check whether the JPY 350,000 is net of withholding. If invoice was JPY 390,000 and client withheld JPY 39,819 (10.21%), the bank statement would show JPY 350,181. Always gross up to invoice amount.

**Classification:** 事業収入 JPY 350,000 (or gross up if TDS was deducted).

### Example 2 -- Withholding (源泉徴収) on Professional Fee

**Input line (楽天銀行 Rakuten Bank statement):**
`2025/05/20 | 振込 株式会社マーケティングXYZ 源泉後 | +107,892 | Ref: 202505-0234`

**Reasoning:**
Received JPY 107,892. Likely gross invoice of JPY 120,000 with 10.21% withholding = JPY 12,252 withheld. Net paid = JPY 107,748 (minor rounding applies per Japanese rules). The gross income is JPY 120,000. The withheld amount JPY 12,252 is a tax credit (源泉徴収税額) claimed on the final return. Verify against client's withholding certificate (支払調書).

**Classification:** 事業収入 JPY 120,000 (gross). Tax credit: JPY 12,252.

### Example 3 -- National Pension Payment

**Input line (ゆうちょ銀行 Japan Post Bank statement):**
`2025/04/30 | 国民年金保険料 振替 | -16,590 | 残高 852,410`

**Reasoning:**
National pension premium (国民年金保険料) JPY 16,590. This is NOT a business expense (必要経費). It is an income deduction (社会保険料控除 -- social insurance deduction) under Section 79 of the Income Tax Act. Remove from the business expense schedule. Record in the 所得控除 (income deductions) section -- fully deductible as social insurance deduction.

**Classification:** EXCLUDE from 必要経費. Record as 社会保険料控除.

### Example 4 -- Home Internet Bill

**Input line (住信SBIネット銀行 SBI Sumishin Net Bank statement):**
`2025/07/10 | NURO光 利用料 | -5,500 | 残高 423,800`

**Reasoning:**
Monthly internet bill (NURO Hikari) JPY 5,500. This is a mixed-use expense -- used for both business and personal internet access. NTA accepts a reasonable business apportionment. If the taxpayer estimates 70% business use (working from home full-time), then JPY 3,850 is deductible. If no apportionment can be supported, default is 0%.

**Classification:** 通信費 -- PENDING apportionment. Default: 0%. Flag for reviewer.

### Example 5 -- Software Subscription

**Input line (三井住友銀行 SMBC statement):**
`2025/09/01 | ADOBE SYSTEMS | -72,600 | 残高 1,540,200`

**Reasoning:**
Adobe Creative Cloud annual subscription JPY 72,600. This is a subscription (月額/年額契約), not a perpetual licence. Subscription costs are 消耗品費 (consumables/operating expenses) deductible in full in the year paid, regardless of the JPY 100,000 capitalisation threshold (which applies to assets, not subscriptions).

**Classification:** 消耗品費 JPY 72,600. Fully deductible.

### Example 6 -- Business Entertainment Dinner

**Input line (みずほ銀行 Mizuho Bank statement):**
`2025/11/12 | デビットカード 銀座レストランXX | -48,000 | 残高 3,210,500`

**Reasoning:**
Restaurant meal JPY 48,000. If this was a client entertainment dinner (接待交際費), it is deductible as a business expense for sole proprietors -- Japan has NO statutory percentage limit for sole proprietors (unlike Germany's 70% rule). However, excessive entertainment will attract NTA scrutiny. Must document: date, restaurant name, names of attendees, business purpose.

**Classification:** 接待交際費 JPY 48,000. Fully deductible if properly documented. Flag for reviewer if aggregate entertainment is high.

---

## Section 5 -- Tier 1 Rules (When Data Is Clear)

### 5.1 Business Revenue (事業収入)

**Legislation:** Income Tax Act Article 27

All business revenue (professional fees, contract income, product sales) is 事業収入. For consumption tax (消費税) registered taxpayers, report net of consumption tax. For non-registered (below JPY 10M threshold), report gross including CT.

### 5.2 Necessary Expenses (必要経費)

**Legislation:** Income Tax Act Article 37

Expenses are deductible if directly incurred for earning business income (業務の遂行に直接必要). Japan allows apportionment of mixed-use expenses where business and personal portions can be separated objectively (按分 -- 按分計算).

### 5.3 Blue Return Special Deduction (青色申告特別控除)

**Legislation:** Measures Act Article 25-2

| Method | Deduction | Conditions |
|---|---|---|
| Double-entry + e-Tax | JPY 650,000 | Must file via e-Tax AND maintain double-entry books |
| Double-entry + paper | JPY 550,000 | Double-entry books, paper filing |
| Simplified bookkeeping | JPY 100,000 | Simplified (簡易簿記) books, either filing method |
| White return | JPY 0 | No special deduction |

### 5.4 Depreciation (減価償却)

**Legislation:** Income Tax Act Article 49; NTA depreciation tables

| Asset | Useful Life | Declining Balance Rate |
|---|---|---|
| Personal computers | 4 years | 0.500 |
| Servers | 5 years | 0.400 |
| Office furniture (wood) | 8 years | 0.250 |
| Motor vehicles (standard) | 6 years | 0.333 |
| Software (purchased) | 3-5 years | varies |

**Expensing rules:**
- Under JPY 100,000: expense immediately (少額減価償却資産)
- JPY 100,000 -- JPY 199,999: option to depreciate uniformly over 3 years (一括償却資産)
- Blue return filers: under JPY 300,000 can be expensed immediately, subject to aggregate limit of JPY 3,000,000/year

### 5.5 Income Deductions (所得控除)

| Deduction | Amount (2025) |
|---|---|
| Basic deduction (基礎控除) | JPY 580,000 (standard); temporary enhancement for income ≤ JPY 6,550,000 -- see below |
| Social insurance (社会保険料控除) | Full amount paid (national pension + health insurance) |
| Small enterprise mutual aid (小規模企業共済) | Full amount paid |
| iDeCo contributions | Full amount paid |
| Life insurance (生命保険料控除) | Up to JPY 120,000 combined |
| Spouse deduction (配偶者控除) | Up to JPY 380,000 (if spouse income ≤ JPY 480,000) |
| Dependent deduction (扶養控除) | JPY 380,000--630,000 per dependent |

**2025 Temporary Enhanced Basic Deduction:**

| Total Income (合計所得金額) | Basic Deduction (2025) |
|---|---|
| Up to JPY 1,320,000 | JPY 950,000 |
| JPY 1,320,001 -- 2,695,000 | JPY 880,000 |
| JPY 2,695,001 -- 6,550,000 | JPY 680,000 |
| JPY 6,550,001 -- 23,500,000 | JPY 580,000 |
| Above JPY 25,000,000 | JPY 0 |

### 5.6 Advance Tax / Estimated Tax (予定納税)

Applies to taxpayers whose prior year national income tax exceeded JPY 150,000. NTA sends a notification. Two instalments: July 31 and November 30, each = 1/3 of prior year's tax.

### 5.7 Filing Deadlines

| Item | Deadline |
|---|---|
| Final return (確定申告) | 15 March of following year |
| Tax payment | 15 March |
| Estimated tax (予定納税) 1st | 31 July |
| Estimated tax 2nd | 30 November |
| Resident tax payment (quarterly) | June, August, October, January |

### 5.8 Penalties

| Offence | Penalty |
|---|---|
| Late filing (within 1 month, voluntary) | 5% of additional tax (無申告加算税) |
| Late filing (after notice or > 1 month) | 15% on first JPY 500,000 + 20% on excess |
| Under-reporting | 10% of additional tax |
| Fraud / concealment | 35-40% (重加算税) |
| Late payment interest (延滞税) | ~2.4% for first 2 months, ~8.7% thereafter |

---

## Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Home Office (家事按分)

NTA accepts reasonable apportionment of home rent, electricity, internet by floor area ratio or time-based ratio. No requirement for a dedicated room. Acceptable range: 20-50% for full-time home workers. Must be documented and consistent year to year.

**Flag for reviewer:** Confirm apportionment method, floor area, and documentation.

### 6.2 Vehicle Business Use

Sole proprietors using a vehicle for business can deduct a proportion of running costs (fuel, insurance, road tax, depreciation). Requires either a mileage log or a reasonable percentage documented.

**Flag for reviewer:** Confirm business-use percentage and documentation.

### 6.3 Entertainment Expenses (接待交際費)

Japan has no statutory cap on entertainment deductions for sole proprietors. However, unusually high entertainment expenses relative to revenue will attract NTA scrutiny. Each meal/event should be documented with attendee names, business purpose, date, venue.

### 6.4 Spouse / Family Employee Salary (専従者給与)

Blue return filers may deduct salaries paid to family members working in the business (pre-registered as 専従者). White return filers are limited to a notional allowance (JPY 500,000 for spouse, JPY 860,000 for others). Flag if family salaries appear in bank data.

### 6.5 iDeCo / Small Enterprise Mutual Aid

Contributions to iDeCo (個人型確定拠出年金) or small enterprise mutual aid (小規模企業共済) are fully deductible as income deductions. Large contributions can significantly reduce tax liability. Flag if client mentions these -- confirm amounts from contribution statements.

---

## Section 7 -- Excel Working Paper Template

```
確定申告 WORKING PAPER -- Tax Year 2025
Taxpayer: _______________  My Number: ___________
Return type: Blue (double-entry / simplified) / White [circle one]
Filing method: e-Tax / Paper [circle one]

A. 事業収入 (GROSS BUSINESS REVENUE)
  A1. Total invoiced / received               ___________
  A2. Less: consumption tax collected (if CT-registered)  ___________
  A3. Net business revenue                    ___________

B. 必要経費 (NECESSARY EXPENSES)
  B1. 地代家賃 (rent / office costs)          ___________
  B2. 水道光熱費 (utilities -- business %)    ___________
  B3. 通信費 (phone/internet -- business %)  ___________
  B4. 旅費交通費 (travel)                    ___________
  B5. 接待交際費 (entertainment)             ___________
  B6. 広告宣伝費 (advertising)              ___________
  B7. 消耗品費 (consumables / SaaS)         ___________
  B8. 減価償却費 (depreciation)             ___________
  B9. 外注工賃 (subcontracting)             ___________
  B10. 税理士費用 (adviser fees)            ___________
  B11. 雑費 (bank charges, misc)            ___________
  B12. Total 必要経費                        ___________

C. 事業所得 BEFORE DEDUCTION (A3 - B12)      ___________

D. 青色申告特別控除 (Blue return deduction)  ___________

E. 事業所得 (C - D)                          ___________

F. 所得控除 (INCOME DEDUCTIONS)
  F1. 基礎控除 (basic deduction)            ___________
  F2. 社会保険料控除 (NHI + pension)        ___________
  F3. 小規模企業共済等 (iDeCo, etc.)       ___________
  F4. 生命保険料控除                        ___________
  F5. 配偶者控除 / 扶養控除               ___________
  F6. Total 所得控除                        ___________

G. 課税所得 (E - F6) -- round down to 1,000  ___________

H. 所得税 (apply rate table)                 ___________

I. 復興特別所得税 (H x 2.1%)               ___________

J. TOTAL NATIONAL TAX (H + I)               ___________

K. 源泉徴収税額 (withholding credits)       ___________

L. 予定納税 (estimated tax credits)         ___________

M. NET TAX DUE / REFUND (J - K - L)        ___________

REVIEWER FLAGS:
  [ ] Blue return application filed in advance?
  [ ] Bookkeeping method confirmed (double-entry vs simplified)?
  [ ] Home office apportionment documented?
  [ ] Withholding credits verified against 支払調書?
  [ ] National pension / NHI receipts confirmed?
```

---

## Section 8 -- Bank Statement Reading Guide

### Japanese Bank Statement Formats

| Bank | Format | Key Fields |
|---|---|---|
| 三菱UFJ (MUFG) | CSV / PDF | 日付, 摘要, お引出し, お預入れ, 残高 |
| みずほ銀行 (Mizuho) | CSV | 取引年月日, 摘要, お支払金額, お預り金額, 差引残高 |
| 三井住友銀行 (SMBC) | CSV / PDF | 年月日, 摘要, 支払金額, 預入金額, 残高 |
| 楽天銀行 (Rakuten Bank) | CSV | 取引日, 入出金(円), 残高(円), 取引名称, 利用先 |
| ゆうちょ銀行 (Japan Post Bank) | CSV | 年月日, 摘要, 支払金額, 預入金額, 差引残高 |
| 住信SBIネット銀行 (SBI Sumishin) | CSV | 取引日, 内容, 出金金額, 入金金額, 残高 |

### Key Japanese Banking Terms

| Japanese Term | English | Classification Hint |
|---|---|---|
| 振込入金 | Wire transfer in | Potential income |
| 振込出金 / 振込手数料 | Wire transfer out / fee | Potential expense or bank fee |
| 自動振替 | Auto debit | Regular expense (utilities, insurance) |
| カード利用 | Card payment | Identify payee |
| ATM出金 | ATM withdrawal | Personal -- ask purpose |
| 利息 / 利子 | Interest | Other income |
| 税金 口座振替 | Tax payment auto-debit | Exclude (tax payment) |
| 国民年金 振替 | Pension auto-debit | Income deduction (not expense) |
| 国保 振替 | Health insurance auto-debit | Income deduction (not expense) |

---

## Section 9 -- Onboarding Fallback

If the client provides a bank statement but cannot answer onboarding questions immediately:

1. Classify all 振込入金 credits from non-bank entities as potential 事業収入
2. Mark all 国民年金 and 国保 debits as 社会保険料控除 (income deductions)
3. Apply conservative defaults: white return (0 special deduction), 0% home office
4. Flag all restaurant / entertainment debits as PENDING
5. Generate working paper with clear PENDING flags

Present these questions:

```
ONBOARDING QUESTIONS -- JAPAN INCOME TAX (確定申告)
1. Blue return or white return (青色申告 or 白色申告)?
2. Bookkeeping: double-entry (複式簿記) or simplified (簡易簿記)?
3. Filing method: e-Tax or paper?
4. Are you registered for consumption tax (消費税)?
5. Home office: what % of home floor area is used for business?
6. Withholding (源泉徴収): do any clients deduct tax before paying?
7. Do you have a 支払調書 (payment record) from each withholding client?
8. iDeCo or 小規模企業共済 contributions this year?
9. Spouse / dependents?
10. Prior year estimated tax (予定納税) notices?
```

---

## Section 10 -- Reference Material

### Key Legislation

| Topic | Article |
|---|---|
| Business income (事業所得) | Income Tax Act Art. 27 |
| Necessary expenses (必要経費) | ITA Art. 37 |
| Blue return (青色申告) | ITA Art. 143-148 |
| Blue return special deduction | Special Taxation Measures Act Art. 25-2 |
| Depreciation | ITA Art. 49 |
| Income deductions (所得控除) | ITA Art. 72-86 |
| Reconstruction surtax | Act on Special Measures for Securing Financial Resources Necessary for Reconstruction |
| Estimated tax (予定納税) | ITA Art. 104-109 |

### Known Gaps / Out of Scope

- Non-resident taxation (非居住者)
- Cryptocurrency / virtual digital assets (暗号資産)
- Real estate capital gains (土地建物の譲渡所得)
- Inheritance tax (相続税)
- Consumption tax (消費税) return -- separate skill required

### Changelog

| Version | Date | Change |
|---|---|---|
| 2.0 | April 2026 | Full rewrite to v2.0 structure; Japanese bank format guide; local platform patterns; worked examples |
| 1.0 | 2025 | Initial version |

### Self-Check

- [ ] Reconstruction surtax (2.1%) added to national income tax?
- [ ] Taxable income rounded DOWN to nearest JPY 1,000 before applying rates?
- [ ] Final tax rounded DOWN to nearest JPY 100?
- [ ] National pension and health insurance excluded from 必要経費?
- [ ] Blue return deduction matched to correct bookkeeping method?
- [ ] Withholding credits verified against 支払調書, not just bank statement?
- [ ] Blue return advance application verified (Form 144)?

---

## PROHIBITIONS

- NEVER omit the reconstruction special income tax (2.1%) -- it applies to all income tax through 2037
- NEVER apply the JPY 650,000 blue return deduction without confirming double-entry bookkeeping AND e-Tax filing
- NEVER allow national pension or health insurance as 必要経費 -- they are 所得控除
- NEVER allow income tax or resident tax as a deduction
- NEVER allow white return filers to carry forward losses
- NEVER skip rounding down taxable income to nearest JPY 1,000 before applying rates
- NEVER skip rounding down final tax to nearest JPY 100
- NEVER present tax calculations as definitive -- always label as estimated and direct client to their 税理士 for confirmation

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a 税理士 or equivalent licensed practitioner in Japan) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
