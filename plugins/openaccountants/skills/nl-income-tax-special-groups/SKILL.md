---
name: nl-income-tax-special-groups
description: "Dutch individual income tax for three groups the main skill does not compute, tax year 2026. (1) People at state pension (AOW) age: the lower first box 1 band rate (17.85%), the longer first band for people born before 1 January 1946, the month-by-month rate for people reaching AOW age in 2026, and the AOW-age general credit, labour credit, ouderenkorting and alleenstaande ouderenkorting. (2) Non-residents: the qualifying non-resident test (Wet IB 2001 art. 7.8) and which tax credits a non-resident gets, including the tax-part-only rule (art. 2.7 and 8.3). (3) Box 3: the actual-return route (tegenbewijsregeling, art. 5.25 to 5.31) against the 2026 deemed return, and the status of the Wet werkelijk rendement box 3. Trigger on: AOW, pensioner, ouderenkorting, gepensioneerd, non-resident tax credits, kwalificerende buitenlandse belastingplichtige, 90% test, belastingdeel heffingskorting, werkelijk rendement, tegenbewijsregeling, opgaaf werkelijk rendement. Out of scope: ordinary residents"
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/nl-income-tax-special-groups"
  jurisdiction: "NL"
  tax_year: "2026"
  last_updated: "2026-10-23"
  authored_by: "Ryan Duguid"
  trust_label: "Accountant-authored"
  review_status: "pending_review"
---

# Netherlands: income tax at AOW age, for non-residents, and the box 3 actual-return route (2026) v0.1

> **Source-cited draft.** No accountant has reviewed this skill yet. Every figure comes from wetten.overheid.nl, belastingdienst.nl or eerstekamer.nl, read on 23 October 2026. It prepares working papers; it is not authority to file or pay.

This skill fills three gaps in the Dutch individual income tax (IT-IND) pack. It does not repeat:

- the ordinary box 1, box 2 and box 3 computation, the below-AOW credit tables and the zzp profit bridge: [nl-income-tax](nl-income-tax.md), [nl-zzp-deductions](nl-zzp-deductions.md), [nl-deductions](nl-deductions.md);
- residence, the M return for a migration year, the expat scheme, exit tax and treaties: [nl-cross-border](nl-cross-border.md);
- substantial interest (box 2): [nl-box2-substantial-interest](nl-box2-substantial-interest.md).

Tax year: the calendar year 2026.

## Who this applies to

**1. People at AOW (state pension) age.** The AOW age in 2026 is 67 (Belastingdienst box 1 page: "In 2026 wordt u 67 jaar? Dan bereikt u de AOW-leeftijd"). From the first day of the month in which a person reaches AOW age, the AOW premium (17.90%) stops (Wet financiering sociale verzekeringen, Wfsv, art. 10(2)). The other national insurance premiums (Anw 0.10%, Wlz 9.65%) continue. Three branches:

- reached AOW age before 2026 and born on or after 1 January 1946: first band to €38,883 at 17.85%;
- born before 1 January 1946: first band to €41,123 at 17.85% (Wet IB 2001 art. 2.10a);
- reaches AOW age during 2026: a first-band rate set by the month (table below).

**2. Non-residents** (buitenlandse belastingplichtigen) with Dutch income. A non-resident is a **qualifying non-resident** (kwalificerende buitenlandse belastingplichtige) when they live in another EU state, an EEA state (Liechtenstein, Norway, Iceland), Switzerland or on Bonaire, Sint Eustatius or Saba, and their income is wholly or almost wholly taxed in the Netherlands (Wet IB 2001 art. 7.8(6)). The Belastingdienst applies this as at least 90% of world income, counting box 2 and box 3 income too. A person who pays no tax at home because their only income is a small Dutch pension or benefit also qualifies. Fiscal partners may add their incomes together for the 90% test. UK residents covered by the Brexit Withdrawal Agreement count as EU residents for this test (art. 10a.22).

