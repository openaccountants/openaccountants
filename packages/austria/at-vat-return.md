---
name: at-vat-return
description: Use this skill whenever asked to prepare, review, or classify transactions for an Austrian VAT return (Umsatzsteuervoranmeldung / UVA) or annual declaration (Umsatzsteuererklärung / U1) for a self-employed individual or small business in Austria. Trigger on phrases like "prepare UVA", "Austrian VAT return", "Umsatzsteuer", "classify transactions for Austrian VAT", or any request involving Austria VAT filing. This skill covers Austria only, standard regime (Regelbesteuerung). Kleinunternehmerregelung, partial exemption, margin scheme (Differenzbesteuerung), and VAT groups (Organschaft) are in the refusal catalogue. MUST be loaded alongside BOTH vat-workflow-base v0.1 or later AND eu-vat-directive v0.1 or later. ALWAYS read this skill before touching any Austrian VAT work.
jurisdiction: AT
tax_year: 2026
last_updated: 2026-09-22
review_status: pending_review
drafted_by: OpenAccountants
approved_by: pending
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Austrian VAT return: the Umsatzsteuervoranmeldung (U 30) and the annual return (U 1)

How to classify an Austrian bank statement for VAT and fill in the VAT advance return (Umsatzsteuervoranmeldung, UVA, form U 30) and the annual return (form U 1) on the normal scheme (Regelbesteuerung). Figures are for tax year 2026. Austria's tax year is the calendar year. Every Kennzahl (KZ, box code) below comes from the Finance Ministry's 2026 U 30 form, version of 13 March 2026, which already carries the new 4.9% rate boxes: https://formulare.bmf.gv.at/service/formulare/inter-Steuern/pdfs/2026/U30.pdf?open=download The ministry's filling instructions for 2026 (U 30a) are dated 20 August 2025, before the 4.9% rate existed, so they do not mention its boxes: https://formulare.bmf.gv.at/service/formulare/inter-Steuern/pdfd/2026/U30a.pdf

## Section 1: Quick reference

**Quick reference field table**

| Field | Value |
| --- | --- |
| Country | Austria (Republik Österreich) |
| Rates | Four rates from 1 July 2026: see the rates table |
| Return forms | U 30 (Umsatzsteuervoranmeldung, monthly or quarterly); U 1 (Umsatzsteuererklärung, annual) |
| Filing portal | FinanzOnline. Paper form U 30 only if the business has no internet access |
| Authority | Finanzamt Österreich (Finanzamt für Großbetriebe for large businesses) |
| Deadline | UVA and payment: 15th of the second month after the period. Annual return: 30 April on paper, 30 June via FinanzOnline |
| Scope | Regelbesteuerung only; refusals in Section 2 |

**VAT rates in 2026**

| What | Rate | Note |
| --- | --- | --- |
| Source | all figures below | https://www.usp.gv.at/themen/steuern-finanzen/umsatzsteuer-ueberblick/steuersaetze-und-steuerbefreiungen-der-umsatzsteuer.html |
| Standard rate (Normalsteuersatz), § 10 UStG | 20% | "Der Normalsteuersatz der Umsatzsteuer beträgt 20 Prozent." |
| Selected basic foods listed by customs code, such as bread, butter, eggs, milk. Deliveries only, from 1 July 2026 | 4.9% | "Der 4,9-prozentige Steuersatz gilt für ausgewählte Nahrungsmittel, wie z.B. Brot, Butter, Eier, Milch." Page updated 1 July 2026 |
| Residential letting, accommodation, camping pitches, waste collection, books, newspapers, magazines, other food | 10% | "Der 10-prozentige Steuersatz gilt z.B. für: Die Vermietung zu Wohnzwecken" |
| Live animals, live plants, firewood, artists' turnover, film and circus shows, sports event tickets | 13% | "Der 13-prozentige Steuersatz gilt z.B. für Die Lieferung von lebenden Tieren" |

The USP page gives examples; the full lists are in § 10 UStG. Restaurant and catering services are outside the 4.9% rate (ministry FAQ): https://www.bmf.gv.at/rechtsnews/steuern-rechtsnews/aktuelle-infos-und-erlaesse/fachinformationen---umsatzsteuer/umsatzsteuersenkung-auf-ausgewaehlte-nahrungsmittel.html

**More 10% examples from the federal citizens' portal**

| What | Rate | Note |
| --- | --- | --- |
| Source | all figures below | https://www.oesterreich.gv.at/lexicon/M/Seite.991672.html |
| Medicines, use of public transport, plus the items above | 10% | "ermäßigter Mehrwertsteuersatz von 10 Prozent . Dazu gehören z.B. Lebensmittel, Medikamente, Bücher". Page updated 11 September 2026 |

**UVA filing: who files and how often**

