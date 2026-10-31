---
name: leaving-france-exit-tax
description: "Leaving France, tax year 2026: the exit tax on unrealised share gains when a French resident moves abroad (CGI art. 167 bis): who is in scope (6 of the last 10 years, shares above EUR 800,000 or a 50% stake), the 12.8% income tax and 18.6% social levies, automatic deferral against deferral on request with guarantees, the 2-year and 5-year cancellation, what ends the deferral, reporting after departure, the IFI on French property kept after leaving (EUR 1.3m threshold), succession reach through heirs (art. 750 ter) and the France-Switzerland lump-sum clause. Trigger on: exit tax France, article 167 bis, sursis de paiement, départ à l'étranger plus-values latentes, quitter la France impôt, IFI non-résident, forfait fiscal Suisse. Out of scope: non-residents' French income, withholding and the 7.5% levy rate (fr-cross-border), securities gains of residents (fr-capital-gains), rental income rules (fr-rental-income)."
jurisdiction: FR
category: international
tax_year: 2026
last_updated: 2026-10-31
version: 0.3
verified_by: pending
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Leaving France: the exit tax, the IFI and succession reach (2026) v0.3

> **General reference only.** This skill is general tax reference material for AI-assisted work. It has not been reviewed for any person's facts. Do not file, pay or take a tax position on it without review by a qualified professional in France.

**Tax year.** This skill covers departures in 2026. The exit tax on a 2026 departure is declared on the 2026 income tax return, filed in 2027. The Code général des impôts (CGI) and Code de la sécurité sociale (CSS) articles were read on Légifrance on 23 October 2026, in the version in force that day. Art. 167 bis is in the version in force since 1 January 2024 (loi n° 2023-1322, art. 11); the 2026 finance law did not change it.

**Sibling skills.** Non-residents' French income after the move (rents, the 20%/30% minimum rate, withholding, property gains, the 7.5% levy rate for people covered by another EU scheme) is in `fr-cross-border`. Resident securities gains and the flat tax are in `fr-capital-gains`. Rental income rules are in `fr-rental-income`. The resident income tax computation is in `fr-personal-income-tax`. Audit and appeals are in `fr-tax-audit`. This skill does not repeat them.

## Who this applies to

**Leaving France.** Apply the art. 4 B domestic residence tests (home or main stay, main professional activity, centre of economic interests), subject to its express treaty override: even a person meeting a domestic test is not French tax-domiciled if the applicable double-tax treaty does not regard them as resident in France (see `fr-cross-border`). For the exit tax, the departure date is the day before the day from which the person stops being taxable in France on worldwide income (art. 167 bis, III).

**The exit tax (art. 167 bis, I).** A person is in scope if both are true:

- They were French tax-domiciled for at least 6 of the 10 years before the departure.
- On the departure date, the members of their tax household hold, directly or indirectly, shares, securities or rights (art. 150-0 A, I, 1) that either represent at least 50% of a company's profits, or are worth more than EUR 800,000 in total.

Earn-out claims (clause de complément de prix) held on departure have the same 6-of-10-years residence condition, but not the share-value or stake threshold (art. 167 bis, I, 1, second paragraph). Separately, the earlier deferred gains listed in art. 167 bis, II, including apport-cession gains under art. 150-0 B ter, become taxable on departure without that six-year condition or the EUR 800,000 / 50% thresholds. A person resident for only three years can therefore be in scope for a covered earlier deferred gain even when the ordinary unrealised-share-gain tests fail.

**What stays French after leaving.**

