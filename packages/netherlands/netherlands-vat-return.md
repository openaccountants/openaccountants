---
name: netherlands-vat-return
description: Use this skill whenever asked to prepare, review, or classify transactions for a Netherlands VAT return (OB aangifte / btw-aangifte) for a self-employed individual or small business in the Netherlands. Trigger on phrases like "prepare OB aangifte", "Dutch VAT return", "BTW aangifte", "classify transactions for Dutch VAT", or any request involving Netherlands VAT filing. This skill covers the Netherlands only, standard BTW regime. Kleineondernemersregeling (KOR), partial exemption, margin scheme (margeregeling), and VAT groups (fiscale eenheid) are in the refusal catalogue. MUST be loaded alongside BOTH vat-workflow-base v0.1 or later AND eu-vat-directive v0.1 or later. ALWAYS read this skill before touching any Dutch VAT work.
version: 2.0
jurisdiction: NL
tax_year: 2026
last_updated: 2026-09-27
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Netherlands VAT return (aangifte omzetbelasting, btw-aangifte)

## Scope and who this is for ([Belastingdienst: notes to the 2026 VAT return](https://download.belastingdienst.nl/belastingdienst/docs/toelichting_bij_btw_aangifte_ob0731t62fd.pdf))

This Guide covers preparing and filing the Dutch VAT return (btw-aangifte, also called aangifte omzetbelasting) for a business **established in the Netherlands**. It covers a sole trader (eenmanszaak), a partnership (vof, maatschap) or a company (bv, nv) that is registered for VAT and uses the normal rules. The primary year is **2026** (calendar year). There is a dated section for the **2025** returns and corrections that are being dealt with now.

It covers:
- which periods apply (month, quarter, year) and the deadlines;
- the boxes (rubrieken) 1a to 5b, and what goes where;
- the 21% and 9% rates, including the 2026 change for accommodation;
- the small business scheme (kleineondernemersregeling, KOR) and the EU version (EU-KOR) that started in 2025;
- reverse charge, intra-EU supplies and acquisitions, and the ICP listing (opgaaf intracommunautaire prestaties);
- input VAT (voorbelasting), including the BUA limits, private use and the car;
- corrections (suppletie), penalties and tax interest (belastingrente).

The practical rules come from the Belastingdienst's own pages and its notes to the 2026 return ("Toelichting bij de btw-aangifte (omzetbelasting) 2026"). Statute points cite the Wet op de omzetbelasting 1968 ("Wet OB 1968") as in force from 1 January 2026 ([wetten.overheid.nl](https://wetten.overheid.nl/BWBR0002629/2026-01-01)).

This Guide does **not** cover businesses established outside the Netherlands (they use separate notes and later deadlines), fiscal unities, the margin scheme, the travel agency scheme, real estate transactions, OSS returns, or the Caribbean Netherlands (Bonaire, Sint Eustatius and Saba). See "When to refuse or refer".

Figures in this Guide were checked against the Belastingdienst sources on 27 September 2026. Penalty amounts and the tax interest rate can change from year to year, so check the linked page before relying on them for a later period.

## Ask the client first

