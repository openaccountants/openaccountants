---
name: it-income-tax
description: "Italian personal income tax (IRPEF) for self-employed professionals (lavoratori autonomi, liberi professionisti) under the regime ordinario, tax year 2026, filed in 2027. Covers the 2026 bands (23%, 33%, 43%; the middle rate cut from 35% by the Legge di Bilancio 2026, L. 199/2025), the art. 13 detrazioni for self-employed, employment and pension income and their phase-outs, the cuneo fiscale in brief, the 19% detrazioni and their cuts above EUR 75,000, 120,000 and 200,000, regional and municipal surcharges, the cash-basis professional income rules and expense limits, the 20% withholding on fees, the forfettario test and the expired flat tax incrementale, Modello Redditi PF and 730 deadlines, acconti, penalties and ravvedimento. Trigger on: IRPEF autonomo, Quadro RE, Redditi PF, detrazioni, addizionale regionale, ritenuta d'acconto 20%, ravvedimento. Out of scope, see: it-irpef-employees, it-regime-forfettario, it-estimated-tax, it-inps-contributions, it-impatriati, italy-payroll, italy-crypto-tax, it-cross-border."
version: 2.1
jurisdiction: IT
tax_year: 2026
last_updated: 2026-10-24
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Italian income tax (IRPEF) for the self-employed: regime ordinario, 2026

> **General reference only.** This skill is general tax reference material for AI-assisted work. No accountant has reviewed it. Do not rely on it to file, pay or take a tax position without review by a qualified Italian professional (commercialista).

How Italy taxes a resident self-employed professional under IRPEF for tax year 2026. The tax year is the calendar year, so 2026 income is declared and settled in 2027. The authority is the Agenzia delle Entrate; the currency is the euro. For 2026 income the TUIR of 1986 (D.P.R. 917/1986) applies; Normattiva shows it in force on 24 October 2026. A new consolidated TUIR, D.Lgs. 19 June 2026 n. 117, was published on 3 July 2026 (see "Not yet confirmed" for the date it starts to apply). Every statute here was read as in force on 24 October 2026.

This skill does not repeat its siblings:

- employees, pensioners, investment and rental income, the cuneo fiscale in full, family detrazioni: `it-irpef-employees`;
- the flat-rate regime in full (coefficients, start-up conditions, exit year): `it-regime-forfettario`;
- acconti methods (storico and previsionale), F24 codes: `it-estimated-tax`;
- INPS gestione separata rates, cap and rivalsa: `it-inps-contributions`; artigiani, commercianti and the casse: `it-inps-artigiani-commercianti`;
- inbound workers and the flat tax for new residents: `it-impatriati`; residence and treaties: `it-cross-border`;
- employer withholding, payslips and the CU: `italy-payroll`; crypto: `italy-crypto-tax`; VAT: `italy-vat-return`; IRAP: `it-irap`.

## Who this applies to

- **Resident individuals** (TUIR art. 2; the residence tests are in `it-cross-border`). They pay IRPEF on income from anywhere in the world.
- **Professionals with self-employed income** (redditi di lavoro autonomo, TUIR art. 53) taxed under the **regime ordinario**: income worked out on the cash basis (art. 54) and declared in Quadro RE of the Modello Redditi PF.
- **People with mixed income.** A professional who is also an employee or a pensioner gets only one of the art. 13 detrazioni (the rates table gives all three). The cuneo fiscale goes only to employees.

Decide the regime first. A person is in the **regime forfettario** (L. 190/2014 art. 1 commi 54-89) if, in the previous year, revenue or fees (annualised, all ATECO codes together) were not above EUR 85,000, staff and collaborator costs were not above EUR 20,000, and no exclusion in comma 57 applies (for example employment income above EUR 35,000 in 2025, a related partnership stake or S.r.l. control, or working mainly for a current or recent employer). A forfettario taxpayer pays one 15% substitute tax (5% for the first five years if the start-up conditions are met) instead of IRPEF, both surcharges and IRAP, and this skill does not apply: use `it-regime-forfettario`. The regime ends the year after a condition fails, but in the same year once revenue or fees go above EUR 100,000, with VAT due from the sale that crosses it.

**Flat tax incrementale.** The 15% substitute tax on the increase in business or professional income (L. 197/2022 art. 1 comma 55) applied "per il solo anno 2023". The text in force on 24 October 2026 has not extended it, so it is not available for 2026.

Out of scope:

