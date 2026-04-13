---
name: thailand-vat
description: Use this skill whenever asked to prepare, review, or classify transactions for a Thailand VAT (ภาษีมูลค่าเพิ่ม) return (PP.30), classify transactions for Thai VAT purposes, or advise on VAT registration and filing in Thailand. Trigger on phrases like "ภาษีมูลค่าเพิ่ม", "Thai VAT", "PP.30", "VAT Thailand", "Revenue Department Thailand", or any Thailand VAT request. ALWAYS read this skill before touching any Thailand VAT work.
version: 2.0
jurisdiction: TH
tax_year: 2025
category: international
depends_on:
  - vat-workflow-base
---

# Thailand VAT (ภาษีมูลค่าเพิ่ม) Skill v2.0

---

## Section 1 — Quick reference

| Field | Value |
|---|---|
| Country | Thailand (ราชอาณาจักรไทย) |
| Tax | ภาษีมูลค่าเพิ่ม (Phaasi Mun Lak Phoem — VAT) |
| Currency | THB (Thai Baht / บาท) |
| Tax year | Calendar year (1 Jan – 31 Dec) |
| Standard rate | 7% (reduced from 10%; currently extended to 2025 — verify) |
| Zero rate | 0% (exports of goods; services provided in Thailand but used abroad; international transport) |
| Exempt | Agricultural products (unprocessed), educational services, medical/health services, domestic land transport, financial services (interest, insurance premiums), cultural/religious services |
| Registration threshold | THB 1,800,000/year |
| Tax authority | กรมสรรพากร Revenue Department (RD) |
| Return form | แบบ ภ.พ.30 (PP.30) — monthly VAT return |
| Filing portal | E-Filing: https://efiling.rd.go.th |
| Filing deadline | 15th of following month (paper); 23rd of following month (e-filing) |
| Key tax invoice | ใบกำกับภาษี (Bai Kamkap Phaasi) — required for input credit |
| Tax ID | เลขประจำตัวผู้เสียภาษี (13-digit tax ID) |
| Contributor | Open Accountants Community |
| Validated by | Pending — requires sign-off by a Thai-licensed CPA or tax consultant |
| Skill version | 2.0 |

### Key PP.30 return lines

| Line | Meaning |
|---|---|
| 1 | Sales subject to 7% VAT (net) |
| 2 | Output VAT at 7% |
| 3 | Zero-rated sales (exports) |
| 4 | Exempt sales |
| 5 | Total purchases with input VAT (net) |
| 6 | Total input VAT claimed |
| 7 | Net VAT payable (line 2 − line 6) |
| 8 | Excess input credit carried forward |
| 9 | Penalties and surcharges (if any) |
| 10 | Net amount payable |

### Conservative defaults

| Ambiguity | Default |
|---|---|
| Unknown rate on a sale | 7% standard rate |
| Unknown counterparty country | Domestic Thailand |
| Unknown whether export qualifies for 0% | 7% until export evidence confirmed |
| Unknown business-use % (vehicle, phone) | 0% input credit |
| Unknown whether tax invoice is compliant | No input credit |
| Unknown whether supply is exempt or taxable | Taxable at 7% |
| Unknown B2B vs B2C for cross-border services | B2C — 7% if consumed in Thailand |

### Red flag thresholds

| Threshold | Value |
|---|---|
| HIGH single transaction | THB 100,000 |
| HIGH tax delta on single default | THB 7,000 |
| MEDIUM counterparty concentration | >40% of output or input |
| MEDIUM conservative default count | >4 per period |
| LOW absolute net VAT position | THB 50,000 |

---

## Section 2 — Required inputs and refusal catalogue

### Required inputs

**Minimum viable** — bank statement for the month in CSV, PDF, or pasted text. Confirmation of VAT registration number (เลขประจำตัวผู้เสียภาษีอากร).

**Recommended** — ใบกำกับภาษี (tax invoices) for all input credits claimed, sales invoices for all output, prior month PP.30 and credit carried forward.

**Ideal** — complete purchase/sales ledger, export documentation (ใบขนสินค้า customs declaration), asset register.

**Refusal if minimum missing — SOFT WARN.** No bank statement = hard stop. "Input VAT credits require compliant ใบกำกับภาษี (tax invoices). All credits are provisional pending invoice verification."

