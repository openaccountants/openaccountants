---
name: taiwan-vat
description: Use this skill whenever asked to prepare, review, or classify transactions for a Taiwan Business Tax (營業稅) return, handle uniform invoice (統一發票) compliance, or advise on VAT registration and filing in Taiwan. Trigger on phrases like "營業稅", "Taiwan business tax", "統一發票", "uniform invoice", "401 return", "403 return", "申報營業稅", or any Taiwan VAT/business tax request. ALWAYS read this skill before touching any Taiwan business tax work.
version: 2.0
jurisdiction: TW
tax_year: 2025
category: international
depends_on:
  - vat-workflow-base
---

# Taiwan Business Tax (營業稅) Skill v2.0

---

## Section 1 — Quick reference

| Field | Value |
|---|---|
| Country | Taiwan (中華民國 / Republic of China) |
| Tax | 營業稅 (Yíngyèshuì — Business Tax / VAT) |
| Currency | NTD (New Taiwan Dollar / 新台幣 NT$) |
| Tax year | Calendar year (1 Jan – 31 Dec) |
| Standard rate | 5% |
| Zero rate | 0% (exports, services to foreign businesses paid in foreign currency) |
| Exempt | Medical, education, land sales, financial services (banking interest, insurance premiums), small businesses below threshold |
| Registration threshold | NTD 480,000/year (goods); NTD 240,000/year (services) for small business; above = mandatory general registration |
| Small business (小規模營業人) | Monthly revenue < NTD 80,000 (goods) / NTD 40,000 (services) — special simplified tax |
| Tax authority | 財政部國稅局 (Ministry of Finance — National Tax Administration / NTA) |
| Return form | 401 (bi-monthly, general taxpayers); 403 (quarterly, small business) |
| Filing portal | eTax (https://www.etax.nat.gov.tw) |
| Filing frequency | Bi-monthly (每兩個月申報一次) for most; quarterly for small |
| Deadline | 15th of month following reporting period (e.g., Jan–Feb period → 15 March) |
| Uniform invoice (統一發票) | Mandatory for B2B and B2C; government-issued invoice numbers |
| Contributor | Open Accountants Community |
| Validated by | Pending — requires sign-off by a Taiwan-licensed 會計師 (CPA) |
| Skill version | 2.0 |

### Key 401 return boxes

| Box | Meaning |
|---|---|
| 401-1 | Sales amount — taxable at 5% (課稅銷售額) |
| 401-2 | Output tax at 5% (銷項稅額) |
| 401-3 | Zero-rated sales (零稅率銷售額) |
| 401-4 | Exempt sales (免稅銷售額) |
| 401-5 | Total input tax (進項稅額合計) |
| 401-6 | Disallowed input tax (不得扣抵進項稅額) |
| 401-7 | Net input tax (進項稅額 − 不得扣抵) |
| 401-8 | Tax payable (應納稅額 = 401-2 − 401-7) |
| 401-9 | Excess credit carried forward (留抵稅額) |
| 401-10 | Net payable after prior credit |

### Conservative defaults

| Ambiguity | Default |
|---|---|
| Unknown rate on a sale | 5% |
| Unknown counterparty country | Domestic Taiwan |
| Unknown B2B vs B2C for foreign customer | B2C — charge 5% |
| Unknown business-use % (vehicle, phone) | 0% credit |
| Unknown invoice type | No input credit until uniform invoice confirmed |
| Unknown whether exempt or taxable service | Taxable at 5% |
| Unknown export documentation | Not zero-rated — 5% default |

### Red flag thresholds

| Threshold | Value |
|---|---|
| HIGH single transaction | NTD 300,000 |
| HIGH tax delta on single default | NTD 15,000 |
| MEDIUM counterparty concentration | >40% of output or input |
| MEDIUM conservative default count | >4 per period |
| LOW absolute net tax position | NTD 100,000 |

---

## Section 2 — Required inputs and refusal catalogue

### Required inputs

**Minimum viable** — bank statement for the bi-monthly period in CSV, PDF, or pasted text. Confirmation of taxpayer type (general 一般 or small business 小規模).

**Recommended** — uniform invoices (統一發票) for all sales, purchase invoices for all input credits claimed above NTD 10,000, business registration certificate (統一編號 8-digit business ID).

**Ideal** — complete invoice register, 進項憑證 (input vouchers), prior period return and credit carried forward (留抵稅額), export documentation.

**Refusal if minimum missing — SOFT WARN.** No bank statement = hard stop. "Input tax credits require uniform invoices (統一發票 or 電子發票). All credits are provisional pending invoice confirmation."

### Refusal catalogue

**R-TW-1 — Small business (小規模) with input credit claims.** "Small businesses (小規模營業人) are taxed on a simplified basis and cannot claim input credits. They file quarterly using Form 403 and pay a deemed tax on purchases. This skill can compute the simplified tax but cannot process input credits for small businesses."

**R-TW-2 — Special industry taxpayers.** "Banks, insurance companies, and certain financial institutions have different business tax calculation methods. Out of scope."

**R-TW-3 — Partial exemption proration.** "If the business makes both taxable and exempt sales and cannot clearly allocate input tax, a proration (比例扣抵) is required. Out of scope without the annual ratio — escalate to a 會計師."

**R-TW-4 — Cross-border electronic services (B2C).** "Foreign businesses providing electronic services to Taiwan consumers (B2C) must register under the special e-services regime. Out of scope for domestic filing."

**R-TW-5 — Land transactions.** "Sales of land are exempt from business tax. If this forms a significant portion of transactions, proration rules apply — escalate."

---

## Section 3 — Supplier pattern library

Match by case-insensitive substring on counterparty or reference. Most specific match wins. Fall through to Section 5 if no match.

### 3.1 Taiwanese banks — fees and charges (exempt / exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| 中華郵政, CHUNGHWA POST BANK | EXCLUDE (fee lines) | Banking — exempt financial service |
| 台灣銀行, BANK OF TAIWAN, BOT | EXCLUDE (fee lines) | Same |
| 合作金庫, TAIWAN COOPERATIVE BANK, TCB | EXCLUDE (fee lines) | Same |
| 第一銀行, FIRST COMMERCIAL BANK | EXCLUDE (fee lines) | Same |
| 兆豐銀行, MEGA BANK, MEGA INTERNATIONAL | EXCLUDE (fee lines) | Same |
| 玉山銀行, E.SUN BANK | EXCLUDE (fee lines) | Same |
| 國泰世華, CATHAY UNITED BANK | EXCLUDE (fee lines) | Same |
| 富邦銀行, TAIPEI FUBON BANK | EXCLUDE (fee lines) | Same |
| 永豐銀行, SINOPAC BANK | EXCLUDE (fee lines) | Same |
| 中信銀行, CTBC BANK, 中國信託 | EXCLUDE (fee lines) | Same |
| 手續費, 帳管費, 匯費 | EXCLUDE | Bank fees — exempt |
| 利息, 利息收入 | EXCLUDE | Interest — exempt |

### 3.2 Taiwanese government and statutory (exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| 財政部, 國稅局, NTA | EXCLUDE | Tax payment — not a supply |
| 營業稅, 綜所稅, 所得稅 | EXCLUDE | Tax remittance |
| 勞保, 健保, 勞工保險, 全民健康保險 | EXCLUDE | Social insurance — out of scope |
| 勞動部, 勞工局 | EXCLUDE | Government authority fees |
| 公路監理, 地方稅 | EXCLUDE | Licensing/local tax — not a supply |
| 中華民國專利局, 智財局 | EXCLUDE | Government IP fees |

### 3.3 Taiwanese utilities (taxable at 5%)

| Pattern | Treatment | Rate | Notes |
|---|---|---|---|
| 台灣電力, TAIWAN POWER, TAIPOWER | Input 5% | 5% | Electricity — taxable |
| 台灣自來水, TAIWAN WATER | Input 5% | 5% | Water — taxable |
| 中華電信, CHUNGHWA TELECOM, CHT | Input 5% | 5% | Telecom/broadband — taxable |
| 台灣大哥大, TAIWAN MOBILE | Input 5% | 5% | Mobile — taxable |
| 遠傳電信, FAR EASTONE | Input 5% | 5% | Mobile — taxable |
| 台灣之星, TAIWAN STAR (now TWM) | Input 5% | 5% | Mobile — taxable |
| 台灣固網, TFIX | Input 5% | 5% | Fixed-line — taxable |

### 3.4 Transport and logistics (taxable at 5%)

| Pattern | Treatment | Rate | Notes |
|---|---|---|---|
| 台灣高鐵, THSR, 高鐵 | Input 5% | 5% | High-speed rail — taxable |
| 台灣鐵路, TRA, 台鐵 | Input 5% | 5% | Rail — taxable |
| 台北捷運, TAIPEI MRT, 北捷 | Input 5% | 5% | Metro — taxable |
| 高雄捷運, KAOHSIUNG MRT | Input 5% | 5% | Metro — taxable |
| 統聯客運, UBUS | Input 5% | 5% | Long-distance bus — taxable |
| 中華航空, CHINA AIRLINES, CAL | Check route | 0%/5% | International 0%; domestic 5% |
| 長榮航空, EVA AIR | Check route | 0%/5% | Same |
| 黑貓宅急便, YAMATO TAIWAN | Input 5% | 5% | Domestic courier — taxable |
| 新竹物流, HSINCHU TRANSPORT | Input 5% | 5% | Domestic freight — taxable |
| 大榮貨運, GREAT WALL TRANSPORT | Input 5% | 5% | Freight — taxable |
| 台灣宅配通, TAIWAN DELIVERY | Input 5% | 5% | Courier — taxable |

### 3.5 Food and retail

| Pattern | Treatment | Rate | Notes |
|---|---|---|---|
| 7-ELEVEN TAIWAN, 統一超商 | Input 5% | 5% | Retail — taxable (food included at 5%) |
| 全家便利商店, FAMILY MART TAIWAN | Input 5% | 5% | Same |
| 萊爾富, HI-LIFE | Input 5% | 5% | Same |
| OK MART | Input 5% | 5% | Same |
| 全聯福利中心, PX MART | Input 5% | 5% | Supermarket — taxable |
| 大潤發, RT-MART TAIWAN | Input 5% | 5% | Hypermarket — taxable |
| 家樂福, CARREFOUR TAIWAN | Input 5% | 5% | Hypermarket — taxable |
| 愛買, JASON'S | Input 5% | 5% | Supermarket — taxable |
| 餐廳, 飲食 (eat-in) | Input 5% | 5% | Restaurant meals — taxable (no exemption for food in Taiwan) |

### 3.6 SaaS — local Taiwanese suppliers (5%)

| Pattern | Treatment | Rate | Notes |
|---|---|---|---|
| 104人力銀行, 104 JOB BANK | Input 5% | 5% | HR platform — taxable |
| 1111人力銀行 | Input 5% | 5% | HR platform — taxable |
| 鼎新電腦, DIGIWIN | Input 5% | 5% | Taiwanese ERP — taxable |
| 資通電腦, ARES | Input 5% | 5% | Taiwanese software — taxable |
| LINE (Taiwan entity) | Input 5% | 5% | If billed via Taiwan entity |

### 3.7 SaaS — international suppliers (reverse charge consideration)

Taiwan imposes business tax on cross-border electronic services to Taiwan businesses. The foreign supplier should register or the Taiwan buyer may need to self-assess.

| Pattern | Billing entity | Treatment | Notes |
|---|---|---|---|
| GOOGLE (Workspace, Ads, Cloud) | Google Asia Pacific (SG) | Reverse charge 5% | Foreign electronic service — self-assess |
| MICROSOFT (365, Azure) | Microsoft Taiwan or regional | Check invoice | If Taiwan entity: 5% on invoice; if foreign: self-assess |
| ADOBE | Adobe Systems (US/SG) | Reverse charge 5% | Foreign service |
| META, FACEBOOK ADS | Meta Platforms | Reverse charge 5% | Foreign service |
| SLACK | Salesforce/Slack (US) | Reverse charge 5% | Foreign service |
| ZOOM | Zoom Video (US) | Reverse charge 5% | Foreign service |
| NOTION | Notion Labs (US) | Reverse charge 5% | Foreign service |
| ANTHROPIC, CLAUDE | Anthropic (US) | Reverse charge 5% | Foreign service |
| OPENAI, CHATGPT | OpenAI (US) | Reverse charge 5% | Foreign service |
| GITHUB | GitHub/Microsoft | Check entity | If via Taiwan entity: 5%; if US: reverse charge |
| AWS | AWS Asia Pacific (SG) | Reverse charge 5% | Singapore entity — foreign service |

### 3.8 Payment processors (exempt fees)

| Pattern | Treatment | Notes |
|---|---|---|
| STRIPE (transaction fees) | EXCLUDE | Payment processing — exempt financial service |
| PAYPAL (fees) | EXCLUDE | Same |
| LINE PAY 手續費 | EXCLUDE | Same |
| 街口支付, JKOPAY 手續費 | EXCLUDE | Same |

### 3.9 Internal transfers and exclusions

| Pattern | Treatment | Notes |
|---|---|---|
| 帳戶轉帳, 內部轉帳 | EXCLUDE | Internal movement |
| 借款, 還款, 貸款 | EXCLUDE | Loan principal — out of scope |
| 薪資, 工資 | EXCLUDE | Payroll — outside business tax scope |
| 股利, 股息 | EXCLUDE | Dividend — outside scope |
| 押金, 保證金 | EXCLUDE | Deposit — out of scope until applied |
| ATM提款 | Tier 2 — ask | Default exclude; ask purpose |

---

## Section 4 — Worked examples

Six classifications from a hypothetical Taipei-based IT consultant. Format: 玉山銀行 (E.SUN Bank) CSV.

### Example 1 — Domestic B2B revenue (5%)

**Input line:**
`2025/04/15  轉帳收入  中信工程顧問股份有限公司  統一發票: WX12345678  +525,000  NT$`

**Reasoning:**
Incoming NTD 525,000 from a Taiwan company for IT consulting. Business tax at 5%. Gross NTD 525,000 includes 5% tax. Net = NTD 500,000 (課稅銷售額) + NTD 25,000 output tax. A uniform invoice (統一發票) must be issued with the 8-digit business number of the buyer. Report on Form 401 box 401-1.

**Classification:** Output tax 5% — NTD 25,000. Net sales: NTD 500,000.

### Example 2 — Export service (zero-rated, paid in foreign currency)

**Input line:**
`2025/04/22  外匯入款  ACME CORPORATION USA  Consulting Invoice TW-2025-018  +USD 10,000 (NTD 312,000)`

**Reasoning:**
USD payment from a US company for consulting services. Services provided to a foreign business paid in foreign currency qualify for zero-rating under the Business Tax Act. Evidence: contract, foreign wire transfer record. Report NTD 312,000 on box 401-3 (zero-rated). No output tax. Confirm: (a) service consumed by a foreign company; (b) payment received in foreign currency.

**Classification:** Zero-rated export — NTD 312,000. Output tax: NTD 0.

### Example 3 — Utility expense (5%, input credit)

**Input line:**
`2025/04/10  自動扣款  台灣電力股份有限公司  電費 2025年3月  -4,200  NT$`

**Reasoning:**
Monthly electricity bill from Taiwan Power (Taipower). Standard 5% business tax. NTD 4,200 gross. Net = NTD 4,000 + NTD 200 input tax. Taipower issues a uniform invoice — input credit of NTD 200 is claimable. Report on 401-5 (total input tax).

**Classification:** Input tax 5% — NTD 200. Net expense: NTD 4,000.

### Example 4 — International SaaS reverse charge (Google Ads)

**Input line:**
`2025/04/08  扣款  GOOGLE ASIA PACIFIC PTE  Google Ads April 2025  -31,500  NT$`

**Reasoning:**
Google Ads billed from Singapore entity. Foreign electronic service provided to a Taiwan business. Taiwan's cross-border e-services rules require the Taiwan buyer to self-assess 5% business tax if the foreign supplier has not registered. NTD 31,500 is treated as net; self-assessed tax = NTD 31,500 × 5% = NTD 1,575. Google Singapore has Taiwan registration — check if their invoice shows Taiwan business tax. If yes, treat as standard input; if no, self-assess.

**Classification:** Reverse charge 5% — NTD 1,575. Confirm Google's Taiwan registration status.

### Example 5 — Blocked input (personal vehicle)

**Input line:**
`2025/04/05  扣款  中油加油站  加油費  -3,000  NT$`

**Reasoning:**
Fuel from CPC (China Petroleum Corporation / 中油). Vehicle expenses — business-use percentage unknown. Business tax rules: input tax on vehicles is disallowed if the vehicle is also used privately. Default: 0% credit until business-use percentage confirmed. If dedicated business vehicle with no personal use: full 5% input credit. Flag for Tier 2 confirmation.

**Classification:** Tier 2 — ask. Conservative default: no input credit (0%).

### Example 6 — Exempt service received (bank interest income recorded as expense reversal)

**Input line:**
`2025/04/01  利息收入  玉山銀行  存款利息 2025年3月  +1,250  NT$`

**Reasoning:**
Bank interest credit. Interest income is exempt from business tax in Taiwan. EXCLUDE from 營業稅 return. This is also not a supply — it is passive income. No output tax. No impact on input credit proration unless the business has significant exempt income that triggers proration rules.

**Classification:** EXCLUDE. Exempt interest income — outside business tax scope.

---

## Section 5 — Tier 1 rules (compressed)

### 5.1 Standard rate 5%

Default rate for all taxable sales of goods and services in Taiwan. Legislation: Business Tax Act (加值型及非加值型營業稅法) Article 10.

### 5.2 Zero rate — exports

Exports of goods and services rendered to foreign businesses paid in foreign currency. Evidence required: export customs declaration for goods; contracts and FX transfer records for services. Legislation: Business Tax Act Article 7.

### 5.3 Exempt supplies

Exempt (免稅) supplies: medical and hospital services, education, cultural/arts services (some), financial services (interest, insurance premiums), residential land, sale of securities, postage stamps. No output tax; no input credit claimable on costs attributable to exempt revenue. Legislation: Business Tax Act Articles 8–9.

### 5.4 Uniform invoice (統一發票)

All taxable sales must be evidenced by a uniform invoice (統一發票) with a government-issued sequential number. Required fields: seller's business number (統一編號), buyer's business number (for B2B), transaction date, description, taxable amount, tax amount. Electronic invoices (電子發票) allowed if registered on the e-invoice platform.

### 5.5 Input credit rules

Input tax is deductible if: (1) a uniform invoice is held; (2) the purchase relates to taxable (not exempt) business activities; (3) not blocked (motor vehicles for mixed use, entertainment, personal expenses). Blocked inputs cannot be credited regardless of business purpose.

### 5.6 Cross-border electronic services

Foreign suppliers of electronic services (B2C to Taiwan consumers) must register if Taiwan B2C sales > NTD 480,000/year. Taiwan B2B buyers self-assess if the foreign supplier has not registered. Rate: 5%.

### 5.7 Small business tax (小規模營業人)

Monthly revenue below NTD 80,000 (goods) / NTD 40,000 (services): file quarterly Form 403. Tax is assessed by the tax office on a deemed basis (usually 1% of sales for food/beverage; standard rates otherwise). No input credits. No uniform invoice required (use plain receipt).

### 5.8 Filing deadlines

| Filer | Period | Due date |
|---|---|---|
| General taxpayer (bi-monthly) | Jan–Feb, Mar–Apr, May–Jun, Jul–Aug, Sep–Oct, Nov–Dec | 15th of following month |
| Small business (quarterly) | Q1, Q2, Q3, Q4 | 15th of month following quarter |

### 5.9 Penalties

| Offence | Penalty |
|---|---|
| Late filing | NTD 1,200–12,000 |
| Late payment | 1% per month up to 30% |
| Failure to issue uniform invoice | NTD 3,000–30,000 + 5× assessed tax |
| Tax evasion | Up to 5× evaded tax + potential criminal liability |

---

## Section 6 — Tier 2 catalogue

### 6.1 Vehicle expenses — business-use percentage

**What it shows:** Fuel, tolls, parking, or vehicle lease payment.
**What's missing:** Proportion of business vs. personal use.
**Conservative default:** 0% input credit.
**Question to ask:** "Is this vehicle used exclusively for business? If mixed, what is the estimated business-use percentage? Is a mileage log kept?"

### 6.2 Export qualification for services

**What it shows:** Revenue from a foreign customer.
**What's missing:** Whether payment was received in foreign currency and the service was consumed outside Taiwan.
**Conservative default:** Taxable at 5%.
**Question to ask:** "Was payment received in foreign currency? Was the service entirely consumed by a foreign entity outside Taiwan?"

### 6.3 International SaaS — registered or not in Taiwan

**What it shows:** Payment to a foreign tech company.
**What's missing:** Whether the foreign supplier has registered for Taiwan business tax.
**Conservative default:** Self-assess 5% reverse charge.
**Question to ask:** "Does the invoice from this supplier show a Taiwan business number (統一編號)? If yes, treat as standard; if no, self-assess."

### 6.4 Mixed residential/commercial property rent

**What it shows:** Rent payment.
**What's missing:** Whether commercial (taxable) or residential (depends — residential land exempt but building portion taxable in some cases).
**Conservative default:** Taxable at 5% if commercial; check for exempt status.
**Question to ask:** "Is this rent for commercial office space or residential? Does the landlord issue a uniform invoice?"

### 6.5 ATM cash withdrawals

**What it shows:** Cash withdrawal.
**What's missing:** What the cash was spent on.
**Conservative default:** Exclude.
**Question to ask:** "What was this cash used for? Do you have receipts?"

---

## Section 7 — Excel working paper template

```
TAIWAN BUSINESS TAX WORKING PAPER — 營業稅計算表
Period: ____________  Entity: ____________  統一編號: ____________

A. OUTPUT TAX (銷項稅額)
  A1. Taxable sales at 5% (net)               ___________
  A2. Output tax at 5% (A1 × 5%)              ___________
  A3. Zero-rated exports (net)                ___________
  A4. Exempt sales (net)                      ___________
  A5. Reverse charge output self-assessed     ___________

B. INPUT TAX (進項稅額)
  B1. Domestic purchases — 5% (net)           ___________
  B2. Input tax at 5% (B1 × 5%)               ___________
  B3. Import business tax paid                ___________
  B4. Reverse charge self-assessed input      ___________
  B5. Total input tax (B2+B3+B4)             ___________
  B6. Disallowed input (vehicles, personal)   ___________
  B7. Net input (B5 − B6)                     ___________

C. NET PAYABLE
  C1. Net tax (A2 − B7)                       ___________
  C2. Prior period credit carried forward     ___________
  C3. Net payable / (excess credit) (C1 − C2) ___________

REVIEWER FLAGS:
  [ ] All uniform invoices (統一發票) confirmed?
  [ ] Export FX evidence available for zero-rated sales?
  [ ] Vehicle use percentage confirmed?
  [ ] International SaaS registration status confirmed?
  [ ] Exempt income proration check done?
```

---

## Section 8 — Bank statement reading guide

### Common Taiwanese bank CSV formats

| Bank | Key columns | Date format | Amount |
|---|---|---|---|
| 玉山銀行 E.SUN | 交易日期, 摘要, 交易金額, 餘額 | YYYY/MM/DD | NTD integer or decimal |
| 國泰世華 Cathay | 交易日, 說明, 存入, 提出, 餘額 | YYYY/MM/DD | NTD |
| 中信銀行 CTBC | 交易日期, 交易說明, 轉入金額, 轉出金額, 餘額 | YYYY-MM-DD | NTD |
| 富邦銀行 Fubon | 交易日期, 交易種類, 金額, 餘額 | YYYYMMDD | NTD |
| 台灣銀行 BOT | 交易日, 摘要, 借方金額, 貸方金額, 餘額 | YYYY/MM/DD | NTD |
| 中華郵政 Chunghwa Post | 日期, 說明, 取款, 存款, 餘額 | YYYY/MM/DD | NTD |

### Key Taiwanese banking terms

| Chinese | Meaning | Classification hint |
|---|---|---|
| 轉帳收入 / 入款 | Incoming transfer | Potential revenue |
| 轉帳支出 / 扣款 | Outgoing transfer / debit | Potential expense |
| 自動扣款 | Auto-debit / standing order | Recurring expense |
| 外匯入款 | Foreign currency receipt | Potential export |
| 手續費 | Handling fee | Bank fee — exempt |
| 利息收入 | Interest income | Exempt |
| 餘額 | Balance | Running balance — ignore |
| 摘要 / 說明 | Description / narrative | Key classification field |
| ATM提款 | ATM withdrawal | Tier 2 — ask |
| 薪資 | Salary | Out of scope |

---

## Section 9 — Onboarding fallback

If the client provides a bank statement but cannot answer all questions immediately:

1. Classify all transactions using the pattern library (Section 3)
2. Apply conservative defaults (Section 1)
3. Mark Tier 2 items as "PENDING — reviewer must confirm"
4. Generate working paper with flags

```
TAIWAN BUSINESS TAX ONBOARDING — MINIMUM QUESTIONS
1. Are you a general taxpayer (一般納稅義務人) or small business (小規模)?
2. Your 統一編號 (8-digit business number)?
3. Filing period: which bi-monthly period does this bank statement cover?
4. Do you have any export sales (paid in foreign currency from foreign clients)?
5. Any vehicle expenses? Business-use percentage?
6. Any international SaaS subscriptions? Do those suppliers show a Taiwan 統一編號?
7. Do you make any exempt sales (land, financial services, medical)?
8. Prior period excess credit (留抵稅額) carried forward amount?
```

---

## Section 10 — Reference material

### Key legislation

| Topic | Reference |
|---|---|
| Business Tax Act | 加值型及非加值型營業稅法 |
| Standard rate | Business Tax Act Article 10 |
| Zero rate | Business Tax Act Article 7 |
| Exemptions | Business Tax Act Articles 8–9 |
| Uniform invoice | 統一發票使用辦法 |
| Cross-border e-services | 財政部公告 (MoF Announcement) on B2C digital services |
| Small business | Business Tax Act Article 13 |
| Penalties | Business Tax Act Articles 45–52; Tax Collection Act |

### Known gaps

- Partial exemption proration (exempt income > de minimis) — escalate to 會計師
- Financial institution special calculation — escalate
- Non-resident B2C e-service registration — out of scope
- Land transaction exemption interaction — verify with 會計師

### Self-check before filing

- [ ] All uniform invoices issued for taxable sales
- [ ] Export FX documentation held for zero-rated sales
- [ ] Input tax correctly split: taxable vs. exempt vs. blocked
- [ ] International SaaS reverse charge self-assessed where needed
- [ ] Prior period credit (留抵稅額) correctly carried forward
- [ ] Vehicle and entertainment inputs correctly blocked

### Changelog

| Version | Date | Change |
|---|---|---|
| 1.0 | 2024 | Initial release |
| 2.0 | April 2026 | Full v2.0 rewrite: pattern library, worked examples, no inline tier tags |

---

## Prohibitions

- NEVER claim input credit without a valid uniform invoice (統一發票)
- NEVER zero-rate a service without confirming FX payment from a foreign entity
- NEVER allow small business taxpayers to claim input credits
- NEVER omit self-assessed reverse charge for foreign electronic services
- NEVER classify bank interest as taxable revenue — it is exempt
- NEVER present calculations as definitive — direct to a licensed 會計師 (CPA) for confirmation

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes. All outputs must be reviewed by a qualified professional (會計師 or equivalent) before filing.

The most up-to-date version is maintained at openaccountants.com.
