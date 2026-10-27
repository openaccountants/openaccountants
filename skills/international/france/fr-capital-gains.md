---
name: fr-capital-gains
description: "France capital gains and investment income of resident individuals, tax year 2026 (income of 2025 declared in 2026, and income of 2026). Covers gains on securities under the flat tax (PFU 12.8% plus social levies of 18.6% for disposals from 1 January 2025) or the global option for the progressive scale, holding allowances on pre-2018 shares, losses carried forward ten years, dividends and interest, PEA, life insurance withdrawals, free shares, RSUs, BSPCE, stock options, employee savings and PER exits, and property gains (19% plus 17.2% social levies, duration allowances, surtax above EUR 50,000, main-home exemption), forms 2074 and 2048-IMM, and penalties. Trigger on plus-value, PFU, flat tax, option barème, 2074, 2048-IMM, abattement pour durée de détention, résidence principale, PEA, assurance-vie, AGA, BSPCE, stock-options. Out of scope: crypto (fr-crypto-tax), non-residents (fr-cross-border), exit tax (leaving-france-exit-tax), rental income (fr-rental-income), household computation (fr-personal-income-tax)."
version: 1.1
jurisdiction: FR
tax_year: 2026
last_updated: 2026-10-26
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# France: capital gains, investment income and employee shares

The return filed in 2026 covers income received and disposals made in 2025. Income and disposals of 2026 are declared in 2027. Where the two years differ, this skill names the year. Crypto gains are in `fr-crypto-tax`, rental income in `fr-rental-income`, the progressive scale and the household computation in `fr-personal-income-tax`, the CSG and CRDS in `fr-social-contributions`, non-residents in `fr-cross-border`, and the exit tax in `leaving-france-exit-tax`.

## Who this applies to

