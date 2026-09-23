---
name: at-corporate-income-tax
description: "Source-cited draft: corporate income tax for Austria (tax year 2025) — rates, thresholds and rules with primary-source citations. Unverified; pending local-accountant review."
jurisdiction: AT
tax_year: 2026
last_updated: 2026-09-22
review_status: pending_review
drafted_by: OpenAccountants
approved_by: pending
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Austria Corporate Income Tax

How Austria taxes companies: the corporate income tax (Körperschaftsteuer, KöSt) on a GmbH, an AG and other bodies, the minimum tax, prepayments, the annual return, losses, group taxation, the participation exemption and the withholding taxes a company deals with when it pays dividends or royalties. It is for companies with their seat or management in Austria and for foreign companies with Austrian income. Figures are for tax year 2026. Most figures come from the business service portal (USP) pages, all dated 1 January 2026. The loss carryforward limit is read from the ministry's K 1 return form for 2025, the latest one published. The group taxation threshold is read from the ministry's group taxation decree of 2005, and the international participation conditions from a 2011 appeals decision on the 2002 tax year, which quotes the law then in force: see the notes under those tables.

## Corporate income tax (Körperschaftsteuer)

### Who pays

- **Unlimited liability.** A body with its seat (Sitz) or its place of management (Ort der Geschäftsleitung) in Austria is taxed on its worldwide income. One of the two is enough. The place of management is where the decisions that run the business are taken. Double tax treaties and national measures can limit Austrian tax on foreign income.
- **Limited liability.** A foreign company with neither seat nor management in Austria is taxed only on certain Austrian income. Public-law bodies and exempt bodies (for example charities) are also limited taxpayers, while a public body's commercial operations (Betriebe gewerblicher Art) are taxed in full.
- **Who counts as a body.** Private-law legal persons such as the AG, GmbH, cooperatives, associations and foundations, and public-law legal persons. A partnership (OG, KG) is not a KöSt taxpayer: its partners pay income tax (see `at-income-tax`).
- **Income of a company.** Income is worked out under the income tax rules, and for a company (Kapitalgesellschaft) all income counts as business income.
- **Exemptions.** Among others: charitable, benevolent and church bodies under conditions, limited-profit housing associations for their exempt business, and certain non-profit credit institutions and pension funds (partly).

**Liability and exemptions**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.usp.gv.at/themen/steuern-finanzen/koerperschaftsteuer-ueberblick/koerperschaftsteuerpflicht.html |
| Seat or management in Austria gives unlimited liability | Worldwide income | "reicht es aus, dass entweder der Sitz oder die Geschäftsleitung im Inland ist" |
| No seat and no management in Austria | Certain Austrian income only | "Die beschränkte Steuerpflicht erstreckt sich nur auf bestimmte inländische Einkünfte." |

### Rate

KöSt is a flat rate on taxable income, whatever the amount, and it is the same whether profits are kept or paid out.

**Corporate income tax rate and dividend tax**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.usp.gv.at/themen/steuern-finanzen/koerperschaftsteuer-ueberblick.html |
| KöSt rate from 2024, flat | 23% | "Die Körperschaftsteuer beträgt 23 Prozent  (bis zum Jahr 2022: 25 Prozent, im Jahr 2023: 24 Prozent)" |
| Capital gains tax (KESt) on a profit distribution to shareholders who are individuals | 27.5% | "mit der Kapitalertragsteuer (das sind 27,5 Prozent) belastet" |

The KESt settles the shareholder's income tax unless the shareholder opts for the regular assessment (Regelbesteuerungsoption), in which case the dividend is taxed at the progressive rates.

### Minimum corporate tax (Mindestkörperschaftsteuer)

