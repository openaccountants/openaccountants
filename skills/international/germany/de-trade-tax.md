---
name: de-trade-tax
description: "German trade tax (Gewerbesteuer, GewSt) for collection period 2026: who is liable (sole traders and partnerships with a commercial business, every GmbH, UG and AG; free professions excluded), trade income (Gewerbeertrag) with the § 8 add-backs (one quarter of financing items above EUR 200,000) and § 9 reductions (Grundsteuer, partnership shares, 15% participation exemption, donations), the EUR 24,500 allowance, the 3.5% base rate, the municipal multiplier (Hebesatz, at least 200% for 2026, 280% from 2027), the § 35 EStG income tax credit (four times the base amount, capped), loss carry-forward (EUR 1 million plus 60%), apportionment between municipalities (Zerlegung), the return, quarterly prepayments, surcharges and interest. Trigger on: Gewerbesteuer, GewSt, Hebesatz, Gewerbeertrag, Steuermessbetrag, Freibetrag 24.500, Hinzurechnungen, Kürzungen, § 35 EStG, Zerlegung, Gewerbesteuer-Vorauszahlung, trade tax Germany. Out of scope: income tax of the owner (de-self-employed-income-tax, de-income-tax), partners' income (de-partners-and-part-year), corporate income tax (de-corporate-tax), non-residents (de-non-resident-tax)."
version: 1.1
jurisdiction: DE
tax_year: 2026
last_updated: 2026-10-24
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Trade tax in Germany (Gewerbesteuer): collection period 2026

> **General reference only.** This skill is a source-cited draft. No accountant has reviewed it. Have a German tax adviser (Steuerberater) check any figure before filing or acting on it.