- **In scope:** individuals who are French tax residents (CGI art. 4 B), taxed on dividends, interest, gains on securities (CGI art. 150-0 A ff.), the PEA, life insurance withdrawals, employee shares, employee savings, PER exits, and gains on property held privately (CGI art. 150 U ff.).
- **Social levies** (CSG, CRDS, solidarity levy) apply on top of income tax to residents (CSS L. 136-6, L. 136-7). A resident insured in another EEA state or Switzerland pays only the 7.5% solidarity levy (F2329).
- **Out of scope:** companies, professional traders in securities, property dealers, property held by a company, building land, non-residents (pointer in Cross-border points), crypto-assets (`fr-crypto-tax`).

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| PFU, income tax part, on dividends, interest and gains on securities (CGI art. 200 A, 1) | 12.8% | 2025 and 2026 | https://www.service-public.gouv.fr/particuliers/vosdroits/F2613 |
| Social levies on gains on securities (income from wealth): CSG 10.6% + CRDS 0.5% + solidarity 7.5% | 18.6% | Disposals from 1 Jan 2025 (17.2% before) | https://www.service-public.gouv.fr/particuliers/vosdroits/F2329 |
| Social levies on dividends and interest (investment income) | 17.2% if received in 2025; 18.6% if received from 1 Jan 2026 | 2025 / 2026 | same page |
| Social levies on property gains, rental income, life insurance, PEL, CEL, PEP (CSG kept at 9.2%) | 17.2% | 2025 and 2026 | same page |
| Life insurance contracts of rente-survie and épargne handicap | 18.6% | 2026 | https://www.service-public.gouv.fr/particuliers/vosdroits/F22414 |
| Deductible CSG, only under the progressive-scale option | 6.8% | 2025 and 2026 | https://www.service-public.gouv.fr/particuliers/vosdroits/F2329 |
| Dividend allowance, only under the scale option (CGI art. 158, 3-2°) | 40% | 2025 and 2026 | https://www.service-public.gouv.fr/particuliers/vosdroits/F2613 |
| Ordinary holding allowance, shares bought before 1 Jan 2018, scale option only: 2 to under 8 years / 8 years or more | 50% / 65% | 2025 and 2026 | https://www.impots.gouv.fr/particulier/questions/jai-realise-des-plus-values-ai-je-droit-un-abattement-pour-duree-de-detention |
| Enhanced allowance (young SME shares): over 1 to under 4 years / over 4 to under 8 / 8 or more | 50% / 65% / 85% | 2025 and 2026 | same page |
| Fixed allowance, retiring SME director (CGI art. 150-0 D ter), disposals 2018 to 2031 | EUR 500,000 (EUR 600,000 farm to young farmer, from 2025) | 2025 and 2026 | https://www.impots.gouv.fr/particulier/questions/dirigeant-de-pme-partant-la-retraite-comment-sera-imposee-la-plus-value-que-je |
| Advance payment excuse, reference income limit, dividends | EUR 50,000 single / EUR 75,000 couple | 2026 | https://www.service-public.gouv.fr/particuliers/vosdroits/F2613 |
| Advance payment excuse, reference income limit, interest | EUR 25,000 single / EUR 50,000 couple | 2026 | same page |
| PEA payment ceiling / with PEA PME-ETI / adult attached to parents | EUR 150,000 / EUR 225,000 / EUR 20,000 | 2026 | https://www.service-public.gouv.fr/particuliers/vosdroits/F2385 |
| Life insurance, premiums from 27 Sep 2017: contract under 8 years / 8 years or more (up to EUR 150,000 of premiums) | 12.8% / 7.5% | 2026 | https://www.service-public.gouv.fr/particuliers/vosdroits/F22414 |
| Life insurance yearly allowance, contract 8 years or more | EUR 4,600 single / EUR 9,200 couple | 2026 | same page |
| Life insurance, premiums before 27 Sep 2017, optional final withholding: under 4 / 4 to 8 / 8 years or more | 35% / 15% / 7.5% | 2026 | https://www.impots.gouv.fr/www2/fichiers/documentation/brochure/ir_2026/pdf_som/08-RCM_121a136.pdf |
| Free shares (plans from 1 Jan 2018): gain up to EUR 300,000 a year: scale after 50% allowance, levies | 50% allowance; 18.6% | 2026 | https://www.impots.gouv.fr/particulier/questions/mon-entreprise-ma-attribue-des-actions-gratuites-comment-sera-impose-le-gain |
| Free shares: part above EUR 300,000: salary rules, levies 9.7%, employee contribution | 9.7%; 10% | 2026 | same page |
| BSPCE, shares subscribed from 1 Jan 2025: exercise gain, 3 years or more / under 3 years; sale gain; levies | 12.8% / 30%; PFU 12.8%; 18.6% | 2026 | https://www.impots.gouv.fr/particulier/questions/jai-vendu-des-bons-de-souscription-de-parts-de-createurs-dentreprise-ou-bspce |
| BSPCE before 1 Jan 2025: granted to 2017 with 3 years or more / any grant under 3 years | 19% / 30% | 2026 | same page |
| Stock options from 28 Sep 2012: levies on exercise gain / employee contribution | 9.7% / 10% | 2026 | https://www.impots.gouv.fr/particulier/questions/jai-des-stock-options-comment-est-impose-le-gain-levee-doptions |
| Stock options 27 Apr 2000 to 28 Sep 2012, lock-up kept: up to EUR 152,500 / above (18% if 2-year holding also kept) | 30% / 41% | 2026 | same page |
| Property gain, income tax (CGI art. 200 B) | 19% | 2025 and 2026 | https://www.service-public.gouv.fr/particuliers/vosdroits/F10864 |
| Property duration allowance, income tax: years 6 to 21 / 22nd year / beyond 22 | 6% a year / 4% / exempt | 2025 and 2026 | same page |
| Property duration allowance, social levies: years 6 to 21 / 22nd year / years 23 to 30 | 1.65% a year / 1.6% / 9% a year (exempt beyond 30) | 2025 and 2026 | same page |
| Property: flat acquisition costs / flat works (held over 5 years) | 7.5% / 15% of the purchase price | 2025 and 2026 | same page |
| Property: sale exempt if price does not exceed | EUR 15,000 | 2025 and 2026 | same page |
| Surtax on property gains (CGI art. 1609 nonies G): taxable gain above EUR 50,000 | 2% to 6% by bracket, with smoothing | 2025 and 2026 | https://bofip.impots.gouv.fr/bofip/8597-PGP.html |
| Late filing surcharge (CGI art. 1728) | 10% / 40% after formal notice / 80% hidden activity | 2026 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000028312309/2026-10-24 |
| Late payment interest (CGI art. 1727) | 0.20% per month | 2026 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000029355562/2026-10-24 |

