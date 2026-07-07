---
name: us-form-1065-partnership
description: US federal content skill for preparing Form 1065 — the US partnership return. Covers tax year 2025 including the March 15 due date and Form 7004 6-month extension, the $245-per-partner-per-month §6698 penalty even for no-tax-due returns, the tax basis capital account reporting requirement, the Centralized Partnership Audit Regime (CPAR/BBA) and the Schedule B-2 election out, Schedule K-1 preparation including §199A passthrough codes, Schedules K-2 and K-3 for international items, §704(b) special allocations, §704(c) contributed property, §752 liability share, basis/at-risk/passive limits, and the post-Soroban scrutiny on limited-partner SE exemption.
jurisdiction: US
domain: federal-tax
tax_year: 2025
reviewed_by: Christopher Aryee
review_status: accountant-reviewed
tier: 1
last_updated: 2026-07-06
---

# us-form-1065-partnership

## US Form 1065 — Partnership Return (Tax Year 2025)

> **Tier 2 federal content skill.** MUST be loaded alongside `us-tax-workflow-base` v0.2+. This skill provides the partnership-return rules; the workflow base provides the intake, runbook, and reviewer-package scaffolding. Federal only. State pass-through entity (PTE) filings are deferred to the relevant state skill.

### 1.1 In scope

This skill prepares **Form 1065 — U.S. Return of Partnership Income** for tax year 2025 for the following entity types treated as partnerships for federal tax purposes:

- General partnerships (GP)
- Limited partnerships (LP) — including family limited partnerships (FLPs)
- Limited liability partnerships (LLPs) and limited liability limited partnerships (LLLPs)
- Limited liability companies (LLCs) with **two or more members** that have not elected to be taxed as a corporation (the default classification under Treas. Reg. §301.7701-3)
- Joint ventures that rise to the level of a partnership under §761 and Treas. Reg. §1.761-1(a)
- "Investment clubs" treated as partnerships
- Foreign partnerships with US-source income or US partners — only to the extent that Form 1065 (rather than Form 8865) is the correct return; see §1.2

The skill produces:

- Form 1065 (5 pages including Schedules B, K, L, M-1, M-2 on the form itself)
- Schedule B-1 (50%+ owner disclosure) when triggered
- Schedule B-2 (election out of CPAR) when triggered
- Schedule K-1 for each partner (the most important deliverable — partners cannot file their own 1040 without it)
- Schedules K-2 and K-3 when international activity or foreign partners exist, OR when the Domestic Filing Exception under the K-2/K-3 instructions does **not** apply
- Schedule M-3 when total assets at year-end are ≥ $10 million
- Common attached forms: 4562, 4797, 8825, 8990, 6765 (where indicated by the taxpayer's facts)
- Reviewer brief covering CPAR election decision, §704(b)/(c) issues, §752 liability allocation, partner basis/at-risk/passive limit indicators, and SE tax classification per partner

### 1.2 Out of scope (refuse and route)

- **LLCs that have elected C-corp treatment** — file Form 1120 (route to us-form-1120-c-corporation skill, when available)  _(Form 8832)_
- **LLCs that have elected S-corp treatment** — file Form 1120-S (route to us-form-1120s-s-corporation skill)  _(Form 2553)_
- **Single-member LLCs, no corporate election** — disregarded entity, owner files Schedule C / E / F on Form 1040 (route to us-sole-prop-bookkeeping, us-schedule-c-and-se-computation)
- **Qualified joint ventures (QJV) between spouses** — each spouse files own Schedule C; not a partnership return  _(§761(f))_
- **Foreign partnerships requiring Form 8865** — refer out; this skill does not prepare Form 8865, but flags the trigger  _(Form 8865, categories 1–4 controlled foreign partnerships)_
- **Publicly traded partnerships (PTPs)** — out of scope; their compliance burden (passive activity per-PTP rules, withholding on transfers) requires a specialized skill  _(§7704; §1446(f))_
- **Tiered partnerships with upper-tier partnership partners** — Schedule B-2 election out is unavailable; specialized CPAR handling required; refuse for v0.1
- **Real estate partnerships with reverse §704(c) layers, §734/§743/§754 step-ups, or disguised-sale issues** — flag and refer to a senior tax attorney; this skill identifies but does not compute these  _(§704(b)/(c); §734; §743; §754; §707(a)(2)(B))_
- **Section 1061 carried-interest holding-period adjustments** — out of scope for v0.1; flag and refer  _(§1061)_
- **State pass-through entity tax (PTET) elections** — deferred to the state skill (e.g., ca-540-pte-election)
- **Section 6226 push-out elections following an IRS audit** — partially covered as concept; mechanics of preparing the statement and partner notifications are out of scope for v0.1  _(§6226)_
- **Withholding under §1446 on ECI for foreign partners** — flag and refer; this skill does not prepare the §1446 withholding return  _(§1446; Forms 8804/8805/8813)_

### 1.3 Conservative defaults

- **K-2/K-3 conservative default** — If the taxpayer's facts could plausibly trigger Schedules K-2/K-3 and the Domestic Filing Exception conditions are not all clearly met from the intake, prepare K-2/K-3.
- **CPAR election-out caution** — If a partner could plausibly be a disregarded entity owned by a non-eligible owner, do not elect out of CPAR on Schedule B-2 without explicit reviewer confirmation.
- **Soroban-style SE flag** — If a partner is a "limited partner" in form but materially participates (Soroban-style fact pattern), flag for SE tax and surface to reviewer.
- **Tax basis capital reporting default** — Tax basis capital account reporting on K-1 Item L is never GAAP, §704(b) book, or "other" — always tax basis.

### 2.1 Statutory rule

- **Filing requirement and informational nature** — §6031(a) requires every partnership to file an information return. The return is informational — the partnership itself does not pay federal income tax (other than certain BBA imputed underpayments after an audit; see §10). All tax flows through to the partners on Schedule K-1, who report it on their own returns.  _(§6031(a))_

### 2.2 Entity classification mechanics

**Entity classification table**  _(Treas. Reg. §301.7701-3(b)(1)(i))_

| Entity type | Default federal classification | Form 1065 required? |
| --- | --- | --- |
| Two-member LLC (no election) | Partnership | **Yes** |
| Two-member LLC, Form 8832 to C-corp | Corporation | No (files 1120) |
| Two-member LLC, Form 2553 to S-corp | S corporation | No (files 1120-S) |
| General partnership | Partnership | **Yes** |
| LP | Partnership | **Yes** |
| LLP / LLLP | Partnership | **Yes** |
| Single-member LLC, no election | Disregarded entity | No (Schedule C/E/F) |
| Spousal LLC in community-property state, election under Rev. Proc. 2002-69 | Disregarded entity (single owner) | No |
| Spousal QJV under §761(f), non-LLC | Two Schedules C | No |
| Tenants-in-common with rental only, no joint marketing | Co-ownership, not a partnership | No (separate Schedule E) |
| Investment club | Usually partnership | **Yes** unless §761(a) election out |

### 2.3 The §761(a) election out

- **§761(a) election out** — A partnership may elect under §761(a) and Treas. Reg. §1.761-2 to be excluded from Subchapter K if it is used only for investment or for the joint production, extraction, or use of property (and certain other narrow categories), and the partners can compute income without computing partnership taxable income. This is rare in practice. If asserted by the taxpayer, verify that the election was properly made on a timely Form 1065 for the first year and that no Form 1065 has been filed since.  _(§761(a); Treas. Reg. §1.761-2)_

### 2.4 Foreign partnerships

- **Foreign partnership filing trigger** — A foreign partnership is required to file Form 1065 if it has either: Gross income effectively connected with a US trade or business (ECI), OR Gross income (including gains) from US sources — subject to the exceptions in Treas. Reg. §1.6031(a)-1(b)(3) (no US partners, no ECI, etc.). A US person who owns a foreign partnership at the controlling level may also need Form 8865. Form 8865 is not a substitute for Form 1065 when the foreign partnership itself has a Form 1065 filing obligation — both can apply. This skill flags the Form 8865 trigger but defers preparation.  _(Treas. Reg. §1.6031(a)-1(b)(3))_

### 3.1 Original due date

- **Original due date** — Form 1065 is due on the 15th day of the 3rd month following the close of the partnership's tax year (§6072(b)). For a calendar-year partnership (the overwhelming majority — §706(b) generally requires the partners' required taxable year), the due date is: March 15, 2026 for tax year 2025. This is one month earlier than the Form 1120 (C corporation) due date of April 15, and the same day as Form 1120-S (S corporation). The March 15 deadline exists so that partners receive their K-1s in time to file their own April 15 returns. If March 15, 2026 falls on a Sunday (it does — 2026-03-15 is a Sunday), the due date moves to the next business day: Monday, March 16, 2026. Reviewer should always confirm the calendar week in the working papers.  _(§6072(b); §706(b))_

### 3.2 Fiscal-year partnerships

- **Required taxable year and fiscal-year due date** — §706(b) requires a partnership to use its "required taxable year" — generally the majority-interest taxable year, then the principal-partners year, then the least-aggregate-deferral year. A partnership may use a different fiscal year only via §444 election (limited to ~3-month deferral, with a §7519 required payment) or an approved business-purpose year under Rev. Proc. 2002-39. For a fiscal-year partnership, due date = 15th day of 3rd month after year-end (e.g., June 30 year-end → September 15 due date).  _(§706(b); §444; §7519; Rev. Proc. 2002-39)_

### 3.3 Extension — Form 7004

- **Form 7004 6-month extension** — Form 7004 (Application for Automatic Extension of Time to File Certain Business Income Tax, Information, and Other Returns) provides a 6-month automatic extension for Form 1065. It must be filed on or before the original due date (March 15 for calendar-year). Extended due date for 2025 calendar-year partnerships: September 15, 2026 (or the next business day if September 15 is a weekend/holiday). Form 7004 is automatic — no reason needs to be stated. But: It extends time to file, not time to pay. Partnerships generally don't owe income tax, but they may owe the §7519 required payment for §444 fiscal years and certain other amounts. A late Form 7004 is not an extension at all and exposes the return to the §6698 late-filing penalty from day one past March 15. Each partner's K-1 should still be furnished as soon as available; partners commonly need to extend their own 1040 to October 15 because their K-1 is not ready until September.  _(Form 7004; §7519; §6698)_

