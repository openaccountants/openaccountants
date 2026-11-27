---
name: de-corporate-tax
description: "German corporate income tax (Körperschaftsteuer, KSt) for tax year 2026: GmbH, UG, AG and other companies resident in Germany, and German permanent establishments of foreign companies. Covers the 15% rate under § 23 KStG and the enacted cuts from 2028, the 5.5% solidarity surcharge, how trade tax adds to the burden, the taxable base, the § 8b participation exemption, loss carry-forward (EUR 1m plus 70% for 2024 to 2027, 60% from 2028) and carry-back, § 8c share changes, Organschaft, the interest barrier, prepayments, filing deadlines, late filing surcharges, interest, and Kapitalertragsteuer on outbound dividends. Trigger on: Körperschaftsteuer, KSt, GmbH tax Germany, German corporate tax rate, Soli on KSt, § 8b KStG, § 8c KStG, Organschaft, Zinsschranke, Verlustvortrag GmbH, Mindestbesteuerung, KSt-Vorauszahlungen, Kapitalertragsteuer Dividende. Out of scope: trade tax detail (de-trade-tax), transfer pricing (germany-transfer-pricing), individual shareholders (germany-income-tax, de-capital-gains), shareholder exit tax (leaving-germany-exit-tax), VAT (germany-vat-return)."
version: 0.8
jurisdiction: DE
tax_year: 2026
last_updated: 2026-11-27
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: corporate-tax
type: computation
---

# German corporate income tax (Körperschaftsteuer): 2026

> **General reference only. Built from the law · Not yet approved.** Obtain review by a qualified German tax adviser before filing, paying or taking a tax position.

