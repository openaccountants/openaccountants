---
name: us-expatriation-exit-tax
description: US federal expatriation tax for citizens relinquishing citizenship and long-term residents ending green-card status in 2026, with explicit 2025 comparisons. Covers covered-expatriate tests, exceptions, valuation, mark-to-market gain, deferred compensation, tax-deferred accounts, trusts, Form 8854, Form W-8CE and section 2801/Form 708. Trigger on renounce citizenship, exit tax, expatriation tax, covered expatriate, long-term resident, Form 8854, Form 708 and section 877A. Produces a working paper and reviewer brief, not a filed return.
version: "1.1"
jurisdiction: US
tax_year: 2026
last_updated: 2026-11-27
depends_on:
  - cross-border-tax-workflow-base
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
---

# US expatriation and the exit tax (section 877A), tax year 2026

**Answer first.** Determine the expatriation date and covered status before planning disposals. In 2026 the three tests are average prior-five-year net income tax **more than USD 211,000**, net worth **USD 2,000,000 or more**, or failure to certify five years of federal tax compliance. The dual-citizen and minor exceptions below affect only the first two tests. Covered expatriates apply the deemed-sale regime, with a **USD 910,000** exclusion, to other property; pensions, specified accounts and nongrantor trusts have separate rules. [Rev. Proc. 2025-32 §§4.37–4.38](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf); [26 USC 877A](https://uscode.house.gov/us/usc/t26/s877a/).

## Scope and who this is for

US citizens who relinquish citizenship and long-term residents (LTRs) who cease lawful permanent residence, on or after 17 June 2008. This Guide uses 2026 figures and labels the retained 2025 comparison separately. A green-card holder outside the LTR definition is outside section 877A. [26 USC 877A(g), effective-date note](https://uscode.house.gov/us/usc/t26/s877a/).

Routing: `cross-border-tax-workflow-base` and `cross-border-tax-router` for the residency map; `us-tax-residency` for other green-card holders and residency ending dates; `us-capital-gains` for rates; `us-form-1040-nr-nonresident-return` for the return; `us-citizen-moving-abroad-tax` for living abroad; `us-fbar-and-fatca-8938` for foreign reporting; `us-foreign-trust-reporting` for trusts; `us-estate-gift-706-709` for estate and gift returns. State tax, immigration steps and pre-17-June-2008 cases need separate advice: Check this point with one of our partner accountants.

## Ask the client first

Obtain citizenships and how/when acquired, birth date, CLN and qualifying-act dates, green-card issue/termination evidence, I-407, final orders and appeals, treaty claims/notices/waivers, and US residence years under the substantial presence test. Obtain the five prior years' federal returns, tax/interest/penalty payments and information returns, plus the FBAR record separately. Request worldwide assets, liabilities, FMV and basis, pensions, deferred compensation, unvested equity, partnerships and trusts; significant prior gifts and changes in net worth; arrival-date asset values; planned US gifts/heirs; and W-8CE delivery evidence. Do not invent missing facts or make a final non-covered determination before documenting the certification. [Form 8854 instructions, Parts I–II](https://www.irs.gov/instructions/i8854).

## The method, step by step

### Rates, bands and thresholds

| Item and condition | Amount | Source |
| --- | --- | --- |
| 2026 expatriation: average annual net income tax for the five prior tax years, strictly more than | USD 211,000 | [Rev. Proc. 2025-32 §4.37](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Mark-to-market exclusion for taxable years beginning in 2026, not below zero | USD 910,000 | [Rev. Proc. 2025-32 §4.38](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Net worth on expatriation date, inclusive threshold, not indexed | USD 2,000,000 | [26 USC 877(a)(2)(B)](https://uscode.house.gov/us/usc/t26/s877/) |
| 2025 expatriation: tax-liability test strictly more than; 2025 mark-to-market exclusion | USD 206,000; USD 890,000 | [Rev. Proc. 2024-40 §§2.37–2.38](https://www.irs.gov/pub/irs-drop/rp-24-40.pdf) |
| Eligible deferred compensation: taxable payments; nongrantor trust: taxable distribution portion | 30% | [26 USC 877A(d)(1), (f)](https://uscode.house.gov/us/usc/t26/s877a/) |
| Required Form 8854 missing, incomplete or incorrect, per year, subject to reasonable cause and no willful neglect | USD 10,000 | [26 USC 6039G(c)](https://uscode.house.gov/us/usc/t26/s6039g/) |
| Section 2801: annual aggregate covered receipts exceeding the exception, calendar 2026 | USD 19,000 | [Rev. Proc. 2025-32 §4.42(3)](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Section 2801 tax on net covered receipts; foreign gift/estate tax reduction below | 40% | [Form 708 instructions, Computing Section 2801 Tax](https://www.irs.gov/instructions/i708) |

### Establish status and the date

1. **Citizen:** use the earliest of qualifying consular renunciation, a signed relinquishment statement furnished to the State Department confirming a qualifying expatriating act, issuance of a CLN, or a US court's cancellation of naturalization. The first two dates require subsequent approval by issuance of a CLN. A judicial cancellation does not itself require a CLN. [26 USC 877A(g)(4)](https://uscode.house.gov/us/usc/t26/s877a/).
2. **LTR:** count LPR status in at least **8 of the 15 tax years ending with the termination year**, including partial years. Exclude a year of treaty foreign residence without waiver of applicable treaty benefits. The test counts tax years, not eight elapsed years or eight full years. [26 USC 877(e)(2)](https://uscode.house.gov/us/usc/t26/s877/); [IRM 20.1.9.11.1, former LTR](https://www.irs.gov/irm/part20/irm_20-001-009).
3. **LPR termination:** use the earliest qualifying I-407 filing, final abandonment order (final judicial order if appealed), final removal order, or commencement of treaty foreign residence with no waiver of treaty benefits and IRS notice. A treaty claim can be the earlier termination; resolve it before counting later years. [Form 8854 instructions, Date of termination](https://www.irs.gov/instructions/i8854); [26 USC 7701(b)(6)](https://uscode.house.gov/us/usc/t26/s7701/).
4. **Covered tests:** any one applies, subject to the two exceptions below. For the tax test, determine each prior year's total tax less foreign tax credit and average the five years. For certification, check all applicable income, employment, gift and information returns and payment of tax, interest and penalties; certify on Form 8854 under penalties of perjury and supply evidence if required. [26 USC 877(a)(2)](https://uscode.house.gov/us/usc/t26/s877/); [Form 8854 instructions, Part II A lines 1 and 7](https://www.irs.gov/instructions/i8854).
5. **Keep FBAR separate:** it remains a separate reporting obligation; a missing FBAR alone does not establish failure to meet the Title 26 certification. Do not confuse FBAR with Form 8938 or other tax information returns. [26 USC 877(a)(2)(C), “requirements of this title”](https://uscode.house.gov/us/usc/t26/s877/); [IRS relief FAQs, Q18](https://www.irs.gov/individuals/international-taxpayers/relief-procedures-for-certain-former-citizens).

### Value and compute

6. **Net worth:** prepare the expatriation-date balance sheet using gift-tax ownership and valuation principles, including pensions/deferred compensation at present value, partnership interests, equity and trust interests, and liabilities. Good-faith FMV/basis estimates are allowed; formal appraisals are not required. If net worth reached the threshold in the prior five years but is lower on expatriation, explain the change in the statement required by Part II A line 3. Beneficial trust interests use the referenced Notice 97-19 method; hard valuations need advice. [Form 8854 instructions, Part II A line 3 and Section B](https://www.irs.gov/instructions/i8854).
7. **Separate the regimes:** other property is deemed sold at FMV on the **day before** expatriation; deferred compensation, specified tax-deferred accounts and nongrantor trust interests are excluded from that pool. Gains count in full; losses remain subject to other Code limits, but section 1091 wash-sale disallowance does **not** apply. Later gain/loss is adjusted for the deemed-sale gain/loss without regard to the exclusion. [26 USC 877A(a), (c)](https://uscode.house.gov/us/usc/t26/s877a/).
8. **Arrival-date basis:** solely for the mark-to-market computation, property held when the individual first became a US resident has basis no lower than its FMV then, unless the individual irrevocably elects **out**. The 2025 instructions say writing “(h)(2)” next to an entry makes the opt-out election; it does not claim the step-up. Obtain evidence before computing. [26 USC 877A(h)(2)](https://uscode.house.gov/us/usc/t26/s877a/); [Form 8854 instructions, Section C column (c)](https://www.irs.gov/instructions/i8854).
9. **Allocate the exclusion:** allocate the available exclusion to gain assets in proportion to each asset's built-in gain over total built-in gains, capping the exclusion at total positive gains and each allocation at that asset's gain. Do not allocate to loss assets or use the exclusion against the special regimes. Attach the allocation schedule. Report each deemed sale on its relevant income-return form (for example Form 8949 or Form 4797), retaining capital/ordinary character. [Form 8854 instructions, Section C columns (e), (f) and Reporting gain or loss](https://www.irs.gov/instructions/i8854). A repeat expatriation needs the prior-use restriction in Notice 2009-85 §3B: Check this point with one of our partner accountants.

## Boundary and exception table

| Rule | Operative conditions and treatment | Source |
| --- | --- | --- |
| Dual citizen at birth | US and other-country citizenship at birth; still citizen of and taxed as resident of that same country at expatriation; US resident under the substantial presence test for no more than 10 of the 15 tax years ending with expatriation. Switches off tax-liability/net-worth tests only; certification remains. | [26 USC 877A(g)(1)(B)(i)](https://uscode.house.gov/us/usc/t26/s877a/) |
| Minor | Relinquishes citizenship before age 18½; US resident under the substantial presence test for no more than 10 tax years before relinquishment. Citizens only; certification remains. | [26 USC 877A(g)(1)(B)(ii)](https://uscode.house.gov/us/usc/t26/s877a/) |
| Eligible deferred compensation | Qualified plans including 401(k), SEP/SIMPLE, foreign pensions, other deferred compensation and qualifying section 83 rights need classification. Eligibility requires a US payer (or an effective qualifying non-US payer election), timely W-8CE notification and irrevocable treaty withholding-reduction waiver on Form 8854. Withholding is on taxable payments, not automatically every dollar paid. Do not assume a non-US payer can effect an election without the required procedure. | [26 USC 877A(d)(1), (3)–(4)](https://uscode.house.gov/us/usc/t26/s877a/); [Form 8854 instructions, Section C line 1a](https://www.irs.gov/instructions/i8854) |
| Ineligible deferred compensation | Present value of accrued benefit is deemed received the day before expatriation; section 83 rights instead become transferable and free of substantial risk of forfeiture. No early-distribution tax; adjust later distributions for this treatment. The foreign-service portion earned while neither a US citizen nor resident is excepted from subsection (d)(1) and (2). | [26 USC 877A(d)(2), (5)](https://uscode.house.gov/us/usc/t26/s877a/) |
| Specified tax-deferred accounts | IRAs except SEP/SIMPLE; 529, ABLE, Coverdell, HSA and Archer MSA: entire interest deemed distributed the day before expatriation, with no early-distribution tax and adjustment to subsequent distributions. Determine the taxable amount under the account's applicable rules; the deemed distribution is not a claim that all account value is taxable in every case. | [26 USC 877A(e), (g)(6)](https://uscode.house.gov/us/usc/t26/s877a/) |
| Nongrantor trust | Beneficiary on the day before expatriation; nongrantor status tested immediately before expatriation. Trustee withholds on taxable portions of direct/indirect distributions; treaty reductions deemed waived. Appreciated property distributions cause trust gain. The alternative whole-interest election requires an IRS valuation ruling; withholding continues until the ruling and payment certification requirements are met. | [26 USC 877A(f)](https://uscode.house.gov/us/usc/t26/s877a/); [Form 8854 instructions, Section C line 1d](https://www.irs.gov/instructions/i8854) |
| Grantor trusts and section 684 | Grantor-portion assets ordinarily enter the mark-to-market regime; section 684 applies first where triggered. For classification, valuation-ruling elections and the interaction: Check this point with one of our partner accountants. | [Notice 2009-85 §§1, 4](https://www.irs.gov/pub/irs-drop/n-09-85.pdf); [26 USC 877A(h)(3)](https://uscode.house.gov/us/usc/t26/s877a/) |
| Deferring mark-to-market tax | Irrevocable, property by property; accepted adequate security, treaty assessment/collection waiver, tax-deferral agreement and US limited agent required. Interest at the underpayment rate compounds daily from the unextended due date of the return for the year containing the day before expatriation. Due on disposition-year return deadline, no later than death-year return deadline or security failure unless timely cured as the IRS allows. Annual Form 8854 continues through full payment. For an actual election: Check this point with one of our partner accountants. | [26 USC 877A(b)](https://uscode.house.gov/us/usc/t26/s877a/); [Notice 2009-85 §3E](https://www.irs.gov/pub/irs-drop/n-09-85.pdf); [Form 8854 instructions, Section D](https://www.irs.gov/instructions/i8854) |
| Existing replacement/payment windows | For covered expatriates, replacement-property periods that would reduce recognized gain terminate the day before expatriation; existing extensions of time to pay also cease, with unpaid tax payable as prescribed. | [26 USC 877A(h)(1)](https://uscode.house.gov/us/usc/t26/s877a/) |
| Later US citizenship/residence | During a later period taxable as a US citizen/resident, the person is not treated as covered for subsection (d)(1), subsection (f) and section 2801. For section 2801, apply the estate/gift residence definition, not income-tax residence. | [26 USC 877A(g)(1)(C)](https://uscode.house.gov/us/usc/t26/s877a/); [Form 708 instructions, Covered expatriate](https://www.irs.gov/instructions/i708) |
| Relief Procedures for Certain Former Citizens | Non-willful failures; citizenship relinquished after 18 March 2010; no filing history as citizen/resident (a good-faith Form 1040-NR is a stated exception); average tax not above the applicable threshold; net worth below USD 2 million both at expatriation and submission; aggregate six-year tax at most USD 25,000 after applicable deductions/exclusions/credits but excluding section 877A, penalties and interest; all six years' required returns/schedules supplied. Eligibility and the submission require advice: Check this point with one of our partner accountants. | [IRS relief procedures, FAQs 2–4](https://www.irs.gov/individuals/international-taxpayers/relief-procedures-for-certain-former-citizens) |

### Section 2801: covered gifts and bequests

The recipient pays. For individuals, US residence here means **domicile for gift/estate tax**, not simply income-tax residence. A domestic trust pays as a US citizen; non-electing foreign-trust distributions attributable to covered transfers can burden US recipients; an electing foreign trust can pay as a domestic trust. [26 USC 2801(a)–(b), (e)(4)](https://uscode.house.gov/us/usc/t26/s2801/); [Form 708 instructions, definitions](https://www.irs.gov/instructions/i708).

Covered property includes direct/indirect gifts while the donor is covered and bequests from a person covered immediately before death. Exclusions include a **chapter 12 taxable gift** shown on a timely gift-tax return, gross-estate property shown on a timely estate-tax return, and qualifying marital/charitable transfers under the specified deduction rules. Merely reporting a transfer that is not a chapter 12 taxable gift does not satisfy the taxable-gift exception. The regime has no general time expiry, subject to the later-US-status rule above. [26 USC 2801(e), (f)](https://uscode.house.gov/us/usc/t26/s2801/).

Compute 40% of aggregate calendar-year covered receipts less the annual exception, not below zero; reduce by foreign gift/estate tax paid on the same transfer. For 2026 the exception is in the rates table; for 2025 it is also USD 19,000. [Form 708 instructions, Section 2801(c) amount and Computing Section 2801 Tax](https://www.irs.gov/instructions/i708).

A living possible expatriate donor who does not authorize disclosure is presumed covered unless the recipient supplies other documentation. A protective Form 708 can start the assessment period when the recipient reasonably concludes the transfer is not covered, but it needs all required information, the sworn affidavit and applicable supporting attachments. [Form 708 instructions, Determining Responsibility](https://www.irs.gov/instructions/i708).

Form 708 implements reporting for covered receipts on or after **1 January 2025**. General due date: the 15th day of the 18th month after the receipt year ends, giving **15 June 2027** for 2025 and **15 June 2028** for 2026. **Bequests received after death and trust events have special deadlines; do not assume the general date is available.** Form 7004 timely filed gives six additional months to file, not to pay. Complex gifts/bequests, trust transfers, protective returns and special deadlines: Check this point with one of our partner accountants. [Form 708 instructions, General Instructions and When To File](https://www.irs.gov/instructions/i708); [IRS, final regulations applicability](https://www.irs.gov/businesses/small-businesses-self-employed/whats-new-estate-and-gift-tax).

## Worked cases

Hypothetical inputs; preserve the stated years. Each conclusion assumes no unstated exception or prior expatriation.

**Case 1: 2025 against 2026.** Average annual net income tax is USD 208,000 and net worth USD 1,900,000. Assume the average is USD 208,000 for **each year's different five-year window**, no dual/minor exception and valid five-year certification. For 2025, 208,000 − 206,000 = USD 2,000 above the tax threshold: covered. For 2026, 208,000 is not more than 211,000; net worth is USD 100,000 below the threshold: not covered. Exactly USD 2,000,000 net worth would make the person covered in either year. This comparison does not promise that delaying departure leaves the average or net worth unchanged. [2025 thresholds](https://www.irs.gov/pub/irs-drop/rp-24-40.pdf); [2026 thresholds](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf); [26 USC 877(a)(2)](https://uscode.house.gov/us/usc/t26/s877/).

```oa-check
name: Covered expatriate tests, 2025 against 2026 thresholds
inputs:
  average_tax: 208000
  net_worth: 1900000
  threshold_2025: 206000
  threshold_2026: 211000
  net_worth_test: 2000000
steps:
  - excess_2025: max(average_tax - threshold_2025, 0)
  - excess_2026: max(average_tax - threshold_2026, 0)
  - net_worth_headroom: net_worth_test - net_worth
expected:
  excess_2025: 2000.00
  excess_2026: 0.00
  net_worth_headroom: 100000.00
```

**Case 2: 2026 exclusion allocation.** A naturalized citizen renounces in 2026, with a later CLN; net worth USD 3,500,000. Covered. Asset A gain USD 1,200,000 and asset B gain USD 300,000 total USD 1,500,000. Allocate USD 910,000: A takes USD 728,000 and recognizes USD 472,000; B takes USD 182,000 and recognizes USD 118,000. Total recognized gain USD 590,000. Report each asset on its appropriate form, retaining character. [Rev. Proc. 2025-32 §4.38](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf); [Form 8854 instructions, Section C](https://www.irs.gov/instructions/i8854).

```oa-check
name: Mark-to-market exclusion allocation (2026)
inputs:
  exclusion: 910000
  gain_a: 1200000
  gain_b: 300000
steps:
  - total_gain: gain_a + gain_b
  - exclusion_a: exclusion * gain_a / total_gain
  - exclusion_b: exclusion * gain_b / total_gain
  - recognized_a: gain_a - exclusion_a
  - recognized_b: gain_b - exclusion_b
  - total_recognized: max(total_gain - exclusion, 0)
expected:
  total_gain: 1500000.00
  exclusion_a: 728000.00
  exclusion_b: 182000.00
  recognized_a: 472000.00
  recognized_b: 118000.00
  total_recognized: 590000.00
```

**Case 3: dual citizen at birth.** US-born to French parents, stipulated US/French citizen at birth; US residence in 9 of the 15 tax years ending with 2026; still French citizen and taxed as resident in France at expatriation; net worth USD 3,000,000; five compliant years certified. Not covered under the exception. With 11 US-resident years, or taxed as resident in Switzerland instead of France, the exception fails and the net-worth test makes them covered. **One missing year of FBARs alone does not negate the Title 26 certification**; investigate and remedy the separate reporting failure. [26 USC 877A(g)(1)(B)](https://uscode.house.gov/us/usc/t26/s877a/); [26 USC 877(a)(2)(C)](https://uscode.house.gov/us/usc/t26/s877/); [IRS relief FAQ 18](https://www.irs.gov/individuals/international-taxpayers/relief-procedures-for-certain-former-citizens).

**Case 4: LTR count in 2026.** Card issued in 2017, held throughout 2018–2025, I-407 in May 2026, no treaty position: the eight full years already establish LTR status (2017–2026 count as ten tax years including partial years). With a card issued in **March 2019** and I-407 in **May 2026**, the six full years 2020–2025 plus partial 2019 and 2026 make **eight**; LTR status does not need referral merely because the endpoint years are partial. Variant retaining the 2017 card but a 2022 treaty-resident position without waiver: distinguish two factual alternatives. **If LPR status continued through May 2026 and only 2022 is excluded**, count partial 2017 + 2018–2021 (four full years) + 2023–2025 (three full years) + partial 2026 = **nine counted years**, so the person is an LTR at the May 2026 I-407 termination; covered status must then be tested separately. **If treaty foreign residence, no waiver and the required IRS notice ended LPR status in 2022**, the six possible years 2017–2022 less excluded 2022 leave **five counted years**, so the person was not an LTR at that termination. The facts do not establish which alternative applies or any later LPR status/reacquisition. Do not give an unconditional May 2026 expatriation or covered-status conclusion. Check this point with one of our partner accountants. [26 USC 877(e)(2)](https://uscode.house.gov/us/usc/t26/s877/); [IRM 20.1.9.11.1](https://www.irs.gov/irm/part20/irm_20-001-009); [26 USC 7701(b)(6)](https://uscode.house.gov/us/usc/t26/s7701/).

```oa-check
name: Case 4 conditional treaty-year counts
inputs:
  original_issue_year: 2017
  full_start_year: 2018
  full_end_year: 2025
  treaty_year: 2022
  i407_year: 2026
  variant_issue_year: 2019
steps:
  - original_full_years: full_end_year - full_start_year + 1
  - full_years_excluding_treaty: original_full_years - 1
  - continuing_lpr_count: i407_year - original_issue_year + 1 - 1
  - years_through_treaty_termination: treaty_year - original_issue_year + 1
  - treaty_termination_count: years_through_treaty_termination - 1
  - march_2019_to_may_2026_count: i407_year - variant_issue_year + 1
expected:
  original_full_years: 8
  full_years_excluding_treaty: 7
  continuing_lpr_count: 9
  years_through_treaty_termination: 6
  treaty_termination_count: 5
  march_2019_to_may_2026_count: 8
```


**Case 5: low wealth, missing returns.** A citizen abroad renounces in 2026, net worth USD 400,000, average tax far below USD 211,000; two of five returns and FBARs unfiled, three returns filed as a citizen. Failure to certify the missing required **tax returns** makes them covered unless compliance is established in time for valid certification. An IRA distribution consequence requires an actual specified account; none was valued in these facts. Future section 2801 exposure depends on covered transfers and recipient/exclusion rules. The three citizen returns prevent use of the no-filing-history relief procedure. Resolve the tax returns and the separate FBAR problem; do not promise that any late filing cures covered status. Check this point with one of our partner accountants. [Form 8854 instructions, certification](https://www.irs.gov/instructions/i8854); [IRS relief FAQs 2–3, 18](https://www.irs.gov/individuals/international-taxpayers/relief-procedures-for-certain-former-citizens).

**Case 6: IRA and 401(k).** A covered expatriate's traditional IRA is USD 300,000, all pre-tax: entire interest is deemed distributed the day before expatriation, USD 300,000 includible, with no early-distribution tax. A US employer's 401(k) is deferred compensation: assuming a qualifying US payer, timely W-8CE and Form 8854 treaty waiver, 30% applies to each later **taxable** payment. Otherwise it is ineligible and the accrued benefit's present value is deemed received before expatriation. [26 USC 877A(d)–(e)](https://uscode.house.gov/us/usc/t26/s877a/); [Form 8854 instructions, Section C](https://www.irs.gov/instructions/i8854).

**Case 7: 2026 gift.** A covered expatriate, now a nonresident, gives USD 500,000 of foreign shares to a US-citizen child in 2026; no US gift-tax return required or filed, no foreign gift tax paid. Assuming no US gift-tax domicile, this is the child's only covered receipt that year and no exclusion other than the annual exception applies: 40% × (500,000 − 19,000) = **USD 192,400** on Form 708, generally due **15 June 2028**. The original hypothetical timely-return exception applies only to an actual chapter 12 taxable gift; gratuitously listing these otherwise non-taxable foreign shares on a return does not create that exception. [26 USC 2801](https://uscode.house.gov/us/usc/t26/s2801/); [Form 708 instructions](https://www.irs.gov/instructions/i708); [2026 exception](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf).

```oa-check
name: Section 2801 gift received in 2026
inputs:
  gift: 500000
  exception: 19000
  rate: 0.40
steps:
  - net_covered: max(gift - exception, 0)
  - recipient_tax: net_covered * rate
expected:
  net_covered: 481000.00
  recipient_tax: 192400.00
```

## When to refuse or refer

Do not default missing valuations, citizenship dates, treaty history, certification or W-8CE delivery into a final tax outcome. Retain these referral codes in the working paper: **R-EX-DATE** unclear acts/CLN/orders; **R-EX-LTR** missing treaty or termination/reacquisition facts; **R-EX-VALUE** hard valuations or near-threshold net worth; **R-EX-CERT** compliance gaps/relief eligibility; **R-EX-TRUST** classification, section 684 or ruling elections; **R-EX-DEFER** actual deferral; **R-EX-PENSION** foreign pensions/payers and service allocation; **R-EX-NEAR** near-threshold average tax; **R-EX-2801** complex gifts/bequests/trusts or recipient status; **R-EX-STATE** state tax; **R-EX-PRE2008** older departures or unresolved earlier Form 8854. For each unresolved point state: **Check this point with one of our partner accountants.** Partial calendar years alone are not a reason to withhold an LTR count.

## Filing and payment

- **Initial Form 8854:** citizens and LTRs who expatriate file it, covered or not. The published general instructions attach Parts I and II to the return for the expatriation year; for the January 1 boundary below, obtain advice on reconciling the day-before-year requirement in Notice 2009-85 §8C. If no income return is required, send Form 8854 by the hypothetical return due date including extensions. The current instructions give **Internal Revenue Service, 3651 S IH35, MS 4301 AUSC, Austin, TX 78741**; follow their Where To File directions for original forms and deferral requests. [Form 8854 instructions, Who Must File / When To File / Where To File](https://www.irs.gov/instructions/i8854).
- **Return type:** status at year-end determines the return. A person nonresident at year-end with a resident period generally files dual-status Form 1040-NR with Form 1040 as statement; the deemed-sale and deemed distributions belong to the year containing the **day before** expatriation. A 1 January expatriation puts those items in the prior year and does not itself create a dual-status expatriation-year return; test any later residence separately. Thus a 1 January 2026 deemed sale is on 31 December 2025 and uses the 2025 exclusion. For the initial Form 8854 filing-year boundary: Check this point with one of our partner accountants. [Notice 2009-85 §8B](https://www.irs.gov/pub/irs-drop/n-09-85.pdf); [Form 8854 instructions, Reporting gain or loss](https://www.irs.gov/instructions/i8854).
- **Calendar-year filing dates, ordinary rules:** a year-end nonresident with no employee wages subject to US withholding generally uses the sixth-month deadline; with such wages, the fourth-month deadline. Derived 2026 dates: **15 June 2027 → 15 December 2027** on timely Form 4868, or **15 April 2027 → 15 October 2027**. The retained 2025 dates are **15 June 2026 → 15 December 2026**, or **15 April 2026 → 15 October 2026**. A year-end resident generally uses April/October, but qualifying residents abroad have separate rules: Check this point with one of our partner accountants. Extensions to file do not extend payment. [Form 1040-NR instructions, When and Where Should You File](https://www.irs.gov/instructions/i1040nr); [Publication 519, When To File / Extensions](https://www.irs.gov/publications/p519).
- **Annual Form 8854:** Parts I and III for later years while deferred tax remains, eligible deferred compensation exists, or the person is a nongrantor-trust beneficiary, subject to the instructed trust-election exception. Attach to an income return when required and send the marked copy to Austin; otherwise file separately by the hypothetical due date including extensions. Annual deferral reporting runs through full payment of tax and interest. [Form 8854 instructions, When To File and Part III](https://www.irs.gov/instructions/i8854).
- **W-8CE:** covered expatriates give it to the relevant deferred-compensation payer, specified-account custodian and nongrantor trustee by the earlier of the day before the first distribution **on or after** expatriation or **30 days after** expatriation; keep a copy. Missing delivery facts need investigation, not an automatic final eligibility finding. [Form W-8CE, When To File](https://www.irs.gov/pub/irs-pdf/fw8ce.pdf).
- **Payment/penalty:** without an effective deferral, pay tax by the applicable unextended return deadline. Deferral interest and acceleration follow the boundary table. The Form 8854 penalty in the rates table has the statutory reasonable-cause/no-willful-neglect exception. [26 USC 877A(b)](https://uscode.house.gov/us/usc/t26/s877a/); [26 USC 6039G(c)](https://uscode.house.gov/us/usc/t26/s6039g/). FBAR/Form 8938 may still apply for the US-person part year; use the linked reporting Guide.

## Completion checklist

Record the evidenced date, year count, each covered test and exception, five-year certification, dated balance sheet and valuations; document asset classification, basis, exclusion allocation and income-return placement; retain W-8CE/waivers, any deferral agreement/security, filing/payment dates, annual reminders and section 2801 handoff. Produce the working paper and reviewer brief; obtain qualified review before filing. **Circular 230 §10.37:** apply these rules to established facts, identify assumptions and unresolved points, and do not use this general Guide as a signed opinion.

## Sources

| Official source and passage actually read | URL | Read on |
| --- | --- | --- |
| Read Rev. Proc. 2025-32 §§4.37–4.38, 4.42(3): 2026 tax test, exclusion and covered-transfer exception | https://www.irs.gov/pub/irs-drop/rp-25-32.pdf | 2026-11-27 |
| Read Rev. Proc. 2024-40 §§2.37–2.38: retained 2025 comparison | https://www.irs.gov/pub/irs-drop/rp-24-40.pdf | 2026-11-27 |
| Read current 26 USC 877(a)(2), (e)(2): covered tests, certification and LTR count | https://uscode.house.gov/us/usc/t26/s877/ | 2026-11-27 |
| Read current 26 USC 877A(a)–(h), effective date and amendment history: operative regimes and conditions | https://uscode.house.gov/us/usc/t26/s877a/ | 2026-11-27 |
| Read current 26 USC 7701(b)(6): LPR/treaty cessation | https://uscode.house.gov/us/usc/t26/s7701/ | 2026-11-27 |
| Read current 26 USC 6039G(c): penalty and exception | https://uscode.house.gov/us/usc/t26/s6039g/ | 2026-11-27 |
| Read current 26 USC 2801(a)–(f), effective-date and amendment notes: recipient tax, exceptions, trusts | https://uscode.house.gov/us/usc/t26/s2801/ | 2026-11-27 |
| Read Form 8854 instructions (2025), General Instructions and Parts II–III: filing, certification, valuation, allocation, basis election and deferral | https://www.irs.gov/instructions/i8854 | 2026-11-27 |
| Read IRM 20.1.9.11.1, former LTR definition: all or any part of qualifying years | https://www.irs.gov/irm/part20/irm_20-001-009 | 2026-11-27 |
| Read Notice 2009-85 §§1–4 and 8: grantor assets, exclusion, deferral interest and year-of-day-before filing | https://www.irs.gov/pub/irs-drop/n-09-85.pdf | 2026-11-27 |
| Read Form W-8CE, Who Must File / When To File: relevant payers and on-or-after distribution timing | https://www.irs.gov/pub/irs-pdf/fw8ce.pdf | 2026-11-27 |
| Read Form 708 instructions (December 2025), General Instructions, definitions, responsibility, computation, deadlines and extensions | https://www.irs.gov/instructions/i708 | 2026-11-27 |
| Read IRS estate/gift update, section 2801 final-regulation paragraph: receipts from 1 January 2025 | https://www.irs.gov/businesses/small-businesses-self-employed/whats-new-estate-and-gift-tax | 2026-11-27 |
| Read Relief Procedures FAQs 2–4 and 18: complete eligibility, good-faith 1040-NR exception and separate FBAR requirement | https://www.irs.gov/individuals/international-taxpayers/relief-procedures-for-certain-former-citizens | 2026-11-27 |
| Read Form 1040-NR instructions, When and Where Should You File: fourth/sixth month deadlines | https://www.irs.gov/instructions/i1040nr | 2026-11-27 |
| Read Publication 519, return type and filing/extension passages: nonresident deadlines and timely six-month extension | https://www.irs.gov/publications/p519 | 2026-11-27 |

Not yet confirmed: the **2026 Form 8854 layout and instructions**. Line/part references above identify the published 2025 instructions and must not be assumed to identify 2026 fields. The indexed 2026 amounts come from Rev. Proc. 2025-32; operative statutory text was read in the official current Code, whose pages state currency through Public Law 119-142 (10 November 2026). Actual relief submissions, repeat expatriation, treaty/payer elections, trust rulings and special Form 708 deadlines require the referrals stated above.
