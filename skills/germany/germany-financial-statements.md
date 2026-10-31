---
name: germany-financial-statements
description: Use this skill when preparing, reviewing, or advising on annual financial statements (Jahresabschluss) for a German company. Trigger on phrases like "Jahresabschluss", "HGB", "Handelsgesetzbuch", "Bundesanzeiger", "Unternehmensregister", "Offenlegung", "Bilanz", "GuV", "GmbH accounts", "Kapitalgesellschaft", "audit Germany", "Kleinstkapitalgesellschaft", "kleine Kapitalgesellschaft", or any question about preparing and filing statutory accounts under German commercial law. Covers HGB frameworks, size thresholds, required statements, formats, notes, filing deadlines, and audit requirements.
version: 1.1
jurisdiction: DE
tax_year: 2026
last_updated: 2026-10-31
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
drafted_by: OpenAccountants
approved_by: pending
depends_on:
  - financial-statements-workflow-base
category: financial-statements
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Annual financial statements in Germany (Jahresabschluss under the HGB)

How a German business draws up, has audited and publishes its annual financial statements under the Commercial Code (Handelsgesetzbuch, HGB): which rules bind which legal form, the size classes, the statements each class needs, the statutory layouts of the balance sheet and the P&L, the notes, publication in the company register, the fine for late publication, and the audit duty. It is for GmbH, UG, AG and KGaA, for partnerships such as the GmbH & Co. KG, and for the people who prepare their accounts. Figures are for tax year 2026. The figures are read from the consolidated federal law pages as they stood on 19 September 2026 and from the Federal Office of Justice (Bundesamt für Justiz). The size limits apply to financial years that begin after 31 December 2023. Publication in the company register applies to financial years that begin after 31 December 2021. One help page of the Federal Office of Justice still prints older, lower limits for micro companies; this Guide follows the statute.

## Section 1: Quick Reference

| Field | Value | Source |
| --- | --- | --- |
| Country | Germany (Bundesrepublik Deutschland) | same |
| Currency | Euro. The statements are drawn up in German and in euro (§ 244 HGB) | https://www.gesetze-im-internet.de/hgb/__244.html |
| Filing authority | The company register (Unternehmensregister), for financial years that begin after 31 December 2021. Statements for earlier financial years go to the operator of the Bundesanzeiger (§ 325 HGB, Art. 88 EGHGB) | https://www.gesetze-im-internet.de/hgb/__325.html |
| Primary legislation | Handelsgesetzbuch (HGB), Third Book (Handelsbücher), §§ 238 to 342r | https://www.gesetze-im-internet.de/hgb/__342r.html |
| Supporting legislation | GmbHG; AktG; PublG (Publizitätsgesetz); EGHGB (start dates and transition rules) | same |
| Accounting standards | HGB (German GAAP). IFRS as adopted by the EU for the consolidated accounts of listed parent companies (§ 315e HGB) | https://www.gesetze-im-internet.de/hgb/__315e.html |
| Financial year | Not longer than twelve months (§ 240(2) HGB). The Federal Office of Justice notes that it is the calendar year in most cases | https://www.bundesjustizamt.de/DE/Themen/OrdnungsgeldVollstreckung/Jahresabschluesse/Offenlegung/Pflichten/Pflichten_node.html |
| Filing deadline | One year after the balance sheet date. Four months for capital-market companies. It cannot be extended. See Section 9 | same |
| Late filing penalty | An administrative fine (Ordnungsgeld) plus procedure costs. See the fine tables in Section 9 | https://www.bundesjustizamt.de/DE/Themen/OrdnungsgeldVollstreckung/Jahresabschluesse/Offenlegung/Verfahren/Verfahren_node.html |
| Digital filing | Electronic only. Orders are sent through the publication platform of the Bundesanzeiger and the company register (publikations-plattform.de) or through a software interface. See Section 9 | https://www.unternehmensregister.de/de/so-gehts/uebermitteln |

## Section 2: Reporting Framework

The Third Book of the HGB is built in layers. Read the index at https://www.gesetze-im-internet.de/hgb/ to see them. The First Section ("Vorschriften für alle Kaufleute", §§ 238 to 263) binds every merchant. The Second Section (§§ 264 to 335c) adds rules for companies and for certain partnerships. It does not bind sole merchants or ordinary partnerships.

| Entity type | Applicable rules |
| --- | --- |
| Every merchant (Kaufmann): sole merchants, and OHG and KG with a natural person as personally liable partner | §§ 238 to 263 HGB only. The annual financial statements are the balance sheet and the P&L (§ 242(3) HGB). The HGB asks for no notes, no management report, no audit and no publication from them, special sectors such as banks and insurers aside |
| Kapitalgesellschaften: AG, KGaA, GmbH. The Federal Office of Justice also lists the UG (haftungsbeschränkt) here | §§ 238 to 263 HGB plus §§ 264 to 335c HGB: notes, management report, fixed layouts, size classes, audit, publication |
| OHG and KG in which no personally liable partner is a natural person, directly or through another partnership (for example the GmbH & Co. KG) | § 264a HGB applies the company rules (First to Fifth Subsection of the Second Section) to them. § 264c HGB has special rules for them. § 264b HGB releases them when they are included in consolidated accounts and the other conditions there are met |
| Parent companies (groups) | Consolidated accounts under §§ 290 to 315e HGB. A parent that Article 4 of Regulation (EC) No 1606/2002 obliges to use the international accounting standards adopted by the EU follows those standards (§ 315e(1) HGB). So must a parent for which admission of a security to trading on an organised market in Germany has been applied for by the balance sheet date (§ 315e(2) HGB). Other parents may choose these standards (§ 315e(3) HGB) |
| Individual accounts of any company | HGB accounts are always required. A large company may publish IFRS individual accounts in place of the HGB accounts (§ 325(2a) HGB). The HGB accounts must then still be drawn up, audited and sent to the register for permanent deposit (§ 325(2b) HGB) |
| Sole merchants within both limits of § 241a HGB | Released from commercial-law bookkeeping, the inventory and the annual financial statements (§ 241a, § 242(4) HGB). See the table below |
| Cooperatives, banks, insurers, pension funds | Own sections of the HGB (from § 336, § 340 and § 341). Not covered here |
| Very large sole merchants, partnerships, associations and foundations | The Publizitätsgesetz. See Section 10 |

Sources for this table: https://www.gesetze-im-internet.de/hgb/__242.html and https://www.gesetze-im-internet.de/hgb/__264.html and https://www.gesetze-im-internet.de/hgb/__264a.html and https://www.gesetze-im-internet.de/hgb/__315e.html and https://www.gesetze-im-internet.de/hgb/__325.html

- **Every merchant.** § 242(1) HGB speaks to the merchant ("Der Kaufmann hat zu Beginn seines Handelsgewerbes und für den Schluß eines jeden Geschäftsjahrs"): a balance sheet at the start of the business and at the end of each financial year. § 242(2) HGB adds the P&L.
- **Companies.** § 264(1) HGB speaks to companies only: "Die gesetzlichen Vertreter einer Kapitalgesellschaft haben den Jahresabschluß (§ 242) um einen Anhang zu erweitern".
- **Certain partnerships.** § 264a(1) HGB says the company rules "sind auch anzuwenden auf offene Handelsgesellschaften und Kommanditgesellschaften, bei denen nicht wenigstens ein persönlich haftender Gesellschafter" is a natural person, directly or through a chain of partnerships. Once a natural person joins as personally liable partner, the Federal Office of Justice notes, the publication duty as a rule falls away: https://www.bundesjustizamt.de/DE/Themen/OrdnungsgeldVollstreckung/Jahresabschluesse/Offenlegung/Pflichten/Pflichten_node.html

**Release for sole merchants (Einzelkaufleute)**

| What | Value | Note | Source |
| --- | --- | --- | --- |
| Source | all figures below | https://www.gesetze-im-internet.de/hgb/__241a.html |  |
| Revenue on each of two balance sheet dates in a row: not more than | EUR 800,000 | § 241a HGB: "nicht mehr als jeweils 800 000 Euro Umsatzerlöse" | https://www.gesetze-im-internet.de/hgb/__241a.html |
| Annual net profit (Jahresüberschuss) on each of the same two dates: not more than | EUR 80,000 | § 241a HGB: "jeweils 80 000 Euro Jahresüberschuss" | same |

