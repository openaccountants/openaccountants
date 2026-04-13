---
name: china-vat
description: Use this skill whenever asked to prepare, review, or classify transactions for a China VAT (增值税 / VAT) return, handle Golden Tax System (金税系统) compliance, classify transactions for Chinese VAT purposes, or advise on VAT registration and filing in China. Trigger on phrases like "增值税", "VAT return China", "增值税申报", "增值税专用发票", "金税系统", "一般纳税人", "小规模纳税人", or any China VAT request. ALWAYS read this skill before touching any China VAT work.
version: 2.0
jurisdiction: CN
tax_year: 2025
category: international
depends_on:
  - vat-workflow-base
---

# China VAT (增值税) Skill v2.0

---

## Section 1 — Quick reference

| Field | Value |
|---|---|
| Country | People's Republic of China (中华人民共和国) |
| Tax | 增值税 (Zēngzhíshuì / Value Added Tax) |
| Currency | CNY (Renminbi 人民币 / RMB) only |
| Tax year | Calendar year (January–December) |
| Standard rate | 13% (goods, processing, repair, leasing of tangible assets) |
| Reduced rate 9% | Agricultural products, utilities, transport, construction, real estate, postal |
| Reduced rate 6% | Financial services, modern services (IT, consulting, R&D), telecom, consumer services |
| Zero rate | Exports of goods and services (出口零税率) |
| Small taxpayer rate | 3% (小规模纳税人 — currently partially reduced to 1% for some sectors) |
| Tax authority | 国家税务总局 State Taxation Administration (STA) |
| Filing portal | 电子税务局 (Online Tax Bureau — local provincial portals) |
| General taxpayer filing | Monthly or quarterly; due 15th of following month/quarter |
| Small taxpayer filing | Quarterly; due 15th of month following quarter |
| Registration threshold (general) | CNY 500,000/year (services); CNY 500,000/year (goods) for voluntary registration |
| Mandatory general taxpayer | Taxable sales > CNY 500,000 for service / CNY 500,000 for goods (verify current threshold) |
| e-Invoice | 电子发票 (全面推行 — fully rolled out; paper invoices being phased out) |
| Contributor | Open Accountants Community |
| Validated by | Pending — requires sign-off by a China-licensed 注册税务师 (CTA) or 注册会计师 (CPA) |
| Skill version | 2.0 |

### Key return form lines (增值税申报表)

| Line | Meaning |
|---|---|
| 1 | Taxable sales at 13% (应税货物及劳务) |
| 2 | Taxable sales at 9% |
| 3 | Taxable sales at 6% |
| 4 | Zero-rated sales (出口) |
| 5 | Exempt sales (免税) |
| 6 | Total output VAT (销项税额合计) |
| 7 | Total input VAT (进项税额合计) |
| 8 | Input VAT not deductible (进项税额转出) |
| 9 | Net input VAT available (7 − 8) |
| 10 | Net VAT payable (6 − 9) |
| 11 | VAT reduction/exemption credits |
| 12 | Excess credit carried forward |
| 13 | Net VAT payable after credits |

### Conservative defaults

| Ambiguity | Default |
|---|---|
| Unknown rate on a sale | 13% |
| Unknown whether general or small taxpayer | General taxpayer (一般纳税人) — more conservative |
| Unknown counterparty country | Domestic China |
| Unknown whether special or ordinary invoice | Ordinary invoice — no input credit |
| Unknown business-use % | 0% credit |
| Unknown whether digital service is B2B or B2C | B2C — no reverse charge |
| Unknown export documentation status | Not zero-rated — treat as domestic 13% |

### Red flag thresholds

| Threshold | Value |
|---|---|
| HIGH single transaction | CNY 200,000 |
| HIGH tax delta on single default | CNY 20,000 |
| MEDIUM counterparty concentration | >40% of output or input |
| MEDIUM conservative default count | >4 per period |
| LOW absolute net VAT position | CNY 100,000 |

---

## Section 2 — Required inputs and refusal catalogue

### Required inputs

**Minimum viable** — bank statement for the period in CSV, PDF, or pasted text. Confirmation of taxpayer category (一般纳税人 general or 小规模纳税人 small).

