---
name: pt-income-tax
description: "Portuguese resident Category B income tax for 2026: simplified and organised accounts, actual annual rates, coefficients, social-contribution and expense adjustments, withholding, payments on account, Modelo 3 and IRS Jovem boundaries. Preserves the historical 2025 cases separately. Special residence, NHR/IFICI, personal reliefs and unverified individual outcomes require the identified specialist routes."
version: 2.5
jurisdiction: PT
tax_year: 2026
last_updated: 2026-11-28
source_checked: 2026-10-16
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
---

# Portugal: IRS for the self-employed, Category B (tax year 2026) v2.5

This Guide computes the annual IRS of a Portuguese resident who earns business or professional income (Category B): freelancers issuing recibos verdes, sole traders and professionals. It covers the simplified regime and organised accounts, client withholding, payments on account and IRS Jovem. The ordinary return for 2026 income is Modelo 3, with Anexo B for simplified income or Anexo C for organised accounts, filed from 1 April to 30 June 2027. The ordinary annual table below is used for mainland cases; do not assume it establishes an autonomous-region result. Historical 2025 cases retain that year and their own table. All examples require the stated facts and actual applicable regime; figures before personal reliefs are not completed assessments.

Companion Guides, which this one links to and does not repeat:

- `pt-irs-employees-investment`: salary, pensions, rent, dividends, interest, capital gains, the deductions from the tax (dependants, health, education, general family expenses) and the minimum existence rule. A self-employed person with other income uses both skills.
- `pt-social-contributions`: self-employed social security, including the actual contribution class, declaration and first-cover date.
- `pt-nhr-ifici`: the distinct non-habitual resident regime and IFICI. Check this first. A person under either regime is taxed differently and cannot use IRS Jovem.
- `pt-cross-border`: residence, non-residents with Portuguese income, arriving and leaving.
- `portugal-crypto-tax`: crypto gains, and crypto traded or mined as a business.

The law is the Código do IRS (CIRS). AT (Autoridade Tributária e Aduaneira) publishes the consolidated text, article by article, on the Portal das Finanças. New official passages were read on 2026-11-28; applicable completed social-security/eligibility/IAS proof is reused with its original 2026-11-27 read date. Sources identify the passages and periods used.

## Who this applies to

**Residents with Category B income.** Category B is income from a business or a profession carried on independently. A person is resident if, in the year, they spent more than 183 days in Portugal in any 12-month period starting or ending in the year, or, having stayed for less time, had a home available on a day in that period in conditions indicating an intention to maintain and occupy it as habitual residence (CIRS art. 16(1)). Residents are taxed on worldwide income. Part-year residence and non-residents are in `pt-cross-border`.

**First check: NHR or IFICI.** If the person is registered under either regime, stop and use `pt-nhr-ifici`. IFICI holders also suffer 20% withholding on Category B, not 23% (art. 101(1)(d)).

**Simplified regime or organised accounts.** The simplified regime applies to a person whose Category B income in the previous year did not exceed EUR 200,000 (art. 28(2)). In the first year of activity the estimate in the start-of-activity declaration decides (art. 28(10)). The person may opt for organised accounts instead, in the start-of-activity declaration or by the end of March of the year the change takes effect (art. 28(3) and (4)). The simplified regime ends only when the EUR 200,000 limit is exceeded in two consecutive years, or in one year by more than 25% (over EUR 250,000). Organised accounts then apply from the next year (art. 28(6)).

**Single client.** A person whose services are all to one entity may elect Category A rules under Article 28(8), subject to the actual Anexo B conditions: no organised-account option or isolated-act treatment, and not a partner providing services to a tax-transparent company. This election is not an employment-status finding.

## Rates, bands and thresholds

