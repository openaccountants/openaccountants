---
name: germany-bookkeeping
description: Use this skill whenever asked about bookkeeping, chart of accounts, Kontenrahmen, SKR03, SKR04, financial statements, P&L format, balance sheet layout, bank reconciliation, expense classification, asset capitalisation, GWG, or day-to-day accounting for a German entity. Trigger on phrases like "Kontenrahmen", "SKR03", "SKR04", "HGB", "Buchhaltung", "chart of accounts Germany", "EÜR", "Einnahmen-Überschussrechnung", "Bilanz", "GuV", "capitalise or expense Germany", "GWG threshold", "Geringwertige Wirtschaftsgüter", "depreciation Germany", "AfA", "bank reconciliation Germany", "Kleinunternehmer", "bookkeeping Germany", or any question about recording transactions, classifying expenses, or preparing accounts under German law. ALWAYS read this skill before touching any bookkeeping work for Germany.
version: 1.0
jurisdiction: DE
tax_year: 2026
last_updated: 2026-10-24
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - bookkeeping-workflow-base
category: bookkeeping
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Bookkeeping in Germany (Buchführung, SKR03 and SKR04)

How a German business keeps its books: who must keep double-entry books and who may use the cash-basis EÜR, the SKR03 and SKR04 charts of accounts, how to classify expenses and fixed assets, the statutory layouts of the P&L and the balance sheet, e-invoicing, and how long to keep records. It is for sole traders, freelancers, partnerships and small companies, and for the people who keep their books. Figures are for tax year 2026. The figures are read from the consolidated federal law pages and from finance ministry documents: the instructions for the 2026 EÜR form (ministry letter of 1 September 2026), the official depreciation table, and the GoBD and e-invoice rulings. The reduced VAT rate is printed as a digit only in the ministry's tax booklet, 2025 edition; the statute states it in words.

## Section 1: Quick Reference

| Field | Value |
| --- | --- |
| Country | Germany (Bundesrepublik Deutschland) |
| Currency | EUR |
| Financial year | Traders entered in the commercial register: the period for which they regularly close their books; moving to a year that differs from the calendar year needs the tax office's agreement. Other traders: the calendar year (§ 4a EStG). Income tax itself is assessed per calendar year (§ 2(7) EStG). A financial year may not be longer than twelve months (§ 240(2) HGB) |
| Accounting standards | HGB (Handelsgesetzbuch), the German Commercial Code |
| GAAP framework | German GAAP (GoB, Grundsätze ordnungsmäßiger Buchführung) |
| Standard chart of accounts | SKR03 (process-oriented) and SKR04 (financial-statement-oriented), published by DATEV |
| Governing body | Finanzamt (local tax office) for tax books and returns. Companies send their annual accounts to the company register (Unternehmensregister, § 325 HGB) |
| Key legislation | HGB, Third Book, from § 238 (Handelsbücher); EStG (Einkommensteuergesetz); UStG (Umsatzsteuergesetz); AO (Abgabenordnung) |
| Record retention | Ten, eight or six years, depending on the class of document. See the retention table below |
| Digital requirements | GoBD: the ministry's principles for books and records kept electronically and for data access by the tax office. See below |

**Record retention under tax law**

| Class of document | Keep for | Note |
| --- | --- | --- |
| Source | all periods below | https://www.gesetze-im-internet.de/ao_1977/__147.html |
| Books and records, inventories, annual financial statements, management reports, the opening balance sheet, and the work instructions and other organisational documents needed to understand them | 10 years | § 147(3) AO: "Die in Absatz 1 Nummer 1 und 4a aufgeführten Unterlagen sind zehn Jahre" |
| Accounting vouchers (Buchungsbelege): the documents that support an entry | 8 years | § 147(3) AO: "die in Absatz 1 Nummer 4 aufgeführten Unterlagen acht Jahre" |
| Business letters received, copies of business letters sent, and other documents that matter for tax | 6 years | § 147(3) AO: "die sonstigen in Absatz 1 aufgeführten Unterlagen sechs Jahre aufzubewahren" |
| Customs documents under the Union Customs Code (§ 147(1) no. 4a AO) | 10 years | Same sentence as the first row |

- **Books and vouchers no longer share one period.** Older material gives one period for "books and records". The current text splits them: books and statements in the first row, vouchers in the second.
- **Which documents the shorter voucher period covers.** It applies to every document whose old period had not yet run out on 31 December 2024. See Art. 97 § 19a(2) EGAO at https://www.gesetze-im-internet.de/aoeg_1977/art_97__19a.html
- **Banks, insurers and securities institutions keep the ten-year voucher period for tax purposes.** For institutions under § 1(1b) of the Banking Act (KWG), including branches under § 53 KWG, businesses supervised under § 1(1) of the Insurance Supervision Act (VAG), and securities institutions under § 2(1) of the Securities Institutions Act (WpIG), § 147(3) sentence 1 AO applies in the version in force on 31 December 2024: "ist § 147 Absatz 3 Satz 1 der Abgabenordnung in der am 31. Dezember 2024 geltenden Fassung abweichend von Absatz 2 anzuwenden". See Art. 97 § 19a(3) EGAO at https://www.gesetze-im-internet.de/aoeg_1977/art_97__19a.html
- **Start of the period.** The end of the calendar year in which the last entry was made, the statements were drawn up, the letter was received or sent, or the voucher came into being (§ 147(4) AO).
- **The period can run longer.** It does not end while the documents still matter for a tax whose assessment period is still open (§ 147(3) AO).
- **Delivery notes** that are not vouchers need to be kept only until the invoice is received (incoming) or sent (outgoing) (§ 147(3) AO).
- **Invoices.** VAT law sets its own period for invoices issued and received: eight years from the end of the calendar year in which the invoice was issued. See § 14b(1) UStG at https://www.gesetze-im-internet.de/ustg_1980/__14b.html
- **Commercial law** has the same three periods for merchants. Banks, insurers and securities institutions keep vouchers for ten years. See § 257(4) HGB at https://www.gesetze-im-internet.de/hgb/__257.html

**GoBD and the order rules**

- **What the law demands of every entry.** Entries and records must be made one by one, completely, correctly, in time and in order. Cash receipts and cash payments must be recorded daily. An entry must not be changed in a way that hides its original content. See § 146(1) and (4) AO at https://www.gesetze-im-internet.de/ao_1977/__146.html
- **GoBD.** The ministry's principles for books, records and documents kept in electronic form and for data access. They were published by ministry letter of 28 November 2019 and changed by the letters of 11 March 2024 and 14 July 2025. First change: https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Weitere_Steuerthemen/Abgabenordnung/AO-Anwendungserlass/2024-03-11-aenderung-gobd.pdf?__blob=publicationFile&v=4
- **GoBD and e-invoices.** For an e-invoice it is enough to keep the structured data part, as long as the GoBD rules are met. The readable part of a hybrid invoice (for example the PDF part of a ZUGFeRD invoice) must be kept only if it holds extra or different information that matters for tax. Second change: https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Weitere_Steuerthemen/Abgabenordnung/2025-07-14-GoBD-2-aenderung.pdf?__blob=publicationFile&v=4
- **Small businesses.** For a small business that stays within the previous-year limit of § 19 UStG and uses the EÜR, the tax office is to judge the GoBD record demands with the size of the business in mind (first change letter, on paragraph 15 of the GoBD).

## Section 2: Standard Chart of Accounts (SKR04: Abschlussgliederungsprinzip)

SKR04 is organised to mirror the balance sheet and income statement structure. SKR03 (process-oriented) is also widely used, especially by sole traders and EÜR filers. The mapping below uses SKR04 with SKR03 equivalents noted.

Account numbers were checked on 19 September 2026 against DATEV's own charts for 2026 (DATEV-Kontenrahmen nach dem Bilanzrichtlinie-Umsetzungsgesetz, SKR03 and SKR04). The copies read were DATEV's branch edition for construction and trades, and only its base accounts were used. The plain standard edition could not be read, because it sits behind DATEV's login. DATEV is a private publisher, not an official source, so it is not linked here. DATEV issues its charts per year, and a client's chart can differ. Check every number in the client's own accounting software before posting.

