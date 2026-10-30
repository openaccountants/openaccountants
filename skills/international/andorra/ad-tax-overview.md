---
name: ad-tax-overview
description: "A one-page map of the Andorran tax system for tax year 2026, read from the consolidated laws on the Portal Jurídic d'Andorra and the Govern d'Andorra tax pages. Covers the tax year, the currency, the Departament de Tributs i de Fronteres, who is resident, personal income tax (IRPF) at 10% with the EUR 24,000 personal reduction and the 50% bonus that gives an effective 5% up to EUR 40,000, the 10% company tax (IS), non-resident tax (IRNR), IGI at 4.5% with its other rates and the EUR 40,000 threshold, CASS contribution rates, the parish (comú) taxes, late surcharges and 2026 late interest, and the main filing windows. Use for 'how does tax work in Andorra', 'Andorra tax overview', 'Andorra tax rates 2026'. For the detail it points to ad-income-tax, ad-corporate-income-tax, andorra-igi, ad-payroll-social, ad-non-resident-income-tax, ad-transfer-pricing and ad-company-formation."
version: 0.3
jurisdiction: AD
category: international
tax_year: 2026
last_updated: 2026-10-30
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Andorra Tax Overview

This is a map, not a computation skill. Each line gives the 2026 headline figure and its source, and names the skill in this pack that carries the full rules. Where a domain skill and this overview ever differ, the domain skill wins.

The laws below are read from the consolidated texts on the Portal Jurídic d'Andorra. The portal marks each one "Text refós sense caràcter oficial": a consolidation without official status. The official text is the one published in the BOPA.

## Andorran tax system at a glance

