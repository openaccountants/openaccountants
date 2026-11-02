---
name: pt-foreign-source-treaties
description: "Foreign income of Portuguese tax residents for tax year 2026: how Portugal taxes foreign pensions, salaries, dividends, interest, rent and gains, and how double taxation is relieved. Covers the foreign tax credit of CIRS art. 81 (lower of foreign and Portuguese tax, capped at the treaty rate), the 28% and 35% special rates for foreign capital income, aggregation at the 2026 art. 68 bands, currency conversion (art. 23), treaty exemption with progression, the IFICI exemption of art. 81(4) and why it does not cover pensions, the old NHR 10% pension rate kept only for NHR holders, Sweden (no treaty since 2022), Anexo J and the filing extension of art. 60(3). Trigger on: foreign income Portugal, foreign tax credit Portugal, crédito de imposto art. 81, Anexo J, pensão estrangeira, dividendos estrangeiros, CDT Portugal, IFICI foreign pension. Out of scope: pt-cross-border, pt-nhr-ifici, pt-irs-employees-investment, pt-income-tax, portugal-crypto-tax."
version: 0.2
jurisdiction: PT
tax_year: 2026
last_updated: 2026-10-31
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Portugal: foreign income of residents and double tax relief (tax year 2026)

This skill answers one question: a Portuguese tax resident has income from abroad in 2026, so how much Portuguese IRS is due on it, and how much credit is given for the foreign tax? The return is the Modelo 3 with Anexo J, filed between 1 April and 30 June 2027.

Sibling skills, which this one links to and does not repeat:

- `pt-cross-border`: whether the person is resident at all, split years, non-residents with Portuguese income, the exit tax and outbound withholding.
- `pt-nhr-ifici`: who holds the old non-habitual resident regime (NHR) or IFICI, registration, qualifying activities and the full NHR exemption matrix.
- `pt-irs-employees-investment`: the 2026 bands, specific deductions, deductions from the tax and the annual return for salary, pension, capital income, rent and gains.
- `pt-income-tax`: self-employed income (Category B).
- `portugal-crypto-tax`: crypto assets.

The law is the Código do IRS (CIRS), read article by article on the Portal das Finanças on 2026-10-23. This skill does not give per-country treaty rates. Read the treaty with the source country for each item of income.

## Who this applies to

**Residents only.** A person resident in Portugal under CIRS art. 16 is taxed on worldwide income. Residence tests, split years and treaty tie-breakers are in `pt-cross-border`. Non-residents pay Portuguese tax only on Portuguese-source income and are out of scope here.

**Is the income foreign at all?** CIRS art. 18(1) lists what counts as Portuguese-source. Salary is Portuguese-source if the work is done in Portugal or the payer is resident in Portugal (art. 18(1)(a)). A remote worker living in Lisbon and paid by a foreign employer therefore has Portuguese income, not foreign income. Pensions are Portuguese-source when owed by a Portuguese payer (art. 18(1)(l)). Rent and gains on property in Portugal are Portuguese-source (art. 18(1)(h)); rent and gains on property abroad are foreign income.

**Three groups of residents, three treatments.** Check status first, with `pt-nhr-ifici`:

