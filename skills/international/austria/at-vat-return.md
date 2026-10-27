---
name: at-vat-return
description: "Austrian VAT (Umsatzsteuer) for tax year 2026, worked box by box: how to turn a business's bank statement and invoices into the advance return (Umsatzsteuervoranmeldung, UVA, form U 30) and the annual return (U 1) under the Umsatzsteuergesetz 1994 as in force on 26 October 2026. Covers the 20%, 13% and 10% rates, the 4.9% rate on listed basic foods from 1 July 2026, the end of the 0% photovoltaic rate, the small business exemption (EUR 55,000 with the 10% tolerance) and the EU SME scheme (EUR 100,000 EU-wide), monthly or quarterly UVA periods, the 15th of the second following month, the U 1 by 30 April or 30 June, reverse charge, the recapitulative statement (ZM), the Kennzahl map, input VAT blocks, late-payment and late-filing surcharges, VAT interest and self-disclosure. Trigger on: prepare UVA, Austrian VAT return, Umsatzsteuer, U 30, Kennzahl, Kleinunternehmer, ZM Austria. Out of scope: income tax (at-income-tax), corporate tax (at-corporate-income-tax), non-residents and treaties (at-cross-border); the short overview is austria-vat-return."
version: 0.2
jurisdiction: AT
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-26
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Austrian VAT return: the UVA (U 30) and the annual return (U 1), 2026

This skill turns a business's bank statement and invoices into the Austrian VAT advance return (Umsatzsteuervoranmeldung, UVA, form U 30) and the annual VAT return (Umsatzsteuererklärung, U 1) for tax year 2026. The law is the Umsatzsteuergesetz 1994 (UStG) and its Binnenmarkt annex, both read on RIS in the version of 26 October 2026, with the Bundesabgabenordnung (BAO) for deadlines and surcharges. The VAT year is the calendar year.

## Who this applies to

- **In:** sole traders, partnerships and companies that make supplies in Austria (§ 1 Abs 1 Z 1 and 2 UStG), whether they are on normal taxation or deciding whether the small business exemption applies.
- **The tax debtor** is the supplier (§ 19 Abs 1 UStG), except where the tax passes to the customer (reverse charge, see the base section).
- **Small businesses** with turnover up to EUR 55,000 are exempt unless they opt out (§ 6 Abs 1 Z 27 UStG). They charge no VAT and deduct none.
- **Out of scope, refer:** the one-stop shop (OSS), VAT groups (Organschaft), the margin scheme, travel services (§ 23 UStG), flat-rate farming (§ 22 UStG), partial exemption apportionment, property sales and opted lettings, fiscal representation, Jungholz and Mittelberg.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source URL |
|---|---|---|---|
| Standard rate (§ 10 Abs 1) | 20% | 2026 | https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004873 |
| Listed basic foods in Anlage 3, deliveries and imports only, from 1 July 2026 (§ 10 Abs 1a, BGBl. I Nr. 37/2026) | 4.9% | 2026 (from 1 July) | https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004873 |
| Reduced rate: Anlage 1 goods (most food, books, newspapers), residential letting, restaurant food and other items in § 10 Abs 2 | 10% | 2026 | https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004873 |
| Second reduced rate: Anlage 2 goods (for example live plants, firewood) and the other items in § 10 Abs 3 | 13% | 2026 | https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004873 |
| Jungholz and Mittelberg (§ 10 Abs 4), refer | 19% | 2026 | https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004873 |
| Photovoltaic modules (§ 28 Abs 62): only for supplies 1 Jan 2024 to 31 Mar 2025, so none in 2026 | 0% (expired) | 2024 to Mar 2025 | https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004873 |
| Small business limit, prior year not exceeded and current year not yet exceeded (§ 6 Abs 1 Z 27) | EUR 55,000 | 2026 | https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004873 |
| Tolerance in the year the limit is crossed | 10% | 2026 | https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004873 |
| Waiver of the exemption binds for at least (§ 6 Abs 3) | 5 calendar years | 2026 | https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004873 |
| EU SME scheme: EU-wide turnover, prior and current year (Art. 6a Binnenmarkt) | EUR 100,000 | 2026 | https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004929 |
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
| Reverse charge on mobile phones, chips, tablets and laptops if the invoiced consideration is at least (§ 19 Abs 1e) | EUR 5,000 | 2026 | https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004873 |
| First late-payment surcharge (§ 217 Abs 2 BAO); none below EUR 50 (§ 217 Abs 10) | 2% | 2026 | https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10003940 |
| Second and third late-payment surcharge, each (§ 217 Abs 3 BAO) | 1% | 2026 | https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10003940 |
| Late-filing surcharge, up to (§ 135 BAO); none below EUR 50 | 10% | 2026 | https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10003940 |
| VAT interest (Umsatzsteuerzinsen, § 205c BAO), per year above the base rate; none below EUR 50 | 2% | 2026 | https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10003940 |
| OeNB base rate (Basiszinssatz) from 16 September 2026, so VAT interest is 4.03% a year | 2.03% | 2026 | https://www.oenb.at/isawebstat/stabfrage/createReport?lang=DE&report=2.1 |
| Late ZM: surcharge up to 1% of reportable amounts, capped at (Art. 21 Abs 10 Binnenmarkt) | EUR 2,200 | 2026 | https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004929 |