### Refusal catalogue

**R-TH-1 — Non-VAT registered businesses.** "Businesses below the THB 1.8M threshold are not required to register. They cannot charge VAT and cannot recover input VAT. This skill covers VAT-registered businesses only."

**R-TH-2 — Special business tax (ธุรกิจเฉพาะ).** "Banks, financial institutions, and life insurance companies pay Specific Business Tax (SBT / ภาษีธุรกิจเฉพาะ) instead of VAT. Out of scope."

**R-TH-3 — Partial exemption proration.** "If the business makes both taxable and exempt supplies, input VAT must be apportioned. The apportionment requires annual sales ratios and is out of scope without the full-year data — escalate."

**R-TH-4 — Withholding VAT (VAT ถูกหัก ณ ที่จ่าย).** "Government agencies and designated businesses act as VAT withholders — they remit the VAT portion of payments directly to the Revenue Department. If your client has significant government contracts, withholding VAT offsets must be tracked. Flag for specialist review."

**R-TH-5 — Digital economy platforms.** "Non-resident digital service providers with B2C supplies > THB 1.8M must register under the Digital Economy VAT rules. Out of scope for domestic filers."

---

## Section 3 — Supplier pattern library

Match by case-insensitive substring on counterparty name or reference. Most specific match wins. Fall through to Section 5 if no match.

### 3.1 Thai banks — fees and charges (exempt / exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| ธนาคารกรุงเทพ, BANGKOK BANK, BBL | EXCLUDE (fee lines) | Financial service — exempt |
| ธนาคารกสิกรไทย, KASIKORNBANK, KBANK | EXCLUDE (fee lines) | Same |
| ธนาคารไทยพาณิชย์, SCB, SIAM COMMERCIAL | EXCLUDE (fee lines) | Same |
| ธนาคารกรุงไทย, KRUNGTHAI, KTB | EXCLUDE (fee lines) | Same |
| ธนาคารกรุงศรี, KRUNGSRI, BAY, BANK OF AYUDHYA | EXCLUDE (fee lines) | Same |
| ทีเอ็มบีธนชาต, TTB BANK | EXCLUDE (fee lines) | Same |
| ธนาคารออมสิน, GOVERNMENT SAVINGS BANK, GSB | EXCLUDE (fee lines) | Same |
| ธนาคารอิสลาม, ISLAMIC BANK OF THAILAND | EXCLUDE (fee lines) | Same |
| ค่าธรรมเนียม, ดอกเบี้ย, FEE, INTEREST | EXCLUDE | Bank fee/interest — exempt |

### 3.2 Thai government and statutory payments (exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| กรมสรรพากร, REVENUE DEPARTMENT, RD | EXCLUDE | Tax payment |
| ภาษีมูลค่าเพิ่ม, ภาษีเงินได้ | EXCLUDE | Tax remittance |
| ประกันสังคม, SOCIAL SECURITY OFFICE, SSO | EXCLUDE | Social insurance |
| กรมศุลกากร, CUSTOMS DEPARTMENT | EXCLUDE | Customs duty |
| กรมสรรพสามิต, EXCISE DEPARTMENT | EXCLUDE | Excise duty |
| กองทุนเงินทดแทน | EXCLUDE | Compensation fund |

### 3.3 Thai utilities (taxable at 7%)

| Pattern | Treatment | Rate | Notes |
|---|---|---|---|
| การไฟฟ้านครหลวง, MEA, METROPOLITAN ELECTRICITY | Input 7% | 7% | Electricity (Bangkok) — taxable |
| การไฟฟ้าส่วนภูมิภาค, PEA, PROVINCIAL ELECTRICITY | Input 7% | 7% | Electricity (provinces) — taxable |
| การประปานครหลวง, MWA, METROPOLITAN WATERWORKS | Input 7% | 7% | Water (Bangkok) — taxable |
| การประปาส่วนภูมิภาค, PWA, PROVINCIAL WATERWORKS | Input 7% | 7% | Water (provinces) — taxable |
| ปตท, PTT, PTT PUBLIC | Input 7% | 7% | Natural gas/fuel — taxable |
| AIS, ADVANCED INFO SERVICE | Input 7% | 7% | Mobile/internet — taxable |
| DTAC, TOTAL ACCESS | Input 7% | 7% | Mobile — taxable |
| TRUE MOVE, TRUE CORPORATION | Input 7% | 7% | Mobile/internet — taxable |
| DITO THAILAND | Input 7% | 7% | Mobile — taxable |
| ทีโอที, TOT | Input 7% | 7% | Fixed-line — taxable |

