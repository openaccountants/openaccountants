---
name: ax-income-tax
description: >
  Prepare the 2026 individual income-tax analysis for an Åland fiscal resident.
  Use for Aland personal income tax, separate state and municipal deductions,
  the adjusted state scale, municipal rates, work-income credits, sole-trader
  income, advance collection, interest and filing penalties. Supplies source-linked
  classification rules, deduction ordering, component examples and a completion
  register for the reviewing practitioner. This Tier 2 draft remains incomplete
  as an operational income-tax companion: final rounding, specialist conditions,
  contribution bases and the full settlement examples require further checks.
  An unresolved required source or input holds the dependent calculation and
  the complete financial output package.
jurisdiction: AX
category: international
tax_year: 2026
tax_year_notes: "Calendar 2026 source reference; 2027 amendments and earlier-year guidance are identified separately"
tier: 2
last_updated: 2026-10-16
version: 0.4
review_status: pending_review
depends_on:
  - workflow-base
  - income-tax-workflow-base
  - ax-tax-scope
---

# Åland individual income tax: 2026

Prepare separate state and Åland municipal income calculations for a qualified
reviewer. Establish the tax year, national residence and fiscal home municipality
before using a rate. This source-cited draft does not yet satisfy every mandatory
slot of the income-tax workflow contract. Use the completion register below to
identify the missing authority or input; a component example is not a final
assessment or a completed country pack.

Load the three declared dependencies. Preserve the five income-tax outputs,
the universal workbook and review checklist, all refusal traces and both bases'
checks. This guide adds substantive rules and reviewer fields; it does not
replace their workflow, question form, output requirements or tool stops.

## Establish the period and taxpayer