### 3.4 Reviewer checklist on due dates

- [ ] Tax year confirmed (calendar vs §444 fiscal vs natural)
- [ ] Original due date computed
- [ ] If extending, Form 7004 filed by original due date (capture postmark / e-file acknowledgment)
- [ ] Extended due date computed and calendared
- [ ] Partners notified of K-1 delivery target date

### 4.1 Statutory rule

- **§6698 penalty amount** — $255 per partner, per month (or fraction thereof), for up to 12 months (2025; Instructions for Form 1065 (2025), Penalties) USD per partner per month  _(§6698(b)(1); §6698(e))_
- **§6698 base amount history** — The base amount was set at $195 by the Tax Increase Prevention Act of 2014 and is adjusted annually for inflation under §6698(e). Historical recent values (verify against Rev. Proc. 2024-40 or successor for the exact 2025 figure):  _(§6698(e); Tax Increase Prevention Act of 2014)_

**Per-partner per-month penalty by tax year**  _(Rev. Proc. 2024-40 §3.61)_

| Tax year | Per-partner / per-month |
| --- | --- |
| 2023 | $220 |
| 2024 | $235 |
| 2025 | $245 (verify; ~$245 per Rev. Proc. 2024-40 §3.61) |

- **Penalty applies even with no tax due** — The penalty applies even when the partnership owes no tax — which it almost never does. This is the most common compliance failure cost in partnership practice.  _(§6698)_

### 4.2 Examples

- **3-partner LLC, return filed 2 months late, no extension:** 3 partners × $245 × 2 months = **$1,470**.
- **3-partner LLC, return filed 13 months late:** 3 × $245 × 12 (capped) = **$8,820**.
- **20-partner LP, return filed 6 months late:** 20 × $245 × 6 = **$29,400**.

The penalty scales linearly with partner count. A 50-partner FLP filed 12 months late owes **$147,000** in §6698 penalties — for a return showing zero tax.

### 4.3 Reasonable cause relief — Rev. Proc. 84-35

- **Rev. Proc. 84-35 safe harbor** — Rev. Proc. 84-35 has long provided a "safe harbor" for small partnerships (10 or fewer partners, all individuals or estates of deceased partners, each partner reporting their share). The IRS has periodically suggested this safe harbor is outdated post-CPAR, but as of 2025 it remains administratively available in practice. Do not rely on it without documenting reasonable cause (e.g., illness, records destroyed, reasonable reliance on a return preparer).  _(Rev. Proc. 84-35)_
- **First-Time Abatement limitation** — The First-Time Abatement (FTA) administrative waiver is generally not available for §6698 because the partnership does not have a "tax" balance for FTA purposes (FTA applies to assessable penalties on returns showing tax). However, some IRS units have granted it; document any request carefully.  _(§6698)_

### 4.4 Other related penalties

- **§6699 late Form 1120-S penalty** — $255/shareholder/month for late Form 1120-S for 2025 (not applicable here, but reviewer should not confuse the two)  _(§6699)_
- **§6722 failure to furnish correct K-1 to partner** — graduated penalties ($60 / $130 / $340 per K-1 for 2025, depending on lateness; verify against current §6721/§6722 schedule)  _(§6722)_
- **§6721 failure to file correct K-1 with IRS** — same graduated structure  _(§6721)_
- **§6707A listed-transaction disclosure failures** — rare  _(§6707A)_
- **§6722 exposure despite timely 1065** — A partnership that files Form 1065 on time but fails to furnish K-1s to partners can still be hit with §6722 penalties. Best practice: K-1s out the same day as the return is filed.  _(§6722)_

### 5.1 The 2020+ requirement

- **Tax basis method requirement on Item L** — Beginning with tax year 2020 (Notice 2020-43 → final instructions for 2020 Form 1065), partnerships must report each partner's capital account on Schedule K-1 Item L using the tax basis method. GAAP, §704(b) book, and "other" methods are no longer permitted on Item L. (A partnership may still maintain §704(b) capital accounts internally to track substantial economic effect — see §11 — but Item L itself must be tax basis.)  _(Notice 2020-43)_

### 5.2 What is a tax basis capital account

- **Tax basis capital account vs outside basis** — A partner's tax basis capital account ≠ the partner's outside basis. The two differ by: The partner's share of partnership liabilities under §752 (included in outside basis, not in tax basis capital); §743(b) basis adjustments (in outside basis only); Built-in gain/loss inherited from contributing partner under §704(c) (the contributing partner's capital reflects FMV at contribution net of §704(c) gain not yet recognized; outside basis reflects historic carryover)  _(§752; §743(b); §704(c))_
- **K-1 Item L rollforward** — Beginning capital account + Capital contributed during the year (cash + tax basis of contributed property) + Current year net income (loss) — tax basis + Other increases (e.g., §734(b) adjustments to common basis on certain distributions) − Withdrawals and distributions (cash + tax basis of distributed property) − Other decreases = Ending capital account  _(§734(b))_

### 5.3 Transition for partnerships still on §704(b)/GAAP

- **Three transition methods** — If a partnership is being prepared for the first time post-2020 and historical capital was tracked on §704(b) or GAAP, the 2020 instructions provided three transition methods: 1. Modified outside basis method — partner's outside basis minus their share of liabilities minus §743(b) adjustments; 2. Modified previously taxed capital method — based on the §743(b) hypothetical liquidation; 3. §704(b) method — §704(b) capital minus §704(c) built-in gain/loss layers. For 2025 returns, the partnership should have completed the transition years ago. If the working papers still show §704(b) capital and no tax basis rollforward exists, stop and surface to reviewer — this is not a v0.1 automation case.  _(§743(b); §704(b); §704(c))_

### 5.4 Negative tax basis capital

- **Negative tax basis capital disclosure and gain trigger** — A negative tax basis capital account does not by itself mean a partner has gain; outside basis (which includes liability share) can still be positive. But it is a flag. Since 2018 (for tax years 2018+), partnerships have had to disclose negative tax capital on Item L (or on a separate statement in earlier years). For 2025, negative tax capital is reported directly on K-1 Item L line "Current year net income (loss)" and "Ending capital account." A partner with negative tax basis capital and a distribution that exceeds outside basis recognizes gain under §731(a)(1). The skill flags this for the reviewer when distributions in Item J/L exceed the available basis.  _(§731(a)(1))_

### 6.1 Conceptual difference

- **Schedule K vs K-1 concept and reconciliation** — Schedule K is the partnership-level summary of all separately stated items. Lines 1–21 of Schedule K aggregate every partner's share of ordinary business income, separately stated items (interest, dividends, §1231 gain, §179, charitable contributions, etc.), credits, foreign items, and other. Schedule K-1 is each individual partner's share of those Schedule K items, allocated according to the partnership agreement (subject to §704(b) substantial economic effect). The sum of all K-1s for any given line must equal the corresponding Schedule K line. Reviewer reconciliation: K-1 line totals === K line totals, partner by partner. Any discrepancy is a preparer error.  _(§704(b))_

### 6.2 K-1 boxes (2025 layout)

The 2025 Schedule K-1 (Form 1065) has the following major sections:

- **Part I** — Partnership information (EIN, name, address, IRS Service Center, PTP indicator)
- **Part II** — Partner information:
  - Item E: Partner's identifying number
  - Item F: Partner's name and address
  - Item G: General partner / LLC member-manager **vs** Limited partner / other LLC member (Critical for SE — see §13)
  - Item H1/H2: Domestic / Foreign partner
  - Item I1/I2: Entity type (Individual / Corporation / Partnership / Trust / DRE / Estate / Exempt org / Foreign government / Nominee / IRA)
  - Item J: Partner's share of profit / loss / capital — beginning and ending percentages
  - Item K: Partner's share of liabilities (nonrecourse / qualified nonrecourse / recourse) — §752
  - Item L: Capital account analysis — tax basis (see §5)
  - Item M: Did partner contribute property with built-in gain or loss? (§704(c) flag)
  - Item N: Partner's share of net unrecognized §704(c) gain or loss — beginning and ending
- **Part III** — Partner's share of income, deductions, credits:
  - Box 1: Ordinary business income (loss)
  - Box 2: Net rental real estate income (loss)
  - Box 3: Other net rental income (loss)
  - Box 4a/4b/4c: Guaranteed payments (services / capital / total)
  - Box 5: Interest income
  - Box 6a/6b/6c: Ordinary / qualified / dividend equivalents
  - Box 7: Royalties
  - Box 8: Net short-term capital gain (loss)
  - Box 9a/9b/9c: Long-term capital gain (loss) / collectibles / unrecaptured §1250
  - Box 10: Net §1231 gain (loss)
  - Box 11: Other income (loss) — coded
  - Box 12: §179 deduction
  - Box 13: Other deductions — coded (includes charitable contributions, investment interest, etc.)
  - Box 14: SE earnings (loss) — A: net SE earnings, B: gross farming, C: gross non-farm
  - Box 15: Credits — coded
  - Box 16: Schedule K-3 attached indicator (replaced the old foreign-transactions box)
  - Box 17: AMT items — coded
  - Box 18: Tax-exempt income & nondeductible expenses — coded
  - Box 19: Distributions — coded (A: cash & marketable securities; B: distribution of property subject to §737; C: other property)
  - Box 20: Other information — coded (the catch-all; includes §199A QBI codes Z/AA/AB/AC/AD, §163(j) interest limit info, §453A interest, §704(c) information, etc.)
  - Box 21: Foreign taxes paid or accrued — new for 2023+; carried to Schedule K-3
  - Box 22: More than one activity for at-risk purposes (check box)
  - Box 23: More than one activity for passive activity purposes (check box)

