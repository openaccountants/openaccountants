---
name: za-provisional-tax
description: >
  Use this South Africa provisional tax reference to work through Part III of
  the Fourth Schedule to the Income Tax Act 58 of 1962 for individuals,
  including the self-employed: who is a provisional taxpayer, estimates, basic
  amount, IRP6 returns, payments, underestimation penalty and interest. Match
  requests about IRP6, provisional tax, SARS provisional, estimated tax South
  Africa, first provisional period, second provisional period, third
  provisional and underestimation penalty. The enacted paragraph 20 threshold
  is R1 million; the R1.8 million figure and the late-payment rule sit in Bill
  B33-2026, and the 2026/27 rate table and rebates sit in Bill B34-2026. No Act
  read at 5 November 2026 enacts them, so each is shown as held. This Tier 2
  draft supports source checking and reviewer questions; it does not authorise
  filing, payment or a tax position.
version: 2.2
jurisdiction: ZA
tax_year: 2026
tax_year_notes: "2026/27 (2027 year of assessment, 1 March 2026 to 28 February 2027). The enacted rate table in Act 3 of 2026 and the rebates in section 6 are shown beside the 2026/27 amounts announced on 25 February 2026 and billed in B34-2026. The R1.8 million paragraph 20 threshold and the late-payment rule are billed in B33-2026 and held. Editing in November 2026 does not establish 2026/27 law."
last_updated: 2026-11-05
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
domain: income-tax
---

# ZA Provisional Tax v2.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

This reference covers South African provisional tax for natural persons, in rand only, under Part III of the Fourth Schedule to the Income Tax Act 58 of 1962 (the Act), with the Tax Administration Act 28 of 2011 (TA Act). Provisional tax is not a separate tax. SARS (South African Revenue Service) treats it as an advance payment of normal tax, set off on assessment (Interpretation Note 1, Issue 3, part 2). 'Paragraph' or 'para' means a paragraph of the Fourth Schedule.

A year of assessment for a natural person runs from 1 March to the last day of February, and SARS names a year by the year it ends in. The 2027 year of assessment is 1 March 2026 to 28 February 2027, written 2026/27 here.

Companies fall under para 23 and are outside this guide. Trusts are persons other than companies, so para 1 can reach them, but this guide does not work their rates or credits.

### Who is a provisional taxpayer

Para 1 makes these persons provisional taxpayers:

- **Limb (a):** any person other than a company who derives (i) remuneration from an employer not registered under para 15, or (ii) any amount that is not remuneration or an allowance or advance under section 8(1).
- **Limb (b):** any company.
- **Limb (c):** any person the Commissioner notifies.

Para 1 then excludes each of these:

- (aa) an approved public benefit organisation
- (bb) an approved recreational club
- (cc) a body corporate, share block company or association of persons under section 10(1)(e)
- (dd)(A) a non-resident owner or charterer of ships or aircraft within section 33
- (dd)(B) a natural person who derives no income from carrying on any business, if either (AA) taxable income for the year does not exceed the tax threshold, or (BB) taxable income derived from interest, dividends, foreign dividends, rental from letting fixed property and remuneration from an unregistered employer does not exceed R30,000
- (ee) a small business funding entity
- (ff) a deceased estate
- (gg) an entity approved under section 30B

The no-business condition governs both (AA) and (BB). A self-employed person below the tax threshold stays a provisional taxpayer. Para 18 was repealed by section 15 of Act 23 of 2015 and is not the source of this exclusion.

| Person | Result | Ground |
| --- | --- | --- |
| Self-employed person or sole proprietor | Yes, at any income level | Limb (a)(ii); business income defeats (dd)(B) |
| Freelancer or contractor | Yes, if the fees are not remuneration | Limb (a)(ii); check para 1 'remuneration' exclusion (ii) for independent trade first |
| Rental income recipient with no business | Yes, unless (AA) or (BB) is met | Limb (a)(ii), (dd)(B). Whether a letting activity is itself a business is a fact question held for a reviewer |
| Non-executive director, resident | Yes, unless (AA) or (BB) is met; held | BGR 40 part 4: fees are not remuneration, so no employees' tax. The ruling applies from 1 June 2017 until it is withdrawn, amended or the relevant legislation is amended. If the person derives no income from carrying on a business, (dd)(B) excludes them where (AA) or (BB) is met, and these fees are not a (BB) category, so fees alone do not fail (BB). SARS's VAT12 FAQ answer 21 says the liability must be settled through the provisional tax system, but does not address (dd)(B), and no text read says whether director's fees are business income |
| Non-executive director, non-resident | Not settled here | BGR 40 part 4 does not apply to non-resident directors |
| Executive director paid through payroll | Not on the director's pay alone | A director paid through payroll receives remuneration and is an employee under para 1 'employee' limb (a). SARS Guide G01 section 4(a) cites limb (g) instead, but that limb was deleted by section 4(1) of Act 22 of 2018, effective 1 March 2019. G01 section 4(b) says directors of private companies and close corporation members are not automatically provisional taxpayers unless they have other business income |
| Salaried employee, registered employer, no other income | No | No limb (a) income |
| Employee of an unregistered employer | Yes, unless (AA) or (BB) is met | Limb (a)(i). With no business income, (dd)(B) can still exclude the person, and (BB) counts this remuneration towards the R30,000. See Cross-border points |
| Natural person with no business and taxable income at or below the tax threshold | No | (dd)(B)(AA). Age sets the threshold; see the thresholds table |

An employee of a registered employer with other non-business income is excluded if either limb is met. With R40,000 of taxable rent on top of R300,000 salary, taxable income exceeds the tax threshold and the rent exceeds R30,000, so the person is a provisional taxpayer. With R25,000 of taxable rent, limb (BB) is met and the person is excluded. Para 1 sets out the exclusions after limb (c), so whether a Commissioner's notice overrides an exclusion is held.

SARS's provisional tax page says exempt interest below R23,800 (under 65) or R34,500 (65 and older) and exempt tax-free savings account amounts do not make a person a provisional taxpayer. That page omits dividends from the R30,000 limb; para 1 includes them. SARS Guide G01 part 2(a)(iv) lists a labour broker with a para 2(5)(a) exemption certificate as a provisional taxpayer. The para 1 'provisional taxpayer' text read has no such limb, so that inclusion is held.

Provisional taxpayer status follows from para 1. There is no registration or deregistration process. The onus is on the taxpayer to decide whether they are liable and to request and submit an IRP6 (SARS provisional tax page, Interpretation Note 1 part 4.1). SARS may also change a person's status on its systems in either direction from the ITR12 return and confirm it by letter; the person must still evaluate their income each year (G05 section 13.2).

### What this file is

This is a Tier 2 source-cited draft. It has no accountant sign-off. Every figure carries its own citation and should be confirmed against it. It loads no workflow base, because none was qualified for this guide in this conversion; do not treat it as a complete operational workflow.

### How to read the 2026/27 amounts

Use these status words. A held amount may be used only in a conditional working, side by side with the enacted amount, and only with a reviewer.

