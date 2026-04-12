---
name: kr-income-tax
description: >
  Use this skill whenever asked about South Korean income tax for self-employed individuals. Trigger on phrases like "comprehensive income tax", "종합소득세", "global income tax Korea", "사업소득", "business income Korea", "간편장부", "simplified bookkeeping", "복식부기", "double-entry Korea", "local income tax surtax", "estimated tax Korea", "Korean income tax return", or any question about filing or computing income tax for a Korean freelancer or self-employed person. Covers progressive brackets (6–45%), local income tax (10% surtax), bookkeeping method thresholds, standard deduction rates, personal deductions, withholding tax (원천징수), filing deadlines, and penalties.
version: 2.0
---

# South Korea Income Tax — Self-Employed (종합소득세)

## Section 1 — Quick Reference

### National Income Tax Brackets (2025)
| Taxable Income (KRW) | Rate | Cumulative Deduction |
|---|---|---|
| 0 – 14,000,000 | 6% | — |
| 14,000,001 – 50,000,000 | 15% | ₩1,260,000 |
| 50,000,001 – 88,000,000 | 24% | ₩5,760,000 |
| 88,000,001 – 150,000,000 | 35% | ₩15,440,000 |
| 150,000,001 – 300,000,000 | 38% | ₩19,940,000 |
| 300,000,001 – 500,000,000 | 40% | ₩25,940,000 |
| 500,000,001 – 1,000,000,000 | 42% | ₩35,940,000 |
| Over 1,000,000,000 | 45% | ₩65,940,000 |

**Formula:** (Taxable income × rate) − cumulative deduction = national income tax
**Local income tax (지방소득세):** 10% of national income tax (assessed separately, filed with municipality)
**Total effective tax:** national tax + local income tax

### Standard Expense Deduction Rates (단순경비율 — Simple Standard Deduction)
For taxpayers below the double-entry bookkeeping threshold who use the simplified standard deduction:
| Business Type | Standard Deduction Rate |
|---|---|
| Retail / wholesale trade | 85–90% |
| Service industry (general) | 60–75% |
| Professional services (doctors, lawyers, engineers) | 60–65% |
| Freelance/creative (writers, designers, artists) | 60–70% |

**Note:** Standard deduction = Revenue × deduction rate. Net income = Revenue − standard deduction. Does not require expense receipts.

### Bookkeeping Threshold (2025)
| Criteria | Required bookkeeping |
|---|---|
| Revenue < ₩75,000,000 (most services) | Simple bookkeeping (간편장부) or standard deduction |
| Revenue ≥ ₩75,000,000 (services) | Double-entry bookkeeping (복식부기) required |
| Revenue < ₩150,000,000 (wholesale/retail) | Simple bookkeeping |
| Revenue ≥ ₩150,000,000 (wholesale/retail) | Double-entry required |
| Professional services (all revenues) | Double-entry always required for tax benefit |

### Key Personal Deductions (인적공제)
| Deduction | Amount |
|---|---|
| Basic personal deduction (본인) | ₩1,500,000 |
| Spouse deduction (income ≤ ₩1,000,000/year) | ₩1,500,000 |
| Dependent deduction (each qualifying dependent) | ₩1,500,000 |
| Elderly (70+) additional deduction | ₩1,000,000 per person |
| Disability additional deduction | ₩2,000,000 per person |
| Single-parent deduction | ₩1,000,000 |

### Key Tax Credits (세액공제)
| Credit | Amount |
|---|---|
| Standard tax credit (소득세액공제) | 7% of national tax (cap ₩740,000 for income < ₩30M; ₩660,000 for ₩30M–₩40M; ₩500,000 for ₩40M–₩70M; reduced for higher) |
| Insurance premium credit | 12% of premiums paid (medical, life, personal pension) |
| Medical expense credit | 15% of expenses > 3% of income |
| Education expense credit | 15% of education costs (children) |
| Political contribution credit | 10%/15% depending on amount |
| Pension account credit (연금계좌세액공제) | 12–15% of pension account contributions |

### Conservative Defaults
| Item | Default |
|---|---|
| Home office % | Do not assume — ask for floor area |
| Vehicle business % | Do not assume — ask for mileage records |
| Phone/internet | 50% if dual-use |
| Bookkeeping method | Assume simple bookkeeping unless double-entry records provided |
| Standard vs actual expenses | Use actual if receipts available and exceed standard deduction |

