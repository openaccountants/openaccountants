---
name: pt-income-tax
description: "Portuguese personal income tax (IRS) for tax year 2026 on self-employed income (Category B, recibos verdes) of a resident individual. Covers the 2026 IRS bands of CIRS art. 68 (Lei 73-A/2025), the solidarity surcharge, the simplified regime coefficients of art. 31 (0.75, 0.35, 0.15, 0.95, 0.10, 1), the 10% social security rule and the 15% expenses rule, the first-year coefficient cut, organised accounts and the EUR 200,000 limit, client withholding (23%, 16.5%, 11.5%) and the waiver below EUR 15,000, payments on account, IRS Jovem on the 2026 IAS (EUR 537.13, cap EUR 29,542.15), the Modelo 3 with Anexo B, fines and interest. Trigger on: 'IRS trabalhador independente', 'recibos verdes', 'Anexo B', 'regime simplificado', 'coeficiente 0,75', 'IRS Jovem 2026', 'freelancer tax Portugal'. Out of scope: employees, pensions, rent and investment income (pt-irs-employees-investment), crypto (portugal-crypto-tax), social security (pt-social-contributions), NHR and IFICI (pt-nhr-ifici), non-residents (pt-cross-border)."
version: 2.3
jurisdiction: PT
tax_year: 2026
last_updated: 2026-10-31
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
source_checked: 2026-10-16
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Portugal: IRS for the self-employed, Category B (tax year 2026) v2.2

> Source-cited draft: not reviewed by an accountant.

This skill computes the annual IRS of a Portuguese resident who earns business or professional income (Category B): freelancers issuing recibos verdes, sole traders and professionals. It covers the simplified regime and organised accounts, client withholding, payments on account and IRS Jovem. The return for 2026 income is the Modelo 3 with Anexo B, filed from 1 April to 30 June 2027.

Sibling skills, which this one links to and does not repeat:

- `pt-irs-employees-investment`: salary, pensions, rent, dividends, interest, capital gains, the deductions from the tax (dependants, health, education, general family expenses) and the minimum existence rule. A self-employed person with other income uses both skills.
- `pt-social-contributions`: self-employed social security (21.4%, the quarterly declaration, the first-year exemption).
- `pt-nhr-ifici`: the old non-habitual resident regime and IFICI (20% flat rate). Check this first. A person under either regime is taxed differently and cannot use IRS Jovem.
- `pt-cross-border`: residence, non-residents with Portuguese income, arriving and leaving.
- `portugal-crypto-tax`: crypto gains, and crypto traded or mined as a business.

The law is the Código do IRS (CIRS). AT (Autoridade Tributária e Aduaneira) publishes the consolidated text, article by article, on the Portal das Finanças. Every figure below was read there, or in the Segurança Social guide, on 2026-10-23.

## Who this applies to

**Residents with Category B income.** Category B is income from a business or a profession carried on independently. A person is resident if, in the year, they spent more than 183 days in Portugal in any 12-month period starting or ending in the year, or had a home there that suggests they intend to keep it as their habitual residence (CIRS art. 16(1)). Residents are taxed on worldwide income. Part-year residence and non-residents are in `pt-cross-border`.

**First check: NHR or IFICI.** If the person is registered under either regime, stop and use `pt-nhr-ifici`. IFICI holders also suffer 20% withholding on Category B, not 23% (art. 101(1)(d)).

**Simplified regime or organised accounts.** The simplified regime applies to a person whose Category B income in the previous year did not exceed EUR 200,000 (art. 28(2)). In the first year of activity the estimate in the start-of-activity declaration decides (art. 28(10)). The person may opt for organised accounts instead, in the start-of-activity declaration or by the end of March of the year the change takes effect (art. 28(3) and (4)). The simplified regime ends only when the EUR 200,000 limit is exceeded in two consecutive years, or in one year by more than 25% (over EUR 250,000). Organised accounts then apply from the next year (art. 28(6)).

**Single client.** A person who provides services to one entity only may opt each year to be taxed under the Category A (employment) rules (art. 28(8)). The exception is a partner providing services to a tax-transparent company.

## Rates, bands and thresholds

