---
name: at-vat-return
description: "Austrian VAT (Umsatzsteuer) for tax year 2026, worked box by box: how to turn a business's bank statement and invoices into the advance return (Umsatzsteuervoranmeldung, UVA, form U 30) and the annual return (U 1) under the Umsatzsteuergesetz 1994 as in force on 26 October 2026. Covers the 20%, 13% and 10% rates, the 4.9% rate on listed basic foods from 1 July 2026, the end of the 0% photovoltaic rate, the small business exemption (EUR 55,000 with the 10% tolerance) and the EU SME scheme (EUR 100,000 EU-wide), monthly or quarterly UVA periods, the 15th of the second following month, the U 1 by 30 April or 30 June, reverse charge, the recapitulative statement (ZM), the Kennzahl map, the 12 items of Anlage 3, catering and drinks, crossing the tolerance mid-year, input VAT blocks, late-payment and late-filing surcharges, VAT interest and self-disclosure. Trigger on: prepare UVA, Austrian VAT return, Umsatzsteuer, U 30, Kennzahl, Kleinunternehmer, ZM Austria. Out of scope: income tax (at-income-tax), corporate tax (at-corporate-income-tax), non-residents and treaties (at-cross-border); this is the one Austrian VAT skill."
version: 0.4
jurisdiction: AT
tax_year: 2026
last_updated: 2026-10-31
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Austrian VAT return: the UVA (U 30) and the annual return (U 1), 2026

This skill turns a business's bank statement and invoices into the Austrian VAT advance return (Umsatzsteuervoranmeldung, UVA, form U 30) and the annual VAT return (Umsatzsteuererklärung, U 1) for tax year 2026. The law is the Umsatzsteuergesetz 1994 (UStG) and its Binnenmarkt annex, both read on RIS in the version of 26 October 2026, with the Bundesabgabenordnung (BAO) for deadlines and surcharges. The VAT year is the calendar year.

**Which text of the law.** The RIS consolidated UStG read on 31 October 2026 lists BGBl. I Nr. 62/2026 as its latest amendment. That act, the Budgetbegleitgesetz 2027-2028, changes § 26 Abs 3 Z 2 (import VAT collected by the tax office) for imports after 31 December 2026 (§ 28 Abs 70), so nothing for tax year 2026 turns on it. The 4.9% food rate and Anlage 3 came in by BGBl. I Nr. 37/2026 and apply to supplies made after 30 June 2026 (§ 28 Abs 69). BGBl. I Nr. 43/2026 changed Art. 21 Abs 2 of the Binnenmarkt annex (new vehicles) from 1 July 2026; nothing in this skill turns on it.

## Who this applies to