**VAT rates used in the chart: the statute**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.gesetze-im-internet.de/ustg_1980/__12.html |
| Standard rate | 19% | § 12(1) UStG: "Die Steuer beträgt für jeden steuerpflichtigen Umsatz 19 Prozent der Bemessungsgrundlage" |
| Reduced rate | seven percent, stated in words | § 12(2) UStG: "Die Steuer ermäßigt sich auf sieben Prozent für die folgenden Umsätze" |

**VAT rates used in the chart: as the ministry prints them**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.bundesfinanzministerium.de/Content/DE/Downloads/Broschueren_Bestellservice/steuern-von-a-z.pdf?__blob=publicationFile&v=9 |
| Standard rate | 19% | Tax booklet, 2025 edition: "den allgemeinen Steuersatz von 19 Prozent" |
| Reduced rate | 7% | Tax booklet, 2025 edition: "den ermäßigten von 7 Prozent" |

### Class 0: Non-Current Assets (Anlagevermögen)

| SKR04 | SKR03 | Account | Notes |
| --- | --- | --- | --- |
| 0150 | 0035 | Goodwill (Geschäfts- oder Firmenwert) |  |
| 0135 | 0027 | Software (EDV-Software) | Licences to industrial rights: 0140 / 0030 |
| 0400 | 0210 | Technical equipment and machinery | SKR03 0210 is machinery (Maschinen). The SKR03 group account is 0200 |
| 0520 | 0320 | Motor vehicles (Fuhrpark) | Cars. Trucks (Lkw): 0540 / 0350 |
| 0500 | 0410 | Office equipment (Betriebs- und Geschäftsausstattung) |  |
| 0690 | 0490 | Other equipment, including computer hardware (Sonstige Betriebs- und Geschäftsausstattung) | DATEV's base accounts have none named for computer hardware |
| 0650 | 0420 | Furniture and fittings (Büromöbel) |  |
| 0230 | 0080 | Buildings on own land (Bauten auf eigenen Grundstücken) |  |

### Class 1: Current Assets (Umlaufvermögen)

| SKR04 | SKR03 | Account | Notes |
| --- | --- | --- | --- |
| 1200 | 1400 | Trade receivables (Forderungen aus L.u.L.) |  |
| 1400 | 1570 | VAT receivable (Vorsteuer) | Input VAT |
| 1406 | 1576 | VAT receivable 19% | Standard rate |
| 1401 | 1571 | VAT receivable 7% | Reduced rate |
| 1407 | 1577 | VAT receivable (reverse charge) | Standard rate. Without a rate: 1408 / 1578 |
| 1800 | 1200 | Bank | Main bank account |
| 1810 | 1210 | Bank account 2 |  |
| 1600 | 1000 | Cash in hand (Kasse) |  |

### Class 2: Equity (Eigenkapital)

| SKR04 | SKR03 | Account | Notes |
| --- | --- | --- | --- |
| 2900 | 0800 | Share capital / registered capital (Gezeichnetes Kapital) |  |
| 2920 | 0840 | Capital reserves (Kapitalrücklage) |  |
| 2970 | 0860 | Retained earnings (Gewinnvortrag) |  |
| 2978 | 0868 | Loss carried forward (Verlustvortrag) |  |
| 2100 | 1800 | Private withdrawals (Privatentnahmen allgemein) |  |

### Class 3: Liabilities (Fremdkapital)

| SKR04 | SKR03 | Account | Notes |
| --- | --- | --- | --- |
| 3300 | 1600 | Trade payables (Verbindlichkeiten aus L.u.L.) |  |
| 3150 | 0630 | Bank loans (Verbindlichkeiten gegenüber Kreditinstituten) | By remaining term: one to five years 3160 / 0640, more than five years 3170 / 0650 |
| 3151 | 0631 | Bank loans (short-term) | Remaining term up to one year |
| 3800 | 1770 | VAT payable (Umsatzsteuer) | Output VAT. At the standard rate: 3806 / 1776 |
| 3700 | 1736 | Other tax liabilities |  |
| 3070 | 0970 | Accruals (Rückstellungen) | Other provisions. Tax provisions (Steuerrückstellungen): 3020 / 0955 |
| 3900 | 0990 | Deferred income (Rechnungsabgrenzung passiv) |  |

### Class 4: Revenue (Betriebliche Erträge)

| SKR04 | SKR03 | Account | Notes |
| --- | --- | --- | --- |
| 4400 | 8400 | Revenue from goods (Umsatzerlöse) | 19% VAT. DATEV's 4000 / 8000 (Umsatzerlöse) is a free range with no VAT function |
| 4300 | 8300 | Revenue, reduced rate | 7% VAT |
| 4125 | 8125 | Revenue, tax-free with input VAT deduction | Intra-EU supplies. Exports: 4120 / 8120 |
| 4100 | 8100 | Revenue, tax-free without input VAT deduction | §4 UStG exempt |
| 4337 | 8337 | Revenue, reverse charge services | §13b UStG |
| 4830 | 8603 | Other operating income (Sonstige betriebliche Erträge) |  |
| 4840 | 2660 | Exchange gains (Erträge aus der Währungsumrechnung) | Exchange losses: 6880 / 2150 (Aufwendungen aus der Währungsumrechnung) |

### Class 5 & 6: Operating Expenses (Betriebliche Aufwendungen)

| SKR04 | SKR03 | Account | Notes |
| --- | --- | --- | --- |
| 5000 | 3000 | Cost of materials / goods purchased (Wareneinkauf) | Goods for resale (Wareneingang): 5200 / 3200 |
| 5900 | 3100 | Purchased services (Fremdleistungen) | Subcontractors |
| 6000 | 4100 | Salaries (Löhne und Gehälter) | Salaries alone (Gehälter): 6020 / 4120 |
| 6010 | 4110 | Wages |  |
| 6100 | 4130 | Social security employer share | SKR04 6100 is the group account. Statutory contributions alone: 6110 |
| 6310 | 4200 | Rent and lease expenses (Miete) | SKR03 4200 is the room costs group (Raumkosten). Rent itself: 4210 |
| 6400 | 4360 | Insurance (Versicherungen) |  |
| 6520 | 4520 | Motor vehicle insurance |  |
| 6500 | 4500 | Motor vehicle costs (Kfz-Kosten) | Group account. Running costs such as fuel: 6530 / 4530 |
| 6600 | 4600 | Advertising (Werbekosten) |  |
| 6650 | 4660 | Travel expenses, employees (Reisekosten Arbeitnehmer) | The owner's own trips: 6670 / 4670 (Reisekosten Unternehmer) |
| 6640 | 4650 | Entertainment, deductible portion | See the entertainment tables in Section 4 |
| 6644 | 4654 | Entertainment, non-deductible portion | Always add back for tax |
| 6490 | 4800 | Repairs and maintenance (Instandhaltung) | SKR04 by asset type: buildings 6450, technical equipment 6460, other equipment 6470. SKR03 other repairs: 4809 |
| 6300 | 4900 | Miscellaneous expenses (Sonstige Aufwendungen) |  |
| 6815 | 4930 | Office supplies (Bürobedarf) |  |
| 6805 | 4920 | Telephone and internet (Telekommunikation) | Internet: 6810 / 4925 (Internetkosten) |
| 6827 | 4957 | Professional fees, accountant | Year-end accounts. Bookkeeping fees: 6830 / 4955 (Buchführungskosten) |
| 6825 | 4950 | Professional fees, legal |  |
| 6855 | 4970 | Bank charges (Bankgebühren) |  |
| 6837 | 4964 | Software subscriptions | DATEV's base accounts have none named for software subscriptions. This is the account for the time-limited use of rights |
| 6821 | 4945 | Training and education (Fortbildung) |  |
| 6220 | 4830 | Depreciation, fixed assets (AfA Sachanlagen) | Without vehicles and buildings. Vehicles: 6222 / 4832. Buildings: 6221 / 4831 |
| 6200 | 4822 | Depreciation, intangible assets (AfA immaterielle) |  |
| 6260 | 4855 | GWG immediate write-off | § 6 Abs. 2 EStG. See the GWG table in Section 5 |
| 6264 | 4862 | GWG pool depreciation (Sammelposten) | § 6 Abs. 2a EStG. See the GWG table in Section 5 |
| 6610 | 4630 | Gifts, deductible (Geschenke abzugsfähig ohne § 37b EStG) |  |
| 6620 | 4635 | Gifts, not deductible (Geschenke nicht abzugsfähig ohne § 37b EStG) |  |
| 6348 | 4288 | Home office room, deductible part (häusliches Arbeitszimmer, abziehbarer Anteil) |  |
| 6349 | 4289 | Home office room, non-deductible part (häusliches Arbeitszimmer, nicht abziehbarer Anteil) |  |
| 6347 | 4287 | Daily flat amount for work at home (Tagespauschale) |  |

