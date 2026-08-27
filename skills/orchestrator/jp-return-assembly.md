---
name: jp-return-assembly
description: Final orchestrator skill that assembles the complete Japanese filing package for Japan-resident self-employed individuals and sole proprietors (個人事業主). Consumes outputs from all Japanese content skills (japan-consumption-tax for 消費税, japan-income-tax for 所得税確定申告, japan-social-insurance for 社会保険料, jp-estimated-tax for 予定納税) to produce a single unified reviewer package containing every worksheet, every form, every brief section, all cross-skill reconciliations, and the final action list with payment instructions, filing instructions, and next-year planning. This is the capstone skill that runs last and produces the final deliverable. MUST be loaded alongside all Japanese content skills listed above. Japan full-year residents only. Self-employed individuals and sole proprietors (個人事業主) only.
version: 1.0
jurisdiction: JP
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
category: orchestrator
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# JP Return Assembly

## Japan Return Assembly Skill v1.0

## CRITICAL EXECUTION DIRECTIVE -- READ FIRST

When this skill is invoked, you have already passed through intake. The user has consented to the full workflow. Execute all steps without pausing for permission.

Specifically:

- Do NOT ask the user "how deep do you want me to go" or "do you want the full package" or any variant. The user asked for their tax returns. They want their tax returns. Produce them.
- Do NOT announce how many tokens or tool calls this will take. Execute.
- Do NOT ask which deliverables to prioritise. Produce all deliverables listed in Section 4. If you run out of context mid-execution, finish the computation work first (numbers, positions, flags) then produce whatever formatted outputs you can, and at the very end state clearly which deliverables were not produced and why.
- Do NOT re-validate scope that intake already validated. If `jp-freelance-intake` produced an intake package, trust it. You can cross-check specific numbers during reconciliation but do not re-interrogate the user about residency, business structure, or anything else intake already captured.
- Do NOT pause between content skills to check in. Run them in dependency order (Section 2) without prose status updates between each one. A single status message at the end is fine.
- Self-checks are targets, not blockers. If a self-check fails, note it in the reviewer brief's open flags section and continue. Do NOT halt the entire workflow because one self-check had an ambiguous answer.
- Primary source citations go in the final reviewer brief, not in intermediate computation steps.

The user has already been told (by the intake skill) that the final package requires 税理士 signoff before filing. State it once in the final output and move on.

Failure mode to avoid: The skill halts mid-execution and asks the user a meta-question about workflow pacing. If you feel the urge to ask "how should I proceed," the correct action is to pick the most defensible path and proceed, flagging the decision in the reviewer brief so the reviewer can challenge it.

## What this file is

The final capstone skill for Japanese self-employed returns. Every Japanese content skill feeds into this one. The output is the complete reviewer package that a 税理士 (zeirishi) can review, sign off on, and deliver to the client along with filing instructions.

This skill coordinates execution of the content skills, verifies cross-skill consistency, and assembles the final deliverable.

## Section 1 -- Scope

Produces the complete Japanese filing package for:
- Full-year Japan residents
- Self-employed individuals and sole proprietors (個人事業主)
- Tax year 2025 (令和7年分)
- Filing 所得税確定申告書 (income tax return), 消費税確定申告書 (consumption tax return if applicable), 青色申告決算書 or 収支内訳書, social insurance reconciliation, estimated tax schedule

## Section 2 -- Execution order and dependency chain

The skill enforces the following execution order:

If any upstream content skill fails to produce validated output, the assembly skill notes the failure in the reviewer brief and continues with available data rather than halting entirely.