### 3.4 Transport and logistics

| Pattern | Treatment | Rate | Notes |
|---|---|---|---|
| การรถไฟ, SRT, STATE RAILWAY OF THAILAND | EXEMPT | 0% | Domestic land transport — exempt |
| รถไฟฟ้าบีทีเอส, BTS SKYTRAIN | EXEMPT | 0% | Mass transit — exempt |
| รถไฟฟ้ามหานคร, MRT BANGKOK | EXEMPT | 0% | Mass transit — exempt |
| บริษัท ขนส่ง, TRANSPORT CO (bus) | EXEMPT | 0% | Public bus — exempt |
| การบินไทย, THAI AIRWAYS, TG | Check route | 0%/7% | International 0%; domestic 7% |
| แอร์เอเชีย, AIR ASIA, FD | Check route | 0%/7% | International 0%; domestic 7% |
| บางกอก แอร์เวยส์, BANGKOK AIRWAYS | Check route | 0%/7% | Domestic 7%; international 0% |
| GRAB THAILAND | Input 7% | 7% | Ride-hailing — taxable |
| BOLT THAILAND | Input 7% | 7% | Ride-hailing — taxable |
| LINEMAN, LINE MAN | Input 7% | 7% | Delivery platform — taxable |
| ไปรษณีย์ไทย, THAILAND POST | Input 7% | 7% | Parcel services — taxable |
| KERRY EXPRESS, KERRY LOGISTICS | Input 7% | 7% | Courier — taxable |
| FLASH EXPRESS, แฟลช เอ็กซ์เพรส | Input 7% | 7% | Courier — taxable |
| J&T EXPRESS THAILAND | Input 7% | 7% | Courier — taxable |

### 3.5 Food and retail

| Pattern | Treatment | Rate | Notes |
|---|---|---|---|
| เซเว่น-อีเลฟเว่น, 7-ELEVEN THAILAND, CPF | Input 7% | 7% | All items 7% in Thailand (no food reduced rate) |
| เทสโก้ โลตัส, TESCO LOTUS, LOTUS'S | Input 7% | 7% | Hypermarket — 7% on all |
| บิ๊กซี, BIG C SUPERCENTER | Input 7% | 7% | Hypermarket — 7% |
| แม็คโคร, MAKRO | Input 7% | 7% | Wholesale — 7% |
| ท็อปส์ มาร์เก็ต, TOPS MARKET | Input 7% | 7% | Supermarket — 7% |
| ครัวบ้าน (RESTAURANT) | Input 7% | 7% | Restaurant — taxable (no block in Thailand) |
| แมคโดนัลด์, MCDONALD'S THAILAND | Input 7% | 7% | Fast food — 7% |
| KFC THAILAND | Input 7% | 7% | Fast food — 7% |

### 3.6 SaaS — local Thai suppliers (7%)

| Pattern | Treatment | Rate | Notes |
|---|---|---|---|
| JOBBKK, จ๊อบบีเคเค | Input 7% | 7% | Thai job board — taxable |
| JOBSDB THAILAND | Input 7% | 7% | HR platform — taxable |
| WONGNAI | Input 7% | 7% | Thai platform — taxable |
| LAZADA THAILAND (local entity) | Input 7% | 7% | E-commerce — taxable |
| SHOPEE THAILAND (local entity) | Input 7% | 7% | E-commerce — taxable |

### 3.7 SaaS — international suppliers (reverse charge)

For B2B digital services received from abroad: the Thai VAT-registered recipient must self-assess and remit 7% VAT (under the reverse charge equivalent). Foreign suppliers with B2C sales > THB 1.8M must register separately.

