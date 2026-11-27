---
name: pt-social-contributions
description: "Portuguese social security contributions for 2026: self-employed coverage, 21.4% and 25.2% rates, quarterly relevant income, employment exemptions, organised accounts and contracting entities; employee and MOE headline rates, filing, penalties and interest. Trigger on Segurança Social independente, declaração trimestral, recibos verdes, entidade contratante, MOE gerente and TSU. Establish start/restart dates, income type, accounting regime, other cover and customer concentration first. Minimum-charge conflicts and specialist cases carry explicit non-usable partner referrals."
version: 2.4
jurisdiction: PT
tax_year: 2026
last_updated: 2026-11-27
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: payroll
type: computation
---

# Portugal: social security contributions (tax year 2026)

For an established self-employed worker in the quarterly regime, calculate relevant income from the previous quarter, divide by three, apply the permitted option and ceiling, then the applicable rate. Employment alongside self-employment has a separate excess-only calculation. The rates and conditions below govern; a referral hold prevents a final answer on that point.

Related Guides: `portugal-payroll` for pay components, IRS withholding, net pay and employer cost; `pt-income-tax` for annual IRS; `pt-cross-border` for residence and applicable-country analysis. Those links do not resolve a hold here.

**Required inputs:** first activity and restart dates; actual service/goods income by quarter and year; hotel/restaurant classification; organised accounts and the assessment notice; ENI/EIRL status; working spouse/partner; employment pay, employer group and protection; pensions; each customer's annual share; paid/unpaid MOE duties. Obtain these from the records before calculating. Refuse a final figure where a material input or the applicable coverage is missing. Check this point with one of our partner accountants.

## Who this applies to

**Self-employed scope.** People working on their own account outside an employment/equivalent contract and not covered for that activity as employees are covered, including professional-society members, qualifying agricultural operators, ENI/EIRL holders and spouses/qualifying unmarried partners working regularly and permanently with them (Code arts. 132–134). Source: https://diariodarepublica.pt/dr/legislacao-consolidada/lei/2009-34514575.

**Exclusions.** Code art. 139 excludes lawyers/solicitadores compulsorily in their professional fund; temporary workers proving compulsory foreign protection including invalidity, old age and death, subject to international instruments; predominantly own-consumption farms with annual activity income no more than four IAS; PAC-only farmers below four IAS with no other income bringing them into the regime; specified local/coastal fishing-boat crew owners, marine harvesters and shore fishers; Category B income exclusively from qualifying renewable electricity or house/apartment rental/local lodging. Four IAS is EUR 2,148.52 in 2026. Farm exclusions use RV 1027. RV 1025 is the temporary-Portugal exclusion application for nationals of a country with no applicable international social-security instrument; do not use it as a universal EU/A1 form. Sources: https://diariodarepublica.pt/dr/legislacao-consolidada/lei/2009-34514575, art. 139; https://www.seg-social.pt/ptss/pssd/documento/cmc1xyfxz00dekl2ynxz676sw, p. 6; https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/diplomas_legislativos/Documents/Portaria_480_A_2025_1.pdf, art. 2.

**Same employer/group.** Employment plus independent work for the same employer/group uses the employee regime: gross fees are the base and the employment-contract rate applies (arts. 129–131). For MOE plus independent work for the same entity/group, the ISS guide also directs the fees to the MOE rate. Establish the actual classification first. Sources: https://diariodarepublica.pt/dr/legislacao-consolidada/lei/2009-34514575; https://www.seg-social.pt/ptss/pssd/documento/cmc1xyfxz00dekl2ynxz676sw, p. 6.

**Start, restart and stop.** AT communicates the start and Segurança Social registers/enrols the worker, including when exempt (arts. 143–144). First cover starts on the first day of the twelfth month after the start month: January 2026 start means 1 January 2027. Cessation in the initial period suspends the count, resumed on the first day of restart if within twelve months of cessation. Otherwise an ordinary restart takes effect on the first day of its month. Voluntary early cover is requested at a quarterly declaration window and starts on the first day of the following month (art. 146(2), Regulation art. 57-A); the ISS guide contains inconsistent same-month wording, which must not override the Code. After cessation, cover/contribution duty ends from the next month, without cancelling annual-review liabilities (arts. 148, 161). Sources: https://diariodarepublica.pt/dr/legislacao-consolidada/lei/2009-34514575; https://diariodarepublica.pt/dr/legislacao-consolidada/decreto-regulamentar/2011-56720826.

