---
name: digital-services-tax-matrix
description: "Screen country digital-services taxes for 2026, classify revenue and users, apply period-specific thresholds and rates, distinguish repealed charges and unresolved claims, and prepare a practitioner review file."
version: 0.2
jurisdiction: GLOBAL
tax_year: 2026
last_updated: 2026-11-15
depends_on:
  - cross-border-workflow-base
category: cross-border
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: cross-border
type: cross-country-method
---

# Digital services tax matrix

## Scope

Use this Guide to screen a digital business for country taxes on digital revenue, then prepare a country practitioner’s review file. Its source cut-off is **2026-11-15**; apply the period-specific rules below. It is a research draft, not an accountant attestation. The countries named in the original are all retained, including separately identified research gaps. This is not a claim to cover every digital tax worldwide.

Load `cross-border-workflow-base` first. Keep VAT/GST, permanent establishment, royalty/technical-service withholding, platform reporting and Amount A computations in their own workstreams. Route them to `cross-border-vat-gst.md`, `eu-oss-digital.md`, `permanent-establishment-risk.md` and `withholding-tax-matrix.md`, as applicable; check whether the proposed DAC7 and Amount A companion files exist before relying on them. Kenya’s SEPT and Vietnam’s income-tax rules are identified here because the old matrix included them, although they require income-tax analysis.

## Ask the client first

Obtain the legal entity and group chart, consolidated and entity accounts, accounting dates, prior and current calendar-year revenue, and revenue split by service and country. Identify the actual supplier, contracting entity, recipient, permanent establishments and related parties. Separate targeted advertising, advertising-related data, other data sales, marketplaces, social media, search, streaming/content, own goods, payments, software/SaaS and professional services. Record whether income is earned, invoiced, received or receivable, with dates spanning any transition.

Obtain user/device and account-opening evidence, ad impressions, marketplace transaction and user counts, data-subject locations, billing and payment evidence, underlying land/accommodation locations, and the reconciliation to accounts. Do not collect unnecessary personal information. Obtain registrations, prior returns, assessments, instalments, refund records and elections. Ask for the UK activity-level operating expenses if considering its alternative calculation. Record missing information as an open item, not a zero.

## The method, step by step

### Start with the service, taxpayer and period

Make one assessment for each country and revenue stream. Establish whether the rule is enacted and operative for that period, then apply its service definition, exclusions, group definition, revenue measurement period, threshold comparison and allocation rule. A local threshold is not automatically a tax-free allowance. A group threshold does not automatically create a group taxpayer or authorise a common filer. Do not substitute the country-by-country reporting test for a DST test.

### United Kingdom: [Finance Act 2020 Part 2](https://www.legislation.gov.uk/ukpga/2020/14/part/2)

<!-- D01 -->
The UK charge applies from **2020-04-01** and covers revenue connected with social media, internet search engines and online marketplaces, including associated advertising services deriving significant benefit from them. Social media needs user interaction and significant user-generated content; an internal website search is excluded. A marketplace must facilitate users’ sales or offers to other users, including hiring. An online financial marketplace is excluded where the statutory majority-of-revenue trading test is met. Standalone advertising, standalone data sales and ordinary streaming subscriptions are not automatically taxable merely because they are digital. Apply sections 40–45 to the actual business.

