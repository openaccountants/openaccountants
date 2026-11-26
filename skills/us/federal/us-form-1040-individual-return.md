---
name: us-form-1040-individual-return
description: "US federal Form 1040 for employees, retirees, investors and families: 2026 planning figures and enacted changes, plus a separately dated 2025 return walkthrough with four worked cases. Federal only; distinguish tax year from filing year."
version: 1.2
jurisdiction: US
tax_year: 2026
tax_year_notes: "2026 planning figures and enacted changes in section 0; sections 2–19 are the separately dated calendar-2025 return walkthrough and original 2025 cases. Never apply 2025 tables or form fields to a 2026 return. Final 2026 form mappings are not supplied."
last_updated: 2026-11-26
source_checked: 2026-11-26
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
reviewed_by: "Christopher Aryee"
reviewed_on: 2026-11-03
tier: 1
domain: income-tax
---

# US Form 1040 Individual Return

## US Form 1040 — Individual Income Tax Return (Non-Freelance)

Federal individual-return guide. **Use section 0 for calendar-2026 planning. Sections 2–19 and all four original cases use calendar-2025 income and final 2025 forms.** A year of filing is not a tax year. Do not use the 2025 walkthrough to prepare a 2026 return. Load alongside `us-tax-workflow-base`; federal only. Professional review before delivery is our workflow policy, not a new approval of this revision.

## 0. Calendar-2026 planning — keep separate from the 2025 return

These figures apply to **2026 income**, generally reported in the following year. The final 2025 form labels and Tax Table cells later in this guide are not 2026 filing instructions. Establish tax year, filing status, dependent/age/blindness facts, income type, coverage and payment dates first. Use the actual year’s final forms and published Tax Table when filing; a continuous bracket calculation is not a substitute where a Tax Table is required.

### 2026 deductions and ordinary brackets

Amounts below are USD. Standard deductions assume eligibility; dependent limits and age/blindness additions are separate. [Rev. Proc.2025-32 §4.14](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf).

