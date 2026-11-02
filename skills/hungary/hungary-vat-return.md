---
name: hungary-vat-return
description: Use this skill whenever asked to prepare, review, or classify transactions for a Hungary VAT return (form 2565 / AFA bevallas) for any client. Trigger on phrases like "prepare VAT return", "do the AFA", "fill in 2565", "Hungarian VAT", or any request involving Hungary VAT filing. This skill covers Hungary only and standard AFA registration. MUST be loaded alongside BOTH vat-workflow-base v0.1 or later AND eu-vat-directive v0.1 or later. ALWAYS read this skill before touching any Hungarian VAT work.
version: 2.0
jurisdiction: HU
tax_year: 2026
last_updated: 2026-10-16
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Hungary VAT return (ÁFA, form 2665): classifying a period and filling in the return

This skill prepares and reviews a periodic Hungarian VAT (általános forgalmi adó, ÁFA) return on form 2665 for a business registered under the general rules. Figures are for tax year 2026. Every rate and threshold sits in a table that links the NAV page it comes from. Use it with the `vat-workflow-base` skill (workflow) and the `eu-vat-directive` skill (EU rules). Online invoice reporting in depth is in `hungary-einvoice`.

## The method, step by step

1. **Check that the client files regular returns at all.** A business that chose the subjective exemption (alanyi adómentesség) does not charge VAT and files only occasional returns. For 2026 it may choose the exemption only if its domestic supplies, in forints and cumulated for the year, did not exceed the limit in the exemption table below in 2025 actually, AND are neither reasonably expected to exceed it nor actually exceed it in 2026. Exceeding the limit that applied in 2025 does not bar the choice ("akkor is, ha 2025. évben átlépte a 18 millió forintos értékhatárt"). The choice for 2026 had to be notified to NAV by the date in that table, unless the business was already exempt on 31 December 2025 and stays eligible. Source: NAV news item of 11 December 2025, https://nav.gov.hu/ado/afa/Emelkedik_az_alanyi_adomentesseg_ertekhatara and booklet 14, https://nav.gov.hu/pfile/file?path=/ugyfeliranytu/nezzen-utana/inf_fuz/2026/14.-Hasznos-tudnivalok-kezdo-afaalanyoknak-2025.-02.-03
2. **Set the 2026 filing frequency from 2024 data, not 2025 data.** The frequency is set by the data of the second year before the tax year (booklet 24, https://nav.gov.hu/pfile/file?path=/ugyfeliranytu/nezzen-utana/inf_fuz/2026/24.-Bevallasi-adofizetesi-informaciok-2026.01.26). Apply the tests in this order, using the amounts in the booklet 14 table below:
   - **Monthly** if the VAT to be accounted for in 2024 (output VAT less deductible input VAT), annualised, was positive AND reached the monthly threshold. Also monthly, whatever the amount: a business formed without a legal predecessor, in its year of registration and the following year; and a VAT group.
   - **Annual** only if ALL three hold: the 2024 VAT to be accounted for, annualised, was below the annual threshold whether positive or negative; AND net supplies, annualised, do not exceed the annual turnover cap; AND the business has no EU (community) VAT number.
   - **Quarterly** for everyone else. A business that passes the first two annual tests but holds an EU VAT number files quarterly.
   - **Mid-year changes.** A quarterly filer moves to monthly once its VAT to be accounted for since 1 January, cumulated with its sign and annualised, is positive and reaches the monthly threshold. An annual filer moves to monthly once the same difference since 1 January, cumulated with its sign, is positive and reaches the monthly threshold. An annual filer moves to quarterly once its VAT to be accounted for since 1 January reaches the annual threshold: the 2665 form guide says "az év elejétől – előjelhelyesen – összesített fizetendő és levonható előzetesen felszámított adó különbözete a 250 ezer forintot elérte", and booklet 24 prints the same test as "a +/- 250 ezer forintot elérte" (read as plus or minus). It also moves to quarterly if its net supplies exceed the annual turnover cap, or if it gets an EU VAT number. Source: the 2665 form guide and booklet 24 (tables below).
3. **Collect the data.** Bank statement for the period, sales and purchase invoices, the client's tax number (adószám), and last period's return for any credit brought forward (row 86 of the last return becomes row 82 of this one). Where the client files through eÁfa, start from NAV's draft return, which the client approves or corrects (booklet 14).
4. **Classify each transaction** with Sections 3, 5 and 6 and put it on its form 2665 row from the row table in Section 1 (2665 form guide, https://nav.gov.hu/pfile/file?path=%2Fnyomtatvanyok%2Fletoltesek%2Fnyomtatvanykitolto_programok%2Fnyomtatvanykitolto_programok_nav%2F2665%2F2665-kitoltesi-utmutato).
5. **Self-assess reverse-charge purchases.** Services from a taxable person in another EU state that are taxable in Hungary under the general place-of-supply rule (Áfa tv. § 37(1)) go on row 18, other EU services taxable in Hungary on row 19, services from a non-EU taxable person on row 27, taxable intra-EU acquisitions of goods on rows 12 to 14 by rate, and domestic reverse-charge purchases (Áfa tv. § 142) on row 29. The deductible part goes on row 67 (services), row 69 (EU goods) and, for domestic reverse charge, on rows 64 to 66 with the reverse-charge sub-field filled in. Source: the 2665 form guide.
6. **Claim input VAT** on domestic purchases on rows 64 (5%), 65 (18%) and 66 (27%), and row 111 for the 0% base. A business with both taxable and exempt supplies that cannot attribute input VAT item by item apportions it on row 68. Do not claim input VAT that a specific prohibition in the VAT Act blocks (Áfa tv. §§ 124 and 125, cited in booklet 14); see Section 5.10.
7. **Fill the M sheets (2665M-02) unless the client files through eÁfa.** The buyer lists every received domestic invoice under normal (not reverse-charge) taxation on which it deducts VAT, with no value threshold ("értékhatártól függetlenül"). eÁfa filers are exempt from this report. The M sheets are filled in forints; the main sheets in thousand forints (2665 form guide; booklet 14).
8. **Compute the balance.** Row 36 totals output VAT (rows 01 to 35 and 110). Row 76 totals deductible VAT (rows 63 to 75 and 111). Row 82 carries in the credit from the previous period. Row 83 is row 36 less row 76 less row 82. A positive row 83 goes, without sign, on row 84 (payable). A negative row 83 goes on row 85 if the client claims a refund it is entitled to, or on row 86 to carry forward to row 82 of the next return. Round each amount to the nearest thousand forints: 499 forints and below round down, 500 forints and above round up. Source: the 2665 form guide.
9. **Refund or carry forward.** NAV pays a refund only if the negative balance reaches the minimum for the client's frequency in the booklet 14 table below. Below that, the credit is carried forward. The general payment deadline for a refund is in the 2665 form guide table. Other deadlines apply to some taxpayers and cases: refer them (see "When to refuse or refer").
10. **File and pay by the deadline** in the booklet 14 table: the return and the payment fall due on the same day, and a refund can be claimed from that day. If a payment deadline falls on a non-working day, it moves to the next working day (2665 form guide). A return is due even when the balance is zero or negative (booklet 14).
11. **File the EU sales list separately** on form 26A60 for intra-EU supplies of goods and services, by the 20th of the month after the month or quarter. Approving an eÁfa draft does not replace it (booklet 14; booklet 24).
12. **Cross-check sales against online invoice data.** The duty covers every invoice the business issues to which the VAT Act applies ("mindazon számlát érinti, melyre az Áfa tv. szabályai vonatkoznak"). Invoices issued with invoicing software are reported to NAV immediately, machine to machine; paper invoices within the deadlines in the booklet 14 table (booklet 14). See `hungary-einvoice`.

## Ask the client first

- What were your domestic sales in 2025, and what do you expect for 2026? (Decides whether the subjective exemption was available for 2026.)
- When did you register for VAT, did you take over a predecessor's business, and what did your 2024 returns show? Do you hold an EU (community) VAT number? (Decides monthly, quarterly or annual filing.)
- Do you file through eÁfa (approving NAV's draft) or on the form through ÁNYK? (Decides whether the M sheets are needed.)
- Do you make any VAT-exempt supplies, such as financial services, insurance or exempt letting? (Decides apportionment on row 68.)
- Did you buy or run passenger cars, buy restaurant or entertainment services, or use business purchases privately? (Decides whether input VAT is blocked.)
- Do you buy from or sell to businesses or consumers in other EU states or outside the EU, and have you chosen cash accounting (pénzforgalmi elszámolás)? (Decides reverse-charge rows, the EU sales list, OSS and the timing of deduction.)

## When to refuse or refer

- **Subjective exemption (alanyi adómentes) clients.** Exempt businesses do not charge VAT and cannot deduct input VAT; their occasional filing is not covered here. Refer.
- **KATA taxpayers.** Whether such a client is a VAT payer or exempt must be settled first. Refer (see `hu-income-tax`).
- **Partial exemption (arányosítás) beyond a simple row 68 split, VAT groups (csoportos adóalanyiság), margin schemes, travel agents, agricultural special status and compensation surcharge (rows 72 and 73).** Out of scope. Refer to an adótanácsadó.
- **Refund timing other than the general deadline.** The 2665 form guide sets shorter deadlines for reliable taxpayers, a special rule tied to paid supplier invoices, and separate deadlines for a refund claimed in the return that closes a liquidation or winding-up. Do not quote a day count for these: refer.
- **Capital goods adjustment (Áfa tv. §§ 135 and 136, row 35)** and self-built assets (rows 10 and 74). Refer.
- **Import VAT self-assessment under a NAV licence (rows 24 to 26, 70 and 71)**, customs warehouses, and distance sales to consumers in other EU states above the EU threshold in the booklet 29 table (OSS). Refer.
- **Self-revision (önellenőrzés) of an earlier return** and the self-revision surcharge. Refer.

## Section 1: Quick reference

Read this whole section before classifying anything. The workflow runbook is in `vat-workflow-base` Section 1.

**Quick reference field table**

| Field | Value |
| --- | --- |
| Country | Hungary (Magyarország) |
| Standard rate | 27% |
| Reduced rates | 18% and 5% (see the booklet 14 table for what each covers) |
| 0% rate | 0% for daily newspapers (row 110). Exports and intra-EU supplies of goods are exempt with the right to deduct, on rows 01 and 02, not "0% rate" sales |
| Return form | Form 2665 for 2026 periods (the year digits followed by 65). "2665A" names the main sheets inside form 2665, not a separate form |
| Filing channels | eÁfa (web or machine to machine), or the form through ÁNYK |
| Authority | Nemzeti Adó- és Vámhivatal (NAV) |
| Currency | HUF; main sheets in thousand forints, M sheets in forints |
| Filing frequencies | Monthly, quarterly or annual, set for 2026 from 2024 data (method step 2) |
| Deadline | 20th of the month after the month or quarter; 25 February for annual filers |
| Online invoice reporting | Every invoice issued to which the VAT Act applies (method step 12) |
| Companion Skill (workflow) | `vat-workflow-base`, must be loaded |
| Companion Skill (EU directive) | `eu-vat-directive`, must be loaded |

**Rates, frequency, deadlines, refunds and invoice reporting (NAV booklet 14, published 22 January 2026)**

| Item | Value | Note (verbatim) |
| --- | --- | --- |
| Source | all figures below | https://nav.gov.hu/pfile/file?path=/ugyfeliranytu/nezzen-utana/inf_fuz/2026/14.-Hasznos-tudnivalok-kezdo-afaalanyoknak-2025.-02.-03 |
| Standard rate (Áfa tv. § 82(1)) | 27% | "általános adómértéke az adó alapjának 27 százaléka" |
| Reduced rate: certain foodstuffs listed by tariff number in the annex; the booklet does not print the full list | 18% | "A 18 százalékos adómértékű termékeket – ilyenek egyes élelmiszerek" |
| Reduced rate: admission to occasional open-air events | 18% | "a szintén 18 százalékos adómértékű, az alkalmi szabadtéri rendezvényre" |
| Reduced rate, goods: for example books, sheet music, periodicals, certain medical products and aids, certain pork, beef, sheep, goat, poultry, egg and milk products, fish for human consumption | 5% | "5 százalékos adómérték alá tartozik például a könyv, a kotta, a folyóirat" |
| Reduced rate, services: for example district heating, some performing-arts services, internet access, restaurant food and on-the-spot non-alcoholic drinks, commercial accommodation | 5% | "Néhány szolgáltatás is az 5 százalékos adómérték alá tartozik, például a távhőszolgáltatás" |
| Daily newspapers (published at least four times a week) | 0% | "A 0 százalékos kulcs alá tartozik a napilap (hetente legalább négyszer" |
| Cash accounting: available only if supplies net of VAT, annualised, did not exceed this in the previous year actually AND are neither expected to nor do exceed it in the current year | HUF 125,000,000 | "nem haladja meg a 125.000.000 forintnak megfelelő pénzösszeget" |
| Monthly filing: VAT to be accounted for in the second year before, annualised, positive AND at least this | HUF 1 million | "összege pozitív előjelű, és az 1 millió forintot elérte" |
| Annual filing, test 1: VAT to be accounted for in the second year before, annualised, below this whatever its sign | HUF 250 thousand | "előjelétől függetlenül nem érte el a 250 ezer forintot" |
| Annual filing, test 2: net supplies, annualised, not above this | HUF 50 million | "éves szinten összesített összege nem haladja meg az 50 millió forintot" |
| Monthly return and payment due | 20th of the following month | "a tárgyhónapot követő hónap 20-ig" |
| Quarterly return and payment due | 20th of the month after the quarter | "a negyedéves adóbevallásra kötelezett adóalanynak a negyedévet követő hónap 20-ig" |
| Annual return and payment due | 25 February of the following year | "a tárgyévet követő év február 25-ig" |
| Refund minimum, monthly filer (negative balance reaches or exceeds) | HUF 1 million | "a havi bevallásra kötelezett adóalanynál az 1 millió forintot" |
| Refund minimum, quarterly filer | HUF 250 thousand | "negyedéves bevallásra kötelezett adóalanynál a 250 ezer forintot" |
| Refund minimum, annual filer | HUF 50 thousand | "éves bevallásra kötelezett adóalanynál az 50 ezer forintot" |
| Paper invoice: report on NAV's online interface within 4 days | 4 days | "4 napon belül, vagy ha a számla adótartalma eléri vagy meghaladja" |
| Paper invoice whose VAT content reaches or exceeds this: report within 1 day | HUF 500,000 | "adótartalma eléri vagy meghaladja az 500.000 forintot, akkor 1 napon belül" |

**Subjective exemption (NAV news item, 11 December 2025)**

| Item | Value | Note (verbatim) |
| --- | --- | --- |
| Source | all figures below | https://nav.gov.hu/ado/afa/Emelkedik_az_alanyi_adomentesseg_ertekhatara |
| Limit for choosing the exemption for 2026 (raised from the 2025 limit; later years carry higher limits already legislated) | HUF 20 million | "2026-tól 18 millió forintról 20 millió forintra" |
| Deadline to notify NAV of the choice for 2026 | 31 December 2025 | "2025. december 31-éig kell bejelenteni a Nemzeti Adó- és Vámhivatalhoz" |

**Frequency reference year and EU sales list (NAV booklet 24, published 26 January 2026)**

| Item | Value | Note (verbatim) |
| --- | --- | --- |
| Source | all figures below | https://nav.gov.hu/pfile/file?path=/ugyfeliranytu/nezzen-utana/inf_fuz/2026/24.-Bevallasi-adofizetesi-informaciok-2026.01.26 |
| Year whose data set the 2026 monthly test | 2024 | "akinek/amelynek a 2024. évre vonatkozóan" |
| EU sales list moves from quarterly to monthly when intra-EU supplies of goods (and acquisitions, triangulation) in the quarter, net of VAT, exceed this | EUR 50,000 | "meghaladja az 50 000 eurónak megfelelő pénzösszeget" |

**EU transactions (NAV booklet 29, published 26 January 2026)**

| Item | Value | Note (verbatim) |
| --- | --- | --- |
| Source | all figures below | https://nav.gov.hu/pfile/file?path=/ugyfeliranytu/nezzen-utana/inf_fuz/2026/29_Az_altalanos_szabalyok_szerint_adozo_afaalanyok_kozossegi_ugyletei_2026.01.26 |
| EU-wide threshold for distance sales of goods and telecom, broadcasting and electronic services to consumers in other EU states; above it VAT is due in the customer's state | EUR 10,000 | "túllépi a 10 000 euró küszöbértéket, vagyis a 3 100 000 forintot" |
| Invoice wording where the customer pays the VAT | "fordított adózás" | "a számlán a „fordított adózás” kifejezést kell szerepeltetni" |

**Form 2665 rows and refund deadline (2665 form guide)**

| Row | What goes there | Note (verbatim) |
| --- | --- | --- |
| Source | all figures below | https://nav.gov.hu/pfile/file?path=%2Fnyomtatvanyok%2Fletoltesek%2Fnyomtatvanykitolto_programok%2Fnyomtatvanykitolto_programok_nav%2F2665%2F2665-kitoltesi-utmutato |
| 01 | Exempt export of goods outside the EU | "a Közösség területén kívülre történő mentes termékértékesítés (export)" |
| 02 | Exempt intra-EU supply of goods | "mentes termékértékesítés adó nélkül számított ellenértékét" |
| 04 | Domestic sales where the buyer pays the VAT (reverse charge), net amount | "a fordított adózás szabályai szerint az adó fizetésére a termék beszerzője" |
| 110 | Domestic sales at 0% | "a 0%-os kulcs alá tartozó termékértékesítések ellenértékét" |
| 05 | Domestic sales at 5%, base and VAT | "az 5%-os kulcs alá tartozó termékértékesítések és szolgáltatásnyújtások" |
| 06 | Domestic sales at 18%, base and VAT | "a belföldi teljesítési helyű 18%-os adómértékű termékek" |
| 07 | Domestic sales at 27%, base and VAT | "A 27%-os kulcs alá tartozó értékesítés után" |
| 08 | Exempt supplies without the right to deduct (Áfa tv. §§ 85 to 87) | "a tevékenység közérdekű jellegére tekintettel mentes szolgáltatások" |
| 12 to 14 | Taxable intra-EU acquisitions of goods, on the row for the rate | "(az adómértéknek megfelelő sorban)" |
| 18 | Services from a taxable person in another EU state, taxable in Hungary under § 37(1) | "a szolgáltatás nyújtója olyan, a Közösség más tagállamában adószámmal rendelkező adóalany" |
| 19 | Other EU services taxable in Hungary, not on row 18 | "a 18. sorban nem szereplő egyéb, közösségi adóalanytól igénybevett szolgáltatás" |
| 27 | Services from a non-EU taxable person, base and VAT | "a harmadik országbeli adóalanytól igénybe vett szolgáltatás ellenértékét" |
| 29 | Domestic reverse-charge VAT the buyer pays; detail on rows 51 to 54 (real estate, waste, emission rights, services) | "a fordított adózás szabályai szerint – adófizetésre kötelezett vevőként" |
| 36 | Total output VAT: rows 01 to 35 and 110 | "a 01-35. és 110. sorokban található részösszegeket" |
| 64 | Deductible domestic input VAT at 5% | "terhelő 5%-os mértékű előzetesen felszámított adót" |
| 65 | Deductible domestic input VAT at 18% | "terhelő 18%-os mértékű előzetesen felszámított adót" |
| 66 | Deductible domestic input VAT at 27% | "terhelő 27%-os mértékű előzetesen felszámított adót" |
| 67 | Deductible VAT on services entered on rows 18, 19 and 27 | "(a 18., a 19. és a 27. sorban feltüntetett)" |
| 68 | Apportioned input VAT (mixed taxable and exempt activity) | "akkor az arányosítás szabályai" |
| 69 | Deductible VAT on intra-EU acquisitions from rows 12 to 16 and 112 | "fizetendőként a bevallás 12-16. és 112. soraiban feltüntetett" |
| 76 | Total deductible input VAT: rows 63 to 75 and 111 | "63-75. és 111. sorokban feltüntetett együttes" |
| 82 | Credit brought forward from the previous period | "az előző adómegállapítási időszakról áthozott" |
| 83 | Balance: row 36 less row 76 less row 82 | "az összes fizetendő adó (36. sor) összege csökkentve" |
| 84 | Payable (row 83 positive), without sign | "ha a tárgyidőszakban a 83. sor adata előjel nélküli" |
| 85 | Refund claimed (row 83 negative and a refund right exists) | "ha a tárgyidőszakban a 83. sor adata mínusz előjelű" |
| 86 | Credit carried forward to row 82 of the next return | "a következő bevallási időszakban csökkentő tételként a 82. sorban" |
| 92 | EU B2B services under the general place-of-supply rule (ties to form 26A60) | "„határon átnyúló, Közösségen belüli szolgáltatások” ellenértékét (ideértve az előleget is)" |
| 93 | EU B2B services whose place of supply is outside Hungary under a rule other than § 37(1); not on the EU sales list | "A 93. sorba kell beírni a „határon átnyúló, Közösségen belüli szolgáltatások” ellenértékét, amely esetben" |
| M-02 | Every received domestic invoice under normal taxation with deducted VAT, no value threshold | "értékhatártól függetlenül minden olyan befogadott, egyenes adózás alá tartozó számláról" |
| 64 to 68 | Filling the rate-by-rate columns for VAT actually deducted is optional | "adómértékenként (5 %, 18 %, 27 %, arányosítás) elkülönített rovatok kitöltése önkéntes" |
| Refund | General refund payment deadline | 75 days: "A visszaigényelt általános forgalmi adót 75 napon belül kell kiutalni" |

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown rate on a sale | 27% |
| Unknown VAT status of a purchase | Not deductible |
| Unknown counterparty country | Domestic Hungary |
| Unknown B2B vs B2C for EU customer | B2C, charge 27% |
| Unknown business-use proportion | No recovery |
| Unknown SaaS billing entity | Reverse charge from non-EU (row 27) |
| Unknown blocked-input status | Blocked |
| Unknown filing channel | Assume ÁNYK form, so the M sheets are needed |

**Red flags for the reviewer**

Flag large single transactions, any single conservative default with a large tax effect, a counterparty that dominates output or input, many conservative defaults in one period, and any refund claim. The thresholds are a review choice for the adopting accountant, not a legal rule.

## Section 2: Required inputs and refusal catalogue

### Required inputs

**Minimum viable**: bank statement for the period. Acceptable from: OTP Bank, K&H Bank, Erste Bank Hungary, MBH Bank (merged Magyar Bankholding), CIB Bank, UniCredit HU, Revolut Business, Wise Business.

**Recommended**: sales and purchase invoices, adószám (tax number), prior form 2665.

**Ideal**: complete register, online invoice data, eÁfa draft where used, prior period reconciliation.

### Hungary-specific refusal catalogue

- **R-HU-1: Alanyi mentes (subjective exemption).** Trigger: the client chose the exemption under the limit in the exemption table. Message: "Exempt small businesses do not charge VAT and cannot deduct input VAT. This skill does not cover their occasional filing."
- **R-HU-2: KATA subject.** Trigger: the client is a KATA taxpayer. Message: "Settle VAT status first. Specialist review required."
- **R-HU-3: Partial exemption.** Message: "Mixed supplies require arányosítás. Use an adótanácsadó."
- **R-HU-4: VAT group.** Message: "Group registration out of scope."
- **R-HU-5: Special schemes.** Message: "Margin scheme, travel agent and agricultural special status out of scope."
- **R-HU-6: Refund timing.** Trigger: client asks when a refund other than the general case will arrive. Message: "Special refund deadlines apply. Refer."

## Section 3: Supplier pattern library

### 3.1 Hungarian banks (exempt, exclude)

**Hungarian banks pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| OTP, OTP BANK | EXCLUDE | Financial service, exempt |
| K&H, K&H BANK | EXCLUDE | Same |
| ERSTE BANK HU, ERSTE | EXCLUDE | Same |
| MBH BANK, BUDAPEST BANK, TAKAREKBANK | EXCLUDE | Same (merged entity) |
| CIB BANK | EXCLUDE | Same |
| UNICREDIT HU | EXCLUDE | Same |
| REVOLUT, WISE, N26 (fee lines) | EXCLUDE | Check subscriptions |
| KAMAT, INTEREST | EXCLUDE | Interest |
| HITEL, KOLCSON, LOAN | EXCLUDE | Loan principal |

### 3.2 Hungarian government (exclude)

**Hungarian government pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| NAV, NEMZETI ADO | EXCLUDE | Tax payment |
| TB, TARSADALOMBIZTOSITAS | EXCLUDE | Social insurance |
| ONKORMANYZAT, MUNICIPALITY | EXCLUDE | Municipal fees |
| CEGJEGYZEK, COMPANY REGISTER | EXCLUDE | Registration |

### 3.3 Hungarian utilities

**Hungarian utilities pattern table**

| Pattern | Treatment | Row | Notes |
| --- | --- | --- | --- |
| MVM, ELMÜ-ÉMÁSZ, E.ON HU | Domestic 27% unless the invoice shows another rate | 66 | Electricity |
| FŐVÁROSI VÍZMŰVEK, VÍZMŰ | Rate as shown on the invoice | 64 to 66 | Water; do not assume the rate |
| FŐGÁZ, GÁZ | Domestic 27% unless the invoice shows another rate | 66 | Gas |
| FŐTÁV, TÁVHŐ | Domestic 5% | 64 | District heating (5% list in the booklet 14 table) |
| MAGYAR TELEKOM, T-MOBILE HU | Split by invoice line: internet access 5%, other telecom 27% | 64 / 66 | Internet access is on the 5% list |
| VODAFONE HU, YETTEL HU | Split by invoice line as above | 64 / 66 | Telecoms |
| DIGI HU | Split by invoice line as above | 64 / 66 | Telecoms and broadband |

### 3.4 Insurance (exempt, exclude)

**Insurance pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| ALLIANZ HUNGARIA | EXCLUDE | Exempt |
| GENERALI BIZTOSITO | EXCLUDE | Same |
| GROUPAMA BIZTOSITO | EXCLUDE | Same |
| BIZTOSITAS, INSURANCE | EXCLUDE | All exempt |

### 3.5 Post and logistics

**Post and logistics pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| MAGYAR POSTA | EXCLUDE for standard post; 27% for parcel | Check the invoice |
| GLS HU | Domestic 27%, row 66 | Courier |
| MPL (Magyar Posta Logisztika) | Domestic 27%, row 66 | Parcel |
| DHL INTERNATIONAL | EU reverse charge (rows 18 and 67) | Check the billing entity |

### 3.6 SaaS: EU suppliers (reverse charge, row 18, deduction row 67)

**SaaS EU suppliers pattern table**

| Pattern | Billing entity | Notes |
| --- | --- | --- |
| GOOGLE | Google Ireland Ltd (IE) | EU reverse charge |
| MICROSOFT | Microsoft Ireland (IE) | EU reverse charge |
| ADOBE | Adobe Ireland (IE) | EU reverse charge |
| META, FACEBOOK | Meta Ireland (IE) | EU reverse charge |
| SPOTIFY | Spotify AB (SE) | EU reverse charge |
| DROPBOX | Dropbox Ireland (IE) | EU reverse charge |
| SLACK | Slack Ireland (IE) | EU reverse charge |
| ATLASSIAN | Atlassian BV (NL) | EU reverse charge |
| ZOOM | Zoom Ireland (IE) | EU reverse charge |
| AWS EMEA SARL | LU entity | EU reverse charge |

### 3.7 SaaS: non-EU suppliers (reverse charge, row 27, deduction row 67)

**SaaS non-EU suppliers pattern table**

| Pattern | Billing entity | Notes |
| --- | --- | --- |
| NOTION | Notion Labs Inc (US) | Non-EU reverse charge |
| ANTHROPIC, CLAUDE | Anthropic PBC (US) | Non-EU reverse charge |
| OPENAI, CHATGPT | OpenAI Inc (US) | Non-EU reverse charge |
| GITHUB | GitHub Inc (US) | Check whether billed from IE |
| FIGMA | Figma Inc (US) | Non-EU reverse charge |
| CANVA | Canva Pty Ltd (AU) | Non-EU reverse charge |

### 3.8 Payment processors

**Payment processors pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| STRIPE (transaction fees) | EXCLUDE (exempt) | Financial service |
| PAYPAL (transaction fees) | EXCLUDE (exempt) | Same |

### 3.9 Professional services

**Professional services pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| KÖZJEGYZŐ, NOTARY | Domestic 27%, row 66 | Legal |
| KÖNYVELŐ, ACCOUNTANT | Domestic 27%, row 66 | Accounting |
| ÜGYVÉD, LAWYER | Domestic 27%, row 66 | Legal |

### 3.10 Payroll (exclude)

**Payroll pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| TB, JÁRULÉK | EXCLUDE | Social contributions |
| BÉR, FIZETÉS, SALARY | EXCLUDE | Wages |
| SZJA | EXCLUDE | Income tax |

### 3.11 Food retail and restaurants

**Food retail pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| TESCO HU, ALDI HU, LIDL HU, SPAR HU, PENNY | Default BLOCK | Personal provisioning |
| ÉTTEREM, RESTAURANT, VENDÉGLŐ | Default BLOCK | Restaurant food is sold at 5% (booklet 14 table), but input VAT on restaurant and entertainment purchases may fall under the VAT Act's specific deduction bans; the accountant decides |

### 3.12 Internal transfers and exclusions

**Internal transfers pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| SAJÁT ÁTUTALÁS, OWN TRANSFER | EXCLUDE | Internal |
| OSZTALÉK, DIVIDEND | EXCLUDE | Out of scope |
| HITELTÖRLESZTÉS, LOAN REPAYMENT | EXCLUDE | Loan principal |
| ATM, KÉSZPÉNZ | Ask | Default exclude |

## Section 4: Worked examples

Amounts are left out of these hypothetical bank lines; the treatment does not depend on them.

### Example 1: non-EU SaaS reverse charge (Notion)

**Input:** `03.04.2026 ; NOTION LABS INC ; debit`
**Treatment:** Service from a non-EU taxable person. Base and self-assessed VAT at 27% on row 27. The deductible amount on row 67, if the service is used for taxable supplies.

### Example 2: EU service reverse charge (Google Ads)

**Input:** `10.04.2026 ; GOOGLE IRELAND LIMITED ; debit`
**Treatment:** B2B service from a taxable person in another EU state, taxable in Hungary under § 37(1). Base and self-assessed VAT at 27% on row 18. Deduction on row 67.

### Example 3: restaurant

**Input:** `15.04.2026 ; BORKONYHA ÉTTEREM ; debit`
**Treatment:** Default block. Booklet 14 confirms that the VAT Act contains specific provisions prohibiting deduction (Áfa tv. §§ 124 and 125) and that some services and goods with deduction restrictions are defined by statistical classification. Do not claim until the accountant confirms the purchase is outside those bans.

### Example 4: EU B2B service sale

**Input:** `22.04.2026 ; STUDIO KREBS GMBH ; credit`
**Treatment:** Service to a German business, place of supply in Germany under the general rule. Report on row 91 and row 92, and on the EU sales list (form 26A60). No Hungarian VAT. Check the customer's VAT number.

### Example 5: equipment purchase

**Input:** `18.04.2026 ; MEDIAMARKT HU ; Laptop ; debit`
**Treatment:** Domestic purchase at 27%, input VAT on row 66 if used for taxable supplies. Ask whether it is a fixed asset (tárgyi eszköz); a later change of use can trigger the capital goods adjustment on row 35. Refer that adjustment.

### Example 6: motor vehicle fuel

**Input:** `28.04.2026 ; MOL NYRT ; Fuel ; debit`
**Treatment:** Default: no recovery. The VAT Act carries a deduction ban on buying a passenger car, which a purchase for resale lifts (booklet 14: "a személygépkocsi beszerzésére vonatkozó levonási tilalmat a továbbértékesítési célú beszerzés feloldotta"). Deduction on fuel and running costs of a passenger car is for the accountant to decide.

## Section 5: Tier 1 classification rules (compressed)

### 5.1 Standard 27% (Áfa tv. § 82(1))

- **Standard rate rule.** Default for every supply not on a reduced-rate annex and not exempt. Sales: row 07. Input: row 66.

### 5.2 Reduced 18%

- **18% rule.** Certain foodstuffs listed by tariff number in the VAT Act annex, and admission to occasional open-air events. The booklet does not print the full food list: check the annex for each product. Sales: row 06. Input: row 65.

### 5.3 Reduced 5%

- **5% rule.** The goods and services listed in the booklet 14 table, including commercial accommodation and restaurant food. Sales: row 05. Input: row 64.

### 5.4 0% rate, exports and intra-EU supplies

- **0% rule.** Daily newspapers only: row 110 (sales), row 111 (purchases).
- **Exports.** Exempt with the right to deduct: row 01.
- **Intra-EU supplies of goods.** Exempt with the right to deduct: row 02, and on the EU sales list.
- **Intra-EU B2B services** under the general rule: row 91 and row 92, and on the EU sales list.
- **Other EU B2B services supplied abroad** under a place-of-supply rule other than § 37(1): row 93, not on the EU sales list.

### 5.5 Exempt without the right to deduct (Áfa tv. §§ 85 to 87)

- **Exempt rule.** Activities exempt because of their public-interest or other special nature (Áfa tv. §§ 85 to 87). Booklet 14 gives as examples the universal postal service, human healthcare and a broad range of education, some only when supplied by a public service provider or a provider licensed for the profession; certain insurance, financial and gambling services; and certain sales and lettings of real estate, for which the client may opt to tax instead. Sales: row 08. Input VAT on related purchases is not deductible.

### 5.6 Reverse charge, EU

- **EU reverse charge rule.** Goods: rows 12 to 14 by rate, deduction row 69. Services under § 37(1): row 18; other EU services: row 19; deduction row 67.

### 5.7 Reverse charge, non-EU

- **Non-EU reverse charge rule.** Services: row 27, deduction row 67.

### 5.8 Domestic reverse charge (Áfa tv. § 142)

- **Domestic reverse charge rule.** Seller: net amount on row 04, invoice carries "fordított adózás". Buyer: VAT on row 29, detail on rows 51 to 54, deduction on rows 64 to 66 with the reverse-charge sub-field.

### 5.9 Online invoice reporting

- **Online invoice rule.** Every invoice issued to which the VAT Act applies. Invoicing software reports immediately, machine to machine. Paper invoices: see the booklet 14 table.

### 5.10 Blocked input

- **Blocked input rules.** Personal use: blocked. Passenger car purchase: the VAT Act bans deduction; booklet 14 names purchase for resale as lifting the ban, and any other exception is for the accountant. Restaurant, entertainment, fuel and other passenger car costs: default block, the accountant decides under Áfa tv. §§ 124 and 125.

## Section 6: Tier 2 catalogue (compressed)

### 6.1 Vehicle costs

- **Vehicle costs.** Default: block. Question: "Is it a passenger car, and was it bought for resale?"

### 6.2 Entertainment and restaurants

- **Entertainment.** Default: block. Question: "What was it, and who attended?"

### 6.3 SaaS entity

- **SaaS entity.** Default: non-EU reverse charge (row 27).

### 6.4 Owner transfers

- **Owner transfers.** Default: exclude.

### 6.5 Fixed assets

- **Fixed assets.** Default: add to the fixed asset register and flag any change of use for the capital goods adjustment (row 35).

### 6.6 Mixed-use telecom

- **Mixed-use telecom.** Default: no recovery until the business share is known.

### 6.7 Cash withdrawals

- **Cash withdrawals.** Default: exclude.

### 6.8 KATA status

- **KATA status.** Default: flag the reviewer.

## Section 7: Excel working paper template

Per `vat-workflow-base` Section 3. Column H accepts form 2665 row codes (for example 07, 18, 27, 66, 67). Bottom line: row 84 (payable), row 85 (refund claimed) or row 86 (carried forward). Main-sheet amounts in thousand forints; M-sheet amounts in forints.

## Section 8: Hungary bank statement reading guide

**CSV conventions.** OTP and K&H use semicolons and YYYY.MM.DD (Hungarian date format).

**Hungarian language.** bérleti díj (rent), bér / fizetés (salary), kamat (interest), átutalás (transfer), készpénz (cash).

**Currency.** HUF. Convert foreign-currency amounts under the VAT Act's exchange-rate rules; ask which rate the client applies.

**IBAN prefix.** HU = Hungary.

## Section 9: Onboarding fallback

### 9.1 Entity type

- **Entity type inference.** Kft. = company; egyéni vállalkozó = sole trader.

### 9.2 VAT status

- **VAT status fallback.** "Standard VAT payer or alanyi mentes?"

### 9.3 Adószám

- **Adószám fallback.** "Tax number? (11 digits)"

### 9.4 Filing frequency

- **Filing frequency fallback.** "Monthly, quarterly or annual for 2026?" Confirm against method step 2.

### 9.5 Filing channel

- **Filing channel fallback.** "Do you approve NAV's eÁfa draft or file the form through ÁNYK?"

### 9.6 Exempt supplies

- **Exempt supplies fallback.** "Any exempt supplies?"

### 9.7 Credit brought forward

- **Credit brought forward fallback.** "Credit carried forward on row 86 of the last return?"

## Section 10: Reference material

Statute: Act CXXVII of 2007 on VAT (Áfa tv.), cited by section. Every figure in this skill is proven on a NAV page.

### Change log

- **v3.0 (October 2026):** Rewritten for 2026 periods by the OpenAccountants team: form 2665 and its real row numbers, 2026 frequency rules, refund minimums, M sheets, subjective exemption limit.
- **v2.0 (April 2026):** Full rewrite. Hungarian banks (OTP, K&H, Erste HU).
- **v1.0 (April 2026):** Initial version.

## Sources

- NAV booklet 14, Hasznos tudnivalók kezdő áfaalanyoknak (published 22 January 2026): https://nav.gov.hu/pfile/file?path=/ugyfeliranytu/nezzen-utana/inf_fuz/2026/14.-Hasznos-tudnivalok-kezdo-afaalanyoknak-2025.-02.-03
- NAV booklet 24, Bevallási, adófizetési információk (published 26 January 2026): https://nav.gov.hu/pfile/file?path=/ugyfeliranytu/nezzen-utana/inf_fuz/2026/24.-Bevallasi-adofizetesi-informaciok-2026.01.26
- NAV booklet 29, EU transactions of VAT payers under the general rules (published 26 January 2026): https://nav.gov.hu/pfile/file?path=/ugyfeliranytu/nezzen-utana/inf_fuz/2026/29_Az_altalanos_szabalyok_szerint_adozo_afaalanyok_kozossegi_ugyletei_2026.01.26
- NAV, Emelkedik az alanyi adómentesség értékhatára (11 December 2025): https://nav.gov.hu/ado/afa/Emelkedik_az_alanyi_adomentesseg_ertekhatara
- NAV, form 2665 completion guide: https://nav.gov.hu/pfile/file?path=%2Fnyomtatvanyok%2Fletoltesek%2Fnyomtatvanykitolto_programok%2Fnyomtatvanykitolto_programok_nav%2F2665%2F2665-kitoltesi-utmutato

This skill is incomplete without both companion skills: `vat-workflow-base` and `eu-vat-directive`.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

The most up-to-date version of this skill is maintained by OpenAccountants.

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
