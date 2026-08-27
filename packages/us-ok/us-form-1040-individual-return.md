---
name: us-form-1040-individual-return
description: Tier 2 US federal content skill for preparing Form 1040 — the standard individual income tax return for non-freelance taxpayers (W-2 employees, retirees, investors, families). Covers tax year 2025 under OBBBA including the $40k SALT cap, the $15,750/$31,500/$23,625 standard deduction, capital gains brackets (0/15/20%), the §1411 3.8% NIIT, AMT post-TCJA, Schedule 1/2/3 walkthrough, dependents and filing status, kiddie tax §1(g), and itemized deduction Schedule A. Distinct from us-federal-return-assembly which orchestrates Schedule C freelance returns. Federal only.
jurisdiction: US
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: Christopher Aryee
review_status: current
tier: 1
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# US Form 1040 Individual Return

## US Form 1040 — Individual Income Tax Return (Non-Freelance)

Tier 2 federal content skill. Covers tax year **2025** under the One Big Beautiful Bill Act (OBBBA, P.L. 119-21, July 4 2025). MUST be loaded alongside `us-tax-workflow-base` v0.2 or later. Federal only — no state tax. Assumes a Circular 230 practitioner reviews and signs off on every output before delivery.

## 1. Scope

### 1.1 In scope

This skill prepares **Form 1040** and its three core schedules (1, 2, 3) plus **Schedule A** (itemized deductions), **Schedule B** (interest & dividends if required), **Schedule D** (capital gains), and **Form 8606** (basis tracking) for the typical American taxpayer who is **not** primarily self-employed:

- W-2 wage earners (single filer or married filing jointly)
- Retirees with Social Security, pension, IRA/401(k) distributions, RMDs
- Investors with brokerage 1099-B, 1099-DIV, 1099-INT
- Families with qualifying children, dependent care, education credits, HSAs
- Homeowners with mortgage interest and property tax (Schedule A)
- Taxpayers with **small** side income reported on Schedule 1 Line 8 (hobby income, gambling winnings, jury duty, prizes) but NOT a trade or business

### 1.2 Out of scope — refer out

**Out of scope — refer out**

| Situation | Skill to load instead |
| --- | --- |
| Schedule C self-employment income | `us-sole-prop-bookkeeping` + `us-schedule-c-and-se-computation` + `us-federal-return-assembly` |
| Single-member LLC disregarded for federal tax | `us-federal-return-assembly` (federal) and the state assembly skill |
| §199A QBI deduction with positive QBI | `us-qbi-deduction` (this skill assumes Line 13 = 0 for pure W-2 / investment income) |
| Quarterly estimated tax planning for 2026 | `us-quarterly-estimated-tax` |
| Foreign tax credit (Form 1116) | `us-foreign-tax-credit-1116` |
| Education credits (Form 8863) AOTC/LLC | `us-education-credits-8863` |
| Foreign earned income exclusion (Form 2555) | `us-foreign-earned-income-2555` |
| Estate / gift returns (Form 706 / 709) | `us-estate-gift-706-709` |
| Partnership K-1 with material participation issues | `us-form-1065-partnership` |
| S-corp election analysis | `us-s-corp-election-decision` |
| State returns | State-specific skill (e.g. `ca-540-individual-return`) |

### 1.3 Refusal catalogue

- **Dual-status alien** — Taxpayer is a dual-status alien in the filing year (departing or arriving US resident)  _(1.3 Refusal catalogue)_
- **§877A expatriation issues** — Taxpayer has §877A expatriation issues (covered expatriate, mark-to-market)  _(1.3 Refusal catalogue)_
- **Non-resident alien filing 1040-NR** — Non-resident alien filing Form 1040-NR (different skill — not yet built)  _(1.3 Refusal catalogue)_
- **Innocent spouse relief** — Innocent spouse relief (Form 8857) is being claimed  _(1.3 Refusal catalogue)_
- **FBAR/FATCA large foreign accounts** — FBAR (FinCEN 114) or Form 8938 FATCA with $100k+ aggregate foreign accounts — coordinate with separate international skill  _(1.3 Refusal catalogue)_
- **Streamlined Filing Compliance / OVDP** — Streamlined Filing Compliance Procedures or OVDP for unreported foreign assets  _(1.3 Refusal catalogue)_
- **Active IRS examination/CP2000/appeals** — Active IRS examination, CP2000, or appeals — those require a tax controversy practitioner  _(1.3 Refusal catalogue)_
- **Trust/estate beneficiary K-1 with foreign/AMT preferences** — Taxpayer is a trust or estate beneficiary receiving Schedule K-1 with foreign or alternative minimum tax preferences flowing through  _(1.3 Refusal catalogue)_

## 2. Tax year 2025 figures — Rev. Proc. 2024-40 + OBBBA

### 2.1 Standard deduction (§63(c))

**Standard deduction table**  _(§63(c))_

| Filing status | 2025 amount |
| --- | --- |
| Single | **$15,750** |
| Married filing jointly (MFJ) | **$31,500** |
| Married filing separately (MFS) | $15,750 |
| Head of household (HoH) | **$23,625** |
| Qualifying surviving spouse (QSS) | $31,500 |

- **Additional standard deduction (age 65+ or blind)** — MFJ / QSS: $1,600 per qualifying condition per spouse; Single / HoH: $2,000 per qualifying condition (2025). For 2026 the indexed amounts are $1,650 for married individuals and $2,050 for unmarried individuals; an MFJ couple where both spouses are 65 or older claims a 2026 standard deduction of $35,500 (OBBBA §70102; IRS Pub 501)  _(§63(c))_
- **Dependent standard deduction limitation** — A taxpayer who can be claimed as a dependent on another return is limited to the greater of (a) $1,350 or (b) earned income + $450, capped at the regular standard deduction.  _(§63(c))_

### 2.2 Ordinary income tax brackets — §1(j) (post-TCJA, OBBBA-permanent)

- **Permanence of §1(j) rates** — OBBBA P.L. 119-21 §70101 made the §1(j) rates permanent (eliminating the 12/31/2025 sunset). Brackets indexed under Rev. Proc. 2024-40.  _(OBBBA P.L. 119-21 §70101; Rev. Proc. 2024-40)_

**Single (2025) tax brackets**  _(§1(j))_

| Rate | Taxable income |
| --- | --- |
| 10% | $0 – $11,925 |
| 12% | $11,925 – $48,475 |
| 22% | $48,475 – $103,350 |
| 24% | $103,350 – $197,300 |
| 32% | $197,300 – $250,525 |
| 35% | $250,525 – $626,350 |
| 37% | over $626,350 |

**MFJ (2025) tax brackets**  _(§1(j))_

| Rate | Taxable income |
| --- | --- |
| 10% | $0 – $23,850 |
| 12% | $23,850 – $96,950 |
| 22% | $96,950 – $206,700 |
| 24% | $206,700 – $394,600 |
| 32% | $394,600 – $501,050 |
| 35% | $501,050 – $751,600 |
| 37% | over $751,600 |

**HoH (2025) tax brackets**  _(§1(j))_

| Rate | Taxable income |
| --- | --- |
| 10% | $0 – $17,000 |
| 12% | $17,000 – $64,850 |
| 22% | $64,850 – $103,350 |
| 24% | $103,350 – $197,300 |
| 32% | $197,300 – $250,500 |
| 35% | $250,500 – $626,350 |
| 37% | over $626,350 |

### 2.3 Capital gains brackets — §1(h)

**Capital gains brackets**  _(§1(h))_

| Rate | Single | MFJ | HoH |
| --- | --- | --- | --- |
| 0% | up to $48,350 | up to $96,700 | up to $64,750 |
| 15% | $48,350 – $533,400 | $96,700 – $600,050 | $64,750 – $566,700 |
| 20% | over $533,400 | over $600,050 | over $566,700 |

- **§1250 unrecaptured gain (real estate depreciation recapture)** — 25% maximum  _(§1250)_
- **Collectibles (art, coins, gold, NFTs)** — 28% maximum  _(§1(h))_
- **Qualified small business stock (§1202)** — exclusion 50/75/100% depending on acquisition date; for stock acquired after July 4, 2025, OBBBA §70431 phases the exclusion by holding period instead: 50% at 3 years, 75% at 4 years, 100% at 5 years, with a $15 million per-issuer cap and a $75 million aggregate gross asset test  _(§1202)_
- **Short-term capital gain taxation** — Short-term capital gain (held ≤ 1 year): taxed at ordinary rates per §2.2.  _(§1(h))_

### 2.4 AMT exemption — §55(d) (post-TCJA, OBBBA-permanent)

**AMT exemption table**  _(§55(d))_

| Filing status | Exemption | Phaseout begins | Fully phased out |
| --- | --- | --- | --- |
| Single / HoH | $88,100 | $626,350 | $978,750 |
| MFJ / QSS | $137,000 | $1,252,700 | $1,800,700 |
| MFS | $68,500 | $626,350 | $900,350 |

- **AMT rates** — 26% on AMTI up to $239,100 (all filers except MFS: $119,550); 28% above. The exemption phases out at $0.25 per $1 of AMTI over the phaseout threshold.  _(§55(d))_

### 2.5 NIIT (Net Investment Income Tax) — §1411

**NIIT MAGI thresholds**  _(§1411)_

| Filing status | MAGI threshold |
| --- | --- |
| Single / HoH | $200,000 |
| MFJ / QSS | $250,000 |
| MFS | $125,000 |

