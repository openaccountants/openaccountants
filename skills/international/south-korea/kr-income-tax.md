---
name: kr-income-tax
description: >
  Use this skill whenever asked about South Korean income tax for self-employed individuals. Trigger on phrases like "comprehensive income tax", "종합소득세", "global income tax Korea", "사업소득", "business income Korea", "간편장부", "simplified bookkeeping", "복식부기", "double-entry Korea", "local income tax surtax", "estimated tax Korea", "Korean income tax return", "Hometax Korea", "Kakao Pay income", "Naver Pay settlement", "KakaoBank statement", or any question about filing or computing income tax for a Korean freelancer or self-employed person. This skill covers progressive brackets (6--45%), local income tax (10% surtax), bookkeeping methods, standard deduction rates, personal deductions, estimated tax, filing deadlines, and penalties. ALWAYS read this skill before touching any Korean income tax work.
version: 2.0
jurisdiction: KR
tax_year: 2025
category: international
depends_on:
  - income-tax-workflow-base
---

# South Korea Income Tax (종합소득세) -- Self-Employed Skill v2.0

---

## Section 1 -- Quick Reference

| Field | Value |
|---|---|
| Country | South Korea (대한민국) |
| Tax | Comprehensive Income Tax (종합소득세) + Local Income Tax (지방소득세, 10% surtax) |
| Currency | KRW only |
| Tax year | Calendar year (1 January -- 31 December) |
| Primary legislation | Income Tax Act (소득세법) |
| Supporting legislation | Local Tax Act (지방세법); Tax Procedures Act (국세기본법) |
| Tax authority | National Tax Service (국세청, NTS) |
| Filing portal | Hometax (hometax.go.kr) |
| Filing deadline | 31 May of the following year |
| Contributor | Open Accountants Community |
| Validated by | Pending -- requires sign-off by a qualified 세무사 (tax accountant) or 공인회계사 (CPA) |
| Skill version | 2.0 |

### National Tax Rate Table (2025) [T1]

| Taxable Income (KRW) | Rate | Deduction Amount (누진공제) |
|---|---|---|
| 0 -- 14,000,000 | 6% | 0 |
| 14,000,001 -- 50,000,000 | 15% | 1,260,000 |
| 50,000,001 -- 88,000,000 | 24% | 5,760,000 |
| 88,000,001 -- 150,000,000 | 35% | 15,440,000 |
| 150,000,001 -- 300,000,000 | 38% | 19,940,000 |
| 300,000,001 -- 500,000,000 | 40% | 25,940,000 |
| 500,000,001 -- 1,000,000,000 | 42% | 35,940,000 |
| Above 1,000,000,000 | 45% | 65,940,000 |

**Formula:** Tax = (Taxable Income x Rate) - Deduction Amount.

**Local Income Tax:** Add 10% of national income tax. Total effective rate = national tax x 110%.

### Standard Deduction Rates (기준/단순경비율) -- Selected Business Types [T1]

| Business Type (업종) | Simplified Deduction Rate (단순경비율) | Standard Deduction Rate (기준경비율) |
|---|---|---|
| IT/software services | ~72% | ~17% |
| Design / creative services | ~69% | ~18% |
| Consulting / management advice | ~67% | ~17% |
| Retail trade | ~87% | ~10% |
| Restaurant / food service | ~88% | ~8% |
| Professional services (doctors, lawyers) | ~65% | ~15% |
| Education / tutoring | ~73% | ~16% |

*Exact rates are set annually by NTS. Confirm current rates on Hometax.*

### Bookkeeping Thresholds [T1]

| Revenue Threshold | Required Method |
|---|---|
| Below KRW 48,000,000 (most service industries) | Simplified bookkeeping (간편장부) permitted |
| KRW 48,000,000 -- below double-entry threshold | Simplified bookkeeping OR double-entry |
| Above KRW 75,000,000 (service) / 150,000,000 (manufacturing) | Double-entry bookkeeping (복식부기) required |

### Conservative Defaults [T1]

| Ambiguity | Default |
|---|---|
| Business type unknown | STOP -- business type determines deduction rate |
| Bookkeeping method unknown | Simplified bookkeeping (간편장부) |
| Deduction method unclear | Standard deduction rate (기준경비율) -- more conservative |
| Estimated tax paid unknown | Nil -- will result in penalty calculation |
| Family deduction eligibility unclear | No deduction until confirmed |

### Red Flag Thresholds [T1]

