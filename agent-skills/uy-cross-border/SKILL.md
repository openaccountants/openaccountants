---
name: uy-cross-border
description: "Uruguay cross-border tax for 2026: the non-resident income tax (IRNR, Impuesto a las Rentas de los No Residentes) in Título 8 of the Texto Ordenado 2023 as amended by Ley 20.446, and its regulation Decreto 149/007. Covers who is resident (183 days, centre of interests, companies formed under Uruguayan law), what is Uruguayan-source income (technical services to IRAE payers, digital services, share sales of foreign entities holding Uruguayan assets from 2026), the IRNR rates (12% general, 7% dividends, 25% low or no-tax jurisdictions, reduced rates on local interest), the withholding rates and the gross-up for net payments, exemptions, the duty to appoint a representative, form 1246, and treaty relief under Uruguay's 25 double tax treaties in force. Trigger on: IRNR, no residentes Uruguay, retención IRNR, convenio doble imposición Uruguay, withholding tax Uruguay, royalties paid abroad Uruguay, dividend to foreign parent Uruguay. Out of scope: permanent establishments (IRAE), transfer p"
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/uy-cross-border"
  jurisdiction: "UY"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Uruguay: non-resident income tax (IRNR) and treaties, 2026 v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

This skill works out the Uruguayan tax on income a non-resident earns from Uruguay without a permanent establishment, and the amount a Uruguayan payer must withhold, for 2026. It links to the other Uruguay skills and does not repeat them:

- [uy-corporate-income-tax](uy-corporate-income-tax.md): permanent establishments (taxed in IRAE, not IRNR), the deduction limits for payments to non-residents, and residents' business income.
- [uruguay-income-tax](uruguay-income-tax.md): residents' income, including foreign capital income taxed from 2026, and the DGI fines that also apply to withholding agents.
- [uy-transfer-pricing](uy-transfer-pricing.md): related-party pricing, including dealings with low or no-tax jurisdictions.
- [uruguay-payroll](uruguay-payroll.md): BPS cover for workers posted abroad or employed by foreign companies.

**Which text of the law.** Título 8 (IRNR) of the Texto Ordenado 2023 approved by Decreto 101/024, as consolidated by IMPO with the changes of Ley 20.446 of 16 December 2025 (Diario Oficial 8 January 2026). The regulation is Decreto 149/007, consolidated by IMPO with amendments up to Decreto 255/026 of 1 October 2026; its references to the "Texto Ordenado 1996" are to the same rules now renumbered in the 2023 text.

**Quick reference, 2026**

| Item | Figure |
|---|---|
| Tax year | Calendar year; the tax arises on 31 December (T8 art. 8) |
| General IRNR rate | 12% (T8 art. 18 B) |
| Dividends paid by IRAE taxpayers | 7% (T8 art. 18 B) |
| Income of entities in low or no-tax jurisdictions | 25% (T8 art. 18 B), 30.25% withheld on real estate income (Decreto 149/007 art. 27) |
| Rent of real estate | 10.5% withheld (Decreto 149/007 art. 33) |
| Treaties in force | 25, listed by DGI; the treaty rate caps the IRNR rate for a resident of the other state who proves residence |

## Who this applies to