**Exemptions while covered.** Under art. 157:

- Employment exemption requires different employers with no control/group relationship; compulsory other protection covering every contingency of this regime; average monthly pay for that regime at least one IAS; and average monthly relevant independent income below four IAS. Regulation art. 59 uses average pay in the preceding quarter. At or above four IAS, art. 163(4) charges only the excess, without the 25% option.
- National or foreign invalidity/old-age pension: work must be legally compatible with the pension. Occupational-risk pension: incapacity at least 70%.
- January recognition following a prior year of minimum-charge liability under art. 163(2), while those circumstances continue. The minimum amount itself is held below.

Recognition is automatic if Segurança Social knows the conditions; otherwise apply, using RC 3001 for the employment case. Automatic exemption normally takes effect the month after the facts, requested exemption the month after application; pension exemption starts at pension award (Regulation art. 60). Do not assume an exemption already operates in the month a condition first arises. Sources: https://diariodarepublica.pt/dr/legislacao-consolidada/lei/2009-34514575, art. 157; https://diariodarepublica.pt/dr/legislacao-consolidada/decreto-regulamentar/2011-56720826, arts. 59–60; https://www.seg-social.pt/ptss/pssd/documento/cmc1xyfxz00dekl2ynxz676sw, pp. 9–10.

**Employees and MOE.** Establish coverage/exclusions before applying the table. Unpaid MOE of a for-profit entity are excluded where another compulsory activity yields income strictly above one IAS, or they are invalidity/old-age pensioners of compulsory national/foreign protection (art. 64). Payroll components are handled in `portugal-payroll`. Source: https://diariodarepublica.pt/dr/legislacao-consolidada/lei/2009-34514575, arts. 61–69.

**Contracting entities.** Legal persons and business individuals buying more than 50% of the worker's total annual activity are covered, grouping companies in the same business group. The worker must be liable to contribute and have annual service income at least six IAS (EUR 3,222.78 in 2026). Art. 140-A extends the determination to ENI/EIRL activity. Sources: https://diariodarepublica.pt/dr/legislacao-consolidada/lei/2009-34514575, arts. 140–140-A; https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/diplomas_legislativos/Documents/Portaria_480_A_2025_1.pdf.

## Rates, bands and thresholds

All amounts below are 2026 unless expressly marked historical.

