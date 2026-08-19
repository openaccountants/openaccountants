---
name: china-pit
description: Use this skill whenever asked to prepare, review, or classify transactions for China Personal Income Tax (个人所得税 / IIT), annual comprehensive income settlement (汇算清缴), or advise on Chinese tax brackets and special deductions. Trigger on phrases like "个人所得税", "IIT China", "综合所得", "汇算清缴", "专项附加扣除", "China income tax", or any PRC personal tax request. ALWAYS read this skill before touching any China PIT work.
version: 1.0
jurisdiction: CN
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - foundation
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# China Pit

## China Personal Income Tax (个人所得税) Skill v1.0

## Section 1 — Quick reference

**Quick reference table**

| Field | Value |
| --- | --- |
| Country | 中华人民共和国 (People's Republic of China) |
| Tax | 个人所得税 (Individual Income Tax / IIT) |
| Currency | CNY (人民币 / RMB / ¥) |
| Tax year | Calendar year (1 Jan – 31 Dec) |
| Current tax year | 2025 |
| Tax authority | 国家税务总局 (State Taxation Administration / STA) |
| Filing app | 个人所得税 APP (IIT APP) |
| Filing portal | https://etax.chinatax.gov.cn |
| Annual settlement (汇算清缴) | 1 March – 30 June of following year |
| Standard deduction | ¥60,000/year (¥5,000/month) |
| Source credit | `cn/individual-income-tax-law` (PRC IIT Law full text) |
| Contributor | Open Accountants Community |
| Validated by | Pending — requires sign-off by a Chinese CPA (注册会计师) or tax advisor |
| Skill version | 1.0 |

## Section 2 — Comprehensive income brackets (综合所得税率表)

Applies to: wages/salary (工资薪金), labor remuneration (劳务报酬), author's remuneration (稿酬), and royalties (特许权使用费).

**Comprehensive income brackets table**

| Annual taxable income (¥) | Rate | Quick deduction (速算扣除数) |
| --- | --- | --- |
| 0 – 36,000 | 3% | 0 |
| 36,001 – 144,000 | 10% | 2,520 |
| 144,001 – 300,000 | 20% | 16,920 |
| 300,001 – 420,000 | 25% | 31,920 |
| 420,001 – 660,000 | 30% | 52,920 |
| 660,001 – 960,000 | 35% | 85,920 |
| Over 960,000 | 45% | 181,920 |

- **Comprehensive income tax formula** — Tax = Taxable income × Rate − Quick deduction

## Section 3 — Business income brackets (经营所得税率表)

Applies to: self-employed (个体工商户), sole proprietorships, partnerships.

**Business income brackets table**

| Annual taxable income (¥) | Rate | Quick deduction |
| --- | --- | --- |
| 0 – 30,000 | 5% | 0 |
| 30,001 – 90,000 | 10% | 1,500 |
| 90,001 – 300,000 | 20% | 10,500 |
| 300,001 – 500,000 | 30% | 40,500 |
| Over 500,000 | 35% | 65,500 |

## Section 4 — Other income (flat rate 20%)

**Other income flat rate table**

| Income type | Rate | Notes |
| --- | --- | --- |
| Interest, dividends (利息、股息、红利) | 20% | Withheld at source |
| Property rental (财产租赁) | 20% | After ¥800 or 20% expense deduction |
| Property transfer (财产转让) | 20% | On gain (proceeds − cost − expenses) |
| Incidental income (偶然所得) | 20% | Lottery winnings, etc. |

## Section 5 — Deductions (扣除项目)

### Standard deduction (基本减除费用)

- **Standard deduction** — ¥60,000/year (¥5,000/month) — everyone gets this CNY

### Mandatory social insurance (专项扣除)

**Mandatory social insurance table**

| Item | Employee rate | Notes |
| --- | --- | --- |
| Pension (养老保险) | 8% | Of salary base |
| Medical (医疗保险) | 2% | Of salary base |
| Unemployment (失业保险) | 0.5% | Of salary base |
| Housing fund (住房公积金) | 5–12% | Of salary base (employer matches) |

- **Pre-tax deduction rule** — All deducted pre-tax from salary.

### Special additional deductions (专项附加扣除) — 2025

**Special additional deductions table**

| Deduction | Monthly amount (¥) | Conditions |
| --- | --- | --- |
| Children's education (子女教育) | 2,000/child | Ages 3–PhD; split 50/50 or one parent claims all |
| Continuing education (继续教育) | 400 | Degree programs; or ¥3,600/year for professional certificates |
| Serious illness medical (大病医疗) | — | Annual out-of-pocket over ¥15,000; max ¥80,000 deduction |
| Housing loan interest (住房贷款利息) | 1,000 | First home; max 240 months |
| Housing rent (住房租金) | 800–1,500 | Depends on city tier (no owned property) |
| Elderly care (赡养老人) | 3,000 | Parent 60+; only child gets full amount |
| Infant care (3岁以下婴幼儿照护) | 2,000/child | Under age 3 |

## Section 6 — Computation method

- **Computation method steps** — Step 1: Total annual income (全年收入额) - Salary: actual amount - Labor remuneration: income × 80% - Author's remuneration: income × 80% × 70% - Royalties: income × 80% Step 2: − Standard deduction (¥60,000) Step 3: − Social insurance (专项扣除) Step 4: − Special additional deductions (专项附加扣除) Step 5: − Other deductions (commercial health insurance max ¥2,400, pension max ¥12,000) Step 6: − Charitable donations (max 30% of taxable income) Step 7: = Annual taxable income (全年应纳税所得额) Step 8: Apply bracket rate − quick deduction (Section 2) Step 9: = Annual tax liability Step 10: − Tax already withheld during year (已预缴税额) Step 11: = Tax payable or refund (补税/退税)

## Section 7 — Worked example

**Scenario:** Employee in Beijing, annual salary ¥360,000, one child in school, housing loan (first home), caring for elderly parent (only child). Social insurance + housing fund deducted at source ≈ ¥4,500/month.

**Worked example table**

| Step | Description | Amount (¥) |
| --- | --- | --- |
| Annual salary |  | 360,000 |
| − Standard deduction | ¥5,000 × 12 | (60,000) |
| − Social insurance | ¥4,500 × 12 | (54,000) |
| − Children's education | ¥2,000 × 12 | (24,000) |
| − Housing loan interest | ¥1,000 × 12 | (12,000) |
| − Elderly care | ¥3,000 × 12 | (36,000) |
| **Taxable income** |  | **174,000** |

Tax on ¥174,000:
- ¥174,000 × 20% − ¥16,920 = **¥17,880**

If monthly withholding totaled ¥18,500 during the year → refund of **¥620**.

## Section 8 — Filing guidance

### Cumulative withholding (累计预扣预缴)

- **Cumulative withholding method** — Employers withhold monthly using cumulative method: - Each month: cumulative income to date, minus cumulative deductions, apply bracket, minus prior months' tax already withheld

### Annual settlement (汇算清缴)

**Annual settlement deadlines table**

| Who must settle | Deadline |
| --- | --- |
| Annual tax > withholding (补税 > ¥400) | By 30 June |
| Annual tax < withholding (退税) | By 30 June (to claim refund) |
| Single employer, withholding correct | No settlement needed |

### Who must file?

- **Who must file criteria** — - Annual income > ¥120,000 (even if fully withheld) - Income from 2+ sources - Foreign income - No withholding agent

### Key filing methods

- **个人所得税 APP** (official mobile app) — most common
- **Web portal** — etax.chinatax.gov.cn
- **In person** — local tax bureau (税务大厅)

## Section 9 — Nine categories of taxable income

**Nine categories of taxable income table**

| # | Chinese | English | Tax treatment |
| --- | --- | --- | --- |
| 1 | 工资、薪金所得 | Wages, salary | Comprehensive (cumulative withholding) |
| 2 | 劳务报酬所得 | Labor remuneration | Comprehensive (20%/30%/40% withholding, settled annually) |
| 3 | 稿酬所得 | Author's remuneration | Comprehensive (×70% preferential) |
| 4 | 特许权使用费所得 | Royalties | Comprehensive |
| 5 | 经营所得 | Business income | Separate (5%–35% brackets) |
| 6 | 利息、股息、红利所得 | Interest, dividends | 20% flat (final) |
| 7 | 财产租赁所得 | Property rental | 20% flat |
| 8 | 财产转让所得 | Property transfer | 20% flat on gain |
| 9 | 偶然所得 | Incidental income | 20% flat |

## Section 10 — Conservative defaults

**Conservative defaults table**

| Situation | Conservative position |
| --- | --- |
| Income category ambiguous | Classify as highest-rate category; flag |
| Special deduction eligibility unclear | Do NOT claim; flag for reviewer |
| Foreign income | Include if tax resident (183+ days); flag treaty |
| Stock options / RSU | Classify as wages on exercise; flag |
| Crypto gains | No explicit guidance; classify as property transfer 20%; flag |

## Section 11 — Sources

**Sources table**

| Source | URL |
| --- | --- |
| State Taxation Administration (国家税务总局) | https://www.chinatax.gov.cn |
| IIT APP | 个人所得税 (iOS/Android) |
| `cn/individual-income-tax-law` | https://github.com/cn/individual-income-tax-law |
| PRC Individual Income Tax Law (2018 amendment) | 中华人民共和国个人所得税法 (第七次修正) |

## Footer

*OpenAccountants — open-source accounting skills for AI*
*This is not tax advice. All outputs must be reviewed by a qualified professional before filing.*

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