### Class 7: Other Income/Expenses (Weitere Erträge und Aufwendungen)

| SKR04 | SKR03 | Account | Notes |
| --- | --- | --- | --- |
| 7100 | 2650 | Interest income (Zinserträge) |  |
| 7300 | 2100 | Interest expense (Zinsaufwand) |  |

### Tax Accounts (Class 7/9)

| SKR04 | SKR03 | Account | Notes |
| --- | --- | --- | --- |
| 7600 | 2200 | Income tax expense (Ertragsteuern) | DATEV's name for both accounts is Körperschaftsteuer (corporation tax) |
| 7610 | 4320 | Trade tax expense (Gewerbesteuer) | If applicable. Not a business expense for tax (§ 4(5b) EStG) |
| 7608 | 2208 | Solidarity surcharge (Solidaritätszuschlag) |  |

## Section 3: Revenue Recognition

| Scenario | Treatment |
| --- | --- |
| **Default (HGB § 252)** | Accruals basis: income and expenses of the year are booked whatever the payment date. Profits count only when realised at the balance sheet date (Realisationsprinzip) |
| **EÜR (Einnahmen-Überschussrechnung)** | Cash basis under § 4(3) EStG. Open to anyone who is not obliged by law to keep books and close accounts and who does not do so by choice. See the limits tables below |
| **Kleinunternehmer (§ 19 UStG)** | Sales are VAT-exempt and no VAT is shown on the invoice. Revenue is recorded at the full amount received and expenses at the gross amount. See the Kleinunternehmer tables below |
| **Advance payments received** | Shown as a liability ("erhaltene Anzahlungen auf Bestellungen", § 266(3) C.3 HGB) until the work is delivered |
| **Construction contracts** | Profit counts only when realised at the balance sheet date (§ 252(1) no. 4 HGB), so long contracts are normally booked on completion, not by stage of completion |
| **Cross-border services between businesses** | Service bought from a business abroad: the German buyer owes the VAT (§ 13b UStG, reverse charge) and books output VAT and, if entitled, input VAT. Service sold to a business in another EU state: see the VAT Guide for the place of supply |

### EÜR vs Double-Entry Bookkeeping

| Criterion | EÜR | Double-Entry (Bilanzierung) |
| --- | --- | --- |
| Who must use | Nobody must. Freiberufler and businesses with no bookkeeping duty may | Merchants (§ 238 HGB). That includes trading companies (§ 6 HGB), and a GmbH counts as one (§ 13(3) GmbHG). Also commercial businesses and farmers told by the tax office that they crossed a § 141 AO limit |
| Revenue recognition | Cash basis | Accruals basis |
| Balance sheet | Not required | Required (HGB § 242) |
| Filing | Anlage EÜR, sent electronically with the tax return (§ 60(4) EStDV) | Bilanz and GuV, sent as E-Bilanz (§ 5b EStG) |

**Tax-law bookkeeping duty for commercial businesses and farmers**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.gesetze-im-internet.de/ao_1977/__141.html |
| Total turnover of the single business in the calendar year: the duty can start above | EUR 800,000 | § 141(1) no. 1 AO: "von mehr als 800 000 Euro im Kalenderjahr" |
| Profit from the business in the financial year: the duty can start above | EUR 80,000 | § 141(1) no. 4 AO: "einen Gewinn aus Gewerbebetrieb von mehr als 80 000 Euro im Wirtschaftsjahr" |

- **Either limit is enough.** The law joins the tests with "or".
- **The duty does not start by itself.** It starts with the financial year that follows the tax office's notice pointing out the duty (§ 141(2) AO). It ends after the financial year that follows the one in which the tax office finds the limits are no longer crossed.
- **Freelancers are not named.** § 141 AO covers commercial businesses and farmers only, so a Freiberufler has no size-based bookkeeping duty under tax law.
- **Duties from other laws count for tax too.** Whoever must keep books under another law, for example a merchant under the HGB, must meet that duty for tax as well. See § 140 AO at https://www.gesetze-im-internet.de/ao_1977/__140.html

**Commercial-law release for sole merchants**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.gesetze-im-internet.de/hgb/__241a.html |
| Revenue on each of two balance sheet dates in a row: not more than | EUR 800,000 | § 241a HGB: "nicht mehr als jeweils 800 000 Euro Umsatzerlöse" |
| Annual surplus on each of the same two dates: not more than | EUR 80,000 | § 241a HGB: "jeweils 80 000 Euro Jahresüberschuss" |

- **Both limits must be kept**, on two balance sheet dates in a row. A new business is released at once if it keeps both limits on its first balance sheet date.
- **Sole merchants only.** The release is for Einzelkaufleute. Partnerships and companies cannot use it.

**Kleinunternehmer limits: the statute**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.gesetze-im-internet.de/ustg_1980/__19.html |
| Total turnover of the previous calendar year: must not have exceeded | EUR 25,000 | § 19(1) UStG: "im vorangegangenen Kalenderjahr 25 000 Euro nicht überschritten hat" |
| Total turnover of the current calendar year: must not exceed | EUR 100,000 | § 19(1) UStG: "im laufenden Kalenderjahr 100 000 Euro nicht überschreitet" |

**Kleinunternehmer limits: how the ministry applies them**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Einkommensteuer/2026-09-01-anlage-EUER-2026.pdf?__blob=publicationFile&v=2 |
| Business starts during the year: total turnover of the current calendar year must not exceed | EUR 25,000 | EÜR instructions 2026, line 12: "darf der Gesamtumsatz im laufenden Kj. 25.000 € nicht überschreiten" |
| Current-year limit for a business that kept the previous-year limit | EUR 100,000 | EÜR instructions 2026, line 12: "im laufenden Kj. 100.000 € nicht überschreitet" |

- **Both tests must be met.** The previous year and the current year are joined by "and".
- **Crossing a limit during the year.** The sale that takes the total over the limit is already taxed under the normal rules. Sales received before that point stay exempt. The instructions say: "Die bis zum Zeitpunkt der Überschreitung vereinnahmten Umsätze sind steuerfrei."
- **What counts.** Total turnover (Gesamtumsatz) is worked out on payments received. Some exempt sales and sales of fixed assets are left out (§ 19(2) UStG).
- **Waiver.** The business may waive the rule. The waiver binds it for at least five calendar years (§ 19(3) UStG).
- **Invoices.** A Kleinunternehmer must not show VAT on the invoice. The invoice must carry a note that the Kleinunternehmer exemption applies. See § 34a UStDV at https://www.gesetze-im-internet.de/ustdv_1980/__34a.html

## Section 4: Expense Classification