| Item and operative condition | Rate or amount | Official source |
|---|---|---|
| IAS | EUR 537.13; four IAS EUR 2,148.52; six IAS EUR 3,222.78 | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/diplomas_legislativos/Documents/Portaria_480_A_2025_1.pdf, art. 2 |
| Ordinary self-employed, including qualifying agricultural workers | 21.4% | https://diariodarepublica.pt/dr/legislacao-consolidada/lei/2009-34514575, art. 168(1) |
| ENI/EIRL holder and respective spouse | 25.2%; employees are not a prerequisite for this rate | https://diariodarepublica.pt/dr/legislacao-consolidada/lei/2009-34514575, art. 168(4) |
| Relevant income, services | 70% of prior-quarter services | https://diariodarepublica.pt/dr/legislacao-consolidada/lei/2009-34514575, art. 162(1)(a) |
| Relevant income, goods; hotel/similar, restaurant and drinks services declared as such for tax | 20% | https://diariodarepublica.pt/dr/legislacao-consolidada/lei/2009-34514575, art. 162(1)(b), (2) |
| Monthly quarterly-regime base | One third of relevant income; declaration month and next two months | https://diariodarepublica.pt/dr/legislacao-consolidada/lei/2009-34514575, art. 163(1) |
| Base option at the quarterly declaration | Up/down to 25%, in 5% steps, subject to limits; unavailable for employment excess base | https://diariodarepublica.pt/dr/legislacao-consolidada/lei/2009-34514575, arts. 163(4), 164(1)–(2) |
| Monthly base ceiling | Twelve IAS = EUR 6,445.56 | https://diariodarepublica.pt/dr/legislacao-consolidada/lei/2009-34514575, art. 163(5); https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/diplomas_legislativos/Documents/Portaria_480_A_2025_1.pdf |
| Organised accounts, once taxable-profit assessment applies | One twelfth of prior-year taxable profit; floor 1.5 IAS = EUR 805.695 before cent rounding (EUR 805.70); ceiling as above | https://diariodarepublica.pt/dr/legislacao-consolidada/lei/2009-34514575, arts. 162(3), 163(3), (5); https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/diplomas_legislativos/Documents/Portaria_480_A_2025_1.pdf |
| Contracting entity: dependency over 80% | 10% of annual services supplied to it | https://diariodarepublica.pt/dr/legislacao-consolidada/lei/2009-34514575, arts. 167, 168(7)(a) |
| Contracting entity: dependency over 50% through 80% | 7% of those services | https://diariodarepublica.pt/dr/legislacao-consolidada/lei/2009-34514575, arts. 140, 167, 168(7)(b) |
| General employee regime, subject to special classification | Total 34.75%: employer 23.75%, employee 11% | https://diariodarepublica.pt/dr/legislacao-consolidada/lei/2009-34514575, art. 53 |
| Covered MOE with management/administration duties | Total 34.75%: entity 23.75%, member 11% | https://diariodarepublica.pt/dr/legislacao-consolidada/lei/2009-34514575, art. 69(2) |
| Other covered MOE | Total 29.6%: entity 20.3%, member 9.3% | https://diariodarepublica.pt/dr/legislacao-consolidada/lei/2009-34514575, art. 69(1) |
| MOE base, each entity | Actual remuneration, at least one IAS; minimum waived for other covered remunerated activity or pension with other base/pension at least IAS | https://diariodarepublica.pt/dr/legislacao-consolidada/lei/2009-34514575, art. 66 |
| Qualifying nonprofit employer, full contingency cover; public entities/services excluded | Total 33.3%: employer 22.3%, employee 11% | https://diariodarepublica.pt/dr/legislacao-consolidada/lei/2009-34514575, arts. 110–112 |
| Disability incentive: indefinite contract and work capacity below 80% of normal for that job; employer application with statutory certificate required | Total 22.9%: employer 11.9%, employee 11% | https://diariodarepublica.pt/dr/legislacao-consolidada/lei/2009-34514575, arts. 108–109; https://diariodarepublica.pt/dr/legislacao-consolidada/decreto-regulamentar/2011-56720826, art. 48 |
| Employment-excess de minimis | Ignore an excess-income amount yielding contribution below EUR 5; do not apply the ordinary minimum to it | https://diariodarepublica.pt/dr/legislacao-consolidada/decreto-regulamentar/2011-56720826, art. 59(5); https://files.diariodarepublica.pt/2s/2019/01/008000000/0152401524.pdf, Despacho 599/2019(1); https://www.seg-social.pt/ptss/pssd/documento/cmc1xyfxz00dekl2ynxz676sw, p. 16 |
| Late interest | Annual general rate 7.221% from 1 January; Code charges by calendar month or part | https://diariodarepublica.pt/dr/legislacao-consolidada/lei/2009-34514575, arts. 211–212; https://diariodarepublica.pt/dr/detalhe/aviso/18-2026-993315668 |

**Minimum-charge hold (non-usable).** Art. 163(2) prints EUR 20, but art. 163(8) requires IAS-linked updating; the January 2026 ISS guide still uses EUR 20. No operative reconciliation of that conflict was established. Do not issue a current minimum-charge figure, apply an automatic EUR 20 floor, or compute a first/restart interim charge from it. Check this point with one of our partner accountants. Sources: https://diariodarepublica.pt/dr/legislacao-consolidada/lei/2009-34514575, art. 163(2), (8); https://www.seg-social.pt/ptss/pssd/documento/cmc1xyfxz00dekl2ynxz676sw, pp. 7, 16–17.

**Special-rate holds (non-usable).** Domestic workers, professional sportspeople, very short contracts, pensioners in work, rural/maritime workers, and first-job/long-term-unemployment incentives require their own coverage, base and eligibility determinations. Do not apply a headline special rate from this Guide to those cases. Check this point with one of our partner accountants.

## The taxable base

**Quarterly calculation.** Separate services from goods/qualifying hotel and restaurant income, apply the factors in the table, then divide by three. For ordinary workers apply an elected permitted percentage and the ceiling; multiply by the correct rate. For qualifying employment alongside the activity, use only the amount above four IAS, with no percentage option and the separate de minimis. Establish exemption effective dates first. A case dependent on the minimum-charge hold cannot yield a final contribution. Sources: https://diariodarepublica.pt/dr/legislacao-consolidada/lei/2009-34514575, arts. 157, 162–164; https://diariodarepublica.pt/dr/legislacao-consolidada/decreto-regulamentar/2011-56720826, arts. 59–60.

