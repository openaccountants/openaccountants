---
name: pt-transfer-pricing
description: "Use this skill for Portuguese transfer pricing (preços de transferência) under article 63 of the IRC Code and Portaria 268/2021. It covers related parties (relações especiais, the 20% holding test), domestic and cross-border dealings, permanent establishments, the arm's length rule and methods, intra-group services, self-adjustments in the Modelo 22, the documentation file (Dossier Principal and Dossier Específico), the EUR 10 million exemption and the EUR 100,000 / EUR 500,000 transaction exemption, the SME simplified file, disclosure in the IES, country-by-country reporting (EUR 750 million) and its notification, advance pricing agreements (art. 138 CIRC, Portaria 267/2021), penalties under RGIT art. 117(6), and corresponding adjustments and the EU dispute procedure (Lei 120/2019). Tax year 2026. Trigger on: transfer pricing Portugal, preços de transferência, dossier fiscal, relações especiais, CbCR Portugal, APPT, Portaria 268/2021. Out of scope: IRC rates and the base in general (pt-corporate-tax), treaty relief for individuals (pt-foreign-source-treaties), VAT (pt-vat-return)."
version: 0.1
jurisdiction: PT
tax_year: 2026
last_updated: 2026-10-23
authored_by: Ryan Duguid
review_status: pending_review
trust_label: Accountant-authored
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Portugal transfer pricing (preços de transferência), 2026

This skill sets out how Portugal taxes dealings between related parties: who is related, the arm's length rule, the methods, the documentation a company must hold, the country-by-country report, advance pricing agreements, the penalties, and how double taxation is removed. Figures are for tax periods in 2026. The rules sit in article 63 of the IRC Code (CIRC), in Portaria 268/2021 (the transfer pricing regulation, in force since 27 November 2021, with its documentation chapter applying to tax periods starting on or after 1 January 2021 under its art. 28; the AT's copy lists no amendments) and in Portaria 267/2021 (advance pricing agreements).

For the IRC rate, the surcharges, losses and the Modelo 22 itself, see pt-corporate-tax. For treaty relief on foreign income of individuals, see pt-foreign-source-treaties.

## Who this applies to

**The rule.** In any dealing between an IRC taxpayer and an entity with which it has a special relationship (relações especiais), the terms must be substantially the same as independent parties would agree in comparable dealings (art. 63(1) CIRC). The other party can be subject to IRC or not. Portaria 268/2021 applies the same rule to IRS taxpayers with business income (Portaria art. 1(1)).

**Who is related (art. 63(4) CIRC).** A special relationship exists where one entity can exercise, directly or indirectly, significant influence over the management decisions of the other. The law presumes it, among other cases, between:

1. An entity and its shareholders, or their spouses, ascendants or descendants, who hold directly or indirectly at least 20% of the capital or the voting rights.
2. Entities in which the same shareholders, or their spouses, ascendants or descendants, hold directly or indirectly at least 20% of the capital or voting rights.
3. An entity and the members of its corporate bodies, or of any management, direction or supervisory body, and their spouses, ascendants and descendants.
4. Entities where most members of the corporate or management bodies are the same people, or are linked by marriage, legally recognised unmarried partnership or direct-line kinship.
5. Entities linked by a subordination contract, an equal-standing group contract or another contract with the same effect.
6. Companies in a relationship of control under article 486 of the Commercial Companies Code.
7. Entities whose legal relationship lets one condition the management decisions of the other, for reasons outside the commercial or professional relationship itself.
8. A resident entity, or a non-resident with a Portuguese permanent establishment, and an entity resident in a country, territory or region on the Finance Minister's list of clearly more favourable tax regimes.

Indirect holdings are measured under article 483(2) of the Commercial Companies Code where no special rule applies (art. 63(5)).

**Which dealings.** Commercial dealings in goods, intangibles, rights and services, including cost-sharing and intra-group service arrangements; financial dealings; and business restructurings (art. 63(2) CIRC). Portaria 268/2021 art. 1(3)(a)(2) spells out that financial dealings include loans of any kind, derivatives, explicit or implicit guarantees, cash pooling and dealings in shares.