- **Standard tax year.** Individuals: the calendar year. The IRPF tax period "coincideix amb l'any natural" and the tax falls due on its last day _(Llei 5/2014 IRPF, arts 40 and 41)_. Companies: the tax period is the company's own financial year (exercici econòmic), so a company can use a year end other than 31 December _(Llei 95/2010 IS, art 39(1))_.
- **Currency.** Euro (EUR). Andorran law states amounts in euros; for example, a company's share capital must appear in its statutes "amb la xifra indicada en euros" _(Llei 20/2007 de societats, art 14(1))_.
- **Tax authority.** Departament de Tributs i de Fronteres, within the Ministry of Finance. It handles the tax filings and taxpayer service _(Govern d'Andorra, "Altres impostos" page; Llei 1/2026 del pressupost, budget heading 420)_.
- **Who is resident (individuals).** A person who stays in Andorra more than 183 days in the calendar year, or whose main base of activities or economic interests is in Andorra. A spouse and minor children resident in Andorra create a presumption of residence. Cross-border workers who travel in daily from Spain or France to work for an Andorran employer are not resident _(Llei 5/2014 IRPF, art 8)_. Detail: `ad-income-tax`.
- **Who is resident (companies).** An entity formed under Andorran law, or with its registered office or its place of effective management in Andorra, or that has moved its seat to Andorra _(Llei 95/2010 IS, art 7(1))_. Detail: `ad-corporate-income-tax`.
- **Basis of taxation.** Residents are taxed on all their income "amb independència del lloc on s'hagin produït" (wherever it arose) _(IRPF art 2; IS art 4)_. Non-residents pay non-resident income tax (IRNR) only on Andorran income _(Llei 94/2010 IRNR; IS art 1(2))_. Detail: `ad-non-resident-income-tax`.
- **Personal income tax (IRPF) rate.** A single rate of 10% _(IRPF art 43)_. The general base is reduced by a personal minimum of EUR 24,000, or EUR 30,000 for a person with a recognised incapacity, and EUR 40,000 where the spouse or stable partner who lives with the taxpayer has no general income _(IRPF art 35(1))_. A taxpayer with employment, business or property income also gets a bonus of 50% of 10% of the general base above the EUR 24,000 personal minimum, capped at EUR 800 _(IRPF art 46)_. So for a single person with that kind of income the effective rate is 0% on the first EUR 24,000, 5% on the next EUR 16,000, and 10% above EUR 40,000. Savings income has its own EUR 3,000 exempt minimum _(IRPF art 37)_. Detail: `ad-income-tax`.
- **Company income tax (IS) rate.** 10% general rate. Regulated Andorran collective investment schemes pay 0%; their management companies pay the general rate _(Llei 95/2010 IS, art 41)_. Detail: `ad-corporate-income-tax`.
- **IS payment on account.** In the ninth month after the tax period starts (September for a calendar-year company), 50% of the previous year's liquidation tax _(IS art 45(1)-(2))_.
- **Non-resident income tax (IRNR).** 10% general rate. Royalties 5%. Reinsurance 1.5%. Gains on Andorran property held under 2 years 25%, from 2 to under 5 years 20%, from 5 to under 10 years 15%, and 10% after that _(Llei 94/2010 IRNR, art 29)_. Detail: `ad-non-resident-income-tax`.
- **Indirect tax (IGI).** Andorra has no VAT; it has the Impost General Indirecte. General rate 4.5% _(Llei 11/2012 IGI, art 57)_. Reduced 1% (listed food, water, books and press and other listed items) _(art 58)_; super-reduced 0% (listed health, education, social and other supplies) _(art 59)_; special 2.5% (passenger transport and listed cultural services) _(art 60 bis)_; specific 3.5% (one listed residential-rental property purchase) _(art 60 ter)_; increased 9.5% on banking and financial services _(art 60)_. Detail: `andorra-igi`.
- **IGI registration threshold.** A person is not treated as a business for IGI while annual supplies do not exceed EUR 40,000, unless they opt in. For farming and livestock the threshold is EUR 150,000 _(IGI art 5(4))_.
- **IGI filing frequency.** Based on the previous year's net turnover: below EUR 250,000, returns in July and January; below EUR 3,600,000, returns in April, July, October and January; EUR 3,600,000 or more, monthly. A new business files in April, July, October and January _(IGI art 78)_.
- **Social security (CASS).** Employee 3% general branch plus 3.5% retirement branch = 6.5%. Employer 7% plus 8.5% = 15.5% _(Llei 17/2008 de la seguretat social, arts 100 and 103)_. Self-employed 10% general plus 12% retirement = 22% of a base set as a percentage of the previous year's average CASS wage _(arts 101(2) and (8), 104(2))_. Detail: `ad-payroll-social`.
- **Personal income tax (IRPF) filing window.** File and pay between 1 April and 30 September of the year after the tax year, so 2026 income is filed in 2027. A person whose only income is employment income, movable capital income or exempt income does not have to file, unless that income was not subject to payments on account _(IRPF arts 55 and 56)_. Detail: `ad-income-tax`.
- **Company income tax (IS) filing window.** The return is due in the month after the six months that follow the end of the tax period: July for a 31 December year end, so July 2027 for calendar 2026. It may be filed earlier, within those six months, but that does not change the payment or refund deadlines _(Reglament de l'impost sobre societats, 29 December 2023, art 45(1))_. Detail: `ad-corporate-income-tax`.
- **Late filing surcharges.** A tax-bearing return filed late without a prior request: 2% if under two months late, 5% from two to twelve months, 10% after twelve months. 15% if filed after a formal request _(Llei 21/2014 de bases de l'ordenament tributari, art 24)_.
- **Late payment interest (interès moratori).** 4.05% for 2026. The separate legal interest rate is 3.24% _(Llei 1/2026 del pressupost per a l'exercici del 2026, art 17)_.
- **Wealth, inheritance and gift tax.** Andorra has none. The Govern's list of Andorran taxes names IRPF, IGI, IS and IRNR, plus "Altres impostos": the empty-housing tax (IHB), the insurance services tax (ISI), the property transfer tax (ITP), the property gains tax (plusvàlua), special taxes on alcohol, tobacco and fuel, and the gambling tax. None of these is a tax on net wealth or on inheritances and gifts as such _(Govern d'Andorra, "Altres impostos")_.
- **Property transfer tax (ITP).** 4% of the real value of a property transfer, paid by the buyer: 1% to the Govern and 3% to the parish _(Govern d'Andorra, "Altres impostos", ITP)_. The parish surcharge may be set between 0.50% and 3% _(Llei 10/2003 de les finances comunals, art 34(3))_.
- **Communal (parish) taxes.** Each of the seven parishes (comuns) sets five local taxes by ordinance, within ranges fixed by law _(Llei 10/2003 de les finances comunals, art 28)_:
  - foc i lloc (residence tax): EUR 5 to EUR 50 a year for each resident aged 18 to 65 _(art 29(2), (4))_;
  - property tax: EUR 0.30 to EUR 3 per m² built; EUR 0 to EUR 0.75 per m² of unbuilt land _(art 30(6))_;
  - tax on rental income: 0.4% to 4% of the rent accrued in the year _(art 31(6))_;
  - tax on business premises (radicació d'activitats): EUR 0.10 to EUR 100 per m², capped at EUR 300,000 _(art 32(6), (7))_;
  - construction tax: EUR 10 to EUR 50 per m² _(art 32 bis(6))_.
  The rate in a given parish is in that comú's ordinance.

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

## Sources

| Source | URL | Read on |
|---|---|---|
| Llei 5/2014 de l'impost sobre la renda de les persones físiques (IRPF), consolidated text, arts 2, 8, 35, 37, 40, 41, 43, 46, 55, 56 | https://www.portaljuridicandorra.ad/L2014005 | 2026-10-30 |
| Llei 95/2010 de l'impost sobre societats (IS), consolidated text, arts 1, 4, 7, 39, 41, 45 | https://www.portaljuridicandorra.ad/L2010095 | 2026-10-30 |
| Reglament de l'impost sobre societats, 29 December 2023, consolidated text, art 45 | https://www.portaljuridicandorra.ad/R20231229C | 2026-10-30 |
| Llei 94/2010 de l'impost sobre la renda dels no-residents fiscals (IRNR), consolidated text, art 29 | https://www.portaljuridicandorra.ad/L2010094 | 2026-10-30 |
| Llei 11/2012 de l'impost general indirecte (IGI), consolidated text, arts 5, 57, 58, 59, 60, 60 bis, 60 ter, 78 | https://www.portaljuridicandorra.ad/L2012011 | 2026-10-30 |
| Llei 17/2008 de la seguretat social, consolidated text, arts 100, 101, 103, 104 | https://www.portaljuridicandorra.ad/L2008017 | 2026-10-30 |
| Llei 21/2014 de bases de l'ordenament tributari, consolidated text, art 24 | https://www.portaljuridicandorra.ad/L2014021 | 2026-10-30 |
| Llei 1/2026 del pressupost per a l'exercici del 2026, art 17 and budget heading 420 | https://www.portaljuridicandorra.ad/L2026001 | 2026-10-30 |
| Llei 10/2003 de les finances comunals, consolidated text, arts 28 to 32 bis and 34 | https://www.portaljuridicandorra.ad/L2003010 | 2026-10-30 |
| Llei 20/2007 de societats anònimes i de responsabilitat limitada, consolidated text, art 14 | https://www.portaljuridicandorra.ad/L2007020 | 2026-10-30 |
| Govern d'Andorra, Impostos a Andorra: Altres impostos (IHB, ISI, ITP, plusvàlua, special taxes, gambling) | https://www.govern.ad/ca/tematiques/impostos-taxes-i-duana/impostos-en-andorra/altres-impostos | 2026-10-30 |
| Govern d'Andorra, Impostos a Andorra (list of the main taxes) | https://www.govern.ad/ca/tematiques/impostos-taxes-i-duana/impostos-a-andorra | 2026-10-30 |

Not yet confirmed: (1) no Andorran statute says in terms that there is no wealth, inheritance or gift tax; the "none" line is read from the Govern's list of taxes, which names no such tax. (2) The Govern's "Altres impostos" page still lists the property gains tax (plusvàlua, Llei 21/2006) at 1% to 15%; how it now interacts with the IRPF, IS and IRNR property-gain rules was not read for this overview, so no plusvàlua rate is given here (see `ad-income-tax`, `ad-corporate-income-tax` and `ad-non-resident-income-tax` for property gains). (3) Each parish's 2026 ordinance rates for the comú taxes were not read; only the legal ranges are given. (4) The consolidated texts are marked as having no official status; the BOPA text governs.

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