| Flag | Threshold |
|---|---|
| Double-entry bookkeeping required | Revenue > KRW 75,000,000 (services) |
| Estimated tax (중간예납) required | Prior year tax > KRW 300,000 |
| VAT registration required | Revenue > KRW 48,000,000 (standard) |
| Tax accountant (세무사) recommended | Revenue > KRW 100,000,000 |

---

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

**Minimum viable:** Bank statement for the full calendar year (January--December) in CSV, PDF, or pasted text, plus confirmation of business type (업종 코드) and bookkeeping method.

**Recommended:** Withholding tax (원천징수) certificates from clients, prior year tax return, estimated tax (중간예납) payment receipts, national health insurance (국민건강보험) and pension (국민연금) payment receipts.

**Ideal:** Complete books of accounts (간편장부 or 복식부기), all client invoices, expense receipts, asset register, prior year tax assessment (납세고지서).

### Refusal Catalogue

**R-KR-1 -- Foreign residents / non-residents.** "Non-resident taxation of Korean-source income has different rules. Out of scope -- escalate."

**R-KR-2 -- Corporations (법인).** "Corporations file Corporate Tax (법인세). Out of scope."

**R-KR-3 -- Financial income global taxation (금융소득 종합과세).** "If interest + dividends exceed KRW 20,000,000, these must be included in comprehensive income. Complex analysis required -- escalate."

**R-KR-4 -- Real estate income and capital gains.** "Real estate rental income and gains on disposal require separate computation under different schedules. Escalate."

**R-KR-5 -- Foreign income / DTAA.** "Cross-border income requires tax treaty analysis. Escalate."

---

## Section 3 -- Transaction Pattern Library

This is the deterministic pre-classifier. When a bank statement line matches a pattern, apply the treatment directly. If no pattern matches, fall through to Tier 1 rules in Section 5.

### 3.1 Income Patterns (Credits -- 입금)

| Pattern | Tax Line | Treatment | Notes |
|---|---|---|---|
| 타행입금 [client name] / 이체입금 | 사업소득 (business income) | Gross revenue | Wire transfer from business client |
| 자동이체 입금 [client] | 사업소득 | Revenue | Auto-transfer standing order from client |
| 카카오페이 입금 / KAKAOPAY | 사업소득 | Revenue | KakaoTalk Pay settlement -- digital platform |
| 네이버페이 정산 / NAVERPAY | 사업소득 | Revenue | Naver Pay e-commerce settlement |
| 쿠팡페이 정산 / COUPANG | 사업소득 | Revenue | Coupang marketplace settlement |
| 토스 입금 / TOSS CREDIT | 사업소득 | Revenue | Toss digital payment receipt |
| 원천징수 후 입금 | 사업소득 (gross-up required) | Revenue -- GROSS UP | Client withheld 3.3% (local 0.33%); gross up to invoice amount |
| 급여이체 [employer] | 근로소득 | NOT business income | Employment salary |
| 이자입금 / 이자수익 [bank] | 이자소득 | NOT business income | Bank interest -- separate income type |
| 배당금 입금 | 배당소득 | NOT business income | Dividend income |
| 세금환급 국세청 | EXCLUDE | Not income | Tax refund |
| 대출금 입금 | EXCLUDE | Not income | Loan proceeds |

### 3.2 Expense Patterns (Debits -- 출금)