- **Enacted** means the amount is in an Act or the Act's text as read.
- **Announced** means Budget Review 2026, tabled on 25 February 2026, proposes the amount.
- **Billed** means a Bill introduced on 21 October 2026 proposes the amount. A Bill is not law.
- **Provisionally effective** is a reading, not a settled fact. Sections 5(2) and 6(6) let an alteration announced in the national annual budget take effect on the announced date for 12 months, subject to Parliament passing legislation within that time. Para 20 has no such mechanism in the text read.

Rates need a separate step. Para 17(4) computes the estimated liability at the relevant rate in force for the year on the date of payment; if that rate has not been fixed, at the rate foreshadowed by the Minister in the budget statement; and if neither, at the rate in force for the latest preceding year with fixed rates. Act 3 of 2026 fixes a table for years commencing on or after 1 March 2025, and SARS publishes the Bill's table as its 2027 table. Which table para 17(4) selects at each payment date is held, so every 2026/27 working below shows both. SARS Guide G02 says eFiling calculates the tax and rebates on the return.

### Refer or stop

- **R-ZA-PROV-1, tax dispute or objection.** Trigger: the client wants to object to a SARS penalty. Message: 'Objections to SARS penalties require qualified tax practitioner review. Escalate.'
- **R-ZA-PROV-2, company provisional tax.** Trigger: a question about company provisional tax. Message: 'This skill covers individuals only. Companies have different rules: para 23 for payments and the R20,000 figure in section 89quat.'

### Standing rules

- Never estimate without asking about all income sources.
- Never tell a client that the basic amount protects them where final taxable income exceeds the para 20 threshold. The threshold tests taxable income as finally determined, so the client cannot know the result when estimating near the line.
- Never say an estimate within tolerance protects against late payment. Enacted law charges the 10% para 27 penalty and section 89bis interest on the late amount. Never say the 20% underestimation penalty applies to a day-late payment: that is neither enacted nor what B33-2026 proposes.
- Never ignore employees' tax credits.
- Never confuse the underestimation penalty, fixed by payments to the end of the year, with section 89quat interest, which a third payment can reduce.
- Never treat the third payment as mandatory.
- Never present provisional tax as a separate tax.
- Never compute the underestimation penalty without the final estimate, final taxable income, the basic amount and payments made by the end of the year.
- Never use a prescribed interest rate without reading the current SARS tables.

### Reviewer flags

Use these forms when a point needs a reviewer or sits outside this guide.

```
REVIEWER FLAG
Tier: T2
Client: [name]
Situation: [description]
Issue: [what is ambiguous]
Options: [possible treatments]
Recommended: [most likely correct treatment and why]
Action Required: Qualified tax practitioner must confirm before advising client.
```

```
ESCALATION REQUIRED
Tier: T3
Client: [name]
Situation: [description]
Issue: [outside skill scope]
Action Required: Do not advise. Refer to qualified tax practitioner. Document gap.
```

## Rates, bands and thresholds

### Enacted rate table for natural persons

Act 3 of 2026, section 2(3)(a) and Schedule I para 1, applies to any year of assessment commencing on or after 1 March 2025, for taxable income other than lump sums and severance benefits.

| Taxable income | Tax | Source | URL |
| --- | --- | --- | --- |
| Up to R237,100 | 18% | Act 3 of 2026, Schedule I para 1. Enacted | https://www.sars.gov.za/legal-lprim-aa-2026-01-rates-and-monetary-amounts-and-amendment-of-revenue-laws-act-3-of-2026-gg-54446-1-april-2026/ |
| R237,100 to R370,500 | R42,678 + 26% above R237,100 | same | same |
| R370,500 to R512,800 | R77,362 + 31% above R370,500 | same | same |
| R512,800 to R673,000 | R121,475 + 36% above R512,800 | same | same |
| R673,000 to R857,900 | R179,147 + 39% above R673,000 | same | same |
| R857,900 to R1,817,000 | R251,258 + 41% above R857,900 | same | same |
| Above R1,817,000 | R644,489 + 45% above R1,817,000 | same | same |

### Held 2026/27 rate table

Announced in Budget Review 2026 Table 4.4 and billed in B34-2026 clause 1 and Schedule I para 1, for years commencing on or after 1 March 2026. SARS's 'Rates of tax for individuals' page, updated 28 October 2026, prints the same table for the 2027 tax year. The bands here use each top limit; the Bill prints each lower limit as the next rand.

| Taxable income | Tax | Source | URL |
| --- | --- | --- | --- |
| Up to R245,100 | 18% | B34-2026, Schedule I para 1; Budget Review 2026 Table 4.4. Announced and billed, held | https://www.sars.gov.za/legal-lprep-bills-2026-03-rates-and-monetary-amounts-and-amendment-of-revenue-laws-bill-b34-2026-21-october-2026/ |
| R245,100 to R383,100 | R44,118 + 26% above R245,100 | same | same |
| R383,100 to R530,200 | R79,998 + 31% above R383,100 | same | same |
| R530,200 to R695,800 | R125,599 + 36% above R530,200 | same | same |
| R695,800 to R887,000 | R185,215 + 39% above R695,800 | same | same |
| R887,000 to R1,878,600 | R259,783 + 41% above R887,000 | same | same |
| Above R1,878,600 | R666,339 + 45% above R1,878,600 | same | same |

### Rebates, credits and tax thresholds

| Item | Enacted | Held 2026/27 | Source | URL |
| --- | --- | --- | --- | --- |
| Primary rebate | R17,235 | R17,820 | B34-2026 clause 3 prints the enacted section 6(2) amount and the billed amount, deemed from 1 March 2026; Budget Review 2026 Table 4.4 | https://www.sars.gov.za/legal-lprep-bills-2026-03-rates-and-monetary-amounts-and-amendment-of-revenue-laws-bill-b34-2026-21-october-2026/ |
| Secondary rebate, age 65 and over | R9,444 | R9,765 | same | same |
| Tertiary rebate, age 75 and over | R3,145 | R3,249 | same | same |
| Medical scheme fees credit, person | R364 a month | R376 a month | B34-2026 clause 4 prints the enacted section 6A amounts and the billed amounts; Budget Review 2026 chapter 4 | same |
| Medical scheme fees credit, person and one dependant, or two dependants | R728 a month | R752 a month | same | same |
| Medical scheme fees credit, each further dependant | R246 a month | R254 a month | same | same |
| Tax threshold, under 65 | R95,750 | R99,000 | Budget Review 2026 Table 4.4, 2025/26 and 2026/27 columns. Held column announced; SARS prints it for 2027 | https://www.treasury.gov.za/documents/National%20Budget/2026/review/Chapter%204.pdf |
| Tax threshold, 65 and over | R148,217 | R153,250 | same | same |
| Tax threshold, 75 and over | R165,689 | R171,300 | same | same |

The para 1 'tax threshold' is the maximum taxable income on which no tax is payable when the section 5 rates and section 6 rebates for that year are applied, so it moves with whichever rebates apply. The enacted column is the 2025/26 column of Table 4.4; it matches the enacted rebates divided by 18%, rounded.

### Paragraph 20 thresholds and percentages

