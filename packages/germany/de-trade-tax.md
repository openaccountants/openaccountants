---
name: de-trade-tax
description: Use this skill whenever asked about German Trade Tax (Gewerbesteuer / GewSt) for self-employed Gewerbetreibende. Trigger on phrases like "Gewerbesteuer", "trade tax Germany", "GewSt", "Hebesatz", "Gewerbeertrag", "Steuermessbetrag", "Freibetrag 24500", "Gewerbesteuer Anrechnung", "§35 EStG", "trade tax credit", "Hinzurechnungen", "Kürzungen", "GewSt 1 A", or any question about German municipal trade tax obligations. Covers the Gewerbeertrag computation, EUR 24,500 Freibetrag, 3.5% Steuermesszahl, Hebesatz by municipality, Anrechnung on Einkommensteuer (4.0x credit under §35 EStG), Hinzurechnungen and Kürzungen, effective rate analysis, and Vorauszahlungen. ALWAYS read this skill before touching any Gewerbesteuer work.
version: 1.0
jurisdiction: DE
tax_year: 2026
last_updated: 2026-09-27
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Trade tax in Germany (Gewerbesteuer)

## Scope

This Guide covers German trade tax (Gewerbesteuer, GewSt) for a sole proprietor or a partnership that runs a commercial business (Gewerbebetrieb): who is liable, how trade income (Gewerbeertrag) is worked out, the add-backs (Hinzurechnungen) and reductions (Kürzungen), the allowance, the base rate (Steuermesszahl), the municipal multiplier (Hebesatz), the credit against income tax under § 35 EStG, prepayments and the return. Companies such as a GmbH are covered only for two questions: do they pay, and do they get the allowance.

