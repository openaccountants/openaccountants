---
name: de-corporate-tax
description: "German corporate income tax (Körperschaftsteuer, KSt) for tax year 2026: GmbH, UG, AG and other companies resident in Germany, and German permanent establishments of foreign companies. Covers the 15% rate under § 23 KStG and the enacted cuts from 2028, the 5.5% solidarity surcharge, how trade tax adds to the burden, the taxable base, the § 8b participation exemption, loss carry-forward (EUR 1m plus 70% for 2024 to 2027, 60% from 2028) and carry-back, § 8c share changes, Organschaft, the interest barrier, prepayments, filing deadlines, late filing surcharges, interest, and Kapitalertragsteuer on outbound dividends. Trigger on: Körperschaftsteuer, KSt, GmbH tax Germany, German corporate tax rate, Soli on KSt, § 8b KStG, § 8c KStG, Organschaft, Zinsschranke, Verlustvortrag GmbH, Mindestbesteuerung, KSt-Vorauszahlungen, Kapitalertragsteuer Dividende. Out of scope: trade tax detail (de-trade-tax), transfer pricing (germany-transfer-pricing), individual shareholders (de-income-tax, de-capital-gains), shareholder exit tax (leaving-germany-exit-tax), VAT (germany-vat-return)."
version: 0.2
jurisdiction: DE
tax_year: 2026
last_updated: 2026-10-29
authored_by: Ryan Duguid
review_status: pending_review
trust_label: Accountant-authored
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# German corporate income tax (Körperschaftsteuer): 2026

> **General reference only.** This skill is a source-cited draft. No accountant has reviewed it. Do not rely on it to file, pay or take a tax position without review by a qualified German tax adviser (Steuerberater).