**Recommended** — 增值税专用发票 (special VAT invoices) for all input credits, 税号 (TIN — 纳税人识别号 18-digit), prior period return.

**Ideal** — complete invoice register from Golden Tax System (金税系统), asset register, full general ledger.

**Refusal if minimum is missing — SOFT WARN.** No bank statement = hard stop. Without special invoices: "Input VAT credits in China require 增值税专用发票 (special VAT invoices) verified through the Golden Tax System. All input credits are provisional pending invoice verification."

### Refusal catalogue

**R-CN-1 — Small taxpayer (小规模纳税人) claiming input credits.** "Small taxpayers cannot recover input VAT. They apply a simplified 3% rate on gross sales (or 1% under temporary relief). No input credit mechanism applies. This skill can calculate the simplified rate return but cannot process input credits."

**R-CN-2 — VAT exemption schemes.** "Certain industries have specific VAT exemption or reduction schemes (e.g., software enterprises, agriculture). These require specialist confirmation. Flag for review."

**R-CN-3 — Real estate and construction (cross-period projects).** "Long-term construction and real estate development projects have complex cross-period VAT rules. Out of scope — escalate to 注册税务师."

**R-CN-4 — Cross-border services without clear PE analysis.** "Services provided across the China border involving permanent establishment (PE) questions require specialist analysis. Out of scope."

**R-CN-5 — Export refund (出口退税).** "Export VAT refund claims require separate 出口退税申报 filings and customs documentation. Out of scope for this skill — escalate."

**R-CN-6 — Financial institutions.** "Banks and insurance companies have separate VAT calculation methods. Out of scope."

---

## Section 3 — Supplier pattern library

Match by case-insensitive substring on counterparty name or transaction reference. Most specific match wins. Fall through to Section 5 if no match.

### 3.1 Chinese banks — fees and charges (exempt / exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| 工商银行, ICBC, 中国工商银行 | EXCLUDE (fee lines) | Bank charges — exempt financial service |
| 建设银行, CCB, 中国建设银行 | EXCLUDE (fee lines) | Same |
| 农业银行, ABC, 中国农业银行 | EXCLUDE (fee lines) | Same |
| 中国银行, BOC, BANK OF CHINA | EXCLUDE (fee lines) | Same |
| 交通银行, BOCOM, 交通银行股份 | EXCLUDE (fee lines) | Same |
| 招商银行, CMB, CHINA MERCHANTS | EXCLUDE (fee lines) | Same |
| 浦发银行, SPDB | EXCLUDE (fee lines) | Same |
| 中信银行, CITIC BANK | EXCLUDE (fee lines) | Same |
| 手续费, 银行手续费 | EXCLUDE | Bank transaction fee — exempt |
| 利息, 利息收入, INTEREST | EXCLUDE | Interest — exempt from VAT |

### 3.2 Digital payment platforms (exclude platform fees)

| Pattern | Treatment | Notes |
|---|---|---|
| 支付宝, ALIPAY | EXCLUDE (fee lines) | Payment processing — exempt |
| 微信支付, WECHAT PAY, 财付通 | EXCLUDE (fee lines) | Same |
| 云闪付, UNIONPAY | EXCLUDE (fee lines) | Same |
| 京东支付, JD PAY | EXCLUDE (fee lines) | Same |

### 3.3 Chinese government and statutory (exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| 国家税务总局, 税务局, STA | EXCLUDE | Tax payment — not a supply |
| 增值税, 企业所得税, 个人所得税 | EXCLUDE | Tax remittance |
| 社会保险, 社保, SOCIAL INSURANCE | EXCLUDE | Statutory contribution |
| 公积金, 住房公积金 | EXCLUDE | Housing provident fund |
| 海关, 关税, CUSTOMS | EXCLUDE | Customs duty (but import VAT handled separately) |
| 工商局, 市场监管 | EXCLUDE | Registration fees — government sovereign acts |

### 3.4 Chinese utilities (taxable)

