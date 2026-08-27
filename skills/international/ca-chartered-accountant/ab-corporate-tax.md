---
name: ab-corporate-tax
description: Use this skill for Alberta provincial corporate income tax. Triggers "Alberta CIT", "AT1 Alberta", "Alberta small business deduction", "Job Creation Tax Cut Alberta", "Alberta corporate tax 8%". ALWAYS read alongside federal T2.
jurisdiction: CA
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# AB Corporate Tax

## Alberta — Corporate Income Tax — Skill v1.0

> **Scope:** Alberta provincial corporate income tax (Alberta Corporate Tax Act, RSA 2000, c A-15) for the 2025 tax year. ALWAYS load this skill alongside the federal T2 skill — Alberta is a non-agreeing province for corporate tax and runs its own AT1 system in parallel with the federal T2.

## 1. Quick reference — Alberta vs federal combined CIT

**Quick reference — Alberta vs federal combined CIT**

| Income type | Federal | Alberta | **Combined** |
| --- | --- | --- | --- |
| **General active business income** | 15% | **8%** | **23%** |
| **SBD income** (first $500,000 active business income, CCPC) | 9% | **2%** | **11%** |
| **Investment income (CCPC, non-active)** | 38.67% (incl. 10.67% refundable) | 8% | 46.67% |
| **M&P income** (no separate AB rate) | 15% | 8% | 23% |

Alberta has the **lowest general provincial corporate income tax rate in Canada** following the Job Creation Tax Cut (Bill 3, 2019), which reduced the general rate from 12% to 8% in four annual 1-point steps culminating July 1, 2020 — accelerated from the original 2022 schedule.

**Comparable provinces (2025 general rate):**
- Alberta: 8%
- BC: 12%
- Saskatchewan: 12%
- Manitoba: 12%
- Ontario: 11.5%
- Quebec: 11.5%

## 2. Required inputs + refusal catalogue

### Required inputs

1. **Permanent establishment (PE)** in Alberta — confirmed via federal Schedule 5 allocation
2. **Alberta taxable income allocation** — % of taxable income earned in Alberta (Schedule 5, federal T2)
3. **Active business income (ABI)** vs aggregate investment income (AAII) split
4. **CCPC status** for the entire tax year
5. **Associated corporation group** — for SBD limit sharing
6. **Federal SR&ED qualified expenditures** — feeds Alberta IEG computation
7. **Fiscal year-end (FYE)** date
8. **Alberta Corporate Account Number (CAN)** — 9 or 10-digit AB TRA identifier

### Refusal catalogue (out of scope — escalate to credentialed Alberta tax practitioner)

- **R-AB-CIT-1** — Multi-provincial PE allocation with disputed Schedule 5 attribution
- **R-AB-CIT-2** — Non-resident corporation carrying on business in Alberta (Part XIV branch tax interaction)
- **R-AB-CIT-3** — Insurance corporations, banks, and financial institutions (special AT1 schedules)
- **R-AB-CIT-4** — Crown corporations, exempt entities under s.35 of the Act
- **R-AB-CIT-5** — Mutual fund corporations, mortgage investment corporations
- **R-AB-CIT-6** — Reorganizations involving Alberta-allocated assets (s.85, s.86, s.87 with cross-border consequences)
- **R-AB-CIT-7** — Voluntary disclosure under the Alberta TRA VDP — credentialed practitioner only
- **R-AB-CIT-8** — AT1 objections, notices of appeal, Alberta Court of King's Bench tax matters

## 3. General rate — 8% (Job Creation Tax Cut)

- **General corporate income tax rate** — 8% (For tax years ending on or after July 1, 2020, remains 8% for the 2025 tax year)  _(s.21 of the Alberta Corporate Tax Act)_

### Rate history (Job Creation Tax Cut, Bill 3, 2019)

**Rate history (Job Creation Tax Cut, Bill 3, 2019)**

| Effective date | General rate |
| --- | --- |
| Before July 1, 2019 | 12% |
| July 1, 2019 | 11% |
| January 1, 2020 | 10% |
| July 1, 2020 | **8%** (accelerated from the originally planned 2022) |
| 2025 | **8%** (current) |

- **Combined federal + Alberta general rate** — 23% (15% federal + 8% AB)

