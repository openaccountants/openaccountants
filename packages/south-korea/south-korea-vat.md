---
name: south-korea-vat
description: Use this skill whenever asked to prepare, review, or classify transactions for a South Korea VAT return (부가가치세 신고서) for any business operator. Trigger on phrases like "prepare Korean VAT return", "Korean VAT", "HomeTax filing", "e-tax invoice", "전자세금계산서", "부가가치세", or any request involving South Korea VAT filing. Also trigger when classifying transactions for VAT purposes from bank statements, invoices, or other source data. This skill contains the complete South Korea VAT classification rules, return form mappings, deductibility rules, reverse charge treatment, simplified taxation thresholds, and filing deadlines required to produce a correct return. ALWAYS read this skill before touching any South Korea VAT-related work.
version: 2.0
---

# South Korea VAT Return Preparation Skill v2.0

## Section 1 -- Quick reference

**Read this whole section before classifying anything.**

| Field | Value |
|---|---|
| Country | South Korea (Republic of Korea, 대한민국) |
| Standard rate | 10% (single rate, Article 30 VAT Act) |
| Reduced rates | None (Korea uses only standard 10%, zero 0%, and exempt) |
| Zero rate | 0% (exports, foreign currency earning services, international transport) |
| Exempt | No VAT charged, no input deduction (unprocessed food, medical, education, financial, public transport, books) |
| Return form | 일반과세자 부가가치세 신고서 (General Taxpayer VAT Return); 간이과세자 신고서 (Simplified Taxpayer Return) |
| Filing portal | https://hometax.go.kr (HomeTax / 홈택스) |
| Authority | National Tax Service (국세청, NTS) |
| Currency | KRW (Korean Won) |
| Filing frequency | Semi-annual with quarterly preliminary returns (general taxpayer); semi-annual (simplified taxpayer) |
| E-invoice requirement | 전자세금계산서 (e-tax invoice) mandatory for all corporations and individual taxpayers with revenue >= KRW 80M |
| Primary legislation | VAT Act (부가가치세법, as amended); VAT Act Enforcement Decree (시행령); Framework Act on National Taxes (국세기본법) |
| Contributor | Open Accounting Skills Registry |
| Validated by | Deep research verification, April 2026 |
| Validation date | April 2026 |
| Skill version | 2.0 |

**Key return lines (일반과세자 부가가치세 신고서):**

| Line | Meaning |
|---|---|
| 1 | Tax invoices issued -- taxable sales (세금계산서 발급분) |
| 2 | Tax invoices issued -- zero-rated sales (영세율 세금계산서 발급분) |
| 3 | Credit card / cash receipt sales (신용카드/현금영수증 발행분) |
| 4 | Other sales (기타 매출) |
| 5 | Total taxable supply value (과세표준, derived: Lines 1-4) |
| 6 | Output tax (매출세액, Line 5 x 10%, adjusted for zero-rated) |
| 7 | Direct exports (직접수출) |
| 8 | Intermediary trade (중계무역) |
| 9 | Deemed exports / local L/C (내국신용장/구매확인서) |
| 10 | Foreign currency earning services (외화획득 용역) |
| 11 | Other zero-rated (기타 영세율) |
| 12 | Tax invoices received (세금계산서 수취분, input) |
| 13 | Fixed assets (고정자산 매입, subset of Line 12) |
| 14 | Non-tax-invoice purchases eligible for input (기타 공제매입세액, credit card/cash receipt) |
| 15 | Total input tax (매입세액 합계) |
| 16 | Net tax (차감세액, Line 6 - Line 15) |
| 17 | Adjustments (가감조정세액, credit notes, bad debt relief) |
| 18 | Preliminary payment credit (예정신고 미환급세액) |
| 19 | Carried-forward credit from prior period (전기 미환급세액) |
| 20 | Tax payable / refundable (납부/환급세액) |

**E-tax invoice (전자세금계산서) requirements:**

All corporations must issue e-tax invoices. Individual general taxpayers with revenue >= KRW 80M must issue e-tax invoices (mandatory since July 2024; threshold was KRW 100M before July 2023). E-tax invoices must contain: business registration numbers (사업자등록번호) of supplier and recipient, supplier name, supply date, description and quantity, supply value (공급가액) and VAT amount (세액). Must be transmitted to NTS within one day of issuance. Penalties: 2% of supply value for failure to issue; 1% for late issuance; 0.5% for failure to transmit to NTS.

**Simplified taxpayer (간이과세자) threshold:**

Annual revenue below KRW 104,000,000 (KRW 104M, raised from KRW 80M effective July 2024). Simplified taxpayers calculate tax using industry value-added ratios (업종별 부가가치율), cannot issue tax invoices (receipts only), and file semi-annually. If revenue below KRW 48M, exempt from VAT payment entirely.

**Filing deadlines -- general taxpayer:**

| Period | Type | Covers | Deadline |
|---|---|---|---|
| Period 1 Preliminary | Preliminary return | Jan 1 - Mar 31 | April 25 |
| Period 1 Final | Confirmed return | Jan 1 - Jun 30 | July 25 |
| Period 2 Preliminary | Preliminary return | Jul 1 - Sep 30 | October 25 |
| Period 2 Final | Confirmed return | Jul 1 - Dec 31 | January 25 (following year) |

**Filing deadlines -- simplified taxpayer:**

