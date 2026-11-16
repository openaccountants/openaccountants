---
name: ad-tax-overview
description: "A one-page rates card and map of the Andorran tax system for tax year 2026, read from the consolidated laws on the Portal Jurídic d'Andorra, the 2026 budget law and the Govern d'Andorra tax pages. Covers the tax year, the currency, the Departament de Tributs i de Fronteres, who is resident, personal income tax (IRPF) at 10% with the EUR 24,000 personal reduction and the 50% bonus that gives an effective 5% up to EUR 40,000, the 10% company tax (IS) and its September payment on account, non-resident tax (IRNR) rates, IGI at 4.5% with its other rates, the EUR 40,000 threshold and return frequency, CASS contribution rates, the property transfer tax, the parish (comú) taxes, late-filing surcharges, enforcement surcharges and 2026 late interest, and the main filing windows, with one worked IRPF example. Use for 'how does tax work in Andorra', 'Andorra tax overview', 'Andorra tax rates 2026'. For the detail it points to ad-income-tax, ad-corporate-income-tax, andorra-igi, ad-payroll-social, ad-non-resident-income-tax, ad-transfer-pricing and ad-company-formation."
version: 0.4
jurisdiction: AD
category: international
tax_year: 2026
last_updated: 2026-11-16
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
type: rates-card
---

# Andorra Tax Overview

This is a map, not a computation skill. Each line gives the 2026 headline figure and its source, and names the skill in this pack that carries the full rules. Where a domain skill and this overview ever differ, the domain skill wins.

The laws below are read from the consolidated texts on the Portal Jurídic d'Andorra. The portal marks each one "Text refós sense caràcter oficial": a consolidation without official status. The official text is the one published in the BOPA.

**Quick answer (2026).** Personal income tax 10%, with the first EUR 24,000 free and an effective 5% up to EUR 40,000 for earned, business or property income. Company tax 10%. IGI (the indirect tax) 4.5% general. Employee CASS 6.5%, employer 15.5%. No wealth, inheritance or gift tax is listed. Late interest 4.05% for 2026. Ask first: resident or not, the kind of income, individual or company, and the parish.

## Ask the client first

- Is the person or company resident in Andorra for tax (183 days, centre of interests, place of incorporation or management)?
- What kind of income: employment, business, property, savings, or Andorran income of a non-resident?
- Individual or company, and for a company its financial year end?
- Annual supplies or turnover (IGI threshold and return frequency)?
- Which parish (the comú taxes are set by each parish)?

## Rates, bands and thresholds

All rows are for 2026 unless a row says otherwise.

