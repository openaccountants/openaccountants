---
name: us-citizen-moving-abroad-tax
description: Plan a US citizen or green card holder's move abroad in 2026. Compare the foreign earned income exclusion and foreign tax credit, check information reporting and social security, and screen state ties, retirement plans and expatriation before acting. Includes the original Dubai salary and exit-gain cases. Federal planning; destination and specialist computations are routed separately.
version: "1.3"
jurisdiction: US
tax_year: 2026
last_updated: 2026-11-27
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: cross-border
type: situation-rules
---

# A US citizen moving abroad: federal planning for 2026

> **Built from the law. Not yet approved.** General planning reference for employees, founders, retirees and accidental Americans. Apply the recorded facts and cited conditions; do not infer an election or filing exemption from residence alone. This is not an individualized written tax opinion under Circular 230 section 10.37 or filing authorization.

Moving abroad does not end US worldwide income taxation for a US citizen or resident alien. Filing depends on income, status and other filing triggers; it is not an unconditional lifetime Form 1040 obligation. Compare the exclusion and credit using the actual income, foreign tax and election history, then check reporting separately. [IRS Publication 54, Filing Requirements](https://www.irs.gov/publications/p54).

## Scope

US citizens and green card holders moving or living abroad in 2026. This Guide supplies the planning sequence and two conditional computations. Existing Guides own the detailed returns:

| Issue | Destination |
| --- | --- |
| Foreign earned income and housing | `us-foreign-earned-income-2555` |
| Foreign tax credit | `us-foreign-tax-credit-1116` |
| FBAR and Form 8938 | `us-fbar-and-fatca-8938` |
| Foreign corporations and inclusions | `us-form-5471-cfc-information`, `us-gilti-fdii-beat` |
| Foreign partnerships | `us-form-8865-foreign-partnership` |
| Foreign trusts and foreign gifts | `us-foreign-trust-reporting` |
| Citizenship, green cards, treaties and spouse elections | `us-tax-residency` |
| Self-employment | `us-schedule-c-and-se-computation` |
| State departure | `us-multi-state-residency-and-allocation`, `ca-residency-leaving-california` |
| Expatriation | `us-expatriation-exit-tax` |
| Estate and gift tax | `us-estate-gift-706-709` |
| Individual return and estimates | `us-federal-income-tax-return-1040`, `us-quarterly-estimated-tax` |
| Destination-country taxation | The destination's Guides; no local tax rate is assumed here |

## Ask the client first

Read existing records before requesting missing facts. Record citizenship and green card dates; destination and move date; 2026/2027 travel days; salary payer and work locations; self-employment, rent, pensions, dividends and gains; foreign tax paid/accrued and refunds; prior Form 2555 elections/revocations and credit carryovers; accounts, signature authority, funds and insurance; companies/ownership; trusts, gifts and non-US spouse; state home, licence, voting, family and business ties; retirement plans and proposed distributions; returns and information filings; and any renunciation plan, net worth and prior-five-year net income tax. Missing records remain unknown, not assumed delinquent or resident.

## The method, step by step

### Rates, bands and thresholds

| Item | Rate or amount, 2026 | Source |
| --- | --- | --- |
| Foreign earned income exclusion (FEIE) | Maximum USD 132,900, limited by qualifying income and days | [Rev. Proc. 2025-32, section 4.39](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Foreign housing base, full qualifying year | USD 21,264, derived: 16% of USD 132,900 | [26 USC 911(c)(1)](https://uscode.house.gov/us/usc/t26/s911/) |
| Housing expense limit, most locations, full qualifying year | USD 39,870; certain locations have higher limits | [2026 Form 2555 instructions, line 29b](https://www.irs.gov/instructions/i2555) |
| Standard deduction used in Case 1 | USD 16,100 for a single individual eligible for the full basic deduction | [Rev. Proc. 2025-32, section 4.14](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Covered-expatriate tax-liability test | Average annual net income tax for the five preceding tax years more than USD 211,000, subject to the exceptions below | [Rev. Proc. 2025-32, section 4.37](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Covered-expatriate net-worth test | USD 2,000,000 or more on expatriation, subject to the exceptions below | [26 USC 877(a)(2), incorporated by 877A(g)](https://uscode.house.gov/us/usc/t26/s877/) |
| Mark-to-market gain reduction | USD 910,000 for the deemed-sale tax year beginning in 2026; not below zero | [Rev. Proc. 2025-32, section 4.38](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |

### 1. Establish status and filing duties

A US citizen or resident alien is generally taxed on worldwide income. Check the Form 1040 filing tests even if exclusions may eliminate tax: worldwide gross income for this purpose includes potentially excluded foreign earned income and housing amounts. [Publication 54, Filing Requirements](https://www.irs.gov/publications/p54).

A green card does not cease to confer tax residence merely because its holder moves. Revocation, abandonment or treaty treatment can change that result; treaty termination requires foreign treaty residence, no waiver of those treaty benefits and notice to the IRS. Before abandonment or a treaty-residence claim, check long-term-resident status: at least 8 of the last 15 tax years ending with termination; treaty-resident years with no waiver are excluded. Do not treat eight full calendar years as necessary. Use `us-tax-residency` and `us-expatriation-exit-tax`. [Form 8854 instructions, LTR and lawful permanent resident](https://www.irs.gov/instructions/i8854).

### 2. Compare FEIE, housing and credit

- **Qualifying income:** FEIE concerns compensation for personal services performed in a foreign country, not investment dividends, interest, gains or pensions. US-government employee pay and the other statutory exclusions do not qualify. [26 USC 911(b), (d)(2)](https://uscode.house.gov/us/usc/t26/s911/).
- **Qualification:** establish a foreign tax home throughout the qualifying period and either 330 full days in foreign countries in a consecutive 12-month period, or bona fide foreign residence for an uninterrupted period including an entire tax year. A full day is midnight to midnight; merely being outside the US, including on international waters, is insufficient. Bona fide residence is available to US citizens and to resident aliens who are citizens/nationals of an income-tax-treaty country. A retained US abode generally prevents a foreign tax home; the Armed Forces combat-zone exception and time-test waivers require specialist review. [2026 Form 2555 instructions, Who Qualifies and Parts II/III](https://www.irs.gov/instructions/i2555).
- **Election and period:** make or maintain a valid Form 2555 election; the annual cap is reduced for a partial qualifying year and cannot exceed eligible foreign earned income. The election continues until revoked. [26 USC 911(b)(2), (e)](https://uscode.house.gov/us/usc/t26/s911/); [Form 2555 instructions](https://www.irs.gov/instructions/i2555).
- **Housing:** qualified expenses above the base can produce an exclusion attributable to employer-provided amounts; the self-employed portion instead uses a deduction with its own limit. The expense cap is not an additional exclusion. Use the location and qualifying-day rules in `us-foreign-earned-income-2555`; do not assume the standard location cap fits Dubai. [26 USC 911(c)](https://uscode.house.gov/us/usc/t26/s911/).
- **Credit:** qualified foreign income taxes paid or accrued may reduce US income tax, subject to legal liability, creditability, sourcing, category and limitation rules. The credit cannot exceed the applicable US tax limit. Ordinary excess credits generally carry back one year then forward ten; special categories/elections differ. Taxes attributable to excluded income cannot also generate a credit or deduction. Use `us-foreign-tax-credit-1116`. [Form 1116 instructions, Eligible Taxes, Line 10 and Line 12](https://www.irs.gov/instructions/i1116).
- **Destination comparison:** with no creditable foreign tax, the credit supplies no relief; model FEIE and any qualified housing benefit. With high foreign tax, model the credit first, but do not promise a zero US bill merely because the destination is Germany, France or the UK. For mixed Gulf salary, European rent and US investments, compute sourcing and categories separately and remove tax allocable to excluded income. [26 USC 911(d)(6)](https://uscode.house.gov/us/usc/t26/s911/); [IRS foreign tax credit](https://www.irs.gov/individuals/international-taxpayers/foreign-tax-credit).
- **Stacking:** nonexcluded income is taxed using the rates that would have applied without FEIE. Excluded salary does not open the lowest brackets for a Roth conversion or gains. [26 USC 911(f)](https://uscode.house.gov/us/usc/t26/s911/).
- **Revocation:** without IRS consent, re-election is barred before the sixth tax year after the revocation year. A revocation for 2025 therefore bars 2026–2030; the earliest unrestricted year is 2031. [26 USC 911(e)(2)](https://uscode.house.gov/us/usc/t26/s911/).

### 3. Review reporting and investments before acting

Build a separate filing map from the records, with owner, trigger, exception, deadline and penalty source for each form. This is a screening list, not a finding that every listed form is due:

| Records to review | Filing destination or hold |
| --- | --- |
| Foreign accounts and signature authority | FBAR; `us-fbar-and-fatca-8938` |
| Specified foreign financial assets | Form 8938; `us-fbar-and-fatca-8938`; test separately from FBAR |
| Foreign corporation and ownership changes | Form 5471; R-ABROAD-CFC |
| Foreign funds, UCITS ETFs, insurance wrappers | Form 8621/PFIC classification; R-ABROAD-PFIC |
| Foreign trusts, gifts or inheritances | Forms 3520/3520-A; `us-foreign-trust-reporting`, R-ABROAD-GIFT |
| Foreign disregarded entity or partnership | Forms 8858/8865; `us-form-8865-foreign-partnership`, R-ABROAD-ENTITY |

Do not assume an information return is unnecessary because no income tax is owed. For example, a required Form 8938 can attract a USD 10,000 failure-to-file penalty; that is not a universal minimum for every form above. FBAR and Form 8938 are separate tests; filing Form 8938 does not discharge an otherwise required FBAR. [Form 8938 instructions, Penalties and Reporting](https://www.irs.gov/instructions/i8938).

Do not classify every foreign fund or wrapper as a PFIC, conclude every shareholder files annually, sell it or choose an election from this screening list. Likewise, do not assume a free-zone company creates deferral or apply a flat CFC inclusion. The PFIC, CFC and entity holds below must be resolved before investment or incorporation advice.

### 4. Check social security, states and retirement

FEIE does not reduce net earnings for self-employment tax. The ordinary components are 12.4% Social Security subject to its combined wage/earnings ceiling and 2.9% Medicare without that ceiling; Additional Medicare Tax may also apply. Compute the actual base and wage interaction in `us-schedule-c-and-se-computation`, not a flat percentage of gross receipts. [Publication 54, Effect of Exclusion](https://www.irs.gov/publications/p54); [IRS self-employment tax](https://www.irs.gov/businesses/small-businesses-self-employed/self-employment-tax-social-security-and-medicare-taxes).

Totalization agreements coordinate coverage; a certificate evidences the applicable system, not an elective exemption. Check the specific agreement and worker facts. The SSA's current agreement list does not include the UAE, so do not assume agreement relief for a Dubai freelancer. Do not infer employees have the same coverage as freelancers. [SSA agreement overview and country list](https://www.ssa.gov/international/agreements_overview.html); [Publication 54, chapters 2–3](https://www.irs.gov/publications/p54).

Collect state ties before drawing any state residence or part-year filing conclusion (R-ABROAD-STATE). Review US retirement accounts before a withdrawal: taxable early distributions before age 59½ can attract a 10% additional tax, subject to exceptions. IRA contribution compensation excludes FEIE/housing-excluded amounts; a joint-return spouse's compensation may matter. Do not infer that moving abroad alone requires liquidation or makes a Roth conversion cheap. Destination taxation, foreign pensions and Social Security benefits remain separate holds below. [IRS early distributions](https://www.irs.gov/taxtopics/tc558); [Publication 590-A, Compensation](https://www.irs.gov/publications/p590a).

### 5. Screen expatriation before renunciation or green card termination

For a citizen or long-term resident expatriating in 2026, apply the financial tests in the table and the separate five-year federal tax-compliance certification on Form 8854. Failure to certify makes the person covered regardless of those financial thresholds; a missing FBAR alone is not the Title 26 certification test. [26 USC 877(a)(2)](https://uscode.house.gov/us/usc/t26/s877/); [Form 8854 instructions](https://www.irs.gov/instructions/i8854).

The dual-at-birth exception requires continued citizenship and resident taxation in that same other country at expatriation, plus no more than 10 US-resident tax years under the substantial presence test in the 15 years ending with expatriation. The minor exception requires relinquishment before age 18½ and no more than 10 such US-resident years before relinquishment. These exceptions waive the financial tests, not the compliance certification. [Form 8854 instructions, Exceptions](https://www.irs.gov/instructions/i8854).

For covered expatriates, mark-to-market generally treats property as sold at fair market value the day before expatriation. Deferred compensation, specified tax-deferred accounts and nongrantor-trust interests have separate regimes. The gain reduction is not an exemption from all exit taxes, and gain character is asset-specific. Route valuation, allocation, special assets, section 2801 covered gifts/bequests, return status, consular mechanics and pre-exit gifts to R-ABROAD-EXIT; do not prescribe a universal gift-then-renounce sequence. [Form 8854 instructions, Taxation Under Section 877A](https://www.irs.gov/instructions/i8854).

## Boundary and exception table

| Situation | Action |
| --- | --- |
| Move on 1 July 2026 | A qualifying consecutive 12-month period may straddle years; establish tax home and foreign days, prorate the cap, and consider Form 2350 below. No automatic half-year entitlement |
| 329 full foreign days in every relevant 12-month period | Ordinary physical presence test fails; examine eligibility for bona fide residence or a specific waiver; no assumed relief |
| Dividends, gains or pensions only | No FEIE for those items; assess creditability and sourcing separately |
| Self-employed with foreign coverage certificate | Verify that the agreement actually assigns this work/period to the foreign system before excluding US coverage |
| Self-employed in the UAE | Apply ordinary US self-employment rules and any actual exemption; FEIE alone supplies none |
| Revoked FEIE for 2025 | 2026–2030 require IRS consent for re-election; 2031 is the sixth year |
| Green card kept after moving | Check continued status and any actual treaty termination; no residence change inferred from moving alone |
| Net worth exactly USD 2,000,000 | Financial test met; first check the dual/minor exceptions and certification |
| Non-US spouse or joint foreign account | Hold the section 6013(g), gift-splitting and separate FBAR analysis under R-ABROAD-TREATY/GIFT; do not infer one form's scope from another |

## Worked cases

Invented facts; retain 2026 throughout. These compare regular federal income tax only.

**Case 1, a decision: exclusion or credit for a single employee moving to Dubai.** Original facts: USD 200,000 of 2026 salary, no UAE income tax, physical presence test met and no other income. For this illustration also stipulate a foreign tax home and full-year qualifying foreign services, eligible timely FEIE election with no revocation bar, eligibility for the full USD 16,100 basic standard deduction, no related deduction adjustment, no housing claim, and no credits or other taxes being compared. Without FEIE, taxable income is 200,000 − 16,100 = USD 183,900. Under Rev. Proc. 2025-32 section 4.01 Table 3, tax is USD 36,734. With FEIE, taxable income is USD 51,000; stacking adds USD 132,900 for the rate calculation and subtracts tax of USD 24,494 on the excluded amount, leaving USD 12,240. Saving: USD 24,494. No foreign tax credit arises from the stipulated zero foreign tax. FEIE wins this bounded comparison; housing needs its own expense/location evidence. The original German high-tax alternative is conditional: an allowed credit sufficient to cover the applicable US income tax can reduce that tax to zero; location alone does not prove it. [Rates and deduction](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf); [stacking](https://uscode.house.gov/us/usc/t26/s911/).

```oa-check
name: Foreign earned income exclusion with the stacking rule, Dubai (2026)
inputs:
  salary: 200000
  standard_deduction: 16100
  exclusion: 132900
steps:
  - taxable_income: salary - standard_deduction
  - tax_no_exclusion: 0.10 * min(taxable_income, 12400) + 0.12 * max(min(taxable_income, 50400) - 12400, 0) + 0.22 * max(min(taxable_income, 105700) - 50400, 0) + 0.24 * max(min(taxable_income, 201775) - 105700, 0)
  - tax_on_excluded: 0.10 * min(exclusion, 12400) + 0.12 * max(min(exclusion, 50400) - 12400, 0) + 0.22 * max(min(exclusion, 105700) - 50400, 0) + 0.24 * max(min(exclusion, 201775) - 105700, 0)
  - tax_with_exclusion: tax_no_exclusion - tax_on_excluded
  - saving: tax_no_exclusion - tax_with_exclusion
expected:
  taxable_income: 183900.00
  tax_no_exclusion: 36734.00
  tax_on_excluded: 24494.00
  tax_with_exclusion: 12240.00
  saving: 24494.00
```

**Case 2: the exit gain reduction for a covered expatriate.** Preserve the US citizen's 2026 renunciation, USD 3,000,000 net worth and USD 1,500,000 built-in gain, with no deferred compensation, retirement accounts or trust interests. Stipulate that the renunciation date is after 1 January 2026 and later confirmed by a certificate of loss of nationality, with no earlier expatriation date; neither dual/minor exception applies. The net-worth test makes her covered. Assuming the stated gain is the properly computed mark-to-market gain for eligible assets, USD 1,500,000 − USD 910,000 = USD 590,000 remains for income-tax computation. This is gain, not USD 590,000 of tax; do not assume capital-gain character for unidentified assets. Allocation and actual return treatment go to `us-expatriation-exit-tax`. In the original alternative, USD 1,900,000 net worth, prior-five-year average net income tax below USD 211,000 and valid five-year tax-compliance certification mean she is not covered. [2026 amounts](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf); [Form 8854 instructions](https://www.irs.gov/instructions/i8854).

```oa-check
name: Section 877A exclusion for a covered expatriate (2026)
inputs:
  net_worth: 3000000
  built_in_gain: 1500000
  exclusion: 910000
  net_worth_test: 2000000
steps:
  - covered_by_net_worth: clamp(net_worth - net_worth_test + 1, 0, 1)
  - taxable_gain: max(built_in_gain - exclusion, 0) * covered_by_net_worth
expected:
  covered_by_net_worth: 1
  taxable_gain: 590000.00
```

## When to refuse or refer

Each unresolved outcome below is **non-usable**: do not implement it from this Guide. Each row's action is: **Check this point with one of our partner accountants.**

| Code | Point needing resolution | Action |
| --- | --- | --- |
| R-ABROAD-BACK | Missing returns, FBARs or information filings; delinquency/streamlined eligibility and form-specific penalty/defence computations | Check this point with one of our partner accountants. |
| R-ABROAD-PFIC | UCITS, Gulf funds, foreign insurance: PFIC classification, Form 8621 gateways/exceptions, default regime, elections and disposals; broker/product eligibility | Check this point with one of our partner accountants. |
| R-ABROAD-CFC | Foreign-company ownership/attribution, CFC/US-shareholder tests, subpart F, net CFC tested income, section 962, high-tax exclusion and check-the-box choice | Check this point with one of our partner accountants. |
| R-ABROAD-ENTITY | Foreign disregarded-entity/partnership classification and Forms 8858/8865 filing categories | Check this point with one of our partner accountants. |
| R-ABROAD-PENSION | UK SIPP, German company pension, Swiss pillars and insurance: treaty treatment, contributions, growth, trust/PFIC classification, US plan withdrawals and Roth conversions | Check this point with one of our partner accountants. |
| R-ABROAD-EXIT | Valuation, special assets, exact expatriation date, Form 8854/final-return status, consular procedure/fee, pre-exit gifts and section 2801 covered gifts/bequests | Check this point with one of our partner accountants. |
| R-ABROAD-STATE | California, Virginia, South Carolina, New Mexico or other state residence, domicile, voting, tie changes, no-tax-state pit stop, filing and record period | Check this point with one of our partner accountants. |
| R-ABROAD-TREATY | Treaty nonresidence, Form 8833 and exceptions, non-US-spouse section 6013(g) election and independent FBAR consequences | Check this point with one of our partner accountants. |
| R-ABROAD-GIFT | Foreign gifts/inheritances, donor aggregation, foreign corporation/partnership thresholds, noncitizen-spouse gifts and gift splitting | Check this point with one of our partner accountants. |
| R-ABROAD-SOCIAL | Employee coverage, certificate disputes, combining benefit credits, payments abroad and the individual's earnings/benefit history | Check this point with one of our partner accountants. |
| R-ABROAD-SPECIAL | FEIE late elections, adverse-condition waivers, combat-zone exception, special income/territories and uncertain foreign tax creditability | Check this point with one of our partner accountants. |

## Filing and payment

For a calendar-year 2026 Form 1040 filer, the regular deadline is 15 April 2027. The automatic two-month filing/payment extension to **15 June 2027** requires that, on the regular due date, the citizen/resident lives outside the US and Puerto Rico and has a main business/post of duty outside both, or is on military/naval duty outside both. Attach the statement explaining qualification. Interest still runs from 15 April. A qualifying joint-return spouse can qualify the joint return; separate filers qualify separately. Timely Form 4868 by 15 June can extend filing to **15 October 2027**, without extending payment beyond June. These are ordinary-rule dates, subject to applicable special relief. [Publication 54, Extensions](https://www.irs.gov/publications/p54).

If the first-year residence/presence test is not met by the filing deadline, apply for Form 2350 relief before that due date, or file without the exclusion and amend after qualifying. Form 2350 is not itself proof of qualification or relief from interest. [2026 Form 2555 instructions, When To File](https://www.irs.gov/instructions/i2555). Calendar each information form separately. Use the return/estimates and expatriation destinations above; do not assume every expatriate files a final dual-status return.

## Completion checklist

- [ ] Status, tax home, travel days, income/work locations and foreign tax evidence recorded.
- [ ] FEIE/housing and credit compared, election history checked, excluded-income tax removed from credit.
- [ ] Each account, fund, entity, trust, gift and form independently screened; holds remain non-usable.
- [ ] Actual social security coverage, state position and retirement consequences resolved before advice.
- [ ] Expatriation tests/exceptions, five-year certification and asset regimes reviewed if relevant.
- [ ] Filing/payment calendar and required extension statement prepared; original cases adapted only to documented facts.

## Sources

| Official source and operative scope | URL | Read on |
| --- | --- | --- |
| Read for Rev. Proc. 2025-32, sections 4.01/Table 3, 4.14, 4.37–4.39: 2026 rates, deduction, expatriation and FEIE amounts | https://www.irs.gov/pub/irs-drop/rp-25-32.pdf | 2026-11-27 |
| Read for 26 USC 911(b)–(f): qualified income/person, housing, double benefits, election and stacking | https://uscode.house.gov/us/usc/t26/s911/ | 2026-11-27 |
| Read for 2026 Form 2555 instructions: qualification, housing, election and first-year filing | https://www.irs.gov/instructions/i2555 | 2026-11-27 |
| Read for Publication 54 (2025 edition): general filing, extensions, social security and self-employment rules; its old annual figures are not used as 2026 amounts | https://www.irs.gov/publications/p54 | 2026-11-27 |
| Read for Form 1116 instructions (2025): ordinary credit conditions and carryovers, not a verified 2026 line map | https://www.irs.gov/instructions/i1116 | 2026-11-27 |
| Read for IRS foreign tax credit: qualified taxes, limitations and exclusions | https://www.irs.gov/individuals/international-taxpayers/foreign-tax-credit | 2026-11-27 |
| Read for Form 8938 instructions: independent FBAR obligation and penalty example | https://www.irs.gov/instructions/i8938 | 2026-11-27 |
| Read for IRS self-employment tax: component rates, ceiling interaction and Additional Medicare Tax | https://www.irs.gov/businesses/small-businesses-self-employed/self-employment-tax-social-security-and-medicare-taxes | 2026-11-27 |
| Read for SSA agreement overview: operative coverage framework and country list | https://www.ssa.gov/international/agreements_overview.html | 2026-11-27 |
| Read for Topic 558: early-distribution additional tax and exceptions | https://www.irs.gov/taxtopics/tc558 | 2026-11-27 |
| Read for Publication 590-A (2025): IRA compensation rule, not annual contribution limits | https://www.irs.gov/publications/p590a | 2026-11-27 |
| Read for 26 USC 877(a)(2) and Form 8854 instructions (2025): tests, certification, exceptions, status and asset regimes; 2026 indexed amounts come from Rev. Proc. 2025-32 | https://uscode.house.gov/us/usc/t26/s877/ ; https://www.irs.gov/instructions/i8854 | 2026-11-27 |

Not yet confirmed: individual outcomes remain non-usable under the referral table. No 2026 Form 8854 or Form 1116 layout, current consular fee, universal banking acceptance policy or individualized treaty result is asserted.
