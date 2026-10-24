---
name: at-cross-border
description: "Use this skill for Austrian tax when a person or company crosses the Austrian border. Covers unlimited and limited tax liability for individuals (home, habitual abode, the six-month rule, the 70-day second-home rule) and for companies (seat or place of management); the inbound Zuzugsbegünstigung for researchers (30% allowance for five years); the exit tax on leaving (Wegzugsbesteuerung) with deferral or instalments for EU/EEA moves; non-residents with Austrian employment, rental or capital income and the add-on of EUR 11,077; withholding on outbound payments (KESt 27.5% and 25%, the § 99 EStG withholding of 20%); treaty relief and the refund route; tax year 2026 (calendar year). Trigger phrases: moving to Austria, leaving Austria, non-resident Austria, expat, exit tax, Wegzug, Zuzug, digital nomad, beschränkte Steuerpflicht. Out of scope: the full tariff and E 1 return (at-income-tax), corporate tax (at-corporate-income-tax), SVS contributions (at-svs-contributions), VAT (at-vat-return"
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/at-cross-border"
  jurisdiction: "AT"
  tax_year: "2026"
  last_updated: "2026-10-23"
  authored_by: "Ryan Duguid"
  trust_label: "Accountant-authored"
  review_status: "pending_review"
---

# Austria cross-border tax: arriving, leaving, non-residents and withholding (2026)

This skill is the hub for cross-border questions in the Austria pack. It says who Austria taxes and on what, what changes on arrival and on departure, and what a payer must withhold when money leaves Austria. It links to the other Austria skills for the detail: `at-income-tax` (tariff, credits, the E 1 return), `at-corporate-income-tax` (corporate rate, participation exemption, dividend withholding to companies), `at-svs-contributions` (social insurance of the self-employed) and `at-tax-overview`.

All figures are for the 2026 calendar year unless a row says otherwise. Statute text was read on RIS (the federal legal information system) on 22 October 2026.

## Who this applies to

**Individuals.** Austria has two kinds of income tax liability (EStG § 1).

- **Unlimited liability (worldwide income).** A person has unlimited liability if they have a home (Wohnsitz) or their habitual abode (gewöhnlicher Aufenthalt) in Austria (EStG § 1(2)).
- **Home.** A person has a home where they hold a dwelling in circumstances that show they will keep and use it (BAO § 26(1)). Citizenship does not decide it.
- **Habitual abode and the six-month rule.** A person has a habitual abode where they stay in circumstances showing the stay is not just temporary. A stay in Austria of more than six months always creates unlimited liability, and the liability then also covers the first six months (BAO § 26(2)).
- **Second homes of people living abroad.** If a person's centre of vital interests has been abroad for more than five calendar years, an Austrian dwelling counts as a home only in years when it (alone or with other Austrian dwellings) is used on more than 70 days. This applies only if the person keeps a record of the days of use (Zweitwohnsitzverordnung § 1(1) and (2)). The rule first applies in the calendar year after the centre of vital interests moves abroad, and last applies in the year before it moves back (§ 2). A dwelling of a spouse or partner who has unlimited liability and not permanently separated always counts as a home (§ 3).
- **Limited liability (Austrian income only).** A person with neither a home nor a habitual abode in Austria is taxed only on the Austrian income listed in EStG § 98 (EStG § 1(3)).
- **Option for EU/EEA nationals.** A national of an EU or EEA state without a home or habitual abode in Austria can apply to be treated as having unlimited liability if at least 90% of their income is subject to Austrian tax, or their income not subject to Austrian tax is not more than EUR 13,539 (2026). Proof is a certificate from the foreign tax authority (EStG § 1(4)). The claim is made on form L 1i with the E 1 or L 1 return (BMF, E 7 guide for 2025).
- **Part-year.** There is no separate split-year statute. Liability follows the facts: unlimited from the day a home is set up or the habitual abode begins, limited after it ends. For the year of arrival or departure, refer the tariff mechanics (foreign income in the progression) to `at-income-tax`.

**Companies.** A company has unlimited liability (worldwide income) if it has its place of management (Geschäftsleitung) or its registered seat (Sitz) in Austria. A company with neither has limited liability on the Austrian income in KStG § 21(1) (KStG § 1(2) and (3)).

