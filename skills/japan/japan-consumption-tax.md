---
name: japan-consumption-tax
description: Use this skill whenever asked to prepare, review, or classify transactions for a Japan Consumption Tax (JCT) return (消費税及び地方消費税の確定申告書), handle Qualified Invoice System (QIS / 適格請求書等保存方式) compliance, or advise on JCT registration, filing, and reporting. Trigger on phrases like "prepare consumption tax return", "JCT return", "消費税", "shouhizei", "qualified invoice", "tekikaku invoice", "e-Tax filing", or any Japan consumption tax request. ALWAYS read this skill before touching any JCT-related work.
version: 2.1
jurisdiction: JP
tax_year: 2026
last_updated: 2026-11-14
depends_on:
  - vat-workflow-base
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: vat-gst
type: computation
job: consumption-transaction-workpaper
---

# Japan consumption tax: classification and return working paper v2.1

> **General reference only.** This skill prepares AI-assisted working papers. A qualified 税理士 must review the facts, elections, computations and current forms before filing, paying or taking a tax position.

## Scope

Prepare 2026 transaction classifications, evidence schedules and the `消費税及び地方消費税の確定申告書` working paper. `jp-consumption-tax` owns sole-proprietor liability, method choice and computation; this skill consumes that decision rather than duplicating it. It also screens corporate transactions but refers complex corporate groups. Latest final form orientation is the 2025-2026 filing cycle; 2026 box numbers are not asserted. Contributor: Open Accountants Community.

### Answer layer

| Item and conditions | Figure | Official source / provision |
|---|---|---|
| Standard domestic taxable supply | 10% combined, 7.8% national + 2.2% local | [NTA 6102, Consumption Tax Act art.29](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6102.htm) |
| Eligible food, excluding alcohol, dining-in and catering; qualifying subscription newspapers issued at least 2 times weekly | 8% combined, 6.24% national + 1.76% local | [NTA 6102, reduced-rate provisions](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6102.htm) |
| Sole proprietor base period | 2 calendar years before current year; 2026 uses 2024 (derived) | [NTA 6501, Act art.9](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6501.htm) |
| Base-period exemption, subject to specified-period, registration, election, succession and asset restrictions | Taxable sales <=JPY 10,000,000 (source: 1,000万円) | [NTA 6501, Act arts.9 and 9-2](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6501.htm) |
| General-method full credit, otherwise allowable business inputs only | Current annualised taxable sales <=JPY 500,000,000 (source: 5億円) AND taxable-sales ratio >=95% | [NTA 6401, Act art.30](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6401.htm) |
| Simplified taxation, effective election and no statutory restriction | Base-period taxable sales <=JPY 50,000,000 (source: 5,000万円) | [NTA 6505, Act art.37](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6505.htm) |

## Ask the client first

- Full period dates, entity, registration/election notices and `jp-consumption-tax` status/method decision.
- Complete bank register and opening/closing balances, sales/purchase invoices, cash transactions and prior return.
- Tax-inclusive/exclusive books, rate mix and platform gross-sales/fee settlement statements.
- Supplier registration/evidence, import declarations, exports, foreign digital terms and billing entities.
- Business-use percentages, exempt activities, asset register and national/local interim payments.

No bank/register evidence is a preparation hard stop. A bank statement without invoices permits a provisional classification schedule, never an unsupported credit claim. Request invoices for every credit needing them; no arbitrary transaction-size cutoff replaces the law.

## The method, step by step