- **Tax year.** Figures are for collection period (tax year) 2026, the law in force on 25 September 2026. A short section below covers the 2025 returns being filed now.
- **Where the figures come from.** The federal statutes, except the 2026 multiplier floor and the church tax range, which come from the finance ministry booklet "Steuern von A bis Z" (Stand Januar 2025).
- **Two authorities.** The tax office sets the base amount (Gewerbesteuermessbescheid), which also decides whether the business is liable at all ([§ 184(1) AO](https://www.gesetze-im-internet.de/ao_1977/__184.html)). The municipality applies its multiplier, sets the tax (Gewerbesteuerbescheid) and collects it.
- **Related Guide.** Whether a self-employed person is a Freiberufler or a Gewerbetreibender in the first place is triaged in `de-freelance-intake`.

## Ask the client first

- What exactly do you do, and do you work alone, in a partnership or through a company? Does any part of the work involve selling goods or reselling other people's products?
- In which municipality or municipalities does the business have premises (Betriebsstätten), and did it move during the year?
- What is the profit from the business for the year (Anlage G, from the EÜR or the balance sheet)? Is the financial year the calendar year?
- What did the business pay in the year for interest, annuities, a silent partner's profit share, rent and leasing (movable and immovable assets separately), and licence fees?
- Does the business own real property, and was Grundsteuer on it booked as a business expense? Does it hold shares in partnerships or companies? Did it make donations?
- Was a trade loss carry-forward (vortragsfähiger Gewerbeverlust) determined at the end of last year?
- What does the last trade tax notice show: base amount, multiplier, tax, and the prepayments now set?
- Is the return prepared by a Steuerberater (this changes the deadline)?
- For the § 35 credit: is the owner a church member, and what other income is in the income tax return?

## The method, step by step

1. **Is there a commercial business?** Decide under [§ 2 GewStG](https://www.gesetze-im-internet.de/gewstg/__2.html) with [§ 15(2) EStG](https://www.gesetze-im-internet.de/estg/__15.html) and [§ 18 EStG](https://www.gesetze-im-internet.de/estg/__18.html). A natural person in a free profession pays no trade tax; a capital company always pays (table "Who is liable" below).
2. **Start from the profit** worked out under income tax or corporation tax rules ([§ 7 GewStG](https://www.gesetze-im-internet.de/gewstg/__7.html)). Trade tax itself is not a business expense ([§ 4(5b) EStG](https://www.gesetze-im-internet.de/estg/__4.html)), so the profit has not been reduced by it.
3. **Add back** under [§ 8 GewStG](https://www.gesetze-im-internet.de/gewstg/__8.html): sum the financing items, each at its own share; subtract the EUR 200,000 allowance; add back one quarter of what is left; then add the other § 8 items.
4. **Reduce** under [§ 9 GewStG](https://www.gesetze-im-internet.de/gewstg/__9.html): above all the Grundsteuer booked for business-owned real property, and profit shares from partnerships.
5. **Deduct trade losses** of earlier years under [§ 10a GewStG](https://www.gesetze-im-internet.de/gewstg/__10a.html): in full up to EUR 1 million of trade income, and above that up to 60% of the excess.
6. **Round and apply the allowance** ([§ 11(1) GewStG](https://www.gesetze-im-internet.de/gewstg/__11.html)): round the trade income down to full EUR 100, then subtract EUR 24,500 for a natural person or partnership, never below zero.
7. **Apply the base rate** of 3.5% to get the base amount (Steuermessbetrag) ([§ 11(2) GewStG](https://www.gesetze-im-internet.de/gewstg/__11.html)).
8. **Apply the multiplier** of each municipality with a permanent establishment, read from that municipality's notice or its decision for the year ([§ 16 GewStG](https://www.gesetze-im-internet.de/gewstg/__16.html)). With several municipalities, apportion the base amount first ([§ 28 GewStG](https://www.gesetze-im-internet.de/gewstg/__28.html)).
9. **File** the return electronically if [§ 25 GewStDV](https://www.gesetze-im-internet.de/gewstdv_1955/__25.html) requires one, by the deadline in [§ 149 AO](https://www.gesetze-im-internet.de/ao_1977/__149.html).
10. **Pay** the prepayments on 15 February, 15 May, 15 August and 15 November and the balance within one month of the tax notice ([§ 19 GewStG](https://www.gesetze-im-internet.de/gewstg/__19.html), [§ 20 GewStG](https://www.gesetze-im-internet.de/gewstg/__20.html)).
11. **Claim the income tax credit** in the owner's or partner's income tax return: four times the base amount, but not more than the trade tax actually payable and not more than the income tax on the commercial income ([§ 35 EStG](https://www.gesetze-im-internet.de/estg/__35.html)).

## Who is liable

| Category | Trade tax? | Where it says so |
| --- | --- | --- |
| A standing commercial business run in Germany (a permanent establishment in Germany). A commercial business is an independent, lasting activity, carried on to make a profit and open to the general market, that is not farming or forestry, not a free profession and not other self-employed work | Yes | [§ 2(1) GewStG](https://www.gesetze-im-internet.de/gewstg/__2.html) with [§ 15(2) EStG](https://www.gesetze-im-internet.de/estg/__15.html) |
| Free professions carried on by a natural person: independent scientific, artistic, writing, teaching or educational work, and the named professions (doctors, dentists, vets, lawyers, notaries, patent attorneys, surveyors, engineers, architects, commercial chemists, auditors, tax advisers, consulting economists, sworn accountants, tax agents, Heilpraktiker, Dentisten, physiotherapists, journalists, photo reporters, interpreters, translators, Lotsen) and similar professions | No | [§ 18(1) no. 1 EStG](https://www.gesetze-im-internet.de/estg/__18.html) |
| Farming and forestry; other self-employed work under § 18(1) no. 3 EStG (for example executor, asset manager, supervisory board member) | No | [§ 15(2) EStG](https://www.gesetze-im-internet.de/estg/__15.html) |
| Capital companies (GmbH, AG, KGaA, SE), cooperatives, mutual insurance associations | Yes, always and in full, whatever they do: "gilt stets und in vollem Umfang" | [§ 2(2) GewStG](https://www.gesetze-im-internet.de/gewstg/__2.html) |
| Other private-law legal persons and associations without legal personality | Only as far as they run a commercial operation (wirtschaftlicher Geschäftsbetrieb), farming and forestry excepted | [§ 2(3) GewStG](https://www.gesetze-im-internet.de/gewstg/__2.html) |
| A partnership that also carries on a commercial activity of its own | Yes: the whole activity counts as commercial, whether the commercial part makes a profit or a loss (Abfärbung). The statute prints no minimum amount | [§ 15(3) no. 1 EStG](https://www.gesetze-im-internet.de/estg/__15.html), first case |
| A partnership with no commercial activity of its own that receives commercial income from a share in another partnership | For income tax the whole activity counts as commercial. For trade tax the states' decree of 5 November 2025 applies the Federal Fiscal Court ruling of 6 June 2019 "in allen offenen Fällen über den entschiedenen Einzelfall hinaus", without restating it. Refer | [State decree, 5 Nov 2025](https://www.bundesfinanzministerium.de/Content/DE/Standardartikel/Themen/Steuern/Steuerarten/Gewerbesteuer/2025-11-05-gle-aufhebung-gle-01-10-20-anl.pdf?__blob=publicationFile&v=3) |
| A partnership whose only personally liable partners are capital companies and which only they or non-partners manage (gewerblich geprägt) | Yes, in full | [§ 15(3) no. 2 EStG](https://www.gesetze-im-internet.de/estg/__15.html) |
| Travelling trade (Reisegewerbe) | Yes; the municipality at the centre of the activity levies it | [§ 35a GewStG](https://www.gesetze-im-internet.de/gewstg/__35a.html) |
| Businesses on the exemption list, for example one whose only activity is producing and selling power from a solar plant on, at or in a building of up to 30 kilowatts installed capacity (no. 32) | No, as far as the list goes | [§ 3 GewStG](https://www.gesetze-im-internet.de/gewstg/__3.html) |

- **Who owes the tax.** The entrepreneur for whose account the business is run. If a partnership runs it, the partnership owes the tax, not the partners ([§ 5 GewStG](https://www.gesetze-im-internet.de/gewstg/__5.html)).
- **Liability follows the activity, not the registration.** Trade tax attaches to running a standing commercial business ([§ 2(1) GewStG](https://www.gesetze-im-internet.de/gewstg/__2.html)), not to the Gewerbeanmeldung. Opening a business is notified to the municipality, which tells the tax office; a free profession is notified to the tax office directly. The further tax information (Fragebogen zur steuerlichen Erfassung) goes to the tax office electronically within one month ([§ 138(1), (1b), (4) AO](https://www.gesetze-im-internet.de/ao_1977/__138.html)).
- **IT consultants and software developers** are not named in § 18 EStG; the facts decide, and selling or reselling software or hardware points to a commercial business. Flag it.
- **Abfärbung is a partnership rule.** § 15(3) no. 1 EStG names partnerships only. Case law may set a de minimis limit, but no page read for this Guide prints it, so never call a small commercial part harmless or fatal without a Steuerberater.

## Trade income: the starting point

- **Definition.** The profit under income or corporation tax rules, plus § 8 and minus § 9 GewStG ([§ 7 GewStG](https://www.gesetze-im-internet.de/gewstg/__7.html)). Sole proprietor: Anlage G. Partnership: the separate and uniform determination, which includes partners' pay for work, loans or letting assets ([§ 15(1) no. 2 EStG](https://www.gesetze-im-internet.de/estg/__15.html)).
- **Period.** The calendar year, or the part of it in which the business was liable ([§ 14 GewStG](https://www.gesetze-im-internet.de/gewstg/__14.html)). A book-keeping business with a different financial year counts the profit in the period in which the financial year ends ([§ 10(2) GewStG](https://www.gesetze-im-internet.de/gewstg/__10.html)).

## Add-backs (Hinzurechnungen, § 8 GewStG)

Items are added back only as far as they reduced the profit. The financing items of § 8 no. 1 work in three steps ([§ 8 GewStG](https://www.gesetze-im-internet.de/gewstg/__8.html)). The law prints the shares in words, and each item has its own share.

| § 8 no. 1 item | Share that goes into the sum |
| --- | --- |
| a) Interest and other payments for debt, including discounts outside the ordinary course of business for early payment and discount amounts on selling bills and money claims | in full |
| b) Annuities and permanent burdens (not pensions under a direct employer pension promise) | in full |
| c) Profit shares of a silent partner | in full |
| d) Rent, lease and leasing for movable fixed assets owned by someone else | one fifth; only half of that for electric vehicles, qualifying plug-in hybrids and bicycles that are not motor vehicles |
| e) Rent, lease and leasing for immovable fixed assets owned by someone else | one half |
| f) Payments for the time-limited use of rights (concessions, licences), except licences that only allow passing derived rights on, and except amounts that are the base for the artists' social levy | one quarter |
| Allowance on the sum, per [§ 8 no. 1 GewStG](https://www.gesetze-im-internet.de/gewstg/__8.html): "soweit die Summe den Betrag von 200 000 Euro übersteigt" | EUR 200,000 |

1. Add up the items, each at its share.
2. Subtract the EUR 200,000 allowance. It is an allowance, not a cliff: at or below it nothing is added back; above it only the excess counts ([§ 8 GewStG](https://www.gesetze-im-internet.de/gewstg/__8.html)).
3. Add back one quarter ("Ein Viertel der Summe") of what is left.

- **Electric vehicles.** The halved share in letter d applies only to payments under contracts made after 31 December 2019; for contracts made before 1 January 2025 an electric range of 60 kilometres is enough where the statute otherwise asks for 80 kilometres; the halving applies for the last time in collection period 2030 ([§ 36(4) GewStG](https://www.gesetze-im-internet.de/gewstg/__36.html)).
- **Other add-backs** in [§ 8 GewStG](https://www.gesetze-im-internet.de/gewstg/__8.html): KGaA general partners' shares (no. 4); exempt dividends from holdings below the § 9 thresholds (no. 5); partnership loss shares (no. 8); corporate donations (no. 9); write-downs on company shares (no. 10); certain foreign taxes (no. 12). Refer these.
- **In practice.** A sole proprietor with ordinary costs stays below the allowance. Flag any case near it.

## Reductions (Kürzungen, § 9 GewStG)

| Reduction | Rule | Condition |
| --- | --- | --- |
| Property tax (no. 1 sentence 1) | The Grundsteuer booked as a business expense in the period, for real property belonging to the entrepreneur's business assets | This wording first applies for collection period 2025 ([§ 36(4b) GewStG](https://www.gesetze-im-internet.de/gewstg/__36.html)). The old rule (a share of the Einheitswert) is gone. Premises that are only rented give no reduction |
| Extended property reduction (no. 1 sentences 2 to 6) | On request, instead: trade income from managing the business's own real property | Only for pure property businesses. Refer |
| Partnership profit shares (no. 2) | Profit shares from a partnership of co-entrepreneurs, if counted in the profit | The partnership pays its own trade tax |
| German company dividends (no. 2a) | Dividends from a non-exempt German capital company, less directly related expenses | Holding at the start of the period "mindestens 15 Prozent des Grund- oder Stammkapitals" |
| Foreign permanent establishment (no. 3) | Trade income of a permanent establishment abroad | Refer |
| Donations (no. 5) | Donations for tax-privileged purposes (§§ 52 to 54 AO) from business funds | Up to 20% of the profit (plus the § 8 no. 9 add-back) or 4 per mille of turnover plus wages; excess carries forward |
| Foreign company dividends (no. 7, no. 8) | Dividends from a company with seat and management abroad | At least 15% holding (no. 7: at the start of the period); a lower treaty threshold prevails. Refer |

Source for every row: [§ 9 GewStG](https://www.gesetze-im-internet.de/gewstg/__9.html).

## Trade losses (§ 10a GewStG)

| What | Value | Source |
| --- | --- | --- |
| Trade income that losses of earlier periods may reduce without limit | EUR 1 million ("1 Million Euro") | [§ 10a sentence 1 GewStG](https://www.gesetze-im-internet.de/gewstg/__10a.html) |
| Share of the trade income above that which losses may reduce | 60% ("bis zu 60 Prozent") | [§ 10a sentence 2 GewStG](https://www.gesetze-im-internet.de/gewstg/__10a.html) |

- **Forward only.** § 10a speaks only of losses of earlier periods; there is no carry-back. Do not use the income tax loss rules of § 10d EStG for trade tax.
- **Separate determination.** The loss left at the end of each period is determined separately, and a business with such a determination must file a return ([§ 25(1) no. 6 GewStDV](https://www.gesetze-im-internet.de/gewstdv_1955/__25.html)).
- **Partnerships.** Losses and the EUR 1 million base are allocated by the general profit-sharing key, without advance profit shares ([§ 10a GewStG](https://www.gesetze-im-internet.de/gewstg/__10a.html)). A change of partners is out of scope: refer.
- **Transfer.** If a business passes as a whole to another entrepreneur, the new owner cannot use the losses of the business taken over (§ 10a sentence 8 with § 2(5) GewStG). For companies, § 8c and § 8d KStG also apply: refer.

## Figures for 2026

| Figure | Value | Year | Source and quote |
| --- | --- | --- | --- |
| Allowance, natural persons and partnerships | EUR 24,500 | 2026 | [§ 11(1) no. 1 GewStG](https://www.gesetze-im-internet.de/gewstg/__11.html): "Freibetrag in Höhe von 24 500 Euro" |
| Allowance, § 2(3) bodies, certain partly exempt bodies, businesses of public-law persons | EUR 5,000 | 2026 | [§ 11(1) no. 2 GewStG](https://www.gesetze-im-internet.de/gewstg/__11.html): "Freibetrag in Höhe von 5 000 Euro" |
| Allowance, capital companies (GmbH, AG) | none | 2026 | § 11(1) names none for them |
| Rounding before the allowance | down to full EUR 100 | 2026 | [§ 11(1) GewStG](https://www.gesetze-im-internet.de/gewstg/__11.html): "auf volle 100 Euro nach unten abzurunden" |
| Base rate (Steuermesszahl) | 3.5% | 2026 | [§ 11(2) GewStG](https://www.gesetze-im-internet.de/gewstg/__11.html): "beträgt 3,5 Prozent" |
| Multiplier floor where the municipality has set none higher | 200% | 2026 | [BMF booklet](https://www.bundesfinanzministerium.de/Content/DE/Downloads/Broschueren_Bestellservice/steuern-von-a-z.pdf?__blob=publicationFile&v=9), chapter Gewerbesteuer: "Er beträgt mindestens 200 Prozent" |
| Multiplier floor from 2027 | 280% | from collection period 2027 only | [§ 16(4) GewStG](https://www.gesetze-im-internet.de/gewstg/__16.html): "Er beträgt 280 Prozent"; start date in [§ 36(5b) GewStG](https://www.gesetze-im-internet.de/gewstg/__36.html) |
| Income tax credit factor | four times the base amount | 2026 | [§ 35(1) EStG](https://www.gesetze-im-internet.de/estg/__35.html): "um das Vierfache" |
| Minimum single prepayment | EUR 50 | 2026 | [§ 19(5) GewStG](https://www.gesetze-im-internet.de/gewstg/__19.html): "mindestens 50 Euro" |
| Return required if trade income is more than | EUR 24,500 | 2026 | [§ 25(1) no. 1 GewStDV](https://www.gesetze-im-internet.de/gewstdv_1955/__25.html): "den Betrag von 24 500 Euro überstiegen hat" |

## Allowance, base rate and multiplier

- **Allowance.** Round down to full EUR 100, then subtract the allowance, "höchstens jedoch in Höhe des abgerundeten Gewerbeertrags", so never below zero ([§ 11(1) GewStG](https://www.gesetze-im-internet.de/gewstg/__11.html)). It is given per period per business; § 11 does not cut it for a short period. The base rate is not the tax rate; home workers get a reduced one under § 11(3): refer.
- **Multiplier.** Trade tax = base amount times the multiplier of the municipality with the permanent establishment ([§ 16(1) GewStG](https://www.gesetze-im-internet.de/gewstg/__16.html), [§ 4 GewStG](https://www.gesetze-im-internet.de/gewstg/__4.html)). It is the same for all businesses in the municipality. A decision for a year is taken by 30 June with effect from 1 January; later it can only be set at or below the last level ([§ 16(3), (4) GewStG](https://www.gesetze-im-internet.de/gewstg/__16.html)).
- **Floor, with its year.** 200% for 2026 ([BMF booklet](https://www.bundesfinanzministerium.de/Content/DE/Downloads/Broschueren_Bestellservice/steuern-von-a-z.pdf?__blob=publicationFile&v=9)). The statute page already shows 280%, inserted by the law of 29 June 2026 (BGBl. 2026 I Nr. 197) and applied "erstmals für den Erhebungszeitraum 2027" ([§ 36(5b) GewStG](https://www.gesetze-im-internet.de/gewstg/__36.html)). Never quote 280% for 2026.
- **No city multipliers here.** They appear on no federal page this Guide may cite. Read the rate from the client's own notice or the municipality's decision for the year, never from memory.
- **Several municipalities or a move.** The base amount is apportioned, also where a permanent establishment moved during the period ([§ 28(1) GewStG](https://www.gesetze-im-internet.de/gewstg/__28.html)), by wages ([§ 29 GewStG](https://www.gesetze-im-internet.de/gewstg/__29.html)); for a business not run by a legal person EUR 25,000 a year in total counts as wages for the working owners ([§ 31(5) GewStG](https://www.gesetze-im-internet.de/gewstg/__31.html): "insgesamt 25.000 Euro jährlich anzusetzen"). Refer the apportionment.

## The income tax credit (§ 35 EStG)

A sole proprietor, a partner in a commercial partnership, and a KGaA general partner get a reduction of income tax for trade tax ([§ 35 EStG](https://www.gesetze-im-internet.de/estg/__35.html)). The reduction is the lowest of three amounts:

1. **Four times the base amount** set for the collection period that matches the income tax year ("das Vierfache ... des festgesetzten Steuermessbetrags"); for a partner, four times the partner's share of it.
2. **The trade tax actually payable**: "Der Abzug des Steuerermäßigungsbetrags ist auf die tatsächlich zu zahlende Gewerbesteuer beschränkt" (§ 35(1) sentence 5).
3. **The maximum reduction amount (Ermäßigungshöchstbetrag)**: the positive commercial income divided by all positive income, times the reduced tariff tax. Commercial income means profits and profit shares that are subject to trade tax.

- **Unused amounts are lost.** § 35 has no carry-forward, carry-back or refund of an unused credit.
- **Partners.** The share follows the general profit-sharing key, without advance profit shares; the base amount, the trade tax payable and each share are determined separately and uniformly (§ 35(2) EStG).
- **Base notices.** The base amount notice and the trade tax notice are Grundlagenbescheide for the credit (§ 35(3) EStG): if the tax office or municipality changes them, the income tax follows.
- **Church tax.** The credit does not reduce church tax: "§ 35 ist bei der Ermittlung der festzusetzenden Einkommensteuer nach Satz 1 nicht anzuwenden" ([§ 51a(2) EStG](https://www.gesetze-im-internet.de/estg/__51a.html)). Church tax is 8% or 9% of income tax depending on the state ([BMF booklet](https://www.bundesfinanzministerium.de/Content/DE/Downloads/Broschueren_Bestellservice/steuern-von-a-z.pdf?__blob=publicationFile&v=9): "je nach Bundesland 8 oder 9 Prozent").
- **Solidarity surcharge: check.** [§ 3(2) SolzG](https://www.gesetze-im-internet.de/solzg_1995/__3.html) has no sentence switching § 35 off, which points to the surcharge being computed after the credit. Older material says the opposite. This Guide does not settle it: check with a Steuerberater.
- **Companies.** A GmbH pays corporation tax and gets no § 35 credit.

## Boundaries and exceptions

| Test | Wording | Consequence | Source |
| --- | --- | --- | --- |
| Allowance | Rounded trade income not more than EUR 24,500 | Base amount nil, no trade tax, no § 35 credit | [§ 11(1) GewStG](https://www.gesetze-im-internet.de/gewstg/__11.html) |
| Return duty | Trade income "überstiegen hat" (more than) EUR 24,500 | Return required; at exactly EUR 24,500 or less, no return unless no. 6 or no. 7 applies | [§ 25(1) GewStDV](https://www.gesetze-im-internet.de/gewstdv_1955/__25.html) |
| Return regardless of amount | Capital companies and cooperatives not exempt; a loss carry-forward determined at the end of the last period; the tax office asks | Return required even with nil tax | [§ 25(1) no. 2, 3, 6, 7 GewStDV](https://www.gesetze-im-internet.de/gewstdv_1955/__25.html) |
| Financing add-back | Sum "übersteigt" (more than) EUR 200,000 | Only the excess counts; one quarter of it is added | [§ 8 no. 1 GewStG](https://www.gesetze-im-internet.de/gewstg/__8.html) |
| Dividend reduction | Holding "mindestens" (at least) 15% at the start of the period | Reduction under no. 2a or no. 7; below that, § 8 no. 5 may add back | [§ 9 GewStG](https://www.gesetze-im-internet.de/gewstg/__9.html) |
| Loss use | Up to EUR 1 million in full; above it up to 60% | Rest carries forward | [§ 10a GewStG](https://www.gesetze-im-internet.de/gewstg/__10a.html) |
| Prepayment | Single prepayment "mindestens" (at least) EUR 50 | Below that none is set | [§ 19(5) GewStG](https://www.gesetze-im-internet.de/gewstg/__19.html) |
| Multiplier decision | By 30 June for the current year | After that only at or below the last level | [§ 16(3) GewStG](https://www.gesetze-im-internet.de/gewstg/__16.html) |
| Free profession in a company | A GmbH of architects or doctors | Liable by legal form | [§ 2(2) GewStG](https://www.gesetze-im-internet.de/gewstg/__2.html) |
| Mixed activity | Partnership with any commercial part | Whole activity commercial; refer | [§ 15(3) EStG](https://www.gesetze-im-internet.de/estg/__15.html) |

## Worked cases

The multipliers below are **assumptions** for the example, as if read from the client's own notice. They are not the rate of any named municipality.

**Case 1: sole proprietor, ordinary costs** ([§ 8](https://www.gesetze-im-internet.de/gewstg/__8.html), [§ 11 GewStG](https://www.gesetze-im-internet.de/gewstg/__11.html), [§ 35 EStG](https://www.gesetze-im-internet.de/estg/__35.html)). Profit EUR 80,000. Loan interest EUR 12,000 (in full), rent for the shop EUR 36,000 (one half = EUR 18,000), car leasing EUR 10,000 for a petrol car (one fifth = EUR 2,000). Sum EUR 32,000, not above EUR 200,000: nothing is added back. Trade income EUR 80,000; less EUR 24,500 = EUR 55,500; times 3.5% = base amount EUR 1,942.50. Assumed multiplier 490%: trade tax EUR 9,518.25. Credit: four times the base amount = EUR 7,770, lower than the trade tax, so (if the income tax on the commercial income is at least that) the credit is EUR 7,770 and EUR 1,748.25 of trade tax is not offset.

**Case 2: same business at the 2026 floor** ([BMF booklet](https://www.bundesfinanzministerium.de/Content/DE/Downloads/Broschueren_Bestellservice/steuern-von-a-z.pdf?__blob=publicationFile&v=9), [§ 35 EStG](https://www.gesetze-im-internet.de/estg/__35.html), [§ 19 GewStG](https://www.gesetze-im-internet.de/gewstg/__19.html)). Base amount EUR 1,942.50 times 200% = trade tax EUR 3,885. Four times the base amount (EUR 7,770) is higher, so the credit is capped at EUR 3,885; the rest is lost. Next year's prepayments: one quarter of EUR 3,885, rounded down to full euros = EUR 971 on each of the four dates, unless the municipality adjusts them.

**Case 3: partnership above the add-back allowance** ([§ 8 GewStG](https://www.gesetze-im-internet.de/gewstg/__8.html)). Interest EUR 180,000 (in full) and rent for a warehouse EUR 120,000 (one half = EUR 60,000). Sum EUR 240,000; less EUR 200,000 = EUR 40,000; one quarter = EUR 10,000 is added to the profit.

**Case 4: loss carry-forward above the base** ([§ 10a GewStG](https://www.gesetze-im-internet.de/gewstg/__10a.html), [§ 11 GewStG](https://www.gesetze-im-internet.de/gewstg/__11.html)). Partnership trade income EUR 1,500,000 before losses; losses carried forward EUR 2,000,000. Deduct EUR 1,000,000 in full, plus 60% of the EUR 500,000 above it = EUR 300,000: total EUR 1,300,000. Trade income left EUR 200,000; loss still carried EUR 700,000. Less EUR 24,500 = EUR 175,500; times 3.5% = base amount EUR 6,142.50.

**Case 5: just above the allowance** ([§ 11 GewStG](https://www.gesetze-im-internet.de/gewstg/__11.html), [§ 25 GewStDV](https://www.gesetze-im-internet.de/gewstdv_1955/__25.html)). Trade income EUR 24,580. Rounded down to EUR 24,500, less the allowance: nil. No trade tax and no § 35 credit. But § 25(1) no. 1 GewStDV looks at the trade income itself, which is more than EUR 24,500, so on its wording a return is due. File it.

**Case 6: free profession** ([§ 18 EStG](https://www.gesetze-im-internet.de/estg/__18.html)). A self-employed architect working alone, nothing else. Architects are named in § 18(1) no. 1 EStG: no commercial business, no trade tax, no trade tax return. If the same architect also sells building materials, flag it: the income tax rules on mixed activity decide, and a partnership doing both is commercial in full.

## When to refuse or refer

- The multiplier of a named municipality: it is on no federal page. Send the client to the municipality's notice or decision.
- Any "combined rate", "effective burden" or break-even multiplier: no official page prints one, and each ignores the two caps on the credit. Work through the client's own figures instead.
- Borderline free profession or mixed activity (IT, software, consultants, a partnership with a commercial side line). Refer to a Steuerberater.
- A partnership holding a share in a commercial partnership, after the 5 November 2025 decree.
- Organschaft (§ 2(2) sentence 2 GewStG), permanent establishments abroad, foreign dividends, controlled foreign company income (§ 7 sentences 7 and 8, § 9 no. 3, 7, 8 GewStG).
- Apportionment between municipalities beyond the basic rule, including wind, solar and storage businesses (§ 29 GewStG).
- The extended property reduction (§ 9 no. 1 sentences 2 to 6 GewStG).
- Sale or closure of a business or a partnership share (§ 7 sentence 2 GewStG); loss use after a change of partners or shareholders (§ 10a GewStG, § 8c and § 8d KStG).
- Partnerships that opted into corporate taxation (§ 2(8) GewStG); home workers (§ 11(3)); shipping, banks and insurers.
- Reclassification after an audit (free profession treated as commercial for open past years): base amounts and trade tax follow, and the § 35 credit follows the notices. Refer.
- The solidarity surcharge effect of the credit (see above): check.

## Filing and payment

**The return.** A declaration for setting the base amount, plus an apportionment declaration where § 28 applies, filed electronically in the official data format; on request the tax office can accept paper to avoid undue hardship, signed by hand ([§ 14a GewStG](https://www.gesetze-im-internet.de/gewstg/__14a.html)). The ELSTER form names are GewSt 1 A (return) and GewSt 1 D (apportionment); check them on ELSTER. Who must file is in the Boundaries table ([§ 25 GewStDV](https://www.gesetze-im-internet.de/gewstdv_1955/__25.html)). This matches `de-freelance-intake`: a sole trader files only above EUR 24,500 of trade income or when asked, or when a loss carry-forward exists.

| Deadline | Collection period 2026 | Source |
| --- | --- | --- |
| Without an adviser: seven months after the year end | 31 July 2027 is a Saturday, so the period ends on Monday 2 August 2027 | [§ 149(2) AO](https://www.gesetze-im-internet.de/ao_1977/__149.html), [§ 108(3) AO](https://www.gesetze-im-internet.de/ao_1977/__108.html) |
| With a Steuerberater: last day of February of the second following year (§ 149(3) no. 3 names this return) | Tuesday 29 February 2028 | [§ 149(3) AO](https://www.gesetze-im-internet.de/ao_1977/__149.html) |
| Earlier call-in | The tax office can call an advised return in earlier, with four months' notice | [§ 149(4) AO](https://www.gesetze-im-internet.de/ao_1977/__149.html) |

**Payment** ([§ 19](https://www.gesetze-im-internet.de/gewstg/__19.html), [§ 20 GewStG](https://www.gesetze-im-internet.de/gewstg/__20.html)).

- **Prepayments** fall due on 15 February, 15 May, 15 August and 15 November, each in principle one quarter ("ein Viertel") of the tax from the last assessment, rounded down to full euros, and set only if at least EUR 50. With a different financial year they are paid during the financial year ending in the period (businesses founded, newly liable or switched after 31 December 1985).
- **Adjustment.** The municipality may adjust prepayments to the expected tax until the end of the 15th month after the period (an increase is then due within one month of the notice); an expected base amount set by the tax office binds it. A new business is set up the same way. If prepayments look too high, ask the municipality to adjust them.
- **Settlement.** Prepayments are credited against the tax. A balance is due within one month of the tax notice (at once for prepayments due and unpaid); an overpayment is set off or refunded.

**Penalties and interest.** The AO collection rules apply to trade tax administered by a municipality ([§ 1(2) AO](https://www.gesetze-im-internet.de/ao_1977/__1.html)).

| Charge | Value | Source and quote |
| --- | --- | --- |
| Late filing surcharge, per started month of delay, for the base amount return and the apportionment declaration | EUR 25 | [§ 152(6) AO](https://www.gesetze-im-internet.de/ao_1977/__152.html): "der eingetretenen Verspätung 25 Euro" |
| Highest late filing surcharge per return | EUR 25,000 | [§ 152(10) AO](https://www.gesetze-im-internet.de/ao_1977/__152.html): "höchstens 25 000 Euro betragen" |
| Late payment surcharge, per started month, on the overdue tax rounded down to a multiple of EUR 50 | 1% | [§ 240(1) AO](https://www.gesetze-im-internet.de/ao_1977/__240.html): "ein Säumniszuschlag von 1 Prozent" |
| Interest on a later assessment difference (either way) | 0.15% a month, 1.8% a year | [§ 238(1a) AO](https://www.gesetze-im-internet.de/ao_1977/__238.html): "0,15 Prozent für jeden Monat, das heißt 1,8 Prozent für jedes Jahr" |

- **Late filing.** The tax office may set a surcharge for any late return, and must if the return is not filed within 14 months of the year end, or by the date in a call-in order, unless the deadline was extended ([§ 152(2) AO](https://www.gesetze-im-internet.de/ao_1977/__152.html)). For this return the let-outs for nil tax or tax covered by prepayments do not apply (§ 152(6) carries over only § 152(3) no. 1). Example: filed three months and five days late = four started months = EUR 100. The surcharge goes to the municipality, without the multiplier ([§ 14b GewStG](https://www.gesetze-im-internet.de/gewstg/__14b.html)).
- **Late payment.** No surcharge for a delay of up to three days ([§ 240(3) AO](https://www.gesetze-im-internet.de/ao_1977/__240.html)). Example: EUR 1,234.56 overdue is rounded down to EUR 1,200, so EUR 12 per started month.
- **Interest** runs from 15 months after the end of the year in which the tax arose and does not apply to prepayments ([§ 233a AO](https://www.gesetze-im-internet.de/ao_1977/__233a.html)).

## Returns being filed now: collection period 2025

- **Same rules.** The allowance, base rate, add-back allowance and § 35 factor above applied in 2025 too ([§ 11](https://www.gesetze-im-internet.de/gewstg/__11.html), [§ 8 GewStG](https://www.gesetze-im-internet.de/gewstg/__8.html)). The new property tax reduction (Grundsteuer booked as an expense) first applies for 2025 ([§ 36(4b) GewStG](https://www.gesetze-im-internet.de/gewstg/__36.html)). The 2025 multiplier floor is the 200% in the booklet (edition Stand Januar 2025).
- **Deadlines.** Without an adviser the 2025 return was due on Friday 31 July 2026; it is now late, so file at once and expect a possible surcharge ([§ 149(2) AO](https://www.gesetze-im-internet.de/ao_1977/__149.html), [§ 152 AO](https://www.gesetze-im-internet.de/ao_1977/__152.html)). With a Steuerberater the deadline is the last day of February 2027; 28 February 2027 is a Sunday, so it ends on Monday 1 March 2027 ([§ 108(3) AO](https://www.gesetze-im-internet.de/ao_1977/__108.html)). The Corona-era extensions stop at period 2024 (advised 2024 returns: 30 April 2026) and do not apply to 2025 ([Art. 97 § 36 EGAO](https://www.gesetze-im-internet.de/aoeg_1977/art_97__36.html)).

## Completion checklist

- [ ] Liability decided and documented (free profession, commercial business, company, partnership rule), with any doubt flagged.
- [ ] Profit taken from Anlage G or the partnership determination; trade tax not deducted.
- [ ] § 8 no. 1 items summed at their own shares; EUR 200,000 allowance applied; other § 8 items checked.
- [ ] § 9 reductions checked, Grundsteuer only for business-owned property booked as an expense.
- [ ] Losses brought forward applied within the EUR 1 million base and 60%.
- [ ] Trade income rounded down to full EUR 100; allowance applied only to natural persons and partnerships.
- [ ] Base amount at 3.5%; multiplier read from the client's own notice, with its year.
- [ ] Return duty checked against § 25 GewStDV; deadline set with or without an adviser.
- [ ] Prepayments reconciled; adjustment requested if the year's tax will differ.
- [ ] § 35 credit worked as the lowest of the three amounts; church tax not reduced; surcharge question flagged.

## Sources

Every rule above links to its section of the consolidated statute on gesetze-im-internet.de (GewStG, GewStDV, EStG, SolzG, AO, EGAO) or to the finance ministry document it comes from: the [booklet "Steuern von A bis Z"](https://www.bundesfinanzministerium.de/Content/DE/Downloads/Broschueren_Bestellservice/steuern-von-a-z.pdf?__blob=publicationFile&v=9) (Stand Januar 2025) and the [states' decree of 5 November 2025](https://www.bundesfinanzministerium.de/Content/DE/Standardartikel/Themen/Steuern/Steuerarten/Gewerbesteuer/2025-11-05-gle-aufhebung-gle-01-10-20-anl.pdf?__blob=publicationFile&v=3). Pages were read on 25 to 27 September 2026.

## Disclaimer

This Guide is information, not tax, legal or financial advice. Have a qualified professional (Steuerberater or Wirtschaftsprüfer) review any figure before filing or acting on it.

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