### Straddling tax years

- **Proration for straddling fiscal years** — A corporation with a fiscal year straddling a rate change date must prorate. For 2025, the rate has been stable at 8% since July 1, 2020, so no proration applies to any FYE in 2025.

## 4. Small Business Deduction (SBD) — 2% Alberta rate

- **SBD availability** — Alberta provides a small business deduction under s.22 of the Alberta Corporate Tax Act on the first $500,000 of active business income of a Canadian-controlled private corporation (CCPC).  _(s.22 of the Alberta Corporate Tax Act)_

### Effective rates

- **Alberta SBD rate** — 2% (general rate of 8% minus SBD of 6%)
- **Federal SBD rate** — 9% (general rate of 15% minus federal SBD of 6%)
- **Combined federal + AB SBD rate** — 11% (on first $500,000 ABI)

### Business limit grind

- **Taxable capital employed in Canada (TCEC) grind** — Alberta mirrors the federal grind — the $500,000 business limit is reduced where TCEC of the associated group exceeds $10M, fully phased out at $50M (consistent with the 2024+ federal expansion from the prior $10M-$15M phase-out band).
- **Passive investment income grind** — Alberta mirrors the federal AAII grind under ITA s.125(5.1) — every $1 of AAII over $50,000 reduces the SBD business limit by $5, fully eliminated at $150,000 AAII.  _(ITA s.125(5.1))_
- **Associated corporations sharing** — Associated corporations must share the $500,000 business limit via AB Schedule 3 (mirrors federal T2 Schedule 23 allocation).

### Specified Investment Business (SIB) and Personal Services Business (PSB)

- **SIB income** — SIB income does not qualify for the SBD; taxed at 8% Alberta general rate (plus federal refundable rates on investment income).
- **PSB income** — PSB income is excluded from the SBD by ITA s.125(7); Alberta follows. PSB also faces the federal 5% additional tax under ITA s.123.5 — Alberta does not apply an additional provincial PSB surtax.  _(ITA s.125(7); ITA s.123.5)_

## 5. AT1 return — Alberta's standalone corporate tax return

Alberta is one of three non-agreeing provinces for corporate tax (along with Quebec and — for the period before 2010 — Ontario, which has since integrated). Corporations with a PE in Alberta file:

- **Federal T2** with the Canada Revenue Agency (CRA), AND
- **AT1 — Alberta Corporate Income Tax Return** with **Alberta Tax and Revenue Administration (TRA)**

> Note: Alberta participates in the federal–provincial Tax Collection Agreement (TCA) for **individuals** (CRA administers the AB personal income tax under the same T1), but **not for corporations**. The AT1 system is administered directly by TRA at Alberta Treasury Board and Finance.

### AT1 core schedules (2025)

**AT1 core schedules (2025)**

| Schedule | Purpose |
| --- | --- |
| **AT1 page 1** | Identification, FYE, AB allocation %, tax payable |
| **AT1 Schedule 1** | Alberta small business deduction calculation |
| **AT1 Schedule 2** | Alberta foreign investment income tax credit (limited) |
| **AT1 Schedule 4** | Alberta foreign tax credit on business income |
| **AT1 Schedule 9** | Listed Personal Property and other capital gains |
| **AT1 Schedule 10** | Alberta loss carry-forward continuity (non-capital, net capital, restricted farm) |
| **AT1 Schedule 12** | Income/loss reconciliation to federal Schedule 1 |
| **AT1 Schedule 13** | Alberta Innovation Employment Grant (IEG) |
| **AT1 Schedule 14** | Cumulative eligible capital (CEC) — historical only; replaced by Class 14.1 |
| **AT1 Schedule 18** | Allocation of Alberta income among PEs |
| **AT1 Schedule 21** | Calculation of Alberta tax payable |
| **AT1 Schedule 29** | Innovation Employment Grant — detailed eligible expenditures |

### Filing channel

- **Net File AT1** via TRA's online portal (mandatory for most corporations)
- **Tax preparer software**: CCH iFirm Taxprep, Wolters Kluwer Cantax, Intuit ProFile, TaxCycle — all support AT1 e-filing
- **Paper filing** permitted only for corporations exempt from e-filing (very rare exceptions)