1. Read intake and prior return first. Preserve raw bank data, parse date, counterparty, narrative, debit, credit and balance, and reconcile opening + inflows - outflows to closing. Deposits are candidates for revenue, not proof. Gross up withholding and platform-net settlements from invoices/settlement reports; remove own-account transfers and loan principal.
2. Match supplier/reference patterns case-insensitively, most specific first. A pattern identifies evidence to inspect; it never decides tax or invoice registration by name alone. If absent or ambiguous, mark PENDING and ask only the missing fact after examining records.
3. For each transaction record date, amount, currency, gross/net, net base, national/local tax, supply category, rate, business use, supplier registration evidence, invoice/book exception, input credit allowed, source document and unresolved flag. Split mixed invoices, refunds and allowances by actual rate. Import credit uses customs evidence, not a blanket import default.
4. Apply the confirmed method from `jp-consumption-tax`. General-method input credit needs the evidence and allocation tests. Simplified/2割 input workpapers reconcile expenses but do not add actual credits to deemed credits. Invoice-transition purchases split at the actual supply date, including 2026-10-01. [NTA 6498](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6498.htm), [FY 2026 reform](https://www.nta.go.jp/taxes/shiraberu/zeimokubetsu/shohi/keigenzeiritsu/invoice-review/index.htm).
5. Compute national output and eligible national input, then local tax; apply the current form's rounding and map each working-paper value by Japanese field label and selected method. The old①-⑨ universal line list was not the official form and must never be used. [NTA 6351](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6351.htm).
6. Produce the return workbook, source register and reviewer flags, with unresolved amounts excluded from the filing-ready balance. Send the reviewed figures to `jp-etax-filing`; taxpayer/reviewer files and pays.

### Retained pattern library, corrected interpretation

| Patterns retained from prior version | Evidence-led treatment | Official source |
|---|---|---|
| みずほ銀行/MIZUHO BANK;三菱UFJ銀行/MUFG BANK;三井住友銀行/SMBC/SUMITOMO MITSUI;りそな銀行/RESONA BANK;ゆうちょ銀行/JAPAN POST BANK/郵便貯金;楽天銀行/RAKUTEN BANK; SBI新生銀行/SBI SHINSEI; PayPay銀行/PAYPAY BANK;振込手数料/口座維持手数料/ATM手数料;利息/利子/INTEREST | Interest is an exempt category; the provider being a bank does not exempt every service fee. Inspect fee type/invoice. Unresolved fee stays pending | [Act arts.4,6; NTA 6201](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6201.htm) |
| 国税庁/税務署/NTA;消費税/所得税/法人税;社会保険料/年金/健康保険;日本年金機構/JAPAN PENSION SERVICE;労働保険/雇用保険;都道府県税/市区町村税/住民税;印紙税 | Tax/social-insurance remittance is not a business purchase supply. Stamp purchases and stamp-tax payments are distinct | [NTA 6157](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6157.htm), [NTA 6201](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6201.htm) |
| 東京電力/TEPCO/東京電力エナジーパートナー;関西電力/KEPCO/関西電力送配電;中部電力/CHUDEN/CHUBU ELECTRIC;東京ガス/TOKYO GAS;大阪ガス/OSAKA GAS; NTT東日本/NTT西日本/NTT EAST/NTT WEST; NTTドコモ/DOCOMO;ソフトバンク/SOFTBANK; au/KDDI;楽天モバイル/RAKUTEN MOBILE | Check actual domestic electricity/gas/telecom supply, rate and business share; standard rate if no exception | [NTA 6102](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6102.htm) |
| JR東日本/JR西日本/JR EAST/JR WEST;東急電鉄/TOKYU;東京メトロ/TOKYO METRO;都営地下鉄/TOEI SUBWAY;日本航空/JAL/JAPAN AIRLINES;全日空/ANA/ALL NIPPON AIRWAYS;ヤマト運輸/YAMATO TRANSPORT/クロネコヤマト;佐川急便/SAGAWA EXPRESS;日本郵便/JAPANPOST | Distinguish domestic travel/courier, international route, postage use and sale of stamps. Check books-only transport exception; airline name alone proves no export | [NTA 6102](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6102.htm), [NTA 6551](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6551.htm), [NTA 6497](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6497.htm) |
| セブン-イレブン/7-ELEVEN JAPAN;ローソン/LAWSON;ファミリーマート/FAMILY MART;イオン/AEON;イトーヨーカ堂/ITO-YOKADO;ライフ/LIFE SUPERMARKET;業務スーパー/GYOMU SUPER;飲食店/レストラン/食堂; UberEats/ウーバーイーツ;出前館/DEMAE-CAN | Itemised food/non-food, alcohol, dine-in/takeout and catering evidence controls. Delivery fees, commissions and courier labour are separate from food sales | [NTA 6102](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6102.htm) |
| freee/フリー;マネーフォワード/MONEY FORWARD;弥生/YAYOI;勘定奉行/OBC;サイボウズ/CYBOZU; ChatWork/チャットワーク | Inspect billing entity, service and compliant invoice; do not presume registration | [NTA 6498](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6498.htm) |
| GOOGLE/Workspace/Ads/Cloud/Google LLC; MICROSOFT/365/Azure/Microsoft Corp; ADOBE/Adobe Inc; META/FACEBOOK ADS/Meta Platforms Inc; SLACK/Slack Technologies; ZOOM/Zoom Video Communications; GITHUB/GitHub Inc; NOTION/Notion Labs Inc; ANTHROPIC/CLAUDE/Anthropic PBC; OPENAI/CHATGPT/OpenAI Inc; FIGMA/Figma Inc; CANVA/Canva Pty Ltd; AWS/AMAZON WEB SERVICES/AWS Inc | Billing-entity names are legacy search hints, not current facts. Determine actual foreign/domestic entity and B 2 B service terms; use cross-border rule below | [NTA 6118](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6118.htm) |
| STRIPE; PayPay手数料/PAYPAY FEE; Square手数料/SQUARE FEE; LINE Pay手数料/LINE PAY FEE | Do not automatically exempt payment-processing fees. Distinguish exempt financial transaction from taxable service and reconcile withheld fees to gross sales | [NTA 6201](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6201.htm) |
| 振替/内部振替/INTERNAL TRANSFER;借入金/LOAN PROCEEDS;元金返済/LOAN REPAYMENT;役員報酬/給与/賃金;配当金/DIVIDEND; ATM出金/現金引出 | Own transfers/principal/wages/dividends are not consideration for a supply. Trace cash withdrawals to actual expense receipts; withdrawal alone gives no credit | [NTA 6157](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6157.htm) |

### Workpaper design

Use sheets Raw Bank, Classification, Sales by Rate, Input Evidence, Exports, Method Eligibility, National Tax, Local Tax, Interim Credits, Reviewer Flags. Sales schedule: standard/reduced net and gross, export-exempt, domestic exempt, outside scope, returns, taxable ratio. Input schedule: domestic by rate, imports from customs tax, reverse-charge eligibility, transition percentage/date/cap, private-use and partial-exemption reductions. Final schedule: national output minus national allowable credit, local calculation, separate national/local interims, final due/refund. Do not use the old template's 10/110 against net sales or add local tax twice.

Bank CSV hints retained: Mizuho `取引日,摘要,相手先,備考,入金,出金,残高` with `YYYY年MM月DD日`; MUFG `取引日付,取引内容,お支払金額,お預り金額,差引残高`; SMBC `年月日,摘要,金額(出金),金額(入金),残高`; Japan Post `年月日,取引内容,出金,入金,残高`; Rakuten `取引日,入出金種別,摘要,入金額,出金額,残高`; SBI `日付,取引内容,お引き出し,お預け入れ,残高`. These are historical import hints, not guaranteed 2026 bank formats: inspect the actual header before parsing. Parse slash/dot/Japanese dates from data, not presumed bank identity.

`振込入金` incoming wire;`引落/口座振替` debit;`振込出金` outgoing transfer;`利息` interest;`手数料` fee;`残高` balance;`摘要` narrative;`相手先` counterparty;`ATM出金` cash withdrawal;`定期振込` standing transfer. Labels are evidence hints only.

## Boundary and exception table

| Missing fact or exceptional supply | Required response |
|---|---|
| Unknown rate, import class, food mix or B 2 B/B 2 C status | Hold classification; no invented standard-rate, reduced-rate or consumer default |
| Unknown supplier status/invoice | Hold credit until invoice, valid books-only exception or documented transition eligibility is established |
| Unknown vehicle/phone/home share | Separate private portion; hold unsupported business credit; obtain log/area/time evidence |
| Restaurant/cafe or mixed convenience-store purchase | Obtain itemised receipt and customer use at supply; do not classify all grocery/delivery lines at reduced rate |
| Rent | Lease and use distinguish commercial from residential; no assumed residential exemption just from `賃料` |
| Exports | Retain export permit or required service contract/evidence; foreign payer alone insufficient |

Cross-border digital services: reverse charge applies to qualifying foreign business-only digital services as `特定課税仕入れ`. Under the current concession, general-method periods with taxable-sales ratio >=95%, simplified-method periods and 2割 periods treat these purchases as absent: no output self-assessment and no input-only credit. General method below 95% needs reverse-charge and eligible input allocation. Consumer-directed service can be supplier/platform taxed even if bought by a business; do not guess from vendor name. [NTA 6118](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6118.htm).

For invoice cancellation, submit `適格請求書発行事業者の登録の取消しを求める旨の届出書` by the day 15 days before the desired next period starts. A later submission defers effect to the following period; no holiday extension applies to this cancellation deadline. Separate taxable-person-election and asset lock-ins still apply. An exempt operator registered under the transition outside the period containing 2023-10-01 remains taxable through the period containing the date 2 years after registration, even after cancellation. [NTA 6629, Act art.57-2 and notice exceptions](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6629.htm), [NTA registration lock-in FAQ](https://www.nta.go.jp/taxes/shiraberu/zeimokubetsu/shohi/keigenzeiritsu/pdf/sinkijigyousha/faq_k08.pdf).

Goods/asset export evidence change from 2026-10-01: for a transfer or lease made as an export from Japan, if the proceeds are received in cash or by a method that does not clearly establish payment from the transaction counterparty, retain destination-country customs import permission or other proof of actual import, including electronic records, in addition to the ordinary export evidence. NTA examples include direct crypto payment without a crypto exchange and payment from a person other than the counterparty. A bank transfer/documentary-bill settlement that clearly identifies the counterparty does not trigger this extra requirement; the third-party example excludes a guarantor or another person clearly obliged to pay the transaction debt. Do not apply this goods/asset-export rule automatically to exported services. If the payment trail or required destination import proof is missing, hold export-exemption treatment for the affected transaction and refer for evidence review. [Consumption Tax Act art.7, Enforcement Order art.17, Regulations art.5; NTA 6551, cash-receipt section](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6551.htm).

## Worked cases

### Historical bank-line fixtures and corrected use

The original six hypothetical みずほ銀行 CSV lines are preserved verbatim as **2025 historical source-record fixtures**, including descriptions, invoice references, signs and running balances. This unordered sample is not a complete bank reconciliation and does not establish any supplier's actual billing entity, registration or taxable status. Each source line must be interpreted under the evidence tests above; the original fixed form-box and provider-based conclusions are superseded.

```text
2025年04月15日,振込入金,株式会社サクラテック,請求書番号:ST-2025-041,+1,100,000,1,100,000
2025年04月18日,振込入金,ウーバーイーツジャパン合同会社,売上精算 2025-04,+216,000,1,316,000
2025年04月10日,引落,GOOGLE LLC,Google Ads April 2025,-110,000,1,206,000
2025年04月01日,引落,フリー株式会社,freee会計 プロプラン 2025年4月,-11,000,1,195,000
2025年04月01日,引落,田中不動産株式会社,4月分賃料,-110,000,1,085,000
2025年04月22日,外貨入金,Acme Corp USA,Invoice JP-2025-018 IT Consulting,-,+1,250,000,2,335,000
```

Line 1 is the domestic consulting case below. Line 2 is only a JPY 216,000 platform receipt until gross food sales/fees are independently evidenced; Case 2 adds settlement evidence as a separate hypothetical, rather than rewriting that source receipt. Line 3 preserves the old JPY 110,000 payment and vendor narrative, but neither foreign billing nor B 2 B status can be proved from that narrative; the former output-plus-input result at a ratio above 95% is withdrawn under the concession. Line 4 needs actual software invoice/credit evidence. Line 5's rent remains pending until lease/use evidence distinguishes commercial from residential. Line 6 preserves the USD-client narrative and JPY 1,250,000 receipt, including its original extra sign field; retain and resolve that parser anomaly rather than repairing source data silently. Export exemption requires the actual service/place/domestic-benefit evidence. No line's running balance proves a tax classification.

Case 1 preserves the domestic consulting and software examples: `株式会社サクラテック` pays JPY 1,100,000 gross, `フリー株式会社` invoice JPY 11,000 gross. Confirm standard-rate domestic supplies and qualified input evidence. Net sale JPY 1,000,000; combined output JPY 100,000; software net JPY 10,000 and combined input JPY 1,000; national balance JPY 77,220, local JPY 21,780, total JPY 99,000 as an unrounded transaction-stage estimate. This is not the final return balance: apply the annual form rounding after aggregating the period. These are hypothetical source-document inputs, not actual registration claims. [NTA 6351](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6351.htm).

```oa-check
name: Classify gross domestic invoice and software purchase
inputs:
  sale: 1100000
  software: 11000
steps:
  sale_net: sale / 1.10
  software_net: software / 1.10
  national: (sale_net - software_net) * 0.078
  local: national * 22 / 78
  total: national + local
expected:
  sale_net: 1000000
  software_net: 10000
  national: 77220
  total: 99000
```

Case 2 preserves the mixed food/rent facts while correcting platform-net inference: hypothetical `ウーバーイーツジャパン合同会社` statement proves food gross JPY 216,000, separately taxable service gross JPY 11,000, net settlement JPY 205,000. Food net JPY 200,000 and combined output JPY 16,000; service net JPY 10,000 and input JPY 1,000 if eligible. Net combined liability JPY 15,000 before other items. A payout without that settlement evidence must not be grossed at a presumed food rate. [NTA 6102](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6102.htm), [NTA 6351](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6351.htm).

```oa-check
name: Gross food sales and separately evidenced platform fee
inputs:
  food_gross: 216000
  fee_gross: 11000
steps:
  food_net: food_gross / 1.08
  output: food_net * 0.08
  input_credit: fee_gross / 1.10 * 0.10
  settlement: food_gross - fee_gross
  combined_balance: output - input_credit
expected:
  output: 16000
  input_credit: 1000
  settlement: 205000
  combined_balance: 15000
```

Other retained cases: `GOOGLE LLC`JPY 110,000 net qualifying B 2 B purchase under general method with ratio>=95% has no reverse-charge entry under the concession; below 95% national output would be JPY 8,580 before allowable allocation. `田中不動産株式会社`JPY 110,000 rent is pending until lease/use confirmed; confirmed commercial gross standard rent contains JPY 10,000 combined tax, residential exemption has no ordinary input tax. `Acme Corp USA`JPY 1,250,000 contract qualifies for export exemption only after domestic-benefit tests and evidence; eligible export output tax is JPY 0. No historical sample identifies an actual person's tax facts.

## When to refuse or refer

R-JP-1: exempt operator, verify all status exceptions and do not fabricate a taxable return. R-JP-2: complex corporate groups/intercompany adjustments require specialist review; do not assert a consolidated JCT filing regime. R-JP-3: partial-exemption allocation where ratio<95% OR annualised sales>JPY 500,000,000 requires specialist working papers. R-JP-4: non-resident digital supplier registration/platform obligations are outside scope. R-JP-5: real estate/construction long contracts, land/building allocation, transfer-pricing adjustments and complex group restructures require specialist input. Continue separable supported work with the boundary visible.

Never claim unsupported inputs, invent exports, reduce dine-in/alcohol rates, assume vendor billing identities, omit an applicable reverse charge, or present provisional figures as filing-ready.

## Filing and payment

### Filing and interim calendar

| Obligation and conditions | Deadline or amount | Official source |
|---|---|---|
| Calendar 2026 individual final JCT return/payment | 2027-03-31; established automatic transfer 2027-04-30 | [NTA annual calendar](https://www.nta.go.jp/taxes/nozei/nofu/24200042/noufu_kigen.htm) |
| Latest final 2025 individual JCT return/payment,2025-2026 filing cycle | 2026-03-31; established automatic transfer 2026-04-30 | [NTA annual calendar](https://www.nta.go.jp/taxes/nozei/nofu/24200042/noufu_kigen.htm) |
| Corporation, ordinary final return | Within 2 months after period end; approved corporate extension can add 1 month for the year-end period | [Act arts.45,45-2; NTA 6601](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6601.htm) |
| Optional monthly/quarterly shortened periods | Generally within 2 months after period end; individual period containing December 31 is due March 31 | [Act arts.19,45; NTA 6601](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6601.htm) |
| Prior annual NATIONAL tax, local excluded, <=JPY 480,000 (source: 48万円) | No mandatory interim return; optional system exists | [Act arts.42-44; NTA 6609](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6609.htm) |
| Prior annual national tax >JPY 480,000 (source: 48万円) to JPY 4,000,000 inclusive | 1 interim, prior tax times 6/12 plus local 22/78 | [NTA 6609](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6609.htm) |
| Prior annual national tax >JPY 4,000,000 to JPY 48,000,000 inclusive | 3 interims, each prior tax times 3/12 plus local 22/78 | [NTA 6609](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6609.htm) |
| Prior annual national tax >JPY 48,000,000 | 11 interims, each prior tax times 1/12 plus local 22/78; special initial-month timing | [NTA 6609](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6609.htm) |

Interims generally fall due within 2 months after the covered period; individual monthly January-March amounts have special May-end timing. Short prior periods, corporate extension and deemed interim returns need the actual NTA notice. Interim provisional-account returns cannot produce a refund. [NTA 6609](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6609.htm). Do not confuse shortened taxable periods with interim periods. A taxable operator with no taxable supplies/specified purchases and no tax due may have no filing duty but can claim an eligible input/interim refund. [NTA 6605](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6605.htm).

For the 2025-2026 cycle general-method return, attach the rate breakdown and taxable-sales/input-credit calculation schedules; refund cases may require the refund detail schedule. Simplified method has its own credit schedule,2割 has rate-specific付表. Do not claim an unverified 2026 box number. Use `jp-etax-filing` for submission and receipt/payment follow-through.

## Completion checklist

Resolve or explicitly exclude each pending item; confirm source-register/bank balance, rate split, QIS or lawful exception evidence, exports, reverse-charge screening, transition dates/caps,95% test, method election, national/local calculations, interim credits and final reviewer signoff. If onboarding is incomplete, prepare a clearly provisional schedule and ask only status/effective dates, period, election/activity, exempt supplies, exports, vehicle share and missing mixed receipts. Never infer legal status from one year's bank deposits.

## Sources

| Source | URL | Read on |
|---|---|---|
| NTA 6102: Read for rate classifications and food exceptions | https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6102.htm | 2026-11-14 |
| NTA 6201: Read for financial and other exemptions, residential/land exceptions | https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6201.htm | 2026-11-14 |
| NTA 6157: Read for non-consideration and outside-scope examples | https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6157.htm | 2026-11-14 |
| NTA 6351: Read for gross/net and national-tax computation | https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6351.htm | 2026-11-14 |
| NTA 6401: Read for partial-credit boundary | https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6401.htm | 2026-11-14 |
| NTA 6497: Read for invoice/book exceptions and reverse charge | https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6497.htm | 2026-11-14 |
| NTA 6498: Read for registration evidence and transition cap | https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6498.htm | 2026-11-14 |
| NTA reform: Read for 2026 input-credit timeline | https://www.nta.go.jp/taxes/shiraberu/zeimokubetsu/shohi/keigenzeiritsu/invoice-review/index.htm | 2026-11-14 |
| NTA 6118: Read for digital B 2 B/B 2 C and 95% concession | https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6118.htm | 2026-11-14 |
| NTA 6551: Read for export evidence, cash/unclear-payer destination import proof, exceptions and domestic-benefit exclusions | https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6551.htm | 2026-11-14 |
| NTA 6601: Read for final and shortened-period deadlines | https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6601.htm | 2026-11-14 |
| NTA 6605: Read for no-activity filing exception | https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6605.htm | 2026-11-14 |
| NTA 6609: Read for interim thresholds/timing | https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6609.htm | 2026-11-14 |
| NTA 6629: Read for invoice cancellation deadline, no-holiday rule and election exceptions | https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6629.htm | 2026-11-14 |
| NTA registration lock-in FAQ: Read for cancellation versus 2-year taxable status and first-period exception | https://www.nta.go.jp/taxes/shiraberu/zeimokubetsu/shohi/keigenzeiritsu/pdf/sinkijigyousha/faq_k08.pdf | 2026-11-14 |
| NTA dates: Read for individual due and debit dates | https://www.nta.go.jp/taxes/nozei/nofu/24200042/noufu_kigen.htm | 2026-11-14 |

Not yet confirmed: Final 2026 form boxes; vendor-specific current billing entities, registration status and bank export layouts; precise fee contracts; penalty/interest assessment; The old arbitrary HIGH/MEDIUM/LOW thresholds and invoice-size recommendation were internal heuristics with no official tax authority basis and are not usable tax rules. Historical penalty table and blanket bank/payment-fee exemption are withdrawn pending fact-specific statutory confirmation.
