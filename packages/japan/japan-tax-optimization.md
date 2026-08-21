---
name: japan-tax-optimization
description: Use this skill when advising on LEGAL tax minimization strategies for Japanese taxpayers — individuals, sole proprietors (kojin jigyō), and small corporations (KK/GK). Trigger on phrases like "reduce my tax Japan", "tax planning", "blue return", "ao-iro shinkoku", "furusato nozei", "iDeCo", "NISA", "sole proprietor vs corporation", "shakai hoken", "social insurance optimization", "consumption tax", or any question about legally minimizing Japanese income tax. Covers entity selection, blue return optimization, deductions, capital allowances, loss utilization, timing, consumption tax, social insurance, and red lines. ALWAYS read this skill before giving Japanese tax optimization advice.
version: 1.0
jurisdiction: JP
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on: - bookkeeping-workflow-base
category: tax-optimization
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Japan Tax Optimization

## Section 1 — Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Japan |
| Currency | JPY |
| Tax year | Calendar year (1 January – 31 December) |
| Primary legislation | Income Tax Act (所得税法, Shotokuzei-hō); Corporation Tax Act (法人税法, Hōjinzei-hō) |
| Anti-avoidance | General anti-avoidance doctrine (judicial); specific provisions per act; transfer pricing (Special Taxation Measures Act) |
| Tax authority | National Tax Agency (NTA, 国税庁) |
| Filing deadline | 15 March of the following year (kakutei shinkoku, 確定申告) |
| Individual top national rate | 45% (+ 2.1% reconstruction surtax on income tax amount) |
| Residence tax (jūmin-zei) | ~10% (prefectural + municipal) |
| Combined top marginal rate | ~55.945% |
| Corporate tax (KK, paid-in capital ≤¥100m) | Effective ~34–35% (combined national + local + enterprise) |
| Consumption tax | 10% standard; 8% reduced rate (food, beverages excl. alcohol/dining out) |

### Individual National Income Tax Brackets (2025)

**Individual National Income Tax Brackets (2025)**

| Taxable Income (JPY) | National Rate | Quick Deduction |
| --- | --- | --- |
| 1 – 1,950,000 | 5% | ¥0 |
| 1,950,001 – 3,300,000 | 10% | ¥97,500 |
| 3,300,001 – 6,950,000 | 20% | ¥427,500 |
| 6,950,001 – 9,000,000 | 23% | ¥636,000 |
| 9,000,001 – 18,000,000 | 33% | ¥1,536,000 |
| 18,000,001 – 40,000,000 | 40% | ¥2,796,000 |
| 40,000,001+ | 45% | ¥4,796,000 |

Add residence tax (~10%) and reconstruction surtax (2.1% of income tax, through 2037).

## Section 2 — Income Splitting & Structuring

### Sole Proprietor (Kojin Jigyō) vs Corporation (KK/GK)

- **Sole proprietor taxation** — All business income taxed at progressive individual rates (up to ~55%). Simpler setup. Blue return available with ¥650,000 special deduction. NHI (国民健康保険) for health; National Pension (国民年金) for pension.
- **Corporation taxation** — Corporate tax at effective ~22–35% depending on income and capital. Director salary (yakuin hōshū) is set annually and must remain fixed. Enrolled in Shakai Hoken (厚生年金 + 健康保険) — higher benefits but split employer/employee contributions. Consumption tax exemption in first 2 fiscal years if capital ≤¥10m and prior-period revenue ≤¥10m.
- **Incorporation threshold** — Generally beneficial when annual profit exceeds ¥8–10 million. Below ¥5 million, sole proprietorship with blue return is usually superior due to lower compliance costs.

### Family Salary (Blue Return)

- **Conditions for family salary (senjūsha kyūyo)** — Blue-return sole proprietors can pay salaries to family members (専従者給与, senjūsha kyūyo) if: Family member is aged 15+ and lives with the taxpayer; Family member works exclusively or principally in the business; Salary is registered with the tax office in advance (届出書); Amount is reasonable relative to work performed.
- **White-return fixed deduction** — This shifts income from the higher-bracket proprietor to lower-bracket family members. White-return filers get a fixed deduction of ¥860,000 (spouse) or ¥500,000 (other family) only.