- **NIIT rate** — 3.8% on the lesser of (a) net investment income or (b) MAGI excess over threshold  _(§1411)_
- **Not indexed** — these thresholds are statutory and have not changed since §1411 was enacted by ACA in 2010.  _(§1411)_

### 2.6 Additional Medicare Tax — §3101(b)(2) and §1401(b)(2)

**Additional Medicare Tax thresholds**  _(§3101(b)(2) and §1401(b)(2))_

| Filing status | Threshold |
| --- | --- |
| Single / HoH | $200,000 |
| MFJ | $250,000 |
| MFS | $125,000 |

- **Additional Medicare Tax rate** — 0.9% on wages/SE income over threshold  _(§3101(b)(2) and §1401(b)(2))_
- **Reporting** — Reported on Form 8959, flows to Schedule 2 Line 11. Employer withholds the 0.9% on wages over $200,000 regardless of filing status; the return reconciles.  _(§3101(b)(2) and §1401(b)(2))_

### 2.7 SALT cap — §164(b)(6) as amended by OBBBA

- **Pre-OBBBA SALT cap** — $10,000 cap (TCJA 2017)  _(§164(b)(6))_
- **OBBBA elevated SALT cap** — $40,000 for 2025 (MFS: $20,000), codified in OBBBA §70120. The elevated cap is temporary: it applies for tax years 2025-2029 with annual inflation adjustment (2026 applicable limitation amount: $40,400) and reverts to the $10,000 limit after December 31, 2029. MFS taxpayers get half ($20,000).  _(OBBBA P.L. 119-21 §70401)_
- **SALT cap phaseout** — PHASEOUT (OBBBA §70120(b)): The elevated SALT cap phases down for taxpayers with MAGI over $500,000 ($250,000 MFS); the thresholds are inflation-adjusted ($505,000 for 2026). The cap is reduced by 30% of excess MAGI, but not below $10,000. Worked example (2026, Single, $550,000 MAGI): excess MAGI = $550,000 - $505,000 = $45,000; reduction = $45,000 × 30% = $13,500; cap = $40,400 - $13,500 = $26,900. Practical effect: fully elevated $40k cap is available up to $500k MAGI; phases to $10k floor by approximately $600k MAGI.  _(OBBBA §70401(b))_

### 2.8 Kiddie tax — §1(g)

- **Kiddie tax unearned income threshold** — For tax year 2025: a child's unearned income over $2,700 is taxed at the parents' marginal rate.  _(§1(g))_
- **Kiddie tax applicability** — Applies to: Children under 18 at year-end, OR Children 18 with earned income ≤ half their support, OR Children 19-23 who are full-time students with earned income ≤ half their support  _(§1(g))_
- **Form 8615 / Form 8814 election** — Computed on Form 8615. Parents may elect to report the child's unearned income on their own return via Form 8814 if the child has only interest/dividend income under $13,500 (2025) and the child files no other return.  _(§1(g))_

### 2.9 Other OBBBA changes

- **§199A QBI** — made permanent at 20% (OBBBA §70105); the final OBBBA did not enact the proposed 23% rate. §70105 instead increased the phase-in threshold to $75,000 ($150,000 joint) and established a $400 minimum deduction for active qualified business income. Not applicable to pure W-2 / investment returns (Line 13 = 0) but flag if Schedule K-1 PTP income or REIT dividends are present — these qualify for QBI even without a trade or business.  _(§199A)_
- **§1(j) brackets permanence** — permanent (see §2.2).  _(§1(j))_
- **Standard deduction increase** — increased for 2025 under OBBBA (see §2.1).  _(OBBBA)_
- **Child Tax Credit** — $2,200 per qualifying child under 17 (§24(h)), refundable portion $1,700 in 2025 (Rev. Proc. 2024-40), made permanent by OBBBA §70104. Phaseout begins $400k MFJ / $200k other.  _(§24(h); OBBBA §70301; Rev. Proc. 2024-40)_
- **§25D Residential Clean Energy Credit termination** — AUDIT FLASH POINT — OBBBA accelerated termination. Pre-OBBBA the credit phased to 26% in 2033 and 22% in 2034. OBBBA P.L. 119-21 §70506 terminated the credit for property placed in service after December 31 2025 for most categories (solar, geothermal heat pump, small wind, biomass) — verify against IRS guidance Notice 2025-XX before claiming for late-2025 installations. Battery storage and fuel cells may have different effective dates. Flag to reviewer.  _(OBBBA P.L. 119-21 §70501)_
- **§30D Clean Vehicle Credit termination** — OBBBA P.L. 119-21 §70502 terminated §30D for vehicles acquired after September 30 2025. Vehicles placed in service through 9/30/2025 still qualify under the existing point-of-sale transferable election rules. Flag to reviewer for any 2025 EV purchase — confirm date of acquisition vs date of placement in service.  _(OBBBA P.L. 119-21 §70502)_
- **§25E Used Clean Vehicle Credit termination** — also terminated 9/30/2025 under OBBBA §70502.  _(OBBBA §70502)_
- **Tip income deduction** — NEW under OBBBA §70201 — up to $25,000 of qualified tip income deductible above-the-line for occupations on the IRS-published tip-receiving occupations list (Treasury list issued under OBBBA §70201). Phases out above $150k single / $300k MFJ. Reported on Schedule 1.  _(OBBBA §70601)_
- **Overtime pay deduction** — NEW under OBBBA §70202 — up to $12,500 single / $25,000 MFJ of FLSA-mandated overtime premium pay deductible above-the-line. Same phaseout. Reported on Schedule 1.  _(OBBBA §70602)_
- **Auto loan interest deduction** — NEW under OBBBA §70203 — up to $10,000 of interest on a loan for a US-assembled passenger vehicle deductible above-the-line. Phases out $100k single / $200k MFJ. Reported on Schedule 1.  _(OBBBA §70603)_

## 3. Filing status and dependents

### 3.1 Filing status determination — §1 and §2

- **Status determination date** — Status is determined on December 31 of the tax year (§7703).  _(§7703)_
- **Single** — unmarried, not HoH, not QSS.  _(§1)_
- **Married filing jointly (MFJ)** — married on 12/31, both spouses agree to file jointly, joint and several liability under §6013.  _(§6013)_
- **Married filing separately (MFS)** — married on 12/31, file separately. Generally inferior — disqualifies from EITC, education credits, student loan interest deduction, child & dependent care credit, exclusion of US savings bond interest for education, traditional IRA deduction if spouse is covered, and the elderly/disabled credit. SALT cap halved. Use only when justified (innocent spouse protection, income-driven student loan repayment, large medical expenses on one spouse).  _(§1)_
- **Head of household (HoH)** — unmarried (or "considered unmarried" — lived apart from spouse last 6 months and home is principal residence of qualifying child) AND paid more than half the cost of keeping up a home that was the principal residence for more than half the year of a qualifying person: A qualifying child (any age if permanently disabled, otherwise under 19 or under 24 if full-time student); A qualifying relative who is the taxpayer's parent (parent need not live with taxpayer); Another qualifying relative who lived with taxpayer more than half the year  _(§2(b))_
- **Qualifying surviving spouse (QSS)** — spouse died in one of the two preceding tax years, taxpayer has not remarried, taxpayer maintained a home for a qualifying child for the whole year, and taxpayer would have been entitled to file jointly in the year of death. Get MFJ brackets and standard deduction. After two years, file as single or HoH.  _(§2(a))_

### 3.2 Qualifying child — §152(c)

- **Qualifying child tests** — All five tests must be met: 1. Relationship: child, stepchild, foster child, sibling, half-sibling, step-sibling, or descendant of any of these. 2. Age: under 19 at year-end, OR under 24 and full-time student for at least 5 months, OR any age if permanently and totally disabled. 3. Residency: lived with taxpayer for more than half the year (temporary absences for school, illness, military service count as present). 4. Support: child did not provide more than half of their own support. 5. Joint return: child is not filing a joint return (unless only to claim a refund of withholding).  _(§152(c))_

### 3.3 Qualifying relative — §152(d)

- **Qualifying relative tests** — All four tests must be met: 1. Not a qualifying child: of the taxpayer or any other taxpayer. 2. Relationship or residency: either related to taxpayer per the §152(d)(2) list (parents, siblings, in-laws, etc. — these need not live with taxpayer) OR lived with taxpayer as a member of the household for the entire year. 3. Gross income: dependent's gross income must be less than the §151(d)(4) exemption amount, which for 2025 is $5,200 (Rev. Proc. 2024-40). Social Security benefits are generally excluded from "gross income" for this test if not taxable to the dependent. 4. Support: taxpayer provided more than half of the dependent's total support.  _(§152(d); §151(d)(4); Rev. Proc. 2024-40)_

### 3.4 Tiebreaker rules — §152(c)(4)

- **Tiebreaker rules** — When two or more taxpayers could claim the same qualifying child: 1. Parent prevails over non-parent. 2. If both are parents who don't file jointly: parent with whom child lived longer; if equal, parent with higher AGI. 3. If no parent claims the child: the eligible taxpayer with the highest AGI prevails.  _(§152(c)(4))_

## 4. Income — Form 1040 lines 1-8

### 4.1 Line 1: Wages and related

**Line 1 wages breakdown**