| Pattern | Tax Category | Treatment | Notes |
|---|---|---|---|
| 사무실임대료 / 임차료 [landlord] | 임차료 (rent) | Fully deductible | Business premises rent |
| 공과금 / 전기요금 [KEPCO/한국전력] | 수도광열비 (utilities) | Business portion deductible | Home office: apportion |
| 도시가스 / 가스요금 | 수도광열비 | Business portion deductible | Apportion if home office |
| 인터넷 요금 [KT/SK브로드밴드/LG유플러스] | 통신비 (communications) | Business portion deductible | Mixed use: apportion |
| 휴대폰 요금 [SK텔레콤/KT/LG유플러스] | 통신비 | Business portion deductible | Mixed use: apportion |
| 교통비 [대중교통/버스/지하철] | 여비교통비 (travel) | Deductible if business | T-money/Cashbee transit charges |
| KTX / SRT [train] | 여비교통비 | Deductible if business purpose | Keep boarding pass |
| 대한항공 / 아시아나 / 저비용항공사 | 여비교통비 | Deductible if business | |
| 접대비 / 식사 [restaurant] | 접대비 (entertainment) | Limited deduction | Cap applies; document names, purpose |
| 도서비 [Kyobo/Aladin] | 소모품비 (consumables) | Deductible if professional literature | |
| 교육훈련비 [Fastcampus/패스트캠퍼스/학원] | 교육훈련비 | Fully deductible if business-related | |
| Adobe / Microsoft / Google Workspace | 소모품비 / 임차료 | Deductible if business | Subscription: current expense |
| Figma / Notion / Slack | 소모품비 | Deductible | Business SaaS |
| 세무사 수수료 | 지급수수료 (professional fees) | Fully deductible | Tax accountant fees |
| 법무사 / 변호사 수수료 | 지급수수료 | Deductible if business-related | Legal fees |
| 국민건강보험 / 건보 | 소득공제 (NOT 필요경비) | EXCLUDE from business expenses | Health insurance = income deduction |
| 국민연금 / 연금보험료 | 소득공제 (NOT 필요경비) | EXCLUDE from business expenses | Pension = income deduction |
| 종합소득세 납부 / 소득세 | EXCLUDE | Tax payment | Not deductible |
| 지방소득세 납부 | EXCLUDE | Local tax payment | Not deductible |
| 중간예납 국세청 | EXCLUDE | Estimated tax prepayment | Credit against final liability |
| 개인인출 / 본인출금 | EXCLUDE | Drawings | Not business expense |

### 3.3 Platform and Digital Payment Patterns

| Pattern | Treatment | Notes |
|---|---|---|
| 카카오뱅크 이체 / KakaoBank Transfer | Business income | Confirm client vs personal transfer |
| 토스뱅크 입금 / TossBank Credit | Business income | Digital bank receipt |
| 케이뱅크 이체 / K bank | Business income | Digital bank |
| 네이버파이낸셜 / 네이버페이 | Business income | Naver Pay settlement |
| 원천징수 3.3% | Revenue gross-up required | National 3% + local 0.3%; client deducted before paying |

### 3.4 Withholding Tax (원천징수) -- 3.3% Rate

Most self-employed Koreans have 3.3% withheld by corporate clients (national 3% + local income tax 0.3%). This appears in bank statements as net amounts.

**Rule:** Always gross up to the full invoice amount. The withheld 3.3% is a tax credit on the final return.

Example: Client pays KRW 966,700 (net of 3.3% withholding on KRW 1,000,000 invoice). Report gross income KRW 1,000,000; claim KRW 33,300 as withholding tax credit.

---

## Section 4 -- Worked Examples

### Example 1 -- Standard Client Wire Transfer

**Input line (KB국민은행 Kookmin Bank statement):**
`2025.03.15 | 타행이체 ABC디자인컴퍼니 | 입금 970,100 | 잔액 4,521,300`

**Reasoning:**
Wire transfer from a business client. KRW 970,100 received is likely net of 3% national withholding tax. If the invoice was KRW 1,000,000, client withheld KRW 30,000 (3%) and paid KRW 970,000. The local income tax portion (0.3% = KRW 3,000) was also withheld separately. Total gross income: KRW 1,000,000. Total withholding credit: KRW 33,000.

**Classification:** 사업소득 KRW 1,000,000 (gross). Withholding credit KRW 33,000.

### Example 2 -- Kakao Pay Settlement

**Input line (카카오뱅크 KakaoBank statement):**
`2025-05-10 | 카카오페이 정산 | +350,000 | 잔고 2,840,000`

**Reasoning:**
KakaoTalk Pay settlement for goods/services sold. This is a digital platform payout representing revenue earned. Check KakaoPay business dashboard for gross sales vs fees.

**Classification:** 사업소득 KRW 350,000 (or gross up if platform fees deducted separately).

### Example 3 -- National Pension Premium

**Input line (신한은행 Shinhan Bank statement):**
`2025-04-30 | 국민연금보험료 자동이체 | -268,500 | 잔액 1,450,200`

**Reasoning:**
National pension premium (국민연금) KRW 268,500. This is NOT a business expense (필요경비). It is an income deduction (소득공제) -- deducted from total income after business income is computed. The full amount paid is deductible as a social insurance premium deduction.

**Classification:** EXCLUDE from 필요경비. Record as 국민연금 소득공제.

### Example 4 -- Estimated Tax Payment

**Input line (우리은행 Woori Bank statement):**
`2025-11-30 | 국세청 중간예납 | -450,000 | 잔액 3,210,000`

**Reasoning:**
Estimated tax (중간예납) payment to NTS. This is a prepayment of income tax -- NOT a business expense. Self-employed persons with prior year tax liability > KRW 300,000 must pay an estimated tax instalment in November.