- **IFI (art. 964).** A non-resident is liable to the real-estate wealth tax on French real property and on the part of company shares that represents French real property, when those assets are worth more than EUR 1,300,000. Liability is assessed on 1 January each year. Apply the threshold to the correct IFI assessment unit: married couples are jointly assessed except for CGI art. 6,4(a)/(b) cases; PACS partners and notorious cohabitants are also jointly assessed (art. 964). Aggregate their actually taxable net assets before testing the threshold; do not award each person a separate EUR1,300,000 threshold merely because each holding is smaller.
- **Gift and inheritance duties (art. 750 ter).** After the move, France taxes gifts and estates on French assets (art. 750 ter, 2°). It also taxes worldwide assets received by an heir or donee who is French-domiciled when they receive them and was French-domiciled for at least 6 of the 10 years before (art. 750 ter, 3°). Leaving does not move the heirs.
- **French-source income.** Rents, French property gains and other French income stay taxable: see `fr-cross-border`.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source URL |
|---|---|---|---|
| Exit tax: residence condition | 6 of the 10 years before departure | 2026 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000048806379 |
| Exit tax: value threshold for shares held by the household | more than EUR 800,000 | 2026 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000048806379 |
| Exit tax: stake threshold | at least 50% of a company's profits | 2026 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000048806379 |
| Exit tax: income tax on the gain (art. 167 bis, II bis, 1, by reference to art. 200 A, 1) | 12.8% (or the scale on option, computed as a differential) | 2026 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053546896 |
| CSG on patrimony income, including exit-tax gains (CSS art. L136-6, I, e bis; L136-8, I, 2°) | 10.6% | Income of 2025 onward (LFSS 2026 art. 12, II) | https://www.legifrance.gouv.fr/jorf/article_jo/JORFARTI000053226452 |
| CRDS | 0.5% | 2026 | https://www.legifrance.gouv.fr/loda/id/JORFTEXT000000190291 |
| Solidarity levy (CGI art. 235 ter) | 7.5% | 2026 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000037949145 |
| Total social levies on exit-tax gains / total with income tax | 18.6% / 31.4% | Income of 2025 onward | Sum of the rows above |
| Exception: deferred 150-0 B ter gain brought into charge by the exit tax | social levies at the rate in force in the year the gain was realised (17.2% for a gain realised in 2024) | 2026 | https://www.legifrance.gouv.fr/jorf/article_jo/JORFARTI000033734387 |
| Guarantee required for deferral on request (art. 167 bis, V) | 12.8% of the gross gains and claims, before allowances | 2026 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000048806379 |
| Cancellation of the tax (income tax and social levies) if the shares are still held | 2 years after departure | 2026 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000048806379 |
| Same, where the total value on departure exceeds EUR 2,570,000 | 5 years after departure | 2026 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000048806379 |
| IFI threshold (art. 964) | net taxable assets above EUR 1,300,000 | IFI 2026 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000036384999 |
| IFI scale (art. 977, 1) | 0% to EUR 800,000; 0.50% to EUR 1,300,000; 0.70% to EUR 2,570,000; 1% to EUR 5,000,000; 1.25% to EUR 10,000,000; 1.50% above | IFI 2026 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000036385041 |
| IFI reduction for net assets from EUR 1,300,000 to under EUR 1,400,000 (art. 977, 2) | EUR 17,500 minus 1.25% of net assets | IFI 2026 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000036385041 |
| Heir's residence condition for worldwide reach (art. 750 ter, 3°) | French-domiciled on receipt and 6 of the last 10 years | 2026 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000024453202 |
| Late filing surcharge (art. 1728) | 10%; 40% after formal notice; 80% for hidden activity | 2026 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053546784 |
| Inaccuracy surcharge (art. 1729) | 40% deliberate; 80% fraud; abuse of law 80%, reduced to 40% unless principal initiative or principal benefit is established | 2026 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000020051904 |
| Late payment interest (art. 1727) | 0.20% a month | 2026 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000051213330 |

## The taxable base

**1. The deemed gain (art. 167 bis, I, 2).** For each holding: value on the departure date minus acquisition price (or the value used for gift or inheritance duties if received free). Value follows art. 758 and art. 973, I, last paragraph. Shares received in a tax-deferred exchange (art. 150-0 B) start from the cost of the shares given up, adjusted for any cash adjustment (soulte). Unrealised losses cannot be set against these gains or any other gains (I, 5). Earn-out claims are taxed at their real value on departure.

**2. Allowances.** The holding-period allowances of art. 150-0 D, 1 ter and 1 quater require qualifying shares acquired or subscribed before1January2018 and the global progressive-scale election; those allowances do not apply to the12.8%PFU route under art. 200 A,1-A-2°. Qualifying holding-period allowances reduce the income-tax base under that scale route. The separate fixed allowance for retiring managers (art. 150-0 D ter, if the person retired before leaving and sells within two years of retiring) reduces the income tax base (I, 2 bis and 3). They do not reduce the social levies base (CSS art. L136-6, I).