- **Both limits must be kept**, on the balance sheet dates of two financial years in a row. For a new business the first balance sheet date is enough.
- **Sole merchants only.** Partnerships and companies cannot use the release, whatever their size.
- **What the release covers.** § 241a HGB lifts §§ 238 to 241 HGB (books and inventory). § 242(4) HGB lifts the balance sheet and the P&L.
- **Not the same as the tax rule.** The tax-law bookkeeping duty in § 141 AO uses the same two amounts but joins them with "or", and it starts only after a notice from the tax office. See the German bookkeeping Guide.
- **Start date.** These amounts apply for the first time to financial years that begin after 31 December 2023. See Art. 92 EGHGB at https://www.gesetze-im-internet.de/hgbeg/art_92.html
- **Correction.** Older material says such a sole merchant has "no publication". The release is about keeping books and drawing up statements. An ordinary sole merchant (not a bank or an insurer) has no publication duty under §§ 325 to 329 HGB at any size. Only the Publizitätsgesetz can create one (Section 10).

## Section 3: Size Thresholds

The size class decides the layouts, the notes, the management report, the audit and what is published. The classes are defined in § 267 and § 267a HGB. They apply to companies and, through § 264a HGB, to the partnerships named in Section 2.

**Small and medium-sized companies**

| What | Value | Note | Source |
| --- | --- | --- | --- |
| Source | all figures below | https://www.gesetze-im-internet.de/hgb/__267.html |  |
| Small company (kleine Kapitalgesellschaft): balance sheet total not more than | EUR 7,500,000 | § 267(1) HGB: "7 500 000 Euro Bilanzsumme" | https://www.gesetze-im-internet.de/hgb/__267.html |
| Small company: revenue in the twelve months before the balance sheet date not more than | EUR 15,000,000 | § 267(1) HGB: "15 000 000 Euro Umsatzerlöse in den zwölf Monaten vor dem Abschlußstichtag" | same |
| Small company: yearly average number of staff not more than | fifty employees | § 267(1) HGB prints the number in words: "Im Jahresdurchschnitt fünfzig Arbeitnehmer" | same |
| Medium-sized company (mittelgroße Kapitalgesellschaft): balance sheet total not more than | EUR 25,000,000 | § 267(2) HGB: "25 000 000 Euro Bilanzsumme" | same |
| Medium-sized company: revenue in the twelve months before the balance sheet date not more than | EUR 50,000,000 | § 267(2) HGB: "50 000 000 Euro Umsatzerlöse in den zwölf Monaten vor dem Abschlußstichtag" | same |
| Medium-sized company: yearly average number of staff not more than | two hundred and fifty employees | § 267(2) HGB prints the number in words: "Im Jahresdurchschnitt zweihundertfünfzig Arbeitnehmer" | same |
| Large company (große Kapitalgesellschaft) | goes over at least two of the three medium-sized limits | § 267(3) HGB | same |

**Micro companies (Kleinstkapitalgesellschaften)**

| What | Value | Note | Source |
| --- | --- | --- | --- |
| Source | all figures below | https://www.gesetze-im-internet.de/hgb/__267a.html |  |
| Balance sheet total not more than | EUR 450,000 | § 267a(1) HGB: "450 000 Euro Bilanzsumme" | https://www.gesetze-im-internet.de/hgb/__267a.html |
| Revenue in the twelve months before the balance sheet date not more than | EUR 900,000 | § 267a(1) HGB: "900 000 Euro Umsatzerlöse in den zwölf Monaten vor dem Abschlussstichtag" | same |
| Yearly average number of staff not more than | ten employees | § 267a(1) HGB prints the number in words: "im Jahresdurchschnitt zehn Arbeitnehmer" | same |

- **Size classification rule: two of three.** A company belongs to a class when it does not go over at least two of that class's three limits. A medium-sized company goes over at least two of the small limits and stays within at least two of the medium-sized limits.
- **Two balance sheet dates in a row.** The legal effects of a class start only when its limits are crossed, upwards or downwards, on the balance sheet dates of two financial years in a row (§ 267(4) HGB). So one year over the limits does not by itself change the class. When the limits are crossed on a second balance sheet date in a row, the new class applies to the statements for that second financial year. The statute does not say this in so many words. It follows from its second sentence, under which the effects for a new or converted company start already at the first balance sheet date.
- **New and converted companies.** The first balance sheet date after a new formation or a conversion decides. This shortcut does not apply to a change of legal form when the old entity was already a company or a partnership within § 264a HGB (§ 267(4) HGB).
- **Balance sheet total.** The sum of items A to E of the asset side in § 266(2) HGB. A deficit not covered by equity that is shown on the asset side is left out (§ 267(4a) HGB).
- **Counting employees.** One quarter of the sum of the staff counts on 31 March, 30 June, 30 September and 31 December. Staff abroad count. Apprentices do not (§ 267(5) HGB).
- **Always large.** A capital-market company within § 264d HGB always counts as large. That is a company that uses an organised market through securities it has issued, or that has applied for their admission to trading on one.
- **A micro company is a small company.** The rules for small companies also apply to micro companies unless the law says otherwise (§ 267a(2) HGB).
- **Never micro.** Investment companies, equity participation companies (Unternehmensbeteiligungsgesellschaften) and companies whose only purpose is to buy, manage and sell participations without taking part in their management (§ 267a(3) HGB).
- **Start date.** The amounts above apply for the first time to financial years that begin after 31 December 2023. They may be used for a financial year that begins after 31 December 2022, but then only all together. See Art. 93 EGHGB at https://www.gesetze-im-internet.de/hgbeg/art_93.html
- **Stale official page.** The size note on the Federal Office of Justice page "Offenlegungspflichten" still prints the micro limits that applied before. The statute above is the law.

## Section 4: Required Financial Statements

| Document | Kleinst | Klein | Mittelgroß | Groß |
| --- | --- | --- | --- | --- |
| Bilanz (Balance sheet) | Required. May be cut down to the items marked with letters (§ 266(1) HGB) | Required. May be cut down to the items marked with letters and Roman numerals (§ 266(1) HGB) | Required, full layout. A shorter form may be sent for publication (§ 327 HGB) | Required, full layout |
| GuV (Profit and loss) | Required. A short form with eight lines is allowed (§ 275(5) HGB). Not published | Required. Lines 1 to 5 may be merged into one line "Rohergebnis" (§ 276 HGB). Not published | Required. "Rohergebnis" allowed (§ 276 HGB) | Required, full layout |
| Anhang (Notes) | Not required if the details named in § 264(1) HGB are given under the balance sheet | Required, with the reliefs of § 288(1) HGB | Required, with the reliefs of § 288(2) HGB | Required, in full |
| Lagebericht (Management report) | Not required | Not required (§ 264(1) HGB) | Required | Required |
| Kapitalflussrechnung (Cash flow statement) | Not required | Not required | Not required | Not required because of size. Required only from a capital-market company that does not have to draw up consolidated accounts (§ 264(1) HGB) |
| Eigenkapitalspiegel (Statement of changes in equity) | Not required | Not required | Not required | Same rule as the cash flow statement |

Source for this table: https://www.gesetze-im-internet.de/hgb/__264.html

- **Correction.** Older material says every large company needs a cash flow statement and a statement of changes in equity. The law asks for them in individual accounts only from capital-market companies without consolidated accounts. Consolidated accounts always contain both (§ 297(1) HGB).
- **Correction.** Older material gives medium-sized companies a "full" P&L. They may use the "Rohergebnis" relief of § 276 HGB, like small companies.
- **Sole merchants and ordinary partnerships** draw up a balance sheet and a P&L only (§ 242 HGB).
- **When to draw up.** Companies: in the first three months of the new financial year. Small companies may take longer if that fits an orderly course of business, but no more than six months (§ 264(1) HGB). Other merchants: within the time that fits an orderly course of business (§ 243(3) HGB).
- **Heading details.** Company name, seat, register court and register number must be stated, and also the fact that the company is in liquidation (§ 264(1a) HGB).
- **Signature.** The merchant signs and dates the statements. If there are several personally liable partners, all sign. See § 245 HGB at https://www.gesetze-im-internet.de/hgb/__245.html
- **Adoption (Feststellung) in a GmbH.** The shareholders decide on adoption and on the use of the result within the first eight months of the financial year, or the first eleven months in a small company. The articles cannot extend this. See § 42a(2) GmbHG at https://www.gesetze-im-internet.de/gmbhg/__42a.html
- **AG.** The general meeting that receives the adopted statements takes place in the first eight months of the financial year. See § 175(1) AktG at https://www.gesetze-im-internet.de/aktg/__175.html
- **True and fair view.** Company accounts must give a true and fair view within the accepted accounting principles. If special circumstances prevent that, extra details go into the notes (§ 264(2) HGB).

## Section 5: Year-End Adjustments Checklist