### Account number

- Corporations must register for an **Alberta Corporate Account Number (CAN)** with TRA before first filing
- Registration: TRA Client Self-Service (TRACS) portal

## 6. Filing deadlines

**Filing deadlines**

| Item | Deadline |
| --- | --- |
| **AT1 return filing** | **6 months after FYE** (same as federal T2) |
| **AT1 tax payment** | **2 months after FYE** (CCPCs claiming SBD: 3 months after FYE — mirrors federal) |
| **Instalments** | Monthly instalments for corporations with prior-year AB tax over $2,000; quarterly available for eligible CCPCs (mirrors federal eligibility) |
| **Notice of objection** | 90 days from Notice of (Re)assessment |
| **Record retention** | 6 years from end of last tax year to which the records relate |

### Late filing penalties (Alberta TRA)

- **Late filing penalty structure** — - **5% of unpaid tax** at filing deadline, plus - **1% per complete month** of continuing failure, up to **12 months** - **Doubled** for repeat offenders (prior late-filing penalty in any of the 3 preceding tax years and TRA demand to file): 10% + 2%/month up to 20 months - **Interest** on unpaid tax accrues from balance-due date at the TRA-prescribed rate (set quarterly; aligned roughly with federal CRA prescribed rate plus a margin)

## 7. Alberta Investor Tax Credit (AITC) — historical

- **AITC description and status** — The AITC was a non-refundable 30% tax credit for investments in eligible Alberta small businesses (capped at $60,000/investor/year and $5M per business lifetime), available 2017–2019. - **Status**: **Eliminated effective March 30, 2020** by the UCP government (Bill 20, 2019) - **Grandfathered claims**: Credits earned 2017–2019 retain a **4-year carry-forward** (last carry-forward window expired with 2023 tax year for the final 2019 vintage) - **2025 action**: Check for any unused AITC carry-forward on prior AT1 — for FYEs in 2025, the 2019-vintage carry-forward has expired; only confirm there is nothing inadvertently still being claimed.  _(Bill 20, 2019)_

## 8. Capital Investment Tax Credit (CITC) — wound down

- **CITC description and status** — The CITC was a 10% non-refundable tax credit for capital investment in manufacturing, processing, and tourism infrastructure (eligible expenditure $1M minimum, credit cap $5M per project). - **Status**: **Program wound down in 2020**; no new applications accepted. - **Grandfathered claims**: Credits earned for approved projects retain a **10-year carry-forward**. - **2025 action**: Check the prior AT1 for any CITC carry-forward balance and confirm continued claim eligibility against TRA approval letter.

## 9. Innovation Employment Grant (IEG) — refundable R&D credit

The IEG is Alberta's refundable R&D tax credit, introduced effective January 1, 2021 to partially replace the wound-down Alberta SR&ED tax credit (which was eliminated effective January 1, 2020).

### Rate structure (s.26.6 Alberta Corporate Tax Act)

**Rate structure (s.26.6 Alberta Corporate Tax Act)**  _(s.26.6 Alberta Corporate Tax Act)_

| Tier | Rate | Base |
| --- | --- | --- |
| **Base credit** | **8%** | First **$4M** of eligible R&D expenditures (in Alberta) |
| **Incremental credit** | **20%** | Expenditures **above the prior 2-year average** R&D spend, up to the $4M cap |

### Eligibility

- **IEG eligibility criteria** — - Corporation with **PE in Alberta** at any time in the tax year - Eligible expenditures = **federal SR&ED qualified expenditures** (per ITA s.37 and Regulation 2900) **incurred in Alberta** - **Refundable**: Excess credit over Alberta tax payable refunded to the corporation (no carry-forward needed)  _(ITA s.37; Regulation 2900)_

### Expenditure cap

- **IEG expenditure cap rules** — - The **$4M expenditure cap** is shared among **associated corporations** - The cap is **prorated** for short tax years

### Claim mechanics

- **IEG claim filing mechanics** — - File **AT1 Schedule 29** (detailed eligible expenditures, allocation among associated group) - File **AT1 Schedule 13** (summary, integration with AT1 tax payable) - Reconciles to **federal T661** (SR&ED claim) line entries restricted to Alberta-located expenditures