0. **japan-consumption-tax step** — 消費税確定申告書 (consumption tax return). Runs first because consumption tax figures affect income tax computation (consumption tax paid is a deductible expense for income tax if using tax-inclusive accounting, or a reconciliation item if using tax-exclusive). Determine method: 本則課税 (standard), 簡易課税 (simplified), or 2割特例 (20% special provision). For 本則課税: compute 課税売上 (taxable sales), 課税仕入れ (taxable purchases), 仕入税額控除 (input tax credit). For 簡易課税: apply みなし仕入率 (deemed purchase rate) by 事業区分 (business category: 第1種~第6種, e.g., services = 第5種 at 50%). For 2割特例: tax = 売上消費税 x 20% (available through 令和8年9月30日を含む課税期間). Verify eligibility for chosen method. Output: 消費税額 due, method used, form values.
0. **japan-income-tax step** — 所得税確定申告書 with 青色申告決算書 or 収支内訳書. Depends on consumption tax: if 税込経理 (tax-inclusive accounting), consumption tax paid is an expense (租税公課); if 税抜経理 (tax-exclusive), no impact on income but reconciliation needed. Compute 売上 (revenue), 売上原価 (COGS if applicable), 経費 (expenses by category), 差引金額 (net income before adjustments). Apply 青色申告特別控除 (blue return special deduction): ¥650,000 (e-Tax + double-entry), ¥550,000 (double-entry paper), ¥100,000 (simplified). Compute 事業所得 (business income). Add other income categories if applicable. Apply 所得控除 (income deductions): 基礎控除 ¥480,000, 社会保険料控除, 小規模企業共済等掛金控除, 生命保険料控除, 地震保険料控除, 配偶者控除/特別控除, 扶養控除, 医療費控除, 寄附金控除 (ふるさと納税), etc. Compute 課税所得 (taxable income). Apply 所得税率 (progressive rates): 5% up to ¥1,950,000; 10% up to ¥3,300,000; 20% up to ¥6,950,000; 23% up to ¥9,000,000; 33% up to ¥18,000,000; 40% up to ¥40,000,000; 45% above. Apply 復興特別所得税 (reconstruction special income tax): 2.1% of income tax. Apply 配当控除 (dividend credit) if applicable. Apply 住宅借入金等特別控除 (housing loan deduction) if applicable. Credit 源泉徴収税額 (withholding tax) and 予定納税額 (estimated tax paid). Output: 申告納税額 (tax payable) or 還付金 (refund), all form line values.
0. **japan-social-insurance step** — 社会保険料 reconciliation. Depends on income tax: social insurance premiums paid enter 社会保険料控除 on the income tax return. 国民健康保険 (National Health Insurance): premiums vary by municipality, based on prior year income. Verify amount paid matches expected. 国民年金 (National Pension): fixed monthly amount (¥16,980 for 2025). Verify 12 months paid or note any 免除 (exemption) periods. 小規模企業共済 (Small Enterprise Mutual Aid): entered under 小規模企業共済等掛金控除 (separate from 社会保険料控除). iDeCo: also entered under 小規模企業共済等掛金控除. Output: total deduction amounts by category, payments verified.
0. **jp-estimated-tax step** — 予定納税 and forward-looking schedule. Depends on income tax: 2026 予定納税 is based on 2025 申告納税額. If 2025 申告納税額 ≥ ¥150,000: 予定納税 applies for 2026. Each instalment = 申告納税額 / 3 (rounded down to nearest ¥100). 1st period: July 1-31, 2026. 2nd period: November 1-30, 2026. 減額申請 (reduction request) available if income is expected to decrease significantly. Output: instalment amounts and dates for 2026.

## Section 3 -- Cross-skill reconciliation

### Cross-check 1: Revenue consistency across consumption tax and income tax

**Cross-check 1 table**  _(Must match within ¥1)_

| Consumption Tax Output | Income Tax Input | Rule |
| --- | --- | --- |
| 課税売上高 (taxable sales, tax-excluded) | 青色申告決算書 売上(収入)金額 (revenue) | Must match within ¥1 |
| If 税込経理: 売上 includes consumption tax | 決算書 売上 = tax-inclusive amount | Consumption tax paid recorded as 租税公課 expense |
| If 税抜経理: 売上 excludes consumption tax | 決算書 売上 = tax-exclusive amount | No consumption tax in revenue or expense lines |
| Export sales (輸出免税) | Included in income but zero-rated for consumption tax | Reconcile total vs taxable |

- **Mismatch handling** — Flag for reviewer. Common causes: timing differences (発生主義 accrual vs 現金主義 cash basis), 非課税売上 (non-taxable sales), free sample/promotional items.  _(Cross-check 1)_

### Cross-check 2: Business income vs miscellaneous income classification (事業所得 vs 雑所得)

**Cross-check 2 table**  _(Cross-check 2)_

| Factor | 事業所得 (Business Income) | 雑所得 (Miscellaneous Income) |
| --- | --- | --- |
| 開業届 filed | Yes | Typically no |
| Continuity and scale | Regular, ongoing activity | Sporadic, side activity |
| 青色申告 | Available | Not available |
| Loss offset (損益通算) | Yes -- offsets against other income | No -- cannot offset losses |
| 繰越損失 (loss carryforward) | Up to 3 years (blue return) | Not available |