- business income (reddito d'impresa: selling goods, e-commerce, trade), declared in Quadro RF or RG, not RE. The bands and detrazioni below still apply, but the income rules do not;
- non-residents beyond the points in `## Cross-border points`;
- cassa contribution rates (each fund sets its own: use the fund's statement);
- anything to be filed: every result here is an estimate for a commercialista to confirm.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| IRPEF band 1, taxable income up to EUR 28,000 | 23% | 2026 | TUIR art. 11(1)(a), https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art11!vig=2026-10-24 |
| IRPEF band 2, EUR 28,000 to 50,000 | 33% (35% in 2024 and 2025) | 2026 | TUIR art. 11(1)(b) as amended by L. 199/2025 art. 1 comma 3, https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2025-12-30;199~art1!vig=2026-10-24 |
| IRPEF band 3, above EUR 50,000 | 43% | 2026 | TUIR art. 11(1)(c), link above |
| Gross tax on the first EUR 50,000 | EUR 13,700 (was 14,140) | 2026 | Agenzia delle Entrate, IRPEF rates page, https://www.agenziaentrate.gov.it/portale/imposta-sul-reddito-delle-persone-fisiche-irpef-/aliquote-e-calcolo-dell-irpef |
| Self-employed detrazione, total income up to EUR 5,500 | EUR 1,265 | 2026 | TUIR art. 13(5)(a), https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art13!vig=2026-10-24 |
| Self-employed detrazione, EUR 5,500 to 28,000 | EUR 500 + 765 x (28,000 - total income) / 22,500 | 2026 | TUIR art. 13(5)(b), link above |
| Self-employed detrazione, EUR 28,000 to 50,000; nil above 50,000 | EUR 500 x (50,000 - total income) / 22,000 | 2026 | TUIR art. 13(5)(b-bis), link above |
| Self-employed detrazione, extra if total income is above EUR 11,000 and not above 17,000 | EUR 50 | 2026 | TUIR art. 13(5-ter), link above |
| Employment detrazione, total income up to EUR 15,000 (minimum 690; 1,380 for fixed-term) | EUR 1,955 | 2026 | TUIR art. 13(1)(a), link above |
| Employment detrazione, EUR 15,000 to 28,000 | EUR 1,910 + 1,190 x (28,000 - total income) / 13,000 | 2026 | TUIR art. 13(1)(b), link above |
| Employment detrazione, EUR 28,000 to 50,000; nil above 50,000 | EUR 1,910 x (50,000 - total income) / 22,000 | 2026 | TUIR art. 13(1)(c), link above |
| Employment detrazione, extra if total income is above EUR 25,000 and not above 35,000 | EUR 65 | 2026 | TUIR art. 13(1.1), link above |
| Pension detrazione, total income up to EUR 8,500 (minimum 713) | EUR 1,955 | 2026 | TUIR art. 13(3)(a), link above |
| Pension detrazione, EUR 8,500 to 28,000 | EUR 700 + 1,255 x (28,000 - total income) / 19,500 | 2026 | TUIR art. 13(3)(b), link above |
| Pension detrazione, EUR 28,000 to 50,000; nil above 50,000 | EUR 700 x (50,000 - total income) / 22,000 | 2026 | TUIR art. 13(3)(c), link above |
| Pension detrazione, extra if total income is above EUR 25,000 and not above 29,000 | EUR 50 | 2026 | TUIR art. 13(3-bis), link above |
| Cuneo fiscale, employees with total income up to EUR 20,000: tax-free sum, share of employment income | 7.1% / 5.3% / 4.8% (pay up to 8,500 / up to 15,000 / above) | 2026 | L. 207/2024 art. 1 comma 4, https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2024-12-30;207~art1!vig=2026-10-24 |
| Cuneo fiscale, employees with total income above EUR 20,000: extra detrazione | EUR 1,000 to 32,000, then 1,000 x (40,000 - total income) / 8,000; nil above 40,000 | 2026 | L. 207/2024 art. 1 comma 6, link above |
| Detrazioni for oneri (art. 15), e.g. medical costs above EUR 129.11 | 19% | 2026 | D.Lgs. 446/1997 art. 49(1), https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-15;446~art49!vig=2026-10-24; Agenzia, https://www.agenziaentrate.gov.it/portale/le-spese-sanitarie-e-i-mezzi-di-ausilio |
| 19% detrazioni in full up to total income of | EUR 120,000; then x (240,000 - total income) / 120,000; nil from 240,000 | 2026 | TUIR art. 15(3-bis), https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art15!vig=2026-10-24 |
| Cap on oneri giving a detrazione, total income above EUR 75,000 and up to 100,000: base amount | EUR 14,000 | 2026 | TUIR art. 16-ter(1)-(2), https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art16ter!vig=2026-10-24 |
| Same cap, total income above EUR 100,000: base amount | EUR 8,000 | 2026 | TUIR art. 16-ter(2)(b), link above |
| Cap coefficient by qualifying children: none / one / two / more or a disabled child | 0.50 / 0.70 / 0.85 / 1 | 2026 | TUIR art. 16-ter(3), link above |
| Cut to 19% detrazioni (not medical), political gifts and disaster insurance, total income above EUR 200,000 | EUR 440 | 2026 | TUIR art. 16-ter(5-bis), inserted by L. 199/2025 art. 1 comma 4, link above |
| Addizionale regionale, base rate | 1.23%; regions may add up to 2.1 points | 2026 | D.Lgs. 68/2011 art. 6, https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2011-05-06;68~art6!vig=2026-10-24 |
| Addizionale comunale, maximum rate set by the comune | 0.8% | 2026 | D.Lgs. 360/1998 art. 1, https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1998-09-28;360~art1!vig=2026-10-24 |
| Withholding on account on fees paid to resident professionals by a withholding agent | 20% | 2026 | Agenzia, rates on self-employed income, https://www.agenziaentrate.gov.it/portale/schede/pagamenti/versamento-modello-f24-ritenute-su-reddito-di-lavoro-autonomo-f24_rit_red_lav_aut/aliquote-f24_rit_red_lav_aut |
| Forfettario entry limit, previous-year revenue or fees | EUR 85,000 | 2026 | L. 190/2014 art. 1 comma 54(a), https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2014-12-23;190~art1!vig=2026-10-24 |
| Forfettario same-year exit | above EUR 100,000 | 2026 | L. 190/2014 art. 1 comma 71, link above |
| Forfettario staff and collaborator costs, previous year | EUR 20,000 | 2026 | L. 190/2014 art. 1 comma 54(b), link above |
| Forfettario exclusion: previous-year employment income above | EUR 35,000 (EUR 30,000 standing rule) | 2025 and 2026 | L. 207/2024 art. 1 comma 12 as amended by L. 199/2025 art. 1 comma 27 |
| Forfettario substitute tax / start-up rate | 15% / 5% | 2026 | L. 190/2014 art. 1 commi 64-65, link above |
| Small asset expensed in full in the year bought, unit cost up to | EUR 516.40 | 2026 | TUIR art. 54-quinquies(1), https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art54quinquies!vig=2026-10-24 |
| Goods and premises used both for work and privately | 50% | 2026 | TUIR art. 54-quinquies, link above |
| Telecom equipment and its running costs | 80% | 2026 | TUIR art. 54-quinquies, link above |
| Hotel and meals: share deductible / overall cap as share of fees received | 75% / 2% | 2026 | TUIR art. 54-septies(1), https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art54septies!vig=2026-10-24 |
| Entertainment (rappresentanza) cap, share of fees received | 1% | 2026 | TUIR art. 54-septies, link above |
| Training, masters, conferences with travel and stay: yearly cap | EUR 10,000 | 2026 | TUIR art. 54-septies(3), link above |
| Car used by an individual professional, one vehicle only | 20% | 2026 | TUIR art. 164, https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art164!vig=2026-10-24 |
| Car used by sales agents / car given to an employee for mixed use | 80% / 70% | 2026 | TUIR art. 164, link above |
| Occasional self-employment: INPS enrolment only if yearly income from it is above | EUR 5,000 | 2026 | D.L. 269/2003 art. 44, https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2003-09-30;269~art44!vig=2026-10-24 |
| Cash payments between different persons prohibited at or above | EUR 5,000 | 2026 | D.Lgs. 231/2007 art. 49, https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2007-11-21;231~art49!vig=2026-10-24 |
| Crypto gains, substitute tax (euro e-money tokens 26%) | 33% | 2026 | L. 207/2024 art. 1 comma 24 as amended by L. 199/2025 art. 1 comma 28 |

How the table works:

- **Why 19% and not 22%.** Normattiva's text of TUIR art. 15(1) still prints "22 per cento". The rate was fixed at 19% for oneri paid from 1998 by D.Lgs. 446/1997 art. 49, which did not amend the words of art. 15, so the consolidated text never changed. L. 199/2025 did not change the rate: it only refers to oneri "nella misura del 19 per cento" in the new art. 16-ter(5-bis).
- **Bands** apply to taxable income: total income (reddito complessivo) less oneri deducibili (art. 10), such as compulsory INPS or cassa contributions paid in the year. Each rate applies only to the slice inside its band.
- **Detrazioni** come off gross tax, never off income, and only up to the tax due: no refund of the excess (art. 11(3)). The art. 13 detrazioni use **total income**, before oneri deducibili and without the main home (art. 13(6-bis)). Each ratio is taken to four decimal places, cut off, not rounded (art. 13(6)).
- **One art. 13 detrazione only.** The self-employed one (comma 5) cannot be combined with the employment (comma 1) or pension (comma 3) one. Employment and pension amounts are scaled to the days worked or drawn in the year; the self-employed one is not.
- **No-tax area for the self-employed.** EUR 1,265 is 23% of EUR 5,500, so with no other income or oneri no IRPEF is due up to EUR 5,500 of total income.
- **Order for oneri.** First the art. 16-ter cap (above EUR 75,000), then the art. 15(3-bis) phase-out (above EUR 120,000), then the EUR 440 cut (above EUR 200,000). Medical costs and mortgage interest (art. 15(1)(a), (b) and (1-ter)) are outside the art. 15(3-bis) phase-out at any income (art. 15(3-quater)), and medical costs are also outside the EUR 440 cut. Medical costs and some start-up investments are outside the art. 16-ter cap; mortgage interest, insurance and multi-year building instalments from contracts or spending up to 31 December 2024 are also outside it (art. 16-ter(4)-(5)).
- **Cuneo fiscale** is for employees only (L. 207/2024 commi 4-9). A professional with no employment income gets neither part. The details, the separate trattamento integrativo and the 2026 payroll substitute taxes are in `it-irpef-employees` and `italy-payroll`.

## The taxable base

**Professional income on the cash basis (TUIR art. 54).** Fees received in the year less costs paid in the year, net of VAT. A fee from a withholding agent received in January counts in the year the agent had to withhold. Not income (art. 54(2)): contributions the law itself puts on the client (the cassa contributo integrativo), job expenses recharged analytically to the client, recharges of shared office costs. The optional 4% gestione separata rivalsa is part of the fee and subject to withholding (see `it-inps-contributions`). Interest on the business account is capital income, not professional income.

**Expense limits** (rates table for the figures):

- **Mixed-use goods and premises** at 50% (art. 54-quinquies). A home also used as an office: 50% of the rent (or of the rendita if owned) and running costs, only if there is no other office in the same comune. Work-only premises: in full.
- **Telecom equipment and use** at 80%.
- **Assets.** Unit cost up to EUR 516.40: expensed in the year bought. Above it: depreciated at no more than the ministerial coefficients, halved in the first year.
- **Hotel and meals** at 75%, within a total cap of 2% of fees received; meals with no work purpose: nil.
- **Entertainment** within 1% of fees received, paid traceably.
- **Training** in full up to the yearly cap.
- **Car.** One vehicle at 20% for an individual professional; the cost cap in art. 164 is still printed in lire ("lire 35 milioni"). Higher shares only for agents and employee cars, with evidence.
- **Traceable payment.** Meals, lodging, travel and taxis in Italy are deductible only if paid by bank, post or another traceable method (art. 54-septies(6-bis)).
- **Never deductible:** IRPEF, surcharges and VAT paid by F24 (they are taxes, not costs).

**Contributions.** Compulsory gestione separata or cassa contributions paid in the year are oneri deducibili. They come off total income, not off professional income (Agenzia IRPEF page). A cassa member pays the fund, not the gestione separata.

**The computation.** Fees less costs = net professional income (Quadro RE). Add other income = total income. Less oneri deducibili = taxable income. Apply the bands = gross tax. Less the art. 13 detrazione, other detrazioni (art. 15 and others) = net IRPEF. Less the 20% withholdings suffered and the acconti paid = balance due or credit. Then the surcharges: both are worked out on taxable income at the region's and comune's own rates, and the comunale is due only if net IRPEF is due for the year (D.Lgs. 360/1998 art. 1(4)). A comune may set an exemption threshold. Forfettario income is outside both.

**Reading bank lines.** Credits such as BONIFICO DA, VB DA, ACCREDITO, STRIPE, PAYPAL, SATISPAY, NEXI, SUMUP or ZETTLE payouts are receipts: gross up card and platform payouts to the amount in the processor report, and deduct the fee. STIPENDIO is employment income, INTERESSI ATTIVI capital income, PAGAMENTO F24 a tax (exclude), RIMBORSO SPESE income unless recharged analytically. Selling goods online (an e-commerce payout pattern) points to business income in Quadro RF or RG: flag it. A credit from a recent employer may block the forfettario. Italian banks print amounts as 1.234,56; app banks (N26, Revolut) as 1234.56, and in a Revolut export only COMPLETED rows count.

**Red flags.** Previous-year fees at or below EUR 85,000 (test the forfettario first); contributions far below the rate on net income; no acconti paid; cash payments at or above EUR 5,000; any cost with no document (reject it); one client providing nearly all fees.

**Other income that stays out of Quadro RE.** Crypto gains (33% substitute tax, `italy-crypto-tax`); occasional self-employment with no VAT number (income from art. 67, can go on the 730; INPS only above EUR 5,000); foreign fees paid with foreign tax (see `## Cross-border points`).

## Deadlines and filing

| Item | Deadline for 2026 income | Source |
|---|---|---|
| Modello Redditi PF, online | 15 April to 31 October 2027. 31 October 2027 is a Sunday, so it moves to the first working day after | D.P.R. 322/1998 art. 2(1); D.L. 70/2011 art. 7(2)(l) |
| Modello Redditi PF on paper at a post office (only where paper is allowed) | 15 April to 30 June 2027 | D.P.R. 322/1998 art. 2(1) |
| Modello 730 (employees, pensioners, and self-employed income needing no VAT number) | 30 September 2027 | D.M. 164/1999 art. 13; Agenzia, 730/2026 page (30 September 2026 for 2025 income) |
| IRPEF balance for 2026 and first acconto for 2027 | 30 June 2027, or the next 30 days with a 0.40% surcharge | Agenzia, "Come si paga l'Irpef" |
| Second or single acconto for 2026 | 30 November 2026 | Agenzia, "Come si paga l'Irpef" |

- **Which return.** A professional with a VAT number files the Modello Redditi PF. The 730 is not for income that needs a VAT number.
- **Late return.** A return filed within 90 days of the deadline is valid, with penalties for the delay; after 90 days it counts as not filed (D.P.R. 322/1998 art. 2(7)).
- **Acconti.** No acconto if the tax declared for the year, after detrazioni, credits and withholdings, is not above EUR 51.65. Otherwise the acconto is 100% of it (or of the lower tax expected). Below EUR 257.52: one payment by 30 November; otherwise 40% by 30 June and 60% by 30 November. Taxpayers subject to ISA pay two equal instalments on the same dates, or one by 30 November if the total is not above EUR 206. Methods and F24 codes: `it-estimated-tax`.
- **Payment** is by F24, online.

## Penalties and interest

| Item | Rule | Source |
|---|---|---|
| Return not filed | 120% of the tax due, minimum EUR 250; no tax due: EUR 250 to 1,000 (up to double for those who must keep books) | D.Lgs. 471/1997 art. 1(1), https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;471~art1!vig=2026-10-24 |
| Return filed more than 90 days late, before any audit and within the assessment period | 75% of the tax due (three times the 25% late-payment penalty) | D.Lgs. 471/1997 art. 1(1-bis), link above |
| Understated return (infedele) | 70% of the extra tax, minimum EUR 150; cut by a third if the extra tax is under 3% of the tax declared and under EUR 30,000 | D.Lgs. 471/1997 art. 1(2) and (4), link above |
| Late payment | 25% of the unpaid amount; half (12.5%) if paid within 90 days; within 15 days, one fifteenth of that half for each day late | D.Lgs. 471/1997 art. 13(1), https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;471~art13!vig=2026-10-24 |
| Ravvedimento: unpaid tax or acconto paid within 30 days | one tenth of the minimum penalty | D.Lgs. 472/1997 art. 13(1)(a), https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;472~art13!vig=2026-10-24 |
| Ravvedimento: within 90 days of the error, or of the return deadline for errors in the return | one ninth of the minimum | D.Lgs. 472/1997 art. 13(1)(a-bis), link above |
| Ravvedimento: by the return deadline for the year of the violation | one eighth of the minimum | D.Lgs. 472/1997 art. 13(1)(b), link above |
| Ravvedimento: after that deadline | one seventh of the minimum | D.Lgs. 472/1997 art. 13(1)(b-bis), link above |
| Ravvedimento: return filed up to 90 days late | one tenth of the minimum omitted-return penalty (EUR 25 on the EUR 250 minimum) | D.Lgs. 472/1997 art. 13(1)(c), link above |
| Interest with ravvedimento | legal rate, day by day: 1.60% a year from 1 January 2026 | D.Lgs. 472/1997 art. 13(2); D.M. 10 December 2025, GU n. 289 of 13 December 2025 |

Ravvedimento is barred once a notice of assessment or liquidation is served (art. 13(1-ter)). The reduced penalty, the tax and the interest are paid together. Smaller reductions (one sixth, one fifth, one quarter) apply after an audit report or a draft assessment (art. 13(1)(b-ter) to (b-quinquies)); refer those. Invoice and VAT penalties are in `italy-vat-return`.

## Cross-border points

- **Residence** decides the base: residents pay on worldwide income, non-residents only on income produced in Italy (Agenzia IRPEF page). The residence tests and treaties are in `it-cross-border`.
- **Non-residents** may deduct only some oneri (TUIR art. 24(2)) and claim only some detrazioni (art. 24(3)). A non-resident with at least 75% of total income from Italy and no similar relief at home ("Schumacker") gets all deductions and detrazioni (Agenzia IRPEF page; D.M. 21 September 2015).
- **Fees paid to non-residents** for work done in Italy bear a final 30% withholding (Agenzia withholding page), unless a treaty reduces it.
- **Foreign clients.** Fees a resident earns abroad are taxed in Italy; foreign tax may give a credit under TUIR art. 165 within its limits. Check the treaty and escalate.
- **Inbound workers** may exempt part of their income under the impatriati regime, and new residents may opt for the EUR 300,000 flat tax on foreign income (raised from EUR 200,000 for those moving from 1 January 2026, L. 199/2025 art. 1 commi 25-26): see `it-impatriati`.
- **Forfettario for EU and EEA residents** is open only to those producing at least 75% of their income in Italy (Agenzia forfettario page).

## Worked examples

### Example 1: Graphic designer in Milan, regime ordinario, 2026

Fees received in 2026, net of VAT: EUR 60,000, of which EUR 40,000 from business clients that withheld 20%. Deductible costs paid: EUR 14,000. Gestione separata contributions paid in 2026: EUR 9,000. No other income, no oneri giving a detrazione.

Net professional income is 60,000 less 14,000 = EUR 46,000, which is also total income. Taxable income is 46,000 less the 9,000 contributions = EUR 37,000. Gross tax: 23% of 28,000 = 6,440, plus 33% of 9,000 = 2,970, total EUR 9,410. The self-employed detrazione uses total income: (50,000 - 46,000) / 22,000 = 0.181818, cut to 0.1818, times 500 = EUR 90.90. Net IRPEF EUR 9,319.10. Withholdings were 20% of 40,000 = EUR 8,000, so EUR 1,319.10 is due by 30 June 2027, before the surcharges at the Lombardy and Milan rates and before acconti.

```oa-check
name: Self-employed designer, fees EUR 60,000, regime ordinario (2026 bands)
inputs:
  fees: 60000
  costs: 14000
  contributions: 9000
  fees_withheld: 40000
steps:
  - net_income: fees - costs
  - taxable: net_income - contributions
  - band_23: min(taxable, 28000) * 0.23
  - band_33: (min(taxable, 50000) - 28000) * 0.33
  - gross_tax: band_23 + band_33
  - ratio: floor((50000 - net_income) / 22000 * 10000) / 10000
  - detrazione: round(500 * ratio, 2)
  - net_irpef: gross_tax - detrazione
  - withholding: fees_withheld * 0.2
  - balance: net_irpef - withholding
expected:
  net_income: 46000
  taxable: 37000
  gross_tax: 9410.00
  ratio: 0.1818
  detrazione: 90.90
  net_irpef: 9319.10
  withholding: 8000.00
  balance: 1319.10
```

### Example 2: Consultant above EUR 75,000 with one child, the art. 16-ter cap (2026)

Net professional income EUR 95,000 (total income). Gestione separata contributions paid EUR 15,000. One qualifying child. Oneri at 19% paid in 2026: EUR 12,000, none medical, all from contracts made after 2024, each already within its own limit.

Taxable income is 95,000 less 15,000 = EUR 80,000. Gross tax: 13,700 on the first 50,000 plus 43% of 30,000 = 12,900, total EUR 26,600. Total income is above EUR 50,000, so there is no self-employed detrazione. Total income is above EUR 75,000 and not above 100,000, so the oneri count only up to 14,000 x 0.70 = EUR 9,800. Total income is not above EUR 120,000, so no phase-out, and not above EUR 200,000, so no EUR 440 cut. Detrazione: 19% of 9,800 = EUR 1,862. Net IRPEF EUR 24,738, before withholdings, acconti and the surcharges. Without the cap the detrazione would have been 19% of 12,000 = EUR 2,280.

```oa-check
name: Consultant, total income EUR 95,000, art. 16-ter cap, one child (2026)
inputs:
  net_income: 95000
  contributions: 15000
  oneri_19: 12000
  coefficient: 0.70
steps:
  - taxable: net_income - contributions
  - band_23: min(taxable, 28000) * 0.23
  - band_33: (min(taxable, 50000) - 28000) * 0.33
  - band_43: max(taxable - 50000, 0) * 0.43
  - gross_tax: band_23 + band_33 + band_43
  - autonomo: 500 * clamp((50000 - net_income) / 22000, 0, 1)
  - cap: 14000 * coefficient
  - allowed: min(oneri_19, cap)
  - phase: clamp((240000 - net_income) / 120000, 0, 1)
  - detrazione_19: round(allowed * 0.19 * phase, 2)
  - net_irpef: gross_tax - autonomo - detrazione_19
expected:
  taxable: 80000
  gross_tax: 26600.00
  autonomo: 0
  cap: 9800.00
  allowed: 9800.00
  phase: 1
  detrazione_19: 1862.00
  net_irpef: 24738.00
```

## Ask the client first

- Revenue or fees in 2025, and so far in 2026, and staff costs? (Forfettario entry and same-year exit.)
- Any employment or pension income in 2025 or 2026, how much, and did the job end? (Forfettario bar; which art. 13 detrazione.)
- A cassa member, or only the INPS gestione separata? Already a pensioner? Rivalsa added on invoices?
- Region and comune of tax residence? (Surcharge rates.)
- Total income likely above EUR 75,000, 120,000 or 200,000, and how many qualifying children? (Detrazione caps.)
- Work from home with no other office in the comune, one car for work, any clients abroad?

## Sources

| Source | URL | Read on |
|---|---|---|
| TUIR, D.P.R. 917/1986, art. 11 (bands) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art11!vig=2026-10-24 | 2026-10-24 |
| TUIR art. 13 (detrazioni by type of income) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art13!vig=2026-10-24 | 2026-10-24 |
| TUIR art. 15 (detrazioni for oneri, phase-out above EUR 120,000) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art15!vig=2026-10-24 | 2026-10-24 |
| TUIR art. 16-ter (cap above EUR 75,000; EUR 440 cut above EUR 200,000) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art16ter!vig=2026-10-24 | 2026-10-24 |
| TUIR art. 54 (professional income, cash basis) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art54!vig=2026-10-24 | 2026-10-24 |
| TUIR art. 54-quinquies (assets, mixed use, telecoms) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art54quinquies!vig=2026-10-24 | 2026-10-24 |
| TUIR art. 54-septies (hotel, meals, entertainment, training, traceability) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art54septies!vig=2026-10-24 | 2026-10-24 |
| TUIR art. 164 (vehicles) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art164!vig=2026-10-24 | 2026-10-24 |
| L. 199/2025 (Legge di Bilancio 2026), art. 1 commi 3-4, 25-28 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2025-12-30;199~art1!vig=2026-10-24 | 2026-10-24 |
| L. 207/2024 (Legge di Bilancio 2025), art. 1 commi 2-12 (cuneo fiscale, art. 16-ter, forfettario EUR 35,000) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2024-12-30;207~art1!vig=2026-10-24 | 2026-10-24 |
| L. 197/2022, art. 1 comma 55 (flat tax incrementale, 2023 only) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2022-12-29;197~art1!vig=2026-10-24 | 2026-10-24 |
| L. 190/2014, art. 1 commi 54-89 (regime forfettario) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2014-12-23;190~art1!vig=2026-10-24 | 2026-10-24 |
| D.Lgs. 68/2011 art. 6 (addizionale regionale) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2011-05-06;68~art6!vig=2026-10-24 | 2026-10-24 |
| D.Lgs. 360/1998 art. 1 (addizionale comunale) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1998-09-28;360~art1!vig=2026-10-24 | 2026-10-24 |
| D.P.R. 322/1998 art. 2 (Redditi PF deadlines, late returns) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1998-07-22;322~art2!vig=2026-10-24 | 2026-10-24 |
| D.M. 164/1999 art. 13 (730 by 30 September) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:ministero.finanze:decreto:1999-05-31;164~art13!vig=2026-10-24 | 2026-10-24 |
| D.L. 70/2011 art. 7(2)(l) (deadlines on a Saturday or holiday) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2011-05-13;70~art7!vig=2026-10-24 | 2026-10-24 |
| D.Lgs. 446/1997 art. 49 (19% rate for oneri from 1998) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-15;446~art49!vig=2026-10-24 | 2026-10-24 |
| D.Lgs. 471/1997 arts. 1 and 13 (penalties) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;471~art1!vig=2026-10-24 | 2026-10-24 |
| D.Lgs. 472/1997 art. 13 (ravvedimento) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;472~art13!vig=2026-10-24 | 2026-10-24 |
| D.M. 10 December 2025, legal interest rate for 2026 (GU n. 289, 13 December 2025) | https://www.gazzettaufficiale.it/atto/vediMenuHTML?atto.dataPubblicazioneGazzetta=2025-12-13&atto.codiceRedazionale=25A06705&tipoSerie=serie_generale&tipoVigenza=originario | 2026-10-24 |
| D.L. 269/2003 art. 44 (occasional work, INPS) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2003-09-30;269~art44!vig=2026-10-24 | 2026-10-24 |
| D.Lgs. 231/2007 art. 49 (cash limit) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2007-11-21;231~art49!vig=2026-10-24 | 2026-10-24 |
| Agenzia delle Entrate, IRPEF rates and calculation (notes the 33% rate) | https://www.agenziaentrate.gov.it/portale/imposta-sul-reddito-delle-persone-fisiche-irpef-/aliquote-e-calcolo-dell-irpef | 2026-10-24 |
| Agenzia delle Entrate, how IRPEF is paid (acconti) | https://www.agenziaentrate.gov.it/portale/come-si-paga-l-irpef | 2026-10-24 |
| Agenzia delle Entrate, when to file the 730/2026 | https://www.agenziaentrate.gov.it/portale/quando-e-come-presentare-il-730-2026 | 2026-10-24 |
| Agenzia delle Entrate, regime forfettario rules | https://www.agenziaentrate.gov.it/portale/regime-forfetario-le-regole-2020-/infogen-regime-forfetario-le-regole-2020- | 2026-10-24 |
| Agenzia delle Entrate, withholding rates on self-employed income | https://www.agenziaentrate.gov.it/portale/schede/pagamenti/versamento-modello-f24-ritenute-su-reddito-di-lavoro-autonomo-f24_rit_red_lav_aut/aliquote-f24_rit_red_lav_aut | 2026-10-24 |
| Agenzia delle Entrate, medical expenses (19% above EUR 129.11, traceable payment) | https://www.agenziaentrate.gov.it/portale/le-spese-sanitarie-e-i-mezzi-di-ausilio | 2026-10-24 |

Not yet confirmed:

- **New TUIR start date.** D.Lgs. 117/2026 is on Normattiva (in force 4 July 2026), but the article that sets when it starts to apply (reported as 1 January 2027) was not read in the official text.
- **Consolidated codes from 2027.** The 2026 balance, the acconti and any penalties fall in 2027, when D.Lgs. 33/2025 (payments) and D.Lgs. 173/2024 (penalties) apply with new article numbers. We did not read whether they change any figure above.
- **Depreciation coefficients** (D.M. 31 December 1988) and the car cost cap in euro: not read.
- **Regional and municipal rates for 2026**: each region and comune sets its own; none read.
- **ISA**: which professions are subject to ISA (equal acconti) was not read; see `it-estimated-tax`.
- **Moved, not dropped:** the gestione separata rates and cap (26.07%, 24%, EUR 122,295, EUR 18,808) are in `it-inps-contributions`; the forfettario coefficients (78%, 67% and the full table) in `it-regime-forfettario`; the 2026 cuneo fiscale detail and family detrazioni in `it-irpef-employees`.

> Contributed by OpenAccountants.

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