The rates in § 10 apply in a strict order: 4.9% first, then 10%, then 13%. The 4.9% rate applies only where the goods fall wholly under a combined-nomenclature heading listed in Anlage 3. It never applies to services, so restaurant sales and catering stay at 10% ([BMF food rate page](https://www.bmf.gv.at/rechtsnews/steuern-rechtsnews/aktuelle-infos-und-erlaesse/fachinformationen---umsatzsteuer/umsatzsteuersenkung-auf-ausgewaehlte-nahrungsmittel.html)). For any item not named here, take the rate from § 10 and its annexes, not from memory.

## The taxable base

### The small business exemption (§ 6 Abs 1 Z 27 and Abs 3 UStG)

- A business whose seat is in Austria or another member state is exempt if its turnover did not exceed EUR 55,000 in the previous calendar year and has not yet exceeded it in the current year.
- The limit is gross: the law says not to compute it on a notional taxable base. Leave out ancillary sales (Hilfsgeschäfte) including the sale of the whole business, and the exempt sales listed in § 6 Abs 1 Z 27 (Z 8 lit d and j, Z 9 lit b and d, Z 10 to 15, Z 17 to 26, Z 28).
- Over the limit: the exemption ends from that moment. Over by no more than 10%: it still applies to 31 December.
- Exempt businesses deduct no input VAT. VAT shown on an invoice anyway is owed (§ 11 Abs 12, KZ 056) until the invoice is corrected.
- **Waiver:** a written declaration to the tax office until the assessment is final. It runs from the start of a calendar year and binds for at least five calendar years. A domestic business revokes it only from the start of a year, by the end of January of that year.
- **EU SME scheme (Art. 6a Binnenmarkt):** an Austrian small business can be exempt in another member state only after an advance notification through the BMF portal, while its EU-wide turnover stays at or below EUR 100,000 in the previous and current year. It then reports turnover per member state each quarter, within one month of the quarter's end. There is no tolerance on the EUR 100,000.

Worked tolerance check (2026): sales January to October EUR 54,500, a November order of EUR 4,000 takes the year to EUR 58,500. The ceiling is 55,000 x 1.1 = EUR 60,500, so 2026 stays exempt, and the business is taxable from 1 January 2027 because 2026 exceeded EUR 55,000. A further sale taking 2026 above EUR 60,500 is taxable from that sale onward.

### Timing basis (§ 17 and § 19 Abs 2 UStG)

- **Accrual basis (Soll):** tax arises at the end of the month of supply. A later invoice defers it by at most one month. No deferral where the tax passes to the customer on a service.
- **Cash basis (Ist):** tax arises at the end of the month of payment, including down payments. It applies to freelance professions and non-accounting traders, and to other businesses (for example landlords) whose total turnover was not above EUR 110,000 in one of the two prior years.
- Foreign currency is converted at the BMF average rate for the period, the latest ECB rate, or the daily rate backed by a bank advice (§ 20 Abs 6).

### Reverse charge (§ 19 UStG)

- **Services and work supplies from a business with no Austrian establishment** to a business customer: the customer owes the tax (§ 19 Abs 1 second sentence). Excluded: federal road tolls, the event services in § 3a Abs 11a, and letting of land. The supplier is liable too.
- **Construction (§ 19 Abs 1a):** the customer owes the tax if it was itself commissioned to do the building work, or usually supplies construction services. Labour hire for construction counts.
- **Other cases (§ 19 Abs 1b to 1e):** security ownership, retained title and forced sales of land (KZ 044); scrap, metals, gold, gas and electricity under the § 19 Abs 1d regulation (KZ 032); mobile phones, chips, tablets and laptops from EUR 5,000 invoiced under § 19 Abs 1e (KZ 057). Refer if the facts are not on the statement.
- **Goods from an EU business:** an intra-EU acquisition, taxed by the buyer (Art. 1 Binnenmarkt), with input VAT in KZ 065.
- Invoices for supplies where the customer owes the tax show the customer's UID and a note that the tax passes to the customer (§ 11 Abs 1a).

### Input VAT (§ 12 UStG)

- Deductible on a proper invoice for a supply to the business, used at least 10% for business. Cash-basis businesses under EUR 2,000,000 deduct only once they have paid.
- **Cars, estate cars and motorcycles:** no input VAT on purchase, lease or running costs, even at full business use (§ 12 Abs 2 Z 2 lit b). Exceptions: driving school cars, demonstration cars, cars held for resale, cars used at least 80% for commercial passenger transport or rental, vans on the BMF list, and zero-emission cars (§ 12 Abs 2 Z 2a), within the EUR 40,000 reasonableness limit.
- **Business meals:** default block. If the client proves the meal serves advertising and the business purpose far outweighs everything else, half is deductible for income tax (§ 20 Abs 1 Z 3 EStG). The cost is then not mainly non-deductible, so § 12 Abs 2 Z 2 lit a does not block the input VAT, and it is deducted in full.
- **Travel services bought in for resale** to travellers: no input VAT.
- **Change of use of a capital asset** is corrected under § 12 Abs 10 and 11 in KZ 063. For land the period is the 19 years after the year of first use, one twentieth a year.
- Unknown VAT status or business share: no deduction until the client answers.

### Exempt supplies

- **Exempt with credit:** exports (§ 7, KZ 011), intra-EU supplies of goods to a business with a valid UID (Art. 6 Abs 1 Binnenmarkt, KZ 017, and the ZM). An intra-EU supply stays exempt only if the ZM is filed correctly, or the failure is justified to the tax office.
- **Exempt without credit:** medical, insurance, finance, land sales (KZ 019 for land, KZ 020 for others). Business premises letting is exempt unless the landlord opts to tax (§ 6 Abs 2). If material alongside taxable sales, refer (partial exemption).
- **Not taxable in Austria:** a general-rule B2B service to an EU business is taxed where the customer is (§ 3a Abs 6). It goes in neither KZ 000 nor KZ 021, but in the ZM.

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

- **UVA and payment:** by the 15th of the second month after the period (§ 21 Abs 1). Quarterly: 15 May, 15 August, 15 November, 15 February. A due date on a Saturday, Sunday, public holiday, Good Friday or 24 December moves to the next working day ([BMF deadlines page](https://www.bmf.gv.at/themen/steuern/fristen-verfahren/fristen-faelligkeiten.html)).
- **Period:** monthly if prior-year turnover exceeded EUR 100,000, otherwise quarterly. A quarterly filer can choose monthly for the whole year by filing the January UVA on time (§ 21 Abs 2).
- **No UVA filing** if prior-year turnover did not exceed EUR 55,000 and the payment is made in full on time, or there is none. The business still prepares a statement of the bases on the official form and keeps it with its records, unless the period shows neither a payment nor a refund (§ 21 Abs 1 and the UVA regulation). A refund is claimed only by filing.
- **Filing route:** electronically through FinanzOnline. Paper only where the filer has no internet access, or, for a self-filed annual return, where prior-year turnover did not exceed EUR 55,000 (§ 2 FinanzOnline-Erklärungsverordnung). Keep a copy of every UVA.
- **Correcting a UVA:** a corrected UVA filed by the due date counts as the UVA itself (§ 21 Abs 1). Later, correct in the annual return or with a self-disclosure.
- **ZM:** by the end of the month after each calendar month, or after each quarter for quarterly UVA filers (Art. 21 Abs 3 Binnenmarkt). It covers intra-EU supplies of goods, transfers under call-off stock, and general-rule B2B services where the customer owes the tax. A wrong ZM must be corrected within one month of discovery.
- **Annual U 1:** 30 April of the next year on paper, 30 June through FinanzOnline ([USP filing page](https://www.usp.gv.at/themen/steuern-finanzen/steuerliche-rechte-und-pflichten/weitere-informationen-zu-steuerlichen-rechten-und-pflichten-als-unternehmen/einreichen-von-steuererklaerungen.html)). A business represented by a tax adviser files later under the quota system (§ 134a BAO). A small business with turnover up to EUR 55,000 and no tax to pay files no annual return (§ 21 Abs 6). An additional amount from the assessment does not get a new due date (§ 21 Abs 5).
- **2025 annual U 1, being filed now:** due 30 June 2026 online.

## Penalties and interest

- **Late payment (§ 217 BAO):** 2% of the unpaid amount. A surcharge below EUR 50 is not set (§ 217 Abs 10). A further 1% if still unpaid three months after it became enforceable, and another 1% three months later. No first surcharge if the delay is at most five days and everything was paid on time in the previous six months.
- **Late filing (§ 135 BAO):** up to 10% of the self-computed tax, if the delay is not excusable. Not set below EUR 50.
- **VAT interest (§ 205c BAO):** 2% a year above the base rate (2.03% from 16 September 2026, so 4.03%), on refunds from the 91st day after the UVA arrives, and on additional tax from the 91st day after the UVA due date (from 1 October of the next year where the additional tax comes from the annual return). Not set below EUR 50.
- **Late ZM:** surcharge up to 1% of the reportable amounts, at most EUR 2,200 (Art. 21 Abs 10 Binnenmarkt).
- **Self-disclosure (§ 29 FinStrG):** protects only if made before investigations start, with the bases fully disclosed and the tax paid within a month. Made after an audit is announced, it also needs an extra charge of 5% of the additional tax, 15% above EUR 33,000, 20% above EUR 100,000 and 30% above EUR 250,000 (§ 29 Abs 6).
- **Shortfall surcharge (§ 30a FinStrG):** in an audit, the tax office can impose 10% of the additional tax (15% above EUR 50,000) instead of a criminal case, if the additional tax is at most EUR 33,000 a year and EUR 100,000 in total. The taxpayer agrees within 14 days, waives an appeal and pays within one month.

## Cross-border points

- **Place of supply first, then the rate.** A B2B service is taxed where the customer is (§ 3a Abs 6). Special rules (land, events, passenger transport) are not in the ZM; check where they are taxed.
- **Foreign suppliers without an Austrian establishment:** the Austrian business customer reverse-charges (KZ 057 and 066).
- **Non-resident businesses** with taxable Austrian sales register with the Finanzamt Österreich and may appoint a fiscal representative (§ 27 Abs 7); refer. Those who only owe reverse-charge tax with full deduction are assessed only on request (§ 21 Abs 6).
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

## Ask the client first

- Are you on normal taxation or the small business exemption? If you waived it, from which year? What was your turnover in 2025 and so far in 2026?
- Monthly or quarterly UVA, and are you on the cash or accrual basis?
- For each foreign supplier: which legal entity invoiced you, and does the invoice show Austrian VAT? For each EU customer: do you hold its valid UID?
- Any Anlage 3 basic foods sold since 1 July 2026, or restaurant and catering sales?
- For each vehicle: ordinary car, zero-emission car or a van on the BMF list?
- Any construction bought or sold, exempt sales, property, or an earlier UVA that was wrong or late?

## Sources

| Source | URL | Read on |
|---|---|---|
| Umsatzsteuergesetz 1994, §§ 1, 3a, 6, 10, 11, 12, 16, 17, 19, 20, 21, 27, 28 (version of 26.10.2026) | https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004873 | 2026-10-26 |
| UStG 1994, Anhang (Binnenmarkt), Art. 6, 6a, 21 | https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004929 | 2026-10-26 |
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

Not yet confirmed: the BMF van list (Kleinbus and Kleinlastkraftwagen regulation) and any upper cap above EUR 40,000 for zero-emission cars, which are BMF guidance not read today; the EUR 40 gift threshold for own use, which is in the VAT guidelines, not the statute; the 2026 U 30a filling instructions (the BMF form server did not return the file).

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