| Item | Rate or amount | Tax year | Source |
|---|---|---|---|
| IRS band 1: taxable income up to EUR 8,342 | 12.20% (average 12.200%) | 2026 | CIRS art. 68(1), wording of Decreto-Lei 212/2026 (effect from 1 January 2026): https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs68.aspx |
| Band 2: over 8,342 to 12,587 | 15.20% (average 13.212%) | 2026 | same |
| Band 3: over 12,587 to 17,838 | 20.70% (average 15.416%) | 2026 | same |
| Band 4: over 17,838 to 23,089 | 23.60% (average 17.277%) | 2026 | same |
| Band 5: over 23,089 to 29,397 | 30.60% (average 20.136%) | 2026 | same |
| Band 6: over 29,397 to 43,090 | 34.60% (average 24.732%) | 2026 | same |
| Band 7: over 43,090 to 46,566 | 43.10% (average 26.103%) | 2026 | same |
| Band 8: over 46,566 to 86,634 | 44.60% (average 34.658%) | 2026 | same |
| Band 9: over 86,634 | 48.00% | 2026 | same |
| Solidarity surcharge | 2.5% on taxable income over EUR 80,000 up to 250,000; 5% over 250,000 | 2026 | CIRS art. 68-A: https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs68a.aspx |
| Coefficient: sales of goods, crypto operations (not mining), restaurants, bars and hotels (not local lodging in a house or flat) | 0.15 | 2026 | CIRS art. 31(1)(a): https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs31.aspx |
| Coefficient: professional activities listed in the art. 151 table | 0.75 | 2026 | CIRS art. 31(1)(b) https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs31.aspx |
| Coefficient: other services | 0.35 | 2026 | CIRS art. 31(1)(c) https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs31.aspx |
| Coefficient: crypto mining, licensing of intellectual or industrial property, know-how, capital income and rent of the business, net capital gains | 0.95 | 2026 | CIRS art. 31(1)(d) https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs31.aspx |
| Coefficient: grants not for operations | 0.30 | 2026 | CIRS art. 31(1)(e) https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs31.aspx |
| Coefficient: operating grants and other Category B income | 0.10 | 2026 | CIRS art. 31(1)(f) https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs31.aspx |
| Coefficient: services to a tax-transparent professional company of which the person is a partner; or to a company in which, for over 183 days, the person holds at least 5% directly/indirectly, or the person, spouse/de facto partner and their ascendants/descendants together hold at least 25% of capital/votes | 1 | 2026 | CIRS art. 31(1)(g) https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs31.aspx |
| Coefficient: local lodging (house or flat) in a containment area | 0.50 | 2026 | CIRS art. 31(1)(h) https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs31.aspx |
| First-year cut of coefficients (b), (c) and (f) | 50% in the year activity starts, 25% in the next year, if no Category A or H income in that year; not if activity ceased less than 5 years before | 2026 | CIRS art. 31(10) and (11) https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs31.aspx |
| Social security deduction in the simplified regime, coefficients (b) and (c) | Compulsory contributions only in the part above 10% of gross income | 2026 | CIRS art. 31(2) https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs31.aspx |
| 15% expenses rule, coefficients (b) and (c) | Add back 15% of gross service income less the listed amounts (see The taxable base) | 2026 | CIRS art. 31(13) https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs31.aspx |
| Simplified regime limit | EUR 200,000 of Category B income in the previous year | 2026 | CIRS art. 28(2) and (6): https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs28.aspx |
| IAS (social support index) | EUR 537.13 | 2026 | Portaria 480-A/2025/1, de 30 de dezembro, art. 2 (AT's copy of the Diário da República text): https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/diplomas_legislativos/Documents/Portaria_480_A_2025_1.pdf |
| Category A specific amount used in the 15% rule | Computed 8.54 × 537.13 = EUR 4,587.09 | 2026 | CIRS art. 25(1)(a): https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs25.aspx ; IAS: https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/diplomas_legislativos/Documents/Portaria_480_A_2025_1.pdf |
| IRS Jovem gross-income exemption cap | Computed 55 × 537.13 = EUR 29,542.15 a year | 2026 | CIRS art. 12-B(5): https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs12b.aspx ; IAS: https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/diplomas_legislativos/Documents/Portaria_480_A_2025_1.pdf |
| IRS Jovem exempt share | 100% year 1; 75% years 2 to 4; 50% years 5 to 7; 25% years 8 to 10 | 2026 | CIRS art. 12-B(5) https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs12b.aspx |
| Withholding by clients: art. 151 professional activities | 23% | 2026 | CIRS art. 101(1)(b): https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs101.aspx |
| Withholding: intellectual property income (art. 3(1)(c)) | 16.5% | 2026 | CIRS art. 101(1)(a) https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs101.aspx |
| Withholding: other Category B services | 11.5% | 2026 | CIRS art. 101(1)(c) https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs101.aspx |
| Withholding: IFICI holders | 20% | 2026 | CIRS art. 101(1)(d) https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs101.aspx |
| Withholding waiver | Expected Category B income for the year below the CIVA art. 53(1) limit of EUR 15,000; not if the limit was reached the year before | 2026 | CIRS art. 101-B(1)(a) and (3): https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs101b.aspx; CIVA art. 53(1): https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/civa_rep/Pages/artigo-53-o-do-civa.aspx |
| No withholding below | EUR 25 per withholding | 2026 | CIRS art. 101-B(1)(d) https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs101b.aspx |
| Payments on account | Three, by 20 July, 20 September and 20 December; total 65% of the formula amount; none if each is under EUR 50 | 2026 | CIRS art. 102(1) to (3): https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs102.aspx |
| Ordinary self-employed social security | 21.4%; ENI/EIRL and qualifying spouses 25.2%. Relevant income: 70% services, 20% goods and fiscally declared qualifying hotel/restaurant/drinks income; monthly base is relevant quarter income / 3, subject to actual coverage/options. Organised accounts differ. | 2026 | `pt-social-contributions`; Code Articles 162/163/168: https://diariodarepublica.pt/dr/legislacao-consolidada/lei/2009-34514575 |
| Ordinary social-security maximum monthly base | Computed 12 × IAS 537.13 = EUR 6,445.56 | 2026 | Code Article 163: https://diariodarepublica.pt/dr/legislacao-consolidada/lei/2009-34514575 ; IAS: https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/diplomas_legislativos/Documents/Portaria_480_A_2025_1.pdf |

The 2026 table reflects Decreto-Lei 212/2026 of 4 November, which states that the reduction applies to income obtained in 2026 with effect from 1 January. Historical calculations use the final 2025 Article 68 table, not the 2026 table or earlier rate schedules. The printed Article 68(2) still mentions EUR 8,059; its split-rate method must be read with the actual year's table. In 2026, income within the first EUR 8,342 uses the first-band rate. Do not change the quoted statutory text or substitute a tax year to conceal that old cross-reference.

## The taxable base

**Step 1: gross Category B income.** Article 3(6) uses the point when an invoice is obligatory for VAT purposes or, if no invoice is obligatory, payment or availability; organised accounts follow the applicable IRC timing rules. Do not require an amount to be both invoiced and received or classify only bank credits. Reconcile invoices/receipts, VAT, platform charges and actual withholding separately. Withholding is a credit, not a cost. Only when the net is solely the relevant gross less evidenced withholding can gross be rebuilt as net / (1 − actual rate), for example net / 0.77 at 23%. Do not invent a processor fee or an exchange rate from a bank label.

**Step 2a: simplified regime.** Taxable income = gross income of each type x its coefficient (art. 31(1)). Pick the coefficient from the activity code registered with AT, not from how the client describes the work. The official Portaria 1011/2001 table lists architects (1001), consultants (1320), programmers (1332), translators (1334) and designers (1336). Obtain AT registration and match the actual activity; the residual code 1519 withholding ruling does not by itself settle its simplified coefficient. Neither 0.35 nor 0.75 is an automatic default.

- **Social security (art. 31(2)).** For coefficients (b) and (c) only, deduct compulsory social security contributions paid for the activity, but only the part above 10% of gross income, only up to the net income after the coefficient, and only when not deducted elsewhere.
- **The 15% rule (art. 31(13)).** For coefficients (b) and (c), add to taxable income the positive difference between 15% of the gross service income and the sum of: (a) EUR 4,587.09 (the Category A specific deduction) or, if higher, the contributions not deducted under art. 31(2); (b) staff costs reported to AT; (c) rent of business premises on invoices reported to AT; (d) 1.5% of the tax value (VPT) of property used in the business of which the person is owner, usufructuary or surface-right holder (4% for hotels and local lodging); (e) other business expenses on e-fatura invoices; (f) business imports and intra-EU purchases. The partly business expenses in items (c), (d) and (e) count at 25% (art. 31(14)); this is not a universal rule for every expense or for organised accounts. The person flags business invoices on the Portal das Finanças by the end of February of the next year (art. 31(15)(a)), or declares the amounts in the return (art. 31(16)).
- **First year.** Coefficients (b), (c) and (f) are cut by 50% in the year activity starts and by 25% in the next year, if the person has no Category A or H income in that year (art. 31(10)). Not if activity ceased less than 5 years before (art. 31(11)).
- **Crypto.** Crypto income under coefficients (a) and (d) counts when the crypto is sold (art. 31(17)). For those business-crypto provisions, stopping the activity and losing residence are equated to a disposal, subject to the Article 10(20) adaptation in Article 31(17) (art. 31(18)). See `portugal-crypto-tax`.

**Step 2b: organised accounts.** Use tax-adjusted accounting profit under the IRC rules incorporated by Article 32, with the IRS adaptations, and the required accounting/Contabilista Certificado process. Costs must be incurred to obtain or guarantee taxable income and documented under the applicable rules; a bank debit or a personal expense is not automatically deductible. Actual qualifying contributions may enter the accounts as costs; do not invent an extra deduction of 10% of profit or deduct a cost twice. Article 33(5) caps documented home-related depreciation/rent, energy, water and fixed-phone expenses at 25% when part of the home is used for the activity. Establish actual business use; do not assume a 50% phone or representation allowance, a universal EUR 250 asset threshold or a tax result from floor area alone.

**Step 3: IRS Jovem (art. 12-B).** Eligibility requires age no greater than 35 at year end, non-dependant status, the qualifying income-year count and an election in the return. Years without A/B income do not consume the remaining eligible income years; dependent years and the statutory transition must be checked. Shares are 100% in year 1, 75% in years 2–4, 50% in years 5–7 and 25% in years 8–10, subject to the annual 55 IAS cap. Past/current NHR or IFICI, the Article 12-A exclusion and unregularised tax status must be checked. A degree is not an additional 2025-onward eligibility requirement, although original historical degree facts remain recorded.

AT ruling [PIV 28155](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/informacoes_vinculativas/rendimento/cirs/Documents/PIV_28155.pdf) answers the simplified Category B question: the exemption applies to **gross** professional income, not income after the coefficient. Article 22(7) includes exempt income **without deductions** for the rate. Do not reuse the former calculation that exempts coefficient-net income and apportions tax on that net total. Establish the subsequent contribution/expense and rate calculation before producing an individual liability; the unverified final interaction in Example 2 remains an explicit hold. **Check this point with one of our partner accountants.**

**Step 4: tax by band.** Add the Category B taxable income to other income that is actually aggregated under the applicable compulsory or elective rules (see `pt-irs-employees-investment`). AT computes the tax as the upper limit of the highest band fully used x that band's average rate (column B), plus the excess x the next band's normal rate (column A) (art. 68(2)). Add the solidarity surcharge over EUR 80,000 (art. 68-A). Eligible married or de facto partners who elect joint taxation halve the relevant taxable income, apply the table and double the result; solidarity uses the same half-and-double approach (art. 68-A(3), art. 69). Joint filing is not automatically the better choice.

**Step 5: deductions from the tax, then credits.** Personal deductions (dependants, general family expenses, health, education, housing) are in `pt-irs-employees-investment`. Then subtract withholding and payments on account.

**Losses.** A Category B loss can only be set against Category B income, carried forward for 12 years (art. 55(1)(a)). Losses from before the simplified regime started can be deducted under that regime (art. 55(4)), subject to the applicable Article 52 IRC limits, ordinarily the 65% profit ceiling. Establish vintage, any exception and assessment method; do not import corporate unlimited carry-forward into the IRS 12-year rule or claim a loss automatically.

## Deadlines and filing

| What | When | Source |
|---|---|---|
| Start of activity, or change to organised accounts | Start-of-activity declaration; a change of regime by the end of March of the year it takes effect | CIRS art. 28(4) and (5) |
| Flag business invoices on e-fatura for the 15% rule | Statutory end of February 2027; establish any applicable calendar extension | CIRS art. 31(15)(a) |
| Payments on account for 2026 | By 20 July, 20 September and 20 December 2026; the amounts come from the 2024 assessment | CIRS art. 102(1) and (2) |
| Social security | Quarterly declaration; contributions paid monthly between the 10th and the 20th of the next month | Segurança Social, Guia Prático, Trabalhadores Independentes |
| Modelo 3 with applicable Anexo B or C, 2026 income | 1 April to 30 June 2027, online, whether or not 30 June is a working day | CIRS art. 60(1): https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs60.aspx |
| IRS amounts actually withheld by an obliged agent | By the 20th of the month after deduction, distinct from the recipient's annual credit | CIRS art. 98, applicable completed proof: https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs98.aspx |
| Payment of the balance | By 31 August 2027 when AT assesses within the normal period | CIRS art. 97(1)(a): https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs97.aspx |

The historical ordinary filing windows remain 1 April–30 June 2026 for 2025 income and 1 April–30 June 2025 for 2024 income. These are not replaced by the current 2026-income/2027-return dates. Establish the actual filing notice/calendar where an extension applies.

The actual Anexo B read is marked in force from January 2026: professional table income is field 403, other services 404 and goods sales 401; Q6 records gross subject to withholding (601), actual withholding (602) and payments on account (603). Q17 records the relevant contribution/expense data, and Q3E.1 the 2025-onward IRS Jovem election. Anexo C is for organised accounts and identifies the certified accountant at 15001. H and J cover their actual deduction/foreign-income functions; J is not a universal non-resident form. Historical A/E/F/G and automatic-return enquiries stay with the appropriate other-income route and actual eligibility/version. Match the form issued for the actual filing; this does not assert a fictional 2027 model.

**The waiver of withholding** is optional, excludes intermediation commissions and cases requiring final-rate withholding, and uses expected annual income strictly below EUR 15,000 with the prior-year restriction. It is not an annual IRS exemption. The person writes "Sem retenção, nos termos do n.º 1 do artigo 101.º-B do Código do IRS." on the receipt (art. 101-B(2)). It stops in the month after the EUR 15,000 limit is reached (art. 101-B(3)(b)). Test the payer's actual organised-accounting and Portuguese withholding obligation (art. 101(1)); do not infer the outcome merely from a company NIF, nationality or a foreign address. The under-EUR-25-per-retention rule in Article 101-B(1)(d) is applicable in its wording effective from 1 July 2025; do not apply that wording indiscriminately to earlier transactions. Code 1519 ("outros prestadores de serviços"), the residual code of the art. 151 table, is for services that fit no other CAE or CIRS code; AT's binding ruling in process 4006/2019 (approved 20 December 2019) places that income in art. 3(1)(b) and sets withholding at 11.5% under art. 101(1)(c), not 23%.

**Payments on account:** the three instalments are based on 65% × [C × (RLB / RLT) − R], using the penultimate year's assessment: C is tax after the specified Article 78 deductions, R is Category B withholding, RLB is positive net B income and RLT total net income. Each instalment is rounded upward to euros and is not demanded if below EUR 50; reconcile the AT notice. For 2026 the reference is 2024, not an invented prior-year EUR 1,000 trigger or a 76.5%/80% method. Cessation/reduction follows Article 102(4)–(5). Compensatory interest on more than 20% of normally payable amounts not paid also requires the penultimate assessment by 31 May and unchanged household, with the statutory equal allocation/daily calculation; it is not triggered by every small difference.

## Penalties and interest

- **Late or missing return:** ordinary fine of EUR 150 to EUR 3,750, excluding Article 116(3)'s dispensed-return cases; actual relief/reduction must be established (RGIT art. 116). Source: https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/rgit/Pages/rgit116.aspx
- **Omissions or errors in the return** that are neither fraud nor the preceding specified offence: fine of EUR 375 to EUR 22,500, cut to a quarter when no tax is due (RGIT art. 119(1) and (2)). Source: https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/rgit/Pages/rgit119.aspx
- **Compensatory interest** when the taxpayer's fault delays the assessment, at the legal interest rate of Civil Code art. 559(1) (LGT art. 35(10)). Source: https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/lgt/Pages/lgt35.aspx
- **Late payment interest** from the due date, at the rate set for debts to the State (LGT art. 44(3)). Source: https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/lgt/Pages/lgt44.aspx
- **Reduced payments on account:** compensatory interest if more than 20% of the normal amount went unpaid (CIRS art. 102(6) and (7)).

Establish the actual annual rate, period and any individual relief through the appropriate specialist route; this Guide does not authorise a universal 4% calculation. Check this point with one of our partner accountants.

## Cross-border points

- **Non-residents** with Portuguese Category B income are taxed by final withholding or at flat rates. See `pt-cross-border`.
- **Foreign clients:** establish source, residence/PE and actual payer obligation; foreign address is not a universal zero-withholding rule. Record evidenced foreign tax without assuming it is fully creditable. Treaties, credit entitlement/limits and any special filing extension require `pt-foreign-source-treaties` and the actual facts.
- **NHR and IFICI** holders: see `pt-nhr-ifici`. They cannot use IRS Jovem (art. 12-B(9)).
- **Leaving Portugal** with crypto within the business provisions raises Article 31(17)–(18) disposal treatment and its adaptations; this is not a universal rule for every private crypto holding. See `portugal-crypto-tax`.
- **VAT** on the same fees is separate. The EUR 15,000 CIVA art. 53 exemption limit also drives the withholding waiver. See `portugal-vat-return`.

## Worked examples

### Example 1: consultant in the simplified regime, gross EUR 52,000

Ana is resident, aged 40, and works as a consultant under an activity code in the art. 151 table. She is in the simplified regime. In 2026 she invoiced EUR 52,000. Portuguese companies with organised accounts paid EUR 40,000 of it and withheld 23%, so EUR 9,200 was withheld. She paid EUR 4,200 of social security and flagged EUR 2,000 of business expenses on e-fatura. She made no payments on account and has no other income. Deductions from the tax are left out. This uses the original ordinary 0.75 coefficient; establish that no commencement-period reduction or other special relief changes the result. The balance shown is before the excluded personal reliefs.

1. Coefficient 0.75: 52,000 x 0.75 = EUR 39,000.
2. Social security (art. 31(2)): 10% of gross is EUR 5,200. She paid EUR 4,200, which is less, so nothing is deducted.
3. The 15% rule (art. 31(13)): 15% x 52,000 = EUR 7,800. Against it count the higher of EUR 4,587.09 and her non-deducted contributions (EUR 4,200), so EUR 4,587.09, plus EUR 2,000 of e-fatura expenses: EUR 6,587.09. The shortfall of EUR 1,212.91 is added.
4. Taxable income: 39,000 + 1,212.91 = EUR 40,212.91, in band 6.
5. Tax: 29,397 x 20.136% + (40,212.91 - 29,397) x 34.60% = 5,919.38 + 3,742.30 = EUR 9,661.68.
6. Illustrative balance before the excluded personal reliefs: 9,661.68 - 9,200 = EUR 461.68; the normal-assessment payment deadline is 31 August 2027, subject to the actual assessment/notice.

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
  - tax: round(29397 * 0.20136 + (taxable - 29397) * 0.346, 2)
  - balance: tax - withheld
expected:
  base: 39000
  ss_deduction: 0
  specific: 4587.09
  shortfall: 1212.91
  taxable: 40212.91
  tax: 9661.68
  balance: 461.68
```

### Example 2: young programmer, IRS Jovem year 3, cap applies

Pedro is 29, resident and in his third income year, with an art. 151 programming activity in the simplified regime. The original 2026 inputs remain EUR 70,000 invoiced, EUR 7,500 contributions, EUR 4,000 qualifying business expenses and no other income. Confirm non-dependant status, qualifying year count, election and all exclusions.

If eligible for the stated 75% share, the gross-income exemption is min(70,000 × 75%, 55 × 537.13) = **EUR 29,542.15**. Gross income remaining before the actual coefficient/contribution/expense computation is **EUR 40,457.85**. The old final tax of EUR 6,296.27 was based on the wrong net-income exemption/rate model and is not usable. The final interaction of the remaining income, actual deductions and progression has not been established for this case; do not produce a filing amount from the cap-only calculation. **Check this point with one of our partner accountants.**

```oa-check
name: PT Category B programmer, original 2026 inputs, gross exemption only
inputs:
  gross: 70000
  coefficient: 0.75
  ss_paid: 7500
  efatura_expenses: 4000
  ias: 537.13
  exempt_share: 0.75
steps:
  - cap: 55 * ias
  - gross_exempt: min(gross * exempt_share, cap)
  - gross_remaining: gross - gross_exempt
expected:
  cap: 29542.15
  gross_exempt: 29542.15
  gross_remaining: 40457.85
```

## Historical 2025 cases and original inputs

These cases retain their original year and amounts. Their former outputs are corrected below; missing facts remain visible. Do not substitute 2026 bands/IAS or treat a conditional working-paper result as a completed return. The original historical cases use mainland locations where stated. The final 2025 annual table is [Article 68, wording of Lei 55-A/2025](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/ra/Pages/irs68ra_202512.aspx):

| 2025 taxable income EUR | Normal rate | Average rate | Source |
|---|---|---|---|
| Up to 8,059 | 12.50% | 12.500% | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/ra/Pages/irs68ra_202512.aspx |
| Over 8,059 to 12,160 | 16.00% | 13.680% | same |
| Over 12,160 to 17,233 | 21.50% | 15.982% | same |
| Over 17,233 to 22,306 | 24.40% | 17.897% | same |
| Over 22,306 to 28,400 | 31.40% | 20.794% | same |
| Over 28,400 to 41,629 | 34.90% | 25.277% | same |
| Over 41,629 to 44,987 | 43.10% | 26.607% | same |
| Over 44,987 to 83,696 | 44.60% | 34.929% | same |
| Over 83,696 | 48.00% | – | same |

Historical taxable income EUR 15,000 therefore gives 12,160 × 13.680% + 2,840 × 21.50% = EUR 2,274.09 before reliefs. IAS is EUR 522.50 in 2025: 8.54 IAS = EUR 4,462.15; the 55 IAS gross-exemption cap is EUR 28,737.50. Do not use a blanket EUR 10,640 minimum-existence subtraction or the old 2024 rates in a 2025 case.

### Original six tests

| Test and original facts | Corrected result or exact unresolved point |
|---|---|
| T1: single, art. 151, gross EUR 40,000, contributions EUR 4,500, documented expenses EUR 7,000, actual withholding EUR 9,200 (stated 23%), no other income/dependants | Ordinary coefficient 0.75 gives 30,000; only contributions above 4,000 are deductible: 500. The expense test is met. Taxable 29,500; 2025 table tax 6,289.40; balance before personal reliefs −2,910.60. Do not deduct all 4,500 or assume the old EUR 850 personal credit. |
| T2: freelancer services EUR 30,000, expenses EUR 2,000 (6.67%; 15% threshold EUR 4,500) | The 2025 specific amount 4,462.15 plus 2,000 already covers the threshold: no EUR 2,500 addback. At the stated ordinary professional coefficient, base is 22,500 before any unprovided contribution adjustment; do not assume missing contributions are zero. |
| T3: IT consulting EUR 45,000 plus hardware EUR 10,000 | Separate coefficients give 33,750 + 1,500 = 35,250 before contribution/expense adjustments. No blended coefficient or final liability inferred. |
| T4: single, taxable income EUR 300,000 | Additional solidarity tax is 170,000 × 2.5% + 50,000 × 5% = 6,750. This is additional tax, not the whole assessment. |
| T5: age 28, master's completed 2023, first professional income 2024, 2025 second year, Category B EUR 35,000 | If all eligibility conditions hold, 75% of gross is 26,250, below the 2025 cap; 8,750 is gross remaining, not final taxable income before blindly applying a coefficient. Establish actual activity, deductions and progression. **Check this point with one of our partner accountants.** |
| T6: EUR 13,000 in 2024; actually no withholding in 2025; EUR 20,000 in 2025 | Retain the actual credit of zero if confirmed, but the old EUR 14,500 threshold is not the operative waiver rule. A valid waiver ceases the month after the actual EUR 15,000 limit is reached; no month or missing withholding is invented. A 15,000 coefficient base is conditional on the actual activity and expense/contribution facts; waiver is not annual tax exemption. |

```oa-check
name: Original 2025 standard freelancer, corrected contribution deduction, before personal reliefs
inputs:
  gross: 40000
  coefficient: 0.75
  ss_paid: 4500
  documented_expenses: 7000
  withheld: 9200
  ias: 522.50
steps:
  - ss_deduction: max(0, ss_paid - gross * 0.10)
  - ss_not_deducted: ss_paid - ss_deduction
  - shortfall: max(0, gross * 0.15 - max(round(8.54 * ias, 2), ss_not_deducted) - documented_expenses)
  - taxable: gross * coefficient - ss_deduction + shortfall
  - tax_before_reliefs: round(28400 * 0.20794 + (taxable - 28400) * 0.349, 2)
  - balance_before_reliefs: tax_before_reliefs - withheld
expected:
  ss_deduction: 500
  shortfall: 0
  taxable: 29500
  tax_before_reliefs: 6289.40
  balance_before_reliefs: -2910.60
```

### Original ten edge cases

| Original case | Corrected treatment |
|---|---|
| EC1: freelance consultant EUR 40,000; e-fatura expenses EUR 3,000 (7.5%); stated 15% requirement EUR 6,000 | Specific amount 4,462.15 plus 3,000 is 7,462.15: no EUR 3,000 shortfall. Baseline 30,000 before unprovided contribution adjustment, not 33,000. |
| EC2: IT services EUR 50,000 and computer hardware EUR 20,000 | Baseline 37,500 + 3,000 = 40,500 before actual adjustments; classify each activity separately. |
| EC3: activity opened March 2025, no contributions paid in 2025 | If first continuous cover with no early election, cover starts 1 March 2026, first contribution payment 10–20 April, with April quarterly declaration. No deduction for contributions not paid in 2025; do not infer first cover or payment amount solely from opening a tax activity. |
| EC4: Category B EUR 12,000, prior income below the old EUR 14,500 parameter, dispensed withholding | Apply the actual EUR 15,000 waiver conditions; no withholding does not establish annual exemption or a guaranteed positive balance after reliefs. |
| EC5: spouse A EUR 60,000 Category A, spouse B EUR 15,000 Category B | Compare joint/separate after each category's proper deductions and actual household facts. EUR 75,000 gross / 2 = 37,500 is not necessarily the taxable quotient. No optimum is established from these inputs alone. **Check this point with one of our partner accountants.** |
| EC6: organised accounts include personal car insurance EUR 800 | Do not deduct a personal cost automatically or invent a business percentage. Establish actual use, evidence and applicable cost rules. **Check this point with one of our partner accountants.** |
| EC7: single freelancer, taxable EUR 120,000 | Solidarity addition is (120,000 − 80,000) × 2.5% = 1,000; separate from ordinary IRS. |
| EC8: age 34, master's 2020, freelancing from 2021, filing 2025 as fifth year | If the qualifying counter is actually year 5, the share is 50%, not the former 25%, with 2025 cap 28,737.50. Preserve degree/start dates; verify dependent/no-income years, election and exclusions. No income amount or final tax is invented. **Check this point with one of our partner accountants.** |
| EC9: moved in 2023 and has NHR; asks about 20% Category B | Preserve arrival/status; follow the NHR route. NHR and IFICI are distinct. No automatic 20% or foreign-income exemption is established. **Check this point with one of our partner accountants.** |
| EC10: freelancer also has EUR 5,000 cryptocurrency trading income | Preserve the amount. Category B versus private gains, holding-period, residence and special disposal rules require the dedicated route; the old 28% / 365-day shorthand is not a usable individual answer. **Check this point with one of our partner accountants.** |

### Historical bank set A: April 2026 rewrite, 2025 transaction inputs

Keep each original bank extract as a reconciliation fixture. Balances and dates are input data, not independently reconstructed opening balances or statutory tax points. The withholding percentages stipulated in the old fixtures are not declarations of the legal rate for 2025. Missing annual expenses, coverage, filing status or other income must remain missing.

#### A1 – Millennium BCP, IT consultant

Art. 151 IT consultant, ordinary simplified regime, gross EUR 75,000; original stipulated withholding EUR 18,750 (25%). The ordinary 0.75 baseline is EUR 56,250 before actual contribution/expense adjustments. The sample EUR 11,250 receipt corresponds to EUR 15,000 only if that actual 25% deduction is evidenced. The statutory professional rate for 2025 is 23%; do not invent a replacement gross from bank data or reuse the former EUR 10,640 subtraction / EUR 16,306 refund.

```text
Data         | Descrição                                  | Débito (€)    | Crédito (€)   | Saldo (€)
15/04/2025   | TRANSF TECHCO CONSULTORIA LDA             |               | 11,250.00     | 52,000.00
20/04/2025   | TRANSF STARTUP LISBOA LDA                 |               |  7,500.00     | 59,500.00
25/04/2025   | DB ADOBE SYSTEMS                          | 65.00         |               | 59,435.00
28/04/2025   | DB NOS COMUNICAÇÕES                       | 45.00         |               | 59,390.00
30/04/2025   | COMISSÃO BANCÁRIA                         | 8.50          |               | 59,381.50
```

#### A2 – CGD, designer with organised accounts

Original gross EUR 55,000, actual expenses EUR 18,000, no withholding, mostly foreign clients. If those expenses are accepted total deductible costs and there are no other adjustments, net is EUR 37,000. An individual ordinary 2025 table calculation before personal relief is EUR 8,906.90. The old additional EUR 3,700 contribution deduction was not established; do not deduct it or present the former approximate EUR 6,800 as a final bill. Actual foreign-credit/payer facts and filing status still matter.

```text
Data valor   | Descrição                                  | Débito (€)    | Crédito (€)   | Saldo (€)
10/03/2025   | TRANSF RECEBIDA LONDON STUDIO UK          |               | 12,000.00     | 38,500.00
15/03/2025   | TRANSF RECEBIDA STARTUP PORTO             |               |  4,250.00     | 42,750.00
20/03/2025   | DB FIGMA INTERNET SERVICES                | 45.00         |               | 42,705.00
22/03/2025   | DB TRANSPORTES URBANOS (MTS PORTO)        | 120.00        |               | 42,585.00
28/03/2025   | ENCARGO CGD CONTA                         | 7.00          |               | 42,578.00
```

#### A3 – Santander Totta, architect

Original 2025 gross EUR 90,000, stipulated withholding EUR 22,500 at 25%, married with two children. Ordinary professional baseline is EUR 67,500 before actual adjustments; the sample EUR 22,500 receipt represents EUR 30,000 only under the stated actual deduction. Do not infer annual contributions from the single EUR 1,200 bank payment. Spouse income, joint election and deductions are needed before a quotient or final tax; no former EUR 17,562 refund is established. Check this point with one of our partner accountants.

```text
Data         | Descrição                                  | Débito (€)    | Crédito (€)   | Saldo (€)
08/05/2025   | TRF ENT URBANISMO CONSTRUTORA SA          |               | 22,500.00     | 98,000.00
12/05/2025   | TRF ENT PROJECTOS ARQUITECTURA LDA        |               | 15,000.00     | 113,000.00
15/05/2025   | DB SEGURANÇA SOCIAL (SS)                  | 1,200.00      |               | 111,800.00
20/05/2025   | DB EDP COMERCIAL                          | 185.00        |               | 111,615.00
25/05/2025   | COMISSÃO SANTANDER                        | 12.00         |               | 111,603.00
```

#### A4 – BPI, copywriter with home office

Original gross EUR 32,000, organised accounts, direct expenses EUR 3,200; apartment 65m² with 10m² office. Rent is EUR 850 monthly / EUR 10,200 annually, electricity EUR 1,560 and internet EUR 420. Exact proposed floor-area allocation gives 10/65 = 15.384615…%, rent 1,569.23, electricity 240 and internet arithmetic 64.62: combined EUR 1,873.85, not 1,876. If those amounts are actually deductible, the arithmetic remainder before contributions is 26,926.15. Floor area alone does not prove use or legal eligibility; apply the Article 33 housing cap to its actual expense categories and establish the internet treatment separately. The old EUR 2,692 contribution estimate and EUR 4,770 tax are non-usable. Check this point with one of our partner accountants.

```text
Data operação | Descrição                                 | Débito (€)    | Crédito (€)   | Saldo (€)
05/06/2025    | TRANSF. RECEBIDA EDITORA PRESENÇA        |               | 5,500.00      | 19,000.00
10/06/2025    | TRANSF. RECEBIDA AGÊNCIA PALAVRAS        |               | 3,200.00      | 22,200.00
15/06/2025    | DB RENDA HABITAÇÃO                       | 850.00        |               | 21,350.00
20/06/2025    | DB NOS FIBRA                             | 35.00         |               | 21,315.00
25/06/2025    | COMISSÃO MANUTENÇÃO CONTA BPI            | 6.00          |               | 21,309.00
```

#### A5 – ActivoBank, young developer

Original 2025 developer age 27, second professional-activity year after graduation, gross EUR 48,000. If eligible for the stated second income year, the gross exemption is min(48,000 × 75%, 28,737.50) = 28,737.50; non-exempt gross is 19,262.50. Verify actual activity, commencement-period reduction, contributions, expense test and progression. The former 0.35 coefficient, EUR 556.50 final tax and EUR 1,143 saving are not usable. Check this point with one of our partner accountants.

```text
Data         | Descrição                                  | Débito (€)    | Crédito (€)   | Saldo (€)
12/07/2025   | TRANSFERÊNCIA FINTECH STARTUP              |               | 12,000.00     | 38,000.00
18/07/2025   | TRANSFERÊNCIA AGÊNCIA TECH                |               |  8,000.00     | 46,000.00
22/07/2025   | DÉBITO GITHUB ENTERPRISE                  | 180.00        |               | 45,820.00
26/07/2025   | DÉBITO JETBRAINS                          | 120.00        |               | 45,700.00
30/07/2025   | DÉBITO ACTIVOBANK MENSALIDADE              | 5.00          |               | 45,695.00
```

#### A6 – Montepio, management consultant

Original 2025 gross EUR 130,000, simplified regime, EUR 8,000 payments on account already paid; the old computation also stipulated EUR 32,500 withholding and estimated contributions EUR 4,550. Professional baseline is 97,500 before actual contribution/expense adjustments. Preserve those old assumptions for verification; an estimate is not an actual deductible payment. Reconcile the EUR 4,000 dated August payment with the annual PPC total without changing its date into a statutory deadline. No former approximate EUR 30,300 refund is established. Check this point with one of our partner accountants.

```text
Data         | Descrição                                  | Débito (€)    | Crédito (€)   | Saldo (€)
03/08/2025   | TRANSFERÊNCIA GRUPO EMPRESARIAL SA        |               | 30,000.00     | 185,000.00
10/08/2025   | TRANSFERÊNCIA CONSULTORIA IBÉRICA LDA     |               | 15,000.00     | 200,000.00
15/08/2025   | PAGAMENTO POR CONTA IRS AT                | 4,000.00      |               | 196,000.00
20/08/2025   | DB VODAFONE NEGÓCIOS                      | 65.00         |               | 195,935.00
25/08/2025   | COMISSÃO MONTEPIO                         | 9.50          |               | 195,925.50
```

### Historical bank set B and Portuguese correction variants

#### B1 – Millennium BCP, Lisbon management consultant

Original 2025 full-year gross EUR 52,000 is an illustrative assumption, not a total extrapolated from the short extract. Contributions EUR 350 × 12 = 4,200. Preserve both the older stipulated 25% withholding variant and the later 23% receipt-confirmed variant; the actual certificates decide the credit.

```text
Data;Descrição;Débito;Crédito;Saldo
05/01/2025;TRANSF DE EMPRESA ALPHA LDA;;3.750,00;
31/01/2025;COMISSÃO BANCÁRIA;4,50;;
10/02/2025;TRANSF DE STARTUP BETA LDA;;2.500,00;
28/02/2025;SEGURANÇA SOCIAL;350,00;;
15/03/2025;TRANSF DE GAMMA CONSULTING LDA;;4.200,00;
31/03/2025;SEGURANÇA SOCIAL;350,00;;
05/04/2025;STRIPE PAYMENTS EUROPE;;1.920,00;
30/04/2025;SEGURANÇA SOCIAL;350,00;;
15/06/2025;TRANSF DE DELTA SA;;3.100,00;
30/06/2025;SEGURANÇA SOCIAL;350,00;;
```

The four withholding-client receipts total EUR 13,550. At the stipulated 25%, aggregate gross-up is 18,066.67 and withholding 4,516.67; rounding each original gross receipt (5,000; 3,333.33; 5,600; 4,133.33) instead gives a one-cent difference, to reconcile to actual certificates. At the later 23%, gross amounts are 4,870.13; 3,246.75; 5,454.55; 4,025.97, total 17,597.40 and withholding 4,047.40. Stripe EUR 1,920 net / approximately EUR 1,978 gross remains the original unsupported fee assumption, not a gross amount inferred by this Guide.

The ordinary professional baseline is 39,000, with no contribution deduction because 4,200 is below 10% of 52,000. The 15% test is 7,800, with 2025 specific amount 4,462.15; other eligible expenses were not supplied. Add the actual positive shortfall, potentially up to 3,337.85 before further qualifying expenses, rather than silently assuming it is zero. If the test is met and the ordinary individual assessment assumptions hold, tax before personal relief is 9,604.90. No former low-rate refund or unqualified Portuguese-variant balance is established.

#### B2 – CGD, Porto programmer

Original gross EUR 45,000 and IRS Jovem year 2 remain. The old contribution calculation 45,000 × 70% × 21.4% = EUR 6,741 and its later “paid” variant must be verified as an actual payment/assessment, not inferred solely from current receipts. If eligible, 75% of gross is 33,750, capped at 28,737.50; gross remaining is 16,262.50. Do not exempt the old coefficient-net 23,631.75 or use the former EUR 298.42 / EUR 1,747.65 final taxes. Check this point with one of our partner accountants.

#### B3 – BPI, Algarve architect with organised accounts

Original gross EUR 220,000; expenses are office rent 12,000, utilities 2,400, phone/internet 1,200, software 2,400, accountant 4,800, professional insurance 1,500 and travel 3,000, totalling 27,300 before contributions. Preserve the original contribution assumption 32,817 and the later 16,101.36 ceiling model separately. Neither is proved as actual liability by 70% of current-year gross: organised social-security assessment uses the actual applicable prior-profit basis/election. The old uncapped multiplication itself is 220,000 × 70% × 21.4% = 32,956, not 32,817. The 2025 maximum monthly base is 12 × 522.50 = 6,270; 12 months at that ceiling and 21.4% derive 16,101.36 only if that assessment/rate applies.

If all stated costs and the respective contribution amount were actually paid/deductible, with no other adjustments, the alternatives are:

| Original contribution assumption EUR | Conditional profit EUR | Ordinary 2025 tax before personal relief EUR | Solidarity EUR | Conditional total before personal relief EUR |
|---|---|---|---|---|
| 32,817 | 159,883 | 65,803.94 | 1,997.08 | 67,801.02 |
| 16,101.36 | 176,598.64 | 73,827.44 | 2,414.97 | 76,242.41 |

These are corrected conditional arithmetic, not a determination of social contributions or a completed assessment. Gross 220,000 alone does not establish mandatory immediate organised accounts: apply the actual prior-period/exit tests. Check this point with one of our partner accountants.

#### B4 – Santander Portugal, Lisbon designer with MB Way

Original consumer MB Way EUR 18,000 plus company transfers EUR 24,000 gross = 42,000. Payment channel does not determine income, payer status or withholding. The older approximate contribution assumption is 6,300; the later gross-percentage model is 6,291.60. If actually paid and qualifying, ordinary coefficient base 31,500 less the respective excess over 4,200 gives 29,400 or 29,408.40 before the expense test. Contributions not separately deducted are 4,200; with specific amount 4,462.15, the unprovided further eligible expenses determine a possible positive shortfall up to 1,837.85. Do not assume that shortfall is zero.

If the expense test is met and the ordinary individual assessment assumptions hold, 2025 tax before personal relief is 6,254.50 or 6,257.43. The later stipulated 23% × 24,000 withholding is 5,520, giving illustrative balances 734.50 or 737.43 before personal relief; the former 737.49 is not a corrected result. Verify actual certificates, contributions, expenses and household facts before filing.

#### B5 – Novo Banco, Lisbon NHR case

Original UK-national IT consultant with registered NHR, and the later RNH/IFICI status enquiry, remain specialist cases. Verify the actual distinct regime, source, registration and eligible activity; no automatic 20% or foreign-income exemption. Check this point with one of our partner accountants.

#### B6 – ActivoBank / Moey, Coimbra first-year translator

Original 2025 first activity year, full-year gross EUR 22,000, contributions assumed EUR 0, with the conditional age-at-most-35/year-1 enquiry. Translation is listed at 1334: ordinary coefficient 0.75 gives 16,500 before adjustments; if the Article 31 commencement conditions actually apply, the first-period 50% coefficient reduction gives 8,250 before other adjustments. These conditions are distinct from IRS Jovem's income-year counter. With expected gross 22,000, the old EUR 12,500 waiver enquiry does not permit a below-15,000 waiver. If all IRS Jovem year-1 conditions are met, all 22,000 gross is below the 2025 cap 28,737.50; no income or age fact is invented. First social-security cover also needs its actual registration/election facts. No unconditional zero final assessment or automatic refund is established. Check this point with one of our partner accountants.

## Ask the client first

Record the NIF, actual residence period/region, filing election, dependants, activity registration, prior returns/losses/credits and twelve months of bank and invoice records before a filing calculation. A missing identity, regime or material fact remains an evidence gap, not a conservative invented value.

1. Have you ever been registered under NHR or IFICI? (Changes the rates and rules IRS Jovem out.)
2. What activity code is on your AT start-of-activity record, and when did the activity start? (Coefficient 0.75, 0.35 or another; the first-year cut.)
3. What was your Category B income in 2024 and 2025, and do you keep organised accounts? (Simplified regime or accounts under art. 28.)
4. Your age, and how many years have you earned employment or self-employed income? (IRS Jovem year and share.)
5. Which clients withheld tax, at what rate, and which business invoices did you flag on e-fatura? (Credits and the 15% rule.)
6. Do you also have salary, rent, investment income or crypto, or are you married filing jointly? (Aggregation and the companion Guides.)

### Records, bank patterns and working-paper controls

Keep the historical transaction library as search candidates, not automatic tax treatment:

- Income candidates: `TRANSF DE`, `TRF DE`, `TRANSF RECEBIDA`, `TRANSFERÊNCIA RECEBIDA`, SEPA/SWIFT, `MB WAY`, `MBWAY RECEBIDO`, Stripe/`STRIPE PAYMENTS EUROPE`/`STRIPE PAYOUT`, PayPal/`PAYPAL RECEBIDO`, Upwork, Fiverr, IFTHENPAY/EUPAGO and Google AdSense. Trace gross invoice, actual withholding, VAT, fees and conversion. A platform transfer or every credit is not necessarily a new taxable supply.
- Expense candidates: NOS/MEO/Vodafone PT/NOWO; EDP/Endesa/Galp Energia/Iberdrola; Adobe/Slack/Figma/Microsoft 365/Google Workspace/JetBrains/GitHub Enterprise; FNAC/Worten/Auchan; CP/Comboios de Portugal/metro/MTS Porto; TAP/Ryanair/easyJet; hotels/Airbnb; professional meals/training/books/publications; `SEGURO PROFISSIONAL`/`SEGURO RC`; `CONTABILISTA`/TOC/ROC; fuel/Galp/BP/Repsol. Obtain purpose and documents; distinguish simplified expense evidence from actual organised-account costs. No automatic 100%, 50%, EUR 250 depreciation threshold or business percentage follows from the supplier name.
- Reconcile `SEGURANÇA SOCIAL`/`TAXA SS`, `RETENÇÃO NA FONTE`, `DESCONTO RECIBO VERDE`/`RETENÇÃO CLIENTE`, `AT PAGAMENTO IRS`/`LIQUIDAÇÃO IRS`/`PGTO IRS AT`, `AT IVA PAGAMENTO`/`IVA ENTREGUE` and `REEMBOLSO IRS AT`/`REEMBOLSO AT` to the real assessment, credit or settlement. Do not create a new cost or income from a tax-settlement description; do not discard supporting evidence of a genuine deductible payment.
- `RENDA RECEBIDA`, `JUROS RECEBIDOS`/`JUROS CONTA` and dividends require actual private-category versus business attribution. `DEVOLUÇÃO`/`REEMBOLSO [client]` or expense reimbursement needs the underlying transaction; a debit note alone does not prove exemption.
- Verify `MBNET`/`TRANSFERÊNCIA MB`/`MULTIBANCO`, own-account savings/transfers, loan receipts, ATM withdrawals and credit-card settlements. Keep underlying invoices and avoid duplicate costs; “exclude” means remove a confirmed non-supply from the tax computation, not delete its accounting record.

Preserve original CSV/PDF dates, Portuguese narrations, debit/credit/balance columns and DD/MM/YYYY format. Millennium BCP, CGD, Santander Totta, BPI, ActivoBank, Montepio, Novo Banco and Moey/MB Way/Multibanco need their actual statement layout, including value date versus operation date. Neither balance movement nor statement date alone establishes Article 3's tax point. Currency conversion follows Article 23's official buy/sell and timing rules, including its missing-date/last-quotation and organised-account exceptions; a processor EUR figure or receipt-date ECB quote is not a universal legal substitute.

Working-paper columns: source/date/tax point, client/supplier, invoice or recibo reference, gross excluding separately reconciled VAT, actual withholding, net payment, original currency/rate, activity/coefficient, receipt versus other-category/non-supply, actual contributions, supporting expenses and business use, evidence gap and applicable return location. Keep income, expense and IRS reconciliation sheets; a multiplication of cost by an assumed business percentage is not a deduction approval. Reconcile coefficient income or tax-adjusted profit, contribution adjustment, expense-test addback, applicable relief/rate base, ordinary and solidarity tax, personal credits, actual withholding/PPC and balance. Never extrapolate a full-year figure from sample months except as an explicitly stated original case assumption.

### Preserved refusal catalogue and non-usable historical parameters

- **R-PT-1, regime:** verify actual prior-year/startup/exit conditions before using simplified rules. EUR 200,000 current gross alone does not require immediate organised accounts or prove eligibility.
- **R-PT-2, NHR/IFICI:** confirm the actual separate status and route to `pt-nhr-ifici`. **Check this point with one of our partner accountants.**
- **R-PT-3, withholding evidence:** obtain certificates/receipts before final credits; not every company/payment requires 25%, 23% or public-payer 11.5%.
- **R-PT-4, employment risk:** preserve the single-client / more-than-80%-receipts / regular-schedule enquiry. It is not a proved automatic employment reclassification test. Distinguish Article 28's single-entity Category A election from employment status. **Check this point with one of our partner accountants.**
- **R-PT-5, organised records:** obtain the accounting, cost evidence, applicable CC identification/signature and real apportionment; the earliest catalogue's no-expense-document/personal-cost/VAT concerns remain here. Compare complete regime computations, not a guaranteed “expenses exceed 65%, so organised wins” shortcut. No invented expense, universal 50% representation/phone allowance, vehicle/km entitlement or EUR 250 asset write-off. **Check this point with one of our partner accountants.**
- **R-PT-6, activity:** establish actual activity/registration and relevant table before choosing a coefficient. Code 1519's withholding ruling is not a complete coefficient ruling. **Check this point with one of our partner accountants.**

Personal reliefs remain the `pt-irs-employees-investment` / Anexo H route. The historical table's EUR 600 per taxpayer, EUR 300/450 dependant shorthand, health 15%/1,000, education 30%/800, housing 15%/502 or600/296, care-home 25%/403.75, alimony 20%, invoice-VAT 15%/250 and general-expense 35%/250 (or a supposed Category B 25%) are preserved as historical enquiries, **not a usable universal deduction table**. The former EUR 10,640 minimum-existence figure and EUR 4,462 / 72%-IAS shortcuts must not be subtracted as generic allowances. Actual year, household, evidence, global caps and the minimum-existence formula control. No automatic EUR 600 credit or old minimum deduction is included in the cases. Authors' EBF Article 58 relief remains an unverified individual route. **Check this point with one of our partner accountants.**

The historical EUR 25–75 voluntary-late-filing / EUR 200–2,500 / 15%–60% penalty shortcuts and a universal 4% interest rate are non-usable. The general legal ranges and distinct interest rules above do not settle individual waiver/reduction, fraud, annual interest rate or liability. **Check this point with one of our partner accountants.**

## Sources

| Source and passage actually read | Official URL | Read on |
|---|---|---|
| CIRS Articles 3, 15 and 16: Category B, tax point, worldwide/residence boundaries | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs3.aspx ; https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs15.aspx ; https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs16.aspx | 2026-11-28 |
| CIRS Article 28: option, prior-period/start estimate, two-period or more-than-25% exit, single-entity election | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs28.aspx | 2026-11-28 |
| CIRS Article 31: full coefficient conditions, contribution/expense adjustments, commencement and business-crypto timing | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs31.aspx | 2026-11-28; applicable completed contribution proof reused 2026-11-27 |
| CIRS Article 151 / Portaria 1011/2001: actual professional classification, original case codes | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs151.aspx ; https://diariodarepublica.pt/dr/legislacao-consolidada/portaria/2001-177307831 | 2026-11-28 |
| CIRS Articles 25, 32, 33 and 117: specific-deduction multiplier, organised-account incorporation, housing cap and accounting duties | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs25.aspx ; https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs32.aspx ; https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs33.aspx ; https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs117.aspx | 2026-11-28 |
| CIRC Article 23: documented costs through the Article 32 incorporation | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc23.aspx | 2026-11-28 |
| CIRS Article 55 and incorporated CIRC Article 52: category losses and limits | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs55.aspx ; https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc52.aspx | CIRS 2026-11-28; applicable completed CIRC proof 2026-11-27 |
| CIRS Article 68 / DL212/2026: current annual bands and 2026-income effect; statutory split-rate wording | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs68.aspx ; https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/diplomas_legislativos/Documents/Decreto-Lei-212-2026.pdf | 2026-11-28 |
| CIRS Article 68, final 2025 wording / Lei55-A/2025: original-year case table | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/ra/Pages/irs68ra_202512.aspx ; https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/diplomas_legislativos/Documents/Lei_55_A_2025.pdf | 2026-11-28 |
| CIRS Articles 68-A, 69 and 22: surcharge, joint quotient, aggregation and exempt income without deductions for rate | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs68a.aspx ; https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs69.aspx ; https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs22.aspx | 2026-11-28 |
| CIRS Article 12-B: identical 2026 eligibility/counter/exclusion/cap conditions from completed proof | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs12b.aspx | 2026-11-27 |
| AT ruling PIV28155, point 6: gross Category B exemption, not coefficient-net | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/informacoes_vinculativas/rendimento/cirs/Documents/PIV_28155.pdf | 2026-11-28 |
| Portaria480-A/2025/1 Article 2: actual 2026 IAS and commencement; 2025 AT page: actual historical IAS | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/diplomas_legislativos/Documents/Portaria_480_A_2025_1.pdf ; https://info.portaldasfinancas.gov.pt/pt/apoio_ao_contribuinte/Cidadaos/Rendimentos/Declaracao/Deducoes_beneficios_taxas/Paginas/default.aspx | 2026 IAS proof 2026-11-27; historical page 2026-11-28 |
| CIRS Articles 101/101-B and ruling4006/2019: payer/rate/payment/waiver and residual1519 withholding | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs101.aspx ; https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs101b.aspx ; https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/informacoes_vinculativas/rendimento/cirs/Documents/PIV_16493.pdf | 2026-11-28 |
| CIRS Article 98: identical agent-remittance deadline from completed proof | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs98.aspx | 2026-11-27 |
| CIVA Article 53: only the incorporated EUR 15,000 amount reused for IRS waiver | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/civa_rep/Pages/artigo-53-o-do-civa.aspx | 2026-11-27 |
| CIRS Articles 60/97/102: filing/payment/actual credits/PPC conditions; Article 102 formula image visually read | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs60.aspx ; https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs97.aspx ; https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs102.aspx | 2026-11-28 |
| CIRS Articles 23/115: currency rules and invoice/receipt alternatives | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs23.aspx ; https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs115.aspx | 2026-11-28 |
| Portaria104/2026/1 Article 1 / actual Anexo B and C instructions: form scope, B income/credits/expense/Jovem fields and C accountant identification; not a fictional 2027 form | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/diplomas_legislativos/Documents/portaria-104-2026-1.pdf ; https://info.portaldasfinancas.gov.pt/pt/apoio_contribuinte/modelos_formularios/irs/Documents/Mod_3_anexo_B.pdf ; https://info.portaldasfinancas.gov.pt/pt/apoio_contribuinte/modelos_formularios/irs/Documents/Mod_3_anexo_C.pdf | 2026-11-28 |
| RGIT Articles116/119 and LGT Articles35/44: actual general fine/interest conditions, not individual annual-rate or waiver calculation | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/rgit/Pages/rgit116.aspx ; https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/rgit/Pages/rgit119.aspx ; https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/lgt/Pages/lgt35.aspx ; https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/lgt/Pages/lgt44.aspx | 2026-11-28 |
| Contributory Code Articles146/151-A/155/162/163/168: applicable completed social-security proof, including the identical March2025 case and AnexoSS reporting | https://diariodarepublica.pt/dr/legislacao-consolidada/lei/2009-34514575 ; https://diariodarepublica.pt/dr/legislacao-consolidada/decreto-regulamentar/2011-56720826 | 2026-11-27 |

Not yet confirmed: the individual IRS Jovem final contribution/expense/progression interaction in the held cases; residual1519 coefficient without actual activity; individual personal-credit/minimum/author relief; mixed-cost/vehicle/representation outcomes; special residence/region/NHR/IFICI/foreign-tax-credit outcomes and actual penalty reductions/annual interest liability. These are non-usable holds with their original inputs, not permissions to substitute a different year or invent a rate. Check this point with one of our partner accountants.

> Contributed by OpenAccountants.