**Domestic and cross-border.** The rule covers dealings with non-residents and dealings between two Portuguese IRC or IRS taxpayers (Portaria art. 2(a) and (d)). The difference is who corrects: the taxpayer must self-correct only for dealings with non-residents (art. 63(8)); for domestic dealings the AT corrects and must then make the matching adjustment at the other Portuguese party (art. 63(13)).

**Permanent establishments.** The rule also applies between a non-resident and its Portuguese permanent establishment, between that PE and the same entity's other PEs abroad, and between a resident entity and its foreign PEs (art. 63(11) CIRC; Portaria art. 2(b) and (c), including the allocation of general administrative costs under art. 55(2) CIRC). It also applies to a person carrying on activities inside and outside the general IRC regime (art. 63(12); Portaria art. 26).

## Rates, bands and thresholds

| Item | Rate or amount | Tax year | Source |
|---|---|---|---|
| Related-party holding test | at least 20% of capital or voting rights, direct or indirect | 2026 | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc63.aspx |
| Exemption from the transfer pricing documentation file: total annual income (rendimentos) in the period below | EUR 10,000,000 | 2026 | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/diplomas_legislativos/Documents/Portaria_268_2021.pdf (art. 17(3)) |
| Start-up year: the EUR 10,000,000 test uses the annualised estimated income in the start-of-activity declaration | annualised | 2026 | Portaria 268/2021 art. 17(4) |
| Exemption for small related dealings even above EUR 10,000,000: value per counterparty, measured at market value, not above | EUR 100,000 | 2026 | Portaria 268/2021 art. 17(5) |
| Same exemption: value in aggregate not above | EUR 500,000 | 2026 | Portaria 268/2021 art. 17(5) |
| Exemptions do not cover dealings with residents of listed preferential tax regimes (art. 63-D(1) or (5) LGT) | no exemption | 2026 | Portaria 268/2021 art. 17(6) |
| SME not exempt and not followed by the Large Taxpayers Unit | simplified file (Dossier simplificado); it must also hold full arm's length evidence for any dealing with a listed preferential regime, business transfers, unlisted shares, restructurings, real estate or intangibles | 2026 | Portaria 268/2021 art. 19(1) and (2) |
| Comparability studies stay valid, if facts have not changed substantially (financial data updated each year) | 3 years | 2026 | Portaria 268/2021 art. 17(12) |
| Disclosure of related-party dealings in the annual return (IES) | every IRC taxpayer, yes or no, with detail if yes | 2026 | art. 63(7) CIRC |
| Country-by-country report: group consolidated revenue in the previous period at or above | EUR 750,000,000 | 2026 | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc121a.aspx |
| Advance pricing agreement: maximum term | 4 years | 2026 | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc138.aspx (art. 138(6)) |
| APA fee: set by Portaria 923/99 arts. 1 and 2 on average turnover of the 3 prior periods; renewal or revision cut by 50%; further cut of 25% for a micro, small or medium enterprise mainly trading internationally | see Not yet confirmed | 2026 | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/diplomas_legislativos/Documents/Portaria_267_2021.pdf (art. 18) |
| IRC general rate, periods starting in 2026 (used in the examples) | 19% | 2026 | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc87.aspx (Lei 64/2025 art. 3(2)) |
| Derrama estadual, taxable profit above EUR 1,500,000 up to EUR 7,500,000 | 3% | 2026 | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc87a.aspx |
| Derrama estadual, above EUR 7,500,000 up to EUR 35,000,000 / above EUR 35,000,000 | 5% / 9% | 2026 | same |

There is no fixed safe-harbour mark-up for low-value services in Portaria 268/2021. Article 14 requires an appropriate profit margin on intra-group services, with no percentage set.

## The taxable base

**Arm's length principle.** Terms in a related-party dealing must be substantially the same as independent parties would agree in comparable dealings (art. 63(1) CIRC; Portaria art. 1(1)). The analysis is dealing by dealing, except where dealings are so closely linked or continuous that splitting them loses meaning, such as continuous supply of goods or services, licences bundled with other services, or a product line (Portaria art. 1(2)). The terms that count are the ones actually practised, even where they differ from the contract (Portaria art. 4(3)).