Most rules in this table come from the First Section and bind every merchant. § 274 HGB and the references to § 266, § 275 and § 277 HGB bind companies and the partnerships within § 264a HGB only. Sources: https://www.gesetze-im-internet.de/hgb/__249.html and https://www.gesetze-im-internet.de/hgb/__250.html and https://www.gesetze-im-internet.de/hgb/__252.html and https://www.gesetze-im-internet.de/hgb/__253.html and https://www.gesetze-im-internet.de/hgb/__256.html and https://www.gesetze-im-internet.de/hgb/__256a.html and https://www.gesetze-im-internet.de/hgb/__274.html

| # | Adjustment | Germany-specific notes |
| --- | --- | --- |
| 1 | Depreciation (planmäßige Abschreibungen) | § 253(3) HGB. Fixed assets with a limited useful life are written down by plan. The plan must spread the cost over the financial years in which the asset can be expected to be used. The HGB names no method and no rates, and it does not mention the tax depreciation tables (AfA-Tabellen). If, in exceptional cases, the useful life of a self-created intangible fixed asset or of purchased goodwill cannot be estimated reliably, the period is ten years |
| 2 | Accruals (Rückstellungen) | § 249 HGB. Required for uncertain liabilities and for expected losses from pending transactions. Also required for maintenance left undone in the year and made up within three months of the next year, for overburden removal made up in the next year, and for warranty work done without a legal duty. Provisions for any other purpose are forbidden. A provision is released only when its reason has gone. Amount: the settlement amount needed by reasonable commercial judgement (§ 253(1) HGB). If the remaining term is over one year, discount at the average market rate of the past seven financial years that matches the remaining term (§ 253(2) HGB). Tax law differs: it allows no provision for expected losses from pending transactions, apart from the case named in § 5(4a) sentence 2 EStG |
| 3 | Prepayments (RAP) | § 250 HGB. Rechnungsabgrenzungsposten on both sides: payments made before the balance sheet date that are expense for a fixed time after it (asset side), and payments received before it that are income for a fixed time after it (liability side). If the settlement amount of a liability is higher than the amount paid out, the difference may be put on the asset side. It is then written off by planned yearly amounts, which may be spread over the whole term (§ 250(3) HGB) |
| 4 | Provisions for pensions | § 253(1) and (2) HGB. Settlement amount, discounted at the average market rate of the past ten financial years that matches the remaining term. A flat remaining term of 15 years may be assumed instead. The Bundesbank works out the rates and publishes them monthly: https://www.bundesbank.de/de/statistiken/geld-und-kapitalmaerkte/zinssaetze-und-renditen/abzinsungszinssaetze/abzinsungszinssaetze-772396 The difference between the ten-year and the seven-year valuation must be worked out every year and shown in the notes or under the balance sheet. Profits may be paid out only if the freely available reserves left after the payout, plus a profit carried forward and minus a loss carried forward, at least equal this difference (§ 253(6) HGB) |
| 5 | Bad debts (Wertberichtigung) | § 253(4) HGB. Current assets must be written down to the lower value at the balance sheet date (lower-of-cost-or-market rule). Each asset is valued on its own and with prudence (§ 252(1) nos. 3 and 4 HGB). The HGB text does not name individual or general allowances; older material lists both |
| 6 | Inventory (Vorräte) | § 253(4) HGB: the lower value that follows from a stock exchange or market price, or else the lower attributable value. § 256 HGB allows the first-in-first-out or the last-in-first-out assumption for similar inventory items where that fits accepted accounting principles. § 240(3) and (4) HGB allow a fixed value and a weighted average for groups. A lower value may not be kept once its reasons have gone (§ 253(5) HGB) |
| 7 | Deferred tax (latente Steuern) | § 274 HGB, companies and the partnerships within § 264a HGB only. Differences between commercial and tax values that are expected to reverse. A net tax burden must be shown as a deferred tax liability. A net tax relief may be shown as a deferred tax asset. Both may be shown without netting. Tax loss carry-forwards count only as far as they are expected to be used within the next five years. Measured at the company's own tax rates at the time of reversal, not discounted. Differences from the minimum tax laws are ignored (§ 274(3) HGB). Small companies are exempt from § 274 HGB altogether (§ 274a no. 4 HGB). Older material calls this an "option" |
| 8 | Foreign currency | § 256a HGB. Assets and liabilities in foreign currency are translated at the mid spot rate on the balance sheet date. For a remaining term of one year or less, the cost ceiling (§ 253(1) HGB) and the realisation rule (§ 252(1) no. 4 HGB) are not applied. For longer terms both still apply. Translation income is shown separately under other operating income, translation expense under other operating expenses (§ 277(5) HGB) |
| 9 | Impairment (außerplanmäßige Abschreibungen) | § 253(3) sentences 5 and 6 HGB. Fixed assets: a write-down is required when the loss in value is expected to be permanent. When it is not expected to be permanent, a write-down is allowed for financial assets only. Current assets: see rows 5 and 6. The write-down is reversed when its reasons have gone, except for purchased goodwill (§ 253(5) HGB). Companies show these write-downs separately or in the notes (§ 277(3) HGB) |
| 10 | Anniversary provisions (Jubiläumsrückstellungen) | The HGB has no special rule. The general rule for uncertain liabilities applies (§ 249(1) HGB). Tax law limits them: the employment must have lasted at least ten years, the anniversary must need at least 15 years of service, the promise must be in writing, and only rights earned after 31 December 1992 count. See § 5(4) EStG at https://www.gesetze-im-internet.de/estg/__5.html |
| 11 | Tax provisions | Provisions for Gewerbesteuer and Körperschaftsteuer. Shown as "Steuerrückstellungen" (§ 266(3) B.2 HGB). The expense goes to the line "Steuern vom Einkommen und vom Ertrag" (§ 275(2) no. 14 HGB) |
| 12 | Construction contracts | § 252(1) no. 4 HGB: profits count only when they are realised at the balance sheet date. The HGB has no percentage-of-completion rule. Unfinished work is carried under inventories as "unfertige Erzeugnisse, unfertige Leistungen" (§ 266(2) B.I.2 HGB) |

- **Correction.** Older material says a write-down for a loss in value that is not permanent is "optional" for fixed assets in general. The law allows it for financial assets only.
- **Clarification.** Older material says unrealised currency gains are "limited to 1 year". The law puts it this way: for items with a remaining term of one year or less, the cost ceiling and the realisation rule are switched off.
- **Micro companies and fair value.** A micro company may measure at fair value only if it uses none of the micro reliefs (notes, short balance sheet, short P&L, deposit). If it uses even one, assets are measured at cost less write-downs (§ 253(1) HGB).
- **Consistency.** The methods used in last year's statements must be kept (§ 246(3), § 252(1) no. 6 HGB). A change is allowed only in justified exceptional cases (§ 252(2) HGB).

## Section 6: Profit and Loss Account Format (GuV)

§ 275 HGB binds companies and the partnerships within § 264a HGB. The P&L is drawn up in vertical form (Staffelform), either by the total cost method (Gesamtkostenverfahren, by nature of expense) or by the cost of sales method (Umsatzkostenverfahren). The lines must be shown separately and in the order given. The lines below follow § 275(2) and (3) HGB as they read now: https://www.gesetze-im-internet.de/hgb/__275.html

~~~
GEWINN- UND VERLUSTRECHNUNG, Gesamtkostenverfahren (§ 275(2) HGB)

 1. Umsatzerlöse (Revenue)
 2. Erhöhung oder Verminderung des Bestands an fertigen und unfertigen
    Erzeugnissen (Change in finished goods and work in progress)
 3. andere aktivierte Eigenleistungen (Own work capitalised)
 4. sonstige betriebliche Erträge (Other operating income)
 5. Materialaufwand (Cost of materials):
    a) Aufwendungen für Roh-, Hilfs- und Betriebsstoffe und für bezogene Waren
    b) Aufwendungen für bezogene Leistungen
 6. Personalaufwand (Personnel expenses):
    a) Löhne und Gehälter
    b) soziale Abgaben und Aufwendungen für Altersversorgung und für
       Unterstützung, davon für Altersversorgung
 7. Abschreibungen (Depreciation, amortisation and write-downs):
    a) auf immaterielle Vermögensgegenstände des Anlagevermögens und Sachanlagen
    b) auf Vermögensgegenstände des Umlaufvermögens, soweit diese die in der
       Kapitalgesellschaft üblichen Abschreibungen überschreiten
 8. sonstige betriebliche Aufwendungen (Other operating expenses)
 9. Erträge aus Beteiligungen, davon aus verbundenen Unternehmen
    (Income from participations)
10. Erträge aus anderen Wertpapieren und Ausleihungen des
    Finanzanlagevermögens, davon aus verbundenen Unternehmen
11. sonstige Zinsen und ähnliche Erträge, davon aus verbundenen Unternehmen
    (Other interest and similar income)
12. Abschreibungen auf Finanzanlagen und auf Wertpapiere des Umlaufvermögens
    (Write-downs on financial assets and on securities held as current assets)
