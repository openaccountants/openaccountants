---
name: de-freelance-intake
description: ALWAYS USE THIS SKILL when a user asks for help preparing their German tax returns AND mentions freelancing (Freiberufler), self-employment (Selbstständigkeit), trade business (Gewerbetreibender), contracting, or sole proprietorship (Einzelunternehmer). Trigger on phrases like "help me do my German taxes", "prepare my EStE", "I'm self-employed in Germany", "I'm a Freiberufler", "do my Steuererklärung", "prepare my USt and ESt", or any similar phrasing where the user is a Germany-resident self-employed individual needing tax return preparation. This is the REQUIRED entry point for the Germany self-employed tax workflow -- every other skill in the stack (germany-vat-return, de-income-tax, de-social-contributions, de-trade-tax, de-estimated-tax, de-return-assembly) depends on this skill running first to produce a structured intake package. Uses upload-first workflow -- the user dumps all their documents and the skill infers as much as possible before asking questions. Uses ask_user_input_v0 for structured questions instead of one-at-a-time prose. Built for speed. Germany full-year residents only; self-employed individuals and sole proprietors.
version: 0.1
jurisdiction: DE
tax_year: 2026
last_updated: 2026-09-27
authored_by: OpenAccountants team
review_status: pending_review
trust_label: Written by the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# German freelancer and sole trader tax intake (Freiberufler and Gewerbetreibende)

## Scope

This is the intake and triage Guide for a self-employed individual who lives in Germany: a Freiberufler (§ 18 EStG) or a Gewerbetreibender (§ 15 EStG) running a sole business. It tells an assistant which questions to ask, which documents to collect, which answers change the route, and which specialist Guide takes over. It computes no tax.

- **Primary year:** calendar year 2026, the tax year in force on 25 September 2026. The returns for 2025 are being filed now; see "Filing and payment".
- **Covered:** full-year residents (a home or habitual abode in Germany, § 1(1) EStG: "Wohnsitz oder ihren gewöhnlichen Aufenthalt"), sole proprietors, cash-basis profit (EÜR), up to a small team.
- **Not covered:** non-residents and part-year residents, partnerships as the business itself, GmbH and UG, balance-sheet filers, farming and forestry, payroll. See "When to refuse or refer".
- **Who decides.** The tax office decides the classification and facts like a home office being the centre of all work. Record, test and flag; do not settle.
- **Review.** A Steuerberater should review the work before anything is filed.

### Where each question goes next

| Topic | Specialist Guide |
| --- | --- |
| Income tax return, Anlage EÜR, Anlage S or G, deductions | `de-einkommensteuer-freelancer` |
| VAT advance returns, annual VAT return, Kleinunternehmer, reverse charge | `germany-vat-return` |
| Books or EÜR, record keeping, GoBD, e-invoices, tills | `germany-bookkeeping` |
| Trade tax computation and return | `de-trade-tax` |
| Income tax prepayments | `de-estimated-tax` |
| Health, care and pension contributions, KSK | `de-social-contributions` |
| Shares, funds, interest (Anlage KAP) | `de-capital-gains` |
| Crypto assets | `de-crypto-tax` |
| Rental income | `de-rental-income` |
| Putting the returns together | `de-return-assembly` |

## Ask the client first

Ask in batches of two or three. Skip anything the documents already answer.

- **Year and residency.** Which tax year are we preparing? Did you live in Germany (a home or your habitual abode) for all of it?
- **What you do.** Describe the work, the training it rests on, and who pays you. Do you also sell goods, earn commissions, broker deals or resell bought-in work?
- **Registration.** When did you start? Did you register a trade (Gewerbeanmeldung) with the municipality, or only report to the tax office? Did you send the tax office the registration questionnaire (Fragebogen zur steuerlichen Erfassung), and do you have a tax number?
- **Structure.** Do you work alone, or share profits with a partner (GbR or other partnership)? Is there a GmbH or UG? Are you entered in the commercial register (Handelsregister)?
- **Staff.** Do you employ anyone? How many, and are they subject to social insurance or on a Minijob?
- **VAT.** What was your total turnover in 2025, and what is it so far in 2026? Do your invoices show VAT, or do they carry the small-business note? Have you ever waived the Kleinunternehmer rule? How much VAT did you pay for 2025, and do you file monthly or quarterly? Do you have a one-month extension (Dauerfristverlängerung)?
- **Profit method.** Do you file an EÜR or a balance sheet? Has the tax office ever sent a notice telling you to keep books?
- **Prepayments.** Have you received an income tax prepayment notice (Vorauszahlungsbescheid)? What did your last assessment (Steuerbescheid) show?
- **Social insurance.** Is your work teaching or coaching, nursing or child care, midwifery, art or publishing, or a craft entered in the Handwerksrolle? Do you work, on a lasting basis, essentially for one client? Are you in statutory or private health insurance? Are you insured through the Künstlersozialkasse?
- **Other income.** Salary, rent, investments, crypto, a share in a partnership, foreign income?
- **Church tax.** Do you belong to a religious community that levies church tax? Which federal state do you live in, and in which municipality is the business run?

