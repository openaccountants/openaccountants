---
name: us-form-1120-c-corp
description: Tier 2 US federal content skill for preparing Form 1120 — the US C-corporation income tax return. Covers tax year 2025 under OBBBA including the 21% flat rate, DRD tiers (50/65/100%), §163(j) interest limit (EBITDA add-back restored), §174A domestic R&D immediate expensing (foreign R&D 15-year amortization), §250 GILTI/FDII deduction (50%/37.5% for tax years beginning in 2025; new permanent OBBBA rates of 40%/33.34% from 2026), the 15% Corporate AMT on AFSI > $1B (IRA 2022), required schedules (B, C, J, K, L, M-1/M-3, O, UTP), and common attached forms (4562, 4626, 5471/5472 refer-out, 6765, 8993, 1125-A, 1125-E). Filing due 15th day of 4th month; Form 7004 6-month extension; quarterly estimated 25/25/25/25 with no 110% safe harbor for corps.
jurisdiction: US
category: federal-tax
tier: 2
verified_by: pending
last_updated: 2026-07-04
version: 0.1
---

# US Form 1120 — C-Corporation Income Tax Return (Tax Year 2025)

> Tier 2 federal content skill. MUST be loaded alongside `us-tax-workflow-base` v0.2 or later. Federal only — state corporate income tax is out of scope; route to the relevant state skill when needed.

> **OBBBA update (2026):** Rates, thresholds, and statutory citations in this Guide were corrected against the One Big Beautiful Bill Act following a professional review by **Christopher Aryee, CPA**.

---

## 1. Scope

This skill covers the preparation of **Form 1120, U.S. Corporation Income Tax Return**, for tax year 2025 for a domestic C-corporation operating in the United States. It walks through the income computation, the tax computation on Schedule J, the required schedules (B, C, J, K, L, M-1/M-3, O, UTP where applicable), the most common attached forms, and the corporate-specific provisions that differ from individual taxation (DRD, NOL post-TCJA, §163(j), §174A R&D expensing, §250 GILTI/FDII deduction, and the 15% Corporate Alternative Minimum Tax).

**In scope:**
- Calendar-year and fiscal-year domestic C-corporations chartered in any US state or DC
- LLCs that have elected C-corp treatment via Form 8832
- Single-entity returns (no consolidated returns — see §1.1)
- The 21% flat federal rate computation under IRC §11
- Schedule C dividends-received deduction (DRD)
- Net operating loss (NOL) treatment under the post-TCJA regime (80% limitation, indefinite carryforward, no carryback)
- §163(j) business interest expense limitation
- §174A specified research and experimental (SRE) expensing — domestic immediate expensing, foreign 15-year amortization (OBBBA §70302)
- §250 GILTI/FDII deduction (50% / 37.5% for tax years beginning in 2025; new permanent OBBBA rates of 40% / 33.34% from 2026)
- Corporate Alternative Minimum Tax (CAMT) under IRC §55(b)(2) and §59(k) for applicable corporations
- Estimated tax requirements under IRC §6655 with the corporate safe-harbor rules
- Late filing (§6651) and late payment (§6651(a)(2)) penalties
- E-file mandate under Reg. §301.6011-5

**Out of scope — refer out:**
- **Consolidated returns** (parent + 80%-affiliated subsidiaries filing a single 1120) — refer to `us-form-1120-consolidated` (separate skill).
- **S-corporations** — use `us-form-1120-s`. If the client is considering the S election, route to `us-s-corp-election-decision` first.
- **Personal Service Corporations (PSCs)** — they file Form 1120 but with special rules; flag for reviewer rather than handling here.
- **Personal Holding Companies (§541)** — refer out; Schedule PH attachment is specialized.
- **Tax-exempt corporations** (§501(c) entities filing Form 990) — out of scope.
- **REITs, RICs, cooperatives, life and non-life insurance companies, FSCs, real estate mortgage investment conduits** — each has a dedicated form (1120-REIT, 1120-RIC, 1120-C, 1120-L, 1120-PC, 1120-FSC, 1066) — refer out.
- **Foreign corporations** with US-source income — use Form 1120-F; refer out.
- **Forms 5471 (CFC reporting)** — refer to `us-form-5471-cfc`.
- **Forms 5472 (25%+ foreign-owned US corp reporting)** — refer to `us-form-5472`.
- **Forms 8990/8991 BEAT** — complex; refer to `us-base-erosion-tax`.
- **Form 6765 R&D credit and §174 capitalization mechanics** — refer to `us-r-and-d-credit-and-174`.
- **Stock buyback excise tax (IRC §4501) and Form 7208** — refer to `us-stock-buyback-excise`.
- **State and local corporate income, franchise, gross receipts, and minimum taxes** — route to state skills (e.g., `us-ca-form-100`, `us-tx-franchise-tax`, `us-de-franchise`, `us-ny-form-ct-3`).

### 1.1 Consolidated returns — quick refusal note

If the corporation is part of an affiliated group filing a consolidated return under IRC §1501 and Reg. §1.1502, this skill does **not** apply. The consolidated return introduces SRLY (separate return limitation year) rules for NOLs, intercompany transaction deferrals under Reg. §1.1502-13, excess loss accounts, investment-basis adjustments, the consolidated §163(j) computation, the consolidated CAMT computation, and Forms 851 and 1122. These are out of scope here.

If the corporation has an 80%-or-more parent or 80%-or-more subsidiaries, ask the client whether a consolidated election (Form 1122) is in effect. If yes, refer out. If no, the entities file separate 1120s and this skill applies to each.

---

## 2. Who must file

Under IRC §6012(a)(2) and Reg. §1.6012-2(a), **every domestic corporation in existence during any portion of the taxable year** must file Form 1120, regardless of whether it had taxable income or any activity, unless it falls under one of the special categories listed in §1 above (S-corp, REIT, RIC, exempt org, etc.).

This includes:

1. **Corporations chartered as such under state law** (Inc., Corp., Co., Ltd.) that have not made an S election.
2. **LLCs that have affirmatively elected C-corporation treatment** by filing Form 8832 (Entity Classification Election). The election is effective on the date specified on Form 8832 (which can be up to 75 days before or 12 months after the filing date). From that effective date forward, the LLC files Form 1120, not Schedule C, Form 1065, or Form 1120-S.
3. **Foreign-incorporated entities that have elected to be treated as a US corporation** via Form 8832 (rare but possible for certain hybrid structures).
4. **Inactive corporations** — even a corporation with no income and no activity must file if it remains in existence under state law. The only way out of the filing requirement is formal dissolution under state law (a final return is then required, with the "Final return" box at the top of Form 1120 checked).
5. **First-year and short-year corporations** — a corporation formed mid-year files a short-year 1120 from the date of incorporation through its first chosen year-end. The first return also must include any Form 1128 (change of accounting period) and any §351 transferor disclosures.

### 2.1 Tax year selection

A C-corporation may adopt a **calendar year** (January 1 – December 31) or any **fiscal year** ending on the last day of a month other than December, except:

- **Personal Service Corporations (PSCs)** are generally required to use a calendar year under IRC §441(i) unless they make a §444 election (with required-payment offset on Form 8716 and Form 8752). PSCs are out of scope here — flag for reviewer.
- A **52/53-week year** is permitted under IRC §441(f).
- The tax year is established by the timing of the first return; changes require Form 1128 and IRS consent (Rev. Proc. 2006-45 automatic procedures for most domestic corps).

---

## 3. Rate

### 3.1 The 21% flat rate

For tax years beginning after December 31, 2017, **IRC §11(b) imposes a flat 21% tax on the taxable income of every corporation**. This rate was set by the Tax Cuts and Jobs Act of 2017 (P.L. 115-97) and made permanent (the 21% rate has no sunset). It replaced the prior graduated corporate rate schedule (15%, 25%, 34%, 39%, 34%, 35%, 38%, 35%) and the personal service corporation flat 35% rate.

**Confirmed for 2025:** The 21% rate continues to apply for tax years beginning in calendar year 2025. **The One Big Beautiful Bill Act (P.L. 119-21, July 4 2025) did not change the corporate rate.** Some legislative proposals during 2024-2025 had floated rate changes (a 15% rate for domestic manufacturers, a 28% rate generally), but none were enacted. For any return with a tax year beginning in 2025, use 21%.

### 3.2 Computation

Tax = Taxable income (line 30 of Form 1120) × 21%, computed on **Schedule J, Part I, line 2**.

There is no "small corporation" rate, no graduated bracket, and no first-dollar exclusion. Even a corporation with $1,000 of taxable income pays $210 of federal income tax.

### 3.3 Effect on planning

Because the rate is flat, the long-standing income-shifting strategies (paying bonuses to bring taxable income down to a lower bracket; timing income to land in the 15% bracket) no longer have any first-order effect. The remaining levers are:

- Defer recognition into a year when an NOL exists (post-TCJA NOLs are still subject to the 80% limit, so this is partial).
- Accelerate deductions to reduce taxable income year-on-year (still beneficial because of the time value of money and the §163(j) ATI floor).
- Choose between deductible compensation and dividend distribution (deductible compensation is still preferred at the entity level — dividends are not deductible and create double taxation).

---

## 4. Due dates and extension

### 4.1 Original due date

Under IRC §6072(b) (as amended by the Surface Transportation and Veterans Health Care Choice Improvement Act of 2015, P.L. 114-41), Form 1120 is due on or before the **15th day of the 4th month following the close of the tax year**.

| Tax year-end | Due date |
|--------------|----------|
| December 31, 2025 (calendar year) | **April 15, 2026** |
| January 31, 2026 (fiscal) | May 15, 2026 |
| June 30, 2026 (fiscal) | October 15, 2026 |