| Item | Figure | Condition | Source |
|---|---|---|---|
| Tax year, individuals | Calendar year; tax falls due on its last day | IRPF arts 40 and 41: the period "coincideix amb l'any natural"; shorter on death | [Llei 5/2014 IRPF arts 40, 41](https://www.portaljuridicandorra.ad/L2014005) |
| Tax year, companies | The company's own financial year, at most 12 months | IS art 39(1), (3); a company can use a year end other than 31 December | [Llei 95/2010 IS art 39](https://www.portaljuridicandorra.ad/L2010095) |
| Currency | Euro (EUR) | For example, share capital must appear in the statutes "amb la xifra indicada en euros" (Llei 20/2007 art 14(1)) | [Llei 20/2007 art 14](https://www.portaljuridicandorra.ad/L2007020) |
| Tax authority | Departament de Tributs i de Fronteres, Ministry of Finance | Handles tax filings and taxpayer service; budget heading 420 | [Govern d'Andorra, Impostos a Andorra](https://www.govern.ad/ca/tematiques/impostos-taxes-i-duana/impostos-a-andorra) ; [Llei 1/2026](https://www.portaljuridicandorra.ad/L2026001) |
| Resident individual | More than 183 days in the calendar year, or main base of activities or economic interests in Andorra | Spouse and minor children resident create a presumption; daily cross-border workers from Spain or France employed in Andorra are not resident (IRPF art 8). Detail: `ad-income-tax` | [Llei 5/2014 IRPF art 8](https://www.portaljuridicandorra.ad/L2014005) |
| Resident company | Formed under Andorran law, or registered office or effective management in Andorra, or seat moved to Andorra | IS art 7(1). Detail: `ad-corporate-income-tax` | [Llei 95/2010 IS art 7](https://www.portaljuridicandorra.ad/L2010095) |
| Basis of taxation | Residents: worldwide income; non-residents: Andorran income only, under IRNR | Residents taxed "amb independència del lloc on s'hagin produït" (IRPF art 2; IS art 4); non-residents under Llei 94/2010 (IS art 1(2)). Detail: `ad-non-resident-income-tax` | [Llei 5/2014 IRPF art 2](https://www.portaljuridicandorra.ad/L2014005) ; [Llei 95/2010 IS arts 1, 4](https://www.portaljuridicandorra.ad/L2010095) |
| IRPF rate | 10% | Single rate (IRPF art 43). Detail: `ad-income-tax` | [Llei 5/2014 IRPF art 43](https://www.portaljuridicandorra.ad/L2014005) |
| IRPF personal minimum | EUR 24,000; EUR 30,000 with recognised incapacity; EUR 40,000 where the cohabiting spouse or stable partner has no general income | Reduces the general base; unused spouse amount can pass to the other spouse, joint cap EUR 40,000 (IRPF art 35(1)) | [Llei 5/2014 IRPF art 35](https://www.portaljuridicandorra.ad/L2014005) |
| IRPF bonus | 50% of the tax on the general base above the personal minimum, capped at EUR 800 | Only with employment, business or property income (IRPF art 46) | [Llei 5/2014 IRPF art 46](https://www.portaljuridicandorra.ad/L2014005) |
| IRPF effective bands, single person with that income | 0% to EUR 24,000; 5% from EUR 24,000 to EUR 40,000; 10% above EUR 40,000 | Computed from arts 35, 43 and 46: the EUR 800 cap is reached at EUR 16,000 above the minimum | [Llei 5/2014 IRPF arts 35, 43, 46](https://www.portaljuridicandorra.ad/L2014005) |
| IRPF savings minimum | EUR 3,000 | Reduces the savings base (IRPF art 37) | [Llei 5/2014 IRPF art 37](https://www.portaljuridicandorra.ad/L2014005) |
| IRPF return and payment | 1 April to 30 September of the following year | 2026 income filed in 2027. No return if the only income is employment, movable capital or exempt income, unless it was not subject to payments on account (IRPF arts 55, 56). Detail: `ad-income-tax` | [Llei 5/2014 IRPF arts 55, 56](https://www.portaljuridicandorra.ad/L2014005) |
| IS rate | 10% | Regulated Andorran collective investment schemes 0%; their management companies pay the general rate (IS art 41). Detail: `ad-corporate-income-tax` | [Llei 95/2010 IS art 41](https://www.portaljuridicandorra.ad/L2010095) |
| IS payment on account | 50% of the previous year's liquidation quota | Paid in the ninth month after the tax period starts: September for a calendar-year company (IS art 45(1)-(2)) | [Llei 95/2010 IS art 45](https://www.portaljuridicandorra.ad/L2010095) |
| IS return | In the month after the six months that follow the period end | July for a 31 December year end, so July 2027 for calendar 2026; may be filed earlier without changing payment or refund deadlines (IS Regulation art 45(1)) | [Reglament IS 2023 art 45](https://www.portaljuridicandorra.ad/R20231229C) |
| IRNR rates | General 10%; royalties 5%; reinsurance 1.5% | IRNR art 29(a)-(c). Detail: `ad-non-resident-income-tax` | [Llei 94/2010 IRNR art 29](https://www.portaljuridicandorra.ad/L2010094) |
| IRNR on Andorran property gains | Held under 2 years 25%; 2 to under 5 years 20%; 5 to under 10 years 15%; 10 years or more 10% | Art 29(d)-(f); the 10% after 10 years is the general rate of art 29(a) | [Llei 94/2010 IRNR art 29](https://www.portaljuridicandorra.ad/L2010094) |
| IGI general rate | 4.5% | Applies unless another rate is expressly provided (IGI art 57). Andorra has no VAT; IGI is its general indirect tax. Detail: `andorra-igi` | [Llei 11/2012 IGI art 57](https://www.portaljuridicandorra.ad/L2012011) |
| IGI reduced rate | 1% | Listed food and non-alcoholic drink, water, books and press, sanitary products (IGI art 58) | [Llei 11/2012 IGI art 58](https://www.portaljuridicandorra.ad/L2012011) |
| IGI super-reduced rate | 0% | Listed health, education, social, sport, cultural (non-profit), residential lettings and other supplies (IGI art 59) | [Llei 11/2012 IGI art 59](https://www.portaljuridicandorra.ad/L2012011) |
| IGI special rate | 2.5% | Passenger transport (not cable), listed cultural services by for-profit providers, art and antiques (IGI art 60 bis) | [Llei 11/2012 IGI art 60 bis](https://www.portaljuridicandorra.ad/L2012011) |
| IGI specific rate | 3.5% | Purchase of a home for permanent residential letting by a non-business buyer, let for at least five years; otherwise the general rate plus late interest (IGI art 60 ter) | [Llei 11/2012 IGI art 60 ter](https://www.portaljuridicandorra.ad/L2012011) |
| IGI increased rate | 9.5% | Banking and financial services (IGI art 60) | [Llei 11/2012 IGI art 60](https://www.portaljuridicandorra.ad/L2012011) |
| IGI business threshold | EUR 40,000 a year; EUR 150,000 for farming and livestock | Below it a person is not treated as a business for IGI unless they opt in (then at least three years); prorated in the start year (IGI art 5(4)) | [Llei 11/2012 IGI art 5](https://www.portaljuridicandorra.ad/L2012011) |
| IGI return frequency | Below EUR 250,000: July and January. Below EUR 3,600,000: April, July, October and January. EUR 3,600,000 or more: monthly | Previous year's net turnover; a new business files April, July, October and January, or July and January under the simplified regime (IGI art 78(1)) | [Llei 11/2012 IGI art 78](https://www.portaljuridicandorra.ad/L2012011) |
| CASS, employee | 6.5% (computed: 3% general + 3.5% retirement) | Llei 17/2008 arts 100, 103. Detail: `ad-payroll-social` | [Llei 17/2008 arts 100, 103](https://www.portaljuridicandorra.ad/L2008017) |
| CASS, employer | 15.5% (computed: 7% general + 8.5% retirement) | Same articles | [Llei 17/2008 arts 100, 103](https://www.portaljuridicandorra.ad/L2008017) |
| CASS, self-employed | 22% (computed: 10% general + 12% retirement) | On a base set as a percentage of the previous year's average CASS wage (arts 101(2), (8), 104(2)) | [Llei 17/2008 arts 101, 104](https://www.portaljuridicandorra.ad/L2008017) |
| Late filing surcharge, voluntary | 2% under two months; 5% from two to twelve months; 10% after twelve months | Tax-bearing return filed late without a prior request (Llei 21/2014 art 24(2)) | [Llei 21/2014 art 24](https://www.portaljuridicandorra.ad/L2014021) |
| Late filing surcharge, after a request | 15% | Filed within the period the formal request sets (art 24(3)) | [Llei 21/2014 art 24](https://www.portaljuridicandorra.ad/L2014021) |
| Enforcement-period surcharges | 2%; 10%; 20% | 2% if paid before the enforcement order is notified; 10% if paid with it before that period ends; 20% otherwise, with late interest only on the 20% (art 25) | [Llei 21/2014 art 25](https://www.portaljuridicandorra.ad/L2014021) |
| Late payment interest (interès moratori) | 4.05% | For 2026 (Llei 1/2026 art 17(2)) | [Llei 1/2026 art 17](https://www.portaljuridicandorra.ad/L2026001) |
| Legal interest rate | 3.24% | For 2026 (Llei 1/2026 art 17(1)) | [Llei 1/2026 art 17](https://www.portaljuridicandorra.ad/L2026001) |
| Property transfer tax (ITP) | 4% of real value, paid by the buyer: 1% Govern, 3% parish | Govern page, ITP | [Govern d'Andorra, Altres impostos](https://www.govern.ad/ca/tematiques/impostos-taxes-i-duana/impostos-en-andorra/altres-impostos) |
| ITP parish share range | 0.50% to 3% | Set by each parish ordinance (Llei 10/2003 art 34(3)) | [Llei 10/2003 art 34](https://www.portaljuridicandorra.ad/L2003010) |
| Foc i lloc (parish residence tax) | EUR 5 to EUR 50 a year | Each resident aged 18 to 65 (Llei 10/2003 art 29(2), (4)) | [Llei 10/2003 art 29](https://www.portaljuridicandorra.ad/L2003010) |
| Parish property tax | EUR 0.30 to EUR 3 per m² built; EUR 0 to EUR 0.75 per m² of unbuilt land | Llei 10/2003 art 30(6) | [Llei 10/2003 art 30](https://www.portaljuridicandorra.ad/L2003010) |
| Parish tax on rental income | 0.4% to 4% of rent accrued in the year | Llei 10/2003 art 31(6) | [Llei 10/2003 art 31](https://www.portaljuridicandorra.ad/L2003010) |
| Parish tax on business premises (radicació) | EUR 0.10 to EUR 100 per m², capped at EUR 300,000 | Llei 10/2003 art 32(6), (7) | [Llei 10/2003 art 32](https://www.portaljuridicandorra.ad/L2003010) |
| Parish construction tax | EUR 10 to EUR 50 per m² | Llei 10/2003 art 32 bis(6) | [Llei 10/2003 art 32 bis](https://www.portaljuridicandorra.ad/L2003010) |

## How the system fits together

- **Standard tax year.** Individuals: the calendar year. The IRPF tax period "coincideix amb l'any natural" and the tax falls due on its last day _(Llei 5/2014 IRPF, arts 40 and 41)_. Companies: the tax period is the company's own financial year (exercici econòmic), so a company can use a year end other than 31 December _(Llei 95/2010 IS, art 39(1))_.
- **Personal income tax (IRPF).** A single rate of 10% _(IRPF art 43)_. The general base is reduced by a personal minimum of EUR 24,000, or EUR 30,000 for a person with a recognised incapacity, and EUR 40,000 where the spouse or stable partner who lives with the taxpayer has no general income _(IRPF art 35(1))_. A taxpayer with employment, business or property income also gets a bonus of 50% of 10% of the general base above the EUR 24,000 personal minimum, capped at EUR 800 _(IRPF art 46)_. So for a single person with that kind of income the effective rate is 0% on the first EUR 24,000, 5% on the next EUR 16,000, and 10% above EUR 40,000. Savings income has its own EUR 3,000 exempt minimum _(IRPF art 37)_. Detail: `ad-income-tax`.
- **Wealth, inheritance and gift tax.** Andorra has none. The Govern's list of Andorran taxes names IRPF, IGI, IS and IRNR, plus "Altres impostos": the empty-housing tax (IHB), the insurance services tax (ISI), the property transfer tax (ITP), the property gains tax (plusvàlua), special taxes on alcohol, tobacco and fuel, and the gambling tax. None of these is a tax on net wealth or on inheritances and gifts as such _(Govern d'Andorra, "Altres impostos")_.
- **Communal (parish) taxes.** Andorra has seven parishes _(Constitució, art 1(5))_. Each parish (comú) sets five local taxes by ordinance, within ranges fixed by law _(Llei 10/2003 de les finances comunals, art 28)_: foc i lloc, property tax, tax on rental income, tax on business premises and construction tax (ranges in the table). The rate in a given parish is in that comú's ordinance.

## Which skill to use

| Question | Skill |
|---|---|
| A resident's IRPF return, allowances, the 50% bonus, property and investment income | `ad-income-tax` |
| Company tax, holding and IP regimes, losses, the September payment on account | `ad-corporate-income-tax` |
| IGI rates, registration, returns, imports, reverse charge | `andorra-igi` |
| Payroll withholding, CASS for employees and the self-employed, the minimum wage | `ad-payroll-social` |
| Non-residents, withholding on payments abroad, property sales by non-residents, treaties | `ad-non-resident-income-tax` |
| Related-party prices, country-by-country reporting | `ad-transfer-pricing` |
| SL or SA, capital, foreign-investment authorisation, annual accounts | `ad-company-formation` |

## Worked example that recomputes

A single resident employee has a general base of EUR 50,000 in 2026 and no other reductions. Tax at 10% on the base above the EUR 24,000 personal minimum is EUR 2,600. The art 46 bonus is 50% of that, EUR 1,300, capped at EUR 800. IRPF due is EUR 1,800, which matches the effective bands: 5% of EUR 16,000 (EUR 800) plus 10% of EUR 10,000 (EUR 1,000). The full return method, including family reductions and payments on account, is in `ad-income-tax`.

```oa-check
name: Andorra IRPF headline, single employee, EUR 50,000 general base (2026)
inputs:
  general_base: 50000
  personal_minimum: 24000
  rate: 0.10
  bonus_share: 0.50
  bonus_cap: 800
steps:
  reduced_base: max(0, general_base - personal_minimum)
  gross_tax: reduced_base * rate
  bonus: min(bonus_cap, gross_tax * bonus_share)
  tax_due: gross_tax - bonus
  band_check: min(reduced_base, 16000) * 0.05 + max(0, reduced_base - 16000) * 0.10
expected:
  gross_tax: 2600
  bonus: 800
  tax_due: 1800
  band_check: 1800
```

## Sources

| Source | URL | Read on |
|---|---|---|
| Llei 5/2014 de l'impost sobre la renda de les persones físiques (IRPF), consolidated text 13, arts 2, 8, 35, 37, 40, 41, 43, 46, 55, 56 | https://www.portaljuridicandorra.ad/L2014005 | 2026-11-16 |
| Llei 95/2010 de l'impost sobre societats (IS), consolidated text 21 (in force 13 February 2026), arts 1, 4, 7, 39, 41, 45 | https://www.portaljuridicandorra.ad/L2010095 | 2026-11-16 |
| Reglament de l'impost sobre societats, 29 December 2023, consolidated text, art 45 | https://www.portaljuridicandorra.ad/R20231229C | 2026-11-16 |
| Llei 94/2010 de l'impost sobre la renda dels no-residents fiscals (IRNR), consolidated text 5, art 29 | https://www.portaljuridicandorra.ad/L2010094 | 2026-11-16 |
| Llei 11/2012 de l'impost general indirecte (IGI), consolidated text 23, arts 5, 57, 58, 59, 60, 60 bis, 60 ter, 78 | https://www.portaljuridicandorra.ad/L2012011 | 2026-11-16 |
| Llei 17/2008 de la seguretat social, consolidated text 35 (in force 4 June 2026), arts 100, 101, 103, 104 | https://www.portaljuridicandorra.ad/L2008017 | 2026-11-16 |
| Llei 21/2014 de bases de l'ordenament tributari, consolidated text 5, arts 23, 24, 25 | https://www.portaljuridicandorra.ad/L2014021 | 2026-11-16 |
| Llei 1/2026 del pressupost per a l'exercici del 2026, art 17 and budget heading 420 | https://www.portaljuridicandorra.ad/L2026001 | 2026-11-16 |
| Llei 10/2003 de les finances comunals, consolidated text 8, arts 28 to 32 bis and 34 | https://www.portaljuridicandorra.ad/L2003010 | 2026-11-16 |
| Llei 20/2007 de societats anònimes i de responsabilitat limitada, consolidated text 15, art 14 | https://www.portaljuridicandorra.ad/L2007020 | 2026-11-16 |
| Constitució del Principat d'Andorra, art 1(5) (the seven parishes) | https://www.portaljuridicandorra.ad/Constitucio | 2026-11-16 |
| Govern d'Andorra, Impostos a Andorra: Altres impostos, read for the IHB, ISI, ITP, plusvàlua, special taxes and gambling sections | https://www.govern.ad/ca/tematiques/impostos-taxes-i-duana/impostos-en-andorra/altres-impostos | 2026-11-16 |
| Govern d'Andorra, Impostos a Andorra, read for the list of the main taxes and the Departament de Tributs i de Fronteres | https://www.govern.ad/ca/tematiques/impostos-taxes-i-duana/impostos-a-andorra | 2026-11-16 |

Not yet confirmed: (1) no Andorran statute says in terms that there is no wealth, inheritance or gift tax; the "none" line is read from the Govern's list of taxes, which names no such tax. (2) The Govern's "Altres impostos" page still lists the property gains tax (plusvàlua, Llei 21/2006) at 1% to 15%; how it now interacts with the IRPF, IS and IRNR property-gain rules was not read for this overview, so no plusvàlua rate is given here (see `ad-income-tax`, `ad-corporate-income-tax` and `ad-non-resident-income-tax` for property gains). (3) Each parish's 2026 ordinance rates for the comú taxes were not read; only the legal ranges are given. (4) The consolidated texts are marked as having no official status; the BOPA text governs. (5) The ITP 4% split (1% Govern, 3% parish) is taken from the Govern page; the ITP law itself was not read, and the parish share can range from 0.50% to 3% under Llei 10/2003.