### 6.3 §199A QBI codes (Box 20)

- **§199A codes and Box 20 content** — For 2025 returns, §199A items flow to partners through Box 20 under Code Z: QBI, W-2 wages, UBIA of qualified property, REIT dividends, PTP income, the SSTB indicator, and aggregation information are all reported in a single attached statement. The legacy AA/AB/AC/AD §199A sub-codes no longer apply; for 2025, Box 20 Code AA carries §704(c) information for non-PTP partnerships. Box 20 must carry, in a clear statement attached to the K-1: QBI from the partnership's trade or business (for each separate trade or business if the partnership has multiple); W-2 wages allocated to that trade or business; UBIA (unadjusted basis immediately after acquisition) of qualified property; Whether the trade or business is an SSTB (Specified Service Trade or Business under §199A(d)(2)); Aggregation under Reg. §1.199A-4 if the partnership has made an aggregation election; Section 199A REIT dividends received; Section 199A PTP income received (from any underlying PTPs the partnership invested in). New for 2025: Box 20 Code ZZ reports the information partners need to elect to pay tax on gain from the sale of qualified farmland property in four equal annual installments, including a copy of the required covenant (new IRC § 1062, added by OBBBA § 70437). Defer the partner-level QBI computation to us-qbi-deduction. The partnership's job is to supply complete and accurate Box 20 statements; the partner's 1040 preparer takes it from there.  _(§199A(d)(2); Reg. §1.199A-4)_

### 6.4 Self-Employment Earnings — Box 14

- **Box 14 SE earnings mechanics by partner type** — Box 14, code A, reports net SE earnings allocable to the partner. This is the most aggressively examined K-1 line in 2024–2025 IRS practice — see §13. For a general partner (Item G "General partner or LLC member-manager"): Box 14A typically equals the partner's distributive share of ordinary business income (Box 1) plus guaranteed payments for services (Box 4a), adjusted for items not subject to SE (e.g., rental real estate, portfolio income, §1231 gain). For a limited partner (Item G "Limited partner or other LLC member"): historically Box 14A includes only guaranteed payments for services, per §1402(a)(13). Post-Soroban (see §13.3), this position is under attack for LLC member-managers and limited partners who materially participate.  _(§1402(a)(13))_

### 6.5 Reconciliation check

- **Reviewer per-line reconciliation test** — Reviewer test: Σ over all K-1s of (Box 1 + Box 4a + Box 4b + Box 5 + Box 6a + Box 7 + Box 8 + Box 9a + Box 10 + Box 11 + …) − (Box 12 + Box 13 +  …) should reconcile to Schedule K. The skill produces a per-line reconciliation table in the reviewer brief.

### 7.1 What they are

- **Schedules K-2 and K-3 overview** — Schedules K-2 and K-3 were introduced for tax year 2021 to replace the old K-1 Box 16 free-text reporting of international items. They are voluminous (Schedule K-2 ran ~19 pages in 2021; the partner-by-partner K-3 ran similarly per partner). Schedule K-2 — partnership-level summary of international items. Filed with Form 1065. Schedule K-3 — per-partner detail. One K-3 per partner who needs international information. Furnished to the partner. The schedules have eleven parts in 2025: Part I — Partnership's other current-year international information; Part II — Foreign tax credit limitation (categories of income, source-of-income); Part III — Other information for preparation of Form 1116 or 1118 (deductions allocable to foreign income); Part IV — §250 deduction (FDII / GILTI / §163(j) interactions); Part V — Distributions from foreign corporations (§959, §961, etc.); Part VI — Information on partners' §951(a) inclusions; Part VII — §965 transition tax (mostly residual / closing accounts); Part VIII — Section 871(m) / dividend equivalents; Part IX — Section 1446 withholding (foreign partners); Part X — Foreign partners' character & source of income; Part XI — Section 871(m), Schedule K-3 supplemental.  _(§250; §959; §961; §951(a); §965; §871(m); §1446)_

### 7.2 Who must file K-2/K-3

- **K-2/K-3 filing triggers** — A partnership must file K-2/K-3 if it has any of the following: 1. Items of international tax relevance — foreign-source income, foreign taxes paid, foreign assets, foreign branch operations, CFC interests, PFIC interests, §250 items, etc. 2. Foreign partners — even with zero foreign-source activity, a foreign partner needs K-3 for their own US filing. 3. A US partner who is eligible to claim a foreign tax credit and requests K-3 information (see §7.3 Domestic Filing Exception).

### 7.3 The Domestic Filing Exception

- **Four conditions of Domestic Filing Exception** — Beginning with tax year 2022 (and refined for 2023+ in the K-2/K-3 instructions), partnerships meeting all four of the following do not need to file K-2/K-3: 1. No or limited foreign activity — the partnership has no foreign-source income, no foreign taxes paid or accrued, and no ownership in any foreign entity, OR foreign activity is below the de minimis thresholds in the instructions (e.g., < $300 of foreign passive income with < $20 of foreign tax). 2. All direct partners are eligible US persons — US citizens, resident aliens, domestic decedents' estates, certain domestic trusts, S corporations with eligible shareholders, single-member LLCs whose sole owner is one of the above. No foreign partners, no partnerships as partners (other than as nominees), no domestic partnerships (except where treated as a nominee partner), no domestic partnerships in multi-tier structures. 3. Partner notification — by January 15 of the year following the tax year (so by January 15, 2026 for tax year 2025), the partnership has notified each partner that it will not provide a Schedule K-3 unless requested. Notification can be embedded in the K-1 footer in many practice templates. 4. No partner has requested K-3 — by the "1-month date" (one month before the partnership files Form 1065, or one month before the extended due date if extending), no partner has requested a K-3 from the partnership in writing. If all four are met, the partnership may omit K-2/K-3. If any one fails, K-2/K-3 must be filed.

### 7.4 The "1-month date" trap

- **1-month date timing rule** — If a partner requests K-3 information after the partnership files Form 1065 but before the original or extended due date, the partnership must furnish that partner's K-3 but is not required to file Schedule K-2 with the IRS. If a partner requests K-3 before the 1-month date, the partnership must file the full K-2 with the IRS. Practitioners should solicit K-3 requests early (e.g., in November/December of the tax year) to know what they're filing.

### 7.5 Practical guidance

- **Default to preparing K-2/K-3** — Even a fully domestic two-person LLC may need K-2/K-3 if it owns a foreign mutual fund through a brokerage account that pays foreign withholding. The Domestic Filing Exception is narrower than it first appears. Default to preparing K-2/K-3 unless the intake form affirmatively confirms all four conditions of the Domestic Filing Exception.

### 8.1 Statutory background

- **CPAR origin and codification** — The Bipartisan Budget Act of 2015 (BBA) repealed the TEFRA partnership audit rules and the Electing Large Partnership rules and replaced them with the Centralized Partnership Audit Regime (CPAR), effective for tax years beginning after December 31, 2017. CPAR is codified in §§6221–6241.  _(§§6221–6241)_

### 8.2 Default mechanics

- **CPAR default audit mechanics** — Under CPAR, an IRS audit of a partnership return results in: 1. Determination of an "imputed underpayment" at the partnership level for the reviewed year (the year being audited). 2. The imputed underpayment is assessed against and collected from the partnership in the adjustment year (the year the audit concludes), at the highest individual or corporate rate (37% for individuals in 2025 / 21% for C corps; the partnership default uses the highest applicable rate). 3. Current-year partners bear the economic burden — even if they were not partners in the reviewed year. This is the default. It is harsh and often inappropriate when the partner roster has changed. The statute provides two safety valves: Section 6226 push-out election — within 45 days of the final partnership adjustment, the partnership can elect to push the adjustment out to the reviewed-year partners, who report the adjustment on their own returns for the adjustment year (with interest at AFR + 2%). The reviewed-year partners then pay, not the partnership. Modification of imputed underpayment under §6225(c) — e.g., tax-exempt partners' allocable share is removed, lower rates for C corp partners' share, etc. Election out of CPAR entirely — Schedule B-2 (see §9).  _(§6226; §6225(c))_

### 8.3 Partnership Representative (PR) — §6223

- **PR designation and authority** — Every BBA partnership must designate a Partnership Representative (PR) for each tax year on Form 1065. The PR replaces the old TEFRA Tax Matters Partner (TMP). Differences: The PR does not have to be a partner. Any person (or entity) with a substantial US presence may serve. If the PR is an entity, the partnership must also name a Designated Individual to act on behalf of the entity. The PR's authority is absolute — the PR's actions bind the partnership and all partners for the relevant tax year. Other partners do not have a statutory right to participate in or contest the PR's actions in the audit. The PR is designated on Form 1065, Schedule B, page 3 (2025 layout), with name, US TIN, US address, and US daytime phone. If the PR is an entity, the Designated Individual's info goes alongside. The PR for one year can be different from the PR for another year. Changes mid-cycle require Form 8979.  _(§6223)_

### 8.4 Audit-year vs reviewed-year — terminology

- **Reviewed year, adjustment year, partnership-level resolution** — Reviewed year = the tax year the IRS is examining. Adjustment year = the year the audit is finalized and the imputed underpayment is assessed. Partnership-level resolution = audit outcome before any push-out election. These terms are statutory and the reviewer brief should use them consistently.

### 9.1 Who can elect out

