---
name: germany-formation
description: Use this skill whenever asked about forming, incorporating, or registering a company in Germany. Trigger on phrases like "set up a company in Germany", "GmbH formation", "UG gründen", "Handelsregister", "German company formation", "register a business Germany", "Gesellschaft mit beschränkter Haftung", "Unternehmergesellschaft", "German notary", "Gewerbeanmeldung", or any question about starting a business entity in Germany. Covers entity types (GmbH, UG, AG, GbR, KG), registration process, capital requirements, costs, post-formation compliance, and bank account opening. ALWAYS read this skill before advising on German company formation.
version: 1.1
jurisdiction: DE
tax_year: 2026
last_updated: 2026-10-31
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - company-formation-workflow-base
category: formation
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Forming a company in Germany (GmbH, UG, AG and partnerships)

How to set up a business entity in Germany: which legal form to pick, the steps from the articles to the commercial register, the capital that must be paid in, the official fees, the registrations that follow, and the duties that start once the company exists. It is for founders, inside and outside Germany, and for the advisers who help them. Most of the detail is on the GmbH and its small variant, the UG (haftungsbeschränkt). Figures are for tax year 2026. The statute figures were read from the consolidated federal law pages on 19 September 2026 and read again on 19 October 2026, with no change to any figure or rule used here. The statutes print the minimum capital amounts in words, so this skill gives them in words too. The small-business start-up limit comes from the finance ministry's instructions for the 2026 EÜR form (ministry letter of 1 September 2026).

## Germany Company Formation Skill

Read Section 2 to pick the legal form, Section 3 for the steps in order, Section 4 for capital, Section 5 for fees, and Section 6 for what is due after the company exists. Every amount and percentage sits in a table that names the official page it was read on. Where no official page prints a number, this skill says so and gives none.

## Section 1: Quick Reference

| Field | Value | Source |
| --- | --- | --- |
| Country | Germany (Federal Republic of Germany) | same |
| Currency | Euro | same |
| Company registrar | Handelsregister, kept by the local court (Amtsgericht) where the company has its seat. It has two divisions: A for sole merchants, OHG and KG, B for the AG, GmbH and other corporations (§ 3 HRV): https://www.gesetze-im-internet.de/hdlregvfg/__3.html The joint register portal of the federal states carries the commercial register and the other company registers: https://www.handelsregister.de/rp_web/welcome.xhtml |  |
| Key legislation | GmbH-Gesetz (GmbHG); Handelsgesetzbuch (HGB); Aktiengesetz (AktG). For partnerships also §§ 705 and following of the Civil Code (BGB) and the PartGG | https://www.gesetze-im-internet.de/gmbhg/__5.html |
| Typical formation time | Legacy estimate: 3 to 6 weeks from the notary to the register entry. No official page states a duration |  |
| Taxes on a GmbH, UG or AG | Corporate income tax, solidarity surcharge and trade tax. The three tables below give the parts. No official page prints one combined rate, so this skill does not state one | https://www.existenzgruendungsportal.de/_noch_neu_einordnen/DE/Gruendung-vorbereiten/Rechtsformen/Gesellschaft-mit-beschraenkter-Haftung-GmbH/inhalt.html |
| Tax authority | Local Finanzamt. Bundeszentralamt für Steuern (BZSt) for the VAT identification number and the business identification number | https://www.bzst.de/DE/Unternehmen/Identifikationsnummern/Wirtschafts-Identifikationsnummer/wirtschaftsidentifikationsnummer_node.html |

**Corporate income tax (Körperschaftsteuer)**

| What | Value | Note | Source |
| --- | --- | --- | --- |
| Source | all figures below | https://www.gesetze-im-internet.de/kstg_1977/__23.html |  |
| Corporate income tax on taxable income, for assessment periods up to and including 2027 | 15% | § 23(1) no. 1 KStG: "Veranlagungszeiträume bis 2027 15 Prozent". The same paragraph schedules lower rates from 2028 on. None of them applies to 2026 | https://www.gesetze-im-internet.de/kstg_1977/__23.html |

**Solidarity surcharge**

| What | Value | Note | Source |
| --- | --- | --- | --- |
| Source | all figures below | https://www.gesetze-im-internet.de/solzg_1995/__4.html |  |
| Solidarity surcharge, charged on the corporate income tax and not on the income | 5.5% | § 4 SolzG: "Der Solidaritätszuschlag beträgt 5,5 Prozent der Bemessungsgrundlage" | https://www.gesetze-im-internet.de/solzg_1995/__4.html |

**Trade tax (Gewerbesteuer)**

| What | Value | Note | Source |
| --- | --- | --- | --- |
| Source | all figures below | https://www.gesetze-im-internet.de/gewstg/__11.html |  |
| Base rate (Steuermesszahl) applied to trade income. It is not the tax rate: the result is multiplied by the multiplier (Hebesatz) that each municipality sets | 3.5% | § 11(2) GewStG: "Die Steuermesszahl für den Gewerbeertrag beträgt 3,5 Prozent" | https://www.gesetze-im-internet.de/gewstg/__11.html |
| Allowance taken off trade income first. Natural persons and partnerships only. A GmbH, UG or AG is not on the list and gets no allowance | EUR 24,500 | § 11(1) GewStG: "bei natürlichen Personen sowie bei Personengesellschaften um einen Freibetrag in Höhe von 24 500 Euro" | same |

The activity of a GmbH, UG or AG always counts as a trade, in full, whatever the company does. See § 2(2) GewStG at https://www.gesetze-im-internet.de/gewstg/__2.html The multiplier is set by the municipality under § 16 GewStG at https://www.gesetze-im-internet.de/gewstg/__16.html so the trade tax burden depends on where the company sits. `de-trade-tax` explains the calculation for sole traders and partnerships. It does not cover companies, so for a GmbH, UG or AG use the base rate above and the municipality's multiplier, with no allowance.

## Section 2: Entity Types Comparison

The capital rules in this table are explained, with their sources, in Section 4.

| Feature | Einzelunternehmen (sole trader) | GmbH | UG (haftungsbeschränkt) | GbR / OHG / KG (partnerships) | AG (stock corporation) |
| --- | --- | --- | --- | --- | --- |
| Legal status | The owner in person | Legal person (§ 13 GmbHG) | A GmbH with less than the GmbH minimum capital, not a separate form (§ 5a GmbHG) | Not called legal persons in the statutes. An OHG or KG can acquire rights and incur liabilities (§ 105(2), § 161(2) HGB). A GbR can too, if the partners mean it to take part in legal transactions (§ 705(2) BGB) | Company with its own legal personality (§ 1 AktG) |
| Liability | Unlimited, personal | Only the company's assets answer to its creditors (§ 13(2) GmbHG) | Same as GmbH | GbR and OHG: every partner, personally, jointly and severally (§ 721 BGB, § 126 HGB). KG: general partners without limit; a limited partner up to the registered liability amount, and not at all as far as the agreed contribution has been paid (§ 171 HGB) | Only the company's assets answer to its creditors (§ 1 AktG) |
| Min. founders | 1 | 1 (§ 1 GmbHG) | 1 | 2 | 1 (§ 2 AktG) |
| Min. share capital | None | twenty-five thousand euros (§ 5(1) GmbHG) | one euro, see Section 4 | None | fifty thousand euros (§ 7 AktG) |
| Min. paid in before the register application | Not applicable | Half of the minimum share capital in total, and one quarter of each cash share (§ 7(2) GmbHG) | All of it, in cash | Not applicable | One quarter of the lowest issue price of each share, plus any premium in full |
| Tax treatment | Income tax on the owner | Corporate income tax, solidarity surcharge, trade tax | Same as GmbH | Partners taxed individually. If the partnership runs a trade, the partnership itself owes the trade tax (§ 5 GewStG) | Same as GmbH |
| Notary | Only to certify a register application, when the owner is a merchant who must register (§ 12, § 29 HGB) | Yes. Articles are notarised (§ 2 GmbHG) and the register application is certified (§ 12 HGB) | Yes, same as GmbH | GbR: none needed to form. An application to the Gesellschaftsregister must be certified (§ 707b BGB, § 12 HGB). OHG and KG: the register application must be certified (§ 12, § 106, § 162 HGB) | Yes. Statutes are notarised (§ 23 AktG) |
| Commercial register | Only merchants (§ 1, § 29 HGB). A small trader may opt in (§ 2 HGB) | Yes, division B | Yes, division B | OHG and KG: yes, division A. GbR: no. It may choose an entry in the Gesellschaftsregister (§ 707 BGB) | Yes, division B |
| Bodies | Owner | Managing director(s) and shareholders' meeting. A supervisory board is compulsory only with more than 500 employees (§ 1 DrittelbG) | Same as GmbH | Partners | Management board, supervisory board of three members or more (§ 95 AktG), general meeting |
| Admin burden | Low | High | High | Low to medium | Very high |

Sources for the table: GmbHG §§ 1, 5a, 13 at https://www.gesetze-im-internet.de/gmbhg/__13.html ; HGB §§ 105, 126, 161, 171 at https://www.gesetze-im-internet.de/hgb/__105.html ; § 705 and § 721 BGB at https://www.gesetze-im-internet.de/bgb/__705.html ; AktG §§ 1, 2, 95 at https://www.gesetze-im-internet.de/aktg/__1.html ; the register divisions at https://www.gesetze-im-internet.de/hdlregvfg/__3.html ; the 500 employee rule at https://www.gesetze-im-internet.de/drittelbg/__1.html

**Recommended default:** GmbH for established businesses. UG for bootstrapped startups with a plan to move up to a GmbH. This default is legacy editorial advice, not an official statement. The start-up portal describes the UG as suited to founders of small commercial businesses, service providers above all, who want limited liability and can manage with little capital. It also tells founders to check the costs of the later step up to a GmbH and to ask whether a GmbH from the start makes more sense: https://www.existenzgruendungsportal.de/_noch_neu_einordnen/DE/Gruendung-vorbereiten/Rechtsformen/UG-haftungsbeschraenkt/inhalt