- **Non-residents.** IRNR taxes Uruguayan-source income of individuals and entities that are not resident (T8 arts. 1 and 2). An individual is resident if they stay in Uruguay more than 183 days in the calendar year (sporadic absences count, unless they prove tax residence elsewhere), or if the main core or base of their activities or economic or vital interests is in Uruguay; vital interests are presumed when the spouse and dependent minor children habitually live there (T8 art. 3). An entity formed under Uruguayan law is resident; a foreign entity becomes resident once it completes the formalities to set up its domicile in Uruguay (art. 4).
- **No permanent establishment.** A non-resident that acts in Uruguay through a permanent establishment pays IRAE on it, not IRNR (T8 art. 9); see [uy-corporate-income-tax](uy-corporate-income-tax.md). A payer does not withhold IRNR on payments to a permanent establishment, which pays the tax itself (Decreto 149/007 art. 41).
- **Options for some foreign staff.** Foreigners working in a free zone who are outside BPS can opt for IRNR on their wages; information technology specialists who moved to Uruguay under contracts started up to 28 February 2025 could opt for IRNR for the year of the option and four more (T8 art. 3). Employers of people taxed under the Programa de Fomento para la Atracción de Personas con Talento Calificado are also IRNR responsables sustitutos (T8 art. 10, last paragraph, added by Ley 20.446 art. 193).
- **Who acts.** IRAE taxpayers that pay or credit business, labour or capital income to IRNR taxpayers withhold it (T8 art. 10). The regulation adds the State and public bodies, entities that attribute income, and associations and foundations outside IRAE (Decreto 149/007 arts. 26, 28 and 32); banks, issuers and fund managers for interest and dividends (art. 34); escribanos for real estate gains (art. 37); auctioneers (art. 39). Sports clubs withhold 12% on transfers of players' federative and image rights (T8 art. 10).
- **Out of scope.** Permanent establishments, transfer pricing, residents' foreign income and foreign tax credits, Impuesto al Patrimonio of non-residents, and free-zone users' own taxation.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source URL |
|---|---|---|---|
| General rate ("restantes rentas"): services, royalties, most interest, gains, labour income | 12% | 2026 | https://www.impo.com.uy/bases/todgi-2023/8-2024 (T8 art. 18 B) |
| Dividends or profits paid or credited by IRAE taxpayers, and fictitious dividends (art. 14) | 7% | 2026 | same |
| Income of entities resident, domiciled or located in low or no-tax jurisdictions, or under such a regime, except IRAE dividends | 25% | 2026 | same |
| Interest on local bank deposits and on listed debt of residents, in pesos at a fixed nominal rate: up to 1 year / over 1 to 3 years / over 3 years | 5.5% / 2.5% / 0.5% | 2026 | same, art. 18 A |
| Same, in pesos with an adjustment clause: up to 1 year / over 1 to 3 years / over 3 years | 10% / 7% / 5% | 2026 | same |
| Same, in foreign currency: up to 1 year / over 3 years | 12% / 7% (the rate for over 1 to 3 years is blank in the consolidated text) | 2026 | same |
| Withholding on business income (services, technical services) of non-residents, general | 12% of the amount paid plus the withholding, without IVA | 2026 | https://www.impo.com.uy/bases/decretos/149-2007 (art. 27 c) |
| Withholding on business income of low or no-tax jurisdiction entities | 25% (30.25% on real estate income, except individuals) | 2026 | same, art. 27 a) and b) |
| Withholding on services outside employment, pensions paid abroad and free-zone wages taxed in IRNR | 12% of the amount paid plus the withholding | 2026 | same, arts. 28 to 31 |
| Withholding on rent of real estate | 10.5%; other real estate income 12% | 2026 | same, art. 33 |
| Real estate gains withheld by the escribano | 12% (30.25% for low or no-tax jurisdiction entities, except individuals) | 2026 | same, art. 38 |
| Federative and image rights of athletes | 12%; 25% for low or no-tax jurisdiction entities except individuals | 2026 | same, art. 36; T8 art. 10 |
| Fictitious dividends of an IRAE taxpayer (profit more than three years old) | 7%, paid the month after imputation; the treaty dividend rate if lower, with a residence certificate | 2026 | same, art. 35 bis; T8 art. 14 |
| Real estate income of low or no-tax jurisdiction entities | General rate plus 5.25% complementary rate | 2026 | https://www.impo.com.uy/bases/todgi-2023/8-2024 (T8 art. 16 A) |
| Exempt small transfers of assets | Single price up to UI 30,000, and the year's such sales below UI 90,000 | 2026 | same, art. 19 H |
| Shares of a non-resident entity: Uruguayan-source when, at any time in the previous 365 days, more than 50% of its assets were in Uruguay, or those assets exceeded UI 31,500,000 and more than 50% of them is transferred | Source rule (taxed at 12%) | 2026 | same, art. 7(3), as replaced by Ley 20.446 art. 658 |
| Digital services rendered directly to a user in Uruguay | 100% Uruguayan-source | 2026 | same, art. 17(3) |
| Intermediation through platforms: both parties in Uruguay / one abroad | 100% / 50% Uruguayan-source | 2026 | same, art. 17(6) |
| Foreign transport companies: fares and freight from Uruguay abroad | 20.83% of gross is Uruguayan-source | 2026 | same, art. 17(2) |
| Low-tax test in the regulation: effective tax on Uruguayan-source income below 12%, and no information exchange agreement in force (or one not fully applied) | Below 12% | 2026 | https://www.impo.com.uy/bases/decretos/149-2007 (art. 11 BIS) |
| Double tax treaties in force (DGI table of 25 April 2024) | 25 treaties | 2026 | https://www.gub.uy/direccion-general-impositiva/comunicacion/publicaciones/convenios-para-evitar-doble-imposicion |
| Example treaty: Spain (Ley 18.730), royalties | 5% for copyright on literary, artistic or scientific works; 10% otherwise | 2026 | https://www.impo.com.uy/bases/leyes-internacional/18730-2011 (art. 12(2)) |
| Example treaty: Spain, dividends | 5%; exempt where a company holds directly at least 75% of the paying company | 2026 | same (art. 10(2)) |
| Example treaty: Spain, interest | 10% | 2026 | same (art. 11(2)) |