**Excluded income.** Renewable-electricity and house/apartment rental/local-lodging income do not enter relevant income. Investment grants/subsidies, capital gains and intellectual/industrial-property income are excluded unless opted in; when included, use the originating activity's treatment. This exclusion is separate from excluding a person with exclusively such income. Source: https://diariodarepublica.pt/dr/legislacao-consolidada/decreto-regulamentar/2011-56720826, art. 62.

**Organised accounts.** Use taxable profit of the immediately preceding calendar year, not quarterly net profit. The monthly base is fixed in October for the next calendar year. No quarterly declaration while relevant income is assessed on taxable profit; the notice's deadline controls an election into quarterly assessment from January (ISS describes 1–30 November). At start/restart, use the quarterly method until Segurança Social knows the relevant IRS declaration. Sources: https://diariodarepublica.pt/dr/legislacao-consolidada/lei/2009-34514575, arts. 151-A(7), 162(3), 163(3), 164(3); https://diariodarepublica.pt/dr/legislacao-consolidada/decreto-regulamentar/2011-56720826, arts. 57-C–57-D; https://www.seg-social.pt/ptss/pssd/documento/cmc1xyfxz00dekl2ynxz676sw, p. 14.

**Working spouses/partners (non-usable calculation hold).** Preserve this route separately from the worker's own calculation. The spouse assessment, adjustment election and continuation/fallback rules when the worker is exempt require an individual determination; do not simply multiply quarterly income by a percentage and report a monthly charge. Check this point with one of our partner accountants.

**Contracting entity.** Apply its rate to the full annual services supplied to it, not to the worker's 70% relevant income. This is the entity's own contribution and does not replace the worker's liability. Source: https://diariodarepublica.pt/dr/legislacao-consolidada/lei/2009-34514575, arts. 154, 167–168.

**IRS.** For simplified-regime income under CIRS art. 31(1)(b)/(c), compulsory contributions connected with the activity and evidenced as borne are deductible after the coefficient, up to that net income, only to the extent above 10% of gross income and not deducted elsewhere. For the 15% expense test, contributions not deductible that way can enter art. 31(13)(a) when above the specific deduction. Do not deduct every contribution automatically or twice. Source: https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs31.aspx, arts. 31(2), (13)(a).

## Deadlines and filing

| Obligation | Timing and conditions | Official source |
|---|---|---|
| Quarterly declaration | Last day of January, April, July and October for preceding three months; next working day if weekend/holiday; submit electronically and retain successful submission | https://diariodarepublica.pt/dr/legislacao-consolidada/lei/2009-34514575, art. 151-A(1)–(4); https://diariodarepublica.pt/dr/legislacao-consolidada/decreto-regulamentar/2011-56720826, art. 57-B |
| Correction | Last declaration in declaration month counts; substitution also allowed through fifteenth day after deadline | https://diariodarepublica.pt/dr/legislacao-consolidada/decreto-regulamentar/2011-56720826, art. 57-B(2)–(3) |
| Late online declaration | From next day after filing period through last day of month before next filing period; remains late and cannot anticipate cover | https://www.seg-social.pt/ptss/pssd/documento/cmc1xyfxz00dekl2ynxz676sw, p. 13 |
| January confirmation/correction | Previous calendar year, where at least one quarterly declaration was required; pension exceptions in art. 151-A(6), taxable-profit exclusion in (7) | https://diariodarepublica.pt/dr/legislacao-consolidada/lei/2009-34514575, art. 151-A(5)–(7); https://diariodarepublica.pt/dr/legislacao-consolidada/decreto-regulamentar/2011-56720826, art. 57-B(4) |
| Stop/suspend activity | File in immediately following declaration window | https://diariodarepublica.pt/dr/legislacao-consolidada/lei/2009-34514575, art. 151-A(4) |
| Annual activity/customer details | Anexo SS to IRS Modelo 3 at the applicable IRS filing deadline; identify service purchasers and values as required | https://diariodarepublica.pt/dr/legislacao-consolidada/lei/2009-34514575, art. 152; https://diariodarepublica.pt/dr/legislacao-consolidada/decreto-regulamentar/2011-56720826, art. 58 |
| Self-employed payment | Monthly, days 10–20 of following month | https://diariodarepublica.pt/dr/legislacao-consolidada/lei/2009-34514575, art. 155(2) |
| Contracting-entity payment | Prior calendar year's liability; by day 20 of month following issue of collection document | https://diariodarepublica.pt/dr/legislacao-consolidada/lei/2009-34514575, art. 155(3) |
| Employer new model | Confirm by day 20 of following month; silence accepts system figures; August acceptance/confirmation extended to day 25 | https://diariodarepublica.pt/dr/detalhe/decreto-lei/127-2025-967317021, art. 2 (Code arts. 23-B, 40) |
| Employer payment | Code art. 43 as amended: monthly, days 1–25 of following month using Segurança Social data | https://diariodarepublica.pt/dr/detalhe/decreto-lei/127-2025-967317021, arts. 2, 6 |
| Employer transition | Request during 2026; services confirm eligibility; effect month after that confirmation, with old-model declarations then rejected; mandatory from 1 January 2027 | https://diariodarepublica.pt/dr/detalhe/decreto-lei/127-2025-967317021, art. 5 |