| Item | Amount | Status and source | URL |
| --- | --- | --- | --- |
| Para 20(1) taxable income threshold | R1,000,000 | Enacted. SARS Guide G01 rev 28, effective 16 October 2026, section 14, and B33-2026 clause 3, which prints the current R1 million. Interpretation Note 1 part 4.4.2 agrees | https://www.sars.gov.za/wp-content/uploads/Ops/Guides/GEN-PT-01-G01-Guide-for-Provisional-Tax-External-Guide.pdf |
| Para 20(1) taxable income threshold, held | R1,800,000 | Announced in Budget Review 2026 Annexure C; billed in B33-2026 clause 3(1)(a), (b) and 3(2), for years commencing on or after 1 March 2026. Held | https://www.sars.gov.za/legal-lprep-bills-2026-02-tax-administration-laws-amendment-bill-b33-2026-21-october-2026/ |
| Above the threshold: final estimate must reach | 80% of taxable income | Para 20(1)(a), read in the unofficial consolidation; Interpretation Note 1 part 4.4.2 restates it | https://www.sars.gov.za/wp-content/uploads/Legal/Notes/LAPD-IntR-IN-2012-01-Provisional-Tax-Estimates.pdf |
| At or below the threshold: final estimate must reach | 90% of taxable income or the basic amount | Para 20(1)(b), as above | same |
| Underestimation penalty | 20% | Para 20(1), as above | same |
| Late payment penalty | 10% of the amount unpaid | Para 27(1), read in the unofficial consolidation; Interpretation Note 1 part 4.3.2(a) restates it | same |
| Basic amount escalation | 8% a year, simple | Para 19(1)(d) proviso, read in the unofficial consolidation; Interpretation Note 1 part 4.3.1 restates it | same |
| Exclusion limb (BB) | R30,000 | Para 1, read in the unofficial consolidation; Interpretation Note 1 part 4.1 restates it | same |

### Prescribed interest rates

| Period | Late and underpaid tax | Credit amounts, section 89quat(4) | Source | URL |
| --- | --- | --- | --- | --- |
| 1 November 2025 to 28 February 2026 | 10.50% | 6.50% | SARS Interest Rates Tables 1 and 2, September 2026. Table 1 URL here; Table 2: https://www.sars.gov.za/wp-content/uploads/Legal/Rates/Legal-Pub-IRT-02-Interest-Rates-Table-2.pdf | https://www.sars.gov.za/wp-content/uploads/Legal/Rates/Legal-Pub-IRT-01-Interest-Rates-Table-1.pdf |
| 1 March to 31 August 2026 | 10.25% | 6.25% | same | same |
| 1 September 2026 until the PFMA rate changes | 10.50% | 6.50% | same | same |

There is no fixed quarterly cycle. The rate follows section 80(1)(b) of the Public Finance Management Act and for these taxes takes effect on the first day of the second month after the PFMA rate comes into operation (table notes; TA Act section 189(4)). Read the current tables.

## The base

### How much to pay

Each payment starts from the estimated liability: normal tax on estimated taxable income, less section 6 rebates, the section 6A medical scheme fees credit and the section 6B additional medical expenses credit (para 21; Interpretation Note 1 part 4.2.1). Employees' tax and foreign tax come off after that.

- **First period (para 21(1)(a)):** one half of the estimated liability, less employees' tax deducted during that period, less tax proved payable to a foreign government that qualifies under section 6quat by the end of the period. Halve the liability only. Employees' tax comes off in full, so `first_period = (annual_tax - rebates - medical_credits) / 2 - PAYE_first_6_months - foreign_credit`.
- **Second period (para 21(1)(b)):** `second_period = annual_tax - rebates - medical_credits - PAYE_full_year - first_period_paid - foreign_credit`.
- **Third payment (para 23A):** `third_payment = actual_tax - rebates - medical_credits - PAYE_full_year - first_period_paid - second_period_paid - earlier_top_ups_paid - foreign_credit`, deducting earlier top-ups actually paid (SARS Guide G01 section 9.1(c)).

SARS's provisional tax page lists the deductions in a looser order. Para 21 and Interpretation Note 1 part 4.2.1 control. A result below zero means a nil payment, as the worked examples show, and any excess is dealt with on assessment (SARS Guide G01). The IRP6 is still due if the payment is nil (Interpretation Note 1 part 4.3.1).

### What the estimate covers

The estimate is of total taxable income for the whole year (para 19(1)(a)). It excludes retirement fund lump sums, withdrawal benefits and severance benefits. It includes taxable capital gains made or reasonably expected in the year, in both the first and second periods (Interpretation Note 1 part 4.3.1; SARS Guide G01 section 5). See [za-capital-gains](za-capital-gains.md) for the gain and [za-income-tax](za-income-tax.md) for taxable income.

A property sale with a R500,000 capital gain, before the annual exclusion and with no other disposals, gives a taxable capital gain of (R500,000 - R40,000) × 40% = R184,000 on the enacted exclusion, which B34-2026 clause 16 prints as the current para 5(1) amount, or R180,000 on the R50,000 exclusion billed in that clause, which is held. [za-capital-gains](za-capital-gains.md) has the inclusion rate. Include that amount in the estimate. It stays out of the basic amount.

### The basic amount

- **First period floor:** para 19(1)(c) says the first period estimate must not be less than the basic amount unless the circumstances justify a lower estimate. No such floor applies to the second estimate, where the basic amount still matters for para 20 (Interpretation Note 1 part 4.4.1).
- **Definition:** para 19(1)(d)(i): taxable income as assessed for the latest preceding year, less (aa) taxable capital gain, (bb) the taxable portion of lump sums and severance benefits, other than amounts within para (eA) of 'gross income', and (bbA) para (d) gross income amounts other than severance benefits.
- **Latest preceding year:** para 19(1)(e): the latest earlier year with a notice of assessment issued not less than 14 days before the date the estimate is submitted. SARS Guide G01 section 5(e) words this by the due date, whilst section 5(a)(v) uses the submission date. Para 19(1)(e) and Interpretation Note 1 part 4.3.1 use the submission date, and the statute controls.
- **18-month escalation:** if the estimate must be made more than 18 months after the end of the latest preceding year, the basic amount rises by 8% a year of that amount, from the end of that year to the end of the year being estimated (para 19(1)(d) proviso). It is simple, not compound (Interpretation Note 1 part 4.3.1).

| Situation | Basic amount |
| --- | --- |
| Prior year assessed, notice at least 14 days old, estimate within 18 months of that year end | Assessed taxable income less the para 19(1)(d)(i) exclusions |
| Estimate more than 18 months after that year end | As above, plus 8% a year, simple |
| First year, no assessment | No basic amount as defined. A nil estimate on that premise is not accepted; estimate total taxable income (Interpretation Note 1 part 4.3.1). How para 20(1)(b) then applies is held |
| Prior year assessed loss | The text read does not say the basic amount is zero. Held for a reviewer. The client gets no comfort from a nil figure: para 19(3) lets the Commissioner increase any estimate |

Using the basic amount can fail para 19(1)(a), which requires an estimate of total taxable income. Interpretation Note 1 part 4.3.1 gives a significant capital gain and a new line of business as examples.

### SARS's powers over an estimate