- **NTA guidance** — 令和4年通達改正: If revenue < ¥3M and no dedicated bookkeeping, the NTA may reclassify as 雑所得. If the user has 開業届 + blue return + proper books, 事業所得 is defensible. Flag if borderline.  _(令和4年通達改正)_

### Cross-check 3: 青色申告特別控除 level verification

**Cross-check 3 table**  _(Cross-check 3)_

| Requirement | ¥650,000 | ¥550,000 | ¥100,000 |
| --- | --- | --- | --- |
| Double-entry bookkeeping (複式簿記) | Required | Required | Not required |
| e-Tax filing OR 電子帳簿保存 | Required (either one) | Not required | Not required |
| 貸借対照表 + 損益計算書 submitted | Required | Required | Not required |

- **Reduction rules** — If the user claims ¥650,000 but files on paper: Reduce to ¥550,000. Flag. If the user claims ¥550,000 but uses simplified bookkeeping: Reduce to ¥100,000. Flag.  _(Cross-check 3)_

### Cross-check 4: Social insurance deductions match payments

**Cross-check 4 table**  _(Cross-check 4)_

| Deduction Claimed | Verification Source | Rule |
| --- | --- | --- |
| 社会保険料控除 (国民健康保険) | Municipality payment notice / bank debits | Amount claimed = amount actually paid in calendar year 2025 |
| 社会保険料控除 (国民年金) | 国民年金控除証明書 from 日本年金機構 | Certificate amount = claimed amount |
| 小規模企業共済等掛金控除 | 控除証明書 from 中小企業基盤整備機構 / 国民年金基金連合会 | Certificate amount = claimed amount |

- **Mismatch handling** — Deduction cannot exceed actual amount paid and certified. Only amounts paid during calendar year 2025 qualify (not amounts due but unpaid).  _(Cross-check 4)_

### Cross-check 5: 源泉徴収 (withholding) reconciliation

**Cross-check 5 table**  _(所得税法第204条)_

| Withholding Claimed | Verification Source | Rule |
| --- | --- | --- |
| 源泉徴収税額 on 確定申告書 | 源泉徴収票 / 支払調書 from payers | Total must match sum of all certificates |
| Rate applied | Payment type per 所得税法第204条 | 10.21% on first ¥1M, 20.42% above for most professional services |

- **Excess withholding** — If withholding exceeds tax liability: Refund (還付) results. Verify all 源泉徴収票 are included.  _(Cross-check 5)_

### Cross-check 6: Consumption tax method eligibility

**Cross-check 6 table**  _(Cross-check 6)_

| Method | Eligibility | Verification |
| --- | --- | --- |
| 本則課税 (standard) | Always available | Default if no 届出書 filed |
| 簡易課税 (simplified) | Base period revenue ≤ ¥50M AND 届出書 filed by prior year-end | Verify 届出書 filing date and base period revenue |
| 2割特例 (20% special) | Was 免税事業者 in base period AND registered for インボイス | Verify base period status |

- **Method reversion rules** — If 簡易課税 claimed but base period > ¥50M: Cannot use. Revert to 本則課税. Flag. If 2割特例 claimed but was already 課税事業者 in base period: Cannot use. Flag.  _(Cross-check 6)_

## Section 4 -- Final reviewer package contents

### Documents

1. Executive summary -- one-page overview: filing status, income, tax liability, consumption tax, social insurance, 予定納税, refund or balance due
2. 消費税 worksheet -- method determination, computation, form values (消費税確定申告書 + 付表)
3. 所得税 worksheet -- 確定申告書B line-by-line with supporting 青色申告決算書 (損益計算書 + 貸借対照表) or 収支内訳書
4. 減価償却 schedule -- asset register with 取得価額, 取得日, 耐用年数, 償却方法, 当期償却額, 期末帳簿価額
5. 社会保険料 reconciliation -- premiums paid, deduction amounts, certificate verification
6. 予定納税 schedule -- 2026 instalment calculation
7. Cross-skill reconciliation summary -- all six cross-checks with pass/fail and notes
8. Reviewer brief -- comprehensive narrative with positions, citations, flags, self-check results
9. Client action list -- what the client needs to do, with dates and amounts

### Reviewer brief contents

