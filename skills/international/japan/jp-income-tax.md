---
name: jp-income-tax
description: >
  Use this skill whenever asked about Japanese income tax for self-employed individuals filing a final tax return (確定申告 Kakutei Shinkoku). Trigger on phrases like "how much tax do I pay in Japan", "kakutei shinkoku", "確定申告", "blue return", "青色申告", "white return", "白色申告", "business income Japan", "事業所得", "necessary expenses", "必要経費", "basic deduction", "基礎控除", "reconstruction tax", "resident tax", "住民税", "self-employed tax Japan", "e-Tax", or any question about filing or computing income tax for a self-employed individual in Japan. Covers progressive brackets (5%-45%) + 2.1% reconstruction surtax + 10% resident tax, blue vs white return special deductions, necessary expenses, social insurance deduction, and filing deadlines.
version: 2.0
---

# Japan Income Tax — Self-Employed (確定申告)

## Section 1 — Quick Reference

### National Income Tax Brackets (2025)
| Taxable Income (JPY) | Rate | Deduction |
|---|---|---|
| 0 – 1,950,000 | 5% | ¥0 |
| 1,950,001 – 3,300,000 | 10% | ¥97,500 |
| 3,300,001 – 6,950,000 | 20% | ¥427,500 |
| 6,950,001 – 9,000,000 | 23% | ¥636,000 |
| 9,000,001 – 18,000,000 | 33% | ¥1,536,000 |
| 18,000,001 – 40,000,000 | 40% | ¥2,796,000 |
| Over 40,000,000 | 45% | ¥4,796,000 |

**Formula:** (Taxable income × rate) − deduction = national income tax
**Reconstruction surtax:** national income tax × 2.1%
**Total national tax:** national income tax + reconstruction surtax
**Resident tax (住民税):** ~10% of taxable income (prefectural 4% + municipal 6%) + per-capita levy (approx. ¥5,000–¥6,000/year); assessed separately and billed June following year

### Key Deductions
| Deduction | Amount |
|---|---|
| Basic deduction (基礎控除) | ¥480,000 (income ≤ ¥24M) |
| Blue return special deduction (青色申告特別控除) | ¥650,000 (e-Tax + double-entry) / ¥550,000 (paper + double-entry) / ¥100,000 (simplified) |
| Social insurance premium deduction | 100% of premiums paid (National Health Insurance + National Pension) |
| Small business mutual aid (小規模企業共済) | 100% of contributions, up to ¥840,000/year |
| iDeCo (individual DC pension) | 100% of contributions, up to ¥816,000/year (self-employed) |
| Spousal deduction | ¥380,000 (spouse income ≤ ¥480,000) |
| Dependent deduction | ¥380,000 per dependent (age 16–69) / ¥630,000 (age 19–22) |
| Medical expense deduction | Actual expenses − ¥100,000 (or 5% of income if lower) |
| Earthquake insurance deduction | Up to ¥50,000 |

### Conservative Defaults (use when client data is missing)
| Item | Default |
|---|---|
| Home office % | Do not assume — ask client for measured floor area ratio |
| Vehicle business % | Do not assume — ask for logbook or estimated business trips |
| Phone/internet business % | 50% unless client provides better split |
| Meals business % | 50% of documented business meals only |
| Blue return status | Assume white return until confirmed |
| Social insurance premiums | Use actual amounts from payment receipts — do not estimate |

### Red Flag Thresholds
| Situation | Flag |
|---|---|
| Revenue > ¥10M | Consumption tax registration likely required — verify |
| Revenue > ¥24M | Basic deduction reduces; check surtax bracket |
| Expenses > 70% of revenue | Unusually high — verify documentation |
| Home office > 30% of floor area | Aggressive — document carefully |
| Vehicle claimed 100% | Rare for non-delivery business — request logbook |
| No National Pension receipts claimed | Likely missing deduction — ask |

---

## Section 2 — Required Inputs & Refusal Catalogue

### Minimum Required Inputs
To complete a Japan income tax calculation the following must be provided:
1. Total gross revenue (売上高) for the tax year
2. Itemised business expenses with supporting receipts or records
3. Whether client has blue return (青色申告) status (requires prior NTA registration by March 15)
4. Social insurance premiums paid (国民健康保険 + 国民年金)
5. Other deductions claimed (iDeCo, 小規模企業共済, medical, dependants)
6. Whether filing via e-Tax or paper