**Classification:** EXCLUDE. Record as 중간예납 KRW 450,000 (credit against final liability).

### Example 5 -- Business Meal (Entertainment)

**Input line (하나은행 KEB Hana Bank statement):**
`2025-07-22 | 음식점 강남ABC식당 | -88,000 | 잔액 2,125,000`

**Reasoning:**
Restaurant meal KRW 88,000. Entertainment expenses (접대비) are deductible but subject to annual limits under NTS rules. Document: date, restaurant, purpose, names of attendees. Without documentation, the deduction is disallowed.

**Classification:** 접대비 KRW 88,000. Deductible if documented. Subject to annual cap.

### Example 6 -- Adobe Creative Cloud

**Input line (KEB하나은행 statement):**
`2025-09-01 | ADOBE SYSTEMS | -80,000 | 잔액 3,870,000`

**Reasoning:**
Adobe Creative Cloud monthly subscription KRW 80,000. Business software used for design services. Classified as 소모품비 (consumables) -- subscription. Fully deductible as a business expense.

**Classification:** 소모품비 KRW 80,000. Fully deductible.

---

## Section 5 -- Tier 1 Rules (When Data Is Clear)

### 5.1 Business Income Computation Methods

**Legislation:** Income Tax Act (소득세법) Arts. 27-55

Three methods exist, applied based on revenue and bookkeeping:

| Method | Who | How |
|---|---|---|
| Double-entry (복식부기) | Required above threshold; option for all | Actual revenue minus actual expenses. Most accurate. |
| Simplified bookkeeping (간편장부) | Available below threshold | Actual revenue minus documented expenses |
| Standard deduction (기준경비율 / 단순경비율) | No books maintained | Revenue minus major expenses, then multiplied by standard rate |

### 5.2 Tax Computation Flow

```
Total business revenue (총수입금액)
Less: Necessary expenses (필요경비) -- actual or standard rate
= Business income (사업소득금액)
Plus: Other income (근로소득, 이자소득, 배당소득, 연금소득)
= Total income (종합소득금액)
Less: Income deductions (소득공제)
= Taxable income (과세표준) -- round down to 10,000 KRW
Apply national rate table
= National income tax (산출세액)
Less: Tax credits (세액공제)
= National income tax due
x 1.10 (add local income tax 10%)
= Total tax
Less: Withholding credits (원천징수)
Less: Estimated tax paid (중간예납)
= Final tax due / refund
```

### 5.3 Income Deductions (소득공제)

| Deduction | Amount |
|---|---|
| Basic deduction (기본공제) | KRW 1,500,000 per person (self, spouse, dependents) |
| Additional deduction -- elderly (70+) | KRW 1,000,000 per person |
| Additional deduction -- disabled | KRW 2,000,000 per person |
| Pension insurance premium (국민연금) | Full amount paid |
| National health insurance (국민건강보험) | Full amount paid |
| Employment insurance (고용보험) | Full amount paid |

### 5.4 Tax Credits (세액공제)

| Credit | Amount |
|---|---|
| Standard credit (표준세액공제) | KRW 70,000 (if no other special deductions claimed) |
| Child tax credit | KRW 150,000 per child (age ≤ 7: KRW 200,000) |
| Pension savings credit | 12% or 15% of pension contributions (up to limits) |

### 5.5 Estimated Tax / Prepayment (중간예납)

**Legislation:** Income Tax Act Art. 65

- Required when prior year comprehensive income tax > KRW 300,000
- Amount: approximately 50% of prior year tax
- Due: 30 November (payment window: 1--30 November)
- NTS issues a notice (중간예납세액 납부고지서)

### 5.6 Filing Deadlines

| Item | Deadline |
|---|---|
| Comprehensive income tax return | 31 May of the following year |
| Payment | 31 May (or in instalments with NTS approval) |
| Estimated tax (중간예납) | 30 November of the current year |
| VAT return (if applicable) | 25 January and 25 July (biannual) |

### 5.7 Penalties

| Offence | Penalty |
|---|---|
| Late filing (무신고) | 20% of tax due (or 40% if fraudulent) |
| Under-reporting (과소신고) | 10% of additional tax (or 40% if fraudulent) |
| Late payment (납부불성실) | 0.022% per day (approx. 8% per year) |
| Failure to keep records | KRW 200,000--2,000,000 |

---

## Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Regime / Method Selection