| Pattern | Billing entity | Treatment | Notes |
|---|---|---|---|
| GOOGLE (Workspace, Ads, Cloud) | Google Asia Pacific | Reverse charge 7% | Self-assess and remit |
| MICROSOFT (365, Azure) | Microsoft regional | Reverse charge 7% | Self-assess |
| ADOBE | Adobe Inc (US) | Reverse charge 7% | Self-assess |
| META, FACEBOOK ADS | Meta Ireland/US | Reverse charge 7% | Self-assess |
| SLACK | Salesforce/Slack | Reverse charge 7% | Self-assess |
| ZOOM | Zoom Video | Reverse charge 7% | Self-assess |
| NOTION | Notion Labs (US) | Reverse charge 7% | Self-assess |
| ANTHROPIC, CLAUDE | Anthropic (US) | Reverse charge 7% | Self-assess |
| OPENAI, CHATGPT | OpenAI (US) | Reverse charge 7% | Self-assess |
| AWS | Amazon (US/SG) | Reverse charge 7% | Self-assess |

### 3.8 Payment processors (exempt)

| Pattern | Treatment | Notes |
|---|---|---|
| STRIPE (transaction fees) | EXCLUDE | Financial service — exempt |
| PAYPAL (fees) | EXCLUDE | Same |
| OMISE (fees) | EXCLUDE | Thai payment gateway — exempt fees |
| 2C2P (fees) | EXCLUDE | Thai payment processor — exempt fees |

### 3.9 Internal transfers and exclusions

| Pattern | Treatment | Notes |
|---|---|---|
| โอนเงินภายใน, INTERNAL TRANSFER | EXCLUDE | Internal movement |
| เงินกู้, LOAN, เงินให้กู้ | EXCLUDE | Loan principal |
| เงินเดือน, SALARY, ค่าจ้าง | EXCLUDE | Wages — outside VAT scope |
| เงินปันผล, DIVIDEND | EXCLUDE | Out of scope |
| เงินประกัน, DEPOSIT | EXCLUDE | Deposit — out of scope until applied |
| ถอนเงินสด, ATM | Tier 2 — ask | Default exclude |

---

## Section 4 — Worked examples

Six classifications from a hypothetical Bangkok-based IT consultant. Format: ธนาคารกสิกรไทย (KBank) CSV export. Note: Thai calendar uses Buddhist Era (BE) — 2568 = 2025 CE.

### Example 1 — Domestic B2B revenue (7%)

**Input line:**
`15/04/2568  โอนเงินรับ  บริษัท เทค โซลูชั่น จำกัด  เลขที่: INV-2025-041  +535,000.00  THB`

**Reasoning:**
Incoming THB 535,000 from a Thai company for IT consulting. Standard 7% VAT. Gross THB 535,000 includes VAT. Net = THB 500,000 (taxable base) + THB 35,000 output VAT. A ใบกำกับภาษี (tax invoice) must be issued showing the client's 13-digit tax ID, seller's registration, and VAT breakdown. Report net on PP.30 line 1.

**Classification:** Output VAT 7% — THB 35,000. Net sales: THB 500,000.

### Example 2 — Export service (zero-rated)

**Input line:**
`22/04/2568  รับโอนเงินตราต่างประเทศ  ACME CORP USA  Technical consulting Q1  +USD 15,000 (THB 540,000)`

**Reasoning:**
USD receipt from a US company for services used abroad. Zero-rated export service. Evidence: contract showing foreign client, services performed for use outside Thailand, FX transfer record. Report THB 540,000 on PP.30 line 3 (zero-rated). Output VAT: THB 0. If export qualification cannot be confirmed: default 7%.

**Classification:** Zero-rated — THB 540,000. Output VAT: THB 0.

### Example 3 — Utility expense (7%, input credit)

**Input line:**
`10/04/2568  หักค่าไฟฟ้า  การไฟฟ้านครหลวง MEA  ค่าไฟ มีนาคม 2568  -10,700.00  THB`

**Reasoning:**
Monthly electricity from MEA (Metropolitan Electricity Authority). Taxable at 7%. Gross THB 10,700. Net = THB 10,000 + THB 700 input VAT. MEA issues a compliant ใบกำกับภาษี — input credit of THB 700 claimable. Report on PP.30 line 6.

**Classification:** Input VAT 7% — THB 700. Net expense: THB 10,000.

### Example 4 — International SaaS (reverse charge)

**Input line:**
`08/04/2568  ตัดบัญชี  GOOGLE ASIA PACIFIC  Google Workspace April  -3,210.00  THB`