### Refusal Catalogue
**R-JP-1 — No expense documentation**
If the client cannot provide any receipts, invoices, or records for claimed expenses: refuse to include those expenses in the calculation. State: "Without documentation we cannot claim these expenses. Japan requires receipts and records for all necessary expense deductions."

**R-JP-2 — Blue return without prior registration**
If the client wants the ¥650,000 blue return deduction but has not previously registered Form 青色申告承認申請書 with NTA: refuse. State: "Blue return status requires advance registration with the NTA. It cannot be applied retrospectively for the current year."

**R-JP-3 — Personal expenses claimed as business**
If the client attempts to deduct clearly personal costs (school fees, personal travel, personal food without business purpose): refuse. State: "These are personal expenses and cannot be deducted as 必要経費 under Japan income tax law."

**R-JP-4 — Consumption tax included in income**
If bank receipts include consumption tax (消費税) collected: exclude from income calculation. State: "Consumption tax collected from clients is not your income — it must be separated before calculating income tax."

**R-JP-5 — Pre-registration expenses**
Expenses incurred before the business was registered cannot be claimed as business expenses. State: "Pre-commencement expenses before business registration cannot be deducted as 必要経費."

**R-JP-6 — Salary income mixed with business**
If the client has both salaried employment (給与所得) and self-employment (事業所得): separate these income streams. Salary income has different deduction rules (給与所得控除). Do not apply business expense deductions against salary income.

---

## Section 3 — Transaction Pattern Library

### 3.1 Income Patterns
| Bank Description Pattern | Income Type | Tax Treatment | Notes |
|---|---|---|---|
| 振込入金 + client name | Client payment (事業所得) | Gross revenue — add to income | Excl. consumption tax if registered |
| 電信振替 + client name | Client payment | Gross revenue | Same as above |
| 外国送金 / USD wire | Foreign client payment | Convert to JPY at transaction date (TTM rate) | Report in JPY |
| PayPal 入金 | Platform payout | Gross revenue (JPY equivalent) | Use PayPal statement rate |
| Stripe 入金 / STRIPE | Stripe payout | Gross revenue (JPY equivalent) | Net of fees? Add fees back as expense |
| Coconala / Lancers / Crowdworks 入金 | Japanese platform payout | Gross revenue (net received) | Platform fee = deductible expense |
| 利息 / 利子 / INTEREST | Bank interest | 雑所得 (miscellaneous income) — already taxed at source 20.315% | Usually negligible — note separately |
| 配当 / DIVIDEND | Dividend | 配当所得 — separate schedule | Not 事業所得 |
| 不動産収入 / RENT received | Rental income | 不動産所得 — separate schedule | Not 事業所得 |