### Director Compensation (Corporation)

- **Teiki dōgaku kyūyo requirement** — Director salary (定期同額給与, teiki dōgaku kyūyo) must be set at the start of the fiscal year and remain constant. Changes mid-year without valid reason are non-deductible to the corporation. Optimise by setting salary to minimise combined corporate + personal + social insurance tax.

## Section 3 — Deductions Most People Miss

**Deductions Most People Miss**

| Deduction | Legislation | Notes |
| --- | --- | --- |
| Blue return special deduction | Income Tax Act Art 65 | ¥650,000 if double-entry bookkeeping + e-filing or electronic ledger storage. ¥550,000 without e-filing. ¥100,000 for simplified bookkeeping |
| Medical expense deduction | Art 73 | Expenses exceeding ¥100,000 (or 5% of income if <¥2m). Family members included |
| Social insurance deduction | Art 74 | NHI premiums, National Pension, Shakai Hoken — full deduction with no cap |
| Small-scale mutual aid (Shōkibo Kyōsai) | Art 75 | Full deduction on contributions up to ¥84,000/month (¥1,008,000/year). Functions like a retirement fund for sole proprietors |
| iDeCo contributions | Art 75 | Full deduction. Self-employed: up to ¥75,000/month (combined with National Pension Fund). Employees: ¥23,000/month (or ¥62,000 combined with employer DC from Dec 2026) |
| Life insurance deduction | Art 76 | Up to ¥40,000 each for general life, medical/nursing, and individual pension = max ¥120,000 national + ¥70,000 residence tax |
| Earthquake insurance deduction | Art 77 | Up to ¥50,000 |
| Furusato Nozei (hometown tax) | Art 78, Local Tax Act | Donations to municipalities — tax credit on income + residence tax. Self-burden ¥2,000. Return gifts (up to 30% of donation value). One-Stop for ≤5 municipalities |
| Casualty loss deduction | Art 72 | Losses from disaster, theft, or embezzlement |
| Spouse deduction | Art 83 | ¥380,000 deduction if spouse income ≤¥480,000/year (taxpayer income ≤¥9m) |
| Dependent deduction | Art 84 | ¥380,000 per qualifying dependent; ¥630,000 for specific dependents (19–22) |
| Home loan deduction (credit) | Special Taxation Measures Act Art 41 | 0.7% of year-end loan balance for up to 13 years (new builds) or 10 years (existing). Max balance varies by building type |

## Section 4 — Capital Allowances Optimization

### Accelerated Depreciation for Small Assets

**Accelerated Depreciation for Small Assets**

| Asset Cost (JPY) | Treatment | Legislation |
| --- | --- | --- |
| <¥100,000 | Immediately expensed | Income Tax Act Art 67 |
| ¥100,000 – ¥199,999 | 3-year straight-line (lump-sum depreciation, 一括償却) | Art 67-5 |
| ¥100,000 – ¥300,000 (blue return, <300 employees) | Immediately expensed (措置法, Special Taxation Measures Act) — annual aggregate limit ¥3 million | Special Taxation Measures Act Art 28-2 |

### Standard Depreciation

- **Depreciation method default** — Declining-balance method (定率法) is default for most assets; straight-line (定額法) can be elected. Buildings and building improvements must use straight-line.

**Standard Depreciation useful life table**

| Asset Category | Useful Life (typical) |
| --- | --- |
| Computer hardware | 4 years |
| Office furniture | 8–15 years |
| Motor vehicles (passenger) | 6 years |
| Buildings (steel-frame) | 34–47 years |
| Software (purchased) | 5 years |

### Vehicle Optimization

- **No statutory vehicle depreciation cap** — No statutory cost cap on vehicle depreciation (unlike Australia or UK). A ¥6 million vehicle depreciates at declining balance over 6 years. High-value vehicles are scrutinised for business-use percentage.