| Sub-line | Item | Source |
| --- | --- | --- |
| 1a | W-2 Box 1 wages | Form W-2 |
| 1b | Household employee wages NOT on W-2 | Schedule H / records |
| 1c | Tip income NOT reported to employer | Form 4137 |
| 1d | Medicaid waiver payments excluded under §131 | Notice 2014-7 |
| 1e | Taxable dependent care benefits | Form 2441 Part III |
| 1f | Employer-provided adoption benefits | Form 8839 |
| 1g | Wages from Form 8919 (uncollected SS/Medicare) | Form 8919 |
| 1h | Other earned income | various |
| 1i | Nontaxable combat pay election | W-2 Box 12 code Q |
| 1z | Sum of 1a through 1h (1i is informational only) | computed |

- **Common issues** — Multiple W-2s: sum Box 1 figures into 1a. Sum Box 2 federal withholding into Line 25a. Excess Social Security tax withheld (two employers, combined wages over $176,100 in 2025): the excess employee SS tax (6.2% × excess) is credited on Schedule 3 Line 11. Statutory employees (W-2 Box 13 "Statutory employee" checked): wages go on Schedule C, not Line 1a. Refer to `us-sole-prop-bookkeeping`. Disability pension before minimum retirement age: report on Line 1h, not Line 5b.

### 4.2 Line 2: Interest income

- **Line 2a — tax-exempt interest** — Tax-exempt interest (municipal bonds, mutual fund exempt-interest dividends). Reported informationally only. Watch: private activity bond interest from these may be an AMT preference (§57(a)(5)).  _(§57(a)(5))_
- **Line 2b — taxable interest** — Includes: Bank/CD interest (1099-INT Box 1); US Treasury interest (1099-INT Box 3) — taxable federally, exempt from state tax; Original issue discount (1099-OID); Seller-financed mortgage interest received; Interest on income tax refunds (1099-INT from IRS or state)
- **Schedule B requirement** — Schedule B required when (a) taxable interest > $1,500, (b) tax-exempt interest is from a private activity bond, (c) seller-financed mortgage interest, or (d) foreign account or foreign trust ownership (Part III FBAR questions).

### 4.3 Line 3: Dividends

- **Line 3a — qualified dividends** — Qualified dividends (1099-DIV Box 1b) — taxed at capital gains rates per §2.3. Must satisfy §1(h)(11) holding period (more than 60 days during the 121-day period beginning 60 days before ex-dividend date; 90 of 181 for preferred stock).  _(§1(h)(11))_
- **Line 3b — ordinary dividends** — Ordinary dividends (1099-DIV Box 1a) — includes qualified dividends; reports the total.
- **Schedule B requirement for dividends** — Schedule B required if Line 3b > $1,500.

### 4.4 Line 4: IRA distributions

- **Line 4a/4b overview** — Line 4a: Gross IRA distributions (1099-R from traditional, SEP, SIMPLE IRAs); Line 4b: Taxable portion
- **Determining 4b — no basis** — Traditional IRA with all-deductible contributions (no basis): 4b = 4a.
- **Determining 4b — basis from nondeductible contributions** — Traditional IRA with basis from nondeductible contributions (Form 8606 history): pro-rata recovery via Form 8606 Part I.
- **Roth IRA distribution ordering rules** — Roth IRA distribution: tax-free if qualified (5-year holding + age 59½ or other qualifying event). Otherwise ordering rules: contributions first (tax-free), conversions next (10% penalty if within 5 years, otherwise tax-free), earnings last (taxable + 10% penalty).
- **Qualified charitable distribution (QCD)** — up to $108,000 in 2025 (Rev. Proc. 2024-40), age 70½+, direct from IRA trustee to qualified charity. Excluded from 4b — write "QCD" next to Line 4b.  _(Rev. Proc. 2024-40)_
- **Rollover** — write "Rollover" next to Line 4b, 4b = 0 if direct trustee-to-trustee or completed within 60 days.
- **RMD failure penalty** — pre-SECURE 2.0 penalty was 50%; under SECURE 2.0 it is 25%, reduced to 10% if corrected within the correction window. Reported on Form 5329.  _(SECURE 2.0)_

### 4.5 Line 5: Pensions and annuities

- **Line 5a/5b overview** — Line 5a: Gross distributions (1099-R from employer plans, 401(k), 403(b), 457, defined benefit); Line 5b: Taxable portion
- **Determining 5b** — Fully taxable if all contributions were pre-tax (most 401(k) distributions). Simplified method (Pub 575 / 939) if after-tax contributions are present and pension started after 11/18/1996. General rule for older annuities. Lump-sum distribution with NUA (net unrealized appreciation) of employer securities: use Form 4972.

### 4.6 Line 6: Social Security benefits

- **Lines 6a/6b/6c overview** — Line 6a: Gross SSA-1099 / RRB-1099 benefits; Line 6b: Taxable portion (0%, up to 50%, or up to 85%); Line 6c: Lump-sum election checkbox (if claiming the §86(e) election to spread prior-year benefits)  _(§86(e))_
- **Computation method** — Computation: Pub 915 Worksheet 1 (or the worksheet in the Form 1040 instructions).
- **AUDIT FLASH POINT — SS taxable amount miscomputed** — This is one of the most common errors on retiree returns. The "provisional income" formula is AGI (excluding SS) + tax-exempt interest + 50% of SS benefits. If provisional income exceeds the first threshold ($25k single / $32k MFJ), up to 50% of benefits is taxable. Above the second threshold ($34k single / $44k MFJ), up to 85% is taxable. These thresholds are statutory under §86(c) and have not been indexed since 1983/1993. The "50% of SS in provisional income" trips up many DIY preparers who use 100%. Show the Pub 915 worksheet in the work file.  _(§86(c))_

### 4.7 Line 7: Capital gains

- **Line 7 sourcing** — From Schedule D Line 16. If only capital gain distributions from mutual funds (1099-DIV Box 2a) and no other capital gain transactions, taxpayer can skip Schedule D and enter the amount directly on Line 7 with the Schedule D checkbox unchecked.

### 4.8 Line 8: Other income (from Schedule 1 Line 10)

See §5.

### 4.9 Line 9: Total income

- **Total income formula** — Sum of Lines 1z, 2b, 3b, 4b, 5b, 6b, 7, 8.  _(Form 1040)_

### 4.10 Line 10: Adjustments to income (from Schedule 1 Line 26)

See §5.

### 4.11 Line 11: AGI

- **AGI formula** — Line 9 minus Line 10.  _(Form 1040)_

## 5. Schedule 1 — Additional Income and Adjustments

### 5.1 Part I — Additional income (flows to 1040 Line 8)

**Schedule 1 Part I table**

| Line | Item | Notes |
| --- | --- | --- |
| 1 | Taxable refunds of state/local tax | Only if itemized in prior year and got tax benefit (§111 tax benefit rule) |
| 2a | Alimony received | Pre-2019 divorce decrees only (TCJA §11051) |
| 3 | Business income / loss | Schedule C — refer to freelance skill |
| 4 | Other gains/losses | Form 4797 (depreciable business property, §1231) |
| 5 | Rental real estate, royalties, partnerships, S corps, trusts | Schedule E |
| 6 | Farm income/loss | Schedule F |
| 7 | Unemployment compensation | 1099-G Box 1 |
| 8a | Net operating loss | §172 |
| 8b | Gambling winnings | W-2G; losses deductible only as itemized misc up to winnings under §165(d) |
| 8c | Cancellation of debt | 1099-C — but check §108 exclusions (insolvency, qualified principal residence indebtedness extended under OBBBA §70405 through 2026, bankruptcy, qualified farm/real property business) |
| 8d | Foreign earned income exclusion | Form 2555 (NEGATIVE amount) — refer to `us-foreign-earned-income-2555` |
| 8e | Income from Form 8853 (Archer MSA) |  |
| 8f | Income from Form 8889 (HSA distributions for non-medical) |  |
| 8g | Alaska Permanent Fund dividends |  |
| 8h | Jury duty |  |
| 8i | Prizes and awards | Includes Olympic/Paralympic medals (taxable above $1M AGI under §74(d)) |
| 8j | Activity not for profit (hobby income) | §183 — see §16 audit flash point |
| 8k | Stock options | Non-qualified options exercised — usually already in W-2 Box 1 |
| 8l | Income from rental of personal property | Not Schedule E business |
| 8m | Olympic/Paralympic medals |  |
| 8n | §951(a) Subpart F inclusion | International — refer out |
| 8o | §951A GILTI inclusion | Refer to `us-gilti-fdii-beat` |
| 8p | §461(l) excess business loss disallowed | Re-included in income |
| 8q | Tax credit bond interest |  |
| 8r | Scholarship/fellowship not reported on W-2 |  |
| 8s | Nontaxable amount of pension from work not covered by SS |  |
| 8t | Pension/annuity from a non-qualified deferred comp plan | §457 from tax-exempt orgs |
| 8u | Wages from Form 8919 | If on Line 1g already, skip here |
| 8v | Digital asset received as reward/award/payment | Property transaction — refer to `us-digital-asset-transactions` if material |
| 8z | Other income | Itemize on a statement |
| 9 | Total other income | sum 8a-8z |
| 10 | Total additional income | sum 1-9 → 1040 Line 8 |

### 5.2 Part II — Adjustments to income (flows to 1040 Line 10)

**Schedule 1 Part II table**