| Expense Type | SKR04 | Tax Treatment | Notes |
| --- | --- | --- | --- |
| Office rent | 6310 | Fully deductible |  |
| Home office (Arbeitszimmer) | 6348/6349 (deductible part / non-deductible part) | Room costs only when the room is the centre of all business and professional work. Otherwise a daily flat amount for days worked mainly at home. See the limits table below | Record room costs separately (§ 4(7) EStG). Daily flat amount: 6347 |
| Motor vehicle (business) | 6500 | Costs are business expenses. Private use is added back by the list-price method or by logbook. See the car table below | Fahrtenbuch is the alternative to the list-price method |
| Entertainment (business meals) | 6640/6644 | Deductible in part only. See the limits table and the entertainment table below | Record separately. Note place, date, participants, occasion and amount |
| Gifts to business partners | 6610/6620 (deductible / not deductible) | Deductible only up to the yearly limit per recipient. See the limits table below | Record separately. The giver may pay a flat-rate tax for the recipient under § 37b EStG |
| Travel expenses | 6650/6670 (employees / owner) | Travel costs deductible. Meals only at the flat daily amounts. See the meal table below |  |
| Software subscriptions | 6837 | Fully deductible as operating expense |  |
| Professional fees | 6827/6825 (accountant / legal) | Fully deductible |  |
| Bank charges | 6855 | Fully deductible |  |
| Training | 6821 | Fully deductible | Must relate to current business |
| Fines and penalties | none | NOT deductible | § 4 Abs. 5 Nr. 8 EStG |
| Trade tax (Gewerbesteuer) | see Tax Accounts | NOT a business expense for tax | § 4(5b) EStG |
| Private withdrawals (Privatentnahme) | 2100 (SKR04) | NOT deductible | Equity movement |

**Limits for gifts, entertainment and the home office**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.gesetze-im-internet.de/estg/__4.html |
| Gifts to people who are not employees: deductible only if the cost of everything given to one recipient in the financial year is not more than | EUR 50 | § 4(5) no. 1 EStG: "insgesamt 50 Euro nicht übersteigen" |
| Business entertainment: share of the reasonable and documented costs that may be deducted | 70% | § 4(5) no. 2 EStG: "soweit sie 70 Prozent der Aufwendungen übersteigen" |
| Home office room that is the centre of all business and professional work: yearly flat amount that may be taken in place of the actual costs | EUR 1,260 | § 4(5) no. 6b EStG: "pauschal ein Betrag von 1 260 Euro (Jahrespauschale)" |
| Daily flat amount for each calendar day on which work is done mainly at home and no first place of work is visited | EUR 6 | § 4(5) no. 6c EStG: "ein Betrag von 6 Euro (Tagespauschale)" |
| Yearly cap on the daily flat amounts | EUR 1,260 | § 4(5) no. 6c EStG: "höchstens 1 260 Euro im Wirtschafts- oder Kalenderjahr" |

- **Gifts: a cliff, not an allowance.** Above the limit the whole cost for that recipient is lost, not just the excess. The statute measures "Anschaffungs- oder Herstellungskosten" and does not say net or gross.
- **Home office room.** Costs of the room and its furnishing are not deductible at all unless the room is the centre of the whole business and professional activity. If it is, the client takes the actual costs or the yearly flat amount. The flat amount falls by one twelfth for each full month in which the room is not the centre.
- **Daily flat amount.** It needs no separate room. If no other workplace is permanently available, it is also allowed on days with work away from home. It cannot be taken for a home whose costs are deducted as a second household, or next to the room deduction.
- **Older material is loose here.** It offers "proportional costs if dedicated room". A dedicated room is not enough: the room must be the centre of all the work.
- **Fines.** Fines, administrative penalties and warning charges set by a German court or authority, or by an EU state or EU body, are not deductible (§ 4(5) no. 8 EStG).
- **Separate recording.** Gifts, entertainment, guest houses, hunting and yachts, the home office room and unreasonable lifestyle costs must be recorded one by one and apart from other expenses. If they are not, they cannot be deducted (§ 4(7) EStG).

**Entertainment: as the ministry puts it for 2026**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Einkommensteuer/2026-09-01-anlage-EUER-2026.pdf?__blob=publicationFile&v=2 |
| Deductible share | 70% | EÜR instructions 2026, line 64: "sind zu 70 % abziehbar und zu 30 % nicht abziehbar" |
| Non-deductible share | 30% | Same sentence |
| Input VAT on the entertainment costs | deductible, as far as the costs are reasonable and documented | EÜR instructions 2026, line 64: "Die hierauf entfallende Vorsteuer ist allerdings abziehbar" |

- **Proof.** Written details of place, date, participants, occasion and amount. For a restaurant, occasion and participants are enough, and the restaurant bill must be attached (§ 4(5) no. 2 EStG).
- **Removed.** Older material tied the input VAT to a gross amount per bill. No official page read for this Guide prints such an amount, so it is gone.

**Meal flat amounts on business trips in Germany**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.gesetze-im-internet.de/estg/__9.html |
| Away from home and the first place of work for 24 hours, per calendar day | EUR 28 | § 9(4a) EStG: "28 Euro für jeden Kalendertag" |
| Day of arrival and day of departure on a trip with an overnight stay, each | EUR 14 | § 9(4a) EStG: "jeweils 14 Euro für den An- und Abreisetag" |
| Day without overnight stay, away from home and the first place of work for more than 8 hours | EUR 14 | § 9(4a) EStG: "14 Euro für den Kalendertag, an dem der Arbeitnehmer ohne Übernachtung" |

- **Business owners too.** § 4(5) no. 5 EStG applies these employee amounts to the owner's own business trips.
- **Three months.** The flat amounts stop after the first three months of a longer job at the same place.
- **Abroad.** Country amounts set by the ministry replace them. They are not listed here.

**Private use of a business car**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.gesetze-im-internet.de/estg/__6.html |
| Business use above which the list-price method applies | 50% | § 6(1) no. 4 EStG: "das zu mehr als 50 Prozent betrieblich genutzt wird" |
| Private use per calendar month, as a share of the German list price at first registration plus extras, VAT included | 1% | § 6(1) no. 4 EStG: "für jeden Kalendermonat mit 1 Prozent des inländischen Listenpreises" |

- **Logbook.** The client may prove the real private share with a proper logbook instead.
- **Car not used mostly for business.** The list-price method is not open. The private share of the total car costs is added back.
- **Electric and plug-in hybrid cars** have a reduced list price under the same paragraph. Not covered here.
- **Trips between home and the business premises** have their own add-back for a car under the list-price method (§ 4(5) no. 6 EStG). Not covered here. See https://www.gesetze-im-internet.de/estg/__4.html

## Section 5: Asset vs Expense Thresholds (GWG Rules)

### GWG (Geringwertige Wirtschaftsgüter): § 6 Abs. 2/2a EStG

| Cost of the single asset, less the input VAT it contains | Treatment | Note |
| --- | --- | --- |
| Source | all figures below | https://www.gesetze-im-internet.de/estg/__6.html |
| Not more than EUR 250 | Expense at once. No special register | § 6(2) EStG asks for the register only for assets "deren Wert 250 Euro übersteigt" |
| More than EUR 250 and not more than EUR 800 | Expense at once (a choice), or depreciate over the useful life. If expensed at once, enter the asset in a special running register, unless the books already show the data | § 6(2) EStG: "für das einzelne Wirtschaftsgut 800 Euro nicht übersteigen" |
| More than EUR 250 and not more than EUR 1,000 | Alternative for the whole year: one pool (Sammelposten), released at one fifth a year over five years | § 6(2a) EStG: "für das einzelne Wirtschaftsgut 250 Euro, aber nicht 1 000 Euro übersteigen" |
| More than EUR 800 if the pool is not chosen, more than EUR 1,000 if it is | Capitalise and depreciate over the useful life | Asset accounts (Class 0). § 6(2) EStG allows the write-off at once only where cost does "800 Euro nicht übersteigen" |