**3. The tax.** Income tax at 12.8% (art. 200 A, 1). On option, the progressive scale applies, computed as the difference between the tax on the year's income with and without the exit-tax gains (II bis, 1). Social levies of 18.6% for gains taxed with 2025 income onward: CSG 10.6% (CSS art. L136-8, I, 2°, as amended by LFSS 2026, loi n° 2025-1403, art. 12), CRDS 0.5% and solidarity levy 7.5%. A 2026 departure is taxed with 2026 income, so 18.6% applies. One exception: a deferred apport-cession gain (art. 150-0 B ter) brought into charge by the exit tax bears social levies at the rate of the year the gain was realised (LFR 2016, loi n° 2016-1918, art. 34, II), so a gain realised in 2024 stays at 17.2%. Its income tax rate is fixed by art. 200 A, 2 ter according to the date of the contribution (art. 167 bis, II bis, 1 bis): 12.8% for a contribution made from 1 January 2018 (an average rate if the scale option was taken that year), and a computed average rate for contributions made from 2013 to 2017. The V guarantee for it uses that rate.

**4. Payment deferred or not.**

- **Automatic deferral (art. 167 bis, IV).** Payment is deferred, with no request, when the person moves to an EU member state, or to a state that has signed with France both an administrative-assistance convention against tax fraud and evasion and a recovery-assistance convention of similar scope to Directive 2010/24/EU, and is not a non-cooperative state (art. 238-0 A). The EEA states (Norway, Iceland, Liechtenstein) are not named: they qualify only if they meet the two-convention test.
- **Deferral on request (art. 167 bis, V).** Any other destination, or a later move from a IV state to another state, gets deferral only on express request. Before leaving, the person must declare the gains, appoint a representative established in France, and lodge guarantees with the public accountant equal to 12.8% of the gross gains and claims (no allowances). Within one month of receiving the tax notice, they top up the guarantee if the income tax computed under II bis is higher; if it is lower, they can ask for the excess guarantee to be released. This route is not limited to non-cooperative states. Its request must be lodged at least 90 days before transfer, as set out under Deadlines.
- Without deferral, the tax is paid with the departure-year income tax.

**5. Switzerland and the UAE against the test.**

- **Switzerland** is not in the EU. The France-Switzerland treaty of 9 September 1966 has an exchange-of-information article (art. 28), and the 2023 amending protocol (décret n° 2025-838) adds no recovery-assistance article. Switzerland is a party to the multilateral Convention on Mutual Administrative Assistance in Tax Matters, but on ratifying it (26 September 2016) it reserved under art. 30, 1, b that it gives no assistance in recovery (arts. 11 to 16) for any tax. So no convention gives France recovery assistance from Switzerland, the IV test is not met, and deferral needs the art. 167 bis, V route: request, representative and guarantees before departure.
- **UAE.** The France-UAE treaty of 19 July 1989 (décret n° 90-631) gained an exchange-of-information article (art. 21 A) in the 1993 amendment (décret n° 95-798), but has no recovery-assistance article. The UAE is a party to the multilateral convention and reserved under art. 30, 1, b that it gives no assistance in the recovery of any tax claim (reservation made on signature, 21 April 2017, confirmed on ratification, 21 May 2018). So the IV test is not met: deferral needs the art. 167 bis, V route.

**6. What ends the deferral and makes the tax payable (art. 167 bis, VII, 1).** Sale, buy-back, redemption or cancellation of the relevant shares; for latent-I holdings, a gift when the donor is domiciled outside IV unless they prove it is not mainly tax-driven; the separately enumerated events for prior-II deferred gains; receipt of an earn-out payment. For the own I earn-out claims, contribution or paid transfer of the claim also ends deferral before payment; donation does so when the donor is domiciled outside IV unless they establish the statutory non-tax-purpose rebuttal. Article150-0 B ter gains have their own enumerated contributed/substituted-title disposal, redemption, repayment and cancellation events. The post-departure150-0 B/150-0 B ter exchange/contribution exception in VII-1(a) applies only to securities whose latent gains were ascertained under I; it is not universal protection for prior-II gains. Keep the substituted-title tracking in VII-1 bis and apply the actual event list for the particular deferred-gain population.

