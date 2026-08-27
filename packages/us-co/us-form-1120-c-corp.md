---
name: us-form-1120-c-corp
description: Tier 2 US federal content skill for preparing Form 1120 — the US C-corporation income tax return. Covers tax year 2025 under OBBBA including the 21% flat rate, DRD tiers (50/65/100%), §163(j) interest limit, §174 R&D capitalization, §250 GILTI/FDII deduction at 50%/37.5%, the 15% Corporate AMT on AFSI > $1B (IRA 2022), required schedules (B, C, J, K, L, M-1/M-3, O, UTP), and common attached forms (4562, 4626, 5471/5472 refer-out, 6765, 8993, 1125-A, 1125-E). Filing due 15th day of 4th month; Form 7004 6-month extension; quarterly estimated 25/25/25/25 with no 110% safe harbor for corps.
jurisdiction: US
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: Christopher Aryee
review_status: current
tier: 1
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# US Form 1120 C Corp

## US Form 1120 — C-Corporation Income Tax Return (Tax Year 2025)

> Tier 2 federal content skill. MUST be loaded alongside `us-tax-workflow-base` v0.2 or later. Federal only — state corporate income tax is out of scope; route to the relevant state skill when needed.

## 1. Scope

This skill covers the preparation of **Form 1120, U.S. Corporation Income Tax Return**, for tax year 2025 for a domestic C-corporation operating in the United States. It walks through the income computation, the tax computation on Schedule J, the required schedules (B, C, J, K, L, M-1/M-3, O, UTP where applicable), the most common attached forms, and the corporate-specific provisions that differ from individual taxation (DRD, NOL post-TCJA, §163(j), §174 capitalization, §250 GILTI/FDII deduction, and the 15% Corporate Alternative Minimum Tax).

**In scope:**
- Calendar-year and fiscal-year domestic C-corporations chartered in any US state or DC
- LLCs that have elected C-corp treatment via Form 8832
- Single-entity returns (no consolidated returns — see §1.1)
- The 21% flat federal rate computation under IRC §11
- Schedule C dividends-received deduction (DRD)
- Net operating loss (NOL) treatment under the post-TCJA regime (80% limitation, indefinite carryforward, no carryback)
- §163(j) business interest expense limitation
- §174 specified research and experimental (SRE) capitalization
- §250 GILTI/FDII deduction (at the post-TCJA, pre-sunset 2025 rates of 50% / 37.5%)
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

- **Consolidated returns out of scope** — If the corporation is part of an affiliated group filing a consolidated return under IRC §1501 and Reg. §1.1502, this skill does not apply. The consolidated return introduces SRLY (separate return limitation year) rules for NOLs, intercompany transaction deferrals under Reg. §1.1502-13, excess loss accounts, investment-basis adjustments, the consolidated §163(j) computation, the consolidated CAMT computation, and Forms 851 and 1122. These are out of scope here. If the corporation has an 80%-or-more parent or 80%-or-more subsidiaries, ask the client whether a consolidated election (Form 1122) is in effect. If yes, refer out. If no, the entities file separate 1120s and this skill applies to each.  _(IRC §1501, Reg. §1.1502, Reg. §1.1502-13)_

## 2. Who must file

- **Filing requirement for domestic corporations** — Under IRC §6012(a)(2) and Reg. §1.6012-2(a), every domestic corporation in existence during any portion of the taxable year must file Form 1120, regardless of whether it had taxable income or any activity, unless it falls under one of the special categories listed in §1 above (S-corp, REIT, RIC, exempt org, etc.). This includes: 1. Corporations chartered as such under state law (Inc., Corp., Co., Ltd.) that have not made an S election. 2. LLCs that have affirmatively elected C-corporation treatment by filing Form 8832 (Entity Classification Election). The election is effective on the date specified on Form 8832 (which can be up to 75 days before or 12 months after the filing date). From that effective date forward, the LLC files Form 1120, not Schedule C, Form 1065, or Form 1120-S. 3. Foreign-incorporated entities that have elected to be treated as a US corporation via Form 8832 (rare but possible for certain hybrid structures). 4. Inactive corporations — even a corporation with no income and no activity must file if it remains in existence under state law. The only way out of the filing requirement is formal dissolution under state law (a final return is then required, with the "Final return" box at the top of Form 1120 checked). 5. First-year and short-year corporations — a corporation formed mid-year files a short-year 1120 from the date of incorporation through its first chosen year-end. The first return also must include any Form 1128 (change of accounting period) and any §351 transferor disclosures.  _(IRC §6012(a)(2), Reg. §1.6012-2(a))_

### 2.1 Tax year selection

- **Tax year options for C-corporations** — A C-corporation may adopt a calendar year (January 1 – December 31) or any fiscal year ending on the last day of a month other than December, except: Personal Service Corporations (PSCs) are generally required to use a calendar year under IRC §441(i) unless they make a §444 election (with required-payment offset on Form 8716 and Form 8752). PSCs are out of scope here — flag for reviewer. A 52/53-week year is permitted under IRC §441(f). The tax year is established by the timing of the first return; changes require Form 1128 and IRS consent (Rev. Proc. 2006-45 automatic procedures for most domestic corps).  _(IRC §441(i), IRC §441(f), Rev. Proc. 2006-45)_

## 3. Rate

### 3.1 The 21% flat rate

- **C-corporation flat federal income tax rate (tax years beginning after Dec 31, 2017, including 2025)** — 21%  _(IRC §11(b); Tax Cuts and Jobs Act of 2017 (P.L. 115-97))_
- **2025 confirmation of 21% rate** — Confirmed for 2025: The 21% rate continues to apply for tax years beginning in calendar year 2025. The One Big Beautiful Bill Act (P.L. 119-21, July 4 2025) did not change the corporate rate. Some legislative proposals during 2024-2025 had floated rate changes (a 15% rate for domestic manufacturers, a 28% rate generally), but none were enacted. For any return with a tax year beginning in 2025, use 21%. It replaced the prior graduated corporate rate schedule (15%, 25%, 34%, 39%, 34%, 35%, 38%, 35%) and the personal service corporation flat 35% rate.  _(P.L. 119-21 (OBBBA, July 4 2025); P.L. 115-97 (TCJA))_

### 3.2 Computation

- **Corporate tax computation** — Tax = Taxable income (line 30 of Form 1120) × 21%, computed on Schedule J, Part I, line 2. There is no "small corporation" rate, no graduated bracket, and no first-dollar exclusion. Even a corporation with $1,000 of taxable income pays $210 of federal income tax.  _(Schedule J, Part I, line 2)_

### 3.3 Effect on planning

Because the rate is flat, the long-standing income-shifting strategies (paying bonuses to bring taxable income down to a lower bracket; timing income to land in the 15% bracket) no longer have any first-order effect. The remaining levers are:
- Defer recognition into a year when an NOL exists (post-TCJA NOLs are still subject to the 80% limit, so this is partial).
- Accelerate deductions to reduce taxable income year-on-year (still beneficial because of the time value of money and the §163(j) ATI floor).
- Choose between deductible compensation and dividend distribution (deductible compensation is still preferred at the entity level — dividends are not deductible and create double taxation).

## 4. Due dates and extension

### 4.1 Original due date

- **General due date rule** — Under IRC §6072(b) (as amended by the Surface Transportation and Veterans Health Care Choice Improvement Act of 2015, P.L. 114-41), Form 1120 is due on or before the 15th day of the 4th month following the close of the tax year.  _(IRC §6072(b); P.L. 114-41)_

**Original due date table by tax year-end**  _(IRC §6072(b))_

| Tax year-end | Due date |
| --- | --- |
| December 31, 2025 (calendar year) | **April 15, 2026** |
| January 31, 2026 (fiscal) | May 15, 2026 |
| June 30, 2026 (fiscal) | October 15, 2026 |

- **Special rule for fiscal years ending June 30** — For tax years beginning before January 1, 2026, a fiscal-year C-corporation with a June 30 year-end has historically used a September 15 due date (15th day of 3rd month). This special rule for June 30 year-ends was scheduled to phase in to the new 4th-month rule for years beginning after December 31, 2025. A June 30, 2026 year-end (i.e., tax year beginning July 1, 2025) is the first year for which the new October 15 due date applies. Confirm against current IRS instructions for the year of filing.  _(IRC §6072(b))_
- **Weekend/holiday rule** — If the due date falls on a Saturday, Sunday, or legal holiday, the return is timely if filed on the next business day.  _(IRC §7503)_

### 4.2 Extension — Form 7004

- **Automatic 6-month extension** — A corporation may obtain an automatic 6-month extension to file Form 1120 by filing Form 7004 (Application for Automatic Extension of Time To File Certain Business Income Tax, Information, and Other Returns) on or before the original due date.  _(Form 7004)_