Tax year: the calendar year 2026 (Veranlagungszeitraum 2026). A company with a financial year that does not match the calendar year is taxed on the profit of the financial year that ends in 2026 ([§ 7(4) KStG](https://www.gesetze-im-internet.de/kstg_1977/__7.html)). A German company pays three taxes on its profit: corporate income tax, the solidarity surcharge on that tax, and municipal trade tax. This skill covers the first two in full and summarises the third. For the trade tax method, use `de-trade-tax`.

## Who this applies to

- **Resident companies (unlimited tax liability).** A company is taxed in Germany on its worldwide income if its place of management (Geschäftsleitung) or its registered seat (Sitz) is in Germany ([§ 1(1) and (2) KStG](https://www.gesetze-im-internet.de/kstg_1977/__1.html)). This includes the GmbH (and its UG variant), the AG, the SE, the KGaA, cooperatives, other private-law legal persons, and commercial businesses of public bodies. "Place of management" means the centre of top-level management ([§ 10 AO](https://www.gesetze-im-internet.de/ao_1977/__10.html)); the seat is the place named in the articles ([§ 11 AO](https://www.gesetze-im-internet.de/ao_1977/__11.html)). A foreign-registered company run from Germany is therefore fully taxable here.
- **Non-resident companies (limited tax liability).** A company with neither its management nor its seat in Germany is taxed only on German-source income ([§ 2 no. 1 KStG](https://www.gesetze-im-internet.de/kstg_1977/__2.html)). The main case is a German permanent establishment (Betriebsstätte): any fixed place of business, such as a branch, office, workshop, warehouse, or a building site lasting more than six months ([§ 12 AO](https://www.gesetze-im-internet.de/ao_1977/__12.html)). A treaty may narrow this.
- **Out of scope here:**
  - Partnerships (OHG, KG, GmbH & Co. KG) are not subject to corporate tax unless they opt in under § 1a KStG. Their partners are taxed. A partnership does pay trade tax.
  - Bodies exempt under [§ 5 KStG](https://www.gesetze-im-internet.de/kstg_1977/__5.html) (for example charities) are not covered.
  - Banks, insurers, investment funds and REITs have special rules. Refer.
  - Groups with consolidated revenue of EUR 750 million or more also fall under the minimum tax law (see the rates table). This skill does not compute top-up tax.

## Rates, bands and thresholds

| Item | Rate or amount | Tax year | Source |
|---|---|---|---|
| Corporate income tax rate | 15% of taxable income | 2026 and 2027 ("Veranlagungszeiträume bis 2027 15 Prozent") | [§ 23(1) KStG](https://www.gesetze-im-internet.de/kstg_1977/__23.html) |
| Enacted rate cuts | 14% (2028), 13% (2029), 12% (2030), 11% (2031), 10% (2032 onwards) | 2028 to 2032 | [§ 23(1) KStG](https://www.gesetze-im-internet.de/kstg_1977/__23.html); [BMF Monatsbericht August 2025](https://www.bundesfinanzministerium.de/Monatsberichte/Ausgabe/2025/08/Inhalte/Kapitel-2-Fokus/investitionssofortprogramm-deutschland.html) |
| Small-company rate | None. One flat rate. The EUR 5,000 allowance in § 24 KStG does not apply to companies whose distributions are dividends | 2026 | [§ 24 KStG](https://www.gesetze-im-internet.de/kstg_1977/__24.html) |
| Solidarity surcharge (Solidaritätszuschlag) | 5.5% of the corporate income tax. The exemption threshold applies only to individuals, so a company pays from the first euro | 2026 | [§ 4 SolzG](https://www.gesetze-im-internet.de/solzg_1995/__4.html); [§ 3(1) and (3) SolzG](https://www.gesetze-im-internet.de/solzg_1995/__3.html) |
| Corporate tax plus surcharge | 15.825% (15% x 1.055) | 2026 | Computed from the two rows above |
| Trade tax (Gewerbesteuer) base rate | 3.5% of trade income, times the municipal multiplier (Hebesatz). Companies get no allowance (the EUR 24,500 allowance is for individuals and partnerships) | 2026 | [§ 11 GewStG](https://www.gesetze-im-internet.de/gewstg/__11.html); [§ 16 GewStG](https://www.gesetze-im-internet.de/gewstg/__16.html) |
| Trade tax multiplier floor | 200% in 2026; 280% from 2027 | 2026; 2027 | [BGBl. 2026 I Nr. 197](https://www.recht.bund.de/bgbl/1/2026/197/VO.html), law of 29 June 2026, Art. 8 no. 1: in § 16(4) sentence 2 GewStG "wird die Angabe „200“ durch die Angabe „280“ ersetzt", first applied for 2027 under [§ 36(5b) GewStG](https://www.gesetze-im-internet.de/gewstg/__36.html). So the text in force for 2026 is 200%. The current [§ 16(4) GewStG](https://www.gesetze-im-internet.de/gewstg/__16.html) page shows only the 2027 wording |
| Trade tax deductibility | Not a business expense | 2026 | [§ 4(5b) EStG](https://www.gesetze-im-internet.de/estg/__4.html) |
| Total burden, BMF figure | "knapp 30 Prozent" today, "knapp 25 Prozent" from 2032 | 2026; 2032 | [BMF Monatsbericht August 2025](https://www.bundesfinanzministerium.de/Monatsberichte/Ausgabe/2025/08/Inhalte/Kapitel-2-Fokus/investitionssofortprogramm-deutschland.html) |
| Participation exemption | Dividends and share gains exempt; 5% of each treated as a non-deductible expense, so 95% is effectively exempt | 2026 | [§ 8b(1)-(3), (5) KStG](https://www.gesetze-im-internet.de/kstg_1977/__8b.html) |
| Dividend exemption holding test | At least 10% directly at the start of the calendar year; acquisition of a participation of at least 10% is deemed to occur at that start | 2026 | [§ 8b(4) KStG](https://www.gesetze-im-internet.de/kstg_1977/__8b.html) |
| Loss carry-forward | EUR 1,000,000 in full, then 70% of income above that. The share falls back to 60% from 2028 | 70%: 2024 to 2027 (so 2026); 60%: 2028 onwards | [§ 10d(2) EStG](https://www.gesetze-im-internet.de/estg/__10d.html); [§ 52(18b) EStG](https://www.gesetze-im-internet.de/estg/__52.html); [BGBl. 2024 I Nr. 108](https://www.recht.bund.de/bgbl/1/2024/108/VO.html), Art. 6 ("70 Prozent" replaced by "60 Prozent", "erstmals für den Veranlagungszeitraum 2028") and Art. 35(9) ("Artikel 6 tritt am 1. Januar 2028 in Kraft") |
| Loss carry-back | Up to EUR 1,000,000, to the previous year, then the year before that | 2026 | [§ 10d(1) EStG](https://www.gesetze-im-internet.de/estg/__10d.html) |
| Trade tax loss carry-forward | EUR 1,000,000 in full, then 60% of the excess. No carry-back | 2026 | [§ 10a GewStG](https://www.gesetze-im-internet.de/gewstg/__10a.html) |
| Interest barrier (Zinsschranke) | Net interest deductible up to 30% of tax EBITDA; rule does not apply if net interest is less than EUR 3,000,000 | 2026 | [§ 4h(1), (2) EStG](https://www.gesetze-im-internet.de/estg/__4h.html) |
| Declining-balance depreciation | Up to 3 times the straight-line rate, max 30%, for movable assets bought or made after 30 June 2025 and before 1 January 2028 | 2026 | [§ 7(2) EStG](https://www.gesetze-im-internet.de/estg/__7.html) |
| Low-value assets | Immediate write-off up to EUR 800 net per item | 2026 | [§ 6(2) EStG](https://www.gesetze-im-internet.de/estg/__6.html) |
| Pillar Two | Minimum tax law (MinStG) applies to groups with EUR 750m+ revenue in two of the four prior years, for financial years beginning after 30 December 2023 | 2026 | [§ 1 MinStG](https://www.gesetze-im-internet.de/minstg/__1.html); [§ 101 MinStG](https://www.gesetze-im-internet.de/minstg/__101.html) |

**What applies for 2026, plainly.** The rate is 15% for 2026 and 2027. The law of 14 July 2025 for an immediate tax investment programme (Gesetz für ein steuerliches Investitionssofortprogramm) wrote the cuts into § 23 KStG; the first cut is for 2028. Do not apply 14% or lower to any 2026 or 2027 income.

**Trade tax in one paragraph.** Every GmbH or AG is a trade business in full ([§ 2(2) GewStG](https://www.gesetze-im-internet.de/gewstg/__2.html)). Trade income starts from the corporate tax profit, then adds back part of financing costs (interest, rent, leases, royalties above a EUR 200,000 allowance) and makes reductions (for example dividends from holdings of at least 15%). It is rounded down to full EUR 100, multiplied by 3.5%, then by the multiplier of each municipality where the company has an establishment. At a 400% multiplier the trade tax is 14% of trade income, which with 15.825% gives 29.825% in total. Multipliers differ widely by town: always read the client's own notice. A company gets no credit for trade tax against corporate tax (the § 35 EStG credit is for individuals only). Method, add-backs and reductions: see `de-trade-tax`.

## The taxable base

Income is worked out under the Income Tax Act and the KStG together ([§ 8(1) KStG](https://www.gesetze-im-internet.de/kstg_1977/__8.html)). For a GmbH or AG all income is business income ([§ 8(2) KStG](https://www.gesetze-im-internet.de/kstg_1977/__8.html)).

1. **Start** from the profit in the tax balance sheet (commercial accounts adjusted to tax rules).
2. **Add back non-deductible items:**
   - Corporate tax, solidarity surcharge and other taxes on income ([§ 10 no. 2 KStG](https://www.gesetze-im-internet.de/kstg_1977/__10.html)), and trade tax ([§ 4(5b) EStG](https://www.gesetze-im-internet.de/estg/__4.html)).
   - Half of supervisory board fees ([§ 10 no. 4 KStG](https://www.gesetze-im-internet.de/kstg_1977/__10.html)).
   - Criminal fines and similar ([§ 10 no. 3 KStG](https://www.gesetze-im-internet.de/kstg_1977/__10.html)) and the other limits in § 4(5) EStG (for example part of gifts and entertainment).
   - Hidden profit distributions (verdeckte Gewinnausschüttungen), such as excess salary or rent paid to a shareholder. They do not reduce income ([§ 8(3) KStG](https://www.gesetze-im-internet.de/kstg_1977/__8.html)). Pricing with related parties: see `germany-transfer-pricing`.
3. **Participation exemption ([§ 8b KStG](https://www.gesetze-im-internet.de/kstg_1977/__8b.html)).**
   - Dividends received are exempt, but 5% is added back as a non-deductible expense (§ 8b(1) and (5)). The direct holding test is at least 10% at the start of the calendar year. Under § 8b(4) sentence 6, acquisition of a participation of at least 10% is deemed to occur at the start of that year. Where the holding test, including that deeming rule, is not met, dividends are fully taxable (§ 8b(4)).
   - Gains on selling shares in a company are exempt with no minimum holding, again with 5% added back (§ 8b(2) and (3)). Losses and write-downs on such shares are not deductible (§ 8b(3)), and the same can apply to loans from a shareholder holding more than 25%.
4. **Depreciation.** Straight-line over useful life ([§ 7(1) EStG](https://www.gesetze-im-internet.de/estg/__7.html)). For movable assets acquired from 1 July 2025 to 31 December 2027 the company may choose declining balance at up to three times the straight-line rate, max 30% (§ 7(2) EStG). Items up to EUR 800 net can be written off at once ([§ 6(2) EStG](https://www.gesetze-im-internet.de/estg/__6.html)).
5. **Interest barrier ([§ 4h EStG](https://www.gesetze-im-internet.de/estg/__4h.html), [§ 8a KStG](https://www.gesetze-im-internet.de/kstg_1977/__8a.html)).**
   - Interest expense is deductible up to interest income. Net interest above that is deductible only up to 30% of tax EBITDA. Interest that cannot be deducted is carried forward (Zinsvortrag). Unused EBITDA capacity is carried forward five years.
   - The rule does not apply when net interest is **less than** EUR 3,000,000 (§ 4h(2)(a)). This is a cliff, not an allowance: at EUR 3,000,000 or more, the whole net interest is tested.
   - Other escapes: the company is not related to anyone and has no foreign PE (§ 4h(2)(b)), or the equity ratio test for group members (§ 4h(2)(c), restricted for companies by § 8a(3) KStG where shareholder debt is more than 10% of net interest).
6. **Losses ([§ 10d EStG](https://www.gesetze-im-internet.de/estg/__10d.html), applied to companies through § 8(1) KStG).**
   - Carry-back: up to EUR 1,000,000 to the previous year, then to the year before that (§ 10d(1)). The company can ask to skip carry-back in full.
   - Carry-forward: unlimited in time. Each year, the first EUR 1,000,000 of income can be fully offset, then 70% of the income above EUR 1,000,000 (§ 10d(2), for 2024 to 2027 under § 52(18b)). So at least 30% of income above EUR 1m is always taxed (minimum taxation). From 2028 the share returns to 60%: Art. 6 of the law of 27 March 2024 ([BGBl. 2024 I Nr. 108](https://www.recht.bund.de/bgbl/1/2024/108/VO.html)) is already enacted and comes into force on 1 January 2028. The consolidated statute page does not show it yet. Plan multi-year loss use with 60% from 2028.
   - Trade tax has its own loss account: EUR 1m plus **60%**, and no carry-back ([§ 10a GewStG](https://www.gesetze-im-internet.de/gewstg/__10a.html)). Do not assume the two loss figures match.
7. **Share changes ([§ 8c KStG](https://www.gesetze-im-internet.de/kstg_1977/__8c.html)).** If more than 50% of the shares or voting rights pass to one buyer (or a group with common interests) within five years, all unused losses so far are lost. Exceptions: transfers inside a 100% group (the group clause), and losses up to the built-in gains (stille Reserven) taxable in Germany. A company that keeps the same business can apply to keep losses under [§ 8d KStG](https://www.gesetze-im-internet.de/kstg_1977/__8d.html); the application goes in the return for the year of the transfer.
8. **Tax group (Organschaft) ([§ 14 KStG](https://www.gesetze-im-internet.de/kstg_1977/__14.html), [§ 17 KStG](https://www.gesetze-im-internet.de/kstg_1977/__17.html)).** The subsidiary's income is attributed to the parent if: the parent holds the majority of votes without break from the start of the subsidiary's financial year; the subsidiary signs a profit transfer agreement (Gewinnabführungsvertrag) for at least five years and actually carries it out; and the holding belongs to a German PE of the parent. A GmbH subsidiary must also agree to loss assumption by reference to § 302 AktG (§ 17 KStG). For trade tax the subsidiary is treated as a PE of the parent ([§ 2(2) GewStG](https://www.gesetze-im-internet.de/gewstg/__2.html)). There is no other form of group relief.

## Deadlines and filing

| Step | Rule for tax year 2026 | Source |
|---|---|---|
| Return | Corporate tax return (Körperschaftsteuererklärung), plus the trade tax return and, where relevant, the separate determinations (for example the tax contribution account, § 27 KStG). Filed electronically in the official data format via the official interface (ELSTER). Paper only on application for hardship. In ELSTER the return is form KSt 1 (a cover form) with annexes, for example Anlage GK (business income), Anlage ZVE (taxable income), Anlage Verluste (losses), Anlage Zinsschranke (interest barrier), Anlagen OG and OT (tax group) and Anlage KSt 1 F (tax contribution account). That is the 2025 set; ELSTER had not yet published its 2026 instructions on 22 October 2026 | [§ 31(1a) KStG](https://www.gesetze-im-internet.de/kstg_1977/__31.html); [§ 14a GewStG](https://www.gesetze-im-internet.de/gewstg/__14a.html); [ELSTER, Anleitung zur KSt 2025](https://www.elster.de/eportal/helpGlobal?themaGlobal=help_kst_2025) |
| Electronic balance sheet (E-Bilanz) | Balance sheet and profit and loss account sent in the official data format. For financial years beginning after 31 December 2024 this includes the unaggregated account balances (Kontennachweise). The fixed-asset schedule (Anlagenspiegel) is added only for financial years beginning after 31 December 2027 | [§ 5b(1) EStG](https://www.gesetze-im-internet.de/estg/__5b.html); [§ 52(11) EStG](https://www.gesetze-im-internet.de/estg/__52.html) |
| Deadline, no adviser | Seven months after the year end: 31 July 2027. That date is a Saturday, so the deadline moves to Monday 2 August 2027 | [§ 149(2) AO](https://www.gesetze-im-internet.de/ao_1977/__149.html); [§ 108(3) AO](https://www.gesetze-im-internet.de/ao_1977/__108.html) |
| Deadline, with a Steuerberater | Last day of February of the second following year: 29 February 2028. The tax office can demand earlier filing in listed cases (for example late filing last year, a large final payment expected, or an audit planned), with at least four months' notice | [§ 149(3), (4) AO](https://www.gesetze-im-internet.de/ao_1977/__149.html) |
| Transitional extensions | The Covid-era extensions ended with tax year 2024 (adviser deadline 30 April 2026). None applies to 2025 or 2026 | [Art. 97 § 36(3) EGAO](https://www.gesetze-im-internet.de/aoeg_1977/art_97__36.html) |
| Quarterly prepayments | 10 March, 10 June, 10 September and 10 December of the tax year, set by the tax office in a prepayment notice, normally based on the last assessment. Set only if at least EUR 400 a year and EUR 100 per date. Solidarity surcharge is paid on the prepayments too | [§ 37(1), (3), (5) EStG](https://www.gesetze-im-internet.de/estg/__37.html) via [§ 31(1) KStG](https://www.gesetze-im-internet.de/kstg_1977/__31.html); [§ 3(1) no. 2 SolzG](https://www.gesetze-im-internet.de/solzg_1995/__3.html) |
| Non-calendar financial year | Prepayments are due during the financial year that ends in the tax year | [§ 31(2) KStG](https://www.gesetze-im-internet.de/kstg_1977/__31.html) |
| Final payment | Within one month after the assessment notice is given (any unpaid prepayments at once) | [§ 36(4) EStG](https://www.gesetze-im-internet.de/estg/__36.html) via § 31(1) KStG |
| Trade tax | Assessed by the tax office (base amount), collected by the municipality, which also sets its own prepayments. See `de-trade-tax` | [§ 14a GewStG](https://www.gesetze-im-internet.de/gewstg/__14a.html) |

## Penalties and interest

| Charge | Rule | Source |
|---|---|---|
| Late filing surcharge (Verspätungszuschlag) | For each month or part month late: 0.25% of the assessed tax less prepayments and withholding credited, minimum EUR 25 a month. Rounded down to full euros; maximum EUR 25,000 | [§ 152(5), (10) AO](https://www.gesetze-im-internet.de/ao_1977/__152.html) |
| When the surcharge is compulsory | If the annual return is not filed within 14 months after the year end (for 2026: by 29 February 2028), or by a date the tax office ordered. Before that it is discretionary. Not compulsory if the tax is nil or negative, or does not exceed prepayments and withholding | [§ 152(2), (3) AO](https://www.gesetze-im-internet.de/ao_1977/__152.html) |
| Trade tax return late | EUR 25 per month or part month | [§ 152(6) AO](https://www.gesetze-im-internet.de/ao_1977/__152.html) |
| Interest on assessed differences (Nachzahlungszinsen / Erstattungszinsen) | 0.15% a month (1.8% a year), starting 15 months after the end of the tax year (for 2026: from 1 April 2028). Full months only; the amount is rounded down to the next EUR 50. Applies both ways | [§ 233a(1)-(3) AO](https://www.gesetze-im-internet.de/ao_1977/__233a.html); [§ 238(1), (1a), (2) AO](https://www.gesetze-im-internet.de/ao_1977/__238.html) |
| Late payment surcharge (Säumniszuschlag) | 1% a month or part month of the overdue tax, rounded down to the next EUR 50. Not charged if payment is up to three days late (except for cheque payment) | [§ 240(1), (3) AO](https://www.gesetze-im-internet.de/ao_1977/__240.html) |

## Cross-border points

- **Dividends paid by a German company (Kapitalertragsteuer).** The company withholds 25% ([§ 43(1) no. 1 EStG](https://www.gesetze-im-internet.de/estg/__43.html), [§ 43a(1) no. 1 EStG](https://www.gesetze-im-internet.de/estg/__43a.html)) plus 5.5% solidarity surcharge on that tax ([§ 3(1) no. 5 SolzG](https://www.gesetze-im-internet.de/solzg_1995/__3.html)): 26.375% in total. Relief for a foreign corporate shareholder:
  - **EU parent company:** no withholding on application if the parent holds at least 10% directly and has held it for 12 months without break ([§ 43b EStG](https://www.gesetze-im-internet.de/estg/__43b.html), implementing the Parent-Subsidiary Directive 2011/96/EU). The anti-treaty-shopping rule in [§ 50d(3) EStG](https://www.gesetze-im-internet.de/estg/__50d.html) applies.
  - **Exemption certificate:** the payer must withhold unless the shareholder holds a Freistellungsbescheinigung from the Federal Central Tax Office (BZSt) under [§ 50c(2) no. 1 EStG](https://www.gesetze-im-internet.de/estg/__50c.html). It runs at the earliest from the day the application reaches the BZSt, for at most five years, and cannot be backdated ([BZSt: exemption procedure](https://www.bzst.de/DE/Unternehmen/Kapitalertraege/Kapitalertragsteuerentlastung/Sonderkonstellation/Freistellungsverfahren_50c/freistellungsverfahren_50c_node.html)). Otherwise the shareholder claims a refund from the BZSt under § 50c(3) EStG.
  - **Any foreign company with no treaty or directive relief:** two fifths of the 25% withheld is refunded ([§ 44a(9) EStG](https://www.gesetze-im-internet.de/estg/__44a.html)), leaving 15% plus surcharge. Treaty rates may be lower, claimed through the same BZSt procedures.
- **Interest.** Withholding under § 43 EStG covers specific types, for example convertible bonds, profit-participating bonds and profit participation rights ([§ 43(1) no. 2 EStG](https://www.gesetze-im-internet.de/estg/__43.html)), at 25%. Ordinary loan interest paid to a foreign lender is not in that list, but check the lender's limited tax liability under § 49 EStG before paying gross. Interest between associated EU companies can be relieved under [§ 50g EStG](https://www.gesetze-im-internet.de/estg/__50g.html) (Interest and Royalties Directive).
- **Royalties.** Payments to a non-resident for the use of rights or know-how bear 15% withholding ([§ 50a(1) no. 3, (2) EStG](https://www.gesetze-im-internet.de/estg/__50a.html)) plus 5.5% surcharge ([§ 3(1) no. 6 SolzG](https://www.gesetze-im-internet.de/solzg_1995/__3.html)). Relief through § 50g EStG, a treaty, or a BZSt exemption certificate. Where a treaty applies and the payments to that recipient in the calendar year are not more than EUR 10,000, the payer need not withhold but must still file the withholding return (§ 50c(2) no. 2 EStG).
- **For the non-resident recipient,** corporate tax on income subject to withholding is generally settled by the withholding, unless the income belongs to a German business ([§ 32(1) KStG](https://www.gesetze-im-internet.de/kstg_1977/__32.html)).
- **CFC rules (Hinzurechnungsbesteuerung).** If German taxpayers control a foreign company, its passive income is added to their German income where it bears tax of less than 15% ([§ 7 AStG](https://www.gesetze-im-internet.de/astg/__7.html), [§ 8(5) AStG](https://www.gesetze-im-internet.de/astg/__8.html)). The test compares the foreign tax with 15%, not with the German rate, so the 2028 to 2032 rate cuts do not change it. Refer any CFC case.
- **Exit tax for companies.** If Germany loses or restricts its right to tax the gain on an asset (for example the asset moves to a foreign PE), the company is treated as selling it at fair market value ([§ 12(1) KStG](https://www.gesetze-im-internet.de/kstg_1977/__12.html)). For a move to an EU or EEA state the company can apply for a compensating item released over five years ([§ 4g EStG](https://www.gesetze-im-internet.de/estg/__4g.html)). Shareholders who leave Germany: see `leaving-germany-exit-tax`.

## Worked examples

### Example 1: trading GmbH, profit EUR 480,000 before tax

A GmbH sells machinery parts from one site. Its financial year is the calendar year 2026. Profit before tax in the accounts is EUR 480,000. It paid EUR 36,000 in supervisory board fees and a criminal-court fine of EUR 2,000 (both expensed). No dividends, no losses, net interest well under EUR 3m. Assumed trade tax multiplier: 400% (illustration only; read the real one from the municipality). No trade tax add-backs or reductions apply.

1. Add back half the board fees, EUR 18,000, and the fine, EUR 2,000. Taxable income: 480,000 + 18,000 + 2,000 = EUR 500,000.
2. Corporate tax at 15%: EUR 75,000. Solidarity surcharge at 5.5%: EUR 4,125.
3. Trade income EUR 500,000 (already a multiple of EUR 100, no allowance for a company). Base amount at 3.5%: EUR 17,500. Trade tax at 400%: EUR 70,000.
4. Total tax on profit: EUR 149,125, which is 29.825% of taxable income.
5. The company paid corporate tax prepayments of EUR 60,000 and surcharge of EUR 3,300 in 2026. Final payment after assessment: EUR 15,000 corporate tax and EUR 825 surcharge, due one month after the notice.

```oa-check
name: Trading GmbH, 2026, taxable income EUR 500,000, multiplier 400%
inputs:
  profit_before_tax: 480000
  board_fees: 36000
  fine: 2000
  hebesatz: 400
  kst_prepaid: 60000
  soli_prepaid: 3300
steps:
  - taxable: profit_before_tax + board_fees * 0.5 + fine
  - kst: taxable * 0.15
  - soli: kst * 0.055
  - trade_income: floor(taxable / 100) * 100
  - base_amount: trade_income * 0.035
  - trade_tax: base_amount * hebesatz / 100
  - total_tax: kst + soli + trade_tax
  - effective_rate: round(total_tax / taxable * 100, 3)
  - kst_due: kst - kst_prepaid
  - soli_due: soli - soli_prepaid
expected:
  taxable: 500000
  kst: 75000
  soli: 4125
  base_amount: 17500
  trade_tax: 70000
  total_tax: 149125
  effective_rate: 29.825
  kst_due: 15000
  soli_due: 825
```

### Example 2: losses brought forward plus a dividend from a subsidiary

A holding and trading GmbH has, for 2026, profit before tax of EUR 3,000,000. This includes a EUR 200,000 dividend from a German GmbH in which it has held 20% since 2020. It has unused losses carried forward of EUR 4,000,000 for corporate tax and, by assumption, also EUR 4,000,000 for trade tax. No change of shareholders in the last five years, so § 8c does not bite. Assumed multiplier 400%. No other add-backs or reductions.

1. **Participation exemption.** The holding was at least 10% at the start of 2026, so the dividend is exempt: deduct EUR 200,000, add back 5% = EUR 10,000. Income before losses: EUR 2,810,000.
2. **Corporate tax loss offset.** First EUR 1,000,000 in full. Then 70% of the EUR 1,810,000 above it = EUR 1,267,000. Total offset EUR 2,267,000. Taxable income EUR 543,000. Losses left: EUR 1,733,000.
3. **Corporate tax and surcharge.** 15% of EUR 543,000 = EUR 81,450. Surcharge 5.5% = EUR 4,479.75.
4. **Trade tax.** Trade income starts from the same EUR 2,810,000. The dividend is already out through § 8b, and the 5% add-back stays in trade income ([§ 9 no. 2a sentence 4 GewStG](https://www.gesetze-im-internet.de/gewstg/__9.html)). Loss offset: EUR 1,000,000 plus **60%** of EUR 1,810,000 = EUR 2,086,000. Trade income EUR 724,000; base amount at 3.5% = EUR 25,340; trade tax at 400% = EUR 101,360. Trade tax losses left: EUR 1,914,000.
5. **Total** for 2026: EUR 187,289.75, even though the company still has losses on both accounts. This is the minimum taxation effect.

```oa-check
name: GmbH with EUR 4m losses and a 20% subsidiary dividend, 2026
inputs:
  profit_before_tax: 3000000
  dividend: 200000
  loss_cf_kst: 4000000
  loss_cf_gewst: 4000000
  hebesatz: 400
steps:
  - income_before_losses: profit_before_tax - dividend + dividend * 0.05
  - kst_offset: min(loss_cf_kst, min(income_before_losses, 1000000) + max(income_before_losses - 1000000, 0) * 0.70)
  - taxable: income_before_losses - kst_offset
  - kst_loss_left: loss_cf_kst - kst_offset
  - kst: taxable * 0.15
  - soli: kst * 0.055
  - gewst_offset: min(loss_cf_gewst, min(income_before_losses, 1000000) + max(income_before_losses - 1000000, 0) * 0.60)
  - trade_income: floor((income_before_losses - gewst_offset) / 100) * 100
  - gewst_loss_left: loss_cf_gewst - gewst_offset
  - base_amount: trade_income * 0.035
  - trade_tax: base_amount * hebesatz / 100
  - total_tax: kst + soli + trade_tax
expected:
  income_before_losses: 2810000
  kst_offset: 2267000
  taxable: 543000
  kst_loss_left: 1733000
  kst: 81450
  soli: 4479.75
  gewst_offset: 2086000
  trade_income: 724000
  gewst_loss_left: 1914000
  trade_tax: 101360
  total_tax: 187289.75
```

## Ask the client first

1. **Where is the company managed, and where are its establishments?** This decides German residence, and the trade tax multiplier of each municipality (with its year). Several towns means the base amount is split.
2. **What is the financial year?** A non-calendar year changes which profit falls into 2026 and when prepayments are due.
3. **Is a Steuerberater filing the return?** It moves the deadline from 2 August 2027 to 29 February 2028, unless the tax office orders earlier filing.
4. **What shareholdings does the company hold, how large, and since when?** For the corporate tax dividend exemption, test at least 10% at 1 January and any acquisition of a participation of at least 10% deemed to occur then under § 8b(4) sentence 6; at least 15% at the start of the period for the trade tax reduction; 12 months for § 43b relief on dividends it pays out.
5. **Have more than 50% of its own shares changed hands in the last five years, or is that planned?** Losses may be forfeited under § 8c KStG.
6. **What is the net interest expense, and is the company part of a group or tax group?** At EUR 3m or more the interest barrier applies; an Organschaft changes who is taxed.

## Sources

| Source | URL | Read on |
|---|---|---|
| KStG § 1 (unlimited liability) | https://www.gesetze-im-internet.de/kstg_1977/__1.html | 2026-10-22 |
| KStG § 2 (limited liability) | https://www.gesetze-im-internet.de/kstg_1977/__2.html | 2026-10-22 |
| KStG § 7 (tax year, financial year) | https://www.gesetze-im-internet.de/kstg_1977/__7.html | 2026-10-22 |
| KStG § 8 (income, hidden distributions) | https://www.gesetze-im-internet.de/kstg_1977/__8.html | 2026-10-22 |
| KStG § 8a (interest barrier for companies) | https://www.gesetze-im-internet.de/kstg_1977/__8a.html | 2026-10-22 |
| KStG § 8b (participation exemption) | https://www.gesetze-im-internet.de/kstg_1977/__8b.html | 2026-10-22 |
| KStG § 8b(4), specifically sentence 6: acquisition deeming for the corporate dividend holding test | https://www.gesetze-im-internet.de/kstg_1977/__8b.html | 2026-10-29 |
| KStG § 8c (share changes and losses) | https://www.gesetze-im-internet.de/kstg_1977/__8c.html | 2026-10-22 |
| KStG § 8d (continuing business) | https://www.gesetze-im-internet.de/kstg_1977/__8d.html | 2026-10-22 |
| KStG § 10 (non-deductible expenses) | https://www.gesetze-im-internet.de/kstg_1977/__10.html | 2026-10-22 |
| KStG § 12 (exit taxation) | https://www.gesetze-im-internet.de/kstg_1977/__12.html | 2026-10-22 |
| KStG § 14 (Organschaft) | https://www.gesetze-im-internet.de/kstg_1977/__14.html | 2026-10-22 |
| KStG § 17 (Organschaft with a GmbH subsidiary) | https://www.gesetze-im-internet.de/kstg_1977/__17.html | 2026-10-22 |
| KStG § 23 (rate and enacted cuts) | https://www.gesetze-im-internet.de/kstg_1977/__23.html | 2026-10-22 |
| KStG § 24 (allowance, not for companies) | https://www.gesetze-im-internet.de/kstg_1977/__24.html | 2026-10-22 |
| KStG § 31 (procedure, e-filing, prepayments) | https://www.gesetze-im-internet.de/kstg_1977/__31.html | 2026-10-22 |
| KStG § 32 (withholding as final tax) | https://www.gesetze-im-internet.de/kstg_1977/__32.html | 2026-10-22 |
| SolzG § 4 (surcharge rate) | https://www.gesetze-im-internet.de/solzg_1995/__4.html | 2026-10-22 |
| SolzG § 3 (surcharge base, threshold for individuals only) | https://www.gesetze-im-internet.de/solzg_1995/__3.html | 2026-10-22 |
| EStG § 4h (interest barrier) | https://www.gesetze-im-internet.de/estg/__4h.html | 2026-10-22 |
| EStG § 4g (exit compensating item) | https://www.gesetze-im-internet.de/estg/__4g.html | 2026-10-22 |
| EStG § 7 (depreciation) | https://www.gesetze-im-internet.de/estg/__7.html | 2026-10-22 |
| EStG § 6 (low-value assets) | https://www.gesetze-im-internet.de/estg/__6.html | 2026-10-22 |
| EStG consolidated text (last amended 15.10.2026) | https://www.gesetze-im-internet.de/estg/BJNR010050934.html | 2026-10-22 |
| EStG § 10d (losses) | https://www.gesetze-im-internet.de/estg/__10d.html | 2026-10-22 |
| EStG § 52 (application dates) | https://www.gesetze-im-internet.de/estg/__52.html | 2026-10-22 |
| EStG § 37 (prepayments) | https://www.gesetze-im-internet.de/estg/__37.html | 2026-10-22 |
| EStG § 36 (final payment) | https://www.gesetze-im-internet.de/estg/__36.html | 2026-10-22 |
| EStG § 43b (EU parent companies) | https://www.gesetze-im-internet.de/estg/__43b.html | 2026-10-22 |
| EStG § 43 (withholding cases) | https://www.gesetze-im-internet.de/estg/__43.html | 2026-10-22 |
| EStG § 43a (withholding rate) | https://www.gesetze-im-internet.de/estg/__43a.html | 2026-10-22 |
| EStG § 44a (two-fifths refund) | https://www.gesetze-im-internet.de/estg/__44a.html | 2026-10-22 |
| EStG § 50a (royalty withholding) | https://www.gesetze-im-internet.de/estg/__50a.html | 2026-10-22 |
| EStG § 50c (exemption and refund procedure) | https://www.gesetze-im-internet.de/estg/__50c.html | 2026-10-22 |
| EStG § 50d (anti-abuse) | https://www.gesetze-im-internet.de/estg/__50d.html | 2026-10-22 |
| EStG § 50g (Interest and Royalties Directive) | https://www.gesetze-im-internet.de/estg/__50g.html | 2026-10-22 |
| AO § 12 (permanent establishment) | https://www.gesetze-im-internet.de/ao_1977/__12.html | 2026-10-22 |
| AO § 108 (deadline on a weekend) | https://www.gesetze-im-internet.de/ao_1977/__108.html | 2026-10-22 |
| AO § 149 (filing deadlines) | https://www.gesetze-im-internet.de/ao_1977/__149.html | 2026-10-22 |
| AO § 152 (late filing surcharge) | https://www.gesetze-im-internet.de/ao_1977/__152.html | 2026-10-22 |
| AO § 233a (interest on assessed differences) | https://www.gesetze-im-internet.de/ao_1977/__233a.html | 2026-10-22 |
| AO § 238 (interest rate) | https://www.gesetze-im-internet.de/ao_1977/__238.html | 2026-10-22 |
| AO § 240 (late payment surcharge) | https://www.gesetze-im-internet.de/ao_1977/__240.html | 2026-10-22 |
| EGAO Art. 97 § 36 (transitional deadlines) | https://www.gesetze-im-internet.de/aoeg_1977/art_97__36.html | 2026-10-22 |
| GewStG § 16 (multiplier) | https://www.gesetze-im-internet.de/gewstg/__16.html | 2026-10-22 |
| GewStG consolidated text (§ 36(5b); last amended 29.6.2026) | https://www.gesetze-im-internet.de/gewstg/BJNR009790936.html | 2026-10-22 |
| BGBl. 2026 I Nr. 197, law of 29 June 2026, Art. 8 (multiplier floor 200 to 280 from 2027) | https://www.recht.bund.de/bgbl/1/2026/197/VO.html | 2026-10-22 |
| BGBl. 2024 I Nr. 108, law of 27 March 2024, Art. 2, Art. 6 and Art. 35(9) (loss share 70% from 2024, 60% from 2028) | https://www.recht.bund.de/bgbl/1/2024/108/VO.html | 2026-10-22 |
| ELSTER, Anleitung zur KSt 2025 (form KSt 1 and annexes) | https://www.elster.de/eportal/helpGlobal?themaGlobal=help_kst_2025 | 2026-10-22 |
| AStG § 8 (CFC low-tax test) | https://www.gesetze-im-internet.de/astg/__8.html | 2026-10-22 |
| MinStG § 1 (Pillar Two scope) | https://www.gesetze-im-internet.de/minstg/__1.html | 2026-10-22 |
| EStG § 4 (§ 4(5b), trade tax not deductible) | https://www.gesetze-im-internet.de/estg/__4.html | 2026-10-22 |
| EStG § 5b (E-Bilanz) | https://www.gesetze-im-internet.de/estg/__5b.html | 2026-10-22 |
| AO § 10 (place of management) | https://www.gesetze-im-internet.de/ao_1977/__10.html | 2026-10-22 |
| AO § 11 (seat) | https://www.gesetze-im-internet.de/ao_1977/__11.html | 2026-10-22 |
| KStG § 5 (exempt bodies) | https://www.gesetze-im-internet.de/kstg_1977/__5.html | 2026-10-22 |
| GewStG § 2 (companies always a trade business; Organschaft) | https://www.gesetze-im-internet.de/gewstg/__2.html | 2026-10-22 |
| GewStG § 9 (reductions, dividend holdings) | https://www.gesetze-im-internet.de/gewstg/__9.html | 2026-10-22 |
| GewStG § 10a (trade tax losses) | https://www.gesetze-im-internet.de/gewstg/__10a.html | 2026-10-22 |
| GewStG § 11 (base rate, allowances) | https://www.gesetze-im-internet.de/gewstg/__11.html | 2026-10-22 |
| GewStG § 14a (trade tax return, e-filing) | https://www.gesetze-im-internet.de/gewstg/__14a.html | 2026-10-22 |
| GewStG § 36 (application dates) | https://www.gesetze-im-internet.de/gewstg/__36.html | 2026-10-22 |
| AStG § 7 (CFC inclusion) | https://www.gesetze-im-internet.de/astg/__7.html | 2026-10-22 |
| MinStG § 101 (Pillar Two start date) | https://www.gesetze-im-internet.de/minstg/__101.html | 2026-10-22 |
| BMF Monatsbericht August 2025, Investitionssofortprogramm | https://www.bundesfinanzministerium.de/Monatsberichte/Ausgabe/2025/08/Inhalte/Kapitel-2-Fokus/investitionssofortprogramm-deutschland.html | 2026-10-22 |
| BMF "Steuern von A bis Z", Ausgabe 2025 (KSt 15%, Soli 5.5%, multiplier floor 200%) | https://www.bundesfinanzministerium.de/Content/DE/Downloads/Broschueren_Bestellservice/steuern-von-a-z.pdf?__blob=publicationFile&v=9 | 2026-10-22 |
| BZSt, exemption procedure under § 50c(2) EStG | https://www.bzst.de/DE/Unternehmen/Kapitalertraege/Kapitalertragsteuerentlastung/Sonderkonstellation/Freistellungsverfahren_50c/freistellungsverfahren_50c_node.html | 2026-10-22 |

Not yet confirmed: the ELSTER form set for tax year 2026. ELSTER's 2026 instructions page was empty on 2026-10-22, so the skill names the 2025 set (KSt 1 and annexes).

> Contributed by Ryan Duguid.

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