| Line | Item | Notes |
| --- | --- | --- |
| 11 | Educator expenses | Up to $300 for K-12 teachers, instructors, counselors who worked 900+ hours |
| 12 | Business expenses for reservists, performing artists, fee-basis gov officials | Form 2106 |
| 13 | HSA deduction | Form 8889 — 2025 limits: $4,300 self-only / $8,550 family, +$1,000 catch-up age 55+ |
| 14 | Moving expenses | Active-duty military PCS only (TCJA §11049) |
| 15 | Deductible part of SE tax | Schedule SE Line 13 — refer out |
| 16 | SEP / SIMPLE / qualified plans | Refer to `us-self-employed-retirement` |
| 17 | Self-employed health insurance deduction | Refer to `us-self-employed-health-insurance` |
| 18 | Penalty on early withdrawal of savings | 1099-INT Box 2 |
| 19a | Alimony paid | Pre-2019 decrees only |
| 19b | Recipient SSN |  |
| 19c | Date of original divorce/separation |  |
| 20 | IRA deduction | Traditional IRA — 2025 limits $7,000 / $8,000 age 50+ catch-up; phaseout for active participants in employer plan |
| 21 | Student loan interest deduction | Up to $2,500; phaseout $80k-$95k single / $165k-$195k MFJ (2025) |
| 22 | Reserved |  |
| 23 | Archer MSA deduction |  |
| 24a | Jury duty pay turned over to employer |  |
| 24b | Deductible expenses related to Line 8l (personal property rental) |  |
| 24c | Nontaxable Olympic/Paralympic medals | If Line 8m |
| 24d | Reforestation amortization / expense |  |
| 24e | Repayment of supplemental unemployment |  |
| 24f | Contributions to §501(c)(18)(D) plans |  |
| 24g | Contributions by certain chaplains to §403(b) |  |
| 24h | Attorney fees and court costs for §62(a)(20) discrimination suits |  |
| 24i | Attorney fees and court costs for whistleblower awards |  |
| 24j | Housing deduction (Form 2555) |  |
| 24k | Excess deferrals (e.g., over-contribution to 401(k)) |  |
| 24l | OBBBA Tip deduction | NEW — see §2.9; up to $25,000 |
| 24m | OBBBA Overtime deduction | NEW — see §2.9 |
| 24n | OBBBA Auto loan interest deduction | NEW — see §2.9 |
| 24z | Other adjustments |  |
| 25 | Total other adjustments | sum 24a-24z |
| 26 | Total adjustments to income | sum 11-23, 25 → 1040 Line 10 |

### 5.3 IRA deduction phaseout (Line 20) — 2025

**IRA deduction phaseout table**

| Filing status | Phaseout range |
| --- | --- |
| Single / HoH, active participant | $79,000 – $89,000 MAGI |
| MFJ, taxpayer active participant | $126,000 – $146,000 MAGI |
| MFJ, only spouse active participant | $236,000 – $246,000 MAGI |
| MFS, active participant | $0 – $10,000 MAGI |

- **No income limit / Roth phaseouts** — If neither spouse is an active participant, no income limit. Roth IRA contribution (not deductible but tracked) phaseouts for 2025: $150,000-$165,000 single / $236,000-$246,000 MFJ.

## 6. Standard vs itemized — Schedule A

### 6.1 The decision

- **Standard vs itemized decision** — Compare standard deduction (§2.1) against the sum of Schedule A items. The taxpayer takes the greater unless filing MFS where one spouse itemizes (then both must — §63(c)(6)).  _(§63(c)(6))_

### 6.2 Schedule A line-by-line

- **Medical and dental — Lines 1-4** — deductible to extent total exceeds 7.5% of AGI (§213(a) post-TCJA permanent). Includes premiums (other than self-employed health insurance taken above the line), prescription drugs, doctors, dentists, surgery, mental health, long-term care insurance (subject to age-based caps), medical mileage at 21¢/mile for 2025 (Notice 2025-XX), home modifications for medical purposes.  _(§213(a))_
- **Taxes paid — Lines 5-7 — SALT cap** — Line 5a: State and local income tax OR general sales tax (election) — sales tax via the IRS optional sales tax tables in Pub 600 / Schedule A instructions, plus actual receipts for big-ticket items. Line 5b: State and local real estate tax (excluding rental property — that goes on Schedule E). Line 5c: State and local personal property tax (e.g., car registration based on value). Line 5d: Sum 5a + 5b + 5c. Line 5e: Lesser of 5d or SALT cap (see §2.7 — $40,000 / $20,000 MFS for 2025, phased down above $500k/$250k MAGI). Line 6: Other taxes (foreign income tax NOT used for FTC, occupational taxes). Line 7: Sum 5e + 6
- **Interest paid — Lines 8-10** — Line 8a: Home mortgage interest from 1098 (acquisition debt up to $750,000 post-12/15/2017 origination; $1,000,000 grandfathered for older debt — §163(h)(3) as amended by TCJA, made permanent by OBBBA §70108). Line 8b: Mortgage interest not on 1098 (seller-financed; report payee name, address, SSN/EIN). Line 8c: Points not on 1098. Line 8d: Mortgage insurance premiums. OBBBA §70108 amended IRC §163(h)(3)(F) to treat qualified mortgage insurance premiums as qualified residence interest, so they are deductible again; this line is no longer Reserved. Line 8e: Sum. Line 9: Investment interest (Form 4952) — limited to net investment income. Line 10: Sum 8e + 9  _(§163(h)(3); OBBBA §70110)_
- **Home equity interest deductibility** — Home equity interest is deductible only if proceeds used to buy, build, or substantially improve the residence securing the loan (§163(h)(3)(F) post-TCJA). Cash-out for personal use is nondeductible.  _(§163(h)(3)(F))_
- **Gifts to charity — Lines 11-14** — Line 11: Cash contributions (limit: 60% of AGI for public charities under §170(b)(1)(G); 30% for non-cash to public; 20% for capital gain property to private foundations). Line 12: Other than cash (Form 8283 required if > $500; qualified appraisal if > $5,000). Line 13: Carryover from prior year (5-year carryforward under §170(d)). Line 14: Total. NEW 0.5% AGI floor (OBBBA §70425; IRC §170(b)(1)(I)): compute the floor first. Individual charitable contributions are deductible only to the extent the aggregate exceeds 0.5% of the taxpayer's contribution base (generally AGI). Example: with $100,000 AGI, subtract $500; only contributions above $500 are deductible on Schedule A.  _(§170(b)(1)(G); OBBBA §70203; §170(d))_
- **AUDIT FLASH POINT — Charitable contributions outsized vs AGI** — A red flag is non-cash contributions over $5,000 without a qualified appraisal attached (Form 8283 Section B). The IRS DIF score weights charitable deductions relative to AGI heavily. For non-cash gifts of vehicles, refer to Pub 4303 and the contemporaneous written acknowledgment requirement under §170(f)(8). Conservation easements (§170(h)) and syndicated conservation easements are an enforcement priority — refer to a tax controversy specialist if encountered.  _(§170(f)(8); §170(h))_
- **Casualty and theft losses — Line 15** — deductible only if the loss is attributable to a federally declared disaster or, per the OBBBA §70109 expansion, certain state-declared disasters (§165(h)(5) post-TCJA, made permanent and expanded by OBBBA §70109). Subject to $100 floor per event and 10% AGI floor. Form 4684.  _(§165(h)(5); OBBBA §70112)_
- **Other itemized — Line 16** — gambling losses up to gambling winnings (§165(d)), federal estate tax on income in respect of a decedent (§691(c)), impairment-related work expenses, deduction for unrecovered investment in pension at death, amortizable bond premium on pre-10/23/86 taxable bonds.  _(§165(d); §691(c))_
- **Misc itemized deductions 2% floor suspension** — Misc itemized deductions subject to 2% AGI floor are SUSPENDED through 2025 by TCJA §11045, made permanent by OBBBA §70110. Exception: OBBBA §70110(b) adds IRC §67(b)(13), so unreimbursed educator expenses are no longer miscellaneous itemized deductions and remain deductible. This means unreimbursed employee business expenses, tax preparation fees, investment advisory fees, safe deposit box fees, and home office for an employee are not deductible. Reservists, performing artists, and fee-basis officials may still deduct via Schedule 1 Line 12.  _(TCJA §11045; OBBBA §70113)_

### 6.3 Pease limitation

- **Pease limitation suspension** — Pease (§68 overall limitation on itemized deductions) was suspended by TCJA; the permanent modification of §68 is codified in OBBBA §70111. No Pease limitation for 2025.  _(§68; OBBBA §70114)_

## 7. Line 12-15 — Standard/itemized deduction, QBI, taxable income

- **Line 12** — Greater of standard deduction (Line 2.1) or Schedule A Line 17.  _(Form 1040)_
- **Line 13 — §199A QBI deduction** — For pure W-2 / investment taxpayers without a trade or business: Line 13 = 0. If the taxpayer has REIT dividends (1099-DIV Box 5) or PTP income (Schedule K-1) without an active trade or business, QBI may still apply — refer to `us-qbi-deduction`.  _(§199A)_
- **Line 14** — Sum Line 12 + Line 13.  _(Form 1040)_
- **Line 15 — Taxable income** — Taxable income = Line 11 (AGI) - Line 14. If negative, enter 0.  _(Form 1040)_

## 8. Line 16 — Tax computation