**Methods (art. 63(3) CIRC; Portaria art. 6).** The taxpayer must use one of:

1. Comparable uncontrolled price, resale price, cost plus, profit split or transactional net margin method.
2. Another generally accepted method, technique or valuation model, only where none of those can be used because the dealing is unique or reliable comparables are missing, especially for real estate rights, unlisted shares, receivables and intangibles. The choice must be documented with reasons (Portaria art. 6(4)).

There is no fixed order among the five methods. The taxpayer must use the most appropriate method: the one that gives the highest degree of comparability, has the best and most information, and needs the fewest adjustments (Portaria art. 6(2)).

**Ranges.** If comparables give a range with high comparability and the related-party price or margin falls inside it, no correction is needed (Portaria art. 6(5)). If the AT corrects, the correction should as a rule be to the median of the range (Portaria art. 6(6)).

**Intra-group services (Portaria art. 14).** A charge is deductible only for a service with economic value that the recipient would pay an independent party for, or would do for itself. The comparable price method is the most appropriate where the service is the same as services between independent parties. A cost-based method, especially cost plus, applies where price data is lacking. The charge must include an appropriate profit margin, except where the provider only buys services from third parties as agent for the group. Use direct charging where costs can be identified; otherwise allocate total costs with a key that reflects use (sales, gross margin, staff costs, units). Shareholder costs and costs already charged directly are excluded from the pool.

**Cost-sharing, intangibles, restructurings.** Portaria arts. 13, 15 and 16 set the rules; art. 18 and annexes III and IV list what the file must contain for cost-sharing and services.

**Primary adjustment by the taxpayer.** Where a dealing with a non-resident is not at arm's length, the company must make a positive correction in the Modelo 22 (art. 63(8) CIRC; Portaria art. 3(1)). The correction goes to the period or periods in which the dealing affects taxable profit (art. 63(10); Portaria art. 3(4)). The rule only runs upward: there is no self-made downward correction.

**Correction by the AT.** The AT may correct taxable profit to what it would have been under market conditions (art. 63(9)).

**Corresponding adjustment.** Where the AT corrects one Portuguese taxpayer, it must make the matching adjustment at the other Portuguese related taxpayer (art. 63(13); Portaria art. 20(1)), within 180 days of the correction becoming final (Portaria art. 23(2)). Where a foreign authority corrects, art. 63(14) lets the AT make the matching adjustment where a treaty signed by Portugal provides for it; Portaria art. 20(2) adds the dispute procedures of Lei 120/2019. Either way it comes through a mutual agreement procedure (Portaria art. 21). The AT then adjusts within 120 days of the taxpayer accepting the outcome and refunds within 90 days of the adjustment (Portaria arts. 23(3) and 25).

**Advance pricing agreements (art. 138 CIRC; Portaria 267/2021).** A taxpayer may ask the AT to agree in advance the method for its related-party dealings, including services, cost-sharing and head office to PE dealings. It can be unilateral, or bilateral or multilateral through the mutual agreement procedure with a treaty partner (art. 138(2)). The agreement lasts at most 4 years (art. 138(6)), binds the AT while law and facts do not change (art. 138(7)), and cannot be appealed by the taxpayer (art. 138(8)). The AT has 180 days to evaluate a unilateral proposal and 360 days for a bilateral or multilateral one, counted from formal acceptance (Portaria 267/2021 art. 11). The fee is paid within 30 days of the notice that the proposal is accepted (Portaria 267/2021 art. 18(3)).

## Deadlines and filing