### Red Flag Thresholds
| Situation | Flag |
|---|---|
| Revenue > ₩75M (services) | Double-entry required — flag if only simple books kept |
| Revenue > ₩100M | VAT registration threshold check |
| Expenses > 80% of revenue | High — verify with receipts |
| Home office > 30% | Aggressive — document |
| No national pension (NPS) contributions | Likely missing deduction — ask |

---

## Section 2 — Required Inputs & Refusal Catalogue

### Minimum Required Inputs
1. Total gross business income (사업소득 총수입금액) for the tax year
2. Bookkeeping method (simple, double-entry, or standard deduction)
3. If actual expenses: itemised expenses with receipts
4. Personal deductions applicable (spouse, children, parents)
5. National Health Insurance (건강보험료) and National Pension (국민연금) premiums paid
6. Withholding taxes (원천징수세액) already paid during the year
7. Advance tax (중간예납) paid (if applicable)

### Refusal Catalogue
**R-KR-1 — No expense documentation**
If actual expense method claimed but no receipts: refuse undocumented expenses. State: "Without receipts or records, we cannot claim these expenses. Consider using the standard deduction rate (단순경비율) instead if your revenue is below the threshold."

**R-KR-2 — Double-entry required but not maintained**
If revenue exceeds the double-entry threshold and client only has simple records: flag as non-compliant. State: "Your revenue requires double-entry bookkeeping. Using the simplified method may result in penalties and a 20% additional tax on the amount not properly recorded."

**R-KR-3 — Personal expenses claimed as business**
Refuse personal costs (personal travel, family meals, school fees) as business expenses. State: "These are personal expenses and cannot be deducted as business expenses under Korean income tax law."

**R-KR-4 — VAT amounts included in income**
VAT (부가가치세) collected from clients must not be included in taxable income. State: "VAT collected is not your income — it must be excluded from business income before computing income tax."

**R-KR-5 — Non-resident claiming resident deductions**
Non-residents are not entitled to personal deductions. State: "Personal deductions are only available to tax residents. Please confirm your residence status."

---

## Section 3 — Transaction Pattern Library

### 3.1 Income Patterns
| Bank Description Pattern | Income Type | Tax Treatment | Notes |
|---|---|---|---|
| 입금 / 이체 + client name | Business income (사업소득) | Include in gross revenue | Verify not a personal transfer |
| 전신환 / 외화 입금 / SWIFT | Foreign client payment | Include — convert to KRW at receipt date rate (KEB Hana/BOK rate) | |
| 세금계산서 발행 거래처 | Invoice payment | Include gross amount | Separate VAT component if registered |
| 플랫폼 정산 (Kakao, Naver, Coupang) | Platform payout | Include gross (net of platform fees = add fees back as expense) | |
| Upwork / Fiverr 입금 | Freelance platform | Include — convert USD to KRW | Platform fee = deductible |
| PayPal 정산 | PayPal payout | Include KRW equivalent | |
| 이자 수입 | Bank interest | 이자소득 — already taxed at source 15.4% | Separate income category |
| 배당금 | Dividend | 배당소득 — separate | Not 사업소득 |
| 임대 수입 | Rental income | 부동산임대소득 — separate schedule | Not 사업소득 |
| 원천징수 후 지급 (net payment) | Withheld income | Gross up: net ÷ (1 − withholding rate) | Withholding = tax credit |

### 3.2 Expense Patterns
| Bank Description Pattern | Expense Category | Deductible? | Notes |
|---|---|---|---|
| SKT / KT / LGU+ 통신비 | Phone | Partial — business % | T2: confirm % |
| KT 인터넷 / LGU+ 가정인터넷 | Internet | Home office % | T2: floor area |
| 전기요금 / 가스요금 / 수도요금 | Utilities | Home office % | T2: floor area |
| 임대료 / 월세 | Rent | Home office % if home; 100% if office | T2 if home |
| 카페 결제 / 스타벅스 (business meeting) | Meals/entertainment | Yes — business purpose documented | Keep receipts with names |
| 교통비 / 지하철 / 버스 | Transport | Yes — business trips | Personal commute excluded |
| 항공권 / 숙박비 | Travel | Yes — business purpose | Document |
| 소프트웨어 / 구독서비스 | Software/SaaS | Yes — 100% | Business tools |
| 도서 / 자료 구매 | Books/research | Yes — business-related | |
| 광고비 / 마케팅 | Advertising | Yes — 100% | |
| 세금계산서 수취 거래처 | B2B expenses | Yes — with 세금계산서 | Required for VAT credit too |
| 건강보험료 (직장가입자 아닌 경우) | National health insurance | Social insurance deduction (별도) | Not a business expense |
| 국민연금 (지역가입자) | National pension | Social insurance deduction (별도) | Not a business expense |
| 부가가치세 납부 | VAT payment | EXCLUDE — not income tax deductible | |
| 소득세 납부 | Income tax payment | EXCLUDE | |
| 은행 수수료 | Bank charges | Yes — 100% | |
| 세무사 / 회계사 비용 | Tax/accounting fees | Yes — 100% | |