A company with share capital (Kapitalgesellschaft, such as a GmbH or AG) with unlimited liability, and a comparable foreign body with unlimited liability, pays a minimum tax every year, in profit and in loss. In the year it starts or ends, only the full calendar quarters of unlimited liability count. The minimum is a YEARLY amount, paid in quarterly instalments. It is not lost: it is credited like a prepayment in later years, but only against the part of a later year's KöSt that exceeds that year's minimum. If the legal form changes during a quarter, the form at the start of the quarter counts.

**Minimum tax per calendar year**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.usp.gv.at/themen/steuern-finanzen/koerperschaftsteuer-ueberblick/koerperschaftsteuerpflicht.html |
| Minimum tax rate, of the legal minimum share capital, per calendar year | 5% | "Sie beträgt pro Kalenderjahr 5 Prozent des gesetzlichen Mindestgrund- bzw. Mindeststammkapitals  und ist vierteljährlich zu entrichten." |
| Legal minimum share capital of a GmbH | EUR 10,000 | "Das Mindeststammkapital von GmbHs (Gesellschaften mit beschränkter Haftung) beträgt 10.000 Euro." |
| Minimum tax of a GmbH, per year | EUR 500 | "insgesamt somit 500 Euro" |
| Legal minimum share capital of an AG | EUR 70,000 | "Das Mindestgrundkapital einer Aktiengesellschaft (AG) beträgt 70.000 Euro." |
| Minimum tax of an AG, per year | EUR 3,500 | "Die davon kalendervierteljährlich zu entrichtende Mindeststeuer in Höhe von 5 Prozent beträgt somit 3.500 Euro." |

The AG sentence says "kalendervierteljährlich" but the amount is the yearly rate applied to the whole minimum capital, so it is a yearly amount paid in quarterly parts, like the GmbH figure. The overview page says the same thing another way: the minimum tax is five percent of a quarter of the minimum capital for each full calendar quarter. The pages print no quarterly amount, so this Guide states none.

### Prepayments and assessment

KöSt is assessed and paid like income tax. Prepayments are set by a notice from the tax office. After the assessment notice, any balance due is payable within one month.

**Prepayment dates**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.usp.gv.at/themen/steuern-finanzen/koerperschaftsteuer-ueberblick.html |
| Prepayments due | 15 February, 15 May, 15 August, 15 November | "zu folgenden Terminen fällig werden: 15. Februar, 15. Mai, 15. August und 15. November" |
| Balance after the assessment notice | Within one month | "ist ein Zahlungsziel von einem Monat vorgesehen" |

### The annual return (Körperschaftsteuererklärung)

The company files a return for the past calendar year, or for its financial year if that differs from the calendar year. It must be filed electronically through FinanzOnline; paper only if electronic filing is unreasonable for lack of technical means. The balance sheet or annual accounts, and any annual or audit reports, are attached (e-Bilanz or on paper). Filing costs nothing. Against the assessment notice, an appeal (Beschwerde) is possible within one month of delivery.

**Return deadlines, forms and tax office**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.usp.gv.at/themen/steuern-finanzen/koerperschaftsteuer-ueberblick/koerperschaftsteuererklaerung.html |
| Return due, on paper | 30 April of the following year | "bis 30. April des Folgejahres" |
| Return due, electronically via FinanzOnline | 30 June of the following year | "bei elektronischer Übermittlung über Finanz Online bis 30. Juni des Folgejahres" |
| Extension | On a reasoned request; a represented company usually has longer | "Wenn ein Unternehmen von einer steuerlichen Vertreterin/einem steuerlichen Vertreter vertreten wird, hat es für die Einreichung der Steuererklärung in der Regel länger Zeit." |
| Large business tax office (Finanzamt für Großbetriebe): turnover in each of the last two years above | EUR 10 million | "jeweils mehr als 10 Mio. Euro überschritten haben" |
| Form K 1 | Unlimited taxpayers that must keep accounts (GmbH, AG) | "Formular K1 für unbeschränkt steuerpflichtige, rechnungslegungspflichtige Körperschaften" |
| Form K 2 | Unlimited taxpayers not under § 7(3) KStG, such as certain associations | "Formular K2" |
| Form K 3 | Limited taxpayers, such as foreign companies with Austrian income | "Formular K3 für beschränkt Steuerpflichtige" |