**Liberal professions.** An OHG or KG is defined by a commercial business (§ 105, § 161 HGB). A small trade, a partnership that only manages its own assets, or a partnership of liberal professionals can still become an OHG by choosing to be entered in the commercial register, the last only as far as the law of the profession allows the entry (§ 107(1) HGB): https://www.gesetze-im-internet.de/hgb/__107.html Otherwise members of the liberal professions who join forces use the GbR or the Partnerschaftsgesellschaft. Only natural persons can be partners in a Partnerschaft, and it does not carry on a commercial business (§ 1 PartGG): https://www.gesetze-im-internet.de/partgg/__1.html In the variant with limited professional liability (PartG mbB) only the partnership is liable for professional errors, if it keeps the professional liability insurance that a statute prescribes for that purpose (§ 8(4) PartGG): https://www.gesetze-im-internet.de/partgg/__8.html

## Section 3: Registration Process

Steps 1 to 4 are written for the GmbH and the UG. Steps 5 to 8 apply to every form that runs a trade. A short note on the other forms follows Step 8.

### Step 1: Draft Gesellschaftsvertrag (Articles of Association)

- **What the articles must contain.** Company name and seat, the object of the business, the amount of the share capital, and the number and nominal amounts of the shares each shareholder takes (§ 3(1) GmbHG): https://www.gesetze-im-internet.de/gmbhg/__3.html
- **Name and seat.** The name must contain "Gesellschaft mit beschränkter Haftung" or a generally understood abbreviation (§ 4 GmbHG). A company formed with less than the GmbH minimum capital must instead use "Unternehmergesellschaft (haftungsbeschränkt)" or "UG (haftungsbeschränkt)" (§ 5a(1) GmbHG). The seat is a place in Germany (§ 4a GmbHG): https://www.gesetze-im-internet.de/gmbhg/__4.html
- **Musterprotokoll usage.** A simplified formation is open to a company with at most three shareholders and one managing director. The model protocol in Annex 1 of the GmbHG must be used, and nothing that departs from the statute may be added. The protocol also counts as the shareholder list (§ 2(1a) GmbHG): https://www.gesetze-im-internet.de/gmbhg/__2.html The protocol only provides for contributions in cash.
- **Custom Satzung usage.** Custom articles for anything the model protocol cannot hold: more shareholders or managing directors, share classes, vesting, investor rights, contributions in kind.

**What the model protocol fixes (Annex 1 of the GmbHG)**

| What | Value | Note | Source |
| --- | --- | --- | --- |
| Source | all figures below | https://www.gesetze-im-internet.de/normengrafiken/bgbl1_2021/j3364_0010.pdf |  |
| Payment options the protocol offers for the cash contribution: all at once, or this share at once and the rest when the shareholders' meeting calls for it. A UG must strike the second option | 50% | Annex 1, clause 3: "sofort in voller Höhe/zu 50 Prozent sofort" | https://www.gesetze-im-internet.de/normengrafiken/bgbl1_2021/j3364_0010.pdf |
| Formation costs the company itself bears under the protocol, and never more than its share capital. Costs above that fall on the shareholders | EUR 300 | Annex 1, clause 5: "bis zu einem Gesamtbetrag von 300 €, höchstens jedoch bis zum Betrag ihres Stammkapitals" | same |

**Model protocols for a formation by video (Annex 2 of the GmbHG)**

| What | Value | Note | Source |
| --- | --- | --- | --- |
| Source | all figures below | https://www.gesetze-im-internet.de/gmbhg/anlage_2.html |  |
| Formation costs the company itself bears under the video protocols, and never more than its share capital | EUR 600 | Annex 2, clause 5: "bis zu einem Gesamtbetrag von 600 €, höchstens jedoch bis zum Betrag ihres Stammkapitals" | https://www.gesetze-im-internet.de/gmbhg/anlage_2.html |

### Step 2: Notary Appointment (Beurkundung)

- **Notarisation requirement.** The articles need notarial form and every shareholder signs them (§ 2(1) GmbHG): https://www.gesetze-im-internet.de/gmbhg/__2.html
- **Signing through a representative.** Allowed only with a power of attorney that a notary drew up or certified (§ 2(2) GmbHG).
- **Video notarisation.** The articles can be notarised by video under §§ 16a to 16e of the Beurkundungsgesetz, unless another form rule stands in the way (§ 2(3) GmbHG). It runs on the video system that the Federal Chamber of Notaries operates (§ 16a(1) BeurkG): https://www.gesetze-im-internet.de/beurkg/__16a.html The start-up portal dates the online formation from 1 August 2022 and says that before 1 August 2023 only cash formations could be done online. It says the online route can be used from abroad and can be mixed, for example one shareholder at the notary's office and the others online: https://www.existenzgruendungsportal.de/_noch_neu_einordnen/DE/Gruendung-vorbereiten/Rechtsformen/Gesellschaft-mit-beschraenkter-Haftung-GmbH/inhalt.html
- **Who can be identified by video.** The notary checks a photo read electronically from the chip of a German identity card, passport or electronic residence permit, or of an official identity card or passport of another state that meets the German passport and identity card duty. No photo is needed if the notary already knows the person. On top of the photo the notary checks an electronic identity: a German one (identity card, eID card or electronic residence permit), or one issued by another EU or EEA state that is recognised for cross-border use and notified at assurance level "high" (§ 16c BeurkG): https://www.gesetze-im-internet.de/beurkg/__16c.html A founder without such an electronic identity cannot normally use the video route. The notary should refuse video if identity or legal capacity cannot be made certain (§ 16a BeurkG).
- **Who can be managing director.** Only a natural person with full legal capacity. Excluded are, among others, persons whom a court or an authority has banned from a trade or profession that matches the company's object in whole or in part, while the ban is in force, and persons convicted of the listed intentional insolvency and false-statement offences, or sentenced to prison for one year or more for the listed fraud, subsidy, credit and embezzlement offences (§§ 263 to 264a, 265b to 266a StGB), in each case for five years from the final judgment. A comparable ban in another EU or EEA state counts too. So does a conviction abroad for a comparable offence (§ 6(2) GmbHG): https://www.gesetze-im-internet.de/gmbhg/__6.html Each managing director assures the court of this in the application (§ 8(3) GmbHG).
- **Notary prepares Handelsregister application.** The application to the register is filed electronically in publicly certified form, and the certification may also be done by video (§ 12(1) HGB): https://www.gesetze-im-internet.de/hgb/__12.html The notary sends it to the register with the documents.

### Step 3: Open Bank Account and Deposit Capital

- **Geschäftskonto naming.** Legacy practice note: open the business account in the name of the company with the addition "i.G." (in Gründung). No official page read for this skill describes the account opening. Treat it as practice, not law.
- **GmbH deposit requirement.** Before the register application, one quarter of each cash share must be paid in, and the total paid in (cash plus the nominal amount of shares to be covered in kind) must reach the amount in the Section 4 table (§ 7(2) GmbHG): https://www.gesetze-im-internet.de/gmbhg/__7.html
- **UG deposit requirement.** The whole share capital must be paid in, in cash, before the application. Contributions in kind are excluded (§ 5a(2) GmbHG): https://www.gesetze-im-internet.de/gmbhg/__5a.html
- **Free disposal.** What is paid in must be at the final free disposal of the managing directors, and they assure this in the application (§ 7(3), § 8(2) GmbHG).
- **Bank confirmation.** Legacy practice note: obtain a bank confirmation for the notary. The statute does not ask for one as a rule. The court may demand proof, such as payment slips from a bank or payment service provider established in the EU, only when it has serious doubts about the assurance (§ 8(2) GmbHG): https://www.gesetze-im-internet.de/gmbhg/__8.html
- **Cash that flows back.** If a cash contribution is, in economic terms and by an arrangement made with it, really a contribution in kind (for example where the company is to buy an asset from the founder with that money), the founder stays liable for the cash contribution, less the value of the asset, and the founder bears the burden of proving that value (§ 19(4) GmbHG): https://www.gesetze-im-internet.de/gmbhg/__19.html A UG cannot take contributions in kind at all, so refer such cases.

### Step 4: Handelsregister Filing

- **Where and how.** The company is filed for entry with the court of its seat (§ 7(1) GmbHG). Applications are filed electronically in publicly certified form (§ 12 HGB): https://www.gesetze-im-internet.de/hgb/__12.html
- **Electronic submission.** The notary submits electronically to the Amtsgericht.
- **Attachments.** The articles (or the model protocol), proof of the managing directors' appointment if they are not named in the articles, the signed shareholder list, and for contributions in kind the contracts, the report on the formation in kind and proof of value (§ 8(1) GmbHG): https://www.gesetze-im-internet.de/gmbhg/__8.html
- **Address and powers.** The application states a business address in Germany and how the managing directors represent the company (§ 8(4) GmbHG).
- **Registration fee.** See the court fee table below.
- **Legal existence date.** Before the entry in the register the GmbH or UG does not exist as such (§ 11(1) GmbHG): https://www.gesetze-im-internet.de/gmbhg/__11.html
- **Beware of fake invoices.** Soon after the entry is published in the register portal, founders often get letters that look like a bill for entry in a state register. The start-up portal reports that the federal justice ministry warns against these "offers": https://www.existenzgruendungsportal.de/_noch_neu_einordnen/DE/Gruendung-vorbereiten/Gruendungswissen/Behoerden/Handelsregister/inhalt Check every bill against the court's own fee notice before paying.

**Court fees for the first entry in the commercial register (Handelsregistergebührenverordnung, fee schedule)**