**Special rule for fiscal years ending June 30:** For tax years beginning before January 1, 2026, a fiscal-year C-corporation with a June 30 year-end has historically used a September 15 due date (15th day of 3rd month). This special rule for June 30 year-ends was scheduled to phase in to the new 4th-month rule for years beginning **after December 31, 2025**. A June 30, 2026 year-end (i.e., tax year beginning July 1, 2025) is the **first year** for which the new October 15 due date applies. Confirm against current IRS instructions for the year of filing.

If the due date falls on a Saturday, Sunday, or legal holiday, the return is timely if filed on the next business day (IRC §7503).

### 4.2 Extension — Form 7004

A corporation may obtain an **automatic 6-month extension** to file Form 1120 by filing **Form 7004 (Application for Automatic Extension of Time To File Certain Business Income Tax, Information, and Other Returns)** on or before the original due date.

| Tax year-end | Original due | Extended due |
|--------------|--------------|--------------|
| December 31, 2025 | April 15, 2026 | **October 15, 2026** |
| June 30, 2026 | October 15, 2026 | **April 15, 2027** |

**Critical caveat: Form 7004 extends the time to FILE, not the time to PAY.** The corporation must pay the **full estimated balance due** by the original due date to avoid the §6651(a)(2) late-payment penalty (0.5% per month, max 25%) and §6601 interest. If Form 7004 is filed but no payment is made and a balance is owed, the extension is still valid for filing-penalty purposes, but late-payment penalty and interest accrue from the original due date.

Form 7004 requires:
- Estimated total tax liability for the year (Line 6)
- Total payments and credits already made (Line 7)
- Balance due to be paid with the extension (Line 8)

The IRS does not require a reason; the extension is automatic if Form 7004 is properly completed and filed timely.

---

## 5. Estimated tax — IRC §6655 (no 110% safe harbor for corps)

### 5.1 Who must pay

A corporation that expects its tax liability to be **$500 or more** for the year must pay estimated tax in four equal installments (IRC §6655(a) and (f); the $500 threshold is in §6655(f)). Below $500, no estimated payments are required and no penalty applies.

### 5.2 Installment due dates

| Installment | Calendar-year due date |
|-------------|------------------------|
| 1st (April installment) | **April 15, 2025** |
| 2nd (June installment) | **June 16, 2025** (the 15th is a Sunday) |
| 3rd (September installment) | **September 15, 2025** |
| 4th (December installment) | **December 15, 2025** |

For fiscal-year corporations, the installments are due on the 15th day of the 4th, 6th, 9th, and 12th months of the tax year.

Each installment is generally **25%** of the required annual payment.

### 5.3 Required annual payment — the safe harbors

Under IRC §6655(d)(1), the **required annual payment** is the lesser of:

**(a) 100% of the tax shown on the current-year return**, OR
**(b) 100% of the tax shown on the preceding year's return**, provided that:
- The preceding year was a 12-month tax year, AND
- The corporation filed a return for the preceding year showing a liability, AND
- The corporation is **not** a "large corporation."

A **large corporation** is defined in IRC §6655(g)(2) as a corporation with **taxable income of $1 million or more** in any of the **three preceding tax years** (whether or not consecutive). For large corporations, the prior-year safe harbor is **disallowed for the 2nd, 3rd, and 4th installments** — the entire year must be funded based on current-year tax. (The first installment may use the prior-year safe harbor; any shortfall must be made up by the second installment under §6655(d)(2)(B).)

**Key contrast with individual taxation:** Individuals have a 110% prior-year safe harbor when AGI exceeds $150,000. **Corporations do not.** The corporate prior-year safe harbor is always 100% (not 110%), and it is unavailable at all to large corporations after the first installment. Do not confuse the two regimes.

### 5.4 Annualized income installment method

A corporation with uneven income may use the **annualized income installment method** under §6655(e)(2) to reduce installments in lighter quarters. The four annualization periods for a calendar-year corp are:

| Installment | Months annualized | Annualization factor |
|-------------|-------------------|----------------------|
| 1st | First 3 months | 4 |
| 2nd | First 3 months | 4 |
| 3rd | First 6 months | 2 |
| 4th | First 9 months | 1.33333 |

(Note: the IRS provides an alternative option of 2/4/7/10 months under §6655(e)(2)(C) if elected on Form 8842 — this is the "adjusted seasonal" or "seasonal" option for businesses with predictable seasonal patterns.)

This is computed on **Schedule A of Form 2220** and attached to Form 1120 if an underpayment penalty is computed.

### 5.5 Form 2220 — underpayment penalty

If installments are missed or underpaid, the corporation computes the §6655 underpayment penalty on **Form 2220, Underpayment of Estimated Tax by Corporations**, and attaches it to Form 1120. Unlike individuals (who can let the IRS bill them), the IRS instructions direct that corporations **must** compute and attach Form 2220 if the penalty applies — failing to attach can trigger a follow-up notice.

### 5.6 Payment mechanics

Corporate estimated tax payments must be made by **electronic funds transfer (EFT)** through the Electronic Federal Tax Payment System (EFTPS). Paper checks are not permitted for corporate deposits per Reg. §31.6302-1. The Form 1120-W worksheet, while no longer filed, is used internally to compute installments.

---

## 6. Income computation walkthrough

Form 1120 income flows in this order: gross income → total income (line 11) → deductions (lines 12–29) → taxable income before NOL/special deductions (line 28) → less NOL deduction and special deductions (lines 29a and 29b) → taxable income (line 30) → tax (line 31).

### 6.1 Gross income (lines 1–11)

- **Line 1a Gross receipts or sales** — total revenue from the sale of goods or services before any returns, allowances, or discounts.
- **Line 1b Returns and allowances** — sales returns, allowances, and discounts. Note: cash discounts to customers may be netted here or treated as a deduction; be consistent year-over-year.
- **Line 1c Net** = 1a − 1b.
- **Line 2 Cost of goods sold** — from **Form 1125-A** (mandatory if there is COGS). See §11.4.
- **Line 3 Gross profit** = Line 1c − Line 2.
- **Line 4 Dividends and inclusions** — from **Schedule C, Line 23, Column (a)**. Gross dividend income, before the DRD (the DRD is taken later as a special deduction on Line 29b).
- **Line 5 Interest** — taxable interest from bank deposits, taxable bonds, etc. Tax-exempt interest is reported on Schedule K, Line 9, not Line 5.
- **Line 6 Gross rents.**
- **Line 7 Gross royalties.**
- **Line 8 Capital gain net income** — from **Schedule D (Form 1120)**. Net of long-term and short-term gains and losses. Corporate capital losses are deductible only against capital gains (not ordinary income); excess losses carry back 3 years and forward 5 years (IRC §1212(a)) — this differs from the individual rule.
- **Line 9 Net gain or (loss) from Form 4797**, Part II — §1231 gains and ordinary recapture (§1245, §1250). Net §1231 gain is treated as long-term capital gain and flows to Schedule D; a net §1231 loss is ordinary and flows to Line 9.
- **Line 10 Other income** — recovery of bad debts, federal tax refund of taxes previously deducted, life insurance proceeds where deducted, gross income from §481(a) adjustments, etc. Attach a statement detailing the components.
- **Line 11 Total income.**

### 6.2 Deductions (lines 12–29)

| Line | Item | Notes |
|------|------|-------|
| 12 | Compensation of officers | From **Form 1125-E** if receipts ≥ $500,000. See §13. |
| 13 | Salaries and wages | Less §41 credit and §51 work opportunity credit reductions. |
| 14 | Repairs and maintenance | Distinguish from capitalized improvements under §263(a) and the tangible property regulations (Reg. §1.263(a)-3). |
| 15 | Bad debts | Specific charge-off method only for corporations (§166); no reserve method. |
| 16 | Rents | Real and personal property rentals; flag related-party rents under §267. |
| 17 | Taxes and licenses | State and local income, real and personal property, payroll (employer share), excise. **Federal income tax is NOT deductible.** State income tax is deductible (no $10k SALT cap — that applies only to individuals). |
| 18 | Interest | Subject to **§163(j) limitation** — see §8. Compute on Form 8990 if not exempt. |
| 19 | Charitable contributions | Limited to **10% of taxable income** before the contribution itself, the DRD, and any NOL or capital loss carryback (§170(b)(2)(A)). Excess carries forward 5 years. |
| 20 | Depreciation | From **Form 4562**; carry to Line 20 after subtracting any included in COGS on Form 1125-A. |
| 21 | Depletion | Cost or percentage; not on oil and gas if integrated producer over thresholds. |
| 22 | Advertising | Includes website production costs that are not capitalized. |
| 23 | Pension, profit-sharing, etc. | Employer contributions; see §404 timing rules. |
| 24 | Employee benefit programs | Health, group term life, dependent care, etc., not deducted elsewhere. |
| 25 | Reserved (formerly DPAD; repealed by TCJA). | Leave blank. |
| 26 | Other deductions | Attach statement. Common items: insurance, utilities, professional fees, office expense, travel and meals (50% limit per §274(n)), software subscriptions, bank fees, domestic R&E expenses now immediately deductible under §174A (see §10). |
| 27 | Total deductions. | |
| 28 | Taxable income before NOL deduction and special deductions = Line 11 − Line 27. | |
| 29a | Net operating loss deduction. | See §7. |
| 29b | Special deductions — from **Schedule C, Line 24**. | Primarily DRD; also §250 GILTI/FDII deduction. |
| 29c | Total = 29a + 29b. | |
| 30 | Taxable income = Line 28 − Line 29c (not less than zero except in the year a loss is generated). | |
| 31 | Total tax — from **Schedule J, Part I, Line 11**. | |