<!-- D02 -->
For a full accounting year, both group digital-services revenue **exceeding GBP 500 million** and UK digital-services revenue **exceeding GBP 25 million** are required. These are current-period digital revenue tests, not total group turnover tests. Reduce both thresholds proportionately for a shorter period. Under the general calculation, subtract the **GBP 25 million** group UK allowance, also reduced for a shorter period, and apply **2%**. Allocate the resulting group amount to relevant entities in proportion to their UK revenue. Group and accounting-period definitions are in sections 57–64; group accounts, including consolidation adjustments, govern revenue recognition. [Sections 46–47, 57–64](https://www.legislation.gov.uk/ukpga/2020/14/part/2).

<!-- D03 -->
A UK individual user is normally in the UK; other users are established there. Exclude the provider, group members and relevant employees acting for them. Marketplace transactions can be attributable where a UK user is a party; UK land/accommodation and marketplace advertising paid by a UK user have separate rules. Foreign land/accommodation exceptions also apply. Other advertising follows consumption by UK users, with just and reasonable allocation where mixed; other revenue connected with UK users also uses that allocation. Do not apply one device-location fraction to every category. [Sections 41–44](https://www.legislation.gov.uk/ukpga/2020/14/part/2).

<!-- D04 -->
An election in the return can apply the alternative charge separately to social media, search and marketplace categories. Allocate the UK allowance proportionately across categories. For an elected category the tax is **0.8 × UK operating margin × net revenue after its allowance share**; a loss gives a nil margin. Unelected categories retain the general rate. Relevant operating expenses must relate to that category’s UK revenue; exclude interest, business acquisition costs, abnormal items, asset revaluations and taxes. This is an election and calculation, not an automatic loss exemption. [Sections 48–49 and HMRC calculation guide](https://www.gov.uk/guidance/work-out-your-digital-services-tax).

<!-- D05 -->
For a claimed qualifying cross-border marketplace transaction, disregard **50%** of the relevant UK revenue and relevant alternative-method operating expenses. A foreign user must be a party and the transaction revenue must be, or would be, subject to a comparable foreign DST charge. This is not general relief for all double taxation. The Act also counteracts relevant avoidance arrangements. [Sections 50 and 65](https://www.legislation.gov.uk/ukpga/2020/14/part/2).

### France: [CIBS L453-45–L453-83](https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000044595989/LEGISCTA000048626177)

<!-- D06 -->
France taxes digital intermediation and user-data-targeted advertising, including qualifying advertising data transmission. It does not tax every data sale or social/search/streaming business by label. Apply the content, communication, payment, financial-system and advertising-interface exclusions in L453-57–59; exclusively intra-group services are excluded. Test previous-calendar-year collected taxable-service consideration at enterprise/group level: worldwide **over EUR 750 million**, and France-weighted **over EUR 25 million**. The rate is **3%** on current-calendar-year collected consideration weighted by that year’s national footprint, with the excise-linked exclusion.

<!-- D07 -->
France locates the user’s terminal by any means. Footprints differ: qualifying French-user marketplace transactions / all transactions; active accounts opened from France / all active accounts; French-user targeted ad messages / all messages; relevant French-generated data users / all data users. Use the statute’s definitions, not payer location. Convert foreign receipts using the latest EU Official Journal rate known on the receipt month’s first day. Preserve monthly receipts, FX and footprint inputs. [L453-51, 55–56, 62–64, 70–74, 80](https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000044595989/LEGISCTA000048626177).

### Italy: [Law 145/2018 article 1, paragraphs 35–50](https://www.normattiva.it/atto/caricaDettaglioAtto?atto.codiceRedazionale=18G00172&atto.dataPubblicazioneGazzetta=2018-12-31&bloccoAggiornamentoBreadCrumb=true&classica=true&dataVigenza=&generaTabId=true&qId=&tabID=0.9037336842842527&tipoDettaglio=vigente&title=lbl.dettaglioAtto)

<!-- D08 -->
Italy’s tax applies from **2020-01-01** (paragraph 47). Its prior-calendar-year **total worldwide revenue at least EUR 750 million**, individually or at group level, gates the charge on Italian taxable digital revenue. The former **EUR 5.5 million** local threshold was removed from **2025** by Law 207/2024 article 1(21). Taxable current-calendar-year revenue carries **3%**. It covers targeted ads, multilateral interfaces permitting user contact/interaction, and user-generated interface data transmission. Exclude qualifying direct underlying goods/services, own-site sales without intermediation, interfaces mainly/exclusively providing content, communication or payments, the specified regulated financial services/data and specified energy/environmental trading platforms. Controlled/common-control intra-group services are excluded. [Current paragraphs 35-bis–41](https://www.normattiva.it/atto/caricaDettaglioAtto?atto.codiceRedazionale=18G00172&atto.dataPubblicazioneGazzetta=2018-12-31&bloccoAggiornamentoBreadCrumb=true&classica=true&dataVigenza=&generaTabId=true&qId=&tabID=0.9037336842842527&tipoDettaglio=vigente&title=lbl.dettaglioAtto).

<!-- D09 -->
Italy uses ad-view device location; transactional-interface access and transaction participation; account-opening location for other interfaces; and the location where transmitted user data were generated, including earlier years. IP or other geolocation evidence may establish device location. Apply paragraph 40-ter’s separate ad, transaction, account and data fractions. The base is gross of costs and net of VAT/other indirect taxes; exclude economically independent underlying supplies and the specified excise-linked amounts. Monthly records must support receipts and location ratios; convert foreign receipts at the latest Official Journal rate known on the receipt month’s first day. [Paragraphs 39–40-ter, 44-bis](https://www.normattiva.it/atto/caricaDettaglioAtto?atto.codiceRedazionale=18G00172&atto.dataPubblicazioneGazzetta=2018-12-31&bloccoAggiornamentoBreadCrumb=true&classica=true&dataVigenza=&generaTabId=true&qId=&tabID=0.9037336842842527&tipoDettaglio=vigente&title=lbl.dettaglioAtto).

<!-- D10 -->
The planned recodification in Legislative Decree 174/2024 is deferred to **2027-01-01**, not the operative basis for calendar 2026. Use the current Law 145/2018 and amendments. [Decree-Law 200/2025 article 4, as converted by Law 26/2026](https://www.normattiva.it/atto/caricaDettaglioAtto?atto.articolo.numero=4&atto.codiceRedazionale=25G00213&atto.dataPubblicazioneGazzetta=2025-12-31).

### Spain: [Law 4/2020 articles 4–16](https://www.boe.es/buscar/act.php?id=BOE-A-2020-12355)

<!-- D11 -->
Spain’s Law entered into force on **2021-01-16** (final provision 6, three months after publication). It taxes targeted online advertising, online intermediation **including marketplaces**, and transmission of user data generated through digital interfaces. Exclude own-site sales without intermediation, underlying goods/services, interfaces principally providing digital content/communication/payments, specified regulated financial services/data, and services between wholly owned group entities. Test each quarter’s first day using prior-calendar-year worldwide total net turnover **over EUR 750 million** and Spanish taxable digital revenue **over EUR 3 million**; annualise a first year of activity. Article 8 aggregates the article 42 Commercial Code group, including intra-group revenue for the local gate; the taxpayer remains each entity. [Articles 4–8](https://www.boe.es/buscar/act.php?id=BOE-A-2020-12355).

<!-- D12 -->
Spain’s **3%** applies to its article 10 base excluding VAT, with market-value rules for connected transactions subject to the wholly owned exclusion. Advertising uses ad impressions; transactional intermediation uses the relevant user fraction; other interfaces use Spanish-opened accounts’ revenue; data uses the relevant users. Location is the ad-view/transaction/account-opening/data-generation device rule appropriate to the service. IP is rebuttable by other admissible geolocation evidence. **Payment location and the underlying goods/services location are disregarded** for this purpose. Prepayments can trigger tax when collected. Provisional bases require statutory adjustment, not permanent estimation. [Articles 7, 9–11](https://www.boe.es/buscar/act.php?id=BOE-A-2020-12355).

### Austria: [Digital Tax Act guidance](https://www.bmf.gv.at/en/topics/taxation/digital-tax-act.html)

<!-- D13 -->
Austria’s online-advertising tax applies from **2020-01-01** at **5%** where business-year worldwide turnover is **at least EUR 750 million** and Austrian online-advertising turnover **at least EUR 25 million**. Use the specified multinational group aggregation and latest consolidated annual accounts. Turnover from a statutory obligation is excluded. Domestic advertising requires a domestic device, established by IP or other geolocation, **and content/design addressing Austrian users**. Deduct eligible outside-group other online advertisers’ intermediate inputs from domestic turnover and taxable remuneration. Search and social businesses enter through qualifying advertising, not their labels; classic advertising under the separate advertising levy is excluded. [BMF scope, thresholds and base sections](https://www.bmf.gv.at/en/topics/taxation/digital-tax-act.html).

### Turkey: [Law 7194, articles 1–6](https://cdn.gib.gov.tr/api/gibportal-file/file/getFileResources?objectKey=arsiv%2Ffileadmin%2Fuser_upload%2FKanunlar%2F7194.pdf)

<!-- D14 -->
Turkey’s DST provisions took effect **2020-03-01** (article 52(a), the third month after publication). They cover digital advertising and related technical/data services, sales/access to digital content including software, and digital environments enabling user interaction, including marketplaces, plus related digital intermediation. Domestic provision includes performance, benefit, targeting or statutory evaluation in Turkey; the payment/accounting test has its own meaning, and foreign-targeted advertising has an exception. Do not reduce this to a Turkish IP/card test. Taxpayer residence or a local PE does not itself decide liability. Article 4(6) excludes the specified Treasury-share telecom, special-communications-tax, banking, qualifying R&D-centre product and payment services, also excluding their revenue from the gates.

<!-- D15 -->
Under article 4, exemption applies if prior accounting-period in-scope Turkish revenue is **below TRY 20 million OR worldwide in-scope revenue below EUR 750 million** or its lira equivalent; use consolidated-group in-scope totals. If both gates are crossed during the current period, examine cumulative revenue at quarter ends: liability starts in the **fourth taxation period following** the period of crossing. Falling below either gate for **two consecutive accounting periods** restores exemption in the following period. Preserve these timing rules and any required exemption documentation. Exact-equality boundary cases are reserved below. [Article 4](https://cdn.gib.gov.tr/api/gibportal-file/file/getFileResources?objectKey=arsiv%2Ffileadmin%2Fuser_upload%2FKanunlar%2F7194.pdf).

<!-- D16 -->
The rate is **5% from 2026-01-01**, scheduled to become **2.5% from 2027-01-01** under Presidential Decision 10767. The old statutory **7.5%** is not the calendar-2026 rate; article 5(5) permits presidential reduction to **1%** or increase to twice the statutory rate, i.e. **15%**, rather than making the statutory rate automatically current. The base permits no expense, cost or tax deduction; convert foreign revenue at the central bank buying rate when revenue becomes definite, and do not show DST separately on the invoice. Paid DST may be an income/corporation-tax expense under article 6(7), not an automatic tax credit. [GIB rate decision note](https://cdn.gib.gov.tr/api/gibportal-file/file/getFile?objectKey=DUYURU%2FUNIVERSAL%2F2025%2FCK10767_abn.pdf) and [articles 2, 5–6](https://cdn.gib.gov.tr/api/gibportal-file/file/getFileResources?objectKey=arsiv%2Ffileadmin%2Fuser_upload%2FKanunlar%2F7194.pdf).

### Hungary: [Act XXII of 2014](https://njt.jog.gov.hu/jogszabaly/2014-22-00-00)

<!-- D17 -->
The current section 5/A advertising-tax rate is **0%** for liabilities arising from **2019-07-01**; the current consolidated text does not impose the old guide’s end-2025 sunset. Internet ads predominantly in Hungarian or on predominantly Hungarian-language websites are among the statutory advertising activities. The publisher’s residence is not decisive. Section 5’s **HUF 100 million** exemption has de minimis aid conditions; it is not a worldwide DST gate and does not override section 5/A. Section 7(6) exempts a taxpayer with no payment liability from the stated tax/advance declarations; assess other obligations separately. [Sections 2–5/A, 7, 11](https://njt.jog.gov.hu/jogszabaly/2014-22-00-00).

### Kenya: [Income Tax Act section 12E](https://www.kra.go.ke/images/publications/Income-Tax-Act-2026.pdf)

<!-- D18 -->
KRA identifies the replacement of DST by SEPT from **2024-12-27**. Current section 12E covers non-resident service income through internet/electronic-network business, including a digital marketplace, where the user is in Kenya. Exclude services through a PE, income chargeable under sections **9(2) or 10**, and digital services to an airline with government ownership **at least 45%**. The former turnover exemption was deleted in 2025; do not apply the old guide’s KES 5 million gate. Taxable profit is deemed **10% of gross turnover**, taxed at **30%** under Schedule 3 Head B paragraph 12: the resulting gross-equivalent rate is **3%**, not 6%. Do not assume a general CIT credit. [Section 12E; Schedule 3 Head B(12)](https://www.kra.go.ke/images/publications/Income-Tax-Act-2026.pdf); [KRA transition, printed page 7](https://www.kra.go.ke/images/publications/iTax-Enhancements-and-Resolution-of-Defects-for-January-2025-Volume-2.pdf).

<!-- D19 -->
Apply the **2026-07-01** Finance Act overlay before classifying Kenyan digital receipts: the expanded royalty definition covers consideration for the use or right to use any software, proprietary or off-the-shelf, whether in the form of licence, development, training, maintenance or support fees. It also covers use or right to use a proprietary digital payment card network or platform, including access, participation or usage rights through a card; management/professional fee and section 10 source rules also change. A receipt excluded from SEPT can enter another income/withholding regime. Review section 10’s payment, business and source conditions, rather than assigning every software sale to SEPT. [Finance Act 2026 sections 1–2, 7](https://www.kra.go.ke/images/publications/Finance-Act-2026.pdf) and [Income Tax Act sections 2, 9–10, 12E](https://www.kra.go.ke/images/publications/Income-Tax-Act-2026.pdf).

### Nepal: [Finance Act 2083, section 23](https://ird.gov.np/content/13566/economic-act--2083--date-of-publication-in/)

<!-- D20 -->
For Nepal FY **2083/84**, section 23 imposes **2%** on non-residents’ qualifying electronic services to Nepal users and sales of Nepal-user data. Annual turnover **up to NPR 3,000,000** is exempt; this is not a deduction from taxable turnover above the gate. Business-purpose supplies to Nepal business users through digital interfaces are excluded as stated in the Act. The native scanned page expresses the rate and threshold in words. Section 1 makes section 23 operative from **2083 Shrawan 1**; this Guide does not invent a Gregorian conversion. Do not apply the old NPR 2 million figure. [Official Act, printed pages 2 and 9–10, sections 1 and 23](https://ird.gov.np/content/13566/economic-act--2083--date-of-publication-in/).

### Tanzania: [TRA digital service tax](https://www.tra.go.tz/page/digital-service-tax)

<!-- D21 -->
Tanzania’s simplified regime covers a non-resident receiving payments for electronic services from an individual, excluding business recipients. There is **no registration threshold**. The rate changes from **2% to 3% from 2026-07-01**: section 24 of Finance Act 2026 amends the charging rate in section 116, with commencement under section 2. The base is gross payments, not the seller’s profit. Do not apply the new rate to the entire calendar year or confuse it with VAT. [Finance Act 2026 sections 2, 24](https://www.tra.go.tz/images/uploads/acts/THE_FINANCE_ACT%2C_2026.pdf) and [TRA current guidance](https://www.tra.go.tz/page/digital-service-tax).

### Canada and India: closed charges and historical work

<!-- D22 -->
**Canada:** Act 3 of 2026 repeals the Digital Services Tax Act and Regulations with deemed effect from **2024-06-20**, and provides for refunds of paid tax, penalties and interest with the specified interest. CRA says **all related obligations no longer apply**, accounts close automatically, and payments by designated entities are refunded to the particular taxpayers. Do not tell a client that a 2022–2023 catch-up payment, RC4731 filing or current 3% charge remains due. Reconcile any historical payments/refunds, including who actually paid; investigate discrepancies without recreating a repealed liability. [Repeal Act sections 126–128](https://laws-lois.justice.gc.ca/eng/annualstatutes/2026_3/page-20.html); [CRA current instructions, updated 2026-09-01](https://www.canada.ca/en/services/taxes/excise-taxes-duties-and-levies/digital-services-tax.html).

<!-- D23 -->
**India e-commerce levy:** the former **2%** charge only applies to qualifying supplies/services made, provided or facilitated from **2020-04-01 before 2024-08-01**. The cut-off follows supplies, not a blanket cash-receipt date. For a historical review, distinguish Indian residents, Indian-IP transactions and specified non-resident transactions, and apply the INR 2 crore turnover, effectively connected PE, ownership and royalty/technical-service exclusions described in the tax department’s statutory summary. Do not issue a current e-commerce EL computation. [Income Tax Department, section 165A discussion](https://www.incometaxindia.gov.in/equalisation-levy3).

<!-- D24 -->
**India advertising levy:** Finance Act 2025 section 146 excludes specified-service consideration **received or receivable on or after 2025-04-01**. Do not substitute an advertising supply-date test. For earlier consideration the historical **6%** charge concerned a resident business/professional payer or a non-resident payer’s Indian PE paying a non-resident provider; the **INR 100,000** exclusion is aggregate consideration for the previous year, not a per-payment gate. Apply the effectively connected PE and non-business exclusions. Historical payer deduction, remittance, Form 1 and section 40(a)(ib) issues require period-specific reconciliation; they are not ongoing advertising EL on new consideration in 2026. [Final Finance Act 2025 section 146](https://egazette.gov.in/WriteReadData/2025/262125.pdf); [Income Tax Department historical scope and compliance](https://www.incometaxindia.gov.in/equalisation-levy3).

### Other original country rows: limited findings and unresolved implementation

<!-- D25 -->
**Uganda:** URA’s official DT-DST form shows **5%** and separate B2B/B2C sales, with calendar-quarter selection. Its FY2026/27 booklet describes royalty exclusion and software added to royalties. Although that printed booklet contains a pre-assent caveat, URA’s later **2026-09-23** notice confirms the Acts’ commencement at **2026-07-01**. The original **UGX 150 million** DST gate is not supported by the sources recovered here and must not be used. **Not yet confirmed for execution:** complete current section 86 scope/exceptions, the filing/payment deadline and current portal field instructions; do not compute or submit Uganda DST using the form alone. [DT-DST form](https://ura.go.ug/storage/2023/11/ITDigitalServiceTaxReturnFormforNonResidentServiceProviders.pdf); [URA booklet](https://ura.go.ug/en/download/tax-amendments-fy-2026-2027/); [later commencement notice](https://ura.go.ug/en/effective-date-of-the-income-tax-amendment-act-2026-and-the-excise-duty-amendment-act-2026/).

<!-- D26 -->
**Pakistan:** FBR notification **SRO 1366(I)/2025**, under Digital Presence Proceeds Tax Act section 15, exempts otherwise-chargeable digitally ordered goods/services supplied from outside Pakistan from **2025-07-01**. That is a defined exemption, not proof that the whole Act was repealed. **Not yet confirmed for execution:** the original claim of a 5% marketplace DST under Income Tax Ordinance section 6A from July 2024, its de minimis rule, and the complete current interaction of DPPT and other income-tax charges. Do not charge or declare zero on those unconfirmed assumptions. [Actual FBR notification](https://download1.fbr.gov.pk/SROs/20257302072529390SRO1366%28I%292025.pdf).

<!-- D27 -->
**Vietnam:** current Corporate Income Tax Law 67/2025/QH15 article 2 includes relevant non-resident e-commerce/platform business; article 11 delegates revenue-percentage calculation for the specified foreign-enterprise categories. **Not yet confirmed for execution:** the old matrix’s uniform “DST-like CIT typically 5%”, combined VAT/CIT rates, no-threshold assertion and January 2022 start under Decree 91/2022. Route the actual service and recipient to current corporate-income-tax and VAT rules separately. A delegated income-tax calculation is not evidence of a standalone uniform DST. [Government publication of the Law, articles 2–3 and 11](https://en.baochinhphu.vn/law-on-corporate-income-tax-111261014131247153.htm).

<!-- D28 -->
**Tunisia:** **Not yet confirmed for current execution:** the original 3% charge, claimed absence of a threshold, 2020 commencement and current declaration/payment procedure. A reproduced 2019 official Gazette contains Law 2019-78 article 27, describing non-resident software/internet service sales to resident persons and quarterly turnover declarations, with procedures delegated to a decree. Current official tax-authority implementation and amendments were not recovered. Preserve this as a research lead; do not treat absent guidance as a zero charge. [Historical Gazette reproduction on a public university’s website, page 4430](https://utm.rnu.tn/utm/documents/2018-56.pdf).

<!-- D29 -->
**Zimbabwe:** **Not yet confirmed for execution:** the original 5% no-threshold charge, section 12B citation, 2019 commencement, current electronic-commerce operators’ tax scope/threshold, and their interaction with digital-services withholding. ZIMRA’s **Public Notice 50/2026**, issued **2026-09-04**, confirms a separate “Withholding Tax on Digital Services” return configured in TaRMS for changes effective **2026-01-01**. That notice does not establish an electronic-commerce tax rate or prove there is no threshold. Do not infer those missing rules from its portal list. [ZIMRA notice, pages 1–2](https://www.zimra.co.zw/public-notices?download=4539%3Apublic-notice-50-of-2026-new-2026-legislation-changes-deployed-in-tarms).

### Original proposed or paused countries

<!-- D30 -->
**New Zealand:** Inland Revenue marks the named Digital Services Tax Bill **withdrawn/discharged 2025-05-21**, replacing the old “paused 2024” description. This is the status of that bill, not a conclusion about every possible later tax measure. [IRD bill record](https://www.taxpolicy.ird.govt.nz/bills/53-dst-23).

<!-- D31 -->
**Brazil:** the Chamber’s PL 2358/2020 record shows a proposal awaiting a committee opinion. **Belgium:** Chamber document 56K1491/001 is a bill dated **2026-04-17**. Neither document alone proves an enacted current charge or a blanket current exemption. The original broad pending/never-enacted/paused labels remain **Not yet confirmed** beyond these identified instruments. [Brazil bill record](https://www.camara.leg.br/proposicoesWeb/fichadetramitacao?idProposicao=2251395); [Belgian bill cover](https://www.lachambre.be/flwb/pdf/56/1491/56K1491001.pdf).

<!-- D32 -->
**Norway:** the Finance Minister’s **2026-08-10** parliamentary answer describes further study of a possible DST and subsequent follow-up. **Czech Republic:** Parliament’s old print 658 record establishes a proposal and committee history, not the old guide’s claimed 2021 withdrawal. **Not yet confirmed:** their current complete legislative status after those records, including the old “never enacted” assertion for Norway. Do not turn historical bill pages into present no-tax advice. [Norwegian answer](https://stortinget.no/no/Saker-og-publikasjoner/Sporsmal/Skriftlige-sporsmal-og-svar/Skriftlig-sporsmal/?qnid=126787); [Czech print 658](https://www.psp.cz/sqw/tisky.sqw?O=8&T=658).

<!-- D33 -->
**Poland:** UKE’s **2026-11-12** notice describes a distinct audiovisual-on-demand contribution under Cinema Act article 19(6a): **1.5%** of the higher of access/subscription revenue or advertising revenue, with the specified microenterprise and audience exemptions, including the **1%** audience test; foreign EU providers use Polish revenue. Payment is quarterly within **30 days**. This is not proof that the original general-DST proposal was paused or enacted. **Not yet confirmed:** current general-DST proposal status and complete qualification for executing the audiovisual charge. [UKE notice](https://uke.gov.pl/akt/obowiazek-wplat-na-rzecz-pisf,718.html).

<!-- D34 -->
**Slovakia:** the Finance Ministry’s **2018-01-05** item describes platform PE registration for repeated transport/accommodation intermediation, with withholding if registration is omitted. That is not proof of a separate turnover DST or a currently paused bill. **Indonesia:** the DGT’s older digital-tax Q&A addresses VAT appointment and refers to possible future ETT identification; it does not establish a current ETT charge or prove that DST was “converted into VAT”. **Not yet confirmed:** both old current-status assertions. Keep PE/WHT and VAT analysis separate. [Slovak item](https://www.mfsr.sk/sk/media/tlacove-spravy/digitalne-platformy-budu-slovensku-musiet-platit-dane.html); [DGT Q&A](https://www.pajak.go.id/en/digital-tax-questions-and-answers).

### Allocation, tax base and international changes

For the original mixed-country scenario, identify a **UK advertiser targeting a French user through a Spanish platform**. First identify the service and supplier; the platform’s Spanish incorporation does not establish a Spanish user. A targeted ad may enter France through French-device impressions; Spanish allocation needs the Spanish statutory user nexus; UK advertising must be connected with a qualifying UK digital-services activity and allocated under its own cases. Run each country’s threshold and exclusions separately. No numerical answer is possible without revenue, service and user metrics. Multiple charges may be possible; do not presume a universal pro-rata split, credit or netting rule.

Compute each applicable tax using its own base: recognised revenue, collected consideration or payments as required, rather than one global spreadsheet basis. Apply only that jurisdiction’s exclusions, allowance and relief. Keep tax deductions distinct from tax credits. Keep VAT accounting separate: neither a VAT exemption nor a VAT collection duty decides DST liability, and this Guide authorises no cross-tax netting. Model the actual contract’s commercial incidence without assuming that every DST is charged to consumers.

<!-- D35 -->
The OECD Amount A page describes its text as **not yet open to signature**, released **2023-10-11**. It is not a 2024 enacted convention or an automatic domestic repeal. Use each country’s actual operative amendment before stopping a DST. The USTR’s **2026 Trade Policy Agenda** identifies DST concerns and possible enforcement, including evaluation of further section 301 investigations. It does not itself impose a tariff or establish that all older tariffs remain suspended. Assess an actual trade measure separately by effective date, country and product; political statements do not suspend a tax filing. [OECD status and documents](https://www.oecd.org/en/topics/sub-issues/reallocation-of-taxing-rights-to-market-jurisdictions/multilateral-convention-to-implement-amount-a-of-pillar-one.html); [USTR agenda, printed page 5](https://ustr.gov/sites/default/files/files/Press/Releases/2026/2026%20Trade%20Policy%20Agenda.pdf).

## Boundary and exception table

| Situation | Required treatment |
| --- | --- |
| Own goods, direct SaaS, payment processing, content or standalone data | Apply each named service definition and exception; do not borrow another country’s carve-out. Turkey’s content/software scope is wider than the European targeted-ad/intermediation models. |
| Global revenue passes but local gate fails | Apply the specific country’s exemption and testing period; do not charge merely because a group meets CbCR. |
| Group passes; a small subsidiary supplies the service | Determine entity liability and authorised filing arrangements separately; Spain does not become a group taxpayer. |
| Loss-making supplier | Consider the UK election with supported category margins; do not deduct all costs from other countries’ turnover bases. |
| Rate, repeal or scope change within the period | Split by the legally relevant event and date; retain the transition reconciliation. |
| Conflicting locations, missing metrics or unknown implementation | Stop the numerical conclusion for that country; resolve the evidence or refer with the precise open item. |

## Worked cases

### UK: choose whether to elect the alternative calculation

<!-- D36 -->
Assume a full-year qualifying group has **GBP 600,000,000** digital revenue worldwide and **GBP 30,000,000** attributable UK search revenue; it passes both gates. There is only this category, no cross-border relief, and its supported UK operating margin is **1%**. After the **GBP 25,000,000** allowance the net revenue is **GBP 5,000,000**. General DST is **GBP 100,000**; a valid alternative election produces **GBP 40,000**, saving **GBP 60,000**. Subject to validating the expenses and election, electing is beneficial on these facts. At a gate exactly equal to, rather than exceeding, the statutory threshold, this calculation would not be triggered. [Sections 46–49](https://www.legislation.gov.uk/ukpga/2020/14/part/2).

```oa-check
name: UK DST general charge versus category election (2026)
inputs:
  worldwide_digital_revenue: 600000000
  uk_revenue: 30000000
  allowance: 25000000
  operating_margin: 0.01
steps:
  global_excess: worldwide_digital_revenue - 500000000
  local_excess: uk_revenue - allowance
  net_revenue: max(0, uk_revenue - allowance)
  general_tax: net_revenue * 0.02
  elected_tax: net_revenue * operating_margin * 0.8
  election_saving: general_tax - elected_tax
expected:
  global_excess: 100000000
  local_excess: 5000000
  net_revenue: 5000000
  general_tax: 100000
  elected_tax: 40000
  election_saving: 60000
```

### Italy: the removed local gate and an advance payment

<!-- D37 -->
Assume prior-calendar-year total group revenue **EUR 800,000,000**, current qualifying Italian digital revenue **EUR 1,000,000**, no exclusions, and prior-year DST **EUR 20,000**. The global gate passes, and the former local gate does not exempt this revenue. Current DST at **3%** is **EUR 30,000**. The statutory advance of **30%** of prior-year DST is **EUR 6,000**, leaving **EUR 24,000** after crediting that advance against the current-year tax. Keep the prior-year tax input separate from current receipts. These are illustrative facts, not a holiday-adjusted filing calendar. [Law 145/2018 article 1(36), (41)–(42)](https://www.normattiva.it/atto/caricaDettaglioAtto?atto.codiceRedazionale=18G00172&atto.dataPubblicazioneGazzetta=2018-12-31&bloccoAggiornamentoBreadCrumb=true&classica=true&dataVigenza=&generaTabId=true&qId=&tabID=0.9037336842842527&tipoDettaglio=vigente&title=lbl.dettaglioAtto).

```oa-check
name: Italy DST after local threshold removal (2026)
inputs:
  prior_global_revenue: 800000000
  current_italian_digital_revenue: 1000000
  prior_year_tax: 20000
steps:
  global_gate_margin: prior_global_revenue - 750000000
  current_tax: current_italian_digital_revenue * 0.03
  advance: prior_year_tax * 0.30
  balance: current_tax - advance
expected:
  global_gate_margin: 50000000
  current_tax: 30000
  advance: 6000
  balance: 24000
```

## When to refuse or refer

Do not compute a country’s liability while its service classification, current operative law, threshold conditions or user evidence is unresolved. Refer financial marketplaces, bundled software/royalty/services, regulated payment services and disputed group/control or anti-avoidance questions with the actual contracts and revenue allocation. Do not propose entity moves to escape DST without the affected countries’ anti-avoidance review. Do not treat a proposal, a delegated rate or an unavailable source as an enacted charge, an exemption or confirmation of zero tax.

Do not apply one country’s attribution rules, revenue period, FX convention or deduction to another. Do not stop a current return because of Amount A negotiations or tariff threats. Do not demand a Canadian retroactive DST payment after the repeal. Preserve India historical withholding and deduction issues for the correct periods, without describing the closed levies as current. Every item explicitly labelled **Not yet confirmed** below is outside usable calculation and filing instructions.

## Filing and payment

<!-- D38 -->
**UK:** notify/register within **90 days** after the first qualifying accounting-period end. The responsible member is a validly nominated company in the group or otherwise the parent. File the group return online within **12 months** of period-end; pay within **9 months and 1 day**. These are different deadlines; the old quarterly percentage schedule is unsupported. HMRC requests entity liability, allowance, category election/margin and relief information; use the consolidated-accounts FX policies/rates. Filing continues for later periods unless HMRC directs otherwise under section 56. [Act sections 51–56](https://www.legislation.gov.uk/ukpga/2020/14/part/2); [return guide](https://www.gov.uk/guidance/submit-a-digital-services-tax-return); [payment guide](https://www.gov.uk/guidance/pay-your-digital-services-tax).

<!-- D39 -->
**Italy:** paragraph 42 provides an advance of **30%** of the previous calendar year’s tax by **30 November** of the current year, balance by **16 May** of the following year, and annual return by **30 June**. For companies in the same group, paragraph 42 requires appointment of a single group company to fulfil the DST obligations; do not presume that all groups file one return in all countries. Paragraph 43 requires a DST identification number where the specified non-resident has neither a PE nor VAT number, and a fiscal representative for the specified non-EU/non-EEA/no-assistance cases, with the stated resident-group joint liability. **Not yet confirmed here:** current F24 codes, electronic return boxes and business-day extensions. Do not execute payment from the old “single payment/F24” row. [Paragraphs 42–44-bis](https://www.normattiva.it/atto/caricaDettaglioAtto?atto.codiceRedazionale=18G00172&atto.dataPubblicazioneGazzetta=2018-12-31&bloccoAggiornamentoBreadCrumb=true&classica=true&dataVigenza=&generaTabId=true&qId=&tabID=0.9037336842842527&tipoDettaglio=vigente&title=lbl.dettaglioAtto).

<!-- D40 -->
**Spain:** file **Modelo 490** electronically, quarterly, during the **month following the calendar quarter**; direct debit closes **5 days earlier**, subject to the actual applicable calendar. The AEAT instructions require recognised electronic certificates and identify taxpayer, non-EU representative where required, period, group and parent details. Reconcile the advertising/intermediation/data bases and tax and any adjustments to the proper fields; include the territorial allocation where relevant. Article 13 requires NIF/census formalities, records and location evidence. [AEAT instructions, pages 1–4](https://sede.agenciatributaria.gob.es/static_files/Sede/Procedimiento_ayuda/GC45/castellano/Instrucciones_490.pdf); [Law article 13–14](https://www.boe.es/buscar/act.php?id=BOE-A-2020-12355).

<!-- D41 -->
**Austria:** pay self-assessed monthly tax by the **15th of the second following month** and file the annual return within **3 months** after business-year end. Use the digital-tax procedure, normally FinanzOnline; BMF describes an electronic online procedure if neither taxpayer nor representative participates in FinanzOnline. Each taxpayer needs its own tax number. Apply the stated mandatory fiscal-representative rule for persons without EU/EEA office, management or PE; the representative must participate in FinanzOnline. Do not use the old U30/month-after deadline. [Digital Tax Act section 5](https://ris.bka.gv.at/Dokumente/Bundesnormen/NOR40224234/NOR40224234.html); [BMF registration and filing guidance](https://www.bmf.gv.at/en/topics/taxation/digital-tax-act.html).

<!-- D42 -->
**Turkey:** article 6 ordinarily uses calendar months, with authority for specified quarterly periods. The return and payment are due by the **end of the following month**; the provider or a legally designated withholding-responsible person files as applicable. **Not yet confirmed here:** current electronic form naming, boxes, registration instructions and particular deadline extensions. The original translated form name is not an execution instruction. [Article 6](https://cdn.gib.gov.tr/api/gibportal-file/file/getFileResources?objectKey=arsiv%2Ffileadmin%2Fuser_upload%2FKanunlar%2F7194.pdf).

<!-- D43 -->
**Kenya:** section 12E requires the return and payment by the **20th of the month after the month the service was offered**. Preserve the old DST ledger separately from SEPT through the transition. **Not yet confirmed here:** current SEPT electronic return fields, any implementing-regulation user-location refinements and applicable extensions; do not borrow the VAT filing path. [Section 12E(5)](https://www.kra.go.ke/images/publications/Income-Tax-Act-2026.pdf); [KRA transition notes](https://www.kra.go.ke/images/publications/iTax-Enhancements-and-Resolution-of-Defects-for-January-2025-Volume-2.pdf).

<!-- D44 -->
**Nepal:** section 23 requires annual turnover declaration and tax within **3 months** of fiscal-year end through the prescribed electronic procedure. The retrieved IRD procedure 2082 supplies historical registration/return mechanics, but its continuation and exact current portal fields under the 2083 Act have not been confirmed here. **Not yet confirmed for execution:** present registration deadline, procedure version, form fields and payment route. Use the verified annual statutory deadline to raise an action item, not to invent a portal submission. [Finance Act 2083 section 23(2)](https://ird.gov.np/content/13566/economic-act--2083--date-of-publication-in/); [IRD procedure 2082 record](https://ird.gov.np/content/13525/procedures-relating-to-digital-service-tax-2082/).

<!-- D45 -->
**Tanzania:** register through the Commissioner’s simplified online portal; TRA says file/pay by the **20th of the next month**, with EFD exemption for this regime. Payment can be in Tanzanian shillings or convertible currency, with the Bank of Tanzania payment-date exchange rate. **Not yet confirmed here:** the current return’s box identifiers and any taxpayer-specific extension. [TRA registration, filing, currency and EFD sections](https://www.tra.go.tz/page/digital-service-tax).

<!-- D46 -->
**France:** CIBS L453-82 requires advances. The official **October 2026 calendar** lists a second TSN advance, with the applicable deadline depending on the taxpayer’s VAT/non-VAT situation; the non-VAT due date is in the professional account. **Not yet confirmed here:** complete current annual declaration deadline, present forms/lines, first-advance deadline and percentage calculation. The old “25 October annual return; April/October 50% each” is not usable without that current procedural proof. [CIBS L453-79–82](https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000044595989/LEGISCTA000048626177); [DGFiP October calendar](https://www.impots.gouv.fr/calendrier-fiscal/2026-10).

For Canada, follow the repeal/refund instructions above. For India, isolate old consideration/supply periods, payer deductions, remittances and statements before deciding whether any historical amendment remains necessary. For Hungary, apply the current zero-rate declaration exception above. For Uganda, Pakistan, Vietnam, Tunisia, Zimbabwe and unresolved proposal jurisdictions, the specific source gaps above prevent filing instructions here. No penalty discount, enforcement tolerance or filing safe harbour has been established by this matrix. Record any actual late-filing, late-payment or understatement exposure as requiring its own operative source before computing it.

## Completion checklist

The review file must contain the entity/group scope and prior/current revenue gate, each service classification and exclusion, country user-location calculation and evidence, tax base and FX reconciliation, local-currency liability and any election alternatives, historical transition/refund reconciliation, and payment/advance/return calendar with the actual form and portal. Distinguish a verified statutory date from unresolved portal or holiday instructions. Include current Amount A and trade-measure findings without assuming repeal; list India historical withholding/deduction and Kenya/Uganda royalty interactions separately.

Before delivery, confirm that group testing has not become an invented group filer, thresholds have not become invented allowances, all UK election costs and margins are supported, revenue recognition/receipts and user fractions follow each country, and rate changes split the correct event dates. Every unresolved item needs its precise missing document or fact and a referral owner. Keep the Canada refund reconciliation instead of the obsolete catch-up liability. Every output must be reviewed and signed off by a credentialed practitioner in each source country before a return is filed. This Guide provides informational and computational material and does not itself constitute tax, legal or financial advice.

## Sources

Official pages and operative provisions were read on **2026-11-15**, with earlier personally read material reused only where stated in the writer’s evidence register. Current-law sources are linked beside their rules. Historical documents and proposals are explicitly identified. The Nepal scanned Act was read visually; its native dates and values written in words are preserved. Source access failures and incomplete current-law recoveries are not approvals.

| Source | Operative scope actually read | Read date | Official URL |
| --- | --- | --- | --- |
| at | Read for General information; Who is the tax debtor?; Assessment basis and tax rate; Submission of tax returns; Registration; Fiscalrepresentative | 2026-11-15 | [Official source](https://www.bmf.gv.at/en/topics/taxation/digital-tax-act.html) |
| atlaw | Read for §5(1); §5(3) | 2026-11-15 | [Official source](https://ris.bka.gv.at/Dokumente/Bundesnormen/NOR40224234/NOR40224234.html) |
| be | Read for Coverp1 | 2026-11-15 | [Official source](https://www.lachambre.be/flwb/pdf/56/1491/56K1491001.pdf) |
| br | Read for Billstatus | 2026-11-15 | [Official source](https://www.camara.leg.br/proposicoesWeb/fichadetramitacao?idProposicao=2251395) |
| ca | Read for CurrentInstructions; Refundinstructions | 2026-11-15 | [Official source](https://www.canada.ca/en/services/taxes/excise-taxes-duties-and-levies/digital-services-tax.html) |
| calaw | Read for s126–127; s128 | 2026-11-15 | [Official source](https://laws-lois.justice.gc.ca/eng/annualstatutes/2026_3/page-20.html) |
| cz | Read for Print658record | 2026-11-15 | [Official source](https://www.psp.cz/sqw/tisky.sqw?O=8&T=658) |
| es | Read for arts4–5; art6(a)–(f); art8(1); art8(1),lastsentence;art8(3); Final provision6; art7(2)–(4); art7(4); art9; art10(1); art10(2); art10(3); art11; art13 | 2026-11-15 | [Official source](https://www.boe.es/buscar/act.php?id=BOE-A-2020-12355) |
| esfile | Read for pp1–3; p3 | 2026-11-15 | [Official source](https://sede.agenciatributaria.gob.es/static_files/Sede/Procedimiento_ayuda/GC45/castellano/Instrucciones_490.pdf) |
| fr | Read for L453-46–47; L453-47; L453-57–59; L453-58; L453-59; L453-60; L453-61(2); L453-64; L453-65; L453-66; L453-70; L453-73; L453-51; L453-55; L453-56; L453-62; L453-63; L453-74; L453-80; L453-82 | 2026-11-15 | [Official source](https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000044595989/LEGISCTA000048626177) |
| frcalendar | Read for October2026TSNentry | 2026-11-15 | [Official source](https://www.impots.gouv.fr/calendrier-fiscal/2026-10) |
| hu | Read for 5/A§; 2§(1)(e),3§; 3§(1); 5§(3)–(4); 7§(6) | 2026-11-15 | [Official source](https://njt.jog.gov.hu/jogszabaly/2014-22-00-00) |
| id | Read for ETTidentityQ&A | 2026-11-15 | [Official source](https://www.pajak.go.id/en/digital-tax-questions-and-answers) |
| in2025 | Read for s146(b),inserted165(3) | 2026-11-15 | [Official source](https://egazette.gov.in/WriteReadData/2025/262125.pdf) |
| india | Read for Transactions/165Adiscussion; 165Aexceptions; 165Anexus; Royalty/FTSexception; 165historicalsummary; 165payerandexclusions | 2026-11-15 | [Official source](https://www.incometaxindia.gov.in/equalisation-levy3) |
| it | Read for art1(36); art1(37); art1(37-bis); art1(37-bis)(c)–(f); art1(38); art1(41); art1(47); art1(39)–(39-ter); art1(40); art1(40-bis); art1(40-ter); art1(44-bis); art1(42); art1(43); art1(42),group-company sentence | 2026-11-15 | [Official source](https://www.normattiva.it/atto/caricaDettaglioAtto?atto.codiceRedazionale=18G00172&atto.dataPubblicazioneGazzetta=2018-12-31&bloccoAggiornamentoBreadCrumb=true&classica=true&dataVigenza=&generaTabId=true&qId=&tabID=0.9037336842842527&tipoDettaglio=vigente&title=lbl.dettaglioAtto) |
| it207 | Read for art1(21)(a) | 2026-11-15 | [Official source](https://www.gazzettaufficiale.it/atto/serie_generale/caricaArticoloDefault/originario?atto.codiceRedazionale=24G00229&atto.dataPubblicazioneGazzetta=2024-12-31&atto.tipoProvvedimento=LEGGE) |
| itdefer | Read for art4(2) | 2026-11-15 | [Official source](https://www.normattiva.it/atto/caricaDettaglioAtto?atto.articolo.numero=4&atto.codiceRedazionale=25G00213&atto.dataPubblicazioneGazzetta=2025-12-31) |
| ke | Read for 12E(1)–(2); 12E(3); 12E(4); Schedule3HeadB(12); s10(1),provisos; 12E(5) | 2026-11-15 | [Official source](https://www.kra.go.ke/images/publications/Income-Tax-Act-2026.pdf) |
| kefin | Read for s1; s2 royalty definition; s2 managementprofessionalfee | 2026-11-15 | [Official source](https://www.kra.go.ke/images/publications/Finance-Act-2026.pdf) |
| ketrans | Read for printedp7 | 2026-11-15 | [Official source](https://www.kra.go.ke/images/publications/iTax-Enhancements-and-Resolution-of-Defects-for-January-2025-Volume-2.pdf) |
| no | Read for Answer10Aug2026 | 2026-11-15 | [Official source](https://stortinget.no/no/Saker-og-publikasjoner/Sporsmal/Skriftlige-sporsmal-og-svar/Skriftlig-sporsmal/?qnid=126787) |
| nppagepdf0 | Read for Act2083§23(1),printedp9; Act2083§23(1)(a),printedp9; Act2083§23(1)(b),printedp9; Act2083§23(2),printedp9; Act2083§1(2),printedp2 | 2026-11-15 | [Official source](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A9%20(%E0%A4%B0%E0%A4%BE%E0%A4%9C%E0%A4%AA%E0%A4%A4%E0%A5%8D%E0%A4%B0%E0%A4%AE%E0%A4%BE%20%E0%A4%AA%E0%A5%8D%E0%A4%B0%E0%A4%95%E0%A4%BE%E0%A4%B6%E0%A4%BF%E0%A4%A4%20%E0%A4%AE%E0%A4%BF%E0%A4%A4%E0%A4%BF%20%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A9%E0%A5%A4%E0%A5%A6%E0%A5%A9%E0%A5%A4%E0%A5%A9%E0%A5%A6)_vzvsbtv.pdf) |
| nz | Read for Billrecordstatus | 2026-11-15 | [Official source](https://www.taxpolicy.ird.govt.nz/bills/53-dst-23) |
| oecd | Read for About/Keydocuments | 2026-11-15 | [Official source](https://www.oecd.org/en/topics/sub-issues/reallocation-of-taxing-rights-to-market-jurisdictions/multilateral-convention-to-implement-amount-a-of-pillar-one.html) |
| pkexempt | Read for SRO1366(I)/2025operative; SROcommencement | 2026-11-15 | [Official source](https://download1.fbr.gov.pk/SROs/20257302072529390SRO1366%28I%292025.pdf) |
| pl | Read for Notice12Nov2026,Art19(6a); Art19(6c); Art19(8) | 2026-11-15 | [Official source](https://uke.gov.pl/akt/obowiazek-wplat-na-rzecz-pisf,718.html) |
| sk | Read for 5Jan2018item | 2026-11-15 | [Official source](https://www.mfsr.sk/sk/media/tlacove-spravy/digitalne-platformy-budu-slovensku-musiet-platit-dane.html) |
| tnhist | Read for Law2019-78Art27,p4430 | 2026-11-15 | [Official source](https://utm.rnu.tn/utm/documents/2018-56.pdf) |
| tr | Read for Current GIB2026/2027 sheet, threshold paragraph | 2026-11-15 | [Official source](https://cdn.gib.gov.tr/api/gibportal-file/file/getFileResources?objectKey=arsiv%2Fyardim-kaynaklar%2Fyararli-bilgiler%2FDijital_hizmet_vergisi.pdf) |
| trarticles | Read for Article4(1),record9485,updated13Feb2026; Article4(2),record9485,updated13Feb2026; Article5(3),record9486,updated13Feb2026 | 2026-11-15 | [Official source](https://gib.gov.tr/api/gibportal/mevzuat/madde/findByKanunId?kanunId=465&status=2&page=0&size=2000&sortFieldName=id&sortType=ASC) |
| trgazette | Read for art1(1)–(2); art2(ç); art3(1); art4(6); art52(a); art4(1); art4(2); art4(3); art4(5); art5(3),(5); art2(c);art5(1)–(2); art6(7); art6(1),(3),(6) | 2026-11-15 | [Official source](https://cdn.gib.gov.tr/api/gibportal-file/file/getFileResources?objectKey=arsiv%2Ffileadmin%2Fuser_upload%2FKanunlar%2F7194.pdf) |
| trnote | Read for Decision10767 explanation | 2026-11-15 | [Official source](https://cdn.gib.gov.tr/api/gibportal-file/file/getFile?objectKey=DUYURU%2FUNIVERSAL%2F2025%2FCK10767_abn.pdf) |
| tz | Read for IncomeTax/Registrationsections; Registration; FilingPayment(2)–(3); FilingPayment(6)–(7) | 2026-11-15 | [Official source](https://www.tra.go.tz/page/digital-service-tax) |
| tzlaw | Read for s24; s2 | 2026-11-15 | [Official source](https://www.tra.go.tz/images/uploads/acts/THE_FINANCE_ACT%2C_2026.pdf) |
| ugnotice | Read for 23Sep2026notice | 2026-11-15 | [Official source](https://ura.go.ug/en/effective-date-of-the-income-tax-amendment-act-2026-and-the-excise-duty-amendment-act-2026/) |
| ugpdf | Read for printedp6 | 2026-11-15 | [Official source](https://ura.go.ug/en/download/tax-amendments-fy-2026-2027/?wpdmdl=71392&refresh=6af987999dc3f1794738073) |
| ugreturn | Read for FormDT-DST,onepage | 2026-11-15 | [Official source](https://ura.go.ug/storage/2023/11/ITDigitalServiceTaxReturnFormforNonResidentServiceProviders.pdf) |
| ukfile | Read for When to submit; ConvertamountstoGBP | 2026-11-15 | [Official source](https://www.gov.uk/guidance/submit-a-digital-services-tax-return) |
| uklaw | Read for s43(2)–(3); s43(4); s43(5)–(8); s45(1)–(3); s61(2); s46(1)–(2); s47(3)–(5); s57(1)–(4); s61–63; s44(2)–(3); s41(4)–(8); s41(9)–(10); s48(1)–(3); s48(4), steps3–5; s49(2)–(4); s50(1)–(5); s65(1)–(4); s54(4); s52; s51; s56(2)–(4) | 2026-11-15 | [Official source](https://www.legislation.gov.uk/ukpga/2020/14/part/2) |
| ust | Read for printedp5 | 2026-11-15 | [Official source](https://ustr.gov/sites/default/files/files/Press/Releases/2026/2026%20Trade%20Policy%20Agenda.pdf) |
| vn | Read for Law67/2025Art2; Art11(2)(a) | 2026-11-15 | [Official source](https://en.baochinhphu.vn/law-on-corporate-income-tax-111261014131247153.htm) |
| zwportal | Read for Notice50/2026pp1–2 | 2026-11-15 | [Official source](https://www.zimra.co.zw/public-notices?download=4539%3Apublic-notice-50-of-2026-new-2026-legislation-changes-deployed-in-tarms) |

### Not yet confirmed: remaining original historical and procedural assertions

<!-- D47 -->
The original description’s assertion of coverage across **25+ jurisdictions** has not been established as a current exhaustive count. The original introduction’s claimed repeal of an Austrian DST proposal and unspecified Spanish IDSD provisions discussed in 2025 has not been confirmed. Neither claim changes the current Austrian or Spanish rules above. The original historical commencement assertions for France (2019-01-01), Nepal (March 2022), Tanzania (2022-07-01), Uganda (2023-07-01) and the old Kenyan DST’s 1.5% rate and 2021-01-01 start have not been established from the recovered operative primary material for those earlier periods. They are retained as individual historical research questions, not dates for a historical computation. For France the old CGI article 299 citations must not replace the current CIBS source.

<!-- D48 -->
The old UK quarterly payment percentages **5%, 17.5%, 32.5% and 45%** are unsupported and must not be used; the verified UK payment rule is above. France’s old annual **25 October** deadline, **3310-A-SD/3310-CA3** form references and **April/October 50% each** advance formula remain individually unconfirmed for current execution. The old Italian F24 implementation is unconfirmed here; the corrected statutory advance/balance dates prevail. No universal annual-average or period-end FX rule, automatic group-nominated filer, general treaty credit or exemption for a loss-making platform has been established. For India historical advertising EL, the precise statutory deduction timing and current handling of old Form 1/section 40(a)(ib) cases require the applicable period’s operative provisions; do not repeat the original payment-only deduction assertion as a current rule.


<!-- D49 -->
**Turkey threshold equality and testing period:** the current official GIB article 4(1) exempts a provider if either prior-accounting-period gate is **below** TRY 20 million or EUR 750 million; article 4(2) ends the exemption when **both** gates are exceeded during the current period, tested on cumulative revenue at quarter ends, with liability starting from the fourth tax period following the crossing period. Those are different period-specific comparisons. The GIB 2026/2027 summary uses not-exceeded wording; do not replace the operative article with that shorthand. **Not yet confirmed for execution:** the application to a particular equality case until the taxpayer’s prior/current testing period and cumulative revenue evidence are established. The current articles were personally recovered and read, including article 5’s rate annotation; the former unreadability statement is superseded. [Current official article 4](https://gib.gov.tr/mevzuat/kanun/465/madde/9485); [current article 5](https://gib.gov.tr/mevzuat/kanun/465/madde/9486).