| What | Value | Note | Source |
| --- | --- | --- | --- |
| Source | all figures below | https://www.gesetze-im-internet.de/hreggebv/anlage.html |  |
| First entry of a GmbH, UG included, cash formation (no. 2100) | EUR 225 | "Eintragung einer Gesellschaft mit beschränkter Haftung einschließlich einer Unternehmergesellschaft" | https://www.gesetze-im-internet.de/hreggebv/anlage.html |
| Same, when one contribution in kind or more is made (no. 2101) | EUR 360 | "Es wird mindestens eine Sacheinlage geleistet: Die Gebühr 2100 beträgt" | same |
| First entry of an AG (no. 2102) | EUR 450 | "Eintragung einer Aktiengesellschaft, einer Kommanditgesellschaft auf Aktien" | same |
| Same, when one contribution in kind or more is made (no. 2103) | EUR 540 | "Es wird mindestens eine Sacheinlage geleistet: Die Gebühr 2102 beträgt" | same |
| First entry of a sole merchant (no. 1100) | EUR 105 | "eines Einzelkaufmanns" | same |
| First entry of a partnership with up to 3 partners to be entered (no. 1101) | EUR 150 | "einer Gesellschaft mit bis zu 3 einzutragenden Gesellschaftern" | same |
| Added to no. 1101 for each further partner to be entered (no. 1102) | EUR 60 | "erhöht sich für jeden weiteren einzutragenden Gesellschafter" | same |

On top of each entry fee the court charges a separate fee for making the data available for retrieval (no. 6000). The schedule prints it as one third of the entry fee ("1/3 der für die Eintragung oder Entgegennahme bestimmten Gebühr"). This skill does not add the two together. The notary's fee is separate: see Section 5.

### Step 5: Gewerbeanmeldung (Trade Registration)

- **Registration requirement.** Whoever starts a standing trade must notify the competent authority at the same time (§ 14(1) GewO): https://www.gesetze-im-internet.de/gewo/__14.html Moving the business, changing its object and closing it must be notified too.
- **Who is outside the trade rules.** The Trade Regulation Act does not apply at all to, among others, fishing, lawyers, notaries, auditors, tax advisers and the teaching sector (§ 6(1) GewO): https://www.gesetze-im-internet.de/gewo/__6.html A partnership of liberal professionals that runs no trade makes no trade notification; it tells the tax office instead (§ 138(1) AO). The start-up portal puts it generally: the liberal professions and primary production (farming, forestry, fishing and hunting) make no trade notification: https://www.existenzgruendungsportal.de/Navigation/DE/So-gehts/Unternehmensanmeldung/unternehmensanmeldung
- **Fee.** The municipality sets it. No federal statute sets the fee. The table below gives the range the Federal Government's start-up portal prints. Ask the trade office for its own amount.
- **What to bring.** Identity card or passport; a permit if the trade needs one; the craft card for a craft; a register extract if the business is in the commercial register; for non-German nationals a residence permit that allows self-employed trading. A certificate of good conduct or an extract from the central trade register may also be asked for: https://www.existenzgruendungsportal.de/Navigation/DE/Gruendungswissen/Behoerden/behoerden
- **Processing.** The trade office passes data from the notification on to other bodies, among them the IHK and the Handwerkskammer (§ 14(8) GewO). The municipality informs the tax office without delay (§ 138(1) AO): https://www.gesetze-im-internet.de/ao_1977/__138.html The start-up portal says a trade notification is normally processed within a few days, and that the trade office informs the accident insurer, the IHK or Handwerkskammer, the register court and the trade supervisory office. It advises founders to check that each of them was in fact informed: https://www.existenzgruendungsportal.de/Navigation/DE/Gruendungswissen/Behoerden/behoerden
- **Penalty.** Not notifying, or notifying late, is an administrative offence (§ 146(2) no. 2 GewO). The statute prints the ceiling in words: a fine of up to one thousand euros ("bis zu eintausend Euro"): https://www.gesetze-im-internet.de/gewo/__146.html

**Fee for the trade notification**

| What | Value | Note | Source |
| --- | --- | --- | --- |
| Source | all figures below | https://www.existenzgruendungsportal.de/Navigation/DE/So-gehts/Unternehmensanmeldung/unternehmensanmeldung |  |
| Lower end of the range the Federal Government's portal gives for the trade notification | EUR 20 | "Die Kosten für der Gewerbeanzeige variieren zwischen 20 und 60 EUR" | https://www.existenzgruendungsportal.de/Navigation/DE/So-gehts/Unternehmensanmeldung/unternehmensanmeldung |
| Upper end of that range | EUR 60 | Same sentence. No federal statute sets the fee. Ask the municipality for its own amount | same |

### Step 6: Tax Registration (Steuerliche Erfassung)

- **Notify within one month.** A taxpayer that is not a natural person must report its formation to the tax office and to the municipality within one month of the event (§ 137 AO): https://www.gesetze-im-internet.de/ao_1977/__137.html The statute names the formation and the acquisition of legal capacity as separate events to report ('die Gründung, den Erwerb der Rechtsfähigkeit'). Do not wait for the register entry before the first notice.
- **Fragebogen.** Further details go to the tax office in the questionnaire for tax registration, sent electronically within one month (§ 138(1b) and (4) AO): https://www.gesetze-im-internet.de/ao_1977/__138.html In Mein ELSTER the form is called "Fragebogen zur steuerlichen Erfassung: Gründung einer Kapitalgesellschaft beziehungsweise Genossenschaft". Its condition is the formation of a corporation with its seat in Germany, for example a GmbH, UG or AG: https://www.elster.de/eportal/formulare-leistungen/alleformulare/fsekapg Practice note: sole traders and partnerships use other versions of the questionnaire.
- **Copy for the tax office.** Under the model protocol the tax office's corporate tax unit receives a plain copy of the deed (clause 6 of the protocol). That copy does not replace the questionnaire.
- **Steuernummer.** After it has processed the questionnaire the tax office tells the business its tax number, which the start-up portal says is needed to issue invoices: https://www.existenzgruendungsportal.de/Navigation/DE/Gruendungswissen/Behoerden/behoerden An invoice must carry the tax number or the VAT identification number (§ 14(4) no. 2 UStG): https://www.gesetze-im-internet.de/ustg_1980/__14.html An invoice for a small amount needs neither, under the lighter rules of § 33 UStDV, which do not apply to supplies under §§ 3c, 6a and 13b UStG: https://www.gesetze-im-internet.de/ustdv_1980/__33.html
- **Business identification number (W-IdNr).** It is assigned at the request of the competent tax authority, not on the business's application, and it starts with the letters DE (§ 139c(1) AO): https://www.gesetze-im-internet.de/ao_1977/__139c.html The BZSt has been assigning it in stages, without application, since November 2024, by public notice or through the ELSTER user account. The tax number and the VAT identification number stay in use next to it, and giving the W-IdNr in tax forms is optional until the first assignment is complete (page dated 10 September 2026): https://www.bzst.de/DE/Unternehmen/Identifikationsnummern/Wirtschafts-Identifikationsnummer/wirtschaftsidentifikationsnummer_node.html
- **USt-IdNr.** The BZSt issues the VAT identification number to a business on application. The application is made in writing and names the tax number under which the business is registered for VAT, so it can only follow the tax registration (§ 27a(1) UStG): https://www.gesetze-im-internet.de/ustg_1980/__27a.html A newly formed business asks for it by ticking the box in the questionnaire. The tax office forwards the request to the BZSt automatically, which can take some weeks. The number can only be issued once the business is registered for VAT and its data has reached the BZSt, and it is sent by post only: https://www.bzst.de/DE/Unternehmen/Identifikationsnummern/Umsatzsteuer-Identifikationsnummer/Vergabe_USt_IdNr/vergabe_ust_idnr_node.html
- **Small-business choice.** The questionnaire asks whether the business uses the small-business VAT rule. The limits are in the first two tables below. § 19 UStG speaks of every business established in Germany (Unternehmer), so a company can use the rule too. A business that uses the rule files no advance VAT returns and no annual VAT return: § 19(1) sentence 2 UStG switches off the filing duties of § 18(1) to (4) ("über die Erklärungspflichten (§ 18 Absatz 1 bis 4) keine Anwendung"); the cases of § 18(4a) UStG stay. A business that waives the rule is bound by the waiver for at least five calendar years ("Der Verzicht bindet den Unternehmer mindestens für fünf Kalenderjahre", § 19(3) UStG). The tables below are for a business that does not use the rule.

**Small-business VAT rule (Kleinunternehmer): the two yearly limits**

| What | Value | Note | Source |
| --- | --- | --- | --- |
| Source | all figures below | https://www.gesetze-im-internet.de/ustg_1980/__19.html |  |
| Total turnover of the previous calendar year must not have gone above this. Condition 1 of 2, joined by AND | EUR 25,000 | § 19(1) UStG: "im vorangegangenen Kalenderjahr 25 000 Euro nicht überschritten hat" | https://www.gesetze-im-internet.de/ustg_1980/__19.html |
| Total turnover of the current calendar year must not go above this. Condition 2 of 2. A hard limit during the year, not a forecast | EUR 100,000 | § 19(1) UStG: "im laufenden Kalenderjahr 100 000 Euro nicht überschreitet" | same |

**Small-business VAT rule in the year the business starts**

| What | Value | Note | Source |
| --- | --- | --- | --- |
| Source | all figures below | https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Einkommensteuer/2026-09-01-anlage-EUER-2026.pdf?__blob=publicationFile&v=2 |  |
| A business that starts during the year: total turnover of that calendar year must not go above this. The receipt that crosses the limit is already taxed under the normal rules. Earlier receipts stay exempt | EUR 25,000 | Ministry's instructions for the 2026 EÜR form: "darf der Gesamtumsatz im laufenden Kj. 25.000 € nicht überschreiten". A GmbH does not file that form. The start-up sentence is the ministry's reading of § 19 UStG and is not printed in the statute. § 19 UStG covers every business established in Germany | https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Einkommensteuer/2026-09-01-anlage-EUER-2026.pdf?__blob=publicationFile&v=2 |

**VAT advance returns: how often**

| What | Value | Note | Source |
| --- | --- | --- | --- |
| Source | all figures below | https://www.gesetze-im-internet.de/ustg_1980/__18.html |  |
| Quarterly is the default. Monthly if the VAT payable for the previous calendar year was more than this | EUR 9,000 | § 18(2) UStG: "für das vorangegangene Kalenderjahr mehr als 9 000 Euro" | https://www.gesetze-im-internet.de/ustg_1980/__18.html |
| The tax office may release the business from advance returns if the VAT for the previous calendar year was not more than this | EUR 2,000 | § 18(2) UStG: "für das vorangegangene Kalenderjahr nicht mehr als 2 000 Euro" | same |

