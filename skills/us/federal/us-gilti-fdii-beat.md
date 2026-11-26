---
name: us-gilti-fdii-beat
description: US federal CFC, subpart F and net CFC tested income computations for 2026, with separately dated 2025 GILTI cases, the section 962 election, FDDEI and BEAT. Establish ownership and credit facts before computing; specialist points are explicitly held. Trigger on GILTI, NCTI, CFC, subpart F, section 962, FDII, FDDEI, BEAT and Forms 8992, 8993 or 8991.
version: "1.2"
jurisdiction: US
category: international
tax_year: 2026
last_updated: 2026-11-26
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: cross-border
type: computation
---

# US controlled foreign corporations, FDDEI and BEAT: tax year 2026

> **Source-cited draft.** No accountant has reviewed this Guide. Federal only. This is a draft working paper, requiring a qualified preparer's review before filing; it does not resolve the specialist points held below. [Circular 230 section 10.37](https://www.ecfr.gov/current/title-31/section-10.37): establish the relevant facts, apply the law to them and consider contrary facts before giving written tax advice.

**Answer first.** Establish the foreign entity's US classification and the shareholder's actual ownership before calculating. For taxable years beginning after 31 December 2025, section 951A includes net CFC tested income without a QBAI reduction; an eligible domestic corporation's section 250 percentages are 40% for that inclusion and its attributable section 78 gross-up, and 33.34% for FDDEI. The section 960(d) deemed-paid percentage is 90%, subject to the separate foreign tax credit limitation. These are not a guaranteed credit or an individual election recommendation. [Sections 951A, 250 and 960](https://uscode.house.gov/us/usc/t26/s951A/); [enacted dates, Public Law 119-21 sections 70312, 70321 and 70323](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm).

## Scope and who this is for

US owners of foreign corporations and corporations considering FDDEI or BEAT. Confirm US-person status and US tax classification; do not classify an entity from its local legal name. Partnerships, disregarded entities, trusts and pass-through owners need their separate analysis. Load `cross-border-tax-workflow-base` for the working-paper process.

Use `us-form-5471-cfc-information` for Form 5471 categories, schedules, penalties and missed years; `us-form-1040-individual-return` or `us-form-1120-c-corp` for the return; `us-foreign-tax-credit-1116` for ordinary individual credits; `us-form-8865-foreign-partnership`, `us-form-5472-foreign-owned-us`, `us-foreign-trust-reporting` and `us-fbar-and-fatca-8938` for their distinct reporting jobs. Forms 8858 (foreign disregarded entities/branches) and 8975/Country-by-Country reporting remain specialist routing topics. These routes do not establish that an obligation exists.

## Ask the client first

Obtain every entity's US classification, owners and ownership chain; vote and value by date; both tax years; acquisitions, disposals and distributions; income by category; US-tax deductions, foreign taxes and earnings and profits; currencies and translation records; earlier returns, elections, PTEP and basis accounts. For FDDEI obtain contracts and evidence of purchaser, foreign use and service location. For BEAT obtain group gross receipts for each preceding year, related-party payments, withholding, deductions, NOLs and the statutory identity of every credit. Missing facts are holds: never assume CFC status, creditability, an election or dividend character.

## The method, step by step

### 1. Ownership and the applicable year