# Complete Return Package: [Client Name] -- 令和7年分 (Tax Year 2025)

## Executive Summary
- Filing status: [Single / Married with 配偶者控除 / etc.]
- Residence: Japan (full-year)
- Business: 個人事業主 (sole proprietor)
- Return type: 青色申告 / 白色申告
- 青色申告特別控除: ¥650,000 / ¥550,000 / ¥100,000
- Filing method: e-Tax / paper
- 適格請求書発行事業者: Yes (T-number) / No
- 売上 (revenue, tax-excluded): ¥X
- 事業所得 (business income after blue deduction): ¥X
- 課税所得 (taxable income after all deductions): ¥X
- 所得税額 (income tax): ¥X
- 復興特別所得税 (reconstruction tax at 2.1%): ¥X
- 源泉徴収税額 credited: ¥X
- 予定納税額 credited: ¥X
- 申告納税額 / 還付金 (tax due / refund): ¥X
- 消費税額 (consumption tax due): ¥X
- 住民税 estimated (for reference): ¥X

## Consumption Tax Return (消費税確定申告書)
[Content from japan-consumption-tax output]
- Method: 本則課税 / 簡易課税 / 2割特例
- Eligibility verification for chosen method
- 課税売上高 (taxable sales): ¥X
- 課税仕入高 (taxable purchases, if 本則): ¥X
- For 本則課税:
  - 消費税額 on sales: ¥X
  - 仕入税額控除 (input tax credit): ¥X
  - 消費税 due: ¥X
  - 地方消費税 (local consumption tax): ¥X
- For 簡易課税:
  - 事業区分 (business category): 第X種
  - みなし仕入率 (deemed purchase rate): X%
  - 消費税 due: ¥X
  - 地方消費税: ¥X
- For 2割特例:
  - 売上消費税 x 20% = ¥X
  - 地方消費税: ¥X
- Comparison of all eligible methods (if multiple eligible)
- Tax paid with return vs instalments (中間納付 if applicable)

## Income Tax Return (所得税確定申告書B)
[Content from japan-income-tax output]
### 青色申告決算書 / 収支内訳書:
- 売上(収入)金額: ¥X
- 売上原価 (COGS): ¥X (if applicable)
- 差引金額 (gross profit): ¥X
- 経費 by category:
  - 租税公課 (taxes and dues): ¥X
  - 荷造運賃 (packing/shipping): ¥X
  - 水道光熱費 (utilities): ¥X
  - 旅費交通費 (travel): ¥X
  - 通信費 (communications): ¥X
  - 広告宣伝費 (advertising): ¥X
  - 接待交際費 (entertainment): ¥X
  - 損害保険料 (insurance): ¥X
  - 修繕費 (repairs): ¥X
  - 消耗品費 (supplies): ¥X
  - 減価償却費 (depreciation): ¥X
  - 福利厚生費 (welfare): ¥X
  - 地代家賃 (rent): ¥X
  - 外注費 (subcontracting): ¥X
  - 雑費 (miscellaneous): ¥X
- 差引金額 (net income before blue deduction): ¥X
- 青色申告特別控除: ¥X
- 事業所得: ¥X

### 確定申告書B:
- 収入金額 (income amounts by category)
- 所得金額 (income after category-specific deductions)
- 所得控除 (income deductions):
  - 社会保険料控除: ¥X
  - 小規模企業共済等掛金控除: ¥X
  - 生命保険料控除: ¥X (一般 + 介護医療 + 個人年金, max ¥120,000 total)
  - 地震保険料控除: ¥X (max ¥50,000)
  - 配偶者控除 / 配偶者特別控除: ¥X
  - 扶養控除: ¥X
  - 基礎控除: ¥480,000 (if 合計所得 ≤ ¥24M)
  - 医療費控除: ¥X
  - 寄附金控除 (ふるさと納税): ¥X
- 課税所得金額: ¥X
- Tax computation (progressive rates applied)
- 復興特別所得税 (2.1% of income tax)
- 税額控除 (tax credits): 配当控除, 住宅ローン控除, etc.
- 源泉徴収税額: ¥X (credited)
- 予定納税額: ¥X (credited)
- 申告納税額 or 還付金: ¥X