13. Zinsen und ähnliche Aufwendungen, davon an verbundene Unternehmen
    (Interest and similar expenses)
14. Steuern vom Einkommen und vom Ertrag (Taxes on income)
15. Ergebnis nach Steuern (Result after taxes)
16. sonstige Steuern (Other taxes)
17. Jahresüberschuss/Jahresfehlbetrag (Net profit or net loss for the year)
~~~

~~~
GEWINN- UND VERLUSTRECHNUNG, Umsatzkostenverfahren (§ 275(3) HGB)

 1. Umsatzerlöse (Revenue)
 2. Herstellungskosten der zur Erzielung der Umsatzerlöse erbrachten
    Leistungen (Cost of sales)
 3. Bruttoergebnis vom Umsatz (Gross profit)
 4. Vertriebskosten (Selling costs)
 5. allgemeine Verwaltungskosten (General administrative costs)
 6. sonstige betriebliche Erträge (Other operating income)
 7. sonstige betriebliche Aufwendungen (Other operating expenses)
 8. Erträge aus Beteiligungen, davon aus verbundenen Unternehmen
 9. Erträge aus anderen Wertpapieren und Ausleihungen des
    Finanzanlagevermögens, davon aus verbundenen Unternehmen
10. sonstige Zinsen und ähnliche Erträge, davon aus verbundenen Unternehmen
11. Abschreibungen auf Finanzanlagen und auf Wertpapiere des Umlaufvermögens
12. Zinsen und ähnliche Aufwendungen, davon an verbundene Unternehmen
13. Steuern vom Einkommen und vom Ertrag (Taxes on income)
14. Ergebnis nach Steuern (Result after taxes)
15. sonstige Steuern (Other taxes)
16. Jahresüberschuss/Jahresfehlbetrag (Net profit or net loss for the year)
~~~

- **Subtotals.** Older material shows lines called "Betriebsergebnis" and "Finanzergebnis". They are not statutory lines. New items and subtotals may be added only if their content is not covered by a prescribed item. See § 265(5) HGB at https://www.gesetze-im-internet.de/hgb/__265.html
- **No extraordinary items.** The law has no line for an extraordinary result and no line "Ergebnis der gewöhnlichen Geschäftstätigkeit". Income and expenses of unusual size or importance are explained in the notes (§ 285 no. 31 HGB).
- **Changes in reserves** may be shown only after the line "Jahresüberschuss/Jahresfehlbetrag" (§ 275(4) HGB).
- **Micro companies** may use eight lines instead: Umsatzerlöse, sonstige Erträge, Materialaufwand, Personalaufwand, Abschreibungen, sonstige Aufwendungen, Steuern, Jahresüberschuss/Jahresfehlbetrag (§ 275(5) HGB).
- **Small and medium-sized companies** may merge lines 1 to 5 of the total cost method, or lines 1 to 3 and 6 of the cost of sales method, into one line "Rohergebnis". A micro company that uses the eight-line form cannot also use this relief. See https://www.gesetze-im-internet.de/hgb/__276.html
- **Revenue** means income from selling, renting or leasing products and from services, after sales deductions, VAT and other taxes directly tied to the sale. See § 277(1) HGB at https://www.gesetze-im-internet.de/hgb/__277.html
- **Cost of sales method.** The notes must then give the cost of materials and the personnel expenses of the year (§ 285 no. 8 HGB). Small companies need not.
- **Sole merchants and ordinary partnerships** are not bound by § 275 HGB. Their P&L sets the expenses of the year against the income of the year (§ 242(2) HGB) and must be clear and orderly (§ 243(2) HGB).

## Section 7: Balance Sheet Format (Bilanz)

§ 266 HGB binds companies and the partnerships within § 264a HGB. The balance sheet is drawn up in account form (Kontoform): assets on one side, equity and liabilities on the other. Medium-sized and large companies show every item below, separately and in this order. See https://www.gesetze-im-internet.de/hgb/__266.html

The block lists the two sides one after the other so that it stays readable.

~~~
AKTIVSEITE (Assets), § 266(2) HGB

A. Anlagevermögen (Fixed assets)
   I.   Immaterielle Vermögensgegenstände (Intangible assets)
        1. Selbst geschaffene gewerbliche Schutzrechte und ähnliche Rechte und Werte
        2. entgeltlich erworbene Konzessionen, gewerbliche Schutzrechte und ähnliche
           Rechte und Werte sowie Lizenzen an solchen Rechten und Werten
        3. Geschäfts- oder Firmenwert
        4. geleistete Anzahlungen
   II.  Sachanlagen (Tangible assets)
        1. Grundstücke, grundstücksgleiche Rechte und Bauten einschließlich der
           Bauten auf fremden Grundstücken
        2. technische Anlagen und Maschinen
        3. andere Anlagen, Betriebs- und Geschäftsausstattung
        4. geleistete Anzahlungen und Anlagen im Bau
   III. Finanzanlagen (Financial assets)
        1. Anteile an verbundenen Unternehmen
        2. Ausleihungen an verbundene Unternehmen
        3. Beteiligungen
        4. Ausleihungen an Unternehmen, mit denen ein Beteiligungsverhältnis besteht
        5. Wertpapiere des Anlagevermögens
        6. sonstige Ausleihungen
B. Umlaufvermögen (Current assets)
   I.   Vorräte (Inventories)
        1. Roh-, Hilfs- und Betriebsstoffe
        2. unfertige Erzeugnisse, unfertige Leistungen
        3. fertige Erzeugnisse und Waren
        4. geleistete Anzahlungen
   II.  Forderungen und sonstige Vermögensgegenstände (Receivables and other assets)
        1. Forderungen aus Lieferungen und Leistungen
        2. Forderungen gegen verbundene Unternehmen
        3. Forderungen gegen Unternehmen, mit denen ein Beteiligungsverhältnis besteht
        4. sonstige Vermögensgegenstände
   III. Wertpapiere (Securities)
        1. Anteile an verbundenen Unternehmen
        2. sonstige Wertpapiere
   IV.  Kassenbestand, Bundesbankguthaben, Guthaben bei Kreditinstituten und Schecks
C. Rechnungsabgrenzungsposten (Prepaid expenses)
D. Aktive latente Steuern (Deferred tax assets)
E. Aktiver Unterschiedsbetrag aus der Vermögensverrechnung

PASSIVSEITE (Equity and liabilities), § 266(3) HGB

A. Eigenkapital (Equity)
   I.   Gezeichnetes Kapital (Subscribed capital)
   II.  Kapitalrücklage (Capital reserve)
   III. Gewinnrücklagen (Revenue reserves)
        1. gesetzliche Rücklage
        2. Rücklage für Anteile an einem herrschenden oder mehrheitlich
           beteiligten Unternehmen
        3. satzungsmäßige Rücklagen
        4. andere Gewinnrücklagen
   IV.  Gewinnvortrag/Verlustvortrag (Profit or loss carried forward)
   V.   Jahresüberschuß/Jahresfehlbetrag (Net profit or net loss for the year)
B. Rückstellungen (Provisions)
        1. Rückstellungen für Pensionen und ähnliche Verpflichtungen
        2. Steuerrückstellungen
        3. sonstige Rückstellungen
C. Verbindlichkeiten (Liabilities)
        1. Anleihen, davon konvertibel
        2. Verbindlichkeiten gegenüber Kreditinstituten
        3. erhaltene Anzahlungen auf Bestellungen
        4. Verbindlichkeiten aus Lieferungen und Leistungen
        5. Verbindlichkeiten aus der Annahme gezogener Wechsel und der
           Ausstellung eigener Wechsel
        6. Verbindlichkeiten gegenüber verbundenen Unternehmen
        7. Verbindlichkeiten gegenüber Unternehmen, mit denen ein
           Beteiligungsverhältnis besteht
        8. sonstige Verbindlichkeiten, davon aus Steuern, davon im Rahmen der
           sozialen Sicherheit
D. Rechnungsabgrenzungsposten (Deferred income)
E. Passive latente Steuern (Deferred tax liabilities)
~~~

- **Correction.** Older material offers a choice between account form and vertical form (Staffelform) for the balance sheet. § 266(1) HGB prescribes the account form. The vertical form belongs to the P&L (§ 275(1) HGB).
- **Small companies** need show only the items marked with letters and Roman numerals. **Micro companies** need show only the items marked with letters (§ 266(1) HGB).
- **Balance sheet after use of the result.** If the balance sheet takes account of a partial use of the year's result, the item "Bilanzgewinn/Bilanzverlust" replaces items IV and V of equity. See § 268(1) HGB at https://www.gesetze-im-internet.de/hgb/__268.html
- **Equity used up by losses.** The excess of liabilities over assets is shown at the end of the asset side as "Nicht durch Eigenkapital gedeckter Fehlbetrag" (§ 268(3) HGB).
- **Remaining terms.** Receivables due after more than one year are noted at each item. For each liability item, the amount due within one year and the amount due after more than one year are noted (§ 268(4) and (5) HGB).
- **Sole merchants and ordinary partnerships** are not bound by § 266 HGB. Their balance sheet shows fixed assets, current assets, equity, debts and prepaid or deferred items separately and broken down far enough. See § 247(1) HGB at https://www.gesetze-im-internet.de/hgb/__247.html