| Pattern | Treatment | Rate | Notes |
|---|---|---|---|
| 国家电网, STATE GRID, 国网 | Input 9% | 9% | Electricity — reduced rate |
| 南方电网, CSG, 南网 | Input 9% | 9% | Electricity — reduced rate |
| 中国石油, CNPC, 中石油, PETROCHINA | Input 9%/13% | 9%/13% | Gas distribution 9%; crude/refined 13% |
| 中国石化, SINOPEC, 中石化 | Input 13% | 13% | Fuel — standard rate |
| 城市燃气, 天然气公司 | Input 9% | 9% | Gas — reduced rate |
| 自来水, 供水公司 | Input 9% | 9% | Water — reduced rate |
| 中国移动, CHINA MOBILE, 移动通信 | Input 6% | 6% | Telecom — modern services rate |
| 中国联通, CHINA UNICOM | Input 6% | 6% | Telecom — modern services rate |
| 中国电信, CHINA TELECOM | Input 6% | 6% | Telecom — modern services rate |

### 3.5 Transport and logistics (taxable)

| Pattern | Treatment | Rate | Notes |
|---|---|---|---|
| 顺丰速运, SF EXPRESS, 顺丰控股 | Input 9% | 9% | Domestic transport — reduced rate |
| 京东物流, JD LOGISTICS | Input 9% | 9% | Transport — reduced rate |
| 中通快递, ZTO EXPRESS | Input 9% | 9% | Transport — reduced rate |
| 圆通快递, YTO EXPRESS | Input 9% | 9% | Transport — reduced rate |
| 申通快递, STO EXPRESS | Input 9% | 9% | Transport — reduced rate |
| 韵达快递, YUNDA EXPRESS | Input 9% | 9% | Transport — reduced rate |
| 邮政EMS, CHINA POST EMS | Input 9% | 9% | Postal transport — reduced rate |
| 滴滴出行, DIDI | Input 6% | 6% | Ride-hailing — modern service rate |
| 中国国航, AIR CHINA, 国航 | Input 9%/0% | 9%/0% | Domestic 9%; international 0% |
| 中国东航, CHINA EASTERN | Input 9%/0% | 9%/0% | Same |
| 南方航空, CHINA SOUTHERN | Input 9%/0% | 9%/0% | Same |
| 高铁, 铁路, CHINA RAILWAY, 中国铁路 | Input 9% | 9% | Rail transport — reduced rate |

### 3.6 Food and retail (taxable)

| Pattern | Treatment | Rate | Notes |
|---|---|---|---|
| 盒马, HEMA FRESH, 盒马鲜生 | Input 9% (food) | 9% | Fresh food retail — agricultural reduced rate |
| 美团, MEITUAN (food delivery) | Input 9% | 9% | Food delivery — reduced rate for food items |
| 饿了么, ELEME | Input 9% | 9% | Food delivery — reduced rate |
| 大润发, RT-MART | Input 13%/9% | Mixed | Non-food 13%; food 9% |
| 沃尔玛, WALMART CHINA | Input 13%/9% | Mixed | Same |
| 家乐福, CARREFOUR CHINA | Input 13%/9% | Mixed | Same |
| 永辉超市, YONGHUI | Input 9% (grocery) | 9% | Food supermarket |

### 3.7 SaaS — Chinese suppliers (modern services 6%)

| Pattern | Treatment | Rate | Notes |
|---|---|---|---|
| 用友网络, YONYOU | Input 6% | 6% | Chinese ERP — modern services |
| 金蝶软件, KINGDEE | Input 6% | 6% | Chinese accounting software |
| 钉钉, DINGTALK | Input 6% | 6% | Alibaba groupware |
| 企业微信, WECHAT WORK | Input 6% | 6% | Tencent enterprise tool |
| 阿里云, ALIBABA CLOUD | Input 6% | 6% | Cloud services — modern services |
| 腾讯云, TENCENT CLOUD | Input 6% | 6% | Cloud services |
| 华为云, HUAWEI CLOUD | Input 6% | 6% | Cloud services |
| 百度智能云, BAIDU CLOUD | Input 6% | 6% | Cloud services |

### 3.8 SaaS — international suppliers (note: many blocked in China)