**Reasoning:**
Google Workspace billed from Singapore entity. Foreign B2B digital service. Thai VAT-registered business must self-assess 7% VAT. THB 3,210 is net; self-assessed VAT = THB 3,210 × 7% = THB 225. This appears as both output (PP.30 line 2) and input (PP.30 line 6) — net effect zero for a fully taxable business. Must be documented separately.

**Classification:** Reverse charge 7% — self-assess THB 225 output; THB 225 input credit.

### Example 5 — Exempt transport (Bangkok MRT)

**Input line:**
`05/04/2568  ตัดบัญชี  MRT กรุงเทพ  ค่าโดยสาร  -1,200.00  THB`

**Reasoning:**
MRT (mass rapid transit) fare. Domestic land passenger transport is exempt from VAT under the Revenue Code. No input VAT on the purchase. EXCLUDE from VAT computation. This is a business expense for income tax but generates no input credit.

**Classification:** EXEMPT — no input VAT. Exclude from PP.30.

### Example 6 — Restaurant (7%, no block in Thailand)

**Input line:**
`12/04/2568  บัตรเครดิต  ร้านอาหาร ครัวไทย  อาหารกลางวัน ลูกค้า  -3,210.00  THB`

**Reasoning:**
Restaurant meal for a client lunch. In Thailand — unlike Malta or the UK — there is no absolute block on entertainment or meal input VAT. Meals at restaurants are taxable at 7%. A compliant tax invoice from the restaurant gives input credit. However, to be safe: flag if no ใบกำกับภาษี is available. Thai Revenue Department scrutinises entertainment claims — ensure business purpose is documented.

**Classification:** Input VAT 7% — THB 210 (if compliant tax invoice held). Net expense: THB 3,000. Flag: confirm ใบกำกับภาษี available.

---

## Section 5 — Tier 1 rules (compressed)

### 5.1 Standard rate 7%

Default rate for all taxable supplies. Currently set at 7% (reduced from the statutory 10%) by Royal Decree; extensions renewed periodically. Legislation: Revenue Code (ประมวลรัษฎากร) Section 80; Royal Decree on VAT rate reduction.

### 5.2 Zero rate 0%

Exports of goods and services used outside Thailand; international transport of goods and passengers; services rendered in Thailand but consumed entirely abroad (evidence required). Legislation: Revenue Code Section 80/1.

### 5.3 Exempt supplies

Agricultural products (raw/unprocessed), educational services, health and medical services, domestic passenger transport (land and water), residential rent, interest/financial services, insurance, cultural/religious services. No output VAT; no input credit on attributable costs. Legislation: Revenue Code Section 81.

### 5.4 Tax invoice (ใบกำกับภาษี) requirements

Required fields: seller's name/address/tax ID, buyer's name/address/tax ID (for B2B), sequential invoice number, date, description, net amount, VAT rate, VAT amount. A simplified tax invoice (ใบกำกับภาษีอย่างย่อ) is allowed for retail sales below THB 1,000 per transaction but does not support input credit claims.

### 5.5 Withholding VAT

When government agencies or designated private companies pay a VAT-registered supplier, they withhold the VAT portion (7%) and remit it directly to the Revenue Department. The supplier records the full sale (including VAT) as revenue but receives only the net amount. The withheld VAT is credited against PP.30 output tax. Track withholding tax certificates (ใบรับรองการหักภาษี ณ ที่จ่าย).

### 5.6 Registration threshold

THB 1,800,000 per year in taxable supplies. Once exceeded, must register within 30 days. Voluntary registration available below the threshold. Legislation: Revenue Code Section 85.

### 5.7 Filing deadlines

| Method | Deadline |
|---|---|
| Paper filing | 15th of following month |
| E-filing (efiling.rd.go.th) | 23rd of following month |
| Late surcharge | 1.5% per month on unpaid VAT |
| Late filing penalty | THB 300–500 |

### 5.8 Penalties

| Offence | Penalty |
|---|---|
| Late payment surcharge | 1.5% per month of unpaid tax |
| Late filing | THB 300–500 fine |
| Failure to issue tax invoice | Fine up to THB 2,000 per invoice |
| Fraudulent invoice | Fine up to 2× VAT evaded + potential criminal |

---

## Section 6 — Tier 2 catalogue