## Section 8: Notes to Accounts (Anhang)

The notes are part of the annual financial statements of a company (§ 264(1) HGB). The numbers in the table are the numbers of § 285 HGB. The reliefs by size are in § 288 HGB. See https://www.gesetze-im-internet.de/hgb/__284.html and https://www.gesetze-im-internet.de/hgb/__285.html and https://www.gesetze-im-internet.de/hgb/__288.html

| # | Disclosure | Klein | Mittelgroß | Groß |
| --- | --- | --- | --- | --- |
| 1 | Accounting policies (§ 284(2) no. 1 HGB) | Required | Required | Required |
| 2 | Fixed asset movements (Anlagenspiegel, § 284(3) HGB) | Not required (§ 288(1) HGB) | Required | Required |
| 3 | Maturity analysis of liabilities | Total of liabilities with a remaining term of more than five years (no. 1 letter a). No split by item | Total, and the split by liability item (no. 2). The split may be left out of the published notes (§ 327 HGB) | Total and split by item |
| 4 | Secured liabilities | Total secured amount, with kind and form of the security (no. 1 letter b). No split by item | Total and split by item (no. 2) | Total and split by item |
| 5 | Related party transactions (no. 21) | Not required | Only transactions made directly or indirectly with a shareholder, with enterprises in which the company itself holds a participation, or with members of the management, supervisory or administrative body (§ 288(2) HGB) | Required |
| 6 | Employee numbers (no. 7) | Average number only, no split by groups | Average number, split by groups | Average number, split by groups |
| 7 | Directors' and supervisory board remuneration (no. 9 letter a and letter b) | Not required | Required | Required |
| 8 | Contingent liabilities (Haftungsverhältnisse, § 251 and § 268(7) HGB) | Required | Required | Required |
| 9 | Off-balance sheet arrangements (no. 3) | Not required | Required | Required |
| 10 | Auditor fees (no. 17) | Not required | May be left out. The company must then send the details to the Wirtschaftsprüferkammer on its written request (§ 288(2) HGB) | Required, unless they are given in consolidated accounts that include the company |
| 11 | Subsidiaries/investments (no. 11) | Not required (§ 288(1) HGB lists nos. 10 to 12) | Required: name and seat, share of capital, equity and result of the last financial year | Required: the same |
| 12 | Deferred tax explanation (no. 29) | Not required | Not required (§ 288(2) HGB). If deferred tax liabilities are shown on the balance sheet, the deferred tax balances at year end and their changes in the year are still required (no. 30) | Required |
| 13 | Events of special importance after the end of the financial year (no. 33) | Not required | Required | Required |
| 14 | Proposal or resolution on the use of the result (no. 34) | Not required | Required | Required |

- **Corrections.** Older material says a small company must disclose its shareholdings, that a medium-sized company need not report related party transactions at all, and that a medium-sized company must explain its deferred taxes. § 288 HGB says otherwise in all three cases. It also says a small company need not "file" the fixed asset movements: the small company need not draw them up at all.
- **Related party transactions: what counts.** At least the material transactions that were not made at normal market terms, with the kind of relationship and the value. Transactions with and between wholly owned companies included in consolidated accounts are left out (§ 285 no. 21 HGB).
- **Directors' pay.** Companies that are not listed AGs may leave out the totals of no. 9 letter a and letter b if the pay of a single member could be worked out from them. See § 286(4) HGB at https://www.gesetze-im-internet.de/hgb/__286.html
- **Loans to directors.** Advances and loans to board members, with interest rates and main terms, must be given by companies of every size (§ 285 no. 9 letter c HGB).
- **Shareholdings.** The details may be left out if they are of minor importance or could cause considerable harm (§ 286(3) HGB). The second reason is closed when the company or one of its subsidiaries is a capital-market company.
- **Other financial commitments** that are not on the balance sheet are given as a total by companies of every size if they matter for judging the financial position (§ 285 no. 3a HGB).
- **Micro companies without notes** give three things under the balance sheet: the contingent liabilities of § 268(7) HGB, the advances and loans to board members of § 285 no. 9 letter c HGB and, for an AG, the details named in § 160(3) sentence 2 AktG (§ 264(1) HGB).
- **Published notes.** A small company's published notes need not contain the details about the P&L (§ 326(1) HGB). A medium-sized company may publish its notes without nos. 2, 8 letter a and 12 of § 285 HGB (§ 327 HGB).

## Section 9: Filing Requirements

| Item | Detail |
| --- | --- |
| Who must publish | The members of the representative body of a company, for the company (§ 325(1) HGB). The same holds for the partnerships within § 264a HGB. Small companies, companies with no business activity, and companies in liquidation or insolvency must publish too, until the company is deleted from the commercial register |
| Filing authority | The body that keeps the company register (Unternehmensregister). The Federal Office of Justice names the Bundesanzeiger Verlag GmbH in Cologne as that body |
| Method | Electronic only, in German. Orders go through the publication platform (publikations-plattform.de) or a software interface (web service). The decisive file format is XML. Issuers of securities use the European single electronic format (XHTML). PDF and Office files are accepted and converted for a charge. Paper is not accepted. The person who sends the documents must first be identified electronically |
| Filing deadline | At the latest one year after the balance sheet date of the financial year (§ 325(1a) HGB). At the latest four months for a capital-market company within § 264d HGB (§ 325(4) HGB). The moment of transmission counts. The deadline cannot be extended, and an extension granted by the tax office for the tax return does not help |
| What must be ready | The adopted statements and, where an audit is required, the audit opinion. Since financial years that began after 31 December 2015, statements that are not yet adopted or not yet audited can no longer be sent just to keep the deadline |
| Operator verification | The register body checks whether the documents arrived in time and in full (§ 329(1) HGB). If it doubts a size relief, it may ask for revenue and the average number of employees. If the company does not answer in time, the relief counts as wrongly used (§ 329(2) HGB) |
| Enforcement | The register body reports missing or incomplete documents to the Bundesamt für Justiz (BfJ), which must open an Ordnungsgeldverfahren under § 335 HGB |
| Content breaches | Breaches of the rules on form and content of the statements are a separate administrative offence. The fine can reach fifty thousand euros; the law prints the amount in words. Capital-market companies face higher maximums, and for them the authority is the Bundesanstalt für Finanzdienstleistungsaufsicht. In the other cases of § 334(1) HGB it is the Bundesamt für Justiz (§ 334(4) HGB). See § 334 HGB at https://www.gesetze-im-internet.de/hgb/__334.html |

Sources for this table: https://www.gesetze-im-internet.de/hgb/__325.html and https://www.gesetze-im-internet.de/hgb/__329.html and https://www.unternehmensregister.de/de/so-gehts/uebermitteln and https://www.bundesjustizamt.de/DE/Themen/OrdnungsgeldVollstreckung/Jahresabschluesse/Offenlegung/Pflichten/Pflichten_node.html and https://www.bundesjustizamt.de/DE/Themen/OrdnungsgeldVollstreckung/Jahresabschluesse/Offenlegung/Aktuelles/Aktuelles_node.html and https://www.bundesjustizamt.de/DE/Themen/OrdnungsgeldVollstreckung/Jahresabschluesse/Offenlegung/Fragen/Fragen_node.html

**The fine for not publishing: as the Federal Office of Justice prints it**

| What | Value | Note | Source |
| --- | --- | --- | --- |
| Source | all figures below | https://www.bundesjustizamt.de/DE/Themen/OrdnungsgeldVollstreckung/Jahresabschluesse/Offenlegung/Verfahren/Verfahren_node.html |  |
| Minimum penalty in the normal case | EUR 2,500 | "Das Ordnungsgeld beträgt im Regelfall mindestens 2.500 Euro und höchstens 25.000 Euro" | https://www.bundesjustizamt.de/DE/Themen/OrdnungsgeldVollstreckung/Jahresabschluesse/Offenlegung/Verfahren/Verfahren_node.html |
| Maximum penalty in the normal case, per fine | EUR 25,000 | Same sentence. § 335(1) HGB prints both amounts in words | same |
| Fee for the procedure, charged with the first threat notice | EUR 100 | "100 Euro Gebühr nach Nr. 1210 des Kostenverzeichnisses des Justizverwaltungskostengesetzes" | https://www.bundesjustizamt.de/DE/Themen/OrdnungsgeldVollstreckung/Jahresabschluesse/Offenlegung/Verfahren/Verfahren_node.html |
| Delivery costs, charged on top | EUR 3.50 | "zuzüglich 3,50 Euro Auslagen für die Zustellung" | same |