| Period | Type | Covers | Deadline |
|---|---|---|---|
| Period 1 | Semi-annual | Jan 1 - Jun 30 | July 25 |
| Period 2 | Semi-annual | Jul 1 - Dec 31 | January 25 (following year) |

**Conservative defaults -- Korea-specific:**

| Ambiguity | Default |
|---|---|
| Unknown rate on a sale | 10% |
| Unknown VAT status of a purchase | Not deductible |
| Unknown counterparty location | Domestic Korea |
| Unknown B2B vs B2C status | B2C (no tax invoice exchange) |
| Unknown business-use proportion (vehicle, phone) | 0% recovery |
| Unknown blocked-input status (entertainment, personal, vehicle) | Blocked |
| Unknown whether transaction is in scope | In scope at 10% |
| Unknown foreign SaaS billing entity | Reverse charge from non-resident |
| Unknown whether e-tax invoice exists | Not deductible (no invoice = no credit) |

**Red flag thresholds:**

| Threshold | Value |
|---|---|
| HIGH single-transaction size | KRW 5,000,000 |
| HIGH tax-delta on a single conservative default | KRW 500,000 |
| MEDIUM counterparty concentration | >40% of output OR input |
| MEDIUM conservative-default count | >4 across the return |
| LOW absolute net VAT position | KRW 10,000,000 |

---

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

**Minimum viable** -- bank statement (거래내역) for the period in CSV, PDF, Excel, or pasted text. Must cover the full semi-annual or quarterly period. Acceptable from any Korean bank: KB Kookmin, Shinhan, Woori, Hana, NH Nonghyup, IBK, Kakao Bank, Toss Bank, K Bank, or any other.

**Recommended** -- e-tax invoice listing from HomeTax (전자세금계산서 합계표) for both issued and received invoices, credit card usage statement (신용카드매출전표), prior period return showing carried-forward credit.

**Ideal** -- complete e-tax invoice download from HomeTax, credit card sales slip summary, cash receipt summary, prior period VAT return, business registration certificate (사업자등록증).

**Refusal policy if minimum is missing -- SOFT WARN.** If no bank statement and no e-tax invoice listing at all, hard stop. If bank statement only without invoices, proceed but record in the reviewer brief: "This VAT return was produced from bank statement alone. The reviewer must verify that all input tax claims are supported by valid e-tax invoices or credit card sales slips and that all output tax is properly accounted for."

### Korea-specific refusal catalogue

**R-KR-1 -- Group VAT registration.** *Trigger:* client is part of a VAT group registration. *Message:* "VAT group registrations require consolidated treatment across the group. This is outside this skill's scope. Escalate to a 세무사 or 공인회계사."

**R-KR-2 -- Special industry regimes.** *Trigger:* client operates under special VAT regimes (gold bullion, scrap metal intermediary, real estate development). *Message:* "Special industry regimes have unique VAT rules beyond this skill's coverage. Escalate to a licensed practitioner."

**R-KR-3 -- Tax tribunal disputes.** *Trigger:* client is in a tax dispute or appealing an NTS assessment. *Message:* "Tax tribunal and appeals work is outside this skill's scope. Engage a tax attorney."

**R-KR-4 -- Partial exemption apportionment (complex).** *Trigger:* client has significant exempt supplies requiring Article 40 apportionment with annual adjustment, and the exempt proportion is not de minimis (>5%). *Message:* "Your exempt supplies exceed 5% of total supplies. Partial input tax apportionment under Article 40 requires confirmation of the apportionment ratio by a 세무사 or 공인회계사 before filing."

**R-KR-5 -- Income tax return instead of VAT.** *Trigger:* user asks about income tax (소득세) or corporate tax (법인세). *Message:* "This skill only handles the VAT return (부가가치세 신고서). For income tax or corporate tax, use the appropriate skill."

**R-KR-6 -- Exempt business operator (면세사업자).** *Trigger:* client is registered as exempt-only business operator. *Message:* "Exempt business operators do not file VAT returns. They file a 사업장 현황 신고 (business status report) annually. This skill covers general and simplified taxpayers only."

---

## Section 3 -- Supplier pattern library (the lookup table)

This is the deterministic pre-classifier. When a transaction's counterparty matches a pattern in this table, apply the treatment directly. If none match, fall through to Tier 1 rules in Section 5.

**How to read this table.** Match by case-insensitive substring on the counterparty name as it appears in the bank statement. Korean names may appear in Hangul or romanized form. If multiple patterns match, use the most specific.

### 3.1 Korean banks (fees exempt -- exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| KB국민은행, KB KOOKMIN, 국민은행 | EXCLUDE for bank charges/fees | Financial service, exempt under Art. 26(1)11 |
| 신한은행, SHINHAN BANK | EXCLUDE for bank charges/fees | Same |
| 우리은행, WOORI BANK | EXCLUDE for bank charges/fees | Same |
| 하나은행, HANA BANK, KEB하나 | EXCLUDE for bank charges/fees | Same |
| NH농협, NONGHYUP, 농협은행 | EXCLUDE for bank charges/fees | Same |
| IBK기업은행, IBK, 기업은행 | EXCLUDE for bank charges/fees | Same |
| 카카오뱅크, KAKAO BANK | EXCLUDE for bank charges/fees | Same |
| 토스뱅크, TOSS BANK | EXCLUDE for bank charges/fees | Same |
| 케이뱅크, K BANK | EXCLUDE for bank charges/fees | Same |
| 이자, 이자수입, INTEREST | EXCLUDE | Interest income/expense, exempt financial service |
| 대출, 상환, LOAN, REPAYMENT | EXCLUDE | Loan principal, out of scope |
| 수수료, 거래수수료, 이체수수료 | EXCLUDE | Bank fees, exempt financial service |