| Obligation | Deadline | Source |
|---|---|---|
| Self-adjustment for non-arm's length dealings with non-residents | in the Modelo 22: by the last day of May for a calendar year, or the last day of the 5th month after year-end | art. 63(8) and art. 120(1) and (2) CIRC |
| Transfer pricing file (Dossier Principal plus Dossier Específico, delivered together) | prepared ("constituído") by the IES deadline: 15 July for a calendar year, or the 15th day of the 7th month after year-end | art. 130(1) and art. 121(2) and (3) CIRC; Portaria art. 17(2) and (9) |
| Hand the file to the AT: companies followed by the Large Taxpayers Unit | by the IES deadline, without being asked | art. 130(3) CIRC |
| Hand the file to the AT: everyone else | when notified | art. 130(5) CIRC |
| Keep the tax documentation file | 10 years | art. 130(1) CIRC |
| Disclose related-party dealings: the parties, amount and type of each dealing, methods and changes, corrections made, and whether the file was prepared at the time | in the IES, same deadline | art. 63(7) and art. 121 CIRC |
| Country-by-country report by the reporting entity | within 12 months after the last day of the group's reporting period | art. 121-A(3) CIRC |
| Country-by-country notification by every Portuguese group entity or PE: whether it is the reporting entity, or who is and where | by the Modelo 22 deadline (art. 120(1) and (2)) | art. 121-A(4) CIRC |

The file must sit in Portugal, or with the fiscal representative where the taxpayer has no seat, management or PE here (art. 130(2)). Foreign-language documents must be translated into Portuguese when handed over, unless the AT waives it (Portaria art. 17(14)). Third-party studies need a statement of responsibility from their author (art. 17(15)), and the AT can ask for access to the comparables databases (art. 17(16)).

A Portuguese entity that is not the ultimate parent must file the country-by-country report itself where the parent is not required to file one, where there is no qualifying exchange agreement in force with the parent's country, or where the AT has notified a systemic failure in that country (art. 121-A(2)). Filing through a surrogate parent can lift this (art. 121-A(9)).

## Penalties and interest

| Failure | Fine | Source |
|---|---|---|
| Not presenting the transfer pricing documentation; not filing on time the country-by-country notification or the country-by-country report | EUR 500 to EUR 10,000, plus 5% for each day of delay; EUR 1,000 to EUR 20,000 for a company after the doubling in RGIT art. 26(4) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/rgit/Pages/rgit117.aspx (RGIT art. 117(6)) |
| Omissions or inaccuracies in returns or other tax documents that do not amount to fraud | EUR 375 to EUR 22,500 (EUR 750 to EUR 45,000 for a company after the doubling in RGIT art. 26(4)); one quarter of those limits where no tax is due | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/rgit/Pages/rgit119.aspx (RGIT art. 119(1) and (2)) |
| Fine limits for a company | the minimum and maximum of each fine are doubled for a legal person | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/rgit/Pages/rgit26.aspx (RGIT art. 26(4)) |
| Compensatory interest on tax assessed late through the taxpayer's fault | counted daily from the return deadline; rate equal to the legal interest rate under art. 559(1) of the Civil Code | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/lgt/Pages/lgt35.aspx (LGT art. 35) |

A transfer pricing correction also brings the extra IRC and derrama estadual it causes (see the examples). An APA proposal can be refused if the fee is not paid (Portaria 267/2021 art. 7(3)).

## Cross-border points

**Mutual agreement procedure.** To remove double taxation after a foreign correction, the company applies to the Director-General of the AT under the relevant treaty, or under Lei 120/2019 for disputes with other EU Member States (Portaria art. 21). The application needs the parties, periods, facts, the rules relied on, the assessment that causes double taxation, and a written commitment to cooperate (Portaria art. 21(3)). Acceptance depends on proof of double taxation, a timely application, cooperation and the other state agreeing to consult (Portaria art. 22).

**EU disputes (Lei 120/2019, transposing Directive (EU) 2017/1852).** A complaint goes to the Portuguese and the other states' competent authorities at the same time, within 3 years of the first official notice of the action causing the dispute (Lei 120/2019 art. 3(2) and (3)). Once accepted, the mutual agreement procedure must end within 2 years of the last acceptance notice, extendable by up to 1 year (art. 8(2) and (3)). If it fails, the law provides for an advisory commission (Comissão Consultiva, art. 10 onwards).

**EU Arbitration Convention.** Not covered here: no official Portuguese page for it was read for this skill.