## Section 5 — Loss Utilization

### Sole Proprietor (Blue Return)

- **Blue return loss carryforward/carryback** — Blue-return filers can carry forward net losses for 3 years (Art 70). Losses can also be carried back 1 year for a refund of prior-year tax (Art 140) — rarely used by individuals but valuable in loss years.  _(Art 70; Art 140)_
- **White-return loss limits** — White-return filers: losses only from casualty, theft, or disaster can be carried forward (3 years). Business losses are not carried forward. This alone justifies filing blue return.

### Corporation

- **Corporate NOL carryforward and carryback** — Net operating losses carry forward 10 years. SMEs (capital ≤¥100m) can offset 100% of income; large corporations limited to ~50–60% offset per year. Carry-back: 1 year (SMEs only; suspended for large corporations).

### Inter-Income Offsetting (損益通算)

- **Loss offsetting across income categories** — Sole proprietors can offset business losses against other income categories (employment, real estate, etc.) in the same year. Capital losses on listed securities cannot offset non-securities income except in specific cases.

## Section 6 — Timing Strategies

**Timing Strategies**

| Strategy | Detail |
| --- | --- |
| Furusato Nozei before year-end | Donations must be made by 31 December. One-Stop application due by 10 January. Simulator to check optimal amount |
| iDeCo / Shōkibo Kyōsai before December | Contributions in the calendar year create that year's deduction. New iDeCo enrolees: start early — processing takes 1–2 months |
| Accelerate asset purchases | Blue-return sole proprietors: buy assets ≤¥300,000 before year-end for immediate deduction (up to ¥3m aggregate) |
| Defer income | Cash-basis small businesses: delay billing to January. Invoice must be dated and delivered in January |
| Medical expenses — consolidate | Aggregate family medical expenses. If close to ¥100,000 threshold, schedule elective procedures in same calendar year |
| Withholding tax settlement | Year-end adjustment (年末調整, nenmatsu chōsei) for employees handles most credits. Self-employed: file by 15 March |
| Capital gains timing on listed shares | Separate taxation at 20.315% (income + residence). Losses carry forward 3 years within listed-securities income only |

## Section 7 — Consumption Tax (消費税) Optimization

**Consumption Tax Optimization**

| Topic | Detail |
| --- | --- |
| Exemption threshold | Taxable sales ≤¥10 million in base period (2 years prior) → exempt (免税事業者). But qualified invoice issuer registration waives exemption |
| Qualified Invoice System (インボイス制度) | From 1 Oct 2023. Registered businesses issue qualified invoices; buyers need these for input tax credits. Non-registered sellers lose B2B competitiveness |
| Special 20% accommodation | Small businesses newly registered as invoice issuers: may use actual sales tax × 20% as payable amount (effectively 80% relief). Valid through September 2026 |
| Simplified tax system (簡易課税) | Businesses with base-period sales ≤¥50m can elect simplified method: deemed purchase ratio by industry (40%–90%) applied to sales tax. Reduces compliance and often reduces tax for service businesses |
| Input tax credit | Standard method: claim consumption tax on business purchases. Requires qualified invoices from suppliers |
| Timing of registration | Voluntary registration creates consumption tax obligations. If primarily B2C (consumers), staying exempt avoids 10% burden on sales |

## Section 8 — Social Insurance Optimization

### NHI vs Shakai Hoken (社会保険)

**NHI vs Shakai Hoken**

| System | Coverage | Who | Cost |
| --- | --- | --- | --- |
| National Health Insurance (NHI, 国民健康保険) | Health only | Sole proprietors, freelancers | Income-based; varies by municipality. Capped ~¥1,060,000/year |
| National Pension (国民年金) | Basic pension | Self-employed | Flat ¥16,980/month (2025). Voluntary add-on: National Pension Fund |
| Shakai Hoken (厚生年金 + 健保) | Health + pension | Employees, company directors | ~30% of standard monthly salary (split employer/employee). No cap on health portion after ¥1,390,000 standard salary |

### Optimization Strategies