### 3.2 Korean government and statutory bodies (exclude entirely)

| Pattern | Treatment | Notes |
|---|---|---|
| 국세청, NTS, HOMETAX | EXCLUDE | Tax authority / tax payment |
| 부가가치세, 부가세 납부 | EXCLUDE | VAT payment to NTS |
| 소득세, 법인세, 원천세 | EXCLUDE | Income/corporate/withholding tax payment |
| 국민연금, NATIONAL PENSION | EXCLUDE | Pension contribution |
| 건강보험, 국민건강보험 | EXCLUDE | Health insurance contribution |
| 고용보험, 산재보험 | EXCLUDE | Employment/workers compensation insurance |
| 지방세, 재산세, 자동차세 | EXCLUDE | Local taxes, not VAT |
| 관세, 세관 | EXCLUDE (but see import VAT below) | Customs duty (not VAT -- but import VAT invoice is separate) |

### 3.3 Korean utilities

| Pattern | Treatment | Line | Notes |
|---|---|---|---|
| 한국전력, KEPCO, 전기요금 | Domestic 10% | 12/input | Electricity -- deductible with e-tax invoice |
| 한국가스공사, 도시가스, 가스요금 | Domestic 10% | 12/input | Gas supply |
| 수도요금, 상수도 | EXCLUDE or exempt | | Water -- municipal water is generally exempt |
| KT, 케이티, KT CORP | Domestic 10% | 12/input | Telecoms -- deductible if business use |
| SKT, SK텔레콤, SK TELECOM | Domestic 10% | 12/input | Same |
| LG유플러스, LG U+, UPLUS | Domestic 10% | 12/input | Same |
| SK브로드밴드, KT인터넷, LG인터넷 | Domestic 10% | 12/input | Internet/broadband |

### 3.4 Insurance (exempt -- exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| 삼성화재, 삼성생명, SAMSUNG INSURANCE | EXCLUDE | Insurance premium, exempt Art. 26(1)11 |
| 현대해상, 현대라이프 | EXCLUDE | Same |
| DB손해보험, 동부화재 | EXCLUDE | Same |
| KB손해보험, KB라이프 | EXCLUDE | Same |
| 한화생명, 한화손해보험 | EXCLUDE | Same |
| 보험, 보험료, INSURANCE | EXCLUDE | All insurance premiums exempt |

### 3.5 Transport

| Pattern | Treatment | Notes |
|---|---|---|
| 코레일, KORAIL, KTX, SRT | Domestic 10% | Rail transport -- standard rated. Deductible with e-tax invoice. |
| 시내버스, 마을버스, 지하철, METRO | EXCLUDE or exempt | Public transport (city bus, subway) exempt Art. 26(1)7 |
| 택시, TAXI, 카카오택시 | Domestic 10% | Taxi -- standard rated. Credit card receipt deductible (Line 14). |
| 카카오T, KAKAO T | Domestic 10% | Platform taxi service |
| 대한항공, KOREAN AIR, 아시아나, ASIANA | 0% (international) or 10% (domestic) | International flights zero-rated. Domestic flights 10%. |
| 제주항공, JEJU AIR, 진에어, JIN AIR | Same | Budget airlines, same treatment |

### 3.6 Major Korean retailers and e-commerce

| Pattern | Treatment | Line | Notes |
|---|---|---|---|
| 쿠팡, COUPANG | Domestic 10% | 14 (credit card) or 12 (if e-tax invoice) | E-commerce -- credit card receipt deductible at Line 14. Check for mixed items (food may be exempt). |
| 네이버, NAVER, 네이버쇼핑 | Domestic 10% | 14 or 12 | Same |
| 카카오, KAKAO | Domestic 10% | 14 or 12 | Kakao services |
| SSG, 이마트, EMART, 신세계 | Domestic 10% | 14 | Retail -- credit card receipt. Food items may be exempt (unprocessed). |
| 롯데마트, LOTTE MART, 롯데백화점 | Domestic 10% | 14 | Same -- department store |
| 홈플러스, HOMEPLUS | Domestic 10% | 14 | Same |
| GS25, CU, 세븐일레븐, 7-ELEVEN | Domestic 10% | 14 | Convenience store -- small purchases. Confirm business purpose. |
| 다이소, DAISO | Domestic 10% | 14 | General merchandise |
| 배달의민족, BAEMIN, 요기요, YOGIYO | Domestic 10% | 14 | Food delivery platform -- standard rated service. Food items may include exempt components. |

### 3.7 Food and entertainment (blocked unless qualifying business)

| Pattern | Treatment | Notes |
|---|---|---|
| 식당, RESTAURANT, 음식점, 한식, 중식, 일식 | Default BLOCK input VAT | Entertainment (접대비) is ALWAYS blocked under Art. 39(1)4. No exceptions for business purpose. |
| 카페, CAFE, 스타벅스, STARBUCKS, 이디야 | Default BLOCK | Same -- entertainment, blocked |
| 술집, BAR, 호프, 노래방 | Default BLOCK | Same |
| 슈퍼마켓, 마트 (personal provisioning) | Default BLOCK | Unless hospitality/catering business |

