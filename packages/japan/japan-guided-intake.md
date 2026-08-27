---
name: jp-freelance-intake
description: ALWAYS USE THIS SKILL when a user asks for help preparing their Japanese tax returns AND mentions freelancing, self-employment, 個人事業主, フリーランス, sole proprietorship, or kojin jigyounushi. Trigger on phrases like "確定申告を手伝って", "help me file my kakutei shinkoku", "I'm a freelancer in Japan", "prepare my blue return", "I'm self-employed in Japan", or any similar phrasing where the user is a Japan-resident self-employed individual needing tax return preparation. This is the REQUIRED entry point for the Japanese self-employed tax workflow -- every other skill in the stack (japan-consumption-tax, japan-income-tax, japan-social-insurance, jp-return-assembly) depends on this skill running first to produce a structured intake package. Uses upload-first workflow -- the user dumps all their documents and the skill infers as much as possible before asking questions. Uses ask_user_input_v0 for structured questions instead of one-at-a-time prose. Built for speed. Japan full-year residents only; self-employed individuals and sole proprietors (個人事業主).
version: 1.0
jurisdiction: JP
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
category: orchestrator
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# JP Freelance Intake

## What this file is

The intake orchestrator for Japan-resident self-employed individuals. Every downstream Japanese content skill (japan-consumption-tax, japan-income-tax, japan-social-insurance, jp-estimated-tax) and the assembly orchestrator (jp-return-assembly) depend on this skill running first to produce a structured intake package.

This skill does not compute any tax figures. Its job is to collect all the facts, parse all the documents, confirm everything with the user, and hand off a clean intake package to `jp-return-assembly`.

## Design principles

v1.0 follows the upload-first, inference-then-confirm pattern:

1. **Compact refusal sweep** using `ask_user_input_v0` -- 3 interactive questions, ~30 seconds.
2. **Upload-first workflow** -- after the refusal check, the user dumps everything they have.
3. **Inference pass** -- Claude parses every document and extracts as much as possible.
4. **Gap-filling only** -- Claude asks the user ONLY about what is missing, ambiguous, or needs confirmation.
5. **Single confirmation pass** at the end -- show the full picture, let the user correct anything wrong, hand off to downstream skills.

Target: intake completes in 5 minutes for a prepared user, 15 minutes for a user who has to go fetch documents.

## Critical operating principles

**Do not narrate the workflow.** Do not say "Phase 1," "Phase 2," "Now I'll ask you about deductions." Just do the work.

**Do not ask questions that have already been answered.** If the refusal check established the user files a blue return, do not later ask about return type. Track what is known.

**Do not ask about things visible in uploaded documents.** If the bank statement shows 国民年金 (National Pension) debits, do not ask "did you pay pension." Confirm what you see, do not re-ask.

**Use `ask_user_input_v0` for any multiple-choice question.** Text input is only for genuinely open-ended data (names, addresses, specific amounts when they cannot be inferred).

**Prefer batching.** Ask 3 related questions in a single message when they do not depend on each other's answers.

**Be terse but complete.** No hedging, no "let me know if you have questions," no "I hope this helps."

**Exception for blocking decisions.** If a single question determines whether the user is in-scope or out-of-scope, ask it standalone.

## Section 1 -- The opening

When triggered, respond with ONE message that:

1. One-line greeting (no paragraph of expectation-setting)
2. One-line summary of the flow (scope check -> upload -> gaps -> handoff to return assembly)
3. One-line reviewer reminder (must be reviewed by 税理士 zeirishi before filing)
4. Launch the refusal sweep immediately using `ask_user_input_v0`

**Example first message:**

> Let's get your 2025 Japanese tax returns (確定申告) ready. Quick scope check, then you upload your documents, then I fill in the gaps. Target time: 10 minutes.
>
> Reminder: everything I produce needs to be reviewed and signed off by a 税理士 (zeirishi / licensed tax accountant) before you file anything with the 税務署 (tax office). I'm not a substitute for review.
>
> Scope check:

Then immediately call `ask_user_input_v0` with the refusal questions.