- **Which assets.** Movable, depreciable fixed assets that can be used on their own. A part that only works together with other assets does not qualify.
- **Thresholds and VAT.** The law measures cost "vermindert um einen darin enthaltenen Vorsteuerbetrag", that is, less the input VAT contained in it. The official pages read for this Guide do not say how a Kleinunternehmer applies this, so this Guide does not say either.
- **Pool rules.** The pool is released in the year it is formed and the four years after, one fifth each year. If a pooled asset is sold or scrapped, the pool is not reduced. The choice of the pool covers all assets of that financial year in the pool range. With the pool, only assets up to the lower limit may still be expensed at once.
- **EÜR filers follow the same rules** (§ 4(3) EStG). Expensed GWG are not entered in the asset schedule Anlage AVEÜR.
- **Recording.** Use the GWG write-off account or the asset account from the chart in Section 2.

### Standard Depreciation Rates (AfA-Tabelle)

Straight-line depreciation spreads the cost evenly over the normal useful life. In the year of purchase it is cut by one twelfth for each full month before the month of purchase (§ 7(1) EStG). The ministry's table gives useful lives in years, not percentages. This Guide does not turn years into rates.

**Useful lives: the ministry's table for generally usable assets (AfA-Tabelle AV)**

| Asset | Useful life in years | Note |
| --- | --- | --- |
| Source | all periods below | https://www.bundesfinanzministerium.de/Content/DE/Standardartikel/Themen/Steuern/Weitere_Steuerthemen/Betriebspruefung/AfA-Tabellen/Ergaenzende-AfA-Tabellen/AfA-Tabelle_AV.pdf?__blob=publicationFile&v=3 |
| Cars and estate cars (Personenkraftwagen und Kombiwagen) | 6 | Table no. 4.2.1 |
| Trucks (Lastkraftwagen, Sattelschlepper, Kipper) | 9 | Table no. 4.2.3 |
| Office furniture (Büromöbel) | 13 | Table no. 6.15 |
| Workstations, personal computers, notebooks and their peripherals | 3 | Table no. 6.14.3.2. See the one-year rule below |
| Telephone systems (Fernsprechnebenstellenanlagen) | 10 | Table no. 6.13.1 |
| Communication devices, general (Kommunikationsendgeräte) | 8 | Table no. 6.13.2.1 |
| Mobile phones (Mobilfunkendgeräte) | 5 | Table no. 6.13.2.2 |
| Photocopiers (Vervielfältigungsgeräte) | 7 | Table no. 6.14.10 |
| Cash registers (Registrierkassen) | 6 | Table no. 6.14.7 |
| Shredders (Reißwölfe, Aktenvernichter) | 8 | Table no. 6.14.13 |
| Goodwill of a commercial business | 15 | Not in the table. Set by § 7(1) EStG |

- **Scope of the table.** It applies to assets bought or made after 31 December 2000. A sector table, where one exists, comes first for businesses of that sector.
- **Computers and software: one year.** The ministry accepts a useful life of one year for computer hardware, with its peripherals, and for operating and application software for data entry and processing. The cost can then be deducted in full in the year of purchase. EÜR filers must still list these assets in Anlage AVEÜR. The instructions say: "kann eine betriebsgewöhnliche Nutzungsdauer von einem Jahr" be assumed. See https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Einkommensteuer/2026-09-01-anlage-EUER-2026.pdf?__blob=publicationFile&v=2
- **Tax only.** The ministry's text deals with tax depreciation. It says nothing about the commercial-law accounts.
- **Removed.** Older material gave a useful life for standard software and yearly rates worked out from the years. The table has no software line and prints no rates, so both are gone.

**Buildings: yearly rates set by law**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.gesetze-im-internet.de/estg/__7.html |
| Building held as a business asset, not used for housing, building application after 31 March 1985 | 3% | § 7(4) no. 1 EStG: "gestellt worden ist, jährlich 3 Prozent" |
| Other building, completed after 31 December 2022 | 3% | § 7(4) no. 2a EStG: "nach dem 31. Dezember 2022 fertiggestellt worden sind, jährlich 3 Prozent" |
| Other building, completed before 1 January 2023 and after 31 December 1924 | 2% | § 7(4) no. 2b EStG: "fertiggestellt worden sind, jährlich 2 Prozent" |
| Other building, completed before 1 January 1925 | 2.5% | § 7(4) no. 2c EStG: "jährlich 2,5 Prozent" |

- **Shorter real life.** If the building's real useful life is shorter than the life these rates imply, the client may depreciate over the real life (§ 7(4) sentence 2 EStG). This needs proof and is a case to refer.

### Declining Balance Option (2025-2027)

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.gesetze-im-internet.de/estg/__7.html |
| Highest declining-balance rate, applied to the book value | 30% | § 7(2) EStG: "und 30 Prozent nicht übersteigen" |
| Electric vehicles bought in the same window: share of cost deductible in the year of purchase | 75% | § 7(2a) EStG: "im Jahr der Anschaffung 75 Prozent" |

- **Window.** Movable fixed assets bought or made after 30 June 2025 and before 1 January 2028.
- **Second cap.** The rate may be at most three times the straight-line rate for the asset. The law says "das Dreifache" and gives no number.
- **Switching.** Moving from declining-balance to straight-line later is allowed (§ 7(3) EStG). Extraordinary write-downs are not allowed while the declining-balance method runs.
- **Electric vehicles.** After the first year the law sets a smaller share for each of the five years that follow, stated in words (§ 7(2a) EStG). The schedule cannot be combined with special depreciation.

## Section 6: P&L Format (GuV: Gewinn- und Verlustrechnung)

HGB § 275 prescribes two formats. The **Gesamtkostenverfahren** (total cost method, by nature of expense) is standard for SMEs. The lines below follow § 275(2) HGB as it reads now: https://www.gesetze-im-internet.de/hgb/__275.html

~~~
GEWINN- UND VERLUSTRECHNUNG (Gesamtkostenverfahren)
Für das Geschäftsjahr [date]

 1. Umsatzerlöse (Revenue)                                   xxx
 2. Erhöhung/Verminderung des Bestands (Inventory changes)   xxx
 3. Andere aktivierte Eigenleistungen                        xxx
 4. Sonstige betriebliche Erträge                            xxx
 5. Materialaufwand (Cost of materials)
    a) Roh-, Hilfs- und Betriebsstoffe, bezogene Waren      (xxx)
    b) Bezogene Leistungen                                  (xxx)
 6. Personalaufwand (Personnel costs)
    a) Löhne und Gehälter                                   (xxx)
    b) Soziale Abgaben, Altersversorgung                    (xxx)
 7. Abschreibungen (Depreciation)                           (xxx)
 8. Sonstige betriebliche Aufwendungen                      (xxx)
 9. Erträge aus Beteiligungen                                xxx
10. Erträge aus anderen Wertpapieren und Ausleihungen        xxx
11. Sonstige Zinsen und ähnliche Erträge                     xxx
12. Abschreibungen auf Finanzanlagen                        (xxx)
13. Zinsen und ähnliche Aufwendungen                        (xxx)
14. Steuern vom Einkommen und vom Ertrag                    (xxx)
                                                            -----
15. ERGEBNIS NACH STEUERN                                    xxx
16. Sonstige Steuern                                        (xxx)
                                                            -----
17. JAHRESÜBERSCHUSS / JAHRESFEHLBETRAG                      xxx
~~~

The older layout with a line "Ergebnis der gewöhnlichen Geschäftstätigkeit" and separate extraordinary items is no longer in the law. Subtotals such as Gesamtleistung, Betriebsergebnis and Finanzergebnis are common in practice but are not statutory lines.

Micro companies (Kleinstkapitalgesellschaft) may use a short format with eight lines: revenue, other income, cost of materials, personnel costs, depreciation, other expenses, taxes, and the result for the year (§ 275(5) HGB). Small and medium-sized companies may combine lines 1 to 5 into one line called "Rohergebnis": https://www.gesetze-im-internet.de/hgb/__276.html

## Section 7: Balance Sheet Format (Bilanz)