### 3.2 Expense Patterns
| Bank Description Pattern | Expense Category | 必要経費? | Notes |
|---|---|---|---|
| NTT / ドコモ / au / SoftBank / 楽天モバイル | Phone | Partial — business % only | T2: confirm business use % |
| NTT東日本 / NTT西日本 / internet provider | Internet | Partial — business % only | T2: confirm business use % |
| 電気代 / ガス代 / 水道代 (utility) | Utilities | Home office % only | T2: requires floor area ratio |
| 家賃 / RENT payment | Rent | Home office % only | T2: requires floor area ratio |
| Amazon.co.jp | Office supplies / equipment | Yes if business purpose | Verify — personal purchases excluded |
| ヨドバシ / ビックカメラ / 家電量販店 | Equipment | Yes if business use | Capitalise if > ¥100,000 (or ¥300,000 under special rules) |
| Adobe / Slack / Zoom / Microsoft | Software/SaaS | Yes — 100% | Document business use |
| ChatGPT / Claude / Notion | SaaS tools | Yes — 100% | Document business use |
| 交通費 / JR / 地下鉄 / 私鉄 | Travel (business) | Yes — business trips only | Personal commute excluded |
| 新幹線 / 飛行機 / ANA / JAL | Travel (business) | Yes — business purpose required | Document purpose |
| ホテル / 旅館 / 宿泊 | Accommodation | Yes — business purpose | Document |
| 飲食店 / レストラン | Meals/entertainment | Partial — 50% if business | Must document who, why |
| 書籍 / Amazon books | Books/research | Yes if business-related | Personal reading excluded |
| 保険料 (business) | Business insurance | Yes — 100% | Exclude life insurance (personal) |
| 国民健康保険 | National health insurance | Social insurance deduction (別枠) | Not 必要経費 — separate deduction line |
| 国民年金 / 付加年金 | National pension | Social insurance deduction (別枠) | Not 必要経費 — separate deduction line |
| 小規模企業共済 | Small business mutual aid | Separate deduction — 100% | Not 必要経費 |
| iDeCo / 個人型確定拠出年金 | Individual pension | Separate deduction — 100% | Not 必要経費 |
| 所得税 / 消費税 納付 | Tax payments | EXCLUDE — not 必要経費 | Tax payments are not deductible |
| 振込手数料 / 銀行手数料 | Bank charges | Yes — 100% | Deductible |
| 税理士報酬 / 会計士 | Accountant/tax advisor fees | Yes — 100% | Deductible |
| 交際費 (entertainment) | Entertainment | Partial — document carefully | Must document business purpose |

### 3.3 Foreign Currency & Platform Payments
| Source | Currency | Treatment |
|---|---|---|
| USD/EUR wire from overseas client | Foreign | Convert at TTM rate on transaction date (Bank of Japan reference) |
| Stripe (USD earnings) | USD | Use Stripe payout date JPY amount, or convert at TTM |
| PayPal (multi-currency) | Various | Use PayPal statement JPY equivalent |
| Upwork / Fiverr | USD | Gross USD earned → convert to JPY; platform fee deductible |
| Google AdSense | USD | Monthly payment → convert to JPY |
| Apple / Google Play (app revenue) | USD | Monthly → convert to JPY; use monthly average if transaction-level unavailable |

### 3.4 Internal Transfers
| Pattern | Treatment |
|---|---|
| 振替 between own accounts | EXCLUDE — not income |
| Savings transfer to business account | EXCLUDE — not income |
| Loan repayment received (personal) | EXCLUDE — not income |
| Credit card settlement debit | EXCLUDE — already captured as individual expenses |

---

## Section 4 — Worked Examples

### Example 1 — Mizuho Bank: Freelance Designer, Blue Return
**Scenario:** Freelance graphic designer, blue return (e-Tax), ¥8M gross revenue, ¥2.5M expenses, NHI ¥420,000, pension ¥199,320

**Bank statement extract (Mizuho):**
```
日付          | 摘要                              | お引き出し | お預け入れ | 残高
2025/04/15   | 振込 カブシキガイシャ サクラテック   |            | 1,100,000  | 3,450,000
2025/04/20   | 振込 コムデザイン ゴドウ タロウ      |            |   550,000  | 4,000,000
2025/04/25   | Amazon.co.jp                      |    12,800  |            | 3,987,200
2025/04/28   | 国民健康保険料                      |    35,000  |            | 3,952,200
2025/04/30   | NTT東日本                          |     5,500  |            | 3,946,700
```

**Calculation:**
| Line | Amount |
|---|---|
| Gross revenue (事業収入) | ¥8,000,000 |
| Necessary expenses (必要経費) | (¥2,500,000) |
| Business income (事業所得) | ¥5,500,000 |
| Blue return special deduction (青色申告特別控除) | (¥650,000) |
| Social insurance deduction | (¥619,320) |
| Basic deduction | (¥480,000) |
| **Taxable income** | **¥3,750,680** |
| National income tax (20% bracket: ¥3,750,680 × 20% − ¥427,500) | ¥322,636 |
| Reconstruction surtax (¥322,636 × 2.1%) | ¥6,775 |
| **Total national tax** | **¥329,411** |
| Resident tax estimate (10%) | ~¥375,000 |

### Example 2 — MUFG Bank: IT Consultant, White Return
**Scenario:** IT consultant, white return, ¥12M gross, ¥3M expenses, NHI ¥600,000, pension ¥199,320

