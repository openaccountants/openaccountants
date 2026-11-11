---
name: colombia-cross-border
description: >
  Colombian cross-border income tax for año gravable 2026: who must withhold on payments to non-residents (ET art. 406),
  Colombian-source income (art. 24), the art. 408 withholding rates (20% on interest, fees, royalties, rents, services,
  technical services and consulting; 15% on loans of a year or more and leasing; 1% on aircraft and ship leasing and
  reinsurance; 5% on 8-year infrastructure loans; 33% on management fees; 10% for significant economic presence; 35%
  to non-cooperative or preferential regimes), dividends to non-residents (art. 245: 20%, with 35% first on untaxed
  profits), non-resident individuals at 35% (art. 247), when a non-resident need not file (art. 592(2)), permanent
  establishments and branches (arts. 20-1, 20-2), significant economic presence (art. 20-3: 31,300 UVT, the 3% option),
  deductibility of payments abroad (arts. 121, 122, 124), the foreign tax credit (art. 254), treaty relief and Form 350.
  Trigger on: retención en la fuente pagos al exterior, dividendos no residentes, presencia económica significativa,
  PES 3%, establecimiento permanente Colombia, convenio doble imposición Colombia, Colombian withholding tax.
  Out of scope: transfer pricing (colombia-transfer-pricing), IVA on imported services (co-vat-return).
version: 1.0
jurisdiction: CO
category: cross-border
tax_year: 2026
last_updated: 2026-11-11
type: computation
tier: 2
domain: cross-border
---

# Colombia: cross-border income tax, año gravable 2026 v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

**Year.** Año gravable 2026 (calendar year). Withholding is monthly; thresholds are in UVT, and one UVT in 2026 is **COP 52,374** (DIAN Resolución 000238 of 15 December 2025).

**Which law.** The Estatuto Tributario (ET) as consolidated on the Senate's official site (last updated there 15 October 2026), arts. 20-1 to 20-3, 24, 121, 122, 124, 240, 245, 247, 254, 406 to 409 and 592, and the Decreto Único Reglamentario 1625 de 2016 (DUR) on DIAN's normograma. Treaties prevail where they apply (arts. 20-1 and 20-3 par. 4).

Related Colombia skills, linked rather than repeated:

- [co-corporate-income-tax](co-corporate-income-tax.md): the 35% corporate rate, dividends between Colombian companies (art. 242-1) and the Form 110 return.
- [colombia-income-tax](colombia-income-tax.md): residence of individuals (art. 10) and resident taxation of foreign income.
- [colombia-transfer-pricing](colombia-transfer-pricing.md): pricing of transactions with related parties abroad.
- [co-vat-return](co-vat-return.md): IVA on services from abroad and digital services, which is separate from the income tax rules here.

## Who this applies to

- **Colombian payers** (companies, individuals who are withholding agents, branches) that pay or credit Colombian-source income to **foreign companies or entities without domicile in Colombia, non-resident foreign individuals, or estates of non-resident foreigners** (art. 406). They withhold, file and pay.
- **Non-residents** with Colombian-source income: taxed only on that income, mostly through withholding. A non-resident whose entire income bore the withholding of arts. 407 to 411 (and any remittance withholding) does not file a return (art. 592(2)).
- **Foreign companies with a permanent establishment or branch in Colombia**: taxpayers on the Colombian-source income attributable to it (art. 20-2).
- **Foreign sellers with significant economic presence (SEP)** selling goods or digital services to customers in Colombia (art. 20-3).
- **Colombian residents with foreign income**: the foreign tax credit (art. 254).
- **Out of scope:** CFC rules (ECE), indirect transfers of Colombian assets, the foreign-assets return, the wealth tax, treaty-by-treaty rates, and IVA.

## Rates, bands and thresholds