**Surtax brackets** (BOFiP BOI-RFPI-TPVIE-20, PV = taxable gain after the income tax allowance): 50,001 to 60,000: 2% x PV - (60,000 - PV) x 1/20; 60,001 to 100,000: 2% x PV; 100,001 to 110,000: 3% x PV - (110,000 - PV) x 1/10; 110,001 to 150,000: 3% x PV; 150,001 to 160,000: 4% x PV - (160,000 - PV) x 15/100; 160,001 to 200,000: 4% x PV; 200,001 to 210,000: 5% x PV - (210,000 - PV) x 20/100; 210,001 to 250,000: 5% x PV; 250,001 to 260,000: 6% x PV - (260,000 - PV) x 25/100; above 260,000: 6% x PV.

**When the CSG rise applies.** LFSS 2026 (loi n° 2025-1403), art. 12, raised the CSG on capital income from 9.2% to 10.6% (CSS L. 136-8 I 2°). It applies to income assessed with income tax from the 2025 income year (gains on securities sold in 2025 and declared in 2026 bear 18.6%), and to income taxed at source (dividends, interest) from 1 January 2026. Property gains, rental income, life insurance and home savings stay at 9.2% CSG, so 17.2% in total (L. 136-8 IV). The same rule is in `fr-social-contributions`.

## The taxable base

**Gains on securities.** Shares, company shares (parts sociales) and fund units. Gain = sale price net of fees minus purchase price and fees. Losses of the year are set first against gains of the same year; any unused loss is carried forward against gains of the next ten years (CGI art. 150-0 D, 11; brochure, plus-values). Declared on the 2042 C box 3VG, with form 2074 unless the bank has computed every gain and no allowance or carried-forward loss is used.

- **PFU or scale.** The PFU is the default. The household may opt for the progressive scale by ticking box 2OP (CGI art. 200 A, 2). The option is global: it covers all dividends, interest and gains on securities of the year. For income of 2025 it is irrevocable. For income of 2026 onwards, F2613 says it can be withdrawn within the claim period or during an audit. Crypto has its own option (box 3CN, `fr-crypto-tax`).
- **What the scale brings.** The 40% dividend allowance, the holding allowances on shares bought before 1 January 2018, the 6.8% deductible CSG, and the deduction of fees. Under the PFU, none of these. F2613: the scale helps at a marginal rate of 0% or 11%; at 30% or more the PFU rate is lower. At 30% with dividends, compute both. Band limits are in `fr-personal-income-tax`.
- **Holding allowances** apply only if the shares were bought before 1 January 2018 AND the scale is chosen. They cut the income tax base only, never the social levy base.
- **Retiring SME director.** The fixed allowance applies under the PFU or the scale, shares held at least one year, form 2074-DIR. It cannot be combined with the holding allowances. Each spouse gets their own allowance. Social levies are due on the gain before the allowance. Other conditions of art. 150-0 D ter are not set out here: refer.

**Dividends and interest.** Dividends go in box 2DC (eligible for the allowance under the scale), interest in box 2TR, with no allowance on interest. The bank withholds 12.8% as an advance payment, credited on the return; a household under the reference income limits may ask to be excused by 30 November of the year before payment. Livret A, livret jeune, LEP and LDD(S) interest is exempt from income tax and social levies.