HGB § 266 prescribes a two-sided (account form) layout for the Bilanz. Small entities may use an abbreviated version. See https://www.gesetze-im-internet.de/hgb/__266.html

~~~
AKTIVA (Assets)                        PASSIVA (Equity & Liabilities)

A. Anlagevermögen (Non-current)        A. Eigenkapital (Equity)
   I.  Immaterielle Vermögensgeg.         I.   Gezeichnetes Kapital
   II. Sachanlagen                        II.  Kapitalrücklage
   III.Finanzanlagen                      III. Gewinnrücklagen
                                          IV.  Gewinn-/Verlustvortrag
B. Umlaufvermögen (Current)               V.   Jahresüberschuss/-fehlbetrag
   I.  Vorräte
   II. Forderungen, sonstige Verm.     B. Rückstellungen (Provisions)
   III.Wertpapiere
   IV. Kassenbestand, Bankguthaben     C. Verbindlichkeiten (Liabilities)

C. Rechnungsabgrenzungsposten          D. Rechnungsabgrenzungsposten
   (Prepaid expenses)                     (Deferred income)

D. Aktive latente Steuern              E. Passive latente Steuern
E. Aktiver Unterschiedsbetrag aus
   der Vermögensverrechnung
~~~

Small companies need show only the items marked with letters and Roman numerals. Micro companies (§ 267a HGB, Kleinstkapitalgesellschaft) need show only the items marked with letters (§ 266(1) HGB).

## Section 8: Bank Reconciliation Patterns

### German Bank Statement Formats

| Bank | Format | Standard | Key Fields |
| --- | --- | --- | --- |
| Sparkasse | MT940 / CAMT.053 | ISO standard 20022 | Buchungsdatum, Betrag, Verwendungszweck |
| Deutsche Bank | MT940 / CSV |  | Wertstellungsdatum, Buchungstext, Betrag |
| Commerzbank | CAMT.053 / CSV | ISO standard 20022 | Buchungsdatum, Name, Verwendungszweck, Betrag |
| Volksbank/Raiffeisenbank | MT940 / CAMT.053 |  | Buchungstag, Empfänger/Auftraggeber, Betrag |
| N26 / Online banks | CSV | Proprietary | Date, Payee, Amount, Reference |

### Common German Transaction Descriptions

| Pattern | Likely Classification |
| --- | --- |
| GUTSCHRIFT / HABEN | Credit: income or refund |
| LASTSCHRIFT / SOLL | Direct debit: expense |
| DAUERAUFTRAG | Standing order: rent, insurance |
| KARTENZAHLUNG / EC-KARTE | Card payment: check merchant |
| GEHALT / LOHN | Salary payment to employee (6000) |
| FINANZAMT / STEUERZAHLUNG | Tax payment: exclude from P&L |
| MIETE | Rent payment (6310) |
| VERSICHERUNG | Insurance (6400) |
| KRANKENKASSE / SOZIALVERSICHERUNG | Social security contribution (6100) |
| ÜBERTRAG / UMBUCHUNG | Internal transfer: exclude |

### DATEV Import

Most German accountants use DATEV. Bank transactions are imported via DATEV Unternehmen Online or the DATEV CSV format. The mapping from bank categories to SKR03/SKR04 accounts is the core bookkeeping task.

## Section 9: Micro-Entity / Small Business Simplifications

### HGB Size Classification (§ 267/267a)

**Small and medium-sized companies**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.gesetze-im-internet.de/hgb/__267.html |
| Small company: balance sheet total not more than | EUR 7,500,000 | § 267(1) HGB: "7 500 000 Euro Bilanzsumme" |
| Small company: revenue in the twelve months before the balance sheet date not more than | EUR 15,000,000 | § 267(1) HGB: "15 000 000 Euro Umsatzerlöse in den zwölf Monaten vor dem Abschlußstichtag" |
| Small company: employees on yearly average not more than | 50 | § 267(1) HGB: "Im Jahresdurchschnitt fünfzig Arbeitnehmer" |
| Medium-sized company: balance sheet total not more than | EUR 25,000,000 | § 267(2) HGB: "25 000 000 Euro Bilanzsumme" |
| Medium-sized company: revenue in the twelve months before the balance sheet date not more than | EUR 50,000,000 | § 267(2) HGB: "50 000 000 Euro Umsatzerlöse in den zwölf Monaten vor dem Abschlußstichtag" |
| Medium-sized company: employees on yearly average not more than | 250 | § 267(2) HGB: "Im Jahresdurchschnitt zweihundertfünfzig Arbeitnehmer" |
| Large company | goes over at least two of the three medium-sized limits | § 267(3) HGB |

**Micro companies (Kleinstkapitalgesellschaften)**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.gesetze-im-internet.de/hgb/__267a.html |
| Balance sheet total not more than | EUR 450,000 | § 267a(1) HGB: "450 000 Euro Bilanzsumme" |
| Revenue in the twelve months before the balance sheet date not more than | EUR 900,000 | § 267a(1) HGB: "900 000 Euro Umsatzerlöse in den zwölf Monaten vor dem Abschlussstichtag" |
| Employees on yearly average not more than | 10 | § 267a(1) HGB: "im Jahresdurchschnitt zehn Arbeitnehmer" |

- **Two-of-three test.** A company belongs to a class if it stays within at least two of that class's three limits.
- **Two balance sheet dates in a row.** The class changes only when the limits are crossed, or no longer crossed, on two balance sheet dates in a row. For a new or converted company the first balance sheet date decides (§ 267(4) HGB).
- **Counting employees.** One quarter of the sum of the staff counts on 31 March, 30 June, 30 September and 31 December, with staff abroad and without trainees (§ 267(5) HGB).
- **Always large.** A capital-market company in the sense of § 264d HGB always counts as large.
- **Never micro.** Investment companies, equity-participation companies and pure holding companies cannot be micro companies (§ 267a(3) HGB).

### Simplifications by Size

| Requirement | Kleinstkapitalgesellschaft | Kleine | Mittelgroße |
| --- | --- | --- | --- |
| Balance sheet | Letter items only (§ 266(1) HGB) | Letter and Roman-numeral items only (§ 266(1) HGB) | Full |
| GuV (P&L) | Short form with eight lines allowed (§ 275(5) HGB) | Lines 1 to 5 may be combined as "Rohergebnis" (§ 276 HGB) | Lines 1 to 5 may be combined as "Rohergebnis" (§ 276 HGB) |
| Notes (Anhang) | NOT required if certain details are given under the balance sheet (§ 264(1) HGB) | Required | Required |
| Management report (Lagebericht) | NOT required | NOT required (§ 264(1) HGB) | Required |
| Audit | NOT required | NOT required (§ 316(1) HGB) | Required |
| Publication | Balance sheet only. It may be deposited with the company register instead of being published (§ 326(2) HGB) | Balance sheet and notes only (§ 326(1) HGB) | Statements, management report and audit opinion (§ 325 HGB) |
| E-Bilanz | Required for tax | Required for tax | Required for tax |

- **Deadlines.** The statements are drawn up in the first three months of the new financial year. Small companies may take longer if that fits an orderly course of business, but no more than six months. See § 264(1) HGB at https://www.gesetze-im-internet.de/hgb/__264.html
- **Filing.** The documents go to the company register within one year after the balance sheet date. See § 325(1a) HGB at https://www.gesetze-im-internet.de/hgb/__325.html and the reliefs at https://www.gesetze-im-internet.de/hgb/__326.html
- **Correction.** Older material names the Bundesanzeiger as the place of deposit. The law now names the company register (Unternehmensregister).

### Sole Traders and Freelancers

| Who | Test | Obligation |
| --- | --- | --- |
| Sole merchant within both § 241a HGB limits on two balance sheet dates in a row | See the release table in Section 3 | EÜR allowed (cash-basis simplified accounts) |
| Commercial business or farmer over either § 141 AO limit | See the duty table in Section 3. The duty starts only after the tax office's notice | Full double-entry bookkeeping and yearly closing |
| Freiberufler (any size) | None | EÜR permitted regardless of size (unless they opt for Bilanz) |