### 6.1 Domestic vs. international transport classification

**What it shows:** Airline or transport charge where the route is unclear.
**What's missing:** Whether domestic (7%) or international (0%).
**Conservative default:** 7% domestic.
**Question to ask:** "Is this a domestic or international flight/transport? Please confirm the route."

### 6.2 Export service qualification

**What it shows:** Revenue from a foreign client.
**What's missing:** Whether the service was consumed outside Thailand.
**Conservative default:** 7% standard rate.
**Question to ask:** "Were these services entirely used/consumed outside Thailand? Is there a contract confirming this? Was payment received in foreign currency?"

### 6.3 Mixed-use vehicle expenses

**What it shows:** Fuel, parking, car lease, or maintenance.
**What's missing:** Business-use percentage.
**Conservative default:** 0% input credit.
**Question to ask:** "Is this vehicle used exclusively for business? What percentage is business vs. personal?"

### 6.4 Tax invoice availability for restaurant/entertainment

**What it shows:** Restaurant or entertainment expense.
**What's missing:** Whether a compliant ใบกำกับภาษี was obtained.
**Conservative default:** No input credit.
**Question to ask:** "Did you receive a full tax invoice (ใบกำกับภาษีเต็มรูปแบบ) from this restaurant/venue?"

### 6.5 Withholding VAT from government clients

**What it shows:** Receipt from a government agency that appears lower than the invoiced amount.
**What's missing:** Whether VAT was withheld and a withholding certificate issued.
**Conservative default:** Record full output VAT on invoice amount; credit withheld portion from certificate.
**Question to ask:** "Did this government client withhold VAT? Do you have the withholding certificate?"

---

## Section 7 — Excel working paper template

```
THAILAND VAT WORKING PAPER — แบบคำนวณภาษีมูลค่าเพิ่ม
Period (เดือน): ____________  VAT Registration No.: ____________

A. OUTPUT VAT (ภาษีขาย)
  A1. Taxable sales at 7% (net, ฐานภาษี)     ___________
  A2. Output VAT at 7% (A1 × 7%)             ___________
  A3. Zero-rated sales (ยอดขาย 0%)            ___________
  A4. Exempt sales (ยอดขายยกเว้น)             ___________
  A5. Reverse charge self-assessed output     ___________

B. INPUT VAT (ภาษีซื้อ)
  B1. Domestic purchases — 7% (net)           ___________
  B2. Input VAT at 7% (B1 × 7%)              ___________
  B3. Import VAT paid at customs              ___________
  B4. Reverse charge self-assessed input      ___________
  B5. Total input VAT (B2+B3+B4)             ___________
  B6. Disallowed input (blocked items)        ___________
  B7. Net input VAT (B5 − B6)                ___________

C. NET VAT PAYABLE
  C1. Net VAT (A2 − B7)                       ___________
  C2. Withholding VAT credits                 ___________
  C3. Prior period excess credit              ___________
  C4. Net payable / (credit) (C1−C2−C3)      ___________

REVIEWER FLAGS:
  [ ] Tax invoices (ใบกำกับภาษี) confirmed for all input credits?
  [ ] Export evidence available for zero-rated sales?
  [ ] Government withholding certificates collected?
  [ ] Reverse charge self-assessments documented?
  [ ] Vehicle use % confirmed?
```

---

## Section 8 — Bank statement reading guide

### Common Thai bank statement formats

| Bank | Key columns | Date format | Amount |
|---|---|---|---|
| ธ.กสิกรไทย KBank | วันที่, รายการ, ถอน/โอนออก, ฝาก/โอนเข้า, ยอดคงเหลือ | DD/MM/YYYY (BE) | THB |
| ธ.ไทยพาณิชย์ SCB | Date, Description, Debit, Credit, Balance | DD/MM/YYYY | THB |
| ธ.กรุงเทพ BBL | วันที่ทำรายการ, คำอธิบาย, ถอน, ฝาก, ยอดคงเหลือ | DD/MM/YYYY (BE) | THB |
| ธ.กรุงไทย KTB | Date, Narrative, Withdrawal, Deposit, Balance | DD/MM/YYYY | THB |
| ธ.กรุงศรี Krungsri | วันที่, รายละเอียด, เดบิต, เครดิต, ยอดเงินคงเหลือ | DD/MM/YYYY (BE) | THB |