**Secondary adjustments.** Neither article 63 CIRC nor Portaria 268/2021 contains a secondary adjustment rule (a deemed dividend or loan for the cash that left the company). Whether other provisions recharacterise the excess payment is not covered by this skill.

**Withholding.** The excess part of a service fee or interest paid to a non-resident can also raise withholding questions under the general IRC and treaty rules; see pt-corporate-tax.

## Worked examples

### Example 1: intra-group service fee above arm's length

A Portuguese company (calendar-year IRC period starting 1 January 2026) pays its foreign parent a management fee of EUR 600,000. The parent's cost of the services provided to the Portuguese company is EUR 400,000. The company's benchmarking study (cost plus method, Portaria art. 14(3)(b)) finds an arm's length range of mark-ups whose median is 5%. The 5% is the result of this invented study, not a rate set by law. The arm's length fee is EUR 420,000.

1. Excess fee: 600,000 minus 420,000 = EUR 180,000. The company adds this to taxable profit in the Modelo 22 (art. 63(8) CIRC).
2. Taxable profit before the correction is EUR 2,000,000; after, EUR 2,180,000. No losses are brought forward, so taxable income is the same.
3. Extra IRC at 19%: EUR 34,200. The company is not an SME or small mid cap, so the 15% band on the first EUR 50,000 (art. 87(2)) does not apply. The correction sits at the top of its profit in any case.
4. Extra derrama estadual. The derrama on the correction depends on the company's total taxable profit, because the bands in art. 87-A apply to the part of the whole profit above each threshold. This example assumes taxable profit of EUR 2,000,000 before the correction, so profit before and after lies between EUR 1,500,000 and EUR 7,500,000 and the whole EUR 180,000 falls in the 3% slice: EUR 5,400. With profit of EUR 1,000,000 before the correction, the profit after (EUR 1,180,000) would stay below EUR 1,500,000 and the extra derrama would be nil; with profit of EUR 7,400,000, EUR 100,000 would fall at 3% and EUR 80,000 at 5%.
5. Total extra tax: EUR 39,600, before derrama municipal, which depends on the municipality.

```oa-check
name: Example 1, management fee corrected to cost plus 5%, IRC 19% and derrama estadual 3%
inputs:
  fee_paid: 600000
  provider_cost: 400000
  markup: 0.05
  profit_before: 2000000
steps:
  - arm_length_fee: provider_cost * (1 + markup)
  - correction: fee_paid - arm_length_fee
  - profit_after: profit_before + correction
  - extra_irc: correction * 0.19
  - in_3pct_slice: min(profit_after, 7500000) - max(profit_before, 1500000)
  - extra_derrama_estadual: in_3pct_slice * 0.03
  - total_extra_tax: extra_irc + extra_derrama_estadual
expected:
  arm_length_fee: 420000
  correction: 180000
  profit_after: 2180000
  extra_irc: 34200
  in_3pct_slice: 180000
  extra_derrama_estadual: 5400
  total_extra_tax: 39600
```

### Example 2: does the company need a transfer pricing file?

A Portuguese company has total annual income of EUR 14,000,000 in 2026, so the EUR 10,000,000 exemption does not apply (Portaria art. 17(3)). Its related-party dealings in 2026 are with three group companies: EUR 60,000, EUR 85,000 and EUR 95,000.

1. Largest dealing per counterparty: EUR 95,000. That is not above EUR 100,000.
2. All related-party dealings together: EUR 240,000. That is not above EUR 500,000.
3. Both limits are met, so the documentation file exemption applies (Portaria art. 17(5)).

If the EUR 85,000 counterparty were resident in a listed preferential tax regime, the exemption would not cover it, and the company would need documentation for that dealing (art. 17(6)). Even when exempt, the company must still prove arm's length terms if the AT asks (art. 17(7)), and must still report the dealings in the IES (art. 63(7) CIRC).

