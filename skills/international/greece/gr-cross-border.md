---
name: gr-cross-border
description: "Greece cross-border tax for tax year 2026 (calendar year). Covers tax residence tests for individuals (home, centre of vital interests, more than 183 days in any 12 months) and companies (Greek incorporation, registered seat, place of effective management); arriving under the special inbound regimes (art. 5A EUR 100,000 lump sum for high-net-worth movers, art. 5B 7% flat tax on foreign income of pensioners, art. 5C 50% exemption on Greek employment or business income for 7 years); leaving (deregistration procedure, the company exit tax of art. 66A); non-residents with Greek-source income such as rent or salary; withholding on outbound dividends, interest, royalties and fees, with the EU directive exemptions; treaty relief and the foreign tax credit. Trigger phrases: moving to Greece, leaving Greece, non-resident, expat, exit tax, digital nomad, Greek non-dom, 5A 5B 5C, golden visa tax. Out of scope: self-employed income tax (gr-income-tax), company tax (gr-corporate-income-tax), EFKA contributions (gr-efka), VAT (gr-vat-return)."
jurisdiction: GR
category: cross-border
tax_year: 2026
tier: 2
last_updated: 2026-10-22
version: 0.1
verified_by: pending
---

# Greece: cross-border tax (arriving, leaving, non-residents, withholding)

This is the hub skill for anyone or any company crossing the Greek border. It sets out the residence tests, the three inbound regimes, what leaving involves, how non-residents are taxed on Greek income, and the withholding rates on payments abroad. It links to the pack's other skills for the detail of each tax:

- Self-employed income tax, presumptive income, prepayments: `gr-income-tax`
- Company income tax: `gr-corporate-income-tax`
- EFKA social contributions for the self-employed: `gr-efka`
- VAT: `gr-vat-return`
- Overview of the system: `gr-tax-overview`

The law is the Income Tax Code (Κώδικας Φορολογίας Εισοδήματος, ΚΦΕ, ν. 4172/2013). We read the Ministry of Finance's administrative codification of the Code, which includes amendments up to ν. 5264/2025 (Α' 239/19.12.2025), published April 2026. Procedure, fines and interest are in the Tax Procedure Code (Κώδικας Φορολογικής Διαδικασίας, ΚΦΔ, ν. 5104/2024), read in the AADE codification circular Ε.2109/2025, which includes amendments up to ν. 5259/2025. Greece's tax authority is AADE (Independent Authority for Public Revenue). The tax year is the calendar year.

## Who this applies to

**Individuals (art. 4 ΚΦΕ).** A person is Greek tax resident if:

1. their permanent or principal residence, their habitual abode, or the centre of their vital interests (personal and economic ties) is in Greece; or
2. they are a Greek national serving abroad as a consular, diplomatic or similar public official or civil servant.

A person who is in Greece for more than 183 days in total in any 12-month period is resident from the first day of their presence in Greece. The day test does not apply to someone in Greece only for tourism, medical treatment or similar private reasons whose stay does not exceed 365 days, including short periods abroad (art. 4(2)).

There is no split-year rule in the Code. Residence starts from the first day of presence once the 183-day test is met. The move out of Greece follows the AADE deregistration procedure described under "Deadlines and filing".

**Companies and other legal entities (art. 4(3) and (4) ΚΦΕ).** An entity is Greek tax resident for a tax year if any one of these applies:

1. it was incorporated or formed under Greek law;
2. its registered seat is in Greece; or
3. its place of effective management is in Greece at any time during the tax year.

Place of effective management is judged on the facts, in particular: where day-to-day management happens, where strategic decisions are taken, where the annual general meeting is held, where the books are kept, where the board (or other executive body) meets, and where the board members live. The residence of the majority of shareholders can also be taken into account alongside these factors.

**Who is in scope here.** Anyone moving to or from Greece, a non-resident with Greek-source income, a Greek payer making payments abroad, and a Greek company moving its residence, assets or a permanent establishment out of Greece.

## Rates, bands and thresholds