| Item | Rate | Year | Source URL |
|---|---|---|---|
| UVT | COP 52,374 | 2026 | https://normograma.dian.gov.co/dian/compilacion/docs/resolucion_dian_0238_2025.htm |
| Interest, commissions, fees, royalties, rents, personal services, industrial property, know-how, services, literary and artistic royalties, films, software, paid to non-residents | 20% of the nominal payment (art. 408) | 2026 | http://www.secretariasenado.gov.co/senado/basedoc/estatuto_tributario_pr016.html |
| Consulting, technical services and technical assistance by non-residents, in Colombia or from abroad | 20% (art. 408) | 2026 | same |
| Interest on foreign loans of 1 year or more; interest or financial cost in leasing with foreign companies | 15% on the interest or financial cost (art. 408) | 2026 | same |
| Leasing of ships, helicopters, aircraft and their parts with foreign companies | 1% (art. 408) | 2026 | same |
| Interest on loans of 8 years or more for public-private infrastructure (Ley 1508 de 2012) | 5% (art. 408) | 2026 | same |
| Reinsurance premiums ceded to non-residents | 1% (art. 408) | 2026 | same |
| Management or direction fees (art. 124) to non-residents | 33% (art. 408) | 2026 | same |
| Sales of goods and services by non-residents with SEP to customers in Colombia, not covered above | 10% of the total payment (art. 408, inciso 8); withheld by card issuers, payment gateways and other agents DIAN names (par. 2) | 2026 | same |
| Any taxable payment to a resident of a non-cooperative or low or no tax jurisdiction, or to a preferential regime | the general corporate rate, 35% (art. 408 par.; art. 240) | 2026 | same; http://www.secretariasenado.gov.co/senado/basedoc/estatuto_tributario_pr010.html |
| Dividends to foreign companies, non-resident individuals and non-resident estates | 20%, withheld on the gross payment (art. 245 and par. 2) | 2026 | http://www.secretariasenado.gov.co/senado/basedoc/estatuto_tributario_pr010.html |
| Dividends from profits that would have been taxed in the hands of a Colombian company (untaxed profits under arts. 48, 49) | the art. 240 rate (35%) first, then 20% on the remainder (art. 245 par. 1) | 2026 | same |
| Non-resident individuals, Colombian-source taxable income | 35% flat (art. 247) | 2026 | same |
| Foreign professors hired for up to 182 days by Colombian higher-education institutions | 7%, withheld (art. 247 par.) | 2026 | same |
| SEP: gross income test | 31,300 UVT (COP 1,639,306,200) or more from customers in Colombia in the prior or current year, with deliberate and systematic interaction (art. 20-3(1)) | 2026 | http://www.secretariasenado.gov.co/senado/basedoc/estatuto_tributario.html |
| SEP: presumption of interaction | 300,000 or more customers or users in Colombia, or prices shown or payment allowed in COP (art. 20-3 par. 1) | 2026 | same |
| SEP: optional filing rate | 3% of all gross income from goods and digital services sold to users in Colombia, on the income tax form; the 10% withholding can then be switched off on request (art. 20-3 par. 2) | 2026 | same |
| Payments abroad without withholding duty: cap on deduction | 15% of net income before those costs (art. 122) | 2026 | http://www.secretariasenado.gov.co/senado/basedoc/estatuto_tributario_pr005.html |

## The base

**Colombian-source income (art. 24).** Income from exploiting goods in Colombia and services performed in Colombia, permanently or not, with or without an establishment, and gains on goods located in Colombia when sold. It includes rents and gains on Colombian real estate; interest on credits held in or economically linked to Colombia (except short-term import credits and overdrafts); work performed in Colombia; royalties and know-how, and **technical assistance and technical services even when supplied from abroad** (nums. 7 and 8); dividends from Colombian companies; turnkey contracts (the whole contract value); reinsurance ceded abroad; and SEP sales to customers in Colombia (num. 17).

**Withholding, step by step (art. 406 ff.).**