**Extended due date table**  _(Form 7004)_

| Tax year-end | Original due | Extended due |
| --- | --- | --- |
| December 31, 2025 | April 15, 2026 | **October 15, 2026** |
| June 30, 2026 | October 15, 2026 | **April 15, 2027** |

- **Extension extends filing time only, not payment time** — Critical caveat: Form 7004 extends the time to FILE, not the time to PAY. The corporation must pay the full estimated balance due by the original due date to avoid the §6651(a)(2) late-payment penalty (0.5% per month, max 25%) and §6601 interest. If Form 7004 is filed but no payment is made and a balance is owed, the extension is still valid for filing-penalty purposes, but late-payment penalty and interest accrue from the original due date. Form 7004 requires: Estimated total tax liability for the year (Line 6); Total payments and credits already made (Line 7); Balance due to be paid with the extension (Line 8). The IRS does not require a reason; the extension is automatic if Form 7004 is properly completed and filed timely.  _(IRC §6651(a)(2); IRC §6601)_

## 5. Estimated tax — IRC §6655 (no 110% safe harbor for corps)

### 5.1 Who must pay

- **Minimum expected tax liability requiring estimated payments** — $500 or more USD  _(IRC §6655(a) and (f))_
- **Estimated payment requirement** — A corporation that expects its tax liability to be $500 or more for the year must pay estimated tax in four equal installments. Below $500, no estimated payments are required and no penalty applies.  _(IRC §6655(a) and (f))_

### 5.2 Installment due dates

**Calendar-year installment due dates**

| Installment | Calendar-year due date |
| --- | --- |
| 1st (April installment) | **April 15, 2025** |
| 2nd (June installment) | **June 16, 2025** (the 15th is a Sunday) |
| 3rd (September installment) | **September 15, 2025** |
| 4th (December installment) | **December 15, 2025** |

- **Fiscal-year installment timing and installment percentage** — For fiscal-year corporations, the installments are due on the 15th day of the 4th, 6th, 9th, and 12th months of the tax year. Each installment is generally 25% of the required annual payment.

### 5.3 Required annual payment — the safe harbors

- **Required annual payment definition** — Under IRC §6655(d)(1), the required annual payment is the lesser of: (a) 100% of the tax shown on the current-year return, OR (b) 100% of the tax shown on the preceding year's return, provided that: The preceding year was a 12-month tax year, AND The corporation filed a return for the preceding year showing a liability, AND The corporation is not a "large corporation."  _(IRC §6655(d)(1))_
- **Large corporation** — A corporation with taxable income of $1 million or more in any of the three preceding tax years (whether or not consecutive). For large corporations, the prior-year safe harbor is disallowed for the 2nd, 3rd, and 4th installments — the entire year must be funded based on current-year tax. (The first installment may use the prior-year safe harbor; any shortfall must be made up by the second installment.)  _(IRC §6655(g)(2); IRC §6655(d)(2)(B))_
- **Corporate vs individual safe harbor contrast** — Key contrast with individual taxation: Individuals have a 110% prior-year safe harbor when AGI exceeds $150,000. Corporations do not. The corporate prior-year safe harbor is always 100% (not 110%), and it is unavailable at all to large corporations after the first installment. Do not confuse the two regimes.  _(IRC §6655)_

### 5.4 Annualized income installment method

- **Annualized income installment method availability** — A corporation with uneven income may use the annualized income installment method under §6655(e)(2) to reduce installments in lighter quarters.  _(IRC §6655(e)(2))_

**Annualization periods and factors for calendar-year corp**  _(IRC §6655(e)(2))_

| Installment | Months annualized | Annualization factor |
| --- | --- | --- |
| 1st | First 3 months | 4 |
| 2nd | First 3 months | 4 |
| 3rd | First 6 months | 2 |
| 4th | First 9 months | 1.33333 |

- **Alternative seasonal annualization option** — The IRS provides an alternative option of 2/4/7/10 months under §6655(e)(2)(C) if elected on Form 8842 — this is the "adjusted seasonal" or "seasonal" option for businesses with predictable seasonal patterns. This is computed on Schedule A of Form 2220 and attached to Form 1120 if an underpayment penalty is computed.  _(IRC §6655(e)(2)(C); Form 8842; Form 2220 Schedule A)_

### 5.5 Form 2220 — underpayment penalty

- **Form 2220 required attachment** — If installments are missed or underpaid, the corporation computes the §6655 underpayment penalty on Form 2220, Underpayment of Estimated Tax by Corporations, and attaches it to Form 1120. Unlike individuals (who can let the IRS bill them), the IRS instructions direct that corporations must compute and attach Form 2220 if the penalty applies — failing to attach can trigger a follow-up notice.  _(IRC §6655; Form 2220)_

### 5.6 Payment mechanics

- **Electronic payment requirement** — Corporate estimated tax payments must be made by electronic funds transfer (EFT) through the Electronic Federal Tax Payment System (EFTPS). Paper checks are not permitted for corporate deposits per Reg. §31.6302-1. The Form 1120-W worksheet, while no longer filed, is used internally to compute installments.  _(Reg. §31.6302-1)_

## 6. Income computation walkthrough

Form 1120 income flows in this order: gross income → total income (line 11) → deductions (lines 12–29) → taxable income before NOL/special deductions (line 28) → less NOL deduction and special deductions (lines 29a and 29b) → taxable income (line 30) → tax (line 31).

### 6.1 Gross income (lines 1–11)

- **Line 1a Gross receipts or sales** — Total revenue from the sale of goods or services before any returns, allowances, or discounts.
- **Line 1b Returns and allowances** — Sales returns, allowances, and discounts. Note: cash discounts to customers may be netted here or treated as a deduction; be consistent year-over-year.
- **Line 1c Net** — 1c = 1a − 1b
- **Line 2 Cost of goods sold** — From Form 1125-A (mandatory if there is COGS). See §11.4.  _(Form 1125-A)_
- **Line 3 Gross profit** — Line 3 = Line 1c − Line 2
- **Line 4 Dividends and inclusions** — From Schedule C, Line 23, Column (a). Gross dividend income, before the DRD (the DRD is taken later as a special deduction on Line 29b).  _(Schedule C, Line 23, Column (a))_
- **Line 5 Interest** — Taxable interest from bank deposits, taxable bonds, etc. Tax-exempt interest is reported on Schedule K, Line 9, not Line 5.
- **Line 6 Gross rents** — Line 6 Gross rents.
- **Line 7 Gross royalties** — Line 7 Gross royalties.
- **Line 8 Capital gain net income** — From Schedule D (Form 1120). Net of long-term and short-term gains and losses. Corporate capital losses are deductible only against capital gains (not ordinary income); excess losses carry back 3 years and forward 5 years (IRC §1212(a)) — this differs from the individual rule.  _(Schedule D (Form 1120); IRC §1212(a))_
- **Line 9 Net gain or (loss) from Form 4797** — Part II — §1231 gains and ordinary recapture (§1245, §1250). Net §1231 gain is treated as long-term capital gain and flows to Schedule D; a net §1231 loss is ordinary and flows to Line 9.  _(Form 4797; IRC §1245; IRC §1250)_
- **Line 10 Other income** — Recovery of bad debts, federal tax refund of taxes previously deducted, life insurance proceeds where deducted, gross income from §481(a) adjustments, etc. Attach a statement detailing the components.  _(IRC §481(a))_
- **Line 11 Total income** — Line 11 Total income.

### 6.2 Deductions (lines 12–29)

**Deductions table lines 12–31**

| Line | Item | Notes |
| --- | --- | --- |
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
| 26 | Other deductions | Attach statement. Common items: insurance, utilities, professional fees, office expense, travel and meals (50% limit per §274(n)), software subscriptions, bank fees, R&E expenses subject to §174 capitalization (see §9). |
| 27 | Total deductions. |  |
| 28 | Taxable income before NOL deduction and special deductions = Line 11 − Line 27. |  |
| 29a | Net operating loss deduction. | See §7. |
| 29b | Special deductions — from **Schedule C, Line 24**. | Primarily DRD; also §250 GILTI/FDII deduction. |
| 29c | Total = 29a + 29b. |  |
| 30 | Taxable income = Line 28 − Line 29c (not less than zero except in the year a loss is generated). |  |
| 31 | Total tax — from **Schedule J, Part I, Line 11**. |  |

### 6.3 Lines 32–37 — Payments, credits, and balance

- **Payments, credits, and balance lines** — - Line 33 (formerly 33a-g): Estimated tax payments, prior year overpayment credit, Form 7004 extension payment, refundable credits. - Line 34: Estimated tax penalty (Form 2220). - Line 35: Amount owed. - Line 36: Overpayment. - Line 37: Refund vs. credit forward.