**PEA.** Payment ceilings apply to payments in, not to the plan's value. One classic PEA per adult domiciled in France. A withdrawal before the end of the 5th year closes the plan in principle (listed exceptions in F2385) and the net gain is taxed under the PFU or the scale, plus social levies; early withdrawals for death or to fund creating or taking over a business are exempt from income tax only. After 5 years gains are exempt from income tax; social levies are due at each withdrawal at the investment income rate of the year (18.6% in 2026), with special CSG rules for gains or payments from before 2018. Take the split from the bank's IFU form. Exempt income of unlisted shares in a PEA is capped each year at 10% of their value. Only securities the law lists may be held.

**Life insurance (assurance-vie).** Any total or partial withdrawal (rachat) is taxable on the gain it contains, as reported by the insurer on the IFU. The 8-year test runs from the contract date. The yearly allowance covers all contracts together and applies once on the return. The 7.5% rate after 8 years applies up to EUR 150,000 of premiums not repaid across all contracts; the gain linked to premiums above that is taxed at 12.8%. For premiums before 27 September 2017 the final withholding applies only if elected when paid; otherwise the gain goes to the scale. A withdrawal after dismissal, retirement, invalidity or judicial liquidation of the taxpayer or spouse is exempt from income tax, not from social levies. Spreading withdrawals after 8 years within the yearly allowance lowers income tax, not social levies.

**Free shares (AGA) and RSUs.** Two amounts, both taxed when the shares are sold: the acquisition gain (value at final vesting) and the later gain on securities. The regime is set by the date of the shareholders' meeting that authorised the plan: the table gives plans from 1 January 2018; plans before 28 September 2012 were taxed at a flat 30% (or the scale on option); plans from 28 September 2012 to 7 August 2015 are salary with the employee contribution; plans from 8 August 2015 to 31 December 2017 have their own rules on the impots.gouv.fr page. The EUR 300,000 limit is yearly across plans, with no carry-forward. A sale below the vesting value gives a loss set against the acquisition gain. Only plans under Commercial Code art. L. 225-197-1 ff. qualify; a foreign RSU plan that does not meet them is taxed as salary: refer.

**BSPCE.** Shares subscribed from 1 January 2025: the exercise gain (value at exercise minus grant price) is taxed at 12.8%, or the salary scale on option, with 3 years or more of service at sale; under 3 years, 30% with no option. The sale gain is under the PFU whatever the service, and the retiring director's allowance can apply. Before 1 January 2025: one gain on sale; granted from 2018 with 3 years or more, PFU or scale; under 3 years, 30% with no option and no fixed allowance; granted to 2017, 19% or 30% by length of service. The company must meet CGI art. 163 bis G.

**Stock options.** The exercise gain is taxed when the shares are sold and always declared on the 2042 C. From 28 September 2012: salary scale plus the levies and contribution in the table. 27 April 2000 to 28 September 2012: salary if the lock-up was broken, flat rates if kept, salary on option. 20 September 1995 to 26 April 2000: gain on securities at a flat rate or salary on option. Before 20 September 1995: gain on securities if form and lock-up conditions were met. Options granted before 28 September 2012 bear 18.6% levies. The discount above 5% of the share value at grant is salary in the year of exercise (boxes 1TP or 1UP). The rise after exercise is a separate gain on securities.

**Employee savings and PER.** Employer payments into an employee savings plan (PEE, PERCO, company PER) are exempt from income tax; their income bears social levies. Match caps follow the annual social security ceiling and are not printed here. Order of use: PEE with match, then PERCO or company PER with match, then individual PER. A PER exit depends on the plan type, annuity or lump sum, timing, and whether payments were deducted: get the provider's split and model it with `fr-personal-income-tax`.