| Prior-year turnover | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.usp.gv.at/themen/steuern-finanzen/umsatzsteuer-ueberblick/weitere-informationen-zur-umsatzsteuer/entstehen-der-steuerschuld-und-pflichten/umsatzsteuervoranmeldung.html |
| Monthly UVA if prior-year turnover exceeded | EUR 100,000 | "Kalenderjahr 100.000 Euro überstiegen haben, sind zur monatlichen Abgabe". A new business estimating more than this in its first year files monthly from the start (https://www.usp.gv.at/themen/steuern-finanzen/umsatzsteuer-ueberblick/umsatzsteuervoranmeldung-und-umsatzsteuererklaerung.html) |
| Quarterly UVA if prior-year turnover exceeded this, up to the monthly limit | EUR 55,000 | "Übersteigt der Vorjahresumsatz 55.000 Euro, aber nicht 100.000 Euro, sind vierteljährlich". A quarterly filer may choose monthly by filing a UVA for January on time |
| No UVA to file if prior-year turnover did not exceed | EUR 55,000 | "Wird die Umsatzgrenze von 55.000 Euro nicht überschritten". Exceptions: the tax office orders it, there is a refund (Überschuss), or the payment is late or short |

Below the lower band the business still keeps an internal return ("interne Voranmeldung") each period, and a refund needs a filed UVA (U 30a).

**Kennzahl map of the 2026 U 30 (the boxes you will use)**

| KZ | Meaning on the form | Rate |
| --- | --- | --- |
| Source | all figures below | https://formulare.bmf.gv.at/service/formulare/inter-Steuern/pdfs/2026/U30.pdf?open=download |
| 000 | Total tax base of supplies and services, incl. down payments, net of VAT | |
| 001 | Plus own use (Eigenverbrauch, § 1 Abs 1 Z 2, § 3 Abs 2, § 3a Abs 1a) | |
| 021 | Minus sales where the tax passed to the customer (§ 19 Abs 1 second sentence, Abs 1a to 1e) | |
| 011 | Exempt with credit: exports (§ 7) | |
| 012 | Exempt with credit: Lohnveredelung (§ 8) | |
| 015 | Exempt with credit: § 6 Abs 1 Z 2 to 6, § 23 Abs 5 (shipping, aviation, cross-border passenger transport and similar) | |
| 017 | Exempt with credit: intra-EU supplies of goods (Art. 6 Abs 1) | |
| 018 | Intra-EU supplies of new vehicles to buyers without a UID number or by occasional vehicle suppliers (Art. 2) | |
| 019 | Exempt without credit: land (§ 6 Abs 1 Z 9 lit a) | |
| 016 | Exempt without credit: small business (§ 6 Abs 1 Z 27) | |
| 020 | Other exempt without credit | |
| 022 | Taxable at the standard rate: tax base | 20% |
| 124 | Taxable at the reduced food rate: tax base (new on the 2026 form) | 4.9% |
| 029 | Taxable at the reduced rate: tax base | 10% |
| 006 | Taxable at the reduced rate: tax base | 13% |
| 037 | Jungholz and Mittelberg rate: tax base | 19% |
| 052, 007 | Additional tax for flat-rate farms and forestry (out of scope) | |
| 056 | Tax owed under § 11 Abs 12 and 14, § 16 Abs 2, Art. 7 Abs 4 (e.g. tax shown wrongly on an invoice) | |
| 057 | Tax owed as recipient under § 19 Abs 1 second sentence, Abs 1c, 1e, Art. 25 Abs 5: services from foreign businesses, EU or non-EU | |
| 048 | Tax owed as recipient of construction services (§ 19 Abs 1a, Bauleistungen) | |
| 044 | Tax owed under § 19 Abs 1b (security and retained title, land in forced sale) | |
| 032 | Tax owed under § 19 Abs 1d (scrap, laptops, tablets, gas, electricity, metals, investment gold and others) | |
| 070 | Intra-EU acquisitions: total tax base | |
| 071 | Of which exempt (Art. 6 Abs 2) | |
| 072 | Intra-EU acquisitions at the standard rate: tax base | 20% |
| 125 | Intra-EU acquisitions at the reduced food rate: tax base (new on the 2026 form) | 4.9% |
| 073 | Intra-EU acquisitions at the reduced rate: tax base | 10% |
| 008 | Intra-EU acquisitions at the reduced rate: tax base | 13% |
| 088 | Intra-EU acquisitions, Jungholz and Mittelberg rate | 19% |
| 076, 077 | Acquisitions under Art. 3 Abs 8 second sentence not taxed here | |
| 060 | Total input VAT (Vorsteuer), without the amounts in the boxes below | |
| 061 | Input VAT: import VAT paid (§ 12 Abs 1 Z 2 lit a) | |
| 083 | Input VAT: import VAT owed and booked on the tax account (§ 12 Abs 1 Z 2 lit b) | |
| 065 | Input VAT from intra-EU acquisitions | |
| 066 | Input VAT on the tax in KZ 057 | |
| 082 | Input VAT on the tax in KZ 048 (construction) | |
| 087 | Input VAT on the tax in KZ 044 | |
| 089 | Input VAT on the tax in KZ 032 | |
| 064 | Input VAT, new vehicles supplied by occasional suppliers (Art. 2) | |
| 062 | Of which not deductible (§ 12 Abs 3 with Abs 4 and 5) | |
| 063 | Correction under § 12 Abs 10 and 11 (change of use) | |
| 067 | Correction of input VAT under § 16 (changes in consideration) | |
| 090 | Other corrections (sonstige Berichtigungen) | |
| 095 | Payment due (Zahllast) or refund (Überschuss): one box for both | |

How the boxes work (form and U 30a):
- Rate boxes take the base, with the tax in a second column. Boxes 057, 048, 044 and 032 take the TAX; its input VAT goes in 066, 082, 087 and 089. Net zero with full deduction.
- There is no "total output VAT" box (the legacy KZ 083 is import VAT).
- A box that would turn negative after price changes gets zero; the negative goes to KZ 067 (input VAT) or KZ 090 (output VAT).
- Import VAT booked on the tax account is paid separately (slip marked "EU"); only its deduction goes in KZ 083.
- Mobile phones and integrated circuits: tax passes to the business customer from the amount in the next table (supplier KZ 021, customer KZ 057 and KZ 066).

**U 30a instructions for 2026**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://formulare.bmf.gv.at/service/formulare/inter-Steuern/pdfd/2026/U30a.pdf |
| Mobile phones and chips: reverse charge from an invoiced consideration of | EUR 5,000 | "wenn das in der Rechnung ausgewiesene Entgelt mindestens 5.000 Euro beträgt" |

**Conservative defaults: Austria-specific**

| Ambiguity | Default |
| --- | --- |
| Unknown rate on a sale | Standard rate |
| Unknown VAT status of a purchase | Not deductible |
| Unknown counterparty country | Domestic Austria |
| Unknown B2B vs B2C for EU customer | B2C, charge Austrian VAT at the standard rate |
| Unknown business-use proportion | No recovery |
| Unknown SaaS billing entity | Reverse charge from abroad, KZ 057 and KZ 066 |
| Unknown blocked-input status | Blocked |
| Unknown whether transaction is in scope | In scope |

**Red flag thresholds**

Use the red-flag thresholds in `vat-workflow-base`. The legacy amounts here were internal review settings, not Austrian law.

## Section 2: Required inputs and refusal catalogue

### Required inputs

**Minimum viable**: bank statement for the period. Acceptable from: Erste Bank, Raiffeisen, BAWAG, Bank Austria (UniCredit), Oberbank, Hypo banks, easybank, Revolut Business, Wise Business, N26, or any other.

**Recommended**: sales invoices (especially intra-EU and reverse charge), purchase invoices, the client's UID-Nummer (ATU followed by 8 digits).

**Ideal**: invoice register, prior period UVA, tax account (Abgabenkonto) balance.

### Austria-specific refusal catalogue

**Small business exemption (Kleinunternehmerregelung, regime since 1 January 2025)**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.usp.gv.at/themen/steuern-finanzen/umsatzsteuer-ueberblick/weitere-informationen-zur-umsatzsteuer/weitere-steuertatbestaende-und-befreiungen/kleinunternehmen.html |
| Small business limit: not exceeded in the previous NOR in the current calendar year | EUR 55,000 | "Kleinunternehmergrenze in Höhe von 55.000 Euro (bis 31. Dezember 2024: 35.000 Euro) wurde weder im vorangegangenen noch im laufenden Kalenderjahr überschritten" |
| Tolerance in the current year | 10% | "wenn die Grenze um nicht mehr als 10 Prozent überschritten wird" |
| Old limit up to 31 December 2024, net, for history only | EUR 35,000 | "bis 31. Dezember 2024: 35.000 Euro" |

The limit is gross: the whole agreed consideration counts ("es ist das gesamte vereinbarte Entgelt zu berücksichtigen"). Within the tolerance the exemption lasts to year end and is lost from the next year; beyond it, it ends with the sale that crosses the limit. An exempt business files no UVA and no annual return and has no input deduction. A waiver (form U12) binds for five years.

- **R-AT-1: Kleinunternehmerregelung.** Trigger: the client is under the exemption above (§ 6 Abs 1 Z 27 UStG). If it was waived, confirm from which year and continue.
- **R-AT-2: Partial exemption (Vorsteueraufteilung).** Mixed taxable and exempt supplies require apportionment under § 12 Abs 4 to 6 UStG. Please use a Steuerberater. (Trigger: both taxable and exempt supplies, non-de-minimis.)
- **R-AT-3: Differenzbesteuerung (margin scheme).** Requires per-item margin computation. Out of scope. (Trigger: second-hand goods, art, antiques.)
- **R-AT-4: Organschaft (VAT group).** Requires consolidation. Out of scope. (Trigger: client is part of an Organschaft.)
- **R-AT-5: Fiscal representative.** Non-resident with fiscal representative: out of scope.
- **R-AT-6: Real estate (Grundstücksumsätze).** Property sales and opted lettings: use a Steuerberater.
- **R-AT-7: Jungholz/Mittelberg special rate.** The rate in KZ 037 in the Kennzahl map requires specific handling. Flag for Steuerberater. (Trigger: client operates in Jungholz or Mittelberg.)
- **R-AT-8: Income tax instead of USt.** This Guide handles Austrian USt only. For income tax use `at-income-tax`; for corporate tax `at-corporate-income-tax`.

## Section 3: Supplier pattern library (the lookup table)

Match by case-insensitive substring. If none match, fall through to Section 5. Domestic input VAT goes in KZ 060.

### 3.1 Austrian banks (fees exempt: exclude)

**Austrian banks table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| ERSTE BANK, SPARKASSE | EXCLUDE for bank charges | Financial service, exempt |
| RAIFFEISEN, RAIFFEISENBANK | EXCLUDE for bank charges | Same |
| BAWAG, BAWAG PSK | EXCLUDE for bank charges | Same |
| BANK AUSTRIA, UNICREDIT AT | EXCLUDE for bank charges | Same |
| OBERBANK, BKS BANK, BTV | EXCLUDE for bank charges | Same |
| HYPO, HYPO TIROL, HYPO NOE | EXCLUDE for bank charges | Same |
| EASYBANK | EXCLUDE for bank charges | Same |
| REVOLUT, WISE, N26 (fee lines) | EXCLUDE | Check for taxable subscriptions |
| ZINSEN, HABENZINSEN, SOLLZINSEN | EXCLUDE | Interest, out of scope |
| KREDIT, DARLEHEN | EXCLUDE | Loan principal |

### 3.2 Austrian government and statutory bodies (exclude entirely)

**Government and statutory bodies table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| FINANZAMT, FA, BMF | EXCLUDE | Tax payment (USt, ESt, KöSt) |
| FINANZONLINE | EXCLUDE | Tax portal payment |
| SVS, SOZIALVERSICHERUNG DER SELBST | EXCLUDE | Self-employed social insurance: see `at-svs-contributions` |
| OEGK, OGK | EXCLUDE | Health insurance |
| AMS | EXCLUDE | Employment service |
| WKO, WIRTSCHAFTSKAMMER | EXCLUDE | Chamber of Commerce membership |
| GERICHT, BEZIRKSGERICHT | EXCLUDE | Court fees |
| GEMEINDE, MAGISTRAT | EXCLUDE | Municipal fees |
| FIRMENBUCH, LANDESGERICHT | EXCLUDE | Company register |

### 3.3 Austrian utilities

**Austrian utilities table**

| Pattern | Treatment | KZ | Notes |
| --- | --- | --- | --- |
| WIEN ENERGIE | Domestic 20% | 060 | Electricity/gas |
| WIENER STADTWERKE | Domestic 20% | 060 | Utilities |
| EVN | Domestic 20% | 060 | Energy |
| ENERGIE AG, LINZ AG | Domestic 20% | 060 | Energy |
| SALZBURG AG, KELAG, TIWAG, ILLWERKE | Domestic 20% | 060 | Regional energy |
| A1 TELEKOM, A1, TELEKOM AUSTRIA | Domestic 20% | 060 | Telecoms, overhead |
| MAGENTA, T-MOBILE AUSTRIA | Domestic 20% | 060 | Telecoms |
| DREI, HUTCHISON DREI | Domestic 20% | 060 | Telecoms |
| WIENER WASSER, WASSERWERK | Domestic, rate as invoiced | 060 | Reduced rate; take it from the invoice |

### 3.4 Insurance (exempt: exclude)

**Insurance table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| WIENER STADTISCHE, VIENNA INSURANCE | EXCLUDE | Insurance, exempt |
| UNIQA, GENERALI AUSTRIA | EXCLUDE | Same |
| ALLIANZ AUSTRIA, ZURICH | EXCLUDE | Same |
| VERSICHERUNG, PRAEMIE | EXCLUDE | All insurance exempt |
| WUSTENROT | EXCLUDE | Building society/insurance |

### 3.5 Post and logistics

**Post and logistics table**

| Pattern | Treatment | KZ | Notes |
| --- | --- | --- | --- |
| OSTERREICHISCHE POST, POST AG (standard) | EXCLUDE for standard postage |  | Universal service exempt |
| POST AG (parcels) | Domestic 20% | 060 | Non-universal taxable |
| DHL EXPRESS AUSTRIA | Domestic 20% | 060 | Express courier |
| DPD AUSTRIA, GLS AUSTRIA | Domestic 20% | 060 | Courier |

### 3.6 Transport (Austria domestic)

**Transport table**

| Pattern | Treatment | KZ | Notes |
| --- | --- | --- | --- |
| OBB, OSTERREICHISCHE BUNDESBAHNEN | Domestic 10% | 060 | Public transport |
| WESTBAHN | Domestic 10% | 060 | Rail |
| WIENER LINIEN | Domestic 10% | 060 | Vienna public transport |
| LINZ AG LINIEN, GRAZER LINIEN, IVB | Domestic 10% | 060 | Regional public transport |
| UBER AT, UBER AUSTRIA | Domestic, rate as invoiced | 060 | Passenger transport |
| TAXI | Domestic, rate as invoiced | 060 | Local taxi |
| AUSTRIAN AIRLINES (domestic) | Domestic, rate as invoiced | 060 | Domestic flight |
| AUSTRIAN AIRLINES, RYANAIR (international) | EXCLUDE |  | Cross-border transport, exempt |
| ASFINAG | BLOCKED for a car; else domestic 20% | none or 060 | Tolls and vignette for a Pkw: rule 5.12 |

### 3.7 Food retail (blocked unless hospitality business)

**Food retail table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| SPAR, INTERSPAR, EUROSPAR | Default BLOCK input VAT | Personal provisioning |
| BILLA, BILLA PLUS, MERKUR | Default BLOCK | Same |
| HOFER, LIDL, PENNY | Default BLOCK | Same |
| MPreis, UNIMARKT | Default BLOCK | Same |
| RESTAURANT, GASTHAUS, WIRTSHAUS, CAFE | Default BLOCK | Entertainment: see 5.12 |

### 3.8 SaaS: EU suppliers (reverse charge, KZ 057 and KZ 066)

**EU SaaS suppliers table**

| Pattern | Billing entity | KZ |
| --- | --- | --- |
| GOOGLE (Ads, Workspace, Cloud) | Google Ireland Ltd (IE) | 057 + 066 |
| MICROSOFT (365, Azure) | Microsoft Ireland Operations Ltd (IE) | 057 + 066 |
| ADOBE | Adobe Systems Software Ireland Ltd (IE) | 057 + 066 |
| META, FACEBOOK ADS | Meta Platforms Ireland Ltd (IE) | 057 + 066 |
| LINKEDIN (paid) | LinkedIn Ireland Unlimited (IE) | 057 + 066 |
| SPOTIFY TECHNOLOGY | Spotify AB (SE) | 057 + 066 |
| DROPBOX | Dropbox International Unlimited (IE) | 057 + 066 |
| SLACK | Slack Technologies Ireland Ltd (IE) | 057 + 066 |
| ATLASSIAN (Jira, Confluence) | Atlassian Network Services BV (NL) | 057 + 066 |
| ZOOM | Zoom Video Communications Ireland Ltd (IE) | 057 + 066 |
| STRIPE (subscription) | Stripe Technology Europe Ltd (IE) | 057 + 066 |

### 3.9 SaaS: non-EU suppliers (reverse charge, KZ 057 and KZ 066)

**Non-EU SaaS suppliers table**

| Pattern | Billing entity | KZ |
| --- | --- | --- |
| AWS (standard) | AWS EMEA SARL (LU): check | 057 + 066 |
| NOTION | Notion Labs Inc (US) | 057 + 066 |
| ANTHROPIC, CLAUDE | Anthropic PBC (US) | 057 + 066 |
| OPENAI, CHATGPT | OpenAI Inc (US) | 057 + 066 |
| GITHUB | GitHub Inc (US) | 057 + 066 |
| FIGMA | Figma Inc (US) | 057 + 066 |
| CANVA | Canva Pty Ltd (AU) | 057 + 066 |
| HUBSPOT | HubSpot Inc (US) or IE: check | 057 + 066 |
| TWILIO | Twilio Inc (US) | 057 + 066 |

The U 30 has one pair of boxes (057, 066) for services from abroad, EU or non-EU.

### 3.10 SaaS: the exception

**AWS EMEA SARL exception table**

| Pattern | Treatment | Why |
| --- | --- | --- |
| AWS EMEA SARL | Reverse charge KZ 057 + KZ 066 (LU entity) | If the invoice shows Austrian USt, treat as a domestic purchase at the standard rate, KZ 060 |

### 3.11 Payment processors

**Payment processors table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| STRIPE (transaction fees) | EXCLUDE (exempt) | Financial services |
| PAYPAL (transaction fees) | EXCLUDE (exempt) | Same |
| STRIPE (subscription) | Reverse charge KZ 057 + KZ 066 | IE entity |
| SUMUP, SQUARE, ZETTLE | Check invoice | If Austrian: domestic 20%; if foreign: reverse charge |

### 3.12 Professional services (Austria)

**Professional services table**

| Pattern | Treatment | KZ | Notes |
| --- | --- | --- | --- |
| STEUERBERATER, WIRTSCHAFTSPRUFER | Domestic 20% | 060 | Business services |
| RECHTSANWALT, ANWALTSKANZLEI | Domestic 20% | 060 | Business legal matters |
| NOTAR, NOTARIAT | Domestic 20% | 060 | Business notarial fees |
| UNTERNEHMENSBERATER, CONSULTANT | Domestic 20% | 060 | Consulting |
| BILANZBUCHHALTER | Domestic 20% | 060 | Bookkeeper |

### 3.13 Payroll and social security (exclude entirely)

**Payroll and social security table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| SVS, SOZIALVERSICHERUNG | EXCLUDE | Self-employed social insurance |
| OEGK, GESUNDHEITSKASSE | EXCLUDE | Health insurance |
| GEHALT, LOHN, ENTGELT | EXCLUDE | Wages |
| MITARBEITERVORSORGEKASSE, MVK | EXCLUDE | Employee provident fund |
| BETRIEBLICHE VORSORGE | EXCLUDE | Pension |

### 3.14 Property and rent

**Property and rent table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| BÜROMIETE, GESCHÄFTSLOKAL | Domestic 20% | Only if the landlord opted to tax; else exempt |
| MIETE, WOHNUNGSMIETE (residential) | Domestic 10% or EXCLUDE | 10% if the landlord charges USt |
| GRUNDSTEUER | EXCLUDE | Property tax |
| GRUNDBUCH | EXCLUDE | Land register fee |

### 3.15 Internal transfers and exclusions

**Internal transfers table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| UMBUCHUNG, INTERN, EIGENUEBERWEISUNG | EXCLUDE | Internal movement |
| DIVIDENDE | EXCLUDE | Out of scope |
| KREDITRÜCKZAHLUNG, TILGUNG | EXCLUDE | Loan repayment |
| BEHEBUNG, BARABHEBUNG | TIER 2: ask | Default exclude |
| PRIVATEINLAGE | EXCLUDE | Owner injection |

## Section 4: Worked examples

Six classifications for a hypothetical Austrian self-employed IT consultant (Regelbesteuerung). Amounts are invented.

### Example 1: Non-EU SaaS reverse charge (Notion)

**Input line:**
`03.04.2026 ; NOTION LABS INC ; DEBIT ; Monthly subscription ; -14.68`

**Reasoning:**
US entity (Section 3.9). B2B service taxed in Austria; the tax passes to the client (§ 19 Abs 1 second sentence UStG): KZ 057 and KZ 066. Net zero. Convert a foreign-currency charge to euro (Section 8).

**Output table**

| Date | Counterparty | Gross | Net | VAT | Rate | KZ (input) | KZ (output) | Default? | Question? | Excluded? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 03.04.2026 | NOTION LABS INC | -14.68 | -14.68 | 2.94 | 20% | 066 | 057 | N | none | none |

### Example 2: EU service, reverse charge (Google Ads)

**Input line:**
`10.04.2026 ; GOOGLE IRELAND LIMITED ; DEBIT ; Google Ads April 2026 ; -850.00`

**Reasoning:**
IE entity. B2B service taxed where the customer is (§ 3a Abs 6 UStG). KZ 057 and KZ 066. Net zero.

**Output table**

| Date | Counterparty | Gross | Net | VAT | Rate | KZ (input) | KZ (output) | Default? | Question? | Excluded? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 10.04.2026 | GOOGLE IRELAND LIMITED | -850.00 | -850.00 | 170.00 | 20% | 066 | 057 | N | none | none |

### Example 3: Entertainment, Bewirtung in Austria

**Input line:**
`15.04.2026 ; GASTHAUS PURSTNER WIEN ; DEBIT ; Business dinner ; -220.00`

**Reasoning:**
Restaurant. Input VAT only if the meal served advertising purposes and the business reason clearly outweighed all else (rule 5.12). Income tax: see `at-income-tax`. Default: block, flag.

**Output table**

| Date | Counterparty | Gross | Net | VAT | Rate | KZ | Default? | Question? | Excluded? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 15.04.2026 | GASTHAUS PURSTNER WIEN | -220.00 | -220.00 | 0 | none | none | Y | Q1 | "Bewirtung: input VAT only if advertising purpose is documented. Confirm." |

### Example 4: Capital goods (Anlagevermögen)

**Input line:**
`18.04.2026 ; DELL AUSTRIA GMBH ; DEBIT ; Laptop, business model ; -1,595.00`

**Reasoning:**
Net cost 1,329.17 is above the low-value asset limit in rule 5.11: capitalise for income tax. Input VAT fully deductible in KZ 060.

**Output table**

| Date | Counterparty | Gross | Net | VAT | Rate | KZ | Default? | Question? | Excluded? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 18.04.2026 | DELL AUSTRIA GMBH | -1,595.00 | -1,329.17 | -265.83 | 20% | 060 | N | none | none |

### Example 5: EU B2B service sale

**Input line:**
`22.04.2026 ; STUDIO KREBS GMBH ; CREDIT ; Invoice AT-2026-018 IT consultancy ; +3,500.00`

**Reasoning:**
B2B service to a German business: taxed in Germany (§ 3a Abs 6 UStG). Invoice net, noting the reverse charge and both UID numbers, by the 15th of the next month. Report in the ZM. It is not taxable in Austria, so it goes in neither KZ 000 nor KZ 021 of the U 30 (rule 5.4).

**Output table**

| Date | Counterparty | Gross | Net | VAT | Rate | KZ | Default? | Question? | Excluded? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 22.04.2026 | STUDIO KREBS GMBH | +3,500.00 | +3,500.00 | 0 | none | ZM only | Y | Q2 (HIGH) | "Verify German USt-IdNr" |

### Example 6: Motor vehicle, Vorsteuerabzug

**Input line:**
`28.04.2026 ; PORSCHE BANK LEASING ; DEBIT ; Lease payment VW Golf ; -550.00`

**Reasoning:**
Car lease. No input VAT on a Pkw, even at full business use (§ 12 Abs 2 Z 2 lit b UStG), unless an exception in rule 5.12 applies. A petrol or diesel VW Golf is none. Default: blocked.

**Output table**

| Date | Counterparty | Gross | Net | VAT | Rate | KZ | Default? | Question? | Excluded? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 28.04.2026 | PORSCHE BANK LEASING | -550.00 | -550.00 | 0 | none | none | Y | Q3 | "Pkw: input VAT blocked. Electric, or a Fiskal-LKW on the ministry's list?" |

## Section 5: Tier 1 classification rules (compressed)

### 5.1 Standard rate 20% (§ 10 Abs 1 UStG)

- **Standard rate.** The default rate in the rates table in Section 1. Sales: KZ 000 and KZ 022. Purchases: input VAT in KZ 060.

### 5.2 Reduced rate 10% (§ 10 Abs 2 UStG, Anlage 1)

- **Reduced rate 10%.** Items in the rates tables in Section 1. Sales: KZ 000 and KZ 029.
- **Reduced rate 4.9% (from 1 July 2026).** Deliveries of the listed basic foods, not restaurant or catering services. Sales: KZ 000 and KZ 124. Intra-EU acquisitions: KZ 070 and KZ 125.

### 5.3 Reduced rate 13% (§ 10 Abs 3 UStG, Anlage 2)

- **Reduced rate 13%.** Items in the rates table in Section 1. Sales: KZ 000 and KZ 006. For domestic flights and cultural events take the rate from the invoice.

### 5.4 Zero rate and exempt with credit

- **Exempt with credit.** Exports: KZ 011. Intra-EU supplies of goods to a business with a valid UID: KZ 017, and the ZM; the supply is exempt only if the ZM is filed by the end of the following month, unless the business justifies the failure to the tax office and files or corrects the ZM. B2B services taxed in another member state: ZM only. They are not taxable in Austria and go in neither KZ 000 nor KZ 021 (U 1a: "Nicht steuerbare Umsätze (z.B. Umsätze, deren Leistungsort im Ausland liegt), sind weder unter der Kennzahl 000 noch unter der Kennzahl 021 einzutragen"): https://formulare.bmf.gv.at/service/formulare/inter-Steuern/pdfd/2025/U1a.pdf

**Recapitulative statement (Zusammenfassende Meldung, ZM, form U13)**

| Turnover | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.usp.gv.at/themen/steuern-finanzen/umsatzsteuer-ueberblick/weitere-informationen-zur-umsatzsteuer/umsaetze-mit-auslandsbezug/zusammenfassende-meldung-zm.html |
| ZM quarterly up to | EUR 100,000 | Table on the page: "55.000 Euro - 100.000 Euro Quartal" |
| ZM monthly above | EUR 100,000 | "Über 100.000 Euro Monat" |

The ZM is due by the end of the month after the period, through FinanzOnline. A period with no such supplies needs no ZM.

### 5.5 Exempt without credit (§ 6 Abs 1 UStG)

- **Exempt without credit.** Medical, certain education, insurance, financial services, land sales. Land: KZ 019. Others: KZ 020. If significant, **R-AT-2 refuses**.

### 5.6 Local purchases

- **Local purchases.** Input VAT on a compliant invoice: KZ 060. Minimum business use and the small-invoice limit are in the tables below.

**Input VAT conditions**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.usp.gv.at/themen/steuern-finanzen/umsatzsteuer-ueberblick/vorsteuerabzug.html |
| Minimum business use for a purchase to count as made for the business | 10% | "wenn zu mindestens 10 Prozent unternehmerischen Zwecken dienen" |

**Small invoices**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.usp.gv.at/themen/steuern-finanzen/umsatzsteuer-ueberblick/weitere-informationen-zur-umsatzsteuer/vorsteuerabzug-und-rechnung/kleinbetragsrechnungen.html |
| Simplified invoice allowed up to this total, gross including VAT | EUR 400 | "Bruttobetrag inkl. Umsatzsteuer) von 400 Euro" |

### 5.7 Reverse charge: EU services (§ 3a Abs 6 / § 19)

- **Services from an EU business** taxable in Austria: tax in KZ 057, input VAT in KZ 066. Net zero. Not covered: federal road tolls, event-related services, letting of land.

### 5.8 Reverse charge: EU goods (innergemeinschaftlicher Erwerb)

- **Goods from an EU business.** Total base KZ 070; by rate KZ 072, 125, 073, 008, 088 (map in Section 1); input VAT KZ 065; exempt KZ 071. The legacy KZ 065/066/070 meanings were wrong.

### 5.9 Reverse charge: non-EU

- **Services from a non-EU business:** same boxes as rule 5.7, KZ 057 and KZ 066 (the legacy KZ 060 is total input VAT). No ZM.
- **Imports of goods:** deduct import VAT paid in KZ 061, or import VAT booked on the tax account in KZ 083.

### 5.10 Reverse charge: Bauleistungen (§ 19 Abs 1a)

- **Construction services received.** The tax passes when the recipient was itself commissioned to do the building work or usually supplies construction services. Tax KZ 048, input VAT KZ 082 (legacy said KZ 057). The subcontractor enters its sale in KZ 000 and KZ 021.

### 5.11 Capital goods

**Low-value assets (income tax limit)**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.usp.gv.at/themen/steuern-finanzen/steuerliche-gewinnermittlung/weitere-informationen-zur-steuerlichen-gewinnermittlung/betriebseinnahmen-und-ausgaben/geringwertige-wirtschaftsgueter.html |
| Asset cost up to which immediate expensing is allowed (net of deductible VAT) | EUR 1,000 | "nicht mehr als 1.000 Euro" |

- **Capital goods.** Above the limit: Anlagevermögen for income tax. Input VAT in KZ 060 either way. A later change of use is corrected under § 12 Abs 10 UStG in KZ 063; for land the period is the 19 years after first use.

### 5.12 Blocked Vorsteuer (§ 12 Abs 2 UStG)

**Cars: the exception by use**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.usp.gv.at/themen/steuern-finanzen/umsatzsteuer-ueberblick/weitere-informationen-zur-umsatzsteuer/vorsteuerabzug-und-rechnung/ausnahmen-vom-vorsteuerabzug.html |
| Vehicle used at least this much for commercial passenger transport or commercial rental: input VAT allowed | 80% | "zu mindestens 80 Prozent dem Zweck der gewerblichen Personenbeförderung oder der gewerblichen Vermietung dienen" |

- **Pkw, Kombi, motorcycles.** No input VAT on purchase, lease or running costs (fuel, repairs, tolls, vignette), even at full business use. Exceptions: vans on the ministry's Fiskal-LKW list, driving school and demonstration cars, resale stock, the use test in the table, and zero-emission cars within the reasonableness cap.
- **Fuel.** Follows the vehicle.
- **Business meals (Bewirtung).** Input VAT only if you can prove the meal served advertising and the business reason clearly outweighed all else.
- **Travel services bought for resale (Reisevorleistungen).** No input VAT.
- **Personal use.** Not deductible.
- **Business gifts.** A gift given for business reasons (for example to a customer) above the value in the table below counts as own use (Eigenverbrauch): report its base in KZ 001 and tax it in the rate box. It is not an input VAT block.

**Gifts as own use**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://formulare.bmf.gv.at/service/formulare/inter-Steuern/pdfd/2025/U1a.pdf |
| Business gift counted as own use if worth more than | EUR 40 | "Darunter fallen auch Geschenke im Wert von über 40 Euro" |

### 5.13 Residential rent at 10%

- **Residential rent.** Taxed at 10% (rates table in Section 1). Business premises: exempt unless the landlord opts to tax. Default: [T2] flag if uncertain.

### 5.14 Sales: local domestic

- **Sales: local domestic.** Map to KZ 022, 124, 029 or 006, total in KZ 000.

### 5.15 Sales: cross-border B2C

**Distance sales threshold**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.usp.gv.at/themen/steuern-finanzen/umsatzsteuer-ueberblick/weitere-informationen-zur-umsatzsteuer/umsaetze-mit-auslandsbezug/innergemeinschaftlicher-versandhandel.html |
| EU-wide B2C distance sales and e-services up to which home VAT may apply | EUR 10,000 | "von insgesamt maximal 10.000 Euro tätigt" |

- **Sales: cross-border B2C.** Above the threshold in the table: **R-EU-5 OSS refusal**.

## Section 6: Tier 2 catalogue (compressed)

### 6.1 Fuel and vehicle costs

- **Fuel and vehicle costs.** *Pattern:* OMV, BP, SHELL, AVIA, ENI, JET. *Default:* blocked. *Question:* "Pkw, electric car, or Fiskal-LKW?"

### 6.2 Restaurants and entertainment

- **Restaurants and entertainment.** *Pattern:* Gasthaus, Restaurant, Wirtshaus. *Default:* block. *Question:* "Advertising meal, documented?"

### 6.3 Ambiguous SaaS

- **Ambiguous SaaS.** *Default:* reverse charge KZ 057 and KZ 066. *Question:* "Which legal entity invoiced?"

### 6.4 Owner transfers

- **Owner transfers.** *Default:* exclude as Privateinlage. *Question:* "Customer payment, own money, or loan?"

### 6.5 Incoming from individuals

- **Incoming from individuals.** *Default:* domestic B2C at the standard rate. *Question:* "Sale?"

### 6.6 Foreign incoming

- **Foreign incoming.** *Default:* domestic at the standard rate. *Question:* "B2B with UID, B2C, goods or services, which country?"

### 6.7 Large purchases

- **Large purchases.** *Default:* if the net cost is above the limit in rule 5.11, Anlagevermögen. *Question:* "Confirm invoice total."

### 6.8 Mixed-use phone, internet

- **Mixed-use phone, internet.** *Default:* no recovery. *Question:* "Business share?"

### 6.9 Outgoing to individuals

- **Outgoing to individuals.** *Default:* exclude. *Question:* "Contractor, wages, refund, personal?"

### 6.10 Cash withdrawals

- **Cash withdrawals.** *Default:* exclude. *Question:* "What for?"

### 6.11 Rent

- **Rent.** *Default:* [T2] flag. *Question:* "Commercial or residential? Did the landlord charge USt?"

### 6.12 Foreign hotel

- **Foreign hotel.** *Default:* exclude; foreign VAT is reclaimed by the refund procedure, not in the UVA. *Question:* "Business trip?"

### 6.13 Airbnb income

- **Airbnb income.** *Default:* [T2] flag. *Question:* "Duration? Small business?"

### 6.14 Bauleistungen reverse charge

- **Bauleistungen reverse charge.** *Pattern:* Bauunternehmen, construction. *Default:* [T2] flag. *Question:* "Do you usually supply construction services?"

### 6.15 Platform sales

- **Platform sales.** *Default:* if EU cross-border above the threshold in rule 5.15, R-EU-5. Otherwise domestic at the standard rate. *Question:* "Sell outside Austria?"

## Section 7: Excel working paper template (Austria-specific)

### Sheet "Transactions"

Column H accepts Kennzahl codes from the map in Section 1.

### Sheet "KZ Summary"

**KZ Summary formulas**

| KZ | Meaning | Formula |
| --- | --- | --- |
| 000 | Total tax base | =SUMIFS(...) |
| 022 | Sales standard-rate base | =SUMIFS(...) |
| 124 | Sales 4.9% base | =SUMIFS(...) |
| 029 | Sales 10% base | =SUMIFS(...) |
| 006 | Sales 13% base | =SUMIFS(...) |
| 057 | Tax on services from abroad | =SUMIFS(...) |
| 072 | Intra-EU acquisitions standard-rate base | =SUMIFS(...) |
| 060 | Input VAT, domestic invoices | =SUMIFS(...) |
| 065 | Input VAT on intra-EU acquisitions | =tax on KZ 072, 125, 073, 008 where deductible (not on certain cars) |
| 066 | Input VAT on KZ 057 | =KZ 057 if fully deductible |
| 095 | Payment due (positive) or refund (negative) | =output tax minus deductible input VAT, plus corrections |

Check against the FinanzOnline calculation before filing.

### Mandatory recalc step

~~~bash
python /mnt/skills/public/xlsx/scripts/recalc.py /mnt/user-data/outputs/austria-vat-period-working-paper.xlsx
~~~

## Section 8: Austrian bank statement reading guide

**CSV format conventions.** Austrian banks export CSV with semicolons and DD.MM.YYYY dates. Common columns: Buchungsdatum, Umsatztext/Verwendungszweck, Betrag, Saldo. Erste Bank uses CAMT format; Raiffeisen varies by regional bank.

**German language variants.** Miete (rent), Gehalt/Lohn (salary), Zinsen (interest), Überweisung (transfer), Beiträge (contributions), Rechnung (invoice), Rückzahlung/Gutschrift (refund), Einzahlung (deposit), Behebung/Abhebung (withdrawal).

**Internal transfers.** "Umbuchung", "Eigenüberweisung". Exclude.

**Finanzamt payments.** Tax payments appear as "FINANZAMT" with an Abgabenkontonummer. Always exclude. The payment slip for a UVA payment must state the period and the amount.

**SVS payments.** Self-employed social insurance appears as quarterly direct debits. Always exclude: not a VATable supply.

**Foreign currency.** Convert to EUR at the ECB rate.

**IBAN prefix.** AT = Austria. DE, NL, IE = EU. US, GB, CH = non-EU. CH (Switzerland) is non-EU, important for Austrian businesses near the Swiss border.

## Section 9: Onboarding fallback

### 9.1 Entity type

- **Entity type.** *Inference:* GmbH = company; Einzelunternehmer/e.U. = sole trader; KG/OG = partnership. *Fallback:* "Einzelunternehmer, GmbH, or KG?" See `at-company-formation`.

### 9.2 USt regime

- **USt regime.** *Fallback:* "Regelbesteuerung or Kleinunternehmerregelung? If you waived the exemption, from which year?"

### 9.3 UID-Nummer

- **UID-Nummer.** *Fallback:* "Your UID-Nummer? (ATU followed by 8 digits)"

### 9.4 Filing period

- **Filing period.** *Fallback:* "Which month or quarter? What was last year's turnover?" (it sets the band in the UVA filing table).

### 9.5 Industry

- **Industry.** *Fallback:* "What does the business do?"

### 9.6 Employees

- **Employees.** *Inference:* Gehalt outgoing. *Fallback:* "Employees?"

### 9.7 Exempt supplies

- **Exempt supplies.** *Fallback:* "Any exempt sales?" *If yes: R-AT-2.*

### 9.8 Credit carried forward

- **Credit carried forward.** *Always ask.* "Any refund still on the tax account?"

### 9.9 Cross-border customers

- **Cross-border customers.** *Fallback:* "Customers outside Austria? EU or non-EU? B2B or B2C?"

### 9.10 Construction

- **Construction.** *Conditional:* "In construction? (Bauleistungen reverse charge may apply.)"

## Section 10: Reference material

### Sources

- **Sources list.** See Sources at the end of this Guide.

### Known gaps

1. Fiskal-LKW list not reproduced: see the ministry's list, linked from the USP exceptions page.
2. Bauleistungen reverse charge flagged T2 only.
3. Rates for flights, water, taxis and cultural events: take from the invoice.
4. GWG limit: check annually.
5. Jungholz/Mittelberg rate refused entirely.
6. Bewirtung input VAT requires documentation: flagged.
7. U 1 Kennzahlen are not listed here.

### Change log

- **v2.1 (September 2026):** Kennzahlen from the 2026 U 30; UVA bands, small business limit, 4.9% rate.
- **v2.0 (April 2026):** Full rewrite to Malta v2.0 structure.
- **v1.0/1.1:** Initial Guide.

### Self-check (v2.0)

Quick reference, supplier library, six examples, Tier 1 and Tier 2 rules, template, onboarding, refusals and reference: present. Kennzahlen checked against the 2026 U 30.

## The method, step by step

1. Check scope. A client under the small business exemption (§ 6 Abs 1 Z 27 UStG) files no UVA and no annual return: stop. Otherwise run the refusal catalogue in Section 2. https://www.usp.gv.at/themen/steuern-finanzen/umsatzsteuer-ueberblick/weitere-informationen-zur-umsatzsteuer/weitere-steuertatbestaende-und-befreiungen/kleinunternehmen.html
2. Fix the period from last year's turnover with the UVA filing table in Section 1 (§ 21 UStG). https://www.usp.gv.at/themen/steuern-finanzen/umsatzsteuer-ueberblick/weitere-informationen-zur-umsatzsteuer/entstehen-der-steuerschuld-und-pflichten/umsatzsteuervoranmeldung.html
3. Classify every line (Section 3, then Section 5). Place of supply comes before the rate: a B2B service is taxed where the customer is (§ 3a UStG). Test each input VAT claim against § 12 UStG and rule 5.12. https://www.usp.gv.at/themen/steuern-finanzen/umsatzsteuer-ueberblick/weitere-informationen-zur-umsatzsteuer/vorsteuerabzug-und-rechnung/ausnahmen-vom-vorsteuerabzug.html
4. Map each line to its Kennzahl with the map in Section 1; listed basic foods from 1 July 2026 go to KZ 124 and KZ 125. https://formulare.bmf.gv.at/service/formulare/inter-Steuern/pdfs/2026/U30.pdf?open=download
5. File the U 30 through FinanzOnline and pay by the 15th of the second month after the period. File the ZM (form U13) by the end of the following month if there were intra-EU supplies or B2B services to the EU. https://www.usp.gv.at/themen/steuern-finanzen/umsatzsteuer-ueberblick/weitere-informationen-zur-umsatzsteuer/umsaetze-mit-auslandsbezug/zusammenfassende-meldung-zm.html
6. After the year, file form U 1 (by 30 June through FinanzOnline). It should equal the sum of the UVAs; a shortfall is payable within a month of the assessment. https://www.usp.gv.at/themen/steuern-finanzen/umsatzsteuer-ueberblick/umsatzsteuervoranmeldung-und-umsatzsteuererklaerung.html

**Annual return**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.usp.gv.at/themen/steuern-finanzen/umsatzsteuer-ueberblick/umsatzsteuervoranmeldung-und-umsatzsteuererklaerung.html |
| Annual VAT return required in principle where yearly turnover exceeds | EUR 55,000 | "deren Jahresumsatz 55.000 Euro übersteigt, sind grundsätzlich zur Abgabe von Umsatzsteuererklärungen verpflichtet" |

A business that waived the small business exemption must file an annual return whatever its turnover ("Das Unternehmen muss bei Ausübung der Option zur Steuerpflicht eine Umsatzsteuerjahreserklärung einreichen"): https://www.usp.gv.at/themen/steuern-finanzen/umsatzsteuer-ueberblick/weitere-informationen-zur-umsatzsteuer/weitere-steuertatbestaende-und-befreiungen/kleinunternehmen.html

## Ask the client first

- Are you on the normal scheme or under the small business exemption? If you waived it, from which year? What was your gross turnover last year and so far this year?
- What was last year's turnover (it decides monthly, quarterly or no UVA), and did you choose monthly filing by filing a January UVA on time?
- Any sales of listed basic foods since 1 July 2026, or restaurant sales?
- For each foreign supplier: which legal entity issued the invoice, and does it show Austrian USt or a reverse-charge note?
- For each EU customer: do you hold a valid UID number, and are these goods or services?
- For each vehicle: Pkw, electric car, or a van on the ministry's Fiskal-LKW list?

## When to refuse or refer

- Any trigger in the refusal catalogue in Section 2 fires: small business exemption, partial exemption, margin scheme, VAT group, fiscal representative, property transactions, Jungholz or Mittelberg.
- A special scheme this Guide does not cover: the one-stop shop (OSS), travel services (§ 23 UStG), or flat-rate farming (KZ 052 and KZ 007).
- Construction, scrap, metals or gold reverse charge (KZ 048, KZ 032): the deciding facts are not on a statement.
- A change-of-use correction (KZ 063), an earlier-period correction, or VAT shown wrongly on an invoice (KZ 056).
- A material line's counterparty cannot be identified and the client cannot produce the invoice.

## Sources

- https://formulare.bmf.gv.at/service/formulare/inter-Steuern/pdfs/2026/U30.pdf?open=download
- https://formulare.bmf.gv.at/service/formulare/inter-Steuern/pdfd/2026/U30a.pdf
- https://formulare.bmf.gv.at/service/formulare/inter-Steuern/pdfd/2025/U1a.pdf
- https://www.usp.gv.at/themen/steuern-finanzen/umsatzsteuer-ueberblick/steuersaetze-und-steuerbefreiungen-der-umsatzsteuer.html
- https://www.oesterreich.gv.at/lexicon/M/Seite.991672.html
- https://www.bmf.gv.at/rechtsnews/steuern-rechtsnews/aktuelle-infos-und-erlaesse/fachinformationen---umsatzsteuer/umsatzsteuersenkung-auf-ausgewaehlte-nahrungsmittel.html
- https://www.usp.gv.at/themen/steuern-finanzen/umsatzsteuer-ueberblick/weitere-informationen-zur-umsatzsteuer/entstehen-der-steuerschuld-und-pflichten/umsatzsteuervoranmeldung.html
- https://www.usp.gv.at/themen/steuern-finanzen/umsatzsteuer-ueberblick/umsatzsteuervoranmeldung-und-umsatzsteuererklaerung.html
- https://www.usp.gv.at/themen/steuern-finanzen/umsatzsteuer-ueberblick/weitere-informationen-zur-umsatzsteuer/weitere-steuertatbestaende-und-befreiungen/kleinunternehmen.html
- https://www.usp.gv.at/themen/steuern-finanzen/umsatzsteuer-ueberblick/weitere-informationen-zur-umsatzsteuer/umsaetze-mit-auslandsbezug/zusammenfassende-meldung-zm.html
- https://www.usp.gv.at/themen/steuern-finanzen/umsatzsteuer-ueberblick/weitere-informationen-zur-umsatzsteuer/umsaetze-mit-auslandsbezug/reverse-charge.html
- https://www.usp.gv.at/themen/steuern-finanzen/umsatzsteuer-ueberblick/weitere-informationen-zur-umsatzsteuer/umsaetze-mit-auslandsbezug/grenzueberschreitende-dienstleistungen.html
- https://www.usp.gv.at/themen/steuern-finanzen/umsatzsteuer-ueberblick/vorsteuerabzug.html
- https://www.usp.gv.at/themen/steuern-finanzen/umsatzsteuer-ueberblick/weitere-informationen-zur-umsatzsteuer/vorsteuerabzug-und-rechnung/ausnahmen-vom-vorsteuerabzug.html
- https://www.usp.gv.at/themen/steuern-finanzen/umsatzsteuer-ueberblick/weitere-informationen-zur-umsatzsteuer/vorsteuerabzug-und-rechnung/kleinbetragsrechnungen.html
- https://www.usp.gv.at/themen/steuern-finanzen/steuerliche-gewinnermittlung/weitere-informationen-zur-steuerlichen-gewinnermittlung/betriebseinnahmen-und-ausgaben/geringwertige-wirtschaftsgueter.html
- https://www.usp.gv.at/themen/steuern-finanzen/umsatzsteuer-ueberblick/weitere-informationen-zur-umsatzsteuer/umsaetze-mit-auslandsbezug/innergemeinschaftlicher-versandhandel.html

## End of Austria VAT Return Guide v2.1

This Guide is incomplete without BOTH companion Guides: `vat-workflow-base` v0.1+ AND `eu-vat-directive` v0.1+.

## Disclaimer

This Guide and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this Guide. All outputs must be reviewed and signed off by a qualified professional (such as a Steuerberater, Wirtschaftsprüfer, or equivalent licensed practitioner) before filing or acting upon.

The latest version of this Guide is maintained by Open Accountants.

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