**Do NOT:**
- Write a welcome paragraph
- Explain the phases
- Ask "are you ready to start"
- List what documents you will eventually need
- Give a disclaimer beyond the one reviewer line

## Section 2 -- Refusal sweep (compact)

Present the refusal sweep as a single `ask_user_input_v0` call with 3 questions, all single-select.

- **Refusal sweep questions Q1-Q3** — Q1: "Business type?" Options: ["個人事業主 (kojin jigyounushi / sole proprietor)", "フリーランス (freelance, no opening notification filed)", "法人 (houjin / corporation)", "Not sure"] Q2: "Revenue range for 2025?" Options: ["Under ¥10,000,000", "¥10,000,000 -- ¥50,000,000", "Over ¥50,000,000", "Not sure"] Q3: "Blue return (青色申告) or white return (白色申告)?" Options: ["Blue return (青色申告承認申請書 filed)", "White return (白色申告)", "Not sure"]
- **Q1 evaluation** — Q1 = 個人事業主 -> continue. Standard sole proprietor. 開業届 (kaigyo todoke) filed with tax office. Q1 = フリーランス (no opening notification) -> continue with a flag: technically should have filed 開業届 within 1 month of starting business (所得税法第229条). If income qualifies as 事業所得 (business income) vs 雑所得 (miscellaneous income), classification matters. Will evaluate after inference. Q1 = 法人 (corporation) -> stop. "法人 (corporations) file a separate corporate tax return (法人税申告書). I'm set up for 個人事業主 (sole proprietors) filing 確定申告 (individual income tax). You need a 税理士 who handles 法人税." Q1 = Not sure -> ask one follow-up: "Did you file an 開業届 (opening notification) with the tax office? Or do you have a 法人番号 (corporate number)? If you filed 開業届, you're a 個人事業主. If you have a corporate number or 登記簿謄本, you're a 法人."  _(所得税法第229条)_
- **Q2 evaluation** — Q2 = Under ¥10M -> continue. Below consumption tax threshold for base period (基準期間 kijun kikan). Q2 = ¥10M-¥50M -> continue with flag: consumption tax (消費税) filing likely required if base period revenue (2023 for tax year 2025) exceeded ¥10M (消費税法第9条). Also flag: simplified tax calculation (簡易課税 kan'i kazei) available if base period revenue ≤ ¥50M (消費税法第37条). Q2 = Over ¥50M -> continue with flag: consumption tax required, simplified calculation NOT available, must use standard (本則課税 honsoku kazei) method. Q2 = Not sure -> continue, infer from documents.  _(消費税法第9条; 消費税法第37条)_
- **Q3 evaluation** — Q3 = Blue return -> continue. 青色申告特別控除 (blue return special deduction) available: ¥650,000 (e-Tax + double-entry bookkeeping or 電子帳簿保存), ¥550,000 (double-entry paper filing), or ¥100,000 (simplified bookkeeping). Q3 = White return -> continue. No special deduction. Simpler 収支内訳書 (income/expense statement) instead of full 青色申告決算書 (blue return financial statements). Q3 = Not sure -> ask one follow-up: "Did you file a 青色申告承認申請書 (blue return approval application) with the tax office? If you did (usually at the same time as 開業届), you're blue. If not, you're white by default. Check your records or ask your tax office."
- **Second batch of scope questions Q4-Q8** — Q4: "Consumption tax and invoice registration?" Options: ["適格請求書発行事業者 (qualified invoice issuer) registered", "Not registered for invoices (免税事業者 tax-exempt business)", "Registered but considering opting out", "Not sure"] Q5: "Marital status and dependents?" Options: ["Single, no dependents", "Married (配偶者控除 / 配偶者特別控除 eligible spouse)", "Married (spouse earns > ¥2,010,000)", "Have dependent family members (扶養親族)"] Q6: "Other income sources in 2025?" Options: ["None -- self-employment only", "Employment income (給与所得 kyuuyo shotoku)", "Rental income (不動産所得 fudousan shotoku)", "Stock/dividend income (配当所得 haitou shotoku / 譲渡所得 joutsuu shotoku)", "Multiple of the above"] Q7: "e-Tax filing preference?" Options: ["e-Tax (マイナンバーカード + スマホ or ICカードリーダー)", "e-Tax (ID・パスワード方式)", "Paper filing at tax office", "Not sure"] Q8: "Prior year's tax payment (2024 確定申告)?" Options: ["Paid final tax ≥ ¥150,000 (予定納税 yotei nouzei applies)", "Paid final tax < ¥150,000", "First year filing", "Not sure"]
- **Q4 evaluation** — Registered (適格請求書発行事業者) -> continue. Issues qualified invoices (適格請求書 / インボイス). Must file consumption tax return even if revenue < ¥10M (irrevocable for registration period). 2割特例 (20% special provision) may apply if was previously 免税事業者 and registered solely for invoice system (available through tax year 2026 returns per 令和5年改正法附則). Not registered (免税事業者) -> continue. No consumption tax filing obligation (if base period < ¥10M). Cannot issue qualified invoices -- clients cannot claim input tax credit on payments. Registered but considering opting out -> continue with flag: opting out requires 適格請求書発行事業者の登録の取消しを求める届出書, effective from the start of the following fiscal year if filed ≥ 30 days before end of current year. Not sure -> ask: "Check the 国税庁 (NTA) invoice registration site (適格請求書発行事業者公表サイト) for your name or registration number (T + 13 digits). If found, you're registered."  _(令和5年改正法附則)_
- **Q5 evaluation** — Single, no dependents -> continue. 基礎控除 (basic deduction) ¥480,000 only (if income ≤ ¥24M). Married (spouse eligible) -> continue. 配偶者控除 (spouse deduction) up to ¥380,000 if spouse income ≤ ¥480,000 (合計所得金額). 配偶者特別控除 (special spouse deduction) if spouse income ¥480,001-¥1,330,000. Taxpayer's own income must be ≤ ¥10M for either deduction. Married (high-earning spouse) -> continue. No spouse deduction available. Dependent family members -> continue. 扶養控除: ¥380,000 per dependent (general), ¥630,000 (specific: age 19-22), ¥480,000 (elderly: age 70+), ¥580,000 (elderly living together).
- **Q6 evaluation** — All options -> note for multi-schedule return. 給与所得 has its own calculation (給与所得控除). 不動産所得 requires separate schedule. 配当所得 may use 申告分離課税 (separate taxation at 20.315%) or 総合課税 (aggregate taxation with 配当控除).
- **Q7 evaluation** — e-Tax with マイナンバーカード -> continue. Qualifies for ¥650,000 blue return special deduction (if double-entry bookkeeping maintained). e-Tax ID/password -> continue. Same e-Tax benefit for blue return deduction. Paper filing -> continue with flag: blue return special deduction capped at ¥550,000 (double-entry) or ¥100,000 (simplified). Consider switching to e-Tax. Not sure -> note, will recommend e-Tax in action items.
- **Q8 evaluation** — ≥ ¥150,000 -> continue. 予定納税 (estimated tax) applied: two equal instalments (1st period: July, 2nd period: November), each = 1/3 of prior year's 申告納税額. Already paid amounts reduce final balance. < ¥150,000 -> continue. No 予定納税 obligation. First year -> continue. No 予定納税. Not sure -> infer from prior year return or bank statements.

**Total time:** ~60 seconds if the user taps through.

## Section 3 -- The dump

Once the refusal sweep passes, immediately ask for the document dump. Single message. No preamble.

**Example:**

> Scope is good. Now upload everything you have for 2025 -- drop it all in at once:
>
> - Business bank account statements for all of 2025 (CSV or PDF)
> - Sales invoices issued in 2025 (請求書)
> - Purchase invoices / receipts for business expenses (領収書)
> - Prior year's 確定申告書 (tax return) and 青色申告決算書 or 収支内訳書
> - 源泉徴収票 (withholding tax certificate) if you received payments with withholding (源泉徴収)
> - 控除証明書 (deduction certificates): 社会保険料, 生命保険料, 地震保険料, 小規模企業共済
> - 国民健康保険料 (NHI) payment notices from your municipality
> - 国民年金 payment certificates from 日本年金機構
> - Prior year's 予定納税 notices or payment receipts
> - Accounting software export (freee, Money Forward, やよい, etc.)
> - Any 税務署 correspondence
> - Anything else tax-related you have
>
> Don't worry about labeling or organizing -- I'll figure out what each file is. Drag and drop when ready.

Then wait. Do not ask any other questions while waiting.

**If the user uploads a partial dump and says "that's what I have":** move to inference. Do not demand more. Request specific missing items during gap-filling.

**If the user says "I don't know what I have":** Switch to guided mode:
> Check these places:
> - Business bank: download 2025 statements as CSV or PDF
> - Accounting software (freee, Money Forward クラウド, やよいの青色申告): export 仕訳帳 or 総勘定元帳
> - e-Tax: download prior year 確定申告書 and 決算書
> - 年金事務所 or ねんきんネット: download 国民年金控除証明書
> - Municipality: 国民健康保険料 payment statement
> - Insurance companies: 生命保険料控除証明書, 地震保険料控除証明書
> - Clients: request 支払調書 (payment records) or check for 源泉徴収票
> - Email: search for "請求書", "領収書", "確定申告", "税務署"
>
> Come back when you have something to upload. I'll work with whatever you bring.

## Section 4 -- The inference pass

**Bank statement:**
- Total deposits (candidate 売上 uriage / revenue)
- Recurring inflows (client payments with names)
- Outflows to 税務署 (所得税 income tax payments, 予定納税 estimated tax)
- Outflows to municipality (住民税 juminzei / resident tax)
- Outflows to 国民健康保険 (NHI premiums)
- Outflows to 国民年金 (national pension premiums)
- Outflows to suppliers (business expenses by category: 経費 keihi)
- Equipment purchases (potential 減価償却 genkashoukyaku / depreciation assets)
- Transfers to personal account (事業主貸 jigyounushi kashi)
- SaaS / software subscriptions
- 小規模企業共済 (Small Enterprise Mutual Aid) payments
- iDeCo (個人型確定拠出年金) payments
- 生命保険 (life insurance) premiums
- 地震保険 (earthquake insurance) premiums

- **Sales invoices inference items** — **Sales invoices (請求書):** - Client names and amounts (税込 tax-included and 税抜 tax-excluded) - Whether consumption tax was charged (and at what rate: 10% standard, 8% reduced) - Whether invoices are 適格請求書 (qualified invoices) with registration number - Total 売上 reconciliation against bank deposits - Any clients applying 源泉徴収 (withholding): 10.21% on payments up to ¥1M, 20.42% above ¥1M (per specific income types listed in 所得税法第204条) - Foreign clients (no Japanese consumption tax on exported services per 消費税法第7条)  _(所得税法第204条; 消費税法第7条)_
- **Purchase invoices / receipts inference items** — **Purchase invoices / receipts (領収書):** - Expense category (経費科目: 旅費交通費, 通信費, 接待交際費, 消耗品費, etc.) - Consumption tax paid (仕入税額控除 input tax credit, if consumption tax filer) - Any items qualifying as 減価償却資産 (depreciable assets): generally ≥ ¥100,000 - Items ¥100,000-¥299,999: eligible for 一括償却 (3-year straight-line) or 少額減価償却資産の特例 (immediate expensing for blue return filers, up to ¥3M total per year per 租税特別措置法第28条の2) - Any blocked categories (家事関連費 mixed personal/business without clear business proportion)  _(租税特別措置法第28条の2)_

**Prior year 確定申告書 / 青色申告決算書:**
- Prior year 所得金額 (income amount) by category
- Prior year 申告納税額 (tax payable -- drives 予定納税)
- Prior year 青色申告特別控除 amount applied
- 繰越損失 (carryforward losses from prior years -- up to 3 years for blue return filers)
- 減価償却資産 schedule (continuing depreciation)
- Filing method (e-Tax vs paper)

**源泉徴収票 (withholding certificates):**
- Amount of income subject to withholding
- Amount withheld (源泉徴収税額)
- Client name and address
- Will be credited against final tax liability on 確定申告書

- **Deduction certificate inference items** — **控除証明書 (deduction certificates):** - 社会保険料控除: 国民健康保険, 国民年金 amounts paid - 生命保険料控除: 一般, 介護医療, 個人年金 categories and amounts (new system post-2012: max ¥40,000 each, total max ¥120,000) - 地震保険料控除: amount paid (max ¥50,000) - 小規模企業共済等掛金控除: 小規模企業共済 and iDeCo amounts (fully deductible)

**After parsing everything, build an internal inference object.** Do not show the raw inference yet -- transform it into a compact summary for the user in Section 5.

## Section 5 -- The confirmation

After inference, present a single compact summary message. Use a structured format that is fast to scan. Invite the user to correct anything wrong.

**Example summary message:**

> Here's what I pulled from your documents. Skim and tell me what's wrong.
>
> **Identity**
> - 田中太郎 (Tanaka Taro), married, 1 dependent child
> - Full-year Japan resident (Shibuya-ku, Tokyo)
> - 個人事業主, 開業届 filed
> - 青色申告 (blue return), e-Tax filing
> - 適格請求書発行事業者 registered (T1234567890123)
>
> **Income (from bank statement + invoices)**
> - 売上 (revenue, tax-excluded): ¥12,500,000
>   - ABC株式会社: ¥6,000,000 (monthly retainer, 源泉徴収 ¥612,600)
>   - DEF合同会社: ¥4,000,000 (project work)
>   - Various smaller clients: ¥2,500,000
> - 消費税 collected (10%): ¥1,250,000
> - 源泉徴収 total withheld: ¥612,600
>
> **Expenses (from bank + receipts, tax-excluded)**
> - 地代家賃 (rent -- home office portion): ¥720,000 (TBD -- need business use %)
> - 通信費 (internet, phone): ¥180,000 (TBD -- need business use %)
> - 旅費交通費 (travel): ¥350,000
> - 消耗品費 (supplies): ¥120,000
> - 新聞図書費 (books, subscriptions): ¥85,000
> - 外注費 (subcontracting): ¥800,000
> - 減価償却: MacBook Pro ¥280,000 (April 2025) -- 少額減価償却資産特例 eligible (blue return, < ¥300,000)
> - Total deductible expenses (preliminary): ~¥2,535,000
>
> **Social insurance (from 控除証明書 + bank statement)**
> - 国民健康保険: ¥620,000
> - 国民年金: ¥203,760 (¥16,980 x 12)
> - 小規模企業共済: ¥840,000 (¥70,000/month)
> - Total 社会保険料控除 + 小規模企業共済等掛金控除: ¥1,663,760
>
> **Estimated tax (予定納税)**
> - 1st period (July): ¥250,000
> - 2nd period (November): ¥250,000
> - Total paid: ¥500,000
>
> **Prior year (from 2024 確定申告書)**
> - 2024 事業所得: ¥8,200,000
> - 2024 申告納税額: ¥750,000
> - 繰越損失: none
> - 青色申告特別控除: ¥650,000 applied
>
> **Consumption tax (消費税)**
> - Revenue > ¥10M in base period (2023): likely consumption tax filer
> - 適格請求書発行事業者 registered
> - 2割特例 (20% special provision): TBD -- check eligibility
> - 簡易課税: TBD -- check if 届出書 was filed and base period ≤ ¥50M
>
> **Flags I already see:**
> 1. Home office -- need business use percentage for rent, internet, phone (家事按分)
> 2. MacBook Pro ¥280,000 -- eligible for 少額減価償却資産の特例 (immediate expensing) since blue return and < ¥300,000. Verify total 少額 assets don't exceed ¥3M for the year.
> 3. 源泉徴収 ¥612,600 from ABC株式会社 -- will be credited against final tax. Verify 支払調書 matches.
> 4. Consumption tax method needs determination: 本則課税 vs 簡易課税 vs 2割特例
> 5. Revenue ¥12.5M -- above ¥10M threshold, so 2027 will definitely require consumption tax filing regardless of invoice registration
>
> **Is any of this wrong? Reply "looks good" or tell me what to fix.**

## Section 6 -- Gap filling

After the user confirms the summary (or corrects it), ask about things that cannot be inferred from documents. Use `ask_user_input_v0` where possible.

**Things that usually cannot be inferred:**

1. **Home office (家事按分 kaji anbun)** -- business-use percentage of rent, utilities, internet.
2. **Vehicle use** -- business-use percentage if applicable.
3. **Consumption tax calculation method** -- whether 簡易課税届出書 was filed, whether 2割特例 is preferred.
4. **Dependents detail** -- ages, income levels, living arrangements (同居 vs 別居) for correct 扶養控除 amount.
5. **Spouse income** -- exact amount for 配偶者控除 / 配偶者特別控除 determination.
6. **Medical expenses** -- 医療費控除 (medical expense deduction) if total exceeds ¥100,000 or 10% of income.
7. **ふるさと納税 (hometown tax donations)** -- 寄附金控除 (donation deduction) certificates.
8. **生命保険 / 地震保険** -- if certificates not in upload, ask whether applicable.

- **Home office gap-filling example** — Call `ask_user_input_v0` with: Q: "Home office (自宅兼事務所) setup?" Options: ["Dedicated room, used ONLY for work", "Dedicated desk/area in a room", "Shared space (living room, kitchen)", "Separate office or coworking space (not at home)", "No fixed workspace"] If option 1 -> ask for room area and total home area for 家事按分 percentage. Commonly accepted: room area / total area. If option 2 -> flag for reviewer: partial room use. Often 30-50% of room, then room/total for overall percentage. Conservative approach recommended. If option 3 -> flag: shared space makes 家事按分 harder to defend. Conservative percentage (10-20%) with documentation. If option 4 -> rent already captured in business expenses. No 家事按分 needed. If option 5 -> skip home office entirely.
- **Consumption tax method example** — Call `ask_user_input_v0` with: Q: "Consumption tax (消費税) calculation method?" Options: ["簡易課税 (simplified) -- filed 届出書 with tax office", "本則課税 (standard) -- actual input tax credits", "2割特例 (20% special provision) -- was 免税事業者 before invoice registration", "Not sure -- help me choose"] If "Not sure" -> compute under all eligible methods and recommend the one producing the lowest tax. Note in reviewer brief.
- **Medical expenses example** — Call `ask_user_input_v0` with: Q: "Medical expenses (医療費) in 2025?" Options: ["Over ¥100,000 for the household", "Under ¥100,000", "Used セルフメディケーション税制 (OTC medicine deduction)", "Not sure"] If over ¥100,000 -> request 医療費の明細書 or individual receipts. Deduction = total - ¥100,000 (or total - 10% of income if income < ¥2M).

## Section 7 -- The final handoff

Once gap-filling is done, produce a final handoff message and hand off to `jp-return-assembly`.

**Example handoff message:**

> Intake complete. Here's what's going to the return assembly:
>
> 個人事業主, blue return (青色申告), married with 1 dependent, e-Tax filing, 適格請求書発行事業者. Revenue ¥12.5M tax-excluded, estimated 事業所得 ~¥9.3M before blue return deduction. Consumption tax filer.
>
> I'm now going to run the full Japanese return preparation. This covers:
> 1. 消費税 (consumption tax) return
> 2. 所得税 確定申告書 (income tax return) with 青色申告決算書
> 3. 社会保険 reconciliation (国民健康保険, 国民年金)
> 4. 予定納税 and estimated payments for 2026
>
> You'll get back:
> 1. A working paper with all forms and computations
> 2. A reviewer brief with positions, citations, and flags for your 税理士
> 3. A filing calendar with all upcoming deadlines
>
> Starting now.

Then internally invoke `jp-return-assembly` with the structured intake package.

## Section 8 -- Structured intake package (internal format)

The downstream skill (`jp-return-assembly`) consumes a JSON structure. It is internal and not shown to the user unless they ask. Key fields:

```json
{
  "jurisdiction": "JP",
  "tax_year": 2025,
  "taxpayer": {
    "name": "",
    "name_kana": "",
    "date_of_birth": "",
    "my_number": "",
    "marital_status": "single | married",
    "spouse_income": 0,
    "dependents": [],
    "residency": "full_year",
    "address": "",
    "tax_office": "",
    "business_type": "kojin_jigyounushi | freelance_no_kaigyo",
    "blue_return": true,
    "blue_return_deduction_level": "650000 | 550000 | 100000",
    "invoice_registered": true,
    "invoice_registration_number": "",
    "filing_method": "e_tax_mynumber | e_tax_id_password | paper"
  },
  "income": {
    "jigyou_shotoku": {
      "uriage_zeikomi": 0,
      "uriage_zeinuki": 0,
      "consumption_tax_collected": 0,
      "client_breakdown": [],
      "gensen_choushu_total": 0
    },
    "other_income": {
      "kyuuyo_shotoku": 0,
      "fudousan_shotoku": 0,
      "haitou_shotoku": 0,
      "zatsu_shotoku": 0
    }
  },
  "expenses": {
    "keihi_by_category": {},
    "kaji_anbun": {
      "rent_business_pct": 0,
      "internet_business_pct": 0,
      "phone_business_pct": 0,
      "utilities_business_pct": 0
    },
    "depreciation_assets": [],
    "shougaku_assets": []
  },
  "consumption_tax": {
    "filing_required": true,
    "method": "honsoku | kani | niwari_tokurei",
    "kani_gyoushu": 0,
    "base_period_revenue": 0,
    "was_menzei_before_invoice": false
  },
  "deductions": {
    "shakai_hokenryo": {
      "kokumin_kenko_hoken": 0,
      "kokumin_nenkin": 0,
      "other": 0
    },
    "shokibo_kigyou_kyousai": 0,
    "ideco": 0,
    "seimei_hokenryo": {
      "ippan": 0,
      "kaigo_iryou": 0,
      "kojin_nenkin": 0
    },
    "jishin_hokenryo": 0,
    "iryouhi_koujo": 0,
    "furusato_nouzei": 0,
    "haigusha_koujo": 0,
    "fuyou_koujo": 0,
    "kiso_koujo": 480000
  },
  "estimated_tax": {
    "prior_year_shinkoku_nouzei": 0,
    "yotei_nouzei_1st": 0,
    "yotei_nouzei_2nd": 0,
    "total_paid": 0
  },
  "prior_year": {
    "jigyou_shotoku": 0,
    "shinkoku_nouzei_gaku": 0,
    "kurikoshi_songaku": 0,
    "depreciation_schedule": []
  },
  "open_flags": [],
  "refusals_triggered": [],
  "documents_received": []
}
```

## Section 9 -- Refusal handling

Refusals fire from either the refusal sweep (Section 2) or during inference (e.g., corporate structure discovered in documents).

- **R-JP-1 -- 法人 (corporation)** — 法人 (corporations) file 法人税申告書 (corporate tax return) with different forms, deadlines, and rates. I'm set up for 個人事業主 filing 確定申告. You need a 税理士 who handles 法人税.
- **R-JP-2 -- Agriculture (農業所得)** — 農業所得 has its own computation method and may involve 農業所得用 収支内訳書 with specific rules. Outside my current scope.
- **R-JP-3 -- Non-resident** — Non-residents (非居住者) are taxed only on Japan-source income with different rates and withholding rules (所得税法第164条). I'm set up for full-year Japan residents only.  _(所得税法第164条)_
- **R-JP-4 -- Estate / inheritance** — 相続税 (inheritance tax) and 贈与税 (gift tax) are separate tax systems with their own returns. Not in scope.
- **R-JP-5 -- Real estate capital gains** — 不動産の譲渡所得 (capital gains from property sale) requires 分離課税 (separate taxation) with complex holding-period rules. Flag for 税理士.
- **R-JP-6 -- Foreign tax credits (外国税額控除) involving complex treaty application** — Simple foreign tax credits can be handled, but complex multi-country treaty situations need a 税理士 specializing in international tax.
- **Refusal firing procedure and prohibitions** — When a refusal fires: 1. Stop the workflow 2. State the specific reason in one sentence 3. Recommend the path forward (specific practitioner type) 4. Offer to continue with partial help ONLY if the out-of-scope item is cleanly separable (rare) **Do not:** - Apologize profusely - Try to work around the refusal - Suggest the user "might be able to" fit into scope if they answer differently - Continue silently

## Section 10 -- Self-checks

**Check IN1 -- No one-question-at-a-time prose in the refusal sweep.** If the skill asked "Question 1 of 10" or walked through questions as separate messages, check fails.

**Check IN2 -- Refusal sweep used ask_user_input_v0.** The first substantive interaction used the interactive tool, not prose questions.

**Check IN3 -- Upload-first flow honoured.** After refusal sweep, the skill asked for a document dump before asking any content questions.

**Check IN4 -- Documents were parsed and inferred before asking questions.** The inference summary (Section 5) was shown before gap-filling questions (Section 6).

**Check IN5 -- Gap-filling only asked about things NOT visible in documents.** If the skill asked "did you pay 国民年金" after the bank statement showed pension debits, check fails.

**Check IN6 -- Open flags captured.** Anything ambiguous, risky, or attention-worthy during inference is in the `open_flags` list in the handoff package.

**Check IN7 -- Handoff to `jp-return-assembly` is explicit.** The user was told "I'm now going to run the return preparation," and the downstream orchestrator was explicitly invoked with the intake package.

**Check IN8 -- Reviewer step was stated upfront and reiterated before handoff.** The opening message mentioned 税理士 signoff.

**Check IN9 -- Refusals were clean.** No hedging. Stop means stop.

**Check IN10 -- No meta-commentary about workflow phases.** The skill did not say "Phase 1," "Phase 2," etc.

**Check IN11 -- Total user-facing turn count is low.** Target: 8 turns or fewer from start to handoff for a prepared user (1 refusal batch + 1 upload + 1 confirmation + 1-3 gap fills + 1 handoff). More than 12 turns for a normal intake is a check failure.

**Check IN12 -- Blue/white return status was established.** 青色 vs 白色 was confirmed before inference, as it changes deduction levels and bookkeeping expectations.

**Check IN13 -- Consumption tax method was determined.** 本則課税 vs 簡易課税 vs 2割特例 vs exempt was confirmed or flagged for computation comparison.

## Section 11 -- Performance targets

For a prepared user (documents in a folder, ready to upload):
- **Refusal sweep**: 60 seconds (1-2 interactive turns)
- **Document upload**: 2 minutes (1 upload turn)
- **Inference and confirmation display**: 1 minute Claude processing + 1 turn for user confirmation
- **Gap filling**: 2 minutes (2-3 interactive turns)
- **Handoff**: immediate
- **Total**: ~7 minutes

For an unprepared user (has to go fetch documents):
- Refusal sweep: same
- Document discovery: 10-20 minutes offline
- Rest: same
- **Total**: 15-25 minutes

## Section 12 -- Cross-skill references

**Inputs:** User-provided documents and answers.

**Outputs:** Structured intake package consumed by `jp-return-assembly`.

**Downstream skills triggered (via jp-return-assembly):**
- `japan-consumption-tax` -- 消費税確定申告書 (consumption tax return)
- `japan-income-tax` -- 所得税確定申告書 with 青色申告決算書 or 収支内訳書
- `japan-social-insurance` -- 社会保険料 reconciliation (国民健康保険, 国民年金, 小規模企業共済)
- `jp-estimated-tax` -- 予定納税 and estimated payments schedule

### Change log

- **v1.0 (May 2026):** Initial draft. Upload-first, inference-then-confirm pattern modelled on mt-freelance-intake v0.1.

## End of Intake Skill v1.0

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