**Bank statement extract (三菱UFJ銀行):**
```
お取引日    | お取引内容                         | お引出し金額 | お預入金額  | 残高
25.03.15   | テレコム コンサルティング カブ 振込   |              | 2,200,000   | 8,120,000
25.03.20   | クラウドワークス 振込                |              |   330,000   | 8,450,000
25.03.25   | 所得税 振替納税                      |   285,000    |             | 8,165,000
25.03.28   | 国民年金保険料                        |    16,610    |             | 8,148,390
25.03.31   | 電気代 東京電力                       |    18,500    |             | 8,129,890
```

**Calculation:**
| Line | Amount |
|---|---|
| Gross revenue | ¥12,000,000 |
| Necessary expenses | (¥3,000,000) |
| Business income | ¥9,000,000 |
| White return — no special deduction | ¥0 |
| Social insurance deduction | (¥799,320) |
| Basic deduction | (¥480,000) |
| **Taxable income** | **¥7,720,680** |
| National income tax (23% bracket: ¥7,720,680 × 23% − ¥636,000) | ¥1,139,756 |
| Reconstruction surtax | ¥23,935 |
| **Total national tax** | **¥1,163,691** |
| Resident tax estimate | ~¥772,000 |
| **Switching to blue return saves: ¥650,000 × 23% = ¥149,500** | |

### Example 3 — SMBC: Translator with Foreign Clients
**Scenario:** Freelance translator, blue return (paper), ¥5M revenue (mix of JPY and USD clients), ¥1M expenses

**Bank statement extract (三井住友銀行):**
```
取引日       | 内容                                 | 支払い      | 預かり      | 残高
2025-02-10  | ﾌﾞｲｰｸﾗｲﾅ ｽﾀｼﾞｵ 外国送金 USD         |             | 440,000     | 2,340,000
2025-02-14  | ﾔﾏﾀﾞ ﾎｰﾙﾃﾞｨﾝｸﾞｽ 振込               |             | 330,000     | 2,670,000
2025-02-20  | Adobe Creative Cloud               | 7,480       |             | 2,662,520
2025-02-25  | 新幹線 EX予約                          | 22,440      |             | 2,640,080
```

**USD income note:** Convert USD invoices to JPY at TTM rate on payment date. Keep Bank of Japan daily rate record.

**Calculation:**
| Line | Amount |
|---|---|
| JPY revenue | ¥3,200,000 |
| USD revenue (converted) | ¥1,800,000 |
| Total gross revenue | ¥5,000,000 |
| Necessary expenses | (¥1,000,000) |
| Business income | ¥4,000,000 |
| Blue return special deduction (paper) | (¥550,000) |
| Social insurance deduction | (¥519,320) |
| Basic deduction | (¥480,000) |
| **Taxable income** | **¥2,450,680** |
| National income tax (10% bracket: ¥2,450,680 × 10% − ¥97,500) | ¥147,568 |
| Reconstruction surtax | ¥3,099 |
| **Total national tax** | **¥150,667** |

### Example 4 — Japan Post Bank (ゆうちょ): Photographer
**Scenario:** Freelance photographer, white return, ¥3.5M revenue, ¥900,000 expenses, home office claimed

**Bank statement extract (ゆうちょ銀行):**
```
年月日        | 摘要                     | お支払い金額 | お預かり金額 | 差引残高
令和7年4月8日  | 振替　フォトスタジオ タナカ  |              | 550,000      | 1,820,000
令和7年4月12日 | 振込　オカダ プロダクション  |              | 220,000      | 2,040,000
令和7年4月15日 | 振込手数料                |    330        |              | 2,039,670
令和7年4月20日 | 電気代                   | 12,000        |              | 2,027,670
```

**Home office claim:**
- Apartment: 50 sqm total; studio/office: 12 sqm dedicated
- Home office %: 12/50 = 24%
- Monthly rent ¥120,000 → annual ¥1,440,000 × 24% = ¥345,600 deductible