For tax periods 2021 to 2026 a new business is not automatically a monthly filer: in the start-up year the expected VAT of the current year is measured against the limits above, and for a business that was active for only part of the previous year the actual VAT is scaled up to a full year (§ 18(2) sentence 6 UStG). Shelf companies and dormant shells that are taken over are monthly filers in the current and the following calendar year (§ 18(2) sentence 5 UStG). The statute limits the relief for new businesses to tax periods up to 2026. Read § 18(2) UStG again for 2027: without the relief, a new business files monthly in its first and second calendar year (§ 18(2) sentence 4 UStG).

### Step 7: Transparenzregister (Beneficial Ownership Register)

- **Registration requirement.** Legal persons under private law and registered partnerships must obtain the details of their beneficial owners, keep them up to date and report them to the register without undue delay, electronically (§ 20(1) GwG): https://www.gesetze-im-internet.de/gwg_2017/__20.html The details are first name and surname, date of birth, place of residence, nature and extent of the interest, and all nationalities (§ 19(1) GwG).
- **Who is a beneficial owner.** See the table below. If no natural person passes the test after a thorough check, the legal representative, managing partner or partner counts as beneficial owner (§ 3(2) GwG).
- **Mandatory since 2021.** Until 31 July 2021 the duty could count as met without a report, under the old § 20(2) GwG (the legacy text of this skill says: through the commercial register entry). That rule is gone. Existing GmbHs that had relied on it had to report by 30 June 2022 (§ 59(8) GwG): https://www.gesetze-im-internet.de/gwg_2017/__59.html A newly formed company reports itself.
- **No fixed number of days.** The statute says "unverzüglich" (without undue delay) for the first report and for changes. It sets no period in days.

**Beneficial owner test**

| What | Value | Note | Source |
| --- | --- | --- | --- |
| Source | all figures below | https://www.gesetze-im-internet.de/gwg_2017/__3.html |  |
| A natural person who, directly or indirectly, holds more than this share of the capital, or controls more than this share of the voting rights, or exercises control in a comparable way | 25% | § 3(2) GwG: "mehr als 25 Prozent der Kapitalanteile hält" | https://www.gesetze-im-internet.de/gwg_2017/__3.html |

### Step 8: Further Registrations

- **IHK membership.** Membership follows from the law, not from an application: whoever is assessed to trade tax and has a permanent establishment in the chamber's district belongs to it (§ 2(1) IHKG): https://www.gesetze-im-internet.de/ihkg/__2.html The trade office sends the chamber the data from the trade notification (§ 14(8) GewO). Crafts businesses register with the Handwerkskammer, and belong to the IHK only with any part of the business that is not a craft (§ 2(3) IHKG).
- **IHK contributions.** Each chamber sets a basic contribution and a levy in its own rules (§ 3 IHKG). No federal page prints an amount. A GmbH or UG is in the commercial register, so the exemption in the table below does not apply to it.
- **Berufsgenossenschaft.** Every entrepreneur must tell the competent accident insurer, within one week of the start of the enterprise, its kind and object, the number of insured persons and the opening day. The duty counts as met if the trade notification under § 14 GewO was made within one week of the start (§ 192(1) SGB VII): https://www.gesetze-im-internet.de/sgb_7/__192.html The start-up portal still advises telling the insurer directly within a week, to be safe, although trade offices usually pass the notification on. Contributions fall due when the entrepreneur is insured there or has employees, and the business alone bears them: https://www.existenzgruendungsportal.de/Navigation/DE/Gruendungswissen/Behoerden/behoerden
- **Employer number.** An employer that reports employees, mini-jobbers or apprentices to social insurance needs a Betriebsnummer for each establishment, issued by the Federal Employment Agency's Betriebsnummern-Service (§§ 18i to 18n SGB IV): https://www.arbeitsagentur.de/unternehmen/betriebsnummern-service/alles-wichtige See `de-payroll`.

**IHK contribution exemption for small unregistered businesses**

| What | Value | Note | Source |
| --- | --- | --- | --- |
| Source | all figures below | https://www.gesetze-im-internet.de/ihkg/__3.html |  |
| Natural persons and partnerships that are NOT in the commercial register pay no contribution while their trade income, or their profit from the trade, does not go above this. Not for a GmbH, UG, AG, OHG or KG | EUR 5,200 | § 3(3) IHKG: "ihr nach dem Einkommensteuergesetz ermittelter Gewinn aus Gewerbebetrieb 5 200 Euro nicht übersteigt". The same paragraph holds a further relief for first-time founders who are natural persons. Read its conditions on the page | https://www.gesetze-im-internet.de/ihkg/__3.html |

**Other legal forms in short.**

