---
name: nl-cross-border
description: "Hub skill for crossing the Dutch border in tax year 2026. Covers tax residence for individuals (facts and circumstances, AWR art. 4) and companies (seat by circumstances plus the incorporation fiction in Wet Vpb art. 2(5)); arriving under the expat scheme (30% ruling) with the 2026 salary norm and the fall to 27% from 2027; non-residents taxed on Dutch box 1, box 2 and box 3 income and qualifying non-resident status; leaving, with the protective assessment (conserverende aanslag) on box 2 shares and pensions; the M return for the migration year; 15% dividend tax and the conditional withholding tax at 25.8% on payments to low-tax jurisdictions; treaty relief. Trigger on: moving to the Netherlands, leaving the Netherlands, emigrating, non-resident, expat, exit tax, conserverende aanslag, M-formulier, digital nomad, bronbelasting. Out of scope: 30% ruling detail (netherlands-30-percent-ruling), payroll (nl-payroll-tax), corporate tax (nl-corporate-tax), resident income tax (nl-income-tax)."
version: 0.2
jurisdiction: NL
tax_year: 2026
last_updated: 2026-10-23
authored_by: Ryan Duguid
review_status: pending_review
trust_label: Accountant-authored
category: cross-border
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Netherlands: cross-border tax for people and companies (2026) v0.2

> **Source-cited draft.** No accountant has reviewed this skill yet. Every figure below comes from wetten.overheid.nl or belastingdienst.nl, read on 22 October 2026. It prepares working papers; it is not authority to file or pay.

This is the hub for the Dutch cross-border (XB) domain. It summarises and links rather than repeating other skills:

- The expat scheme (30% ruling) in full: [netherlands-30-percent-ruling](netherlands-30-percent-ruling.md) and [nl-30-percent-ruling](nl-30-percent-ruling.md).
- Resident income tax, boxes and credits: [nl-income-tax](nl-income-tax.md), [nl-deductions](nl-deductions.md).
- Corporate tax, participation exemption and fiscal unity: [nl-corporate-tax](nl-corporate-tax.md).
- Payroll withholding for incoming and outgoing employees: [nl-payroll-tax](nl-payroll-tax.md).
- Transfer pricing: [netherlands-transfer-pricing](netherlands-transfer-pricing.md). Objections: [nl-tax-objection](nl-tax-objection.md).

Tax year: the calendar year. 2026 figures apply to 1 January to 31 December 2026.

## Who this applies to

**Individuals.** The Netherlands has no day-count test. Article 4(1) of the Algemene wet inzake rijksbelastingen (AWR) says where someone lives is judged on the circumstances ("naar de omstandigheden beoordeeld"). In practice that means the durable personal ties: where the home is, where the partner and children live, where the person works, where they are registered, and where their social and economic life sits. A short stay can make someone resident if the ties are there; a long stay without them may not.

- A **resident** (binnenlands belastingplichtige) is taxed on worldwide income in box 1 (work and home), box 2 (substantial interest, 5% or more of a company) and box 3 (savings and investments).
- A **non-resident** (buitenlands belastingplichtige) is taxed only on Dutch income in each box (Wet IB 2001 art. 7.1).
- A **qualifying non-resident** (kwalificerende buitenlandse belastingplichtige) lives in another EU country, Liechtenstein, Norway, Iceland, Switzerland or on Bonaire, Sint Eustatius or Saba, and pays Dutch wage or income tax on all or nearly all (at least 90%) of world income. They get the deductions a resident would. An income statement from the home tax authority is needed only if the inspector asks for it (Wet IB 2001 art. 7.8(6), text valid in 2026).

**Part-year (split year).** There is no separate split-year election. A person who arrives or leaves during the year is resident for part of the year and non-resident for the rest, and files one M return covering both parts (see Deadlines).