**Important:** Thai bank statements often use Buddhist Era (พ.ศ. / BE) dates. BE = CE + 543. Example: 15/04/2568 BE = 15/04/2025 CE.

### Key Thai banking terms

| Thai | Meaning | Classification hint |
|---|---|---|
| โอนเงินรับ / รับโอน | Incoming transfer | Potential revenue |
| โอนเงิน / ตัดบัญชี | Outgoing transfer / debit | Potential expense |
| หักค่า | Auto-deduct | Subscription/utility |
| ดอกเบี้ย | Interest | Exempt |
| ค่าธรรมเนียม | Fee | Bank fee — exempt |
| ยอดคงเหลือ | Balance | Running balance — ignore |
| รายการ / คำอธิบาย | Transaction description | Key classification field |
| ถอนเงิน / ATM | Cash withdrawal | Tier 2 — ask |
| เงินเดือน | Salary | Out of VAT scope |

---

## Section 9 — Onboarding fallback

If the client provides a bank statement but cannot answer all questions immediately:

1. Classify all transactions using the pattern library (Section 3)
2. Apply conservative defaults (Section 1)
3. Mark Tier 2 items as "PENDING — reviewer must confirm"
4. Generate working paper with flags

```
THAILAND VAT ONBOARDING — MINIMUM QUESTIONS
1. VAT registration number (เลขทะเบียนภาษีมูลค่าเพิ่ม — 13 digits starting with a specific format)?
2. What month does this bank statement cover? (Confirm BE or CE year)
3. Do you have any export sales (services used outside Thailand)?
   If yes: is payment received in foreign currency?
4. Do you have government agency clients? Do they withhold VAT?
5. Any vehicle expenses? Business-use percentage?
6. Do you hold ใบกำกับภาษีเต็มรูปแบบ for all major input purchases?
7. Prior month excess credit (ภาษีซื้อส่วนเกิน) carried forward amount?
8. Any international SaaS subscriptions (Google, Microsoft, etc.)?
```

---

## Section 10 — Reference material

### Key legislation

| Topic | Reference |
|---|---|
| VAT general | Revenue Code (ประมวลรัษฎากร) Part 4 (Sections 77–87/1) |
| Standard rate | Revenue Code Section 80; Royal Decree on rate |
| Zero rate | Revenue Code Section 80/1 |
| Exemptions | Revenue Code Section 81 |
| Tax invoice | Revenue Code Section 86/4 |
| Registration | Revenue Code Section 85 |
| Withholding VAT | Revenue Code Section 83/5 |
| Penalties | Revenue Code Sections 89–90 |
| Digital services | Royal Decree No. 694 (2021) |

### Known gaps

- Partial exemption apportionment — escalate if exempt supplies > 5% of total
- Specific Business Tax (SBT) for financial institutions — out of scope
- Government contract withholding VAT reconciliation — flag for specialist
- Property/real estate transactions — escalate
- Reverse charge for non-digital imported services — verify current RD guidance

### Self-check before filing

- [ ] All tax invoices (ใบกำกับภาษี) held for input credits claimed
- [ ] Export services supported by contracts + FX evidence
- [ ] Withholding VAT certificates collected from government clients
- [ ] Reverse charge self-assessed for all foreign digital services
- [ ] BE/CE date conversion correct throughout
- [ ] Prior month excess credit correctly carried forward

### Changelog

| Version | Date | Change |
|---|---|---|
| 1.0 | 2024 | Initial release |
| 2.0 | April 2026 | Full v2.0 rewrite: pattern library, worked examples, no inline tier tags |

---

## Prohibitions

- NEVER apply 10% rate — the current rate is 7% (verify if Royal Decree has not been renewed)
- NEVER block restaurant/entertainment input VAT categorically — Thailand does not have a blanket block (unlike Malta/UK); require tax invoice
- NEVER zero-rate a service without confirming consumption outside Thailand + FX payment
- NEVER omit reverse charge self-assessment for B2B foreign digital services
- NEVER ignore withholding VAT from government clients — offset against output tax
- NEVER present calculations as definitive — direct to a licensed Thai CPA or tax consultant

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes. All outputs must be reviewed by a qualified professional before filing.

The most up-to-date version is maintained at openaccountants.com.