| Item | Figure | Tax year | Source |
|---|---|---|---|
| Scale for employment, pension and business income: EUR 0 to 10,000 | 9% | 2026 | ΚΦΕ art. 15(1)(a), as replaced by ν. 5246/2025 art. 3(1), [ΚΦΕ codification](https://minfin.gov.gr/wp-content/uploads/2026/04/%CE%9A%CE%A9%CE%94%CE%99%CE%9A%CE%9F%CE%A0%CE%9F%CE%99%CE%97%CE%A3%CE%97-%CE%A4%CE%9F%CE%A5-%CE%9A%CE%A9%CE%94%CE%99%CE%9A%CE%91-%CE%A6%CE%9F%CE%A1%CE%9F%CE%9B%CE%9F%CE%93%CE%99%CE%91%CE%A3-%CE%95%CE%99%CE%A3%CE%9F%CE%94%CE%97%CE%9C%CE%91%CE%A4%CE%9F%CE%A3-%CE%9C%CE%95%CE%A7%CE%A1%CE%99-%CE%A4%CE%9F-%CE%9D-5264-2025.pdf) |
| EUR 10,000.01 to 20,000 | 20% | 2026 | same |
| EUR 20,000.01 to 30,000 | 26% | 2026 | same |
| EUR 30,000.01 to 40,000 | 34% | 2026 | same |
| EUR 40,000.01 to 60,000 | 39% | 2026 | same |
| Over EUR 60,000 | 44% | 2026 | same |
| Lower rates on the 2nd and 3rd bands for taxpayers with dependent children, and 0% or 9% on the first EUR 20,000 for taxpayers up to 25 or aged 26 to 30 | see art. 15(1)(b) to (e) | 2026 | same |
| Rental income from Greek property: EUR 0 to 12,000 | 15% | 2026 | ΚΦΕ art. 40(4), as amended by ν. 5246/2025 art. 8, same |
| Rental income: EUR 12,000.01 to 24,000 | 25% | 2026 | same |
| Rental income: EUR 24,000.01 to 36,000 | 35% | 2026 | same |
| Rental income: over EUR 36,000 | 45% | 2026 | same |
| Art. 5A lump-sum tax on all foreign income (high-net-worth movers) | EUR 100,000 a year, for up to 15 tax years | 2026 | ΚΦΕ art. 5A(2) and (4), same; [AADE guide, 12.11.2025](https://aade.gr/sites/default/files/2025-11/forologika_kinitra.pdf) |
| Art. 5A extension to each relative (spouse or civil partner, ascendants, descendants) | EUR 20,000 a year per relative | 2026 | ΚΦΕ art. 5A(2), same |
| Art. 5A minimum Greek investment (not needed if the person holds an investor residence permit under art. 16 ν. 4251/2014) | EUR 500,000, completed within 3 years of the application | 2026 | ΚΦΕ art. 5A(1)(b), same |
| Art. 5B flat tax on all foreign income of a pensioner | 7% a year, for up to 15 tax years | 2026 | ΚΦΕ art. 5B(2) and (4), same |
| Art. 5C exemption on Greek employment or business income | 50% of that income exempt from income tax, for 7 tax years | 2026 | ΚΦΕ art. 5C(2), (4) and (7), same |
| Corporate income tax rate (also the rate of the company exit tax) | 22% | 2021 onwards, so 2026 | ΚΦΕ art. 58(1)(a) and art. 66A(2), same |
| Withholding on dividends | 5% | 2026 | ΚΦΕ art. 64(1)(a), same |
| Withholding on interest | 15% | 2026 | ΚΦΕ art. 64(1)(b), same |
| Withholding on royalties and other payments | 20% | 2026 | ΚΦΕ art. 64(1)(c), same |
| Withholding on fees for technical, management, consulting and similar services | 20% | 2026 | ΚΦΕ art. 64(1)(d), same |
| Dividends to an EU parent (Parent-Subsidiary Directive) | 0% if holding at least 10% for at least 24 months | 2026 | ΚΦΕ art. 63(1), same |
| Interest and royalties to an associated EU company (Interest and Royalties Directive) | 0% if holding at least 25% for at least 24 months | 2026 | ΚΦΕ art. 63(2), same |

## The taxable base

**Residents are taxed on worldwide income; non-residents only on Greek-source income** (art. 3 ΚΦΕ, as AADE states on its [non-resident](https://aade.gr/en/greeks-abroad-non-residents/income-taxation/taxation-greek-sourced-income-obtained-non-residents-pit) and [resident](https://aade.gr/en/greeks-abroad-non-residents/income-taxation/taxation-non-greek-sourced-income-obtained-greek-tax-residents-pit) pages). There is no remittance basis. Greek-source income (art. 5(1)) includes employment exercised in Greece, Greek state and Greek fund pensions, business carried on through a Greek permanent establishment, rent from property in Greece, gains on Greek property, and the other categories listed in art. 5(1).

**Non-residents and tax reductions (art. 20).** A non-resident does not get the tax reductions of arts. 16 to 19 (for example the employment and pension tax reduction of art. 16), unless they are resident in another EU or EEA state and either (a) at least 90% of their worldwide income arises in Greece, or (b) they show their taxable income is low enough that they would get the reduction under their home state's law.

**Art. 5A, high-net-worth movers.** All conditions must be met:

1. not Greek tax resident in 7 of the 8 years before the move;
2. an investment of at least EUR 500,000 in Greek real estate, businesses, securities or shares in Greek entities, made by the person, a relative or a company they control by majority, completed within 3 years of the application (AADE says investments count from 12.12.2019). This condition does not apply to a person who holds an investor residence permit under art. 16 ν. 4251/2014.

The lump sum covers all foreign income, whatever its amount. Foreign income under the regime is not declared (art. 67(1)). Greek-source income is taxed under the normal rules and declared. Foreign tax paid on covered income cannot be credited. Foreign movable property passing by inheritance or gift is exempt from Greek inheritance and gift tax. Failing to pay the full lump sum in any year ends the regime from that year, and the person is taxed on worldwide income. If the investment is not completed within 3 years, the regime is withdrawn from the first year (art. 5A(5)).

**Art. 5B, pensioners.** The conditions are that the person receives foreign pension income, was not Greek tax resident in 5 of the 6 years before the move, and moves from a state that has an administrative cooperation agreement on tax with Greece. The 7% applies to all foreign income, not only the pension. Both Greek and foreign income are declared on the return (art. 67(1)). Arts. 5A and 5B cannot be combined. Either can be combined with 5C if each article's conditions are met (AADE guide, section 4).

**Art. 5C, people moving to work or do business in Greece.** The conditions are:

1. not Greek tax resident in 5 of the 6 years before the move;
2. moving from an EU or EEA state, or from a state with an administrative cooperation agreement on tax with Greece;
3. working in Greece for a Greek entity or a Greek permanent establishment of a foreign business, or starting an individual business in Greece (art. 5C(7)); and
4. declaring an intention to stay in Greece for at least 2 years.

Half of the Greek employment or business income is exempt from income tax and from the special solidarity contribution of art. 43A, for 7 tax years in total. The regime cannot be extended beyond 7 years. If conditions 3 or 4 fail in any year, the regime ends from that year (art. 5C(5)). AADE adds that the person is also exempt from presumptive (deemed) living-expense income based on homes and cars for the 7 years. The regime also ends if employment or the business stops for more than 12 months, or the person moves residence abroad (AADE guide, section 3.3).

**Companies leaving: exit tax (art. 66A ΚΦΕ).** This applies only to Greek-resident legal persons and entities, and to permanent establishments in Greece. It does not apply to individuals; we found no exit charge for individuals in the consolidated Code. The charge is on market value minus tax value of assets when any of these happens:

1. assets move from the Greek head office to a permanent establishment abroad;
2. assets move from a Greek permanent establishment to the head office or another permanent establishment abroad;
3. the company moves its tax residence out of Greece (except assets that stay effectively connected with a Greek permanent establishment); or
4. the business of a Greek permanent establishment moves abroad.

In each case the charge applies only where Greece loses the right to tax the assets. It is taxed at the art. 58 rate for the year of exit (22%). Art. 66A implements art. 5 of the Anti-Tax Avoidance Directive (2016/1164/EU) and applies to transfers from 1.1.2020.

**Withholding scope (arts. 62 and 64).** Withholding applies to dividends, interest and royalties. It applies to fees for technical, management, consulting and similar services when the recipient is an individual, or a legal person resident outside Greece and outside the EU and EEA (art. 62(1)(d) and (3)). A legal person resident in Greece or in another EU or EEA state receiving those fees is not subject to withholding (art. 62(2)). A non-EU/EEA recipient of royalties or of those fees can elect to be taxed as Greek residents are and credit the tax withheld (art. 62(3)). Treaty rates override the domestic rate when the recipient gives a residence certificate.

## Deadlines and filing

| Event | Deadline | Source |
|---|---|---|
| Get a Greek tax number (AFM) as a non-resident, appointing a tax representative where required | Before the first Greek income or transaction; online via myAADE "TIN & Authentication Key" | [AADE: TIN for non-residents](https://aade.gr/en/greeks-abroad-non-residents/registration-tax-register/issuance-tax-identification-number-and-authentication-key-and-appointment) |
| Art. 5A application | By 31 March of the tax year (also open to people who moved in the previous tax year). AADE decides by the last working day of June | ΚΦΕ art. 5A(3) |
| Art. 5A lump sum | One payment by the last working day of July each year; first year within 30 days of approval | ΚΦΕ art. 5A(2) |
| Art. 5B application | By 31 March of the tax year (also open to people who moved in the previous tax year). The regime starts from the following tax year; AADE decides within 60 days | ΚΦΕ art. 5B(3) and (4) |
| Art. 5B tax | One payment by the last working day of July each year | ΚΦΕ art. 5B(2)(b) |
| Art. 5C application (online in myAADE) | Start of work by 2 July: apply by the end of that year, or during the following year, which then counts as the first year. Start after 2 July: apply for the following year, by the end of that year. AADE decides within 60 days | ΚΦΕ art. 5C(3); AADE guide, section 3.2 |
| Individual income tax return (residents, and non-residents with Greek-source income) | 15 March to 15 July of the year after the tax year; for 2026 income, in 2027 | ΚΦΕ art. 67(3); [AADE: filing obligations](https://aade.gr/en/greeks-abroad-non-residents/income-taxation/fulfillment-tax-obligations) |
| Move of tax residence out of Greece | Application by the last business day of the first ten days of March of the year after departure; supporting documents by the last business day of the first ten days of September; applications accepted until 31 December of that year | [AADE: transferring tax residency abroad](https://aade.gr/en/greeks-abroad-non-residents/income-taxation/transferring-tax-residency-greece-abroad) |
| Company exit tax return | 3 working days before the exit event. The tax is paid in one sum with the return, or in 5 equal annual interest-free instalments where the move is to an EU state or an EEA state with a tax-debt recovery assistance agreement. The first instalment is paid with the return and the rest by the last working day of each of the next 4 years | ΚΦΕ art. 66A(3) and (4) |

Non-residents earning only interest on Greek government bonds and T-bills, or on qualifying corporate bonds under art. 37(5), do not have to file a return (art. 67(1)).

## Penalties and interest

From the Tax Procedure Code (ν. 5104/2024), in the [AADE codification Ε.2109/2025](https://www.aade.gr/sites/default/files/2025-12/e2109_2025.pdf):

| Breach | Penalty | Source |
|---|---|---|
| Late or missing return with no tax due (includes a late income tax return) | EUR 100 per breach | ΚΦΔ art. 53(1) |
| Late or missing return, for a taxpayer keeping single-entry books | EUR 250 per breach | ΚΦΔ art. 53(2) |
| Late or missing return, for a taxpayer keeping double-entry books | EUR 500 per breach | ΚΦΔ art. 53(2) |
| No return filed where tax would be due (income tax, withholding and others) | 50% of the tax due on the missing return | ΚΦΔ art. 53(6) |
| A late original income tax return showing tax of EUR 100 or less | No fine under art. 53(1) or (2) | ΚΦΔ art. 53(7)(c) |
| Inaccurate return: tax difference 5% to 20% of the tax declared | 10% of the difference | ΚΦΔ art. 54(1)(a) |
| Tax difference over 20% and up to 50% | 25% of the difference | ΚΦΔ art. 54(1)(b) |
| Tax difference over 50% | 50% of the difference | ΚΦΔ art. 54(1)(c) |
| Inaccurate withholding tax return | 50% of the difference | ΚΦΔ art. 54(2) |
| Late payment | Interest from the day after the payment deadline. There is no interest on interest | ΚΦΔ art. 52(1) and (5) |

The late-payment interest rate is not set in art. 52. We did not read it on an official page today. See "Not yet confirmed".

For the inbound regimes, the sanction is losing the regime. Under 5A and 5B, failing to pay the full annual tax ends the regime from that year. Under 5A, an investment not completed within 3 years withdraws the regime from the first year.

## Cross-border points

**Treaties first.** Where Greece has a double tax treaty with the other state, the treaty decides which state may tax. The non-resident must give a tax residence certificate from their state to get treaty relief (AADE). Greek residents get an electronic residence certificate (e-TRC) through myAADE ([AADE: DTA forms](https://aade.gr/en/greeks-abroad-non-residents/income-taxation/forms-application-double-taxation-agreements)). For a person resident in both states under domestic law, the treaty tie-breaker decides residence. Check the specific treaty.

**Foreign tax credit, not exemption (art. 9 ΚΦΕ).** A Greek resident deducts foreign tax paid on foreign income from the Greek tax on that income. The credit cannot exceed the Greek tax on that income. Under art. 5A there is no credit for foreign tax on covered income. Art. 5B does not override treaties.

**Social security (EU/EEA and Switzerland).** Regulation (EC) 883/2004 means a person is subject to one state's social security legislation at a time, normally the state where they work (art. 11). An employee posted by their employer to another member state stays in the home system if the posting is expected to last no more than 24 months and they do not replace another posted worker (art. 12(1)). The self-employed have a parallel rule (art. 12(2)). The posting is shown by a form A1 from the home system (the A1 rules are in Regulation 987/2009; see "Not yet confirmed"). Someone who moves to Greece to work for a Greek employer under art. 5C normally joins the Greek system (e-EFKA). EFKA for the self-employed is in `gr-efka`. There is no employee or employer EFKA skill in the pack yet.

**Companies.** The 22% rate, deductions and filing are in `gr-corporate-income-tax`. Withholding on outbound dividends, interest, royalties and fees is set out above. The directive exemptions need the holding thresholds and the 24-month holding period. If the period is not yet complete, the payer may skip withholding by lodging a bank guarantee (art. 63(3)).

## Worked examples

### Example 1: engineer moving from Germany under art. 5C

Eleni is a German-resident engineer, aged 35, with no children. She has not been Greek tax resident in the last 6 years. She starts work for a Greek company in Athens on 1 March 2026 and declares she will stay for at least 2 years. She starts before 2 July, so she applies for 5C in myAADE by 31 December 2026, and 2026 is her first 5C year. Her 2026 Greek employment income, after employee social contributions, is EUR 70,000.

Under 5C, half (EUR 35,000) is exempt. The other EUR 35,000 is taxed on the 2026 scale: 9% on 10,000 (900), 20% on 10,000 (2,000), 26% on 10,000 (2,600) and 34% on 5,000 (1,700). Tax before the art. 16 reduction is EUR 7,200. Without 5C, tax on EUR 70,000 before the art. 16 reduction would be EUR 21,100. The regime saves EUR 13,900 in 2026 and can run for 7 tax years (2026 to 2032).

This example does not compute the art. 16 employment tax reduction, the employee EFKA contributions, or whether the special solidarity contribution applies in 2026.

```oa-check
name: Art. 5C mover, Greek salary EUR 70,000, 2026 scale, before art. 16 reduction
inputs:
  salary: 70000
  exempt_share: 0.5
steps:
  - taxable: salary * (1 - exempt_share)
  - b1: min(taxable, 10000) * 0.09
  - b2: max(min(taxable, 20000) - 10000, 0) * 0.20
  - b3: max(min(taxable, 30000) - 20000, 0) * 0.26
  - b4: max(min(taxable, 40000) - 30000, 0) * 0.34
  - b5: max(min(taxable, 60000) - 40000, 0) * 0.39
  - b6: max(taxable - 60000, 0) * 0.44
  - tax_5c: b1 + b2 + b3 + b4 + b5 + b6
  - f1: min(salary, 10000) * 0.09
  - f2: max(min(salary, 20000) - 10000, 0) * 0.20
  - f3: max(min(salary, 30000) - 20000, 0) * 0.26
  - f4: max(min(salary, 40000) - 30000, 0) * 0.34
  - f5: max(min(salary, 60000) - 40000, 0) * 0.39
  - f6: max(salary - 60000, 0) * 0.44
  - tax_normal: f1 + f2 + f3 + f4 + f5 + f6
  - saving: tax_normal - tax_5c
expected:
  taxable: 35000
  tax_5c: 7200.00
  tax_normal: 21100.00
  saving: 13900.00
```

### Example 2: non-resident with a rented flat in Athens

Klaus lives in Munich and is not Greek tax resident. He owns a flat in Athens. His 2026 taxable rental income from it is EUR 30,000. Rent from Greek property is Greek-source income (art. 5(1)), so he files a Greek return between 15 March and 15 July 2027. The rent is taxed separately on the art. 40(4) scale for 2026: 15% on 12,000 (1,800), 25% on 12,000 (3,000) and 35% on 6,000 (2,100). Greek tax is EUR 6,900.

As a non-resident he gets the art. 16 to 19 reductions only under the art. 20 EU/EEA test. Those reductions are tax reductions on other income and do not change this separate rental tax. How Germany treats the rent and relieves the Greek tax depends on the Greece-Germany treaty and German law; check both before advising.

```oa-check
name: Non-resident, Greek rental income EUR 30,000, 2026 rental scale
inputs:
  rent: 30000
steps:
  - r1: min(rent, 12000) * 0.15
  - r2: max(min(rent, 24000) - 12000, 0) * 0.25
  - r3: max(min(rent, 36000) - 24000, 0) * 0.35
  - r4: max(rent - 36000, 0) * 0.45
  - tax: r1 + r2 + r3 + r4
expected:
  tax: 6900.00
```

## Ask the client first

1. Where was the person tax resident in each of the last 8 years, and on what date did they arrive in or leave Greece? This decides residence and eligibility for 5A (7 of 8 years) and 5B or 5C (5 of 6 years).
2. Which state are they moving from? Is it an EU or EEA state, or a state with an administrative cooperation agreement on tax with Greece? This decides 5B and 5C.
3. What income do they have, where does it arise, and how much? Include salary, business income, pension, rent, dividends and gains. This decides which regime, if any, saves tax.
4. For 5C: when does the job or business start (before or after 2 July), who is the employer, and will they stay at least 2 years?
5. For 5A: what Greek investment has been made or is planned, when, and through whom? Do they hold an investor residence permit?
6. For a company: where do the board meet and decide, where are the books kept, and are any assets, the residence or a permanent establishment moving abroad? For outbound payments: who is the recipient, where are they resident, what is the holding, and since when?

## Sources

All read on 2026-10-22.

- Income Tax Code (ν. 4172/2013), Ministry of Finance administrative codification including amendments up to ν. 5264/2025 (circular 56053/06-04-2026): arts. 3, 4, 5, 5A, 5B, 5C, 9, 15, 20, 40, 58, 62, 63, 64, 66A, 67. https://minfin.gov.gr/wp-content/uploads/2026/04/%CE%9A%CE%A9%CE%94%CE%99%CE%9A%CE%9F%CE%A0%CE%9F%CE%99%CE%97%CE%A3%CE%97-%CE%A4%CE%9F%CE%A5-%CE%9A%CE%A9%CE%94%CE%99%CE%9A%CE%91-%CE%A6%CE%9F%CE%A1%CE%9F%CE%9B%CE%9F%CE%93%CE%99%CE%91%CE%A3-%CE%95%CE%99%CE%A3%CE%9F%CE%94%CE%97%CE%9C%CE%91%CE%A4%CE%9F%CE%A3-%CE%9C%CE%95%CE%A7%CE%A1%CE%99-%CE%A4%CE%9F-%CE%9D-5264-2025.pdf
- Ministry of Finance, notice of the codification of the Income Tax Code: https://minfin.gov.gr/koinopoiisi-kodikopoiisis-tou-kodika-forologias-eisodimatos-symfona-me-to-arthro-83-par-55-tou-n-5104-2024/
- AADE guide "Tax incentives to attract new tax residents, arts. 5A, 5B, 5C ΚΦΕ" (12 November 2025): https://aade.gr/sites/default/files/2025-11/forologika_kinitra.pdf
- AADE, tax incentives for new tax residents: https://www.aade.gr/omogeneis-katoikoi-exoterikoy/eisodima/forologika-kinitra-proselkysis-neon-forologikon-katoikon
- AADE, tax residence for natural persons: https://aade.gr/en/greeks-abroad-non-residents/income-taxation/tax-residence-natural-persons-itc
- AADE, taxation of Greek-sourced income of non-residents: https://aade.gr/en/greeks-abroad-non-residents/income-taxation/taxation-greek-sourced-income-obtained-non-residents-pit
- AADE, taxation of foreign income of Greek residents and the foreign tax credit: https://aade.gr/en/greeks-abroad-non-residents/income-taxation/taxation-non-greek-sourced-income-obtained-greek-tax-residents-pit
- AADE, transferring tax residency from Greece abroad: https://aade.gr/en/greeks-abroad-non-residents/income-taxation/transferring-tax-residency-greece-abroad
- AADE, fulfilment of tax obligations (who files): https://aade.gr/en/greeks-abroad-non-residents/income-taxation/fulfillment-tax-obligations
- AADE, forms for applying double taxation agreements: https://aade.gr/en/greeks-abroad-non-residents/income-taxation/forms-application-double-taxation-agreements
- AADE, TIN and tax representative for non-residents: https://aade.gr/en/greeks-abroad-non-residents/registration-tax-register/issuance-tax-identification-number-and-authentication-key-and-appointment
- Tax Procedure Code (ν. 5104/2024), AADE codification circular Ε.2109/30-12-2025, amendments up to ν. 5259/2025: arts. 52, 53, 54. https://www.aade.gr/sites/default/files/2025-12/e2109_2025.pdf
- Regulation (EC) No 883/2004, consolidated text, arts. 11 and 12: https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02004R0883-20190731

Note: AADE's English page "Income categories and income taxation in Greece" still shows the pre-2026 scale (9/22/28/36/44%). The 2026 scale in this skill is from the law text (art. 15 as replaced by ν. 5246/2025, applying from tax year 2026).

Not yet confirmed: the late-payment interest rate under ΚΦΔ art. 52 (set outside the Code; not read on an official page today); any amendments to the Income Tax Code after ν. 5264/2025 or to the Tax Procedure Code after ν. 5259/2025 made during 2026; the 2026 amounts of the art. 16 employment and pension tax reduction; whether the special solidarity contribution of art. 43A is charged for 2026; the deductions from gross rent that give taxable rental income; the A1 certificate rules in Regulation (EC) 987/2009; the list of states with an administrative cooperation agreement on tax with Greece; the Greece-Germany treaty treatment of rent in Example 2.