### 3.8 SaaS -- foreign suppliers (reverse charge)

Korean businesses receiving services from non-residents self-assess VAT at 10% under Article 52 (reverse charge / 대리납부). Both output and input VAT reported; net effect zero for fully taxable businesses.

| Pattern | Billing entity | Treatment | Notes |
|---|---|---|---|
| GOOGLE (Ads, Workspace, Cloud) | Google Asia Pacific Pte Ltd (SG) or Google LLC (US) | Reverse charge 10% | Self-assess output + input. Net zero if fully taxable. |
| MICROSOFT (365, Azure) | Microsoft Corp (US) or regional entity | Reverse charge 10% | Same |
| ADOBE | Adobe Inc (US) | Reverse charge 10% | Same |
| META, FACEBOOK ADS | Meta Platforms Inc (US) | Reverse charge 10% | Same |
| AWS, AMAZON WEB SERVICES | Amazon Web Services Inc (US) | Reverse charge 10% | Same |
| SLACK, NOTION, FIGMA | US entities | Reverse charge 10% | Same |
| ANTHROPIC, OPENAI, CHATGPT | US entities | Reverse charge 10% | Same |
| ZOOM | Zoom Video Communications Inc (US) | Reverse charge 10% | Same |
| ATLASSIAN (Jira, Confluence) | Atlassian Pty Ltd (AU) or US entity | Reverse charge 10% | Same |
| GITHUB | GitHub Inc (US) | Reverse charge 10% | Same |

**Note:** For B2C digital services, non-resident providers (Netflix, Spotify, Apple) register under the simplified registration scheme (Article 53-2) and collect VAT directly from Korean consumers. B2B clients receiving from these providers still self-assess under reverse charge.

### 3.9 Payment processors

| Pattern | Treatment | Notes |
|---|---|---|
| 토스페이먼츠, TOSS PAYMENTS | EXCLUDE (exempt) | Payment processing -- financial service |
| KG이니시스, INICIS | EXCLUDE (exempt) | Same |
| NHN한국사이버결제, KCP | EXCLUDE (exempt) | Same |
| PAYPAL (transaction fees) | EXCLUDE (exempt) | Payment processing, financial service |
| STRIPE (transaction fees) | EXCLUDE (exempt) or reverse charge | If billed from US: imported financial service. Transaction fees may be exempt. |

### 3.10 Professional services (Korea)

| Pattern | Treatment | Line | Notes |
|---|---|---|---|
| 세무사, 세무법인, TAX ACCOUNTANT | Domestic 10% | 12/input | Tax advisory, deductible with e-tax invoice |
| 회계사, 회계법인, 공인회계사 | Domestic 10% | 12/input | Audit/accounting, always deductible |
| 변호사, 법무법인, LAW FIRM | Domestic 10% | 12/input | Legal, deductible if business matter |
| 법무사, 변리사 | Domestic 10% | 12/input | Judicial scrivener / patent attorney |
| 컨설팅, CONSULTING | Domestic 10% | 12/input | Consulting, standard rated |

### 3.11 Payroll and social security (exclude entirely)

| Pattern | Treatment | Notes |
|---|---|---|
| 급여, 월급, SALARY, WAGES | EXCLUDE | Wages, outside VAT scope |
| 국민연금, PENSION | EXCLUDE | Pension contribution |
| 건강보험, HEALTH INSURANCE | EXCLUDE | National health insurance |
| 고용보험, EMPLOYMENT INSURANCE | EXCLUDE | Employment insurance |
| 산재보험, WORKERS COMP | EXCLUDE | Workers compensation |
| 퇴직금, SEVERANCE | EXCLUDE | Severance, outside VAT |

### 3.12 Internal transfers and exclusions

| Pattern | Treatment | Notes |
|---|---|---|
| 자기이체, 본인이체, OWN TRANSFER | EXCLUDE | Internal movement |
| 적금, 예금, 정기예금 | EXCLUDE | Savings/time deposit |
| 배당, DIVIDEND | EXCLUDE | Dividend, out of scope |
| 대출상환, LOAN REPAYMENT | EXCLUDE | Loan principal |
| 현금인출, ATM, 출금 | Ask | Cash withdrawal -- ask what it was spent on |
| NTS 납부, 세금납부 | EXCLUDE | Tax payment |

---

## Section 4 -- Worked examples

These are six fully worked classifications drawn from a hypothetical bank statement of a Seoul-based self-employed IT consultant (일반과세자, general taxpayer).

### Example 1 -- Standard domestic B2B sale with e-tax invoice

**Input line:**
`2026.04.05 ; (주)테크솔루션즈 ; 입금 ; 전자세금계산서 IT컨설팅 4월 ; KRW 11,000,000`

**Reasoning:**
Client issued e-tax invoice for supply value KRW 10,000,000 + VAT KRW 1,000,000 = KRW 11,000,000. Line 1 = KRW 10,000,000. Output tax = KRW 1,000,000. E-tax invoice transmitted to NTS.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Line | Default? | Question? |
|---|---|---|---|---|---|---|---|---|
| 2026.04.05 | (주)테크솔루션즈 | +11,000,000 | +10,000,000 | +1,000,000 | 10% | 1 (output) | N | -- |

### Example 2 -- Export sale, zero-rated

**Input line:**
`2026.04.10 ; ACME CORP (US) ; 입금 ; Invoice KR-2026-018 software dev ; USD 8,000 ; KRW 10,800,000`