**7. Cancellation (art. 167 bis, VII, 2).** The tax on the deemed gain is cancelled (or refunded if paid) when the shares are still held 2 years after departure, or 5 years when the total value on departure exceeded EUR 2,570,000. It is also cancelled on return to France if earlier, on death, and on a gift when the donor lives in a IV state (or, elsewhere, proves the gift was not mainly tax-driven). The social levies are cancelled with the income tax in these cases: CSS art. L136-6, I withholds from the levies only the cancellation of VII, 2, last paragraph (a disposal within art. 150-0 A, III while resident in a IV state) and that of VIII, 4 (unless the sale is taxed under art. 244 bis A). Earn-out claim tax is cancelled on return to France, death or a qualifying gift (VII, 4). The window polynomials in the original examples are case-specific arithmetic fixtures. The general statutory selector is two years at or below EUR2,570,000 and five years strictly above it; do not interpolate a fractional cancellation period from those fixture formulas.

**8. Sale for less than the departure value (art. 167 bis, VIII).** If the actual gain on a sale or gift is lower than the deemed gain, the tax is capped at the tax on the actual gain; a loss cancels it. Eligible tax actually paid in the new residence state on the disposal is credited only within the definitive French tax on the relevant gain (VIII, 5). First apportion the foreign tax by the French social-levy gain divided by the foreign taxable gain, and apply it against CSG/CRDS and then the solidarity levy, each within the French tax due. Then apportion the remaining foreign tax by the French income-tax gain, after applicable allowances, divided by that foreign taxable gain, capped at the French income tax due. Keep the foreign assessment and payment evidence. A tax charged only on post-departure appreciation after a foreign step-up, or a gift duty, is not this credit. The proportional method is stated in current VIII, 5 and illustrated by BOI-RPPM-PVBMI-50-10-40, VI-F; its old example rates and eight-year cancellation period are not 2026 parameters. If the sale is taxed in France under art. 244 bis A or 244 bis B, the exit-tax income tax on those shares is cancelled (VIII, 4); the social levies are cancelled too only where the sale falls under art. 244 bis A (CSS art. L136-6, I).

## Deadlines and filing

- **Before departure.** For deferral on request, submit the request form and representative details to the non-resident tax office at least 90 days before the transfer (CGI annexe III, art. 41 tervicies A; current DGFiP guidance). Declare the gains and lodge the guarantees before leaving under art. 167 bis, V; the one-month post-notice top-up rule is separate.
- **Departure-year return.** The gains and claims are declared on the income tax return filed in the year after departure, by the art. 175 deadline (art. 167 bis, IX, 1). For a 2026 departure, that is the 2026 return filed in 2027.
- **Annual follow-up.** A yearly statement of the deferred tax is required where the deferral covers earn-out claims or pre-departure deferred gains (II) (art. 167 bis, IX, 2). Where it covers only unrealised gains under I, 1, the law asks for no yearly statement. The DGFiP page updated 10 March 2026 nevertheless describes a simplified 2074-ETSL follow-up for total deferral without an event, alongside the 2074-ETS versions. That administrative instruction is recorded separately from IX, 2; the applicable 2027 form and annual procedure for a 2026 departure are not yet confirmed.
- **When the deferral ends.** In the year after the event, by the art. 175 deadline, declare the event, its date and the tax due on the administration's form; the tax is paid when the form is filed (IX, 3). Refund and cancellation claims follow the same deadline.
- **Change of address.** Tell the tax office the new address within two months of each move (IX, 5).
- **IFI.** Liability is fixed on 1 January each year (art. 964). The filing route for non-residents is in Not yet confirmed.

## Penalties and interest

- **Missing reports end the deferral.** Not filing the return and form of IX, 1 and 2, or the claim of IX, 3, last paragraph, or leaving out any required information, makes the deferred tax payable at once (art. 167 bis, IX, 4).
- **Late filing (art. 1728).** 10% of the tax; 40% if not filed within 30 days of a formal notice; 80% for a hidden activity.
- **Inaccuracies (art. 1729).** 40% for a deliberate breach; 80% for fraud. Abuse of law is 80%, reduced to 40% where it is not established that the taxpayer had the principal initiative or was the principal beneficiary.
- **Late payment interest (art. 1727).** 0.20% a month.
- **Social levies on exit-tax gains** are assessed and collected under the income tax rules (CSS art. L136-6, III, second paragraph). A 10% surcharge applies to levies unpaid 45 days after assessment (L136-6, III).

## Cross-border points