### 3.3 Withholding Tax Credits (원천징수)
| Source | Withholding Rate | Treatment |
|---|---|---|
| 사업소득 (services to companies) | 3.3% (3% tax + 0.3% local) | Credit against final tax |
| 이자소득 | 15.4% (14% + 1.4%) | Separate — final withholding usually |
| 프리랜서 방송·예술 소득 | 3.3% | Credit against final tax |
| Foreign wire (no withholding) | 0% at source | Include gross in income |

### 3.4 Platform Payouts (Korea-Specific)
| Platform | Currency | Notes |
|---|---|---|
| Kakao / Kakao Pay | KRW | Net of platform commission; add back as expense |
| Naver Smart Store | KRW | Net payout; gross up for commissions |
| Coupang | KRW | Net payout; gross up |
| Kmong / Soomgo | KRW | Freelance platforms; net payout |
| YouTube Korea (AdSense) | USD | Convert to KRW monthly |

### 3.5 Internal Transfers
| Pattern | Treatment |
|---|---|
| 본인 계좌 간 이체 | EXCLUDE — internal transfer |
| 적금 / 예금 이체 | EXCLUDE — savings movement |
| 카드값 자동이체 | EXCLUDE — expense captured individually |
| 대출금 입금 | EXCLUDE — not income |

---

## Section 4 — Worked Examples

### Example 1 — Shinhan Bank: IT Freelancer, Simple Bookkeeping
**Scenario:** IT consultant, ₩60,000,000 gross revenue, actual expenses ₩15,000,000, 3.3% withholding ₩1,980,000 already deducted

**Bank statement extract (신한은행):**
```
거래일자      | 적요                              | 출금(원)      | 입금(원)      | 잔액(원)
2025.04.15   | 이체 ㈜테크솔루션                    |               | 4,850,000     | 28,400,000
2025.04.20   | 이체 프리랜서닷컴 정산               |               | 1,650,000     | 30,050,000
2025.04.25   | 자동이체 AWS Korea                  | 320,000        |               | 29,730,000
2025.04.28   | 자동이체 SKT 통신비                  | 89,000         |               | 29,641,000
2025.04.30   | 신한은행 수수료                      | 500            |               | 29,640,500
```

**Note on 3.3% withholding:** Client companies often pay net: e.g., ₩5,000,000 gross → ₩165,000 withheld → ₩4,835,000 deposited. Always gross up deposits where withholding applies.

**Calculation:**
| Line | Amount |
|---|---|
| Gross business income | ₩60,000,000 |
| Actual expenses (receipts) | (₩15,000,000) |
| Business income | ₩45,000,000 |
| Personal deductions (self) | (₩1,500,000) |
| **Taxable income** | **₩43,500,000** |
| National tax (15% bracket: ₩43,500,000 × 15% − ₩1,260,000) | ₩5,265,000 |
| Less: tax credits (standard credit) | (₩660,000) |
| Less: withholding credit | (₩1,980,000) |
| **National tax payable** | **₩2,625,000** |
| Local income tax (10%) | ₩262,500 |
| **Total tax** | **₩2,887,500** |

### Example 2 — KB Kookmin Bank: Designer, Standard Deduction
**Scenario:** Freelance designer, ₩40,000,000 gross, uses standard deduction (62% rate), no receipts maintained

**Bank statement extract (KB국민은행):**
```
거래일       | 내용                                | 찾으신 금액    | 맡기신 금액    | 잔액
25-03-10    | 타행이체 디자인스튜디오봄               |                | 3,200,000      | 15,600,000
25-03-15    | 인터넷뱅킹 이체 프리모션㈜              |                | 2,000,000      | 17,600,000
25-03-20    | 자동이체 어도비시스템즈                 | 14,000         |                | 17,586,000
25-03-25    | ATM 출금                             | 300,000        |                | 17,286,000
25-03-31    | KB 이체수수료                         | 500            |                | 17,285,500
```