Collection period (Erhebungszeitraum) 2026 is the calendar year 2026 ([§ 14 GewStG](https://www.gesetze-im-internet.de/gewstg/__14.html)). Trade tax is a municipal tax with two authorities. The tax office sets the base amount in the Gewerbesteuermessbescheid, and that notice also decides whether the business is liable at all ([§ 184(1) AO](https://www.gesetze-im-internet.de/ao_1977/__184.html)). The municipality applies its multiplier, issues the trade tax notice and collects the tax ([§ 16(1) GewStG](https://www.gesetze-im-internet.de/gewstg/__16.html)).

This skill does not repeat the profit computation. The owner's profit comes from `de-self-employed-income-tax` or `de-income-tax` (Anlage G), a partnership's from `de-partners-and-part-year`, a company's from `de-corporate-tax`. Whether a self-employed person is a Freiberufler or a trader is triaged in `de-freelance-intake`.

## Who this applies to

| Who | Trade tax? | Where it says so |
| --- | --- | --- |
| A standing commercial business (Gewerbebetrieb) with a permanent establishment in Germany. Commercial means an independent, lasting activity, run for profit and open to the general market, that is not farming or forestry, not a free profession and not other self-employed work | Yes | [§ 2(1) GewStG](https://www.gesetze-im-internet.de/gewstg/__2.html), [§ 15(2) EStG](https://www.gesetze-im-internet.de/estg/__15.html) |
| Free professions of a natural person: independent scientific, artistic, writing, teaching or educational work, and the named professions (doctors, dentists, vets, lawyers, notaries, patent attorneys, surveyors, engineers, architects, commercial chemists, auditors, tax advisers, consulting economists, sworn accountants, tax agents, Heilpraktiker, Dentisten, physiotherapists, journalists, photo reporters, interpreters, translators, pilots) and similar professions | No | [§ 18(1) no. 1 EStG](https://www.gesetze-im-internet.de/estg/__18.html) |
| Farming and forestry; other self-employed work (for example executor, asset manager, supervisory board member) | No | [§ 15(2) EStG](https://www.gesetze-im-internet.de/estg/__15.html), [§ 18 EStG](https://www.gesetze-im-internet.de/estg/__18.html) |
| Capital companies (GmbH, UG, AG, KGaA, SE), cooperatives, mutual insurance and pension associations | Yes, "stets und in vollem Umfang" (always and in full), whatever they do. A GmbH of architects pays | [§ 2(2) GewStG](https://www.gesetze-im-internet.de/gewstg/__2.html) |
| A partnership that has opted to be taxed as a company (§ 1a KStG) | Yes, treated as a capital company | [§ 2(8) GewStG](https://www.gesetze-im-internet.de/gewstg/__2.html) |
| Other private-law legal persons and associations | Only as far as they run a commercial operation (wirtschaftlicher Geschäftsbetrieb), farming excepted | [§ 2(3) GewStG](https://www.gesetze-im-internet.de/gewstg/__2.html) |
| A partnership that also carries on any commercial activity of its own | Yes: the whole activity counts as commercial (Abfärbung). The statute prints no minimum amount | [§ 15(3) no. 1 EStG](https://www.gesetze-im-internet.de/estg/__15.html) |
| A partnership whose only personally liable partners are companies and which only they or non-partners manage (gewerblich geprägt) | Yes, in full | [§ 15(3) no. 2 EStG](https://www.gesetze-im-internet.de/estg/__15.html) |
| A partnership with no commercial activity of its own that holds a share in a commercial partnership | For trade tax, the states' decree of 5 November 2025 applies the Federal Fiscal Court ruling of 6 June 2019 (IV R 30/16) "in allen offenen Fällen über den entschiedenen Einzelfall hinaus". Refer | [State decree, 5 Nov 2025](https://www.bundesfinanzministerium.de/Content/DE/Standardartikel/Themen/Steuern/Steuerarten/Gewerbesteuer/2025-11-05-gle-aufhebung-gle-01-10-20-anl.pdf?__blob=publicationFile&v=3) |
| Travelling trade (Reisegewerbe, needs a Reisegewerbekarte) | Yes; the municipality at the centre of the activity levies it | [§ 35a GewStG](https://www.gesetze-im-internet.de/gewstg/__35a.html) |
| Exempt businesses, for example one whose only activity is producing and selling power from a solar plant on, at or in a building of up to 30 kilowatts | No, as far as the list goes | [§ 3 no. 32 GewStG](https://www.gesetze-im-internet.de/gewstg/__3.html) |

- **Who owes the tax.** The entrepreneur for whose account the business runs. If a partnership runs it, the partnership owes the tax, not the partners ([§ 5(1) GewStG](https://www.gesetze-im-internet.de/gewstg/__5.html)). If a business passes as a whole to a new owner, the old owner owes the tax up to the transfer ([§ 5(2)](https://www.gesetze-im-internet.de/gewstg/__5.html), [§ 2(5) GewStG](https://www.gesetze-im-internet.de/gewstg/__2.html)).
- **Liability follows the activity, not the registration.** Opening a commercial business is notified to the municipality, which tells the tax office; a free profession is notified to the tax office. The tax registration questionnaire goes to the tax office electronically, within one month of the event ([§ 138(1), (1b), (4) AO](https://www.gesetze-im-internet.de/ao_1977/__138.html)).
- **Temporary breaks** caused by the nature of the business do not end liability ([§ 2(4) GewStG](https://www.gesetze-im-internet.de/gewstg/__2.html)).
- **IT consultants and software developers** are not named in § 18 EStG. The facts decide; selling software or hardware points to a commercial business. Flag it.
- **Refer these cases:** a group with a profit-transfer agreement (Organschaft: the subsidiary counts as a permanent establishment of the parent, [§ 2(2) sentence 2 GewStG](https://www.gesetze-im-internet.de/gewstg/__2.html)); shipping, banks and insurers; and reclassification after an audit (a free profession treated as commercial for open years: the base amount and trade tax follow, and the § 35 credit follows those notices).
- **Abfärbung is a partnership rule.** § 15(3) no. 1 EStG names partnerships only. A sole trader with a free profession and a separate commercial side line has two activities, and only the commercial one pays trade tax.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
| --- | --- | --- | --- |
| Rounding of trade income | Down to full EUR 100 | 2026 | [§ 11(1) GewStG](https://www.gesetze-im-internet.de/gewstg/__11.html) |
| Allowance (Freibetrag), natural persons and partnerships | EUR 24,500, at most the rounded trade income | 2026 | [§ 11(1) no. 1 GewStG](https://www.gesetze-im-internet.de/gewstg/__11.html) |
| Allowance, § 2(3) bodies, certain partly exempt bodies, businesses of public-law persons | EUR 5,000 | 2026 | [§ 11(1) no. 2 GewStG](https://www.gesetze-im-internet.de/gewstg/__11.html) |
| Allowance, capital companies | None | 2026 | [§ 11(1) GewStG](https://www.gesetze-im-internet.de/gewstg/__11.html) names none |
| Base rate (Steuermesszahl) | 3.5% of trade income | 2026 | [§ 11(2) GewStG](https://www.gesetze-im-internet.de/gewstg/__11.html) |
| Base rate, home workers (Hausgewerbetreibende) | Reduced to 56% of the normal rate | 2026 | [§ 11(3) GewStG](https://www.gesetze-im-internet.de/gewstg/__11.html) |
| Multiplier (Hebesatz) floor | 200% where the municipality has set none higher | 2026 | Old wording of [§ 16(4) GewStG](https://www.gesetze-im-internet.de/gewstg/__16.html), which BGBl. 2026 I Nr. 197, Art. 8, changes from "200" to "280" only from 2027 ([BGBl.](https://www.recht.bund.de/bgbl/1/2026/197/VO.html)); [BMF "Steuern von A bis Z"](https://www.bundesfinanzministerium.de/Content/DE/Downloads/Broschueren_Bestellservice/steuern-von-a-z.pdf?__blob=publicationFile&v=9): "Er beträgt mindestens 200 Prozent" |
| Multiplier floor from 2027 | 280% | from 2027 | [§ 16(4) GewStG](https://www.gesetze-im-internet.de/gewstg/__16.html), [§ 36(5b) GewStG](https://www.gesetze-im-internet.de/gewstg/__36.html): "erstmals für den Erhebungszeitraum 2027" |
| Multiplier example: Munich | 490% | current (read 2026-10-24) | [City of Munich, Gewerbesteuer](https://stadt.muenchen.de/service/info/gewerbesteuer/1074725/) |
| Multiplier example: average of all German municipalities | 410% | 2025 | [Destatis press release 369, October 2026](https://www.destatis.de/DE/Presse/Pressemitteilungen/2026/10/PD26_369_712.html) |
| Financing add-back allowance | EUR 200,000 on the sum of financing items; one quarter of the excess is added | 2026 | [§ 8 no. 1 GewStG](https://www.gesetze-im-internet.de/gewstg/__8.html) |
| Participation exemption threshold | At least 15% at the start of the period | 2026 | [§ 9 no. 2a, no. 7 GewStG](https://www.gesetze-im-internet.de/gewstg/__9.html) |
| Loss use | EUR 1 million in full, then up to 60% of the excess | 2026 | [§ 10a GewStG](https://www.gesetze-im-internet.de/gewstg/__10a.html) |
| Wages deemed for working owners in apportionment (not a legal person) | EUR 25,000 a year in total | 2026 | [§ 31(5) GewStG](https://www.gesetze-im-internet.de/gewstg/__31.html) |
| Income tax credit | 4.0 times the base amount, capped | 2026 | [§ 35(1) EStG](https://www.gesetze-im-internet.de/estg/__35.html) |
| Minimum single prepayment | EUR 50 | 2026 | [§ 19(5) GewStG](https://www.gesetze-im-internet.de/gewstg/__19.html) |
| Return required if trade income is more than | EUR 24,500 | 2026 | [§ 25(1) no. 1 GewStDV](https://www.gesetze-im-internet.de/gewstdv_1955/__25.html) |

- **Multipliers differ by town.** The decision for a year is taken by 30 June with effect from 1 January; after that it can only be set at or below the last level. It is the same for every business in the municipality ([§ 16(3), (4) GewStG](https://www.gesetze-im-internet.de/gewstg/__16.html)). Always read the rate from the client's own notice or the municipality's decision for the year. The Munich and average figures are examples only.
- **No combined rate.** Do not quote a "combined" or "effective" rate for an individual. The § 35 credit has two caps (below), so only the client's own figures give the real burden. For companies, `de-corporate-tax` gives the corporate burden.

## The taxable base

**1. Start from the profit.** Trade income (Gewerbeertrag) is the profit under income tax or corporation tax rules for the matching year, plus § 8 add-backs, minus § 9 reductions ([§ 7 GewStG](https://www.gesetze-im-internet.de/gewstg/__7.html)). Trade tax is not a business expense, so the profit is before trade tax ([§ 4(5b) EStG](https://www.gesetze-im-internet.de/estg/__4.html)). For a partnership the profit includes partners' pay for work, loans and assets let to it ([§ 15(1) no. 2 EStG](https://www.gesetze-im-internet.de/estg/__15.html)). Gains on selling a partnership business or share count, unless they fall to a natural person who is a direct partner (§ 7 sentence 2). A business with HGB books and a different financial year counts the profit in the period in which the financial year ends ([§ 10(2) GewStG](https://www.gesetze-im-internet.de/gewstg/__10.html)). If liability does not last the whole year, the period is shortened ([§ 14 GewStG](https://www.gesetze-im-internet.de/gewstg/__14.html)); § 11 does not cut the allowance for a short period.

**2. Add back (Hinzurechnungen, [§ 8 GewStG](https://www.gesetze-im-internet.de/gewstg/__8.html)),** only as far as the items reduced the profit. The financing items of § 8 no. 1 go in at their own shares:

| § 8 no. 1 item | Share in the sum |
| --- | --- |
| a) Interest and other payments for debt, including discounts outside the ordinary course of business and discount amounts on selling receivables | in full |
| b) Annuities and permanent burdens (not pensions under a direct employer promise) | in full |
| c) Profit shares of a silent partner | in full |
| d) Rent and leasing for movable fixed assets owned by someone else | one fifth; half of that for electric vehicles, qualifying plug-in hybrids and bicycles that are not motor vehicles |
| e) Rent and leasing for immovable fixed assets owned by someone else | one half |
| f) Time-limited use of rights (licences, concessions), except licences that only allow passing derived rights on, and amounts that are the base for the artists' social levy | one quarter |

Sum the items, subtract EUR 200,000 ("soweit die Summe den Betrag von 200 000 Euro übersteigt"), and add back one quarter of the excess. At or below EUR 200,000 nothing is added. The halved share for electric vehicles applies only to contracts made after 31 December 2019; for contracts made before 1 January 2025 a 60 km electric range is enough instead of 80 km; it applies for the last time in 2030 ([§ 36(4) GewStG](https://www.gesetze-im-internet.de/gewstg/__36.html)). The other add-backs: KGaA general partners' shares (no. 4); dividends exempt under § 3 no. 40 EStG or § 8b KStG from holdings that miss the § 9 test (no. 5); loss shares from partnerships (no. 8); corporate donations (no. 9); write-downs on company shares linked to exempt dividends (no. 10); certain foreign taxes (no. 12). Refer these.

**3. Reduce (Kürzungen, [§ 9 GewStG](https://www.gesetze-im-internet.de/gewstg/__9.html)).**

| Reduction | Rule and condition |
| --- | --- |
| Property (no. 1 sentence 1) | The Grundsteuer booked as a business expense in the period, for real property that belongs to the entrepreneur's business assets. This wording first applies for collection period 2025 ([§ 36(4b) GewStG](https://www.gesetze-im-internet.de/gewstg/__36.html)); for 2024 and earlier the old wording applies. Rented premises give no reduction |
| Extended property reduction (no. 1 sentences 2 to 6) | On request, for businesses that only manage their own real property (and capital): the trade income from that property. Narrow limits (20% for power supply, 5% for other tenant services). Refer |
| Partnership shares (no. 2) | Profit shares from a partnership of co-entrepreneurs, if counted in the profit. The partnership pays its own trade tax |
| German company dividends (no. 2a) | Dividends from a non-exempt German company, if the holding is "mindestens 15 Prozent" at the start of the period, less directly related expenses |
| Foreign permanent establishment (no. 3) | Trade income of a permanent establishment abroad (see Cross-border points) |
| Donations (no. 5) | Donations for tax-privileged purposes (§§ 52 to 54 AO) from business funds, up to 20% of the profit (plus the § 8 no. 9 add-back) or 4 per mille of turnover plus wages; excess carries forward |
| Foreign company dividends (no. 7, no. 8) | Holding of at least 15% (no. 7: at the start of the period); a lower treaty threshold prevails. Refer |

**4. Deduct trade losses ([§ 10a GewStG](https://www.gesetze-im-internet.de/gewstg/__10a.html)).** Losses of earlier periods reduce trade income in full up to EUR 1 million, and above that up to 60% of the excess. The rest carries forward. There is no carry-back, and § 10d EStG does not apply. The loss left at the end of each period is determined separately. In a partnership, losses and the EUR 1 million are split by the general profit-sharing key, without advance shares. A new owner cannot use the losses of a business taken over as a whole (§ 10a sentence 8). For companies, § 8c and § 8d KStG apply; refer changes of partners or shareholders. The Federal Constitutional Court held sentences 1 and 2 compatible with the Basic Law (decision of 23 July 2025, 2 BvL 19/14, noted on the statute page).

**5. Round, allow, apply the base rate.** Round trade income down to full EUR 100, subtract the allowance (never below zero), and multiply by 3.5% to get the base amount (Steuermessbetrag) ([§ 11 GewStG](https://www.gesetze-im-internet.de/gewstg/__11.html)).

**6. Apportion between municipalities (Zerlegung).** If the business had permanent establishments in more than one municipality during the period, or one establishment spans two, or it moved, the tax office splits the base amount ([§ 28(1) GewStG](https://www.gesetze-im-internet.de/gewstg/__28.html)). The key is wages paid at each establishment, rounded down to full EUR 1,000 ([§ 29 GewStG](https://www.gesetze-im-internet.de/gewstg/__29.html)). Where the business is not run by a legal person, EUR 25,000 a year in total is added as wages for the working owners ([§ 31(5) GewStG](https://www.gesetze-im-internet.de/gewstg/__31.html)). Wind, solar and storage businesses use installed capacity for nine tenths (§ 29(1) no. 2 and 3). Each municipality then applies its own multiplier to its share ([§ 4(1) GewStG](https://www.gesetze-im-internet.de/gewstg/__4.html)).

**7. Multiply** each share by the municipality's multiplier. The result is the trade tax ([§ 16(1) GewStG](https://www.gesetze-im-internet.de/gewstg/__16.html)).

**8. The income tax credit ([§ 35 EStG](https://www.gesetze-im-internet.de/estg/__35.html)).** A sole trader, a partner in a commercial partnership and a KGaA general partner reduce their income tax by the lowest of:

1. **Four times the base amount** set for the matching period ("das Vierfache"); for a partner, four times the partner's share.
2. **The trade tax actually payable**: "Der Abzug des Steuerermäßigungsbetrags ist auf die tatsächlich zu zahlende Gewerbesteuer beschränkt" (§ 35(1) sentence 5).
3. **The maximum reduction amount (Ermäßigungshöchstbetrag)**: positive commercial income divided by all positive income, times the reduced tariff tax.

- **At a low multiplier the credit is capped.** At the 200% floor, a base amount of EUR 1,942.50 gives trade tax of EUR 3,885, while four times the base amount is EUR 7,770. The credit is EUR 3,885. An unused credit is lost: § 35 has no carry-forward or refund.
- **Partners.** The share follows the general profit-sharing key, without advance shares, as a percentage with two decimals; the base amount, the tax payable and the shares are determined separately and uniformly (§ 35(2) EStG). The base amount notice and the trade tax notice are Grundlagenbescheide for the credit (§ 35(3) EStG): if they change, the income tax follows.
- **Church tax is not reduced.** "§ 35 ist bei der Ermittlung der festzusetzenden Einkommensteuer nach Satz 1 nicht anzuwenden" ([§ 51a(2) EStG](https://www.gesetze-im-internet.de/estg/__51a.html)). Church tax is "je nach Bundesland 8 oder 9 Prozent" of income tax ([BMF booklet](https://www.bundesfinanzministerium.de/Content/DE/Downloads/Broschueren_Bestellservice/steuern-von-a-z.pdf?__blob=publicationFile&v=9)).
- **Solidarity surcharge is computed after the credit.** Its base is the income tax to be assessed under [§ 2(6) EStG](https://www.gesetze-im-internet.de/estg/__2.html), which is the tariff tax "vermindert um ... die Steuerermäßigungen" (§ 35 is one). [§ 3(1) no. 1, (2) SolzG](https://www.gesetze-im-internet.de/solzg_1995/__3.html) departs from § 2(6) only for the child allowances, so the § 35 credit also lowers the surcharge. Church tax is the exception, by the express rule above.
- **Companies get no credit.** A GmbH pays trade tax on top of corporation tax (see `de-corporate-tax`).

## Deadlines and filing

**Who must file** ([§ 25(1) GewStDV](https://www.gesetze-im-internet.de/gewstdv_1955/__25.html)): every liable business whose trade income "den Betrag von 24 500 Euro überstiegen hat"; every non-exempt capital company and cooperative, whatever the amount; a business with a loss carry-forward determined at the end of the last period; any business the tax office asks. A sole trader at or below EUR 24,500 with no loss carry-forward and no request files nothing. Note the test is on trade income before rounding: EUR 24,580 rounds to EUR 24,500, gives no tax, yet a return is due.

**What.** A declaration for setting the base amount and, where § 28 applies, an apportionment declaration, sent electronically in the official data format. On request the tax office can accept a signed paper form to avoid undue hardship ([§ 14a GewStG](https://www.gesetze-im-internet.de/gewstg/__14a.html)).

| Deadline | Collection period 2026 | Source |
| --- | --- | --- |
| Without an adviser: seven months after the year end | 31 July 2027 is a Saturday, so Monday 2 August 2027 | [§ 149(2) AO](https://www.gesetze-im-internet.de/ao_1977/__149.html), [§ 108(3) AO](https://www.gesetze-im-internet.de/ao_1977/__108.html) |
| With a Steuerberater (§ 149(3) no. 3 names this return) | Last day of February of the second year after: Tuesday 29 February 2028 | [§ 149(3) AO](https://www.gesetze-im-internet.de/ao_1977/__149.html) |
| Earlier call-in of an advised return | The tax office may order an earlier date | [§ 149(4) AO](https://www.gesetze-im-internet.de/ao_1977/__149.html) |
| Prepayments | 15 February, 15 May, 15 August, 15 November | [§ 19(1) GewStG](https://www.gesetze-im-internet.de/gewstg/__19.html) |
| Balance | Within one month of the trade tax notice; at once for prepayments already due and unpaid | [§ 20(2) GewStG](https://www.gesetze-im-internet.de/gewstg/__20.html) |

- **Prepayments.** Each is in principle one quarter ("ein Viertel") of the tax at the last assessment, rounded down to full euros, and set only if at least EUR 50 ([§ 19(2), (5) GewStG](https://www.gesetze-im-internet.de/gewstg/__19.html)). With a different financial year they are paid during the financial year ending in the period (businesses founded or switched after 31 December 1985).
- **Adjustment.** The municipality may adjust prepayments to the expected tax until the end of the 15th month after the period; an increase is due within one month of the notice. The tax office may set an expected base amount, which binds the municipality. A new business is set up the same way ([§ 19(3), (4) GewStG](https://www.gesetze-im-internet.de/gewstg/__19.html)). If prepayments look too high, ask the municipality to adjust them.
- **Settlement.** Prepayments are credited; an overpayment is set off or refunded after the notice ([§ 20 GewStG](https://www.gesetze-im-internet.de/gewstg/__20.html)).
- **Objections** to liability or the amount of the base go to the tax office, against the Messbescheid; the municipality is bound by it ([§ 184(1) AO](https://www.gesetze-im-internet.de/ao_1977/__184.html)). Only the multiplier step is the municipality's.

**Returns for 2025 being filed now.** The same allowance, base rate, add-back allowance, loss rule and § 35 factor applied; the Grundsteuer reduction first applied for 2025; the floor was 200%. Without an adviser the 2025 return was due on Friday 31 July 2026, so it is now late. With a Steuerberater the deadline is the last day of February 2027; 28 February 2027 is a Sunday, so Monday 1 March 2027 ([§ 108(3) AO](https://www.gesetze-im-internet.de/ao_1977/__108.html)). The Corona-era extensions stop at period 2024 ([Art. 97 § 36 EGAO](https://www.gesetze-im-internet.de/aoeg_1977/art_97__36.html)).

## Penalties and interest

The AO rules apply to trade tax administered by a municipality ([§ 1(2) AO](https://www.gesetze-im-internet.de/ao_1977/__1.html)).

| Charge | Amount | Source |
| --- | --- | --- |
| Late filing surcharge, base amount return and apportionment declaration | EUR 25 per started month of delay | [§ 152(6) AO](https://www.gesetze-im-internet.de/ao_1977/__152.html) |
| Highest late filing surcharge | EUR 25,000 | [§ 152(10) AO](https://www.gesetze-im-internet.de/ao_1977/__152.html) |
| Late payment surcharge (Säumniszuschlag) | 1% per started month, on the overdue tax rounded down to a multiple of EUR 50; none for a delay of up to three days | [§ 240(1), (3) AO](https://www.gesetze-im-internet.de/ao_1977/__240.html) |
| Interest on an assessment difference (either way) | 0.15% a month (1.8% a year), from 15 months after the end of the year | [§ 233a AO](https://www.gesetze-im-internet.de/ao_1977/__233a.html), [§ 238(1a) AO](https://www.gesetze-im-internet.de/ao_1977/__238.html) |

- **Late filing.** The surcharge is discretionary, but must be set if the return is not filed within 14 months after the year end, or by the call-in date ([§ 152(2) AO](https://www.gesetze-im-internet.de/ao_1977/__152.html)). For this return § 152(6) carries over only § 152(3) no. 1 (an extended deadline), not the let-outs for nil tax or tax covered by prepayments. Example: three months and five days late is four started months, EUR 100. The surcharge goes to the municipality without the multiplier ([§ 14b GewStG](https://www.gesetze-im-internet.de/gewstg/__14b.html)).
- **Late payment example.** EUR 1,234.56 overdue rounds down to EUR 1,200: EUR 12 per started month.
- **Interest** does not apply to prepayments (§ 233a(1) AO).

## Cross-border points

- **Germany only.** Trade tax reaches a business only as far as it has a permanent establishment in Germany, including a German-registered merchant ship ([§ 2(1) GewStG](https://www.gesetze-im-internet.de/gewstg/__2.html)). Germany's share of the exclusive economic zone and continental shelf counts for the activities listed in § 2(7).
- **Foreign businesses with a German establishment** pay trade tax on it like anyone else. Only if the management is in a state with no tax treaty, the income is exempt under limited income tax liability and that state grants reciprocity (or has no similar tax), is the establishment exempt ([§ 2(6) GewStG](https://www.gesetze-im-internet.de/gewstg/__2.html)). The corporation or income tax side is in `de-non-resident-tax` and `de-corporate-tax`.
- **German businesses with an establishment abroad** reduce trade income by the part that falls on it ([§ 9 no. 3 GewStG](https://www.gesetze-im-internet.de/gewstg/__9.html)), except income under § 7 sentences 7 and 8 (controlled foreign company and passive establishment income), which stays in trade income ([§ 7 GewStG](https://www.gesetze-im-internet.de/gewstg/__7.html)).
- **Foreign dividends** are reduced only with a holding of at least 15% (§ 9 no. 7, no. 8); below it the exempt part is added back (§ 8 no. 5). Foreign taxes deducted under § 34c EStG on income left out of trade income are added back (§ 8 no. 12).
- **Moving the business** between municipalities in the year triggers apportionment (§ 28(1) sentence 2). Moving the owner abroad: see `leaving-germany-exit-tax` for shares and `de-non-resident-tax` for income.

## Worked examples

**Example 1: sole trader in Munich, ordinary costs.** A trader runs a shop in Munich. Profit before trade tax EUR 80,000. Loan interest EUR 12,000 (in full), shop rent EUR 36,000 (one half, EUR 18,000), leasing of a petrol car EUR 10,000 (one fifth, EUR 2,000). The financing sum is EUR 32,000, not above EUR 200,000, so nothing is added back. No § 9 reductions. Trade income EUR 80,000 is already a full EUR 100. Less the allowance of EUR 24,500 leaves EUR 55,500. Times 3.5% gives a base amount of EUR 1,942.50. Munich's multiplier of 490% gives trade tax of EUR 9,518.25. The § 35 credit is four times the base amount, EUR 7,770, which is below the trade tax; assuming the income tax on the commercial income is at least that, the credit is EUR 7,770 and EUR 1,748.25 of trade tax stays a cost. Next year's prepayments are one quarter of EUR 9,518.25, rounded down: EUR 2,379 on each date.

```oa-check
name: Sole trader in Munich, profit EUR 80,000 (2026)
inputs:
  profit: 80000
  interest: 12000
  shop_rent: 36000
  car_lease: 10000
  allowance: 24500
  multiplier: 490
steps:
  - financing_sum: interest + shop_rent / 2 + car_lease / 5
  - add_back: max(financing_sum - 200000, 0) / 4
  - trade_income: profit + add_back
  - rounded: floor(trade_income / 100) * 100
  - taxable: max(rounded - allowance, 0)
  - base_amount: taxable * 0.035
  - trade_tax: base_amount * multiplier / 100
  - credit: min(4 * base_amount, trade_tax)
  - not_offset: trade_tax - credit
  - prepayment: floor(trade_tax / 4)
expected:
  financing_sum: 32000
  add_back: 0
  base_amount: 1942.50
  trade_tax: 9518.25
  credit: 7770.00
  not_offset: 1748.25
  prepayment: 2379
```

**Example 2: partnership above the add-back allowance, with a property and old losses.** A KG (two equal partners) has profit of EUR 1,400,000. It paid interest of EUR 180,000 (in full) and warehouse rent of EUR 120,000 (one half, EUR 60,000): sum EUR 240,000, excess over EUR 200,000 is EUR 40,000, one quarter, EUR 10,000, is added. It owns its office building and booked Grundsteuer of EUR 6,000, which is deducted. Trade income before losses is EUR 1,404,000. Losses brought forward are EUR 2,000,000. It deducts EUR 1,000,000 in full plus 60% of the EUR 404,000 above it (EUR 242,400): EUR 1,242,400 in all. Trade income left is EUR 161,600; EUR 757,600 of loss carries forward. Less the EUR 24,500 allowance leaves EUR 137,100, and 3.5% gives a base amount of EUR 4,798.50. Assume the municipality's multiplier is 410% (the 2025 national average): trade tax EUR 19,673.85. Each partner's 50% share of the base amount is EUR 2,399.25, so each partner's § 35 credit is capped first at EUR 9,597 (four times the share), which is below the partner's half of the tax payable.

```oa-check
name: KG with add-back, Grundsteuer and loss carry-forward (2026)
inputs:
  profit: 1400000
  interest: 180000
  warehouse_rent: 120000
  grundsteuer: 6000
  losses_bf: 2000000
  allowance: 24500
  multiplier: 410
  partner_share: 0.5
steps:
  - financing_sum: interest + warehouse_rent / 2
  - add_back: max(financing_sum - 200000, 0) / 4
  - before_losses: profit + add_back - grundsteuer
  - loss_limit: min(before_losses, 1000000) + max(before_losses - 1000000, 0) * 0.6
  - loss_used: min(losses_bf, loss_limit)
  - trade_income: before_losses - loss_used
  - loss_cf: losses_bf - loss_used
  - rounded: floor(trade_income / 100) * 100
  - base_amount: max(rounded - allowance, 0) * 0.035
  - trade_tax: base_amount * multiplier / 100
  - partner_credit_cap: 4 * base_amount * partner_share
expected:
  add_back: 10000
  before_losses: 1404000
  loss_used: 1242400
  loss_cf: 757600
  base_amount: 4798.50
  trade_tax: 19673.85
  partner_credit_cap: 9597.00
```

## Ask the client first

- What exactly does the business do, and is it run alone, in a partnership or through a company? Does any part involve selling goods or reselling others' products? (Decides liability.)
- In which municipalities did it have premises in 2026, and did it move? Which multiplier is on the last trade tax notice? (Decides the multiplier and any apportionment.)
- What did it pay in the year for interest, annuities, silent partners, rent and leasing (movable and immovable separately) and licences? (Decides the § 8 add-back.)
- Does it own real property with Grundsteuer booked as an expense, hold shares in partnerships or companies (and what percentage at 1 January), or make donations? (Decides § 9.)
- Was a trade loss carry-forward determined at the end of 2025? (Decides § 10a and the return duty.)
- Is a Steuerberater preparing the return, and what other income does the owner have? (Decides the deadline and the § 35 cap.)

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| GewStG § 2 (liability, inland, foreign management) | https://www.gesetze-im-internet.de/gewstg/__2.html | 2026-10-24 |
| GewStG § 3 (exemptions, no. 32 solar) | https://www.gesetze-im-internet.de/gewstg/__3.html | 2026-10-24 |
| GewStG § 4 (municipality entitled) | https://www.gesetze-im-internet.de/gewstg/__4.html | 2026-10-24 |
| GewStG § 5 (who owes the tax) | https://www.gesetze-im-internet.de/gewstg/__5.html | 2026-10-24 |
| GewStG § 7 (trade income) | https://www.gesetze-im-internet.de/gewstg/__7.html | 2026-10-24 |
| GewStG § 8 (add-backs, EUR 200,000) | https://www.gesetze-im-internet.de/gewstg/__8.html | 2026-10-24 |
| GewStG § 9 (reductions, 15%) | https://www.gesetze-im-internet.de/gewstg/__9.html | 2026-10-24 |
| GewStG § 10 (period of income) | https://www.gesetze-im-internet.de/gewstg/__10.html | 2026-10-24 |
| GewStG § 10a (losses, EUR 1m and 60%) | https://www.gesetze-im-internet.de/gewstg/__10a.html | 2026-10-24 |
| GewStG § 11 (EUR 24,500, 3.5%) | https://www.gesetze-im-internet.de/gewstg/__11.html | 2026-10-24 |
| GewStG § 14 (collection period) | https://www.gesetze-im-internet.de/gewstg/__14.html | 2026-10-24 |
| GewStG § 14a (electronic return) | https://www.gesetze-im-internet.de/gewstg/__14a.html | 2026-10-24 |
| GewStG § 14b (late filing surcharge to municipality) | https://www.gesetze-im-internet.de/gewstg/__14b.html | 2026-10-24 |
| GewStG § 16 (multiplier, 280% from 2027) | https://www.gesetze-im-internet.de/gewstg/__16.html | 2026-10-24 |
| GewStG § 19 (prepayments) | https://www.gesetze-im-internet.de/gewstg/__19.html | 2026-10-24 |
| GewStG § 20 (settlement) | https://www.gesetze-im-internet.de/gewstg/__20.html | 2026-10-24 |
| GewStG § 28 (apportionment) | https://www.gesetze-im-internet.de/gewstg/__28.html | 2026-10-24 |
| GewStG § 29 (apportionment key) | https://www.gesetze-im-internet.de/gewstg/__29.html | 2026-10-24 |
| GewStG § 31 (wages, EUR 25,000 for owners) | https://www.gesetze-im-internet.de/gewstg/__31.html | 2026-10-24 |
| GewStG § 35a (travelling trade) | https://www.gesetze-im-internet.de/gewstg/__35a.html | 2026-10-24 |
| GewStG § 36 (application dates) | https://www.gesetze-im-internet.de/gewstg/__36.html | 2026-10-24 |
| GewStDV § 25 (who files) | https://www.gesetze-im-internet.de/gewstdv_1955/__25.html | 2026-10-24 |
| EStG § 2(6) (income tax to be assessed, after Steuerermäßigungen) | https://www.gesetze-im-internet.de/estg/__2.html | 2026-10-24 |
| EStG § 4(5b) (trade tax not deductible) | https://www.gesetze-im-internet.de/estg/__4.html | 2026-10-24 |
| EStG § 15 (commercial business, partnerships) | https://www.gesetze-im-internet.de/estg/__15.html | 2026-10-24 |
| EStG § 18 (free professions) | https://www.gesetze-im-internet.de/estg/__18.html | 2026-10-24 |
| EStG § 35 (credit) | https://www.gesetze-im-internet.de/estg/__35.html | 2026-10-24 |
| EStG § 51a (church tax) | https://www.gesetze-im-internet.de/estg/__51a.html | 2026-10-24 |
| SolzG § 3 (surcharge base) | https://www.gesetze-im-internet.de/solzg_1995/__3.html | 2026-10-24 |
| AO § 1, § 108, § 138, § 149, § 152, § 184, § 233a, § 238, § 240 | https://www.gesetze-im-internet.de/ao_1977/ | 2026-10-24 |
| EGAO Art. 97 § 36 (Corona extensions) | https://www.gesetze-im-internet.de/aoeg_1977/art_97__36.html | 2026-10-24 |
| BGBl. 2026 I Nr. 197, Art. 8 (floor 200 to 280 from 2027) | https://www.recht.bund.de/bgbl/1/2026/197/VO.html | 2026-10-24 |
| BMF "Steuern von A bis Z", Ausgabe 2025 (floor 200%, church tax 8 or 9%) | https://www.bundesfinanzministerium.de/Content/DE/Downloads/Broschueren_Bestellservice/steuern-von-a-z.pdf?__blob=publicationFile&v=9 | 2026-10-24 |
| States' decree of 5 November 2025 (partnership holding a commercial share) | https://www.bundesfinanzministerium.de/Content/DE/Standardartikel/Themen/Steuern/Steuerarten/Gewerbesteuer/2025-11-05-gle-aufhebung-gle-01-10-20-anl.pdf?__blob=publicationFile&v=3 | 2026-10-24 |
| Destatis press release 369, October 2026 (average multiplier 2025: 410%) | https://www.destatis.de/DE/Presse/Pressemitteilungen/2026/10/PD26_369_712.html | 2026-10-24 |
| City of Munich, Gewerbesteuer (multiplier 490%) | https://stadt.muenchen.de/service/info/gewerbesteuer/1074725/ | 2026-10-24 |

Not yet confirmed: the ELSTER form names GewSt 1 A and GewSt 1 D for 2026 (not read on ELSTER); any de minimis limit for Abfärbung under § 15(3) no. 1 EStG (case law, not in the statute); the Munich multiplier as a decision for 2026 specifically (the city page says "aktuell gültig" without a year).

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