| Status | Foreign income treatment in 2026 |
|---|---|
| General rules (most residents) | Taxed in Portugal, with the art. 81(1) foreign tax credit |
| IFICI holder (EBF art. 58-A) | Foreign Category A, B, E, F and G income exempt, but counted to find the rate on other income (CIRS art. 81(4)). Foreign pensions (Category H) are **not** exempt: general rules apply |
| NHR holder still inside the 10-year period (art. 236(3) Lei 82/2023) | Old wording of CIRS art. 72(10) and (12) and 81(4) to (8) keeps applying. Foreign pensions taxed at 10% for most NHRs (old art. 72(12)) |

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| IRS bands: up to EUR 8,342 at 12.50%; over 8,342 to 12,587 at 15.70%; over 12,587 to 17,838 at 21.20%; over 17,838 to 23,089 at 24.10%; over 23,089 to 29,397 at 31.10%; over 29,397 to 43,090 at 34.90%; over 43,090 to 46,566 at 43.10%; over 46,566 to 86,634 at 44.60%; over 86,634 at 48.00% | Average rates for the whole band: 12.500%, 13.579%, 15.823%, 17.705%, 20.579%, 25.130%, 26.472%, 34.856% | 2026 | CIRS art. 68(1), wording of Lei 73-A/2025: https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs68.aspx |
| Solidarity surcharge | 2.5% on taxable income over EUR 80,000 up to 250,000; 5% above | 2026 | CIRS art. 68-A: https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs68a.aspx |
| Foreign capital income (dividends, interest) not withheld in Portugal | 28% autonomous rate; the resident may opt to aggregate | 2026 | CIRS art. 72(1)(d) and (13): https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs72.aspx |
| Capital income from a payer in a listed low-tax jurisdiction, not withheld | 35% | 2026 | CIRS art. 72(18)(a) |
| Net gains on shares and other securities | 28%; 35% where the issuer is in a listed low-tax jurisdiction | 2026 | CIRS art. 72(1)(c) and (18)(b) |
| Rent | 25% for residential leases, 28% for other rent; option to aggregate | 2026 | CIRS art. 72(1)(e), (2) and (13) |
| IAS (social support index) | EUR 537.13 | 2026 | Portaria 480-A/2025/1: https://diariodarepublica.pt/dr/detalhe/portaria/480-a-2025-993056222 |
| Specific deduction for pensions (Category H) | 8.54 x IAS = EUR 4,587.09 per pensioner, or the whole pension if lower | 2026 | CIRS art. 53(1) and (2), by reference to art. 25(1)(a): https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs53.aspx |
| Foreign tax credit | Lower of the foreign tax paid and the share of Portuguese tax on that income; capped at the tax the treaty allows; unused amount carried forward 5 years only when Portuguese tax was too small | 2026 | CIRS art. 81(1) to (3): https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs81.aspx |
| IFICI special rate | 20% on net Category A and B income from the qualifying activity only | 2026 | EBF art. 58-A(2): https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/bf_rep/Pages/ebf58a.aspx |
| IFICI holder: foreign Category A, B, E, F, G | Exempt, counted for the rate on other income | 2026 | CIRS art. 81(4) |
| IFICI holder: capital income and gains paid by or linked to an entity in a listed low-tax jurisdiction | 35% | 2026 | CIRS art. 81(5) |
| NHR holder: net foreign pension | 10% (option to aggregate) | Rest of the NHR period | Old CIRS art. 72(12) and (13), wording of Lei 2/2020: https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/ra/Pages/irs72ra_202312.aspx; kept by art. 236(3) Lei 82/2023 |

There is no CIRS art. 72-A. The 2024 Budget (Lei 82/2023) put IFICI in the Tax Benefits Statute, EBF art. 58-A, and revoked CIRS art. 72(10) and (12) for everyone except NHR holders covered by its transitional art. 236.

## The taxable base

**Step 1: classify each item.** Put each item of foreign income in its IRS category (A salary, B self-employment, E capital, F rent, G gains, H pensions). The category decides the Portuguese rate and the treaty article to read.

**Step 2: convert to euros (art. 23).** Income from abroad uses the buying rate on the date it was paid or made available (art. 23(1)(b) and (c)). If that date cannot be proved, use the rate of 31 December of the income year (art. 23(2)). If there is no rate on the date, use the last rate before it (art. 23(3)).

**Step 3: declare the gross.** Income that gets a foreign tax credit is declared before foreign tax (art. 22(6)). Do not declare the net amount received.

**Step 4: Portuguese tax on the income.**