- **Sole proprietor with high income — NHI cap advantage** — NHI premiums cap out at ~¥1,060,000 regardless of income above the cap threshold. Above that level, additional income incurs no additional NHI cost — a marginal advantage over Shakai Hoken (which increases with salary).
- **Corporation — director salary setting** — Set director salary (hōshū) to optimise total of corporate tax + personal tax + social insurance. Very low salary triggers NTA scrutiny for unreasonable compensation; very high salary increases social insurance cost.
- **Shōkibo Kyōsai (小規模企業共済)** — Retirement fund for sole proprietors and small company directors. Contributions up to ¥84,000/month fully deductible. Lump-sum withdrawal taxed as retirement income (退職所得) with significant exemptions.
- **iDeCo stacking** — Contributions fully deductible from income. Upon withdrawal at retirement, lump-sum receives retirement income treatment; annuity receives pension income deduction. Layer with Shōkibo Kyōsai for maximum deductions.

## Section 9 — Investment & Retirement

**Investment & Retirement**

| Vehicle | Tax Treatment |
| --- | --- |
| NISA (新NISA, from 2024) | Growth investment: ¥2.4m/year; Tsumitate (accumulation): ¥1.2m/year. Lifetime cap ¥18m. Dividends, capital gains, and interest within NISA are permanently tax-free. No time limit |
| iDeCo | Contributions deductible. Growth tax-free. Withdrawal as lump sum → retirement income treatment (退職所得控除); as annuity → pension income deduction (公的年金等控除) |
| Shōkibo Kyōsai | Contributions deductible. Lump-sum → retirement income treatment. Annuity option available |
| National Pension Fund (国民年金基金) | Contributions deductible (combined with iDeCo max ¥75,000/month for Category 1). Annuity taxed as pension income |
| Listed securities | 20.315% separate taxation on capital gains and dividends. Losses carry forward 3 years within securities income |
| Real estate | Rental income taxed at progressive rates. Building depreciation deductible. Losses from real estate offset other income (except certain interest on high-leverage properties) |

### Layering Strategy

- **Sole proprietor maximizing deductions — steps** — For sole proprietors maximising deductions: 1. iDeCo — up to ¥75,000/month (Category 1) = ¥900,000/year deduction. 2. Shōkibo Kyōsai — up to ¥84,000/month = ¥1,008,000/year deduction. 3. National Pension Fund — remaining room within ¥75,000/month combined iDeCo limit. 4. NISA — invest after-tax income; all returns tax-free. 5. Furusato Nozei — redirect taxes to municipalities for return gifts.
- **Combined iDeCo + Shōkibo saving estimate** — Combined deduction from iDeCo + Shōkibo alone: ~¥1.9m/year. At 33% national + 10% residence = ~¥820,000 tax reduction.

## Section 10 — Red Lines (GAAR & Scrutiny Triggers)

### Anti-Avoidance Framework

- **Japan's anti-avoidance approach** — Japan does not have a statutory GAAR like Australia's Part IVA, but the NTA applies: Specific anti-avoidance rules per act (e.g., transfer pricing under Special Taxation Measures Act); Judicial substance-over-form doctrine; Blue return revocation for non-compliance with bookkeeping requirements; Penalty taxes for underreporting (10% additional tax; 15% for large amounts; 35%–40% if fraud).

### NTA Scrutiny Triggers

**NTA Scrutiny Triggers**

| Trigger | Risk |
| --- | --- |
| Unreasonable director salary (too high or too low) | Excess disallowed as corporate deduction (Corporation Tax Act Art 34) |
| Family salary without corresponding work | Disallowed deduction; potential blue return revocation |
| Personal expenses through business | Non-deductible; additional tax |
| Consumption tax evasion via exempt status | NTA reclassification if artificial structure |
| Transfer pricing on related-party transactions | Special Taxation Measures Act adjustment |
| Cryptocurrency gains not reported | NTA data matching with exchanges since 2020 |
| Non-resident income not reported | Global income obligation for residents |
| Excessive depreciation claims | Asset useful life adjusted by NTA |
| Mixing personal and business accounts | Blue return revocation risk |
| Furusato Nozei exceeding deductible limit | No penalty, but excess is non-refundable; pure donation |