**Reasoning:**
IT consulting services to US company earning foreign currency. Zero-rated under Article 24(1)2. Line 2 = KRW 10,800,000 (zero-rated). Line 10 = KRW 10,800,000 (foreign currency earning services detail). Output tax = 0. Export evidence retained.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Line | Default? | Question? |
|---|---|---|---|---|---|---|---|---|
| 2026.04.10 | ACME CORP (US) | +10,800,000 | +10,800,000 | 0 | 0% | 2 / 10 | Y | Verify service qualifies as foreign currency earning |

### Example 3 -- Reverse charge on imported SaaS (US provider)

**Input line:**
`2026.04.15 ; NOTION LABS INC ; 출금 ; Monthly subscription ; USD 16 ; KRW 21,600`

**Reasoning:**
Notion Labs Inc is US entity. No Korean VAT charged. Reverse charge under Article 52. Self-assess output VAT KRW 2,160 (10% of KRW 21,600). Claim input VAT KRW 2,160. Net effect zero for fully taxable business.

**Output:**

| Date | Counterparty | Gross | Net | VAT (output) | VAT (input) | Rate | Line | Default? | Question? |
|---|---|---|---|---|---|---|---|---|---|
| 2026.04.15 | NOTION LABS INC | -21,600 | -21,600 | +2,160 | -2,160 | 10% | Reverse charge adj. | N | -- |

### Example 4 -- Entertainment expense, input blocked

**Input line:**
`2026.04.18 ; 강남 삼겹살집 ; 출금 ; 접대비 고객미팅 ; KRW 550,000`

**Reasoning:**
Restaurant meal (삼겹살집). Entertainment (접대비) is ALWAYS blocked under Article 39(1)4, regardless of business purpose. This is an absolute block in Korea -- no exceptions. VAT component (KRW 50,000) is irrecoverable. The entire KRW 550,000 is a cost.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Line | Default? | Question? |
|---|---|---|---|---|---|---|---|---|
| 2026.04.18 | 강남 삼겹살집 | -550,000 | -550,000 | 0 | -- | -- | Y | "Entertainment: blocked Art. 39(1)4" |

### Example 5 -- Non-business vehicle purchase, input blocked

**Input line:**
`2026.04.22 ; 현대자동차 강남지점 ; 출금 ; 투싼 리스 월납입 ; KRW 650,000`

**Reasoning:**
Car lease payment. Input VAT on non-business passenger vehicles (비영업용 소형승용차) is hard-blocked under Article 39(1)5. This applies to purchase, lease, fuel, repair, insurance. IT consultant does not fall within exception categories (taxi, rental car, driving school, freight). Entire KRW 650,000 is cost.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Line | Default? | Question? |
|---|---|---|---|---|---|---|---|---|
| 2026.04.22 | 현대자동차 강남지점 | -650,000 | -650,000 | 0 | -- | -- | Y | "Vehicle: blocked Art. 39(1)5" |

### Example 6 -- Credit card purchase without e-tax invoice

**Input line:**
`2026.04.28 ; 오피스디포 코리아 ; 출금 ; 법인카드 사무용품 ; KRW 330,000`

**Reasoning:**
Office supplies purchased with corporate credit card. No e-tax invoice obtained. Input VAT is still recoverable via credit card sales slip (신용카드매출전표) under Article 46(1). Report on Line 14 (non-tax-invoice purchases eligible for input). VAT = KRW 330,000 / 1.1 x 0.1 = KRW 30,000 (net KRW 300,000). Retain card statement.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Line | Default? | Question? |
|---|---|---|---|---|---|---|---|---|
| 2026.04.28 | 오피스디포 코리아 | -330,000 | -300,000 | -30,000 | 10% | 14 (credit card input) | N | -- |

---

## Section 5 -- Tier 1 classification rules (compressed)

### 5.1 Standard rate 10% (Article 30)

Single rate for all taxable supplies. No reduced rates in Korea. Sales: Line 1 (with e-tax invoice) or Line 3 (credit card/cash receipt). Purchases: Line 12 (with e-tax invoice) or Line 14 (credit card/cash receipt).

### 5.2 Zero-rated supplies (Article 24)

Exports of goods (FOB value) -- Line 2/7. Services to non-residents earning foreign currency -- Line 2/10. International transportation -- Line 2/11. Local letter of credit supplies (내국신용장) -- Line 2/9. Goods/services to foreign diplomats -- Line 2/11. Zero-rating allows full input tax deduction.

### 5.3 Exempt supplies (Article 26)

Unprocessed foodstuffs (rice, vegetables, fresh fish), medical/health services, accredited education, financial/insurance services, books/newspapers, residential rental (국민주택 규모 이하, 85 sqm or less), public transport (city bus, subway), postal services, religious/charitable activities. No output VAT; no input deduction on attributable costs.

### 5.4 E-tax invoice requirement

Mandatory for all corporations (since 2011) and individual general taxpayers with revenue >= KRW 80M (since July 2024). Must transmit to NTS within one day. Content: both parties' registration numbers, supply date, description, supply value and VAT. Without valid e-tax invoice, input VAT is not deductible EXCEPT via credit card sales slip (Line 14) or cash receipt.

### 5.5 Credit card and cash receipt input deduction (Article 46)

Corporate credit card purchases without e-tax invoice: input VAT deductible via credit card sales slip. Report on Line 14. Entertainment expenses remain blocked regardless. Cash receipt (현금영수증) purchases: same treatment as credit card for VAT purposes.