| Test | Rule | Official source |
| --- | --- | --- |
| Ordinary United States shareholder | At least 10% of vote **or** value, counting section 958(a) and (b) ownership; exactly 10% qualifies | [Section 951(b)](https://uscode.house.gov/us/usc/t26/s951/) |
| Ordinary CFC | United States shareholders own more than 50% of vote **or** value on any day; exactly 50% fails. Count underlying stock once | [Section 957(a)](https://uscode.house.gov/us/usc/t26/s957/) |
| Corporate rate | 21% | [Section 11(b)](https://uscode.house.gov/us/usc/t26/s11/) |

Keep section 958(a) direct/proportionate indirect ownership through foreign entities separate from section 958(b) constructive status. Constructive status alone does not establish an inclusion; domestic pass-through owners require separate treatment. For foreign-corporation years beginning after 31 December 2025, restored section 958(b)(4) blocks attribution under section 318(a)(3)(A)–(C) from a foreign person to a US person. Do not conclude that a foreign sister has no inclusion exposure: section 951B is held below. [Section 958](https://uscode.house.gov/us/usc/t26/s958/); [Public Law 119-21 section 70353](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm).

For foreign-corporation years beginning after 31 December 2025, a section 958(a) shareholder on **any day** includes subpart F income attributable to its stock and the period when it owned it, was a United States shareholder and the corporation was a CFC. Include in the shareholder year containing its last ownership day in that CFC year. Section 951A uses those pro rata/timing rules. This is not permission to divide all annual income mechanically by days. Mid-year transactions, fiscal-year mismatches, section 956, the 2025 dividend transition and the section 898 one-month-deferral repeal: **Check this point with one of our partner accountants.** [Sections 951(a), 951A(c)](https://uscode.house.gov/us/usc/t26/s951/); [Public Law 119-21 sections 70352–70354](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm).

### 2. Subpart F before tested income

Section 952 includes insurance and foreign base company income, and also boycott, unlawful-payment and section 901(j) items. Section 954's main categories are personal holding company income, related-party sales income and related-party services income. A label such as active trading, services, rent or royalty does not itself settle classification. Detailed classification, same-country and active rents/royalties exceptions, manufacturing/branch rules (including Whirlpool), active financing/insurance and related-CFC look-through: **Check this point with one of our partner accountants.** [Sections 952](https://uscode.house.gov/us/usc/t26/s952/) and [954](https://uscode.house.gov/us/usc/t26/s954/).

| Subpart F screen | Exact boundary | Official source |
| --- | --- | --- |
| De minimis | Foreign base company income, before paragraph (5) deductions, plus gross insurance income **less than** the lesser of 5% of gross income or USD 1,000,000 | [Section 954(b)(3)(A)](https://uscode.house.gov/us/usc/t26/s954/) |
| Full inclusion | That sum **exceeds 70%** of gross income; whole gross income is treated as foreign base company/insurance income, subject to high-tax relief and deductions | [Section 954(b)(3)(B)](https://uscode.house.gov/us/usc/t26/s954/) |
| Statutory high-tax test | Item's foreign effective rate **greater than 90%** of the maximum section 11 rate: derived threshold greater than 18.9%; equality fails | [Section 954(b)(4)](https://uscode.house.gov/us/usc/t26/s954/), [section 11](https://uscode.house.gov/us/usc/t26/s11/) |

The current-year E&P limit in section 952(c)(1)(A) and later recapture in (c)(2) must both be considered; tested losses also affect that E&P limit under section 951A(b)(2)(B)(ii). E&P/deficit calculations and an actual subpart F inclusion or its credit-category allocation are specialist holds. **Check this point with one of our partner accountants.** [Section 952(c)](https://uscode.house.gov/us/usc/t26/s952/); [section 951A(b)](https://uscode.house.gov/us/usc/t26/s951A/).

The tested-income high-tax exclusion is not automatic because a country's headline rate exceeds the threshold. Tested units, CFC-group consistency, controlling-shareholder authority, notices, amended returns, payment and election/revocation windows must be established. The earlier 24-month/six-month instructions are not supplied as usable 2026 election instructions here. **Check this point with one of our partner accountants.**

### 3. Net CFC tested income

Under [section 951A(b)](https://uscode.house.gov/us/usc/t26/s951A/), tested income is the excess of the following eligible gross income over properly allocable deductions **including taxes**. Exclude section 952(b) income (observe its treaty exception), gross income taken into account for subpart F, income excluded by section 954(b)(4), related-person dividends and foreign oil and gas extraction income. Deductions exceeding eligible gross income give tested loss. Net CFC tested income is the **positive excess**, if any, of aggregate pro rata tested income over aggregate pro rata tested losses. Do not report a negative inclusion or give a tested-loss CFC's taxes a deemed-paid credit.

No QBAI return reduces the inclusion for taxpayer years beginning after 31 December 2025. Section 951A(d) applies section 959, 961 and 962 treatment to this inclusion for the specified purposes; it does not turn it into subpart F for every purpose. [Section 951A](https://uscode.house.gov/us/usc/t26/s951A/); [Public Law 119-21 section 70323](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm).

### 4. Corporate deduction and credits

| Item, years beginning after 31 December 2025 | Computation and conditions | Official source |
| --- | --- | --- |
| Section 960(d) | 90% × inclusion percentage × tested foreign income taxes properly attributable to tested income taken into account | [Section 960(d)](https://uscode.house.gov/us/usc/t26/s960/), [enacted date](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| Section 250(a)(1)(B) | 40% of net CFC tested income **plus its attributable section 78 gross-up**, subject to taxable-income limitation | [Section 250](https://uscode.house.gov/us/usc/t26/s250/), [enacted date](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| Section 250(a)(1)(A) | 33.34% of FDDEI, subject to the same limitation | [Section 250](https://uscode.house.gov/us/usc/t26/s250/), [enacted date](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |

Inclusion percentage is net CFC tested income divided by aggregate pro rata tested income. The section 78 gross-up, where the corporation chooses the foreign tax credit regime, ignores the percentage haircut. Section 960(a) separately deems taxes properly attributable to subpart F items paid, without the tested-income haircut. Actual creditability, tax translation, sourcing and section 904 limitations must still be established. [Sections 960](https://uscode.house.gov/us/usc/t26/s960/) and [78](https://uscode.house.gov/us/usc/t26/s78/).

Apply section 250(a)(2) **before** the percentages: where FDDEI plus net CFC tested income exceeds taxable income before section 250, reduce FDDEI proportionately and net CFC tested income by the remainder. Do not merely cap the final deduction at taxable income. [Section 250(a)(2)](https://uscode.house.gov/us/usc/t26/s250/).

For the section 951A category limitation from 2026, allocate section 250(a)(1)(B) and relevant section 164(a)(3) deductions, plus other directly allocable deductions. Allocate no interest or research/experimental expenditure to this category; amounts displaced by section 904(b)(5)(B)/(C) go to US-source income. The separate limitation still applies; excess section 951A credits have no carryback/forward. Derived tax before credits is 21% × 60% = 12.6% of the grossed-up amount; 12.6% ÷ 90% = 14% is only a simplified break-even calculation, not a credit guarantee. [Section 904](https://uscode.house.gov/us/usc/t26/s904/); [Public Law 119-21 section 70311](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm).

**Distribution-tax hold.** Section 960(d)(4)'s 10% credit denial concerns taxes on amounts excluded under section 959(a) by reason of section 951A inclusions. Section 70312(c)(2) ties the effective wording to an inclusion after 28 June 2025; do not use only the distribution's date. Applying it to actual PTEP, taxes, tiers and distribution dates: **Check this point with one of our partner accountants.** [Section 960(d)(4)](https://uscode.house.gov/us/usc/t26/s960/); [section 70312(c)(2)](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm).

### 5. Individual and section 962

Without section 962 an individual has no corporate section 250 deduction or deemed-paid section 960 credit for the CFC's own tax. Use the individual return's applicable ordinary rates. Under section 962, the chapter 1 tax on covered inclusions is computed as for a domestic corporation; the regulation permits the section 250 deduction on the tested-income inclusion and related gross-up, not an individual's FDDEI deduction. [Sections 250](https://uscode.house.gov/us/usc/t26/s250/), [960](https://uscode.house.gov/us/usc/t26/s960/), [962](https://uscode.house.gov/us/usc/t26/s962/); [Reg. 1.962-1(b)](https://www.ecfr.gov/current/title-26/section-1.962-1).

An eligible individual (including a trust or estate) files an election statement with the return, containing the CFC/ownership-chain, company-by-company inclusions, E&P/taxes and distribution information. The election covers all CFCs producing that year's section 951(a) inclusions; revocation needs consent. Do not infer either a blanket amended-return prohibition or automatic late-election relief. [Reg. 1.962-2](https://www.ecfr.gov/current/title-26/section-1.962-2).

Section 962(d) includes distributed attributable E&P to the extent it exceeds the tax paid on the elected amounts, notwithstanding section 959(a)(1). Actual PTEP ordering, distributable E&P, qualified-dividend eligibility (including treaty, holding-period and PFIC conditions), NIIT, withholding and state treatment require a separate model. Ireland's treaty status alone does not prove a 20% rate; Singapore or Hong Kong residence alone does not settle every dividend. Election recommendation, Smith/CCA 202118008 analysis and the distribution years: **Check this point with one of our partner accountants.** [Section 962(d)](https://uscode.house.gov/us/usc/t26/s962/).

### 6. FDDEI

An eligible domestic C corporation may deduct the FDDEI percentage above; S corporations, RICs and REITs are excluded. DEI excludes section 951(a)(1) inclusions, section 951A income, financial-services income, CFC dividends, domestic oil/gas extraction income, foreign-branch income and the specified disposition income/gains. Subtract properly allocable expenses/deductions including taxes, **other than interest and R&E** for years beginning after 31 December 2025. The disposition exclusion covers intangible property and other seller-depreciable/amortizable/depletable property, subject to statutory exceptions, for dispositions after 16 June 2025. [Section 250(b)(3)](https://uscode.house.gov/us/usc/t26/s250/); [Public Law 119-21 section 70322](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm); [Form 8993 eligibility](https://www.irs.gov/instructions/i8993).

FDDEI is eligible income from property sold to a non-US person for demonstrated foreign use, or services demonstrated to be provided to persons/property outside the US; no domestic QBAI routine-return subtraction applies from 2026. Related-party and domestic-intermediary conditions apply. Foreign distributors, US round-tripping, digital/cloud content, mixed-territory licences, business-recipient location, contemporaneous substantiation and small-business documentation exceptions are **held**, not approved from an address or IP log. **Check this point with one of our partner accountants.** [Section 250(b)(1)–(2)](https://uscode.house.gov/us/usc/t26/s250/); [section 70323](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm). Section 174/174A expensing/amortization itself is also held. Historical 2025 FDII domestic-QBAI, deemed-intangible-income and foreign-derived-ratio calculations are a separate held point: **Check this point with one of our partner accountants.**

### 7. BEAT

| Gateway/rate | Conditions | Official source |
| --- | --- | --- |
| USD 500,000,000 | Three-prior-taxable-year **average**, applying aggregation and foreign-person receipts rules; corporation other than RIC, REIT or S corporation | [Section 59A(e)](https://uscode.house.gov/us/usc/t26/s59A/) |
| 3% base erosion percentage | At least this percentage; 2% for the statutory bank/securities-dealer affiliated group | [Section 59A(e)(1)(C)](https://uscode.house.gov/us/usc/t26/s59A/) |
| 10.5% | Years beginning after 31 December 2025; bank/securities-dealer group adds one percentage point (derived 11.5%) | [Section 59A(b)](https://uscode.house.gov/us/usc/t26/s59A/), [section 70331](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |

Identify payments, then benefits. Section 59A(d) covers deductible foreign-related payments, depreciable/amortizable acquisitions, reinsurance and specified expatriated-entity payments. Section 59A(g) includes 25%-owner, section 267/707 and section 482 relationships; it is not simply a 25% common-ownership rule. The percentage denominator excludes section 172/245A/250 deductions and specified services/derivative deductions. Modified taxable income disregards base erosion benefits and the applicable NOL portion. NOL vintages/origin-year percentages, COGS exceptions, SCM cost/markup, ECI, derivatives and withholding exclusions require classification: **Check this point with one of our partner accountants.** [Section 59A(c)–(h)](https://uscode.house.gov/us/usc/t26/s59A/).

Compute the positive excess of rate × modified taxable income over regular tax reduced (not below zero) by credits **less protected credits**. The research credit is protected. For applicable section 38 credits (section 42, section 45 and the section 48 energy portion of section 46), protection is **80% of the lesser of those credits or the BEAT amount computed without that protection**. It is not always 80% of the credits. Foreign tax credits are not in this protected list. [Section 59A(b)(1), (3)](https://uscode.house.gov/us/usc/t26/s59A/).

**Filing differs from liability.** The December 2025 Form 8991 instructions require filing if the corporation or aggregate group has annual gross receipts of at least USD 500 million in **one or more** of the preceding three years, even if the average or percentage does not produce BEAT. Thus a USD 499 million average does not establish a filing exemption. Attach to the income tax return by its due date including extensions. [Form 8991, Who Must File / When To File](https://www.irs.gov/instructions/i8991).

## Boundary and exception table

| Boundary | Result |
| --- | --- |
| Original 9% direct owner with possible family/entity attribution | Do not treat the direct percentage as the whole test; complete the ownership maps, with specialist attribution held |
| Unknown ownership, foreign tax or E&P | Stop the affected calculation; no assumed CFC or guessed credit |
| Constructive-only owner | Status is separate from section 958(a) inclusion; pass-through/951B cases held |
| Aggregate tested losses exceed tested income | No negative section 951A inclusion |
| Corporate taxable-income limitation binds | Apply section 250(a)(2) before deduction percentages |
| High-tax/election, dividend character or a treaty position is unresolved | No recommendation or usable final figure; partner-accountant referral |
| BEAT receipts below the average gateway | Independently test Form 8991's single-year filing trigger |

## Worked cases

All cases are hypothetical. Foreign taxes, marginal rates, exchange rates and QBAI amounts are **case inputs**, not statements of foreign law or approved translation methods. Simple 2026 cases stipulate calendar taxpayer/CFC years, full-year 100% section 958(a) ownership, no subpart F, no other CFCs, creditable tested foreign taxes, all relevant income foreign-source, no extra deductions/losses or binding section 250 limit. Establish those facts before using a calculation. Held cases are diagnostic arithmetic only, **not usable filing figures or recommendations**.

### Case 1: 2026 German CFC, compare the high-tax exclusion

The US C corporation's CFC earns USD 1,320,000 before USD 396,000 of foreign tax (30% input). Tested income is USD 924,000; gross-up USD 396,000; section 250 deduction USD 528,000; pre-credit US tax USD 166,320. Deemed-paid tax USD 356,400 is capped at USD 166,320, leaving nil residual and USD 190,080 unused without carryover. Under the **stipulation** that the whole item is validly excluded, its inclusion/gross-up/credit would all be nil. The same immediate tax does not prove that electing is better across the group: **Check this point with one of our partner accountants.** Sources: sections 951A, 78, 250, 960 and 904 above.

```oa-check
name: Corporate tested income arithmetic (2026)
inputs:
  pretax_income: 1320000
  foreign_tax: 396000
steps:
  - tested_income: pretax_income - foreign_tax
  - grossed_up: tested_income + foreign_tax
  - deduction_250: grossed_up * 0.40
  - precredit: (grossed_up - deduction_250) * 0.21
  - deemed_paid: foreign_tax * 0.90
  - allowed: min(deemed_paid, precredit)
  - residual: precredit - allowed
  - unused: deemed_paid - allowed
expected:
  tested_income: 924000
  deduction_250: 528000
  precredit: 166320
  deemed_paid: 356400
  residual: 0
  unused: 190080
```

### Case 2: 2026 Irish CFC, section 962 comparison held

Original inputs: USD 300,000 pretax, USD 37,500 foreign tax (12.5%), 37% individual marginal rate, later payout of all earnings, and an **unproved** 20% qualified-dividend assumption. Tested income USD 262,500; no-election income tax at the stipulated marginal rate USD 97,125. The stipulated corporate-rate inclusion arithmetic gives grossed-up income USD 300,000, deduction USD 120,000, pre-credit tax USD 37,800, credit USD 33,750 and current tax USD 4,050. Purely applying the former distribution assumptions gives (262,500 − 4,050) × 20% = USD 51,690; total USD 55,740, difference USD 41,385. **Those later-year outputs and the recommendation are held**: actual E&P/PTEP, tax paid, dividend eligibility/rates and NIIT were not established. **Check this point with one of our partner accountants.**

### Case 3: 2026 FDDEI

Original DEI USD 10,000,000; USD 4,000,000 **stipulated to satisfy all FDDEI requirements**, taxable income sufficient for the whole deduction. Deduction USD 1,333,600; corporate tax attributable to FDDEI USD 559,944; derived effective rate 13.9986%. This illustrates the section 250 percentage, not documentary eligibility.

```oa-check
name: FDDEI deduction arithmetic (2026)
inputs:
  dei: 10000000
  fddei: 4000000
steps:
  - deduction: fddei * 0.3334
  - tax: (fddei - deduction) * 0.21
  - effective_rate: tax / fddei
expected:
  deduction: 1333600
  tax: 559944
  effective_rate: 0.139986
```

### Case 4: 2026 BEAT, current foreign-tax-credit variant

Original average receipts USD 2.4 billion; taxable income USD 300 million; eligible denominator USD 1 billion; stipulated base erosion benefits USD 235.1 million (Bermuda royalty USD 150 million, Swiss cost-plus-8% management fee USD 80 million, building depreciation USD 5.1 million); regular tax USD 63 million; research credit USD 20 million; **foreign tax credit USD 15 million**. Assume no NOL, bank surcharge or excluded benefits and all credit allowances established. Percentage 23.51%; MTI USD 535.1 million; tentative amount USD 56,185,500; regular comparison USD 48 million; BEAT USD 8,185,500. Regular tax after credits USD 28 million; total USD 36,185,500. Payment classification/withholding is held; the figures cannot be used before that is resolved. **Check this point with one of our partner accountants.**

```oa-check
name: BEAT stipulated FTC variant (2026)
inputs:
  taxable_income: 300000000
  benefits: 235100000
  denominator: 1000000000
  regular_tax: 63000000
  research_credit: 20000000
  foreign_tax_credit: 15000000
steps:
  - percentage: benefits / denominator
  - mti: taxable_income + benefits
  - tentative: mti * 0.105
  - comparison: regular_tax - foreign_tax_credit
  - beat: max(tentative - comparison, 0)
  - regular_after: regular_tax - research_credit - foreign_tax_credit
  - total: regular_after + beat
expected:
  percentage: 0.2351
  mti: 535100000
  comparison: 48000000
  beat: 8185500
  total: 36185500
```

### Predecessor Case A/B: 2026 individual, retain both scenarios

Original tested income USD 100,000 **after** USD 15,000 foreign tax; pretax USD 115,000. Without section 962: USD 100,000 ordinary inclusion, no corporate deduction/deemed-paid credit. With the simple-case assumptions above: foreign rate 15,000 / 115,000 = 13.043478%; gross-up USD 15,000; deduction USD 46,000; taxable USD 69,000; pre-credit USD 14,490; credit USD 13,500; current tax USD 990. The old USD 99,010 distribution calculation is only 100,000 − 990 under stipulated distributable E&P; actual later taxation is held. **Check this point with one of our partner accountants.**

### Predecessor Case C: 2025 QBAI, compared with 2026

Original tested income USD 100,000, eligible QBAI USD 200,000, no specified interest expense, individual without section 962. For 2025, NDTIR USD 20,000, GILTI USD 80,000. With the same tested income in 2026 the inclusion is USD 100,000, without that reduction. This uses [pre-amendment section 951A(b),(d)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partIII-subpartF-sec951A.htm) and section 70323's effective date; historical QBAI is quarterly-average eligible tangible property using ADS, not a general asset balance.

### Predecessor Case D: late Form 5471

One CFC, one unfiled year, failure continuing after an IRS notice and beyond 90 days. The original maximum arithmetic was USD 10,000 + USD 50,000 = USD 60,000, **not a penalty automatically reached on day 91**. The actual notice periods, credit reductions, assessment period and reasonable cause require the Form 5471 Guide; do not calculate them here. **Check this point with one of our partner accountants.**

### Historical Example 1: TechCo, Inc. / TechCo GmbH, 2025

Keep the original Delaware parent and 100%-owned German CFC, calendar 2025; gross EUR 5,000,000, operating deductions EUR 3,800,000, pretax EUR 1,200,000, input tax rate 30%, tax EUR 360,000, after-tax EUR 840,000; ADS QBAI EUR 600,000; stipulated EUR 1 = USD 1.10; no subpart F/ECI, no high-tax election, no other CFC or specified interest and a nonbinding deduction limit. Translation method/credit eligibility are held, not established from an average rate.

Corrected diagnostic arithmetic: USD pretax 1,320,000, tax 396,000, **tested income after tax 924,000**, QBAI 660,000; NDTIR 66,000; GILTI 858,000; inclusion percentage 13/14; gross-up 367,714.29; 50% deduction 612,857.14; pre-credit tax 128,700; 80% deemed-paid amount 294,171.43; under a fully available limit, residual nil and unused 165,471.43. No 2026 percentage is used in this 2025 case. Election/translation/credit decisions: **Check this point with one of our partner accountants.**

### Historical Example 2: Sarah / Sarah Trading Pte. Ltd., 2025

Preserve the US citizen in San Francisco, 100% owner of the Singapore company formed in 2022, Asia-Pacific consulting; SGD gross 800,000, operating deductions 500,000, pretax 300,000, input tax 17% = 51,000, after-tax 249,000; ADS QBAI 40,000; salary 120,000 already in deductions; no dividend in 2025; exact input SGD 1.35 per USD (the old SGD 1 = USD 0.74 was rounded). Preserve the former 37% ordinary, 3.8% NIIT and 13.3% California assumptions **as unverified historical assumptions, not applicable rates or an additive inclusion tax**.

Diagnostic arithmetic using the exact exchange input: USD tested income after tax 184,444.44; tax 37,777.78; QBAI 29,629.63; NDTIR 2,962.96; GILTI 181,481.48. At the stipulated 37% alone: USD 67,148.15. Hypothetical section 962 computation with all credit/source facts stipulated: inclusion percentage 0.98393574297; gross-up USD 37,170.91; 50% deduction USD 109,326.19; pre-credit USD 22,958.50; 80% deemed-paid amount USD 29,736.72; capped credit USD 22,958.50, unused USD 6,778.22, current residual nil. Do not add the old NIIT assumption, assume a qualified dividend, or declare this a lifetime saving. Later distributions, PTEP, NIIT, state and Singapore law are **non-usable holds**. **Check this point with one of our partner accountants.**

### Historical Example 3: MegaCorp, Inc., 2025 and 2026

Preserve average 2022–2024 receipts USD 2.4 billion, 2025 receipts USD 2.5 billion, COGS USD 1.2 billion and stated total deductions USD 1 billion. Original component list: salaries/G&A 400 million, third-party US interest 50 million, Bermuda related royalty 150 million, Swiss related services 80 million at cost plus 8% without SCM, other domestic deductions 320 million, plus building depreciation 5.1 million on a 2023 related-party USD 200 million acquisition with a 39-year input life. **The components sum to USD 1,005.1 million, not USD 1 billion.** Keep the stated total and taxable income USD 300 million only as a separate stipulated scenario; reconcile the underlying deductions before filing. Do not silently absorb the USD 5.1 million discrepancy.

The earlier credit input was research USD 20 million plus **other general business credits USD 15 million**, described as section 38/48 ITC/45 PTC, not the current Case 4's FTC. Classification is not established. Under the explicit hypothetical that all USD 15 million are statutory applicable section 38 credits, with the other Case 4 facts fixed: before their protection the 2025 BEAT amount is 53.51 − (63 − 15) = USD 5.51 million; protection = 80% × min(15, 5.51) = USD 4.408 million; BEAT USD 1.102 million; total USD 29.102 million. For the 2026 projection, 56.1855 − 48 = USD 8.1855 million before that protection; protection USD 6.5484 million; BEAT USD 1.6371 million; total USD 29.6371 million. These conditional results replace both the old nil and USD 22.51 million results. Receipts averaging must be updated for 2026; payment exclusions, credit identity and the deduction discrepancy remain **non-usable holds**. **Check this point with one of our partner accountants.**

## When to refuse or refer

Each held point below means: **Check this point with one of our partner accountants.** Do not supply a usable calculation, election, exemption or deadline for it.

| Code | Held point |
| --- | --- |
| R-INTL-951B / PRS / FY | Foreign-parent attribution, section 951B, domestic pass-through and trust chains; mid-year transactions; fiscal years, one-month deferral and 2025 transition dividends |
| R-INTL-956 / EP | Section 956; insurance/active-financing, same-country, rents/royalties, manufacturing/Whirlpool, look-through, E&P/deficits/recapture and boycott/sanctions/unlawful-payment classification |
| R-INTL-7 / NIIT / 2 | High-tax election/revocation and tested units; section 962 late election, second layer, PTEP/basis ordering, Smith and CCA 202118008, NIIT; creditability, translation, sourcing, consolidated groups and Form 1118/1116 coordination |
| R-INTL-1 / 4 / 5 / 6 / 10 | Transfer pricing; treaty/LOB, inbound FDAP/ECI and FIRPTA; inversion planning; hybrids; cross-border M&A and section 245A distributions |
| R-INTL-3 | Pillar Two QDMTT/IIR/UTPR, foreign adoption, creditability, section 891 and ASC 740 provision; no US or foreign adoption/threshold conclusion supplied |
| R-INTL-8 / 9 / 965 / STATE | Trusts, PFIC overlap, transition tax/installments and S-corporation deferral, state conformity; Farhy litigation and penalty strategy |
| R-INTL-FDDEI / BEAT | Transaction documentation and foreign use; section 174/174A; BEAT aggregation, payment exceptions, NOLs, withholding and credit identity |

## Filing and payment

Reconcile the inclusion working paper to Forms 8992/5471, the section 250 deduction to Form 8993 and corporate/deemed-paid credits to Form 1118; these are form routes, not clearance of a return's reporting obligations. The read Form 8992 instructions are December 2024 and Form 8993 instructions December 2025; their pre-amendment computations/lines do not override the enacted 2026 statute. **2026 line mapping, attachments, section 962 reporting and consolidated/pass-through reporting are held. Check this point with one of our partner accountants.**

Use `us-form-5471-cfc-information` for categories and schedules, notice penalties, correction/late filing and assessment periods; its Form 5471 timing is the return due date including extensions. Use the individual/corporate return Guides and `us-quarterly-estimated-tax` for deadlines, extensions and payment. Do not apply the former blanket overseas automatic extension or an extension of time to pay from this Guide.

## Completion checklist

- [ ] Classification, US-person status, ownership maps and both tax years established.
- [ ] Income categories, E&P, deductions, creditable foreign taxes and translations documented.
- [ ] Correct year's inclusions, section 250 limit, credit percentage and separate limitation reconciled.
- [ ] Original case assumptions distinguished from verified client facts; held outputs excluded from filing.
- [ ] Election and later-distribution outcomes reviewed together; required specialist holds resolved.
- [ ] BEAT liability and Form 8991 filing trigger tested separately; credit cap applied.
- [ ] Return mapping, reporting, payments and professional sign-off completed separately.

## Sources

| Official source and passage read | URL | Date read |
| --- | --- | --- |
| Circular 230 section 10.37(a)(2): relevant facts, reasonable assumptions and application of law to facts | https://www.ecfr.gov/current/title-31/section-10.37 | 2026-11-26 |
| Public Law 119-21: sections 70311–70312, 70321–70323, 70331 and 70352–70354; read operative amendments and their separate effective dates, especially 70312(c)(2) | https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm | 2026-11-26 |
| Sections 951(b), 957(a) and 958(a)/(b), ordinary shareholder/CFC tests and restored foreign downward-attribution block; completed Form 5471 proof rows F04/F05/F09/F11/F17 reused for the same conditions | https://uscode.house.gov/us/usc/t26/s951/ ; https://uscode.house.gov/us/usc/t26/s957/ ; https://uscode.house.gov/us/usc/t26/s958/ | 2026-11-26 |
| Section 951A(a)–(d): exclusions, taxes, positive excess, tested-loss coordination, ownership/timing and specified-purpose treatment | https://uscode.house.gov/us/usc/t26/s951A/ | 2026-11-26 |
| Sections 952(a)–(c), 954(a)/(b): categories, strict boundaries, E&P and recapture; detailed exceptions are held | https://uscode.house.gov/us/usc/t26/s952/ ; https://uscode.house.gov/us/usc/t26/s954/ | 2026-11-26 |
| Sections 250(a)/(b), 960(a)/(d), 78 and 904(a)/(b)(5)/(c): deduction, tested taxes, gross-up, limits and expense allocation; completed FTC no-carryover proof reused | https://uscode.house.gov/us/usc/t26/s250/ ; https://uscode.house.gov/us/usc/t26/s960/ ; https://uscode.house.gov/us/usc/t26/s78/ ; https://uscode.house.gov/us/usc/t26/s904/ | 2026-11-26 |
| Sections 11(b), 962(a)/(d); Reg. 1.962-1(b), 1.962-2(a)–(c): corporate rate, permitted deductions, election scope/statement and distribution rule; regulatory historical percentages read with enacted amendments | https://uscode.house.gov/us/usc/t26/s11/ ; https://uscode.house.gov/us/usc/t26/s962/ ; https://www.ecfr.gov/current/title-26/section-1.962-1 ; https://www.ecfr.gov/current/title-26/section-1.962-2 | 2026-11-26 |
| Section 59A(b)–(h): protected-credit cap, benefits, denominator exclusions, gateways, relatedness; Form 8991 December 2025 Who Must File and When To File | https://uscode.house.gov/us/usc/t26/s59A/ ; https://www.irs.gov/instructions/i8991 | 2026-11-26 |
| Form 8992 December 2024 Purpose of Form/Schedule A; Form 8993 December 2025 Who Must File/When To File; historical form routes only, no 2026 line clearance | https://www.irs.gov/instructions/i8992 ; https://www.irs.gov/instructions/i8993 | 2026-11-26 |
| Pre-amendment section 951A(b)/(c)/(d), for the separately dated 2025 QBAI cases; 2025 50%/80% amounts from section 70321/70312 amendment text, 10% BEAT from 70331 and Form 8991 rate instructions | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapN-partIII-subpartF-sec951A.htm ; https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm | 2026-11-26 |

Not yet confirmed: all expressly held classification, election, distribution, foreign-law, credit, translation, documentation, fiscal-year, NOL, reporting and specialist points above. Held historical computations are non-usable diagnostics; no comprehensive claim that later guidance or forms do not exist is made. Repeated background/history, blanket non-indexation, unsupported automatic-filing/penalty predictions and repeated recommendations were removed; operative topics and original case inputs/years remain here or are explicitly routed/held.