**Companies.** A body's seat is also judged on the circumstances (AWR art. 4(1)), which looks mainly at where it is effectively managed. On top of that, a company incorporated under Dutch law is always treated as established in the Netherlands for corporate tax (Wet Vpb 1969 art. 2(5)), except for the participation exemption and fiscal unity articles that the same paragraph lists (arts. 13 to 13d, 13i to 13k, 14a, 14b, 15 and 15a). A Dutch BV managed abroad therefore stays a Dutch taxpayer under domestic law; a treaty tie-breaker may still allocate residence to the other state.

## Rates, bands and thresholds

| Item | 2026 figure | Source |
|---|---|---|
| Box 1, band 1 (to €38,883), resident under AOW age | 35.75%: 8.10% income tax plus 27.65% national insurance | [Belastingdienst box 1](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/prive/inkomstenbelasting/heffingskortingen_boxen_tarieven/boxen_en_tarieven/box_1/box_1); [Wet IB 2001 art. 2.10](https://wetten.overheid.nl/BWBR0011353/) |
| Box 1, band 1, non-resident not in Dutch national insurance | 8.10% (tax part only) | [Wet IB 2001 art. 2.10](https://wetten.overheid.nl/BWBR0011353/) |
| Box 1, band 2 (€38,883 to €78,426) | 37.56% | same |
| Box 1, band 3 (above €78,426) | 49.50% | same |
| Box 2, substantial interest, to €68,843 | 24.5% | [Wet IB 2001 art. 2.12](https://wetten.overheid.nl/BWBR0011353/) |
| Box 2, above €68,843 | €16,866 plus 31% of the excess | same |
| Box 3, savings and investments | 36% | [Wet IB 2001 art. 2.13](https://wetten.overheid.nl/BWBR0011353/) |
| Box 3 tax-free allowance (heffingvrij vermogen) | €59,357 | [Wet IB 2001 art. 5.5](https://wetten.overheid.nl/BWBR0011353/) |
| Expat scheme, maximum tax-free allowance | 30% of wage including the allowance in 2025 and 2026; 27% from 1 January 2027 (30% kept for rulings applied by the last 2023 pay period) | [Handboek Loonheffingen 2026 §19.4](https://download.belastingdienst.nl/belastingdienst/docs/handboek-loonheffingen-lh0221t61fd.pdf) |
| Expat scheme, salary norm (wage excluding allowance must be more than) | €48,013; €36,497 if under 30 with a qualifying master's | [Belastingdienst expat scheme](https://www.belastingdienst.nl/wps/wcm/connect/en/individuals/content/coming-to-work-in-the-netherlands-30-percent-facility); Handboek 2026 |
| Expat scheme, salary norm announced for 2027 | €51,899 (before indexation, not final) | Handboek 2026 |
| Expat scheme, cap | €78,600 a year (30% of a €262,000 base) | [Belastingdienst expat scheme](https://www.belastingdienst.nl/wps/wcm/connect/en/individuals/content/coming-to-work-in-the-netherlands-30-percent-facility) |
| Corporate tax (Vpb) | 19% to €200,000; 25.8% above | [Wet Vpb 1969 art. 22](https://wetten.overheid.nl/BWBR0002672/) |
| Dividend tax (dividendbelasting) | 15% of the distribution | [Wet DB 1965 art. 5](https://wetten.overheid.nl/BWBR0002515/) |
| Conditional withholding tax on interest, royalties and dividends to affiliates in low-tax jurisdictions | Top Vpb rate: 25.8% in 2024, 2025 and 2026 | [Wet bronbelasting 2021 art. 4.1](https://wetten.overheid.nl/BWBR0042952/); [Belastingdienst bronbelasting](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/bronbelasting-rente-en-royalty/bronbelasting-op-renten-en-royalty) |
| Low-tax jurisdiction test | A state designated by ministerial regulation that, on 1 October of the preceding year, has no profit tax or a rate below 9%, or is on the EU list of non-cooperative jurisdictions | [Wet bronbelasting 2021 art. 1.2(1)(e)](https://wetten.overheid.nl/BWBR0042952/); Belastingdienst bronbelasting |
| Ordinary withholding on interest, royalties and service fees | None outside the conditional withholding tax | [Belastingdienst bronbelasting](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/bronbelasting-rente-en-royalty/bronbelasting-op-renten-en-royalty) |
| Exit charge on emigration | No separate rate: the deemed box 2 gain is taxed at box 2 rates; pensions and annuities at the box 1 top rate, in a protective assessment | [Belastingdienst conserverende aanslag](https://www.belastingdienst.nl/wps/wcm/connect/nl/buitenland/content/conserverende-aanslag-bij-emigratie) |

The 2026 box 1 bands apply to people under AOW (state pension) age. People at AOW age pay a lower first-band rate; see [nl-income-tax](nl-income-tax.md).

## The taxable base

**Residents: worldwide.** There is no remittance basis. Foreign income goes into the boxes and double taxation is relieved afterwards (see Cross-border points).

**Non-residents: Dutch income only** (Wet IB 2001 arts. 7.1 to 7.7):

- **Box 1:** profit from a business run through a Dutch permanent establishment or permanent representative, wages for work done in the Netherlands, result from other work done in the Netherlands, and certain periodic payments such as Dutch pensions whose premiums were deducted (art. 7.2).
- **Box 2:** income from a substantial interest in a company established in the Netherlands (art. 7.1(b)).
- **Box 3:** a deemed return on Dutch assets only: Dutch real estate, rights relating to it, and profit shares in a business managed in the Netherlands, less related debts (art. 7.7). A non-resident's foreign bank accounts and shares are outside it. Every non-resident gets the box 3 tax-free allowance for these assets (Belastingdienst, Fiscale informatie 2026, "U woont buiten Nederland").

**Arriving: the expat scheme.** An employee recruited or seconded from abroad, who lived more than 150 km from the Dutch border for more than 16 of the 24 months before the first working day in the Netherlands (Handboek 2026 §19.4), and who meets the salary norm, can receive up to 30% of wage including the allowance tax-free for at most 60 months. The detail, including the cap, part years and the annual salary test, is in [netherlands-30-percent-ruling](netherlands-30-percent-ruling.md). The headline history, from the Handboek Loonheffingen 2026 §19.4:

- 2024: the law cut the maximum to 30% for the first 20 months, 20% for the next 20 and 10% for the last 20.
- 2025: that 30/20/10 path was largely reversed. The maximum is 30% in 2025 and 2026 for every incoming employee.
- From 1 January 2027: the maximum falls to 27% for the whole remaining term, except for employees whose ruling was applied by the last pay period of 2023 (they keep 30%). Rulings started from 2025 also face the new, higher salary norm in 2027.
- Partial non-resident status (treating box 2 and box 3 as if non-resident) is closed from the 2025 return, except under a transitional rule for employees whose ruling was applied over the last pay period of 2023 and who have not become a new incoming employee after a break; it ends with the 2026 return (Handboek Loonheffingen 2026 §19.4; Belastingdienst expat scheme page).

**Leaving: deemed disposal of a substantial interest.** Ceasing to be resident, otherwise than by death, is a deemed disposal of shares that form a substantial interest (Wet IB 2001 art. 4.16(1)(h)). This includes becoming treaty-resident elsewhere. The gain is market value at emigration less the acquisition price. If the person later sells, the acquisition price for Dutch non-resident tax is that market value (art. 7.6).

**Leaving: pensions and annuities.** Pension and annuity rights built up with tax relief, and some own-home capital insurance or savings, are charged in the same protective assessment.

## Deadlines and filing

- **Year of arrival or departure: the M return.** Someone who lived in the Netherlands for only part of the year because of immigration or emigration files the M return (migration) for that year, online in Mijn Belastingdienst under "Aangifte inkomstenbelasting voor belastingplichtigen die een deel van het jaar buiten Nederland wonen", or on a paper M form requested from the Belastingdienst. An entrepreneur filing on paper also completes the M annual accounts booklet ([Belastingdienst M return](https://www.belastingdienst.nl/wps/wcm/connect/nl/buitenland/content/deels-niet-in-nederland-wonen-m-aangifte-doen)).
- **M return deadline.** The date in the invitation letter. The 2025 M return could be filed online from 1 May 2026, and the Belastingdienst notice says it can be filed until 1 July 2026 ([Belastingdienst M return notice](https://sorry.belastingdienst.nl/mbd/storing/nog-geen-aangifte-doen)). A return filed without an invitation is due within five years after the end of the year (Uitvoeringsregeling inkomstenbelasting 2001 art. 45(1)). Detail in [nl-double-tax-relief](nl-double-tax-relief.md).
- **Assessment period.** The Belastingdienst has 3 years to impose the final assessment; for 2025 that is 31 December 2028, extended by any filing extension granted (same page).
- **Protective assessment.** It is issued after the M return for the emigration year has been filed ([Belastingdienst conserverende aanslag](https://www.belastingdienst.nl/wps/wcm/connect/nl/buitenland/content/conserverende-aanslag-bij-emigratie)).
- **Payment deferral.** On emigration to an EU or EEA country, deferral is automatic and no collection interest runs during it. Otherwise apply for it as the assessment explains; the Belastingdienst can ask for security (bank guarantee, mortgage or pledge) when the person moves outside the EU. A move from an EU country on to a non-EU country withdraws an automatic deferral for the box 2 and own-home insurance parts; reapply in writing (same page).
- **How long the protective assessment lives:**
  - Pensions and annuities: deferral for at most 10 years, then remission on request if the rules were kept. Surrendering the pension or annuity in that period makes it payable.
  - Box 2 shares, emigration before 15 September 2015 at 15:15: 10 years' deferral, then remission on request if the company still exists and the person still owns the shares.
  - Box 2 shares, deregistration from the municipality after 15 September 2015 at 15:15: lifetime deferral, no remission after 10 years. A sale, a dividend or the end of the business must be reported and makes the assessment (partly) payable.
- **Non-residents with Dutch income** file a non-resident (C) income tax return for the year by the date in the invitation letter ([Belastingdienst, uitstel aangifte buitenland](https://www.belastingdienst.nl/wps/wcm/connect/nl/buitenland/content/uitstel-aanvragen-belastingaangifte-buitenland-hoe-doe-ik-dat)). Without an invitation, they must file if the tax due exceeds the assessment threshold (€57 for 2025) ([Belastingdienst, aangifte buitenlands belastingplichtige](https://www.belastingdienst.nl/wps/wcm/connect/nl/buitenland/content/buitenlands-belastingplichtig-hoe-doe-ik-aangifte-inkomstenbelasting)). Qualifying non-residents send an income statement from their home tax authority only if the inspector asks (Wet IB 2001 art. 7.8(6)).
- **Dividend tax and conditional withholding tax** are withheld when the payment is made available, then declared and paid on a return. Dividend tax: return and payment within one month after the dividend is made available (AWR art. 19(3)). Conditional withholding tax: one return a year for the calendar year, filed and paid within one month after the year ends (Wet bronbelasting 2021 art. 5.1(3); AWR art. 19(1); Belastingdienst). Detail in [nl-dividend-withholding](nl-dividend-withholding.md). Dividend tax already withheld on the same dividend is credited against the conditional withholding tax (Wet bronbelasting 2021 art. 5.2).

## Penalties and interest

- **Late or missing income tax return (assessment taxes):** an administrative penalty of up to €6,709 (AWR art. 67a). If a year has both a normal and a protective assessment, the penalty is imposed with the normal one; if only a protective assessment, with that.
- **Late or short payment of a tax paid on a return** (dividend tax, conditional withholding tax): up to €6,709 (AWR art. 67c).
- **Intentional or grossly negligent errors:** up to 100% of the tax involved. For assessment taxes: art. 67d (return not filed or incorrect, intent) and art. 67e (assessment too low through intent or gross negligence). For taxes paid on a return: art. 67f (intent or gross negligence).
- **Tax interest (belastingrente):** 5% from 1 January 2026 (6.5% in 2025). Corporate tax now uses the same rate: the higher corporate tax percentage was dropped after the Hoge Raad ruling of 16 January 2026. Benefits (toeslagen) are not covered by this rate ([Belastingdienst belastingrente](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/standaard_functies/prive/contact/rechten_en_plichten_bij_de_belastingdienst/belastingrente/overzicht_percentages_belastingrente)).
- **Collection interest (invorderingsrente)** on late payment of an assessment: 4.3% from 1 January 2026 ([Belastingdienst invorderingsrente](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/standaard_functies/prive/contact/rechten_en_plichten_bij_de_belastingdienst/invorderingsrente)). It does not run during an approved deferral of a protective assessment.
- **Expat scheme failure:** if the wage falls to or below the salary norm, the ruling lapses back to 1 January of that year and the payroll returns must be corrected; see [netherlands-30-percent-ruling](netherlands-30-percent-ruling.md).

## Cross-border points

- **Treaty tie-breaker.** Where both states treat a person as resident, the treaty decides, usually in the order permanent home, centre of vital interests, habitual abode, nationality. Dutch law follows the outcome: becoming treaty-resident elsewhere is itself a deemed disposal of a substantial interest (Wet IB 2001 art. 4.16(1)(h)). For a company, a Dutch-incorporated BV whose management sits abroad stays Dutch under art. 2(5) Wet Vpb, and the treaty decides which state may tax.
- **Relief method.** The Netherlands gives relief after computing tax on worldwide income: an exemption-type reduction for foreign employment and business income, and a credit for foreign withholding on dividends, interest and royalties, under the applicable treaty or the unilateral decree (Besluit voorkoming dubbele belasting 2001). Method, formulas and treaty dividend rates: [nl-double-tax-relief](nl-double-tax-relief.md).
- **Dividend tax relief.** Withholding is not required on distributions to a corporate shareholder established in the EU, the EEA, or a treaty state with a dividend article, if the holding would qualify for the participation exemption had the shareholder been Dutch, subject to anti-abuse conditions (Wet DB art. 4(2) and (3)). Treaty rates apply otherwise.
- **Conditional withholding tax** applies to interest, royalties and dividends paid by a Dutch entity to an affiliated entity (a qualifying interest, meaning decisive influence) in a low-tax jurisdiction, and in some abuse cases. The lists are published each year on overheid.nl ("Overzicht laagbelastende landen 2026").
- **EU social security.** Within the EU, EEA and Switzerland, Regulation (EC) 883/2004 decides which single country's social security applies, normally the country where the work is done, with A1 certificates for postings. A non-resident who is not insured in the Netherlands pays only the 8.10% tax part of the first box 1 band, not the 27.65% national insurance part. Payroll treatment is in [nl-payroll-tax](nl-payroll-tax.md).
- **Corporate side.** Participation exemption, foreign permanent establishments and CFC rules are in [nl-corporate-tax](nl-corporate-tax.md); related-party pricing in [netherlands-transfer-pricing](netherlands-transfer-pricing.md).

## Worked examples

### Example 1: an engineer moves to Amsterdam in January 2026 under the expat scheme

She is 35, recruited from Spain, lived there all her life, and has a ruling from her first payroll in January 2026. Agreed wage including the allowance: €90,000 for 2026. She is resident for the whole year and below AOW age.

1. Maximum tax-free allowance: 30% × €90,000 = €27,000.
2. Wage excluding the allowance: €63,000. That is more than the €48,013 norm, so the scheme holds.
3. Box 1 tax on €63,000 before tax credits: €38,883 × 35.75% = €13,900.67, plus (€63,000 − €38,883) × 37.56% = €9,058.35. Total €22,959.02.
4. Without the scheme, tax on €90,000 before credits would be €34,482.15, so the scheme saves €11,523.13 before credits.
5. From 1 January 2027 her maximum falls to 27% (€24,300 on the same wage), and her wage excluding the allowance must exceed the 2027 norm (announced at €51,899 before indexation).

Tax credits (general and labour credits) are left out; they reduce both figures and are computed in [nl-income-tax](nl-income-tax.md).

```oa-check
name: Expat scheme, wage EUR 90,000 including allowance (2026 box 1, before credits)
inputs:
  wage: 90000
  norm: 48013
steps:
  - allowance: wage * 0.30
  - taxable: wage - allowance
  - headroom: taxable - norm
  - tax_with: round(min(taxable, 38883) * 0.3575 + (min(taxable, 78426) - 38883) * 0.3756 + max(taxable - 78426, 0) * 0.495, 2)
  - tax_without: round(min(wage, 38883) * 0.3575 + (min(wage, 78426) - 38883) * 0.3756 + max(wage - 78426, 0) * 0.495, 2)
  - saving: tax_without - tax_with
  - allowance_2027: wage * 0.27
expected:
  allowance: 27000
  taxable: 63000
  headroom: 14987
  tax_with: 22959.02
  tax_without: 34482.15
  saving: 11523.13
  allowance_2027: 24300
```

### Example 2: a founder emigrates to Portugal in 2026 holding 100% of a Dutch BV

He paid €18,000 for the shares when he formed the BV. On the day he deregisters from his Dutch municipality the shares are worth €500,000. He is single and has no other box 2 income that year.

1. Leaving is a deemed disposal of his substantial interest (Wet IB 2001 art. 4.16(1)(h)).
2. Deemed gain: €500,000 − €18,000 = €482,000.
3. Box 2 tax: €16,866 on the first €68,843, plus 31% × (€482,000 − €68,843) = €128,078.67. Total €144,944.67.
4. This amount goes into a protective assessment after he files the 2026 M return. Portugal is in the EU, so deferral is automatic and no collection interest runs.
5. Because he left after 15 September 2015, the deferral is for life and is never remitted after 10 years. If the BV pays him a dividend, or he sells the shares, he must report it and pay the matching part of the €144,944.67. His acquisition price for any later Dutch tax on the shares is €500,000 (art. 7.6).
6. A dividend from the BV is also subject to 15% dividend tax at source; how the dividend tax and the protective assessment interact, and what the Portugal treaty allows, should be referred.

```oa-check
name: Emigration with a substantial interest, deemed gain EUR 482,000 (2026 box 2)
inputs:
  market_value: 500000
  acquisition_price: 18000
steps:
  - gain: market_value - acquisition_price
  - box2_tax: 16866 + max(gain - 68843, 0) * 0.31
expected:
  gain: 482000
  box2_tax: 144944.67
```

## Ask the client first

1. The exact arrival or departure date, and what ties stay behind: a home, a partner or children, a job, registration with the municipality.
2. Where the person becomes resident under the other country's law, and which treaty applies.
3. For an arrival: was the person recruited or seconded from abroad, where did they live in the 24 months before, what is the agreed wage, and when was any ruling first applied?
4. For a departure: any shareholding of 5% or more in a company (with acquisition price and current value), any Dutch pension, annuity or own-home insurance, and the destination country (EU or not).
5. For a non-resident: what Dutch income they have (work days in the Netherlands, Dutch property, Dutch company shares) and what share of world income it is, for the 90% qualifying test.
6. For a company: where the board meets and decisions are taken, where it was incorporated, and whether it pays interest, royalties or dividends to affiliates in low-tax jurisdictions.

## Sources

| Source | URL | Read on |
|---|---|---|
| Algemene wet inzake rijksbelastingen (AWR), arts. 4, 19, 67a, 67c, 67d, 67e, 67f | https://wetten.overheid.nl/BWBR0002320/ | 2026-10-22 |
| Wet op de vennootschapsbelasting 1969, arts. 2(5), 17, 22 | https://wetten.overheid.nl/BWBR0002672/ | 2026-10-22 |
| Wet inkomstenbelasting 2001, arts. 2.10, 2.12, 2.13, 4.16, 5.5, 7.1, 7.2, 7.6, 7.7, 7.8 | https://wetten.overheid.nl/BWBR0011353/ | 2026-10-22 |
| Wet op de loonbelasting 1964, art. 31a(8): expat scheme at up to 30% of the designated wage, capped at 30% of the WNT maximum (text valid from 1 January 2026; the cut to 27% from 2027 was made by the Belastingplan 2025 and is set out in Handboek §19.4) | https://wetten.overheid.nl/BWBR0002471/ | 2026-10-22 |
| Wet op de dividendbelasting 1965, arts. 4, 5, 7 | https://wetten.overheid.nl/BWBR0002515/ | 2026-10-22 |
| Wet bronbelasting 2021, arts. 1.2, 2.1, 4.1, 5.1, 5.2 | https://wetten.overheid.nl/BWBR0042952/ | 2026-10-22 |
| Invorderingswet 1990 (conserverende aanslag deferral, art. 25) | https://wetten.overheid.nl/BWBR0004770/ | 2026-10-22 |
| Belastingdienst, Conserverende aanslag bij emigratie | https://www.belastingdienst.nl/wps/wcm/connect/nl/buitenland/content/conserverende-aanslag-bij-emigratie | 2026-10-22 |
| Belastingdienst, Aangifte doen over het jaar van emigratie of immigratie (M return) | https://www.belastingdienst.nl/wps/wcm/connect/nl/buitenland/content/deels-niet-in-nederland-wonen-m-aangifte-doen | 2026-10-22 |
| Belastingdienst, Inkomensverklaring voor kwalificerend buitenlands belastingplichtigen | https://www.belastingdienst.nl/wps/wcm/connect/nl/buitenland/content/inkomensverklaring-aangifte-inkomstenbelasting-buitenlandse-belastingplichtigen | 2026-10-22 |
| Belastingdienst, notice on the 2025 M return (online from 1 May, until 1 July 2026) | https://sorry.belastingdienst.nl/mbd/storing/nog-geen-aangifte-doen | 2026-10-23 |
| Belastingdienst, Aangifte inkomstenbelasting als buitenlands belastingplichtige | https://www.belastingdienst.nl/wps/wcm/connect/nl/buitenland/content/buitenlands-belastingplichtig-hoe-doe-ik-aangifte-inkomstenbelasting | 2026-10-23 |
| Belastingdienst, Uitstel aanvragen belastingaangifte buitenland | https://www.belastingdienst.nl/wps/wcm/connect/nl/buitenland/content/uitstel-aanvragen-belastingaangifte-buitenland-hoe-doe-ik-dat | 2026-10-23 |
| Belastingdienst, Fiscale informatie 2026, U woont buiten Nederland | https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/u_woont_buiten_nederland | 2026-10-23 |
| Belastingdienst, Aangifte doen en betalen bronbelasting | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/bronbelasting-rente-en-royalty/aangifte-doen-en-betalen-+bronbelasting | 2026-10-23 |
| Belastingdienst, Box 1 uitleg en tarieven | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/prive/inkomstenbelasting/heffingskortingen_boxen_tarieven/boxen_en_tarieven/box_1/box_1 | 2026-10-22 |
| Belastingdienst, Expat Scheme (30% facility) | https://www.belastingdienst.nl/wps/wcm/connect/en/individuals/content/coming-to-work-in-the-netherlands-30-percent-facility | 2026-10-22 |
| Belastingdienst, Handboek Loonheffingen 2026 (March 2026), §19.4 | https://download.belastingdienst.nl/belastingdienst/docs/handboek-loonheffingen-lh0221t61fd.pdf | 2026-10-22 |
| Belastingdienst, Bronbelasting op renten, royalty's en dividenden | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/bronbelasting-rente-en-royalty/bronbelasting-op-renten-en-royalty | 2026-10-22 |
| Belastingdienst, Overzicht percentages belastingrente | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/standaard_functies/prive/contact/rechten_en_plichten_bij_de_belastingdienst/belastingrente/overzicht_percentages_belastingrente | 2026-10-22 |
| Belastingdienst, Invorderingsrente | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/standaard_functies/prive/contact/rechten_en_plichten_bij_de_belastingdienst/invorderingsrente | 2026-10-22 |

Not yet confirmed: the filing deadlines for 2026 M and non-resident returns (set in the 2027 invitation letters); the final 2027 expat salary norm and 2027 WNT cap.

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