## 7. Dividends-Received Deduction (DRD) — Schedule C

### 7.1 Purpose and structure

- **Dividends-received deduction purpose** — The DRD under IRC §243 mitigates the triple taxation that would otherwise occur when a corporation receives a dividend from another corporation (the dividend was paid out of earnings already taxed at the payor's level; without the DRD, the recipient corp would pay 21% on it and then its shareholder would pay tax again on distribution). The deduction is computed on Schedule C of Form 1120 and flows to Line 29b via Schedule C Line 24.  _(IRC §243)_

### 7.2 The three tiers

**DRD tiers by ownership**  _(IRC §243(a)(1), §243(c), §243(a)(3), §243(b))_

| Ownership of payor by recipient corp | Deduction % | IRC section |
| --- | --- | --- |
| **Less than 20%** | **50%** | §243(a)(1) |
| **20% to less than 80%** | **65%** | §243(c) |
| **80% or more (affiliated group, no consolidated return)** | **100%** | §243(a)(3) and §243(b) — "qualifying dividends" |

- **TCJA DRD rate change and ownership measurement** — The TCJA reduced the DRD from 70%/80%/100% to 50%/65%/100% effective 2018; this remains in effect for 2025. Ownership is measured by vote and value (§243(c)(2)). For the 80% tier, the affiliated group must meet the §1504(a) definition (80% of vote and value, with attribution rules in §1563), and the dividend must be a "qualifying dividend" under §243(b) — generally, a dividend from a domestic corporation that is a member of the same affiliated group (whether or not consolidated). If consolidated, intercompany dividends are eliminated and the DRD is moot.  _(IRC §243(c)(2); §1504(a); §1563; §243(b))_

### 7.3 Special categories on Schedule C

- **Schedule C key lines** — Schedule C has many specific lines for distinct categories. Key lines: - **Lines 1, 2 Dividends from less-than-20% / 20%-or-more domestic corps** — the bread-and-butter 50% / 65% DRD. - **Line 3 Dividends on certain debt-financed stock** — DRD reduced under §246A if the stock was acquired with debt; reduction is in proportion to debt-financing percentage. - **Line 4 Dividends on certain preferred stock of public utilities** — special 23.3% / 26.7% rate. - **Line 6/7 Dividends from foreign corps that are 20%-or-more US-owned** — eligible for partial DRD. - **Line 8 Dividends from wholly-owned foreign subsidiaries** — fully deductible under §245(b), but only if certain conditions met. - **Line 13 Dividends received from a domestic corp that is a member of the same affiliated group (other than debt-financed)** — 100% DRD. - **Line 14 Other dividends** — including subpart F inclusions, GILTI inclusion, §965 transition tax inclusion. **Subpart F and GILTI inclusions are not eligible for the DRD** (separately, GILTI is partially offset by the §250 deduction — see §10). - **Line 15 §245A 100% participation exemption** — for dividends from 10%-owned specified foreign corporations meeting holding period requirements. This is a 100% deduction, not a true DRD; it implements the post-TCJA territorial system.  _(IRC §246A; §245(b); §965; §245A)_

### 7.4 Holding period rule — §246(c)

- **DRD holding period requirement** — The DRD is disallowed if the recipient corp does not hold the stock for more than 45 days during the 91-day period beginning 45 days before the ex-dividend date (for common stock; 90/181 days for preferred). The holding period is reduced by periods during which the corp has substantially diminished its risk of loss (hedges, options, short positions). Verify with the client that the stock was held throughout — this is a common audit issue with portfolio dividend recipients.  _(IRC §246(c))_

### 7.5 Taxable-income limitation — §246(b)

- **DRD taxable income limitation** — The aggregate DRD (excluding the 100% DRD from affiliated-group dividends and the §245A participation exemption) is limited to a percentage of taxable income computed without regard to the DRD, NOL deduction, §250 deduction, and §1202 deduction. The percentage matches the DRD tier — 50% or 65%. Exception: the limitation does not apply if the DRD creates or increases an NOL (the "NOL exception"). This is computed on Schedule C, Lines 17 through 22 with worksheet support in the Form 1120 instructions. §1202 note (OBBBA): for QSBS issued after July 4, 2025, OBBBA adds a phased exclusion for stock held less than five years (50% for stock held at least three years; 75% for stock held at least four years; 100% at five years), raises the per-issuer gain exclusion limit to $15 million, and raises the issuing corporation's aggregate gross asset test to $75 million. (OBBBA § 70431; IRC § 1202(a))  _(IRC §246(b))_

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

## 8. Net Operating Loss (NOL) — post-TCJA rules

### 8.1 Post-2017 NOLs

- **Post-TCJA NOL treatment** — For NOLs generated in tax years beginning after December 31, 2017 (i.e., 2018 forward, including 2025): No carryback. (The CARES Act temporarily restored a 5-year carryback for 2018, 2019, 2020 losses only — that window is now closed.) Indefinite carryforward under IRC §172(b)(1)(A). 80% limitation under §172(a) — the NOL deduction in any year is limited to 80% of taxable income computed without regard to the NOL deduction itself (and without regard to the §199A and §250 deductions — those are computed after). The 80% limit applies only to post-2017 NOLs; it does not stack on pre-2018 NOLs in the same year (the pre-2018 NOL is taken first under the old rules, then the post-2017 NOL is taken subject to the 80% cap on remaining taxable income).  _(IRC §172(b)(1)(A); IRC §172(a))_

### 8.2 Pre-2018 NOLs

- **Pre-TCJA NOL treatment** — NOLs generated in tax years beginning before January 1, 2018 retain their original-rule treatment: 2-year carryback, 20-year carryforward (§172(b)(1)(A) as in effect pre-TCJA). No 80% limit — can offset 100% of taxable income. Most pre-2018 NOLs have either been used or are nearing the end of their 20-year window. A 2005 NOL expires in 2025; a 2017 NOL expires in 2037. If both pre-2018 and post-2017 NOLs exist, apply them in this order: (1) pre-2018 NOLs first, without the 80% limit; (2) post-2017 NOLs second, subject to the 80% limit on remaining taxable income.  _(IRC §172(b)(1)(A) (pre-TCJA))_

### 8.3 §382 limitation on NOL after ownership change

- **§382 limitation formula** — If the corporation underwent an ownership change (more than 50 percentage point shift in 5%-shareholder ownership over a 3-year testing period) under IRC §382(g), the use of pre-change NOLs is limited annually to: §382 limitation = FMV of equity immediately before the ownership change × long-term tax-exempt rate (published monthly by the IRS — for ownership changes in 2025, in the 4% range; check the AFR table for the change date). Plus a NUBIG (net unrealized built-in gain) adjustment in years where built-in gains are recognized within 5 years of the change. Flag any §382 event for reviewer — the computation is technical and commonly missed.  _(IRC §382(g))_

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

## 9. §163(j) business interest expense limitation

### 9.1 The limit

- **Business interest expense limitation formula** — For tax years beginning after December 31, 2017, IRC §163(j) limits the deduction for business interest expense to the sum of: 1. Business interest income for the year, plus 2. 30% of "adjusted taxable income" (ATI), plus 3. Floor plan financing interest (specific to vehicle dealers). Disallowed business interest carries forward indefinitely and is deducted in future years subject to the same limit.  _(IRC §163(j))_

### 9.2 ATI definition (post-2022)

- **ATI computation change post-2022** — For tax years beginning before January 1, 2022, ATI was computed by adding back depreciation, amortization, and depletion to taxable income — effectively an EBITDA base. For tax years beginning on or after January 1, 2022 and before January 1, 2025 (a TCJA-driven change), ATI was computed without that add-back, making it effectively an EBIT base and substantially tightening the §163(j) limit for capital-intensive businesses. OBBBA permanently restored the EBITDA add-back for tax years beginning after December 31, 2024 (OBBBA § 70303; IRC § 163(j)). For 2025: ATI is EBITDA-based. Add back deductions for depreciation, amortization, and depletion (along with business interest expense and any NOL and §250 deductions) to taxable income when computing ATI. Confirm against the Form 8990 instructions current for 2025.  _(IRC §163(j); Form 8990 instructions)_

### 9.3 Small-business exemption

- **§448(c) gross receipts threshold for §163(j) exemption, 2025** — $31 million USD (average annual gross receipts for prior 3 years; was $30M in 2024)  _(IRC §448(c))_
- **Small business exemption from §163(j)** — A taxpayer is exempt from §163(j) if its average annual gross receipts for the prior 3 years are at or below the §448(c) threshold — $31 million for tax years beginning in 2025 (inflation-adjusted; was $30M in 2024). A corporation that satisfies this test does not need to file Form 8990 (except in limited circumstances such as passing through interest to a partner).  _(IRC §448(c))_

### 9.4 Other exemptions

- **Other §163(j) exemptions** — - Electing real property trades or businesses (irrevocable election under §163(j)(7)(B)) — must use ADS for nonresidential real, residential rental, and qualified improvement property; trades off the §163(j) limit for slower depreciation. - Electing farming businesses (similar trade-off). - Regulated utilities (§163(j)(7)(A)(iv)) — automatically excluded.  _(IRC §163(j)(7)(B); §163(j)(7)(A)(iv))_

### 9.5 Mechanics

- **Form 8990 mechanics** — Computed on Form 8990, Limitation on Business Interest Expense Under Section 163(j), attached to Form 1120 if applicable. The disallowed interest carryforward is tracked on Form 8990 Schedule A.  _(Form 8990)_

### 9.6 Worked §163(j) example

**Facts (corp not subject to small-business exemption):**
- Taxable income (before interest deduction) = $5,000,000
- Depreciation = $1,500,000 (already in deductions)
- Business interest expense = $1,800,000
- Business interest income = $50,000
- Floor plan financing = $0

**ATI computation (EBIT-based, 2025):**
- Start with taxable income before interest = $5,000,000
- Add back: business interest expense ($1,800,000) — yes
- Add back: NOL deduction — yes
- Add back: §250 deduction — yes
- Do NOT add back depreciation/amortization (post-2021 rule).
- ATI = $5,000,000 + $1,800,000 = $6,800,000 (assume no NOL or §250)

**Limit:**
- 30% × $6,800,000 = $2,040,000
- Plus business interest income $50,000 = $2,090,000

**Result:**
- Business interest of $1,800,000 ≤ $2,090,000 limit → fully deductible.

**Alternative (tight scenario):**
- If business interest = $2,500,000:
- Deductible = $50,000 (interest income) + $2,040,000 (30% × ATI) = $2,090,000
- Disallowed and carried forward = $2,500,000 − $2,090,000 = $410,000

## 10. §174 R&D capitalization

### 10.1 The post-TCJA rule

- **§174 capitalization requirement** — Effective for tax years beginning after December 31, 2021, TCJA's §174 amendment required capitalization and amortization of "specified research and experimental expenditures" (SREs). OBBBA then restored immediate expensing for domestic SREs for tax years beginning after December 31, 2024 (OBBBA § 70302; new IRC § 174A): Domestic SREs (tax years beginning after December 31, 2021 and before January 1, 2025): capitalize and amortize over 5 years (60 months), straight-line, beginning with the midpoint of the year incurred (half-year convention). Domestic SREs (tax years beginning after December 31, 2024): fully deductible in the year paid or incurred under new IRC §174A, reduced by any §41 research credit allowed for the year. Foreign SREs (R&E performed outside the US): capitalize and amortize over 15 years (180 months), beginning at the midpoint of the year incurred. Prior to 2022, taxpayers could elect to deduct R&E currently under §174(a); that option was unavailable for 2022-2024, and for tax years beginning after December 31, 2024 current deduction of domestic R&E is again available under §174A.  _(IRC §174; §174(a))_

### 10.2 Status as of 2025

- **§174 status under OBBBA** — OBBBA changed the rule for domestic R&E starting in 2025. For domestic research or experimental expenditures paid or incurred in taxable years beginning after December 31, 2024, OBBBA restores full immediate expensing under new IRC §174A (OBBBA § 70302). Mandatory five-year capitalization applied only to tax years beginning in 2022 through 2024; amounts capitalized in those years continue amortizing under prior law unless a transition election is made. Foreign R&E remains subject to capitalization and 15-year amortization. Any domestic R&E deducted under §174A must be reduced by the §41 research credit allowed for the year. If a 2025 return was prepared assuming mandatory domestic capitalization, revisit it: immediate expensing is the treatment for domestic SREs in 2025.  _(P.L. 119-21 (OBBBA))_

### 10.3 What counts as SRE

- **Specified research or experimental expenditures (SRE)** — "Specified research or experimental expenditures" under §174(b) include: Direct labor and materials for R&D. Software development costs (explicitly included under §174(c)(3)). Allocated overhead reasonably attributable to R&D. Patent costs (legal and filing fees in obtaining a patent, but not litigation). Costs that would have been §41 qualified research expenses under prior law. What does NOT count: market research, quality control, advertising, management studies, routine data collection, efficiency surveys, social science research (in some cases — see §174(d)).  _(IRC §174(b); §174(c)(3); §174(d))_

### 10.4 Mechanics on Form 1120

- **§174 mechanics on Form 1120** — Domestic SREs incurred in 2025 are deductible in the year incurred under §174A (OBBBA § 70302); report them with other deductions (Line 26 with a supporting statement), reduced by any §41 credit. Foreign SREs are not directly deductible on Lines 13, 22, 26, etc. Capitalize foreign SREs (and domestic SREs from 2022-2024 still amortizing) on Form 4562 (intangibles section); foreign SREs amortize over 15 years. For domestic SREs capitalized in 2022-2024, the continuing amortization deduction (1/10 of domestic SREs in year 1 under half-year convention, then 1/5 per year for 4 years, then 1/10 in year 6 — actually: 10% / 20% / 20% / 20% / 20% / 10% over 6 calendar years for 5-year period under half-year, OR 1/2 month start of midpoint convention depending on interpretation; the IRS in Rev. Proc. 2023-8 / Rev. Proc. 2023-11 has clarified mechanics) flows to Form 1120 Line 26 (or appropriate line) as "amortization of §174 costs." Refer R&D mechanics to `us-r-and-d-credit-and-174` for detail. This skill notes the existence of the rule and flags it for the preparer; for any return with material R&E spend (defined here as >$50k of arguable SRE), the R&D skill should be loaded alongside.  _(Form 4562; Rev. Proc. 2023-8; Rev. Proc. 2023-11)_

### 10.5 Interaction with §41 R&D credit

- **§174/§41 credit interaction** — The §41 R&D credit is still available in 2025, computed on Form 6765. There is no incompatibility between deducting domestic R&E under §174A and claiming the §41 credit. However, domestic research expenditures deducted under §174A must be reduced by the §41 credit allowed for the year, unless the taxpayer makes the §280C(c)(2) reduced-credit election (OBBBA § 70302; IRC § 174A). This interaction is computed on Form 6765 Section A or B.  _(IRC §41; §280C(c)(1); §280C(c)(2); Form 6765)_

### 11.1 What §250 does

For tax years beginning after December 31, 2017, IRC §250 (added by TCJA §14202) provides domestic C-corporations a deduction for two categories of income:

1. **GILTI** (Global Intangible Low-Taxed Income inclusion under §951A) — a **50% deduction**, effectively bringing the GILTI tax rate to 10.5% (50% × 21%).
2. **FDII** (Foreign-Derived Intangible Income, generally income from US-based serving of foreign markets) — a **37.5% deduction**, effectively bringing the FDII rate to 13.125% (62.5% × 21%).

- **GILTI §250 deduction rate (post-2017, pre-2026)** — 50% percent (effective GILTI rate 10.5% (50% × 21%))  _(IRC §250, TCJA §14202)_
- **FDII §250 deduction rate (post-2017, pre-2026)** — 37.5% percent (effective FDII rate 13.125% (62.5% × 21%))  _(IRC §250, TCJA §14202)_

### 11.2 The 2025 rates and the 2026 sunset

- **§250 rate sunset schedule** — Under pre-OBBBA §250(a)(3), the percentages were scheduled to drop to 37.5% (GILTI) / 21.875% (FDII) for tax years beginning after December 31, 2025. OBBBA replaced that sunset with new permanent rates for tax years beginning after December 31, 2025 (OBBBA § 70321; IRC § 250(a)(1)): GILTI (renamed "net CFC tested income" by OBBBA) 50% → 40% (effective rate 12.6%); FDII 37.5% → 33.34% (effective rate ~14.0%).  _(§250(a)(3))_
- **OBBBA status on §250 rates** — For tax years beginning in 2025, the 50% / 37.5% rates still apply. For tax years beginning after December 31, 2025, OBBBA sets permanent rates of 40% for net CFC tested income (formerly GILTI) and 33.34% for FDII (OBBBA § 70321; IRC § 250(a)(1)). Flag this on multi-year planning for clients with material GILTI/FDII.  _(§250(a)(3))_

### 11.3 The taxable-income limitation — §250(a)(2)

- **§250 taxable income limitation** — The aggregate §250 deduction is limited to taxable income (computed without regard to the §250 deduction). If the limit binds, the deduction is allocated proportionally between FDII and GILTI categories under §250(a)(2)(B). OBBBA also narrowed deduction-eligible income (DEI): for sales or other dispositions occurring after June 16, 2025, DEI excludes income or gain from the sale or other disposition of intangible property or of any other property of a type subject to depreciation, amortization, or depletion in the hands of the seller. In addition, interest expense and R&D expenses are no longer subtracted in determining DEI. (OBBBA § 70322; IRC § 250(b))  _(§250(a)(2), §250(a)(2)(B))_

### 11.4 Mechanics

- **§250 deduction mechanics** — Computed on Form 8993, Section 250 Deduction for Foreign-Derived Intangible Income (FDII) and Global Intangible Low-Taxed Income (GILTI). The deduction flows to Schedule C, Line 22, which then flows to Form 1120 Line 29b via Schedule C Line 24. GILTI inclusion itself flows to Schedule C Line 14 (as "other dividends" — historically a misleading classification, since GILTI is not actually a dividend; it's a deemed inclusion under §951A). The Form 5471 Schedule I-1 supports the GILTI computation.  _(Form 8993; Schedule C Line 22, 24; Form 1120 Line 29b; §951A)_

### 11.5 Refer-out for complex computations

- **Refer out for GILTI/FDII computation** — The actual GILTI computation (tested income, QBAI return, allocated deductions, high-tax exclusion election under §951A(c)(2)(B)(ii) Reg. §1.951A-2(c)(7)) is highly technical. Similarly, the FDII computation (deduction-eligible income, foreign-derived deduction-eligible income, deemed intangible income) involves multi-step allocations under Reg. §1.250(b)-1 through -6. For any return with material GILTI or FDII, refer to `us-gilti-fdii-computation` (separate skill). This skill notes the existence of the deduction, the 2025 rates, and the form (8993), and ensures the line items flow correctly on Form 1120 and Schedule C.  _(§951A(c)(2)(B)(ii); Reg. §1.951A-2(c)(7); Reg. §1.250(b)-1 through -6)_

### 12.1 Origin and rate

- **CAMT origin and rate** — The Inflation Reduction Act of 2022 (P.L. 117-169, §10101) added IRC §55(b)(2) and §59(k), imposing a 15% Corporate Alternative Minimum Tax on the Adjusted Financial Statement Income (AFSI) of "applicable corporations" for tax years beginning after December 31, 2022. This is NOT the same as the corporate AMT that existed under prior law (repealed by TCJA in 2018). The new CAMT is book-income-based, not tax-base-based, and applies only to very large corporations.  _(P.L. 117-169 §10101; IRC §55(b)(2); §59(k))_
- **CAMT rate** — 15% percent (on Adjusted Financial Statement Income (AFSI) of applicable corporations, tax years beginning after Dec 31, 2022)  _(IRC §55(b)(2); §59(k))_

### 12.2 Who is an "applicable corporation"

- **Applicable corporation** — Under §59(k)(1)(B), a corporation is an "applicable corporation" if its average annual AFSI exceeds $1 billion over the 3 prior tax years (or such shorter period as the corporation has existed). For a corporation that is a member of a foreign-parented multinational group, a separate $100M test applies under §59(k)(2). Once a corporation becomes an applicable corporation, it generally remains one in future years (with limited exceptions for sustained drops in AFSI).  _(§59(k)(1)(B); §59(k)(2))_
- **Applicable corporation AFSI threshold** — $1 billion USD (average annual AFSI over 3 prior tax years)  _(§59(k)(1)(B))_
- **Foreign-parented multinational group AFSI threshold** — $100 million USD (separate test under §59(k)(2))  _(§59(k)(2))_

Practical effect: CAMT applies only to a few thousand of the largest US corporations. If the corporation's revenue is under $500M, CAMT essentially never applies; if AFSI is under $700M-ish on a 3-year average, the test is unlikely to be met. For mid-size and small corps, the answer is "no CAMT" and the corp does not need to compute it.

### 12.3 AFSI definition — book income, adjusted

- **AFSI (Adjusted Financial Statement Income)** — AFSI starts with net income or loss reported on the applicable financial statement (generally the GAAP consolidated income statement, or IFRS if no GAAP — order of priority is in §451(b)(3)) and applies adjustments specified in §56A: - Add back: federal income tax expense. - Adjust for: depreciation differences between book and tax (§56A(c)(13) — added by IRA, allowing tax depreciation in lieu of book depreciation in AFSI to avoid penalizing capital investment). - Adjust for: tax-credit-related items, certain employee benefit items, partnership and CFC pass-throughs. - Adjust for: §168(k) bonus depreciation (allowed as a deduction against AFSI under §56A(c)(13)). - Reduce by: financial statement NOL (FSNOL), limited to 80% of pre-FSNOL AFSI.  _(§451(b)(3); §56A; §56A(c)(13))_
- **FSNOL limitation** — 80% percent (of pre-FSNOL AFSI)  _(§56A)_

### 12.4 The 15% computation

- **Tentative minimum tax (TMT)** — TMT = 15% × AFSI (after FSNOL)  _(§55(b)(2); §59(k))_
- **CAMT computation** — CAMT = max(0, TMT − Regular tax + BEAT) — i.e., the corp pays CAMT only to the extent it exceeds regular tax. The regular tax for this purpose includes the §11 21% tax plus BEAT, but excludes the corporate AMT itself.  _(§55(b)(2); §59(k))_

### 12.5 Foreign tax credit

- **CAMT foreign tax credit** — A CAMT foreign tax credit is available under §59(l) — limited to AFSI-equivalent foreign taxes; mechanics are intricate.  _(§59(l))_

### 12.6 Refundable nature

- **CAMT credit carryforward** — CAMT paid creates a CAMT credit (§53) carried forward indefinitely, usable in future years to reduce regular tax (but not below TMT). It is not refundable in cash; it offsets future regular tax.  _(§53)_

### 12.7 Mechanics

- **CAMT mechanics — Form 4626** — CAMT is computed on Form 4626, Alternative Minimum Tax — Corporations (revised for 2023 and forward to reflect the IRA changes). For 2025, the form requires: AFSI computation worksheet; Adjustments under §56A; FSNOL computation; TMT computation; Comparison with regular tax; CAMT credit carryforward tracking. For any corp with revenue ≥ $500M or with international operations and a parent group ≥ $1B in revenue, run the §59(k) test. For everyone else, document the conclusion that CAMT does not apply (the corp is not an applicable corporation) and skip Form 4626.  _(Form 4626; §59(k); §56A)_

### 12.8 Provisional and final regulations

Treasury issued proposed regulations (REG-112129-23, September 2024) that run several hundred pages. Final regs may differ. For any actual CAMT computation, refer to `us-corporate-amt-computation` (separate skill) — this is too specialized for first-line preparation under this skill.

### 13.1 Schedule B — Additional Information for Schedule M-3 Filers

- **Schedule B questions** — Schedule B asks 13 yes/no questions, primarily directed at consolidated group, ownership, and accounting-method disclosures. Required of all 1120 filers. Key questions: - 1: Is the corporation a subsidiary in an affiliated group or parent-subsidiary controlled group? - 4a, 4b: At end of year, did any individual or estate own (directly or indirectly under §267(c)) 50% or more of total voting stock? - 5a, 5b: At year-end, did the corp own 20% or more of voting stock of any other corporation, or 50% or more in any partnership? - 6: During the year, did the corporation pay dividends in excess of E&P? - 12: Does the corporation have a financial accounting method that materially differs from the tax accounting method? (Drives M-3 requirement.) - 13: During the tax year, did the corp dispose of any tangible property by like-kind exchange? (§1031 is now real-property-only post-TCJA.)  _(§267(c); §1031)_

### 13.2 Schedule C — Dividends, Inclusions, and Special Deductions

See §7. The DRD lines, the §245A participation exemption, the §250 deduction (Line 22), and various subpart F / GILTI inclusions all flow through Schedule C.

### 13.3 Schedule J — Tax Computation and Payment

- **Schedule J Part I — Tax computation** — - Line 1: Check if a "personal holding company" — flag and refer if yes. - Line 2: Income tax = Line 30 × 21%. - Line 3: Base erosion minimum tax (Form 8991) — refer to BEAT skill. - Line 5: Add §59A BEAT, §965 transition tax installments if any. - Line 6 onwards: nonrefundable credits, foreign tax credit (Form 1118), general business credit (Form 3800), §53 prior-year minimum tax credit, etc. - Line 9: Personal holding company tax (Schedule PH). - Line 9a–9g: Other taxes — CAMT (Form 4626), §1374 built-in gains tax (former S that converted — out of scope here), §1375 excess passive investment income tax (S-corps — out of scope), §1291 excess distribution tax from PFIC. - Line 10: Total tax = sum of regular + AMT + other taxes. - Line 11: Total tax flowing to Form 1120 Line 31. FTC haircut on PTEP distributions (OBBBA): for foreign income taxes paid or accrued with respect to amounts excluded from gross income as previously taxed earnings and profits under §959(a), 10% of the foreign taxes paid, accrued, or deemed paid with respect to the distribution is disallowed where the PTEP was excluded by reason of a §951A inclusion, effective for distributions after June 28, 2025. Report the reduction on Schedule G of Form 1118. (OBBBA § 70312(b); IRC § 960(d)(4))  _(§59A; §965; Form 1118; Form 3800; §53; Form 4626; §1374; §1375; §1291)_

**Part II — Payments and refundable credits:**
Prior year overpayment, current-year estimated tax, Form 7004 extension payment, refundable credits.

**Part III — Payments and refundable credits (continued).**

### 13.4 Schedule K — Other Information

- **Schedule K disclosure items** — A miscellany of yes/no and dollar items used by IRS examiners to identify audit issues: - Accounting method (cash, accrual, hybrid). - Business activity code (NAICS). - Direct ownership by foreign person of 25% or more (triggers Form 5472). - Whether the corp had any §351 transferor or §1244 stock issuance. - Tax-exempt interest (§103 — not on Line 5). - Schedule UTP filing (Line 15). - §163(j) status (Line 23, asking whether the corp is subject to and required to file Form 8990). - §59A BEAT status (Line 24, asking whether BEAT applies). - §267A hybrid disallowance. - §59(k) CAMT applicability (Line 29 — added in 2023 for the IRA CAMT).  _(§351; §1244; §103; §163(j); §59A; §267A; §59(k))_

### 13.5 Schedule L — Balance Sheets per Books

- **Schedule L filing threshold** — $250,000 USD (required if total receipts AND total assets are both $250,000 or more at year-end)
- **Schedule L contents** — Even if the threshold is not met, Schedule L is often prepared internally for the M-1 reconciliation. Year-beginning and year-end columns for: - Assets: cash, receivables, inventory, federal/state tax securities, other current assets, loans to shareholders, mortgage and real estate loans, other investments, buildings (with accumulated depreciation), depletable assets, intangibles (less amortization), other. - Liabilities and equity: accounts payable, short-term notes, current portion of mortgages, other current liabilities, loans from shareholders, long-term mortgages, other liabilities, capital stock, additional paid-in capital, retained earnings — appropriated and unappropriated, adjustments to shareholders' equity, treasury stock, less cost of treasury stock. The end-of-year balance sheet must tie to the books and to Schedule M-1/M-3.

### 13.6 Schedule M-1 — Reconciliation of Book Income to Tax Income

- **Schedule M-1 reconciliation** — Required if Schedule M-3 is not required. Reconciles: - Net income per books (Line 1) + federal income tax (Line 2) + excess of capital losses over gains (Line 3) + income subject to tax not on books (Line 4) + expenses on books not deducted (Line 5) − income on books not on return (Line 7) − deductions on return not charged against book income (Line 8) = taxable income before NOL and special deductions (must equal Form 1120 Line 28). Common Line 5 items: 50% of meals, fines and penalties, federal tax expense (also on Line 2), political contributions, lobbying (§162(e)), club dues, executive comp over §162(m) $1M limit, certain disallowed fringe benefits. Common Line 7 items: tax-exempt interest, life insurance proceeds, federal income tax refund of prior-year taxes if not previously deducted. Common Line 8 items: tax depreciation in excess of book, §199A — N/A (corp), §250 deduction (if not in book), §168(k) bonus deduction.  _(§162(e); §162(m); §250; §168(k))_

### 13.7 Schedule M-3 — Net Income (Loss) Reconciliation

- **Schedule M-3 filing threshold** — $10 million USD (total assets at year-end triggers Schedule M-3 requirement)  _(Reg. §1.6011-4(c)(1))_
- **Schedule M-3 structure** — For total assets under $10M, M-1 is used instead; corps with assets between $10M and $50M may file Schedule M-1 in lieu of M-3 only in limited circumstances. Schedule M-3 has three parts: - Part I: Financial Statement Information — identifies the source of book income (Form 10-K, certified audit report, internal financials). - Part II: Reconciliation of net income per income statement to taxable income — line by line on income items. - Part III: Reconciliation on expense and deduction items. Schedule M-3 is far more detailed than M-1 and is used by IRS LB&I examiners to identify large book-tax differences for audit selection. Misclassifications between permanent and temporary differences (Columns A through D) commonly cause IRS notices.  _(Reg. §1.6011-4(c)(1))_

### 13.8 Schedule O — Consent Plan and Apportionment for a Controlled Group

- **Schedule O requirement** — Required if the corporation is a member of a controlled group under §1561 that elects to apportion the §11 rate brackets (now irrelevant under the flat 21% rate — but Schedule O is still used to apportion certain other items, particularly the AMT exemption pre-2018 and the §535 accumulated earnings credit). For 2025, the practical use of Schedule O has narrowed. Still required if the corp is a member of a controlled group and certain elections are made.  _(§1561; §535)_

### 13.9 Schedule UTP — Uncertain Tax Positions

- **Schedule UTP filing threshold** — $10 million USD (total assets $10 million or more AND at least one uncertain tax position reserved for in audited financial statements (GAAP ASC 740-10, formerly FIN 48))
- **Schedule UTP disclosures and penalty** — Discloses: - Each UTP, by IRC section. - Ranking by size of reserve. - Description of the position (concise — the IRS provides examples in the Schedule UTP instructions). Failure to file Schedule UTP when required does not have a stand-alone penalty (per IRS internal practice), but it draws scrutiny. Refer technical UTP analysis to the tax provision team or specialist — this skill flags the obligation but does not analyze the positions.

## 14. Common attached forms

**Common attached forms**

| Form | When attached |
| --- | --- |
| **Form 1125-A — Cost of Goods Sold** | Mandatory if there is any COGS on Form 1120 Line 2. |
| **Form 1125-E — Compensation of Officers** | Mandatory if total receipts are **$500,000 or more**. See §15. |
| **Form 4562 — Depreciation and Amortization** | Attach if any §168(k) bonus, §179, MACRS placed in service this year, or any amortization (§174, §195, §197). |
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

## 15. Officer compensation — Form 1125-E

- **Form 1125-E filing threshold** — $500,000 USD (total receipts (Form 1120 Line 1a + Line 4 + Lines 5–10))  _(IRC §6651; Form 1120 instructions)_
- **Form 1125-E contents and flow** — Form 1125-E discloses: - Name and SSN of each officer (or top-paid officers if many). - Percent of time devoted to the business. - Percent of voting stock owned. - Amount of compensation paid (cash + non-cash). The total from Form 1125-E flows to Form 1120 Line 12.  _(Form 1120 instructions)_

### 15.1 Reasonable compensation issue

- **Reasonable compensation — overpayment issue** — Unlike S-corps (where reasonable compensation is an issue about underpayment — owners trying to recharacterize wages as distributions to avoid payroll tax), C-corps face a reasonable compensation issue under §162(a) about overpayment — owner-employees paying themselves excessive salary to convert nondeductible dividends into deductible wages. The IRS may recharacterize "excessive" compensation as a constructive dividend, disallowing the corporation's deduction (creating taxable income at 21%) and treating it as a dividend to the shareholder (taxed again at qualified dividend rates of 0/15/20% plus 3.8% NIIT). The classic case law factors (Mayson Mfg., Charles Schneider, Exacto Spring, Menard) examine: - Role and responsibility. - Time and effort. - Comparison with industry comp data. - Internal pay consistency. - Whether unrelated executives would accept the same comp. - The "independent investor test" — would a hypothetical outside investor accept the salary level given the return on equity? (Exacto Spring, 7th Cir. 1999.) For closely-held C-corps with material owner-employee comp, flag this for reviewer if comp exceeds industry norms.  _(§162(a); Mayson Mfg.; Charles Schneider; Exacto Spring (7th Cir. 1999); Menard)_

### 15.2 §162(m) $1M deduction cap

- **§162(m) covered employee compensation cap** — $1,000,000 USD (per individual per year, for publicly held corporations, covered employees (CEO, CFO, top 3 highest-paid, plus anyone who was a covered employee in a prior year post-2017))  _(IRC §162(m))_
- **§162(m) cap scope and ARPA expansion** — The cap applies whether comp is base salary, bonus, equity, or any other form (TCJA repealed the performance-based-comp exception). For private companies, no §162(m) cap applies. ARPA expanded covered employees to include the next 5 highest-paid effective 2027.  _(IRC §162(m); TCJA; ARPA)_

### 15.3 §280G golden parachute

- **§280G golden parachute rule** — For change-in-control payments, §280G may disallow the deduction for "excess parachute payments" and impose a 20% excise tax on the recipient (§4999). Out of scope for routine prep; flag any M&A-year return for reviewer.  _(§280G; §4999)_

### 16.1 §6651(a)(1) Late filing

- **Late filing penalty rate and cap** — If Form 1120 is filed after the original due date (or extended due date, if Form 7004 was timely filed), penalty is: 5% of unpaid tax per month or fraction thereof, capped at 25% of unpaid tax.  _(§6651(a)(1))_
- **Late filing minimum penalty (60+ days late)** — If more than 60 days late, the minimum penalty is the lesser of $485 (2025 inflation-adjusted amount; verify against the current Rev. Proc.) or 100% of unpaid tax. For 2025, the §6651(a) minimum is in the $485 range; check the most recent Rev. Proc. for the exact figure. If no tax is due (refund or zero balance), the late filing penalty is $0 — there's nothing to multiply 5% against.  _(§6651(a))_

### 16.2 §6651(a)(2) Late payment

- **Late payment penalty rate and cap** — If tax is unpaid after the original due date (even with a valid extension to file), penalty is: 0.5% of unpaid tax per month, capped at 25%. Reduced to 0.25%/month while an installment agreement is in effect.  _(§6651(a)(2))_

### 16.3 Combined cap

- **Combined late filing/payment penalty cap** — When both §6651(a)(1) and §6651(a)(2) apply in the same month, the late-filing penalty is reduced by the late-payment penalty for that month, so the combined monthly rate is 5% (not 5.5%). Total combined cap = 47.5% (25% LF − 25% × 0.5% × 5 months reduction + 25% LP). In practice, the §6651(a)(1) penalty is 4.5%/month after the §6651(a)(2) offset.  _(§6651(a)(1); §6651(a)(2))_

### 16.4 §6651(c)(1) reasonable cause

- **Reasonable cause abatement** — Penalty abated for reasonable cause (e.g., reliance on professional advice, natural disaster, death of preparer or officer). Document the facts contemporaneously; the IRS applies §6651(c)(1) restrictively.  _(§6651(c)(1))_

### 16.5 §6601 Interest

- **Interest on unpaid tax** — Interest on unpaid tax accrues from the original due date at the applicable federal underpayment rate (announced quarterly by the IRS). For Q1 2026, the corporate underpayment rate for amounts up to $100k is generally 1 percentage point above the short-term AFR; for large corporate underpayments above $100k, the rate is 5 percentage points above (the "hot interest" under §6621(c)). Verify against the current quarterly rate notice.  _(§6601; §6621(c))_

### 16.6 §6699 — N/A for C-corps

- **§6699 inapplicability to C-corps** — Note: §6699 (per-shareholder per-month late filing penalty for S-corps and partnerships) does not apply to C-corps. The C-corp penalty is tax-based under §6651, not headcount-based.  _(§6699; §6651)_

## 17. E-file mandate

- **E-file mandate conditions** — Under Reg. §301.6011-5 (as amended by T.D. 9972, effective for filings due in 2024 and later), electronic filing is mandatory for any corporation that: 1. Has total assets of $10 million or more at year-end, OR 2. Files 10 or more returns of any kind during the calendar year (aggregating Forms W-2, 1099, 1042-S, 5471, 5472, etc.). This is a substantial expansion of the prior rules and now captures most small and mid-size corps that issue payroll W-2s and 1099s.  _(Reg. §301.6011-5; T.D. 9972)_
- **E-file mandate — total assets threshold** — $10 million USD (total assets at year-end triggers mandatory e-filing)  _(Reg. §301.6011-5; T.D. 9972)_
- **E-file mandate — number of returns threshold** — 10 returns (10 or more returns of any kind filed during the calendar year (aggregating W-2, 1099, 1042-S, 5471, 5472, etc.) triggers mandatory e-filing)  _(Reg. §301.6011-5; T.D. 9972)_

Paper filing remains permitted for corporations under both thresholds — primarily very small inactive or holding companies. Even then, e-filing is recommended; it reduces processing time and avoids transcription errors.

E-file is via IRS Modernized e-File (MeF) through an authorized e-file provider (Drake, Lacerte, ProConnect, UltraTax, CCH Axcess, etc.) or direct via the IRS-provided software for very small filers.

### 17.1 Signature

- **E-file signature authorization** — For e-filed returns, the corporate officer (typically the CFO, CEO, treasurer, or other person authorized to sign Form 1120) signs Form 8879-CORP, IRS e-file Signature Authorization for Form 1120, which authorizes the ERO (electronic return originator) to submit the return with a PIN. The original signed 8879-CORP must be retained by the ERO and made available on IRS request; it is not filed with the return.  _(Form 8879-CORP)_

### 18.1 Form 8832 effective date

- **Form 8832 effective date rules** — An LLC that elects C-corp treatment files Form 8832 (Entity Classification Election) and specifies an effective date (up to 75 days back, up to 12 months forward, from filing). The first 1120 covers the period beginning on the effective date.  _(Form 8832)_
- **Disregarded entity to C-corp conversion** — If the LLC was previously a disregarded entity (single member), the conversion is a deemed §351 transfer — the member is deemed to contribute the LLC's assets and liabilities to a newly-formed corporation in exchange for stock. Recognize: - Built-in gain on the contributed assets (rare unless boot or excess liabilities). - Carryover basis for the C-corp under §362. - Holding period tacks under §1223. - Pre-conversion losses of the disregarded entity (which were Schedule C) do NOT carry into the C-corp (they were the owner's losses, not the entity's).  _(§351; §362; §1223)_
- **Partnership to C-corp conversion** — If the LLC was previously a partnership (multi-member), the conversion is a deemed contribution by each partner of their partnership interest to the corporation under §351, or alternatively can be structured as a deemed asset contribution. The form of the deemed transaction matters for basis and gain — see Rev. Rul. 84-111 for the three permissible forms of partnership-to-corp conversion.  _(§351; Rev. Rul. 84-111)_

### 18.2 Short year

- **Short-year first 1120 due date** — If Form 8832 is effective mid-year, the C-corp files a short-year 1120 for the period from effective date to year-end. The first-year due date is the 15th day of the 4th month after that short year-end.

### 18.3 New EIN?

- **EIN retention on classification election** — The LLC retains its existing EIN — no new EIN is needed solely because of the entity classification election (per IRS practice and the EIN instructions, Form SS-4).  _(Form SS-4)_

### 18.4 Five-year rule on revocation

- **60-month classification lock-in** — Once a Form 8832 election is made, the entity generally cannot change classification again for 60 months (5 years) — IRC §7701 default rules and Reg. §301.7701-3(c)(1)(iv). Limited exceptions exist for ownership changes exceeding 50%.  _(IRC §7701; Reg. §301.7701-3(c)(1)(iv))_

### 18.5 Disclosure

- **First-year 1120 disclosure statement** — The first 1120 should include a statement noting the election, attaching a copy of Form 8832, and noting the effective date.  _(Form 8832)_

## 19. Worked examples

### 19.1 Example A — Simple domestic C-corp

"Acme Widgets, Inc.", a Delaware C-corp, calendar year, single-state operations (Delaware only).
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

**Form 1120 income**  _(Form 1120)_

| Line | Description | Amount |
| --- | --- | --- |
| 1a | Gross receipts | $4,200,000 |
| 2 | COGS (Form 1125-A) | $2,300,000 |
| 3 | Gross profit | $1,900,000 |
| 5 | Interest | $5,000 |
| 11 | Total income | $1,905,000 |

**Deductions**  _(Form 1120)_

| Line | Description | Amount |
| --- | --- | --- |
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

**Corrected TI and tax**  _(Schedule J)_

| Line | Description | Amount |
| --- | --- | --- |
| 28 | TI (corrected) | $252,000 |
| 29a | NOL deduction | $0 |
| 29b | Special deductions (DRD/§250) | $0 |
| 30 | Taxable income | $252,000 |
| 31 | Tax (Schedule J) = 21% × $252,000 | **$52,920** |

- Prior-year tax (2024): assume $115,000.
- Current-year tax (2025): $52,920.
- Required annual payment = lesser of 100% × $115,000 = $115,000 OR 100% × $52,920 = $52,920 → $52,920 (this is the lesser).
- Acme is NOT a large corp (taxable income never $1M+ in prior 3 years, presumably).
- Quarterly installments: $52,920 / 4 = $13,230 each.
- Estimated taxes paid: $130,000. Massive overpayment.
- Refund or credit forward = $130,000 − $52,920 = $77,080.

**Schedule M-1**  _(Schedule M-1)_

| Line | Item | Amount |
| --- | --- | --- |
| 1 | Net income per books | (Compute backward) |
| 2 | Federal income tax expense per books | $130,000 |
| 5 | Expenses on books not deducted: $2k charitable carryforward + meals 50% etc. | $2,000 |
| 8 | Tax depreciation in excess of book | (Assume 0 for simplicity) |
| 10 | TI per Form 1120 Line 28 | $252,000 |

If book NI = $120,000, M-1 reconciles: $120,000 + $130,000 + $2,000 = $252,000. ✓

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

Due April 15, 2026. E-file (over 10 W-2s/1099s issued).

### 19.2 Example B — Multinational with GILTI and FDII

"GlobalTech Inc.", a Delaware C-corp, calendar year.
- 100% owner of a wholly-owned Irish CFC, "GlobalTech Ireland Ltd."
- 2025 US revenue: $80M (of which $30M is FDDEI — Foreign-Derived Deduction-Eligible Income, sales to foreign customers).
- 2025 GlobalTech Inc. taxable income before §250 deduction = $20,000,000.
- GlobalTech Ireland Ltd. tested income = $5,000,000 (passes through as a GILTI inclusion).
- QBAI return on Ireland tangible assets = $800,000.
- Foreign tax credits available for GILTI (after 80% haircut and §904 sourcing) — assume usable to reduce GILTI tax.

- Tested income: $5,000,000
- Less: 10% × QBAI return × QBAI ($8M, so 10% × $8M = $800k, but assume this is already netted in tested income terms — net GILTI = $5,000,000 − $800,000 = $4,200,000.
- GILTI inclusion on Schedule C Line 14 = $4,200,000.

GILTI portion:
- GILTI included = $4,200,000.
- §250 deduction on GILTI = 50% × $4,200,000 = $2,100,000.
- §78 gross-up for foreign taxes paid by CFC ≅ assume $500,000 → additional Schedule C line 16 inclusion (also eligible for §250).

FDII portion:
- Deduction-eligible income = ... (computed under §250(b) regulations) — assume FDII = $4,000,000 after the allocation steps.
- §250 deduction on FDII = 37.5% × $4,000,000 = $1,500,000.

Total §250 deduction = $2,100,000 + $1,500,000 = $3,600,000.

- **§250(a)(2) limitation** — Aggregate §250 deduction limited to taxable income before §250. Taxable income before §250 = $20,000,000 (assumed; this already includes the GILTI inclusion). $3,600,000 ≤ $20,000,000 → no proration needed.  _(§250(a)(2))_

- Line 28 TI before NOL and special deductions = $20,000,000.
- Line 29b Special deductions (§250 from Schedule C Line 22) = $3,600,000.
- Line 30 TI = $16,400,000.
- Line 31 Tax (Schedule J) = 21% × $16,400,000 = $3,444,000.

Reduces the line 31 tax via Schedule J, computed on Form 1118. (Refer to FTC skill.)

- Plus Forms 5471 (Ireland), 8993, 1118 (FTC), Schedule UTP if applicable (assets ≥ $10M likely).
- Schedule M-3 likely required (assets ≥ $10M).

For 2026, the §250 deduction percentages drop to 37.5% / 21.875% (see §11). If GlobalTech's GILTI inclusion were the same in 2026, the §250 deduction on GILTI alone would drop from $2.1M to $1.575M, increasing 2026 tax by $110,250. Flag for tax planning.

### 19.3 Example C — CAMT-triggered large corp

"MegaCorp, Inc.", a Delaware C-corp, calendar year.
- 3-year average AFSI (2022, 2023, 2024): $1.2 billion → **MegaCorp is an applicable corporation** under §59(k).
- 2025 AFSI before FSNOL = $1,100,000,000.
- 2025 FSNOL available = $200,000,000 (limited to 80% × $1.1B = $880M, so all $200M usable).
- 2025 regular taxable income (Form 1120 Line 30) = $300,000,000 (heavily reduced by §168(k), §174 amortization, FDII deduction).
- Regular tax (Schedule J Line 2) = 21% × $300,000,000 = $63,000,000.
- BEAT: assume $0 for simplicity.

- **CAMT computation (Form 4626)** — AFSI after FSNOL = $1,100,000,000 − $200,000,000 = $900,000,000. TMT = 15% × $900,000,000 = $135,000,000. Regular tax (+ BEAT) = $63,000,000. CAMT = max(0, $135,000,000 − $63,000,000) = $72,000,000.  _(Form 4626)_

- Regular tax: $63,000,000
- + CAMT: $72,000,000
- = **Total: $135,000,000**

Effective rate = $135M / $300M = 45% on regular taxable income, but actually 15% on AFSI, which is the policy outcome of CAMT.

- **CAMT credit carryforward** — The $72M CAMT generates a §53 CAMT credit of $72M carried forward indefinitely, usable in years when regular tax exceeds TMT.  _(§53)_

- All of Schedule J including CAMT lines.
- Form 4626.
- Schedule UTP (assets ≥ $10M almost certainly).
- Schedule M-3 (assets ≥ $10M).
- Likely Forms 5471, 5472, 8990, 8991/8993, 8975 (CbC) — refer out for each.
- E-file mandatory (large corp).

- **Estimated tax** — MegaCorp is a large corporation (TI well over $1M in each prior year). No prior-year safe harbor allowed for installments 2–4. Must use 100% of current-year tax. Quarterly installments = $135M / 4 = $33,750,000 each. Failure to fully fund triggers §6655 penalty on Form 2220.  _(§6655)_

## 20. Provenance and disclaimer

### 20.1 Statutory citations relied on

- IRC §11 (corporate rate, 21%)
- IRC §55(b)(2), §59(k), §56A (CAMT, IRA 2022)
- IRC §163(j) (interest limitation)
- IRC §172 (NOL, post-TCJA rules)
- IRC §174 (R&E capitalization, TCJA)
- IRC §243, §245, §245A, §246, §246A (DRD)
- IRC §250 (GILTI/FDII deduction)
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

- **Small-business threshold (IRC §448(c))** — $31,000,000 USD (for 2025)  _(IRC §448(c))_

### 20.2 Legislative provenance

- **Tax Cuts and Jobs Act (TCJA), P.L. 115-97 (December 22, 2017)** — 21% rate, §163(j), §174 capitalization (delayed effective date), DRD reduction, NOL 80%/no-carryback, §250 enactment, FDII/GILTI.
- **Inflation Reduction Act (IRA), P.L. 117-169 (August 16, 2022)** — CAMT under §55(b)(2) and §59(k), stock buyback excise tax under §4501.
- **One Big Beautiful Bill Act (OBBBA), P.L. 119-21 (July 4, 2025)** — did NOT modify the corporate rate, the CAMT, §163(j), §174, §250, or DRD. Confirmed in conference report. Made certain individual TCJA provisions permanent but did not extend the §250 elevated deduction (50%/37.5%) past 2025.

### 20.3 IRS guidance

- Form 1120 Instructions for 2024 (used as template for 2025 — verify against released 2025 instructions before filing).
- Form 4626 Instructions (2023 revision for IRA CAMT).
- Form 8993 Instructions.
- Form 8990 Instructions.
- Rev. Proc. 2024-40 (inflation adjustments for 2025; $485 minimum late filing penalty figure subject to confirmation against current Rev. Proc.).
- Rev. Proc. 2023-8, Rev. Proc. 2023-11 (§174 SRE method change).
- Notice 2023-7 and subsequent CAMT notices (Notice 2023-20, 2023-64, 2024-10, 2024-66, 2025 updates).
- REG-112129-23 (CAMT proposed regs, September 2024).

### 20.4 Disclaimer

This skill provides a structured walkthrough for preparing Form 1120 for tax year 2025 under federal law. It is intended for use by a Circular 230 practitioner (CPA, EA, or attorney) and must be reviewed and signed by such a practitioner before the return is filed. The skill does not constitute tax advice to any specific taxpayer.

**Specific verification required before filing any return:**

1. Confirm the 2025 Form 1120 and instructions as released by the IRS in late 2025 / early 2026 (changes from the 2024 form possible).
2. Confirm the 2025 Rev. Proc. inflation adjustments (small-business threshold, §6651 minimum penalty, §6655 large-corp threshold).
3. Confirm no late-2025 or early-2026 legislation altered §174, §163(j), §250 sunset, or CAMT thresholds. Watch for the routinely-proposed (and routinely-stalled) R&D restoration / EBITDA restoration / bonus depreciation extension package.
4. Confirm the corporation's state filings — this skill addresses federal only.
5. For any item flagged "refer out" (consolidated returns, foreign subsidiaries, BEAT, R&D, FTC, CAMT mechanics, stock buyback excise), engage the specialized skill or specialist.

**State tax warning:** Federal taxable income is the starting point for most state corporate income tax computations, but virtually every state adjusts away from federal in specific areas (state-specific decoupling from bonus depreciation, §163(j), §168(k), §250, §174). Always run the state return alongside the federal, not after.

**End of skill.**

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