**Calculation:**
| Line | Amount |
|---|---|
| Gross revenue | ¥3,500,000 |
| Direct business expenses | (¥554,400) |
| Home office (rent ¥345,600 + utilities ¥24,000×24%) | (¥351,360) |
| Total necessary expenses | (¥905,760) |
| Business income (approximate) | ¥2,594,240 |
| Social insurance deduction | (¥519,320) |
| Basic deduction | (¥480,000) |
| **Taxable income** | **¥1,594,920** |
| National income tax (5%) | ¥79,746 |
| Reconstruction surtax | ¥1,675 |
| **Total national tax** | **¥81,421** |

### Example 5 — Shinsei Bank: Developer with iDeCo + 小規模企業共済
**Scenario:** Software developer, blue return (e-Tax), ¥18M revenue, ¥5M expenses, iDeCo ¥816,000, 小規模企業共済 ¥840,000

**Bank statement extract (新生銀行):**
```
取引日        | 取引内容                              | 出金額      | 入金額      | 残高
2025/01/15   | 振込入金　テクスタートカブシキガイシャ   |             | 3,300,000   | 12,450,000
2025/01/20   | iDeCo掛金　SBI証券                  | 68,000      |             | 12,382,000
2025/01/25   | 小規模企業共済掛金                    | 70,000      |             | 12,312,000
2025/01/31   | AWS Amazon Web Services            | 45,000      |             | 12,267,000
```

**Calculation:**
| Line | Amount |
|---|---|
| Gross revenue | ¥18,000,000 |
| Necessary expenses | (¥5,000,000) |
| Business income | ¥13,000,000 |
| Blue return special deduction | (¥650,000) |
| Social insurance deduction (NHI + pension) | (¥800,000) |
| iDeCo deduction | (¥816,000) |
| 小規模企業共済 deduction | (¥840,000) |
| Basic deduction | (¥480,000) |
| **Taxable income** | **¥9,414,000** |
| National income tax (33% bracket: ¥9,414,000 × 33% − ¥1,536,000) | ¥1,570,620 |
| Reconstruction surtax | ¥32,983 |
| **Total national tax** | **¥1,603,603** |
| Resident tax estimate | ~¥941,000 |
| **Total tax if no iDeCo/共済: add back ¥1,656,000 deductions × 33% ≈ ¥546,480 extra tax** | |

### Example 6 — Rakuten Bank: E-commerce / Rakuten seller
**Scenario:** Rakuten shop owner, blue return (e-Tax), ¥6M gross sales, ¥2M COGS + expenses, Rakuten fees included

**Bank statement extract (楽天銀行):**
```
取引日        | 取引説明                             | 支払金額    | 受取金額    | 残高
2025/05/20   | 楽天ペイメント売上入金                  |             | 850,000     | 4,230,000
2025/05/25   | 楽天ペイメント売上入金                  |             | 420,000     | 4,650,000
2025/05/28   | 楽天市場出店料                         | 50,000      |             | 4,600,000
2025/05/30   | ヤマト運輸 送料                         | 78,500      |             | 4,521,500
```

**Important:** Rakuten payouts are net of Rakuten fees. Gross sales = payout + fees withheld. Claim Rakuten commission as expense.

**Calculation:**
| Line | Amount |
|---|---|
| Gross sales (売上高) | ¥6,000,000 |
| Cost of goods sold (仕入高) | (¥1,200,000) |
| Gross profit | ¥4,800,000 |
| Other expenses (Rakuten fees, shipping, etc.) | (¥800,000) |
| Business income | ¥4,000,000 |
| Blue return special deduction | (¥650,000) |
| Social insurance deduction | (¥619,320) |
| Basic deduction | (¥480,000) |
| **Taxable income** | **¥2,250,680** |
| National income tax (10% bracket) | ¥127,568 |
| Reconstruction surtax | ¥2,679 |
| **Total national tax** | **¥130,247** |

---

## Section 5 — Tier 1 Rules (Compressed Reference)

### Residency
- **Tax resident:** Lived in Japan > 12 months OR has 住所 (domicile) in Japan → worldwide income taxable
- **Non-permanent resident:** Foreign national, resident ≤ 5 of last 10 years → Japan-source + remitted foreign income
- **Non-resident:** < 1 year stay → Japan-source income only