Every other company falls under the Finanzamt Österreich.

### Losses

A business loss that cannot be offset in the year it arises is carried forward and deducted in later years (Verlustabzug), with no time limit, if it was worked out from proper books. For a company the carried-forward loss is deducted only up to a share of the total income of the year; the rest waits for later years.

**Loss carryforward limit**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://formulare.bmf.gv.at/service/formulare/inter-Steuern/pdfs/2025/K1.pdf?open=download |
| Share of the total income against which carried-forward losses can be deducted | 75% | "nur im Ausmaß von 75% des Gesamtbetrages der Einkünfte abzugsfähig". K 1 form for 2025, version of 20 October 2025, note to § 8(4) no. 2 KStG |

The form says the limit does not apply to the extent the total income contains the gains listed in § 8(4) KStG. The general loss rules (no time limit, proper books) are on the USP loss page: https://www.usp.gv.at/themen/steuern-finanzen/einkommensteuer-ueberblick/weitere-informationen-est/moeglichkeiten-zur-verlustverwertung.html

### Group taxation (Gruppenbesteuerung)

Companies linked by a large enough holding can form a tax group (Unternehmensgruppe) under § 9 KStG. The results of the group members are added to the group parent (Gruppenträger). The group is set up by an application to the tax office on form G 4, describing the financial link from the top level down: https://formulare.bmf.gv.at/service/formulare/inter-Steuern/pdfs/9999/G4.pdf?open=inline

**Group taxation threshold**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://findok.bmf.gv.at/findok/resources/pdf/d496d1e6-a12f-4229-9fe8-dab5e8063f9d/14269.1.1.5.pdf |
| Financial link needed, in nominal capital AND in voting rights | more than 50% | "finanzielle Verbindung von mehr als 50% am Nennkapital und an den Stimmrechten voraus". Group taxation decree of the ministry, 2005 |

The decree also says the link must exist for the whole financial year of each member, and that a foreign member may be linked in that way only to an Austrian group member with unlimited liability or to the group parent. It dates from 2005; later changes to § 9 KStG are not reflected in it (see "For the accountant" at the end).

### Participation exemption (Beteiligungsertragsbefreiung)

- **Domestic dividends.** § 10(1) no. 1 to 4 KStG exempts profit shares from Austrian companies and cooperatives received by a company. The K 1 form notes name no minimum holding for these.
- **Foreign dividends outside an international participation.** Exempt under § 10(1) no. 5 and 6 KStG if the foreign company either meets the conditions of Annex 2 to the EStG, or is comparable to an Austrian company under § 7(3) KStG and its state of residence has comprehensive administrative assistance with Austria.
- **International participation (internationale Schachtelbeteiligung).** § 10(1) no. 7 and § 10(3) KStG exempt dividends, and gains, losses and other value changes, from a qualifying holding in a foreign company. The appeals decision linked below (22 June 2011, on the 2002 tax year) quotes the law as a holding "während eines ununterbrochenen Zeitraumes von mindestens einem Jahr mindestens zu einem Zehntel": at least one tenth, held without a break for at least one year. A company can opt in the return for the year of acquisition to make value changes taxable (§ 10(3) KStG, annex K 10).
- **Switch-over and anti-abuse rules.** § 10a KStG can replace the exemption with a credit of foreign tax; the K 1 form carries annex K 12 for this.

Where each item goes in the return: https://formulare.bmf.gv.at/service/formulare/inter-Steuern/pdfs/2025/K1.pdf?open=download (codes 9297, 9298, 9313 and 9314). The appeals decision quoting the holding conditions: https://findok.bmf.gv.at/findok/resources/pdf/aea48cfe-b74b-4e31-bd43-42d39052a2df/54102.1.1.1.pdf