## Section 10: Interaction with Tax Skills

| Tax Guide | How Bookkeeping Connects |
| --- | --- |
| **de-self-employed-income-tax** | Profit from GuV/EÜR feeds Anlage G (Gewerbe) or Anlage S (Freiberufler) of the Einkommensteuererklärung. Non-deductible items from Section 4 (the non-deductible share of entertainment, gifts over the limit, fines, trade tax) must be added back. |
| **de-vat-return** | VAT accounts (1400 and 1406 for input VAT, 3800 and 3806 for output VAT, in SKR04) feed the Umsatzsteuer-Voranmeldung, sent electronically. Monthly or quarterly: see the VAT return table below. Input VAT (Vorsteuer) is netted against output VAT (Umsatzsteuer). |
| **de-trade-tax** | Gewerbesteuer is worked out from the adjusted trade profit. Financing costs are partly added back (Hinzurechnungen): see the trade tax table below. |
| **de-crypto-tax** | Gains on crypto held privately are private sales when sold within one year of purchase. Bookkeeping must track acquisition cost per wallet and exchange. See that Guide for the method. |

**VAT return rhythm**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.gesetze-im-internet.de/ustg_1980/__18.html |
| VAT of the previous calendar year above which the return period is the month, not the quarter | EUR 9,000 | § 18(2) UStG: "mehr als 9 000 Euro" |
| VAT of the previous calendar year up to which the tax office may release the business from advance returns | EUR 2,000 | § 18(2) UStG: "nicht mehr als 2 000 Euro" |

- **Default.** The return period is the calendar quarter. The return and the payment are due by the tenth day after the period ends (§ 18(1) UStG).
- **New businesses, tax periods 2021 to 2026.** The expected VAT of the current year decides the period. If the business ran for only part of the previous year, that year's VAT is scaled up to a full year. Outside those tax periods the basic rule applies: monthly returns in the year of start and in the year after (§ 18(2) UStG).
- **Refund cases.** A business with a surplus in its favour above the first amount in the table may choose monthly returns (§ 18(2a) UStG).

**Trade tax: add-back of financing costs**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.gesetze-im-internet.de/gewstg/__8.html |
| Allowance taken off the sum of the financing items before anything is added back | EUR 200,000 | § 8 no. 1 GewStG: "soweit die Summe den Betrag von 200 000 Euro übersteigt" |

- **Step 1: add up the items, each at the share the law gives.** Interest and other payments for debt: in full. Annuities and permanent burdens: in full. Profit shares of a silent partner: in full. Rent, lease and leasing payments for movable fixed assets owned by someone else: one fifth (and only half of that for electric vehicles, certain plug-in hybrids and bicycles). Rent, lease and leasing payments for immovable fixed assets owned by someone else: one half. Payments for the time-limited use of rights such as licences and concessions: one quarter.
- **Step 2: take off the allowance** in the table.
- **Step 3: add back one quarter** of what is left. The law gives all these shares in words ("ein Viertel", "einem Fünftel", "der Hälfte"), so no percentages are printed here.
- **Correction.** Older material says a flat share of rent and a flat share of interest is added back. That skips the different shares per item and the allowance.
- **Bookkeeping consequence.** Keep interest, leases of movable assets, rent of immovable assets and licence fees on separate accounts, so the add-back can be worked out.

## Section 11: E-invoicing between German businesses

- **The duty.** For a supply to another business, an invoice must be issued within six months. If supplier and customer are both established in Germany, it must be an e-invoice: an invoice issued, sent and received in a structured electronic format that allows electronic processing. The format must meet the European standard for e-invoicing. The two parties may agree on another structured format only if the required data can be extracted from it, correctly and completely, into a format that meets the standard or works with it. Sales that are exempt under § 4 nos. 8 to 29 UStG are outside the duty. See § 14(1) and (2) UStG at https://www.gesetze-im-internet.de/ustg_1980/__14.html
- **A plain PDF is not an e-invoice.** An invoice on paper or in another electronic format, for example a PDF with no data set inside it, is an "other invoice" (sonstige Rechnung). A hybrid file such as ZUGFeRD, a PDF that carries the structured data, can be an e-invoice: see Formats below.
- **Receiving.** Since 1 January 2025 every business in Germany must be able to receive e-invoices, Kleinunternehmer included. The customer's consent is not needed. E-invoices may come by e-mail, and no separate inbox just for them is needed. See the ministry's letter of 15 October 2025: https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Umsatzsteuer/Umsatzsteuer-Anwendungserlass/2025-10-15-einfuehrung-obligatorische-e-rechnung.pdf?__blob=publicationFile&v=5
- **Formats.** The same letter names XRechnung, and ZUGFeRD from version 2.0.1 without the profiles MINIMUM and BASIC-WL, as formats that meet the European standard.
- **Issuing: transition for sales made in 2025 and 2026.** Until 31 December 2026 a paper invoice may still be sent, or, with the customer's consent, an invoice in another electronic format.
- **Issuing: transition for sales made in 2027.** The same relief runs until 31 December 2027 only if the issuer's total turnover of the previous calendar year is within the limit in the table below. Invoices sent by EDI also have until 31 December 2027.

**E-invoicing: turnover limit for the 2027 relief**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.gesetze-im-internet.de/ustg_1980/__27.html |
| Issuer's total turnover (§ 19(2) UStG) of the previous calendar year: not more than | EUR 800,000 | § 27(38) no. 2 UStG: "im vorangegangenen Kalenderjahr nicht mehr als 800 000 Euro betragen hat" |

**Small invoices**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.gesetze-im-internet.de/ustdv_1980/__33.html |
| Invoice total up to which fewer details are needed and the invoice may always be an other invoice | EUR 250 | § 33 UStDV: "Eine Rechnung, deren Gesamtbetrag 250 Euro nicht übersteigt" |

- **Also always allowed as other invoices:** invoices issued by a Kleinunternehmer (§ 34a UStDV) and passenger tickets (§ 34 UStDV).
- **Bookkeeping consequence.** Store incoming e-invoices in their structured form and keep them for the invoice period in Section 1.

## The method, step by step

1. Decide whether the client must keep double-entry books. Merchants must under § 238 HGB, and § 140 AO carries that duty into tax law. A sole merchant within both § 241a HGB limits is released. Other commercial businesses and farmers must once the tax office has told them that a § 141 AO limit was crossed. https://www.gesetze-im-internet.de/ao_1977/__141.html
2. If there is no duty, and always for a Freiberufler, the client may use the cash-basis EÜR under § 4(3) EStG. Fixed assets, GWG and depreciation rules still apply, and fixed assets go into a running register. https://www.gesetze-im-internet.de/estg/__4.html
3. Settle the VAT status before the first invoice: Kleinunternehmer under § 19 UStG or normal taxation. Test both turnover limits in Section 3. https://www.gesetze-im-internet.de/ustg_1980/__19.html
4. Set the VAT return period under § 18 UStG from last year's VAT (Section 10). https://www.gesetze-im-internet.de/ustg_1980/__18.html
5. Set up the chart (SKR03 or SKR04) and record every transaction one by one, completely, correctly, in time and in order. Record cash daily. Never overwrite an entry. https://www.gesetze-im-internet.de/ao_1977/__146.html
6. Issue invoices within six months and as e-invoices where § 14 UStG demands it. Make sure the client can receive e-invoices (Section 11). https://www.gesetze-im-internet.de/ustg_1980/__14.html
7. Book the restricted expenses on their own accounts as § 4(7) EStG demands: gifts, entertainment, home office room. Apply the limits in Section 4. If they are mixed into other accounts, the deduction is lost. https://www.gesetze-im-internet.de/estg/__4.html
8. For each fixed asset, test the GWG limits of § 6(2) and (2a) EStG first. Otherwise capitalise it and depreciate under § 7 EStG with the useful life from the ministry's table (Section 5). https://www.gesetze-im-internet.de/estg/__6.html
9. At year end, a bookkeeping business draws up the balance sheet and the P&L (§ 242 HGB) and sends them as E-Bilanz (§ 5b EStG). An EÜR business sends the Anlage EÜR electronically (§ 60(4) EStDV). https://www.gesetze-im-internet.de/estg/__5b.html and https://www.gesetze-im-internet.de/estdv_1955/__60.html
10. For tax, add back what is not deductible (Section 4) and pass the figures to the income tax, VAT and trade tax Guides (Section 10). https://www.gesetze-im-internet.de/gewstg/__8.html
11. Keep every document for the period in the retention table in Section 1. Doing this step early matters: a voucher thrown away too soon cannot be replaced. https://www.gesetze-im-internet.de/ao_1977/__147.html