Employment/pension exemptions under art. 157(1)(a)–(c) and taxable-profit assessment have the quarterly-declaration exceptions described in the ISS guide; do not extend them to the January duty without checking the separate statutory exceptions. Source: https://www.seg-social.pt/ptss/pssd/documento/cmc1xyfxz00dekl2ynxz676sw, p. 14; https://diariodarepublica.pt/dr/legislacao-consolidada/lei/2009-34514575, art. 151-A.

**Old-model employer filing hold (non-usable).** Do not apply the new-model confirmation date to employers still using the previous model during transition. Their operative declaration timing/acceptance is not supplied as a usable rule here. Check this point with one of our partner accountants.

**Annual review.** Segurança Social compares the year with AT data, notifies differences and allows a response. Regulation art. 62-A places a resulting liability in January of the following year; payments from review are late under Code art. 164-A(2). The annual-review de minimis is a minimum **base** of EUR 20 in Despacho 599/2019, not a universal EUR 20 contribution threshold. The ISS guide states that extra payment after January 2026 confirmation of 2025 income could be made by 20 February 2026; retain that dated instruction only for that case. Credits go against future contributions or a refund can be requested on RC 3041. Sources: https://diariodarepublica.pt/dr/legislacao-consolidada/lei/2009-34514575, art. 164-A; https://diariodarepublica.pt/dr/legislacao-consolidada/decreto-regulamentar/2011-56720826, art. 62-A; https://files.diariodarepublica.pt/2s/2019/01/008000000/0152401524.pdf, point 2; https://www.seg-social.pt/ptss/pssd/documento/cmc1xyfxz00dekl2ynxz676sw, p. 18.

**Payments.** Multibanco, homebanking and authorised direct debit are available. Direct debit covers the current month's contribution only; old debts/interest and increased differences after a corrected declaration need another payment route. Source: https://www.seg-social.pt/ptss/pssd/documento/cmc1xyfxz00dekl2ynxz676sw, pp. 19–21.

## Penalties and interest

Late self-employed/contracting-entity payment is a light offence if cured within thirty days after deadline, serious thereafter (art. 155(4)); quarterly-declaration breach is light (art. 151-A(8)). New-model omission of a worker's remuneration is very serious; a declaration/correction breach affecting worker amounts is light when cured in sixty days, otherwise serious (art. 40(10)–(11)). Sources: https://diariodarepublica.pt/dr/legislacao-consolidada/lei/2009-34514575; https://diariodarepublica.pt/dr/detalhe/decreto-lei/127-2025-967317021.

| Offence class | Negligent fine (EUR) | Intentional fine (EUR) | Official source |
|---|---|---|---|
| Light | 50–250 | 100–500 | https://diariodarepublica.pt/dr/legislacao-consolidada/lei/2009-34514575, art. 233(1) |
| Serious | 300–1,200 | 600–2,400 | https://diariodarepublica.pt/dr/legislacao-consolidada/lei/2009-34514575, art. 233(2) |
| Very serious | 1,250–6,250 | 2,500–12,500 | https://diariodarepublica.pt/dr/legislacao-consolidada/lei/2009-34514575, art. 233(3) |

Both limits rise by 50% for legal persons/equivalent entities with fewer than fifty workers, and by 100% with fifty or more. These are statutory bands, not an assessed fine; recurrence, concurrent offences and criminal treatment are outside the calculation here. Check this point with one of our partner accountants. Source: https://diariodarepublica.pt/dr/legislacao-consolidada/lei/2009-34514575, arts. 233–237.