**Reduced fine when the duty is met late: the statute**

| What | Value | Note | Source |
| --- | --- | --- | --- |
| Source | all figures below | https://www.gesetze-im-internet.de/hgb/__335.html |  |
| The company used the micro company right to deposit its balance sheet (§ 326(2) HGB) | EUR 500 | § 335(4) no. 1 HGB: "auf einen Betrag von 500 Euro, wenn die Beteiligten von dem Recht einer Kleinstkapitalgesellschaft" | https://www.gesetze-im-internet.de/hgb/__335.html |
| The company is a small company (§ 267(1) HGB) | EUR 1,000 | § 335(4) no. 2 HGB: "auf einen Betrag von 1 000 Euro, wenn es sich um eine kleine Kapitalgesellschaft" | same |
| Any other company, if a higher fine had been threatened | EUR 2,500 | § 335(4) no. 3 HGB: "auf einen Betrag von 2 500 Euro, wenn ein höheres Ordnungsgeld angedroht worden ist" | same |

**Further fee when another fine is set: the cost schedule**

| What | Value | Note | Source |
| --- | --- | --- | --- |
| Source | all figures below | https://www.gesetze-im-internet.de/jvkostg/anlage.html |  |
| Fee for setting a second and each further fine (no. 1211 of the cost schedule of the Justizverwaltungskostengesetz) | EUR 100 | "jedes weiteren Ordnungsgelds jeweils .......... 100,00 €" | https://www.gesetze-im-internet.de/jvkostg/anlage.html |

- **Each person separately.** If the procedure runs against several persons, the fees arise for each person on their own (preliminary note 1.2.1 of the same cost schedule).

- **How the procedure runs.** The BfJ sends a threat notice (Androhungsverfügung). It names a fine and gives six weeks from receipt to publish or to justify the failure by an objection (Einspruch). If the documents are published in full and in proper form within the six weeks, the procedure is closed and no fine is set. The procedure costs are charged with this first notice and stay due even then.
- **Not a one-off.** If the six weeks pass without publication or a justified objection, the fine is set and a new fine is threatened at once. This repeats until the documents are published. The BfJ states that the fine is as a rule raised step by step.
- **Who is fined.** The members of the representative body, or the company itself (§ 335(1) HGB). It is no defence that the statements are not yet drawn up or that the audit has not been ordered. For a partnership within § 264a HGB the fine rules apply through § 335b HGB. The procedure is then directed against the personally liable partners or the members of their representative bodies, and it can also be directed against the partnership itself. See https://www.gesetze-im-internet.de/hgb/__335b.html
- **When the reduced amounts apply.** Only when the duty is met after the six-week period has passed. The BfJ counts only what happened before its decision on the fine. If the six weeks were missed only slightly, the fine falls to a lower amount still (§ 335(4) no. 4 HGB). The minimum in the first table cannot be undercut in any other case.
- **Same number, two rules.** The minimum penalty in the first table is the normal minimum fine. The same amount appears in the second table as the reduced fine for medium-sized and large companies.
- **Objection.** It does not suspend anything. If it fails and the six weeks have passed, publishing later no longer stops the fine.
- **Missed the six weeks through no fault.** Reinstatement can be requested in writing within two weeks after the obstacle has gone, and the missed act must be made up within six weeks (§ 335(5) HGB). The fault of a representative counts as the fault of the person represented. If within one year after the six weeks ended neither reinstatement was requested nor the missed act made up, reinstatement can no longer be granted.
- **Complaint (Beschwerde).** Within two weeks of delivery of the decision, lodged with the BfJ. If the BfJ does not give way, the Landgericht Bonn decides.
- **Capital-market companies** face much higher maximum fines. See § 335(1a) HGB.
- **Using a tax adviser is not enough.** The BfJ states that handing the documents to a Steuerberater in time does not meet the duty. The managers must check that publication really took place.

### What must be filed (Offenlegung) by size

| Size | Documents to disclose |
| --- | --- |
| Kleinst (Micro) | Balance sheet only, with the details under it where there are no notes. The company may ask for permanent deposit (Hinterlegung) in the company register instead of publication. To use this right it must tell the register body that it stays within two of the three micro limits on the balance sheet dates that count (§ 326(2) HGB). A deposited balance sheet is not open to free inspection: third parties get a copy on request only (§ 9(6) HGB), and the BfJ adds that this needs registration and a fee |
| Klein (Small) | Balance sheet and notes. The notes need not contain the details about the P&L. No P&L and no management report (§ 326(1) HGB) |
| Mittelgroß (Medium) | Adopted statements (balance sheet, P&L, notes), management report, and the audit opinion or the note that it was refused. Where they exist: the supervisory board's report and the resolution on the use of the result. The balance sheet may be sent in the small-company form with the extra items listed in § 327 HGB. The notes may leave out nos. 2, 8 letter a and 12 of § 285 HGB |
| Groß (Large) | Everything named in § 325(1) HGB, in full: adopted statements, management report, audit opinion or refusal note, supervisory board report and, for listed companies, the declaration under § 161 AktG |

Sources for this table: https://www.gesetze-im-internet.de/hgb/__326.html and https://www.gesetze-im-internet.de/hgb/__327.html and https://www.gesetze-im-internet.de/hgb/__9.html and https://www.bundesjustizamt.de/DE/Themen/OrdnungsgeldVollstreckung/Jahresabschluesse/Verstoesse/InhaltJahresabschluss/Bestandteile/Bestandteile_node.html

- **Correction.** Older material lists the "Prüfungsbericht" among the documents a large company publishes. What is published is the audit opinion (Bestätigungsvermerk), in its full wording. The long audit report goes to the company's management or supervisory board. See § 321(5) HGB at https://www.gesetze-im-internet.de/hgb/__321.html and § 328(1a) HGB at https://www.gesetze-im-internet.de/hgb/__328.html
- **Correction.** Older material leaves the audit opinion out of the medium-sized row. Medium-sized companies are audited, so they publish it too.
- **Date of adoption.** The published statements must state the date on which they were adopted (§ 328(1a) HGB).
- **Use of the result.** If the statements contain only the proposal, the resolution is published once it exists (§ 325(1b) HGB). Later changes to the statements are published as well.
- **What may follow later.** The supervisory board's report and the declaration under § 161 AktG must be published without delay once they exist, if they were not ready within the deadline (§ 325(1a) HGB). The statements and the management report may not follow later.
- **Subsidiaries.** A subsidiary that is not a capital-market company and is included in the consolidated accounts of a parent in the EU or EEA need not apply the rules on statements, audit and publication if all the conditions of § 264(3) HGB are met. These include the consent of all shareholders for the year and the parent's declaration that it will stand in for the subsidiary's obligations. If one condition is missing, the duty stays. The rules for all merchants (§§ 238 to 263 HGB) are not lifted.
- **German branch of a foreign company.** It publishes the accounting documents of its head office, not German-law statements. See § 325a HGB at https://www.gesetze-im-internet.de/hgb/__325a.html
- **Start of the register rule.** Sending the documents to the company register applies for the first time to financial years that begin after 31 December 2021. Statements for earlier years still go to the operator of the Bundesanzeiger. See Art. 88 EGHGB at https://www.gesetze-im-internet.de/hgbeg/art_88.html

## Section 10: Audit Requirements

| Category | Audit requirement |
| --- | --- |
| Kleinstkapitalgesellschaft (Micro) | Exempt. A micro company is a small company (§ 267a HGB) |
| Kleine Kapitalgesellschaft (Small) | Exempt (§ 316(1) HGB) |
| Mittelgroße Kapitalgesellschaft (Medium) | Mandatory statutory audit (Jahresabschlussprüfung) of the statements and the management report. Without the audit the statements cannot be adopted (§ 316(1) HGB) |
| Große Kapitalgesellschaft (Large) | Mandatory statutory audit |
| Partnerships within § 264a HGB | As for companies of the same size |
| Capital-market companies (kapitalmarktorientiert, § 264d HGB) | Mandatory. They always count as large and are public-interest entities (§ 316a HGB), so the EU audit regulation applies on top. The auditor oversight body (Abschlussprüferaufsichtsstelle; older material calls it APAS) inspects the auditors of public-interest entities. See § 66a(6) WPO at https://www.gesetze-im-internet.de/wipro/__66a.html |
| Consolidated accounts | Mandatory (§ 316(2) HGB) |
| PublG companies (exceed PublG thresholds) | Mandatory (§ 6(1) PublG). See below |