- **Treaty and EU law.** The Conseil d'État held that art. 167 bis, with its deferral without guarantees on a move within the EU, is compatible with the freedom of establishment, and that taxing unrealised and deferred gains under it is governed by EU law, so EU general principles such as legal certainty apply to it (5 February 2025, n° 476399). A treaty does not stop France computing the exit tax at departure, but a foreign tax on the later sale is credited (art. 167 bis, VIII, 5).
- **Switzerland: the lump-sum clause.** The France-Switzerland treaty (art. 4, 6, b) excludes from residence a person taxed only on a lump sum based on the rental value of their home. The Conseil d'État (25 June 2021, n° 442790) held that people taxed under the Swiss expenditure-based regime fall within the exclusion. It then applied French doctrine of 1972 (14 B-2211, relied on under LPF art. L80 A) under which a lump-sum taxpayer still counts as Swiss resident if the tax base is above five times the rental value and the cantonal base covers at least the Swiss income and the French income for which treaty relief is claimed; the couple met it and were held Swiss residents for 2011. A person who is not a treaty resident of Switzerland can stay a French resident under art. 4 B (for example through French assets) with no tie-breaker. Whether that doctrine is still published in BOFiP was not checked.
- **UAE: wealth tax article.** France-UAE treaty art. 16 A (1993 amendment): French real property of a UAE resident is taxable in France only if its value exceeds that resident's listed French shares and claims on French public bodies or listed companies, held for more than eight months in total in the previous calendar year (art. 16 A, 6, a); property-rich companies (over 50% French real property) count as property. Whether art. 16 A, written for the former wealth tax, applies to the IFI was not confirmed.
- **Social levies on French income after leaving.** Rents and French property gains bear 17.2% (rents) or 18.6% (furnished letting); only 7.5% for a person covered under Regulation (EC) 883/2004 (EU, EEA, Switzerland) and not by a French scheme. For qualifying UK compulsory coverage, the current DGFiP non-resident property-gains page expressly continues the CSG/CRDS exemption after Brexit and leaves the 7.5% solidarity levy. This is the published administrative route, not a claim that the literal Regulation 883/2004 wording of CSS L136-6 I ter itself names the UK. Establish the applicable compulsory scheme and absence of French compulsory coverage; residence in the UK alone is not the test. UAE coverage alone does not establish this relief. Other foreign-income and levy computations remain in `fr-cross-border`.
- **Former main home.** Under art. 244 bis A I-1, the home must have been the seller’s main home in France at departure, the destination must be an EU state or meet both assistance-convention tests and not be a non-cooperative state, sale must occur by 31 December of the following year, and the home must not have been made available to any third party, free or paid, in between. A seller who already used art. 150 U II-2’s separate non-resident housing exemption cannot use this exemption. Immediate necessary dependencies must be sold with the home; see `fr-cross-border`.

## Worked examples

### Example 1: a founder moving to Portugal (EU), automatic deferral, 5-year window

A founder has been French-domiciled for 15 years and moves to Lisbon on 1 July 2026, so the transfer is deemed to occur on 30 June 2026. The household holds shares in her company worth EUR 3,000,000 on that date, bought for EUR 200,000. No allowance applies. Portugal is an EU state, so payment is deferred automatically.

- Deemed gain: 3,000,000 minus 200,000 = EUR 2,800,000.
- Income tax at 12.8%: EUR 358,400. Social levies at 18.6% (2026 income): EUR 520,800. Total computed and deferred: EUR 879,200.
- Value above EUR 2,570,000, so the cancellation window is 5 years: if she still holds the shares on 30 June 2031, the EUR 879,200 (income tax and social levies) is cancelled.
- She declares the gain on the 2026 return in 2027. No yearly statement is needed for unrealised gains alone (IX, 2).

```oa-check
name: Founder to Portugal, shares EUR 3,000,000, cost EUR 200,000, 2026 departure
inputs:
  value_on_departure: 3000000
  acquisition_cost: 200000
  five_year_line: 2570000
  departure_year: 2026
steps:
  - gain: value_on_departure - acquisition_cost
  - income_tax: gain * 0.128
  - social_levies: gain * 0.186
  - total_deferred: income_tax + social_levies
  - window_years: 2 + 3 * min(max(value_on_departure - five_year_line, 0), 1)
  - cancellation_year: departure_year + window_years
expected:
  gain: 2800000.00
  income_tax: 358400.00
  social_levies: 520800.00
  total_deferred: 879200.00
  window_years: 5
  cancellation_year: 2031
```

### Example 2: a move to the UAE, deferral on request, sale in year one