### 5.6 Blocked input VAT (Article 39)

Entertainment of any kind (접대비) -- absolute block, Art. 39(1)4. Non-business passenger vehicles (비영업용 소형승용차) including purchase, lease, fuel, repair, insurance -- Art. 39(1)5. Exceptions for vehicles: taxi, rental car operators, driving schools, freight transport, vehicle sales/repair, hearse. Non-business expenses -- Art. 39(1)1. Purchases without proper tax invoice -- Art. 39(1)2. Land acquisition costs -- Art. 39(1)6. Input tax on exempt supplies -- Art. 39(1)7. Pre-registration expenses beyond 20-day lookback -- Art. 39(1)8. Blocked categories override partial exemption. Check blocked status FIRST.

### 5.7 Reverse charge on imported services (Article 52)

Korean business receives services from non-resident with no Korean PE: self-assess VAT at 10%. Report as both output tax (additional) and input tax (deductible). Net effect zero for fully taxable businesses. File and pay via HomeTax by the 25th of the month following quarter end. If business makes exempt supplies, reverse charge input tax is subject to partial apportionment.

### 5.8 Simplified taxpayer regime (Articles 61-68)

Revenue below KRW 104M: eligible as simplified taxpayer. Tax = supply value x industry value-added ratio x 10%. Industry ratios: retail 15%, manufacturing 20%, agriculture 10%, food/beverage 40%, accommodation 30%, transportation 40%, construction 30%, other services 30%, real estate rental 40%, professional services 40%. Input deduction = purchases x 0.5%. Cannot issue tax invoices. Revenue below KRW 48M: exempt from VAT payment.

### 5.9 Capital assets (fixed assets, 고정자산)

Assets subject to depreciation per Corporate Tax Act or Income Tax Act. Report as a subset of Line 12 on Line 13. No separate threshold test like Malta. All depreciable assets go to Line 13 regardless of value.

### 5.10 Bad debt relief (Article 45)

Output VAT on irrecoverable debts can be recovered in the period confirmed irrecoverable. Report on Line 17 (adjustments). Conditions: debt must be legally irrecoverable (bankruptcy, statute of limitations); claim within 5 years of original supply.

### 5.11 Credit notes and adjustments

Credit notes (수정세금계산서) for price changes, returns, or cancellations. Report on Line 17 (adjustments). Must issue revised e-tax invoice with reason code.

### 5.12 Correction of prior returns (수정신고)

File amended return via HomeTax. Additional tax: underreporting penalty 10% (general) or 40% (fraudulent). Voluntary correction before NTS audit notice: reduced penalties (50-90% reduction depending on timing).

---

## Section 6 -- Tier 2 catalogue (compressed)

### 6.1 Fuel and vehicle costs

*Pattern:* 주유소, GS칼텍스, SK에너지, S-OIL, 현대오일뱅크, fuel receipts. *Why insufficient:* vehicle type and business use unknown. If car (소형승용차) = blocked regardless of use. If van, truck, delivery vehicle = deductible. *Default:* 0% recovery. *Question:* "Is this a passenger car (blocked) or a commercial/delivery vehicle used exclusively for business?"

### 6.2 Restaurants and entertainment

*Pattern:* any restaurant, cafe, bar. *Why insufficient:* entertainment is hard blocked under Art. 39(1)4. No business-purpose exception in Korea. *Default:* block. *Question:* "Was this entertainment (접대비)? (Note: blocked regardless of business purpose.)"

### 6.3 Ambiguous SaaS billing entity

*Pattern:* Google, Microsoft, Adobe, Meta, Amazon where billing entity unclear. *Default:* reverse charge from non-resident. *Question:* "Can you check the invoice? I need the legal entity name and whether Korean VAT was charged."

### 6.4 Round-number incoming transfers from owner-named counterparties

*Pattern:* large round credit from a name matching the business owner. *Default:* exclude as owner capital injection. *Question:* "Is this a customer payment, your own capital injection, or a loan?"

### 6.5 Incoming transfers from foreign counterparties

*Pattern:* foreign currency or foreign name on incoming. *Default:* domestic 10% sale. *Question:* "Is this a B2B export service (zero-rated) or domestic sale? Can you provide the customer's country and business status?"

### 6.6 Mixed-use phone and internet

*Pattern:* KT, SKT, LG U+ on personal lines, home internet. *Default:* 0% if mixed use. 100% if confirmed dedicated business line. *Question:* "Is this a dedicated business line or mixed personal/business?"

### 6.7 Cash withdrawals

*Pattern:* 현금인출, ATM, 출금. *Default:* exclude as personal drawing. *Question:* "What was the cash used for?"

### 6.8 Outgoing transfers to individuals

*Pattern:* outgoing to private-sounding names. *Default:* exclude as drawings or wages. *Question:* "Was this a contractor payment with tax invoice, wages, or personal transfer?"

### 6.9 Simplified vs general taxpayer determination

*Pattern:* client's taxpayer type is unknown. *Default:* general taxpayer (more conservative filing obligations). *Question:* "Are you a 일반과세자 (general taxpayer) or 간이과세자 (simplified taxpayer)? What is your annual revenue?"

### 6.10 Real estate lease

*Pattern:* monthly 임대료, 월세 payment. *Default:* no VAT deduction (assume residential). *Question:* "Is this a commercial property lease (10% VAT) or residential lease (exempt)?"

