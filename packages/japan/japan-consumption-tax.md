---
name: japan-consumption-tax
description: Use this skill whenever asked to prepare, review, or classify transactions for a Japan Consumption Tax (JCT) return (消費税及び地方消費税の確定申告書), handle Qualified Invoice System (QIS / 適格請求書等保存方式) compliance, or advise on JCT registration, filing, and reporting. Trigger on phrases like "prepare consumption tax return", "JCT return", "消費税", "shouhizei", "qualified invoice", "tekikaku invoice", "e-Tax filing", or any Japan consumption tax request. ALWAYS read this skill before touching any JCT-related work.
version: 2.0
jurisdiction: JP
tax_year: 2025
category: international
depends_on:
  - vat-workflow-base
---

# Japan Consumption Tax (JCT / 消費税) Skill v2.0

---

## Section 1 — Quick reference

| Field | Value |
|---|---|
| Country | Japan (日本国) |
| Tax | Consumption Tax (消費税 / JCT) + Local Consumption Tax (地方消費税) |
| Currency | JPY only |
| Tax year | Fiscal year (varies by entity; calendar year for most individuals) |
| Standard rate | 10% (national 7.8% + local 2.2%) |
| Reduced rate | 8% (food and non-alcoholic beverages 食料品; subscription newspapers 新聞) |
| Zero rate | 0% (exports 輸出; international transport) |
| Exempt | Financial services, insurance, medical, education, residential rent, postage stamps, certain land transactions |
| Registration threshold | JPY 10,000,000 in base period (基準期間) taxable sales |
| Small business simplified | 簡易課税制度 — taxable sales ≤ JPY 50M; fixed credit ratio by industry |
| Tax authority | National Tax Agency (NTA / 国税庁) |
| Filing portal | e-Tax (https://www.e-tax.nta.go.jp) |
| Return form | 消費税及び地方消費税の確定申告書 |
| Annual filing deadline | 2 months after fiscal year end (e.g., 31 March for calendar-year filers) |
| Quarterly/monthly deadlines | End of month following reporting period |
| QIS registration | 適格請求書発行事業者登録番号 — T + 13 digits; mandatory from 1 October 2023 |
| Contributor | Open Accountants Community |
| Validated by | Pending — requires sign-off by a Japan-licensed zeirishi (税理士) |
| Skill version | 2.0 |

### Key return form lines

| Line | Meaning |
|---|---|
| ① | Taxable sales (課税売上高) at 10% — net of tax |
| ② | Taxable sales at 8% reduced rate — net of tax |
| ③ | Zero-rated exports (輸出売上高) |
| ④ | Exempt sales (非課税売上高) |
| ⑤ | Total output tax (課税標準額に対する消費税額) |
| ⑥ | Input tax credit (仕入税額控除) |
| ⑦ | Net consumption tax payable (納付税額) = ⑤ − ⑥ |
| ⑧ | Local consumption tax (地方消費税) = ⑦ × 22/78 |
| ⑨ | Total payable (⑦ + ⑧) |

### Conservative defaults

| Ambiguity | Default |
|---|---|
| Unknown rate on a sale | 10% standard |
| Unknown whether food/beverage qualifies for 8% | 10% until confirmed |
| Unknown counterparty registration status | Assume unregistered — no input credit |
| Unknown business-use % (vehicle, phone, home) | 0% credit |
| Unknown import classification | Taxable at 10% |
| Unknown whether QIS invoice available | No input credit until confirmed |
| Unknown B2B vs B2C for digital services | B2C — supplier must self-assess |

### Red flag thresholds

| Threshold | Value |
|---|---|
| HIGH single transaction | JPY 300,000 |
| HIGH tax delta on single conservative default | JPY 30,000 |
| MEDIUM counterparty concentration | >40% of output or input |
| MEDIUM conservative default count | >4 per return |
| LOW absolute net JCT position | JPY 500,000 |

---

## Section 2 — Required inputs and refusal catalogue

### Required inputs

**Minimum viable** — bank statement for the full fiscal year in CSV, PDF, or pasted text, plus confirmation of registration status (taxable operator 課税事業者 or exempt 免税事業者) and fiscal year dates.

**Recommended** — QIS registration number (T + 13 digits), sales invoices (適格請求書) for any line above JPY 100,000, purchase invoices confirming supplier QIS numbers.

**Ideal** — complete transaction register (帳簿), prior year return, asset register, quarterly prepayment records (中間申告), industry code for 簡易課税.

**Refusal if minimum is missing — SOFT WARN.** No bank statement = hard stop. Bank statement without invoices = proceed but flag: "Input tax credit claims require qualified invoices (適格請求書) from QIS-registered suppliers. All credits are provisional pending invoice verification."

### Refusal catalogue

**R-JP-1 — Exempt business operator (免税事業者).** "This client's base-period taxable sales are below JPY 10M. They are exempt from filing a consumption tax return and cannot recover input tax. If they have voluntarily registered (課税事業者選択届出書), provide registration document before proceeding."

**R-JP-2 — Corporations with complex group structures.** "Consolidated consumption tax filing and intercompany transactions in a corporate group require specialist handling. Out of scope."

**R-JP-3 — 95% rule with proportional allocation required.** "Client makes both taxable and exempt supplies and taxable sales exceed JPY 500M, triggering individual or lump-sum proportional methods. Out of scope — escalate to zeirishi."

**R-JP-4 — Non-resident digital service providers.** "Non-resident businesses providing digital services to Japanese consumers (国境を越えた役務の提供) have separate registration and filing obligations. Out of scope."

**R-JP-5 — Real estate or construction companies.** "Industry-specific JCT rules for real estate and construction (e.g., long-term contracts, land/building allocation) require specialist input. Out of scope."

---

## Section 3 — Supplier pattern library

Match by case-insensitive substring on the counterparty name or reference in the bank statement. Most specific match wins. If no match, fall through to Section 5.

### 3.1 Japanese banks — fees and charges (exempt / exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| みずほ銀行, MIZUHO BANK | EXCLUDE (bank fee lines) | Financial service — exempt from JCT |
| 三菱UFJ銀行, MUFG BANK | EXCLUDE (bank fee lines) | Same |
| 三井住友銀行, SMBC, SUMITOMO MITSUI | EXCLUDE (bank fee lines) | Same |
| りそな銀行, RESONA BANK | EXCLUDE (bank fee lines) | Same |
| ゆうちょ銀行, JAPAN POST BANK, 郵便貯金 | EXCLUDE (bank fee lines) | Same |
| 楽天銀行, RAKUTEN BANK | EXCLUDE (bank fee lines) | Same |
| SBI新生銀行, SBI SHINSEI | EXCLUDE (bank fee lines) | Same |
| PayPay銀行, PAYPAY BANK | EXCLUDE (bank fee lines) | Same |
| 振込手数料, 口座維持手数料, ATM手数料 | EXCLUDE | Bank transaction/maintenance fees — exempt |
| 利息, 利子, INTEREST | EXCLUDE | Interest income/expense — exempt from JCT |

### 3.2 Japanese government and statutory payments (exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| 国税庁, 税務署, NTA | EXCLUDE | Tax payment — not a supply |
| 消費税, 所得税, 法人税 | EXCLUDE | Tax remittance — not a supply |
| 社会保険料, 年金, 健康保険 | EXCLUDE | Social insurance — out of JCT scope |
| 日本年金機構, JAPAN PENSION SERVICE | EXCLUDE | Pension — out of scope |
| 労働保険, 雇用保険 | EXCLUDE | Employment insurance — out of scope |
| 都道府県税, 市区町村税, 住民税 | EXCLUDE | Local income tax — not a JCT supply |
| 印紙税 | EXCLUDE | Stamp duty — exempt |

### 3.3 Japanese utilities (taxable at 10%)

| Pattern | Treatment | Rate | Notes |
|---|---|---|---|
| 東京電力, TEPCO, 東京電力エナジーパートナー | Input 10% | 10% | Electricity — taxable |
| 関西電力, KEPCO, 関西電力送配電 | Input 10% | 10% | Electricity — taxable |
| 中部電力, CHUDEN, CHUBU ELECTRIC | Input 10% | 10% | Electricity — taxable |
| 東京ガス, TOKYO GAS | Input 10% | 10% | Gas — taxable |
| 大阪ガス, OSAKA GAS | Input 10% | 10% | Gas — taxable |
| NTT東日本, NTT西日本, NTT EAST, NTT WEST | Input 10% | 10% | Fixed-line telephone — taxable |
| NTTドコモ, DOCOMO | Input 10% | 10% | Mobile — taxable |
| ソフトバンク, SOFTBANK | Input 10% | 10% | Mobile/internet — taxable |
| au, KDDI | Input 10% | 10% | Mobile — taxable |
| 楽天モバイル, RAKUTEN MOBILE | Input 10% | 10% | Mobile — taxable |

### 3.4 Japanese transport (various rates)

| Pattern | Treatment | Rate | Notes |
|---|---|---|---|
| JR東日本, JR西日本, JR EAST, JR WEST | Input 10% | 10% | Domestic rail — taxable |
| 東急電鉄, TOKYU | Input 10% | 10% | Private rail — taxable |
| 東京メトロ, TOKYO METRO | Input 10% | 10% | Subway — taxable |
| 都営地下鉄, TOEI SUBWAY | Input 10% | 10% | Subway — taxable |
| 日本航空, JAL, JAPAN AIRLINES | Check route | 0%/10% | Domestic 10%; international 0% |
| 全日空, ANA, ALL NIPPON AIRWAYS | Check route | 0%/10% | Domestic 10%; international 0% |
| ヤマト運輸, YAMATO TRANSPORT, クロネコヤマト | Input 10% | 10% | Domestic courier — taxable |
| 佐川急便, SAGAWA EXPRESS | Input 10% | 10% | Domestic courier — taxable |
| 日本郵便, JAPANPOST (parcel) | Input 10% | 10% | Parcel services — taxable |
| 日本郵便, JAPANPOST (stamps) | EXCLUDE | Exempt | Postage stamps — exempt |

### 3.5 Food and retail (8% reduced rate for food items)

| Pattern | Treatment | Rate | Notes |
|---|---|---|---|
| セブン-イレブン, 7-ELEVEN JAPAN | Split 8%/10% | Mixed | Food 8%; non-food 10%; eat-in 10% |
| ローソン, LAWSON | Split 8%/10% | Mixed | Same |
| ファミリーマート, FAMILY MART | Split 8%/10% | Mixed | Same |
| イオン, AEON | Split 8%/10% | Mixed | Supermarket — classify by item |
| イトーヨーカ堂, ITO-YOKADO | Split 8%/10% | Mixed | Same |
| ライフ, LIFE SUPERMARKET | Input 8% (food) | 8% | Grocery — default food rate |
| 業務スーパー, GYOMU SUPER | Input 8% (food) | 8% | Wholesale food — taxable at 8% |
| 飲食店, レストラン, 食堂 (eat-in) | Input 10% | 10% | Eat-in meals — standard rate |
| UberEats, ウーバーイーツ | Input 8% | 8% | Takeout food delivery — reduced rate |
| 出前館, DEMAE-CAN | Input 8% | 8% | Takeout delivery — reduced rate |

### 3.6 SaaS — Japanese suppliers (taxable at 10%)

| Pattern | Treatment | Rate | Notes |
|---|---|---|---|
| freee, フリー | Input 10% | 10% | Japanese accounting SaaS — taxable |
| マネーフォワード, MONEY FORWARD | Input 10% | 10% | Japanese finance SaaS — taxable |
| 弥生, YAYOI | Input 10% | 10% | Japanese accounting software — taxable |
| 勘定奉行, OBC | Input 10% | 10% | Japanese ERP — taxable |
| サイボウズ, CYBOZU | Input 10% | 10% | Japanese groupware — taxable |
| ChatWork, チャットワーク | Input 10% | 10% | Japanese messaging SaaS — taxable |

### 3.7 SaaS — international suppliers (reverse charge for B2B)

For B2B digital services from foreign suppliers (国外事業者から受ける電気通信利用役務の提供), the Japanese business must self-assess JCT under the reverse charge mechanism (リバースチャージ方式). Applies only to taxable businesses where taxable sales > 95% of total sales.

| Pattern | Billing entity | Treatment | Notes |
|---|---|---|---|
| GOOGLE (Workspace, Ads, Cloud) | Google LLC (US) | Reverse charge 10% | Self-assess; note on return |
| MICROSOFT (365, Azure) | Microsoft Corp (US) | Reverse charge 10% | Same |
| ADOBE | Adobe Inc (US) | Reverse charge 10% | Same |
| META, FACEBOOK ADS | Meta Platforms Inc (US) | Reverse charge 10% | Same |
| SLACK | Slack Technologies (US) | Reverse charge 10% | Same |
| ZOOM | Zoom Video Communications (US) | Reverse charge 10% | Same |
| GITHUB | GitHub Inc (US) | Reverse charge 10% | Same |
| NOTION | Notion Labs Inc (US) | Reverse charge 10% | Same |
| ANTHROPIC, CLAUDE | Anthropic PBC (US) | Reverse charge 10% | Same |
| OPENAI, CHATGPT | OpenAI Inc (US) | Reverse charge 10% | Same |
| FIGMA | Figma Inc (US) | Reverse charge 10% | Same |
| CANVA | Canva Pty Ltd (AU) | Reverse charge 10% | Same |
| AWS (AMAZON WEB SERVICES) | AWS Inc (US) | Reverse charge 10% | Check if billed via Japanese entity |

### 3.8 Payment processors and fintech

| Pattern | Treatment | Notes |
|---|---|---|
| STRIPE (transaction fees) | EXCLUDE (exempt) | Payment processing — exempt financial service |
| PayPay手数料, PAYPAY FEE | EXCLUDE (exempt) | Payment processing — exempt |
| Square手数料, SQUARE FEE | EXCLUDE (exempt) | Same |
| LINE Pay手数料, LINE PAY FEE | EXCLUDE (exempt) | Same |

### 3.9 Internal transfers and exclusions

| Pattern | Treatment | Notes |
|---|---|---|
| 振替, 内部振替, INTERNAL TRANSFER | EXCLUDE | Internal movement between own accounts |
| 借入金, LOAN PROCEEDS | EXCLUDE | Loan principal — out of JCT scope |
| 元金返済, LOAN REPAYMENT | EXCLUDE | Loan repayment — out of scope |
| 役員報酬, 給与, 賃金 | EXCLUDE | Salaries/wages — outside JCT scope |
| 配当金, DIVIDEND | EXCLUDE | Dividend — exempt |
| ATM出金, 現金引出 | Tier 2 — ask | Default exclude; ask what cash was spent on |

---

## Section 4 — Worked examples

Six classifications drawn from a hypothetical bank statement of a Tokyo-based freelance IT consultant. Format: みずほ銀行 CSV export.

### Example 1 — Client payment (domestic, taxable at 10%)

**Input line:**
`2025年04月15日,振込入金,株式会社サクラテック,請求書番号:ST-2025-041,+1,100,000,1,100,000`

**Reasoning:**
Incoming JPY 1,100,000 from a Japanese company. This is revenue for IT consulting services. Standard rate 10% applies. If the invoice is JPY 1,100,000 gross, net = JPY 1,000,000 (課税売上高) + JPY 100,000 (JCT). Report net on line ①. Confirm QIS invoice was issued showing registration number T + 13 digits.

**Classification:** 課税売上高 (taxable sales) Line ①, JPY 1,000,000 net. Output JCT: JPY 100,000.

### Example 2 — Food delivery platform payout (reduced rate 8%)

**Input line:**
`2025年04月18日,振込入金,ウーバーイーツジャパン合同会社,売上精算 2025-04,+216,000,1,316,000`

**Reasoning:**
Payout from Uber Eats Japan (takeout food delivery). Takeout food is reduced rate 8%. JPY 216,000 gross includes 8% JCT. Net = JPY 200,000 (課税売上高 reduced) + JPY 16,000 (JCT). Report on line ② (reduced rate sales). Confirm platform invoices show the 8% rate and the client's QIS registration.

**Classification:** 課税売上高 reduced rate line ②, JPY 200,000 net. Output JCT at 8%: JPY 16,000.

### Example 3 — International reverse charge (Google Ads)

**Input line:**
`2025年04月10日,引落,GOOGLE LLC,Google Ads April 2025,-110,000,1,206,000`

**Reasoning:**
Google LLC is a US entity providing B2B digital advertising services to a Japanese business. This triggers the reverse charge mechanism (リバースチャージ方式). The JPY 110,000 payment is treated as net (Google does not charge Japanese JCT on the invoice). Self-assess: output JCT = JPY 110,000 × 10/110 × 10% ... actually: JPY 110,000 is net; self-assessed JCT = JPY 110,000 × 10% = JPY 11,000. Simultaneously claim same as input credit if taxable sales > 95% threshold.

**Classification:** Reverse charge — note on return. Net base: JPY 110,000. Self-assessed JCT: JPY 11,000 (output and input if fully taxable).

### Example 4 — Domestic software subscription (10%, requires QIS invoice)

**Input line:**
`2025年04月01日,引落,フリー株式会社,freee会計 プロプラン 2025年4月,-11,000,1,195,000`

**Reasoning:**
freee is a Japanese SaaS company (QIS registered). Monthly subscription JPY 11,000 gross. Net = JPY 10,000 + JPY 1,000 JCT at 10%. Input credit claimable if supplier's QIS registration number (T + 13 digits) appears on the invoice/receipt. freee is a major registered supplier — credit is expected to be available. Confirm invoice.

**Classification:** Input JCT Line ⑥, JPY 1,000. Net purchase JPY 10,000.

### Example 5 — Exempt rent (residential — no input credit)

**Input line:**
`2025年04月01日,引落,田中不動産株式会社,4月分賃料,-110,000,1,085,000`

**Reasoning:**
Monthly rent payment. Need to determine: is this office rent (課税) or residential rent (非課税)? The reference "賃料" (rent) is ambiguous. Default: residential = exempt, no input credit. If this is confirmed commercial/office rent and the landlord is JCT-registered and issued a qualified invoice, input credit is available. Flag for confirmation.

**Classification:** Tier 2 — ask. Default: EXCLUDE (residential/exempt assumption). If commercial: Input 10%, JPY 10,000 credit available.

### Example 6 — Export sale (zero rate)

**Input line:**
`2025年04月22日,外貨入金,Acme Corp USA,Invoice JP-2025-018 IT Consulting,-,+1,250,000,2,335,000`

**Reasoning:**
Incoming JPY 1,250,000 from a US company for IT consulting exported overseas. Export services (輸出免税) are zero-rated (0% JCT) if the service is provided to a non-resident for use outside Japan. Report on line ③. The client must retain export evidence (contracts, wire transfer records showing foreign payor). No output JCT. No box entry for input side of this transaction.

**Classification:** 輸出等の売上高 (zero-rated exports) Line ③, JPY 1,250,000. Output JCT: JPY 0.

---

## Section 5 — Tier 1 rules (compressed)

Apply these rules when a transaction is unambiguous. No flags required. For complex or data-dependent situations, see Tier 2 catalogue in Section 6.

### 5.1 Standard rate 10%

All taxable supplies of goods and services in Japan not falling into reduced rate, zero rate, or exemption. Output: Line ①. Input credit: Line ⑥. Legislation: Consumption Tax Act (消費税法) Article 29.

### 5.2 Reduced rate 8% (軽減税率)

Applies to: (1) food and non-alcoholic beverages 食料品 for home consumption (takeout, grocery) — NOT eat-in meals; (2) subscription newspapers (週2回以上発行の定期購読新聞). Output: Line ②. Legislation: 消費税法 Article 29, 軽減税率 Schedule.

**Eat-in test:** If food is consumed on the premises (外食), standard 10% applies. If taken away or delivered, 8% applies. When bank statement only — default to 8% for grocery/delivery, flag restaurants as 10%.

### 5.3 Zero rate 0% — exports (輸出免税)

Exports of goods and services provided to non-residents for use outside Japan are zero-rated. Evidence required: export declarations (輸出許可通知書) for goods; contracts and payment records for services. Legislation: 消費税法 Article 7.

### 5.4 Exempt supplies (非課税取引)

No JCT charged; no input credit on related purchases. Includes: financial services (利子、保険料), medical services (社会保険診療), education (学校教育), residential rent (住宅の貸付), postage stamps, certain land transactions. Legislation: 消費税法 Article 6, Exempt Schedule (別表第一).

### 5.5 Outside scope (不課税 / 課税対象外)

No JCT. Includes: wages and salaries (給与), dividend payments (配当), gifts, donations, loan principal. These are not supplies for JCT purposes. Legislation: 消費税法 Article 2(1)(viii).

### 5.6 QIS invoice requirement (適格請求書等保存方式)

From 1 October 2023, input tax credit requires a qualified invoice (適格請求書) from a QIS-registered supplier. Required fields: supplier name, QIS registration number (T + 13 digits), transaction date, description, taxable amount (10% and 8% separately), JCT amount, recipient name. Without a compliant invoice, NO input credit is allowed.

### 5.7 Transitional credit for non-QIS suppliers (経過措置)

Purchases from unregistered suppliers: 80% of otherwise allowable credit available through 30 September 2026; 50% through 30 September 2029; 0% thereafter. Always flag when supplier QIS status is unconfirmed.

### 5.8 Filing deadlines

| Filer type | Deadline |
|---|---|
| Individual (calendar year) | 31 March of following year |
| Corporation (annual) | 2 months after fiscal year end |
| Quarterly filers | End of month following quarter |
| Monthly filers | End of following month |
| Interim payment (中間申告) | End of month following applicable period |

### 5.9 Simplified tax method (簡易課税制度)

Available to taxable businesses with prior-year taxable sales ≤ JPY 50M. Input credit is calculated as a fixed percentage of output tax based on industry category (みなし仕入率):

| Category | Industry | Credit ratio |
|---|---|---|
| 第一種 | Wholesale | 90% |
| 第二種 | Retail, agriculture | 80% |
| 第三種 | Manufacturing, construction | 70% |
| 第四種 | Restaurant, other | 60% |
| 第五種 | Services (IT consulting, finance, insurance) | 50% |
| 第六種 | Real estate | 40% |

Actual input invoices are irrelevant under 簡易課税 — the fixed ratio applies automatically.

### 5.10 Penalties

| Offence | Penalty |
|---|---|
| Late filing (無申告加算税) | 15% of unpaid tax (20% if undeclared income detected) |
| Late payment (延滞税) | 2.4%–8.7% per annum (rate varies by year) |
| Understatement (過少申告加算税) | 10% (15% if detected after investigation) |
| Fraud (重加算税) | 35%–40% |

---

## Section 6 — Tier 2 catalogue (reviewer judgement required)

Tier 2 items are those where the correct classification cannot be determined from the bank statement line alone because critical factual data is missing. The rule is clear — the data is not.

### 6.1 Eat-in vs. takeout (restaurant/café charges)

**What it shows:** Debit to a restaurant or café.
**What's missing:** Whether the meal was consumed on premises (eat-in = 10%) or taken away (takeout = 8%).
**Conservative default:** 10% (eat-in).
**Question to ask:** "Was this meal consumed at the restaurant, or was it a takeout/delivery order?"

### 6.2 Commercial vs. residential rent

**What it shows:** Regular debit to a property company or individual labelled "賃料" or "家賃".
**What's missing:** Whether the premises are office/commercial (課税) or residential (非課税/exempt).
**Conservative default:** Exempt — no input credit.
**Question to ask:** "Is this payment for office/commercial space or for residential accommodation? Does the landlord issue a JCT-registered invoice?"

### 6.3 Vehicle expenses (business vs. personal use)

**What it shows:** Debit to petrol station, parking, car dealer, or car leasing company.
**What's missing:** Business-use percentage; whether a mileage log (運行記録) is maintained.
**Conservative default:** 0% input credit.
**Question to ask:** "What percentage of this vehicle's use is for business? Is a mileage log maintained?"

### 6.4 Cash withdrawals (ATM出金)

**What it shows:** ATM cash withdrawal.
**What's missing:** What the cash was spent on.
**Conservative default:** Exclude (no credit, no income).
**Question to ask:** "What was this cash withdrawal used for? Do you have receipts?"

### 6.5 Mixed purchases (convenience store — food and non-food)

**What it shows:** Single debit to convenience store (7-Eleven, Lawson, Family Mart).
**What's missing:** Proportion of food items (8%) vs. non-food (10%).
**Conservative default:** 10% (single rate) unless itemised receipt available.
**Question to ask:** "Do you have an itemised receipt showing which items were food vs. non-food?"

### 6.6 Supplier QIS registration status unconfirmed

**What it shows:** Purchase from a domestic supplier with no QIS number on record.
**What's missing:** Whether the supplier is QIS-registered.
**Conservative default:** Apply 80% transitional credit (through 30 Sep 2026) — flag as requiring confirmation.
**Question to ask:** "Can you provide the supplier's QIS registration number (T + 13 digits) from their invoice?"

---

## Section 7 — Excel working paper template

```
JAPAN CONSUMPTION TAX WORKING PAPER — 消費税計算書
Fiscal Year: 2025 / Entity: _______________

A. TAXABLE SALES (課税売上)
  A1. Standard rate 10% sales (net)           ___________
  A2. Reduced rate 8% sales (net)             ___________
  A3. Zero-rated exports (輸出)               ___________
  A4. Exempt sales (非課税売上)               ___________
  A5. Total sales (A1+A2+A3+A4)              ___________
  A6. Taxable ratio (A1+A2+A3) / A5           ___________%

B. OUTPUT TAX (課税標準額に対する消費税額)
  B1. Output JCT at 10% (A1 × 10/110)        ___________
  B2. Output JCT at 8% (A2 × 8/108)          ___________
  B3. Reverse charge output JCT               ___________
  B4. Total output JCT (B1+B2+B3)             ___________

C. INPUT TAX CREDIT (仕入税額控除)
  C1. Domestic purchases — 10% (net)          ___________
  C2. Domestic purchases — 8% (net)           ___________
  C3. Import purchases (net)                  ___________
  C4. Total input JCT (C1×10% + C2×8% + C3×10%)  _______
  C5. Reverse charge input credit             ___________
  C6. Transitional credit adjustments         ___________
  C7. Total input credit (C4+C5+C6)           ___________

D. NET CONSUMPTION TAX
  D1. Net national JCT (B4 − C7)              ___________
  D2. Local consumption tax (D1 × 22/78)      ___________
  D3. Total payable (D1 + D2)                 ___________
  D4. Interim payments deducted (中間申告)     ___________
  D5. Net payable / (refundable) (D3 − D4)    ___________

REVIEWER FLAGS:
  [ ] QIS registration numbers confirmed for all major suppliers?
  [ ] Eat-in vs. takeout split confirmed for food items?
  [ ] Reverse charge self-assessments documented?
  [ ] Transitional credits for non-QIS suppliers calculated?
  [ ] Taxable ratio computed for 95% rule check?
  [ ] Simplified tax method (簡易課税) applicable?
```

---

## Section 8 — Bank statement reading guide

### Common Japanese bank CSV formats

| Bank | CSV columns | Date format | Amount |
|---|---|---|---|
| みずほ銀行 (Mizuho) | 取引日, 摘要, 相手先, 備考, 入金, 出金, 残高 | YYYY年MM月DD日 | JPY integer |
| 三菱UFJ銀行 (MUFG) | 取引日付, 取引内容, お支払金額, お預り金額, 差引残高 | YYYY/MM/DD | JPY integer |
| 三井住友銀行 (SMBC) | 年月日, 摘要, 金額(出金), 金額(入金), 残高 | YYYY/MM/DD | JPY integer |
| ゆうちょ銀行 (Japan Post Bank) | 年月日, 取引内容, 出金, 入金, 残高 | YYYY.MM.DD | JPY integer |
| 楽天銀行 (Rakuten) | 取引日, 入出金種別, 摘要, 入金額, 出金額, 残高 | YYYY/MM/DD | JPY |
| SBI新生銀行 | 日付, 取引内容, お引き出し, お預け入れ, 残高 | YYYY/MM/DD | JPY |

### Key Japanese banking terms

| Japanese | Meaning | Classification hint |
|---|---|---|
| 振込入金 | Incoming wire transfer | Potential income |
| 引落 / 口座振替 | Direct debit | Potential expense |
| 振込出金 | Outgoing wire transfer | Potential expense |
| 利息 | Interest | Exempt — exclude |
| 手数料 | Fee/commission | Potentially exempt |
| 残高 | Balance | Running balance — ignore |
| 摘要 | Description/narrative | Key classification field |
| 相手先 | Counterparty | Key identification field |
| ATM出金 | ATM cash withdrawal | Tier 2 — ask |
| 定期振込 | Regular/standing transfer | Check if business expense |

---

## Section 9 — Onboarding fallback

If the client uploads a bank statement but cannot immediately answer all onboarding questions:

1. Classify all transactions using the pattern library (Section 3)
2. Apply conservative defaults from Section 1
3. Mark all Tier 2 items as "PENDING — reviewer must confirm"
4. Generate the working paper with flagged items
5. Ask only the following priority questions:

```
JAPAN JCT ONBOARDING — MINIMUM QUESTIONS
1. What is your QIS registration number? (T + 13 digits)
   If unregistered: confirm annual taxable sales are below JPY 10M
2. What is your fiscal year start and end date?
3. Are you using the simplified tax method (簡易課税)?
   If yes: what is your primary business category?
4. Do you make any exempt sales (e.g. residential rent, financial services)?
5. Any export sales to overseas clients? (zero-rated)
6. Are there any vehicle expenses? What is the business-use percentage?
7. Any mixed-rate convenience store purchases with itemised receipts?
```

Do not ask for information that can be inferred from the bank statement.

---

## Section 10 — Reference material

### Key legislation

| Topic | Reference |
|---|---|
| Consumption Tax Act | 消費税法 (Act No. 108 of 1988, as amended) |
| Standard rate | 消費税法 Article 29 |
| Reduced rate | 消費税法 附則第34条; 軽減税率制度 |
| Exemptions | 消費税法 Article 6; 別表第一 |
| Exports zero rate | 消費税法 Article 7 |
| Input tax credit | 消費税法 Articles 30–36 |
| QIS (qualified invoice) | 消費税法 Articles 57-2 to 57-4 |
| Simplified tax | 消費税法 Article 37 |
| Penalties | 国税通則法 (National Tax General Act) |
| Reverse charge (digital) | 消費税法 Article 28(2); 5% rule |

### Known gaps and escalation triggers

- 95% rule with proportional allocation methods (個別対応方式 / 一括比例配分方式) — escalate to zeirishi
- Real estate and construction long-term contracts — escalate
- Non-resident digital service providers' separate obligations — escalate
- Corporate group consolidated filing — escalate
- Transfer pricing adjustments — escalate

### Self-check before filing

- [ ] All QIS registration numbers recorded for input credits claimed
- [ ] Eat-in / takeout split resolved for all food items
- [ ] All export sales supported by evidence
- [ ] Reverse charge self-assessments included in return
- [ ] Transitional credits calculated for any non-QIS suppliers
- [ ] Simplified tax method elected? If yes, industry ratio applied
- [ ] Interim payment (中間申告) credited against total payable

### Changelog

| Version | Date | Change |
|---|---|---|
| 1.0 | 2024 | Initial release |
| 2.0 | April 2026 | Full v2.0 rewrite: supplier pattern library, worked examples, QIS update, no inline tier tags |

---

## Prohibitions

- NEVER allow input tax credit without confirming QIS invoice availability (post October 2023)
- NEVER classify eat-in restaurant meals at 8% — standard 10% applies
- NEVER claim input credit for exempt purchases (residential rent, financial services, medical)
- NEVER omit reverse charge self-assessment for B2B digital services from non-resident suppliers
- NEVER apply simplified tax method without confirming election (簡易課税選択届出書) was filed
- NEVER present calculations as definitive — always label as estimates and direct to a licensed zeirishi (税理士)

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a zeirishi 税理士 or equivalent) before filing or acting upon.

The most up-to-date version of this skill is maintained at openaccountants.com.