- Salary and pensions are aggregated with other income and taxed at the art. 68 bands, after the specific deduction (art. 25 for salary, art. 53 for pensions).
- Dividends and interest paid by a foreign payer directly to the resident are not withheld in Portugal, so they pay the 28% autonomous rate (art. 72(1)(d)), or 35% from a listed low-tax jurisdiction (art. 72(18)(a)). If a Portuguese bank or broker acting for the payer or the holder pays out foreign securities income (dividends, bond interest), it withholds 28% as a final tax (art. 71(1)(b)). The resident may aggregate them instead (art. 72(13)); then every item of Category E must be aggregated (art. 22(5)). On aggregation, dividends from an EU or EEA company that meets art. 2 of Directive 2011/96/EU count at 50%, with a certificate from that state's tax authority as proof (art. 40-A(1), (4) and (5)).
- Rent and gains follow art. 72 and the rules in `pt-irs-employees-investment`.

**Step 5: the foreign tax credit (art. 81(1) and (2)).** The credit is the lower of:

1. the income tax paid abroad, and no more than the treaty allows the source state to charge (art. 81(2)); and
2. the part of the Portuguese tax, before this credit, that belongs to that income, net of its specific deductions (art. 81(1)(b)). For income taxed at a special rate, the limit is the tax at that rate (art. 81(1)).

Foreign tax above the treaty rate is not credited. Claim it back from the source state. Foreign tax above the Portuguese tax on the income is lost. The only carry-forward is in art. 81(3): if the credit allowed cannot be used because the year's Portuguese tax is too small, the rest can be used in the next five years, within the art. 81(1)(b) limit of those years.

**Step 6: treaty exemption.** Where a treaty gives Portugal the exemption method with progression, the income is exempt but counted to find the rate on the other income (art. 81(9), art. 22(4)). Where a treaty applies the credit method in the source state instead, no Portuguese credit is given (art. 81(10)).

**IFICI holders.** IFICI is EBF art. 58-A. Its 20% rate covers only net Category A and B income earned in the qualifying activity (art. 58-A(2)). Foreign Category A, B, E, F and G income is exempt and counted for the rate on other income (CIRS art. 81(4)). Category H is not in that list. An IFICI holder's foreign pension is therefore aggregated at the art. 68 bands, after the art. 53 specific deduction, with the art. 81(1) credit for foreign tax. It is not taxed at 10%. Capital income and gains paid by, or on securities of, an entity in a listed low-tax jurisdiction pay 35% (art. 81(5), applying art. 71(17)(b) and (c) and art. 72(18)).

**NHR holders.** The 10% pension rate was old CIRS art. 72(12), added by Lei 2/2020. Lei 82/2023 revoked it from 2024 but its art. 236(3) keeps the old wording of art. 72(10) and (12) and art. 81(4) to (8) for people already registered as NHR and for the closed 2023 and 2024 transitional groups, until their 10 years end. Under Lei 2/2020 art. 329(2), NHRs registered (or with a request pending) when that law took effect, and residents who applied by 31 March 2020 or 2021, keep the pre-2020 pension exemption unless they opted for 10% in their 2020 return. The 10% applies to the net pension that is not Portuguese-source under art. 18(1), on the part that did not create a deduction under art. 25(2). The NHR holder may aggregate instead (old art. 72(13)). Details and the full NHR matrix are in `pt-nhr-ifici`.

## Deadlines and filing

| What | When | Source |
|---|---|---|
| Modelo 3 return with Anexo J for 2026 income | 1 April to 30 June 2027, online, whether or not 30 June is a working day | CIRS art. 60(1): https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs60.aspx |
| Foreign tax credit not yet fixed in the source state by 30 June 2027 | Deadline extended to 31 December 2027, if the taxpayer tells AT within the normal period, naming the type of income and the source state | CIRS art. 60(3) and (4) |
| Correction after a change in income declared (for example a later foreign assessment or refund) | Within 30 days of the change | CIRS art. 60(2) |
| Payment of the balance | By 31 August 2027 when AT assesses in the normal period | CIRS art. 97(1)(a): https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs97.aspx |