- Is the business established in the Netherlands? What is its legal form (eenmanszaak, vof, maatschap, bv, nv)?
- Is it registered for VAT, and does it have its VAT id (btw-id) and turnover tax number (ob-nummer)? The ob-nummer is used only with the Belastingdienst; the btw-id goes on invoices ([notes 2026](https://download.belastingdienst.nl/belastingdienst/docs/toelichting_bij_btw_aangifte_ob0731t62fd.pdf)). A Dutch btw-id is NL, then 9 digits, the letter B and a 2-digit sub-number, for example NL123456789B01 ([btw-id and ob-nummer](https://www.belastingdienst.nl/wps/wcm/connect/nl/btw/content/btw-identificatienummer-en-omzetbelastingnummer)). Check EU customers' VAT ids and, where available, names and addresses on the European Commission's VIES site. German customer names and addresses cannot be checked there; VIES can still validate the German VAT id ([checking a btw-id](https://www.belastingdienst.nl/wps/wcm/connect/nl/btw/content/btw-id-controleren)).
- Does it take part in the KOR, or is it thinking of joining or leaving? A KOR participant does not file normal returns ([what the KOR means](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/hoe_werkt_de_btw/kleineondernemersregeling/wat-betekent-meedoen-met-de-kleineondernemersregeling)).
- Which return period applies (month, quarter or year)? Ask for the annual letter (aangiftebrief) that lists the periods, deadlines and payment references ([filing period](https://www.belastingdienst.nl/wps/wcm/connect/nl/btw/content/wijziging-aangiftetijdvak-btw)).
- Which period is being prepared, and is it the last return of the calendar year? The year-end adjustments (private use, car, BUA, partial exemption) go in the last return ([last return of the year](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/btw_aangifte_doen_en_betalen/btw-aangifte-waar-moet-u-aan-denken/laatste-btw-aangifte-van-het-jaar)).
- Does the invoice VAT scheme apply? This method assumes invoice-based output VAT data. If the business uses a cash VAT scheme, refer its output-VAT timing for scheme-specific preparation before filling these boxes; do not select sales merely by invoice date.
- Sales invoices and purchase invoices for the period. Input VAT must be backed by invoices that meet the legal requirements ([notes 2026](https://download.belastingdienst.nl/belastingdienst/docs/toelichting_bij_btw_aangifte_ob0731t62fd.pdf)). A bank statement alone is not enough to support a deduction.
- Any sales that are exempt from VAT (for example medical, financial, insurance or residential letting)? If so, input VAT must be split.
- Customers or suppliers outside the Netherlands: which country, business or consumer, goods or services? For EU business customers, their VAT ids.
- Imports from outside the EU, and whether the business has an article 23 licence (vergunning artikel 23).
- A car of the business used privately (including commuting): catalogue price including VAT and bpm, first year of use, and whether a closing mileage record exists.
- Gifts, staff provisions and food and drink in restaurants and cafés during the year.
- Buildings, large renovations and other investment goods: purchase date, VAT deducted and the taxable share of use in the first year.
- Errors found in earlier returns, and when they were found.
- Refunds claimed for earlier periods that have not arrived yet.

## The method, step by step

1. **Confirm the business must file, and for which period.** A VAT-registered business always files the return that the Belastingdienst puts ready for it, even with nothing to declare. That is a nil return (0-aangifte or nihilaangifte) ([what to consider](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/btw_aangifte_doen_en_betalen/btw-aangifte-waar-moet-u-aan-denken)). A KOR participant does not file normal returns.
2. **Sort every sale** into: Dutch VAT at 21% (1a) or 9% (1b); private use (1d, normally the last return of the year; retained goods on business cessation go in the transfer period); 0% or VAT shifted to a Dutch customer (1e); exports (3a); intra-EU supplies of goods and B2B services (3b); installation and distance sales in other EU states (3c); OSS sales (not on this return). Exempt sales are not entered ([notes 2026](https://download.belastingdienst.nl/belastingdienst/docs/toelichting_bij_btw_aangifte_ob0731t62fd.pdf)).
3. **Sort every purchase that shifts VAT to the client**: domestic reverse charge (2a), goods or services from outside the EU (4a), goods or services from other EU states (4b). The client calculates and declares the VAT and, where the purchase is used for taxed activities, deducts it again in 5b.
4. **Collect deductible input VAT (5b)** from compliant invoices dated in the period, even if the supplier has not been paid yet. Take out purchases that are private, used for exempt or non-taxable activities, food and drink in hospitality, gifts and staff provisions disallowed under the applicable BUA conditions and exceptions, and VAT charged in error ([notes 2026](https://download.belastingdienst.nl/belastingdienst/docs/toelichting_bij_btw_aangifte_ob0731t62fd.pdf)).
5. **In the last return of the year, make the annual adjustments**: private use (1d), including the car; BUA over-limit amounts; the final taxable/exempt ratio; and revisions of investment goods ([last return of the year](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/btw_aangifte_doen_en_betalen/btw-aangifte-waar-moet-u-aan-denken/laatste-btw-aangifte-van-het-jaar)).
6. **Process past errors.** An error of €1,000 or less goes into the next return in the normal box. An error of more than €1,000 goes on a separate Suppletie form (see "Corrections").
7. **Round to whole euros** (you may round in the client's favour), put a minus sign before negative amounts, and let the program calculate the total ([notes 2026](https://download.belastingdienst.nl/belastingdienst/docs/toelichting_bij_btw_aangifte_ob0731t62fd.pdf)).
8. **File the ICP listing** for the ordinary intra-EU B2B transactions covered here. Reconcile it to box 3b for the same period. New or nearly new means of transport sold to non-VAT customers require a separate reporting route and referral ([ICP](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/zakendoen_met_het_buitenland/goederen_en_diensten_naar_andere_eu_landen/opgaaf_icp/opgaaf_icp)).
9. **File and pay by the deadline.** Payment counts on the day it is credited to the Belastingdienst's account, so allow for bank processing time ([filling in and sending](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/btw_aangifte_doen_en_betalen/btw-aangifte-waar-moet-u-aan-denken/hoe-btw-aangifte-invullen-en-versturen)).

### The boxes (rubrieken) of the 2026 return ([notes 2026](https://download.belastingdienst.nl/belastingdienst/docs/toelichting_bij_btw_aangifte_ob0731t62fd.pdf))

| Box | Dutch label | What goes in it |
| --- | --- | --- |
| 1a | Leveringen/diensten belast met hoog tarief | Domestic sales at 21%: turnover and VAT |
| 1b | Leveringen/diensten belast met laag tarief | Domestic sales at 9%: turnover and VAT |
| 1c | Leveringen/diensten belast met overige tarieven, behalve 0% | Only the sports canteen flat rate of 13% on total canteen receipts |
| 1d | Privégebruik | VAT on private use by the owner or staff. Normally in the last return of the year; on business cessation, goods retained privately are reported in the period they transfer to private ownership |
| 1e | Leveringen/diensten belast met 0% of niet bij u belast | Domestic 0% supplies (not exports or intra-EU supplies), and supplies where VAT is shifted to another business |
| 2a | Leveringen/diensten waarbij de btw naar u is verlegd | Domestic reverse charge **received** (for example construction subcontracting, or services to real estate from another EU state) |
| 3a | Leveringen naar landen buiten de EU (uitvoer) | Exports of goods, including goods placed in a customs warehouse |
| 3b | Leveringen naar of diensten in landen binnen de EU | Intra-EU supplies of goods and B2B services. Reconcile to the ICP listing for ordinary covered transactions; new means of transport have a separate reporting exception |
| 3c | Installatie/afstandsverkopen binnen de EU | Installation or assembly in another EU state, and distance sales where OSS is not used |
| 4a | Leveringen/diensten uit landen buiten de EU | Services from non-EU suppliers with VAT shifted to the client, and imports under an article 23 licence |
| 4b | Leveringen/diensten uit landen binnen de EU | Intra-EU acquisitions of goods, and services from EU suppliers with VAT shifted to the client |
| 5a | Verschuldigde btw (rubrieken 1 t/m 4) | Calculated by the program: total VAT due from boxes 1 to 4 ([step-by-step](https://www.belastingdienst.nl/wps/wcm/connect/nl/btw/content/ik-moet-btw-aangifte-doen-hoe-vul-ik-die-in)) |
| 5b | Voorbelasting | Deductible input VAT, including reverse-charged VAT declared in 2a, 4a or 4b |

Boxes 1a to 1d, 2a, 4a and 4b each have a turnover column and a VAT column. In 4a and 4b the amounts do not need to be split by rate. The program then works out the amount to pay or reclaim. The 2026 notes describe no other box that the business fills in. There is no box for a KOR reduction: KOR participants do not file normal returns, so do not look for or fill in one.

## Figures by year

### Rates ([Wet OB 1968, article 9](https://wetten.overheid.nl/BWBR0002629/2026-01-01))

| Rate | 2026 | 2025 | What it covers |
| --- | --- | --- | --- |
| Standard | 21% | 21% | Everything not exempt and not in the 9% or 0% lists |
| Reduced | 9% | 9% | Goods and services in Table I of the Wet OB 1968 (see below) |
| Zero | 0% | 0% | Table II: mainly exports, intra-EU supplies of goods and some cross-border services |

Article 9 says: "De belasting bedraagt 21 percent", with 9% for Table I and nil for Table II ([wetten.overheid.nl](https://wetten.overheid.nl/BWBR0002629/2026-01-01)).

**9% goods** include food, water, ornamental horticulture products, medicines and aids, art, collectors' items and antiques, and books and periodicals ([9% goods](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/tarieven_en_vrijstellingen/goederen_9_btw)).

**9% services** include repairs of bicycles, shoes and leather goods, clothing and household linen; hairdressers; some work on homes; camping; access to cultural and recreational events and facilities; performing artists; the chance to play sport and to bathe (including swimming pools and saunas); passenger transport; comparable e-books; news websites and apps; and food served in hospitality ([9% services](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/tarieven_en_vrijstellingen/diensten_9_btw)). On 27 September 2026 that list still included cultural events and sport. For 2026 the Belastingdienst lists accommodation as the rate change (below). If a client asks about a planned change for culture, media or sport, check the 9% services page for the period concerned rather than relying on news reports.

**Accommodation (logies) from 1 January 2026: 21%, not 9%.** This covers furnished short-stay accommodation in hotels, guesthouses and holiday businesses, including holiday homes, static caravans and seasonal letting of furnished rooms. Related facilities (gas, electricity, water, sanitary and laundry facilities, and parking with the stay) are also 21%. A payment made in 2025 for a stay in 2026 or later is also 21%, and so is a single-purpose voucher for such a stay ([accommodation rate](https://www.belastingdienst.nl/wps/wcm/connect/nl/btw/content/btw-logies)). Facilities offered **separately**, such as breakfast or access to a swimming pool or amusement park, stay at 9%. An all-in price is split by the market values of the parts ([news, 30 October 2025](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/berichten/nieuws/btw-logies)).

### Filing period thresholds ([filing period](https://www.belastingdienst.nl/wps/wcm/connect/nl/btw/content/wijziging-aangiftetijdvak-btw))

Most businesses file quarterly. A business can ask for monthly filing by letter. The Belastingdienst can impose monthly filing after late returns or payments. An **annual return** is possible on request only if **all** of these apply:
- the business pays less than €1,883 VAT a year;
- it has no article 23 licence;
- it is a natural person (eenmanszaak) or a partnership made up only of natural persons;
- it has less than €10,000 a year of **each** of: intra-EU supplies of goods, intra-EU services, intra-EU acquisitions, and intra-EU services received.

The Belastingdienst replies within 6 weeks. A change takes effect at the start of the next return period.

### KOR and EU-KOR

| Rule | Figure | Source |
| --- | --- | --- |
| Dutch KOR turnover limit, in the year of joining **and** the previous calendar year | Not more than €20,000 | [KOR conditions](https://www.belastingdienst.nl/wps/wcm/connect/nl/btw/content/kor-voorwaarden); [article 25a Wet OB 1968](https://wetten.overheid.nl/BWBR0002629/2026-01-01) |
| EU-KOR: total EU turnover (including the Netherlands), this year and last year | Not more than €100,000 | [EU-KOR](https://www.belastingdienst.nl/wps/wcm/connect/nl/btw/content/kleineondernemersregeling-in-de-europese-unie-eu-kor) |
| Later-year annual revision caused by joining or leaving the KOR | None if the qualifying annual revision total is less than €500; do not use this to waive first-use/full first-year adjustment | [Revision](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/btw_aftrekken/belaste_en_vrijgestelde_omzet/inschatting_van_het_gebruik2/herziening_aftrek_bij_investeringsgoederen2/herziening_aftrek_bij_investeringsgoederen) |

The KOR rules are in "KOR and EU-KOR in practice" below.

### Input VAT limits

| Rule | Figure | Source |
| --- | --- | --- |
| Gifts, business gifts and staff provisions (BUA) | For expenditure within the BUA exclusion, threshold is €227 per recipient per year excluding VAT; check the recipient condition and exceptions below | [BUA](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/btw_aftrekken/personeelsvoorzieningen_en_relatiegeschenken) |
| Gifts: the BUA limit applies only if the recipients could deduct | Less than 30% of the VAT themselves | [BUA](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/btw_aftrekken/personeelsvoorzieningen_en_relatiegeschenken) |
| Car private use, no mileage record | 2.7% of the catalogue price including VAT and bpm | [Car](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/btw_aftrekken/btw_en_de_auto/privegebruik_auto_van_de_zaak) |
| Car private use later than 4 years after the year the car was first used, or car bought without VAT deduction | 1.5% instead of 2.7% | [Car](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/btw_aftrekken/btw_en_de_auto/privegebruik_auto_van_de_zaak) |
| Revision follow-up of investment goods | Movables: year of first use plus 4 years; immovables: plus 9 years | [Investment services](https://www.belastingdienst.nl/wps/wcm/connect/nl/btw/content/btw-aftrek-investeringsdiensten) |
| Later-year revision threshold | After the year of first use, revise if the difference exceeds 10% of the first-year taxable-use percentage; first-year true-up is separate | [Revision](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/btw_aftrekken/belaste_en_vrijgestelde_omzet/inschatting_van_het_gebruik2/herziening_aftrek_bij_investeringsgoederen2/herziening_aftrek_bij_investeringsgoederen) |
| **New from 1 January 2026**: investment services (major work on immovable property) | From €30,000 excluding VAT, 5-year revision period | [Investment services](https://www.belastingdienst.nl/wps/wcm/connect/nl/btw/content/btw-aftrek-investeringsdiensten) |

### Corrections, ICP and payment

| Rule | Figure | Source |
| --- | --- | --- |
| Error processed in the next return | €1,000 or less | [Correcting a return](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/btw_aangifte_doen_en_betalen/aangifte_corrigeren) |
| Error that needs the Suppletie form, within 8 weeks of discovery | More than €1,000 | [Correcting a return](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/btw_aangifte_doen_en_betalen/aangifte_corrigeren) |
| ICP listing for goods may be quarterly | Not more than €50,000 of goods a quarter, in that quarter and each of the previous 4 quarters | [ICP period](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/zakendoen_met_het_buitenland/goederen_en_diensten_naar_andere_eu_landen/opgaaf_icp/tijdvak_opgaaf_icp/tijdvak_opgaaf_icp) |
| Distance sales and digital services to consumers in other EU states: threshold for taxation in the customer's state | €10,000 (last year and/or this year) | [notes 2026, box 3c](https://download.belastingdienst.nl/belastingdienst/docs/toelichting_bij_btw_aangifte_ob0731t62fd.pdf) |
| Paying by iDEAL or Wero from the online return | Amount due at most €50,000 | [notes 2026](https://download.belastingdienst.nl/belastingdienst/docs/toelichting_bij_btw_aangifte_ob0731t62fd.pdf) |

### Penalties and tax interest (belastingrente)

| Item | 2026 | 2025 | Source |
| --- | --- | --- | --- |
| Late or missing return (after a 7-day grace period) | €82 | Not re-checked; see the page for the year | [Late return](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/btw_aangifte_doen_en_betalen/boetes/u_doet_geen_of_te_laat_aangifte) |
| Late return, exceptional cases (for example often late) | Up to €165 | Not re-checked | [Special situations](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/btw_aangifte_doen_en_betalen/boetes/uitzonderlijke_of_bijzondere_situaties) |
| Late, missing or short payment | 3% of the amount, minimum €50, maximum €6,709 | Not re-checked | [Late payment](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/btw_aangifte_doen_en_betalen/boetes/u_betaalt_niet_te_laat_of_te_weinig) |
| Often late with payment | Up to 10%, never more than €6,709 a year | Not re-checked | [Special situations](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/btw_aangifte_doen_en_betalen/boetes/uitzonderlijke_of_bijzondere_situaties) |
| Too little declared, or too much refunded | 10% of the tax, never more than €6,709 a year | Not re-checked | [Special situations](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/btw_aangifte_doen_en_betalen/boetes/uitzonderlijke_of_bijzondere_situaties) |
| Vergrijpboete (gross negligence or intent) | Up to 100% of the tax | Same | [Special situations](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/btw_aangifte_doen_en_betalen/boetes/uitzonderlijke_of_bijzondere_situaties) |
| Belastingrente on VAT: rate for interest days falling in the year | 5% (from 1 January 2026) | 6.5% (days in 2025, for example interest on 2024 VAT) | [Tax interest rates](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/standaard_functies/prive/contact/rechten_en_plichten_bij_de_belastingdienst/belastingrente/overzicht_percentages_belastingrente) |

The penalty pages carry no year. The amounts above were checked on 27 September 2026. For a penalty relating to 2025, read the amount on the penalty decision itself.

## Rules in practice

### Reverse charge, intra-EU trade and the ICP listing ([notes 2026](https://download.belastingdienst.nl/belastingdienst/docs/toelichting_bij_btw_aangifte_ob0731t62fd.pdf))

- **Domestic reverse charge (verleggingsregeling)** can apply in the following categories, subject to the specific scheme conditions and thresholds: subcontracting and hiring out staff in construction, shipbuilding, cleaning and gardening; telecom services to another business; mobile phones, chips, games consoles, laptops and tablets; real estate where a taxed supply was chosen; waste and scrap; gas and electricity certificates; forced sales; gold; and emission rights. The **supplier** puts the turnover in 1e and writes "btw verlegd" and the customer's VAT id on the invoice. The **customer** calculates the VAT, declares it in 2a, and deducts it in 5b if the conditions are met. Declare the reverse-charged VAT even where an eligible matching deduction makes the net result nil; 5b only contains the amount actually deductible.
- **Ordinary intra-EU B2B supplies of goods (3b, 0%)** qualify for 0% only if the business can show from its records that the goods went to another EU state, that the customer is a business with a valid VAT id from another EU state, and that the ICP listing was filed on time, correctly and completely. Report goods in the period of the **invoice date**. Own goods moved to another EU state and call-off stock also need the relevant reporting checks; call-off stock is referred below. New or nearly new means of transport supplied to a non-VAT customer abroad are a separate exception: use the special invoice-copy and letter reporting route described in the official notes and refer before filing.
- **B2B services to EU businesses (3b)**: the customer declares the VAT in its own country. Report them in the period in which the **service was performed**; the invoice date does not matter. Some services are **not** reported in 3b or on the ICP listing: services that are exempt or 0% in the customer's state, OSS services, services connected with real estate, passenger transport, admission to events, restaurant and catering services, and short-term hire of means of transport.
- **Exports (3a)** are goods sent outside the EU.
- **Purchases from EU suppliers (4b)**: intra-EU acquisitions of goods, and services where the EU supplier shifted the VAT to the client. Services connected with real estate go in 2a instead. Report services in the period they were performed.
- **Purchases from non-EU suppliers (4a)**: services where the VAT was shifted to the client, and imports under an **article 23 licence**. With that licence, import VAT is not paid to Customs but declared in the return and deducted in 5b. For certain raw materials named in the law, the shift at import is compulsory and no licence is needed. **Without a licence**, import VAT is paid to Customs; it is ordinary input VAT and is deducted in 5b for goods used for taxed activities (article 15(1)(c) Wet OB 1968, [wetten.overheid.nl](https://wetten.overheid.nl/BWBR0002629/2026-01-01)).
- **ICP listing** ([ICP](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/zakendoen_met_het_buitenland/goederen_en_diensten_naar_andere_eu_landen/opgaaf_icp/opgaaf_icp)): lists intra-EU supplies of goods and services, transfers of own goods and call-off stock. It is filed in Mijn Belastingdienst Zakelijk, and no invitation is sent. Reconcile the total to box 3b for ordinary ICP-reportable transactions; separately identify the new/nearly new means-of-transport exception for a customer without a VAT identification number described above. Nothing is filed for a period with no such supplies. An error is corrected in the next listing.
- **VAT paid in other EU states** cannot be deducted in the Dutch return; it is reclaimed through the separate EU refund procedure.
- **United Kingdom**: a third country. Northern Ireland still counts as an EU state for goods, but not for services.

### Input VAT: what can and cannot be deducted

- Deduct in the period in which the VAT was charged on a compliant invoice, even if the supplier is still unpaid. Only purchases used for the business and for taxed activities qualify. Supplies at 0% or with VAT shifted to the customer count as taxed ([notes 2026](https://download.belastingdienst.nl/belastingdienst/docs/toelichting_bij_btw_aangifte_ob0731t62fd.pdf)).
- **Excluded or restricted**: private purchases; costs of exempt or non-taxable turnover (for example genuinely non-taxable subsidies or activities supplied without taxable consideration); **food and drink in hospitality (eten en drinken in de horeca)**; gifts, business gifts and staff provisions where the applicable BUA exclusion applies (see its recipient test and exceptions below); and VAT a supplier charged in error ([what is not deductible](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/btw_aftrekken/welke_btw_is_aftrekbaar/welke_btw_mag_u_niet_aftrekken)). A restaurant bill is not deductible at the time of purchase; there is nothing to correct later.
- **Items with no input VAT at all**: qualifying exempt financial/insurance services and exempt supplies or lettings of real estate carry no deductible VAT; examine the particular service rather than treating every bank fee as exempt ([exemptions](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/tarieven_en_vrijstellingen/vrijstellingen)), so there is nothing to deduct on them. Tax payments, wages, pension and social contributions, and loan or savings movements are not supplies and stay out of the return.
- **BUA (Besluit uitsluiting aftrek omzetbelasting 1968)** ([BUA](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/btw_aftrekken/personeelsvoorzieningen_en_relatiegeschenken)): staff provisions (housing, fitness, recreation, pay in kind, Christmas packages), private transport of staff, gifts and business gifts. For expenditure within the BUA exclusion, the de minimis threshold is €227 excluding VAT per recipient per year. Check the recipient condition for gifts, exceptions for certain staff provisions, and the separate staff food-and-drink rules before applying the threshold. For gifts, the limit applies where the recipients could deduct less than 30% of the VAT themselves if they bought the item. Employees' own contributions may **not** be netted off when testing the threshold ([notes 2026](https://download.belastingdienst.nl/belastingdienst/docs/toelichting_bij_btw_aangifte_ob0731t62fd.pdf)). If more was spent and the VAT was deducted, correct it in the last return of the year. The BUA does **not** apply to staff's private use of a company car; that follows the car rules. Unsaleable food donated to a food bank needs no correction.
- **Mixed taxable and exempt turnover** ([taxable and exempt turnover](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/btw_aftrekken/belaste_en_vrijgestelde_omzet)): VAT on costs used only for taxed turnover is fully deductible; on costs used only for exempt turnover, not deductible; on shared costs, partly deductible. Split by the ratio of taxed to exempt turnover, or by actual use if it can be shown. Check the estimate at the end of the year and correct it in the last return.
- **Business and private use** ([mixed use](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/btw_aftrekken/privegebruik/gemengd_gebruik)): depending on the type of goods or services, possible treatments are no deduction, deduction of the business part only, or deduction followed by VAT on private use at year-end (1d). Do not treat these as freely interchangeable elections; apply the relevant investment-good or other-item rules. Private use of gas, water, electricity and telephone also goes in 1d ([notes 2026](https://download.belastingdienst.nl/belastingdienst/docs/toelichting_bij_btw_aangifte_ob0731t62fd.pdf)).
- **Bad debts**: VAT can be reclaimed once a debt is certain to be (partly) uncollectable, and at the latest 1 year after the agreed payment date. If no term was agreed, the statutory term of 30 days after the customer received the invoice applies, so the 1-year period runs from the end of those 30 days. Deduct both the VAT and the turnover in 1a or 1b of that period ([notes 2026](https://download.belastingdienst.nl/belastingdienst/docs/toelichting_bij_btw_aangifte_ob0731t62fd.pdf)).

### Investment-use changes: first year versus later years

At first use, reassess any earlier deduction using the use at that time; reconcile again at the end of the year of first use using the full-year position. Do not apply the later-year tolerance to avoid this first-year true-up. For subsequent years within the revision period, compare the change in taxable-use percentage with 10% of the original first-year percentage. Where revision is required, the annual amount uses one fifth of the original VAT for movable investment goods/services or one tenth for immovable investment goods, multiplied by the change in use. A disposal can accelerate remaining-year revision. Refer property and investment-service calculations as indicated below. [Investment revision](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/btw_aftrekken/belaste_en_vrijgestelde_omzet/inschatting_van_het_gebruik2/herziening_aftrek_bij_investeringsgoederen2/herziening_aftrek_bij_investeringsgoederen) [Investment services](https://www.belastingdienst.nl/wps/wcm/connect/nl/btw/content/btw-aftrek-investeringsdiensten)

### The company car ([car private use](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/btw_aftrekken/btw_en_de_auto/privegebruik_auto_van_de_zaak))

- VAT on buying, maintaining and using a business car (including a lease car) is deductible to the extent it is used for taxed turnover. Private use, **including commuting**, is then charged in 1d in the last return of the calendar year.
- With a closing mileage record (or other evidence of the business/private split), pay VAT on the actual private use and enter the base amount in the left column.
- Without such a record, pay 2.7% of the catalogue price including VAT and bpm, and enter "0" in the left column. Apply 1.5% instead if the private use is later than 4 years after the year the car was first used, or if no VAT was deducted on purchase (for example a margin car, or a car bought from a private person). Reduce the charge pro rata for a car bought during the year, and for exempt use.
- **Cap**: during the 4 years after the year of purchase, the charge is not more than the VAT deducted that year on maintenance and use, plus one fifth of the VAT deducted on purchase. After that period, or if no purchase VAT was deducted, the cap is the VAT deducted that year on maintenance and use.
- For a bv, the director-shareholder is treated as an employee. If an employee contributes for private use, first establish whether the contribution covers the attributable costs, including both VAT-bearing and other costs. If cost-covering, account for VAT on the contribution. Only for a non-cost-covering contribution compare VAT on the contribution with the flat-rate amount. Where it is lower, apply the source's deemed cost-covering amount or permitted flat-rate option, avoiding double taxation of the contribution; refer if the cost allocation is uncertain.
- No VAT is deductible on allowances paid to employees for business use of their **own** cars.

### KOR and EU-KOR in practice

- **Who**: businesses established in the Netherlands, including sole traders, partnerships and legal entities such as foundations, associations and bv's, whose counted turnover is not more than €20,000 in the calendar year of joining and in the previous calendar year ([KOR conditions](https://www.belastingdienst.nl/wps/wcm/connect/nl/btw/content/kor-voorwaarden)).
- **Counted turnover**: supplies at 21%, 9% and 0% (including exports and intra-EU supplies), supplies where VAT is shifted to another Dutch business, and some exempt real estate, financial and insurance turnover. **Not counted**: VAT on private use, sales of the business's own investment goods, supplies taxed in another country, and intra-EU acquisitions. Before joining, count turnover excluding VAT. All sub-numbers of one business count together, and the choice applies to all of them.
- **Effect**: no VAT is charged or shown on invoices, no normal returns are filed, and no input VAT can be deducted (including VAT paid in other EU states). An earlier deduction may have to be revised. Some supplies stay outside the exemption: real estate used in the business, and new means of transport sent to another EU state. An occasional return may still be needed, for example for some EU purchases ([what the KOR means](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/hoe_werkt_de_btw/kleineondernemersregeling/wat-betekent-meedoen-met-de-kleineondernemersregeling)). Joining ends an article 23 licence and rules out taxed letting of real estate.
- **Joining**: only after VAT registration, online. It takes effect at the earliest from the next quarter or return period, allowing 4 weeks' processing time. To join from 1 January 2027, the application must arrive by 4 December 2026. Keep filing returns until the letter with the final start date arrives, usually within 8 weeks ([joining the KOR](https://www.belastingdienst.nl/wps/wcm/connect/nl/btw/content/aanmelden-kor)).
- **Leaving** ([leaving the KOR](https://www.belastingdienst.nl/wps/wcm/connect/nl/btw/content/afmelden-kor)): if turnover goes above €20,000 in a calendar year, the exemption ends immediately. The supply that takes turnover over the limit is itself taxed in full, and the business must deregister at once. A voluntary exit takes effect only from the first day of a return period; apply at least 4 weeks ahead. After leaving, the business cannot rejoin for the rest of that calendar year and the next year.
- **EU-KOR (since 1 January 2025)**: a Dutch-established business can choose exemption in one or more other EU states if its EU-wide turnover (including the Netherlands) is not more than €100,000 in this year and last year, it stays under each chosen state's national threshold, and it does not use the import scheme (Invoerregeling). It then files a quarterly turnover report (opgaaf kwartaalomzet) with the Belastingdienst. Above €100,000 it must deregister at once ([EU-KOR](https://www.belastingdienst.nl/wps/wcm/connect/nl/btw/content/kleineondernemersregeling-in-de-europese-unie-eu-kor)). Each state's national threshold and tolerance differ, so check that state's rules.

## Boundary and exception table

| Situation | Treatment | Source |
| --- | --- | --- |
| Error in an earlier return of exactly €1,000 | Next return, normal box ("maximaal €1000") | [Correcting a return](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/btw_aangifte_doen_en_betalen/aangifte_corrigeren) |
| Error of any amount above €1,000 | Suppletie form, within 8 weeks of discovery ("meer dan € 1.000") | [Correcting a return](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/btw_aangifte_doen_en_betalen/aangifte_corrigeren) |
| KOR turnover of exactly €20,000 | Still eligible ("maximaal € 20.000") | [KOR conditions](https://www.belastingdienst.nl/wps/wcm/connect/nl/btw/content/kor-voorwaarden) |
| KOR turnover goes one euro above €20,000 during the year | Exemption ends at once; that supply is taxed in full | [Leaving the KOR](https://www.belastingdienst.nl/wps/wcm/connect/nl/btw/content/afmelden-kor) |
| BUA spending of exactly €227 per recipient (excluding VAT) | The BUA threshold itself does not block deduction, subject to the recipient/exception rules and ordinary deduction conditions | [BUA](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/btw_aftrekken/personeelsvoorzieningen_en_relatiegeschenken) |
| Goods supplied to EU businesses of exactly €50,000 in a quarter | Quarterly ICP remains possible only if this quarter and each of the preceding four quarters satisfy the threshold | [ICP period](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/zakendoen_met_het_buitenland/goederen_en_diensten_naar_andere_eu_landen/opgaaf_icp/tijdvak_opgaaf_icp/tijdvak_opgaaf_icp) |
| Later-year change in taxable use of an investment good equal to 10% of the first-year percentage | No later-year revision ("kleiner dan of gelijk aan") | [Revision](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/btw_aftrekken/belaste_en_vrijgestelde_omzet/inschatting_van_het_gebruik2/herziening_aftrek_bij_investeringsgoederen2/herziening_aftrek_bij_investeringsgoederen) |
| Return arrives within 7 calendar days after the deadline | No late-filing penalty | [Late return](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/btw_aangifte_doen_en_betalen/boetes/u_doet_geen_of_te_laat_aangifte) |
| Payment within 7 days after the deadline, previous return paid on time and in full | No payment penalty, only a notice (verzuimmededeling) | [Late payment](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/btw_aangifte_doen_en_betalen/boetes/u_betaalt_niet_te_laat_of_te_weinig) |
| Payment within 7 days, but the previous return was paid late | Payment penalty applies | [Late payment](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/btw_aangifte_doen_en_betalen/boetes/u_betaalt_niet_te_laat_of_te_weinig) |
| Return both late and underpaid | Two separate penalties | [Both](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/btw_aangifte_doen_en_betalen/boetes/samenloop_betaal_en_aangifteverzuim) |
| Suppletie for underpaid VAT sent within 3 months after the year | No belastingrente | [Tax interest on VAT](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/standaard_functies/prive/contact/rechten_en_plichten_bij_de_belastingdienst/belastingrente/belastingrente_betalen_bij_loonbelasting_btw_en_overdrachtsbelasting) |
| Car first used in 2021; private use in 2026 | 1.5%: 2026 is later than 4 years after 2021 | [Car](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/btw_aftrekken/btw_en_de_auto/privegebruik_auto_van_de_zaak) |
| Hotel stay in 2026 paid in 2025 | 21% | [Accommodation](https://www.belastingdienst.nl/wps/wcm/connect/nl/btw/content/btw-logies) |
| Breakfast sold separately from the room in 2026 | 9% | [News](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/berichten/nieuws/btw-logies) |
| Services from an EU supplier connected with Dutch real estate | Box 2a, not 4b | [notes 2026](https://download.belastingdienst.nl/belastingdienst/docs/toelichting_bij_btw_aangifte_ob0731t62fd.pdf) |
| Ordinary intra-EU B2B goods supply without the customer's valid EU VAT id | Do not apply ordinary B2B 0% treatment; investigate and refer. The new-means-of-transport exception has separate rules | [notes 2026](https://download.belastingdienst.nl/belastingdienst/docs/toelichting_bij_btw_aangifte_ob0731t62fd.pdf) |
| Nothing to declare in the period | File a nil return anyway | [What to consider](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/btw_aangifte_doen_en_betalen/btw-aangifte-waar-moet-u-aan-denken) |

## Worked cases

Cases one to four use the Belastingdienst's published example figures, with arithmetic recomputed. Case seven explicitly reuses a dated official example. The other cases are illustrative decision checks.

### Case 1: a simple quarterly return, 2026 ([step-by-step](https://www.belastingdienst.nl/wps/wcm/connect/nl/btw/content/ik-moet-btw-aangifte-doen-hoe-vul-ik-die-in))

A jewellery maker files quarterly. Domestic sales at 21% are €5,000 excluding VAT, so the VAT is €1,050. Purchases for the business are €1,000 excluding VAT, with €210 VAT on valid invoices.
- 1a: turnover €5,000, VAT €1,050. Rubrieken 3 and 4: nothing.
- 5a (calculated): €1,050. 5b: €210.
- Amount to pay: €1,050 − €210 = €840. For Q3 2026 it must be filed and paid by 31 October 2026 ([deadlines](https://www.belastingdienst.nl/wps/wcm/connect/nl/btw/content/uiterste-aangifte-en-betaaldatums)).

### Case 2: car private use with no mileage record ([car](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/btw_aftrekken/btw_en_de_auto/privegebruik_auto_van_de_zaak))

The catalogue price is €45,000 including VAT and bpm. All VAT on purchase, maintenance and use was deducted, and there is no mileage record.
- Full year: 2.7% × €45,000 = €1,215, declared in 1d in the last return of the year, with "0" in the left column.
- Car bought on 1 September: only 4 of 12 months count, so the charge is 4/12 of €1,215, which is €405.
- In a separate full-year variant, 40% of use is for exempt turnover and only 60% of purchase/use VAT was deductible; the charge is therefore 60% of €1,215, or €729. This is not combined with the part-year variant.

### Case 3: the cap on the car charge ([car](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/btw_aftrekken/btw_en_de_auto/privegebruik_auto_van_de_zaak))

A used car was bought last year for €18,150, with a catalogue price of €75,000. Purchase VAT of €3,150 was deducted. This year €210 VAT on maintenance and €525 on use were deducted, and there is no mileage record.
- Normal charge: 2.7% × €75,000 = €2,025.
- Cap: €210 + €525 + 1/5 × €3,150 = €1,365. **Declare €1,365.**

### Case 4: all-in hotel price, 2026 ([news, 30 October 2025](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/berichten/nieuws/btw-logies))

The market value of a weekend stay for two is €280 and of breakfast €70, together €350. Accommodation is 280/350 = 80% and breakfast is 20%. An all-in price of €150 excluding VAT splits into €120 at 21% (accommodation) and €30 at 9% (breakfast). The VAT is therefore €25.20 plus €2.70 = €27.90, entered as €120 and €25.20 in 1a and €30 and €2.70 in 1b (rounded to whole euros on the return).

### Case 5: correcting an error ([correcting a return](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/btw_aangifte_doen_en_betalen/aangifte_corrigeren))

- In the Q2 2026 return the client under-claimed €100 input VAT. Add €100 to 5b in the Q3 2026 return; no form is needed.
- In February 2026 the client finds that 2025 sales VAT was understated by €4,000. That is more than €1,000, so a Suppletie is compulsory, within 8 weeks. Filed before 1 April 2026 (within 3 months after 2025), it attracts **no belastingrente**. The client then waits for the additional assessment (naheffingsaanslag) before paying. If the Belastingdienst finds the error first, a penalty can follow. Not filing a suppletie can lead to a vergrijpboete.

### Case 6: late payment penalty, 2026 ([late payment](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/btw_aangifte_doen_en_betalen/boetes/u_betaalt_niet_te_laat_of_te_weinig))

A Q1 2026 return showing €10,000 VAT was filed on time, but the money was credited on 20 May 2026, after the 7-day grace period. Penalty: 3% × €10,000 = €300 (within the €50 minimum and €6,709 maximum). If the return had also arrived after the grace period, a separate €82 late-filing penalty would apply as well.

### Case 7: crossing the KOR limit ([leaving the KOR](https://www.belastingdienst.nl/wps/wcm/connect/nl/btw/content/afmelden-kor))

This is the Belastingdienst's own 2024 example; the rule is unchanged for 2026. A KOR participant has turnover of €19,750 on 15 September. The next day it receives a €500 advance, which takes turnover over €20,000. The exemption lapses from 16 September. The €500 advance is fully taxable, and the business deregisters with effect from 16 September. It cannot rejoin for the rest of that year and the next year.

### Case 8: services to a German business and software from an Irish supplier

Assume a Dutch consultant making only taxed supplies, a German business customer with a validated VAT id, and an ordinary B2B consultancy service performed in Q3 2026. The consultant also receives a valid reverse-charge invoice from an Irish supplier for a business-only online subscription; no exemption, special place-of-supply rule or fixed-establishment exception applies. Before the sale, the consultant checks the German customer's VAT id (the Belastingdienst's btw-id check page explains how).
- Consultancy: no Dutch VAT. The turnover goes in 3b for the quarter in which the service was performed, and on the ICP listing for that period, due within 1 month after the period ([ICP notes 2026](https://download.belastingdienst.nl/belastingdienst/docs/toelichting-digitale-opgaaf-intracomm-pres-ob1291t62fd.pdf)).
- Irish subscription: the value goes in 4b with the VAT the client calculates at the Dutch rate; the same VAT is deductible in 5b on these assumptions. Net result nil because the business-only subscription supports only taxed supplies ([notes 2026](https://download.belastingdienst.nl/belastingdienst/docs/toelichting_bij_btw_aangifte_ob0731t62fd.pdf)).

### Case 9: correcting a nil-result Suppletie ([correcting a return](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/btw_aangifte_doen_en_betalen/aangifte_corrigeren))

A submitted correction changes reported turnover but produces neither VAT payable nor a refund. The business later discovers that the turnover allocation still needs amendment. No decision is issued for the nil-result correction: fill in and submit the correction form again. Do not wait for a decision that will not arrive. Where a refund decision or additional assessment is issued, use the objection route instead.

### Further decision checks

- **First-year adjustment:** an investment's actual first-year taxable use differs from the initial deduction assumption. Reconcile the first-use and year-end deduction; do not apply the later-year tolerance to suppress this adjustment. [Investment revision](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/btw_aftrekken/belaste_en_vrijgestelde_omzet/inschatting_van_het_gebruik2/herziening_aftrek_bij_investeringsgoederen2/herziening_aftrek_bij_investeringsgoederen)
- **Employee car contribution:** a contribution demonstrably covers the attributable private-use costs. Account for VAT on that contribution; do not automatically substitute the flat-rate correction. [Car private use](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/btw_aftrekken/btw_en_de_auto/privegebruik_auto_van_de_zaak)
- **Business cessation:** goods on which VAT was deducted transfer to private ownership when the business stops. Report the applicable VAT in that period; do not wait for the final calendar-year return. [Return notes](https://download.belastingdienst.nl/belastingdienst/docs/toelichting_bij_btw_aangifte_ob0731t62fd.pdf)

## When to refuse or refer

- **KOR participant**: no normal return is due. Help only with the decision to join or leave, the turnover test and occasional returns. Refer any revision of earlier deductions caused by joining.
- **Business not established in the Netherlands**: it uses different notes and later deadlines ([deadlines](https://www.belastingdienst.nl/wps/wcm/connect/nl/btw/content/uiterste-aangifte-en-betaaldatums)). A fiscal representative may be required ([fiscal representative](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/btw_aangifte_doen_en_betalen/fiscaal_vertegenwoordiger)). Refer.
- **Fiscal unity for VAT (fiscale eenheid)**: one combined return and special login rules. Refer.
- **Significant exempt turnover alongside taxed turnover** (partial exemption), beyond a simple ratio: refer, especially where buildings or investment services are involved.
- **Real estate**: sale or letting of buildings, the option for taxed letting, new buildings, major renovations (investment services of €30,000 or more from 2026), and revision of immovable property. Refer.
- **Cash VAT scheme timing, margin scheme, travel agency scheme, sports canteen flat rate or specialist agricultural VAT questions**: refer for the applicable method; do not import ordinary invoice-based timing.
- **OSS (One Stop Shop) and import scheme returns**: these are separate returns and are not covered here. Refer.
- **Imports** without an article 23 licence, call-off stock, and new or nearly new means of transport supplied abroad to non-VAT customers: refer. The last category can be an intra-EU supply despite no customer VAT id; follow the official invoice-copy and letter reporting route instead of inserting a fictitious customer VAT id into ICP.
- **Suspected VAT fraud** in the supply chain (for example carousel fraud): if the client knew or should have known, deduction can be refused. Refer at once ([notes 2026](https://download.belastingdienst.nl/belastingdienst/docs/toelichting_bij_btw_aangifte_ob0731t62fd.pdf)).
- **Caribbean Netherlands (Bonaire, Sint Eustatius, Saba)**: outside the Dutch VAT return. Refer.
- **Penalty decisions, a vergrijpboete, objections or a dispute with the Belastingdienst**: refer to a Dutch belastingadviseur.
- **Income tax or corporate income tax questions**: use the Guides for those taxes.
- **No invoices at all**: do not claim input VAT from a bank statement alone. Ask for the invoices.

## Filing and payment

### Deadlines for 2026 periods ([deadlines](https://www.belastingdienst.nl/wps/wcm/connect/nl/btw/content/uiterste-aangifte-en-betaaldatums))

Monthly and quarterly returns are due, and must be paid, by the last day of the month after the period ("uiterlijk op de laatste dag van de maand die volgt op het kwartaal of de maand"). An annual return is due before 1 April of the next year ([what to consider](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/btw_aangifte_doen_en_betalen/btw-aangifte-waar-moet-u-aan-denken)). The date that counts is the date of receipt; for payment, the date the money reaches the Belastingdienst's account.

| Period | Return and payment must be received by |
| --- | --- |
| Q1 2026 | 30 April 2026 |
| Q2 2026 | 31 July 2026 |
| Q3 2026 | 31 October 2026 |
| Q4 2026 | 31 January 2027 |
| Month (for example August 2026) | 30 September 2026 (the last day of the next month) |
| December 2026 | 31 January 2027 |
| Year 2026 | 31 March 2027 |

Returns filed with software can be sent from the 24th of the last month of the period; earlier filing is rejected. An **extension** is given only for a serious calamity, requested in writing ([notes 2026](https://download.belastingdienst.nl/belastingdienst/docs/toelichting_bij_btw_aangifte_ob0731t62fd.pdf)).

### Returns for 2025 being dealt with now

- Q4 2025 and December 2025 returns were due by 31 January 2026, and the 2025 annual return by 31 March 2026 ([deadlines](https://www.belastingdienst.nl/wps/wcm/connect/nl/btw/content/uiterste-aangifte-en-betaaldatums)). If one is still missing, file it now: the late-filing and late-payment penalties above apply, and belastingrente runs from 1 January 2026.
- Errors in 2025 returns above €1,000 need a Suppletie. It is interest-free only if sent within 3 months after 2025, that is before 1 April 2026. After that, belastingrente runs from 1 January 2026 until 14 days after the date of the additional assessment, so for a 2025 error only the 2026 rate of 5% applies. The 2025 rate of 6.5% applied to interest days in 2025, for example on 2024 VAT ([tax interest on VAT](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/standaard_functies/prive/contact/rechten_en_plichten_bij_de_belastingdienst/belastingrente/belastingrente_betalen_bij_loonbelasting_btw_en_overdrachtsbelasting); [tax interest rates](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/standaard_functies/prive/contact/rechten_en_plichten_bij_de_belastingdienst/belastingrente/overzicht_percentages_belastingrente)). Corrections are possible up to 5 years after the year, so 2025 can be corrected until the end of 2030 (the Belastingdienst's example: 2024 until the end of 2029).
- Accommodation supplied in 2025 was still at 9%; stays from 1 January 2026 are at 21%.

### How to pay ([paying or receiving VAT](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/btw_aangifte_doen_en_betalen/btw_betalen))

- No assessment is issued; the business pays the amount itself. Pay to IBAN NL04 RABO 0200 1122 44 in the name of "Belastingdienst" (BIC RABONL2U), always with the payment reference (betalingskenmerk). The Belastingdienst moved from ING to Rabobank on 1 May 2026, so update any old payment templates.
- iDEAL or Wero can be used from the return in Mijn Belastingdienst Zakelijk, within the payment term and for amounts up to €50,000.
- **Refunds**: a letter within 8 weeks of receipt, and the money within 1 week of that letter. An unpaid refund from an earlier period can be offset against a current payment, on request by letter.
- **Tax interest (belastingrente)**: charged on late payment and on additional assessments, from 1 January after the tax year. None is charged if the client voluntarily corrects within 3 months after the year, or pays late but within 3 months after the year ([tax interest on VAT](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/standaard_functies/prive/contact/rechten_en_plichten_bij_de_belastingdienst/belastingrente/belastingrente_betalen_bij_loonbelasting_btw_en_overdrachtsbelasting)).
- **Objection**: within 6 weeks of the date of an additional assessment or refund decision, or within 6 weeks of paying on the return ([notes 2026](https://download.belastingdienst.nl/belastingdienst/docs/toelichting_bij_btw_aangifte_ob0731t62fd.pdf)).

### Corrections (suppletie) ([correcting a return](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/btw_aangifte_doen_en_betalen/aangifte_corrigeren))

- €1,000 or less: put it in the next return, in the box where it normally belongs.
- More than €1,000: a Suppletie form in Mijn Belastingdienst Zakelijk, as soon as possible and at the latest within 8 weeks of finding the error. It can cover one period or a whole year. Corrections are possible up to 5 years after the year concerned.
- If VAT was overpaid, a refund decision usually follows within 8 weeks. If VAT was underpaid, wait for the additional assessment and pay that.
- To change a Suppletie already sent, normally wait for the refund decision or additional assessment and object to that decision within 6 weeks. **Exception:** if the submitted correction produces neither VAT payable nor a refund, no decision is issued. To amend that nil-result correction, fill in and submit the correction form again.

### ICP listing deadlines (Dutch-established businesses) ([ICP notes 2026](https://download.belastingdienst.nl/belastingdienst/docs/toelichting-digitale-opgaaf-intracomm-pres-ob1291t62fd.pdf))

The listing must be received within 1 month after the chosen period: quarterly by 30 April, 31 July, 31 October and 31 January of the next year; monthly by the end of the next month. Annual ICP needs permission. A late or wrong listing can bring a penalty and loss of the 0% rate.

## Completion checklist

- [ ] Business established in the Netherlands, not in the KOR, not in a fiscal unity; period and deadline taken from the aangiftebrief.
- [ ] A return is filed even if it is nil.
- [ ] Sales split into 1a (21%), 1b (9%), 1e, 3a, 3b and 3c; exempt sales left out; OSS sales left out.
- [ ] Accommodation supplied from 1 January 2026 charged at 21%; separately sold extras classified individually (qualifying breakfast/pool admission at 9%, not every extra).
- [ ] Reverse-charge purchases in 2a, 4a or 4b, with only the eligible deductible amount in 5b.
- [ ] Input VAT only from compliant invoices; no horeca food and drink; BUA €227 limit checked; exempt share taken out.
- [ ] Last return of the year: ordinary 1d private use (car at actual use, or 2.7% or 1.5% within the cap), applicable BUA and partial-exemption corrections. Check investment first-use/year-end true-up separately; later-year revision uses the relative 10% threshold. On cessation, report retained goods in the transfer period.
- [ ] Earlier errors: €1,000 or less in this return; above that a Suppletie within 8 weeks.
- [ ] Ordinary covered box 3b transactions reconciled to ICP; customer VAT ids checked; ICP filed within 1 month. Special new-means-of-transport reporting referred.
- [ ] Amounts in whole euros; total checked; paid with the right payment reference to the Rabobank account, in time to be credited by the deadline.
- [ ] KOR: turnover tested against €20,000 for this year and last year; EU-KOR against €100,000.
- [ ] Anything in "When to refuse or refer" flagged for a Dutch belastingadviseur.

This Guide is not tax advice. Check the linked Belastingdienst pages for the period you are filing.

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