### Interaction with federal SR&ED

- **IEG and federal SR&ED interaction** — - The IEG is **separate from federal SR&ED ITC** — both can be claimed on the same eligible expenditure pool (where Alberta-located) - The IEG itself is **taxable income** for federal purposes in the year received (ITA s.12(1)(x); included on federal T2 Schedule 1) - Alberta does not require an offsetting addback (avoids double-taxing the grant in AB)  _(ITA s.12(1)(x))_

## 10. Foreign investment income — no additional AAII refundable tax in Alberta

- **No AB AAII refundable tax** — Some provinces (e.g., Saskatchewan with its 2% additional refundable tax on AAII) apply a provincial refundable tax on aggregate investment income (AAII) of CCPCs mirroring the federal 10.67% Part I refundable tax under ITA s.123.3. **Alberta does NOT have an additional provincial refundable tax on AAII.** Investment income of an Alberta CCPC is taxed at: - **Federal**: 38.67% (28% Part I + 10.67% additional refundable Part I) - **Alberta**: **8% only** (general rate; no surtax, no AAII supplement) - **Combined**: 46.67% Federal RDTOH (refundable dividend tax on hand) mechanics apply at the federal level only; Alberta has no provincial RDTOH equivalent. Refundable mechanics operate solely through CRA on the federal Part I refundable component.  _(ITA s.123.3)_

## 11. Worked example — Calgary tech CCPC

### Facts

- **Corporation**: Cascade Code Inc., a CCPC incorporated in Alberta, FYE December 31, 2025
- **Single PE**: Calgary, Alberta (100% Alberta allocation per federal Schedule 5)
- **Gross revenue**: $2,000,000 (Canadian-source SaaS development services)
- **Net income for tax purposes (line 300, federal T2)**: $400,000
- **Active business income (ABI)**: $300,000 (after federal Schedule 7 calculation)
- **Investment income**: $20,000 (interest on cash reserves)
- **Taxable capital employed in Canada (TCEC)**: $3,200,000 (below $10M — no TCEC grind)
- **Associated corporations**: none
- **SR&ED qualified expenditures (Alberta)**: $250,000 (current-year)
- **Prior 2-year average Alberta R&D spend**: $180,000

### Step 1 — Federal T2 (for context)

- ABI eligible for SBD: $300,000 (all under $500,000 limit, no grind)
- Federal SBD-rate tax: $300,000 × 9% = **$27,000**
- Federal general-rate tax on remaining $100,000 ($400,000 − $300,000 ABI): $100,000 × 15% = **$15,000**
- Federal Part I refundable on investment income: not separately computed here; subsumed in T2 mechanics
- **Federal tax (Part I, simplified)**: ~$42,000 before credits

### Step 2 — Alberta AT1 — Schedule 21 tax payable

- **Alberta taxable income**: $400,000 (100% Alberta allocation)
- **SBD-rate portion** (matches federal SBD claim): $300,000 × **2%** = **$6,000**
- **General-rate portion**: $100,000 × **8%** = **$8,000**
- **Alberta tax before credits**: **$14,000**

### Step 3 — Innovation Employment Grant (AT1 Schedule 13 + 29)

- Eligible AB SR&ED expenditures: $250,000
- Prior 2-year average: $180,000
- **Base credit** (8% on first $4M of $250,000): $250,000 × 8% = **$20,000**
- **Incremental credit** (20% on amount above prior 2-yr avg, up to $4M cap):
  - Incremental: $250,000 − $180,000 = $70,000
  - 20% × $70,000 = **$14,000**
- **Total IEG**: $20,000 + $14,000 = **$34,000** (refundable)

### Step 4 — Net AT1 result

- Alberta tax before credits: $14,000
- Less: IEG (refundable): ($34,000)
- **Alberta net refund: $20,000**
- (The IEG creates a refundable position because credits exceed tax payable; TRA issues the refund.)

### Step 5 — Combined effective Alberta rate (this example)

- Pre-credit combined federal + AB on $400,000:
  - SBD portion: $300,000 × 11% = $33,000
  - General portion: $100,000 × 23% = $23,000
  - Combined pre-IEG: **$56,000** (14% effective)