**The annexes.** Foreign income goes on Anexo J. NHR and IFICI holders also file Anexo L, where they show the regime and the method for foreign income. Keep proof of the foreign tax: a statement from the payer or the foreign tax authority showing the tax actually paid.

## Penalties and interest

- **Late or missing return:** fine of EUR 150 to EUR 3,750 (RGIT art. 116(1)). Source: https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/rgit/Pages/rgit116.aspx
- **Fine waived** if there was no tax conviction or earlier waiver in the past five years (RGIT art. 29(1)), or no loss of revenue and the failure is put right (RGIT art. 29(2)). Source: https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/rgit/Pages/rgit29.aspx
- **Compensatory interest** when the taxpayer's fault delays the assessment, at the legal rate of 4% a year (LGT art. 35; Portaria 291/2003). Source: https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/lgt/Pages/lgt35.aspx
- **Late payment interest** from the payment deadline, at the rate the IGCP sets each year: 7.221% from 1 January 2026 (Aviso 18/2026/2). A 2026 balance paid late in 2027 uses the 2027 rate. Source: https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/lgt/Pages/lgt44.aspx

## Cross-border points

- **Sweden: no treaty.** Sweden terminated the 2002 Portugal-Sweden treaty with effect from 1 January 2022 (Aviso 2/2022, Diário da República of 1 February 2022). For Swedish income only the unilateral art. 81(1) credit applies, with no treaty cap under art. 81(2).
- **Treaty rates.** The source state's withholding cap comes from the treaty with that state. Ask the payer to apply the treaty rate at source, using a Portuguese certificate of residence. Tax withheld above the treaty rate is not credited in Portugal (art. 81(2)); reclaim it from the source state.
- **Listed low-tax jurisdictions.** Art. 72(18) and 81(5) refer to the list approved by portaria of the Finance Minister. Check the current list before applying 35%.
- **US citizens** living in Portugal remain taxable in the US on citizenship. The Portuguese credit is computed the same way; US relief is a US question.
- **Multilateral Instrument (MLI).** Portugal is a party. Where it modifies a treaty, the principal purpose test can deny treaty benefits to an arrangement whose main aim is the benefit. Read the treaty as modified.

## Worked examples

### Example 1: resident under the general rules (or an IFICI holder) with a foreign pension

Maria is resident in Portugal for all of 2026. Her only income is a pension from abroad of EUR 24,000 gross. The source state withheld EUR 1,800, and the treaty lets that state tax the pension at that level. Many treaties give private pensions only to the state of residence; under such a treaty the art. 81(2) cap is nil, nothing is credited and the EUR 1,800 must be reclaimed abroad. Read the pension article of the treaty first. She is not NHR. The pension computation is the same if she also held IFICI for a job in Portugal taxed at 20%, because art. 81(4) does not exempt pensions and income taxed at the art. 72 special rates is not aggregated (art. 22(3)(b)).

1. Specific deduction (art. 53): EUR 4,587.09. Taxable income: 24,000 - 4,587.09 = EUR 19,412.91. The pension is declared gross of the foreign tax (art. 22(6)).
2. Minimum existence (art. 70) does not apply: gross income is above 2.2 x 14 x IAS = EUR 16,543.60 (art. 70(4)(a)).
3. Tax by band: 19,412.91 is in band 4. Tax = 17,838 x 15.823% + (19,412.91 - 17,838) x 24.10% = 2,822.51 + 379.55 = EUR 3,202.06.
4. Share of Portuguese tax on the foreign income: all her income is foreign, so EUR 3,202.06.
5. Credit = lower of 1,800 and 3,202.06 = EUR 1,800. Tax after the credit: EUR 1,402.06, before deductions from the tax such as general family expenses.