A shareholder French-domiciled for 10 years moves to Dubai in 2026. The shares are worth EUR 1,000,000 on the departure date, cost EUR 100,000. The UAE is not in the EU, the France-UAE treaty has no recovery-assistance article and the UAE reserved recovery assistance under the multilateral convention, so deferral needs a request. He requests deferral at least 90 days before transfer; before leaving he declares the gain, appoints a representative in France and lodges a guarantee of 12.8% of the gross gain. In 2027, within the 2-year window, he sells for EUR 1,200,000.

- Deemed gain: EUR 900,000. Guarantee before departure: 12.8% x 900,000 = EUR 115,200.
- Tax computed: income tax EUR 115,200, social levies 18.6% = EUR 167,400, total EUR 282,600.
- Window: the value is not above EUR 2,570,000, so 2 years. The 2027 sale falls inside it and ends the deferral.
- The actual gain (1,200,000 minus 100,000 = 1,100,000) is not lower than the deemed gain, so the VIII cap does not reduce the tax. The full EUR 282,600 becomes payable, declared with the 2027 return in 2028. No UAE tax to credit. The EUR 200,000 rise after departure is outside the exit tax; whether France taxes it depends on art. 244 bis B and the treaty (`fr-cross-border`).

```oa-check
name: Move to the UAE, deferral on request, shares EUR 1,000,000, sold in year one for EUR 1,200,000
inputs:
  value_on_departure: 1000000
  acquisition_cost: 100000
  sale_price: 1200000
  five_year_line: 2570000
steps:
  - gain: value_on_departure - acquisition_cost
  - guarantee: gain * 0.128
  - income_tax: gain * 0.128
  - social_levies: gain * 0.186
  - total_tax: income_tax + social_levies
  - window_years: 2 + 3 * min(max(value_on_departure - five_year_line, 0), 1)
  - actual_gain: sale_price - acquisition_cost
  - taxed_gain: min(actual_gain, gain)
  - tax_payable: taxed_gain * (0.128 + 0.186)
  - post_departure_rise: sale_price - value_on_departure
expected:
  gain: 900000.00
  guarantee: 115200.00
  income_tax: 115200.00
  social_levies: 167400.00
  total_tax: 282600.00
  window_years: 2
  actual_gain: 1100000.00
  taxed_gain: 900000.00
  tax_payable: 282600.00
  post_departure_rise: 200000.00
```

## Ask the client first

1. Where are you moving, on what date, and will your family and main activity move with you? This fixes the departure date (art. 167 bis, III and art. 4 B) and whether deferral is automatic (IV) or on request (V).
2. Every shareholding of the household (value on the departure date, cost, any stake of 50% or more), any earn-out clause, and any gain deferred under art. 150-0 B ter or earlier rules. This decides scope, the gain and the 2-year or 5-year window.
3. Do you plan to sell, gift or contribute the shares in the next five years, or is a sale already in negotiation? This decides whether the tax will be cancelled or become payable.
4. Do you keep French property, directly or through companies, and what is it worth net on 1 January? This decides the IFI.
5. Where do your children and other heirs live, and how long have they lived in France? This decides art. 750 ter, 3°.
6. Which social security scheme will cover you after the move, and if Switzerland, will you be taxed on a lump sum? This decides the levy rate on French income and treaty residence.

## Sources