- **Tax computation paths** — 1. Tax Tables (income < $100,000, no LTCG/qualified div): IRS-published. 2. Tax Computation Worksheet (income ≥ $100,000, no LTCG/qualified div): formulaic per bracket. 3. Qualified Dividends and Capital Gain Tax Worksheet (LTCG / QDIV present, no Schedule D Worksheet items): segregates LTCG/QDIV taxed at preferential rates (§2.3) from ordinary income taxed at §1(j) rates. 4. Schedule D Tax Worksheet (Schedule D Line 18 or 19 has §1250 unrecaptured or 28% collectibles): more granular bracketing for 25% and 28% rate gains. 5. Form 8615 (kiddie tax): child's unearned income > $2,700 taxed at parents' rate. 6. Schedule J (farm income averaging) — niche.
- **AUDIT FLASH POINT — Wrong tax computation worksheet used** — When a taxpayer has both ordinary income and LTCG, using the Tax Table on the total taxable income overpays tax. The Qualified Dividends and Capital Gain Tax Worksheet is mandatory in that case. Verify the worksheet in the work file.

## 9. Alternative Minimum Tax — Form 6251

### 9.1 When AMT bites in 2025

- **Why AMT applies to fewer taxpayers** — Post-TCJA / OBBBA, AMT applies to far fewer taxpayers because: The exemption is large ($88,100 single / $137,000 MFJ — §2.4); The phaseout starts at very high income ($626k / $1.25M); The SALT cap pushed many former AMT victims onto the regular tax instead
- **Most common 2025 AMT triggers** — 1. ISO exercise with bargain element (FMV - strike price at exercise) > AMT exemption — bargain element is an AMT preference under §56(b)(3). 2. Large private activity bond interest (§57(a)(5)) — flag tax-exempt interest from PABs on 1099-INT/1099-DIV. 3. Depreciation differences — §168(k) bonus and MACRS depreciation can create AMT adjustments. Less of an issue for non-business returns. 4. Net operating loss without ATNOL recalculation. 5. Large LTCG at very high income — LTCG keeps its 0/15/20% rate inside AMT but pushes ordinary AMTI through the phaseout zone, effectively creating a 32.5% / 35% AMT rate on ordinary income at the margin.  _(§56(b)(3); §57(a)(5); §168(k))_

### 9.2 AMT computation flow

- **AMT computation steps** — 1. Start with regular taxable income (Line 15). 2. Add back the standard deduction (if claimed). 3. Add AMT adjustments and preferences (Form 6251 Lines 2a-2t). 4. Subtract the AMT exemption (with phaseout if AMTI > threshold). 5. Apply 26%/28% AMT rates. 6. Subtract AMT foreign tax credit. 7. Compare to regular tax. If AMT > regular tax, the excess goes on Schedule 2 Line 1.

### 9.3 AMT credit — Form 8801

- **AMT minimum tax credit** — AMT paid in a prior year due to timing items (e.g. ISO bargain element later realized when stock is sold) generates a minimum tax credit usable in later years to the extent regular tax exceeds tentative AMT. Track on Form 8801.

## 10. Capital gains and Schedule D

### 10.1 Schedule D flow

- **Schedule D parts** — Part I — short-term (held ≤ 1 year): from Form 8949 Parts A (1099-B with basis reported), B (basis not reported), C (no 1099-B). Part II — long-term (held > 1 year): Form 8949 Parts D, E, F. Part III — summary: net short-term + net long-term, carryovers, capital loss limitation.

### 10.2 Capital loss limitation — §1211(b)

- **Capital loss deduction limit** — Net capital loss deductible against ordinary income capped at $3,000 ($1,500 MFS). Excess carries forward indefinitely retaining character (short / long).  _(§1211(b))_

### 10.3 Wash sale — §1091

- **Wash sale rule** — Loss is disallowed if substantially identical stock or securities are purchased within 30 days before or after the sale date. The disallowed loss is added to the basis of the replacement shares and the holding period tacks. Reported in Form 8949 Column (g) with code W. Crypto is NOT currently subject to wash sale rules — proposed legislation pending, but for 2025 §1091 does not apply to digital assets that are not securities.  _(§1091)_

### 10.4 Holding period

- **Holding period rule** — Acquired-date day excluded; sale-date day counted. To get long-term, sale must be on or after the date one year + one day after acquisition.

### 10.5 §1202 QSBS

- **QSBS exclusion** — For stock acquired on or before July 4, 2025: up to 100% gain exclusion (post-9/27/2010 acquisitions held > 5 years) on a $10M / 10× basis cap. OBBBA §70431 (IRC §1202(a)) enhanced §1202 for stock acquired after July 4, 2025: phased exclusion of 50% for stock held at least 3 years, 75% for 4 years, and 100% for 5 years; per-issuer gain exclusion limit raised to $15 million; aggregate gross asset test threshold raised to $75 million. Disqualified for FIRE (Finance Insurance Real Estate, etc.) businesses.  _(§1202)_

### 10.6 §121 home sale exclusion

- **Home sale exclusion amount** — Up to $250,000 ($500,000 MFJ) gain excluded if owned and used as principal residence for 2 of last 5 years. Reported only if gain exceeds exclusion or 1099-S was received.  _(§121)_

## 11. Net Investment Income Tax — Form 8960

Computed on **Form 8960**, flows to **Schedule 2 Line 12**.

- **Net investment income (NII) includes** — Interest (less §163(d) investment interest expense); Dividends; Capital gains (net); Royalties (if not in trade or business); Rental income (if not in real estate professional safe harbor under §469(c)(7)); Annuity income (non-qualified); Passive activity income (§469)  _(§469(c)(7); §163(d); §469)_
- **Excluded from NII** — Wages; Active business income; Distributions from qualified plans / IRAs; Self-employment income (already subject to SE tax); Tax-exempt interest  _(Form 8960)_
- **NIIT tax computation** — Tax = 3.8% × MIN(NII, MAGI - threshold)  _(Form 8960)_
- **MAGI adjustment for NIIT** — For MAGI: add back foreign earned income exclusion. Otherwise MAGI ≈ AGI for most domestic taxpayers.  _(Form 8960)_

## 12. Schedule 3 — Credits and payments

### 12.1 Part I — Nonrefundable credits

**Part I — Nonrefundable credits**  _(Schedule 3 Part I)_