| 2026 filing status | Basic standard deduction | Official source |
| --- | --- | --- |
| Single / MFS | $16,100 | [§4.14](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| MFJ / QSS | $32,200 | [§4.14](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| HoH | $24,150 | [§4.14](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Age 65/blind addition per qualifying condition | $1,650; $2,050 if unmarried and not QSS | [§4.14](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Dependent basic limit | Greater of $1,350 or earned income + $450, capped at the regular status deduction; age/blindness additions separately | [§4.14](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |

Each ordinary rate applies only to the slice above the previous upper boundary, starting at zero; the last rate applies above the sixth boundary. [Rev. Proc.2025-32 §4.01](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf).

| 2026 filing status | Upper boundaries for 10%, 12%, 22%, 24%, 32%, 35%; then 37% | Official source |
| --- | --- | --- |
| Single | $12,400; $50,400; $105,700; $201,775; $256,225; $640,600 | [Table 3](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| MFJ / QSS | $24,800; $100,800; $211,400; $403,550; $512,450; $768,700 | [Table 1](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| HoH | $17,700; $67,450; $105,700; $201,750; $256,200; $640,600 | [Table 2](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| MFS | $12,400; $50,400; $105,700; $201,775; $256,225; $384,350 | [Table 4](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |

### Other 2026 planning amounts and changed conditions

| Topic | 2026 rule and operative boundary | Official source |
| --- | --- | --- |
| Ordinary preferential capital gains / qualified dividends | 0% ceiling and 15% ceiling: Single $49,450 / $545,500; MFJ/QSS $98,900 / $613,700; HoH $66,200 / $579,600; MFS $49,450 / $306,850. 20% above the second boundary. Stack on ordinary taxable income; special 25%/28% categories remain separate. | [Rev. Proc.2025-32 §4.03](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| AMT | Exemptions Single/HoH $90,100; MFJ/QSS $140,200; MFS $70,100. Phaseout starts $500,000 / $1,000,000 / $500,000 respectively and reduces exemption by **50%** of excess AMTI. Zero points $680,200 / $1,280,400 / $640,200. Ordinary base after exemption: 26% to $244,500 ($122,250 MFS), then 28%; preferential gains require their separate computation and MFS has its additional adjustment. | [Rev. Proc.2025-32 §4.10](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf); [Act §70107](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| SALT | Applicable limitation $40,400; MAGI threshold $505,000. Apply the 30% reduction, $10,000 floor and MFS halving order in section 2.7. Example: Single MAGI $550,000 gives $26,900 limit, before comparing actual eligible taxes. | [Act §70120](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| Senior deduction | Up to $6,000 per eligible person age 65 by year end, separately from the standard deduction. Reduce each person’s $6,000 by 6% of MAGI above $75,000 ($150,000 joint), no lower than zero. Valid SSN and married-joint requirements apply; MAGI adds back sections 911/931/933 exclusions. Applies through 2028. | [Act §70103](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| Child tax credit | Maximum $2,200 per qualifying child; refundable maximum $1,700, subject to the underlying eligibility/SSN/earned-income/liability tests, not automatic entitlement. | [Rev. Proc.2025-32 §4.05](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf); [Act §70104](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| HSA full-year limits | $4,400 self-only / $8,750 family; eligible age-55 catch-up $1,000. Establish eligible coverage/months, Medicare/dependency restrictions, employer contributions and testing-period conditions. Do not assume a 2025 coverage classification settles new 2026 eligibility. | [Rev. Proc.2025-19](https://www.irs.gov/pub/irs-drop/rp-25-19.pdf); [Publication 969](https://www.irs.gov/publications/p969) |
| IRA contributions | Combined traditional/Roth limit $7,500, or $8,600 age 50+, capped by eligible compensation. Deductibility/contribution MAGI rules and coverage remain separate. Traditional active-participant phaseouts: Single/HoH $81,000–$91,000; MFJ/QSS $129,000–$149,000. MFJ noncovered contributor with covered spouse $242,000–$252,000. Roth Single/HoH $153,000–$168,000; MFJ/QSS $242,000–$252,000. Apply MFS living-apart/living-together rules separately. | [Publication 590-A, What’s New for 2026](https://www.irs.gov/publications/p590a); [Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf) |
| Student-loan interest | Maximum $2,500; phaseout Single/HoH/QSS $85,000–$100,000, joint $175,000–$205,000; no MFS. Qualified-loan, legal obligation, dependency and no-double-benefit tests remain. | [Rev. Proc.2025-32 §4.29](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf); [Form 1040 instructions, deduction conditions](https://www.irs.gov/instructions/i1040gi) |
| Qualifying-relative gross income | Less than $5,300; still apply relationship/household, support and general dependency gateways. | [Rev. Proc.2025-32 §4.23](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Care-credit percentage | 50%, reduced by 1 percentage point per $2,000 or fraction of AGI above $15,000, to a 35% floor; further reduced by 1 point per $2,000 ($4,000 joint) or fraction above $75,000 ($150,000 joint), to a 20% floor. This changes the 2025 percentage table; qualifying-person, employment, earned-income, expense-cap and benefit-coordination tests still apply. | [Act §70405](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| Gambling losses | Deduction is the lesser of 90% of wagering losses and wagering gains; the loss definition includes otherwise-allowable deductions incurred in carrying on wagering transactions. Do not reuse the full-loss 2025 rule. | [Act §70114](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| Itemized charity | The 0.5% contribution-base floor starts in 2026, before considering the other applicable percentage/order/carryover rules. At contribution base $100,000 the floor is $500; that alone does not determine the deductible amount. | [Act §70425](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| Top-bracket itemized limitation | After other deduction limits, reduce otherwise allowable itemized deductions by 2/37 of the lesser of those deductions or the positive excess of pre-section-68 taxable income plus those deductions over the start of the 37% bracket. It is not the former Pease rule. | [Act §70111](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| Educator expenses / mortgage insurance / casualty losses | From 2026, the Act adds qualifying educator expenses to the non-miscellaneous itemized category (with expanded sports/instructional scope), restores qualifying mortgage-insurance treatment and expands personal casualty rules to defined State-declared disasters. Detailed expense/contract/event eligibility and coordination: **Check this point with one of our partner accountants.** | [Act §§70108–70110](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| Vehicle / residential-energy credits | No new/used vehicle credit for a vehicle acquired after September 30, 2025; section 25D does not cover expenditures after December 31, 2025. Prior eligible credits/carryforwards and vehicle delivery dates require their own analysis; 2026 filing does not revive expired eligibility. | [Act §§70501–70502,70506](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |

For 2026 EITC, Saver’s Credit, adoption, QCD limits, excess-business-loss/NOL computations, qualified tips/overtime/vehicle-loan deductions and the nonitemizer charitable deduction, use the current-year official worksheet and all eligibility conditions; their **2025** cheat-sheet amounts below are not 2026 figures. Where a specialist entitlement or unusual interaction is unresolved: **Check this point with one of our partner accountants.** No 2026 filing deadline or form mapping is inferred from a 2025 form.

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
| §199A QBI deduction with positive QBI | `us-qbi-deduction` (this skill assumes line 13a is zero only after REIT/PTP screening) [2025 authority](https://www.irs.gov/instructions/i1040gi) |
| Quarterly estimated tax planning for 2026 | `us-quarterly-estimated-tax` [2025 authority](https://www.irs.gov/instructions/i1040gi) |
| Foreign tax credit (Form 1116) | `us-foreign-tax-credit-1116` [2025 authority](https://www.irs.gov/instructions/i1040gi) |
| Education credits (Form 8863) AOTC/LLC | `us-education-credits-8863` [2025 authority](https://www.irs.gov/instructions/i1040gi) |
| Foreign earned income exclusion (Form 2555) | `us-foreign-earned-income-2555` [2025 authority](https://www.irs.gov/instructions/i1040gi) |
| Estate / gift returns (Form 706 / 709) | `us-estate-gift-706-709` [2025 authority](https://www.irs.gov/instructions/i1040gi) |
| Partnership K-1 with material participation issues | `us-form-1065-partnership` [2025 authority](https://www.irs.gov/instructions/i1040gi) |
| S-corp election analysis | `us-s-corp-election-decision` |
| State returns | State-specific skill (e.g. `ca-540-individual-return`) [2025 authority](https://www.irs.gov/instructions/i1040gi) |

### 1.3 Refusal catalogue

- **Dual-status alien** — Taxpayer is a dual-status alien in the filing year (departing or arriving US resident)  _(1.3 Refusal catalogue)_
- **§877A expatriation issues** — Taxpayer has §877A expatriation issues (covered expatriate, mark-to-market)  _(1.3 Refusal catalogue)_
- **Non-resident alien filing 1040-NR** — Non-resident alien filing Form 1040-NR (different skill — not yet built)  _(1.3 Refusal catalogue)_
- **Innocent spouse relief** — Innocent spouse relief (Form 8857) is being claimed  _(1.3 Refusal catalogue)_
- **Foreign accounts, assets and trusts** — Screen regardless of the former $100,000 routing cutoff. A US person with a financial interest in or signature authority over foreign financial accounts exceeding $10,000 in aggregate at any time in the calendar year generally has an FBAR filing requirement; exceptions and Form 8938 have separate tests. For account exceptions, FATCA thresholds and international compliance: Check this point with one of our partner accountants. [FinCEN](https://www.fincen.gov/report-foreign-bank-and-financial-accounts).
- **Streamlined Filing Compliance / OVDP** — Streamlined Filing Compliance Procedures or OVDP for unreported foreign assets  _(1.3 Refusal catalogue)_
- **Active IRS examination/CP2000/appeals** — Active IRS examination, CP2000, or appeals — those require a tax controversy practitioner  _(1.3 Refusal catalogue)_
- **Trust/estate beneficiary K-1 with foreign/AMT preferences** — Taxpayer is a trust or estate beneficiary receiving Schedule K-1 with foreign or alternative minimum tax preferences flowing through  _(1.3 Refusal catalogue)_

## 2. Tax year 2025 figures — Rev. Proc. 2024-40 + OBBBA

### 2.1 Standard deduction (§63(c))

**Standard deduction table**  _(§63(c))_

| Filing status | 2025 amount |
| --- | --- |
| Single | **$15,750** [2025 authority](https://www.irs.gov/publications/p501) |
| Married filing jointly (MFJ) | **$31,500** [2025 authority](https://www.irs.gov/publications/p501) |
| Married filing separately (MFS) | $15,750 [2025 authority](https://www.irs.gov/publications/p501) |
| Head of household (HoH) | **$23,625** [2025 authority](https://www.irs.gov/publications/p501) |
| Qualifying surviving spouse (QSS) | $31,500 [2025 authority](https://www.irs.gov/publications/p501) |

- **Additional standard deduction (age 65+ or blind)** — MFJ / QSS: $1,600 per qualifying condition per spouse; Single / HoH: $2,000 per qualifying condition (2025). For 2026 the indexed amounts are $1,650 for married individuals and $2,050 for unmarried individuals; an MFJ couple where both spouses are 65 or older claims a 2026 standard deduction of $35,500 (OBBBA §70102; IRS Pub 501)  _(§63(c))_
- **Dependent standard deduction limitation** — A taxpayer who can be claimed as a dependent on another return is limited to the greater of (a) $1,350 or (b) earned income + $450, capped at the regular standard deduction.  _(§63(c))_

### 2.2 Ordinary income tax brackets — §1(j) (post-TCJA, OBBBA-permanent)

- **Permanence of §1(j) rates** — OBBBA P.L. 119-21 §70101 made the §1(j) rates permanent (eliminating the 12/31/2025 sunset). Brackets indexed under Rev. Proc. 2024-40.  _(OBBBA P.L. 119-21 §70101; Rev. Proc. 2024-40)_

**Single (2025) tax brackets**  _(§1(j))_

| Rate | Taxable income |
| --- | --- |
| 10% | $0 – $11,925 [2025 authority](https://www.irs.gov/pub/irs-drop/rp-24-40.pdf) |
| 12% | $11,925 – $48,475 [2025 authority](https://www.irs.gov/pub/irs-drop/rp-24-40.pdf) |
| 22% | $48,475 – $103,350 [2025 authority](https://www.irs.gov/pub/irs-drop/rp-24-40.pdf) |
| 24% | $103,350 – $197,300 [2025 authority](https://www.irs.gov/pub/irs-drop/rp-24-40.pdf) |
| 32% | $197,300 – $250,525 [2025 authority](https://www.irs.gov/pub/irs-drop/rp-24-40.pdf) |
| 35% | $250,525 – $626,350 [2025 authority](https://www.irs.gov/pub/irs-drop/rp-24-40.pdf) |
| 37% | over $626,350 [2025 authority](https://www.irs.gov/pub/irs-drop/rp-24-40.pdf) |

**MFJ (2025) tax brackets**  _(§1(j))_

| Rate | Taxable income |
| --- | --- |
| 10% | $0 – $23,850 [2025 authority](https://www.irs.gov/pub/irs-drop/rp-24-40.pdf) |
| 12% | $23,850 – $96,950 [2025 authority](https://www.irs.gov/pub/irs-drop/rp-24-40.pdf) |
| 22% | $96,950 – $206,700 [2025 authority](https://www.irs.gov/pub/irs-drop/rp-24-40.pdf) |
| 24% | $206,700 – $394,600 [2025 authority](https://www.irs.gov/pub/irs-drop/rp-24-40.pdf) |
| 32% | $394,600 – $501,050 [2025 authority](https://www.irs.gov/pub/irs-drop/rp-24-40.pdf) |
| 35% | $501,050 – $751,600 [2025 authority](https://www.irs.gov/pub/irs-drop/rp-24-40.pdf) |
| 37% | over $751,600 [2025 authority](https://www.irs.gov/pub/irs-drop/rp-24-40.pdf) |

**HoH (2025) tax brackets**  _(§1(j))_

| Rate | Taxable income |
| --- | --- |
| 10% | $0 – $17,000 [2025 authority](https://www.irs.gov/pub/irs-drop/rp-24-40.pdf) |
| 12% | $17,000 – $64,850 [2025 authority](https://www.irs.gov/pub/irs-drop/rp-24-40.pdf) |
| 22% | $64,850 – $103,350 [2025 authority](https://www.irs.gov/pub/irs-drop/rp-24-40.pdf) |
| 24% | $103,350 – $197,300 [2025 authority](https://www.irs.gov/pub/irs-drop/rp-24-40.pdf) |
| 32% | $197,300 – $250,500 [2025 authority](https://www.irs.gov/pub/irs-drop/rp-24-40.pdf) |
| 35% | $250,500 – $626,350 [2025 authority](https://www.irs.gov/pub/irs-drop/rp-24-40.pdf) |
| 37% | over $626,350 [2025 authority](https://www.irs.gov/pub/irs-drop/rp-24-40.pdf) |

### 2.3 Capital gains brackets — §1(h)

**Capital gains brackets**  _(§1(h))_

| Rate | Single | MFJ | HoH |
| --- | --- | --- | --- |
| 0% | up to $48,350 | up to $96,700 | up to $64,750 [2025 authority](https://www.irs.gov/pub/irs-drop/rp-24-40.pdf) |
| 15% | $48,350 – $533,400 | $96,700 – $600,050 | $64,750 – $566,700 [2025 authority](https://www.irs.gov/pub/irs-drop/rp-24-40.pdf) |
| 20% | over $533,400 | over $600,050 | over $566,700 [2025 authority](https://www.irs.gov/pub/irs-drop/rp-24-40.pdf) |

- **Unrecaptured §1250 gain** — Distinguish this preferential-rate category from ordinary depreciation recapture; use the applicable Schedule D worksheet. [Publication 550](https://www.irs.gov/publications/p550).
- **Collectibles and unrecaptured §1250 gain** — Use the Schedule D Tax Worksheet where required; the maximum rates are 28% and 25% respectively. NFT classification under the associated-asset analysis: Check this point with one of our partner accountants. [Publication 550](https://www.irs.gov/publications/p550).
- **Qualified small business stock (§1202)** — Acquisition/issuance dates, exclusion percentages, holding periods, per-issuer/basis limits, gross assets and eligible-business tests need a separate analysis: Check this point with one of our partner accountants.
- **Short-term capital gain taxation** — Short-term capital gain (held ≤ 1 year): taxed at ordinary rates per §2.2.  _(§1(h))_

### 2.4 AMT exemption — 2025 only

**AMT exemption table**  _(§55(d))_

| Filing status | Exemption | Phaseout begins | Fully phased out |
| --- | --- | --- | --- |
| Single / HoH | $88,100 | $626,350 | $978,750 [2025 authority](https://www.irs.gov/pub/irs-pdf/f6251.pdf) |
| MFJ / QSS | $137,000 | $1,252,700 | $1,800,700 [2025 authority](https://www.irs.gov/pub/irs-pdf/f6251.pdf) |
| MFS | $68,500 | $626,350 | $900,350 [2025 authority](https://www.irs.gov/pub/irs-pdf/f6251.pdf) |

- **AMT rates (2025)** — After the exemption, 26% applies to the first $239,100 ($119,550 MFS) of the ordinary AMT base and 28% above. Preferential capital gains require Form 6251 Part III. The 2025 exemption reduction is 25% of AMTI above its threshold. MFS AMTI above $900,350 has an additional adjustment; apply the instructions. [Form 6251](https://www.irs.gov/pub/irs-pdf/f6251.pdf); [instructions](https://www.irs.gov/instructions/i6251).

### 2.5 NIIT (Net Investment Income Tax) — §1411

**NIIT MAGI thresholds**  _(§1411)_

| Filing status | MAGI threshold |
| --- | --- |
| Single / HoH | $200,000 [2025 authority](https://www.irs.gov/instructions/i8960) |
| MFJ / QSS | $250,000 [2025 authority](https://www.irs.gov/instructions/i8960) |
| MFS | $125,000 [2025 authority](https://www.irs.gov/instructions/i8960) |

- **NIIT rate** — 3.8% on the lesser of (a) net investment income or (b) MAGI excess over threshold  _(§1411)_
- **NIIT scope** — These filing-status thresholds apply to US citizens/residents. International residency and elections need separate analysis. [Form 8960 instructions](https://www.irs.gov/instructions/i8960).

### 2.6 Additional Medicare Tax — §3101(b)(2) and §1401(b)(2)

**Additional Medicare Tax thresholds**  _(§3101(b)(2) and §1401(b)(2))_

| Filing status | Threshold |
| --- | --- |
| Single / HoH | $200,000 [2025 authority](https://www.irs.gov/instructions/i8959) |
| MFJ | $250,000 [2025 authority](https://www.irs.gov/instructions/i8959) |
| MFS | $125,000 [2025 authority](https://www.irs.gov/instructions/i8959) |

- **Additional Medicare Tax rate** — 0.9% on Medicare wages plus positive self-employment income above the filing-status threshold. RRTA compensation is tested separately. Use Medicare wages (generally W-2 box 5), not box 1. QSS uses $200,000. Reconcile actual withholding on Form 8959. [instructions](https://www.irs.gov/instructions/i8959).
- **Reporting** — Reported on Form 8959, flows to Schedule 2 Line 11. Employer withholds the 0.9% on wages over $200,000 regardless of filing status; the return reconciles.  _(§3101(b)(2) and §1401(b)(2))_

### 2.7 SALT cap — §164(b)(6) as amended by OBBBA

- **SALT type and MAGI** — Apply the cap to deductible state/local income or sales taxes plus qualifying real/personal property taxes, rather than every payment called a tax. MAGI includes the prescribed excluded-income addbacks. [Schedule A instructions](https://www.irs.gov/instructions/i1040sca).
- **SALT limit** — The applicable limitation amount is $40,000 for 2025 and $40,400 for 2026; the pre-MFS-halving floor is $10,000. The elevated amounts run through 2029, with 101% annual increases after 2026; $10,000 applies from 2030. MFS takes half the applicable amount after the reduction. [P.L.119-21 §70120](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm).
- **SALT reduction** — Compute max($10,000, applicable limitation amount − 30% × max(0, MAGI − threshold)); then halve the result for MFS. The threshold is $500,000 for 2025, $505,000 for 2026, each halved for MFS. Deduct the lesser of qualifying taxes and this limit. Thus 2026 Single MAGI $550,000 gives excess $45,000, reduction $13,500 and limit $26,900. In 2025 the Single limit reaches $10,000 at $600,000 MAGI; the MFS floor is $5,000. [§70120](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm); [2025 worksheet](https://www.irs.gov/instructions/i1040sca).

### 2.8 Kiddie tax — §1(g)

- **Kiddie tax unearned income threshold** — For tax year 2025: a child's unearned income over $2,700 is taxed at the parents' marginal rate.  _(§1(g))_
- **Kiddie tax applicability** — Apply the Form 8615 tests together: unearned income over $2,700 for 2025; a required return; at least one living parent; no joint return; and the applicable age/earned-income/support test (under 18, age 18 without earned income exceeding half support, or a full-time student age 19–23 without earned income exceeding half support). Age/support alone does not establish liability. [KID](https://www.irs.gov/instructions/i8615).
- **Form 8814 election (2025)** — The child must be under 19, or a full-time student under 24; have only interest/dividends including permitted distributions; gross income below $13,500; be required to file; not file jointly; and have no federal withholding or estimated payments including a prior-year credit. The electing parent must satisfy the instructions’ joint-return/custody/higher-taxable-income rules and file timely with Form 8814. Compare the resulting tax before electing. [instructions](https://www.irs.gov/instructions/i8814).

### 2.9 Other OBBBA changes

- **QBI** — Employee wages are not QBI. Qualified REIT dividends and qualified PTP income may produce a deduction; do not set line 13a to zero just because there is no Schedule C. For eligibility, wage/property limits, SSTBs, threshold/phase-in calculations and the post-2025 minimum deduction: Check this point with one of our partner accountants. [Form 8995 instructions](https://www.irs.gov/instructions/i8995).
- **Ordinary brackets** — Use the separately dated 2025 tables below or 2026 tables in section 0. Do not substitute one year for the other.
- **Standard deduction increase** — increased for 2025 under OBBBA (see §2.1).  _(OBBBA)_
- **Child/other-dependent credits** — Use Schedule 8812 and the eligibility tests below; a cap does not establish entitlement. [2025 instructions](https://www.irs.gov/instructions/i1040s8).
- **§25D Residential Clean Energy Credit termination** — **AUDIT FLASH POINT** — P.L.119-21 §70506 terminates the credit for expenditures made after December 31, 2025 (IRC §25D(h)). Apply the operative expenditure/completion rules to the actual installation; the former phase-down does not extend that deadline. A placeholder notice number is not authority. [LAW](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm).
- **Clean-vehicle termination** — New and previously owned vehicle credits do not apply to vehicles acquired after September 30, 2025. Timely acquisition does not by itself establish eligibility; delivery/placed-in-service and other tests remain. [2025 Form 8936 instructions](https://www.irs.gov/instructions/i8936).
- **§25E Used Clean Vehicle Credit termination** — P.L.119-21 §70501 terminates §25E for vehicles acquired after September 30, 2025. Establish acquisition and other eligibility conditions separately. [LAW](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm).
- **Qualified tips: occupation, voluntary cash-tip character, reporting, SSN, marital-status and phaseout tests** — Check this point with one of our partner accountants. These Schedule 1-A topics are not cleared merely by an income figure or form label.
- **Qualified overtime: only the FLSA-required premium, reporting, SSN, marital-status and phaseout tests** — Check this point with one of our partner accountants. These Schedule 1-A topics are not cleared merely by an income figure or form label.
- **Passenger-vehicle loan interest: new-vehicle original use, acquisition/loan dates, personal use, lien, final US assembly, VIN and phaseout tests** — Check this point with one of our partner accountants. These Schedule 1-A topics are not cleared merely by an income figure or form label.

## 3. Filing status and dependents

### 3.1 Filing status determination — §1 and §2

- **Status determination** — Ordinarily use marital status on the last day of the tax year. Death, remarriage, nonresident spouses and community-property income require their specific rules. [Publication 501](https://www.irs.gov/publications/p501).
- **Single** — unmarried, not HoH, not QSS.  _(§1)_
- **Married filing jointly (MFJ)** — married on 12/31, both spouses agree to file jointly, joint and several liability under §6013.  _(§6013)_
- **Married filing separately (MFS)** — Married taxpayers may file separately, but test each benefit individually. Education credits, student-loan interest and the education savings-bond interest exclusion are generally unavailable; EITC and dependent-care rules have qualifying separated-spouse exceptions. The elderly/disabled credit is generally unavailable if the spouses lived together at any time during the year. The adoption exclusion/credit is unavailable in most cases. If one spouse itemizes, the other MFS spouse cannot take the standard deduction. An IRA deduction is not universally barred: plan coverage, income and living-apart conditions matter. Apply the status-specific SALT cap and other limits. [Publication 501](https://www.irs.gov/publications/p501); [Publication 590-A](https://www.irs.gov/publications/p590a).
- **Head of household (HoH)** — Meet the unmarried/considered-unmarried rules, pay more than half the home’s cost and have a qualifying person under Publication 501. A qualifying parent can satisfy the separate-parent-home rule without living with the taxpayer; other qualifying persons generally need the required residence. A qualifying relative who is a dependent only because of full-year household membership is not a qualifying person for HoH. Apply the listed relationship and dependency conditions rather than treating every resident qualifying relative as sufficient. [P501](https://www.irs.gov/publications/p501).
- **QSS (2025)** — A spouse died in 2023 or 2024; no remarriage by the end of 2025; entitlement to a joint return in the death year; a child/stepchild (not foster child) meeting the dependency test or one of the specified exceptions; that child lives in the home all year subject to permitted absences/birth/death rules; and the taxpayer pays more than half the home cost. This provides MFJ rates and the QSS deduction. After the two-year window, test Single/HoH. [Publication 501](https://www.irs.gov/publications/p501).

### 3.2 Qualifying child — §152(c)

- **Qualifying child tests** — First apply the dependent-taxpayer, citizenship/residency and joint-return gateways in Publication 501; a dependent generally must be a US citizen/national/resident or resident of Canada/Mexico, with the adopted-child exception. Then apply all five tests: 1. Relationship: child, stepchild, foster child, sibling, half-sibling, step-sibling, or descendant of any of these. 2. Age: under 19 at year-end and younger than the taxpayer (or spouse if filing jointly), OR under 24, a full-time student for at least 5 months and younger than the taxpayer (or spouse), OR any age if permanently and totally disabled. 3. Residency: lived with taxpayer for more than half the year (temporary absences for school, illness, military service count as present). 4. Support: child did not provide more than half of their own support. 5. Joint return: child is not filing a joint return (unless filed solely to recover withheld income tax or estimated tax paid).  _(§152(c))_ [P501](https://www.irs.gov/publications/p501).

### 3.3 Qualifying relative — §152(d)

- **Qualifying relative tests** — Apply the same general dependency gateways, then all four tests: 1. Not a qualifying child: of the taxpayer or any other taxpayer. 2. Relationship or residency: either related to taxpayer per the §152(d)(2) list (parents, siblings, in-laws, etc. — these need not live with taxpayer) OR lived with taxpayer as a member of the household for the entire year. 3. Gross income: less than $5,200 for 2025 ($5,300 for 2026). [2025 Publication 501](https://www.irs.gov/publications/p501); [2026 Rev. Proc.2025-32](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf). Social Security benefits are generally excluded from "gross income" for this test if not taxable to the dependent. 4. Support: taxpayer provided more than half of the dependent's total support.  _(§152(d); §151(d)(4); Rev. Proc. 2024-40)_

### 3.4 Tiebreaker rules — §152(c)(4)

- **Tiebreaker rules** — A parent prevails over a nonparent. If two eligible parents do not file jointly, the parent with whom the child lived longer prevails; if equal, use the higher parent AGI. If no parent can claim the child as a qualifying child, the eligible person with the highest AGI prevails. If a parent can claim but no eligible parent does so, a nonparent can claim only if that person’s AGI exceeds the highest AGI of any eligible parent. [Publication 501](https://www.irs.gov/publications/p501).

## 4. Income — Form 1040 lines 1-8

### 4.1 Line 1: Wages and related

**Line 1 wages breakdown**

| Sub-line | Item | Source |
| --- | --- | --- |
| 1a | W-2 Box 1 wages | Form W-2 [2025 authority](https://www.irs.gov/instructions/i1040gi) |
| 1b | Household employee wages NOT on W-2 | Schedule H / records [2025 authority](https://www.irs.gov/instructions/i1040gi) |
| 1c | Tip income NOT reported to employer | Form 4137 [2025 authority](https://www.irs.gov/instructions/i1040gi) |
| 1d | Medicaid waiver payments not reported on W-2; apply exclusion separately | [2025 Form 1040 instructions](https://www.irs.gov/instructions/i1040gi) |
| 1e | Taxable dependent care benefits | Form 2441 Part III [2025 authority](https://www.irs.gov/instructions/i1040gi) |
| 1f | Employer-provided adoption benefits | Form 8839 [2025 authority](https://www.irs.gov/instructions/i1040gi) |
| 1g | Wages from Form 8919 (uncollected SS/Medicare) | Form 8919 [2025 authority](https://www.irs.gov/instructions/i1040gi) |
| 1h | Other earned income | various [2025 authority](https://www.irs.gov/instructions/i1040gi) |
| 1i | Nontaxable combat pay election | W-2 Box 12 code Q [2025 authority](https://www.irs.gov/instructions/i1040gi) |
| 1z | Sum of 1a through 1h (1i is informational only) | computed [2025 authority](https://www.irs.gov/instructions/i1040gi) |

- **Wage checks** — Sum W-2 box 1 into line 1a and box 2 withholding into 25a. For 2025, test each employee separately for actual Social Security withholding over $10,918.20 from multiple employers; do not combine spouses or infer the credit from box 1 wages. One-employer errors must first be corrected by that employer. Statutory-employee income routes to Schedule C. Disability pension before minimum retirement age generally goes to 1h. [2025 Form 1040 instructions](https://www.irs.gov/instructions/i1040gi).

### 4.2 Line 2: Interest income

- **Line 2a — tax-exempt interest** — Tax-exempt interest (municipal bonds, mutual fund exempt-interest dividends). Reported informationally only. Watch: private activity bond interest from these may be an AMT preference (§57(a)(5)).  _(§57(a)(5))_
- **Line 2b — taxable interest** — Includes: Bank/CD interest (1099-INT Box 1); US Treasury interest (1099-INT Box 3) — taxable federally, exempt from state tax; Original issue discount (1099-OID); Seller-financed mortgage interest received; Interest on income tax refunds (1099-INT from IRS or state)
- **Schedule B requirement** — Apply the Schedule B instructions: taxable interest over $1,500 or ordinary dividends over $1,500 is a separate threshold test, not their combined sum. Seller-financed mortgage interest and applicable foreign-account/trust and other listed conditions can also require it. Private-activity-bond tax-exempt interest alone is not a listed Schedule B trigger. [B](https://www.irs.gov/instructions/i1040sb).

### 4.3 Line 3: Dividends

- **Line 3a — qualified dividends** — Report qualified dividends from 1099-DIV box 1b only after confirming an eligible US/qualified foreign corporation, no excluded dividend category and the holding/risk-of-loss conditions. Days with diminished risk of loss do not count toward holding requirements. Ordinarily, hold the stock more than 60 days during the 121-day period beginning 60 days before the ex-dividend date. The more-than-90-days/181-day preferred-stock rule applies to dividends attributable to periods totaling more than 366 days; it is not a rule for every preferred dividend. [P550](https://www.irs.gov/publications/p550).
- **Line 3b — ordinary dividends** — Ordinary dividends (1099-DIV Box 1a) — includes qualified dividends; reports the total.
- **Schedule B requirement for dividends** — Schedule B required if Line 3b > $1,500.

### 4.4 Line 4: IRA distributions

- **Line 4a/4b overview** — Line 4a: Gross IRA distributions (1099-R from traditional, SEP, SIMPLE IRAs); Line 4b: Taxable portion
- **Determining 4b — no basis** — An ordinary fully taxable traditional IRA distribution with no basis or exclusion is taxable; first remove any valid rollover/QCD or other excluded amount. Use the instructions to determine whether gross line 4a must be filled. [2025 instructions](https://www.irs.gov/instructions/i1040gi).
- **Determining 4b — basis from nondeductible contributions** — Traditional IRA with basis from nondeductible contributions (Form 8606 history): pro-rata recovery via Form 8606 Part I.
- **Roth IRA distribution ordering rules** — Apply the qualified-distribution rules first. For nonqualified distributions, regular contributions come out first, then conversions/rollovers under the separate ordering and five-year rules, then earnings. A conversion recapture tax generally concerns its taxable conversion portion distributed within the separate five-year period before age 59½, subject to exceptions. Nonqualified earnings may be taxable; the 10% additional tax depends on age and exceptions. Do not impose an unconditional penalty on all conversion amounts or earnings. [P590B](https://www.irs.gov/publications/p590b).
- **QCD (2025)** — Up to $108,000 per eligible IRA owner; at least age 70½ at distribution; made directly by the trustee of an IRA other than an ongoing SEP/SIMPLE to an eligible organization. Exclusion is limited to otherwise-taxable amounts and can be reduced by post-70½ deductible contributions. Obtain acknowledgment; no charitable deduction for the excluded QCD. On final 2025 Form 1040, use line 4c box 2 for QCD and determine 4b under the instructions. [Publication 590-B](https://www.irs.gov/publications/p590b).
- **Rollover** — Establish eligible-distribution, receiving-plan, 60-day/waiver, one-IRA-rollover-per-year and RMD restrictions before excluding an amount. Transfers and direct rollovers have different rules. Complex/late/partial/inherited rollovers: Check this point with one of our partner accountants. [Publication 590-A](https://www.irs.gov/publications/p590a).
- **RMD shortfalls** — Form 5329 applies a 25% additional tax, reduced to 10% for qualifying timely correction. The correction window ends at the earliest statutory notice, assessment or end of the second following taxable year; reasonable-error waiver rules are separate. For the actual shortfall/correction/waiver: Check this point with one of our partner accountants. [Publication 590-B](https://www.irs.gov/publications/p590b).

### 4.5 Line 5: Pensions and annuities

- **Line 5a/5b overview** — Line 5a: Gross distributions (1099-R from employer plans, 401(k), 403(b), 457, defined benefit); Line 5b: Taxable portion
- **Determining 5b** — Determine taxable pension/annuity amounts under Publication 575, accounting for basis, rollovers and exclusions. The Simplified Method depends on a qualified plan, annuity starting date and the age/guaranteed-payment conditions, not just a start after November 18, 1996. For General Rule, NUA, Form 4972 and unusual contracts: Check this point with one of our partner accountants. [Publication 575](https://www.irs.gov/publications/p575).

### 4.6 Line 6: Social Security benefits

- **Lines 6a/6b/6c overview** — Line 6a: Gross SSA-1099 / RRB-1099 benefits; Line 6b: Taxable portion (0%, up to 50%, or up to 85%); Line 6c: Lump-sum election checkbox (if claiming the §86(e) election to spread prior-year benefits)  _(§86(e))_
- **Computation method** — Computation: Pub 915 Worksheet 1 (or the worksheet in the Form 1040 instructions).
- **Social Security computation** — Use the 2025 Social Security Benefits Worksheet, including its modified-income adjustments. For ordinary domestic Single/MFJ cases the base comparison includes other income plus tax-exempt interest plus half the benefits: first thresholds $25,000/$32,000 and second thresholds $34,000/$44,000; no more than 85% of benefits is taxable. MFS living-together, benefit repayments, excluded foreign income, IRA adjustments and lump-sum elections require the separate worksheet rules. [2025 instructions](https://www.irs.gov/instructions/i1040gi).

### 4.7 Line 7: Capital gains

- **Line 7 sourcing** — Use final 2025 Form 1040 line 7a for the amount. Where the instructions permit capital-gain distributions to be reported without Schedule D, check line 7b (Schedule D not required); do not leave it unchecked merely because the schedule is omitted. [F](https://www.irs.gov/pub/irs-pdf/f1040.pdf); [I](https://www.irs.gov/instructions/i1040gi).

### 4.8 Line 8: Other income (from Schedule 1 Line 10)

See §5.

### 4.9 Line 9: Total income

- **Total income formula** — Sum of lines 1z, 2b, 3b, 4b, 5b, 6b, 7a and 8.  _(Form 1040)_

### 4.10 Line 10: Adjustments to income (from Schedule 1 Line 26)

See §5.

### 4.11 Line 11: AGI

- **AGI formula** — Line 9 minus line 10 gives 11a, carried to 11b.  _(Form 1040)_

## 5. Schedule 1 — Additional Income and Adjustments

### 5.1 Part I — Additional income (flows to 1040 Line 8)

**Schedule 1 Part I table**

| Line | Item | Notes |
| --- | --- | --- |
| 1 | Taxable refunds, credits or offsets of state/local income taxes | Apply the tax-benefit worksheet; taxable only to the extent the prior deduction reduced tax [2025 authority](https://www.irs.gov/pub/irs-pdf/f1040s1.pdf) |
| 2a | Alimony received | Pre-2019 instruments only if not modified to adopt the later regime; establish deductible/taxable alimony conditions [2025 authority](https://www.irs.gov/pub/irs-pdf/f1040s1.pdf) |
| 3 | Business income / loss | Schedule C — refer to freelance skill [2025 authority](https://www.irs.gov/pub/irs-pdf/f1040s1.pdf) |
| 4 | Other gains/losses | Form 4797 (depreciable business property, §1231) [2025 authority](https://www.irs.gov/pub/irs-pdf/f1040s1.pdf) |
| 5 | Rental real estate, royalties, partnerships, S corps, trusts | Schedule E [2025 authority](https://www.irs.gov/pub/irs-pdf/f1040s1.pdf) |
| 6 | Farm income/loss | Schedule F [2025 authority](https://www.irs.gov/pub/irs-pdf/f1040s1.pdf) |
| 7 | Unemployment compensation | 1099-G Box 1 [2025 authority](https://www.irs.gov/pub/irs-pdf/f1040s1.pdf) |
| 8a | Net operating loss | §172 [2025 authority](https://www.irs.gov/pub/irs-pdf/f1040s1.pdf) |
| 8b | Gambling winnings | W-2G; losses deductible only as itemized misc up to winnings under §165(d) [2025 authority](https://www.irs.gov/pub/irs-pdf/f1040s1.pdf) |
| 8c | Cancellation of debt | Apply §108 exclusions. Qualified principal-residence indebtedness requires discharge before January 1, 2026, or a qualifying arrangement entered into and evidenced in writing before that date; there is no blanket extension of all 2026 discharges. [CODE108](https://uscode.house.gov/us/usc/119-124/t26/s108/). |
| 8d | Foreign earned income exclusion | Form 2555 (NEGATIVE amount) — refer to `us-foreign-earned-income-2555` [2025 authority](https://www.irs.gov/pub/irs-pdf/f1040s1.pdf) |
| 8e | Income from Form 8853 (Archer MSA) | [2025 authority](https://www.irs.gov/pub/irs-pdf/f1040s1.pdf) |
| 8f | Income from Form 8889 (taxable HSA distributions after its exclusions) | [2025 authority](https://www.irs.gov/pub/irs-pdf/f1040s1.pdf) |
| 8g | Alaska Permanent Fund dividends | [2025 authority](https://www.irs.gov/pub/irs-pdf/f1040s1.pdf) |
| 8h | Jury duty | [2025 authority](https://www.irs.gov/pub/irs-pdf/f1040s1.pdf) |
| 8i | Prizes and awards | Do not duplicate amounts on 8m; apply the medal exclusion separately [2025 authority](https://www.irs.gov/pub/irs-pdf/f1040s1.pdf) |
| 8j | Activity not for profit (hobby income) | §183 — see §16 audit flash point [2025 authority](https://www.irs.gov/pub/irs-pdf/f1040s1.pdf) |
| 8k | Stock options | Only income not reported elsewhere; never duplicate W-2 amounts [2025 authority](https://www.irs.gov/pub/irs-pdf/f1040s1.pdf) |
| 8l | Income from rental of personal property | For-profit personal-property rental outside a rental business; business rental belongs on Schedule C [2025 authority](https://www.irs.gov/pub/irs-pdf/f1040s1.pdf) |
| 8m | Olympic/Paralympic medals | [2025 authority](https://www.irs.gov/pub/irs-pdf/f1040s1.pdf) |
| 8n | §951(a) Subpart F inclusion | International — refer out [2025 authority](https://www.irs.gov/pub/irs-pdf/f1040s1.pdf) |
| 8o | §951A GILTI inclusion | Refer to `us-gilti-fdii-beat` [2025 authority](https://www.irs.gov/pub/irs-pdf/f1040s1.pdf) |
| 8p | §461(l) excess business loss disallowed | Re-included in income [2025 authority](https://www.irs.gov/pub/irs-pdf/f1040s1.pdf) |
| 8q | Taxable distributions from an ABLE account | [S1](https://www.irs.gov/pub/irs-pdf/f1040s1.pdf). |
| 8r | Scholarship/fellowship not reported on W-2 | [2025 authority](https://www.irs.gov/pub/irs-pdf/f1040s1.pdf) |
| 8s | Nontaxable Medicaid waiver payments included on Form 1040 line 1a or 1d | Enter as the prescribed subtraction. [S1](https://www.irs.gov/pub/irs-pdf/f1040s1.pdf). |
| 8t | Pension/annuity from a non-qualified deferred comp plan | Nonqualified deferred compensation / nongovernmental section 457 pension or annuity income [2025 authority](https://www.irs.gov/pub/irs-pdf/f1040s1.pdf) |
| 8u | Wages earned while incarcerated | [S1](https://www.irs.gov/pub/irs-pdf/f1040s1.pdf). |
| 8v | Digital asset received as reward/award/payment | Property transaction — refer to `us-digital-asset-transactions` if material [2025 authority](https://www.irs.gov/pub/irs-pdf/f1040s1.pdf) |
| 8z | Other income | Itemize on a statement [2025 authority](https://www.irs.gov/pub/irs-pdf/f1040s1.pdf) |
| 9 | Total other income | sum 8a-8z [2025 authority](https://www.irs.gov/pub/irs-pdf/f1040s1.pdf) |
| 10 | Total additional income | sum 1-9 → 1040 Line 8 [2025 authority](https://www.irs.gov/pub/irs-pdf/f1040s1.pdf) |

For exceptional cancellation-of-debt exclusions, medal/MSA/ABLE/stock-option classification, foreign inclusions and nonstandard adjustments: **Check this point with one of our partner accountants.** The table identifies form fields; it does not grant an exclusion or deduction merely because a form was received.

### 5.2 Part II — Adjustments to income (flows to 1040 Line 10)

**Schedule 1 Part II table**

| Line | Item | Notes |
| --- | --- | --- |
| 11 | Educator expenses (2025) | Up to $300 per eligible educator; K–12 teacher, instructor, counselor, principal or aide, at least 900 hours in the school year; qualified unreimbursed expenses with coordination for exclusions/reimbursements. [instructions](https://www.irs.gov/instructions/i1040gi) |
| 12 | Business expenses for reservists, performing artists, fee-basis gov officials | Form 2106 [2025 authority](https://www.irs.gov/pub/irs-pdf/f1040s1.pdf) |
| 13 | HSA deduction | Form 8889 — 2025 full-year limits $4,300 self-only / $8,550 family, plus eligible age-55 $1,000 catch-up; apply eligibility/month and employer-contribution rules below [2025 authority](https://www.irs.gov/pub/irs-pdf/f1040s1.pdf) |
| 14 | Moving expenses | Active-duty military PCS only (TCJA §11049) [2025 authority](https://www.irs.gov/pub/irs-pdf/f1040s1.pdf) |
| 15 | Deductible part of SE tax | Schedule SE Line 13 — refer out [2025 authority](https://www.irs.gov/pub/irs-pdf/f1040s1.pdf) |
| 16 | SEP / SIMPLE / qualified plans | Refer to `us-self-employed-retirement` [2025 authority](https://www.irs.gov/pub/irs-pdf/f1040s1.pdf) |
| 17 | Self-employed health insurance deduction | Refer to `us-self-employed-health-insurance` [2025 authority](https://www.irs.gov/pub/irs-pdf/f1040s1.pdf) |
| 18 | Penalty on early withdrawal of savings | 1099-INT Box 2 [2025 authority](https://www.irs.gov/pub/irs-pdf/f1040s1.pdf) |
| 19a | Alimony paid | Pre-2019 qualifying instruments unless modified to adopt the later regime [2025 authority](https://www.irs.gov/pub/irs-pdf/f1040s1.pdf) |
| 19b | Recipient SSN | [2025 authority](https://www.irs.gov/pub/irs-pdf/f1040s1.pdf) |
| 19c | Date of original divorce/separation | [2025 authority](https://www.irs.gov/pub/irs-pdf/f1040s1.pdf) |
| 20 | IRA deduction | Traditional IRA — 2025 limits $7,000 / $8,000 age 50+ catch-up; phaseout for active participants in employer plan [2025 authority](https://www.irs.gov/pub/irs-pdf/f1040s1.pdf) |
| 21 | Student loan interest deduction | Up to $2,500; phaseout $85k-$100k single / $170k-$200k MFJ (2025) [2025 authority](https://www.irs.gov/pub/irs-pdf/f1040s1.pdf) |
| 22 | Reserved | [2025 authority](https://www.irs.gov/pub/irs-pdf/f1040s1.pdf) |
| 23 | Archer MSA deduction | [2025 authority](https://www.irs.gov/pub/irs-pdf/f1040s1.pdf) |
| 24a | Jury duty pay turned over to employer | [2025 authority](https://www.irs.gov/pub/irs-pdf/f1040s1.pdf) |
| 24b | Deductible expenses related to Line 8l (personal property rental) | [2025 authority](https://www.irs.gov/pub/irs-pdf/f1040s1.pdf) |
| 24c | Nontaxable Olympic/Paralympic medals | If Line 8m [2025 authority](https://www.irs.gov/pub/irs-pdf/f1040s1.pdf) |
| 24d | Reforestation amortization / expense | [2025 authority](https://www.irs.gov/pub/irs-pdf/f1040s1.pdf) |
| 24e | Repayment of supplemental unemployment | [2025 authority](https://www.irs.gov/pub/irs-pdf/f1040s1.pdf) |
| 24f | Contributions to §501(c)(18)(D) plans | [2025 authority](https://www.irs.gov/pub/irs-pdf/f1040s1.pdf) |
| 24g | Contributions by certain chaplains to §403(b) | [2025 authority](https://www.irs.gov/pub/irs-pdf/f1040s1.pdf) |
| 24h | Attorney fees and court costs for §62(a)(20) discrimination suits | [2025 authority](https://www.irs.gov/pub/irs-pdf/f1040s1.pdf) |
| 24i | Attorney fees and court costs for whistleblower awards | [2025 authority](https://www.irs.gov/pub/irs-pdf/f1040s1.pdf) |
| 24j | Housing deduction (Form 2555) | [2025 authority](https://www.irs.gov/pub/irs-pdf/f1040s1.pdf) |
| 24k | Excess deductions of section 67(e) expenses from Schedule K-1 (Form 1041) | [S1](https://www.irs.gov/pub/irs-pdf/f1040s1.pdf). |
| 24z | Other adjustments | [2025 authority](https://www.irs.gov/pub/irs-pdf/f1040s1.pdf) |
| 25 | Total other adjustments | sum 24a-24z [2025 authority](https://www.irs.gov/pub/irs-pdf/f1040s1.pdf) |
| 26 | Total adjustments to income | sum 11-23, 25 → 1040 Line 10 [2025 authority](https://www.irs.gov/pub/irs-pdf/f1040s1.pdf) |

### 5.3 IRA and HSA operative conditions — 2025

HSA contributions require eligible HDHP coverage, no disqualifying coverage, no Medicare enrollment and no dependent eligibility. Use eligible months or the last-month rule with its testing period. Employer/cafeteria contributions reduce the available individual limit and are not deducted again. Catch-up contributions require age 55 and a separate eligible spouse account. For IRAs, cap combined traditional/Roth contributions at eligible compensation and the annual limit; determine each spouse’s coverage and MAGI. MFS living apart all year uses the stated separate rules; do not universally deny the IRA deduction. Student-loan interest requires a qualified loan, legal interest obligation, permitted filing status, dependency and MAGI tests. [Publication 969](https://www.irs.gov/publications/p969); [Publication 590-A](https://www.irs.gov/publications/p590a); [2025 instructions](https://www.irs.gov/instructions/i1040gi).

### IRA deduction phaseout (Line 20) — 2025

**IRA deduction phaseout table**

| Filing status | Phaseout range |
| --- | --- |
| Single / HoH, active participant | $79,000 – $89,000 MAGI [2025 authority](https://www.irs.gov/publications/p590a) |
| MFJ, taxpayer active participant | $126,000 – $146,000 MAGI [2025 authority](https://www.irs.gov/publications/p590a) |
| MFJ, only spouse active participant | $236,000 – $246,000 MAGI [2025 authority](https://www.irs.gov/publications/p590a) |
| MFS, active participant | $0 – $10,000 MAGI [2025 authority](https://www.irs.gov/publications/p590a) |

- **No income limit / Roth phaseouts** — If neither spouse is an active participant, no deduction income phaseout, but compensation and contribution limits remain. Roth IRA contribution (not deductible but tracked) phaseouts for 2025: $150,000-$165,000 single / $236,000-$246,000 MFJ.

## 6. Standard vs itemized — Schedule A

### 6.1 The decision

- **Standard vs itemized decision** — Compare standard deduction (§2.1) against the sum of Schedule A items. Generally choose the greater federal benefit if eligible; a taxpayer may elect to itemize even if lower. MFS spouse-itemizing, dual-status and other disqualifications can bar the standard deduction; apply Publication 501 rather than assuming everyone qualifies.  _(§63(c)(6))_

### 6.2 Schedule A line-by-line

- **Medical/dental (2025), lines 1–4** — Only qualifying unreimbursed expenses, generally paid in 2025, above 7.5% of AGI. No duplicate deduction for reimbursed/pre-tax/above-the-line premiums; qualified long-term-care premiums have age limits. Medical driving is 21 cents per mile in 2025. For capital improvements and unusual care/insurance: Check this point with one of our partner accountants. [Schedule A instructions](https://www.irs.gov/instructions/i1040sca).
- **Taxes paid — Lines 5-7 — SALT cap** — Line 5a: State and local income tax OR general sales tax (election) — sales tax via the IRS optional sales tax tables in Pub 600 / Schedule A instructions, plus actual receipts for big-ticket items. Line 5b: State and local real estate tax (excluding rental property — that goes on Schedule E). Line 5c: State and local personal property tax (e.g., car registration based on value). Line 5d: Sum 5a + 5b + 5c. Line 5e: Lesser of 5d or SALT cap (see §2.7 — $40,000 / $20,000 MFS for 2025, phased down above $500k/$250k MAGI). Line 6: Other eligible taxes (including foreign income taxes not taken as a credit); no occupational-tax blanket deduction. Line 7: Sum 5e + 6
- **Interest paid — Lines 8-10** — Line 8a: Home mortgage interest from 1098 (qualifying acquisition debt generally capped at $750,000 ($375,000 MFS) after December 15, 2017, or $1,000,000 ($500,000 MFS) for qualifying earlier debt; apply refinance, date and mixed-debt rules — §163(h)(3) as amended by TCJA, made permanent by OBBBA §70108). Line 8b: Mortgage interest not on 1098 (seller-financed; report payee name, address, SSN/EIN). Line 8c: Points not on 1098. Line 8d is reserved for 2025: no mortgage-insurance-premium deduction for 2025. The 2026 treatment is separate in section 0. Line 8e: Sum. Line 9: Investment interest (Form 4952) — limited to net investment income. Line 10: Sum 8e + 9  _([§163(h)(3); OBBBA §70108](https://www.irs.gov/pub/irs-pdf/f1040sa.pdf))_
- **Home equity interest deductibility** — Home equity interest is deductible only if proceeds used to buy, build, or substantially improve the residence securing the loan (§163(h)(3)(F) post-TCJA). Cash-out for personal use is nondeductible.  _(§163(h)(3)(F))_
- **Gifts to charity — Lines 11-14** — Line 11 reports cash gifts; the ordinary cash-to-qualifying-public-charity limit is 60% of AGI. Line 12 reports other-than-cash gifts: ordinary noncash gifts to qualifying public charities can have a 50% limit, long-term capital-gain property generally 30%, and qualifying capital-gain-property gifts to private nonoperating foundations generally 20%; classify recipient/property and apply the relevant elections/special rules. Form 8283 is generally required above $500; appraisal rules above $5,000 have exceptions. Generally obtain/retain the appraisal; attachment generally begins above $500,000, with special-category exceptions. Line 13 reports carryovers: excess charitable contributions generally carry forward for up to 5 years under the applicable percentage/order rules. Line 14 totals the deductible amounts. The 0.5% contribution-base floor starts with tax years after December 31, 2025 under §70425; it does not apply to 2025. Substantiation, quid-pro-quo reductions, property valuation and recipient eligibility must be established; unusual gifts/elections: Check this point with one of our partner accountants. [Publication 526](https://www.irs.gov/publications/p526); [P.L.119-21](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm).
- **AUDIT FLASH POINT — Charitable contributions outsized vs AGI** — Above $5,000, establish whether a qualified appraisal is required and was obtained, with the correct Form 8283 section. Do not call every appraisal “attached”: attachment generally begins above $500,000, subject to special rules/exceptions. Vehicle gifts, conservation easements and acknowledgment requirements remain separate checks; refer unresolved specialist cases. [P526](https://www.irs.gov/publications/p526).
- **Casualty and theft losses — Line 15** — For 2025 personal-use losses, apply the federally declared-disaster restriction and the exception allowing other personal casualty losses to the extent of personal casualty gains. The ordinary $100/event and 10%-of-AGI floors are not universal: qualified disaster losses, as defined in Publication 547, can instead use the $500 reduction without that percentage floor. Establish the disaster/category before calculating Form 4684. The §70109 state-declared-disaster expansion applies to tax years beginning after December 31, 2025. [P547](https://www.irs.gov/publications/p547); [LAW](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm).
- **Other itemized — Line 16** — gambling losses up to gambling winnings (§165(d)), federal estate tax on income in respect of a decedent (§691(c)), impairment-related work expenses, deduction for unrecovered investment in pension at death, amortizable bond premium on pre-10/23/86 taxable bonds.  _(§165(d); §691(c))_
- **Misc itemized deductions 2% floor suspension** — Misc itemized deductions subject to 2% AGI floor are SUSPENDED through 2025 by TCJA §11045, made permanent by OBBBA §70110. Exception, for tax years beginning after 31 December 2025: OBBBA §70110(b) adds IRC §67(b)(13), so unreimbursed educator expenses are no longer miscellaneous itemized deductions and remain deductible. This means unreimbursed employee business expenses, tax preparation fees, investment advisory fees, safe deposit box fees, and home office for an employee are not deductible. Reservists, performing artists, and fee-basis officials may still deduct via Schedule 1 Line 12.  _([TCJA §11045; OBBBA §70110](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm))_

### 6.3 Pease limitation

- **2025 overall limitation** — The former Pease limitation does not apply for 2025. A different top-bracket limitation starts in 2026; see section 0. [P.L.119-21 §70111](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm).

## 7. Line 12-15 — Standard/itemized deduction, QBI, taxable income

- **Line 12** — Greater of standard deduction (Line 2.1) or Schedule A Line 17.  _(Form 1040)_
- **Line 13a — QBI** — Employee wages do not qualify. Screen qualified REIT dividends/PTP income before concluding zero. For the computation: Check this point with one of our partner accountants. [Form 8995 instructions](https://www.irs.gov/instructions/i8995).
- **Line 14** — On final 2025 Form 1040, total line 12e + line 13a (QBI) + line 13b (Schedule 1-A); the additional deductions must not be dropped. [F](https://www.irs.gov/pub/irs-pdf/f1040.pdf).
- **Line 15 — Taxable income** — Taxable income = Line 11b (AGI) - line 14. If negative, enter 0.  _(Form 1040)_

## 8. Line 16 — Tax computation

- **Tax computation paths** — 1. Tax Tables (income < $100,000, no LTCG/qualified div): IRS-published. 2. Tax Computation Worksheet (income ≥ $100,000, no LTCG/qualified div): formulaic per bracket. 3. Qualified Dividends and Capital Gain Tax Worksheet (LTCG / QDIV present, no Schedule D Worksheet items): segregates LTCG/QDIV taxed at preferential rates (§2.3) from ordinary income taxed at §1(j) rates. 4. Schedule D Tax Worksheet (Schedule D Line 18 or 19 has §1250 unrecaptured or 28% collectibles): more granular bracketing for 25% and 28% rate gains. 5. Form 8615 (kiddie tax): child's unearned income > $2,700 taxed at parents' rate. 6. Schedule J (farm income averaging) — niche.
- **Worksheet selection** — Follow the line 16 instructions: special Form 8615/2555/4972/Schedule J paths can take precedence. If eligible for the Qualified Dividends and Capital Gain Tax Worksheet, use it; Schedule D Tax Worksheet applies in its specified cases. The ordinary-income step can require the Tax Table even within a preferential-rate worksheet. [2025 instructions](https://www.irs.gov/instructions/i1040gi).

## 9. Alternative Minimum Tax — Form 6251

### 9.1 When AMT bites in 2025

- **AMT screening** — Use the Form 6251 filing tests; exemption size alone does not settle whether the form is required. [instructions](https://www.irs.gov/instructions/i6251).
- **AMT adjustments** — Review ISO exercise-and-hold, specified private-activity-bond interest, depreciation differences, AMT NOL and passive/loss adjustments. An ISO spread need not exceed the exemption before it matters. Preferential gains require Part III and can affect exemption phaseout. [2025 Form 6251](https://www.irs.gov/pub/irs-pdf/f6251.pdf).

### 9.2 AMT computation flow

- **AMT computation (2025)** — Line 1a is Form 1040 line 14 less Schedule 1-A line 37; 1b subtracts that from 11b. Apply every relevant line 2/3 adjustment, including standard deduction or Schedule A taxes at 2a; total at 4. Apply line 5 exemption and MFS adjustment, then 6/7 and Part III where required. Subtract AMT foreign tax credit at 8 to obtain tentative minimum tax at 9. Line 10 is the form’s adjusted regular-tax comparison, not automatically Form 1040 line 16. Positive 9 minus 10 goes at 11 to Schedule 2 line 2. [Form 6251](https://www.irs.gov/pub/irs-pdf/f6251.pdf).

### 9.3 AMT credit — Form 8801

- **Prior-year minimum tax credit (Form 8801)** — Timing-item AMT and the later-year credit limitation require an actual Form 8801 computation. Exclusion items do not automatically generate a recoverable credit. Check this point with one of our partner accountants.

## 10. Capital gains and Schedule D

### 10.1 Schedule D flow

- **Schedule D parts** — Part I — short-term (held ≤ 1 year): from Form 8949 Part I boxes A (1099-B basis reported), B (basis not reported), C (no 1099-B). Part II — long-term (held > 1 year): boxes D, E, F. Digital-asset reporting uses its separate boxes and instructions. Part III — summary: net short-term + net long-term, carryovers, capital loss limitation.

### 10.2 Capital loss limitation — §1211(b)

- **Capital loss deduction limit** — Net capital loss deductible against ordinary income capped at $3,000 ($1,500 MFS). Excess carries forward indefinitely retaining character (short / long).  _(§1211(b))_

### 10.3 Wash sale — §1091

- **Wash sales** — A stock/securities loss can be disallowed when substantially identical stock/securities or an option/contract is acquired within 30 days before/after sale, including specified spouse/controlled-company/IRA purchases. Ordinarily add the disallowed loss to replacement basis and tack the holding period; an IRA replacement does not receive that basis addition. Report code W under Form 8949 instructions. For digital-asset/security classification: Check this point with one of our partner accountants. [Publication 550](https://www.irs.gov/publications/p550); [Form 8949 instructions](https://www.irs.gov/instructions/i8949).

### 10.4 Holding period

- **Holding period rule** — Acquired-date day excluded; sale-date day counted. To get long-term, sale must be on or after the date one year + one day after acquisition.

### 10.5 §1202 QSBS

- **QSBS** — Acquisition/issuance dates, old/new holding periods, percentage exclusions, per-issuer/basis limits, gross-asset tests and excluded businesses: Check this point with one of our partner accountants.

### 10.6 §121 home sale exclusion

- **Home sale exclusion** — Ownership/use, MFJ eligibility, prior exclusions, nonqualified use, depreciation, partial relief and Form 1099-S reporting must be tested together. Check this point with one of our partner accountants.

## 11. Net Investment Income Tax — Form 8960

Computed on **Form 8960**, flows to **Schedule 2 Line 12**.

- **NII** — Generally taxable interest, dividends, annuities, royalties, rents and net disposition gains, less properly allocable deductions. Business income depends on passive status and trading-business rules; ordinary active business income is not a universal exclusion. [Form 8960 instructions](https://www.irs.gov/instructions/i8960).
- **NII exclusions** — Wages, Social Security, tax-exempt interest, qualifying retirement-plan/IRA distributions and income actually subject to SE tax are generally excluded. Real-estate-professional status alone does not exclude rent; establish a nonpassive trade/business or satisfy the safe harbor. [Form 8960 instructions](https://www.irs.gov/instructions/i8960).
- **NIIT** — 3.8% × min(max(0, NII), max(0, MAGI − filing-status threshold)). Use Form 8960 deductions, not gross investment receipts. [instructions](https://www.irs.gov/instructions/i8960).
- **NIIT MAGI** — For an ordinary domestic individual without special adjustments, AGI is the starting figure. Foreign exclusions and CFC/PFIC adjustments require separate analysis: Check this point with one of our partner accountants. [Form 8960 instructions](https://www.irs.gov/instructions/i8960).

## 12. Schedule 3 — Credits and payments

### 12.1 Part I — Nonrefundable credits

**Part I — Nonrefundable credits**  _(Schedule 3 Part I)_

| Line | Credit | Form | Refer-out |
| --- | --- | --- | --- |
| 1 | Foreign tax credit | Form 1116; the election to omit that form has separate conditions | `us-foreign-tax-credit-1116` [2025 authority](https://www.irs.gov/pub/irs-pdf/f1040s3.pdf) |
| 2 | Credit for child & dependent care | Form 2441 | — [2025 authority](https://www.irs.gov/pub/irs-pdf/f1040s3.pdf) |
| 3 | Education credits | Form 8863 (AOTC, LLC) | `us-education-credits-8863` [2025 authority](https://www.irs.gov/pub/irs-pdf/f1040s3.pdf) |
| 4 | Retirement savings contributions credit (Saver's Credit) | Form 8880 | — [2025 authority](https://www.irs.gov/pub/irs-pdf/f1040s3.pdf) |
| 5a | Residential clean energy credit (§25D) | Form 5695 — **OBBBA termination flag, see §2.9** | — [2025 authority](https://www.irs.gov/pub/irs-pdf/f1040s3.pdf) |
| 5b | Energy efficient home improvement credit (§25C) | Form 5695 — **OBBBA accelerated termination flag** | — [2025 authority](https://www.irs.gov/pub/irs-pdf/f1040s3.pdf) |
| 6 | Other nonrefundable credits | various | — [2025 authority](https://www.irs.gov/pub/irs-pdf/f1040s3.pdf) |
| 6a | General business credit | Form 3800 | — [2025 authority](https://www.irs.gov/pub/irs-pdf/f1040s3.pdf) |
| 6b | Prior-year minimum tax credit | Form 8801 | —  [S3](https://www.irs.gov/pub/irs-pdf/f1040s3.pdf). |
| 6c | Nonrefundable adoption credit | Form 8839; refundable part goes to Form 1040 line 30 | —  [S3](https://www.irs.gov/pub/irs-pdf/f1040s3.pdf). |
| 6d | Credit for the elderly or disabled | Schedule R | —  [S3](https://www.irs.gov/pub/irs-pdf/f1040s3.pdf). |
| 6e | Reserved for future use | — | —  [S3](https://www.irs.gov/pub/irs-pdf/f1040s3.pdf). |
| 6f | Clean vehicle credit | Form 8936 | —  [S3](https://www.irs.gov/pub/irs-pdf/f1040s3.pdf). |
| 6g | Mortgage interest credit, including eligible carryforward | Form 8396 | —  [S3](https://www.irs.gov/pub/irs-pdf/f1040s3.pdf). |
| 6h | District of Columbia first-time homebuyer credit (legacy carryforward) | Form 8859 | [2025 Schedule 3](https://www.irs.gov/pub/irs-pdf/f1040s3.pdf) |
| 6j | Alternative fuel vehicle refueling property credit | Form 8911 | [2025 Schedule 3](https://www.irs.gov/pub/irs-pdf/f1040s3.pdf) |
| 6l | Amount from Form 8978 line 14 | Form 8978 | —  [S3](https://www.irs.gov/pub/irs-pdf/f1040s3.pdf). |
| 6m | Previously owned clean vehicle credit | Form 8936 | —  [S3](https://www.irs.gov/pub/irs-pdf/f1040s3.pdf). |
| 7 | Total other nonrefundable credits (lines 6a–6z) | Schedule 3 | —  [S3](https://www.irs.gov/pub/irs-pdf/f1040s3.pdf). |
| 8 | Total Part I (lines 1–4, 5a, 5b and 7) → Form 1040 line 20 | Schedule 3 | [S3](https://www.irs.gov/pub/irs-pdf/f1040s3.pdf). |

The nonrefundable child/other-dependent credit belongs on Form 1040 line 19 via Schedule 8812, not Schedule 3 line 6m. [Final 2025 Form 1040](https://www.irs.gov/pub/irs-pdf/f1040.pdf).

### 12.2 Part II — Refundable credits and other payments

**Part II — Refundable credits and other payments**  _(Schedule 3 Part II)_

| Line | Item |
| --- | --- |
| 9 | Net premium tax credit (Form 8962 — ACA marketplace) [2025 authority](https://www.irs.gov/pub/irs-pdf/f1040s3.pdf) |
| 10 | Amount paid with extension request (Form 4868) [2025 authority](https://www.irs.gov/pub/irs-pdf/f1040s3.pdf) |
| 11 | Excess Social Security tax withheld [2025 authority](https://www.irs.gov/pub/irs-pdf/f1040s3.pdf) |
| 12 | Credit for federal tax on fuels (Form 4136) [2025 authority](https://www.irs.gov/pub/irs-pdf/f1040s3.pdf) |
| 13 | Refundable credits not elsewhere [2025 authority](https://www.irs.gov/pub/irs-pdf/f1040s3.pdf) |
| 13a | Form 2439 (regulated investment company undistributed LTCG) [2025 authority](https://www.irs.gov/pub/irs-pdf/f1040s3.pdf) |
| 13b | Credit for repayment of amounts under claim of right >$3,000 (§1341) [2025 authority](https://www.irs.gov/pub/irs-pdf/f1040s3.pdf) |
| 13c | Net elective payment election amount from Form 3800 Part III line 6, column (j) [2025 Schedule 3](https://www.irs.gov/pub/irs-pdf/f1040s3.pdf). |
| 13d | Deferred section 965 net tax liability (see instructions) [2025 Schedule 3](https://www.irs.gov/pub/irs-pdf/f1040s3.pdf). |
| 13z | Other refundable [2025 authority](https://www.irs.gov/pub/irs-pdf/f1040s3.pdf) |
| 14 | Total other payments/refundable credits (13a–13z) [2025 Schedule 3](https://www.irs.gov/pub/irs-pdf/f1040s3.pdf). |
| 15 | Total Part II (9–12 and 14) → Form 1040 line 31 [2025 Schedule 3](https://www.irs.gov/pub/irs-pdf/f1040s3.pdf). |

### 12.3 Credits cheat sheet

**Credits cheat sheet**  _(Schedule 3 cheat sheet)_

| Credit | Refundable? | Cap 2025 | Phaseout begins (MFJ) |
| --- | --- | --- | --- |
| Child Tax Credit (CTC) | Partially ($1,700 ACTC) | $2,200/child <17 (OBBBA §70104) | $400,000 [2025 authority](https://www.irs.gov/instructions/i1040gi) |
| Credit for Other Dependents (ODC) | No | $500/dependent | $400,000 [2025 authority](https://www.irs.gov/instructions/i1040gi) |
| Earned Income Credit (EITC) | Yes | $649 – $8,046 by # kids | varies by household [2025 authority](https://www.irs.gov/instructions/i1040gi) |
| Child & Dependent Care | No | $3,000 / $6,000 expenses × 20–35% | Rate begins declining above $15,000 AGI; 20% applies above $43,000 (not a phaseout to zero). [2025 Form 2441, line 8](https://www.irs.gov/pub/irs-pdf/f2441.pdf). |
| AOTC | 40% refundable | $2,500 (100% first $2k + 25% next $2k) | $160k MFJ ($80k other) [2025 authority](https://www.irs.gov/instructions/i1040gi) |
| LLC | No | $2,000 (20% of $10k) | $160k MFJ ($80k other) [2025 authority](https://www.irs.gov/instructions/i1040gi) |
| Saver's Credit | No | $1,000 ($2,000 MFJ) | $47,500 MFJ (credit ends above $79,000) [2025 authority](https://www.irs.gov/instructions/i1040gi) |
| Adoption Credit | Specialist credit | Check this point with one of our partner accountants. | Timing, eligible child/expenses, refundability and carryovers require separate analysis. |
| Residential Clean Energy (§25D) | Nonrefundable | Check this point with one of our partner accountants. | Qualification/completion and carryforward analysis; no expenditures after 2025. [Act §70506](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| New clean vehicle (§30D) | Specialist credit | Check this point with one of our partner accountants. | MAGI/MSRP or sale-price, vehicle, seller, transfer and ownership tests; no acquisition after September 30, 2025. [2025 instructions](https://www.irs.gov/instructions/i8936) |
| Previously owned clean vehicle (§25E) | Specialist credit | Check this point with one of our partner accountants. | MAGI/MSRP or sale-price, vehicle, seller, transfer and ownership tests; no acquisition after September 30, 2025. [2025 instructions](https://www.irs.gov/instructions/i8936) |

### Credit eligibility — 2025 only

The caps above are ceilings, not entitlements. **CTC/ODC:** apply general dependency tests; CTC child under 17 at year end and a qualifying US citizen/national/resident; valid employment SSNs by the return due date including extensions for the child and taxpayer (at least one spouse if joint); the other joint filer needs a timely issued SSN or ITIN. ODC requires its own dependency, citizenship/residency and timely TIN tests. Apply Schedule 8812 MAGI reduction and nonrefundable liability limits. ACTC is not automatically $1,700: apply the earned-income/alternative-family computation and exclusions, including the Form 2555 restriction. [Schedule 8812 instructions](https://www.irs.gov/instructions/i1040s8).

**EITC:** apply all Form 1040 steps, including valid SSNs, earned-income and AGI limits for filing status/child count, no Form 2555, residency and investment-income rules. For 2025 the investment-income ceiling is $11,950; use the special worksheet when required. The EITC child tests include relationship, age/student/disability, US residence and joint-return conditions; dependency support tests are not interchangeable with EITC tests. Childless filers generally need age 25–64, US main home more than half the year, and no disqualifying dependent/qualifying-child status. Separated married persons require the particular statutory exception. [2025 Form 1040 EIC steps and tables](https://www.irs.gov/instructions/i1040gi).

**Dependent care:** qualifying child under 13 or qualifying incapable spouse/dependent; generally residence more than half the year. Care must enable work/job search; enforce both earned-income limits, special student/disability deemed-income rules, provider exclusions, required identifiers, eligible payment period and employer-benefit coordination. MFS generally cannot claim unless the specific living-apart/home-cost tests apply. The 2025 rate table above is not the changed 2026 rate table. [Form 2441 instructions](https://www.irs.gov/instructions/i2441).

**Education:** route to `us-education-credits-8863`. AOTC requires the first-four-years/four-credit-years, half-time credential-program and felony-drug-conviction tests; 40% refundability has age/support restrictions. LLC is nonrefundable and has its own expense/institution tests. No MFS; both phase out over $80,000–$90,000 MAGI ($160,000–$180,000 joint), with no double use of expenses or same-student AOTC/LLC. Obtain the required Form 1098-T or substantiate an allowed exception, and coordinate scholarships/other tax-free benefits. [Form 8863 instructions](https://www.irs.gov/instructions/i8863).

**Saver’s Credit:** age 18+, not a student and not claimed as a dependent; qualified contributions/elective deferrals after required distribution offsets, capped at $2,000 per spouse for the credit base. Use the full 2025 Form 8880 status/AGI 50%/20%/10% table and tax-liability limit; $47,500 joint is the end of the 50% band, and no credit above $79,000 joint. [2025 Form 8880](https://www.irs.gov/pub/irs-prior/f8880--2025.pdf).

## 13. Schedule 2 — Additional taxes

**Schedule 2 — Additional taxes**  _([Schedule 2](https://www.irs.gov/pub/irs-pdf/f1040s2.pdf))_

| Line | Item | Form |
| --- | --- | --- |
| 1a | Excess advance premium tax credit repayment | Form 8962 [2025 authority](https://www.irs.gov/pub/irs-pdf/f1040s2.pdf) |
| 2 | AMT | Form 6251 [2025 authority](https://www.irs.gov/pub/irs-pdf/f1040s2.pdf) |
| 4 | SE tax | Schedule SE — refer out [2025 authority](https://www.irs.gov/pub/irs-pdf/f1040s2.pdf) |
| 7 | Unreported SS/Medicare from Form 4137 / 8919 | [2025 authority](https://www.irs.gov/pub/irs-pdf/f1040s2.pdf) |
| 8 | Additional tax on IRAs (early withdrawal, RMD failure) | Form 5329 [2025 authority](https://www.irs.gov/pub/irs-pdf/f1040s2.pdf) |
| 9 | Household employment taxes | Schedule H [2025 authority](https://www.irs.gov/pub/irs-pdf/f1040s2.pdf) |
| 10 | Reserved for future use | [S2](https://www.irs.gov/pub/irs-pdf/f1040s2.pdf). |
| 11 | Additional Medicare Tax | Form 8959 [2025 authority](https://www.irs.gov/pub/irs-pdf/f1040s2.pdf) |
| 12 | Net Investment Income Tax | Form 8960 [2025 authority](https://www.irs.gov/pub/irs-pdf/f1040s2.pdf) |
| 13 | Uncollected Social Security/Medicare or RRTA tax on tips or group-term life insurance | [S2](https://www.irs.gov/pub/irs-pdf/f1040s2.pdf). |
| 14 | Interest on §453(l) deferred installment sale tax | [2025 authority](https://www.irs.gov/pub/irs-pdf/f1040s2.pdf) |
| 15 | Interest on deferred tax on certain installment sales with sales price over $150,000; apply section 453A separately | [2025 Schedule 2](https://www.irs.gov/pub/irs-pdf/f1040s2.pdf) |
| 16 | Recapture of low-income housing credit | Form 8611. [S2](https://www.irs.gov/pub/irs-pdf/f1040s2.pdf). |
| 17a-17z | Other additional taxes | [2025 authority](https://www.irs.gov/pub/irs-pdf/f1040s2.pdf) |
| 18–21 | Follow final Schedule 2 totals, including Form 4255 amounts; line 21 goes to Form 1040 line 23 | [2025 Schedule 2](https://www.irs.gov/pub/irs-pdf/f1040s2.pdf) |

## 14. Payments — Form 1040 Lines 25-33

**Payments — Form 1040 Lines 25-33**  _(Form 1040 Lines 25-33)_

| Line | Item |
| --- | --- |
| 25a | Federal income tax withheld from W-2 [2025 authority](https://www.irs.gov/instructions/i1040gi) |
| 25b | Federal income tax withheld from 1099 [2025 authority](https://www.irs.gov/instructions/i1040gi) |
| 25c | Other withholding (Form 8959, Form W-2G, Schedule K-1) [2025 authority](https://www.irs.gov/instructions/i1040gi) |
| 26 | 2025 estimated tax payments + prior year overpayment applied [2025 authority](https://www.irs.gov/instructions/i1040gi) |
| 27a | EITC [2025 authority](https://www.irs.gov/instructions/i1040gi) |
| 28 | Refundable Child Tax Credit / Additional CTC (Schedule 8812) [2025 authority](https://www.irs.gov/instructions/i1040gi) |
| 29 | American Opportunity Credit refundable portion (Form 8863 Line 8) [2025 authority](https://www.irs.gov/instructions/i1040gi) |
| 30 | Refundable adoption credit from Form 8839 line 13 [2025 authority](https://www.irs.gov/instructions/i1040gi) |
| 31 | Schedule 3 line 15 (other payments and refundable credits) [2025 authority](https://www.irs.gov/instructions/i1040gi) |
| 32 | Sum 27a, 28, 29, 30 and 31 [2025 authority](https://www.irs.gov/instructions/i1040gi) |
| 33 | Total payments = 25d + 26 + 32 [2025 authority](https://www.irs.gov/instructions/i1040gi) |

## 15. Estimated tax — §6654

Although primarily a freelancer concern (refer to `us-quarterly-estimated-tax`), W-2 taxpayers with material non-wage income (RSU vesting, large dividends, IRA conversions to Roth, year-end capital gains) may owe estimates.

- **Estimated-tax installments** — Generally test timely payments against 90% of current-year tax or 100% of prior-year tax; substitute 110% when prior AGI exceeds $150,000 ($75,000 if current filing status MFS). The prior return must cover 12 months. A qualifying US citizen/resident with no prior-year liability for a full year has a separate exception; farmers/fishers, uneven income and waivers need their own tests. A year-end refund does not prove installments were timely. [Form 2210 instructions](https://www.irs.gov/instructions/i2210).
- **Underpayment penalty computation** — Underpayment penalty computed on Form 2210. The "annualized income installment method" can reduce penalty when income is lumpy.  _(Form 2210)_
- **De minimis exception** — $1,000 USD (no penalty if tax owed after withholding and refundable credits is < $1,000)  _(§6654)_

## 16. Amended returns — Form 1040-X

### 16.1 Statute of limitations — §6511(a)

- **Refund claims** — The general filing limit is the later of three years after filing or two years after payment, but the recoverable amount also has payment-lookback limits. Early/deemed filing/payment and special-period rules matter. For an actual limitation deadline or carryback: Check this point with one of our partner accountants. [Form 1040-X instructions](https://www.irs.gov/instructions/i1040x).

### 16.2 When to amend

- **Amendment** — Correct omitted/misreported income, deductions or credits using Form 1040-X. Filing-status changes and any NOL/foreign-tax-credit carryback have separate statutory restrictions; an individual net capital loss is not a general carryback. Check this point with one of our partner accountants. [instructions](https://www.irs.gov/instructions/i1040x).

### 16.3 E-file

- **Amended-return e-file** — Check the IRS’s currently accepted years and the software provider’s support; there is no general requirement here to use the original software. Where unsupported, follow the paper filing instructions. [Form 1040-X instructions](https://www.irs.gov/instructions/i1040x).

## 17. Other operational items

### 17.1 IP PIN (Identity Protection PIN)

- **IP PIN** — A six-digit IRS identity-protection number valid for one calendar year; a new one is generated each year. Enter the current PIN if one was issued to the taxpayer/spouse/dependent; having a PIN is not a universal condition for e-filing. [IRS](https://www.irs.gov/identity-theft-fraud-scams/get-an-identity-protection-pin).

### 17.2 Direct deposit

- **Direct deposit** — Form 8888 permits splitting an eligible refund into up to three accounts. Validate ownership, routing and account details. [Form 8888](https://www.irs.gov/pub/irs-pdf/f8888.pdf).

### 17.3 Filing deadline

- **2025 return deadlines** — Generally April 15, 2026; a timely valid Form 4868 extends filing to October 15, 2026, not payment. Disaster, overseas, combat-zone and other relief can alter the actual deadline. For late-payment interest/penalties and relief: Check this point with one of our partner accountants. [2025 instructions](https://www.irs.gov/instructions/i1040gi).

### 17.4 E-file mandate

- **E-file mandate** — A specified tax-return preparer generally must e-file when reasonably expecting to file 11 or more covered income-tax returns for individuals, estates or trusts during the calendar year, subject to the written taxpayer paper-filing choice, hardship and other permitted exceptions. [EF](https://www.irs.gov/e-file-providers/frequently-asked-questions-e-file-requirements-for-specified-tax-return-preparers-sometimes-referred-to-as-the-e-file-mandate).

### 17.5 §183 hobby loss

- **Hobby/business classification** — Report activity-not-for-profit income on Schedule 1 line 8j; ordinary hobby expenses are not a Schedule C loss. Mixed-profit-motive facts, independent deductions, cost of goods sold and the regulatory factors need case analysis: Check this point with one of our partner accountants. [2025 instructions](https://www.irs.gov/instructions/i1040gi).

### 17.6 §469 passive activity losses

- **Rental real estate passive loss allowance** — The ordinary actively participating rental-real-estate allowance is up to $25,000, phased out over $100,000–$150,000 MAGI. MFS taxpayers living apart for the entire year have a maximum $12,500 allowance, phased out over $50,000–$75,000; MFS taxpayers living with their spouse at any time do not qualify for the allowance. Active participation also generally requires at least 10% ownership by value (including the spouse’s interest) throughout the year. Use the special rental MAGI definition, not unadjusted AGI. Suspended losses on disposition, death, gift or installment sale: Check this point with one of our partner accountants. [P925](https://www.irs.gov/publications/p925).

### 17.7 §461(l) excess business loss

- **Excess business losses (2025)** — Form 461 applies the $313,000 threshold ($626,000 joint) after the other loss limitations. This is not a deductible allowance for employee wages. For aggregation, disallowed-loss/NOL treatment and 2026 changes: Check this point with one of our partner accountants. [Rev. Proc.2024-40](https://www.irs.gov/pub/irs-drop/rp-24-40.pdf).

## 18. Common errors checklist

1. **SS taxable amount (Line 6b)** computed wrong — failed to use Pub 915 Worksheet 1; over- or understated tax-exempt interest in the formula. (See §4.6 Audit Flash.)
2. **Wrong tax computation method** — Follow the Qualified Dividends and Capital Gain Tax Worksheet where required; its ordinary-income tax step can itself require the Tax Table. Do not substitute continuous brackets merely because the worksheet is used. [I](https://www.irs.gov/instructions/i1040gi).
3. **Forgot Schedule B** — Test taxable interest over $1,500 and ordinary dividends over $1,500 separately, plus the other listed triggers and applicable Part III questions. [B](https://www.irs.gov/instructions/i1040sb).
4. **Excess Social Security tax** from two employers not credited on Schedule 3 Line 11.
5. **Capital loss carryover** not picked up from prior return (line 6 / Line 14 of Schedule D).
6. **Dependent claimed by both parents** post-divorce — Form 8332 release of claim or §152(e) custodial parent rule violated.
7. **Missing Form 8606** when rolled over after-tax 401(k) contributions to IRA, or made nondeductible IRA contributions — destroys basis tracking.
8. **NIIT** not computed when AGI > $200k/$250k and investment income present.
9. **Kiddie tax** Form 8615 missed for college student dependents with brokerage 1099-DIV.
10. **AMT** not run for ISO exercises.
11. **Standard deduction limitation** — Apply the dependent’s regular standard-deduction limit: for 2025, the greater of $1,350 or earned income + $450, capped at the regular standard deduction for the filing status ($15,750 for Single/MFS in 2025); any age/blindness additions require their separate conditions. [P501](https://www.irs.gov/publications/p501).
12. **Wrong filing status** — HoH claimed without a qualifying person; QSS claimed in year 3+ after spouse's death.
13. **Box 12 W-2 code DD** (employer-sponsored health coverage) mistakenly added to income — informational only.
14. **Scholarship/education-credit coordination** — Do not automatically add back the full scholarship; apply taxable-scholarship and no-double-benefit rules. Check this point with one of our partner accountants.
15. **Marketplace coverage** — Obtain Form 1095-A and determine Form 8962 reconciliation requirements; receiving a form alone is not the full eligibility analysis. [2025 instructions](https://www.irs.gov/instructions/i1040gi).

## 19. Worked examples — calendar 2025 only

These are synthetic conditional cases. All original numerical inputs are preserved. Assume the stated qualifying children/dividends/debt/charities/HSA and retirement amounts satisfy the detailed eligibility, documentation and income-base rules; no omitted item, international adjustment, wash sale, special tax or credit applies. For Medicare use the separately stated box 5 assumptions, not an inference from box 1. For a real return obtain the records and facts in the intake checklist first. All form labels and Tax Table cells below are 2025 only. [2025 instructions](https://www.irs.gov/instructions/i1040gi).

### 19.1 Example A — Single W-2 employee with brokerage

Sarah, single, age 34, lives in Texas (federal case; state tax is outside scope)
W-2 Box 1 wages: $95,000; Box 2 federal withholding: $12,400
1099-INT: $850 (Treasury bond fund)
1099-DIV: $3,200 ordinary, of which $2,800 qualified
1099-B sales: sold $40,000 of VTI held 18 months for $5,000 LTCG (basis $35,000); sold $8,000 of TSLA held 4 months for $1,200 STCG (basis $6,800)
401(k) contribution: $23,500 (already in W-2)
HSA contribution (outside payroll): $4,300
Roth IRA contribution: $7,000 (not deductible, no Form 8606)
Student loan interest paid: $1,800

- **Tax computation (Qualified Dividends and Capital Gain Tax Worksheet)** — Preserve all supplied income, contribution and withholding facts and assume eligible HSA/qualified-dividend treatment. Student-loan MAGI is $105,250 − $4,300 = $100,950, above the $100,000 single phaseout endpoint: no deduction for the $1,800 paid. AGI $100,950 less $15,750 gives taxable income $85,200. Ordinary portion = $85,200 − $5,000 LTCG − $2,800 qualified dividends = $77,400. The 2025 Single Tax Table row $77,400–$77,450 gives $11,948; add $7,800 × 15% = $1,170. Tax is $13,118; subtract $12,400 withholding: $718 owed. [I](https://www.irs.gov/instructions/i1040gi).

- **NIIT check Example A** — AGI $100,950 < $200k threshold — no NIIT  _(§1411)_

### 19.2 Example B — MFJ with kids, mortgage, HSA, large itemized

Marcus and Priya, MFJ, both age 41, California residents (refer to `ca-540-individual-return` for CA portion — this skill covers federal only)
Marcus W-2 wages: $185,000; withholding $32,000
Priya W-2 wages: $95,000; withholding $11,000
Combined Social Security wages exceed $176,100 only on Marcus alone (so no excess SS tax issue)
Two qualifying children: ages 8 and 11
Assume each spouse’s Medicare wages equal the stated W-2 wages; no Additional Medicare withholding.
Family HSA contribution: $8,550 (Priya's W-2 Box 12 W = $8,550 already pre-tax — so no Schedule 1 deduction)
Mortgage interest (1098): $24,000 on $620,000 acquisition debt originated 2020
Property tax: $14,000
CA state income tax withheld: $19,800
Charitable cash gifts to public charities: $9,500 (with substantiation)
401(k) contributions: Marcus $23,500, Priya $20,000 (already in W-2)
1099-DIV: $4,800 ordinary, $4,200 qualified
1099-INT: $1,400

AGI is $286,200; adjustments are zero because the HSA amount was already excluded through payroll.

**Schedule A — Itemized**  _([SALT authority §70120](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm))_

| Line | Item | Amount |
| --- | --- | --- |
| 5a | State income tax | $19,800 [2025 authority](https://www.irs.gov/instructions/i1040gi) |
| 5b | Property tax | $14,000 [2025 authority](https://www.irs.gov/instructions/i1040gi) |
| 5d | Sum | $33,800 [2025 authority](https://www.irs.gov/instructions/i1040gi) |
| 5e | SALT cap | min($33,800, $40,000) = $33,800 — **NO phaseout** since MAGI $286,200 < $500k threshold (§2.7) [2025 authority](https://www.irs.gov/instructions/i1040gi) |
| 7 | Total taxes | $33,800 [2025 authority](https://www.irs.gov/instructions/i1040gi) |
| 8a / 8e | Mortgage interest | $24,000 [2025 authority](https://www.irs.gov/instructions/i1040gi) |
| 10 | Total interest | $24,000 [2025 authority](https://www.irs.gov/instructions/i1040gi) |
| 11 | Charitable cash (≤ 60% AGI limit) | $9,500 [2025 authority](https://www.irs.gov/instructions/i1040gi) |
| 14 | Total charitable | $9,500 [2025 authority](https://www.irs.gov/instructions/i1040gi) |
| 17 | Total itemized | **$67,300** [2025 authority](https://www.irs.gov/instructions/i1040gi) |

- **Itemize vs standard decision** — Itemized ($67,300) > standard ($31,500) → itemize.  _(§63)_

- **Tax (Qualified Dividends and Capital Gain Worksheet)** — Taxable income is $286,200 − $67,300 = $218,900. Ordinary portion: $218,900 - $4,200 QDIV = $214,700; Tax on $214,700 MFJ (§1(j) brackets): 10% × $23,850 = $2,385; 12% × ($96,950 - $23,850) = $8,772; 22% × ($206,700 - $96,950) = $24,145; 24% × ($214,700 - $206,700) = $1,920; Subtotal = $37,222; Tax on $4,200 QDIV at 15% (ordinary income > $96,700 0% bracket): $630; Line 16 tax: ~$37,852  _(§1(j))_
- **Credits — Schedule 8812** — 2 qualifying children × $2,200 = $4,400 CTC; AGI $286,200 < $400,000 phaseout — full credit; Line 19: $4,400  _(§24)_
After CTC, regular tax is $33,452; additional taxes $506 give total $33,958. Withholding $43,000 gives a $9,042 refund.

- **NIIT check** — MAGI $286,200 vs $250,000 threshold → excess $36,200; NII = $1,400 + $4,800 = $6,200; NIIT = 3.8% × min($6,200, $36,200) = 3.8% × $6,200 = $236; Schedule 2 Line 12: $236  _(§1411)_
- **Additional Medicare Tax check** — Combined wages $280,000 vs $250,000 MFJ threshold → excess $30,000; 0.9% × $30,000 = $270; Marcus's Medicare wages alone ($185k) under the employer’s $200k withholding threshold so employer didn't withhold the 0.9% on his wages — full $270 owed; Schedule 2 Line 11: $270  _(Form 8959)_

### 19.3 Example C — Retiree with Social Security + RMD

Walter, single, age 73, widower (spouse died 2019 — no longer QSS), lives in Florida
Social Security: $32,000 gross (SSA-1099)
Traditional IRA RMD: $28,000 (1099-R)
Pension (1099-R, fully taxable): $14,000
1099-INT (bank): $600
1099-DIV: $3,500 ordinary, $3,200 qualified
1099-B: sold mutual fund LTCG $9,000 (basis $21,000, proceeds $30,000)
Assume no deductible IRA contribution after age 70½ reduces the QCD exclusion; the recipient is eligible and acknowledgment obtained.
QCD from IRA to local charity: $10,000 (part of the $28,000 RMD distribution — directly transferred by trustee)
Property tax: $4,800
Mortgage paid off — no mortgage interest
Charitable contributions other than QCD: $1,200 cash
Federal withholding: $4,200 from pension; $2,800 from IRA

- **SS taxable computation (2025 Social Security Benefits Worksheet)** — Provisional income = (AGI excl SS) + tax-exempt interest + 50% SS; AGI excl SS = ($28,000 - $10,000 QCD) + $14,000 + $600 + $3,500 + $9,000 = $45,100; Note: QCD reduces 4b; line 4a shows $28,000 and line 4c box 2 identifies QCD; the $10,000 QCD is excluded from gross income; Provisional income = $45,100 + 0 + ($32,000 × 0.5) = $61,100; Single thresholds: $25k first / $34k second; Above second threshold, so up to 85% taxable; Computation: lesser of (a) 85% × $32,000 = $27,200 or (b) 85% × ($61,100 - $34,000) + lesser of [$4,500 or 50% × $32,000 = $16,000] = $23,035 + $4,500 = $27,535; Taxable SS = min($27,200, $27,535) = $27,200  _(Pub 915 Worksheet 1)_

- **Standard deduction (single, age 65+)** — Base $15,750 + age 65+ addition $2,000 = $17,750. Separately, the OBBBA senior deduction: $6,000 on Schedule 1-A Part V, carried to Form 1040 line 13b (age 65+; MAGI $72,300 is under the $75,000 phase-out start)  _([Rev. Proc. 2024-40](https://www.irs.gov/pub/irs-pdf/f1040s1a.pdf))_
- **Itemize vs standard decision Example C** — Compare itemized: property tax $4,800 + charitable $1,200 = $6,000 — well below standard. Use standard.  _(§63)_

AGI is $72,300; total deductions $23,750 give taxable income $48,550.

- **Tax (Qualified Dividends and Capital Gain Tax Worksheet)** — Keep taxable income $48,550 and all supplied eligibility assumptions. Ordinary portion = $48,550 − $9,000 LTCG − $3,200 qualified dividends = $36,350. The 2025 Single Tax Table row $36,350–$36,400 gives $4,127. The first $12,000 of preferential income is in the 0% band; remaining $200 × 15% = $30. Tax = $4,157, giving a $2,843 refund on $7,000 withholding. [I](https://www.irs.gov/instructions/i1040gi).

- **NIIT and RMD checks Example C** — NIIT is zero below the $200,000 threshold. Keep the supplied $28,000 RMD input; independently obtain the prior-year balance/divisor and verify fulfillment rather than claiming the amount is proven by age. An eligible QCD counts toward the RMD. [Publication 590-B](https://www.irs.gov/publications/p590b).

### 19.4 Example D — Single W-2 employee, ISO exercise-and-hold (AMT)

Dana, single, age 38, lives in Georgia
W-2 Box 1 wages: $185,000 (already includes a $40,000 RSU vest reported in Box 14 — do NOT add the $40,000 again)
1099-INT: $244
1099-B sales: sold RSU lots for +$43,000 long-term and +$3,600 short-term capital gain
Medicare wages (W-2 box 5): $197,000 (a distinct supplied base, not derived from box 1).
ISO exercise-and-hold: exercised 4,000 incentive stock options (strike $3, FMV $28) and held them past year-end (did not sell)

**Return (Example D, Part 1 — regular tax)**  _(Example D regular-tax return)_

| Line | Item | Amount |
| --- | --- | --- |
| 1a | Wages (Box 1 as-is — $40,000 RSU already included; do not re-add) | $185,000 [2025 authority](https://www.irs.gov/instructions/i1040gi) |
| 2b | Taxable interest | $244 [2025 authority](https://www.irs.gov/instructions/i1040gi) |
| 7 | Capital gain (Schedule D: $43,000 LT + $3,600 ST) | $46,600 [2025 authority](https://www.irs.gov/instructions/i1040gi) |
| 9 | Total income | $231,844 [2025 authority](https://www.irs.gov/instructions/i1040gi) |
| 11 | AGI | $231,844 [2025 authority](https://www.irs.gov/instructions/i1040gi) |
| 12 | Standard deduction (single) | $15,750 [2025 authority](https://www.irs.gov/instructions/i1040gi) |
| 15 | Taxable income | $216,094 [2025 authority](https://www.irs.gov/instructions/i1040gi) |
| 16 | Regular tax (QDCGT worksheet) | $40,840 [2025 authority](https://www.irs.gov/instructions/i1040gi) |

- **Regular tax computation — Example D** — Ordinary income $173,094 (taxable income $216,094 − $43,000 net long-term capital gain) at 2025 single rates = $34,390; plus $43,000 LTCG × 15% = $6,450 → regular tax $40,840. The ISO exercise-and-hold adds ZERO regular-tax income: the $100,000 bargain element is invisible to the regular system and surfaces only in AMT (common error #10).  _(§1(j); §1(h))_

**Form 6251 (Example D — AMT)**  _([Example D Form 6251 AMT](https://www.irs.gov/pub/irs-pdf/f6251.pdf))_

| Line | Item | Amount |
| --- | --- | --- |
| 1a | Form 1040 line 14 minus Schedule 1-A line 37 (none in supplied facts) | $15,750 [2025 Form 6251](https://www.irs.gov/pub/irs-pdf/f6251.pdf) |
| 1b | Form 1040 line 11b ($231,844) minus line 1a ($15,750) | $216,094 [2025 Form 6251](https://www.irs.gov/pub/irs-pdf/f6251.pdf) |
| 2a | Standard deduction add-back | $15,750 [2025 authority](https://www.irs.gov/instructions/i1040gi) |
| 2i | ISO exercise adjustment — 4,000 × ($28 − $3), §56(b)(3) | $100,000  [2025 Form 6251](https://www.irs.gov/pub/irs-pdf/f6251.pdf) |
| 4 | AMTI | $331,844 [2025 authority](https://www.irs.gov/instructions/i1040gi) |
| 5 | AMT exemption (single $88,100; AMTI below $626,350 phaseout → full) | ($88,100) [2025 authority](https://www.irs.gov/instructions/i1040gi) |
| 6 | Base | $243,744 [2025 authority](https://www.irs.gov/instructions/i1040gi) |
| 7 | AMT computation before AMT foreign tax credit (none assumed) | $58,643  [2025 Form 6251](https://www.irs.gov/pub/irs-pdf/f6251.pdf) |
| 8 | AMT foreign tax credit (none in supplied facts) | $0  [2025 Form 6251](https://www.irs.gov/pub/irs-pdf/f6251.pdf) |
| 9 | Tentative minimum tax ($200,744 × 26% + $43,000 LTCG × 15%) | $58,643  [2025 Form 6251](https://www.irs.gov/pub/irs-pdf/f6251.pdf) |
| 10 | Regular tax | $40,840  [2025 Form 6251](https://www.irs.gov/pub/irs-pdf/f6251.pdf) |
| 11 | AMT — to Schedule 2, line 2 | $17,803  [2025 Form 6251](https://www.irs.gov/pub/irs-pdf/f6251.pdf) |

- **AMT result and credit — Example D** — The stated ISO exercise/hold produces AMT $17,803. Do not promise that the entire amount becomes a credit or is refunded when shares are sold. Form 8801 timing/exclusion and later-year limitations: Check this point with one of our partner accountants.
- **NIIT and Additional Medicare checks — Example D** — NIIT (§1411): AGI $231,844 > $200,000 → 3.8% × lesser of net investment income ($46,844) and MAGI over threshold ($31,844) = ~$1,210 — separate from AMT. Additional Medicare Tax (§3101(b)(2)): Medicare wages $197,000 < $200,000 → none.  _(§1411; §3101(b)(2))_

```oa-check
name: Example A, student-loan phaseout and final 2025 tax-table result
inputs:
  total_income: 105250
  eligible_hsa: 4300
  standard_deduction: 15750
  ltcg: 5000
  qualified_dividends: 2800
  ordinary_tax_table: 11948
  withholding: 12400
steps:
  student_loan_magi: total_income - eligible_hsa
  student_loan_deduction: 0
  agi: total_income - eligible_hsa - student_loan_deduction
  taxable_income: agi - standard_deduction
  ordinary_income: taxable_income - ltcg - qualified_dividends
  preferential_tax: (ltcg + qualified_dividends) * 0.15
  tax: ordinary_tax_table + preferential_tax
  owed: tax - withholding
expected:
  student_loan_magi: 100950
  agi: 100950
  taxable_income: 85200
  ordinary_income: 77400
  tax: 13118
  owed: 718
```

```oa-check
name: Example C, final 2025 tax-table ordinary portion
inputs:
  taxable_income: 48550
  ltcg: 9000
  qualified_dividends: 3200
  zero_rate_ceiling: 48350
  ordinary_tax_table: 4127
  withholding: 7000
steps:
  ordinary_income: taxable_income - ltcg - qualified_dividends
  preferential_income: ltcg + qualified_dividends
  zero_rate_income: min(preferential_income, max(0, zero_rate_ceiling - ordinary_income))
  preferential_tax: (preferential_income - zero_rate_income) * 0.15
  tax: ordinary_tax_table + preferential_tax
  refund: withholding - tax
expected:
  ordinary_income: 36350
  preferential_tax: 30
  tax: 4157
  refund: 2843
```

## Intake and completion controls

Obtain tax year, residence/citizenship, year-end marital and death/remarriage facts, household costs, each dependent’s relationship/age/student/residence/support/citizenship and competing claims; Forms W-2 (boxes 1, 2, 3, 4, 5, 6 and relevant box 12 codes), all 1099s, basis/carryovers, foreign account/trust facts, retirement basis/rollovers/QCD/RMD records, HSA coverage and contribution history, mortgage use/balance/origination/refinancing, taxes paid, charity documentation, credit-specific eligibility and payments. Screen dependent eligibility before claiming deductions; do not infer eligibility from a maximum amount.

Use final forms for the specified year. Reconcile the information returns and schedules, compute the tax/credit/payment totals, obtain the taxpayer’s review/signature and applicable e-file authorization, submit through authorized filing software, retain the acceptance or fix a rejection, and arrange any payment through [IRS Payments](https://www.irs.gov/payments). Scope/referral and professional-review steps here are workflow policy.

### Specialist boundaries retained

Dual-status/nonresident/expatriation, innocent spouse, foreign-account/asset/trust compliance, streamlined procedures, controversy, unusual pensions/rollovers, QSBS/NFT classification, home-sale exceptions, foreign tax-credit elections, adoption, loss dispositions/carrybacks and minimum-tax credits: **Check this point with one of our partner accountants.** This sentence is a referral, not confirmation that a credit or exclusion applies.

For written advice, apply the reasonable-facts/assumptions and relevant-authority standards of [Circular 230 §10.37](https://www.irs.gov/pub/irs-pdf/pcir230.pdf). The preserved approval metadata records its original approval; it is not a fresh human approval of this edit.

## Sources

Read on 2026-11-26: the operative sections/table cells listed below, not every page of each publication. Earlier unchanged readings and review receipts were reused for applicability; missing quotations were recovered from official text. Generic forms were checked for their printed year; Form8880 uses the archived2025 URL because the generic file now shows2026. Synthetic cases remain conditional.

Not yet confirmed: no unverified proposition is retained as usable guidance. Specialist topics use the explicit partner-accountant referral. Final2026 form mappings are outside this guide.

| Source and scope read | Official URL | Read date |
| --- | --- | --- |
| AMT: Operative form fields/instruction sections quoted in the claims ledger | [official text](https://www.irs.gov/pub/irs-pdf/f6251.pdf) | 2026-11-26 |
| B: Operative form fields/instruction sections quoted in the claims ledger | [official text](https://www.irs.gov/instructions/i1040sb) | 2026-11-26 |
| C230raw: Section10.37 written-advice requirements; PDF raw extraction | [official text](https://www.irs.gov/pub/irs-pdf/pcir230.pdf) | 2026-11-26 |
| CARE: Operative form fields/instruction sections quoted in the claims ledger | [official text](https://www.irs.gov/instructions/i2441) | 2026-11-26 |
| CODE108: Operative form fields/instruction sections quoted in the claims ledger | [official text](https://uscode.house.gov/us/usc/119-124/t26/s108/) | 2026-11-26 |
| CTC: Operative form fields/instruction sections quoted in the claims ledger | [official text](https://www.irs.gov/instructions/i1040s8) | 2026-11-26 |
| EDUC: Operative form fields/instruction sections quoted in the claims ledger | [official text](https://www.irs.gov/instructions/i8863) | 2026-11-26 |
| EF: Operative form fields/instruction sections quoted in the claims ledger | [official text](https://www.irs.gov/e-file-providers/frequently-asked-questions-e-file-requirements-for-specified-tax-return-preparers-sometimes-referred-to-as-the-e-file-mandate) | 2026-11-26 |
| ELECT: Operative form fields/instruction sections quoted in the claims ledger | [official text](https://www.irs.gov/instructions/i8814) | 2026-11-26 |
| EST: Operative form fields/instruction sections quoted in the claims ledger | [official text](https://www.irs.gov/instructions/i2210) | 2026-11-26 |
| EV: Operative form fields/instruction sections quoted in the claims ledger | [official text](https://www.irs.gov/instructions/i8936) | 2026-11-26 |
| F: Operative form fields/instruction sections quoted in the claims ledger | [official text](https://www.irs.gov/pub/irs-pdf/f1040.pdf) | 2026-11-26 |
| F8949: Operative form fields/instruction sections quoted in the claims ledger | [official text](https://www.irs.gov/instructions/i8949) | 2026-11-26 |
| FBAR: Operative form fields/instruction sections quoted in the claims ledger | [official text](https://www.fincen.gov/report-foreign-bank-and-financial-accounts) | 2026-11-26 |
| FCARE: Operative form fields/instruction sections quoted in the claims ledger | [official text](https://www.irs.gov/pub/irs-pdf/f2441.pdf) | 2026-11-26 |
| I: 2025 income/status/adjustment, Social Security, capital-gain, tax computation, EIC, filing and payment sections; two Tax Table cells | [official text](https://www.irs.gov/instructions/i1040gi) | 2026-11-26 |
| IA: Operative form fields/instruction sections quoted in the claims ledger | [official text](https://www.irs.gov/instructions/i1040sca) | 2026-11-26 |
| IAMT: Operative form fields/instruction sections quoted in the claims ledger | [official text](https://www.irs.gov/instructions/i6251) | 2026-11-26 |
| KID: Operative form fields/instruction sections quoted in the claims ledger | [official text](https://www.irs.gov/instructions/i8615) | 2026-11-26 |
| LAW: Operative sections 70103–70111, 70114, 70120, 70405, 70425 and 70501–70506; limited to claims quoted here | [official text](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) | 2026-11-26 |
| MED: Operative form fields/instruction sections quoted in the claims ledger | [official text](https://www.irs.gov/instructions/i8959) | 2026-11-26 |
| NII: Operative form fields/instruction sections quoted in the claims ledger | [official text](https://www.irs.gov/instructions/i8960) | 2026-11-26 |
| P501: 2025 marital/household/dependency rules and Tables6–8; senior deduction | [official text](https://www.irs.gov/publications/p501) | 2026-11-26 |
| P526: Charity recipient/property limits, ordering, carryovers,8283/appraisal rules | [official text](https://www.irs.gov/publications/p526) | 2026-11-26 |
| P547: Federal/qualified disaster categories and deduction floors | [official text](https://www.irs.gov/publications/p547) | 2026-11-26 |
| P550: Interest/dividend,holding period,wash-sale,capital-loss and preferential-rate sections | [official text](https://www.irs.gov/publications/p550) | 2026-11-26 |
| P590A: IRA contributions, coverage and phaseout tables,2026 changes | [official text](https://www.irs.gov/publications/p590a) | 2026-11-26 |
| P590B: QCD/Roth/RMD operative sections | [official text](https://www.irs.gov/publications/p590b) | 2026-11-26 |
| P925: Active rental participation,ownership and special MAGI/allowance | [official text](https://www.irs.gov/publications/p925) | 2026-11-26 |
| P969: HSA eligibility,contributions,catch-up and last-month tests | [official text](https://www.irs.gov/publications/p969) | 2026-11-26 |
| PIN: Operative form fields/instruction sections quoted in the claims ledger | [official text](https://www.irs.gov/identity-theft-fraud-scams/get-an-identity-protection-pin) | 2026-11-26 |
| QBI: Operative form fields/instruction sections quoted in the claims ledger | [official text](https://www.irs.gov/instructions/i8995) | 2026-11-26 |
| REF: Operative form fields/instruction sections quoted in the claims ledger | [official text](https://www.irs.gov/pub/irs-pdf/f8888.pdf) | 2026-11-26 |
| RET26: 2026 IRA contribution/phaseout provisions; resolves typographic Roth ceiling in Publication590-A | [official text](https://www.irs.gov/pub/irs-drop/n-25-67.pdf) | 2026-11-26 |
| RP24: 2025 ordinary/preferential tables, student-loan, EITC and loss thresholds | [official text](https://www.irs.gov/pub/irs-drop/rp-24-40.pdf) | 2026-11-26 |
| RP25: 2026 ordinary/preferential tables, AMT, standard/dependent, CTC and student-loan figures | [official text](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) | 2026-11-26 |
| RP26HSA: Operative form fields/instruction sections quoted in the claims ledger | [official text](https://www.irs.gov/pub/irs-drop/rp-25-19.pdf) | 2026-11-26 |
| S1: Operative form fields/instruction sections quoted in the claims ledger | [official text](https://www.irs.gov/pub/irs-pdf/f1040s1.pdf) | 2026-11-26 |
| S2: Operative form fields/instruction sections quoted in the claims ledger | [official text](https://www.irs.gov/pub/irs-pdf/f1040s2.pdf) | 2026-11-26 |
| S3: Operative form fields/instruction sections quoted in the claims ledger | [official text](https://www.irs.gov/pub/irs-pdf/f1040s3.pdf) | 2026-11-26 |
| SAVE25: Operative form fields/instruction sections quoted in the claims ledger | [official text](https://www.irs.gov/pub/irs-prior/f8880--2025.pdf) | 2026-11-26 |
| X: Operative form fields/instruction sections quoted in the claims ledger | [official text](https://www.irs.gov/instructions/i1040x) | 2026-11-26 |
