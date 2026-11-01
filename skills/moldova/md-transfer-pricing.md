---
name: md-transfer-pricing
description: Use this Guide for Moldova transfer-pricing affiliation, local and cross-border scope, the aggregate information threshold, statutory exclusions, method selection, comparability intervals and adjustments for 2026. It explains requested master and local files, electronic information filing, advance pricing agreements, corresponding adjustments and period-specific sanctions. Trigger on Moldova TP, affiliated transactions, the MDL 20 million threshold, transfer-pricing information, an SFS file request or an APA. Reconcile actual transaction values and evidence rather than using net balances or an expired automatic file tier. Current source and implementation gaps remain explicit; this is a draft with a bounded source-review record linked under Sources.
version: "0.8"
jurisdiction: MD
category: transfer-pricing
tax_year: 2026
last_updated: 2026-10-31
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Moldova transfer pricing v0.8

2026 draft, primary law read 30 October 2026; the current information annex and APA application model read 31 October 2026. The 24 October draft and its independent correction evidence are preserved; that review does not attest to this expanded country pack. This Guide provides the domestic TP computation/documentation method. Actual comparables, legal facts and any treaty relief must be evidenced before use.

## Who this applies to

Start with the current Fiscal Code TitleV chapter 11², arts. 226¹⁷–226³⁰, and Ministry of Finance Order 9/2024 as amended, including Order 8/2026. The rules apply to Moldovan-registered business legal/natural persons and foreign legal persons with Moldovan branches/permanent establishments. Art. 226¹⁹(9) excludes Moldovan-citizen individuals not carrying on business from that article's filing rule. The arm's-length obligation is separate from the information/file threshold. [Code arts. 226¹⁷–226¹⁹](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro), [Order 9 annex 1 points 1–2](https://www.legis.md/cautare/getResults?doc_id=152738&lang=ro).

Under 226¹⁷(1)(1), affiliation includes spouses or relatives up to the second degree; an individual/legal-person relationship with at least 25% direct/indirect voting participation including affiliated holdings or effective control; a legal-person/legal-person relationship on the same basis; and common third-person ownership/control of both. Effective control includes the specified majority board/executive/auditor appointment/removal powers and contractual/constitutional/agreed control. Indirect participation can pass through several people/entities; the legal person and its PE are affiliated. Do not stop the test at a 25% share register where another control limb applies. [Code 226¹⁷](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro).

A transaction includes sales, purchases, giving/receiving services, assignments, leases, credit, loans and transfers of interests or rights in tangible/intangible property. A local transaction under 226¹⁷(1)(9) concerns residents where either/both have the specified free-zone/IT-park status or different business-income tax rates/bases; a cross-border transaction under(10) is between a resident and a nonresident outside Moldova. Classify the parties, regimes and transaction before applying 226¹⁸(2). Do not treat every same-rate domestic intercompany movement as automatically satisfying the statutory local-transaction definition, or omit eligible domestic transactions solely because neither party is foreign. [Code 226¹⁷–226¹⁸](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro).

The current 226¹⁹ filing structure applies from fiscal period 2025 under Law 187/2025 art. XXVI(1)(b). It replaced the two-tier 20m/50m system: for 2025/2026 periods there is one information threshold and a request-based file. For 2024, Law 187 art. XXVI(3) creates a separate request/120-day file transition for its specified former category and disapplies the identified non-submission sanction for the former deadline; do not apply an old automatic filing calendar or treat that transition as the 2026 rule. [Law 187 art. II point 19 and art. XXVI](https://www.legis.md/cautare/getResults?doc_id=149593&lang=ro).

## Rates, bands and thresholds

| Item | Current rule | Official source |
|---|---|---|
| Voting-participation affiliation limb |At least 25%, direct/indirect including affiliated holdings; effective-control/family limbs are separate|[Code 226¹⁷(1)(1)](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro)|
| Information threshold, periods from 2025 |Aggregate eligible affiliated transactions excluding VAT **at least MDL 20m**, across all affiliates; apply the exclusions below|[Code 226¹⁹(1),(4),(7)](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro)|
| Annual information |25th of the sixth month after the actual fiscal period ends|[Code 226¹⁹(2)](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro)|
| File |Prepare/submit on SFS request within 120-days of request, not earlier than the information deadline; no automatic MDL 50m tier|[Code 226¹⁹(3)](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro)|
| Corrected file |Up to 30-days from communication of the SFS adjustment/estimation decision|[Code 226¹⁹(6)](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro)|
| Comparability interval |Lower/upper quartiles; if at most two reliable comparable values, use min/max and their arithmetic mean for the median|[Order 9 annex 1 points 3,22–25](https://www.legis.md/cautare/getResults?doc_id=152738&lang=ro)|
| Audit adjustment/estimation |Median of the justified comparability interval|[Order 9 annex 1 point 47](https://www.legis.md/cautare/getResults?doc_id=152738&lang=ro)|
| Unilateral APA fee |MDL 30,000 per transaction **type**|[Code 226²⁸(1)(a)](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro)|
| Bilateral/multilateral APA fee |MDL 50,000 per transaction **type**|[Code 226²⁸(1)(b)](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro)|
| Ongoing/future APA |No more than five fiscal periods including the application period|[Code 226²⁶(1)](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro)|
| Completed-transaction APA |Last two fiscal periods, excluding the application period|[Code 226²⁶(2)](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro)|
| APA extension/revision request |At least 60-days before expiry under the statutory request rule; separately track the 30-day changed-assumptions duty|[Code 226²⁵(8)](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro), [Order 9 annex 3 point 47](https://www.legis.md/cautare/getResults?doc_id=152738&lang=ro)|
| Cross-border corresponding-adjustment application |SFS examines within 30 working days; adjustment is conditional, not automatic|[Code 226²²(2)–(3)](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro)|
| Ordinary corporate rate used in example 2 |12% of the additional taxable income for the assumed ordinary company; not a universal TP surcharge|[Code 15(b)](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro)|

The 20m filing threshold is not a safe-harbour price, deductible-expense limit or separate TP tax rate. Regulated/judicially set price elements fall within the deemed arm's-length rule in 226¹⁸(3); retain the instrument and demonstrate that it governs the actual element. Income/expense adjustments operate through Titles II/X and **do not alter VAT** on supplies/purchases under 226¹⁸(4),(6). [Code](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro).

## The base

### Build the affiliate and threshold reconciliation

Identify ownership/control and fiscal periods; record each party's residence, PE and tax regime. Reconcile transaction values across all eligible affiliates **without VAT**, maintaining sales and purchases separately instead of netting bilateral balances. Tag legal exclusions individually. Art. 226¹⁹(4) excludes transactions covered by an actual APA from the threshold and its documentation, whereas a pending APA application does not exempt the information filing under Order 9 annex 3 point 4. [Code 226¹⁹](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro), [Order 9](https://www.legis.md/cautare/getResults?doc_id=152738&lang=ro).

Art. 226¹⁹(7) excludes received/paid advances, exchange differences and accounting revaluation differences of assets/liabilities arising from affiliated transactions, except actual currency-exchange transactions. For leases, credit and loans, the threshold includes **only interest calculated during the fiscal period** under art. 12(7), rather than the funding principal or all instalments. Preserve the bridge from accounting/contract data to eligible amounts; do not use the expired Order 9 point 52 as if it overrode current statutory exclusions. Foreign-currency conversion mechanics and unusual financing components require the confirmed rule stated below before using an assumed exchange rate. [Code 226¹⁹(7)](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro), [current Order 9 annex 1 point 52 repealed](https://www.legis.md/cautare/getResults?doc_id=152738&lang=ro).

Below 20m, the statutory information/request-file obligation under 226¹⁹(1) is not triggered solely by value; it does not prove arm's-length pricing or remove ordinary evidence duties. Order 9 annex 1 point 36 permits SFS to require structure/affiliation, markets, competitors, contracts, accounting and transaction-support records from persons without the file obligation; point 37 says missing documents do not stop the audit. The old point 30 MDL 1m verification exclusion is repealed in the current rules. [Code 226¹⁸–226²⁰](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro), [Order 9 annex 1 points 30–37](https://www.legis.md/cautare/getResults?doc_id=152738&lang=ro).

### Delineate and price the actual transaction

The taxpayer bears the burden of demonstrating arm's-length compliance. Compare legal, economic, commercial and financial conditions using characteristics, functions/assets/risks, contractual terms, economic circumstances and business strategy. Record risk control and financial capacity, not only a contract allocating the risk. The actual conduct/conditions prevail where inconsistent with the document. Examine markets, competition, substitutes, supply/demand, purchasing power, regulation and infrastructure; justify a different geographic market and reliable adjustments. [Code 226¹⁸(7)–(8),226²⁰(5)](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro), [Order 9 annex 1 points 4–13](https://www.legis.md/cautare/getResults?doc_id=152738&lang=ro).

Select the most appropriate method and document why the data and comparability support it. The domestic methods are comparable uncontrolled price (CUP), cost-plus, resale-price, transactional net margin (TNMM), profit-split, and another method recognised in the OECD TP Guidelines. Do not invent a universal statutory cost-plus markup, guarantee fee or interest margin. [Code 226²⁰(3)–(5)](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro).

| Method | Computation and evidence to retain | Official provision |
|---|---|---|
|CUP|Compare actual controlled unit price with sufficiently comparable independent prices, adjusting material differences reliably|Order 9 annex 1 point 16|
|Resale price|Independent resale price less the justified resale margin (resale costs and appropriate gross profit), adjusting relevant acquisition costs; keep consistent gross-margin accounting|Point 17|
|Cost-plus|Relevant production/service costs plus a justified gross-profit markup; retain cost-pool, allocation and functions/risks/asset analysis|Point 18|
|TNMM|Compare a properly delineated tested party's relevant net-profit indicator with reliable independent/internal uncontrolled results; reconcile the chosen denominator and segment accounts|Point 19 and 21|
|Profit-split|Delineate the relevant combined profit and allocate consistently with evidenced contributions/functions/risks/assets and independent conditions|Point 20|
|Other OECD-recognised method|Explain its suitability to the actual case and data under the statutory most-appropriate-method criteria|Code 226²⁰(3)(f),(5)|

Table sources: [Order 9 annex 1 points 14–21](https://www.legis.md/cautare/getResults?doc_id=152738&lang=ro), [Code 226²⁰](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro). Resale, cost-plus and TNMM require a tested-party selection under point 21. A group policy or a database printout without delineation, comparable selection, adjustments and accounting reconciliation is not the required conclusion.

Build the comparability interval from the justified independent data. Points 22–24 use the lower/upper quartiles as the interval bounds. Point 25's special rule for at most two comparable values uses the minimum/maximum and arithmetic mean for the median. Preserve the data, rejection log, search date, formula and adjustments; the actual quartile interpolation algorithm for larger samples is not prescribed here and remains a precise gap below. A result within a properly established interval is treated as arm's-length; audit adjustment/estimation uses the median under 47. [Order 9 annex 1 points 3,22–25,47](https://www.legis.md/cautare/getResults?doc_id=152738&lang=ro).

### Voluntary and corresponding adjustments

Art. 226²³ allows voluntary income/expense adjustment; for prior periods submit the required corrected information/file and corrected tax returns under 188. Order 9 annex 1 points 26–28 permits adjustment within the interval where pricing is not arm's-length but prevents voluntary correction of the controlled transactions once a TP audit of one of the relevant affiliates has started. SFS can adjust where the principle fails, or estimate where necessary data are absent, and can use another method after demonstrating failure of the taxpayer's method. The amended rules use a thematic tax audit; the former preliminary-review procedure and its protection in repealed point 44 must not be reused as a current amnesty. [Code 226²⁰,226²³,188](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro), [Order 9 annex 1 points 26–49](https://www.legis.md/cautare/getResults?doc_id=152738&lang=ro).

For resident affiliates, 226²¹ makes the SFS adjustment/estimation opposable to the other party. SFS issues the counterpart decision after the 226²¹/252(3) stage, and the other party can amend its income-tax return; where 188(4) blocks amendment, request an audit for double-tax elimination. Order 9 annex 1 point 55(1) specifies 15 working days after the 252(3) 30-day period; its other limb still references the now-repealed point 43, so do not invent a surviving notification process for that branch. For foreign-affiliate adjustments, follow the treaty-dependent application and evidence in Cross-border points below. [Code 226²¹–226²²,252](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro), [Order 9 annex 1 points 54–56](https://www.legis.md/cautare/getResults?doc_id=152738&lang=ro).

### Compile the master file and local file

For periods from 2025, Order 8/2026 points 2–4 and current Order 9 annex 1 point 50 prescribe:

- **Master file:** legal/ownership structure and geography; business drivers/value chain, significant intragroup services, markets, group functions/risks/assets and restructuring; intangible strategy, ownership, agreements, DEMPE and transfers; intragroup/independent financing policy and treasury entities; consolidated financial information or the stated equivalent/segment data; APAs and relevant allocation rulings. DEMPE means development, enhancement, maintenance, protection and exploitation, not legal ownership alone.
- **Local file:** local structure, all affiliates/PEs and direct/indirect affiliation; business/markets/pricing and competitors; each controlled transaction's property/service characteristics and contracts/context, restructuring, service cost allocations and cost-contribution arrangements; detailed functional/comparability analysis; method and tested-party selection; internal/external comparables, search method/data; interval, adjustments and the reasoned arm's-length conclusion.

Use the whole-group master information. Point 51 permits the relevant group segment if complete information is unavailable **and justified reasons are supplied**; this is not an unconditional master-file waiver. The local file must be Romanian; the master file can be Romanian, Russian or English. Paper and/or electronic files are permitted; electronic local/master files require the specified responsible resident taxpayer signatures, with identification of the master-file preparer. Requested copies of underlying contracts/documents require authorised Romanian translation except English/Russian. The information filing itself carries the responsible electronic signature. [Order 9 annex 1 points 50–53²](https://www.legis.md/cautare/getResults?doc_id=152738&lang=ro), [Order 8](https://www.legis.md/cautare/getResults?doc_id=152708&lang=ro).

Retain contracts, invoices, accounting reconciliation, functional interviews, benchmark inputs, signed submissions, the actual SFS request and receipt and review evidence. The current retention rule is expressly unconfirmed below. Preserve the records pending resolution; do not destroy them on an assumed expiry.

## Deadlines and filing

Reconcile a voluntary income/expense adjustment with the income-tax return as well as the TP information/file. The [corporate Guide](md-corporate-income-tax.md) identifies the VEN12 adjustment rows verified directly from enacted MF Order 145/2024. Those return rows are separate from the Order 9 annex-2 information form, whose current fields and code mappings are supplied below. [MF Order 145/2024, read 30 October 2026](https://www.legis.md/cautare/getResults?doc_id=146071&lang=ro); [Code art. 226²³](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro).

Use the actual tax period, including a legally adopted non-calendar fiscal period under art. 12¹, rather than the parent group's reporting calendar by default. The information deadline is the 25th of month six after that period ends. Thus a calendar 2026 period has a statutory 25 June 2027 deadline before any applicable nonworking-day adjustment; a valid 30 June 2026 period has 25 December 2026 on that same basis. The taxpayer's actual fiscal-period eligibility and general calendar adjustment must be confirmed before fixing a live deadline. File-request due time is 120-days from the request but cannot fall before the information deadline; monitor the actual valid request/communication, not an informal conversation. [Code 226¹⁹(2)–(3),12¹](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro).

Annual information is distinct from the requested file and APA application/report. Current Order 9 annex 1 points 53¹–53² requires the approved annex 2 information and responsible electronic signature. Order 8 adds fiscal-period identifiers to annexA row 5, annexB row 6 and annexC row 8, and updates annexB table 2 to sequence, transaction code, object/contract details, party-role code, controlled amount and optional comments. The complete current annex 2, including transaction-role, method, indicator and country catalogues, has now been read and retained; use its field mappings below. Authenticated electronic-field acceptance and legacy country-code handling remain untested. The 12 May 2026 SFS launch notice identifies the electronic-declaration service in the taxpayer cabinet for periods from 2025, but a portal receipt is still required for the actual filing. [Order 9](https://www.legis.md/cautare/getResults?doc_id=152738&lang=ro), [Order 8 points 1.3,4](https://www.legis.md/cautare/getResults?doc_id=152708&lang=ro), [SFS launch notice](https://www.sfs.md/ro/stiri/formularul-privind-preturile-de-transfer-disponibil-in-sia-declaratia-electronica).

Correct information under 226¹⁹(5)/188, using the form and method valid for the corrected period, subject to 188's six-year and audit restrictions. A corrected **file** has the separate 30-day decision-communication rule in 226¹⁹(6); do not turn it into a general extension of an original request. Titles II/X determine the related return; the special IT-park TP single-tax return under 373(1¹) is not automatically an ordinary 12% corporation-tax calculation. Its actual current forms and field computation are supplied below, with the specific minimum/refund-floor and portal ambiguities retained. [Code 226¹⁹,188,226¹⁸(4)](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro), [Law 187 art. II point 28](https://www.legis.md/cautare/getResults?doc_id=149593&lang=ro).

### Complete the actual current information form

Use the actual annex 2 linked from current Order 9/2024, incorporating Order 8/2026 for periods from 2025. Its first-page caption incorrectly says “nr.9 din februarie 2023”; the enacted parent, current attachment link and amended fields identify the applicable form. The complete 20-page attachment, including its four nomenclatures, is retained. This is a form-completion method, not a portal submission receipt. [Current Order 9](https://www.legis.md/cautare/getResults?doc_id=152738&lang=ro); [actual information annex](https://www.legis.md/UserFiles/Image/RO/2026/mo55-58ro/an_2_9md.docx); [Order 8 point 4](https://www.legis.md/cautare/getResults?doc_id=152708&lang=ro).

| Form area | Fields and reconciliation |
|---|---|
| Main table 1 | Registered taxpayer name and fiscal identifier; actual main activity and four-digit CAEM code; reporting fiscal period in row 5. The signature area records presentation date, director/administrator, IDNP and signature. |
| Main table 2 | For each reported affiliate, name, fiscal identifier, **registration-state name and code**, and total controlled amount in MDL. A Moldovan fiscal resident uses the Moldovan identifier; the stated nonresident route uses the identifier assigned where registered. Use this annex's own country nomenclature, rather than treating citizenship, registration and tax residence as interchangeable. |
| Main table 3 | Separately identify the affiliates/controlled transactions actually covered by an APA, with the corresponding name/identifier/state/code/MDL amount fields. Keep the statutory APA exclusion from threshold calculation distinct from reporting its covered amounts. |
| Annex A | One affiliation schedule per affiliate. Row 5 is the fiscal period. Codes 1001/1002/1003 identify taxpayer ownership of affiliate, affiliate ownership of taxpayer, or common third-party ownership, respectively, using the stated minimum 25% voting-participation test. Show direct, indirect and total shares and the actual intermediary chains; common ownership has separate taxpayer/affiliate columns. Codes 1004/1005/1006 identify the corresponding effective-control directions through appointments, contracts, constitutive provisions or voting agreements. A share below 25% does not by itself disprove effective control. |
| Annex B | One schedule per affiliate. Its identity table includes affiliation code in 5 and fiscal period in 6. Current transaction table 2 has **six columns**: sequence; transaction code; actual object/contract number/date; **taxpayer's role** code; controlled amount; optional comments. Do not put the affiliate's role in the taxpayer-role field. Instruction 25's comments subpoint is numbered 7, but maps to actual column 6. |
| Annex C, APA compliance | One schedule per affiliate with transactions actually covered by the APA. Header fields include affiliation 5, unilateral/bilateral/multilateral type 6, APA number/date 7 and fiscal period 8. The transaction table has nine columns: sequence, transaction code, object/contract details, taxpayer-role code, method code, profit-indicator code, measured indicator, controlled amount and optional comments. This separate annual APA compliance report follows the already-sourced income-tax-return deadline, rather than being made due at the sixth-month information deadline merely by its location in the packet. |

Table sources: [actual information form and instructions 1–36, including 10¹–10⁵,15¹,24¹,35¹](https://www.legis.md/UserFiles/Image/RO/2026/mo55-58ro/an_2_9md.docx); threshold/APA scope and deadline remain governed by [Code 226¹⁹,226²⁹](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro). Keep the MDL/no-VAT/exclusion working paper above, rather than replacing current statutory financing and advance exclusions with the older accounting-recognition wording removed by Order 8.

### Transaction-role, method and indicator codes

These are the actual transaction catalogue's paired codes. Preserve leading zeroes in transaction codes and select the **filing taxpayer's** side. An affiliation code 1001 in Annex A means ownership; transaction-role 1001 means seller. They belong to different fields. [Information annex, nomenclature 2 and instructions 25/36](https://www.legis.md/UserFiles/Image/RO/2026/mo55-58ro/an_2_9md.docx).

| Transaction | Contract | Taxpayer-role codes |
|---|---|---|
| 0001 | Sale/purchase | 1001 seller; 2001 buyer |
| 0002 | Loan | 1002 lender; 2002 borrower |
| 0003 | Locațiune | 1003 locator; 2003 locatar |
| 0004 | Arendă | 1004 arendator; 2004 arendaș |
| 0005 | Leasing | 1005 locator; 2005 locatar |
| 0006 | Works, antrepriză | 1006 contractor; 2006 client |
| 0007 | Services | 1007 provider; 2007 beneficiary |
| 0008 | Transport | 1008 transporter; 2008 client |
| 0009 | Forwarding, expediție | 1009 expeditor; 2009 client |
| 0010 | Mandate | 1010 mandant; 2010 mandatar |
| 0011 | Commission | 1011 comisionar; 2011 comitent |
| 0012 | Deposit | 1012 deponent; 2012 depozitar |
| 0013 | Intermediation | 1013 intermediary; 2013 client |
| 0014 | Commercial agency | 1014 commercial agent; 2014 principal |
| 0015 | Franchise | 1015 franchisor; 2015 franchisee |
| 0016 | Distribution | 1016 supplier; 2016 distributor |
| 0017 | Credit | 1017 creditor; 2017 debtor |
| 0018 | Insurance | 1018 insurer; 2018 insured |
| 0019 | Civil partnership | 1019 participant; no second role printed |
| 0020 | Other contracts | 1020 financial outflow; 2020 financial inflow |

For Annex C, method codes are **01 CUP; 02 cost-plus; 03 resale price; 04 TNMM; 05 profit split; 06 other OECD-recognised methods**. Do not swap 02/03 or infer that a code alone justifies method selection. Profit-indicator codes are 01 resale margin; 02 cost-plus gross-profit margin; 03 return on total assets; 04 return on total costs; 05 return on sales; 06 return on operating costs; 07 gross sales margin; 08 economic return; 09 financial return; 10 return on resources consumed; 11 Berry ratio; 12 other indicator. Select the actual agreed method/indicator and reconcile its accounting definition and measured value to the APA and supporting analysis; the catalogue's label alone supplies no universal denominator or safe harbour. [Nomenclatures 3–4 and instruction 36](https://www.legis.md/UserFiles/Image/RO/2026/mo55-58ro/an_2_9md.docx).

The country nomenclature supplies, for example, 004 Afghanistan, 276 Germany, 470 Malta, 498 Moldova, 642 Romania, 826 United Kingdom and 840 United States, plus 000 “Altele”. Use the actual registration-state entry and preserve its three characters. The retained list has legacy labels, including 720 “Yemen democratic”; do not silently replace it with a modern ISO list or certify an unresolved portal mapping for an unlisted/currently renamed jurisdiction. [Nomenclature 1 and instructions 8–9](https://www.legis.md/UserFiles/Image/RO/2026/mo55-58ro/an_2_9md.docx).

For an assumed eligible non-APA affiliate, reconcile goods sold for MDL 9 million using 0001/1001, services bought for MDL 8 million using 0007/2007 and eligible calculated loan interest of MDL 3 million using 0002/2002. The total is MDL 20 million without netting inflows against outflows; assumed loan principal of MDL 50 million and advances of MDL 2 million remain outside the stated statutory threshold. A separate actual-APA-covered amount belongs in its own covered schedule and is not added back to that threshold merely because the form records it. These assumed records test classification and aggregation, not whether a real contract meets the legal exclusions. [Actual transaction catalogue](https://www.legis.md/UserFiles/Image/RO/2026/mo55-58ro/an_2_9md.docx); [Code 226¹⁹](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro).

### IT-park related-party adjustment return: IUPT25 and IUPT24

IUPT is a single-tax adjustment return for the applicable affiliated transactions, separate from the Order 9 TP information form/file and the monthly IU17. The current Order 135 annex 7 is actually labelled **IUPT25**; annex 9 is explicitly **IUPT24 for 2024**. Original forms/instructions 7–10 were fully text-read and visually inspected, including all eight rendered pages. Do not use a 12% ordinary company calculation for a 7% park sales-base adjustment, or rename the approved form because its label contains 25. Establish the correct taxpayer, covered transaction, arm's-length adjustment and fiscal period first. [Current Order 135][parkorder]; [actual IUPT25][iupt25actual] and [instructions][iupt25instructions]; [actual IUPT24][iupt24actual] and [instructions][iupt24instructions]; [Code 373(1^1)](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro).

**Commencement matters.** Actual Order 106 of **10 October 2025**, published **28 October 2025**, adds the annual and 2024-specific annexes. Points **1,3,4,5** take effect on **1 January 2026**; the other provisions take effect on publication. Thus current monthly IU17 no longer includes old rows 011/012, while the annual IUPT25 method explicitly carries the 2025 adjustments that were already reported through monthly IU17. IUPT24 separately isolates 2024 adjustments already reported monthly in 013. Preserve those returns and make the annual bridge once. The current general deadline is the **25th of the sixth month after the article 12^1 fiscal period**; Law 187 article XXVI(4) separately prints **25 December 2025** for the 2024 transition; the [SFS notice of 15 December 2025](https://www.sfs.md/ro/stiri/formularul-darii-de-seama-privind-impozitul-unic-pentru-tranzactii-cu-persoane-afiliate-pentru-anul-2024-disponibil-online) announces **26 December 2025** as the filing date. Code 129(8) supplies the nonworking day rollover and full day electronic filing rule. The historical deadline is not an extension or template for 2026 periods. [Order 106 points 1–8][park106]; [Law 187 article XXVI(4)](https://www.legis.md/cautare/getResults?doc_id=149593&lang=ro); [Code 373(1^1)](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro).

Use registered identity, CAEM-2 activity, park registration code, head-office four-character CUATM and actual submission date. IUPT25 instruction 6 supplies **A/YYYY** for the annual reporting year; IUPT24 prints **A/2024**. These are not the monthly IU17 L/NN/YYYY code or the IPC21 taxpayer marker. Head-only and the stated authorised two-signature routes are separate from electronic acceptance. [Annex 8 instructions 1–7,16][iupt25instructions]; [annex 10 instructions 1–7,17][iupt24instructions]; [actual forms][iupt25actual].

| IUPT field | General annex 7/IUPT25 | 2024-specific annex 9/IUPT24 |
|---|---|---|
| 011 column 3 | Annual financial-accounting sales, account 611, under SNC/IFRS | The corresponding 2024 accounting sales |
| 012 column 3 | Annual article 226^23(1) sales adjustment; for 2025 include the previously monthly-reported adjustments and subsequent adjustments once | Adjustments excluding those separately reported in 013 |
| 013 column 3 | No such row in the general form | Adjustments already reported through 2024 IU17, kept disjoint from 012 |
| 010 columns 3–5 | **011 +012** in 3; printed **7%** in 4; resulting tax in 5 | **011 +012 +013** in 3; the same printed rate/calculation |
| 020 column 5 | The instructed average annual minimum under article 370(2); instruction 11 says sum the single-tax amounts and divide by 12 | Instruction 12 specifies the corresponding 2024 average and divisor 12 |
| 030 column 5 | Tax calculated for the reporting period | Tax calculated for 2024 |
| 040 column 5 | Tax actually paid for that reporting period, reconciled to payments/account | Tax actually paid for 2024 |
| 050; 060 column 5 | Adjustment calculation and its payable/refundable route under instructions 14–15 | The corresponding calculation under instructions 15–16 |

Sources: [actual general form][iupt25actual]; [instructions 8–15][iupt25instructions]; [actual 2024 form][iupt24actual]; [instructions 8–16][iupt24instructions]. Keep the 020 average, 030 calculated tax and 040 actual payment as different measures. The minimum row's label expressly refers to the statutory minimum, while its explanation says to sum “single tax” and divide by 12; retain the monthly minimum and actual-tax schedules separately. Neither the wording nor the divisor alone verifies a different partial year divisor or which electronic validation the portal applies. Do not silently substitute annual total minimum or actual 7% tax for the required average without resolving that source conflict.

Let **T=010 column 5**, **B=030 column 5** and **M=020 column 5**. The published branches, rather than an invented single formula, are:

| Published branch | IUPT25 instruction 14 / IUPT24 instruction 15 |
|---|---|
| T>B and T>M | 050=T−B;060 follows the payable route. |
| T≤B and T>M | 050=T−B;060 follows the refundable route. Keep a zero result zero. |
| T≤B, T<M and B=M | 050=0. |
| T≤B, T<M and B>M | The text says T−B, “not less than” M, while the next instruction calls it refundable. The signed-floor interpretation is unresolved; do not encode it as an automatic positive floor, negative floor or approved cash refund. |

The instructions do not expressly resolve **T=M**, or every other ordering/equality case. Their published 050/060 formulas also contain no explicit subtraction of 040, although actual paid tax is collected separately. Record these as source/implementation gaps; a return's “refund” label does not prove an amount was actually paid, an accepted tax-account credit or approval for cash reimbursement. Current Code 373(3) sends excess-payment refunds through article 176 and the receiving revenue administrators. [Annex 8 instructions 11–15][iupt25instructions]; [annex 10 instructions 12–16][iupt24instructions]; [Code 373(3)](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro).

For a clear upward branch, assume accounted annual sales **1,000,000**, an evidenced disjoint upward sales adjustment **100,000**, B of **70,000**, and established M of **5,220**. General 010 base is **1,100,000**, T is **77,000** and the additional assessed tax under branch(a) is **7,000**. Actual 040 of **65,000** would be an account/payment fact; it does not turn the published T−B adjustment into **12,000**. Reconcile the pre-existing 5,000 shortfall separately before concluding a cash amount due. This example uses an expressly clear ordering and established M; it does not settle the ambiguous average/floor cases. [Annex 8 instructions 8–15][iupt25instructions]; [actual form][iupt25actual].

For a 2024 bridge, assumed account 611 sales **1,000,000**, later adjustments in 012 of **80,000**, and disjoint previously monthly-reported adjustments in 013 of **20,000** give 010 base **1,100,000** and T **77,000**. Adding the full 100,000 to 012 and repeating 20,000 in 013 would incorrectly give 1,120,000 and 78,400. For 2025 the general 012 includes both buckets once and has no 013. Preserve the monthly returns, adjusted amounts and original calculated tax; do not erase historical adjustments merely because current IU17 has removed the old monthly fields. [Annex 10 instructions 8–11][iupt24instructions]; [annex 8 instruction 10][iupt25instructions]; [Order 106 points 3–4,8][park106].

### APA application and monitoring

An APA requires an application, relevant documents and fee proof, and cannot cover transactions already subject to an ongoing/completed TP audit at application. Residents and registered foreign-person PEs/branches can apply; a bilateral/multilateral APA requires the relevant treaty. An optional written preliminary discussion request is answered with a meeting date within 30-days. For unilateral requests use Romanian; bilateral/multilateral requests use English, with the annex 3 translation requirements. Supply entity/affiliate details, structure, functional/DEMPE analysis, selected method/tested party, comparables/interval, periods, critical assumptions, foreign-authority request where relevant, fee proof, authenticity/no-proceedings declarations and supporting copies. Do not submit duplicate same-object applications already under consideration. [Code 226²⁵](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro), [Order 9 annex 3 points 1–15](https://www.legis.md/cautare/getResults?doc_id=152738&lang=ro).

Track **admissibility separately from substantive resolution**: annex 3 points 16–19 allows 30-days for unilateral admissibility and seven months for bilateral/multilateral admissibility, including foreign-authority availability. After admission, point 26 allows six/twelve/eighteen months for unilateral/bilateral/multilateral resolution, with the point 27 suspension grounds. The Code's foreign refusal/no-response-six-month route gives 30-days after communication to withdraw/refund or convert the request; do not promise a six-month overall result. The draft decision allows 30-days for objections and the specified 15-day response after rejected objections; the decision is communicated within 10 working days. [Code 226²⁵(6)–(7)](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro), [Order 9 annex 3 points 16–44](https://www.legis.md/cautare/getResults?doc_id=152738&lang=ro).

The APA's scope, transaction types, period, assumptions, method, interval and conditions control protection; an application alone is not approval. Monitor material changes and file the revision request within 30-days of a point 46 condition, observing the statutory pre-expiry request rule as well. Annex 3 points 45–67 govern extension/revision and decisions. Annually report APA compliance by the **income-tax return deadline** under 226²⁹, with electronic signature and the prescribed annex 2 reporting content; this is not the sixth-month information deadline. Code 226³⁰ and annex 3 points 70–86 allow audit/termination: “revocarea” operates from conclusion, “anularea” from cancellation, with distinct false-data/noncompliance/changed-assumption/no-report grounds and objection routes. Preserve the actual decision before excluding covered transactions from the threshold. [Code 226²⁵–226³⁰](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro), [Order 9 annex 3](https://www.legis.md/cautare/getResults?doc_id=152738&lang=ro).

Pay the per-type fee before application/modification. Annex 3 points 87–90 sends it to the State budget; withdrawal before admission permits requested refund through the statutory process, while withdrawal after admission does not under that ordinary branch. Separately apply the Code's foreign-refusal/no-response and other specific reapplication/refund routes; do not infer a blanket refund entitlement. The approved APA application model is mapped below; technical payment/refund implementation remains unconfirmed. [Code 226²⁵(7),226²⁸](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro), [Order 9 annex 3 points 21–25,55–57,87–90](https://www.legis.md/cautare/getResults?doc_id=152738&lang=ro).

### Prepare the approved APA application model

The actual two-page model is Order 9 annex 3 introduced through Order 8/2026 annex 1; distinguish this **application model** from the APA procedure in the TP regulation and from information-form Annex C's annual compliance report. Address it to SFS, date it and preserve the authority's registration reference. [Order 8 point 1.1](https://www.legis.md/cautare/getResults?doc_id=152708&lang=ro); [approved model](https://www.legis.md/UserFiles/Image/RO/2026/mo55-58ro/an3_9ro.docx).

| Model section | Actual requested material |
|---|---|
| I | Taxpayer name/code, legal/correspondence addresses, telephone/email, representative and representative's legal capacity. |
| II | APA type; partner jurisdiction for bilateral/multilateral requests; covered transactions; affiliated-party names, fiscal identifiers and legal addresses; evidence of the foreign-authority request where relevant; covered fiscal periods. |
| III–VII | Annex 1 activity description; 2 functional analysis; 3 selected pricing method; 4 comparability interval; 5 critical assumptions. These are application exhibits, not the information form's similarly numbered code catalogues. |
| VIII–IX | Conclusions and the APA fee exhibit 6. Retain actual payment evidence under the applicable procedure; the blank model is not proof of payment. |
| X–XI | Authenticity/completeness/correctness declaration and declaration that no relevant administrative/tax-audit, criminal or judicial proceedings are ongoing/completed. Section XI also contains an undertaking to notify SFS within a maximum 10 days if proceedings arise; it does not call those working days. Keep that undertaking separate from the 30-day changed-assumptions/revision procedure. |
| XII–XIII and signature | Actual exhibit list, other relevant information and authorised signature. Check the underlying admissibility, language, fee and evidence requirements above before submission. |

Source: [complete approved APA application model I–XIII](https://www.legis.md/UserFiles/Image/RO/2026/mo55-58ro/an3_9ro.docx), read 31 October 2026. Receipt, electronic-field acceptance, technical payment/refund handling and any case-specific deadline computation remain separate evidence requirements.

## Penalties and interest

**Calendar-2026 ordinary tax late charge.** Code art. 228(3) and the BNM decision of 6 November 2025, point 1, supply the calculation: the retained **6.00%** short-term policy rate, rounded up to a whole percent, plus **5 percentage points**, divided by **365 days**, gives **0.0301% per delayed day** after rounding the daily percentage to four decimal places. The decimal multiplier is **0.000301**. Apply it to the established outstanding principal for each chargeable day; split changes in principal and calendar year. This calculation concerns debts governed by art. 228 and does not replace a separate statutory regime's rate or establish case-specific relief. [Code art. 228(2)–(3)](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro); [BNM decision, point 1](https://bnm.md/en/node/69226).

Map the offence and period, rather than multiplying one late-return fine by every missing document:

| Offence | Statutory fine | Provision |
|---|---|---|
|Late annual information|MDL 30,000–50,000|260(7)|
|No annual information|MDL 100,000–150,000|260(9)|
|Late TP file|MDL 30,000–50,000|260(10)|
|No TP file|MDL 300,000–500,000|260(12), with applicable transition exceptions|
|False information causing understatement/evasion|MDL 60,000–90,000; special commencement below|260(8)|
|False file causing understatement/evasion|MDL 150,000–200,000; special commencement below|260(11)|

Figures: [Code 260(7)–(12)](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro). **Law 214/2024 art. XVII(2)** applies 260(8),(11) in SFS audits of fiscal periods beginning with 2028; do not charge those two penalties as 2026-period sanctions merely because their amounts appear in the Code. This does not postpone the ordinary late/non-submission duties or the underlying tax/interest. The separate 2024 file transition is in Law 187 art. XXVI(3). [Law 214 official text](https://www.legis.md/cautare/getResults?doc_id=144601&lang=ro), [Law 187](https://www.legis.md/cautare/getResults?doc_id=149593&lang=ro).

For the specific **article 228(2^1) self-correction route**, the late charge is capped at the corresponding additional tax obligation. The paragraph covers discovery of errors/omissions followed by a corrected return, and the stated no-return-duty case where erroneous calculation/payment creates an additional obligation. Establish those conditions before applying the cap; it is not a universal cap on every audit debt, sanction or late charge. [Code art.228(2^1)](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro); exact source context is retained in ledger row MD-TP-088.

Additional income/expense adjustments can change the relevant income/single tax. General understatement/evasion and self-correction provisions are in 261(4)–(5)/188; establish the actual offence and interaction before stacking sanctions. Art. 228 charges late-payment interest from after due date through payment using its prior-November BNM base-rate-plus-five-points annual formula; case-specific relief and any applicable special single-tax rate must be established. An objection does not automatically suspend collection under 252(2). [Code 228,252,261,188](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro).

## Cross-border points

For a foreign corresponding adjustment, 226²² requires the applicable double-tax treaty and a resident's application with evidence of the foreign affiliate's arm's-length adjustment/assessment. SFS has 30 working days to confirm, reject with reasons for insufficient basis/documents, or order an audit. Do not post an automatic equal tax credit or deduction from a foreign assessment. A treaty mutual-agreement route, beneficial ownership and the actual treaty/protocol are distinct questions covered by the cross-border Guide; no universal treaty outcome is assumed. [Code 226²²,4](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro).

A bilateral/multilateral APA needs the treaty/foreign-authority process in 226²⁵; a unilateral APA does not compel a foreign authority to accept the price. PE/head-office affiliation does not itself make every head-office charge deductible: test the substantive PE, interest, royalty and service rules in the cross-border/corporate Guides. VAT follows its own base and place rules and is not automatically changed by a TP adjustment. The group master file is not a country-by-country report; current CbC/reporting/exchange applicability remains expressly unconfirmed, not assumed from another jurisdiction's EUR 750m threshold. [Code 226¹⁷–226¹⁸,226²⁵](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro).

## Two worked examples that recompute

### 1. Aggregate threshold with the statutory exclusions

Assume all parties satisfy the relevant affiliation/local-or-cross-border conditions, values are already evidenced in MDL, and the ordinary eligible affiliate flows are 12m sales, 7.5m purchases and 0.5m calculated loan interest. Separate ledger entries are 4m APA-covered transactions, 2m advances, 10m loan principal, 0.3m accounting FX differences (not currency-exchange trades),0.2m asset/liability revaluation and 3.9m VAT; no overlap with the eligible flows. The eligible 20m reaches the threshold. The information is required; file submission still needs the SFS request. [Code 226¹⁹(1),(3),(4),(7)](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro).

```oa-check
name: Moldova TP aggregate reconciled to statutory exclusions
inputs:
  eligible_sales: 12000000
  eligible_purchases: 7500000
  interest: 500000
  apa_covered: 4000000
  advances: 2000000
  loan_principal: 10000000
  accounting_fx: 300000
  revaluation: 200000
  vat: 3900000
  threshold: 20000000
steps:
  eligible_total: eligible_sales + eligible_purchases + interest
  excluded_total: apa_covered + advances + loan_principal + accounting_fx + revaluation + vat
  ledger_total: eligible_total + excluded_total
  threshold_difference: eligible_total - threshold
expected:
  eligible_total: 20000000
  excluded_total: 20400000
  ledger_total: 40400000
  threshold_difference: 0
```

Eligible flows of 12m+8m total 20m and meet the information threshold, as do eligible flows of 49.9m or 50m. A higher amount creates no automatic file-submission tier. Check the affiliation and exclusion assumptions.

### 2. Audit CUP adjustment with two reliable comparable prices

Assume an ordinary 12% corporation sells 10,000 units to a covered affiliate at MDL 60 each. Two genuinely comparable uncontrolled unit prices are MDL 80 and 100 after reliable adjustments; assume the audit has established comparability and non-arm's-length pricing. Order 9 annex 1 point 25 gives bounds 80/100 and median 90; the audit point 47 target produces 300,000 additional income and 36,000 tax before any other relief/credit. No extra costs or loss/credit offsets are assumed. This is not a proposed market price for an actual client, and the TP adjustment does not automatically alter VAT. [Order 9 points 16,25,47](https://www.legis.md/cautare/getResults?doc_id=152738&lang=ro), [Code 15(b),226¹⁸(6),226²⁰](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro).

```oa-check
name: Moldova audit CUP median and ordinary corporate tax
inputs:
  units: 10000
  actual_unit_price: 60
  comparable_low: 80
  comparable_high: 100
  ordinary_tax_rate: 0.12
steps:
  interval_lower: min(comparable_low, comparable_high)
  interval_upper: max(comparable_low, comparable_high)
  median: (comparable_low + comparable_high) / 2
  actual_revenue: units * actual_unit_price
  adjusted_revenue: units * median
  additional_taxable_income: adjusted_revenue - actual_revenue
  additional_tax: additional_taxable_income * ordinary_tax_rate
expected:
  interval_lower: 80
  interval_upper: 100
  median: 90
  actual_revenue: 600000
  adjusted_revenue: 900000
  additional_taxable_income: 300000
  additional_tax: 36000
```

## Ask the client first

- What are the actual fiscal period, legal entity/branch/PE, residence and tax regimes of every potentially affiliated party? Obtain the complete voting/control/family structure and changes.
- Reconcile all sales/purchases/rights/services/financing flows excluding VAT. Which amounts are advances, interest/principal, currency trades versus FX accounting differences, revaluations or actually APA-covered transactions?
- What do contracts and real conduct show about functions, risk control/financial capacity, assets and DEMPE? Obtain segment accounts, allocation keys and evidence for intragroup services, intangibles, financing and restructurings.
- Which independent/internal comparables, adjustments, methods and tested-party data are available? What supports geography, timing, quantity, terms and the interval calculation?
- Has SFS requested a file, communicated an assessment or started an audit of either relevant affiliate? Obtain actual communications and submission receipts before deciding correction/deadline options.
- Obtain the group master/local files, language/signature authority, prior information filings, current annexes, actual APA decisions/assumptions and annual compliance reports. Is a foreign adjustment or bilateral/multilateral request supported by an actual treaty and foreign-authority evidence?

## Sources

**Bounded source review, 31 October 2026.** The [independent review record](../../evidence/ledgers/md-country-evidence/independent-review/FINAL-REVIEW.md) covers the stated source/claim scope. Ordinary gaps below remain unresolved. This Guide remains a source-cited draft, without accountant attestation or comprehensive coverage.

|Primary source actually read|Scope|Read|
|---|---|---|
| [BNM monetary-policy decision, 6 November 2025, point 1](https://bnm.md/en/node/69226) | Fetched 6.00% short-term base input; calendar-2026 daily percentage derived with Code 228(3), rather than copied from an old rate. | 2026-10-30 |
|[Current Fiscal Code 157050](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro)|226¹⁷–226³⁰,260,252,188 and relevant ordinary tax/interest provisions; selected articles only|2026-10-30|
|[Law 187/2025](https://www.legis.md/cautare/getResults?doc_id=149593&lang=ro)|ArtII point 19, selected point 28 and art. XXVI: period 2025 structure and separate 2024 transition|2026-10-30|
|[Order 9 current consolidation 152738](https://www.legis.md/cautare/getResults?doc_id=152738&lang=ro)|Complete rendered annex 1 and annex 3 text: pricing, documentation, amendments and APA procedure. Current annex 2 separately retained/read on 31 October as below|2026-10-30|
|[Order 8/2026](https://www.legis.md/cautare/getResults?doc_id=152708&lang=ro)|Current master/local file, language/signature/form amendments; applies stated file/information changes to periods from 2025|2026-10-30|
|[Law 214/2024 art. XVII(2)](https://www.legis.md/cautare/getResults?doc_id=144601&lang=ro)|Exact paragraph read in the official browser-rendered law; delayed 260(8),(11) period 2028 sanctions. No successful PDF-download claim|2026-10-30|
|[SFS 12 May 2026 electronic-form launch](https://www.sfs.md/ro/stiri/formularul-privind-preturile-de-transfer-disponibil-in-sia-declaratia-electronica)|Official search-returned notice identifies the 2025-onward electronic service. Direct retrieval 403; portal/form not tested|2026-10-30|
| [Current information annex 2, complete approved DOCX](https://www.legis.md/UserFiles/Image/RO/2026/mo55-58ro/an_2_9md.docx) | All 20 rendered pages and original Word text: main form, affiliation A, transaction B, APA report C, instructions and all four code catalogues; incorrect February 2023 caption and comments numbering retained as source defects. Parent Order 9 current header/link rechecked. | 2026-10-31 |
| [Approved APA application model](https://www.legis.md/UserFiles/Image/RO/2026/mo55-58ro/an3_9ro.docx) | Both pages, sections I–XIII/signature; six exhibits and specific maximum-10-day proceedings undertaking. Parent Order 8 header/link rechecked. | 2026-10-31 |

| [Current Order 135][parkorder], [enacted Order 106][park106], [IUPT25 form][iupt25actual]/[instructions][iupt25instructions] and [IUPT24 form][iupt24actual]/[instructions][iupt24instructions] | Allfour original DOCX attachments/all 8 rendered pages read. Annualadjustment/monthly bridge and clear calculation branches mapped; minimum-average wording, partial-year divisor, missing equalities, signed refund floor and actual account/portal approval remain explicit | 2026-10-31 |

Not yet confirmed: authenticated portal acceptance, legacy country-code/renamed-jurisdiction mapping and actual submission receipts; APA technical payment/refund implementation; general deadline adjustment/communication and foreign-currency conversion mechanics for an actual off-calendar case; current TP-record retention trigger after repeal/rewrite of the former six-year clause; larger-sample quartile interpolation; application of the stale annex 1 point 55(2) cross-reference for voluntary corresponding adjustments; IUPT minimum-average wording/partial-year divisor, omitted equality branches, signed refund-floor interpretation and actual tax-account/portal/refund implementation beyond the now-mapped form method; CbC/exchange applicability and specialist OECD/treaty routes; transaction-specific independent comparables, actual treaty texts/protocols and full amendment/commencement reconciliation. These are explicit source/procedure gaps. Neither the ledger nor this expanded draft establishes independent whole-country review, accountant attestation or comprehensive coverage.

[parkorder]: https://www.legis.md/cautare/getResults?doc_id=154298&lang=ro
[park106]: https://www.legis.md/cautare/getResults?doc_id=151376&lang=ro
[iupt25actual]: https://www.legis.md/UserFiles/Image/RO/2025/mo544-546ro/an7_135md.docx
[iupt25instructions]: https://www.legis.md/UserFiles/Image/RO/2025/mo544-546ro/an8_135md.docx
[iupt24actual]: https://www.legis.md/UserFiles/Image/RO/2025/mo544-546ro/an9_135md.docx
[iupt24instructions]: https://www.legis.md/UserFiles/Image/RO/2025/mo544-546ro/an10_135md.docx

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This document is general reference information, not advice for a specific transaction. Consult the cited legislation and a Moldovan transfer-pricing specialist before filing or setting prices.

## Sources

- Moldova Fiscal Code, Title V, Chapter 11², official consolidated text: https://www.legis.md/cautare/getResults?doc_id=142855&lang=ro (read 2026-10-24)
- Law 187/2025, amendment to Article 226¹⁹: https://www.legis.md/cautare/downloadpdf/149593 (read 2026-10-24)
- Ministry of Finance Order 9/2024, as amended by Orders 21/2025 and 8/2026: https://www.legis.md/cautare/downloadpdf/147520 and https://www.legis.md/cautare/downloadpdf/152708 (read 2026-10-24)
- State Tax Service transfer-pricing page and 2025 reporting deadline notice: https://www.sfs.md/ro/pagina/preturi-de-transfer and https://www.sfs.md/ru/novosti/25-iunie-2026-termen-limita-de-prezentare-a-informatiei-privind-preturile-de-transfer-pentru-anul-2025 (read 2026-10-24)