Interest uses the table's dated rate and Code calendar-month/part rule. Do not substitute a universal daily-interest formula. For benefits the ISS guide requires contributions regularised through the end of the third month before the event month; irregular payment can temporarily suspend payment of benefits. This is not a complete benefit-eligibility assessment. Sources: https://diariodarepublica.pt/dr/legislacao-consolidada/lei/2009-34514575, arts. 211–212; https://diariodarepublica.pt/dr/detalhe/aviso/18-2026-993315668; https://www.seg-social.pt/ptss/pssd/documento/cmc1xyfxz00dekl2ynxz676sw, p. 12.

## Cross-border points

Code art. 138 permits continued cover for a determined foreign-work period, ordinarily one year plus a further authorised year, subject to an international instrument; special technical knowledge/aptitude may justify longer authorisation. Under art. 165(4), the last base continues where the independent income is not declared in Portugal. Foreign pension exemption retains the compatibility condition above. Source: https://diariodarepublica.pt/dr/legislacao-consolidada/lei/2009-34514575, arts. 138, 157, 165.

**Applicable-country/A1 hold (non-usable).** EU multi-state work, postings, foreign cover and the temporary-in-Portugal exclusion require the applicable international rules and evidence; domestic continuation alone does not establish which state can charge. Check this point with one of our partner accountants.

## Worked examples

### Example 1: freelance designer, services only, first quarter 2026

Rita has been self-employed since 2022. She has no other job. From January to March 2026 she invoiced EUR 9,000 of design services. She files the declaration in April and does not use the 25% option.

1. Relevant income: 9,000 x 70% = EUR 6,300.
2. Monthly base: 6,300 / 3 = EUR 2,100. This is under the EUR 6,445.56 ceiling.
3. Monthly contribution: 2,100 x 21.4% = EUR 449.40 for April, May and June. She pays each between the 10th and the 20th of May, June and July.
4. For the quarter: 449.40 x 3 = EUR 1,348.20.

Over 2026 Rita invoices EUR 36,000, all to one Lisbon company. The company received 100% of her activity, which is over 80%, and her service income is over 6 x IAS. So the company owes 10% of EUR 36,000 = EUR 3,600 as a contracting entity. It pays this in 2027, by the 20th of the month after Segurança Social's notice. This is the company's own cost, not deducted from Rita.

```oa-check
name: PT self-employed services EUR 9,000 in Q1 2026, plus contracting entity
inputs:
  services: 9000
  goods: 0
  ias: 537.13
  rate: 0.214
  annual_services_to_client: 36000
  entity_rate: 0.10
steps:
  - relevant: services * 0.70 + goods * 0.20
  - base: min(relevant / 3, 12 * ias)
  - monthly: round(base * rate, 2)
  - quarter: monthly * 3
  - entity_contribution: annual_services_to_client * entity_rate
expected:
  relevant: 6300
  base: 2100
  monthly: 449.40
  quarter: 1348.20
  entity_contribution: 3600
```

### Example 2: employee with a side business above 4 x IAS

João is employed full-time by an unrelated company at EUR 1,400 a month, which is above 1 x IAS. His employment provides every contingency required by art. 157(1)(a), the exemption already takes effect and the independent activity is established. He also has recibos verdes activity and sells goods online; he is neither an ENI nor an EIRL holder. From April to June 2026 he invoiced EUR 15,000 of services and sold EUR 6,000 of goods. He files the declaration in July.

1. Relevant income: 15,000 x 70% + 6,000 x 20% = 10,500 + 1,200 = EUR 11,700.
2. Monthly average: 11,700 / 3 = EUR 3,900. This is at least 4 x IAS (EUR 2,148.52), so the employment exemption does not cover all of it.
3. Base: 3,900 - 2,148.52 = EUR 1,751.48 (art. 163(4)). This is under the ceiling. The 25% option does not apply to this base (art. 163(4)).
4. Monthly contribution: 1,751.48 x 21.4% = EUR 374.82 for July, August and September. He pays each between the 10th and the 20th of the following month.

If his next quarter's monthly average falls below EUR 2,148.52 and all employment-exemption conditions remain in force, he owes nothing as self-employed for those three months.