---

## Section 7 -- Excel working paper template (Korea-specific)

### Sheet "Transactions"

Columns: A (Date), B (Counterparty), C (사업자등록번호 or note), D (Gross KRW), E (Net KRW), F (VAT KRW), G (Rate), H (Line code), I (Input method: e-tax invoice / credit card / cash receipt), J (Default Y/N), K (Question), L (Notes).

Column I (input method) is important in Korea because it determines which return line receives the input: Line 12 for e-tax invoices, Line 14 for credit card/cash receipt.

### Sheet "Return Summary"

```
Output tax:
| 1  | Tax invoices issued -- taxable | =SUMIFS(Transactions!E:E, Transactions!H:H, "1") |
| 2  | Tax invoices issued -- zero-rated | =SUMIFS(Transactions!E:E, Transactions!H:H, "2") |
| 3  | Credit card / cash receipt sales | =SUMIFS(Transactions!E:E, Transactions!H:H, "3") |
| 4  | Other sales | =SUMIFS(Transactions!E:E, Transactions!H:H, "4") |
| 5  | Total taxable supply value | =SUM(Lines 1-4) |
| 6  | Output tax | =(Line 1 + Line 3 + Line 4) * 0.10 |

Zero-rated detail:
| 7  | Direct exports | =SUMIFS(Transactions!E:E, Transactions!H:H, "7") |
| 10 | Foreign currency services | =SUMIFS(Transactions!E:E, Transactions!H:H, "10") |

Input tax:
| 12 | Tax invoices received | =SUMIFS(Transactions!E:E, Transactions!H:H, "12") |
| 13 | Fixed assets (subset of 12) | =SUMIFS(Transactions!E:E, Transactions!H:H, "13") |
| 14 | Credit card / cash receipt purchases | =SUMIFS(Transactions!E:E, Transactions!H:H, "14") |
| 15 | Total input tax | =SUM(input VAT from Lines 12, 14) |

Calculation:
| 16 | Net tax | =Line 6 - Line 15 |
| 17 | Adjustments | [manual: credit notes, bad debt] |
| 18 | Preliminary payment credit | [manual from prior preliminary return] |
| 19 | Carried-forward credit | [manual from prior period] |
| 20 | Tax payable / refundable | =Line 16 + Line 17 - Line 18 - Line 19 |
```

### Color and formatting conventions

Blue for hardcoded values from bank statement. Black for formulas. Green for cross-sheet references. Yellow background for any row where Default = "Y". Red background for entertainment or vehicle entries (blocked).

---

## Section 8 -- Korean bank statement reading guide (거래내역)

**Korean bank statement format conventions.** Korean banks (KB Kookmin, Shinhan, Woori, Hana) export statements in Excel (XLS/XLSX), CSV, or PDF. Date format: YYYY.MM.DD or YYYY-MM-DD. Common columns: 거래일 (date), 적요 or 거래내용 (description), 출금 (debit/withdrawal), 입금 (credit/deposit), 잔액 (balance). Some banks include 거래점 (branch), 메모 (memo), and 거래구분 (transaction type).

**Transaction types.** 이체 (transfer), 카드결제 (card payment), 자동이체 (automatic transfer/direct debit), 현금입금 (cash deposit), 현금출금 (cash withdrawal), 수표 (check), 대출 (loan), 이자 (interest).

**Hangul descriptions.** Most descriptions are in Korean. Common terms: 급여 (salary), 임대료 (rent), 보험료 (insurance premium), 전기요금 (electricity), 통신요금 (telecoms), 세금 (tax), 수수료 (fee/commission), 이자 (interest), 배당 (dividend).

**Internal transfers.** Between the client's own accounts. Labelled 자기이체, 본인이체, 계좌이체 (own transfer). Always exclude.

**Card payments.** Credit/debit card charges appear with the merchant name, often abbreviated. 쿠팡 = Coupang, 네이버 = Naver, 카카오 = Kakao, 배민 = Baemin (배달의민족). Card charges are important for VAT because credit card sales slips (신용카드매출전표) serve as input VAT evidence on Line 14.

**Salary payments.** Outgoing 급여, 월급, 상여금 (salary, monthly pay, bonus) to employee names. Exclude -- outside VAT scope.

**Tax payments.** 부가세, 소득세, 법인세, 원천세, 국세 to NTS or 지방세 to local government. Exclude -- tax payments, not supplies.

**Insurance premiums.** 보험료 to insurance company names. Exempt financial service -- exclude.

**Foreign currency entries.** Some banks show USD, EUR, JPY amounts alongside KRW equivalent. Use the KRW amount. If only foreign currency is shown, convert at the 매매기준율 (market base rate) from the Bank of Korea for the transaction date.

**Refunds and reversals.** 환불, 반품, 취소 (refund, return, cancellation). Book as negative in the same line as the original. Ensure a revised e-tax invoice (수정세금계산서) has been issued.

**Cryptic descriptions.** Some entries show only a transaction number or abbreviated code. Ask the client for clarification. Do not classify unidentified transactions.

---

## Section 9 -- Onboarding fallback (only when inference fails)

### 9.1 Business registration number (사업자등록번호)
*Inference rule:* 10-digit format XXX-XX-XXXXX may appear in transfer descriptions or e-tax invoice data. *Fallback question:* "What is your 사업자등록번호?"

