---
name: belarus-income-tax
description: Compute Belarus personal income tax for the 2026 calendar year for resident and nonresident individuals, registered individual entrepreneurs and eligible professional-income taxpayers. Use for Belarus PIT, podokhodny nalog, annual income declarations, the 350000 and 600000 high-income bands, the separate dividend base, documented or deemed business expenses, deductions, private rent, and the professional-income app. The skill distinguishes ordinary agent withholding from annual assessment and the entrepreneur whole-year rate test. It supplies sourced calculation rules, filing and payment procedures and two recomputing examples. Read the payroll and social-contributions skills for gross-to-net and FSZN; use the cross-border skill for treaty restrictions and foreign-tax credits. Tier 2, checked against the law.
version: 0.2
jurisdiction: BY
tax_year: 2026
last_updated: 2026-10-30
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Belarus individual and business income tax, 2026 v0.2

## Who this applies to

Calendar-year 2026, BYN. Individuals resident under General Code art. 17 are taxed on Belarus and foreign-source income; nonresidents on Belarus-source income (Special Code arts. 195-198). Residence means more than 183 days in Belarus, with the statutory temporary-absence rules, prior-year provisional status and treaty tie-breaker. Count from the day after arrival through departure. Citizenship or a residence permit alone does not replace that test; art. 17(5) supplies a fallback where no applicable treaty resolves residence. [General Code art. 17](https://pravo.by/document/?guid=3871&p0=hk0200166); [Special Code arts. 195-198](https://pravo.by/document/?guid=3871&p0=hk0900071).

Before calculating business tax, classify the activity and legal status. From 2026 continuing entrepreneurs must be on the permitted activity list under Council Resolution 457 of 28 June 2024. Professional income is a separate regime for permitted independent professional activities, using the app, rather than an entrepreneur turnover election. Employment income and civil-contract work/service receipts from a current employer, or a former employer that employed the person less than three years ago, are outside that regime (art. 379). The single tax is available only within arts. 335-337; short-stay accommodation by entrepreneurs must use it under art. 336(5). [MNS activity transition](https://nalog.gov.by/news/33527/); [Code arts. 335-337, 378-380](https://pravo.by/document/?guid=3871&p0=hk0900071).

## Rates, bands and thresholds

| Item | Amount | Period | Official act/article |
|---|---|---|---|
| Ordinary individual PIT | 13% | 2026 | [Code art. 214(1.1)](https://pravo.by/document/?guid=3871&p0=hk0900071) |
| Specified Belarus-source high incomes | 25% on excess over BYN 350,000 through 600,000; 30% on excess over 600,000 | 2026 | [Arts. 199(8-2), 214(1.2)-(1.3)](https://pravo.by/document/?guid=3871&p0=hk0900071) |
| Belarus-source dividends, separate base | Ordinary 13%; 25% on excess over BYN 350,000; no 30% dividend band | 2026 | [Arts. 199(8-3), 214(1.2)](https://pravo.by/document/?guid=3871&p0=hk0900071) |
| Qualifying retained-profit dividends to resident individuals | 0% after five consecutive preceding calendar years without distribution to Belarus-resident participants | 2026 | [Art. 214(6)](https://pravo.by/document/?guid=3871&p0=hk0900071) |
| Entrepreneur general system | 20%; 30% for the whole year once business income exceeds BYN 500,000, including specified later receipts for that year | 2026 | [Art. 214(3)](https://pravo.by/document/?guid=3871&p0=hk0900071) |
| Deemed entrepreneur expenses, instead of actual expenses | 30% for exclusively permitted retail and/or transport; 20% for other entrepreneurs | 2026 | [Art. 205(10)](https://pravo.by/document/?guid=3871&p0=hk0900071) |
| Standard personal deduction | BYN 216/month if taxable monthly income is no more than 1,308; entrepreneur quarterly income after art. 205 expenses no more than 3,930 | 2026 | [Art. 209(1.1),(2)](https://pravo.by/document/?guid=3871&p0=hk0900071) |
| Child/dependant deduction | BYN 63/month; BYN 120 for each child for qualifying multiple-child/disabled-child parents and qualifying sole-parent/guardian cases | 2026 | [Art. 209(1.2)](https://pravo.by/document/?guid=3871&p0=hk0900071) |
| Protected-category / qualifying young-specialist deduction | BYN 306 / 860 per month, respectively, subject to status and duration conditions | 2026 | [Art. 209(1.3)-(1.4)](https://pravo.by/document/?guid=3871&p0=hk0900071) |
| Professional-income tax | 10%; 20% only on Belarus-registered business customers' aggregate annual receipts above BYN 60,000 | 2026 | [Art. 381-2(1)](https://pravo.by/document/?guid=3871&p0=hk0900071) |
| Professional-income minimum | No art. 381-6(2) minimum before July; BYN 45/month from July, pension recipient BYN 18 | Jan-Jun / Jul-Dec 2026 | [Arts. 381-3, 381-6; MNS commencement](https://nalog.gov.by/actual/npd_45/) |
| Private domestic gifts exemption | BYN 6,000 aggregate for nonbusiness gifts from individuals in Belarus; foreign transfers have a separate conditional BYN 6,000 exemption | 2026 | [Art. 208(22),(22-2)](https://pravo.by/document/?guid=3871&p0=hk0900071) |
| Taxable property disposal alternative deduction | 20% of taxable proceeds, instead of evidenced acquisition/disposal costs | 2026 | [Art. 211(1.2)](https://pravo.by/document/?guid=3871&p0=hk0900071) |
| Gambling winnings and returned unplayed stakes from Belarus legal-entity gambling organisers | 5%, subject to the exception named in the paragraph | 2026 | [Art. 214(4)](https://pravo.by/document/?guid=3871&p0=hk0900071) |
| Basic unit (bazovaya velichina) used for fines | BYN 45 | From 1 January 2026 | [Council Resolution 651 of 20 November 2025, paras. 1, 3](https://pravo.by/document/?guid=12551&p0=C22500651) |
| Entrepreneur single-tax turnover surcharge | 6% of revenue exceeding 40 times the unrelieved single tax for the reporting period | 2026 | [Art. 342(14)](https://pravo.by/document/?guid=3871&p0=hk0900071) |

Private nonbusiness rent to individuals uses art. 214(2), not a general percentage election. The following monthly BYN rates are per rented room, garden house/dacha, garage or parking space as applicable. The city lists in Annex 2 control classification. [Annex 2, art. 221(1.2)](https://pravo.by/document/?guid=3871&p0=hk0900071); [MNS January and February-December schedules](https://nalog.gov.by/individuals/income_taxation/payment_incom_tax_of_residential_and_non-residential_premises/).

| Location | January: room / metal or wood garage or parking / brick or reinforced-concrete garage | February-December: room / garage / parking |
|---|---|---|
| Minsk | 50 / 16 / 21 | 53 / 22 / 17 |
| Regional capitals and Minsk district | 46 / 13 / 18 | 49 / 19 / 14 |
| The 27 named towns in Annex 2 | 31 / 8 / 12 | 33 / 13 / 9 |
| Other towns and urban settlements | 22 / 6 / 8 | 20 / 8 / 7 |
| Other settlements/territories | 16 / 5 / 6 | 20 / 8 / 7 |

## The base

**Ordinary individuals.** Classify each receipt under arts. 196-203; value in-kind benefits under art. 200. Exclude only an art. 208 exemption whose conditions are documented. Common nonbusiness disposals are exempt under art. 208(44): one of each listed real-estate type in five years and one eligible vehicle per calendar year, with the citizenship/nonresident extension and business-asset exclusions in that paragraph. For an eligible taxable disposal under art. 211(1.2), deduct qualifying evidenced acquisition/disposal costs or the 20% alternative, never both. BYN costs are converted to USD at the National Bank rate on the cost date and back to BYN at the income-receipt-date rate; do not make that conversion if the cost-date BYN/USD rate is higher than the receipt-date rate (retain nominal BYN costs in that case). Costs originally paid in foreign currency are converted at the relevant income-receipt-date rate. Allocate co-owned costs by ownership share and acquisition costs proportionately to instalment proceeds. In nonresident cases assessed under art. 218, paragraph 5 expressly grants the art. 211(1.2) deduction for immovable-property income; do not automatically extend that route to movable-property receipts without checking their own source/agent/classification rules. Securities, company interests and intellectual property need their own classification; do not extend the ordinary personal-property exemption to them. [Arts. 196-203, 208(44), 211(1.2)](https://pravo.by/document/?guid=3871&p0=hk0900071).

Apply art. 209 standard deductions at the main employment/study place. Without one, obtain the written election and supporting documents; only one agent or the tax authority supplies the relevant standard deductions. Entrepreneurs without a main job apply them only for the qualifying months and test the statutory quarterly income limit. Do not multiply the monthly income limit to invent that quarterly figure. Unused standard deductions do not create a negative tax base (art. 199(3)). [Arts. 199(3), 209(2)](https://pravo.by/document/?guid=3871&p0=hk0900071).

Art. 210 allows evidenced qualifying Belarus first higher, secondary-specialist or vocational education costs and qualifying Belarus voluntary insurance, including eligible family expenditure. Qualifying life/additional-pension insurance requires a term of at least three years. Art. 211(1.1) allows evidenced qualifying Belarus home construction/acquisition and related loan repayments for persons registered as needing better housing. Keep the eligibility and payment documents listed in arts. 210-211; carry unused qualifying social/housing deductions forward under those articles, without also deducting a reimbursement. The young-specialist deduction requires the specified placement/service documents and employment continuity conditions in art. 209(1.4); age alone is insufficient. [Arts. 209-211](https://pravo.by/document/?guid=3871&p0=hk0900071).

**High income.** Aggregate only the Belarus-source items listed in art. 199(8-2), including employment, taxable employer compensation, civil-contract work/services/IP, loan interest to agents, rent and board fees; exclude the paragraph's stated items. Dividends form the separate art. 199(8-3) base. Apply ordinary taxation below the thresholds, then assess the excess at the higher rates and credit tax already imposed on that excess under art. 219(1.9). Do not assess the higher tax again on the first band or pool dividends with wages. Deductions/exemptions in arts. 208-212 cannot reduce the excess above the high-income threshold. Foreign income is not automatically part of this specified Belarus-source pool. [Arts. 199(8-2)-(8-3), 214, 219(1.9)](https://pravo.by/document/?guid=3871&p0=hk0900071).

**Entrepreneurs.** Assemble business revenue and other business income under art. 205 and receipt dates under art. 213, including statutory treatment of advances, barter, third-party payments and discontinued-business receipts. Choose evidenced business costs or the deemed-cost election, documented in writing for the year. Do not combine the two. Actual expenses follow art. 205: match stock, depreciate qualifying capital assets, exclude private costs, capital acquisition costs already recovered by depreciation, tax penalties and costs of exempt/special-regime income. Expenses cannot generally exceed period income; art. 205(11) specifically carries qualifying registration, bank-opening, rent/utilities and licensing excess costs until used. Do not apply corporate loss rules. Calculate the cumulative base, allowable personal deductions, the whole-year rate and subtract earlier instalments. [Arts. 199, 205, 213-214, 217](https://pravo.by/document/?guid=3871&p0=hk0900071).

**Professional income.** First test the art. 379 object: Belarus citizens can include Belarus-source and foreign-source professional income; other eligible taxpayers can include Belarus-source professional income and the specified Belarus-located property income, with foreign-source professional receipts outside this object. A foreign customer alone does not settle income source. Exclude current-employer and less-than-three-years former-employer civil-contract work/service receipts. Art. 379 also excludes separately charged tenant utility/service reimbursements where the contract requires reimbursement outside rent, and buyer delivery reimbursements outside the goods price. Then tax eligible receipts without business-expense deductions, tracking Belarus business-customer income separately from individuals and foreign customers. Form app receipts for each settlement; refund/correction rules are in art. 381-1. The pension exemption removes the social-insurance component, leaving 4%/8% effective rates, rather than an across-the-board 8%. From July compare the monthly result with the applicable minimum even in a zero-receipt month while registered. The former first-user BYN 2,000 deduction ended on 1 January 2026. [Arts. 381-1 through 381-7](https://pravo.by/document/?guid=3871&p0=hk0900071); [FSZN Law art. 16-1](https://pravo.by/document/?guid=3871&p0=H12100118); [MNS 2026 changes](https://nalog.gov.by/clarifications/comments/33519/).

**Single-tax route.** Check the closed activity/customer list in arts. 335-337: no general B2B or commission/distance-goods election. The monthly entrepreneur schedule below uses location columns A Minsk; B Brest/Vitebsk/Gomel/Grodno/Mogilev and Minsk district; C the 16 Annex 24 towns; D other settlements. Product exclusions in art. 336 still apply. C comprises Baranovichi, Bobruisk, Borisov, Zhlobin, Zhodino, Lida, Mozyr, Molodechno, Novopolotsk, Orsha, Pinsk, Polotsk, Rechitsa, Svetlogorsk, Slutsk and Soligorsk. [Arts. 335-339 and Annex 24](https://pravo.by/document/?guid=3871&p0=hk0900071).

| Entrepreneur activity | January A/B/C/D, BYN | February-December A/B/C/D, BYN | Enacted source |
|---|---|---|---|
| Each short-stay property | 703 / 655 / 344 / 305 | 750 / 699 / 367 / 325 | [47-Z art. 1(191), pp. 98-99](https://pravo.by/upload/docs/op/H12400047_1734642000.pdf); [127-Z art. 2(183), p. 79 and art. 4(5), pp. 87-88](https://pravo.by/upload/docs/op/H12500127_1767214800.pdf) |
| Bread/bakery and milk/dairy retail | 798 / 487 / 319 / 266 | 851 / 520 / 340 / 284 | [47-Z art. 1(191)](https://pravo.by/upload/docs/op/H12400047_1734642000.pdf); [127-Z arts. 2(183), 4(5)](https://pravo.by/upload/docs/op/H12500127_1767214800.pdf) |
| Vegetable/fruit/berry/melon/grape retail | 802 / 603 / 422 / 311 | 856 / 643 / 450 / 332 | [47-Z art. 1(191)](https://pravo.by/upload/docs/op/H12400047_1734642000.pdf); [127-Z arts. 2(183), 4(5)](https://pravo.by/upload/docs/op/H12500127_1767214800.pdf) |
| Other qualifying food retail | 1242 / 764 / 530 / 496 | 1325 / 815 / 566 / 529 | [47-Z art. 1(191)](https://pravo.by/upload/docs/op/H12400047_1734642000.pdf); [127-Z arts. 2(183), 4(5)](https://pravo.by/upload/docs/op/H12500127_1767214800.pdf) |
| Qualifying nonfood retail | 1645 / 1020 / 724 / 656 | 1755 / 1088 / 773 / 700 | [47-Z art. 1(191)](https://pravo.by/upload/docs/op/H12400047_1734642000.pdf); [127-Z arts. 2(183), 4(5)](https://pravo.by/upload/docs/op/H12500127_1767214800.pdf) |
| Construction | 800 / 700 / 550 / 550 | 800 / 700 / 550 / 550 | [127-Z arts. 2(183), 4(5)](https://pravo.by/upload/docs/op/H12500127_1767214800.pdf) |
| Taxi | 400 / 350 / 300 / 300 | 400 / 350 / 300 / 300 | [127-Z arts. 2(183), 4(5)](https://pravo.by/upload/docs/op/H12500127_1767214800.pdf) |

The new schedule applies where the statutory payment deadline falls after 30 January; January continuing activities retain the former schedule, while newly eligible construction/taxi use the new one. January-only eligible retail for fewer than 15 days at a trading place, exhibition/sale, fair or itinerant/peddling trade uses coefficient 0.5. It does not continue from February. Initial construction/taxi elections from January require the Q1 return by 31 January and January payment by 1 February, subject to General Code art. 4 nonworking-day adjustment. [127-Z art. 4(5)](https://pravo.by/upload/docs/op/H12500127_1767214800.pdf); [MNS transition](https://nalog.gov.by/clarifications/clarifications/33616/).

For each month, charge each trading object/place separately, subject to art. 342(5)'s precise no-other-persons trading-place/itinerant exception. Use the highest product rate for mixed retail. Several other services use the highest service rate, but add a separate charge for each short-stay property. Taxi uses tax-registration location; other activities use activity location. Keep shipment/performance revenue and other income under art. 342(15)-(25); unassigned mixed-regime other income follows the revenue-share allocation. [Art. 342(1)-(25)](https://pravo.by/document/?guid=3871&p0=hk0900071).

Art. 340 reduces tax 25% for the first three months beginning with first business activity; 20% for qualifying pension, disability, three-or-more minor children or disabled-child grounds; multiple simultaneous grounds within (1.1)-(1.5) give a total 45% reduction. The specified group I/II disabled-parent and spouse conditions in (1.6) give 100%. Obtain the exact status documents and apply the statutory month boundaries. Entrepreneurs choose one object/place/activity for relief, not every unit. Ordinary individuals' relief rules differ and exclude their short-stay activity. Sum the fixed charges after eligible relief; surcharge is `6% × max(0, quarter revenue − 40 × quarter fixed tax BEFORE relief)`. Supported art. 344 absence grounds require application/evidence for proration, `monthly charge × active days / calendar days`; there is no unrestricted part-month election. [Arts. 340, 342(14),(30), 344](https://pravo.by/document/?guid=3871&p0=hk0900071).

**Rent.** Multiply the monthly rate by taxable units and prorate first/last partial months by days under art. 221(2). Under art. 221(3), a 10% supplementary assessment applies to stated rental income exceeding ten times fixed PIT paid for the relevant period when that income is given in the specified income/expenditure-check explanations. It is not an automatic annual rent surtax. Renting to a business is outside the private fixed-rent rule. [Arts. 214(2), 221](https://pravo.by/document/?guid=3871&p0=hk0900071).

## Deadlines and filing

| Obligation | Rule | Official source |
|---|---|---|
| Resident annual individual declaration | By 31 March 2027 for 2026 art. 219 income, including foreign-source and high-income cases; attach deduction/credit evidence | [Arts. 219, 222](https://pravo.by/document/?guid=3871&p0=hk0900071) |
| Assessed annual PIT | Authority notice by 30 April; payment by 1 June of following year | [Art. 219(2)](https://pravo.by/document/?guid=3871&p0=hk0900071) |
| Entrepreneur return/payment | Cumulative quarter, half-year, nine months, year; return by 20th and payment by 22nd of following month, including January for the final quarter | [Arts. 207, 217](https://pravo.by/document/?guid=3871&p0=hk0900071) |
| Professional-income app | Install and notify before using regime; authority notification by 10th, payment by 22nd of following month; no conventional annual return for this regime | [Arts. 381, 381-4, 381-7](https://pravo.by/document/?guid=3871&p0=hk0900071) |
| Fixed private rent | Register the written rental agreement before occupation; first/new extension payment by next working day after contractual provision, then by first day of paid month | [Art. 221; MNS procedure](https://nalog.gov.by/individuals/income_taxation/payment_incom_tax_of_residential_and_non-residential_premises/) |
| Entrepreneur single tax | Return by first day of quarter; payment by first day of each month; first annual start by working day before activity; amend changed conditions before change | [Arts. 341-343](https://pravo.by/document/?guid=3871&p0=hk0900071) |
| Single-tax surcharge, both return and payment | Q1/Q2/Q3/Q4: 1 July / 1 October / 1 January / 1 April, including after exit | [Arts. 342(27), 343(3)](https://pravo.by/document/?guid=3871&p0=hk0900071) |

Use the tax inspectorate or MNS personal cabinet for individual declarations; entrepreneur electronic filing follows General Code art. 40. Apply General Code art. 4 to nonworking-day tax deadlines, rather than assuming contribution payment dates follow the same convention. [General Code arts. 4, 28, 40](https://pravo.by/document/?guid=3871&p0=hk0200166).

## Penalties and interest

Late-payment interest under General Tax Code art. 55 is computed separately for each period of constant unpaid tax and National Bank refinancing rate: `unpaid tax × overdue calendar days × annual rate / 360 / 100`. Count from the day after the due date through payment; interest reflected in the audit decision on audit-assessed tax is capped at that assessed tax amount; apply art. 55(3) exclusions and art. 55(4)'s four-decimal interest-rate precision. Use the rate actually in force in each period, not a single assumed 2026 rate. [General Code art. 55](https://pravo.by/document/?guid=3871&p0=hk0200166).

For an ordinary individual with tax payable and a return more than 30 working days late, Administrative Code art. 14.2(3) sets 0.5 basic unit plus 0.5 per complete month, capped at 10. Negligent ordinary-individual underpayment above one basic unit carries 15%, minimum 0.5 basic unit under art. 14.4(6); intentional cases use art. 14.4(8), 40%, minimum 10 basic units. Apply the statutory exclusions and correction rules before estimating a fine. For a business/agent return, Administrative Code art. 14.2(1)-(2) sets up to 1 basic unit for no more than 3 working days late; otherwise 2 basic units plus 0.5 per complete month, capped at 10. Repetition within a year invokes art. 14.2(4), 3 per complete or incomplete month, capped at 20. Under art. 14.4(1), business tax underpayment carries 40% of unpaid tax, minimum 2 basic units for an entrepreneur or 10 for a company, subject to the statutory notes, including timely voluntary correction/payment. Do not apply these amounts automatically to an ordinary individual or to a withholding default. [Administrative Code arts. 14.2 and 14.4](https://pravo.by/document/?guid=3871&p0=hk2100091).

Unregistered prohibited business income and the other specified art. 214(7) cases use 26%, distinct from an administrative fine. Unreceipted/late-receipted professional income uses 20% without the pension relief (art. 381-2(2)); from July repeated nonpayment three times triggers authority deregistration and the art. 381(4) re-entry rule. [Arts. 214(7), 381, 381-2](https://pravo.by/document/?guid=3871&p0=hk0900071).

## Cross-border points

Convert foreign receipts at the National Bank rate on actual receipt, with the specific monthly employment and entrepreneur-advance rules in art. 199(11). Resident foreign-tax credits are calculated income by income, limited to Belarus tax on that income, with the art. 224 evidence and offshore exception; entrepreneur credits use art. 224(3). Read `belarus-cross-border-tax` before applying a treaty. [Arts. 199(11), 224](https://pravo.by/document/?guid=3871&p0=hk0900071).

Nonresident art. 218 cases require a declaration of expected Belarus income before the activity/disposal/rental starts and advance payment, with real-estate tax payable within five working days after notice; actual-income reconciliation and additional payment also have five-working-day rules. Belarus citizens departing permanently must file and pay the art. 222(5) departure assessment, within 15 calendar days of notice and no later than departure. Agent withholding alone does not remove the annual high-income declaration obligation. [Arts. 214(1.2)-(1.3), 218, 222(5)](https://pravo.by/document/?guid=3871&p0=hk0900071).

## Two worked examples that recompute

### 1. Entrepreneur with documented expenses

A permitted general-system entrepreneur receives BYN 120,000 and has BYN 40,000 of deductible current costs. All amounts follow art. 205, no personal deductions apply, and the business-income threshold is not exceeded. The base is 80,000; PIT is 16,000. FSZN is computed separately.

```oa-check
name: BY 2026 ordinary entrepreneur actual expenses
inputs:
  income: 120000
  deductible_costs: 40000
steps:
  base: max(0, income - deductible_costs)
  tax: base * 0.20
expected:
  base: 80000
  tax: 16000
```

### 2. Annual high-income wage assessment

A resident has BYN 700,000 of taxable Belarus wages included in art. 199(8-2), no deductions and no dividends. The first 350,000 bears 13%, the next 250,000 bears 25%, and the remaining 100,000 bears 30%. Total PIT is 138,000. With 91,000 already withheld at 13% on all wages, the additional annual assessment is 47,000.

```oa-check
name: BY 2026 separate high-income wage bands
inputs:
  wages: 700000
steps:
  ordinary: min(wages, 350000) * 0.13
  middle: max(0, min(wages, 600000) - 350000) * 0.25
  upper: max(0, wages - 600000) * 0.30
  total: ordinary + middle + upper
  withheld: wages * 0.13
  balance: total - withheld
expected:
  total: 138000
  balance: 47000
```

## Ask the client first

- Where were you each day, and which temporary absences, citizenship/permanent residence and treaty residence facts apply?
- For each receipt, who paid, where is the source, when was it earned/received, and what tax was withheld?
- Which main job, children/dependants, protected status, education, insurance or housing deductions are evidenced?
- Is the activity on the permitted list, which regime was elected, and are business receipts approaching the entrepreneur threshold?
- Are there private rental units, property disposals, foreign taxes or a permanent departure?
- For professional income, what are the customer classes, app receipts, pension status and registration months?

## Sources

| Source and read scope | Official URL | Read on |
|---|---|---|
| Law 47-Z of 13 December 2024, art. 1(191), PDF pp. 98-99, retained January rates | https://pravo.by/upload/docs/op/H12400047_1734642000.pdf | 2026-10-24 |
| Law 127-Z of 30 December 2025, arts. 2(183), 4(5), 6, PDF pp. 79, 87-89 | https://pravo.by/upload/docs/op/H12500127_1767214800.pdf | 2026-10-24 |
| MNS January single-tax transition | https://nalog.gov.by/clarifications/clarifications/33616/ | 2026-10-24 |
| Tax Code Special Part, arts. 195-224, 335-344, 378-381-7 and Annexes 2/24 | https://pravo.by/document/?guid=3871&p0=hk0900071 | 2026-10-24 |
| Tax Code General Part, arts. 4, 17, 28, 40, 55 | https://pravo.by/document/?guid=3871&p0=hk0200166 | 2026-10-24 |
| Administrative Code, arts. 14.2-14.5 | https://pravo.by/document/?guid=3871&p0=hk2100091 | 2026-10-24 |
| FSZN Law 118-Z, art. 16-1 | https://pravo.by/document/?guid=3871&p0=H12100118 | 2026-10-24 |
| MNS private-rent January and February-December 2026 schedules and procedure | https://nalog.gov.by/individuals/income_taxation/payment_incom_tax_of_residential_and_non-residential_premises/ | 2026-10-24 |
| MNS professional-income 2026 changes | https://nalog.gov.by/clarifications/comments/33519/ | 2026-10-24 |
| MNS professional-income minimum commencement | https://nalog.gov.by/actual/npd_45/ | 2026-10-24 |
| MNS entrepreneur permitted-activity transition | https://nalog.gov.by/news/33527/ | 2026-10-24 |
| Council Resolution 651 of 20 November 2025, paras. 1, 3, official PDF, basic unit BYN 45 from 1 January 2026 | https://pravo.by/document/?guid=12551&p0=C22500651 | 2026-10-31 |

Pravo consolidated HTML was read in a normal browser after scripted access returned HTTP 403. Published PDFs were read in the official browser PDF viewer. Checked against the law (tier 2); no licensed Belarusian accountant has signed it off.

Not yet confirmed: No unresolved ordinary general-system, professional-income or entrepreneur single-tax computation is identified within the stated scope. Specialist crypto, HTP, craft and agro-tourism regimes and ordinary non-entrepreneur single-tax activity schedules are excluded, rather than inferred to be tax-free.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