### Absolute Prohibitions

- **Absolute prohibitions list** — NEVER advise underreporting income or hiding cash transactions; NEVER advise claiming personal expenses as business deductions; NEVER set director compensation at levels that cannot be justified; NEVER advise structuring solely to maintain consumption tax exemption if the arrangement lacks business substance; NEVER advise filing a white return to avoid bookkeeping obligations — the lost deductions almost always outweigh the effort.

## Section 11 — Annual Tax Planning Calendar

**Annual Tax Planning Calendar**

| When | Action |
| --- | --- |
| January | One-Stop Furusato Nozei deadline (10 Jan for prior-year donations). Begin preparing kakutei shinkoku documents |
| February 16 – March 15 | Filing period for income tax return (確定申告). Claim all deductions. Elect blue return for next year if not yet registered |
| March 15 | Filing deadline. Final tax payment due |
| April | Review prior-year assessment. Corporations: set director compensation for new fiscal year |
| June | Residence tax assessment notice arrives. Verify Furusato Nozei credits reflected |
| July – September | Mid-year tax review. Estimate annual income for optimal Furusato Nozei and iDeCo planning |
| October | Confirm iDeCo/Shōkibo contributions on track. Life/earthquake insurance certificate arrives |
| November | Execute year-end tax strategies. Purchase sub-¥300,000 assets. Confirm medical expenses |
| December | **Critical month.** Make Furusato Nozei donations. Final iDeCo/Shōkibo contributions. Year-end adjustment (nenmatsu chōsei) for employees. National Pension catch-up payments |

## Section 12 — Cash Impact Examples

### Example 1 — Blue Return vs White Return (Sole Proprietor)

Income: ¥8,000,000 business income. No other income.

White return: Taxable income = ¥8,000,000 – basic deduction ¥480,000 = ¥7,520,000. National tax: ~¥1,097,100. Residence tax: ~¥752,000. Total: ~¥1,849,100.

Blue return: Taxable income = ¥8,000,000 – ¥650,000 (blue deduction) – ¥480,000 (basic) = ¥6,870,000. National tax: ~¥946,500. Residence tax: ~¥687,000. Total: ~¥1,633,500. Saving: ~¥215,600 per year.

### Example 2 — Layered Deduction Strategy

Sole proprietor, ¥12,000,000 income.
- iDeCo: ¥816,000/year (¥68,000/month)
- Shōkibo Kyōsai: ¥840,000/year
- Blue return deduction: ¥650,000
- Social insurance (NHI + pension): ~¥1,200,000
- Furusato Nozei: ~¥250,000 (net cost ¥2,000)
- Total deductions: ~¥3,756,000
- Taxable income: ~¥7,764,000 (after basic deduction)
- Tax saving vs no planning: ~¥1,300,000 annually (at ~33%+10% marginal)

### Example 3 — Incorporation at ¥10m Profit

Before (sole proprietor): ¥10m profit. After blue deduction and social insurance: ~¥8.2m taxable. Total tax + NHI: ~¥2,870,000.

After (KK corporation): Pay ¥6m director salary. Corporate profit ¥4m taxed at ~22% = ¥880,000. Personal tax on ¥6m salary (after employment income deduction ¥1.64m): ~¥970,000. Shakai hoken (employer + employee): ~¥1,700,000. Total: ~¥3,550,000. Higher in this case due to Shakai Hoken costs. Incorporation advantage appears at ~¥12–15m+ profit.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a certified tax accountant (税理士, zeirishi) or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your jurisdiction — no liability on either side until you and the accountant sign a formal engagement letter — book a free 30-minute call:

→ [Book a call](https://calendly.com/openaccountants-info/30min)

We'll route you to the named verifier covering your country or state. You can also see the full list of verified accountants at [openaccountants.com/network](https://openaccountants.com/network).

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