Source for this table: https://www.gesetze-im-internet.de/hgb/__316.html

- **Choosing the auditor.** The shareholders elect the auditor. In a GmbH and in a partnership within § 264a HGB the articles may say otherwise. The auditor should be elected before the end of the financial year to be audited. The engagement letter follows without delay. See § 318(1) HGB at https://www.gesetze-im-internet.de/hgb/__318.html
- **Changes after the audit.** If the statements or the management report are changed after the audit report was handed over, the auditor must audit the change (§ 316(3) HGB).
- **Exempt subsidiaries.** A subsidiary that meets all the conditions of § 264(3) HGB need not apply the audit rules.

### PublG Thresholds (Publizitätsgesetz)

| What | Value | Note | Source |
| --- | --- | --- | --- |
| Source | all figures below | https://www.gesetze-im-internet.de/publg/__1.html |  |
| Balance sheet total at the balance sheet date: more than | EUR 65 million | § 1(1) no. 1 PublG: "übersteigt 65 Millionen Euro" | https://www.gesetze-im-internet.de/publg/__1.html |
| Revenue in the twelve months before the balance sheet date: more than | EUR 130 million | § 1(1) no. 2 PublG: "übersteigen 130 Millionen Euro" | same |
| Average number of staff in the twelve months before the balance sheet date: more than | five thousand employees | § 1(1) no. 3 PublG prints the number in words: "durchschnittlich mehr als fünftausend Arbeitnehmer" | same |

- **PublG applicability thresholds: two of three, three dates in a row.** The enterprise must meet at least two of the three tests at a balance sheet date and at the two balance sheet dates that follow. It must then account under the PublG for the first time for the third of these dates. See § 2(1) PublG at https://www.gesetze-im-internet.de/publg/__2.html
- **Who is covered.** Only these legal forms: partnerships for which no statements under § 264a or § 264b HGB are drawn up, sole merchants, associations whose purpose is a commercial business, foundations under civil law that run a trade, and public-law bodies that are merchants. See § 3(1) PublG at https://www.gesetze-im-internet.de/publg/__3.html
- **Who is not.** Cooperatives, banks, insurers, certain municipal undertakings, collecting societies and enterprises in winding-up (§ 3(2) and (3) PublG). Companies (GmbH, AG, KGaA) are not on the list in § 3(1) PublG; they follow the HGB size classes.
- **Correction.** Older material says the PublG applies to "all enterprises". It applies only to the legal forms above.
- **Capital-market enterprises.** An enterprise of one of these legal forms that is a capital-market enterprise must account under the PublG whatever its size (§ 1(3) PublG).
- **Employees are counted differently here.** One twelfth of the month-end counts, with apprentices and with staff abroad (§ 1(2) PublG). The HGB size classes leave apprentices out.
- **Duty to tell the register.** When two of the three tests are met for the first time, the legal representatives must send a declaration to the company register without delay (§ 2(2) PublG).
- **What follows.** Statements within three months. The company layout rules apply with the necessary changes (§ 5(1) PublG). Partnerships and sole merchants may draw up the P&L under the rules for their own business (§ 5(5) PublG). Audit under § 6 PublG. Publication under § 9 PublG. Sole merchants and partnerships need no notes and no management report (§ 5(2) PublG). They need not publish the P&L if an annex to the balance sheet gives the details of § 5(5) PublG (§ 9(2) PublG). Private assets stay out of the balance sheet (§ 5(4) PublG). See https://www.gesetze-im-internet.de/publg/__5.html and https://www.gesetze-im-internet.de/publg/__6.html and https://www.gesetze-im-internet.de/publg/__9.html
- **End of the duty.** After three balance sheet dates in a row on which two of the three tests are no longer met (§ 2(1) PublG).

### Auditor qualification

- **Auditor qualification.** Auditors can be Wirtschaftsprüfer (WP) and Wirtschaftsprüfungsgesellschaften. Vereidigte Buchprüfer and Buchprüfungsgesellschaften may also audit medium-sized GmbHs and medium-sized partnerships within § 264a HGB. The statute names no other legal form for them. Every auditor needs an extract from the professional register that shows the entry under § 38 no. 1 letter h or no. 2 letter f WPO. See § 319(1) HGB at https://www.gesetze-im-internet.de/hgb/__319.html
- **Independence.** An auditor is shut out where there is reason to fear bias. § 319(3) HGB lists cases, among them holding shares in the company, being its legal representative, board member or employee, and having helped to keep the books or to draw up the statements being audited.

## The method, step by step

1. Fix the legal form and with it the set of rules. Every merchant draws up a balance sheet and a P&L under § 242 HGB. Companies add notes and a management report under § 264 HGB. An OHG or KG with no natural person as personally liable partner follows the company rules under § 264a HGB. https://www.gesetze-im-internet.de/hgb/__264a.html
2. For a sole merchant, test the release of § 241a HGB first: both limits in Section 2, on two balance sheet dates in a row. https://www.gesetze-im-internet.de/hgb/__241a.html
3. Set the size class under § 267 and § 267a HGB: two of three limits, on two balance sheet dates in a row, first date for a new company. Check the "always large" and "never micro" rules in Section 3. https://www.gesetze-im-internet.de/hgb/__267.html
4. Close the books. Take the inventory (§ 240 HGB) and post the year-end adjustments in Section 5 under the valuation rules of §§ 252 to 256a HGB. https://www.gesetze-im-internet.de/hgb/__253.html
5. Draw up the balance sheet in the layout of § 266 HGB and the P&L in the layout of § 275 HGB, with the reliefs of the size class. Companies do this within three months, small companies within six months at the latest (§ 264(1) HGB). https://www.gesetze-im-internet.de/hgb/__266.html
6. Write the notes under §§ 284 to 288 HGB (Section 8). Medium-sized and large companies add the management report under § 289 HGB. https://www.gesetze-im-internet.de/hgb/__289.html
7. If the company is not small, have the statements and the management report audited under § 316 HGB. The auditor should be elected before the financial year ends (§ 318 HGB). https://www.gesetze-im-internet.de/hgb/__316.html
8. Have the statements adopted. In a GmbH the shareholders decide within eight months, or eleven months in a small company (§ 42a GmbHG). https://www.gesetze-im-internet.de/gmbhg/__42a.html
9. Send the documents for the size class (Section 9) to the company register within one year after the balance sheet date under § 325 HGB, with the reliefs of § 326 and § 327 HGB. Register and identify the sender first. https://www.unternehmensregister.de/de/so-gehts/uebermitteln
10. Send the content of the balance sheet and the P&L to the tax office as an electronic data set (E-Bilanz) under § 5b EStG. Values that do not follow tax law are adjusted by additions or notes, or a separate tax balance sheet is sent. The paragraph lists further documents to send; their start dates are in § 52 EStG and are not covered here. https://www.gesetze-im-internet.de/estg/__5b.html
11. Keep the statements, the books and the inventories for ten years, the accounting vouchers for eight years and business letters for six years under § 257(4) HGB. https://www.gesetze-im-internet.de/hgb/__257.html
12. If a threat notice from the Bundesamt für Justiz arrives, publish within six weeks of receipt or lodge a justified objection in the same time under § 335 HGB. https://www.bundesjustizamt.de/DE/Themen/OrdnungsgeldVollstreckung/Jahresabschluesse/Offenlegung/Verfahren/Verfahren_node.html

## Ask the client first

- What is the legal form? For an OHG or KG: is at least one personally liable partner a natural person?
- What were the balance sheet total, the revenue and the average number of employees at the last two balance sheet dates (three for the PublG)? Was the company newly formed or converted in that time?
- Are the company's securities traded on an organised market, or has admission been applied for? Is it a bank, an insurer, an investment company, or a company that only holds participations?
- When does the financial year begin and end? This decides the size limits that apply, the publication medium and the one-year deadline.
- Is the company included in a parent's consolidated accounts, and are all conditions of § 264(3) or § 264b HGB met? Is the company itself a parent?
- Has the Bundesamt für Justiz sent a threat notice, and on which day was it received?

## When to refuse or refer