| Line | Credit | Form | Refer-out |
| --- | --- | --- | --- |
| 1 | Foreign tax credit | Form 1116 (or de minimis under $300/$600) | `us-foreign-tax-credit-1116` |
| 2 | Credit for child & dependent care | Form 2441 | — |
| 3 | Education credits | Form 8863 (AOTC, LLC) | `us-education-credits-8863` |
| 4 | Retirement savings contributions credit (Saver's Credit) | Form 8880 | — |
| 5a | Residential clean energy credit (§25D) | Form 5695 — **OBBBA termination flag, see §2.9** | — |
| 5b | Energy efficient home improvement credit (§25C) | Form 5695 — **OBBBA accelerated termination flag** | — |
| 6 | Other nonrefundable credits | various | — |
| 6a | General business credit | Form 3800 | — |
| 6b | Adoption credit | Form 8839 ($17,280 in 2025, Rev. Proc. 2024-40) | — |
| 6c | DC first-time homebuyer (legacy) | — | — |
| 6d | Mortgage interest credit | Form 8396 | — |
| 6e | Plug-in electric vehicle credit (§30D personal use) | Form 8936 — **OBBBA termination 9/30/2025, see §2.9** | — |
| 6f | Mortgage interest credit (prior year carryforward) | — | — |
| 6g | Alt fuel vehicle refueling property credit (§30C personal) | Form 8911 | — |
| 6l | Credit for elderly or disabled | Schedule R | — |
| 6m | Credit for child tax (nonrefundable portion) | Schedule 8812 | — |
| 7 | Total nonrefundable | sum | — |

### 12.2 Part II — Refundable credits and other payments

**Part II — Refundable credits and other payments**  _(Schedule 3 Part II)_

| Line | Item |
| --- | --- |
| 9 | Net premium tax credit (Form 8962 — ACA marketplace) |
| 10 | Amount paid with extension request (Form 4868) |
| 11 | Excess Social Security tax withheld |
| 12 | Credit for federal tax on fuels (Form 4136) |
| 13 | Refundable credits not elsewhere |
| 13a | Form 2439 (regulated investment company undistributed LTCG) |
| 13b | Credit for repayment of amounts under claim of right >$3,000 (§1341) |
| 13c | Net §965 transition tax (rare for individuals) |
| 13d | Credit for previously taxed income under §962 |
| 13z | Other refundable |
| 14 | Total → 1040 Line 31 |

### 12.3 Credits cheat sheet

**Credits cheat sheet**  _(Schedule 3 cheat sheet)_

| Credit | Refundable? | Cap 2025 | Phaseout begins (MFJ) |
| --- | --- | --- | --- |
| Child Tax Credit (CTC) | Partially ($1,700 ACTC) | $2,000/child <17 | $400,000 |
| Credit for Other Dependents (ODC) | No | $500/dependent | $400,000 |
| Earned Income Credit (EITC) | Yes | $649 – $8,046 by # kids | varies by household |
| Child & Dependent Care | No | $3,000 / $6,000 expenses × 20-35% | $43,000 (rate drops to 20%) |
| AOTC | 40% refundable | $2,500 (100% first $2k + 25% next $2k) | $160k MFJ ($80k other) |
| LLC | No | $2,000 (20% of $10k) | $160k MFJ ($80k other) |
| Saver's Credit | No | $1,000 ($2,000 MFJ) | $79,000 MFJ |
| Adoption Credit | No (refundable portion under OBBBA §70302 if §36C(a)(2) election) | $17,280 | $259,190 |
| Residential Clean Energy (§25D) | No | 30% of qualified spend | none — but OBBBA terminated for property placed in service after 12/31/2025; flag |
| EV Credit (§30D) | No (transferable at point of sale) | $7,500 new / $4,000 used | $300k MFJ income / $80k MSRP — OBBBA terminated 9/30/2025 |

## 13. Schedule 2 — Additional taxes

**Schedule 2 — Additional taxes**  _(Schedule 2)_

| Line | Item | Form |
| --- | --- | --- |
| 1 | AMT | Form 6251 |
| 2 | Excess advance premium tax credit repayment | Form 8962 |
| 4 | SE tax | Schedule SE — refer out |
| 7 | Unreported SS/Medicare from Form 4137 / 8919 |  |
| 8 | Additional tax on IRAs (early withdrawal, RMD failure) | Form 5329 |
| 9 | Household employment taxes | Schedule H |
| 10 | First-time homebuyer credit repayment (legacy) | Form 5405 |
| 11 | Additional Medicare Tax | Form 8959 |
| 12 | Net Investment Income Tax | Form 8960 |
| 13 | §72(m)(5) excess benefits / §72(q) §72(t) |  |
| 14 | Interest on §453(l) deferred installment sale tax |  |
| 15 | Interest on §453A deferred tax on installment sales > $5M |  |
| 16 | §72(m)(5) recapture |  |
| 17a-17z | Other additional taxes |  |
| 18-21 | Various |  |

## 14. Payments — Form 1040 Lines 25-33

**Payments — Form 1040 Lines 25-33**  _(Form 1040 Lines 25-33)_

| Line | Item |
| --- | --- |
| 25a | Federal income tax withheld from W-2 |
| 25b | Federal income tax withheld from 1099 |
| 25c | Other withholding (Form 8959, Form W-2G, Schedule K-1) |
| 26 | 2025 estimated tax payments + prior year overpayment applied |
| 27 | EITC |
| 28 | Refundable Child Tax Credit / Additional CTC (Schedule 8812) |
| 29 | American Opportunity Credit refundable portion (Form 8863 Line 8) |
| 31 | Schedule 3 Line 15 (refundable credits) |
| 32 | Sum 27-31 |
| 33 | Total payments = 25d + 26 + 32 |

## 15. Estimated tax — §6654

Although primarily a freelancer concern (refer to `us-quarterly-estimated-tax`), W-2 taxpayers with material non-wage income (RSU vesting, large dividends, IRA conversions to Roth, year-end capital gains) may owe estimates.

- **Safe harbors** — 90% of current year tax, OR 100% of prior year tax (110% if prior-year AGI > $150,000 / $75,000 MFS)  _(§6654(d)(1))_
- **Underpayment penalty computation** — Underpayment penalty computed on Form 2210. The "annualized income installment method" can reduce penalty when income is lumpy.  _(Form 2210)_
- **De minimis exception** — $1,000 USD (no penalty if tax owed after withholding and refundable credits is < $1,000)  _(§6654)_

## 16. Amended returns — Form 1040-X

### 16.1 Statute of limitations — §6511(a)

- **Claim for refund statute of limitations** — Later of 3 years from date original return filed OR 2 years from date tax paid.  _(§6511(a))_

### 16.2 When to amend

- **Reasons to amend** — Discovered omitted income, deductions, or credits; Received corrected Form W-2c, 1099-Corrected, or amended K-1; Carryback claim (NOL, capital loss, foreign tax credit); Change in filing status (MFS to MFJ is allowed any time within 3 years; MFJ to MFS only by original due date)  _(Form 1040-X)_

### 16.3 E-file

- **1040-X e-file availability** — Form 1040-X has been e-filable since tax year 2019. Use the same software for the amended return.  _(Form 1040-X)_

## 17. Other operational items

### 17.1 IP PIN (Identity Protection PIN)

- **IP PIN** — Six-digit number issued by IRS to confirmed identity theft victims or any taxpayer who opts in via IRS.gov/IPPIN. Required to e-file; entered on the signature block. Rotates annually.  _(IRS.gov/IPPIN)_

### 17.2 Direct deposit

- **Direct deposit accounts** — Up to three accounts (Form 8888). Routing and account number errors are a leading cause of refund delays — verify.  _(Form 8888)_

### 17.3 Filing deadline

- **Filing deadline and extension** — April 15, 2026 for tax year 2025 returns. Extension Form 4868 grants automatic 6-month extension to October 15, 2026 — extension to file, not extension to pay. Underpayment of tax via extension still accrues interest and §6651 failure-to-pay penalty (0.5%/month).  _(Form 4868; §6651)_

### 17.4 E-file mandate

- **E-file mandate for paid preparers** — Most paid preparers must e-file under §6011(e) and Regs §301.6011-7 (10-return rule effective 2024, aggregating across return types). Paper allowed only with a §6011(e) hardship waiver or specific exception (Form 8948).  _(§6011(e); Regs §301.6011-7)_

### 17.5 §183 hobby loss

- **AUDIT FLASH POINT — Hobby vs business** — A taxpayer with a W-2 day job who reports a "side gig" on Schedule C with consistent losses is a §183 audit target. The 9-factor test in Treas. Reg. §1.183-2(b) determines whether the activity is for profit. If hobby, income reports on Schedule 1 Line 8j and expenses are NOT deductible (post-TCJA the 2% misc itemized deduction was suspended). If the taxpayer has hobby income, do not put it on Schedule C — put it on Line 8j and refuse business-expense treatment. Refer to a credentialed preparer if facts are mixed.  _(§183; Treas. Reg. §1.183-2(b))_

### 17.6 §469 passive activity losses

- **Rental real estate passive loss allowance** — Rental real estate losses are generally passive. Up to $25,000 of rental loss may offset active income for taxpayers who actively participate (lower bar than material participation), phased out between $100,000 and $150,000 MAGI under §469(i)(3). Suspended losses carry forward to offset future passive income or are released on full disposition.  _(§469(i)(3))_

### 17.7 §461(l) excess business loss

- **Excess business loss limitation 2025** — $313,000 ($626,000 MFJ) USD (excess business loss disallowed when business losses exceed business income by more than these thresholds, indexed per Rev. Proc. 2024-40; disallowed amount becomes part of NOL carryforward to next year; OBBBA §70205 made §461(l) permanent)  _(§461(l); Rev. Proc. 2024-40; OBBBA §70205)_

## 18. Common errors checklist

1. **SS taxable amount (Line 6b)** computed wrong — failed to use Pub 915 Worksheet 1; over- or understated tax-exempt interest in the formula. (See §4.6 Audit Flash.)
2. **Wrong tax computation method** — used Tax Tables when LTCG/qualified div present; should use Qualified Dividends and Capital Gain Tax Worksheet. (See §8 Audit Flash.)
3. **Forgot Schedule B** when interest + dividends > $1,500 — must answer Part III foreign account / FBAR questions.
4. **Excess Social Security tax** from two employers not credited on Schedule 3 Line 11.
5. **Capital loss carryover** not picked up from prior return (line 6 / Line 14 of Schedule D).
6. **Dependent claimed by both parents** post-divorce — Form 8332 release of claim or §152(e) custodial parent rule violated.
7. **Missing Form 8606** when rolled over after-tax 401(k) contributions to IRA, or made nondeductible IRA contributions — destroys basis tracking.
8. **NIIT** not computed when AGI > $200k/$250k and investment income present.
9. **Kiddie tax** Form 8615 missed for college student dependents with brokerage 1099-DIV.
10. **AMT** not run for ISO exercises.
11. **Standard deduction limitation** when claimed as a dependent — taxpayer used the regular $15k instead of the §63(c)(5) limit ($1,350 or earned income + $450, capped at $15k).
12. **Wrong filing status** — HoH claimed without a qualifying person; QSS claimed in year 3+ after spouse's death.
13. **Box 12 W-2 code DD** (employer-sponsored health coverage) mistakenly added to income — informational only.
14. **Form 1098-T scholarship amount** not added back when in excess of qualified tuition for AOTC.
15. **ACA Form 8962 reconciliation** missed when 1095-A received — required before refund processing; held in IRS error resolution if omitted.

## 19. Worked examples

### 19.1 Example A — Single W-2 employee with brokerage

Sarah, single, age 34, lives in Texas (no state income tax)
W-2 Box 1 wages: $95,000; Box 2 federal withholding: $12,400
1099-INT: $850 (Treasury bond fund)
1099-DIV: $3,200 ordinary, of which $2,800 qualified
1099-B sales: sold $40,000 of VTI held 18 months for $5,000 LTCG (basis $35,000); sold $8,000 of TSLA held 4 months for $1,200 STCG (basis $6,800)
401(k) contribution: $23,500 (already in W-2)
HSA contribution (outside payroll): $4,300
Roth IRA contribution: $7,000 (not deductible, no Form 8606)
Student loan interest paid: $1,800

**Return (Example A, Part 1)**

**Return (Example A, Part 1)**  _(Example A return table)_

| Line | Item | Amount |
| --- | --- | --- |
| 1a | Wages | $95,000 |
| 1z | Total | $95,000 |
| 2a | Tax-exempt interest | 0 |
| 2b | Taxable interest | $850 |
| 3a | Qualified dividends | $2,800 |
| 3b | Ordinary dividends | $3,200 |
| 7 | Capital gains (Schedule D: $5,000 LT + $1,200 ST = $6,200) | $6,200 |
| 9 | Total income | $105,250 |
| 10 | Adjustments (Sch 1 Line 13 HSA $4,300 + Line 21 SLI $1,800) | $6,100 |
| 11 | AGI | $99,150 |
| 12 | Standard deduction | $15,750 |
| 13 | QBI | 0 |
| 14 | Sum | $15,750 |
| 15 | Taxable income | $83,400 |

- **Tax computation (Qualified Dividends and Capital Gain Tax Worksheet)** — Ordinary taxable income portion: $83,400 - $5,000 LTCG - $2,800 QDIV = $75,600; STCG of $1,200 is in ordinary portion; Tax on $75,600 (single, §1(j)): 10% × $11,925 = $1,192.50; 12% × ($48,475 - $11,925) = $4,386.00; 22% × ($75,600 - $48,475) = $5,967.50; Total = $11,546; Tax on $5,000 + $2,800 = $7,800 LTCG/QDIV at 15% (since ordinary income > $48,350 threshold): $1,170; Line 16 tax: ~$12,716  _(§1(j))_

**Return (Example A, Part 2)**  _(Example A return table part 2)_

| Line | Item | Amount |
| --- | --- | --- |
| 16 | Tax | $12,716 |
| 22 | Total tax before other | $12,716 |
| 23 | Other taxes (Schedule 2) | 0 |
| 24 | Total tax | $12,716 |
| 25a | Withholding W-2 | $12,400 |
| 33 | Total payments | $12,400 |
| 37 | Amount owed | **$316** |

- **NIIT check Example A** — AGI $99,150 < $200k threshold — no NIIT  _(§1411)_

### 19.2 Example B — MFJ with kids, mortgage, HSA, large itemized

Marcus and Priya, MFJ, both age 41, California residents (refer to `ca-540-individual-return` for CA portion — this skill covers federal only)
Marcus W-2 wages: $185,000; withholding $32,000
Priya W-2 wages: $95,000; withholding $11,000
Combined Social Security wages exceed $176,100 only on Marcus alone (so no excess SS tax issue)
Two qualifying children: ages 8 and 11
Family HSA contribution: $8,550 (Priya's W-2 Box 12 W = $8,550 already pre-tax — so no Schedule 1 deduction)
Mortgage interest (1098): $24,000 on $620,000 acquisition debt originated 2020
Property tax: $14,000
CA state income tax withheld: $19,800
Charitable cash gifts to public charities: $9,500 (with substantiation)
401(k) contributions: Marcus $23,500, Priya $20,000 (already in W-2)
1099-DIV: $4,800 ordinary, $4,200 qualified
1099-INT: $1,400

**Return (Example B, Part 1)**  _(Example B return table part 1)_

| Line | Item | Amount |
| --- | --- | --- |
| 1a + 1z | Wages | $280,000 |
| 2b | Interest | $1,400 |
| 3a / 3b | Qualified $4,200 / Ordinary $4,800 | 3b: $4,800 |
| 9 | Total income | $286,200 |
| 10 | Adjustments | 0 (HSA via cafeteria plan; no other) |
| 11 | AGI | $286,200 |

**Schedule A — Itemized**  _(§2.7; OBBBA §70401)_

| Line | Item | Amount |
| --- | --- | --- |
| 5a | State income tax | $19,800 |
| 5b | Property tax | $14,000 |
| 5d | Sum | $33,800 |
| 5e | SALT cap | min($33,800, $40,000) = $33,800 — **NO phaseout** since MAGI $286,200 < $500k threshold (§2.7) |
| 7 | Total taxes | $33,800 |
| 8a / 8e | Mortgage interest | $24,000 |
| 10 | Total interest | $24,000 |
| 11 | Charitable cash (≤ 60% AGI limit) | $9,500 |
| 14 | Total charitable | $9,500 |
| 17 | Total itemized | **$67,300** |

- **Itemize vs standard decision** — Itemized ($67,300) > standard ($31,500) → itemize.  _(§63)_

**Return (Example B, Part 2)**  _(Example B return table part 2)_

| Line | Item | Amount |
| --- | --- | --- |
| 12 | Itemized | $67,300 |
| 13 | QBI | 0 |
| 15 | Taxable income | $286,200 - $67,300 = $218,900 |

- **Tax (Qualified Dividends and Capital Gain Worksheet)** — Ordinary portion: $218,900 - $4,200 QDIV = $214,700; Tax on $214,700 MFJ (§1(j) brackets): 10% × $23,850 = $2,385; 12% × ($96,950 - $23,850) = $8,772; 22% × ($206,700 - $96,950) = $24,145; 24% × ($214,700 - $206,700) = $1,920; Subtotal = $37,222; Tax on $4,200 QDIV at 15% (ordinary income > $96,700 0% bracket): $630; Line 16 tax: ~$37,852  _(§1(j))_
- **Credits — Schedule 8812** — 2 qualifying children × $2,200 = $4,400 CTC; AGI $286,200 < $400,000 phaseout — full credit; Line 19: $4,400  _(§24)_
- **NIIT check** — MAGI $286,200 vs $250,000 threshold → excess $36,200; NII = $1,400 + $4,800 = $6,200; NIIT = 3.8% × min($6,200, $36,200) = 3.8% × $6,200 = $236; Schedule 2 Line 12: $236  _(§1411)_
- **Additional Medicare Tax check** — Combined wages $280,000 vs $250,000 MFJ threshold → excess $30,000; 0.9% × $30,000 = $270; Marcus's wages alone ($185k) under $200k single threshold so employer didn't withhold the 0.9% on his wages — full $270 owed; Schedule 2 Line 11: $270  _(Form 8959)_

**Return (Example B, Part 3)**  _(Example B return table part 3)_

| Line | Item | Amount |
| --- | --- | --- |
| 16 | Tax | $37,852 |
| 19 | CTC | $4,400 |
| 22 | Subtotal after nonrefundable | $33,452 |
| 23 | Schedule 2 (NIIT $236 + Add'l Medicare $270) | $506 |
| 24 | Total tax | $33,958 |
| 25a | Withholding | $43,000 |
| 33 | Total payments | $43,000 |
| 34 | Overpayment | **$9,042 refund** |

### 19.3 Example C — Retiree with Social Security + RMD

Walter, single, age 73, widower (spouse died 2019 — no longer QSS), lives in Florida
Social Security: $32,000 gross (SSA-1099)
Traditional IRA RMD: $28,000 (1099-R)
Pension (1099-R, fully taxable): $14,000
1099-INT (bank): $600
1099-DIV: $3,500 ordinary, $3,200 qualified
1099-B: sold mutual fund LTCG $9,000 (basis $21,000, proceeds $30,000)
QCD from IRA to local charity: $10,000 (part of the $28,000 RMD distribution — directly transferred by trustee)
Property tax: $4,800
Mortgage paid off — no mortgage interest
Charitable contributions other than QCD: $1,200 cash
Federal withholding: $4,200 from pension; $2,800 from IRA

- **SS taxable computation (Pub 915 Worksheet 1)** — Provisional income = (AGI excl SS) + tax-exempt interest + 50% SS; AGI excl SS = ($28,000 - $10,000 QCD) + $14,000 + $600 + $3,500 + $9,000 = $45,100; Note: QCD reduces 4b but Line 4a still shows $28,000; the $10,000 QCD is excluded from gross income; Provisional income = $45,100 + 0 + ($32,000 × 0.5) = $61,100; Single thresholds: $25k first / $34k second; Above second threshold, so up to 85% taxable; Computation: lesser of (a) 85% × $32,000 = $27,200 or (b) 85% × ($61,100 - $34,000) + lesser of [$4,500 or 50% × $32,000 = $16,000] = $23,035 + $4,500 = $27,535; Taxable SS = min($27,200, $27,535) = $27,200  _(Pub 915 Worksheet 1)_

**Return (Example C, Part 1)**  _(Example C return table part 1)_

| Line | Item | Amount |
| --- | --- | --- |
| 4a | IRA gross | $28,000 |
| 4b | IRA taxable (write "QCD $10,000" beside) | $18,000 |
| 5a | Pension gross | $14,000 |
| 5b | Pension taxable | $14,000 |
| 6a | SS gross | $32,000 |
| 6b | SS taxable | $27,200 |
| 2b | Interest | $600 |
| 3a / 3b | $3,200 / $3,500 | 3b: $3,500 |
| 7 | Capital gains (LTCG $9,000) | $9,000 |
| 9 | Total income | $72,300 |
| 10 | Adjustments | 0 |
| 11 | AGI | $72,300 |

- **Standard deduction (single, age 65+)** — Base $15,750 + age 65+ addition $2,000 = $17,750  _(Rev. Proc. 2024-40)_
- **Itemize vs standard decision Example C** — Compare itemized: property tax $4,800 + charitable $1,200 = $6,000 — well below standard. Use standard.  _(§63)_

**Return (Example C, Part 2)**  _(Example C return table part 2)_

| Line | Item | Amount |
| --- | --- | --- |
| 12 | Standard | $17,750 |
| 15 | Taxable income | $54,550 |

- **Tax (Qualified Dividends and Capital Gain Worksheet)** — Ordinary portion: $54,550 - $9,000 LTCG - $3,200 QDIV = $42,350; Tax on $42,350 single: 10% × $11,925 = $1,192.50; 12% × ($42,350 - $11,925) = $3,651; Total = $4,844; Tax on $9,000 + $3,200 = $12,200 LTCG/QDIV: $42,350 ordinary + $12,200 = $54,550 total; $48,350 - $42,350 = $6,000 at 0%; $12,200 - $6,000 = $6,200 at 15% = $930; Line 16 tax: ~$5,774  _(§1(h))_

**Return (Example C, Part 3)**  _(Example C return table part 3)_

| Line | Item | Amount |
| --- | --- | --- |
| 16 | Tax | $5,774 |
| 24 | Total tax | $5,774 |
| 25b | 1099 withholding | $7,000 |
| 33 | Total payments | $7,000 |
| 34 | Overpayment | **$1,226 refund** |

- **NIIT and RMD checks Example C** — NIIT check: AGI $72,300 < $200k — none. RMD check: Walter is 73, RMD age (73 under SECURE 2.0 §107 for those born 1951-1959) — confirm full RMD was satisfied. The $10,000 QCD counts toward RMD (§408(d)(8)(B)).  _(SECURE 2.0 §107; §408(d)(8)(B))_

### 19.4 Example D — Single W-2 employee, ISO exercise-and-hold (AMT)

Dana, single, age 38, lives in Georgia
W-2 Box 1 wages: $185,000 (already includes a $40,000 RSU vest reported in Box 14 — do NOT add the $40,000 again)
1099-INT: $244
1099-B sales: sold RSU lots for +$43,000 long-term and +$3,600 short-term capital gain
ISO exercise-and-hold: exercised 4,000 incentive stock options (strike $3, FMV $28) and held them past year-end (did not sell)

**Return (Example D, Part 1 — regular tax)**  _(Example D regular-tax return)_

| Line | Item | Amount |
| --- | --- | --- |
| 1a | Wages (Box 1 as-is — $40,000 RSU already included; do not re-add) | $185,000 |
| 2b | Taxable interest | $244 |
| 7 | Capital gain (Schedule D: $43,000 LT + $3,600 ST) | $46,600 |
| 9 | Total income | $231,844 |
| 11 | AGI | $231,844 |
| 12 | Standard deduction (single) | $15,750 |
| 15 | Taxable income | $216,094 |
| 16 | Regular tax (QDCGT worksheet) | $40,840 |

- **Regular tax computation — Example D** — Ordinary income $173,094 (taxable income $216,094 − $43,000 net long-term capital gain) at 2025 single rates = $34,390; plus $43,000 LTCG × 15% = $6,450 → regular tax $40,840. The ISO exercise-and-hold adds ZERO regular-tax income: the $100,000 bargain element is invisible to the regular system and surfaces only in AMT (common error #10).  _(§1(j); §1(h))_

**Form 6251 (Example D — AMT)**  _(Example D Form 6251 AMT)_

| Line | Item | Amount |
| --- | --- | --- |
| 1 | Taxable income (Form 1040 line 15) | $216,094 |
| 2a | Standard deduction add-back | $15,750 |
| 2m | ISO exercise adjustment — 4,000 × ($28 − $3), §56(b)(3) | $100,000 |
| 4 | AMTI | $331,844 |
| 5 | AMT exemption (single $88,100; AMTI below $626,350 phaseout → full) | ($88,100) |
| 6 | Base | $243,744 |
| 7 | Tentative minimum tax ($200,744 × 26% + $43,000 LTCG × 15%) | $58,643 |
| 9 | Regular tax | $40,840 |
| 10 | AMT — to Schedule 2, line 1 | $17,803 |

- **AMT result and minimum tax credit — Example D** — Without the ISO seam AMT would be $0; the $100,000 preference produces ~$17,803 of real AMT. That AMT also generates a ~$17,803 minimum tax credit (Form 8801), recoverable when the shares are sold — a timing item, not a permanent cost.  _(§55; §53)_
- **NIIT and Additional Medicare checks — Example D** — NIIT (§1411): AGI $231,844 > $200,000 → 3.8% × lesser of net investment income ($46,844) and MAGI over threshold ($31,844) = ~$1,210 — separate from AMT. Additional Medicare Tax (§3101(b)(2)): Medicare wages $197,000 < $200,000 → none.  _(§1411; §3101(b)(2))_

## 20. Provenance and citations

### 20.1 Primary authority

**Internal Revenue Code** (Title 26 USC): §§1, 1(g), 1(h), 1(j), 2, 24, 25A, 25D, 30D, 32, 55, 56, 57, 63, 68, 86, 121, 151, 152, 162, 163, 164, 165, 170, 172, 183, 199A, 213, 408, 411, 469, 691, 877A, 1091, 1202, 1211, 1250, 1402, 1411
**OBBBA (One Big Beautiful Bill Act, P.L. 119-21)**: §70101 (rate permanence), §70110 (mortgage cap permanence), §70112 (casualty loss), §70113 (misc itemized suspension permanent), §70114 (Pease permanent), §70201 (QBI 23% in 2026), §70203 (60% charity limit permanent), §70205 (§461(l) permanent), §70301 (CTC permanence), §70302 (adoption credit), §70401 ($40k SALT cap 2025-2029), §70405 (§108 QPRI extension), §70501 (§25D termination), §70502 (§30D / §25E termination), §70601 (tip deduction), §70602 (overtime deduction), §70603 (auto loan interest)
**TCJA (Tax Cuts and Jobs Act, P.L. 115-97)**: §11045 (misc itemized suspension), §11049 (moving expense), §11051 (alimony)
**SECURE 2.0 Act (Division T of Consolidated Appropriations Act, 2023)**: §107 (RMD age), §302 (RMD penalty reduction)
**Inflation Reduction Act (P.L. 117-169)**: §13301 (§25C/§25D pre-OBBBA), §13401 (§30D pre-OBBBA)
**ACA (P.L. 111-148)**: §1411 NIIT enactment
**Rev. Proc. 2024-40**: 2025 inflation adjustments (standard deduction, brackets, AMT exemption, capital gains brackets, dependent gross income test, adoption credit, etc.)
**Treas. Reg. §1.183-2**: nine-factor hobby vs business test
**Pub 915**: Social Security and Equivalent Railroad Retirement Benefits
**Pub 17**: Your Federal Income Tax
**Pub 575**: Pension and Annuity Income
**Pub 939**: General Rule for Pensions and Annuities
**Pub 4303**: Donor's Guide to Vehicle Donation

### 20.2 Verification status

Tax year: **2025**
Effective law as of: **2026-05-27** (knowledge cutoff). OBBBA enacted 2025-07-04 P.L. 119-21.
Verified against: Rev. Proc. 2024-40, JCT explanation of OBBBA (JCS-1-25), IRS draft Form 1040 and instructions for tax year 2025
`verified_by`: pending — requires Circular 230 practitioner sign-off before output reaches taxpayer

### 20.3 Circular 230 §10.37 disclosure

This skill produces **written advice** within the meaning of Treas. Dept. Circular 230 §10.37(a). The skill:

- Bases its conclusions on the facts the taxpayer represents in the intake; the practitioner must independently verify those facts.
- Reasonably considers relevant legal authorities including the Code, regulations, IRS published guidance, and the OBBBA legislative text.
- Does not take into account the possibility that a return will not be audited.
- Does not contain a reliance opinion for §6662 substantial-understatement penalty purposes unless explicitly marked.
- Is intended as a working draft for a credentialed reviewer (EA, CPA, or attorney). The reviewer is responsible for signing the return as paid preparer under §6695 and for compliance with §6694 preparer accuracy standards.

The output of this skill is not a "covered opinion" under former Circular 230 §10.35 (rescinded 2014) but the practitioner remains subject to §10.37 written-advice standards.

### 20.4 Self-checks before submission

The reviewer must confirm:

1. Filing status matches the 12/31/2025 marital and household facts.
2. Each dependent satisfies §152(c) or §152(d); Form 8332 is on file if applicable.
3. SS taxable amount uses Pub 915 Worksheet 1.
4. Tax computation uses Qualified Dividends and Capital Gain Tax Worksheet when LTCG/QDIV present.
5. NIIT (Form 8960) computed when AGI > §1411 threshold.
6. Additional Medicare Tax (Form 8959) reconciled to W-2 Box 6 + 1099 withholding.
7. AMT (Form 6251) at least run mentally for ISO exercises, large PAB interest, or high LTCG with ordinary AMTI in phaseout.
8. Schedule B questions Part III answered correctly (foreign account, foreign trust).
9. SALT phaseout (OBBBA §70401(b)) applied if MAGI > $500k.
10. §25D / §30D OBBBA termination dates verified for any 2025 credit claim.
11. Kiddie tax Form 8615 for dependents with unearned income > $2,700.
12. RMD satisfied for taxpayers age 73+ (§401(a)(9), §4974); 25% / 10% penalty on Form 5329 if not.
13. 1095-A reconciliation on Form 8962 if marketplace coverage.
14. Direct deposit routing/account verified character by character.
15. Preparer signature, PTIN, firm EIN, and §6695 due diligence checklist (Form 8867 for EITC, CTC, AOTC, HoH) complete.

## End of skill note

*End of skill. Load alongside `us-tax-workflow-base`. Refer downstream to state assembly skills as applicable.*

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
