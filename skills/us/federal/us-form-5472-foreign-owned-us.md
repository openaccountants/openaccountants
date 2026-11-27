---
name: us-form-5472-foreign-owned-us
description: Determine Form 5472 filing for foreign-owned US corporations, foreign corporations doing US business and foreign-owned US disregarded entities for tax year 2026. Covers ownership, related-party transactions, pro forma Form 1120, filing and extension, EIN, records and penalties; retains dated 2025 cases with explicit holds for unresolved residency, treaty and dividend questions. Trigger on Form 5472, foreign-owned LLC, pro forma 1120, 6038A or foreign-owned U.S. DE.
version: "2.2"
jurisdiction: US
tax_year: 2026
last_updated: 2026-11-27
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: cross-border
type: situation-rules
---

# US Form 5472 for foreign-owned US corporations and single-member LLCs, tax year 2026

A foreign-owned US disregarded entity (DE) files Form 5472 with a pro forma Form 1120 for a year with a reportable related-party transaction, including owner contributions and distributions; unrelated customer receipts alone do not trigger it. A missing or substantially incomplete return can attract USD 25,000 per related party per year. [Filing and penalty rules](https://www.irs.gov/instructions/i5472).

## Scope and who this is for

Federal reporting for a domestic corporation that is 25% foreign-owned, a foreign corporation engaged in US business, or a domestic DE wholly owned by one foreign person. This is an information-return analysis, not an income-tax, withholding or treaty computation. Use alongside `us-tax-workflow-base`. The 2025 cases below remain dated 2025. [26 USC 6038A](https://uscode.house.gov/us/usc/t26/s6038A/), [6038C](https://uscode.house.gov/us/usc/t26/s6038C/), [Regulation 1.6038A-1(c)](https://www.ecfr.gov/current/title-26/section-1.6038A-1).

## Ask the client first

- Obtain formation documents, elections (including Forms 8832/2553), owner history throughout the year, ownership chains and family relationships. Do not infer tax classification from the word LLC or foreign-person status from nationality, overseas residence or absence of a green card alone.
- Establish citizenship, US tax residence and any section 6013(g)/(h) election for individual owners; obtain the identifiers and residence/organization details requested on the form. Resolve US residence using `us-tax-residency` before applying this Guide.
- Reconcile every owner/related-party contribution, distribution, personally paid entity expense, loan, interest, fee, royalty and property/service transfer, including free or discounted transfers. Obtain opening/closing loan balances and the exchange-rate schedule.
- Confirm tax year, EIN, related reporting corporations, gross receipts/income, prior filings, valid extensions and IRS contact/notices. Preserve bank statements, agreements and filing evidence.

## The method, step by step

### 1. Reporting corporation and related parties

A domestic corporation meets the ownership test if **one foreign person owns at least 25% of vote or value at any time in the year**. A foreign corporation engaged in US trade or business is separately within section 6038C; there is no 25% ownership prerequisite for that category. [Sections 6038A(a), (c) and 6038C(a)](https://uscode.house.gov/us/usc/t26/s6038A/); [6038C](https://uscode.house.gov/us/usc/t26/s6038C/).

A domestic entity otherwise disregarded, with one foreign person as direct or indirect sole owner, is treated as a separate domestic corporation for section 6038A. Indirect sole ownership here runs entirely through other DEs or grantor trusts, domestic or foreign. Its year follows the owner's US income-tax or information-return year if the owner has such a filing obligation; otherwise it uses the calendar year. [Regulation 301.7701-2(c)(2)(vi)](https://www.ecfr.gov/current/title-26/section-301.7701-2).

An individual foreign person is neither a US citizen nor a US resident and has no section 6013(g)/(h) election in effect. Regulation 1.6038A-1(f) also covers qualifying possession citizens, non-US-organized entities, foreign estates/trusts and commercial foreign-government activity; a foreign government is outside the special records/agent rules. [Definition](https://www.ecfr.gov/current/title-26/section-1.6038A-1).

Apply section 318 attribution with **10% substituted for 50% in section 318(a)(2)(C)** and the prohibition on section 318(a)(3)(A)–(C) attributing foreign-owned stock to a US person. Section 267(c) applies to the extent it attributes to persons whom section 318 does not reach. Also do not apply section 318(a)(3)(C)/Regulation 1.318-1(b) to make a US corporation a reporting corporation if it would not otherwise be 25% foreign-owned. Family attribution includes a spouse other than one legally separated under a decree of divorce/separate maintenance, children (including adopted children), grandchildren and parents. Corporate-to-owner attribution is proportionate, not automatic ownership of the whole block. [6038A(c)(5)](https://uscode.house.gov/us/usc/t26/s6038A/), [318(a)](https://uscode.house.gov/us/usc/t26/s318/), [Regulation 1.6038A-1(e)](https://www.ecfr.gov/current/title-26/section-1.6038A-1).

A related party is a direct/indirect 25% foreign shareholder, anyone related under section 267(b) or 707(b)(1) to the corporation or such shareholder, or anyone related to the corporation under section 482. A corporation filing a consolidated federal income-tax return with the reporting corporation is excluded. A foreign related party must also meet the foreign-person definition. [Regulation 1.6038A-1(d), (g)](https://www.ecfr.gov/current/title-26/section-1.6038A-1).

File one Form 5472 for **each foreign or US related party with a reportable transaction**. Without any Part IV/VI transaction, and for DEs any Part V transaction, no Form 5472 is required. The information can be required even when it affects no tax due. Treaty/no-PE, shipping, FSC, Form 5471/Schedule M, foreign-to-foreign exceptions and consolidated filings go to the referral table; do not assume an exception. [Regulation 1.6038A-2(a), (e)](https://www.ecfr.gov/current/title-26/section-1.6038A-2).

### 2. Report the transactions

The following is the mapping on **Form 5472 (Rev. December 2023)**; use the form and its instructions together. Part IV is for monetary transactions with a foreign related party. Part III still identifies a US related party, but do not complete Parts IV/VI for that party. [Form](https://www.irs.gov/pub/irs-pdf/f5472.pdf), [instructions](https://www.irs.gov/instructions/i5472).

| Type | Received / borrowed | Paid / loaned | Source |
| --- | --- | --- | --- |
| Inventory; other tangible property | 9; 10 | 23; 24 | [Form 5472 p2](https://www.irs.gov/pub/irs-pdf/f5472.pdf) |
| Rents; royalties other than intangible-property rights | 13a; 13b | 27a; 27b | [Form 5472 p2](https://www.irs.gov/pub/irs-pdf/f5472.pdf) |
| Intangible-property rights, including patent licences | 14 | 28 | [Form 5472 p2](https://www.irs.gov/pub/irs-pdf/f5472.pdf) |
| Technical/managerial/engineering/construction/scientific or like services; commissions | 15; 16 | 29; 30 | [Form 5472 p2](https://www.irs.gov/pub/irs-pdf/f5472.pdf) |
| Loans: beginning balance; ending balance or monthly average | 17a; 17b | 31a; 31b | [Form and loan instructions](https://www.irs.gov/instructions/i5472) |
| Interest; insurance/reinsurance premiums; loan guarantee fees | 18; 19; 20 | 32; 33; 34 | [Form 5472 p2](https://www.irs.gov/pub/irs-pdf/f5472.pdf) |
| Other amounts, only to extent taken into account in taxable income | 21 | 35 | [Instructions](https://www.irs.gov/instructions/i5472) |
| Totals of the received and paid columns | 22 | 36 | [Form 5472 p2](https://www.irs.gov/pub/irs-pdf/f5472.pdf) |

For loans, use either beginning/ending outstanding balances or the monthly average, entering only line 17b/31b for the latter. For interest paid, line 32 includes only the amount allowed under section 163(j) where that limitation applies. Platform contribution and cost-sharing transactions (lines 11/25 and 12/26) need specialist completion, including the no-netting rule and the line-12 condition that the corporation itself incurred intangible development costs. Check this point with one of our partner accountants. [Instructions](https://www.irs.gov/instructions/i5472).

**Part V, DE only:** check the box and attach a description of other Regulation 1.482-1(i)(7) transactions not already entered in Part IV, including formation/dissolution/acquisition/disposition, contributions and distributions. Capture owner-paid entity fees as contributions when paid on its behalf without repayment obligation. There is no filing floor: even the earlier examples of a USD 1 contribution, USD 50 reimbursement, or USD 40 transaction must be tested, not discarded as small. Unrelated customer/supplier flows are not related-party transactions. [Regulation 1.6038A-2(a), (b)(3)(xi), Example 1](https://www.ecfr.gov/current/title-26/section-1.6038A-2).

**Part VI:** for nonmonetary or less-than-full consideration, attach the property/rights/obligations and services transferred each way and a reasonable FMV estimate, if possible, or another reasonable value indicator. Use accrued amounts if on accrual, US dollars and an exchange-rate schedule; statements are in English. Partnership-attributed transactions go to the referral table. [Regulation 1.6038A-2(b)(4), (10), (c)](https://www.ecfr.gov/current/title-26/section-1.6038A-2).

### Rates, bands and thresholds

| Rule | Amount or boundary | Source |
| --- | --- | --- |
| Reporting small amounts rather than omitting them: transaction or series total | USD 50,000 or less | [Regulation 1.6038A-2(b)(9)](https://www.ecfr.gov/current/title-26/section-1.6038A-2) |
| Reasonable estimate safe band if actual amounts are not determinable | 75%–125% of actual | [Regulation 1.6038A-2(b)(8)](https://www.ecfr.gov/current/title-26/section-1.6038A-2) |
| Small-corporation exception to special records/agent rules, excluding DEs | US gross receipts strictly under USD 10,000,000, aggregating related reporting corporations | [Regulation 1.6038A-1(h)](https://www.ecfr.gov/current/title-26/section-1.6038A-1) |
| Alternative records/agent safe harbor, excluding DEs | Gross payments not more than USD 5,000,000 AND strictly less than 10% of US gross income | [Regulation 1.6038A-1(i)](https://www.ecfr.gov/current/title-26/section-1.6038A-1) |

The small-amount entry applies to the **total of a transaction or series**, not to each payment split out. Estimates outside the band are not automatically acceptable: Regulation 1.6038A-2(b)(8)(ii) requires an affirmative facts-and-circumstances statement under penalties of perjury and IRS determination. Check this point with one of our partner accountants.

For the records safe harbor, add gross payments in and out, including nonmonetary/discounted transactions; never net them. Aggregate the payments and relevant gross income of related reporting corporations. The small-corporation receipts test also aggregates related reporting corporations. Neither exception removes Form 5472 filing or section 6001 records. [Regulation 1.6038A-1(h)–(j)](https://www.ecfr.gov/current/title-26/section-1.6038A-1).

### 3. Complete and file the return

Part I: line 1f totals Part IV lines 22/36 plus Part VI FMV and DE Part V amounts; leave 1f blank for a US related party. Line 1g counts the forms; line 1h totals all their 1f amounts. Use the correct asset source: Form 1120 item D for domestic corporations, Form 1120-F Schedule L line 17(d) for foreign corporations. Check initial-filing line 1j, 50%-ownership line 2 with modified attribution, and DE line 3 as applicable. [Instructions, Part I](https://www.irs.gov/instructions/i5472).

Part II applies only to 25% foreign-owned US corporations/DEs: enter the largest two **direct** and largest two **ultimate indirect** 25% foreign shareholders, with more on an attached sheet and an attribution explanation. A holder below 25% directly does not become a direct 25% shareholder just because family attribution takes its holding above that threshold. A DE reports its foreign owner; a foreign DE direct owner is reported as such. Use US ID if any, otherwise the required reference ID, consistently year to year; reference IDs are alphanumeric, no spaces/special characters, maximum 50 characters and never reassigned to another person. For DE owners enter FTIN if any, otherwise “None”/“N/A”. Identifier changes/mergers need the instructions' correlation procedure. [Instructions, Part II](https://www.irs.gov/instructions/i5472).

All filers complete Part III, even if the party already appears in Part II, and Part VII with its **line-specific conditions**. In particular, do not complete lines 43a/43b for foreign corporations or foreign-owned US DEs; they are for domestic corporations within the instructions' conditions. Imported goods/customs value, hybrid interest/royalties, section 250, loan safe-haven rates and covered debt require the applicable instructions, not blanket “No” answers. For substantive calculations use the referral table. [Instructions, Parts III/VII](https://www.irs.gov/instructions/i5472).

For a DE, write **“Foreign-owned U.S. DE”** on the pro forma Form 1120, complete its name/address and page-one items B and E, sign and attach Form 5472. The pro forma form reports no income/deduction/tax calculation; it does not settle the owner's own income-tax or withholding obligations. [DE instructions](https://www.irs.gov/instructions/i5472).

## Worked cases

### Case 1 - original 2026 LLC inputs

Lucía is a Spanish resident, no US citizenship or green card; she forms a Wyoming LLC as sole member, no election, in February 2026. She contributes USD 3,000 in February, pays its USD 300 registered-agent fee personally in March, receives USD 30,000 in December; unrelated payment-processor customer receipts are USD 48,000. She has never filed.

**Conditional conclusion:** the original facts do not establish US tax nonresidence (including substantial presence), absence of a section 6013 election, or the owner's US filing tax year. Do not use a final filing conclusion until established. Check this point with one of our partner accountants. If she qualifies as a foreign person, the LLC uses the calendar year, and the fee is a contribution rather than a repayable advance, one Form 5472 reports three Part V owner transactions with line 1f USD 33,300, attached to pro forma 1120. The unrelated USD 48,000 is excluded. Use exact amounts; do not apply “USD 50,000 or less” separately to split a series. A year with no reportable transaction requires no Form 5472. [DE rule and Example 1](https://www.ecfr.gov/current/title-26/section-1.6038A-2), [filing instructions](https://www.irs.gov/instructions/i5472).

Assuming the same filing duty in each of 2026, 2027 and 2028 and no relief, three unfiled years expose USD 75,000 base penalty. A failure for one party/year continuing **150 days beyond** the notice's initial 90-day period adds five periods, USD 125,000. These are conditional statutory amounts, not an assessed liability or a promise about future law. [Penalty rule](https://uscode.house.gov/us/usc/t26/s6038A/).

```oa-check
name: Foreign-owned single-member LLC, 2026, is a Form 5472 needed and what is the exposure
inputs:
  contribution_cash: 3000
  owner_paid_fee: 300
  distribution: 30000
  customer_receipts: 48000
  related_parties: 1
  years_unfiled: 3
  penalty: 25000
  days_after_90_day_period: 150
  reportable_count: 3
steps:
  - line_1f: contribution_cash + owner_paid_fee + distribution
  - must_file: min(reportable_count, 1)
  - base_exposure: penalty * related_parties * years_unfiled
  - continuation_periods: ceil(days_after_90_day_period / 30)
  - continuation_penalty: continuation_periods * penalty
expected:
  line_1f: 33300
  must_file: 1
  base_exposure: 75000
  continuation_periods: 5
  continuation_penalty: 125000
```

### Case 2 - original 2026 corporation inputs

Delaware calendar-year C corporation: Hans, German, 15%; wife Petra, German, 12%; Sakura KK, Japanese company, 30%; US founders 43%. Kaito, Japanese individual, owns 60% of Sakura KK. Services received from Sakura KK USD 150,000; patent licence paid USD 420,000; Hans consulting paid USD 80,000. Nothing passes to/from Petra or Kaito. US gross receipts and gross income each USD 6,000,000.

Subject to confirming foreign-person status, vote/value percentages, no legally separated spouse, no other attribution and no filing exception: Hans and Petra each constructively own 27%; Kaito's proportionate holding is 18%; Sakura KK directly owns 30%. Kaito is related to Sakura KK under section 267(b)(2), but has no transactions. No person in the stated chain reaches 50%. [Ownership rules](https://uscode.house.gov/us/usc/t26/s318/), [267(b)(2)](https://uscode.house.gov/us/usc/t26/s267/), [Regulation 1.6038A-1](https://www.ecfr.gov/current/title-26/section-1.6038A-1).

Two forms: Sakura KK line 15/22 USD 150,000, line 28/36 USD 420,000, 1f USD 570,000; Hans line 29/36 and 1f USD 80,000. Line 1h is USD 650,000 on both. Part II shows Sakura KK as the direct 25% holder; Hans/Petra are indirect holders by attribution, with the required explanation, not direct 25% holders. No separate form solely for Petra/Kaito with no reportable transactions. [Form instructions](https://www.irs.gov/instructions/i5472).

USD 650,000 exceeds 10% of USD 6,000,000 (USD 600,000), so the de minimis safe harbor fails. The small-corporation records/agent exemption works **only if the aggregate receipts of all related reporting corporations remain under USD 10,000,000**; USD 6,000,000 for this corporation alone does not establish that. Filing remains required. Missing the two forms exposes USD 50,000 base penalty before relief. Patent pricing remains a hold: Check this point with one of our partner accountants. [Regulation 1.6038A-1(h)/(i)](https://www.ecfr.gov/current/title-26/section-1.6038A-1), [penalty](https://www.ecfr.gov/current/title-26/section-1.6038A-4).

```oa-check
name: 25% foreign-owned C corporation, attribution and record-keeping exceptions (2026)
inputs:
  hans_direct: 15
  petra_direct: 12
  kaito_share_of_kk: 0.60
  kk_direct: 30
  kk_services_received: 150000
  kk_royalties_paid: 420000
  hans_consulting_paid: 80000
  us_gross_receipts: 6000000
  us_gross_income: 6000000
  penalty: 25000
steps:
  - hans_constructive: hans_direct + petra_direct
  - kaito_attributed: kaito_share_of_kk * kk_direct
  - kk_line_1f: kk_services_received + kk_royalties_paid
  - hans_line_1f: hans_consulting_paid
  - line_1h: kk_line_1f + hans_line_1f
  - safe_harbor_limit: min(5000000, us_gross_income * 0.10)
  - safe_harbor_shortfall: line_1h - safe_harbor_limit
  - small_corp_headroom: 10000000 - us_gross_receipts
  - exposure_2026: 2 * penalty
expected:
  hans_constructive: 27
  kaito_attributed: 18
  kk_line_1f: 570000
  hans_line_1f: 80000
  line_1h: 650000
  safe_harbor_limit: 600000
  safe_harbor_shortfall: 50000
  small_corp_headroom: 4000000
  exposure_2026: 50000
```

### Retained 2025 cases and earlier boundary examples

- **Aisha / Frostbite LLC:** UK resident/national; Delaware SMLLC formed 1 March 2025, no election; Mercury/Stripe, GBP 8,000 contribution stated as USD 10,200, USD 14,500 unrelated US-customer receipts, USD 9,000 draws, no other related transactions. If foreign-person status/calendar year are established, Part V contribution/draws total USD 19,200; customer receipts are excluded. Complete Part III as well as II and the applicable Part VII questions. Ordinary calendar-2025 deadline was 15 April 2026, extended to 15 October 2026 only with a valid timely extension; both dates have passed. Original scenario's USD 0 customer-revenue variant still tests owner transactions; its unspecified USD X contribution/USD Y draws are not invented. Original three-unfiled-year scenario gives USD 75,000 base exposure only if all three years required filing. The currency equivalence is an original case input, not a verified exchange rate. UK LLC characterization, personal trading-income treatment, US residency/ECI, actual prior years and relief are **non-usable holds**. Check this point with one of our partner accountants. [Part V/filing](https://www.irs.gov/instructions/i5472), [deadline](https://uscode.house.gov/us/usc/t26/s6072/).
- **GreenMobil USA Inc. / GreenMobil GmbH:** Delaware calendar-year C corporation, EIN 88-1234567, 100% German-parent ownership; 2025 cost-plus 8% R&D contract, USD 4,200,000 service receipts, USD 620,000 patent royalties paid, no loans/other transactions. Conditional on stated foreign ownership and no exception, one Form 5472: line 15/22 USD 4,200,000; line 28/36 USD 620,000; 1f USD 4,820,000 with real Form 1120. Ordinary calendar-2025 filing dates as above. The earlier unquantified R&D scenario maps services to 15 and any interest received to 18. The 8% contract is preserved, **not certified arm's length**; neither a German treaty rate (including the old film/TV claim) nor “below USD 500 million, so no BEAT” is usable without the separate tests. Withholding, pricing documentation and BEAT are holds. Check this point with one of our partner accountants. [Form](https://www.irs.gov/pub/irs-pdf/f5472.pdf), [instructions](https://www.irs.gov/instructions/i5472).
- **Renata / TechCo Inc.:** Brazilian individual 30%, US founders 70%; 2025 total dividends USD 200,000, Renata's USD 60,000 share, no other transactions. The prior USD 18,000 withholding/USD 42,000 net is **arithmetic only**, not a usable withholding result. Dividend-only Form 5472 treatment, all prior “US–Brazil treaty” assertions, rates and resulting filing conclusion are expressly withdrawn pending specialist determination; Part V is DE-only. The original unquantified quarterly-dividend scenario is held the same way. Check this point with one of our partner accountants.
- **Earlier ownership boundaries:** a French national's 30% direct Delaware holding meets the ownership percentage only after foreign-person status is established. UK Holdings Ltd's 100% Cayman Sub Ltd holding, with Cayman owning 40% of a Delaware LLC taxed as a corporation, attributes 40% to UK Holdings. A 10% holding in UK Holdings does **not** automatically confer 25% ownership of Delaware; compute the proportionate chain and test other related-party rules. The earlier French-founder loan/management-fee example uses one form per related party with reportable transactions; the French founder plus UK passive investor variant does not establish DE status or two reporting duties without classification/relatedness/transactions. Check this point with one of our partner accountants. [Attribution](https://uscode.house.gov/us/usc/t26/s318/), [modified rules](https://www.ecfr.gov/current/title-26/section-1.6038A-1).

```oa-check
name: Preserved 2025 case arithmetic, not residency or treaty determinations
inputs:
  aisha_gbp: 8000
  aisha_usd_stated: 10200
  aisha_customer_receipts: 14500
  aisha_draws: 9000
  three_unfiled_years: 3
  penalty: 25000
  rd_receipts: 4200000
  rd_royalties: 620000
  rd_contract_markup: 0.08
  techco_dividends: 200000
  renata_share: 0.30
  old_withholding_assumption: 0.30
  uk_cayman_share: 1
  cayman_delaware_share: 0.40
steps:
  - aisha_part_v_total: aisha_usd_stated + aisha_draws
  - conditional_base_exposure: three_unfiled_years * penalty
  - greenmobil_line_1f: rd_receipts + rd_royalties
  - renata_gross: techco_dividends * renata_share
  - held_old_withholding_arithmetic: renata_gross * old_withholding_assumption
  - held_old_net_arithmetic: renata_gross - held_old_withholding_arithmetic
  - uk_attributed_percent: uk_cayman_share * cayman_delaware_share * 100
expected:
  aisha_part_v_total: 19200
  conditional_base_exposure: 75000
  greenmobil_line_1f: 4820000
  renata_gross: 60000
  held_old_withholding_arithmetic: 18000
  held_old_net_arithmetic: 42000
  uk_attributed_percent: 40
```

## When to refuse or refer

Every held topic below is **non-usable for a filing or calculation** until resolved. Check this point with one of our partner accountants.

| Situation | Destination / hold |
| --- | --- |
| Multiple LLC members, ownership changes, Forms 8832/2553, foreign DE/grantor-trust chains | Classification hold; `us-form-1065-partnership` where applicable; do not assume a DE |
| Corporation filing computation or extension payment | `us-form-1120-c-corp`, `us-1120-corporation-return-schedule-ordinary-business`, `us-corporate-extension-form-7004-and-the` |
| Foreign owner's ECI, 1040-NR/1120-F, residence, UK LLC treatment, treaty/PE, inbound withholding or Forms 1042/1042-S/W-8BEN-E | Separate taxpayer/treaty/withholding determination; preserve original inputs, no rate/default conclusion |
| Dividend-only regular corporation, nonmonetary dividends, corporate capital flows | Form 5472 reportability hold, not an asserted exemption or filing duty |
| Form 5471/Schedule M, FSC/1120-FSC, shipping sections 883/887, wholly foreign transactions | Establish all exception conditions first; DE exclusions and BEAT anti-avoidance rules must be tested |
| Consolidated Form 5472, foreign-government, partnership-attributed or other rare transactions | Specialist completion, member schedule and relevant aggregation/exceptions; no automatic filing exemption |
| Section 482 methods/studies, section 1.6662-6 documentation, section 6662 penalties, loans/AFR safe haven | No assurance of pricing method, documentation protection, rate or penalty outcome |
| Platform contributions/cost sharing, Parts VII–IX hybrids/covered debt/section 250/BEAT/GILTI | Specialist form completion; `us-gilti-fdii-beat`; do not use a gross-receipts shortcut or an obsolete form label as 2026 law |
| US-owned foreign corporations, partnerships or DEs, outbound section 367, bank/assets reporting | `us-form-5471-cfc-information`, separate Forms 8865/8858/367 analysis, `us-fbar-and-fatca-8938` |
| IRS notice/CP 215, examination/investigation, multiple delinquent years, claimed streamlined eligibility | Practitioner handles correction/penalty response and procedural deadlines; no relief guaranteed |
| Fiscal/short-year deadlines, June-ending transitions, special foreign-corporation extensions or disaster relief | Date hold; do not reuse the calendar dates below |

## Filing and payment

- Form 5472 accompanies the corporation's return, normally Form 1120 or 1120-F, by its due date including a valid extension. DEs use the pro forma 1120 described above. [Regulation 1.6038A-2(d)](https://www.ecfr.gov/current/title-26/section-1.6038A-2).
- Ordinary **calendar 2026** Form 1120/pro forma deadline is **15 April 2027**; timely valid Form 7004 ordinarily extends filing six months to **15 October 2027**. Calendar 1120-F is ordinarily 15 April 2027 with a US office/place of business, 15 June 2027 without; ordinary six-month requested extensions yield 15 October/15 December 2027 respectively. Special extension/fiscal-year rules remain held above. A weekend/legal holiday moves filing to the next business day. [6072](https://uscode.house.gov/us/usc/t26/s6072/), [7004 instructions](https://www.irs.gov/instructions/i7004), [1120-F instructions](https://www.irs.gov/instructions/i1120f).
- A foreign-owned US DE cannot e-file Form 5472. Fax the pro forma 1120 and attachment at **300 DPI or higher to 855-887-7737**, or mail to **Internal Revenue Service, 1973 Rulon White Blvd, M/S 6112 Attn: PIN Unit, Ogden, UT 84201**. Keep transmission/posting evidence. Its Form 7004 must be filed by the unextended due date to that same dedicated fax/address, with the Form 1120 code in Part I line 1 and “Foreign-owned U.S. DE” across the top; do not use the regular 7004 addresses. [DE filing instructions](https://www.irs.gov/instructions/i5472).
- Obtain the DE's own EIN. SS-4 line 9a: Other, “Foreign-owned U.S. disregarded entity-Form 5472”; line 10 Other: “Foreign-owned U.S. disregarded entity filing Form 5472”. Responsible party is an individual except government entities; line 7b takes “foreign”/N/A only if that party has no SSN/ITIN **and is ineligible to obtain one**. Online application requires its stated US-location and taxpayer-ID conditions; international applicants without a US/territory legal residence, principal business place or principal office/agency can use **267-941-1099**, Monday–Friday **6 a.m.–11 p.m. Eastern**, not toll-free. For applicants without a legal residence/principal business place/principal office/agency in a state/DC, fax from outside the US to **304-707-9471**; mail is also available. [SS-4 instructions](https://www.irs.gov/instructions/iss4).
- The pro forma DE return has no income-tax computation/payment; assess the owner's separate obligations independently. Form 7004 does not extend a real corporation's tax-payment time. [5472](https://www.irs.gov/instructions/i5472), [7004](https://www.irs.gov/instructions/i7004).

## Completion checklist

- Reconcile owners, attribution, foreign-person status, related parties and every transaction; apply only established exceptions, with one form per relevant party and the required attachments.
- Reconcile 1f/1g/1h, choose the correct direct/indirect Part II fields, complete III and line-conditioned VII; sign the correct return, use its filing channel and preserve timely filing/extension evidence.
- Keep permanent accurate records sufficient to establish the correct related-party treatment, as long as relevant/material and **no less than the applicable assessment and collection limitation period**. There is no universal seven-year release date. Under section 6501(c)(8), assessment cannot expire before three years after required information is furnished; reasonable cause **and no willful neglect** limit that extension to related items. Do not promise assessment closes automatically then. [Regulation 1.6038A-3(a), (g)](https://www.ecfr.gov/current/title-26/section-1.6038A-3), [6501(c)(8)](https://uscode.house.gov/us/usc/t26/s6501/).
- Subject to the applicable exemptions, a foreign related party's signed limited-agent authorization and the corporation's signed acceptance for sections 7602–7604 must be provided within 30 days of IRS request, with the regulation's wording. Failure to authorize or summons noncompliance may invoke section 6038A(e)'s determination of related-party deduction/property cost; do not infer the result without its conditions and procedure. Check this point with one of our partner accountants. [Regulation 1.6038A-5](https://www.ecfr.gov/current/title-26/section-1.6038A-5), [6038A(e)](https://uscode.house.gov/us/usc/t26/s6038A/).
- Missing/substantially incomplete filing, or required-record failure, attracts USD 25,000 per related party/year before relief. After more than 90 days from mailing notice, add USD 25,000 per 30 days **or fraction** of continuing failure, per affected party; reasonable-cause timing applies. Consolidated members have separate exposure and joint/several liability. Criminal penalties may apply to nonfiling or false/fraudulent information. [6038A(d)](https://uscode.house.gov/us/usc/t26/s6038A/), [Regulation 1.6038A-4](https://www.ecfr.gov/current/title-26/section-1.6038A-4), [IRS penalties](https://www.irs.gov/instructions/i5472).
- Reasonable cause requires an affirmative written showing of all facts under penalties of perjury, filed with the appropriate IRS official/service center, and IRS determination. Liberal treatment for gross receipts **USD 20,000,000 or less** requires no knowledge of the requirements, limited US presence/contact and prompt full compliance with IRS requests; size alone is no relief. [Regulation 1.6038A-4(b)](https://www.ecfr.gov/current/title-26/section-1.6038A-4).
- First-time abatement is not standalone Form 5472 relief. For a systemic initial penalty from a late Form 1120, the IRM permits linked relief if that 1120 penalty is abated under FTA (or would qualify but no penalty because no tax/fully paid), **and** no similar penalties and no late related Form 1120 in the prior three periods. Relief is not automatic. [IRM 20.1.9.5.5](https://www.irs.gov/irm/part20/irm_20-001-009).
- For delinquent returns, the IRS normal-procedure route requires no civil examination/criminal investigation and no prior IRS contact about those returns. Follow amended-income-return attachment and applicable filing instructions; a reasonable-cause statement can accompany each but does not ensure consideration before assessment. If already contacted, or no underlying income return exists, resolve the actual correction route with a practitioner. Check this point with one of our partner accountants. [IRS delinquent-return procedures](https://www.irs.gov/individuals/international-taxpayers/delinquent-international-information-return-submission-procedures).

## Sources

Read 27 November 2026 unless the claims ledger expressly identifies applicable completed proof reused from 26 November. The printed form is Rev. December 2023 and its instructions Rev. December 2024 as read; form labels do not establish substantive 2026 eligibility. Recheck the applicable filing-season revision before preparing a return.

| Official source | Operative material | Read on |
| --- | --- | --- |
| [26 USC 6038A](https://uscode.house.gov/us/usc/t26/s6038A/) | Ownership, relatedness, attribution, penalty, agent/noncompliance | 2026-11-27 |
| [26 USC 6038C](https://uscode.house.gov/us/usc/t26/s6038C/) | Foreign corporations engaged in US business | 2026-11-27 |
| [26 USC 318](https://uscode.house.gov/us/usc/t26/s318/) and [267](https://uscode.house.gov/us/usc/t26/s267/) | Attribution and relatedness | 2026-11-27 |
| [Regulation 301.7701-2](https://www.ecfr.gov/current/title-26/section-301.7701-2) | Domestic DE, indirect sole ownership, tax year | 2026-11-27 |
| [Regulation 1.6038A-1](https://www.ecfr.gov/current/title-26/section-1.6038A-1) | Definitions, aggregation, exemptions | 2026-11-27 |
| [Regulation 1.6038A-2](https://www.ecfr.gov/current/title-26/section-1.6038A-2) | Transactions, reporting, estimates, filing | 2026-11-27 |
| [Regulation 1.6038A-3](https://www.ecfr.gov/current/title-26/section-1.6038A-3) | Records and retention | 2026-11-27 |
| [Regulation 1.6038A-4](https://www.ecfr.gov/current/title-26/section-1.6038A-4) and [1.6038A-5](https://www.ecfr.gov/current/title-26/section-1.6038A-5) | Penalties, reasonable cause, authorization | 2026-11-27 |
| [Form 5472](https://www.irs.gov/pub/irs-pdf/f5472.pdf) and [instructions](https://www.irs.gov/instructions/i5472) | Printed lines, DE filing, identifiers, conditional questions | 2026-11-27 |
| [26 USC 6072](https://uscode.house.gov/us/usc/t26/s6072/), [1120-F](https://www.irs.gov/instructions/i1120f) and [7004 instructions](https://www.irs.gov/instructions/i7004) | Ordinary calendar deadlines and extensions; fiscal/special cases held | 2026-11-27 |
| [SS-4 instructions](https://www.irs.gov/instructions/iss4) | EIN application and channels | 2026-11-27 |
| [26 USC 6501(c)(8)](https://uscode.house.gov/us/usc/t26/s6501/) | Assessment; completed applicable proof reused | 2026-11-26 |
| [IRM 20.1.9.5.5](https://www.irs.gov/irm/part20/irm_20-001-009) and [delinquent procedures](https://www.irs.gov/individuals/international-taxpayers/delinquent-international-information-return-submission-procedures) | Procedural relief and limits | 2026-11-27 |

Not yet confirmed: case-specific residency, UK LLC characterization, dividend-only reporting, treaty/withholding outcomes and the specialist/fiscal-year matters listed above remain non-usable holds. No unconfirmed rate, exemption or filing conclusion is supplied for them. Check this point with one of our partner accountants.