## Rates, bands and thresholds

| Item | Amount | Tax year | Source |
|---|---|---|---|
| Income tax tariff, 0% band | up to EUR 13,539 | 2026 | https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004570&Paragraf=33 |
| 20% band | EUR 13,539 to 21,992 | 2026 | same |
| 30% band | EUR 21,992 to 36,458 | 2026 | same |
| 40% band | EUR 36,458 to 70,365 | 2026 | same |
| 48% band | EUR 70,365 to 104,859 | 2026 | same |
| 50% band | EUR 104,859 to 1,000,000 | 2026 | same |
| 55% on income above EUR 1,000,000 | 55% | 2016 to 2029 | same |
| Non-resident add-on: amount added to income before the tariff is applied | EUR 11,077 | 2026 (EUR 11,329 announced for 2027) | https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004570&Paragraf=102 |
| EU/EEA option: non-Austrian income cap | EUR 13,539 | 2026 (EUR 13,846 for 2027) | https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004570&Paragraf=1 |
| Zuzugsfreibetrag for researchers and scientists | 30% of scientific income taxed at the tariff, for 5 years from arrival | 2026 | https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004570&Paragraf=103 |
| Zuzugsbegünstigung (removal of extra burden), flat average rate floor | not below 15% | 2026 | same |
| Capital income special rate (dividends, gains on shares, most other capital income) | 27.5% | 2026 | https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004570&Paragraf=27a |
| Capital income special rate on bank deposits and current accounts | 25% | 2026 | same |
| Exit tax on private shares and other capital assets (gain treated as a sale) | 27.5% (special rate above) | 2026 | https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004570&Paragraf=27 |
| Exit tax instalments (business assets, EU/EEA moves): fixed assets | 5 equal yearly instalments | 2026 | https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004570&Paragraf=6 |
| Exit tax instalments (business assets, EU/EEA moves): current assets | 2 equal yearly instalments | 2026 | same |
| § 99 EStG withholding, gross (artists, authors, sportspeople, royalties, board fees, consulting, labour hire) | 20% | 2026 | https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004570&Paragraf=100 |
| § 99 EStG withholding on income under § 99(1) no. 6 (property income of non-public real estate funds) and no. 7 (silent partnerships) | 27.5% | 2026 | same |
| § 99 EStG net taxation (EU/EEA recipients): up to EUR 20,000 a year / above | 20% / 25% | 2026 | same |
| § 99 EStG net taxation where the recipient is a company; a company may also have 23% withheld on § 99(1) no. 6 and 7 income | 23% (from 2024) | 2026 | same |
| Refund example in BMF guidance: treaty rate on dividends to an individual | 15% (refund of 12.5 points of the 27.5%) | 2026 | https://www.bmf.gv.at/themen/steuern/internationales-steuerrecht/rueckerstattung/rueckerstattung-oesterreichischer-abzugsteuer.html |

The tariff bands and the amounts in EStG §§ 1(4) and 102(3) are indexed every year (EStG § 33(1a)). Never reuse one year's figures for another. The 2025 add-on was EUR 10,888 and the 2025 EU/EEA cap EUR 13,308 (BMF, E 7 guide for 2025).

## The taxable base

**Unlimited liability: worldwide income.** A resident is taxed on all Austrian and foreign income (EStG § 1(2)). There is no remittance basis and no non-dom regime. Treaties then decide which state may tax each item (see Cross-border points).

**Limited liability: Austrian income only.** EStG § 98(1) lists what a non-resident is taxed on. The main items:

- employment exercised or used in Austria, or paid from Austrian public funds (§ 98(1) no. 4);
- business income from an Austrian permanent establishment, a permanent representative or Austrian real property; also consulting, labour hire and performances in Austria even with no permanent establishment (§ 98(1) no. 3);
- rental income from property located in Austria or entered in an Austrian register (§ 98(1) no. 6);
- gains on private sales of Austrian real property (§ 98(1) no. 7);
- capital income such as Austrian dividends where KESt was to be withheld (§ 98(1) no. 5). For bank interest: a non-resident individual living in a state that has automatic exchange of information with Austria has no limited liability on Austrian savings interest. If KESt was withheld anyway, it is refunded on application (BMF, refund page, ZISP example).