### Withholding taxes

**Capital gains tax (KESt) withheld in Austria**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.usp.gv.at/themen/steuern-finanzen/einkommensteuer-ueberblick/weitere-informationen-est/kapitalertragsteueranmeldung.html |
| Special rate for interest on savings and current accounts | 25% | "mit einem besonderen Steuersatz von 25 Prozent (für Zinsen aus Sparbüchern und Girokonten)" |
| Special rate for all other capital income | 27.5% | "einem besonderen Steuersatz von 27,5 Prozent" |

Where the recipient is a company under § 1(1) KStG, § 93(1a) EStG lets the payer withhold a lower rate than the special rate for other capital income. The USP page still prints an older rate for this case, so check the current wording of § 93(1a) EStG before applying it. If a company suffered the higher rate, it can use the regular assessment option to get the difference back.

**Dividends and royalties paid abroad: refund of Austrian withholding tax**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.bmf.gv.at/themen/steuern/internationales-steuerrecht/rueckerstattung/rueckerstattung-oesterreichischer-abzugsteuer.html |
| KESt on dividends from an Austrian AG or GmbH, before treaty relief | 27.5% | "Gewinnanteile unterliegen inländischem Steuersatz iHv 27,5 Prozent" |
| Withholding tax on royalties, gross or net taxation | 20% or 25% | "Einkünfte unterliegen einer Abzugsteuer iHv 20 Prozent oder 25 Prozent (bei Nettobesteuerung)" |

Where a treaty lowers the Austrian rate, the tax is either not withheld (with a residence certificate) or refunded on request. Under certain conditions, § 94 no. 2 EStG exempts profit shares paid to a company that holds at least one tenth of the paying company, directly or indirectly (Mutter-Tochter-Befreiung); the same page covers the refund where tax was withheld anyway. A company resident in an EU or EEA state can also claim a refund of KESt on profit shares under § 21(1) no. 1a KStG, to the extent it cannot credit the tax under a treaty, and must prove that. Royalties between associated EU companies can be relieved under § 99a EStG.

**Withholding tax on payments to foreign businesses (Abzugsteuer, § 99 EStG)**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.usp.gv.at/themen/steuern-finanzen/einkommensteuer-ueberblick/weitere-informationen-est/internationales-steuerrecht/pflichten-bei-inlandsaktivitaeten-auslaendischer-unternehmer.html |
| Gross taxation, general rate (royalties, performers, technical or commercial consulting, hired-out workers) | 20% | "Der Steuersatz beträgt 20 Prozent, bei Einkünften gemäß § 99 Abs 1 Z 6 und 7 EStG 27,5 Prozent" |
| Gross taxation, income under § 99(1) no. 6 and 7 EStG | 27.5% | "bei Einkünften gemäß § 99 Abs 1 Z 6 und 7 EStG 27,5 Prozent" |
| Same income when the foreign recipient is a company subject to Austrian KöSt | 23% | "kann bei Einkünften gemäß § 99 Abs 1 Z 6 und 7 EStG  23 Prozent Abzugsteuer einbehalten werden" |
| Net taxation: rate on income up to EUR 20,000 per calendar year | 20% | "Bei der Nettobesteuerung beträgt der Steuersatz für Einkünfte bis 20.000 Euro pro Kalenderjahr 20 Prozent" |
| Net taxation: rate on the part above EUR 20,000 | 25% | "für den übersteigenden Teil 25 Prozent" |

The two rows for income under § 99(1) no. 6 and 7 EStG do not cover dividends from an Austrian GmbH or AG; for dividends see the table on dividends paid abroad. Net taxation is available only for payments to businesses from an EU or EEA state, only if the directly linked costs were notified in writing with receipts before payment, and the payer may still choose gross taxation.

