---
name: us-nonresident-cgt
description: Determine federal tax and FIRPTA withholding on a nonresident individual's 2026 property gains. Covers US real property interests, ECI, the separate capital-gains presence test, residence-buyer withholding, certificates and reporting. Trigger on "FIRPTA", "nonresident capital gains", "183-day rule", "USRPI", "8288-B" or "W-8BEN broker". Use us-tax-residency to establish status first.
version: "2.1"
jurisdiction: US
tax_year: 2026
last_updated: 2026-11-26
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: situation-rules
---

# US capital gains of nonresident alien individuals: 2026

A nonresident's US real property gain follows the effectively connected income rules; other investment gains require separate checks of source, business connection and actual days present. Withholding is a payment toward tax, so it can exceed the final liability.

## Scope and who this is for

Federal individual gains for a person established to be a nonresident throughout 2026. Do not infer status from an F, J, M, Q, A or G visa: establish eligibility and applicable time limits with `us-tax-residency`. A dual-status year or doubtful treaty tie-breaker goes to R-NRCG-RES. A properly established dual-resident treaty claim requires Form 1040-NR with Form 8833 and computation as a nonresident ([Publication 519](https://www.irs.gov/publications/p519)).

Use `us-capital-gains` for citizens/residents; `us-form-1040-nr-nonresident-return` for the complete return; `us-itin-form-w-7` for identification; `us-installment-sale-6252` for installment-sale intake; `us-schedule-e-rental-income` for prior rentals/elections; and `us-expatriation-exit-tax` for former citizens/long-term residents. Specialist routes below are holds, not conclusions supplied by those other Guides.

**Circular 230 §10.37:** General written tax information, based on the stated facts and sources. Establish the taxpayer's actual facts and applicable law before using a filing position; do not assume eligibility or assume a position will escape examination.

## Ask the client first

- Obtain status evidence and US travel dates for 2026, 2025 and 2024. Count actual 2026 presence separately from residency-test days; identify exempt-individual eligibility.
- Establish the tax home from work, living arrangements, intended duration and later changes. Do not assume a foreign or US tax home when evidence is missing.
- Identify each asset, acquisition/disposal dates, adjusted basis, selling costs, prior depreciation/rental elections, and whether it was personal-use or business property.
- For company/fund shares, obtain class, market, full ownership history, related/indirect holdings and corporate USRPHC evidence. For entities or partnership/LLC interests, use the referral table.
- Identify all US business activities, offices, employees and agents; distinguish a securities dealer from own-account investing.
- For property, obtain total consideration including debt, each seller's contribution/status, the buyer's individual status and detailed residence plans, TINs, contract/closing dates and certificate applications.
- Obtain treaty residence/eligibility evidence and the actual treaty article, broker documentation, states of property/work/residence and any other income or deductions. Missing facts remain missing; do not choose favourable defaults.

## The method, step by step

### Rates, bands and thresholds

| Item and operative conditions | 2026 rate / amount | Official source |
| --- | --- | --- |
| Non-ECI US-source capital-asset gains within section 871(a)(2), actual presence at least 183 days in the tax year; special section 871(a)(1) gains excluded | 30% of eligible net gain, unless an applicable treaty provides relief | [26 U.S.C. 871(a)(2)](https://uscode.house.gov/us/usc/119-142/t26/s871/) |
| USRPHC asset test: USRPIs / (USRPIs + foreign real property + other business-use assets), all at fair market value | At least 50%; corporate interests still need the look-back, ownership and exceptions below | [26 U.S.C. 897(c)(2)](https://uscode.house.gov/us/usc/119-142/t26/s897/) |
| FIRPTA general withholding on foreign seller's amount realized; absent a valid exception/certificate | 15% | [26 U.S.C. 1445(a)](https://uscode.house.gov/us/usc/119-142/t26/s1445/) |
| Individual residence buyer satisfying the use test below; total property amount realized at most USD 300,000 | No FIRPTA withholding | [26 U.S.C. 1445(b)(5)](https://uscode.house.gov/us/usc/119-142/t26/s1445/) |
| Same residence conditions; total more than USD 300,000 and at most USD 1,000,000 | 10%; above that ceiling, general rate | [26 U.S.C. 1445(c)(4)](https://uscode.house.gov/us/usc/119-142/t26/s1445/) |
| Ordinary long-term capital gain of a single filer, including qualifying ECI: taxable-income ceilings for the zero / 15% bands | USD 49,450 / USD 545,500; stack gains above other taxable income | [Rev. Proc. 2025-32 §2.03](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf); [capital-gains method](https://www.irs.gov/taxtopics/tc409) |

### 1. Identify US real property interests before applying the presence test

A USRPI includes an interest other than solely as creditor in US or US Virgin Islands real property, including land, buildings, mines, wells and natural deposits. Associated personal property is also within the definition, but equipment/furnishings and separate-disposal exclusions require R-NRCG-ASSOC. A gain/loss from a USRPI is treated as ECI under section 897(a), whether or not the property is a capital asset ([26 U.S.C. 897(a), (c)](https://uscode.house.gov/us/usc/119-142/t26/s897/)).

A noncreditor interest in a domestic corporation is within the USRPI definition unless the taxpayer establishes that the corporation was never a USRPHC in the shorter of the holding period after June 18, 1980 and the five years ending on disposition, subject to statutory exclusions. Obtain evidence rather than presume that absence of a certificate proves the actual tax outcome ([section 897(c)(1)](https://uscode.house.gov/us/usc/119-142/t26/s897/)).

For the class actually **regularly traded on an established securities market**, the listed-stock exception is lost only if ownership exceeded 5% at some time in that same testing period; for REIT stock the threshold is more than 10%. Include constructive ownership under section 897(c)(6)(C), as modified by (k)(1), before deciding the threshold. A listed company does not make every class regularly traded. For actual USRPHC analysis, large/indirect holdings or any other REIT/RIC exception, use R-NRCG-USRPHC ([section 897(c)(3), (6)(C), (k)(1)](https://uscode.house.gov/us/usc/119-142/t26/s897/)).

### 2. Check ECI and distinguish the trading safe harbours

For US-source capital gains, section 864(c)(2) considers assets used/held for the US business **and** whether business activities were a material factor in realizing the gain. Do not classify a foreign-source sale by asset use alone; refer nonstandard source/business cases. The independent-agent safe harbour and own-account safe harbour are separate:

- Section 864(b)(2)(A)(i) covers securities trading through a resident broker/other independent agent, subject to no US office through/by whose direction those trades occur at any time in the year.
- Section 864(b)(2)(A)(ii) separately covers a **nondealer's own-account** securities trading, personally, through employees or agents, including discretionary agents. The office limitation in (C) applies to (A)(i), not (A)(ii). This does not exempt other US business activity or turn a USRPI into an exempt asset.

Source: [26 U.S.C. 864(b)(2), (c)(2)](https://uscode.house.gov/us/usc/119-120/t26/s864/), read with [Publication 519, Trading for a nonresident alien's own account](https://www.irs.gov/publications/p519). Partnership/LLC sales go to R-NRCG-PSHIP.

### 3. Source other gains, then apply the separate capital-gains presence rule

Under section 865(a), (g), ordinary personal-property investment gains generally follow tax-home residence for this sourcing purpose: an NRA with a US tax home is a US resident for that purpose. This is not the income-tax residency test. A foreign tax home generally gives foreign-source gains, but US-office-attributable sales, inventory, depreciable property, intangibles and treaty re-sourcing have special rules; do not apply the generalisation to them. Check this point with one of our partner accountants. ([26 U.S.C. 865](https://uscode.house.gov/us/usc/119-142/t26/s865/))

For the remaining non-ECI US-source capital gains, section 871(a)(2) uses **actual presence of 183 days or more in that tax year**, including exempt-individual days. It bears no relation to the weighted substantial-presence residency test. Exactly 183 qualifies; transactions while abroad can still count. Establish tax home from the facts; the IRS describes the general shift on arrival for someone intending to be away from the old home for longer than one year, subject to the actual programme/employment and intentions ([IRS students/scholars guidance](https://www.irs.gov/individuals/international-taxpayers/the-taxation-of-capital-gains-of-nonresident-alien-students-scholars-and-employees-of-foreign-governments)).

Net eligible US-source gains against eligible US-source losses only to the extent they would be recognized/taken into account as ECI. Exclude personal-use losses, loss carryovers, losses above gains and the section 1202 exclusion. Do not double-count gains taxed under section 871(a)(1) or (b). Below 183 days, the ordinary gains covered by (a)(2) are exempt; that conclusion does not extend to OID, contingent intellectual-property payments or other special (a)(1) gains (R-NRCG-SPECIAL). If not engaged in US business and no tax year was previously established, use a calendar year for this test ([section 871(a)(2)](https://uscode.house.gov/us/usc/119-142/t26/s871/); [Publication 519, Sales or Exchanges of Capital Assets](https://www.irs.gov/publications/p519)).

### 4. Compute ECI tax separately from withholding

ECI is taxed after allowable deductions at citizen/resident rates; use the applicable capital-gain computation for qualifying gains. Nonresidents generally cannot claim a standard deduction, but treaty-eligible Indian students/business apprentices have a special rule: do not assume it applies. USRPI losses remain subject to section 165(c), so a personal-use home loss is not deductible. Nonresident aliens are excluded from NIIT under section 1411(e)(1); treaty-resident elections and dual-status cases require separate review. Home exclusions, depreciation/recapture and the FIRPTA minimum-tax calculation are held below ([Publication 519](https://www.irs.gov/publications/p519); [section 897(b)](https://uscode.house.gov/us/usc/119-142/t26/s897/); [section 1411(e)](https://uscode.house.gov/us/usc/119-142/t26/s1411/)).

### 5. Withhold using the total transaction and proven residence plans

The buyer generally is the withholding agent and can be liable for failing to withhold. Amount realized is cash paid/to be paid (principal), fair market value of other property, and liabilities assumed or to which the property is subject. Allocate between co-sellers by capital contribution; spouses count as contributing half each. Withhold on the foreign sellers' allocated amount. Foreign sellers must request an agreed credit allocation by the tenth day after transfer; otherwise divide the credit evenly ([IRS FIRPTA guidance](https://www.irs.gov/individuals/international-taxpayers/firpta-withholding)).

The residence thresholds test the **whole property's amount realized**, not each seller's allocated share. The actual buyer must be an individual with definite plans for the buyer/family to reside there for at least 50% of all days anyone uses it in **each** of the first two 12-month periods after transfer; ignore vacant days. A mere label or signature does not establish those facts. The test does not require a principal home. An investor/company buyer has no residence reduction, although another valid exception/certificate may apply ([Form 8288 instructions, residence rules](https://www.irs.gov/instructions/i8288); [IRS FIRPTA FAQ 6, 17](https://www.irs.gov/individuals/international-taxpayers/firpta-withholding)).

An assignment of a right to purchase US real property is also subject to FIRPTA withholding on its amount realized ([IRS FIRPTA FAQ 4](https://www.irs.gov/individuals/international-taxpayers/firpta-withholding)). Other exceptions require the separate review below; absence of withholding does not itself exempt taxable gain.

### 6. Consider a certificate; document broker status

The buyer, buyer's agent or seller may request a withholding certificate, including where withholding exceeds maximum tax liability or gain is exempt. IRS generally acts within 90 days of receiving a **complete** application including all parties' TINs. A seller applying must notify the buyer in writing on or the day before transfer ([IRS withholding certificates](https://www.irs.gov/individuals/international-taxpayers/withholding-certificates)).

An application filed on/before transfer and still pending **does not remove withholding at closing**. It postpones reporting/payment to the IRS until 20 days after the IRS mails the certificate or denial; pay the amount withheld or approved lesser amount. A delay-purpose application triggers interest/penalties from day 21 after transfer. Report gain in the actual sale year even if certificate processing changes the date on Form 8288-A ([IRS reporting/payment](https://www.irs.gov/individuals/international-taxpayers/reporting-and-paying-tax-on-us-real-property-interests); [FIRPTA FAQ 3](https://www.irs.gov/individuals/international-taxpayers/firpta-withholding)).

Give the broker a properly completed W-8BEN to establish foreign status and claim the applicable reporting/backup-withholding exception. It generally lasts through the last day of the third succeeding calendar year unless circumstances change; some conditions allow indefinite validity. ECI generally requires W-8ECI instead, with the partnership allocation exception in the instructions. W-8BEN is not proof that the gain is tax exempt ([W-8BEN instructions](https://www.irs.gov/instructions/iw8ben)). Non-ECI US dividends are generally subject to 30% or applicable treaty relief, separately from stock-sale gains ([Publication 519, The 30% Tax](https://www.irs.gov/publications/p519)).

## Boundary and exception table

| Facts established | Result |
| --- | --- |
| Actual presence exactly 183 days, ordinary non-ECI US-source gain | The section 871(a)(2) test is met; establish treaty relief separately |
| Foreign tax home, ordinary investment sale with no special sourcing rule | Foreign-source gain, outside that test |
| F-1 student present 200 days | Confirm NRA eligibility separately; exempt-individual days still count for gains |
| Regularly traded class held at exactly 5% throughout the applicable period, including constructive holdings | Listed-stock exception remains; REIT threshold instead exceeds 10% |
| Residence buyer, total exactly USD 300,000 / USD 1,000,000 | No withholding / 10%, if the actual residence test is met and no different certificate applies |
| Personal-use US home sold at a loss | No deduction; withholding may still require a certificate |

## Worked cases

Illustrations retain the original 2026 facts. Apply the conditions above; treaty, AMT, state tax and special assets require separate clearance.

**Case 1: certificate decision.** Vacant US land, never depreciated/not rented, sold to an investor for USD 750,000; adjusted basis USD 640,000, selling costs USD 40,000. Gain is USD 70,000 and statutory withholding USD 112,500. **If** the original long-term classification is established, the seller qualifies as single, and there is no other taxable income/deduction, ordinary federal capital-gain tax before AMT/state tax is USD 3,082.50: 15% of USD 20,550 above the USD 49,450 zero-rate ceiling. The difference is USD 109,417.50. Without a certificate, claim excess withholding through the return; applying by transfer preserves the pending-application payment deferral, but releases that difference at closing **only if an appropriate certificate is obtained in time**. Do not promise release merely because an application was filed. Check this point with one of our partner accountants. ([Publication 544, Sales and Exchanges](https://www.irs.gov/publications/p544); [Rev. Proc. 2025-32](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf); [IRS reporting/payment](https://www.irs.gov/individuals/international-taxpayers/reporting-and-paying-tax-on-us-real-property-interests))

```oa-check
name: FIRPTA withholding against the likely tax (2026)
inputs:
  amount_realized: 750000
  basis: 640000
  selling_costs: 40000
  zero_rate_top: 49450
steps:
  - withholding: amount_realized * 0.15
  - gain: amount_realized - basis - selling_costs
  - tax: max(gain - zero_rate_top, 0) * 0.15
  - excess_withheld: withholding - tax
expected:
  withholding: 112500.00
  gain: 70000.00
  tax: 3082.50
  excess_withheld: 109417.50
```

**Case 2: residence band, co-sellers and actual presence.** (a) Condo consideration: USD 520,000 cash plus USD 230,000 assumed mortgage = USD 750,000. An individual buyer satisfying the residence test gives USD 75,000 withholding; an investor gives USD 112,500, absent another valid exception/certificate. (b) Foreign/US spouses sell for USD 500,000 total to a qualifying residence buyer: the foreign spouse's USD 250,000 half gives USD 25,000 withholding, not an exemption based on that half alone. (c) An F-1 student, separately established to remain an NRA with a US tax home, present 200 days in 2026: ordinary non-ECI US-source gains USD 12,000 less eligible current-year US-source losses USD 2,000 give USD 3,000 tax on Schedule NEC, absent treaty relief. Do not presume exempt-individual status from the visa or presume all losses qualify; treaty/disclosure eligibility is R-NRCG-TREATY. ([IRS FIRPTA guidance](https://www.irs.gov/individuals/international-taxpayers/firpta-withholding); [IRS student gains guidance](https://www.irs.gov/individuals/international-taxpayers/the-taxation-of-capital-gains-of-nonresident-alien-students-scholars-and-employees-of-foreign-governments))

```oa-check
name: FIRPTA rates and the 183-day rule (2026)
inputs:
  cash: 520000
  assumed_mortgage: 230000
  joint_total: 500000
  gains: 12000
  losses: 2000
steps:
  - amount_realized: cash + assumed_mortgage
  - residence_withholding: amount_realized * 0.10
  - investor_withholding: amount_realized * 0.15
  - foreign_spouse_withholding: joint_total * 0.5 * 0.10
  - tax_183_day: max(gains - losses, 0) * 0.30
expected:
  amount_realized: 750000.00
  residence_withholding: 75000.00
  investor_withholding: 112500.00
  foreign_spouse_withholding: 25000.00
  tax_183_day: 3000.00
```

**Other original cases.** Listed shares, 20 days in the US, no US office/tax home, well under 5%: if full-period/constructive ownership and nondealer own-account/no-other-business conditions establish the ordinary non-USRPI, non-ECI outcome, no federal gain tax or gain-only return obligation. Keep W-8BEN current; other income can independently require a return. A qualifying residence buyer at exactly USD 300,000 gives no withholding, but taxable USRPI gain still needs reporting. At exactly USD 1,000,000 the withholding is USD 100,000. An investor at USD 280,000 gives USD 42,000, absent another exception/certificate.

```oa-check
name: Original withholding boundaries (2026)
inputs:
  residence_lower: 300000
  residence_upper: 1000000
  investor_price: 280000
steps:
  - lower_withholding: residence_lower * 0
  - upper_withholding: residence_upper * 0.10
  - investor_withholding: investor_price * 0.15
expected:
  lower_withholding: 0
  upper_withholding: 100000
  investor_withholding: 42000
```

## When to refuse or refer

Every row below is an explicit hold: **Check this point with one of our partner accountants.** Do not supply a numerical entitlement from these topics until resolved.

| Code | Topic held for that review |
| --- | --- |
| R-NRCG-RES | Unclear residence, exempt-individual limits, closer connection, treaty tie-breaker/election or dual-status year; `us-tax-residency` |
| R-NRCG-ENTITY | Corporate, partnership, trust/estate sellers or property held through entities; section 1445(e) |
| R-NRCG-USRPHC | Corporate asset valuation/look-through, unlisted or large/constructive holdings; cleansing including predecessor corporations; domestically controlled QIE, REIT/RIC qualified-shareholder/cut-back, foreign-corporation domestic election and QIE wash-sale rules |
| R-NRCG-ASSOC | Associated personal property, separate sales and timing exceptions |
| R-NRCG-PSHIP | Partnership/LLC interest sales; sections 864(c)(8), 1446(f), withholding exceptions and PTP rules |
| R-NRCG-NONREC | Installment sales, exchanges, other nonrecognition, security agreements and specialist certificate categories |
| R-NRCG-HOME | Section 121 former-home exclusion, eligibility, limits, nonqualified use and depreciation |
| R-NRCG-RECAPTURE | Depreciated/rented property, capital versus ordinary gain, recapture and unrecaptured section 1250 gain; `us-capital-gains` |
| R-NRCG-AMT | FIRPTA alternative minimum tax/section 897(a)(2), Form 6251 and final certificate tax estimate |
| R-NRCG-TREATY | Actual treaty entitlement/articles, USRPI or personal-property relief; Form 8833 disclosure, exceptions and penalties |
| R-NRCG-WHEX | Nonforeign/corporate certifications, listed-corporation withholding exceptions, nonrecognition/treaty notices, zero consideration and government acquisitions; never equate these with automatic gain exemption |
| R-NRCG-SPECIAL | Special section 871(a)(1) gains, OID, portfolio-interest exemption, intellectual property, natural-resource gains, nonstandard source/ECI cases |
| R-NRCG-EXPAT | Former citizens/long-term residents; estate/gift tax; `us-expatriation-exit-tax`, `us-estate-gift-706-709` |
| R-NRCG-STATE | All state tax/withholding questions |

## Filing and payment

- **Buyer:** file Form 8288 Part I, attach Forms 8288-A Copies A/B for each person withheld from, retain Copy C, and transmit tax by day 20 after transfer. Send to the address in the current instructions. The pending-certificate exception above changes remittance timing, not the closing withholding obligation. Late filing/payment and failure to withhold can create tax, interest and penalties; specific penalty computation requires accountant review ([Form 8288 instructions](https://www.irs.gov/instructions/i8288)).
- **Seller:** ordinary taxable non-ECI capital gains go on Schedule NEC; ECI capital-asset gains go on Schedule D and/or Form 4797 as appropriate, attached to Form 1040-NR. A taxable FIRPTA disposition requires return/reporting even if withholding was nil. Claim withholding using stamped Form 8288-A Copy B; without a TIN the IRS does not issue that stamped copy. To claim credit without it, attach substantial evidence of withholding and a statement with required 8288/8288-A information including TIN. If eligible for an ITIN, apply with completed Forms W-7/8288-B using the W-7 instructions ([Publication 519](https://www.irs.gov/publications/p519); [IRS reporting/payment](https://www.irs.gov/individuals/international-taxpayers/reporting-and-paying-tax-on-us-real-property-interests)).
- **Ordinary calendar-year deadlines:** with wages subject to US income-tax withholding, April 15, 2027 for 2026; otherwise June 15, 2027. A timely Form 4868 ordinarily extends filing six months, to October 15 / December 15, 2027 respectively, not payment. These are calendar applications of the continuing fourth/sixth-month rules, not a claim to have read final 2026 return instructions; special relief requires separate review ([Publication 519, Nonresident Aliens: When To File](https://www.irs.gov/publications/p519)).
- **2025 returns:** ordinary dates were April 15 / June 15, 2026 respectively; timely extensions give October 15 / December 15, 2026. October's date has passed as of this read. Do not apply the 2026 capital-gain ceiling to 2025 ([Publication 519](https://www.irs.gov/publications/p519)).
- **Estimated tax, final 2026 form fields and refund timing:** Check this point with one of our partner accountants. Preserve the Form 1040-ES (NR) route; do not assume withholding covers liability, promise a refund date, or carry the old 2025 line 25f into a final 2026 filing without checking the issued form.

## Completion checklist

- [ ] Status, actual presence and tax home established separately; source/ECI/USRPI classification documented.
- [ ] Original transaction inputs reconciled; applicable stock testing period and constructive holdings checked.
- [ ] Residence conditions and whole-transaction threshold documented; buyer withholding and seller tax computed separately.
- [ ] Certificate timing, all TINs, reporting deadlines and withholding evidence checked.
- [ ] Specialist/treaty/state holds resolved by an accountant before using those outcomes.

## Sources

Read dates record the passages actually read, including reused applicable exact quotations from the completed residency/1040/capital-gains proof; no download-status-only evidence is used.

| Official source | Passages read / reused | Read on |
| --- | --- | --- |
| [26 U.S.C. 871](https://uscode.house.gov/us/usc/119-142/t26/s871/) | Read for: (a)(1), (a)(2), (b): special gains, actual-presence test, netting, ECI; current text through Public Law 119-142 | 2026-11-26 |
| [26 U.S.C. 864](https://uscode.house.gov/us/usc/119-120/t26/s864/) | Read for: (b)(2)(A), (C), (c)(2): distinct trading limbs and ECI factors; continuing wording also read in Pub. 519 | 2026-11-26 |
| [26 U.S.C. 865](https://uscode.house.gov/us/usc/119-142/t26/s865/) | Read for: (a)–(g): source rules, tax-home definition and exceptions | 2026-11-26 |
| [26 U.S.C. 897](https://uscode.house.gov/us/usc/119-142/t26/s897/) | Read for: (a)–(c), (k)(1): ECI, losses, USRPI, stock thresholds and constructive ownership | 2026-11-26 |
| [26 U.S.C. 1445](https://uscode.house.gov/us/usc/119-142/t26/s1445/) | Read for: (a), (b)(5), (c)(4): general withholding and residence thresholds | 2026-11-26 |
| [26 U.S.C. 1411](https://uscode.house.gov/us/usc/119-142/t26/s1411/) | Read for: (e)(1): NRA exclusion | 2026-11-26 |
| [Rev. Proc. 2025-32](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) | Read for: §2.03, 2026 single capital-gain ceilings; same completed US1040/USCG quotation reused | 2026-11-26 |
| [IRS capital-gains overview](https://www.irs.gov/taxtopics/tc409) | Read for: Gain/basis, personal-use losses, long-term/short-term and stacking; same completed USCG quotations reused | 2026-11-26 |
| [Publication 544 (2025)](https://www.irs.gov/publications/p544) | Read for: Sales and Exchanges, Amount realized, Example 1 selling expenses deducted before basis | 2026-11-26 |
| [Publication 519 (2025)](https://www.irs.gov/publications/p519) | Read for: Trading, ECI, capital gains/netting/reporting, deductions/India exception, dual-resident treaty filing and nonresident deadlines; continuing rules only | 2026-11-26 |
| [IRS student/scholar capital gains](https://www.irs.gov/individuals/international-taxpayers/the-taxation-of-capital-gains-of-nonresident-alien-students-scholars-and-employees-of-foreign-governments) | Read for: Separate presence test, exempt days, tax home and Schedule NEC | 2026-11-26 |
| [IRS FIRPTA guidance](https://www.irs.gov/individuals/international-taxpayers/firpta-withholding) | Read for: USRPI/amount realized, liability, FAQs 1, 3, 4, 6 and 17 | 2026-11-26 |
| [Form 8288 instructions (January 2026)](https://www.irs.gov/instructions/i8288) | Read for: Residence conditions, joint sellers, Part I, forms/copies, deadlines and pending certificates | 2026-11-26 |
| [IRS reporting/payment](https://www.irs.gov/individuals/international-taxpayers/reporting-and-paying-tax-on-us-real-property-interests) | Read for: Pending certificate, delay penalties, stamped copy/credit evidence and ITIN route | 2026-11-26 |
| [IRS withholding certificates](https://www.irs.gov/individuals/international-taxpayers/withholding-certificates) | Read for: Applicants, complete application/90 days and seller notification | 2026-11-26 |
| [W-8BEN instructions](https://www.irs.gov/instructions/iw8ben) | Read for: Broker documentation, validity and ECI/partnership exception | 2026-11-26 |

Not yet confirmed: final 2026 Form 1040-NR field numbers and the specialist outcomes expressly held in the referral table and estimated-tax/refund paragraph. Those outcomes are not usable advice; Check this point with one of our partner accountants.