**How a non-resident's tariff tax is worked out.** Expenses are deductible only if economically linked to the Austrian income (EStG § 102(2) no. 1). For income that is assessed, EUR 11,077 is added to the income and the tariff is applied to the total (EStG § 102(3); BMF E 7 guide: "das Einkommen wird um diesen Betrag erhöht und davon die Steuer bemessen"). Illustration for 2026: Austrian rental income of EUR 20,000 is taxed as if income were EUR 31,077. That gives EUR 8,453 at 20% (EUR 1,690.60) plus EUR 9,085 at 30% (EUR 2,725.50), so EUR 4,416.10 before any credits.

**Inbound regime: Zuzugsbegünstigung (EStG § 103, Zuzugsbegünstigungsverordnung 2016).**

- *Zuzugsfreibetrag (§ 103(1a)).* For a person whose move from abroad serves science or research in the public interest, the Finanzamt Österreich can grant an allowance of 30% of the income from scientific activity taxed at the tariff, for five years from arrival. If granted, no other moving-related expenses can be deducted.
- *Removal of extra burden (§ 103(1)).* For moves serving science, research, art or sport, the Finanzamt can remove the extra tax caused by becoming resident on income not covered by § 98, for example by applying a flat average rate based on the burden before the move. That rate cannot be below 15% (§ 103(3)).
- *Gap rule.* A person who moved their centre of vital interests out of Austria qualifies again only after more than ten years abroad, or more than five years for the 30% allowance (§ 103(2)).
- *Who qualifies.* The regulation sets the conditions: mainly scientific activity, in Austria's public interest, documented high qualification (Zuzugsbegünstigungsverordnung 2016 § 2(1)). Some cases count in any event, such as a university professor appointment under § 94(2) no. 1 UG, or work at a listed research institution with pay at least the EU Blue Card gross salary (§ 2(2)).

**Exit tax: individuals (Wegzugsbesteuerung, EStG § 27(6) no. 1).** Any event that restricts Austria's right to tax a capital asset, a derivative or a cryptocurrency counts as a sale. The typical event is moving abroad so that a treaty gives the new state the right to tax the gain. The gain is the fair value less acquisition cost, taxed at 27.5%.

- *Move to an EU/EEA state:* on application, the tax is assessed in the notice but not collected until the asset is actually sold (lit. a). A later move to a third country, or breach of the proof duty, counts as a sale (lit. b). If the deferred gains total more than EUR 100,000 in a year, the person must confirm every year to the Finanzamt, by the end of the following year, that no triggering event has happened (lit. f).
- *Other cases:* § 6 Z 6 lit. c and d apply by reference (lit. d). Instalments under § 6 Z 6 lit. c exist only for EU/EEA cases, so a move to a third country is taxed in full.
- *Arrival:* when Austria gains the right to tax an asset, its fair value becomes the acquisition cost (lit. e).

**Exit tax: business assets and companies (EStG § 6 Z 6; KStG § 7(2) applies the EStG).** Moving assets, a business or a permanent establishment abroad, or any other restriction of Austria's taxing right, is valued at arm's length (lit. a and b). For EU/EEA cases, on application, the tax is paid in instalments: fixed assets over five years, current assets over two years. The first instalment is due one month after the assessment notice, later ones on 30 June of each following year (lit. c to e). Open instalments fall due at once if the assets are sold or moved outside the EU/EEA, if a company's place of management moves outside the EU/EEA, on insolvency, or if an instalment is more than 12 months late. These events must be reported within three months (lit. d).

## Deadlines and filing