## Depreciation Schedule (減価償却費の計算)
- Asset-by-asset detail:
  - 資産名 (asset name)
  - 取得年月 (acquisition date)
  - 取得価額 (acquisition cost)
  - 耐用年数 (useful life per 耐用年数省令)
  - 償却方法 (method: 定額法 straight-line / 定率法 declining-balance)
  - 本年分の償却費 (current year depreciation)
  - 期末未償却残高 (year-end book value)
- 少額減価償却資産の特例 (immediate expensing for items < ¥300,000, blue return only, ¥3M annual cap per 租税特別措置法第28条の2)
- 一括償却資産 (3-year straight-line for items ¥100,000-¥199,999)

## Social Insurance Reconciliation
[Content from japan-social-insurance output]
- 国民健康保険:
  - Municipality: [name]
  - Annual premium paid: ¥X
  - Calculation basis (prior year income, 所得割 + 均等割 + 平等割)
  - Payment verified against certificates / bank
- 国民年金:
  - Monthly amount: ¥16,980 x months paid
  - Total: ¥X
  - 控除証明書 verified
  - Any 免除/猶予 (exemption/deferral) periods noted
- 小規模企業共済:
  - Monthly contribution: ¥X
  - Annual total: ¥X
  - 控除証明書 verified
- iDeCo (if applicable):
  - Monthly contribution: ¥X
  - Annual total: ¥X

## Estimated Tax (予定納税) for 2026
[Content from jp-estimated-tax output]
- Based on 2025 申告納税額: ¥X
- If ≥ ¥150,000: 予定納税 applies
- 1st period (第1期): ¥X -- due July 1-31, 2026
- 2nd period (第2期): ¥X -- due November 1-30, 2026
- 減額申請 option: available if 2026 income expected to decrease (deadline: July 15 for 1st period, November 15 for both)
- 振替納税 (automatic bank transfer) recommended -- debit date typically ~1 month after deadline

## Cross-skill Reconciliation
- Revenue: consumption tax vs income tax: [pass/fail]
- Business income vs miscellaneous income classification: [pass/fail]
- 青色申告特別控除 level justified: [pass/fail]
- Social insurance deductions vs certificates: [pass/fail]
- 源泉徴収 reconciliation: [pass/fail]
- Consumption tax method eligibility: [pass/fail]

## Reviewer Attention Flags
[Aggregated from all upstream skills]
- 事業所得 vs 雑所得 classification borderline cases
- 青色申告特別控除 level (¥650,000 vs ¥550,000 if filing method uncertain)
- Consumption tax method comparison (all eligible methods computed)
- 家事按分 (business/personal split) percentages for home office, vehicle, phone
- 少額減価償却資産 annual ¥3M cap tracking
- インボイス registration implications and 2割特例 sunset (available through 令和8年分)
- Revenue approaching ¥10M consumption tax threshold for future years
- 源泉徴収 amounts and client 支払調書 verification
- 繰越損失 utilisation (if applicable)
- Any 国民年金 未納 (unpaid months)

## Positions Taken
[List with legislation citations]
- e.g., "事業所得 classification maintained -- 開業届 filed, blue return approved, double-entry books maintained per 所得税法第26条"
- e.g., "青色申告特別控除 ¥650,000 applied -- double-entry bookkeeping + e-Tax filing per 租税特別措置法第25条の2第3項"
- e.g., "Home office 家事按分 30% applied -- dedicated room 9㎡ of total 30㎡ per 所得税法第45条, 所得税法施行令第96条"
- e.g., "簡易課税 第5種 50% applied -- サービス業 per 消費税法第37条, base period revenue ¥8.2M ≤ ¥50M threshold"
- e.g., "少額減価償却資産の特例 for MacBook Pro ¥280,000 -- blue return filer, annual total ¥280,000 < ¥3M cap per 租税特別措置法第28条の2"

## Planning Notes for 2026
- 予定納税 schedule (two instalments with amounts and dates)
- 国民健康保険 premium projection (based on 2025 income -- municipality recalculates in June 2026)
- Consumption tax: will base period (2024) revenue require filing? Method choice for 2026
- インボイス 2割特例 availability: still available for 令和8年分 (2026), sunsets after
- 青色申告 bookkeeping requirements for 2026
- 減価償却 continuing assets into 2026 (年末未償却残高 carried forward)
- Any 税制改正 (tax reform) affecting 2026

## Client Action List