The Austrian payer withholds, pays over the amounts withheld in a calendar month by the 15th of the following month, and reports them on form E 19. Most treaties give Austria no right to tax royalties; relief is by exemption at source or refund, subject to the formal proof on the USP page.

### Overall burden when profits are paid out

**Tax on distributed profit**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.usp.gv.at/themen/steuern-finanzen/koerperschaftsteuer-ueberblick/weitere-informationen-zur-koerperschaftsteuer/steuerbelastung-im-vergleich-zur-einkommensteuer.html |
| Combined burden of KöSt plus KESt when a one-person GmbH distributes all profit to an individual shareholder | 44.18% | "ergibt sich eine Gesamtsteuerbelastung von insgesamt 44,18 Prozent" |
| Worked example: profit before tax | EUR 40,000 | "Gewinn vor Steuer 40.000 100" |
| KöSt on it | EUR 9,200 | "Körperschaftsteuer (KSt) 9.200 23" |
| KESt on the distribution | EUR 8,470 | "Kapitalertragsteuer (KESt) 8.470 21,2" |
| Shareholder receives | EUR 22,330 | "Gesellschafter erhält 22.330 55,8" |
| Tax borne, KöSt plus KESt together | EUR 17,670 | "Steuerbelastung 17.670 44,2" |

The same page compares this with an income tax bracket, but the bracket limits it quotes are not the 2026 ones. For the 2026 income tax brackets use `at-income-tax`.

## The method, step by step

1. **Confirm the company is a KöSt taxpayer and which kind.** Check seat and place of management under the KStG, and whether an exemption applies, on the USP liability page: https://www.usp.gv.at/themen/steuern-finanzen/koerperschaftsteuer-ueberblick/koerperschaftsteuerpflicht.html
2. **Pay the prepayments set by notice** on the four dates in the prepayment table, and at least the minimum tax in the minimum tax table, even in a loss year: https://www.usp.gv.at/themen/steuern-finanzen/koerperschaftsteuer-ueberblick.html
3. **Work out taxable income** from the accounts under the income tax rules plus the KStG adjustments on form K 1: exempt participation income (§ 10 KStG), non-deductible items (§ 12 KStG), the interest limit (§ 12a KStG) and carried-forward losses up to the limit in the loss table: https://formulare.bmf.gv.at/service/formulare/inter-Steuern/pdfs/2025/K1.pdf?open=download
4. **For a tax group,** file form G 4 with the tax office of the group parent before relying on group results, and check the link in the group table: https://formulare.bmf.gv.at/service/formulare/inter-Steuern/pdfs/9999/G4.pdf?open=inline
5. **File the return** on K 1, K 2 or K 3 through FinanzOnline with the annual accounts attached, by the date in the return table: https://www.usp.gv.at/themen/steuern-finanzen/koerperschaftsteuer-ueberblick/koerperschaftsteuererklaerung.html
6. **Apply the rate** in the rate table, credit prepayments and any unused minimum tax, and pay any balance within one month of the notice.
7. **On any dividend paid,** withhold and file KESt at the special rate for all other capital income in the KESt table (for a company shareholder, see the note on § 93(1a) EStG under that table), or apply the Mutter-Tochter exemption or treaty relief: https://www.usp.gv.at/themen/steuern-finanzen/einkommensteuer-ueberblick/weitere-informationen-est/kapitalertragsteueranmeldung.html
8. **On royalties or other § 99 payments abroad,** withhold at the rates in the withholding table unless relief at source is documented: https://www.usp.gv.at/themen/steuern-finanzen/einkommensteuer-ueberblick/weitere-informationen-est/internationales-steuerrecht/pflichten-bei-inlandsaktivitaeten-auslaendischer-unternehmer.html

## Ask the client first

