---
name: at-vat-return
description: Use this skill whenever asked to prepare, review, or classify transactions for an Austrian VAT return (Umsatzsteuervoranmeldung / UVA) or annual declaration (Umsatzsteuererklärung / U1) for a self-employed individual or small business in Austria. Trigger on phrases like "prepare UVA", "Austrian VAT return", "Umsatzsteuer", "classify transactions for Austrian VAT", or any request involving Austria VAT filing. This skill covers Austria only, standard regime (Regelbesteuerung). Kleinunternehmerregelung, partial exemption, margin scheme (Differenzbesteuerung), and VAT groups (Organschaft) are in the refusal catalogue. MUST be loaded alongside BOTH vat-workflow-base v0.1 or later AND eu-vat-directive v0.1 or later. ALWAYS read this skill before touching any Austrian VAT work.
jurisdiction: AT
tax_year: 2026
last_updated: 2026-09-27
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Austrian VAT return: the Umsatzsteuervoranmeldung (U 30) and the annual return (U 1)

How to turn a business's bank statement and invoices into the Austrian VAT advance return (Umsatzsteuervoranmeldung, UVA, form U 30) and the annual VAT return (Umsatzsteuererklärung, form U 1) on the normal scheme (Regelbesteuerung). Figures are for tax year 2026, and each figure below names its year. Austria's VAT year is the calendar year. Every Kennzahl (KZ, box code) comes from the Finance Ministry's [2026 U 30 form, version of 13 March 2026](https://formulare.bmf.gv.at/service/formulare/inter-Steuern/pdfs/2026/U30.pdf?open=download), which already carries the boxes for the new food rate. The ministry's [2026 filling instructions (U 30a)](https://formulare.bmf.gv.at/service/formulare/inter-Steuern/pdfd/2026/U30a.pdf) are dated 20 August 2025, before that rate existed, so they do not mention its boxes.

The statute is the Umsatzsteuergesetz 1994 (UStG). The federal legal database (ris.bka.gv.at) did not answer when this Guide was checked, so section numbers come from the Finance Ministry (BMF) and business service portal (USP) pages that cite them: check the statute before relying on one in a dispute.

## Scope

- **Who:** sole traders, partnerships and companies established in Austria that charge Austrian VAT under the normal scheme, and small businesses deciding whether the small business exemption (Kleinunternehmerregelung) applies to them.
- **What:** the monthly or quarterly UVA, the annual U 1, the recapitulative statement (Zusammenfassende Meldung, ZM, form U 13), rates, reverse charge, intra-EU supplies and acquisitions, input VAT blocks, corrections and penalties.
- **Periods:** calendar 2026 (the UVA periods being filed now), with a dated section for the 2025 annual return.
- **Out of scope, refer:** the one-stop shop (OSS), VAT groups (Organschaft), the margin scheme, travel services (§ 23 UStG), flat-rate farming, partial exemption, property transactions, fiscal representation, Jungholz and Mittelberg, and income tax.

## Ask the client first

- Are you on the normal scheme or under the small business exemption? If you gave the exemption up (form U12), from which year?
- What was your turnover last year and so far this year, and did you opt for monthly filing? It decides the period and the exemption.
- Are you taxed on money received (Istbesteuerung) or on work done (Sollbesteuerung)? Freelance professions are usually on money received.
- Does a tax adviser file for you (it changes the annual deadline)?
- For each foreign supplier: which legal entity issued the invoice, and does it show Austrian VAT or a reverse-charge note?
- For each EU customer: do you hold its valid VAT number (UID), and are these goods or services?
- Any sales of listed basic foods since 1 July 2026, or restaurant or catering sales?
- For each vehicle: ordinary car, zero-emission car, or a van on the ministry's approved list (Fiskal-LKW)?
- Any construction work bought or sold, exempt sales, property, short-term letting (for example Airbnb: how long are stays, and does the small business exemption apply?), or an earlier UVA that was wrong or late?
- Is any refund (credit) still on the tax account?
- What is your VAT number (UID)? An Austrian UID is "ATU" followed by 8 digits (check the certificate from the tax office).

## The method, step by step

1. **Check the scheme.** Under the small business exemption there is no VAT, no UVA, no annual return and no input VAT: confirm the limit test and stop. If the exemption was waived, continue.
2. **Run the refusal list** in "When to refuse or refer". Stop on any trigger.
3. **Fix the period** from last year's turnover (monthly, quarterly or none) with the UVA table in the figures section.
4. **Fix the timing basis.** On work done (Soll), output tax arises at the end of the month the supply was made; if the invoice is issued in a later month, the tax point moves by at most one month (supply 10 July, invoice 4 October: tax arises at the end of August). No such deferral where the tax passes to the customer (reverse charge on a service or work supply): it arises at the end of the month of supply. On money received (Ist), it arises at the end of the month of payment, including down payments.
5. **Classify every line** with the pattern table, then the classification rules. Place of supply comes before the rate: a service to a business is taxed where the customer is (§ 3a Abs 6 UStG).
6. **Test each input VAT claim:** a proper invoice, a supply for the business, the at-least business-use test, the payment condition for cash-basis businesses, and the blocks for cars, business meals and travel services.
7. **Map each line to its Kennzahl** with the KZ map. Listed basic foods from 1 July 2026 go to KZ 124 (sales) and KZ 125 (intra-EU acquisitions).
8. **Compute KZ 095**: output tax plus reverse-charge and acquisition tax, less deductible input VAT, plus corrections; check it against FinanzOnline.
9. **File and pay** the U 30 by the 15th of the second month after the period. File the ZM by the end of the following month if there were intra-EU supplies of goods or general-rule B2B services to other member states.
10. **After the year**, file the U 1. It should equal the sum of the UVAs. Correct errors as set out under "Corrections and penalties".

## Figures for 2026, with years

### VAT rates (2026)

| What | Rate | Note |
| --- | --- | --- |
| Source | all rows | https://www.usp.gv.at/themen/steuern-finanzen/umsatzsteuer-ueberblick/steuersaetze-und-steuerbefreiungen-der-umsatzsteuer.html (updated 1 July 2026) |
| Standard rate (Normalsteuersatz), § 10 UStG | 20% | "Der Normalsteuersatz der Umsatzsteuer beträgt 20 Prozent." |
| Selected basic foods such as bread, butter, eggs, milk, from 1 July 2026 | 4.9% | Deliveries only, see the food rate rules below |
| Residential letting, accommodation, camping pitches, waste collection, books, newspapers, magazines, other food | 10% | Examples; the full list is in § 10 UStG |
| Live animals, live plants, firewood, artists' turnover, film and circus shows, sports event tickets | 13% | Examples; the full list is in § 10 UStG |
| Jungholz and Mittelberg (KZ 037, KZ 088) | 19% | Shown on the 2026 U 30; refer |

The page gives examples only: "Diese sind im § 10 Umsatzsteuergesetz vollständig aufgelistet." For any item not named above (for example passenger transport, medicines, water), take the rate from the supplier's invoice or check § 10 UStG.

**Food rate rules (from 1 July 2026).** Per the ministry's FAQ the rate is not time-limited, applies only where the food falls wholly under a combined-nomenclature heading listed in the new Anlage 3 to the UStG, and never to services: restaurant sales and catering stay outside it. A down payment received before 1 July 2026 for food delivered later is in principle taxed at the old rate, though the supplier may already apply the new one. [BMF FAQ on the food rate](https://www.bmf.gv.at/rechtsnews/steuern-rechtsnews/aktuelle-infos-und-erlaesse/fachinformationen---umsatzsteuer/umsatzsteuersenkung-auf-ausgewaehlte-nahrungsmittel.html)

### UVA: who files and how often (2026, based on 2025 turnover)

| Prior-year turnover | Value | Rule |
| --- | --- | --- |
| Source | all rows | https://www.usp.gv.at/themen/steuern-finanzen/umsatzsteuer-ueberblick/weitere-informationen-zur-umsatzsteuer/entstehen-der-steuerschuld-und-pflichten/umsatzsteuervoranmeldung.html |
| Monthly UVA if prior-year turnover exceeded | EUR 100,000 | "Kalenderjahr 100.000 Euro überstiegen haben, sind zur monatlichen Abgabe" |
| Quarterly UVA if prior-year turnover exceeded this, but not the monthly limit | EUR 55,000 | "Übersteigt der Vorjahresumsatz 55.000 Euro, aber nicht 100.000 Euro, sind vierteljährlich" |
| No UVA to file if prior-year turnover did not exceed | EUR 55,000 | Only if the payment is made in full on time, or there is none; see below |

- A quarterly filer may choose monthly by filing the January UVA on time; the choice binds for that calendar year. A new business estimates its first-year turnover and files monthly from the start if it expects more than EUR 100,000 ([annual return page](https://www.usp.gv.at/themen/steuern-finanzen/umsatzsteuer-ueberblick/umsatzsteuervoranmeldung-und-umsatzsteuererklaerung.html)).
- At or below EUR 55,000 the business still computes each period, keeps an internal return (interne Voranmeldung) with its records and pays on time. It must file a UVA when the period shows a refund (a refund can only be claimed by filing), when it pays late or short, or when the tax office orders it ([U 30a 2026](https://formulare.bmf.gv.at/service/formulare/inter-Steuern/pdfd/2026/U30a.pdf)).
- A business making only exempt-without-credit supplies (§ 6 Abs 1 Z 7 to 28) files no UVA for a period with neither a payment nor a refund (U 30a 2026).

### Small business exemption (rules since 1 January 2025; limit for 2026)

| What | Value | Note |
| --- | --- | --- |
| Source | all rows | https://www.usp.gv.at/themen/steuern-finanzen/umsatzsteuer-ueberblick/weitere-informationen-zur-umsatzsteuer/weitere-steuertatbestaende-und-befreiungen/kleinunternehmen.html |
| Limit, not exceeded in the previous nor the current calendar year (2025 onward) | EUR 55,000 | "Kleinunternehmergrenze in Höhe von 55.000 Euro (bis 31. Dezember 2024: 35.000 Euro)" |
| Tolerance in the year the limit is crossed | 10% | "wenn die Grenze um nicht mehr als 10 Prozent überschritten wird" |
| Old limit to 31 December 2024, net, history only | EUR 35,000 | Old law: crossing it made the whole year taxable |

Conditions and effects:
- The business must have its seat of economic activity in the EU. For a business based in Austria the exemption applies automatically from the first sale; to use normal taxation it must opt out. Businesses from outside the EU cannot use it ([USP news, 26 February 2025](https://www.usp.gv.at/aktuelles/newsliste/kleinunternehmerregelung-ab-2025.html)).
- The limit is gross: the whole agreed consideration counts, with no notional VAT taken out ([USP news](https://www.usp.gv.at/aktuelles/newsliste/kleinunternehmerregelung-ab-2025.html)).
- Count all B2C and B2B sales taxable in Austria, including intra-EU supplies and transfers. Do not count purchases on which the business owes the tax (intra-EU acquisitions, reverse-charge services), ancillary sales including the sale of the whole business, or certain exempt sales listed in § 6 Abs 1 (for example doctors' treatment).
- Over the limit by no more than the tolerance: exempt to year end, taxable from 1 January of the next year. Over by more: the sale that crosses the limit and every later sale are taxable.
- Exempt businesses file no UVA and no annual return and deduct no input VAT. VAT shown on an invoice anyway is owed unless the invoice is corrected.
- Waiver: a written declaration (form U12) until the VAT assessment is final; it binds for five years and can be revoked. A business that waived must file an annual return.

**Exemption in other member states (EU SME scheme, from 2025).** An Austrian small business can also be exempt in another member state only after an advance notification through FinanzOnline, and only while its total EU turnover does not exceed EUR 100,000 in the current and the previous calendar year and it stays under that state's own limit. There is no tolerance: crossing the EU-wide limit ends the scheme ([USP page](https://www.usp.gv.at/themen/steuern-finanzen/umsatzsteuer-ueberblick/weitere-informationen-zur-umsatzsteuer/weitere-steuertatbestaende-und-befreiungen/kleinunternehmerbefreiung-in-anderen-mitgliedstaaten.html)).

### Timing basis and deadlines (2026)

| What | Value | Note |
| --- | --- | --- |
| Source | timing rows | https://www.usp.gv.at/themen/steuern-finanzen/umsatzsteuer-ueberblick/weitere-informationen-zur-umsatzsteuer/entstehen-der-steuerschuld-und-pflichten/zeitpunkt-des-entstehens-der-steuerschuld.html |
| Cash basis (Ist) for other businesses (for example landlords) if total turnover in either of the two prior years was not above | EUR 110,000 | Freelance professions and non-accounting traders are on the cash basis whatever their turnover; the accrual basis can be chosen on application |
| Accrual basis (Soll): tax point | End of month of supply | Late invoice defers it by at most one month; no deferral when the tax passes to the customer |
| Input VAT only once paid, for cash-basis businesses whose prior-year taxable turnover did not exceed | EUR 2 million | [Input VAT page](https://www.usp.gv.at/themen/steuern-finanzen/umsatzsteuer-ueberblick/vorsteuerabzug.html) |

- **UVA and payment:** the 15th of the second month after the period. Quarterly: 15 May, 15 August, 15 November, 15 February. Example: May is due 15 July. A due date on a Saturday, Sunday, public holiday, Good Friday or 24 December moves to the next working day ([BMF deadlines](https://www.bmf.gv.at/themen/steuern/fristen-verfahren/fristen-faelligkeiten.html)). The payment slip must name the period and the amount.
- **ZM:** by the end of the calendar month after the reporting period, through FinanzOnline. The ZM period follows the UVA period: a quarterly UVA filer files quarterly ZMs, a monthly UVA filer (including a quarterly filer who opted for monthly UVAs) files monthly ZMs, and periods cannot be combined ([U 13a](https://formulare.bmf.gv.at/service/formulare/inter-steuern/pdfd/9999/u13a.pdf)).
- **Annual U 1:** 30 June of the next year through FinanzOnline, or 30 April on paper. Paper filing is allowed without internet access, or for a self-filer whose prior-year turnover does not exceed EUR 55,000 ([USP, Einreichen von Steuererklärungen](https://www.usp.gv.at/themen/steuern-finanzen/steuerliche-rechte-und-pflichten/weitere-informationen-zu-steuerlichen-rechten-und-pflichten-als-unternehmen/einreichen-von-steuererklaerungen.html)); the [BMF deadlines page](https://www.bmf.gv.at/themen/steuern/fristen-verfahren/fristen-faelligkeiten.html) still states EUR 35,000, so confirm with the tax office before relying on paper filing. A represented business usually has longer. Any balance set by the assessment is due within one month of its delivery.

### Other limits used in this Guide

| What | Value | Year and note |
| --- | --- | --- |
| Source | this row | https://www.usp.gv.at/themen/steuern-finanzen/umsatzsteuer-ueberblick/weitere-informationen-zur-umsatzsteuer/umsaetze-mit-auslandsbezug/zusammenfassende-meldung-zm.html |
| ZM monthly if turnover is over (quarterly at or below) | EUR 100,000 | Standing rule, page updated 1 January 2026 |
| Source | this row | https://www.usp.gv.at/themen/steuern-finanzen/umsatzsteuer-ueberblick/vorsteuerabzug.html |
| Minimum business use for a purchase to count as made for the business | 10% | "wenn zu mindestens 10 Prozent unternehmerischen Zwecken dienen" |
| Source | this row | https://www.usp.gv.at/themen/steuern-finanzen/umsatzsteuer-ueberblick/weitere-informationen-zur-umsatzsteuer/vorsteuerabzug-und-rechnung/kleinbetragsrechnungen.html |
| Simplified invoice allowed up to this total, gross | EUR 400 | Not for distance sales |
| Source | this row | https://www.usp.gv.at/themen/steuern-finanzen/umsatzsteuer-ueberblick/weitere-informationen-zur-umsatzsteuer/vorsteuerabzug-und-rechnung/ausnahmen-vom-vorsteuerabzug.html |
| Car input VAT allowed if used at least this much for commercial passenger transport or rental | 80% | Other car exceptions in the rules below |
| Source | this row | https://formulare.bmf.gv.at/service/formulare/inter-Steuern/pdfd/2026/U30a.pdf |
| Mobile phones and integrated circuits: reverse charge if the invoiced consideration is at least | EUR 5,000 | 2026 instructions |
| Source | this row | https://formulare.bmf.gv.at/service/formulare/inter-Steuern/pdfd/2025/U1a.pdf |
| Business gift treated as own use (Eigenverbrauch) if worth over | EUR 40 | 2025 U 1a instructions |
| Source | this row | https://www.usp.gv.at/themen/steuern-finanzen/steuerliche-gewinnermittlung/weitere-informationen-zur-steuerlichen-gewinnermittlung/betriebseinnahmen-und-ausgaben/geringwertige-wirtschaftsgueter.html |
| Low-value asset, income tax only: immediate write-off if cost, net of deductible VAT, is not more than | EUR 1,000 | Business years from 1 January 2023 |
| Source | this row | https://www.usp.gv.at/themen/steuern-finanzen/umsatzsteuer-ueberblick/weitere-informationen-zur-umsatzsteuer/umsaetze-mit-auslandsbezug/innergemeinschaftlicher-versandhandel.html |
| EU-wide B2C distance sales and electronic services up to which home-country VAT may apply | EUR 10,000 | Micro-business rule since 1 July 2021 |

### Kennzahl map of the 2026 U 30

| KZ | Meaning on the form | Rate |
| --- | --- | --- |
| Source | all rows | https://formulare.bmf.gv.at/service/formulare/inter-Steuern/pdfs/2026/U30.pdf?open=download |
| 000 | Total tax base of supplies and services, incl. down payments, net of VAT | |
| 001 | Plus own use (Eigenverbrauch, § 1 Abs 1 Z 2, § 3 Abs 2, § 3a Abs 1a) | |
| 021 | Minus sales where the tax passed to the customer (§ 19 Abs 1 second sentence, Abs 1a to 1e) | |
| 011 | Exempt with credit: exports (§ 7) | |
| 012 | Exempt with credit: processing for export (Lohnveredelung, § 8) | |
| 015 | Exempt with credit: shipping, aviation, cross-border passenger transport and similar (§ 6 Abs 1 Z 2 to 6) | |
| 017 | Exempt with credit: intra-EU supplies of goods (Art. 6 Abs 1) | |
| 018 | Intra-EU supplies of new vehicles to buyers without a UID (Art. 2) | |
| 019 | Exempt without credit: land (§ 6 Abs 1 Z 9 lit a) | |
| 016 | Exempt without credit: small business (§ 6 Abs 1 Z 27) | |
| 020 | Other exempt without credit | |
| 022 | Taxable at the standard rate: base | 20% |
| 124 | Taxable at the food rate: base (new on the 2026 form) | 4.9% |
| 029 | Taxable at the reduced rate: base | 10% |
| 006 | Taxable at the reduced rate: base | 13% |
| 037 | Jungholz and Mittelberg: base | 19% |
| 052, 007 | Additional tax for flat-rate farming and forestry (out of scope) | |
| 056 | Tax owed for example on VAT shown wrongly on an invoice (§ 11 Abs 12 and 14) | |
| 057 | Tax owed as recipient: services from foreign businesses, EU or non-EU (§ 19 Abs 1 second sentence, 1c, 1e) | |
| 048 | Tax owed as recipient of construction services (§ 19 Abs 1a) | |
| 044 | Tax owed under § 19 Abs 1b (security ownership, retained title, land in forced sale) | |
| 032 | Tax owed under § 19 Abs 1d (scrap, laptops, tablets, gas, electricity, metals, gold) | |
| 070 | Intra-EU acquisitions: total base | |
| 071 | Of which exempt (Art. 6 Abs 2) | |
| 072 | Intra-EU acquisitions at the standard rate: base | 20% |
| 125 | Intra-EU acquisitions at the food rate: base (new on the 2026 form) | 4.9% |
| 073 | Intra-EU acquisitions at the reduced rate: base | 10% |
| 008 | Intra-EU acquisitions at the reduced rate: base | 13% |
| 088 | Intra-EU acquisitions, Jungholz and Mittelberg | 19% |
| 076, 077 | Acquisitions not taxed here (Art. 3 Abs 8) | |
| 060 | Total input VAT, without the amounts in the boxes below | |
| 061 | Input VAT: import VAT paid | |
| 083 | Input VAT: import VAT booked on the tax account | |
| 065 | Input VAT from intra-EU acquisitions | |
| 066 | Input VAT on the tax in KZ 057 | |
| 082 | Input VAT on the tax in KZ 048 | |
| 087 | Input VAT on the tax in KZ 044 | |
| 089 | Input VAT on the tax in KZ 032 | |
| 064 | Input VAT, new vehicles from occasional suppliers | |
| 062 | Of which not deductible (§ 12 Abs 3 with Abs 4 and 5) | |
| 063 | Correction under § 12 Abs 10 and 11 (change of use) | |
| 067 | Correction of input VAT under § 16 (changes in consideration) | |
| 090 | Other corrections (sonstige Berichtigungen) | |
| 095 | Payment due (Zahllast) or refund (Überschuss): one box for both | |

How the boxes work (form and [U 30a 2026](https://formulare.bmf.gv.at/service/formulare/inter-Steuern/pdfd/2026/U30a.pdf)):
- Rate boxes take the base, with the tax in a second column. KZ 057, 048, 044 and 032 take the TAX; its input VAT goes in KZ 066, 082, 087 and 089, so the net is zero with full deduction.
- There is no "total output VAT" box. KZ 083 is import VAT, not output tax.
- Changes in price go into KZ 000 and the matching rate box. If a box would turn negative, enter zero there and put the negative amount in KZ 067 (input VAT) or KZ 090 (output VAT).
- Import VAT booked on the tax account is paid separately (slip marked "EU"); only its deduction goes in KZ 083.
- KZ 021 holds sales already in KZ 000 where the customer owes the tax, such as construction services, and mobile phones or chips from the invoiced amount in the limits table. The customer enters that tax in KZ 057 and KZ 066 (phones and chips) or KZ 048 and KZ 082 (construction).
- Sales not taxable in Austria (place of supply abroad, for example a B2B service to an EU business) go in neither KZ 000 nor KZ 021 ([U 1a 2025](https://formulare.bmf.gv.at/service/formulare/inter-Steuern/pdfd/2025/U1a.pdf)).

## Boundary and exception table

| Situation | Treatment | Why |
| --- | --- | --- |
| Source | limits in this table | https://www.usp.gv.at/themen/steuern-finanzen/umsatzsteuer-ueberblick/weitere-informationen-zur-umsatzsteuer/weitere-steuertatbestaende-und-befreiungen/kleinunternehmen.html |
| Prior-year turnover exactly EUR 55,000 | No UVA duty (the test is "exceeded") | Monthly and quarterly bands start above the figure |
| Prior-year turnover exactly EUR 100,000 | Quarterly, not monthly | Monthly only if it was exceeded |
| Small business: last year over EUR 55,000, this year under | Not exempt this year | Neither year may exceed the limit |
| Small business: crosses the limit by at most 10% | Exempt to 31 December, taxable from 1 January | Tolerance |
| Small business: crosses by more than 10% | Taxable from the crossing sale onward | No tolerance |
| Food rate: bread sold over the counter vs served in a restaurant | 4.9% vs restaurant rate | Services are outside the food rate |
| B2B service to an EU business, general rule | Not in KZ 000 or KZ 021; in the ZM | Taxed in the customer's state |
| B2B service to an EU business, special rule (land, events, passenger transport) | Not in the ZM; check where it is taxed | ZM covers the general rule only |
| Service from a foreign business: federal road tolls, event services, letting of land | No reverse charge; the supplier charges VAT | Excluded from the reverse charge |
| Construction service bought by a business that neither was commissioned for the building work nor usually supplies construction | Normal invoice with VAT, KZ 060 | Reverse charge only for those two groups |
| Intra-EU supply of goods without a ZM filed by the end of the following month | Exempt only if the failure is justified to the tax office and the ZM is filed or corrected | Since 1 January 2020 |
| Zero-emission car | Input VAT allowed within the reasonableness cap (check the current cap with the BMF) | Exception to the car block |

### Classification rules

**Rates and sales**
- Sales go in KZ 000 and the rate box from the KZ map. Unknown rate on a sale: standard rate.
- Exempt with credit: exports KZ 011; intra-EU supplies of goods to a business with a valid UID KZ 017 and the ZM ([ZM page](https://www.usp.gv.at/themen/steuern-finanzen/umsatzsteuer-ueberblick/weitere-informationen-zur-umsatzsteuer/umsaetze-mit-auslandsbezug/zusammenfassende-meldung-zm.html)).
- Exempt without credit (medical, certain education, insurance, finance, land sales): land KZ 019, others KZ 020. If material alongside taxable sales, refer (partial exemption).
- Residential letting is at the reduced rate; business premises are exempt unless the landlord opts to tax. The option needs no separate declaration: treating the letting as taxable in the UVA is enough ([rates page](https://www.usp.gv.at/themen/steuern-finanzen/umsatzsteuer-ueberblick/steuersaetze-und-steuerbefreiungen-der-umsatzsteuer.html)).
- Cross-border B2C goods and e-services above the EU-wide limit in the limits table: refer (OSS).

**Reverse charge and acquisitions** ([reverse charge](https://www.usp.gv.at/themen/steuern-finanzen/umsatzsteuer-ueberblick/weitere-informationen-zur-umsatzsteuer/umsaetze-mit-auslandsbezug/reverse-charge.html))
- Service from a business abroad with no Austrian establishment, taxable in Austria (EU or non-EU): tax in KZ 057, input VAT in KZ 066. One pair of boxes for both.
- Goods from an EU business: base in KZ 070 and the rate box; input VAT KZ 065.
- Construction received: the tax passes when the recipient was itself commissioned to do the building work or usually supplies construction services. Tax KZ 048, input VAT KZ 082. The subcontractor enters its sale in KZ 000 and KZ 021.
- Scrap, metals, gold, electronics, gas and electricity under § 19 Abs 1d: KZ 032 and KZ 089 (refer if unsure).
- Reverse-charge invoices are net, with a note of the transfer of liability and both UID numbers, issued by the 15th of the month after the supply.

**Input VAT** ([input VAT](https://www.usp.gv.at/themen/steuern-finanzen/umsatzsteuer-ueberblick/vorsteuerabzug.html))
- Deductible on a proper invoice for a supply to the business (business use at least the share in the limits table), in KZ 060. Down payments are deductible once paid and invoiced. Start-up costs before the first sale are deductible.
- Cash-basis businesses under the payment limit deduct only once they have paid.
- Unknown VAT status or business share (for example a mixed-use phone): no deduction until the client answers.
- A later change of use of a capital asset is corrected under § 12 Abs 10 UStG in KZ 063. For land the correction period is the 19 calendar years after the year of first use, one twentieth per year of change.

**Blocked input VAT** ([exceptions](https://www.usp.gv.at/themen/steuern-finanzen/umsatzsteuer-ueberblick/weitere-informationen-zur-umsatzsteuer/vorsteuerabzug-und-rechnung/ausnahmen-vom-vorsteuerabzug.html))
- Cars, estate cars and motorcycles: no input VAT on purchase, lease or running costs (fuel, repairs, tolls, vignette, parking), even at full business use. Exceptions: driving school cars, demonstration cars, cars held for resale, cars used at least the share in the limits table for commercial passenger transport or rental, vans on the ministry's Fiskal-LKW list, and zero-emission cars within the reasonableness cap.
- Business meals: only if you can prove the meal served advertising and the business reason far outweighed everything else. Default: block and ask.
- Travel services bought in for resale to travellers (Reisevorleistungen): no input VAT.
- A business gift above the own-use limit in the limits table is own use: base in KZ 001, tax in the rate box. It is not an input VAT block.

### Bank-statement patterns

Match by case-insensitive text. Domestic input VAT goes in KZ 060; take the rate from the invoice.

| Pattern | Treatment |
| --- | --- |
| Source | https://www.usp.gv.at/themen/steuern-finanzen/umsatzsteuer-ueberblick/steuersaetze-und-steuerbefreiungen-der-umsatzsteuer.html |
| Bank fees and interest (ERSTE, RAIFFEISEN, BAWAG, BANK AUSTRIA, HYPO, REVOLUT, WISE); ZINSEN, KREDIT, TILGUNG | Exclude (exempt or outside VAT); check fintech lines for taxable subscriptions |
| FINANZAMT, GERICHT, GEMEINDE, FIRMENBUCH, GRUNDSTEUER; SVS, ÖGK, WKO, GEHALT, LOHN; VERSICHERUNG, UNIQA, GENERALI, ALLIANZ | Exclude (taxes, fees, social insurance, wages, exempt insurance) |
| Energy and telecoms (WIEN ENERGIE, EVN, KELAG, A1, MAGENTA, DREI) | Standard rate, KZ 060 (water: rate from the invoice) |
| Post and couriers: ÖSTERREICHISCHE POST (letters) / parcels, DHL, DPD, GLS | Letter postage exempt: exclude. Parcels and couriers: standard rate |
| Transport: ÖBB, WESTBAHN, WIENER LINIEN, regional lines, taxi, Uber, domestic flights | Domestic, rate from the invoice. International flights: exclude |
| ASFINAG, fuel (OMV, BP, SHELL, AVIA, ENI, JET) | Blocked for a car; ask about the vehicle |
| Supermarkets (SPAR, BILLA, HOFER, LIDL, PENNY, MPREIS, UNIMARKT) and restaurants | Block unless the business is hospitality or a documented advertising meal |
| STEUERBERATER, RECHTSANWALT, NOTAR, BILANZBUCHHALTER, consultants | Standard rate, KZ 060 |
| Foreign software and ads: Google, Microsoft, Adobe, Meta, Zoom (Irish entities); Notion, OpenAI, Anthropic, GitHub, Figma, Canva (non-EU) | Reverse charge KZ 057 and KZ 066. If the invoice shows Austrian VAT (for example AWS EMEA), domestic KZ 060. Unknown entity: ask |
| Stripe or PayPal transaction fees | Exclude (financial). Stripe subscription (Irish entity): reverse charge |
| Rent: BÜROMIETE, GESCHÄFTSLOKAL / WOHNUNGSMIETE | Business rent: 20% input VAT only if the landlord opted to tax, otherwise exempt; residential rent: 10% if VAT is charged |
| UMBUCHUNG, PRIVATEINLAGE, DIVIDENDE; cash withdrawals (BEHEBUNG) | Exclude; ask about cash |

Convert foreign currency to euro; IBAN prefix CH, GB or US means outside the EU. A foreign hotel bill is excluded: foreign VAT is reclaimed through the refund procedure, not the UVA. Conservative defaults when the client cannot answer: unknown counterparty country, treat as domestic; unknown whether an EU customer is a business, charge Austrian VAT; unknown whether in scope, treat as in scope.

## Worked cases

Statement amounts are in euro; the client is an IT consultant on the normal scheme unless stated.

**Case 1: US software, reverse charge.** `03.04.2026 ; NOTION LABS INC ; -14.68`. A US entity with no Austrian establishment supplies a B2B service taxed in Austria, so the client owes the tax (§ 19 Abs 1 second sentence UStG). Tax 14.68 x standard rate = 2.94 in KZ 057, and 2.94 in KZ 066. Net zero.

**Case 2: Irish advertising, reverse charge.** `10.04.2026 ; GOOGLE IRELAND LIMITED ; -850.00`. Service to a business, taxed where the customer is (§ 3a Abs 6 UStG). Tax 850.00 x standard rate = 170.00 in KZ 057 and KZ 066. No ZM: the ZM is for the supplier's sales, not purchases.

**Case 3: Laptop.** `18.04.2026 ; DELL AUSTRIA GMBH ; -1,595.00`, invoice at the standard rate. Net 1,329.17, input VAT 265.83 in KZ 060. The net cost is above the income tax low-value asset limit, so it is capitalised for income tax; VAT deduction is the same either way. [Low-value assets](https://www.usp.gv.at/themen/steuern-finanzen/steuerliche-gewinnermittlung/weitere-informationen-zur-steuerlichen-gewinnermittlung/betriebseinnahmen-und-ausgaben/geringwertige-wirtschaftsgueter.html)

**Case 4: Consulting for a German business.** `22.04.2026 ; STUDIO KREBS GMBH ; +3,500.00`. General-rule B2B service, taxed in Germany. Invoice net by 15 May 2026 with a reverse-charge note and both UID numbers; check the German VAT number first. Not in KZ 000 or KZ 021; report 3,500.00 in the ZM for April (monthly filer: due 31 May 2026). If the customer's business status cannot be confirmed, charge Austrian VAT.

**Case 5: Car lease and a business dinner.** `28.04.2026 ; PORSCHE BANK LEASING ; -550.00` for a petrol VW Golf: no input VAT, even at full business use; record the gross amount as a cost. `15.04.2026 ; GASTHAUS ; -220.00`: no input VAT unless the client documents an advertising purpose that far outweighs the rest. Ask both questions before filing.

**Case 6: Small business near the limit (2026).** Exempt small business, 2025 turnover under the limit. Sales January to October 2026: EUR 54,500; a EUR 4,000 order in November takes 2026 turnover to EUR 58,500. The tolerance ceiling is EUR 55,000 x 1.1 = EUR 60,500, so the November invoice can still go out without VAT and 2026 stays exempt; from 1 January 2027 the business is taxable and must file UVAs if 2026 turnover exceeded the UVA limit. A further December sale taking the year above EUR 60,500 would be taxable from that sale onward. [USP news](https://www.usp.gv.at/aktuelles/newsliste/kleinunternehmerregelung-ab-2025.html)

**Case 7: Late quarterly payment (2026).** Quarterly filer; Q2 2026 (April to June) payable EUR 3,000. Due date 15 August 2026 is a Saturday and a public holiday, so it moves to Monday 17 August 2026. Paid on 1 September 2026, more than five days late: first late-payment surcharge 2% x EUR 3,000 = EUR 60 (the five-day grace cannot apply: the payment is 15 days late). A late UVA also risks the late-filing surcharge. [BMF deadlines](https://www.bmf.gv.at/themen/steuern/fristen-verfahren/fristen-faelligkeiten.html)

## When to refuse or refer

- The small business exemption applies and the question is anything beyond the limit test (for example the EU SME scheme in another member state).
- Mixed taxable and exempt sales needing apportionment (§ 12 Abs 4 to 6 UStG), the margin scheme, a VAT group, fiscal representation, property sales or opted lettings, Jungholz or Mittelberg.
- A special scheme: OSS, travel services (§ 23 UStG), flat-rate farming (KZ 052, KZ 007).
- Construction, scrap, metals, gold or electronics reverse charge (KZ 048, KZ 032) where the deciding facts are not on the statement.
- A change-of-use correction (KZ 063), VAT shown wrongly on an invoice (KZ 056), or an error in an earlier period that may need a self-disclosure.
- A material line whose counterparty cannot be identified and whose invoice the client cannot produce.
- Income tax questions: use the Austrian income tax Guide.

## Filing and payment

- **Where:** FinanzOnline; paper forms only without internet access (a representative's access counts). Keep a copy of every UVA. Authority: Finanzamt Österreich, or Finanzamt für Großbetriebe. [UVA page](https://www.usp.gv.at/themen/steuern-finanzen/umsatzsteuer-ueberblick/weitere-informationen-zur-umsatzsteuer/entstehen-der-steuerschuld-und-pflichten/umsatzsteuervoranmeldung.html)
- **When:** UVA and payment by the 15th of the second month after the period (see the deadlines above); ZM by the end of the following month; annual U 1 by 30 June online (30 April where paper is allowed).
- **Annual return duty:** in principle every business whose annual turnover exceeds EUR 55,000, and every business that waived the small business exemption. The U 1 should match the UVAs; a shortfall set by the assessment is due within a month, and an appeal (Beschwerde) is due within a month of the assessment. [Annual return page](https://www.usp.gv.at/themen/steuern-finanzen/umsatzsteuer-ueberblick/umsatzsteuervoranmeldung-und-umsatzsteuererklaerung.html)
- **Returns being filed now (2025 annual U 1):** due 30 June 2026 online (30 April 2026 where paper filing is allowed); later only if the business is represented by a tax adviser or an extension was granted on a reasoned request. Use the [2025 U 1a instructions](https://formulare.bmf.gv.at/service/formulare/inter-Steuern/pdfd/2025/U1a.pdf). 2025 was the first year of the EUR 55,000 gross small business limit.

### Corrections and penalties (2026)

| What | Value | Rule |
| --- | --- | --- |
| Source | rows 1 to 3 | https://www.bmf.gv.at/themen/steuern/fristen-verfahren/fristen-faelligkeiten.html |
| First late-payment surcharge (Säumniszuschlag) | 2% | Of tax not paid by the due date; none if no more than five days late and everything was paid on time in the previous six months |
| Second and third late-payment surcharge | 1% | Each, three months apart, on the amount still unpaid |
| Late-filing surcharge (Verspätungszuschlag, § 135 BAO) | 10% | Up to this share of the tax, if the delay is not excusable |
| Source | rows 5 and 6 | https://formulare.bmf.gv.at/service/formulare/inter-steuern/pdfd/9999/u13a.pdf |
| Late ZM: surcharge up to this share of all reportable amounts | 1% | ZM instructions version 27.02.2020 |
| Late ZM: surcharge cap | EUR 2,200 | Separate coercive penalty up to EUR 5,000 |
| Source | row 8 | https://www.bmf.gv.at/themen/steuern/finanzstrafverfahren/schlechtes-gewissen-selbstanzeige.html |
| Extra charge if self-disclosure comes after an audit is announced | 30% | Maximum, of the additional tax |
| Source | rows 10 to 12 | https://www.bmf.gv.at/themen/steuern/finanzstrafverfahren/ein-fehler-passiert.html |
| Shortfall surcharge instead of a criminal referral (Verkürzungszuschlag, § 30a FinStrG), up to EUR 50,000 of shortfall | 10% | Above that: 15% |
| Maximum shortfall for that route, per year | EUR 33,000 | In total at most EUR 100,000. The tax office decides whether to offer it; you must agree or apply within 14 days and waive an appeal; no criminal case or self-disclosure may be pending; no penalty only if tax and surcharge are paid in full within one month |

- **Correcting a UVA before or on its due date:** file a corrected UVA (tick "Berichtigte Umsatzsteuervoranmeldung" on the [U 30](https://formulare.bmf.gv.at/service/formulare/inter-Steuern/pdfs/2026/U30.pdf?open=download)) with the full corrected figures.
- **After the due date:** a too-low payment is a possible offence. A self-disclosure (Selbstanzeige, § 29 FinStrG) protects only if made before investigations start, with the bases fully disclosed; for UVA amounts the tax must be paid within one month from the self-disclosure. In practice file the corrected UVA with it, or correct the year in the U 1. Refer to a Steuerberater.
- **Price changes** (discounts, bad debts) go in the current UVA, not as corrections of the old period.
- **What the ZM covers:** intra-EU supplies of goods, intra-EU transfers of own goods (Verbringungen), and general-rule B2B services to other member states.
- **Wrong ZM:** file a corrected ZM for the period; an intra-EU supply stays exempt only if a missing or wrong ZM is justified and corrected.

## Completion checklist

- [ ] Scheme confirmed (normal, or exemption limit tested for both years).
- [ ] Period (monthly, quarterly, none) and timing basis (Soll or Ist) confirmed.
- [ ] Every line classified; exclusions listed; foreign currency converted.
- [ ] Every reverse-charge line has both the tax box and the matching input VAT box.
- [ ] Food-rate sales from 1 July 2026 in KZ 124, not KZ 029.
- [ ] Input VAT blocks applied (cars, meals, travel services); business share checked.
- [ ] Non-taxable foreign B2B services kept out of KZ 000 and KZ 021 and put in the ZM.
- [ ] KZ 095 agrees with the FinanzOnline calculation.
- [ ] UVA filed and paid by the due date (weekend rule checked); ZM filed by the end of the following month.
- [ ] Earlier-period errors flagged for correction or self-disclosure.

Every source is linked where it is used. All are official pages of the Federal Ministry of Finance (bmf.gv.at, formulare.bmf.gv.at) or the business service portal (usp.gv.at), read on 25 to 27 September 2026.

This Guide is general information, not tax advice. Have a qualified adviser (Steuerberater) check a return before it is filed.

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