## The base

**Uruguayan source** (T8 art. 7). Income from activities carried out, assets situated or rights used economically in Uruguay. Also Uruguayan-source, even if the work is done abroad:

- advertising and technical services (management, technical, administrative or advisory work of any kind) provided from abroad, outside employment, to IRAE taxpayers, as far as they relate to IRAE-taxed income;
- athletes' federative and image rights;
- sales of shares in non-resident entities that hold Uruguayan assets (the 50% and UI 31,500,000 tests in the table), on the share of assets situated in Uruguay; not where the ultimate owners stay the same (at least 95%) for two years, or in qualifying mergers and spin-offs;
- income of low or no-tax jurisdiction entities from intangibles bought by IRAE taxpayers for use in Uruguay, and from related-party imports and resales, presumed at 50% of the price.

Not Uruguayan-source: pay of foreign diplomats accredited in Uruguay, and non-residents' income from derivatives.

**Classes and amounts** (T8 arts. 6 and 13). Business income and labour income are taxed on the gross Uruguayan-source amount; capital income and gains on the amount computed as in IRPF. Results of different classes do not offset. **Where tax is withheld on a payment abroad, the base is the net amount paid plus the withholding** (art. 13), so a payer that bears the tax grosses the payment up: base = net paid / (1 - rate).

**Partly Uruguayan activities** (art. 17): insurance premiums (6.25% for life, 16.67% fire, 20.83% marine, 4.17% other risks), foreign transport (20.83%), film and television (100% from 2018), news agencies (20.83%), containers (31.25%), digital services and platforms as in the table.

**Exemptions** (T8 art. 19), among others: interest on public debt; interest on loans to IRAE taxpayers whose assets are more than 90% used for untaxed income; dividends out of income not taxed in IRAE, and dividends on shares listed on a Uruguayan exchange (art. 19 C, as replaced by Ley 20.446 art. 657); foreign exchange and adjustment gains; donations to public bodies; foreign shipping and air companies, subject to reciprocity; freight for exports; goods in transit in free zones and customs warehouses; foreign official bodies (reciprocity) and international organisations; pension fund results; income already in IRAE (art. 19 U, added by Ley 20.446 art. 659).

**Low or no-tax jurisdictions** (T8 arts. 5 and 16). The Executive sets the test (Decreto 149/007 art. 11 BIS: effective tax on the Uruguayan income below 12% and no information exchange in force) and DGI keeps the list. Such entities pay 25% instead of 12%, a 5.25% complement on real estate income, and their real estate gains are computed on the real basis.

**Treaty relief.** A treaty in force caps Uruguayan tax on its residents at the treaty rate. For treaty dividends on fictitious dividends the regulation applies the lower of 7% and the treaty rate, and requires a certificate of tax residence issued by the other state's competent authority (Decreto 149/007 art. 35 bis); DGI sets the conditions. Check the DGI table for the date each treaty applies from and whether the Multilateral Instrument (MLI) modifies it.

**Step by step, one payment to a non-resident.**

1. Is the recipient non-resident and without a permanent establishment in Uruguay? If it has one, stop: IRAE.
2. Is the income Uruguayan-source under art. 7 or 17? If not, no IRNR.
3. Is it exempt under art. 19?
4. Pick the rate: art. 18 (and the withholding rate in Decreto 149/007); 25% or 30.25% if the recipient is in a low or no-tax jurisdiction.
5. If a treaty applies and the recipient gives a residence certificate, cap the rate at the treaty rate.
6. Base: the gross amount; if the payer bears the tax, gross up the net payment.
7. Withhold on payment or credit, issue a receipt (resguardo), and declare and pay to DGI.

## Deadlines and filing