- **AG.** The statutes are notarised (§ 23 AktG). The founders appoint the first supervisory board and the first auditor, by notarial deed, and the supervisory board appoints the first management board (§ 30 AktG). The boards examine the formation. A separate audit by formation auditors is also needed in the four cases of § 33(2) AktG, among them a board member who is a founder, and contributions in kind. In the first two cases (a board member is a founder, or shares were taken for a board member's account) the notary who notarised the statutes may do that audit on the founders' instruction, in place of a formation auditor. If the notary does not, the court appoints the auditors (§ 33(3) AktG). For contributions in kind § 33a AktG allows the audit to be dropped in narrow cases: https://www.gesetze-im-internet.de/aktg/__33a.html All founders and all board members file the application (§ 36 AktG): https://www.gesetze-im-internet.de/aktg/__36.html Before the entry the AG does not exist as such, and whoever acts in its name is personally liable (§ 41 AktG).
- **OHG and KG.** All partners file the application (§ 106, § 162 HGB). Towards third parties the partnership exists once it is entered, or earlier if it takes part in legal transactions with every partner's consent. The earlier start applies only as far as § 107(1) HGB does not say otherwise (§ 123(1) HGB): https://www.gesetze-im-internet.de/hgb/__123.html A small trade, a partnership that only manages its own assets, or a partnership of liberal professionals is an OHG or KG only once it is entered. If it takes part in legal transactions before that, with every partner's consent, it exists towards third parties as a GbR and the partners are personally liable (§ 719(1), § 721 BGB): https://www.gesetze-im-internet.de/bgb/__719.html In a partnership whose purpose is a commercial business, a limited partner who agreed to trading before the entry is liable like a general partner for debts created up to the entry, unless the creditor knew of the limited status (§ 176(1) HGB): https://www.gesetze-im-internet.de/hgb/__176.html
- **GbR.** It is set up by the partnership contract (§ 705 BGB). Entry in the Gesellschaftsregister is a choice (§ 707 BGB): https://www.gesetze-im-internet.de/bgb/__707.html The application follows the commercial register rules, so it is filed electronically in publicly certified form, through a notary (§ 707b no. 2 BGB with § 12 HGB): https://www.gesetze-im-internet.de/bgb/__707b.html One trap: a GbR can be entered in a GmbH's shareholder list only if it is itself in the Gesellschaftsregister (§ 40(1) GmbHG). A GbR that is to be a founder of a GmbH must register first.
- **Partnerschaftsgesellschaft.** It is filed for entry in the Partnerschaftsregister, and each partner's liberal profession is stated (§ 4 PartGG): https://www.gesetze-im-internet.de/partgg/__4.html

## Section 4: Capital Requirements

**GmbH: minimum capital and what must be paid in first**

| What | Value | Note | Source |
| --- | --- | --- | --- |
| Source | all figures below | https://www.gesetze-im-internet.de/gmbhg/__5.html |  |
| Minimum share capital (Stammkapital) of a GmbH, printed in words | twenty-five thousand euros | § 5(1) GmbHG: "Das Stammkapital der Gesellschaft muß mindestens fünfundzwanzigtausend Euro betragen" | https://www.gesetze-im-internet.de/gmbhg/__5.html |

| What | Value | Note | Source |
| --- | --- | --- | --- |
| Source | all figures below | https://www.gesetze-im-internet.de/gmbhg/__7.html |  |
| Amount that must be reached before the register application: cash paid in, plus the nominal amount of shares to be covered in kind. The rest stays owed by the shareholders | half of the minimum share capital | § 7(2) GmbHG: "die Hälfte des Mindeststammkapitals gemäß § 5 Abs. 1 erreicht" | https://www.gesetze-im-internet.de/gmbhg/__7.html |

A second test applies together with the total, not instead of it: on each cash share one quarter of the nominal amount must be paid in before the application. The statute prints it in words ("ein Viertel des Nennbetrags eingezahlt ist", § 7(2) GmbHG): https://www.gesetze-im-internet.de/gmbhg/__7.html Contributions in kind must be made in full before the application (§ 7(3) GmbHG). Each share must be a full euro amount, and the shares must add up to the share capital (§ 5 GmbHG): https://www.gesetze-im-internet.de/gmbhg/__5.html

**UG (haftungsbeschränkt): minimum capital and the reserve**

| What | Value | Note | Source |
| --- | --- | --- | --- |
| Source | all figures below | https://www.gesetze-im-internet.de/gmbhg/__5a.html |  |
| Minimum share capital of a UG. The statute sets no amount: a UG is a company formed with less than the GmbH minimum (§ 5a(1)), and each share must be a full euro amount (§ 5(2) GmbHG). This skill reads that as a lowest possible capital of one euro | one euro | § 5a(1) GmbHG: "mit einem Stammkapital gegründet wird, das den Betrag des Mindeststammkapitals nach § 5 Abs. 1 unterschreitet". The start-up portal prints it: "Das Stammkapital beträgt mindestens einen Euro" (https://www.existenzgruendungsportal.de/_noch_neu_einordnen/DE/Gruendung-vorbereiten/Rechtsformen/UG-haftungsbeschraenkt/inhalt) |  |
| Share of each year's annual net profit, reduced by a loss carried forward from the year before, that must go into a statutory reserve, printed in words | one quarter | § 5a(3) GmbHG: "ein Viertel des um einen Verlustvortrag aus dem Vorjahr geminderten Jahresüberschusses" | https://www.gesetze-im-internet.de/gmbhg/__5a.html |
| Registered share capital at which the UG rules stop applying, once the company raises its capital to it or above | the GmbH minimum | § 5a(5) GmbHG: "den Betrag des Mindeststammkapitals nach § 5 Abs. 1 erreicht oder übersteigt" | same |

- **UG profit retention rule.** The reserve duty has no time limit. It does not end when the reserve reaches a certain size. It ends only when the company raises its registered share capital to the GmbH minimum or above. From then on the special UG rules no longer apply, and the company may keep the UG name or change to GmbH (§ 5a(5) GmbHG): https://www.gesetze-im-internet.de/gmbhg/__5a.html
- **What the reserve may be used for.** Only a capital increase from company funds, or to cover an annual loss or a loss carried forward that profits do not cover (§ 5a(3) GmbHG). A capital increase from company funds rests on a balance sheet, and the last annual balance sheet can serve only if it was audited (§ 57c, § 57e GmbHG): https://www.gesetze-im-internet.de/gmbhg/__57e.html The start-up portal puts it this way: before the step up to a GmbH the UG's balance sheet must be examined by an auditor: https://www.existenzgruendungsportal.de/_noch_neu_einordnen/DE/Gruendung-vorbereiten/Rechtsformen/UG-haftungsbeschraenkt/inhalt § 5a(5) GmbHG itself does not say by which kind of capital increase the minimum must be reached.
- **No profit, no reserve.** The reserve is a share of the annual net profit, so a UG with no annual net profit puts nothing in it (§ 5a(3) GmbHG). The start-up portal warns that the duty must not be dodged through hidden profit distributions, for example excessive pay for the managing director: https://www.existenzgruendungsportal.de/_noch_neu_einordnen/DE/Gruendung-vorbereiten/Rechtsformen/UG-haftungsbeschraenkt/inhalt
- **Meeting on looming insolvency.** In a UG the shareholders' meeting must be called without delay when the company is threatened with inability to pay (§ 5a(4) GmbHG).

**AG: minimum capital**

| What | Value | Note | Source |
| --- | --- | --- | --- |
| Source | all figures below | https://www.gesetze-im-internet.de/aktg/__7.html |  |
| Minimum share capital (Grundkapital) of an AG, printed in words | fifty thousand euros | § 7 AktG: "Der Mindestnennbetrag des Grundkapitals ist fünfzigtausend Euro" | https://www.gesetze-im-internet.de/aktg/__7.html |

For cash contributions to an AG the amount called in before the application must be one quarter of the lowest issue price of each share or more, plus the whole premium if shares are issued above that price. The statute prints it in words ("mindestens ein Viertel des geringsten Ausgabebetrags", § 36a(1) AktG): https://www.gesetze-im-internet.de/aktg/__36a.html Contributions in kind must be made in full. Where the contribution is a duty to transfer an asset, the transfer must be carried out within five years of the entry (§ 36a(2) AktG). No official page prints that quarter as a euro amount, so this skill gives none.

**Capital Requirements**

| Entity Type | Min. Share Capital | Min. Paid In Before the Application | Payment Timing | In-Kind Contributions |
| --- | --- | --- | --- | --- |
| GmbH | twenty-five thousand euros | Half of the minimum share capital in total, and one quarter of each cash share | Before the register application | Permitted. They must be set out in the articles, with a report on the formation in kind (§ 5(4) GmbHG), and made in full before the application. The court fee is higher (Step 4 table) |
| UG (haftungsbeschränkt) | one euro | The whole stated capital, in cash | Before the register application | Excluded (§ 5a(2) GmbHG) |
| AG | fifty thousand euros | One quarter of the lowest issue price of each share, plus any premium in full | Before the register application | Permitted. Made in full. A duty to transfer an asset must be carried out within five years of the entry (§ 36a(2) AktG). The formation is audited by formation auditors (§ 33(2) no. 4 AktG), unless the narrow exception of § 33a AktG applies: traded securities at their average market price, or other assets valued by an independent expert not more than six months before. The court fee is higher (Step 4 table) |

## Section 5: Costs Breakdown

The legacy version of this section gave euro ranges for notary fees, adviser fees and a total. No official page prints those ranges, so they are gone. What the official pages do print is below.

| Cost Component | GmbH | UG | Notes |
| --- | --- | --- | --- |
| Notary fee (Musterprotokoll) | By the fee statute (GNotKG). See the four tables below | Same | With the model protocol the floor for the business value does not apply, so the value can be lower than the floor |
| Notary fee (custom Satzung) | By the fee statute. The floor for the business value applies | Same | The notary quotes the fee. This skill does not compute one |
| Handelsregister fee | See the Step 4 table | Same fee number as the GmbH | Plus the separate retrieval fee (no. 6000) |
| Gewerbeanmeldung | Set by the municipality (Step 5) | Same | No federal amount |
| Share capital deposit | See Section 4 | See Section 4 | Stays in the company as its own money |
| Steuerberater (initial setup) | No official figure | No official figure | Agreed with the adviser |
| Total (excl. capital) | Not stated | Not stated | No official page prints a total, and this skill does not add fees up |

**Notary fees: the business value (Geschäftswert) for the articles**

| What | Value | Note | Source |
| --- | --- | --- | --- |
| Source | all figures below | https://www.gesetze-im-internet.de/gnotkg/__107.html |  |
| Lowest business value for notarising articles of association. It does NOT apply to a formation with the model protocol (§ 105(6) GNotKG) | EUR 30,000 | § 107(1) GNotKG: "beträgt der Geschäftswert mindestens 30 000 Euro" | https://www.gesetze-im-internet.de/gnotkg/__107.html |

**Notary fees: the business value for the first register application of a company**

| What | Value | Note | Source |
| --- | --- | --- | --- |
| Source | all figures below | https://www.gesetze-im-internet.de/gnotkg/__105.html |  |
| The business value is the capital to be entered in the register, and not less than this. The floor does NOT apply to a formation with the model protocol (§ 105(6) GNotKG) | EUR 30,000 | § 105(1) GNotKG: "Der Geschäftswert beträgt mindestens 30 000 Euro" | https://www.gesetze-im-internet.de/gnotkg/__105.html |

**Notary fees: the fee rates for notarising (fee schedule, part 2)**

| What | Value | Note | Source |
| --- | --- | --- | --- |
| Source | all figures below | https://www.gesetze-im-internet.de/gnotkg/anlage_1.html |  |
| Lowest fee for notarising a contract (no. 21100, fee rate 2.0). A formation by two or more founders is a contract | EUR 120 | No. 21100 Beurkundungsverfahren: "mindestens 120,00 €" | https://www.gesetze-im-internet.de/gnotkg/anlage_1.html |
| Lowest fee for notarising other declarations (no. 21200, fee rate 1.0). The schedule does not name the one-person formation. Ask the notary which number applies | EUR 60 | No. 21200 Beurkundungsverfahren: "Unerheblich ist, ob eine Erklärung von einer oder von mehreren Personen abgegeben wird", then "mindestens 60,00 €" | same |

**Notary fees: the single fee from Table B (the table notaries use)**

| What | Value | Note | Source |
| --- | --- | --- | --- |
| Source | all figures below | https://www.gesetze-im-internet.de/gnotkg/anlage_2.html |  |
| Single fee (rate 1.0) for a business value up to EUR 25,000 | EUR 115 | Table B row "25 000 435,50 115,00". The first number is the value step, the second is Table A, the third is Table B | https://www.gesetze-im-internet.de/gnotkg/anlage_2.html |
| Single fee (rate 1.0) for a business value up to EUR 30,000 | EUR 125 | Table B row "30 000 476,00 125,00" | same |

How the notary fee is built: the fee rate from the schedule is applied to the single fee that Table B gives for the business value. Separate fees can come on top, for drafting the register application, for carrying out the filing and for producing the structured electronic data, plus outlays and VAT (fee schedule, no. 32014). These amounts are building blocks, not a quote. Agreements on the amount of notary costs are void, except where the next section allows one (§ 125 GNotKG): https://www.gesetze-im-internet.de/gnotkg/__125.html That exception (§ 126 GNotKG) covers only work as a mediator or conciliator, and official acts for which the statute sets no fee and that are not connected with other acts that carry a fee: https://www.gesetze-im-internet.de/gnotkg/__126.html Notarising the articles and certifying the register application have fees in the schedule, so the formation fee cannot be negotiated. Ask the notary to state it in advance.

### Annual Maintenance

The legacy version gave euro ranges for chamber contributions, accident insurance, advisers and publication costs. No official page prints those ranges, so they are gone.

| Item | Cost |
| --- | --- |
| IHK membership | Set by each chamber's own rules (§ 3 IHKG). No federal amount. See Step 8 |
| Berufsgenossenschaft | Worked out by the accident insurer after the end of each business year. No federal amount. See https://www.dguv.de/de/ihr_partner/unternehmen/index.jsp |
| Steuerberater | Agreed with the adviser. No official figure |
| Disclosure of annual accounts | Sent electronically to the company register (§ 325 HGB, see Section 6). The register's own page explains where and how to file: https://www.unternehmensregister.de/ureg/ No fee was found on the pages read |
| Handelsregister changes | See the table below |

**Court fees for later entries in the commercial register, division B (GmbH, UG, AG)**

| What | Value | Note | Source |
| --- | --- | --- | --- |
| Source | all figures below | https://www.gesetze-im-internet.de/hreggebv/anlage.html |  |
| Entry of one fact, for example a new managing director (this skill's example, the schedule gives none) (no. 2500) | EUR 105 | "2500 Eintragung einer Tatsache 105,00 €" | https://www.gesetze-im-internet.de/hreggebv/anlage.html |
| Second and each further fact in the same application (no. 2501) | EUR 60 | "Eintragung der zweiten und jeder weiteren Tatsache aufgrund derselben Anmeldung: Die Gebühr 2500 beträgt jeweils 60,00 €" | same |
| Entry of a fact with no economic significance (no. 2502). The schedule gives no examples | EUR 45 | "Die Eintragung betrifft eine Tatsache ohne wirtschaftliche Bedeutung: Die Gebühren 2500 und 2501 betragen 45,00 €" | same |
| Receipt of a new shareholder list (no. 5002) | EUR 45 | "der Liste der Gesellschafter (§ 40 GmbHG) 45,00 €" | same |

The retrieval fee (no. 6000, one third of the fee in question) comes on top of each of these as well. Capital measures and conversions have their own, higher fee numbers on the same page.

## Section 6: Post-Formation Compliance

| Obligation | Deadline | Authority |
| --- | --- | --- |
| Jahresabschluss (annual financial statements), preparation | Within the first three months of the new financial year. A small company may take longer if that fits an orderly course of business, but no longer than the first six months (§ 264(1) HGB) | Managing directors |
| Adoption of the accounts and decision on the profit | Shareholders decide within the first eight months of the financial year, or the first eleven months for a small company. The articles cannot extend this (§ 42a(2) GmbHG) | Shareholders' meeting |
| Offenlegung (disclosure) | Sent electronically to the company register at the latest one year after the balance sheet date (§ 325(1a) HGB). Not the Bundesanzeiger, as older texts say | Unternehmensregister. The Federal Office of Justice enforces it (§ 335 HGB) |
| Körperschaftsteuererklärung (corporate tax return) | Seven months after the end of the calendar year. If an adviser prepares it: the last day of February of the second calendar year after the tax period (§ 149(2) and (3) AO). The tax office can call an advised return in earlier (§ 149(4) AO) | Finanzamt |
| Gewerbesteuererklärung (trade tax return) | Same deadlines as the corporate tax return (§ 149 AO) | Finanzamt. The municipality sets and collects the tax |
| Umsatzsteuervoranmeldung (VAT returns) | Quarterly or monthly, see the Step 6 table. Annual VAT return on top. Not for a business under the small-business rule of § 19 UStG (Step 6) | Finanzamt |
| E-invoices (E-Rechnung) | Receiving: since 1 January 2025 every business established in Germany must be able to receive an e-invoice from another German business. There are no exceptions, small businesses under § 19 UStG included, and an e-mail inbox is enough (finance ministry FAQ). A small business under § 19 UStG must receive e-invoices but need not issue them (§ 34a UStDV, FAQ question 4). Issuing: for supplies made in 2025 and 2026 an invoice between German businesses may still be sent on paper, or with the recipient's consent in another electronic format, until 31 December 2026; a narrower transition for 2027 depends on the issuer's turnover in the previous year (§ 27(38) UStG). See `germany-einvoice` | None. It is a standing duty from the first supply |
| Gesellschafterliste (shareholder list) | Without undue delay after any change in the shareholders or their holdings. The managing directors file it, or the notary if a notary took part in the change (§ 40 GmbHG) | Handelsregister |
| Business letters | Every business letter, in any form, that is addressed to a specific recipient states the legal form, the seat, the register court and number, and all managing directors by surname and at least one full first name, plus the chair of the supervisory board if there is one. Order forms always count as business letters. Routine notices within an existing business relationship on preprinted forms are exempt (§ 35a GmbHG) | None. It is a standing duty |
| Transparenzregister | Keep the details current and report changes without undue delay (§ 20(1) GwG). The statute sets no number of days | Transparenzregister |

Sources for the table: https://www.bundesfinanzministerium.de/Content/DE/FAQ/e-rechnung.html and https://www.gesetze-im-internet.de/ustg_1980/__27.html and https://www.gesetze-im-internet.de/hgb/__264.html and https://www.gesetze-im-internet.de/gmbhg/__42a.html and https://www.gesetze-im-internet.de/hgb/__325.html and https://www.gesetze-im-internet.de/ao_1977/__149.html and https://www.gesetze-im-internet.de/gmbhg/__40.html and https://www.gesetze-im-internet.de/gmbhg/__35a.html

**What "small" and "micro" mean (size classes)**

A class applies when two or more of its three criteria are not exceeded. The legal effects normally start only when that holds on the balance sheet dates of two financial years in a row, but for a newly formed company the first balance sheet date is enough (§ 267(4) HGB). Apprentices are not counted as employees.

| What | Value | Note | Source |
| --- | --- | --- | --- |
| Source | all figures below | https://www.gesetze-im-internet.de/hgb/__267.html |  |
| Small company: balance sheet total | EUR 7,500,000 | § 267(1) HGB: "7 500 000 Euro Bilanzsumme" | https://www.gesetze-im-internet.de/hgb/__267.html |
| Small company: revenue in the twelve months before the balance sheet date | EUR 15,000,000 | § 267(1) HGB: "15 000 000 Euro Umsatzerlöse in den zwölf Monaten vor dem Abschlußstichtag" | same |
| Small company: yearly average number of employees, printed in words | fifty employees | § 267(1) HGB: "Im Jahresdurchschnitt fünfzig Arbeitnehmer" | same |

| What | Value | Note | Source |
| --- | --- | --- | --- |
| Source | all figures below | https://www.gesetze-im-internet.de/hgb/__267a.html |  |
| Micro company: balance sheet total | EUR 450,000 | § 267a(1) HGB: "450 000 Euro Bilanzsumme" | https://www.gesetze-im-internet.de/hgb/__267a.html |
| Micro company: revenue in the twelve months before the balance sheet date | EUR 900,000 | § 267a(1) HGB: "900 000 Euro Umsatzerlöse in den zwölf Monaten vor dem Abschlussstichtag" | same |
| Micro company: yearly average number of employees, printed in words | ten employees | § 267a(1) HGB: "im Jahresdurchschnitt zehn Arbeitnehmer" | same |

A small company files only the balance sheet and the notes. A micro company files only the balance sheet and may have it deposited instead of published, if it tells the register that it keeps within the micro criteria (§ 326 HGB): https://www.gesetze-im-internet.de/hgb/__326.html Pure holding companies, investment companies and equity participation companies cannot be micro companies (§ 267a(3) HGB).

**Fine for not disclosing the annual accounts (Ordnungsgeld)**

| What | Value | Note | Source |
| --- | --- | --- | --- |
| Source | all figures below | https://www.gesetze-im-internet.de/hgb/__335.html |  |
| Lowest fine, printed in words. It is first threatened, with six weeks from receipt of the threat to comply or object (§ 335(3) HGB) | two thousand five hundred euros | § 335(1) HGB: "Das Ordnungsgeld beträgt mindestens zweitausendfünfhundert und höchstens fünfundzwanzigtausend Euro" | https://www.gesetze-im-internet.de/hgb/__335.html |
| Highest fine, printed in words. A capital-market company faces a higher ceiling (§ 335(1a) HGB) | twenty-five thousand euros | Same sentence | same |
| Reduced fine when the accounts are filed after the six weeks have run out but before the Federal Office decides on the fine, for a micro company that used its deposit right | EUR 500 | § 335(4) HGB: "auf einen Betrag von 500 Euro, wenn die Beteiligten von dem Recht einer Kleinstkapitalgesellschaft" | https://www.gesetze-im-internet.de/hgb/__335.html |
| Reduced fine in the same late case for a small company | EUR 1,000 | § 335(4) HGB: "auf einen Betrag von 1 000 Euro, wenn es sich um eine kleine Kapitalgesellschaft" | same |

The costs of the procedure come on top: they are imposed together with the threat of the fine (§ 335(3) HGB). The fines go to the Federal Office of Justice, which runs the procedure. Its page describes the cycle: if the duty is still not met, the fine is set and the order is repeated under threat of a new fine, until the accounts are disclosed, with the fine normally raised step by step: https://www.bundesjustizamt.de/DE/Themen/OrdnungsgeldVollstreckung/Jahresabschluesse/Offenlegung/Verfahren/Verfahren_node.html

**Bookkeeping duty depends on the legal form**

A GmbH or UG counts as a commercial company (§ 13(3) GmbHG), and so does an AG (§ 3 AktG). The rules for merchants apply to commercial companies (§ 6(1) HGB), so the company must keep books (§ 238 HGB): https://www.gesetze-im-internet.de/hgb/__238.html The two rules below are not for companies. They matter when the choice is between a company and a sole trader business.

| What | Value | Note | Source |
| --- | --- | --- | --- |
| Source | all figures below | https://www.gesetze-im-internet.de/hgb/__241a.html |  |
| Sole merchants only: released from commercial-law bookkeeping while revenue stays within this limit | EUR 800,000 | § 241a HGB: "nicht mehr als jeweils 800 000 Euro Umsatzerlöse" | https://www.gesetze-im-internet.de/hgb/__241a.html |
| AND annual net profit stays within this limit. Both limits, on the balance sheet dates of two financial years in a row. For a new business the first balance sheet date is enough | EUR 80,000 | § 241a HGB: "jeweils 80 000 Euro Jahresüberschuss" | same |

| What | Value | Note | Source |
| --- | --- | --- | --- |
| Source | all figures below | https://www.gesetze-im-internet.de/ao_1977/__141.html |  |
| Tax-law bookkeeping duty for traders who are not already bound by other law: total turnover of more than this in the calendar year | EUR 800,000 | § 141(1) no. 1 AO: "von mehr als 800 000 Euro im Kalenderjahr" | https://www.gesetze-im-internet.de/ao_1977/__141.html |
| OR profit from the trade of more than this in the business year. Either test is enough. The duty starts only with the business year after the tax office's notice | EUR 80,000 | § 141(1) no. 4 AO: "einen Gewinn aus Gewerbebetrieb von mehr als 80 000 Euro im Wirtschaftsjahr" | same |

See `germany-bookkeeping` and `germany-financial-statements` for the detail.

## Section 7: Bank Account Opening

No official page read for this skill describes how banks open company accounts. The two lists and the note below are legacy practice notes. Only the beneficial owner test is law.

### Documents Typically Required

- Handelsregisterauszug (commercial register extract), once the company is entered
- Gesellschaftsvertrag (articles of association)
- Notarised appointment of the Geschäftsführer
- ID (passport or Personalausweis) for all managing directors and for the beneficial owners. The test for a beneficial owner is in the Step 7 table (§ 3(2) GwG)
- Proof of address for all beneficial owners
- Business plan or description of activities

### Typical Timeline

- **Traditional banks.** Legacy estimate: 2 to 4 weeks (customer due diligence).
- **Neo-banks.** Legacy estimate: 1 to 5 days.
- **i.G. stage note.** Legacy practice note: the account can be opened at the "GmbH i.G." stage, before the register entry. The capital has to be paid in before the application in any case (Step 3).

### Common Banks

The legacy version named commercial banks here. The names are gone: no official page supports such a list, a name in a public skill reads as a recommendation, and offers change. Business accounts come from branch banks (private banks, savings banks, cooperative banks) and from online-only providers. Whether a given provider opens an account for a GmbH in formation, or for a company at all, must be checked with that provider.

## Section 8: Foreign Founder Considerations

| Question | Answer |
| --- | --- |
| Non-resident Geschäftsführer allowed? | § 6(2) GmbHG lists who cannot be managing director. Residence and nationality are not on that list. A comparable ban in another EU or EEA state counts, and so does a conviction abroad for a comparable offence |
| Minimum German-resident director? | The GmbHG does not ask for one. The company does need its seat in Germany (§ 4a GmbHG) and a business address in Germany in the register (§ 8(4) GmbHG). Legacy practice note: a resident director helps with banks and the tax office |
| Instruction of a director abroad | The instruction about the duty to give the court full information can be given in writing, or by a foreign notary, a comparable legal adviser or a consular officer (§ 8(3) GmbHG) |
| Video notarisation for foreigners? | The start-up portal says the online route can be used from abroad, but only with an electronic identity that § 16c BeurkG accepts: a German one, or one from another EU or EEA state notified at level "high", plus a photo read from the chip of an identity card, passport or residence permit. See Step 2 |
| Apostille requirements | Legacy note: foreign documents need an apostille or legalisation and a certified German translation. No official page read for this skill states this. Ask the notary |
| Physical presence required? | Not strictly. A representative can sign with a power of attorney that a notary drew up or certified (§ 2(2) GmbHG). That power of attorney can itself be drawn up by video |
| Trade notification by a non-German | The start-up portal lists a residence permit that allows self-employed trading among the papers for the trade office. Immigration law is outside this skill |
| Foreign ownership restrictions | The GmbHG sets none. Investment screening under the Außenwirtschaftsverordnung is about acquiring an existing German business or a stake in one. § 55 covers buyers from outside the EU. The sections on specific sectors were not read for this skill. Refer such cases |

Sources for the table: https://www.existenzgruendungsportal.de/_noch_neu_einordnen/DE/Gruendung-vorbereiten/Rechtsformen/Gesellschaft-mit-beschraenkter-Haftung-GmbH/inhalt.html and https://www.existenzgruendungsportal.de/Navigation/DE/Gruendungswissen/Behoerden/behoerden and https://www.gesetze-im-internet.de/gmbhg/__6.html and https://www.gesetze-im-internet.de/gmbhg/__8.html and https://www.gesetze-im-internet.de/beurkg/__16c.html and https://www.gesetze-im-internet.de/awv_2013/__55.html

Whether a founder or director from outside the EU needs a visa or residence permit to work in Germany is immigration law. It is outside this skill.

## Section 9: Common Mistakes and Refusals

- **R-DE-F1: UG with minimal capital and no plan.** A UG with the legal minimum is possible but fragile. The start-up portal says the capital should follow the real need, because thin capital always carries a high risk of insolvency: https://www.existenzgruendungsportal.de/_noch_neu_einordnen/DE/Gruendung-vorbereiten/Rechtsformen/UG-haftungsbeschraenkt/inhalt The legacy version named a euro range as the capital to advise. No official page prints one, so it is gone. Remember that under the model protocol the company bears its formation costs only up to the cap in the Step 1 table, and never beyond its share capital. The rest falls on the founders.
- **R-DE-F2: Trading before Handelsregister entry.** The GmbH does not exist as such until it is entered. If someone acts in the company's name before that, the persons acting are liable personally, jointly and severally (§ 11(2) GmbHG): https://www.gesetze-im-internet.de/gmbhg/__11.html The statute says "die Handelnden" (the persons acting), not only the managing director. Flag this risk clearly.
- **R-DE-F3: Missing Transparenzregister filing.** The old rule, under which the duty could count as met without a report, ended on 31 July 2021 (Step 7). Not reporting, or reporting late, wrongly or incompletely, is an administrative offence if done with intent or recklessly (§ 56(1) no. 55 GwG). The statute prints the ceilings in words: a fine of up to one hundred and fifty thousand euros for intent ("bis zu einhundertfünfzigtausend Euro"), otherwise up to one hundred thousand euros. Serious, repeated or systematic breaches carry more (§ 56(3) GwG): https://www.gesetze-im-internet.de/gwg_2017/__56.html
- **R-DE-F4: Sacheinlage in UG.** Contributions in kind are excluded for a UG under § 5a(2) GmbHG. Only cash works. A hidden contribution in kind (Step 3) is the same mistake in disguise.
- **R-DE-F5: Ignoring Berufsgenossenschaft.** The duty to notify the accident insurer within one week applies to every entrepreneur, with or without employees. A trade notification made within that week counts as the notice. Not notifying, or notifying late, is an administrative offence (§ 209(1) no. 8 SGB VII). The statute prints the ceiling in words: up to two thousand five hundred euros: https://www.gesetze-im-internet.de/sgb_7/__209.html
- **R-DE-F6: Believing the UG reserve duty ends by itself.** It does not end when the reserve is full. It ends when the registered capital is raised to the GmbH minimum (Section 4).
- **R-DE-F7: Missing the disclosure deadline.** Every GmbH and UG must send its accounts to the company register within one year of the balance sheet date (§ 325 HGB). Size does not remove the duty. It only changes what is filed and how far a late fine is reduced (Section 6).

## Section 10: Timeline

The durations below are legacy estimates. The only durations found on official pages are: a trade notification is normally processed within a few days (start-up portal, Step 5), and the VAT identification number request can take some weeks to pass from the tax office to the BZSt (Step 6). Court and notary times vary and no official page states them.

| Step | Duration | Cumulative |
| --- | --- | --- |
| Draft articles or Musterprotokoll | 1 to 5 days | Day 1 to 5 |
| Notary appointment | 1 to 7 days | Day 2 to 12 |
| Open bank account (i.G.) and deposit capital | 1 to 3 weeks | Day 9 to 33 |
| Notary files with Handelsregister | 1 day | Day 10 to 34 |
| Handelsregister entry | 1 to 3 weeks | Day 17 to 55 |
| Gewerbeanmeldung | 1 to 3 days | Day 18 to 58 |
| Tax registration (ELSTER) | 2 to 6 weeks | Day 32 to 100 |
| Transparenzregister | 1 to 2 days | Day 33 to 102 |
| **All steps done** |  | **Day 33 to 102 by these legacy estimates** |

The main bottleneck is the processing time at the register court, which varies by court district. The legal deadlines run regardless: one month for the tax notice and questionnaire (Step 6), one week for the accident insurer (Step 8), and "without undue delay" for the Transparenzregister (Step 7).

## The method, step by step

1. Pick the legal form with Section 2: who is liable, how much capital can be paid in now, and who the founders are. GmbH and UG rules are in the GmbHG, starting with the capital rule in § 5: https://www.gesetze-im-internet.de/gmbhg/__5.html
2. Draft the articles with the minimum content of § 3 GmbHG, or use the model protocol of § 2(1a) GmbHG if there are at most three shareholders, one managing director and cash only: https://www.gesetze-im-internet.de/gmbhg/__2.html
3. Have the articles notarised, in person or by video (§ 2 GmbHG, § 16a BeurkG): https://www.gesetze-im-internet.de/beurkg/__16a.html
4. Pay in the capital so that it is at the free disposal of the managing directors: the GmbH amounts of § 7(2) GmbHG, or the whole capital for a UG under § 5a(2) GmbHG: https://www.gesetze-im-internet.de/gmbhg/__7.html
5. File the certified application with the register court through the notary, with the attachments of § 8 GmbHG, and pay the court fee from the Handelsregistergebührenverordnung: https://www.gesetze-im-internet.de/hreggebv/anlage.html
6. Wait for the entry. Until then the company does not exist as such and whoever acts in its name is personally liable (§ 11 GmbHG): https://www.gesetze-im-internet.de/gmbhg/__11.html
7. Notify the trade office at the moment the business starts (§ 14 GewO): https://www.gesetze-im-internet.de/gewo/__14.html
8. Within one month of the formation, without waiting for the register entry, notify the tax office (§ 137 AO) and send the ELSTER form "Fragebogen zur steuerlichen Erfassung: Gründung einer Kapitalgesellschaft beziehungsweise Genossenschaft" (§ 138(1b) AO). Tick the VAT identification number box if the company will trade across EU borders: https://www.elster.de/eportal/formulare-leistungen/alleformulare/fsekapg
9. Report the beneficial owners to the Transparenzregister without undue delay (§ 20(1) GwG): https://www.gesetze-im-internet.de/gwg_2017/__20.html
10. Make sure the accident insurer hears of the business within one week of its start (§ 192(1) SGB VII): https://www.gesetze-im-internet.de/sgb_7/__192.html
11. Put the standing duties of Section 6 in the calendar: accounts, adoption, disclosure within one year (§ 325 HGB), tax returns, shareholder list: https://www.gesetze-im-internet.de/hgb/__325.html

## Ask the client first

- Who are the founders: how many, natural persons or companies, is one of them a GbR, and does every one of them hold an electronic identity that works for a video notarisation?
- How much capital can be paid in, in cash, before the application? Is any contribution to be made in kind, or will the company buy assets from a founder soon after the formation?
- Is the activity a trade, a craft or a liberal profession, and does it need a permit or licence?
- One managing director or more? Is any of them banned from a trade or profession now, in Germany or another EU or EEA state? Was any of them convicted of an offence, in Germany or abroad, in the last five years?
- Will anyone sign contracts in the company's name before the register entry?
- What turnover is expected in the first calendar year, and will the company buy or sell across EU borders? This decides the small-business VAT rule, the filing rhythm and the VAT identification number.

## When to refuse or refer

- Drafting custom articles, shareholder agreements, vesting or investor rights. That is work for a notary or lawyer.
- Formations with contributions in kind, suspected hidden contributions in kind, and the capital increase that takes a UG up to a GmbH.
- An AG beyond the outline here, and every form not covered: KGaA, SE, GmbH & Co. KG, cooperative, association, foundation, and the branch of a foreign company.
- Conversions and mergers under the Umwandlungsgesetz.
- Activities that need a licence, for example banking, insurance and financial services, or a regulated craft.
- Visa and residence questions for founders from outside the EU, and the apostille or legalisation of foreign documents.
- A buyer from outside the EU acquiring an existing German business (investment screening under the Außenwirtschaftsverordnung).
- A quote for the notary's fee. Ask the notary.
- Tax structuring: company or partnership, the option for a partnership to be taxed like a corporation (§ 1a KStG), holding structures and tax groups. Refer to a Steuerberater.
- A company that is already in financial trouble. Insolvency duties are outside this skill.

```oa-check
name: DE GmbH 2026, least paid in before the register application
inputs:
  minimum_capital: 25000
steps:
  - paid_in: minimum_capital * 0.5
expected:
  paid_in: 12500.00
```

```oa-check
name: DE GmbH 2026, trade tax, no allowance, multiplier 400%
inputs:
  trade_income: 50000
  hebesatz: 4.0
steps:
  - base: trade_income * 0.035
  - trade_tax: base * hebesatz
expected:
  trade_tax: 7000.00
```

## Sources

- GmbHG §§ 1 to 8, 10, 11, 13, 19, 35a, 40, 42a, 57c, 57e: https://www.gesetze-im-internet.de/gmbhg/__2.html and https://www.gesetze-im-internet.de/gmbhg/__35a.html and https://www.gesetze-im-internet.de/gmbhg/__5.html and https://www.gesetze-im-internet.de/gmbhg/__5a.html and https://www.gesetze-im-internet.de/gmbhg/__7.html and https://www.gesetze-im-internet.de/gmbhg/__8.html and https://www.gesetze-im-internet.de/gmbhg/__11.html (read 2026-10-31)
- GmbHG model protocols, Annex 1 and Annex 2: https://www.gesetze-im-internet.de/normengrafiken/bgbl1_2021/j3364_0010.pdf and https://www.gesetze-im-internet.de/gmbhg/anlage_2.html (read 2026-10-31)
- AktG §§ 1, 2, 3, 7, 23, 30, 33, 33a, 36, 36a, 41, 95: https://www.gesetze-im-internet.de/aktg/__7.html and https://www.gesetze-im-internet.de/aktg/__36a.html and https://www.gesetze-im-internet.de/aktg/__33a.html (read 2026-10-31)
- Handelsregisterverordnung § 3: https://www.gesetze-im-internet.de/hdlregvfg/__3.html (read 2026-10-31)
- HGB §§ 1, 2, 6, 12, 19, 29, 105, 106, 107, 123, 126, 161, 162, 171, 176, 238, 241a, 264, 267, 267a, 325, 326, 335: https://www.gesetze-im-internet.de/hgb/__12.html and https://www.gesetze-im-internet.de/hgb/__267.html and https://www.gesetze-im-internet.de/hgb/__335.html (read 2026-10-31)
- Civil Code §§ 705, 707, 707b, 719, 721 and PartGG §§ 1, 4, 8: https://www.gesetze-im-internet.de/bgb/__705.html and https://www.gesetze-im-internet.de/bgb/__719.html and https://www.gesetze-im-internet.de/bgb/__707b.html and https://www.gesetze-im-internet.de/partgg/__1.html (read 2026-10-31)
- Beurkundungsgesetz §§ 16a, 16c: https://www.gesetze-im-internet.de/beurkg/__16a.html (read 2026-10-31)
- Handelsregistergebührenverordnung, fee schedule: https://www.gesetze-im-internet.de/hreggebv/anlage.html (read 2026-10-31)
- GNotKG §§ 34, 105, 107, 125, 126 and its two annexes: https://www.gesetze-im-internet.de/gnotkg/__105.html and https://www.gesetze-im-internet.de/gnotkg/__126.html and https://www.gesetze-im-internet.de/gnotkg/__107.html and https://www.gesetze-im-internet.de/gnotkg/anlage_1.html and https://www.gesetze-im-internet.de/gnotkg/anlage_2.html (read 2026-10-31)
- GewO §§ 6, 14, 146: https://www.gesetze-im-internet.de/gewo/__6.html and https://www.gesetze-im-internet.de/gewo/__14.html (read 2026-10-31)
- AO §§ 137, 138, 139c, 141, 149: https://www.gesetze-im-internet.de/ao_1977/__139c.html and https://www.gesetze-im-internet.de/ao_1977/__137.html and https://www.gesetze-im-internet.de/ao_1977/__138.html (read 2026-10-31)
- UStG §§ 14, 18, 19, 27, 27a and UStDV § 33: https://www.gesetze-im-internet.de/ustg_1980/__14.html and https://www.gesetze-im-internet.de/ustdv_1980/__33.html and https://www.gesetze-im-internet.de/ustg_1980/__18.html and https://www.gesetze-im-internet.de/ustg_1980/__27.html and https://www.gesetze-im-internet.de/ustg_1980/__19.html and https://www.gesetze-im-internet.de/ustg_1980/__27a.html (read 2026-10-31)
- KStG §§ 1, 1a, 23, SolzG § 4, GewStG §§ 2, 5, 11, 16: https://www.gesetze-im-internet.de/kstg_1977/__23.html and https://www.gesetze-im-internet.de/solzg_1995/__4.html and https://www.gesetze-im-internet.de/gewstg/__11.html (read 2026-10-31)
- GwG §§ 3, 19, 20, 56, 59: https://www.gesetze-im-internet.de/gwg_2017/__20.html (read 2026-10-31)
- IHKG §§ 2, 3, SGB VII §§ 192, 209, DrittelbG § 1, Außenwirtschaftsverordnung § 55: https://www.gesetze-im-internet.de/ihkg/__3.html and https://www.gesetze-im-internet.de/sgb_7/__192.html (read 2026-10-31)
- Federal Employment Agency, Betriebsnummern-Service: https://www.arbeitsagentur.de/unternehmen/betriebsnummern-service/alles-wichtige (read 2026-10-31)
- Start-up portal of the Federal Government, pages on the GmbH, the UG, the commercial register, the authorities, and registering a business: https://www.existenzgruendungsportal.de/_noch_neu_einordnen/DE/Gruendung-vorbereiten/Rechtsformen/Gesellschaft-mit-beschraenkter-Haftung-GmbH/inhalt.html and https://www.existenzgruendungsportal.de/_noch_neu_einordnen/DE/Gruendung-vorbereiten/Rechtsformen/UG-haftungsbeschraenkt/inhalt and https://www.existenzgruendungsportal.de/_noch_neu_einordnen/DE/Gruendung-vorbereiten/Gruendungswissen/Behoerden/Handelsregister/inhalt and https://www.existenzgruendungsportal.de/Navigation/DE/Gruendungswissen/Behoerden/behoerden and https://www.existenzgruendungsportal.de/Navigation/DE/So-gehts/Unternehmensanmeldung/unternehmensanmeldung (read 2026-10-31)
- ELSTER, questionnaire for tax registration of a corporation: https://www.elster.de/eportal/formulare-leistungen/alleformulare/fsekapg (read 2026-10-31)
- BZSt, VAT identification number and business identification number: https://www.bzst.de/DE/Unternehmen/Identifikationsnummern/Umsatzsteuer-Identifikationsnummer/Vergabe_USt_IdNr/vergabe_ust_idnr_node.html and https://www.bzst.de/DE/Unternehmen/Identifikationsnummern/Wirtschafts-Identifikationsnummer/wirtschaftsidentifikationsnummer_node.html (read 2026-10-31)
- Federal Office of Justice, fine procedure for undisclosed accounts: https://www.bundesjustizamt.de/DE/Themen/OrdnungsgeldVollstreckung/Jahresabschluesse/Offenlegung/Verfahren/Verfahren_node.html (read 2026-10-31)
- Register portal of the federal states and the company register: https://www.handelsregister.de/rp_web/welcome.xhtml and https://www.unternehmensregister.de/ureg/ (read 2026-10-31)
- German Social Accident Insurance (DGUV), page for businesses: https://www.dguv.de/de/ihr_partner/unternehmen/index.jsp (read 2026-10-31)
- Finance ministry, questions and answers on the compulsory e-invoice (Stand März 2026): https://www.bundesfinanzministerium.de/Content/DE/FAQ/e-rechnung.html (read 2026-10-31)
- Finance ministry, instructions for the 2026 EÜR form, letter of 1 September 2026: https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Einkommensteuer/2026-09-01-anlage-EUER-2026.pdf?__blob=publicationFile&v=2
- [AO § 141](https://www.gesetze-im-internet.de/ao_1977/__141.html), read 2026-10-31
- [GwG § 3](https://www.gesetze-im-internet.de/gwg_2017/__3.html), read 2026-10-31
- [HGB § 241a](https://www.gesetze-im-internet.de/hgb/__241a.html), read 2026-10-31
- [HGB § 267a](https://www.gesetze-im-internet.de/hgb/__267a.html), read 2026-10-31

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute legal, tax, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before acting upon.

The most up-to-date version of this skill is maintained at openaccountants.com.

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