| Item | Rate or amount | Tax year | Source |
|---|---|---|---|
| IRS band 1: taxable income up to EUR 8,342 | 12.50% (average 12.500%) | 2026 | CIRS art. 68(1), wording of Lei 73-A/2025: https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs68.aspx |
| Band 2: over 8,342 to 12,587 | 15.70% (average 13.579%) | 2026 | same |
| Band 3: over 12,587 to 17,838 | 21.20% (average 15.823%) | 2026 | same |
| Band 4: over 17,838 to 23,089 | 24.10% (average 17.705%) | 2026 | same |
| Band 5: over 23,089 to 29,397 | 31.10% (average 20.579%) | 2026 | same |
| Band 6: over 29,397 to 43,090 | 34.90% (average 25.130%) | 2026 | same |
| Band 7: over 43,090 to 46,566 | 43.10% (average 26.472%) | 2026 | same |
| Band 8: over 46,566 to 86,634 | 44.60% (average 34.856%) | 2026 | same |
| Band 9: over 86,634 | 48.00% | 2026 | same |
| Solidarity surcharge | 2.5% on taxable income over EUR 80,000 up to 250,000; 5% over 250,000 | 2026 | CIRS art. 68-A: https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs68a.aspx |
| Coefficient: sales of goods, crypto operations (not mining), restaurants, bars and hotels (not local lodging in a house or flat) | 0.15 | 2026 | CIRS art. 31(1)(a): https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs31.aspx |
| Coefficient: professional activities listed in the art. 151 table | 0.75 | 2026 | CIRS art. 31(1)(b) |
| Coefficient: other services | 0.35 | 2026 | CIRS art. 31(1)(c) |
| Coefficient: crypto mining, licensing of intellectual or industrial property, know-how, capital income and rent of the business, net capital gains | 0.95 | 2026 | CIRS art. 31(1)(d) |
| Coefficient: grants not for operations | 0.30 | 2026 | CIRS art. 31(1)(e) |
| Coefficient: operating grants and other Category B income | 0.10 | 2026 | CIRS art. 31(1)(f) |
| Coefficient: services to a tax-transparent company of which the person is a partner, or to a company in which the person holds at least 5% (or the family at least 25%) for over 183 days | 1 | 2026 | CIRS art. 31(1)(g) |
| Coefficient: local lodging (house or flat) in a containment area | 0.50 | 2026 | CIRS art. 31(1)(h) |
| First-year cut of coefficients (b), (c) and (f) | 50% in the year activity starts, 25% in the next year, if no Category A or H income in that year; not if activity ceased less than 5 years before | 2026 | CIRS art. 31(10) and (11) |
| Social security deduction in the simplified regime, coefficients (b) and (c) | Compulsory contributions only in the part above 10% of gross income | 2026 | CIRS art. 31(2) |
| 15% expenses rule, coefficients (b) and (c) | Add back 15% of gross service income less the listed amounts (see The taxable base) | 2026 | CIRS art. 31(13) |
| Simplified regime limit | EUR 200,000 of Category B income in the previous year | 2026 | CIRS art. 28(2) and (6): https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs28.aspx |
| IAS (social support index) | EUR 537.13 | 2026 | Portaria 480-A/2025/1, de 30 de dezembro, art. 2 (AT's copy of the Diário da República text): https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/diplomas_legislativos/Documents/Portaria_480_A_2025_1.pdf |
| Category A specific deduction used in the 15% rule | 8.54 x IAS = EUR 4,587.09 | 2026 | CIRS art. 25(1)(a): https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs25.aspx |
| IRS Jovem exemption cap | 55 x IAS = EUR 29,542.15 of exempt income a year | 2026 | CIRS art. 12-B(5): https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs12b.aspx |
| IRS Jovem exempt share | 100% year 1; 75% years 2 to 4; 50% years 5 to 7; 25% years 8 to 10 | 2026 | CIRS art. 12-B(5) |
| Withholding by clients: art. 151 professional activities | 23% | 2026 | CIRS art. 101(1)(b): https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs101.aspx |
| Withholding: intellectual property income (art. 3(1)(c)) | 16.5% | 2026 | CIRS art. 101(1)(a) |
| Withholding: other Category B services | 11.5% | 2026 | CIRS art. 101(1)(c) |
| Withholding: IFICI holders | 20% | 2026 | CIRS art. 101(1)(d) |
| Withholding waiver | Expected Category B income for the year below the CIVA art. 53(1) limit of EUR 15,000; not if the limit was reached the year before | 2026 | CIRS art. 101-B(1)(a) and (3): https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs101b.aspx; CIVA art. 53(1) |
| No withholding below | EUR 25 per withholding | 2026 | CIRS art. 101-B(1)(d) |
| Payments on account | Three, by 20 July, 20 September and 20 December; total 65% of the formula amount; none if each is under EUR 50 | 2026 | CIRS art. 102(1) to (3): https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs102.aspx |
| Self-employed social security | 21.4% (25.2% for sole traders with a business, empresários em nome individual) on 70% of service income (20% of sales of goods and of hotel and restaurant income), monthly base capped at 12 x IAS = EUR 6,445.56 | 2026 | Segurança Social, Guia Prático, Trabalhadores Independentes; detail in `pt-social-contributions` |

The 2026 bands are lower than the 2025 bands. Lei 73-A/2025 (the 2026 State Budget) cut the rates of bands 2 to 5 (band 2 from 16.00% to 15.70%, band 3 from 21.50% to 21.20%, band 4 from 24.40% to 24.10%, band 5 from 31.40% to 31.10%) and raised every band limit (band 1 from EUR 8,059 to EUR 8,342; band 9 from over EUR 83,696 to over EUR 86,634). Do not use the 2025 table (Lei 55-A/2025) for 2026 income.

## The taxable base

**Step 1: gross Category B income.** All fees and sales invoiced and received in the year, before withholding. Withholding is a credit, not a cost: rebuild the gross from the net received as net / (1 - rate), for example net / 0.77 at 23%. Check the rate on each receipt.

**Step 2a: simplified regime.** Taxable income = gross income of each type x its coefficient (art. 31(1)). Pick the coefficient from the activity code registered with AT, not from how the client describes the work. Code-by-code mapping to the art. 151 table (Portaria 1011/2001) is outside this skill; ask for the AT start-of-activity proof.

- **Social security (art. 31(2)).** For coefficients (b) and (c) only, deduct compulsory social security contributions paid for the activity, but only the part above 10% of gross income, and only up to the net income after the coefficient.
- **The 15% rule (art. 31(13)).** For coefficients (b) and (c), add to taxable income the positive difference between 15% of the gross service income and the sum of: (a) EUR 4,587.09 (the Category A specific deduction) or, if higher, the contributions not deducted under art. 31(2); (b) staff costs reported to AT; (c) rent of business premises on invoices reported to AT; (d) 1.5% of the tax value (VPT) of property the person owns and uses in the business (4% for hotels and local lodging); (e) other business expenses on e-fatura invoices; (f) business imports and intra-EU purchases. Expenses used only partly for the business count at 25% (art. 31(14)). The person flags business invoices on the Portal das Finanças by the end of February of the next year (art. 31(15)(a)), or declares the amounts in the return (art. 31(16)).
- **First year.** Coefficients (b), (c) and (f) are cut by 50% in the year activity starts and by 25% in the next year, if the person has no Category A or H income in that year (art. 31(10)). Not if activity ceased less than 5 years before (art. 31(11)).
- **Crypto.** Crypto income under coefficients (a) and (d) counts when the crypto is sold (art. 31(17)). Stopping the activity and losing residence are treated as a sale (art. 31(18)). See `portugal-crypto-tax`.

**Step 2b: organised accounts.** Taxable profit from the accounts under IRC rules, with a certified accountant (Contabilista Certificado). Social security is a cost in full. The accounts are required when art. 28(6) is triggered, or by option.

**Step 3: IRS Jovem (art. 12-B).** A taxpayer aged 35 or under who is not a dependant may exempt part of their Category A and B income in the first 10 years of earning income, by opting in the return (art. 12-B(1)). Years with no Category A or B income do not count (art. 12-B(3)(b)). The exempt share is in the table above, capped at EUR 29,542.15 of exempt income in 2026 (art. 12-B(5)). The exempt income is still counted to find the rate on the rest (art. 12-B(4), art. 22(4)). This skill computes it as tax on the total income x (non-exempt income / total income). People who have had NHR or IFICI, opted for art. 12-A, or have unpaid tax cannot use it (art. 12-B(9)).

**Step 4: tax by band.** Add the Category B taxable income to any other income that is aggregated (see `pt-irs-employees-investment`). AT computes the tax as the upper limit of the highest band fully used x that band's average rate (column B), plus the excess x the next band's normal rate (column A) (art. 68(2)). Add the solidarity surcharge over EUR 80,000 (art. 68-A). Joint filers halve the income, apply the table and double the result (art. 68-A(3), art. 69).

**Step 5: deductions from the tax, then credits.** Personal deductions (dependants, general family expenses, health, education, housing) are in `pt-irs-employees-investment`. Then subtract withholding and payments on account.

**Losses.** A Category B loss can only be set against Category B income, carried forward for 12 years (art. 55(1)(a)). Losses from before the simplified regime started can be deducted under that regime (art. 55(4)).

## Deadlines and filing

| What | When | Source |
|---|---|---|
| Start of activity, or change to organised accounts | Start-of-activity declaration; a change of regime by the end of March of the year it takes effect | CIRS art. 28(4) and (5) |
| Flag business invoices on e-fatura for the 15% rule | By end of February 2027 | CIRS art. 31(15)(a) |
| Payments on account for 2026 | By 20 July, 20 September and 20 December 2026; the amounts come from the 2024 assessment | CIRS art. 102(1) and (2) |
| Social security | Quarterly declaration; contributions paid monthly between the 10th and the 20th of the next month | Segurança Social, Guia Prático, Trabalhadores Independentes |
| Modelo 3 with Anexo B, 2026 income | 1 April to 30 June 2027, online, whether or not 30 June is a working day | CIRS art. 60(1): https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs60.aspx |
| Payment of the balance | By 31 August 2027 when AT assesses within the normal period | CIRS art. 97(1)(a): https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs97.aspx |

**The waiver of withholding** is optional. The person writes "Sem retenção, nos termos do n.º 1 do artigo 101.º-B do Código do IRS." on the receipt (art. 101-B(2)). It stops in the month after the EUR 15,000 limit is reached (art. 101-B(3)(b)). Only clients that have or must have organised accounts withhold (art. 101(1)); private individuals do not. Code 1519 ("outros prestadores de serviços"), the residual code of the art. 151 table, is for services that fit no other CAE or CIRS code; AT's binding ruling in process 4006/2019 (approved 20 December 2019) places that income in art. 3(1)(b) and sets withholding at 11.5% under art. 101(1)(c), not 23%.

**Payments on account** stop when withholding plus payments already made cover the tax for the year, or when Category B income stops (art. 102(4)). They can be reduced (art. 102(5)). If the reduction leaves more than 20% unpaid, compensatory interest is due (art. 102(6)).

## Penalties and interest

- **Late or missing return:** fine of EUR 150 to EUR 3,750 (RGIT art. 116(1)). Source: https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/rgit/Pages/rgit116.aspx
- **Omissions or errors in the return** that are not fraud: fine of EUR 375 to EUR 22,500, cut to a quarter when no tax is due (RGIT art. 119(1) and (2)). Source: https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/rgit/Pages/rgit119.aspx
- **Compensatory interest** when the taxpayer's fault delays the assessment, at the legal interest rate of Civil Code art. 559(1) (LGT art. 35(10)). Source: https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/lgt/Pages/lgt35.aspx
- **Late payment interest** from the due date, at the rate set for debts to the State (LGT art. 44(3)). Source: https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/lgt/Pages/lgt44.aspx
- **Reduced payments on account:** compensatory interest if more than 20% of the normal amount went unpaid (CIRS art. 102(6) and (7)).

The current rates for both kinds of interest are in `pt-irs-employees-investment`.

## Cross-border points

- **Non-residents** with Portuguese Category B income are taxed by final withholding or at flat rates. See `pt-cross-border`.
- **Foreign clients** do not withhold Portuguese tax. The whole IRS is then paid through payments on account and the final balance. Foreign tax withheld by a client's country is credited under the treaty; see `pt-foreign-source-treaties`.
- **NHR and IFICI** holders: see `pt-nhr-ifici`. They cannot use IRS Jovem (art. 12-B(9)).
- **Leaving Portugal** with crypto held in the business is treated as a sale (art. 31(18)(b)). See `portugal-crypto-tax`.
- **VAT** on the same fees is separate. The EUR 15,000 CIVA art. 53 exemption limit also drives the withholding waiver. See `portugal-vat-return`.

## Worked examples

### Example 1: consultant in the simplified regime, gross EUR 52,000

Ana is resident, aged 40, and works as a consultant under an activity code in the art. 151 table. She is in the simplified regime. In 2026 she invoiced EUR 52,000. Portuguese companies with organised accounts paid EUR 40,000 of it and withheld 23%, so EUR 9,200 was withheld. She paid EUR 4,200 of social security and flagged EUR 2,000 of business expenses on e-fatura. She made no payments on account and has no other income. Deductions from the tax are left out.

1. Coefficient 0.75: 52,000 x 0.75 = EUR 39,000.
2. Social security (art. 31(2)): 10% of gross is EUR 5,200. She paid EUR 4,200, which is less, so nothing is deducted.
3. The 15% rule (art. 31(13)): 15% x 52,000 = EUR 7,800. Against it count the higher of EUR 4,587.09 and her non-deducted contributions (EUR 4,200), so EUR 4,587.09, plus EUR 2,000 of e-fatura expenses: EUR 6,587.09. The shortfall of EUR 1,212.91 is added.
4. Taxable income: 39,000 + 1,212.91 = EUR 40,212.91, in band 6.
5. Tax: 29,397 x 20.579% + (40,212.91 - 29,397) x 34.90% = 6,049.61 + 3,774.75 = EUR 9,824.36.
6. Balance due: 9,824.36 - 9,200 = EUR 624.36, by 31 August 2027.

```oa-check
name: PT Category B consultant, simplified regime, gross EUR 52,000 (2026)
inputs:
  gross: 52000
  coefficient: 0.75
  ss_paid: 4200
  efatura_expenses: 2000
  ias: 537.13
  withheld: 9200
steps:
  - base: gross * coefficient
  - ss_deduction: max(0, ss_paid - gross * 0.10)
  - specific: round(8.54 * ias, 2)
  - ss_not_deducted: ss_paid - ss_deduction
  - shortfall: max(0, gross * 0.15 - (max(specific, ss_not_deducted) + efatura_expenses))
  - taxable: base - ss_deduction + shortfall
  - tax: round(29397 * 0.20579 + (taxable - 29397) * 0.349, 2)
  - balance: tax - withheld
expected:
  base: 39000
  ss_deduction: 0
  specific: 4587.09
  shortfall: 1212.91
  taxable: 40212.91
  tax: 9824.36
  balance: 624.36
```

### Example 2: young programmer, IRS Jovem year 3, cap applies

Pedro is 29, resident, and in his third year of earning income, so IRS Jovem exempts 75%. He programs under an art. 151 activity code, simplified regime. In 2026 he invoiced EUR 70,000, paid EUR 7,500 of social security and flagged EUR 4,000 of business expenses on e-fatura. He has no other income.

1. Coefficient 0.75: 70,000 x 0.75 = EUR 52,500.
2. Social security above 10% of gross: 7,500 - 7,000 = EUR 500 deducted. Net EUR 52,000. The EUR 7,000 not deducted stays available for the 15% rule.
3. The 15% rule: 15% x 70,000 = EUR 10,500. Against it: the higher of EUR 4,587.09 and EUR 7,000, so EUR 7,000, plus EUR 4,000 of expenses: EUR 11,000. No shortfall. Taxable income EUR 52,000.
4. IRS Jovem: 75% x 52,000 = EUR 39,000, above the 2026 cap. Exempt income is EUR 29,542.15. Non-exempt income is 52,000 - 29,542.15 = EUR 22,457.85.
5. Tax on the full EUR 52,000 (band 8): 46,566 x 26.472% + (52,000 - 46,566) x 44.60% = 12,326.95 + 2,423.56 = EUR 14,750.52 (EUR 14,750.5155 before rounding).
6. Tax due on the non-exempt part: 14,750.52 x 22,457.85 / 52,000 = EUR 6,370.48. Applying the bands to EUR 22,457.85 alone would give too little tax, because the exempt income counts for the rate (art. 22(4)).

```oa-check
name: PT Category B programmer, IRS Jovem year 3 with the 2026 cap, gross EUR 70,000
inputs:
  gross: 70000
  coefficient: 0.75
  ss_paid: 7500
  efatura_expenses: 4000
  ias: 537.13
  exempt_share: 0.75
steps:
  - ss_deduction: max(0, ss_paid - gross * 0.10)
  - ss_not_deducted: ss_paid - ss_deduction
  - shortfall: max(0, gross * 0.15 - (max(round(8.54 * ias, 2), ss_not_deducted) + efatura_expenses))
  - taxable: gross * coefficient - ss_deduction + shortfall
  - cap: 55 * ias
  - exempt: min(taxable * exempt_share, cap)
  - non_exempt: taxable - exempt
  - tax_on_all: round(46566 * 0.26472 + (taxable - 46566) * 0.446, 2)
  - tax_due: round(tax_on_all * non_exempt / taxable, 2)
expected:
  ss_deduction: 500
  shortfall: 0
  taxable: 52000
  cap: 29542.15
  exempt: 29542.15
  non_exempt: 22457.85
  tax_on_all: 14750.52
  tax_due: 6370.48
```

## Ask the client first

1. Have you ever been registered under NHR or IFICI? (Changes the rates and rules IRS Jovem out.)
2. What activity code is on your AT start-of-activity record, and when did the activity start? (Coefficient 0.75, 0.35 or another; the first-year cut.)
3. What was your Category B income in 2024 and 2025, and do you keep organised accounts? (Simplified regime or accounts under art. 28.)
4. Your age, and how many years have you earned employment or self-employed income? (IRS Jovem year and share.)
5. Which clients withheld tax, at what rate, and which business invoices did you flag on e-fatura? (Credits and the 15% rule.)
6. Do you also have salary, rent, investment income or crypto, or are you married filing jointly? (Aggregation and the sibling skills.)

## Sources

| Source | URL | Read on |
|---|---|---|
| CIRS art. 68, IRS bands 2026 (wording of Lei 73-A/2025) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs68.aspx | 2026-10-23 |
| CIRS art. 68, 2025 bands (wording of Lei 55-A/2025, until December 2025) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/ra/Pages/irs68ra_202512.aspx | 2026-10-23 |
| CIRS art. 68-A, solidarity surcharge | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs68a.aspx | 2026-10-23 |
| CIRS art. 12-B, IRS Jovem | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs12b.aspx | 2026-10-23 |
| CIRS art. 16, residence | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs16.aspx | 2026-10-23 |
| CIRS art. 22, aggregation and exempt income for the rate | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs22.aspx | 2026-10-23 |
| CIRS art. 25, specific deduction 8.54 x IAS | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs25.aspx | 2026-10-23 |
| CIRS art. 28, simplified regime and EUR 200,000 | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs28.aspx | 2026-10-23 |
| CIRS art. 31, coefficients, 10% and 15% rules, first year | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs31.aspx | 2026-10-23 |
| CIRS art. 55, losses | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs55.aspx | 2026-10-23 |
| CIRS art. 60, filing period | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs60.aspx | 2026-10-23 |
| CIRS art. 97, payment | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs97.aspx | 2026-10-23 |
| CIRS art. 101, withholding rates | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs101.aspx | 2026-10-23 |
| CIRS art. 101-B, withholding waiver | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs101b.aspx | 2026-10-23 |
| CIRS art. 102, payments on account | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs102.aspx | 2026-10-23 |
| AT binding ruling, process 4006/2019 (Ficha doutrinária, CIRS art. 101, code 1519 withholding 11.5%) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/informacoes_vinculativas/rendimento/cirs/Documents/PIV_16493.pdf | 2026-10-27 |
| CIRS art. 151, activity classification | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs151.aspx | 2026-10-23 |
| CIVA art. 53(1), EUR 15,000 limit | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/civa_rep/Pages/artigo-53-o-do-civa.aspx | 2026-10-23 |
| RGIT art. 116 and 119, fines | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/rgit/Pages/rgit116.aspx | 2026-10-23 |
| LGT art. 35 and 44, interest | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/lgt/Pages/lgt35.aspx | 2026-10-23 |
| Portaria 480-A/2025/1, art. 2, IAS 2026 EUR 537.13 (AT's copy of the Diário da República text) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/diplomas_legislativos/Documents/Portaria_480_A_2025_1.pdf | 2026-10-23 |
| Segurança Social, Guia Prático, Novo Regime dos Trabalhadores Independentes (IAS 2026 EUR 537.13, 21.4%, 25.2%, 70%/20%, ceiling EUR 6,445.56, payment 10th to 20th) | https://www.seg-social.pt/ptss/pssd/documento/cmc1xyfxz00dekl2ynxz676sw | 2026-10-23 |

Not yet confirmed: which activity codes of Portaria 1011/2001 fall in the art. 151 table (the table was not read); which simplified-regime coefficient applies to code 1519 (an earlier version said 0.75 as AT's position; the AT ruling read covers withholding only); that AT applies the IRS Jovem art. 22(4) rule as average rate on total income x non-exempt income, as this skill does, and that for Category B in the simplified regime the exempt share and the cap apply to income after the coefficient, as this skill does (no AT guidance read); the EBF art. 58 relief for authors' income, not read for 2026 and not used here; CIRS art. 68(2) still names EUR 8,059 (the 2025 first band limit), and this skill applies the method with the 2026 band limits.

> Contributed by Michael Cutajar.

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