### Business Income (事業所得) vs Miscellaneous Income (雑所得)
- NTA 2022 guideline: If gross receipts < ¥300,000/year AND no records kept → likely 雑所得
- If ≥ ¥300,000 or proper books kept → 事業所得
- This matters: 事業所得 losses can offset other income; 雑所得 losses cannot

### Blue Return (青色申告) Requirements
- Must register 青色申告承認申請書 with district NTA office:
  - New business: by 2 months after opening
  - Existing business: by March 15 of the tax year
- Must maintain double-entry bookkeeping for ¥650,000 deduction
- Can carry forward net operating losses 3 years (10 years for certain cases)
- Can deduct salary paid to family members (青色事業専従者給与)

### Depreciation (減価償却)
- Assets ≤ ¥100,000: expensed immediately
- ¥100,001 – ¥300,000 (special SME rule): can expense immediately if elected
- ≥ ¥300,001: must depreciate (定額法 straight-line for most assets)
- PC useful life: 4 years; car: 6 years; furniture: 8 years; buildings (RC): 47 years

### Consumption Tax Note
- If prior year taxable sales > ¥10M: mandatory consumption tax payer
- Consumption tax collected ≠ income — must be separated

### Social Insurance
- National Health Insurance (国民健康保険): varies by municipality; based on prior year income
- National Pension (国民年金): fixed ¥16,980/month (FY2025); 付加年金 ¥400/month additional
- Both 100% deductible as social insurance premium deduction

### Filing Deadlines
| Event | Deadline |
|---|---|
| Kakutei shinkoku filing | February 16 – March 15 (following year) |
| Tax payment | March 15 (same as filing) |
| Advance tax (予定納税) 1st installment | July 31 |
| Advance tax 2nd installment | November 30 |
| Blue return registration (new) | Within 2 months of business opening |
| Blue return registration (existing) | March 15 of applicable tax year |
| Resident tax payment | 4 installments: June, August, October, January |

### Advance Tax (予定納税)
- If prior year national tax ≥ ¥150,000: must pay advance tax
- 1st installment (July 31): 1/3 of prior year tax
- 2nd installment (November 30): 1/3 of prior year tax
- Balance paid with March 15 filing
- Can apply to reduce 予定納税 if income drops (減額申請 by July 15 / November 15)

### Penalties
| Situation | Penalty |
|---|---|
| Late filing | 15% of unpaid tax (+ 5% if > 2 months) |
| Late payment | 2.4% p.a. (up to 2 months) / 8.7% p.a. thereafter |
| Under-reporting | 10% of understated tax |
| Fraud | 35–40% of understated tax |

---

## Section 6 — Tier 2 Catalogue (Data-Unknowable Items)

These items require client-specific information that cannot be determined from bank statements alone.

### T2-JP-1: Home Office (家事按分 — Rent & Utilities)
**Why T2:** Floor area measurements and home/work use split are facts only the client knows.

**Three scenarios:**
1. **Dedicated office room (used exclusively for business):** Deduct room area ÷ total apartment area × rent/utilities. Must be exclusively business — sleeping/living there disqualifies.
2. **Shared space (desk in living room):** Less clear — NTA allows a reasonable proportion. Document desk hours or area used.
3. **No home office:** No deduction. Client must work from external office/café.

**Required from client:** Total apartment floor area (sqm), office/desk area (sqm), confirmation of exclusive use.

**Maximum defensible:** Generally ≤ 30% without detailed records.

### T2-JP-2: Vehicle (自動車費用の按分)
**Why T2:** Business use proportion depends on actual trips made — only the client knows.

**Options:**
1. **Logbook (走行記録):** Record every business trip. Business km ÷ total km = business %.
2. **Estimated %:** Reasonable estimate based on business nature (e.g., delivery business = 80%; office-based consultant = 20%). Document basis.
3. **No vehicle business use:** Exclude entirely.

**Required from client:** Total km driven, business km (from logbook or estimate), car purchase price (for depreciation), insurance, maintenance costs.

### T2-JP-3: Phone & Internet (通信費の按分)
**Why T2:** Personal/business split is a judgement call.

**Guidance:**
- Phone: 50% default if used for both; 80–100% if dedicated business line
- Internet: 50% default for home office; proportional if floor area method used