```oa-check
name: PT resident with EUR 24,000 foreign pension, art. 81 credit, 2026 bands
inputs:
  pension: 24000
  foreign_tax: 1800
  specific_deduction: 4587.09
  band3_top: 17838
steps:
  - taxable: pension - specific_deduction
  - tax: round(band3_top * 0.15823 + (taxable - band3_top) * 0.241, 2)
  - pt_share: tax
  - credit: min(foreign_tax, pt_share)
  - tax_after_credit: tax - credit
expected:
  taxable: 19412.91
  tax: 3202.06
  credit: 1800.00
  tax_after_credit: 1402.06
```

### Example 2: foreign dividends with too much tax withheld at source

João is resident and not NHR or IFICI. In 2026 he receives EUR 10,000 gross dividends from a company in a treaty country. The company withheld 30% (EUR 3,000) because he did not give it a Portuguese certificate of residence. Assume the treaty caps the source tax on his dividends at 15% (read the actual treaty). He does not aggregate.

1. Portuguese tax: 28% autonomous rate on the gross (art. 72(1)(d), art. 22(6)): 28% x 10,000 = EUR 2,800.
2. Foreign tax that can count: the treaty cap, 15% x 10,000 = EUR 1,500 (art. 81(2)). The other EUR 1,500 is not credited.
3. Credit = lower of 1,500 and 2,800 = EUR 1,500. Portuguese tax due: EUR 1,300.
4. João must reclaim the EUR 1,500 over-withheld from the source state. If he does not, his total tax is EUR 4,300 instead of EUR 2,800.

```oa-check
name: PT resident, EUR 10,000 foreign dividends, 28% rate, treaty cap 15%, 30% withheld
inputs:
  dividends: 10000
  withheld: 3000
steps:
  - pt_tax: dividends * 0.28
  - treaty_tax: dividends * 0.15
  - creditable: min(withheld, treaty_tax)
  - credit: min(creditable, pt_tax)
  - pt_due: pt_tax - credit
  - to_reclaim: withheld - treaty_tax
  - total_if_not_reclaimed: withheld + pt_due
expected:
  pt_tax: 2800.00
  credit: 1500.00
  pt_due: 1300.00
  to_reclaim: 1500.00
  total_if_not_reclaimed: 4300.00
```

The EUR 4,300 is the total burden if the over-withholding is never recovered (3,000 abroad plus 1,300 in Portugal); with the refund it falls to EUR 2,800.

**The aggregation option.** Suppose the dividends are João's only income and he aggregates them (art. 72(13)). The company is outside the EU and EEA, so art. 40-A does not halve them. Tax at the art. 68 bands on EUR 10,000: 8,342 x 12.50% + (10,000 - 8,342) x 15.70% = 1,042.75 + 260.31 = EUR 1,303.06. Credit = lower of 1,500 (treaty cap) and 1,303.06 = EUR 1,303.06. Portuguese tax due: nil, against EUR 1,300 at 28%. Aggregation also pulls in every other item of Category E he has (art. 22(5)), so compare both routes on all of it.

```oa-check
name: PT resident, EUR 10,000 foreign dividends aggregated at 2026 bands, treaty cap 15%
inputs:
  dividends: 10000
  band1_top: 8342
steps:
  - pt_tax: round(band1_top * 0.125 + (dividends - band1_top) * 0.157, 2)
  - treaty_tax: dividends * 0.15
  - credit: min(treaty_tax, pt_tax)
  - pt_due: pt_tax - credit
expected:
  pt_tax: 1303.06
  credit: 1303.06
  pt_due: 0.00
```

## Ask the client first

1. Were you resident in Portugal for all of 2026, and are you registered under NHR or IFICI? If NHR, when did you become resident and did you opt for the 10% pension rate in your 2020 return? (Decides exemption, 10%, or the general rules.)
2. For each item of foreign income: the country, the type (salary, pension, dividend, interest, rent, gain) and, for a pension, whether it is a state or private pension. (Decides the category and the treaty article.)
3. How much foreign tax was actually paid on each item, and do you have the payer's or tax authority's statement? (The credit needs proof and is capped at the treaty rate.)
4. Did the payer apply the treaty rate, or withhold at its full domestic rate? (Over-withholding must be reclaimed abroad.)
5. Is the foreign tax for 2026 still not final by 30 June 2027? (The art. 60(3) extension must be notified in time.)
6. Do you want dividends, interest or rent aggregated? (Worth it when the bands on the extra income come out below the special rate, or when EU dividends count at 50% under art. 40-A. Aggregating Category E pulls in all of it.)