**Standard deduction method:**
- Standard deduction rate for designers: 62%
- Standard deduction: ₩40,000,000 × 62% = ₩24,800,000
- Business income: ₩40,000,000 − ₩24,800,000 = ₩15,200,000

**Calculation:**
| Line | Amount |
|---|---|
| Gross revenue | ₩40,000,000 |
| Standard deduction (62%) | (₩24,800,000) |
| Business income | ₩15,200,000 |
| Personal deduction (self) | (₩1,500,000) |
| **Taxable income** | **₩13,700,000** |
| National tax (6% bracket) | ₩822,000 |
| Less: standard tax credit (7%) | (₩57,540) |
| **National tax payable** | **₩764,460** |
| Local income tax (10%) | ₩76,446 |
| **Total tax** | **₩840,906** |

### Example 3 — Woori Bank: Writer with NPS Deduction
**Scenario:** Freelance writer, ₩35,000,000 gross, ₩8,000,000 actual expenses, married (spouse income ₩0), NPS premium ₩1,485,000, NHI ₩1,200,000

**Bank statement extract (우리은행):**
```
거래일시          | 거래내용                           | 출금금액       | 입금금액       | 잔액
2025-05-12 09:15 | 이체 도서출판사㈜                   |                | 2,500,000      | 12,300,000
2025-05-18 14:30 | 이체 ㈜온라인미디어                  |                | 1,200,000      | 13,500,000
2025-05-22 10:00 | 지로 국민연금공단                   | 247,500        |                | 13,252,500
2025-05-25 09:30 | 지로 건강보험공단                   | 200,000        |                | 13,052,500
2025-05-30 16:45 | 우리은행 수수료                     | 500            |                | 13,052,000
```

**Calculation:**
| Line | Amount |
|---|---|
| Gross revenue | ₩35,000,000 |
| Actual expenses | (₩8,000,000) |
| Business income | ₩27,000,000 |
| Social insurance deduction (NPS ₩1,485,000 + NHI ₩1,200,000) | (₩2,685,000) |
| Personal deduction — self | (₩1,500,000) |
| Personal deduction — spouse | (₩1,500,000) |
| **Taxable income** | **₩21,315,000** |
| National tax (15% bracket: ₩21,315,000 × 15% − ₩1,260,000) | ₩1,937,250 |
| Less: standard credit | (₩135,607) |
| **National tax payable** | **₩1,801,643** |
| Local income tax | ₩180,164 |
| **Total** | **₩1,981,807** |

### Example 4 — Hana Bank: Developer with Foreign Income
**Scenario:** Developer, ₩50,000,000 domestic + USD $30,000 (converted ₩40,000,000) from US client, actual expenses ₩18,000,000

**Bank statement extract (하나은행):**
```
거래일자       | 적요                               | 출금액(원)     | 입금액(원)     | 잔고(원)
2025-06-10    | 외화입금 USD 10,000 COMPANY ABC     |                | 13,500,000     | 45,000,000
2025-06-15    | 타행이체입금 ㈜테크스타트              |                | 8,000,000      | 53,000,000
2025-06-20    | 신용카드결제 AWS Korea              | 450,000        |                | 52,550,000
2025-06-25    | 자동이체 깃허브 엔터프라이즈          | 180,000        |                | 52,370,000
2025-06-30    | 하나은행 수수료                      | 500            |                | 52,369,500
```

**Foreign income:** Convert USD at KEB Hana / Bank of Korea TTM rate on transaction date. Total foreign income ₩40,000,000 (cumulative over year).

**Calculation:**
| Line | Amount |
|---|---|
| Domestic revenue | ₩50,000,000 |
| Foreign revenue (KRW equivalent) | ₩40,000,000 |
| Total gross revenue | ₩90,000,000 |
| Actual expenses | (₩18,000,000) |
| Business income | ₩72,000,000 |
| Social insurance deductions | (₩2,800,000) |
| Personal deduction | (₩1,500,000) |
| **Taxable income** | **₩67,700,000** |
| National tax (24% bracket: ₩67,700,000 × 24% − ₩5,760,000) | ₩10,488,000 |
| Local income tax | ₩1,048,800 |
| **Total** | **₩11,536,800** |