```oa-check
name: PT employee with side activity, Q2 2026 services 15,000 and goods 6,000
inputs:
  services: 15000
  goods: 6000
  ias: 537.13
  rate: 0.214
steps:
  - relevant: services * 0.70 + goods * 0.20
  - monthly_avg: relevant / 3
  - threshold: 4 * ias
  - base: min(max(0, monthly_avg - threshold), 12 * ias)
  - monthly: round(base * rate, 2)
  - quarter: monthly * 3
expected:
  relevant: 11700
  monthly_avg: 3900
  threshold: 2148.52
  base: 1751.48
  monthly: 374.82
  quarter: 1124.46
```

Both examples use Code arts. 140, 154–155, 157, 162–164 and 167–168 and the 2026 IAS; no minimum-charge conclusion is needed. Sources: https://diariodarepublica.pt/dr/legislacao-consolidada/lei/2009-34514575; https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/diplomas_legislativos/Documents/Portaria_480_A_2025_1.pdf.

### Retained historical cases: original inputs and years

The earlier 2025 cases were repeated in the 2026 version. They remain dated comparisons, not permission to use a historical IAS for a 2026 charge. The 2025 IAS was EUR 522.50, so four IAS EUR 2,090 and twelve IAS EUR 6,270. Sources: https://diariodarepublica.pt/dr/detalhe/portaria/6-b-2025-902111932, arts. 2, 4; https://diariodarepublica.pt/dr/legislacao-consolidada/lei/2009-34514575, arts. 145–146, 157, 162–164, 168. Unless the row says otherwise, numerical results are conditional on established ordinary quarterly cover, no exemption and no base option; keep full precision until the final cent.

| Original case | Preserved inputs | Corrected result / action |
|---|---|---|
| EC1, March 2025 start | Activity opened March 2025 | If first-ever, continuous and no early election: cover begins 1 March 2026, not after April declaration. March payment due 10–20 April; April is the next quarterly window. Interim charge remains non-usable under the minimum hold: Check this point with one of our partner accountants. |
| EC2, 2025 and 2026 | Services EUR 1,000/quarter | Monthly relevant income EUR 233.333…; contribution EUR 49.93. The old IAS minimum-base/EUR 102.81 result is withdrawn. |
| EC3, 2025 and 2026 | Services EUR 30,000/quarter | Monthly relevant income EUR 7,000. Cap EUR 6,270 → contribution EUR 1,341.78 in 2025; cap EUR 6,445.56 → EUR 1,379.35 in 2026. |
| EC4, 2025 and 2026 | Services EUR 6,000, goods EUR 15,000/quarter | Relevant income EUR 7,200/quarter, base EUR 2,400, contribution EUR 513.60/month. |
| EC5, 2025 and 2026 | Employment EUR 1,200/month, services EUR 2,000/quarter | Relevant income EUR 466.666…/month; contribution zero only if all employment-exemption conditions/effective dates above hold. Salary alone is insufficient. |
| Test 1, 2025 and 2026 | Services EUR 9,000/quarter, established, no employment | Base EUR 2,100, contribution EUR 449.40/month. EUR 5,392.80 is only a twelve-month projection if that contribution remains unchanged all year. |
| Test 2, 2025 and 2026 | Services EUR 1,500/quarter | Base EUR 350, contribution EUR 74.90/month, not EUR 102.81. |
| Test 3, 2025 and 2026 | Services EUR 30,000/quarter | Same complete calculation as EC3, preserving both original occurrences. |
| Test 4, 2025 and 2026 | Opened four months ago, services EUR 12,000/quarter | Zero only if first-ever start, continuous activity and no early election; an unqualified first-year exemption is withdrawn. Missing history/election: Check this point with one of our partner accountants. |
| Test 5, 2025 and 2026 | Goods EUR 20,000/quarter, no employment | Quarterly relevant income EUR 4,000; monthly base EUR 1,333.333…; monthly contribution EUR 285.33 at the stipulated ordinary rate. An actual ENI/EIRL uses its separate rate. |
| Test 6, 2025 and 2026 | Employment EUR 1,500/month, services EUR 2,000/quarter | Monthly relevant income EUR 466.666…; zero only with all employment-exemption conditions/effective dates, as in EC5. |
| Test 7, 2025 and 2026 | ENI with employees, services EUR 15,000/quarter | Base EUR 3,500; rate 25.2%; monthly EUR 882.00. Employees are part of this input, not a legal prerequisite for the ENI rate. |