**3. Box 3 taxpayers whose actual return is below the deemed return.** Anyone with box 3 savings and investments can prove a lower actual return and be taxed on that instead (Wet IB 2001 art. 5.25).

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Box 1 first band, reached AOW age before 2026, born on or after 1 Jan 1946 | 17.85% to €38,883 (8.10% tax + 0.10% Anw + 9.65% Wlz) | 2026 | [Belastingdienst box 1](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/prive/inkomstenbelasting/heffingskortingen_boxen_tarieven/boxen_en_tarieven/box_1/box_1); [Wet IB 2001 art. 2.10](https://wetten.overheid.nl/BWBR0011353/2026-01-01) |
| Box 1 first band, born before 1 Jan 1946 | 17.85% to €41,123 | 2026 | same; [Wet IB 2001 art. 2.10a](https://wetten.overheid.nl/BWBR0011353/2026-01-01) |
| Box 1 second and third band, all AOW-age branches | 37.56% to €78,426; 49.50% above | 2026 | same |
| First-band rate for someone reaching AOW age in 2026, by month | Jan 17.85%, Feb 19.34%, Mar 20.83%, Apr 22.33%, May 23.82%, Jun 25.31%, Jul 26.80%, Aug 28.29%, Sep 29.78%, Oct 31.28%, Nov 32.77%, Dec 34.26% (band to €38,883). The Toelichting 2026 ch. 29 prints six of these 0.01 point lower: Apr 22.32%, May 23.81%, Jun 25.30%, Oct 31.27%, Nov 32.76%, Dec 34.25% | 2026 | [Belastingdienst box 1](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/prive/inkomstenbelasting/heffingskortingen_boxen_tarieven/boxen_en_tarieven/box_1/box_1); [Belastingdienst, belastingberekening 2026](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/belastingberekening) |
| Premium income maximum (premie-inkomen) | €38,883; €41,123 if born before 1 Jan 1946 | 2026 | [Belastingdienst, premie volksverzekeringen 2026](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/premie_volksverzekeringen) |
| General tax credit, AOW age all of 2026 | €1,556, reduced by 3.195% of verzamelinkomen above €29,736; nil above €78,426 | 2026 | [Belastingdienst, heffingskortingen 2026](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/heffingskortingen) |
| Labour credit, AOW age all of 2026 | to €11,965: 4.156%; to €25,845: €498 + 15.483% of excess over €11,965; to €45,592: €2,647 + 0.974% of excess over €25,845; to €132,920: €2,840 − 3.250% of excess over €45,592; nil above | 2026 | same |
| Income-dependent combination credit (IACK), AOW age all of 2026 | 5.72% of work income above €6,239, maximum €1,514 | 2026 | same |
| Ouderenkorting (elderly credit) | €2,067 if verzamelinkomen up to €46,002; reduced by 15% of the excess; nil above €59,782 | 2026 | [Wet IB 2001 art. 8.17](https://wetten.overheid.nl/BWBR0011353/2026-01-01); Belastingdienst heffingskortingen 2026 |
| Alleenstaande ouderenkorting (single elderly credit) | €540 | 2026 | [Wet IB 2001 art. 8.18](https://wetten.overheid.nl/BWBR0011353/2026-01-01) |
| Tax part of a credit (belastingdeel) | 8.10/35.75 of the credit; premium parts 17.90 (AOW), 0.10 (Anw), 9.65 (Wlz) over 35.75 | 2026 | [Wet IB 2001 art. 8.3 to 8.6](https://wetten.overheid.nl/BWBR0011353/2026-01-01); Belastingdienst heffingskortingen 2026, §21.9 |
| Tax part of ouderenkorting and alleenstaande ouderenkorting | 8.10/17.85 (the AOW premium is left out of the combined rate; the AOW part is nil) | 2026 | [Wet IB 2001 art. 8.7](https://wetten.overheid.nl/BWBR0011353/2026-01-01) |
| Payout of the general credit to a non-earning partner | Only if born before 1 January 1963 | 2026 | Belastingdienst heffingskortingen 2026, §21.8 |
| Box 3 deemed return: bank balances | 1.28% (provisional; fixed early 2027) | 2026 | [Belastingdienst, box 3 2026](https://www.belastingdienst.nl/wps/wcm/connect/nl/box-3/content/berekening-box-3-inkomen-2026) |
| Box 3 deemed return: investments and other assets | 6.00% (fixed) | 2026 | same |
| Box 3 deemed return: debts | 2.70% (provisional) | 2026 | same |
| Box 3 debt threshold | €3,800; €7,600 for partners together | 2026 | [Wet IB 2001 art. 5.3(3)(f)](https://wetten.overheid.nl/BWBR0011353/2026-01-01) |
| Box 3 tax-free allowance (heffingvrij vermogen) | €59,357 per person; none in the actual-return route | 2026 | [Wet IB 2001 art. 5.5](https://wetten.overheid.nl/BWBR0011353/2026-01-01); [Belastingdienst, belastingberekening 2026](https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/belastingberekening) |
| Box 3 rate | 36% | 2026 | [Wet IB 2001 art. 2.13](https://wetten.overheid.nl/BWBR0011353/2026-01-01) |

The 2026 general credit for someone under AOW age is €3,115. The AOW-age figure of €1,556 is the credit with the AOW premium part (17.90/35.75) taken out (€3,115 × 17.85/35.75 = €1,555.34; the Belastingdienst publishes €1,556), because a person at AOW age no longer pays that premium (Wet IB 2001 art. 8.4; Wfsv art. 12). The under-AOW tables are in [nl-income-tax](nl-income-tax.md).

## The taxable base

### AOW age

- **What is taxed.** The AOW benefit and occupational pensions are box 1 income. They are not work income (arbeidsinkomen), so they do not earn the labour credit (Wet IB 2001 art. 8.1(1)(e)). A pensioner who still works, employed or self-employed, gets the AOW-age labour credit on that work income.
- **Credits for the whole year at AOW age.** Use the AOW-age general credit, labour credit and IACK tables. The ouderenkorting applies to someone who has reached AOW age at the end of the year (art. 8.17(1)). The alleenstaande ouderenkorting applies to someone entitled to the single person's AOW benefit, or who would be except for years spent abroad before AOW age (art. 8.18(1)).
- **Reaching AOW age in 2026.** Apply the month rate to the first band for the whole year. The ouderenkorting applies in full because the person is at AOW age at year end. The Belastingdienst says the general credit and labour credit change too, but the 2026 Toelichting publishes no part-year table. The online return computes it.
- **Credit cap.** Total credits cannot exceed the combined tax and premium due (art. 8.8). Unused credits are lost, except the payout rules for a non-earning partner born before 1963.

### Non-residents

- **What is taxed.** Only Dutch income in each box (art. 7.1 to 7.7); see [nl-cross-border](nl-cross-border.md). A non-resident not insured for Dutch national insurance pays only the 8.10% tax part of the first band.
- **Qualifying non-resident.** Treated like a resident for: the tax part of every credit, personal deductions (gifts, medical costs, alimony), mortgage interest on the home abroad, income provisions such as annuity premiums, fiscal partnership, and income averaging (art. 7.8(1) to (3); Belastingdienst §30.2.2). A deduction is not given if the home state already allows the same thing (art. 7.8(4)). The status can apply to part of the year; the benefits are then time-apportioned (Belastingdienst §30.2.1.1).
- **Non-qualifying non-resident living in the EU, EEA, Switzerland or BES**, or one with Dutch business profit who can rely on a treaty clause against discrimination of permanent establishments: only the tax part of the **labour credit** and of the **IACK** (art. 2.7(1), third sentence). No general credit, no ouderenkorting, no personal deductions, no fiscal partner.
- **Non-qualifying non-resident living anywhere else**: no tax credit against income tax at all. Article 2.7(1) gives the credit only to residents, qualifying non-residents and the group in the bullet above.
- **Belgium, Suriname and Aruba.** Non-qualifying residents of these states get extra benefits (Belastingdienst §30.2.4): Belgium, the tax part of the general credit, labour credit and IACK, some personal deductions pro rata, and a fiscal partner; Suriname and Aruba, the tax part of the general credit and labour credit, some deductions and a fiscal partner. Read the chapter before computing.
- **Box 3.** Every non-resident gets the €59,357 tax-free allowance against Dutch box 3 assets (Belastingdienst §30.2: "U hebt recht op het heffingsvrij vermogen voor uw bezittingen in box 3").
- **Income statement.** The law now requires a statement from the home tax authority only when the inspector asks for it (art. 7.8(6)). The Belastingdienst Toelichting says the general requirement was abolished from 2026.
- **Premium parts.** Someone insured for Dutch national insurance, resident or not, gets the premium parts of the credits for the insured schemes, time-apportioned for part-year insurance (Wfsv art. 12; Belastingdienst §21.9.1).

### Box 3 actual return (tegenbewijsregeling)

- **The rule.** If the taxpayer shows that the actual return is lower than the deemed benefit from savings and investments (voordeel uit sparen en beleggen), box 3 income is the actual return, less personal deductions (art. 5.25(1)). The actual return is set at nil at least (art. 5.25(2)). Partners share the joint actual return in the same ratio as they shared the deemed base (art. 5.25(4)).
- **What counts.** The actual return is all benefits from box 3 assets and debts (art. 5.26):
  - **regular benefits:** interest, rent, dividends, profit distributions, licence and user fees, and the economic rental value of property held for own use (art. 5.27, 5.27a). Interest paid on box 3 debts is negative (art. 5.27(2));
  - **capital growth (vermogensaanwas):** net asset value at 31 December less net asset value at 1 January, less deposits plus withdrawals (art. 5.28 to 5.30). Unrealised gains and losses count. A dwelling is valued at its WOZ value; the year-end value is the WOZ value set for the next year (art. 5.31(2)).
- **No allowance, no costs, no carry-forward.** The tax-free allowance does not apply. Costs are not deductible (for example dealing costs on shares, or maintenance on a second home). Two exceptions: interest paid on a box 3 debt, and an investment in a second home that raised its WOZ value and was reported to the municipality. Gains and losses across assets are netted within the year; a negative total becomes nil and cannot be carried to another year (Belastingdienst, belastingberekening 2026).
- **Assets bought during the year count.** The deemed return looks only at 1 January; the actual return includes assets bought or sold during the year.
- **Coming system.** The Wet werkelijk rendement box 3 (bill 36 748) was adopted by the Tweede Kamer on 12 February 2026 and is still before the Eerste Kamer. The Eerste Kamer debated it on 30 June 2026 and put off the vote until the announced novelle is dealt with. On 13 October 2026 the Eerste Kamer finance committee provisionally agreed the cabinet's route and decided to wait for the Tweede Kamer to deal with an amending bill (novelle) before deciding on the bill. Entry into force is by royal decree; the bill aims at 1 January 2028. It is not law today. Use the deemed return and the tegenbewijsregeling for 2026.

## Deadlines and filing

- **Return date.** File by the date in the invitation to file (aangiftebrief). The Belastingdienst says this is usually 1 May. An extension adds 4 months, usually to 1 September. For the 2025 return the extension request had to be made by 1 May 2026 ([Belastingdienst, uitstel](https://www.belastingdienst.nl/wps/wcm/connect/nl/belastingaangifte/content/kan-ik-nog-uitstel-aanvragen-belastingaangifte)).
- **Non-residents** file online in Mijn Belastingdienst or on the paper C form. Without an invitation, they must still file if the tax due is above the assessment threshold (€57 for 2025; €58 for 2026, Toelichting 2026 ch. 29), and may file up to 5 years back: for 2025, until 31 December 2030 ([Belastingdienst, buitenlands belastingplichtig](https://www.belastingdienst.nl/wps/wcm/connect/nl/buitenland/content/buitenlands-belastingplichtig-hoe-doe-ik-aangifte-inkomstenbelasting)). Extensions for non-residents are in writing on the form or by phone to the BelastingTelefoon Buitenland.
- **Actual return, 2025 onwards.** It is part of the income tax return. When box 3 assets exceed the tax-free allowance, the online return asks whether the taxpayer wants to give the actual return. Giving it is optional; the Belastingdienst then computes both and uses the lower ([Belastingdienst, werkelijk rendement in aangifte](https://www.belastingdienst.nl/wps/wcm/connect/nl/box-3/content/werkelijk-rendement-belastingaangifte)).
- **Actual return, 2024 and earlier.** Use the form "Opgaaf werkelijk rendement" in Mijn Belastingdienst. For 2021 to 2024 it can be filed without a letter; for 2017 to 2020 only after a letter, and all those letters have been sent ([Belastingdienst, opgaaf zonder brief](https://www.belastingdienst.nl/wps/wcm/connect/nl/box-3/content/zonder-brief-formulier-opgaaf-werkelijk-rendement-invullen)). Supporting documents may follow within 6 weeks of sending the form (art. 5.25(7)).
- **Provisional assessment 2026.** The 2026 provisional assessment uses only the deemed return; the actual return is applied in the 2026 return.

## Penalties and interest

- **Late return:** reminder, then a demand with 10 working days; after that a default penalty of €469, rising to €6,709 for repeat lateness ([Belastingdienst, te laat aangifte](https://www.belastingdienst.nl/wps/wcm/connect/nl/belastingaangifte/content/wat-gebeurt-er-als-ik-geen-aangifte-doe-of-te-laat-of-onvolledig)). The legal maximum is AWR art. 67a; see [nl-cross-border](nl-cross-border.md).
- **Tax interest (belastingrente):** runs on an income tax assessment payable after 1 July following the year. The 2026 rate (5%) and the collection interest rate are in [nl-cross-border](nl-cross-border.md).
- **Wrong actual-return figures:** a too-low assessment caused by intent or gross negligence carries a penalty of up to 100% (AWR art. 67e; see [nl-cross-border](nl-cross-border.md)).

## Cross-border points

- **Pensioner living abroad.** A Dutch AOW or pension paid to a non-resident who is not insured in the Netherlands carries 8.10% in the first band, not 17.85%. Whether the Netherlands may tax a private pension depends on the treaty; see [nl-cross-border](nl-cross-border.md).
- **Tax part example.** A full under-AOW labour credit of €5,300 has a tax part of €5,300 × 8.10/35.75 = €1,200.84. That is all a non-qualifying EU-resident employee gets.
- **Qualifying test includes foreign wealth.** Large foreign savings can break the 90% test even when all work income is Dutch: the Belastingdienst example has €50,000 Dutch wages and €6,000 deemed foreign box 3 benefit, 89.3% in the Netherlands, so not qualifying.
- **Social security.** Which country's national insurance applies is decided under Regulation (EC) 883/2004 within the EU, EEA and Switzerland; see [nl-cross-border](nl-cross-border.md) and [nl-social-contributions](nl-social-contributions.md).
- **Box 3 for non-residents** covers only Dutch real estate, rights relating to it, and profit shares in a business managed in the Netherlands, less related debts (art. 7.7); the actual-return route applies to those assets.

## Worked examples

### Example 1: a single pensioner born in 1955 with €30,000 AOW and pension

She was born in 1955, reached AOW age before 2026, lives alone in the Netherlands and receives the single AOW benefit. In 2026 her AOW plus occupational pension totals €30,000. No other income, no deductions.

1. Box 1: all €30,000 is in the first band. Tax and premiums: €30,000 × 17.85% = €5,355.00.
2. General credit at AOW age: €1,556 − 3.195% × (€30,000 − €29,736) = €1,556 − €8.43 = €1,547.57.
3. Labour credit: nil. Pension and AOW are not work income.
4. Ouderenkorting: verzamelinkomen €30,000 is below €46,002, so €2,067 in full.
5. Alleenstaande ouderenkorting: she gets the single AOW benefit, so €540.
6. Total credits €4,154.57. Tax and premiums after credits: €5,355.00 − €4,154.57 = €1,200.43, before the return's rounding. The SVB and pension fund will have withheld wage tax during the year; the return reconciles the two. The income-dependent Zvw health contribution is separate.

```oa-check
name: Single pensioner born 1955, AOW and pension EUR 30,000 (2026 box 1)
inputs:
  income: 30000
steps:
  - box1: income * 0.1785
  - general_credit: max(1556 - 0.03195 * max(income - 29736, 0), 0)
  - elderly_credit: max(2067 - 0.15 * max(income - 46002, 0), 0)
  - single_elderly_credit: 540
  - credits: general_credit + elderly_credit + single_elderly_credit
  - tax_after_credits: round(box1 - credits, 2)
expected:
  box1: 5355.00
  general_credit: 1547.5652
  credits: 4154.5652
  tax_after_credits: 1200.43
```

### Example 2: €300,000 of savings and investments, deemed against actual return

A single resident holds on 1 January 2026: €100,000 in bank accounts and €200,000 in listed shares. No debts, no partner, no personal deductions. During 2026 the bank pays €1,200 interest, the shares pay €3,000 dividends (both paid out and spent), and the share prices rise so the portfolio is worth €202,000 on 31 December with no purchases or sales. Dealing and custody costs of €400 are not deductible.

**Deemed route.**

1. Deemed return: €100,000 × 1.28% + €200,000 × 6.00% = €1,280 + €12,000 = €13,280.
2. Base (rendementsgrondslag): €300,000. Taxable base after allowance: €300,000 − €59,357 = €240,643.
3. Deemed benefit: €13,280 × €240,643 / €300,000 = €10,652.46. (The Belastingdienst rounds the ratio to a percentage first; the return's figure can differ by a few euros.)
4. Tax: 36% × €10,652.46 = €3,834.89.

**Actual route.**

1. Regular benefits: €1,200 interest + €3,000 dividends = €4,200.
2. Capital growth: shares €202,000 − €200,000 = €2,000. This follows the Belastingdienst method: income received plus the change in value of the assets themselves, with each euro counted once.
3. Actual return €6,200. No allowance and no cost deduction. Tax: 36% × €6,200 = €2,232.00.

The actual return (€6,200) is below the deemed benefit (€10,652.46), so box 3 income is €6,200 (art. 5.25(1)). Saving: €1,602.89. The bank rate of 1.28% is provisional; the final 2026 percentage is set early in 2027 and changes the deemed side.

```oa-check
name: Box 3 EUR 300,000, deemed versus actual return (2026)
inputs:
  bank: 100000
  shares: 200000
  allowance: 59357
  interest: 1200
  dividends: 3000
  shares_end: 202000
steps:
  - deemed_return: bank * 0.0128 + shares * 0.06
  - base: bank + shares
  - taxable_base: max(base - allowance, 0)
  - deemed_benefit: round(deemed_return * taxable_base / base, 2)
  - tax_deemed: round(deemed_benefit * 0.36, 2)
  - actual_return: max(interest + dividends + (shares_end - shares), 0)
  - box3_income: min(actual_return, deemed_benefit)
  - tax_final: round(box3_income * 0.36, 2)
  - saving: tax_deemed - tax_final
expected:
  deemed_return: 13280
  taxable_base: 240643
  deemed_benefit: 10652.46
  tax_deemed: 3834.89
  actual_return: 6200
  tax_final: 2232.00
  saving: 1602.89
```

## Ask the client first

1. Date of birth, and the month AOW age was or will be reached. Born before 1 January 1946 changes the first band.
2. Does the client receive the single or the couple AOW benefit, and is there a fiscal partner? This decides the alleenstaande ouderenkorting and the payout rules.
3. Does the client still have work income (wages, profit, freelance) after AOW age? That earns the AOW-age labour credit.
4. For a non-resident: country of residence, Dutch income, world income including foreign savings and investments (for the 90% test), and whether they are insured for Dutch national insurance.
5. For box 3: values of every asset and debt on 1 January and 31 December, all interest, dividends and rent received, interest paid, and every purchase, sale, deposit and withdrawal during the year with dates.
6. For a second home or let property: the WOZ values for this year and next, and any improvement reported to the municipality.

## Sources

| Source | URL | Read on |
|---|---|---|
| Wet inkomstenbelasting 2001 (text valid 1 January 2026), arts. 2.7, 2.10, 2.10a, 2.13, 5.2, 5.3, 5.5, 5.25 to 5.31, 7.8, 8.1 to 8.8, 8.10, 8.11, 8.17, 8.18, 10a.22 | https://wetten.overheid.nl/BWBR0011353/2026-01-01 | 2026-10-23 |
| Wet financiering sociale verzekeringen (text valid 1 January 2026), arts. 9 to 12 | https://wetten.overheid.nl/BWBR0017745/2026-01-01 | 2026-10-23 |
| Belastingdienst, Box 1 uitleg en tarieven (2026 and 2025, AOW tables) | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/prive/inkomstenbelasting/heffingskortingen_boxen_tarieven/boxen_en_tarieven/box_1/box_1 | 2026-10-23 |
| Belastingdienst, Toelichting 2026, ch. 21 Heffingskortingen | https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/heffingskortingen | 2026-10-23 |
| Belastingdienst, Toelichting 2026, ch. 27 Premie volksverzekeringen | https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/premie_volksverzekeringen | 2026-10-23 |
| Belastingdienst, Toelichting 2026, ch. 29 Belastingberekening (box 3 and actual return) | https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/belastingberekening | 2026-10-23 |
| Belastingdienst, Toelichting 2026, ch. 30 U woont buiten Nederland | https://www.belastingdienst.nl/wps/wcm/connect/fisin/fisin2026/u_woont_buiten_nederland | 2026-10-23 |
| Belastingdienst, Berekening box 3-inkomen voorlopige aanslag 2026 | https://www.belastingdienst.nl/wps/wcm/connect/nl/box-3/content/berekening-box-3-inkomen-2026 | 2026-10-23 |
| Belastingdienst, Werkelijk rendement in belastingaangifte 2025 | https://www.belastingdienst.nl/wps/wcm/connect/nl/box-3/content/werkelijk-rendement-belastingaangifte | 2026-10-23 |
| Belastingdienst, Opgaaf werkelijk rendement zonder brief | https://www.belastingdienst.nl/wps/wcm/connect/nl/box-3/content/zonder-brief-formulier-opgaaf-werkelijk-rendement-invullen | 2026-10-23 |
| Belastingdienst, Aangifte als buitenlands belastingplichtige | https://www.belastingdienst.nl/wps/wcm/connect/nl/buitenland/content/buitenlands-belastingplichtig-hoe-doe-ik-aangifte-inkomstenbelasting | 2026-10-23 |
| Belastingdienst, Uitstel aanvragen belastingaangifte 2025 | https://www.belastingdienst.nl/wps/wcm/connect/nl/belastingaangifte/content/kan-ik-nog-uitstel-aanvragen-belastingaangifte | 2026-10-23 |
| Belastingdienst, Uitstel aangifte buitenland | https://www.belastingdienst.nl/wps/wcm/connect/nl/buitenland/content/uitstel-aanvragen-belastingaangifte-buitenland-hoe-doe-ik-dat | 2026-10-23 |
| Belastingdienst, Te laat of geen aangifte | https://www.belastingdienst.nl/wps/wcm/connect/nl/belastingaangifte/content/wat-gebeurt-er-als-ik-geen-aangifte-doe-of-te-laat-of-onvolledig | 2026-10-23 |
| Eerste Kamer, Wet werkelijk rendement box 3 (36.748) | https://www.eerstekamer.nl/wetsvoorstel/36748_wet_werkelijk_rendement_box | 2026-10-23 |

Not yet confirmed: which of the two Belastingdienst monthly first-band tables is exact for April, May, June, October, November and December (the box 1 page and the Toelichting ch. 29 differ by 0.01 point); the general credit, labour credit and IACK amounts for someone who reaches AOW age during 2026 (the Toelichting gives no part-year table); the exact rounding of the tax part of each credit for non-residents; how art. 5.28 to 5.30 treat income that is received into a box 3 bank account and then withdrawn (the worked example counts it once, as a regular benefit); the final 2026 box 3 percentages for bank balances and debts (set early 2027); the 2026 filing date (the 2027 invitation to file is not yet published; 1 May is the usual date); whether and when the Eerste Kamer adopts the Wet werkelijk rendement box 3 and its novelle.

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

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-10-23. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `nl-income-tax-special-groups` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/nl-income-tax-special-groups. If neither is available, confirm every figure against the official source pages cited above before relying on it.