### Example 5 — IBK Industrial Bank: Sole Proprietor with Double-Entry
**Scenario:** Consulting firm (sole proprietor), ₩200,000,000 revenue, ₩120,000,000 expenses (double-entry required), advance tax ₩8,000,000 paid

**Bank statement extract (IBK기업은행):**
```
날짜          | 거래내용                            | 출금           | 입금           | 잔액
2025-08-05   | 이체입금 ㈜대한컨설팅                 |                | 22,000,000     | 185,000,000
2025-08-10   | 이체입금 글로벌비즈니스㈜              |                | 15,000,000     | 200,000,000
2025-08-15   | 이체출금 직원급여 (직원A)             | 3,500,000      |                | 196,500,000
2025-08-20   | 국세 중간예납                        | 8,000,000      |                | 188,500,000
2025-08-25   | 이체출금 사무실임대료                 | 2,000,000      |                | 186,500,000
```

**Calculation:**
| Line | Amount |
|---|---|
| Gross revenue | ₩200,000,000 |
| Business expenses (double-entry) | (₩120,000,000) |
| Business income | ₩80,000,000 |
| Social insurance | (₩3,500,000) |
| Personal deduction | (₩1,500,000) |
| **Taxable income** | **₩75,000,000** |
| National tax (35% bracket: ₩75,000,000 × 35% − ₩15,440,000) | ₩10,810,000 |
| Less: advance tax (중간예납) | (₩8,000,000) |
| **National tax balance due** | **₩2,810,000** |
| Local income tax | ₩281,000 |
| **Total balance** | **₩3,091,000** |

### Example 6 — Kakao Bank: Creator/YouTuber
**Scenario:** YouTuber/content creator, ₩25,000,000 AdSense (USD converted), ₩10,000,000 brand deals, standard deduction used

**Bank statement extract (카카오뱅크):**
```
거래일시              | 내용                               | 보낸금액       | 받은금액       | 잔액
2025.09.05 10:23:11  | 구글 AdSense 입금                  |                | 4,500,000      | 18,200,000
2025.09.12 14:05:33  | 타행입금 마케팅에이전시              |                | 3,000,000      | 21,200,000
2025.09.20 09:45:02  | 이체 쿠팡이츠 저녁식사 (미팅)        | 45,000         |                | 21,155,000
2025.09.25 11:30:45  | 국민연금 자동납부                   | 247,500        |                | 20,907,500
2025.09.30 00:00:01  | 카카오뱅크 이자                    |                | 8,500          | 20,916,000
```

**Standard deduction for creators (65% rate):**
- Total revenue: ₩35,000,000
- Standard deduction: ₩35,000,000 × 65% = ₩22,750,000
- Business income: ₩12,250,000

**Calculation:**
| Line | Amount |
|---|---|
| Gross revenue | ₩35,000,000 |
| Standard deduction (65%) | (₩22,750,000) |
| Business income | ₩12,250,000 |
| NPS deduction | (₩1,485,000) |
| Personal deduction | (₩1,500,000) |
| **Taxable income** | **₩9,265,000** |
| National tax (6%) | ₩555,900 |
| Less: standard credit | (₩38,913) |
| **National tax** | **₩516,987** |
| Local income tax | ₩51,699 |
| **Total** | **₩568,686** |

---

## Section 5 — Tier 1 Rules (Compressed Reference)

### Tax Residency
- **Resident:** Domicile in Korea OR presence ≥ 183 days in tax year → worldwide income taxable
- **Non-resident:** < 183 days → Korea-source income only; withheld at source (no personal deductions)

### Business Income vs Other Income
| Source | Category |
|---|---|
| Freelance, consulting, design, IT services | 사업소득 (business income) |
| Rental income | 부동산임대소득 |
| Interest | 이자소득 |
| Dividends | 배당소득 |
| Employment salary | 근로소득 (separate schedule) |
| Capital gains | 양도소득 (separate, not aggregated) |

**Comprehensive income tax (종합소득세):** Aggregates business, rental, interest, dividend, employment income into one progressive rate. Capital gains computed separately.

### Withholding Tax (원천징수)
- Business services paid by companies: 3.3% withheld (3% national + 0.3% local)
- Gross up all net payments before including in income
- Withholding amounts = credit against final tax liability