**Property gains.** Gain = sale price minus purchase price, the purchase price raised by actual costs or a flat 7.5%, and by actual works or a flat 15% if held over 5 years (F10864). The income tax allowance and the social levy allowance run on different scales (table). Income tax 19% on the gain after the income tax allowance; social levies 17.2% on the gain after the social levy allowance. The surtax applies to the income tax base above EUR 50,000, not to exempt sales or building land. Exemptions: the main home at the time of sale (occupied most of the year), a sale price up to EUR 15,000, and others in F10864 (for example a first sale of another dwelling with the price reinvested in a main home). A non-resident EU or EEA national who was tax resident in France for at least two continuous years gets an exemption on one French dwelling up to EUR 150,000 of net gain, if sold by 31 December of the tenth year after leaving, or at any time if the seller has had free use of it since 1 January of the year before the sale (CGI art. 150 U, II, 2°). The notary computes, files form 2048-IMM-SD and pays the tax out of the sale price; the seller reports the gain the notary declared on the 2042 C.

## Deadlines and filing

| Step | Date or rule | Source |
|---|---|---|
| Return 2042, 2042 C, 2074 for income and disposals of 2025, online | 21 May 2026 (départements 01 to 19 and non-residents), 28 May (20 to 54), 4 June (55 to 976) | `fr-personal-income-tax` |
| Paper return | 19 May 2026 | same |
| Option for the scale (box 2OP) | On the return, within the filing deadline | F2613 |
| Advance payment excuse on dividends and interest | Request to the bank by 30 November of the year before payment | F2613 |
| Property gain | Form 2048-IMM-SD filed by the notary with the deed when it is registered or published, and the tax paid at that filing (CGI art. 150 VG, I, 1°; 150 VF); in other cases, within one month of the sale (150 VG, I, 4°). Gain then reported on the 2042 C | CGI art. 150 VG |
| Balance of income tax and levies | Debited from September 2026 (one debit up to EUR 300, else four) | `fr-personal-income-tax` |

Income and disposals of 2026 are declared in spring 2027 on the same forms.

## Penalties and interest

- **Late filing** of the 2042 or 2074: 10% surcharge; 40% if not filed within 30 days of a formal notice; 80% for a hidden activity (CGI art. 1728).
- **Inaccuracy:** 40% for a deliberate breach; 80% for abuse of law or fraudulent manoeuvres (CGI art. 1729).
- **Late payment interest:** 0.20% per month (CGI art. 1727), on top of any surcharge.
- **Capital-income CSG assessed with income tax:** 10% surcharge on amounts unpaid 45 days after the assessment (CSS L. 136-6 III; CGI art. 1730).
- The details, thresholds and halving for a spontaneous correction are in `fr-personal-income-tax`.

## Cross-border points

- **Non-residents.** A gain on French property by a non-resident individual is taxed at 19% (CGI art. 244 bis A, I and 200 B), paid when the deed is registered or within one month of the sale, under the responsibility of a representative in France accredited by the tax office (244 bis A, IV). The surtax applies to non-residents too (CGI art. 1609 nonies G, I). Gains on substantial holdings in French companies, social levies and treaty relief: use `fr-cross-border`.
- **Resident insured in another EEA state or Switzerland:** social levies on capital income are the 7.5% solidarity levy only (F2329; CSS L. 136-6 I ter).
- **Foreign dividends and interest:** taxable in France; the foreign tax credit depends on the treaty. Refer with the treaty text.
- **Employee shares and mobility:** an employee who moved into or out of France during vesting has the gain split by period of French activity. Refer.
- **Leaving France:** unrealised share gains can be taxed on departure (`leaving-france-exit-tax`).
- **Crypto-assets:** separate regime and separate option (`fr-crypto-tax`).

## Worked examples

**Example 1. Shares sold in 2025, flat tax.** A resident single person sold listed shares in 2025 with a net gain of EUR 10,000 and kept the PFU. Income tax 10,000 x 12.8% = 1,280. The disposal is from 2025, so social levies are 18.6%, not 17.2%: 10,000 x 18.6% = 1,860. Total 3,140, declared in May 2026 on the 2042 C box 3VG.

```oa-check
name: FR securities gain 2025 under the PFU
inputs:
  gain: 10000
steps:
  - income_tax: gain * 0.128
  - social_levies: gain * 0.186
  - total: income_tax + social_levies
expected:
  income_tax: 1280.00
  social_levies: 1860.00
  total: 3140.00
```