| Pattern | Treatment | Notes |
|---|---|---|
| GOOGLE (Search, Workspace, Ads) | BLOCKED in China | Google services not available without VPN — flag if appearing |
| FACEBOOK, META ADS | BLOCKED in China | Not available — flag if appearing |
| TWITTER, X | BLOCKED in China | Not available — flag if appearing |
| MICROSOFT (365, Azure) | Input 6% via China entity | Microsoft operates via local China entity — standard 6% VAT invoiced |
| MICROSOFT 中国 | Input 6% | Microsoft (China) Co. Ltd. — modern services |
| SAP CHINA | Input 6% | SAP licensed via China entity |
| ORACLE CHINA | Input 6% | Same |
| ADOBE (China entity) | Input 6% | If via China entity — check invoice |

### 3.9 Internal transfers and exclusions

| Pattern | Treatment | Notes |
|---|---|---|
| 内部转账, 账户间转账 | EXCLUDE | Internal transfer |
| 借款, 贷款, 还款 | EXCLUDE | Loan principal |
| 工资, 薪资, 薪酬 | EXCLUDE | Payroll — out of VAT scope |
| 股利, 分红, DIVIDEND | EXCLUDE | Dividend — out of VAT scope |
| 押金, 保证金 | EXCLUDE | Deposit — out of VAT scope until applied |

---

## Section 4 — Worked examples

Six classifications from a hypothetical bank statement of a Shanghai-based IT consulting firm. Format: 招商银行 (CMB) CSV export.

### Example 1 — Domestic B2B service revenue (6%)

**Input line:**
`2025-04-15  转账收入  北京科技有限公司  发票号: INV-2025-041  +530,000.00  CNY`

**Reasoning:**
Incoming CNY 530,000 from a Beijing company for IT consulting. IT consulting is a "modern service" (现代服务) taxed at 6%. If the invoice is CNY 530,000 gross: net = CNY 500,000 (销项税基) + CNY 30,000 output VAT (6%). The 增值税专用发票 must be issued through the Golden Tax System showing the 6% rate. Report on line 3 (6% sales).

**Classification:** Output VAT at 6% — CNY 30,000. Net sales: CNY 500,000.

### Example 2 — Goods purchase (13%, input credit requires special invoice)

**Input line:**
`2025-04-10  转账支出  联想集团有限公司  采购笔记本电脑10台  -113,000.00  CNY`

**Reasoning:**
Purchase of 10 laptops from Lenovo. Goods at standard rate 13%. Gross CNY 113,000. Net = CNY 100,000 + CNY 13,000 input VAT. Input credit of CNY 13,000 available ONLY if a valid 增值税专用发票 (special VAT invoice) is obtained from Lenovo and verified in the Golden Tax System. If only an ordinary invoice (普通发票) is held, no input credit.

**Classification:** Input VAT 13% — CNY 13,000 (provisional, pending special invoice verification).

### Example 3 — Export services (zero-rated)

**Input line:**
`2025-04-22  外汇收入  ACME CORPORATION USA  技术服务费 Q1 2025  +700,000.00  CNY`

**Reasoning:**
Incoming CNY 700,000 (USD equivalent) from a US company for technical services. If the service qualifies as "exported services" (completely consumed outside China, provided to a foreign entity), it is zero-rated. Evidence required: signed contract, foreign payment records, proof service was consumed abroad. Report on line 4 (zero-rated). If export qualification uncertain — apply 6% default until confirmed.

**Classification:** Zero-rated export sales — CNY 700,000. Output VAT: CNY 0 (if confirmed). Conservative default: 6% (CNY 42,000) pending confirmation.

### Example 4 — Freight/logistics (9% reduced rate)

**Input line:**
`2025-04-08  转账支出  顺丰速运股份有限公司  快递费 2025年3月  -9,540.00  CNY`

**Reasoning:**
Payment to SF Express for domestic courier services. Transport is taxed at 9% reduced rate. Gross CNY 9,540. Net = CNY 8,752 + CNY 788 input VAT at 9%. Input credit requires a special invoice (增值税专用发票) from SF Express — they are a QIS equivalent registered supplier.