Choosing between actual expenses (복식부기 / 간편장부) and the standard deduction rate (기준경비율) requires comparing actual documented expenses vs the standard deduction rate applied to revenue. For most service businesses with low costs (consulting, IT), actual bookkeeping yields lower taxable income.

Flag for reviewer to compute both and select the lower-tax method.

### 6.2 Home Office (가사관련비 按分)

Korea allows apportionment of home expenses for self-employed persons working from home. Acceptable basis: floor area ratio. Utilities, internet, and proportionate rent (if renting) are deductible at the business-use percentage.

### 6.3 Entertainment Expense Cap (접대비)

Entertainment expenses for sole proprietors are capped under NTS guidance. The annual cap depends on the type of business. Document every meal with names, business purpose, and receipts.

### 6.4 Vehicle Expenses

Korea allows deduction of vehicle expenses for business-use vehicles. For passenger vehicles used for both business and personal purposes, a vehicle usage log (운행기록부) is required.

**Flag for reviewer:** Confirm vehicle type, business-use percentage, and documentation method.

### 6.5 Withholding Credit Reconciliation

Self-employed persons often receive net amounts after 3.3% withholding. At year-end, clients must issue a withholding receipt (원천징수영수증). Reconcile bank inflows against withholding receipts to ensure all income is reported gross and all withholding is claimed as credits.

---

## Section 7 -- Excel Working Paper Template

```
종합소득세 WORKING PAPER -- Tax Year 2025
납세자 (Taxpayer): _______________  사업자번호: ___________
업종 코드 (Business type code): ___________
장부 방법 (Bookkeeping): 복식부기 / 간편장부 / 기준경비율 [circle one]

A. 총수입금액 (GROSS REVENUE)
  A1. Total business revenue (gross, before withholding) ___________

B. 필요경비 (NECESSARY EXPENSES)
  B1. 임차료 (rent)                           ___________
  B2. 수도광열비 (utilities -- business %)    ___________
  B3. 통신비 (communications -- business %)  ___________
  B4. 여비교통비 (travel)                    ___________
  B5. 접대비 (entertainment -- capped)       ___________
  B6. 광고선전비 (advertising)               ___________
  B7. 소모품비 (consumables / SaaS)         ___________
  B8. 감가상각비 (depreciation)             ___________
  B9. 외주비 (subcontracting)               ___________
  B10. 지급수수료 (professional fees)       ___________
  B11. 기타경비 (other expenses)            ___________
  B12. Total 필요경비                        ___________

C. 사업소득금액 (A1 - B12)                   ___________

D. 소득공제 (INCOME DEDUCTIONS)
  D1. 기본공제 (basic deduction)             ___________
  D2. 국민연금 (pension premiums)            ___________
  D3. 국민건강보험 (health insurance)        ___________
  D4. 기타 공제                              ___________
  D5. Total 소득공제                         ___________

E. 과세표준 (C - D5, round down to 10,000)   ___________

F. 산출세액 (national tax per rate table)    ___________

G. 세액공제 (TAX CREDITS)
  G1. 표준세액공제 / other credits           ___________

H. NATIONAL TAX DUE (F - G1)               ___________

I. 지방소득세 (H x 10%)                     ___________

J. TOTAL TAX (H + I)                        ___________

K. 원천징수 공제 (withholding credits 3.3%) ___________

L. 중간예납 (estimated tax paid)            ___________

M. FINAL TAX DUE / REFUND (J - K - L)      ___________

REVIEWER FLAGS:
  [ ] Business type code confirmed?
  [ ] All withholding receipts (원천징수영수증) collected?
  [ ] Estimated tax (중간예납) credited?
  [ ] Pension/health insurance correctly in 소득공제 (not 필요경비)?
  [ ] Entertainment cap applied?
  [ ] Double-entry threshold checked for this business?
```

---

## Section 8 -- Bank Statement Reading Guide

### Korean Bank Statement Formats

| Bank | Format | Key Fields |
|---|---|---|
| KB국민은행 (Kookmin) | CSV / PDF | 거래일, 거래내용, 출금금액, 입금금액, 잔액 |
| 신한은행 (Shinhan) | CSV | 거래일자, 적요, 출금액, 입금액, 잔액 |
| 우리은행 (Woori) | CSV | 날짜, 내용, 출금, 입금, 잔액 |
| KEB하나은행 (Hana) | CSV | 거래일, 거래내용, 출금(원), 입금(원), 잔액(원) |
| 카카오뱅크 (KakaoBank) | CSV | 거래일시, 거래내용, 출금금액, 입금금액, 잔액 |
| 토스뱅크 (TossBank) | CSV / App | 날짜, 내용, 금액, 잔액 |
| 케이뱅크 (K bank) | CSV | 거래일, 내용, 출금, 입금, 잔액 |