**Required from client:** Confirmation of whether phone/internet is dual-use or dedicated business.

### T2-JP-4: Meals & Entertainment (交際費・会議費)
**Why T2:** Business purpose and attendee details are client-specific facts.

**Rules:**
- 会議費 (meeting expense, < ¥5,000/person): fully deductible if business meeting documented
- 交際費 (entertainment > ¥5,000/person): deductible but requires recipient name + business purpose
- 50% of meals with no documentation: do not claim

**Required from client:** Who attended, business purpose, receipts with amounts.

### T2-JP-5: Family Member Salary (青色事業専従者給与)
**Why T2:** Reasonableness of salary depends on actual work performed.

**Rules (blue return only):**
- Must file 青色事業専従者給与に関する届出書 with NTA before payment
- Salary must be "appropriate" for work performed — not arbitrary
- Family member filing their own 確定申告 for this salary income

**Required from client:** Family member's role, hours worked, salary amount, whether届出書 was filed.

---

## Section 7 — Excel Working Paper

### Sheet 1: Income Summary
| Column | Content |
|---|---|
| A | Transaction date (YYYY/MM/DD) |
| B | Bank account |
| C | Payee/description |
| D | Amount received (JPY) |
| E | Category (事業収入 / 雑収入 / Exclude) |
| F | Notes |

**Formula (E2 subtotal):** `=SUMIF(E:E,"事業収入",D:D)`

### Sheet 2: Expense Ledger
| Column | Content |
|---|---|
| A | Date |
| B | Vendor |
| C | Amount (JPY) |
| D | Category (rent/utilities/travel/software etc.) |
| E | Business % |
| F | Deductible amount (=C×E) |
| G | Receipt reference |

**Total 必要経費:** `=SUM(F:F)`

### Sheet 3: Deduction Summary
| Deduction | Amount |
|---|---|
| 事業所得 (from Sheet 1 − Sheet 2) | |
| 青色申告特別控除 | |
| 社会保険料控除 (NHI + pension) | |
| 小規模企業共済等掛金控除 | |
| iDeCo | |
| 医療費控除 | |
| 配偶者控除 | |
| 扶養控除 | |
| 基礎控除 | ¥480,000 |
| **課税所得 (Taxable income)** | |

### Sheet 4: Tax Computation
| Line | Formula |
|---|---|
| Taxable income | From Sheet 3 |
| National tax bracket | VLOOKUP against bracket table |
| National income tax | (Taxable income × rate) − deduction |
| 復興特別所得税 | National tax × 2.1% |
| Total national tax | Sum |
| 予定納税 paid | From payment records |
| Balance due / refund | Total − 予定納税 |
| Resident tax estimate | Taxable income × 10% + per capita levy |

---

## Section 8 — Bank Statement Reading Guide

### Mizuho Bank (みずほ銀行)
- Format: `日付 | 摘要 | お引き出し | お預け入れ | 残高`
- Date: YYYY/MM/DD
- Income = お預け入れ column
- Key identifiers: 振込入金 (wire received), 外国送金 (foreign remittance)

### MUFG / 三菱UFJ銀行
- Format: `お取引日 | お取引内容 | お引出し金額 | お預入金額 | 残高`
- Date: YY.MM.DD (2-digit year)
- Income = お預入金額

### SMBC / 三井住友銀行
- Format: `取引日 | 内容 | 支払い | 預かり | 残高`
- Date: YYYY-MM-DD
- Income = 預かり column

### Japan Post Bank (ゆうちょ銀行)
- Format: `年月日 | 摘要 | お支払い金額 | お預かり金額 | 差引残高`
- Date: 令和X年Y月Z日 (Japanese imperial era) OR YYYY/MM/DD on e-bank
- Convert 令和7 = 2025 (令和 + 2018 = Western year)
- Income = お預かり金額

### Rakuten Bank (楽天銀行)
- Format: `取引日 | 取引説明 | 支払金額 | 受取金額 | 残高`
- Date: YYYY/MM/DD
- Income = 受取金額
- 楽天ペイメント売上入金 = e-commerce sales net of fees

### PayPay Bank / Shinsei Bank
- Format: `取引日 | 取引内容 | 出金額 | 入金額 | 残高`
- Income = 入金額 column