- Post-IEG (Alberta refunds $20,000, federal SR&ED ITC computed separately):
  - Effective combined rate drops materially once both IEG and federal SR&ED ITC are factored in.

### Step 6 — Deliverables for the client

1. AT1 return + Schedules 1, 13, 21, 29
2. Federal T2 with consistent Schedule 1, 7, 23, 31, 49 entries
3. T661 federal SR&ED claim (Alberta-located expenditures flagged for IEG cross-reference)
4. IEG refund expected: ~$20,000 (subject to TRA processing — typical 6–9 months from filing)
5. Instalment recalculation for 2026 based on 2025 AT1 tax

## 12. Conservative defaults

- **Conservative default rules** — When information is missing, the skill applies these conservative defaults (always flag for reviewer confirmation): 1. **Allocation %**: If federal Schedule 5 not yet finalized, assume **100% Alberta** only when the corporation has confirmed sole-PE Alberta status; otherwise **refuse** and request allocation. 2. **CCPC status**: Confirm CCPC status throughout the year — do **not** assume; non-CCPC status disqualifies SBD entirely. 3. **Associated group sharing**: Default the SBD allocation to **$0 for the subject corporation** until associated group T2-Sch 23 allocation is confirmed in writing. 4. **TCEC grind**: If TCEC near $10M, apply **full grind treatment** (assume worst case) until prior-year T2 Schedule 33 is reviewed. 5. **IEG prior-2-year average**: If unavailable, compute **base 8% only** (no incremental); flag for reviewer to add incremental after historic data confirmation. 6. **IEG eligibility**: Apply **only to expenditures with documented Alberta location** (work performed at AB PE, AB-resident employees); refuse to extend to ambiguous remote-work expenditures without payroll address evidence. 7. **AITC / CITC carry-forwards**: Assume **none** unless prior AT1 Schedule 10 / TRA approval letter confirms balance. 8. **Instalment base**: Default to **prior-year method** unless current-year estimate is substantially lower and documented. 9. **Filing penalty exposure**: Flag any late filing — even by 1 day — for immediate reviewer escalation.

## 13. Sources

### Primary law

- **Primary law sources** — - **Alberta Corporate Tax Act, RSA 2000, c A-15** — the operative statute - s.21: General corporate income tax rate - s.22: Small business deduction - s.26.6: Innovation Employment Grant - s.35: Exempt corporations - **Alberta Corporate Tax Regulation, Alta Reg 119/2008** - **Bill 3, Job Creation Tax Cut Act, 2019** (general rate reduction to 8%) - **Bill 20, Fiscal Measures and Taxation Act, 2019** (AITC elimination)  _(Alberta Corporate Tax Act, RSA 2000, c A-15)_

### Federal coordination

- **Federal coordination sources** — - **Income Tax Act (Canada), RSC 1985, c 1 (5th Supp)** — s.123–125 (federal CIT and SBD), s.37 + Reg 2900 (SR&ED expenditures used for IEG base)  _(Income Tax Act (Canada), RSC 1985, c 1 (5th Supp))_

### Administrative guidance

- **Administrative guidance sources** — - **TRA Information Circular CT-1** — Filing the AT1 - **TRA Information Circular CT-17** — Innovation Employment Grant guide - **TRA Information Circular CT-2** — Alberta Small Business Deduction - **TRA Information Circular IC-PEN-1** — Penalties and interest - **TRA Client Self-Service (TRACS)** — corporate account registration and filing portal - **Alberta Treasury Board and Finance — Corporate Income Tax** program page

### Federal forms (cross-referenced)

- **Federal forms cross-referenced** — - **T2 Corporation Income Tax Return** + Schedules 1, 5, 7, 23, 31, 33, 49 - **T661 SR&ED Expenditures Claim** (Alberta-located expenditures feed IEG)

### Rate confirmation

- **2025 rate confirmation** — Alberta Budget 2025 (tabled February 27, 2025) — reaffirmed 8% general / 2% SBD rates for the 2025 tax year; no rate changes announced.  _(Alberta Budget 2025 (tabled February 27, 2025))_

## End of Skill v1.0 — Alberta Corporate Income Tax

**End of Skill v1.0 — Alberta Corporate Income Tax**

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