## Ask the client first

- What is the legal form, and is the business entered in the commercial register (sole merchant, partnership, GmbH or UG, Freiberufler)?
- What were turnover and profit in the last two financial years, and has the tax office sent a notice to start keeping books?
- Is the business a Kleinunternehmer? What was last year's total turnover, what is expected this year, and was the rule ever waived?
- Who are the customers: German businesses (e-invoice duty), consumers, or customers abroad?
- Is anything used both privately and for the business: a car, a room at home, a phone? For a room at home, is it the centre of all the client's work?
- Which accounting software and which chart (SKR03 or SKR04) are in use, and who records the cash?

## When to refuse or refer

- Annual financial statements of companies, audits, publication questions and group accounts. Refer to a Steuerberater or Wirtschaftsprüfer.
- Banks, insurers and securities institutions: they have their own accounting and retention rules.
- Farming and forestry: different financial year and extra rules.
- Payroll accounting and social security.
- Cross-border VAT beyond the basic reverse charge: place of supply, intra-EU supplies, the one-stop shop. See the German VAT Guide.
- Working out income tax, corporation tax or trade tax. This Guide only feeds them.
- Electric and hybrid company cars, and any car whose private use is disputed.
- A building depreciated over a shorter real useful life.
- Cash registers and their technical security device (§ 146a AO).
- IFRS accounts.
- Exact account numbers for one client: Section 2 shows DATEV's base account numbers for 2026. Sector charts and a client's own chart can differ. Confirm every number in the client's software.
- How a Kleinunternehmer measures the GWG limits, and whether the gift limit is net or gross: the official pages read for this Guide do not say.

## Sources

- AO § 140, § 141, § 146, § 147 (bookkeeping duty, order rules, retention): https://www.gesetze-im-internet.de/ao_1977/__140.html and https://www.gesetze-im-internet.de/ao_1977/__141.html and https://www.gesetze-im-internet.de/ao_1977/__146.html and https://www.gesetze-im-internet.de/ao_1977/__147.html
- EGAO Art. 97 § 19a (start of the shorter voucher period): https://www.gesetze-im-internet.de/aoeg_1977/art_97__19a.html
- GmbHG § 13 (a GmbH is a trading company): https://www.gesetze-im-internet.de/gmbhg/__13.html
- HGB § 1, § 6, § 238, § 240, § 241a, § 242 (merchants, bookkeeping duty, release): https://www.gesetze-im-internet.de/hgb/__1.html and https://www.gesetze-im-internet.de/hgb/__6.html and https://www.gesetze-im-internet.de/hgb/__238.html and https://www.gesetze-im-internet.de/hgb/__240.html and https://www.gesetze-im-internet.de/hgb/__241a.html and https://www.gesetze-im-internet.de/hgb/__242.html
- HGB § 252, § 257 (valuation principles, retention): https://www.gesetze-im-internet.de/hgb/__252.html and https://www.gesetze-im-internet.de/hgb/__257.html
- HGB § 264, § 266, § 267, § 267a, § 275, § 276 (statements, layouts, size classes): https://www.gesetze-im-internet.de/hgb/__264.html and https://www.gesetze-im-internet.de/hgb/__266.html and https://www.gesetze-im-internet.de/hgb/__267.html and https://www.gesetze-im-internet.de/hgb/__267a.html and https://www.gesetze-im-internet.de/hgb/__275.html and https://www.gesetze-im-internet.de/hgb/__276.html
- HGB § 316, § 325, § 326 (audit, publication): https://www.gesetze-im-internet.de/hgb/__316.html and https://www.gesetze-im-internet.de/hgb/__325.html and https://www.gesetze-im-internet.de/hgb/__326.html
- EStG § 2, § 4, § 4a, § 5, § 5b, § 6, § 7, § 9, § 37b: https://www.gesetze-im-internet.de/estg/__2.html and https://www.gesetze-im-internet.de/estg/__4.html and https://www.gesetze-im-internet.de/estg/__4a.html and https://www.gesetze-im-internet.de/estg/__5.html and https://www.gesetze-im-internet.de/estg/__5b.html and https://www.gesetze-im-internet.de/estg/__6.html and https://www.gesetze-im-internet.de/estg/__7.html and https://www.gesetze-im-internet.de/estg/__9.html and https://www.gesetze-im-internet.de/estg/__37b.html
- EStDV § 60 (EÜR sent electronically): https://www.gesetze-im-internet.de/estdv_1955/__60.html
- UStG § 12, § 13b, § 14, § 14b, § 18, § 19, § 27: https://www.gesetze-im-internet.de/ustg_1980/__12.html and https://www.gesetze-im-internet.de/ustg_1980/__13b.html and https://www.gesetze-im-internet.de/ustg_1980/__14.html and https://www.gesetze-im-internet.de/ustg_1980/__14b.html and https://www.gesetze-im-internet.de/ustg_1980/__18.html and https://www.gesetze-im-internet.de/ustg_1980/__19.html and https://www.gesetze-im-internet.de/ustg_1980/__27.html
- UStDV § 33, § 34a (small invoices, Kleinunternehmer invoices): https://www.gesetze-im-internet.de/ustdv_1980/__33.html and https://www.gesetze-im-internet.de/ustdv_1980/__34a.html
- GewStG § 8 (trade tax add-backs): https://www.gesetze-im-internet.de/gewstg/__8.html
- Finance ministry, EÜR form and instructions for 2026, letter of 1 September 2026: https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Einkommensteuer/2026-09-01-anlage-EUER-2026.pdf?__blob=publicationFile&v=2
- Finance ministry, depreciation table for generally usable assets (AfA-Tabelle AV): https://www.bundesfinanzministerium.de/Content/DE/Standardartikel/Themen/Steuern/Weitere_Steuerthemen/Betriebspruefung/AfA-Tabellen/Ergaenzende-AfA-Tabellen/AfA-Tabelle_AV.pdf?__blob=publicationFile&v=3
- Finance ministry, GoBD change letters of 11 March 2024 and 14 July 2025: https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Weitere_Steuerthemen/Abgabenordnung/AO-Anwendungserlass/2024-03-11-aenderung-gobd.pdf?__blob=publicationFile&v=4 and https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Weitere_Steuerthemen/Abgabenordnung/2025-07-14-GoBD-2-aenderung.pdf?__blob=publicationFile&v=4
- Finance ministry, e-invoice letter of 15 October 2025: https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Umsatzsteuer/Umsatzsteuer-Anwendungserlass/2025-10-15-einfuehrung-obligatorische-e-rechnung.pdf?__blob=publicationFile&v=5
- Finance ministry, tax booklet (Steuern von A-Z), 2025 edition: https://www.bundesfinanzministerium.de/Content/DE/Downloads/Broschueren_Bestellservice/steuern-von-a-z.pdf?__blob=publicationFile&v=9

## Disclaimer

This Guide and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this Guide. All outputs must be reviewed and signed off by a qualified professional (such as a Steuerberater or Wirtschaftsprüfer) before filing or acting upon.

> Contributed by OpenAccountants.

> Contributed by Michael Cutajar.

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