### Key Korean Banking Terms

| Korean Term | English | Classification Hint |
|---|---|---|
| 타행이체 입금 | Transfer from another bank | Potential business income |
| 자동이체 입금 | Auto-transfer credit | Regular income from client |
| 카드결제 | Card payment | Expense |
| ATM출금 / 자동화기기 | ATM withdrawal | Personal -- investigate |
| 세금이체 / 국세청 | Tax payment | Tax payment -- exclude |
| 공과금 자동이체 | Utility auto-debit | Business or personal expense |
| 이자입금 | Interest credit | Other income |
| 중간예납 | Estimated tax prepayment | Tax credit |
| 원천징수 후 수령 | Received after withholding | Gross up 3.3% |

---

## Section 9 -- Onboarding Fallback

If the client provides a bank statement but cannot answer onboarding questions immediately:

1. Classify all wire transfer credits from non-personal accounts as potential 사업소득
2. Assume all client payments are net of 3.3% withholding -- gross up
3. Mark all 국민연금 and 국민건강보험 auto-debits as income deductions (NOT expenses)
4. Apply conservative defaults: simplified bookkeeping, standard deduction rate
5. Flag all large purchases (> KRW 500,000) for review -- potential capital assets

Present these questions:

```
ONBOARDING QUESTIONS -- SOUTH KOREA 종합소득세
1. What is your main business type (업종)? Do you have an 업종코드?
2. Did you maintain simplified (간편장부) or double-entry (복식부기) books?
3. What is your total gross revenue for 2025 (before 3.3% withholding)?
4. Did any corporate clients withhold 3.3%? If so, do you have withholding receipts (원천징수영수증)?
5. Did you pay estimated tax (중간예납) in November 2025?
6. Marital status and number of dependents?
7. National pension (국민연금) total paid in 2025?
8. National health insurance (국민건강보험) total paid in 2025?
9. Do you use a vehicle for business? If so, do you keep a driving log (운행기록부)?
10. Did you work from a home office? If so, what % of your home is used for business?
```

---

## Section 10 -- Reference Material

### Key Legislation

| Topic | Article |
|---|---|
| Comprehensive income (종합소득) | Income Tax Act Art. 4 |
| Business income (사업소득) | ITA Art. 27 |
| Necessary expenses (필요경비) | ITA Art. 27, 33-35 |
| Income deductions (소득공제) | ITA Art. 50-55 |
| Tax credits (세액공제) | ITA Art. 56-66 |
| Estimated tax (중간예납) | ITA Art. 65 |
| Bookkeeping obligation | ITA Art. 160 |
| Local income tax | Local Tax Act Art. 86-92 |

### Known Gaps / Out of Scope

- Non-resident Korean-source income
- Financial income global taxation (금융소득 종합과세, > KRW 20M)
- Real estate capital gains (양도소득세)
- Corporate income tax (법인세)
- International income / DTAA

### Changelog

| Version | Date | Change |
|---|---|---|
| 2.0 | April 2026 | Full rewrite to v2.0 structure; Korean bank formats; local platform patterns (KakaoTalk Pay, Naver Pay, Toss); worked examples |
| 1.0 | 2025 | Initial version |

### Self-Check

- [ ] Business type (업종) confirmed? Standard deduction rate varies by type.
- [ ] All client payments grossed up from net-of-withholding amounts?
- [ ] Local income tax (10%) added to national tax?
- [ ] National pension and health insurance in 소득공제, NOT 필요경비?
- [ ] Estimated tax (중간예납) credited against final liability?
- [ ] Double-entry threshold checked? Revenue > KRW 75M (services) requires 복식부기.

---

## PROHIBITIONS

- NEVER compute income without confirming the business type (업종) -- standard deduction rates differ by industry
- NEVER treat 3.3% withheld amounts as income -- always gross up to invoice amount
- NEVER include national pension or health insurance as business expenses -- they are income deductions (소득공제)
- NEVER omit the 10% local income tax surtax on national income tax
- NEVER allow income tax or local tax payments as deductible expenses
- NEVER advise on non-resident taxation -- escalate
- NEVER present tax calculations as definitive -- always label as estimated and direct client to their 세무사 for confirmation

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a 세무사, 공인회계사, or equivalent licensed practitioner in South Korea) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