**Example 2. Second home sold in 2026 after 12 full years, with surtax.** Net taxable gain before allowances EUR 120,000 (price minus purchase price and the flat 7.5% and 15%). Years 6 to 12 count, so 7 years. Income tax allowance 7 x 6% = 42%, base 120,000 x 58% = 69,600, tax at 19% = 13,224. Social levy allowance 7 x 1.65% = 11.55%, base 120,000 x 88.45% = 106,140, levies at 17.2% (property gains stay at 17.2%) = 18,256.08. The income tax base is above EUR 50,000 and in the 60,001 to 100,000 bracket: surtax 2% x 69,600 = 1,392. Total 32,872.08, paid by the notary.

```oa-check
name: FR property gain 2026, 12 years held, surtax bracket 2%
inputs:
  gain: 120000
  years_over_5: 7
steps:
  - it_base: gain * (1 - years_over_5 * 0.06)
  - income_tax: it_base * 0.19
  - ps_base: gain * (1 - years_over_5 * 0.0165)
  - social_levies: ps_base * 0.172
  - surtax: it_base * 0.02
  - total: income_tax + social_levies + surtax
expected:
  it_base: 69600.00
  income_tax: 13224.00
  ps_base: 106140.00
  social_levies: 18256.08
  surtax: 1392.00
  total: 32872.08
```

## Ask the client first

- For each sale, dividend or interest payment: what was it, and in which year was it received or sold? (Type and year set the levy rate: 17.2% or 18.6%.)
- Do you want the progressive scale, and what is the household's full income and marginal rate? (The option covers all investment income and gains of the year.)
- For shares: bought before or after 1 January 2018, any losses from the last ten years, and are you a retiring SME director?
- For employee shares: date of the shareholders' meeting, French-qualifying plan or not, subscription date, years of service at sale, and did you move country during vesting?
- For a PEA or life insurance: opening date, premium dates (before or after 27 September 2017), total premiums across contracts.
- For property: main home at the time of sale, years held, actual costs and works, and the notary's 2048-IMM-SD.

Defaults while waiting: PFU, not the scale; PEA under 5 years; no life insurance allowance; no main-home exemption until occupation is shown; BSPCE under 3 years of service; free shares under the salary rules until the plan is checked.