| Source | URL | Read on |
|---|---|---|
| CGI art. 167 bis (exit tax), version in force since 1 January 2024; selected deferral-event/allowance scopes reread31October2026, with own200A PFU exclusion and750ter residence continuation | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000048806379 | 2026-10-23; selected scopes2026-10-31 |
| CGI art. 200 A (12.8% flat rate) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053546896 | 2026-10-23 |
| CGI art. 964 (IFI scope and EUR 1,300,000 threshold) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000036384999 | 2026-10-23 |
| CGI art. 977 (IFI scale and reduction) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000036385041 | 2026-10-23 |
| CGI art. 975 (IFI exemptions, as amended by loi n° 2026-103, art. 7) | https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069577/LEGISCTA000036384995/ | 2026-10-23 |
| CGI art. 750 ter (gift and inheritance duties, territorial reach) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000024453202 | 2026-10-23 |
| CGI art. 235 ter (7.5% solidarity levy) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000037949145 | 2026-10-23 |
| CGI art. 1727 (late payment interest) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000051213330 | 2026-10-23 |
| CGI art. 1728 (late filing) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053546784 | 2026-10-23 |
| CGI art. 1729 (inaccuracies) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000020051904 | 2026-10-23 |
| CSS art. L136-8 (CSG rates) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000054336623 | 2026-10-23 |
| CSS art. L136-6 (levies on exit-tax gains, I, e bis; I ter; III) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000051218166 | 2026-10-23 |
| LFSS 2026 (loi n° 2025-1403), art. 12 (10.6% CSG and start dates) | https://www.legifrance.gouv.fr/jorf/article_jo/JORFARTI000053226452 | 2026-10-23 |
| LFSS 2026 (loi n° 2025-1403), full text | https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000053226384 | 2026-10-23 |
| LFR 2016 (loi n° 2016-1918), art. 34, II (150-0 B ter gains at the realisation-year rate) | https://www.legifrance.gouv.fr/jorf/article_jo/JORFARTI000033734387 | 2026-10-23 |
| Ordonnance n° 96-50, art. 19 (CRDS 0.5%) | https://www.legifrance.gouv.fr/loda/id/JORFTEXT000000190291 | 2026-10-23 |
| France-UAE treaty of 19 July 1989 (décret n° 90-631) | https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000000533051 | 2026-10-23 |
| France-UAE amending protocol of 6 December 1993, art. 16 A (décret n° 95-798) | https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000000537402 | 2026-10-23 |
| France-Switzerland amending protocol of 27 June 2023 (décret n° 2025-838) | https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000052129841 | 2026-10-23 |
| Council of Europe Treaty Office, Convention on Mutual Administrative Assistance in Tax Matters (ETS 127), reservations and declarations (Switzerland: art. 30, 1, b, 26 September 2016; UAE: art. 30, 1, b, 21 April 2017 and 21 May 2018) | https://www.coe.int/en/web/conventions/full-list?module=declarations-by-treaty&numSte=127&codeNature=0 | 2026-10-23 |
| Conseil d'État, 25 June 2021, n° 442790 (Swiss lump-sum taxpayers, treaty art. 4, 6, b) | https://www.legifrance.gouv.fr/juri/id/CETATEXT000043704443 | 2026-10-23 |
| Conseil d'État, 5 February 2025, n° 476399 (exit tax within the EU governed by EU law; point 2: levies on the latent gain cancelled by the administration after the holding period) | https://www.legifrance.gouv.fr/ceta/id/CETATEXT000051141457 | 2026-10-23 |
| Selected current DGFiP exit-tax request/form guidance, including the 90-day deadline and broader follow-up wording | https://www.impots.gouv.fr/particulier/questions/je-quitte-la-france-suis-je-concerne-par-lexit-tax | 2026-10-29 |
| Selected BOFiP credit method, VI-F §§470–530; old rates and retention periods not imported | https://bofip.impots.gouv.fr/bofip/8020-PGP.html | 2026-10-29 |
| DGFiP non-resident property gains: published UK CSG/CRDS continuation | https://www.impots.gouv.fr/international-particulier/questions/je-vends-un-bien-immobilier-comment-et-quel-taux-suis-je-impose | 2026-10-29 |

Historical source limit: BOFiP returned an error page and impots.gouv.fr was not read on 23 October 2026. On 29 October the selected current legal clauses, DGFiP exit-tax/UK property-gain guidance and BOFiP credit method were read and are separately bound in the figure ledger. Not yet confirmed: (1) Which EEA states (Norway, Iceland, Liechtenstein) meet the art. 167 bis, IV test. (2) The applicable 2027 versions, filing dates and reconciliation of the current DGFiP simplified annual-follow-up instruction with the latent-gain-only statutory position; the current page identifies 2074-ETD, 2074-ETS and 2074-ETSL. (3) Whether the 1972 doctrine on Swiss lump-sum taxpayers is still in BOFiP. (4) Whether France-UAE treaty art. 16 A, written for the former wealth tax, applies to the IFI. (5) How non-residents file the IFI. (6) The treaty/coordination implementation bridge behind the published DGFiP UK relief is not derived here; the expressly published property-gain route above is supplied with its coverage gates, rather than treated as unavailable. (7) Whether the high-income contributions (CEHR, art. 223 sexies, and the differential contribution on high incomes) apply to exit-tax gains; this skill does not compute them.