- Para 19(2): the Commissioner may estimate if the taxpayer fails to submit.
- Para 19(3): the Commissioner may call for justification at any time and, if not satisfied, increase the estimate. The increase is not subject to objection and appeal (para 19(3); SARS Guide G01 section 6). Interpretation Note 1 part 4.3.1 says an internal review under TA Act section 9 may be requested and does not suspend payment.
- SARS Guide G01 section 6 says the para 19(3) letter goes by eFiling and email, and the documents are due within 10 business days.
- Para 25(1): extra tax after an increase is payable within the period the Commissioner sets.
- Para 24: the Commissioner may absolve the first payment if taxable income cannot be estimated on the available facts.

### Refunds and credits

Provisional tax cannot be refunded before assessment, or reallocated between periods or taxpayers (paras 28 and 29; Interpretation Note 1 part 4.6). Excess is refunded after assessment.

## Deadlines and filing

SARS names each period by year and number. TA Act section 244(1) moves a deadline falling on a Saturday, Sunday or public holiday to the last business day before it.

| Period | IRP6 label | Statutory period ends | 2026/27 last day | Requirement |
| --- | --- | --- | --- | --- |
| First | 2027/01 | Six months from the start of the year (para 21(1)(a)) | Monday 31 August 2026 | Estimate the full year; pay half the estimated liability less credits |
| Second | 2027/02 | Last day of the year (para 21(1)(b)) | Friday 26 February 2027 | Estimate the full year; pay the balance |
| Third, voluntary | 2027/03 | Effective date, seven months after the year end (para 23A; section 89quat(1)) | Thursday 30 September 2027 | Pay to avoid or reduce section 89quat interest |

28 February 2027 is a Sunday. SARS's ITR12 guide G05 section 13.1 prints 27 February 2027 for 2027/02, which is a Saturday. SARS's provisional tax page says the last business day of February, and section 244(1) gives Friday 26 February 2027. SARS Guide G01 part 2(f) also prints the year as ending 29 February 2027, a date that does not exist. Work to 26 February. A para 19(6) deemed nil estimate arises if the final estimate is not submitted by the last day of the fourth month after the year end, 30 June 2027.

### Year-ends other than February

A natural person's year ends on the last day of February (section 5(1)(c)). Under section 66(13A), SARS may accept accounts drawn to a date falling after the end of the year, for income that cannot conveniently be returned to the February year end. Para 21(2) then reckons the first period from the date the Commissioner approves on the taxpayer's application. All other income stays in the February year (SARS Guide G01 section 10(c)). The third payment moves to six months after the year end (section 89quat(1); Interpretation Note 1 part 4.2.1). SARS Guide G01 section 10 shows a 31 May 2026 year end with payments due 30 November 2025 and 31 May 2026 and a third on 30 November 2026. Get the SARS approval letter before using any non-February date. Without approval, hold the case.

### Short years and part-year cases

- **No first payment:** para 21(1A) and SARS Guide G01 section 10(b): where the year does not exceed six months, for example through death or ceasing to be resident.
- **Business starts mid-year:** the year does not shorten, so a person who starts a business in October files the second period by the last business day of February. The first period position is flagged for a reviewer. No text read says how para 19 or para 27 treats a first period that passed before the person met para 1. Para 24 and section 89quat(3A) are the relief routes to raise.
- **Business stops mid-year:** closing a business does not end the year of assessment. The person has still derived limb (a)(ii) income in that year and (dd)(B) needs no business income, so the second period IRP6 is still due by the last business day of February.
- **Ceasing to be resident:** section 9H(2)(b) deems the year to end on the date immediately before the day the person ceases to be resident, and section 9H(2)(c) starts the next year on that day. Section 66(13)(a)(iii) frames the return the same way. SARS Guide G01 Note 5 says the year ends on the date of ceasing and that two assessments arise; the statute controls the date. G01 part 2(h) says the IRP6 needs the cessation date.
- **Death:** section 66(13)(a)(i) ends the return period on the date of death, and SARS Guide G01 section 10(b) treats death as a case that can shorten the year. A deceased estate is excluded by para 1 exclusion (ff).

### Filing

Every provisional taxpayer files an IRP6 for the first and second periods, even if the payment is nil (Interpretation Note 1 parts 4.3.1 and 4.4.1; SARS Guide G01 section 7). The form is requested through SARS eFiling at www.sarsefiling.co.za, the SARS contact centre on 0800 00 7277 or a SARS branch. A person already on eFiling adds provisional tax to the profile.

SARS Guide G02 rev 5, effective 27 June 2025, gives the eFiling path: Returns, Returns Issued, Provisional Tax (IRP6), select the period, Request Return, then the Provisional Tax Work Page and IRP6. The first period fields are Gross Income, Estimated taxable income, the two medical credits, Employees' tax for the period (enter 0.00 if none), Foreign tax credits, and penalty and interest on late payment. eFiling calculates the tax and the rebates by age at the year end. Save and File Return, then keep the confirmation.

### Payment

Pay through eFiling, EFT or a bank using the 19-digit payment reference and the beneficiary ID on the IRP6 payment advice, and allow for bank clearance and cut-off times. SARS does not accept a payment without both (SARS Guide G01 section 10). On eFiling: Payments, Pay Now, Create Additional Payment, Provisional Tax (PROV), Provisional Tax Period Payment, then the tax reference, period and amount.

SARS Guide G01 section 11 says the section 167 instalment deferral covers debts arising from an issued assessment and does not apply to provisional tax. Interpretation Note 1 part 4.3.1 says taxpayers with liquidity concerns may apply for an instalment agreement on an increased estimate. The two conflict, so treat instalments as unavailable until a reviewer resolves it. Interest runs either way.

## Penalties and interest

### Underestimation penalty, para 20

The test uses the taxpayer's own final estimate, not one the Commissioner increased (Interpretation Note 1 part 4.4.2). The first period attracts no underestimation penalty (Interpretation Note 1 part 4.3.2). Taxable income means taxable income as finally determined, excluding retirement lump sums and severance benefits. Para (d) 'gross income' amounts are in conflict: the para 20(1) proviso read names only lump sums and severance benefits, SARS Guide G01 section 14 says these amounts are included, and Interpretation Note 1 part 4.4.2 says they are excluded. Hold the point where it changes the result.