### Advance Tax (중간예납)
- If prior year tax ≥ ₩500,000: advance tax required
- 1st installment: November 30 = 50% of prior year final national tax
- Reduce advance tax if current year income significantly lower (감액 신청 by November 1)

### National Pension (국민연금) & National Health Insurance (건강보험)
- Self-employed join as 지역가입자 (regional subscriber)
- NPS premium: ~9% of income (employer+employee combined; self-employed pay full 9%), capped at ₩590,850/month (2025 approx)
- NHI premium: ~6.99% of income, also income-tested for 지역가입자
- Both 100% deductible as social insurance deduction (소득공제)

### Filing Deadlines
| Event | Deadline |
|---|---|
| 종합소득세 return filing | May 31 (following year) |
| Tax payment | May 31 |
| Advance tax (중간예납) | November 30 |
| VAT return (if registered) | Separate — Jan 25 and Jul 25 |

### Penalties
| Situation | Penalty |
|---|---|
| Late filing | 20% of unpaid tax |
| Late payment | 8.03% p.a. (2025 rate) |
| Under-reporting | 10–40% additional tax |
| Double-entry required but not kept | 20% additional tax on net income |

---

## Section 6 — Tier 2 Catalogue

### T2-KR-1: Home Office (사업용 비율 — 주거용 겸용)
**Why T2:** Floor area split is a fact only the client knows.

**Method:** Business area ÷ total area × rent/utilities
**Required from client:** Total floor area (m²), office area (m²), whether space exclusively used for business.

### T2-KR-2: Vehicle Business Use
**Why T2:** Business use proportion depends on actual trips — only client knows.

**Required from client:** Total km driven, business km (logbook or estimate), vehicle operating costs.
**Note:** Korean tax law requires a vehicle logbook (업무용 승용차 운행기록부) for tax deduction of vehicle expenses > ₩15,000,000/year. Without logbook, deduction is capped at ₩15,000,000.

### T2-KR-3: Phone & Internet
**Why T2:** Business/personal split is client-specific.

**Default:** 50% if dual-use; 100% if dedicated business line.
**Required from client:** Whether personal phone is also used for business, estimated business call %.

### T2-KR-4: Standard vs Actual Expenses
**Why T2:** Decision depends on whether actual expenses exceed the standard deduction.

**Guidance:** Calculate both; claim whichever is higher. Standard deduction requires no receipts but may be lower for high-expense businesses. Actual expenses require full documentation.

**Required from client:** Decision on method, and if actual: all receipts.

### T2-KR-5: Family Member Employment
**Why T2:** Whether spouse/family member genuinely works in the business affects deductibility.

**Rules:**
- Salary paid to spouse/family members only deductible if they actually work and are properly registered as employees with NPS/NHI
- Must be reasonable market rate for work performed
- Cannot pay family members for work they don't actually do

---

## Section 7 — Excel Working Paper

### Sheet 1: Revenue Ledger (매출장)
| Column | Content |
|---|---|
| A | Date |
| B | Bank |
| C | Payer |
| D | Gross amount (KRW) |
| E | Withholding (3.3%) deducted |
| F | Net received |
| G | Category (사업소득 / Other / Exclude) |

**Gross up formula (E2):** `=D2/(1-0.033)` (when net amount known)
**Total gross revenue:** `=SUMIF(G:G,"사업소득",D:D)`

### Sheet 2: Expense Ledger (경비장)
| Column | Content |
|---|---|
| A | Date |
| B | Vendor |
| C | Amount (KRW) |
| D | Category |
| E | Business % |
| F | Deductible amount |
| G | Receipt? Y/N |

### Sheet 3: Deduction & Credit Summary
| Line | Amount |
|---|---|
| Gross business income | |
| Standard deduction OR actual expenses | |
| Business income | |
| Social insurance deduction (NPS + NHI) | |
| Personal deductions | |
| **Taxable income** | |
| National tax (per bracket) | |
| Tax credits | |
| Withholding credits (3.3%) | |
| Advance tax credits | |
| **Net tax payable** | |
| Local income tax (10%) | |
| **Total** | |

---

## Section 8 — Bank Statement Reading Guide

### Shinhan Bank (신한은행)
- Format: `거래일자 | 적요 | 출금(원) | 입금(원) | 잔액(원)`
- Date: YYYY.MM.DD
- Income = 입금 column
- Key: 이체 = transfer; 타행이체 = inter-bank transfer

