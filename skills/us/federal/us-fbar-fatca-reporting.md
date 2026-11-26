---
name: us-fbar-fatca-reporting
description: "Decide whether a US person must file an FBAR (FinCEN Form 114), a Form 8938 (FATCA, IRC section 6038D), both or neither for calendar and tax year 2026. Covers the FBAR aggregate test (more than USD 10,000 at any time), the Form 8938 thresholds for people living in the US and abroad, what each regime counts, signature authority and its exceptions, due dates, the FBAR and Form 8938 penalties, the assessment periods, and the late-filing and Streamlined routes. Trigger on FBAR, FinCEN 114, Form 8938, FATCA, foreign bank account reporting, specified foreign financial assets. Produces a working paper and a reviewer brief, not a filed report. Load alongside cross-border-tax-workflow-base."
version: "1.1"
jurisdiction: US
tax_year: 2026
last_updated: 2026-11-26
depends_on:
  - cross-border-tax-workflow-base
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: cross-border
type: situation-rules
---

# US foreign account and asset reporting: FBAR (FinCEN Form 114) and Form 8938 (FATCA), tax year 2026

**Answer first.** Test FBAR and Form 8938 separately. Filing one does not satisfy the other ([Form 8938 instructions](https://www.irs.gov/instructions/i8938)). This Guide screens calendar/tax year 2026 and retains a dated 2025 filing note. Load `cross-border-tax-workflow-base`; produce an asset schedule and reviewer brief. Do not file, certify intent or claim professional approval from this working paper.

## Scope and who this is for

FBAR covers US citizens, residents under its own definition, and entities formed under US federal, state, territorial or tribal law, including corporations, partnerships, LLCs and trusts ([31 CFR 1010.350(b)](https://www.ecfr.gov/current/title-31/section-1010.350)). Income-tax disregard does not itself remove an entity's FBAR duty ([FinCEN instructions](https://www.fincen.gov/system/files/shared/FBAR%20Line%20Item%20Filing%20Instructions.pdf)).

Form 8938 requires a specified person with an interest in specified foreign financial assets over the applicable threshold, unless an exception applies. A US citizen is a specified individual. If no annual income tax return is required, no Form 8938 is required even above the threshold ([instructions, Who Must File](https://www.irs.gov/instructions/i8938)). Resident/electing/partial-year/dual-resident individuals and specified domestic entities need the separate review below; FBAR status alone does not settle Form 8938 status.

## Ask the client first

Read the existing working paper and records before requesting missing facts. Obtain status separately for each regime, filing status, return requirement, foreign tax home and residence/presence evidence. List every account and non-account asset, legal title, beneficial ownership, signing powers, institution location, annual maximum and year-end value in original currency, statements, transfers between accounts, and sourced currency conversions. Capture employer regulatory/listing status, spouses' holdings, trusts, pensions, insurance, other information returns, prior filings and any authority contact. Do not assume missing returns were filed or missing values are zero.

## The method, step by step

1. Establish each regime's person, ownership and exemption conditions separately.
2. **FBAR:** a US person with financial interest or signature authority over reportable foreign accounts files if aggregate annual account maxima exceed USD 10,000. The maxima need not coincide. Reconcile transfers: money moved between foreign accounts is counted only once in the aggregate test. Exactly USD 10,000 does not exceed it. Once required, include every reportable account, including small accounts ([FinCEN instructions](https://www.fincen.gov/system/files/shared/FBAR%20Line%20Item%20Filing%20Instructions.pdf); [IRM 4.26.16.2.6](https://www.irs.gov/irm/part4/irm_04-026-016)).
3. **Form 8938:** build last-day and maximum-value schedules under the valuation rules below and apply the appropriate threshold pair. Use supported asset valuations rather than an assumed simultaneous portfolio peak. Do not treat Form 8938 assets as an automatic superset of FBAR accounts.
4. Map holdings to both regimes, document exceptions and unresolved classifications, then set the applicable filing dates. Missing status, values, exchange rates or exception evidence leaves the conclusion on hold; do not invent a filing requirement or exemption.

### Rates, bands and thresholds

All Form 8938 rows require the person/interest/return gateway and applicable exceptions. These continuous-use thresholds apply to 2025 and 2026; they are strict “more than” tests.

| Individual's position | Last day of tax year | Any time during tax year | Official source |
| --- | --- | --- | --- |
| Unmarried, US thresholds | USD 50,000 | USD 75,000 | [Instructions, US unmarried](https://www.irs.gov/instructions/i8938) |
| Married filing separately, US thresholds | USD 50,000 | USD 75,000 | [Instructions, US separate return](https://www.irs.gov/instructions/i8938) |
| Married filing jointly, US thresholds | USD 100,000 | USD 150,000 | [Instructions, US joint return](https://www.irs.gov/instructions/i8938) |
| Unmarried or married filing separately, qualifying abroad | USD 200,000 | USD 300,000 | [Instructions, outside US](https://www.irs.gov/instructions/i8938) |
| Married filing jointly, qualifying abroad | USD 400,000 | USD 600,000 | [26 CFR 1.6038D-2(a)(4)](https://www.ecfr.gov/current/title-26/section-1.6038D-2) |

Qualifying abroad requires a foreign tax home and either US-citizen bona fide foreign residence for an uninterrupted period including an entire tax year, or US-citizen/resident presence in foreign countries for at least 330 full days in 12 consecutive months ending in the reporting year ([instructions, Presence abroad](https://www.irs.gov/instructions/i8938)). For a joint return the regulation permits the higher thresholds when a qualified individual under section 911(d)(1) and that individual's spouse file jointly; it does not require both spouses independently to qualify ([26 CFR 1.6038D-2(a)(4)](https://www.ecfr.gov/current/title-26/section-1.6038D-2)).

### Accounts, assets and valuation

| Situation | FBAR | Form 8938 | Official source |
| --- | --- | --- | --- |
| Ordinary bank or securities account at a foreign financial institution | Apply financial-interest/signature gateway | Apply interest and asset gateway | [31 CFR 1010.350](https://www.ecfr.gov/current/title-31/section-1010.350); [instructions](https://www.irs.gov/instructions/i8938) |
| Foreign branch of a US bank | Foreign account by location | Account maintained by a US payer is excluded | [FinCEN instructions](https://www.fincen.gov/system/files/shared/FBAR%20Line%20Item%20Filing%20Instructions.pdf); [instructions, Certain Financial Accounts](https://www.irs.gov/instructions/i8938) |
| US branch of a foreign bank | Not a foreign account by location | Apply US-payer account exclusion | [FinCEN instructions](https://www.fincen.gov/system/files/shared/FBAR%20Line%20Item%20Filing%20Instructions.pdf); [instructions](https://www.irs.gov/instructions/i8938) |
| Foreign-issuer shares held for investment outside any financial account | Direct share certificates are not financial accounts | Specified foreign financial assets | [31 CFR 1010.350(c)](https://www.ecfr.gov/current/title-31/section-1010.350); [instructions, Other Specified Foreign Financial Assets](https://www.irs.gov/instructions/i8938) |
| Mere signature authority | Can trigger FBAR, subject to exceptions | Does not by itself establish an interest | [31 CFR 1010.350(f)](https://www.ecfr.gov/current/title-31/section-1010.350); [instructions, Interests](https://www.irs.gov/instructions/i8938) |

Legal title or record ownership may create FBAR financial interest even for someone else's benefit. Signature authority means control of disposition by direct communication with the institution, alone or jointly ([31 CFR 1010.350(e)(1), (f)(1)](https://www.ecfr.gov/current/title-31/section-1010.350)). Foreign cash-value insurance/annuity accounts and public pooled funds with regular NAV determination and redemptions can be FBAR accounts; actual classifications remain review items ([31 CFR 1010.350(c)(3)](https://www.ecfr.gov/current/title-31/section-1010.350)).

Form 8938 interest generally means income, gains, losses, deductions, credits, gross proceeds or distributions are or would be reflected on the person's return, even if none arise this year. Financial-institution accounts and investment-held non-account foreign stock, entity interests and qualifying instruments/contracts are included. Assets inside an account are reflected in the account value ([instructions, Specified Foreign Financial Assets and Interests](https://www.irs.gov/instructions/i8938); [26 CFR 1.6038D-5(e)](https://www.ecfr.gov/current/title-26/section-1.6038D-5)).

- **FBAR valuation:** determine each annual maximum in its account currency, then convert at the reporting calendar year's last-day Treasury rate, even if closed earlier. If unavailable, use another verifiable rate and document its source. Periodic statements are acceptable only if they fairly reflect the annual maximum ([FinCEN instructions](https://www.fincen.gov/system/files/shared/FBAR%20Line%20Item%20Filing%20Instructions.pdf)).
- **Form 8938 valuation:** generally fair market value; maximum means a reasonable estimate of the year's maximum. Use last-day tax-year Treasury USD-purchase rates even for assets disposed of earlier; if none is available, another public rate with source disclosed. Annual-or-more-frequent account statements, including their currency conversion, may be used unless known or readily accessible facts show an unreasonable maximum estimate. Non-account investment assets may generally use the value on the last day the person held an interest, unless known/readily accessible information makes that an unreasonable maximum estimate. Special trust/pension rules are held below ([26 CFR 1.6038D-5](https://www.ecfr.gov/current/title-26/section-1.6038D-5)).
- **Form 8938 joint assets:** for threshold testing, joint filers count a spousal joint asset once; separate filers who are both specified individuals count half. A separate filer whose spouse is not a specified individual counts the whole asset, as do other joint owners. When reporting is required, report the entire joint asset value, including on each spouse's separate Form 8938 ([26 CFR 1.6038D-2(c), (d)](https://www.ecfr.gov/current/title-26/section-1.6038D-2)).

No final 2026 foreign-currency totals are supplied here. Keep the rate and rate-date evidence with the schedule; do not substitute a quarterly draft rate for the required year-end rate.

## Worked cases

The original 2026 inputs below are preserved. Filing results are conditional on the person, interest, complete-holdings, return and exemption gateways above; no missing eligibility fact is supplied. The `oa-check` blocks recompute whole-dollar threshold screens, not authorization to file. `clamp(value - threshold, 0, 1)` is unsuitable as a general cents-level Boolean test.

**Case A: small accounts add up.** Unmarried US resident; 2026 account maxima USD 4,000, USD 3,500 and USD 3,000; year-end total well below USD 50,000; no other foreign assets. Sum USD 10,500 exceeds USD 10,000. Subject to transfer reconciliation and exemptions, FBAR required for all three accounts. The Form 8938 US-unmarried thresholds are not met on these values ([FinCEN instructions](https://www.fincen.gov/system/files/shared/FBAR%20Line%20Item%20Filing%20Instructions.pdf); [Form 8938 instructions](https://www.irs.gov/instructions/i8938)). The earliest version's separate illustration, five accounts of USD 3,000 each, totals USD 15,000; apply the same transfer/exemption qualifications.

**Case B: exactly at the line.** Same person, but the original highest combined daily balance was exactly USD 10,000. That alone does not establish the aggregate of the accounts' individual annual maxima. If the properly reconciled annual-maxima aggregate is also exactly USD 10,000, the FBAR threshold is not met. Otherwise recompute it; a simultaneous peak alone does not clear the person ([FinCEN instructions](https://www.fincen.gov/system/files/shared/FBAR%20Line%20Item%20Filing%20Instructions.pdf)).

**Case C: couple abroad, both threshold schedules.** Married filing jointly; German tax home; both bona fide residents for all of 2026; joint foreign accounts USD 350,000 at year-end and USD 450,000 highest in the year. The original inputs do not establish citizenship, complete asset maxima or all exemptions. Conditionally using the qualifying-abroad joint tier, the stated values leave USD 50,000/150,000 headroom. Using US joint thresholds they exceed both lines. The regulation does not require both spouses to qualify abroad. FBAR's USD 10,000 threshold is crossed by the stated account value, subject to each person's status and applicable filing exceptions. Spouse-only filing and final Form 8938 eligibility: Check this point with one of our partner accountants. Sources: [FinCEN](https://www.fincen.gov/system/files/shared/FBAR%20Line%20Item%20Filing%20Instructions.pdf), [26 CFR 1.6038D-2(a)](https://www.ecfr.gov/current/title-26/section-1.6038D-2).

```oa-check
name: Couple abroad, FBAR and Form 8938 both ways (2026)
inputs:
  year_end_value: 350000
  max_value: 450000
  fbar_threshold: 10000
  abroad_last_day: 400000
  abroad_any_time: 600000
  us_last_day: 100000
  us_any_time: 150000
steps:
  - fbar_required: clamp(max_value - fbar_threshold, 0, 1)
  - f8938_abroad: max(clamp(year_end_value - abroad_last_day, 0, 1), clamp(max_value - abroad_any_time, 0, 1))
  - f8938_if_in_us: max(clamp(year_end_value - us_last_day, 0, 1), clamp(max_value - us_any_time, 0, 1))
  - headroom_last_day: abroad_last_day - year_end_value
  - headroom_any_time: abroad_any_time - max_value
expected:
  fbar_required: 1
  f8938_abroad: 0
  f8938_if_in_us: 1
  headroom_last_day: 50000
  headroom_any_time: 150000
```

**Case D: share certificates.** Unmarried US resident; foreign-issuer share certificates USD 80,000 all year; no foreign accounts. Direct shares do not create an FBAR account. If investment-held and the Form 8938 gateway is satisfied, USD 80,000 exceeds both US-unmarried thresholds and Form 8938 is required. Investment purpose and eligibility must be established ([instructions](https://www.irs.gov/instructions/i8938); [31 CFR 1010.350(c)](https://www.ecfr.gov/current/title-31/section-1010.350)).

**Case E: employee signer.** US employee of a US operating company can instruct payments from its foreign bank account, owns none of it. Capture bank/SEC/CFTC/Authorized Service Provider status, US exchange listing or section 12(g) registration, US-parent/subsidiary/consolidated facts and any covered signature-only notice. Employer exception and extension eligibility: Check this point with one of our partner accountants. Mere signing power does not establish Form 8938 interest; no ownership does not by itself prove absence of every interest ([instructions, Interests](https://www.irs.gov/instructions/i8938)).

**Case F: one late FBAR, five accounts, stipulated non-willful reporting violation.** One non-willful reporting violation yields one reporting penalty, rather than five account penalties ([IRM 4.26.16.5.2](https://www.irs.gov/irm/part4/irm_04-026-016)). The original USD 16,536 figure belongs to the assessment-date regime below; it is not a predicted penalty for a 2026 report assessed later. Intent, defenses and actual amount: Check this point with one of our partner accountants.

**Case G: last-day test.** Unmarried US resident; 2026 account maxima USD 4,000/3,500/3,000, year-end USD 2,500/3,000/1,500, foreign-issuer share certificates USD 45,000 on 31 December 2026; no information that their annual high differed. Account maxima sum USD 10,500; FBAR threshold crossed subject to transfers and exceptions. Last-day account total USD 7,000 plus shares USD 45,000 is USD 52,000, exceeding USD 50,000. If investment-held and the other gateways apply, that alone triggers Form 8938. USD 55,500 is only the original arithmetic using USD 45,000 for shares, not a proven annual-maximum total. Apply the reasonable-estimate/readily-accessible-information rule before reporting the share maximum; an unknown high is not a verified high. Sources: [FinCEN](https://www.fincen.gov/system/files/shared/FBAR%20Line%20Item%20Filing%20Instructions.pdf), [instructions](https://www.irs.gov/instructions/i8938), [26 CFR 1.6038D-5(f)](https://www.ecfr.gov/current/title-26/section-1.6038D-5).

```oa-check
name: Accounts plus shares outside an account, unmarried US resident (2026)
inputs:
  acct1_max: 4000
  acct2_max: 3500
  acct3_max: 3000
  acct1_ye: 2500
  acct2_ye: 3000
  acct3_ye: 1500
  shares: 45000
  fbar_threshold: 10000
  last_day_threshold: 50000
  any_time_threshold: 75000
steps:
  - fbar_aggregate: acct1_max + acct2_max + acct3_max
  - fbar_required: clamp(fbar_aggregate - fbar_threshold, 0, 1)
  - f8938_last_day_total: acct1_ye + acct2_ye + acct3_ye + shares
  - f8938_any_time_total: fbar_aggregate + shares
  - last_day_met: clamp(f8938_last_day_total - last_day_threshold, 0, 1)
  - any_time_met: clamp(f8938_any_time_total - any_time_threshold, 0, 1)
  - f8938_required: max(last_day_met, any_time_met)
expected:
  fbar_aggregate: 10500
  fbar_required: 1
  f8938_last_day_total: 52000
  f8938_any_time_total: 55500
  last_day_met: 1
  any_time_met: 0
  f8938_required: 1
```

## Filing and payment

FBAR is filed electronically through FinCEN's BSA E-Filing System, separately from the income return, unless FinCEN has granted an e-filing exception ([IRM 4.26.16.3.1](https://www.irs.gov/irm/part4/irm_04-026-016)). Ordinary calendar-2026 dates are 15 April 2027 and automatic extension to 15 October 2027, with no extension request. Specific relief must be considered separately ([FinCEN instructions](https://www.fincen.gov/system/files/shared/FBAR%20Line%20Item%20Filing%20Instructions.pdf)).

Attach Form 8938 to the annual return by that return's due date, including extensions; do not use the FBAR extension as a return extension ([instructions, When and How To File](https://www.irs.gov/instructions/i8938)). The original calendar-1040 illustrations, 15 April 2027 and extended 15 October 2027, are not an eligibility determination for special overseas/other filing dates: Check this point with one of our partner accountants. Track income-tax computation/payment separately in `cross-border-tax-workflow-base`.

FBAR records contain account name/designation, institution name/address, type and maximum value. Retain five years and keep available for inspection; exclude the specified false/fraudulent-income-return or nonfiling criminal-proceeding period from counting those five years ([31 CFR 1010.420](https://www.ecfr.gov/current/title-31/section-1010.420)). Exact retention start dates, employee record exceptions, signed Form 114a authorization/retention, professional BSA registration and amended-FBAR prior-identifier steps: Check this point with one of our partner accountants.

### Penalties and assessment periods

These are ceilings and rules, not automatic assessments; FBAR examiners have discretion and there is no floor ([IRM 4.26.16.5.2.1](https://www.irs.gov/irm/part4/irm_04-026-016)).

| Rule | Amount and operative conditions | Official source |
| --- | --- | --- |
| FBAR non-willful statutory ceiling, before inflation replacement | USD 10,000 | [31 USC 5321(a)(5)(B)](https://uscode.house.gov/us/usc/119-124/t31/s5321/) |
| FBAR willful statutory ceiling, before inflation replacement | Greater of USD 100,000 or 50% of account balance at violation; ceiling, not minimum | [31 USC 5321(a)(5)(C), (D)](https://uscode.house.gov/us/usc/119-124/t31/s5321/) |
| FBAR adjusted non-willful ceiling; penalties assessed on or after 17 January 2025, violations after 2 November 2015 | USD 16,536 per non-willful reporting violation | [31 CFR 1010.821](https://www.ecfr.gov/current/title-31/section-1010.821); [IRM applicability](https://www.irs.gov/irm/part4/irm_04-026-016) |
| FBAR adjusted willful dollar ceiling; same assessment/violation-date conditions | Greater of USD 165,353 or 50% of violation-date account balance | [31 CFR 1010.821](https://www.ecfr.gov/current/title-31/section-1010.821); [31 USC 5321](https://uscode.house.gov/us/usc/119-124/t31/s5321/); [IRM applicability](https://www.irs.gov/irm/part4/irm_04-026-016) |
| Form 8938 incomplete/incorrect or late filing when required | USD 10,000 | [Instructions, Penalties](https://www.irs.gov/instructions/i8938) |
| Form 8938 continuing failure after 90 days from mailed IRS notice | Additional USD 10,000 per 30-day period or part, maximum USD 50,000 additional; USD 60,000 combined (computed) | [Instructions, Continuing failure](https://www.irs.gov/instructions/i8938) |
| Tax underpayment from transaction involving undisclosed specified foreign financial asset | May attract 40% of that underpayment | [Instructions, Underpayment](https://www.irs.gov/instructions/i8938) |

Single willful reporting violations can yield account-by-account penalties; single non-willful reporting violations yield a single penalty ([IRM 4.26.16.5.2](https://www.irs.gov/irm/part4/irm_04-026-016)). The adjusted dollar figures above preserve their original assessment-year conditions. Do not carry them into a later assessment year without checking the applicable adjustment.

A section 6038D information failure keeps assessment open until at least three years after the required information is furnished. Reasonable cause and no willful neglect limit this extension to related items. Separately, more than USD 5,000 omitted gross income attributable to the specified foreign assets can allow six years after return filing, ignoring section 6038D thresholds and exceptions. Adequately disclosed omitted items are excluded from this omission calculation, except the statutory basis-overstatement case ([26 USC 6501(c)(8), (e)(1)(A)(ii), (B)(iii)](https://uscode.house.gov/us/usc/119-124/t26/s6501/)).

The ordinary FBAR civil assessment period is six years from the transaction/violation ([31 USC 5321(b)(1)](https://uscode.house.gov/us/usc/119-124/t31/s5321/)). Computing the actual violation date, tolling/consent or expiry, including the former April/October shorthand: Check this point with one of our partner accountants.

### 2025 reports: dated note, 26 November 2026

Ordinary calendar-2025 FBAR dates were 15 April 2026 and automatic 15 October 2026; the latter has passed. Do not infer every filer is late without checking specific relief ([FinCEN instructions](https://www.fincen.gov/system/files/shared/FBAR%20Line%20Item%20Filing%20Instructions.pdf)). FIN-2025-NTC3 extends covered signature-authority reporting during 2025 and earlier specified notice periods to 15 April 2027. It concerns individuals within the earlier notices, not every employee with no financial interest ([notice, both pages](https://www.fincen.gov/system/files/2025-12/FBAR-FBAR-Filing-Requirement-for-Certain-Financial-Professionals.pdf)). Application of the incorporated notice conditions and any 2026-calendar-year special extension: Check this point with one of our partner accountants.

Form 8938 follows the 2025 return's applicable filing deadline, including extensions. The original extended individual-return illustration was 15 October 2026. Correcting a return already filed without Form 8938, and determining special-date relief: Check this point with one of our partner accountants. The threshold table above also applies to 2025; do not replace those historical inputs with 2026-report dates.

## When to refuse or refer

Each row is an explicit hold: no filing exemption, special valuation, remedy or penalty defense is authorized for that point.

| Topic retained from the earlier Guide | Action |
| --- | --- |
| Indirect corporate/partnership/entity ownership, more-than-50% tests, grantor trusts, beneficiary/current-income tests and entity-held accounts/assets | Check this point with one of our partner accountants. |
| Employee exceptions: regulated bank, SEC/CFTC institution, Authorized Service Provider, listed/section-12(g) entity or US subsidiary/consolidated FBAR | Check this point with one of our partner accountants. |
| FBAR correspondent/nostro, government/international institution, military-facility accounts; US retirement/IRA, consolidated, spouse-only and trust-beneficiary filing exceptions | Check this point with one of our partner accountants. |
| Specified domestic entities, their former USD 50,000/75,000 threshold illustration, passive tests/aggregation; resident/electing/dual-resident and partial-year Form 8938, Forms 1040-NR/8833 | Check this point with one of our partner accountants. |
| Foreign pensions, trusts, estates and deferred compensation; distribution-based/zero valuation; no automatic zero for missing records | Check this point with one of our partner accountants. |
| Partnership/private fund/mutual fund and cash-value policy classification; direct versus entity-held real estate/currency/metals/tangibles; foreign social-security versus private-plan benefits | Check this point with one of our partner accountants. |
| Duplicative reporting on Forms 3520, 3520-A, 5471, 8621, 8865 and Part IV; individual/entity threshold-counting differences; Rev. Proc. 2020-17 | Check this point with one of our partner accountants. |
| Willfulness, reasonable cause, balance correction, foreign secrecy laws, joint/several Form 8938 penalties, IRS value presumption, criminal exposure and actual penalty defenses | Check this point with one of our partner accountants. |
| Late FBAR/DFSP, IRS contact/examination/investigation, income reporting/payment, Streamlined Domestic/Foreign and VDP selection, non-willful certification, eligibility, look-back periods and relief | Check this point with one of our partner accountants. |
| Historical Streamlined figures: 5% affected-asset penalty, 3 tax years/6 FBAR years, and 330-day/one-of-three-year foreign non-residency shorthand; none establishes eligibility or a computed liability here | Check this point with one of our partner accountants. |

Financial interest in 25 or more accounts, or signature authority over 25 or more accounts, can modify required FBAR detail; full information remains available on request ([31 CFR 1010.350(g)(1), (2)](https://www.ecfr.gov/current/title-31/section-1010.350)). Applying this rule to mixed ownership/signature categories: Check this point with one of our partner accountants.

Preserved routing: trusts and Forms 3520/3520-A/gifts → `us-foreign-trust-reporting`; CFC/Form 5471 → `us-form-5471-cfc-information`; partnerships/Form 8865 → `us-form-8865-foreign-partnership`; foreign-owned US entities/Form 5472 → `us-form-5472-foreign-owned-us`; FEIE/housing → `us-foreign-earned-income-2555`; FTC → `us-foreign-tax-credit-1116`; nonresident/dual-status returns → `us-form-1040-nr-nonresident-return`. These are topic routes, not findings that a form is required or that a destination resolves every held issue.

## Completion checklist

- [ ] Document separate person, asset, ownership and exception tests; retain original case years and inputs.
- [ ] Reconcile transfers and supported maxima; record year-end currency rate and source.
- [ ] Test both Form 8938 thresholds under the correct qualified-person rules.
- [ ] Document each account/asset's reporting destination, dates, prior-year gaps and explicit holds.
- [ ] Give the accountant the schedule, source citations and unresolved facts; never infer intent or sign the person's certification.

This is general educational information, not a signed opinion or filing. A practitioner applying it must evaluate the actual facts, assumptions and law under Circular 230 section 10.37.

## Sources

Exact applicable official-source reads completed for the separate FBAR/Form 8938 proof were reused on 26 November 2026; changed valuation, joint-abroad and notice dependencies were read separately. Referral topics are non-usable holds, not proven exceptions.

| Official source and scope used | URL | Read on |
| --- | --- | --- |
| FinCEN FBAR instructions, read for gateway, annual maxima, location, FX, ordinary dates | https://www.fincen.gov/system/files/shared/FBAR%20Line%20Item%20Filing%20Instructions.pdf | 2026-11-26 |
| IRS Form 8938 continuous-use instructions, read for gateway, thresholds, interests, US-payer exclusion, filing and penalties | https://www.irs.gov/instructions/i8938 | 2026-11-26 |
| 31 CFR 1010.350, read for persons, accounts, title/signature and modified detail | https://www.ecfr.gov/current/title-31/section-1010.350 | 2026-11-26 |
| 26 CFR 1.6038D-2, read for joint-abroad threshold and joint ownership | https://www.ecfr.gov/current/title-26/section-1.6038D-2 | 2026-11-26 |
| 26 CFR 1.6038D-5, read for valuation and currency conditions | https://www.ecfr.gov/current/title-26/section-1.6038D-5 | 2026-11-26 |
| IRM 4.26.16, read for transfer reconciliation, electronic filing, penalty unit/discretion and inflation applicability | https://www.irs.gov/irm/part4/irm_04-026-016 | 2026-11-26 |
| 31 CFR 1010.420, read for records and criminal-proceeding exclusion | https://www.ecfr.gov/current/title-31/section-1010.420 | 2026-11-26 |
| 31 CFR 1010.821, read for assessment-dated adjusted ceilings | https://www.ecfr.gov/current/title-31/section-1010.821 | 2026-11-26 |
| 31 USC 5321, read for statutory ceilings and assessment period | https://uscode.house.gov/us/usc/119-124/t31/s5321/ | 2026-11-26 |
| 26 USC 6501, read for information-failure and omitted-income assessment rules | https://uscode.house.gov/us/usc/119-124/t26/s6501/ | 2026-11-26 |
| FIN-2025-NTC3, read for 2025/prior-notice-period extension; individual eligibility held | https://www.fincen.gov/system/files/2025-12/FBAR-FBAR-Filing-Requirement-for-Certain-Financial-Professionals.pdf | 2026-11-26 |
| Circular 230 section 10.37, read for practitioner written-advice standard | https://www.irs.gov/pub/irs-pdf/pcir230.pdf | 2026-11-26 |

Not yet confirmed: the applications expressly held above, including special status, employer/notice eligibility, pensions, entity/trust look-through, remediation and assessment expiry. No 2026 year-end currency rate or future assessment-year penalty adjustment is assumed. These points are not usable filing conclusions.