### Exclusion Patterns (across all banks)
| Pattern | Action |
|---|---|
| 振替 own account | EXCLUDE — internal transfer |
| 定期預金 | EXCLUDE — savings movement |
| ATM 引き出し | EXCLUDE — cash withdrawal |
| 消費税 in payer description | Flag — may need to strip CT |
| 所得税 / 住民税 納付 | EXCLUDE from income/expenses — tax payments |

---

## Section 9 — Onboarding Fallback

If the client cannot provide complete information, ask these questions in priority order:

**Priority 1 (blocking — cannot proceed without):**
1. "What was your total gross revenue (売上高) for the year? Please provide bank statements or a summary."
2. "Do you have 青色申告 (blue return) status registered with your tax office?"
3. "What were your total National Health Insurance and National Pension premiums paid this year?"

**Priority 2 (needed for accurate calculation):**
4. "Do you work from home? If yes, what is the total floor area of your home, and how much space is used exclusively for work?"
5. "Do you use a vehicle for business? If yes, approximately what % of km driven are for business purposes?"
6. "Do you have iDeCo or 小規模企業共済 contributions? If yes, what were the total annual amounts?"
7. "Do you have a spouse or dependants? If yes, provide their annual income."

**Priority 3 (deductions that may be missed):**
8. "Did you pay any medical expenses exceeding ¥100,000 this year (or 5% of income)?"
9. "Do you have earthquake insurance (地震保険) on your home?"
10. "Are you paying life insurance premiums (生命保険料)? These have a separate deduction up to ¥40,000–¥120,000."

**Conservative approach if data gaps remain:**
- Exclude any deduction that cannot be documented
- Use white return assumption if blue return status unconfirmed
- Do not estimate social insurance — these must be actual amounts

---

## Section 10 — Reference Material

### Key NTA Forms
| Form | Purpose |
|---|---|
| 確定申告書 B (Form B) | Main self-employment tax return form |
| 青色申告決算書 | Blue return profit/loss statement (attached to Form B) |
| 収支内訳書 | White return income/expense summary |
| 青色申告承認申請書 | Application to elect blue return status |
| 青色事業専従者給与に関する届出書 | Family salary election form |
| 減額申請書 | Application to reduce advance tax (予定納税) |

### Filing Methods
- **e-Tax:** Online via NTA MyNumber portal — required for ¥650,000 blue return deduction. Signature via マイナンバーカード or ID/password.
- **Paper:** Submit to district NTA office (税務署). Blue return deduction limited to ¥550,000.
- **Third-party software:** Freee, Money Forward Claim, やよいの青色申告 — all support e-Tax submission.

### Key Rates Summary
| Tax | Rate |
|---|---|
| National income tax | 5% – 45% progressive |
| Reconstruction surtax | 2.1% of national income tax |
| Resident tax | ~10% of taxable income + per-capita levy |
| Consumption tax | 10% standard / 8% reduced (separate obligation) |
| National pension (FY2025) | ¥16,980/month |

### Useful References
- NTA (国税庁): nta.go.jp
- e-Tax: e-tax.nta.go.jp
- MyNumber (マイナポータル): myna.go.jp
- Bank of Japan TTM rates: boj.or.jp
- 確定申告 period: February 16 – March 15 annually

---

## Prohibitions
- Do not advise on consumption tax (消費税) registration, calculation, or filing — separate skill required
- Do not advise on corporate tax (法人税) — this skill covers self-employed individuals only
- Do not advise on inheritance tax (相続税) or gift tax (贈与税)
- Do not advise on securities income (株式 / FX) beyond noting it exists as a separate schedule
- Do not advise on social insurance contribution amounts for employees — NTA / 年金事務所 jurisdiction
- Do not guarantee tax outcomes — tax positions depend on NTA audit and individual facts

## Disclaimer
This skill provides general guidance for informational and planning purposes. It does not constitute tax advice. Clients should verify their specific situation with a 税理士 (licensed tax accountant) registered with the Japan Federation of Certified Public Tax Accountants' Associations. Tax law changes regularly — confirm current rules with the NTA or a qualified advisor.