- **§6221(b) election-out eligibility** — Under §6221(b), a partnership may elect out of CPAR for a tax year if it has 100 or fewer partners at any point during the tax year and every partner is an "eligible partner." Eligible partners are: Individuals; C corporations (and foreign entities that would be C corporations if domestic); S corporations (each S-corp shareholder is counted toward the 100-partner limit); Estates of deceased partners; Certain other eligible categories per the regulations (Reg. §301.6221(b)-1). Ineligible partners (any one of which destroys election-out eligibility): Partnerships (any tier — no upper-tier partnerships allowed; this is the most common disqualifier); Trusts (including grantor trusts, in most cases — verify against Reg. §301.6221(b)-1 for the limited exceptions); Disregarded entities (DREs) — except the regulations carve out an SMLLC owned by an eligible individual under Reg. §301.6221(b)-1(b)(3)(ii) (verify against current regs; treatment has been clarified over time); Nominees and similar agents that are not the beneficial owner; IRAs (treated as exempt trusts); Foreign entities that are not C-corp-equivalent.  _(§6221(b); Reg. §301.6221(b)-1)_

### 9.2 Counting partners

- **S-corp partner and spousal counting rule** — S-corporation partners count as one partner + one for each shareholder of the S-corporation for the 100-partner threshold under §6221(b)(2). Spouses each count separately. A husband-and-wife LLC is two partners (one for each spouse), not one.  _(§6221(b)(2))_

### 9.3 Schedule B-2 mechanics

- **Schedule B-2 content and annual re-election** — Schedule B-2 is a one-page statement filed with Form 1065. It lists, by partner: Partner name; Partner US TIN; Partner type (individual / C corp / S corp / estate / eligible foreign entity); For S corp partners, the number and identity of S-corp shareholders. The election out is annual — it must be re-made every year on each year's Form 1065. A partnership that elected out for 2024 must elect out again for 2025 by attaching Schedule B-2.

### 9.4 When to elect out

**Pros of electing out:**

- Audits go partner-by-partner under pre-TEFRA rules
- No PR with absolute authority
- No imputed underpayment at partnership level
- Each partner gets their own statute of limitations

**Cons of electing out:**