## The method, step by step

1. **Fix the year and test residency.** Full-year residents only ([§ 1 EStG](https://www.gesetze-im-internet.de/estg/__1.html)). Anyone else is referred.
2. **Screen out what this Guide cannot handle** (partnership as the business, corporation, balance sheet, more than five employees). Stop there; see "When to refuse or refer".
3. **Classify the work: Freiberufler or Gewerbe.** Compare what the client does with the list in [§ 18(1) no. 1 EStG](https://www.gesetze-im-internet.de/estg/__18.html) and the definition of a trade in [§ 15(2) EStG](https://www.gesetze-im-internet.de/estg/__15.html). See "Freiberufler or Gewerbe" below.
4. **Check the registration of a new business**: reports and questionnaire within one month ([§ 138 AO](https://www.gesetze-im-internet.de/ao_1977/__138.html)); see below.
5. **Settle the VAT status before reading any invoice**, because it decides whether every amount is recorded net or gross. Test both Kleinunternehmer limits of [§ 19 UStG](https://www.gesetze-im-internet.de/ustg_1980/__19.html). For a client in the normal scheme, set the return period from last year's VAT under [§ 18 UStG](https://www.gesetze-im-internet.de/ustg_1980/__18.html). Then hand VAT to `germany-vat-return`.
6. **Confirm the profit method.** EÜR under [§ 4(3) EStG](https://www.gesetze-im-internet.de/estg/__4.html) unless there is a duty to keep books. A Gewerbetreibender can be brought into bookkeeping by a tax office notice under [§ 141 AO](https://www.gesetze-im-internet.de/ao_1977/__141.html). Details go to `germany-bookkeeping`.
7. **Collect the documents** (list below) and read what they already answer.
8. **Record the prepayments** from the Vorauszahlungsbescheid against the four due dates in [§ 37(1) EStG](https://www.gesetze-im-internet.de/estg/__37.html). Route the schedule to `de-estimated-tax`.
9. **Screen social insurance.** Test the pension duty list of [§ 2 SGB VI](https://www.gesetze-im-internet.de/sgb_6/__2.html) and, for artists and publicists, the [KSVG](https://www.gesetze-im-internet.de/ksvg/__1.html). Do not advise on contributions: refer to `de-social-contributions` and the pension or KSK authority.
10. **Route other income** (`de-capital-gains`, `de-crypto-tax`, `de-rental-income`), confirm the picture in one summary, list open points as flags, hand over, and diarise the deadlines in "Filing and payment".

### Documents to collect

- Business bank statements for the whole year.
- Sales invoices issued and purchase invoices or receipts.
- The last income tax assessment (Steuerbescheid) and any prepayment notice (Vorauszahlungsbescheid).
- VAT advance returns filed for the year, and any letter on the return period or a Dauerfristverlängerung.
- Last year's Anlage EÜR and the asset schedule (Anlage AVEÜR).
- Health and care insurance annual statement (Beitragsbescheinigung).
- For a new business: the trade registration, the tax office's letter with the tax number, and a copy of the registration questionnaire.
- Any notice from the pension insurance (Deutsche Rentenversicherung) or the Künstlersozialkasse.
- Any tax office letter, including a notice to keep books.
- Receipts for equipment, vehicles and other assets bought in the year.


### Freiberufler or Gewerbe (§ 18 vs § 15 EStG)

This is the first fork of every German intake.

- **The § 18 list.** Freelance work is self-employed scientific, artistic, literary, teaching or educational work ("wissenschaftliche, künstlerische, schriftstellerische, unterrichtende oder erzieherische Tätigkeit"), plus the self-employed work of the professions the statute names: Ärzte, Zahnärzte, Tierärzte, Rechtsanwälte, Notare, Patentanwälte, Vermessungsingenieure, Ingenieure, Architekten, Handelschemiker, Wirtschaftsprüfer, Steuerberater, beratende Volks- und Betriebswirte, vereidigte Buchprüfer, Steuerbevollmächtigte, Heilpraktiker, Dentisten, Krankengymnasten, Journalisten, Bildberichterstatter, Dolmetscher, Übersetzer, Lotsen "und ähnlicher Berufe" ([§ 18(1) no. 1 EStG](https://www.gesetze-im-internet.de/estg/__18.html)).
- **What is not on the list.** Software developers, IT consultants, web designers, marketing agencies and "consultants" in general are not named. Such a client is a Freiberufler only if the work is one of the five activity types or a profession similar to a named one. Do not tell the client either way: flag it.
- **The trade definition.** A self-employed, lasting activity with the aim of profit that takes part in general commerce is a Gewerbebetrieb unless it is farming, a liberal profession or other self-employed work ([§ 15(2) EStG](https://www.gesetze-im-internet.de/estg/__15.html)). The 2026 EÜR instructions say the same for line 8 of the form: freelance income exists only "wenn die Voraussetzungen des § 18" EStG are met ([BMF, Anlage EÜR 2026](https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Einkommensteuer/2026-09-01-anlage-EUER-2026.pdf?__blob=publicationFile&v=2)).
- **Staff.** A Freiberufler may use trained staff only while leading the work and taking personal responsibility for it on the strength of their own expertise ("leitend und eigenverantwortlich", § 18(1) no. 1 sentence 3 EStG). Flag any client with staff doing the core work.
- **Mixed activities.** Ask about every side line: sales of goods, commissions, brokerage, resold print or other bought-in work. Where the freelance and commercial parts can be separated, keep separate records and report them separately (Anlage S and Anlage G). Where they cannot, the classification of the whole is at risk. Flag it for the Steuerberater.
- **Who decides.** The tax office. A first treatment as Freiberufler can be reversed later, typically after an audit, with trade tax for past years. A binding ruling (verbindliche Auskunft) can settle a real doubt.

**What follows from the answer**

| | Freiberufler | Gewerbetreibender |
| --- | --- | --- |
| Start reported to | the tax office ([§ 138(1) AO](https://www.gesetze-im-internet.de/ao_1977/__138.html)) | the municipality, which informs the tax office |
| Trade tax | none | every Gewerbebetrieb run in Germany ([§ 2(1) GewStG](https://www.gesetze-im-internet.de/gewstg/__2.html)); allowance for sole traders |
| IHK membership | no, unless entered in the Handelsregister | yes, if assessed to trade tax and running a business establishment in the chamber's district ([§ 2 IHKG](https://www.gesetze-im-internet.de/ihkg/__2.html)) |
| Size-based bookkeeping duty ([§ 141 AO](https://www.gesetze-im-internet.de/ao_1977/__141.html)) | never | only after a tax office notice |
| Routed to | `de-einkommensteuer-freelancer` | `de-einkommensteuer-freelancer` and `de-trade-tax` |

- **IHK fees.** Members are those "sofern sie zur Gewerbesteuer veranlagt sind" (§ 2(1) IHKG). [§ 3(3) IHKG](https://www.gesetze-im-internet.de/ihkg/__3.html) frees unregistered sole traders from fees while their trade income or profit is not more than EUR 5,200.
- **Trade tax in detail.** The trade income of a sole trader is reduced by an allowance of EUR 24,500 per year ([§ 11(1) GewStG](https://www.gesetze-im-internet.de/gewstg/__11.html): "Freibetrag in Höhe von 24 500 Euro"). It is an allowance, not a cliff: only trade income above it is taxed. The trade income is rounded down to full EUR 100 before the allowance. The rate base (Steuermesszahl) is 3.5% ("beträgt 3,5 Prozent") and the municipality's multiplier (Hebesatz) decides the tax. Income tax is then reduced by up to four times the trade tax base amount ([§ 35 EStG](https://www.gesetze-im-internet.de/estg/__35.html): "das Vierfache"), within a ceiling set in § 35 and never above the trade tax actually payable ("auf die tatsächlich zu zahlende Gewerbesteuer beschränkt"). A trade tax return, filed electronically ([§ 14a GewStG](https://www.gesetze-im-internet.de/gewstg/__14a.html)), is due only if the year's trade income exceeded EUR 24,500 ([§ 25(1) no. 1 GewStDV](https://www.gesetze-im-internet.de/gewstdv_1955/__25.html): "den Betrag von 24 500 Euro überstiegen hat") or the tax office asks (§ 149(1) AO). Route every computation to `de-trade-tax`.

### Registration of a new business

- **Report the start within one month.** Opening a trade is reported to the municipality on the official form, and the municipality informs the tax office. Starting freelance work is reported to the tax office directly ([§ 138(1) AO](https://www.gesetze-im-internet.de/ao_1977/__138.html)). The same applies to moving or closing the business.
- **The registration questionnaire.** Anyone who must report a start must also give the tax office further details relevant to tax, "nach amtlich vorgeschriebenem Datensatz über die amtlich bestimmte Schnittstelle", so electronically; paper only on application for hardship (§ 138(1b) AO). In practice this is the Fragebogen zur steuerlichen Erfassung sent through ELSTER. The deadline is the same month: "innerhalb eines Monats nach dem meldepflichtigen Ereignis" (§ 138(4) AO).
- **What to check.** Was the questionnaire sent, and on time? What did the client choose there for VAT (Kleinunternehmer or not) and for expected turnover and profit? If it was never sent, the client should send it now; flag the delay.

### VAT status and return period

- **Kleinunternehmer (§ 19 UStG).** VAT is not charged if total turnover (Gesamtumsatz) did not exceed EUR 25,000 in the previous calendar year ("25 000 Euro nicht überschritten hat") and does not exceed EUR 100,000 in the current year ("100 000 Euro nicht überschreitet") ([§ 19(1) UStG](https://www.gesetze-im-internet.de/ustg_1980/__19.html)). Both tests must be met. A turnover exactly at a limit is still inside.
- **Start-up year.** For a business that starts during the year, the current-year limit is EUR 25,000 ([2026 EÜR instructions](https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Einkommensteuer/2026-09-01-anlage-EUER-2026.pdf?__blob=publicationFile&v=2), line 12: "darf der Gesamtumsatz im laufenden Kj. 25.000 € nicht überschreiten").
- **Crossing a limit in the year.** The sale that takes current-year turnover over the limit is already taxed: the EÜR instructions say the receipt "mit dem Sie die jeweilige Grenze im laufenden Kj. überschreiten, unterliegt der Regelbesteuerung". Earlier sales stay exempt. Route to `germany-vat-return` at once.
- **Waiver.** A Kleinunternehmer may opt into normal VAT by an irrevocable declaration up to the last day of February of the second year after the tax year; it binds for at least five calendar years (§ 19(3) UStG). Ask whether the client ever waived.
- **Invoices.** A Kleinunternehmer must not show VAT on an invoice. VAT shown without entitlement is owed anyway ([§ 14c UStG](https://www.gesetze-im-internet.de/ustg_1980/__14c.html)). An invoice without VAT does not by itself prove Kleinunternehmer status: check the turnover. Reading § 19(2) with § 1(1) no. 1 UStG, services supplied abroad are left out of the turnover test; confirm with `germany-vat-return`.
- **Returns for a Kleinunternehmer.** As a rule no advance returns and no annual VAT return, but the tax office can still ask for one, and a Kleinunternehmer who owes VAT as the recipient of a service from abroad (reverse charge) or on EU acquisitions must file for those periods (§ 19(1) sentence 2 with § 18(4a) UStG). Route to `germany-vat-return`.
- **Normal scheme: the return period** ([§ 18 UStG](https://www.gesetze-im-internet.de/ustg_1980/__18.html)). The default period is the calendar quarter. It is the month if the VAT for the previous calendar year was more than EUR 9,000 ("mehr als 9 000 Euro"). The tax office may release a business from advance returns if last year's VAT was not more than EUR 2,000; the annual return is still due. The test is last year's VAT, not turnover.
- **New businesses, tax periods 2021 to 2026.** A business started in the current year uses the expected VAT for that year for the test above; a business that ran only part of the previous year scales that year's VAT up to a full year (§ 18(2) UStG). This relief is written for 2021 to 2026 only; for 2027 check whether it has been extended, because the basic rule is monthly returns in the year of start and the year after.
- **Deadlines.** Advance returns and payment are due by the tenth day after the period ends ("bis zum 10. Tag nach Ablauf"). A Dauerfristverlängerung adds one month; a monthly filer pays a special prepayment of one eleventh of last year's prepayments ([§§ 46 and 47 UStDV](https://www.gesetze-im-internet.de/ustdv_1980/__47.html)).

### Profit method: EÜR for Freiberufler

- **EÜR.** Anyone not obliged by law to keep books, and not keeping them by choice, may work out profit as receipts less expenses ([§ 4(3) EStG](https://www.gesetze-im-internet.de/estg/__4.html): "nicht auf Grund gesetzlicher Vorschriften verpflichtet sind, Bücher zu führen"). A Freiberufler not entered as a merchant can use the EÜR at any size. The Anlage EÜR goes to the tax office electronically ([§ 60(4) EStDV](https://www.gesetze-im-internet.de/estdv_1955/__60.html)).
- **Gewerbetreibende: § 141 AO.** The tax-law duty to keep books can start for a commercial business with total turnover above EUR 800,000 in the calendar year, or trade profit above EUR 80,000 in the business year ([§ 141(1) AO](https://www.gesetze-im-internet.de/ao_1977/__141.html)). Either test is enough. The duty does not start by itself: it begins with the business year after the tax office's notice (§ 141(2) AO). Freiberufler are not named in § 141.
- **Merchants.** A merchant entered in the Handelsregister, or one who files a balance sheet for any reason, is outside this Guide: refer, and use `germany-bookkeeping` for the § 238 and § 241a HGB tests.

### Income tax prepayments

Prepayments are due on 10 March, 10 June, 10 September and 10 December ([§ 37(1) EStG](https://www.gesetze-im-internet.de/estg/__37.html)). They are set by notice, usually from the last assessment, and only if they come to at least EUR 400 a year and at least EUR 100 per due date (§ 37(5) EStG). A client with no notice has not missed a payment. The tax office may adjust them until the end of the fifteenth month after the tax year (§ 37(3) EStG). Route to `de-estimated-tax`.

### Social insurance: screen and refer

- **Pension duty for some self-employed people.** [§ 2 SGB VI](https://www.gesetze-im-internet.de/sgb_6/__2.html) makes these self-employed people compulsorily insured in the statutory pension scheme, among others: teachers and educators, and carers in sick, maternity, infant or child care, in each case if they regularly employ no insured employee; midwives; artists and publicists under the KSVG; craftspeople entered in the Handwerksrolle; and anyone who regularly employs no insured employee and works "auf Dauer und im Wesentlichen nur für einen Auftraggeber". A Minijob employee does not count as an employee for these tests. If a duty may apply and no pension contributions appear on the bank statement, flag it and refer to `de-social-contributions` and the Deutsche Rentenversicherung.
- **Artists and publicists: the Künstlersozialkasse.** Self-employed artists and publicists are insured in pension, health and care insurance through the KSK if they work in the field for a living and not just temporarily, and employ no more than one employee in that work, with trainees and Minijobs not counted ([§ 1 KSVG](https://www.gesetze-im-internet.de/ksvg/__1.html)). Ask whether the client is registered with the KSK; if not and the test may be met, refer.
- **Health insurance.** Ask whether the client is in statutory (GKV) or private (PKV) health insurance and collect the annual statement. How much of it counts as basic cover for the income tax deduction ([§ 10(1) no. 3 EStG](https://www.gesetze-im-internet.de/estg/__10.html)) is worked out in `de-einkommensteuer-freelancer`; take the figure from the insurer's statement, never estimate it.

## Figures for 2026

Limits that decide a route, for tax year 2026; unless a note says otherwise they were the same for 2025.

**Route-deciding limits**

| What | Value | Source and wording |
| --- | --- | --- |
| Kleinunternehmer: previous-year total turnover, not exceeded | EUR 25,000 | [§ 19(1) UStG](https://www.gesetze-im-internet.de/ustg_1980/__19.html): "25 000 Euro nicht überschritten hat" |
| Kleinunternehmer: current-year total turnover, not exceeded | EUR 100,000 | § 19(1) UStG: "100 000 Euro nicht überschreitet" |
| Kleinunternehmer in the start-up year: current-year limit | EUR 25,000 | EÜR instructions 2026, line 12 |
| Monthly VAT returns if last year's VAT was more than | EUR 9,000 | § 18(2) UStG: "mehr als 9 000 Euro" |
| Release from advance returns possible if last year's VAT was not more than | EUR 2,000 | § 18(2) UStG: "nicht mehr als 2 000 Euro" |
| Trade tax allowance, sole traders and partnerships, per year | EUR 24,500 | § 11(1) GewStG: "24 500 Euro" |
| Trade tax rate base (Steuermesszahl) | 3.5% | § 11(2) GewStG: "3,5 Prozent" |
| IHK fee exemption for unregistered sole traders, trade income or profit not more than | EUR 5,200 | § 3(3) IHKG: "5 200 Euro nicht übersteigt" |
| Bookkeeping duty possible (after notice), total turnover above | EUR 800,000 | § 141(1) no. 1 AO: "800 000 Euro im Kalenderjahr" |
| Bookkeeping duty possible (after notice), trade profit above | EUR 80,000 | § 141(1) no. 4 AO: "80 000 Euro im Wirtschaftsjahr" |
| Income tax prepayments set only if at least, per year | EUR 400 | § 37(5) EStG: "mindestens 400 Euro im Kalenderjahr" |
| and at least, per due date | EUR 100 | § 37(5) EStG: "mindestens 100 Euro" |

**Figures you will meet while sorting the documents** (the rules and the computation sit in `de-einkommensteuer-freelancer`)

| What | Value | Source and wording |
| --- | --- | --- |
| Low-value asset: may be expensed at once if the net cost is not more than | EUR 800 | [§ 6(2) EStG](https://www.gesetze-im-internet.de/estg/__6.html): "800 Euro nicht übersteigen" |
| Optional pool (Sammelposten), per asset: more than / not more than | EUR 250 / EUR 1,000 | § 6(2a) EStG: "250 Euro, aber nicht 1 000 Euro übersteigen" |
| Gifts to non-employees: deductible only if the total per recipient per year is not more than | EUR 50 | § 4(5) no. 1 EStG: "insgesamt 50 Euro nicht übersteigen" |
| Business entertainment: share deductible | 70% | § 4(5) no. 2 EStG: "70 Prozent der Aufwendungen" |
| Home office room that is the centre of all work: yearly flat amount | EUR 1,260 | § 4(5) no. 6b EStG: "1 260 Euro (Jahrespauschale)" |
| Home office day rate, no separate room needed | EUR 6 | § 4(5) no. 6c EStG: "6 Euro (Tagespauschale)" |
| Cap on the day rates per year | EUR 1,260 | § 4(5) no. 6c EStG: "höchstens 1 260 Euro" |
| Business car: list-price method only if business use is more than | 50% | § 6(1) no. 4 EStG: "mehr als 50 Prozent betrieblich genutzt" |
| List-price method: private use per month | 1% | § 6(1) no. 4 EStG: "1 Prozent des inländischen Listenpreises" |
| Commuting to own first premises, per km of one-way distance, from the first km | EUR 0.38 | § 9(1) sentence 3 no. 4 EStG: "0,38 Euro" |
| Commuting cap per year, where no own or provided car is used | EUR 4,500 | § 9(1) sentence 3 no. 4 EStG: "4 500 Euro im Kalenderjahr" |

- **2025 versus 2026 commuting.** From 1 January 2026 the EUR 0.38 rate applies from the first kilometre. For 2025 returns it applied only from the 21st kilometre ([BMF, what changes in 2026](https://www.bundesfinanzministerium.de/Content/DE/Standardartikel/Themen/Steuern/das-aendert-sich-2026.html)).
- **Computers and software.** The Finance Ministry accepts a useful life of one year ("Nutzungsdauer von einem Jahr") for computer hardware and software, so the cost can be deducted in the year of purchase; the item is still listed in Anlage AVEÜR (2026 EÜR instructions).
- **Church tax.** Read the rate from the client's last assessment, unless the client moved state or joined or left a church since then. It is set by the religious communities and differs by federal state; do not assume it.

## Boundaries and exceptions

| Situation | Treatment | Source |
| --- | --- | --- |
| 2025 turnover exactly EUR 25,000, 2026 turnover not over EUR 100,000 | Still a Kleinunternehmer: the limits must not be exceeded | [§ 19 UStG](https://www.gesetze-im-internet.de/ustg_1980/__19.html) |
| 2026 turnover crosses EUR 100,000 in October | The crossing sale and every later sale carry VAT; earlier sales stay exempt | 2026 EÜR instructions, line 12 |
| 2025 VAT exactly EUR 9,000 | Quarterly returns in 2026: monthly needs more than the limit | [§ 18(2) UStG](https://www.gesetze-im-internet.de/ustg_1980/__18.html) |
| Kleinunternehmer buys a service from a business abroad | Owes the VAT as recipient and files for that period | § 18(4a) UStG |
| Work not named in § 18, no trade registered | Record as stated, flag: the tax office decides and trade tax may follow for past years | [§ 18 EStG](https://www.gesetze-im-internet.de/estg/__18.html), [§ 15(2) EStG](https://www.gesetze-im-internet.de/estg/__15.html) |
| Trade income not more than EUR 24,500 | No trade tax after the allowance; no trade tax return unless the tax office asks | [§ 11 GewStG](https://www.gesetze-im-internet.de/gewstg/__11.html), [§ 25 GewStDV](https://www.gesetze-im-internet.de/gewstdv_1955/__25.html) |
| Gewerbe with profit above EUR 80,000 but no tax office notice | No § 141 AO duty yet; it starts with the business year after a notice | [§ 141(2) AO](https://www.gesetze-im-internet.de/ao_1977/__141.html) |
| Artist employs two people in the artistic work (not trainees or Minijobs) | Outside the KSK test | [§ 1 KSVG](https://www.gesetze-im-internet.de/ksvg/__1.html) |
| Self-employed with one main client and only a Minijob helper | Minijob does not count as an employee: the one-client pension test may be met | [§ 2 SGB VI](https://www.gesetze-im-internet.de/sgb_6/__2.html) |

## Worked cases

1. **The software developer** ([§ 11 GewStG](https://www.gesetze-im-internet.de/gewstg/__11.html)). Lena writes software for three agencies, has no trade registration and calls herself Freiberuflerin. Software development is not on the § 18 list, so record "Freiberufler, as stated; not named in § 18(1) no. 1 EStG" and flag it. Explain the stakes without deciding: if the tax office treats the work as a Gewerbe, trade tax and IHK membership follow. With trade income of EUR 30,000, the Gewerbe route would give EUR 30,000 less EUR 24,500 = EUR 5,500, times 3.5% = a trade tax base amount of EUR 192.50; the income tax credit could be up to four times that, EUR 770, but never more than the trade tax actually payable. Route to `de-trade-tax` and `de-einkommensteuer-freelancer`.
2. **The translator near the VAT limit** ([§ 19 UStG](https://www.gesetze-im-internet.de/ustg_1980/__19.html)). Tom, an Übersetzer (named in § 18), had total turnover of EUR 25,000 in 2025 and expects EUR 60,000 in 2026. He did not exceed EUR 25,000 in 2025 and will not exceed EUR 100,000 in 2026, so he remains a Kleinunternehmer in 2026, with no VAT on invoices. His 2026 turnover is above EUR 25,000, so for 2027 he moves to normal VAT from 1 January 2027. Route to `germany-vat-return` to plan the switch.
3. **The new coach.** Aylin starts freelance business coaching on 15 October 2026. She reports the start to the tax office and sends the questionnaire within one month; 15 November 2026 is a Sunday, so the deadline moves to Monday 16 November 2026 ([§ 108(3) AO](https://www.gesetze-im-internet.de/ao_1977/__108.html)). As a start-up she stays a Kleinunternehmer only while 2026 turnover does not exceed EUR 25,000. Coaching may fall under the teachers' pension duty in § 2 SGB VI if she employs no insured staff: flag and refer to `de-social-contributions`.
4. **The quarterly filer** ([§ 18 UStG](https://www.gesetze-im-internet.de/ustg_1980/__18.html)). Max, a Gewerbetreibender in the normal VAT scheme, paid EUR 9,000 of VAT for 2025. That is not more than EUR 9,000, so his 2026 periods are quarters. The third quarter return is due on 10 October 2026, a Saturday, so it moves to Monday 12 October 2026. With a Dauerfristverlängerung it would be due one month later. Route to `germany-vat-return`.
5. **The late 2025 return.** Sara prepares her own 2025 returns and has not filed. They were due on 31 July 2026. She should file now. If the 2025 income tax return is still not filed 14 months after the year end (end of February 2027), a late-filing surcharge must be set, unless an exception applies such as tax fixed at zero or not above the prepayments ([§ 152(2) and (3) AO](https://www.gesetze-im-internet.de/ao_1977/__152.html)).
## When to refuse or refer

Stop, say why, and name the adviser needed.

- **Part-year residents and non-residents.** Different rules on limited tax liability. Refer to a Steuerberater who handles non-resident returns.
- **Partnership as the business** (GbR, PartG, OHG, KG). It files a separate declaration of profit shares. A client who is a partner alongside their own sole business stays in scope with a flag: the share arrives in a separate determination notice.
- **GmbH, UG or other corporation.** Corporate tax and trade tax rules differ. Refer.
- **Balance-sheet filers**, including merchants in the Handelsregister and a Gewerbetreibender whose § 141 AO duty has already started. A notice received during the year being prepared takes effect only from the next business year, so that year stays in scope with a flag.
- **More than five employees.** This is this Guide's own scope line, not a legal threshold. Payroll at any size goes to `de-payroll`.
- **An unsettled classification that matters**: work not named in § 18, freelance and commercial work that cannot be separated, or staff doing work the client does not lead. Record, flag, and tell the client the tax office decides and that a Steuerberater or binding ruling can settle it.
- **VAT beyond the basics**: a Kleinunternehmer crossing a limit mid-year, reverse-charge purchases, goods sold across borders, distance sales and the one-stop shop. Route to `germany-vat-return`.
- **Social insurance.** Any possible pension duty, KSK membership or health insurance question: refer to `de-social-contributions` and to the Deutsche Rentenversicherung or the Künstlersozialkasse.
- **Business run in another tax office's district.** The business profit is then determined separately ([§ 180(1) no. 2 b AO](https://www.gesetze-im-internet.de/ao_1977/__180.html)). Flag it.
- **Electric or plug-in hybrid business cars, disputed car use, and whether a home office is the centre of all work** where the client also works elsewhere. Record and flag for `de-einkommensteuer-freelancer`.
- **Farming and forestry.** Refer.

## Filing and payment

**Returns for tax year 2026** (the income tax return duty is set out in [§ 56 EStDV](https://www.gesetze-im-internet.de/estdv_1955/__56.html); in practice a self-employed client with a profit files every year)

| Return | Who | Deadline |
| --- | --- | --- |
| Income tax return with Anlage EÜR and Anlage S or G | every client in scope | 31 July 2027, a Saturday, so Monday 2 August 2027; with a Steuerberater, 29 February 2028 |
| Annual VAT return | normal-scheme clients, and Kleinunternehmer only where § 18(4a) UStG applies or the office asks | same as above |
| Trade tax return | Gewerbetreibende with trade income over EUR 24,500, or if asked ([§ 25 GewStDV](https://www.gesetze-im-internet.de/gewstdv_1955/__25.html)) | same as above |
| VAT advance returns | normal scheme | tenth day after each month or quarter, plus one month with a Dauerfristverlängerung |
| Income tax prepayments | where a notice sets them | 10 March, 10 June, 10 September, 10 December |

- **The rule.** Annual returns are due seven months after the end of the calendar year ("sieben Monate nach Ablauf des Kalenderjahres", [§ 149(2) AO](https://www.gesetze-im-internet.de/ao_1977/__149.html)). Where a tax adviser prepares them, the deadline is the last day of February of the second following year (§ 149(3) AO), but the office can call a return in earlier (§ 149(4) AO). A deadline falling on a Saturday, Sunday or public holiday moves to the next working day ([§ 108(3) AO](https://www.gesetze-im-internet.de/ao_1977/__108.html)).
- **Returns for 2025, being filed now.** Self-prepared: due 31 July 2026, now past. With a Steuerberater: last day of February 2027; 28 February 2027 is a Sunday, so Monday 1 March 2027. The longer deadlines of the pandemic years ([Art. 97 § 36 EGAO](https://www.gesetze-im-internet.de/aoeg_1977/art_97__36.html)) covered tax periods 2020 to 2024 only; do not apply them to 2025.
- **Electronic filing.** The Anlage EÜR, the VAT returns and the trade tax return go electronically in the official format ([§ 60(4) EStDV](https://www.gesetze-im-internet.de/estdv_1955/__60.html), [§ 18 UStG](https://www.gesetze-im-internet.de/ustg_1980/__18.html), [§ 14a GewStG](https://www.gesetze-im-internet.de/gewstg/__14a.html)). Paper only on application for hardship.
- **Late filing.** A surcharge can be set for a late return. For a calendar-year return it is 0.25% of the assessed tax less prepayments and withheld tax for each started month of delay, at least EUR 25 for each started month, and at most EUR 25,000. It must be set if the return is more than 14 months late, subject to exceptions such as tax fixed at zero or not above the prepayments ([§ 152 AO](https://www.gesetze-im-internet.de/ao_1977/__152.html)).

## Completion checklist

- [ ] Tax year fixed; full-year residency confirmed.
- [ ] Out-of-scope structures screened out (partnership, corporation, balance sheet, more than five employees).
- [ ] Classification recorded as stated, tested against § 18 and § 15 EStG, and flagged where the work is not named or activities are mixed.
- [ ] Consequences noted: trade tax, IHK membership, Anlage S or G.
- [ ] For a new business: start reported and questionnaire sent within one month, or delay flagged.
- [ ] VAT status settled: both Kleinunternehmer limits tested (start-up limit where relevant), waiver asked, return period set from last year's VAT, Dauerfristverlängerung noted.
- [ ] Profit method confirmed: EÜR, and for a Gewerbe any § 141 AO notice.
- [ ] Prepayments read from the notice.
- [ ] Pension duty and KSK screened; referrals made where a duty may apply.
- [ ] Health insurance statement collected.
- [ ] Other income routed: `de-capital-gains`, `de-crypto-tax`, `de-rental-income`.
- [ ] Summary confirmed with the client; open flags listed.
- [ ] Handed to `de-einkommensteuer-freelancer`, `germany-vat-return`, `germany-bookkeeping` and, for a Gewerbe, `de-trade-tax`.
- [ ] 2025 and 2026 deadlines diarised; late 2025 returns flagged.
- [ ] Steuerberater review before filing.

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