Tax year: the calendar year 2026 (Veranlagungszeitraum 2026). A company with a financial year that does not match the calendar year is taxed on the profit of the financial year that ends in 2026, for entities required to keep HGB books; changing to a non-calendar year requires agreement with the tax office ([§ 7(4) KStG](https://www.gesetze-im-internet.de/kstg_1977/__7.html)). A German company pays three taxes on its profit: corporate income tax, the solidarity surcharge on that tax, and municipal trade tax. This Guide computes ordinary KSt and solidarity surcharge and summarises trade tax; the explicit specialist holds below are not usable tax positions. For the trade tax method, use `de-trade-tax`.

## Who this applies to

- **Resident companies (unlimited tax liability).** A company is taxed in Germany on its worldwide income if its place of management (Geschäftsleitung) or its registered seat (Sitz) is in Germany ([§ 1(1) and (2) KStG](https://www.gesetze-im-internet.de/kstg_1977/__1.html)). This includes the GmbH (and its UG variant), the AG, the SE, the KGaA, cooperatives, other private-law legal persons, and commercial businesses of public bodies. "Place of management" means the centre of top-level management ([§ 10 AO](https://www.gesetze-im-internet.de/ao_1977/__10.html)); the seat is the place named in the articles ([§ 11 AO](https://www.gesetze-im-internet.de/ao_1977/__11.html)). This is the domestic-law residence test; dual residence, treaty tie-breakers and foreign tax relief require the actual treaty. Check this point with one of our partner accountants.
- **Non-resident companies (limited tax liability).** A company with neither its management nor its seat in Germany is taxed only on German-source income ([§ 2 no. 1 KStG](https://www.gesetze-im-internet.de/kstg_1977/__2.html)). The main case is a German permanent establishment (Betriebsstätte): a fixed business facility or installation serving the enterprise, such as a branch, office, workshop, warehouse, or a building site lasting more than six months ([§ 12 AO](https://www.gesetze-im-internet.de/ao_1977/__12.html)). Treaty PE thresholds and profit attribution require the actual treaty. Check this point with one of our partner accountants.
- **Out of scope here:**
  - Ordinary partnerships (OHG, KG, GmbH & Co. KG) are outside this company computation. A qualifying partnership can elect corporate treatment under [§ 1a KStG](https://www.gesetze-im-internet.de/kstg_1977/__1a.html). For partner taxation and professional/commercial classification use `de-partners-and-part-year` and `de-trade-tax`.
  - Exempt bodies, charities, public-body businesses, banks, insurers, investment funds and REITs are excluded from this ordinary-company computation. Check this point with one of our partner accountants.
  - Entity classification and special exemptions must be settled before using this computation.
  - Pillar Two/top-up-tax computation is outside scope; the EUR 750m group threshold and two-of-four-year test below are screening conditions, not a top-up-tax calculation.

## Rates, bands and thresholds

| Item | Rate or amount | Tax year | Source |
|---|---|---|---|
| Corporate income tax rate | 15% of taxable income | 2026 and 2027 ("Veranlagungszeiträume bis 2027 15 Prozent") | [§ 23(1) KStG](https://www.gesetze-im-internet.de/kstg_1977/__23.html) |
| Enacted rate cuts | 14% (2028), 13% (2029), 12% (2030), 11% (2031), 10% (2032 onwards); never use these for 2026 | 2028 onwards | [§ 23(1) KStG](https://www.gesetze-im-internet.de/kstg_1977/__23.html) |
| Small-company rate | None. One flat rate. The EUR 5,000 allowance in § 24 KStG does not apply to companies whose distributions are dividends | 2026 | [§ 24 KStG](https://www.gesetze-im-internet.de/kstg_1977/__24.html) |
| Solidarity surcharge (Solidaritätszuschlag) | 5.5% of the corporate income tax. The § 3(3) exemption threshold applies only to income-tax persons, so an ordinary company pays on positive KSt; discard fractions of a cent | 2026 | [§ 4 SolzG](https://www.gesetze-im-internet.de/solzg_1995/__4.html); [§ 3(1) and (3) SolzG](https://www.gesetze-im-internet.de/solzg_1995/__3.html) |
| Corporate tax plus surcharge | 15.825% nominal (15% x 1.055), before assessed-KSt whole-euro rounding and SolZ cent truncation | 2026 | Computed from the two rows above; https://www.gesetze-im-internet.de/kstg_1977/__23.html ; https://www.gesetze-im-internet.de/solzg_1995/__4.html |
| Trade tax (Gewerbesteuer) base rate | 3.5% of trade income, times the municipal multiplier (Hebesatz). Ordinary GmbH/UG/AG get no EUR 24,500 allowance (that allowance is for individuals and partnerships); special bodies require their own allowance test | 2026 | [§ 11 GewStG](https://www.gesetze-im-internet.de/gewstg/__11.html); [§ 16 GewStG](https://www.gesetze-im-internet.de/gewstg/__16.html) |
| Trade tax multiplier floor | 200% in 2026; 280% first applies for 2027 | 2026; 2027 | [BMF trade tax](https://www.bundesfinanzministerium.de/Content/DE/Glossareintraege/G/gewerbesteuer.html?view=renderHelp); [§ 36(5b) GewStG](https://www.gesetze-im-internet.de/gewstg/__36.html) |
| Trade tax deductibility | Not a business expense | 2026 | [§ 4(5b) EStG](https://www.gesetze-im-internet.de/estg/__4.html) |
| Combined burden, illustration | At the assumed 400% multiplier and equal KSt/trade bases: 29.825% for 2026; 24.55% using the enacted 2032 KSt rate. Computed illustrations; obtain the actual municipal multiplier and separate bases | 2026; 2032 | [§ 23 KStG](https://www.gesetze-im-internet.de/kstg_1977/__23.html); [§ 4 SolzG](https://www.gesetze-im-internet.de/solzg_1995/__4.html); [§ 11 GewStG](https://www.gesetze-im-internet.de/gewstg/__11.html); [§ 16 GewStG](https://www.gesetze-im-internet.de/gewstg/__16.html) |
| Participation exemption | Ordinary qualifying dividends and share gains: 5% deemed non-deductible, effectively 95% exempt (computed), subject to the holding and anti-hybrid/recapture conditions below; special-sector/share-lending cases excluded | 2026 | [§ 8b(1)–(5), (7)–(11) KStG](https://www.gesetze-im-internet.de/kstg_1977/__8b.html) |
| Dividend exemption holding test | At least 10% directly at the start of the calendar year; acquisition of a participation of at least 10% is deemed to occur at that start | 2026 | [§ 8b(4) KStG](https://www.gesetze-im-internet.de/kstg_1977/__8b.html) |
| Loss carry-forward | EUR 1,000,000 in full, then 70% of income above that. The share falls back to 60% from 2028 | 70%: 2024 to 2027 (so 2026); 60%: 2028 onwards | [§ 10d(2) EStG](https://www.gesetze-im-internet.de/estg/__10d.html); [§ 52(18b) EStG](https://www.gesetze-im-internet.de/estg/__52.html); [BGBl. 2024 I Nr. 108](https://www.recht.bund.de/bgbl/1/2024/108/regelungstext.pdf?__blob=publicationFile&v=1), Art. 6 ("70 Prozent" replaced by "60 Prozent", "erstmals für den Veranlagungszeitraum 2028") and Art. 35(9) ("Artikel 6 tritt am 1. Januar 2028 in Kraft") |
| Loss carry-back | Up to EUR 1,000,000, to the previous year, then the year before that | 2026 | [§ 10d(1) EStG](https://www.gesetze-im-internet.de/estg/__10d.html) |
| Trade tax loss carry-forward | EUR 1,000,000 in full, then 60% of the excess. No carry-back | 2026 | [§ 10a GewStG](https://www.gesetze-im-internet.de/gewstg/__10a.html) |
| Interest barrier (Zinsschranke) | Net interest up to 30% of statutory tax EBITDA; current-interest escape only below three million euros (the statute: “weniger als drei Millionen Euro”), subject to the old-interest-carry restriction below | 2026 | [§ 4h(1), (2) EStG](https://www.gesetze-im-internet.de/estg/__4h.html) |
| Declining-balance depreciation | Up to 3 times the straight-line rate, max 30%, for movable fixed assets bought or made after 30 June 2025 and before 1 January 2028; remaining-book-value basis and first-year month apportionment | 2026 | [§ 7(2) EStG](https://www.gesetze-im-internet.de/estg/__7.html) |
| Low-value assets | Optional immediate write-off for independently usable, depreciable movable fixed assets up to EUR 800, measured excluding contained input VAT; record items above EUR 250 separately unless the bookkeeping supplies the details | 2026 | [§ 6(2) EStG](https://www.gesetze-im-internet.de/estg/__6.html) |
| Pillar Two screening only | German-located group entities: EUR 750m+ consolidated revenue in at least two of the four immediately preceding financial years; proportionate threshold for non-12-month years, excluded-entity and § 63 adjustments, and joint-venture rules must be tested. General start: financial years beginning after 30 December 2023; § 11 has its own later start. No top-up-tax computation here | 2026 | [§ 1 MinStG](https://www.gesetze-im-internet.de/minstg/__1.html); [§ 101 MinStG](https://www.gesetze-im-internet.de/minstg/__101.html) |

**What applies for 2026.** Use 15% for 2026 and 2027. The enacted schedule in § 23 KStG starts its cuts in 2028.

**Trade tax in one paragraph.** A GmbH or AG is a trade business in full ([§ 2(2) GewStG](https://www.gesetze-im-internet.de/gewstg/__2.html)). Start from corporate-tax profit and apply the separate trade-tax additions/reductions. The financing add-back is one quarter of the positive excess of the statutory weighted sum over EUR 200,000, only for amounts deducted in profit; rents and royalties are not all counted at full weight ([§ 8 no. 1 GewStG](https://www.gesetze-im-internet.de/gewstg/__8.html)). Round trade income down to EUR 100, apply 3.5%, then the actual municipal multiplier; there is no EUR 24,500 allowance for an ordinary GmbH/AG ([§ 11 GewStG](https://www.gesetze-im-internet.de/gewstg/__11.html), [§ 16 GewStG](https://www.gesetze-im-internet.de/gewstg/__16.html)). At an assumed 400%, trade tax is 14% of that base; add 15.825% only when both tax bases match. The § 35 EStG credit reduces income tax of eligible individual businesses/partners, not corporate tax. Establishments in several municipalities require apportionment. Use `de-trade-tax` for the weighted financing categories, dividend reductions (domestic threshold 15% at the start of the collection period), apportionment and prepayments.

## The taxable base

Income is worked out under the Income Tax Act and the KStG together ([§ 8(1) KStG](https://www.gesetze-im-internet.de/kstg_1977/__8.html)). For a GmbH or AG all income is business income ([§ 8(2) KStG](https://www.gesetze-im-internet.de/kstg_1977/__8.html)).

1. **Start** from the profit in the tax balance sheet (commercial accounts adjusted to tax rules).
2. **Add back non-deductible items:**
   - Corporate tax, solidarity surcharge and other taxes on income ([§ 10 no. 2 KStG](https://www.gesetze-im-internet.de/kstg_1977/__10.html)), and trade tax ([§ 4(5b) EStG](https://www.gesetze-im-internet.de/estg/__4.html)).
   - Half of supervisory board fees ([§ 10 no. 4 KStG](https://www.gesetze-im-internet.de/kstg_1977/__10.html)).
   - Criminal-court fines and punitive sanctions under [§ 10 no. 3 KStG](https://www.gesetze-im-internet.de/kstg_1977/__10.html); compensatory payments are not automatically included. Gifts and entertainment require their separate § 4(5) EStG limits: Check this point with one of our partner accountants.
   - Hidden profit distributions (verdeckte Gewinnausschüttungen), such as excess salary or rent paid to a shareholder. They do not reduce income ([§ 8(3) KStG](https://www.gesetze-im-internet.de/kstg_1977/__8.html)). Pricing with related parties: see `germany-transfer-pricing`.
3. **Participation exemption ([§ 8b KStG](https://www.gesetze-im-internet.de/kstg_1977/__8b.html)).**
   - For an ordinary qualifying dividend, exemption requires that the payment did not reduce the paying company’s income (§ 8b(1)); 5% is added back as a non-deductible expense (§ 8b(5)). Different foreign attribution/anti-hybrid cases are held: Check this point with one of our partner accountants. The direct holding test is at least 10% at the start of the calendar year. Under § 8b(4) sentence 6, acquisition of a participation of at least 10% is deemed to occur at the start of that year. Where the holding test, including that deeming rule, is not met, dividends are fully taxable (§ 8b(4)).
   - Ordinary share-sale gains have no minimum holding threshold and are exempt with 5% added back (§ 8b(2)–(3)). The exemption does not cover recapture of an earlier tax-effective write-down not reversed by a higher valuation, or the specified § 6b/similar deductions. Share-related losses/write-downs are not deductible (§ 8b(3)). Shareholder loans (including the original more-than-25% holding case), securities lending, hybrid attribution and financial-sector exceptions need their full tests: Check this point with one of our partner accountants.
4. **Depreciation.** Straight-line over useful life ([§ 7(1) EStG](https://www.gesetze-im-internet.de/estg/__7.html)). For movable fixed assets acquired or made from 1 July 2025 to 31 December 2027 the company may choose declining balance on remaining book value at up to three times the straight-line rate, max 30% (§ 7(2) EStG). Apportion the acquisition/manufacture year by completed earlier months (one twelfth each); do not combine declining balance with extraordinary wear deductions. An independently usable, depreciable movable fixed asset costing no more than EUR 800 excluding contained input VAT may be written off at once; above EUR 250 keep the required asset details in a register or the bookkeeping ([§ 6(2) EStG](https://www.gesetze-im-internet.de/estg/__6.html)).
5. **Interest barrier ([§ 4h EStG](https://www.gesetze-im-internet.de/estg/__4h.html), [§ 8a KStG](https://www.gesetze-im-internet.de/kstg_1977/__8a.html)).**
   - Interest expense is deductible up to interest income. Net interest above that is deductible only up to 30% of tax EBITDA. After using eligible EBITDA carries from the previous five financial years in chronological order, remaining nondeductible interest is carried forward (Zinsvortrag). Unused current EBITDA capacity is carried into the following five financial years, but no EBITDA carry is generated in a year when interest expense does not exceed interest income or an Absatz 2 escape excludes the barrier (§ 4h(1) sentences 3–6). For companies, replace the statutory relevant profit with relevant income before §§ 4h/10d EStG and § 9(1) no. 2 KStG (§ 8a(1)); do not use commercial EBITDA. Mixed old/current interest allocation requires a separate worksheet: Check this point with one of our partner accountants.
   - The rule does not apply when net interest is **less than** EUR 3,000,000 (§ 4h(2)(a)). This is a cliff, not an allowance: at EUR 3,000,000 or more, the whole net interest is tested. Absatz 2 does not apply insofar as interest expense is increased by an old interest carry (§ 4h(1) sentence 7); do not exempt that old carry under the current-year escape.
   - Other escapes: no related person within § 1(2) AStG and no PE outside the residence/seat/management state (§ 4h(2)(b)); or the group equity-ratio test, allowing a shortfall of at most two percentage points, with uniform accounting and statutory adjustments (§ 4h(2)(c)). For a company the latter also requires proof of § 8a(3): the relevant remuneration to qualifying at-least-25% shareholders, related persons or recourse lenders must not exceed 10% of that entity’s net interest, subject to its consolidated-debt/recourse conditions. This is not a blanket exception for every group. Group-ratio, shareholder-financing and carry-forfeiture determinations: Check this point with one of our partner accountants.
6. **Losses ([§ 10d EStG](https://www.gesetze-im-internet.de/estg/__10d.html), applied to companies through § 8(1) KStG).**
   - Carry-back: up to EUR 1,000,000 to the previous year, then to the year before that (§ 10d(1)). The company can ask to skip carry-back in full.
   - Carry-forward: unlimited in time. Each year, the first EUR 1,000,000 of income can be fully offset, then 70% of the income above EUR 1,000,000 (§ 10d(2), for 2024 to 2027 under § 52(18b)). So at least 30% of income above EUR 1m is always taxed (minimum taxation). From 2028 the share returns to 60%: Art. 6 of the law of 27 March 2024 ([BGBl. 2024 I Nr. 108](https://www.recht.bund.de/bgbl/1/2024/108/regelungstext.pdf?__blob=publicationFile&v=1)) is already enacted and comes into force on 1 January 2028. The consolidated statute page does not show it yet. Plan multi-year loss use with 60% from 2028.
   - Trade tax has its own loss account: EUR 1m plus **60%**, and no carry-back ([§ 10a GewStG](https://www.gesetze-im-internet.de/gewstg/__10a.html)). Do not assume the two loss figures match.
7. **Share changes ([§ 8c KStG](https://www.gesetze-im-internet.de/kstg_1977/__8c.html)).** The basic rule disallows unused losses before a harmful acquisition if more than 50% of capital, membership/participation rights or votes is transferred directly or indirectly within five years to one acquirer, related persons or a common-interest group; comparable transactions and proportion-changing capital increases count. Test the exceptions before declaring losses lost. The three specified 100% ownership chains, German-taxable built-in gains, restructuring exception and the continuing-business application under § 8d are separate tests, not automatic relief. Check this point with one of our partner accountants.
8. **Tax group (Organschaft) ([§ 14 KStG](https://www.gesetze-im-internet.de/kstg_1977/__14.html), [§ 17 KStG](https://www.gesetze-im-internet.de/kstg_1977/__17.html)).** For a subsidiary with German management and EU/EEA seat, the ordinary conditions include a legally effective agreement to transfer its entire profit to one qualifying commercial parent for at least five years, actually performed throughout; majority voting control continuously from the start of the subsidiary’s financial year (indirect chains require majority votes at every link); and continuous attribution of the holding to the parent’s German PE whose income is taxable in Germany under domestic law and the treaty. The parent must be an eligible natural person/non-exempt body or a commercially active qualifying partnership. Income attribution first occurs for the year in which the subsidiary financial year ends in which the agreement becomes effective. Reserves beyond statutory reserves require commercial justification. For a GmbH, profit transfer must respect § 301 AktG and loss assumption must refer dynamically to § 302 AktG. A qualifying trade-tax Organschaft treats the subsidiary as the parent’s PE (§ 2(2) GewStG). Agreement defects, early termination, compensation payments and pre-group losses require a separate determination: Check this point with one of our partner accountants.

9. **Corporate-tax assessment rounding.** Round each individual assessed corporate-tax amount in the taxpayer's favour to whole euros ([§ 31(1) sentence 2 KStG](https://www.gesetze-im-internet.de/kstg_1977/__31.html)). For an ordinary positive amount this means rounding down: stipulated taxable income of EUR 10,001 at 15% gives EUR 1,500.15 before rounding and assessed KSt of EUR 1,500. This is the assessed KSt step; underlying bases and surcharges retain their own rules.

## Deadlines and filing

| Step | Rule for tax year 2026 | Source |
|---|---|---|
| Return | Corporate-tax return and separate determinations electronically via the official interface (ELSTER); hardship paper filing only on approved application. Also file the trade-tax/base-apportionment return as applicable. The old 2025 KSt 1 / GK / ZVE / Verluste / Zinsschranke / OG / OT / KSt 1 F list is historical, not a verified 2026 form map. Do not infer 2026 field numbers from it. Check this point with one of our partner accountants. | [§ 31(1a) KStG](https://www.gesetze-im-internet.de/kstg_1977/__31.html); [§ 14a GewStG](https://www.gesetze-im-internet.de/gewstg/__14a.html) |
| Electronic balance sheet (E-Bilanz) | Balance sheet and profit and loss account sent in the official data format. For financial years beginning after 31 December 2024 this includes the unaggregated account balances (Kontennachweise). The fixed-asset schedule and underlying asset register, and existing notes/management/audit reports or § 5(1) sentence 2 register, are added for financial years beginning after 31 December 2027; a hardship waiver requires application | [§ 5b(1) EStG](https://www.gesetze-im-internet.de/estg/__5b.html); [§ 52(11) EStG](https://www.gesetze-im-internet.de/estg/__52.html) |
| Deadline, no adviser | Seven months after the year end: 31 July 2027. That date is a Saturday, so the deadline moves to Monday 2 August 2027 | [§ 149(2) AO](https://www.gesetze-im-internet.de/ao_1977/__149.html); [§ 108(3) AO](https://www.gesetze-im-internet.de/ao_1977/__108.html) |
| Deadline, with a Steuerberater | Last day of February of the second following year: 29 February 2028. The tax office can demand earlier filing in listed cases (for example late filing last year, a large final payment expected, or an audit planned), with a four-month filing period after notification and no date earlier than the ordinary unadvised deadline; an individual extension may also apply | [§ 149(3), (4) AO](https://www.gesetze-im-internet.de/ao_1977/__149.html) |
| Transitional extensions | The Covid-era extension provisions address tax years 2020–2024, not 2026. The old 2024 adviser-deadline illustration (30 April 2026) is historical and not a 2026 filing date | [Art. 97 § 36(3) EGAO](https://www.gesetze-im-internet.de/aoeg_1977/art_97__36.html) |
| Quarterly prepayments | 10 March, 10 June, 10 September and 10 December of the tax year, set by the tax office in a prepayment notice, normally based on the last assessment. Set only if at least EUR 400 a year and EUR 100 per date. Solidarity surcharge is paid on the prepayments too | [§ 37(1), (3), (5) EStG](https://www.gesetze-im-internet.de/estg/__37.html) via [§ 31(1) KStG](https://www.gesetze-im-internet.de/kstg_1977/__31.html); [§ 3(1) no. 2 SolzG](https://www.gesetze-im-internet.de/solzg_1995/__3.html) |
| Non-calendar financial year | Prepayments are due during the financial year that ends in the tax year | [§ 31(2) KStG](https://www.gesetze-im-internet.de/kstg_1977/__31.html) |
| Final payment | Within one month after notification of the assessment; the portion corresponding to overdue unpaid prepayments is payable immediately | [§ 36(4) EStG](https://www.gesetze-im-internet.de/estg/__36.html) via [§ 31(1) KStG](https://www.gesetze-im-internet.de/kstg_1977/__31.html) |
| Trade tax | Assessed by the tax office (base amount), collected by the municipality, which also sets its own prepayments. See `de-trade-tax` | [§ 14a GewStG](https://www.gesetze-im-internet.de/gewstg/__14a.html) |

## Penalties and interest

| Charge | Rule | Source |
|---|---|---|
| Late filing surcharge (Verspätungszuschlag) | For each month or part month late: 0.25% of the assessed tax less prepayments and withholding credited, minimum EUR 25 a month. Rounded down to full euros; maximum EUR 25,000 | [§ 152(5), (10) AO](https://www.gesetze-im-internet.de/ao_1977/__152.html) |
| When the surcharge is compulsory | Ordinarily after 14 months: for 2026, after 29 February 2028, or after a lawful § 149(4) demand. Before then, discretionary; excuse must be considered. The compulsory rule does not apply after an allowed § 109 extension, for a nil/negative assessment, or where tax does not exceed fixed prepayments plus credited withholding; discretionary assessment remains possible. Agriculture and exceptional first-demand/non-filing cases need separate review: Check this point with one of our partner accountants. | [§ 152(1)–(3), (5) AO](https://www.gesetze-im-internet.de/ao_1977/__152.html) |
| Trade tax return late | EUR 25 per started month, rounded to whole euros and capped at EUR 25,000; § 152(1), (2), (3) no. 1 apply. Nil tax or sufficient prepayments do not switch off the compulsory rule for this return | [§ 152(6), (10) AO](https://www.gesetze-im-internet.de/ao_1977/__152.html) |
| Interest on assessed differences (Nachzahlungszinsen / Erstattungszinsen) | Ordinary 2026 assessment: 0.15% per full month (1.8% a year), normally from 1 April 2028 until the assessment becomes effective; not interest on advance-payment or withholding assessments. Round the interest-bearing difference for each tax down to a multiple of EUR 50. Deduct credited withholding/KSt and prepayments fixed before interest begins. Refund interest is limited to the refundable amount and starts no earlier than payment; allocate separate payments chronologically, youngest first. Predominant agricultural income, carrybacks, retroactive events and amended assessments need their special periods: Check this point with one of our partner accountants. | [§ 233a(1)–(3) AO](https://www.gesetze-im-internet.de/ao_1977/__233a.html); [§ 238(1), (1a), (2) AO](https://www.gesetze-im-internet.de/ao_1977/__238.html) |
| Late payment surcharge (Säumniszuschlag) | 1% per started month on overdue assessed/declared tax, with the tax base rounded down to a multiple of EUR 50; none on tax ancillary charges. Not charged if payment is up to three days late (except payments within § 224(2) no. 1 AO, including cash or cheques handed or sent to the tax authority) | [§ 240(1), (3) AO](https://www.gesetze-im-internet.de/ao_1977/__240.html) |

## Cross-border points

- **Dividends paid by a German company (Kapitalertragsteuer).** The company withholds 25% ([§ 43(1) no. 1 EStG](https://www.gesetze-im-internet.de/estg/__43.html), [§ 43a(1) no. 1 EStG](https://www.gesetze-im-internet.de/estg/__43a.html)) plus 5.5% solidarity surcharge on that tax ([§ 3(1) no. 5 SolzG](https://www.gesetze-im-internet.de/solzg_1995/__3.html)): 26.375% in total. Relief for a foreign corporate shareholder:
  - **EU parent company ([§ 43b EStG](https://www.gesetze-im-internet.de/estg/__43b.html)):** § 43b relief requires the qualifying Annex 2 legal-form/tax-status conditions, direct holding of at least 10% at the withholding-tax date (or the distribution-resolution date if the threshold is not met then), and a proven uninterrupted 12-month holding. If the 12 months complete later, claim refund under § 50c(3); exemption at source is unavailable in that case. Liquidation/conversion distributions are excluded. The § 50d(3) anti-abuse test applies. Check this point with one of our partner accountants before treating a particular recipient as eligible.
  - **Exemption certificate ([§ 50c EStG](https://www.gesetze-im-internet.de/estg/__50c.html)):** the payer must withhold unless the shareholder holds a Freistellungsbescheinigung from the Federal Central Tax Office (BZSt) under [§ 50c(2) no. 1 EStG](https://www.gesetze-im-internet.de/estg/__50c.html). It runs at the earliest from the day the application reaches the BZSt, for at most five years, and cannot be backdated (§ 50c(2) sentence 4 EStG). Treaty-based dividend certificates also require a taxable, non-exempt corporate recipient directly holding at least one tenth. Otherwise seek the applicable BZSt refund under § 50c(3), with the tax certificate/data required by that provision. Its filing period is four years after the receipt calendar year, ending no earlier than one year after payment of tax or the treaty deadline. Applications are electronic (hardship exception on application), with foreign-authority residence/PE evidence under § 50c(5); a certificate never establishes eligibility beyond its terms.
  - **Foreign corporate recipient within KStG § 2 no. 1:** for a corporation with neither management nor seat in Germany, taxable on its German-source income, two fifths of the 25% withheld and paid over is refunded ([§ 44a(9) EStG](https://www.gesetze-im-internet.de/estg/__44a.html)), leaving 15% plus surcharge. This refund is subject to the applicable § 50d(3) anti-abuse test and the § 50c(3) and (5) BZSt refund procedure, including the claim and residence evidence; it is not an automatic entitlement for every foreign entity. Treaty rates may be lower, claimed through the same BZSt procedures.
- **Interest, royalties and foreign-source relief : non-usable hold.** Classify the instrument, domestic-source nexus, treaty and beneficial recipient before any gross payment. The original convertible/profit-participating bond 25% illustration, ordinary-loan case, associated-EU-company § 50g route and royalty 15% plus surcharge illustration are not a complete payment instruction. The original EUR 10,000 same-payer/same-recipient annual royalty case requires actual treaty opposition to taxation and continuing return duties; it is not a universal exemption. Check this point with one of our partner accountants.
- **Non-resident recipient.** Withholding can settle corporation tax for limited taxpayers where income is outside a domestic commercial/agricultural business (§ 32(1) KStG); the § 32(2) assessment/liability exceptions remain. Do not infer finality for a residence-change year or every withheld income stream. Check this point with one of our partner accountants.
- **CFC and corporate exit : non-usable holds.** Retain the original passive-income/foreign-tax-below-15% CFC question and the asset-to-foreign-PE/five-year EU/EEA balancing-item question as unresolved case inputs, not automatic inclusion or instalment conclusions. Control, income class, exemptions, taxing-right changes and relief conditions need separate proof. Check this point with one of our partner accountants. Shareholder exit remains routed to `leaving-germany-exit-tax`.

## Worked examples

### Example 1: trading GmbH, profit EUR 480,000 before tax

A GmbH sells machinery parts from one site. Its financial year is the calendar year 2026. Profit before tax in the accounts is EUR 480,000. It paid EUR 36,000 in supervisory board fees and a criminal-court fine of EUR 2,000 (both expensed). No dividends, no losses, net interest well under EUR 3m, and no old interest carry. Assumed trade tax multiplier: 400% (illustration only; read the real one from the municipality). No trade tax add-backs or reductions apply.

1. Add back half the board fees, EUR 18,000, and the fine, EUR 2,000. Taxable income: 480,000 + 18,000 + 2,000 = EUR 500,000.
2. Corporate tax at 15%: EUR 75,000. Solidarity surcharge at 5.5%: EUR 4,125.
3. Trade income EUR 500,000 (already a multiple of EUR 100, no allowance for a company). Base amount at 3.5%: EUR 17,500. Trade tax at 400%: EUR 70,000.
4. Total tax on profit: EUR 149,125, which is 29.825% of taxable income.
5. The company paid corporate tax prepayments of EUR 60,000 and surcharge of EUR 3,300 in 2026. Final payment after assessment: EUR 15,000 corporate tax and EUR 825 surcharge, due one month after notification, assuming no unpaid overdue prepayments.

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
  - kst: floor(taxable * 0.15)
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

A holding and trading GmbH has, for 2026, profit before tax of EUR 3,000,000. This includes a EUR 200,000 dividend from a German GmbH in which it has held 20% since 2020. It has unused losses carried forward of EUR 4,000,000 for corporate tax and, by assumption, also EUR 4,000,000 for trade tax. No change of shareholders in the last five years, so § 8c does not bite. Assumed multiplier 400%. No other add-backs or reductions; the ordinary dividend did not reduce the paying company’s income, no hybrid/recapture/special-sector issue applies, and the loss accounts remain available after all ownership/continuity tests.

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
  - kst: floor(taxable * 0.15)
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
6. **What are interest expense, interest income, tax EBITDA, all interest carries and EBITDA carry vintages, and the group/escape facts?** Test the current EUR 3m cliff, other escapes and the separate restriction for old interest carry; an Organschaft changes who is taxed.
7. **For outbound royalties or dividends, who is the recipient and where are its seat and management?** Obtain the actual treaty relief entitlement/extent, same-payer/same-recipient remuneration already received that calendar year, residence evidence, exemption/refund applications and facts for the applicable anti-abuse test.

## Sources

Read dates mean the selected operative clauses were read, not merely that the URL opened. Unchanged clauses reused from completed German proofs keep their original read dates; their 2026 applicability was checked on 27 November 2026.

| Source / portion read | URL | Read on |
|---|---|---|
| KStG § 7; selected operative clauses read | https://www.gesetze-im-internet.de/kstg_1977/__7.html | 2026-11-27 |
| KStG § 1; selected operative clauses read | https://www.gesetze-im-internet.de/kstg_1977/__1.html | 2026-11-27 |
| AO § 10; selected operative clauses read | https://www.gesetze-im-internet.de/ao_1977/__10.html | 2026-11-27 |
| AO § 11; selected operative clauses read | https://www.gesetze-im-internet.de/ao_1977/__11.html | 2026-11-27 |
| KStG § 2; selected operative clauses read | https://www.gesetze-im-internet.de/kstg_1977/__2.html | 2026-11-27 |
| AO § 12; selected operative clauses read | https://www.gesetze-im-internet.de/ao_1977/__12.html | 2026-11-27 |
| KStG § 1a; selected operative clauses read | https://www.gesetze-im-internet.de/kstg_1977/__1a.html | 2026-11-27 |
| MinStG § 1; selected operative clauses read | https://www.gesetze-im-internet.de/minstg/__1.html | 2026-11-27 |
| MinStG § 101; selected operative clauses read | https://www.gesetze-im-internet.de/minstg/__101.html | 2026-11-27 |
| KStG § 23; selected operative clauses read | https://www.gesetze-im-internet.de/kstg_1977/__23.html | 2026-11-27 |
| KStG § 24; selected operative clauses read | https://www.gesetze-im-internet.de/kstg_1977/__24.html | 2026-11-27 |
| SolzG § 3; selected operative clauses read | https://www.gesetze-im-internet.de/solzg_1995/__3.html | 2026-11-27 |
| SolzG § 4; selected operative clauses read | https://www.gesetze-im-internet.de/solzg_1995/__4.html | 2026-11-27 |
| GewStG § 2; selected operative clauses read | https://www.gesetze-im-internet.de/gewstg/__2.html | 2026-11-27 |
| GewStG § 11; reused exact clauses, applicability checked | https://www.gesetze-im-internet.de/gewstg/__11.html | 2026-11-27 |
| GewStG § 16; reused exact clauses, applicability checked | https://www.gesetze-im-internet.de/gewstg/__16.html | 2026-11-27 |
| BMF trade-tax transition; reused exact clauses, applicability checked | https://www.bundesfinanzministerium.de/Content/DE/Glossareintraege/G/gewerbesteuer.html?view=renderHelp | 2026-11-27 |
| GewStG § 36; reused exact clauses, applicability checked | https://www.gesetze-im-internet.de/gewstg/__36.html | 2026-11-27 |
| EStG § 4; reused exact clauses, applicability checked | https://www.gesetze-im-internet.de/estg/__4.html | 2026-10-29 |
| GewStG § 8; reused exact clauses, applicability checked | https://www.gesetze-im-internet.de/gewstg/__8.html | 2026-11-27 |
| GewStG § 9; selected operative clauses read | https://www.gesetze-im-internet.de/gewstg/__9.html | 2026-11-27 |
| KStG § 8; selected operative clauses read | https://www.gesetze-im-internet.de/kstg_1977/__8.html | 2026-11-27 |
| EStG § 5b; selected operative clauses read | https://www.gesetze-im-internet.de/estg/__5b.html | 2026-11-27 |
| KStG § 10; selected operative clauses read | https://www.gesetze-im-internet.de/kstg_1977/__10.html | 2026-11-27 |
| KStG § 8b; selected operative clauses read | https://www.gesetze-im-internet.de/kstg_1977/__8b.html | 2026-11-27 |
| EStG § 7; selected operative clauses read | https://www.gesetze-im-internet.de/estg/__7.html | 2026-11-27 |
| EStG § 6; selected operative clauses read | https://www.gesetze-im-internet.de/estg/__6.html | 2026-11-27 |
| EStG § 4h; selected operative clauses read | https://www.gesetze-im-internet.de/estg/__4h.html | 2026-11-27 |
| KStG § 8a; selected operative clauses read | https://www.gesetze-im-internet.de/kstg_1977/__8a.html | 2026-11-27 |
| EStG § 10d; selected operative clauses read | https://www.gesetze-im-internet.de/estg/__10d.html | 2026-11-27 |
| EStG § 52; selected operative clauses read | https://www.gesetze-im-internet.de/estg/__52.html | 2026-11-27 |
| BGBl.2024 I Nr.108, Art.6 and35(9), pages11/36; selected operative clauses read | https://www.recht.bund.de/bgbl/1/2024/108/regelungstext.pdf?__blob=publicationFile&v=1 | 2026-11-27 |
| GewStG § 10a; reused exact clauses, applicability checked | https://www.gesetze-im-internet.de/gewstg/__10a.html | 2026-11-27 |
| KStG § 8c; selected operative clauses read | https://www.gesetze-im-internet.de/kstg_1977/__8c.html | 2026-11-27 |
| KStG § 14; selected operative clauses read | https://www.gesetze-im-internet.de/kstg_1977/__14.html | 2026-11-27 |
| KStG § 17; selected operative clauses read | https://www.gesetze-im-internet.de/kstg_1977/__17.html | 2026-11-27 |
| KStG § 31; selected operative clauses read | https://www.gesetze-im-internet.de/kstg_1977/__31.html | 2026-11-27 |
| GewStG § 14a; reused exact clauses, applicability checked | https://www.gesetze-im-internet.de/gewstg/__14a.html | 2026-11-27 |
| AO § 149; reused exact clauses, applicability checked | https://www.gesetze-im-internet.de/ao_1977/__149.html | 2026-11-26 |
| AO § 108; reused exact clauses, applicability checked | https://www.gesetze-im-internet.de/ao_1977/__108.html | 2026-11-26 |
| EGAO Art.97 § 36; reused exact clauses, applicability checked | https://www.gesetze-im-internet.de/aoeg_1977/art_97__36.html | 2026-11-26 |
| EStG § 37; selected operative clauses read | https://www.gesetze-im-internet.de/estg/__37.html | 2026-11-27 |
| EStG § 36; selected operative clauses read | https://www.gesetze-im-internet.de/estg/__36.html | 2026-11-27 |
| AO § 152; selected operative clauses read | https://www.gesetze-im-internet.de/ao_1977/__152.html | 2026-11-27 |
| AO § 233a; reused exact clauses, applicability checked | https://www.gesetze-im-internet.de/ao_1977/__233a.html | 2026-11-26 |
| AO § 238; reused exact clauses, applicability checked | https://www.gesetze-im-internet.de/ao_1977/__238.html | 2026-11-26 |
| AO § 240; selected operative clauses read | https://www.gesetze-im-internet.de/ao_1977/__240.html | 2026-11-27 |
| AO § 224; selected operative clauses read | https://www.gesetze-im-internet.de/ao_1977/__224.html | 2026-11-27 |
| EStG § 43; selected operative clauses read | https://www.gesetze-im-internet.de/estg/__43.html | 2026-11-27 |
| EStG § 43a; selected operative clauses read | https://www.gesetze-im-internet.de/estg/__43a.html | 2026-11-27 |
| EStG § 43b; selected operative clauses read | https://www.gesetze-im-internet.de/estg/__43b.html | 2026-11-27 |
| EStG § 50c; selected operative clauses read | https://www.gesetze-im-internet.de/estg/__50c.html | 2026-11-27 |
| EStG § 44a; selected operative clauses read | https://www.gesetze-im-internet.de/estg/__44a.html | 2026-11-27 |
| EStG § 50d; selected operative clauses read | https://www.gesetze-im-internet.de/estg/__50d.html | 2026-11-27 |
| KStG § 32; selected operative clauses read | https://www.gesetze-im-internet.de/kstg_1977/__32.html | 2026-11-27 |

Not yet confirmed: the 2026 ELSTER form/field map (the 2026 help page could not be read on 2026-11-27); the 2025 names above are historical only. Actual treaty residence/PE and foreign-tax relief, special entities/Pillar Two computation, shareholder loans/hybrids/financial-sector cases, ownership-change exceptions and continuing-business relief, group-ratio/mixed interest-carry worksheets, defective tax-group agreements, special interest/penalty cases and the held interest/royalty/CFC/exit outcomes are not usable determinations. Original case facts are retained in their holds. Check this point with one of our partner accountants.