1. Is the recipient a foreign company or entity without domicile in Colombia, or a non-resident foreign individual? If not, use domestic withholding.
2. Is the payment Colombian-source income (art. 24)? If not, no withholding.
3. Is the recipient in a non-cooperative, low-tax jurisdiction or preferential regime? Then 35% on any taxable payment (art. 408 par.).
4. Otherwise, find the concept in art. 408 (or art. 245 for dividends) and apply the rate to the **gross** amount.
5. Check whether a treaty in force with the recipient's country lowers the rate (see Cross-border points).
6. Declare and pay in the monthly Form 350 (section "Pagos exterior") by the NIT date (see Deadlines and filing).

**Dividends (art. 245).** The 20% rate applies to dividends from profits that were taxed at company level. For the part of a dividend paid from profits not taxed at company level (determined under arts. 48 and 49), the art. 240 corporate rate (35%) applies first, and the 20% then applies to what is left after that tax. Dividends from a Colombian company to another Colombian company follow art. 242-1 (see [co-corporate-income-tax](co-corporate-income-tax.md)).

**Permanent establishment (art. 20-1).** A fixed place of business in Colombia through which a foreign enterprise or non-resident carries on all or part of its business: branches, agencies, offices, factories, workshops, mines, quarries, oil and gas wells. A dependent agent who habitually concludes binding contracts also creates a PE. No PE through a genuinely independent broker or agent acting in the ordinary course (unless it works almost only for the enterprise on non-arm's-length terms), for purely auxiliary or preparatory activity, or for representative offices of foreign reinsurers. **Attribution (art. 20-2):** the PE or branch is taxed on the Colombian-source income attributable to it, by functions, assets, risks and personnel, with separate accounts backed by a study of those factors; the corporate rate is 35% (art. 240).

**Significant economic presence (art. 20-3).** A non-resident selling goods or the listed digital services (online advertising, digital content, streaming, data monetisation, intermediation platforms, digital subscriptions, cloud and data hosting, search engines and software, intangibles, and other digital services) to customers in Colombia is taxable if it interacts deliberately and systematically with the Colombian market and earns 31,300 UVT or more from Colombian customers in the prior or current year. The test is applied on an aggregated basis for related parties (par. 3). Treaties prevail (par. 4). The default is 10% withholding by the payer or payment intermediary (art. 408); the non-resident may instead file and pay 3% of all gross income from Colombian users (par. 2). SEP non-residents have no other formal duties of residents (par. 7). In force since 1 January 2024 (par. 8).

**Deducting payments abroad (arts. 121, 122, 124).** A payment abroad is deductible only if tax was withheld where it is taxable income for the recipient in Colombia (art. 121). Costs abroad on which no withholding is due are capped at 15% of net income before those costs, except purchases of tangible goods, payments under legal obligations and the other cases listed (art. 122). Management fees and intangibles paid by a Colombian subsidiary or branch to its foreign head office are deductible only with withholding (art. 124).

**Foreign tax credit for residents (art. 254).** Foreign income tax on foreign-source income is credited up to the Colombian tax on that income, computed net of its costs. For dividends from foreign companies held directly as fixed assets, the credit is the dividend times the effective tax rate of the profits that paid it, plus any withholding on the dividend, capped at the Colombian tax on it, and proved with a foreign tax certificate and an auditor's certificate. See [co-corporate-income-tax](co-corporate-income-tax.md) for where it goes on Form 110.

## Deadlines and filing

| What | When | How | Source |
|---|---|---|---|
| Withholding on payments abroad | monthly, with all other withholding: by the 7th to 16th business day of the next month by the last digit of the payer's NIT (1: 7th ... 0: 16th); December's in January | Form 350, section "Pagos exterior" on page two (DIAN Resolución 000031 de 2024, art. 1 par. 2) | DUR art. 1.6.1.13.2.33 |
| Non-resident taxed fully by withholding | no return | none | art. 592(2) |
| PE or branch | yearly income tax return, as for companies | Form 110; see [co-corporate-income-tax](co-corporate-income-tax.md) | art. 20-2 |
| SEP non-resident choosing 3% | on the income tax form | return; may ask for the 10% withholding not to apply | art. 20-3 par. 2 |

## Penalties and interest

- **No withholding made:** the payment abroad is not deductible (arts. 121, 124). The withholding agent's own liability for tax not withheld is outside this skill (see Not yet confirmed).
- **Late Form 350 or late payment:** the general late filing penalty (art. 641) and late payment interest (arts. 634, 635), as set out in [co-corporate-income-tax](co-corporate-income-tax.md).
- **Inaccuracy:** art. 648, same skill.

## Cross-border points

- **Treaties.** Arts. 20-1 and 20-3 apply "sin perjuicio" of the double tax treaties Colombia has signed; a treaty in force with the recipient's country can reduce or remove the art. 408 and art. 245 rates and narrow the PE and SEP rules. Get the recipient's tax residence certificate and read the treaty's dividend, interest, royalty, business profits and PE articles before applying a lower rate. This skill does not list treaties or their rates.
- **Mutual agreement and corresponding adjustments** (art. 260-6): see [colombia-transfer-pricing](colombia-transfer-pricing.md).
- **Becoming or ceasing to be resident**: art. 10, in [colombia-income-tax](colombia-income-tax.md).

## Two worked examples that recompute

### Example 1: a Colombian SAS pays its foreign parent

Montaña SAS pays its parent, a company in a country with **no treaty** with Colombia and not on the tax-haven list, during 2026: technical assistance COP 100,000,000; interest of COP 50,000,000 on a 3-year loan; management fees COP 30,000,000; and a dividend of COP 1,000,000,000, of which COP 600,000,000 comes from taxed profits and COP 400,000,000 from profits not taxed at company level (art. 49).

- Technical assistance: 20% = 20,000,000.
- Interest on a loan of a year or more: 15% = 7,500,000.
- Management fees: 33% = 9,900,000.
- Dividend from taxed profits: 20% x 600,000,000 = 120,000,000.
- Dividend from untaxed profits: 35% x 400,000,000 = 140,000,000; then 20% x 260,000,000 = 52,000,000; total 192,000,000.
- Total withheld: **COP 349,400,000**, declared on Form 350 ("Pagos exterior") in the month of each payment or credit.

```oa-check
name: CO cross-border 2026, outbound payments to a non-treaty parent
inputs:
  technical: 100000000
  interest: 50000000
  management: 30000000
  div_taxed: 600000000
  div_untaxed: 400000000
steps:
  - wht_technical: technical * 0.20
  - wht_interest: interest * 0.15
  - wht_management: management * 0.33
  - wht_div_taxed: div_taxed * 0.20
  - first_35: div_untaxed * 0.35
  - wht_div_untaxed: first_35 + (div_untaxed - first_35) * 0.20
  - total: wht_technical + wht_interest + wht_management + wht_div_taxed + wht_div_untaxed
expected:
  wht_technical: 20000000
  wht_interest: 7500000
  wht_management: 9900000
  wht_div_taxed: 120000000
  wht_div_untaxed: 192000000
  total: 349400000
```

### Example 2: a foreign streaming service, 10% withholding or the 3% return (a decision)

A non-resident streaming company, no PE in Colombia, prices in COP and earns COP 5,000,000,000 in 2026 from Colombian subscribers, collected through card issuers and payment gateways. Its home country has no treaty with Colombia.

- SEP test: 5,000,000,000 is above 31,300 UVT (COP 1,639,306,200), and showing prices in COP is presumed deliberate and systematic interaction. It is taxable under art. 20-3.
- **Option A, default:** 10% withheld by the card issuers and gateways = **COP 500,000,000**.
- **Option B, elect to file:** 3% of gross income from Colombian users = **COP 150,000,000**, on the income tax form, after asking that the 10% withholding not be applied.
- **What decides it:** the 3% option costs COP 350,000,000 less on these figures, against the cost of filing a Colombian return. Withholding already suffered before the request is a separate question (see Not yet confirmed).

```oa-check
name: CO cross-border 2026, SEP streaming, 10% withholding or 3% election
inputs:
  uvt: 52374
  gross_colombia: 5000000000
steps:
  - sep_threshold: 31300 * uvt
  - margin_over_threshold: gross_colombia - sep_threshold
  - option_withholding: gross_colombia * 0.10
  - option_3pct: gross_colombia * 0.03
  - saving: option_withholding - option_3pct
expected:
  sep_threshold: 1639306200
  margin_over_threshold: 3360693800
  option_withholding: 500000000
  option_3pct: 150000000
  saving: 350000000
```

## Ask the client first

1. Who is paid: a company or an individual, resident where, with or without a PE or branch in Colombia, and is the country on Colombia's list of non-cooperative or low-tax jurisdictions?
2. What is paid, exactly: services (technical or not, performed where), interest (loan term), royalties, rent, management fees, dividends (taxed or untaxed profits under art. 49), or sales of goods or digital services.
3. Is there a treaty in force with the recipient's country, and does the recipient hold a tax residence certificate?
4. For a foreign seller: Colombian gross income in 2025 and 2026, number of Colombian users, and whether prices or payment are in COP.
5. The payer's NIT (Form 350 dates) and whether the payment is to a related party (transfer pricing).
6. For a resident with foreign income: the foreign tax paid, the certificates, and for foreign dividends, the holding and the foreign company's effective rate.

## Sources

| Source | URL | Read on |
|---|---|---|
| DIAN Resolución 000238 de 2025 (UVT 2026 = COP 52,374) | https://normograma.dian.gov.co/dian/compilacion/docs/resolucion_dian_0238_2025.htm | 2026-11-11 |
| Estatuto Tributario arts. 20-1, 20-2, 20-3 (PE, branches, SEP), Senate consolidated text updated 15 Oct 2026 | http://www.secretariasenado.gov.co/senado/basedoc/estatuto_tributario.html | 2026-11-11 |
| ET art. 24 (Colombian-source income) | http://www.secretariasenado.gov.co/senado/basedoc/estatuto_tributario_pr001.html | 2026-11-11 |
| ET arts. 121, 122, 124 (payments abroad) | http://www.secretariasenado.gov.co/senado/basedoc/estatuto_tributario_pr005.html | 2026-11-11 |
| ET arts. 240, 245, 247, 254 (corporate rate, dividends, non-resident individuals, foreign tax credit) | http://www.secretariasenado.gov.co/senado/basedoc/estatuto_tributario_pr010.html | 2026-11-11 |
| ET arts. 406, 407, 408, 409 (withholding on payments to non-residents) | http://www.secretariasenado.gov.co/senado/basedoc/estatuto_tributario_pr016.html | 2026-11-11 |
| ET art. 592 (who need not file) | http://www.secretariasenado.gov.co/senado/basedoc/estatuto_tributario_pr024.html | 2026-11-11 |
| DUR 1625 de 2016, art. 1.6.1.13.2.33 (Form 350 dates), DIAN normograma | https://normograma.dian.gov.co/dian/compilacion/docs/decreto_1625_2016.htm | 2026-11-11 |
| DIAN Resolución 000031 de 2024, art. 1 and par. 2 (Form 350, "Pagos exterior") | https://normograma.dian.gov.co/dian/compilacion/docs/resolucion_dian_0031_2024.htm | 2026-11-11 |

Not yet confirmed: the list of double tax treaties in force and their rates (DIAN's treaty page was not read); the current list of non-cooperative and low-tax jurisdictions (DUR art. 1.2.2.5.1); how the 10% SEP withholding already suffered is credited when the 3% option is chosen, and the DUR rules on the SEP return and its dates; the "remesas" tax mentioned in arts. 124 and 592 (it is noted on the page as a former tax); art. 409's 4-month rule for foreign professors against art. 247's 182 days (both appear on the page; this skill uses art. 247); the Andean Community regime (Decisión 578); the withholding agent's liability for tax not withheld; the art. 49 calculation of the untaxed part of a dividend.