### Immediate (確定申告 filing period):
1. Review this return package with your 税理士
2. File 所得税確定申告書 via e-Tax or at 税務署 -- deadline: March 16, 2026 (March 15 falls on Sunday)
3. File 消費税確定申告書 -- deadline: March 31, 2026
4. Pay 所得税 balance due:
   - If 振替納税: automatic debit ~April 22, 2026
   - If direct payment: by March 16, 2026
   - If instalment (延納): 50%+ by March 16, remaining by May 31 (interest: 年0.9% for 2026)
5. Pay 消費税 balance due:
   - If 振替納税: automatic debit ~April 28, 2026
   - If direct payment: by March 31, 2026

### 予定納税 (if applicable):
- 1st period (第1期分): ¥X -- due July 1-31, 2026 (振替納税: ~August 1)
- 2nd period (第2期分): ¥X -- due November 1-30, 2026 (振替納税: ~December 1)
- 減額申請 deadline: July 15 for 1st period, November 15 for both periods

### 住民税 (resident tax, for reference):
- Based on 2025 income, calculated by municipality
- 普通徴収 (self-payment): 4 instalments -- June, August, October, January
- Approximate total: computed from 2025 課税所得 at ~10% (均等割 + 所得割)

### 消費税 中間納付 (if 2025 consumption tax ≥ ¥480,000):
- ¥480,000-¥4M: 1 instalment (半期) -- by August 31, 2026
- ¥4M-¥48M: 3 instalments (quarterly)
- ≥ ¥48M: 11 instalments (monthly)

### Ongoing:
1. Maintain 複式簿記 (double-entry bookkeeping) for blue return eligibility
2. Issue 適格請求書 (qualified invoices) with registration number for all sales (if registered)
3. Retain all 帳簿 and 書類 for 7 years (青色申告 per 所得税法施行規則第63条) or 5 years (白色申告)
4. Track 家事按分 ratios with documentation
5. Monitor 売上 vs ¥10M threshold for future consumption tax obligations
6. File 開業届 if not yet done (for フリーランス without notification)
7. Consider 小規模企業共済 or iDeCo increases for additional deductions
8. Track 少額減価償却資産 running total against ¥3M annual cap

## Section 5 -- Refusals

- **R-JP-A1** — Upstream skill did not run. Name the specific skill. Note: this is a warning, not a hard stop. Continue with available data and flag the gap.  _(Section 5)_
- **R-JP-A2** — Upstream self-check failed. Name the specific check and note it in the reviewer brief. Continue.  _(Section 5)_
- **R-JP-A3** — Cross-skill reconciliation failed. Name the specific reconciliation and describe the discrepancy. Flag for reviewer but continue.  _(Section 5)_
- **R-JP-A4** — Intake incomplete. Specific missing intake items prevent computation. List what is missing and ask the user for the specific data point.  _(Section 5)_
- **R-JP-A5** — Out-of-scope item discovered during assembly. E.g., 不動産の譲渡所得, 山林所得, or complex international tax. Flag and exclude from computation.  _(Section 5)_
- **R-JP-A6** — Classification dispute risk. If the 事業所得 vs 雑所得 boundary is questionable (e.g., low revenue, no 開業届, no proper books), prominently flag in reviewer brief. The 税理士 must confirm the classification is defensible.  _(Section 5)_

## Section 6 -- Self-checks

- **Check JP1** — All upstream skills executed. japan-consumption-tax, japan-income-tax, japan-social-insurance all produced output. jp-estimated-tax produced output or 予定納税 was computed from income tax output.  _(Section 6)_
- **Check JP2** — Revenue matches across consumption tax and income tax. 課税売上高 = 決算書 売上金額 within ¥1 tolerance (adjusting for accounting method: 税込 vs 税抜).  _(Section 6)_
- **Check JP3** — 事業所得 classification is defensible. 開業届 filed, blue return approved (if blue), proper bookkeeping maintained. If any factor is missing, flag.  _(Section 6)_
- **Check JP4** — 青色申告特別控除 level is correct. ¥650,000 only if e-Tax AND double-entry. ¥550,000 only if double-entry. Otherwise ¥100,000 or zero (white return).  _(Section 6)_
- **Check JP5** — Social insurance deductions match certificates. 控除証明書 amounts = claimed deduction amounts. No uncertified amounts claimed.  _(Section 6)_
- **Check JP6** — 源泉徴収 fully credited. All withholding certificates accounted for. Total credited on 確定申告書 = sum of all 源泉徴収票 / 支払調書.  _(Section 6)_
- **Check JP7** — Consumption tax method is eligible. 簡易課税 only if base period ≤ ¥50M and 届出書 filed. 2割特例 only if was 免税事業者 in base period.  _(Section 6)_
- **Check JP8** — 基礎控除 correctly applied. ¥480,000 if 合計所得 ≤ ¥24M. Reduced if ¥24M-¥25M. Zero if > ¥25M.  _(Section 6)_
- **Check JP9** — 復興特別所得税 applied. 2.1% of 所得税 added. This is easy to forget.  _(Section 6)_
- **Check JP10** — 予定納税 correctly credited. Both instalment amounts credited on 確定申告書 第1表 ㊹欄.  _(Section 6)_
- **Check JP11** — Filing calendar is complete. All deadlines for 所得税, 消費税, 予定納税, and 住民税 are listed with specific dates and amounts.  _(Section 6)_
- **Check JP12** — Reviewer brief contains legislation citations. Every position taken references the specific article of 所得税法, 消費税法, or 租税特別措置法.  _(Section 6)_

