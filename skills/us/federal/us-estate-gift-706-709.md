---
name: us-estate-gift-706-709
description: Compute US federal estate and gift tax for 2026 on Forms 706 and 709, with separate GST allocation, gift splitting, direct payments, 529 elections, marital deductions and portability. Preserve historical 2025 cases and hold unsupported specialist outcomes. Trigger on estate tax, gift tax, Form 706, Form 709, DSUE, portability or GST tax. Federal only.
version: "1.2"
jurisdiction: US
tax_year: 2026
last_updated: 2026-11-27
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: estate-wealth-tax
type: computation
---

# US estate, gift and generation-skipping transfer tax (Forms 706 and 709), 2026

For 2026, the basic exclusion amount (BEA) is USD 15,000,000 and the basic credit is USD 5,945,800. Estate and gift tax share the credit; GST has its own USD 15,000,000 exemption and allocation history. An asset value alone does not establish tax payable or a filing exemption. [2010](https://uscode.house.gov/us/usc/t26/s2010/); [2505](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleB-chap12-subchapA-sec2505.htm); [2631](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleB-chap13-subchapD-sec2631.htm).

## Scope and who this is for

US citizens and US-domiciled individuals dying or making gifts in 2026. Establish transfer-tax domicile separately from income-tax residence. Use `us-tax-workflow-base` for preparation workflow. Produce a reviewer brief and draft forms for a Circular 230 practitioner. This limited written guidance under Circular 230 section 10.37 requires verified facts and practitioner sign-off before filing. Missing facts stop the affected computation; do not assume citizenship, trust classification, a discount or an election.

## Ask the client first

Collect death/gift dates; citizenship/domicile; spouse and marriage history; every prior Form 709 and DSUE election; assets, ownership, basis and appraisals; will/trust instruments; insurance ownership, beneficiary and Form 712; retained benefits/powers and recent transfers; expenses/debts; donee and present-interest evidence; signed consents; 529 contributions; GST history/elections; and state domicile/property locations. Reconcile available records before asking for missing information.

## Rates, bands and thresholds

| Item and conditions | Amount | Source |
| --- | --- | --- |
| BEA for 2026 deaths/gifts; indexing after 2026 using 2025 base, nearest USD 10,000; no scheduled 2026 sunset | USD 15,000,000 | [2010(c)(3)](https://uscode.house.gov/us/usc/t26/s2010/); [P.L. 119-21 section 70106](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| 2026 basic credit (computed), before DSUE/restored exclusion or pre-1977 adjustment | USD 5,945,800 = 345,800 + (15,000,000 − 1,000,000) × 40% | [2001(c)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleB-chap11-subchapA-partI-sec2001.htm); [2010(c)(1)](https://uscode.house.gov/us/usc/t26/s2010/) |
| Tentative tax for a base above USD 1,000,000; lower bases use the full statutory table | USD 345,800 + 40% of excess over USD 1,000,000 | [2001(c)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleB-chap11-subchapA-partI-sec2001.htm) |
| 2026 annual exclusion, per donor/donee, present interests | USD 19,000 | [Rev. Proc. 2025-32 section 4.42(1)](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| 2026 non-citizen spouse: present interests otherwise marital-deductible but for citizenship; replaces ordinary annual exclusion | USD 194,000 | [2523(i)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleB-chap12-subchapC-sec2523.htm); [Rev. Proc. 2025-32 section 4.42(2)](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Separate GST exemption; DSUE does not increase it | USD 15,000,000 | [2631(c)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleB-chap13-subchapD-sec2631.htm); [Rev. Proc. 2025-32 section 2.14](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| GST applicable rate | 40% × inclusion ratio | [2641](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleB-chap13-subchapE-sec2641.htm); [2001(c)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleB-chap11-subchapA-partI-sec2001.htm) |
| Historical 2025 BEA / annual exclusion / non-citizen spouse exclusion, only for qualifying 2025 transfers | USD 13,990,000 / USD 19,000 / USD 190,000 | [Rev. Proc. 2024-40 sections 2.41, 2.43](https://www.irs.gov/pub/irs-drop/rp-24-40.pdf) |

## The method, step by step

### 1. Filing tests and gifts

**Form 706:** add date-of-death gross estate, post-1976 adjusted taxable gifts and former section 2521 specific exemption allowed for gifts after 8 September 1976. The 2026 threshold is more than USD 15,000,000; deductions/DSUE do not raise it. Below the threshold, a return is still needed to elect portability. [6018(a)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap61-subchapA-partII-subpartC-sec6018.htm); [2010(c)(5)](https://uscode.house.gov/us/usc/t26/s2010/).

**Form 709:** section 6019 requires a return except for its qualifying annual/direct-payment exclusions, deductible marital transfers and specified charitable transfers. Future interests do not obtain the ordinary annual exclusion; elections may require a return even without tax (splitting, gift QTIP, 529). A trust gift is not automatically a future interest: section 2503(c) has a minor-transfer exception. [6019](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap61-subchapA-partII-subpartC-sec6019.htm); [2503(b),(c)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleB-chap12-subchapA-sec2503.htm); [2025 instructions, Who Must File](https://www.irs.gov/instructions/i709). Trust withdrawal/minor-trust qualification and disputed completion dates are held. Check this point with one of our partner accountants.

**Direct payments:** qualifying tuition paid directly to the educational organization and medical care paid directly to the provider have no dollar cap. Tuition excludes books, supplies, room and board; medical insurance qualifies, but insurance-reimbursed care does not. Payment to the beneficiary does not qualify for this exclusion. [2503(e)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleB-chap12-subchapA-sec2503.htm); [Reg. 25.2503-6(b)](https://www.ecfr.gov/current/title-26/section-25.2503-6).

**Spousal gifts:** qualifying outright gifts to a US-citizen spouse receive the marital deduction; terminable interests need an exception/election. The non-citizen exclusion above applies only on its stated conditions. [2523(a),(b),(f),(i)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleB-chap12-subchapC-sec2523.htm).

**Gift splitting:** each spouse must be a citizen or resident at the gift, married to the other then, and not remarry in the rest of the year. Both consent to all eligible third-party gifts while married that year; each reports half. This does not transfer BEA between spouses. A general power of appointment created in the spouse prevents splitting; gifts partly benefiting the spouse need an ascertainable third-party interest. Do not elect merely because property is jointly owned. Two qualifying 2026 annual exclusions total USD 38,000 per donee. [2513](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleB-chap12-subchapB-sec2513.htm); [2025 Part III instructions](https://www.irs.gov/instructions/i709).

Each spouse generally files separately. The 2025 layout uses Part III lines 1–7 and a signed, dated Notice of Consent. One return suffices if either only one spouse made gifts, all present interests and no donee received over USD 38,000; or only the donor gave above USD 19,000 and up to USD 38,000 per donee, the other gave no more than USD 19,000 to different donees, and all gifts were present interests. Consent cannot be signified after 15 April following the gift year unless neither spouse filed by that date; in that event it must be on the first gift return either files. Consent cannot follow a gift-tax deficiency notice sent to either spouse; do not backdate it. These thresholds also equal the 2026 exclusions; 2026 form placement is held until read. [Part III and both exceptions](https://www.irs.gov/instructions/i709).

**529:** an election spreads contributions over five years starting in the contribution year. USD 95,000 is five times the 2026 annual exclusion; USD 190,000 needs both donors' elections, with splitting applied first where used. File in the election year; later years without another filing trigger need no return solely for that fifth. Other gifts use any remaining exclusion: smaller allocations or later increased exclusions may leave room. Death within five years includes the part allocable after death. [529(c)(2),(4)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapF-partVIII-sec529.htm); [2025 Schedule A line B](https://www.irs.gov/instructions/i709).

Reconcile Schedule A gifts, Schedule B history, Schedule C DSUE and Schedule D GST before Part II. Gift tax is tentative tax on cumulative gifts including this year minus tentative tax on prior gifts, at section 2001(c) rates, then less available section 2505 credit, limited to tax. Do not subtract the full credit anew each year. [2502(a)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleB-chap12-subchapA-sec2502.htm); [2505](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleB-chap12-subchapA-sec2505.htm).

### 2. Gross estate to net tax

Reconcile includible assets to Schedules A–I and Part V: A real estate, B stocks/bonds, C mortgages/notes/cash, D insurance, E joint property, F miscellaneous, G lifetime transfers, H powers, I annuities. Inclusion must be established, not inferred from a list of owned assets. Special-use valuation now uses **Schedule T**, formerly A-1. [2026 instructions, schedule redesign and Part V](https://www.irs.gov/instructions/i706).

Use only allowable deductions/exclusions. Map J funeral/administration, K debts/mortgages, L losses/other administration, M spouse, O charity; U is the conservation-easement exclusion. State death tax deductions go on Part II line 3b. Labels do not establish deductibility. Retained interests, insurance transfers, joint contributions, appraisals and unsupported deductions are held for professional analysis. [2026 Part V and Part II line 3b](https://www.irs.gov/instructions/i706).

Section 2001(b) computes tentative tax on taxable estate plus adjusted taxable gifts, less gift tax that would have been payable on post-1976 gifts under the prescribed death-year rates. Adjusted taxable gifts exclude gifts already in the gross estate. Apply section 2010 credit, then substantiated other credits and separately computed GST. Restored exclusion, pre-1977 adjustments, foreign death/prior-transfer credits (P/Q), protective refund claim (PC), conservation easements (U) and payment deferrals need their own supported computation; missing records do not justify an assumed zero. [2001(b),(g)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleB-chap11-subchapA-partI-sec2001.htm); [2010](https://uscode.house.gov/us/usc/t26/s2010/); [2026 Part II](https://www.irs.gov/instructions/i706).

**Marital:** only included value passing to the surviving spouse is potentially deductible; terminable-interest restrictions apply. QTIP needs an election, qualifying income for life payable at least annually, and no power to appoint to anyone else during the spouse's life. Non-citizen spouse treatment is held for QDOT/treaty advice; it is not invariably denied without a QDOT because section 2056(d)(4) has a citizenship/residence exception. [2056(a),(b)(7),(d)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleB-chap11-subchapA-partIV-sec2056.htm). QTIP survivor inclusion and QDOT drafting/security/tax: Check this point with one of our partner accountants.

**Charity:** apply section 2055 recipient/use tests, reduce for death taxes borne by the bequest and cap at included value. Do not substitute the income-tax domestic-charity test. Split-interest charitable trusts/actuarial valuation are held. [2055(a),(c)–(e)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleB-chap11-subchapA-partIV-sec2055.htm). Check this point with one of our partner accountants.

### 3. Portability

Applicable exclusion is BEA plus valid DSUE from the last deceased spouse. DSUE is the lesser of the deceased spouse's BEA and that spouse's applicable exclusion minus (taxable estate plus adjusted taxable gifts). It is not a new indexed BEA for the survivor. Preserve records: IRS may examine DSUE after the ordinary assessment period. Multiple spouses, DSUE already used on gifts and restored exclusion need separate reconciliation. [2010(c)(2),(4),(5)](https://uscode.house.gov/us/usc/t26/s2010/).

A timely complete, properly prepared Form 706 elects portability unless the executor opts out. Deadline is nine months after death or the obtained extension. Simplified valuation is limited to nonrequired estates and eligible marital/charitable property: not where value affects other beneficiaries, determines other tax eligibility/elections, an interest is only partly deductible, or there is a partial disclaimer/QTIP election. Due-diligence estimates still enter the total. [Reg. 20.2010-2(a)(1),(2),(7)](https://www.ecfr.gov/current/title-26/section-20.2010-2).

Rev. Proc. 2022-32 covers a US citizen/resident dying after 2010, survived by a spouse, with no section 6018 filing duty and no timely estate return. The authorized executor files a complete, properly prepared Form 706 by the fifth anniversary and marks it “FILED PURSUANT TO REV. PROC. 2022-32 TO ELECT PORTABILITY UNDER § 2010(c)(5)(A).” A timely opt-out is not cured; discovery of a statutory filing duty voids relief. The survivor need not still be alive: the survivor's estate may benefit. Refund limitation periods do not extend. [Sections 3–5](https://www.irs.gov/pub/irs-drop/rp-22-32.pdf). Outside these conditions: Check this point with one of our partner accountants.

### 4. Valuation and deferrals

Section 2032 applies to all gross-estate property: disposals within six months use disposal-date value; retained assets use six-month value; lapse-of-time interests have their special rule. Both gross-estate value and combined estate/GST tax after credits must decrease. Elect on the last return filed by the extended due date, or the first late return filed within one year after that due date. An election may be revoked on a subsequent return filed by the extended due date; afterward it is irrevocable. Reconcile related deductions under section 2032(b), avoiding any duplicate benefit from alternate valuation. Basis follows a valid alternate value. [2032(a)–(d)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleB-chap11-subchapA-partIII-sec2032.htm); [Reg. 20.2032-1(b)](https://www.ecfr.gov/current/title-26/section-20.2032-1); [1014(a)(2)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapO-partII-sec1014.htm).

Section 6166 is an issue-spotting gateway: the included qualifying closely held business interest must exceed 35% of adjusted gross estate, and deferrable tax is proportionately limited. Up to ten installments, first no more than five years after the original payment date, are subject to statutory special rules. Business/passive-asset qualification, interest, acceleration, elections and bonds/liens are **non-usable holds** here. [6166(a),(b)](https://uscode.house.gov/us/usc/t26/s6166/). Check this point with one of our partner accountants.

Section 2032A special use, qualified heirs/recapture, section 6161 payment extensions and section 6163 remainder/reversion deferral: **non-usable holds**, including eligibility inferred from a cap alone. Check this point with one of our partner accountants.

### 5. GST

A skip person is a natural person at least two generations below the transferor or a trust satisfying section 2613's all-skip-interest/no-nonskip-distribution tests. Assign generations under section 2651, including spouse/adoption rules; not every grandchild automatically qualifies. Non-lineal age assignments and deceased-parent/collateral-heir exceptions are held for case analysis. [2613](https://uscode.house.gov/us/usc/t26/s2613/); [2651](https://uscode.house.gov/us/usc/t26/s2651/). Check this point with one of our partner accountants.

| Transfer to investigate | Route, subject to classification | Source |
| --- | --- | --- |
| Lifetime direct skip | Form 709 Schedule A Part 2 and Schedule D | [2025 instructions](https://www.irs.gov/instructions/i709) |
| Direct skip at death | Form 706 Schedules R/R-1 as applicable | [2026 instructions](https://www.irs.gov/instructions/i706) |
| Taxable distribution / termination | Forms 706-GS(D), 706-GS(D-1) / 706-GS(T); preparation held for specialist classification | [2025 instructions, GST transfers](https://www.irs.gov/instructions/i709) |

The separate GST exemption is allocated by individual/executor; allocations are irrevocable and DSUE does not augment it. Lifetime direct skips and indirect skips to a statutory GST trust receive unused exemption automatically unless a valid election changes treatment. Non-filing does not prevent allocation; apply every statutory GST-trust exception. [2631](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleB-chap13-subchapD-sec2631.htm); [2632(b),(c)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleB-chap13-subchapD-sec2632.htm).

For an ordinary initial transfer, inclusion ratio is the excess, if any, of one over the applicable fraction: allocated exemption divided by transferred value less estate/state death tax actually recovered from the trust and the relevant charitable deduction. Zero ratio means no GST at that ratio; otherwise applicable rate is 40% times ratio. Additional contributions, late allocations and special trusts need recomputation; an old allocation does not freeze every later ratio. [2642(a),(d),(e)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleB-chap13-subchapE-sec2642.htm); [2641](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleB-chap13-subchapE-sec2641.htm).

An ETIP generally defers allocation if immediate death would include the property, **other than solely by section 2035**, subject to regulatory exceptions/spouse coordination. Late-allocation timing/valuation, ETIP applications, reverse QTIP and missed-allocation relief are held. [2642(f),(g)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleB-chap13-subchapE-sec2642.htm). Check this point with one of our partner accountants.

### 6. Basis and reporting

Section 1014 generally uses death-date FMV or valid alternate/special-use value, potentially stepping down. IRD is excluded; conservation-easement property has a carryover exception. Both community-property halves adjust only if at least half the community interest is included. Appreciated property gifted to the decedent within one year and returning to donor/spouse has a carryback exception. Do not promise a step-up on every gross-estate asset. [1014(a)–(f)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapO-partII-sec1014.htm). IRD, retirement distributions and section 691(c) go to `us-form-1041-trust-and-estate-income`.

Ordinary gifts generally retain donor basis for gain and use gift-date FMV for loss when lower; post-1976 gift-tax basis increases relate to net appreciation. Spousal section 1041 transfers have their own rule. Actual estate/income tax outcomes decide gift-versus-hold planning. [1015(a),(d),(e)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapO-partII-sec1015.htm).

Form 8971 applies to required section 6018 returns filed after July 2015, not solely portability/GST/protective returns without statutory filing duty. File separately by the earlier of 30 days after the required estate-return date with extensions or 30 days after actual filing. Required Schedules A for property already acquired accompany that filing and go to those beneficiaries by the same deadline. For later-acquired property, the required statement and supplemental return are due by 31 January following acquisition, unless already reported under the permitted early-statement rule; beneficiary/property exceptions and other supplementation still apply. Reporting is distinct from section 1014(f)'s narrower tax-increasing-property cap. [Reg. 1.6035-1(b)](https://www.ecfr.gov/current/title-26/section-1.6035-1); [August 2025 instructions](https://www.irs.gov/pub/irs-prior/i8971--2025.pdf); [1014(f)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapO-partII-sec1014.htm).

## Worked cases

Cases assume stated allowable deductions, no unmentioned credits, pre-1977 adjustment, restored exclusion or GST liability. Arithmetic is not an appraisal/trust opinion.

### Case 1. Single decedent, 2026

Original inputs: unmarried, taxable estate USD 16,500,000; adjusted taxable gifts USD 1,000,000; no gift tax paid (assume none payable for this computation); BEA USD 15,000,000. Base USD 17,500,000; tentative tax USD 6,945,800; credit USD 5,945,800; estate tax USD 1,000,000. [2001](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleB-chap11-subchapA-partI-sec2001.htm); [2010](https://uscode.house.gov/us/usc/t26/s2010/).

```oa-check
name: Single decedent, taxable estate plus prior gifts above the 2026 BEA
inputs:
  taxable_estate: 16500000
  adjusted_taxable_gifts: 1000000
  bea: 15000000
steps:
  - tax_base: taxable_estate + adjusted_taxable_gifts
  - tentative_tax: 345800 + (tax_base - 1000000) * 0.40
  - applicable_credit: 345800 + (bea - 1000000) * 0.40
  - net_estate_tax: max(tentative_tax - applicable_credit, 0)
expected:
  tax_base: 17500000
  tentative_tax: 6945800.00
  applicable_credit: 5945800.00
  net_estate_tax: 1000000.00
```

### Case 2. Portability decision, 2026

First estate USD 4,000,000 entirely to US-citizen spouse, taxable estate nil, prior taxable gifts USD 500,000; survivor's estate USD 22,000,000; assumed return cost USD 25,000. Hold BEA at USD 15,000,000, indexing ignored; assume no inherited DSUE/prior survivor gifts. DSUE USD 14,500,000; survivor AEA USD 29,500,000; tax without portability USD 2,800,000, with it nil. Saving exceeds assumed cost: elect, subject to actual facts/deadlines and all late-relief conditions above if needed. [2010](https://uscode.house.gov/us/usc/t26/s2010/); [Rev. Proc. 2022-32](https://www.irs.gov/pub/irs-drop/rp-22-32.pdf).

```oa-check
name: Portability decision, 2026 death, survivor estate 22 million
inputs:
  bea: 15000000
  first_taxable_estate: 0
  first_adjusted_gifts: 500000
  survivor_estate: 22000000
  return_cost: 25000
steps:
  - dsue: min(bea, bea - (first_taxable_estate + first_adjusted_gifts))
  - tax_without: max(survivor_estate - bea, 0) * 0.40
  - tax_with: max(survivor_estate - bea - dsue, 0) * 0.40
  - saving: tax_without - tax_with
  - elect: min(max(saving - return_cost, 0), 1)
expected:
  dsue: 14500000
  tax_without: 2800000.00
  tax_with: 0.00
  saving: 2800000.00
  elect: 1
```

### Historical Case 14.1. USD 5 million estate, 2025

D dies in 2025, estate USD 5,000,000 all outright to S, no prior gifts. Conditional on US-citizen S/full marital deduction, taxable estate/tax are zero; DSUE USD 13,990,000 with valid election. No statutory threshold filing duty on these inputs, but portability needs a return. Combined 2025 exclusion USD 27,980,000; 2026 exclusion USD 28,990,000 if DSUE remains available. Former sunset urgency is withdrawn. [2025 BEA](https://www.irs.gov/pub/irs-drop/rp-24-40.pdf); [2010](https://uscode.house.gov/us/usc/t26/s2010/); [2056](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleB-chap11-subchapA-partIV-sec2056.htm).

```oa-check
name: Historical 2025 portability retains the original year
inputs:
  estate: 5000000
  marital_deduction: 5000000
  bea_2025: 13990000
  survivor_bea_2026: 15000000
steps:
  - taxable_estate: estate - marital_deduction
  - dsue: bea_2025 - taxable_estate
  - combined_2025: bea_2025 + dsue
  - combined_2026: survivor_bea_2026 + dsue
expected:
  taxable_estate: 0
  dsue: 13990000
  combined_2025: 27980000
  combined_2026: 28990000
```

### Historical Case 14.2. USD 20 million estate, 2025 : outcome held

Preserve US-citizen S, three adult children, 2018 taxable gift USD 500,000; will gives USD 13,990,000 to bypass trust for S for life/remainder children, residue to S. Asset inputs: joint residence USD 3,000,000; separate brokerage USD 9,000,000; IRA payable to S USD 4,000,000; insurance payable to estate USD 2,000,000; personal effects/autos USD 500,000; 50% family real-estate LLC interest valued USD 1,500,000. Listed total USD 20,000,000; expenses USD 200,000; mortgage USD 400,000.

**Non-usable hold:** establish whole-versus-included residence value, allowable expense/debt allocation, probate/non-probate funding and actual bypass formula. Withdraw old USD 5,910,000 marital deduction and nil-tax conclusion. Arithmetic: 20,000,000 − 200,000 − 400,000 − 13,990,000 = 5,410,000, not 5,910,000. Conversely the old deduction implies taxable estate 13,490,000, conflicting with the fixed 13,990,000 bypass gift. Neither settles funding/tax. No assumed LLC discount, ILIT exclusion or GST allocation is usable. Check this point with one of our partner accountants.

### Historical Case 14.3. Reciprocal SLATs, November 2025 : outcome held

Preserve H/W ages 65/63, healthy US citizens, USD 30,000,000 roughly half each, no prior gifts, three children/six grandchildren. Each proposes USD 13,000,000 separate assets to a SLAT benefiting spouse/descendants; annual exclusions ignored. Other inputs: USD 3,000,000 basis per contribution; 6% growth for 20 years; assumed death in 2045 at age 85; New York domicile as an unresolved example.

**Non-usable hold:** instruments/legal review must settle completion, reciprocal trusts/retained benefits, value, GST, splitting and filing dates. No permanent exclusion of USD 26,000,000 or growth is assured. Arithmetic only: retained assets 30,000,000 − 26,000,000 = 4,000,000; growth 26,000,000 × 1.06^20 = 83,385,522.28; built-in gain per contribution 10,000,000. The old tentative tax 4,989,800 was wrong: the statutory formula gives 5,145,800 on 13,000,000. Conditional credit headroom 13,990,000 − 13,000,000 = 990,000 is not an approved transaction outcome. Withdraw USD 25–30 million estate-saving and USD 2.4 million income-tax-cost promises; no scheduled sunset justifies rushing. Check this point with one of our partner accountants.

## When to refuse or refer

Each held outcome below is non-usable; do not fill it with remembered figures/defaults.

| Topic retained from current/historical coverage | Destination/action |
| --- | --- |
| T.D. 9884/Reg. 20.2010-1(c) anti-clawback; original USD 13,000,000 gift in 2025 / hypothetical USD 7,000,000 later BEA (historically 2027) | Preserve difference 6,000,000 and total 13,000,000 only; future-law input is not an enacted sunset. Protection/credit computation held. Check this point with one of our partner accountants. |
| REG-118913-21, former 5% exception, proposed-rule finalization/effectiveness | No operative conclusion retained. Check this point with one of our partner accountants. |
| SLAT, dynasty trust, IDGT sale, GRAT, QPRT, CLAT; reciprocal trust, ETIP, section 7520/1274 rates, divorce/liquidity/state planning | Mechanisms, rates, inclusion outcomes and discounts held. Check this point with one of our partner accountants. |
| Nonresident noncitizen situs, credits, treaties, Forms 706-NA/709-NA | No exemption/credit/treaty or filing conclusion here. Check this point with one of our partner accountants. |
| QDOT; special-use/recapture; installment/interest/acceleration and other payment deferrals; valuation/FLP/2704; IRS examinations; late portability/GST relief; charitable trust opinions | Check this point with one of our partner accountants. |
| Estate/trust income, DNI, 65-day rule, 642(g), IRD/691(c) | `us-form-1041-trust-and-estate-income` |
| State estate/inheritance/gift tax, portability; former 2025 matrix (CT, DC, HI, IL, ME, MD, MA, MN, NY, OR, RI, VT, WA, IA, KY, NE, NJ, PA) | `us-state-estate-and-inheritance-tax-matrix`; former state figures not usable here. |
| Covered expatriate gifts/bequests; foreign trusts; other 529; charitable design | `us-expatriation-exit-tax`; `us-foreign-trust-reporting`; `us-529-and-trump-accounts`; `us-charitable-giving-strategies`, respectively. |

## Filing and payment

| Return | Deadline/payment and next step | Source |
| --- | --- | --- |
| Form 706 | File/pay within nine months after death. Timely Form 4768 requests automatic six-month filing extension; payment relief is separate. Attach death certificate, certified will if testate (or explain unavailable certification), and supporting records. Keep delivery/payment proof. | [6075(a)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap61-subchapA-partV-sec6075.htm); [2026 instructions, When/Where To File, Paying the Tax](https://www.irs.gov/instructions/i706) |
| Form 709, 2026 gifts | Ordinary deadline 15 April 2027. Calendar-year income-tax extension also extends gift return; otherwise Form 8892 requests six months. Neither extends payment. In death year the gift deadline is no later than extended estate deadline; Form 4768 alone is not a universal gift extension. | [6075(b)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap61-subchapA-partV-sec6075.htm); [2025 instructions, extensions](https://www.irs.gov/instructions/i709) |
| Closing letter | Request through Pay.gov after waiting at least nine months from filing; current user fee applies. Account transcript is an alternative. Old fee figures are not usable. | [2026 instructions, closing letters](https://www.irs.gov/instructions/i706) |

The 2025 Form 709 layout does not prove the 2026 edition or electronic filing support. Confirm applicable edition, delivery address, e-file/signature authorization and payment channel before filing; unverified operational details are held. Check this point with one of our partner accountants.

Reviewer brief: filing test/deadline, assets/deductions, cumulative gifts/credit, separate GST history, elections/consents, basis/reporting, state routes and each held point. No final return while a dependent fact remains unresolved.

## Sources

| Official source and portions read | URL | Read on |
| --- | --- | --- |
| Read for 2010(b)–(d), current amount/indexing, DSUE, election/examination | https://uscode.house.gov/us/usc/t26/s2010/ | 2026-11-27 |
| Read for P.L.119-21 section70106, amount/indexing/sunset/effect | https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm | 2026-11-27 |
| Read for 2001(a)–(c),(g), computation and entire rate table | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleB-chap11-subchapA-partI-sec2001.htm | 2026-11-27 |
| Read for Rev.Proc.2025-32 section2.14 and4.41,4.42,4.51; old section3.14 citation corrected | https://www.irs.gov/pub/irs-drop/rp-25-32.pdf | 2026-11-27 |
| Read for Rev.Proc.2024-40 sections2.41–2.43; 2025 only | https://www.irs.gov/pub/irs-drop/rp-24-40.pdf | 2026-11-27 |
| Read for 6018(a), filing threshold/gifts/specific exemption | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap61-subchapA-partII-subpartC-sec6018.htm | 2026-11-27 |
| Read for 6019, statutory gift-return exceptions | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap61-subchapA-partII-subpartC-sec6019.htm | 2026-11-27 |
| Read for 2503(a)–(c),(e), annual/minor/direct-payment exclusions | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleB-chap12-subchapA-sec2503.htm | 2026-11-27 |
| Read for 2513(a)–(c), eligibility/consent | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleB-chap12-subchapB-sec2513.htm | 2026-11-27 |
| Read for 2523(a),(b),(f),(i), marital exceptions/citizenship | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleB-chap12-subchapC-sec2523.htm | 2026-11-27 |
| Read for 529(c)(2),(4), gift election/death inclusion only; no other 2024-edition rules relied on | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapF-partVIII-sec529.htm | 2026-11-27 |
| Read for 2502(a), cumulative computation | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleB-chap12-subchapA-sec2502.htm | 2026-11-27 |
| Read for 2505(a)–(c), available credit/limit | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleB-chap12-subchapA-sec2505.htm | 2026-11-27 |
| Read for 2056(a),(b)(1),(7),(d), marital/QTIP/noncitizen exceptions | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleB-chap11-subchapA-partIV-sec2056.htm | 2026-11-27 |
| Read for 2055(a),(c)–(e), recipients/tax burden/cap/split interests | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleB-chap11-subchapA-partIV-sec2055.htm | 2026-11-27 |
| Read for 20.2010-2(a)(1),(2),(7), election and valuation exceptions; eCFR through24November2026 | https://www.ecfr.gov/current/title-26/section-20.2010-2 | 2026-11-27 |
| Read for Rev.Proc.2022-32 sections3–5, scope/heading/deadline/survivor-estate/refund limits | https://www.irs.gov/pub/irs-drop/rp-22-32.pdf | 2026-11-27 |
| Read for 2032(a)–(d), all assets/lapse-of-time/combined tax/irrevocability | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleB-chap11-subchapA-partIII-sec2032.htm | 2026-11-27 |
| Read for 6166(a),(b), gateway/proportional cap/basic timing only; specialist outcomes held | https://uscode.house.gov/us/usc/t26/s6166/ | 2026-11-27 |
| Read for 2613(a), natural-person/trust tests | https://uscode.house.gov/us/usc/t26/s2613/ | 2026-11-27 |
| Read for 2651(b)–(f), generations; case-specific exceptions held | https://uscode.house.gov/us/usc/t26/s2651/ | 2026-11-27 |
| Read for 2631(a)–(c), separate exemption/irrevocability/BEA link | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleB-chap13-subchapD-sec2631.htm | 2026-11-27 |
| Read for 2632(b),(c), automatic allocation/trust exceptions/elections | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleB-chap13-subchapD-sec2632.htm | 2026-11-27 |
| Read for 2641(a),(b), rate product | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleB-chap13-subchapE-sec2641.htm | 2026-11-27 |
| Read for 2642(a),(d)–(g), adjusted denominator/recomputation/ETIP/relief | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleB-chap13-subchapE-sec2642.htm | 2026-11-27 |
| Read for 1014(a)–(f), valuations/community/IRD/gift-back/cap | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapO-partII-sec1014.htm | 2026-11-27 |
| Read for 1015(a),(d),(e), gain/loss/gift-tax/spousal basis | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapO-partII-sec1015.htm | 2026-11-27 |
| Read for 1.6035-1(b),(c)(1)–(5), required-return scope, acquisition, statements and supplementation | https://www.ecfr.gov/current/title-26/section-1.6035-1 | 2026-11-27 |
| Read for August2025 instructions, Who Must File/When To File; future-dated December2026 online edition not relied on | https://www.irs.gov/pub/irs-prior/i8971--2025.pdf | 2026-11-27 |
| Read for 6075(a),(b), deadlines/extensions/deceased donor | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap61-subchapA-partV-sec6075.htm | 2026-11-27 |
| Read for 25.2503-6(a),(b), direct tuition/medical/reimbursement | https://www.ecfr.gov/current/title-26/section-25.2503-6 | 2026-11-27 |
| Read for July2026 instructions, general filing/payment, PartII/V, schedules/redesign, marital/charity/GST, closing letter/supporting records | https://www.irs.gov/instructions/i706 | 2026-11-27 |
| Read for 2025 instructions, filing/extensions, PartIII consent/timing/both exceptions, SchedulesA–D and529; 2026 edition not confirmed | https://www.irs.gov/instructions/i709 | 2026-11-27 |

| Read for 20.2032-1(a),(b),(g), election/revocation/late first return and related deduction coordination | https://www.ecfr.gov/current/title-26/section-20.2032-1 | 2026-11-27 |

Not yet confirmed: explicitly held specialist outcomes above; 2026 Form 709 edition/placement/e-filing. Reg.20.2010-1 returned an access challenge; no anti-clawback outcome or proposal status is represented as proven. Historical 2024/state rates, NRA amounts, QDOT security limits, special-use/interest caps and appraisal thresholds are not usable guidance here.