| Step | What | When | Where |
|---|---|---|---|
| On payment or credit | Withhold IRNR and give the recipient a resguardo | When paid or credited (Decreto 149/007 arts. 27, 33 and 42) | Payer's records |
| Withholding returns | Declare and pay the withholdings | In the terms DGI sets (art. 42) | DGI online services (SIGMA), form 1246 "Declaración de Retenciones del IRNR - Responsables" ([DGI forms list](https://www.gub.uy/direccion-general-impositiva/sites/direccion-general-impositiva/files/2023-11/Formularios%2Bincluidos%2Ben%2BBeta.pdf)) |
| Athletes' rights | Pay over the 12% | Month after the contract date (T8 art. 10) | DGI |
| Fictitious dividends | Pay the 7% | Month after the imputation (Decreto 149/007 art. 35 bis) | DGI |
| Non-resident's own return | Annual liquidation; optional where all the tax was withheld | After 31 December, as the Executive sets (T8 art. 20) | DGI |
| Representative | A non-resident with income not withheld (for example services or installation works in Uruguay without a permanent establishment) must appoint a resident representative and tell DGI | Before the income arises | DGI (T8 art. 11) |
| Identification | The recipient gives the payer its DGI registration number, or cannot credit the withholding | With the payment | Decreto 149/007 art. 43 |

## Penalties and interest

- **Late payment by the withholding agent**: the fines and monthly surcharge of the Código Tributario art. 94; see [uruguay-income-tax](uruguay-income-tax.md) for the figures. The agent is the taxpayer for the withholding: if the recipient does not identify itself, the agent still pays (Decreto 149/007 art. 43).
- **Representative not appointed or not notified**: an intention to defraud is presumed under Código Tributario art. 96 I), and the representative is jointly liable for the non-resident's tax (T8 art. 11).
- **Low-tax related parties**: an IRAE taxpayer that resells goods it exported to a related low-tax entity is jointly liable for that entity's IRNR (T8 art. 10).

## Cross-border points

- **Treaties in force** (DGI table): Germany, Argentina, Belgium, Brazil (applies from 1 January 2024), Chile, South Korea, Ecuador, United Arab Emirates, Spain, Finland, Hungary, India, Italy, Japan, Liechtenstein, Luxembourg, Malta, Mexico, Paraguay, Portugal, United Kingdom, Romania, Singapore, Switzerland and Vietnam. Colombia is signed but not in force. The MLI modifies 17 of them, from dates in the table.
- **Residents abroad**: a Uruguayan resident's foreign capital income is taxed from 2026 in IRPF ([uruguay-income-tax](uruguay-income-tax.md)); companies' foreign income and credits are in [uy-corporate-income-tax](uy-corporate-income-tax.md).
- **Changing residence**: a non-resident who becomes resident closes an IRNR period on that date (T8 art. 8 C).
- **Social security**: posted and foreign-employer workers' BPS cover is in [uruguay-payroll](uruguay-payroll.md).

## Two worked examples that recompute

### Example 1: patent royalty to a Spanish company, paid net of tax

A Uruguayan SA (an IRAE taxpayer) licenses a patent from a Spanish company that has no establishment in Uruguay. The contract says the Spanish company must receive UYU 900,000 net; the SA bears any Uruguayan tax.

The royalty is for a right used in Uruguay, so it is Uruguayan-source and taxed at 12%. The payer bears the tax, so the base is the net payment plus the withholding (T8 art. 13).

- **With the Spanish residence certificate:** the treaty caps the tax at 10% (art. 12(2)(b), not a copyright on a literary, artistic or scientific work). Base 900,000 / 0.90 = UYU 1,000,000; IRNR UYU 100,000.
- **Without it:** 12%. Base 900,000 / 0.88 = UYU 1,022,727.27; IRNR UYU 122,727.27.

Getting the certificate before payment saves the SA UYU 22,727.27 on this payment. The SA withholds, issues a resguardo and declares the withholding on form 1246.

```oa-check
name: Royalty to a Spanish company, UYU 900,000 net, treaty and domestic rate
inputs:
  net: 900000
  treaty_rate: 0.10
  domestic_rate: 0.12
steps:
  - base_treaty: net / (1 - treaty_rate)
  - irnr_treaty: base_treaty * treaty_rate
  - base_domestic: round(net / (1 - domestic_rate), 2)
  - irnr_domestic: base_domestic - net
  - saving: irnr_domestic - irnr_treaty
expected:
  base_treaty: 1000000.00
  irnr_treaty: 100000.00
  base_domestic: 1022727.27
  irnr_domestic: 122727.27
  saving: 22727.27
```

### Example 2: dividend to a Spanish parent, should it claim the treaty

A Uruguayan SA pays a dividend of UYU 2,000,000 out of profits taxed in IRAE to its Spanish shareholder company, which holds 80% of its capital directly. Should the parent claim the treaty, and does the size of its holding matter?

Domestic law: 7% IRNR (T8 art. 18 B) = UYU 140,000. Treaty (art. 10(2)): 5% for a beneficial owner resident in Spain, and exempt where a company holds directly at least 75% of the payer.

- **80% holding, certificate given:** exempt, IRNR 0. Saving UYU 140,000.
- **If it held 60%:** 5% = UYU 100,000. Saving UYU 40,000.
- **No certificate:** 7% = UYU 140,000.

The decision: with at least 75% held directly, claiming the treaty removes the tax; below 75% it still cuts it from 7% to 5%. Either way the Spanish parent should give the residence certificate before the dividend is paid. Had the dividend come from profits not taxed in IRAE, it would be exempt in domestic law (T8 art. 19 C) and the treaty would not matter.

```oa-check
name: Dividend UYU 2,000,000 to a Spanish parent, 80% and 60% holdings
inputs:
  dividend: 2000000
  domestic_rate: 0.07
  treaty_rate: 0.05
steps:
  - irnr_domestic: dividend * domestic_rate
  - irnr_80: dividend * 0
  - irnr_60: dividend * treaty_rate
  - saving_80: irnr_domestic - irnr_80
  - saving_60: irnr_domestic - irnr_60
expected:
  irnr_domestic: 140000.00
  irnr_80: 0.00
  irnr_60: 100000.00
  saving_80: 140000.00
  saving_60: 40000.00
```

## Ask the client first

1. The recipient: country of residence, individual or entity, whether it is in a low or no-tax jurisdiction or regime, and whether it has an office, staff or agent in Uruguay (a possible permanent establishment).
2. The payment: what it is for (services, royalties, interest, dividends, rent, sale of shares or property), where the work is done, and whether the price is gross or net of Uruguayan tax.
3. The payer: is it an IRAE taxpayer, a public body or another withholding agent?
4. For dividends: whether the profits were taxed in IRAE, the shareholding and how long it has been held, and whether the shares are listed.
5. Treaty: which treaty, whether it applies from the payment date, and whether the recipient can give a certificate of tax residence.
6. Has the recipient a DGI registration number and a resident representative where one is needed?

## Sources

| Source | URL | Read on |
|---|---|---|
| Texto Ordenado 2023, Título 8 IRNR, IMPO consolidated text with Ley 20.446 integrated: arts. 1 to 20 read in full | https://www.impo.com.uy/bases/todgi-2023/8-2024 | 2026-11-11 |
| Decreto 149/007, IMPO consolidated text: arts. 8 to 11 BIS, 26 to 44 read (low-tax test, withholding agents and rates, fictitious dividends, obligations of agents) | https://www.impo.com.uy/bases/decretos/149-2007 | 2026-11-11 |
| DGI, Estado de los Convenios para evitar la Doble Imposición (table of 25 April 2024), full table read | https://www.gub.uy/direccion-general-impositiva/comunicacion/publicaciones/convenios-para-evitar-doble-imposicion | 2026-11-11 |
| Ley 18.730, treaty with Spain, IMPO text: arts. 10 to 12 read | https://www.impo.com.uy/bases/leyes-internacional/18730-2011 | 2026-11-11 |
| DGI, list of forms in the ßeta application, read for form 1246 (IRNR withholding returns, migrated to SIGMA) | https://www.gub.uy/direccion-general-impositiva/sites/direccion-general-impositiva/files/2023-11/Formularios%2Bincluidos%2Ben%2BBeta.pdf | 2026-11-11 |

Not yet confirmed: the IRNR rate on foreign-currency interest over one and up to three years (blank in the consolidated text); the DGI list of low or no-tax jurisdictions; the monthly due dates for paying IRNR withholdings and the lines of form 1246; the form and certificate DGI requires to apply a treaty rate at source outside fictitious dividends; the rules of the Programa de Fomento para la Atracción de Personas con Talento Calificado; whether any treaty entered into force after the DGI table of April 2024; the rates in the other 24 treaties.

> Contributed by OpenAccountants.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `uy-cross-border` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/uy-cross-border. If neither is available, confirm every figure against the official source pages cited above before relying on it.