## Section 7 -- Output files

The final output is three files:

1. `[client_slug]_2025_japan_master.xlsx` -- Single master workbook containing every worksheet and form. Sheets include: Cover, 消費税 (computation + form values), 青色申告決算書 (損益計算書 + 貸借対照表) or 収支内訳書, 確定申告書B (line-by-line), 減価償却 Schedule, 所得控除 Detail, 源泉徴収 Reconciliation, 予定納税 2026, Cross-Check Summary. Use live formulas where possible -- e.g., 確定申告書 事業所得 references the 決算書 net income cell; 社会保険料控除 references the social insurance sheet total. Verify no `#REF!` errors. Verify computed values match the Python/computation model within ¥1 before shipping.

2. `reviewer_brief.md` -- Single markdown file covering all sections from Section 4 above: executive summary, consumption tax, income tax, social insurance, estimated tax, cross-skill reconciliation, flags, positions, planning notes.

3. `client_action_list.md` -- Single markdown file with step-by-step actions: immediate filings and payments, 予定納税 schedule, 住民税 reference, 消費税 中間納付 if applicable, ongoing compliance reminders.

If execution runs out of context mid-build: produce whatever is complete, then state at the end which of the three files were not produced or are partial.

All files are placed in `/mnt/user-data/outputs/` and presented to the user via the `present_files` tool at the end.

## Section 8 -- Cross-skill references

Inputs:
- `jp-freelance-intake` -- structured intake package (JSON)
- `japan-consumption-tax` -- 消費税 computation and form output
- `japan-income-tax` -- 所得税確定申告書 and 決算書 computation output
- `japan-social-insurance` -- 社会保険料 reconciliation output
- `jp-estimated-tax` -- 予定納税 schedule

Outputs: The final reviewer package. No downstream skill.

## Section 9 -- Known gaps

1. PDF form filling is not automated. The reviewer uses the worksheets to fill official NTA forms on e-Tax or print forms.
2. e-Tax filing is handled by the reviewer or client, not by this skill.
3. Payment execution is the client's responsibility; the skill only provides instructions and amounts.
4. 住民税 (resident tax) is computed by the municipality based on the 確定申告 data. This skill provides an estimate for planning but cannot produce the official 住民税 notice.
5. Multi-year 減価償却 tracking assumes the prior year schedule is provided. If not, only current-year acquisitions are depreciated.
6. 山林所得 (forestry income) and 退職所得 (retirement income) are out of scope.
7. Complex 譲渡所得 (capital gains) requiring 分離課税 (separate taxation) -- real estate, stocks outside 特定口座 -- are out of scope.
8. 外国税額控除 (foreign tax credit) is supported at a basic level but complex multi-treaty situations are out of scope.
9. 事業税 (enterprise tax) is computed by the prefecture and is not filed separately. Noted for reference in planning.
10. 消費税 中間申告 (interim consumption tax returns) preparation is out of scope but the obligation and deadlines are noted.
11. The package is complete only for the 2025 tax year (令和7年分); 2026 appears only as prospective planning.

### Change log

v1.0 (May 2026): Initial draft. Modelled on mt-return-assembly v0.1 adapted for Japan jurisdiction with four content skills (consumption tax, income tax, social insurance, estimated tax).

## End of skill

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

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