### KB Kookmin Bank (KB국민은행)
- Format: `거래일 | 내용 | 찾으신 금액 | 맡기신 금액 | 잔액`
- Date: YY-MM-DD
- Income = 맡기신 금액

### Woori Bank (우리은행)
- Format: `거래일시 | 거래내용 | 출금금액 | 입금금액 | 잔액`
- Date: YYYY-MM-DD HH:MM:SS
- Income = 입금금액

### Hana Bank (하나은행)
- Format: `거래일자 | 적요 | 출금액(원) | 입금액(원) | 잔고(원)`
- Date: YYYY-MM-DD
- 외화입금 = foreign currency inward remittance

### IBK Industrial Bank (IBK기업은행)
- Format: `날짜 | 거래내용 | 출금 | 입금 | 잔액`
- Date: YYYY-MM-DD
- 국세 중간예납 = advance tax payment → EXCLUDE from expenses

### Kakao Bank (카카오뱅크)
- Format: `거래일시 | 내용 | 보낸금액 | 받은금액 | 잔액`
- Date: YYYY.MM.DD HH:MM:SS
- Income = 받은금액

### Exclusion Patterns (all banks)
| Pattern | Action |
|---|---|
| 본인계좌 이체 / 자기계좌 | EXCLUDE — internal transfer |
| 카드값 자동이체 | EXCLUDE — captured as individual expenses |
| 부가가치세 납부 / 국세 | EXCLUDE — tax payments |
| 중간예납 | Credit against final tax — not expense |
| 대출 입금 | EXCLUDE — not income |
| 적금 만기 입금 | EXCLUDE — return of savings |

---

## Section 9 — Onboarding Fallback

**Priority 1 (blocking):**
1. "What was your total gross business income for the year? Please provide bank statements."
2. "Do you have receipts for business expenses, or should we use the standard deduction rate?"
3. "What is your bookkeeping method — simple bookkeeping (간편장부) or double-entry (복식부기)?"

**Priority 2 (deductions):**
4. "Are you married? Does your spouse have income?"
5. "Do you have children or elderly parents as dependants?"
6. "What were your National Pension and National Health Insurance premiums this year?"
7. "Did you contribute to a personal pension account (연금저축)?"

**Priority 3 (credits and advance tax):**
8. "Were any of your payments made with 3.3% withholding deducted? If so, please provide the withholding statements (원천징수영수증)."
9. "Did you pay advance tax (중간예납) in November? If so, how much?"
10. "Do you have any medical expenses exceeding 3% of your income?"

**Conservative defaults:**
- Use standard deduction if no receipts maintained
- Exclude any expenses without documentation
- Do not claim home office or vehicle unless client provides specific data

---

## Section 10 — Reference Material

### Key Forms
| Form | Purpose |
|---|---|
| 종합소득세 신고서 | Main comprehensive income tax return |
| 사업소득명세서 | Business income schedule |
| 원천징수영수증 | Withholding tax certificate (from payers) |
| 소득공제 신청서 | Deductions claim form |

### Filing Platform
- **홈택스 (Hometax):** hometax.go.kr — NTS (National Tax Service)
- Mobile: 손택스 (Sontax) app
- Filing period: May 1–31 each year

### Key Rates (2025)
| Item | Rate |
|---|---|
| National income tax | 6%–45% progressive |
| Local income tax | 10% of national tax |
| Withholding on services | 3.3% (3% + 0.3%) |
| VAT (별도) | 10% (separate obligation) |

### National Tax Service (NTS)
- Website: nts.go.kr
- Telephone: 126

---

## Prohibitions
- Do not advise on VAT (부가가치세) — separate Korean VAT skill required
- Do not advise on corporate tax (법인세) — sole proprietors only
- Do not advise on capital gains tax (양도소득세) on property or securities — separate schedule
- Do not advise on payroll tax (근로소득세) for employees
- Do not advise on customs duties or import taxes

## Disclaimer
This skill provides general guidance for informational and planning purposes. It does not constitute tax advice. Korean tax law is administered by the National Tax Service (국세청). Clients should consult a licensed 세무사 (tax accountant) registered with the Korea Tax Accountants Association for advice specific to their circumstances. Tax brackets, rates, and deduction amounts are updated annually — verify current rules at nts.go.kr.