**Classification:** Input VAT 9% — CNY 788. Net expense: CNY 8,752.

### Example 5 — Cloud services from Chinese provider (6%)

**Input line:**
`2025-04-01  代扣  阿里云计算有限公司  云服务器费用 2025-04  -10,600.00  CNY`

**Reasoning:**
Monthly cloud hosting from Alibaba Cloud (阿里云). Cloud/IT services = modern services at 6%. CNY 10,600 gross. Net = CNY 10,000 + CNY 600 input VAT. Alibaba Cloud issues 增值税专用发票 — input credit available. Fully deductible for income tax purposes as well.

**Classification:** Input VAT 6% — CNY 600. Net expense: CNY 10,000.

### Example 6 — Payroll (outside VAT scope)

**Input line:**
`2025-04-25  工资发放  员工薪酬  2025年4月工资  -850,000.00  CNY`

**Reasoning:**
Payroll payment. Wages and salaries are outside VAT scope entirely — not a supply of goods or services. No VAT input or output. EXCLUDE from the VAT return. This will appear in income tax calculations but not VAT.

**Classification:** EXCLUDE from VAT return entirely. Out of scope (不征税).

---

## Section 5 — Tier 1 rules (compressed)

### 5.1 Standard rate 13%

Default rate for taxable supply of goods, processing, repair and replacement services, and leasing of tangible movable property. Legislation: VAT Law (增值税法) Article 2; 财税[2016]36号.

### 5.2 Reduced rate 9%

Agricultural products (农产品), tap water, heating, cooling, gas, coal (household), books/newspapers, animal feed, agricultural machinery, fertilizer; transport services; postal services; construction and real estate. Legislation: 增值税税率 Schedule; 财税[2016]36号 附件1.

### 5.3 Reduced rate 6%

Financial services (金融服务), modern services (现代服务: IT, consulting, R&D, advertising, design, logistics support), telecom services, life services (生活服务: catering, accommodation, tourism, entertainment, consumer services). Legislation: 财税[2016]36号.

### 5.4 Zero rate — exports

Exports of goods and eligible exported services (完全在境外消费 — consumed entirely outside China). Evidence: customs export declaration for goods; contracts and payment proof for services. Legislation: 增值税法 Article 2(3).

### 5.5 Exempt supplies

Medical and healthcare, education, childcare, elderly care, financial services (some), cultural services, residential rent, certain agricultural self-produced goods. No output VAT; no input credit on exempt revenues. Legislation: 增值税法 Article 13; 营改增 exemption list.

### 5.6 Input VAT credit rules

Input VAT is deductible only when:
- A valid 增值税专用发票 (or customs import VAT certificate) is held
- The invoice is verified in the Golden Tax System (金税系统)
- The purchase relates to taxable (not exempt) business activities
- Invoice is within the 360-day certification window

Ordinary invoices (普通发票) do NOT generate input credits.

### 5.7 Small taxpayer (小规模纳税人) simplified calculation

Rate: 3% on gross sales (currently reduced to 1% for some sectors — verify current policy). No input credit. No special invoices issued (only ordinary invoices unless authorised). Filing: quarterly. Gross sales × 3% (or 1%) = VAT payable.

### 5.8 Filing deadlines

| Filer type | Period | Due date |
|---|---|---|
| General taxpayer (monthly) | Monthly | 15th of following month |
| General taxpayer (quarterly) | Quarterly | 15th of month following quarter |
| Small taxpayer | Quarterly | 15th of month following quarter |
| Annual reconciliation | Calendar year | 31 March following year |

### 5.9 Penalties

| Offence | Penalty |
|---|---|
| Late filing | CNY 2,000–10,000 fine |
| Late payment (滞纳金) | 0.05% per day of unpaid tax |
| Understatement | 50%–500% of tax evaded |
| False invoicing (虚开发票) | Criminal liability possible |

---

## Section 6 — Tier 2 catalogue

### 6.1 Export service qualification (境外消费确认)

