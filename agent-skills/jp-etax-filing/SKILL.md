---
name: jp-etax-filing
description: "Use this skill whenever asked about filing a Japanese tax return electronically via e-Tax (確定申告書等作成コーナー). Trigger on phrases like \"e-Tax\", \"電子申告\", \"e-Tax filing\", \"確定申告書等作成コーナー\", \"how to file taxes in Japan online\", \"e-Tax submission\", \"マイナンバーカード認証\", \"QR code authentication e-Tax\", \"blue return financial statements\", \"決算書入力\", \"所得税申告書\", \"consumption tax return filing\", \"消費税申告書作成\", or any question about the step-by-step process of filing income tax or consumption tax returns electronically in Japan. This skill covers the complete e-Tax workflow: authentication, financial statement entry (決算書), income tax return entry (申告書B), consumption tax return entry, and electronic submission. ALWAYS read this skill before assisting with any Japan e-Tax filing work."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/jp-etax-filing"
  jurisdiction: "JP"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Japan e-Tax filing v1.1

> **General reference only.** This skill prepares AI-assisted working papers. A qualified 税理士 must review the facts, elections, computations and current forms before filing, paying or taking a tax position.

> Based on work by [Kazuki Nagata (@kazukinagata)](https://github.com/kazukinagata/shinkoku), licensed under MIT. Adapted for the OpenAccountants format.

## Scope

Guide the taxpayer/reviewer through electronic individual business-income and consumption-tax return preparation, saved data, signature, receipt and payment. This is 2026 workflow readiness, using final 2025 forms in the 2025-2026 filing cycle for screen orientation. Do not enter 2026 figures in a 2025 return. Current 2026 law must come from the computation skills; screens and form numbers can change. Contributor: Open Accountants Community.

### Quick reference

| Item | Condition/value | Official source |
|---|---|---|
| Start portal | `確定申告書等作成コーナー`; choose `決算書・収支内訳書(＋所得税)` for business statements followed by income tax | [e-Tax selection FAQ](https://www.e-tax.nta.go.jp/toiawase/faq/gaiyo/07.htm) |
| Blue-return special deduction | JPY 550,000 (source: 55万円) requires eligible business, regular books, statements and timely return; JPY 650,000 (source: 65万円) additionally timely e-Tax return/statements OR qualifying excellent electronic books plus required notice; other eligible blue filers up to JPY 100,000 (source: 10万円), limited by relevant positive income | [Special Measures Act art.25-2; NTA 2072](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/2072.htm) |
| Authentication PINs, taxpayer enters personally | User authentication 4 numeric digits; signature 6-16 alphanumeric characters | [NTA e-Tax PIN FAQ](https://www.e-tax.nta.go.jp/toiawase/faq/zizen/10.htm) |
| Calendar 2026 income tax final due/debit | 2027-03-15 /2027-04-23 if valid transfer arrangement | [NTA tax calendar](https://www.nta.go.jp/taxes/nozei/nofu/24200042/noufu_kigen.htm) |
| Calendar 2026 individual JCT final due/debit | 2027-03-31 /2027-04-30 if valid transfer arrangement | [NTA tax calendar](https://www.nta.go.jp/taxes/nozei/nofu/24200042/noufu_kigen.htm) |
| Final 2025 return,2025-2026 filing cycle | Income tax due 2026-03-16, debit 2026-04-23; JCT due 2026-03-31, debit 2026-04-30 | [NTA tax calendar](https://www.nta.go.jp/taxes/nozei/nofu/24200042/noufu_kigen.htm) |
|2026 estimated-tax notice calendar | First period 2026-07-31; second 2026-11-30; use assessed notice and `jp-estimated-tax`, not prior final balance alone | [NTA tax calendar](https://www.nta.go.jp/taxes/nozei/nofu/24200042/noufu_kigen.htm) |
| Consumer-app/convenience payment in opened 2025 JCT manual | Total tax <=JPY 300,000 (source: 30万円); options disappear above that amount; app option not offered for paper submissions | [NTA manual payment section](https://www.nta.go.jp/taxes/shiraberu/shinkoku/tebiki/2025/kisairei/pdf/0023010-154_04.pdf) |

## Ask the client first

- Exact return year, return type, blue approval and filing history.
- Reviewed computation, financial statements, expense/asset and withholding/deduction schedules.
- Consumption-tax status, method/election proof and gross/net classification schedules.
- Taxpayer's available My Number Card/smartphone/card-reader or existing supported alternate method.
- Tax office/address, name/kana/trade name, own refund account and chosen payment method.
- Unresolved discrepancies, missing attachments and explicit confirmation of final figures.

## The method, step by step

1. Load `jp-income-tax`, `jp-consumption-tax`, `jp-return-assembly`. Obtain reviewed financial statements, income/credit schedules and JCT workpaper first. At [the official portal](https://www.keisan.nta.go.jp/) choose the actual tax year, new preparation or saved data, and submission method supported by that year's system. Never automatically answer Yes to card/smartphone questions.
2. Select `決算書・収支内訳書(＋所得税)`, then `青色申告決算書`, `収支内訳書`, or eligible elected `青色申告決算書（現金主義用）`. The official FAQ confirms statements can lead into income-tax preparation. [NTA e-Tax FAQ](https://www.e-tax.nta.go.jp/toiawase/faq/gaiyo/07.htm).
3. My Number Portal linkage is optional: ask whether configured and desired, review imported certificates and remove duplicates. Read displayed terms, then taxpayer accepts them and authenticates personally. For a QR flow the taxpayer scans using the official app/card and enters the appropriate PIN; never collect, store, infer or type it. Check live environment guidance rather than assuming a browser/OS is supported.
4. Enter statement period, monthly sales/purchases, personal consumption and miscellaneous receipts, opening/closing inventory and cost of goods sold. Enter expenses by Japanese label:租税公課,荷造運賃,水道光熱費,旅費交通費,通信費,広告宣伝費,接待交際費,損害保険料,修繕費,消耗品費,減価償却費,福利厚生費,給料賃金,外注工賃,利子割引料,地代家賃,貸倒金,任意科目/税理士等報酬 and雑費. Use dedicated depreciation, payroll, interest and rent subforms where displayed. Expense labels and statement structure are read from the final 2025 general blue form; do not assume the old expense-line numbering is correct. [NTA blue form](https://www.nta.go.jp/taxes/shiraberu/shinkoku/yoshiki/01/shinkokusho/pdf/r07/10.pdf).
5. Check pre-deduction income, approved blue deduction and resulting business income. Paper filing can still support JPY 650,000 under the excellent-electronic-books route when all notice/other conditions hold; do not automatically reduce every paper filer. Enter opening/closing balance sheets with cash/deposits, receivables, inventory, prepayments, property/equipment/vehicles/tools, land and custom accounts; payables, loans, accruals, deposits, allowance,元入金 and事業主借. `事業主貸` is on the asset side, not liabilities/equity. Reconcile balance using the form including pre-deduction income. [NTA 2072](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/2072.htm), [NTA blue form](https://www.nta.go.jp/taxes/shiraberu/shinkoku/yoshiki/01/shinkokusho/pdf/r07/10.pdf).
6. Enter the 12-digit individual My Number only through the authorised filing screen when required, distinguish it from the e-Tax identification number and corporate number, and never store PINs. [NTA identity-verification guide, individual-number definition](https://www.nta.go.jp/taxes/tetsuzuki/mynumberinfo/pdf/kakunin.pdf). Enter postal/residential and business addresses, tax office, kanji/kana name, occupation,屋号, contact and filing date. Continue to income-tax return. Select all actual income categories: employment, business/commercial, agriculture only if separately supported, rental, miscellaneous/business-other including crypto, pension, retirement, stocks/dividends and temporary income. Business income can transfer from statements, but verify the amount. Enter employment from源泉徴収票, miscellaneous receipts/expenses/payer details, and all independently prepared schedules. No automatic business-income classification solely from occupation or opening notice.
7. Enter certificate-supported social insurance, mutual aid/iDeCo, life/earthquake insurance, casualty losses, medical expenses and donations; spouse/dependents, widow/single parent, student, disability, basic deduction, housing loan, estimated tax and eligible loss carryforward. Never reuse a fixed basic deduction:2025 and 2026 reforms differ. Import exact eligibility and computed values from `jp-income-tax`; do not let an old saved default override them. [NTA 1199](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1199.htm).
8. On calculation confirmation reconcile total income, deductions, taxable income, computed income tax, tax credits, reconstruction tax, withholding, estimated-tax credits and final due/refund against the working paper. Investigate every discrepancy before submission. Select payment method: authorised account transfer, direct payment/internet banking, credit card with displayed fee, eligible app/convenience payment or bank counter; taxpayer performs payment. For refund use the taxpayer's eligible bank details. Resident-tax settings need the taxpayer's actual facts, not a default.
9. Prepare a separate consumption-tax return when applicable. On `一般課税・簡易課税の条件判定等`, enter base-period sales, invoice registration, mid-year taxable start, eligible 2割 choice, simplified election and gross/net books. On `所得区分の選択` select all relevant activities; enter `売上（収入）金額（雑収入を含む）`, expand export/exempt/outside-scope deductions, reduced-rate portion, returns, bad debts and recoveries, then `中間納付税額等`, `計算結果の確認` and `納税地等入力`. For the 2025 form base period is 2023; for 2026 use the appropriate 2024 facts on the 2026 form. Input only taxable-period transactions after registration if liability starts midyear. Some statement carry-forward is unavailable for simplified method/midyear starts: reconcile manually. [NTA JCT screen manual,2025-2026 cycle](https://www.nta.go.jp/taxes/shiraberu/shinkoku/tebiki/2025/kisairei/pdf/0023010-154_04.pdf).
10. Save resumable input data after statements and before sending, then review PDF/forms/attachments and actual year. Taxpayer gives explicit confirmation of figures, electronically signs and clicks the final submission personally. The taxpayer retains card/PIN control at all times. If interrupted, preserve data and resume via the offered saved-data route; do not treat a saved draft as filed.
11. After each return, retain the sent return/PDF and electronic data plus receipt. Open e-Tax message box `受信通知`; check name, tax office, tax type, year, receipt date/time and number. Receipt proves arrival, not payment or substantive acceptance. A `.data` file alone is insufficient evidence of arrival. Archive receipts before expiry. Finish any separate JCT return and payment workflow, and retain confirmations. [NTA receipt FAQ](https://www.e-tax.nta.go.jp/toiawase/qa/yokuaru01/13.htm).

## Boundary and exception table

| Event | Action |
|---|---|
| QR missing or authentication failure | Stop at authentication; inspect current supported environment, card validity and displayed help. Taxpayer handles PIN/reset; do not retry blindly or bypass controls |
| Balance-sheet mismatch | Reconcile underlying accounts and drawings/contributions; never force a balancing expense |
| Required field missing or intentional-reset warning | Identify the actual displayed message, preserve checkpoint, correct evidence or cancel reset; never acknowledge blindly |
| Different deduction result | Test timely filing, bookkeeping, statements, electronic route and income cap; do not infer a legal error solely from a historic error code |
| Consumer-app/convenience limit or bank transfer not arranged | Choose a genuinely available method and independently confirm payment deadline and transfer eligibility |
| Corrected return | Preserve original data/receipt and refer amended-return/reassessment procedure; do not overwrite filing evidence |

## Worked cases

Case 1, e-Tax data reconciliation: hypothetical balance sheet assets JPY 4,200,000, liabilities JPY 1,100,000, opening capital JPY 2,000,000, business profit JPY 1,500,000, owner's contributions JPY 100,000 and drawings JPY 500,000. Closing balancing equity is JPY 3,100,000; imbalance JPY 0. Drawings reduce equity for this reconciliation and appear as asset-side事業主貸 on the form. The computation tests the accounting identity, not a tax rate.

```oa-check
name: Blue statement balance reconciliation before send
inputs:
  assets: 4200000
  liabilities: 1100000
  capital: 2000000
  profit: 1500000
  contributions: 100000
  drawings: 500000
steps:
  equity: capital + profit + contributions - drawings
  imbalance: assets - liabilities - equity
expected:
  equity: 3100000
  imbalance: 0
```

Case 2, transfer from JCT computation: confirmed standard-rate gross sales JPY 11,000,000, eligible invoice purchases JPY 2,200,000, national interim JPY 156,000 and local interim JPY 44,000. National annual balance JPY 624,000, local JPY 176,000; residual national JPY 468,000, local JPY 132,000, total JPY 600,000. Match both interim fields before submission. [NTA 6351](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6351.htm), [NTA 6609](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6609.htm).

```oa-check
name: Separate national and local interim fields
inputs:
  gross_sales: 11000000
  gross_purchases: 2200000
  national_interim: 156000
  local_interim: 44000
steps:
  national_annual: (gross_sales - gross_purchases) / 1.10 * 0.078
  local_annual: national_annual * 22 / 78
  national_due: national_annual - national_interim
  local_due: local_annual - local_interim
  total_due: national_due + local_due
expected:
  national_due: 468000
  local_due: 132000
  total_due: 600000
```

## When to refuse or refer

Never submit without explicit confirmation, enter taxpayer PINs, click final submission, bypass unsuccessful authentication, omit balance reconciliation or substitute e-Tax for professional review. Refer unsupported schedules, residence/treaty disputes, unresolved election/deduction eligibility and altered live screens whose meaning cannot be established. Work may continue on separable drafts while filing stays blocked.

## Filing and payment

The calendar in Quick reference distinguishes 2026 returns from 2025-2026 filing-cycle returns. Tax submission and payment are separate. Set up chosen payment route before the relevant due date; never promise that a new direct-debit arrangement works immediately. Use the actual transfer notice for dates and maintain sufficient funds. Extensions, departure/death and late returns require separate review. Penalty/interest amounts are not computed by this workflow.

## Completion checklist

Prepared computations; correct year and forms; all statements/schedules; balanced accounts; blue eligibility including electronic-book alternative; deductions and source certificates; national/local interims; final taxpayer confirmation; taxpayer-owned authentication/signature/submission; both returns' receipts; payment/refund route and deadlines; saved input checkpoints and filed data archived. Report incomplete items explicitly.

## Sources

| Source | URL | Read on |
|---|---|---|
| NTA entry: Read for statement-selection flow | https://www.e-tax.nta.go.jp/toiawase/faq/gaiyo/07.htm | 2026-11-14 |
| NTA blueform: Read for all statement pages and expense/balance labels | https://www.nta.go.jp/taxes/shiraberu/shinkoku/yoshiki/01/shinkokusho/pdf/r07/10.pdf | 2026-11-14 |
| NTA blue: Read for 55/65/10 deduction conditions including timely submission and electronic-book alternative | https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/2072.htm | 2026-11-14 |
| NTA auth: Read for authentication/signature PINs and lock warning | https://www.e-tax.nta.go.jp/toiawase/faq/zizen/10.htm | 2026-11-14 |
| NTA basic: Read for 2025/2026 reform and effective-date boundaries | https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1199.htm | 2026-11-14 |
| NTA jctmanual: Read for 2025 condition/sales/interim/payment screens and neighbors | https://www.nta.go.jp/taxes/shiraberu/shinkoku/tebiki/2025/kisairei/pdf/0023010-154_04.pdf | 2026-11-14 |
| NTA 6351: Read for national computation | https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6351.htm | 2026-11-14 |
| NTA 6609: Read for national/local interims | https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6609.htm | 2026-11-14 |
| NTA receipt: Read for receipt fields and archive necessity | https://www.e-tax.nta.go.jp/toiawase/qa/yokuaru01/13.htm | 2026-11-14 |
| NTA dates: Read for 2025 and 2026 due/debit calendar | https://www.nta.go.jp/taxes/nozei/nofu/24200042/noufu_kigen.htm | 2026-11-14 |

| NTA identity guide: Read for individual-number definition and statutory purpose/security limits, printed pages3-6 | https://www.nta.go.jp/taxes/tetsuzuki/mynumberinfo/pdf/kakunin.pdf | 2026-11-14 |

Not yet confirmed: Final 2026 screens/form box numbers and current supported browser/OS list are not checked here. The old screen IDs CC-AA-010,CC-AE-090,CC-AE-600,CC-AA-024,CC-AA-440 and error IDs KS-E10089,KS-E10001,KS-E40003,KS-W10035,KS-W90011 remain unconfirmed historical identifiers, not operative instructions. The keisan 2025 full screen manuals returned 403 to ordinary fetch and a blank ordinary-browser PDF; recovered the statement route from official e-Tax FAQ and form PDF, and JCT route from the official NTA-hosted 2025 manual. Do not infer 2026 availability from these older screens.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `jp-etax-filing` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/jp-etax-filing. If neither is available, confirm every figure against the official source pages cited above before relying on it.