| Final taxable income | Penalty arises if | Penalty |
| --- | --- | --- |
| Above the threshold (para 20(1)(a)) | Final estimate is less than 80% of taxable income | 20% × max(normal tax after rebates on 80% of taxable income - employees' tax and provisional tax paid by the end of the year, 0) |
| At or below the threshold (para 20(1)(b)) | Final estimate is less than 90% of taxable income and less than the basic amount | 20% × max(the lesser of normal tax after rebates on 90% of taxable income and on the basic amount - employees' tax and provisional tax paid by the end of the year, 0) |

Enacted, the threshold is R1,000,000. Held, it is R1,800,000. An estimate of at least the basic amount avoids para 20(1)(b) even if taxable income turns out higher, but only if final taxable income is at or below the threshold. Above it, the basic amount gives no protection.

Para 20 says 'the difference between' the 2 amounts and no text read addresses payments above the tax on the floor. This guide shows nil in that case and holds the point for a reviewer. The estimate does not feature in the amount. The comparison is with what was actually paid by the end of the year, so a payment made after the year end does not count (para 20(1); Interpretation Note 1 part 4.4.2). SARS Guide G01 section 14(c)(i)(A) still says 'The amount of normal tax as determined in respect of such estimate' and its examples do not reconcile; the statute and Interpretation Note 1 control.

- **Reduction:** para 20(2B) reduces the penalty by any para 27 penalty on the second payment.
- **Remission:** para 20(2) lets the Commissioner remit if the estimate was seriously calculated with due regard to the relevant factors and was not deliberately or negligently understated. Interpretation Note 1 part 4.4.2 says merely relying on the basic amount is unlikely to meet this. Para 20(2C) allows remission of the deemed nil consequence if the lateness was not meant to postpone or evade.
- **Late estimate:** a deemed nil estimate under para 19(6) feeds para 20. Interpretation Note 1 Example 6, a company example, says that for a deemed nil second estimate no para 27 penalty arises on that payment, because no liability was estimated. Applying that to a natural person is an inference. Para 20A was repealed for years commencing on or after 1 March 2015.
- **Procedure:** the penalty is a percentage based penalty under chapter 15 of the TA Act (Interpretation Note 1 part 4.4.2). A refusal to remit is subject to objection and appeal (TA Act section 220). See R-ZA-PROV-1.

### Late payment penalty, para 27

Para 27(1) charges 10% of any amount not paid in the para 21, 23 or 25(1) period. It does not cover a para 23A third payment. Under TA Act section 217(3), SARS may remit if the penalty concerns a first incidence or an amount under R2,000, reasonable grounds exist and the non-compliance is remedied. Section 218 requires remission in listed exceptional circumstances, including disaster, serious illness and specified SARS errors. Section 215 sets the request procedure.

### The late-payment rule in B33-2026

Budget Review 2026 Annexure C proposed that timely payment be required before an estimate may be relied on, with effect from 25 February 2026. No Act read enacts this.

B33-2026 clause 3(1)(c) proposes a further proviso to para 20(1). If the para 21(1)(b) payment 'is not made in full within one month from the date such payment was due', the taxpayer is deemed to have submitted a final estimate equal to the aggregate of the payments, employees' tax and foreign tax proved payable on or before the end of that month. Clause 3(1)(d) limits remission in that case. Clause 3(2) dates only the threshold change; clause 19(2) brings the rest into operation on promulgation. So even as billed, it has a one-month allowance, applies no earlier than promulgation, and does not make a day-late payment a para 20 case. The clause equates an estimate of taxable income with an aggregate of tax amounts, and how that compares is held.

### Interest

| Charge | When | Period | Rate |
| --- | --- | --- | --- |
| Section 89bis(2), overdue payment | Provisional tax not paid in full in the para 21, 23, 23A or 25(1) period | From the end of the period until paid. Interpretation Note 1 part 4.3.3 counts 1 September to the payment date inclusive for a 31 August payment. Unless the Commissioner directs otherwise | Prescribed rate, Table 1 |
| Section 89quat(2), underpayment | Taxable income above R50,000 and normal tax exceeds the credit amount | From the effective date until the date of assessment | Prescribed rate, Table 1 |
| Section 89quat(4), overpayment | Credit amount exceeds normal tax, and the excess is above R10,000 or taxable income is above R50,000 | From the effective date until refunded | Table 2 |

- **Effective date:** section 89quat(1): seven months after the year end for a natural person without section 66(13A) permission, otherwise six months. For 2026/27 that is 30 September 2027.
- **Credit amount:** para 21 and para 23A payments, employees' tax and section 6quat foreign taxes.
- **Normal tax here:** Interpretation Note 1 part 4.4.3(b) includes the para 20 penalty and any understatement penalty.
- **SARS's date:** SARS Guide G01 section 13 stops the count on the day before the first due date on assessment. The statute says until the date of assessment.
- **Relief:** section 89quat(3) for circumstances beyond the taxpayer's control and section 89quat(3A) for a natural person's first year as a provisional taxpayer; both are subject to objection and appeal under section 89quat(5).
- **Deductibility:** SARS Guide G01 section 13 says this interest is not deductible.

The third payment reduces section 89quat interest only. It comes after the year end, so para 20 ignores it. A taxpayer who sees in August that the second estimate was too low can pay by 30 September 2027 to cut interest, but not the penalty. Paid after the effective date, para 23A(2) treats it as overdue under section 89bis(2) (Interpretation Note 1 part 4.5.3).

## Cross-border points

- **Foreign employer not registered under para 15:** the employee is a provisional taxpayer under limb (a)(i), unless para 1 (dd)(B) applies, including an expatriate seconded here (Interpretation Note 1 Example 1). The note also covers embassy and diplomatic mission staff, with an exclusion for certain non-resident staff not liable to tax.
- **Shadow payroll:** a foreign employer's shadow payroll does not register the employer. SARS may direct under para 19(1)(a) that returns are not required, on written application, if employees' tax is correctly withheld on all South African remuneration, there is no risk of loss to the fiscus and the person has no other taxable income (Interpretation Note 1 part 4.1 Example 1).
- **Foreign tax credit:** section 6quat tax proved payable reduces each payment; the second period takes the credit for the full year.
- **Ceasing to be resident:** see Short years and part-year cases. For residence, see [za-tax-residency](za-tax-residency.md) and [leaving-south-africa-tax-emigration](leaving-south-africa-tax-emigration.md).
- **Non-resident non-executive director:** outside BGR 40; see the table above.
- **Non-resident ship or aircraft owner:** excluded by para 1 exclusion (dd)(A) where section 33 applies.
- **Currency:** IRP6 amounts are in rand only.

## Two worked examples that recompute

All examples assume a natural person under 65 with a February year end and no medical or foreign credits. Each shows the enacted and held figures side by side.

### Example 1: first period on R600,000

R600,000 falls in the 36% band on both tables.

```oa-check
name: ZA 2026/27 first period, Act 3 table and enacted primary rebate
inputs:
  estimate: 600000
  band_floor: 512800
  band_base: 121475
  band_percent: 36
  primary_rebate: 17235
  paye_first_period: 30000
steps:
  - gross_tax: band_base + pct(estimate - band_floor, band_percent)
  - liability: gross_tax - primary_rebate
  - half: liability / 2
  - payment: max(half - paye_first_period, 0)
expected:
  gross_tax: 152867
  liability: 135632
  half: 67816
  payment: 37816
```

```oa-check
name: ZA 2026/27 first period, held B34-2026 table and rebate
inputs:
  estimate: 600000
  band_floor: 530200
  band_base: 125599
  band_percent: 36
  primary_rebate: 17820
  paye_first_period: 30000
steps:
  - gross_tax: band_base + pct(estimate - band_floor, band_percent)
  - liability: gross_tax - primary_rebate
  - half: liability / 2
  - payment: max(half - paye_first_period, 0)
expected:
  gross_tax: 150727
  liability: 132907
  half: 66453.5
  payment: 36453.5
```

Decision point: the two answers differ by R1,362.50 before employees' tax. With no employees' tax the first payment is R67,816 or R66,453.50. A taxpayer paying on the held table should know eFiling's result first and record which table it used. Halving after deducting employees' tax would understate the credit: the payment would be wrongly shown as R52,816 instead of R37,816 on the enacted table.

### Example 2: basic amount R900,000, final taxable income R1,200,000

Final estimate R900,000, equal to the basic amount. Payments by the end of the year equal the tax on that estimate. On the enacted threshold, R1,200,000 exceeds R1,000,000, so para 20(1)(a) applies and the basic amount gives no protection. 80% of taxable income is R960,000, above the estimate, so a penalty arises.

```oa-check
name: ZA para 20(1)(a) on the enacted R1 million threshold, Act 3 table
inputs:
  taxable_income: 1200000
  estimate: 900000
  band_floor: 857900
  band_base: 251258
  band_percent: 41
  primary_rebate: 17235
steps:
  - floor_income: pct(taxable_income, 80)
  - tax_on_floor: band_base + pct(floor_income - band_floor, band_percent) - primary_rebate
  - paid: band_base + pct(estimate - band_floor, band_percent) - primary_rebate
  - penalty: pct(max(tax_on_floor - paid, 0), 20)
expected:
  floor_income: 960000
  tax_on_floor: 275884
  paid: 251284
  penalty: 4920
```

Decision point: on the held R1,800,000 threshold, R1,200,000 is at or below it, so para 20(1)(b) applies. The estimate of R900,000 is below 90% of taxable income (R1,080,000) but not below the basic amount, so no penalty arises. If the R1 million threshold stands but the held rate table applies, the two taxes are R271,893 and R247,293 and the penalty is still R4,920. To stay clear on enacted law, this client's final estimate needed to reach R960,000. An employee with R800,000 salary and R400,000 freelance income, R1,200,000 in all, falls under the same tests, with employees' tax counted in the amount paid.

### Example 3: stale assessment and both para 20(1)(b) limbs

The latest assessment is for the year ended 29 February 2024, assessed taxable income R400,000 with no exclusions. The final estimate is made in February 2027, more than 18 months after that year end, so the basic amount gains 3 years at 8%. Final estimate R480,000, final taxable income R700,000, payments by the end of the year equal the tax on the estimate.

```oa-check
name: ZA basic amount escalation and para 20(1)(b), Act 3 table
inputs:
  assessed: 400000
  years: 3
  estimate: 480000
  taxable_income: 700000
  band_floor: 370500
  band_base: 77362
  band_percent: 31
  primary_rebate: 17235
steps:
  - basic_amount: assessed + pct(assessed, 8) * years
  - ninety: pct(taxable_income, 90)
  - tax_on_basic: band_base + pct(basic_amount - band_floor, band_percent) - primary_rebate
  - paid: band_base + pct(estimate - band_floor, band_percent) - primary_rebate
  - penalty: pct(max(tax_on_basic - paid, 0), 20)
expected:
  basic_amount: 496000
  ninety: 630000
  tax_on_basic: 99032
  paid: 94072
  penalty: 992
```

Decision point: R480,000 is below both R630,000 and R496,000, and the lesser tax is on the basic amount because R496,000 is less than R630,000. The held table gives taxes of R97,177 and R92,217 and the same R992. Raising the final estimate to R496,000 and paying the matching tax by 26 February 2027 removes the penalty on either threshold, because R700,000 is below both. Section 89quat interest can still arise on the shortfall.

### Example 4: payment late, estimate within tolerance

Final estimate R700,000, final taxable income R750,000, second payment R80,000 paid on 14 March 2027, with the rate at 10.50% and unchanged. The estimate is above 90% of taxable income (R675,000), so para 20 does not apply on either threshold. Enacted law charges para 27 and section 89bis interest. Section 89bis(2) reckons from the end of the period, para 21(1)(b) ends that period on the last day of the year, and Interpretation Note 1 part 4.3.3 counts from the next day, so this example assumes the period ended on 28 February 2027 and counts 1 to 14 March 2027. Section 244(1) moves the last day for payment to 26 February. If it also moves the end of the period, the count is 16 days and the interest is R368.22. No text read settles this, so the count is held.

```oa-check
name: ZA late second payment, para 27 and section 89bis
inputs:
  unpaid: 80000
  penalty_percent: 10
  rate_percent: 10.5
  days: 14
steps:
  - para_27: pct(unpaid, penalty_percent)
  - interest: round(pct(unpaid, rate_percent) * days / 365, 2)
expected:
  para_27: 8000
  interest: 322.19
```

Decision point: the legacy 20% result is wrong. The cost is R8,000 plus R322.19 on the stated count. As billed, B33-2026 would not change this payment, because it was made within one month of the due date. Simple interest is safe here because the period is under a month; section 187(2) compounding is held.

### Other results checked

| Case | Result |
| --- | --- |
| Actual R1,900,000 | Above both thresholds. The final estimate must reach R1,520,000 (80%); the basic amount gives no protection |
| Basic R400,000, estimate R350,000, actual R700,000 | At or below both thresholds. Estimate is below R630,000 and below the basic amount, so a penalty arises. An estimate of R400,000 avoids it |
| Basic R400,000, estimate R350,000, actual R800,000 | Penalty on the lesser of tax on R400,000 and on R720,000, less payments. If payments equal tax on R350,000: 20% × (R69,272 - R54,797) = R2,895 on the enacted table, or 20% × (R67,417 - R53,572) = R2,769 on the held table |
| Basic R500,000, estimate R500,000, actual R700,000 | No para 20 penalty on either threshold. Interest can still arise, and SARS can test the estimate under para 19(3) |
| Basic R1,200,000, estimate R1,500,000, actual R2,000,000 | Above both thresholds. R1,500,000 is below R1,600,000. If payments equal tax on R1,500,000: 20% × (R538,284 - R497,284) = R8,200 on the enacted table; on the held table R534,293 - R493,293 gives the same R8,200 |
| Salary R900,000 plus freelance R300,000 | Provisional taxpayer. Taxable income of R1,200,000 is above the enacted threshold, so the 80% test applies. On the held threshold, the 90% and basic amount test applies. Employees' tax counts |
| Second estimate R500,000, actual R800,000, R100,000 third payment by 30 September 2027 | Reduces section 89quat interest, not any para 20 penalty |
| First year, estimate R400,000 | No basic amount. Estimate total taxable income; a nil estimate on the premise of no basic amount is not accepted |

## Ask the client first

1. **Person and year:** age on the last day of the year, residence status, the year of assessment, and any SARS-approved section 66(13A) date.
2. **All income sources:** business, freelance, rent, interest, dividends, foreign income, non-executive fees, payroll and any unregistered employer. Is any income from carrying on a business?
3. **Latest assessment:** notice date, year, taxable income, and any taxable capital gain, lump sum or severance benefit in it.
4. **Current estimate:** estimated taxable income, expected capital gains, and whether final taxable income may exceed R1,000,000 or R1,800,000.
5. **Credits:** employees' tax for the first six months and the full year, medical scheme fees and additional medical credits, and foreign tax proved payable.
6. **Compliance so far:** IRP6s filed and dates, payments made and dates, any para 19(3) letter, penalty or SARS notice.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Act 3 of 2026, Gazette 54446, read in part: section 2 and Schedule I para 1; searched for Fourth Schedule references, none found | https://www.sars.gov.za/legal-lprim-aa-2026-01-rates-and-monetary-amounts-and-amendment-of-revenue-laws-act-3-of-2026-gg-54446-1-april-2026/ | 2026-11-05 |
| Act 4 of 2026, Gazette 54447, searched for Fourth Schedule and section 89 references: none found | https://www.sars.gov.za/wp-content/uploads/Legal/AmendActs/Legal-LPrim-AA-2026-02-Tax-Administration-Laws-Amendment-Act-4-of-2026-GG-54447-1-April-2026.pdf | 2026-11-05 |
| Act 5 of 2026, Gazette 54448, searched for Fourth Schedule and section 89 references: none found | https://www.sars.gov.za/legal-lprim-aa-2026-03-taxation-laws-amendment-act-5-of-2026-gg-54448-1-april-2026/ | 2026-11-05 |
| B34-2026 rates bill, read in part: clauses 1, 3, 4 and 16 and Schedule I para 1 | https://www.sars.gov.za/legal-lprep-bills-2026-03-rates-and-monetary-amounts-and-amendment-of-revenue-laws-bill-b34-2026-21-october-2026/ | 2026-11-05 |
| B33-2026 Tax Administration Laws Amendment Bill, read in part: clauses 1 to 3 and 19 and the memorandum on clause 3 | https://www.sars.gov.za/legal-lprep-bills-2026-02-tax-administration-laws-amendment-bill-b33-2026-21-october-2026/ | 2026-11-05 |
| B32-2026 Taxation Laws Amendment Bill, searched for Fourth Schedule and section 89 references: no provisional tax change found | https://www.sars.gov.za/legal-lprep-bills-2026-01-taxation-laws-amendment-bill-b32-2026-21-october-2026/ | 2026-11-05 |
| SARS Amendment Acts page, read for its list of Acts | https://www.sars.gov.za/legal-counsel/primary-legislation/amendment-acts/ | 2026-11-05 |
| SARS Bills page, read for its list of current bills | https://www.sars.gov.za/legal-counsel/preparation-of-legislation/bills/ | 2026-11-05 |
| Budget Review 2026, Chapter 4, read in part: personal income tax text and Table 4.4 | https://www.treasury.gov.za/documents/National%20Budget/2026/review/Chapter%204.pdf | 2026-11-05 |
| Budget Review 2026, Annexure C, read in part: provisional tax items | https://www.treasury.gov.za/documents/National%20Budget/2026/review/Annexure%20C.pdf | 2026-11-05 |
| Budget Speech 2026, read in part: personal income tax passage | https://www.treasury.gov.za/documents/national%20budget/2026/speech/speech.pdf | 2026-11-05 |
| SARS Budget tax guide 2026, read in part: individual tables and the provisional tax box | https://www.sars.gov.za/wp-content/uploads/Docs/Budget/Budget2026/Budget-tax-guide-2026-online-version-for-printing.pdf | 2026-11-05 |
| SARS Budget 2026 frequently asked questions, read in part: provisional tax items | https://www.sars.gov.za/about/sars-tax-and-customs-system/budget/budget-2026-frequently-asked-questions/ | 2026-11-05 |
| SARS Rates of tax for individuals, updated 28 October 2026, read in part: 2027 table, rebates and thresholds | https://www.sars.gov.za/tax-rates/income-tax/rates-of-tax-for-individuals/ | 2026-11-05 |
| SARS provisional tax page, updated 21 August 2026, read in full | https://www.sars.gov.za/types-of-tax/provisional-tax/ | 2026-11-05 |
| SARS Interpretation Note 1 (Issue 3), 20 February 2019, read in part: parts 1 to 5 apart from the company passages other than Example 6, and not Example 5 or the annexure | https://www.sars.gov.za/wp-content/uploads/Legal/Notes/LAPD-IntR-IN-2012-01-Provisional-Tax-Estimates.pdf | 2026-11-05 |
| SARS Guide for Provisional Tax GEN-PT-01-G01 rev 28, effective 16 October 2026, read in part: sections 1 to 10, 11, 13 and 14 | https://www.sars.gov.za/wp-content/uploads/Ops/Guides/GEN-PT-01-G01-Guide-for-Provisional-Tax-External-Guide.pdf | 2026-11-05 |
| SARS How to eFile your Provisional Tax Return GEN-PT-01-G02 rev 5, effective 27 June 2025, read in full | https://www.sars.gov.za/wp-content/uploads/Ops/Guides/GEN-PT-01-G02-How-to-eFile-your-Provisional-Tax-Return-External-Guide.pdf | 2026-11-05 |
| SARS ITR12 guide IT-AE-36-G05, read in part: section 13 on provisional taxpayers | https://www.sars.gov.za/wp-content/uploads/Ops/Guides/IT-AE-36-G05-Comprehensive-Guide-to-the-ITR12-Income-Tax-Return-for-Individuals-External-Guide.pdf | 2026-11-05 |
| SARS Interest Rates Table 1, September 2026, read in full | https://www.sars.gov.za/wp-content/uploads/Legal/Rates/Legal-Pub-IRT-01-Interest-Rates-Table-1.pdf | 2026-11-05 |
| SARS Interest Rates Table 2, September 2026, read in full | https://www.sars.gov.za/wp-content/uploads/Legal/Rates/Legal-Pub-IRT-02-Interest-Rates-Table-2.pdf | 2026-11-05 |
| SARS Binding General Ruling (Income Tax) 40, read in full | https://www.sars.gov.za/wp-content/uploads/Legal/Rulings/BGR/LAPD-IntR-R-BGR-2017-03-BGR40-Remuneration-paid-to-non-executive-directors.pdf | 2026-11-05 |
| SARS FAQs on BGRs 40 and 41, read in part: provisional tax answer | https://www.sars.gov.za/wp-content/uploads/Ops/Guides/Legal-Pub-FAQs-VAT12-FAQs-on-BGRs-40-and-41-Non-executive-Directors-VAT-and-PAYE.pdf | 2026-11-05 |
| Income Tax Act section 5(1)(c) and (2), unofficial consolidation, read in part | https://source.acts.co.za/income-tax-act-1962/5__levy_of_normal_tax_and_rates_thereof.php | 2026-11-05 |
| Income Tax Act section 6(2), (4) and (6), unofficial consolidation, read in part | https://source.acts.co.za/income-tax-act-1962/6__normal_tax_rebates.php | 2026-11-05 |
| Income Tax Act section 9H(1) and (2), unofficial consolidation, read in part | https://source.acts.co.za/income-tax-act-1962/9h__change_of_residence_or_b_ecoming_headquarter_company.php | 2026-11-05 |
| Income Tax Act section 66(13), (13A) and (13B), unofficial consolidation, read in part | https://source.acts.co.za/income-tax-act-1962/66__notice_by_commissioner_requiring_returns_for_assessment_of_taxes_under_this_act_and_manner_of_furnishing_returns_and.php | 2026-11-05 |
| Income Tax Act section 89 repeal note, unofficial consolidation, digest only | https://source.acts.co.za/income-tax-act-1962/89__appointment_of_day_for_payment_of_tax_and_interest_on_overdue_payments_.php | 2026-11-05 |
| Income Tax Act section 89bis, unofficial consolidation, read in part | https://source.acts.co.za/income-tax-act-1962/89bis__payments_of_employees_tax_and_provisional_tax_and_interest_on_overdue_payments_of_such_taxes.php | 2026-11-05 |
| Income Tax Act section 89quat(1) to (5), unofficial consolidation, read in part | https://source.acts.co.za/income-tax-act-1962/89quat__interest_on_underpayments_.php | 2026-11-05 |
| Income Tax Act section 89quin, unofficial consolidation, read in part | https://source.acts.co.za/income-tax-act-1962/89quin__calculation_of_interest_payable_under_this_act_.php | 2026-11-05 |
| Income Tax Act section 89sex, unofficial consolidation, digest only | https://source.acts.co.za/income-tax-act-1962/89sex__determination_of_day_for_payment_of_tax_interest_or_penalties_.php | 2026-11-05 |
| Fourth Schedule para 1, unofficial consolidation, read in part: 'employee', 'provisional taxpayer', 'remuneration' and 'tax threshold' | https://source.acts.co.za/income-tax-act-1962/sch4_1__sch4_part_i_1__definitions.php | 2026-11-05 |
| Fourth Schedule para 17, unofficial consolidation, read in part | https://source.acts.co.za/income-tax-act-1962/sch4_17__payment_of_provisional_tax.php | 2026-11-05 |
| Fourth Schedule para 18 repeal note, unofficial consolidation, read in part | https://source.acts.co.za/income-tax-act-1962/sch4_18__exemptions.php | 2026-11-05 |
| Fourth Schedule para 19, unofficial consolidation, read in part | https://source.acts.co.za/income-tax-act-1962/sch4_19__estimates_of_taxable_income_to_be_mademade_by_provisional_taxpayers.php | 2026-11-05 |
| Fourth Schedule para 20, unofficial consolidation, read in part | https://source.acts.co.za/income-tax-act-1962/sch4_20__penalty_for_the_underpayment_.php | 2026-11-05 |
| Fourth Schedule para 20A repeal note, unofficial consolidation, read in part | https://source.acts.co.za/income-tax-act-1962/sch4_20a__penalty_in_the_event.php | 2026-11-05 |
| Fourth Schedule para 21, unofficial consolidation, read in part | https://source.acts.co.za/income-tax-act-1962/sch4_21__payment_of_provisional_tax_by_.php | 2026-11-05 |
| Fourth Schedule para 23 opening words, unofficial consolidation, read in part | https://source.acts.co.za/income-tax-act-1962/sch4_23__provisional_tax_payments_by_companies.php | 2026-11-05 |
| Fourth Schedule paras 23A and 24, unofficial consolidation, read in part | https://source.acts.co.za/income-tax-act-1962/sch4_23a__additional_provisional_tax_payments.php | 2026-11-05 |
| Fourth Schedule para 25, unofficial consolidation, read in part | https://source.acts.co.za/income-tax-act-1962/sch4_25__extension_of_time_for_payment_of.php | 2026-11-05 |
| Fourth Schedule para 27, unofficial consolidation, read in part | https://source.acts.co.za/income-tax-act-1962/sch_4_27_penalty_on_late_payment_of_provisional_tax.php | 2026-11-05 |
| Fourth Schedule paras 28 and 29, unofficial consolidation, read in part | https://source.acts.co.za/income-tax-act-1962/sch4_28__employees_tax_and_provisional.php | 2026-11-05 |
| Tax Administration Act 28 of 2011 section 187, unofficial consolidation, read in full | https://source.acts.co.za/tax-administration-act-2011/187__general_interest_rules.php | 2026-11-05 |
| Tax Administration Act 28 of 2011 section 189, unofficial consolidation, read in full | https://source.acts.co.za/tax-administration-act-2011/189__rate_at_which_interest_is_charged.php | 2026-11-05 |
| Tax Administration Act 28 of 2011 section 213, unofficial consolidation, read in full | https://source.acts.co.za/tax-administration-act-2011/213__imposition_of_percentage_based_penalty.php | 2026-11-05 |
| Tax Administration Act 28 of 2011 section 215, unofficial consolidation, read in full | https://source.acts.co.za/tax-administration-act-2011/215__procedure_to_request_remittance_of_penalty.php | 2026-11-05 |
| Tax Administration Act 28 of 2011 section 217, unofficial consolidation, read in full | https://source.acts.co.za/tax-administration-act-2011/217__remittance_of_penalty_for_nominal_or_first_incidence_of_non_compliance.php | 2026-11-05 |
| Tax Administration Act 28 of 2011 section 218, unofficial consolidation, read in full | https://source.acts.co.za/tax-administration-act-2011/218__remittance_of_penalty_in_exceptional_circumstances.php | 2026-11-05 |
| Tax Administration Act 28 of 2011 section 220, unofficial consolidation, read in full | https://source.acts.co.za/tax-administration-act-2011/220__objection_and_appeal_against_decision_not_to_remit_penalty.php | 2026-11-05 |
| Tax Administration Act 28 of 2011 section 244(1) to (3), unofficial consolidation, read in part | https://source.acts.co.za/tax-administration-act-2011/244__deadlines.php | 2026-11-05 |

Not yet confirmed: enactment of B33-2026 (R1.8 million threshold, late-payment proviso, remission limit, exclusion (hh)) and of B34-2026 (rate table, rebates, medical credits, abatement); whether Budget Review 2026 Table 4.4 is the section 5(2) and section 6(6) announcement; which table para 17(4) selects at each 2026/27 payment date and which rate eFiling used on a given IRP6; whether the unofficial consolidations match the Gazette text; how B33-2026's deemed estimate compares a tax aggregate with taxable income; whether the 25 February 2026 date in Annexure C has any legal effect (no text read gives it one); how para 20(1)(b) applies where there is no basic amount; whether para (d) 'gross income' amounts count for para 20; whether section 244(1) moves the end of the period for section 89bis(2), which changes Example 4 from 14 to 16 days; the basic amount after an assessed loss; whether a letting activity is a business under para 1 (the SARS ring-fencing guide was not read); the labour broker inclusion in Guide G01 part 2(a)(iv); whether a limb (c) notice overrides a para 1 exclusion; whether a resident non-executive director's fees are business income for (dd)(B); the treatment of a first period that passed before a person met para 1; the G05 date of 27 February 2027 against section 244(1), and that no public holiday falls on 31 August 2026, 26 February 2027 or 30 September 2027 (the holiday list was not read); whether TA Act chapter 12 has replaced sections 89bis and 89quat for provisional tax, and whether section 187(2) compounding applies to it (Interpretation Note 1 of 2019 says those provisions were not effective; Guide G01 cites section 187; section 189(2) matches Table 2); the SARS Guide G01 and Interpretation Note 1 conflict on instalment agreements; the end date of section 89quat interest as SARS applies it; and any change after 5 November 2026.

### Version history

| Version | Date | Change |
| --- | --- | --- |
| 2.2 | 2026-11-05 | Converted to the upstream template. Separated enacted from held 2026/27 amounts, restored the enacted R1 million threshold and corrected the exclusion, the basic amount, the first period and para 20 formulas, the late-payment result and the interest rules. Frontmatter reviewer field removed. |
| 2.1 | 2026-11-01 | Legacy version, carrying the billed amounts as current. |

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a registered tax practitioner, CA(SA), or registered legal practitioner) before filing or acting upon.