| What | Deadline | Source |
|---|---|---|
| Register a new address (Anmeldung) with the registration office | within 3 days after moving in | MeldeG § 3(1) |
| Deregister (Abmeldung) when giving up the dwelling | within 3 days before or after | MeldeG § 4(1) |
| Zuzugsbegünstigung or Zuzugsfreibetrag application to the Finanzamt Österreich | at the latest 6 months after arrival | Zuzugsbegünstigungsverordnung 2016 § 1(2) |
| Income tax return (E 1, or E 7 for non-residents), including the year of arrival or departure and any exit tax | 30 April of the following year on paper, 30 June if filed electronically | BAO § 134(1); BMF E 7 guide |
| Non-resident application to be assessed on wage income or § 99 income | within 5 years after the end of the year | EStG § 102(1) no. 3 |
| Exit tax proof duty (deferred gains above EUR 100,000) | every year, by the end of the following year | EStG § 27(6) no. 1 lit. f |
| Exit tax instalments (EU/EEA business assets) | first: 1 month after the notice; then 30 June each year | EStG § 6 Z 6 lit. d and e |
| § 99 withholding paid over by the Austrian payer | 15th day after the end of the month of withholding | EStG § 101(1) |
| Refund of Austrian withholding tax for non-residents | only after the end of the year of withholding; by the end of the fifth calendar year after that year | BAO § 240a(1) (BMF refund page); BAO § 240(3) (tax withheld wrongly) and § 240(4) (refund under a treaty) |

**Refund route.** Since 1 January 2019 a non-resident must first file an electronic pre-notification (Vorausmeldung) through the BMF web form. The applicant prints it, signs it, has the foreign tax authority confirm residence on it, and posts it to the Finanzamt für Großbetriebe. Fax is not accepted. Each income type needs its own application, for example DIAG for dividends and ZISP for savings interest. The first application gives the applicant an ABZ number to quote in all later ones (BMF refund page). Relief at source instead of refund, and the dividend rules for companies, are in `at-corporate-income-tax`.

## Penalties and interest

| What | Figure | Source |
|---|---|---|
| Late filing surcharge (Verspätungszuschlag), if the delay is not excusable | up to 10% of the tax assessed; not set below EUR 50 | BAO § 135 |
| First late-payment surcharge (Säumniszuschlag) | 2% of the tax not paid by the due date | BAO § 217(2) |
| Second and third late-payment surcharges | 1% each, if still unpaid 3 months after enforceability and 3 months after that | BAO § 217(3) |
| Interest on income tax and corporate tax differences (Anspruchszinsen) | 2% above the base rate a year, from 1 October of the following year, for at most 48 months; not set below EUR 50 | BAO § 205(1) and (2) |
| Anspruchszinsen rate from 16 September 2026 | 4.03% (base rate 2.03%); 3.53% from 11 June 2025 to 15 September 2026 | BMF-AV Nr. 171/2026 |

Anspruchszinsen do not apply to deferred exit tax or exit tax instalments (EStG § 27(6) no. 1 lit. c; § 6 Z 6 lit. d). The payer of § 99 income is liable for tax it fails to withhold (EStG § 100(2)).

## Cross-border points

**Treaties.** Where a person is resident in Austria under domestic law and also in another state, the treaty's residence article decides where they are resident for the treaty. The treaty then says which state may tax each income type and whether the residence state exempts or credits. Read the specific treaty on the BMF treaty list; do not assume a method. A treaty partner's withholding at source is relieved at source with an Austrian residence certificate (form ZS-A) or refunded under that state's procedure (BMF, DBA general page). Austria and Switzerland signed an amending protocol on 30 July 2026; its entry into force is not confirmed here.

**Social security (EU/EEA).** Under Regulation (EC) No 883/2004 a person is insured in one state at a time. An employee posted from Austria to another EU/EEA state stays under Austrian social insurance if the posting is expected to last no more than 24 months, the person was under Austrian law for one month before, is not replacing another posted person, and the employer has substantial activity in Austria. The worker carries the A1 certificate issued by the sending state's insurer. After 24 months, an extension to at most five years needs an exception agreement between the authorities (USP, posting to EU/EEA states, updated 27 July 2026). Self-employed contributions: `at-svs-contributions`.

**Pointers.** Wage tax for employees in Austria and the employer's payroll duties are not yet covered in this pack. Dividend withholding to companies, the participation exemption and the parent-subsidiary exemption: `at-corporate-income-tax`. Credits, the full return and foreign income in the progression: `at-income-tax`.

## Worked examples

### Example 1: researcher moving to Vienna in 2026 with the Zuzugsfreibetrag