Refer: non-residents; foreign tax credits; non-qualifying or cross-border employee share plans; BSPCE where the company's eligibility is in doubt; management packages (salary above a limit since 15 February 2025, line 1MP); the retiring director's conditions; PEE match caps and PER exit computations; deferred gains (report d'imposition), carried interest, futures, professional traders; property sold by a company or dealer, and building land.

Key law: CGI art. 200 A (PFU), 158 (dividend allowance), 150-0 A to 150-0 D ter (securities), 80 quaterdecies (free shares), 163 bis G (BSPCE), 80 bis (stock options), 163 quinquies D and CMF L. 221-30 (PEA), 125-0 A (life insurance), 150 U to 150 VH and 200 B (property), 1609 nonies G (surtax); CSS L. 136-6 to L. 136-8; LFSS 2026 art. 12; Code du travail L. 3332-1 ff. (PEE).

## Sources

| Source | URL | Read on |
|---|---|---|
| service-public.gouv.fr F2329, social levies on capital income (Vérifié le 30 juin 2026) | https://www.service-public.gouv.fr/particuliers/vosdroits/F2329 | 2026-10-26 |
| service-public.gouv.fr F2613, investment income and PFU (Vérifié le 15 avril 2026) | https://www.service-public.gouv.fr/particuliers/vosdroits/F2613 | 2026-10-26 |
| service-public.gouv.fr F10864, property gains (Vérifié le 15 avril 2026) | https://www.service-public.gouv.fr/particuliers/vosdroits/F10864 | 2026-10-26 |
| BOFiP BOI-RFPI-TPVIE-20, surtax on property gains (CGI art. 1609 nonies G) | https://bofip.impots.gouv.fr/bofip/8597-PGP.html | 2026-10-26 |
| impots.gouv.fr, holding allowances on gains on securities | https://www.impots.gouv.fr/particulier/questions/jai-realise-des-plus-values-ai-je-droit-un-abattement-pour-duree-de-detention | 2026-10-26 |
| impots.gouv.fr, Brochure pratique 2026, plus-values (2074, losses ten years) | https://www.impots.gouv.fr/www2/fichiers/documentation/brochure/ir_2026/pdf_som/09-plus_values_137a156.pdf | 2026-10-26 |
| impots.gouv.fr, Brochure pratique 2026, nouveautés (CSG timing) | https://www.impots.gouv.fr/www2/fichiers/documentation/brochure/ir_2026/pdf_som/nouveautes.pdf | 2026-10-19 |
| impots.gouv.fr, Brochure pratique 2026, revenus des capitaux mobiliers | https://www.impots.gouv.fr/www2/fichiers/documentation/brochure/ir_2026/pdf_som/08-RCM_121a136.pdf | 2026-10-19 |
| impots.gouv.fr, Brochure pratique 2026, traitements et salaires | https://www.impots.gouv.fr/www2/fichiers/documentation/brochure/ir_2026/pdf_som/06-traitements_salaires_85a114.pdf | 2026-10-19 |
| impots.gouv.fr, retiring SME director | https://www.impots.gouv.fr/particulier/questions/dirigeant-de-pme-partant-la-retraite-comment-sera-imposee-la-plus-value-que-je | 2026-10-19 |
| impots.gouv.fr, free shares | https://www.impots.gouv.fr/particulier/questions/mon-entreprise-ma-attribue-des-actions-gratuites-comment-sera-impose-le-gain | 2026-10-19 |
| impots.gouv.fr, BSPCE | https://www.impots.gouv.fr/particulier/questions/jai-vendu-des-bons-de-souscription-de-parts-de-createurs-dentreprise-ou-bspce | 2026-10-19 |
| impots.gouv.fr, stock options | https://www.impots.gouv.fr/particulier/questions/jai-des-stock-options-comment-est-impose-le-gain-levee-doptions | 2026-10-19 |
| service-public.gouv.fr F2385, PEA | https://www.service-public.gouv.fr/particuliers/vosdroits/F2385 | 2026-10-19 |
| service-public.gouv.fr F22414, life insurance | https://www.service-public.gouv.fr/particuliers/vosdroits/F22414 | 2026-10-19 |
| Légifrance, CGI art. 1728 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000028312309/2026-10-24 | 2026-10-24 |
| Légifrance, CGI art. 1727 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000029355562/2026-10-24 | 2026-10-24 |
| Légifrance, CGI art. 1729 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000020051904/2026-10-24 | 2026-10-24 |
| Légifrance, loi n° 2025-1403 (LFSS 2026), art. 12 (CSG 10.6%, IV list at 9.2%, start dates) | https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000053226384 | 2026-10-26 |
| Légifrance, CGI art. 200 A (PFU 12.8%, global option) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053546896 | 2026-10-26 |
| Légifrance, CGI art. 200 B (19%) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000030061684 | 2026-10-26 |
| Légifrance, CGI art. 150 U (exemptions) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053544910 | 2026-10-26 |
| Légifrance, CGI art. 150 VC (duration allowance, income tax) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000047970756 | 2026-10-26 |
| Légifrance, CGI art. 150 VG (2048-IMM filing) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000027978330 | 2026-10-26 |
| Légifrance, CGI art. 1609 nonies G (surtax brackets) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000048806252 | 2026-10-26 |
| Légifrance, CGI art. 244 bis A (non-residents) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000048806274 | 2026-10-26 |

Not yet confirmed: the CGI text of art. 150-0 D (holding allowances, ten-year loss carry-forward) and the social levy duration allowance scale read on Légifrance (figures from impots.gouv.fr and F10864); the EUR 15,000 sale price exemption in the code text; the social levies on non-residents' property gains; employee savings match caps; PER exit computation; the free-share regime for plans of 8 August 2015 to 31 December 2017; the conditions of the retiring director's allowance.

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