**What it shows:** Revenue from a foreign client.
**What's missing:** Whether the service was consumed entirely outside China (required for zero-rating).
**Conservative default:** 6% domestic rate.
**Question to ask:** "Was this service fully consumed outside China? Can you provide the contract and evidence that the service output was used abroad?"

### 6.2 Mixed-rate retail purchases (supermarket)

**What it shows:** Supermarket debit (Walmart, Carrefour, RT-Mart China).
**What's missing:** Split between food items (9%) and non-food (13%).
**Conservative default:** 13% (standard rate).
**Question to ask:** "Do you have the itemised receipt showing food vs. non-food items?"

### 6.3 Invoice type — special vs. ordinary

**What it shows:** Payment to a supplier.
**What's missing:** Whether a 增值税专用发票 (special) or 普通发票 (ordinary) was received.
**Conservative default:** No input credit (assume ordinary invoice).
**Question to ask:** "Did you receive a 增值税专用发票 from this supplier, verified in the Golden Tax System?"

### 6.4 Foreign SaaS / tech services (non-blocked)

**What it shows:** Payment to an international software company accessible in China (Microsoft, Oracle, SAP via China entity).
**What's missing:** Whether invoice is from China local entity (6% VAT invoiced) or foreign entity (withholding tax / no VAT credit).
**Conservative default:** No input credit until invoice confirmed.
**Question to ask:** "Is the invoice from a Chinese registered entity? Does it show a Chinese 税号 (TIN)?"

### 6.5 Partial exempt proration

**What it shows:** Business makes both taxable and exempt sales.
**What's missing:** The proration ratio for input VAT allocation.
**Conservative default:** 0% credit on shared costs.
**Question to ask:** "What proportion of your sales are taxable vs. exempt? Provide monthly breakdown."

---

## Section 7 — Excel working paper template

```
CHINA VAT WORKING PAPER — 增值税计算表
Period: ____________  Entity: ____________  TIN: ____________

A. OUTPUT VAT (销项税额)
  A1. Sales at 13% (net)                      ___________
  A2. Sales at 9% (net)                       ___________
  A3. Sales at 6% (net)                       ___________
  A4. Zero-rated exports (net)                ___________
  A5. Exempt sales (net)                      ___________
  A6. Total output VAT (A1×13% + A2×9% + A3×6%)  _______

B. INPUT VAT (进项税额)
  B1. Purchases — special invoices 13% (net)  ___________
  B2. Purchases — special invoices 9% (net)   ___________
  B3. Purchases — special invoices 6% (net)   ___________
  B4. Import VAT certificates (net)           ___________
  B5. Total input VAT (B1×13% + B2×9% + B3×6% + B4)  ____
  B6. Input VAT not deductible (转出)         ___________
  B7. Net input VAT (B5 − B6)                 ___________

C. NET VAT PAYABLE
  C1. Net VAT (A6 − B7)                       ___________
  C2. VAT reduction credits                   ___________
  C3. Prior period excess credit              ___________
  C4. Net payable / (refund) (C1 − C2 − C3)  ___________

REVIEWER FLAGS:
  [ ] All special invoices verified in Golden Tax System?
  [ ] Export qualification confirmed for zero-rated sales?
  [ ] Small taxpayer threshold check (CNY 500,000)?
  [ ] Any blocked/international SaaS invoice type confirmed?
  [ ] Proration calculated for any exempt sales?
```

---

## Section 8 — Bank statement reading guide

### Common Chinese bank CSV formats

| Bank | Key columns | Date format | Amount format |
|---|---|---|---|
| 招商银行 CMB | 交易日期, 摘要, 交易金额, 账户余额 | YYYY-MM-DD | CNY with 2 decimals |
| 工商银行 ICBC | 记账日期, 交易摘要, 收入金额, 支出金额, 账户余额 | YYYYMMDD | CNY |
| 建设银行 CCB | 记账日期, 对方户名, 交易金额, 余额 | YYYY-MM-DD | CNY |
| 中国银行 BOC | 交易日期, 摘要, 贷方金额, 借方金额, 余额 | YYYY/MM/DD | CNY |
| 支付宝 Alipay | 交易时间, 交易对方, 商品说明, 收/支, 金额 | YYYY-MM-DD HH:MM | CNY |
| 微信支付 WeChat | 交易时间, 交易类型, 交易对方, 金额 | YYYY-MM-DD HH:MM:SS | CNY |