A researcher moves from abroad in January 2026 to a professorship at an Austrian university and applies within six months. The Finanzamt grants the 30% Zuzugsfreibetrag. Their only income is EUR 90,000 from scientific activity, taxed at the tariff (after social insurance and expenses). The allowance is deducted from that income before the tariff is applied (§ 103(1a)). Fixed credits such as the Verkehrsabsetzbetrag reduce the tax by the same amount with or without the allowance, so they are left out of both figures and the saving is unchanged.

1. Allowance: 30% of EUR 90,000 = EUR 27,000. Taxable income EUR 63,000.
2. Tariff 2026 on EUR 63,000: EUR 8,453 at 20% = EUR 1,690.60; EUR 14,466 at 30% = EUR 4,339.80; EUR 26,542 at 40% = EUR 10,616.80. Total EUR 16,647.20.
3. Without the allowance, tariff tax on EUR 90,000 is EUR 29,018.00. The allowance saves EUR 12,370.80 a year, for five years.

```oa-check
name: Researcher, Zuzugsfreibetrag 30%, scientific income EUR 90,000 (2026 tariff)
inputs:
  income: 90000
steps:
  - allowance: income * 0.30
  - taxable: income - allowance
  - b20: (min(taxable, 21992) - 13539) * 0.20
  - b30: (min(taxable, 36458) - 21992) * 0.30
  - b40: (min(taxable, 70365) - 36458) * 0.40
  - tax_with: b20 + b30 + b40
  - n20: (21992 - 13539) * 0.20
  - n30: (36458 - 21992) * 0.30
  - n40: (70365 - 36458) * 0.40
  - n48: (income - 70365) * 0.48
  - tax_without: n20 + n30 + n40 + n48
  - saving: tax_without - tax_with
expected:
  allowance: 27000.00
  taxable: 63000.00
  tax_with: 16647.20
  tax_without: 29018.00
  saving: 12370.80
```

### Example 2: leaving Austria for the United Kingdom with shares in a GmbH

An Austrian resident moves permanently to London on 1 March 2026 and gives up the Austrian home. They privately hold 20% of an Austrian GmbH, bought for EUR 40,000 and worth EUR 240,000 on the day of departure. The UK is not an EU/EEA state.

1. Under the Austria-UK treaty, gains on shares are taxable only in the seller's state of residence (Art. 13(5)), unless more than 50% of the company's value comes from Austrian real property (Art. 13(2)). This GmbH is not property-rich, so the move restricts Austria's right to tax the gain and counts as a sale (EStG § 27(6) no. 1).
2. Gain: EUR 240,000 less EUR 40,000 = EUR 200,000.
3. Tax at the 27.5% special rate: EUR 55,000.
4. No deferral and no instalments: § 27(6) no. 1 lit. a and § 6 Z 6 lit. c name only EU/EEA states, and there is no route for a third country with a mutual assistance agreement. The UK has been a third country since Brexit. The EUR 55,000 is assessed with the 2026 return and paid on the notice. If it is paid late, the first late-payment surcharge is 2%, EUR 1,100.
5. Had the person moved to Germany instead, they could apply for the tax to be assessed but not collected until a sale. Because the deferred gain exceeds EUR 100,000, they would have to confirm every year that no sale or further move has happened.

```oa-check
name: Exit to the UK, private GmbH shares, gain EUR 200,000 (2026)
inputs:
  fair_value: 240000
  cost: 40000
steps:
  - gain: fair_value - cost
  - exit_tax: gain * 0.275
  - first_late_surcharge: exit_tax * 0.02
expected:
  gain: 200000.00
  exit_tax: 55000.00
  first_late_surcharge: 1100.00
```

## Ask the client first

1. Where is your home now, and will you keep a dwelling in Austria? If you keep one, how many days a year will you use it, and for how many years has your life centred abroad?
2. Exact arrival or departure date, and the country you are moving from or to (EU/EEA or not).
3. Do you hold shares, fund units, crypto or business assets, and what did they cost? (Exit tax and the fair value on arrival.)
4. Is the move for research, science, art or sport, and who is the employer? (Zuzugsbegünstigung, applied for within six months.)
5. What Austrian income will you have after leaving: salary, rent, dividends, fees? Are you an EU/EEA national with 90% or more of your income from Austria?
6. For an employee: is this a posting from an employer abroad, and for how long? (A1 certificate and payroll.)