## Sources

| Source | URL | Read on |
|---|---|---|
| CIRS art. 81, foreign tax credit and IFICI exemption (current wording, with art. 236 Lei 82/2023 and art. 329 Lei 2/2020) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs81.aspx | 2026-10-23 |
| CIRS art. 81, wording to December 2023 (NHR rules) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/ra/Pages/irs81ra_202312.aspx | 2026-10-23 |
| CIRS art. 72, special rates (current; art. 72(10) and (12) revoked by Lei 82/2023) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs72.aspx | 2026-10-23 |
| CIRS art. 72, wording to December 2023 (NHR 10% pension rate, art. 72(12)) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/ra/Pages/irs72ra_202312.aspx | 2026-10-23 |
| EBF art. 58-A, IFICI | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/bf_rep/Pages/ebf58a.aspx | 2026-10-23 |
| CIRS art. 68, 2026 bands (wording of Lei 73-A/2025) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs68.aspx | 2026-10-23 |
| CIRS art. 68-A, solidarity surcharge | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs68a.aspx | 2026-10-22 |
| CIRS art. 22, aggregation and gross-up of foreign income | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs22.aspx | 2026-10-23 |
| CIRS art. 40-A, 50% of qualifying dividends on aggregation | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs40a.aspx | 2026-10-23 |
| CIRS art. 70, minimum existence | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs70.aspx | 2026-10-23 |
| CIRS art. 23, currency conversion | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs23.aspx | 2026-10-23 |
| CIRS art. 18, Portuguese-source income | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs18.aspx | 2026-10-23 |
| CIRS art. 53, pension specific deduction | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs53.aspx | 2026-10-22 |
| CIRS art. 60, filing period and extension | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs60.aspx | 2026-10-23 |
| CIRS art. 71, 28% final withholding (incl. foreign securities income paid through a Portuguese intermediary, art. 71(1)(b)) and 35% for low-tax jurisdictions | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs71.aspx | 2026-10-23 |
| CIRS art. 97, payment | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs97.aspx | 2026-10-22 |
| Portaria 480-A/2025/1, IAS 2026 = EUR 537.13 | https://diariodarepublica.pt/dr/detalhe/portaria/480-a-2025-993056222 | 2026-10-23 |
| Aviso 2/2022, Sweden terminates the treaty from 1 January 2022 | https://files.dre.pt/1s/2022/02/02200/0000300003.pdf | 2026-10-23 |
| RGIT art. 116 and 29, fines | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/rgit/Pages/rgit116.aspx | 2026-10-22 |
| LGT art. 35 and 44, interest | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/lgt/Pages/lgt35.aspx | 2026-10-22 |
| Aviso 18/2026/2 (IGCP), late payment interest 7.221% from 1 January 2026 | https://diariodarepublica.pt/dr/detalhe/aviso/18-2026-993315668 | 2026-10-23 |

Not yet confirmed: per-country treaty withholding rates (the AT treaty tables were not read; read each treaty); the MLI ratification and entry-into-force dates for Portugal and which treaties it modifies; whether the IFICI exempt income or 20% income changes the rate applied to a foreign pension that is aggregated (art. 81(4) says exempt income counts for the rate on other income, but AT guidance on this case was not read); whether the 25% residential rent rate of art. 72(2) is applied by AT to foreign property; the Anexo J table and code numbers (the 2027 return instructions were not read); the current list of low-tax jurisdictions (Portaria 150/2004 as amended); the late payment interest rate for 2027.

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