- **In:** sole traders, partnerships and companies that make supplies in Austria (§ 1 Abs 1 Z 1 and 2 UStG), whether they are on normal taxation or deciding whether the small business exemption applies.
- **The tax debtor** is the supplier (§ 19 Abs 1 UStG), except where the tax passes to the customer (reverse charge, see the base section).
- **Small businesses** with turnover up to EUR 55,000 are exempt unless they opt out (§ 6 Abs 1 Z 27 UStG). They charge no VAT and deduct none.
- **Businesses established in another member state** can use the Austrian exemption only through the EU SME scheme: EU-wide turnover not above EUR 100,000 in the previous and current year, and the Art. 6a procedure in their home state. The exemption starts on the day Austria is notified of their small-business identification number, or, if they already have one, on the day the other member state confirms it for the Austrian exemption (§ 6 Abs 1 Z 27 UStG).
- **Out altogether:** private individuals, and businesses making only exempt supplies without credit (for example doctors, insurers) for those supplies.
- **Out of scope, refer:** the one-stop shop (OSS), VAT groups (Organschaft), the margin scheme, travel services (§ 23 UStG), flat-rate farming (§ 22 UStG), partial exemption apportionment, property sales and opted lettings, fiscal representation, Jungholz and Mittelberg.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source URL |
|---|---|---|---|
| Standard rate (§ 10 Abs 1) | 20% | 2026 | https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004873 |
| Listed basic foods in Anlage 3, deliveries and imports only, from 1 July 2026 (§ 10 Abs 1a, § 28 Abs 69, BGBl. I Nr. 37/2026). Anlage 3 has 12 items: milk, yoghurt, butter, fresh hen eggs, fresh or chilled vegetables, frozen vegetables, apples, pears and stone fruit (CN 0808 and 0809), rice, wheat flour and semolina, uncooked pasta, bread, table salt, each only within its listed CN code | 4.9% | 2026 (from 1 July) | https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004873 |
| Reduced rate: Anlage 1 goods (most food, books, newspapers), residential letting, restaurant and catering food and the drinks Anlage 1 lists (only water and milk drinks; alcoholic drinks stay at 20%), hotel accommodation, passenger transport, waste collection, repairs of bicycles, shoes, clothing, and other items in § 10 Abs 2 | 10% | 2026 | https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004873 |
| Second reduced rate: Anlage 2 goods (for example live animals, live plants, firewood), artists, swimming pools, theatre, concerts, museums, film, circus, domestic flights, farm wine, sports event tickets, and the other items in § 10 Abs 3 | 13% | 2026 | https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004873 |
| Jungholz and Mittelberg (§ 10 Abs 4), refer | 19% | 2026 | https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004873 |
| Photovoltaic modules (§ 28 Abs 62): only for supplies 1 Jan 2024 to 31 Mar 2025, so none in 2026 | 0% (expired) | 2024 to Mar 2025 | https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004873 |
| Small business limit, prior year not exceeded and current year not yet exceeded (§ 6 Abs 1 Z 27) | EUR 55,000 | 2026 | https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004873 |
| Tolerance in the year the limit is crossed | 10% (to EUR 60,500) | 2026 | https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004873 |
| Waiver of the exemption binds for at least (§ 6 Abs 3) | 5 calendar years | 2026 | https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004873 |
| EU SME scheme: EU-wide turnover, prior and current year (Art. 6a Binnenmarkt) | EUR 100,000 | 2026 | https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004929 |
| No annual return for a small business with turnover not above this and no tax to pay (§ 21 Abs 6) | EUR 55,000 | 2026 | https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004873 |
| ZM period follows the UVA period: quarterly if prior-year turnover did not exceed this and no monthly UVA was chosen, otherwise monthly | EUR 100,000 | 2026 | https://www.usp.gv.at/themen/steuern-finanzen/umsatzsteuer-ueberblick/weitere-informationen-zur-umsatzsteuer/umsaetze-mit-auslandsbezug/zusammenfassende-meldung-zm.html |
| Quarterly UVA period if prior-year turnover did not exceed; monthly above (§ 21 Abs 2) | EUR 100,000 | 2026 | https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004873 |
| No UVA to file if prior-year turnover did not exceed, and the payment is made in full on time or there is none (UVA regulation) | EUR 55,000 | 2026 | https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10005119 |
| Cash basis (Ist) for other businesses if total turnover in one of the two prior years was not above (§ 17 Abs 2 Z 2) | EUR 110,000 | 2026 | https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004873 |
| Cash-basis business deducts input VAT only once paid, unless prior-year turnover exceeded (§ 12 Abs 1 Z 1) | EUR 2,000,000 | 2026 | https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004873 |
| EU-wide distance sales and e-services below which the place of supply stays in the supplier's member state (Art. 3 Abs 5 Binnenmarkt) | EUR 10,000 | 2026 | https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004929 |
| Annual return on paper allowed for a self-filer whose prior-year turnover did not exceed (no UVA duty; § 2 FinanzOnline-Erklärungsverordnung) | EUR 55,000 | 2026 | https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20005197 |
| Car reasonableness limit, gross purchase cost incl. VAT and NoVA (§ 1 PKW-Angemessenheitsverordnung) | EUR 40,000 | 2026 | https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20003797 |
| Business meals with a documented advertising purpose: deductible for income tax (§ 20 Abs 1 Z 3 EStG) | 50% | 2026 | https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004570 |
| Minimum business use for a purchase to count as made for the business (§ 12 Abs 2) | 10% | 2026 | https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004873 |
| Simplified invoice allowed up to this gross total (§ 11 Abs 6) | EUR 400 | 2026 | https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004873 |
| Domestic invoice must also show the customer's UID if the gross total exceeds (§ 11 Abs 1) | EUR 10,000 | 2026 | https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004873 |
| Car input VAT allowed if used at least this much for commercial passenger transport or rental (§ 12 Abs 2 Z 2 lit b) | 80% | 2026 | https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004873 |
| Reverse charge on mobile phones and integrated circuits, each within the CN codes listed in § 19 Abs 1e lit b, if the invoiced consideration is at least | EUR 5,000 | 2026 | https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004873 |
| Reverse charge on video game consoles (from CN 9504), laptops and tablet computers (from CN 8471 30 00) if the invoiced consideration is at least (§ 19 Abs 1d, § 2 Z 1 UStBBKV). Tested separately from the mobile phone limit; these three goods are added together | EUR 5,000 | 2026 | https://www.ris.bka.gv.at/Dokumente/BgblAuth/BGBLA_2013_II_369/BGBLA_2013_II_369.html |
| First late-payment surcharge (§ 217 Abs 2 BAO); none below EUR 50 (§ 217 Abs 10) | 2% | 2026 | https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10003940 |
| Second and third late-payment surcharge, each (§ 217 Abs 3 BAO) | 1% | 2026 | https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10003940 |
| Late-filing surcharge, up to (§ 135 BAO); none below EUR 50 | 10% | 2026 | https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10003940 |
| VAT interest (Umsatzsteuerzinsen, § 205c BAO), per year above the base rate; none below EUR 50 | 2% | 2026 | https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10003940 |
| OeNB base rate (Basiszinssatz) from 16 September 2026, so VAT interest is 4.03% a year | 2.03% | 2026 | https://www.oenb.at/isawebstat/stabfrage/createReport?lang=DE&report=2.1 |
| Late ZM: surcharge up to 1% of reportable amounts, capped at (Art. 21 Abs 10 Binnenmarkt) | EUR 2,200 | 2026 | https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004929 |
| ZM not filed: coercive penalty up to (U 13a instructions) | EUR 5,000 | 2026 | https://formulare.bmf.gv.at/service/formulare/inter-steuern/pdfd/9999/u13a.pdf |