## Sources

All read on 2026-10-22.

- EStG 1988 § 1 (tax liability; EU/EEA option): https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004570&Paragraf=1
- EStG § 6 (Z 6, exit for business assets, instalments): https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004570&Paragraf=6
- EStG § 27 (para. 6 no. 1, exit tax on capital assets): https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004570&Paragraf=27
- EStG § 27a (27.5% and 25% special rates): https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004570&Paragraf=27a
- EStG § 33 (2026 tariff, indexation): https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004570&Paragraf=33
- EStG § 98 (income of non-residents): https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004570&Paragraf=98
- EStG § 99 (withholding cases): https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004570&Paragraf=99
- EStG § 100 (withholding rates, liability): https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004570&Paragraf=100
- EStG § 101 (paying over § 99 tax): https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004570&Paragraf=101
- EStG § 102 (assessment of non-residents, EUR 11,077 add-on): https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004570&Paragraf=102
- EStG § 103 (Zuzugsbegünstigung): https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004570&Paragraf=103
- Zuzugsbegünstigungsverordnung 2016: https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20009641
- Zweitwohnsitzverordnung (BGBl. II Nr. 528/2003): https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20003027
- KStG 1988 § 1 (corporate residence): https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004569&Paragraf=1
- KStG § 7 (income determined under the EStG): https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004569&Paragraf=7
- BAO § 26 (home, habitual abode, six months): https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10003940&Paragraf=26
- BAO § 134 (return deadlines): https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10003940&Paragraf=134
- BAO § 135 (late filing surcharge): https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10003940&Paragraf=135
- BAO § 205 (Anspruchszinsen): https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10003940&Paragraf=205
- BAO § 217 (late payment surcharges): https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10003940&Paragraf=217
- BAO § 240 (refund of tax withheld, five-year limit): https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10003940&Paragraf=240
- MeldeG §§ 3 and 4 (registration and deregistration): https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10005799&Paragraf=4
- Austria-UK double tax treaty (BGBl. III Nr. 32/2019), Art. 13: https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20010606
- BMF, refund of Austrian withholding tax: https://www.bmf.gv.at/themen/steuern/internationales-steuerrecht/rueckerstattung/rueckerstattung-oesterreichischer-abzugsteuer.html
- BMF, double tax treaties, general: https://www.bmf.gv.at/themen/steuern/internationales-steuerrecht/doppelbesteuerungsabkommen/dba-allgemeines.html
- BMF, press release on the Austria-Switzerland protocol, 30 July 2026: https://www.bmf.gv.at/presse/pressemeldungen/2026/juli-2026/dba-schweiz.html
- BMF, E 7 guide for 2025 (non-resident return): https://formulare.bmf.gv.at/service/formulare/inter-Steuern/pdfd/2025/E8.pdf
- BMF-AV Nr. 171/2026, interest rates from 16 September 2026 (findok): https://findok.bmf.gv.at/findok/iwg/84/84659/84659.1.pdf
- USP, social insurance when posting to EU/EEA states: https://www.usp.gv.at/themen/mitarbeiter-und-gesundheit/einstellung-mitarbeiter-und-arten-der-beschaeftigung/weitere-informationen-einstellen-von-personal/arbeiten-im-ausland/entsendung-in-eu-ewr-staaten-aus-oesterreich/sozialversicherung--entsendung-.html

Not yet confirmed: the text of Regulation (EC) No 883/2004 itself (EUR-Lex blocked the fetch; the posting rules above come from the USP page); the E 7 guide for 2026 (only the 2025 guide was published at the fetch); the current KESt rate that § 93(1a) EStG lets a payer withhold for a corporate recipient (see `at-corporate-income-tax`); a statutory split-year rule (none found); the entry into force of the 2026 Austria-Switzerland protocol; any named form for the Zuzugsbegünstigung application.

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

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-10-23. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `at-cross-border` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/at-cross-border. If neither is available, confirm every figure against the official source pages cited above before relying on it.