- Consolidated accounts: the duty under § 290 HGB, the size exemption under § 293 HGB, consolidation methods and IFRS accounts. Refer to a Wirtschaftsprüfer.
- Banks, financial services firms, insurers, pension funds and cooperatives: they have their own sections of the HGB and their own layouts.
- Capital-market companies: the single electronic reporting format, the responsibility statement, the four-month deadline and the higher fines.
- The non-financial statement under § 289b HGB and any sustainability reporting. This Guide does not cover it.
- The country-by-country income tax report of very large groups (from § 342 HGB) and payment reports of the raw materials sector (from § 341q HGB).
- Investment funds, issuers of investment products and energy suppliers: separate publication rules named by the Federal Office of Justice.
- Pension valuations and any discount rate: an actuary and the current Bundesbank table are needed.
- Deferred tax calculations and the tax balance sheet. This Guide names the rules only.
- Liquidation, insolvency and changes of the financial year: the duty to publish goes on, but the dates and the documents differ.
- An objection, a request for reinstatement or a complaint against a fine from the Bundesamt für Justiz: refer to a Steuerberater, Wirtschaftsprüfer or lawyer at once, because the time limits are short.
- Whether a given Steuerberater or Wirtschaftsprüfer may sign off the statements: this Guide does not replace the professional.

## Sources

- HGB index (structure of the Third Book): https://www.gesetze-im-internet.de/hgb/ (read 2026-10-31)
- HGB § 9, § 240, § 241a, § 242, § 243, § 244, § 245, § 247 (register access, inventory, release, duty to draw up, language, signature, content): https://www.gesetze-im-internet.de/hgb/__9.html and https://www.gesetze-im-internet.de/hgb/__240.html and https://www.gesetze-im-internet.de/hgb/__241a.html and https://www.gesetze-im-internet.de/hgb/__242.html and https://www.gesetze-im-internet.de/hgb/__243.html and https://www.gesetze-im-internet.de/hgb/__244.html and https://www.gesetze-im-internet.de/hgb/__245.html and https://www.gesetze-im-internet.de/hgb/__247.html (read 2026-10-31)
- HGB § 246, § 249, § 250, § 251, § 252, § 253, § 256, § 256a, § 257 (recognition, valuation, retention): https://www.gesetze-im-internet.de/hgb/__246.html and https://www.gesetze-im-internet.de/hgb/__249.html and https://www.gesetze-im-internet.de/hgb/__250.html and https://www.gesetze-im-internet.de/hgb/__251.html and https://www.gesetze-im-internet.de/hgb/__252.html and https://www.gesetze-im-internet.de/hgb/__253.html and https://www.gesetze-im-internet.de/hgb/__256.html and https://www.gesetze-im-internet.de/hgb/__256a.html and https://www.gesetze-im-internet.de/hgb/__257.html (read 2026-10-31)
- HGB § 264, § 264a, § 264b, § 264d, § 265, § 266, § 267, § 267a, § 268 (companies, partnerships, layouts, size classes): https://www.gesetze-im-internet.de/hgb/__264.html and https://www.gesetze-im-internet.de/hgb/__264a.html and https://www.gesetze-im-internet.de/hgb/__264b.html and https://www.gesetze-im-internet.de/hgb/__264d.html and https://www.gesetze-im-internet.de/hgb/__265.html and https://www.gesetze-im-internet.de/hgb/__266.html and https://www.gesetze-im-internet.de/hgb/__267.html and https://www.gesetze-im-internet.de/hgb/__267a.html and https://www.gesetze-im-internet.de/hgb/__268.html (read 2026-10-31)
- HGB § 274, § 274a, § 275, § 276, § 277 (deferred tax, P&L): https://www.gesetze-im-internet.de/hgb/__274.html and https://www.gesetze-im-internet.de/hgb/__274a.html and https://www.gesetze-im-internet.de/hgb/__275.html and https://www.gesetze-im-internet.de/hgb/__276.html and https://www.gesetze-im-internet.de/hgb/__277.html (read 2026-10-31)
- HGB § 284, § 285, § 286, § 288, § 289, § 289b (notes, management report): https://www.gesetze-im-internet.de/hgb/__284.html and https://www.gesetze-im-internet.de/hgb/__285.html and https://www.gesetze-im-internet.de/hgb/__286.html and https://www.gesetze-im-internet.de/hgb/__288.html and https://www.gesetze-im-internet.de/hgb/__289.html and https://www.gesetze-im-internet.de/hgb/__289b.html (read 2026-10-31)
- HGB § 290, § 293, § 297, § 315e (groups, IFRS): https://www.gesetze-im-internet.de/hgb/__290.html and https://www.gesetze-im-internet.de/hgb/__293.html and https://www.gesetze-im-internet.de/hgb/__297.html and https://www.gesetze-im-internet.de/hgb/__315e.html (read 2026-10-31)
- HGB § 316, § 316a, § 318, § 319, § 321 (audit): https://www.gesetze-im-internet.de/hgb/__316.html and https://www.gesetze-im-internet.de/hgb/__316a.html and https://www.gesetze-im-internet.de/hgb/__318.html and https://www.gesetze-im-internet.de/hgb/__319.html and https://www.gesetze-im-internet.de/hgb/__321.html (read 2026-10-31)
- HGB § 325, § 325a, § 326, § 327, § 328, § 329, § 334, § 335, § 335b (publication, fines): https://www.gesetze-im-internet.de/hgb/__325.html and https://www.gesetze-im-internet.de/hgb/__325a.html and https://www.gesetze-im-internet.de/hgb/__326.html and https://www.gesetze-im-internet.de/hgb/__327.html and https://www.gesetze-im-internet.de/hgb/__328.html and https://www.gesetze-im-internet.de/hgb/__329.html and https://www.gesetze-im-internet.de/hgb/__334.html and https://www.gesetze-im-internet.de/hgb/__335.html and https://www.gesetze-im-internet.de/hgb/__335b.html (read 2026-10-31)
- EGHGB Art. 88, Art. 92 and Art. 93 (start of the register rule, start of the § 241a amounts, start of the size limits): https://www.gesetze-im-internet.de/hgbeg/art_88.html and https://www.gesetze-im-internet.de/hgbeg/art_92.html and https://www.gesetze-im-internet.de/hgbeg/art_93.html (read 2026-10-31)
- PublG § 1, § 2, § 3, § 5, § 6, § 9: https://www.gesetze-im-internet.de/publg/__1.html and https://www.gesetze-im-internet.de/publg/__2.html and https://www.gesetze-im-internet.de/publg/__3.html and https://www.gesetze-im-internet.de/publg/__5.html and https://www.gesetze-im-internet.de/publg/__6.html and https://www.gesetze-im-internet.de/publg/__9.html (read 2026-10-31)
- GmbHG § 42a, AktG § 175, WPO § 66a: https://www.gesetze-im-internet.de/gmbhg/__42a.html and https://www.gesetze-im-internet.de/aktg/__175.html and https://www.gesetze-im-internet.de/wipro/__66a.html (read 2026-10-31)
- EStG § 5, § 5b (tax limits on provisions, E-Bilanz): https://www.gesetze-im-internet.de/estg/__5.html and https://www.gesetze-im-internet.de/estg/__5b.html (read 2026-10-31)
- JVKostG cost schedule (fee for a second and further fine under § 335 HGB): https://www.gesetze-im-internet.de/jvkostg/anlage.html (read 2026-10-31)
- Bundesamt für Justiz, fine procedure: https://www.bundesjustizamt.de/DE/Themen/OrdnungsgeldVollstreckung/Jahresabschluesse/Offenlegung/Verfahren/Verfahren_node.html (read 2026-10-31)
- Bundesamt für Justiz, publication duties: https://www.bundesjustizamt.de/DE/Themen/OrdnungsgeldVollstreckung/Jahresabschluesse/Offenlegung/Pflichten/Pflichten_node.html (read 2026-10-31)
- Bundesamt für Justiz, questions and answers: https://www.bundesjustizamt.de/DE/Themen/OrdnungsgeldVollstreckung/Jahresabschluesse/Offenlegung/Fragen/Fragen_node.html (read 2026-10-31)
- Bundesamt für Justiz, news on the move to the company register: https://www.bundesjustizamt.de/DE/Themen/OrdnungsgeldVollstreckung/Jahresabschluesse/Offenlegung/Aktuelles/Aktuelles_node.html (read 2026-10-31)
- Bundesamt für Justiz, parts of the statements by size: https://www.bundesjustizamt.de/DE/Themen/OrdnungsgeldVollstreckung/Jahresabschluesse/Verstoesse/InhaltJahresabschluss/Bestandteile/Bestandteile_node.html (read 2026-10-31)
- Company register, how to send documents: https://www.unternehmensregister.de/de/so-gehts/uebermitteln (read 2026-10-31)
- Deutsche Bundesbank, discount rates under § 253(2) HGB: https://www.bundesbank.de/de/statistiken/geld-und-kapitalmaerkte/zinssaetze-und-renditen/abzinsungszinssaetze/abzinsungszinssaetze-772396 (read 2026-10-31)
- [HGB § 342r](https://www.gesetze-im-internet.de/hgb/__342r.html), read 2026-10-31

## Disclaimer

This Guide and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this Guide. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

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