### 6.3 Lines 32–37 — Payments, credits, and balance

- Line 33 (formerly 33a-g): Estimated tax payments, prior year overpayment credit, Form 7004 extension payment, refundable credits.
- Line 34: Estimated tax penalty (Form 2220).
- Line 35: Amount owed.
- Line 36: Overpayment.
- Line 37: Refund vs. credit forward.

---

## 7. Dividends-Received Deduction (DRD) — Schedule C

### 7.1 Purpose and structure

The DRD under IRC §243 mitigates the triple taxation that would otherwise occur when a corporation receives a dividend from another corporation (the dividend was paid out of earnings already taxed at the payor's level; without the DRD, the recipient corp would pay 21% on it and then its shareholder would pay tax again on distribution). The deduction is computed on **Schedule C of Form 1120** and flows to Line 29b via Schedule C Line 24.

### 7.2 The three tiers

| Ownership of payor by recipient corp | Deduction % | IRC section |
|---|---|---|
| **Less than 20%** | **50%** | §243(a)(1) |
| **20% to less than 80%** | **65%** | §243(c) |
| **80% or more (affiliated group, no consolidated return)** | **100%** | §243(a)(3) and §243(b) — "qualifying dividends" |

The TCJA reduced the DRD from 70%/80%/100% to 50%/65%/100% effective 2018; this remains in effect for 2025.

Ownership is measured by **vote and value** (§243(c)(2)). For the 80% tier, the affiliated group must meet the §1504(a) definition (80% of vote and value, with attribution rules in §1563), and the dividend must be a "qualifying dividend" under §243(b) — generally, a dividend from a domestic corporation that is a member of the same affiliated group (whether or not consolidated). If consolidated, intercompany dividends are eliminated and the DRD is moot.

### 7.3 Special categories on Schedule C

Schedule C has many specific lines for distinct categories. Key lines:

- **Lines 1, 2 Dividends from less-than-20% / 20%-or-more domestic corps** — the bread-and-butter 50% / 65% DRD.
- **Line 3 Dividends on certain debt-financed stock** — DRD reduced under §246A if the stock was acquired with debt; reduction is in proportion to debt-financing percentage.
- **Line 4 Dividends on certain preferred stock of public utilities** — special 23.3% / 26.7% rate.
- **Line 6/7 Dividends from foreign corps that are 20%-or-more US-owned** — eligible for partial DRD.
- **Line 8 Dividends from wholly-owned foreign subsidiaries** — fully deductible under §245(b), but only if certain conditions met.
- **Line 13 Dividends received from a domestic corp that is a member of the same affiliated group (other than debt-financed)** — 100% DRD.
- **Line 14 Other dividends** — including subpart F inclusions, GILTI inclusion, §965 transition tax inclusion. **Subpart F and GILTI inclusions are not eligible for the DRD** (separately, GILTI is partially offset by the §250 deduction — see §10).
- **Line 15 §245A 100% participation exemption** — for dividends from 10%-owned specified foreign corporations meeting holding period requirements. This is a 100% deduction, not a true DRD; it implements the post-TCJA territorial system.

### 7.4 Holding period rule — §246(c)

The DRD is **disallowed** if the recipient corp does not hold the stock for **more than 45 days during the 91-day period beginning 45 days before the ex-dividend date** (for common stock; 90/181 days for preferred). The holding period is reduced by periods during which the corp has substantially diminished its risk of loss (hedges, options, short positions). Verify with the client that the stock was held throughout — this is a common audit issue with portfolio dividend recipients.

### 7.5 Taxable-income limitation — §246(b)

The aggregate DRD (excluding the 100% DRD from affiliated-group dividends and the §245A participation exemption) is **limited to a percentage of taxable income** computed without regard to the DRD, NOL deduction, §250 deduction, and §1202 deduction. The percentage matches the DRD tier — 50% or 65%.

**Exception:** the limitation does not apply if the DRD creates or increases an NOL (the "NOL exception"). This is computed on **Schedule C, Lines 17 through 22** with worksheet support in the Form 1120 instructions.

### 7.6 Worked DRD computation

**Facts:**
- Corp A holds 5% of Corp B (publicly traded). Receives $100,000 dividend.
- Corp A holds 30% of Corp C (private). Receives $200,000 dividend.
- Corp A holds 100% of Corp D (member of same affiliated group). Receives $500,000 dividend.

**DRD:**
- B: $100,000 × 50% = $50,000
- C: $200,000 × 65% = $130,000
- D: $500,000 × 100% = $500,000 (no §246(b) limit applies)
- **Total DRD on Schedule C, Line 24 = $680,000** flowing to Form 1120, Line 29b.

If the §246(b) limit applies (assume taxable income before DRD is $260,000), then:
- 50% × $260,000 = $130,000 cap on the 50% DRD ($50,000 is under cap — OK)
- 65% × $260,000 = $169,000 cap on the 65% DRD ($130,000 is under cap — OK)
- 100% DRD is not subject to limit.

If instead taxable income before DRD were $50,000, the 50% DRD would be capped at $25,000 unless the NOL exception applied. Apply the NOL exception test on the Schedule C worksheet.

---

## 8. Net Operating Loss (NOL) — post-TCJA rules

### 8.1 Post-2017 NOLs

For NOLs **generated in tax years beginning after December 31, 2017** (i.e., 2018 forward, including 2025):

- **No carryback.** (The CARES Act temporarily restored a 5-year carryback for 2018, 2019, 2020 losses only — that window is now closed.)
- **Indefinite carryforward** under IRC §172(b)(1)(A).
- **80% limitation** under §172(a) — the NOL deduction in any year is limited to **80% of taxable income computed without regard to the NOL deduction itself** (and without regard to the §199A and §250 deductions — those are computed after).

The 80% limit applies only to post-2017 NOLs; it does not stack on pre-2018 NOLs in the same year (the pre-2018 NOL is taken first under the old rules, then the post-2017 NOL is taken subject to the 80% cap on remaining taxable income).

### 8.2 Pre-2018 NOLs

NOLs generated in tax years beginning before January 1, 2018 retain their original-rule treatment:

- **2-year carryback, 20-year carryforward** (§172(b)(1)(A) as in effect pre-TCJA).
- **No 80% limit** — can offset 100% of taxable income.
- Most pre-2018 NOLs have either been used or are nearing the end of their 20-year window. A 2005 NOL expires in 2025; a 2017 NOL expires in 2037.

If both pre-2018 and post-2017 NOLs exist, apply them in this order: (1) pre-2018 NOLs first, without the 80% limit; (2) post-2017 NOLs second, subject to the 80% limit on remaining taxable income.

### 8.3 §382 limitation on NOL after ownership change

If the corporation underwent an **ownership change** (more than 50 percentage point shift in 5%-shareholder ownership over a 3-year testing period) under IRC §382(g), the use of pre-change NOLs is limited annually to:

**§382 limitation = FMV of equity immediately before the ownership change × long-term tax-exempt rate** (published monthly by the IRS — for ownership changes in 2025, in the 4% range; check the AFR table for the change date).

Plus a NUBIG (net unrealized built-in gain) adjustment in years where built-in gains are recognized within 5 years of the change. Flag any §382 event for reviewer — the computation is technical and commonly missed.

### 8.4 Worked NOL example

**Facts:**
- 2024: NOL of $1,000,000 (post-TCJA NOL).
- 2025: Taxable income before NOL = $800,000.

**Computation:**
- 80% × $800,000 = $640,000 (the 80% cap)
- 2024 NOL available = $1,000,000
- NOL used in 2025 = lesser of $640,000 (cap) or $1,000,000 (available) = $640,000
- Taxable income after NOL = $800,000 − $640,000 = $160,000
- Tax = $160,000 × 21% = $33,600
- Remaining NOL carryforward to 2026 = $1,000,000 − $640,000 = $360,000

Even though there was a $1M NOL fully covering the $800k income, only $640k could be used because of the 80% limit. The corporation still owes $33,600 of federal tax for 2025.

---

## 9. §163(j) business interest expense limitation

### 9.1 The limit

For tax years beginning after December 31, 2017, IRC §163(j) limits the deduction for **business interest expense** to the sum of:

1. **Business interest income** for the year, plus
2. **30% of "adjusted taxable income" (ATI)**, plus
3. **Floor plan financing interest** (specific to vehicle dealers).

Disallowed business interest **carries forward indefinitely** and is deducted in future years subject to the same limit.

### 9.2 ATI definition — EBITDA add-back restored by OBBBA

From tax years beginning in 2022 through 2024, ATI was computed on an **EBIT** base (no add-back for depreciation, amortization, or depletion), which tightened the §163(j) limit for capital-intensive businesses. **OBBBA (§70303) permanently restored the EBITDA add-back** for tax years **beginning after December 31, 2024**.

**For 2025:** ATI is **EBITDA-based** — **add back depreciation, amortization, and depletion** (in addition to business interest expense, any NOL deduction, and the §250 deduction) when computing ATI. This loosens the limit for capital-intensive businesses. Confirm against the Form 8990 instructions current for 2025.

Source: OBBBA §70303; IRC §163(j).

### 9.3 Small-business exemption

A taxpayer is **exempt** from §163(j) if its **average annual gross receipts for the prior 3 years are at or below the §448(c) threshold** — **$31 million** for tax years beginning in 2025 (inflation-adjusted; was $30M in 2024). A corporation that satisfies this test does not need to file Form 8990 (except in limited circumstances such as passing through interest to a partner).

### 9.4 Other exemptions

- Electing real property trades or businesses (irrevocable election under §163(j)(7)(B)) — must use ADS for nonresidential real, residential rental, and qualified improvement property; trades off the §163(j) limit for slower depreciation.
- Electing farming businesses (similar trade-off).
- Regulated utilities (§163(j)(7)(A)(iv)) — automatically excluded.

### 9.5 Mechanics

Computed on **Form 8990, Limitation on Business Interest Expense Under Section 163(j)**, attached to Form 1120 if applicable. The disallowed interest carryforward is tracked on Form 8990 Schedule A.

### 9.6 Worked §163(j) example

**Facts (corp not subject to small-business exemption):**
- Taxable income (before interest deduction) = $5,000,000
- Depreciation = $1,500,000 (already in deductions)
- Business interest expense = $1,800,000
- Business interest income = $50,000
- Floor plan financing = $0

**ATI computation (EBITDA-based, 2025 — OBBBA add-back restored):**
- Start with taxable income before interest = $5,000,000
- Add back: business interest expense ($1,800,000) — yes
- Add back: depreciation/amortization/depletion ($1,500,000) — **yes** (restored by OBBBA §70303)
- Add back: NOL deduction — yes
- Add back: §250 deduction — yes
- ATI = $5,000,000 + $1,800,000 + $1,500,000 = $8,300,000 (assume no NOL or §250)

**Limit:**
- 30% × $8,300,000 = $2,490,000
- Plus business interest income $50,000 = $2,540,000

**Result:**
- Business interest of $1,800,000 ≤ $2,540,000 limit → fully deductible.

**Alternative (tight scenario):**
- If business interest = $3,000,000:
- Deductible = $50,000 (interest income) + $2,490,000 (30% × ATI) = $2,540,000
- Disallowed and carried forward = $3,000,000 − $2,540,000 = $460,000

---

## 10. §174 / §174A R&D expensing

### 10.1 The rule after OBBBA — new §174A

The TCJA required **capitalization and amortization** of "specified research and experimental expenditures" (SREs) for tax years beginning after December 31, 2021 (domestic over 5 years, foreign over 15 years). **OBBBA (§70302) enacted a new IRC §174A that reverses this for domestic R&D:**

- **Domestic SREs:** for tax years **beginning after December 31, 2024**, domestic research or experimental expenditures may be **fully expensed IMMEDIATELY** in the year incurred under §174A. (A taxpayer may instead elect to capitalize and amortize over not less than 60 months, but immediate expensing is the default.) The domestic §174A deduction **must be reduced by the §41 research credit** unless the §280C(c)(2) reduced-credit election is made.
- **Foreign SREs** (R&E performed outside the US): **no change** — these remain subject to **15-year (180-month)** capitalization and amortization, beginning at the midpoint of the year incurred.

Source: OBBBA §70302; IRC §174A.

### 10.2 Status after OBBBA

**OBBBA (§70302) restored immediate expensing of domestic R&D through new IRC §174A**, effective for tax years beginning after December 31, 2024. For any 2025 return, domestic SREs are **deductible in full in the year incurred** (subject to the §41-credit reduction); they are no longer capitalized over 5 years. The long line of restoration proposals (the Tax Relief for American Families and Workers Act of 2024, the "Build It in America Act," etc.) has therefore been overtaken — the fix is now law.

Only **foreign** R&E remains on the 15-year amortization schedule. Confirm which expenditures are domestic vs. foreign, because the treatment now diverges sharply.

### 10.3 What counts as SRE

"Specified research or experimental expenditures" under §174(b) include:

- Direct labor and materials for R&D.
- Software development costs (explicitly included under §174(c)(3)).
- Allocated overhead reasonably attributable to R&D.
- Patent costs (legal and filing fees in obtaining a patent, but not litigation).
- Costs that would have been §41 qualified research expenses under prior law.

What does NOT count: market research, quality control, advertising, management studies, routine data collection, efficiency surveys, social science research (in some cases — see §174(d)).

### 10.4 Mechanics on Form 1120

- **Domestic SREs incurred in 2025 are directly deductible** in full under §174A — take them on the appropriate expense line (e.g., Line 26, "Other deductions"). They are no longer capitalized on Form 4562.
- **Foreign SREs** are still capitalized on Form 4562 (intangibles section) and amortized over 15 years (180 months), beginning at the midpoint of the year incurred; the current-year amortization flows to Form 1120 Line 26 as "amortization of §174 costs."
- Remember to reduce the domestic §174A deduction by the §41 credit under §280C(c) unless the reduced-credit election is made (see §10.5).

**Refer R&D mechanics to `us-r-and-d-credit-and-174` for detail.** This skill notes the existence of the rule and flags it for the preparer; for any return with material R&E spend (defined here as >$50k of arguable SRE), the R&D skill should be loaded alongside.

### 10.5 Interaction with §41 R&D credit

The §41 R&D credit is **still available** in 2025, computed on **Form 6765**. There is no incompatibility between capitalizing under §174 and claiming the §41 credit. However, under §280C(c)(1), the §174 capitalized amount must be **reduced by the §41 credit** unless the taxpayer makes the §280C(c)(2) reduced-credit election. This interaction is computed on Form 6765 Section A or B.

---

## 11. §250 GILTI / FDII deduction

### 11.1 What §250 does

For tax years beginning after December 31, 2017, IRC §250 (added by TCJA §14202) provides domestic C-corporations a deduction for two categories of income:

1. **GILTI** (Global Intangible Low-Taxed Income inclusion under §951A) — a **50% deduction**, effectively bringing the GILTI tax rate to 10.5% (50% × 21%).
2. **FDII** (Foreign-Derived Intangible Income, generally income from US-based serving of foreign markets) — a **37.5% deduction**, effectively bringing the FDII rate to 13.125% (62.5% × 21%).

### 11.2 The 2025 rates and the new permanent OBBBA rates from 2026

**For tax years beginning in 2025, the 50% (GILTI) / 37.5% (FDII) deduction rates still apply.**

The pre-OBBBA law scheduled a drop to 37.5% / 21.875% after 2025. **OBBBA (§70321) repealed that scheduled cut and set NEW PERMANENT deduction rates for tax years beginning after December 31, 2025:**

- **FDII deduction: 33.34%** (not the old 21.875%).
- **GILTI deduction: 40%** — GILTI is also **renamed "net CFC tested income"** under OBBBA.

So from 2026 the deductions are **higher** than the old scheduled sunset rates, and permanent. Update multi-year planning for clients with material GILTI/net CFC tested income and FDII.

Source: OBBBA §70321; IRC §250(a)(1).

### 11.3 The taxable-income limitation — §250(a)(2)

The aggregate §250 deduction is limited to taxable income (computed without regard to the §250 deduction). If the limit binds, the deduction is allocated proportionally between FDII and GILTI categories under §250(a)(2)(B).

### 11.4 Mechanics

Computed on **Form 8993, Section 250 Deduction for Foreign-Derived Intangible Income (FDII) and Global Intangible Low-Taxed Income (GILTI)**. The deduction flows to **Schedule C, Line 22**, which then flows to Form 1120 Line 29b via Schedule C Line 24.

GILTI inclusion itself flows to Schedule C Line 14 (as "other dividends" — historically a misleading classification, since GILTI is not actually a dividend; it's a deemed inclusion under §951A). The Form 5471 Schedule I-1 supports the GILTI computation.

### 11.5 Refer-out for complex computations

The actual GILTI computation (tested income, QBAI return, allocated deductions, high-tax exclusion election under §951A(c)(2)(B)(ii) Reg. §1.951A-2(c)(7)) is highly technical. Similarly, the FDII computation (deduction-eligible income, foreign-derived deduction-eligible income, deemed intangible income) involves multi-step allocations under Reg. §1.250(b)-1 through -6. For any return with material GILTI or FDII, refer to `us-gilti-fdii-computation` (separate skill).

This skill notes the existence of the deduction, the 2025 rates, and the form (8993), and ensures the line items flow correctly on Form 1120 and Schedule C.

### 11.6 OBBBA restriction on Deduction Eligible Income (DEI)

**OBBBA (§70322) narrowed the FDII base.** For **sales or dispositions after June 16, 2025**, Deduction Eligible Income (DEI) **excludes any gain from the sale or disposition of intangible property and of depreciable, amortizable, or depletable property**. In addition, **interest expense and research and experimental expenditures are no longer subtracted** in arriving at DEI. Both changes reduce the FDII base for affected taxpayers. Apply the new DEI rules to any post-June 16, 2025 disposition when computing FDII on Form 8993.

Source: OBBBA §70322; IRC §250(b)(3)(A)(i)(VII).

### 11.7 OBBBA FTC haircut on §951A-related PTEP distributions

**Warning:** **OBBBA (§70312(b)) disallows 10% of the foreign taxes** deemed paid on **distributions of previously-taxed earnings and profits (PTEP) attributable to §951A (GILTI / net CFC tested income) inclusions**, for distributions **after June 28, 2025**. In other words, only 90% of those foreign taxes are creditable. Report the affected taxes on **Schedule G of Form 1118**. This interacts with the Schedule J foreign tax credit — do not claim the full 100% on §951A-related PTEP distributions after that date.

Source: OBBBA §70312(b); IRC §960(d)(4).

---

## 12. Corporate Alternative Minimum Tax (CAMT) — 15% on AFSI

### 12.1 Origin and rate

The Inflation Reduction Act of 2022 (P.L. 117-169, §10101) added IRC §55(b)(2) and §59(k), imposing a **15% Corporate Alternative Minimum Tax** on the **Adjusted Financial Statement Income (AFSI)** of "applicable corporations" for tax years beginning after December 31, 2022.

This is NOT the same as the corporate AMT that existed under prior law (repealed by TCJA in 2018). The new CAMT is **book-income-based**, not tax-base-based, and applies only to very large corporations.

### 12.2 Who is an "applicable corporation"

Under §59(k)(1)(B), a corporation is an "applicable corporation" if its **average annual AFSI exceeds $1 billion** over the **3 prior tax years** (or such shorter period as the corporation has existed). For a corporation that is a member of a foreign-parented multinational group, a separate $100M test applies under §59(k)(2).

Once a corporation becomes an applicable corporation, it generally remains one in future years (with limited exceptions for sustained drops in AFSI).

**Practical effect:** CAMT applies only to a few thousand of the largest US corporations. If the corporation's revenue is under $500M, CAMT essentially never applies; if AFSI is under $700M-ish on a 3-year average, the test is unlikely to be met. For mid-size and small corps, the answer is "no CAMT" and the corp does not need to compute it.

### 12.3 AFSI definition — book income, adjusted

AFSI starts with **net income or loss reported on the applicable financial statement** (generally the GAAP consolidated income statement, or IFRS if no GAAP — order of priority is in §451(b)(3)) and applies adjustments specified in §56A:

- Add back: federal income tax expense.
- Adjust for: depreciation differences between book and tax (§56A(c)(13) — added by IRA, allowing tax depreciation in lieu of book depreciation in AFSI to avoid penalizing capital investment).
- Adjust for: tax-credit-related items, certain employee benefit items, partnership and CFC pass-throughs.
- Adjust for: §168(k) bonus depreciation (allowed as a deduction against AFSI under §56A(c)(13)).
- Reduce by: financial statement NOL (FSNOL), limited to 80% of pre-FSNOL AFSI.

### 12.4 The 15% computation

If applicable:
- **Tentative minimum tax (TMT) = 15% × AFSI** (after FSNOL).
- **CAMT = max(0, TMT − Regular tax + BEAT)** — i.e., the corp pays CAMT only to the extent it exceeds regular tax.

The regular tax for this purpose includes the §11 21% tax plus BEAT, but excludes the corporate AMT itself.

### 12.5 Foreign tax credit

A **CAMT foreign tax credit** is available under §59(l) — limited to AFSI-equivalent foreign taxes; mechanics are intricate.

### 12.6 Refundable nature

CAMT paid creates a **CAMT credit** (§53) carried forward indefinitely, usable in future years to reduce regular tax (but not below TMT). It is **not refundable** in cash; it offsets future regular tax.

### 12.7 Mechanics

CAMT is computed on **Form 4626, Alternative Minimum Tax — Corporations** (revised for 2023 and forward to reflect the IRA changes). For 2025, the form requires:

- AFSI computation worksheet.
- Adjustments under §56A.
- FSNOL computation.
- TMT computation.
- Comparison with regular tax.
- CAMT credit carryforward tracking.

For any corp with revenue ≥ $500M or with international operations and a parent group ≥ $1B in revenue, run the §59(k) test. For everyone else, document the conclusion that CAMT does not apply (the corp is not an applicable corporation) and skip Form 4626.

### 12.8 Provisional and final regulations

Treasury issued proposed regulations (REG-112129-23, September 2024) that run several hundred pages. Final regs may differ. For any actual CAMT computation, refer to `us-corporate-amt-computation` (separate skill) — this is too specialized for first-line preparation under this skill.

---

## 13. Required schedules walkthrough

### 13.1 Schedule B — Additional Information for Schedule M-3 Filers

Schedule B asks 13 yes/no questions, primarily directed at consolidated group, ownership, and accounting-method disclosures. Required of all 1120 filers. Key questions:

- 1: Is the corporation a subsidiary in an affiliated group or parent-subsidiary controlled group?
- 4a, 4b: At end of year, did any individual or estate own (directly or indirectly under §267(c)) 50% or more of total voting stock?
- 5a, 5b: At year-end, did the corp own 20% or more of voting stock of any other corporation, or 50% or more in any partnership?
- 6: During the year, did the corporation pay dividends in excess of E&P?
- 12: Does the corporation have a financial accounting method that materially differs from the tax accounting method? (Drives M-3 requirement.)
- 13: During the tax year, did the corp dispose of any tangible property by like-kind exchange? (§1031 is now real-property-only post-TCJA.)

### 13.2 Schedule C — Dividends, Inclusions, and Special Deductions

See §7. The DRD lines, the §245A participation exemption, the §250 deduction (Line 22), and various subpart F / GILTI inclusions all flow through Schedule C.

### 13.3 Schedule J — Tax Computation and Payment

Computes the actual tax:

**Part I — Tax computation:**
- Line 1: Check if a "personal holding company" — flag and refer if yes.
- Line 2: **Income tax = Line 30 × 21%**.
- Line 3: Base erosion minimum tax (Form 8991) — refer to BEAT skill.
- Line 5: Add §59A BEAT, §965 transition tax installments if any.
- Line 6 onwards: nonrefundable credits, foreign tax credit (Form 1118), general business credit (Form 3800), §53 prior-year minimum tax credit, etc.
- Line 9: Personal holding company tax (Schedule PH).
- Line 9a–9g: Other taxes — CAMT (Form 4626), §1374 built-in gains tax (former S that converted — out of scope here), §1375 excess passive investment income tax (S-corps — out of scope), §1291 excess distribution tax from PFIC.
- Line 10: Total tax = sum of regular + AMT + other taxes.
- Line 11: Total tax flowing to Form 1120 Line 31.

**Part II — Payments and refundable credits:**
- Prior year overpayment, current-year estimated tax, Form 7004 extension payment, refundable credits.

**Part III — Payments and refundable credits (continued).**

### 13.4 Schedule K — Other Information

A miscellany of yes/no and dollar items used by IRS examiners to identify audit issues:

- Accounting method (cash, accrual, hybrid).
- Business activity code (NAICS).
- Direct ownership by foreign person of 25% or more (triggers Form 5472).
- Whether the corp had any §351 transferor or §1244 stock issuance.
- Tax-exempt interest (§103 — not on Line 5).
- Schedule UTP filing (Line 15).
- §163(j) status (Line 23, asking whether the corp is subject to and required to file Form 8990).
- §59A BEAT status (Line 24, asking whether BEAT applies).
- §267A hybrid disallowance.
- §59(k) CAMT applicability (Line 29 — added in 2023 for the IRA CAMT).

### 13.5 Schedule L — Balance Sheets per Books

Required if **total receipts AND total assets** are both **$250,000 or more at year-end**. Even if the threshold is not met, Schedule L is often prepared internally for the M-1 reconciliation.

Year-beginning and year-end columns for:
- Assets: cash, receivables, inventory, federal/state tax securities, other current assets, loans to shareholders, mortgage and real estate loans, other investments, buildings (with accumulated depreciation), depletable assets, intangibles (less amortization), other.
- Liabilities and equity: accounts payable, short-term notes, current portion of mortgages, other current liabilities, loans from shareholders, long-term mortgages, other liabilities, capital stock, additional paid-in capital, retained earnings — appropriated and unappropriated, adjustments to shareholders' equity, treasury stock, less cost of treasury stock.

The end-of-year balance sheet must tie to the books and to Schedule M-1/M-3.

### 13.6 Schedule M-1 — Reconciliation of Book Income to Tax Income

Required if Schedule M-3 is not required. Reconciles:

- Net income per books (Line 1) + federal income tax (Line 2) + excess of capital losses over gains (Line 3) + income subject to tax not on books (Line 4) + expenses on books not deducted (Line 5) − income on books not on return (Line 7) − deductions on return not charged against book income (Line 8) = **taxable income before NOL and special deductions** (must equal Form 1120 Line 28).

Common Line 5 items: 50% of meals, fines and penalties, federal tax expense (also on Line 2), political contributions, lobbying (§162(e)), club dues, executive comp over §162(m) $1M limit, certain disallowed fringe benefits.

Common Line 7 items: tax-exempt interest, life insurance proceeds, federal income tax refund of prior-year taxes if not previously deducted.

Common Line 8 items: tax depreciation in excess of book, §199A — N/A (corp), §250 deduction (if not in book), §168(k) bonus deduction.

### 13.7 Schedule M-3 — Net Income (Loss) Reconciliation

**Required** if **total assets at year-end are $10 million or more** (Schedule B Question 1 or the M-3 instructions; the threshold is in Reg. §1.6011-4(c)(1)). For total assets under $10M, M-1 is used instead; corps with assets between $10M and $50M may file Schedule M-1 in lieu of M-3 only in limited circumstances.

Schedule M-3 has three parts:
- **Part I:** Financial Statement Information — identifies the source of book income (Form 10-K, certified audit report, internal financials).
- **Part II:** Reconciliation of net income per income statement to taxable income — line by line on income items.
- **Part III:** Reconciliation on expense and deduction items.

Schedule M-3 is far more detailed than M-1 and is used by IRS LB&I examiners to identify large book-tax differences for audit selection. Misclassifications between permanent and temporary differences (Columns A through D) commonly cause IRS notices.

### 13.8 Schedule O — Consent Plan and Apportionment for a Controlled Group

Required if the corporation is a **member of a controlled group under §1561** that elects to apportion the §11 rate brackets (now irrelevant under the flat 21% rate — but Schedule O is still used to apportion certain other items, particularly the AMT exemption pre-2018 and the §535 accumulated earnings credit). For 2025, the practical use of Schedule O has narrowed. Still required if the corp is a member of a controlled group and certain elections are made.

### 13.9 Schedule UTP — Uncertain Tax Positions

Required if **total assets are $10 million or more** AND the corp has at least one uncertain tax position reserved for in audited financial statements (GAAP ASC 740-10, formerly FIN 48). Discloses:

- Each UTP, by IRC section.
- Ranking by size of reserve.
- Description of the position (concise — the IRS provides examples in the Schedule UTP instructions).

Failure to file Schedule UTP when required does not have a stand-alone penalty (per IRS internal practice), but it draws scrutiny. Refer technical UTP analysis to the tax provision team or specialist — this skill flags the obligation but does not analyze the positions.

---

## 14. Common attached forms

| Form | When attached |
|------|--------------|
| **Form 1125-A — Cost of Goods Sold** | Mandatory if there is any COGS on Form 1120 Line 2. |
| **Form 1125-E — Compensation of Officers** | Mandatory if total receipts are **$500,000 or more**. See §15. |
| **Form 4562 — Depreciation and Amortization** | Attach if any §168(k) bonus, §179, MACRS placed in service this year, or any amortization (§174A foreign, §195, §197). **§179 (OBBBA §70306):** for property placed in service in tax years beginning after December 31, 2024, the §179 expensing **limit is $2.5 million** and the **phase-out threshold is $4 million** (both up from the prior $1.25M / $3.13M and indexed thereafter). Source: OBBBA §70306; IRC §179(b). |
| **Form 4626 — CAMT** | Attach if the corp is an "applicable corporation" under §59(k); see §12. |
| **Form 4797 — Sales of Business Property** | §1231 gains/losses, §1245/§1250 recapture, §1252/§1254/§1255 recapture, ordinary income from §1239 related-party gain. |
| **Schedule D (Form 1120)** | Capital gain net income on Line 8; net of short-term and long-term. |
| **Form 5471 — Information Return for CFCs** | Required if the corp is a US shareholder of a controlled foreign corporation. **Refer to `us-form-5471-cfc`.** |
| **Form 5472 — Information Return of 25% Foreign-Owned US Corp** | Required if 25% or more of the corp is owned by a foreign person at any time during the year. **Refer to `us-form-5472`.** |
| **Form 6765 — Credit for Increasing Research Activities (R&D credit)** | §41 credit; mandatory for §174 SRE coordination. **Refer to `us-r-and-d-credit-and-174`.** |
| **Form 8990 — §163(j) Limitation on Business Interest** | If subject to §163(j) and not exempt under §448(c). |
| **Form 8991 — BEAT (§59A)** | If the corp meets the BEAT thresholds (3-year avg gross receipts ≥ $500M and base erosion %≥ 3%). **Refer to BEAT skill.** |
| **Form 8993 — §250 Deduction** | If any GILTI inclusion or FDII; see §11. |
| **Form 7004 — Extension** | Filed by original due date for 6-month extension. |
| **Form 2220 — Underpayment of Estimated Tax** | If any installment underpaid; attach to 1120 (do not let the IRS bill). |
| **Form 3800 — General Business Credit** | If claiming any §38 credit; aggregates §41, §47, §45, §45L, §45Q, etc. |
| **Form 1118 — Foreign Tax Credit (Corps)** | If claiming FTC. **Refer to FTC skill.** |
| **Form 8832 — Entity Classification Election** | Attach to first 1120 if an LLC elected C-corp treatment in the first year. |
| **Form 8716 — §444 Election** (PSCs only) | Out of scope. |
| **Form 1128 — Application to Adopt/Change Tax Year** | If changing year. |
| **Form 7208 — Excise Tax on Stock Buybacks** | Filed quarterly, not with 1120. **Refer to buyback excise skill.** |
| **Form 8975 — Country-by-Country Report** | If parent of multinational group with revenue ≥ $850M. **Refer out.** |
| **Schedule UTP** | If applicable; see §13.9. |

---

## 15. Officer compensation — Form 1125-E

Under IRC §6651 and the Form 1120 instructions, **Form 1125-E is required when the corporation's total receipts (Form 1120 Line 1a + Line 4 + Lines 5–10) are $500,000 or more**.

Form 1125-E discloses:
- Name and SSN of each officer (or top-paid officers if many).
- Percent of time devoted to the business.
- Percent of voting stock owned.
- Amount of compensation paid (cash + non-cash).

The total from Form 1125-E flows to Form 1120 **Line 12**.

### 15.1 Reasonable compensation issue

Unlike S-corps (where reasonable compensation is an issue about *underpayment* — owners trying to recharacterize wages as distributions to avoid payroll tax), C-corps face a *reasonable compensation* issue under §162(a) about *overpayment* — owner-employees paying themselves excessive salary to convert nondeductible dividends into deductible wages.

The IRS may **recharacterize "excessive" compensation as a constructive dividend**, disallowing the corporation's deduction (creating taxable income at 21%) and treating it as a dividend to the shareholder (taxed again at qualified dividend rates of 0/15/20% plus 3.8% NIIT). The classic case law factors (Mayson Mfg., Charles Schneider, Exacto Spring, Menard) examine:

- Role and responsibility.
- Time and effort.
- Comparison with industry comp data.
- Internal pay consistency.
- Whether unrelated executives would accept the same comp.
- The "independent investor test" — would a hypothetical outside investor accept the salary level given the return on equity? (Exacto Spring, 7th Cir. 1999.)

For closely-held C-corps with material owner-employee comp, flag this for reviewer if comp exceeds industry norms.

### 15.2 §162(m) $1M deduction cap

For **publicly held corporations**, IRC §162(m) caps the deduction for compensation paid to **covered employees** (CEO, CFO, top 3 highest-paid, plus anyone who was a covered employee in a prior year post-2017) at **$1 million per individual per year**. The cap applies whether comp is base salary, bonus, equity, or any other form (TCJA repealed the performance-based-comp exception). For private companies, no §162(m) cap applies. ARPA expanded covered employees to include the next 5 highest-paid effective 2027.

### 15.3 §280G golden parachute

For change-in-control payments, §280G may disallow the deduction for "excess parachute payments" and impose a 20% excise tax on the recipient (§4999). Out of scope for routine prep; flag any M&A-year return for reviewer.

---

## 16. Late filing and late payment penalties

### 16.1 §6651(a)(1) Late filing

If Form 1120 is filed after the original due date (or extended due date, if Form 7004 was timely filed), penalty is:
- **5% of unpaid tax per month or fraction thereof**, capped at **25%** of unpaid tax.
- If more than 60 days late, the minimum penalty is the **lesser of $485 (2025 inflation-adjusted amount; verify against the current Rev. Proc.) or 100% of unpaid tax**. For 2025, the §6651(a) minimum is in the $485 range; check the most recent Rev. Proc. for the exact figure.

If no tax is due (refund or zero balance), the late filing penalty is $0 — there's nothing to multiply 5% against.

### 16.2 §6651(a)(2) Late payment

If tax is unpaid after the original due date (even with a valid extension to file), penalty is:
- **0.5% of unpaid tax per month**, capped at 25%.
- Reduced to 0.25%/month while an installment agreement is in effect.

### 16.3 Combined cap

When both §6651(a)(1) and §6651(a)(2) apply in the same month, the late-filing penalty is reduced by the late-payment penalty for that month, so the combined monthly rate is 5% (not 5.5%). Total combined cap = 47.5% (25% LF − 25% × 0.5% × 5 months reduction + 25% LP). In practice, the §6651(a)(1) penalty is 4.5%/month after the §6651(a)(2) offset.

### 16.4 §6651(c)(1) reasonable cause

Penalty abated for reasonable cause (e.g., reliance on professional advice, natural disaster, death of preparer or officer). Document the facts contemporaneously; the IRS applies §6651(c)(1) restrictively.

### 16.5 §6601 Interest

Interest on unpaid tax accrues from the original due date at the applicable federal underpayment rate (announced quarterly by the IRS). For Q1 2026, the corporate underpayment rate for amounts up to $100k is generally 1 percentage point above the short-term AFR; for large corporate underpayments above $100k, the rate is 5 percentage points above (the "hot interest" under §6621(c)). Verify against the current quarterly rate notice.

### 16.6 §6699 — N/A for C-corps

Note: §6699 (per-shareholder per-month late filing penalty for S-corps and partnerships) does **not** apply to C-corps. The C-corp penalty is tax-based under §6651, not headcount-based.

---

## 17. E-file mandate

Under **Reg. §301.6011-5** (as amended by T.D. 9972, effective for filings due in 2024 and later), **electronic filing is mandatory** for any corporation that:

1. Has **total assets of $10 million or more** at year-end, OR
2. Files **10 or more returns of any kind** during the calendar year (aggregating Forms W-2, 1099, 1042-S, 5471, 5472, etc.).

This is a substantial expansion of the prior rules and now captures most small and mid-size corps that issue payroll W-2s and 1099s.

Paper filing remains permitted for corporations under both thresholds — primarily very small inactive or holding companies. Even then, e-filing is recommended; it reduces processing time and avoids transcription errors.

E-file is via **IRS Modernized e-File (MeF)** through an authorized e-file provider (Drake, Lacerte, ProConnect, UltraTax, CCH Axcess, etc.) or direct via the IRS-provided software for very small filers.

### 17.1 Signature

For e-filed returns, the corporate officer (typically the CFO, CEO, treasurer, or other person authorized to sign Form 1120) signs **Form 8879-CORP, IRS e-file Signature Authorization for Form 1120**, which authorizes the ERO (electronic return originator) to submit the return with a PIN. The original signed 8879-CORP must be retained by the ERO and made available on IRS request; it is not filed with the return.

---

## 18. LLC electing C-corp first-year considerations

### 18.1 Form 8832 effective date

An LLC that elects C-corp treatment files **Form 8832 (Entity Classification Election)** and specifies an effective date (up to 75 days back, up to 12 months forward, from filing). The first 1120 covers the period beginning on the effective date.

**If the LLC was previously a disregarded entity (single member),** the conversion is a **deemed §351 transfer** — the member is deemed to contribute the LLC's assets and liabilities to a newly-formed corporation in exchange for stock. Recognize:
- Built-in gain on the contributed assets (rare unless boot or excess liabilities).
- Carryover basis for the C-corp under §362.
- Holding period tacks under §1223.
- Pre-conversion losses of the disregarded entity (which were Schedule C) do NOT carry into the C-corp (they were the owner's losses, not the entity's).

**If the LLC was previously a partnership (multi-member),** the conversion is a deemed contribution by each partner of their partnership interest to the corporation under §351, or alternatively can be structured as a deemed asset contribution. The form of the deemed transaction matters for basis and gain — see Rev. Rul. 84-111 for the three permissible forms of partnership-to-corp conversion.

### 18.2 Short year

If Form 8832 is effective mid-year, the C-corp files a **short-year 1120** for the period from effective date to year-end. The first-year due date is the 15th day of the 4th month after that short year-end.

### 18.3 New EIN?

The LLC retains its existing EIN — no new EIN is needed solely because of the entity classification election (per IRS practice and the EIN instructions, Form SS-4).

### 18.4 Five-year rule on revocation

Once a Form 8832 election is made, the entity generally cannot change classification again for **60 months** (5 years) — IRC §7701 default rules and Reg. §301.7701-3(c)(1)(iv). Limited exceptions exist for ownership changes exceeding 50%.

### 18.5 Disclosure

The first 1120 should include a statement noting the election, attaching a copy of Form 8832, and noting the effective date.

---

## 19. Worked examples

### 19.1 Example A — Simple domestic C-corp

**Facts:**
- "Acme Widgets, Inc.", a Delaware C-corp, calendar year, single-state operations (Delaware only).
- 2025 sales: $4,200,000.
- COGS: $2,300,000.
- Officer compensation: $400,000 (one shareholder-CEO).
- Salaries: $800,000.
- Rent: $120,000.
- Depreciation: $90,000 (Form 4562).
- Other operating expenses: $180,000.
- State income tax expense: $35,000.
- Federal income tax expense (book): $130,000.
- Interest income: $5,000.
- Charitable contributions: $30,000.
- No dividends received, no foreign operations.
- Total assets at year-end: $1.2 million.
- Estimated taxes paid: $130,000.

**Form 1120 income:**

| Line | Description | Amount |
|------|-------------|--------|
| 1a | Gross receipts | $4,200,000 |
| 2 | COGS (Form 1125-A) | $2,300,000 |
| 3 | Gross profit | $1,900,000 |
| 5 | Interest | $5,000 |
| 11 | Total income | $1,905,000 |

**Deductions:**

| Line | Description | Amount |
|------|-------------|--------|
| 12 | Officer comp (Form 1125-E, receipts ≥ $500k) | $400,000 |
| 13 | Other salaries | $800,000 |
| 16 | Rent | $120,000 |
| 17 | State income tax | $35,000 |
| 19 | Charitable (≤ 10% of TI before contribution) | $30,000* |
| 20 | Depreciation | $90,000 |
| 26 | Other | $180,000 |
| 27 | Total deductions | $1,655,000 |
| 28 | TI before NOL/special deductions | $250,000 |

*Check 10% charitable limit: TI before contribution = $250,000 + $30,000 = $280,000. 10% = $28,000. **The $30,000 contribution exceeds the limit by $2,000.** Allowable in 2025: $28,000. Carry $2,000 to 2026 (5-year carryforward). Restate Line 19 to $28,000 and Line 28 to $252,000.

| Line | Description | Amount |
|------|-------------|--------|
| 28 | TI (corrected) | $252,000 |
| 29a | NOL deduction | $0 |
| 29b | Special deductions (DRD/§250) | $0 |
| 30 | Taxable income | $252,000 |
| 31 | Tax (Schedule J) = 21% × $252,000 | **$52,920** |

**Estimated tax safe harbor analysis:**
- Prior-year tax (2024): assume $115,000.
- Current-year tax (2025): $52,920.
- Required annual payment = lesser of 100% × $115,000 = $115,000 OR 100% × $52,920 = $52,920 → $52,920 (this is the lesser).
- Acme is NOT a large corp (taxable income never $1M+ in prior 3 years, presumably).
- Quarterly installments: $52,920 / 4 = $13,230 each.
- Estimated taxes paid: $130,000. Massive overpayment.
- Refund or credit forward = $130,000 − $52,920 = $77,080.

**Schedule M-1:**

| Line | Item | Amount |
|------|------|--------|
| 1 | Net income per books | (Compute backward) |
| 2 | Federal income tax expense per books | $130,000 |
| 5 | Expenses on books not deducted: $2k charitable carryforward + meals 50% etc. | $2,000 |
| 8 | Tax depreciation in excess of book | (Assume 0 for simplicity) |
| 10 | TI per Form 1120 Line 28 | $252,000 |

If book NI = $120,000, M-1 reconciles: $120,000 + $130,000 + $2,000 = $252,000. ✓

**Schedules required:**
- Schedule B: yes.
- Schedule C: no (no dividends).
- Schedule J: yes (every return).
- Schedule K: yes.
- Schedule L: yes (assets ≥ $250k).
- Schedule M-1: yes (assets under $10M so M-3 not required).
- Schedule O: no (not in controlled group).
- Schedule UTP: no (under $10M).
- Form 1125-A: yes (COGS).
- Form 1125-E: yes (receipts ≥ $500k).
- Form 4562: yes (depreciation).

**Filing:**
- Due April 15, 2026. E-file (over 10 W-2s/1099s issued).

### 19.2 Example B — Multinational with GILTI and FDII

**Facts:**
- "GlobalTech Inc.", a Delaware C-corp, calendar year.
- 100% owner of a wholly-owned Irish CFC, "GlobalTech Ireland Ltd."
- 2025 US revenue: $80M (of which $30M is FDDEI — Foreign-Derived Deduction-Eligible Income, sales to foreign customers).
- 2025 GlobalTech Inc. taxable income before §250 deduction = $20,000,000.
- GlobalTech Ireland Ltd. tested income = $5,000,000 (passes through as a GILTI inclusion).
- QBAI return on Ireland tangible assets = $800,000.
- Foreign tax credits available for GILTI (after 80% haircut and §904 sourcing) — assume usable to reduce GILTI tax.

**GILTI inclusion (computed on Form 5471 Schedule I-1, summarized):**
- Tested income: $5,000,000
- Less: 10% × QBAI return × QBAI ($8M, so 10% × $8M = $800k, but assume this is already netted in tested income terms — net GILTI = $5,000,000 − $800,000 = $4,200,000.
- GILTI inclusion on Schedule C Line 14 = $4,200,000.

**§250 deduction (Form 8993):**

GILTI portion:
- GILTI included = $4,200,000.
- §250 deduction on GILTI = 50% × $4,200,000 = $2,100,000.
- §78 gross-up for foreign taxes paid by CFC ≅ assume $500,000 → additional Schedule C line 16 inclusion (also eligible for §250).

FDII portion:
- Deduction-eligible income = ... (computed under §250(b) regulations) — assume FDII = $4,000,000 after the allocation steps.
- §250 deduction on FDII = 37.5% × $4,000,000 = $1,500,000.

Total §250 deduction = $2,100,000 + $1,500,000 = $3,600,000.

**§250(a)(2) limitation:** Aggregate §250 deduction limited to taxable income before §250.
- Taxable income before §250 = $20,000,000 (assumed; this already includes the GILTI inclusion).
- $3,600,000 ≤ $20,000,000 → no proration needed.

**Form 1120 Lines:**
- Line 28 TI before NOL and special deductions = $20,000,000.
- Line 29b Special deductions (§250 from Schedule C Line 22) = $3,600,000.
- Line 30 TI = $16,400,000.
- Line 31 Tax (Schedule J) = 21% × $16,400,000 = $3,444,000.

**Foreign tax credit:**
Reduces the line 31 tax via Schedule J, computed on Form 1118. (Refer to FTC skill.)

**Schedules required:**
- Plus Forms 5471 (Ireland), 8993, 1118 (FTC), Schedule UTP if applicable (assets ≥ $10M likely).
- Schedule M-3 likely required (assets ≥ $10M).

**Comment on 2026 rate change:**
For tax years beginning in 2026, OBBBA sets new permanent §250 deduction rates of **40% on GILTI (renamed "net CFC tested income") and 33.34% on FDII** (see §11.2) — higher than the old scheduled sunset rates of 37.5% / 21.875%. If GlobalTech's GILTI inclusion were the same in 2026, the §250 deduction on GILTI alone would drop from $2.1M (50% × $4.2M) to $1.68M (40% × $4.2M), increasing 2026 tax by roughly $88,200 (= $420,000 × 21%). Flag for tax planning.

### 19.3 Example C — CAMT-triggered large corp

**Facts:**
- "MegaCorp, Inc.", a Delaware C-corp, calendar year.
- 3-year average AFSI (2022, 2023, 2024): $1.2 billion → **MegaCorp is an applicable corporation** under §59(k).
- 2025 AFSI before FSNOL = $1,100,000,000.
- 2025 FSNOL available = $200,000,000 (limited to 80% × $1.1B = $880M, so all $200M usable).
- 2025 regular taxable income (Form 1120 Line 30) = $300,000,000 (heavily reduced by §168(k), §174 amortization, FDII deduction).
- Regular tax (Schedule J Line 2) = 21% × $300,000,000 = $63,000,000.
- BEAT: assume $0 for simplicity.

**CAMT computation (Form 4626):**
- AFSI after FSNOL = $1,100,000,000 − $200,000,000 = $900,000,000.
- TMT = 15% × $900,000,000 = $135,000,000.
- Regular tax (+ BEAT) = $63,000,000.
- **CAMT = max(0, $135,000,000 − $63,000,000) = $72,000,000.**

**Total tax (Schedule J Line 11):**
- Regular tax: $63,000,000
- + CAMT: $72,000,000
- = **Total: $135,000,000**

Effective rate = $135M / $300M = 45% on regular taxable income, but actually 15% on AFSI, which is the policy outcome of CAMT.

**CAMT credit carryforward:**
- The $72M CAMT generates a §53 CAMT credit of $72M carried forward indefinitely, usable in years when regular tax exceeds TMT.

**Schedules required:**
- All of Schedule J including CAMT lines.
- Form 4626.
- Schedule UTP (assets ≥ $10M almost certainly).
- Schedule M-3 (assets ≥ $10M).
- Likely Forms 5471, 5472, 8990, 8991/8993, 8975 (CbC) — refer out for each.
- E-file mandatory (large corp).

**Estimated tax:**
- MegaCorp is a large corporation (TI well over $1M in each prior year).
- No prior-year safe harbor allowed for installments 2–4. Must use 100% of current-year tax.
- Quarterly installments = $135M / 4 = $33,750,000 each.
- Failure to fully fund triggers §6655 penalty on Form 2220.

---

## 20. §1202 Qualified Small Business Stock (QSBS) — OBBBA phased exclusion

QSBS status is a **C-corp-level attribute**: the exclusion is claimed by the shareholder on sale, but only if the issuing corporation was a **qualified small business (QSB)** C-corporation when the stock was issued and throughout the holding period. OBBBA (§70431) liberalized §1202 for **stock issued after July 4, 2025**:

- **Phased gain exclusion** (replacing the old flat 5-year / 100% rule for newly issued stock):
  - **50%** exclusion if held **at least 3 years**,
  - **75%** exclusion if held **at least 4 years**,
  - **100%** exclusion if held **at least 5 years**.
- **Per-issuer cap raised to $15 million** (from $10 million) of eligible gain.
- **Aggregate gross asset test raised to $75 million** (from $50 million) — a corporation may now be a QSB with up to $75M of aggregate gross assets at issuance.

For a C-corp that may issue stock to founders or investors, confirm QSB eligibility at issuance (the $75M gross-asset test, active-business requirement, and the excluded lines of business) and document it contemporaneously, because the shareholder exclusion depends on the corporation's facts.

Source: OBBBA §70431; IRC §1202(a).

---

## 21. Provenance and disclaimer

### 21.1 Statutory citations relied on

- IRC §11 (corporate rate, 21%)
- IRC §55(b)(2), §59(k), §56A (CAMT, IRA 2022)
- IRC §163(j) (interest limitation; EBITDA add-back restored by OBBBA §70303)
- IRC §172 (NOL, post-TCJA rules)
- IRC §174A (domestic R&D immediate expensing, foreign R&D 15-year amortization; OBBBA §70302)
- IRC §179(b) (§179 limit $2.5M / phase-out $4M; OBBBA §70306)
- IRC §243, §245, §245A, §246, §246A (DRD)
- IRC §250 (GILTI/FDII deduction; OBBBA §70321 permanent 40%/33.34% rates and §70322 DEI restriction)
- IRC §960(d)(4) (10% FTC haircut on §951A-related PTEP distributions; OBBBA §70312(b))
- IRC §1202(a) (QSBS phased exclusion 50/75/100%, $15M cap, $75M gross-asset test; OBBBA §70431)
- IRC §382 (NOL after ownership change)
- IRC §448(c) (small-business threshold $31M for 2025)
- IRC §6012(a)(2) (filing requirement)
- IRC §6651 (late filing/payment penalty)
- IRC §6655 (corporate estimated tax)
- IRC §6072(b) (due date)
- IRC §7503 (weekend/holiday)
- Reg. §301.6011-5 (e-file mandate)
- Reg. §1.6012-2 (filing requirement)
- Reg. §1.250(b)-1 through -6 (FDII)
- Reg. §1.951A (GILTI)
- Reg. §1.6011-4 (Schedule M-3 threshold)

### 21.2 Legislative provenance

- **Tax Cuts and Jobs Act (TCJA), P.L. 115-97 (December 22, 2017)** — 21% rate, §163(j), §174 capitalization (delayed effective date), DRD reduction, NOL 80%/no-carryback, §250 enactment, FDII/GILTI.
- **Inflation Reduction Act (IRA), P.L. 117-169 (August 16, 2022)** — CAMT under §55(b)(2) and §59(k), stock buyback excise tax under §4501.
- **One Big Beautiful Bill Act (OBBBA), P.L. 119-21 (July 4, 2025)** — did NOT modify the corporate 21% rate, the CAMT, or the DRD. It DID: restore immediate expensing of **domestic** R&D via new **§174A** (§70302, tax years beginning after Dec 31, 2024, foreign R&D still 15-year); permanently **restore the §163(j) EBITDA add-back** (§70303, after Dec 31, 2024); set **new permanent §250 rates** of 40% GILTI ("net CFC tested income") / 33.34% FDII (§70321, after Dec 31, 2025) and **narrow the FDII/DEI base** (§70322, dispositions after June 16, 2025); impose a **10% FTC haircut on §951A-related PTEP distributions** (§70312(b)/§960(d)(4), after June 28, 2025); raise **§179** to $2.5M / $4M (§70306, after Dec 31, 2024); and enact the **§1202 QSBS** phased 50/75/100% exclusion with a $15M per-issuer cap and $75M gross-asset test (§70431, stock issued after July 4, 2025).

### 21.3 IRS guidance

- Form 1120 Instructions for 2024 (used as template for 2025 — verify against released 2025 instructions before filing).
- Form 4626 Instructions (2023 revision for IRA CAMT).
- Form 8993 Instructions.
- Form 8990 Instructions.
- Rev. Proc. 2024-40 (inflation adjustments for 2025; $485 minimum late filing penalty figure subject to confirmation against current Rev. Proc.).
- Rev. Proc. 2023-8, Rev. Proc. 2023-11 (§174 SRE method change).
- Notice 2023-7 and subsequent CAMT notices (Notice 2023-20, 2023-64, 2024-10, 2024-66, 2025 updates).
- REG-112129-23 (CAMT proposed regs, September 2024).

### 21.4 Disclaimer

This skill provides a structured walkthrough for preparing Form 1120 for tax year 2025 under federal law. It is intended for use by a Circular 230 practitioner (CPA, EA, or attorney) and must be reviewed and signed by such a practitioner before the return is filed. The skill does not constitute tax advice to any specific taxpayer.

**Specific verification required before filing any return:**

1. Confirm the 2025 Form 1120 and instructions as released by the IRS in late 2025 / early 2026 (changes from the 2024 form possible).
2. Confirm the 2025 Rev. Proc. inflation adjustments (small-business threshold, §6651 minimum penalty, §6655 large-corp threshold).
3. Apply the OBBBA changes now in law: §174A domestic R&D immediate expensing, the restored §163(j) EBITDA add-back, the new permanent §250 rates (40%/33.34% from 2026) and DEI narrowing, the §960(d)(4) FTC haircut on §951A-related PTEP, §179 at $2.5M/$4M, and the §1202 QSBS phased exclusion. Confirm no further late-2025 or 2026 legislation altered these or the CAMT thresholds.
4. Confirm the corporation's state filings — this skill addresses federal only.
5. For any item flagged "refer out" (consolidated returns, foreign subsidiaries, BEAT, R&D, FTC, CAMT mechanics, stock buyback excise), engage the specialized skill or specialist.

**State tax warning:** Federal taxable income is the starting point for most state corporate income tax computations, but virtually every state adjusts away from federal in specific areas (state-specific decoupling from bonus depreciation, §163(j), §168(k), §250, §174). Always run the state return alongside the federal, not after.

**End of skill.**

---

<!-- openaccountants-cta-block -->

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is
different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your
jurisdiction — **no liability on either side until you and the accountant sign
a formal engagement letter** — book a free 30-minute call:

**→ [Book a call](https://calendly.com/openaccountants-info/30min)**

We'll route you to the named verifier covering your country or state. You can
also see the full list of verified accountants at
[openaccountants.com/network](https://www.openaccountants.com/network).

<!-- openaccountants-mcp-cta -->

## The accountant-verified version lives in the connector

This file is the open, **research-grade draft**. The **accountant-verified**
version of this skill is **not published to GitHub** — it is delivered free
through the OpenAccountants MCP connector, where your AI agent loads the
verified rules together with the name of the accountant who signed them off.

**→ Install the free connector:** <https://www.openaccountants.com/connect>
**MCP endpoint:** `https://www.openaccountants.com/api/mcp`

---

## Changelog

- **2026-07-04** — OBBBA corrections applied from a review by Christopher Aryee, CPA: §174A domestic R&D immediate expensing, §163(j) EBITDA add-back, GILTI/FDII permanent rates, §250 DEI restriction, §960 FTC-on-PTEP haircut, §179 $2.5M/$4M, §1202 phased exclusion.