For a 2026 calculation, establish full-year Finnish tax residence separately
from the municipality used for taxation. [Income Tax Act 1535/1992, sections 9
and 11](https://www.finlex.fi/sv/lagstiftning/1992/1535) distinguishes residents'
worldwide income from non-residents' Finnish-source income, includes the
continuous-stay test and the Finnish citizen's substantial-ties rules, and
provides for a change of status during a year. Route non-resident, part-year,
dual-resident and treaty questions to a verified cross-border companion.
Nationality, a postal address and a residence permit alone do not settle all
these tests.

[Assessment Procedure Act 1558/1995, section 5](https://www.finlex.fi/sv/lagstiftning/1995/1558)
normally uses the municipality where the individual had a home municipality
under the Home Municipality Act at the end of the preceding year. For 2026 that
date is 31 December 2025. Section 5 has separate rules for a missing recorded
municipality, immigration and emigration. [Home Municipality Act 201/1994,
sections 2–5](https://www.finlex.fi/sv/lagstiftning/1994/201) addresses residence,
multiple homes, specified temporary absences, immigration and emigration.
Record the applicable branch and evidence. A move within Finland during 2026
does not by itself replace section 5's preceding-year-end test.

[Assessment Procedure Act section 3](https://www.finlex.fi/sv/lagstiftning/1995/1558)
uses the calendar year, or the accounting period or periods ending during that
calendar year where the accounting period differs. Verify the permitted period
and accounting method for the particular business before applying this mapping.
[Income Tax Act section 14](https://www.finlex.fi/sv/lagstiftning/1992/1535)
taxes spouses separately on their own incomes; shared-business income has its
own work-contribution and net-asset allocation rules. A shared bank account
does not establish joint taxation. Minors, estates and partnership returns
require separate verified companions.

## Classify income before applying rates

[Income Tax Act sections 29–30, 61, 64 and 110](https://www.finlex.fi/sv/lagstiftning/1992/1535)
establish the two income categories, income in money or money's worth,
employment income and fringe benefits, the income calculation and ordinary
receipt timing. Maintain the following distinct schedules.

| Receipt or movement | Preparation treatment | Required evidence or further rule |
|---|---|---|
| Salary and taxable employment benefits | Earned income at gross taxable value | Pay certificate, benefit type and applicable annual valuation decision; net bank pay is not gross salary |
| Pension or replacement benefit | Separate earned-income category | Payment certificate and the specific exemption, deduction and contribution rules; it is not automatically work-credit income |
| Sole-trader business receipts | Business computation before personal income allocation | Accounts, tax adjustments, loss schedule and verified business-income rules |
| Rent, dividends, interest and disposal proceeds | Separate capital or source-specific schedule | Establish taxable amount and exemptions; a bank credit does not establish the taxable gain or dividend fraction |
| Foreign receipt, account or tax | Flag and hold the affected cross-border calculation | Residence, source, treaty, conversion and relief authority |
| Transfer, loan or capital introduced | Record as a candidate exclusion | Match both sides or the agreement; do not exclude an unexplained credit |
| VAT, drawings and loan principal | Keep separate from personal taxable profit | Reconcile accounts and the applicable VAT/business treatment |

Under [section 30a](https://www.finlex.fi/sv/lagstiftning/1992/1535), the
entrepreneur deduction is 5% of the specified eligible business and other income,
including distributable business income after the preceding section 30 process.
Under sections 38 and 41, ordinary distributable business income has a capital
share based on a 20% annual return on the prescribed business net-asset base;
a timely claim may select 10% or all earned income, subject to section 38(2).
The start-up valuation date, mandatory capital-gain treatment, tax valuation of
assets and liabilities, and the 30% addition for qualifying wages paid in the
preceding 12 months require the statutory conditions. These are not percentages
of turnover. Preserve elections for the taxpayer and reviewer. Business expenses,
depreciation, valuation and allocation remain held until their full source
conditions are verified.

## Build two earned-income bases

[Åland Municipal Income Tax Act 2011:119, sections 1–4](https://www.regeringen.ax/alandsk-lagstiftning/alex/2011119)
adopts national legislation subject to regional departures. Section 2 excludes
the corresponding national deduction provisions from the municipal calculation.
State and municipal amounts must therefore remain separate throughout the
working paper, as [Vero's Åland guidance, section 2](https://www.vero.fi/sv/Detaljerade_skatteanvisningar/anvisningar/48911/beskattningen-pa-aland8/)
also explains.

1. Classify gross taxable earned income by source and period.
2. Deduct the applicable natural expenses separately for state and municipal tax
   to obtain each net earned-income amount.
3. Deduct the permitted contributions and other deductions from net earned
   income, applying each deduction's own base and ordering.
4. Apply the appropriate basic deduction after preceding income deductions.
5. Apply verified prior earned-income losses in the statutory order to obtain
   each taxable earned-income base.
6. Apply the adjusted state scale and the municipal rate to their respective
   bases, then allocate credits in the required order.

The distinction between net earned income and final taxable income matters for
the work-credit taper. [National section 30](https://www.finlex.fi/sv/lagstiftning/1992/1535)
and [regional section 1a](https://www.regeringen.ax/alandsk-lagstiftning/alex/2011119)
place prior earned-income losses after the year's income deductions. Do not
silently reorder that statutory calculation to match a generic workbook label.

### Losses and source restrictions

[Income Tax Act sections 117–119](https://www.finlex.fi/sv/lagstiftning/1992/1535)
deduct assessed losses oldest first. The earned-income loss defined in section
118 carries against the corresponding earned income for the following 10 tax
years in state and municipal taxation. An assessed loss follows the statutory
definition; a negative amount after a personal allowance is not automatically
such a loss. [Assessment Procedure Act section 26e](https://www.finlex.fi/sv/lagstiftning/1995/1558)
provides for establishing losses in assessment or on appeal. Obtain the
assessment and loss-year schedule before using a balance.

Business and agricultural losses have their separate section 119 ten-year
carry-forward against the corresponding results. [Section 59](https://www.finlex.fi/sv/lagstiftning/1992/1535)
allows an individual's timely claim to deduct all or part of a current business
or agricultural loss against capital income, with both spouses required to claim
for their shared business. Section 121 has separate cessation rules. Do not
offset a business loss against wages automatically, invent a carry-back or treat
an unevidenced loss as available relief. Capital-income losses and specialist
cessation/ownership conditions need their own complete checks.

### Ordinary wage expenses and contributions

The following 2026 figures come from [national sections 31, 93, 95–96 and
106](https://www.finlex.fi/sv/lagstiftning/1992/1535), [amendment
1141/2025](https://www.finlex.fi/fi/lainsaadanto/saadoskokoelma/2025/1141),
[regional sections 9–14 and 23](https://www.regeringen.ax/alandsk-lagstiftning/alex/2011119)
and [ÅFS 2026:10](https://www.regeringen.ax/node/222885). The regional amendment
commences on 1 March 2026 and applies to tax year 2026.

| 2026 item | State calculation | Åland municipal calculation |
|---|---|---|
| Automatic wage earning-expense deduction | EUR 750, capped at salary | EUR 750, capped at salary |
| Other ordinary wage earning expenses | Deduct only the aggregate excess over the automatic allowance | Same allowance/excess structure under regional section 13 |
| Unemployment fund membership fees | Separately deductible; not absorbed by the EUR 750 limit | Separately deductible under regional section 13 |
| Labour-market organisation membership fees | Disallowed from tax year 2026 | Disallowed from tax year 2026; distinguish unemployment fund fees |
| Home-to-work commuting | Cheapest-method rule; maximum deduction EUR 7,000 after EUR 900 own-risk | Maximum deduction EUR 6,000 after EUR 750 own-risk; section 10's public-transport exception can remove the own-risk |
| Qualifying benefit-month commuting relief | EUR 80 per full month, EUR 160 minimum own-risk; preserve the 2026 benefit-law changes | EUR 80 per full month, EUR 160 minimum; verify the regional benefit references |
| Own/family home or holiday-home costs against wages | Disallowed from tax year 2026 | Disallowed from tax year 2026 |
| Compulsory employee pension, unemployment and health daily-allowance premiums | Deduct from net earned income under section 96 | Deduct from net earned income under regional section 14 |
| Healthcare contribution | Not an income deduction | Not an income deduction |
| Own/spouse compulsory pension premiums | Personal deduction only if not already deducted from business or farm income | Same no-double-deduction condition in regional section 14 |
| Basic deduction | Up to EUR 4,265, tapered at 18% | Up to EUR 3,925, tapered at 8.4% |

For either basic deduction, let R be the non-negative income remaining after
the preceding applicable deductions and B the full basic deduction. Its
unrounded arithmetic is `min(R, max(0, B - taper × max(0, R - B)))`.
Use the separate R, B and taper for each tax. Verify the loss and rounding stages
before deriving the final assessment.

Regional section 10 removes the EUR 750 own-risk where more than half the
deductible commuting costs are public transport. Its non-public-transport
valuation refers to national section 93(2) and the annual Tax Administration
decision. The currently retained mileage decision is expressly for 2025;
permission to use those figures when estimating a 2026 tax card does not verify
a final 2026 mileage allowance. Hold that valuation.

The [general Vero commuting page](https://www.vero.fi/sv/privatpersoner/avdrag/resekostnader/resor-mellan-bostaden-och-arbetsplatsen/)
labels EUR 800 own-risk, EUR 75 monthly relief and EUR 150 minimum as 2026.
These conflict with the retained national section 93, whose own-risk is EUR 900,
and the [2026 withholding decision, section 4.2.1](https://www.vero.fi/syventavat-vero-ohjeet/paatokset/47363/verohallinnon-paatos-ennakonpidatysprosenttien-laskentaperusteista-palkkatuloa-varten-ja-ennakonkannossa-maarattavan-ennakkoveron-laskentaperusteista-vuodelle-2026/).
The reason is unverified. Preserve the conflicting guidance in the reviewer
brief; do not substitute its figures for either statute.

For qualifying home use to earn income other than wages, [Vero's annual 2026
workroom decision](https://www.vero.fi/sv/Detaljerade_skatteanvisningar/beslut/360555/skatteforvaltningens-beslut-om-beloppet-av-avdrag-for-arbetsrum-vid-beskattningen-for-ar-2026/)
sets EUR 980 for qualifying full-time use, EUR 490 for qualifying part-time use
and EUR 245 for sporadic recurring use; insignificant use gives no deduction.
Read the workday and continuity conditions. National section 31(9) and regional
section 9(9) govern the home-cost restriction. Regional maximum-amount wording
and an actual-cost claim require verification; do not infer an election to a
higher amount or apply this deduction to salary.

### Pension and other deductions

[National section 100](https://www.finlex.fi/sv/lagstiftning/1992/1535) and
[regional section 19](https://www.regeringen.ax/alandsk-lagstiftning/alex/2011119)
use different pension-deduction formulas. The [2026 national taxable-income
guidance, section 3.5](https://www.vero.fi/syventavat-vero-ohjeet/ohje-hakusivu/49038/verotettavan-tulon-laskeminen-henkiloverotuksessa9/)
gives a national maximum of EUR 11,080, capped at pension. The deduction reduces
by 51% of net earned income between that maximum and EUR 22,500, and by 19.6%
of the portion above EUR 22,500; the two taper percentages do not apply to the
same slice.
Regional section 19 instead multiplies the full annual single-person national
pension by 1.346, subtracts EUR 1,480 and rounds upward to the next EUR 10;
it caps the deduction at pension and tapers by 51% of excess net earned income.
The [Åland overview](https://www.vero.fi/sv/Detaljerade_skatteanvisningar/anvisningar/48911/beskattningen-pa-aland8/)
and the 2026 pension prepayment decision give EUR 11,240 for the municipal
maximum. Final annual input and eligibility checks remain open. Employment
income can reduce a pension deduction; pension is not ordinary work-credit
income.

The national taxable-income guidance contains two inconsistent pension
illustrations for its stated EUR 18,000 pension case. Use the verified statute
and formula; do not copy an illustration without recomputing it and resolving
the applicable source conditions.

Regional sections 11–12 and 15–21 contain separate work-location housing,
forestry-work, collective pension, seafarer, hardship, donation, disability and
study deductions. Establish each trigger and its national cross-references
before claiming it. The former separate medical-expense deduction and former
municipal earned-income deduction are repealed. Collective supplementary
pension deduction section 15 and the special deficit-credit provisions remain
relevant through 2026; [ÅFS 2026:70](https://www.regeringen.ax/node/226467)
changes them from 1 January 2027, first applying in tax year 2027. A prospective
repeal does not remove a 2026 entitlement.

## Apply the tax schedules and credits

### State earned-income tax

[Annual Scale Act 1140/2025](https://www.finlex.fi/sv/lagstiftning/2025/1140)
applies from 1 January 2026. [Income Tax Act section 124(5)](https://www.finlex.fi/sv/lagstiftning/1992/1535)
reduces its marginal percentages by 12.64 percentage points for a person whose
fiscal municipality is in Åland. The resulting 2026 scale, corroborated by
[Vero's Åland table](https://www.vero.fi/sv/Detaljerade_skatteanvisningar/anvisningar/48911/beskattningen-pa-aland8/),
is applied to state taxable earned income, not gross salary or the municipal base.

| State taxable earned income, EUR | Tax at the lower boundary, EUR | Rate on the excess |
|---|---|---|
| 0 to 22,000 | 0.00 | 0% |
| Over 22,000 to 32,600 | 0.00 | 6.36% |
| Over 32,600 to 40,100 | 674.16 | 17.61% |
| Over 40,100 to 52,100 | 1,994.91 | 20.61% |
| Over 52,100 | 4,468.11 | 24.86% |

At a boundary, the preceding slice and the next row give the same amount.
The table is before work-income and other tax credits. A zero first state
band does not establish zero municipal tax, contributions or media fee.

[Income Tax Act section 124(1), (4)](https://www.finlex.fi/sv/lagstiftning/1992/1535),
as amended from 1 January 2026 by Act 1141/2025, also charges an additional
5.85% on pension income after the pension-income deduction to the extent that
this distinct base exceeds EUR 60,000. The former EUR 47,000 threshold applies
to the earlier wording, including 2025; do not carry it into 2026. The Åland
12.64 percentage-point reduction applies to the progressive scale, not this
additional rate. A pensioner's full state liability requires this separate
component, the lawful pension deduction and all applicable credit and rounding
rules. Keep the complete pension result held until those conditions are verified.

### Municipal and capital income tax

Use the fiscal municipality established above. The [Tax Administration's 2026
municipal and church rate decision 1012/2025](https://www.finlex.fi/sv/lagstiftning/2025/1012)
contains the annual rows below. These municipal percentages apply to the
separate municipal taxable earned-income base before applicable credits.

| Municipality | 2026 municipal rate | Municipality | 2026 municipal rate |
|---|---|---|---|
| Brändö | 17.70% | Kökar | 19.70% |
| Eckerö | 18.50% | Lemland | 17.80% |
| Finström | 19.00% | Lumparland | 19.50% |
| Föglö | 18.50% | Mariehamn | 17.00% |
| Geta | 18.50% | Saltvik | 18.50% |
| Hammarland | 18.00% | Sottunga | 18.00% |
| Jomala | 17.50% | Sund | 19.00% |
| Kumlinge | 19.30% | Vårdö | 19.00% |

### Church membership and parish

[Act 1013/2012, section 1](https://www.finlex.fi/sv/lagstiftning/2012/1013)
charges an individual who belonged to an Evangelical Lutheran parish at the end
of the preceding year on municipal taxable income. For 2026, establish membership
at 31 December 2025. [Vero's church-tax guidance](https://www.vero.fi/sv/skatteforvaltningen/nyhetsrummet/presentations_och_undervisningsmateria/kyrkoskat/)
uses the preceding-year-end membership test for both the Lutheran and Orthodox
churches. [Orthodox Church Act 985/2006, section 77](https://www.finlex.fi/sv/lagstiftning/2006/985)
also bases church tax on municipal taxable income. Use the lawful Åland municipal
base, not the state base or gross wages, before applicable tax credits.

The following church columns come from the same [2026 annual decision 1012/2025](https://www.finlex.fi/sv/lagstiftning/2025/1012).
They cover the ordinary geographical parish branch. Vero identifies different
rules for members of Olaus Petri and the German parish, and possible liability
for membership of another Evangelical Lutheran church abroad. Hold those cases
until their membership, parish and applicable rate are established.

| Municipality | 2026 Lutheran rate | 2026 Orthodox rate |
|---|---|---|
| Brändö | 2.00% | 1.75% |
| Eckerö | 1.80% | 1.75% |
| Finström | 1.95% | 1.75% |
| Föglö | 2.00% | 1.75% |
| Geta | 1.95% | 1.75% |
| Hammarland | 1.80% | 1.75% |
| Jomala | 1.70% | 1.75% |
| Kumlinge | 2.00% | 1.75% |
| Kökar | 2.00% | 1.75% |
| Lemland | 1.70% | 1.75% |
| Lumparland | 1.70% | 1.75% |
| Mariehamn | 1.55% | 1.75% |
| Saltvik | 1.75% | 1.75% |
| Sottunga | 2.00% | 1.75% |
| Sund | 1.95% | 1.75% |
| Vårdö | 1.95% | 1.75% |

Unknown membership is Needs Input, not zero tax. Record the church, parish and
effective membership dates and check any conflicting prefilled information.
The Vero page, updated 4 January 2022, states both the year-end membership test
and a separate exit-notification deadline on the next-to-last calendar day.
This draft does not resolve that notice wording or prescribe an exit deadline.
Establish the legally effective membership status from the relevant evidence.

[Church Law 652/2023, chapter 6 section 2](https://www.finlex.fi/sv/lagstiftning/2023/652)
governs the Lutheran church-tax funding and relief decision. Its chapter 13
repeals the former Church Law 1054/1993 from 1 July 2023, although Act 1013/2012
section 3 still displays that older cross-reference. Sections 2 of Act 1013/2012
and 78 of the Orthodox Act provide corresponding municipal-tax relief and
separate application-based relief. An unresolved relief claim is not an
exemption. Estate, foreign-membership, contested effective-date and relief or
appeal cases require their complete conditions; the table alone cannot clear them.

### Capital income

[Income Tax Act section 124(2)](https://www.finlex.fi/sv/lagstiftning/1992/1535)
taxes ordinary taxable capital income at 30% up to EUR 30,000 and 34% above it.
Establish the taxable capital-income amount after the relevant source expenses,
losses, exemptions and allocations first. This rate statement supplies no
dividend, disposal, rental or foreign-tax calculation by itself.

### Work-income credit and allocation

[National section 125](https://www.finlex.fi/sv/lagstiftning/1992/1535), as
amended by [1141/2025](https://www.finlex.fi/fi/lainsaadanto/saadoskokoelma/2025/1141),
and [regional section 25](https://www.regeringen.ax/alandsk-lagstiftning/alex/2011119)
govern the following 2026 credit. Qualifying income includes the listed salary,
work/services, earned royalties, earned dividends and earned business or
partnership shares. It is not every type of earned income.

- Accrual is 18% of qualifying income, with a base maximum of EUR 3,430.
- The maximum increases by EUR 1,200 if the person reached age 65 before 2026.
- It increases by EUR 105 for each qualifying minor child for whom the person
  is guardian at year-end. The increase doubles for a child for whom the person
  is sole guardian if the Act's spouse provisions do not apply and there is no
  spouse abroad. Section 8 defines a minor child by age before the tax year.
- Reduce the credit by 2% of net earned income above EUR 35,000, only until
  that income reaches EUR 50,550. There is no further taper above that point.
- Apply the credit before other income-tax credits, first to state earned-income
  tax. Allocate the excess proportionately against municipal tax, healthcare
  contribution and church tax. It does not reduce the daily-allowance premium.

Use the distinct qualifying-income, net-earned-income and tax amounts in that
sequence. Do not deduct the credit from income, subtract it in full from each
tax, or create a cash refund from an unused amount. Establish the available
taxes and complete allocation/rounding rules before producing final amounts.
Deficit credits, household/oil-heating credits, student-loan credits and
maintenance relief require their own eligibility, ordering and spouse rules.

## Contributions, media fee and collection

### Establish insured status

[Health Insurance Act 1224/2004, chapter 1 sections 2–3](https://www.finlex.fi/fi/lainsaadanto/2004/1224)
links insured status to the work, entrepreneurial and residence routes in
[Act 16/2019, sections 4–10](https://www.finlex.fi/fi/lainsaadanto/2019/16),
and the treated-as-resident routes in sections 11–13. Kela determines health
insurance status. For the ordinary residence branch, sections 4–5 require
lawful presence, a valid residence permit where required, an actual dwelling
and home in Finland, and continuous predominant presence there. If a permit
applied for in Finland is granted, section 4 treats the requirement as met from
the application date. Record the statutory route, relevant period and evidence.

[Vero's insured-person guidance, section 1.2](https://www.vero.fi/syventavat-vero-ohjeet/ohje-hakusivu/338472/vakuutetun-sairausvakuutusmaksu2/)
expressly distinguishes social-insurance residence from income-tax residence.
An Åland fiscal municipality or Finnish taxable income does not establish
insured status. Meeting a statutory route gives coverage without purchasing a
policy, but each benefit has additional entitlement conditions. This is not a
verification of every Åland public-health-service entitlement.

The Health Insurance Act's specified diplomatic and related exclusions, EU
coordination, social-security agreements, foreign coverage and pension routes
require separate checks. Migration, temporary or repeated absence, student and
special residence cases remain held. [Amendment 22/2019](https://www.finlex.fi/fi/lainsaadanto/saadoskokoelma/2019/22)
introduced the reviewed scope reference from 1 April 2019. [Amendment 66/2026](https://www.finlex.fi/fi/lainsaadanto/saadoskokoelma/2026/66)
changes Act 16/2019's worker route from 1 May 2026; it does not replace the
ordinary residence test with a worker earnings threshold.

### Separate contribution bases

[Vero's insured-person health guidance](https://www.vero.fi/syventavat-vero-ohjeet/ohje-hakusivu/338472/vakuutetun-sairausvakuutusmaksu2/)
distinguishes the deductible daily-allowance premium from the non-deductible
healthcare contribution. The [2026 social-insurance table](https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/being-an-employer/social-insurance-contributions/)
shows ordinary employee pension 7.30% and unemployment 0.89%; an applicable
shareholder-employee unemployment rate is 0.39%. These are rate references,
not evidence of a particular person's insurance coverage, age scope or base.
Consume evidenced amounts from a verified contribution/payroll analysis.

[Health Insurance Act 1224/2004, chapter 18 sections 14–15](https://www.finlex.fi/fi/lainsaadanto/2004/1224)
establishes separate healthcare and daily-allowance bases. The ordinary healthcare
base is municipal taxable income unless the Act supplies another base. Combining
that statutory reference with the applicable Åland municipal rules means using
the insured Åland resident's lawful municipal taxable income. This is a statutory
inference, not an express Åland deduction table in the health guidance. Verify
each local deduction and every exception before using that base.

For YEL/MYEL-insured activity, confirmed insured income replaces the specified
entrepreneurial income under chapter 18 section 14(2). Recalculate the applicable
municipal deductions on that substituted base. Section 14(3) expressly excludes
deduction of YEL/MYEL pension premiums from the healthcare base. Unrelated
employment income remains additional. Do not add confirmed income to the
entrepreneurial income it replaces or copy the personal income-tax deduction of
YEL/MYEL premiums into this health calculation.

The daily-allowance base instead uses the insurance-law wage and confirmed-income
definitions in chapter 11 sections 3–4 and chapter 18 section 15. Pensions and
ordinary replacement benefits are outside that base. The statutory wage
exclusions, insured-activity attribution and uninsured entrepreneurial cases
need their own checks; a zero daily-allowance charge does not by itself permit
the increased healthcare rate.

[Decree 1026/2025, sections 1–4](https://www.finlex.fi/fi/lainsaadanto/saadoskokoelma/2025/1026)
applies for 2026 and establishes these insured-person rates:

| 2026 charge | Rate and base condition |
|---|---|
| Ordinary healthcare | 1.10% of the applicable municipal or special base |
| Increased healthcare | Ordinary 1.10% plus the conditional 0.39% differential component below; 1.49% is the combined rate only on a base to which both components apply |
| Ordinary daily allowance | 0.88% of the whole applicable base once annual relevant wages/entrepreneur income reach EUR 17,255; zero below that threshold |
| YEL entrepreneur financing supplement | 0.23% of confirmed YEL income, including below the ordinary threshold; not a MYEL supplement |

[Chapter 18 section 20(3)–(4)](https://www.finlex.fi/fi/lainsaadanto/2004/1224)
requires the 0.39% additional component where the insured person receives earned
income outside sections 15–18, subject to the exclusion for income in section
14(2). Calculate it from the applicable positive difference between the
healthcare-contribution base and the daily-allowance-contribution base. No
additional component is collected when the daily base exceeds the healthcare
base; equality also gives zero. Establish both bases, the income trigger and
the section 14(2) exclusion separately. A YEL/MYEL substitution is not itself
permission to charge the supplement, and a mixed-income case does not permit
1.49% on the entire healthcare base. Missing attribution or coverage holds the
dependent component and the full contribution result.

Chapter 18 section 5 starts daily-allowance liability at the beginning of the
month after turning 16 and ends it after the month of turning 68. It exempts
a person who dies during the tax year from the insured person's health
contribution. Special bases, age-transition allocations, international coverage
and changes in insured status remain subject to their own conditions.

### Personal media fee

[Regional Media Fee Act 2019:103, section 2](https://www.regeringen.ax/alandsk-lagstiftning/alex/2019103)
requires general Finnish tax liability, an Åland home municipality and turning
18 no later than the end of the tax year. The personal fee applies when the
statutory income measure **exceeds EUR 14,000**. Equality does not meet that
test. Compare state net earned income plus state net capital income with
confirmed YEL plus MYEL work income and use the higher amount. Without confirmed
work income, use the combined state net amounts. This is not municipal taxable
income, gross receipts or the final state base after personal deductions.

[Vero's 2026 media-fee guidance, sections 2.1–2.3 and appendix](https://www.vero.fi/sv/Detaljerade_skatteanvisningar/anvisningar/89754/medieavgift-i-landskapet-%C3%A5land4/)
and [ÅFS 2025:54, section 1](https://www.regeringen.ax/node/219674) fix the charge
at EUR 128 for tax year 2026. It is a fixed annual amount once the test is met,
not a percentage of the excess. Natural earning expenses enter the state net
income calculation; employee pension premiums, acquisition-debt interest and
the pension-income deduction are not natural deductions for this comparison.
Ordinary work-income or household tax credits do not reduce the fee, and the
fee is not an income deduction. Foreign-tax relief has separate treaty conditions
and remains held.

The fee is personal, so several members of a household can owe it. Ownership,
use or ability to use a radio, television or the service does not remove
liability. The reviewed Act and personal guidance provide no disability-specific
exemption. Unlike the insured health contribution, the media fee remains payable
for the death year by the estate; later estate years are excluded. Full estate,
part-year, migration and cross-border calculations remain outside this draft's
ordinary resident branch.

There is a commencement discrepancy to resolve before any affected collection
instruction. ÅFS 2025:54 was issued on 19 June 2025 and printed on 29 August
2025. Its section 2 expressly starts on **1 October 2026**, while section 1
fixes the tax-2026 fee. Vero's guidance is effective from 1 January 2026 and
cites that decision. No official correction or complete treatment of collection
before 1 October 2026 was verified. Preserve both dates; do not silently change
the original to 2025 or infer an exemption for the earlier period.

### Advance collection reference

The [2026 withholding/prepayment decision, sections 3.3–3.4 and 7](https://www.vero.fi/syventavat-vero-ohjeet/paatokset/47363/verohallinnon-paatos-ennakonpidatysprosenttien-laskentaperusteista-palkkatuloa-varten-ja-ennakonkannossa-maarattavan-ennakkoveron-laskentaperusteista-vuodelle-2026/)
corroborates the separate calculations within advance collection, including
the EUR 128 media-fee amount. It does not resolve the original decision's
commencement discrepancy. Do not add employee pension or
unemployment deductions twice to the authority-collected income-tax balance.

The same decision applies from 1 January 2026. Its automatic initial estimates
and omissions do not remove final-assessment deduction rights. Section 8 rounds
the withholding percentage upward in half-percentage-point increments, capped
at 60%. That rule does not establish annual taxable-income, credit-allocation
or tax-amount rounding. A tax card sets collection; it is not the final liability.

### Return, dates and settlement

[Assessment Procedure Act sections 7–8](https://www.finlex.fi/sv/lagstiftning/1995/1558)
requires review and correction of the prefilled return. Unchanged prefilled
information is deemed filed as shown; if no prefilled return arrives but
reportable matters exist, the individual must file without waiting for a request.
A business return remains separately required. [Vero's sole-trader instructions](https://www.vero.fi/sv/foretag-och-samfund/skatter-och-avgifter/rorelseidkare-eller-yrkesutovare/deklarationsanvisning/)
identify Form 5, including a return without activity. Those instructions expressly
display tax year 2025 and a 1 April 2026 deadline. That date is not the deadline
for 2026 income. Use the actual personal return/authority prescription and
verify the 2026-specific form revision before mapping fields.

[Form 17, Ålandsbilaga](https://www.vero.fi/sv/skatteforvaltningen/kontakta-oss/blanketter/beskrivning/17-%C3%A5landsbilaga-3017r/)
supplements the prefilled return for deductions specific to Åland municipal
taxation; the information can also be supplied in MinSkatt. [Vero's paper-filing
instructions](https://www.vero.fi/sv/privatpersoner/skattekort-och-skattedeklaration/skattedeklaration_och_beskattningsbeslu/deklarationsanvisning/s%C3%A5-h%C3%A4r-deklarerar-du-p%C3%A5-papper/)
identify separate correction forms including 50A for earned income/deductions,
1A for commuting, 19 for work-location housing and 50B for capital income.
HTML form identities do not verify PDF layout, a 2026 form version or live portal
fields. A preliminary tax calculation is not a payment notice.

[Assessment Procedure Act sections 34, 34a, 37 and 50](https://www.finlex.fi/sv/lagstiftning/1995/1558)
distinguish assessment credits and settlement cash. Record reported or reliably
established withholding and the advances imposed by the authority, separately
from actual advance payments. Preserve the statutory exceptions, including
foreign transfers, accounting-period mismatches and collusive unpaid withholding.
An employer's non-payment alone is not a general reason to deny evidenced
employee withholding.

Under section 50, excess assessment credits first reduce advances from the
latest due date to the oldest. Paid amounts of reduced advances and other
refundable credits are returned with the applicable interest. Insufficient
credits produce residual tax plus interest; residual tax below EUR 10 is not
imposed. The cash reconciliation must therefore show imposed, paid, reduced,
unpaid and refunded advances separately. A simple subtraction of cash advances
from liability does not reproduce this statutory process in every case.

[Tax Collection Act 11/2018, section 12](https://www.finlex.fi/sv/lagstiftning/2018/11)
uses the due date in the tax-imposition decision. Sections 22–24 and 30–32
provide for refund offsets and payout; unused refund/payment funds must reach
EUR 10 in aggregate for payout. Use the person's current assessment notice,
collection statement and dates. The ordinary collection rules below do not
establish an individual's notice, final liability or a common 2027 due date.

### Advances and ordinary payment dates

[Prepayment Act 1118/1996, sections 6 and 23–24](https://www.finlex.fi/sv/lagstiftning/1996/1118)
provides for assessed advances and their amendment. A taxpayer can request a
new, amended or cancelled advance until assessment ends. Payment without the
required decision is not an application for an additional advance. Keep the
decision, imposed amount, due dates and payment evidence separately.

[Advance decision VH/6503/00.01.00/2022, sections 1–6](https://vero.fi/syventavat-vero-ohjeet/paatokset/47497/verohallinnon-p%C3%A4%C3%A4t%C3%B6s--luonnollisen-henkil%C3%B6n-ja-kuolinpes%C3%A4n-ennakonkannon--alarajasta-ja-kantoerist%C3%A4/)
applies from 1 January 2023 until further notice to the ordinary individual
branch, including a sole trader. Its minimum total advance before division is
EUR 170. The ordinary in-year schedule is:

| Total advance, EUR | Instalments | Collection months |
|---|---|---|
| 170 to 500 inclusive | 2 | March and September |
| Over 500 to 1,700 inclusive | 3 | February, July and November |
| Over 1,700 to 10,000 inclusive | 6 | February, April, June, August, October and December |
| Over 10,000 | 12 | January to December |

Instalments are equal to cent precision. A taxpayer-requested remaining-month
schedule and changes during the year can alter the ordinary pattern. After
year-end, the advance is collected in one instalment. For an amended advance,
subtract instalments already due before dividing the remaining amount; a
remaining amount below EUR 170 is collected in one instalment. Reductions
first affect instalments not yet due, then those already due from latest to
oldest. Do not substitute the residual-tax instalment rules for this schedule.

[Prepayment Act section 24](https://www.finlex.fi/sv/lagstiftning/1996/1118)
separately prevents imposing tax below EUR 10 as a consequence of determining
or amending an advance. This tests the tax imposed by that decision; the
EUR 170 initial minimum and amended-advance division rule do different jobs.
An existing unpaid or remaining instalment below EUR 10 is not, by itself,
evidence that the decision imposes tax below EUR 10. Verify the decision's
assessed amount and already-due instalments before applying either rule;
hold an unresolved small amendment instead of cancelling an existing debt.

[Tax Collection Decree 1010/2019, sections 1–3 and 9–10](https://www.finlex.fi/fi/lainsaadanto/2019/1010)
supplies the following ordinary individual residual/refund rules:

- Residual tax of at least EUR 170 has two instalments; below that amount it
  has one, subject to the separate EUR 10 non-imposition rule above.
- Equal instalments place any division remainder in the first instalment.
  The first residual instalment falls on day 1 of the second month after the
  assessment-completion month; the second falls on day 1 of the fourth month.
- The ordinary refund payment date is day 3 of the second month after the
  completion month. It is deemed paid when the Tax Administration's account
  is debited; this does not promise receipt in the taxpayer's account that day.
- A due date or refund payment date that is not a bank day moves to the next
  bank day. Verify the applicable calendar and current decision before use.

Section 2 separately addresses changed assessments: a new amount imposed on
reassessment or appeal is payable in one instalment; a reduction of tax already
in two instalments affects the second first. Its EUR 85 remaining-collection
rule belongs to that changed-tax context. It is not the initial two-instalment
threshold. Section 7's changed-assessment dates and exit-tax deferrals require
their own notice and specialist checks.

[Vero's residual-payment page](https://www.vero.fi/sv/privatpersoner/betalning/betalning-av-kvarskatt/sa-har-betalar-du/)
shows a calendar for payments in 2026. It does not establish the calendar for
2026 income settled in 2027. Corrections, including a spouse's corrections,
can change completion and payment dates. Use the latest notice. [Vero's
additional-advance instructions](https://www.vero.fi/sv/foretag-och-samfund/skatter-och-avgifter/forskottsskatt/tillaggsforskott/)
likewise display the tax-2025/2026 settlement cycle. Their dated application
opening and year-end receipt dates cannot be copied into the 2026-income cycle.

### Reduced interest and late-payment interest

[Tax Interest Act 1556/1995, sections 5a–5c](https://www.finlex.fi/sv/lagstiftning/1995/1556)
distinguishes interest included in ordinary settlement from interest on overdue
tax. The ordinary late-payment annual rate is the [Interest Act section 12](https://www.finlex.fi/sv/lagstiftning/1982/633)
reference for the half-year preceding the calendar year, plus 7 percentage
points. The reduced rate uses that reference plus 2 points, with a 0.5% floor.
[Vero's current guidance](https://www.vero.fi/sv/foretag-och-samfund/skatter-och-avgifter/forskottsskatt/tillaggsforskott/nedsatt-dr%C3%B6jsm%C3%A5lsr%C3%A4nta/)
confirms 4.5% reduced interest and 9.5% ordinary late interest for calendar 2026.
These are collection-year rates, not permanent rates attached to 2026 income.
The [Bank of Finland's 30 June 2026 release](https://www.suomenpankki.fi/fi/ajankohtaista/lehdistotiedotteet-ja-uutiset/tiedotteet/2026/korkolain-mukainen-viitekorko-ja-viivastyskorot-1.7.31.12.2026)
establishes the second-half-2026 reference as 2.5%. That is the retained input
for the statutory calendar-2027 formula; verify the law and applicable rate
announcement before preparing a 2027 collection calculation.

For ordinary calendar-year individual residual tax, reduced interest starts
on 1 February following the tax year and runs through the first instalment's
due date. For an additional advance due after January, it runs from that same
start through the advance due date. The authority guidance uses actual days
in the period and year. Deduct EUR 20, capped at the interest amount, only from
reduced interest on residual tax imposed at completion of annual assessment.
There is no corresponding EUR 20 deduction from additional-advance interest.
Paying early does not shorten these due-date-based reduced-interest periods.
A January date shifted into February can therefore create interest despite
an earlier cash payment. Obtain the additional-advance decision before payment.

Ordinary overdue interest runs from the day after the due date through payment.
Do not compound late interest on a tax supplement or on late/reduced interest.
No reduced interest is calculated on a tax increase or late-filing fee. The
EUR 3 minimum in the Act's separate sections 2 and 4 is not an ordinary
income-tax section 5a minimum. Section 10 disallows an income-tax deduction for
these interest charges. Sections 6–7 address tax reductions and qualifying
interest relief; an unresolved application is not an assumed waiver. Refund
offsets, payment allocation, changed assessments and periods spanning rate
years require their complete rules. Final monetary rounding remains held.

### Late filing and tax increases

[Assessment Procedure Act sections 32–33](https://www.finlex.fi/sv/lagstiftning/1995/1558),
introduced by [amendment 15/2018](https://www.finlex.fi/sv/lagstiftning/forfattningssamling/2018/15)
from tax year 2018, and [Vero's guidance of 20 May 2026](https://www.vero.fi/sv/Detaljerade_skatteanvisningar/anvisningar/66816/pofoljdsavgifter-for-inkomstbeskattningen/)
distinguish the ordinary natural person's EUR 50 annual late-filing fee from
a tax increase. An individual sole trader uses the natural-person branch.
Corporate and partnership-share amounts require separate rules.

A complete required main return filed late but before assessment ends comes
within the fee branch even if the authority requested it. A late correction
of an existing or deemed prefilled return qualifies for that substitution only
on the taxpayer's own initiative. An issue-specific authority request or
awareness of control can end own initiative; a general public announcement of
sector checks alone does not. Separate errors in the same return may still
attract a tax increase. The fee is once per tax year, not once per form, and
is not deductible. Both charges are imposed after statutory tax credits.

An omitted taxpayer-favourable item ordinarily attracts neither charge, subject
to the repeated-failure/clear-indifference exception. This does not excuse an
entirely late required return that reports only a loss or deductions, or an
unfounded deduction claimed. Apply the statutory non-imposition grounds before
any minimum: a minor failure, valid reason or the applicable unreasonableness
test; the fee also has outside-control and other-special-reason grounds.
Vero's EUR 2,000 income/EUR 500 tax and three-day minor-failure criteria are
conditional administrative interpretations. Repeated or clearly deliberate
failures are excluded; a small income or loss alone does not excuse a wholly
late return. Record the evidence and reviewer decision instead of treating
these criteria as automatic safe harbours.

For an incomplete, incorrect or missing required disclosure, first establish
the failure, applicable exemption and correct penalty base. Added income is
the primary base, including a qualifying reduction of an assessed loss. Where
that base cannot be used, or income was reported in the wrong income category,
section 32b uses increased tax. Do not apply an added-income percentage to tax
or net unrelated failures together automatically.

| Qualifying branch | Percentage of added income | Percentage of increased tax |
|---|---|---|
| Ordinary | 2% | 10% |
| Repeated failure or clear indifference | 3% to 10% | 15% to 50% |
| Estimated assessment | 5% | 25% |
| Statutory interpretive uncertainty or qualifying unreasonableness | 1% | 5% |
| Foreign income satisfying section 32a(5), excluding the aggravated branch | 1% | 5% |
| Own-initiative correction after completion with the explanation duty fulfilled | 0.5% | 2% |

The natural-person minimum is EUR 75 when an increase is imposed; guidance
applies it to the aggregate percentage increases in the same assessment
decision. Non-minor formal failures may attract a minimum even without added
income. Qualifying post-completion correction requires cooperation and evidence;
filing a missing return after estimated assessment is not automatically that
branch. The EUR 25,000 cap in section 32a(8) concerns the specific failures
listed in section 32(1)(2–4), not every ordinary income-tax increase.

The guidance contains two apparent wording conflicts. Section 3.2.5 describes
the 15% to 50% increased-tax range using added-income wording, whereas section
32b makes increased tax the base. Section 3.2.12 states a EUR 150 minimum without
qualifying the taxpayer category, although section 32a(9) and guidance section
3.2.9 give EUR 75 for natural persons. Preserve both discrepancies for the
reviewer and follow the statutory category and base. Do not infer a blanket
corporate-only scope for the foreign-credit guidance.

Disputed culpability, trust protection, foreign-credit penalties, remission,
criminal referrals and appeals require a qualified review of the complete
applicable process. [Act 781/2013](https://www.finlex.fi/sv/lagstiftning/2013/781)
has separate-decision and parallel-criminal-process safeguards; this guide does
not certify that whole chain. Non-imposition under sections 32–33 and later
collection remission are distinct. Hold the affected charge and remedy calendar
when facts, competence, service dates or applicable law are unresolved.

## Currency and monetary precision

Use EUR. [The declaration-details decision VH/7150/00.01.00/2025, section 1](https://vero.fi/syventavat-vero-ohjeet/paatokset/62189/verohallinnon-paatos-veroilmoituksessa-annettavista-tiedoista8/)
requires income, deductions, debts and reportable asset values to cent precision.
It commences on 1 January 2026 and first applies to personal tax-year-2025
returns. This reporting rule alone does not settle intermediate calculations
or a final-assessment rounding tie.

[Acts 896/2001](https://www.finlex.fi/fi/lainsaadanto/saadoskokoelma/2001/896)
and [907/2001](https://www.finlex.fi/fi/lainsaadanto/saadoskokoelma/2001/907)
repealed the old whole-mark tax/base provisions from 2002. Their
[explanatory proposal HE 91/2001](https://www.finlex.fi/fi/hallituksen-esitykset/2001/91)
explains cent precision. This historical explanation is not a complete current
rounding algorithm. Preserve exact intermediate arithmetic in demonstrations;
hold the affected final figures until rounding direction, stage and allocation
are verified. Foreign conversion basis and dates also require separate sources.

## Hypothetical component examples

These examples test individual rules with invented inputs. None completes the
employee, self-employed or mixed full settlement ladder required by the domain
contract. Monetary results described as unrounded remain intermediate values.

| Position | Hypothetical inputs and calculation | Result and boundary |
|---|---|---|
| State scale at EUR 32,600 | EUR 10,600 above EUR 22,000 × 6.36% | EUR 674.16 before credits; municipal and other charges are separate |
| State scale at EUR 52,100 | EUR 1,994.91 + EUR 12,000 × 20.61% | EUR 4,468.11 before credits |
| Pension additional-tax boundary | Established 2026 pension income after the pension deduction of EUR 60,000 versus EUR 60,100 | Additional component EUR 0 versus EUR 5.85 before annual rounding; the full pension liability remains held |
| Healthcare differential | Confirmed ordinary healthcare base EUR 30,000, daily base EUR 20,000 and qualifying non-excluded income under chapter 18 section 20(3) | EUR 330 ordinary plus EUR 39 additional = EUR 369 unrounded; no flat EUR 447 charge |
| Healthcare supplement exclusions | Daily base equals or exceeds the healthcare base, or the only purported trigger is excluded section 14(2) income | No 0.39% additional component on that basis; verify the ordinary charge separately |
| Separate basic deductions | R = EUR 20,000 after preceding deductions. State: EUR 4,265 − 18% × EUR 15,735. Municipal: EUR 3,925 − 8.4% × EUR 16,075 | State deduction EUR 1,432.70 and base EUR 18,567.30; municipal deduction EUR 2,574.70 and base EUR 17,425.30, before prior losses |
| Public-transport commuting | Eligible costs EUR 2,000, all public transport. State cheapest-method conditions satisfied, no benefit-month relief | State deduction EUR 1,100; regional section 10 exception gives municipal deduction EUR 2,000; neither uses a mileage estimate |
| Work-credit taper plateau | Qualifying income sufficient for the base maximum; net earned income EUR 60,000; no age/child increase | EUR 3,430 − 2% × EUR 15,550 = EUR 3,119; reduction stops at EUR 50,550; allocation still requires each tax |
| Work-credit family maximum | Age 65 before 2026; two minor children, guardian at year-end; no sole-guardian doubling; sufficient qualifying income and net earned income at most EUR 35,000 | Maximum EUR 3,430 + EUR 1,200 + 2 × EUR 105 = EUR 4,840, subject to accrual and available taxes |
| Prospective repeal | Eligible collective supplementary pension contribution paid in 2026; the 2027 repeal is displayed in the source | Test the 2026 section and all its eligibility conditions; the future repeal alone is not a disallowance |
| Unknown municipality | An Åland address is shown but the section 5 municipality evidence is missing | R-AX-I-PROFILE fires; no municipal rate or adjusted state scale is selected |
| Advance division | Ordinary advance EUR 170.01, two instalments, no schedule variation | EUR 85.01 first and EUR 85.00 second; the cent remainder rule does not establish annual tax rounding |
| Advance band boundary | Ordinary in-year total EUR 500 versus EUR 500.01, no variation requested | Two versus three instalments; the upper boundary is inclusive |
| Small advance decision | The authority establishes the tax imposed under section 24 as EUR 9.99 versus EUR 10 | Below EUR 10 is not imposed; at EUR 10 this rule alone does not prevent imposition. A EUR 9.99 balance left from an earlier assessment does not establish the first condition |
| Residual band boundary | Residual principal EUR 169.99 versus EUR 170, no changed assessment | One versus two instalments; the separate non-imposition and interest rules still apply |
| Ordinary increase component | Added income EUR 5,000; reviewer establishes the ordinary 2% branch, no non-imposition ground or other failure | EUR 100, exceeding the EUR 75 individual minimum; no liability or actual penalty decision is certified |
| Ordinary church component | Municipal taxable income EUR 20,000; confirmed 31 December 2025 membership and ordinary Mariehamn geographical parish; no relief or credit yet | Lutheran EUR 310 or Orthodox EUR 350 before credit allocation; unknown membership holds the component |
| Media threshold | Ordinary 2026 resident aged 18 by year-end; no confirmed YEL/MYEL income or foreign relief; state net sum EUR 14,000 versus EUR 14,000.01 | EUR 0 versus fixed EUR 128 under the annual amount rule; commencement discrepancy remains recorded |
| Media insured-income comparison | State net sum EUR 5,900; confirmed YEL EUR 17,000 and no MYEL; ordinary resident age conditions met, no foreign relief | EUR 17,000 is the higher measure, giving the fixed EUR 128 annual fee; a low taxable business profit alone does not remove it |

### Full-ladder example work still required

| Required case | Inputs and schedules to establish | Dependent result held |
|---|---|---|
| Employee | Gross pay/benefits, separate natural deductions, certified contributions, both basic deductions and losses, state/municipal/church/health/media charges, credit allocation, evidenced collection | Final liability, balance and calendar until all applicable bases, rounding and collection rules are verified |
| Self-employed | Accounts and tax adjustments, capital allowances, losses, entrepreneur deduction, valued net assets/wage addition, elected capital share, earned-income deductions, YEL/MYEL substitution, credits and advances | Business allocation and complete personal settlement until source conditions and contribution inputs are verified |
| Mixed salary/business/capital | Both source registers, once-only contribution/expense treatment, entrepreneur share, separate state/municipal/health bases, capital tax, credit ordering and combined collection | Complete liability and balance; a solved salary component cannot certify the mixed result |

## Intake, defaults and reviewer controls

Add fiscal municipality evidence, national residence branch, accounting period,
income categories, church/parish and effective membership dates, health-insurance
route/period evidence, state net amounts and confirmed YEL/MYEL income for the
media comparison, age and guardian/spouse status,
commuting method and qualifying months, pension/contribution certificates,
business net-asset/wage/election schedules, losses, credit evidence and the
authority collection statement to the bases' intake. Use taxpayer references
and redacted evidence; this guide does not require submission of identity,
tax-number or bank-detail records.

| Uncertainty | Permitted preparation treatment |
|---|---|
| Applicable law, year, municipality, residence, insurance or rounding unresolved | Needs Input; hold dependent calculations |
| Deduction expense unsupported, after its legal treatment is established | No deduction provisionally; flag the missing evidence and alternative effect |
| Private/business proportion unsupported | No business deduction provisionally; do not invent a proportion |
| Withholding/payment evidence absent | Do not credit an unverified amount; retain the reconciliation question and any known authority assessment |
| Election or entitlement unresolved | Hold any result that depends on it; no inferred business-share election, spouse transfer or church exemption |
| Specialist receipt, capital asset or foreign item | Separate schedule and verified companion before computation |

Flag every source conflict, refusal, unverified legal condition, election and
potential double count, regardless of amount. The following are review-policy
thresholds, not statutory limits: flag each assumed item's potential effect of
at least EUR 100, or an aggregate at least EUR 250. An effect that cannot be
quantified is a flag, not zero. These thresholds never suppress a legal hold.

## Topical refusal catalogue

Record both universal and topical triggers. Use the exact message for each
fired code; a refusal is not evidence that the underlying tax is zero.

| Code | Trigger | Exact output |
|---|---|---|
| R-AX-I-INCOMPLETE | A required domain slot, source condition or full-ladder example remains incomplete for the requested result | "This Åland income-tax companion is incomplete for the requested calculation. The missing requirements are [list]. I can prepare the source and input issues for the reviewer; the dependent figures and complete financial package remain held." |
| R-AX-I-PROFILE | Tax year, filing unit, national residence or fiscal municipality cannot be established | "I need the applicable tax year, taxpayer/filing unit, residence branch and fiscal home municipality before selecting Åland income-tax rules. The unresolved profile items are [list]." |
| R-AX-I-CROSS-BORDER | Non-resident, part-year, dual-resident, foreign income/account/tax or treaty issue | "This fact pattern needs a verified cross-border companion and the applicable residence, source, treaty and conversion rules. I have held the affected amounts: [list]." |
| R-AX-I-BUSINESS | Business status, period, expenses, valuation, capital allowance, loss or split/election is unverified | "The business-income calculation or earned/capital allocation is not established. Obtain [specific accounts, valuation, election or authority] before computing the affected personal-tax amounts." |
| R-AX-I-CONTRIBUTIONS | Insurance coverage, health base, contributions, church membership or media-fee conditions are unresolved | "The separate contribution, church or media-fee calculation requires [missing evidence or rule]. It cannot be replaced with a flat percentage or an assumed exemption." |
| R-AX-I-ROUNDING | Conversion, intermediate rounding, credit allocation or final money rule is missing | "The required conversion or rounding rule is unverified for [stage]. I have preserved the supported inputs and held the dependent calculation." |
| R-AX-I-SETTLEMENT | Collection, return/date, advance reduction, interest, penalty or residual/refund treatment is unverified | "The filing or settlement position is not established. Reconcile [specific statement, notice or rule] before giving a balance, payment date or client instruction." |
| R-AX-I-SPECIALIST | Estate, partnership return, special pension/maritime/forestry regime, disputed classification or omitted credit mechanics | "This specialist position requires its complete period-specific rules and a qualified review. The unsupported items are [list]; they remain outside this calculation." |

## Completion register and self-check additions

This is the operational acceptance register for this draft, not a claim of
comprehensive coverage. A row marked partial cannot be cleared by guide
presence, a passing linter or an assumed zero.

| Income-tax contract slot | Current support | Requirement still open |
|---|---|---|
| 1. Year, basis, filing unit, residence | Calendar/accounting-period mapping, separate spouse taxation and resident/municipality distinctions | Permitted business accounting basis and specialist taxpayer exceptions |
| 2. Income categories | Earned/capital separation, source schedules, business allocation framework | Complete receipt-specific exemptions, business adjustments and special categories |
| 3. Rates and charges | Adjusted state scale, 16 municipal/church rate rows, ordinary membership and media conditions, capital rates | Special church/health cases, media commencement discrepancy and final bases/credit allocation |
| 4. Deductions and credits | Separate ordinary wage/basic rules and work-credit ordering | Complete specialist/other-credit eligibility, allocation, refundability and spouse rules |
| 5. Expenses and capital | Ordinary wage/home/commuting distinctions | Business deductions, depreciation, valuations and final 2026 mileage decision |
| 6. Losses | Assessed earned/business ten-year carry-forward, oldest first; separate capital-income election route | Full capital-loss, cessation and specialist conditions; personal loss balances |
| 7. Collection and advances | Imposed/paid/reduced advances, ordinary advance bands, residual instalments and interest-period/rate framework | Dated personal estimates/notices, final interest rounding, offsets and complete special cases |
| 8. Contributions | Ordinary insured-residence route, municipal healthcare bridge, YEL/MYEL substitution/exclusion, separate daily base and annual rates | Special/cross-border eligibility, coverage changes, age-transition bases and applicable companion outputs |
| 9. Filing/payment | Return duties, Form 5/17 identities, ordinary instalment/date rules and conditional filing-penalty branches | 2026 form fields, personal notices, complete bank-day calendar, disputed/special penalty and remedy processes |
| 10. Transaction patterns | Source categories and exclusions above | Validate document/statement field maps and remaining receipt patterns |
| 11. Refusals/defaults | Exact catalogue, lawful factual holds and review thresholds | Check against the final content and observable consumer behaviour |
| 12. Currency/rounding | EUR, cent reporting rule and historical precision explanation | Current final rounding/credit allocation and foreign conversion rules |
| 13. Worked examples | Nineteen hypothetical component positions | Employee, self-employed and mixed cases through the full settlement ladder |

Before any eventual financial delivery, run both bases' checks and also verify:

- State, municipal, healthcare, daily-allowance and capital bases have separate
  source trails; a convenient shared number has not replaced a required base.
- Every deduction is on its correct side of net earned income, credit and loss
  ordering. Contributions and business expenses appear once.
- Work-credit accrual, age/child maxima, capped taper and proportional allocation
  use their own bases, with no unused-credit cash refund.
- The municipality, annual rate, membership, age, period and insurance evidence
  match the source year. Prospective repeals and historical examples are excluded.
- Every collection amount reconciles to the authority statement and evidence;
  imposed advances are distinguished from paid cash and later reductions.
- Collection year, tax year and completion month are explicit. The correct
  interest base/period, EUR 20 residual-only reduction, advance/residual bands
  and penalty classification are checked before any balance or calendar.
- Every held figure remains held in the workbook, reviewer brief, calendar,
  action list and review checklist. All mandatory output components must pass.

The reviewer brief must show the two earned-income ladders, contribution bases,
each credit's allocation, the collection reconciliation, source conflicts,
period/election decisions and all open acceptance rows. Add these as mapped
fields to the universal workbook rather than replacing its required columns.

## Sources, revision and limits

The [pack source register](references.md) records retained primary captures and
read limits. Selected provisions and enacted amendments were checked on
16 October 2026 in Australia/Sydney. This editing date does not establish the
complete operative chain for an engagement. Numerical examples are invented
component checks; consumer, full-workbook, portal and professional validation
remain unverified. The guide is Tier 2/pending_review and gives no comprehensive
country-coverage credit.

Version 0.3 adds ordinary church membership and sixteen parish-rate rows,
the ordinary insured-residence test, the personal media-fee comparison and
three component positions. The original media decision's commencement date
remains an explicit source issue. Annual rounding is still unproved.

Version 0.2 adds ordinary advance/residual collection, interest-period rules and
conditional filing penalties. Four additional component positions test
thresholds, division and a classified penalty. Final annual rounding and the
complete settlement examples remain open.

Version 0.1: initial 2026 income reference covering the separate bases, ordinary
deductions, state/municipal schedules, work credit, business-allocation framework
and the remaining operational requirements.

## Disclaimer

This guide is general reference material, not tax, legal or financial advice.
A qualified practitioner must verify the applicable law, facts, calculations
and complete output package before any filing, payment or other reliance.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained in the
[ryanduguid/openaccountants fork](https://github.com/ryanduguid/openaccountants).
Check its quality tier, recorded review status and cited sources before use.
Choose a practitioner whose credentials and engagement scope you have verified.
The links below are optional upstream services; they do not publish or verify
this fork's changes.

- Upstream connection service: https://www.openaccountants.com/connect
- Upstream accountant network: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