### Key Chinese banking terms

| Chinese | Meaning | Classification hint |
|---|---|---|
| 转账收入 | Incoming transfer | Potential revenue |
| 转账支出 | Outgoing transfer | Potential expense |
| 代扣 | Direct debit / auto-deduction | Subscription expense |
| 手续费 | Handling fee | Bank charge — exempt |
| 利息 | Interest | Exempt |
| 余额 | Balance | Running balance — ignore |
| 摘要 | Description/narrative | Key classification field |
| 对方户名 | Counterparty name | Key identification field |
| 外汇收入 | Foreign currency receipt | Potential export |
| 工资发放 | Payroll disbursement | Out of VAT scope |

---

## Section 9 — Onboarding fallback

If the client provides a bank statement but cannot immediately answer all questions:

1. Classify using the pattern library (Section 3)
2. Apply conservative defaults (Section 1)
3. Mark all Tier 2 items as "PENDING — reviewer must confirm"
4. Generate working paper with flags

```
CHINA VAT ONBOARDING — MINIMUM QUESTIONS
1. Are you a 一般纳税人 (general taxpayer) or 小规模纳税人 (small taxpayer)?
2. Your 纳税人识别号 (TIN / 18-digit tax registration number)?
3. Filing frequency: monthly or quarterly?
4. Do you make any export sales (zero-rated)?
   If yes: do you have customs declarations or foreign payment evidence?
5. Do you make any exempt sales (e.g. financial services, residential rent)?
6. For all large purchases: do you hold 增值税专用发票 verified in 金税系统?
7. Any international SaaS subscriptions? Which ones and are invoices from China entities?
```

---

## Section 10 — Reference material

### Key legislation

| Topic | Reference |
|---|---|
| VAT Law | 增值税法 (effective 2026) / 增值税暂行条例 (Provisional Regulations) |
| VAT rates | 财税[2016]36号; 财税[2018]32号 (rate reductions) |
| Exemptions | 增值税法 Article 13 |
| Input credit rules | 增值税法 Article 14; 财税[2016]36号 附件1 |
| Export zero-rating | 增值税法 Article 2(3); 财税[2012]196号 |
| e-Invoice | 税总发[2020]124号; 全面推行 nationwide rollout circulars |
| Small taxpayer | 增值税法 Article 17; 小规模纳税人免税政策 |
| Penalties | 税收征管法 (Tax Collection Administration Law) |

### Known gaps

- VAT refund for exporters (出口退税) — out of scope; requires separate filing
- Real estate and construction cross-period rules — escalate
- Financial institution simplified VAT — escalate
- Transfer pricing adjustments affecting VAT base — escalate
- Cultural/media VAT exemptions — verify current policy

### Self-check before filing

- [ ] All special invoices (专用发票) verified in Golden Tax System
- [ ] Export sales supported by customs/payment evidence
- [ ] Small taxpayer threshold confirmed
- [ ] Input VAT not deductible (转出) calculated for exempt activities
- [ ] Prior period excess credit applied correctly

### Changelog

| Version | Date | Change |
|---|---|---|
| 1.0 | 2024 | Initial release |
| 2.0 | April 2026 | Full v2.0 rewrite: pattern library, worked examples, no inline tier tags |

---

## Prohibitions

- NEVER claim input credit from an ordinary invoice (普通发票) — special invoice required
- NEVER apply 13% to transport or agricultural services — these are 9%
- NEVER apply 6% to goods sales — goods are 13% (or 9% for agricultural)
- NEVER allow small taxpayer (小规模) to claim input credits
- NEVER zero-rate a service without confirming it was consumed entirely outside China
- NEVER present calculations as definitive — direct to a 注册税务师 (CTA) for confirmation

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes. All outputs must be reviewed by a qualified professional (注册税务师 or 注册会计师) before filing.

The most up-to-date version is maintained at openaccountants.com.