### 9.2 Business type
*Inference rule:* if client asks for a VAT return with e-tax invoices, they are 일반과세자. If revenue seems low and they mention simplified filing, likely 간이과세자. *Fallback question:* "Are you a 일반과세자 (general taxpayer), 간이과세자 (simplified taxpayer), or 면세사업자 (exempt operator)?"

### 9.3 Filing period
*Inference rule:* first and last transaction dates on the statement. Semi-annual periods: Jan-Jun (Period 1) or Jul-Dec (Period 2). *Fallback question:* "Which period -- Period 1 (Jan-Jun) or Period 2 (Jul-Dec)? Is this a preliminary (quarterly) or final (semi-annual) return?"

### 9.4 Industry and sector
*Inference rule:* counterparty mix, income patterns. *Fallback question:* "What is your business activity?"

### 9.5 Exempt supplies
*Inference rule:* presence of medical, educational, financial, or residential rental income. *Fallback question:* "Do you make any exempt supplies (면세)? If so, what proportion of your revenue?"

### 9.6 Annual revenue
*Inference rule:* extrapolate from period income. *Fallback question:* "What is your approximate annual revenue? (Determines simplified taxpayer eligibility at KRW 104M threshold.)"

### 9.7 E-tax invoice usage
*Inference rule:* if corporation or revenue >= KRW 80M, mandatory. *Fallback question:* "Do you issue e-tax invoices (전자세금계산서)?"

### 9.8 Import activities
*Inference rule:* customs payments, foreign-currency debits for goods. *Fallback question:* "Do you import goods? (Customs VAT recovery rules apply.)"

### 9.9 Prior period credit
*Inference rule:* not inferable from single period. Always ask. *Question:* "Do you have a carried-forward refund (전기 미환급세액) from the prior period?"

### 9.10 Cross-border digital services
*Inference rule:* SaaS debits to foreign names. *Fallback question:* "Do you subscribe to foreign digital services (SaaS, cloud)? (Reverse charge may apply.)"

---

## Section 10 -- Reference material

### Sources

**Primary legislation:**
1. VAT Act (부가가치세법) -- Articles 4, 5-8, 9-11, 24-28, 30, 32, 36, 38, 39, 40, 45, 46, 48, 49, 52, 53-2, 60, 61-68
2. VAT Act Enforcement Decree (부가가치세법 시행령) -- Articles 17, 33, 35, 44, 80, 81, 82, 87, 109, 111
3. Framework Act on National Taxes (국세기본법) -- Articles 45, 47-2, 47-3, 47-4, 47-5
4. Restriction of Special Taxation Act (조세특례제한법)

**NTS guidance:**
5. HomeTax (홈택스) -- https://hometax.go.kr
6. NTS e-tax invoice system and completion notes
7. NTS simplified taxpayer guidance

### Known gaps

1. The supplier pattern library covers common national brands but not every regional business or local shop.
2. The worked examples are from a hypothetical Seoul IT consultant. Sector-specific examples (manufacturing, retail, hospitality) should be added in v2.1.
3. Simplified taxpayer industry value-added ratios may be updated by NTS -- verify annually.
4. The KRW 104M simplified taxpayer threshold and KRW 48M payment exemption threshold are as of July 2024 -- verify for changes.
5. The KRW 80M e-tax invoice threshold for individuals may change.
6. Partial exemption apportionment (Article 40) is simplified here; complex multi-activity businesses need specialist review.

### Change log

- **v2.0 (April 2026):** Full rewrite to Malta v2.0 structure. Quick reference at top (Section 1) with 10% rate, semi-annual filing, e-tax invoice requirements, and conservative defaults. Supplier pattern library restructured as literal lookup tables (Section 3) with Korean vendors. Six worked examples added (Section 4). Tier 1 rules compressed (Section 5). Tier 2 catalogue added (Section 6). Excel template specification added (Section 7). Korean bank statement reading guide (거래내역) added (Section 8). Onboarding fallback with inference rules (Section 9).
- **v1.0 (April 2026):** Previous version with full monolithic structure.

### Self-check (v2.0)

1. Quick reference at top with 10% rate and e-tax invoice requirements: yes (Section 1).
2. Semi-annual filing with quarterly preliminary returns explicit: yes (Section 1).
3. Conservative defaults with Korean-specific values: yes (Section 1).
4. Supplier library as literal lookup tables with Korean vendors: yes (Section 3, 12 sub-tables).
5. Worked examples from hypothetical Seoul IT consultant: yes (Section 4, 6 examples).
6. Tier 1 rules compressed: yes (Section 5, 12 rules).
7. Tier 2 catalogue compressed: yes (Section 6, 10 items).
8. Excel template specification: yes (Section 7).
9. Korean bank statement reading guide (거래내역): yes (Section 8).
10. Onboarding as fallback with inference rules: yes (Section 9, 10 items).
11. Entertainment hard-block (접대비, Art. 39(1)4) explicit: yes (Section 5.6, Example 4).
12. Vehicle hard-block (비영업용 소형승용차, Art. 39(1)5) explicit: yes (Section 5.6, Example 5).
13. Reverse charge on imported services (Art. 52) explicit: yes (Section 5.7, Example 3).
14. Credit card input deduction without e-tax invoice (Line 14) explicit: yes (Section 5.5, Example 6).
15. Refusal catalogue present: yes (Section 2, R-KR-1 through R-KR-6).

## End of South Korea VAT Return Skill v2.0


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