```oa-check
name: Example 2, documentation exemption test, income EUR 14m, three counterparties
inputs:
  total_income: 14000000
  cp_a: 60000
  cp_b: 85000
  cp_c: 95000
steps:
  - income_over_10m: total_income - 10000000
  - largest_counterparty: max(cp_a, cp_b, cp_c)
  - headroom_per_counterparty: 100000 - largest_counterparty
  - total_related: cp_a + cp_b + cp_c
  - headroom_aggregate: 500000 - total_related
expected:
  income_over_10m: 4000000
  largest_counterparty: 95000
  headroom_per_counterparty: 5000
  total_related: 240000
  headroom_aggregate: 260000
```

Both headroom figures are zero or more, so the exemption applies. A negative figure on either would mean it does not.

## Ask the client first

1. Who holds the company's capital and votes, directly and indirectly, and which group entities, directors and family members does it deal with? This settles who is related under art. 63(4).
2. What was the company's total annual income in the period, and the value of the dealings with each related party? This settles the EUR 10,000,000 and EUR 100,000 / EUR 500,000 exemptions.
3. Is any related party resident in a country on the Portuguese list of preferential tax regimes? The exemptions do not apply to those dealings.
4. Is the company followed by the Large Taxpayers Unit, and is it an SME? This settles whether the file is handed in with the IES and whether the simplified file is enough.
5. Is the group's consolidated revenue EUR 750,000,000 or more, and which entity files the country-by-country report?
6. Are there written agreements, cost bases and benchmarking studies for each dealing, and how old are the studies (3-year limit)?

## Sources

| Source | URL | Read on |
|---|---|---|
| CIRC art. 63, transfer pricing | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc63.aspx | 2026-10-22 |
| CIRC art. 87, IRC rates, with Lei 64/2025 art. 3 transitional rates | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc87.aspx | 2026-10-22 |
| CIRC art. 87-A, derrama estadual | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc87a.aspx | 2026-10-22 |
| CIRC art. 120, Modelo 22 deadline | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc120.aspx | 2026-10-22 |
| CIRC art. 121, IES deadline | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc121.aspx | 2026-10-22 |
| CIRC art. 121-A, country-by-country report | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc121a.aspx | 2026-10-22 |
| CIRC art. 130, tax documentation file | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc130.aspx | 2026-10-22 |
| CIRC art. 138, advance pricing agreements | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc138.aspx | 2026-10-22 |
| Portaria 268/2021, transfer pricing regulation (AT copy; Diário da República n.º 230/2021, Série I) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/diplomas_legislativos/Documents/Portaria_268_2021.pdf | 2026-10-22 |
| Portaria 268/2021, Diário da República page | https://diariodarepublica.pt/dr/detalhe/portaria/268-2021-174969198 | 2026-10-22 |
| Portaria 267/2021, advance pricing agreement procedure (AT copy) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/diplomas_legislativos/Documents/Portaria_267_2021.pdf | 2026-10-22 |
| Lei 120/2019, EU tax dispute resolution (AT copy) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/diplomas_legislativos/Documents/Lei_120_2019.pdf | 2026-10-22 |
| RGIT art. 117, failure to present documents | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/rgit/Pages/rgit117.aspx | 2026-10-22 |
| RGIT art. 119, omissions and inaccuracies | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/rgit/Pages/rgit119.aspx | 2026-10-22 |
| RGIT art. 26, fine limits for companies | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/rgit/Pages/rgit26.aspx | 2026-10-22 |
| LGT art. 35, compensatory interest | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/lgt/Pages/lgt35.aspx | 2026-10-22 |

Not yet confirmed: whether the 2026 State Budget law (Orçamento do Estado 2026) touched any rule here (its text was not read; the consolidated CIRC pages read on 2026-10-22 show no 2025 or 2026 change to arts. 63, 87-A, 121-A, 130 or 138, and art. 87 shows Lei 64/2025 as the last change); the APA fee amounts in Portaria 923/99 (not read); which IES annex and table carries the art. 63(7) disclosure for 2026 filings (the current IES instructions were not read); the legal interest rate under art. 559 of the Civil Code that sets compensatory interest; the base of the "5% for each day of delay" in RGIT art. 117(6) (the text does not say 5% of what); the SME size tests in the annex to Decree-Law 372/2007; and the Madeira and Azores rates, which are outside this skill.

> Contributed by Ryan Duguid.

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
