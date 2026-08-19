---
name: jp-incorporation
description: Use this skill whenever asked about incorporating in Japan -- transitioning from sole proprietorship (個人事業主) to a corporation (法人). Trigger on phrases like "incorporation Japan", "法人成り", "会社設立", "should I incorporate", "法人化", "株式会社", "合同会社", "KK vs GK", "corporate tax vs income tax", "法人税", "when to incorporate", "法人成りのタイミング", "micro corporation", "マイクロ法人", "officer compensation", "役員報酬", "social insurance comparison", "社会保険", "個人事業 vs 法人", "定期同額給与", "consumption tax exemption reset", "消費税の免税リセット", or any question about whether, when, and how a Japanese sole proprietor should form a company. This skill covers tax burden comparison, breakeven analysis, corporate form selection, establishment procedures, filing deadlines, officer compensation strategy, and social insurance optimization. ALWAYS read this skill before advising on Japanese incorporation.
version: 1.0
jurisdiction: JP
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - jp-income-tax
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# JP Incorporation

## Japan Incorporation (法人成り) -- Self-Employed Skill v1.0

> **Based on work by [Kazuki Nagata (@kazukinagata)](https://github.com/kazukinagata/shinkoku)**, licensed under MIT. Adapted for the OpenAccountants format.

## Section 1 -- Quick Reference

**Quick Reference Table**

| Field | Value |
| --- | --- |
| Country | Japan (日本) |
| Topic | Sole proprietor → Corporation transition (法人成り) |
| Legislation | Companies Act (会社法), Corporate Tax Act (法人税法), Income Tax Act (所得税法), Consumption Tax Act (消費税法) |
| Tax Authority | National Tax Agency (国税庁 NTA), Legal Affairs Bureau (法務局) |
| Contributor | Open Accountants Community |
| Validated by | Pending -- requires sign-off by a Japanese 税理士 (Zeirishi) |
| Skill version | 1.0 |
| Tax year basis | 2025 (令和7年) |

### Key Decision Thresholds

**Key Decision Thresholds Table**

| Business Income | Recommendation |
| --- | --- |
| Under JPY 5,000,000 | Stay as sole proprietor |
| JPY 6,000,000 -- 7,000,000 | Sole proprietor slightly favorable; prepare for future incorporation |
| ~JPY 8,000,000 | **Breakeven point** -- evaluate with social insurance benefits |
| JPY 9,000,000 -- 10,000,000 | Corporation slightly favorable |
| Over JPY 10,000,000 | Corporation clearly favorable |
| Over JPY 15,000,000 | Strong case for incorporation |

## Section 2 -- Tax Burden Comparison: Sole Proprietor vs Corporation

### 2.1 Sole Proprietor Tax Structure

**Sole Proprietor Tax Structure Table**

| Tax | Rate/Rule | Legislation |
| --- | --- | --- |
| Income tax (所得税) | Progressive 5%--45% on taxable income | Income Tax Act Art. 89 |
| Reconstruction surtax (復興特別所得税) | Income tax × 2.1% (through 2037) | Reconstruction Finance Act Art. 13 |
| Resident tax (住民税) | 10% of taxable income + per-capita levy ~JPY 5,000 | Local Tax Act |
| Enterprise tax (個人事業税) | 3%--5% on income over JPY 2,900,000 (deduction) | Local Tax Act Art. 72-49-17 |
| National health insurance (国民健康保険) | Income-based + per-capita; cap ~JPY 1,090,000/year (2025) | Per municipality |
| National pension (国民年金) | Flat JPY 17,510/month (JPY 210,120/year, 2025) | National Pension Act |

- **Total formula (sole proprietor)** — Income tax + reconstruction surtax + resident tax + enterprise tax + NHI + national pension

### 2.2 Corporate Tax Structure

**Corporate Tax Structure Table**

| Tax | Rate | Legislation |
| --- | --- | --- |
| Corporate tax (法人税) -- income ≤ JPY 8M | 15% (reduced rate for SMEs) | Corporate Tax Act Art. 66; Special Measures Art. 42-3-2 |
| Corporate tax -- income > JPY 8M | 23.2% | Corporate Tax Act Art. 66 |
| Local corporate tax (地方法人税) | Corporate tax × 10.3% | Local Corporate Tax Act Art. 6 |
| Corporate inhabitant tax (法人住民税) -- tax portion | Corporate tax × ~7% | Local Tax Act |
| Corporate inhabitant tax -- per-capita (均等割) | JPY 70,000/year minimum (capital ≤ JPY 10M, ≤ 50 employees) | Local Tax Act |
| Enterprise tax (法人事業税) | 3.5%--7.0% (progressive by income bracket) | Local Tax Act Art. 72-24-7 |
| Special enterprise tax (特別法人事業税) | Enterprise tax × 37% |  |
| Social insurance (健康保険 + 厚生年金) | ~28--30% of officer compensation (split employer/employee) | Health Insurance Act; Employees' Pension Insurance Act |

- **Total formula (corporate)** — Corporate taxes + officer's personal income tax/resident tax + social insurance (both halves)

### 2.3 Enterprise Tax Brackets (Corporate)

**Enterprise Tax Brackets Table**

| Taxable Income | Rate | With surcharge |
| --- | --- | --- |
| Up to JPY 4,000,000 | 3.5% | 3.75% |
| JPY 4,000,001 -- 8,000,000 | 5.3% | 5.665% |
| Over JPY 8,000,000 | 7.0% | 7.48% |

## Section 3 -- Breakeven Simulations

### Assumptions

- Sole proprietor: blue return (JPY 650,000 deduction), single, no dependents
- Corporation: capital JPY 1,000,000, single-person company, one officer
- Social insurance: Kyokai Kenpo (Tokyo), under 40 (no nursing care insurance)
- Officer compensation optimized to keep corporate profit under JPY 8,000,000
- Consumption tax excluded (same for both)

### 3.1 Business Income JPY 5,000,000 -- Sole Proprietor Wins

**JPY 5,000,000 comparison table**

|  | Sole Proprietor | Corporation (officer comp. JPY 4M) |
| --- | --- | --- |
| Income/corporate tax + surtaxes | ~JPY 620,000 | ~JPY 516,000 |
| Social insurance | ~JPY 610,000 (NHI + pension) | ~JPY 1,200,000 (both halves) |
| **Total burden** | **~JPY 1,230,000** | **~JPY 1,764,000** |

**Verdict:** Sole proprietor saves ~JPY 530,000. Social insurance costs overwhelm the corporate tax advantage.

### 3.2 Business Income JPY 8,000,000 -- Breakeven

**JPY 8,000,000 comparison table**

|  | Sole Proprietor | Corporation (officer comp. JPY 6M) |
| --- | --- | --- |
| Income/corporate tax + surtaxes | ~JPY 1,398,000 | ~JPY 870,000 |
| Social insurance | ~JPY 910,000 | ~JPY 1,500,000 |
| **Total burden** | **~JPY 2,308,000** | **~JPY 2,370,000** |

**Verdict:** Nearly equal. Factor in social insurance benefits (disability coverage, employer pension, sick pay) to tip the decision.

### 3.3 Business Income JPY 10,000,000 -- Corporation Wins

**JPY 10,000,000 comparison table**

|  | Sole Proprietor | Corporation (officer comp. JPY 7M) |
| --- | --- | --- |
| Income/corporate tax + surtaxes | ~JPY 2,188,000 | ~JPY 1,240,000 |
| Social insurance | ~JPY 1,110,000 | ~JPY 1,700,000 |
| **Total burden** | **~JPY 3,298,000** | **~JPY 2,940,000** |

**Verdict:** Corporation saves ~JPY 360,000.

### 3.4 Business Income JPY 15,000,000 -- Corporation Clearly Wins

**JPY 15,000,000 comparison table**

|  | Sole Proprietor | Corporation (officer comp. JPY 9M) |
| --- | --- | --- |
| Income/corporate tax + surtaxes | ~JPY 3,938,000 | ~JPY 2,250,000 |
| Social insurance | ~JPY 1,270,000 | ~JPY 2,200,000 |
| **Total burden** | **~JPY 5,208,000** | **~JPY 4,450,000** |

**Verdict:** Corporation saves ~JPY 760,000.

### 3.5 Business Income JPY 20,000,000+ -- Corporation Strongly Wins

**JPY 20,000,000+ comparison table**

|  | Sole Proprietor | Corporation (officer comp. JPY 10M) |
| --- | --- | --- |
| Income/corporate tax + surtaxes | ~JPY 5,518,000 | ~JPY 3,620,000 |
| Social insurance | ~JPY 1,270,000 | ~JPY 2,400,000 |
| **Total burden** | **~JPY 7,638,000** | **~JPY 6,020,000** |

**Verdict:** Corporation saves ~JPY 1,620,000.

## Section 4 -- Corporate Forms: KK vs GK

### 4.1 Comparison Table

**KK vs GK Comparison Table**

| Feature | Kabushiki Kaisha (株式会社/KK) | Godo Kaisha (合同会社/GK) |
| --- | --- | --- |
| Legal basis | Companies Act Art. 25+ | Companies Act Art. 575+ |
| Establishment cost (electronic articles) | ~JPY 200,000 | ~JPY 60,000 |
| Establishment cost (paper articles) | ~JPY 240,000 | ~JPY 100,000 |
| Articles of incorporation notarization | Required (notary public) | Not required |
| Registration tax (minimum) | JPY 150,000 | JPY 60,000 |
| Social credibility | High | Moderate (less recognized in B2B) |
| Decision-making | Shareholders meeting + directors | Majority of members (flexible) |
| Financial statement disclosure | Required (official gazette, etc.) | Not required |
| Officer term | Up to 10 years (private company), re-registration required | No term limit |
| Profit distribution | Based on shareholding ratio | Freely determined by articles |
| IPO possibility | Yes | No |
| Transfer of interest | Share transfer (relatively easy) | Requires all members' consent |

### 4.2 Establishment Cost Breakdown

**Kabushiki Kaisha (electronic articles) Cost Table**

| Item | Amount |
| --- | --- |
| Notarization fee | JPY 30,000--50,000 (depends on capital amount) |
| Certified copy fee | ~JPY 2,000 |
| Registration tax | JPY 150,000 (or capital × 0.7%, whichever is higher) |
| **Total** | **~JPY 182,000--202,000** |

**Godo Kaisha (electronic articles) Cost Table**

| Item | Amount |
| --- | --- |
| Notarization fee | Not required |
| Registration tax | JPY 60,000 (or capital × 0.7%, whichever is higher) |
| **Total** | **~JPY 60,000** |

Paper articles add JPY 40,000 in revenue stamps for both forms.

### 4.3 When to Choose Which

**Choose KK when:**
- B2B sales where counterparties conduct credit checks
- Future financing, capital raising, or IPO is planned
- Hiring multiple employees
- "Kabushiki Kaisha" brand recognition matters to customers

**Choose GK when:**
- Minimizing startup costs
- Solo or very small team (1--3 people)
- B2C business where corporate form is invisible to customers (IT, consulting)
- Faster decision-making and lower administrative overhead

## Section 5 -- Officer Compensation Strategy (役員報酬)

### 5.1 Fixed Monthly Compensation Rule (定期同額給与)

- **Fixed monthly compensation requirement** — To deduct officer compensation as a corporate expense, it must be paid monthly in equal amounts.  _(Corporate Tax Act Art. 34, para. 1, item 1)_

**Fixed Monthly Compensation Rules Table**

| Rule | Detail |
| --- | --- |
| Amount must be equal each month | Set once at the start of the fiscal year |
| Change window | Within 3 months of fiscal year start (at shareholders' meeting) |
| Mid-year changes | Prohibited except for extraordinary reasons |
| Bonuses to officers | Not deductible unless pre-registered (事前確定届出給与) |

### 5.2 Employment Income Deduction Advantage (給与所得控除)

This is the key advantage of incorporation. Sole proprietors only get the blue return deduction (max JPY 650,000), but officers get the employment income deduction:

**Employment Income Deduction Table (2025)**

| Annual Compensation | Employment Income Deduction (2025) |
| --- | --- |
| Up to JPY 1,625,000 | JPY 650,000 (minimum) |
| JPY 1,625,001 -- 1,800,000 | Compensation × 40% − JPY 100,000 |
| JPY 1,800,001 -- 3,600,000 | Compensation × 30% + JPY 80,000 |
| JPY 3,600,001 -- 6,600,000 | Compensation × 20% + JPY 440,000 |
| JPY 6,600,001 -- 8,500,000 | Compensation × 10% + JPY 1,100,000 |
| Over JPY 8,500,000 | JPY 1,950,000 (cap) |

### 5.3 Optimal Compensation Targets

**Optimal Compensation Targets Table**

| Business Profit | Officer Compensation Target | Corporate Profit Target | Rationale |
| --- | --- | --- | --- |
| JPY 8,000,000 | JPY 6,000,000 | JPY 2,000,000 | Keep personal tax at 20% bracket |
| JPY 10,000,000 | JPY 7,000,000 | JPY 3,000,000 | Good balance of deduction and rate |
| JPY 12,000,000 | JPY 8,000,000 | JPY 4,000,000 | Maximize deduction; corporate profit at 15% rate |
| JPY 15,000,000 | JPY 9,000,000 | JPY 6,000,000 | Watch social insurance upper bounds |
| JPY 20,000,000 | JPY 10,000,000 | JPY 10,000,000 | Retain profits in corporation |
| JPY 30,000,000 | JPY 12,000,000 | JPY 18,000,000 | Significant corporate retention |

**Optimization principles:**
1. Keep corporate profit ≤ JPY 8,000,000 for the 15% reduced rate
2. Maximize employment income deduction (peaks at JPY 1,950,000 for comp. over JPY 8,500,000)
3. Consider social insurance cap: pension tops out at standard monthly compensation JPY 650,000 (~JPY 7,800,000 annual)
4. Balance personal progressive tax rates against flat corporate rate

### 5.4 Family Income Splitting

A corporation can pay salaries to family members as employees or directors, achieving income splitting:

**Family Income Splitting Scenario Table**

| Scenario | Effect |
| --- | --- |
| Sole proprietor: all JPY 12M to owner | Owner at ~23% marginal rate |
| Corporation: JPY 9M to owner + JPY 3M to spouse | Owner at ~20%, spouse at ~5% |
| **Tax savings** | **~JPY 570,000/year** |

- **Requirements for family income splitting** — Family employees must have genuine work duties. Compensation must be reasonable for the role. No-work salary payments will be denied as a deductible expense.

## Section 6 -- Social Insurance Comparison

### 6.1 Sole Proprietor vs Corporation

**Sole Proprietor vs Corporation Social Insurance Table**

| Feature | Sole Proprietor (NHI + National Pension) | Corporation (Kyokai Kenpo + Employees' Pension) |
| --- | --- | --- |
| Basis | Prior year income | Standard monthly compensation |
| Dependent coverage | None (each family member pays) | Yes (dependents covered at no extra cost) |
| Sick pay (傷病手当金) | None | 2/3 of daily comp. for up to 18 months |
| Maternity pay (出産手当金) | None | 2/3 of daily comp. |
| Pension benefit | Basic pension only (~JPY 810,000/year at full) | Basic + employees' pension (income-proportional) |
| Premium cap | NHI: ~JPY 1,090,000; pension: flat | Standard compensation table cap |

### 6.2 Social Insurance Rates (2025)

**Social Insurance Rates Table (2025)**

| Insurance | Rate | Burden |
| --- | --- | --- |
| Health insurance (Kyokai Kenpo, national avg.) | ~10.00% | Split 50/50 employer/employee |
| Nursing care (age 40--64) | 1.59% | Split 50/50 |
| Employees' pension (厚生年金) | 18.3% | Split 50/50 |
| Child-rearing contribution | 0.36% | 100% employer |
| **Total (under 40)** | **~28.66%** | **~14.33% each** |
| **Total (40 and over)** | **~30.25%** | **~15.125% each** |

### 6.3 Social Insurance Cap

**Social Insurance Cap Table**

| Insurance | Standard Monthly Comp. Cap | Annual Comp. Equivalent |
| --- | --- | --- |
| Health insurance | JPY 1,390,000 (Grade 50) | ~JPY 16,680,000 |
| Employees' pension | JPY 650,000 (Grade 32) | ~JPY 7,800,000 |

- **Cap plateau note** — Above the pension cap (~JPY 7,800,000 annual compensation), pension premiums stop increasing. Health insurance premiums stop at ~JPY 16,680,000.

## Section 7 -- Consumption Tax Exemption Reset

### 7.1 The Two-Year Exemption

- **Two-year exemption** — A newly established corporation with capital under JPY 10,000,000 is generally exempt from consumption tax for the first two fiscal years.  _(Consumption Tax Act Art. 12-2)_

**Conditions:**
1. Capital under JPY 10,000,000
2. First fiscal period: no base period exists → exempt
3. Second fiscal period: exempt IF specified-period taxable sales (or wages) ≤ JPY 10,000,000
4. Not a "specified newly established corporation" (特定新規設立法人)

### 7.2 Maximizing the Exemption Period

**Maximizing Exemption Period Strategies Table**

| Strategy | Effect |
| --- | --- |
| Set capital below JPY 10,000,000 (e.g., JPY 9,990,000) | Qualifies for exemption |
| Make first fiscal period ≤ 7 months | Eliminates specified-period test for 2nd year |
| Delay qualified invoice registration | Preserves exemption (but may lose clients who need invoices) |

**Example:** Establish on October 1 with March fiscal year-end → first period = 6 months → no specified period → second period also exempt → up to ~19 months exempt.

### 7.3 Invoice Registration Caution

- **Invoice registration caution** — If the sole proprietor was already a qualified invoice issuer: - The corporation needs its own new invoice registration - Registering makes the corporation taxable from the registration date, losing the exemption - The individual's registration does NOT automatically cancel -- submit a cancellation notice (適格請求書発行事業者の登録の取消しを求める届出書) - The 20% special measure (2割特例) may apply to the new corporation through periods ending September 2026

## Section 8 -- Establishment Procedure

### Step 1: Pre-establishment Decisions

**Pre-establishment Decisions Table**

| Decision | Considerations |
| --- | --- |
| Corporate form | KK vs GK (see Section 4) |
| Trade name (商号) | Check for conflicts at Legal Affairs Bureau |
| Business purpose | List broadly in articles (include future activities) |
| Registered office | Home address or office |
| Capital amount | Under JPY 10,000,000 for CT exemption |
| Fiscal year-end | Avoid March (tax adviser busy season); optimize for CT exemption |
| Incorporators | Confirm contributing members |
| Seals (印鑑) | Representative seal, bank seal, square seal |

### Step 2: Draft and Authenticate Articles of Incorporation

**KK:** Create articles → notarize at public notary office (公証役場)
**GK:** Create articles → no notarization required

### Step 3: Capital Contribution

1. Transfer capital to the incorporator's personal bank account
2. Prepare a copy of the bankbook page showing the transfer
3. Create a certificate of capital contribution (払込証明書)

### Step 4: Registration at Legal Affairs Bureau

Submit: registration application, articles, capital contribution proof, officer acceptance letters, seal registration form. Pay registration tax.

Processing time: typically 1--2 weeks. Obtain certificate of registered matters (登記事項証明書) and seal certificate (印鑑証明書) after completion.

### Step 5: Post-Establishment Filings

#### Tax Office (税務署)

**Tax Office Filings Table**

| Filing | Deadline | Notes |
| --- | --- | --- |
| Corporate establishment notice (法人設立届出書) | Within 2 months of establishment | Attach articles + registration certificate |
| Blue return approval application (青色申告の承認申請書) | Within 3 months of establishment OR fiscal year end (whichever is earlier) | **Highest priority -- missing this means white return** |
| Payroll office opening notice (給与支払事務所等の開設届出書) | Within 1 month | Required if paying officer compensation |
| Special withholding payment approval (源泉所得税の納期の特例) | As soon as possible | Allows semi-annual withholding deposits (≤10 employees) |
| CT taxable business election (消費税課税事業者選択届出書) | By end of fiscal year | If registering for invoices |
| Qualified invoice registration (適格請求書発行事業者の登録申請書) | Any time | If clients require invoices |

#### Prefectural/Municipal Tax Office

**Prefectural/Municipal Tax Office Filings Table**

| Filing | Deadline |
| --- | --- |
| Corporate establishment notice (prefectural) | 15 days to 2 months (varies by municipality) |
| Corporate establishment notice (municipal) | 15 days to 2 months (Tokyo 23 wards: file with Tokyo Metropolitan) |

#### Pension Office (年金事務所)

**Pension Office Filings Table**

| Filing | Deadline | Notes |
| --- | --- | --- |
| New workplace application (健康保険・厚生年金保険 新規適用届) | Within 5 days | Mandatory for all corporations |
| Insured person qualification (被保険者資格取得届) | Within 5 days | Officers are also covered |
| Dependent notification (被扶養者異動届) | Within 5 days | If there are dependents |

#### Labor Insurance (only if hiring employees)

**Labor Insurance Filings Table**

| Filing | Submit To | Deadline |
| --- | --- | --- |
| Insurance relationship establishment (保険関係成立届) | Labor Standards Office | Within 10 days of hiring |
| Employment insurance workplace (雇用保険 適用事業所設置届) | Hello Work | Within 10 days of hiring |
| Employment insurance qualification (雇用保険 被保険者資格取得届) | Hello Work | By 10th of following month |

*Not required for single-person corporations with no employees.*

## Section 9 -- Closing the Sole Proprietorship

If not maintaining a dual structure, file these to close the sole proprietorship:

**Closing Sole Proprietorship Filings Table**

| Filing | Submit To | Deadline |
| --- | --- | --- |
| Business opening/closing notice (開業・廃業等届出書) | Tax office | Within 1 month of closure |
| Blue return cessation (青色申告の取りやめ届出書) | Tax office | By March 15 of following year |
| Business cessation notice (CT) (事業廃止届出書) | Tax office | Promptly |
| Invoice registration cancellation (適格請求書発行事業者の登録取消届出書) | Tax office | 15 days before start of desired cancellation period |
| Payroll office closure (給与支払事務所等の廃止届出書) | Tax office | Within 1 month |
| Enterprise tax cessation (個人事業税の事業廃止届出書) | Prefectural tax office | Promptly |

**Important notes:**
- File the final year's individual income tax return (確定申告) as usual
- Transfer inventory to the corporation at fair market value
- Transfer fixed assets at book value or fair market value (beware of below-market transfers)
- Settle all receivables/payables between individual and corporation
- Consider filing for estimated tax reduction (予定納税の減額申請)

## Section 10 -- Micro Corporation + Sole Proprietorship ("Two-Sword" Strategy)

### Overview

Maintain the sole proprietorship while also establishing a micro corporation (マイクロ法人). The corporation pays minimal officer compensation to access corporate social insurance at the lowest tier.

### Structure

```
Micro Corporation:
  → Officer compensation: ~JPY 63,000/month (JPY 756,000/year)
  → Social insurance: enrolled at minimum tier
  → Annual social insurance (personal share): ~JPY 107,000

Sole Proprietorship (continued):
  → Business income filed via 確定申告
  → No NHI or national pension obligation (covered by corporate insurance)

Compared to sole proprietor only at JPY 10,000,000 income:
  NHI + national pension: ~JPY 1,100,000/year
  Micro corp social insurance (both shares): ~JPY 210,000/year
  Potential savings: ~JPY 890,000/year
```

### Risk Factors

**Risk Factors Table**

| Risk | Description |
| --- | --- |
| Tax denial | If the corporation has no real business activity, it may be treated as a paper company |
| Same business split | Splitting the same client work between personal and corporate is high-risk for denial |
| Zero revenue corporation | A corporation existing solely for social insurance access may be challenged |
| Audit exposure | Cannot explain a reasonable business separation |

**Acceptable examples:** Personal = freelance engineering (main); Corporation = SaaS product development (separate business). **Unacceptable:** Both entities doing the same programming work for the same clients.

## Section 11 -- Optimal Timing

**Optimal Timing Table**

| Factor | Recommended Timing | Reason |
| --- | --- | --- |
| Income tax optimization | Mid-year | Split income between individual (first half) and corporation |
| Consumption tax reset | Before becoming a taxable business | Maximize exemption period |
| Accounting simplicity | January 1 | Clean separation of individual fiscal year and corporate fiscal year |
| Client relationships | Start of quarter | Smoother invoice/contract transition |
| Fiscal year-end choice | Avoid March | Tax advisers are busiest in March; consider September or December |

## PROHIBITIONS

- NEVER present incorporation as universally beneficial -- at lower income levels, sole proprietorship is cheaper
- NEVER recommend specific officer compensation amounts as definitive -- individual circumstances vary
- NEVER ignore social insurance costs in the comparison -- they are often the largest single factor
- NEVER assume consumption tax exemption applies if the corporation registers for qualified invoices
- NEVER recommend the "two-sword" strategy without prominently disclosing tax denial risks
- NEVER omit the annual JPY 70,000+ corporate inhabitant tax (均等割) from cost projections -- it applies even when the corporation has no profit
- NEVER forget to mention tax adviser fees (~JPY 300,000--500,000/year) as a fixed cost of incorporation
- NEVER present simulations as definitive -- always label as estimated and direct to a 税理士 for confirmation

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill.

Incorporation involves tax, legal, and social insurance considerations that vary significantly based on individual circumstances. All decisions must be reviewed and confirmed by qualified professionals (税理士 for tax, 司法書士 for company registration, 社会保険労務士 for social insurance) before acting upon.

Information is based on the 2025 tax year (令和7年分) tax system. Tax laws, social insurance rates, and registration fees change annually.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is
different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your
jurisdiction — **no liability on either side until you and the accountant sign
a formal engagement letter** — book a free 30-minute call:

**→ [Book a call](https://calendly.com/openaccountants-info/30min)**

We'll route you to the named verifier covering your country or state. You can
also see the full list of verified accountants at
[openaccountants.com/network](https://openaccountants.com/network).

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
