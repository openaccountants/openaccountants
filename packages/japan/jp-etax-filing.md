---
name: jp-etax-filing
description: "Use this skill whenever asked about filing a Japanese tax return electronically via e-Tax (確定申告書等作成コーナー). Trigger on phrases like \"e-Tax\", \"電子申告\", \"e-Tax filing\", \"確定申告書等作成コーナー\", \"how to file taxes in Japan online\", \"e-Tax submission\", \"マイナンバーカード認証\", \"QR code authentication e-Tax\", \"blue return financial statements\", \"決算書入力\", \"所得税申告書\", \"consumption tax return filing\", \"消費税申告書作成\", or any question about the step-by-step process of filing income tax or consumption tax returns electronically in Japan. This skill covers the complete e-Tax workflow: authentication, financial statement entry (決算書), income tax return entry (申告書B), consumption tax return entry, and electronic submission. ALWAYS read this skill before assisting with any Japan e-Tax filing work."
version: 1.0
jurisdiction: JP
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on: - jp-income-tax
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# JP Etax Filing

## Japan e-Tax Filing (電子申告) -- Self-Employed Skill v1.0

> Based on work by [Kazuki Nagata (@kazukinagata)](https://github.com/kazukinagata/shinkoku), licensed under MIT. Adapted for the OpenAccountants format.

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Japan (日本) |
| System | e-Tax (国税電子申告・納税システム) |
| Portal URL | https://www.keisan.nta.go.jp/ |
| Portal Name | 確定申告書等作成コーナー (Tax Return Preparation Corner) |
| Authentication | My Number Card (マイナンバーカード) via smartphone QR code or IC card reader |
| Tax Authority | National Tax Agency (国税庁 NTA) |
| Filing Deadline (Income Tax) | 15 March of the following year |
| Filing Deadline (Consumption Tax) | 31 March of the following year |
| Contributor | Open Accountants Community |
| Validated by | Pending -- requires sign-off by a Japanese 税理士 (Zeirishi) |
| Skill version | 1.0 |

## Section 2 -- Prerequisites

Before starting the e-Tax filing process, ensure:

1. **Income tax calculations are complete** -- use the `jp-income-tax` skill to compute all figures
2. **Financial statements (決算書) are prepared** -- P/L (損益計算書) and B/S (貸借対照表) for blue return filers
3. **Consumption tax calculations are complete** (if applicable) -- use the `jp-consumption-tax` skill
4. **Taxpayer profile is ready** -- name, address, My Number (マイナンバー), tax office name, business type, trade name (屋号)
5. **Authentication method is available** -- My Number Card + smartphone with マイナポータル app, or IC card reader

### Required Documents at Hand

**Required Documents at Hand**

| Document | Japanese Name | Purpose |
| --- | --- | --- |
| My Number Card | マイナンバーカード | Authentication + electronic signature |
| Withholding certificates | 源泉徴収票 | Employment income data |
| Payment records | 支払調書 | Business withholding data |
| Insurance premium certificates | 控除証明書 | Deduction claims |
| Prior year return (optional) | 前年の確定申告書 | Reference for estimated tax |
| Bank account details | 口座情報 | Refund account or payment method |

## Section 3 -- e-Tax Screen Flow Overview

The 確定申告書等作成コーナー follows this overall flow:

```
Step 1: Submission Method Selection (CC-AA-010)
    ↓
Step 2: Return Type Selection (CC-AE-090)
    ↓
Step 3: My Number Portal Linkage (CC-AE-600)
    ↓
Step 4: Pre-submission Confirmation (CC-AA-024)
    ↓
Step 5: QR Code Authentication (CC-AA-440) ★ Manual step
    ↓
Step 6: Financial Statements Entry (決算書コーナー)
    ├── P/L Entry (損益計算書)
    ├── Blue Return Deduction (青色申告特別控除)
    ├── B/S Entry (貸借対照表)
    ├── Income Confirmation (所得確認)
    └── Address/Name Entry (住所・氏名)
    ↓
Step 7: Income Tax Return Entry (所得税コーナー)
    ├── Income Type Selection (所得選択)
    ├── Income Entry by Type (収入入力)
    ├── Deductions Entry -- Part 1 (控除入力1/2)
    ├── Deductions Entry -- Part 2 (控除入力2/2)
    ├── Calculation Result Confirmation (計算結果確認)
    ├── Payment Method (納付方法)
    ├── Resident Tax Settings (住民税)
    ├── Personal Information (基本情報)
    └── My Number Entry (マイナンバー)
    ↓
Step 8: Consumption Tax Return (消費税コーナー) -- if applicable
    ├── Method Determination (条件判定)
    ├── Income Category Selection (所得区分選択)
    ├── Sales Entry (売上入力)
    └── Calculation Result (計算結果)
    ↓
Step 9: Electronic Signature & Submission ★ Manual step
    ↓
Step 10: Data File Save (.data)
```

## Section 4 -- Step-by-Step Filing Workflow

### 4.1 Submission Method Selection (提出方法の選択)

**Submission Method Selection (Screen: CC-AA-010)**  _(Screen: CC-AA-010)_

| Question | Answer |
| --- | --- |
| Do you have a My Number Card (マイナンバーカード)? | Yes (はい) |
| Do you have a compatible smartphone or IC card reader? | Yes (はい) |
| Method | Select "Use Smartphone" (スマートフォンを使用する) |

### 4.2 Return Type Selection (申告書等の選択)

**Return Type Selection (Screen: CC-AE-090)**  _(Screen: CC-AE-090)_

| Option | When to Select |
| --- | --- |
| Income Tax (所得税) | Salary income only, no business income |
| Financial Statements + Income Tax (決算書・収支内訳書＋所得税) | **Self-employed with business income** -- most common |
| Consumption Tax (消費税) | File separately after income tax |
| Gift Tax (贈与税) | Gift tax only |

**For self-employed taxpayers, select "Financial Statements + Income Tax".**

### 4.3 My Number Portal Linkage

Select "Do not use My Number Portal linkage" (マイナポータル連携を利用しない) unless you have already configured the linkage.

### 4.4 Pre-submission Confirmation

Review the terms of use and click "Agree and proceed" (利用規約に同意して次へ).

### 4.5 QR Code Authentication (QRコード認証)

**This requires manual action by the taxpayer:**

1. A QR code appears on screen
2. Open the マイナポータル app on your smartphone
3. Scan the QR code displayed on the computer screen
4. Authenticate with your My Number Card (hold card to phone's NFC reader)
5. Enter your 4-digit PIN (利用者証明用電子証明書の暗証番号)
6. The screen will automatically proceed after successful authentication

**Troubleshooting:** If the QR code does not display, ensure you are using a supported browser (Chrome or Edge on Windows, Safari on macOS). Linux is not officially supported.

## Section 5 -- Financial Statements Entry (決算書コーナー)

This section applies to self-employed taxpayers filing a blue return (青色申告).

### 5.1 Select Statement Type

**Select Statement Type**

| Option | When to Select |
| --- | --- |
| Blue Return Financial Statements (青色申告決算書) | Blue return filers (most common) |
| Income/Expense Statement (収支内訳書) | White return filers |
| Blue Return -- Cash Basis (青色申告決算書・現金主義用) | Cash-basis filers (rare) |

### 5.2 Profit & Loss Statement (損益計算書) Entry

Enter the fiscal period (typically January 1 -- December 31) and the following data:

**Revenue Section:**
- Monthly sales breakdown (月別売上) -- 12 months
- Monthly cost of goods sold (月別仕入) -- if applicable
- Personal consumption (家事消費等)
- Miscellaneous income (雑収入)

**Expense Section (経費)**

| Line | Expense Category | Japanese Name |
| --- | --- | --- |
| 8 | Taxes and public charges | 租税公課 |
| 9 | Packing and shipping | 荷造運賃 |
| 10 | Utilities | 水道光熱費 |
| 11 | Travel and transportation | 旅費交通費 |
| 12 | Communication | 通信費 |
| 13 | Advertising | 広告宣伝費 |
| 14 | Entertainment | 接待交際費 |
| 15 | Insurance | 損害保険料 |
| 16 | Repairs | 修繕費 |
| 17 | Consumables | 消耗品費 |
| 18 | Depreciation | 減価償却費 (sub-form entry) |
| 19 | Welfare | 福利厚生費 |
| 20 | Salaries | 給料賃金 (sub-form entry) |
| 21 | Subcontracting | 外注工賃 |
| 22 | Interest | 利子割引料 (sub-form entry) |
| 23 | Rent | 地代家賃 (sub-form entry) |
| 24 | Bad debts | 貸倒金 |
| 25 | Tax adviser fees | 税理士等の報酬 |
| 26-30 | Custom expense categories | 任意科目 |
| 31 | Miscellaneous | 雑費 |

### 5.3 Blue Return Special Deduction (青色申告特別控除)

**Blue Return Special Deduction Q&A**

| Deduction | Conditions |
| --- | --- |
| JPY 650,000 | Double-entry bookkeeping + e-Tax submission (required for this amount) |
| JPY 550,000 | Double-entry bookkeeping + paper submission |
| JPY 100,000 | Simplified bookkeeping |

- **KS-E10089** — If filing via e-Tax and selecting JPY 650,000, the system will verify e-Tax submission is being used. Paper filing with this selection will trigger error KS-E10089.  _(KS-E10089)_

### 5.4 Balance Sheet (貸借対照表) Entry

Enter opening and closing balances for:

**Assets (資産の部):**
Cash, deposits, accounts receivable, securities, inventory, prepayments, buildings, equipment, vehicles, tools/fixtures, land, and custom asset accounts.

**Liabilities & Equity (負債・資本の部):**
Notes payable, accounts payable, borrowings, accrued expenses, deposits received, allowance for bad debts, capital (元入金), owner's draws (事業主貸), owner's contributions (事業主借), and pre-deduction income.

**The system will reject the entry (error KS-E40003) if total assets ≠ total liabilities + equity at year-end.**

- **KS-E40003** — The system will reject the entry (error KS-E40003) if total assets ≠ total liabilities + equity at year-end.  _(KS-E40003)_

### 5.5 Address and Name Entry (住所・氏名等)

**Address and Name Entry**

| Field | Details |
| --- | --- |
| Postal code | 7-digit postal code |
| Prefecture and address | Full residential address |
| Business address | If different from home |
| Tax office | Submitting tax office name (所轄税務署) |
| Full name | In kanji |
| Business type | e.g., IT consultant, designer, writer |
| Trade name (屋号) | If applicable |
| Submission date | Date of filing |

## Section 6 -- Income Tax Return Entry (所得税コーナー)

After completing financial statements, the system transitions to the income tax return.

### 6.1 Income Type Selection (所得種類の選択)

**Income Type Selection**

| Income Type | Japanese | Typical Selection |
| --- | --- | --- |
| Employment | 給与 | If also employed |
| Business (commercial) | 事業（営業等） | **Self-employed: always check** |
| Business (agriculture) | 事業（農業） | If applicable |
| Real estate | 不動産 | If rental income |
| Miscellaneous (business/other) | 雑（業務・その他） | Side income, crypto |
| Public pension | 公的年金等 | If receiving pension |
| Retirement | 退職金 | If received |
| Stocks/dividends | 株式等 | If applicable |
| Temporary income | 一時 | Insurance payouts, prizes |

### 6.2 Income Entry by Type

For each selected income type, enter the relevant data through dedicated sub-forms:

**Employment income (給与所得):** Enter data from withholding certificates (源泉徴収票) -- payment amount, withheld tax, social insurance premiums, and employer details.

**Business income (事業所得):** Automatically populated from the financial statements entered in Step 5.

**Miscellaneous income (雑所得):** Enter revenue, expenses, and payer details for each item.

### 6.3 Deductions Entry -- Part 1 (支出系控除)

**Deductions Entry -- Part 1**

| Deduction | Japanese | Data Source |
| --- | --- | --- |
| Social insurance premiums | 社会保険料控除 | Partially from withholding certificate |
| Small enterprise mutual aid | 小規模企業共済等掛金控除 | iDeCo, mutual aid contribution certificates |
| Life insurance premiums | 生命保険料控除 | Insurance premium certificates |
| Earthquake insurance | 地震保険料控除 | Insurance certificates |
| Casualty losses | 雑損控除 | If applicable |
| Medical expenses | 医療費控除 | Medical expense summary |
| Charitable donations | 寄附金控除 | Furusato nozei + other donation receipts |

### 6.4 Deductions Entry -- Part 2 (人的控除・住宅控除等)

**Deductions Entry -- Part 2**

| Deduction | Japanese | Notes |
| --- | --- | --- |
| Spouse deduction | 配偶者（特別）控除 | Based on spouse's income |
| Dependent deduction | 扶養控除 | By age category |
| Widow/single parent | 寡婦・ひとり親控除 | If applicable |
| Working student | 勤労学生控除 | If applicable |
| Disability | 障害者控除 | If applicable |
| Basic deduction | 基礎控除 | Calculated automatically |
| Housing loan deduction | 住宅借入金等特別控除 | First year requires details |
| Estimated tax paid | 予定納税額 | If advance payments were made |
| Loss carryforward | 繰越損失額 | Blue return only, up to 3 years |

### 6.5 Calculation Result Confirmation (計算結果の確認)

**Calculation Result Confirmation**

| Item | What to Verify |
| --- | --- |
| Total income (合計所得金額) | Matches your working paper |
| Total deductions (所得控除合計) | Matches your calculations |
| Taxable income (課税所得金額) | Rounded down to nearest JPY 1,000 |
| Computed tax (算出税額) | Rate table correctly applied |
| Tax credits | Housing loan, dividend credits |
| Reconstruction surtax (復興特別所得税) | 2.1% of base income tax |
| Total tax (所得税及び復興特別所得税) | Sum of income tax + reconstruction tax |
| Withholding credits (源泉徴収税額) | All withholding properly credited |
| Tax due or refund (申告納税額/還付) | Final amount to pay or receive |

**Cross-check all figures against your income tax working paper. Any discrepancy should be investigated before proceeding.**

### 6.6 Payment Method (納付方法)

**Payment Method**

| Method | Japanese | Notes |
| --- | --- | --- |
| Account transfer | 振替納税 | Auto-debit from bank account |
| Electronic payment | 電子納税 | Direct debit or internet banking |
| Credit card | クレジットカード納付 | Fee applies |
| Convenience store | コンビニ納付 | For amounts under JPY 300,000 |
| Bank counter | 金融機関等での窓口納付 | Traditional method |

If a refund is due, enter bank account details (bank name, branch, account number, account holder).

### 6.7 Personal Information & My Number

Enter personal details (name in kana and kanji, phone number, address, tax office, occupation, trade name) and your 12-digit My Number (マイナンバー). The system validates the check digit.

## Section 7 -- Consumption Tax Return (消費税コーナー)

If you are a taxable business (課税事業者) for consumption tax, file the consumption tax return after completing the income tax return.

### 7.1 Method Determination (条件判定)

**Method Determination Fields**

| Field | What to Enter |
| --- | --- |
| Base period taxable sales (基準期間の課税売上高) | Sales from 2 years prior |
| Qualified invoice issuer (インボイス発行事業者) | Yes/No |
| Simplified taxation elected (簡易課税) | Yes/No |
| Accounting method | Tax-inclusive (税込) or tax-exclusive (税抜) |

**Computation Route Determination**

| Condition | Route |
| --- | --- |
| Invoice registrant + 20% special measure elected | 2割特例 route |
| Simplified taxation elected + base sales ≤ JPY 50M | 簡易課税 route |
| All other cases | 本則課税 (general) route |

### 7.2 Sales Entry

Enter total sales broken down by:
- Taxable sales amount (tax-inclusive total)
- Reduced rate (8%) portion (軽減税率適用分)
- Tax-exempt sales (免税売上)
- Non-taxable sales (非課税売上)
- Returns/allowances by rate category

### 7.3 Calculation Result (計算結果)

**Calculation Result**

| Item | Description |
| --- | --- |
| Taxable base amount (課税標準額) | Sales ÷ 1.10 (or 1.08), rounded down to JPY 1,000 |
| National consumption tax (消費税額) | Base × 7.8% (standard) or 6.24% (reduced) |
| Input tax credit (控除税額) | Varies by method |
| Differential tax (差引税額) | Output tax − input tax credit, rounded down to JPY 100 |
| Local consumption tax (地方消費税) | Differential × 22/78, rounded down to JPY 100 |
| Total tax due (合計納付税額) | National + local |

### 7.4 Taxpayer Information

Enter address, tax office, name, My Number, and payment method for the consumption tax return.

## Section 8 -- Electronic Signature and Submission

### 8.1 Save Input Data (Strongly Recommended)

Before submitting, save input data as a `.data` file using the "Save input data" (入力データの一時保存) button. This file allows you to:
- Resume filing if interrupted
- Reference data for next year's return
- Restore data if a correction filing (修正申告) is needed

### 8.2 Electronic Signature

Sign the return electronically using your My Number Card:
1. Enter your signature PIN (署名用パスワード -- 6-16 alphanumeric characters)
2. Hold your My Number Card to the smartphone's NFC reader
3. Wait for confirmation

### 8.3 Submission

**Review the final confirmation page carefully before submitting.**

After confirming all figures are correct, click the submit button. Record the receipt number (受付番号) displayed after successful submission.

### 8.4 Post-Submission

1. **Save the post-submission `.data` file** -- it contains the receipt number and submission timestamp
2. **Check your e-Tax message box** for the receipt notification (受信通知)
3. **If consumption tax return is pending**, proceed to file it after the income tax submission
4. **Note payment deadlines:** Income tax by March 15, consumption tax by March 31

## Section 9 -- Common Errors and Troubleshooting

**Common Errors and Troubleshooting**

| Error Code | Description | Resolution |
| --- | --- | --- |
| KS-E10089 | e-Tax submission required for JPY 650,000 deduction | Must submit electronically, not on paper |
| KS-E10001 | Required field missing | Check all mandatory fields are filled |
| KS-E40003 | Balance sheet does not balance | Verify total assets = total liabilities + equity |
| KS-W10035 | Print confirmation | Acknowledge with OK to proceed |
| KS-W90011 | Data will be reset | Acknowledge with OK if intentional |

### QR Code Not Displaying

If the QR code does not appear on the authentication screen:
- Ensure you are using a supported browser (Chrome/Edge on Windows, Safari on macOS)
- Linux is not officially supported by the NTA
- Try refreshing the page

### Authentication Failures

- Ensure the My Number Card is not expired
- Check that the correct PIN is being used (4-digit user authentication PIN, not the 6-16 digit signature PIN)
- Hold the card steady against the phone's NFC reader for several seconds

## Section 10 -- Key Deadlines and Calendar

**Key Deadlines and Calendar**

| Item | Deadline | Notes |
| --- | --- | --- |
| Income tax filing | March 15 | 確定申告 deadline |
| Income tax payment | March 15 | Same as filing |
| Consumption tax filing | March 31 | Sole proprietors |
| Consumption tax payment | March 31 | Same as filing |
| Account transfer (振替納税) date | Late April (income tax), late April (consumption tax) | Exact date announced annually |
| Estimated tax 1st instalment | July 31 | If prior year tax > JPY 150,000 |
| Estimated tax 2nd instalment | November 30 | If prior year tax > JPY 150,000 |

## Section 11 -- Data File Management

The 確定申告書等作成コーナー allows saving and loading `.data` files at any point during the process.

### The `.data` File

**The `.data` File**

| Action | When to Use |
| --- | --- |
| Save during entry | To create a checkpoint before complex sections |
| Save before submission | To preserve a pre-submission backup |
| Save after submission | To preserve receipt number and submission details |
| Load saved data | To resume from a previous session via "保存データを利用して作成" |

**Best practice:** Save `.data` files at three points: (1) after completing financial statements, (2) before electronic submission, and (3) after successful submission.

## PROHIBITIONS

- **Prohibitions list** — NEVER submit a tax return without the taxpayer's explicit confirmation of all figures; NEVER enter the electronic signature PIN -- this must be done by the taxpayer personally; NEVER click the final submission button -- this must be done by the taxpayer personally; NEVER select the JPY 650,000 blue return deduction for paper filing (will cause error KS-E10089); NEVER skip the balance sheet balance check -- assets must equal liabilities + equity; NEVER proceed past the QR code authentication step without confirmation that authentication succeeded; NEVER present e-Tax filing as a substitute for professional review -- all returns should be reviewed by a 税理士

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a 税理士 or equivalent licensed practitioner in Japan) before filing or acting upon.

The 確定申告書等作成コーナー screen layout and form fields are maintained by the National Tax Agency and may change without notice. Always verify against the live system.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

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

## Section 4 -- Step-by-Step Filing Workflow

0. **Prerequisite step: income tax calculations** — Use jp-income-tax skill to compute all figures before starting e-Tax filing
0. **Prerequisite step: consumption tax calculations** — Use jp-consumption-tax skill to compute consumption tax figures if applicable
0. **Submission Method Selection** — Select submission method (My Number Card + smartphone or IC card reader)

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