```oa-check
name: PT preserved historical numeric cases 2025 and 2026
inputs:
  ias_2025: 522.50
  ias_2026: 537.13
  rate: 0.214
  eni_rate: 0.252
  ec2_services: 1000
  ec3_test3_services: 30000
  ec4_services: 6000
  ec4_goods: 15000
  ec5_salary: 1200
  ec5_test6_services: 2000
  test1_services: 9000
  test2_services: 1500
  test4_services: 12000
  test4_months: 4
  test5_goods: 20000
  test6_salary: 1500
  test7_services: 15000
steps:
  - ec2: round(ec2_services * 0.70 / 3 * rate, 2)
  - ec3_test3_2025: round(min(ec3_test3_services * 0.70 / 3, 12 * ias_2025) * rate, 2)
  - ec3_test3_2026: round(min(ec3_test3_services * 0.70 / 3, 12 * ias_2026) * rate, 2)
  - ec4: round((ec4_services * 0.70 + ec4_goods * 0.20) / 3 * rate, 2)
  - ec5_test6_monthly_relevant: round(ec5_test6_services * 0.70 / 3, 2)
  - test1_monthly: round(test1_services * 0.70 / 3 * rate, 2)
  - test1_projection: test1_monthly * 12
  - test2: round(test2_services * 0.70 / 3 * rate, 2)
  - test5: round(test5_goods * 0.20 / 3 * rate, 2)
  - test7: round(test7_services * 0.70 / 3 * eni_rate, 2)
expected:
  ec2: 49.93
  ec3_test3_2025: 1341.78
  ec3_test3_2026: 1379.35
  ec4: 513.60
  ec5_test6_monthly_relevant: 466.67
  test1_monthly: 449.40
  test1_projection: 5392.80
  test2: 74.90
  test5: 285.33
  test7: 882.00
```

## Ask the client first

Use existing records to establish the required inputs at the top. Ask only for missing facts. Keep gross income, year, period, chosen option, coverage/effective date, assessed base, payment month and any referral hold visible in the answer.

## Sources

| Official source and provisions read | URL | Read on |
|---|---|---|
| Contribution Code, arts. 53, 61–69, 108–112, 129–168, 211–212, 233–237; neighbouring scope/base conditions checked | https://diariodarepublica.pt/dr/legislacao-consolidada/lei/2009-34514575 | 2026-11-27 |
| Regulation 1-A/2011, arts. 48, 57-A–64: elections, declarations, exemptions, exclusions, review and spouse dependencies | https://diariodarepublica.pt/dr/legislacao-consolidada/decreto-regulamentar/2011-56720826 | 2026-11-27 |
| DL 127/2025: Code arts. 23-B, 40, 43; transition art. 5 and commencement art. 6 | https://diariodarepublica.pt/dr/detalhe/decreto-lei/127-2025-967317021 | 2026-11-27 |
| IAS 2026, Portaria 480-A/2025/1, arts. 2, 4 | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/diplomas_legislativos/Documents/Portaria_480_A_2025_1.pdf | 2026-11-27 |
| IAS 2025, Portaria 6-B/2025/1, arts. 2, 4; historical cases only | https://diariodarepublica.pt/dr/detalhe/portaria/6-b-2025-902111932 | 2026-11-27 |
| Despacho 599/2019, points 1–3: employment-excess and annual-review thresholds, read with current Regulation and ISS guidance | https://files.diariodarepublica.pt/2s/2019/01/008000000/0152401524.pdf | 2026-11-27 |
| Late interest 2026, Aviso 18/2026/2, points 1–2 | https://diariodarepublica.pt/dr/detalhe/aviso/18-2026-993315668 | 2026-11-27 |
| ISS Guide 1009 v1.09 (12 January 2026), pp. 6–22; conflicts resolved in favour of the Code or held | https://www.seg-social.pt/ptss/pssd/documento/cmc1xyfxz00dekl2ynxz676sw | 2026-11-27 |
| CIRS art. 31(2), (13)(a), with coefficient scope in (1)(b)/(c) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs31.aspx | 2026-11-27 |

Not yet confirmed for usable guidance: the updated minimum charge and dependent interim charges; old-model employer filing timing/acceptance; working-spouse assessment; specialist rates/bases/incentives and applicable-country/A1 outcomes. Each is a non-usable hold above. Check this point with one of our partner accountants.

> Contributed by OpenAccountants.