- Each partner audited separately — more administrative burden if multiple partners are examined
- No push-out election available (the entity isn't in CPAR to begin with)
- Refunds for over-payments must be claimed by each partner on amended 1040s, not by the partnership

**Reviewer recommendation framework:**

- Small, stable partnership (≤10 individual partners, no S-corp partners, no foreign partners, no trusts): elect out
- Partnership with frequent partner changes: lean CPAR (push-out available)
- Partnership with any ineligible partner: cannot elect out
- Partnership with state PTET election: confirm state rules don't depend on CPAR status

### 10.1 Designation requirements

- **PR designation requirements** — §6223 and Reg. §301.6223-1(b)(2): Must have a substantial presence in the United States — a US address, a US phone, and reasonable availability to meet with the IRS in the US. Must have the capacity to act — not a minor, not incapacitated, not deceased. Must be designated on Form 1065 each tax year (separately from the PR designation for any other year).  _(§6223; Reg. §301.6223-1(b)(2))_

### 10.2 Designated Individual

- **Designated Individual (DI) requirement** — If the PR is an entity (e.g., a CPA firm, the LLC's parent entity, a designated PR-services company), the partnership must also designate a Designated Individual (DI) who will act on behalf of the entity PR. The DI must meet the same substantial-presence requirements.

### 10.3 Changing the PR

- **Form 8979 PR change** — The partnership can change the PR by filing Form 8979 with the IRS. The change is generally effective only prospectively — it cannot be done in the middle of an audit to escape an unfavorable PR's decisions. The IRS can also designate a PR if the partnership has not done so or the designated PR is not eligible.  _(Form 8979)_

### 10.4 Reviewer brief content

The reviewer brief should include:

- PR name, TIN, address, phone (and DI if applicable)
- Confirmation that the PR has signed an internal acknowledgment of duties (best practice — not statutorily required)
- Whether the partnership agreement addresses PR appointment, indemnification, and procedure
- Whether the partnership has made the Schedule B-2 election out (in which case PR designation is still required on Form 1065 but the PR's CPAR authority does not apply because the partnership is not in CPAR for that year)

### 11.1 The allocation problem

- **§704(a)/(b) allocation reallocation rule** — §704(a) says that a partner's distributive share of income, gain, loss, deduction, or credit is determined by the partnership agreement. But §704(b)(2) provides that if the allocation doesn't have substantial economic effect (or otherwise lack a permissible basis), it will be reallocated according to the partner's interest in the partnership (PIP). §704(b) and Reg. §1.704-1(b)(2) lay out the safe harbor for "substantial economic effect":  _(§704(a); §704(b)(2); Reg. §1.704-1(b)(2))_

### 11.2 The three-part test for "economic effect"

- **Three-part economic effect test** — To have economic effect, an allocation must satisfy all three of the basic test under Reg. §1.704-1(b)(2)(ii)(b): 1. Capital accounts maintained per Reg. §1.704-1(b)(2)(iv) — the §704(b) "book" capital account rules. (Distinct from tax basis capital — see §5.) 2. Liquidation by capital account balances — upon liquidation of the partnership (or of a partner's interest), distributions must be made in accordance with positive §704(b) capital account balances. 3. Deficit restoration obligation (DRO) — a partner with a negative §704(b) capital account at liquidation must be unconditionally obligated to restore the deficit. If a partner has no DRO, allocations can still have economic effect under the alternate test if the partnership agreement contains a qualified income offset (QIO) — a provision that allocates income to that partner as quickly as possible to restore a negative capital account caused by certain "unexpected" events.  _(Reg. §1.704-1(b)(2)(ii)(b); Reg. §1.704-1(b)(2)(iv))_

### 11.3 Substantiality

- **Substantiality test elements** — Even an allocation with economic effect must be substantial — meaning it must have a non-tax economic consequence to the partners independent of tax effects. Reg. §1.704-1(b)(2)(iii) outlines: Overall tax effect — the allocation must have a reasonable possibility of substantially affecting the dollar amounts to be received by the partners apart from tax consequences; Shifting — allocations that merely shift tax burden among partners with offsetting non-tax economic effects (e.g., character of income shifting) are presumed non-substantial; Transitory — allocations whose effects are offset within five years are presumed non-substantial.  _(Reg. §1.704-1(b)(2)(iii))_

### 11.4 PIP fallback

- **Partner's interest in the partnership fallback factors** — If allocations fail substantial economic effect, the IRS reallocates per partner's interest in the partnership (PIP), considering: Partners' relative contributions; Partners' interests in economic profits and losses; Partners' interests in cash flow and other non-liquidating distributions; Partners' rights to distributions of capital upon liquidation.

### 11.5 What this skill does and doesn't do

- **Scope of §704(b) allocation flagging** — This skill does not redesign allocation provisions. It accepts the partnership agreement as given and applies allocations. But it does flag: Allocations that lack the three-part economic effect test (e.g., LLC operating agreement liquidates by units owned rather than by capital account); Special allocations that lack a stated business purpose; Loss allocations that drive a partner below zero §704(b) capital without a DRO and without a QIO; §704(b) capital accounts that have not been maintained at all (very common in small LLC practice — needs reviewer attention). When any flag fires, the skill surfaces the issue to the reviewer for partnership counsel input. It does not "fix" the allocation silently.

### 12.1 The rule

- **§704(c) built-in gain/loss allocation requirement** — §704(c) requires that income, gain, loss, and deduction with respect to property contributed by a partner to a partnership be allocated among the partners so as to take account of the variation between the basis of the property to the partnership and its fair market value at the time of contribution. In short: built-in gain or loss attaches to the contributing partner.  _(§704(c))_

### 12.2 The three §704(c) methods

- **Traditional, curative, and remedial methods** — Reg. §1.704-3 allows partnerships to choose, on a property-by-property basis, among: 1. Traditional method — depreciation and disposition gain/loss are allocated to "true up" the contributor and the non-contributors, but only to the extent of tax items. The "ceiling rule" caps allocations at the actual tax depreciation or gain available — meaning if tax depreciation is less than book depreciation, the non-contributing partner is shortchanged and the contributing partner gets a windfall. 2. Traditional method with curative allocations — same as traditional, but the partnership can make a "curative" allocation of other items (e.g., unrelated ordinary income) to make the non-contributing partner whole. 3. Remedial method — the partnership creates "remedial" items (notional income to the contributing partner, notional deduction to the non-contributing partner) to fully eliminate the ceiling rule effects. The most accurate, the most complex.  _(Reg. §1.704-3)_

### 12.3 §704(c) layers and "forward" / "reverse" §704(c)

- **Forward vs reverse §704(c)** — Forward §704(c) — property contributed at inception or by a new partner; built-in gain/loss as of contribution date. Reverse §704(c) — when the partnership revalues its books (a "book-up" or "book-down") under Reg. §1.704-1(b)(2)(iv)(f) — e.g., on a new partner entering at FMV, on a non-pro-rata distribution, on a grant of a profits interest under Rev. Proc. 93-27 — the §704(b) book values change but tax basis does not. The resulting variation creates a "reverse" §704(c) layer with respect to the historic partners. Multiple layers accumulate over the life of a partnership. Real estate partnerships with multiple book-ups can have very complex §704(c) accounting.  _(Reg. §1.704-1(b)(2)(iv)(f); Rev. Proc. 93-27)_

### 12.4 Disclosure on K-1

- **§704(c) K-1 disclosure items** — Item M asks whether the partner contributed property with a built-in gain or loss. Item N reports the partner's share of net unrecognized §704(c) gain or loss at both the beginning and the end of the tax year (required for 2025). If the partnership's taxable income is affected by §704(c) allocations, the sum of those items is reported in Box 20 with Code AA for non-PTP partnerships (Instructions for Form 1065 (2025), Item N and Box 20 Code AA).

### 12.5 What this skill does

- **Scope of §704(c) flagging** — This skill flags contributions of appreciated or depreciated property and reports Item M, Item N, and the Box 20 §704(c) statement at the level supported by the working papers. It does not select among methods — that's a partnership-agreement decision. If the working papers indicate property was contributed at a basis differing from §704(b) book value and no §704(c) method has been documented, the skill stops and surfaces to the reviewer.

### 13.1 Why it matters

- **§752(a)/(b) basis and distribution treatment** — §752(a) treats an increase in a partner's share of partnership liabilities as a contribution of cash by that partner (increasing outside basis). §752(b) treats a decrease as a deemed distribution of cash (decreasing outside basis, potentially triggering gain under §731). Without liability sharing, a partner could never deduct losses funded by partnership debt.  _(§752(a); §752(b); §731)_

### 13.2 The three categories

- **Recourse, nonrecourse, and QNF liability categories** — Reg. §1.752-1 through -3: 1. Recourse liabilities — a partnership liability is recourse to the extent any partner (or related person) bears the economic risk of loss (EROL). The partner who bears EROL is allocated 100% of the recourse liability for §752 purposes. EROL is determined by a constructive liquidation analysis under Reg. §1.752-2. 2. Nonrecourse liabilities — no partner bears EROL. Allocated under the three-tier rule of Reg. §1.752-3: Tier 1: Partner's share of partnership minimum gain (§704(b) book gain that would result from a §752(b) deemed disposition of property securing the nonrecourse debt); Tier 2: §704(c) built-in gain on contributed property secured by the debt (to the contributing partner); Tier 3: Excess nonrecourse liabilities — allocated per the partnership agreement (subject to certain constraints). 3. Qualified nonrecourse financing (QNF) under §465(b)(6) — nonrecourse debt from a qualified lender (a bank, etc., not the seller or a related person) secured by real property held in the trade or business of holding real property. Treated as "at-risk" for §465 purposes (see §14.2).  _(Reg. §1.752-1; Reg. §1.752-2; Reg. §1.752-3; §465(b)(6))_

### 13.3 LLC practice — almost everything is nonrecourse

- **LLC debt classification and guarantee planning** — Because LLC members are not personally liable for LLC debts, most LLC debt is nonrecourse for §752 purposes — even when commercial-law recourse. The exception is when a member guarantees the debt (creating EROL for the guaranteeing member). For a typical two-member LLC with bank financing where neither member guarantees, the debt is allocated 50/50 (Tier 3 — per the partnership agreement profit-sharing ratio, absent a special allocation). For a guaranteed loan, the guaranteeing member is allocated 100% of the debt. This is a common "basis planning" technique — one partner takes a personal guarantee specifically to get the outside basis to deduct losses.

### 13.4 K-1 Item K

- **Item K liability reporting** — Item K on K-1 reports each partner's share of: Nonrecourse liabilities; Qualified nonrecourse financing; Recourse liabilities. …at the beginning and end of the year. Reviewer reconciliation: Σ over all K-1s of each category = the partnership's total of that category.

### 13.5 What this skill does

- **§752 skill scope** — The skill: Classifies each partnership liability as recourse / nonrecourse / QNF based on the loan documents and EROL analysis; Allocates recourse debt to the partner(s) bearing EROL; Allocates nonrecourse debt under the three-tier rule; Reports Item K; Flags any partner whose outside basis (including §752 share) is insufficient to absorb the year's allocated loss — see §14.

### 14.1 §704(d) — outside basis limit

- **Outside basis limit and components** — A partner cannot deduct partnership losses in excess of their outside basis at the end of the tax year. Excess loss is suspended and carried forward until basis is restored. Outside basis components (a partial list): Initial contributions (cash + adjusted basis of property contributed); Share of partnership liabilities under §752 (added); Allocable share of partnership income (including tax-exempt income); Less: distributions (cash + adjusted basis of property distributed); Less: allocable share of partnership loss and nondeductible expenses; Less: §743(b) basis adjustments (in/out depending on direction). The partnership itself does not track partner outside basis (that's the partner's job). But the partnership produces all the inputs on K-1. Best practice: include a partner-outside-basis worksheet with the K-1 package as a service to the partner, even though it is not statutorily required. For 2018+, the IRS requires partners with outside basis loss limitation issues to file Form 7203 (for S corps) — no equivalent partnership form exists, but Form 6198 (at-risk) and Form 8582 (passive) interact.  _(§704(d); §752; §743(b))_

### 14.2 §465 — at-risk limit

- **At-risk limit and nonrecourse debt exclusion** — §465 further limits losses to the amount the partner is "at risk" — generally cash contributed + adjusted basis of contributed property + recourse debt allocated under §752 + qualified nonrecourse financing. Nonrecourse debt (other than QNF) is NOT at-risk. Result: an LLC member can have outside basis (because nonrecourse debt is included under §752) but no at-risk amount (because nonrecourse debt other than QNF is not at-risk). The loss clears §704(d) but is suspended under §465. Box 22 on K-1 — "more than one activity for at-risk purposes" — is checked when the partnership has more than one activity. The partner must compute at-risk on Form 6198 separately for each activity.  _(§465; §752; §704(d))_

### 14.3 §469 — passive activity loss limit

- **Passive activity loss limit and participation tests** — §469 limits passive activity losses to passive activity income. A loss that clears §704(d) and §465 may still be suspended under §469 if the activity is "passive" with respect to the partner. A limited partner's interest in a partnership is presumptively passive (Reg. §1.469-5T(e)(3)) — though three exceptions allow limited partners to qualify as materially participating in specific factual circumstances. An LLC member's interest — the case law is mixed (Garnett, Thompson, etc.). The IRS abandoned its strict "all LLC members are limited partners" position after losing in Garnett. Today, LLC members can demonstrate material participation under any of the seven tests in Reg. §1.469-5T(a). Rental activities are per se passive under §469(c)(2), with two exceptions: real estate professionals (§469(c)(7)) and short-term rentals (where average customer use is ≤ 7 days, taking it out of the rental category). Box 23 on K-1 — "more than one activity for passive activity purposes" — is checked when the partnership has more than one activity. The partner aggregates on Form 8582.  _(§469; Reg. §1.469-5T(e)(3); Reg. §1.469-5T(a); §469(c)(2); §469(c)(7))_

### 14.4 §461(l) — excess business loss

- **§461(l) excess business loss threshold for 2025** — approximately $313,000 single / $626,000 MFJ — verify against Rev. Proc. 2024-40 USD (2025, inflation-adjusted, applies at partner level)  _(§461(l); P.L. 119-21 (OBBBA); Rev. Proc. 2024-40)_

### 14.5 Ordering rules

- **Loss limitation ordering** — Losses are tested in the following order at the partner level: 1. §704(d) outside basis limit; 2. §465 at-risk limit; 3. §469 passive activity limit; 4. §461(l) excess business loss limit. The partnership produces the K-1; the partner runs through the ordering on their own 1040.  _(§704(d); §465; §469; §461(l))_

### 15.1 General partners

- **SE tax rates on general partner distributive share** — 12.4% OASDI up to the SS wage base of $176,100 for 2025, 2.9% Medicare on all SE earnings, plus 0.9% Additional Medicare on SE earnings above the §1401(b)(2) thresholds percent (2025 SS wage base $176,100)  _(§1402(a); §1401(b)(2))_
- **Guaranteed payments subject to SE tax** — Guaranteed payments under §707(c) for services are also subject to SE tax — for general partners and limited partners alike (see §15.2).  _(§707(c))_

### 15.2 Limited partners — §1402(a)(13)

- **Limited partner SE exclusion** — §1402(a)(13) excludes from net SE earnings: the distributive share of any item of income or loss of a limited partner, as such, other than guaranteed payments described in §707(c) to that partner for services actually rendered to or on behalf of the partnership to the extent that those payments are established to be in the nature of remuneration for those services. So a limited partner has: SE tax YES on guaranteed payments for services; SE tax NO on distributive share. This rule was enacted in 1977 when "limited partner" had a clear meaning under state law (a non-managing investor with limited liability). It has not been updated to reflect modern LLCs, LLPs, and LP-with-active-LP structures.  _(§1402(a)(13); §707(c))_

### 15.3 The Soroban Capital Partners case (2023)

- **Soroban functional test for limited partner exception** — In Soroban Capital Partners LP v. Commissioner, 161 T.C. No. 12 (November 28, 2023), the Tax Court held that the §1402(a)(13) "limited partner" exception is functional, not formal. A partner labeled a "limited partner" under state law is not automatically a limited partner for §1402(a)(13) purposes if they actively participate in the partnership's business. The Court applied a facts-and-circumstances test focused on the partner's actual role. In Soroban itself, the LPs of an investment-management LP performed substantial services (managing the funds, sourcing investments, client-facing work) and the Court held their distributive shares were subject to SE tax. The IRS has since pursued similar positions against fund managers and operating LPs.  _(Soroban Capital Partners LP v. Commissioner, 161 T.C. No. 12 (November 28, 2023))_

### 15.4 Post-Soroban posture for 2025 returns

- **Recommended conservative SE position and alternatives** — The IRS treats §1402(a)(13) as available only to truly passive limited partners. For working LP/LLC members: Conservative position (recommended for 2025 returns): subject the distributive share to SE tax to the extent it reflects compensation for services. This may mean a partial inclusion — e.g., the portion in excess of a reasonable return on capital is SE income. Aggressive position: continue to rely on §1402(a)(13) for state-law limited partners. High risk of audit; reviewer must confirm and document. Hybrid position (proposed Regs. 1.1402(a)-2, never finalized — the "1997 proposed regulations"): treat a partner as a "limited partner" only if (i) the partner has no personal liability for partnership debts, (ii) the partner has no authority to contract for the partnership, and (iii) the partner does not provide more than 500 hours of service per year. Many practitioners follow this informally. This skill flags any partner labeled limited but apparently providing material services and asks the reviewer to confirm SE treatment. The default Box 14A computation for limited partners includes only guaranteed payments for services; any deviation requires reviewer sign-off and documentation.  _(§1402(a)(13); proposed Regs. 1.1402(a)-2)_

### 15.5 LLC member-managers

- **LLC member-manager SE treatment** — LLC member-managers are treated more like general partners for SE purposes. The IRS position (and most practitioner consensus) is that an LLC member who participates in management has SE income on their distributive share.

### 15.6 Box 14 mechanics

- **Box 14 codes and SE exclusions** — Box 14, code A: net SE earnings (loss) — the partner's share of partnership SE income. Box 14, code B: gross farming or fishing income (for §1402 optional method). Box 14, code C: gross non-farm income (for §1402 optional method). Excluded from SE income (regardless of partner type): Rental real estate income (§1402(a)(1)); Dividends and interest not derived in the ordinary course of trade or business (§1402(a)(2)); Gain or loss on disposition of property other than inventory (§1402(a)(3)); §1231 gain; Capital gain.  _(§1402(a)(1); §1402(a)(2); §1402(a)(3))_

## 16. §199A QBI Passthrough on K-1

### 16.1 Background

- **§199A QBI deduction rate for tax year 2025** — 20% percent (tax years beginning after Dec 31, 2024)  _(§199A, OBBBA P.L. 119-21 §70105)_
- **§199A QBI deduction rate for tax year 2026+** — 20% (OBBBA § 70105 made § 199A permanent at 20%; the enacted law did not adopt the proposed 23% rate. From 2026 it also adds a $400 minimum deduction, inflation-adjusted, for applicable taxpayers with at least $1,000 of aggregate active QBI) percent (tax years beginning after Dec 31, 2025)  _(OBBBA P.L. 119-21 §70105)_
- **§199A deduction** — Provides a deduction up to 20% of qualified business income (QBI) from a domestic trade or business operated as a sole proprietorship, partnership, S corporation, trust, or estate. For partnerships, QBI flows out to partners on K-1.  _(§199A (enacted by TCJA, made permanent at 20% by OBBBA P.L. 119-21 §70105))_

### 16.2 What the partnership reports

- **Partnership §199A reporting items** — The partnership must report, separately for each trade or business it operates (and for each underlying RPE it invests in): QBI (net qualified items of income, gain, deduction, loss); W-2 wages properly allocable, computed under Notice 2018-64 method (1, 2, or 3); UBIA of qualified property; SSTB indicator (health, law, accounting, actuarial, performing arts, consulting, athletics, financial services, investing/investment management, trading, dealing in securities, or any business where principal asset is reputation or skill of employees/owners); REIT dividends; PTP income; Aggregation if aggregated under Reg. §1.199A-4. These flow to K-1 Box 20 under Code Z in a single attached statement (Instructions for Form 1065 (2025); the legacy AA/AB/AC/AD §199A sub-codes no longer apply, and Code AA now carries §704(c) information).  _(Reg. §1.199A-4; Notice 2018-64)_

### 16.3 What the partner does

- **Partner-level §199A computation** — The partner computes the §199A deduction on their own Form 1040 using Form 8995 (simplified — under threshold) or Form 8995-A (full method — over threshold). See `us-qbi-deduction` skill. The partnership does not compute the partner's QBI deduction. It only supplies the inputs.  _(Form 8995 / Form 8995-A)_

### 16.4 Aggregation election

- **§1.199A-4(b)(1) aggregation election requirements** — If the partnership operates multiple trades or businesses, it may elect under Reg. §1.199A-4(b)(1) to aggregate them at the partnership level. The aggregation must satisfy: Same person or group owns ≥ 50% of each trade or business; All trades or businesses operate in the same tax year; None is an SSTB; Two of three 'factors of integration' — same products/services, shared facilities or centralized support, operated in coordination with or reliance on each other. Once made, the election is binding and must be disclosed each year on a §1.199A-4(c)(2) statement attached to the partnership return. The partner can also aggregate at their own level — but cannot disaggregate items the partnership has already aggregated.  _(Reg. §1.199A-4(b)(1), §1.199A-4(c)(2))_

## 17. Common Attached Forms

**Common Attached Forms**  _(IRC §179(d)(8); §1231; §163(j); §448(c); §6662; §1.6011-4)_

| Form | Trigger | Notes |
| --- | --- | --- |
| **4562** Depreciation and Amortization | Any depreciation, amortization, §179, listed property, or property placed in service this year | §179 expense flows out separately on K-1 (subject to §179(d)(8) partner-level limit) |
| **4797** Sales of Business Property | §1231 gain/loss, §1245/1250 recapture, ordinary gain on §1239 sales | §1231 gain flows to K-1 Box 10 |
| **8825** Rental Real Estate Income and Expenses | Any rental real estate activity | Replaces Schedule E logic for partnerships; output flows to K Line 2 / K-1 Box 2 |
| **8990** §163(j) Limitation on Business Interest Expense | Partnership not eligible for §163(j) small-business exemption (gross receipts > $30M for 2025, verify against §448(c)) | Excess business interest is allocated to partners and carried at the partner level; complex 11-step §163(j) partner-level rule |
| **6765** Credit for Increasing Research Activities | Qualified research expenses | Credit flows on K-1 Box 15 |
| **8283** Noncash Charitable Contributions | Property contribution > $500 | Special partnership rules apply for partner-level deduction |
| **8332** Release of Claim to Exemption | Not applicable to partnerships, but partners may need at their level | n/a |
| **8082** Notice of Inconsistent Treatment or AAR | Filing an Administrative Adjustment Request, or partner is taking a position inconsistent with K-1 | For AAR — see §18 |
| **8893** Election of Partnership-Level Tax Treatment | Legacy TEFRA — rarely used post-CPAR | Verify if old |
| **8804/8805/8813** §1446 ECI Withholding for Foreign Partners | Any foreign partner with allocable share of ECI | **Out of scope for v0.1 — refer out** |
| **8865** Return of US Persons With Respect to Certain Foreign Partnerships | US person owns ≥10% of a foreign partnership | **Out of scope for v0.1 — refer out** |
| **8918** Material Advisor Disclosure | Material advisor to a reportable transaction | Rare; reviewer attention |
| **8275 / 8275-R** Disclosure Statement | Any position requiring disclosure to avoid §6662 penalty | Attach when needed |
| **Schedule M-3** | Total assets ≥ $10M at end of year (or other §1.6011-4 triggers) | Much more detailed than M-1; can be very time-intensive |

## 18. Push-Out Election and Administrative Adjustment Request (AAR)

### 18.1 §6226 push-out election

- **§6226 push-out election window and mechanics** — After an IRS audit finalizes an imputed underpayment under CPAR, the partnership has 45 days from the date of the final partnership adjustment to elect under §6226 to push out the adjustment to reviewed-year partners. Mechanics: Partnership prepares 'Statements' (one per reviewed-year partner) showing each partner's share of the adjustments; Partnership files Form 8985 (Pass-Through Statement) with the IRS and furnishes Form 8986 (Partner's Share of Adjustments) to each reviewed-year partner; Each reviewed-year partner reports the adjustment on their own return for the year that includes the date the statement was furnished (the 'reporting year'); Interest accrues at AFR + 2% (higher than the standard underpayment rate of AFR + 3% — actually a penalty premium; verify against current §6621 underpayment-rate plus §6226(c) 2-point increase). The push-out election is irrevocable once made.  _(IRC §6226; §6621; §6226(c))_
- **Push-out election deadline** — 45 days (from date of final partnership adjustment)  _(IRC §6226)_

### 18.2 Administrative Adjustment Request (AAR) — §6227

- **AAR mechanics and restrictions** — A partnership cannot file an 'amended Form 1065' the way a corporation files an amended 1120. Instead, the partnership files an Administrative Adjustment Request (AAR) to correct a previously filed BBA partnership return. Mechanics: Use Form 1065 with the 'Amended Return' or 'AAR' box appropriately checked (the 2025 form has a dedicated AAR indicator); Compute the imputed underpayment for the year of the original return (the 'reviewed year'); The partnership can elect to push out the adjustment to reviewed-year partners (similar to §6226), or pay the imputed underpayment at the partnership level; AAR cannot be filed after the IRS has mailed a Notice of Administrative Proceeding to the partnership; AAR is the BBA-era equivalent of the old 'Amended K-1' practice; partners cannot generally amend their own returns to reflect K-1 corrections without an AAR being filed (with very narrow exceptions). For BBA partnerships that have elected out of CPAR on Schedule B-2, AAR does not apply — the partnership files an amended Form 1065 and amended K-1s in the conventional manner, and partners amend their own 1040s.  _(IRC §6227)_

### 18.3 Reviewer brief content

- Confirm whether the partnership is in CPAR or has elected out
- If in CPAR and corrections are needed → AAR (not amended return)
- If elected out → amended return and amended K-1s
- For AAR with push-out: confirm 45-day window from final adjustment / file the §6226 election timely / track partner-level reporting in the partner's reporting year

## 19. LLC vs Partnership — Classification Reminder

Reviewer should never confuse: LLC (state-law entity) — flexible default federal classification; Partnership (federal-tax classification) — the result of the default rules or a §761 / §301.7701-3 path. A multi-member LLC is a partnership for federal tax unless it has elected otherwise. An LLC that has elected C-corp or S-corp treatment files 1120 / 1120-S, not 1065. An SMLLC is disregarded, not a partnership. The two-spouse LLC in a community property state has an additional wrinkle. Under Rev. Proc. 2002-69, if (i) the LLC is wholly owned by a husband and wife as community property under state law, (ii) no person other than the spouses is considered an owner for federal tax purposes, and (iii) the business is not treated as a corporation, the spouses may elect to treat it as a disregarded entity (one Schedule C, one owner). This is not the same as the §761(f) Qualified Joint Venture election (which is for non-LLC ventures between spouses in any state). Both are alternatives to Form 1065 for spousal-owned businesses.

- **Rev. Proc. 2002-69 disregarded entity election for spousal community-property LLC** — If (i) the LLC is wholly owned by a husband and wife as community property under state law, (ii) no person other than the spouses is considered an owner for federal tax purposes, and (iii) the business is not treated as a corporation, the spouses may elect to treat it as a disregarded entity (one Schedule C, one owner).  _(Rev. Proc. 2002-69)_

## 20. Worked Examples

### 20.1 Example 1 — Simple two-member LLC, services business, no foreign activity

- Cetta Cutajar Consulting LLC, Maltese-American consultancy operating in Texas
- Two members: Alice Cetta (50%) and Bob Cutajar (50%), both US citizens, individuals
- Both members manage the business; LLC operating agreement labels both as "managing members"
- 2025 results: Revenue $400,000, expenses $250,000, ordinary income $150,000
- No foreign partners, no foreign-source income, no foreign assets, no foreign taxes
- No property contributions (only cash at formation)
- Bank loan of $50,000, neither member guaranteed, secured by accounts receivable (nonrecourse for §752)
- Total assets at year-end: $180,000
- Both members materially participate (full-time)

*Form 1065:*
- Page 1, Line 22 Ordinary business income: $150,000
- Schedule B: Domestic LLC; cash method; two partners; no foreign activity
- Schedule B-1: not required (no partner owns 50%+ on either capital or profits considered alone — both at exactly 50%; verify against B-1 instructions, which trigger at >50% in many years, but disclosure may still be best practice for 50% partners)
- Schedule B-2: **Elect out of CPAR** — two individual eligible partners, well under 100
- Partnership Representative: Alice Cetta (managing partner, US citizen, US address); DI not required (PR is an individual)
- Schedule K Line 1: $150,000
- Schedule L: not required (assets $180K < $1M and receipts $400K > $250K — actually triggered by receipts; **Schedule L is required**); reviewer to confirm
- Schedule M-1 / M-2: required (because L is required)
- Schedule K-2 / K-3: **Not required** — Domestic Filing Exception satisfied (no foreign activity, all US individual partners, partner notifications sent by Jan 15, 2026, no partner requested K-3 by 1-month date)

- Part II, Item G: General partner or LLC member-manager (because she manages and has unlimited management authority within the LLC; SE-exempt status under §1402(a)(13) is not available)
- Item J: Profit/loss/capital 50% / 50% / 50%
- Item K: Nonrecourse $25,000 (50% of $50K Tier-3 allocation)
- Item L (tax basis):
  - Beginning capital: $0 (formation, first year)
  - Capital contributed: cash contributed at formation
  - Current year net income: $75,000
  - Withdrawals: per partnership records
- Part III:
  - Box 1: $75,000 ordinary business income
  - Box 14, code A: $75,000 net SE earnings (full distributive share — Alice is a managing LLC member, fully subject to SE)
  - Box 20, code Z: §199A statement — QBI $75,000, no W-2 wages (no employees), no UBIA (services business, minimal qualified property), SSTB indicator: **YES** (consulting is an SSTB under §199A(d)(2)(A))
  - Box 22: not checked (one activity)
  - Box 23: not checked (one activity, both members material participants — non-passive)
- Same for Bob.

- Consulting is an SSTB → at Alice and Bob's individual level, their QBI deduction phases out if taxable income exceeds the 2025 §199A SSTB phase-in threshold (~$241,950 single / ~$483,900 MFJ — verify against Rev. Proc. 2024-40). This is a partner-level computation; the partnership only flags.
- SE tax: $75,000 each at full SE rates. Approximately 14.13% net effective SE rate (taking into account the 92.35% adjustment, the 12.4% OASDI up to $176,100 and 2.9% Medicare). See `us-schedule-c-and-se-computation` for partner-level numbers.
- §6698 calendar: file by March 16, 2026 (March 15 is Sunday). Reminder set.

- **2025 §199A SSTB phase-in threshold, single** — $197,300 (2025, Rev. Proc. 2024-40; fully phased out at $247,300; OBBBA § 70105 widens the phase-in range to $75,000, $150,000 joint, from 2026) USD (verify against Rev. Proc. 2024-40)  _(Rev. Proc. 2024-40)_
- **2025 §199A SSTB phase-in threshold, MFJ** — $394,600 (2025, Rev. Proc. 2024-40; fully phased out at $494,600; OBBBA § 70105 widens the joint phase-in range to $150,000 from 2026) USD (verify against Rev. Proc. 2024-40)  _(Rev. Proc. 2024-40)_
- **OASDI portion of SE tax rate up to wage base** — 12.4 percent (up to $176,100)  _(see `us-schedule-c-and-se-computation`)_
- **OASDI wage base** — $176,100 USD  _(see `us-schedule-c-and-se-computation`)_
- **Medicare portion of SE tax rate** — 2.9 percent  _(see `us-schedule-c-and-se-computation`)_
- **SE tax net earnings adjustment factor** — 92.35 percent  _(see `us-schedule-c-and-se-computation`)_
- **Form 1065 filing deadline reminder 2026** — March 16, 2026 (March 15 is a Sunday)  _(§6698)_

### 20.2 Example 2 — Partnership with one foreign partner, triggering K-3

- Global Software Partners LLP, Delaware LLP
- Three partners: US Corp Inc. (40%, C-corporation, Delaware), Marie Dubois (30%, French citizen and tax resident of France, individual), Tomas Kowalski (30%, US resident alien with green card, individual)
- 2025 ordinary business income: $1,200,000
- Two foreign customers paid the partnership: customer X (German GmbH) paid €200,000, customer Y (Japanese KK) paid ¥10,000,000. No physical presence in those countries; no permanent establishment under treaties; no foreign taxes withheld at source.
- The partnership has a brokerage account that holds $500,000 in international mutual funds — produced $25,000 of foreign dividends with $3,500 of foreign tax withheld (reported on broker 1099-DIV).
- Marie does not work in the US; she is a passive investor.
- US Corp Inc and Tomas are active.

- **Schedule B-2 election out?** — No. The partnership has a foreign partner (Marie). Foreign individuals are not eligible partners under §6221(b). The partnership stays in CPAR. Partnership Representative: US Corp Inc. (entity), with a Designated Individual (a US employee of US Corp Inc.).  _(§6221(b))_
- **K-2/K-3 required?** — Yes, both triggers fire: Foreign partner (Marie) — automatic K-3 requirement; Foreign-source income (foreign dividends, foreign tax). Domestic Filing Exception does not apply because (1) there is a foreign partner, (2) there is foreign-source income with foreign taxes.  _(Domestic Filing Exception)_

- Part I — basic international information
- Part II — FTC limitation: split foreign-source vs US-source; the $25,000 foreign dividends are passive-category income
- Part III — allocable deductions
- Part X — foreign partners' character & source (Marie's income — what is and is not US-source ECI)
- Part IX — §1446 withholding (Marie's allocable share of ECI is subject to §1446; partnership must withhold; this is **out of scope** for v0.1 — refer to a §1446 specialist; the partnership likely owes withholding on Marie's $360,000 distributive share of the $1.2M business income to the extent ECI)

- Item G: Limited partner / other LLC member (she is a non-managing passive investor)
- Item H1: Foreign
- Item I1: Individual
- Box 1: $360,000 ordinary business income (30%)
- Box 14: Marie's SE earnings — **zero** for §1402(a)(13) limited-partner exclusion **even if Soroban applied**, because as a non-US person she is not subject to SE tax in any case (§1402(b) — net earnings from SE include earnings only of a "United States citizen or resident"; Marie is neither, assuming she is not a US tax resident)
- Box 16: K-3 attached — Yes
- Box 21: foreign tax — Marie's allocable share of $3,500 foreign tax
- K-3 attached covers Marie's portion of foreign-source income, deductions, FTC info, and §1446 ECI withholding statement

- Item G: General partner (as a C-corp partner, the SE question is moot)
- Item H1: Domestic
- Item I1: Corporation
- Box 1: $480,000 (40%)
- Box 14: not applicable (C-corp partner)
- K-3 attached with C-corp specific items (no FTC limitation for individual purposes; instead, §901/§902 treatment at the C-corp level for the corp's own 1120)

- Item G: General partner or LLC member-manager
- Item H1: Domestic (US resident alien)
- Item I1: Individual
- Box 1: $360,000 (30%)
- Box 14, code A: $360,000 (fully SE — Tomas is a managing partner who materially participates)
- Box 20: §199A statement — partnership is in software development (non-SSTB under §199A); reviewer should confirm
- K-3 with FTC info for Tomas's $7,500 share of foreign dividends and $1,050 share of foreign taxes

- §1446 withholding on Marie — partnership owes 37% (highest individual rate) on Marie's allocable share of ECI; partnership must file Forms 8804/8805/8813 quarterly. **Out of scope for v0.1.** Refer to §1446 specialist before finalizing.
- Marie's foreign-status W-8BEN must be in the file (verify)
- Schedule M-3 required if assets ≥ $10M — verify (likely yes for a $1.2M income company with international ops)
- Schedule K-2 / K-3 production — many hours of preparer time; budget accordingly

- **§1446 withholding rate on Marie's ECI** — 37 percent (highest individual rate)  _(§1446)_
- **§1446 ECI withholding — out of scope** — Out of scope for v0.1. Refer to §1446 specialist before finalizing.  _(§1446; Forms 8804/8805/8813)_

### 20.3 Example 3 — Family LP with §704(c) contributed property and limited-partner SE issue

- Cutajar Family Real Estate Limited Partnership (FLP), formed 2020 under Texas law
- General Partner: Cutajar Management LLC (a Texas SMLLC wholly owned by Michael Cutajar, individual)
- Limited Partners: Michael Cutajar (49%, founder), Sofia Cutajar (his adult daughter, 25%), Marcus Cutajar (his adult son, 25%); the GP holds 1%
- 2020 — at formation, Michael contributed a Houston rental property with:
  - FMV at contribution: $1,000,000
  - Adjusted tax basis at contribution: $200,000
  - Mortgage assumed by partnership: $400,000 (qualified nonrecourse — commercial bank, secured by the property, real-property trade or business)
- 2025 — partnership operates the rental, has additional properties acquired with bank financing
- Michael actively manages the FLP (he is the operating brain), through the GP LLC
- Sofia and Marcus are pure passive investors; neither provides services
- 2025 results:
  - Net rental real estate income: $80,000 (after depreciation)
  - Net §1231 gain on sale of one property: $200,000 (built-in gain layer attributable to Michael's 2020 contribution — see below)
  - Interest income on operating cash: $5,000
- §704(c) accounting: partnership uses **traditional method with curative allocations** under Reg. §1.704-3(c)

**§704(c) layer analysis (2020 contribution)**  _(Reg. §1.704-3(c))_

| Item | Tax basis | §704(b) book |
| --- | --- | --- |
| Property at contribution | $200,000 | $1,000,000 |
| Built-in gain layer (FMV − basis) | $800,000 | — |

Through 2024, depreciation has been allocated under §704(c) traditional+curative method. In 2025, the property is sold. Gain on disposition: Sale price: $1,300,000; Adjusted tax basis at sale (after depreciation): $120,000; Total tax gain: $1,180,000; Of which: built-in gain attributable to Michael under §704(c) = $800,000 (less recapture already allocated through depreciation); Remaining "common" gain split per partnership shares: ~$380,000

- **Schedule B-2 election out eligibility** — Possible. Eligibility check: 4 partners (1 GP + 3 LPs). Under 100. ✓ Cutajar Management LLC (the GP) — this is an SMLLC owned by Michael (an eligible individual). Per Reg. §301.6221(b)-1(b)(3)(ii) — verify with current regs — an SMLLC wholly owned by an eligible individual partner IS an eligible partner. ✓ Michael, Sofia, Marcus — individuals. ✓ → Schedule B-2 election out is available. Reviewer to confirm with Michael whether he wants to elect out (recommend yes — small stable family entity, no benefit to staying in CPAR).  _(Reg. §301.6221(b)-1(b)(3)(ii))_
- **§1402(a)(13) limited-partner SE issue analysis** — Cutajar Management LLC (the GP): the GP receives a 1% allocation. The GP itself is a partnership-tax disregarded entity (SMLLC), so its allocation flows through to Michael. But Michael's distributive share via the GP is a general-partner allocation, subject to SE tax. Net rental real estate income is excluded from SE under §1402(a)(1) regardless — so Michael's GP-routed share of $80,000 is not SE income. The §1231 gain is also excluded (§1402(a)(3)). The interest income is excluded (§1402(a)(2)). Michael's LP share (49%) — Michael is labeled an LP but he actively manages through the GP. Under Soroban (2023), a labeled-LP who provides material services is not necessarily an LP for §1402(a)(13). But: Rental real estate income is excluded from SE in any case (§1402(a)(1)); §1231 gain is excluded (§1402(a)(3)); Interest is excluded; Net SE income at the partnership level = $0 regardless of LP/GP characterization. So in this fact pattern, the LP/GP characterization for §1402 is moot because the income items are all per-se non-SE.  _(§1402(a)(13); §1402(a)(1); §1402(a)(2); §1402(a)(3); Soroban Capital Partners LP v. Commissioner)_

However: if the FLP also had a side business of "property management services" charged at fair market value to third parties, that service revenue would be ordinary trade-or-business income subject to SE rules and the Soroban question would matter. Reviewer to confirm no service business is being conducted alongside the rental.

1. §704(c) — built-in gain on sale of contributed property — verify the historic depreciation allocations under traditional+curative, confirm the remaining built-in gain layer is fully recognized in 2025, and ensure Item M / Item N on the 2025 K-1s reflect the closing-out of Michael's §704(c) layer.
2. §752 — qualified nonrecourse financing — the original $400K mortgage and the additional bank loans (assume all real-property QNF). Allocate per Reg. §1.752-3 three-tier rule:
   - Tier 1 (partnership minimum gain): based on depreciation that exceeds book depreciation
   - Tier 2 (§704(c) gain): Michael gets first allocation
   - Tier 3 (excess): per partnership agreement, typically per profit-sharing ratio
3. §469 passive activity — Sofia and Marcus are clearly passive (rental is per se passive; no real estate professional status). Their net rental income is passive income but the §1231 gain is portfolio/§1231 not passive (Box 10 on K-1; partner-level §469 grouping rule applies).
4. Michael's real estate professional status (§469(c)(7)) — verify; if he qualifies, his rental income/loss is non-passive at his level.
5. Schedule B-2: elect out (recommended).
6. K-3: Domestic Filing Exception likely applies (all US individual/SMLLC partners, no foreign activity). Confirm partner notifications and no K-3 requests.
7. Schedule L: required (assets very likely > $1M for a $1M+ contribution + appreciation + multiple properties).
8. Schedule M-3: required if year-end assets ≥ $10M — verify against rollforward.

- Item G: Limited partner / other LLC member (labeled LP; reviewer documents the management activity is via the GP, not the LP interest)
- Item L tax basis capital — full rollforward including the §704(c) closing out
- Item M: Yes (contributed property with built-in gain)
- Item N: net §704(c) remaining gain/loss — starts at the 1/1/2025 balance, ends at zero (property fully sold)
- Box 2: net rental real estate income, his share
- Box 10: §1231 gain, his share (including the §704(c) curative allocation to Michael)
- Box 14: $0 (rental and §1231 excluded from SE)
- Box 16: K-3 not attached (DFE)
- Box 20: §199A — net rental real estate may or may not be QBI depending on Rev. Proc. 2019-38 safe harbor; reviewer determines

**Property at contribution**  _($1,000,000)_

| Item | Value |
| --- | --- |
| Property at contribution | $200,000 |
| Built-in gain layer (FMV − basis) | $1,000,000 |

## 21. Provenance and Disclaimer

### 21.1 Primary statutory and regulatory sources

- IRC §§701–777 (Subchapter K)
- IRC §6031 (return requirement); §6072 (due dates); §6698 (penalty)
- IRC §§704, 707, 752 (allocation, capital accounts, liabilities)
- IRC §§465, 469, 461(l) (loss limits)
- IRC §1402 (self-employment tax); §1402(a)(13) (limited partner exclusion)
- IRC §199A (QBI deduction); made permanent at 20% (2025) / 23% (2026+) by OBBBA P.L. 119-21 §70105
- IRC §§6221–6241 (Centralized Partnership Audit Regime / BBA)
- Treas. Reg. §301.7701-1 through -3 (entity classification)
- Treas. Reg. §1.704-1, -2, -3 (substantial economic effect; §704(c) methods)
- Treas. Reg. §1.752-1, -2, -3 (recourse / nonrecourse allocation)
- Treas. Reg. §1.469-5T (material participation; LLC member-manager question)
- Treas. Reg. §301.6221(b)-1 (election out of CPAR)
- Treas. Reg. §1.199A-1 through -6 (QBI mechanics)
- Reg. §1.6031(a)-1 (foreign partnership filing)

### 21.2 Case law

- *Soroban Capital Partners LP v. Commissioner*, 161 T.C. No. 12 (Nov 28, 2023) — functional test for "limited partner" under §1402(a)(13)
- *Garnett v. Commissioner*, 132 T.C. 368 (2009) — LLC members not automatically limited partners for §469 purposes
- *Thompson v. United States*, 87 Fed. Cl. 728 (2009) — similar
- *Renkemeyer, Campbell & Weaver, LLP v. Commissioner*, 136 T.C. 137 (2011) — LLP partners providing services were not §1402(a)(13) limited partners

### 21.3 IRS guidance

- Rev. Proc. 84-35 (small partnership §6698 reasonable cause safe harbor)
- Rev. Proc. 93-27 (profits-interest grants)
- Rev. Proc. 2002-69 (spousal community-property LLC)
- Rev. Proc. 2024-40 (2025 inflation adjustments; verify §6698 figure)
- Notice 2018-64 (§199A W-2 wages methods)
- Notice 2020-43 (tax basis capital account reporting)
- Notice 2021-39 (good-faith transition relief for K-2/K-3)
- 2025 Form 1065 Instructions (verify against IRS final release for exact line references and 2025 indexed figures)
- Final K-2/K-3 Instructions for tax year 2025 (verify Domestic Filing Exception language)

### 21.4 Statutory changes from OBBBA (P.L. 119-21, July 4, 2025) potentially affecting this skill

- §199A made permanent at 20% (2025) / 23% (2026+) — confirmed
- §461(l) excess business loss limit made permanent
- §163(j) interest limitation — small business exemption threshold (gross receipts) — verify Rev. Proc. 2024-40 for 2025 threshold
- §6698 penalty amount — verify 2025 indexed figure
- §1402 self-employment tax — no statutory change; Soroban case law continues to develop

### 21.5 Disclaimer

This skill produces a reviewer-oriented draft of Form 1065 and supporting schedules. A credentialed tax practitioner under Circular 230 (Enrolled Agent, CPA, or attorney) must review and sign the return before it is filed. The skill is conservative by default; it flags rather than auto-decides on ambiguous allocations, SE tax characterizations, §704(c) methods, and CPAR election questions. The 2025 indexed amounts (§6698 penalty, §199A thresholds, §461(l) thresholds, §163(j) small-business gross-receipts threshold) must be verified against the final Rev. Proc. 2024-40 (or its successor) before final filing. This skill is federal-only. State partnership returns, state pass-through entity tax (PTET) elections, and state withholding on nonresident partners are out of scope and must be handled by the relevant state skill or a state-licensed practitioner. The skill does not, and cannot, replace partnership counsel for drafting allocation provisions, DRO clauses, QIO provisions, partnership-representative indemnification, or §704(c) method elections. Where the skill flags a structural issue, the reviewer should refer to qualified partnership-law counsel.

— End of skill —

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is different, and the rules in the skill may not match your specific facts. To speak with one of the licensed accountants who verifies skills for your jurisdiction — no liability on either side until you and the accountant sign a formal engagement letter — book a free 30-minute call: **→ [Book a call](https://calendly.com/openaccountants-info/30min)**. We'll route you to the named verifier covering your country or state. You can also see the full list of verified accountants at [openaccountants.com/network](https://openaccountants.com/network).