The rates in § 10 apply in a strict order: 4.9% first, then 10%, then 13%. The 4.9% rate applies only where the goods fall wholly under a combined-nomenclature heading listed in Anlage 3. It never applies to services, so restaurant sales and catering stay at 10% ([BMF food rate page](https://www.bmf.gv.at/rechtsnews/steuern-rechtsnews/aktuelle-infos-und-erlaesse/fachinformationen---umsatzsteuer/umsatzsteuersenkung-auf-ausgewaehlte-nahrungsmittel.html)). For any item not named here, take the rate from § 10 and its annexes, not from memory.

Transition for the 4.9% rate: a down payment received before 1 July 2026 for Anlage 3 food delivered on or after 1 July 2026 is taxed at the rate in force when it is received, and corrected to 4.9% once the delivery is made. The supplier may instead show and tax the down payment at 4.9% on the invoice straight away; then no invoice correction is needed when the rate changes ([BMF food rate FAQ, question 2](https://www.bmf.gv.at/rechtsnews/steuern-rechtsnews/aktuelle-infos-und-erlaesse/fachinformationen---umsatzsteuer/umsatzsteuersenkung-auf-ausgewaehlte-nahrungsmittel.html)).

## The taxable base

### What is taxed (§ 4 and § 16 UStG)

- The base is the consideration net of VAT for each taxable supply (§ 4), plus own use (Eigenverbrauch) of business goods and services. Down payments are taxed when received. Price changes, discounts and bad debts are corrected in the period they happen (§ 16).

### The small business exemption (§ 6 Abs 1 Z 27 and Abs 3 UStG)

- A business whose seat is in Austria or another member state is exempt if its turnover did not exceed EUR 55,000 in the previous calendar year and has not yet exceeded it in the current year.
- The limit is gross: the law says not to compute it on a notional taxable base. Leave out ancillary sales (Hilfsgeschäfte) including the sale of the whole business, and the exempt sales listed in § 6 Abs 1 Z 27 (Z 8 lit d and j, Z 9 lit b and d, Z 10 to 15, Z 17 to 26, Z 28).
- Over the limit: the exemption ends from that moment. Over by no more than 10%: it still applies to 31 December.
- Exempt businesses deduct no input VAT. VAT shown on an invoice anyway is owed (§ 11 Abs 12, KZ 056) until the invoice is corrected.
- **Waiver:** a written declaration to the tax office until the assessment is final. It runs from the start of a calendar year and binds for at least five calendar years. A domestic business revokes it only from the start of a year, by the end of January of that year.
- **EU SME scheme (Art. 6a Binnenmarkt):** an Austrian small business can be exempt in another member state only after an advance notification through the BMF portal, while its EU-wide turnover stays at or below EUR 100,000 in the previous and current year, and once at least one member state confirms the exemption. It then reports turnover per member state each quarter, within one month of the quarter's end. There is no tolerance on the EUR 100,000.

Worked tolerance check (2026): sales January to October EUR 54,500, a November order of EUR 4,000 takes the year to EUR 58,500. The ceiling is 55,000 x 1.1 = EUR 60,500, so 2026 stays exempt, and the business is taxable from 1 January 2027 because 2026 exceeded EUR 55,000. A further sale taking 2026 above EUR 60,500 is taxable from that sale onward.

### Timing basis (§ 17 and § 19 Abs 2 UStG)

- **Accrual basis (Soll):** tax arises at the end of the month of supply. A later invoice defers it by at most one month. No deferral where the tax passes to the customer on a service.
- **Cash basis (Ist):** tax arises at the end of the month of payment, including down payments. It applies to freelance professions and non-accounting traders, and to other businesses (for example landlords) whose total turnover was not above EUR 110,000 in one of the two prior years.
- Foreign currency is converted at the BMF average rate for the period, the latest ECB rate, or the daily rate backed by a bank advice (§ 20 Abs 6).

### Reverse charge (§ 19 UStG)

- **Services and work supplies from a business with no Austrian establishment** to a business customer, or to a public body that is not a business: the customer owes the tax (§ 19 Abs 1 second sentence). Excluded: federal road tolls, the event services in § 3a Abs 11a, and letting of land. The supplier is liable too.
- **Construction (§ 19 Abs 1a):** the customer owes the tax if it was itself commissioned to do the building work, or usually supplies construction services. Labour hire for construction counts.
- **Other cases (§ 19 Abs 1b to 1e):** security ownership, retained title and forced sales of land (KZ 044); scrap, metals, gold, gas and electricity under the § 19 Abs 1d regulations, and, from EUR 5,000 invoiced, video game consoles, laptops and tablet computers (§ 2 Z 1 UStBBKV, BGBl. II Nr. 369/2013) (KZ 032); emission allowances (no minimum) and, from EUR 5,000 invoiced, mobile phones and integrated circuits within the listed CN codes under § 19 Abs 1e (KZ 057); gas, electricity, heat and cooling through networks from a supplier with no Austrian establishment, where the customer is VAT-registered in Austria, under § 19 Abs 1c (KZ 057). Refer if the facts are not on the statement.
- **Goods from an EU business:** an intra-EU acquisition, taxed by the buyer (Art. 1 Binnenmarkt), with input VAT in KZ 065.
- Invoices for supplies where the customer owes the tax show the customer's UID and a note that the tax passes to the customer (§ 11 Abs 1a).

### Input VAT (§ 12 UStG)

- Deductible on a proper invoice for a supply to the business, used at least 10% for business. Cash-basis businesses under EUR 2,000,000 deduct only once they have paid.
- **Down payments:** input VAT on a payment made before the supply is deductible once the invoice is held and the payment has been made (§ 12 Abs 1 Z 1 lit b).
- **Cars, estate cars and motorcycles:** no input VAT on purchase, lease or running costs, even at full business use (§ 12 Abs 2 Z 2 lit b). Exceptions: driving school cars, demonstration cars, cars held for resale, cars used at least 80% for commercial passenger transport or rental, vans on the BMF list, and zero-emission cars (§ 12 Abs 2 Z 2a), within the EUR 40,000 reasonableness limit.
- **Business meals:** default block. If the client proves the meal serves advertising and the business purpose far outweighs everything else, half is deductible for income tax (§ 20 Abs 1 Z 3 EStG). The cost is then not mainly non-deductible, so § 12 Abs 2 Z 2 lit a does not block the input VAT, and it is deducted in full.
- **Travel services bought in for resale** to travellers: no input VAT.
- **Change of use of a capital asset** is corrected under § 12 Abs 10 and 11 in KZ 063. If the facts that decided the deduction on a fixed asset change in the four calendar years after the year of first use, the deduction is corrected for each year of change, one fifth of the asset's input VAT a year. For land (including capitalised costs and major repairs) the period is the 19 years after the year of first use, one twentieth a year. On a sale, the rest of the period is corrected at the latest in the last UVA of that year.
- Unknown VAT status or business share: no deduction until the client answers.

### Exempt supplies

- **Exempt with credit:** input VAT on related costs stays deductible. Exports (§ 7, KZ 011), cross-border transport (§ 6 Abs 1 Z 3, KZ 015), intra-EU supplies of goods to a business with a valid UID (Art. 6 Abs 1 Binnenmarkt, KZ 017, and the ZM). An intra-EU supply stays exempt only if the business has met its duty to file the ZM, or has properly justified its failure to the satisfaction of the authorities (Art. 7 Abs 1 Z 5 Binnenmarkt).
- **Exempt without credit:** medical, insurance, finance, land sales (KZ 019 for land, KZ 020 for others). Business premises letting is exempt unless the landlord opts to tax (§ 6 Abs 2). Input VAT on related costs is lost; a business with both kinds of supply apportions (§ 12 Abs 4 to 6). If material alongside taxable sales, refer (partial exemption).
- **Not taxable in Austria:** a general-rule B2B service to an EU business is taxed where the customer is (§ 3a Abs 6). It goes in neither KZ 000 nor KZ 021, but in the ZM. The Austrian supplier charges no Austrian VAT and shows both VAT numbers and the note that the tax passes to the customer on the invoice (§ 11 Abs 1a).

### Kennzahl map of the 2026 U 30

From the [BMF 2026 U 30 form](https://formulare.bmf.gv.at/service/formulare/inter-Steuern/pdfs/2026/U30.pdf?open=download), read on 26 October 2026, which carries the new 4.9% boxes.

| KZ | Meaning on the form |
|---|---|
| 000 | Total base of supplies and services, incl. down payments, net of VAT |
| 001 | Plus own use (Eigenverbrauch) |
| 021 | Minus sales where the tax passed to the customer |
| 011, 012, 015, 017, 018 | Exempt with credit: exports, processing for export, shipping and aviation, intra-EU supplies, new vehicles to buyers without a UID |
| 019, 016, 020 | Exempt without credit: land, small business, others |
| 022 | Base at 20% |
| 124 | Base at 4.9% |
| 029 | Base at 10% |
| 006 | Base at 13% |
| 037 | Base at 19% (Jungholz and Mittelberg) |
| 052, 007 | Flat-rate farming additional tax (out of scope) |
| 056 | Tax owed on VAT shown wrongly (§ 11 Abs 12 and 14) |
| 057 | Tax owed as recipient (§ 19 Abs 1 second sentence, 1c, 1e) |
| 048 | Tax owed as recipient of construction (§ 19 Abs 1a) |
| 044 | Tax owed under § 19 Abs 1b |
| 032 | Tax owed under § 19 Abs 1d |
| 070, 071 | Intra-EU acquisitions: total base, of which exempt |
| 072, 125, 073, 008, 088 | Acquisitions at 20%, 4.9%, 10%, 13%, 19% |
| 076, 077 | Acquisitions not taxed here (Art. 3 Abs 8) |
| 060 | Total input VAT, without the boxes below |
| 061, 083 | Import VAT paid, import VAT booked on the tax account |
| 065 | Input VAT on intra-EU acquisitions |
| 066, 082, 087, 089 | Input VAT on the tax in KZ 057, 048, 044, 032 |
| 064 | Input VAT on new vehicles from occasional suppliers |
| 062 | Of which not deductible |
| 063 | Correction under § 12 Abs 10 and 11 |
| 067 | Correction of input VAT under § 16 |
| 090 | Other corrections |
| 095 | Payment due (Zahllast) or refund (Überschuss) |

How the boxes work:
- Rate boxes take the base; the form computes the tax. KZ 057, 048, 044 and 032 take the tax itself; its input VAT goes in KZ 066, 082, 087 and 089, so the net is zero with full deduction.
- Price changes (discounts, bad debts) go into the current period, not the old one (§ 16). If a box would turn negative, enter zero and put the amount in KZ 067 or KZ 090.
- KZ 021 holds sales already in KZ 000 where the customer owes the tax, such as construction subcontracts.

### Bank-statement patterns

| Pattern | Treatment |
|---|---|
| Bank fees and interest (ERSTE, RAIFFEISEN, BAWAG, BANK AUSTRIA, HYPO, REVOLUT, WISE); ZINSEN, KREDIT, TILGUNG | Exclude (exempt or outside VAT) |
| FINANZAMT, GEMEINDE, FIRMENBUCH, SVS, ÖGK, WKO, GEHALT, LOHN, insurers (UNIQA, GENERALI, ALLIANZ) | Exclude |
| Energy and telecoms (WIEN ENERGIE, EVN, KELAG, A1, MAGENTA, DREI) | 20%, KZ 060 |
| ÖSTERREICHISCHE POST letters / parcels and couriers (DHL, DPD, GLS) | Letters exempt: exclude. Parcels: 20% |
| ÖBB, WESTBAHN, WIENER LINIEN, taxi, Uber | Rate from the invoice. International flights: exclude |
| ASFINAG, fuel (OMV, BP, SHELL, AVIA, ENI, JET) | Blocked for a car; ask about the vehicle |
| Supermarkets (SPAR, BILLA, HOFER, LIDL, PENNY) and restaurants | Block unless hospitality or a documented advertising meal |
| STEUERBERATER, RECHTSANWALT, NOTAR | 20%, KZ 060 |
| Foreign software and ads (Google, Microsoft, Meta, Adobe from Ireland; Notion, OpenAI, Anthropic, GitHub from outside the EU) | Reverse charge KZ 057 and KZ 066. If the invoice shows Austrian VAT, domestic KZ 060. Unknown entity: ask |
| Stripe or PayPal fees | Exclude (financial) |
| BÜROMIETE / WOHNUNGSMIETE | 20% only if the landlord opted to tax / 10% if VAT is charged |
| UMBUCHUNG, PRIVATEINLAGE, BEHEBUNG | Exclude; ask about cash |

Conservative defaults when the client cannot answer: unknown counterparty country, treat as domestic; unknown whether an EU customer is a business, charge Austrian VAT; unknown rate on a sale, 20%. A foreign hotel bill is excluded: foreign VAT is reclaimed through the EU refund procedure (§ 21 Abs 9), not the UVA.

## Deadlines and filing

- **UVA and payment:** by the 15th of the second month after the period (§ 21 Abs 1). Quarterly: 15 May, 15 August, 15 November, 15 February. A due date on a Saturday, Sunday, public holiday, Good Friday or 24 December moves to the next working day (§ 108 Abs 3 BAO; 15 August 2026 is a Saturday and a holiday, 15 November 2026 is a Sunday) ([BMF deadlines page](https://www.bmf.gv.at/themen/steuern/fristen-verfahren/fristen-faelligkeiten.html)).
- **Period:** monthly if prior-year turnover exceeded EUR 100,000, otherwise quarterly. A quarterly filer can choose monthly for the whole year by filing the January UVA on time (§ 21 Abs 2).
- **No UVA filing** if prior-year turnover did not exceed EUR 55,000 and the payment is made in full on time, or there is none. The business still prepares a statement of the bases on the official form and keeps it with its records, unless the period shows neither a payment nor a refund (§ 21 Abs 1 and the UVA regulation). A refund is claimed only by filing. The business also files when it pays late or short, or when the tax office asks (UVA regulation § 2).
- **Filing route:** electronically through FinanzOnline. Paper only where the filer has no internet access, or, for a self-filed annual return, where prior-year turnover did not exceed EUR 55,000 (§ 2 FinanzOnline-Erklärungsverordnung). Keep a copy of every UVA.
- **Correcting a UVA:** a corrected UVA filed by the due date counts as the UVA itself (§ 21 Abs 1). Later, correct in the annual return or with a self-disclosure.
- **ZM (form U 13, through FinanzOnline):** by the end of the month after each calendar month, or after each quarter for quarterly UVA filers (Art. 21 Abs 3 Binnenmarkt). It covers intra-EU supplies of goods, transfers under call-off stock, and general-rule B2B services where the customer owes the tax. A wrong ZM must be corrected within one month of discovery.
- **Annual U 1:** 30 April of the next year on paper, 30 June through FinanzOnline (§ 134 Abs 1 BAO; [USP filing page](https://www.usp.gv.at/themen/steuern-finanzen/steuerliche-rechte-und-pflichten/weitere-informationen-zu-steuerlichen-rechten-und-pflichten-als-unternehmen/einreichen-von-steuererklaerungen.html)). The 2026 return is due 30 June 2027. A business represented by a tax adviser files later under the quota system (§ 134a BAO). The tax office can extend a deadline in a single case on a reasoned request (§ 134 Abs 2 BAO). A small business with turnover up to EUR 55,000 and no tax to pay files no annual return (§ 21 Abs 6). An additional amount from the assessment does not get a new due date (§ 21 Abs 5).
- **2025 annual U 1, being filed now:** due 30 June 2026 online.

## Penalties and interest

- **Late payment (§ 217 BAO):** 2% of the unpaid amount. A surcharge below EUR 50 is not set (§ 217 Abs 10). A further 1% if still unpaid three months after it became enforceable, and another 1% three months later. No first surcharge if the delay is at most five days (Saturdays, Sundays, public holidays, Good Friday and 24 December not counted) and everything was paid on time in the previous six months (§ 217 Abs 5).
- **Late filing (§ 135 BAO):** up to 10% of the self-computed tax, if the delay is not excusable. Not set below EUR 50.
- **VAT interest (§ 205c BAO):** 2% a year above the base rate (2.03% from 16 September 2026, so 4.03%), on refunds from the 91st day after the UVA arrives, and on additional tax from the 91st day after the UVA due date (from 1 October of the next year where the additional tax comes from the annual return). Not set below EUR 50.
- **Late ZM:** surcharge up to 1% of the reportable amounts, at most EUR 2,200 (Art. 21 Abs 10 Binnenmarkt). Filing can be forced by a coercive penalty of up to EUR 5,000 ([U 13a instructions](https://formulare.bmf.gv.at/service/formulare/inter-steuern/pdfd/9999/u13a.pdf)).
- **Interest on assessed differences (Anspruchszinsen, § 205 BAO)** applies only to income tax and corporate income tax, not to VAT.
- **Self-disclosure (§ 29 FinStrG):** protects only if made before investigations start, with the bases fully disclosed and the tax paid within a month. Made after an audit is announced, it also needs an extra charge of 5% of the additional tax, 15% above EUR 33,000, 20% above EUR 100,000 and 30% above EUR 250,000 (§ 29 Abs 6).
- **Shortfall surcharge (§ 30a FinStrG):** in an audit, the tax office can impose 10% of the additional tax (15% above EUR 50,000) instead of a criminal case, if the additional tax is at most EUR 33,000 a year and EUR 100,000 in total. The taxpayer agrees within 14 days, waives an appeal and pays within one month.

## Cross-border points

- **Place of supply first, then the rate.** A B2B service is taxed where the customer is (§ 3a Abs 6). Special rules (land, events, passenger transport) are not in the ZM; check where they are taxed.
- **Foreign suppliers without an Austrian establishment:** the Austrian business customer reverse-charges (KZ 057 and 066).
- **Non-resident businesses** with taxable Austrian sales register with the Finanzamt Österreich and may appoint a fiscal representative (§ 27 Abs 7); refer. Those who only owe reverse-charge tax with full deduction are assessed only on written request (§ 21 Abs 4). Otherwise they register and file UVAs like an Austrian business unless every Austrian supply is reverse-charged to the customer.
- **Refunds:** an EU business without Austrian sales reclaims Austrian VAT through the EU refund procedure; an Austrian business reclaims foreign VAT electronically (§ 21 Abs 9 and 10).
- **B2C distance sales and e-services** to other member states above the EU-wide threshold go through OSS: refer.
- **EU SME scheme:** see the base section; the EUR 100,000 EU-wide limit has no tolerance.

## Worked examples

### Example 1: IT consultant, monthly UVA for September 2026

An IT consultancy in Vienna on normal taxation, monthly filer (2025 turnover EUR 400,000). September 2026: Austrian sales EUR 30,000 net at 20%; consulting for a German business EUR 12,000 (taxed in Germany, ZM only); a US software subscription of EUR 1,000 (reverse charge); domestic input VAT of EUR 2,400 on proper invoices.

- KZ 022: base 30,000, tax 6,000.
- KZ 057: 1,000 x 20% = 200; the same 200 in KZ 066.
- KZ 060: 2,400.
- KZ 095: 6,000 + 200 - 200 - 2,400 = 3,600, due 15 November 2026. 15 November is a Sunday, so it moves to Monday 16 November.
- ZM for September: 12,000 to the German UID. Due 31 October 2026, a Saturday, and 1 November is a Sunday and a holiday, so it moves to Monday 2 November 2026 (§ 108 Abs 3 BAO).

```oa-check
name: Vienna IT consultancy, September 2026 UVA with reverse charge and ZM
inputs:
  domestic_sales: 30000
  eu_b2b_service: 12000
  us_software: 1000
  input_vat_domestic: 2400
steps:
  - output_vat: domestic_sales * 20 / 100
  - kz057: us_software * 20 / 100
  - kz066: kz057
  - kz095: output_vat + kz057 - kz066 - input_vat_domestic
  - zm_amount: eu_b2b_service
expected:
  output_vat: 6000
  kz057: 200
  kz066: 200
  kz095: 3600
  zm_amount: 12000
```

### Example 2: grocer, Q3 2026 with the new 4.9% rate, paid late

A grocer in Graz, quarterly filer. Q3 2026 (July to September), the first quarter of the new rate: Anlage 3 basic foods EUR 60,000 net at 4.9%; other food EUR 30,000 at 10%; household goods EUR 15,000 at 20%; input VAT EUR 4,500. The payment due 16 November 2026 (15 November is a Sunday) is made on 10 December 2026, more than five days late, so the first 2% surcharge applies.

- KZ 124: 60,000 x 4.9% = 2,940. KZ 029: 30,000 x 10% = 3,000. KZ 022: 15,000 x 20% = 3,000.
- Output VAT 8,940, less input VAT 4,500: KZ 095 is 4,440.
- Surcharge: 4,440 x 2% = 88.80. It is at least EUR 50, so it is set (§ 217 Abs 10 BAO).

```oa-check
name: Graz grocer, Q3 2026 UVA at 4.9%, 10% and 20%, paid late
inputs:
  food_anlage3: 60000
  food_other: 30000
  standard_goods: 15000
  input_vat: 4500
steps:
  - vat_49: food_anlage3 * 49 / 1000
  - vat_10: food_other * 10 / 100
  - vat_20: standard_goods * 20 / 100
  - output_vat: vat_49 + vat_10 + vat_20
  - kz095: output_vat - input_vat
  - surcharge: round(kz095 * 2 / 100, 2)
expected:
  vat_49: 2940
  vat_10: 3000
  vat_20: 3000
  output_vat: 8940
  kz095: 4440
  surcharge: 88.80
```

### Example 3: Quarterly filer, Q3 2026, with the new food rate and a reverse charge

A grocery and catering business in Graz had 2025 turnover of EUR 80,000, so it files quarterly UVAs. For July to September 2026 its net sales are: EUR 18,000 of catering (food served at customers' events), EUR 4,000 of wine and beer served at those events, EUR 8,000 of non-food goods, EUR 8,000 of listed basic foods sold over the counter (all after 30 June 2026), and EUR 5,000 of other food sold over the counter. The catering food is a restaurant supply at 10% (§ 10 Abs 2 Z 1 lit b UStG). The 4.9% rate does not reach it, because § 10 Abs 1a covers only supplies and imports of goods. Wine and beer are not in Anlage 1, so they stay at 20% (§ 10 Abs 1). The rates are: EUR 12,000 at 20% (drinks 4,000 and non-food 8,000), EUR 8,000 at 4.9%, and EUR 23,000 at 10% (catering 18,000 and other food 5,000). It bought online advertising for EUR 1,000 net from an Irish company, which is reverse-charged at 20%. Domestic input VAT on proper invoices is EUR 4,200.

Output VAT is 2,400 + 392 + 2,300 = EUR 5,092. The reverse charge adds EUR 200 output and EUR 200 input, so output VAT is EUR 5,292. Input VAT is 4,200 + 200 = EUR 4,400. The UVA shows a payment of EUR 892. The due date, 15 November 2026, is a Sunday, so the UVA and payment are due Monday 16 November 2026 (§ 108 Abs 3 BAO). If the business pays three weeks late and the five-day grace does not apply, the first late-payment surcharge is 2% of EUR 892, EUR 17.84. It is not set, because it is below EUR 50 (§ 217 Abs 10 BAO).

```oa-check
name: Austria quarterly UVA Q3 2026 with 4.9% food rate and reverse charge
inputs:
  sales_drinks_20: 4000
  sales_nonfood_20: 8000
  sales_food: 8000
  sales_catering_10: 18000
  sales_other_food_10: 5000
  rc_service: 1000
  domestic_input_vat: 4200
steps:
  - sales_20: sales_drinks_20 + sales_nonfood_20
  - sales_10: sales_catering_10 + sales_other_food_10
  - out_20: sales_20 * 0.20
  - out_food: sales_food * 0.049
  - out_10: sales_10 * 0.10
  - rc_vat: rc_service * 0.20
  - output_total: out_20 + out_food + out_10 + rc_vat
  - input_total: domestic_input_vat + rc_vat
  - payable: output_total - input_total
  - first_surcharge: payable * 0.02
expected:
  sales_20: 12000
  sales_10: 23000
  out_20: 2400
  out_food: 392
  out_10: 2300
  output_total: 5292
  input_total: 4400
  payable: 892
  first_surcharge: 17.84
```

### Example 4: Small business crosses the limit, inside and then outside the tolerance

A sole trader in Vienna had 2025 turnover of EUR 48,000 and is exempt in 2026. Sales to 31 October 2026 are EUR 54,500. A EUR 4,000 job on 12 November takes the year to EUR 58,500. That is over EUR 55,000 but within the 10% tolerance (EUR 60,500), so the November job stays exempt and the exemption could run to 31 December; from 1 January 2027 the business is taxable because 2026 exceeded the limit.

On 14 December a further EUR 3,000 sale takes the year to EUR 61,500, above the tolerance by EUR 1,000. The exemption ends from that point (§ 6 Abs 1 Z 27 UStG), so this sale is taxable at 20%. The limit is counted gross, and the client billed EUR 3,000 with no VAT, so the VAT is inside the price: 3,000 x 20 / 120 = EUR 500. From that sale the business charges VAT. Its 2025 turnover did not exceed EUR 100,000, so its period is the quarter, and the EUR 500 is due by 15 February 2027 (a Monday). Because 2025 turnover did not exceed EUR 55,000, it files no UVA if it pays in full by then (UVA-Verordnung § 1); it files one if it pays late or short.

```oa-check
name: Austria small business limit, tolerance and crossing sale (2026)
inputs:
  sales_to_october: 54500
  november_job: 4000
  december_sale: 3000
  limit: 55000
  tolerance_pct: 10
steps:
  - tolerance_ceiling: limit + pct(limit, tolerance_pct)
  - after_november: sales_to_october + november_job
  - november_headroom: tolerance_ceiling - after_november
  - after_december: after_november + december_sale
  - excess_over_ceiling: after_december - tolerance_ceiling
  - vat_in_december_sale: december_sale * 20 / 120
expected:
  tolerance_ceiling: 60500
  after_november: 58500
  november_headroom: 2000
  after_december: 61500
  excess_over_ceiling: 1000
  vat_in_december_sale: 500
```

## Ask the client first

- Are you on normal taxation or the small business exemption? If you waived it, from which year? What was your turnover in 2025 and so far in 2026?
- Monthly or quarterly UVA, and are you on the cash or accrual basis?
- For each foreign supplier: which legal entity invoiced you, and does the invoice show Austrian VAT? For each EU customer: do you hold its valid UID?
- Any Anlage 3 basic foods sold since 1 July 2026, or restaurant and catering sales?
- For each vehicle: ordinary car, zero-emission car or a van on the BMF list?
- Any construction bought or sold, exempt sales, property, or an earlier UVA that was wrong or late?
- Does a tax adviser file for you? It changes the annual deadline.

## Sources

| Source | URL | Read on |
|---|---|---|
| Umsatzsteuergesetz 1994, §§ 1, 3a, 6, 10, 11, 12, 16, 17, 19, 20, 21, 27, 28 (version of 26.10.2026) | https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004873 | 2026-10-26 |
| UStG 1994, Anhang (Binnenmarkt), Art. 6, 6a, 21 | https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004929 | 2026-10-26 |
| Umsatzsteuergesetz 1994, re-read for the merge: §§ 6, 10, 12 Abs 10, 19 Abs 1 and 1c to 1e, 21 Abs 4 and 6, 26 Abs 3, 28 Abs 69 and 70, Anlage 3 (version of 31.10.2026) | https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004873 | 2026-10-31 |
| UStG 1994, Anlage 1 (chapter 22 lists only water and milk drinks) | https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004873&Anlage=1 | 2026-10-31 |
| UStG 1994, Anlage 2 | https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004873&Anlage=2 | 2026-10-31 |
| Bundesabgabenordnung, §§ 134, 205, 217 Abs 5, re-read for the merge (version of 31.10.2026) | https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10003940 | 2026-10-31 |
| Budgetbegleitgesetz 2027-2028, BGBl. I Nr. 62/2026 | https://www.ris.bka.gv.at/Dokumente/BgblAuth/BGBLA_2026_I_62/BGBLA_2026_I_62.html | 2026-10-31 |
| Budgetmaßnahmengesetz 2026, BGBl. I Nr. 43/2026 (Art. 2, UStG change) | https://www.ris.bka.gv.at/Dokumente/BgblAuth/BGBLA_2026_I_43/BGBLA_2026_I_43.html | 2026-10-23 |
| Änderung des Umsatzsteuergesetzes 1994, BGBl. I Nr. 37/2026 (4.9% rate, Anlage 3) | https://www.ris.bka.gv.at/Dokumente/BgblAuth/BGBLA_2026_I_37/BGBLA_2026_I_37.html | 2026-10-23 |
| USP, Umsatzsteuervoranmeldung | https://www.usp.gv.at/themen/steuern-finanzen/umsatzsteuer-ueberblick/weitere-informationen-zur-umsatzsteuer/entstehen-der-steuerschuld-und-pflichten/umsatzsteuervoranmeldung.html | 2026-10-23 |
| USP, Zusammenfassende Meldung (deadline, period table) | https://www.usp.gv.at/themen/steuern-finanzen/umsatzsteuer-ueberblick/weitere-informationen-zur-umsatzsteuer/umsaetze-mit-auslandsbezug/zusammenfassende-meldung-zm.html | 2026-10-31 |
| BMF, U 13a instructions for the ZM (late surcharge, coercive penalty) | https://formulare.bmf.gv.at/service/formulare/inter-steuern/pdfd/9999/u13a.pdf | 2026-10-31 |
| Bundesabgabenordnung, §§ 108, 134, 134a, 135, 205c, 217 | https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10003940 | 2026-10-24 |
| Finanzstrafgesetz, §§ 29, 30a | https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10003898 | 2026-10-26 |
| Verordnung über die Abstandnahme von der Verpflichtung zur Abgabe von Voranmeldungen | https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10005119 | 2026-10-24 |
| Einkommensteuergesetz 1988, § 20 Abs 1 Z 3 | https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004570 | 2026-10-24 |
| FinanzOnline-Erklärungsverordnung, § 2 | https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20005197 | 2026-10-24 |
| PKW-Angemessenheitsverordnung, § 1 | https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20003797 | 2026-10-24 |
| OeNB, base and reference rates | https://www.oenb.at/isawebstat/stabfrage/createReport?lang=DE&report=2.1 | 2026-10-24 |
| BMF, U 30 form 2026 | https://formulare.bmf.gv.at/service/formulare/inter-Steuern/pdfs/2026/U30.pdf?open=download | 2026-10-26 |
| BMF, deadlines and due dates | https://www.bmf.gv.at/themen/steuern/fristen-verfahren/fristen-faelligkeiten.html | 2026-10-26 |
| BMF, VAT cut on selected foods | https://www.bmf.gv.at/rechtsnews/steuern-rechtsnews/aktuelle-infos-und-erlaesse/fachinformationen---umsatzsteuer/umsatzsteuersenkung-auf-ausgewaehlte-nahrungsmittel.html | 2026-10-26 |
| USP, filing tax returns | https://www.usp.gv.at/themen/steuern-finanzen/steuerliche-rechte-und-pflichten/weitere-informationen-zu-steuerlichen-rechten-und-pflichten-als-unternehmen/einreichen-von-steuererklaerungen.html | 2026-10-24 |
| Umsatzsteuerbetrugsbekämpfungsverordnung (UStBBKV), BGBl. II Nr. 369/2013, § 1 and § 2 Z 1, original text | https://www.ris.bka.gv.at/Dokumente/BgblAuth/BGBLA_2013_II_369/BGBLA_2013_II_369.html | 2026-10-31 |
| BMF FAQ on the UStBBKV (separate EUR 5,000 limits) | https://www.bmf.gv.at/themen/steuern/fuer-unternehmen/umsatzsteuer/informationen/faq-umsatzsteuerbetrugsbekaempfungsverordnung-(ustbbkv).html | 2026-10-31 |
| BMF form U 30 for 2026 (KZ 032 and 089 name consoles, laptops and tablets under § 19 Abs 1d) | https://formulare.bmf.gv.at/service/formulare/inter-Steuern/pdfs/2026/U30.pdf?open=download | 2026-10-31 |

Not yet confirmed: the current consolidated UStBBKV § 2 and the BGBl. II Nr. 120/2014 changes to it were not read, so the laptop and tablet rule rests on the original text, the 2026 U 30 and the BMF FAQ; the BMF van list (Kleinbus and Kleinlastkraftwagen regulation) and any upper cap above EUR 40,000 for zero-emission cars, which are BMF guidance not read today; the EUR 40 gift threshold for own use, which is in the VAT guidelines, not the statute; the 2026 U 30a filling instructions (the BMF form server did not return the file); three rules from the old version that the statute does not state: that input VAT on start-up costs before the first sale is deductible (UStR guidance, not read today), that a new business with no prior year files monthly from the start if it expects turnover above EUR 100,000 (§ 21 Abs 2 tests only the prior year), and that a domestic reverse-charge invoice is due by the 15th of the month after the supply (the statute sets that deadline only for intra-EU supplies of goods, Art. 11 Abs 1 Binnenmarkt).

This skill is general information, not tax advice. Have a Steuerberater check a return before it is filed.

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