- Is it a GmbH, an AG or another body, and where are its registered seat and its real management? This decides liability and the minimum tax.
- Is the company part of a group, and does any parent or subsidiary hold more than half of the capital AND the votes? Has a G 4 application been filed?
- Does the company hold shares in other companies, Austrian or foreign, and since when and how much? This decides the participation exemption.
- Does the company have losses carried forward from earlier years, and were they worked out from proper books?
- Does the company pay dividends, royalties, consulting or service fees to anyone abroad?
- Is the company represented by a tax adviser (longer filing time), and does its financial year differ from the calendar year?

## When to refuse or refer

- Group taxation set-up, foreign group members, recapture of foreign losses and exit from a group: refer to a Steuerberater.
- Switch-over under § 10a KStG, controlled foreign company rules and the interest limit under § 12a KStG: refer.
- The minimum tax for very large groups (the global minimum tax) and transfer pricing: outside this Guide.
- Reorganisations (mergers, conversions, contributions under the UmgrStG) and liquidations: refer.
- Charities, associations, public bodies and their commercial operations: outside this Guide beyond the liability summary.
- Treaty claims on a specific payment: read the treaty and refer.
- Company formation, capital and the founding steps: see `at-company-formation`. VAT: see `at-vat-return`. The shareholder's own income tax and social insurance: see `at-income-tax` and `at-svs-contributions`.

## Sources

- USP, Körperschaftsteuer: https://www.usp.gv.at/themen/steuern-finanzen/koerperschaftsteuer-ueberblick.html
- USP, Körperschaftsteuerpflicht: https://www.usp.gv.at/themen/steuern-finanzen/koerperschaftsteuer-ueberblick/koerperschaftsteuerpflicht.html
- USP, Körperschaftsteuererklärung: https://www.usp.gv.at/themen/steuern-finanzen/koerperschaftsteuer-ueberblick/koerperschaftsteuererklaerung.html
- USP, Steuerbelastung im Vergleich zur Einkommensteuer: https://www.usp.gv.at/themen/steuern-finanzen/koerperschaftsteuer-ueberblick/weitere-informationen-zur-koerperschaftsteuer/steuerbelastung-im-vergleich-zur-einkommensteuer.html
- USP, Möglichkeiten zur Verlustverwertung: https://www.usp.gv.at/themen/steuern-finanzen/einkommensteuer-ueberblick/weitere-informationen-est/moeglichkeiten-zur-verlustverwertung.html
- USP, Kapitalertragsteuer-Anmeldung: https://www.usp.gv.at/themen/steuern-finanzen/einkommensteuer-ueberblick/weitere-informationen-est/kapitalertragsteueranmeldung.html
- USP, Pflichten bei Inlandsaktivitäten ausländischer Unternehmer: https://www.usp.gv.at/themen/steuern-finanzen/einkommensteuer-ueberblick/weitere-informationen-est/internationales-steuerrecht/pflichten-bei-inlandsaktivitaeten-auslaendischer-unternehmer.html
- BMF, Rückerstattung österreichischer Abzugsteuer: https://www.bmf.gv.at/themen/steuern/internationales-steuerrecht/rueckerstattung/rueckerstattung-oesterreichischer-abzugsteuer.html
- BMF, form K 1 for 2025: https://formulare.bmf.gv.at/service/formulare/inter-Steuern/pdfs/2025/K1.pdf?open=download
- BMF, form G 4: https://formulare.bmf.gv.at/service/formulare/inter-Steuern/pdfs/9999/G4.pdf?open=inline
- BMF, group taxation decree 2005: https://findok.bmf.gv.at/findok/resources/pdf/d496d1e6-a12f-4229-9fe8-dab5e8063f9d/14269.1.1.5.pdf
- BMF Findok, appeals decision RV/0431-W/07: https://findok.bmf.gv.at/findok/resources/pdf/aea48cfe-b74b-4e31-bd43-42d39052a2df/54102.1.1.1.pdf

This Guide is a source-cited draft. It is not tax advice. Confirm each figure on the official page before relying on it, and have a Steuerberater review any filing.

> Contributed by OpenAccountants.

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
